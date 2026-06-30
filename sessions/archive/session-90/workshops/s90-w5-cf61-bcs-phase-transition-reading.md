# Session 90 Workshop: volovik x connes

**Date**: 2026-05-16
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: volovik (volovik-superfluid-universe-theorist), connes (connes-ncg-theorist)
**Source Documents**:
- `sessions/archive/session-90/session-90-w8-workingpaper.md`
- `.claude/rules/mechanical-closure-discipline.md`
- `.claude/rules/cross-pillar-bridge-anatomy.md`
- `.claude/rules/phononic-framing.md`
- `sessions/permanent-results-registry.md`
- `sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md`

**Focus Topics** (CF-61 BCS PHASE TRANSITION READING: SUBSTRATE-PHYSICS STRUCTURAL FINDING vs OPERATIONAL-PARAMETERIZATION ARTIFACT):

W8 CF-61 (`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS`) FAIL revealed: on the L_max-truncated D_K² spectrum at canonical (V_BCS, T_fold = 0.640), the BCS gap equation admits ONLY trivial Δ=0 solution for L_max ∈ {6..10}; only L_max ∈ {11, 12} produce finite gap (Δ=0.1062 at L_max=11; Δ=0.4643 at L_max=12 by V_BCS calibration). α=nan, R²=nan (only 1 non-degenerate data point survives BCS phase boundary). L_max=12 FULL-BdG anchor mismatch 1.428 ≫ 1e-9 vs canonical −7.046336 (scalar-Δ gap-equation vs s52 multi-branch Δ_per_mode structural mismatch).

**Competing readings**:

- **Reading A (volovik / substrate-physics structural)** — L_max-truncated spectrum literally does not have enough spectral kernel weight to support finite gap at canonical coupling; STRUCTURAL substrate finding (BCS phase transition at spectral-cutoff axis); §W5-3 Casimir-bound SCHEMATIC proxy `Δ_eff(L) = Δ_static · sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` was smooth-interpolation ansatz that SMOOTHED OVER real phase boundary; forward implication: §VII.AV proxy-refinement MUST switch to structurally-different machinery (CF-70 FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers with W3 A.14 regulator-INVARIANT cocycle ratio as cross-anchor); Casimir-bound proxy class STRUCTURALLY CLOSED.

- **Reading B (connes / operational-parameterization)** — L_max=12 FULL-BdG re-derivation uses single scalar Δ from gap-equation self-consistency, whereas canonical §W5-2 anchor `L_emp(L_max=12) = −7.046336474406761` was computed against multi-branch Δ_per_mode structure from s52 ED solution (B1=0, B2=0.7704, B3=0.176); both routes compute same Cell IV substrate-IS observable (variance of Bogoliubov occupation at K_horizon) on `M_2(ℂ) ⊂ A_K` but through different operational machineries; FULL-BdG anchor mismatch 1.428 is structural mismatch BETWEEN operational routes, NOT substrate phase transition; forward implication: §VII.AV refinement should investigate K_canonical pin uniqueness (CF-71) and align FULL-BdG operational route with multi-branch s52 Bogoliubov structure; Casimir-bound proxy class may remain admissible IF alignment succeeds.

Per `mechanical-closure-discipline.md §"Layer-separability carve-out"` L1-L4, substrate-IS observable IS K-window log-derivative on `M_2(ℂ)` Type-F per CF-62 disambiguation: Reading A says L_max-dependence of that Type-F observable IS phase-transition-discontinuous on substrate; Reading B says it is smooth on substrate but operational machinery introduces artificial discontinuity. The two readings yield INCOMPATIBLE forward dispatch priorities (CF-70 vs CF-71) and incompatible registry-text framings of WHY §VII.AV is REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT.

**Adjudication questions**:

1. **(a)** Does the L_max ≤ 10 trivial-Δ solution represent a STRUCTURAL phase transition at the spectral-cutoff axis (Reading A), or an OPERATIONAL artifact of scalar-Δ gap-equation self-consistency on a multi-branch problem (Reading B)?
2. **(b)** Does the L_max=12 FULL-BdG anchor mismatch (1.428 ≫ 1e-9 vs canonical −7.046) reflect a substrate-physics structural difference (Reading A: phase boundary structurally distinct from canonical multi-branch domain) or an operational-machinery alignment defect (Reading B: scalar-Δ-vs-multi-branch operational route mismatch on same substrate observable)?
3. **(c)** Under each reading, which §VII.AV refinement pathway is structurally licensed: CF-70 (Connes-Chamseddine multipliers) or CF-71 (K_canonical pin uniqueness) — and is the OTHER pathway structurally CLOSED or merely deferred?
4. **(d)** What is the discriminator-gate that PASS/FAILs cleanly between Reading A and Reading B in S91+? Candidate: `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` — does the L_max=12 multi-branch s52 ED reproduce canonical anchor at any (B1, B2, B3) configuration matching scalar-Δ FULL-BdG output?
5. **(e)** Substrate framing per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`: does the BCS phase transition at L_max=10/11 represent a Level-1 single-τ-slice substrate-IS structural property OR a Level-2 moduli-deformation property that lifts under τ-extension (CF-69 in W8 WP queues τ ∈ {0.18, 0.19, 0.20} extension)?

**Pre-registered structural verdict options** (per schedule OUTPUT clause):

- **(a) Reading A canonical** — §VII.AV registry-text annotation lands "Casimir-bound proxy class STRUCTURALLY CLOSED" with CF-70 prioritized (Connes-Chamseddine multipliers) at S91+; CF-71 demoted to deferred.
- **(b) Reading B canonical** — §VII.AV registry-text annotation lands "operational-parameterization mismatch resolved via CF-71 alignment" with CF-71 prioritized (K_canonical pin uniqueness) at S91+; CF-70 deferred pending CF-71 outcome.
- **(c) Both readings structurally distinct, refinement pathway space carries both** — §VII.AV refinement pathway space documents BOTH CF-70 and CF-71 as independent forward routes; pre-registered S91+ discriminator-gate fires first to determine which reads (Reading A vs Reading B) dominates; both pathways admissible until discriminator-gate resolves.
- **(d) Hybrid: substrate phase boundary AT operational-machinery joint layer** — both readings partially-correct; the L_max ≤ 10 trivial-Δ regime IS a substrate-IS phase boundary (Reading A) AND the L_max=12 anchor mismatch IS an operational-machinery artifact (Reading B); §VII.AV refinement pathway space adopts CF-70 + CF-71 wave-together at S91+ with discriminator-gate first.

**Note on OAA exclusion (per schedule line 230)**: OAA exclusion does NOT apply for this workshop — the workshop's structural object IS the substrate-physics interpretation of volovik + connes's own joint gate (CF-61). The adversarial axis IS the divergence in their original framings, surfaced explicitly. Both authoring agents are inside the structural object.

**Cross-link to W-1 + W-2 + W-3 + W-4 cross-workshop K=4 pattern**: this workshop is the 5th sequential Slot 2 dispatch at S90; advancing the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern toward K=5 MANDATORY promotion candidate per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold. If W-5 closes with cross-axis JOINT-WIN, the K-counter advances K=4 → K=5 MANDATORY.

---

## Round 1 — volovik: Opening Analysis

### V1: Trivial-Δ solution (L_max ≤ 10) — substrate-physics STRUCTURAL phase transition reading

**Claim**: At the canonical (V_BCS, T_fold = 0.640) pin, the L_max-truncated D_K² spectrum at L_max ∈ {6, 7, 8, 9, 10} literally does not have enough spectral kernel weight to support a finite BCS gap. The L_max = 10 → 11 transition IS a substrate-IS phase boundary at the spectral-cutoff axis — a STRUCTURAL property of the substrate's finite spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L}(τ_fold))`, not an operational artifact of scalar-Δ gap-equation machinery. The §W5-3 Casimir-bound SCHEMATIC proxy `Δ_eff(L) = Δ_static · sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` is a smooth-interpolation ansatz that SMOOTHS OVER this discontinuity at the algebraic-envelope layer; the FULL re-derivation reveals the substrate's intrinsic step.

**1. The BCS gap equation on the truncated spectral triple IS substrate-IS, not container-thinking**

Per `phononic-framing.md §"IS Space, Not IN Space"` MANDATORY direction-of-explanation: the substrate IS the finite spectral triple at τ_fold = 0.19; the BCS gap equation `Δ = V_BCS · Σ_a m_a · tanh(βE_a/2) / (2 E_a)` with `E_a = sqrt(λ_a² + Δ²)` and {λ_a, m_a} running over the L_max-truncated D_K² eigenvalues (per the W8-3 spectrum table at lines 333-341: |λ|_min = 0.819741 L_max-invariant, |λ|_max sweeping 5.160371 → 5.418937 across L_max ∈ {6..12}) IS the self-consistency condition of a substrate-IS gap on the substrate's intrinsic spectral kernel. It is NOT a self-consistency equation "in" an external container that gets refined as L_max increases — L_max IS the substrate's own spectral cutoff under the Peter-Weyl decomposition, refining toward the cohomology-class image at HKR `L_max → ∞`.

The empirical evidence reported at WP §W8-3 Step 3 (lines 357-365) is decisive: gap-equation bisection converges to `Δ(L_max=10) = 0.0000000000` with residual `−1.217e+05` after 2903 iterations (the maximum permitted); `Δ(L_max=11) = 0.1062` with residual `−1.024e-08` after 45 iterations; `Δ(L_max=12) = 0.4643` (canonical BCS aliased to Δ_0_OES, per get_constant("Delta_BCS")=0.4642547394830737) with residual `−2.383e-06` after 42 iterations. The convergence pattern itself is substrate-IS information: at L_max ≤ 10 the gap equation has ONLY the trivial fixed point (the bracket bisection drives Δ to 0 because the kernel sum `Σ_a m_a · tanh(βE_a/2) / (2 E_a)` evaluated at finite Δ is structurally smaller than 1/V_BCS for the truncated spectrum). This is a Cooper-pair-instability criterion failing at the substrate's intrinsic spectral kernel restricted to L_max ≤ 10.

**2. Why the spectral kernel weight is structurally insufficient (Volovik / Khodel-Shaginyan microscopic physics)**

The BCS critical-coupling threshold in the substrate microscopic Hamiltonian formulation is:
```
1/V_BCS = Σ_a^{L_max} m_a · tanh(λ_a / (2 T_fold)) / (2 λ_a)        [Δ → 0 limit of the gap equation]
```
where the LHS at canonical V_BCS = 2.447e-7 M_KK^{−1} (calibrated at L_max=12 to reproduce Δ_BCS = 0.4642547) gives `inv_V_BCS = 4086524.798`. The truncated-spectrum kernel sums (Volovik Papers 16/17/18 flat-band Δ ~ g·N(0) linear-condensation framework; Khodel-Shaginyan condensation): per the W8-3 Step 2 spectrum accounting (lines 333-341), the L_max=10 weighted-eigenvalue count is 30,593,872 vs 31,956,720 at L_max=12 — the missing 4.3% of UV weight (sectors with p+q = 11, 12) is structurally critical for the kernel sum to cross 1/V_BCS at the canonical T_fold. This IS the Volovik flat-band condensation criterion at the spectral-truncation axis: the substrate's intrinsic Cooper-instability threshold sits between the L_max=10 and L_max=11 spectral cutoffs at the canonical pin, NOT smoothly across them.

The translation to the project's cosmological convention (BCS condensate on SU(3) as spectral-action vacuum, per memory's microscopic-to-emergent mapping table): the L_max ≤ 10 truncation does not retain enough of the SU(3) Peter-Weyl content above the |λ|_min = 0.819741 floor to drive condensation at the canonical pin. The substrate's BCS phase transition at the spectral-cutoff axis is the inheritance-class structural manifestation of the parent 3He-B (BDI, N_3 = 0) Cooper instability — child-realization of the parent superfluid criticality — at the finite spectral-triple layer of the framework.

**3. The §W5-3 Casimir-bound SCHEMATIC proxy is STRUCTURALLY FALSIFIED at this phase boundary**

Per `mechanical-closure-discipline.md §"Layer-separability carve-out"` L1-L4 + per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline + per the deferred-pending PROXY-REFINEMENT sub-class at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`: the §W5-3 Casimir-bound proxy `Δ_eff(L) = Δ_static · sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` is a SCHEMATIC closed-form that satisfies L2 (closed-form algebraic identity) but VIOLATES L1 (Layer-functor F decomposition cleanness) when the FULL physical pipeline reveals discontinuous behavior. The proxy's smoothness in C_2(L,L) is structurally incompatible with the substrate's discontinuous Cooper-instability criterion at L_max ≤ 10 → L_max ≥ 11.

The substitution chain `Δ_proxy(L_max=10) / Δ_proxy(L_max=12) = sqrt((C_2(10,10)+1)/(C_2(12,12)+1)) = sqrt(221/337) ≈ 0.810` predicts `Δ_proxy(10) ≈ 0.376` (about 81% of canonical). The FULL re-derivation returns `Δ(10) = 0.0000` — a 100% discrepancy. Per the L4 honesty-disclosure clause, the SCHEMATIC proxy was carried under `convention=...-SCHEMATIC` tag; the FULL refinement reveals that the SCHEMATIC ansatz was not just numerically imprecise but STRUCTURALLY WRONG-CLASS: it interpolated through a substrate-IS phase boundary the FULL physical pipeline cannot. This is a stronger statement than "the SCHEMATIC value disagrees with the FULL value by some margin"; it is "the SCHEMATIC functional form (smooth in C_2) cannot represent the substrate-IS observable (discontinuous in L_max at the Cooper-instability threshold) at the canonical pin".

**4. Forward question for connes**

Under your Reading B (operational-parameterization), the L_max ≤ 10 trivial-Δ result is a consequence of scalar-Δ vs multi-branch operational asymmetry. But the multi-branch s52 ED solution (B1=0, B2=0.7704, B3=0.176) at L_max=10 was constructed on the L_max=10 spectrum using the SAME spectral kernel weights the gap equation sees. From the Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula perspective: under what NCG-axiomatic argument does the multi-branch s52 Bogoliubov problem at L_max=10 evade the kernel-weight insufficiency that defeats the scalar-Δ gap equation at the same L_max? If the answer is that s52 ED imposes B-amplitudes externally (e.g., as fixed-point solutions of an L_max=12 problem then truncated, rather than self-consistently solved at L_max=10), then the s52 anchor is NOT computing the same substrate-IS observable as the FULL gap equation at L_max=10 — and the anchor mismatch 1.428 is informative about WHICH operational route is substrate-IS-faithful at the spectral-cutoff axis. Cite the K-theory / Connes-Karoubi pairing structure that bridges the multi-branch s52 ED route to a Level-1 cohomology-class identity at HKR `L_max → ∞`; if no such pairing exists at L_max ≤ 10, the s52 route IS structurally an L_max=12 ansatz, and the scalar-Δ gap-equation FULL re-derivation IS the substrate-IS-faithful pipeline at the cohomology-class layer.

### V2: L_max=12 FULL-BdG anchor mismatch 1.428 — substrate-physics structural difference reading

**Claim**: The L_max=12 FULL-BdG anchor mismatch (`L_emp_FULL(12) = −5.6188` vs canonical `L_emp(L_max=12) = −7.046336474406761`; `|diff| = 1.428e+00 ≫ 1e-9` per W8-3 Step 6 lines 402-416) is NOT an operational alignment defect to be eliminated by tuning K_canonical (Reading B's CF-71 path). It is a SUBSTRATE-PHYSICS structural separation between two distinct substrate-IS regimes that the BCS phase transition at L_max=10/11 makes intrinsic: (i) the canonical multi-branch post-phase-transition domain (B1=0, B2=0.7704, B3=0.176 per s52 ED, applied at L_max=10 / canonical at S87 W2-3); (ii) the scalar-Δ FULL-BdG phase-boundary domain (Δ(12)=0.4643 from gap-equation self-consistency at the only post-transition L_max in the scan). The anchor mismatch is the substrate's signature of these regimes' STRUCTURAL non-equivalence, NOT a defect of operational tuning.

**1. The two operational routes compute structurally DISTINCT observables at the substrate-IS layer**

Per W8-3 Step 4 (lines 374-388): the FULL re-derivation at L_max=12 applies a UNIFORMLY rescaled scalar `Δ(L_max=12) = 0.4643` across all 8 BdG modes (B1+B2+B3 sectors), with rescale factor `Δ(L_max)/Δ_static = 0.4643/0.7704 = 0.6026` — meaning every per-mode |Δ_a| is uniformly attenuated to 60.26% of its s52 ED value. The §W5-2 canonical anchor `L_emp(L_max=12) = −7.046336474406761` was computed against the un-rescaled s52 multi-branch amplitudes directly. The two observables are:

- **Route A (FULL-BdG, this gate)**: `L_emp(12)_FULL = d² ln P_GGE / d(ln K)² |_{K_horizon}` computed with Bogoliubov amplitudes `{v_a^2 = (1 − ε_a/E_a)/2}` where `E_a = sqrt(ε_a² + Δ_canonical²)` and Δ_canonical = 0.4643 is the SCALAR self-consistent gap. The Bogoliubov-state covariance lives on a substrate state-space defined by a single condensate-scale Δ.

- **Route B (s52 canonical, §W5-2)**: `L_emp(12)_s52 = d² ln P_GGE / d(ln K)² |_{K_horizon}` computed with multi-branch `{v_a^{(B1)}, v_a^{(B2)}, v_a^{(B3)}}` per the s52 ED solution at L_max=10 (then evaluated on the L_max=12 kernel under fixed B1=0, B2=0.7704, B3=0.176 ratio structure). The Bogoliubov-state covariance lives on a substrate state-space with multiple independent condensate branches.

These ARE the same Cell-IV substrate-IS observable family (`Var_a(n_a^GGE)` parse-tree per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"` reduces both to the closed form `(1/N) Σ_a m_a · v_a^4 − ((1/N) Σ_a m_a · v_a^2)^2`), BUT they are evaluated on STRUCTURALLY DISTINCT Bogoliubov-amplitude tensors. The substrate-IS observable's *value* depends on which Bogoliubov-amplitude tensor it is evaluated against — and the two tensors inhabit different substrate regimes.

**2. The two regimes ARE structurally distinct by the BCS phase transition**

Reading A's substantive claim from V1 — that the L_max ≤ 10 trivial-Δ region is a substrate-IS phase boundary at the spectral-cutoff axis — implies that L_max=12 is the ONLY post-transition L_max in the FULL re-derivation scan. The s52 anchor at L_max=10 was constructed on the pre-transition spectrum (where the scalar-Δ gap equation has NO finite solution at canonical V_BCS) using B-amplitudes IMPORTED from a problem at higher kernel weight (an ED solution carrying B1=0, B2=0.7704, B3=0.176 that does NOT satisfy the gap equation at L_max=10 at canonical V_BCS). The s52 anchor at L_max=12, by analogy, is constructed by applying the SAME B-ratio structure on the L_max=12 spectrum — preserving multi-branch tensor structure across the phase boundary.

The FULL gap-equation route, by contrast, SELF-CONSISTENTLY solves at L_max=12 under canonical V_BCS and returns the scalar `Δ(12) = 0.4643`. The self-consistency forces a UNIFORM rescale: the Bogoliubov problem on the L_max=12 spectrum at the canonical pin has a single condensate-scale solution; the multi-branch B1/B2/B3 structure of s52 does NOT self-consistently arise from the gap equation on the L_max=12 spectrum at canonical V_BCS.

The substrate-IS reading: at the canonical pin, the L_max=12 substrate admits TWO inequivalent Bogoliubov-amplitude tensors as substrate-IS observables — one self-consistent with the gap equation (scalar Δ = 0.4643), one inherited from the s52 multi-branch ED solution (B1=0, B2=0.7704, B3=0.176). These are STRUCTURALLY DISTINCT substrate regimes, NOT alignable by K_canonical pin uniqueness. The 1.428 mismatch is the substrate's signature of this structural distinction at the K-window log-derivative observable layer.

**3. Engagement with Reading B's likely counter-claim (same substrate observable, different operational machineries on M_2(ℂ))**

Per CF-62 disambiguation (`S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION` PASS, audit_sha `8b4bfdee600fceb7…` per W8-4 lines 583-589): the canonical substrate-IS Element-1 for §VII.AV is the K-window log-derivative `R_KW(τ_fold) = d ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})) / d ln(K_window)` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` — a single-summand-projection trace on `M_2(ℂ)` under the layer-separability carve-out Type-F classification (mechanical-closure-discipline.md L1-L4). Connes's Reading B will argue: the K-window log-derivative IS a single substrate-IS observable on `M_2(ℂ)`; the two operational routes (FULL-BdG scalar-Δ vs s52 multi-branch ED) evaluate it under different `P_BdG` projector implementations on the BdG sub-algebra image.

**Counter-engage**: under W8-3 gen-physicist adversarial Q3 (lines 511-512) — explicitly cited at W8-3 line 511 — both routes "BOTH compute the same Cell IV substrate-IS observable (variance of Bogoliubov occupation at K_horizon) on the substrate algebra `A_K`, but they evaluate it on different operational machineries". Connes is correct that the observable is the same at the parse-tree-expansion layer (Var_a closed-form Cell-IV per §VII.U.2 Corner II corrigendum line 12961, lifted to Cell-IV under the K-window log-derivative state-pair functional family). But the SAME observable evaluated on STRUCTURALLY DISTINCT Bogoliubov-amplitude tensors at the canonical pin produces STRUCTURALLY DISTINCT numerical results IFF the two tensors inhabit different substrate regimes — which is precisely what the BCS phase transition at L_max=10 → 11 ESTABLISHES.

The analogy to the §VII.AQ Reading A vs Reading B precedent (S89 W5; `s89-w5-vii-aq-level3-binding.md` verdict table line 1163) is structural: there too, the "same substrate-IS observable" admits two structural readings at different MACHINERY SCOPES (full-leaf-foliation vs |λ|-only cache); the resolution route was a substrate-physics discriminator gate (`S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR`, deliverable α, 1.0 wave-equiv). The §VII.AV case admits the same epistemic structure: Reading A vs Reading B at different OPERATIONAL ROUTES on the same observable; the resolution route is `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` (V4 below) — substrate-physics adjudication, NOT workshop-internal argument.

**4. Forward question for connes**

The K-window log-derivative on `M_2(ℂ) ⊂ A_K` is a single-summand-projection trace under the layer-separability carve-out Type-F classification. The W8-3 line 511 gen-physicist Q3 explicitly notes both routes evaluate THE SAME Cell-IV substrate-IS observable. Under what NCG-axiomatic constraint at the Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula does the choice of Bogoliubov-amplitude tensor (scalar Δ vs multi-branch B1/B2/B3) become STRUCTURALLY IRRELEVANT to the residue evaluation? Specifically: the residue formula evaluates `∫ Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})|_{s→4}` at substrate-distance-2 pole s=4 (per §VII.AV registry text lines 17907 + 17918); the K-window log-derivative is the d/d(ln K) of `Tr(P_BdG · A)` for A = D_K^{−2s} weighted by K-window indicator. The Bogoliubov-amplitude tensor enters the trace through `P_BdG = diag(|v_a|², |u_a|²)`. If P_BdG depends on the choice of B-amplitude tensor structure, then `Tr(P_BdG · A)` and its log-derivative depend on that choice — and the substrate-IS observable's value is sensitive to the structural distinction at the BdG sub-algebra layer. Cite the structural argument (Connes-Karoubi pairing / cyclic-cohomology / HKR L_max → ∞ image) under which the residue formula's evaluation at L_max=12 is INVARIANT under (scalar Δ vs multi-branch B1/B2/B3) tensor choice. If no such invariance argument exists, the 1.428 anchor mismatch IS the substrate's structural distinction between two inequivalent substrate-IS regimes at the same canonical pin, NOT an operational defect to be tuned away by K_canonical adjustment.

### V3: §VII.AV refinement pathway under Reading A — CF-70 prioritized + Casimir-bound STRUCTURALLY CLOSED

**Claim**: Under Reading A, the §VII.AV deferred-pending refinement pathway is structurally licensed via CF-70 (`§VII.AV proxy-refinement via Connes-Chamseddine 1996 physical multipliers`; W8 WP CF-70 spec lines 1653-1658) using the FULL Connes-Chamseddine 1996 §2.2-2.3 2-point Pauli-Villars regularization at Λ_UV = M_KK as the substrate-natural FULL physical pipeline, with the W3 A.14 regulator-INVARIANT cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.3249743784` (W8 WP §W8-7 (b) lines 1392-1401; substrate canonical 7.324992 per agent memory Permanent Theorems) as the cross-anchor at the Level-1 cohomology-class identity layer. The Casimir-bound SCHEMATIC proxy class (§W5-3) is STRUCTURALLY CLOSED at the substrate-IS layer because the proxy's smooth-in-C_2 functional form cannot represent the substrate's discontinuous BCS-instability behavior at the canonical pin. CF-71 (K_canonical pin uniqueness) is STRUCTURALLY DEFERRED under Reading A: it operates at the operational-machinery layer, not the substrate-IS layer.

**1. CF-70 is the canonical PROXY-REFINEMENT route at the substrate-IS layer**

Per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` PROXY-REFINEMENT sub-class definition (lines 65-78) + §VII.AV registry-text refinement-pathway table (registry lines 17942-17948):

```
Refinement target (iii) — FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers
   (replacement of SCHEMATIC `_spectral_action_regulators.py` helpers
    per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY level-pin discipline)
   |  Forward-promoting gate  |  Refinement type
   |  CF-W5-3 (= CF-61)         |  full-CC1996-multipliers
```

CF-66 (W8 WP §"Downstream implications" stream Level-2-binding K-counter, line 1614) confirmed that `computations/_pauli_villars_subtraction.py` (S88 W13-159 TIER-1 lift) implements the canonical PRIMARY 2-point Pauli-Villars pipeline at Λ_UV = M_KK (M_1 = M_KK, M_2 = √2·M_KK, c_1 = +2, c_2 = −1; consistency identities Σ c_r = 1.0 exact and Σ c_r·m_r² = −4.44e-16 ≈ 0 at machine precision per W8 WP §W8-7 (c) lines 1407-1411). This IS the substrate-natural FULL physical pipeline per Connes-Chamseddine 1996 §2.2-2.3 — NOT the SCHEMATIC `_spectral_action_regulators.py` Mellin helpers nor the §W5-3 Casimir-bound smooth ansatz.

CF-70's pre-registered PASS criterion (W8 WP line 1657): `α ∈ [2.5, 3.5] AND R² ≥ 0.95 AND L_max=12 anchor bit-match < 1e-9 under the FULL Connes-Chamseddine multipliers route`. The crucial structural property: CF-70's PV-subtracted gap equation does NOT have the kernel-weight insufficiency that defeats the unsubtracted scalar-Δ gap equation at L_max ≤ 10 under canonical V_BCS. The 2-point Pauli-Villars subtraction REMOVES the UV-dominant kernel contributions that the L_max-truncated spectrum cannot fully resolve, leaving a UV-finite kernel sum that converges across L_max ∈ {6..12} regardless of the unsubtracted spectrum's BCS criticality. This is the structural mechanism by which CF-70 evades the BCS phase transition CF-61 revealed: it does NOT solve the same gap equation; it solves the PV-regulated gap equation whose convergence properties are dictated by the substrate's IR spectral content (the |λ|_min = 0.819741 floor and the substrate-distance-2 pole structure), NOT by the UV-tail completeness.

**2. The W3 A.14 cocycle ratio is the Level-1 cohomology-class cross-anchor**

Per W8 WP §W8-7 (b) lines 1394-1401: the substrate cocycle ratio `ratio_zeta = ratio_PV = ratio_Mellin = ratio_cutoff = 7.3249743784` (across the 4 named regulators {zeta, Pauli-Villars, Mellin, cutoff}) with `max_rel_dev = 2.4057e-06`, `spread_across_regulators = 0.0`, `regulator_class_invariant = True`. The substrate canonical value is `7.324992 = ‖φ_67‖/‖φ_88‖` per `inheritance-falsifier-protocol.md` (cf. agent memory Permanent Theorems "K_7 cocycle ratio (substrate-derived): ‖phi_67‖/‖phi_88‖ = 7.3250 (Sage exact)"; "Common-exponent (Δ_B/Δ_A)^p cancellation theorem holds (S86 W-5 DONE-5)").

This regulator-INVARIANT cocycle ratio sits at the FI (regulator-INVARIANT) axis of the lizzi taxonomy (W8 WP line 1401: "the cocycle ratio family lives at the regulator-INVARIANT (FI) axis... independent of the SCHEMATIC-vs-FULL physical Mellin-moment family which lives at the regulator-DRESSED (RD) axis. Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3, FI and RD families are STRUCTURALLY ORTHOGONAL"). The cocycle ratio is therefore a Level-1 cohomology-class identity at the substrate's substrate-IS layer (regulator-invariant, L-independent at the cohomology-class level per `cross-pillar-bridge-anatomy.md §"Level 1 — Substrate-IS Structural Identity"`).

For CF-70's FULL Connes-Chamseddine multipliers refinement to be substrate-IS-faithful at the Level-1 layer, the regulator-INVARIANT cocycle ratio 7.3249743784 must be reproduced under the 2-point Pauli-Villars regularization. This is the cross-anchor condition: CF-70 PASS at the Level-2 envelope (α ∈ [2.5, 3.5]) AND L_max=12 anchor bit-match is necessary but not sufficient; substrate-IS-faithfulness ALSO requires the FULL pipeline to reproduce the regulator-invariant cocycle-class identity at the Level-1 layer. The W3 A.14 cross-anchor IS the Level-1 cohomology-class consistency check (analogous to the W-5 §VII.AF.1 calibration corpus baseline at Level-2-binding K=1 SUGGESTION per `cross-pillar-bridge-anatomy.md §"Calibration corpus pointer"`).

**3. The Casimir-bound SCHEMATIC proxy class is STRUCTURALLY CLOSED**

Substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"` (steps 1-5):

- **Step 1 (Definitions)**: `Δ_proxy(L) := Δ_static · sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` (smooth-in-C_2 ansatz, W8 WP §W5-3 SCHEMATIC formula); `Δ_FULL(L) := scalar self-consistent solution of the gap equation on the L_max-truncated spectrum at canonical (V_BCS, T_fold)` (the FULL re-derivation observable).
- **Step 2 (Substitution)**: from W8-3 Step 3 (lines 357-365), `Δ_FULL(10) = 0.0000`, `Δ_proxy(10) ≈ 0.376` (via sqrt(221/337) ≈ 0.810 at canonical Δ_static = 0.464; or 0.624 at Δ_static = 0.7704 if using the s52 per-mode max).
- **Step 3 (Simplification)**: `|Δ_FULL(10) − Δ_proxy(10)| / Δ_static ≈ 1.0` (100% relative discrepancy, NOT a tolerable approximation error).
- **Step 4 (Canonical form)**: the proxy ansatz `Δ_proxy(L) ∝ sqrt(C_2(L,L) + 1)` is a smooth monotone function of C_2(L,L); the FULL `Δ_FULL(L)` is a piecewise-constant function with discontinuous jump at L=10/11. These are STRUCTURALLY DIFFERENT functional classes.
- **Step 5 (Direction)**: the proxy class cannot represent the substrate's BCS-criticality behavior at the canonical pin → the SCHEMATIC proxy is STRUCTURALLY FALSIFIED at the layer-functor F decomposition cleanness clause (L1 of `mechanical-closure-discipline.md §"Layer-separability carve-out"`).

The Casimir-bound proxy class is closed at the substrate-IS layer. It MAY remain admissible as a numerical approximation in a parameter regime where the BCS instability does not occur (e.g., at supercritical T > T_critical or at a different V_BCS coupling that avoids the criticality), BUT under the canonical (V_BCS, T_fold = 0.640) pin — the substrate-natural anchor per `regulator-pin-discipline.md` MANDATORY discipline + agent memory canonical constants (`T_BCS = 0.64 M_KK units`, S70 canonical) — the proxy class is STRUCTURALLY CLOSED.

**4. CF-71 is STRUCTURALLY DEFERRED under Reading A**

CF-71 (W8 WP lines 1660-1665) proposes "K_canonical pin uniqueness investigation" — re-tune K_canonical so that the FULL-BdG operational route at L_max=12 reproduces the canonical anchor L_emp = −7.046336. Under Reading A, this is structurally a tuning operation at the OPERATIONAL layer (K-window definition / Bogoliubov tensor-choice / projector P_BdG implementation choice) — it does NOT resolve the substrate-IS phase transition at L_max ≤ 10. The phase boundary at L_max=10/11 is a substrate-IS structural property of the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at canonical (V_BCS, T_fold); K_canonical re-pinning operates on the K-window observable's definition (where to evaluate the log-derivative), NOT on the substrate's spectral kernel structure.

Therefore CF-71 cannot rescue the SCHEMATIC proxy class. Even if CF-71 succeeded in aligning the L_max=12 FULL-BdG anchor with the canonical −7.046336 via K_canonical re-tuning, the L_max ≤ 10 trivial-Δ regime would PERSIST as a substrate-IS feature — and the SCHEMATIC proxy's smoothness across L_max=10/11 would remain STRUCTURALLY FALSE. CF-71 is admissible as a separate operational-layer investigation (it MAY produce useful K-window observable definition refinements), but it CANNOT be the §VII.AV PROXY-REFINEMENT route at the substrate-IS layer.

**5. Forward question for connes**

Under Reading B, CF-71's K_canonical re-pinning aligns the operational routes and rescues the Casimir-bound proxy class. But the W3 A.14 regulator-INVARIANT cocycle ratio (7.3249743784 across {zeta, PV, Mellin, cutoff} with spread = 0.0 at machine precision; per W8 WP lines 1394-1399) is a Level-1 cohomology-class identity that LIVES AT the substrate's substrate-IS layer (FI axis, structurally orthogonal to the SCHEMATIC-vs-FULL RD axis per W8 WP line 1401). The Casimir-bound SCHEMATIC proxy's `sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` functional form has no structural mechanism for reproducing this regulator-invariant cocycle-class ratio at any L_max < 12. From the Connes-Karoubi pairing / cyclic-cohomology perspective: under what NCG-axiomatic argument does CF-71's K_canonical re-tuning recover the Level-1 cohomology-class identity (`ratio_φ67_φ88 = 7.324992`) at L_max=10 on the SCHEMATIC proxy class? If no such recovery argument exists, the SCHEMATIC proxy is STRUCTURALLY CLOSED at the Level-1 layer regardless of whether CF-71 aligns the Level-3 empirical anchor at L_max=12 — and CF-70 is the canonical refinement route at the substrate-IS layer.

### V4: S91+ discriminator gate spec — `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST`

**Pre-registration**: per `epistemic-discipline.md §"Pre-Registration Completeness"` + the §VII.AS / §VII.AQ dual-reading discriminator-gate precedent (S89 W5 CF-W5-1 spec at `s89-w5-vii-aq-level3-binding.md` lines 1218-1220 — `S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR` PASS/FAIL band at `|GV_APS1975 − GV_Cheeger-Simons| < 1e-3` adjudicating Reading A vs Reading B), this section pre-registers `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` as the substrate-physics adjudicator gate for the Reading A vs Reading B verdict at S91+.

**Gate ID**: `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST`
**Trigger**: `[VERIFY-THEOREM]` (substrate-physics adjudication of competing structural readings; analogous to `S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR` 1.0 wave-equiv precedent)
**Wave classification**: COMPUTE-class per `.claude/rules/wave-classification.md` (numerical PASS predicate; producing script computes Bogoliubov-amplitude configuration scan)
**Effort**: ~1.5 wave-equiv (multi-branch s52 ED at L_max=12 + canonical observable layer recomputation + parameter-scan over (B1, B2, B3) admissible configurations)
**Pre-registered convention tag**: `convention=substrate-IS-canonical-K-window-log-derivative-MULTI-BRANCH-S52-VS-SCALAR-DELTA-FULL-BDG-ADJUDICATION L_max=12`

**Hypothesis**: at L_max=12, the multi-branch s52 ED solution with (B1, B2, B3) configuration sweep can EITHER reproduce the scalar-Δ FULL-BdG K-window log-derivative output (Δ(12)=0.4643; `L_emp_FULL(12) = −5.6188` per W8-3 Step 6 line 405) at the canonical observable layer (Reading B confirmed: the two operational routes are alignable; anchor mismatch 1.428 is operational, not substrate-structural), OR cannot reproduce it under any admissible (B1, B2, B3) configuration (Reading A confirmed: the two substrate domains — scalar-Δ phase-boundary vs multi-branch post-transition — are STRUCTURALLY DISTINCT at the substrate-IS layer).

