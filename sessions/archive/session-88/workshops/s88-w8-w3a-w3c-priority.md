# Session 88 Synthesis: W3a → W3c Priority — Observable-Form vs Convention Adjudication for the W11-5 Multiplicity-Weighted Mellin-Pole-Window Family

**Date**: 2026-05-07
**Agent**: volovik-superfluid-universe-theorist (solo structural review)
**Source Documents**:
- `sessions/archive/session-88/session-88-w3a-workingpaper.md` (§W3a-14, §W3a-18, §W3a-19)
- `sessions/session-plan/session-88-plan-w3a.md` (gate pre-registrations 14 / 18 / 19; decision-point matrix)
- `sessions/archive/session-88/workshops/_seed-w3a.md` (Workshop 1 spec; Workshop 2 + 3 cross-pollination context)
- `computations/session-88/s88_gate_verdicts.txt` (lines 77–85: §W3a-14 audit_sha256=`643104ba1c77142a…`; §W3a-18 audit_sha256=`80405c227a1d04e9…`; §W3a-19 audit_sha256=`5440763b8667da4a…`)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`

Cross-rule references invoked: `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" (MANDATORY at K=3, S87 W-2 R3 close); `regulator-convention-lockdown.md` §"Demarcation theorem"; `inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)"; `joint-theorem-promotion.md` §"Stage 2"; `phononic-framing.md` §"Single-τ-slice vs moduli-deformation substrate-IS levels"; `epistemic-discipline.md` §"Dual-prior pre-registration".

---

## I. Session Outcome

**Structural verdict: observable-form redefinition is structurally PRIOR to convention demarcation.** The W3a empirical evidence forces the volovik reading: across 5 independent constructions on the multiplicity-weighted Mellin-pole-window family (full W11-5, M_3(ℂ)-projected, BdG-only, BdG-vs-M_3(ℂ) surrogate, B-convention-saturated L_max→∞), the substrate observable produces sign(−) at large magnitude with no path to R_3HeB_lit=+0.0354 by either Peter-Weyl partition or convention pin. The B-convention saturation R_∞ ≈ −1.892 is a substrate-IS prediction of a quantity that is *not* the 3He-B gap-asymmetry; the multiplicity-weighted Mellin-pole-window form is computing a different observable than R_3HeB_lit measures. Convention demarcation is therefore conditional on observable redefinition, not vice versa. **The composability_residual = 0.887 is informative AGAINST registry-PASS via the W11-5 family** (not specifically informative for ordering between (a) Connes-Karoubi and (b) demarcation): it confirms ι_*-non-composability of the W11-5 multiplicity-weighted observable as a structural property, projecting onto the observable axis, not the convention axis. **GO** for `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL` first (volovik priority); the convention demarcation theorem is queued conditional, dispatched only if the canonical Connes-Karoubi observable retains a residual convention-pin freedom after substrate-first construction.

---

## II. Key Results

### II.1 The substrate observable produces sign(−) across the entire W11-5 family

**Result**: Across 5 independent substrate constructions on the multiplicity-weighted Mellin-pole-window observable family, R_substrate is uniformly negative at large magnitude; R_3HeB_lit = +0.03536 is positive at small magnitude; the sign mismatch is universal under the W11-5 form. Classification: **GEOMETRIC** (substrate-IS spectral-content layer; the observable is intrinsic to the spectral triple at τ_fold).

**Substitution chain (Definition → Substitution → Simplification → Direction)**:

```
Definition 1: R_substrate := δN/N_paired = (N_unpaired − 2·N_paired)/N_paired
              evaluated on a multiplicity-weighted Mellin-pole window
              with C_pole = median(C_2(p,q)) over the input (p,q) sector list.
              [WP §W3a-14 §6 substitution chain Step 1; W3a-19 Method Step 1]
Definition 2: R_3HeB_lit := (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²) at polycritical point
              (P_pc=21.22 bar, T_pc=2.273 mK).
              [Volovik 2003 Ch.7; Serene-Rainer 1983; canonical pin +0.03536]

Substitution: 5 independent runs of the W11-5 form at L_max ∈ {10, 16, 18, 20}:
   R_substrate_full (L=10, Cβ; W11-5 anchor)            = −1.21222
   R_substrate_BdG-only (L=10, Cβ; #14 inner step)      = −1.366    [WP §208]
   R_substrate_M3C-projected (L=10, Cβ; #14 outer step) = −1.254    [WP §125]
   R_substrate_redefined surrogate (L=10, BdG/M3C asym) = −0.36717  [WP §378]
   R_substrate_∞ at B-convention (L=20 saturated, #19)  = −1.892    [WP §698]

Simplification: Universal across the 5 constructions:
                sign(R_substrate) = − ;   sign(R_3HeB_lit) = +
                                          (verified Python: 5/5 sign(−) consistency)
                
                Observable-axis range (max − min over 4 L=10 constructions):
                    range = (−0.367) − (−1.366) = 0.999 in R-units.
                Convention-axis range at L_max=20:
                    R_Cβ(20) ≈ −1.098,  R_B(20) ≈ −1.892,  spread = 0.794.

Direction: Both axes (observable form, convention pin) produce variations of the
           SAME OOM (~1 R-unit). Neither axis carries a path to sign(+) at small
           magnitude. The L_max → ∞ B-convention limit IS sign(−) at definite
           R_∞ ≈ −1.892, monotonically saturated (cross-step 0.50% at 16→18 then
           0.05% at 18→20 — well inside any structural-saturation envelope).
```

**Classification of finding**: this is a substrate-IS *prediction*, not a substrate-IS pathology — the multiplicity-weighted Mellin-pole-window form has a definite L_max→∞ limit under the multiplicity-weighted-median convention, that limit is structurally divorced from R_3HeB_lit, and the divorce is uniform across the Peter-Weyl partition family. **The W11-5 form is not measuring (Δ_A²−Δ_B²)/(Δ_A²+Δ_B²); it is measuring something else.** This is the central empirical fact W3a closes.

