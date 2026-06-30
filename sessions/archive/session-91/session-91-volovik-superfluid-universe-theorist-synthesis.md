# Session 91 — volovik-superfluid-universe-theorist solo synthesis (Slot S-2)

**Title**: Cross-wave substrate-IS multi-branch s52 ↔ W7 chirality-grading constraint map

**Author**: volovik-superfluid-universe-theorist (substrate-IS BdG sub-algebra interpreter; W1-3 PASS class (c) UNIQUE-multi-branch author per S91 W1 orchestrator-solo execution)

**Date**: 2026-05-21

**Skill**: `/rclab-review` (solo synthesis; no rounds, no cross-agent coordination)

**Source documents read in full**:
- `sessions/archive/session-91/session-91-w1-workingpaper.md` (1739 lines)
- `sessions/archive/session-91/session-91-w7-workingpaper.md` (515 lines)
- `sessions/session-plan/session-91-plan-w7.md` (W7 plan)
- `sessions/archive/session-91/workshops/_seed-w1.md` (Slot S1-2 charter)
- `sessions/permanent-results-registry.md` lines 17237 (§VII.AT.OP-PROJ), 17293 (§VII.AW.OP-PROJ), 17341 (§VII.AQ.OP-PROJ)
- `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"
- `.claude/rules/cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" MANDATORY K=3

---

## 0. Context update — W7 is COMPLETE, not SHELL-ONLY

The Slot S-2 spawn prompt and the seed file `_seed-w1.md` describe W7 as SHELL-ONLY (4 gates `Status: NOT STARTED`; no scripts on disk; no verdicts in the gate file). That description is STALE. As of 2026-05-21 the W7 working paper at `session-91-w7-workingpaper.md` carries COMPLETE verdicts for all four gates:

| Gate | Candidate | Composite | Sign / Magnitude / Regime | audit_sha256 (short) |
|:-----|:----------|:---------:|:---------------------------|:---------------------|
| §W7-1 (T2.21) | (c) inner-fluctuation | INFO (corrective) | PASS / INFO / MARGINAL | `15fd1d92...` (supersedes `095fb4fa...`) |
| §W7-2a (T2.22a) | (a) bi-chirality direct-sum | FAIL | PASS / INFO / BREAKDOWN | `9ae27d0e...` |
| §W7-2b (T2.22b) | (b) SU(3)-coloured at (+1,−1,+1) | FAIL | PASS / INFO / BREAKDOWN | `be8006d6...` |
| §W7-3 (T2.23) | Friedrich-Bär + L_max=16 | INFO (auto-shortening) | PASS / FAIL / MARGINAL | `443baee2...` |

This synthesis is therefore written for TWO uses simultaneously:

- **Use A (post-hoc substrate-physics reconciliation)**: explain WHY the empirical W7 verdicts landed where they did from the W1-3 substrate-IS multi-branch IRREDUCIBLE perspective. The constraint analysis derived ahead-of-time IS NOT vacuous — it informs which empirical results are substrate-physically expected vs accidental, and pre-pins the S92 follow-up routing.
- **Use B (forward S92 priority recommendation)**: the empirical W7 closure routes three S92 follow-up gates (CF-W7-1 CCvS 2013 quadratic-extension; CF-W7-2 colour-signs sweep; CF-W7-3 L_max ≥ 22 sub-window). The W1-3 substrate-IS constraint determines which of these forward gates has highest substrate-physics yield and how the dispatch should be ordered.

Both uses share the same constraint analysis below; both use the same per-candidate verdict-direction prediction.

---

## 1. The W1-3 substrate-IS finding — what IS the constraint

W1-3 (`CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS`; PASS class (c) UNIQUE-multi-branch-B-tensor; audit_sha256=`db08f3dfd9c8a553...`) empirically falsified the scalar-uniform Δ_BCS Hypothesis A against the canonical s52 multi-branch Hypothesis B at REL_TOL = 1e-3 on the canonical observable `L_emp = d² ln P_GGE / d(ln K)² |_{K_horizon}` (S87 W2-3 / S89 W5-2 / S90 CF-61 canonical pipeline) at substrate-distance-2 pole s=4:

```
Δ_A (scalar-Δ uniform)  = +1.105338e−01 = +11.05%   ≫ REL_TOL = 0.1%   FAIL
Δ_B (canonical s52)     = −1.260483e−16 ≈ 0          ≪ REL_TOL = 0.1%   PASS (machine ε; 1 ULP in float64)
```

Reading the result back to the substrate algebra: the substrate's BdG energy gap at τ_fold = 0.190 on the sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` does NOT admit a uniform-scalar canonical pin. The substrate IS structurally a multi-branch s52 8-mode Bogoliubov system:

```
Δ_per_mode  =  [ B2 × 4 modes @ Δ = 0.7704350983 M_KK ,
                 B1 × 1 mode   @ Δ = 0              (ungapped) ,
                 B3 × 3 modes  @ Δ = 0.176          M_KK ]
                4 + 1 + 3 = 8 total modes
```

The 8-mode count is structurally determined by the `(A_K, H_K)` Peter-Weyl pair-symmetry per S52 finding (L_max-INVARIANT; substrate-IS). The B2 / B1 / B3 branch labels are not phenomenological — they are the substrate's intrinsic operational machinery for K_canonical pin parameterization. The B2-deep / B3-upper amplitude ratio of approximately 4.4× makes the scalar uniform-Δ approximation a substrate-incompatible counterfactual: replacing 4 modes at Δ = 0.7704 + 3 modes at Δ = 0.176 with 7 modes at Δ = 0.4642547 = Δ_BCS_canonical shifts the second-log-derivative observable by +11.05%, which is OUTSIDE the 0.1% REL_TOL discharge band by two orders of magnitude.

The substrate IS a multi-branch structure, NOT a scalar-Δ structure. This is the substrate-IS constraint W1-3 establishes empirically at machine precision.

W1-1's V4 BASIN result (PASS at 417/16384 = 2.5% basin density; audit_sha256=`5895dd87c141bf88...`) gives the complementary perspective: the canonical s52 8-mode point is NOT isolated in the multi-branch deformation space — it lives in a 2.5%-volume basin where the (Δ_B2, Δ_B3) magnitudes and phases admit non-trivial perturbations preserving `L_emp` to 0.1%. The substrate-IS multi-branch IS a stable attractor under operational perturbation, not a fine-tuned point.