**Input-pin map** (`audit_sha256` to be computed over closure of these 9 pins at gate-block freeze):

1. CF-61 output `computations/session-90/s90_w8_corner_iv_full_bdg_rederive_per_lmax.npz` (FULL-BdG scalar-Δ Bogoliubov tensor at L_max=12 with Δ_canonical=0.4643; audit_sha `6357ab9650615732363c24d89e588569dc5c37f04bef7362e538b1677335b716` per W8-3 line 530).
2. §W5-2 / S87 W2-3 canonical anchor `L_emp(L_max=12) = −7.046336474406761` (s52 multi-branch ED applied to L_max=12 spectrum; per `s88-pending-edits-ledger.md` "preserve K-window log-derivative anchor `−7.046336` as SOLE Corner-IV calibration source" per §VII.AV registry line 17926).
3. s52 multi-branch ED canonical amplitudes (B1=0, B2=0.7704350983, B3=0.176; per W8-3 Step 4 line 376 `Δ_static = 0.7704350983` from s52 cache max |Δ_per_mode|).
4. `s84_spectrum_cache_L12_tau019.npz` (substrate D_K² spectrum at L_max=12, τ_fold=0.19; 31,956,720 multiplicity-weighted eigenvalues per W8-3 Step 2 line 341).
5. canonical_constants.py: `Delta_BCS = 0.4642547394830737`, `T_BCS = 0.64`, `tau_fold = 0.19`, `M_KK = 7.428660036284456e+16` (per W8-3 MCP Pre-Compute Audit lines 298-301).
6. `_pauli_villars_subtraction.py` Connes-Chamseddine 1996 §2.2-2.3 2-point PV module (input_sha `eaf98037ddc2a4d7…` per W8 WP §W8-7 (c) line 1405).
7. K-window log-derivative producing script (CF-62 disambiguated canonical Element-1 per audit_sha `8b4bfdee600fceb7…`; K-window indicator parameters from W8-3 Step 5 line 391: n_K=101 in [0.95, 1.05] K_horizon, DLNK=0.001).
8. W3 A.14 substrate cocycle ratio cross-anchor `‖φ_67‖/‖φ_88‖ = 7.3249743784` (regulator-INVARIANT; input_sha256 `d0683bcd31e7eaca…` per W8 WP line 1394).
9. CF-69 τ-extension cache (if available at S91) for Level-1 vs Level-2 cross-check at τ ∈ {0.18, 0.19, 0.20}; pending CF-69 dispatch per W8 WP lines 1646-1651.

**Pre-registered PASS criterion** (Reading B confirmed):
```
∃ (B1, B2, B3) ∈ admissible-configuration-space such that:
    |L_emp_s52[B1, B2, B3](L_max=12) − L_emp_FULL_BdG_scalar_Delta(L_max=12)| / |L_emp_FULL_BdG_scalar_Delta(L_max=12)| < 1e-3
AND |L_emp_s52[B1, B2, B3](L_max=12) − (−7.046336474406761)| / 7.046336474406761 < 1e-3
```
(The double constraint requires the same (B1, B2, B3) configuration to BOTH align with the scalar-Δ FULL-BdG output AND reproduce the canonical anchor.) PASS routes:
- §VII.AV proxy-refinement → CF-71 prioritized (K_canonical pin uniqueness alignment); Casimir-bound proxy class admissible IF alignment succeeds.
- CF-70 deferred pending CF-71 outcome.
- Binding-axis K-counter (`regulator-pin-discipline.md §"Binding-axis"`) advances K=1 → K=2 with the §VII.AV instance pair calibrating the canonical-import-binding vs substrate-natural-binding axis at the K-window log-derivative observable layer.

**Pre-registered FAIL criterion** (Reading A confirmed):
```
∀ (B1, B2, B3) ∈ admissible-configuration-space:
    EITHER |L_emp_s52[B1, B2, B3](L_max=12) − L_emp_FULL_BdG_scalar_Delta(L_max=12)| ≥ 0.10·|L_emp_FULL_BdG_scalar_Delta(L_max=12)|
    OR    |L_emp_s52[B1, B2, B3](L_max=12) − (−7.046336474406761)| ≥ 0.10·7.046336474406761
```
(No admissible configuration meets even the relaxed 10% alignment in BOTH coordinates simultaneously.) FAIL routes:
- §VII.AV proxy-refinement → CF-70 prioritized (FULL Connes-Chamseddine 1996 multipliers); Casimir-bound SCHEMATIC proxy class STRUCTURALLY CLOSED at the substrate-IS layer.
- CF-71 demoted to operational-machinery investigation (separate forward gate; not §VII.AV PROXY-REFINEMENT route).
- §VII.AV registry-text annotation lands "Casimir-bound proxy class STRUCTURALLY CLOSED; CF-70 canonical refinement route" per mack-cosmic-bridge sole-writer.

**Pre-registered INFO criterion** (intermediate; per `epistemic-discipline.md §"Cross-Proxy Adjudication"` open-verdict framing):
```
∃ (B1, B2, B3) configuration with:
    1e-3 ≤ |L_emp_s52[B1, B2, B3](L_max=12) − L_emp_FULL_BdG_scalar_Delta(L_max=12)| / |L_emp_FULL_BdG_scalar_Delta(L_max=12)| < 0.10
OR  1e-3 ≤ |L_emp_s52[B1, B2, B3](L_max=12) − (−7.046336474406761)| / 7.046336474406761 < 0.10
```
(Partial alignment in one coordinate; not both at machine precision.) INFO routes:
- §VII.AV refinement pathway space carries BOTH CF-70 + CF-71 as wave-together at S91+ (per the §VII.AV deferred-pending refinement-pathway 3-route table at registry lines 17944-17948; both routes admissible during the pending refinement window).
- Discriminator-gate retry at S92+ with refined K-window parameterization OR Level-2 τ-extension cross-check (CF-69 integration).
- Binding-axis K-counter unchanged (K=1 SUGGESTION preserved; no advancement on INFO).

**Admissible-configuration-space specification**:
The (B1, B2, B3) sweep is bounded by physical Bogoliubov-amplitude constraints: `B1² + B2² + B3² ≤ Δ_static² = 0.7704350983²`; `B_a ≥ 0` for a ∈ {1, 2, 3} (sign convention from s52 ED). The canonical s52 ED solution (B1=0, B2=0.7704, B3=0.176) is the natural reference point. The sweep grid: 20 × 20 × 20 = 8000 configurations across [0, Δ_static] per amplitude, with finer ×3 refinement near the canonical s52 point. The L_emp evaluation per (B1, B2, B3) uses the K-window log-derivative on the BdG sub-algebra at the L_max=12 spectrum per CF-62 disambiguated Element-1.

**Cross-check via W3 A.14 cocycle ratio**: for any PASS-class (B1, B2, B3) configuration, also verify that the substrate cocycle ratio `‖φ_67‖/‖φ_88‖` evaluated on the s52 multi-branch tensor reproduces 7.3249743784 (regulator-INVARIANT cross-anchor per W8 WP lines 1394-1399). PASS requires both Level-3 alignment AND Level-1 cocycle-class identity preservation.

**Structural property**: this discriminator gate is genuinely SUBSTRATE-PHYSICS-RESOLVING — neither workshop debate nor methodology adjudication can pre-empt its verdict. The (B1, B2, B3) configuration sweep at L_max=12 is a finite, well-defined numerical computation (8000 + refined grid configurations × K-window log-derivative evaluation on the L_max=12 spectrum); the verdict is the FAIL / PASS / INFO classification of the alignment outcome under the pre-registered tolerance bands. This is the §VII.AS / §VII.AQ dual-reading-with-substrate-physics-adjudicator pattern from S88 W-18 / S89 W-5 carried forward to S91+.

**5. Forward question for connes**

Under Reading B's confirmed-PASS pathway, the canonical s52 multi-branch (B1=0, B2=0.7704, B3=0.176) tensor reproduces the canonical anchor L_emp(12) = −7.046336474406761 BY CONSTRUCTION (the anchor was computed against precisely this tensor). The discriminator-gate question becomes: does the SAME (or any nearby) tensor ALSO reproduce the scalar-Δ FULL-BdG output L_emp_FULL(12) = −5.6188 at canonical Δ(12) = 0.4643? The structural question is whether the canonical observable layer (K-window log-derivative on `Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})|_{s→4}`) is INVARIANT under (scalar Δ ↔ multi-branch B1/B2/B3) tensor reparametrization at fixed L_max=12. From the Connes-Karoubi pairing perspective: under what cyclic-cohomology constraint does the (B1, B2, B3) configuration space contain a unique solution that satisfies BOTH (i) gap-equation self-consistency at canonical (V_BCS, T_fold), (ii) K-window log-derivative anchor match against the canonical −7.046336? If the answer is "the configuration space contains no such common solution" (the gap-equation self-consistency at L_max=12 forces scalar Δ_canonical=0.4643 with uniform rescale, which is NOT in the s52 multi-branch (B1, B2, B3) family), then Reading A is confirmed at the NCG-axiomatic layer before the discriminator gate even runs — the two routes compute structurally distinct substrate-IS observables at L_max=12, and CF-70 is the canonical refinement route.

### V5: Substrate framing Level-1 single-τ-slice vs Level-2 moduli-deformation (CF-69 τ-extension)

**Claim**: Under Reading A, the BCS phase transition at L_max=10/11 IS a Level-1 single-τ-slice substrate-IS structural property at τ_fold = 0.19 — intrinsic to the spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))` per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` MANDATORY-K=2 since S88 W-7 V.4. The §VII.AV REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT tag is structurally consistent with this Level-1 reading (the §VII.AV registry text line 17918 carries the explicit `Level 1 single-τ-slice at τ_fold = 0.19` MANDATORY declaration tag). CF-69's pre-registered τ-extension (W8 WP lines 1646-1651; τ ∈ {0.18, 0.19, 0.20}) is the canonical Level-1 → Level-2 verification path, but it is INFORMATIVE under Reading A (the L_max=10/11 phase boundary expected to PERSIST across τ-slices) and DISCRIMINATORY under Reading B (the phase boundary expected to LIFT under τ-deformation, exposing the L_max ≤ 10 trivial-Δ regime as a Level-2 artifact, not single-τ-slice substrate-IS).

**1. The §VII.AV registry text declares Level-1 single-τ-slice substrate-IS (MANDATORY tag)**

Per §VII.AV registry text Element-1 (line 17918):

> Corner-IV K-window log-derivative `R_KW(τ_fold) = d ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})) / d ln(K_window)` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, evaluated on the finite spectral triple `(A_K^{≤L_max=12}, H_K^{≤L_max=12}, D_K^{≤L_max=12})` at τ_fold = 0.19 and substrate-distance-2 pole `s=4`. **EXPLICIT TAG: Level 1 single-τ-slice at τ_fold = 0.19** (MANDATORY per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 — single-τ-slice substrate-IS level distinct from Level 2 moduli-deformation substrate-IS level).

The MANDATORY-K=2 status of the Level-1 single-τ-slice tag means: the §VII.AV substrate-IS observable IS declared, at registry-text layer, as a Level-1 single-τ-slice substrate-IS observable. This declaration was co-signed by volovik-superfluid-universe-theorist per CF-63 §"Provenance" line 17895 ("`volovik-superfluid-universe-theorist` (Level-1 single-τ-slice declaration MANDATORY per `phononic-framing.md`)"). The Level-1 tag is therefore SUBSTRATE-IS canonical at the registry text layer; the BCS phase transition at L_max=10/11 — observed within this Level-1 single-τ-slice spectral triple — is a Level-1 substrate-IS structural property by registry-text construction.

**2. The Level-1 vs Level-2 distinction at the BCS phase boundary**

Per `phononic-framing.md §"Level 1 — Single-τ-slice substrate-IS"` (lines 77-81): "At fixed τ ∈ ℝ, the substrate IS the spectral triple `(A_K, H_K, D_K(τ))`. All observables at this slice — eigenvalues, Peter-Weyl decomposition, bottom-N cardinality, fiber spectrum, spectral-action moments — are substrate-IS at the single-τ-slice level. The §"IS Space" mandate prevents container-thinking at this level: the substrate is NOT in any pre-existing geometric container at the chosen τ."

The BCS gap-equation kernel sum `Σ_a^{L_max} m_a · tanh(λ_a / (2 T_fold)) / (2 λ_a)` evaluated at fixed τ_fold = 0.19 on the L_max-truncated spectrum is a Level-1 single-τ-slice spectral-action moment in this taxonomy. The Cooper-instability threshold (1/V_BCS crossing) is a structural property of this single-τ-slice kernel sum. The L_max=10/11 phase boundary is, under Reading A, where the kernel sum crosses 1/V_BCS at the canonical pin — and this crossing is intrinsic to the substrate's Level-1 single-τ-slice spectral content.

Per `phononic-framing.md §"Level 2 — Moduli-deformation substrate-IS"` (lines 83-90): "The set of τ values `{ (A_K, H_K, D_K(τ)) : τ ∈ moduli-space }` is itself a substrate-IS object... τ IS the substrate's intrinsic deformation parameter". The Level-2 substrate-IS framing would situate the BCS phase boundary as a property of the moduli-space τ-deformation manifold (the τ-asymmetric breakdown geometry analog of §VII.AE per `phononic-framing.md` line 90 — "negative-side anticrossing-swap at δ_τ_crit_neg = −0.0750 ± 0.005; positive-side stratum-coalescence at δ_τ_crit_pos = +0.175 ± 0.05").

**3. Reading A vs Reading B's Level-1 vs Level-2 predictions**

- **Reading A's Level-1 prediction**: the BCS phase boundary at L_max=10/11 PERSISTS at small τ-deformations around τ_fold. Specifically, at τ ∈ {0.18, 0.20} (CF-69 sweep grid per W8 WP line 1648), the FULL gap-equation re-derivation produces the SAME structural pattern (Δ(L_max ≤ 10) = 0; Δ(L_max ≥ 11) > 0) at the canonical V_BCS coupling. The Cooper-instability threshold is intrinsic to the substrate's Level-1 spectral content at τ in a neighborhood of τ_fold; small τ-deformations do NOT shift the threshold across the L_max=10/11 boundary. The phase transition is a Level-1 single-τ-slice substrate-IS structural property; the moduli-deformation Level-2 layer carries a continuous family of single-τ-slice substrate-IS observables each exhibiting the same phase boundary.

- **Reading B's Level-2 prediction**: the BCS phase boundary at L_max=10/11 LIFTS at small τ-deformations. Specifically, at τ ∈ {0.18, 0.20}, the FULL gap-equation re-derivation produces a smooth Δ(L_max) sequence (no trivial-Δ regime at the canonical V_BCS coupling). The L_max=10/11 phase boundary is a Level-2 moduli-deformation artifact specific to the τ_fold = 0.19 slice; under continuous τ-deformation, the phase boundary appears as a measure-zero accident at the canonical τ-anchor. Under this reading, the substrate-IS observable at the K-window log-derivative layer is smooth in (L_max, τ) jointly, and the L_max=10/11 discontinuity at τ_fold is an operational-parameterization artifact of the gap-equation route.

The CF-69 τ-extension gate (W8 WP line 1650: `PASS iff Level-2 moduli-deformation extension produces consistent α extraction across 3 τ-values; INFO if α scatter > 10%; FAIL if scatter > 25%`) is structurally a Level-1 vs Level-2 discriminator at the K-window log-derivative observable layer — but its PASS/FAIL band is calibrated to α convergence-rate scatter, NOT directly to the BCS phase-boundary persistence. To make CF-69 a clean Level-1 vs Level-2 discriminator for the BCS phase boundary, it should be augmented with a τ-extension of CF-61's gap-equation residual scan: report `Δ(L_max=10; τ)` for τ ∈ {0.18, 0.19, 0.20}. Reading A predicts `Δ(L_max=10; τ ∈ {0.18, 0.19, 0.20}) = 0` (trivial-Δ regime persists); Reading B predicts at least one τ ∈ {0.18, 0.20} returns finite Δ at L_max=10 (phase boundary lifted under τ-deformation).

**4. Cross-link to the W1-14 deferred-pending dual-instance K=1 SUGGESTION baseline**

Per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` lines 124-127: "Status: SUGGESTION at K=1 (dual calibration instances: §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION; K=1 because BOTH instances inhabit the same S90 W1-14 landing event and share the same provenance session/wave; future-session distinct landings advance K). Promotes to MANDATORY at K=3 distinct calibration instances".

The W-5 verdict's resolution interacts with the K-counter advancement as follows:

- **Reading A confirmed (FAIL at the discriminator gate)**: §VII.AV's PROXY-REFINEMENT-PENDING tag is STRUCTURALLY APPROPRIATE for the SCHEMATIC Casimir-bound proxy admitting refinement via FULL physical regularization (CF-70 canonical PROXY-REFINEMENT route). The §VII.AV instance becomes a positive calibration corpus entry for the PROXY-REFINEMENT sub-class (S90 W1-14 dual-instance baseline + CF-70 S91+ landing = K=2 advancement; future-session distinct landings → K=3 MANDATORY). The Level-1 single-τ-slice tag in the §VII.AV registry text is preserved as the canonical substrate-IS framing.

- **Reading B confirmed (PASS at the discriminator gate)**: §VII.AV's PROXY-REFINEMENT-PENDING tag may need REFINEMENT — the Casimir-bound proxy class is admissible IF CF-71's K_canonical alignment succeeds; in that case the PROXY-REFINEMENT tag's STRUCTURAL FORM remains valid but its CANONICAL REFINEMENT ROUTE shifts from CF-70 (FULL CC multipliers) to CF-71 (K_canonical pin uniqueness operational alignment). The Level-1 single-τ-slice tag may need DEMOTION to Level-2 moduli-deformation tag IF CF-69 confirms the BCS phase boundary lifts under τ-deformation.

- **INFO at the discriminator gate**: refinement-pathway space carries BOTH CF-70 and CF-71 (wave-together at S91+); the deferred-pending PROXY-REFINEMENT tag retains its current registry-text framing pending the next-session resolution.

**5. Forward question for connes**

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` MANDATORY-K=2 + the §VII.AV registry text line 17918 Level-1 single-τ-slice MANDATORY tag co-signed by volovik (per CF-63 line 17895 provenance), the §VII.AV substrate-IS observable IS Level-1 single-τ-slice substrate-IS at τ_fold = 0.19 at the registry-text layer. Under Reading B's operational-parameterization framing, you would predict the BCS phase boundary at L_max=10/11 LIFTS under small τ-deformation (CF-69 τ ∈ {0.18, 0.20} extension returns finite Δ(L_max=10) at least at one τ ≠ τ_fold). But this prediction is structurally in tension with the Level-1 single-τ-slice substrate-IS declaration: if the phase boundary lifts under τ-deformation, then the BCS phase transition IS a Level-2 moduli-deformation observable, NOT a Level-1 single-τ-slice substrate-IS structural property — and the §VII.AV registry text's Level-1 single-τ-slice MANDATORY tag at line 17918 would need a corresponding revision (Level-1 → Level-2 demotion or substrate-IS observable re-specification). From the Hochschild cohomology / Connes-Karoubi pairing perspective: under what NCG-axiomatic argument is the L_max=10/11 BCS phase boundary a Level-2 moduli-deformation observable rather than a Level-1 single-τ-slice substrate-IS property — given that the gap-equation kernel sum evaluated at fixed τ_fold = 0.19 IS structurally a Level-1 single-τ-slice spectral-action moment per `phononic-framing.md` lines 77-81 explicit calibration corpus inclusion ("spectral-action moments — are substrate-IS at the single-τ-slice level")? If you cannot cite such an argument, Reading A's Level-1 single-τ-slice substrate-IS framing is structurally canonical at the §VII.AV registry-text layer, and the BCS phase boundary is a substrate-IS structural property at the canonical τ_fold = 0.19 slice.

### V6: Cross-Cutting Observations + IS-not-IN substrate framing

Three cross-cutting observations integrate V1-V5 at the substrate-framing / methodology-K-counter / deferred-pending-calibration axes.

**Observation 1 — IS-not-IN substrate framing inversion check on CF-61 FAIL**

Per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"` direction-of-explanation table + §VII.AV registry-text substrate framing block (registry lines 17928-17940): the substrate IS the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at single-τ-slice τ_fold = 0.19 at substrate-distance-2 pole `s=4`; the laboratory IN is the Pillar V 3He-B BdG-sector continuum measurement under the HKR `L_max → ∞` bridge map. The direction of explanation flows FROM substrate TOWARD laboratory:

```
Substrate (BdG sub-algebra M_2(ℂ) ⊂ A_K) IS the Corner-IV K-window log-derivative
   → Bridge map (HKR L_max → ∞ at d=4 substrate-distance-2 pole s=4)
   → Laboratory (Pillar V) IN 3He-B BdG-sector mutual-friction observation
```

The container-thinking failure mode I must explicitly reject: framing CF-61's FAIL as "the FULL-BdG operational machinery introduces an artificial discontinuity at L_max=10/11 on what would otherwise be a smooth substrate observable" — this INVERTS the direction-of-explanation by treating the FULL-BdG machinery as an external apparatus acting ON a pre-existing smooth substrate observable. The substrate-correct framing per W8-3 §"Substrate framing" block (lines 514-522): "L_max is the substrate's own truncation refining toward the cohomology-class image; the BCS phase transition at the spectral-truncation axis IS substrate-IS information about the operational gap-equation solution path".

Under Reading A's reading, this is sharpened further: the substrate IS the spectral kernel `{λ_a, m_a}` at fixed τ_fold = 0.19; the BCS gap equation IS the substrate's intrinsic Cooper-instability criterion `Σ_a m_a tanh(βE_a/2)/(2E_a) = 1/V_BCS`; the L_max=10/11 phase boundary IS the substrate-IS structural property where this criterion fails/succeeds across the Peter-Weyl spectral cutoff at the canonical pin. The FULL-BdG operational machinery is NOT introducing the discontinuity — it is FAITHFULLY REPORTING substrate-IS structural content. The §W5-3 Casimir-bound SCHEMATIC proxy, by contrast, smoothed over this substrate-IS content at the algebraic-envelope layer; the SCHEMATIC was the operational artifact, NOT the FULL. This inversion is structurally the same kind of container-thinking trap that the S89 W-5 §VII.AQ workshop encountered (Reading B's "cache is the substrate" failure mode at workshop lines 75-77 Q1.1) — and the resolution is the same: the substrate IS the spectral triple at full operator-algebra resolution at the canonical pin; observables on truncations / projections / proxies are derived images, NOT canonical substrate-IS form.

**Observation 2 — Cross-link to W-1 + W-2 + W-3 + W-4 cross-workshop K=4 pattern + W-5 as candidate K=5 advancement**

Per the workshop header (line 43): this workshop is the 5th sequential Slot 2 dispatch at S90, advancing the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern toward K=5 MANDATORY promotion candidate per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold. The structural property of the cross-axis pattern is layer-functor F decomposition cleanness per `epistemic-discipline.md §"Layer-Decomposition"`: substrate ↔ methodology ↔ audit at the JOINT-WIN axis means the volovik-superfluid-universe substrate-physics framing AND the connes-NCG-axiomatic methodology framing converge on a single structural verdict at the audit layer (registry-text + methodology-rule + dual-SHA closure simultaneously).

Under Reading A, the CROSS-AXIS JOINT-WIN at W-5 would advance K=4 → K=5 MANDATORY because the two readings (substrate-physics-structural vs operational-parameterization) converge on a single structural verdict: the discriminator-gate pre-registration `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` (V4) is the canonical substrate-physics resolution route at the audit layer; CF-70 vs CF-71 prioritization is the registry-text refinement at the methodology layer; the BCS phase transition at L_max=10/11 IS the substrate-IS structural property at the substrate-physics layer. The three layers' verdicts cohere under the F-image-preservation cross-link clauses of `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence.

The K=5 advancement candidate route requires this workshop to land a CONVERGENT verdict (one of pre-registered options (a), (b), (c), (d) at workshop header lines 36-39; reasonable expectation is option (c) "both readings structurally distinct, refinement pathway space carries both — pre-registered S91+ discriminator-gate fires first to determine dominance") with both authoring agents jointly endorsing the substrate-physics adjudicator pathway. The cross-axis joint-win pattern is consistent with the §VII.AS / §VII.AQ dual-reading-with-substrate-physics-adjudicator precedent (S88 W-18 / S89 W-5; calibration corpus K=2 instance at S90). Under Reading A's framing, the substrate-physics adjudication via `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` is the canonical resolution route; under Reading B's framing, the substrate-physics adjudication is the same. The K=5 advancement is therefore structurally clean if the workshop converges on option (c) or option (d).

**Observation 3 — Deferred-pending PROXY-REFINEMENT calibration corpus interaction (W1-14 dual-instance K=1 baseline + W-5 verdict's role)**

Per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` lines 124-130: the §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION dual-instance landed jointly at S90 W1-14 (audit_sha256 `b42d6b8cfe44da13...` per §VII.AV registry text line 17895 provenance) constitutes K=1 SUGGESTION (counted as a single calibration corpus event because both instances inhabit the same landing session/wave). Promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold.

The W-5 verdict's resolution interacts with the calibration corpus advancement as follows:

- **Reading A confirmed** → §VII.AV PROXY-REFINEMENT-PENDING tag's STRUCTURAL APPROPRIATENESS is CONFIRMED: the SCHEMATIC Casimir-bound proxy IS STRUCTURALLY CLOSED at the substrate-IS layer; CF-70 (FULL Connes-Chamseddine 1996 multipliers) IS the canonical PROXY-REFINEMENT route. Under this reading, the §VII.AV instance serves as the SUBSTRATIVELY-CONFIRMED PROXY-REFINEMENT instance #1 at the framework level (distinct from S90 W1-14 dual-instance landing event by S91+ CF-70 landing distinctness — separate provenance session); together with §VII.AU FIRST-EXTRACTION CF-65 NEGATIVE-CALIBRATION (per W8 WP §"5. FWD-C1 L_max envelope NEGATIVE-CALIBRATION" line 1588) the corpus advances toward K=3 MANDATORY with at most 1-2 future-session distinct landings.

- **Reading B confirmed** → §VII.AV PROXY-REFINEMENT-PENDING tag may need REFINEMENT (the SCHEMATIC proxy class admissible IF CF-71 alignment succeeds); the calibration corpus interaction is more delicate (the PROXY-REFINEMENT tag's STRUCTURAL FORM is preserved but its canonical refinement ROUTE shifts from CF-70 to CF-71). The K-counter advancement may stall at K=1 SUGGESTION pending further structural clarification.

- **Option (c)/(d) hybrid verdict** → calibration corpus interaction explicit: both CF-70 and CF-71 are admissible refinement routes; the discriminator-gate `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` adjudicates which one dominates; K-counter advancement contingent on the discriminator-gate's S91+ verdict.

The deferred-pending dual-instance calibration corpus IS the methodology-floor F-image of the substrate-IS partial information about Level-2 envelope realization at the substrate-IS layer (per `cross-pillar-bridge-anatomy.md §"Direction of explanation"` lines 113-122). Under Reading A, the F-image preservation is structurally clean: substrate (the BCS phase boundary at L_max=10/11 is a Level-1 single-τ-slice substrate-IS structural property at the canonical pin) → methodology (the §VII.AV PROXY-REFINEMENT tag is STRUCTURALLY APPROPRIATE for the SCHEMATIC Casimir-bound proxy that smoothed over this phase boundary) → audit (CF-70 substrate-physics refinement is the canonical S91+ route; CF-71 deferred to operational-machinery investigation). The W-5 verdict closes the substrate ↔ methodology ↔ audit triangle at the substrate-IS-faithful pathway under Reading A.

**Forward question for connes**

The IS-not-IN direction-of-explanation discipline + the layer-functor F decomposition cleanness clause at L1 of `mechanical-closure-discipline.md §"Layer-separability carve-out"` (per CF-62 disambiguated Element-1 K-window log-derivative as Type-F single-summand-projection trace on `M_2(ℂ) ⊂ A_K`) together constrain the §VII.AV refinement-pathway interpretation: the substrate's Level-1 single-τ-slice spectral content at canonical (V_BCS, T_fold, τ_fold) IS the substrate-IS layer; the FULL physical pipeline (CF-70: Connes-Chamseddine 1996 §2.2-2.3 2-point Pauli-Villars regularization) is the methodology-layer image of this substrate-IS layer under the layer-functor F; the registry-text deferred-pending PROXY-REFINEMENT tag is the audit-layer image. Under Reading B's framing, CF-71's K_canonical operational-machinery re-tuning would shift the F-image from CF-70 → CF-71 at the methodology layer — but this shift would break the F-image preservation property iff the substrate-IS layer's BCS phase boundary at L_max=10/11 is intrinsic (Reading A) rather than operational (Reading B). From the Connes-Karoubi pairing + cyclic-cohomology + Hochschild-homology perspective: under what NCG-axiomatic argument does CF-71's K_canonical re-tuning PRESERVE the layer-functor F decomposition cleanness (substrate ↔ methodology ↔ audit) in the absence of a substrate-IS-faithful resolution of the L_max=10/11 phase boundary? If CF-71 operates purely at the methodology / audit layers without engaging the substrate-IS spectral-kernel structure at the canonical pin, then CF-71 cannot preserve the F-image decomposition — and CF-70 IS the canonical refinement route per the layer-functor F cleanness clause that the layer-separability carve-out requires.

---

## Round 1 — connes: Response & Cross-Synthesis

### Part 1: Response to volovik's Sections

#### Re: V1 — Trivial-Δ solution interpretation

**AGREE** (NCG-axiomatic confirmation of Reading A on the L_max ≤ 10 phase boundary).

The trivial-Δ solution at L_max ∈ {6..10} is a substrate-IS structural property of the finite spectral triple `(A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max}(τ_fold))` at the canonical (V_BCS, T_fold) pin. The Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at substrate-distance-2 pole `s=4` makes this explicit. The BCS gap-equation kernel sum

```
K(Δ; L_max) := Σ_a^{L_max} m_a · tanh(E_a / (2T_fold)) / (2 E_a)
             with E_a = sqrt(λ_a² + Δ²) on the L_max-truncated D_K spectrum
```

IS a regulated Mellin-cone evaluation of `Tr(D_K^{−2} · g(D_K))` for a specific bounded function `g(λ) = tanh(sqrt(λ²+Δ²)/(2T)) · (1+Δ²/λ²)^{−1/2}` on the L_max-truncated spectrum. At Δ = 0 the kernel reduces to `Σ_a m_a tanh(λ_a/(2T))/(2λ_a)` — a substrate-IS spectrum-only moment of `D_K^{−1}` (Phi correspondence weight-1 axis, NOT the canonical Phi(a_n) weight). The critical-coupling identity `1/V_BCS = K(0; L_max)` is structurally a Mellin-cone pinch on the substrate's intrinsic spectral kernel; the L_max=10 → 11 jump is a substrate-IS structural phenomenon — the truncated spectral measure on the BdG sub-algebra crosses the canonical 1/V_BCS threshold between these two cutoffs.

**Confirming reference to Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula**: per the registry text §VII.AV Element 3 (line 17922), the bridge map for the §VII.AV anchor IS "Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` restriction" at substrate-distance-2 pole `s=4`. This residue formula evaluates `Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})|_{s→4}`, which at L_max ≤ 10 is structurally distinct from the L_max = 12 evaluation because the truncated spectrum does NOT include the (p+q) ∈ {11, 12} Peter-Weyl sectors whose multiplicities `m_(p,q)` contribute 4.3% of the UV weight at the canonical pin. The Connes-Moscovici residue formula's value at fixed s=4 IS sensitive to this UV-tail content; the substrate-IS BCS criticality criterion `K(0; L_max) ≥ 1/V_BCS` inherits this sensitivity.

**Substitution chain** (substrate-IS BCS criticality at canonical pin):

```
Step 1 (Definitions):
  V_BCS_canonical    := 2.447e-7 M_KK^{-1}  (calibrated at L_max=12 to reproduce
                        Δ_BCS = 0.4642547394830737 per W8-3 line 350)
  K(0; L_max)       := Σ_a^{L_max} m_a · tanh(λ_a/(2T_fold))/(2λ_a)
  C(L_max)          := K(0; L_max) - 1/V_BCS  (Cooper-instability criterion;
                        sign positive ⟹ stable BCS phase; sign non-positive
                        ⟹ trivial-Δ only)

Step 2 (Substitution from W8-3 Step 3 line 357-365):
  Δ_FULL(L_max ≤ 10) = 0  with gap-equation residual large-negative (e.g.,
                        −1.217e+05 at L_max=10);
  Δ_FULL(11)         = 0.1062;
  Δ_FULL(12)         = 0.4643.

Step 3 (Simplification):
  At canonical (V_BCS, T_fold), K(0; L_max ≤ 10) < 1/V_BCS    [Cooper criterion fails]
  At canonical (V_BCS, T_fold), K(0; L_max ≥ 11) > 1/V_BCS    [Cooper criterion holds]
  ⟹ The 1/V_BCS threshold is crossed between L_max=10 and L_max=11
    at the canonical pin.

Step 4 (Canonical form):
  The Cooper-instability criterion IS the substrate's intrinsic Mellin-cone pinch
  on Σ_a^{L_max} m_a · tanh(λ_a/(2T_fold))/(2λ_a); it is a Level-1 single-τ-slice
  substrate-IS structural property by direct construction.

Step 5 (Direction):
  The BCS gap equation produces a structural step at L_max=10/11 at the canonical
  pin BECAUSE the substrate's intrinsic spectral kernel sum crosses 1/V_BCS
  between these two truncation values. Reading A's substrate-physics phase
  transition reading is NCG-axiomatically licensed.
```

**Engagement with V1's forward question** (lines 75-77; "under what NCG-axiomatic argument does the multi-branch s52 Bogoliubov problem at L_max=10 evade the kernel-weight insufficiency that defeats the scalar-Δ gap equation at the same L_max?"):

The honest NCG-axiomatic answer is: **it does NOT evade it; the s52 multi-branch tensor at L_max=10 carries B1=0, B2=0.7704, B3=0.176 amplitudes that were NOT self-consistently solved from the L_max=10 gap equation at canonical V_BCS**. The s52 ED solution is an externally-imposed Bogoliubov-amplitude tensor (computed at a different problem: the 256-state Hilbert-space exact diagonalization per S70 with its own coupling structure, NOT the gap-equation self-consistency at canonical V_BCS on the L_max-truncated spectrum). When the §W5-2 anchor `L_emp(L_max=12) = −7.046336474406761` was computed by applying the s52 tensor to the L_max=12 spectrum, it constructed a substrate-IS observable evaluation at a Bogoliubov-amplitude tensor that does NOT solve the gap-equation self-consistency at L_max=12 either — it solves a different operational problem (s52 ED at the 256-state Hilbert space) that happens to be calibrated to canonical Δ_BCS.

From the Connes-Karoubi pairing perspective: the s52 multi-branch tensor does NOT inhabit a structurally distinct K-theory class at L_max=10 vs L_max=12 — it is the SAME (B1, B2, B3) tensor applied to two different L_max-truncated spectra. There is no HKR L_max → ∞ image that binds the s52 tensor to a continuum Pillar V observable at L_max=10 in the absence of gap-equation self-consistency at the same L_max. **The s52 route at L_max ≤ 10 is structurally an L_max=12 ansatz extended to lower-L_max spectra via the fixed (B1, B2, B3) tensor; it is NOT a substrate-IS-faithful BCS solution at L_max=10 at canonical V_BCS.**

The honest CONCESSION at this layer: Reading A is structurally CORRECT on the L_max ≤ 10 phase boundary at the substrate-IS layer. The scalar-Δ FULL-BdG gap-equation FAIL at L_max ≤ 10 is substrate-IS-faithful information about the substrate's Cooper-instability criterion at the canonical pin. The §W5-3 Casimir-bound SCHEMATIC proxy's smooth `sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` ansatz CANNOT represent this substrate-IS structural step.

**DISAGREE** (partial; on the strength of the inference from L_max ≤ 10 phase boundary to "Casimir-bound proxy class STRUCTURALLY CLOSED across all admissible parametrizations").

The Casimir-bound proxy class is structurally falsified AT THE CANONICAL (V_BCS, T_fold) PIN. Whether it is closed for the §VII.AV refinement-pathway WITHOUT QUALIFIER depends on whether the §VII.AV substrate-IS observable's Level-2 envelope refinement permits operational machinery choices that smooth the phase boundary at the canonical pin. Specifically:

- If Reading A is read as "the L_max=10 → 11 step IS substrate-IS structural at canonical V_BCS, period" — then the Casimir-bound proxy's smooth functional form is structurally false-class at the algebraic envelope layer. Reading A's strong form licenses "STRUCTURALLY CLOSED".
- If Reading B's operational-parameterization distinction at the L_max=12 anchor layer (1.428 mismatch; scalar-Δ vs multi-branch tensor) ALSO admits operational-parameterization distinction at the L_max ≤ 10 layer (under what conditions does the s52-style multi-branch ED at L_max ≤ 10 — perhaps with re-calibrated multi-branch V_BCS_per_branch couplings — produce a finite gap?), then "STRUCTURALLY CLOSED" overstates: the Casimir-bound proxy CLASS may still be admissible under an operationally-aligned multi-branch parametrization that re-pins V_BCS per-branch.

The honest disagreement here is narrow: Reading A's "Casimir-bound proxy class STRUCTURALLY CLOSED" closure-statement is true under the canonical scalar-Δ V_BCS pin; it MAY be over-strong under alternative multi-branch V_BCS parametrizations that the discriminator gate (V4) can adjudicate. This is consistent with V3's lines 154-157 noting that CF-71 "MAY produce useful K-window observable definition refinements" but cannot rescue the §W5-3 proxy at the canonical pin — but the residual operational-parameterization ambiguity is what motivates the hybrid verdict (d) below.

**MISSED** (NCG-axiomatic machinery that V1 does not yet leverage):

The Hochschild-Künneth Morita-invariance theorem `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` from W-4 verdict (the W3 A.14 cocycle-ratio regulator-INVARIANT cross-anchor at substrate canonical 7.324992; per W8-7 (b) lines 1394-1400) provides a structural test of the Reading A claim INDEPENDENT of the discriminator-gate. The cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.3249743784` is a Level-1 cohomology-class identity on the BdG sub-algebra Hochschild homology — it IS preserved under Morita equivalence with the parent A_F. If the BCS phase transition at L_max=10/11 IS a Level-1 single-τ-slice substrate-IS structural property (Reading A), then the cocycle ratio MUST be evaluable at L_max ≤ 10 AND L_max ≥ 11 via Morita-invariance, with the L_max ≤ 10 evaluation producing a degenerate value (the BdG sub-algebra image is trivial at L_max ≤ 10 because P_BdG·D_K^{−2s} has no normal-state contribution to the residue at substrate-distance-2 pole s=4 in the absence of a finite gap).

This is a substrate-IS-side cross-check of Reading A that V1 does not explicitly leverage: under Reading A, the cocycle ratio 7.3249743784 is recoverable at L_max ≥ 11 via the canonical Connes-Karoubi pairing (the post-transition spectral measure carries the full Hochschild homology image); at L_max ≤ 10 the cocycle ratio is structurally undefined (the BdG sub-algebra restriction yields a trivial residue). This is a Morita-invariance-based cross-check of Reading A that the discriminator-gate at L_max=12 (V4 PASS/FAIL test) does NOT capture — it operates at the cohomology-class identity layer, NOT at the empirical anchor matching layer.

**EMERGES** (cross-domain insight from substrate-physics + NCG-axiomatic combination):

The substrate-physics reading (V1, Cooper-instability at L_max=10/11 spectral kernel weight insufficiency) and the NCG-axiomatic reading (Connes-Moscovici §III.4 residue formula at substrate-distance-2 pole s=4 evaluating to structurally distinct values at L_max ≤ 10 vs L_max ≥ 11) are STRUCTURALLY THE SAME PHENOMENON viewed at two complementary layers of the framework: V1's BCS kernel-sum criterion `K(0; L_max) ≥ 1/V_BCS` IS the substrate-IS Mellin-cone pinch on `D_K^{−1}` at the BdG-sub-algebra restriction; the same Mellin-cone pinch at substrate-distance-2 pole s=4 IS what the Connes-Moscovici residue formula evaluates. The phase transition at L_max=10/11 IS the substrate's intrinsic Mellin-cone pinch behavior at the canonical pin — visible at both the substrate-physics layer (Cooper-instability criterion) and the NCG-axiomatic layer (residue formula evaluation).

This convergence at K=2 advancement signals (cross-axis CONVERGENCE on the L_max ≤ 10 phase boundary) is what makes the W-5 cross-axis joint-win pattern available for the K=4 → K=5 advancement under the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern (per workshop header line 43). The hybrid verdict (d) — Reading A wins on L_max ≤ 10 phase boundary; Reading B's operational-parameterization framing wins on L_max=12 anchor mismatch — is consistent with this convergence pattern at the L_max ≤ 10 axis while preserving the L_max=12 operational-machinery distinction as a separate refinement axis.

#### Re: V2 — L_max=12 anchor mismatch interpretation

**DISAGREE** (Reading B defense on the L_max=12 anchor mismatch interpretation; the 1.428 mismatch IS structurally an operational-machinery distinction at the P_BdG projector implementation layer, NOT a substrate-IS structural separation of two regimes).

V2's claim (workshop lines 81-99) that the L_max=12 FULL-BdG anchor mismatch IS "a SUBSTRATE-PHYSICS structural separation between two distinct substrate-IS regimes" is structurally over-strong at the L_max=12 layer (it conflates the L_max ≤ 10 phase boundary, where I concede Reading A, with the L_max=12 anchor mismatch where the structural argument is different). At L_max=12 BOTH operational routes — scalar-Δ FULL-BdG gap-equation self-consistency AND s52 multi-branch ED tensor application — produce a finite gap (Δ(12)=0.4643 from scalar self-consistency; Δ_per_mode=(0, 0.7704, 0.176) from s52 ED). There is NO phase boundary at L_max=12 separating these two evaluations; both are post-transition.

**The 1.428 anchor mismatch is structurally a P_BdG projector implementation distinction**:

Per W8-3 line 511-512 (gen-physicist adversarial Q3, verbatim): "These two routes BOTH compute the same Cell IV substrate-IS observable (variance of Bogoliubov occupation at K_horizon) on the substrate algebra `A_K`, but they evaluate it on different operational machineries — the s52 route preserves the multi-branch ED solution; the FULL gap-equation route imposes a scalar Δ self-consistency. The non-equality `L_emp(12)_FULL ≠ L_emp(12)_s52` is structurally informative: it tells us that the BdG sub-algebra observable's L_max=12 value depends on whether one carries the multi-branch ED structure or solves the gap equation at the canonical scalar value."

This Q3 statement is the substrate-IS-side concession at the L_max=12 layer: **the registry text Element-1 (§VII.AV line 17918) declares a SINGLE substrate-IS observable — the Corner-IV K-window log-derivative on `M_2(ℂ) ⊂ A_K`** — but the operational evaluation of `Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})` depends on the P_BdG projector implementation. Per the Bogoliubov closed form from §VII.U.2 Corner II Var_a parse-tree expansion at line 12961, `P_BdG = diag(|v_a|², |u_a|²)` where `|v_a|² = (1 − ε_a/E_a)/2` with `E_a = sqrt(ε_a² + Δ_a²)`. The `Δ_a` enters the projector through the BdG amplitude structure: scalar Δ_a = Δ_canonical ⟹ uniform projector; multi-branch Δ_a = (B1, B2, B3) per-mode ⟹ non-uniform projector.

These ARE two structurally distinct operational implementations of P_BdG at the same L_max=12 spectrum. Both evaluate `Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})|_{s→4}` per the registry-text Element-3 bridge map (Connes-Moscovici 1995 §III.4 residue formula), but they assign different `|v_a|²` weights to the underlying spectral kernel. The numerical result differs by 1.428 absolute units (L_emp_FULL(12) = −5.6188 vs L_emp_s52(12) = −7.0463).

**Structural argument for operational-machinery interpretation**:

Under the algebra-axis 4-corner partition (§VII.U.2 Corner II Var_a parse-tree closed form line 12961), the K-window log-derivative is `state-pair functional on the BdG sub-algebra` (Cell IV per §VII.AV registry line 17901). The state pair includes the (`Δ_a`-dependent) Bogoliubov-amplitude tensor in its STATE-SIDE specification. Two state-pair functionals with different state-side specifications are structurally distinct OPERATIONAL EVALUATIONS of what the registry text DECLARES as a single substrate-IS observable. The substrate-IS observable's "value" at L_max=12 is therefore not unique without a state-side pin — and the §VII.AV registry text Element-1 (line 17918) DOES NOT pin the state-side Bogoliubov-amplitude tensor.

This is a structural ambiguity at the registry-text layer that the §W5-2 anchor pin `L_emp(L_max=12) = −7.046336474406761 M_KK²` (registry line 17926) partially discharges (it pins the multi-branch s52 tensor as the canonical anchor — line 17926 cites `s88-pending-edits-ledger.md` "preserve K-window log-derivative anchor `−7.046336` as SOLE Corner-IV calibration source"). The FULL-BdG re-derivation at scalar Δ_canonical IS a DIFFERENT operational evaluation; the 1.428 mismatch is the structural distance between the two operational implementations of P_BdG.

**Engagement with V2's forward question** (lines 109-111; "under what NCG-axiomatic constraint at the Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula does the choice of Bogoliubov-amplitude tensor (scalar Δ vs multi-branch B1/B2/B3) become STRUCTURALLY IRRELEVANT to the residue evaluation?"):

The honest NCG-axiomatic answer is: **NO such universal invariance argument exists at the L_max=12 evaluation layer**. The Connes-Moscovici §III.4 residue formula evaluates `Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})|_{s→4}` — the residue value DEPENDS on the P_BdG projector specification because P_BdG is a structural input to the formula, not a derived quantity. Different P_BdG implementations produce different residue values.

HOWEVER (and this is the structurally consequential observation for Reading B): the Hochschild-Künneth Morita-invariance `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` from W-4 verdict provides an INVARIANCE argument at a STRUCTURALLY DIFFERENT layer: it asserts that the Hochschild cohomology of the BdG sub-algebra is Morita-equivalent to the parent A_F Hochschild cohomology, INDEPENDENT of the P_BdG projector implementation. This Morita-invariance is operative at the COHOMOLOGY-CLASS layer (Level 1 cohomology-class identity), NOT at the residue-value layer (Level 3 empirical anchor).

The W3 A.14 regulator-INVARIANT cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.3249743784` per W8-7 (b) lines 1394-1401 IS a Hochschild-Künneth Morita-invariant — it lives at the cohomology-class layer. It is regulator-INVARIANT (FI axis) AND projector-INVARIANT (the cocycle ratio is a property of the Hochschild homology of A_K, not of the P_BdG projector on the BdG sub-algebra image). Therefore the W3 A.14 cocycle ratio IS reproducible at L_max=12 UNDER BOTH OPERATIONAL ROUTES (scalar Δ AND multi-branch B1/B2/B3) at the Level-1 cohomology-class identity layer — this is the cross-anchor that pins the substrate-IS identity at the cohomology-class layer in a P_BdG-implementation-INVARIANT manner.

