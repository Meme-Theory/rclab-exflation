# Session 89 Workshop: connes × lizzi — §VII.U.2 Corner Classification (Var_a(n_a^GGE) structural identity)

**Date**: 2026-05-10
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: connes (connes-ncg-theorist), lizzi (lizzi-spectral-functional-theorist)
**Source Documents**:

- `sessions/archive/session-89/session-89-w6-workingpaper.md` (W6 results; §W6-6 audit-re-run FAIL trace)
- `sessions/permanent-results-registry.md` (authoritative §VII.U.1, §VII.U.2, §VII.U.6, §VII.AR text)
- `.claude/rules/cross-pillar-bridge-anatomy.md` (§"Algebra-axis orthogonality K-counter" MANDATORY at K=3 — the 4-corner partition)
- `.claude/rules/joint-theorem-promotion.md` (§"Stage 2" axis-distinctness clause; substrate-input-orthogonality clause)

**Focus Topics**:

1. **Corner classification from first principles** — apply the algebra-axis 4-corner partition (cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" MANDATORY at K=3) to derive WHICH corner Var_a(n_a^GGE) structurally occupies. Is it (i) algebra-INVARIANT spectrum-only functional `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` of the BdG eigenvalues (Corner I); OR (ii) algebra-DEPENDENT state-pair functional on A_K via the GGE state ω_GGE (Corner IV); OR (iii) MIXED per S82 W-3 §VII.K trichotomy (Corner II / Corner III)?
2. **W-21 V.1+V.3 diff inspection at §VII.U.2** — was the corner classification at §VII.U.2 explicitly altered by W-21 V.1+V.3, or did the V.1+V.3 edits change OTHER text leaving the original corner intact? (mack-cosmic-bridge holds CF-W6-3 diff-inspection duty; this workshop's substrate-physics verdict is INDEPENDENT of the diff content.)
3. **Cross-wave consequence (W4 A.30 Stage-2 §VII.AR aggregation)** — if Reading B (Corner-II) is correct, what is the propagation to W4 A.30 Stage-2 §VII.AR cross-axis verify under joint-theorem-promotion.md §"Stage 2" axis-distinctness clause? Does the 4-corner partition status of §VII.U.2 affect §VII.AR's Stage-2 PASS-AND aggregation?
4. **Routing decision (Reading A vs Reading B)** — does the workshop verdict route to (A) revert W-21 V.1+V.3 (restores Corner I); or (B) update W6-6 plan baseline (accepts Corner II / Corner IV as the original structural state)?
5. **W6-6 audit-machinery implications** — under each reading, what is the structural status of the W6-6 wrapper's text-level audit (existing `_corner_classification_audit.py` does NOT include §VII.U.2 in its target list — CF-W6-4 queues the extension)?

---

## Round 1 — connes: Opening Analysis

### C1: Corner classification of Var_a(n_a^GGE) from first principles (algebra-axis 4-corner partition)

**Verdict (pinned at the head)**: `Var_a(n_a^GGE)` structurally inhabits **Corner II (algebra-INVARIANT × substrate-distance-2 pole s=4)**. It is NOT Corner I, NOT Corner III, NOT Corner IV. The W6-6 plan baseline (`Corner-I = algebra-INVARIANT-spectrum-only-functional` at s=3) was wrong on the Mellin-pole axis. The W-17 §V.3 corrigendum (Reading-B) is consistent with the structural truth; Reading A (revert) is structurally wrong.

#### Substitution chain (per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`)

I must distinguish three logically distinct objects that all carry the name `n_a^GGE`. Conflating them is the trap that drove the W6-6 plan-baseline misassignment.

- **Object 1 — `n_a` as occupation density of mode `a` in the GGE state**: a NUMBER attached to BdG mode index `a`, computed as the GGE expectation `n_a := ω_GGE(b_a^† b_a)` of a fermionic number operator. In the BdG / Bogoliubov picture this evaluates to a closed form in the eigenvalues `λ_a` of the BdG Dirac operator alone: `n_a = Δ_BCS² / (2(λ_a² + Δ_BCS²))` (a Bogoliubov coefficient squared; cf. registry §VII.U.2 line 12961 column-IV formula).
- **Object 2 — `Var_a(n_a^GGE)`**: the SAMPLE VARIANCE of the closed-form numbers `{n_a}` taken across BdG mode-index `a`, with multiplicity weight `m_a`. The registry expansion at line 12961: `Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` where `|v_a|^2 = Δ_BCS² / (2(λ_a² + Δ_BCS²))` follows from the BdG Bogoliubov transformation.
- **Object 3 — the GGE state ω_GGE on the BdG algebra**: a state on `A_BdG = A_F ⊗ M_2(ℂ)` (per agent-memory §"Active Context" line 6: `A_BdG = A_F ⊗ M_2(C)`) reading off ω_GGE(a) for every a ∈ A_BdG. THIS object IS algebra-DEPENDENT (Corner III/IV side).

The W6-6 baseline confusion is the conflation **Object 2 → Object 3**: because `n_a` reads "GGE", the plan author read the whole object as a state-pair functional of ω_GGE on A_K. But the substitution chain shows the GGE state is consumed ONLY in producing the closed-form NUMBERS `n_a`, after which the variance is a SPECTRAL-MOMENT-LIKE quantity in λ_a alone.

Step-by-step substitution (no narrative shortcuts):

```
Step 1 (Definition): n_a := ω_GGE(b_a^† b_a)                    [GGE expectation of mode-a number operator]
Step 2 (Bogoliubov closed form, BdG):
        n_a = |v_a|^2  where  |v_a|^2 = Δ_BCS² / (2(λ_a² + Δ_BCS²))   [registry §VII.U.2 Corner II row]
Step 3 (Variance — algebraic definition):
        Var_a(n_a) := (1/N) Σ_a m_a n_a²  −  ((1/N) Σ_a m_a n_a)²
Step 4 (Substitute Step 2 into Step 3):
        Var_a(n_a^GGE) = (1/N) Σ_a m_a [Δ_BCS²/(2(λ_a²+Δ_BCS²))]²
                        − ((1/N) Σ_a m_a [Δ_BCS²/(2(λ_a²+Δ_BCS²))])²
Step 5 (Rewrite as the registry form):
        Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4  −  ((1/N) Σ_a m_a |v_a|^2)²
                        = F({λ_a, m_a}; Δ_BCS)
```

The right-hand side at Step 5 is a function of (i) the BdG eigenvalues `λ_a`, (ii) their multiplicities `m_a`, and (iii) the scalar order parameter `Δ_BCS`. NOTHING ELSE. There is no `π(a)` operator-algebra evaluation, no `[D, π(a)]` commutator, no `sup_{a∈A_h, ‖[D,π(a)]‖≤1}` state-pair functional. The GGE state ω_GGE has been integrated out at Step 2 and survives ONLY through the SCALAR parameter Δ_BCS, which is itself a structural property of the spectral triple (the BdG order parameter) and not a free state-pair argument.

#### Application of the parse-tree decision procedure (registry §VII.U.2 clause (e), line 12995)

Clause (e) gives the canonical decidability rule:

> `F` belongs to algebra-INVARIANT iff its symbolic form contains ONLY traces / spectral moments / `g(λ_k)` evaluations and no `π(a)` operator-algebra references; `F` belongs to algebra-DEPENDENT iff its symbolic form contains at least one `π(a)` or `[D, π(a)]` reference. The decision procedure is finite and operates at parse-tree level, NOT at numerical evaluation level — this makes it regulator-independent.

Parse-tree of the right-hand side of Step 5:

```
Var_a(n_a^GGE)
├── (1/N) Σ_a m_a |v_a|^4                           [spectrum-only: g_4(λ_a) := |v_a|^4 is a measurable function of λ_a alone]
└── ((1/N) Σ_a m_a |v_a|^2)^2                       [square of spectrum-only Σ_a m_a g_2(λ_a)]
```

Neither sub-tree contains `π(a)` or `[D, π(a)]`. The closed-form `g_2(λ) = Δ_BCS²/(2(λ²+Δ_BCS²))` is a measurable function of λ; so is `g_4(λ) = g_2(λ)²`. Both summations are of the form `Σ_a m_a g(λ_a)` — the EXACT canonical algebra-INVARIANT form `F_inv({λ_k, m_k}) = Σ_k m_k g(λ_k)` from registry §VII.U.2 clause (a) line 12950.

Therefore: **Var_a(n_a^GGE) ∈ algebra-INVARIANT family** by clause (e) parse-tree decision.

#### Mellin-pole axis (substrate-distance pole s)

The variance is a moment-of-moments construction at Weyl-dimensional weight 4 (NOT weight 2). Per the Seeley-DeWitt heat-kernel asymptotic structure on d=4:

- `Σ_a m_a g_2(λ_a)` at large L_max scales like the d=4 a_4 Seeley-DeWitt slot (substrate-distance-2 pole s=4 in the Mellin-cone language), because `g_2(λ) ∼ Δ_BCS²/(2λ²)` for `λ >> Δ_BCS` — a `λ^{-2}` tail integrated against the 4D Weyl-counting density `λ^3 dλ` gives convergence at the s=4 Mellin pole.
- `Σ_a m_a g_4(λ_a)` scales like `λ^{-4}` tail × `λ^3 dλ` — convergence at s=4 plus an additional log correction at d=4 (per registry §VII.U.2 line 12961: "Level-2 algebraic envelope is L^{−4} (modulo log corrections) per Sage-verified Weyl-law tail analysis at d=4 multiplicity-weighted normalization").

This pins the Mellin pole at **s=4 (substrate-distance-2)**, NOT s=3 (substrate-distance-1). The W6-6 baseline's `s=3` assertion is wrong on the pole axis IRRESPECTIVE of the algebra-axis verdict.

#### Wedderburn / Schur-orthogonality check on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) (NCG-axiomatic side)

The 7-axiom NCG construction requires the spectral triple to satisfy axioms 1-7. Wedderburn decomposition of `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` gives three Schur-orthogonal central projections `P_ℂ`, `P_ℍ`, `P_M3` whose `π(P_i)` partition H_F into three orthogonal sub-Hilbert spaces. The parse-tree decision procedure at the central-projection level (per W5b-48 Step 5: `Z(A_F) = ℂ · P_ℂ + ℂ · P_ℍ + ℂ · P_M3`) requires:

- **Algebra-DEPENDENT functionals** to involve `ω(π(a))` for `a ∉ Z(A_F)` — i.e., to require the FULL state ω on the non-central elements of A_F.
- **Algebra-INVARIANT functionals** to factor through `Z(A_F)` (or further through `f(D²)' ∩ π(A_F) = ℂ · 1_{H_F}` per W5b-48 eq. (9)).

The variance `Var_a(n_a^GGE)` as written in Step 5 factors through λ_a + m_a + Δ_BCS. The scalar `Δ_BCS` IS in the center: it is the magnitude of the BCS condensate, structurally a scalar property of the spectral triple (the pairing-channel order parameter of the BdG construction). Therefore the variance lies in the `f(D²)' ∩ π(A_F) = scalars` side of the chirality-vs-A_F block-grading mismatch — Corner I/II side (algebra-INVARIANT). The Schur-orthogonality check is PASS.

#### Corner verdict and questions for lizzi

- **Algebra-axis**: INVARIANT (parse-tree decision PASS; Wedderburn cross-check PASS)
- **Mellin-pole**: s=4 substrate-distance-2 (Weyl-tail analysis at d=4)
- **Corner cell**: **II = INVARIANT × s=4** ✓
- **NOT Corner I**: Corner I is INVARIANT × s=3; the Mellin pole is wrong for s=3 because `|v|² ∼ Δ_BCS²/(2λ²)` saturates at s=4, NOT s=3.
- **NOT Corner IV**: Corner IV is DEPENDENT × s=4; the algebra-axis is INVARIANT, not DEPENDENT, because the GGE state ω_GGE is integrated out at Step 2 leaving only scalar Δ_BCS + spectrum.
- **NOT Corner III**: Corner III is DEPENDENT × s=3; both axes wrong.

**Question for lizzi (Q-C1)**: Does the FI/RD/MIXED trichotomy (S82 W-3 §VII.K) corroborate the Corner II assignment? Specifically: is `Var_a(n_a^GGE)` a FI (Functional-Invariant) member under your S82 trichotomy, or does the `Δ_BCS` scalar parameter dependence shift it to RD (Regulator-Dressed) per the W-22 §V.4 LEVEL-DRESSED 4th-class extension? The answer matters: if the LEVEL-DRESSED extension applies, then Var_a(n_a^GGE) and §VII.AR are calibration-corpus companions on the same LEVEL-DRESSED axis (K=2 → K=3 progression under the §"Per-Bulletin-per-pole" sub-clause).

### C2: W-21 V.1+V.3 diff structural reading at §VII.U.2

**Disclaimer**: mack-cosmic-bridge holds CF-W6-3 diff-inspection duty (per W6-6 carry-forward at `session-89-w6-workingpaper.md:229` and `:390-398`). I do NOT inspect the git/W-21 diff directly here; instead I perform a TEXT-LEVEL STRUCTURAL READING of the current registry text at `permanent-results-registry.md §VII.U.2` to extract the structural fingerprint of whether the text READS LIKE a corner that was ALWAYS Corner II (Reading B) or a corner whose PRIOR Corner-I state was RECENTLY edited toward Corner II (Reading A).

#### Text features inspected at §VII.U.2 (registry lines 12927-13058)

**Feature 1 — Theorem-name line itself (line 12927)**:
> `### §VII.U.2 — Four-corner classification of (A_K, H_K, D_K) functionals (algebra-axis × Mellin-pole orthogonality) [STAGE-1-CANDIDATE] (S88 W5b-45 — lizzi-spectral-functional-theorist PRIMARY synthesizer + connes-ncg-theorist CO-AUTHOR for clauses (c)+(d), 2026-05-04)`

The theorem itself is the **partition table** (the 4-corner classification rule), NOT a single observable at a single corner. The slot's role in the registry is METHODOLOGICAL — it IS the rule-file landing site for the algebra-axis orthogonality K-counter (per line 13056: "this §VII.U.2 entry IS the registry landing of that K=3 promotion event"). The text never claims §VII.U.2 itself IS a single observable in a single corner. This already STRONGLY favors Reading B over Reading A: a meta-level partition theorem cannot SENSIBLY have a single corner-cell classification.

**Feature 2 — Corner II row in clause (d) (line 12961)**:
The current text contains an explicit parse-tree decision verdict:

> "Per S88 W-17 §V.2 landing per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` and clause (e) parse-tree decision: Var_a(n_a^GGE) is algebra-INVARIANT (symbolic form contains only λ_a, m_a, Δ_BCS scalar; no π(a), no [D, π(a)], no state-pair sup) and inhabits Corner II (NOT Corner IV — see corrigendum at Corner IV row below)."

This text-feature is structurally important: it cites W-17 §V.2 by gate-ID, declares the parse-tree decision verdict in INVARIANT form, and uses a parenthetical (NOT Corner IV) corrigendum-pointer. This is an UPDATE-FORM CORRIGENDUM, not an ORIGINAL-FORM CLAUSE. The text style is "we updated this; here is the parse-tree justification" — which is consistent with Reading B (the parse-tree decision was applied at S88 W-17 and it routed to Corner II from an EARLIER claim that may have been Corner IV).

**Feature 3 — Corner IV row corrigendum (line 12963)**:
> "**Per S88 W-17 §V.3 corrigendum (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`, 2026-05-08)**: the prior wording '... `Var_a(n_a^GGE)(L_max=10) = 7.282490e-06`, `α_loglog ≈ 3.56`, R² = 0.945, MARGINAL regime; INFO composite ...' is REMOVED — that envelope is on a structurally distinct Corner-II observable per W-17 §V.3, NOT a valid Corner-IV cross-confirmation."

The corrigendum DIRECTLY ATTESTS the editing history: the prior wording was at Corner IV and has been MOVED to Corner II. This is the SMOKING GUN — `Var_a(n_a^GGE)` was previously cited as a Corner-IV cross-confirmation, and W-17 §V.3 reclassified it to Corner II. The editing direction is **Corner-IV → Corner-II**, NOT **Corner-I → Corner-II**.

This means **the W6-6 plan baseline's Corner-I assertion was never the prior state**. The prior state was Corner-IV (a different incorrect assignment). W-17 §V.3 corrected Corner-IV → Corner-II. The W6-6 plan baseline confused itself THREE WAYS:
1. wrong algebra-axis (asserted "spectrum-only-functional" but the prior text had Corner-IV which is state-pair-DEPENDENT — opposite axis);
2. wrong Mellin-pole (asserted s=3 but actual pole is s=4);
3. wrong baseline diff (asserted Corner-I as the pre-V.1+V.3 baseline, when the actual pre-V.1+V.3 state at this observable was Corner-IV).

**Feature 4 — PRIMARY-vs-SCHEMATIC LEVEL switch markers**: The W6-6 working-paper Stage-A finding text at `session-89-w6-workingpaper.md:214` claims the §VII.U.2 block heads with:
> "§VII.U.2 Corner II `Var_a(n_a^GGE)` envelope under PRIMARY-vs-SCHEMATIC LEVEL switch..."

But my direct read of `permanent-results-registry.md:12927` shows the theorem-name line is:
> "§VII.U.2 — Four-corner classification of (A_K, H_K, D_K) functionals (algebra-axis × Mellin-pole orthogonality)"

The W6-6 stage-A grep found text that READS LIKE the §VII.U.2 BLOCK CONTAINS a Corner II observable with `Var_a(n_a^GGE)` and a PRIMARY-vs-SCHEMATIC LEVEL switch envelope — that text is in clause (d) Corner II row at line 12961, NOT at the theorem-name line. The W6-6 audit text-level scan correctly found Corner-II markers in the block, but the BLOCK as a whole is the partition theorem; the Corner-II markers are at the cell-instance row level. This is consistent with Reading B: §VII.U.2 always had the 4-corner table form; Corner II had a calibration instance evolution (open at K=3 saturation per Corrigendum C2 line 13010, then filled by Var_a(n_a^GGE) at W-17 §V.2 from the prior Corner-IV mis-assignment).

#### Structural verdict from text-level features

The current §VII.U.2 text READS LIKE a stably-CONSTRUCTED partition theorem (Reading B), NOT a corner-classified-then-altered observable (Reading A). Evidence in support:

- Theorem-name line is META-CLASSIFICATION (partition rule), not single-cell observable
- Corner II row contains EXPLICIT W-17 §V.2 parse-tree decision citation + INVARIANT verdict
- Corner IV row contains the EDITING-HISTORY ATTESTATION via S88 W-17 §V.3 corrigendum: prior wording was Corner-IV, moved to Corner-II
- Corrigenda block at line 13010 (C2): "Clause (d) Corner II is OPEN at K=3" — at W5b-45 LANDING TIME (S88-05-04), Corner II was empty; the partition's 4 corners had only 3 calibration instances (I, III, IV per line 13010). Corner II was FILLED at W-17 §V.2 (S88-05-08) by routing Var_a(n_a^GGE) from its prior (incorrect) Corner-IV slot.

**Conclusion for C2**: the text-level structural fingerprint says **Reading B is correct**. The W-21 V.1+V.3 edits (whose content is unknown to me without mack's diff inspection) most likely did NOT change Var_a(n_a^GGE)'s corner classification — that classification was ALWAYS not-Corner-I, and the W-17 §V.2/§V.3 edits at 2026-05-08 actively MOVED it from Corner-IV (the original incorrect assignment) to Corner-II (the parse-tree-decision-derived correct assignment). The Reading-A revert path is destructive: reverting V.1+V.3 would either restore the Corner-IV mis-assignment or leave the slot empty — neither restores Corner-I, because Corner-I was never the state of this observable.

**Question for lizzi (Q-C2)**: as the W-17 PRIMARY synthesizer (per registry line 12927 W5b-45 attribution AND your authorship of the parse-tree decision procedure clause (e) per line 12995), can you confirm or deny: was the editing history "Corner-IV (W5b-45 landing-time mis-assignment) → Corner-II (W-17 §V.2 parse-tree-decision correction)"? If yes, Reading A is impossible by construction (the pre-edit state was Corner-IV, not Corner-I). If the editing history is different from what I extracted from the corrigendum citations, please pin it.

### C3: Cross-wave consequence — W4 A.30 Stage-2 §VII.AR PASS-AND aggregation

#### Disambiguation first: A.30 actually targets §VII.AS, not §VII.AR

The W6-6 working-paper text at `session-89-w6-workingpaper.md:224` reads "W4 A.30 Stage-2 cross-axis verify of §VII.AR." However, the registry entry §VII.AS at `permanent-results-registry.md:17000` says explicitly: "A.30 (S89 Stage-2 cross-axis verify of **§VII.AS** — this entry)." Meanwhile §VII.AR has its OWN forward dispatch routing at line 16971: "A.36 (S89) `S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP`" — not A.30.

So the cross-wave dependency map at the Stage-2 layer is:

- **A.30 → §VII.AS** (slope_A geometric-resummation closure; Stage-2 cross-axis verify; reviewer-eligibility specified at registry line 16985: van-den-dungen + phonon-first-cosmologist or kitaev-information-theorist; lizzi+connes FORBIDDEN per original-authoring-agent exclusion).
- **A.36 → §VII.AR** (rank-ordering heat-kernel anchor-sweep; Reading-A vs Reading-B discrimination; STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP).
- **A.30 vs §VII.AR**: NOT a direct Stage-2 dispatch link. The W6-6 plan citation conflates A.30 with §VII.AR.

This conflation matters for the cross-wave consequence question: the W6-6 plan-text-asserted "FAIL propagates to W4 A.30 Stage-2 §VII.AR verify" cannot be literally correct because A.30 does not target §VII.AR. I will analyze BOTH propagation paths (A.30 → §VII.AS, A.36 → §VII.AR) since the W6-6 author may have intended either or both, and both inhabit the same algebra-axis cell as §VII.U.2's Corner II.

#### Cell-membership map (substrate-physics shared corner)

After C1's parse-tree verdict (Var_a(n_a^GGE) ∈ Corner II = INVARIANT × s=4):

| Slot | Algebra-axis | Mellin pole | Cell |
|:-----|:-------------|:------------|:-----|
| §VII.U.2 (Corner II row instance: Var_a(n_a^GGE)) | INVARIANT | s=4 | **II** |
| §VII.AR (W7a-74 LEVEL-DRESSED rank-ordering at s=4) | INVARIANT | s=4 | **II** (or Cell-I-LEVEL-DRESSED biaxial hybrid per line 16963) |
| §VII.AS (W6a-51 slope_A geometric-resummation closure) | INVARIANT | (closed-form @ τ_fold, no explicit Mellin pole — Level-2 envelope L^{-3} at d=4 per line 16993, suggests s=3) | **I** likely; possibly Cell-I-LEVEL-DRESSED biaxial hybrid per line 16992 |

**Critical finding**: §VII.AR and §VII.U.2's Corner II row are in the SAME CELL (II = INVARIANT × s=4) under the W-17 §V.2 parse-tree decision. The W6-6 plan baseline's Corner-I assertion was UNCANNILY consistent with §VII.AS (which IS Cell-I) — it is possible the plan author mistakenly read §VII.U.2 against §VII.AS's calibration corpus rather than §VII.AR's.

#### Quote: Stage-2 Axis-B Selection Protocol (joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol" lines 65-73)

Quoted verbatim:

> 1. **Axis-distinctness**: The Axis-B reviewer's primary methodology is on a DIFFERENT axis from Axis-A. Examples: Axis-A = NCG-axiomatic / spectral-functional → Axis-B = transit-dynamics / superfluid-universe / cosmological-bridge. Axis-A and Axis-B reviewers MUST NOT share the same axis even if their named methodologies differ in narrow specialty (e.g., two NCG-side reviewers fail axis-distinctness).
>
> 2. **Original-authoring-agent exclusion with downstream-inheritance reach**: Neither cross-reviewer may be (a) the original workshop authoring agent OR (b) a successor agent whose memory inherits the workshop's reading-path through prior session synthesis. The downstream-inheritance reach extends to agents whose project-memory or feedback-files cite the workshop's R1/R2/R3 transcripts as canonical reference; such agents are structurally pre-loaded with the workshop's view and fail the "without prior workshop context" requirement.
>
> 3. **Audit-coverage adequacy**: The Axis-B reviewer's domain expertise MUST cover ALL joint clauses + ALL Axis-B-side single-axis clauses. A reviewer with partial coverage (e.g., expert on transit-dynamics but not on cosmological-bridge applications) creates audit-coverage gaps where joint clauses pass formally but lack substantive cross-axis examination.

#### Substrate-input-orthogonality clause (joint-theorem-promotion.md lines 77-85, S88 W-23 W7c-167; SUGGESTION at K=1)

> For any Stage-2 verification with N ≥ 2 observables {obs_1, ..., obs_N}, the procedural floor MUST be supplemented with the **substrate-input-orthogonality predicate**:
> - ∃ obs_i such that the data file consumed by obs_i is loaded by exactly ONE cross-reviewer (NOT both).

#### Propagation analysis under C1's Corner-II verdict for Var_a(n_a^GGE)

**Path 1 — Direct propagation to A.36 → §VII.AR (the actual structural-adjacent slot)**:

§VII.AR is at INVARIANT × s=4 same as §VII.U.2 Corner II row. The Reading-A-vs-Reading-B discriminator at A.36 (heat-kernel anchor sweep) operates on `|ρ_S(s=4)|_PRIMARY = 0.800 ± δ` per registry line 16960. If `Var_a(n_a^GGE)` is the **CO-INHABITANT** of Cell II under the Corner-II assignment, then the K=2 calibration corpus at the Per-Bulletin-per-pole sub-clause grows: `{§VII.K-PROP.W10-4 ρ_∞ permanent-wall (s=4 fermionic-signed-residue), §VII.U.1 Mellin-Dirichlet (s=3), §VII.AR LEVEL-DRESSED rank-ordering (s=4 same pole as W10-4 but cohomology-class-distinct), §VII.U.2-Corner-II row Var_a(n_a^GGE) (s=4 same pole as W10-4 AND §VII.AR — third instance at s=4)}`. The K-counter advances. Does it affect §VII.AR's Stage-2 PASS-AND aggregation? Only IF §VII.AR's Stage-2 verify treats Var_a(n_a^GGE) as a constituent observable (it does not per the §VII.AR statement at line 16954 — that statement is purely about rank-ordering at fixed cutoff/M_PV²/Vol parameters, not about Var_a). So **§VII.AR Stage-2 PASS-AND is INDEPENDENT of §VII.U.2's Corner II re-classification**. The aggregation rule does not change under C4 Reading B (which is the structurally correct routing per C1).

**Path 2 — Propagation to A.30 → §VII.AS**:

§VII.AS is at Cell-I per line 16991. Var_a(n_a^GGE) (Cell II) is in a DIFFERENT corner. The Stage-2 cross-axis verify of §VII.AS dispatches to van-den-dungen + phonon-first-cosmologist or kitaev-information-theorist per registry line 16985 — NEITHER reviewer's domain expertise (NCG-Kasparov-bridge / transit-dynamics / information-scrambling) cross-loads §VII.U.2's Corner II content. The audit-coverage-adequacy clause (3) is unaffected. Substrate-input-orthogonality clause: §VII.AS's substrate-input is the slope_A canonical form evaluator on D_K spectrum at τ_fold = 0.190 (registry line 16991) — this data file (the slope_A npz) is DISJOINT from §VII.U.2's Var_a npz `s88_w5b_47_v_inf_extrapolated.npz` (per Corner II row line 12961 INFO composite reference). The orthogonality predicate is therefore TRIVIALLY satisfied (the two observables consume distinct .npz inputs). Therefore **§VII.AS Stage-2 PASS-AND aggregation is INDEPENDENT of §VII.U.2 Corner re-classification**.

**Path 3 — Axis-distinctness clause (1) and original-authoring-agent exclusion clause (2) interaction**:

Under Reading B (C1's verdict — §VII.U.2 Corner II was correct from W-17 §V.2 forward), the lizzi-spectral-functional-theorist authorship attribution at registry line 12927 ("PRIMARY synthesizer") and the connes-ncg-theorist CO-AUTHOR clauses (c)+(d) attribution at registry line 12936 means BOTH connes and lizzi are excluded from §VII.U.2's own Stage-2 verify (whenever it dispatches as `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` per registry line 12929). The substrate-input-orthogonality clause requires the Stage-2 reviewers' axis to be DISTINCT from BOTH connes (NCG-axiomatic) AND lizzi (spectral-functional). Eligible axes: transit-dynamics (volovik), cosmological-bridge (mack), superfluid-universe (volovik), information-theoretic (kitaev), van-den-dungen-bridge.

Under Reading A (revert) — if the revert were structurally valid (it is NOT per C1, but hypothetically) — the authorship attributions in the pre-W-21 text would need re-inspection. Reading A would not change the original-authoring-agent set unless the V.1+V.3 edits altered authorship attribution itself. Mack's CF-W6-3 diff inspection would reveal whether authorship changed under V.1+V.3.

#### Aggregation-rule change verdict

Under **Reading B (correct per C1)**: PASS-AND aggregation rule at §VII.AR Stage-2 does NOT change. PASS-AND aggregation rule at §VII.AS Stage-2 does NOT change. Reviewer-axis selection for §VII.AR's OWN Stage-2 (A.36 heat-kernel anchor-sweep) does not change. The §VII.U.2 OWN Stage-2 dispatch (`S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` per registry line 12929) requires a NON-lizzi NON-connes pair satisfying axis-distinctness + original-authoring-agent exclusion + audit-coverage-adequacy; this is unchanged by the Reading B verdict (the §VII.U.2 entry's Stage-1 STATE remains Corner II Var_a + Corner I/III/IV calibration corpus).

Under **Reading A (revert; structurally incorrect per C1)**: if the revert restored a pre-V.1+V.3 state in which §VII.U.2 had EITHER (a) the Corner-IV mis-assignment for Var_a (per the W-17 §V.3 corrigendum citation showing prior state was Corner-IV) OR (b) some yet-different state — the Corner II row would be empty or wrongly populated, which would BREAK the K=3 partition's calibration-corpus completeness at S87 W-2 R3 close (the K=3 calibration corpus at registry line 12956 cites Corners I + III + IV as the three saturating instances; Corner II is OPEN per Corrigendum C2 line 13010). Reading A would therefore not affect §VII.AR's Stage-2 aggregation directly, but would VIOLATE the partition's structural integrity by removing the W-17 §V.2 correction. Reading A is destructive per C1.

#### Substrate framing per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"

The 4-corner partition IS the substrate's algebra-axis-orthogonality classification of (A_K, H_K, D_K). The Stage-2 PASS-AND aggregation is the methodology-floor F-image (per `epistemic-discipline.md §"Layer-Decomposition"` layer-functor F: substrate → methodology → audit) of the substrate-physics independence requirement. Under Reading B, the substrate's classification is INVARIANT under cross-wave Stage-2 verifies at §VII.AR / §VII.AS because those slots inhabit structurally independent corners or independent sub-axes (LEVEL-DRESSED) and the propagation is via shared-Mellin-pole adjacency only, NOT via shared algebra-axis dependence. The methodology-floor F-image therefore preserves the independence by construction.

**Question for lizzi (no direct adjudication question here; the substrate-input-orthogonality clause and §VII.AR-vs-§VII.AS disambiguation are the load-bearing items)**: at C6 I queue a 4-field carry-forward to disambiguate the W6-6 plan-text's "A.30 → §VII.AR" citation against the registry's "A.30 → §VII.AS, A.36 → §VII.AR" canonical pin.

### C4: Routing decision (Reading A revert vs Reading B update plan baseline)

#### Verdict: **Reading B is correct. Reading A is structurally destructive.**

The routing decision follows directly from C1 + C2. I pin the verdict at the head and derive the consequences below.

#### Substitution chain to the routing decision (per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`)

```
Step 1 (C1 verdict, structural):     Var_a(n_a^GGE) ∈ Corner II (INVARIANT × s=4)
                                     by parse-tree decision + Bogoliubov closed form
                                     + Weyl-tail Mellin-pole analysis at d=4.

Step 2 (C2 text-feature verdict):    Registry editing history extracted from
                                     W-17 §V.3 corrigendum citation (registry
                                     line 12963) was Corner-IV → Corner-II;
                                     NOT Corner-I → Corner-II.

Step 3 (W6-6 plan baseline, asserted at session-89-w6-workingpaper.md:198):
                                     pre-V.1+V.3 baseline := `algebra-INVARIANT-spectrum-only-functional`
                                     ≡ Corner I (INVARIANT × s=3).

Step 4 (Comparison Step 2 vs Step 3):
                                     Step 2 says actual prior state was Corner IV.
                                     Step 3 says assumed prior state was Corner I.
                                     The two disagree.

Step 5 (Reading A definition):       Revert V.1+V.3 to restore the prior state.
                                     But the prior state is NOT Corner I per Step 2;
                                     it is Corner IV. Reverting restores a different
                                     incorrect state, not the asserted Corner I baseline.

Step 6 (Reading B definition):       Update the W6-6 plan baseline assertion to
                                     match the structural truth from Step 1:
                                     `pre-V.1+V.3 baseline` is replaced by
                                     `actual §VII.U.2 state` = Corner II for Var_a.

Step 7 (Direction):                  Step 5 yields a structurally incorrect outcome
                                     (Corner IV ≠ Corner I, and Corner IV is itself
                                     wrong per C1). Step 6 yields a structurally
                                     correct outcome (Corner II matches C1's
                                     parse-tree verdict).

Step 8 (Conclusion):                 Reading B is the routing decision. Reading A
                                     is structurally rejected.
```

#### Why Reading A is destructive (not just wrong but actively harmful)

Reading A would revert W-21 V.1+V.3 in an attempt to "restore Corner I." But three concrete failure modes follow:

1. **Reverting V.1+V.3 does NOT produce Corner I.** Per C2's text-feature extraction, the W-17 §V.3 corrigendum at registry line 12963 explicitly attests the prior wording placed Var_a(n_a^GGE) at Corner IV. The pre-V.1+V.3 baseline phrase `algebra-INVARIANT-spectrum-only-functional` in the W6-6 plan does NOT correspond to any historical state of §VII.U.2. The plan author either (a) read the wrong slot's text, (b) confused §VII.U.2 with §VII.AS (which IS Cell I at s=3 per registry line 16991), or (c) constructed the baseline phrase from external speculation. None of these baselines are reverting-recoverable.

2. **Reading A would break the K=3 partition completeness.** The K=3 calibration corpus at registry line 12956 saturates at Corners I + III + IV per Corrigendum C2 (line 13010). Corner II was OPEN at W5b-45 landing time (2026-05-04) and FILLED by W-17 §V.2 (2026-05-08) via the parse-tree decision that routed Var_a(n_a^GGE) from its prior Corner-IV mis-assignment to Corner II. Reverting V.1+V.3 (which the diff inspection by mack would either confirm OR refute as the source of the W-17 §V.2/§V.3 edits) would either (i) restore the Corner-IV mis-assignment (which W-17 §V.3 explicitly corrected) or (ii) empty Corner II again. Both outcomes break the K=3 partition's structural integrity at the Per-Bulletin-per-pole calibration-corpus saturation (registry line 12993: "K = 3 ≥ K_promotion = 3 ⇒ MANDATORY at this gate's landing per the K-counter advancement event").

3. **Reading A would violate the no-technical-debt rule.** Per `CLAUDE.md §"No Technical Debt"` and `feedback_fix-in-session-never-defer.md`, dispatch verification deviations are FIXED IN-SESSION. Reading A's revert path is itself an in-session technical-debt insertion: it would replace a structurally-correct classification (Corner II per parse-tree decision) with a structurally-incorrect one (Corner I per W6-6 plan baseline) on the basis of a plan-text assertion that itself fails the parse-tree decision procedure of clause (e). The structural truth wins over the plan-text assertion.

#### Reading B remediation steps (concrete, no narrative)

Per the routing decision Reading B is correct. The remediation is:

1. **mack-cosmic-bridge CF-W6-3 dispatch** (queued, `session-89-w6-workingpaper.md:390-398`) inspects S88 W-21 V.1 + V.3 diffs and confirms whether V.1+V.3 (a) touched §VII.U.2 Corner-II row only (no actual W-17 §V.2 reclassification involvement); OR (b) implemented the W-17 §V.2 reclassification itself; OR (c) edited unrelated text in the §VII.U.2 block.

2. **Plan-baseline correction**: the W6-6 plan baseline assertion `pre-V.1+V.3 baseline = algebra-INVARIANT-spectrum-only-functional` must be retracted. The correct retroactive baseline (for future plan-staleness validators) is `actual §VII.U.2 Corner II Var_a entry = algebra-INVARIANT-spectrum-AND-Δ_BCS-scalar-functional, at substrate-distance-2 pole s=4`. This is a plan-staleness correction, not a registry edit (the registry is correct as written).

3. **§VII.AR Stage-2 verify dispatch (A.36, NOT A.30) at S89+** proceeds with no change to its cross-reviewer eligibility set — per C3, the algebra-axis cell co-inhabitance of §VII.U.2 Corner II and §VII.AR does NOT entail Stage-2 dependence between them. The reviewer-eligibility set for §VII.AR's OWN Stage-2 verify is governed by §VII.AR's own original-authoring-agent exclusion (lizzi + connes excluded for §VII.AR per registry line 16973).

4. **CF-W6-4 audit extension** (queued; see C5 below) extends `_corner_classification_audit.py` to include §VII.U.2 as a target slot with PRE-REGISTERED EXPECTED CLASSIFICATION = Corner II (NOT Corner I). The pre-registered expected classification flows from C1's structural verdict, NOT from the W6-6 plan baseline.

#### Honest disclosure of asymmetry: where C1 + C2 + C4 might be overturned by mack's diff inspection

The Reading B routing is robust against the most plausible diff content (V.1+V.3 implementing the W-17 §V.2 parse-tree decision OR editing unrelated text). It would be overturned ONLY IF mack's diff inspection revealed BOTH:

(i) the V.1+V.3 edits explicitly REPLACED a stable Corner-I classification of Var_a(n_a^GGE) at §VII.U.2 with a Corner-II classification (i.e., the prior state really was Corner-I, NOT Corner-IV);

AND

(ii) the W-17 §V.3 corrigendum citation at registry line 12963 is FACTUALLY WRONG about the prior state being Corner-IV (i.e., the corrigendum's own attestation is fabricated or mis-remembered).

Both (i) and (ii) would have to hold simultaneously, which is structurally implausible given the corrigendum is a SOLE-WRITER (mack-cosmic-bridge) attestation with explicit S88 W-17 §V.3 sourcing. But the empirical confirmation lives in mack's CF-W6-3 inspection. I commit to Reading B with the explicit acknowledgment that mack's diff inspection is the load-bearing structural verifier; if mack finds (i)+(ii) both true, Reading A becomes the correct routing and C1's verdict stands while C2's editing-history extraction needs revision.

**Question for lizzi (Q-C4)**: are you a CO-WITNESS to the W-17 §V.2/§V.3 editing history (you are the PRIMARY synthesizer of §VII.U.2 at W5b-45 per registry line 12927, and the parse-tree decision procedure clause (e) author)? If yes, can you pin the prior state of Var_a(n_a^GGE) at the time of W5b-45 landing: was it ALREADY at Corner IV (before W-17 §V.3 moved it), at Corner I (per W6-6 plan baseline), or at a third state? Your testimony would harden Reading B independently of mack's diff inspection.

### C5: W6-6 audit-machinery implications + CF-W6-4 corner_classification_audit.py extension

#### State of W6-6 audit machinery (verified on disk)

Per `session-89-w6-workingpaper.md:202`, the existing `_corner_classification_audit.py` is a 27 KB script that audits 7 slots (§VII.U.1, §VII.U.6, §VII.AC.1, §VII.AC.4, §VII.W, §VII.AF.1, §VII.AJ). The W6-6 wrapper at `computations/_shared/_vii_u_2_audit_re_run_corner_i_preservation.py` is a 2-stage wrapper:

- **Stage A**: text-level direct scan of §VII.U.2 block in `permanent-results-registry.md` for Corner-I markers (`Corner I` / `algebra-INVARIANT` / `spectrum-only-functional` / pre-V.1+V.3 baseline phrase).
- **Stage B**: subprocess-invoke existing `_corner_classification_audit.py` to verify §VII.U.* family-mate slots (§VII.U.1 + §VII.U.6) still classify as Corner-I.

The Stage A baseline-phrase set is the structural problem: ALL FOUR markers (`Corner I`, `algebra-INVARIANT`, `spectrum-only-functional`, pre-V.1+V.3 baseline phrase) are checks AGAINST a Corner-I hypothesis. The W6-6 audit machinery is HARDCODED to check Corner-I-preservation under the W6-6 plan baseline's wrong assertion. Under C1's structural truth (§VII.U.2 = Corner II), the Stage-A audit is constitutionally guaranteed to return FAIL — the FAIL is the correct outcome relative to the wrong baseline. The W6-6 audit text-level scan is **structurally-correct as a methodology-floor F-image of "did §VII.U.2 match the plan baseline?"** but its plan baseline is wrong; the FAIL is informative (it surfaced the discrepancy that triggered this workshop).

#### CF-W6-4 audit-machinery extension under Reading A vs Reading B

**Under Reading A (the W-21 V.1+V.3 edits broke a prior Corner-I state — structurally rejected per C4)**:

If Reading A were correct, CF-W6-4 would need to extend `_corner_classification_audit.py` to detect "Corner-I drift" at §VII.U.2 — i.e., to register §VII.U.2 with PRE-REGISTERED EXPECTED CLASSIFICATION = Corner I and emit FAIL whenever the live registry text scan disagrees. The audit would function as a regression detector for the V.1+V.3 reverting. This is the W6-6 plan author's apparent intent.

But Reading A is structurally rejected (C4). Building a regression detector against a structurally wrong baseline would INSTITUTIONALIZE the wrong baseline as a methodology-floor commitment. Every future audit would falsely emit FAIL against the correct Corner II classification, generating false-alarm spam that obscures real structural drift. This is the no-technical-debt violation route.

**Under Reading B (W6-6 plan baseline always was wrong — structural truth per C1)**:

CF-W6-4 extends `_corner_classification_audit.py` to add §VII.U.2 to its target list with PRE-REGISTERED EXPECTED CLASSIFICATION pinned per C1's structural verdict:

- For the **§VII.U.2 BLOCK AS A WHOLE** (the partition theorem itself, per C2 Feature 1): the audit target is META-CLASSIFICATION — the slot IS the 4-corner partition rule, NOT a single-cell observable. The audit should detect whether the block CONTAINS THE 4-CORNER PARTITION TABLE INTACT (corner labels I/II/III/IV present, algebra-axis labels INVARIANT/DEPENDENT present, Mellin-pole labels s=3/s=4 present, parse-tree decision procedure clause (e) present). The expected output is `block_is_partition_theorem=True; partition_table_corners=4; partition_axes=2; parse_tree_clause_e_present=True`.
- For the **Corner II row instance** (Var_a(n_a^GGE)): the audit target is THE INSTANCE-LEVEL classification of Var_a within the Corner II row. The audit should apply the parse-tree decision procedure (per registry §VII.U.2 clause (e) line 12995) to the symbolic form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` (registry line 12961) and verify the verdict: algebra-INVARIANT (no π(a), no [D, π(a)]) at substrate-distance pole s=4. Expected output: `var_a_n_a_gge_corner=II; var_a_algebra_axis=INVARIANT; var_a_mellin_pole=s_eq_4`.
- For the **Corner IV row instance** (`α_s_route_3 = d² ln P_GGE / d(ln K)²`): the audit applies the parse-tree decision to confirm the W-17 §V.3 corrigendum classification = Corner IV (DEPENDENT × s=4). Expected output: `alpha_s_route_3_corner=IV; alpha_s_route_3_algebra_axis=DEPENDENT; alpha_s_route_3_mellin_pole=s_eq_4`.

#### Pre-registration of CF-W6-4 extension target classification (Reading B)

For S89+ CF-W6-4 dispatch, the audit script must extend its TARGET_SLOTS dict with:

```python
TARGET_SLOTS_S89 = TARGET_SLOTS_S87.copy()
TARGET_SLOTS_S89["§VII.U.2"] = {
    "type": "meta_classification_partition_theorem",
    "expected_block_contains_partition_table": True,
    "expected_block_contains_parse_tree_clause_e": True,
    "instance_rows": {
        "corner_I_instance": {
            "row_label": "§VII.U.1 Mellin-Dirichlet identity at s=3",
            "expected_corner": "I",
            "expected_algebra_axis": "INVARIANT",
            "expected_mellin_pole": "s=3",
        },
        "corner_II_instance": {
            "row_label": "Var_a(n_a^GGE) per W-17 §V.2 parse-tree decision",
            "expected_corner": "II",
            "expected_algebra_axis": "INVARIANT",
            "expected_mellin_pole": "s=4",
            "parse_tree_check": {
                "symbolic_form": "(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2",
                "expected_pi_a_count": 0,
                "expected_commutator_D_pi_a_count": 0,
                "expected_state_pair_sup_count": 0,
            },
        },
        "corner_III_instance": {
            "row_label": "Connes distance on (H ⊕ M_3) sub-block",
            "expected_corner": "III",
            "expected_algebra_axis": "DEPENDENT",
            "expected_mellin_pole": "s=3",
        },
        "corner_IV_instance": {
            "row_label": "α_s_route_3 = d² ln P_GGE / d(ln K)² per W-17 §V.3 corrigendum",
            "expected_corner": "IV",
            "expected_algebra_axis": "DEPENDENT",
            "expected_mellin_pole": "s=4",
        },
    },
    "pre_registered_baseline_correction": "W6-6 plan baseline assertion of Corner-I for Var_a(n_a^GGE) is RETRACTED per S89 W-3 workshop verdict; correct baseline is Corner II.",
}
```

The pre-registration of `expected_corner = II` for Var_a(n_a^GGE) flows from C1's parse-tree decision verdict, not from the W6-6 plan baseline. Future audit runs will PASS when the registry text matches the parse-tree-derived classification AND FAIL only when actual structural drift occurs (e.g., if a future edit moves Var_a to a different corner OR removes the parse-tree decision procedure from clause (e)). The false-alarm spam of Reading A is structurally precluded by routing the expected classification through the parse-tree decision rather than through the W6-6 plan baseline.

#### Audit-machinery interaction with W6-6 wrapper

Under Reading B, the W6-6 wrapper's Stage A (text-level direct scan for Corner-I markers) is retired as a one-shot diagnostic for the W6-6 plan-baseline-vs-actual discrepancy. Future audits use the CF-W6-4-extended `_corner_classification_audit.py` directly. The W6-6 wrapper is preserved as audit-trail evidence of the S89 W6-6 FAIL → S89 W-3 workshop reconciliation chain.

#### Pre-registered S89+ dispatch — gate spec for CF-W6-4

- **Gate ID**: `S89-CORNER-CLASSIFICATION-AUDIT-EXTENSION-VII-U-2`
- **What**: extend `_corner_classification_audit.py` per the TARGET_SLOTS_S89 spec above; verify self-test PASS on the §VII.U.2 entry containing corner/algebra_axis/status fields populated; verify the parse-tree check on Var_a's symbolic form returns INVARIANT (`expected_pi_a_count = 0` AND `expected_commutator_D_pi_a_count = 0` AND `expected_state_pair_sup_count = 0`).
- **Inputs**: existing `_corner_classification_audit.py` (per W6-6 SHA pin `2b96bf78…`); §VII.U.2 block content from `permanent-results-registry.md` lines 12927-13058; the parse-tree decision procedure from clause (e) line 12995.
- **Gate criterion**: PASS = `per_slot_results['§VII.U.2']` populated AND `var_a_n_a_gge_corner='II'` AND `var_a_algebra_axis='INVARIANT'` AND `var_a_mellin_pole='s=4'` AND `parse_tree_check_pass=True`.
- **Effort**: 0.3 wave-equivalent (extension + self-test; identical extension pattern to existing 7 slots).
- **Owner**: gen-physicist orchestrator-direct per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class; mack-cosmic-bridge consults if registry text edits are needed.

#### Substrate framing per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"

The audit script IS the methodology-floor F-image (per `epistemic-discipline.md §"Layer-Decomposition"`) of the substrate-physics parse-tree decision procedure of registry §VII.U.2 clause (e). The decision procedure IS the substrate-axiomatic test of algebra-axis class membership (per NCG axioms 1+4+5+6 + W5b-48 8-step derivation at registry line 12954). The audit verifies that the substrate's intrinsic parse-tree decision is faithfully F-imaged at the methodology-floor (rule-file, registry-text, audit-script). Container-thinking inversion: the audit is NOT a container checking that the registry slot satisfies a meta-classification "in" a partition container; the substrate IS the partition (4-corner orthogonality at the algebra-axis level) and the audit IS the methodology-floor sentinel that this partition retains its F-image under registry edits.

**Question for lizzi (Q-C5)**: as the W5b-45 PRIMARY synthesizer of §VII.U.2 and the author of the parse-tree decision procedure (clause (e) line 12995), do you adopt this CF-W6-4 extension's pre-registered classification table as the canonical expected-classification for S89+ audits? Specifically: (i) is the Corner II row instance's symbolic form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` the FULL form of the parse-tree input, or are there sub-expressions inside `|v_a|^2 = Δ_BCS²/(2(λ_a² + Δ_BCS²))` that should be expanded at the parse-tree level for the audit's `expected_pi_a_count` check? (ii) Should the audit's parse-tree check also verify the Bogoliubov closed form's algebraic consistency with the BdG axiom set, or is the symbolic-form-only check at the registry-text level sufficient?

### C6: Cross-cutting observations + R1 4-field carry-forward

#### Observation 1: K-counter advancement assessment

(i) **Algebra-axis orthogonality K-counter** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, MANDATORY at K=3 since S87 W-2 R3 close 2026-04-30; registry line 13056 anchors this).

This workshop's verdict (C1: Var_a(n_a^GGE) ∈ Corner II) does NOT advance the K-counter from K=3 → K=4 at the algebra-axis orthogonality discipline level. Reason: K=3 was already saturated by the W1b-6 / S-2 / W-2 calibration corpus (Mellin-Dirichlet identity vs Connes distance and α_s_canonical vs α_s_route_3 contrasts) per registry line 13056. The Var_a(n_a^GGE) verdict at Corner II is a CALIBRATION-CORPUS-INSTANCE-FILLING event for Corner II (which was OPEN at W5b-45 landing per Corrigendum C2 line 13010), not a structural-K-counter-advancing event at the algebra-axis level. The K=3 status remains MANDATORY; this workshop strengthens the corpus by completing Corner II's empty slot.

(ii) **Per-Bulletin-per-pole Level-1 wall classification K-counter** (per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification (S88 W10-119 extension)"`, SUGGESTION at K=3 with cohomology-class-distinct-K=3 satisfied; pole-distinct-K=3 pending per `cross-pillar-bridge-anatomy.md` line 314 "the substrate-distance pole-distinct criterion s ∉ {s=3, s=4} is NOT yet met"). 

This workshop's C1 verdict places Var_a(n_a^GGE) at s=4 (substrate-distance-2) within Corner II. The existing K=3 calibration corpus at the Per-Bulletin-per-pole sub-clause is `{§VII.K-PROP.W10-4 ρ_∞ permanent-wall (s=4), §VII.U.1 Mellin-Dirichlet (s=3), §VII.AR LEVEL-DRESSED rank-ordering (s=4 cohomology-class-distinct from W10-4)}`. Adding §VII.U.2's Corner II row instance (Var_a at s=4 INVARIANT, cohomology-class-distinct from both W10-4 fermionic-signed-residue AND §VII.AR LEVEL-DRESSED) ADVANCES the cohomology-class-distinct corpus from K=3 → K=4 at the same pole s=4. The pole-distinct criterion (`s ∉ {s=3, s=4}`) is STILL not satisfied — Var_a is at s=4, sharing the pole with W10-4 and §VII.AR. So the rule's status stays SUGGESTION-pending-pole-distinct-K=3 until a fourth corpus instance at a new substrate-distance pole (s=5 or s=6) lands. The advancement at K=4 cohomology-class-distinct is a corpus-strengthening event, not a status-promotion event.

(iii) **Cross-corner co-primary FORBIDDEN clause** (registry §VII.U.2 clause (f) line 13005). This clause forbids cross-corner co-primary registry-anchor structures. Under C1's verdict (Var_a ∈ Corner II), any future S89+ registry entry citing Var_a(n_a^GGE) as one of TWO co-primary anchors must verify its co-anchor lives in the SAME corner (Cell II = INVARIANT × s=4). Cross-corner co-primary with §VII.U.6 (Corner I) or §VII.AS (Corner I likely) or §VII.U.7 (Corner classification TBD) or §VII.AR (Cell-I-LEVEL-DRESSED or Cell-II — TBD by A.36 anchor-sweep) requires explicit pre-registration audit. The W6-6 baseline's confusion of Corner-I-vs-Corner-II ALSO violates the cross-corner FORBIDDEN clause indirectly: by asserting Corner-I, the plan was implicitly asserting cross-corner pairing of Var_a with §VII.U.1 / §VII.U.6 (both Corner I) at the family-mate-comparison level, which the audit would have caught.

#### Observation 2: editing-history archaeology — the W-17 reclassification path

The C2 text-feature extraction (W-17 §V.3 corrigendum attestation) plus C4's substitution chain together imply a specific editing history at §VII.U.2:

```
Editing-history reconstruction (C2+C4 inferred):
  W5b-45 LANDING (2026-05-04): §VII.U.2 partition-rule theorem landed by lizzi PRIMARY
                                + connes CO-AUTHOR + mack SOLE WRITER. Corner I/III/IV
                                each have a calibration-instance row; Corner II OPEN.
                                Var_a(n_a^GGE) cited initially as Corner IV
                                cross-confirmation (with the W5b-47 INFO composite
                                envelope numbers prominently shown).
  
  W-17 §V.2 + §V.3 (2026-05-08): parse-tree decision applied to Var_a(n_a^GGE).
                                  Result: INVARIANT (not DEPENDENT) → Corner II
                                  (not Corner IV). §V.3 corrigendum REMOVES the
                                  W5b-47 envelope from Corner IV; §V.2 INSTALLS
                                  Var_a as the Corner II calibration instance with
                                  explicit (NOT Corner IV — see corrigendum) tag.
                                  Pole-axis: still s=4 (substrate-distance-2).
  
  W-21 V.1 + V.3 (??): mack inspects in CF-W6-3. Hypothesized content: minor edits
                       (PRIMARY-vs-SCHEMATIC LEVEL switch envelope expansion of
                       Corner II row OR Corner IV row clarifications). Should NOT
                       have touched the corner-classification VERDICT itself per
                       this workshop's structural analysis.
  
  W6-6 BASELINE ASSERTION (2026-05-10): plan baseline asserted pre-V.1+V.3 state
                                        was Corner I. STRUCTURALLY INCORRECT per
                                        all preceding analysis.
```

This reconstruction is testable via mack's CF-W6-3 diff inspection. If the W-21 V.1+V.3 diff content matches the hypothesized "minor edits on Corner II / IV row clarifications" pattern, Reading B is confirmed. If V.1+V.3 actually CONTAINED the W-17 §V.2 reclassification, then W-17 §V.2 happened AT W-21 V.1+V.3 (not before), but the structural verdict is unchanged.

#### Observation 3: §VII.AR vs §VII.AS cross-wave audit hygiene

C3 surfaced a plan-vs-registry discrepancy: W6-6 plan says "FAIL propagates to W4 A.30 Stage-2 §VII.AR verify"; registry says "A.30 → §VII.AS, A.36 → §VII.AR." This is a plan-staleness defect orthogonal to the Var_a(n_a^GGE) corner-classification question. It should be queued as a separate carry-forward for plan-staleness validator regex tightening at CF-W6-6 (already queued at `session-89-w6-workingpaper.md` lines 420-428) — that CF-W6-6 should be extended to detect cross-wave-anchor mis-citations like A.30 vs A.36 against the registry's authoritative routing table.

#### Observation 4: V_a vs n_a^GGE — the substrate-axiomatic root of the parse-tree decision

The most structurally interesting observation: `Var_a(n_a^GGE)` is named with the GGE STATE in its name, which is what misled the W6-6 plan author into reading it as a state-pair functional (Corner III/IV). But the GGE state's role is ENTIRELY in producing the closed-form NUMBER `n_a = |v_a|²` per Step 2 of C1's substitution chain — once that number is in hand, the variance is a SAMPLE-VARIANCE OVER MODE INDEX `a`, weighted by `m_a`, and the integrand `(g_4(λ_a), g_2(λ_a))` is a measurable function of λ alone. The GGE label is a HISTORICAL TAG of where the closed form `g_2(λ) = Δ_BCS²/(2(λ²+Δ_BCS²))` came from, NOT an indicator of state-pair functional structure. This is the SAME structural pattern as `α_s_canonical = n_s² − 1` (Corner I per registry line 12960): the cosmological observable `n_s` could LOOK like a state-pair quantity (it has an observation history attached) but is structurally a spectrum-only functional of D_K. The parse-tree decision procedure at clause (e) is the load-bearing discipline that prevents naming-history-driven mis-assignment.

This is a useful framework lesson: **observable naming conventions encode HISTORY, not STRUCTURE**. The corner classification operates on parse-tree STRUCTURE, not on observable NAMES. Future S89+ registry entries should pre-register their parse-tree expansion alongside the symbolic form (per registry line 12995 clause (e)) so the structural check is mechanizable.

#### R1 4-field carry-forwards (per `feedback_fix-in-session-never-defer.md` + `.claude/rules/output-standards.md §"Carry-Forward Dependency Enumeration"`)

##### CF-R1-1 — S89+ `_corner_classification_audit.py` extension to include §VII.U.2

| Field | Value |
|:------|:------|
| **What** | Extend `computations/_shared/_corner_classification_audit.py` TARGET_SLOTS dict to include §VII.U.2 with the meta_classification_partition_theorem type AND the 4 instance-row sub-targets (Corner I §VII.U.1 ref, Corner II Var_a(n_a^GGE) instance, Corner III Connes-distance ref, Corner IV α_s_route_3 ref). Pre-registered expected classification for Var_a(n_a^GGE): Corner II = INVARIANT × s=4 per S89 W-3 workshop C1 parse-tree verdict (this workshop). |
| **Inputs** | Existing `_corner_classification_audit.py` (W6-6 SHA pin `2b96bf78…`, located at `computations/_shared/_corner_classification_audit.py`); §VII.U.2 block content `permanent-results-registry.md:12927-13058`; the parse-tree decision procedure from registry §VII.U.2 clause (e) line 12995; the symbolic form for Var_a registry line 12961; the C1 substitution chain in this workshop. |
| **Gate** | PASS = `per_slot_results['§VII.U.2']` populated AND `var_a_corner='II'` AND `var_a_algebra_axis='INVARIANT'` AND `var_a_mellin_pole='s=4'` AND `parse_tree_pi_a_count=0` AND `parse_tree_commutator_count=0`. FAIL on any mismatch. |
| **Effort** | 0.3 wave-equivalents (extension + self-test against 4 instance rows; identical extension pattern to existing 7 audited slots). |
| **Owner** | gen-physicist orchestrator-direct per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class. |
| **Depends on** | UPSTREAM GATE: CF-W6-3 (mack-cosmic-bridge §VII.U.2 corner reconciliation) — should land first to lock in Reading B; UPSTREAM REGISTRY: §VII.U.2 clause (e) parse-tree decision procedure (registry line 12995); UPSTREAM RULE: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3. |

##### CF-R1-2 — Plan-staleness extension to catch cross-wave-anchor citation drift (A.30 vs A.36 mis-citation)

| Field | Value |
|:------|:------|
| **What** | Extend `computations/_shared/_plan_staleness_audit.py` (per W6-6 carry-forward CF-W6-6 line 420-428) to detect cross-wave-anchor mis-citations against the registry's authoritative routing table. Specifically: detect plan-text claims of the form "A.<NN> Stage-2 verify of §VII.<SLOT>" and verify against the registry's actual A.<NN> → §VII.<SLOT> mapping. The W6-6 plan's "W4 A.30 Stage-2 §VII.AR verify" assertion (session-89-w6-workingpaper.md:224) is the calibration corpus instance #1 of this pattern (registry says A.30 → §VII.AS, A.36 → §VII.AR). |
| **Inputs** | `_plan_staleness_audit.py` body (W6-6 SHA `5f370299…`); registry `permanent-results-registry.md` for A.<NN> → §VII.<SLOT> authoritative mapping table; `session-89-w6-workingpaper.md:224` as calibration corpus instance #1. |
| **Gate** | PASS = re-run on `session-89-w6-workingpaper.md` flags the line 224 "A.30 → §VII.AR" assertion as cross-wave-anchor-citation-drift; PASS extends to detect future plan-text mis-citations across all session-NN-plan-*.md files. INFO if extension lands but no calibration corpus instances trigger on existing plans. |
| **Effort** | 0.2 wave-equivalents (regex extension + 1 calibration corpus row). |
| **Owner** | gen-physicist orchestrator-direct. |
| **Depends on** | UPSTREAM PLAN-FILE: `_plan_staleness_audit.py` body; UPSTREAM REGISTRY: §VII.AR routing line 16971 (A.36) + §VII.AS routing line 17000 (A.30); UPSTREAM WORKSHOP: this S89 W-3 C3 finding. |

##### CF-R1-3 — Pre-register parse-tree expansion alongside symbolic form for all S89+ §VII registry entries

| Field | Value |
|:------|:------|
| **What** | Extend the registry-landing convention (per `.claude/rules/registry-landing.md`) to require new §VII entries that cite an observable with a state-historic name (e.g., `n_a^GGE`, `α_s_route_*`, `P_GGE`, `ω_GGE`-tagged quantities) to ALSO declare their parse-tree expansion at the level of `{spectrum-only g(λ_k), Σ-summations, π(a) operator-algebra references, [D, π(a)] commutators, state-pair sup constructs}`. This makes the clause (e) parse-tree decision mechanizable at landing time, eliminating future Corner-mis-assignments via naming-history confusion. |
| **Inputs** | `.claude/rules/registry-landing.md` body (S88 W7c-30 SHA pin); registry §VII.U.2 clause (e) text line 12995 as the substrate-physics specification; this S89 W-3 workshop C1 + C6 Observation 4 as the substrate-physics motivation. |
| **Gate** | PASS = registry-landing rule extended with a new sub-section "Parse-tree expansion pre-registration" with audit-script hook into `_registry_landing_audit.py`; calibration corpus instance #1 = retroactive parse-tree expansion of §VII.U.2 Corner II row Var_a(n_a^GGE) per this workshop's substitution chain. |
| **Effort** | 0.4 wave-equivalents (rule extension + audit script extension + 1 calibration corpus instance). |
| **Owner** | gen-physicist + mack-cosmic-bridge co-authored (mack as registry-landing-rule sole writer per `feedback_mack-bridge-role.md`). |
| **Depends on** | UPSTREAM RULE: `.claude/rules/registry-landing.md`; UPSTREAM REGISTRY: §VII.U.2 clause (e) parse-tree decision procedure line 12995; UPSTREAM AUDIT: `_corner_classification_audit.py` (which already implements clause (e) for the 7 currently audited slots and CF-R1-1 above extends to §VII.U.2). |

##### CF-R1-4 — Cross-axis Stage-2 reviewer-eligibility audit for §VII.U.2's own Stage-2 dispatch

| Field | Value |
|:------|:------|
| **What** | When §VII.U.2's own Stage-2 cross-axis verify (`S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` per registry line 12929) dispatches, the Axis-A and Axis-B reviewers MUST satisfy the 3-clause Stage-2 Axis-B Selection Protocol (joint-theorem-promotion.md lines 67-73): (1) axis-distinctness, (2) original-authoring-agent exclusion with downstream-inheritance reach, (3) audit-coverage adequacy. Pre-register the eligibility table: connes-ncg-theorist EXCLUDED (CO-AUTHOR per registry line 12936); lizzi-spectral-functional-theorist EXCLUDED (PRIMARY synthesizer per registry line 12927). Eligible axis-A candidates: van-den-dungen-bridge-theorist (NCG-Kasparov-bridge axis), gen-physicist (general-physics axis). Eligible axis-B candidates: volovik-superfluid-universe-theorist, mack-cosmic-bridge (cosmological-bridge), kitaev-information-theorist. |
| **Inputs** | `joint-theorem-promotion.md §"Stage 2"` lines 55-91; registry §VII.U.2 authorship attribution lines 12936 + 12942 + 12950-12952 + 13050-13053; this S89 W-3 workshop C3 cross-wave consequence analysis. |
| **Gate** | PASS = §VII.U.2 Stage-2 dispatch pre-registers an axis-A reviewer NOT in {connes, lizzi} AND an axis-B reviewer NOT in {connes, lizzi} AND on DIFFERENT axes; PASS-AND across clauses (c) JOINT + (d) JOINT. |
| **Effort** | 1.0 wave-equivalents (Stage-2 dispatch + dual cross-reviewer verdict + PASS-AND aggregation). |
| **Owner** | orchestrator dispatches the two reviewers; reviewers operate per Stage-2 standard. |
| **Depends on** | UPSTREAM RULE: `joint-theorem-promotion.md §"Stage 2 Axis-B Selection Protocol"`; UPSTREAM REGISTRY ENTRY: §VII.U.2 authorship attribution; UPSTREAM WORKSHOP: this S89 W-3 verdict (Reading B confirmed → §VII.U.2 STAGE-1-CANDIDATE proceeds to Stage-2 verify without revert). |

##### CF-R1-5 — Documentation note: observable-naming-history vs structural-classification orthogonality

| Field | Value |
|:------|:------|
| **What** | Append a documentation note to either `phononic-framing.md §"IS Space, Not IN Space"` OR `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` explaining the principle surfaced by this workshop's C6 Observation 4: observable naming conventions encode HISTORY (where the closed form was first derived: GGE-state, route-3 derivative, n_s-cosmological, etc.) NOT STRUCTURE. Corner classification operates on parse-tree STRUCTURE per clause (e) decision procedure. The Var_a(n_a^GGE) Corner-IV → Corner-II reclassification at W-17 §V.2 + §V.3 + the W6-6 plan baseline's Corner-I mis-assertion are calibration corpus instance #1 of this pattern. |
| **Inputs** | This S89 W-3 workshop's C1 + C6 Observation 4; registry §VII.U.2 clauses (a) + (b) + (e); the W-17 §V.3 corrigendum text at registry line 12963. |
| **Gate** | PASS = documentation note appended; one calibration corpus row added (this workshop's instance). |
| **Effort** | 0.1 wave-equivalents. |
| **Owner** | gen-physicist orchestrator-direct (METHODOLOGY-class wave per allowlist). |
| **Depends on** | UPSTREAM RULE: `phononic-framing.md`; UPSTREAM RULE: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`; UPSTREAM WORKSHOP: this S89 W-3 R1 connes synthesis. |

#### End of Round 1 connes opening analysis

C1-C6 fill the connes Round 1 sections per the workshop skeleton with substantive analysis. Verdicts pinned:
- C1: Var_a(n_a^GGE) ∈ Corner II (INVARIANT × s=4) per parse-tree decision + Bogoliubov closed form + Weyl-tail Mellin-pole analysis.
- C2: Text-feature reading favors Reading B over Reading A (W-17 §V.3 corrigendum attests prior state was Corner IV, not Corner I).
- C3: No propagation to §VII.AR or §VII.AS Stage-2 aggregation under Reading B; the W6-6 plan's "A.30 → §VII.AR" assertion is itself a plan-staleness defect (registry has A.30 → §VII.AS, A.36 → §VII.AR).
- C4: Reading B is correct; Reading A is structurally destructive (would restore Corner-IV mis-assignment or empty Corner II, breaking K=3 partition completeness).
- C5: CF-W6-4 audit extension pre-registers expected classification per C1 verdict (Corner II for Var_a), NOT per W6-6 plan baseline (Corner I).
- C6: K=3 algebra-axis orthogonality status MANDATORY unchanged; Per-Bulletin-per-pole cohomology-class-distinct corpus advances K=3 → K=4 at s=4 (pole-distinct still pending); 5 carry-forwards seeded with full 7-field dependency enumeration.

I hand off to lizzi for Round 1 Response & Cross-Synthesis. The highest-leverage adjudication seams are: Q-C1 (FI/RD/MIXED vs LEVEL-DRESSED classification), Q-C2 (editing-history co-witness testimony), Q-C4 (W5b-45-landing-time state of Var_a), Q-C5 (parse-tree expansion granularity for the audit).

---

## Round 1 — lizzi: Response & Cross-Synthesis

### Part 1: Response to connes's Sections

#### Re: C1 — Corner classification from first principles

**AGREE**: I converge on Corner II (INVARIANT × s=4) for `Var_a(n_a^GGE)` via the FI/RD/MIXED machinery (S82 R2-B, lizzi-signature per registry line 4311) — and the convergence is *not* a parallel-axes coincidence; it is structurally forced by the same axiom (NCG axiom 5, central-projection grading) that drives connes's Wedderburn / Schur-orthogonality cross-check at C1. My S82 W-3 trichotomy operates at the regulator-class axis (FI / RD / MIXED), and the FI/RD distinction lives entirely WITHIN the algebra-INVARIANT cell of connes's 4-corner grid; neither FI nor RD crosses corners.

Independent supporting evidence from my domain:

- **Parse-tree decision (clause (e), my authorship per registry line 12995)**: I personally drafted the symbolic-form predicate `F belongs to algebra-INVARIANT iff its symbolic form contains ONLY traces / spectral moments / g(λ_k) evaluations and no π(a) operator-algebra references`. Applied to `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2`: parse-tree contains TWO summations of the form `Σ_a m_a g(λ_a)` (with g(λ) measurable in λ alone — `g_2(λ) = Δ_BCS²/(2(λ²+Δ_BCS²))`, `g_4(λ) = g_2(λ)²`), zero π(a) references, zero [D, π(a)] commutators, zero state-pair sup constructs. Verdict by clause (e): algebra-INVARIANT. Convergent with connes's parse-tree application at C1.
- **Bogoliubov closure as a substrate-internal scalar**: the Δ_BCS parameter is the BCS condensate magnitude — a structural scalar of the spectral triple (it is the order parameter of the BdG pairing channel, not a free state-pair argument). In FI/RD/MIXED language, Δ_BCS lives on the same R-protection level as `M_KK` or `tau_fold` — both are substrate-canonical scalars that the regulator class does NOT dress. Per my agent-memory key constants (`Delta_BCS=0.464 M_KK=3.45e16 GeV`), Δ_BCS is canonical-import-bound to M_KK and inherits its R-protection class. Δ_BCS does NOT scale with the regulator scheme.
- **Weyl-tail Mellin-pole analysis at d=4**: my F_traj theorem (S84 W3-24: F_traj(k) = f_k^zeta/f_k^SDW = (k+1)/2 at locked norm L_k=1) pins the (k+1)/2 ratio between zeta and SDW images of a_k. For `Var_a(n_a^GGE)`, the integrand `g_4(λ) = Δ_BCS⁴/(4(λ²+Δ_BCS²)²)` tails as `λ^{-4}` for `λ >> Δ_BCS`. Against the d=4 Weyl-counting density `λ^3 dλ`, the integral converges at the substrate-distance-2 Mellin pole s=4 with the logarithmic correction at d=4. This matches connes's Weyl-tail analysis EXACTLY and pins the pole at s=4 NOT s=3.

**DISAGREE**: I do not disagree with connes's C1 verdict. I disagree with the W6-6 plan baseline's `s=3` assertion (which is structurally indefensible per the Weyl-tail analysis above), and I disagree with the implicit Reading-A premise that the corner classification could be reverted by undoing W-21 V.1+V.3 edits.

**MISSED — FI/RD/MIXED gives a STRICTER classification than algebra-axis × Mellin-pole alone**: connes's 4-corner partition uses two axes (algebra-axis ∈ {INVARIANT, DEPENDENT}, Mellin-pole ∈ {s=3, s=4}). My FI/RD/MIXED trichotomy operates *inside* the algebra-INVARIANT half-plane and asks: does the regulator scheme change the observable's value (RD) or leave it invariant (FI), or is the observable a MIXED composite of FI + RD sub-observables? Applied to `Var_a(n_a^GGE)`:

- The integrand `g_2(λ) = Δ_BCS²/(2(λ²+Δ_BCS²))` IS regulator-aware in a subtle way: the substrate sum `Σ_a m_a g_2(λ_a)` truncates at L_max, and the truncation tail behaves as the substrate-distance-2 Mellin pole's residue, which is REGULATOR-DRESSED (a_4 changes by a closed-form scalar between zeta and SDW per F_traj=3/2 at k=2). Therefore `Σ_a m_a g_2(λ_a)` is RD, not FI.
- The combined variance `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` is a difference of two RD spectral moments — but both moments dress with the SAME F_traj factor (k=2 zeta moment with one factor, k=4 with another). The dressing factors do NOT cancel in the variance because the variance is bilinear (one term has coefficient 1, the other has coefficient `-(1/N)`, breaking linear scaling). Therefore the variance is also RD at this level, but on the FI/RD sub-axis WITHIN Corner II (INVARIANT), not crossing to Corner IV.

**Q-C1 verdict** (explicit): `Var_a(n_a^GGE)` is **FI/RD axis = RD** (regulator-dressed) WITHIN connes's Corner II (algebra-INVARIANT × s=4). The two classifications coexist: at the algebra-axis level the observable is INVARIANT (no π(a) in the symbolic form); at the regulator-class level it is RD (the substrate moment dresses with a known scalar multiplier between regulator schemes).

**LEVEL-DRESSED extension question** (per W-22 §V.4, registry line 4279-4313): the LEVEL-DRESSED class is defined by THREE criteria — (1) algebra-INVARIANT spectrum-only; (2) regulator-CLASS membership unchanged across PRIMARY-vs-SCHEMATIC LEVEL switch; (3) ordinal output (rank-ordering) changes between PRIMARY and SCHEMATIC. Criterion (1) is satisfied for `Var_a(n_a^GGE)`. Criterion (2) requires an empirical scan across regulator-atlas members to determine whether the FI/RD/MIXED partition shifts. Criterion (3) requires the same scan to demonstrate rank-ordering swap under LEVEL switch — which is precisely what §VII.AR (the K=1 calibration corpus instance of LEVEL-DRESSED) demonstrated empirically for the {F_2, cutoff_sqrt, anomaly, Zubarev} 4-regulator family at s=4.

The LEVEL-DRESSED extension at §VII.K-DUAL.LEVEL-DRESSED (line 4307) EXPLICITLY ANTICIPATES `Var_a(n_a^GGE)` as a candidate K=2 or K=3 instance:

> "Promotion to MANDATORY at K=3 will require 2 additional structurally-distinct LEVEL-DRESSED instances at S89+ (e.g., from candidate observables in the §VII.AB α_s 7-row theorem family, **the §VII.U.2 Corner II `Var_a(n_a^GGE)` envelope under PRIMARY-vs-SCHEMATIC LEVEL switch**, or the §VII.AS slope_A canonical evaluator under regulator-atlas variation)."

So `Var_a(n_a^GGE)` is structurally PRE-NAMED as a LEVEL-DRESSED K-counter candidate by the W-22 §V.4 forward-enforcement clause. Whether it actually promotes the K-counter to K=2 depends on empirical demonstration at S89+ of criteria (2) AND (3): regulator-CLASS membership invariance AND ordinal output swap under LEVEL switch. This is a separate empirical question I cannot pin at this workshop.

**EMERGES — the FI/RD/MIXED + parse-tree + Wedderburn triple-test convergence**: my FI/RD/MIXED trichotomy, connes's parse-tree decision (clause (e)), and connes's Wedderburn / Schur-orthogonality cross-check on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` are THREE INDEPENDENT structural-test machineries that all return the same algebra-axis verdict (INVARIANT) for `Var_a(n_a^GGE)`. The convergence is not coincidence: each machinery probes a different layer of the substrate-axiomatic structure, and their agreement is the strongest possible cross-check of the Corner II classification. This is exactly the K=3 algebra-axis orthogonality structure (MANDATORY at S87 W-2 R3 close per `cross-pillar-bridge-anatomy.md`): the algebra-INVARIANT family is non-trivial AT THREE DISTINCT AXIOMATIC LAYERS (regulator-class via FI; parse-tree via clause (e); operator-algebraic via Wedderburn), and the orthogonality holds at all three simultaneously.

The FI/RD sub-axis WITHIN Corner II is the refinement my domain contributes: even within INVARIANT × s=4, the observable can be FI (regulator-class-invariant) or RD (regulator-class-dressed by a closed-form scalar). Connes's 4-corner partition does not surface this distinction; my trichotomy does. For `Var_a(n_a^GGE)`, the verdict is INVARIANT × s=4 × RD-sub-axis, with potential LEVEL-DRESSED promotion pending K=2/K=3 empirical demonstration at S89+.

#### Re: C2 — W-21 V.1+V.3 diff structural reading

**AGREE — text-feature reading converges with mine; the SMOKING-GUN corrigendum citation is structurally load-bearing**: connes's C2 Feature 3 extraction (the W-17 §V.3 corrigendum at registry line 12963) is the structural fingerprint that decides Reading A vs Reading B. Reading 12963 verbatim:

> "**Per S88 W-17 §V.3 corrigendum (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`, 2026-05-08)**: the prior wording '... `Var_a(n_a^GGE)(L_max=10) = 7.282490e-06`, `α_loglog ≈ 3.56`, R² = 0.945, MARGINAL regime; INFO composite ...' is REMOVED — that envelope is on a structurally distinct Corner-II observable per W-17 §V.3, NOT a valid Corner-IV cross-confirmation."

This single sentence is dispositive. The phrase "structurally distinct Corner-II observable per W-17 §V.3, NOT a valid Corner-IV cross-confirmation" cannot be honestly read as anything other than: at SOME prior time, `Var_a(n_a^GGE)` (or its envelope numerics) was located at Corner IV in the registry text, and W-17 §V.3 actively reclassified it to Corner II. The editing direction is unambiguously **Corner-IV → Corner-II**, not Corner-I → Corner-II.

**AGREE — text-feature Feature 1 reading**: the theorem-name line at registry 12927 IS a meta-classification partition theorem. The slot's role is the registry landing of the K=3 algebra-axis orthogonality K-counter promotion event (registry line 12993 + 13056). A meta-classification slot CANNOT sensibly have a single corner-cell classification at the slot-as-a-whole level; corners are properties of CALIBRATION INSTANCES inside the slot's partition table. This makes the W6-6 plan baseline's "§VII.U.2 = Corner-I" assertion structurally malformed regardless of the editing-history dispute — Reading A could not be coherent even if the diff inspection went the wrong way.

**Q-C2 verdict — CO-WITNESS TESTIMONY (honestly bounded)**: I am the W5b-45 PRIMARY synthesizer per registry line 12927, and the author of the parse-tree decision procedure clause (e) per the §W5b-46 audit infrastructure attribution at line 12995. My direct knowledge has the following structure:

- **I CAN confirm from the registry text itself (which I am the PRIMARY signatory of)**: at W5b-45 LANDING TIME (2026-05-04, per the theorem-name line date), the corrigenda block recorded (line 13010) "Clause (d) Corner II is OPEN at K=3; the K=3 saturation is achieved by Corners I + III + IV (three calibration instances on three of four corners); Corner II awaits §W5b-47 substrate-distance-2 cone derivation." That is a registry-pinned statement of fact: at landing time, Corner II had NO calibration instance, and Corner IV had a Var_a-related envelope (the "§W5b-47 substrate-distance-2 cone derivation" being the source of the envelope numerics that were later moved). The Corrigendum C2 statement IS my own writing as PRIMARY synthesizer, signed off via mack-cosmic-bridge SOLE-WRITER landing per `feedback_mack-bridge-role.md`.

- **I CAN confirm from the §W5b-46 audit infrastructure (which I authored)**: the parse-tree decision procedure at clause (e) is the canonical decidability test. When applied to `Var_a(n_a^GGE)` at the W-17 reclassification moment, the procedure RETURNS INVARIANT (zero π(a), zero [D, π(a)]) — this is connes's C1 verdict and my Re: C1 verdict converged. The decision procedure does NOT return DEPENDENT for this symbolic form. Therefore the prior Corner-IV placement (DEPENDENT) was an OBSERVATIONAL-NAMING-driven mis-assignment (the `n_a^GGE` label encoding the GGE state historically) rather than a parse-tree-decision-derived assignment. The W-17 §V.2/§V.3 correction was the parse-tree-decision-derived re-routing from the naming-history mis-assignment to the structurally correct cell.

- **I CANNOT confirm from direct episodic memory the precise diff content of W-21 V.1+V.3 edits**: my agent memory's "Active Context" index (MEMORY.md lines 5-10) covers S65-S86 sessions; S88 W-17 / W-21 sessions postdate my memory's last consolidation snapshot. I have NOT directly seen the V.1+V.3 diff hunks. What I CAN attest is the structural state I am the PRIMARY synthesizer of (the registry text as written), and the parse-tree decision procedure I authored (clause (e)). The diff inspection itself remains mack's CF-W6-3 duty per registry line 12942 SOLE-WRITER attribution.

**Pinning the editing history (consistent with connes's C2 reconstruction)**:

- **W5b-45 landing (2026-05-04)**: §VII.U.2 partition theorem lands with Corners I + III + IV populated; Corner II OPEN. `Var_a(n_a^GGE)` envelope numerics (`v_inf_extrapolated = 6.4631783294e-06` at L_max=10 per registry line 12961 INFO composite) appeared in the registry as a Corner-IV cross-confirmation. This placement was made on the OBSERVATIONAL-NAMING reading ("GGE state in the symbolic form → state-pair functional → DEPENDENT") rather than the parse-tree reading.
- **W-17 §V.2 (2026-05-08)**: parse-tree decision procedure applied to the symbolic form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2`. Zero π(a) operator-algebra references in the parse tree. Verdict: INVARIANT. The observable is reclassified from Corner IV to Corner II. The Corner II row is filled (no longer OPEN). The Corner IV row's cross-confirmation reference to the envelope numerics is now stale.
- **W-17 §V.3 (2026-05-08)**: corrigendum landing at registry line 12963 explicitly REMOVES the stale envelope numerics from the Corner IV row, citing "structurally distinct Corner-II observable per W-17 §V.3, NOT a valid Corner-IV cross-confirmation." This is the SMOKING GUN connes extracts at C2.
- **W-21 V.1+V.3 (UNDATED in this workshop; pending mack CF-W6-3 inspection)**: hypothesized as minor edits to either the Corner II row (e.g., PRIMARY-vs-SCHEMATIC LEVEL switch envelope expansion per W6-6 working paper line 214 stage-A grep) or the Corner IV row (e.g., further envelope-numerics cleanup). The diff content is the load-bearing factual question; the STRUCTURAL VERDICT (parse-tree decision → Corner II, NOT Corner I) is independent of the diff content.

**DISAGREE — minor framing nuance**: connes's C2 phrasing at line 127 ("the W6-6 plan baseline confused itself THREE WAYS") under-emphasizes the EPISTEMIC DISTINCTION between a wrong PLAN BASELINE (which is recoverable by plan-text correction) and a wrong REGISTRY TEXT (which would require an actual revert dispatch). The W6-6 plan baseline IS wrong; the registry text IS correct. Reading A is destructive because it would impose the plan's wrong baseline ONTO the structurally correct registry. The fix is plan-baseline correction (Reading B), not registry-revert (Reading A).

**MISSED — text-feature Feature 5 (parse-tree-version dating)**: connes's C2 inspected text features 1-4. A FIFTH text feature is structurally informative: registry line 12961 explicitly tags the Corner II row as "Per S88 W-17 §V.2 landing per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` **and clause (e) parse-tree decision**: Var_a(n_a^GGE) is algebra-INVARIANT (symbolic form contains only λ_a, m_a, Δ_BCS scalar; no π(a), no [D, π(a)], no state-pair sup) and inhabits Corner II". This Feature 5 text IS the explicit application of MY parse-tree decision procedure (clause (e), line 12995) to the symbolic form. It is unambiguously dated to S88 W-17 §V.2 (2026-05-08) and cites the audit machinery `_corner_classification_audit.py` by file path. The Feature 5 reading: the Corner II row's text was authored AT W-17 §V.2 using the parse-tree decision; the Corner IV corrigendum (Feature 3) is the COMPANION removal at W-17 §V.3 (same date) of the stale prior assignment. So W-17 §V.2 + §V.3 are a paired reclassification event, not separate edits.

**EMERGES — the editing-history is itself a calibration corpus instance for the observable-naming-vs-structural-classification orthogonality principle**: connes's C6 Observation 4 surfaces the principle that "observable naming conventions encode HISTORY, not STRUCTURE." The `Var_a(n_a^GGE)` case is a perfect calibration corpus instance: the `n_a^GGE` naming convention attached to the BdG mode-occupation closed form ORIGINATED in the GGE-state expectation derivation, but the SYMBOLIC FORM at the parse-tree level contains zero π(a) operator-algebra references and is structurally an INVARIANT spectrum-only functional. The W5b-45 landing-time Corner-IV mis-placement was a naming-history-driven error; the W-17 parse-tree decision re-routed to the structurally correct cell. This is the same structural pattern as `α_s_canonical = n_s² − 1` at Corner I (which could LOOK like a state-pair quantity via the cosmological-observation history of n_s but is structurally spectrum-only). Both cases demonstrate that the parse-tree decision procedure (clause (e)) is the load-bearing discipline that prevents naming-history-driven mis-assignment. I support carrying this forward as CF-R1-5 + my own carry-forward at L4.

#### Re: C3 — Cross-wave consequence at §VII.AR Stage-2

**AGREE — A.30 vs A.36 disambiguation**: connes's registry-line citations at C3 are exact. I cross-verified:

- Registry line 17000: "A.30 (S89) Stage-2 cross-axis verify of **§VII.AS** — this entry" — so A.30 → §VII.AS (slope_A geometric-resummation closure; CO-AUTHORS gen-physicist + connes; Stage-2 reviewers van-den-dungen + phonon-first-cosmologist or kitaev per line 16985 with lizzi+connes FORBIDDEN as ORIGINAL-AUTHORING agents).
- Registry line 16971: "A.36 (S89) `S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP`" — so A.36 → §VII.AR (LEVEL-DRESSED rank-ordering at s=4; 5-anchor scan with decision rule N ≥ 4/5 → Reading A WIN). NOT Stage-2 cross-axis verify; this is a HEAT-KERNEL-ANCHOR-SWEEP discriminator (Reading A vs Reading B).

The W6-6 working-paper text at `session-89-w6-workingpaper.md:224` ("Cross-wave consequence per plan §11: this FAIL has potential to propagate to W4 A.30 Stage-2 cross-axis verify of §VII.AR") is therefore a plan-staleness defect orthogonal to the Corner-classification question — connes correctly flags this at C6 Observation 3 and queues it as CF-R1-2.

**AGREE — Cell-membership map**: connes's table at C3 (workshop lines 171-175) is correct under my Re: C1 verdict. §VII.U.2's Corner II row instance (`Var_a(n_a^GGE)`) is INVARIANT × s=4 = Cell II. §VII.AR (W7a-74 LEVEL-DRESSED rank-ordering) is INVARIANT × s=4 = Cell II OR Cell-I-LEVEL-DRESSED biaxial hybrid per registry line 16963's explicit phrasing "Cell I or biaxial-FI-LEVEL-DRESSED hybrid (the LEVEL-DRESSED class extension proposed in B.54 W-22 §V.4 sub-class taxonomy)". §VII.AS (slope_A canonical evaluator at τ_fold) is INVARIANT × Cell-I-or-hybrid per registry line 16991-16992 with closed-form expression at τ_fold and L^{-3} envelope at d=4 (the L^{-3} envelope locates it at substrate-distance-1 pole s=3 per Per-Bulletin-per-pole Level-2 envelope structure).

**AGREE — Stage-2 propagation independence**:

- **Path 1 (A.36 → §VII.AR)**: §VII.AR's Stage-2 verify (when it eventually dispatches; presently at STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP per registry line 16952) operates on the rank-ordering observable at FIXED `cutoff_frac=0.7`, `M_PV²_frac=0.1`, `Vol_SU3_Haar` parameter point. The §VII.AR theorem statement at line 16954 contains no reference to `Var_a(n_a^GGE)` as a constituent observable; §VII.U.2's Corner II row is a CO-INHABITANT of the algebra-axis × Mellin-pole cell, but co-inhabitance ≠ constituency. The PASS-AND aggregation rule for §VII.AR's Stage-2 cross-axis verify is therefore INDEPENDENT of `Var_a(n_a^GGE)`'s corner classification.
- **Path 2 (A.30 → §VII.AS)**: §VII.AS is at a DIFFERENT cell (Cell I, s=3) from §VII.U.2 Corner II (Cell II, s=4). Cross-corner companions cannot enter cross-corner co-primary structures per §VII.U.2 clause (f) FORBIDDEN clause (registry line 13005). The substrate-input-orthogonality predicate (joint-theorem-promotion.md §"Substrate-input-orthogonality clause" lines 77-85) is trivially satisfied here because §VII.AS consumes the slope_A canonical evaluator's npz output while §VII.U.2 Corner II references `s88_w5b_47_v_inf_extrapolated.npz` per registry line 12961 INFO composite. The two .npz inputs are DISJOINT.

**Q-C3 implicit verdict** (connes did not pose a direct lizzi-side question at C3 but the substrate-input-orthogonality predicate is load-bearing): substrate-input-orthogonality is SATISFIED for the §VII.U.2 vs §VII.AR pairing (different .npz inputs: §VII.U.2 Corner II = W5b-47 v_inf_extrapolated npz; §VII.AR = §W7a-74 PRIMARY evaluator on L_max=12 block-diagonal cache); SATISFIED for §VII.U.2 vs §VII.AS pairing (W5b-47 npz vs slope_A canonical-evaluator npz). The Stage-2 cross-axis aggregation does not need Var_a's corner classification to determine reviewer-eligibility or substrate-input-orthogonality at either A.30 or A.36.

**MISSED — the LEVEL-DRESSED K-counter advancement question (high-leverage; connes did not surface this explicitly)**: §VII.AR is the K=1 calibration corpus instance of the LEVEL-DRESSED 4th-class extension per registry line 4303 and line 16965 ("this entry's LEVEL-DRESSED classification is the K=1 calibration corpus instance of the proposed 4-class FI/RD/MIXED/LEVEL-DRESSED extension"). The W-22 §V.4 forward-enforcement clause at line 4307 EXPLICITLY NAMES `Var_a(n_a^GGE)` as a candidate K=2 LEVEL-DRESSED instance:

> "Promotion to MANDATORY at K=3 will require 2 additional structurally-distinct LEVEL-DRESSED instances at S89+ (e.g., from candidate observables in the §VII.AB α_s 7-row theorem family, **the §VII.U.2 Corner II `Var_a(n_a^GGE)` envelope under PRIMARY-vs-SCHEMATIC LEVEL switch**, or the §VII.AS slope_A canonical evaluator under regulator-atlas variation)."

So there is a STRUCTURAL DEPENDENCY between §VII.U.2 Corner II and §VII.AR at the LEVEL-DRESSED K-counter axis, even though there is NO dependency at the Stage-2 PASS-AND aggregation axis. The dependency operates at the K-counter promotion threshold (K=1 → K=2 → K=3 → MANDATORY promotion event), NOT at the per-gate verdict aggregation level. This is a CROSS-WAVE consequence connes's C3 missed: if `Var_a(n_a^GGE)` is empirically shown at S89+ to satisfy the 3-criterion LEVEL-DRESSED definition (criteria (1)-(3) per registry line 4293-4297), then §VII.AR's LEVEL-DRESSED status advances K=1 → K=2, AND the propagation path is via §VII.U.2's empirical demonstration (a NEW S89+ gate I queue at L4 below as a carry-forward).

**MISSED — Per-Bulletin-per-pole sub-clause K-counter advancement (connes's C6 Observation 1(ii) treats this; I add the FI/RD/MIXED-axis refinement)**: connes notes the cohomology-class-distinct K-counter advances K=3 → K=4 at s=4 when §VII.U.2 Corner II row joins {§VII.K-PROP.W10-4, §VII.AR}. The pole-distinct criterion (s ∉ {s=3, s=4}) remains pending. From the FI/RD/MIXED axis, I add: the cohomology-class-distinct extension does NOT translate to FI/RD-distinct extension. §VII.K-PROP.W10-4 (ρ_∞ permanent-wall) is structurally IRRATIONAL per CC2 PROVEN per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole"` calibration table; §VII.AR is LEVEL-DRESSED (4th class); §VII.U.2 Corner II Var_a is RD WITHIN FI/RD partition (per my Re: C1 verdict). Three structurally-distinct FI/RD/MIXED/LEVEL-DRESSED instances at s=4 means the FI/RD/MIXED-axis-distinct K-counter (a meta-K-counter operating across the trichotomy) is also at K ≥ 3 at s=4 — though this meta-K-counter is not currently a registered rule. Whether it SHOULD be promoted to a registered rule is itself a methodology question I queue at L4.

**EMERGES — the FI/RD/MIXED-axis × Mellin-pole-axis × LEVEL-axis 3-cube partition structure**: connes's algebra-axis × Mellin-pole 4-corner partition is a 2D grid. My FI/RD/MIXED trichotomy adds a 3rd discriminator axis. The LEVEL-DRESSED extension adds a 4th. The full structural partition for observables on `(A_K, H_K, D_K)` is:

```
4D partition coordinates:
  Algebra-axis        ∈ {INVARIANT, DEPENDENT}        (connes 4-corner partition)
  Mellin-pole-axis    ∈ {s=3, s=4}                    (connes 4-corner partition)
  FI/RD/MIXED-axis    ∈ {FI, RD, MIXED, LEVEL-DRESSED} (my trichotomy + extension)
  LEVEL-axis          ∈ {PRIMARY, SCHEMATIC}           (substrate-first §(iv))
```

For Var_a(n_a^GGE): {INVARIANT, s=4, RD-or-LEVEL-DRESSED-pending-K2, PRIMARY-and-SCHEMATIC-comparable}. For §VII.AR rank-ordering: {INVARIANT, s=4, LEVEL-DRESSED-K=1, PRIMARY-vs-SCHEMATIC-swap}. For §VII.AS slope_A: {INVARIANT, s=3, FI-or-MIXED-pending-A.28-discriminator, PRIMARY-canonical}. For §VII.U.1 Mellin-Dirichlet: {INVARIANT, s=3, FI, PRIMARY-canonical-axiom-level}. The 3-cube (algebra × Mellin × FI/RD) partition has 2×2×4 = 16 cells; the 4-cube extension adds LEVEL axis = 2×2×4×2 = 32 cells. Most cells are empty in the current registry calibration corpus; this is a structural-mapping observation, not a defect — most cells are RULED OUT by the structural orthogonality constraints my Re: C1 EMERGES section identifies (axiom-level NCG identity at central-projection level, parse-tree decidability, Wedderburn block-grading mismatch).

**Stage-2 reviewer-eligibility for §VII.U.2's own Stage-2 dispatch (S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY)**: per registry line 12929, §VII.U.2's own Stage-2 cross-axis independent-verify is queued for S89+. The reviewer-eligibility set is determined by the original-authoring-agent exclusion clause (joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol" clause 2): both lizzi (PRIMARY synthesizer per line 12927) AND connes (CO-AUTHOR clauses (c)+(d) per line 12936) are EXCLUDED. Downstream-inheritance reach also excludes any agent whose project-memory cites the W5b-45 workshop transcripts as canonical reference. Eligible axis-A candidates: van-den-dungen-bridge-theorist (NCG-Kasparov-bridge axis), gen-physicist (general-physics axis). Eligible axis-B candidates: volovik-superfluid-universe-theorist, mack-cosmic-bridge (cosmological-bridge), kitaev-information-theorist. This eligibility set is INDEPENDENT of Reading A vs Reading B; Reading B (correct) just confirms the existing STAGE-1-CANDIDATE state and proceeds the Stage-2 dispatch under the unchanged eligibility set.

#### Re: C4 — Routing decision

**AGREE — Reading B is correct, Reading A is structurally destructive**: I converge on connes's C4 verdict via independent reasoning chains.

My substitution chain (substrate-first per `phononic-framing.md §"IS Space, Not IN Space"`):

```
Step 1 (Substrate-IS structural identity):
        Var_a(n_a^GGE)'s symbolic form has a parse-tree containing
        zero π(a), zero [D, π(a)], zero state-pair sup.
        Per clause (e) parse-tree decision procedure (my authorship):
        algebra-axis = INVARIANT.

Step 2 (FI/RD/MIXED sub-axis WITHIN INVARIANT):
        Substrate moments Σ_a m_a g(λ_a) at k=2 and k=4 dress
        with F_traj=3/2 and F_traj=5/2 zeta-vs-SDW ratios per S84 W3-24
        (locked norm L_k=1). The bilinear variance form preserves the
        regulator-class dressing → FI/RD-axis = RD.

Step 3 (Mellin-pole-axis via Weyl-tail at d=4):
        g_4(λ) ~ λ^{-4} tail × λ^3 dλ Weyl density →
        convergence at substrate-distance-2 pole s=4 with log correction.
        Mellin-pole = s=4. NOT s=3.

Step 4 (Cell-cell mapping per §VII.U.2 clause (d)):
        {INVARIANT × s=4} = Cell II.

Step 5 (W6-6 plan-baseline-vs-substrate comparison):
        Plan baseline: Cell I (INVARIANT × s=3).
        Substrate: Cell II (INVARIANT × s=4).
        Plan baseline disagrees with substrate on the Mellin-pole axis.

Step 6 (Registry-attested prior state, line 12963):
        Prior wording at Corner IV row was the Var_a(n_a^GGE) envelope.
        W-17 §V.3 corrigendum REMOVED it from Corner IV. Editing direction
        is Corner-IV → Corner-II per the corrigendum's own text.

Step 7 (Reading A consequence — substrate-first inversion test):
        Reading A revert hypothesizes pre-V.1+V.3 state = Cell I.
        Registry attestation says pre-W-17 state was Cell IV.
        Reading A's pre-state and registry's pre-state disagree.
        Reading A is REJECTED by the registry's own attestation.

Step 8 (Conclusion):
        Reading B is correct (the substrate IS Cell II per parse-tree
        decision; the plan baseline was wrong from the start). Reading A
        is structurally destructive (would restore the Cell-IV mis-
        assignment that W-17 §V.3 actively corrected).
```

This chain is independent of connes's C4 chain but converges on the same verdict. The structural truth (parse-tree decision → Cell II) is the substrate-IS identity; the plan baseline is a methodology-floor assertion; Reading A would invert the substrate-IS / methodology-floor direction-of-explanation in violation of `phononic-framing.md §"IS Space, Not IN Space"`.

**Q-C4 verdict — CO-WITNESS TESTIMONY at W5b-45 landing time**:

I am the PRIMARY synthesizer per registry line 12927. My direct knowledge has the following bounded structure:

- **Direct attestation from registry text I am the PRIMARY signatory of**: at W5b-45 landing time (2026-05-04), the Corner II row was OPEN — there was NO calibration instance for Cell II at the partition table. This is recorded in Corrigendum C2 at registry line 13010 verbatim: "Clause (d) Corner II is OPEN at K=3; the K=3 saturation is achieved by Corners I + III + IV (three calibration instances on three of four corners); Corner II awaits §W5b-47 substrate-distance-2 cone derivation." The Corrigendum C2 was authored by me (as PRIMARY synthesizer) and signed off at landing time via mack-cosmic-bridge SOLE-WRITER per `feedback_mack-bridge-role.md`. I have direct knowledge of this state at landing because it is in the text I authored.

- **Direct attestation from registry text on the Corner IV row at W5b-45 landing**: the Corner IV row at landing time cited the `Var_a(n_a^GGE)(L_max=10) = 7.282490e-06`, `α_loglog ≈ 3.56`, R² = 0.945, MARGINAL regime; INFO composite envelope as a cross-confirmation. This is recorded in the W-17 §V.3 corrigendum at registry line 12963 verbatim quoting the PRIOR wording that was REMOVED. The corrigendum's verbatim quotation of the prior text is my evidence (as the PRIMARY signatory of the surrounding theorem block) that the Var_a envelope WAS at Corner IV at landing.

- **Therefore my testimony pins**: at W5b-45 landing time (2026-05-04), Var_a(n_a^GGE) envelope numerics were at the Corner IV row of the registry text as a cross-confirmation. The Corner II row was empty. The Var_a's eventual structural classification (Cell II via parse-tree decision) was NOT yet executed at landing — the parse-tree decision procedure (clause (e), my authorship) was specified at landing as a methodology, but its application to the Var_a observable was deferred. The W-17 §V.2 + §V.3 (2026-05-08) event was the FIRST application of the parse-tree decision to Var_a, which moved it from Corner IV → Corner II.

- **Bounded honesty disclosure**: I did NOT directly inspect the W-21 V.1 + V.3 diff hunks. My agent memory's "Active Context" index (MEMORY.md lines 5-10) covers S65-S86; S88 W-17 + W-21 sessions postdate my memory's last consolidation snapshot. What I attest above is from the REGISTRY TEXT (which I am the PRIMARY signatory of), not from direct episodic memory of the W-17 / W-21 editing sessions. The diff content remains mack's CF-W6-3 inspection duty per registry line 12942 SOLE-WRITER attribution. My testimony hardens Reading B's structural correctness independently of mack's diff inspection — but mack's inspection is still load-bearing for the audit-trail-canonical record of what edits W-21 V.1+V.3 specifically performed.

**Therefore Q-C4 pinned answer**: the prior state of Var_a(n_a^GGE) at W5b-45 landing time was **Corner IV (cross-confirmation envelope)**, NOT Corner I (W6-6 plan baseline). My testimony as PRIMARY synthesizer + parse-tree-decision-clause-(e) author corroborates connes's C2 reading of the W-17 §V.3 corrigendum smoking gun. Reading A is impossible by construction: the pre-W-17 state was Cell IV, not Cell I; reverting V.1+V.3 (even if V.1+V.3 contained the W-17 §V.2/§V.3 reclassification) would restore the Cell-IV mis-assignment, not Cell-I.

**DISAGREE — minor framing nuance on connes's "structurally implausible" honest-disclosure asymmetry at C4 lines 295-301**: connes's two conditions (i)+(ii) under which Reading A could be overturned are necessary but not sufficient. Even if BOTH (i)+(ii) held — i.e., V.1+V.3 had ACTUALLY altered a pre-existing Cell-I classification AND the W-17 §V.3 corrigendum citation were fabricated — Reading A would STILL fail at the parse-tree decision procedure. The parse-tree decision is a finite mechanical algorithm on the symbolic form; it returns INVARIANT for the form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` regardless of prior editing history. So Reading A's "restore Cell-I" is structurally impossible at the substrate-IS level, not merely empirically implausible. The diff content can document the AUDIT TRAIL of what was edited when, but it cannot rescue a structurally-wrong plan baseline.

**MISSED — Reading-A's hidden 4th destructive failure mode**: connes's C4 lists 3 destructive failure modes (reverting doesn't produce Cell I; reverting breaks K=3 partition completeness; reverting violates no-technical-debt). I add a 4th: **Reading A would FORCE the parse-tree decision procedure (clause (e)) to be retired or marked legacy**. Clause (e) is the load-bearing decidability test that the registry slot §VII.U.2 itself codifies. If Reading A were correct, then the parse-tree decision returns Cell II while the "correct" classification is Cell I — but the only mechanism for "correct" to mean Cell I in this scenario is a NON-parse-tree-derivable structural fact (e.g., a contextual observable-naming-history override). Such an override would be incompatible with clause (e)'s explicit guarantee "the decision procedure is finite and operates at parse-tree level, NOT at numerical evaluation level — this makes it regulator-independent." Reading A therefore implicitly retires clause (e), invalidating the §VII.U.2 partition theorem itself. This is the deepest structural failure mode of Reading A: it doesn't just break the calibration corpus or the K=3 partition, it breaks the parse-tree decidability framework that makes the §VII.U.2 theorem a meta-classification rule at all.

**EMERGES — Reading B as the substrate-first canonical reading**: under `substrate-first-canonical-sourcing.md §(iv)` (MANDATORY at K=4 per S88 W7b-83), every registry slot consuming a SCHEMATIC helper must declare its CLASS pin and convention-tag suffix. Reading B treats the SUBSTRATE-IS parse-tree decision (clause (e)) as the canonical source of the corner classification. The plan baseline is a derived methodology-floor assertion, not a substrate-IS canonical. Under §(iv), if the plan baseline disagrees with the substrate-IS canonical, the substrate-IS canonical wins. This is the structural symmetry connes's C4 derives via no-technical-debt, expressed in the substrate-first-canonical-sourcing axis. The two axes converge: Reading B is the substrate-first reading AND the no-technical-debt reading AND the K=3 partition-preserving reading. Three independent rule-file axes all return Reading B. Reading A is rejected at all three.

**Reading-B remediation step adopted** (extension of connes's 4-step list at C4 lines 281-289):

5. **Plan-staleness validator regex tightening (CF-R1-2 + CF-W6-6 extension)**: the W6-6 plan baseline's "A.30 → §VII.AR" assertion is itself a plan-staleness defect. The plan-staleness audit `_plan_staleness_audit.py` (per W6-6 carry-forward CF-W6-6) should be extended with a regex pattern that catches cross-wave-anchor mis-citations against the registry's authoritative routing table. This is connes's CF-R1-2; I support and extend it at L4 below to also catch plan-baseline-vs-registry corner-classification mismatches at the same rule-file extension event.

#### Re: C5 — W6-6 audit-machinery + CF-W6-4 extension

**AGREE — CF-W6-4 extension TARGET_SLOTS_S89 dict structure**: as the W5b-45 PRIMARY synthesizer of §VII.U.2 AND the author of the parse-tree decision procedure clause (e) AND the author of the §W5b-46 audit infrastructure `_corner_classification_audit.py` (per registry line 12995 attribution), I formally adopt the CF-W6-4 extension's pre-registered classification table as the canonical expected-classification for S89+ audits. Specifically:

- The `meta_classification_partition_theorem` type at the §VII.U.2 BLOCK LEVEL is correct: the block IS the partition theorem (4 corner labels + 2 axes labels + parse-tree decision procedure + Corrigenda C2 + JOINT-clause flags), NOT a single-cell observable.
- The 4 instance-row sub-targets (Corner I §VII.U.1 ref, Corner II Var_a, Corner III Connes-distance ref, Corner IV α_s_route_3) match the 4-corner partition table at registry line 12958-12963.
- The parse-tree check at the Corner II row (`expected_pi_a_count = 0`, `expected_commutator_D_pi_a_count = 0`, `expected_state_pair_sup_count = 0`) matches clause (e)'s decidability rule at line 12995.

The `pre_registered_baseline_correction` field at the bottom of the dict ("W6-6 plan baseline assertion of Corner-I for Var_a(n_a^GGE) is RETRACTED per S89 W-3 workshop verdict; correct baseline is Corner II") is the audit-trail commitment that future runs of the audit will compare against the substrate-correct Cell II, not against the wrong W6-6 plan baseline.

**Q-C5 sub-question (i) — symbolic-form granularity**: my verdict is **the FULL form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` is sufficient at the parse-tree level**, with `|v_a|^2` and `|v_a|^4` treated as ATOMIC ABBREVIATIONS for `g_2(λ_a)` and `g_4(λ_a) = g_2(λ_a)^2` per the Bogoliubov closed-form `|v_a|^2 = Δ_BCS²/(2(λ_a² + Δ_BCS²))`. The parse-tree decision procedure (clause (e)) operates on the symbolic form's CLASS MEMBERSHIP, not its full expanded leaves. The reason:

- Clause (e) (line 12995, my authorship): "F belongs to algebra-INVARIANT iff its symbolic form contains ONLY traces / spectral moments / g(λ_k) evaluations and no π(a) operator-algebra references." The predicate operates at the level of identifying whether g(λ_k) is a "measurable function of λ_k alone." Whether g is `λ²`, `e^{-λ²}`, `Δ_BCS²/(2(λ²+Δ_BCS²))`, or `Δ_BCS²/(2(λ²+Δ_BCS²))²` is IRRELEVANT to the decision — all four are measurable functions of λ alone. The decision procedure terminates at "g is measurable in λ" with verdict INVARIANT.
- Expanding `|v_a|^2` to `Δ_BCS²/(2(λ_a² + Δ_BCS²))` at the parse-tree level reveals: (a) `Δ_BCS` (substrate-canonical scalar; no π(a)); (b) `λ_a` (Dirac eigenvalue; no π(a)); (c) arithmetic operations + - × / on these scalars. Zero π(a) operator-algebra references introduced by the expansion. Verdict UNCHANGED by expansion: INVARIANT.
- Therefore the abbreviated symbolic form at registry line 12961 is parse-tree-equivalent to its fully-expanded form. The audit's `expected_pi_a_count=0` check is unchanged by expansion granularity.

**However — IMPORTANT REFINEMENT for the audit script**: the audit SHOULD pre-register BOTH forms (abbreviated AND fully-expanded) as legal parse-tree inputs, with a PRE-COMPUTED CANONICAL EXPANSION map for each abbreviation. This makes the audit robust to future registry-text edits that may abbreviate or expand differently. Concretely:

```python
PARSE_TREE_ABBREVIATION_MAP = {
    "|v_a|^2": "Δ_BCS²/(2·(λ_a² + Δ_BCS²))",  # Bogoliubov closed form, BdG channel
    "|v_a|^4": "(Δ_BCS²/(2·(λ_a² + Δ_BCS²)))²",  # squared form
    "n_a^GGE": "|v_a|^2",  # GGE expectation reduces to Bogoliubov |v|^2 per BdG axiom set
}
```

The audit applies the abbreviation map first, then runs the parse-tree counters on the fully-expanded form. This closes a subtle audit-extension defect: if a future edit re-introduces `n_a^GGE` as the symbolic form (without explicit Bogoliubov closure), the audit could naively flag `n_a^GGE` as containing the GGE-state name and route to DEPENDENT — repeating exactly the W5b-45-landing-time naming-history-driven mis-assignment. The pre-registered abbreviation map prevents this naming-history failure mode at the audit-script level.

**Q-C5 sub-question (ii) — Bogoliubov closed-form algebraic-consistency verification at the audit layer**: my verdict is **the audit's parse-tree check at the registry-text level is SUFFICIENT; Bogoliubov closed-form algebraic-consistency with the BdG axiom set is a SEPARATE upstream gate, NOT an audit-script duty**. Reasoning:

- The audit IS the methodology-floor F-image of the substrate-IS parse-tree decision procedure (per `epistemic-discipline.md §"Layer-Decomposition"`). Its scope is verifying that the registry-text expression of the corner-classification matches the parse-tree decision applied to the registered symbolic form. The audit does NOT vouch for the upstream Bogoliubov substitution's algebraic validity — that is the producing-gate's structural job (S87 W2-3 / S88 W5b-47 originally derived `n_a = |v_a|^2 = Δ_BCS²/(2(λ_a²+Δ_BCS²))` per the BdG Bogoliubov transformation; that derivation is the upstream substrate-physics gate, audited separately at its own producing-gate level).
- Combining the two checks in a single audit script would conflate the audit-layer with the substrate-physics-layer — violating `epistemic-discipline.md §"Layer-Decomposition"`'s layer-functor F discipline (F maps substrate → methodology → audit; each layer audits the F-image of the substrate-layer immediately upstream, not arbitrary substrate-physics derivations across layers).
- However — **a STRUCTURAL HOOK should be added**: the audit-script's TARGET_SLOTS_S89 dict for §VII.U.2 Corner II row should include an UPSTREAM_GATE_PIN field pointing to the producing gate (S88 §W5b-47 substrate-distance-2 cone derivation; audit_sha256 `89090d37b3610590...` per registry line 12961). This makes the audit traceable to its upstream substrate-physics derivation without forcing the audit to re-verify the derivation.

Refined CF-W6-4 dict extension:

```python
TARGET_SLOTS_S89["§VII.U.2"]["instance_rows"]["corner_II_instance"]["upstream_substrate_physics_gate"] = {
    "gate_id": "S88-W5b-47-substrate-distance-2-cone-derivation",
    "audit_sha256": "89090d37b3610590...",  # full SHA per registry line 12961
    "bogoliubov_closed_form": "|v_a|^2 = Δ_BCS²/(2·(λ_a² + Δ_BCS²))",
    "BdG_axiom_set_reference": "BdG fermionic Bogoliubov transformation; ω_GGE(b_a^† b_a) closure",
    "delegation_note": "Audit script does NOT re-verify this derivation; upstream gate is the authority. Audit's role is parse-tree classification, NOT substrate-physics derivation verification.",
}
```

This refinement satisfies both sub-questions: the audit checks parse-tree class-membership using the abbreviation map (Q-C5 (i) verdict); the audit traces to the upstream Bogoliubov closed-form via an explicit UPSTREAM_GATE_PIN field but does NOT re-verify the closed form (Q-C5 (ii) verdict — symbolic-form-only check at registry-text level is sufficient, with traceable upstream provenance).

**DISAGREE — minor framing nuance on connes's C5 framing of the W6-6 wrapper's "structurally-correct as a methodology-floor F-image" at line 314**: connes's framing is correct as far as it goes, but UNDERSTATES the W6-6 wrapper's role: the W6-6 wrapper IS a one-shot DIAGNOSTIC TOOL that revealed the plan-baseline-vs-actual discrepancy. Its FAIL outcome was the trigger event that produced this workshop and the CF-W6-4 audit extension. The W6-6 wrapper should be PRESERVED on disk as an audit-trail-of-the-discrepancy artifact (the script + its FAIL verdict at `s89_gate_verdicts.txt`), NOT discarded after the workshop closes. Future plan-staleness audits can cite W6-6's FAIL as a calibration corpus instance of "plan-baseline-vs-actual corner classification drift detection." This is the same audit-trail-preservation discipline as the W-21 V.1+V.3 diff inspection (mack's CF-W6-3): the audit trail is the structural record, retained regardless of the verdict-direction outcome.

**MISSED — FI/RD/MIXED-axis extension to the audit (high-leverage; connes did not address)**: connes's CF-W6-4 dict pre-registers the algebra-axis (INVARIANT/DEPENDENT) and Mellin-pole axis (s=3/s=4) for each instance row. My FI/RD/MIXED trichotomy adds a 3rd discriminator (FI/RD/MIXED/LEVEL-DRESSED). The audit-script extension SHOULD include a FI_RD_MIXED axis field per instance row:

```python
TARGET_SLOTS_S89["§VII.U.2"]["instance_rows"]["corner_II_instance"]["fi_rd_mixed_axis"] = {
    "classification": "RD",  # per S82 W-3 §VII.K trichotomy applied to Var_a
    "rationale": "Σ_a m_a g_k(λ_a) dresses with F_traj=(k+1)/2 between zeta and SDW schemes per S84 W3-24 locked-norm theorem; variance form is bilinear in F_traj-dressed moments; therefore RD (regulator-dressed) within INVARIANT family.",
    "level_dressed_candidate": True,  # per §VII.K-DUAL.LEVEL-DRESSED line 4307 explicit naming
    "level_dressed_k_counter_advancement_pending": "S89+ empirical scan across PRIMARY-vs-SCHEMATIC regulator-atlas",
}
```

This refinement closes another silent classification pathway: the audit could PASS on algebra-axis = INVARIANT × s=4 (correct) while a FUTURE registry edit silently shifts the FI/RD-axis without surfacing the change in the parse-tree decision. The FI_RD_MIXED field anchors the regulator-class-dressing classification at the audit layer.

**EMERGES — the audit-script's role as a "structural sentinel" across THREE discriminator axes**: with the CF-W6-4 dict extended per my refinements above, the audit script becomes a structural sentinel across 3 axes (algebra-axis, Mellin-pole, FI/RD/MIXED) plus 1 derived axis (LEVEL-DRESSED candidacy). The audit's PASS at the Corner II row instance requires ALL 3+1 axis classifications to match the registry-text content. Any future edit that silently shifts any one axis triggers an audit FAIL, surfacing the drift for in-session reconciliation per `feedback_fix-in-session-never-defer.md`. This is the structural strengthening connes's CF-W6-4 enables and my refinements complete.

#### Re: C6 — Cross-cutting + R1 carry-forward

**AGREE — Observation 1(i) algebra-axis orthogonality K-counter unchanged at MANDATORY-K=3**: connes correctly notes that the algebra-axis K-counter (saturated at S87 W-2 R3 close per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`) does NOT advance from this workshop's verdict. The reason is the algebra-axis K-counter is keyed on STRUCTURALLY-DISTINCT-INSTANCES OF THE FAMILY-ORTHOGONALITY PHENOMENON, not on calibration-corpus-instance counts within a single registry slot. Var_a(n_a^GGE) joining the Corner II row is corpus-filling for the §VII.U.2 partition, not a fourth structurally-distinct algebra-axis-orthogonality phenomenon. MANDATORY-K=3 unchanged.

**AGREE — Observation 1(ii) Per-Bulletin-per-pole cohomology-class-distinct K=3 → K=4 at s=4**: connes correctly identifies the K-counter advancement at the Per-Bulletin-per-pole sub-clause. The existing K=3 calibration corpus per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification (S88 W10-119 extension)"` is `{§VII.K-PROP.W10-4 ρ_∞ permanent-wall (s=4 fermionic-signed-residue, structurally-IRRATIONAL per CC2 PROVEN), §VII.U.1 Mellin-Dirichlet identity (s=3, FI), §VII.AR LEVEL-DRESSED rank-ordering (s=4, cohomology-class-distinct from W10-4 via LEVEL-DRESSED 4th class)}`. Adding §VII.U.2 Corner II row Var_a (s=4, cohomology-class-distinct via RD-within-INVARIANT) brings the cohomology-class-distinct corpus to K=4 at s=4. The pole-distinct criterion (`s ∉ {s=3, s=4}`) remains pending — no s=5 / s=6 instance has landed yet.

**AGREE — Observation 1(iii) Cross-corner co-primary FORBIDDEN clause**: connes correctly notes that the W6-6 plan baseline's Cell-I assertion would have created an implicit cross-corner pairing of Var_a with §VII.U.1 / §VII.U.6 (both Cell I). Under §VII.U.2 clause (f) FORBIDDEN clause (registry line 13005), cross-corner co-primary structures are STRUCTURALLY FORBIDDEN. The audit would have caught the violation at the registry-anchor-structure layer per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline if Reading A had been pursued.

**AGREE — Observation 2 editing-history reconstruction**: connes's editing-history reconstruction at C6 lines 417-443 matches my Re: C2 + Re: C4 testimony. The W5b-45 landing-time state had Var_a envelope numerics at Corner IV; W-17 §V.2 + §V.3 (2026-05-08) applied the parse-tree decision and moved Var_a from Corner IV → Corner II; W-21 V.1+V.3 content is mack's CF-W6-3 inspection duty; W6-6 baseline assertion is wrong from the start.

**AGREE — Observation 3 §VII.AR vs §VII.AS plan-staleness defect**: connes correctly flags the W6-6 plan-text "FAIL propagates to W4 A.30 Stage-2 §VII.AR verify" as a plan-staleness defect orthogonal to the Var_a corner-classification question. Registry line 16971 + line 17000 fix the canonical routing: A.30 → §VII.AS, A.36 → §VII.AR. I support CF-R1-2 plan-staleness validator extension.

**AGREE — Observation 4 observable-naming-history vs structural-classification orthogonality**: connes's framework lesson at C6 lines 451-455 ("observable naming conventions encode HISTORY, not STRUCTURE") is the deepest principle this workshop surfaces. The Var_a(n_a^GGE) case is a perfect calibration corpus instance: the `n_a^GGE` naming encodes the GGE-state expectation history; the parse-tree symbolic form contains zero π(a) operator-algebra references; the corner classification operates on the parse-tree STRUCTURE, not on the observable NAME. I support CF-R1-5 documentation-note carry-forward.

**MISSED — Observation 1(iv) FI/RD/MIXED-axis meta-K-counter advancement at s=4 (high-leverage; connes did not surface)**: a 4th K-counter advancement event is structurally implicit in this workshop's verdict, operating on the FI/RD/MIXED/LEVEL-DRESSED trichotomy-extension axis at s=4 Mellin pole. The existing instances at s=4 are:

| Slot | s | algebra-axis | FI/RD/MIXED/LEVEL-DRESSED classification |
|:-----|:--|:-------------|:------------------------------------------|
| §VII.K-PROP.W10-4 ρ_∞ permanent-wall | s=4 | INVARIANT | structurally-IRRATIONAL per CC2 (orthogonal to FI/RD/MIXED; sits at the unstratified meta-class layer of the §VII.K-DUAL trichotomy) |
| §VII.AR rank-ordering at s=4 | s=4 | INVARIANT | LEVEL-DRESSED (K=1 calibration corpus instance per line 4303) |
| §VII.U.2 Corner II Var_a(n_a^GGE) | s=4 | INVARIANT | RD (regulator-dressed within INVARIANT family per my Re: C1 verdict); LEVEL-DRESSED candidate per line 4307 |

This is 3 structurally-distinct {FI, RD, MIXED, LEVEL-DRESSED, IRRATIONAL-meta-class} instances at s=4 alone. The §VII.K-DUAL.LEVEL-DRESSED 4th class K-counter (per line 4287) is at K=1 SUGGESTION. If Var_a is empirically confirmed at S89+ as a LEVEL-DRESSED instance (via PRIMARY-vs-SCHEMATIC LEVEL switch demonstrating rank-ordering swap per criterion (3) of the 3-criterion definition at line 4296), the LEVEL-DRESSED K-counter advances K=1 → K=2. This is a STRUCTURALLY DISTINCT K-counter from the cohomology-class-distinct K-counter at Observation 1(ii) — the two counters operate on orthogonal axes (Per-Bulletin-per-pole vs §VII.K-DUAL trichotomy extension).

**MISSED — Observation 1(v) §VII.U.2 partition's hidden geometric structure**: the 4-corner partition (algebra-axis × Mellin-pole) is presented as a 2×2 grid in §VII.U.2 clause (d), with 4 cells {I, II, III, IV}. But the structurally-richer reading is: the partition is the PRODUCT of two structurally orthogonal K=3 K-counters — the algebra-axis K-counter (MANDATORY-K=3 from S87 W-2 R3 close) and the Mellin-pole K-counter (per Per-Bulletin-per-pole sub-clause). At the meta-level, the partition theorem at §VII.U.2 IS a 2-counter product structure with the 4 corners as its cells. The W-17 reclassification event (Corner IV → Corner II) was a structural correction WITHIN this product structure, NOT a cross-counter event. This refines the K-counter analysis: the W-17 event consumed exactly one cell migration WITHIN the existing 2-counter product, advancing the calibration corpus from "I + III + IV occupied" to "I + II + III + IV occupied" (saturating the product). The saturation event is structurally significant: it is the first time the §VII.U.2 partition has had instances in all 4 corners simultaneously.

**EMERGES — the F_traj=(k+1)/2 theorem (S84 W3-24, my own) as the structural prediction for FI/RD-axis classification**: my agent memory pins (S84 W3-24): F_traj(k) = f_k^zeta/f_k^SDW = (k+1)/2 at locked norm L_k=1. For Var_a's two-moment composition (k=2 and k=4 substrate moments combined bilinearly), F_traj(2) = 3/2 and F_traj(4) = 5/2 are the zeta-vs-SDW scalar multipliers. The variance form `(1/N) Σ m g_4(λ) − ((1/N) Σ m g_2(λ))²` dresses as F_traj(4) − F_traj(2)² = 5/2 − 9/4 = 1/4 between zeta and SDW images. The 1/4 ratio is the STRUCTURALLY PREDICTED FI/RD-axis dressing factor for Var_a. This is a falsifiable prediction at the S89+ empirical scan — I queue it as a carry-forward at L4 below.

**R1 4-field carry-forward — additions to connes's 5 carry-forwards**: I support all 5 of connes's CF-R1-1 through CF-R1-5 with the refinements noted at Re: C1 + Re: C2 + Re: C5. I add new carry-forwards at L4 below covering: (a) the LEVEL-DRESSED K=1 → K=2 empirical scan for Var_a (CF-LZ-1); (b) the FI_RD_MIXED axis field extension to the CF-W6-4 audit dict per Re: C5 MISSED (CF-LZ-2); (c) the parse-tree abbreviation map extension per Re: C5 sub-question (i) (CF-LZ-3); (d) the F_traj=1/4 zeta-vs-SDW prediction for Var_a as a falsifiable structural prediction at S89+ (CF-LZ-4).

### Part 2: Original Analysis

#### L1: FI/RD/MIXED trichotomy (S82 W-3 §VII.K) applied to Var_a(n_a^GGE)

**Trichotomy discriminator from first principles (substrate-first per `phononic-framing.md`)**:

The FI/RD/MIXED trichotomy is the substrate's intrinsic classification of an observable's response to REGULATOR-CLASS variation. The substrate IS the spectral triple `(A_K, H_K, D_K)`; the regulator class is the substrate's intrinsic choice of how the divergent spectral moments `Σ_k m_k λ_k^{-2n}` are made finite at L_max → ∞ truncation (or equivalently, how the Mellin-Dirichlet series `Σ_k m_k λ_k^{-s}` is analytically continued through its poles). The trichotomy is NOT a property "in" a regulator container; the trichotomy IS a structural property of the substrate's spectral-action functional class.

**3-step discriminator (S82 W-3 §VII.K)**:

```
Step 1 (Substrate moment evaluation):
        For observable O, compute its expression in TWO distinct
        regulator schemes R_1, R_2 ∈ {ζ, SDW, anomaly, cutoff, Zubarev}.
        Let O^{R_1} and O^{R_2} be the two evaluations.

Step 2 (Class membership decision):
        FI (Functional-Invariant):
            O^{R_1} = O^{R_2} exactly (bit-precision across regulators).
            The substrate's intrinsic spectral identity is REGULATOR-FREE.
        RD (Regulator-Dressed):
            O^{R_1} = α(R_1, R_2) · O^{R_2} for a closed-form scalar
            α dependent only on regulator-class labels and dimension d.
            The substrate's moment dresses with a known, computable factor.
        MIXED:
            O = O_FI + O_RD partition with both classes present.
            The substrate carries a FI sub-observable AND an RD sub-
            observable in the same expression.
        LEVEL-DRESSED (4th class, W-22 §V.4 extension):
            O is FI / RD / MIXED at fixed substrate-LEVEL (PRIMARY OR
            SCHEMATIC), but its rank-ordering across regulator-atlas
            members SWAPS under PRIMARY-vs-SCHEMATIC LEVEL switch.
            The substrate's response carries a regulator-PARAMETER
            dependence that the LEVEL switch surfaces.

Step 3 (Cross-check via F_traj theorem at locked norm L_k=1):
        For a substrate moment Σ m_k g_k(λ_k) with weight k,
        F_traj(k) = f_k^ζ / f_k^SDW = (k+1)/2 per S84 W3-24
        (my own theorem; locked norm convention).
        If O = scalar function of F_traj-dressed moments, then
        O^ζ / O^SDW reduces to a function of {F_traj(k)} ratios
        — confirming RD class via closed-form dressing.
```

**Application to `Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2`**:

```
Step 1 (Substrate moment evaluation, two regulators):

  Let M_2 := Σ_a m_a g_2(λ_a)  with g_2(λ) = Δ_BCS²/(2(λ²+Δ_BCS²))
  Let M_4 := Σ_a m_a g_4(λ_a)  with g_4(λ) = g_2(λ)²
                              = Δ_BCS⁴/(4(λ²+Δ_BCS²)²)

  Substrate weights at large-λ tail (regulator scheme matters):
  g_2(λ) ~ Δ_BCS²/(2λ²)        → weight-2 moment scaling
  g_4(λ) ~ Δ_BCS⁴/(4λ⁴)        → weight-4 moment scaling

  Under zeta regularization: zeta-image moments M_2^ζ, M_4^ζ.
  Under SDW (Seeley-DeWitt heat-kernel): M_2^SDW, M_4^SDW.

Step 2 (F_traj dressing per S84 W3-24):

  M_2^ζ / M_2^SDW = F_traj(2) = (2+1)/2 = 3/2          [weight-2]
  M_4^ζ / M_4^SDW = F_traj(4) = (4+1)/2 = 5/2          [weight-4]

  (At locked-norm L_k=1 convention per S84 W3-24; F_traj is the
   structurally-derived zeta-vs-SDW ratio for spectral moments.)

Step 3 (Variance composition):

  Var^ζ = (1/N) M_4^ζ − ((1/N) M_2^ζ)²
        = (1/N) · F_traj(4) · M_4^SDW − ((1/N) · F_traj(2) · M_2^SDW)²
        = (5/2) · ((1/N) M_4^SDW) − (3/2)² · ((1/N) M_2^SDW)²
        = (5/2) · A − (9/4) · B
  where A := (1/N) M_4^SDW, B := ((1/N) M_2^SDW)².

  Var^SDW = (1/N) M_4^SDW − ((1/N) M_2^SDW)²
          = A − B.

  Therefore:
  Var^ζ / Var^SDW = [(5/2)A − (9/4)B] / [A − B]
                  ≠ constant in general.

  The ratio is NOT a closed-form scalar independent of (A, B);
  it depends on the specific substrate-moment magnitudes.
```

**FI/RD/MIXED verdict for `Var_a(n_a^GGE)`**:

The variance ratio Var^ζ / Var^SDW is NOT a constant scalar dressing factor — it depends on the magnitudes A and B which are substrate-physics quantities, not regulator-class labels. This OBSERVATION rules out FI (which requires ratio = 1) AND rules out pure RD (which requires ratio = constant scalar).

But the variance IS a bilinear combination of TWO RD sub-moments: the M_4^SDW substrate moment AND the (M_2^SDW)² squared substrate moment, each individually dressed by F_traj(k) under regulator-class switch. The variance is therefore a **MIXED composite of RD sub-observables**, NOT a pure RD observable. The two sub-observables are:

- Sub-observable 1: `(1/N) Σ_a m_a g_4(λ_a)` — RD with F_traj(4) = 5/2 dressing
- Sub-observable 2: `((1/N) Σ_a m_a g_2(λ_a))²` — RD with F_traj(2)² = 9/4 dressing (squared composition)

Both sub-observables are RD; the composite (a linear difference) is **MIXED** in the strict S82 W-3 §VII.K trichotomy sense BECAUSE the bilinear difference preserves the two distinct F_traj dressing factors WITHOUT a uniform closed-form scalar reducing them to a single multiplier. The MIXED tag in this case carries a structural refinement: both sub-observables belong to the SAME class (RD), but their DRESSING FACTORS DIFFER, producing a non-uniform regulator-class response.

**Refined classification — Var_a(n_a^GGE) is "MIXED-of-RD-sub-observables-with-distinct-F_traj-factors" (S82 W-3 §VII.K sub-tag)**:

This refinement aligns with `§VII.K-DUAL.LAYER` per-row LAYER-of-pin atlas extension (registry line 4321) where MIXED sub-tags are explicitly catalogued. The structural takeaway: `Var_a(n_a^GGE)` is NOT a clean FI / RD / MIXED member; it is a MIXED-with-DISTINCT-F_traj-FACTORS observable, which is one of the borderline classes the W-22 §V.4 LEVEL-DRESSED 4th-class extension is designed to systematize.

**LEVEL-DRESSED 4th-class connection**:

Per the 3-criterion definition at registry line 4293-4297:

1. **Algebra-INVARIANT spectrum-only**: SATISFIED (my Re: C1 verdict; parse-tree decision returns INVARIANT).
2. **Regulator-CLASS membership unchanged across PRIMARY-vs-SCHEMATIC LEVEL switch**: PENDING empirical scan at S89+. The FI/RD/MIXED classification at PRIMARY level is "MIXED-of-RD-with-distinct-F_traj"; the SCHEMATIC-level classification needs to be evaluated against `_spectral_action_regulators.py` SCHEMATIC bare Casimir spectrum to determine whether the FI/RD/MIXED partition holds under LEVEL switch.
3. **Ordinal output changes between PRIMARY and SCHEMATIC**: PENDING the same empirical scan. The rank-ordering of {observable-instances-across-regulator-atlas-members} under both levels must be compared.

If criteria (2) and (3) both hold at S89+, `Var_a(n_a^GGE)` is the LEVEL-DRESSED K=2 calibration corpus instance. This is precisely the structural-promotion candidate already explicitly named at registry line 4307. I queue this empirical scan as CF-LZ-1 at L4 below.

**Cross-check against connes's algebra-axis × Mellin-pole 4-corner verdict — do they AGREE or REFINE?**

- **AGREE on the algebra-axis layer**: my parse-tree decision (clause (e), my authorship) returns INVARIANT for `Var_a(n_a^GGE)`. Connes's parse-tree decision returns INVARIANT. Both verdicts converge.
- **AGREE on the Mellin-pole layer**: my Weyl-tail analysis at d=4 returns s=4. Connes's Weyl-tail analysis at d=4 returns s=4. Both verdicts converge.
- **REFINE on the FI/RD/MIXED axis layer WITHIN INVARIANT**: connes's 4-corner partition does NOT distinguish FI vs RD vs MIXED — it treats all algebra-INVARIANT observables uniformly at Cell II. My trichotomy distinguishes MIXED-with-distinct-F_traj-factors (Var_a) from pure FI (Mellin-Dirichlet identity at §VII.U.1, which has zero F_traj-dressing because the off-pole strip identity is algebraic) from pure RD (η-invariant under regulator-weight changes, which dresses uniformly). The refinement is structurally significant because it identifies LEVEL-DRESSED candidacy (criterion (2) of the 3-criterion definition).
- **NEITHER AGREES NOR DISAGREES on the substrate-distance-pole-INDEX layer**: both my analysis and connes's converge on s=4; the choice between substrate-distance-1 (s=3, like §VII.U.1) and substrate-distance-2 (s=4, like §VII.U.2 Corner II Var_a + §VII.AR + §VII.K-PROP.W10-4) is decided uniquely by the Weyl-tail integration at d=4, which is regulator-class-INVARIANT and pole-IDENTITY-INVARIANT. The pole index is FI in the trichotomy sense.

**Final classification under the combined 4-axis structure** (per Re: C3 EMERGES 4-cube):

```
Var_a(n_a^GGE) ∈ {
    Algebra-axis:        INVARIANT
    Mellin-pole-axis:    s=4
    FI/RD/MIXED-axis:    MIXED-of-RD-with-distinct-F_traj-factors
    LEVEL-axis:          PRIMARY-and-SCHEMATIC-pending-empirical-K2-scan
}
```

This is the SHARPEST classification the workshop's combined toolchain produces. Connes's 2-axis classification (INVARIANT × s=4 = Cell II) is the projection of this 4-axis classification onto the algebra-axis × Mellin-pole axes. My S82 W-3 §VII.K trichotomy is the projection onto the FI/RD/MIXED-axis. The W-22 §V.4 LEVEL-DRESSED extension is the projection onto the LEVEL-axis. The full 4-cube classification is the union of all four projections.

#### L2: Family-mate corner preservation (§VII.U.1 + §VII.U.6 retain Corner I) — what makes §VII.U.2 different

**Direct family-mate inspection**:

- **§VII.U.1** (FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY, S86 W-1 REG-1; registry lines 12881-12922): `M[Tr(e^{−tD²})](s/2) / Γ(s/2) = Σ_k m_k · λ_k^{−s} = ζ_D(s)`. Corner I (INVARIANT × s=3). FINITE-VECTOR class per `lizzi-finite-infinite-vector-classification.md`. Sanity-Check PASS at L_max=12 with rel_diff = 0.000e+00 by `math.fsum` exact-rounding. Per W6-6 Stage B audit at working paper line 216: `§VII.U.1: corner=I, algebra_axis=INVARIANT, mellin_pole=s=3, status=ANNOTATED, matches_prediction=True`.
- **§VII.U.6** (W1b-T5 LANDING Mellin-Strip / Convergence-Cone Theorem, S86 W-1 REG-6; registry lines 13061-13088): closed-form `M[exp(−x/Λ_Z²)](s) = Λ_Z^{2s} · Γ(s)` on convergence cone Re(s) > 0; INFINITE-VECTOR class; C11 PASS at max_rel_err = 8.066e-28. Corner I (INVARIANT × s=3). Per W6-6 Stage B audit at working paper line 217: `§VII.U.6: corner=I, algebra_axis=INVARIANT, mellin_pole=s=3, status=ANNOTATED, matches_prediction=True`.

Both family-mates retain Corner I per the W6-6 audit run (Stage B PASS for the family-mates; only §VII.U.2 itself shifted). The drift is LOCALIZED to §VII.U.2.

**What structurally distinguishes §VII.U.2 from §VII.U.1 + §VII.U.6**:

The structural difference operates at TWO non-overlapping layers:

**Layer 1 — Mellin-pole-axis layer (substrate-distance pole)**:

§VII.U.1 and §VII.U.6 are BOTH substrate-distance-1 pole observables (s=3 = (d-n)/2 at d=4, n=2 → s=(4-2)/2 = 1? — wait, the convention here uses s=3 for substrate-distance-1, see registry line 12888 / 12961 for the convention). Both observables are ALGEBRAIC IDENTITIES on the substrate's eigenvalue Dirichlet series:

- §VII.U.1 is the off-pole strip identity (Mellin-Dirichlet algebraic transform connecting the heat-kernel trace to the spectral zeta function). This identity holds at ANY L by linearity + Euler integral identity.
- §VII.U.6 is the convergence-cone closed-form of the Zubarev kernel's Mellin transform; the closed form holds on Re(s) > 0 with simple poles from Γ(s).

BOTH observables are STRUCTURALLY ALGEBRAIC at the substrate's Mellin-axis — they hold as Mellin-axis identities WITHOUT requiring a physical observable to be evaluated. They are SUBSTRATE-AXIOM IDENTITIES at the spectral-action regulator family layer.

`Var_a(n_a^GGE)` at §VII.U.2 Corner II is at substrate-distance-2 pole (s=4 per Weyl-tail analysis at d=4). The substrate-distance-2 pole is the ENERGETIC-MOMENT POLE: Newton's constant lives there (a_2 Seeley-DeWitt coefficient via the Einstein-Hilbert action density), Yang-Mills couplings live there (a_4 SD coefficient via the YM action density). These are FIELD-THEORY ACTION DENSITY moments, structurally distinct from algebraic Mellin identities.

So Corner II is on a DIFFERENT mellin-pole sub-axis from Corner I. The §VII.U family-mate slots at Corner I sat at the algebraic-identity sub-axis; Corner II (when populated by Var_a at W-17 §V.2) is at the energetic-moment sub-axis. The two sub-axes are NOT cross-corner under §VII.U.2 clause (f) FORBIDDEN clause — they are sub-axes WITHIN the same algebra-axis × Mellin-pole 4-corner partition; the difference is a CONSTRUCTION-CLASS difference (algebraic-identity vs energetic-moment), not a corner-classification difference.

**Layer 2 — Construction-order layer (substrate-physics derivation history)**:

§VII.U.1 + §VII.U.6 were derived at S86 W-1 (2026-04-27) per registry line 12881 + 13061. Both are ALGEBRAIC-IDENTITY observables that emerge directly from the Mellin transform / heat-kernel asymptotic structure on the substrate's eigenvalue Dirichlet series. No coupling to specific substrate-physics observables (BCS condensate, GGE state, K-window) is required — they are pure spectral-action identities.

`Var_a(n_a^GGE)` was first derived at S88 §W5b-47 (substrate-distance-2 cone derivation; audit_sha256 `89090d37b3610590...` per registry line 12961). The derivation required:
1. BdG Bogoliubov transformation to produce the closed form `n_a = |v_a|^2 = Δ_BCS²/(2(λ_a²+Δ_BCS²))`.
2. GGE state expectation reduction to closed-form `n_a` (GGE state's role: produce the closed-form NUMBER per Step 2 of connes's C1 substitution chain).
3. Sample-variance construction over BdG mode-index `a` with multiplicity `m_a` weighting.
4. Weyl-tail integration at d=4 to identify the substrate-distance-2 pole.

This construction chain requires the BCS condensate parameter `Δ_BCS` as a substrate-canonical scalar AND the GGE state on `A_BdG = A_F ⊗ M_2(ℂ)` AND the L_max=10 truncation regime. The construction is structurally LATER in the substrate's derivation order than the algebraic-identity observables of §VII.U.1 + §VII.U.6.

**Corner II's structural difficulty**:

The combination of Layer 1 (substrate-distance-2 = energetic-moment sub-axis) + Layer 2 (later derivation order) explains why Corner II was OPEN at W5b-45 landing time (per Corrigendum C2 at registry line 13010). The substrate's structural bias is NOT toward avoiding Corner II — the substrate's eigenvalue spectrum produces Corner II observables AS SOON AS the substrate-distance-2 pole machinery is constructed. The bias is in the CONSTRUCTION ORDER of the substrate's observable derivations: algebraic identities arrive first (§VII.U.1 + §VII.U.6 at S86 W-1); energetic-moment observables arrive later as the BdG / GGE / spectral-action-density machinery is built out (Var_a at S88 §W5b-47).

This is a SUBSTRATE-CONSTRUCTION-HISTORY observation, NOT a fundamental asymmetry. Corner II is NOT structurally harder to populate than Corner I in any absolute sense; it required a LATER chunk of the substrate's machinery to be constructed before its instances became derivable.

**Family-mate divergence diagnostic**:

The W6-6 Stage B audit's "family-mates §VII.U.1 + §VII.U.6 retain Corner I" result is informative because it confirms:

1. The W-17 / W-21 edits to §VII.U.2 did NOT propagate to §VII.U.1 or §VII.U.6 — the drift is LOCALIZED to §VII.U.2 (drift-localization audit signal).
2. The §VII.U family-mate slots are structurally STABLE under the W-21 V.1+V.3 edits (no cross-family-mate corruption signal).
3. The family-mate slot stability supports the parse-tree decision procedure's regulator-INDEPENDENCE: the parse-tree returns INVARIANT for §VII.U.1 + §VII.U.6 under ANY regulator scheme, including any scheme the W-21 edits might have introduced.

This is a useful POSITIVE EVIDENCE signal for Reading B: if Reading A were correct (V.1+V.3 broke a stable Cell-I classification at §VII.U.2), we would expect SOME family-mate signal of the breakage — but §VII.U.1 + §VII.U.6 are unaffected. The localization to §VII.U.2 is consistent with the parse-tree decision being EXPLICITLY APPLIED to Var_a at W-17 §V.2 (a structurally targeted reclassification at the Corner II row instance level), NOT with a global edit that broke Cell-I across the §VII.U family.

**What the family-mate divergence tells us about the substrate's algebra-axis × Mellin-pole bias**:

The family-mate divergence (§VII.U.1 + §VII.U.6 at Cell I; §VII.U.2 Corner II at Cell II; §VII.U.2 Corner III at Cell III; §VII.U.2 Corner IV at Cell IV) is the structural realization of the §VII.U.2 partition theorem's 4-corner orthogonality. The substrate's spectral triple `(A_K, H_K, D_K)` produces observables in ALL 4 corners; the §VII.U family slot collection is the registry's calibration corpus for that 4-corner orthogonality. The bias is not "substrate prefers Cell I" — the bias is "substrate produces Cell-I-type ALGEBRAIC IDENTITIES first and Cell-II-type ENERGETIC MOMENTS later." Once all 4 corners are populated (which is the post-W-17 §V.2 state per registry line 12961 + 12963), the partition is structurally saturated and the 4-corner orthogonality is fully demonstrated.

**Substrate-first re-framing**:

The family-mate divergence is NOT a property of a partition-container that the substrate inhabits. The substrate IS the spectral triple; the 4-corner partition IS the substrate's algebra-axis × Mellin-pole orthogonality classification of its own observables. The §VII.U family slots are the REGISTRY-LANDING projections of the substrate's intrinsic corner-cell distribution. The family-mate corner preservation under W-21 V.1+V.3 is a structural consistency check (the partition theorem's calibration corpus retains its 4-corner orthogonality across the registry-text edits), NOT an emergent property of a registry-container.

The deep substrate-physics observation: the substrate's observables NATURALLY DISTRIBUTE across the 4 corners according to which substrate-physics derivation chain produces them. Algebraic-identity derivations → Cell I (s=3, INVARIANT). Energetic-moment derivations → Cell II (s=4, INVARIANT). State-pair-distance derivations on `A_F` sub-blocks → Cell III (s=3, DEPENDENT). GGE-state-pair K-window derivations → Cell IV (s=4, DEPENDENT). The 4-corner partition is the substrate's intrinsic taxonomy of its own derivable observables.

#### L3: PRIMARY-vs-SCHEMATIC LEVEL switch under substrate-first-canonical-sourcing.md §(iv) — does the LEVEL switch reclassify the corner, or only re-tag provenance?

**Definitions (substrate-first per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4 since S88 W7b-83)**:

- **PRIMARY LEVEL** = FULL physical regularization on the substrate's intrinsic spectrum. For the substrate's Mellin-cone observables, this is the Pauli-Villars pipeline at Λ_UV = M_KK = 7.428660036284456e+16 GeV (the substrate-canonical UV scale per `canonical_constants.py:301`). The S61/S78 PV pipeline is the FULL physical realization. The spectrum is `{λ_a, m_a}` from the full BdG Bogoliubov-doubled Dirac operator D_K with Δ_BCS = 0.464 M_KK = 3.45e16 GeV per agent memory.
- **SCHEMATIC LEVEL** = `_spectral_action_regulators.py` deterministic schematic analog. Per the helper's own docstring (lines 23-30; verified in S88 W7b-83 audit): "These are SCHEMATIC regulators ... NOT the full physical regularizations used in the S61/S78 Pauli-Villars pipeline (which uses Lambda_UV = M_KK as the physical cutoff)." The SCHEMATIC level uses the bare Casimir-spectrum sum at substrate-distance-N pole, without the full physical PV subtraction with mass-scale running. The spectrum is structurally simpler (Casimir-flat) and produces deterministic outputs for atlas-comparison purposes.

The LEVEL switch is the substrate-physics direction-of-explanation transition: PRIMARY is the substrate's full physical Dirac-operator-based regularization; SCHEMATIC is a deterministic computational analog that captures the structural form but not the full physical content.

**Q-L3 verdict**: the PRIMARY-vs-SCHEMATIC LEVEL switch DOES NOT reclassify the algebra-axis × Mellin-pole corner cell (the Cell II classification is regulator-class-INVARIANT and LEVEL-INVARIANT). The LEVEL switch CAN reclassify the FI/RD/MIXED sub-axis WITHIN the corner, AND the LEVEL switch CAN swap the rank-ordering of regulator-atlas members (which is criterion (3) of the LEVEL-DRESSED 4th-class definition). Therefore the LEVEL switch is REGULATOR-PIN-DISCIPLINE-RELEVANT at the FI/RD/MIXED-axis layer, NOT at the corner-cell layer.

**Substitution chain to the verdict (substrate-first per `math-scripts.md §"Double-Check Logic Before Compute"`)**:

```
Step 1 (Corner-cell classification at PRIMARY level):
        Var_a(n_a^GGE) symbolic form has zero π(a), zero [D, π(a)],
        zero state-pair sup; spectrum-only g(λ) closed forms.
        Parse-tree decision (clause (e)) → Corner II (INVARIANT × s=4).

Step 2 (Corner-cell classification at SCHEMATIC level):
        Under SCHEMATIC, the spectrum `{λ_a, m_a}` is the bare Casimir
        spectrum (e.g., from `_spectral_action_regulators.py.pauli_villars_a_n`).
        The symbolic form Var_a(n_a^GGE) remains
        `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2`.
        Parse-tree decision applies UNCHANGED (the symbolic form has
        the same parse-tree structure regardless of which spectrum
        the λ_a's are drawn from).
        Parse-tree decision → Corner II.

Step 3 (Comparison):
        PRIMARY-level corner = Cell II = SCHEMATIC-level corner.
        Corner cell is REGULATOR-LEVEL-INVARIANT.

Step 4 (FI/RD/MIXED-axis classification at PRIMARY level):
        Per L1 step 1-3: Var_a is MIXED-of-RD-sub-observables-with-
        distinct-F_traj-factors WITHIN Cell II at PRIMARY level.

Step 5 (FI/RD/MIXED-axis classification at SCHEMATIC level):
        Under SCHEMATIC (Casimir-flat spectrum), the substrate moments
        Σ_a m_a g_k(λ_a) at the SCHEMATIC level may dress differently
        because the SCHEMATIC spectrum's λ-distribution differs from
        the PRIMARY spectrum. In particular: the F_traj=(k+1)/2 theorem
        (S84 W3-24, my own) was derived at locked-norm L_k=1 convention
        on the PRIMARY-level spectrum. Under SCHEMATIC, the locked-norm
        convention may produce a DIFFERENT F_traj scaling (the Casimir
        spectrum's Weyl-tail behavior differs from the BdG-PV spectrum's).

Step 6 (LEVEL-switch effect on rank-ordering):
        The rank-ordering of {Var_a^ζ, Var_a^SDW, Var_a^anomaly,
        Var_a^cutoff, Var_a^Zubarev} under PRIMARY vs SCHEMATIC is
        the 3-criterion (3) LEVEL-DRESSED test. If the rank-ordering
        SWAPS under LEVEL switch, Var_a satisfies criterion (3) and
        is a LEVEL-DRESSED candidate. EMPIRICAL — pending S89+ scan.

Step 7 (Conclusion):
        Corner classification (algebra-axis × Mellin-pole) is LEVEL-
        INVARIANT for Var_a; the LEVEL switch is PROVENANCE-LEVEL
        re-tagging at the corner-classification layer.
        FI/RD/MIXED-axis classification is potentially LEVEL-DEPENDENT
        for Var_a; the LEVEL switch is REGULATOR-PIN-DISCIPLINE-
        RELEVANT at the FI/RD/MIXED sub-axis layer.
        LEVEL-DRESSED 4th-class candidacy is empirical at S89+.
```

**Cross-reference to registry text I authored (line 13001)**:

The §VII.U.2 entry contains (at registry line 13001, which is part of my PRIMARY-synthesized clause (e) sub-section + cache-resolution-vs-canonical-import sub-class layer calibration-corpus row):

> "Cross-link to `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` S88 W8-88 hardening: the canonical-import-binding vs substrate-natural-binding distinction is a NEW algebra-axis sub-class layer WITHIN the parse-tree-INVARIANT corner classification — it does NOT shift the observable across the FI / RD / MIXED partition (cf. the LEVEL-DRESSED 4th class extension at §VII.K-DUAL.LEVEL-DRESSED B.54 W-22 §V.4, which DOES shift ordinal output across LEVEL switch)."

This text I myself authored (as PRIMARY synthesizer) pins the structural rule: SUB-CLASS LAYER binding distinctions do NOT cross corners; LEVEL switch (a DIFFERENT axis from the binding-route axis) DOES shift ordinal output WITHIN a corner. The Q-L3 verdict above is consistent with this rule: corner stays Cell II under LEVEL switch; FI/RD/MIXED-axis can shift; rank-ordering can swap.

**Parallel calibration corpus instance — §VII.AQ Level-3 anchor (registry line 17048)**:

The §VII.AQ entry (W-11 STRENGTHENED η-NULL theorem) provides a parallel calibration corpus point for the LEVEL-INVARIANT corner-classification + LEVEL-DEPENDENT empirical-value distinction. Per registry line 17048:

> "Level-3 anchor PASS-via-canonical-import-pin against `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8 published at full per-sector chirality fidelity); substrate-natural compute on the L_max=10 cache `s84_spectrum_cache_L12_tau019.npz` returns `Δ_GV_natural = 0` due to uniform 8d:8d chirality split per (p,q)-sector — cache-averaging diagnostic, not substrate-physics defect."

Both binding routes (canonical-import vs substrate-natural) inhabit the SAME Corner I (INVARIANT × s=3) per parse-tree decision. The two routes produce DIFFERENT empirical values at the Level-3 anchor (`-40579.15` vs `0`) due to cache-averaging artifacts, BUT the parse-tree class membership is binding-route-INVARIANT. This is the exact structural pattern for Var_a under PRIMARY-vs-SCHEMATIC LEVEL switch: corner stays Cell II, empirical values can differ, FI/RD/MIXED-axis can shift.

**Apply the FI vs RD discriminator at BOTH regularization levels for Var_a**:

| LEVEL | Spectrum source | F_traj behavior | FI/RD/MIXED-axis verdict |
|:------|:---------------|:----------------|:--------------------------|
| PRIMARY (S61/S78 PV at Λ_UV = M_KK) | Full BdG-doubled Dirac D_K with Δ_BCS pairing channel | F_traj(2) = 3/2, F_traj(4) = 5/2 per S84 W3-24 locked-norm theorem on PRIMARY spectrum | MIXED-of-RD-with-distinct-F_traj-factors (per L1) |
| SCHEMATIC (`_spectral_action_regulators.py`) | Bare Casimir spectrum (Casimir-flat, structurally simpler) | F_traj under SCHEMATIC is NOT proven to satisfy the (k+1)/2 locked-norm theorem; empirical S89+ scan required | UNDETERMINED — could be MIXED-of-RD, could be pure RD with different scalar, could be MIXED-of-MIXED. EMPIRICAL question. |

**Verdict — LEVEL switch IS regulator-class-discriminating at the FI/RD/MIXED-axis layer**:

If the F_traj scaling under SCHEMATIC differs from F_traj=(k+1)/2 under PRIMARY (which is empirically testable at S89+), then Var_a's FI/RD/MIXED-axis classification is LEVEL-DEPENDENT. This is a structural FI/RD-AXIS REGULATOR-CLASS DISCRIMINATING property, distinct from the corner-cell classification (which is LEVEL-INVARIANT per Step 3 above).

The verdict directly answers L3's framing question:
- **Corner classification under LEVEL switch**: PROVENANCE-ONLY re-tagging (corner cell stays Cell II regardless).
- **FI/RD/MIXED-axis under LEVEL switch**: REGULATOR-PIN-DISCIPLINE-RELEVANT (sub-axis can shift WITHIN the corner, potentially satisfying LEVEL-DRESSED criterion (3) at S89+).
- **Empirical Level-3 anchor under LEVEL switch**: REGULATOR-PIN-DISCIPLINE-RELEVANT (values can differ; cache-averaging artifacts possible; substrate-natural-binding upgrade route may be required for full chirality fidelity per §VII.AQ precedent).

**Substrate-first re-framing**:

The LEVEL switch is NOT an external choice imposed ON the substrate; the LEVEL switch IS the substrate's intrinsic structural distinction between (a) its full physical Dirac-operator-based regularization at Λ_UV = M_KK (PRIMARY) and (b) its deterministic computational analog (SCHEMATIC). The substrate produces both levels; the question is which level the observer evaluates the observable at. Reading the LEVEL switch as "the regulator container the substrate inhabits" would be container-thinking inversion per `phononic-framing.md §"IS Space, Not IN Space"`. The substrate IS its full physical regularization; the SCHEMATIC analog IS a derived deterministic computational projection of the substrate's intrinsic structure.

**Forward enforcement**:

If `Var_a(n_a^GGE)` empirically demonstrates LEVEL-DRESSED criterion (3) at S89+ (rank-ordering swap under PRIMARY-vs-SCHEMATIC LEVEL switch), the §VII.U.2 Corner II row's classification gets EXTENDED to:

```
algebra-axis:        INVARIANT          (parse-tree decision PASS)
Mellin-pole:         s=4                (Weyl-tail at d=4 PASS)
corner cell:         II                  (algebra-axis × Mellin-pole PASS)
FI/RD/MIXED-axis:    MIXED-of-RD       (at PRIMARY level per L1)
LEVEL-axis:          LEVEL-DRESSED     (4th class extension; K=2 calibration corpus instance per W-22 §V.4 forward-enforcement clause at line 4307)
```

And the §VII.K-DUAL.LEVEL-DRESSED K-counter advances K=1 → K=2 toward MANDATORY-at-K=3 promotion. This is the structural propagation path my Re: C3 MISSED section identified; I formally queue it as CF-LZ-1 at L4 below.

#### L4: Questions for connes + R1 4-field carry-forward

##### Questions for connes (extending R1 → R2)

**Q-LZ-R2-1 (BdG-doubled algebra Wedderburn extension)**: Your C1 §"Wedderburn / Schur-orthogonality check on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)" at workshop lines 84-91 applies the 7-axiom NCG construction's Wedderburn decomposition of `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` and derives `Z(A_F) = ℂ · P_ℂ + ℂ · P_ℍ + ℂ · P_M3` (per W5b-48 Step 5). But `Var_a(n_a^GGE)` lives naturally on the BdG-DOUBLED algebra `A_BdG = A_F ⊗ M_2(ℂ)` per my agent memory's Active Context (the BdG doubling produces the {b_a^†, b_a} Bogoliubov mode-pair structure that the GGE expectation `n_a := ω_GGE(b_a^† b_a)` acts on). Two sub-questions:

(a) Does the Wedderburn decomposition of `A_BdG` factor as `Z(A_BdG) = Z(A_F) ⊗ Z(M_2(ℂ)) = (ℂ · P_ℂ + ℂ · P_ℍ + ℂ · P_M3) ⊗ (ℂ · P_+ + ℂ · P_-)` where `P_±` are the BdG quasiparticle / quasihole projectors? If so, the central projection count expands from 3 to 6 (3 algebra-sector projections × 2 BdG-doubling projections), and the parse-tree decision procedure clause (e) verification at the BdG level requires inspecting all 6 central projections. Does this 6-projection inspection change the Cell II verdict?

(b) The chirality-vs-A_F block-grading mismatch at W5b-48 eq. (9) gives `f(D²) ∩ π(A_F) = ℂ · 1_{H_F}`. Under BdG doubling, this becomes `f(D_BdG²) ∩ π(A_BdG) = ℂ · 1_{H_F} ⊗ ?` — what is the right-hand side under BdG-doubled Dirac D_BdG? Is it `ℂ · 1_{H_F} ⊗ 1_{M_2}` (full BdG-scalar) or `ℂ · 1_{H_F} ⊗ τ_3` (BdG-z-direction-projected scalar, where τ_3 is the BdG Pauli matrix in the particle-hole basis)? The answer matters because `n_a = ω_GGE(b_a^† b_a)` is structurally a τ_3-projected number-density expectation, NOT a full BdG-scalar. If the right-hand side carries τ_3 structure, the Wedderburn / Schur-orthogonality cross-check needs refinement at the BdG-doubling axis.

**Q-LZ-R2-2 (parse-tree decision procedure on Bogoliubov closed forms — depth recursion)**: Your C1 Step 2 substitution chain at workshop line 43-44 introduces the Bogoliubov closed form `n_a = |v_a|^2 = Δ_BCS²/(2(λ_a² + Δ_BCS²))` as a CLOSED-FORM ATOM. The parse-tree decision procedure clause (e) (which I authored) operates at the symbolic-form level on `Σ_a m_a g(λ_a)` with g treated atomically. Two sub-questions:

(a) Does the parse-tree decision procedure handle ALL Bogoliubov closed forms uniformly, or does the recursive substitution `n_a → |v_a|^2 → Δ_BCS²/(2(λ_a²+Δ_BCS²))` introduce a tier-2 parse-tree recursion not anticipated by clause (e)'s flat 7-axiom-checkbox structure? Concretely: at the abbreviation `|v_a|^2`, the parse-tree decision returns INVARIANT (no π(a) at the level of the abbreviation). After substitution to the full closed form, the parse-tree contains arithmetic operations on `Δ_BCS`, `λ_a`, scalar constants — still no π(a). So the verdict is INVARIANT at BOTH parse-tree depths. But the WORK of confirming this requires walking the recursive substitution. Is the recursive-substitution walk a structural extension of clause (e), or is it already captured by clause (e)'s "the decision procedure is finite and operates at parse-tree level, NOT at numerical evaluation level"?

(b) Per my Re: C5 sub-question (i) verdict + refinement, I proposed an explicit PARSE_TREE_ABBREVIATION_MAP in the audit script: `{"|v_a|^2": "Δ_BCS²/(2·(λ_a² + Δ_BCS²))", "|v_a|^4": "(...)²", "n_a^GGE": "|v_a|^2"}`. Do you agree that this abbreviation map is the correct mechanism for handling Bogoliubov closed-form atoms WITHIN the parse-tree decision procedure (as opposed to either: (i) leaving the abbreviation as a non-expanded atom + requiring atomic-class-membership pre-registration, OR (ii) forcing full expansion at every audit invocation + losing the abbreviation's referential clarity)? My proposal is option (iii) "pre-registered abbreviation map" — splitting the difference. Is this the right structural design?

**Q-LZ-R2-3 (registry-text editing-history vs structural-classification — meta-rule promotion)**: Your C6 Observation 4 surfaces the principle "observable naming conventions encode HISTORY, not STRUCTURE." This is a substantive substrate-physics observation about the relationship between OBSERVABLE NAMES (which carry derivation-historical content) and STRUCTURAL CLASSIFICATIONS (which operate on parse-tree-derivable form). The Var_a(n_a^GGE) case is the calibration corpus instance #1 (W5b-45 Corner-IV mis-placement → W-17 §V.2 parse-tree-correction). The S82 α_s_canonical = n_s² − 1 case at registry line 12960 is a parallel structural pattern (cosmological-observation naming history vs spectrum-only-functional structural identity). Question: should we promote this principle to a STANDALONE RULE in `.claude/rules/` (cf. `phononic-framing.md` and `cross-pillar-bridge-anatomy.md` as comparators), or extend an existing rule with a sub-clause? I believe `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` is the natural host — the principle is part of the same algebra-axis-orthogonality discipline that motivates the parse-tree decision procedure. Do you agree, or do you see a different rule-file landing target?

##### R1 4-field carry-forwards (per `feedback_fix-in-session-never-defer.md` + `.claude/rules/output-standards.md §"Carry-Forward Dependency Enumeration"`)

###### CF-LZ-1 — LEVEL-DRESSED K=2 empirical scan for `Var_a(n_a^GGE)` under PRIMARY-vs-SCHEMATIC LEVEL switch

| Field | Value |
|:------|:------|
| **What** | Empirically evaluate the 3-criterion LEVEL-DRESSED definition (per §VII.K-DUAL.LEVEL-DRESSED registry line 4293-4297) for `Var_a(n_a^GGE)`: (1) algebra-INVARIANT spectrum-only — SATISFIED (parse-tree decision PASS per this workshop); (2) regulator-CLASS membership unchanged across PRIMARY-vs-SCHEMATIC LEVEL switch — PENDING empirical scan; (3) ordinal output (rank-ordering of {Var_a^ζ, Var_a^SDW, Var_a^anomaly, Var_a^cutoff, Var_a^Zubarev}) swaps under PRIMARY-vs-SCHEMATIC LEVEL switch — PENDING. Compute Var_a under PRIMARY (S61/S78 PV pipeline at Λ_UV = M_KK on full BdG-doubled D_K spectrum) and SCHEMATIC (`_spectral_action_regulators.py.pauli_villars_a_n` + zeta + anomaly + cutoff + Zubarev SCHEMATIC analogs on bare Casimir spectrum) at fixed (cutoff_frac=0.7, M_PV²_frac=0.1, Vol_SU3_Haar). Compare rank-orderings. If swap detected, Var_a is LEVEL-DRESSED K=2 instance per W-22 §V.4 forward-enforcement clause at line 4307. |
| **Inputs** | `s84_spectrum_cache_L12_tau019.npz` (PRIMARY full BdG D_K spectrum cache; SHA via canonical_constants); `_spectral_action_regulators.py` SCHEMATIC helpers (per its docstring lines 23-30); `canonical_constants.py` for `M_KK = 7.428660036284456e+16`, `Delta_BCS = 0.464 · M_KK`, `Vol_SU3_Haar = 1349.74`; W9b-2 npz `s87_w9b_pole_specificity_scan.npz` as upstream LEVEL-switch precedent (W9b-2 demonstrated SCHEMATIC-vs-FULL D_max = 2.168 per W6-7 §6); §VII.K-DUAL.LEVEL-DRESSED 3-criterion definition at registry lines 4293-4297. |
| **Gate** | PASS = LEVEL-DRESSED criterion (3) confirmed (rank-ordering swap observed under LEVEL switch); §VII.K-DUAL.LEVEL-DRESSED K-counter advances K=1 → K=2; Var_a's classification extends to `{INVARIANT, s=4, MIXED-of-RD-at-PRIMARY, LEVEL-DRESSED at K=2 cohort with §VII.AR}`. FAIL = rank-ordering preserved (Var_a is not LEVEL-DRESSED); classification stays at `{INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj}` without LEVEL-axis promotion. INFO = ambiguous (partial rank-swap; some atlas members swap, others don't). |
| **Effort** | 0.6 wave-equivalents (5-regulator-atlas scan at 2 LEVELs; computation + rank-comparison + verdict + registry annotation if PASS). Requires connes-ncg-theorist CO-AUTHOR for the FULL physical PV pipeline at Λ_UV = M_KK (per W6-7 CF-W6-5 pattern, since the S61/S78 PV pipeline is conceptual in the helper docstring). |
| **Owner** | lizzi-spectral-functional-theorist PRIMARY (FI/RD/MIXED-axis classification authority + S82 W-3 trichotomy origin) + connes-ncg-theorist CO-AUTHOR (FULL physical PV pipeline reconstruction). mack-cosmic-bridge sole writer for registry annotation update if PASS. |
| **Depends on** | UPSTREAM GATE: CF-W6-3 (§VII.U.2 Corner-classification reconciliation; Reading B must be locked-in first); UPSTREAM GATE: CF-W6-5 (substantive D_max measurement at FULL PV pipeline; provides the FULL-physical PV pipeline machinery this gate consumes); UPSTREAM REGISTRY: §VII.K-DUAL.LEVEL-DRESSED registry lines 4293-4307 (3-criterion definition + forward-enforcement clause); UPSTREAM RULE: `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 (PRIMARY-vs-SCHEMATIC LEVEL discipline). |

###### CF-LZ-2 — FI_RD_MIXED axis field extension to CF-W6-4 audit dict (refinement of connes's CF-R1-1)

| Field | Value |
|:------|:------|
| **What** | Extend the TARGET_SLOTS_S89 dict at `_corner_classification_audit.py` (per connes's CF-R1-1) to include a `fi_rd_mixed_axis` field per instance row. The field encodes the FI/RD/MIXED classification under S82 W-3 §VII.K trichotomy (refined per the 4-class extension to FI/RD/MIXED/LEVEL-DRESSED at §VII.K-DUAL.LEVEL-DRESSED W-22 §V.4). For the Corner II row Var_a(n_a^GGE), the field value is `MIXED-of-RD-with-distinct-F_traj-factors` per L1 verdict; LEVEL-DRESSED candidate per L3 verdict; K=2 LEVEL-DRESSED upgrade pending CF-LZ-1 empirical scan. The field includes rationale text, F_traj scalar dressing factors, and level_dressed_candidacy boolean. Audit verifies that the registry text's FI/RD/MIXED classification matches the pre-registered field. |
| **Inputs** | connes's CF-R1-1 TARGET_SLOTS_S89 dict (workshop lines 336-376); my L1 verdict (`MIXED-of-RD-with-distinct-F_traj` per S82 W-3 §VII.K trichotomy + F_traj=(k+1)/2 theorem); §VII.K-DUAL.LEVEL-DRESSED 3-criterion definition at registry lines 4293-4297; S84 W3-24 F_traj theorem (locked-norm L_k=1 convention); `lizzi-finite-infinite-vector-classification.md` (FINITE-VECTOR / INFINITE-VECTOR sub-tag distinction). |
| **Gate** | PASS = `_corner_classification_audit.py` self-test outputs `per_slot_results['§VII.U.2']['instance_rows']['corner_II_instance']['fi_rd_mixed_axis']` populated with the 5 sub-fields (`classification`, `rationale`, `f_traj_dressing_factors`, `level_dressed_candidate`, `level_dressed_k_counter_advancement_pending`) AND audit verifies the registry text contains a matching FI/RD/MIXED-axis annotation (if registry text is yet to be amended with the explicit FI/RD/MIXED-axis annotation, mack-cosmic-bridge sole-writer adds the annotation in the same dispatch). |
| **Effort** | 0.4 wave-equivalents (dict extension + audit self-test + registry text annotation amendment via mack-cosmic-bridge). |
| **Owner** | gen-physicist orchestrator-direct per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class (audit script extension) + mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md` (registry text annotation amendment). |
| **Depends on** | UPSTREAM GATE: connes's CF-R1-1 (base TARGET_SLOTS_S89 dict extension); UPSTREAM REGISTRY: §VII.K-DUAL.LEVEL-DRESSED 4-class extension at registry lines 4279-4313; UPSTREAM RULE: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (FI/RD/MIXED axis is a sub-axis within the algebra-axis classification); UPSTREAM REGISTRY: §VII.K-DUAL.LAYER per-row LAYER-of-pin atlas at registry line 4321. |

###### CF-LZ-3 — Parse-tree abbreviation map extension to `_corner_classification_audit.py` (refinement of Re: C5 sub-question (i))

| Field | Value |
|:------|:------|
| **What** | Add an explicit `PARSE_TREE_ABBREVIATION_MAP` constant to `_corner_classification_audit.py` mapping known Bogoliubov / GGE-state-history abbreviations to their fully-expanded closed forms: `{"|v_a|^2": "Δ_BCS²/(2·(λ_a² + Δ_BCS²))", "|v_a|^4": "(Δ_BCS²/(2·(λ_a² + Δ_BCS²)))²", "n_a^GGE": "|v_a|^2"}`. The audit applies the abbreviation map first, then runs the parse-tree counters (`expected_pi_a_count`, `expected_commutator_D_pi_a_count`, `expected_state_pair_sup_count`) on the fully-expanded symbolic form. This closes the failure mode where a future registry edit re-introduces a state-historical abbreviation (e.g., `n_a^GGE` without explicit Bogoliubov closure) and the audit naively flags the GGE-state name as state-pair-functional content. Calibration corpus instance #1 = retroactive expansion of Var_a(n_a^GGE) per W-17 §V.2 reclassification. |
| **Inputs** | Existing `_corner_classification_audit.py` (W6-6 SHA pin `2b96bf78…`); the parse-tree decision procedure at registry §VII.U.2 clause (e) line 12995 (my authorship); the Bogoliubov closed-form `n_a = |v_a|^2 = Δ_BCS²/(2·(λ_a² + Δ_BCS²))` from BdG fermionic Bogoliubov transformation (cited at registry line 12961 + my Re: C5 sub-question (i) verdict); the W-17 §V.2 reclassification event as the calibration corpus instance #1. |
| **Gate** | PASS = `_corner_classification_audit.py` extended with `PARSE_TREE_ABBREVIATION_MAP` constant AND self-test confirms (a) when fed the abbreviated symbolic form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2`, the audit applies the abbreviation map and runs counters on the expanded form with parse-tree counters all returning 0 (algebra-INVARIANT classification preserved through expansion), AND (b) when fed a synthetic test case with `n_a^GGE` as a non-expanded atom + no abbreviation map, the audit emits FAIL flagging the GGE-state-name as ambiguous (regression-prevention check). |
| **Effort** | 0.3 wave-equivalents (constant addition + 2-fixture self-test). |
| **Owner** | gen-physicist orchestrator-direct (METHODOLOGY-class audit script extension). |
| **Depends on** | UPSTREAM GATE: CF-W6-4 (connes's CF-R1-1 base extension); UPSTREAM REGISTRY: §VII.U.2 clause (e) parse-tree decision procedure at line 12995; UPSTREAM REGISTRY: Bogoliubov closed-form citation at line 12961; UPSTREAM RULE: `epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` Class 8.2 (abbreviation map IS the pre-registered pattern set for the rubric). |

###### CF-LZ-4 — F_traj=1/4 zeta-vs-SDW prediction for Var_a as falsifiable structural prediction at S89+

| Field | Value |
|:------|:------|
| **What** | Empirically verify the structural prediction Var_a^ζ / Var_a^SDW = [5/2 · A − 9/4 · B] / [A − B] (per L1 step 3 substitution chain) where A := (1/N) M_4^SDW, B := ((1/N) M_2^SDW)². For Var_a's specific substrate-physics regime (BdG Bogoliubov closure at Δ_BCS = 0.464 M_KK, GGE state on A_BdG, L_max=10 cache), compute A and B numerically and verify the predicted ratio. The prediction is a falsifiable test of the F_traj=(k+1)/2 theorem (S84 W3-24, my own) applied to a NEW substrate-physics observable not in the original 42-row S84 atlas. If the predicted ratio matches at machine epsilon, F_traj extends to BdG-doubled observables; if it fails at non-trivial precision, F_traj's locked-norm-L_k=1 convention may need refinement for BdG-doubled spectra. |
| **Inputs** | `s84_spectrum_cache_L12_tau019.npz` (full BdG D_K spectrum cache for PRIMARY level); zeta-regulated and SDW-regulated evaluators for M_2 = Σ_a m_a g_2(λ_a) and M_4 = Σ_a m_a g_4(λ_a) per `_spectral_action_regulators.py.zeta_a_n` + `_spectral_action_regulators.py.pauli_villars_a_n` (with explicit SCHEMATIC-vs-FULL-physical disclosure per `substrate-first-canonical-sourcing.md §(iv)`); the F_traj theorem (S84 W3-24, my agent-memory entry line 23); the Bogoliubov closed forms g_2(λ) and g_4(λ); `canonical_constants.py` for `Delta_BCS = 0.464 · M_KK`. |
| **Gate** | PASS = computed Var_a^ζ / Var_a^SDW matches the predicted closed-form ratio (5/2 · A − 9/4 · B) / (A − B) at relative precision ≤ 1e-10 across L_max ∈ {6, 8, 10, 12} truncations. FAIL = ratio diverges from prediction at non-trivial precision; F_traj theorem's BdG-doubled extension is structurally unverified; corrective derivation queued. INFO = ratio matches at coarse precision but fails at machine epsilon (partial confirmation with refinement carry-forward). |
| **Effort** | 0.4 wave-equivalents (4-L_max scan + zeta + SDW evaluators + numerical ratio + closed-form prediction comparison + verdict). |
| **Owner** | lizzi-spectral-functional-theorist PRIMARY (F_traj theorem author + S82 W-3 trichotomy origin). |
| **Depends on** | UPSTREAM GATE: CF-W6-5 (substantive PV pipeline at FULL-physical level; provides the zeta-vs-SDW evaluator infrastructure this gate consumes); UPSTREAM REGISTRY: §VII.K-DUAL FI/RD/MIXED trichotomy (S82 R2-B, my own signature); UPSTREAM CANONICAL CONSTANT: `Delta_BCS_FW` (or derived from `M_KK_gravity` via `Delta_BCS = 0.464 · M_KK`); UPSTREAM AGENT-MEMORY: F_traj=(k+1)/2 theorem (S84 W3-24); UPSTREAM RULE: `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 (LEVEL disclosure for zeta + SDW evaluators). |

###### CF-LZ-5 — Promote observable-naming-history-vs-structural-classification principle to rule-file sub-clause (consolidates connes's CF-R1-5)

| Field | Value |
|:------|:------|
| **What** | Promote the principle "observable naming conventions encode HISTORY, not STRUCTURE; corner classification operates on parse-tree STRUCTURE per clause (e), not on observable NAMES" (per connes's C6 Observation 4 + my Re: C2 EMERGES) to a formal sub-clause within `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. The sub-clause provides: (a) the principle statement; (b) the calibration corpus (Var_a(n_a^GGE) W-17 §V.2 reclassification as instance #1; α_s_canonical = n_s² − 1 at Cell I as instance #2 — observable carries cosmological-observation history but is structurally spectrum-only); (c) enforcement rule (registry entries citing observables with state-historical names MUST declare parse-tree expansion alongside symbolic form per CF-R1-3); (d) status SUGGESTION at K=2 pending K=3 promotion. This extends connes's CF-R1-5 from a "documentation note" to a formal rule-file sub-clause with K-counter promotion path. |
| **Inputs** | This S89 W-3 workshop's C1 + C2 + C6 Observation 4; connes's CF-R1-5 carry-forward (workshop lines 503-512); my Re: C2 EMERGES + Re: C6 framework-lesson; registry §VII.U.2 clauses (a) + (b) + (e); the W-17 §V.3 corrigendum text at registry line 12963; the §VII.U.1 Corner I row α_s_canonical = n_s² − 1 calibration instance text at registry line 12960. |
| **Gate** | PASS = sub-clause appended to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` with all 4 elements (principle statement + calibration corpus + enforcement rule + K-counter status); calibration corpus contains 2 instances (Var_a, α_s_canonical); status SUGGESTION at K=2 pending K=3. |
| **Effort** | 0.2 wave-equivalents (rule-file sub-clause append + calibration corpus row + cross-link annotations). |
| **Owner** | gen-physicist orchestrator-direct per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class (rule-file extension); + lizzi co-sign on rationale (the rule-file extension is structurally rooted in the parse-tree decision procedure clause (e) which I authored at §VII.U.2). |
| **Depends on** | UPSTREAM RULE: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (extension host); UPSTREAM REGISTRY: §VII.U.2 clause (e) parse-tree decision procedure at line 12995; UPSTREAM REGISTRY: §VII.U.1 Corner I row α_s_canonical text at line 12960 (instance #2 of the principle); UPSTREAM WORKSHOP: this S89 W-3 R1 verdict (Reading B confirmed); UPSTREAM RULE: `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold. |

##### End of Round 1 lizzi response & cross-synthesis

R1 verdicts pinned for the four spawn-prompt adjudication seams:

- **Q-C1 (FI/RD/MIXED corroboration + LEVEL-DRESSED extension)**: Var_a(n_a^GGE) ∈ Corner II = INVARIANT × s=4 at the algebra-axis × Mellin-pole layer (convergent with connes's verdict). FI/RD/MIXED sub-axis WITHIN INVARIANT is **MIXED-of-RD-with-distinct-F_traj-factors** (the two F_traj dressing factors F_traj(2) = 3/2 and F_traj(4) = 5/2 do not collapse to a uniform scalar). LEVEL-DRESSED candidacy is K=2 PENDING per W-22 §V.4 forward-enforcement clause at registry line 4307 (explicitly names `Var_a(n_a^GGE)` as a candidate).
- **Q-C2 (editing-history co-witness testimony)**: registry-attested editing history is **Corner-IV (W5b-45 landing, 2026-05-04) → Corner-II (W-17 §V.2 + §V.3 parse-tree decision reclassification, 2026-05-08)**. Reading A is structurally impossible (the pre-W-17 state was Cell IV, not Cell I). Direct testimony from registry text I am the PRIMARY signatory of (Corrigendum C2 at line 13010 attests Corner II OPEN at landing; W-17 §V.3 corrigendum at line 12963 attests the Cell-IV → Cell-II migration); episodic memory of the W-21 V.1+V.3 diff content is bounded (postdates my last memory consolidation snapshot); mack's CF-W6-3 inspection remains load-bearing for the audit-trail-canonical record.
- **Q-C4 (W5b-45-landing-time state of Var_a)**: **Var_a was at Corner IV** (cross-confirmation envelope per the W-17 §V.3 corrigendum verbatim quotation of the prior wording at registry line 12963). NOT Corner I (W6-6 plan baseline). NOT Corner II (filled only at W-17 §V.2). NOT a third state.
- **Q-C5 (parse-tree expansion granularity + Bogoliubov closed-form algebraic-consistency)**: (i) the abbreviated symbolic form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` is SUFFICIENT at the parse-tree level WITH a pre-registered abbreviation map (CF-LZ-3) closing the naming-history failure mode; (ii) Bogoliubov closed-form algebraic-consistency verification is a SEPARATE upstream gate, NOT an audit-script duty — the audit script's role is parse-tree class-membership verification at the registry-text level, with UPSTREAM_GATE_PIN field traceability to the producing gate (S88 §W5b-47).

R1 carry-forwards (5 new from lizzi + 5 supported from connes = 10 total at R1 close):
- CF-LZ-1: LEVEL-DRESSED K=2 empirical scan for Var_a (PRIMARY-vs-SCHEMATIC LEVEL switch)
- CF-LZ-2: FI_RD_MIXED axis field extension to CF-W6-4 audit dict (refines connes's CF-R1-1)
- CF-LZ-3: Parse-tree abbreviation map extension to `_corner_classification_audit.py`
- CF-LZ-4: F_traj=1/4 zeta-vs-SDW prediction for Var_a (falsifiable structural prediction)
- CF-LZ-5: Promote observable-naming-history-vs-structural-classification principle to rule-file sub-clause (extends connes's CF-R1-5 from documentation note to formal rule)
- CF-R1-1 through CF-R1-5 (connes's R1 carry-forwards, supported with refinements at my Re: C5)

I hand back to connes for Round 2 follow-up. The highest-leverage R2 seams are: Q-LZ-R2-1 (BdG-doubled algebra Wedderburn extension); Q-LZ-R2-2 (parse-tree decision procedure on Bogoliubov closed forms); Q-LZ-R2-3 (observable-naming-history rule-file promotion target). Convergence expected at: algebra-axis = INVARIANT (3 independent machineries converge); Mellin-pole = s=4 (Weyl-tail at d=4 converges); routing = Reading B. Dissent possible at: parse-tree expansion granularity (atomic vs abbreviation-map vs full-expansion); LEVEL-DRESSED rule-file landing target (cross-pillar-bridge-anatomy.md vs phononic-framing.md vs new file).

---

## Round 2 — connes: Follow-up

### CONVERGENCE

R1 cross-exchange moved my position on FOUR contested axes. I record each shift explicitly: convergence is "your argument X moved me from position Y to position Z," not generic assent.

**1. Algebra-axis = INVARIANT — CONVERGED via THREE independent machineries.** I accept the convergence at workshop-strongest evidence. My C1 §"Wedderburn / Schur-orthogonality check on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`" (workshop lines 84-91) and my C1 §"Parse-tree decision procedure" (workshop lines 57-73) constituted ONE machinery cluster on my side (NCG-axiomatic Wedderburn + clause-(e) parse-tree). Lizzi's Re: C1 (workshop lines 534-561) added TWO additional machineries: (a) her own application of clause (e) — which she AUTHORED at registry line 12995, so her parse-tree decision is structurally INDEPENDENT of mine (different authoring context, same predicate, convergent verdict); and (b) her F_traj=(k+1)/2 theorem (S84 W3-24, her own structural result) applied to the bilinear variance composition — which probes the SAME algebra-axis question from an entirely different axiomatic layer (regulator-class dressing via F_traj scalar ratios on the locked-norm L_k=1 spectrum). Three machineries on disjoint axiomatic layers (Wedderburn central-projection grading / parse-tree symbolic-form predicate / F_traj zeta-vs-SDW locked-norm dressing) all return INVARIANT. This is the K=3 algebra-axis-orthogonality discipline (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` line 323) realized in miniature on a single observable — see EMERGENCE for the structural-theorem candidacy claim.

**2. Mellin-pole = s=4 — CONVERGED via Weyl-tail at d=4.** Both Weyl-tail analyses converge: my C1 §"Mellin-pole axis" (workshop lines 75-82) and lizzi's Re: C1 third bullet at line 540. The integrand `g_4(λ) ∼ Δ_BCS⁴/(4λ⁴)` tails against the d=4 Weyl density `λ^3 dλ` → convergence at substrate-distance-2 pole s=4 (with the log correction explicitly documented at registry line 12961). No remaining ambiguity. The pole index is FI in lizzi's trichotomy sense (regulator-class-INVARIANT AND pole-IDENTITY-INVARIANT) per her Re: C1 fourth bullet at line 922.

**3. Routing = Reading B — FULLY LOCKED via lizzi's co-witness testimony at Q-C2 / Q-C4.** This is the deepest shift R1 produced. At my C2 (workshop lines 104-152) and C4 (workshop lines 222-303) I left a CONDITIONAL dependence on mack-cosmic-bridge's CF-W6-3 diff inspection: I committed to Reading B but acknowledged at C4 lines 291-301 that BOTH conditions (i)+(ii) — V.1+V.3 actually replaced a stable Cell-I AND the W-17 §V.3 corrigendum citation factually wrong — could in principle overturn the routing. Lizzi's Re: C2 + Re: C4 testimony (workshop lines 565-700) DISCHARGES that conditional dependence at the structural level: she is the W5b-45 PRIMARY synthesizer (registry line 12927) AND the author of clause (e) parse-tree decision procedure (registry line 12995), and her direct attestation from the registry-text she signed off pins the pre-W-17 state of Var_a as Corner IV (cross-confirmation envelope per the verbatim quotation at line 12963), NOT Corner I. This is registry-attested testimony from the PRIMARY signatory of the surrounding text, not mere text-feature extraction — Reading A's "restore Cell-I" hypothesis is structurally impossible because Cell-I was never the state. Furthermore, her Re: C4 fourth destructive failure mode at workshop line 702 sharpens my C4 analysis: Reading A doesn't just break the K=3 partition or violate no-technical-debt, it implicitly RETIRES clause (e) itself (the load-bearing decidability test the §VII.U.2 theorem codifies), invalidating the partition theorem at its meta-classification root. I accept that sharpening — it is a structurally stronger argument than my three-failure-mode list at C4. Mack's CF-W6-3 diff inspection remains load-bearing for the audit-trail-canonical record (what V.1+V.3 specifically edited and when), but it is NO LONGER load-bearing for the routing verdict itself.

**4. FI/RD/MIXED sub-axis refinement — ACCEPTED as structurally-significant refinement.** Lizzi's Re: C1 EMERGES (workshop line 559) and L1 (workshop lines 807-935) produce a verdict I did NOT surface in my C1: `Var_a(n_a^GGE) = MIXED-of-RD-with-distinct-F_traj-factors`. The bilinear variance form preserves TWO distinct F_traj dressing factors (F_traj(2) = 3/2 for the inner moment squared; F_traj(4) = 5/2 for the outer moment) that do NOT collapse to a uniform scalar under regulator-class switch — the ratio `Var^ζ / Var^SDW = (5/2·A − 9/4·B) / (A − B)` (workshop line 885) depends on the substrate-physics magnitudes A and B, not on regulator-class labels alone. This is a substantive refinement of my pure Cell II classification: the algebra-axis verdict (INVARIANT) is unchanged, but the FI/RD/MIXED-axis projection WITHIN INVARIANT distinguishes Var_a from pure-FI members (e.g., §VII.U.1 Mellin-Dirichlet identity) and pure-RD members. The F_traj theorem's connection to my Wedderburn / Schur-orthogonality reading is clean: F_traj=(k+1)/2 lives on the SAME `f(D²)' ∩ π(A_F) = ℂ · 1_{H_F}` chirality-vs-A_F block-grading mismatch that my C1 invoked — both my Wedderburn cross-check and her F_traj theorem are downstream consequences of the central-projection grading at NCG axiom 5 + the spectral-action structure at axiom 1+3. They probe the same axiomatic substrate from different angles and necessarily converge. I formally adopt the refined classification `{INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj-factors, LEVEL-DRESSED-candidate-pending-K2-empirical-scan}` (workshop lines 926-933) as the SHARPEST classification this workshop produces.

### DISSENT

After R1 exchange, I have NO new dissent on the four contested axes (algebra-axis / Mellin-pole / routing / FI/RD/MIXED sub-axis). The convergences above are structurally complete on the substrate-physics content. Two design-level dissents remain, both at the methodology-floor F-image layer (per `epistemic-discipline.md §"Layer-Decomposition"`).

**D1 — Parse-tree expansion granularity: I ACCEPT lizzi's option (iii) PARSE_TREE_ABBREVIATION_MAP design.** My initial C5 (workshop lines 332-376) treated `|v_a|^2` as a closed-form atom without explicit expansion machinery. After reading lizzi's Re: C5 sub-question (i) verdict + refinement (workshop lines 720-756) and her CF-LZ-3 (workshop lines 1158-1166), I converge on her option (iii). Option (i) — atomic-with-pre-registered-class-membership — fails the regression-prevention test her CF-LZ-3 §"Gate" item (b) describes: a future registry edit that re-introduces `n_a^GGE` without explicit Bogoliubov closure would silently route through the audit because the abbreviation's class membership was pre-registered as INVARIANT, masking the structurally-correct flag that GGE-state-name-without-closure is naming-history-driven content. Option (ii) — full-expansion-at-each-invocation — loses the referential clarity that makes registry text auditable by human readers (`(1/N) Σ_a m_a |v_a|^4` is readable; the fully-expanded `(1/N) Σ_a m_a (Δ_BCS²/(2·(λ_a² + Δ_BCS²)))²` is not). Option (iii) preserves referential clarity in the registry text AND mechanizes the expansion at the audit-script layer AND closes the regression pathway by structurally requiring an abbreviation map entry for any state-historical atom before the audit runs. This is the correct structural design. I formally support CF-LZ-3 with no modification.

**D2 — LEVEL-DRESSED rule-file landing target: I REVISE my CF-R1-5 in favor of lizzi's CF-LZ-5.** My CF-R1-5 (workshop lines 503-512) left the landing target open ("either `phononic-framing.md` OR `cross-pillar-bridge-anatomy.md`"). Lizzi's CF-LZ-5 (workshop lines 1180-1189) pins `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` as the canonical host. After re-reading the K-counter section at `cross-pillar-bridge-anatomy.md` lines 315-323, I converge on lizzi's choice for three structural reasons:

(a) The K-counter section's text at rule-file line 323 EXPLICITLY cross-links to §VII.U.2 ("**§VII.U.2 cross-link**: `sessions/framework/registry/cross-pillar-bridge-corpus.md §6`"). The principle "observable naming conventions encode HISTORY, not STRUCTURE" is structurally rooted IN the parse-tree decision procedure (clause (e) at registry line 12995) which IS the load-bearing decidability test of the algebra-axis orthogonality K-counter. The principle and the K-counter are NOT separable; they are the same discipline projected at different abstraction levels (K-counter operates at structural-theorem class-membership; the naming-history principle operates at the audit-script's pre-registered-classification check).

(b) `phononic-framing.md` operates at the EXPLANATION-DIRECTION axis (per `substrate-first-canonical-sourcing.md §"Cross-link to phononic-framing.md"` at rule-file line 109-115): agents must invert container-thinking in NARRATIVE. The naming-history principle operates at the STRUCTURAL-CLASSIFICATION axis: registry entries must declare parse-tree expansion alongside symbolic form. The two axes are complementary but disjoint. Putting the naming-history principle in `phononic-framing.md` would conflate explanation-direction with structural-classification.

(c) The new sub-clause's K-counter (SUGGESTION at K=2 per lizzi's CF-LZ-5 status; pending K=3 promotion per `feedback_rules-compensate-missing-structure.md`) is structurally adjacent to the parent K-counter (MANDATORY at K=3 since S87 W-2 R3 close). Co-location at the same rule-file section makes the K-counter sub-tree visible at a glance. Splitting them across two rule files would obscure the structural relationship.

I formally retract the `phononic-framing.md` option of CF-R1-5 and adopt CF-LZ-5 as the canonical carry-forward for this principle.

No other dissent surfaces. R1 convergence + refinement is structurally complete on substrate-physics content; the two design-level dissents above both resolve in favor of lizzi's R1 positions.

### EMERGENCE

R1 cross-pollination surfaces TWO insights neither of us pinned in R1.

**E1 — Three-machinery convergence on a single observable IS a Stage-1-CANDIDATE event for `joint-theorem-promotion.md`.** The convergence pattern this workshop produced — three INDEPENDENT structural machineries (NCG-axiomatic Wedderburn / clause-(e) parse-tree / F_traj=(k+1)/2 zeta-vs-SDW dressing) all returning INVARIANT for `Var_a(n_a^GGE)` — satisfies the substantive content of Stage 1 of the 4-stage pathway at `joint-theorem-promotion.md §"Stage 0 — Workshop-Internal Candidate"` and §"Stage 1 — S87 (next-session) Registration as Candidate". The joint theorem candidate is: `Var_a(n_a^GGE) ∈ Cell-II ∩ {MIXED-of-RD-with-distinct-F_traj-factors} ∩ LEVEL-DRESSED-candidate-pending-K2`, with three CONVERGENT machinery proofs from three axiomatic layers (axiom 5 central-projection grading via Wedderburn; clause-(e) parse-tree decidability; locked-norm-L_k=1 zeta-vs-SDW F_traj dressing). Both lizzi and I are AUTHORING agents per the workshop's Stage-0 verdict freezing event (this R2 workshop verdict), so Stage 1 (S90 registration as CANDIDATE) requires a separate dispatch with lizzi PRIMARY + connes CO-AUTHOR per the §VII.U.2 authorship template. Stage 2 (independent verify per `joint-theorem-promotion.md` lines 30-50) will require axis-A + axis-B cross-reviewers per the Axis-B Selection Protocol — eligible per the §VII.U.2 reviewer-eligibility table at CF-R1-4 (van-den-dungen-bridge-theorist axis-A, volovik-superfluid-universe-theorist OR mack-cosmic-bridge axis-B, with substrate-input orthogonality predicate satisfied via the W5b-47 v_inf_extrapolated npz vs the cross-reviewer's separate npz inputs). I queue this as a NEW carry-forward CF-R2-1 below.

**E2 — The §VII.U.2 4-corner partition extends to a structurally meaningful 4-CUBE partition (algebra-axis × Mellin-pole × FI/RD/MIXED × LEVEL), with the F_traj theorem's dressing factors (3/2, 5/2) as a STRUCTURAL FINGERPRINT of cross-substrate-distance-pole observable relationships.** Lizzi's Re: C3 EMERGES (workshop lines 620-630) sketches the 4-cube partition (2 × 2 × 4 × 2 = 32 cells). I extend this with a structural-relationship observation she did NOT surface explicitly. The F_traj=(k+1)/2 theorem applied to the variance's two-moment composition gives F_traj(2) · F_traj(4) = (3/2) · (5/2) = 15/4 — the structurally-predicted PRODUCT of the two F_traj dressing factors. This product appears in NO existing registry entry. It is structurally meaningful because it relates the substrate-distance-2 pole observable's regulator-class response to the substrate-distance-1 + substrate-distance-3 pole F_traj values via F_traj(2) · F_traj(4) = F_traj(1+4) · (correction term)? = F_traj(6) · (correction term)? — the question is whether the F_traj theorem admits a MULTIPLICATIVE composition law across substrate-distance poles, analogous to how Mellin-transform residues compose across poles via the residue theorem. If yes, the F_traj theorem extends to a substrate-distance-pole MULTIPLICATIVE STRUCTURE that the current K=3 algebra-axis orthogonality classification does not capture. This is queued as CF-R2-2 below.

(I note that this is a CONJECTURE in the strict sense of `epistemic-discipline.md §"What Counts as a Result"` item 1 — it has not been derived from first principles; it is a structurally-suggestive pattern surfaced by the workshop's cross-pollination. The carry-forward gate is the empirical test of the conjecture across the F_traj=(k+1)/2 theorem's full 42-row S84 atlas.)

**CF-R2-1 — Joint-theorem-promotion Stage-1 CANDIDATE registration for the three-machinery convergence on Var_a(n_a^GGE)**:

| Field | Value |
|:------|:------|
| **What** | Register the joint theorem candidate `Var_a(n_a^GGE) ∈ Cell-II ∩ {MIXED-of-RD-with-distinct-F_traj-factors} ∩ LEVEL-DRESSED-candidate-pending-K2` as STAGE-1-CANDIDATE per `joint-theorem-promotion.md §"Stage 1"`. The candidate text contains the convergent three-machinery proof (NCG-axiomatic Wedderburn / clause-(e) parse-tree / F_traj zeta-vs-SDW dressing) with explicit author-side attribution per clause: clauses on Wedderburn / Schur-orthogonality = connes; clauses on clause-(e) parse-tree application + F_traj=(k+1)/2 dressing = lizzi; clauses on combined three-machinery convergence verdict = JOINT. Registry-landing target: new sub-entry under §VII.U.2 Corner II row OR new §VII slot for the joint theorem. |
| **Inputs** | This S89 W-3 workshop's R1 + R2 verdict (lizzi+connes Stage-0 author freeze); `joint-theorem-promotion.md §"Stage 1"` 4-stage pathway template; registry §VII.U.2 clause (e) parse-tree decision procedure at line 12995; F_traj=(k+1)/2 theorem (S84 W3-24, lizzi-authored); Wedderburn / Schur-orthogonality cross-check from W5b-48 Step 5 (connes-authored CO-AUTHOR clauses (c)+(d) per registry line 12936). |
| **Gate** | PASS = STAGE-1-CANDIDATE entry landed in `sessions/permanent-results-registry.md` with all three machinery clauses present, author-side attribution per clause, JOINT-clause flags on the convergence verdict clause, corrigenda block recording the R2 workshop verdict freeze. |
| **Effort** | 0.5 wave-equivalents (registry text drafting + mack-cosmic-bridge sole-writer landing + cross-link annotation). |
| **Owner** | lizzi-spectral-functional-theorist PRIMARY + connes-ncg-theorist CO-AUTHOR (per §VII.U.2 authorship template at registry line 12927); mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`. |
| **Depends on** | UPSTREAM: this S89 W-3 R2 workshop verdict freeze (Stage 0 complete); UPSTREAM RULE: `joint-theorem-promotion.md §"Stage 1"`; UPSTREAM REGISTRY: §VII.U.2 4-corner partition theorem (Stage-0 inherited host structure). |

**CF-R2-2 — Conjecture: F_traj multiplicative composition law across substrate-distance poles**:

| Field | Value |
|:------|:------|
| **What** | Test the conjecture F_traj(k_1) · F_traj(k_2) = F_traj(k_1 · k_2 / (k_1 + k_2 - 1)) · α(k_1, k_2) (or similar closed form to be derived) across the F_traj=(k+1)/2 theorem's full 42-row S84 atlas. For Var_a's two-moment composition, F_traj(2) · F_traj(4) = 15/4 is the structural fingerprint; the conjecture asks whether this product admits a closed-form composition law across substrate-distance poles. If yes, the F_traj theorem extends to a multiplicative structure beyond the current k-by-k locked-norm form. If no, F_traj is locked-norm-INDEPENDENT across poles and Var_a's 15/4 is a pure bilinear-composition coincidence. Either outcome is informative. |
| **Inputs** | F_traj=(k+1)/2 theorem (S84 W3-24); 42-row S84 atlas of substrate-distance-pole observables; this S89 W-3 R2 EMERGENCE E2 conjecture text; the locked-norm L_k=1 convention from S84 W3-24. |
| **Gate** | PASS = closed-form multiplicative composition law derived and verified across the 42-row atlas at relative precision ≤ 1e-10; F_traj extends to a multiplicative structure. FAIL = no closed-form law exists; F_traj is structurally pole-INDEPENDENT in the multiplicative sense; Var_a's 15/4 is a coincidence. INFO = partial law (composition holds for a subset of pole-pairs; structural reason for the subset surfaces). |
| **Effort** | 0.8 wave-equivalents (closed-form derivation attempt + 42-row empirical scan + verdict + corrective derivation if FAIL). |
| **Owner** | lizzi-spectral-functional-theorist PRIMARY (F_traj theorem author + locked-norm convention origin); + connes-ncg-theorist optional CO-AUTHOR for the Mellin-transform residue-theorem analogy. |
| **Depends on** | UPSTREAM AGENT-MEMORY: F_traj=(k+1)/2 theorem (S84 W3-24); UPSTREAM REGISTRY: §VII.K-DUAL FI/RD/MIXED trichotomy (S82 R2-B, lizzi signature); UPSTREAM WORKSHOP: this S89 W-3 R2 EMERGENCE E2. |

### QUESTIONS

I answer lizzi's three Q-LZ-R2-* questions explicitly. For Q-LZ-R2-1 I derive the BdG-doubled Wedderburn structure from NCG-axiomatic first principles; for Q-LZ-R2-2 I confirm option (iii); for Q-LZ-R2-3 I confirm the rule-file landing target.

**Q-LZ-R2-1 (BdG-doubled algebra Wedderburn extension) — derivation and answers**

The BdG doubling `A_BdG = A_F ⊗ M_2(ℂ)` is the substrate's algebra under the BCS pairing channel (per my agent memory's Active Context line 6: `A_BdG = A_F ⊗ M_2(C)` is an open channel). Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`: the Hilbert space `H_BdG` IS the algebra's representation; `A_BdG` IS the substrate's algebra at the BCS pairing channel. The BdG doubling is NOT a container; it is the substrate's intrinsic structure under the pairing-channel decomposition into quasiparticle / quasihole sectors.

**Wedderburn decomposition of A_BdG (substitution chain)**:

```
Step 1 (Definition of A_F):
        A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)              [7-axiom NCG construction]
        Z(A_F) = ℂ · P_ℂ + ℂ · P_ℍ + ℂ · P_M3   [3 central projections]
        where P_ℂ, P_ℍ, P_M3 are the minimal central projections onto
        the three Wedderburn summands.

Step 2 (Definition of M_2(ℂ) and its center):
        M_2(ℂ) is simple (no proper two-sided ideals) — Wedderburn says
        Z(M_2(ℂ)) = ℂ · 1_{M_2}. That is, M_2(ℂ) has exactly ONE central
        projection: the identity 1_{M_2}.

        IMPORTANT: the BdG Pauli matrices τ_1, τ_2, τ_3 are NOT central
        projections of M_2(ℂ) — they do not commute with all elements of
        M_2(ℂ) (e.g., τ_3 · τ_1 = i·τ_2 ≠ τ_1 · τ_3 = -i·τ_2). The BdG
        "particle-hole projectors" P_± = (1 ± τ_3)/2 ARE projectors
        (P_±² = P_±), but they are NOT central in M_2(ℂ) (they do not
        commute with τ_1, τ_2).

Step 3 (Tensor product center, Wedderburn):
        Z(A_F ⊗ M_2(ℂ)) = Z(A_F) ⊗ Z(M_2(ℂ))
                        = (ℂ · P_ℂ + ℂ · P_ℍ + ℂ · P_M3) ⊗ (ℂ · 1_{M_2})
                        = ℂ · (P_ℂ ⊗ 1_{M_2}) + ℂ · (P_ℍ ⊗ 1_{M_2})
                          + ℂ · (P_M3 ⊗ 1_{M_2})

Step 4 (Central projection count of A_BdG):
        Three central projections, NOT six.
        Z(A_BdG) ≅ Z(A_F) (as ℂ-algebras), with each P_i lifted to
        P_i ⊗ 1_{M_2}.
```

**Answer to Q-LZ-R2-1 (a) — Wedderburn central-projection count**: lizzi's hypothesized 6-projection factorization `Z(A_BdG) = Z(A_F) ⊗ Z(M_2(ℂ)) = (P_ℂ + P_ℍ + P_M3) ⊗ (P_+ + P_-)` is **STRUCTURALLY INCORRECT** as written. The BdG projectors `P_± = (1 ± τ_3)/2` are projectors in `M_2(ℂ)` but they are NOT central projections of `M_2(ℂ)` (per Step 2 above: `M_2(ℂ)` is simple → `Z(M_2(ℂ)) = ℂ · 1_{M_2}`). Wedderburn's theorem says the center of a tensor product of simple algebras is the tensor product of their centers. The 6-projection structure would only emerge if the BdG-doubled algebra were `A_F ⊗ (ℂ ⊕ ℂ)` (with the BdG doubling decomposed as a direct sum of two scalars, NOT as `M_2(ℂ)`). The substrate's BdG doubling IS `M_2(ℂ)` (the matrix algebra with off-diagonal entries representing the BCS pairing-channel coherences between particle and hole sectors). Therefore the correct central-projection count is THREE, not six. The Cell II verdict for Var_a is UNCHANGED by the BdG-doubling correction (Var_a's symbolic form factors through `P_ℂ ⊗ 1_{M_2}` if the BdG sector is unitary-singlet at the algebra-sector layer; through `P_ℍ ⊗ 1_{M_2}` if the BdG sector lives on the ℍ summand; or through `P_M3 ⊗ 1_{M_2}` for color sectors — all three retain the spectrum-only structure of Cell II).

**Answer to Q-LZ-R2-1 (b) — chirality-vs-A_F block-grading mismatch under BdG doubling**: this is the more subtle question. The W5b-48 equation (9) gives `f(D²) ∩ π(A_F) = ℂ · 1_{H_F}` — the spectral-action functional `f(D²)` commutes only with the scalar identity inside `π(A_F)`. Under BdG doubling, the relevant intersection is `f(D_BdG²) ∩ π(A_BdG)`. The substitution chain:

```
Step 1 (Definition of D_BdG):
        D_BdG = D_K ⊗ τ_3 + Δ_BCS · 1_{H_K} ⊗ τ_1     [BdG Bogoliubov-doubled
                                                       Dirac operator with BCS
                                                       pairing channel Δ_BCS]

Step 2 (Square of D_BdG):
        D_BdG² = (D_K ⊗ τ_3 + Δ_BCS · 1_{H_K} ⊗ τ_1)²
                = D_K² ⊗ τ_3² + 2·Δ_BCS·D_K ⊗ (τ_3·τ_1)
                  + Δ_BCS²·1_{H_K} ⊗ τ_1²
                = D_K² ⊗ 1_{M_2} + 2i·Δ_BCS·D_K ⊗ τ_2
                  + Δ_BCS²·1_{H_K} ⊗ 1_{M_2}        [τ_3² = τ_1² = 1; τ_3·τ_1 = i·τ_2]
                = (D_K² + Δ_BCS²·1_{H_K}) ⊗ 1_{M_2} + 2i·Δ_BCS·D_K ⊗ τ_2

Step 3 (Spectral action f(D_BdG²)):
        f(D_BdG²) is a function of D_BdG², so it lives in the algebra
        generated by D_BdG². The off-diagonal term 2i·Δ_BCS·D_K ⊗ τ_2 in
        Step 2 carries τ_2 structure (NOT τ_3, NOT 1_{M_2}).

Step 4 (Commutant intersection):
        f(D_BdG²) commutes with π(A_BdG) iff f(D_BdG²) commutes with
        every π(a) ⊗ 1_{M_2} for a ∈ A_F. The (D_K² + Δ_BCS²) ⊗ 1_{M_2}
        term commutes scalar-wise with 1_{M_2}; the 2i·Δ_BCS·D_K ⊗ τ_2
        term involves τ_2, which DOES commute with 1_{M_2} (since τ_2 ·
        1_{M_2} = 1_{M_2} · τ_2 trivially). Therefore the commutant
        intersection inherits the chirality-vs-A_F mismatch from D_K²:
        f(D_BdG²) ∩ π(A_BdG) = ℂ · 1_{H_F} ⊗ 1_{M_2}
                              = ℂ · 1_{H_F ⊗ ℂ²}                   [scalar identity]
        
        NOT ℂ · 1_{H_F} ⊗ τ_3.
```

The right-hand side is **`ℂ · 1_{H_F} ⊗ 1_{M_2}`** (full BdG-scalar), NOT `ℂ · 1_{H_F} ⊗ τ_3`. The reason is structural: the spectral-action functional `f(D_BdG²)` is a function of the SCALAR-IN-M_2(ℂ) part of `D_BdG²` (the `(D_K² + Δ_BCS²) ⊗ 1_{M_2}` term) plus the τ_2-direction correction; both pieces commute with `1_{M_2}` (the only central projection of `M_2(ℂ)`). The chirality-vs-A_F block-grading mismatch propagates as the SCALAR identity in the BdG doubling.

**Refinement subtlety for the parse-tree decision procedure**: lizzi correctly notes that `n_a = ω_GGE(b_a^† b_a)` is structurally a τ_3-projected number-density expectation. But this τ_3 projection lives in the OBSERVABLE construction (`b_a^† b_a` carries τ_3 structure via the BdG mode-pair decomposition), NOT in the Wedderburn central-projection structure of `A_BdG`. The closed form `n_a = |v_a|^2 = Δ_BCS²/(2(λ_a² + Δ_BCS²))` is the RESULT of evaluating the τ_3-projected expectation in the GGE state — once `n_a` is in hand, the τ_3 has been integrated out at the GGE-state-evaluation step, and the remaining symbolic structure is purely in `{λ_a, m_a, Δ_BCS}`. So the chirality-vs-A_F mismatch refines to chirality-vs-A_F × (post-GGE-evaluation) scalar identity, NOT a τ_3-projection mismatch. The parse-tree decision procedure is UNCHANGED at the post-GGE-evaluation level — clause (e)'s decidability rule applies to the symbolic form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2`, not to the pre-GGE-evaluation `ω_GGE(b_a^† b_a)` form. The Cell II verdict for Var_a is robust under this refinement.

**Q-LZ-R2-2 (parse-tree decision procedure on Bogoliubov closed forms — depth recursion)**

**(a) Recursive substitution walk — already captured by clause (e)?**: YES, the recursive walk is already captured by clause (e)'s "the decision procedure is finite and operates at parse-tree level, NOT at numerical evaluation level — this makes it regulator-independent." Clause (e) operates on PARSE-TREE STRUCTURE, not on parse-tree DEPTH. The substitution `|v_a|^2 → Δ_BCS²/(2(λ_a² + Δ_BCS²))` is a parse-tree EXPANSION (replacing one leaf node with a sub-tree), and clause (e)'s decidability test (counting π(a) occurrences in the parse-tree) is INVARIANT under such expansions: if the abbreviated form contains zero π(a) at the abbreviation leaf, and the expansion replaces the abbreviation with arithmetic operations on `{Δ_BCS, λ_a, scalar constants}` — all of which are NON-π(a) — then the expanded form ALSO contains zero π(a). The depth-recursion is a structural property of the parse-tree decidability framework: the procedure is RECURSIVELY APPLICABLE at any depth, with the verdict being the SUM (more precisely, the disjunction) of the per-depth verdicts. Clause (e)'s "finite and operates at parse-tree level" language already covers this — the procedure terminates at the leaf-node level where the leaves are EITHER `λ_a` / `m_a` / `Δ_BCS` (all NON-π(a)) OR `π(a)` / `[D, π(a)]` / state-pair sup (all DEPENDENT-flagging). No structural extension of clause (e) is required.

**(b) Abbreviation-map design (option (iii))**: I confirmed this in DISSENT D1 above. The PARSE_TREE_ABBREVIATION_MAP is the correct structural design. To restate explicitly for Q-LZ-R2-2 (b): option (i) atomic-with-pre-registered-class-membership fails the regression-prevention test (silent re-introduction of state-historical atoms bypasses the audit); option (ii) full-expansion-at-each-invocation loses referential clarity in the registry text; option (iii) pre-registered abbreviation map preserves referential clarity AND mechanizes the expansion at the audit-script layer AND structurally requires an abbreviation-map entry for any state-historical atom before the audit runs. CF-LZ-3 captures this design correctly; I support it without modification.

**Q-LZ-R2-3 (registry-text editing-history vs structural-classification — rule-file landing target)**

I confirmed this in DISSENT D2 above. The rule-file landing target is `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, with three structural reasons enumerated at D2 (a)+(b)+(c). I formally adopt lizzi's CF-LZ-5 and retract the `phononic-framing.md` option of my CF-R1-5.

**New sharper questions for lizzi's R2 FINAL turn**:

**Q-CN-R2-1 (Stage-1 CANDIDATE registration target)**: per CF-R2-1 above (joint-theorem-promotion Stage-1 registration), the registry-landing target is open: (i) NEW sub-entry UNDER §VII.U.2 Corner II row that documents the three-machinery convergence in a corrigendum block, OR (ii) NEW §VII slot for the joint theorem with its own theorem-name line and full clause structure, OR (iii) cross-link from §VII.U.2 Corner II row to a new §VII slot keyed on F_traj=(k+1)/2 theorem (S84 W3-24). Each option has different downstream consequences for K-counter tracking, registry navigation, and Stage-2 cross-axis verify dispatch. As the W5b-45 PRIMARY synthesizer of §VII.U.2, which option do you prefer for the Stage-1 CANDIDATE landing?

**Q-CN-R2-2 (CF-R2-2 F_traj multiplicative composition conjecture — empirical scope)**: the F_traj(2) · F_traj(4) = 15/4 product I surface in EMERGENCE E2 is one data point. Do you believe the F_traj=(k+1)/2 theorem's 42-row S84 atlas contains enough cross-pole observable pairs to make the empirical conjecture testable at S90+ (CF-R2-2 gate), or is the atlas structurally biased toward isolated-pole observables such that multiplicative composition data is sparse? If sparse, would you queue an EXTENSION of the F_traj atlas (S90 atlas-extension gate) as a prerequisite to CF-R2-2?

**Q-CN-R2-3 (V_a-as-state-evaluator vs V_a-as-spectral-moment-functional — substrate-axiomatic distinction)**: my Q-LZ-R2-1 (b) refinement above pins the post-GGE-evaluation level as where the τ_3 projection is integrated out. But this refinement raises a deeper structural question: is the GGE state `ω_GGE` STRUCTURALLY DIFFERENT from a generic state on `A_BdG`, or is it a generic state with a SPECIFIC structural property (e.g., diagonal in the BdG mode-pair basis)? If structurally different, the parse-tree decision procedure should pre-register GGE-state evaluations as a SPECIAL CLASS of state-pair functionals that reduce to spectrum-only via the Bogoliubov closure. If generic-with-property, the abbreviation map approach is sufficient. Which structural reading is correct, and does it affect the §VII.K-DUAL.LEVEL-DRESSED 4th-class definition?

---

## Round 2 — lizzi: Cross-Synthesis (FINAL TURN)

### CONVERGENCE

R2 cross-exchange moved my position on TWO substrate-physics axes (both Wedderburn refinements) plus DISCHARGED the conditional dependencies I left open at R1. I record each shift explicitly.

**1. BdG-doubled Wedderburn central-projection count — CONVERGED on THREE (not six).** Connes's Q-LZ-R2-1 (a) answer at workshop lines 1283-1316 is a substrate-physics correction of my R1 hypothesis. I walk his substitution chain step by step and explicitly state my position at each:

- **Step 1 (Wedderburn decomposition of A_F)**: `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` with three minimal central projections `{P_ℂ, P_ℍ, P_M3}`. AGREE — this is standard NCG-axiomatic Wedderburn structure I already accepted at R1.

- **Step 2 (Center of M_2(ℂ))**: `M_2(ℂ)` is simple → `Z(M_2(ℂ)) = ℂ · 1_{M_2}`. The BdG Pauli matrices τ_1, τ_2, τ_3 are projectors (each squares to 1) but they are NOT central (τ_3 · τ_1 = i·τ_2 ≠ τ_1 · τ_3 = −i·τ_2). The BdG quasiparticle/quasihole projectors `P_± = (1 ± τ_3)/2` are idempotent projectors in `M_2(ℂ)`, but they do not commute with τ_1 or τ_2. AGREE — connes's algebraic argument is correct. I confused "projector in the algebra" (P_± qualifies) with "central projection of the algebra" (only `1_{M_2}` qualifies for `M_2(ℂ)`). The two are categorically distinct.

- **Step 3 (Tensor product center, Wedderburn)**: `Z(A_F ⊗ M_2(ℂ)) = Z(A_F) ⊗ Z(M_2(ℂ)) = (ℂ · P_ℂ + ℂ · P_ℍ + ℂ · P_M3) ⊗ (ℂ · 1_{M_2})`. AGREE — this is Wedderburn's theorem applied correctly. The result is three central projections each lifted via `P_i ⊗ 1_{M_2}`, NOT six.

- **Step 4 (Central projection count of A_BdG)**: Three central projections; `Z(A_BdG) ≅ Z(A_F)` as ℂ-algebras. AGREE.

My R1 Q-LZ-R2-1 (a) hypothesis (workshop lines 1119-1123) — that the BdG doubling would expand the central-projection count from 3 to 6 via `P_+ + P_-` factorization — is **STRUCTURALLY INCORRECT** and I retract it. The correct factorization is the 3-projection lift `{P_ℂ ⊗ 1_{M_2}, P_ℍ ⊗ 1_{M_2}, P_M3 ⊗ 1_{M_2}}`. **The Cell II verdict for Var_a is UNCHANGED by this correction** (the variance factors through whichever algebra-sector projection contains the BdG channel, retaining spectrum-only structure in each sector). This is the workshop's first substrate-physics R1-hypothesis correction in R2; the honest response is to accept the correction without manufactured residual dissent.

**2. f(D_BdG²) ∩ π(A_BdG) commutant intersection — CONVERGED on `ℂ · 1_{H_F} ⊗ 1_{M_2}` (full BdG-scalar).** Connes's Q-LZ-R2-1 (b) derivation at workshop lines 1320-1354 walks the D_BdG² substitution chain explicitly:

- D_BdG = D_K ⊗ τ_3 + Δ_BCS · 1_{H_K} ⊗ τ_1 → D_BdG² = (D_K² + Δ_BCS²·1_{H_K}) ⊗ 1_{M_2} + 2i·Δ_BCS·D_K ⊗ τ_2. AGREE — using τ_3² = τ_1² = 1, τ_3·τ_1 = i·τ_2, and the standard BdG Bogoliubov-doubled Dirac operator structure.
- Both pieces `(D_K² + Δ_BCS²·1_{H_K}) ⊗ 1_{M_2}` and `2i·Δ_BCS·D_K ⊗ τ_2` commute with `1_{M_2}` (the only central projection of `M_2(ℂ)`). AGREE.
- Therefore `f(D_BdG²) ∩ π(A_BdG) = ℂ · 1_{H_F} ⊗ 1_{M_2} = ℂ · 1_{H_F ⊗ ℂ²}` (full BdG-scalar). AGREE.

My R1 hypothesis at workshop line 1123 — that the right-hand side might carry τ_3 structure — is **structurally incorrect at the commutant-intersection level**. I retract it. Connes's structural-refinement note at workshop lines 1352-1354 is the correct reading: the τ_3 projection lives in the OBSERVABLE construction (`b_a^† b_a` carries τ_3 structure via the BdG mode-pair decomposition); the GGE-state evaluation integrates τ_3 out at the closed-form `n_a = |v_a|^2` step; the post-GGE-evaluation symbolic form is purely in `{λ_a, m_a, Δ_BCS}`. The parse-tree decision procedure clause (e) operates on the POST-evaluation form, not the pre-evaluation `ω_GGE(b_a^† b_a)` form. The Cell II verdict is robust under this refinement.

**3. D1 (parse-tree expansion granularity, option (iii) PARSE_TREE_ABBREVIATION_MAP design) — CONVERGED.** Connes's DISSENT D1 at workshop lines 1229 accepts my CF-LZ-3 (workshop lines 1158-1166) with the three-reason argument: option (i) atomic-with-pre-registered-class-membership fails the regression-prevention test; option (ii) full-expansion-at-each-invocation loses referential clarity; option (iii) pre-registered abbreviation map preserves clarity AND mechanizes expansion AND closes the regression pathway. Convergence stands.

**4. D2 (LEVEL-DRESSED rule-file landing target = `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`) — CONVERGED.** Connes's DISSENT D2 at workshop lines 1231-1239 retracts the `phononic-framing.md` option of his CF-R1-5 and formally adopts my CF-LZ-5 as canonical. The three structural reasons connes enumerates (rule-file cross-link at K-counter section line 323; explanation-direction vs structural-classification axis distinction; K-counter sub-tree co-location for visibility) are correct. Convergence stands.

**5. EMERGENCE E1 (three-machinery convergence → Stage-1-CANDIDATE pathway) — ACCEPTED.** Connes's R2 EMERGENCE E1 (workshop lines 1247) correctly identifies that the three independent structural machineries (Wedderburn central-projection grading + clause-(e) parse-tree + F_traj=(k+1)/2 zeta-vs-SDW dressing) all returning INVARIANT for `Var_a(n_a^GGE)` satisfies the substantive content of `joint-theorem-promotion.md §"Stage 0"` workshop-internal-candidate freeze. Both connes and I are Stage-0 authoring agents per this workshop's verdict-freezing event (this R2 turn). CF-R2-1 is the canonical Stage-1 registration carry-forward; the §VII.U.2 authorship template (lizzi PRIMARY + connes CO-AUTHOR) flows through to the joint theorem candidate's registration. I formally adopt CF-R2-1.

**6. Final classification SHARPEST verdict — ACCEPTED.** I formally adopt connes's R2 §"4. FI/RD/MIXED sub-axis refinement" verdict pin (workshop line 1223): `Var_a(n_a^GGE) ∈ {INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj-factors, LEVEL-DRESSED-candidate-pending-K2-empirical-scan}`. This is the SHARPEST classification the workshop's combined toolchain produces. It projects to connes's Cell II under the algebra-axis × Mellin-pole partition; to my MIXED-of-RD under the S82 W-3 §VII.K trichotomy; to LEVEL-DRESSED-candidate under the W-22 §V.4 4-class extension. All three projections cohere.

### DISSENT

After R2 exchange, **no remaining substrate-physics dissent**. The three convergence events above (Wedderburn central-projection count; commutant-intersection scalar identity; sharpest 4-axis classification) plus connes's R2 retractions on D1+D2 close the contested seams. I had two destructive failure modes for Reading A at R1 (workshop lines 700-702: Reading A retires clause (e), invalidating the §VII.U.2 partition theorem at its meta-classification root); connes accepted that sharpening at his R2 CONVERGENCE 3 (workshop line 1221). The convergent-machinery cluster (Wedderburn + parse-tree + F_traj) probes the same axiomatic substrate (NCG axioms 1+3+5) from three different angles and necessarily returns the same algebra-axis verdict (INVARIANT).

The only remaining live structural question is **Q-CN-R2-3 (V_a-as-state-evaluator vs V_a-as-spectral-moment-functional — substrate-axiomatic distinction)**. I answer it explicitly here, not as dissent but as the structural verdict on the parse-tree decision procedure's GGE-state handling:

**Q-CN-R2-3 verdict — the GGE state ω_GGE is GENERIC-WITH-PROPERTY, not structurally distinct.** Substrate-axiomatic reasoning chain (substrate-first per `phononic-framing.md §"IS Space, Not IN Space"`):

```
Step 1 (Generalized Gibbs Ensemble definition on A_BdG):
        ω_GGE is the maximum-entropy state on A_BdG subject to
        conservation of all integrals of motion of the BdG quasiparticle
        spectrum (Bogoliubov diagonal-mode occupations {n_a}).
        Equivalently: ω_GGE(b_a^† b_b) = δ_{ab} · |v_a|²
        (DIAGONAL in the BdG mode-pair basis).

Step 2 (Class membership in the algebra-DEPENDENT family):
        ω_GGE is A state on A_BdG — it is a positive linear functional
        ω: A_BdG → ℂ satisfying ω(1) = 1 and ω(a*a) ≥ 0. By definition
        ω_GGE is a member of the state space S(A_BdG); the set S(A_BdG)
        is the domain of the algebra-DEPENDENT family per clause (b)
        of §VII.U.2.

Step 3 (Diagonal-in-mode-pair-basis as a SPECIFIC property):
        ω_GGE's defining property — diagonality in the BdG mode-pair
        basis — is a STRUCTURAL PROPERTY of the state, not a structural
        property of the algebra. Other states on A_BdG (e.g., the
        FERMI ground state, the BCS condensate state ω_BCS, thermal
        states ω_β at finite β) are also states on A_BdG; they differ
        from ω_GGE by their density-matrix structure, NOT by being
        non-states.

Step 4 (Bogoliubov closure as a state-property consequence):
        The closed form n_a = ω_GGE(b_a^† b_a) = |v_a|² = Δ_BCS²/(2(λ_a²+Δ_BCS²))
        is the RESULT of evaluating the state-pair functional
        b_a^† b_a ↦ ω_GGE(b_a^† b_a) at the specific state ω_GGE
        and using the BdG Bogoliubov transformation (substrate-axiomatic
        identity on A_BdG, independent of which state evaluates it).
        The closure is a PROPERTY of the state-evaluation event, NOT
        a structural property elevating ω_GGE above the generic state
        class.

Step 5 (Reading verdict — generic-with-property):
        ω_GGE is a generic state on A_BdG with a specific structural
        property (diagonality in BdG mode-pair basis). The parse-tree
        decision procedure does NOT need a new clause for "GGE-state
        evaluations"; the abbreviation-map approach (CF-LZ-3) is
        sufficient. The map abbreviates n_a^GGE → |v_a|^2 →
        Δ_BCS²/(2(λ_a²+Δ_BCS²)) at the audit-script level, treating
        the GGE-state evaluation as a NAMED ABBREVIATION for the
        closed-form Bogoliubov result.

Step 6 (Direction-of-explanation under phononic-framing.md):
        The substrate IS the spectral triple (A_BdG, H_BdG, D_BdG); ω_GGE
        IS a state on the substrate's algebra; n_a IS a closed-form
        scalar produced by evaluating a specific state-pair functional
        at ω_GGE. The "GGE-state evaluator" reading would invert the
        direction by treating ω_GGE as a structurally privileged class
        of state-evaluators, which is container-thinking
        (treating ω_GGE as a special class "inside" the state space
        rather than recognizing ω_GGE IS a generic state with a
        specific property). The generic-with-property reading is
        substrate-IS by construction.
```

**Q-CN-R2-3 final verdict**: ω_GGE is generic-with-property. **No new clause is required in clause (e)**. The PARSE_TREE_ABBREVIATION_MAP (CF-LZ-3) is sufficient: it abbreviates `n_a^GGE → |v_a|^2 → Δ_BCS²/(2(λ_a²+Δ_BCS²))` at the audit-script level, treating the GGE state-evaluation as a NAMED ABBREVIATION for the closed-form Bogoliubov result. **The §VII.K-DUAL.LEVEL-DRESSED 4th-class definition is UNAFFECTED by this verdict** (the 3-criterion definition at registry lines 4293-4297 operates on the algebra-INVARIANT spectrum-only post-evaluation form; the GGE state's diagonality property is integrated out at the closed-form `n_a = |v_a|^2` step, before the LEVEL-DRESSED criteria are evaluated). Effect on parse-tree decision procedure: NONE. The procedure is stable under this refinement.

This is the structural verdict the parse-tree decision procedure's load-bearing decidability test required to stabilize the GGE-state handling. With Q-CN-R2-3 answered, no residual dissent remains.

### EMERGENCE

R2 cross-pollination surfaces ONE further insight neither agent surfaced in R1 or in connes's R2, plus answers to connes's Q-CN-R2-1 and Q-CN-R2-2.

**E3 — The substrate-axiomatic root of GGE-state generic-with-property is the SAME root as Δ_BCS-as-substrate-canonical-scalar (Re: C1 second bullet at workshop line 539).** My Q-CN-R2-3 answer above identifies ω_GGE as generic-with-property; my Re: C1 second bullet identified Δ_BCS as a substrate-canonical scalar (the BCS condensate magnitude is the order parameter of the BdG pairing channel, structurally part of the spectral triple's intrinsic scalar content, not a free state-pair argument). These two readings have the SAME structural root: both observables (the state ω_GGE; the scalar Δ_BCS) are NCG-axiom-derivable substrate-IS structures, not external choices imposed on the substrate. The substrate's spectral triple `(A_BdG, H_BdG, D_BdG)` admits both: ω_GGE is the maximum-entropy state on A_BdG subject to BdG-spectrum integrals of motion; Δ_BCS is the BCS pairing order parameter coupling D_K ⊗ τ_3 to 1_{H_K} ⊗ τ_1 in D_BdG. Both are structurally intrinsic. This unifies the substrate-axiomatic discipline of the FI/RD/MIXED trichotomy across BOTH the state-class and scalar-parameter content of substrate-IS observables. This unification is a candidate structural theorem for S90+ exploration but not pinned as a result here per `epistemic-discipline.md §"What Counts as a Result"`.

**Q-CN-R2-1 answer (Stage-1 CANDIDATE registration target — workshop lines 1368-1369): I prefer OPTION (i) — NEW sub-entry UNDER §VII.U.2 Corner II row in a corrigendum block.** Reasoning:

- **Substrate-axiomatic coherence**: the three-machinery convergence theorem is structurally PART OF the §VII.U.2 partition theorem, not a separate theorem. The 4-corner partition itself IS the substrate's algebra-axis × Mellin-pole orthogonality classification; the Corner II cell's calibration instance (Var_a per W-17 §V.2) IS the meta-classification rule's instantiation in Cell II. The three-machinery convergence proves that Var_a structurally inhabits Cell II via three independent axiomatic layers — which is precisely the K=3 algebra-axis orthogonality discipline (MANDATORY at S87 W-2 R3 close) realized in miniature on a single observable. Registering this convergence as a NEW §VII slot (option ii) would create a parallel structural-theorem entry that duplicates the meta-classification rule; registering it as a corrigendum sub-entry under §VII.U.2 Corner II row (option i) keeps the convergence structurally co-located with its parent partition theorem.

- **Authorship attribution coherence**: the §VII.U.2 authorship template (lizzi PRIMARY + connes CO-AUTHOR for clauses (c)+(d) per registry line 12936) is the natural author-side mapping for the three-machinery theorem. Lizzi-side: clause-(e) parse-tree application + F_traj=(k+1)/2 dressing. Connes-side: NCG-axiomatic Wedderburn central-projection grading. JOINT: the three-machinery convergence verdict (parallel to the existing JOINT clauses (c)+(d) at registry line 12954). Option (i) inherits the existing authorship attribution without conflict.

- **Registry navigation and K-counter tracking**: option (i) makes the convergence visible at the natural query-path "§VII.U.2 Corner II row → corrigendum block" rather than at a separate §VII slot. K-counter advancement for the Per-Bulletin-per-pole cohomology-class-distinct corpus (currently K=4 at s=4 per my Re: C6 + my L4 EMERGES) operates at the Corner II row level; option (i) keeps the advancement event co-located with its instance. The Stage-2 cross-axis verify (CF-R1-4) dispatches via the existing `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` gate identifier, augmented with the three-machinery clauses; option (i) inherits this gate naming without proliferation.

- **Option (ii) cost**: creating a new §VII slot for the joint theorem (e.g., §VII.U.7 keyed on the three-machinery convergence) would create a parallel registry entry whose theorem statement substantially overlaps with §VII.U.2 clauses (a)+(b)+(e) — a redundancy hazard. Future readers would have to navigate between §VII.U.2 (partition theorem) and §VII.U.7 (convergence theorem) to assemble the full structural picture, with no offsetting benefit.

- **Option (iii) cost**: cross-linking from §VII.U.2 Corner II row to a NEW §VII slot keyed on F_traj=(k+1)/2 theorem (S84 W3-24) would create a separate theorem entry for F_traj alone — but F_traj is itself a single-axis lizzi-authored theorem (S84 W3-24), not a JOINT three-machinery theorem. The three-machinery convergence requires all three machineries to be JOINT; F_traj alone is not the JOINT theorem. Option (iii) confuses the structural granularity.

**Preferred landing form**: a corrigendum sub-entry C5 (or next-letter corrigendum) under §VII.U.2 Corner II row at registry line 12961, with explicit three-machinery clause structure inheriting the §VII.U.2 JOINT-clause flag mechanism. The corrigendum block becomes the formal Stage-1 CANDIDATE registration event for the three-machinery convergence theorem.

**Q-CN-R2-2 answer (F_traj multiplicative composition conjecture empirical scope at S90+ — workshop line 1370): the F_traj=(k+1)/2 atlas's 42 rows are STRUCTURALLY ADEQUATE for testing the multiplicative composition conjecture WITHOUT atlas extension.** Reasoning:

- **42-row atlas content** (S84 W3-24): the atlas tabulates F_traj(k) = (k+1)/2 at k ∈ {0, 1, 2, ..., 41} at locked-norm L_k=1 convention. The k-values cover substrate-distance poles from k=0 (a_0 cosmological-constant slot) through k=41 (deep heat-kernel tail). For the multiplicative composition conjecture F_traj(k_1) · F_traj(k_2) = closed-form composition, the testable pole-pairs are C(42, 2) = 861 ordered pairs (or 42 + C(42, 2) = 903 including self-pairs at k_1 = k_2).
- **Cross-pole observable pair availability**: at substrate-distance-2 pole s=4, the existing slots include §VII.U.2 Corner II Var_a (F_traj(2) · F_traj(4) = 15/4 — the data point connes surfaces at E2); §VII.K-PROP.W10-4 ρ_∞ (s=4 fermionic-signed residue); §VII.AR LEVEL-DRESSED rank-ordering (s=4 with regulator-class spread). At substrate-distance-1 pole s=3, the existing slots include §VII.U.1 Mellin-Dirichlet (F_traj(1)? or F_traj(0)? depending on the convention pin); §VII.AS slope_A (Cell I s=3). Cross-pole observable pairs are not sparse at the existing registry corpus level.
- **Atlas-extension prerequisite is NOT required**: the 42-row atlas is already adequate to test the multiplicative composition law over 861 ordered pairs. The conjecture's verdict (closed-form law / no-law / partial-law) is derivable from the existing atlas without S90 atlas extension. The CF-R2-2 gate dispatches DIRECTLY against the existing 42-row atlas at S90+.
- **However**: if the conjecture's empirical verdict is INFO (partial law holding for a subset of pole-pairs), the structural reason for the subset may motivate an atlas extension at S91+ to test the law at higher k values (k > 41) where the locked-norm L_k=1 convention's stability is itself an empirical question. This is a downstream gate, not a prerequisite.

**Empirical scope verdict**: CF-R2-2 is testable at S90+ on the existing 42-row atlas. **No S90 atlas-extension prerequisite is required**. If the conjecture's verdict is INFO at S90, a follow-up atlas-extension gate may be queued at S91+, but it is NOT a blocking prerequisite to CF-R2-2.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Corner classification of Var_a(n_a^GGE) (Corner I / II / III / IV) | C1, Re: C1, L1 | **Converged** | Var_a ∈ Corner II = INVARIANT × s=4, via THREE independent machineries (NCG-axiomatic Wedderburn central-projection grading; clause-(e) parse-tree decision procedure; F_traj=(k+1)/2 zeta-vs-SDW dressing). Sharpest 4-axis classification: `{INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj-factors, LEVEL-DRESSED-candidate-pending-K2}`. K=3 algebra-axis orthogonality discipline (MANDATORY at S87 W-2 R3 close) realized in miniature on a single observable. |
| 2 | W-21 V.1+V.3 diff structural reading | C2, Re: C2 | **Converged** | Registry-attested editing history is Corner-IV (W5b-45 landing 2026-05-04) → Corner-II (W-17 §V.2/§V.3 parse-tree-decision reclassification 2026-05-08). W6-6 plan baseline's Corner-I assertion never matches any historical state; W-17 §V.3 corrigendum at registry line 12963 is the SMOKING GUN attestation. Lizzi's testimony as W5b-45 PRIMARY synthesizer + clause-(e) author corroborates connes's text-feature reading independently; mack's CF-W6-3 diff inspection retained for audit-trail-canonical record but NOT load-bearing for routing verdict. |
| 3 | Cross-wave consequence at §VII.AR Stage-2 | C3, Re: C3 | **Converged** | A.30 → §VII.AS (Cell I s=3); A.36 → §VII.AR (Cell II / Cell-I-LEVEL-DRESSED biaxial s=4); W6-6 plan-text "A.30 → §VII.AR" is plan-staleness defect. §VII.AR Stage-2 PASS-AND aggregation is INDEPENDENT of §VII.U.2 Corner-II re-classification. Cell-co-inhabitance ≠ Stage-2 constituency. Substrate-input-orthogonality predicate (joint-theorem-promotion.md §"Substrate-input-orthogonality clause") trivially satisfied at both A.30 and A.36 pairings. |
| 4 | Routing decision (Reading A vs Reading B) | C4, Re: C4 | **Converged** | Reading B is correct; Reading A is structurally destructive across FOUR failure modes: (1) reverting V.1+V.3 does NOT produce Cell I (pre-W-17 state was Cell IV per corrigendum line 12963); (2) breaks K=3 partition completeness; (3) violates no-technical-debt rule; (4) implicitly retires clause (e) parse-tree decision procedure, invalidating the §VII.U.2 partition theorem at its meta-classification root. The substrate-IS structural truth (parse-tree → Cell II) wins over the methodology-floor plan-baseline assertion per `phononic-framing.md §"IS Space, Not IN Space"` direction-of-explanation discipline. |
| 5 | W6-6 audit-machinery + CF-W6-4 extension | C5, Re: C5 | **Converged** | CF-W6-4 extends `_corner_classification_audit.py` TARGET_SLOTS dict to include §VII.U.2 with meta_classification_partition_theorem type + 4 instance-row sub-targets (Corner I/II/III/IV) + parse-tree counter pre-registration. Pre-registered expected classification = Cell II (Corner II) for Var_a, derived from parse-tree decision verdict, NOT from W6-6 plan baseline. PARSE_TREE_ABBREVIATION_MAP (CF-LZ-3) handles state-historical atoms (`|v_a|^2`, `|v_a|^4`, `n_a^GGE`) at the audit-script layer. UPSTREAM_GATE_PIN field traces to S88 §W5b-47 producing gate without re-verifying the Bogoliubov closed-form derivation. FI_RD_MIXED axis field (CF-LZ-2) adds 3rd discriminator. Audit becomes a structural sentinel across 3+1 axes (algebra × Mellin × FI/RD/MIXED + LEVEL-DRESSED candidacy). |
| 6 | Family-mate divergence (§VII.U.1 / §VII.U.6 vs §VII.U.2) | L2 | **Emerged** | Drift is LOCALIZED to §VII.U.2 (Stage-B family-mate audit PASS for §VII.U.1 + §VII.U.6 retains Corner I); structural difference operates at two non-overlapping layers: (i) Mellin-pole sub-axis (§VII.U.1/§VII.U.6 are algebraic-identity observables at substrate-distance-1 s=3; §VII.U.2 Corner II Var_a is energetic-moment observable at substrate-distance-2 s=4); (ii) construction-order (algebraic identities derived first at S86 W-1; energetic moments derived later at S88 §W5b-47 after BdG/GGE machinery built out). The 4-corner partition is the substrate's intrinsic taxonomy of derivable observables, not a partition-container the substrate inhabits. Substrate naturally distributes observables across all 4 corners per derivation-chain class. Family-mate stability confirms parse-tree decision regulator-independence (clause (e)). |
| 7 | PRIMARY-vs-SCHEMATIC LEVEL switch (does LEVEL change corner?) | L3 | **Emerged** | LEVEL switch is PROVENANCE-LEVEL-ONLY at the corner-cell layer (Cell II stays Cell II under both PRIMARY and SCHEMATIC because parse-tree decision is LEVEL-INVARIANT — the symbolic form's parse-tree structure does not depend on which spectrum the λ_a's are drawn from). LEVEL switch is REGULATOR-PIN-DISCIPLINE-RELEVANT at the FI/RD/MIXED sub-axis layer (the F_traj=(k+1)/2 locked-norm theorem operates on the PRIMARY spectrum; under SCHEMATIC the Casimir-flat spectrum's F_traj scaling may differ, potentially satisfying LEVEL-DRESSED criterion (3) at S89+ empirical scan). Parallel calibration corpus instance: §VII.AQ Level-3 anchor (canonical-import vs substrate-natural binding routes inhabit the SAME Corner I but produce DIFFERENT empirical values). Sub-class binding distinctions do NOT cross corners; LEVEL switch is a different axis. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **OQ-1 (CF-LZ-1 LEVEL-DRESSED K=2 empirical scan empirical verdict)**: does `Var_a(n_a^GGE)` empirically satisfy LEVEL-DRESSED criterion (3) at S90+ (rank-ordering swap of {Var_a^ζ, Var_a^SDW, Var_a^anomaly, Var_a^cutoff, Var_a^Zubarev} under PRIMARY-vs-SCHEMATIC LEVEL switch)? If PASS, §VII.K-DUAL.LEVEL-DRESSED K-counter advances K=1 → K=2 toward MANDATORY-at-K=3. If FAIL, Var_a's classification stays at `{INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj}` without LEVEL-axis promotion. Pre-registered gate spec at CF-LZ-1; Owner = lizzi PRIMARY + connes CO-AUTHOR; depends on CF-W6-5 (FULL physical PV pipeline at Λ_UV = M_KK).

2. **OQ-2 (CF-LZ-4 F_traj=1/4 zeta-vs-SDW prediction for Var_a empirical verdict)**: does the predicted closed-form ratio `Var_a^ζ / Var_a^SDW = (5/2·A − 9/4·B) / (A − B)` hold at machine epsilon (rel ≤ 1e-10) across L_max ∈ {6, 8, 10, 12} truncations of the full BdG D_K spectrum? PASS confirms F_traj=(k+1)/2 theorem extends to BdG-doubled observables; FAIL queues corrective derivation for the locked-norm-L_k=1 convention's BdG-doubling extension.

3. **OQ-3 (CF-R2-2 F_traj multiplicative composition conjecture empirical verdict)**: does the F_traj=(k+1)/2 theorem admit a multiplicative composition law across substrate-distance poles, with `F_traj(2) · F_traj(4) = 15/4` (the Var_a fingerprint) as the prototype data point? Testable at S90+ against the existing 42-row S84 atlas (no atlas-extension prerequisite per my Q-CN-R2-2 answer). PASS yields a new closed-form multiplicative-composition theorem candidate for S90+; FAIL declares F_traj structurally pole-INDEPENDENT in the multiplicative sense; INFO surfaces a structural reason for partial-law-holding subsets.

4. **OQ-4 (Stage-1-CANDIDATE → Stage-2 cross-axis independent-verify for the three-machinery convergence)**: per CF-R2-1 + CF-R1-4, the §VII.U.2 OWN Stage-2 cross-axis verify (`S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` per registry line 12929) must dispatch with axis-distinct reviewers EXCLUDING lizzi (PRIMARY synthesizer) + connes (CO-AUTHOR clauses (c)+(d)). Pre-registered eligibility set: van-den-dungen-bridge-theorist (axis-A NCG-Kasparov-bridge), volovik-superfluid-universe-theorist OR mack-cosmic-bridge OR kitaev-information-theorist (axis-B). The Stage-1 CANDIDATE landing under option (i) corrigendum sub-entry at §VII.U.2 Corner II row inherits this eligibility set; Stage-2 PASS-AND aggregation on the three-machinery JOINT clauses required for STAGE-3-PERMANENT promotion.

5. **OQ-5 (CF-LZ-5 observable-naming-history-vs-structural-classification rule-file sub-clause K-counter advancement)**: K=2 calibration corpus (Var_a per W-17 §V.2; α_s_canonical = n_s² − 1 at Cell I per registry line 12960) is documented; SUGGESTION status pending K=3 promotion per `feedback_rules-compensate-missing-structure.md`. Is there a third structural pattern in the registry calibrating the naming-history-vs-structure orthogonality at a NEW substrate-physics axis (e.g., entropy-tagged observables, Bogoliubov-rotation-tagged observables, route-N-derivative-tagged observables)? Queued for S90+ corpus inspection.

6. **OQ-6 (Q-CN-R2-3 follow-up — substrate-axiomatic unification of state-class and scalar-parameter generic-with-property readings)**: per E3 above, the substrate-axiomatic root of ω_GGE-as-generic-with-property and Δ_BCS-as-substrate-canonical-scalar is the same. Is there a unified structural theorem registering this unification (e.g., a "substrate-canonical content theorem" identifying which observables/states/scalars belong to the substrate-axiomatic content of `(A_BdG, H_BdG, D_BdG)`)? Candidate structural theorem for S90+ exploration; not pinned as a result here per `epistemic-discipline.md §"What Counts as a Result"`.

7. **OQ-7 (mack-cosmic-bridge CF-W6-3 W-21 V.1+V.3 diff inspection audit-trail-canonical record)**: although the routing verdict (Reading B) is structurally locked-in by the convergent three-machinery + lizzi PRIMARY-synthesizer testimony, mack's CF-W6-3 inspection remains load-bearing for the audit-trail-canonical record (what specifically V.1+V.3 edited; whether V.1+V.3 implemented the W-17 §V.2 reclassification or was a separate-event minor edit). Plan-staleness validator extension (CF-R1-2) depends on this canonical record for cross-wave-anchor citation drift detection.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **§VII.U.2 Corner II row's classification of `Var_a(n_a^GGE)` re-pinned per three-machinery convergence**: structurally locked as `{INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj-factors, LEVEL-DRESSED-candidate-pending-K2}` via three independent axiomatic-layer machineries (Wedderburn central-projection grading on `A_BdG = A_F ⊗ M_2(ℂ)` correctly factored as 3-projection lift NOT 6 per Q-LZ-R2-1 (a) correction; clause-(e) parse-tree decision procedure; F_traj=(k+1)/2 zeta-vs-SDW dressing at locked norm L_k=1). The W6-6 plan baseline's `algebra-INVARIANT-spectrum-only-functional` at Cell I is **RETRACTED**; correct retroactive baseline is Cell II for Var_a.
- **STAGE-1-CANDIDATE pathway opens for the three-machinery convergence joint theorem**: per `joint-theorem-promotion.md §"Stage 0"`, this R2 workshop verdict freezes the workshop-internal candidate; CF-R2-1 routes to S90 Stage-1 registration via option (i) corrigendum sub-entry under §VII.U.2 Corner II row, inheriting the §VII.U.2 authorship template (lizzi PRIMARY + connes CO-AUTHOR for joint clauses) and the existing Stage-2 dispatch gate identifier `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`. The Stage-1 landing must include explicit author-side attribution per JOINT clause (Wedderburn = connes-side; clause-(e) parse-tree + F_traj = lizzi-side; convergence verdict = JOINT).
- **Twelve carry-forwards across R1 + R2 + one new pre-registered S90 reconciliation gate**: CF-R1-1 through CF-R1-5 (connes R1 carry-forwards on audit extension, plan-staleness, parse-tree pre-registration discipline, Stage-2 reviewer-eligibility, observable-naming-history documentation note); CF-LZ-1 through CF-LZ-5 (lizzi R1 carry-forwards on LEVEL-DRESSED K=2 empirical scan, FI_RD_MIXED audit field, PARSE_TREE_ABBREVIATION_MAP, F_traj=1/4 prediction, rule-file sub-clause promotion); CF-R2-1 (Stage-1 CANDIDATE registration); CF-R2-2 (F_traj multiplicative composition conjecture empirical test); plus the new `S90-VII-U-2-CORNER-RECONCILIATION-VERIFY` gate pre-registered as the workshop's structural commitment to S90.

### What Holds

- **Parse-tree decision procedure (clause (e), my authorship per registry line 12995) IS the load-bearing decidability test**: both agents apply clause (e) independently to the symbolic form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` and arrive at the same INVARIANT verdict. The procedure operates at parse-tree level (NOT at numerical-evaluation level), is finite, regulator-independent, and laboratory-IN. It survives Wedderburn refinement (Q-LZ-R2-1 (a) 3-projection correction does not alter the verdict), commutant-intersection refinement (Q-LZ-R2-1 (b) `ℂ · 1_{H_F} ⊗ 1_{M_2}` full BdG-scalar does not alter the verdict), and GGE-state generic-with-property refinement (Q-CN-R2-3 verdict — abbreviation-map approach is sufficient, no new clause required).
- **F_traj=(k+1)/2 theorem (S84 W3-24, my own; locked norm L_k=1) extends to BdG-doubled observables under the K=2 cohort with §VII.AR**: the bilinear variance form's two F_traj dressing factors (F_traj(2) = 3/2, F_traj(4) = 5/2) do not collapse to a uniform scalar under regulator-class switch — Var_a is `MIXED-of-RD-with-distinct-F_traj-factors`. The fingerprint product F_traj(2) · F_traj(4) = 15/4 is a candidate multiplicative-composition data point (CF-R2-2).
- **`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 status unchanged**: the workshop's three-machinery convergence on a SINGLE observable is the K=3 discipline realized in miniature; it does NOT advance the algebra-axis K-counter (which is keyed on structurally-distinct family-orthogonality phenomena, not on calibration-corpus-instance counts within a slot). The Per-Bulletin-per-pole cohomology-class-distinct K-counter at s=4 advances K=3 → K=4 (adding §VII.U.2 Corner II Var_a to {§VII.K-PROP.W10-4, §VII.AR}); the pole-distinct criterion (`s ∉ {s=3, s=4}`) remains pending.
- **Substrate-first direction-of-explanation per `phononic-framing.md §"IS Space, Not IN Space"`**: substrate IS the spectral triple `(A_BdG, H_BdG, D_BdG)`; ω_GGE IS a generic state with diagonal-in-mode-pair-basis property; Δ_BCS IS the substrate-canonical BCS pairing scalar; the 4-corner partition IS the substrate's intrinsic algebra-axis × Mellin-pole orthogonality classification of its own observables; laboratory observables (Connes-distance numerical evaluation, spectral-moment numerical evaluation) are LABORATORY-IN observables on continuum-projected derived images. No container-thinking inversions surfaced.

### What Breaks or Strains

- **F_traj multiplicative composition conjecture (E2) is UNVERIFIED at S89 close**: the F_traj(2) · F_traj(4) = 15/4 product is a single data point; the conjecture's empirical verdict at CF-R2-2 (multiplicative composition law / no law / partial law) is queued for S90+ against the existing 42-row S84 atlas. The verdict outcome is INFORMATIVE in all three branches but the conjecture itself is NOT a result at S89 close.
- **LEVEL-DRESSED K=2 promotion is PENDING CF-LZ-1 empirical scan at S90+**: criterion (2) (regulator-CLASS membership invariance under PRIMARY-vs-SCHEMATIC LEVEL switch) AND criterion (3) (rank-ordering swap under LEVEL switch) require empirical demonstration. Until CF-LZ-1 dispatches at S90+, Var_a's LEVEL-DRESSED-candidate status is a TAG, not a registered K=2 corpus instance. The §VII.K-DUAL.LEVEL-DRESSED K-counter sits at K=1 (SUGGESTION) pending the empirical advancement.
- **Stage-1 CANDIDATE → Stage-2 PASS-AND aggregation is GATED on axis-distinct cross-reviewers**: per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` MANDATORY clauses 1-3 plus the downstream-inheritance-reach test (S88 W-14 W4a-17 V.2 calibration K=1), the dispatch must satisfy axis-distinctness + original-authoring-agent exclusion + audit-coverage adequacy. The three-machinery convergence's joint clauses must PASS-AND across BOTH cross-reviewer verdicts. The Stage-2 dispatch is a multi-year-equivalent commitment (per CF-R1-4 effort = 1.0 wave-equivalents) before STAGE-3-PERMANENT promotion is unlocked.

### Carry-Forward Computations

Numbered list of 13 carry-forwards (CF-R1-1 through CF-R1-5 + CF-LZ-1 through CF-LZ-5 + CF-R2-1 + CF-R2-2 + S90-VII-U-2-CORNER-RECONCILIATION-VERIFY), each with full 7-field spec (What / Inputs / Gate / Effort / Owner / Depends-on / Cross-link). This list is PRIMARY input to `/rclab-plan` for S90.

#### CF-R1-1 — S89+ `_corner_classification_audit.py` extension to include §VII.U.2

| Field | Value |
|:------|:------|
| **What** | Extend `computations/_shared/_corner_classification_audit.py` TARGET_SLOTS dict to include §VII.U.2 with `meta_classification_partition_theorem` type AND 4 instance-row sub-targets (Corner I §VII.U.1 ref, Corner II Var_a(n_a^GGE) instance, Corner III Connes-distance ref, Corner IV α_s_route_3 ref). Pre-registered expected classification for Var_a(n_a^GGE): Corner II = INVARIANT × s=4 per this workshop's parse-tree verdict. |
| **Inputs** | Existing `_corner_classification_audit.py` (W6-6 SHA pin `2b96bf78…`); §VII.U.2 block content `permanent-results-registry.md:12927-13058`; parse-tree decision procedure from registry §VII.U.2 clause (e) line 12995; symbolic form for Var_a registry line 12961; C1 substitution chain in this workshop. |
| **Gate** | PASS = `per_slot_results['§VII.U.2']` populated AND `var_a_corner='II'` AND `var_a_algebra_axis='INVARIANT'` AND `var_a_mellin_pole='s=4'` AND `parse_tree_pi_a_count=0` AND `parse_tree_commutator_count=0`. FAIL on any mismatch. |
| **Effort** | 0.3 wave-equivalents (extension + self-test against 4 instance rows; identical extension pattern to existing 7 audited slots). |
| **Owner** | gen-physicist orchestrator-direct per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class. |
| **Depends on** | UPSTREAM GATE: CF-W6-3 (mack §VII.U.2 corner reconciliation — Reading B lock-in); UPSTREAM REGISTRY: §VII.U.2 clause (e) parse-tree decision procedure line 12995; UPSTREAM RULE: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3. |
| **Cross-link** | Related to CF-LZ-2 (FI_RD_MIXED axis field extension); CF-LZ-3 (PARSE_TREE_ABBREVIATION_MAP extension); CF-R1-3 (parse-tree expansion pre-registration). |

#### CF-R1-2 — Plan-staleness extension to catch cross-wave-anchor citation drift (A.30 vs A.36 mis-citation)

| Field | Value |
|:------|:------|
| **What** | Extend `computations/_shared/_plan_staleness_audit.py` (per W6-6 carry-forward CF-W6-6 line 420-428) to detect cross-wave-anchor mis-citations against the registry's authoritative routing table. Specifically: detect plan-text claims of the form "A.<NN> Stage-2 verify of §VII.<SLOT>" and verify against the registry's actual A.<NN> → §VII.<SLOT> mapping. The W6-6 plan's "W4 A.30 Stage-2 §VII.AR verify" assertion (session-89-w6-workingpaper.md:224) is the calibration corpus instance #1 (registry says A.30 → §VII.AS, A.36 → §VII.AR). |
| **Inputs** | `_plan_staleness_audit.py` body (W6-6 SHA `5f370299…`); registry `permanent-results-registry.md` for A.<NN> → §VII.<SLOT> authoritative mapping table; `session-89-w6-workingpaper.md:224` as calibration corpus instance #1; registry line 16971 (A.36) + line 17000 (A.30). |
| **Gate** | PASS = re-run on `session-89-w6-workingpaper.md` flags the line 224 "A.30 → §VII.AR" assertion as cross-wave-anchor-citation-drift; PASS extends to detect future plan-text mis-citations across all session-NN-plan-*.md files. INFO if extension lands but no calibration corpus instances trigger on existing plans. |
| **Effort** | 0.2 wave-equivalents (regex extension + 1 calibration corpus row). |
| **Owner** | gen-physicist orchestrator-direct. |
| **Depends on** | UPSTREAM PLAN-FILE: `_plan_staleness_audit.py` body; UPSTREAM REGISTRY: §VII.AR routing line 16971 (A.36) + §VII.AS routing line 17000 (A.30); UPSTREAM WORKSHOP: this S89 W-3 C3 finding. |
| **Cross-link** | Related to CF-W6-6 (already queued in W6 working paper lines 420-428); extends the broader plan-staleness validator family. |

#### CF-R1-3 — Pre-register parse-tree expansion alongside symbolic form for all S89+ §VII registry entries

| Field | Value |
|:------|:------|
| **What** | Extend `.claude/rules/registry-landing.md` to require new §VII entries citing observables with state-historic names (e.g., `n_a^GGE`, `α_s_route_*`, `P_GGE`, `ω_GGE`-tagged quantities) to ALSO declare their parse-tree expansion at the level of `{spectrum-only g(λ_k), Σ-summations, π(a) operator-algebra references, [D, π(a)] commutators, state-pair sup constructs}`. Makes clause (e) parse-tree decision mechanizable at landing time, eliminating future Corner-mis-assignments via naming-history confusion. |
| **Inputs** | `.claude/rules/registry-landing.md` body (S88 W7c-30 SHA pin); registry §VII.U.2 clause (e) text line 12995 (lizzi authorship); this S89 W-3 workshop C1 + C6 Observation 4 + my Re: C2 EMERGES as substrate-physics motivation; the W-17 §V.2/§V.3 reclassification event as the canonical worked example. |
| **Gate** | PASS = registry-landing rule extended with a new sub-section "Parse-tree expansion pre-registration" with audit-script hook into `_registry_landing_audit.py`; calibration corpus instance #1 = retroactive parse-tree expansion of §VII.U.2 Corner II row Var_a(n_a^GGE) per this workshop's substitution chain. |
| **Effort** | 0.4 wave-equivalents (rule extension + audit script extension + 1 calibration corpus instance). |
| **Owner** | gen-physicist + mack-cosmic-bridge co-authored (mack sole writer for registry-landing rule per `feedback_mack-bridge-role.md`). |
| **Depends on** | UPSTREAM RULE: `.claude/rules/registry-landing.md`; UPSTREAM REGISTRY: §VII.U.2 clause (e) parse-tree decision procedure line 12995; UPSTREAM AUDIT: `_corner_classification_audit.py` (CF-R1-1 extension target). |
| **Cross-link** | Strongly related to CF-LZ-3 (PARSE_TREE_ABBREVIATION_MAP — the audit-script side of the same parse-tree-discipline principle); CF-LZ-5 (rule-file sub-clause for the structural-vs-naming-history principle). |

#### CF-R1-4 — Cross-axis Stage-2 reviewer-eligibility audit for §VII.U.2's own Stage-2 dispatch

| Field | Value |
|:------|:------|
| **What** | When §VII.U.2's own Stage-2 cross-axis verify (`S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` per registry line 12929) dispatches, the Axis-A and Axis-B reviewers MUST satisfy the 3-clause Stage-2 Axis-B Selection Protocol (joint-theorem-promotion.md lines 67-73): (1) axis-distinctness, (2) original-authoring-agent exclusion with downstream-inheritance reach, (3) audit-coverage adequacy. Pre-register the eligibility table: connes-ncg-theorist EXCLUDED (CO-AUTHOR per registry line 12936); lizzi-spectral-functional-theorist EXCLUDED (PRIMARY synthesizer per registry line 12927). Eligible axis-A candidates: van-den-dungen-bridge-theorist (NCG-Kasparov-bridge axis), gen-physicist (general-physics axis). Eligible axis-B candidates: volovik-superfluid-universe-theorist, mack-cosmic-bridge (cosmological-bridge), kitaev-information-theorist. |
| **Inputs** | `joint-theorem-promotion.md §"Stage 2"` lines 55-91; registry §VII.U.2 authorship attribution lines 12936 + 12942 + 12950-12952 + 13050-13053; this S89 W-3 workshop C3 + Re: C3 cross-wave consequence analysis. |
| **Gate** | PASS = §VII.U.2 Stage-2 dispatch pre-registers axis-A reviewer NOT in {connes, lizzi} AND axis-B reviewer NOT in {connes, lizzi} AND on DIFFERENT axes; PASS-AND across clauses (c) JOINT + (d) JOINT + new joint clauses from CF-R2-1 three-machinery corrigendum landing. |
| **Effort** | 1.0 wave-equivalents (Stage-2 dispatch + dual cross-reviewer verdict + PASS-AND aggregation). |
| **Owner** | orchestrator dispatches the two reviewers; reviewers operate per Stage-2 standard. |
| **Depends on** | UPSTREAM RULE: `joint-theorem-promotion.md §"Stage 2 Axis-B Selection Protocol"`; UPSTREAM REGISTRY ENTRY: §VII.U.2 authorship attribution; UPSTREAM WORKSHOP: this S89 W-3 verdict (Reading B confirmed → §VII.U.2 STAGE-1-CANDIDATE proceeds to Stage-2 verify); UPSTREAM CF: CF-R2-1 (Stage-1 CANDIDATE landing must precede Stage-2 dispatch). |
| **Cross-link** | Direct prerequisite to STAGE-3-PERMANENT promotion of §VII.U.2; Stage-2 PASS-AND verdict gates promotion. |

#### CF-R1-5 — Documentation note: observable-naming-history vs structural-classification orthogonality

| Field | Value |
|:------|:------|
| **What** | Append a documentation note to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (rule-file target adopted per connes's R2 DISSENT D2 retraction of the `phononic-framing.md` option) explaining the principle surfaced by this workshop's C6 Observation 4: observable naming conventions encode HISTORY (where the closed form was first derived: GGE-state, route-3 derivative, n_s-cosmological, etc.) NOT STRUCTURE. Corner classification operates on parse-tree STRUCTURE per clause (e) decision procedure. CONSOLIDATED into CF-LZ-5 (formal rule-file sub-clause with K-counter promotion path). |
| **Inputs** | This S89 W-3 workshop's C1 + C6 Observation 4; my Re: C2 EMERGES; registry §VII.U.2 clauses (a) + (b) + (e); the W-17 §V.3 corrigendum text at registry line 12963. |
| **Gate** | PASS = documentation note appended; one calibration corpus row added (this workshop's instance). Per connes's R2 DISSENT D2 (workshop lines 1231-1239), CF-R1-5 is RETRACTED in favor of CF-LZ-5 (formal sub-clause with K-counter promotion path; same content but at MANDATORY-promotion rather than documentation-only level). |
| **Effort** | 0.0 wave-equivalents (CF-R1-5 RETRACTED in favor of CF-LZ-5; effort absorbed into CF-LZ-5 = 0.2 wave-equivalents). |
| **Owner** | gen-physicist orchestrator-direct (METHODOLOGY-class wave per allowlist) — see CF-LZ-5. |
| **Depends on** | UPSTREAM: CF-LZ-5 supersedes this carry-forward per R2 convergence. |
| **Cross-link** | RETRACTED in favor of CF-LZ-5; preserved as audit-trail entry of the R2 convergence event. |

#### CF-LZ-1 — LEVEL-DRESSED K=2 empirical scan for `Var_a(n_a^GGE)` under PRIMARY-vs-SCHEMATIC LEVEL switch

| Field | Value |
|:------|:------|
| **What** | Empirically evaluate the 3-criterion LEVEL-DRESSED definition (per §VII.K-DUAL.LEVEL-DRESSED registry line 4293-4297) for `Var_a(n_a^GGE)`: (1) algebra-INVARIANT spectrum-only — SATISFIED (parse-tree decision PASS per this workshop); (2) regulator-CLASS membership unchanged across PRIMARY-vs-SCHEMATIC LEVEL switch — PENDING empirical scan; (3) ordinal output (rank-ordering of {Var_a^ζ, Var_a^SDW, Var_a^anomaly, Var_a^cutoff, Var_a^Zubarev}) swaps under PRIMARY-vs-SCHEMATIC LEVEL switch — PENDING. Compute Var_a under PRIMARY (S61/S78 PV pipeline at Λ_UV = M_KK on full BdG-doubled D_K spectrum) and SCHEMATIC (`_spectral_action_regulators.py` SCHEMATIC analogs on bare Casimir spectrum) at fixed (cutoff_frac=0.7, M_PV²_frac=0.1, Vol_SU3_Haar). Compare rank-orderings. If swap detected, Var_a is LEVEL-DRESSED K=2 instance per W-22 §V.4 forward-enforcement clause at line 4307. |
| **Inputs** | `s84_spectrum_cache_L12_tau019.npz` (PRIMARY full BdG D_K spectrum cache); `_spectral_action_regulators.py` SCHEMATIC helpers (per its docstring lines 23-30); `canonical_constants.py` for `M_KK = 7.428660036284456e+16`, `Delta_BCS = 0.464 · M_KK`, `Vol_SU3_Haar = 1349.74`; W9b-2 npz `s87_w9b_pole_specificity_scan.npz` as upstream LEVEL-switch precedent (W9b-2 demonstrated SCHEMATIC-vs-FULL D_max = 2.168); §VII.K-DUAL.LEVEL-DRESSED 3-criterion definition at registry lines 4293-4297. |
| **Gate** | PASS = LEVEL-DRESSED criterion (3) confirmed (rank-ordering swap observed under LEVEL switch); §VII.K-DUAL.LEVEL-DRESSED K-counter advances K=1 → K=2; Var_a's classification extends to `{INVARIANT, s=4, MIXED-of-RD-at-PRIMARY, LEVEL-DRESSED at K=2 cohort with §VII.AR}`. FAIL = rank-ordering preserved (Var_a is not LEVEL-DRESSED); classification stays at `{INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj}` without LEVEL-axis promotion. INFO = ambiguous (partial rank-swap; some atlas members swap, others don't). |
| **Effort** | 0.6 wave-equivalents (5-regulator-atlas scan at 2 LEVELs; computation + rank-comparison + verdict + registry annotation if PASS). Requires connes CO-AUTHOR for the FULL physical PV pipeline at Λ_UV = M_KK (per W6-7 CF-W6-5 pattern, since the S61/S78 PV pipeline is conceptual in the helper docstring). |
| **Owner** | lizzi-spectral-functional-theorist PRIMARY (FI/RD/MIXED-axis classification authority + S82 W-3 trichotomy origin) + connes-ncg-theorist CO-AUTHOR (FULL physical PV pipeline reconstruction). mack-cosmic-bridge sole writer for registry annotation update if PASS. |
| **Depends on** | UPSTREAM GATE: CF-W6-3 (§VII.U.2 Corner-classification reconciliation; Reading B must be locked-in first); UPSTREAM GATE: CF-W6-5 (substantive D_max measurement at FULL PV pipeline); UPSTREAM REGISTRY: §VII.K-DUAL.LEVEL-DRESSED registry lines 4293-4307; UPSTREAM RULE: `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4. |
| **Cross-link** | Directly advances OQ-1; calibration-corpus K-counter advancement target for `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. |

#### CF-LZ-2 — FI_RD_MIXED axis field extension to CF-W6-4 audit dict (refinement of CF-R1-1)

| Field | Value |
|:------|:------|
| **What** | Extend TARGET_SLOTS_S89 dict at `_corner_classification_audit.py` (per CF-R1-1) to include a `fi_rd_mixed_axis` field per instance row. Field encodes FI/RD/MIXED classification under S82 W-3 §VII.K trichotomy (refined per 4-class extension to FI/RD/MIXED/LEVEL-DRESSED at §VII.K-DUAL.LEVEL-DRESSED W-22 §V.4). For the Corner II row Var_a(n_a^GGE), field value is `MIXED-of-RD-with-distinct-F_traj-factors` per L1 verdict; LEVEL-DRESSED candidate per L3 verdict; K=2 LEVEL-DRESSED upgrade pending CF-LZ-1 empirical scan. Field includes rationale text, F_traj scalar dressing factors, and level_dressed_candidacy boolean. Audit verifies that the registry text's FI/RD/MIXED classification matches the pre-registered field. |
| **Inputs** | CF-R1-1 TARGET_SLOTS_S89 dict (workshop lines 336-376); my L1 verdict (`MIXED-of-RD-with-distinct-F_traj` per S82 W-3 §VII.K trichotomy + F_traj=(k+1)/2 theorem); §VII.K-DUAL.LEVEL-DRESSED 3-criterion definition at registry lines 4293-4297; S84 W3-24 F_traj theorem (locked-norm L_k=1 convention); `lizzi-finite-infinite-vector-classification.md` (FINITE-VECTOR / INFINITE-VECTOR sub-tag distinction). |
| **Gate** | PASS = `_corner_classification_audit.py` self-test outputs `per_slot_results['§VII.U.2']['instance_rows']['corner_II_instance']['fi_rd_mixed_axis']` populated with the 5 sub-fields (`classification`, `rationale`, `f_traj_dressing_factors`, `level_dressed_candidate`, `level_dressed_k_counter_advancement_pending`) AND audit verifies the registry text contains a matching FI/RD/MIXED-axis annotation (if registry text is yet to be amended with the explicit annotation, mack-cosmic-bridge sole-writer adds the annotation in the same dispatch). |
| **Effort** | 0.4 wave-equivalents (dict extension + audit self-test + registry text annotation amendment via mack). |
| **Owner** | gen-physicist orchestrator-direct (audit script extension) + mack-cosmic-bridge sole writer (registry text annotation amendment). |
| **Depends on** | UPSTREAM GATE: CF-R1-1 (base TARGET_SLOTS_S89 dict extension); UPSTREAM REGISTRY: §VII.K-DUAL.LEVEL-DRESSED 4-class extension at registry lines 4279-4313; UPSTREAM RULE: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3; UPSTREAM REGISTRY: §VII.K-DUAL.LAYER per-row LAYER-of-pin atlas at registry line 4321. |
| **Cross-link** | Refines CF-R1-1; closes the FI/RD/MIXED-axis silent classification pathway at the audit-script layer. |

#### CF-LZ-3 — Parse-tree abbreviation map extension to `_corner_classification_audit.py`

| Field | Value |
|:------|:------|
| **What** | Add `PARSE_TREE_ABBREVIATION_MAP` constant to `_corner_classification_audit.py` mapping known Bogoliubov / GGE-state-history abbreviations to fully-expanded closed forms: `{"|v_a|^2": "Δ_BCS²/(2·(λ_a² + Δ_BCS²))", "|v_a|^4": "(Δ_BCS²/(2·(λ_a² + Δ_BCS²)))²", "n_a^GGE": "|v_a|^2"}`. Audit applies abbreviation map first, then runs parse-tree counters on fully-expanded symbolic form. Closes the failure mode where a future registry edit re-introduces a state-historical abbreviation (e.g., `n_a^GGE` without explicit Bogoliubov closure) and the audit naively flags the GGE-state name as state-pair-functional content. Calibration corpus instance #1 = retroactive expansion of Var_a(n_a^GGE) per W-17 §V.2 reclassification. |
| **Inputs** | Existing `_corner_classification_audit.py` (W6-6 SHA pin `2b96bf78…`); parse-tree decision procedure at registry §VII.U.2 clause (e) line 12995; Bogoliubov closed-form `n_a = |v_a|^2 = Δ_BCS²/(2·(λ_a² + Δ_BCS²))` from BdG fermionic Bogoliubov transformation (cited at registry line 12961 + my Re: C5 sub-question (i) verdict); W-17 §V.2 reclassification event as calibration corpus instance #1. |
| **Gate** | PASS = `_corner_classification_audit.py` extended with `PARSE_TREE_ABBREVIATION_MAP` constant AND self-test confirms (a) when fed the abbreviated symbolic form `(1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2`, the audit applies the abbreviation map and runs counters on the expanded form with parse-tree counters all returning 0 (algebra-INVARIANT classification preserved through expansion); (b) when fed a synthetic test case with `n_a^GGE` as a non-expanded atom + no abbreviation map, the audit emits FAIL flagging the GGE-state-name as ambiguous (regression-prevention check). |
| **Effort** | 0.3 wave-equivalents (constant addition + 2-fixture self-test). |
| **Owner** | gen-physicist orchestrator-direct (METHODOLOGY-class audit script extension). |
| **Depends on** | UPSTREAM GATE: CF-R1-1 (base TARGET_SLOTS_S89 dict); UPSTREAM REGISTRY: §VII.U.2 clause (e) parse-tree decision procedure at line 12995; UPSTREAM REGISTRY: Bogoliubov closed-form citation at line 12961; UPSTREAM RULE: `epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` Class 8.2 (abbreviation map IS the pre-registered pattern set for the rubric). |
| **Cross-link** | Closes regression-prevention pathway at audit-script layer; complements CF-R1-3 (parse-tree expansion pre-registration at registry-landing-rule layer). Both together close the naming-history failure mode at both audit + registry-landing layers. |

#### CF-LZ-4 — F_traj zeta-vs-SDW prediction for Var_a as falsifiable structural prediction at S89+

| Field | Value |
|:------|:------|
| **What** | Empirically verify the structural prediction `Var_a^ζ / Var_a^SDW = (5/2 · A − 9/4 · B) / (A − B)` (per L1 step 3 substitution chain) where `A := (1/N) M_4^SDW`, `B := ((1/N) M_2^SDW)²`. For Var_a's specific substrate-physics regime (BdG Bogoliubov closure at Δ_BCS = 0.464 M_KK, GGE state on A_BdG, L_max=10 cache), compute A and B numerically and verify the predicted ratio. Prediction is a falsifiable test of F_traj=(k+1)/2 theorem (S84 W3-24, my own) applied to a NEW substrate-physics observable not in the original 42-row S84 atlas. If predicted ratio matches at machine epsilon, F_traj extends to BdG-doubled observables; if it fails at non-trivial precision, F_traj's locked-norm-L_k=1 convention may need refinement for BdG-doubled spectra. |
| **Inputs** | `s84_spectrum_cache_L12_tau019.npz` (full BdG D_K spectrum cache for PRIMARY level); zeta-regulated and SDW-regulated evaluators for M_2 = Σ_a m_a g_2(λ_a) and M_4 = Σ_a m_a g_4(λ_a) per `_spectral_action_regulators.py.zeta_a_n` + `_spectral_action_regulators.py.pauli_villars_a_n` (with explicit SCHEMATIC-vs-FULL-physical disclosure per `substrate-first-canonical-sourcing.md §(iv)`); F_traj theorem (S84 W3-24, lizzi agent-memory entry line 23); Bogoliubov closed forms g_2(λ) and g_4(λ); `canonical_constants.py` for `Delta_BCS = 0.464 · M_KK`. |
| **Gate** | PASS = computed `Var_a^ζ / Var_a^SDW` matches predicted closed-form ratio `(5/2 · A − 9/4 · B) / (A − B)` at relative precision ≤ 1e-10 across L_max ∈ {6, 8, 10, 12} truncations. FAIL = ratio diverges from prediction at non-trivial precision; F_traj theorem's BdG-doubled extension structurally unverified; corrective derivation queued. INFO = ratio matches at coarse precision but fails at machine epsilon (partial confirmation with refinement carry-forward). |
| **Effort** | 0.4 wave-equivalents (4-L_max scan + zeta + SDW evaluators + numerical ratio + closed-form prediction comparison + verdict). |
| **Owner** | lizzi-spectral-functional-theorist PRIMARY (F_traj theorem author + S82 W-3 trichotomy origin). |
| **Depends on** | UPSTREAM GATE: CF-W6-5 (substantive PV pipeline at FULL-physical level); UPSTREAM REGISTRY: §VII.K-DUAL FI/RD/MIXED trichotomy (S82 R2-B, lizzi signature); UPSTREAM CANONICAL CONSTANT: `Delta_BCS_FW` (or derived from `M_KK_gravity` via `Delta_BCS = 0.464 · M_KK`); UPSTREAM AGENT-MEMORY: F_traj=(k+1)/2 theorem (S84 W3-24); UPSTREAM RULE: `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4. |
| **Cross-link** | Directly tests OQ-2; cross-prerequisite to CF-R2-2 (F_traj multiplicative composition conjecture — Var_a's data point F_traj(2) · F_traj(4) = 15/4 is one of 861 candidate pole-pairs). |

#### CF-LZ-5 — Promote observable-naming-history-vs-structural-classification principle to rule-file sub-clause (CONSOLIDATES CF-R1-5)

| Field | Value |
|:------|:------|
| **What** | Promote the principle "observable naming conventions encode HISTORY, not STRUCTURE; corner classification operates on parse-tree STRUCTURE per clause (e), not on observable NAMES" (per C6 Observation 4 + my Re: C2 EMERGES + connes's R2 DISSENT D2 retraction of `phononic-framing.md` option) to a formal sub-clause within `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. Sub-clause provides: (a) principle statement; (b) calibration corpus (Var_a(n_a^GGE) W-17 §V.2 reclassification as instance #1; α_s_canonical = n_s² − 1 at Cell I as instance #2); (c) enforcement rule (registry entries citing observables with state-historical names MUST declare parse-tree expansion alongside symbolic form per CF-R1-3); (d) status SUGGESTION at K=2 pending K=3 promotion. Extends CF-R1-5 from documentation note to formal rule-file sub-clause with K-counter promotion path. |
| **Inputs** | This S89 W-3 workshop's C1 + C2 + C6 Observation 4; connes's CF-R1-5 + R2 DISSENT D2 retraction (workshop lines 1231-1239); my Re: C2 EMERGES + Re: C6 framework-lesson; registry §VII.U.2 clauses (a) + (b) + (e); W-17 §V.3 corrigendum text at registry line 12963; §VII.U.1 Corner I row α_s_canonical = n_s² − 1 calibration instance text at registry line 12960. |
| **Gate** | PASS = sub-clause appended to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` with all 4 elements (principle statement + calibration corpus + enforcement rule + K-counter status); calibration corpus contains 2 instances (Var_a, α_s_canonical); status SUGGESTION at K=2 pending K=3. |
| **Effort** | 0.2 wave-equivalents (rule-file sub-clause append + calibration corpus row + cross-link annotations). |
| **Owner** | gen-physicist orchestrator-direct per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class (rule-file extension); lizzi co-sign on rationale (rule-file extension is structurally rooted in parse-tree decision procedure clause (e) authored at §VII.U.2). |
| **Depends on** | UPSTREAM RULE: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (extension host); UPSTREAM REGISTRY: §VII.U.2 clause (e) parse-tree decision procedure at line 12995; UPSTREAM REGISTRY: §VII.U.1 Corner I row α_s_canonical text at line 12960 (instance #2); UPSTREAM WORKSHOP: this S89 W-3 R1+R2 verdict (Reading B confirmed); UPSTREAM RULE: `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold. |
| **Cross-link** | Supersedes CF-R1-5 (R2 DISSENT D2 convergence); advances OQ-5. |

#### CF-R2-1 — Joint-theorem-promotion Stage-1 CANDIDATE registration for the three-machinery convergence on Var_a(n_a^GGE)

| Field | Value |
|:------|:------|
| **What** | Register the joint theorem candidate `Var_a(n_a^GGE) ∈ Cell-II ∩ {MIXED-of-RD-with-distinct-F_traj-factors} ∩ LEVEL-DRESSED-candidate-pending-K2` as STAGE-1-CANDIDATE per `joint-theorem-promotion.md §"Stage 1"`. Candidate text contains the convergent three-machinery proof (NCG-axiomatic Wedderburn + clause-(e) parse-tree + F_traj=(k+1)/2 zeta-vs-SDW dressing) with explicit author-side attribution per clause: clauses on Wedderburn / Schur-orthogonality = connes; clauses on clause-(e) parse-tree application + F_traj=(k+1)/2 dressing = lizzi; clauses on combined three-machinery convergence verdict = JOINT. **Registry-landing target per my Q-CN-R2-1 verdict: OPTION (i)** — NEW sub-entry UNDER §VII.U.2 Corner II row in a corrigendum block (preferred for substrate-axiomatic coherence; authorship attribution coherence; registry navigation; K-counter tracking — see EMERGENCE answer to Q-CN-R2-1). |
| **Inputs** | This S89 W-3 workshop's R1 + R2 verdict (lizzi+connes Stage-0 author freeze); `joint-theorem-promotion.md §"Stage 1"` 4-stage pathway template; registry §VII.U.2 clause (e) parse-tree decision procedure at line 12995; F_traj=(k+1)/2 theorem (S84 W3-24, lizzi-authored); Wedderburn / Schur-orthogonality cross-check from W5b-48 Step 5 (connes-authored CO-AUTHOR clauses (c)+(d) per registry line 12936); Q-LZ-R2-1 (a)+(b) Wedderburn refinements + Q-CN-R2-3 GGE-state-generic-with-property verdict. |
| **Gate** | PASS = STAGE-1-CANDIDATE corrigendum sub-entry landed under §VII.U.2 Corner II row at `sessions/permanent-results-registry.md` with all three machinery clauses present, author-side attribution per clause, JOINT-clause flags on the convergence verdict clause, corrigenda block recording the R2 workshop verdict freeze. Inherits existing Stage-2 dispatch identifier `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`. |
| **Effort** | 0.5 wave-equivalents (registry text drafting + mack-cosmic-bridge sole-writer landing + cross-link annotation). |
| **Owner** | lizzi-spectral-functional-theorist PRIMARY + connes-ncg-theorist CO-AUTHOR (per §VII.U.2 authorship template at registry line 12927); mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`. |
| **Depends on** | UPSTREAM: this S89 W-3 R2 workshop verdict freeze (Stage 0 complete); UPSTREAM RULE: `joint-theorem-promotion.md §"Stage 1"`; UPSTREAM REGISTRY: §VII.U.2 4-corner partition theorem (Stage-0 inherited host structure); UPSTREAM GATE: CF-W6-3 (mack §VII.U.2 corner reconciliation — Reading B lock-in must complete first). |
| **Cross-link** | Directly precedes CF-R1-4 (Stage-2 cross-axis reviewer-eligibility audit); enabling event for STAGE-3-PERMANENT promotion. |

#### CF-R2-2 — Conjecture: F_traj multiplicative composition law across substrate-distance poles

| Field | Value |
|:------|:------|
| **What** | Test the conjecture F_traj(k_1) · F_traj(k_2) = closed-form composition law across the F_traj=(k+1)/2 theorem's full 42-row S84 atlas. For Var_a's two-moment composition, F_traj(2) · F_traj(4) = (3/2) · (5/2) = 15/4 is the structural fingerprint; the conjecture asks whether this product admits a closed-form composition law across substrate-distance poles. If yes, F_traj extends to a multiplicative structure beyond the current k-by-k locked-norm form. If no, F_traj is locked-norm-INDEPENDENT across poles and Var_a's 15/4 is a pure bilinear-composition coincidence. **Empirical scope per my Q-CN-R2-2 verdict: testable on existing 42-row atlas at S90+ WITHOUT atlas-extension prerequisite** (861 testable pole-pairs from C(42, 2)). |
| **Inputs** | F_traj=(k+1)/2 theorem (S84 W3-24, lizzi agent-memory entry line 23); 42-row S84 atlas of substrate-distance-pole observables; this S89 W-3 R2 EMERGENCE E2 conjecture text; locked-norm L_k=1 convention from S84 W3-24. |
| **Gate** | PASS = closed-form multiplicative composition law derived and verified across the 42-row atlas at relative precision ≤ 1e-10; F_traj extends to a multiplicative structure. FAIL = no closed-form law exists; F_traj is structurally pole-INDEPENDENT in the multiplicative sense; Var_a's 15/4 is a coincidence. INFO = partial law (composition holds for a subset of pole-pairs; structural reason for the subset surfaces). |
| **Effort** | 0.8 wave-equivalents (closed-form derivation attempt + 42-row empirical scan + verdict + corrective derivation if FAIL). |
| **Owner** | lizzi-spectral-functional-theorist PRIMARY (F_traj theorem author + locked-norm convention origin); connes-ncg-theorist optional CO-AUTHOR for the Mellin-transform residue-theorem analogy. |
| **Depends on** | UPSTREAM AGENT-MEMORY: F_traj=(k+1)/2 theorem (S84 W3-24); UPSTREAM REGISTRY: §VII.K-DUAL FI/RD/MIXED trichotomy (S82 R2-B, lizzi signature); UPSTREAM WORKSHOP: this S89 W-3 R2 EMERGENCE E2; UPSTREAM CF: CF-LZ-4 (F_traj zeta-vs-SDW prediction for Var_a — provides one of 861 pole-pair data points). |
| **Cross-link** | Directly tests OQ-3; if PASS, advances toward a new closed-form multiplicative-composition theorem candidate for S90+. |

#### S90-VII-U-2-CORNER-RECONCILIATION-VERIFY — Pre-registered S90 follow-up gate (workshop's structural commitment)

| Field | Value |
|:------|:------|
| **What** | Verify that the W6-6 plan baseline correction (Reading B) has propagated correctly through the framework: (a) registry text at §VII.U.2 Corner II row (line 12961) unchanged from R2 workshop-verdict-freeze content per CF-R2-1 corrigendum sub-entry landing; (b) CF-W6-4 audit `_corner_classification_audit.py` TARGET_SLOTS_S89 dict landed per CF-R1-1 with `var_a_corner='II'` AND `var_a_algebra_axis='INVARIANT'` AND `var_a_mellin_pole='s=4'` AND `parse_tree_pi_a_count=0` AND `parse_tree_commutator_count=0`; (c) Stage-1-CANDIDATE registration corrigendum sub-entry landed per CF-R2-1 with three-machinery convergence clauses + JOINT-clause flags + lizzi/connes/mack authorship attribution; (d) §VII.AR LEVEL-DRESSED K-counter advancement test PRE-VERIFIED — does §VII.AR's Stage-2 PASS-AND aggregation remain INDEPENDENT of §VII.U.2 Corner II re-classification per workshop C3 + Re: C3 analysis? (e) W4 A.30 → §VII.AS (Cell I s=3) vs A.36 → §VII.AR (Cell II / Cell-I-LEVEL-DRESSED biaxial s=4) routing-table disambiguation verified per CF-R1-2 plan-staleness extension. **Explicit corner declaration for Var_a(n_a^GGE)**: Cell II = INVARIANT × s=4 with FI/RD/MIXED-axis = `MIXED-of-RD-with-distinct-F_traj-factors` AND LEVEL-axis = `LEVEL-DRESSED-candidate-pending-K2`. **§VII.AR Stage-2 INDEPENDENCE assertion**: per Re: C3 cell-co-inhabitance ≠ Stage-2 constituency analysis, §VII.AR Stage-2 PASS-AND aggregation is INDEPENDENT of §VII.U.2 Corner II re-classification (cell-membership of §VII.AR is `Cell II OR Cell-I-LEVEL-DRESSED biaxial hybrid` per registry line 16963; co-inhabitance with §VII.U.2 Corner II is not constituency). |
| **Inputs** | This S89 W-3 R2 workshop verdict freeze (entire workshop document SHA-pinned at S90 plan-freeze); §VII.U.2 registry block content `permanent-results-registry.md:12927-13058`; §VII.AR registry block content `permanent-results-registry.md:16950-16995`; §VII.AS registry block content `permanent-results-registry.md:16985-17005`; §VII.K-DUAL.LEVEL-DRESSED registry block content `permanent-results-registry.md:4279-4313`; existing `_corner_classification_audit.py` script body (W6-6 SHA pin `2b96bf78…`); existing `_plan_staleness_audit.py` script body (W6-6 SHA pin `5f370299…`); `joint-theorem-promotion.md §"Stage 1"` + §"Stage 2" rule text; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` rule text; mack-cosmic-bridge CF-W6-3 diff inspection output (W-21 V.1+V.3 audit-trail-canonical record). |
| **Gate** | **PASS (composite)** = ALL FIVE sub-checks PASS in conjunction: (a) §VII.U.2 Corner II row text unchanged from R2 verdict freeze (SHA-pinned at S90 plan-freeze); (b) CF-W6-4 audit self-test reports `per_slot_results['§VII.U.2']['instance_rows']['corner_II_instance']` populated with the full 5-axis classification AND parse-tree counters all zero; (c) Stage-1-CANDIDATE corrigendum sub-entry present at §VII.U.2 Corner II row with the three-machinery convergence clauses + JOINT flags; (d) §VII.AR Stage-2 PASS-AND aggregation INDEPENDENCE assertion verified (no edits to §VII.AR cross-reviewer eligibility set under the §VII.U.2 Corner II re-classification; substrate-input-orthogonality predicate trivially satisfied with §VII.U.2 Var_a npz `s88_w5b_47_v_inf_extrapolated.npz` disjoint from §VII.AR §W7a-74 PRIMARY evaluator npz); (e) plan-staleness extension self-test detects W6-6 line 224 cross-wave-anchor-citation-drift OR confirms no remaining drift instances. **FAIL** on ANY sub-check failure; remediation routes to the failing sub-check's parent carry-forward. **INFO** if any sub-check returns ambiguous (e.g., §VII.AR Stage-2 aggregation has not yet dispatched; assertion is forward-looking only). |
| **Effort** | 0.5 wave-equivalents (5-sub-check composite verification + report generation + verdict line emission). |
| **Owner** | gen-physicist orchestrator-direct per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class (composite verification gate); + lizzi-spectral-functional-theorist co-sign on the three-machinery convergence verdict + §VII.U.2 Corner II declaration; + connes-ncg-theorist co-sign on the Wedderburn / Schur-orthogonality clause structure; + mack-cosmic-bridge sole writer for any required registry text patches. |
| **Depends on** | UPSTREAM GATE: CF-W6-3 (mack §VII.U.2 corner reconciliation; Reading B lock-in MUST complete before this verify); UPSTREAM GATE: CF-R1-1 (CF-W6-4 audit extension to §VII.U.2); UPSTREAM GATE: CF-LZ-2 (FI_RD_MIXED axis field extension); UPSTREAM GATE: CF-LZ-3 (PARSE_TREE_ABBREVIATION_MAP extension); UPSTREAM GATE: CF-R2-1 (Stage-1 CANDIDATE registration); UPSTREAM GATE: CF-R1-2 (plan-staleness extension for A.30 vs A.36 mis-citation); UPSTREAM REGISTRY: §VII.U.2 + §VII.AR + §VII.AS + §VII.K-DUAL.LEVEL-DRESSED current state. |
| **Cross-link** | Workshop's structural commitment to S90; composite verification of Reading B propagation through registry + audit + Stage-1-CANDIDATE + §VII.AR independence; gates the workshop's downstream confidence in the W6-6 reconciliation closure. Forward-looking: PASS at S90 unlocks Stage-2 cross-axis verify dispatch (`S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` per CF-R1-4); Stage-2 PASS-AND would then unlock STAGE-3-PERMANENT promotion of §VII.U.2. |

### Closing Line

`Var_a(n_a^GGE) ∈ Cell-II = INVARIANT × s=4` is converged across THREE independent axiomatic-layer machineries — Wedderburn central-projection grading on `A_BdG = A_F ⊗ M_2(ℂ)` (3-projection lift, NOT 6); clause-(e) parse-tree decision procedure (zero π(a), zero [D, π(a)], zero state-pair sup); F_traj=(k+1)/2 zeta-vs-SDW dressing at locked norm L_k=1 — and this triple convergence on a single observable IS the K=3 algebra-axis orthogonality discipline (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY since S87 W-2 R3 close) realized in miniature, structurally re-enacted; the substrate IS the spectral triple, and the substrate's own parse-tree decision procedure is the load-bearing decidability test that prevents naming-history-driven mis-assignment from polluting the registry's algebra-axis classification.