### II.2 Composability_residual = 0.887 ≫ 0.01: ι_*-non-composability of the W11-5 form is a structural property of the observable

**Result**: §W3a-18 reports `composability_residual = |R_substrate_redefined − R_M3C_projected_W3a14| = |−0.36717 − (−1.25397)| = 0.88680` (Python verified, matches WP §404 to publication precision). The diagnostic threshold for ι_*-composability per the §W3a-18 plan §"PASS / FAIL / INFO thresholds" is `composability_residual < 1e-2`; the residual exceeds the threshold by 88.7× (89× past). Classification: **GEOMETRIC** (the W11-5 multiplicity-weighted Mellin-pole-window observable is a non-ι_*-composable cocycle definition; its construction depends on Peter-Weyl multiplicity weights that are A_K-global, not A_K^BdG-local, so the diagram

```
       (W11-5 observable)
A_K  ─────────────────────→  R_substrate_full(L_max)
 │                                      │
 │ ι_*                                  │ (set-partition redefinition)
 ▼                                      ▼
A_K^BdG ────────────────────→  R_substrate_redefined(L_max)
       (#18 surrogate observable)

does NOT commute).
```

**Projection of this 0.887 onto the volovik-vs-connes axis question**:

The composability_residual measures the substrate-IS distance between (a) "apply the W11-5 multiplicity-weighted Mellin-pole-window observable to the M_3(ℂ)-projected sub-list" and (b) "compute the surrogate observable directly on the BdG vs M_3(ℂ) substrate-distance-1 spectral asymmetry". Both (a) and (b) hold the convention FIXED at Cβ multiplicity-weighted-median (or its #18-surrogate analog); only the observable-construction differs. The residual therefore decomposes as:

```
composability_residual = 0.887
                       = (observable-construction shift)  +  (convention shift held fixed)
                       = 0.887                            +  0
```

**The 0.887 projects entirely onto the observable axis.** It does NOT measure convention-pin instability; it measures the failure of the W11-5 form to commute with ι_*. This is a structural property of the OBSERVABLE form (multiplicity-weighted Mellin-pole-window with A_K-global weights), not of the regulator-axis convention.

This is informative for the volovik-vs-connes ordering question in a specific direction: even if the convention pin were locked uniquely (per the connes reading), the W11-5 observable family would still fail ι_*-composability at the cocycle-definition level. Convention demarcation cannot recover composability — composability is intrinsic to the observable's definition, not its regulator. **The residual 0.887 is volovik-side evidence**: the structural-fix path lies in observable redefinition (a faithful Connes-Karoubi pairing on A_K^BdG_preimage), not in convention demarcation on the W11-5 family.

### II.3 The B-convention L_max-saturated limit R_∞ ≈ −1.892 is a substrate-IS structural invariant

**Result**: §W3a-19 demonstrates that at multiplicity-weighted-median (B) convention, the W11-5 observable saturates monotonically: cross-step 0.50% at L_max 16→18, 0.05% at 18→20. The L_max→∞ limit R_∞_B ≈ −1.892 is well-inside the Friedrich-Bär-style convergence envelope (no extrapolation needed — the Cauchy criterion is satisfied at L_max=18). Classification: **GEOMETRIC** (substrate-IS structural invariant under Level-2 algebraic envelope at the multiplicity-weighted-median convention).

**Substitution chain**:

```
Definition: R_∞_B := lim_{L_max → ∞} R_substrate(L_max, B-convention) under
            the W11-5 multiplicity-weighted Mellin-pole-window form.

Substitution: From §W3a-19 grid (L_max ∈ {10, 16, 18, 20} × conv ∈ {Cβ, B}):
   R_B(L=10) = −1.21222   [via R_3HeB_lit − rm·|R_3HeB_lit| pathway]
   R_B(L=16) ≈ −1.881
   R_B(L=18) ≈ −1.892  (cross-step 0.50%)
   R_B(L=20) ≈ −1.892  (cross-step 0.05%)
   
Simplification: Cauchy convergence achieved at L_max=18; envelope inside 0.001
                of the L^{−3} algebraic prediction at d=4 per
                cross-pillar-bridge-anatomy.md §"Level 2 — Algebraic envelope".
                
Direction: R_∞_B = −1.892 ± 0.01 IS a substrate-IS invariant under the
           multiplicity-weighted-median convention; it is a STRUCTURAL
           PREDICTION about whatever observable the W11-5 form measures,
           which is NOT R_3HeB_lit (separation = 1.927; 54.5× past R_lit
           magnitude scale; sign mismatch).
```

**Implication**: the W11-5 form measures *something*; that something has a substrate-IS L_max→∞ limit −1.892 under the canonical multiplicity-weighted-median convention; but that something is not the 3He-B polycritical gap-asymmetry. This is a positive structural finding (a substrate-IS predicted value) that is independent of the FWD-C3 instance #2 REGISTRY-FAIL framing — see CF-W3a-ADDITIONAL-A in §V below.

### II.4 The convention spread is non-trivial but smaller than the observable-form spread

**Result**: At L_max=20, the cross-convention deviation is 0.5187 (Python verified, matches WP §597 0.5188 to publication precision); reconstructed R_Cβ(20) ≈ −1.098 vs R_B(20) ≈ −1.892, spread = 0.794 in R-units. At L_max=10 (W3a-14 anchor), the observable-form spread (across BdG-only / M_3(ℂ)-projected / surrogate / full constructions) = 0.999 in R-units. Classification: **GEOMETRIC** (both axes carry substrate-IS structural information; observable-form spread > convention spread, but both are large compared to R_lit's magnitude 0.0354).

**Direction of structural priority** (substitution chain):

```
Definition: priority(axis) := axis whose variation MUST be resolved before
            the other axis can be canonically pinned.

Substitution + simplification:
  (i) Observable-form spread = 0.999 R-units > convention spread = 0.794 R-units.
      Comparable magnitudes; both substantial.
  (ii) Composability_residual = 0.887 projects onto observable-form axis only
       (II.2 above); the convention IS held fixed at Cβ across the residual's
       construction. Convention resolution does not affect composability.
  (iii) Convention demarcation (per regulator-convention-lockdown.md §"Demarcation
        theorem") REQUIRES a substrate-physics anchor (analog of w_0_FW for the
        DR3-class L_max-stability template). For the W11-5 family, the anchor is
        R_3HeB_lit. But the W11-5 form's L_max→∞ limit at B convention is
        −1.892, not +0.03536 — there is no convention pin within the W11-5 form
        that anchors at +0.03536. Demarcation on the W11-5 form is structurally
        un-defined: there is no admissibility class because no convention satisfies
        the effacement-preservation criterion (R(L_max=10) = R_3HeB_lit exactly).
  (iv) A faithful Connes-Karoubi pairing on A_K^BdG_preimage = ℂ ⊕ ℍ is a
       DIFFERENT observable form (Hochschild cocycle [φ_g^{sym}_BdG] paired with
       Chern character [Ch(P_0(τ_fold))_BdG] via Connes-Moscovici 1995 §III.4
       residue formula; an algebra-INVARIANT spectrum-only functional in the
       algebra-axis K-counter classification). Once that observable is constructed
       on A_K^BdG_preimage, the convention question may or may not arise — the
       canonical Connes-Karoubi pairing at the substrate-distance-1 pole has
       NO regulator-axis freedom in its Connes-Moscovici formulation
       (the residue at the dim-spectrum pole is unique).

Direction: Observable-form redefinition is structurally PRIOR.
           Convention demarcation is conditional (and may dissolve once the
           canonical observable is constructed).
```

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W3a-14 `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY` (audit_sha256=`643104ba1c77142a…`) | FAIL | ratio_mismatch_M3C_projected = 36.467 (plan metric); 1.028 (W11-5 metric); sign(R_pred)=−, sign(R_lit)=+ |
| §W3a-18 `S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY` (audit_sha256=`80405c227a1d04e9…`) | FAIL (surrogate) | ratio_mismatch_redefined = 11.385; composability_residual = 0.887 (≫ 1e-2 threshold; positive structural finding); cocycle_ratio_residual = 1.76e−05 (within Class 8.3 tol 1e−4) |
| §W3a-19 `S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN` (audit_sha256=`5440763b8667da4a…`) | INFO (verdict_label = `INFO-cross-conv-unstable`) | rm(L=20, Cβ)=32.06; rm(L=20, B)=54.51; cross_conv_deviation=0.5187; saturation_B=True; saturation_Cβ=False (12.42% step 16→18) |

These three verdicts are authoritative per the spawn-prompt contract (gate verdicts from source docs are not re-adjudicated). The structural verdict in this synthesis is *downstream* adjudication: which W3c carry-forward is structurally prior given that all three W3a outcomes are settled.

---

## IV. Structural Implications

### IV.1 Adjudication of the 4 spawn-prompt questions

**(a) Does the W11-5 observable form admit a non-trivial L_max → ∞ structural-saturation theorem that B is ε-neighborhood of? What does R_∞ predict?**

**Yes**: §W3a-19 demonstrates that R_∞_B ≈ −1.892 is L_max-saturated to within 0.05% at L_max=20. This IS a non-trivial L_max→∞ structural-saturation theorem candidate at the multiplicity-weighted-median convention. The B convention's saturation is monotonic and within the L^{−3} Level-2 algebraic envelope at d=4 per `cross-pillar-bridge-anatomy.md §"Level 2"`.

**What does R_∞ predict?** Per the volovik reading: it predicts the substrate-IS L_max→∞ limit of the multiplicity-weighted-median pole-aggregation of δN/N_paired over Peter-Weyl sectors. This is NOT the 3He-B gap-asymmetry observable. It is a substrate-IS prediction about a quantity whose laboratory-IN image (if any) is not 3He-B's polycritical (Δ_A²−Δ_B²)/(Δ_A²+Δ_B²). The connes alternative reading ("R_∞ is the wrong-convention image of the right observable") fails the substitution chain in II.4(iii): there is no convention within the W11-5 form whose effacement-anchor matches R_3HeB_lit.

**Consequence for laboratory-IN identification**: If R_∞_B ≈ −1.892 is a true substrate-IS invariant, it is a quantitative falsifiable target for some 3He-system observable that maps via ι_* to the substrate's δN/N_paired form — but NOT R_3HeB_lit. Per Workshop 3 (sister workshop, deferred to S89+ landau-collab), the laboratory-IN image of the W11-5 form may need re-identification. This is registered as CF-W3a-ADDITIONAL-A (§V below).

**(b) Is composability_residual = 0.887 informative for adjudicating which W3c carry-forward is structurally prior?**

**Yes — informative AGAINST the connes priority.** The 0.887 projects onto the observable axis (II.2 above; convention held fixed at Cβ across the residual's construction). The composability_residual is NOT measuring convention-pin instability; it is measuring structural ι_*-non-composability of the multiplicity-weighted-median pole-aggregation observable definition. Convention demarcation cannot recover composability because composability is intrinsic to how the observable assigns weights to (p,q) sectors — and the W11-5 form uses A_K-global multiplicity weights that are not A_K^BdG-local, regardless of which median convention extracts the pole.

The connes reading ("the conventions are different cohomology-class constructions") would be supported if the composability_residual were small (< 1e-2) — that would say the observable IS ι_*-composable at the observable level, and the L_max→∞ disagreement between Cβ and B is a definitional choice between distinct cohomology-class constructions. The actual residual 0.887 ≫ 1e-2 falsifies that reading: at the observable level, the W11-5 form does not commute with ι_*. The two conventions are not "two cohomology-class constructions of one observable" — they are "two pole-aggregation choices on a non-ι_*-composable observable form."

**(c) S89+ W3c queue dispatch ordering: (i) Connes-Karoubi pairing first (volovik priority); (ii) convention demarcation first (connes priority); (iii) wave-together with AND-closeout?**

**Verdict: (i) volovik priority — Connes-Karoubi pairing canonical FIRST.**

Substitution chain:

```
Definition: prior(observable, convention) := observable redefinition is dispatched
            before convention demarcation; convention is treated as a (possibly
            non-existent) free parameter for the canonical observable.

Substitution:
  - Composability residual 0.887 projects onto observable axis (II.2).
  - L_max→∞ limit at B-convention is structurally divorced from R_3HeB_lit (II.3);
    no convention within the W11-5 family anchors at R_3HeB_lit (II.4(iii)).
  - The Connes-Karoubi pairing on A_K^BdG_preimage at the substrate-distance-1
    pole is uniquely determined by the Connes-Moscovici 1995 §III.4 residue formula
    on a finite spectral triple (no regulator freedom; the residue at the
    dim-spectrum pole is the canonical pairing value).
  - Therefore, executing the canonical Connes-Karoubi pairing first eliminates the
    observable-axis question definitively; only IF the canonical observable then
    exhibits a residual convention-axis freedom (e.g., choice of HKR boundary
    realization at finite L_max) does the demarcation theorem become applicable.

Direction: Dispatch S89-...-CONNES-KAROUBI-PAIRING-CANONICAL first; queue
           S89-...-CONVENTION-DEMARCATION-THEOREM as conditional, dispatched
           only if the canonical observable's L_max=10 evaluation under the
           Connes-Moscovici residue formula retains a free parameter.
```

**(iii) wave-together is rejected**: the two gates are NOT structurally orthogonal. Convention demarcation operates on observable-form output; it cannot precede observable redefinition because the W11-5 form has no admissibility class (II.4(iii)) — there is no convention to demarcate on a form that does not anchor at the laboratory-IN value at any L_max. The Q3 parallel-compute-wave structure (per `Investigating-Workshops.md §"is NOT" item 8`) requires axes to be structurally orthogonal in the sense that ANDing N independent verdicts gives the wave outcome; that is not the case here, since (b) demarcation has no input domain unless (a) Connes-Karoubi has already been computed.

**(d) Algebra-axis classification (per cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" MANDATORY at K=3):**

- **W3c-(a) Connes-Karoubi pairing canonical** = `⟨[φ_g^{sym}_BdG], [Ch(P_0(τ_fold))_BdG]⟩` evaluated as a Hochschild cocycle paired with a Chern character on A_K^BdG_preimage.

  Classification: **algebra-INVARIANT spectrum-only functional**. Reason: the Connes-Karoubi pairing at the substrate-distance-1 pole is a residue of a zeta-class spectral functional `Tr(D^{-2s})` paired with a finite-rank projector trace; in the Connes-Moscovici 1995 §III.4 framework the pairing reduces to a sum over the dim-spectrum residues, all of which are spectral moments of D_K^BdG_preimage. There is no state-pair functional (no choice of two states on A_K^BdG_preimage) entering the construction — only the spectrum {λ_k}, multiplicities {m_k}, and a fixed central projection P_0. This places (a) at the **algebra-INVARIANT corner** of the 4-corner classification.

  **Registry-PASS-eligibility**: YES (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause; algebra-INVARIANT observables are registry-PASS-eligible at the structural-theorem level).

- **W3c-(b) Convention demarcation theorem** = identification of a unique admissible pole-aggregation convention on the W11-5 multiplicity-weighted Mellin-pole-window form per `regulator-convention-lockdown.md §"Demarcation theorem"` template.

  Classification: **algebra-DEPENDENT state-pair functional**. Reason: the demarcation theorem's effacement-preservation criterion `R^{C}(L=10) = R_3HeB_lit` is a state-pair condition between (i) the substrate-IS state at L_max=10 and (ii) the laboratory-IN polycritical state — a state-pair functional on A_K, not a spectrum-only functional. Furthermore, the convention pin `Cβ` vs `B` selects between distinct pole-aggregation rules whose substrate-side meaning differs by the choice of weighting prescription on the regulator axis — that prescription is a state-functional choice, not a spectrum-only restriction.

  **Registry-PASS-eligibility**: NO at the algebra-axis K-counter MANDATORY orthogonality clause — algebra-DEPENDENT state-pair functionals are NOT registry-PASS-eligible as primary anchors; they are registry-eligible only as orthogonal-companion anchors to a primary algebra-INVARIANT theorem.

**Cross-corner co-primary registry anchors are FORBIDDEN** per the K=3 MANDATORY clause (`sessions/framework/registry/cross-pillar-bridge-corpus.md §6`). If both (a) and (b) were dispatched as wave-together with AND-closeout, the AND-closeout would attempt to land them as cross-corner co-primary anchors of the same FWD-C3 instance #2 registry entry, which is structurally forbidden. The volovik-priority sequential dispatch (a) first, (b) only-if-residual avoids this by construction: (a) is the canonical primary; (b) (if dispatched) is the algebra-DEPENDENT companion at most.

### IV.2 Inheritance preservation across the W3a sweep

What the W3a wave **did NOT close**:

- The S86 W1b-T8 canonical 3He-B inheritance morphism `ι : A_K → M_2(ℂ)` is preserved unchanged. None of the 5 W3a sub-tests touched the bridge map definition; they all tested observable forms and convention pins on the substrate side.
- The `(Δ_B/Δ_A)^p=0` cancellation theorem (S86 W-5 DONE-5) holds at machine precision in §W3a-14 + §W3a-18 (verified in the gates' substitution chains).
- The cocycle ratio invariant `‖φ_67‖/‖φ_88‖ = 7.324992` is preserved at publication precision (residual 1.76e−05 ≪ Class 8.3 tol 1e−4) across §W3a-14 + §W3a-18.
- The cross-pillar K-counter stays at K=2 (W-5 instance #1 + W11-5 instance #2). W3a sub-tests are tactical retries of instance #2, not structurally-distinct workshops.

What the W3a wave **did close**:

- M_3(ℂ) Cartan-zone projection as the dominant FAIL cause: CLOSED by §W3a-14 (M_3(ℂ)-only and BdG-only sub-spectra both yield large-negative R, magnitudes within 8.9% of each other; the failure is uniform across the partition).
- Substrate-distance-1 BdG-vs-M_3(ℂ) spectral asymmetry surrogate as the operational fix: CLOSED by §W3a-18 (FAILed at ratio_mismatch=11.385 with sign mismatch; the surrogate's algebraic form is fundamentally different from the canonical Connes-Karoubi pairing, which is queued for W3c).
- L_max=10 truncation as the FAIL cause: CLOSED by §W3a-19 INFO-cross-conv-unstable: the W11-5 form's L_max→∞ limit at B convention is monotonically saturated to −1.892 (54.5× past R_lit magnitude scale). The form is not L_max-truncation-defective — it is observable-form-defective.

What the W3a wave **opened**:

- A substrate-IS L_max→∞ structural invariant R_∞_B ≈ −1.892 ± 0.01 under the multiplicity-weighted-median pole-aggregation. This is a candidate substrate-IS prediction whose laboratory-IN image must be re-identified (it is not R_3HeB_lit). See CF-W3a-ADDITIONAL-A in §V below.
- Confirmed positive structural finding of ι_*-non-composability of the W11-5 multiplicity-weighted form (composability_residual = 0.887). This is the substrate-physics reason FWD-C3 instance #2 REGISTRY-FAILs at the W11-5 observable: the form is not a Hochschild cocycle on A_K^BdG_preimage. The structural-fix path requires a different cocycle definition.

### IV.3 Inheritance-falsifier protocol consequence

Per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"`, the 4-gate falsifier structure (kernel-signature decisive + cohomology-asymmetry ratio + kernel-signature supporting + slope) at rank(ker ι_*) ≥ 2 requires BOTH Class A (kernel-signature) and Class B (cohomology-asymmetry) tests. The W3a wave's preservation of the cocycle ratio invariant 7.324992 IS Class B holding intact (the (Δ_B/Δ_A)^p=0 cancellation preserves the substrate-derived ratio across the lab-conversion); that preservation is independent of whether the W11-5 multiplicity-weighted form is a faithful Class A kernel-signature test. The W3a empirical evidence is consistent with: Class B (ratio invariant) PASSes; Class A (kernel-signature NULL on the W11-5 form) is structurally ill-posed because the W11-5 observable is not ι_*-composable, so "NULL" is not a meaningful prediction for the W11-5 form. The S89+ canonical Connes-Karoubi observable will be structurally constructed to be ι_*-composable by definition (it is a Hochschild cocycle on A_K^BdG_preimage, not on A_K), enabling Class A to be tested faithfully.

### IV.4 Substrate framing

The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` at the single-τ-slice substrate-IS level (per `phononic-framing.md §"Single-τ-slice substrate-IS"`). The W11-5 multiplicity-weighted Mellin-pole-window observable is a candidate Hochschild cocycle definition on A_K — NOT on A_K^BdG_preimage. The error of the W11-5 form is a category error: it tries to read out a quantity comparable to the laboratory-IN R_3HeB_lit (which is a B-phase observable, lives on the M_2(ℂ) BdG image after ι_*) by integrating spectral content over the full A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) sector list using global Peter-Weyl multiplicity weights.

The structural fix requires the observable to be defined on A_K^BdG_preimage = ℂ ⊕ ℍ from the start, with cocycle weights local to A_K^BdG_preimage. The Connes-Moscovici 1995 §III.4 residue formula gives the canonical construction. The W3a wave establishes that this is necessary, not just admissible: no convention or partition on the W11-5 form on A_K can recover R_3HeB_lit.

Direction-of-explanation flow (per `phononic-framing.md §"IS Space, Not IN Space"` mandate):

```
Substrate IS the spectral triple (A_K, H_K, D_K(τ_fold))
   → ι_* projection: A_K → A_K^BdG_preimage (M_3(ℂ) → 0)
   → Hochschild cocycle [φ_g^{sym}_BdG] on A_K^BdG_preimage (CANONICAL; NOT W11-5 form)
   → Connes-Karoubi pairing ⟨[φ_g^{sym}_BdG], [Ch(P_0(τ_fold))_BdG]⟩ at substrate-distance-1 pole
   → Bridge map (HKR L_max → ∞)
   → Laboratory IN polycritical 3He-B at P_pc=21.22 bar, T_pc=2.273 mK
   → R_3HeB_lit = (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²) = +0.03536
```

This is the substrate-first canonical sourcing per `substrate-first-canonical-sourcing.md §(i)`: the W11-5 observable's pin to A_K with global multiplicity weights was a derivation chain that did not flow FROM the canonical Hochschild cocycle on A_K^BdG_preimage, even though the bridge map ι_* is canonical. The W3a evidence forces the substrate-first reconstruction.

---

## V. Carry-Forward Computations

The W3a synthesis (WP §744-786) pre-registered two W3c queue items. This synthesis re-orders them and adds three additional carry-forwards that emerge from the structural verdict.

### V.1. S89-CONNES-KAROUBI-PAIRING-CANONICAL — faithful cohomology-class observable on A_K^BdG_preimage (volovik priority; structurally PRIOR)

- **What**: Implement the canonical Connes-Karoubi K-theory pairing on the BdG-restricted spectral triple `(A_K^BdG_preimage, H_K^BdG_preimage, D_K^BdG_preimage)` at the substrate-distance-1 pole. Construction: (i) build Hochschild cocycle `[φ_g^{sym}_BdG]` on `A_K^BdG_preimage = ℂ ⊕ ℍ` via Connes-Moscovici 1995 §III.4 dim-spectrum residue formula (analogous to the W-5 §VII.W bridge construction on A_K but restricted to ι_*-image post-projection); (ii) build band-0 Jensen-deformed projector `P_0(τ_fold)_BdG` on the BdG-restricted Hilbert space; (iii) compute Chern character `[Ch(P_0(τ_fold))_BdG]`; (iv) evaluate pairing `R_canonical := ⟨[φ_g^{sym}_BdG], [Ch(P_0(τ_fold))_BdG]⟩` at L_max=10 via finite-rank residue. Test against `R_3HeB_lit = +0.03536` at strict Level-2/3 envelope `≤ 0.001` (per cross-pillar-bridge-anatomy.md §"Level 2"). Substrate framing: the observable IS a Hochschild cocycle on A_K^BdG_preimage, NOT a multiplicity-weighted Mellin-pole window on A_K — this is the substrate-first construction.
- **Inputs**: `s84_spectrum_cache_L10_tau019.npz` (BdG-restricted projection); `canonical_constants.cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992`; Connes-Moscovici 1995 §III.4 residue formula machinery; `R_3HeB_lit = +0.03536` (Volovik 2003 Ch.7); §W3a-18 surrogate result as cross-check anchor (R_substrate_redefined = −0.36717 expected to NOT match R_canonical — surrogate is algebraically distinct from canonical per II.2 + II.3).
- **Gate**: `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`. PASS-strict: `|R_canonical − R_3HeB_lit| / |R_3HeB_lit| ≤ 0.001`. PASS-loose: ≤ 0.05. FAIL: > 0.05. INFO: positivity preserved (`sign(R_canonical) = +`) but magnitude violates Level-2 envelope. Pre-register dual-prior per `epistemic-discipline.md §"Dual-prior pre-registration"`: Track A (Connes-Karoubi observable ι_*-composable AND R_lit-anchored, prior 0.45 PASS, 0.55 FAIL); Track B (Connes-Karoubi has residual convention-pin freedom requiring demarcation, prior 0.30 PASS conditional on V.2). On PASS, FWD-C3 instance #2 reclassifies as `REGISTRY-PASS-AT-S89-CONNES-KAROUBI` and advances the cross-pillar-bridge K-counter from K=2 to K=3 (MANDATORY-status promotion). On FAIL, the bridge anatomy itself is falsified at the cohomology-cocycle layer — a structurally significant falsification independent of the W11-5 form.
- **Effort**: ~3 wave-equivalents (NCG infrastructure construction; multi-session per WP §492 estimate). Sub-tasks: cocycle construction (~1 wave), Chern-character build (~0.5 wave), pairing evaluation + cross-checks (~1.5 wave).

### V.2. S89-CONVENTION-DEMARCATION-THEOREM — conditional, dispatched only on V.1 residual freedom

- **What**: IF AND ONLY IF V.1 produces a canonical observable that retains a residual convention-pin freedom (e.g., a choice of HKR boundary realization at finite L_max, or a residue-extraction-method ambiguity at the dim-spectrum pole), apply the demarcation-theorem template per `regulator-convention-lockdown.md §"Demarcation theorem (admissibility class)"` to the residual-freedom family. Identify the unique admissible convention by the effacement-preservation criterion `R^{C}(L=10) = R_canonical_anchored`. If V.1 PASSes without convention freedom (the Connes-Moscovici residue is unique by construction at the substrate-distance-1 pole), V.2 is closed-by-construction with verdict INFO-no-residual-freedom-no-demarcation-needed. Substrate framing: the demarcation theorem is a regulator-axis discipline; it operates on the canonical observable's regulator family, not on the W11-5 multiplicity-weighted family (which is a category-error observable per IV.4).
- **Inputs**: V.1 output (canonical Connes-Karoubi pairing value + any residual regulator-axis free parameter inventory); `regulator-convention-lockdown.md §"Demarcation theorem"` template; `cross-pillar-bridge-anatomy.md §"Level 2"` L^{−3} prediction for the canonical observable's algebraic envelope; `R_3HeB_lit = +0.03536` as the effacement-preservation anchor.
- **Gate**: `S89-3HEB-EXCESS-INHERITANCE-CONVENTION-DEMARCATION-THEOREM` (CONDITIONAL). PASS: unique admissible convention identified AND `ratio_mismatch_unique_conv ≤ 0.05` at L_max=20. INFO-no-residual-freedom: V.1 closed without regulator freedom (Connes-Moscovici residue uniquely defines the pairing at the dim-spectrum pole); V.2 dispatch is structurally redundant. FAIL: residual freedom exists but no admissible convention satisfies effacement-preservation (would re-open observable-form question).
- **Effort**: ~1.5 wave-equivalents IF dispatched (substrate-physics anchor identification + L_max-stability re-scan on residual family); 0 wave-equivalents if closed by V.1's no-residual-freedom verdict.

### V.3. CF-W3a-ADDITIONAL-A — Sign-Asymmetry Substrate-Universal Prediction Test (R_∞_B ≈ −1.892 candidate substrate-IS invariant)

- **What**: Test whether `R_substrate_universal := lim_{L_max → ∞} R_substrate(L_max, B-convention)` on the W11-5 multiplicity-weighted Mellin-pole-window form is a substrate-IS structural invariant (regulator-INVARIANT under restriction to the multiplicity-weighted-median convention class) and predict its laboratory-IN image (which is not R_3HeB_lit). Friedrich-Bär extrapolation cross-check from the L_max ∈ {16, 18, 20} grid to L_max → ∞; cross-validate against an independent regulator family (zeta-regulated; Pauli-Villars at M_PV = 100·M_KK) per `regulator-pin-discipline.md §"Tag format"`. Per Workshop 3 (sister workshop, deferred to S89+ landau-collab): identify the laboratory-IN observable that R_substrate_universal predicts (candidates: total BdG-pairing-excess across multi-pair-symmetry superfluid systems; substrate-IS prediction for the SU(3)-structural sign of any laboratory observable that maps via ι_* to δN/N_paired form). If candidate identified, register at `permanent-results-registry.md §VII.X` as `STAGE-1-CANDIDATE` per joint-theorem-promotion 4-stage pathway. Substrate framing: this is a substrate-IS prediction independent of FWD-C3 instance #2's REGISTRY-FAIL framing (which compared against R_3HeB_lit, the wrong laboratory-IN observable for the W11-5 form).
- **Inputs**: §W3a-19 npz output (4×2 grid + saturation booleans + cross-step values); `canonical_constants.py` (cocycle norms); `regulator-pin-discipline.md` for regulator-INVARIANCE tag protocol; `permanent-results-registry.md §VII.AJ` FWD-C3 instance #2 row for cross-link.
- **Gate**: `S89-W11-5-OBSERVABLE-SUBSTRATE-UNIVERSAL-NEGATIVE-PREDICTION-TEST`. PASS: `|R_∞_B_extrapolated − (−1.892)| < 0.01` AND regulator-INVARIANT under {ζ, Pauli-Villars, multiplicity-weighted-median} restricted family AND a STAGE-1-CANDIDATE registry-text drafted with substrate-IS prediction value `−1.892 ± 0.02`. FAIL: regulator-axis variance > 0.01 (R_∞ is not an invariant; it's a convention-class-specific prediction). INFO: invariance confirmed but no laboratory-IN candidate identifiable (substrate prediction with no falsifier).
- **Effort**: ~0.6 wave-equivalents (Friedrich-Bär extrapolation + regulator-INVARIANCE cross-check on existing grid + STAGE-1-CANDIDATE registry-text drafting).

### V.4. CF-W3a-ADDITIONAL-B — Cocycle Ratio Sage-Exact L_max-Invariance Cross-Validation

- **What**: §W3a-14 + §W3a-18 verified `cocycle_ratio_67_88 = 7.324974` from canonical pins at L_max=10 (residual 1.76e−05 to canonical Sage-exact 7.324992, within Class 8.3 publication-precision floor 1e−4). §W3a-19 did NOT cross-validate the cocycle ratio across the L_max scan {16, 18, 20}. Sage-exact recompute of the ratio from canonical pins (`cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`) at each L_max in the scan; verify L_max-invariance to publication-precision floor.
- **Inputs**: `canonical_constants.cocycle_norm_phi67`, `cocycle_norm_phi88`, `substrate_cocycle_ratio_67_88`; §W3a-19 sector enumeration code at L_max ∈ {16, 18, 20}.
- **Gate**: `S89-W3A-COCYCLE-RATIO-LMAX-INVARIANCE-CROSS-VALIDATION`. PASS: `|ratio(L) − 7.324992| / 7.324992 ≤ 1e-4` for ALL L ∈ {10, 16, 18, 20} (Class 8.3 publication-precision tol).
- **Effort**: ~0.2 wave-equivalents (single closed-form Sage-exact recompute; no eigenvalue work needed).

### V.5. CF-W3a-ADDITIONAL-D — §W3a-19 verdict-label compound diagnostic separation

- **What**: §W3a-19's INFO-cross-conv-unstable verdict label captures `cross_conv_deviation_at_Lmax20 = 0.5188 ≥ 0.50` but loses the structurally distinct `saturation_Cβ = False` (12.42% step at 16→18) signal. Both signals are positive structural information; the verdict-line schema should carry a compound `verdict_label` for downstream consumers. Hygiene update per `gate-verdicts.md §"S87+ canonical form (Schema-v2)"` companion-row taxonomy: extend the schema to allow `verdict_label = INFO-cross-conv-unstable+NOT-saturation-Cβ` (compound) so W3b synthesis + S89+ planners can disambiguate the two diagnostic axes.
- **Inputs**: §W3a-19 npz output; `gate-verdicts.md §"S87+ canonical form (Schema-v2)"`.
- **Gate**: `S89-W3A-19-COMPOUND-VERDICT-LABEL-SCHEMA-EXTENSION` (METHODOLOGY-class per `wave-classification.md §M1-M4`; orchestrator-direct-write under `gate-verdicts.md` schema discipline).
- **Effort**: ~0.05 wave-equivalents (verdict-line schema decision; no recompute).

### V.6. CF-W3a-ADDITIONAL-C dispatch ordering — RESOLVED IN-WORKSHOP

The seed-W3a CF-W3a-ADDITIONAL-C item ("wave-together vs sequential dispatch structure for the two W3c queue items") is resolved in this synthesis (§IV.1(c) + IV.1(d)): **sequential, V.1 first, V.2 conditional**. The wave-together option (Q3 routing per `Investigating-Workshops.md §"is NOT" item 8`) is rejected because the two gates are not structurally orthogonal — the demarcation theorem's input domain depends on the canonical observable's residual freedom, which is V.1's output. The S89 plan author should pre-register V.1 in early-wave dispatch and V.2 as conditional-on-V.1-result; no carry-forward computation needed beyond this in-workshop decision.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| II.1 | R_substrate sign(−) universal across 5 W11-5-family constructions; R_3HeB_lit sign(+); observable-axis range 0.999 in R-units | GEOMETRIC | CLOSED (substrate-IS layer) | The W11-5 multiplicity-weighted Mellin-pole-window form measures something other than (Δ_A²−Δ_B²)/(Δ_A²+Δ_B²); observable-form redefinition is the structural-fix corridor |
| II.2 | composability_residual = 0.887 ≫ 1e-2 threshold; projects onto observable axis (convention held fixed); 89× past threshold | GEOMETRIC | CONFIRMED (positive structural finding) | ι_*-non-composability is intrinsic to the W11-5 observable form, not the convention; convention demarcation cannot recover composability; volovik priority for W3c queue |
| II.3 | R_∞_B ≈ −1.892 ± 0.01 monotonically L_max-saturated under multiplicity-weighted-median; Cauchy convergence at L_max=18; 54.5× past R_lit magnitude | GEOMETRIC | CANDIDATE substrate-IS invariant (CF-W3a-ADDITIONAL-A queued) | Candidate substrate-IS prediction whose laboratory-IN image is NOT R_3HeB_lit; opens registry §VII.X STAGE-1-CANDIDATE per V.3 carry-forward |
| II.4 | Observable-axis spread 0.999 > convention-axis spread 0.794 R-units; both same OOM, both ≫ R_lit magnitude 0.0354 | GEOMETRIC | CLOSED (priority direction) | Both axes substantial; observable-form structurally PRIOR by composability projection (II.2) and L_max-saturation absence-of-anchor (II.3) |
| IV.1(a) | W11-5 form has L_max-saturation theorem candidate at B convention; predicts NON-3HeB observable | GEOMETRIC | OPEN-QUEUE (V.3 carry-forward) | Substrate-IS prediction independent of FWD-C3 instance #2 framing; routes to V.3 |
| IV.1(b) | composability_residual 0.887 informative AGAINST connes priority (projects onto observable axis) | GEOMETRIC | DECISIVE (volovik priority) | Direction-of-explanation flow falsifies the connes "two cohomology constructions" reading; structural-fix lies at observable level |
| IV.1(c) | Sequential dispatch (V.1 first, V.2 conditional) VS wave-together rejected | METHODOLOGY | DECISIVE | Q3 wave-together fails: V.2 input domain depends on V.1 output; not structurally orthogonal |
| IV.1(d) | W3c-(a) Connes-Karoubi pairing = algebra-INVARIANT (registry-PASS-eligible); W3c-(b) demarcation = algebra-DEPENDENT (orthogonal-companion only) | METHODOLOGY (algebra-axis K-counter MANDATORY at K=3) | DECISIVE | Cross-corner co-primary registry anchors FORBIDDEN; sequential V.1-then-V.2 avoids the violation by construction |
| IV.2 | S86 W1b-T8 inheritance morphism, (Δ_B/Δ_A)^p=0 cancellation, cocycle ratio 7.324992 ALL preserved | GEOMETRIC | PRESERVED (machine + publication precision) | The structural floor is intact; W3a closes 3 fix-corridors at the observable layer without disturbing the inheritance theorem; K-counter unchanged at K=2 |
| V.1 | S89-CONNES-KAROUBI-PAIRING-CANONICAL, ~3 wave-equivalents, dispatched first | PHONONIC + GEOMETRIC | QUEUED (S89+) | Volovik-priority canonical observable on A_K^BdG_preimage; PASS advances K=2→K=3, FAIL falsifies bridge anatomy at cocycle layer |
| V.2 | S89-CONVENTION-DEMARCATION-THEOREM, ~1.5 wave-equivalents, conditional on V.1 residual freedom | METHODOLOGY | QUEUED (CONDITIONAL) | Closed-by-construction at INFO if Connes-Moscovici residue is unique at substrate-distance-1 pole (likely outcome) |
| V.3 | CF-W3a-ADDITIONAL-A: R_∞_B substrate-universal prediction test, ~0.6 wave-equivalents | PHONONIC + GEOMETRIC | QUEUED (S89+) | Independent of FWD-C3 instance #2; potential STAGE-1-CANDIDATE registry entry at §VII.X |
| V.4 | CF-W3a-ADDITIONAL-B: cocycle ratio L_max-invariance Sage cross-validation, ~0.2 wave-equivalents | GEOMETRIC | QUEUED (S89+) | Closes a hygiene gap on §W3a-19's L_max scan; high-confidence PASS expected |
| V.5 | CF-W3a-ADDITIONAL-D: §W3a-19 compound verdict-label schema extension, ~0.05 wave-equivalents | METHODOLOGY | QUEUED (S89+) | Diagnostic-axis separation in verdict-line schema; downstream-consumer disambiguation |
| V.6 | CF-W3a-ADDITIONAL-C: dispatch ordering decision | METHODOLOGY | RESOLVED-IN-WORKSHOP | No carry-forward computation; decision encoded in V.1+V.2 ordering |

---

## VII. Substrate framing — direction-of-explanation summary

The W3a evidence forces the substrate-first reconstruction. The W11-5 multiplicity-weighted Mellin-pole-window observable was an algebra-up construction on A_K with global Peter-Weyl multiplicity weights; it does not flow FROM the canonical Hochschild cocycle on A_K^BdG_preimage that the inheritance morphism ι_* canonicalizes. The substrate IS the spectral triple (single-τ-slice substrate-IS at τ_fold per `phononic-framing.md §"Single-τ-slice"`), and the laboratory-IN measurement of R_3HeB_lit IS the Connes-Karoubi pairing's HKR L_max → ∞ image after ι_* projection. The W3a wave establishes, by closing 3 structural-fix corridors on the W11-5 form and confirming the form's ι_*-non-composability via the 0.887 residual, that no convention or partition on the W11-5 family on A_K can canonicalize the substrate-IS observable that inherits-into R_3HeB_lit. The structural-fix path is to construct the canonical Connes-Karoubi pairing on A_K^BdG_preimage from first principles (V.1), with convention demarcation (V.2) as a downstream conditional. The cross-pillar bridge anatomy at K=2 stands; the K=3 promotion event is contingent on V.1 PASS.

**End of solo synthesis** (volovik-superfluid-universe-theorist; structural verdict: observable-form redefinition structurally PRIOR; Connes-Karoubi pairing canonical first; convention demarcation conditional; algebra-axis classification (a) algebra-INVARIANT registry-PASS-eligible / (b) algebra-DEPENDENT orthogonal-companion; cross-corner co-primary FORBIDDEN; 5 carry-forwards routed for S89+).