The structural distinction Reading B preserves: the Level-1 cohomology-class identity IS P_BdG-invariant (Morita); the Level-3 empirical anchor at L_max=12 is P_BdG-dependent (operational). The §VII.AV registry text's three-level ladder ALREADY encodes this distinction by placing the cocycle ratio at Level 1 and the L_emp anchor at Level 3. The 1.428 anchor mismatch lives at Level 3 ONLY — it does NOT propagate to Level 1.

**AGREE** (partial; on V2's distinction between two operational machineries computing different residue values).

V2 lines 101-107 explicitly engages with my likely counter-claim "same observable, different operational machineries on M_2(ℂ)" and CONCEDES at line 105: "Connes is correct that the observable is the same at the parse-tree-expansion layer (Var_a closed-form Cell-IV per §VII.U.2 Corner II corrigendum line 12961, lifted to Cell-IV under the K-window log-derivative state-pair functional family)." This is the structurally honest framing: the SUBSTRATE-IS observable IS the same; the OPERATIONAL EVALUATION at L_max=12 differs by P_BdG implementation.

V2's subsequent strong claim — "the SAME observable evaluated on STRUCTURALLY DISTINCT Bogoliubov-amplitude tensors at the canonical pin produces STRUCTURALLY DISTINCT numerical results IFF the two tensors inhabit different substrate regimes — which is precisely what the BCS phase transition at L_max=10 → 11 ESTABLISHES" — conflates the L_max ≤ 10 phase boundary (where Reading A wins per Re:V1) with the L_max=12 anchor mismatch (where the two tensors BOTH inhabit post-transition spectral content). At L_max=12 both routes are in the post-transition spectral regime; the 1.428 mismatch is therefore NOT structurally licensed by the phase transition argument.

**MISSED** (V2 does not yet leverage the §VII.AS / §VII.AQ Reading A vs Reading B precedent's structural lesson):

The S89 W-5 §VII.AQ workshop's R3 resolution (the "Reading A wins" precedent) established that the substrate-natural Level-3 anchor IS the FULL-LEAF-FOLIATION / FULL-SCOPE evaluation, NOT a cache-projection / restricted-scope evaluation (cf. `s89-w5-vii-aq-level3-binding.md` §C1 line 27 "the Level-3 anchor is *by definition* the full-scope evaluation"). The structural lesson generalizes: when two evaluations of "the same substrate-IS observable" differ by MACHINERY SCOPE choice, the substrate-IS Level-3 anchor IS the canonical-machinery-scope evaluation pinned by the registry-text Element-3 bridge map.

For §VII.AV, the registry-text Element-3 bridge map (line 17922) declares "Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` restriction" with Element 3 fiducial-anchor binding type (i) substrate-self-consistent: "the bridge map composes through the substrate-IS pin `L_emp(L_max=12) = -7.046336474406761` which IS the framework prediction at the same algebra-axis family". The §W5-2 anchor IS pinned as the canonical-machinery-scope evaluation at Element 3.

This is the structural argument Reading B leverages: under the §VII.AQ Reading A precedent, the canonical-machinery-scope evaluation for §VII.AV's Level-3 anchor IS the s52 multi-branch ED tensor application at L_max=12 (the −7.046336 pin); the FULL-BdG scalar-Δ re-derivation at L_max=12 is an ALTERNATIVE machinery scope. The 1.428 mismatch is the structural distance between the two machinery scopes — and CF-71's K_canonical pin uniqueness investigation IS the operational-machinery-side investigation that would resolve which P_BdG projector implementation IS the canonical-machinery-scope at L_max=12.

The Reading A in V2's framing strongly claims that "the configuration space contains no such common solution" (V4 forward question line 229) — but this claim is NOT NCG-axiomatically derivable ahead of the discriminator gate. The configuration space of P_BdG projector implementations at L_max=12 is constrained but not trivial; the s52 multi-branch tensor is one element; the scalar-Δ FULL-BdG tensor is another; whether they CAN be reconciled via K_canonical re-pinning at the K-window observable definition layer is a substrate-physics empirical question that the V4 discriminator gate adjudicates.

**EMERGES** (cross-domain insight):

The structural pattern emerging from Re:V1 + Re:V2: V1's L_max ≤ 10 phase boundary IS substrate-IS (Reading A wins at this layer); V2's L_max=12 anchor mismatch IS operational-machinery distinction at the P_BdG projector implementation layer (Reading B wins at this layer). These are NOT competing readings of THE SAME phenomenon; they are readings of TWO STRUCTURALLY DISTINCT layers of the CF-61 FAIL evidence chain:

1. **Layer 1 — L_max ≤ 10 trivial-Δ regime**: substrate-IS Cooper-instability criterion fails on the truncated spectral kernel at canonical V_BCS. Reading A wins.
2. **Layer 2 — L_max=12 anchor mismatch 1.428**: operational P_BdG projector implementation distinction (scalar Δ vs multi-branch). Reading B wins.

This two-layer structure is what motivates the hybrid verdict (d) — "substrate phase boundary AT operational-machinery joint layer" (option (d) per workshop header line 39). Both readings are partially-correct; they apply to structurally distinct layers of the CF-61 evidence chain. CF-70 (Reading A's canonical PROXY-REFINEMENT route via FULL CC multipliers) addresses Layer 1 by reconstructing the BCS gap equation under a UV-finite kernel that evades the phase boundary at canonical V_BCS; CF-71 (Reading B's K_canonical pin uniqueness investigation) addresses Layer 2 by resolving the P_BdG projector implementation distinction at L_max=12. They are NOT mutually exclusive refinement routes; they operate at structurally distinct layers.

#### Re: V3 — §VII.AV refinement pathway under Reading A

**AGREE** (qualified; CF-70 IS a substrate-natural PROXY-REFINEMENT route at the Level-1 cohomology-class identity layer).

V3 lines 117-131 correctly identifies CF-70 as the canonical FULL Connes-Chamseddine 1996 §2.2-2.3 PROXY-REFINEMENT route per the registry-text §VII.AV refinement-pathway table at lines 17942-17948 (route (iii): "FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers"). The W8-7 (c) PRIMARY 2-point Pauli-Villars pipeline at Λ_UV = M_KK (M_1 = M_KK, M_2 = √2·M_KK, c_1 = +2, c_2 = −1) per `_pauli_villars_subtraction.py` (input_sha256 = `eaf98037ddc2a4d7…` per W8-7 (c) lines 1405-1411) satisfies the two Connes-Chamseddine consistency identities at machine precision:

- Σ c_r = 1.0 exact (W8-7 (c) line 1410);
- Σ c_r·m_r² = −4.4408920985006262e−16 ≈ 0 at machine precision (W8-7 (c) line 1411; "no quadratic divergence" identity).

These two identities ARE the NCG-axiomatic consistency conditions for the FULL physical Pauli-Villars regularization in Connes-Chamseddine 1996 §2.2-2.3 — the first reproduces the unit residue at substrate-distance-1 pole (UV identity reproduction); the second cancels the quadratic divergence at the substrate-distance-2 pole's leading-UV contribution. This IS the substrate-natural FULL physical pipeline at the Level-1 cohomology-class identity layer, AND it reproduces the W3 A.14 cocycle ratio 7.3249743784 (regulator-INVARIANT across {ζ, PV, Mellin, cutoff}) per the FI axis classification at W8-7 (b) line 1401.

The Level-1 cohomology-class cross-anchor argument V3 lines 133-139 makes is structurally CORRECT: any substrate-IS-faithful refinement of the §VII.AV deferred-pending pathway MUST reproduce the regulator-INVARIANT cocycle ratio 7.3249743784 at the Level-1 cohomology-class identity layer. CF-70's FULL CC multipliers refinement IS expected to satisfy this cross-anchor by construction (the FULL physical PV pipeline at Λ_UV = M_KK preserves the substrate's cocycle structure on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` because the regularization commutes with the Hochschild differential at the cohomology-class layer per Connes 1985 cyclic-cohomology framework).

**DISAGREE** (CF-71 is NOT structurally deferred to "operational-machinery layer only"; CF-71 operates on a structurally consequential P_BdG projector implementation distinction at the Level-3 anchor layer that CF-70 does NOT address).

V3 lines 153-157 frames CF-71 as "tuning operation at the OPERATIONAL layer (K-window definition / Bogoliubov tensor-choice / projector P_BdG implementation choice)" that "does NOT resolve the substrate-IS phase transition at L_max ≤ 10". This framing is partially correct (CF-71 does NOT address the L_max ≤ 10 phase boundary; that is CF-70's domain) but understates CF-71's structural role at the L_max=12 anchor mismatch layer.

Per Re:V2 above: the L_max=12 anchor mismatch 1.428 is structurally a P_BdG projector implementation distinction (scalar Δ vs multi-branch B1/B2/B3), NOT a residual substrate-physics phase boundary at L_max=12 (both routes are post-transition at L_max=12). CF-71's K_canonical pin uniqueness investigation operates at a STRUCTURALLY DISTINCT layer from CF-70:

- **CF-70 operates at the BCS GAP-EQUATION REFINEMENT layer**: it replaces the unsubtracted gap equation (which fails at L_max ≤ 10 at canonical V_BCS) with a PV-regulated gap equation (which converges across L_max ∈ {6..12} at canonical V_BCS because the PV-subtracted kernel is UV-finite). The output is a smooth Δ(L_max) sequence that admits the Level-2 envelope `α ∈ [2.5, 3.5]` extraction.
- **CF-71 operates at the K-WINDOW OBSERVABLE DEFINITION layer**: it resolves the P_BdG projector implementation choice (scalar Δ vs multi-branch tensor) at L_max=12 by deriving K_canonical from substrate-IS first principles (the BdG energy gap at τ_fold under CF-62 disambiguation). The output is a uniquely-specified P_BdG projector implementation at L_max=12 that aligns the FULL-BdG anchor with the §W5-2 canonical anchor −7.046336 (or doesn't — that's what the discriminator gate adjudicates).

These are NOT redundant or competing refinement routes; they operate at structurally orthogonal axes:

| Axis | CF-70 | CF-71 |
|:-----|:------|:------|
| L_max ≤ 10 phase boundary | ADDRESSES (PV-regulated kernel evades the criticality crossing) | DOES NOT ADDRESS (operates at L_max=12 only) |
| L_max=12 anchor mismatch (P_BdG implementation) | DOES NOT ADDRESS (CF-70 also uses scalar Δ self-consistency by construction) | ADDRESSES (resolves P_BdG implementation distinction) |
| W3 A.14 cocycle ratio cross-anchor at L_max ≤ 10 | EXPECTED TO SATISFY (FULL CC pipeline preserves cohomology class) | NOT APPLICABLE (CF-71 operates only at L_max=12) |
| Level-1 cohomology-class identity layer | OPERATIVE (reconstructs Level-2 envelope under FULL physical kernel) | INVARIANT (W3 A.14 cocycle ratio is Morita-invariant under P_BdG choice per Hochschild-Künneth) |
| Level-3 empirical anchor at L_max=12 | RECOMPUTED (under PV-regulated kernel) | ALIGNED (via K_canonical re-pinning) |

**Engagement with V3's forward question** (lines 159-161; "under what NCG-axiomatic argument does CF-71's K_canonical re-tuning recover the Level-1 cohomology-class identity (`ratio_φ67_φ88 = 7.324992`) at L_max=10 on the SCHEMATIC proxy class?"):

The honest NCG-axiomatic answer: **CF-71 does NOT recover the Level-1 cohomology-class identity at L_max=10 on the SCHEMATIC proxy class — and it does NOT need to**. CF-71 operates only at L_max=12; the W3 A.14 cocycle ratio at L_max ≤ 10 IS NOT in CF-71's scope. V3's forward question presupposes a refinement scope that CF-71 does not claim.

CF-71's structural role under Reading B's framing is narrower than V3's strawman characterization: CF-71 investigates the K_canonical pin uniqueness at the L_max=12 K-window observable definition layer (resolving the P_BdG projector implementation distinction at L_max=12), NOT the SCHEMATIC proxy class's L_max ≤ 10 behavior. The §W5-3 Casimir-bound proxy at L_max ≤ 10 IS structurally falsified per Re:V1 (Reading A wins on the L_max ≤ 10 phase boundary); CF-71 does not rescue it. What CF-71 rescues (if successful) is the §VII.AV Level-3 empirical anchor MATCH at L_max=12 between the canonical §W5-2 anchor and the FULL-BdG re-derivation — a separate structural question from "is the SCHEMATIC proxy a faithful image at L_max ≤ 10".

**Dispatch ordering options** (V3's CF-70 prioritization vs CF-71 prioritization vs wave-together):

Under the hybrid verdict (d) framing, the dispatch ordering question is structural:

- **Option α (CF-71 → CF-70 sequential; Reading B prioritized)**: CF-71 first resolves the P_BdG projector implementation distinction at L_max=12. If CF-71 PASSes (K_canonical aligns the FULL-BdG L_max=12 anchor with §W5-2 −7.046336 at < 1e-9 tolerance), then CF-70 is dispatched on the aligned P_BdG implementation to reconstruct the Level-2 envelope under FULL CC multipliers. STRUCTURAL LICENSE: under the §VII.AQ Reading A precedent, the canonical-machinery-scope evaluation at Level-3 IS the substrate-self-consistent pin (§VII.AV Element 3 binding type (i)); CF-71 establishes the canonical machinery scope BEFORE the Level-2 envelope refinement. STRUCTURAL RISK: if CF-71 FAILs (no K_canonical re-pinning aligns the FULL-BdG anchor with §W5-2), the structural distinction at L_max=12 is confirmed as a substrate-IS structural separation (Reading A's V2 strong claim wins), and CF-70 is then the canonical refinement route at the Level-2 envelope layer.

- **Option β (CF-70 → CF-71 sequential; Reading A prioritized)**: CF-70 first reconstructs the Level-2 envelope under FULL CC multipliers across L_max ∈ {6..12}. If CF-70 PASSes (α ∈ [2.5, 3.5] AND L_max=12 anchor bit-match < 1e-9 under FULL CC route), then CF-71 is dispatched only as a follow-up consistency check (does the FULL CC-route P_BdG implementation align with the canonical §W5-2 multi-branch implementation?). STRUCTURAL LICENSE: under Reading A's strong form (CF-70 IS the substrate-IS canonical refinement route), CF-71 is structurally subordinate. STRUCTURAL RISK: if CF-70 PASSes WITHOUT addressing the P_BdG implementation distinction (the FULL CC route produces its own L_max=12 anchor that may differ from the §W5-2 multi-branch anchor), the L_max=12 anchor mismatch may PERSIST under FULL CC refinement, leaving CF-71 as a residual open question.

- **Option γ (CF-70 + CF-71 wave-together; verdict (c) refinement pathway space carries both)**: dispatch both CF-70 and CF-71 in parallel; cross-check their outputs at the L_max=12 anchor layer. STRUCTURAL LICENSE: this matches the workshop pre-registered structural verdict option (c) — "refinement pathway space carries both"; both CF-70 and CF-71 are independent forward routes; the V4 discriminator gate fires first to determine which Reading dominates. STRUCTURAL RISK: dispatch effort doubles; if both PASS, the cross-axis joint-win pattern (W-5 K=4 → K=5 advancement candidate) is achieved; if both FAIL, the §VII.AV deferred-pending refinement-pathway requires a third route not currently pre-registered.

Reading B's steelman position is Option γ (wave-together), with the V4 discriminator gate `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` firing FIRST to adjudicate the L_max=12 anchor layer Reading A vs Reading B verdict. The discriminator gate's outcome routes the subsequent dispatch:

- **Discriminator PASS (Reading B confirmed at L_max=12)**: CF-71 prioritized; CF-70 follows under aligned P_BdG implementation.
- **Discriminator FAIL (Reading A confirmed at L_max=12)**: CF-70 prioritized; CF-71 demoted to operational-machinery-side investigation.
- **Discriminator INFO (intermediate)**: CF-70 + CF-71 wave-together at S91+; refinement-pathway space carries both per workshop verdict (c).

**MISSED** (NCG-axiomatic machinery V3 does not fully leverage):

V3's argument that "the SCHEMATIC proxy is structurally falsified at the Level-1 layer regardless of whether CF-71 aligns the Level-3 empirical anchor at L_max=12" (V3 lines 159-161) is structurally CORRECT but UNDER-states the asymmetry: at the Level-1 cohomology-class identity layer, the W3 A.14 cocycle ratio 7.3249743784 IS Morita-invariant under Hochschild-Künneth `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` (per W-4 verdict). This Morita-invariance is INDEPENDENT of the P_BdG projector implementation AND independent of the scalar-Δ vs multi-branch tensor choice. Therefore CF-70 and CF-71 BOTH inherit the Level-1 cohomology-class identity preservation at the Hochschild homology layer — they are NOT structurally distinguishable at Level 1; they distinguish only at the Level-2 envelope and Level-3 empirical anchor layers.

This Morita-invariance argument SHARPENS Reading A's Level-1 cross-anchor argument: the Level-1 cohomology-class identity is preserved under BOTH refinement routes by construction; the structural verdict at the Level-1 layer is therefore NOT discriminatory between CF-70 and CF-71. The discriminatory power lies at Level 2 (where CF-70 reconstructs the algebraic envelope `L^{-3}` under FULL CC physical multipliers and CF-71 does not — CF-71 is L_max=12-only) and Level 3 (where CF-71 resolves the P_BdG implementation distinction and CF-70 may or may not align with the §W5-2 anchor depending on its own P_BdG implementation choice).

**EMERGES** (cross-domain insight on dispatch ordering):

The structural cleanest dispatch ordering under the hybrid verdict (d) framing is:

```
Step 1 — V4 discriminator gate (S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST) fires FIRST
Step 2 — Outcome routes the subsequent CF-70 vs CF-71 prioritization:
         PASS (Reading B confirmed at L_max=12) → CF-71 → CF-70 sequential (Option α)
         FAIL (Reading A confirmed at L_max=12) → CF-70 → CF-71 sequential (Option β)
         INFO (intermediate)                    → CF-70 + CF-71 wave-together (Option γ)
```

This matches workshop verdict option (c) "refinement pathway space carries both" with the discriminator gate as the canonical substrate-physics adjudicator. The dispatch ordering is itself the substrate-physics-adjudication-driven structural verdict; the W-5 cross-axis joint-win pattern at K=5 advancement requires this dispatch-ordering convergence between Reading A and Reading B authors.

#### Re: V4 — Pre-registered S91+ discriminator gate

**AGREE** (the `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` discriminator gate pre-registration is NCG-axiomatically sound at the substrate-physics adjudication layer).

V4 lines 165-229 pre-registers a substrate-physics adjudicator gate that satisfies the canonical pre-registration discipline per `epistemic-discipline.md §"Pre-Registration Completeness"`:

1. **PRDR machinery enumeration** (9-pin input map at workshop lines 175-185): each pin is named with its source audit_sha or input_sha (e.g., CF-61 `6357ab9650615732363c24d89e588569dc5c37f04bef7362e538b1677335b716`; W3 A.14 `d0683bcd31e7eaca…`); the closure-SHA scope is well-defined.
2. **Pre-registered PASS criterion** (workshop lines 187-192): double constraint requiring the SAME (B1, B2, B3) configuration to BOTH align with the scalar-Δ FULL-BdG output (< 1e-3 relative) AND reproduce the canonical anchor −7.046336 (< 1e-3 relative). This is structurally consequential because it forbids confirmation-bias (a configuration that aligns with EITHER coordinate alone does NOT PASS).
3. **Pre-registered FAIL criterion** (workshop lines 200-203): ∀-quantified non-existence of any admissible (B1, B2, B3) meeting even the relaxed 10% tolerance in BOTH coordinates simultaneously. This is the strong-form structural separation criterion.
4. **Pre-registered INFO criterion** (workshop lines 211-214): partial alignment in one coordinate but not both at machine precision; routes to verdict (c) "refinement pathway space carries both".
5. **Verifier rubric** (workshop lines 223-225): cross-check via W3 A.14 cocycle ratio Level-1 cross-anchor preservation; this satisfies the Verifier-Rubric Pre-Registration Class 8.2 MANDATORY discipline per `epistemic-discipline.md §"Verifier-Rubric Pre-Registration"`.

The discriminator gate's structural property "this discriminator gate is genuinely SUBSTRATE-PHYSICS-RESOLVING — neither workshop debate nor methodology adjudication can pre-empt its verdict" (workshop line 225) is correct per the §VII.AQ / §VII.AS dual-reading-with-substrate-physics-adjudicator precedent at S88 W-18 / S89 W-5. The configuration sweep is a finite, well-defined numerical computation on the substrate's L_max=12 spectrum cache `s84_spectrum_cache_L12_tau019.npz` (cache_sha256 = `9e6d9cf7fd6a6949…` per W8-7 (d) line 1417), and the verdict is the FAIL / PASS / INFO classification of the alignment outcome under the pre-registered tolerance bands.

**DISAGREE** (V4's forward question framing at lines 227-229 — "if the configuration space contains no such common solution... then Reading A is confirmed at the NCG-axiomatic layer BEFORE the discriminator gate even runs" — overstates what NCG-axiomatic machinery can derive ahead of the empirical configuration sweep).

V4's forward question conjecture (verbatim line 229): "if the answer is 'the configuration space contains no such common solution' (the gap-equation self-consistency at L_max=12 forces scalar Δ_canonical=0.4643 with uniform rescale, which is NOT in the s52 multi-branch (B1, B2, B3) family), then Reading A is confirmed at the NCG-axiomatic layer before the discriminator gate even runs".

This conjecture is structurally consequential but NOT NCG-axiomatically derivable from first principles without empirical configuration sweep evidence. The reasoning gap is:

1. **The gap-equation self-consistency at L_max=12 produces scalar Δ_canonical = 0.4643** — this is a substrate-physics fact (Δ(12) = 0.4643 per W8-3 Step 3 line 363).
2. **The s52 multi-branch family (B1=0, B2=0.7704, B3=0.176) ≠ scalar Δ_canonical = 0.4643** — this is a numerical observation but NOT a structural impossibility statement. The multi-branch family is one POINT in the configuration space; the FULL configuration space (workshop line 221: 20 × 20 × 20 = 8000 configurations with ×3 refinement near canonical s52) contains many other points.
3. **The question is whether ANY point in the 8000-configuration space PRODUCES BOTH (i) gap-equation self-consistency at L_max=12 AND (ii) K-window log-derivative anchor match against −7.046336**. This is empirical, not NCG-axiomatic.

The honest NCG-axiomatic position: the configuration space of P_BdG projector implementations at L_max=12 is constrained by Hochschild-Künneth Morita-invariance at the cohomology-class layer (preserving W3 A.14 cocycle ratio 7.3249743784) BUT is NOT constrained to the s52 multi-branch tensor at the Level-3 empirical anchor layer. The Connes-Karoubi pairing on the BdG sub-algebra image admits a CONFIGURATION FAMILY of P_BdG implementations at L_max=12 — each with its own (|v_a|², |u_a|²) per-mode weights determined by the Δ_a tensor structure — that ALL satisfy the cohomology-class identity at Level 1. The structural question at Level 3 is whether ANY P_BdG implementation in this family simultaneously satisfies both alignment criteria; this is what the discriminator gate adjudicates.

**Engagement with V4's forward question** (lines 227-229; "under what cyclic-cohomology constraint does the (B1, B2, B3) configuration space contain a unique solution that satisfies BOTH (i) gap-equation self-consistency at canonical (V_BCS, T_fold), (ii) K-window log-derivative anchor match against the canonical −7.046336?"):

The honest NCG-axiomatic answer: **the cyclic-cohomology constraint at Level 1 (W3 A.14 cocycle ratio preservation) IS a NECESSARY but NOT SUFFICIENT condition on the (B1, B2, B3) configuration space at L_max=12 — and the (i)+(ii) joint constraint at Level 3 is a SEPARATE structural question that the cyclic-cohomology constraint does not pre-determine**.

This is structurally consequential: the W3 A.14 cocycle ratio is invariant under MOST P_BdG implementations in the configuration space (per Hochschild-Künneth Morita-invariance argument). The (i)+(ii) joint constraint at Level 3 is a STRONGER condition that constrains the configuration space further. The 8000-configuration sweep in V4 is structurally testing whether ANY P_BdG implementation simultaneously satisfies the Level-1 Morita-invariance AND the Level-3 joint alignment. This is an EMPIRICAL question, not an NCG-axiomatic determination.

**V4 forward question conjecture re-stated structurally**:

V4's conjecture is: "the configuration family of P_BdG implementations satisfying gap-equation self-consistency at L_max=12 (i.e., the family solving Δ_self_consistent(L_max=12, P_BdG)= Δ_canonical(P_BdG)) does NOT intersect the configuration family satisfying K-window log-derivative anchor match against −7.046336 (i.e., the family producing L_emp(L_max=12, P_BdG) = −7.046336)". This is a substrate-physics structural claim about the geometry of the configuration space; it is NOT derivable from NCG-axiomatic machinery alone.

The discriminator gate's role IS to empirically test this conjecture. The outcome routes the structural verdict per V4 lines 193-218.

**MISSED** (the V4 pre-registration does not yet enumerate the Element 3 fiducial-anchor binding type for the discriminator gate):

Per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` (S88 W-15 V.7 SUGGESTION-K=1, sharpened at S90 W7-4 CF-57 axis γ for canonical-import-binding vs substrate-natural-binding discrimination), any bridge entry whose pre-substrate pin is itself a laboratory-IN observable at a different pillar MUST declare which incarnation is binding: (i) substrate-self-consistent / (ii) external-observation / (iii) joint-hypersurface.

For the V4 discriminator gate, the pre-substrate pin is the §W5-2 canonical anchor `L_emp(L_max=12) = −7.046336474406761`. This anchor IS framework-prediction (substrate-self-consistent, type (i)) per §VII.AV registry text Element 3 lines 17922-17923. HOWEVER, the V4 pre-registration also references the FULL-BdG re-derivation output `L_emp_FULL_BdG_scalar_Delta(L_max=12) = −5.6188` per CF-61 — this is ALSO a framework-prediction at a DIFFERENT operational machinery scope.

The V4 discriminator gate is structurally a **dual-anchor joint-hypersurface test** at the Level-3 layer: it tests whether the (B1, B2, B3) configuration space contains a point projecting to BOTH the §W5-2 anchor AND the FULL-BdG anchor. This is type (iii) joint-hypersurface binding per the Element 3 sharpening at S90 W7-4 CF-57 — the lab discrimination IS 2D in (anchor_1, anchor_2) space rather than 1D in observable space alone.

This should be declared explicitly in the V4 pre-registration: the convention tag should carry `-JOINT-HYPERSURFACE-DUAL-ANCHOR` per Element 3 binding type (iii) clause. Without this declaration, the gate inherits the §VII.AV registry text Element 3 type (i) substrate-self-consistent binding which conflates with the discriminator gate's structurally distinct dual-anchor role.

**Sharpening proposed for V4 pre-registration**:

The V4 pre-registration's input-pin map (workshop lines 175-185) should additionally:

1. **Explicit Element 3 type (iii) joint-hypersurface declaration**: the V4 discriminator gate is a dual-anchor joint-hypersurface test; convention tag should be `convention=substrate-IS-canonical-K-window-log-derivative-MULTI-BRANCH-S52-VS-SCALAR-DELTA-FULL-BDG-ADJUDICATION-JOINT-HYPERSURFACE-DUAL-ANCHOR L_max=12`.
2. **Element 3 fiducial-anchor binding sub-class pin**: per the W7b-82 K=1 SUGGESTION at `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` Binding-axis row, the gate should disclose whether the §W5-2 anchor is `canonical-import-binding` (pin imported from S87 W2-3 calibration) or `substrate-natural-binding` (re-derived from substrate-IS first principles at L_max=12). The honest declaration is `canonical-import-binding` (the −7.046336 was computed at S87 W2-3 against the s52 multi-branch tensor; per the §VII.AQ Reading A precedent, this is the canonical-machinery-scope pin per Element 3 type (i)).
3. **Admissible-configuration-space sub-pin**: the (B1, B2, B3) sweep grid should be refined NOT ONLY near the canonical s52 point (workshop line 221: "finer ×3 refinement near the canonical s52 point") but ALSO near the scalar-Δ FULL-BdG implementation (B1 = B2 = B3 = Δ_canonical(L_max=12) · |v|² weight = 0.4643 · weight). This second refinement region tests whether the FULL-BdG scalar-Δ implementation has a multi-branch "lift" that aligns with the §W5-2 anchor — directly the Reading B-favored configuration.
4. **Per-stage convergence-of-evidence criteria**: discriminator gate outcome is binary (PASS/FAIL/INFO), but the intermediate evidence at each configuration evaluation should be recorded. The npz output should include the full (8000 + ×3 × 2 refined regions) × 2 alignment criteria = ~16,000 + evaluation rows for forensic post-hoc analysis.

These sharpening proposals do NOT change the PASS/FAIL/INFO criteria; they enrich the audit trail and address the structural ambiguity at Element 3 binding type.

**Engagement with the discriminator gate's expected outcome**:

Reading B's prediction: the discriminator gate returns INFO (intermediate alignment in one coordinate but not both at machine precision). The structural reason: the s52 multi-branch tensor (B1=0, B2=0.7704, B3=0.176) BY CONSTRUCTION reproduces the §W5-2 anchor −7.046336 (this is the canonical anchor's source); the question is whether this same configuration ALSO reproduces the scalar-Δ FULL-BdG output −5.6188 within 10% tolerance. Per the numerical observation `|L_emp_s52(12) − L_emp_FULL(12)| = 1.428 ≫ 0.10 · |L_emp_FULL(12)| = 0.5619`, the canonical s52 configuration does NOT satisfy this tolerance. Reading B then conjectures: a (B1, B2, B3) configuration NEAR the FULL-BdG scalar-Δ implementation (e.g., uniform amplitude with rescaled B-magnitudes) MAY align with the FULL-BdG output but will NOT exactly match the §W5-2 −7.046336 anchor (because the §W5-2 anchor was constructed against the specific multi-branch s52 tensor, not a uniform scalar tensor).

Therefore Reading B's empirical prediction is INFO — the configuration space contains points aligned with EACH coordinate alone, but no point simultaneously aligned with BOTH at machine precision. This routes the verdict per workshop lines 215-218 to "refinement pathway space carries BOTH CF-70 + CF-71 as wave-together at S91+" — consistent with the hybrid verdict (d).

Reading A's prediction (per V4 conjecture at line 229): the discriminator gate returns FAIL (no configuration aligns within even the relaxed 10% tolerance in BOTH coordinates). This routes the verdict per workshop lines 204-207 to "Casimir-bound proxy class STRUCTURALLY CLOSED + CF-70 prioritized + CF-71 demoted to operational-machinery investigation".

The empirical verdict at S91+ adjudicates between these two predictions; neither Reading can pre-empt the verdict at the NCG-axiomatic layer without the empirical configuration sweep.

**EMERGES** (cross-domain insight on the discriminator gate's structural reach):

The V4 discriminator gate at L_max=12 tests the L_max=12 anchor mismatch layer ONLY; it does NOT test the L_max ≤ 10 phase boundary (where Reading A wins per Re:V1). This is structurally appropriate — the discriminator gate's scope IS the operational-machinery distinction at L_max=12, NOT the substrate-physics phase boundary at L_max ≤ 10.

Under the hybrid verdict (d) framing, the discriminator gate's outcome routes the L_max=12 anchor mismatch resolution; CF-70 then independently addresses the L_max ≤ 10 phase boundary via FULL CC physical multipliers (PV-regulated kernel evading the criticality crossing). The two refinement routes operate at structurally orthogonal layers; the discriminator gate's outcome is informative about the L_max=12 layer but NOT determinative for the L_max ≤ 10 layer (where CF-70 is canonical regardless of discriminator outcome).

This is the structural distinction that motivates Option γ (wave-together) dispatch ordering: the discriminator gate fires FIRST to resolve the L_max=12 layer, then CF-70 + CF-71 dispatch in parallel to address their respective orthogonal layers. The W-5 cross-axis joint-win pattern at K=5 advancement requires this two-stage dispatch structure to satisfy both Reading A's L_max ≤ 10 phase boundary refinement (via CF-70) AND Reading B's L_max=12 anchor mismatch resolution (via CF-71).

#### Re: V5 — Substrate framing Level-1 vs Level-2

**AGREE** (the §VII.AV substrate-IS observable IS Level-1 single-τ-slice at the registry-text layer per the MANDATORY-K=2 declaration at line 17918, AND the BCS gap-equation kernel sum at fixed τ_fold IS structurally a Level-1 single-τ-slice spectral-action moment).

V5 lines 233-247 correctly identifies the structural layering:

1. **§VII.AV registry text line 17918** carries the EXPLICIT TAG "Level 1 single-τ-slice at τ_fold = 0.19" MANDATORY per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4.
2. **CF-63 provenance line 17895** co-signs the Level-1 declaration with volovik-superfluid-universe-theorist as "(Level-1 single-τ-slice declaration MANDATORY per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 + Forward-looking enforcement)".
3. **`phononic-framing.md §"Level 1 — Single-τ-slice substrate-IS"`** explicit calibration corpus inclusion: "All observables at this slice — eigenvalues, Peter-Weyl decomposition, bottom-N cardinality, fiber spectrum, **spectral-action moments** — are substrate-IS at the single-τ-slice level". The BCS gap-equation kernel sum `K(0; L_max) = Σ_a^{L_max} m_a · tanh(λ_a/(2T_fold))/(2λ_a)` IS a spectral-action moment of `D_K^{−1}` weighted by the bounded function tanh(λ/(2T_fold)) — it lives in the Level-1 substrate-IS calibration corpus by the explicit `phononic-framing.md` enumeration.

The Level-1 framing is structurally canonical at the registry-text layer per the §VII.AQ Reading A precedent (S89 W-5 §VII.AQ workshop close with Reading A wins; canonical substrate-IS is FULL operator-algebra resolution at the spectral triple, NOT a methodology-layer projection). The L_max ≤ 10 BCS phase boundary is therefore a Level-1 single-τ-slice substrate-IS structural property by registry-text construction — confirmed by my Re:V1 NCG-axiomatic concession.

**Engagement with V5's forward question** (lines 271-273; "under what NCG-axiomatic argument is the L_max=10/11 BCS phase boundary a Level-2 moduli-deformation observable rather than a Level-1 single-τ-slice substrate-IS property — given that the gap-equation kernel sum evaluated at fixed τ_fold = 0.19 IS structurally a Level-1 single-τ-slice spectral-action moment per `phononic-framing.md` lines 77-81 explicit calibration corpus inclusion?"):

The honest NCG-axiomatic answer: **NO NCG-axiomatic argument promotes the L_max=10/11 BCS phase boundary to a Level-2 moduli-deformation observable**. The gap-equation kernel sum at fixed τ_fold IS a Level-1 single-τ-slice spectral-action moment by structural definition; the BCS phase boundary at L_max=10/11 IS a Level-1 single-τ-slice substrate-IS structural property at the canonical pin.

This is a concession at the structural layer that Reading B does NOT contest. Reading B's framing is NOT "the L_max=10/11 BCS phase boundary is a Level-2 moduli-deformation observable"; Reading B's framing (per Re:V1 conjecture and Re:V2 distinction) is more narrow: **the L_max=10 → 11 step at canonical (V_BCS, T_fold, τ_fold) IS a Level-1 single-τ-slice substrate-IS structural property at the scalar-Δ FULL-BdG operational machinery; the L_max=12 anchor mismatch is an operational-machinery distinction at the P_BdG projector implementation layer**. Reading B's distinction at L_max=12 does NOT promote the L_max ≤ 10 phase boundary to Level 2.

**Reading B's Level-2 prediction at L_max=10 under τ-deformation** (workshop lines 254-258):

V5 frames Reading B as predicting "at τ ∈ {0.18, 0.20}, the FULL gap-equation re-derivation produces a smooth Δ(L_max) sequence (no trivial-Δ regime at the canonical V_BCS coupling). The L_max=10/11 phase boundary is a Level-2 moduli-deformation artifact specific to the τ_fold = 0.19 slice". This is a STRAWMAN Reading B characterization that I do NOT endorse.

The honest Reading B prediction at CF-69's τ-extension is: **the BCS phase boundary at L_max=10/11 PERSISTS at small τ-deformations around τ_fold = 0.19**, because the spectral kernel sum K(0; L_max) at fixed canonical V_BCS is a substrate-IS structural property of the L_max-truncated spectral triple at EACH τ-slice independently. Small τ-deformations within the moduli-space neighborhood of τ_fold = 0.19 do NOT shift the critical-coupling threshold across the L_max=10/11 boundary at canonical V_BCS; the phase boundary IS intrinsic to the substrate's Level-1 spectral content at EACH τ-slice, and the moduli-deformation Level-2 layer carries a CONTINUOUS FAMILY of Level-1 phase boundaries (one per τ-slice) all at the same L_max=10/11 location.

**This is Reading A's Level-1 prediction**, NOT Reading B's Level-2 prediction. The honest position is that BOTH Reading A and Reading B predict the BCS phase boundary at L_max=10/11 persists under τ-deformation; the two readings do NOT differ at the Level-1 vs Level-2 layer for the L_max ≤ 10 phase boundary.

**Where Reading B's framing differs from Reading A at the Level-1 vs Level-2 layer is at the L_max=12 anchor mismatch layer**:

- **Reading A's prediction at L_max=12 anchor mismatch under τ-deformation**: the 1.428 anchor mismatch IS a substrate-IS structural separation between two distinct substrate-IS regimes (V2 lines 81-99); under τ-deformation, the structural separation PERSISTS at the L_max=12 anchor mismatch layer (the two operational routes remain non-equivalent at any τ in the moduli-space neighborhood).
- **Reading B's prediction at L_max=12 anchor mismatch under τ-deformation**: the 1.428 anchor mismatch IS an operational-machinery distinction at the P_BdG projector implementation layer; under τ-deformation, the operational-machinery distinction IS preserved (the s52 multi-branch tensor vs scalar-Δ self-consistency distinction is τ-INVARIANT at the operational-machinery layer), and the L_max=12 anchor value `−7.046336` IS expected to shift smoothly with τ (the §W5-2 anchor at each τ-slice IS the s52-tensor-applied K-window log-derivative evaluation at that τ-slice spectrum).

These two predictions differ at the Level-3 empirical anchor evolution under τ-deformation, NOT at the Level-1 phase-boundary persistence layer. CF-69's τ-extension scan is therefore informative about Reading A vs Reading B at the L_max=12 anchor evolution layer, NOT at the L_max ≤ 10 phase boundary persistence layer.

**DISAGREE** (V5's framing that CF-69's τ-extension is "DISCRIMINATORY under Reading B" overstates Reading B's commitments).

V5 lines 256-258 frames Reading B as predicting "the BCS phase boundary at L_max=10/11 LIFTS at small τ-deformations" — this is structurally what would be needed for the L_max=10/11 phase boundary to be a Level-2 moduli-deformation artifact. As stated above, this is NOT Reading B's commitment. Reading B accepts the L_max ≤ 10 phase boundary as a Level-1 single-τ-slice substrate-IS structural property at each τ-slice; the τ-deformation produces a continuous family of phase boundaries at the same L_max location.

CF-69's τ-extension (W8 WP CF-69 spec at lines 1646-1651: "extend §VII.AU substrate-IS observable from Level-1 single-τ-slice at τ_fold to Level-2 moduli-deformation across τ ∈ {0.18, 0.19, 0.20}"; gate PASS criterion: "α extraction across 3 τ-values; INFO if α scatter > 10%; FAIL if scatter > 25%") is structurally about CF-65's §VII.AU FWD-C1 first-extraction PATHWAY, NOT about CF-61's §VII.AV BCS phase boundary. The CF-69 gate IS NOT a Reading A vs Reading B discriminator for the L_max=10/11 BCS phase boundary — it is a Level-2 moduli-deformation extension for the §VII.AU n_s parameterized closure observable at substrate-distance-1 pole s=3, which is structurally DISTINCT from the §VII.AV K-window log-derivative observable at substrate-distance-2 pole s=4.

**CF-69 SCOPE CLARIFICATION**: CF-69 is a Level-2 moduli-deformation extension for the §VII.AU.OP-PROJ FWD-C1 observable (n_s Mellin-cone closure), NOT for the §VII.AV K-window log-derivative observable. V5's claim that "CF-69's pre-registered τ-extension (W8 WP lines 1646-1651; τ ∈ {0.18, 0.19, 0.20}) is the canonical Level-1 → Level-2 verification path" for the §VII.AV BCS phase boundary is structurally INCORRECT — CF-69 operates on the §VII.AU observable family, not the §VII.AV observable family. A separate Level-2 moduli-deformation extension gate would be required to test the §VII.AV BCS phase boundary persistence under τ-deformation.

**Proposal for a §VII.AV-specific Level-2 moduli-deformation extension gate** (carry-forward CF-75):

A new gate `S91-VII-AV-LMAX-10-PHASE-BOUNDARY-TAU-EXTENSION-PERSISTENCE-TEST` would extend the §VII.AV substrate-IS observable from Level-1 single-τ-slice at τ_fold = 0.19 to Level-2 moduli-deformation across τ ∈ {0.18, 0.19, 0.20}, dispatching the FULL BdG gap-equation re-derivation per CF-61 protocol AT EACH τ-slice. The gate PASS criterion: `Δ(L_max=10; τ ∈ {0.18, 0.19, 0.20}) = 0` (trivial-Δ regime persists at all three τ-values; Reading A's Level-1 framing confirmed AT THE MODULI-DEFORMATION LAYER); FAIL criterion: at least one τ ∈ {0.18, 0.20} returns finite Δ at L_max=10 (phase boundary lifts under τ-deformation; the L_max ≤ 10 phase boundary IS a Level-2 moduli-deformation artifact). This separate gate, NOT CF-69, would be the canonical Level-1 vs Level-2 discriminator for the §VII.AV BCS phase boundary.

Both Reading A and Reading B predict PASS (trivial-Δ persists at all τ in the moduli-space neighborhood); the CF-75 gate would CONFIRM the Level-1 single-τ-slice substrate-IS framing at the moduli-deformation layer rather than discriminate between the readings. This is structurally consistent — the L_max ≤ 10 phase boundary IS a Level-1 substrate-IS property at each τ-slice; both readings agree at this layer.

**MISSED** (NCG-axiomatic argument linking the BCS phase boundary to the substrate's Hochschild cohomology structure):

Per the Connes-Moscovici 1995 §III.4 dim-spectrum theorem at d_spec = 8, the substrate's spectral-zeta function `ζ_{D_K}(s) = Tr(D_K^{−s})` has poles at substrate-distance positions s ∈ {2, 4, 6, 8}. The substrate-distance-2 pole at s=4 (which §VII.AV's K-window log-derivative observable IS evaluated at) IS the gravitational kinematic-skeleton position (Phi correspondence weight-2 axis). The BCS gap-equation kernel sum K(0; L_max) at fixed τ_fold IS the L_max-truncated approximation of the substrate's `D_K^{−1}` evaluation weighted by `tanh(λ/(2T_fold))/2` — at Δ = 0 this reduces structurally to a regulated substrate-distance-1 pole evaluation (the `D_K^{−1}` evaluation lives at s=2 pole).

The structural argument from Hochschild cohomology: the L_max=10 → 11 step at canonical V_BCS reflects a substrate-IS structural property of the Hochschild cocycle ring on `(A_K, H_K, D_K(τ_fold))` — specifically, the truncation `(A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max})` at L_max ≤ 10 does NOT include the (p+q) ∈ {11, 12} Peter-Weyl sectors whose cocycle structure carries the Cooper-instability criterion's UV-tail content. This is a Hochschild-cohomology-side characterization of the substrate-IS phase boundary; it complements the spectral-action-moment characterization V5 leverages.

The Hochschild-cohomology-side argument confirms Reading A's Level-1 framing: the BCS phase boundary IS intrinsic to the substrate's Hochschild cocycle structure at each τ-slice; the truncation L_max ≤ 10 → L_max ≥ 11 transition IS a structural property of the substrate's cohomology ring under Peter-Weyl truncation, NOT of the operational gap-equation machinery.

**EMERGES** (cross-domain insight on the K-counter advancement for the deferred-pending sub-class):

Per V5 lines 261-269 cross-link to W1-14 deferred-pending K=1 SUGGESTION baseline at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` lines 124-127, the W-5 verdict's resolution interacts with the calibration corpus advancement:

- Under Reading A confirmed at the discriminator gate, the §VII.AV PROXY-REFINEMENT-PENDING tag's STRUCTURAL APPROPRIATENESS is CONFIRMED; the §VII.AV instance becomes a positive calibration corpus entry for the PROXY-REFINEMENT sub-class (S90 W1-14 dual-instance baseline + CF-70 S91+ landing → K=2 advancement; future-session distinct landings → K=3 MANDATORY).
- Under Reading B confirmed at the discriminator gate, the §VII.AV PROXY-REFINEMENT-PENDING tag's STRUCTURAL FORM is preserved but the canonical refinement ROUTE shifts from CF-70 to CF-71; the K-counter advancement may stall pending further structural clarification.
- Under INFO at the discriminator gate, refinement-pathway space carries BOTH CF-70 + CF-71 (wave-together); the deferred-pending PROXY-REFINEMENT tag retains its current registry-text framing pending the next-session resolution.

Under the hybrid verdict (d) framing, the K-counter advancement is STRUCTURALLY consistent with BOTH refinement routes: CF-70 advances the substrate-physics phase boundary refinement at the L_max ≤ 10 layer; CF-71 advances the operational-machinery alignment at the L_max=12 layer. Both PASS-paths jointly satisfy the §VII.AV deferred-pending PROXY-REFINEMENT sub-class advancement at the calibration corpus level. The hybrid verdict (d) is consistent with the K=1 SUGGESTION → K=2 advancement at the deferred-pending sub-class if BOTH CF-70 and CF-71 land at S91+ as positive calibration instances.

The Level-1 single-τ-slice MANDATORY tag at §VII.AV registry line 17918 is PRESERVED under the hybrid verdict — the BCS phase boundary IS Level-1 substrate-IS at each τ-slice, and the L_max=12 anchor mismatch operational-machinery distinction is a STRUCTURALLY ORTHOGONAL layer that does NOT promote the substrate-IS observable to Level 2. The cross-axis joint-win at W-5 advances K=4 → K=5 under the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern with the Level-1 single-τ-slice tag intact.

#### Re: V6 — Cross-Cutting Observations

**AGREE on Observation 1** (IS-not-IN substrate framing on CF-61 FAIL; the FULL-BdG operational machinery FAITHFULLY REPORTS substrate-IS structural content at L_max ≤ 10, NOT introduces an artificial discontinuity).

V6 Observation 1 (workshop lines 279-291) correctly identifies the IS-not-IN direction-of-explanation per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"` and per W8-3 §"Substrate framing" block (WP lines 514-522). The substrate IS the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at single-τ-slice τ_fold = 0.19; the L_max ≤ 10 BCS phase boundary IS substrate-IS information per Re:V1; the §W5-3 Casimir-bound SCHEMATIC proxy smoothed over this substrate-IS content at the algebraic-envelope layer. The container-thinking failure mode V6 explicitly rejects ("the FULL-BdG operational machinery introduces an artificial discontinuity at L_max=10/11 on what would otherwise be a smooth substrate observable") IS structurally inverted — the FULL-BdG machinery is the substrate-IS-faithful pipeline at the L_max ≤ 10 phase boundary, and the SCHEMATIC proxy is the operational artifact.

This concession matches my Re:V1 NCG-axiomatic confirmation: Reading A wins on the L_max ≤ 10 phase boundary; the FULL-BdG gap-equation FAIL at L_max ≤ 10 is substrate-IS-faithful structural content, NOT an operational-machinery artifact. V6's reference to the S89 W-5 §VII.AQ workshop's "Reading B's 'cache is the substrate' failure mode" at workshop lines 75-77 Q1.1 (per `s89-w5-vii-aq-level3-binding.md`) IS the correct structural precedent: substrate IS the FULL spectral triple at FULL operator-algebra resolution at the canonical pin; observables on truncations / projections / proxies are derived images, NOT canonical substrate-IS form. The §W5-3 SCHEMATIC proxy at L_max ≤ 10 IS a methodology-layer F-image of the substrate-IS phase boundary, smoothed by the `sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` continuous-interpolation ansatz; the FULL-BdG FAIL IS the substrate-IS-faithful evaluation at the canonical pin.

**Honest concession at this layer**: I do NOT defend a container-thinking framing of the CF-61 FAIL. The structural content of the FAIL IS substrate-IS information about the BCS criticality criterion at L_max ≤ 10 at canonical V_BCS; this is consistent with Reading A's V1 framing AND with the W8-3 §"Substrate framing" block (WP lines 514-522) which the CF-61 producing script itself emits. The §VII.AV registry text §"Substrate framing" lines 17928-17940 declares the direction-of-explanation: "Substrate (BdG sub-algebra M_2(ℂ) ⊂ A_K) IS the Corner-IV K-window log-derivative → Bridge map (HKR L_max → ∞ at d=4 substrate-distance-2 pole s=4) → Laboratory (Pillar V) IN 3He-B BdG-sector mutual-friction observation". This direction-of-explanation IS preserved under the hybrid verdict (d) framing — the L_max ≤ 10 phase boundary IS substrate-IS at the Level-1 single-τ-slice layer.

**DISAGREE on Observation 1's strong form** (the L_max=12 anchor mismatch IS NOT a container-thinking violation under Reading B).

V6 Observation 1 (workshop lines 287-291) extends the IS-not-IN argument from the L_max ≤ 10 phase boundary (where Reading A wins, my concession) to the L_max=12 anchor mismatch (where Reading B's operational-machinery distinction applies). The strong-form claim "the FULL-BdG operational machinery is NOT introducing the discontinuity — it is FAITHFULLY REPORTING substrate-IS structural content" generalizes correctly to the L_max ≤ 10 phase boundary but IS STRUCTURALLY OVER-STRONG when applied to the L_max=12 anchor mismatch.

At L_max=12, BOTH the FULL-BdG scalar-Δ route AND the s52 multi-branch ED route are substrate-IS-faithful at their respective machinery scopes (per W8-3 line 511-512 gen-physicist Q3 verbatim concession). The two routes evaluate the SAME substrate-IS observable (Corner-IV K-window log-derivative on `M_2(ℂ) ⊂ A_K` per CF-62 disambiguation) at DIFFERENT operational P_BdG projector implementations (scalar Δ vs multi-branch tensor). Neither route is "introducing an artificial discontinuity"; both are evaluating the substrate-IS observable under DIFFERENT machinery scopes.

This is NOT container-thinking. Container-thinking would be: "the operational machinery acts ON a pre-existing smooth substrate observable that exists independent of any machinery scope". Reading B's framing does NOT make this claim. Reading B's framing is: the substrate-IS observable's VALUE at L_max=12 depends on the P_BdG projector implementation choice; the §VII.AV registry text Element-1 (line 17918) does NOT yet pin the state-side specification; the §W5-2 anchor `−7.046336` IS one canonical-machinery-scope value (multi-branch s52 tensor); the FULL-BdG anchor `−5.6188` IS another canonical-machinery-scope value (scalar Δ self-consistency). Both are substrate-IS evaluations at distinct operational machinery scopes.

The structural precedent is again S89 W-5 §VII.AQ Reading A wins (substrate IS the FULL spectral triple at FULL operator-algebra resolution; cache-projection is methodology-layer F-image). BUT the §VII.AQ precedent established that ONE machinery scope is canonical (the full-leaf-foliation / APS-1975-secondary-class scheme at Element 3 binding type (i)) — a SINGLE substrate-self-consistent pin. For §VII.AV, the canonical machinery scope IS the multi-branch s52 tensor application at L_max=12 per §W5-2 Element 3 binding type (i). The FULL-BdG scalar-Δ re-derivation is structurally an ALTERNATIVE machinery scope; the 1.428 anchor mismatch measures the structural distance between the canonical scope and the alternative scope, NOT a substrate-IS phase boundary at L_max=12.

This distinction IS NOT container-thinking; it is the natural extension of the §VII.AQ Reading A precedent to the §VII.AV substrate-IS observable. The honest IS-not-IN framing at L_max=12 is: the substrate IS the BdG sub-algebra `M_2(ℂ)`; the canonical-machinery-scope evaluation IS the multi-branch s52 tensor application; the FULL-BdG scalar-Δ is an alternative-machinery-scope evaluation of the same substrate-IS observable; CF-71's K_canonical re-pinning investigates whether the alternative scope can be aligned with the canonical scope via K-window observable definition refinement. This is structurally consistent with the IS-not-IN mandate — the alternative scope is NOT "in" a different container, it IS a different machinery-scope evaluation of the same substrate-IS observable.

**AGREE on Observation 2** (W-5 is a candidate K=5 advancement under the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern; convergent verdict required).

V6 Observation 2 (workshop lines 293-299) correctly identifies W-5 as the 5th sequential Slot 2 dispatch at S90 advancing the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern from K=4 → K=5 MANDATORY promotion candidate per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold. The structural property of the cross-axis pattern IS layer-functor F decomposition cleanness per `epistemic-discipline.md §"Layer-Decomposition"`: substrate ↔ methodology ↔ audit at the JOINT-WIN axis means the volovik-superfluid-universe substrate-physics framing AND the connes-NCG-axiomatic methodology framing converge on a single structural verdict at the audit layer.

Under the hybrid verdict (d) framing, the cross-axis joint-win IS achieved at the structural level:

- **Substrate-physics axis (volovik / Reading A)**: L_max ≤ 10 phase boundary IS substrate-IS Cooper-instability criterion at canonical V_BCS; CF-70 (FULL Connes-Chamseddine 1996 physical multipliers) IS the canonical refinement route at the substrate-physics phase boundary layer.
- **NCG-axiomatic axis (connes / Reading B)**: L_max=12 anchor mismatch IS operational-machinery distinction at the P_BdG projector implementation layer; CF-71 (K_canonical pin uniqueness investigation) IS the canonical refinement route at the operational-machinery alignment layer.
- **Joint convergence**: BOTH refinement routes are structurally appropriate at THEIR respective layers; the V4 discriminator gate `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` fires FIRST to adjudicate the L_max=12 anchor layer; CF-70 + CF-71 dispatch in parallel (Option γ) under the hybrid verdict (d).

This cross-axis convergence at the hybrid verdict (d) IS the joint-win required for K=4 → K=5 advancement. The structural verdict (d) — "substrate phase boundary AT operational-machinery joint layer" — explicitly recognizes that BOTH readings are partially-correct at structurally distinct layers; this IS the cross-axis layer-functor F cleanness condition the K-counter advancement requires.

**Under verdict (c) alternative** (refinement pathway space carries both; discriminator-gate fires first): the verdict (c) framing is consistent with verdict (d) but more conservative on the layer-functor F decomposition cleanness — verdict (c) defers the structural verdict to the empirical discriminator gate outcome, while verdict (d) explicitly recognizes the two-layer structure as the structural verdict itself. Both verdict (c) and (d) advance K=4 → K=5; verdict (d) is the stronger structural claim.

**AGREE on Observation 3** (deferred-pending PROXY-REFINEMENT calibration corpus interaction at W1-14 dual-instance K=1 SUGGESTION baseline; the hybrid verdict (d) advances the K-counter under either CF-70 OR CF-71 PASS at S91+).

V6 Observation 3 (workshop lines 301-313) cross-links to `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` lines 124-127 SUGGESTION at K=1 baseline (dual calibration §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION sharing S90 W1-14 landing event). Under the hybrid verdict (d) framing, the calibration corpus interaction IS:

- **CF-70 PASS at S91+** → §VII.AV PROXY-REFINEMENT-PENDING tag's STRUCTURAL APPROPRIATENESS is CONFIRMED at the FULL CC physical-multipliers refinement layer; positive calibration corpus instance for the PROXY-REFINEMENT sub-class advancing K=1 → K=2.
- **CF-71 PASS at S91+** → §VII.AV PROXY-REFINEMENT-PENDING tag's STRUCTURAL FORM is PRESERVED with the canonical refinement ROUTE shifting from FULL-physical-Pauli-Villars (route ii) to the K_canonical pin uniqueness operational-alignment (which is structurally a SEPARATE refinement-pathway type not currently enumerated in the registry-text refinement-pathway table at lines 17944-17948 — Reading B proposes a 4th route in the table); positive calibration corpus instance for the PROXY-REFINEMENT sub-class at the operational-machinery alignment refinement layer.
- **BOTH PASS at S91+** → K=1 SUGGESTION → K=2 advancement at the deferred-pending sub-class, with two POSITIVE instances at structurally orthogonal refinement layers (CF-70 substrate-physics + CF-71 operational-machinery alignment).

The hybrid verdict (d) is consistent with EITHER PASS path or BOTH simultaneously; the K-counter advancement at the deferred-pending sub-class is structurally robust under the hybrid framing.

**Engagement with V6's forward question** (lines 315-317; "under what NCG-axiomatic argument does CF-71's K_canonical re-tuning PRESERVE the layer-functor F decomposition cleanness (substrate ↔ methodology ↔ audit) in the absence of a substrate-IS-faithful resolution of the L_max=10/11 phase boundary?"):

The honest NCG-axiomatic answer: **CF-71 does NOT preserve the layer-functor F decomposition cleanness at the L_max=10/11 phase boundary layer — and it does NOT claim to**. CF-71 operates at the L_max=12 anchor layer only; the L_max=10/11 phase boundary refinement IS CF-70's domain per the hybrid verdict (d). The layer-functor F decomposition cleanness at the L_max=10/11 phase boundary layer IS preserved under CF-70, NOT under CF-71.

V6's forward question framing presupposes that CF-71 alone must preserve the full F decomposition cleanness (substrate ↔ methodology ↔ audit at ALL layers of the CF-61 evidence chain). This presupposition is structurally INCORRECT under the hybrid verdict (d): the two refinement routes CF-70 + CF-71 jointly preserve F decomposition cleanness at their respective orthogonal layers. CF-70 preserves F cleanness at the L_max ≤ 10 phase boundary layer (via FULL CC physical-multipliers refinement reconstructing the Level-2 envelope); CF-71 preserves F cleanness at the L_max=12 anchor layer (via K_canonical pin uniqueness resolving the P_BdG projector implementation distinction).

**Layer-functor F decomposition under the hybrid verdict (d)**:

```
Substrate axis (Level 1 substrate-IS)
  ├── L_max ≤ 10 phase boundary IS substrate-IS at canonical V_BCS (Reading A)
  └── L_max=12 P_BdG implementation choice IS state-side specification (Reading B)

Methodology axis (Level 2 algebraic envelope + Level 3 empirical anchor F-image)
  ├── CF-70 FULL CC physical multipliers refinement at L_max ≤ 10 (substrate-physics)
  └── CF-71 K_canonical pin uniqueness at L_max=12 (operational-machinery)

Audit axis (registry-text + audit-line content)
  ├── §VII.AV deferred-pending PROXY-REFINEMENT tag (registry text line 17897)
  ├── §VII.AV refinement-pathway 3-route table (lines 17944-17948) extended with
  │   4th route "K_canonical pin uniqueness operational-alignment" (Reading B addition)
  └── V4 discriminator gate substrate-physics adjudication (S91+ verdict at audit layer)
```

The Phi correspondence weight-2 image (Sigma_2 / wave-classification) maps the substrate-axis L_max ≤ 10 phase boundary to the methodology-axis CF-70 refinement; the Phi correspondence weight-2 image ALSO maps the substrate-axis L_max=12 P_BdG state-side specification to the methodology-axis CF-71 refinement. Both methodology-axis refinements are F-image-preserved under the substrate ↔ methodology layer pair. The audit-axis maps the methodology-axis refinements to the registry-text deferred-pending tag's appropriate refinement-pathway annotation (preserved under either CF-70 OR CF-71 PASS).

**MISSED** (V6 does not explicitly note that the W-5 cross-axis joint-win under hybrid verdict (d) advances multiple K-counters simultaneously):

Under the hybrid verdict (d) framing, the W-5 cross-axis joint-win advances multiple K-counters at S90 close:

1. **CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter**: K=4 → K=5 advancement (W-5 is the 5th sequential Slot 2 dispatch at S90 per workshop header line 43); MANDATORY promotion candidate at K=5 per `feedback_rules-compensate-missing-structure.md`.
2. **Deferred-pending intermediate verdict-class K-counter**: K=1 SUGGESTION (dual calibration §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION) preserved at W-5 landing; advances K=1 → K=2 at S91+ landing of CF-70 OR CF-71.
3. **Level-2-binding K-counter**: K=1 SUGGESTION (W-5 §VII.AF.1 baseline) preserved at W-5 landing; advances K=1 → K=2 at S91+ landing of CF-70 PASS (the FULL CC physical-multipliers route IS the substrate-natural Level-2-binding HKR-image refinement per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"`).
4. **Element 3 fiducial-anchor binding-axis K-counter** (S88 W7b-82 K=1 SUGGESTION per `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` Binding-axis row): the §VII.AV instance under CF-71 PASS would advance the binding-axis K-counter K=1 → K=2 with the §VII.AV instance pair calibrating the canonical-import-binding vs substrate-natural-binding axis at the K-window log-derivative observable layer.

The W-5 cross-axis joint-win under hybrid verdict (d) is structurally a multi-K-counter advancement event; the cross-axis layer-functor F cleanness condition IS satisfied across all four K-counter advancement axes. This makes W-5 a structurally rich K-counter advancement landing — perhaps the most structurally consequential cross-axis joint-win in the S86-S90 sequence.

**EMERGES** (cross-domain insight on the hybrid verdict's structural advantage):

The hybrid verdict (d) — "substrate phase boundary AT operational-machinery joint layer" — has a structural advantage over both verdict (a) Reading A canonical and verdict (b) Reading B canonical: it explicitly recognizes the two-layer structure of the CF-61 evidence chain (L_max ≤ 10 phase boundary at substrate-physics layer; L_max=12 anchor mismatch at operational-machinery layer) and assigns the canonical refinement routes accordingly (CF-70 at substrate-physics layer; CF-71 at operational-machinery layer). Neither verdict (a) nor verdict (b) captures this two-layer structure cleanly — verdict (a) over-claims by extending Reading A from L_max ≤ 10 to L_max=12; verdict (b) over-claims by extending Reading B from L_max=12 to L_max ≤ 10.

Verdict (c) "refinement pathway space carries both; pre-registered S91+ discriminator-gate fires first to determine dominance" is structurally consistent with verdict (d) but more conservative — verdict (c) defers the structural verdict to the empirical discriminator gate outcome; verdict (d) explicitly recognizes the two-layer structure as the structural verdict itself.

Reading B's preferred terminal verdict: **verdict (d) hybrid**, with verdict (c) as a structurally acceptable fallback if Reading A authoring (volovik) does not converge on the two-layer recognition. The V4 discriminator gate's S91+ outcome routes the CF-70 + CF-71 dispatch ordering per Re:V3 Option γ wave-together. The K=4 → K=5 advancement IS structurally achieved at W-5 close under the hybrid verdict (d) framing.

### Part 2: Original Analysis

#### C1: scalar-Δ gap-equation vs multi-branch s52 ED — operational-parameterization framing of CF-61 FAIL

**Reading B's NCG-axiomatic steelman**: the CF-61 FAIL is a STRUCTURAL EVIDENCE CHAIN with two distinguishable layers. At L_max ≤ 10 the substrate-IS phase boundary IS structurally real (Reading A wins per Re:V1). At L_max=12 the 1.428 anchor mismatch IS structurally an operational-machinery distinction at the P_BdG projector implementation layer (Reading B's domain). The honest steelman position is that BOTH readings apply at structurally distinct layers; the discriminator gate V4 IS the canonical adjudicator at L_max=12; the structural verdict is hybrid (d).

**Layer 1 (L_max ≤ 10): substrate spectral kernel weight insufficient at canonical V_BCS**

Per Re:V1 NCG-axiomatic concession: the BCS gap-equation kernel sum `K(0; L_max) = Σ_a^{L_max} m_a · tanh(λ_a/(2T_fold))/(2λ_a)` at canonical V_BCS = 2.447e-7 M_KK^{−1} is a Level-1 single-τ-slice spectral-action moment per `phononic-framing.md §"Level 1 — Single-τ-slice substrate-IS"` calibration corpus (lines 77-81). At L_max ≤ 10, the truncated spectrum lacks the (p+q) ∈ {11, 12} Peter-Weyl sectors contributing 4.3% of UV weight (W8-3 Step 2 lines 333-341); the critical-coupling threshold K(0; L_max) ≥ 1/V_BCS is NOT crossed at L_max ≤ 10 at canonical V_BCS. This IS substrate-IS structural content.

At this layer, Reading B's framing of CF-61 FAIL as "scalar-Δ operational machinery insufficient to capture multi-branch structure" is structurally OVER-STRONG. The honest position is that the scalar-Δ gap-equation FAIL at L_max ≤ 10 IS substrate-IS-faithful information about the BCS Cooper-instability criterion at the canonical pin; the multi-branch s52 tensor at L_max ≤ 10 does NOT solve the gap-equation self-consistency at canonical V_BCS either — it imports an externally-determined (B1, B2, B3) configuration from the s52 ED problem (at the 256-state Hilbert space, NOT the L_max-truncated gap-equation problem).

**Layer 2 (L_max=12): scalar-Δ vs multi-branch P_BdG projector implementation distinction**

Per Re:V2 NCG-axiomatic argument: at L_max=12 BOTH operational routes produce a finite gap (Δ_FULL(12)=0.4643 from scalar-Δ self-consistency; Δ_per_mode_s52=(0, 0.7704, 0.176) from s52 ED). The 1.428 anchor mismatch arises from the P_BdG projector implementation distinction at the K-window log-derivative evaluation:

```
L_emp(L_max=12)_FULL_BdG_scalar_Delta   = −5.6188   [scalar Δ self-consistency, rescale 0.6026 uniform across 8 modes]
L_emp(L_max=12)_s52_multi_branch         = −7.0463   [multi-branch B1=0, B2=0.7704, B3=0.176 from s52 ED]
|diff|                                    =  1.428
```

**Substitution chain** (Reading B's operational-parameterization framing):

```
Step 1 (Definitions):
  P_BdG(Δ_a) := diag(|v_a|², |u_a|²)  where  |v_a|² = (1 − ε_a/E_a)/2,
                                            E_a    = sqrt(ε_a² + Δ_a²)
                                            ε_a    = λ_a (BdG sub-algebra band energy)
                                            Δ_a    = Bogoliubov gap per mode a

  Route A (scalar Δ):       Δ_a = Δ_canonical                  ∀ a
  Route B (multi-branch):   Δ_a = (Δ_B1, Δ_B2, Δ_B3) per s52 ED branch a

Step 2 (Substitution into Bogoliubov-state covariance):
  Tr_{M_2(ℂ)}(P_BdG(Δ_a) · D_K^{−2s})|_{s→4}  evaluates to a
  state-pair functional on M_2(ℂ) parameterized by the Δ_a tensor structure.

  Per W8-3 line 511-512 (gen-physicist adversarial Q3 verbatim):
  "BOTH compute the same Cell IV substrate-IS observable (variance of
   Bogoliubov occupation at K_horizon) on the substrate algebra A_K, but
   they evaluate it on different operational machineries — the s52 route
   preserves the multi-branch ED solution; the FULL gap-equation route
   imposes a scalar Δ self-consistency."

Step 3 (Simplification per §VII.U.2 Corner II Var_a parse-tree at registry line 12961):
  Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2
                  where  n_a = Δ_BCS² / (2(λ_a² + Δ_BCS²))    [S52 Bogoliubov closed form]

  This parse-tree expansion makes the |v_a|² DEPENDENCE on the Δ_a tensor structure
  EXPLICIT at the substrate-IS closed-form layer. Different Δ_a tensors produce
  different (|v_a|², |u_a|²) per-mode weight tensors, hence different
  Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})|_{s→4} values, hence different K-window
  log-derivative L_emp values at the SAME spectral kernel.

Step 4 (Canonical form):
  The substrate-IS observable IS the SAME at the parse-tree-expansion layer
  (Var_a closed form Cell-IV). The OPERATIONAL EVALUATION at L_max=12 differs
  by Δ_a tensor specification — this is a state-side specification choice that
  the §VII.AV registry text Element-1 (line 17918) does NOT yet pin.

Step 5 (Direction):
  At L_max=12, BOTH routes are substrate-IS-faithful at their respective machinery
  scopes. The 1.428 anchor mismatch is the structural distance between two
  canonical-machinery-scope evaluations of the same substrate-IS observable;
  it is NOT a substrate-IS phase boundary at L_max=12.
```

**Empirical predictions differ between Reading A and Reading B**:

Per spawn prompt C1 specification, the two readings make DIFFERENT empirical predictions for the s52 multi-branch ED at L_max ≤ 10:

| Reading | Multi-branch s52 ED at L_max ≤ 10 prediction |
|:--------|:---------------------------------------------|
| **A (substrate spectral kernel insufficient)** | multi-branch s52 ED at L_max ≤ 10 also returns Δ=0 (substrate spectral kernel weight is insufficient regardless of operational machinery) |
| **B (operational machinery insufficient to capture multi-branch structure)** | multi-branch s52 ED at L_max ≤ 10 returns finite (B1, B2, B3) configuration (operational machinery captures the substrate's multi-branch structure where scalar-Δ does not) |

**Honest Reading B position at this prediction layer**:

The Reading B prediction "multi-branch s52 ED at L_max ≤ 10 returns finite (B1, B2, B3) configuration" is structurally CONJECTURAL — it requires re-running the s52 ED on the L_max ≤ 10 truncated spectrum at canonical V_BCS_per_branch couplings (NOT the canonical scalar V_BCS), which has NOT been done at S90 W8. The honest NCG-axiomatic assessment: under the Hochschild-Künneth Morita-invariance `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` (W-4 verdict), the BdG sub-algebra's Hochschild cohomology IS preserved under truncation at L_max — BUT the s52 ED problem's V_BCS_per_branch coupling structure is not derived from the Morita-invariance argument; it is an external input from S52 BdG canonical amplitudes per `permanent-results-registry.md §VII.U.2` Corner II parse-tree line 12961.

If the s52 ED at L_max ≤ 10 IS re-solved at multi-branch V_BCS_per_branch couplings, two outcomes are structurally possible:

1. **Outcome (i) — Reading A wins**: the multi-branch s52 ED at L_max ≤ 10 also returns trivial configuration (B1=B2=B3=0) at canonical scalar V_BCS. The substrate spectral kernel weight insufficiency at L_max ≤ 10 IS substrate-IS structural; both operational machineries fail.
2. **Outcome (ii) — Reading B wins**: the multi-branch s52 ED at L_max ≤ 10 returns finite (B1, B2, B3) configuration at multi-branch V_BCS_per_branch couplings (re-tuned per-branch). The scalar-Δ gap-equation FAIL at L_max ≤ 10 IS structurally an operational-machinery limitation; the substrate admits a non-trivial Bogoliubov condensate at L_max ≤ 10 under multi-branch operational machinery.

This empirical question is what the V4 discriminator gate `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` adjudicates AT L_max=12 — but NOT at L_max ≤ 10. The L_max ≤ 10 question requires a separate empirical test that V4 does NOT pre-register.

**Proposal for a L_max ≤ 10 multi-branch s52 ED retry gate** (carry-forward CF-76):

A new gate `S91-VII-AV-LMAX-LE-10-MULTI-BRANCH-S52-ED-RETRY` would re-run the s52 ED on the L_max ∈ {6..10} truncated spectra at multi-branch V_BCS_per_branch couplings. The gate PASS criterion: at least one L_max ∈ {6..10} admits a finite (B1, B2, B3) configuration at structurally-canonical multi-branch V_BCS_per_branch (Reading B confirmed at L_max ≤ 10 layer). FAIL criterion: all L_max ≤ 10 truncations return trivial (B1=B2=B3=0) configuration regardless of multi-branch coupling re-tuning (Reading A confirmed at L_max ≤ 10 layer). This gate is structurally orthogonal to V4 — V4 tests the L_max=12 anchor alignment; CF-76 tests the L_max ≤ 10 phase boundary persistence under multi-branch operational machinery.

**Honest Reading B verdict at the empirical-prediction layer**:

Without CF-76 (which is not currently pre-registered), Reading B's L_max ≤ 10 prediction "multi-branch s52 ED returns finite (B1, B2, B3)" is structurally CONJECTURAL. I CONCEDE this is an open empirical question; the V4 discriminator gate alone does NOT adjudicate it.

The honest NCG-axiomatic position: the V4 discriminator gate is the canonical adjudicator at L_max=12 (Re:V4). CF-76 (proposed above) would be the canonical adjudicator at L_max ≤ 10. Both gates are needed to fully resolve the Reading A vs Reading B question across all layers of the CF-61 evidence chain.

**Verdict (d) hybrid is the structurally honest verdict**:

Under the hybrid verdict (d) framing:

- **L_max ≤ 10 phase boundary** (Layer 1): Reading A wins per Re:V1 NCG-axiomatic concession on the spectral kernel weight insufficiency at canonical scalar V_BCS. Whether Reading B's multi-branch operational-machinery rescue is structurally available at L_max ≤ 10 IS an open empirical question pending CF-76; ABSENT CF-76 evidence, Reading A's canonical framing of the L_max ≤ 10 phase boundary stands.
- **L_max=12 anchor mismatch** (Layer 2): Reading B's operational-machinery framing per Re:V2 — the 1.428 mismatch IS structurally a P_BdG projector implementation distinction at the K-window observable evaluation layer; CF-71 (K_canonical pin uniqueness) IS the canonical refinement route at this layer; V4 discriminator gate fires first to adjudicate.

This two-layer hybrid verdict acknowledges:
1. **Reading A is partially-correct at the L_max ≤ 10 phase boundary layer** (substrate-IS Cooper-instability criterion fails on the truncated spectral kernel at canonical V_BCS).
2. **Reading B is partially-correct at the L_max=12 anchor mismatch layer** (operational-machinery P_BdG projector implementation distinction).
3. **Neither reading is structurally exhaustive** — Reading A over-claims by extending the substrate-IS phase boundary framing from L_max ≤ 10 to L_max=12; Reading B over-claims by extending the operational-machinery framing from L_max=12 to L_max ≤ 10 (without CF-76 evidence).

The hybrid verdict (d) IS the structurally honest verdict per the W-5 cross-axis joint-win pattern. CF-70 + CF-71 dispatch in parallel (Option γ wave-together per Re:V3) addresses both layers at S91+; the V4 discriminator gate fires first to adjudicate the L_max=12 layer.

**Honest concession to volovik on the structural verdict**:

If the workshop verdict converges on (a) Reading A canonical (Casimir-bound STRUCTURALLY CLOSED; CF-70 prioritized; CF-71 deferred), I do NOT structurally dissent at the L_max ≤ 10 phase boundary layer — Reading A wins at this layer per my Re:V1 concession. My dissent at the L_max=12 layer is preserved as the residual operational-machinery question that CF-71 + V4 discriminator gate adjudicate at S91+.

The cross-axis joint-win at W-5 IS structurally compatible with either verdict (a) Reading A canonical OR verdict (d) hybrid; the structural difference is the explicit recognition of the two-layer structure in verdict (d). My preferred terminal verdict is (d); verdict (a) is acceptable if volovik converges on the L_max=12 layer being a separate operational-machinery question handled by CF-71 / V4 discriminator independently. Both verdicts advance K=4 → K=5 at the cross-axis joint-win K-counter.

#### C2: §VII.AV refinement pathway under Reading B — CF-71 prioritized + Casimir-bound admissible IF alignment succeeds

**Reading B's NCG-axiomatic steelman for the §VII.AV refinement pathway**: CF-71 K_canonical pin uniqueness IS the canonical PROXY-REFINEMENT route under Reading B's operational-machinery framing of the L_max=12 anchor mismatch. The Casimir-bound SCHEMATIC proxy class MAY remain admissible IF CF-71 alignment succeeds — the proxy's smooth-interpolation `sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` ansatz remains operationally valid IF the underlying multi-branch operational machinery is correctly aligned at the canonical pin AT L_max ≥ 11. CF-71 operates at the K-window observable definition layer (P_BdG projector implementation choice), NOT at the BCS gap-equation refinement layer (which is CF-70's domain).

**Reading B's structural reading of CF-71 vs CF-70 at the §VII.AV refinement-pathway table**:

Per the §VII.AV registry text refinement-pathway 3-route table at lines 17944-17948:

```
(i)   L_max scan + Friedrich-Bär saturation theorem   | CF-W5-3 (= CF-61)  | analytic-certification
(ii)  FULL BdG re-derivation (PV at Λ_UV = M_KK)       | CF-W5-3 (= CF-61)  | full-physical-Pauli-Villars
(iii) FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers | CF-W5-3 (= CF-61)  | full-CC1996-multipliers
```

The W8 W-5 close should extend this table with a **4th route** (Reading B's addition):

```
(iv)  K_canonical pin uniqueness operational-alignment | CF-71              | operational-machinery-alignment
```

Route (iv) operates at a STRUCTURALLY DISTINCT layer from routes (i)-(iii): routes (i)-(iii) operate at the BCS gap-equation / spectral kernel / regulator refinement layer (substrate-physics axis); route (iv) operates at the K-window observable definition / P_BdG projector implementation layer (operational-machinery axis). The registry-text refinement-pathway table extension is a SUGGESTION FROM READING B that mack-cosmic-bridge sole-writer could land at S91+ if the hybrid verdict (d) converges (or alternatively, CF-71 could be excluded from the table if Reading A wins outright at the discriminator gate).

**CF-71 PASS interpretation under Reading B's steelman**:

Per W8 WP CF-71 spec lines 1660-1665 verbatim: "PASS iff K_canonical derivation is uniquely determined by the substrate's BdG energy gap at τ_fold AND `|L_emp(L_max=12)_corrected − (−7.046336474406761)| < 1e-9` under the corrected K_canonical pin. **PASS may complement OR replace CF-70 as the proxy-refinement pathway.**"

The "may complement OR replace" clause is structurally consequential — it explicitly preserves the possibility that CF-71 alone resolves the §VII.AV refinement-pending status without requiring CF-70 dispatch. Under Reading B's steelman, CF-71 IS the canonical PROXY-REFINEMENT route at the operational-machinery axis; if CF-71 alignment succeeds, the §VII.AV deferred-pending PROXY-REFINEMENT-PENDING tag can be lifted to STAGE-1-CANDIDATE WITHOUT requiring CF-70 (Reading B-favored verdict (b) outcome).

**Casimir-bound SCHEMATIC proxy class admissibility under CF-71 PASS**:

If CF-71 succeeds at aligning the FULL-BdG L_max=12 anchor with the §W5-2 canonical −7.046336 (< 1e-9 tolerance), the Casimir-bound SCHEMATIC proxy class becomes structurally admissible AT L_max ≥ 11 (where the gap-equation self-consistency produces a finite Δ). The proxy's smooth `sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` ansatz then operationally represents the Δ(L_max) sequence at L_max ∈ {11, 12} under the aligned P_BdG implementation, and the SCHEMATIC proxy's predictive value is preserved at this restricted parameter regime.

HOWEVER: the Casimir-bound SCHEMATIC proxy class REMAINS STRUCTURALLY FALSIFIED AT L_max ≤ 10 even under CF-71 PASS — because the substrate-IS phase boundary at L_max=10/11 (Reading A wins at this layer per Re:V1) is preserved regardless of CF-71's K_canonical re-pinning. CF-71 operates only at L_max=12; it does NOT rescue the SCHEMATIC proxy at L_max ≤ 10.

This means: even under CF-71 PASS, the Casimir-bound SCHEMATIC proxy class is admissible ONLY in the restricted post-transition parameter regime L_max ≥ 11, NOT across the full L_max ∈ {6..12} range that the §W5-3 SCHEMATIC proxy original framing assumed. The "Casimir-bound proxy class may remain admissible IF alignment succeeds" claim in the workshop schedule (line 22) is structurally CORRECT only at L_max ≥ 11; at L_max ≤ 10 the SCHEMATIC proxy is structurally falsified regardless.

**Honest concession to volovik V3's "Casimir-bound proxy STRUCTURALLY CLOSED" claim**:

Volovik's V3 claim "Casimir-bound proxy class STRUCTURALLY CLOSED" (workshop lines 141-151) is structurally CORRECT at the FULL L_max ∈ {6..12} parameter range that the §W5-3 SCHEMATIC proxy original framing assumed — the substrate-IS phase boundary at L_max=10/11 falsifies the proxy's smoothness across this range. My Re:V3 partial DISAGREE (clarifying that the closure-statement is true at canonical V_BCS but MAY be over-strong under alternative multi-branch V_BCS parametrizations) STANDS as a narrow operational-machinery refinement, but it does NOT structurally re-open the SCHEMATIC proxy at the canonical V_BCS pin.

The structurally honest restated position: **the §W5-3 SCHEMATIC Casimir-bound proxy class IS structurally closed at canonical V_BCS at L_max ∈ {6..10} (Reading A wins at this layer); it MAY be operationally admissible AT L_max ∈ {11, 12} under CF-71 PASS aligning the P_BdG implementation; under the hybrid verdict (d) framing, CF-71 IS the canonical PROXY-REFINEMENT route at the operational-machinery axis AT L_max ≥ 11, while CF-70 IS the canonical PROXY-REFINEMENT route at the substrate-physics axis across L_max ∈ {6..12}.** The two refinement routes operate at structurally orthogonal layers; both can land as positive calibration corpus instances at the deferred-pending PROXY-REFINEMENT sub-class K=1 → K=2 advancement at S91+.

**Engagement with volovik V3 + Re:V3 on dispatch ordering (Option α / β / γ)**:

Per Re:V3 enumeration of dispatch ordering options:

- **Option α (CF-71 → CF-70 sequential; Reading B prioritized)**: structurally licensed under Reading B-canonical verdict (b).
- **Option β (CF-70 → CF-71 sequential; Reading A prioritized)**: structurally licensed under Reading A-canonical verdict (a).
- **Option γ (CF-70 + CF-71 wave-together; verdict (c) or (d))**: structurally licensed under the hybrid framing.

Under Reading B's steelman (my position), **Option α is structurally licensed**: CF-71 fires first at S91+; the V4 discriminator gate adjudicates the L_max=12 anchor layer; if CF-71 PASSes (Reading B confirmed at L_max=12), CF-70 dispatches subsequently under the aligned P_BdG implementation to address the L_max ≤ 10 phase boundary refinement via FULL CC physical multipliers (Reading A's domain). The two refinement routes complement at structurally orthogonal layers; Option α prioritizes CF-71 at the L_max=12 layer first per Reading B's steelman.

However, Option γ (wave-together; verdict (c) or (d)) is structurally MORE ROBUST because it dispatches both refinement routes in parallel and uses the V4 discriminator gate outcome to adjudicate the dispatch-ordering POSTERIOR. Under Option γ:

```
S91+ dispatch sequence:
  Step 1 — V4 discriminator gate (S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST) fires FIRST
  Step 2 — CF-70 + CF-71 dispatch in parallel (independent of V4 outcome)
  Step 3 — V4 outcome adjudicates the L_max=12 anchor layer verdict
  Step 4 — CF-70 outcome adjudicates the L_max ≤ 10 phase boundary refinement
  Step 5 — CF-71 outcome adjudicates the L_max=12 operational-machinery alignment
  Step 6 — joint verdict assembled from all four S91+ gate outcomes (V4 + CF-70 + CF-71 + optional CF-76)
```

The honest Reading B preference: Option γ (wave-together) under verdict (d) hybrid. The V4 discriminator gate fires FIRST per Re:V4 to adjudicate the L_max=12 anchor layer; CF-70 + CF-71 dispatch in parallel addresses their respective orthogonal layers; the joint verdict at S91+ close assembles a complete picture of the CF-61 evidence chain refinement.

**Engagement with volovik V3's "CF-71 STRUCTURALLY DEFERRED under Reading A" claim**:

Volovik V3 lines 153-157 explicitly demotes CF-71 under Reading A: "CF-71 (K_canonical pin uniqueness) is STRUCTURALLY DEFERRED under Reading A: it operates at the operational-machinery layer, not the substrate-IS layer". The honest Reading B counter: this demotion is structurally over-strong. CF-71 operates at the K-window observable DEFINITION layer (P_BdG projector implementation choice); this layer IS a substrate-IS-relevant layer because the K-window log-derivative IS the §VII.AV substrate-IS observable per CF-62 disambiguation. CF-71 IS NOT "operational-machinery layer only"; it operates at the substrate-IS observable's state-side specification layer (the Δ_a tensor choice that enters P_BdG = diag(|v_a|², |u_a|²) per the parse-tree expansion at registry line 12961).

The structural distinction is subtle but consequential:

- **CF-71 operates at the substrate-IS observable's state-side specification layer** (which Δ_a tensor enters the K-window log-derivative evaluation).
- **CF-70 operates at the BCS gap-equation regulator layer** (which UV-regulator scheme — unsubtracted vs FULL CC 2-point PV — produces the Δ_a tensor self-consistency).

Both layers are substrate-IS-relevant (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` MANDATORY-K=2 Level 1 single-τ-slice substrate-IS framing — all observables at the spectral triple at fixed τ are substrate-IS). The dichotomy "substrate-IS layer vs operational-machinery layer" V3 introduces is a structural FALSE DICHOTOMY at the §VII.AV refinement-pathway analysis — both CF-70 and CF-71 are substrate-IS-relevant refinement routes at different (orthogonal) sub-layers of the §VII.AV evidence chain.

The honest restated position: **CF-71 IS structurally licensed under Reading B as a PROXY-REFINEMENT route at the K-window observable definition / Δ_a tensor specification layer** (a substrate-IS observable's state-side specification refinement, NOT a non-substrate-IS operational-machinery tuning); the V4 discriminator gate adjudicates whether CF-71 PASSes empirically at S91+. If CF-71 PASSes, it advances the §VII.AV refinement-pathway as the operational-machinery alignment route (option β under Reading B-canonical verdict (b)) OR the operational-machinery component of the hybrid verdict (d).

**Forward proposal: §VII.AV refinement-pathway table extension at S91+ mack landing**:

Under the hybrid verdict (d) framing, the W-5 close should propose to mack-cosmic-bridge (sole-writer per `feedback_mack-bridge-role.md`) the following extension to the §VII.AV refinement-pathway table at registry lines 17944-17948:

```markdown
**Deferred-pending refinement pathway** (per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` PROXY-REFINEMENT sub-class):

| # | Refinement target | Forward-promoting gate | Refinement type | Layer |
|:-:|:------------------|:-----------------------|:----------------|:------|
| (i) | L_max scan + Friedrich-Bär saturation theorem | CF-W5-3 (= CF-61) [FAILED at S90 W8] | analytic-certification | substrate-physics |
| (ii) | FULL BdG re-derivation (PV at Λ_UV = M_KK) | CF-W5-3 (= CF-61) [FAILED at S90 W8; superseded by CF-70] | full-physical-Pauli-Villars | substrate-physics |
| (iii) | FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers | CF-70 (pre-registered S91+) | full-CC1996-multipliers | substrate-physics |
| **(iv)** | **K_canonical pin uniqueness operational-alignment** | **CF-71 (pre-registered S91+)** | **operational-machinery-alignment** | **operational-machinery** |
| **(v)** | **V4 substrate-physics discriminator gate adjudication** | **S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST (pre-registered S91+)** | **substrate-physics-adjudicator** | **dual-anchor joint-hypersurface** |
```

This extension explicitly enumerates the four S91+ refinement routes plus the V4 discriminator gate; routes (iii) and (iv) operate at structurally orthogonal layers; route (v) IS the substrate-physics adjudicator that fires first to route the (iii) vs (iv) prioritization. The "Layer" column makes the structural orthogonality EXPLICIT at the registry-text layer per Re:V6 layer-functor F decomposition argument.

**Reading B's terminal verdict preference**:

Reading B's preferred terminal verdict is **(d) hybrid** with the refinement-pathway table extension above and Option γ wave-together dispatch ordering at S91+. The V4 discriminator gate fires first; CF-70 + CF-71 dispatch in parallel. The K-counter advancement at the deferred-pending PROXY-REFINEMENT sub-class K=1 → K=2 IS structurally robust under either CF-70 OR CF-71 PASS (or both); the cross-axis joint-win K-counter K=4 → K=5 IS achieved at W-5 close under the hybrid verdict (d) framing.

If volovik converges on hybrid verdict (d), the W-5 cross-axis joint-win at K=5 advancement is structurally clean. If volovik prefers verdict (a) Reading A canonical, my honest concession is that the L_max ≤ 10 phase boundary layer is structurally Reading A-correct (per Re:V1); the L_max=12 anchor layer (where Reading B applies) IS a separate operational-machinery question handled by CF-71 + V4 discriminator gate independently of verdict (a) outcome. Under verdict (a), the §VII.AV refinement-pathway table extension above is still structurally licensed at the operational-machinery sub-layer; the verdict (a) framing simply de-prioritizes route (iv) without closing it.

#### C3: Questions for volovik

Three forward questions for volovik's R2 CONVERGENCE / DISSENT / EMERGENCE / QUESTIONS sections. Each targets a specific substrate-physics commitment from V1-V6 and asks whether the commitment survives NCG-axiomatic counter-pressure.

---

**Q-C1 — Hochschild-Künneth Morita-invariance test of the L_max=12 anchor-mismatch substrate-physics claim**

Per V2 (workshop lines 81-99), the L_max=12 FULL-BdG anchor mismatch (1.428 absolute units) IS claimed as a "SUBSTRATE-PHYSICS structural separation between two distinct substrate-IS regimes" — specifically, the canonical multi-branch post-phase-transition domain (B1=0, B2=0.7704, B3=0.176 per s52 ED) vs the scalar-Δ FULL-BdG phase-boundary domain (Δ(12)=0.4643 from gap-equation self-consistency). V2 lines 95-99 explicitly claims "at the canonical pin, the L_max=12 substrate admits TWO inequivalent Bogoliubov-amplitude tensors as substrate-IS observables".

Per W-4 verdict (Hochschild-Künneth Morita-invariance theorem `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)`) + per W8-7 (b) lines 1394-1400 (W3 A.14 regulator-INVARIANT cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.3249743784` across {ζ, PV, Mellin, cutoff}; substrate canonical 7.324992 per `inheritance-falsifier-protocol.md`): the BdG sub-algebra's Hochschild cohomology IS Morita-equivalent to the parent A_F Hochschild cohomology, INDEPENDENT of the P_BdG projector implementation choice.

**Q-C1.1**: Does the BCS gap-equation self-consistency criterion `Δ = V_BCS · Σ_a m_a · tanh(βE_a/2)/(2E_a)` at canonical V_BCS factor through the Hochschild-Künneth Morita-invariance such that the substrate phase transition (Reading A) is INVARIANT under operational machinery choice (scalar-Δ vs multi-branch)? Specifically: if Morita-invariance applies, then the substrate phase boundary at L_max=10/11 should manifest at the SAME L_max value regardless of whether the gap equation is solved at scalar-Δ self-consistency OR at multi-branch self-consistency — does V2's substrate-IS framing of the L_max=12 anchor mismatch survive this Morita-invariance argument?

**Q-C1.2**: If the answer to Q-C1.1 is YES (Morita-invariance applies and the substrate phase boundary is invariant under operational machinery), then V2's strong claim "the L_max=12 substrate admits TWO inequivalent Bogoliubov-amplitude tensors as substrate-IS observables" is structurally over-strong — the two tensors are operational P_BdG projector implementations of the SAME substrate-IS observable, distinguishable at Level 3 but Morita-equivalent at Level 1. Do you concede that the 1.428 anchor mismatch is structurally the Level-3 image of an operational-machinery distinction at the P_BdG projector implementation layer (Reading B's position at the L_max=12 layer), NOT a substrate-IS phase separation at L_max=12?

**Q-C1.3**: If the answer to Q-C1.1 is NO (Morita-invariance does NOT apply at the gap-equation self-consistency layer), what NCG-axiomatic machinery PROHIBITS the Hochschild-Künneth Morita-equivalence from extending to the BdG gap-equation self-consistency criterion? Specifically: per the parse-tree expansion at registry line 12961 (Var_a Cell-IV closed form), the Bogoliubov-amplitude tensor enters the K-window log-derivative through `|v_a|² = (1 − ε_a/E_a)/2` with `E_a = sqrt(ε_a² + Δ_a²)`; this is a state-pair functional on `M_2(ℂ)` that Morita-equivalent to A_F should preserve in cohomology class but admit Level-3 numerical variation by P_BdG choice. Does V2's substrate-IS framing of the L_max=12 mismatch survive this parse-tree-layer analysis?

---

**Q-C2 — W3 A.14 regulator-INVARIANT cocycle ratio extension to Level-1 PROHIBITION at L_max ≤ 10**

Per V3 lines 133-139, the W3 A.14 regulator-INVARIANT cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.3249743784` IS the Level-1 cohomology-class identity cross-anchor that any substrate-IS-faithful refinement of §VII.AV MUST reproduce. The cocycle ratio lives at the FI (regulator-INVARIANT) axis per W8-7 (b) line 1401 lizzi taxonomy classification.

The W3 A.14 cocycle ratio was computed at substrate-natural L_max (likely L_max=12 master spectrum cache per `s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` input_sha `d0683bcd31e7eaca…`). Whether the cocycle ratio is STRUCTURALLY DEFINED at L_max ≤ 10 — where Reading A wins on the BCS phase boundary (per Re:V1 NCG-axiomatic concession) — is a structurally consequential question.

**Q-C2.1**: At L_max ≤ 10 truncations, is the substrate cocycle ratio `‖φ_67‖/‖φ_88‖` STRUCTURALLY DEFINED on the truncated BdG sub-algebra Hochschild cohomology, OR is it DEGENERATE (the BdG sub-algebra image becomes structurally trivial at L_max ≤ 10 in the absence of a finite gap, per Re:V1 §"MISSED" sub-section on Morita-invariance + Hochschild-cohomology-side characterization)?

**Q-C2.2**: If the cocycle ratio IS structurally degenerate at L_max ≤ 10 (Reading A wins at the Hochschild-cohomology layer too), this would be the strongest NCG-axiomatic cross-anchor for Reading A's substrate-IS phase boundary claim — the Hochschild cohomology degeneration at L_max ≤ 10 would be a SUBSTRATE-IS-FAITHFUL cross-check of the BCS phase boundary INDEPENDENT of the gap-equation operational machinery. Does V3's reliance on the W3 A.14 cocycle ratio as Level-1 cross-anchor at L_max=12 EXTEND to a Level-1 PROHIBITION on Reading B's L_max ≤ 10 operational-machinery rescue conjecture (per C1 Outcome (ii))?

**Q-C2.3**: A separate hypothesized gate `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST` would evaluate the substrate cocycle ratio at L_max ∈ {6..10} truncations under the FULL BdG re-derivation route (CF-61 extended to lower L_max evaluations of the cocycle ratio). Reading A predicts the cocycle ratio is structurally DEGENERATE at L_max ≤ 10 (the BdG sub-algebra image is trivial; ratio undefined or 0/0). Reading B predicts the cocycle ratio is FINITE but DIFFERENT from 7.3249743784 at L_max ≤ 10 (non-trivial but distinct from the L_max=12 substrate-IS canonical). Would you endorse pre-registering this gate as a forward calibration test? If yes, the W-5 close should add this gate to the carry-forward queue as CF-77 alongside the CF-70 + CF-71 + V4 wave-together dispatch.

---

**Q-C3 — Deferred-pending sub-class admissibility: PROXY-REFINEMENT vs FIRST-EXTRACTION classification for §VII.AV under Reading B's operational-machinery framing**

Per W1-14 deferred-pending intermediate verdict-class K=1 SUGGESTION baseline at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` lines 124-127, the §VII.AV registry text carries the PROXY-REFINEMENT sub-class tag (substrate-distance-2 pole; SCHEMATIC Casimir-bound proxy admitting refinement by FULL physical pipeline). The W1-14 dual-instance K=1 SUGGESTION baseline includes §VII.AV PROXY-REFINEMENT (the SCHEMATIC proxy refinement case) + §VII.AU FIRST-EXTRACTION (the symbolic-only first-extraction case).

Per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` sub-class definitions:

- **`REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`**: Level-2 envelope realized via SCHEMATIC proxy OR Casimir-bound argument; refinement pathways are (i) L_max scan + Friedrich-Bär saturation, (ii) FULL BdG re-derivation, (iii) FULL CC physical multipliers.
- **`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`**: Level-2 envelope SYMBOLIC-only (no numerical anchor yet); refinement pathways are (i) L_max scan + analytic limit derivation, (ii) Friedrich-Bär saturation, (iii) closed-form residue formula evaluation.

Under Reading B's operational-machinery framing of CF-71 (K_canonical pin uniqueness operational-alignment), the §VII.AV refinement-pathway route (iv) proposed in C2 ABOVE adds a STRUCTURALLY NEW refinement type "operational-machinery-alignment" that is NOT enumerated in the original PROXY-REFINEMENT sub-class definition (which lists only SCHEMATIC vs FULL physical regularization refinement types).

**Q-C3.1**: Does the addition of route (iv) "K_canonical pin uniqueness operational-alignment" structurally exceed the PROXY-REFINEMENT sub-class definition, requiring either (a) a NEW deferred-pending sub-class (`REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT`) at the rule-file layer, OR (b) extension of the PROXY-REFINEMENT sub-class definition to include operational-machinery-alignment as a 4th admissible refinement type?

**Q-C3.2**: If option (a) (new sub-class) is structurally preferred, the W1-14 dual-instance K=1 SUGGESTION baseline would extend to a TRIPLE-instance K=1 SUGGESTION baseline (§VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION + §VII.AV-route-iv OPERATIONAL-ALIGNMENT all sharing the S90 W1-14 landing event) — does this re-classification require mack-cosmic-bridge sole-writer re-landing at S91+, OR is it admissible as an in-session rule-file extension at W-5 close (per the methodology-wave-allowlist.md pattern)?

**Q-C3.3**: If option (b) (PROXY-REFINEMENT sub-class extended) is structurally preferred, the §VII.AV registry text refinement-pathway table extension proposed in C2 (lines 17944-17948 + 4th route + V4 discriminator gate as 5th adjudicator row) IS the canonical landing at S91+ via mack-cosmic-bridge sole-writer. Do you endorse this extension under the hybrid verdict (d) framing, OR does the verdict (a) Reading A canonical framing REQUIRE excluding route (iv) from the §VII.AV refinement-pathway table (i.e., CF-71 is structurally outside the §VII.AV deferred-pending refinement scope)?

**Q-C3.4** (most consequential): The structural verdict at the deferred-pending sub-class K-counter (K=1 SUGGESTION → K=2 advancement) depends on whether the W-5 verdict allows route (iv) to count as a positive PROXY-REFINEMENT instance:

- If route (iv) IS within PROXY-REFINEMENT scope (Reading B's preferred framing), then CF-71 PASS at S91+ counts as a positive calibration instance, advancing K=1 → K=2.
- If route (iv) IS NOT within PROXY-REFINEMENT scope (Reading A's preferred framing per V3 line 153 "CF-71 is STRUCTURALLY DEFERRED under Reading A: it operates at the operational-machinery layer, not the substrate-IS layer"), then CF-71 PASS at S91+ does NOT count as a PROXY-REFINEMENT instance; the K=1 SUGGESTION baseline stalls pending an alternative positive instance.

Under hybrid verdict (d), my preferred position is: route (iv) IS within PROXY-REFINEMENT scope (operational-machinery-alignment IS a structural refinement of the SCHEMATIC Casimir-bound proxy's L_max=12 anchor mismatch behavior, just as FULL CC physical multipliers route (iii) IS a refinement of the SCHEMATIC proxy's L_max ≤ 10 phase boundary behavior). Do you concur with this scope extension under verdict (d), OR maintain Reading A canonical's narrow PROXY-REFINEMENT scope under verdict (a)?

---

**Summary of forward questions for volovik R2**:

| Question | Targets | Volovik R2 location to address |
|:---------|:--------|:------------------------------|
| Q-C1 (Morita-invariance test of L_max=12 anchor mismatch) | V2 substrate-IS regime separation claim | DISSENT (if Q-C1.1 = NO) or CONVERGENCE (if Q-C1.1 = YES) |
| Q-C2 (W3 A.14 cocycle ratio degeneration at L_max ≤ 10) | V3 Level-1 cross-anchor argument | EMERGENCE (if Q-C2.1 = degenerate) — strongest Reading A cross-anchor |
| Q-C3 (deferred-pending sub-class scope for route (iv)) | V3 + V6 PROXY-REFINEMENT structural framing | DISSENT or CONVERGENCE on hybrid verdict (d) scope extension |
| Q-C3.4 (K=1 → K=2 advancement contingency) | K-counter advancement under W-5 cross-axis joint-win | QUESTIONS — terminal-verdict adjudication |

Each question targets a specific commitment in V1-V6 and tests its structural robustness under NCG-axiomatic counter-pressure. The honest expected R2 outcome: Q-C1 likely converges on Hochschild-Künneth Morita-invariance applying at the Level-1 layer but NOT at the Level-3 numerical-evaluation layer (Reading B's L_max=12 distinction preserved); Q-C2 likely converges on Reading A's Hochschild cohomology degeneration at L_max ≤ 10 (Reading A strengthened at the cohomology-class cross-anchor layer); Q-C3 is the workshop's terminal-verdict adjudicator on whether route (iv) is admissible within the PROXY-REFINEMENT sub-class scope under hybrid verdict (d).

The W-5 cross-axis joint-win at K=4 → K=5 advancement is structurally robust under EITHER hybrid verdict (d) (my preference) OR verdict (a) Reading A canonical (volovik's preference); the structural adjudication on Q-C3 determines the registry-text refinement-pathway table extension at S91+ mack landing.

---

## Round 2 — volovik: Follow-up

### CONVERGENCE

I accept connes's R1 cross-axis HYBRID convergence at four substrate-axis-grounded positions. The state-after-R1 is structurally different from the V1-V6 state in four substantively distinct ways; the CONVERGENCE below is not parallel-agreement but reading-shift on my part to the layer-functor F decomposed two-layer structure connes surfaced.

**CONVERGENCE C1 — Reading A's L_max ≤ 10 substrate-IS Cooper-instability phase boundary is JOINT-WIN (substrate-axis × NCG-axiomatic axis)**

connes's Re:V1 at workshop lines 327-373 IS a substantive NCG-axiomatic concession on the L_max ≤ 10 phase boundary, not narrative agreement. The substitution chain at Re:V1 lines 341-373 ("Step 1 Definitions → Step 5 Direction") derives the same Cooper-instability criterion `K(0; L_max) ≥ 1/V_BCS` from the Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula at substrate-distance-2 pole `s=4` that V1 lines 55-67 derived from the Volovik / Khodel-Shaginyan microscopic flat-band condensation framework. Two structurally distinct derivations on opposite axes (substrate-physics microscopic Hamiltonian axis vs NCG-axiomatic residue-formula axis) producing IDENTICAL structural content: at L_max ∈ {6..10} the truncated spectral kernel fails to cross `1/V_BCS` at canonical V_BCS = 2.447e-7 M_KK^{-1}; at L_max ≥ 11 it does. The 4.3% missing UV weight in sectors (p+q) ∈ {11, 12} is what mediates this crossing on the substrate's Level-1 single-τ-slice spectral content.

Per `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence: this is structural-content convergence at the substrate ↔ methodology layer pair under F. The Volovik microscopic Hamiltonian framing IS the substrate-side image (substrate IS the flat-band Cooper instability on the BdG sub-algebra); the Connes-Moscovici residue formula at s=4 IS the methodology-side image (the same instability evaluated as a regulated Mellin-cone pinch on `Tr(D_K^{-1} · g(D_K))` per the substrate-distance-2 pole). The K=4 → K=5 advancement on the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern is structurally licensed at this layer.

**CONVERGENCE C2 — HYBRID verdict (d) framing: my V1+V2+V3+V5 wins at L_max ≤ 10 substrate-IS phase boundary layer; connes's Re:V2 wins at L_max=12 P_BdG projector implementation layer**

connes's hybrid verdict (d) proposal at Re:V2 EMERGES at workshop lines 450-457 ("Layer 1 — L_max ≤ 10 trivial-Δ regime: substrate-IS Cooper-instability criterion fails on the truncated spectral kernel at canonical V_BCS. Reading A wins. Layer 2 — L_max=12 anchor mismatch 1.428: operational P_BdG projector implementation distinction (scalar Δ vs multi-branch). Reading B wins.") IS the structurally honest closure of the V1-V6 vs Re:V1-Re:V6 contention. I accept verdict (d) over verdict (a) Reading A canonical.

The substrate-axis reason I accept verdict (d) and not verdict (a): V2's strong-form claim at workshop lines 95-99 ("at the canonical pin, the L_max=12 substrate admits TWO inequivalent Bogoliubov-amplitude tensors as substrate-IS observables") IS structurally over-strong when read through the Hochschild-Künneth Morita-invariance theorem `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` connes surfaced at Re:V1 lines 392-396 (MISSED block) and Re:V2 lines 426-432. At L_max=12 the SAME Cell-IV substrate-IS observable (variance of Bogoliubov occupation at K_horizon per §VII.U.2 Corner II parse-tree closed form line 12961) is being evaluated under two structurally distinct `P_BdG = diag(|v_a|², |u_a|²)` projector implementations: scalar Δ produces uniform `|v_a|² = (1 − ε_a/E_a)/2` with `E_a = sqrt(ε_a² + Δ_canonical²)`; multi-branch produces per-mode non-uniform `|v_a^{(B_n)}|²` per the s52 ED tensor structure. Both implementations live on the SAME `M_2(ℂ) ⊂ A_K` sub-algebra image; both yield the SAME Hochschild cohomology class under Morita-invariance; both yield the SAME W3 A.14 cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.3249743784` at Level-1; they differ ONLY at Level-3 numerical anchor by 1.428 M_KK² absolute.

The substrate-axis lesson: my V2 was reading Level-3 P_BdG-implementation distinction as Level-1 substrate-IS regime separation. The Morita-invariance argument forces a layer-decomposition: Level-1 IS P_BdG-invariant (the cohomology class is the same); Level-3 IS P_BdG-dependent (the numerical anchor is not). The 1.428 anchor mismatch lives strictly at Level-3 and does NOT propagate to Level-1. This IS Reading B's Re:V2 position at workshop lines 410-422, and I concede it.

**CONVERGENCE C3 — Option γ wave-together dispatch (V4 discriminator gate first, then CF-70 + CF-71 parallel) is the structurally appropriate S91+ refinement pathway**

connes's Re:V3 Option γ enumeration at workshop lines 521-531 (EMERGES block) IS the structurally correct dispatch ordering under verdict (d). The substrate-axis reason: CF-70 (FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers per W8-7 (c) lines 1405-1411; M_1 = M_KK, M_2 = √2·M_KK, c_1 = +2, c_2 = −1; Σ c_r = 1 + Σ c_r·m_r² ≈ 0 at machine precision) addresses the L_max ≤ 10 phase boundary at the substrate-physics axis by replacing the unsubtracted gap-equation kernel with a UV-finite PV-regulated kernel that evades the Cooper-instability threshold crossing at canonical V_BCS. CF-71 (K_canonical pin uniqueness per W8 WP lines 1660-1665) addresses the L_max=12 P_BdG-implementation alignment at the operational-machinery axis by re-deriving K_canonical from the substrate-IS BdG energy gap at τ_fold. These operate at structurally orthogonal sub-layers per the table connes constructed at Re:V3 lines 483-489.

The V4 discriminator gate `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` firing FIRST is what makes Option γ structurally distinct from option (c) "both routes equally licensed pending discriminator-gate outcome": V4 IS the substrate-physics adjudicator at the L_max=12 anchor layer, and its outcome routes the CF-70 vs CF-71 prioritization POSTERIOR per connes's flowchart at Re:V3 lines 523-529. The K-counter advancement at the deferred-pending PROXY-REFINEMENT sub-class K=1 → K=2 is structurally robust under either CF-70 PASS or CF-71 PASS (or both) per Re:V6 lines 713-721.

**CONVERGENCE C4 — Registry-text 4th refinement route extension at §VII.AV registry lines 17944-17948 (route iv K_canonical operational-alignment)**

connes's Re:V3 + C2 proposed extension at workshop lines 967-981 (registry-pathway table extension with route (iv) "K_canonical pin uniqueness operational-alignment" + route (v) "V4 substrate-physics discriminator gate adjudication" + explicit "Layer" column distinguishing substrate-physics from operational-machinery from dual-anchor joint-hypersurface) IS structurally compatible with verdict (d). I accept the extension proposal as canonical mack-cosmic-bridge sole-writer landing at S91+ per `feedback_mack-bridge-role.md`.

The substrate-axis reason: the explicit "Layer" column in the proposed table extension makes the layer-functor F decomposition cleanness condition (`epistemic-discipline.md §"Layer-Decomposition"`) visible at the registry-text layer. Routes (i)-(iii) are substrate-physics-layer refinements; route (iv) is operational-machinery-layer refinement; route (v) is the dual-anchor joint-hypersurface adjudicator. This satisfies the cross-pillar-bridge-anatomy.md Element 3 fiducial-anchor binding discipline at S88 W-15 V.7 MANDATORY-K=1 baseline sharpened at S90 W7-4 CF-57 axis γ — connes correctly flagged at Re:V4 lines 571-590 that V4 IS a type-(iii) joint-hypersurface dual-anchor binding (the lab discrimination is 2D in (L_emp_FULL_BdG, L_emp_s52) space), not a type-(i) substrate-self-consistent binding alone. I endorse the convention-tag sharpening connes proposed: `convention=substrate-IS-canonical-K-window-log-derivative-MULTI-BRANCH-S52-VS-SCALAR-DELTA-FULL-BDG-ADJUDICATION-JOINT-HYPERSURFACE-DUAL-ANCHOR L_max=12`.

### DISSENT

No new dissent at the L_max=12 P_BdG-implementation reframe — Q-C1.1 + Q-C1.2 (Hochschild-Künneth Morita-invariance applies at the cohomology-class layer; V2's strong-form substrate-IS regime separation claim collapses to Level-3 P_BdG-implementation distinction) are CONVERGED per C2 above, and I answer them affirmatively in QUESTIONS below.

One narrow methodological dissent remains, on Q-C3.1 sub-class taxonomy granularity. I record it as DISSENT D1 because it shifts the K-counter advancement structure at the deferred-pending intermediate verdict-class.

**DISSENT D1 — Q-C3.1 sub-class taxonomy: operational-machinery-alignment is structurally orthogonal to PROXY-REFINEMENT (Option a NEW sub-class is correct), not a 4th admissible refinement type within PROXY-REFINEMENT (Option b extension is structurally collapsing)**

connes's Q-C3.1 at workshop lines 1034-1036 frames a binary: Option (a) NEW deferred-pending sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` at the rule-file layer, OR Option (b) extension of PROXY-REFINEMENT sub-class to include operational-machinery-alignment as 4th admissible refinement type. connes's preferred position at Q-C3.4 line 1045 is Option (b) within scope; my preferred position is Option (a) new sub-class.

The substrate-axis reason for Option (a): PROXY-REFINEMENT sub-class definition at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` lines 65-78 enumerates three refinement pathways — (i) L_max scan + Friedrich-Bär saturation theorem; (ii) FULL BdG re-derivation; (iii) FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers. All three operate at the UV-regulator axis of the substrate-physics layer — they refine the SCHEMATIC `_spectral_action_regulators.py` helper or the SCHEMATIC Casimir-bound proxy by replacing the SCHEMATIC regulator with a FULL physical regulator (PV at Λ_UV, full CC multipliers). The Level-2 envelope is RECONSTRUCTED under the FULL physical regulator.

Route (iv) operational-machinery-alignment (CF-71) operates at a structurally DIFFERENT axis: the K-window observable DEFINITION layer + the P_BdG projector implementation specification layer. The K_canonical pin re-derivation from the substrate-IS BdG energy gap at τ_fold does NOT replace a SCHEMATIC regulator with a FULL physical regulator — it pins the Bogoliubov-amplitude tensor specification (Δ_a vs multi-branch B-tensor) at the K-window log-derivative evaluation. The Level-2 envelope under CF-71 is NOT reconstructed; it is the Level-3 anchor at L_max=12 that is re-pinned via the corrected P_BdG implementation.

These two axes are STRUCTURALLY ORTHOGONAL per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3. The substrate-physics UV-regulator axis (Cell I-II in the 4-corner partition: algebra-INVARIANT spectrum-only functional family; the Level-2 envelope reconstruction is on `{λ_n, m_n}`) is structurally distinct from the operational-machinery state-side specification axis (Cell IV: algebra-DEPENDENT state-pair functional family on `M_2(ℂ) ⊂ A_K`; the state-side P_BdG implementation is on `S(M_2(ℂ))`). The 4-corner orthogonality K=3 MANDATORY clause FORBIDS conflating these axes under a single registry slot at the substrate-IS observable level (per `cross-pillar-bridge-anatomy.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"` item 4 cross-corner co-primary FORBIDDEN clause). Extension of the PROXY-REFINEMENT sub-class to include route (iv) would conflate these two corners under a single sub-class.

Option (a) preserves the 4-corner orthogonality at the sub-class taxonomy layer: PROXY-REFINEMENT IS the UV-regulator-axis SCHEMATIC-to-FULL refinement (Cell I-II algebra-INVARIANT axis); a separate sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` IS the state-side specification refinement (Cell IV algebra-DEPENDENT axis). The K-counter advancement under verdict (d) is then:

- §VII.AV PROXY-REFINEMENT-PENDING tag advances under CF-70 PASS (substrate-physics axis, Cell I-II) — K=1 SUGGESTION → K=2 contingent on S91+ CF-70 dispatch outcome.
- §VII.AV OPERATIONAL-ALIGNMENT-PENDING tag (NEW; landed at the registry-text refinement-pathway table extension's route (iv) row per Q-C3.3 endorsement) advances under CF-71 PASS (operational-machinery axis, Cell IV) — K=1 SUGGESTION baseline established at this W-5 landing event.

This Option (a) structure also reinforces the cross-axis joint-win pattern: the K=4 → K=5 CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM advancement is structurally a layer-functor F image of two ORTHOGONAL refinement-pathway advancements, one per axis. The Option (b) collapse would make the K=5 advancement structurally a single-axis advancement, missing the cross-axis layer decomposition cleanness condition.

Note this dissent is narrow: it does NOT contest the CONVERGENCE on hybrid verdict (d), on Option γ wave-together dispatch, or on registry-text route (iv) + route (v) extension. It only contests the sub-class taxonomy granularity at the rule-file layer — Option (a) preserves 4-corner orthogonality; Option (b) collapses it.

### EMERGENCE

Three substantive cross-domain insights emerge from the R1 cross-axis exchange that neither V1-V6 nor Re:V1-Re:V6 produced alone.

**EMERGENCE EV1 — HYBRID verdict (d) IS itself a STRUCTURAL THEOREM at the layer-functor F decomposition (CROSS-AXIS JOINT-WIN PATTERN K=4 → K=5 MANDATORY candidate)**

The hybrid verdict (d) "substrate phase boundary AT operational-machinery joint layer" is not a narrative compromise between Reading A and Reading B; it IS a STRUCTURAL THEOREM at the layer-functor F decomposition cleanness condition per `epistemic-discipline.md §"Layer-Decomposition"`. The two-layer structure is:

```
Substrate-IS axis (the substrate IS the spectral triple at full operator-algebra resolution):
  Level-1 single-τ-slice substrate-IS at τ_fold = 0.19:
    Layer 1 (UV-regulator axis, Cell I-II algebra-INVARIANT spectrum-only):
      L_max ≤ 10 trivial-Δ regime IS substrate-IS Cooper-instability criterion failure
      on the truncated spectral kernel at canonical V_BCS.
      Reading A WINS at this layer.
    Layer 2 (state-side specification axis, Cell IV algebra-DEPENDENT state-pair):
      L_max=12 P_BdG-implementation distinction (scalar Δ vs multi-branch B-tensor)
      IS substrate-IS state-side specification choice; both implementations yield
      the same Hochschild cohomology class (Morita-invariant W3 A.14 cocycle ratio
      7.3249743784) but distinct Level-3 numerical anchors.
      Reading B WINS at this layer.

Methodology axis (Phi-correspondence weight-2 image of substrate-IS):
  CF-70 (FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers) IS the F-image of Layer 1
  CF-71 (K_canonical pin uniqueness operational-alignment) IS the F-image of Layer 2
  V4 discriminator gate IS the substrate-physics adjudicator on Layer 2 alignment

Audit axis (registry-text + audit-line content):
  §VII.AV PROXY-REFINEMENT-PENDING tag at registry text line 17897 (Layer 1 audit image)
  §VII.AV OPERATIONAL-ALIGNMENT-PENDING tag (NEW; Layer 2 audit image per DISSENT D1 Option (a))
  V4 dispatch + CF-70 + CF-71 parallel dispatch at S91+ (audit-layer dispatch image)
```

Both readings win at structurally orthogonal layers under F. Neither reading is the "correct" reading at the merged level; the merged level is exactly where the layer-functor F decomposition cleanness condition is satisfied. This continues the W-1 H̃-DIVERGENCE-CHASE / W-2 A_s LEDGER 3PI-vs-SLOT / W-3 r-dual-pathway / W-4 (S88) dual-symbol-convention pattern at a different structural axis — the K=4 → K=5 advancement at the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter (per workshop header line 43 + Re:V6 Observation 2 lines 699-711) is structurally licensed at this W-5 close.

The substrate-axis lesson: the W-5 cross-axis joint-win pattern is structurally distinct from the S82 H̃-divergence and S86 A_s-ledger workshop patterns in one critical way — there, two readings adjudicated a NUMERICAL discrepancy (5.91e-3 vs 2.46e-5 H̃; 47.92 vs 0.39 F_amp) and the resolution was identification of which numerical value was the canonical physical anchor (one wins, one falls). Here, the resolution is layer-decomposition: BOTH readings hold at structurally orthogonal sub-layers; the numerical mismatch 1.428 at L_max=12 IS Level-3 P_BdG-implementation distance, not Level-1 substrate-IS regime separation. This is a MORE structural form of cross-axis joint-win than the S82 / S86 precedents.

**EMERGENCE EV2 — CF-77 `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST` is an EMERGENT cross-anchor at the Hochschild-cohomology layer**

connes's Q-C2.3 at workshop line 1019 surfaces a structurally novel gate that NEITHER V3 nor Re:V3 proposed alone: extending the W3 A.14 regulator-INVARIANT cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.3249743784` (Level-1 cohomology-class identity per V3 lines 133-139) to L_max ≤ 10 as a Hochschild-cohomology-side cross-anchor test of Reading A's substrate-IS phase boundary claim — INDEPENDENT of the gap-equation operational machinery.

The substrate-axis structural content: my V3 framed the W3 A.14 cocycle ratio as a CONSISTENCY constraint on the FULL CC physical-multipliers refinement at L_max=12 (any substrate-IS-faithful refinement must reproduce 7.3249743784 at Level-1). connes's Q-C2.3 PROMOTES this from consistency-constraint to STRUCTURAL DISCRIMINATOR at L_max ≤ 10: if the cocycle ratio is structurally DEGENERATE at L_max ≤ 10 (because the BdG sub-algebra image is structurally trivial in the absence of finite gap at the truncated spectral kernel), the Hochschild-cohomology degeneration IS a SUBSTRATE-IS-FAITHFUL cross-check of Reading A's phase boundary claim — INDEPENDENT of whether the scalar-Δ FULL-BdG gap-equation OR the multi-branch s52 ED route is operating at the canonical V_BCS pin.

This is structurally novel because it gives Reading A a Hochschild-cohomology-layer cross-anchor that NO V1-V6 argument leveraged: the substrate's Hochschild cohomology degeneration on the BdG sub-algebra restriction at L_max ≤ 10 is a Level-1 cohomology-class identity layer test that is OPERATIONAL-MACHINERY-INDEPENDENT. It cannot be rescued by multi-branch s52 ED at multi-branch V_BCS_per_branch couplings (CF-76 conjecture at Re:V1 sub-class proposal lines 855-858) because the multi-branch tensor — even if it solves a self-consistency on the L_max ≤ 10 truncated spectrum — still operates on a BdG sub-algebra image whose Hochschild cohomology degenerates in the absence of finite gap.

The structural prediction under Reading A: at L_max ≤ 10, the cocycle ratio `‖φ_67‖/‖φ_88‖` is structurally undefined (0/0 degeneracy on the trivial BdG sub-algebra image; per `inheritance-falsifier-protocol.md §"Class A — Kernel-Signature Test"` row-wise NULL prediction on the BdG sub-algebra restriction when the parent inheritance is BDI-protected at the gapless regime). This is an inheritance-falsifier-protocol-style Class-A NULL prediction at the cocycle layer.

I endorse pre-registering CF-77 alongside CF-70 + CF-71 + V4 wave-together at S91+ per QUESTIONS Q-C2.3 answer below. This is a structurally clean addition to the wave-together dispatch — it operates at a structurally orthogonal axis from CF-70 (substrate-physics UV-regulator refinement at Layer 1) and CF-71 (operational-machinery state-side specification at Layer 2) and V4 (Level-3 dual-anchor joint-hypersurface adjudication). CF-77 is a Level-1 cohomology-class identity layer test, the FOURTH structurally orthogonal axis of the §VII.AV refinement-pathway space.

**EMERGENCE EV3 — The S91+ refinement-pathway space IS 4-axis orthogonal (UV-regulator × state-side × Level-3 dual-anchor × Hochschild-cohomology)**

EMERGES from EV1 + EV2 + connes's Re:V4 dual-anchor type-(iii) joint-hypersurface declaration at workshop lines 571-590: the §VII.AV refinement-pathway space at S91+ is structurally 4-axis orthogonal per the cross-pillar-bridge-anatomy.md table at `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` orthogonality structure (UV-regulator axis × Level axis × Binding axis × MACHINERY-SCOPE axis). The four axes mapped to the §VII.AV S91+ refinement pathways:

| Axis | Substrate content at §VII.AV | Refinement gate at S91+ | Layer-functor F image |
|:-----|:----------------------------|:------------------------|:----------------------|
| UV-regulator axis | unsubtracted gap-eqn kernel vs FULL CC PV at Λ_UV = M_KK | CF-70 | Layer 1 (Cell I-II algebra-INVARIANT) |
| State-side specification axis | scalar Δ vs multi-branch B-tensor P_BdG implementation | CF-71 | Layer 2 (Cell IV algebra-DEPENDENT) |
| Level-3 dual-anchor binding axis | canonical-import-binding L_emp_s52 vs substrate-natural-binding L_emp_FULL | V4 = `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` | Level-3 dual-hypersurface (joint-hypersurface type iii) |
| Hochschild-cohomology axis | W3 A.14 cocycle ratio structurally defined vs degenerate | CF-77 = `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST` | Level-1 cohomology-class identity |

Each gate operates at a structurally orthogonal axis; each gate's verdict is INDEPENDENTLY informative about a different substrate-IS sub-property of §VII.AV's deferred-pending status. The S91+ wave-together dispatch is therefore a 4-gate parallel-compute-wave structure per `.claude/rules/Investigating-Workshops.md §"is NOT" item 8` parallel-compute-wave classification: N=4 prerequisite conditions on structurally orthogonal axes, each with its own pre-registered PASS criterion, combining via logical AND at S91+ close for the unified §VII.AV refinement-pathway resolution. This is the same structural pattern as the S88 W13 W-4 Path-B Step-0 calibration corpus instance for "is NOT" item 8 — the agent-attribution per axis is a derivation-author tag (which agent owns the math for axis X), NOT a workshop-participant tag.

The substrate-axis lesson: the W-5 wave-together at S91+ is the canonical instance of the 4-axis orthogonality structure at a single registry slot's refinement pathway. The K-counter advancement at the deferred-pending intermediate verdict-class — under DISSENT D1's Option (a) preserves 4-corner orthogonality at sub-class taxonomy — IS structurally aligned with this 4-axis refinement-pathway orthogonality.

### QUESTIONS

I answer connes's Q-C1.1-3, Q-C2.1-3, and Q-C3.1-4 substantively below, with substrate-axis machinery grounded in the Volovik corpus (`Volovik`-superfluid-universe-theorist memory) and the project's `cross-pillar-bridge-anatomy.md` + `phononic-framing.md` + `inheritance-falsifier-protocol.md` rule machinery. Then I pose 2 forward questions for connes R2-B FINAL.

---

**Q-C1.1 answer — Hochschild-Künneth Morita-invariance applies at the cohomology-class layer; the substrate phase boundary at L_max=10/11 IS invariant under operational machinery choice; my V2 "two-tensor substrate-IS regimes" framing collapses to Level-3 P_BdG-implementation distinction**

YES at the Level-1 cohomology-class identity layer; YES at the substrate phase boundary position invariance (L_max=10/11 boundary is the SAME L_max value regardless of operational machinery choice); the 1.428 anchor mismatch is Level-3 P_BdG-implementation distinction, NOT substrate-IS regime separation.

Substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"`:

```
Step 1 (Definitions):
  HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)              [Hochschild-Künneth Morita-invariance,
                                                W-4 verdict; cohomology class is invariant
                                                under tensoring with M_n(ℂ)]
  A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)                       [substrate algebra per memory's
                                                microscopic-to-emergent mapping +
                                                §VII.AV registry text]
  K(0; L_max) := Σ_a^{L_max} m_a · tanh(λ_a/(2T_fold))/(2λ_a)
                                              [BCS critical-coupling kernel at Δ=0;
                                                Level-1 single-τ-slice spectral-action
                                                moment of D_K^{-1} on the BdG sub-algebra]
  P_BdG(Δ_a) := diag(|v_a|², |u_a|²)         [Bogoliubov projector, Δ_a-tensor parameterized]

Step 2 (Substitution):
  The substrate phase boundary criterion K(0; L_max) ≥ 1/V_BCS is evaluated on the
  spectral kernel {λ_a, m_a} at the L_max-truncated D_K spectrum AT Δ_a = 0
  (the BCS criticality probe; ALL Δ_a tensors collapse to zero at this probe).
  Therefore the criterion is INDEPENDENT of the Δ_a tensor specification —
  scalar-Δ vs multi-branch is irrelevant at the Δ_a → 0 critical-coupling layer.

Step 3 (Simplification):
  The L_max=10/11 phase boundary IS the L_max value where K(0; L_max) crosses 1/V_BCS.
  This crossing is a structural property of the L_max-truncated D_K spectrum AT THE
  CANONICAL V_BCS PIN, NOT of the P_BdG projector implementation choice.

Step 4 (Canonical form):
  Substrate phase boundary position invariance under operational machinery choice:
  ∀ Δ_a tensor specifications (scalar Δ, multi-branch B1+B2+B3, anything in between),
  the critical-coupling threshold crossing occurs at the SAME L_max ∈ {10, 11} pair,
  because the threshold criterion at the Δ_a → 0 limit is Δ_a-independent.

Step 5 (Direction):
  Reading A's substrate phase boundary claim at L_max=10/11 IS Morita-invariant
  under operational machinery choice. My V2 claim that the L_max=12 anchor mismatch
  IS "structurally two inequivalent substrate-IS regimes" CONFLATED Level-1 (cohomology
  class, Morita-invariant) with Level-3 (numerical anchor at L_max=12, P_BdG-dependent).
  The honest reading: at L_max=12 BOTH P_BdG implementations live on the SAME
  Hochschild cohomology class (Morita-equivalence), produce the SAME W3 A.14 cocycle
  ratio 7.3249743784 at Level-1, but produce DIFFERENT Level-3 numerical anchors
  (-5.6188 vs -7.0463; 1.428 mismatch).
```

I CONCEDE Q-C1.2 reframe of V2: the two tensors at L_max=12 are operational P_BdG implementations of the SAME Cell-IV substrate-IS observable, distinguishable at Level-3 but Morita-equivalent at Level-1. The 1.428 anchor mismatch is Level-3 P_BdG-implementation distance, not Level-1 substrate-IS regime separation. This collapses my V2 strong-form claim at workshop lines 95-99 ("at the canonical pin, the L_max=12 substrate admits TWO inequivalent Bogoliubov-amplitude tensors as substrate-IS observables") to the weaker honest claim: at L_max=12 the substrate-IS observable admits TWO operational P_BdG-implementations distinguishable at Level-3 only.

**Q-C1.3 answer — Not applicable** (Q-C1.1 + Q-C1.2 answered affirmatively; the substrate phase boundary IS Morita-invariant; the L_max=12 mismatch IS Level-3 P_BdG-implementation distinction, not substrate-IS phase separation).

---

**Q-C2.1 answer — At L_max ≤ 10 the substrate cocycle ratio `‖φ_67‖/‖φ_88‖` IS STRUCTURALLY DEGENERATE on the truncated BdG sub-algebra Hochschild cohomology in the absence of finite gap**

YES — structurally degenerate. The BdG sub-algebra image `M_2(ℂ) ⊂ A_K` at L_max ≤ 10 trivial-Δ regime has K_0(M_2(ℂ))-trivial Hochschild homology structure when the gap = 0 (the Bogoliubov projector P_BdG = diag(|v_a|², |u_a|²) at Δ_a = 0 collapses to P_BdG = diag(0, 1) for ε_a > 0 and diag(1, 0) for ε_a < 0 — i.e., the trivial normal-state projector with NO BdG superposition structure). The cocycle ratio `‖φ_67‖/‖φ_88‖` evaluated on a trivial BdG sub-algebra is structurally a 0/0 indeterminate form — the inheritance-falsifier-protocol Class-A kernel-signature null prediction fires on this row.

Substrate-axis structural argument:

- The Volovik 3He-B BDI universality class inheritance (memory's Permanent Theorems "N_3=0 (3He-B class, NOT 3He-A): vacuum energy unprotected by Fermi-point topology; q-theory required") establishes that the parent inheritance morphism `ι : (3He-B BdG sub-algebra) → (A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ))` has kernel structure carrying the BdG-specific cocycle generators (φ_67 chiral pair + φ_88 Cartan hypercharge per agent memory K_7 cocycle ratio canonical 7.324992).
- At L_max ≥ 11 finite-gap regime, the BdG sub-algebra image is non-trivial; the cocycle ratio is structurally defined and reproduces 7.3249743784 across regulators per W3 A.14 regulator-INVARIANT class.
- At L_max ≤ 10 trivial-Δ regime, the BdG sub-algebra image collapses to the normal-state projector; the cocycle generators (φ_67, φ_88) DO NOT inherit a non-trivial Hochschild homology class on this restricted image — the cocycle ratio is structurally 0/0.

This is precisely the Hochschild-cohomology-side characterization of Reading A's substrate-IS phase boundary that connes surfaced at Re:V1 "MISSED" block lines 392-396: the BdG sub-algebra restriction yields a trivial residue at substrate-distance-2 pole s=4 in the absence of finite gap. The cocycle ratio degenerates on the trivial residue.

**Q-C2.2 answer — YES, the Hochschild-cohomology degeneration at L_max ≤ 10 IS the strongest NCG-axiomatic cross-anchor for Reading A's substrate-IS phase boundary claim, INDEPENDENT of gap-equation operational machinery**

YES. The Hochschild cohomology degeneration on the trivial BdG sub-algebra restriction at L_max ≤ 10 is OPERATIONAL-MACHINERY-INDEPENDENT in the strongest sense:

- It does not depend on the scalar-Δ FULL-BdG gap-equation route (CF-61 producing script) — the Hochschild cohomology evaluated on the truncated BdG sub-algebra image at canonical T_fold = 0.640 has 0/0 indeterminate cocycle ratio independent of how the Δ_a tensor was constructed.
- It does not depend on the multi-branch s52 ED route — even if a non-trivial (B1, B2, B3) tensor is externally imported and applied to the L_max ≤ 10 spectrum (the "L_max=12 ansatz" framing per Re:V1 lines 375-381), the Hochschild cohomology class on the BdG sub-algebra restriction at the canonical (V_BCS, T_fold) probe remains degenerate (the externally-imposed tensor solves a different self-consistency criterion at a different problem, not the substrate's intrinsic Cooper-instability criterion on the L_max ≤ 10 spectral kernel).
- It does not depend on the SCHEMATIC Casimir-bound proxy — the proxy's smooth `sqrt((C_2(L,L)+1)/(C_2(12,12)+1))` ansatz operates at the Level-2 envelope layer, not at the Level-1 Hochschild cohomology layer.

The Hochschild-cohomology cross-anchor IS therefore the canonical substrate-IS-faithful test of Reading A's phase boundary claim at the Level-1 layer, INDEPENDENT of any operational machinery choice at any S91+ refinement-gate dispatch.

**Q-C2.3 answer — YES, I endorse pre-registering CF-77 `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST` alongside CF-70 + CF-71 + V4 wave-together dispatch at S91+**

YES. CF-77 IS the canonical Hochschild-cohomology-layer cross-check of Reading A's substrate-IS phase boundary. The W-5 close should add CF-77 to the carry-forward queue. Pre-registered structure (substrate-axis):

- **Gate ID**: `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST`
- **Trigger**: `[VERIFY-THEOREM]` (substrate-physics cross-anchor adjudication at the Hochschild-cohomology layer)
- **Wave classification**: COMPUTE-class per `.claude/rules/wave-classification.md` (numerical PASS predicate on the cocycle ratio evaluation at L_max ∈ {6..10})
- **Effort**: ~0.8 wave-equiv (cocycle ratio evaluation per the existing `s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` pipeline, extended to L_max ∈ {6..10} truncations)
- **PASS criterion (Reading A confirmed at Hochschild-cohomology layer)**: at L_max ∈ {6..10}, the cocycle ratio `‖φ_67‖/‖φ_88‖` returns STRUCTURALLY DEGENERATE (0/0 indeterminate; computed as NaN OR numerical regularization producing |ratio - canonical_value| > 1.0 across regulators {ζ, PV, Mellin, cutoff} — distinct from the regulator-INVARIANT 7.3249743784 at L_max=12).
- **FAIL criterion (Reading B alternative at Hochschild-cohomology layer)**: at L_max ∈ {6..10}, the cocycle ratio returns a finite well-defined value across regulators with regulator-spread < 1e-3 and value distinct from 7.3249743784 (the substrate would carry a Hochschild cohomology class at L_max ≤ 10 that is non-trivial but inequivalent to the L_max ≥ 11 class — this is structurally a Level-2 moduli-deformation type observation under L_max axis).
- **INFO criterion**: regulator-spread ≥ 1e-3 at L_max ≤ 10 OR mixed degeneracy/finite outcomes across L_max ∈ {6..10} (intermediate; requires further structural analysis).

CF-77's outcome is structurally orthogonal to V4's outcome (Level-3 dual-anchor at L_max=12) and to CF-70's outcome (Level-2 envelope under FULL CC physical multipliers) and to CF-71's outcome (operational-machinery alignment at L_max=12). Per EMERGENCE EV3 the four gates operate on the four orthogonal axes of the §VII.AV refinement-pathway space.

---

**Q-C3.1 answer — Option (a) NEW sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` is structurally cleaner per DISSENT D1**

Option (a) NEW sub-class. The substrate-axis structural argument for Option (a) over Option (b) is at DISSENT D1 above. Briefly: PROXY-REFINEMENT sub-class refinements (i)-(iii) operate at the UV-regulator axis of the substrate-physics layer (Cell I-II algebra-INVARIANT spectrum-only functional family); route (iv) operational-machinery-alignment operates at the state-side specification axis (Cell IV algebra-DEPENDENT state-pair functional family). The 4-corner orthogonality K=3 MANDATORY at `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` forbids conflating these axes under a single sub-class. Option (a) preserves the orthogonality at the sub-class taxonomy layer; Option (b) collapses it.

**Q-C3.2 answer — In-session rule-file extension at W-5 close is admissible per the methodology-wave-allowlist.md pattern; S91+ mack-cosmic-bridge sole-writer re-landing is also acceptable**

Either pathway works structurally; my preference is in-session rule-file extension at W-5 close per the precedent at `methodology-wave-allowlist.md` for prior W0a-1, W0a-3, W0a-5 landings (per the calibration corpus at lines 144-149 of `.claude/rules/methodology-wave-allowlist.md`). The W-5 close lands the rule-file extension to `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` adding the new sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` with the refinement-pathway type "operational-machinery-alignment" (route iv at the §VII.AV registry text refinement-pathway table per CONVERGENCE C4).

If in-session rule-file extension is not preferred by the orchestrator (e.g., to preserve the no-technical-debt rule's MANDATORY status promotion threshold per `feedback_rules-compensate-missing-structure.md` K-counter threshold), the alternative is S91+ mack-cosmic-bridge sole-writer re-landing per `feedback_mack-bridge-role.md`. Both pathways achieve the same structural outcome.

The TRIPLE-instance K=1 SUGGESTION baseline (§VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION + §VII.AV OPERATIONAL-ALIGNMENT) sharing the S90 W-5 close landing event is structurally permissible at K=1 SUGGESTION level per the dual-instance precedent established at S90 W1-14 (per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` lines 124-127). The K-counter advancement from K=1 → K=2 → K=3 MANDATORY proceeds via future-session distinct landings at S91+ (CF-70 PASS for PROXY-REFINEMENT advancement; CF-71 PASS for OPERATIONAL-ALIGNMENT advancement; some future independent instance for further advancement).

**Q-C3.3 answer — Under hybrid verdict (d), I endorse the §VII.AV registry text refinement-pathway table extension at lines 17944-17948 as canonical landing at S91+ via mack-cosmic-bridge sole-writer**

YES, endorsed. The connes-proposed extension at workshop lines 967-981 (route iv operational-machinery-alignment + route v V4 substrate-physics adjudicator + explicit "Layer" column with substrate-physics / operational-machinery / dual-anchor-joint-hypersurface tags) IS the canonical landing form at S91+ via mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. The explicit "Layer" column satisfies the cross-pillar-bridge-anatomy.md Element 3 binding discipline (canonical-import-binding vs substrate-natural-binding distinction at S88 W7b-82 K=1 SUGGESTION + S90 W7-4 CF-57 axis γ sharpening).

The combined registry-text extension PLUS the rule-file sub-class extension (per Q-C3.2 answer) PLUS the K-counter advancement structure (per Q-C3.2 + Q-C3.4 answers) IS the complete canonical landing structure under verdict (d).

**Q-C3.4 answer (most consequential) — Route (iv) operational-machinery-alignment is structurally DISTINCT from PROXY-REFINEMENT (Option a per DISSENT D1); CF-71 PASS at S91+ does NOT count toward PROXY-REFINEMENT K=1 → K=2 advancement; CF-71 PASS at S91+ instead establishes the K=1 SUGGESTION baseline for the NEW OPERATIONAL-ALIGNMENT sub-class**

(ii) Route (iv) is structurally distinct new sub-class under Option (a) per DISSENT D1. K-counter advancement structure:

- **PROXY-REFINEMENT K-counter**: K=1 SUGGESTION baseline at S90 W1-14 dual-instance landing event (§VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION). Advances to K=2 contingent on CF-70 PASS at S91+ (CF-70 IS the substrate-physics UV-regulator-axis Layer 1 refinement, within PROXY-REFINEMENT scope). Advances to K=3 MANDATORY at distinct future-session landing.
- **OPERATIONAL-ALIGNMENT K-counter (NEW under Option a)**: K=1 SUGGESTION baseline established at this S90 W-5 close landing event (the new sub-class is FIRST-LANDED at W-5; the §VII.AV instance is the first calibration corpus entry). Advances to K=2 contingent on CF-71 PASS at S91+ (CF-71 IS the operational-machinery state-side specification axis Layer 2 refinement, within OPERATIONAL-ALIGNMENT scope by construction). Advances to K=3 MANDATORY at distinct future-session landing.
- **FIRST-EXTRACTION K-counter**: K=1 SUGGESTION baseline at S90 W1-14 dual-instance landing event. Advances per existing CF-65 NEGATIVE-CALIBRATION + future-session positive instances.

Under this structure, CF-71 PASS at S91+ advances OPERATIONAL-ALIGNMENT K=1 → K=2 but does NOT advance PROXY-REFINEMENT K-counter. CF-70 PASS at S91+ advances PROXY-REFINEMENT K=1 → K=2 but does NOT advance OPERATIONAL-ALIGNMENT K-counter. The two K-counters are STRUCTURALLY INDEPENDENT — each tracks its own axis of the §VII.AV refinement-pathway space.

The W-5 cross-axis joint-win at K=4 → K=5 advancement on the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter IS structurally robust under EITHER CF-70 PASS or CF-71 PASS (or both); the cross-axis K-counter advancement is at a higher structural layer (the workshop-verdict-pattern layer) than the sub-class K-counters (the registry-content layer). Per EMERGENCE EV1 the hybrid verdict (d) IS itself a structural theorem at the layer-functor F decomposition cleanness condition — independent of which axis advances its own sub-class K-counter at S91+.

---

**Two forward questions for connes R2-B FINAL**

After the substantive convergence on hybrid verdict (d) + Option γ wave-together + 4-axis orthogonal refinement-pathway space at EV3, two structural questions remain that test specific NCG-axiomatic commitments emerging from R2.

**Q-V-R2-1 — Hochschild-Künneth Morita-invariance applied to CF-71 PASS: does the K_canonical re-derivation from the substrate's BdG energy gap at τ_fold preserve the Level-1 cocycle ratio identity at L_max=12 INDEPENDENTLY of the resulting P_BdG implementation alignment?**

Per CONVERGENCE C2 + Q-C1.1 answer, the W3 A.14 cocycle ratio 7.3249743784 IS Morita-invariant under Hochschild-Künneth `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` (your Re:V2 lines 426-432). This Morita-invariance ASSERTS that the cocycle ratio at L_max=12 IS preserved under ANY P_BdG implementation choice — including the K_canonical-re-derived implementation under CF-71.

CF-71's structural role is to re-derive K_canonical from the substrate-IS BdG energy gap at τ_fold (per W8 WP lines 1660-1665), yielding a specific P_BdG implementation that aligns the FULL-BdG L_max=12 anchor with the §W5-2 canonical −7.046336. The K_canonical-re-derived P_BdG implementation IS expected to satisfy Morita-invariance at Level-1 by construction.

Question: under CF-71 PASS, IS the cocycle ratio 7.3249743784 at L_max=12 trivially preserved (Morita-invariance argument), OR is the K_canonical re-derivation structurally distinct enough to introduce a corrigendum to the Level-1 cocycle ratio identity? Specifically: does the K_canonical re-derivation enter the Hochschild differential on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` only at the boundary terms (Morita-preserving) OR does it modify the interior cohomology class structure (Morita-breaking, requiring corrigendum)? Cite the cyclic-cohomology structural argument that pins which option holds.

If CF-71 PASS preserves the cocycle ratio at Level-1 trivially via Morita-invariance, the §VII.AV refinement-pathway 4-axis orthogonality at EMERGENCE EV3 is structurally clean: CF-71 operates strictly at Level-3 with Morita-invariance preservation at Level-1, while CF-77 operates strictly at Level-1 with structural-degeneration test at L_max ≤ 10. If CF-71 PASS does NOT trivially preserve the cocycle ratio, there is a structurally coupled relationship between CF-71 and CF-77 that should be made explicit in the registry-text refinement-pathway table extension.

**Q-V-R2-2 — Cross-axis joint-win pattern K=4 → K=5 MANDATORY promotion: under verdict (d), do you concur that the K-counter advancement structure at the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter is itself a layer-functor F image at the workshop-verdict-pattern layer, structurally distinct from the registry-content sub-class K-counters (PROXY-REFINEMENT, OPERATIONAL-ALIGNMENT, FIRST-EXTRACTION)?**

Per EMERGENCE EV1 the hybrid verdict (d) IS a structural theorem at the layer-functor F decomposition cleanness condition. The W-5 close is structurally a JOINT theorem candidate under `joint-theorem-promotion.md` 4-stage promotion pathway: Stage-0 workshop-internal candidate (this workshop's R3 closure); Stage-1 registry-as-candidate (S91+ registry landing as STAGE-1-CANDIDATE); Stage-2 two-agent parallel cross-check (S91+ or later independent-verify dispatch); Stage-3 permanent registration (STAGE-3-PERMANENT promotion).

Per `joint-theorem-promotion.md §"Stage 2 — Two-Agent Parallel Cross-Check"` axis-distinctness clause (item 1) and downstream-inheritance-reach exclusion clause (item 2), the Stage-2 cross-reviewers for the W-5 joint theorem at S91+ MUST be on different axes from the W-5 authoring (volovik = transit-dynamics / superfluid-universe axis; connes = NCG-axiomatic / spectral-functional axis). The natural Stage-2 cross-reviewer assignments would be: a different transit-dynamics-axis or substrate-physics-axis reviewer (lizzi-spectral-functional-theorist on the spectral-side; gen-physicist on the general-physics-side; transit-dynamics-aether-mechanic on the transit-side) operating WITHOUT prior workshop context per the procedural-floor independence guarantee.

Question: do you concur that the W-5 joint theorem (the hybrid verdict (d) as structural theorem at the layer-functor F decomposition cleanness condition) is structurally analogous to the §VII.AH STAGE-3-PERMANENT promotion event (S90 W2 CF-20 LANDED, 2026-05-13; per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` K=3 MANDATORY)? Specifically: does the W-5 hybrid verdict (d) satisfy the substrate-input-orthogonality predicate at ≥ 1 observable for Stage-2 verification with N ≥ 2 observables — where the N ≥ 2 observables are the 4 orthogonal-axis refinement gates (CF-70 + CF-71 + V4 + CF-77) at S91+? The substrate-input-orthogonality structural ceiling at the joint-theorem promotion layer would be satisfied if each Stage-2 cross-reviewer loads exactly one of the 4 orthogonal-axis gates' data files (not shared substrate-input data files across both cross-reviewers).

If concurred, the W-5 close should pre-register the Stage-1 candidate landing structure at S91+ via mack-cosmic-bridge sole-writer alongside the registry-text refinement-pathway table extension; the Stage-2 cross-check dispatch at S92+ should pre-register the substrate-input-orthogonality assignment per the joint-theorem-promotion.md §"Stage 2" procedural floor.

---

## Round 2 — connes: Cross-Synthesis

### CONVERGENCE

I accept volovik's R2 CONVERGENCE C1-C4 and DISSENT D1 in full. The state-after-R2-A is structurally closed at the hybrid verdict (d) framing with Option (a) NEW sub-class taxonomy at the rule-file layer. The cross-axis HYBRID convergence at five substantive positions below is reading-shift on my part, not parallel-agreement.

**CONVERGENCE CC1 — HYBRID verdict (d) cross-axis JOINT-WIN at layer-functor F decomposition (V1+V2+V3+V5 wins L_max ≤ 10 substrate-IS phase boundary layer; Re:V2+C1+C2 wins L_max=12 P_BdG-implementation layer)**

I accept volovik's R2 CONVERGENCE C1-C4 (workshop lines 1067-1094) in full. The hybrid verdict (d) emerged at Re:V2 EMERGES lines 450-457 (Layer 1 substrate-IS Cooper-instability criterion wins for Reading A at L_max ≤ 10; Layer 2 P_BdG-implementation distinction wins for Reading B at L_max=12); volovik C1 (line 1070) accepted Reading A as JOINT-WIN substrate-axis × NCG-axiomatic-axis (two structurally distinct derivations producing the SAME Cooper-instability criterion K(0; L_max) ≥ 1/V_BCS — Volovik/Khodel-Shaginyan microscopic Hamiltonian axis V1 lines 55-67 + Connes-Moscovici §III.4 residue formula at substrate-distance-2 pole s=4 Re:V1 substitution chain lines 341-373); volovik C2 (line 1076) conceded V2 strong-form to the Hochschild-Künneth Morita-invariance argument I surfaced at Re:V1 MISSED block lines 392-396 + Re:V2 lines 426-432; volovik C3 (line 1084) endorsed Option γ wave-together dispatch (V4 first, then CF-70 + CF-71 parallel) per Re:V3 EMERGES lines 521-531; volovik C4 (line 1090) endorsed §VII.AV registry-text 4th refinement route extension at lines 17944-17948 (route iv operational-machinery-alignment + route v V4 substrate-physics adjudicator + explicit "Layer" column) per Re:V3 + C2 proposal lines 967-981.

The cross-axis JOINT-WIN at K=4 → K=5 MANDATORY promotion candidate per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold IS structurally licensed at this W-5 close. The layer-functor F decomposition cleanness condition per `epistemic-discipline.md §"Layer-Decomposition"` is satisfied at the substrate ↔ methodology ↔ audit layer triangle: substrate-axis Layer 1 + Layer 2 → methodology-axis CF-70 + CF-71 → audit-axis §VII.AV PROXY-REFINEMENT-PENDING tag + §VII.AV OPERATIONAL-ALIGNMENT-PENDING tag (NEW per DISSENT D1 Option (a)).

**CONVERGENCE CC2 — V2 strong-form CONCESSION (Q-C1.2 reframe): the L_max=12 anchor mismatch 1.428 IS Level-3 P_BdG-implementation distance, NOT substrate-IS regime separation at L_max=12**

I accept volovik's Q-C1.1 + Q-C1.2 answers at workshop lines 1191-1242 in full. The substitution chain volovik produced at Q-C1.1 (lines 1198-1238) is structurally clean: the Hochschild-Künneth Morita-invariance `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` (W-4 verdict) applies at the Level-1 cohomology-class identity layer; the BCS critical-coupling kernel K(0; L_max) at canonical V_BCS evaluated at the Δ_a → 0 probe is INDEPENDENT of the Δ_a tensor specification (scalar Δ collapses to zero; multi-branch B-tensor collapses to zero; all probes the SAME L_max-truncated D_K spectral kernel `{λ_a, m_a}`); the substrate phase boundary position invariance at L_max=10/11 follows as a structural property of the L_max-truncated D_K spectrum at canonical V_BCS, NOT of the P_BdG projector implementation choice.

volovik's honest concession at lines 1240-1242 ("at L_max=12 the substrate-IS observable admits TWO operational P_BdG-implementations distinguishable at Level-3 only") IS the structurally correct Reading B framing at L_max=12: the SAME Cell-IV substrate-IS observable (variance of Bogoliubov occupation at K_horizon per §VII.U.2 Corner II parse-tree closed form line 12961) is evaluated under two structurally distinct P_BdG = diag(|v_a|², |u_a|²) projector implementations at L_max=12; both implementations live on the SAME `M_2(ℂ) ⊂ A_K` sub-algebra image; both yield the SAME Hochschild cohomology class under Morita-invariance; both yield the SAME W3 A.14 cocycle ratio 7.3249743784 at Level-1; they differ ONLY at Level-3 numerical anchor by 1.428 M_KK² absolute. This is the structurally honest restatement of my Re:V2 position at workshop lines 410-422.

**CONVERGENCE CC3 — EV3 4-axis orthogonal refinement-pathway space (UV-regulator CF-70 × state-side CF-71 × Level-3 dual-anchor V4 × Hochschild-cohomology CF-77) is the canonical S91+ wave-together structure**

I accept volovik's EMERGENCE EV3 at workshop lines 1170-1183 as a structurally novel partition that neither V1-V6 nor Re:V1-Re:V6 produced alone. The 4-axis orthogonality maps cleanly to the cross-pillar-bridge-anatomy.md / regulator-pin-discipline.md / phononic-framing.md 4-axis orthogonality structure (UV-regulator axis × Level axis × Binding axis × MACHINERY-SCOPE axis at `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"`):

| Axis | Substrate content at §VII.AV | S91+ refinement gate | Layer-functor F image |
|:-----|:----------------------------|:---------------------|:----------------------|
| UV-regulator axis | unsubtracted gap-eqn kernel vs FULL CC PV at Λ_UV = M_KK | CF-70 | Layer 1 (Cell I-II algebra-INVARIANT) |
| State-side specification axis | scalar Δ vs multi-branch B-tensor P_BdG implementation | CF-71 | Layer 2 (Cell IV algebra-DEPENDENT) |
| Level-3 dual-anchor binding axis | canonical-import-binding L_emp_s52 vs substrate-natural-binding L_emp_FULL | V4 = `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST` | Level-3 dual-hypersurface (joint-hypersurface type iii) |
| Hochschild-cohomology axis | W3 A.14 cocycle ratio structurally defined vs degenerate | CF-77 = `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST` | Level-1 cohomology-class identity |

The 4-axis orthogonality satisfies the `.claude/rules/Investigating-Workshops.md §"is NOT" item 8` parallel-compute-wave classification structure (4 prerequisite conditions on structurally orthogonal axes, each with its own pre-registered PASS criterion, combining via logical AND at S91+ close). This is the canonical S91+ dispatch structure for §VII.AV's deferred-pending refinement.

**CONVERGENCE CC4 — CF-77 endorsement: `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST` IS the Hochschild-cohomology-layer cross-anchor of Reading A's substrate-IS phase boundary, INDEPENDENT of gap-equation operational machinery**

I accept volovik's Q-C2.1 + Q-C2.2 + Q-C2.3 answers at workshop lines 1246-1280 in full. Q-C2.1 (line 1248: "structurally degenerate. The BdG sub-algebra image `M_2(ℂ) ⊂ A_K` at L_max ≤ 10 trivial-Δ regime has K_0(M_2(ℂ))-trivial Hochschild homology structure when the gap = 0") IS the Hochschild-cohomology-side characterization I surfaced at Re:V1 MISSED block lines 392-396 sharpened to its strongest form: the cocycle ratio `‖φ_67‖/‖φ_88‖` evaluated on a trivial BdG sub-algebra at canonical (V_BCS, T_fold) probe is structurally a 0/0 indeterminate form per the inheritance-falsifier-protocol Class-A kernel-signature null prediction.

Q-C2.2 (line 1258) establishes the Hochschild-cohomology degeneration as OPERATIONAL-MACHINERY-INDEPENDENT: it does not depend on the scalar-Δ FULL-BdG gap-equation route, nor on the multi-branch s52 ED route (even with externally-imposed (B1, B2, B3) tensor at L_max ≤ 10), nor on the SCHEMATIC Casimir-bound proxy. This is the strongest cross-anchor for Reading A's substrate-IS phase boundary at the Level-1 cohomology-class identity layer.

Q-C2.3 (line 1268) endorses CF-77 pre-registration alongside CF-70 + CF-71 + V4 wave-together dispatch at S91+, with explicit gate-spec (Gate ID, Trigger, Wave classification, Effort ~0.8 wave-equiv, PASS/FAIL/INFO criteria at lines 1271-1278). I endorse the CF-77 pre-registration as a 4th structurally orthogonal axis of the §VII.AV refinement-pathway space.

**CONVERGENCE CC5 — DISSENT D1 + Q-C3.1 + Q-C3.4 ACCEPTED: Option (a) NEW sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` preserves 4-corner algebra-axis orthogonality at the sub-class taxonomy layer; CF-71 PASS at S91+ establishes the NEW K=1 SUGGESTION baseline for OPERATIONAL-ALIGNMENT, NOT advancing PROXY-REFINEMENT K-counter**

I CONCEDE my Q-C3.4 line 1045 preferred framing (route (iv) within PROXY-REFINEMENT scope under Option (b)). volovik's DISSENT D1 (lines 1102-1119) + Q-C3.1 answer (line 1284) substrate-axis argument is structurally cleaner: PROXY-REFINEMENT sub-class refinements (i)-(iii) operate at the UV-regulator axis of the substrate-physics layer (Cell I-II algebra-INVARIANT spectrum-only functional family); route (iv) operational-machinery-alignment (CF-71) operates at the state-side specification axis (Cell IV algebra-DEPENDENT state-pair functional family). The `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 clause (per S87 W-2 R3 close) FORBIDS conflating these axes under a single registry slot at the substrate-IS observable level — and equivalently FORBIDS conflating them under a single deferred-pending sub-class at the rule-file taxonomy layer. Option (b) extension would collapse the 4-corner orthogonality at the sub-class taxonomy layer; Option (a) preserves it by construction.

Under Option (a), the K-counter advancement structure at the deferred-pending intermediate verdict-class becomes:

- **PROXY-REFINEMENT K-counter** (UV-regulator axis; Cell I-II algebra-INVARIANT spectrum-only): K=1 SUGGESTION baseline at S90 W1-14 dual-instance landing (§VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION). Advances K=1 → K=2 contingent on CF-70 PASS at S91+ (CF-70 IS the substrate-physics UV-regulator-axis Layer 1 refinement, within PROXY-REFINEMENT scope by construction).
- **OPERATIONAL-ALIGNMENT K-counter** (state-side specification axis; Cell IV algebra-DEPENDENT state-pair; NEW under Option (a)): K=1 SUGGESTION baseline established at THIS S90 W-5 close landing event (§VII.AV OPERATIONAL-ALIGNMENT is the first calibration corpus entry). Advances K=1 → K=2 contingent on CF-71 PASS at S91+ (CF-71 IS the operational-machinery state-side specification axis Layer 2 refinement, within OPERATIONAL-ALIGNMENT scope by construction).
- **FIRST-EXTRACTION K-counter** (symbolic-only first extraction axis): K=1 SUGGESTION baseline at S90 W1-14 dual-instance landing. Existing CF-65 NEGATIVE-CALIBRATION + future-session positive instances govern its advancement.

The two K-counters (PROXY-REFINEMENT vs OPERATIONAL-ALIGNMENT) are STRUCTURALLY INDEPENDENT — each tracks its own algebra-axis orthogonality cell at the §VII.AV refinement-pathway space. This is the structurally cleanest taxonomy under verdict (d).

### DISSENT

No new dissent at the L_max=12 P_BdG-implementation reframe, the 4-axis orthogonality refinement-pathway space, the Option (a) NEW sub-class taxonomy, the CF-77 endorsement, or the cross-axis JOINT-WIN K=4 → K=5 MANDATORY promotion candidate. The cross-axis HYBRID convergence on verdict (d) is structurally closed at the layer-functor F decomposition cleanness condition.

One narrow methodological observation, recorded for forward enforcement clarity but NOT structurally contesting any volovik R2 position:

**Methodological observation MO1 — In-session rule-file extension at W-5 close (Q-C3.2 Option) requires methodology-wave-allowlist.md M4 gate-ID allowlist append, NOT direct rule-file edit**

volovik's Q-C3.2 answer at workshop lines 1289-1294 states a structurally clean preference for in-session rule-file extension at W-5 close per the methodology-wave-allowlist.md precedent (W0a-1 / W0a-3 / W0a-5 / W11-meta-1/2/3 / etc.). This is correct in principle; my narrow methodological observation is that under `.claude/rules/wave-classification.md §M4` strict-conjunction requirement, in-session rule-file extension via the orchestrator-direct-write path requires the W-5 close gate-ID (a hypothetical `S90-W5-VII-AV-DEFERRED-PENDING-OPERATIONAL-ALIGNMENT-SUB-CLASS-EXTENSION`) to appear in `.claude/rules/methodology-wave-allowlist.md` allowlist BEFORE the rule-file edit fires. Per the recursion-attack-closure protocol at `methodology-wave-allowlist.md §"Edit discipline (recursion-attack closure)"` lines 26-42, this allowlist append is orchestrator-only-edit (subagents denied edit by harness convention).

The structurally clean path under verdict (d): the orchestrator handles the methodology-wave-allowlist.md allowlist append at W-5 close, the rule-file extension to `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` (adding the new sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` with refinement-pathway type "operational-machinery-alignment"), and the §VII.AV registry-text refinement-pathway table extension via mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. Alternatively, the S91+ mack-cosmic-bridge sole-writer re-landing pathway volovik mentions at line 1292 IS structurally permissible and may be cleaner since it co-locates the rule-file extension and the registry-text extension at a single S91+ landing event.

This is methodological book-keeping, NOT structural dissent. Either pathway (in-session at W-5 close OR S91+ mack landing) reaches the same structural outcome. I record it here so the W-5 carry-forward queue handles the path-of-least-resistance decision explicitly.

### EMERGENCE

Three substantive cross-domain insights emerge from R2-A volovik's responses that neither V1-V6 nor Re:V1-Re:V6 nor R2-A CONVERGENCE C1-C4 + DISSENT D1 + EMERGENCE EV1-EV3 produced alone. Each substantively answers one of volovik's Q-V-R2 forward questions OR identifies a structurally novel implication.

**EMERGENCE EC1 — Q-V-R2-1 answer: CF-71 PASS preserves the W3 A.14 cocycle ratio at Level-1 TRIVIALLY via Morita-invariance; CF-71 and CF-77 are structurally DECOUPLED at the registry-text refinement-pathway table extension layer**

volovik's Q-V-R2-1 at workshop lines 1320-1328 asks whether under CF-71 PASS the K_canonical re-derivation preserves the Level-1 cocycle ratio identity 7.3249743784 INDEPENDENTLY of the resulting P_BdG implementation alignment, OR whether CF-71 PASS introduces a corrigendum to the Level-1 cocycle ratio identity requiring structurally coupled treatment with CF-77.

**NCG-axiomatic answer: CF-71 PASS preserves the W3 A.14 cocycle ratio at Level-1 TRIVIALLY via Hochschild-Künneth Morita-invariance. CF-71 operates strictly at Level-3 (the K-window log-derivative numerical anchor at L_max=12) and inherits Morita-invariance at Level-1 by construction; CF-77 operates strictly at Level-1 (the cocycle ratio structural-definedness probe at L_max ≤ 10) INDEPENDENTLY of CF-71.**

Substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"`:

```
Step 1 (Definitions):
  HH^n(A_F ⊗ M_2(ℂ)) ≅ HH^n(A_F)         [Hochschild-Künneth Morita-invariance,
                                            W-4 verdict; cohomology class invariant
                                            under tensoring with M_n(ℂ)]
  P_BdG^{K_canonical}(τ_fold) := diag(|v_a|², |u_a|²)
                                           [Bogoliubov projector under CF-71 PASS;
                                            K_canonical re-derived from substrate-IS
                                            BdG energy gap at τ_fold per W8 WP lines 1660-1665]
  φ_67, φ_88 ∈ HH^*(A_F)                   [Hochschild cocycle classes on parent A_F;
                                            substrate canonical ‖φ_67‖/‖φ_88‖ = 7.324992]
  ι_*: HH^*(A_F) → HH^*(A_F ⊗ M_2(ℂ))     [Morita-invariance push-forward; structural
                                            isomorphism by Künneth theorem]

Step 2 (Substitution):
  Under Morita-invariance, the cocycle ratio at L_max=12 evaluated on
  HH^*(A_F ⊗ M_2(ℂ)) IS the push-forward image of the parent A_F cocycle ratio:
       ‖ι_*φ_67‖ / ‖ι_*φ_88‖ = ‖φ_67‖ / ‖φ_88‖ = 7.324992
  The cocycle ratio at Level-1 is INVARIANT under the Morita push-forward by
  construction of the Hochschild-Künneth isomorphism.

Step 3 (Simplification):
  The K_canonical re-derivation under CF-71 enters the construction of P_BdG^{K_canonical}
  at the operator-trace evaluation layer: Tr_{M_2(ℂ)}(P_BdG^{K_canonical} · D_K^{-2s}).
  P_BdG^{K_canonical} is an element of the operator algebra acting on the BdG sub-algebra
  Hilbert space; it is NOT an element of the Hochschild differential / cyclic
  cohomology structure on A_F ⊗ M_2(ℂ).

Step 4 (Canonical form):
  The cyclic cohomology on A_F ⊗ M_2(ℂ) is determined by the algebra structure
  (the Hochschild differential acting on (A_F ⊗ M_2(ℂ))^⊗(n+1) modulo boundaries),
  NOT by the specific operator-trace evaluation P_BdG · D_K^{-2s}. Different P_BdG
  implementations produce different numerical traces (Level-3 anchor distinct)
  but inhabit the SAME cohomology class (Level-1 identity preserved).

Step 5 (Direction):
  CF-71 PASS preserves Level-1 cocycle ratio identity 7.324992 TRIVIALLY via Morita
  push-forward; CF-71 operates only at Level-3 anchor alignment; CF-77's Level-1
  Hochschild cohomology degeneration test at L_max ≤ 10 is STRUCTURALLY DECOUPLED
  from CF-71's Level-3 P_BdG alignment at L_max=12. Both gates operate at orthogonal
  axes of the §VII.AV refinement-pathway space per EMERGENCE EV3.
```

Cited cyclic-cohomology structural argument: the K_canonical re-derivation enters the operator-trace evaluation BOUNDARY (the specific element P_BdG^{K_canonical} of the operator algebra acting on the BdG sub-algebra) without modifying the Hochschild differential's INTERIOR cohomology class structure. Per Connes 1985 cyclic cohomology framework (Connes, "Noncommutative Differential Geometry," 1985, §III) + Loday "Cyclic Homology" 2nd ed. 1998 §4.1.2 Hochschild-Künneth theorem: the Morita push-forward `ι_*: HH^*(A_F) → HH^*(A_F ⊗ M_n(ℂ))` is a structural isomorphism on cohomology classes regardless of which inner products / operator-traces are subsequently used to numerically evaluate cocycle norms. CF-71's K_canonical re-derivation modifies the operator-trace evaluation; it does NOT modify the Hochschild cohomology structure.

**Structural consequence for the §VII.AV registry-text refinement-pathway table extension**: CF-71 PASS at S91+ does NOT require structurally coupled treatment with CF-77 PASS at S91+. The two gates can be dispatched in parallel with INDEPENDENT verdicts. The §VII.AV refinement-pathway table extension at registry lines 17944-17948 lists CF-71 (route iv operational-machinery-alignment, Layer 2) and CF-77 (route vi Hochschild-cohomology cross-anchor, Layer 1) as STRUCTURALLY INDEPENDENT axes of the §VII.AV refinement-pathway space — the 4-axis orthogonality of EMERGENCE EV3 is preserved.

**EMERGENCE EC2 — Q-V-R2-2 answer: the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter IS a layer-functor F image at the workshop-verdict-pattern layer, structurally DISTINCT from registry-content sub-class K-counters (PROXY-REFINEMENT, OPERATIONAL-ALIGNMENT, FIRST-EXTRACTION); the W-5 hybrid verdict (d) joint theorem is Stage-0 → Stage-1-CANDIDATE candidate per `joint-theorem-promotion.md` 4-stage pathway**

volovik's Q-V-R2-2 at workshop lines 1330-1338 asks whether the K-counter advancement structure at the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter is itself a layer-functor F image at the workshop-verdict-pattern layer, structurally distinct from the registry-content sub-class K-counters (PROXY-REFINEMENT, OPERATIONAL-ALIGNMENT, FIRST-EXTRACTION), AND whether the W-5 hybrid verdict (d) joint theorem satisfies the substrate-input-orthogonality predicate of `joint-theorem-promotion.md §"Stage 2"` per the S90 W2 §VII.AH STAGE-3-PERMANENT precedent.

**NCG-axiomatic answer: YES on both counts.**

**Part 1 — Layer-functor F image at the workshop-verdict-pattern layer**:

Per `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence: the substrate-IS axis (substrate IS the spectral triple at full operator-algebra resolution at canonical τ_fold) maps under F to the methodology-axis image (the workshop-verdict-pattern at the cross-axis JOINT-WIN structural-theorem layer). The CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter IS the Phi-correspondence weight-2 image of substrate-IS layer-decomposition cleanness; it lives at the methodology-floor Σ_2 stratum (wave-classification per `wave-classification.md`).

The registry-content sub-class K-counters (PROXY-REFINEMENT, OPERATIONAL-ALIGNMENT, FIRST-EXTRACTION) live at the audit-floor stratum (registry-text content). Per the Phi correspondence:

- `Phi(a_0) = Σ_1` (perimeter / cosmological term, weight-0; user-adjudication-only deliverable) — registry-text content lives at this stratum
- `Phi(a_2) = Σ_2` (Einstein-Hilbert kinematic skeleton, weight-2; wave-classification) — workshop-verdict-pattern lives at this stratum
- `Phi(a_4) = Σ_3` (Yang-Mills + Higgs quartic load-bearing, weight-4; mcp-pre-check hook) — gate-execution machinery lives at this stratum

The CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern at K=4 → K=5 MANDATORY promotion candidate IS at the methodology-floor Σ_2 stratum (workshop-verdict-pattern layer); the registry-content sub-class K-counters at PROXY-REFINEMENT / OPERATIONAL-ALIGNMENT / FIRST-EXTRACTION are at the audit-floor Σ_1 stratum. The two layers are STRUCTURALLY ORTHOGONAL per the layer-functor F decomposition cleanness condition.

Structural consequence: the W-5 cross-axis joint-win advances the workshop-verdict-pattern K-counter K=4 → K=5 INDEPENDENTLY of which sub-class K-counter (PROXY-REFINEMENT or OPERATIONAL-ALIGNMENT) advances at S91+ via CF-70 or CF-71 PASS. The cross-axis K-counter advancement is at a higher structural layer than the sub-class K-counter advancement — and the W-5 close IS the K=5 advancement event regardless of S91+ S91+ gate verdicts.

**Part 2 — Stage-0 → Stage-1-CANDIDATE joint theorem candidate per `joint-theorem-promotion.md` 4-stage pathway**:

YES. The W-5 hybrid verdict (d) IS a structurally novel JOINT theorem candidate at the workshop-verdict-pattern layer per the 4-stage promotion pathway:

- **Stage 0** (workshop-internal candidate): this workshop's R2-B FINAL closure (R2 CONVERGENCE CC1-CC5 + DISSENT D1 + EMERGENCE EC1-EC2 + Verdict table + Wrap-Up) — workshop-internal artifact at W-5 close.
- **Stage 1** (registry-as-candidate at S91+): mack-cosmic-bridge sole-writer landing of the W-5 cross-axis joint-win as a STAGE-1-CANDIDATE entry in `sessions/permanent-results-registry.md`. The candidate text would identify joint clauses (substrate-axis Reading A WINS at Layer 1 L_max ≤ 10; NCG-axiomatic axis Reading B WINS at Layer 2 L_max=12; HYBRID verdict d at workshop-verdict-pattern layer is structural theorem at layer-functor F decomposition).
- **Stage 2** (two-agent parallel cross-check at S92+): per `joint-theorem-promotion.md §"Stage 2"` axis-distinctness requirement, the Stage-2 cross-reviewers MUST be on different axes from volovik (transit-dynamics / superfluid-universe) and connes (NCG-axiomatic / spectral-functional). Candidate Stage-2 cross-reviewer assignments:
  - Axis A (spectral / NCG-axiomatic; NOT connes): lizzi-spectral-functional-theorist (spectral-functional axis distinct from connes's NCG-axiomatic axis; downstream-inheritance-reach exclusion check per S88 W-14 W4a-17 V.2 calibration corpus — verify lizzi's project memory does NOT inherit the workshop's reading-path through prior session synthesis).
  - Axis B (substrate / superfluid-universe; NOT volovik): transit-dynamics-aether-mechanic (transit-dynamics axis distinct from volovik's superfluid-universe axis; same downstream-inheritance-reach check).
- **Stage 3** (permanent registration at S93+): if Stage-2 PASS-AND at both axis reviewers, registry tag promotes from STAGE-1-CANDIDATE to STAGE-3-PERMANENT.

The substrate-input-orthogonality predicate (`joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY at K=3 per S90 W2 §VII.AH STAGE-3-PERMANENT promotion event 2026-05-13) IS satisfied at the W-5 Stage-2 verification if the 4 orthogonal-axis gates (CF-70 + CF-71 + V4 + CF-77) load distinct data files at S92+ Stage-2 cross-check, such that ≥ 1 observable has exactly ONE cross-reviewer loading its substrate-input. Per EMERGENCE EV3 the 4 axes ARE structurally orthogonal — CF-70 PV-regulated kernel data is distinct from CF-71 K_canonical-corrected K-window data is distinct from V4 multi-branch B-tensor sweep data is distinct from CF-77 cocycle-ratio L_max ≤ 10 truncation data. The substrate-input-orthogonality predicate is satisfiable at structural ceiling.

I concur with volovik's framing at workshop line 1336-1338: the W-5 close should pre-register the Stage-1 candidate landing structure at S91+ via mack-cosmic-bridge sole-writer alongside the registry-text refinement-pathway table extension; the Stage-2 cross-check dispatch at S92+ should pre-register the substrate-input-orthogonality assignment per the joint-theorem-promotion.md §"Stage 2" procedural floor.

**EMERGENCE EC3 — Cross-workshop K=5 MANDATORY promotion candidate watchpoint: the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern becomes a permanent workshop-verdict structural rule at K=5 advancement**

The W-1 H̃-DIVERGENCE-CHASE (S82 W-1; H̃ 2.38 OOM gap on same observable across transit-dynamics axis vs lizzi spectral-functional axis) + W-2 A_s LEDGER 3PI-vs-SLOT (S82 W-2; F_amp 122× discrepancy on slot-vs-3PI routes) + W-3 r-dual-pathway (S86; r-Path-H invariant + Path-C inheritance-forced inversion) + W-4 dual-symbol-convention (S88 W-4) + W-5 (this workshop; CF-61 BCS phase transition reading at hybrid verdict d) form a 5-instance corpus of the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern. Per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold (K=3 MANDATORY promotion), the cross-workshop K=5 MANDATORY promotion event at this W-5 close advances the pattern from K=4 SUGGESTION to K=5 MANDATORY status as a permanent workshop-verdict structural rule at the methodology-floor Σ_2 stratum.

The structurally novel content at K=5: the cross-axis JOINT-WIN pattern operates at the layer-functor F decomposition cleanness condition (per EMERGENCE EC2 Part 1); future workshops dispatched at the cross-axis adversarial-review topology MUST adopt the layer-decomposition framing as the structural verdict template (not the narrative-compromise framing of "both readings win some / both lose some"). The hybrid verdict (d) is NOT a compromise; it IS a structural theorem at the substrate-IS / methodology / audit layer triangle where the two readings inhabit structurally orthogonal sub-layers.

Forward enforcement: per `methodology-wave-allowlist.md §"Allowlist Rows"` table + the K=5 MANDATORY promotion event, future workshops with a cross-axis adversarial-review topology + a layer-decomposable structural object MUST adopt the layer-functor F-decomposition verdict template at the workshop-internal R3 closure. This is a methodology-rule extension at the Phi(a_2) = Σ_2 weight-2 wave-classification stratum; the rule-file extension lands via the orchestrator-direct-write path per `wave-classification.md §"Dispatch consequences"` with gate-ID appearing in `methodology-wave-allowlist.md` allowlist per recursion-attack-closure protocol.

The W-5 close IS the K=5 MANDATORY promotion event. This is structurally significant beyond the §VII.AV registry-content advancement: it advances the framework's METHODOLOGY at the workshop-verdict-pattern layer, establishing the cross-axis JOINT-WIN at layer-decomposition as the canonical resolution template for future cross-axis adversarial workshops.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | (a) Trivial-Δ solution interpretation (L_max ≤ 10) | V1, Re:V1, R2-A C1, R2-B CC1 | **Converged** | Reading A WINS at Layer 1: substrate-IS Cooper-instability criterion `K(0; L_max) ≥ 1/V_BCS` fails on the L_max-truncated D_K spectral kernel at canonical V_BCS = 2.447e-7 M_KK^{-1}; cross-axis JOINT-WIN from Volovik/Khodel-Shaginyan microscopic flat-band condensation axis (V1 lines 55-67) AND Connes-Moscovici §III.4 residue-formula axis at substrate-distance-2 pole s=4 (Re:V1 lines 341-373) producing identical structural content — the 4.3% missing UV weight in sectors (p+q) ∈ {11, 12} mediates the threshold crossing on the substrate's Level-1 single-τ-slice spectral content. |
| 2 | (b) L_max=12 anchor mismatch interpretation (1.428 absolute) | V2, Re:V2, R2-A C2, R2-B CC2 | **Converged** | Reading B WINS at Layer 2: 1.428 anchor mismatch IS Level-3 P_BdG-projector-implementation distance (scalar-Δ uniform `|v_a|² = (1 − ε_a/E_a)/2` vs multi-branch s52 per-mode `|v_a^{(B_n)}|²`), NOT substrate-IS regime separation; volovik V2 strong-form claim (lines 95-99 "two inequivalent Bogoliubov-amplitude tensors as substrate-IS observables") CONCEDED via R2-A C2 + Q-C1.1+Q-C1.2 answers under Hochschild-Künneth Morita-invariance `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` (W-4 verdict) — both implementations live on the same Hochschild cohomology class at Level-1; differ only at Level-3 numerical anchor. |
| 3 | (c) §VII.AV refinement pathway licensing (CF-70 vs CF-71) | V3, Re:V3, R2-A C3+DISSENT D1, R2-B CC3+CC5 | **Emerged** | 4-axis orthogonal refinement-pathway space (EMERGENCE EV3): CF-70 at UV-regulator axis (Layer 1; PROXY-REFINEMENT sub-class Cell I-II algebra-INVARIANT) + CF-71 at state-side specification axis (Layer 2; NEW OPERATIONAL-ALIGNMENT sub-class Cell IV algebra-DEPENDENT per DISSENT D1 Option (a)) + V4 at Level-3 dual-anchor binding axis (joint-hypersurface type iii) + CF-77 at Hochschild-cohomology axis (Level-1 cocycle-ratio degeneration test). Sub-class taxonomy preserves 4-corner algebra-axis orthogonality at K=3 MANDATORY clause per `cross-pillar-bridge-anatomy.md`. |
| 4 | (d) S91+ discriminator gate spec (V4 `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST`) | V4, Re:V4, R2-A C3, R2-B CC3 | **Converged** | V4 IS the canonical substrate-physics adjudicator at the L_max=12 dual-anchor joint-hypersurface layer (Element 3 fiducial-anchor binding type iii per S88 W-15 V.7 + S90 W7-4 CF-57 axis γ); convention tag carries `-JOINT-HYPERSURFACE-DUAL-ANCHOR L_max=12` suffix; PASS/FAIL/INFO pre-registration is structurally sound (the configuration sweep over 8000+ refined (B1, B2, B3) configurations is empirically decidable; neither reading can pre-empt verdict at NCG-axiomatic layer without empirical sweep). |
| 5 | (e) Substrate framing Level-1 vs Level-2 (single-τ-slice MANDATORY tag) | V5, Re:V5, R2-A (implicit) | **Converged** | §VII.AV registry text line 17918 Level-1 single-τ-slice MANDATORY tag at τ_fold = 0.19 PRESERVED under hybrid verdict (d). BOTH readings predict BCS phase boundary at L_max=10/11 PERSISTS under small τ-deformations (Reading A's Level-1 prediction; Reading B accepts same prediction per Re:V5 lines 626-634); CF-69 τ-extension is structurally about §VII.AU FWD-C1 observable family, NOT §VII.AV (Re:V5 CF-69 SCOPE CLARIFICATION lines 645-649); a separate §VII.AV τ-extension gate (CF-75 candidate) would test the phase boundary persistence directly. |
| 6 | Cross-cutting observations (IS-not-IN framing + K-counter advancement + cross-axis JOINT-WIN pattern) | V6, Re:V6, R2-A EMERGENCE EV1-EV3, R2-B EMERGENCE EC1-EC3 | **Emerged** | (i) CF-61 FAIL is substrate-IS-faithful information at Layer 1 (the FULL-BdG gap-equation machinery FAITHFULLY REPORTS the substrate-IS Cooper-instability criterion failure on the truncated spectral kernel; the §W5-3 Casimir-bound SCHEMATIC proxy is the operational artifact, NOT the FULL). (ii) Multi-K-counter advancement event: cross-axis JOINT-WIN K=4 → K=5 MANDATORY at workshop-verdict-pattern layer (Σ_2 stratum) + PROXY-REFINEMENT K=1 baseline (CF-70 advancement at S91+) + NEW OPERATIONAL-ALIGNMENT K=1 baseline (CF-71 advancement at S91+) + Level-2-binding K-counter + Binding-axis K-counter potential advancement. (iii) hybrid verdict (d) IS a structural theorem at layer-functor F decomposition cleanness (EMERGENCE EV1 + EC2) — Stage-0 → Stage-1-CANDIDATE candidate per `joint-theorem-promotion.md` 4-stage pathway; Stage-2 cross-reviewers (lizzi spectral-side; transit-dynamics-aether-mechanic substrate-side) pre-registered for S92+. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

**Final structural verdict** (one of four pre-registered):

- **(a) Reading A canonical** — Casimir-bound STRUCTURALLY CLOSED; CF-70 prioritized; CF-71 deferred.
- **(b) Reading B canonical** — operational alignment via CF-71; Casimir-bound admissible IF alignment succeeds; CF-70 deferred.
- **(c) Both structurally distinct, refinement pathway space carries both** — CF-70 + CF-71 independent; pre-registered S91+ discriminator-gate fires first.
- **(d) Hybrid: substrate phase boundary AT operational-machinery joint layer** — both partially-correct; CF-70 + CF-71 wave-together with discriminator-gate first.

**SELECTED: (d) Hybrid — substrate phase boundary AT operational-machinery joint layer**

Cross-axis HYBRID convergence per R2-A CONVERGENCE C1-C4 (lines 1067-1094) + R2-B CONVERGENCE CC1-CC5. Layer 1 (L_max ≤ 10 phase boundary): Reading A WINS as substrate-IS Cooper-instability criterion failure on the truncated D_K spectral kernel at canonical V_BCS, with cross-axis confirmation from Volovik/Khodel-Shaginyan microscopic Hamiltonian axis AND Connes-Moscovici §III.4 residue-formula axis. Layer 2 (L_max=12 anchor mismatch): Reading B WINS as Level-3 P_BdG-projector-implementation distance, NOT substrate-IS regime separation, under Hochschild-Künneth Morita-invariance `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)`. The hybrid verdict IS a structural theorem at the layer-functor F decomposition cleanness condition per `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence (EMERGENCE EV1 + EC2). Forward dispatch: Option γ wave-together at S91+ with V4 discriminator gate firing FIRST, then CF-70 + CF-71 + CF-77 in parallel (4-axis orthogonal refinement-pathway space per EMERGENCE EV3); §VII.AV registry-text refinement-pathway table extension at registry lines 17944-17948 (routes iv operational-machinery-alignment + v V4 substrate-physics adjudicator + vi Hochschild-cohomology cross-anchor + explicit Layer column) lands at S91+ via mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; NEW deferred-pending sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` per DISSENT D1 Option (a) preserves 4-corner algebra-axis orthogonality. Cross-workshop K=4 → K=5 MANDATORY promotion candidate at the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter at the workshop-verdict-pattern layer (Σ_2 stratum).

## Remaining Open Questions

1. **CF-77 `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST`** (Hochschild-cohomology degeneration cross-anchor at Level-1 layer; per R2-A Q-C2.3 answer lines 1268-1280 + R2-B CONVERGENCE CC4) — pre-registered for S91+ wave-together dispatch. PASS predicate: at L_max ∈ {6..10}, cocycle ratio `‖φ_67‖/‖φ_88‖` returns STRUCTURALLY DEGENERATE (0/0 indeterminate or |ratio − 7.3249743784| > 1.0 across regulators {ζ, PV, Mellin, cutoff}) confirming Reading A's substrate-IS phase boundary at Hochschild-cohomology layer INDEPENDENT of gap-equation operational machinery.

2. **CF-70 `S91-VII-AV-FULL-CC-MULTIPLIERS-REFINEMENT`** (UV-regulator refinement at Layer 1; PROXY-REFINEMENT sub-class) — pre-registered for S91+ wave-together dispatch. PASS predicate: `α ∈ [2.5, 3.5] AND R² ≥ 0.95 AND L_max=12 anchor bit-match < 1e-9 under FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers` (W8 WP CF-70 spec line 1657); advances PROXY-REFINEMENT K=1 → K=2 on PASS.

3. **CF-71 `S91-VII-AV-K_CANONICAL-PIN-UNIQUENESS`** (state-side operational-alignment at Layer 2; NEW OPERATIONAL-ALIGNMENT sub-class per DISSENT D1) — pre-registered for S91+ wave-together dispatch. PASS predicate: `K_canonical derivation uniquely determined by substrate's BdG energy gap at τ_fold AND |L_emp(L_max=12)_corrected − (−7.046336474406761)| < 1e-9` (W8 WP CF-71 spec lines 1660-1665); advances NEW OPERATIONAL-ALIGNMENT K=1 → K=2 on PASS.

4. **V4 `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST`** (Level-3 dual-anchor discriminator at joint-hypersurface type iii; convention `-JOINT-HYPERSURFACE-DUAL-ANCHOR L_max=12`) — pre-registered for S91+ wave-together dispatch FIRST per Re:V3 Option γ flowchart. PASS/FAIL/INFO criteria per V4 lines 187-218 (∃ (B1, B2, B3) configuration in 8000+ refined sweep satisfying BOTH alignment criteria at < 1e-3 relative tolerance).

5. **§VII.AV registry-text 4th refinement route extension** (registry lines 17944-17948; route iv operational-machinery-alignment + route v V4 substrate-physics adjudicator + route vi Hochschild-cohomology cross-anchor + explicit Layer column) — pre-registered for S91+ mack-cosmic-bridge sole-writer landing per `feedback_mack-bridge-role.md`.

6. **NEW deferred-pending sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT`** (per DISSENT D1 Option (a)) — rule-file extension at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` per Q-C3.2 answer lines 1289-1294. Either in-session at W-5 close via orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"` + `methodology-wave-allowlist.md` allowlist append (orchestrator-only-edit per recursion-attack-closure protocol) OR S91+ mack-cosmic-bridge sole-writer re-landing.

7. **Cross-workshop K=5 MANDATORY promotion watchpoint** (CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern at Σ_2 stratum; W-1 + W-2 + W-3 + W-4 + W-5 corpus per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold) — at W-5 close the K-counter advances K=4 → K=5; MANDATORY promotion event makes the cross-axis JOINT-WIN at layer-decomposition the canonical resolution template for future cross-axis adversarial workshops per EMERGENCE EC3.

8. **Joint theorem 4-stage promotion pathway** (per `joint-theorem-promotion.md`) — W-5 R2-B FINAL closure IS Stage-0 workshop-internal candidate. Stage-1 registry-as-candidate at S91+ via mack-cosmic-bridge sole-writer (registry tag `STAGE-1-CANDIDATE`). Stage-2 two-agent parallel cross-check at S92+ with substrate-input-orthogonality predicate satisfied at structural ceiling (4 orthogonal-axis gates supply distinct substrate-input data files); candidate Stage-2 cross-reviewers: lizzi-spectral-functional-theorist (spectral-side) + transit-dynamics-aether-mechanic (substrate-side) per axis-distinctness + downstream-inheritance-reach exclusion. Stage-3 STAGE-3-PERMANENT promotion at S93+ contingent on Stage-2 PASS-AND.

## Wrap-Up — Workshop Impact Summary

### What Changed

1. **Cross-axis HYBRID convergence on verdict (d) at layer-functor F decomposition** — the L_max=10/11 BCS phase boundary (Layer 1 substrate-IS Cooper-instability criterion failure on truncated D_K spectral kernel at canonical V_BCS) and the L_max=12 anchor mismatch 1.428 (Layer 2 Level-3 P_BdG-projector-implementation distance under Hochschild-Künneth Morita-invariance) are STRUCTURALLY ORTHOGONAL sub-layers of the CF-61 evidence chain; both readings inhabit structurally distinct sub-layers under F; verdict (d) IS a structural theorem at the substrate ↔ methodology ↔ audit layer triangle per `epistemic-discipline.md §"Layer-Decomposition"`. volovik R2-A CONVERGENCE C1-C4 + connes R2-B CONVERGENCE CC1-CC5 jointly close the substrate-axis × NCG-axiomatic-axis cross-axis JOINT-WIN.

2. **§VII.AV registry-text refinement-pathway 4-route extension at registry lines 17944-17948 (routes iv + v + vi + explicit Layer column)** — adds route (iv) operational-machinery-alignment (CF-71; Layer 2 Cell IV algebra-DEPENDENT state-side specification) + route (v) V4 substrate-physics adjudicator (Level-3 dual-anchor joint-hypersurface type iii per S88 W-15 V.7 + S90 W7-4 CF-57 axis γ) + route (vi) Hochschild-cohomology cross-anchor (CF-77; Level-1 cocycle-ratio degeneration test at L_max ≤ 10) + explicit "Layer" column making layer-functor F decomposition cleanness condition visible at registry-text layer; canonical mack-cosmic-bridge sole-writer landing at S91+.

3. **Cross-workshop K=4 → K=5 MANDATORY promotion candidate at the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter (Σ_2 stratum)** — W-1 H̃-DIVERGENCE-CHASE + W-2 A_s LEDGER 3PI-vs-SLOT + W-3 r-dual-pathway + W-4 dual-symbol-convention + W-5 (this workshop) form a 5-instance corpus advancing the cross-axis JOINT-WIN structural-theorem pattern from K=4 SUGGESTION to K=5 MANDATORY at the workshop-verdict-pattern layer (Phi(a_2) = Σ_2 wave-classification stratum per `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence). Structurally novel at K=5: future cross-axis adversarial workshops MUST adopt the layer-decomposition verdict template (NOT narrative-compromise framing).

### What Holds

1. **Substrate-IS phase boundary at L_max ≤ 10 (Reading A canonical at Layer 1)** — the BCS gap-equation kernel sum `K(0; L_max) = Σ_a^{L_max} m_a · tanh(λ_a/(2T_fold))/(2λ_a)` at canonical V_BCS = 2.447e-7 M_KK^{-1} fails to cross the critical-coupling threshold 1/V_BCS at L_max ∈ {6..10} on the L_max-truncated D_K spectral kernel; 4.3% missing UV weight in sectors (p+q) ∈ {11, 12} mediates the L_max=10 → 11 transition. Both substrate-axis (Volovik/Khodel-Shaginyan microscopic flat-band condensation framework) AND NCG-axiomatic axis (Connes-Moscovici §III.4 residue formula at substrate-distance-2 pole s=4) produce identical structural content. Level-1 single-τ-slice substrate-IS at τ_fold = 0.19 per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` MANDATORY-K=2 since S88 W-7 V.4; §VII.AV registry-text Level-1 single-τ-slice MANDATORY tag at line 17918 PRESERVED.

2. **Hochschild-Künneth Morita-invariance `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` (W-4 verdict)** — the BdG sub-algebra `M_2(ℂ) ⊂ A_K` Hochschild cohomology IS Morita-equivalent to the parent A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) Hochschild cohomology INDEPENDENT of P_BdG projector implementation choice (scalar Δ vs multi-branch B-tensor). The W3 A.14 regulator-INVARIANT cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.3249743784` (substrate canonical 7.324992 per agent memory Permanent Theorems) IS preserved at Level-1 under ANY operational P_BdG implementation at L_max ≥ 11; degenerates structurally at L_max ≤ 10 trivial-Δ regime per CF-77 prediction (Reading A cross-anchor at Hochschild-cohomology layer).

3. **§VII.AV Level-1 single-τ-slice substrate-IS MANDATORY-K=2 at registry line 17918** — co-signed by volovik per CF-63 §"Provenance" line 17895; PRESERVED under hybrid verdict (d). The substrate IS the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at single-τ-slice τ_fold = 0.19 at substrate-distance-2 pole s=4; the laboratory IN is the Pillar V 3He-B BdG-sector continuum measurement under the HKR `L_max → ∞` bridge map per `phononic-framing.md §"IS Space, Not IN Space"` direction-of-explanation.

### What Breaks or Strains

1. **CF-77 Hochschild-cohomology degeneration test PENDING S91+ dispatch** — pre-registered as Reading A's strongest cross-anchor at the Level-1 cohomology-class identity layer INDEPENDENT of gap-equation operational machinery. Until S91+ verdict, the cocycle ratio degeneration prediction at L_max ∈ {6..10} is structurally CONJECTURAL (NCG-axiomatically sound per Q-C2.1 + Q-C2.2 answers lines 1248-1266, but empirically unverified). PASS confirms Reading A at the Hochschild-cohomology layer; FAIL would surface a Level-2 moduli-deformation-type observation on the L_max axis requiring further structural analysis.

2. **NEW deferred-pending sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` admissibility taxonomy** — per DISSENT D1 Option (a) the rule-file extension at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` preserves 4-corner algebra-axis orthogonality at sub-class taxonomy layer (PROXY-REFINEMENT for Cell I-II algebra-INVARIANT UV-regulator-axis refinements; NEW OPERATIONAL-ALIGNMENT for Cell IV algebra-DEPENDENT state-side specification axis). The K-counter advancement structure (PROXY-REFINEMENT vs OPERATIONAL-ALIGNMENT as STRUCTURALLY INDEPENDENT K-counters) STRAINS the W1-14 dual-instance K=1 SUGGESTION baseline (§VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION) by adding a TRIPLE-instance K=1 SUGGESTION baseline at W-5 close (§VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION + §VII.AV OPERATIONAL-ALIGNMENT). Pending mack-cosmic-bridge sole-writer landing at S91+ OR in-session orchestrator-direct-write at W-5 close via methodology-wave-allowlist.md allowlist append per Methodological Observation MO1.

3. **Cross-workshop K=5 MANDATORY promotion candidate K-counter advancing at workshop-verdict-pattern layer (Σ_2 stratum)** — the K=4 → K=5 advancement at this W-5 close is a structurally novel methodology-rule promotion event per `feedback_rules-compensate-missing-structure.md`. Forward enforcement requires future cross-axis adversarial workshops (W-6, W-7, ... at S91+) to adopt the layer-decomposition verdict template (NOT narrative-compromise framing) per the K=5 MANDATORY status. The promotion event itself is the first instance where the cross-axis JOINT-WIN at layer-functor F decomposition cleanness condition becomes a methodology-floor structural rule rather than an instance-specific verdict observation; future workshop dispatchers MUST verify layer-decomposability of the structural object at workshop-spec time.

### Carry-Forward Computations

1. **CF-S91-VII-AV-HOCHSCHILD-DEGENERATION-TEST** (per R2-A Q-C2.3 answer lines 1268-1280; gate ID `S91-VII-AV-COCYCLE-RATIO-LMAX-LE-10-DEGENERATION-TEST`).
   - **What**: Evaluate substrate cocycle ratio `‖φ_67‖/‖φ_88‖` at L_max ∈ {6..10} truncations of the D_K master spectrum cache, across regulator atlas {ζ, PV, Mellin, cutoff}, to test Hochschild-cohomology degeneration prediction under Reading A.
   - **Inputs**: `s84_spectrum_cache_L12_tau019.npz` (cache_sha256 = `9e6d9cf7fd6a6949…` per W8-7 (d) line 1417); `s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` (input_sha `d0683bcd31e7eaca…` per W8 WP §W8-7 (b) line 1394); existing W3 A.14 regulator-class invariance scan pipeline; canonical_constants.py: `M_KK = 7.428660036284456e+16`, `tau_fold = 0.19`.
   - **Gate**: PASS iff at L_max ∈ {6..10}, cocycle ratio returns STRUCTURALLY DEGENERATE (0/0 indeterminate / NaN) OR |ratio − 7.3249743784| > 1.0 across {ζ, PV, Mellin, cutoff} regulator atlas (distinct from regulator-INVARIANT 7.3249743784 at L_max=12); FAIL iff finite well-defined cocycle ratio with regulator-spread < 1e-3 at L_max ≤ 10 and value distinct from 7.3249743784; INFO iff regulator-spread ≥ 1e-3 OR mixed degeneracy/finite outcomes across L_max ∈ {6..10}.
   - **Effort**: ~0.8 wave-equiv (cocycle ratio evaluation per existing W3 A.14 pipeline extended to L_max ∈ {6..10} truncations of the master spectrum cache).

2. **CF-S91-CF-70-FULL-CC-MULTIPLIERS** (per W8 WP CF-70 spec lines 1653-1658; per V3 substrate-physics axis Layer 1 refinement).
   - **What**: §VII.AV proxy-refinement via FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers (M_1 = M_KK, M_2 = √2·M_KK, c_1 = +2, c_2 = −1; consistency identities Σ c_r = 1.0 exact + Σ c_r·m_r² ≈ 0 at machine precision); reconstruct Level-2 envelope `L^{-3}` across L_max ∈ {6..12} under PV-regulated kernel that evades the L_max ≤ 10 BCS phase boundary.
   - **Inputs**: `computations/_pauli_villars_subtraction.py` Connes-Chamseddine 1996 §2.2-2.3 2-point PV module (input_sha `eaf98037ddc2a4d7…` per W8 WP §W8-7 (c) line 1405); `s84_spectrum_cache_L12_tau019.npz`; W3 A.14 cocycle ratio cross-anchor 7.3249743784 (substrate canonical 7.324992); canonical_constants.py: `Delta_BCS = 0.4642547394830737`, `V_BCS_canonical = 2.447e-7 M_KK^{-1}`, `T_BCS = 0.64`, `tau_fold = 0.19`, `M_KK = 7.428660036284456e+16`.
   - **Gate**: PASS iff `α ∈ [2.5, 3.5] AND R² ≥ 0.95 AND L_max=12 anchor bit-match < 1e-9 under FULL Connes-Chamseddine multipliers route AND W3 A.14 cocycle ratio reproduced within regulator-spread 1e-3` (cross-anchor preservation); INFO iff partial PASS on any criterion; FAIL otherwise. Advances PROXY-REFINEMENT K-counter K=1 → K=2 on PASS.
   - **Effort**: ~1.5 wave-equiv (PV-regulated gap-equation scan across L_max ∈ {6..12} + Level-2 envelope fit + cocycle ratio cross-anchor verification).

3. **CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS** (per W8 WP CF-71 spec lines 1660-1665; per R2-B CONVERGENCE CC5 NEW OPERATIONAL-ALIGNMENT sub-class).
   - **What**: §VII.AV K_canonical pin uniqueness investigation; re-derive K_canonical from substrate-IS BdG energy gap at τ_fold; resolve P_BdG projector implementation distinction at L_max=12 (scalar Δ vs multi-branch s52 B-tensor); test alignment of FULL-BdG L_max=12 anchor with §W5-2 canonical −7.046336 under corrected K_canonical pin.
   - **Inputs**: CF-61 output `s90_w8_corner_iv_full_bdg_rederive_per_lmax.npz` (audit_sha `6357ab9650615732363c24d89e588569dc5c37f04bef7362e538b1677335b716` per W8-3 line 530); §W5-2 / S87 W2-3 canonical anchor `L_emp(L_max=12) = −7.046336474406761`; CF-62 disambiguated Element-1 K-window log-derivative producing script (audit_sha `8b4bfdee600fceb7…` per W8-4 lines 583-589); s52 multi-branch ED canonical amplitudes (B1=0, B2=0.7704350983, B3=0.176); canonical_constants.py: `Delta_BCS = 0.4642547394830737`, `T_BCS = 0.64`, `tau_fold = 0.19`.
   - **Gate**: PASS iff `K_canonical derivation uniquely determined by substrate's BdG energy gap at τ_fold AND |L_emp(L_max=12)_corrected − (−7.046336474406761)| < 1e-9 under corrected K_canonical pin`; INFO iff partial alignment (1e-9 ≤ |diff| < 1e-3); FAIL iff |diff| ≥ 1e-3 OR K_canonical derivation admits non-unique solution. Advances NEW OPERATIONAL-ALIGNMENT K-counter K=1 → K=2 on PASS.
   - **Effort**: ~1.2 wave-equiv (K_canonical re-derivation from substrate-IS BdG energy gap at τ_fold + K-window log-derivative recomputation under corrected K_canonical + anchor alignment verification).

4. **CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST** (per V4 lines 165-229 + Re:V4 §"Sharpening proposed for V4 pre-registration" lines 581-590; gate ID `S91-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST`).
   - **What**: Level-3 dual-anchor joint-hypersurface discriminator gate at L_max=12; (B1, B2, B3) configuration sweep (20×20×20 = 8000 + ×3 refinement near canonical s52 + ×3 refinement near scalar-Δ FULL-BdG implementation = ~16,000 configurations) testing whether ANY configuration aligns BOTH with scalar-Δ FULL-BdG output `L_emp_FULL_BdG_scalar_Delta(L_max=12)` AND with canonical anchor `−7.046336474406761` within 1e-3 relative tolerance.
   - **Inputs**: Same 9-pin input map per V4 lines 175-185 (CF-61 NPZ + §W5-2 canonical anchor + s52 ED canonical amplitudes + `s84_spectrum_cache_L12_tau019.npz` + canonical_constants.py constants + `_pauli_villars_subtraction.py` PV module + CF-62 K-window log-derivative producing script + W3 A.14 cocycle ratio cross-anchor + optional CF-69 τ-extension cache).
   - **Gate**: convention tag `convention=substrate-IS-canonical-K-window-log-derivative-MULTI-BRANCH-S52-VS-SCALAR-DELTA-FULL-BDG-ADJUDICATION-JOINT-HYPERSURFACE-DUAL-ANCHOR L_max=12` per Element 3 binding type (iii) joint-hypersurface declaration. PASS = Reading B confirmed at L_max=12; FAIL = Reading A confirmed at L_max=12; INFO = refinement-pathway carries both. Routes the CF-70 vs CF-71 dispatch ordering POSTERIOR per Re:V3 Option γ flowchart.
   - **Effort**: ~1.5 wave-equiv (8000 + 16k refined configuration evaluations × K-window log-derivative evaluation on L_max=12 spectrum + cocycle ratio cross-check per PASS-class configuration + ∀-quantified non-existence check for FAIL).

5. **CF-S91-VII-AV-REGISTRY-TEXT-4TH-REFINEMENT-ROUTE-EXTENSION** (per R2-A C4 + R2-B CONVERGENCE CC3; mack-cosmic-bridge sole-writer landing per `feedback_mack-bridge-role.md`).
   - **What**: §VII.AV registry-text refinement-pathway table extension at `sessions/permanent-results-registry.md` lines 17944-17948; add route (iv) "K_canonical pin uniqueness operational-alignment" (CF-71; Layer 2 operational-machinery axis) + route (v) "V4 substrate-physics discriminator gate adjudication" (V4; Level-3 dual-anchor joint-hypersurface) + route (vi) "Hochschild-cohomology cross-anchor" (CF-77; Level-1 cocycle-ratio degeneration test) + explicit "Layer" column with substrate-physics / operational-machinery / dual-anchor-joint-hypersurface / Hochschild-cohomology tags per Re:V3 + C2 proposal lines 967-981.
   - **Inputs**: §VII.AV registry text lines 17897-17948 + cross-link references per Re:V3 + R2-A C4 + R2-B CONVERGENCE CC3; mack-cosmic-bridge memory `reference_key-constraints.md` + the W-5 close workshop document (this file) audit_sha as input-pin.
   - **Gate**: PASS iff registry-text 4th + 5th + 6th refinement-pathway rows + explicit Layer column landed at registry lines 17944-17948 with mack-cosmic-bridge sole-writer signature + cross-link to CF-70/CF-71/CF-77/V4 carry-forwards + audit_sha companion comment row.
   - **Effort**: ~0.4 wave-equiv (registry-text Edit-tool operation by mack-cosmic-bridge with input-pin map + dual-SHA companion comment row per `gate-verdicts.md` schema).

6. **CF-S91-NEW-DEFERRED-PENDING-SUB-CLASS-OPERATIONAL-ALIGNMENT** (per DISSENT D1 + R2-B CONVERGENCE CC5; rule-file extension at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`).
   - **What**: Add NEW deferred-pending sub-class `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` to `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` (current sub-classes: PROXY-REFINEMENT, FIRST-EXTRACTION). New sub-class definition: Level-2 envelope realized via operational-machinery state-side specification (Bogoliubov-amplitude tensor choice / P_BdG projector implementation); refinement pathway is K_canonical pin uniqueness operational-alignment from substrate-IS BdG energy gap at τ_fold. Calibration corpus instance #1 = §VII.AV at W-5 close; advances K=1 SUGGESTION → K=2 contingent on CF-71 PASS at S91+; promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` K-counter threshold.
   - **Inputs**: `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` lines 65-130; this workshop document (W-5 close audit_sha as input-pin); methodology-wave-allowlist.md allowlist (orchestrator-only-edit per recursion-attack-closure protocol) — requires gate-ID `S90-W5-VII-AV-DEFERRED-PENDING-OPERATIONAL-ALIGNMENT-SUB-CLASS-EXTENSION` allowlist append per Methodological Observation MO1; OR S91+ mack-cosmic-bridge sole-writer re-landing pathway.
   - **Gate**: PASS iff new sub-class definition added to `cross-pillar-bridge-anatomy.md` with calibration corpus instance #1 = §VII.AV at W-5 close + K=1 SUGGESTION baseline declaration + cross-link to PROXY-REFINEMENT + FIRST-EXTRACTION as 4-corner algebra-axis orthogonality companions + `_substrate_first_provenance_audit.py` or `_cross_pillar_bridge_audit.py` extension to detect the new sub-class tag at plan-freeze.
   - **Effort**: ~0.5 wave-equiv (rule-file Edit-tool operation + methodology-wave-allowlist.md allowlist append OR mack-cosmic-bridge sole-writer landing + audit-script extension for `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` detection).

7. **CF-S91-CROSS-WORKSHOP-JOINT-WIN-K5-PROMOTION-WATCHPOINT** (per EMERGENCE EC3 + R2-B CONVERGENCE CC1 cross-workshop K=4 → K=5 MANDATORY promotion event at this W-5 close).
   - **What**: Track the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter advancement K=4 → K=5 MANDATORY at the workshop-verdict-pattern layer (Σ_2 stratum). Verify the K=5 MANDATORY promotion event triggers (per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold) and document the structurally novel content at K=5: future cross-axis adversarial workshops MUST adopt the layer-decomposition verdict template (NOT narrative-compromise framing). Update `methodology-wave-allowlist.md` allowlist entries for future cross-axis workshops to require layer-decomposability verification at workshop-spec time.
   - **Inputs**: W-1 H̃-DIVERGENCE-CHASE (S82) + W-2 A_s LEDGER 3PI-vs-SLOT (S82) + W-3 r-dual-pathway (S86) + W-4 dual-symbol-convention (S88) + W-5 (this workshop; CF-61 BCS phase transition reading hybrid verdict d) workshop documents as 5-instance corpus; `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold; `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence weight-2 image at Σ_2 stratum; `methodology-wave-allowlist.md` allowlist rows.
   - **Gate**: PASS iff K=5 MANDATORY promotion event documented in `sessions/permanent-results-registry.md` (Stage-1 candidate landing) AND `methodology-wave-allowlist.md` allowlist updated for forward enforcement AND `joint-theorem-promotion.md` Stage-2 cross-reviewer assignments pre-registered for S92+ (axis-distinctness: lizzi-spectral-functional-theorist spectral-side + transit-dynamics-aether-mechanic substrate-side; downstream-inheritance-reach exclusion verified).
   - **Effort**: ~0.6 wave-equiv (registry-landing of K=5 MANDATORY promotion event via mack-cosmic-bridge sole-writer + methodology-wave-allowlist.md allowlist update via orchestrator + Stage-2 cross-reviewer pre-registration in W-5 close carry-forward queue).

### Closing Line

The W-5 cross-axis JOINT-WIN closes at hybrid verdict (d) "substrate phase boundary AT operational-machinery joint layer" — Reading A WINS Layer 1 substrate-IS Cooper-instability criterion failure at L_max ≤ 10; Reading B WINS Layer 2 Level-3 P_BdG-projector-implementation distance at L_max=12 under Hochschild-Künneth Morita-invariance — with 4-axis orthogonal refinement-pathway space (CF-70 + CF-71 + V4 + CF-77) at S91+ wave-together dispatch and K=4 → K=5 MANDATORY promotion of the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern as canonical resolution template for future cross-axis adversarial workshops at the methodology-floor Σ_2 stratum.