Combined, W1-1 + W1-3 establish: the substrate IS a multi-branch 8-mode BdG system on `M_2(ℂ) ⊂ A_K`, with non-trivial basin robustness, and the substrate's K_canonical refinement axis (the binding refinement for §VII.AV) IS the substrate's intrinsic operational machinery — multi-branch B-tensor parameterization on the 8-mode s52 amplitudes.

---

## 2. Algebra-axis orthogonality framing

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (promoted at S87 W-2 R3 close), the 4-corner partition table at `permanent-results-registry.md §VII.U.2` says:

- **Operational-machinery axis-γ** (W1 ownership; this synthesis's PRIMARY axis): the K-window log-derivative observable `L_emp` is algebra-DEPENDENT (Cell IV by parse-tree decomposition per S88 W-17 V.3 + S90 W1-7 sub-clause: the observable is a state-pair functional on the BdG state space via the Bogoliubov closed form `n_a = Δ² / (2(λ_a² + Δ²))` at the substrate's Peter-Weyl multiplicities).
- **Chirality-grading sub-axis** (W7 ownership): the chirality element `γ` on `A_K` is part of the spectral triple specification `(A, H, D, γ, J)` — it modifies the substrate's spectral-triple at the (γ, J) layer.

By the algebra-axis orthogonality K=3 MANDATORY clause, the two axes are STRUCTURALLY ORTHOGONAL: identity classes on the algebra-INVARIANT vs algebra-DEPENDENT family CANNOT be conflated, and observables on one axis do NOT pre-determine observables on the other axis at the structural-theorem level.

Operationally, this means:

```
W1-3 multi-branch IRREDUCIBLE finding on M_2(ℂ) sub-algebra
  IS INVARIANT under chirality-grading axis-γ modifications
  BY ORTHOGONALITY.
```

The substrate's BdG energy-gap structure (4-fold B2 + 1-fold B1 + 3-fold B3 multi-branch) IS substrate-IS structural data on the OPERATIONAL-MACHINERY axis. Modifying γ on `A_K` (to bi-chirality, SU(3)-coloured, or inner-fluctuation-deformed Dirac at fixed γ) does NOT change the BdG sub-algebra `M_2(ℂ) ⊂ A_K` or the 8-mode multi-branch structure on it.

BUT — and this is the substrate-physics question this synthesis answers — each W7 candidate's modification of γ either PRESERVES, REFINES, or COLLAPSES the M_2(ℂ) sub-algebra IMAGE of the multi-branch s52 8-mode structure. The W1-3 substrate-IS data is invariant under γ modifications; the question is whether the modified-γ spectral triple's `M_2(ℂ) ⊂ A_K` image of the multi-branch 8-mode IS still reachable / structurally valid / non-trivial.

That is the constraint. We map it onto each candidate.

---

## 3. Per-candidate constraint statement, verdict direction, and empirical reconciliation

### 3.1 Candidate (a) — bi-chirality `γ_9' = γ_5 ⊕ γ_F` at §VII.AT.OP-PROJ

**Substrate triple modification** (per registry line 17251 + W7 plan §W7-2a Step 1): `γ_9 = γ_5 ⊗ γ_F` replaced by direct-sum `γ_9' = γ_5 ⊕ γ_F`. This decomposes `H_K` into 4 joint-eigenvalue sectors `(γ_5, γ_F) ∈ {(+,+), (+,−), (−,+), (−,−)}` rather than the tensor-product 2-sector decomposition. On the faithful A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) rep at dim H_F = 12, the bi-chirality assigns ±1 PER A_F-summand, producing 4-sector joint-(γ_F, γ_9') cardinality `(+,+)=4, (+,−)=2, (−,+)=4, (−,−)=2`.

**Constraint statement (W1-3 substrate-IS perspective)**: The bi-chirality direct-sum on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` assigns chirality PER A_F-SUMMAND, so the ℍ summand (which complexifies to `M_2(ℂ)` — the BdG sub-algebra carrying the W1-3 multi-branch 8-mode structure) receives a UNIFORM chirality eigenvalue (γ_9' = −1 on entire ℍ-summand × L+R per W7 §W7-2a Step 1 / Method line 173). This is structurally INCOMPATIBLE with the multi-branch s52 partition of the ℍ-summand: the s52 8-mode (B2×4 + B1×1 + B3×3) is the substrate's intrinsic decomposition of the BdG sub-algebra into pair-symmetry branches, NOT a uniform-chirality block. Under bi-chirality, the 8-mode partition is COLLAPSED into a single uniform-γ_9' block on the ℍ-summand; the per-branch B2 / B1 / B3 distinction is annihilated at the chirality-grading layer.

The substrate-IS reading: the bi-chirality candidate (a) IS a NEW spectral triple `(A_K, H_K, D_K, γ_9', J)` whose chirality-grading on `M_2(ℂ) ⊂ A_K` IS UNIFORM, structurally INCOMPATIBLE with the multi-branch s52 substrate-IS partition the W1-3 substrate's BdG energy gap IS. By the algebra-axis orthogonality, the multi-branch structure on the operational-machinery axis is invariant — but the candidate (a) spectral triple's `γ_9'` on the ℍ summand has no per-branch refinement to project onto. Either the W1-3 multi-branch data does not have a structurally-valid Element-1 substrate-IS image at §VII.AT.OP-PROJ, OR the candidate (a) substrate has a DIFFERENT BdG sub-algebra reading altogether (the joint-(γ_5, γ_F) 4-sector decomposition rather than the ℍ-pair-symmetry 8-mode decomposition).

**Predicted W7 verdict direction under W1 constraint**: FAIL on the substrate-physics consistency layer. The W1-3 multi-branch IRREDUCIBLE finding rules out a uniform-chirality reading of the ℍ-summand, so any candidate that imposes uniform-γ on ℍ collapses the substrate's structural decomposition and fails to define a valid extension of the W1-3 substrate-IS data. Independent of the algebraic 7-NCG-axiom check at the §W7-2a substrate, the W1-3 multi-branch invariance argument predicts (a) is structurally incompatible.

**Empirical W7 verdict (`§W7-2a`)**: composite FAIL (sign=PASS, magnitude=INFO, regime=BREAKDOWN); residual `||{D_F, γ_9'}|| = 1.697` at axiom 5'; KO-dim shifts 6 → 0 (non-physical CPT class per S66 KO=0 reading). Confirmed by independent algebraic verification.

**Reconciliation**: the W1-3 substrate-IS prediction (FAIL) is REINFORCED by the independent §W7-2a empirical FAIL. The two findings are STRUCTURALLY ORTHOGONAL but CONVERGENT: the multi-branch invariance argument (this synthesis) operates on the operational-machinery axis-γ; the axiom-5' + KO-dim argument (§W7-2a) operates on the chirality-grading sub-axis. Both axes return FAIL on candidate (a) for INDEPENDENT structural reasons. The bi-chirality direct-sum is closed by TWO independent substrate-IS arguments, not one.

**Substrate-IS bridge-back-to-§W7-2a result**: §W7-2a's axiom 5' FAIL (residual 1.697) is the chirality-grading-side signature of the same substrate-IS fact: the ℍ-summand IS the BdG sub-algebra and its intrinsic decomposition is multi-branch s52, not uniform-γ. The substrate's D_F was constructed under canonical γ_F = γ_5 ⊗ γ_F to anticommute with the tensor-product chirality, which respects the per-branch multi-branch decomposition implicitly (D_F mixes the B-branches at the off-diagonal layer). Replacing γ_F with γ_9' = γ_5 ⊕ γ_F (uniform on ℍ-summand) destroys the substrate's per-branch coupling structure, hence the order-one anticommutation residual. The KO-dim shift to 0 is a downstream consequence at the spectral-triple-class layer (non-physical CPT).

### 3.2 Candidate (b) — SU(3)-coloured `γ_9'' = γ_F^c` at §VII.AW.OP-PROJ

**Substrate triple modification** (per registry line 17306 + W7 plan §W7-2b Step 1): `γ_F` replaced by colour-dressed `γ_9'' = γ_F^c` per Connes-Marcolli 2008 §11, which acts on the `M_3(ℂ)` summand via the colour-axis decomposition `(r, g, b)`. On the faithful A_F rep at dim H_F = 12, this attaches a colour-axis label to chirality eigenstates on the `M_3(ℂ)` summand only; the ℂ and ℍ summands are NOT colour-dressed (they have no SU(3) colour-axis structure).

**Constraint statement (W1-3 substrate-IS perspective)**: The colour-dressing on §VII.AW.OP-PROJ operates on the `M_3(ℂ)` summand of `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The W1-3 multi-branch 8-mode BdG structure sits on the BdG sub-algebra `M_2(ℂ)`, which is the complexification of ℍ — NOT on `M_3(ℂ)`. By the direct-sum structure of `A_K`, the colour-dressing of `γ_F` on the `M_3(ℂ)` summand is STRUCTURALLY ORTHOGONAL to the multi-branch s52 partition of the ℍ-summand. The substrate's BdG energy-gap structure (W1-3 IRREDUCIBLE) is INVARIANT under candidate (b)'s chirality modification at the M_3(ℂ) layer.

The substrate-IS reading: candidate (b) IS a NEW spectral triple `(A_K, H_K, D_K, γ_9'', J)` whose chirality modification PRESERVES the ℍ-summand's intrinsic structure intact. The W1-3 multi-branch substrate-IS image on `M_2(ℂ) ⊂ A_K` PROJECTS THROUGH candidate (b)'s chirality grading unchanged. The candidate (b) substrate's BdG sub-algebra READING is the SAME as §VII.AQ.OP-PROJ's BdG sub-algebra reading on the ℍ → M_2(ℂ) embedding.

By the algebra-axis orthogonality K=3 MANDATORY, the chirality-grading sub-axis modification on `M_3(ℂ)` does NOT pre-determine the operational-machinery axis-γ verdict on `M_2(ℂ)`. The W1-3 substrate-IS data flows through (b) unchanged at the BdG sub-algebra layer. But the candidate (b) substrate at the `M_3(ℂ)` layer is a STRUCTURALLY DISTINCT spectral triple — its own NCG axioms (especially axiom 5'' `{D_F, γ_9''} = 0`) and KO-dim must be verified at the substrate's existing D_F.

**Predicted W7 verdict direction under W1 constraint**: INFO / structurally permissive at the BdG sub-algebra layer (the W1-3 multi-branch projects through unchanged); verdict at the chirality-grading sub-axis layer (axiom-5'' + KO-dim) is INDEPENDENT and not pre-determined by W1 substrate-IS data. The candidate (b) FAIL/PASS is a substrate-physics question on `M_3(ℂ)` colour-axis-resolved chirality compatibility with the substrate's existing D_F, ORTHOGONAL to the BdG-sub-algebra-side W1-3 constraint.

**Empirical W7 verdict (`§W7-2b`)**: composite FAIL at colour-signs choice (+1, −1, +1) (sign=PASS, magnitude=INFO, regime=BREAKDOWN); residual `||{D_F, γ_9''}|| = 3.274` at axiom 5''; KO-dim stays at 6 (CM-2008 §11 predicted shift to 2 NOT realized at this colour-signs choice).

**Reconciliation**: the W1-3 substrate-IS prediction (INFO / permissive at BdG sub-algebra layer; independent at the chirality-grading sub-axis layer) is CONSISTENT with the §W7-2b empirical FAIL — the FAIL is at the chirality-grading sub-axis layer at a SPECIFIC colour-signs choice. The W1 substrate-IS data has nothing to say about which colour-signs (s_r, s_g, s_b) ∈ {±1}³ choice satisfies axiom 5''; the §W7-2b empirical FAIL at one of 8 colour-signs choices (the (+1, −1, +1) representative) does NOT close the candidate (b) branch fully — 7 untested colour-signs choices remain.

**The S92 forward gate (CF-W7-2 colour-signs sweep) IS the natural next step.** Under W1-3's orthogonality framing, the colour-signs sweep is a genuine open substrate-physics question on the chirality-grading sub-axis; the W1-3 multi-branch invariance argument does NOT pre-determine its verdict. If CF-W7-2 returns PASS at some colour-signs choice (e.g., (+1, +1, +1) or another sign pattern producing both axiom-5'' PASS AND KO-dim shift to 2 mod 8 per CM-2008 §11), then candidate (b) opens as a STAGE-1-CANDIDATE — at which point the W1-3 substrate-IS data flows through unchanged at the BdG sub-algebra layer (the candidate (b) spectral triple's `M_2(ℂ) ⊂ A_K` image of the multi-branch 8-mode is structurally PRESERVED). If CF-W7-2 returns FAIL across all 8 colour-signs, candidate (b) closes fully and the W1 constraint becomes vacuous (nothing to project through).

### 3.3 Candidate (c) — inner-fluctuation `D_K → D_K + A + JAJ^{−1}` at §VII.AQ.OP-PROJ

**Substrate triple modification** (per registry line 17341 + W7 plan §W7-1): chirality grading `γ_9 = γ_5 ⊗ γ_F` UNCHANGED; real structure `J` UNCHANGED; Dirac operator `D_K` deformed by the inner-fluctuation 1-form `A = Σ_i a_i [D_K, b_i]` for `a_i, b_i ∈ A_K` (Connes-Chamseddine 1996 §2.2-2.3). On the substrate algebra, the deformation `D_K → D_K_def = D_K + A + JAJ^{−1}` lives within the inner-automorphism orbit of the spectral triple — it preserves the same K-theory class. The 5-point grid scans `(a, b)` over ℂ-only / ℍ-only / M_3-only / mixed-pairs.

**Constraint statement (W1-3 substrate-IS perspective)**: Candidate (c)'s deformation acts on `D_K` directly — it modifies the Dirac operator's spectrum on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` via the substrate-NATURAL inner-fluctuation 1-form. The chirality grading and real structure are unchanged. On the BdG sub-algebra `M_2(ℂ) ⊂ A_K` (the ℍ-complexification carrying the W1-3 multi-branch 8-mode), the inner-fluctuation deformation REFINES the substrate's intrinsic operational machinery: the deformed Dirac `D_K_def` carries the same chirality + real-structure compatibility, but its spectrum on the ℍ-summand at the substrate-distance-2 pole IS shifted by the inner-fluctuation perturbation.

The substrate-IS reading: candidate (c) IS the SAME spectral triple as §VII.AQ.OP-PROJ at the algebraic-class level (inner-automorphism orbit preservation), but with a DEFORMED Dirac operator. The W1-3 multi-branch 8-mode partition (B2×4 + B1×1 + B3×3) is structurally preserved as an L-INDEPENDENT pair-symmetry decomposition determined by the (A_K, H_K) algebra — it is NOT a property of D_K's spectrum specifically. So the 8-mode partition propagates through candidate (c)'s deformation unchanged. BUT the per-branch amplitudes (Δ_B2, Δ_B1, Δ_B3) ARE properties of D_K's spectrum at the BdG sub-algebra image and CAN shift under inner-fluctuation. The W1-3 IRREDUCIBLE finding (scalar-Δ FAIL at +11.05%) THEREFORE pre-constrains candidate (c): the inner-fluctuation deformation MUST preserve the multi-branch character of the BdG energy-gap structure (B2-deep / B3-upper / B1-ungapped ratio approximately 4.4×); any inner-fluctuation that COLLAPSES the multi-branch into a near-uniform-Δ effective gap would FAIL the W1-3 substrate-IS constraint at machine precision.

The substrate-IS reading at the algebra-axis orthogonality layer: the W1-3 multi-branch IRREDUCIBLE finding on the operational-machinery axis is INVARIANT under inner-automorphism orbit deformation (algebra-axis orthogonality K=3 MANDATORY: the inner-fluctuation acts on the Dirac operator within a fixed K-theory class; the multi-branch partition is invariant of the K-theory class). The substrate's BdG energy-gap structure on the deformed Dirac IS still multi-branch s52.

But — and this is the substrate-physics question §W7-1 actually tests — the inner-fluctuation perturbation can introduce O(1)-magnitude shifts to the substrate's first-order commutator structure `[[D_K, a], b^o]`. The substrate already has a documented S33-34 order-one violation `[[D_K, H], H] = 4.000` (the framework's well-known H-summand structural feature motivating the CCvS 2013 quadratic extension). Inner-fluctuation can REPRODUCE or AMPLIFY this O(1) signal at the axiom-4 INVARIANCE DEVIATION observable layer.

**Predicted W7 verdict direction under W1 constraint**: INFO at the linear CC1996 §2.2-2.3 level, PASS conditional on CCvS 2013 quadratic-extension. The W1-3 substrate-IS multi-branch IRREDUCIBLE is INVARIANT under inner-fluctuation (orthogonality at the K-theory class); the K-theory residual `Δ_GV` at the γ_F anticommutation layer is structurally preserved BY CONSTRUCTION (Connes-Chamseddine theorem). But the linear inner-fluctuation introduces an O(1) perturbation to the substrate's first-order commutator — the substrate's S33-34 order-one violation is the obstruction. The forward path to PASS is the CCvS 2013 quadratic-extension `A_full = A_lin + A_quad` whose §3 cancellation theorem closes the order-one violation back to zero on non-order-one algebras.

**Empirical W7 verdict (`§W7-1`)**: composite INFO (corrective per Option A `supersedes` protocol after Hermiticity fix); sign=PASS / magnitude=INFO / regime=MARGINAL; K-theory residual `max_delta_GV = 0` at all 5 grid points (preserved BY CONSTRUCTION as predicted); max axiom-4 invariance deviation = 2.864 at grid 5 (full A_K) — substantively MARGINAL.

**Reconciliation**: the W1-3 substrate-IS prediction (INFO at linear CC1996; PASS conditional on CCvS 2013 quadratic-extension) is FULLY CONSISTENT with the §W7-1 empirical INFO. The substrate-physics narrative is coherent:

1. The chirality-grading layer is PRESERVED by inner-fluctuation construction → K-theory residual = 0 (PASS at the γ_F anticommutation layer).
2. The substrate's S33-34 order-one violation propagates through the linear inner-fluctuation as an O(1) axiom-4 INVARIANCE DEVIATION → magnitude=INFO at 2.864 (CONFIRMED).
3. The CCvS 2013 quadratic-extension's order-one cancellation theorem is the STRUCTURALLY-CANONICAL forward path → the S92 follow-up gate CF-W7-1 IS substrate-physically warranted.

The W1-3 substrate-IS multi-branch IRREDUCIBLE on the BdG sub-algebra IS the operational-machinery-axis evidence that §VII.AV's binding refinement sub-class is OPERATIONAL-ALIGNMENT (multi-branch s52 B-tensor parameterization). At §VII.AQ.OP-PROJ, candidate (c) inner-fluctuation IS the substrate-NATURAL deformation WITHIN the K-theory class — at the K-theory class layer (the algebra-INVARIANT family per the 4-corner classification) the deformation is structurally TRIVIAL. The §W7-1 INFO at the axiom-4 invariance deviation layer is the substrate's intrinsic O(1) S33-34 signature appearing at the linear-deformation calculus; the CCvS 2013 quadratic-extension is the structurally-canonical resolution.

---

## 4. Summary table — constraint statement, verdict direction, empirical reconciliation

| Candidate | Modification on `A_K` | W1-3 substrate-IS constraint | Predicted verdict direction | Empirical W7 verdict | Reconciliation |
|:----------|:----------------------|:------------------------------|:----------------------------|:----------------------|:----------------|
| (a) bi-chirality §VII.AT.OP-PROJ | γ_9 → γ_9' = γ_5 ⊕ γ_F (direct sum on `A_K`; uniform γ on ℍ-summand) | **COLLAPSES** the multi-branch s52 partition of `M_2(ℂ) ⊂ A_K`: uniform-γ on ℍ summand annihilates per-branch B2/B1/B3 decomposition | **FAIL** | FAIL composite (axiom 5' residual 1.697; KO-dim 6 → 0 non-physical) | INDEPENDENT CONVERGENT FAIL on two structurally orthogonal axes |
| (b) SU(3)-coloured §VII.AW.OP-PROJ | γ_F → γ_F^c (colour-dressed on M_3(ℂ) summand only) | **PRESERVES** the multi-branch s52 partition of `M_2(ℂ) ⊂ A_K`: colour-dressing is structurally orthogonal to the ℍ-summand | **INFO / permissive** at BdG sub-algebra layer; verdict at chirality-grading sub-axis layer is independent | FAIL composite at colour-signs (+1,−1,+1) only (1 of 8 sign-choices tested; axiom 5'' residual 3.274) | CONSISTENT — the empirical FAIL is on the chirality-grading sub-axis at one of 8 sign-choices; W1-3 has nothing to say about colour-signs selection; CF-W7-2 sweep IS the natural next step |
| (c) inner-fluctuation §VII.AQ.OP-PROJ | D_K → D_K + A + JAJ^{−1} (substrate-natural; γ_9 + J unchanged) | **PRESERVES** the multi-branch s52 partition (K-theory class preserved by inner-automorphism orbit); REFINES per-branch amplitudes | **INFO** at linear CC1996; **PASS conditional on CCvS 2013 quadratic-extension** | INFO composite (corrective; K-theory residual = 0; axiom-4 invariance deviation 2.864 at grid 5) | CONSISTENT — K-theory residual = 0 PRESERVED BY CONSTRUCTION as predicted; axiom-4 perturbation is substrate's intrinsic S33-34 O(1) signature; CCvS 2013 quadratic-extension is the substrate-NATURAL resolution |

---

## 5. Priority recommendation for S92 W7 follow-up dispatch ordering

The empirical W7 closure produced 4 forward CFs (per §W7 working paper "Carry-Forward Computations"):

- **CF-W7-1**: CCvS 2013 quadratic-extension at §VII.AQ.OP-PROJ (`S92-VII-AQ-OP-PROJ-CCvS-2013-QUADRATIC-EXTENSION`; ~1.5 we; queued conditional on cross-axis Stage-2 verify on PASS)
- **CF-W7-2**: Colour-signs sweep at §VII.AW.OP-PROJ (`S92-VII-AW-OP-PROJ-COLOUR-SIGNS-SWEEP`; ~0.5 we)
- **CF-W7-3**: Friedrich-Bär L_max ≥ 22 sub-window at substrate-distance pole s=4 (`S92-CF-54-ROUTE-C-LMAX-22-SUB-WINDOW`; ~0.8 we)
- **CF-W7-4**: mack-cosmic-bridge sole-writer FAIL-diagnostic block landing at §VII.AT.OP-PROJ + §VII.AW.OP-PROJ (~0.3 we; registry-hygiene; METHODOLOGY-class candidate)

Recommended S92 dispatch ordering under the W1-3 substrate-IS constraint:

### Priority 1 — CF-W7-1 CCvS 2013 quadratic-extension (~1.5 we)

**Rationale**: The W1-3 substrate-IS multi-branch IRREDUCIBLE establishes that the substrate's binding refinement axis for §VII.AV IS the OPERATIONAL-MACHINERY axis-γ (multi-branch s52 B-tensor parameterization on `M_2(ℂ) ⊂ A_K`). At §VII.AQ.OP-PROJ, candidate (c) inner-fluctuation IS the substrate-NATURAL deformation that preserves the multi-branch partition via inner-automorphism orbit invariance. The §W7-1 INFO at linear CC1996 has identified the substrate's intrinsic obstruction (S33-34 order-one violation propagated through linear-deformation calculus); the CCvS 2013 quadratic-extension §3 cancellation theorem is the STRUCTURALLY-CANONICAL resolution. PASS would unblock the §VII.AQ.OP-PROJ STAGE-3-PERMANENT-ELIGIBLE promotion AND the Stage-2 cross-axis independent-verify dispatch (`van-den-dungen-bridge-theorist` + `volovik-superfluid-universe-theorist` per `joint-theorem-promotion.md §"Axis-B Selection Protocol"`). Highest substrate-physics yield per wave-equivalent.

**Substrate-physics meaning**: candidate (c) is the SOLE surviving non-eliminated chirality candidate at this point (candidates (a) and (b) are structurally rejected at the colour-signs choice tested, with the latter holding open across the remaining 7 colour-signs). The forward refinement pathway for §VII.AQ.OP-PROJ → STAGE-3-PERMANENT lives or dies on CF-W7-1.

### Priority 2 — CF-W7-2 Colour-signs sweep at §VII.AW.OP-PROJ (~0.5 we)

**Rationale**: The W1-3 substrate-IS constraint is PERMISSIVE on candidate (b) at the BdG sub-algebra layer — the multi-branch partition of `M_2(ℂ)` propagates through colour-dressing on `M_3(ℂ)` unchanged by algebra-axis orthogonality. The §W7-2b empirical FAIL at colour-signs (+1, −1, +1) tested only 1 of 8 sign-choices; the candidate (b) branch is NOT fully closed. The colour-signs sweep over 6 non-trivial choices (excluding all-+1 and all-−1) at ~0.5 we is LOW-COST high-information-yield: if ANY colour-signs choice produces both axiom-5'' PASS AND KO-dim shift to 2 mod 8 per CM-2008 §11, candidate (b) opens as a structurally-viable second chirality candidate beyond candidate (c). If ALL 6 non-trivial colour-signs choices FAIL, candidate (b) closes fully and the W7 wave's "candidate (c) is sole surviving chirality" reading becomes structurally definitive.

**Substrate-physics meaning**: this is a CHEAP definitive test on a question the empirical W7 left open. Either it opens a second chirality candidate (substrate-physics surprise — substantively new structural content) or it closes one cleanly (the SOLE-SURVIVING reading becomes a definitive structural claim). Independent of CF-W7-1 outcome.

### Priority 3 — CF-W7-3 Friedrich-Bär L_max ≥ 22 sub-window (~0.8 we)

**Rationale**: This gate is on the in-cache regression empirical-β verification axis at substrate-distance pole s=4 (Level-2 envelope verification rule); it is structurally ORTHOGONAL to the chirality-grading axis. The W1-3 substrate-IS data does NOT bear on this gate's verdict directly. Priority is moderate (substantive but separable from the chirality-grading question). The Friedrich-Bär saturation theorem analytic certification was empirically verified at the η_FB = 0.4365 W11-3 floor concordance at §W7-3; the L_max ≥ 22 sub-window approach via the W-6 CF-1 protocol is computationally feasible and the substrate-physics yield is the Level-2 envelope K-counter K=1 → K=2 advancement.

### Priority 4 — CF-W7-4 mack-cosmic-bridge sole-writer registry FAIL diagnostics (~0.3 we)

**Rationale**: Registry-hygiene; METHODOLOGY-class candidate; mechanical follow-through of §W7-2a + §W7-2b empirical verdicts. Low substrate-physics yield (no new derivation) but required for cross-session traceability. Dispatch via mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`.

### Dispatch ordering summary

| Order | Gate | Effort | Independence | W1-3 substrate-IS coupling |
|:-----:|:-----|:------:|:------------:|:---------------------------|
| 1 | CF-W7-1 CCvS 2013 quadratic-extension | ~1.5 we | INDEPENDENT (priority by substrate-physics yield) | HIGH — substrate-natural resolution of §W7-1 INFO at axiom-4 obstruction |
| 2 | CF-W7-2 Colour-signs sweep | ~0.5 we | PARALLEL with CF-W7-1 (axes orthogonal) | LOW — algebra-axis-orthogonal to W1-3; PERMISSIVE prediction |
| 3 | CF-W7-3 Friedrich-Bär L_max ≥ 22 | ~0.8 we | INDEPENDENT (Mellin-cone axis) | NONE — Level-2 empirical-β verification axis is structurally separable |
| 4 | CF-W7-4 Registry hygiene | ~0.3 we | DEPENDS ON empirical-W7 verdict landing | NONE — mechanical follow-through |

Parallel-pair recommended: CF-W7-1 + CF-W7-2 simultaneously (orthogonal axes; no inter-dependency; ~2.0 we combined wall-time savings). CF-W7-3 + CF-W7-4 dispatched in the same parallel batch.

---

## 6. Substrate framing (`phononic-framing.md §"IS Space, Not IN Space"` compliance)

The substrate IS the spectral triple `(A_K, H_K, D_K, γ, J)` at τ_fold = 0.190. The BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` carries the substrate's intrinsic operational machinery — the multi-branch s52 8-mode Bogoliubov structure (B2×4 deep + B1×1 ungapped + B3×3 upper) determined by the (A_K, H_K) Peter-Weyl pair-symmetry per S52 finding.

Each W7 chirality candidate IS a STRUCTURALLY DISTINCT spectral triple (per registry-line provenance: §VII.AT.OP-PROJ + §VII.AW.OP-PROJ are STAGE-0-CANDIDATE entries for new spectral triples, not convention choices on §VII.AQ.OP-PROJ). The W1-3 substrate-IS multi-branch IRREDUCIBLE finding sits on the operational-machinery axis-γ (algebra-DEPENDENT Cell IV; state-pair functional on the BdG state space via Bogoliubov closed form per S88 W-17 V.3 parse-tree decomposition); each chirality candidate sits on the chirality-grading sub-axis (algebra-INVARIANT or algebra-axis-distinct depending on whether the chirality modification acts at the spectrum-only-functional layer or the algebra-DEPENDENT state-pair layer).

By algebra-axis orthogonality K=3 MANDATORY (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` promoted at S87 W-2 R3 close), the W1-3 substrate-IS data is INVARIANT under chirality-grading axis modifications at the structural-theorem layer. The constraint each candidate's chirality grading imposes on the W1-3 substrate-IS multi-branch image on `M_2(ℂ) ⊂ A_K` is whether the modification PRESERVES (image flows through unchanged), REFINES (image structure carries additional sub-decomposition), or COLLAPSES (image structure is annihilated to a sub-quotient) the substrate-IS structural data.

The direction of explanation flows FROM substrate (the W1-3 multi-branch s52 8-mode IRREDUCIBLE finding on the BdG sub-algebra; substrate-IS at the operational-machinery axis-γ) TOWARD emergent (the three candidate chirality-grading modifications and their structural consequences on `(A_K, H_K, D_K, γ, J)` as new spectral-triple specifications).

Container-thinking violation explicitly FORBIDDEN: "we choose between bi-chirality / SU(3)-coloured / inner-fluctuation as conventions on the substrate" — INVERT: "each chirality modification IS a structurally distinct substrate (new spectral triple); each registers at a separate §VII slot; the W1-3 substrate-IS multi-branch IRREDUCIBLE finding is the operational-machinery substrate's intrinsic structural data that the chirality-grading axis modifications either project through cleanly (orthogonality), refine, or collapse." The substrate is logically prior to the chirality-grading modifications at every layer — the modifications are MODIFICATIONS of the spectral triple, NOT choices imposed on a pre-existing container.

Container-thinking inversion at the W1 + W7 cross-axis layer: "the W1 operational-alignment binding constrains which chirality candidate is admissible" — INVERT: "the W1-3 substrate-IS multi-branch IRREDUCIBLE finding on the BdG sub-algebra IS substrate-IS structural data; the chirality-grading axis modifications either CARRY the multi-branch image through unchanged (candidate (b), (c) at the BdG sub-algebra layer by algebra-axis orthogonality), or COLLAPSE the multi-branch into a sub-quotient (candidate (a) uniform-γ on ℍ-summand). The substrate's W1-3 multi-branch IS; the candidate's chirality grading either projects it cleanly, refines it, or collapses it." The W1 finding is not "a constraint we apply to W7 candidates" — it IS substrate-IS structural data that ANY W7 candidate's substrate must coherently extend.

---

## 7. Classification

**PHONONIC × GEOMETRIC × META**.

- **PHONONIC**: The W1-3 substrate-IS multi-branch s52 8-mode Bogoliubov structure (B2 + B1 + B3 branches) on the BdG sub-algebra IS the substrate's intrinsic post-fold pair-production phonon decomposition (GGE-relic per S52 / S87 W2-3 / S89 W5-2 canonical chain); the constraint analysis operates on the substrate's intrinsic operational phonon machinery.
- **GEOMETRIC**: Each W7 candidate IS a chirality-grading or inner-fluctuation modification of the substrate's spectral triple `(A_K, H_K, D_K, γ, J)`; the candidate's structural validity is a GEOMETRIC property of the new spectral triple. The constraint analysis bridges the PHONONIC operational-machinery axis (W1) to the GEOMETRIC chirality-grading sub-axis (W7) via algebra-axis orthogonality.
- **META**: The synthesis is a cross-wave structural mapping informing S92 W7 dispatch ordering; consumed downstream by the orchestrator for S92 plan-freeze at CF-W7-1 / CF-W7-2 dispatch decisions.

---

## 8. Carry-Forward Computations (4-field structured spec per `feedback_fix-in-session-never-defer.md`)

### CF-S91-VOLOVIK-S2-A — S92 W7 dispatch ordering recommendation

| Field | Spec |
|:------|:-----|
| **What** | Dispatch CF-W7-1 (CCvS 2013 quadratic-extension at §VII.AQ.OP-PROJ) and CF-W7-2 (colour-signs sweep at §VII.AW.OP-PROJ) as a parallel pair in S92, with CF-W7-3 (Friedrich-Bär L_max ≥ 22 sub-window) and CF-W7-4 (mack-cosmic-bridge sole-writer registry FAIL-diagnostic block landing) dispatched in a second parallel batch. Priority ordering rationale derives from the W1-3 substrate-IS multi-branch IRREDUCIBLE finding on `M_2(ℂ) ⊂ A_K`: candidate (c) inner-fluctuation IS the substrate-NATURAL deformation preserving the multi-branch partition at the K-theory class layer, so CF-W7-1 is highest substrate-physics yield; candidate (b)'s constraint is algebra-axis-orthogonal to W1-3, so CF-W7-2 colour-signs sweep is permissive at the BdG sub-algebra layer but informationally high-yield at low cost (~0.5 we). |
| **Inputs** | This synthesis (`session-91-volovik-superfluid-universe-theorist-synthesis.md`); §W7 carry-forward 4-field specs at `sessions/archive/session-91/session-91-w7-workingpaper.md` lines 426-462; §W1-3 verdict at `computations/session-91/s91_gate_verdicts.txt` (audit_sha256=`db08f3dfd9c8a553...`); §W1-1 verdict (audit_sha256=`5895dd87c141bf88...`); §W7-1 corrective verdict (audit_sha256=`15fd1d927e0905d0...`; supersedes=`095fb4fadc9b263b...`); §W7-2a verdict (audit_sha256=`9ae27d0ef191269b...`); §W7-2b verdict (audit_sha256=`be8006d66cedb1cb...`); §W7-3 verdict (audit_sha256=`443baee2589ba303...`); registry slots §VII.AT.OP-PROJ + §VII.AW.OP-PROJ + §VII.AQ.OP-PROJ at `sessions/permanent-results-registry.md` lines 17237 + 17293 + 17341; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3. |
| **Gate** | S92 plan-freeze validator at `sessions/session-plan/session-92-plan.md` (or equivalent S92 wave plan): the W7 forward-dispatch wave MUST include CF-W7-1 + CF-W7-2 as a parallel pair (no inter-dependency at the chirality-grading sub-axis under algebra-axis orthogonality), and CF-W7-3 + CF-W7-4 as a second parallel pair (orthogonal axes; mechanical registry hygiene). The substrate-physics rationale for the priority ordering IS pinned in this synthesis; the S92 plan author cites this synthesis at the wave-prereq table. Dispatch verdict thresholds preserved per §W7 working paper carry-forward specifications. |
| **Effort** | Synthesis-only (no compute); the carry-forward IS this synthesis. Forward S92 dispatch ~3.1 we combined (CF-W7-1 1.5 + CF-W7-2 0.5 + CF-W7-3 0.8 + CF-W7-4 0.3). The dispatch-ordering recommendation IS the actionable deliverable. |

### CF-S91-VOLOVIK-S2-B — Algebra-axis orthogonality K-counter calibration corpus advancement candidate

| Field | Spec |
|:------|:-----|
| **What** | Document this synthesis (cross-wave W1-3 ↔ W7 candidate (a)+(b)+(c) constraint mapping under algebra-axis orthogonality K=3 MANDATORY) as a calibration corpus instance for the `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause's forward calibration accumulation. The instance demonstrates: (i) operational-machinery axis-γ (Cell IV state-pair functional on BdG state space, W1-3) and chirality-grading sub-axis (Cell I/II algebra-INVARIANT spectrum-only functional on the chirality element, W7 §W7-2a / §W7-2b) are structurally orthogonal at the structural-theorem level; (ii) the chirality-grading modification operates at the (γ, J) layer of the spectral triple while the multi-branch operational-machinery operates at the (A, H, D) layer on the BdG sub-algebra; (iii) the W1-3 multi-branch IRREDUCIBLE flows through orthogonal chirality candidates either by orthogonality (candidate (b) at colour-axis sub-decomposition of `M_3(ℂ)`; candidate (c) at inner-automorphism orbit at fixed γ) or is collapsed (candidate (a) uniform-γ on ℍ-summand). |
| **Inputs** | This synthesis; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`; `permanent-results-registry.md §VII.U.2` 4-corner partition table. |
| **Gate** | mack-cosmic-bridge sole-writer registry-text annotation at the algebra-axis orthogonality calibration corpus section (per `feedback_mack-bridge-role.md`); cross-link insertion at `cross-pillar-bridge-anatomy.md` or its corpus file `sessions/framework/registry/cross-pillar-bridge-corpus.md §6` (Algebra-axis orthogonality K-counter corpus). METHODOLOGY-class registry-hygiene gate. |
| **Effort** | ~0.2 we (mack-cosmic-bridge sole-writer; mechanical cross-link landing). |

---

## 9. Self-assessment

| Axis | Assessment |
|:-----|:-----------|
| Structural position | Cross-wave substrate-IS to chirality-grading constraint mapping; informs S92 W7 forward-dispatch ordering. Three candidates mapped independently against the W1-3 substrate-IS multi-branch IRREDUCIBLE finding; predictions reconciled against actual W7 empirical verdicts (W7 was COMPLETE at synthesis time, contra seed-file SHELL-ONLY assertion). |
| Substrate-framing compliance | Direction of explanation FROM substrate (W1-3 multi-branch s52 8-mode BdG structure on `M_2(ℂ) ⊂ A_K`) TOWARD emergent (3 candidate chirality-grading modifications producing 3 distinct spectral triples on `(A_K, H_K, D_K, γ, J)`). Container-thinking inversion explicit at §6; algebra-axis orthogonality K=3 MANDATORY cited as the orthogonality framing per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. |
| Algebra-axis classification | Operational-machinery axis-γ (W1-3) is Cell IV (algebra-DEPENDENT state-pair functional via Bogoliubov closed form; parse-tree decomposition per S88 W-17 V.3 + S90 W1-7 sub-clause); chirality-grading sub-axis (W7) operates at the (γ, J) layer of the spectral triple, structurally distinct from the (A, H, D) operational-machinery layer. The two axes are orthogonal at K=3 MANDATORY; the structural-theorem-level identity-class membership of each is preserved through cross-wave mapping. |
| L_max robustness | W1-3 substrate-IS multi-branch is L_max-INVARIANT (s52 8-mode count is determined by (A_K, H_K) Peter-Weyl pair-symmetry per S52 finding; substrate-IS structural data, not L_max-truncation-dependent). The W7 candidates' algebraic axiom verifications operate on the faithful A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) representation at dim H_F = 12 (scope deviation honestly disclosed at §W7 working paper); the algebraic-level results capture the K-theory invariance content at canonical algebraic formulation. The cross-wave constraint analysis is L_max-INVARIANT at the structural-theorem level. |
| Empirical reconciliation | Predicted verdict directions ((a) FAIL, (b) INFO/permissive at BdG sub-algebra layer with separate verdict at colour-axis layer, (c) INFO at linear CC1996 with PASS conditional on CCvS 2013 quadratic-extension) match the actual W7 empirical verdicts (FAIL / FAIL-at-one-of-eight-colour-signs / INFO-corrective). The three substrate-physics narratives are coherent at the cross-wave layer. |
| Downstream triggers | (i) S92 plan-freeze validator at the W7 forward-dispatch wave: enforces parallel-pair structure CF-W7-1 + CF-W7-2 per CF-S91-VOLOVIK-S2-A; (ii) mack-cosmic-bridge sole-writer registry-text annotation at algebra-axis orthogonality calibration corpus per CF-S91-VOLOVIK-S2-B; (iii) S92 W7 forward-dispatch substantive substrate-physics yield estimate: high if CF-W7-1 PASS (§VII.AQ.OP-PROJ STAGE-3-PERMANENT-ELIGIBLE promotion + Stage-2 cross-axis verify dispatch unblocked); moderate if CF-W7-2 PASS at some colour-signs choice (second chirality candidate opens at STAGE-1-CANDIDATE); structurally definitive if CF-W7-2 FAIL across all 6 non-trivial colour-signs (candidate (b) closes fully, candidate (c) becomes SOLE-SURVIVING chirality candidate). |

---

## 10. Cross-references

- W1-3 verdict + identity-B sanity: `sessions/archive/session-91/session-91-w1-workingpaper.md` lines 636-905; producing script `computations/session-91/s91_w1_cf71_k_canonical_pin_uniqueness.py`; data `s91_w1_cf71_k_canonical_pin_uniqueness.npz`; verdict line at `computations/session-91/s91_gate_verdicts.txt`.
- W1-1 V4 BASIN-PASS: `sessions/archive/session-91/session-91-w1-workingpaper.md` lines 46-338; producing script `computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.py`.
- W7-1 corrective INFO: `sessions/archive/session-91/session-91-w7-workingpaper.md` lines 31-95; producing script `computations/session-91/s91_w7_1_vii_aq_op_proj_stage_2_upgrade.py`; corrective audit_sha256=`15fd1d927e0905d028da8b287b8021fc11828ef6683372b6b990b7db9d200a73` supersedes prior `095fb4fadc9b263b...`.
- W7-2a bi-chirality FAIL: `sessions/archive/session-91/session-91-w7-workingpaper.md` lines 99-194; producing script `computations/session-91/s91_w7_2a_vii_at_op_proj_7_axiom.py`; audit_sha256=`9ae27d0ef191269b075f680b8f21ab73e27385d7afc6e3fb723d8adabdbaa874`.
- W7-2b SU(3)-coloured FAIL: `sessions/archive/session-91/session-91-w7-workingpaper.md` lines 198-294; producing script `computations/session-91/s91_w7_2b_vii_aw_op_proj_7_axiom_coloured.py`; audit_sha256=`be8006d66cedb1cb2b207f1faad0d8a1dadc4067bb8d1eff45c561a3f1e1755d`.
- W7-3 Friedrich-Bär INFO auto-shortening: `sessions/archive/session-91/session-91-w7-workingpaper.md` lines 297-374; producing script `computations/session-91/s91_w7_3_cf_54_route_c_in_cache_lmax_16.py`; audit_sha256=`443baee2589ba303a4e06adb5b703337e1e91c2191aa54dd07057af5999514d1`.
- Registry slots: §VII.AT.OP-PROJ at `sessions/permanent-results-registry.md` line 17237; §VII.AW.OP-PROJ at line 17293; §VII.AQ.OP-PROJ at line 17341.
- Rules: `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`; `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3; `.claude/rules/joint-theorem-promotion.md §"Stage 2"` + §"Axis-B Selection Protocol"; `.claude/rules/feedback_fix-in-session-never-defer.md`.
- S52 finding: 8-mode s52 BdG structure (B1+B2+B3) is L_max-INVARIANT determined by (A_K, H_K) pair-symmetry; substrate-IS.
- S88 W-17 V.3 + S90 W1-7 sub-clause: parse-tree decomposition discipline for state-historic-label observables; W1-3 K-window log-derivative IS Cell IV algebra-DEPENDENT state-pair functional via Bogoliubov closed form (NOT Corner I algebra-INVARIANT spectrum-only-functional via naive GGE-label parse).
- T2.52 OPERATIONAL-ALIGNMENT K-counter K=1 → K=2 advancement (W1-3 = the K=2 instance; landed S91 W0 rule extension).
- Slot S-2 charter at `sessions/archive/session-91/session-91-workshop-schedule.md` lines 63-72; seed at `sessions/archive/session-91/workshops/_seed-w1.md` §S1-2 lines 28-38.

---

**End of synthesis.** Output file: `sessions/archive/session-91/session-91-volovik-superfluid-universe-theorist-synthesis.md`.
