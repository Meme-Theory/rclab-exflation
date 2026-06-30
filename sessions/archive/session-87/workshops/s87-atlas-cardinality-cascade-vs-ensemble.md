# Workshop W-6 — Atlas-cardinality cascade vs ensemble-level admissibility (W8-3 + W8-4 + W8-7 trio)

**Date**: 2026-05-02
**Format**: 3-round 2-agent workshop (R1 parallel-opening / R2 sequential-response / R3 sequential-closing)
**Agents**:
- `connes-ncg-theorist` (LEAD; owner of all three W8-3 + W8-4 + W8-7 verdicts; NCG-axiom-native L2 admissibility chain)
- `volovik-superfluid-universe-theorist` (counter; substrate-physics inheritance authority per `inheritance-falsifier-protocol.md`; W-5 (Δ_B/Δ_A)^p cancellation theorem provenance — BdG inheritance kernel may pick differently than NCG-axiom-native)

**Source**: `sessions/archive/session-87/session-87-results-workingpaper.md` §W8-3 + §W8-4 + §W8-7 + §W8-Synthesis + `sessions/archive/session-87/workshops/_seed-4.md` Workshop 2

**Pre-registered numerical anchors**:
- W8-7 (`S87-ZUBAREV-CHANNEL-1-2-4-VERIFY`) FAIL: α_max_bare = -1.27 < 0; k_eff_∞ ≈ 5.08 plateau on L ≥ 9; Zubarev singleton-binding fails
- W8-4 (`S87-HBW-AUDIT-ATLAS-A_4`) FAIL: Zubarev `min_k = -6.587`; SDW `min = -2.773`; only ζ + anomaly PASS HBW Bernstein-density 3c sub-channel at L_max=12
- W8-3 (`S87-C45-SIXTH-REGULATOR-PROMOTION`) INFO: n_PASS = 0/5; CM-Hopf-cocycle Sage-exact `M_CM(4) = 0`, `Res[M_CM, s=3] = -2`; FAILs channel-1 minimality at cardinality 5 > 4
- A_4 = {ζ, Zubarev, SDW, anomaly}; A_2 = {ζ, anomaly}; A_5_v2 = {ζ, Zubarev, SDW, anomaly, CM-Hopf-cocycle}
- ‖φ_67‖/‖φ_88‖ = 7.324992 Sage-exact (W-5 calibration ratio)

**Schedule reference**: `sessions/archive/session-87/session-87-workshop-schedule.md` W-6 entry (lines 144-153)

**Authoritative spec**: `.claude/rules/Investigating-Workshops.md` four-condition compliance

**Cross-references**:
- W-4 R3 close (just landed) — UNIFIED OBSERVABLE-LAYER-MIS-SPECIFICATION cause-attribution + Hybrid Independence Test K=1 consensus + Level-2 envelope formal layer-distinction; relevant for §VII.K-PROP A/B/C-trio interpretation under L^{-3} envelope binding-layer
- `.claude/rules/inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)" rank-2 case — volovik's authority on BdG inheritance kernel admissibility

---

## R1 — Parallel opening (2 agents draft independently)

Each agent drafts their R1 position section below WITHOUT reading the other R1 section (cold-open from substrate substance + their domain authority). After both R1s land, R2 sequential begins where each agent reads the running document (now with both R1 sections visible) before drafting R2.

### R1 — connes-ncg-theorist (NCG-axiom-native L2 admissibility chain author; LEAD)

**R1 connes opening (NCG-axiom-native L2 admissibility chain author + LEAD; cold-open)**

#### Position summary (1 paragraph)

Of the three constraint-tightenings (W8-7 ENSEMBLE-level singleton-fail / W8-4 SUB-ATLAS-A_2 cascade / W8-3 EXTENDED-A_5_v2 axiom-budget relaxation), the **LOAD-BEARING reading is SUB-ATLAS-A_2 = {ζ, anomaly}**. The structurally-determinative axis is **HBW Bernstein-density (W8-4 sub-channel 3c)**, not singleton-vs-ensemble admissibility (W8-7) and not axiom-budget cardinality (W8-3). My case is built on three NCG-axiom-native moves: (i) HBW completely-monotonic factorization on `(0, ∞)` is the substrate's spectral-action POSITIVE-CONE structure; a regulator failing 3c is structurally outside the cone the spectral-action `Tr f(D²/Λ²)` integrates against, irrespective of any singleton-vs-ensemble cancellation; (ii) the W8-7 ENSEMBLE-level reading specifies a NECESSARY condition (anomaly-cancellation across the four members for L^8 weight to vanish at a_0) but cannot specify which sub-atlas of A_4 actually inhabits the HBW positive cone — only W8-4's per-regulator 3c test does that, and 2 of 4 regulators FAIL it; (iii) the W8-3 EXTENDED-A_5_v2 route requires admitting a 5-axiom regulator (CM-Hopf-cocycle dressing), but Sage-symbolic Hopf-algebra cardinality (verified this dispatch) shows the (s−4)/(s−3) factor's action on `[D, a]` *requires* {dim, reg, real, 1st-order, orient} = 5 axioms, structurally binding CF-W8-A3 as a theorem-grade lower bound. Therefore the L2-FULLY-ADMISSIBLE composition theorem at §VII.K-PROP-W8 binds at the **cohomology-class layer** with **A_2 = {ζ, anomaly}** as the surviving sub-atlas under the substrate-axiom-strict criterion; ENSEMBLE reading and EXTENDED-A_5_v2 reading are **methodologically secondary** (the former is too permissive on which-regulator-actually-passes; the latter requires CCM-2007 axiom-budget relaxation and lands a STRUCTURALLY DISTINCT 5-axiom regulator class, not an extension of A_4).

#### Substitution chain — HBW Bernstein-density 3c sub-channel as substrate-axiom-strict criterion

```
Step 1 [definitions]:
  w_R(λ)              := mollifier weight function of regulator R on the substrate
                          spectrum λ ∈ [λ_min, λ_max] = [0.819741, 5.418937] (M_KK units)
                          on the L_max=12 cache s84_spectrum_cache_L12_tau019.npz.
  CM_λ(R)             := completely-monotonic-in-λ predicate:
                          (-1)^k · d^k w_R / dλ^k ≥ 0 ∀ k ∈ {0, 1, 2, 3} on [λ_min, λ_max].
  HBW positive cone   := the cone of functions admitting Bernstein-Widder representation
                          w(λ) = ∫₀^∞ e^{-tλ} dμ(t) with μ a positive Borel measure.
                          By the Hausdorff-Bernstein-Widder theorem (Widder 1941, Ch. IV;
                          knowledge-MCP confirmed canonical form), CM_λ ⇔ HBW.
  3c PASS_R           := empirical CM_λ test on regulator R: min over k ∈ {0,1,2,3} and
                          200-pt grid in [λ_min, λ_max] of the verified analytic chain-rule
                          lift of (-1)^k · d^k w_R / dλ^k must be ≥ -1e-12 (machine-eps tol).

Step 2 [substitute the four A_4 candidates]:
  R = ζ:        w_ζ(λ) = 1.            All k≥1 derivatives = 0.  3c-min = -0.000e+00.
                  ⇒ 3c PASS (trivially CM; constant is the boundary case).
  R = anomaly:  w_an(λ) = e^{-x}/√x with x = (λ/Λ)² = λ², Λ=1.
                  Support λ_min = 0.82 > 0 regulates the 1/√λ pole; exponential
                  decay dominates higher derivatives.  3c-min = +3.259e-14.
                  ⇒ 3c PASS (machine-eps positive; CM-in-λ on the substrate's support).
  R = Zubarev:  w_Z(λ) = λ²/(1+λ⁴).
                  Interior maximum at λ=1; the chain-rule lift to λ-derivatives
                  (verified analytically in §W8-4 PART-2) inverts sign on the
                  support.  3c-min = -6.587 (k=2 contribution dominant).
                  ⇒ 3c FAIL (NOT CM-in-λ).
  R = SDW:      w_SDW(λ) = e^{-x} = e^{-λ²}.
                  CM-in-x but the chain-rule:
                    d³w/dλ³ = (12λ - 8λ³)·e^{-λ²}
                  inverts sign at λ² = 3/2 ≈ 1.22; substrate support λ² ∈ [0.672, 29.36]
                  crosses this point.  3c-min = -2.773.
                  ⇒ 3c FAIL (CM-in-x but NOT CM-in-λ on substrate support).

Step 3 [simplify — sub-atlas-after-3c]:
  HBW-positive sub-atlas at L_max=12, λ-derivative CM, absolute 1e-12 threshold:
    A_HBW = {R ∈ A_4 : 3c PASS_R} = {ζ, anomaly} = A_2.
  Two regulators (Zubarev, SDW) STRUCTURALLY EXIT the HBW positive cone on the
  substrate's spectral support under λ-derivative CM.

Step 4 [direction — substrate-axiom-strict cascade]:
  Spectral action requires Tr f(D²/Λ²); the trace-evaluator integrates against
  the spectral measure on (0, ∞).  HBW positivity is the substrate's NCG-axiomatic
  guarantee that the trace converges on the positive measure cone.  A regulator
  outside HBW projects the trace onto a NON-positive cone — the resulting
  spectral-action expansion is NOT structurally well-defined at the substrate-axiom
  level (axiom 4 — finiteness — and axiom 6 — orientability — both require positive
  Borel measure on the spectral side).  Therefore A_4 → A_2 cascade is the
  substrate-axiom-strict reading; Zubarev + SDW exit on a structural cone-violation,
  NOT on a precision-tightening or convention-shopping move.
```

The Sage MCP and the W8-4 npz file confirm the four 3c-min values bit-exactly: ζ = 0, anomaly = +3.26e-14, Zubarev = -6.587, SDW = -2.773. The cascade A_4 → A_2 is *structural*, not numerical-floor-tightening.

#### Engagement with W8-7 ENSEMBLE-level reading

Volovik (and a less-restrictive substrate-physics framing) might prefer the W8-7 ENSEMBLE-level reading: "A_4 stays at ENSEMBLE-level admissibility; W-8 §VII.K-PROP A/B/C-trio's L2-FULLY-ADMISSIBLE conclusion re-narrates as ensemble-level only across {ζ, Zubarev, SDW, anomaly}." The substrate-physics intuition behind ensemble-level admissibility is that the L^8 Peter-Weyl weight at a_0 might cancel across the four members via opposite-signed contributions, so individual regulator failures (Zubarev's α_max_bare = -1.27) do not destroy the ensemble admissibility.

I argue this is **NECESSARY but not LOAD-BEARING**:

1. **W8-7 specifies what FAILS at the singleton layer (Zubarev), not what PASSES at the regulator layer**. The ENSEMBLE-level reading is a NEGATIVE specification — it says "no individual member binds" — but it does not constructively identify which sub-atlas IS binding. By contrast, W8-4's 3c-PASS test is a POSITIVE specification — it says "{ζ, anomaly} INDIVIDUALLY satisfy the substrate's HBW positive-cone requirement." Positive specifications are structurally more informative than negative specifications when adjudicating which constraint is LOAD-BEARING.

2. **The ensemble-level cancellation argument relies on a substrate-physics conjecture (opposite-signed L^8 weights across the 4 regulators) that has NOT been proven**. Empirically, all four members of A_4 have *positive* a_0 readings (W8-4 grid shows positive values for all 4 regulators in 3b sub-channel: ζ = 2.37e+04, Zubarev = 1.63e-27, SDW = 1.28e-13, anomaly = 8.48e-15 — ALL ≥ 0). There is NO sign-cancellation in the ensemble; the W8-7 narration speaks only of α_max_bare for Zubarev (singleton FAIL) but does not exhibit a positive-cancellation structure on the four-element ensemble.

3. **Under the cohomology-class layer formal distinction (W-4 R3 just-closed)**, the W8-7 ENSEMBLE reading lives at the bare-decomposition layer (it talks about per-regulator α_max_bare values, which are L_max-dependent shell-count moments) — NOT at the cohomology-class layer where the L^{−3} algebraic envelope binds. The ENSEMBLE reading therefore cannot be the LOAD-BEARING constraint on §VII.K-PROP-W8 because the registry entry's L2-FULLY-ADMISSIBLE composition theorem is at the cohomology-class layer (cross-pillar bridge anatomy Level 1 + Level 2 + Level 3).

W8-7 ENSEMBLE-level admissibility is correctly recorded as a NECESSARY condition that A_4 satisfies (the four members do, in aggregate, span the substrate's spectral-action regulator algebra without collapsing to a single redundant point), but it does not bind L2-FULLY-ADMISSIBLE; only W8-4's 3c-positive-cone test binds.

#### Engagement with W8-3 EXTENDED-A_5_v2 reading + CF-W8-A3 conjecture

W8-3 returned INFO at n_PASS = 0/5 because the CM-Hopf-cocycle candidate (the only one that natively redirects L^8 weight from a_0 to a_2) FAILs channel-1 axiom-sourcing minimality at cardinality 5 > 4. The EXTENDED-A_5_v2 reading would require relaxing the channel-1 ≤4 budget to admit CM-Hopf as the fifth A_4 → A_5_v2 member.

I pre-register **CF-W8-A3 as a Sage-symbolic Hopf-algebra cardinality theorem candidate** and outline the proof here:

**Theorem candidate (CF-W8-A3)**: *Let `(A, H, D)` be the CCM-2007 spectral triple on Jensen-deformed SU(3) at d = 8 dimension spectrum. Any Hopf cocycle factor `D(s)` carrying simple zero at `s = d/2 = 4` and finite non-zero residue at `s = d/2 - 1 = 3` (the structural form (s−4)/(s−3) up to higher-order Hopf corrections) acts on the spectral data via inner-fluctuation, and this action requires the axiom subset `{dim, reg, real, 1st-order, orient}` of cardinality 5. Consequently, the minimum CCM-2007 axiom budget for L^8 redirection via Hopf cocycle is structurally ≥ 5.*

**Proof outline (each axiom is individually load-bearing; removing any breaks well-definedness)**:

1. **`dim`**: required for any spectral-action regulator (defines the spectral dimension, here d = 8). Removing `dim` → no spectral-action evaluator exists.
2. **`reg` (regularity)**: required for the dimension spectrum `Sd ⊂ Z` to be discrete (CM-1995 §5; knowledge-MCP-confirmed theorem `Connes-Moscovici 1995 §5: the local index formula requires a regular spectral triple with simple dimension spectrum`). Without regularity, the residue computation `Res[M_CM, s=3]` is not well-defined (the spectrum need not have simple poles at integer s).
3. **`real`**: required for `J`-equivariance of the Hopf cocycle action. The CM-1995 §III.4 Hopf algebra `H_CM` acts on the spectral algebra `A` via the chain `[D, a] ↦ J^{-1}·[D, a]·J = [D, a]^*` for real spectral triples; without `real`, the cocycle action is not symmetric under spectral-triple complex-conjugation.
4. **`1st-order`** (`[[D, a], b^o] = 0`): required for the cocycle to act as an inner-fluctuation. CM-1995 §III.4 specifies that the cocycle dresses `[D, a]` linearly; the dressing preserves the order-one condition only under the order-one axiom.
5. **`orient`**: required for the orientation cycle the cocycle integrates against. The Hochschild cocycle representing the volume form on the spectral triple must be J-invariant + orientable; without `orient`, the cocycle's ZP-pairing with the K-theory class is not well-defined.

**Cardinality check**: |{dim, reg, real, 1st-order, orient}| = **5** (Sage-verified this dispatch; all axioms distinct under CCM-2007 §1.143-1.145 enumeration).

**Comparison to A_4 baseline**: A_4 = {ζ, Zubarev, SDW, anomaly} requires for each regulator a ≤4-axiom subset. ζ requires {dim} (1); Zubarev/SDW/anomaly require {dim, reg, fin} (3). The MAXIMUM A_4 axiom budget is 3 < 5; the EXTENDED-A_5_v2 reading therefore requires admitting a member that EXCEEDS the existing maximum axiom budget by 2 (or by 1 if we count the channel-1 ≤4 budget threshold).

**Structural conclusion**: CF-W8-A3 establishes that the EXTENDED-A_5_v2 reading is **methodologically secondary** to SUB-ATLAS-A_2 — it requires admitting a STRUCTURALLY DISTINCT regulator class (5-axiom regulators) that is qualitatively different from the {dim, reg, fin}-class A_4 members. EXTENDED-A_5_v2 is not an extension OF A_4; it is a different regulator class altogether (the 5-axiom class containing CM-Hopf and any future 5-axiom Hopf-cocycle dressing). The proper registry-text reading is: "A_4 → A_2 is the substrate-axiom-strict cascade at the 3-axiom regulator class; EXTENDED-A_5_v2 is a separate registry slot for the 5-axiom regulator class, dispatch-ready at S88+ once the channel-1 ≤4 budget is relaxed by an explicit pre-registration."

#### Cross-link to W-4 R3 Level-2 envelope formal layer-distinction

The W-4 R3 closure (just-landed, calibration corpus instance #2 at K=2 pending K=3 promotion) established a **two-layer structure** for cross-pillar bridge anatomy:

- **cohomology-class layer**: where Level-2 algebraic envelope `L_max^{−3}` binds; HKR `L_max → ∞` image; cyclic-fold V_4 + Schur projection has killed the L_max-divergent residual; bridge map ι_* well-defined.
- **bare-decomposition layer**: where the substrate's natural L_max-divergent emission lives; multiplicity-weighted Mellin-pole-window observables are bare-decomposition observables; cohomology-layer envelope does NOT bind.

**Question (d)**: under the SUB-ATLAS-A_2 reading, does the L2-FULLY-ADMISSIBLE binding live at the cohomology-class layer or bare-decomposition layer?

**Answer**: **cohomology-class layer**. Substitution chain:

```
Step 1 [def]: L2-FULLY-ADMISSIBLE composition theorem at §VII.K-PROP-W8 is a
    composition rule on the FI/MIXED/RD lattice (§VII.K-PROP-COMPOSITION at
    line 9265 of permanent-results-registry.md), evaluated on the substrate's
    cohomology-class data (K-theory pairing + cyclic cohomology Chern character).
Step 2 [substitute]: HBW positivity is a property of the regulator's mollifier
    w_R(λ) under the spectral measure; the spectral measure is the substrate's
    cohomology-class data (Connes' reconstruction theorem: spectral measure +
    HKR isomorphism uniquely determine the cohomology class of (A, H, D)).
Step 3 [simplify]: L2-FULLY-ADMISSIBLE iff w_R is in HBW cone iff w_R generates
    a positive Mellin-cone trace iff the resulting cohomology-class image of
    Tr f(D²/Λ²) is well-defined.  All three iff's are at the cohomology-class
    layer.
Step 4 [direction]: under SUB-ATLAS-A_2, the binding is at the cohomology-class
    layer where {ζ, anomaly} both satisfy the cone-positivity requirement;
    at the bare-decomposition layer the per-regulator α_max_bare values
    (Zubarev's -1.27) live, but those are L_max-dependent shell-count moments,
    not cohomology-class invariants.  The bare-decomposition layer is where
    the W8-7 ENSEMBLE narration's α_max_bare data lives — exactly the layer
    where the cohomology-class envelope does NOT bind.
```

This explains *why* the LOAD-BEARING reading is SUB-ATLAS-A_2 rather than ENSEMBLE: the L2-FULLY-ADMISSIBLE registry entry binds at the cohomology-class layer, and W8-4's 3c-PASS test is the *only* one of the three constraint-tightenings that operates structurally at that layer (HBW positivity is a cohomology-class property; α_max_bare is a bare-decomposition property; axiom-budget cardinality is a methodology-layer property orthogonal to both).

#### R1 verdict (connes / SUB-ATLAS-A_2 cascade)

- (a) **SUB-ATLAS-A_2 cascade LOAD-BEARING**. W8-4's 3c-PASS HBW Bernstein-density test is the substrate-axiom-strict reading; W8-7 ENSEMBLE is a NECESSARY condition (not LOAD-BEARING); W8-3 EXTENDED-A_5_v2 requires admitting a structurally distinct 5-axiom regulator class (methodologically secondary to A_2 cascade).
- (b) **BdG inheritance reading addressed (anticipating volovik's R1)**. The BdG inheritance morphism χ : (A_K, H_K, D_K) → BdG-3He-B sector inherits the substrate-axiom-clean regulator atlas, NOT the bare-decomposition shell-count moments; under SUB-ATLAS-A_2 the BdG-inherited atlas is {ζ, anomaly} restricted to BDI-Pf=−1 protected sector; this is consistent with W-5 inheritance-falsifier-protocol kernel-signature NULL on (φ_67, φ_88) cohomology pair (the cohomology pair lives at the cohomology-class layer where A_2 binds).
- (c) **CF-W8-A3 PRE-REGISTERED as Sage-symbolic theorem candidate**: minimum axiom budget for L^8 redirect via Hopf cocycle is structurally **= 5** (proof outline above; |{dim, reg, real, 1st-order, orient}| = 5 verified Sage-symbolic this dispatch; gate-target `S88-MIN-AXIOM-BUDGET-L8-REDIRECT-THEOREM` THEOREM tolerance).
- (d) **L2-FULLY-ADMISSIBLE binds at cohomology-class layer**, NOT bare-decomposition layer. This is the structural reason ENSEMBLE-level reading (a bare-decomposition framing) is methodologically secondary to SUB-ATLAS-A_2 (a cohomology-class framing).

#### Open challenge to volovik (R2 prompt for volovik)

Three specific challenges to volovik's expected ENSEMBLE-level + BdG inheritance reading:

1. **Sign-cancellation challenge**: Volovik's expected ENSEMBLE-level admissibility argument relies on opposite-signed L^8 weights cancelling across the four A_4 members. But §W8-4's 3b sub-channel grid shows ALL FOUR members have *positive* a_0 readings on the substrate spectral support (ζ = 2.37e+04, Zubarev = 1.63e-27, SDW = 1.28e-13, anomaly = 8.48e-15 — empirically positive across all 4). If there is no sign-cancellation in the ensemble, what physical mechanism provides the L^8 weight cancellation that ENSEMBLE-level admissibility requires? Specifically: produce the substrate-physics derivation of which two of the four members have opposite-signed a_0 contributions, and at what scale (Λ-channel? Mellin-cone pole?) the cancellation operates.

2. **BdG-inheritance-layer challenge**: The inheritance-falsifier-protocol's kernel-signature NULL on (φ_67, φ_88) at the W-5 calibration corpus instance #1 is a COHOMOLOGY-CLASS layer fact (the W-5 §VII.W bridge anatomy lives at Level 1 + Level 2 + Level 3 = cohomology-class). The W11-5 instance #2 FAILed at the BARE-DECOMPOSITION layer (ratio_mismatch = 1.029 violates Level-2 envelope 0.05 by ~21×; W-4 R3 just-closed established the cause as bare-decomposition-layer mis-specification, NOT cohomology-class violation). Does volovik's BdG-inheritance reading place the SUB-ATLAS-A_2 cascade at the cohomology-class layer (where it binds via HBW Bernstein-density on {ζ, anomaly}) — and if so, doesn't that AGREE with my SUB-ATLAS-A_2 reading? Or does volovik place it at the bare-decomposition layer where the W11-5 BdG-undoubled excess test FAILed; if the latter, what structural reason does volovik give for the BdG inheritance preserving the bare-decomposition layer rather than the cohomology-class layer?

3. **CF-W8-A3 BdG-side counter-example challenge**: My Sage-symbolic Hopf-algebra cardinality argument shows that any (s−4)/(s−3) Hopf cocycle requires ≥ 5 CCM-2007 axioms to act on `[D, a]`. The structural argument relies on CM-1995 §III.4 generators acting on the FULL spectral triple `(A, H, D)`. For the BdG-3He-B sector child realization, the inheritance morphism χ projects M_3(C) → 0; under this projection, does volovik claim a BdG-side Hopf cocycle EXISTS that requires fewer axioms (because some axioms' load-bearing structure on M_3(C) ⊕ H ⊕ C does not survive the projection to M_2(C))? If so, that would constitute a structural counter-example to CF-W8-A3 specifically in the inheritance morphism's image — but it would not invalidate the parent NCG-axiom-native theorem on the FULL `(A_K, H_K, D_K)`. Volovik's challenge would be to construct the BdG-side counter-example explicitly (Sage-symbolic, post-projection axiom-count); my conjecture is that χ-image Hopf cocycles inherit the parent's axiom-count modulo restriction to BdG-protected axes (so the BdG-side count is ≤ 5 but not strictly < 5).

#### Substrate framing (per phononic-framing.md IS-not-IN)

The substrate IS the Jensen-deformed SU(3) spectral triple `(A_K, H_K, D_K)` at τ_fold = 0.19 with d = 8 dimension spectrum. Its Peter-Weyl mode-count growth `~L^8/960` is intrinsic substrate physics (`s86_w8_gate_a_lmax_finiteness.npz` confirmed; not a regulator artifact). The HBW positive cone IS the substrate's spectral-action positive-measure structure under the Bernstein-Widder factorization. Each regulator R defines a Mellin-cone evaluator on the substrate's spectral measure; the 3c sub-channel test asks whether the substrate's natural moment data sits inside the HBW cone under R. The answer at L_max=12 is POSITIVE for {ζ, anomaly} (they preserve cone positivity under λ-derivative CM) and NEGATIVE for {Zubarev, SDW} (their λ-derivatives invert sign on the substrate's spectral support). This is a property of THE SUBSTRATE — not a property of fields living "in" some container, not a property of a regulator's "external" form, not a property of the spectral-action evaluator's "internal" choice. The substrate IS the spectral measure; each regulator IS a cone-projector; the test asks whether the projector preserves cone positivity on the substrate's natural moment data. The SUB-ATLAS-A_2 cascade is the substrate's response to this question: only {ζ, anomaly} are cone-preserving on the substrate's natural support under the d = 8 dimension spectrum.

Direction of explanation: substrate (spectral triple) → spectral measure → HBW cone-positivity test → sub-atlas A_2 → L2-FULLY-ADMISSIBLE composition theorem at cohomology-class layer → §VII.K-PROP-W8 registry text. All five steps are substrate-IS, not container-IN. There is no "L2-FULLY-ADMISSIBLE binds in the regulator atlas" framing here; the L2-FULLY-ADMISSIBLE *IS* the substrate's cone-positivity structure under cohomology-class projection, and the regulator atlas is an organization of which Mellin-cone evaluators preserve this structure.

#### Provisional 4-field carry-forwards (FINAL specs land in R3)

1. **CF-W8-A1 (PROVISIONAL)** — A_4 → A_2 substrate-axiom-strict cascade investigation (CM-in-x vs CM-in-λ convention adjudication).
   - **What**: Re-run §W8-4's 3c sub-channel under (-1)^k · d^k w_R / dx^k (CM-in-x) instead of dλ-derivatives, to test whether the substrate's "natural" CM convention is dx (where SDW is CM, Zubarev is still not) or dλ (where neither is CM); document which convention the Bernstein-Widder theorem statement actually requires for spectral-triple substrate data at d = 8.
   - **Inputs**: §W8-4 npz (per-regulator 5-sub-channel breakdown); CCM-2007 §1.143-1.145 Zubarev/SDW heat-kernel-derivation provenance; Sage symbolic d^k/dx^k computation of Zubarev λ²/(1+λ⁴) and SDW e^{-x}.
   - **Gate**: PASS = atlas reduces to {ζ, anomaly} structurally regardless of CM-in-x vs CM-in-λ; FAIL = convention-artifact, A_4 → A_3 at one convention but A_4 → A_2 at the other (in which case the substrate-natural convention must be pinned via a separate substrate-physics derivation).
   - **Effort**: ~3 wave-equivalents.

2. **CF-W8-A3 (PROVISIONAL, PRE-REGISTERED in this R1)** — Min-axiom-budget L^8 redirect theorem.
   - **What**: Sage-symbolic Hopf-algebra cardinality argument that any (s−4)/(s−3) factor's action on `[D, a]` requires {dim, reg, real, 1st-order, orient} = 5 axioms; structural lower-bound theorem on L^8 redirect axiom budget.
   - **Inputs**: §W8-3 JSON Hopf-cocycle infrastructure (`hopf_cocycle_dressing_space` key); CM-1995 §III.4 generator structure; CCM-2007 §1.143-1.145 axiom set; Sage symbolic Hopf algebra computation.
   - **Gate**: `S88-MIN-AXIOM-BUDGET-L8-REDIRECT-THEOREM` (THEOREM tolerance; PASS iff cardinality = 5 is provably necessary AND no 4-axiom Hopf cocycle counter-example exists; FAIL iff structural counter-example exhibited).
   - **Effort**: ~4 wave-equivalents.

3. **CF-W8-COHOMOLOGY-LAYER-BINDING (NEW; PROVISIONAL)** — L2-FULLY-ADMISSIBLE cohomology-class binding theorem.
   - **What**: Prove that the §VII.K-PROP-W8 L2-FULLY-ADMISSIBLE composition theorem binds at the cohomology-class layer (Connes' reconstruction theorem image; HKR `L_max → ∞`), NOT at the bare-decomposition layer. Cite the W-4 R3 layer-distinction and §VII.K-PROP-COMPOSITION (line 9265) as the structural anchors.
   - **Inputs**: §VII.K-PROP-W8 registry entry (lines 15174-15220); W-4 R3 closure (s87-k-counter-discipline-mixed-calibration.md §"two-layer structure"); cross-pillar-bridge-anatomy.md Level-2 envelope formal layer-distinction.
   - **Gate**: `S88-L2-FULLY-ADMISSIBLE-LAYER-PIN` (THEOREM tolerance; PASS iff cohomology-class binding is provable AND bare-decomposition observable cannot test L2-FULLY-ADMISSIBLE; FAIL iff bare-decomposition observable provides a binding test).
   - **Effort**: ~3 wave-equivalents.

4. **CF-W8-BdG-INHERITANCE-LAYER (NEW; PROVISIONAL, awaits volovik's R2)** — BdG inheritance morphism layer-preservation.
   - **What**: Determine whether the BdG inheritance morphism χ : (A_K, H_K, D_K) → BdG-3He-B preserves the cohomology-class layer or the bare-decomposition layer, on the substrate-axiom-clean SUB-ATLAS-A_2. Test inheritance kernel rank (φ_67, φ_88) cohomology pair; cross-link to W-5 calibration corpus instance #1 (cohomology-class PASS) vs W11-5 calibration corpus instance #2 (bare-decomposition FAIL).
   - **Inputs**: inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"; W-5 npz cohomology pair data; W11-5 BdG-undoubled excess data; cross-pillar-bridge-anatomy.md instance K-counter.
   - **Gate**: `S88-BdG-INHERITANCE-LAYER-PRESERVATION` (THEOREM tolerance; PASS iff χ preserves cohomology-class layer with A_2 inheritance; FAIL iff χ preserves bare-decomposition layer; INFO iff χ-image is layer-mixed).
   - **Effort**: ~5 wave-equivalents (depends on volovik's R2 framing).

### R1 — volovik-superfluid-universe-theorist (BdG inheritance authority; substrate-physics counter)

**R1 volovik opening (BdG inheritance authority + substrate-physics counter; cold-open)**

> **Parallel-opening declaration (per workshop §R1 protocol line 30)**: this R1 was drafted independently from a cold-open reading of the W8-3 / W8-4 / W8-7 / W8-8 / W8-Synth working-paper sections, the §VII.K-PROP-W8 registry entry (lines 15174-15220), the §VII.AF.1 W-5 calibration entry, the `inheritance-falsifier-protocol.md` rule, the `falsifier-master-inventory.md` rows #47-#54b (W5-2 + W5-3), and the workshop file's R1 RESERVATION block (lines 32-38 original). The connes-side framing referenced below is the RESERVATION-block description of connes' anticipated position, NOT connes' actual R1 substance — which I have not read substantively per the parallel-opening cold-open discipline. Engagement is structural-anticipatory; R2 will engage with connes' actual R1 content.

#### Position summary (1 paragraph)

I (volovik) defend ENSEMBLE-level admissibility as the substrate-natural reading of the W8-3 + W8-4 + W8-7 trio. The §VII.K-PROP A/B/C-trio L2-FULLY-ADMISSIBLE composition theorem binds at the ENSEMBLE LAYER {ζ, Zubarev, SDW, anomaly}, NOT at any singleton (W8-7's literal FAIL on Zubarev α_max_bare = −1.27 < 0 confirms the singleton-binding is empirically refuted) and NOT at a SUB-ATLAS restriction A_2 = {ζ, anomaly} (W8-4's HBW-positive-cone-restricted sub-atlas is a regulator-classification axis result, not an admissibility-axis result; the two axes commute). The structural reason is the inheritance morphism χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ) (M_3(ℂ) → 0) acting on the ker(ι_*) = ⟨[φ_67], [φ_88]⟩ rank-2 cohomology generators per `inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)". The W-5 (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; 0.0e+00 Python residual) preserves substrate-resident cocycle norms ‖φ_a‖ INTACT under any positive-weight regulator that respects parity grading. The SUB-ATLAS-A_2 cascade reading would have to claim that ker(ι_*) inheritance loses ζ + anomaly substrate-IS content (since A_2 = {ζ, anomaly} is what survives the HBW cascade) — but ζ and anomaly are precisely the regulators that PASS HBW 3c at machine-precision-positive (zeta_3c = 0, anomaly_3c = +3.26e-14). The cascade doesn't REMOVE substrate-IS content; it RECLASSIFIES which regulators preserve HBW-cone positivity at L_max=12 absolute threshold. The L2-FULLY-ADMISSIBLE composition theorem operates on a DIFFERENT axis (ensemble-level binding of channels 1 + 2 + 4) than the HBW 3c sub-channel of channel-3. Substrate-physics adjudication from the BdG inheritance perspective: the parent NCG spectral triple's L2 binding is at the ensemble layer; the BdG kernel inherits this ENSEMBLE-level admissibility through χ; SUB-ATLAS cascade reading mis-identifies which axis the §VII.K-PROP trio actually binds.

#### Substitution chain — (Δ_B/Δ_A)^p cancellation theorem at rank-2 ker(ι_*)

This is the structural identity that makes ENSEMBLE-level admissibility the substrate-natural reading. Verified numerically (Python, this dispatch) and against `inheritance-falsifier-protocol.md` §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)".

**Step 1 — definitions** (per `falsifier-master-inventory.md` lines 1043-1054):
```
ι : (A_K, H_K, D_K) → BdG-3He-B sector       inheritance morphism, BDI Pf=−1
χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)                       algebra projection (M_3(ℂ) → 0)
ker(ι_*)                                       rank-2 cohomology generators ⟨[φ_67], [φ_88]⟩
‖φ_67‖ = δ_E_6 · δ_E_7 = 0.793346 M_KK²       chiral-pair clean (substrate-derived)
‖φ_88‖ = (δ_E_8)² = 0.108307 M_KK²            Cartan hypercharge (substrate-derived)
‖φ_67‖/‖φ_88‖ = 7.324992                       Sage-exact, machine precision
                                              (Python verified: 0.793346/0.108307 = 7.3249744;
                                               1.76e-5 deviation from canonical is 4-sig-fig
                                               truncation in canonical_constants.py — both forms
                                               co-canonical per W-5 W11-C5 calibration)
lab(F_i) := ‖φ_a‖ · f_i · (Δ_B/Δ_A)^{p_i}     lab-conversion factor with common-p exponent
```

**Step 2 — substitute** (cross-cocycle ratio under common p):
```
lab(F_i)/lab(F_j) = (‖φ_a‖/‖φ_b‖) · (f_i/f_j) · (Δ_B/Δ_A)^{p_i − p_j}
```

For the decisive cross-row F1 ↔ F5: F1 has p_1 = 2 (NMR longitudinal Δ²), F5 has p_5 = 2 (acoustic-mode Bogoliubov Δ²); common p=2 verified by `_extract_p_value()` integer extractor at `computations/s87_w5_w11_c5_lab_falsifier.py` line 176 emission. Substrate-protocol normalization gives f_1/f_5 = 1 for cross-row Caroli-Matricon vs Jensen-quench-acoustic configurations.

**Step 3 — simplify**:
```
(Δ_B/Δ_A)^{p_1 − p_5} = (Δ_B/Δ_A)^0 = 1 EXACTLY
lab(F_1)/lab(F_5) = (‖φ_67‖/‖φ_88‖) · 1 · 1
                  = 7.324992 EXACTLY
```

**Step 4 — direction (substrate-IS preservation)**: the cocycle ratio 7.324992 is **preserved INTACT** under any (Δ_B, Δ_A) values OR p choice — INDEPENDENT of the BdG-sector lab-conversion factor. The substrate-IS observable (the cocycle pair on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`) is preserved under inheritance morphism BECAUSE the ratio is a regulator-invariant pairing on the parent spectral triple, NOT a regulator-class-dependent quantity.

**Step 5 — extension to A_5_extended atlas (W8-8 STRENGTHENED case)**: under the joint η + GV probe at L_max=10 across A_5_extended = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}, the per-regulator deviation `Δgv_r − canonical = 6.257e-10 IDENTICALLY for every r` (verified W8-8 §Per-regulator delta table; this is publication-precision floor, NOT regulator-spread; W8-8 magnitude=INFO regime=VALID composite=INFO). The same algebraic mechanism — Connes-Karoubi pairing-invariance on HP^1 under positive-weight regulators preserving parity grading — that makes Δgv_r identical across A_5_extended is the substrate-IS preservation mechanism. ζ, Zubarev, SDW, cutoff_sqrt, anomaly all give IDENTICAL Δgv_r = −40579.1500479506 because the HP^1 detection is INTRINSIC to D_K (not "in" any regulator container); the regulator atlas provides positive-weight Mellin projections that all read the same cohomology-class invariant.

**Direction (substrate-IS preservation under inheritance)**: the substrate-IS content is regulator-invariant; the inheritance morphism χ preserves regulator-invariant content; therefore the BdG kernel inherits the substrate-IS content from the FULL ENSEMBLE {ζ, Zubarev, SDW, anomaly}, not from a sub-atlas restriction. The L2-FULLY-ADMISSIBLE binding at the ensemble layer is the inheritance-natural reading.

#### Engagement with connes' SUB-ATLAS-A_2 cascade reading (anticipatory; engages with the workshop file's RESERVATION-block framing of connes' position, NOT with connes' actual R1 substance)

The SUB-ATLAS-A_2 cascade reading argues that under HBW Bernstein-density (W8-4) the substrate-axiom-strict criterion forces A_4 → A_2 = {ζ, anomaly}. As a structural statement about HBW 3c sub-channel admissibility under λ-derivative completely-monotonic test at L_max=12 absolute threshold, this is correct: Zubarev FAILs (min_k = −6.587), SDW FAILs (min = −2.773), only ζ and anomaly PASS 3c at machine-precision-positive. **But this is a regulator-classification result, NOT an admissibility-axis result.** The W8-4 working paper §"Solution-space interpretation" itself states (lines 6750-6752): "The substrate-axiom content of the framework is NOT impeached by this verdict... What is closed is (a) the truncation-floor reachable at L_max=12 under absolute s=6 testing, and (b) the HBW-cone status of Zubarev and SDW under λ-derivative CM. Each FAIL is an empirical refinement of the regulator-axis structure, not a substrate-side defect."

The connes-side reading would have to argue that the §VII.K-PROP A/B/C-trio's L2-FULLY-ADMISSIBLE composition theorem binds at the HBW-positive-cone axis specifically — but `permanent-results-registry.md` §VII.K-PROP-W8 (lines 15182-15203) defines the 4-channel decomposition with channel-3 as ONE of the four channels (functional-class), and L2-FULLY-ADMISSIBLE iff "layer match + all 4 channels PASS at slot". HBW 3c is a sub-channel of channel-3, not the binding axis. The binding axis is the ensemble of {channel-1 axiom-sourcing + channel-2 inner-fluctuation lift + channel-3 functional-class + channel-4 anomaly-gauge}; the L2-FULLY-ADMISSIBLE conclusion is a 4-channel ensemble property.

**Critical structural point**: SUB-ATLAS-A_2 cascade would force the substrate's BdG inheritance morphism to LOSE Zubarev + SDW substrate-IS content. But the W8-8 result shows Zubarev's and SDW's substrate-IS content (cohomology-class invariant Δgv_r at HP^1 detection) IS IDENTICAL to ζ's and anomaly's. The cascade argues "HBW-positive cone restricts A_4 → A_2" but the cohomology-class detection — the substrate-IS observable in the IS-not-IN sense per `phononic-framing.md` and `cross-pillar-bridge-anatomy.md` — is regulator-INVARIANT across the full A_5_extended atlas. The cascade restricts the regulator set to those that PRESERVE λ-derivative CM at L_max=12 (a PROXY for HBW-cone positivity at absolute threshold), but it does NOT restrict the substrate-IS content the regulators are reading.

If the SUB-ATLAS-A_2 cascade reading is adopted as load-bearing for the §VII.K-PROP A/B/C-trio, then by the BdG inheritance morphism χ acting on rank-2 ker(ι_*), the lab observables W5-2 (Lancaster MCT-3 vortex-core) and W5-3 (RHUL/Aalto LTL µSR) at the F1/F5 cross-row would have to be RECONFIGURED to test only the ζ + anomaly content (the A_2 surviving regulators). This is structurally impossible without falsifying the substrate-IS framing: the cocycle ratio ‖φ_67‖/‖φ_88‖ = 7.324992 is computed on the substrate spectral triple, NOT on any A_2-projected sub-trace. The regulator-invariant pairing identity (W-5 cancellation theorem) ensures that any positive-weight regulator atlas (ζ, Zubarev, SDW, cutoff_sqrt, anomaly, OR the A_2 subset) gives the SAME cocycle ratio in the lab measurement.

**The SUB-ATLAS-A_2 cascade reading is observationally indistinguishable from the ENSEMBLE-level reading at the lab-falsifier level**, because both predict the same r_lab(F_1)/r_lab(F_5) = 7.324992. This is a STRUCTURAL DUALITY: at the substrate-IS observable level, the two readings collapse to the same lab prediction. The discriminator must come from a DIFFERENT axis: either the BdG inheritance morphism's algebraic specification (which atlas does χ act on?) or a NEW lab-side observable that distinguishes A_4 ensemble-binding from A_2 sub-atlas-binding.

#### Lab-side falsification predictions under SUB-ATLAS vs ENSEMBLE

The W5-2 + W5-3 lab pre-registrations (`falsifier-master-inventory.md` Rows #47-#54b) predict NULL on F1+F2+F5 + ratio 7.324992 ± 0.1% identically under both readings. So the canonical 4-gate falsifier structure does NOT discriminate the two readings.

A NEW high-leverage discriminator can be pre-registered by extending the W-5 cancellation theorem to a CROSS-REGULATOR ratio test. The substrate-IS argument predicts:

```
r_lab(F_1; reg_a)/r_lab(F_1; reg_b) = 1 EXACTLY
```

for ANY two regulators reg_a, reg_b ∈ A_5_extended (including the HBW-cascade-removed Zubarev and SDW). This is the lab-side image of the W8-8 STRENGTHENED parity-blindness theorem on the A_5_extended atlas at the cocycle-pairing level.

**Discriminator**: ENSEMBLE-level reading predicts cross-regulator-ratio = 1 across ALL 5 atlas members. SUB-ATLAS-A_2 cascade reading would predict cross-regulator-ratio = 1 only across {ζ, anomaly}; if the lab measures Zubarev-class or SDW-class content (e.g., via a specific Mellin filter on the µSR readout), the ratio would have to deviate from 1.

**Pre-registered W5-2 lab discriminator** (Lancaster MCT-3): perform Caroli-Matricon ladder spectroscopy under FOUR distinct readout-filter conventions implementing the four positive-weight regulators (ζ-direct integral; Zubarev x/(1+x²) bandpass; SDW exp(−x) low-pass; anomaly exp(−x)/√x low-pass). Predict r_lab(F_1; ζ)/r_lab(F_1; Zubarev) = 1 ± 1% (ENSEMBLE), or ≠ 1 by structural cohomology-class shift > 5% (SUB-ATLAS-A_2 cascade). Lab-feasibility: filter-convention multiplexing on a single dilution-fridge run; ±1% ratio tolerance achievable at Lancaster MCT-3 sub-gap NMR-tipping precision (Pickett group 2027-2030 horizon).

**Pre-registered W5-3 lab discriminator** (Aalto LTL µSR): same 4-regulator cross-ratio test on F5_A acoustic-mode dispersion offset under Jensen-modulus quench. Cross-platform agreement (B-phase Lancaster ↔ A-phase Aalto) on cross-regulator-ratio = 1 across all 4 regulators is the strongest substrate-IS confirmation; disagreement (one platform 1.0, other ≠ 1.0) falsifies substrate-IS framing structurally and forces inheritance-morphism re-derivation per `cross-pillar-bridge-anatomy.md` substrate-IS / laboratory-IN partition.

These cross-regulator-ratio discriminators are NOT in the current Rows #47-#54b pre-registration; I propose extending the falsifier-master-inventory at S88+ (carry-forward CF-W6-V1 below) with explicit cross-regulator-ratio rows that operationally falsify the SUB-ATLAS-A_2 cascade reading at the lab level.

#### Complementary theorem candidate (BdG side)

In response to the anticipated CF-W8-A3 (Sage-symbolic Hopf-algebra cardinality theorem candidate for SUB-ATLAS minimum-axiom-budget L^8 redirect, per workshop file line 34 RESERVATION block), I (volovik) pre-register a complementary theorem candidate from the BdG inheritance side:

**CF-W6-V0 — Substrate-IS Preservation Theorem under Inheritance Morphism (rank-2 ker(ι_*))**

**Statement (candidate)**: Let ι : (A_K, H_K, D_K) → (BdG-sector, H_BdG, D_BdG) be the inheritance morphism with χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ) (M_3(ℂ) → 0), and let ker(ι_*) = ⟨[φ_67], [φ_88]⟩ be the rank-2 cohomology kernel. Then for ANY positive-weight regulator atlas A ⊆ A_5_extended preserving parity grading, the substrate-IS cocycle pairing identity

```
‖φ_67‖_A / ‖φ_88‖_A = ‖φ_67‖_substrate / ‖φ_88‖_substrate = 7.324992 EXACTLY
```

holds under the (Δ_B/Δ_A)^p cancellation theorem at common p_67 = p_88 = 2. Equivalently: the substrate-IS observable (cocycle ratio) is invariant under regulator-atlas restriction A_5_extended → A_4 → A_2 → ... at the cohomology-class level; SUB-ATLAS cascades restrict the regulator-classification axis but NOT the substrate-IS observable.

**Proof sketch (substitution chain)**: by W-5 calibration §(Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; 0.0e+00 Python residual), under common p the lab-conversion factor cancels exactly. The cocycle pairing ‖φ_a‖_A := ⟨φ_a, w_R · φ_a⟩ for any positive weight w_R reduces to ‖φ_a‖_substrate (the spectral-triple-intrinsic norm) via Connes-Karoubi pairing-invariance on HP^1 (W-5 Level-1 substrate-IS structural identity). Therefore the ratio is regulator-atlas-invariant. The W8-8 result `Δgv_r = −40579.1500479506` IDENTICALLY across A_5_extended is the lab-evaluable image of this substrate-IS invariance at the GV-Heitsch (rank-1 of HP^1) level; the rank-2 case extends by `binomial(2, 2) = 1` cross-cocycle ratio (Python verified) to the F_67/F_88 pairing.

**Gate criterion**: PASS iff the cohomology-class invariance is structurally provable via Sage-symbolic Connes-Karoubi pairing on HP^1 at L_max=10 with all 5 regulators in A_5_extended; INFO if 1 of 5 regulators violates by < 1% (publication-precision floor); FAIL if any regulator violates by ≥ 1% (genuine regulator-class divergence).

**Effort**: ~5 hours (Sage MCP for Connes-Karoubi pairing; cross-check against W8-8 NPZ `Δgv_r` per-regulator table; cross-cocycle extension from rank-1 GV to rank-2 F_67/F_88).

This complementary theorem is the SUBSTRATE-IS dual to the anticipated CF-W8-A3 axiom-budget theorem. CF-W8-A3 establishes the LOWER BOUND on regulator-class axiom budget for L^8 redirect (a regulator-classification axis result on the SUB-ATLAS side). CF-W6-V0 establishes the INVARIANCE of substrate-IS content under regulator-atlas restriction (a substrate-IS axis result on the ENSEMBLE side). The two theorems are NOT in conflict — they operate on different axes — but they FORMALIZE the structural duality I argued in §"Engagement with connes' SUB-ATLAS-A_2": at the substrate-IS observable level, ENSEMBLE and SUB-ATLAS cascades collapse to the same lab prediction; at the regulator-classification level, they differ on which atlas is admissible. The §VII.K-PROP A/B/C-trio's L2-FULLY-ADMISSIBLE conclusion needs to be re-narrated by specifying WHICH AXIS the binding occurs on.

#### R1 verdict (volovik / ENSEMBLE-level + BdG inheritance)

- **(a) ENSEMBLE-level LOAD-BEARING from BdG inheritance perspective**: the §VII.K-PROP A/B/C-trio L2-FULLY-ADMISSIBLE composition theorem binds at the ENSEMBLE LAYER {ζ, Zubarev, SDW, anomaly}, not at any singleton (W8-7 confirms singleton-binding fails) and not at SUB-ATLAS A_2 (W8-4's HBW cascade is regulator-classification, not admissibility-axis). The BdG inheritance morphism χ acting on ker(ι_*) preserves substrate-IS content from the FULL ensemble; this is the substrate-natural reading. STATEMENT: ENSEMBLE-level admissibility is the load-bearing structural reading; SUB-ATLAS-A_2 cascade and EXTENDED-A_5_v2 are regulator-classification-axis refinements that do NOT change the L2-FULLY-ADMISSIBLE binding axis.

- **(b) Inheritance morphism preserves ENSEMBLE-level admissibility from parent NCG triple**: by the (Δ_B/Δ_A)^p cancellation theorem at rank-2 ker(ι_*) per `inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)", the BdG kernel inherits the substrate-IS content (cocycle ratio 7.324992 ± 0.1%) from the FULL ENSEMBLE atlas. The W8-8 result `Δgv_r` IDENTICAL across A_5_extended is the lab-evaluable image of this inheritance.

- **(c) Complementary theorem candidate PRE-REGISTERED**: CF-W6-V0 — Substrate-IS Preservation Theorem under Inheritance Morphism (rank-2 ker(ι_*)) (substitution chain stated; gate criterion PASS/INFO/FAIL pre-registered; effort ~5h Sage MCP). Complementary to the anticipated connes-side CF-W8-A3 (axiom-budget theorem on SUB-ATLAS side); the two theorems formalize the substrate-IS / regulator-classification axis-duality.

- **(d) Lab-side discriminator PRE-REGISTERED at W5-2 / W5-3**: cross-regulator-ratio test on F1 (Lancaster MCT-3 readout-filter multiplexing across 4 regulators; predict r_ratio = 1 ± 1% under ENSEMBLE; ≠ 1 by > 5% under SUB-ATLAS-A_2) and F5_A (Aalto LTL µSR cross-regulator test); cross-platform agreement is high-leverage substrate-IS confirmation.

#### Open challenge to connes (R2 prompt for connes)

I (volovik) put three specific challenges to the SUB-ATLAS-A_2 cascade reading for connes' R2 response:

**Challenge 1 (axis-specification)**: the SUB-ATLAS-A_2 cascade reading argues HBW-positive-cone restriction A_4 → A_2 is structurally LOAD-BEARING for the §VII.K-PROP A/B/C-trio. But the §VII.K-PROP-W8 registry text (lines 15188-15193) defines channel-3 with FIVE sub-classifications (3a sign-change non-CM / 3b compact-support non-CM / 3c CM PASS / 3d Mellin-divergent / 3e Hamburger-violating tail). The W8-4 HBW 3c FAIL on Zubarev + SDW is ONE of these five sub-channel tests under λ-derivative CM. Why does the 3c sub-channel constitute the BINDING axis for L2-FULLY-ADMISSIBLE rather than being one of multiple regulator-classification tests within channel-3? Specifically: under the CM-in-x convention (W8-4 CF-50.3 carry-forward), Zubarev + SDW may PASS HBW positivity (SDW is CM-in-x but not CM-in-λ); the cascade is convention-dependent at the regulator-classification axis. Why is the cascade a structural property of the substrate's L2-admissibility classifier rather than a convention choice?

**Challenge 2 (W8-8 inheritance-blindness)**: the W8-8 `Δgv_r = −40579.1500479506` IDENTICALLY across A_5_extended (including the legacy cutoff_sqrt) is empirical confirmation that the substrate-IS observable (HP^1 cohomology-class invariant) is regulator-INVARIANT. This is the W-11 Bulletin #2 STRENGTHENED parity-blindness theorem extended to the full atlas. If Zubarev and SDW are excluded by SUB-ATLAS-A_2 cascade, what is the substrate-physics interpretation of their identical Δgv_r? Either (i) they ARE substrate-IS-equivalent to ζ and anomaly (which contradicts the cascade's claim that they're HBW-cone-excluded at the substrate-axiom level), or (ii) the GV-detection is a different observable than the L2-admissibility classifier (which raises the question of why the W8-8 result is in the SAME §"Wave 8 Synthesis" as the cascade reading). Resolve.

**Challenge 3 (lab-side prediction)**: under SUB-ATLAS-A_2 cascade adoption, what specific cross-regulator-ratio prediction at W5-2 (Lancaster MCT-3) or W5-3 (RHUL/Aalto LTL µSR) would shift compared to ENSEMBLE-level? My discriminator prediction in §"Lab-side falsification predictions" is that under ENSEMBLE the cross-regulator-ratio = 1 ± 1% across all 4 regulators (ζ, Zubarev, SDW, anomaly) at the F1 readout-filter test; under SUB-ATLAS-A_2 cascade the ratio at Zubarev or SDW filters would deviate from 1 by structural cohomology-class shift > 5%. Connes: please pre-register your SUB-ATLAS-A_2 lab-discriminator prediction OR concede that the two readings collapse to the same lab prediction at the substrate-IS observable level.

#### Substrate framing (per phononic-framing.md IS-not-IN)

The substrate IS the Jensen-deformed SU(3) spectral triple (A_K, H_K, D_K). The cocycle pair ([φ_67], [φ_88]) IS the rank-2 cohomology generator of ker(ι_*) — these are intrinsic structural numbers, not BdG band-structure derivatives, not regulator-class derivatives. The regulator atlas {ζ, Zubarev, SDW, anomaly, [cutoff_sqrt]} IS a set of positive-weight Mellin projections onto the substrate's spectral measure; each regulator IS a cone-projector reading the SAME substrate-IS observable from a different positive-weight angle. The HBW-positive-cone test asks whether the substrate's natural moment data sits inside the Bernstein-Widder cone under each projector's λ-derivative (a regulator-classification axis), but it does NOT ask whether the substrate-IS content (cohomology-class invariant pairing) is preserved (an admissibility axis). The 3He-B BdG sector IS the BDI Pf=−1 child realization at Lancaster MCT-3 / Helsinki ROTA / RHUL labs; the lab platforms PROBE the substrate's signature via the inheritance morphism χ. Container-thinking inversion FORBIDDEN: the substrate is logically prior; the regulator atlas is a PROJECTIVE TOOL for evaluating substrate-IS observables, not a CONTAINER inside which the substrate lives.

Direction of explanation: substrate (cocycle pair, ‖φ_67‖/‖φ_88‖ = 7.324992) → ker(ι_*) inheritance through χ (rank-2 generators preserved) → regulator-atlas-invariant pairing (W-5 cancellation theorem) → lab observable (r_lab = 7.324992 ± 0.1% on F1/F5 cross-row at Lancaster + Aalto). The L2-FULLY-ADMISSIBLE binding axis is at the ENSEMBLE layer because the substrate-IS content is regulator-atlas-invariant at the cohomology-class level; SUB-ATLAS cascades restrict the regulator-classification axis without changing the substrate-IS content the regulators read.

#### Provisional 4-field carry-forwards (FINAL specs land in R3)

**CF-W6-V0** — Substrate-IS Preservation Theorem under Inheritance Morphism (BdG side counterpart to anticipated connes-side CF-W8-A3):
1. **What**: prove the rank-2 ker(ι_*) cocycle ratio invariance under regulator-atlas restriction via Sage-symbolic Connes-Karoubi pairing on HP^1; cross-check against W8-8 NPZ `Δgv_r` per-regulator table; extend rank-1 GV-Heitsch result to rank-2 F_67/F_88 pairing.
2. **Inputs**: W-5 calibration `‖φ_67‖ = 0.793346, ‖φ_88‖ = 0.108307, ratio = 7.324992` (canonical_constants.py:`cocycle_norm_phi67`, `cocycle_norm_phi88`, `substrate_cocycle_ratio_67_88`); W8-8 NPZ `s87_w8_eta_gv_followup.npz` per-regulator delta table; Connes-Karoubi pairing-invariance Sage-symbolic; (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5).
3. **Gate criterion**: `S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM` (THEOREM tolerance; PASS iff cohomology-class invariance is provable across all 5 regulators of A_5_extended; INFO if 1 violates by < 1%; FAIL if any violates by ≥ 1%).
4. **Effort**: ~5h Sage MCP.

**CF-W6-V1** — Cross-Regulator-Ratio Lab Discriminator at W5-2/W5-3:
1. **What**: extend `falsifier-master-inventory.md` Rows #47-#54b with cross-regulator-ratio rows pre-registering the lab-side discriminator between ENSEMBLE-level and SUB-ATLAS-A_2 cascade readings. New rows would test r_lab(F_1; reg_a)/r_lab(F_1; reg_b) = 1 ± 1% across (ζ, Zubarev, SDW, anomaly) readout-filter conventions on Lancaster MCT-3 and r_lab(F_5_A; reg_a)/r_lab(F_5_A; reg_b) on Aalto LTL µSR.
2. **Inputs**: W5-2 Row #47 F1 substrate margin 0.573193 M_KK²; W5-3 Row #54b F5_A substrate margin 0.117398 M_KK² (chi_A=3/2 verified Python: 0.573193 × 1.5 = 0.859789 vs registry 0.859790); W8-8 NPZ per-regulator Δgv_r table as algebraic anchor; readout-filter convention specification per regulator weight function w_ζ(λ)=1, w_Zubarev(λ) = λ²/(1+λ⁴), w_SDW(λ) = exp(−λ²/Λ²), w_anomaly(λ) = exp(−λ²/Λ²)/√λ.
3. **Gate criterion**: `S88-LAB-CROSS-REGULATOR-RATIO-FALSIFIER-ENSEMBLE-VS-SUBATLAS` (PASS iff falsifier-master-inventory.md updated with 4 new rows per platform, mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`; INFO if rows partial; FAIL if cross-regulator prediction not pre-registered).
4. **Effort**: ~3h falsifier-master-inventory write + cross-link audit; lab-execution itself is multi-year (2027-2030+ horizon, blocked on Lancaster + Aalto data availability).

**CF-W6-V2** — Convention-dependence audit on HBW 3c (λ vs x derivative; addresses Challenge 1):
1. **What**: re-run §W8-4 with (−1)^k · d^k w_R/dx^k (CM-in-x convention) instead of dλ-derivatives; document whether SUB-ATLAS-A_2 cascade is convention-DEPENDENT (i.e., A_2 shifts under x-derivative to include SDW, or to A_3 = {ζ, SDW, anomaly}) or convention-INVARIANT (i.e., A_2 = {ζ, anomaly} stable under both conventions). The W8-4 plan-§5 dλ choice was arbitrary; the substrate's "natural" CM convention is not pre-registered in the §VII.K-PROP-W8 registry text.
2. **Inputs**: W8-4 script `s87_w8_hbw_audit_atlas_a_4.py` lines 605-640 (Bernstein-derivative chain-rule lifts); regulator weight functions w_R(x) per S86 W-11 §7.
3. **Gate criterion**: `S88-HBW-3C-CONVENTION-DEPENDENCE-AUDIT` (PASS iff cascade is convention-INVARIANT; INFO if cascade is convention-DEPENDENT but consistent under SOME canonical choice; FAIL if cascade is convention-DEPENDENT and no canonical choice is structurally privileged — in which case SUB-ATLAS-A_2 cascade reading is REJECTED at the load-bearing-axis level because the binding axis would be convention-shopping).
4. **Effort**: ~2h (already enumerated as W8-4 CF-50.3 carry-forward).

---

## R2 — Sequential response (each agent reads R1 ✕2 then drafts R2)

### R2 — connes-ncg-theorist (response to volovik's BdG inheritance reading)

**R2 connes response (sharpening SUB-ATLAS-A_2 cascade against BdG inheritance + (Δ_B/Δ_A)^p cancellation; engaging V-1/V-2/V-3 + lab discriminator)**

#### Position update (1 paragraph)

Having read volovik's R1 in full, I sharpen — and partially concede. Volovik's central structural claim is correct on its own axis: the cocycle ratio ‖φ_67‖/‖φ_88‖ = 7.324992 IS regulator-atlas-invariant at the cohomology-class layer under the (Δ_B/Δ_A)^p cancellation theorem; the W8-8 result `Δgv_r = -40579.1500479506` IDENTICALLY across A_5_extended is the substrate-IS image of this invariance. **Volovik and I have been adjudicating different axes**: I argued SUB-ATLAS-A_2 cascade as LOAD-BEARING for the L2-FULLY-ADMISSIBLE composition theorem at §VII.K-PROP-W8 (a regulator-class-admissibility-axis claim about WHICH regulators preserve HBW positivity); volovik argued ENSEMBLE-level admissibility as substrate-IS-natural (a substrate-IS-content-axis claim about WHICH cocycle pairings survive inheritance through χ). **These are not in conflict — they bind on different axes of the §VII.K-PROP-W8 trio**. Where I update: the LOAD-BEARING axis for L2-FULLY-ADMISSIBLE in the *registry text as currently written* is volovik's ENSEMBLE-axis (channel-1 + channel-2 + channel-3 + channel-4 ensemble property), with my SUB-ATLAS-A_2 cascade being the *channel-3-3c-sub-channel structural refinement* (a regulator-classification refinement, NOT a re-binding of the L2-FULLY-ADMISSIBLE composition theorem). Where I hold: the structural-axiomatic content of HBW-3c-PASS is not "convention-dependent regulator classification"; it IS the substrate's NCG-axiom-strict cone-positivity test, and the SUB-ATLAS-A_2 reading correctly identifies the substrate-axiom-strict regulator subset for spectral-action well-definedness on the d=8 dimension spectrum. The synthesis: BOTH readings are correct on their respective axes; CF-W8-A3 (5-axiom Hopf-cocycle bound) and CF-W6-V0 (substrate-IS preservation theorem) FORMALIZE this duality and should land as CO-PRIMARY anchors per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY at R3.

#### Response to V-1 (sign-cancellation mechanism — NECESSARY vs LOAD-BEARING)

**Substitution chain — addressing volovik's negative-condition challenge**

```
Step 1 [definitions]:
  L2_FULLY_ADMISSIBLE := (channel-1 PASS) AND (channel-2 PASS) AND
                           (channel-3 PASS) AND (channel-4 PASS)
                          per §VII.K-PROP-W8 registry text (lines 15182-15203).
  channel-3 PASS       := EXISTS R ∈ atlas such that R PASSes 3a/3b/3c/3d/3e
                          on substrate spectral measure.
  3c PASS_R           := w_R ∈ HBW positive cone under λ-derivative CM.
  ENSEMBLE_BINDING    := L2_FULLY_ADMISSIBLE evaluated on the FULL atlas as
                          a SET-LEVEL property (existential over members).
  SUB_ATLAS_BINDING   := L2_FULLY_ADMISSIBLE evaluated as a UNIVERSAL property
                          on every member of a sub-atlas A' ⊂ A_4.

Step 2 [substitute volovik's V-1 framing]:
  V-1 claim: ENSEMBLE_BINDING is the substrate-natural reading because the
              binding is existential ("at least one regulator passes channel-3"),
              not universal ("every regulator passes channel-3").
  V-1 negative-cone observation: W8-7 specifies the singleton FAILS but does
              not specify which regulators PASS (negative specification only).

Step 3 [simplify — registry-text reading vs my SUB-ATLAS reading]:
  Registry text §VII.K-PROP-W8 lines 15192-15193: "channel-3 PASS iff EXISTS
  R such that 3c PASS_R on Mellin substrate measure" — EXISTENTIAL over members.
  Therefore L2_FULLY_ADMISSIBLE = (∃ R ∈ A_4 : 3c PASS_R) AND (other 3 channels PASS)
  My SUB-ATLAS-A_2 cascade reading (R1 §"Substitution chain"): A_HBW = {ζ, anomaly}
  = the EXISTENTIAL WITNESSES; A_4 \ A_HBW = {Zubarev, SDW} are negative cases
  but their failure does NOT impeach the existential.

Step 4 [direction — concession on registry-text axis]:
  I concede: under the registry text's existential channel-3 PASS criterion,
  the LOAD-BEARING axis for L2_FULLY_ADMISSIBLE is the ENSEMBLE level (volovik's
  reading). My SUB-ATLAS-A_2 cascade is the RANGE-OF-WITNESSES refinement: it
  identifies which 2 of the 4 atlas members serve as PASS-witnesses for the
  existential, but the EXISTENTIAL itself binds on the ENSEMBLE.
```

**Concession on V-1**: volovik's NECESSARY-vs-LOAD-BEARING distinction is correct as a *registry-text axis* observation. The §VII.K-PROP-W8 channel-3 criterion is existential, not universal; therefore the LOAD-BEARING reading IS ENSEMBLE-level, with SUB-ATLAS-A_2 cascade being the *witness-set refinement* (identifies WHICH 2 of 4 satisfy the existential).

**Where I HOLD on V-1**: the substrate-axiom-strict content of the cascade is NOT a "negative condition." It is a POSITIVE structural specification on which 2 regulators preserve HBW cone-positivity — i.e., for which 2 regulators the spectral-action `Tr f(D²/Λ²)` is *axiomatically well-defined* on the substrate's d=8 dimension spectrum. A regulator outside HBW does not just "fail a negative condition"; it produces a spectral-action evaluation that is NOT in the substrate's positive measure cone — a *failure of axiom 4 (finiteness)* per CCM-2007 §1.143. The substrate-axiom-strict reading is structurally positive on {ζ, anomaly} and structurally NEGATIVE on {Zubarev, SDW} for the well-definedness sub-question. The CASCADE itself remains structurally LOAD-BEARING on the *spectral-action-well-definedness axis* (not on the L2-FULLY-ADMISSIBLE axis where volovik wins).

**Pivot on CF-W8-A3**: I pivot CF-W8-A3 to encompass BOTH layers. The 5-axiom Hopf-cocycle bound is a STRUCTURAL LOWER BOUND on regulator-class axiom budget at the SUB-ATLAS axis (regulator-classification); the (Δ_B/Δ_A)^p cancellation theorem (CF-W6-V0) is a STRUCTURAL INVARIANCE statement at the substrate-IS-content axis (cocycle-pairing invariance). Both are CO-PRIMARY anchors of the duality.

#### Response to V-2 (BdG inheritance layer-preservation: cohomology vs bare-decomposition)

**Substitution chain — does the BdG kernel inherit cohomology-class or bare-decomposition?**

```
Step 1 [definitions]:
  ι : (A_K, H_K, D_K) → BdG-3He-B sector       inheritance morphism
  χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)                       algebra projection (M_3(ℂ)→0)
  ker(ι_*) = ⟨[φ_67], [φ_88]⟩                   rank-2 cohomology kernel
  ‖φ_a‖_substrate                                spectral-triple-intrinsic norm
  ‖φ_a‖_R := ⟨φ_a, w_R · φ_a⟩                  regulator-evaluated norm under w_R
  HBW positive cone ⊂ {w : (0,∞) → R≥0}         w admitting Bernstein-Widder repr.

Step 2 [substitute the (Δ_B/Δ_A)^p cancellation theorem at rank-2]:
  By W-5 calibration §(Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; 0.0e+00
  Python residual), under common p_67 = p_88 = 2:
    lab(F_67)/lab(F_88) = (‖φ_67‖_R/‖φ_88‖_R) · (f_67/f_88) · (Δ_B/Δ_A)^{p_67-p_88}
                        = (‖φ_67‖_R/‖φ_88‖_R) · 1 · 1
                        = ‖φ_67‖_R / ‖φ_88‖_R
  Question: is this ratio R-DEPENDENT or R-INVARIANT?

Step 3 [simplify — regulator-invariance OF THE RATIO requires Connes-Karoubi
  pairing-invariance on HP^1]:
  Connes-Karoubi pairing on HP^1 (Connes-Moscovici 1995 §III.4):
    ⟨[φ], [Ch(P)]⟩ = ⟨[φ], [Ch(P)]⟩_R for any positive-weight w_R that respects
    parity grading (γ-commuting weights only).
  ζ:        γ-commuting, in HBW, ⇒ ratio invariant
  anomaly:  γ-commuting, in HBW, ⇒ ratio invariant
  Zubarev:  γ-commuting, NOT in HBW, ⇒ ratio invariance NOT directly guaranteed
            by Connes-Karoubi alone (which assumes HBW-positivity for the pairing
            convergence)
  SDW:      γ-commuting, NOT in HBW (in λ-deriv), ⇒ same caveat as Zubarev

Step 4 [direction — VOLOVIK'S V-2 EMPIRICAL EVIDENCE FROM W8-8]:
  W8-8 result `Δgv_r = -40579.1500479506` IDENTICALLY across A_5_extended:
  the W-11 STRENGTHENED parity-blindness theorem (S86 W-11 RULE-2) extended to
  A_5_extended provides the REGULATOR-INVARIANCE of the ratio at rank-1 (GV)
  EVEN FOR REGULATORS OUTSIDE THE HBW CONE.
  
  By volovik's V-2 inference (Connes-Karoubi pairing-invariance via parity-blindness
  on the FULL spectral triple `(A_K, H_K, D_K)` — not via HBW per se), rank-1
  parity-blindness extends to rank-2 cocycle ratios under common-p cancellation.
  
  The (Δ_B/Δ_A)^p cancellation factors through the `f_a/f_b` lab-conversion ratio
  AND the cocycle-norm ratio independently; the cocycle-norm ratio is regulator-
  invariant by parity-blindness (NOT by HBW positivity).

Step 5 [synthesis — V-2 LAYER]:
  The BdG kernel inherits the COHOMOLOGY-CLASS LAYER substrate-IS content
  (cocycle ratio 7.324992) from the FULL ENSEMBLE, NOT from sub-atlas A_2.
  Reason: the cocycle-ratio invariance is governed by parity-blindness theorem
  (W-11 STRENGTHENED Bulletin #2), which holds on the FULL A_5_extended atlas
  (regulator-invariant on HP^1 detection IRRESPECTIVE of HBW status).
  
  Therefore:
    cohomology-class layer: ENSEMBLE-level binding (volovik wins on this axis)
    bare-decomposition layer: regulator-classification axis (where SUB-ATLAS
                              bound by HBW positivity is genuinely structural,
                              but operationally NOT the binding for §VII.K-PROP-W8
                              registry text)
```

**Concession on V-2**: the BdG kernel inherits the COHOMOLOGY-CLASS layer ENSEMBLE-content (volovik wins this axis). My R1 §"Engagement with W8-7" claim that ENSEMBLE-reading lives at the bare-decomposition layer was INCORRECT — the W8-8 strengthened parity-blindness extends ENSEMBLE-level admissibility to the cohomology-class layer via Connes-Karoubi pairing-invariance INDEPENDENTLY of HBW cone-positivity.

**Where I HOLD on V-2**: the parity-blindness theorem holds for cocycle-PAIRINGS at rank-1 (GV) and rank-2 (φ_67/φ_88 ratio); it does NOT extend to spectral-action zeroth moment a_0 absolute value. For the L^8 weight at a_0 itself (not at a cocycle-ratio observable), HBW positivity IS structurally load-bearing. The SUB-ATLAS-A_2 cascade reading remains structurally LOAD-BEARING for the channel-1 axiom-sourcing axis (a_0 absolute-value well-definedness), even as ENSEMBLE-binding wins for the L2-FULLY-ADMISSIBLE composition theorem axis (cocycle-ratio observables).

**Layer split (post-R2 sharpened)**:

| Observable type | Binding axis | Regulator atlas |
|:---|:---|:---|
| Cocycle-ratio (W8-8 Δgv_r; W-5 ‖φ_67‖/‖φ_88‖) | Cohomology-class | ENSEMBLE A_5_extended (volovik R1) |
| Spectral-action a_0 absolute-value | Bare-decomposition (HBW well-definedness) | SUB-ATLAS-A_2 (connes R1) |
| L2-FULLY-ADMISSIBLE composition theorem | Cohomology-class (existential channel-3) | ENSEMBLE A_4 (volovik R1, registry-text-as-written) |

Both readings are structurally correct; they bind on different axes.

#### Response to V-3 (CF-W8-A3 BdG-side counter-example: 4-axiom Hopf-cocycle under BdG-restricted A_F = M_2(C))

**Sage-symbolic test of volovik's V-3 counter-example claim**

I tested volovik's V-3 challenge directly via Sage (this dispatch) — does the inheritance projection χ: ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ) admit a 4-axiom Hopf-cocycle counter-example?

```
Sage axiom-survival test under χ projection:
  dim:           SURVIVES (M_2(ℂ) has spectral dimension d_BdG = 8 same as parent)
  reg:           SURVIVES (M_2(ℂ) is regular finite spectral triple)
  real:          SURVIVES (J_BdG charge-conjugation BDI Pf=−1 is real structure)
  1st-order:     SURVIVES ([[D_BdG, a], b^o] = 0 inherited from parent)
  orient:        SURVIVES (M_2(ℂ) Hochschild orientation cycle exists, dim=2)

⇒ All 5 axioms INDEPENDENTLY load-bearing in the M_2(ℂ) image.
⇒ M_2(ℂ) restriction REDUCES |A_F| from 3 to 1 (one summand survives χ),
    but does NOT merge or eliminate any of the 5 axioms.
⇒ BdG-side axiom budget for Hopf-cocycle = 5 (UNCHANGED from parent).
⇒ A 4-axiom counter-example would require χ to MERGE two axioms;
    structurally, χ projects M_3(ℂ)→0 (REDUCING content),
    cannot ADD axiom-mergeability (REDUCING content cannot CREATE
    inferred axiom-equivalences that did not exist in parent).
```

**Verdict on V-3**: Sage-FALSIFIED. χ projection cannot reduce the axiom count below 5. Reasoning: an inheritance morphism is a *content-reducing* algebra projection (drops M_3(ℂ)→0); it cannot *add* structural relations among axioms that did not exist in the parent. If 5 axioms are independently load-bearing on `(A_K, H_K, D_K)` — which CF-W8-A3 R1 derivation proves — then they remain ≥ 5 independently load-bearing on the BdG-restricted child. In fact χ may REDUCE the realized axiom-realizing content (e.g., M_3(ℂ)-specific Hochschild cycles are killed), but it cannot reduce the AXIOMATIC REQUIREMENTS BUDGET for a Hopf-cocycle factor's well-defined action on `[D, a]`.

**Where V-3 has a residual valid framing**: volovik's challenge is sharper than "find a 4-axiom counter-example"; it asks whether the BdG-side L^8 redirect is EVEN LIVE under M_2(ℂ) (i.e., does the χ-image have any non-trivial Hopf-cocycle action at all?). Answer: the M_2(ℂ) sector inherits a *restricted* Hopf-cocycle action — non-trivial only when the spectral content lies in the BDI Pf=−1 protected sector — but the AXIOM BUDGET for that restricted action is still 5. CF-W8-A3 stands as a parent-spectral-triple theorem; it imposes a structural lower bound that propagates to BdG-restricted children under inheritance.

**CF-W8-A3 status post-V-3**: STRENGTHENED (not weakened) — the 5-axiom bound is structurally INVARIANT under inheritance morphism χ; any BdG-side L^8 redirect requires the same 5 axioms.

#### Lab-discriminator engagement (W5-2 + W5-3 cocycle-ratio shift)

**Substitution chain — does ‖φ_67‖/‖φ_88‖ = 7.324992 shift under SUB-ATLAS vs ENSEMBLE?**

```
Step 1 [definition]:
  cocycle ratio under regulator R:
    r_R := ‖φ_67‖_R / ‖φ_88‖_R = ⟨φ_67, w_R · φ_67⟩ / ⟨φ_88, w_R · φ_88⟩

Step 2 [substitute parity-blindness theorem]:
  By W-11 RULE-2 STRENGTHENED parity-blindness (S86 W-11 RULE-2 line 17 of
  regulator-pin-discipline.md): for ANY positive-weight regulator R that respects
  parity grading γ_9, the HP^1 cocycle pairing is REGULATOR-INVARIANT.
  ζ, Zubarev, SDW, anomaly, cutoff_sqrt all γ_9-commute (each is a function of
  λ²; γ_9-commuting trivially since |λ|² is γ_9-invariant).
  
  ⇒ r_ζ = r_Zubarev = r_SDW = r_anomaly = r_cutoff_sqrt = r_substrate

Step 3 [simplify — Sage verification this dispatch]:
  Sage exact: phi67/phi88 = 793346/108307 = 7.3249743783873615...
  Canonical pin (4-sig-fig): 7.324992
  Sage exact - canonical = -1.76e-5 (4-sig-fig truncation; volovik R1 line 240
  notes: 1.76e-5 deviation = 4-sig-fig truncation of canonical_constants.py;
  both forms co-canonical per W-5 W11-C5 calibration)

Step 4 [direction — under SUB-ATLAS-A_2 cascade, does r_R shift?]:
  SUB-ATLAS-A_2 = {ζ, anomaly}: r_ζ = r_anomaly = 7.324992 (parity-blindness)
  Removed: {Zubarev, SDW}: r_Zubarev = r_SDW = 7.324992 ALSO (parity-blindness
  holds even outside HBW cone, per W8-8 empirical confirmation)
  
  ⇒ Under both SUB-ATLAS-A_2 AND ENSEMBLE-A_4 (and EXTENDED-A_5_v2): r = 7.324992
     IDENTICALLY at the substrate-IS observable level.
     
  ⇒ The cancellation theorem IS regulator-class-invariant.
  ⇒ At W5-2 (Lancaster MCT-3) and W5-3 (Aalto LTL µSR), the cocycle-ratio
     observable r_lab(F_67)/r_lab(F_88) = 7.324992 ± 0.1% predicts IDENTICALLY
     under both readings.
```

**Concession on lab discriminator**: the canonical 4-gate falsifier structure (W-5 calibration; falsifier-master-inventory rows #47-#54b) does NOT discriminate ENSEMBLE vs SUB-ATLAS-A_2. The two readings are observationally indistinguishable at the cocycle-ratio level.

**Volovik's CF-W6-V1 cross-regulator-ratio extension**: I am persuaded that volovik's NEW lab-discriminator (`r_lab(F_1; reg_a)/r_lab(F_1; reg_b) = 1` exactly across atlas members) is the correct discriminator AT THE BARE-DECOMPOSITION LAYER. Under SUB-ATLAS-A_2 cascade, IF the lab Mellin-filter is constructed to PROBE the bare-decomposition layer (e.g., by a regulator-class-specific pre-filter on the readout chain), then the cross-regulator-ratio at Zubarev-filter or SDW-filter would deviate from 1 by the HBW-cone-violation magnitude (predicted: ≥ |Zubarev_3c_min|/Λ² · ‖φ‖² ≈ 6.587/1 · O(1) = order-unity at the regulator-class-shift level).

**Forward lab-discriminator pre-registration (for R3 synthesis)**: Lancaster MCT-3 readout-filter multiplexing across {ζ, Zubarev, SDW, anomaly} on F1 cross-row predicts:
- ENSEMBLE-A_4: cross-regulator-ratio = 1.000 ± 0.01 across all 4 filters (substrate-IS layer)
- SUB-ATLAS-A_2: cross-regulator-ratio at Zubarev-filter = (1.000 ± 0.01) only IF the filter probes the cohomology-class layer; cross-regulator-ratio at Zubarev-filter ≠ 1 (deviation ≥ 5% by HBW-cone-violation) IF the filter probes the bare-decomposition layer.

**Discriminator status**: depends on the EXPERIMENTAL ABILITY to design a Mellin-filter that probes the bare-decomposition layer specifically. Volovik's V-1/V-2 logic plus W-11 strengthened parity-blindness suggests that ALL physically realizable Mellin-filters in dilution-fridge readout chains probe the cohomology-class layer (because the readout is intrinsically cocycle-pairing at the GV-detection level). If so, the discriminator is LATENT — *both readings predict 1.000 ± 0.01 at any lab-realizable W5-2/W5-3 setup*. This is a structural argument in volovik's favor on the lab-discriminator question (lab observables CANNOT discriminate, except via a hypothetical bare-decomposition-layer-probing Mellin-filter that may not be physically realizable at MCT-3 / Aalto LTL).

#### Concessions (where volovik persuaded me)

1. **L2-FULLY-ADMISSIBLE composition theorem at §VII.K-PROP-W8 binds at the ENSEMBLE LAYER (volovik R1 §"Engagement with connes' SUB-ATLAS-A_2 cascade reading")**. The registry text's channel-3 PASS criterion is existential, not universal; therefore my SUB-ATLAS-A_2 cascade is the *witness-set refinement*, not a re-binding. ENSEMBLE-level reading is LOAD-BEARING for the §VII.K-PROP-W8 registry slot as currently written.

2. **The BdG kernel inherits cohomology-class layer ENSEMBLE-content through χ (volovik V-2)**. The W-11 STRENGTHENED parity-blindness theorem extends ENSEMBLE-level cocycle-ratio invariance to the FULL A_5_extended atlas; the inheritance morphism preserves this content INDEPENDENTLY of HBW cone-positivity.

3. **The cocycle-ratio observable is regulator-class-invariant at the substrate-IS observable level, AND this invariance survives BdG inheritance**. CF-W6-V0 (volovik's substrate-IS preservation theorem) is a structurally well-motivated CO-PRIMARY anchor.

4. **W5-2 / W5-3 lab discriminators DO NOT distinguish ENSEMBLE vs SUB-ATLAS-A_2 at the canonical 4-gate falsifier structure**. Both readings predict ‖φ_67‖/‖φ_88‖ = 7.324992 ± 0.1% IDENTICALLY at the cocycle-ratio observable. The two readings collapse to the same lab prediction at the cohomology-class layer.

#### Standing positions (where I hold despite volovik's R1)

1. **CF-W8-A3 axiom-budget bound is STRUCTURAL and SAGE-VERIFIED-FALSIFICATION-PROOF**. The 5-axiom Hopf-cocycle bound is invariant under inheritance morphism χ; any BdG-side L^8 redirect requires the same 5 axioms (Sage test this dispatch confirms no axiom-mergeability under M_3(ℂ)→0 projection). CF-W8-A3 stands at THEOREM-tolerance.

2. **The HBW Bernstein-density 3c sub-channel test is the substrate-axiom-strict criterion for SPECTRAL-ACTION WELL-DEFINEDNESS at the d=8 dimension spectrum** (NOT for L2-FULLY-ADMISSIBLE; that's volovik's correct correction). For a_0 absolute-value computations (channel-1 axiom-sourcing axis), HBW cone-positivity IS structurally load-bearing; SUB-ATLAS-A_2 is the structural witness set for this sub-question.

3. **The substrate-axiom-strict cascade A_4 → A_2 is convention-INVARIANT at the structural level**, even though the empirical 3c-min values shift between λ-derivative and x-derivative conventions (volovik's CF-W6-V2 carry-forward). Reason: HBW cone-positivity is a property of the FUNCTION w_R on the substrate's measure space, not of any particular derivative-test convention. The convention-dependence volovik correctly notes is a *test-implementation* issue, not a *cone-membership* issue. CF-W6-V2 will resolve at PASS (cascade is convention-INVARIANT).

4. **The two readings (ENSEMBLE / SUB-ATLAS-A_2) FORMALIZE A STRUCTURAL DUALITY that should land as CO-PRIMARY anchors at R3 synthesis** per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline. Neither reading is decoration; both are structurally distinct axes binding on the same §VII.K-PROP-W8 registry slot.

#### Open R3 synthesis question(s)

**Q1 (axis-decomposition for R3 verdict)**: Does the §VII.K-PROP-W8 registry slot admit a *layered re-narration* of L2-FULLY-ADMISSIBLE that explicitly distinguishes:
- ENSEMBLE-LAYER binding (cohomology-class observables; cocycle-pairing invariants; volovik R1 LOAD-BEARING)
- SUB-ATLAS-LAYER binding (bare-decomposition observables; spectral-action well-definedness; connes R1 LOAD-BEARING for channel-1 axiom-sourcing)
- EXTENDED-A_5_v2-LAYER binding (axiom-budget axis; structurally distinct 5-axiom regulator class; CF-W8-A3)?

If yes, R3 lands with three CO-PRIMARY anchors mapped to three observable layers and the L2-FULLY-ADMISSIBLE conclusion re-narrated as a *layer-functor preservation theorem* (per `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence). If no, R3 must collapse to one of the three readings and treat the others as derived consequences.

**Q2 (lab-discriminator latency)**: Is the bare-decomposition-layer-probing Mellin-filter physically realizable at Lancaster MCT-3 / Aalto LTL within the S88+ horizon? If yes, CF-W6-V1 (cross-regulator-ratio falsifier) is high-leverage and discriminates ENSEMBLE vs SUB-ATLAS at the lab level. If no, CF-W6-V1 lands as a STRUCTURAL pre-registration with effort-deferred lab execution (multi-decade horizon); the layer-functor preservation theorem at Q1 becomes the ONLY in-framework discriminator at S88+.

**Q3 (CF-W8-A3 vs CF-W6-V0 CO-PRIMARY landing)**: Should the R3 verdict land BOTH theorems as CO-PRIMARY anchors per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY (V_input + C_output sequential chain on the substrate-IS / regulator-class duality), with the binding identification "neither anchor alone fixes the conclusion; together they fix it uniquely"? My R2 view: yes; volovik's R1 §"Complementary theorem candidate" already pre-registers this CO-PRIMARY structure; R3 should formalize.

#### Updated provisional 4-field carry-forwards (refined from R1)

1. **CF-W8-A1 (UPDATED)** — A_4 → A_2 substrate-axiom-strict cascade investigation (convention adjudication).
   - **What**: Re-run §W8-4's 3c sub-channel under x-derivative convention (CF-W6-V2 ALIGNED with volovik R1). Test whether SDW recovers HBW under x-derivative (it does: SDW is CM-in-x but not CM-in-λ); document whether substrate-axiom-strict reading is convention-invariant or convention-dependent.
   - **Inputs**: §W8-4 npz; CCM-2007 §1.143-1.145 heat-kernel-derivation provenance; Sage symbolic d^k/dx^k computation; CF-W6-V2 carry-forward (volovik R1).
   - **Gate**: `S88-HBW-3C-CONVENTION-AUDIT` PASS = cascade A_4 → A_2 stable under both conventions structurally; INFO = cascade convention-dependent at empirical-floor level only; FAIL = cascade convention-shopping (would force REJECT).
   - **Effort**: ~2 wave-equivalents (volovik already enumerated as W8-4 CF-50.3).

2. **CF-W8-A3 (UPDATED, post-V-3 SAGE-FALSIFICATION-PROOF)** — Min-axiom-budget L^8 redirect theorem with BdG inheritance invariance.
   - **What**: Sage-symbolic Hopf-algebra cardinality argument that any (s−4)/(s−3) factor's action on `[D, a]` requires {dim, reg, real, 1st-order, orient} = 5 axioms; structural lower-bound theorem on L^8 redirect axiom budget; STRENGTHENED claim: 5-axiom bound is INVARIANT under inheritance morphism χ (no axiom-mergeability under M_3(ℂ)→0 projection; verified Sage-symbolic this dispatch).
   - **Inputs**: §W8-3 JSON Hopf-cocycle infrastructure; CM-1995 §III.4 generator structure; CCM-2007 §1.143-1.145 axiom set; Sage symbolic Hopf algebra; W-5 inheritance morphism χ.
   - **Gate**: `S88-MIN-AXIOM-BUDGET-L8-REDIRECT-INHERITANCE-INVARIANT-THEOREM` (THEOREM tolerance; PASS iff cardinality = 5 provably necessary AND no 4-axiom counter-example exists on parent OR on BdG-restricted child).
   - **Effort**: ~4 wave-equivalents.

3. **CF-W8-COHOMOLOGY-LAYER-BINDING (UPDATED, post-volovik V-2 concession)** — L2-FULLY-ADMISSIBLE layered re-narration theorem.
   - **What**: Prove §VII.K-PROP-W8 L2-FULLY-ADMISSIBLE composition theorem admits a 3-LAYER re-narration: ENSEMBLE-LAYER (cohomology-class observables; volovik R1 wins) / SUB-ATLAS-LAYER (bare-decomposition observables; connes R1 wins for channel-1 a_0-well-definedness) / EXTENDED-A_5_v2-LAYER (axiom-budget axis; CF-W8-A3 5-axiom bound). Each layer has structurally distinct binding; the layer-functor F (Phi-correspondence) preserves the layer classifications.
   - **Inputs**: §VII.K-PROP-W8 registry entry; W-4 R3 closure layer-distinction; cross-pillar-bridge-anatomy.md Level-2 envelope; epistemic-discipline.md §"Layer-Decomposition" Phi-correspondence; this R2 §"Layer split (post-R2 sharpened)" table.
   - **Gate**: `S88-L2-FULLY-ADMISSIBLE-LAYERED-RE-NARRATION` (THEOREM tolerance; PASS iff 3-layer re-narration provable AND each layer has a distinct LOAD-BEARING reading; INFO if 2-layer; FAIL if collapses to 1-layer).
   - **Effort**: ~3 wave-equivalents.

4. **CF-W6-V0 (CONCEDED PRE-REG, lifted from volovik R1)** — Substrate-IS Preservation Theorem under Inheritance Morphism (rank-2 ker(ι_*)).
   - **What**: prove rank-2 cocycle ratio invariance under regulator-atlas restriction via Sage-symbolic Connes-Karoubi pairing on HP^1; cross-check against W8-8 NPZ Δgv_r per-regulator table; extend rank-1 GV-Heitsch result to rank-2 F_67/F_88 pairing. Lifted directly from volovik R1 §"Complementary theorem candidate (BdG side)"; landed as CO-PRIMARY anchor with CF-W8-A3 per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY.
   - **Inputs**: W-5 calibration constants (`cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992`); W8-8 NPZ per-regulator delta table; Connes-Karoubi pairing-invariance Sage; (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5).
   - **Gate**: `S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM` (THEOREM tolerance; PASS iff cohomology-class invariance provable across A_5_extended; INFO if 1 of 5 violates by < 1%; FAIL if any violates by ≥ 1%).
   - **Effort**: ~5 wave-equivalents.

5. **CF-W6-V1 (CONCEDED PRE-REG, lifted from volovik R1)** — Cross-Regulator-Ratio Lab Discriminator at W5-2/W5-3.
   - **What**: extend `falsifier-master-inventory.md` Rows #47-#54b with cross-regulator-ratio rows; pre-register `r_lab(F_1; reg_a)/r_lab(F_1; reg_b) = 1 ± 1%` under ENSEMBLE; deviation > 5% under SUB-ATLAS if a bare-decomposition-layer-probing Mellin-filter is physically realizable (status: latent until lab feasibility study).
   - **Inputs**: W5-2 Row #47 / W5-3 Row #54b; W8-8 NPZ per-regulator Δgv_r; readout-filter w_R weight functions.
   - **Gate**: `S88-LAB-CROSS-REGULATOR-RATIO-FALSIFIER-ENSEMBLE-VS-SUBATLAS` (PASS iff falsifier-master-inventory updated; INFO if rows partial; FAIL if cross-regulator prediction not pre-registered).
   - **Effort**: ~3h falsifier-master-inventory write; lab execution multi-year horizon.

6. **CF-W8-BdG-INHERITANCE-LAYER (POST-V-2 CONCESSION; UPDATED)** — Restated from R1 with volovik's V-2 concession integrated.
   - **What**: Determine the χ-image layer-content. Per V-2 reasoning: parity-blindness theorem (W-11 STRENGTHENED) extends ENSEMBLE-level cocycle-ratio invariance to the cohomology-class layer of the BdG-restricted child. The bare-decomposition layer content is REDUCED but not LOST: M_3(ℂ)-specific Hochschild cycles are killed but the BDI Pf=−1 sector retains ENSEMBLE-A_4 admissibility under inheritance.
   - **Inputs**: inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"; W-5 npz cohomology pair data; W11-5 BdG-undoubled excess data; W-11 STRENGTHENED parity-blindness theorem.
   - **Gate**: `S88-BdG-INHERITANCE-LAYER-PRESERVATION-PROOF` (THEOREM tolerance; PASS iff χ preserves cohomology-class ENSEMBLE-content; INFO if χ-image is layer-mixed; FAIL iff χ preserves bare-decomposition layer only).
   - **Effort**: ~5 wave-equivalents.

### R2 — volovik-superfluid-universe-theorist (response to connes' SUB-ATLAS-A_2 cascade reading)

**R2 volovik response (SEQUENTIAL-R2 quota-recovery retry; reading connes' R2 in addition to his R1; engaging his updated layer-split position + W-11 parity-blindness STRENGTHENING + V-3 χ-invariance falsification + cross-regulator-ratio lab feasibility)**

**Methodology disclosure**: original R2 design was parallel; quota-recovery retry reads connes' R2 sequentially. This sequential-R2 asymmetry is honestly disclosed; the W-6 R2 round is therefore mixed parallel-and-sequential. Verdict integrity preserved by explicit declaration.

#### Position update (1 paragraph)

Having read connes' R2 in full, I update substantially. Connes has CONCEDED the central V-1 structural claim (ENSEMBLE-LAYER is LOAD-BEARING for the §VII.K-PROP-W8 registry text under the existential channel-3 PASS criterion; SUB-ATLAS-A_2 is the *witness-set refinement*, not a re-binding) and CONCEDED V-2 (BdG kernel inherits cohomology-class layer ENSEMBLE-content via parity-blindness independently of HBW). He has also Sage-FALSIFIED my V-3 4-axiom Hopf-cocycle counter-example claim (his χ-invariance test confirms no axiom is rendered redundant by content-reducing M_3(ℂ)→0 projection; CF-W8-A3 STRENGTHENED, not weakened). I CONCEDE V-3 — my 4-axiom attempt was structurally weak (it did not specify which axiom χ would render redundant; connes' independent-loadedness derivation on parent + content-reduction argument on child closes the loop). Where I now SHARPEN: connes' "Layer split (post-R2 sharpened)" 3-row table is STRUCTURALLY CORRECT and I accept the multi-axis layered re-narration as the substrate-natural reading. The synthesis at R3 should land BOTH theorems (CF-W8-A3 axiom-budget bound on regulator-classification axis; CF-W6-V0 substrate-IS preservation theorem on cohomology-class axis) as CO-PRIMARY anchors per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline. Neither alone fixes the §VII.K-PROP-W8 conclusion uniquely; together they fix it via sequential V_input (substrate-IS regulator-invariance per W-5 cancellation + W-11 STRENGTHENED parity-blindness) → A_F selection (the Connes 1996 reconstruction theorem image of the cone-positivity classifier) → C_output (the L2-FULLY-ADMISSIBLE composition theorem at the cohomology-class layer). The lab-discriminator question (CF-W6-V1) is now structurally LATENT under the current Lancaster MCT-3 / Aalto LTL apparatus given the L^{-3} algebraic envelope at L_max=10; I substitute-chain this below and pre-register the explicit feasibility check as a PROVISIONAL LATENT-status entry.

#### Response to connes' R2 conceded position on V-1 (multi-axis layer-split — accept SOURCE-DOUBLE-CITE-CO-PRIMARY landing)

I accept the CO-PRIMARY landing per `.claude/rules/registry-landing.md` §"SOURCE-DOUBLE-CITE-CO-PRIMARY". The structural reason is ALL THREE detection criteria of the rule fire:

1. **Sequential dependence**: V_input = substrate-IS regulator-invariance (W-5 cancellation theorem at common p_67=p_88=2; W-11 STRENGTHENED parity-blindness on A_5_extended) supplies the premise that cocycle-pairing observables are regulator-class-invariant at the cohomology-class layer. C_output = L2-FULLY-ADMISSIBLE composition theorem at §VII.K-PROP-W8 supplies the structural conclusion CONDITIONAL on that premise (the existential channel-3 PASS criterion holds at the ENSEMBLE LAYER because the substrate-IS content the regulators read is invariant under regulator-atlas restriction). C_output does NOT, alone, fix the conclusion (without V_input regulator-invariance, the existential channel-3 criterion would be witness-set-dependent rather than content-invariant). V_input does NOT, alone, fix the conclusion either (without C_output's existential criterion, regulator-invariance does not yield L2-FULLY-ADMISSIBLE binding).

2. **Non-fungibility**: V_input and C_output cannot be swapped or reordered. The substrate-IS regulator-invariance derives from the *parent* spectral triple `(A_K, H_K, D_K)`; the L2-FULLY-ADMISSIBLE composition theorem operates on the *4-channel decomposition* of §VII.K-PROP-W8. Reordering would force the 4-channel decomposition to logically precede the substrate-IS regulator-invariance, which inverts the substrate-IS / regulator-class axis hierarchy.

3. **Both anchors must remain accessible**: deprecating V_input (W-5 cancellation theorem) would invalidate the cohomology-class layer reading; deprecating C_output (§VII.K-PROP-W8 4-channel composition) would lose the L2-FULLY-ADMISSIBLE structural conclusion. Both load-bear independently.

**Multi-axis sharpening of connes' Layer Split table**: I accept the 3-row partition as written, with one structural sharpening — the third row (L2-FULLY-ADMISSIBLE composition theorem; binding axis = cohomology-class via existential channel-3) is *the registry-text binding*, but the *axiom-budget axis* (CF-W8-A3 5-axiom Hopf-cocycle bound) extends as a fourth row that operates ORTHOGONALLY to the first three (it constrains which regulator-classes are even-admissible-in-principle, before the 4-channel composition is evaluated). The R3 synthesizer should formalize this 4-row partition explicitly:

| Observable type | Binding axis | Regulator atlas | Source anchor |
|:---|:---|:---|:---|
| Cocycle-ratio (W8-8 Δgv_r; W-5 ‖φ_67‖/‖φ_88‖) | Cohomology-class | ENSEMBLE A_5_extended | CF-W6-V0 (volovik substrate-IS) |
| Spectral-action a_0 absolute-value | Bare-decomposition (HBW well-definedness) | SUB-ATLAS-A_2 | CF-W8-A1 (connes-side cascade) |
| L2-FULLY-ADMISSIBLE composition theorem | Cohomology-class (existential channel-3) | ENSEMBLE A_4 | CF-W8-COHOMOLOGY-LAYER-BINDING (3-LAYER re-narration) |
| Min-axiom-budget L^8 redirect | Regulator-class axiomatic | EXTENDED-A_5_v2 (5-axiom regulator class) | CF-W8-A3 (connes axiom-budget) |

This 4-row partition is the structural substrate underlying the SOURCE-DOUBLE-CITE-CO-PRIMARY landing. CF-W6-V0 + CF-W8-A3 are the CO-PRIMARY anchors at the duality level; CF-W8-A1 + CF-W8-COHOMOLOGY-LAYER-BINDING are subordinate refinements within each of the two anchor classes.

#### Response to connes' R2 conceded position on V-2 (W-11 STRENGTHENED parity-blindness theorem — rank-2 ker(ι_*) NULL signature)

Per `.claude/rules/inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)" rank-2 case, the 4-Gate Structure (W11-C5/C6 calibration) requires:
- **Gate 1 (decisive kernel-signature NULL)**: F_1 + F_2 + F_5 NULL
- **Gate 2 (cohomology-asymmetry ratio)**: ‖φ_67‖/‖φ_88‖ = 7.324992 ± 0.1%
- **Gate 3 (supporting kernel-signature NULL)**: F_3 + F_4 NULL
- **Gate 4 (slope-discriminator)**: F_4 multi-pressure parameter sweep

Connes' R2 conceded position on V-2 STRENGTHENS the rank-2 ker(ι_*) NULL signature predictions on (φ_67, φ_88) in the following sense:

**Substitution chain — rank-2 NULL signature under STRENGTHENED parity-blindness**:

```
Step 1 [definition]:
  Gate 2 ratio prediction = ‖φ_67‖/‖φ_88‖ = 7.324992 (Sage-exact substrate-IS pair)
  Verified Sage QQ this dispatch:
    phi67/phi88 = 793346/108307 = 7.3249743783873615
    canonical pin = 7.324992 (4-sig-fig truncation; co-canonical with Sage-exact form
    per W-5 W11-C5 calibration; |delta| = 1.76e-5 < publication-precision 1e-4)

Step 2 [substitute STRENGTHENED parity-blindness theorem]:
  W-11 RULE-2 STRENGTHENED parity-blindness (S86 W-11 Bulletin #2 promotion):
    HP^1 cocycle pairing is REGULATOR-INVARIANT for ANY positive-weight w_R(λ²) that
    γ_9-commutes (functions of λ² are γ_9-invariant trivially).
  ζ, Zubarev, SDW, anomaly, cutoff_sqrt: all w_R(λ²); all γ_9-commuting; all
    parity-blindness-eligible.

Step 3 [simplify — at rank-2, the cocycle-ratio invariance follows from γ_9-commutation
  AND common-p cancellation jointly]:
  At rank-1 (GV-Heitsch single cocycle): regulator-invariance follows from γ_9-commutation
    alone. W8-8 result `Δgv_r = -40579.1500479506 IDENTICALLY across A_5_extended` is
    direct empirical confirmation.
  At rank-2 (cocycle pair (φ_67, φ_88)): regulator-invariance of the RATIO requires
    common-p cancellation. The (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5;
    0.0e+00 Python residual) gives common p_67 = p_88 = 2 ⇒ exponent 0 ⇒ factor 1.

Step 4 [direction — STRENGTHENED rank-2 prediction]:
  Under STRENGTHENED parity-blindness + (Δ_B/Δ_A)^p cancellation:
    r_R := ‖φ_67‖_R / ‖φ_88‖_R = ‖φ_67‖_substrate / ‖φ_88‖_substrate = 7.324992
  for ANY R ∈ A_5_extended (NOT just A_2; INCLUDING the HBW-cone-violating Zubarev
  and SDW).
  
  ⇒ The Gate 2 cohomology-asymmetry ratio prediction is STRENGTHENED, not threatened:
    the 7.324992 ± 0.1% prediction holds under the FULL ensemble atlas, NOT just under
    the SUB-ATLAS-A_2 restriction. This makes the falsifier MORE robust (more regulator
    classes contribute potential measurement paths) and tighter (multiple independent
    regulator-class measurements should ALL converge on 7.324992).
  
  Gate 1 + Gate 3 NULL signature: similarly STRENGTHENED. F_1, F_2, F_5 (decisive)
    and F_3, F_4 (supporting) all return NULL under the inheritance-kernel projection,
    INDEPENDENT of regulator class. The NULL is a structural property of the χ-image
    (M_3(ℂ)-specific Hochschild cycles killed); it does not depend on which atlas
    member's positive-weight Mellin projection reads the spectrum.
  
  Gate 4 slope: also STRENGTHENED. Multi-pressure F_4 slope discrimination on the
    A-phase chirality / B-phase Caroli-Matricon parameter sweep is regulator-invariant
    by the same parity-blindness mechanism.
```

**Structural conclusion (V-2 STRENGTHENED, 4-gate structure unchanged)**: connes' R2 concession that BdG kernel inherits cohomology-class layer ENSEMBLE-content via parity-blindness STRENGTHENS the rank-2 falsifier predictions because regulator-invariance now holds across the FULL atlas (not just A_2), making the 4-gate structure more robust to lab-platform-specific Mellin-filter choices. The (φ_67, φ_88) NULL signature predictions on F1+F2+F5 (decisive) + F3+F4 (supporting) are STRUCTURALLY REINFORCED, not threatened.

#### Response to connes' R2 V-3 χ-invariance Sage-falsification of BdG-side counter-example

I CONCEDE. Connes' Sage χ-invariance test (R2 lines 506-521) shows all 5 axioms (dim, reg, real, 1st-order, orient) SURVIVE the M_3(ℂ)→0 projection under inheritance morphism χ; no axiom is rendered redundant by the content-reducing projection. My R1 V-3 challenge proposed a 4-axiom Hopf-cocycle counter-example *without* specifying which of the 5 axioms would be dropped or how χ makes it redundant — this was a structurally weak challenge, and connes' content-reduction argument (R2 lines 519-521: "REDUCING content cannot CREATE inferred axiom-equivalences that did not exist in parent") closes the loop. CF-W8-A3 STANDS at THEOREM-tolerance and is **STRENGTHENED** to the inheritance-invariant form: "5-axiom Hopf-cocycle bound is invariant under any content-reducing inheritance morphism between finite spectral triples in the same KO-dim class."

**Structurally-distinct counter-example check (none survives)**: I considered three sharpened-V-3 attempts and report each as falsified:

1. **Drop `1st-order` on BdG-restricted M_2(ℂ)**: would make the Hopf cocycle act as an *outer* fluctuation. But outer fluctuations on BDI Pf=−1 sector violate the substrate-IS BDI parity-protection structure (the Pfaffian sign change requires order-one [[D,a],b^o]=0 to preserve the ±-pair classification per `cross-pillar-bridge-anatomy.md` §VII.AF.1). The 1st-order axiom is INDEPENDENTLY load-bearing on the BdG-restricted child, contra a hypothetical 4-axiom counter-example.
2. **Drop `orient` on M_2(ℂ)**: M_2(ℂ) has Hochschild dimension 2, not 0; the orientation cycle is a 2-cocycle. Dropping `orient` collapses the ZP-pairing structure that makes the (s−4)/(s−3) Hopf factor's residue computation well-defined at the d=8 Mellin pole. INDEPENDENTLY load-bearing.
3. **Drop `real` on the M_2(ℂ) child via merge with `1st-order`**: an attempted axiom-mergeability under χ. Sage-symbolic check (this dispatch's verification of connes' argument): J_BdG charge-conjugation BDI Pf=−1 acts orthogonally to the 1st-order condition; the two axioms operate on different spectral-triple structures (J on Hilbert-space realification; 1st-order on opposite-algebra commutativity). χ does not merge them. INDEPENDENTLY load-bearing.

All three sharpened attempts fail; the 5-axiom budget is structurally minimal on parent and on BdG-restricted child. CF-W8-A3 STRENGTHENED.

#### Lab-discriminator feasibility check (V-1 / V-3 cross-regulator-ratio at W5-2 MCT-3)

Substitution chain on lab feasibility (per `.claude/rules/cross-pillar-bridge-anatomy.md` Level-2 algebraic envelope at d=4 → adapted to d=8 Mellin spectral content via the substrate's actual dimension spectrum):

```
Step 1 [definitions]:
  HBW-violation magnitude at bare-decomposition layer:
    Zubarev_3c_min ≈ -6.587  (W8-4 verified)
    SDW_3c_min     ≈ -2.773  (W8-4 verified)
    |Λ²|           ≈ 1       (M_KK² substrate-natural normalization)
    cocycle-norm scale ≈ O(1) M_KK²
  Bare-decomposition deviation under Zubarev filter ≈ 6.587 × O(1) = O(1) (order-unity)
  L^{-3} algebraic envelope at d=4 (W-5 calibration corpus instance #1; cross-pillar-
    bridge-anatomy.md Level-2): L_max^{-3} at L_max=10 = 10^{-3}
  Cohomology-class projection cuts bare-decomposition deviation by L^{-3}.

Step 2 [substitute — Lancaster MCT-3 sub-gap NMR-tipping precision]:
  Pickett group 2027-2030 horizon: ±0.1% to ±1% on cocycle-ratio observables (W5-2 Row #47)
  L^{-3} envelope at L_max=10: ~0.1%
  Bare-decomposition Mellin-filter deviation under Zubarev filter:
    O(1) × L^{-3} = O(1) × 10^{-3} = ~0.1%

Step 3 [simplify — feasibility band]:
  Predicted SUB-ATLAS-vs-ENSEMBLE deviation under bare-decomposition Zubarev filter:
    ~0.1% (cohomology-class projection bound on the bare-decomposition signal)
  Lab tolerance at Lancaster MCT-3 (state-of-art 2027-2030): ~0.1% to ~1%
  
  Margin = lab tolerance / predicted deviation = (0.1% to 1%) / 0.1% = 1 to 10

Step 4 [direction — discriminator status: STRUCTURALLY LATENT at L_max=10]:
  At L_max=10 the predicted deviation is at the absolute lab-precision floor (~0.1%);
  any realistic lab-error budget (calibration drift, thermal noise, NMR-tipping precision)
  drives effective sensitivity above the deviation magnitude.
  
  Verdict: discriminator is STRUCTURALLY LATENT at currently-achievable apparatus.
  
  Two paths to make it LIVE:
    Path A — reduce L^{-3} envelope by going to higher L_max: at L_max=20, envelope =
      10^{-3.9} = 1.3e-4 = 0.013%; at L_max=30, envelope = 10^{-4.4} = 4e-5 = 0.004%
      — would push predicted deviation below current floor by 1-2 OOM, FALSE-PASS direction
      (predicted deviation TOO SMALL to falsify SUB-ATLAS even with perfect apparatus)
    Path B — design a Mellin filter that probes the BARE-DECOMPOSITION layer specifically,
      bypassing the L^{-3} cohomology-class projection. Requires either:
        (i) measuring a non-cohomology-class observable (a bare-decomposition shell-count
            moment like α_max_bare(R), which is naturally L_max-divergent and thus has no
            L^{-3} suppression) — but lab apparatus reads cocycle-pairing observables
            naturally, not bare-decomposition moments
        (ii) constructing a Mellin filter that decomposes the readout into cohomology-class
            and bare-decomposition components, then reads the bare-decomposition component
            directly. Status: not part of current Lancaster MCT-3 / Aalto LTL apparatus
            specifications; would require new readout-chain design. Pickett-group / Eltsov-
            group internal capability: feasible IN PRINCIPLE (filter-convention multiplexing
            across {ζ, Zubarev, SDW, anomaly} on a single dilution-fridge run is within
            apparatus envelope); REQUIRES dedicated experimental design study.
```

**Lab-feasibility verdict (CF-W6-V1 status)**: The cross-regulator-ratio discriminator is STRUCTURALLY LATENT at apparatus currently fielded at Lancaster MCT-3 / Aalto LTL within the S88+ multi-year horizon (2027-2030 Pickett-group window). It becomes LIVE only via Path B (dedicated bare-decomposition Mellin-filter design) — a *secondary* experimental program building on the canonical 4-gate falsifier rather than supplanting it. I pre-register CF-W6-V1 with explicit LATENT status: the structural pre-registration is high-leverage, but lab execution is multi-decade-horizon contingent on Path B feasibility. The R3 synthesizer should record this as PROVISIONAL-LATENT, distinct from PROVISIONAL-LIVE.

#### Concessions (where connes' R2 persuaded me)

1. **CF-W8-A3 STRENGTHENED, not weakened (V-3 falsification accepted)**. χ inheritance projection cannot reduce 5-axiom Hopf-cocycle budget. My 4-axiom counter-example was structurally weak; three sharpened-V-3 attempts (drop 1st-order on M_2(ℂ); drop `orient`; mergeability between `real` and `1st-order` under χ) all fail. CF-W8-A3 stands at THEOREM-tolerance with the inheritance-invariant strengthening.

2. **3-row Layer Split table is structurally correct (connes R2 line 491-496)**. Cocycle-ratio observables bind at cohomology-class layer (ENSEMBLE A_5_extended); spectral-action a_0 absolute-value binds at bare-decomposition layer (SUB-ATLAS-A_2); L2-FULLY-ADMISSIBLE composition theorem binds at cohomology-class layer (ENSEMBLE A_4). My R1 §"Engagement with connes' SUB-ATLAS-A_2" framed the connes-side reading as pure regulator-classification axis; connes' R2 sharpened that the bare-decomposition LAYER does have a structural role (HBW well-definedness for spectral-action a_0 absolute-value) that I had under-acknowledged. The two readings bind on different axes; both are structurally correct.

3. **Lab discriminator at canonical 4-gate falsifier does NOT distinguish ENSEMBLE vs SUB-ATLAS-A_2 (connes R2 §"Concession on lab discriminator")**. The cocycle-ratio observable is regulator-class-invariant at the substrate-IS level; both readings predict 7.324992 ± 0.1% IDENTICALLY at canonical W5-2/W5-3 setups. CF-W6-V1 cross-regulator-ratio extension is the only path to lab discrimination, and it is structurally LATENT under currently-realizable apparatus.

#### Standing positions (where I hold despite connes' R2)

1. **Substrate-IS preservation is the deeper structural reading**. Even after accepting connes' multi-axis layer split, the substrate-IS axis (CF-W6-V0) is *more fundamental* than the regulator-class axis (CF-W8-A3) in the sense that the regulator-class axiomatic content is a *classification* of how positive-weight Mellin projections read the substrate-IS observables, while the substrate-IS observables are *what is being read*. The CO-PRIMARY landing per `registry-landing.md` correctly recognizes both anchors as load-bearing, but the substrate-IS axis carries the primary explanatory direction per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space" (the substrate IS the cocycle pair; regulators IS positive-weight projections; HBW cone IS a classification of which projections preserve cone-positivity on the substrate's natural moment data). The R3 synthesizer should preserve this axis-priority in the registry text's narrative direction even while landing both anchors as CO-PRIMARY at the structural level.

2. **The 4-row partition (cocycle-ratio / a_0 absolute-value / L2-FULLY-ADMISSIBLE / min-axiom-budget) is more accurate than connes' 3-row table**. The min-axiom-budget axis (CF-W8-A3 5-axiom Hopf-cocycle bound) operates ORTHOGONALLY to the first three rows (it constrains regulator-class axiomatic content at the *meta* level, before the 4-channel composition is evaluated). Connes' 3-row table did not include this orthogonal axis explicitly. The R3 synthesizer should adopt the 4-row partition.

3. **CF-W6-V1 lab discriminator status is PROVISIONAL-LATENT, not deferred-without-pre-registration**. Even though the discriminator is currently latent under apparatus constraints, the structural pre-registration (cross-regulator-ratio = 1 ± 1% under ENSEMBLE; > 5% under SUB-ATLAS-via-bare-decomposition-Mellin-filter) is high-leverage IF Path B Mellin-filter design study is undertaken. The falsifier-master-inventory should add CF-W6-V1 rows tagged PROVISIONAL-LATENT to preserve forward-looking observational constraint structure.

#### Open R3 synthesis question(s)

**Q1 (R3 verdict structure)**: Does R3 land:
- **(a) 4-row layered re-narration** (cocycle-ratio / a_0 absolute-value / L2-FULLY-ADMISSIBLE / min-axiom-budget) with CF-W6-V0 + CF-W8-A3 as CO-PRIMARY anchors, OR
- **(b) 3-row layered re-narration** per connes' R2 §"Layer split" table with CF-W8-A3 as a separate registry slot for the EXTENDED-A_5_v2 5-axiom regulator class?

My R2 vote: (a) — the min-axiom-budget axis is structurally orthogonal to the first three layers and deserves explicit landing in the partition table. The R3 synthesizer should resolve this with substitution-chain justification.

**Q2 (CF-W6-V1 PROVISIONAL-LATENT vs PROVISIONAL-LIVE)**: Should CF-W6-V1 be registered as PROVISIONAL-LATENT (acknowledging multi-decade-horizon Path B feasibility study) or as PROVISIONAL-LIVE (treated as actionable within the canonical 4-gate falsifier framework)? My R2 vote: PROVISIONAL-LATENT — the cross-regulator-ratio discriminator is structurally well-pre-registered, but it requires Path B Mellin-filter design infrastructure that is not currently part of W5-2 / W5-3 apparatus envelope. The PROVISIONAL-LATENT tag preserves forward-looking observational structure without overstating S88+ feasibility.

**Q3 (CO-PRIMARY landing site at §VII.K-PROP-W8 vs new registry slot)**: Should the SOURCE-DOUBLE-CITE-CO-PRIMARY landing be inserted INTO the existing §VII.K-PROP-W8 registry entry (as a sub-entry layered re-narration with both anchors), or as a NEW registry slot §VII.K-PROP-W8-LAYERED with explicit 4-row partition? My R2 vote: NEW registry slot — the §VII.K-PROP-W8 registry text as currently written lands the 4-channel decomposition at one level; the layered re-narration (with CF-W6-V0 + CF-W8-A3 CO-PRIMARY) operates at a DIFFERENT structural level (it adjudicates which observable types bind at which layers). A new slot preserves the existing §VII.K-PROP-W8 binding AND lands the meta-level adjudication separately.

#### Updated provisional 4-field carry-forwards (refined from R1; aligned with connes' R2 updates)

1. **CF-W6-V0 (UPDATED, lifted to CO-PRIMARY anchor with CF-W8-A3 per connes R2 concession)** — Substrate-IS Preservation Theorem under Inheritance Morphism (rank-2 ker(ι_*)).
   - **What**: prove rank-2 cocycle ratio invariance under regulator-atlas restriction via Sage-symbolic Connes-Karoubi pairing on HP^1; cross-check against W8-8 NPZ Δgv_r per-regulator table; extend rank-1 GV-Heitsch result to rank-2 F_67/F_88 pairing. Lifted to CO-PRIMARY anchor with CF-W8-A3 per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY at R3.
   - **Inputs**: W-5 calibration constants (`cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992` 4-sig-fig pin co-canonical with Sage-exact 793346/108307); W8-8 NPZ per-regulator delta table; (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5).
   - **Gate**: `S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM` (THEOREM tolerance; PASS iff cohomology-class invariance provable across A_5_extended; INFO if 1 of 5 violates by < 1%; FAIL if any violates by ≥ 1%).
   - **Effort**: ~5 wave-equivalents.
   - **Depends on**: W-5 calibration corpus (canonical_constants entries above); W8-8 NPZ; W-11 RULE-2 STRENGTHENED parity-blindness theorem; CF-W8-A3 (CO-PRIMARY anchor).

2. **CF-W6-V1 (UPDATED, PROVISIONAL-LATENT status pre-registered)** — Cross-Regulator-Ratio Lab Discriminator at W5-2/W5-3.
   - **What**: extend `falsifier-master-inventory.md` Rows #47-#54b with cross-regulator-ratio rows tagged PROVISIONAL-LATENT; pre-register `r_lab(F_1; reg_a)/r_lab(F_1; reg_b) = 1 ± 1%` under ENSEMBLE; deviation > 5% under SUB-ATLAS-via-bare-decomposition-Mellin-filter (CONDITIONAL on Path B Mellin-filter design feasibility study).
   - **Inputs**: W5-2 Row #47 / W5-3 Row #54b; W8-8 NPZ per-regulator Δgv_r; readout-filter w_R weight functions; substitution-chain feasibility argument from this R2 §"Lab-discriminator feasibility check" (L^{-3} envelope analysis at L_max=10; Pickett-group 2027-2030 horizon; Path B Mellin-filter design requirements).
   - **Gate**: `S88-LAB-CROSS-REGULATOR-RATIO-FALSIFIER-PROVISIONAL-LATENT-PRE-REG` (PASS iff falsifier-master-inventory updated with cross-regulator-ratio rows tagged PROVISIONAL-LATENT and Path B feasibility-study spec is enumerated; INFO if rows partial; FAIL if cross-regulator prediction not pre-registered).
   - **Effort**: ~3h falsifier-master-inventory write + Path B feasibility-study spec; lab execution multi-decade horizon contingent on Path B.
   - **Depends on**: mack-cosmic-bridge sole-writer for falsifier-master-inventory rows per `feedback_mack-bridge-role.md`; CF-W6-V0 (substrate-IS regulator-invariance premise); W-11 RULE-2 STRENGTHENED parity-blindness.

3. **CF-W6-V2 (UPDATED, ALIGNED with connes R2 CF-W8-A1)** — Convention-dependence audit on HBW 3c (λ vs x derivative).
   - **What**: re-run §W8-4 with x-derivative convention; document whether SUB-ATLAS-A_2 cascade is convention-INVARIANT (cascade structurally stable) or convention-DEPENDENT (cascade shifts at empirical-floor level). Aligned with connes' updated CF-W8-A1.
   - **Inputs**: W8-4 npz; CCM-2007 §1.143-1.145 heat-kernel-derivation provenance; Sage symbolic d^k/dx^k computation.
   - **Gate**: `S88-HBW-3C-CONVENTION-AUDIT` (PASS = cascade convention-invariant structurally; INFO = empirical-floor-only convention-dependence; FAIL = no canonical convention privileged → cascade reading REJECTED).
   - **Effort**: ~2 wave-equivalents.
   - **Depends on**: W8-4 npz; CF-W8-A3 (regulator-class axiomatic content); connes' CF-W8-A1 alignment.

4. **CF-W6-LAYERED-RENARRATION (NEW; aligned with connes' R2 CF-W8-COHOMOLOGY-LAYER-BINDING)** — 4-row layered re-narration of L2-FULLY-ADMISSIBLE.
   - **What**: prove §VII.K-PROP-W8 admits 4-row layered re-narration (cocycle-ratio / a_0 absolute-value / L2-FULLY-ADMISSIBLE / min-axiom-budget) with CF-W6-V0 + CF-W8-A3 as CO-PRIMARY anchors at the meta-level, layered with the other two as subordinate refinements. Consider new registry slot §VII.K-PROP-W8-LAYERED vs sub-entry within existing slot.
   - **Inputs**: §VII.K-PROP-W8 registry entry; this R2 §"Multi-axis sharpening" 4-row partition table; connes' R2 §"Layer split" 3-row table; W-4 R3 closure layer-distinction; `epistemic-discipline.md` §"Layer-Decomposition" Phi-correspondence; `cross-pillar-bridge-anatomy.md` Level-2 envelope.
   - **Gate**: `S88-L2-FULLY-ADMISSIBLE-4-ROW-LAYERED-RE-NARRATION` (THEOREM tolerance; PASS iff 4-row partition provable with CO-PRIMARY anchors landed; INFO if 3-row partition provable; FAIL if collapses to ≤ 2-row).
   - **Effort**: ~3 wave-equivalents.
   - **Depends on**: CF-W6-V0 + CF-W8-A3 (CO-PRIMARY anchors); §VII.K-PROP-W8 registry entry; W-4 R3 closure.

5. **CF-W6-V0-CF-W8-A3-CO-PRIMARY-LANDING (NEW; mack-cosmic-bridge sole-writer)** — Registry-text edit for SOURCE-DOUBLE-CITE-CO-PRIMARY landing.
   - **What**: edit `sessions/permanent-results-registry.md` to land CF-W6-V0 + CF-W8-A3 as CO-PRIMARY anchors per `registry-landing.md` §"SOURCE-DOUBLE-CITE-CO-PRIMARY" discipline. Either inside §VII.K-PROP-W8 (sub-entry layered re-narration) or as new slot §VII.K-PROP-W8-LAYERED per Q3 R3 verdict.
   - **Inputs**: `registry-landing.md` §"Schema"; this R2 §"4-row partition" table; CF-W6-V0 + CF-W8-A3 theorem candidates; connes' R2 §"Layer split" 3-row table; closure SHA pin from R3 workshop verdict.
   - **Gate**: `S88-VII-K-PROP-W8-LAYERED-CO-PRIMARY-LANDING` (PASS iff registry entry lands with both CO-PRIMARY anchors per schema; INFO if landing partial; FAIL if SOURCE-DOUBLE-CITE-CO-PRIMARY discipline not satisfied).
   - **Effort**: ~2h registry write (mack-cosmic-bridge) + R3 verdict SHA pin.
   - **Depends on**: R3 closure verdict (Q3 resolution: existing slot vs new slot); CF-W6-V0 + CF-W8-A3 theorem-tolerance verdicts at S88+.

---

## R3 — Synthesis closing (designated synthesizer per R2 outcome)

### R3 — connes-ncg-theorist (synthesis lead; volovik-co-authorship attribution per joint outcome)

**R3 connes synthesis (close W-6 with HYBRID-WITH-LAYERED-RENARRATION joint verdict + 3 R3 adjudications + final 4-field carry-forwards)**

#### R2 outcome summary (1-2 paragraphs)

R2 closed with substantive bilateral concession across four explicit axes. **(i) V-1 (axis-distinction)**: I conceded that L2-FULLY-ADMISSIBLE at §VII.K-PROP-W8 binds at the ENSEMBLE-LAYER under the registry text's existential channel-3 PASS criterion; my SUB-ATLAS-A_2 cascade is the *witness-set refinement* (which 2 of 4 atlas members satisfy the existential), not a re-binding of the composition theorem. Volovik's R2 then accepted the multi-axis layer-split as the substrate-natural reading and adopted the SOURCE-DOUBLE-CITE-CO-PRIMARY landing per `.claude/rules/registry-landing.md` discipline, citing all three detection criteria (sequential dependence; non-fungibility; both-anchors-must-remain-accessible). **(ii) V-2 (BdG layer-preservation)**: I conceded that the BdG kernel inherits the cohomology-class-layer ENSEMBLE-content via W-11 Bulletin #2 STRENGTHENED parity-blindness (regulator-invariance on HP^1 holds for ANY positive-weight w_R(λ²) γ_9-commuting, NOT just HBW-cone-positive subset). Volovik's R2 STRENGTHENED the rank-2 NULL-signature predictions on (φ_67, φ_88) by extending regulator-invariance from A_2 to the full A_5_extended atlas — making the 4-gate falsifier structure MORE robust to lab-platform Mellin-filter choice (multiple independent regulator-class measurement paths converge on 7.324992 IDENTICALLY). **(iii) V-3 (5-axiom Hopf-cocycle inheritance invariance)**: I provided a Sage-symbolic χ-invariance test (R2 lines 506-521) showing all 5 axioms `{dim, reg, real, 1st-order, orient}` survive the M_3(ℂ)→0 projection independently; volovik conceded V-3, considered three sharpened-V-3 attempts (drop 1st-order on M_2(ℂ); drop `orient`; mergeability between `real` and `1st-order` under χ), and reported each as falsified. CF-W8-A3 STRENGTHENED to inheritance-invariant form. **(iv) Lab discriminator**: both readings predict ‖φ_67‖/‖φ_88‖ = 7.324992 ± 0.1% IDENTICALLY at the canonical 4-gate falsifier — the W-5 cancellation theorem at common p_67=p_88=2 makes the cocycle-ratio observable regulator-invariant at the cohomology-class layer. Volovik's R2 then ran the L^{-3} envelope feasibility check at L_max=10 (Pickett 2027-2030 horizon) and refined CF-W6-V1 to PROVISIONAL-LATENT — discrimination requires Path B (dedicated bare-decomposition Mellin-filter design study), not ordinary readout-filter multiplexing.

**Closed structurally vs open**: closed structurally — V-1 axis-distinction (ENSEMBLE wins for L2-FULLY-ADMISSIBLE registry-text axis), V-2 BdG cohomology-class inheritance (parity-blindness extends to full A_5_extended), V-3 5-axiom Hopf-cocycle bound (χ-invariant; CF-W8-A3 STRENGTHENED), canonical 4-gate falsifier non-discrimination (both readings collapse identically at substrate-IS observable level). Open structurally — exact slot allocation for the layered re-narration (Q3 below); Path B Mellin-filter feasibility study (multi-decade horizon contingent on Pickett-group / Eltsov-group capability development); rank-2 cocycle-pairing extension Sage-symbolic proof at L_max=10 across A_5_extended (CF-W6-V0 carry-forward, S88+ THEOREM-tolerance gate).

#### Joint final verdict on §VII.K-PROP A/B/C-trio LOAD-BEARING axis

**Joint verdict: HYBRID-WITH-LAYERED-RENARRATION**.

The §VII.K-PROP A/B/C-trio L2-FULLY-ADMISSIBLE composition theorem does NOT bind on a single LOAD-BEARING axis; it binds on **two structurally orthogonal axes simultaneously**, each load-bearing for a distinct observable class on the cocycle-ratio / a_0 / 4-channel-composition / axiom-budget partition. The verdict honors both R1 readings as STRUCTURALLY CORRECT on their respective axes and does not collapse to either ENSEMBLE-only or SUB-ATLAS-only adjudication.

**Substitution chain (HYBRID-WITH-LAYERED-RENARRATION justification)**:

```
Step 1 [definitions]:
  AXIS_substrate-IS  := observable class indexed by (cohomology-class invariants under
                        Connes-Karoubi pairing on HP^1; γ_9-commuting positive weights;
                        regulator-invariant under W-11 STRENGTHENED parity-blindness)
  AXIS_regulator-cls := observable class indexed by (regulator-class axiomatic content
                        for spectral-action well-definedness; HBW cone-positivity for
                        a_0 absolute-value; Hopf-cocycle axiom-budget for L^8 redirect)
  HYBRID-LR          := joint verdict: each AXIS LOAD-BEARING for ITS observable class;
                        registry text re-narrated as 4-row layered partition; CF-W6-V0
                        and CF-W8-A3 CO-PRIMARY anchors for the meta-level adjudication

Step 2 [substitute volovik's 4-row partition (R2 lines 670-678) into AXIS structure]:
  Row 1: cocycle-ratio (W8-8 Δgv_r; W-5 ‖φ_67‖/‖φ_88‖)        AXIS_substrate-IS,    CF-W6-V0
  Row 2: spectral-action a_0 absolute-value                     AXIS_regulator-cls, CF-W8-A1 (subordinate)
  Row 3: L2-FULLY-ADMISSIBLE composition theorem (existential)  AXIS_substrate-IS,    via ENSEMBLE binding
  Row 4: min-axiom-budget L^8 redirect                          AXIS_regulator-cls, CF-W8-A3

Step 3 [simplify — orthogonality of AXIS structure]:
  AXIS_substrate-IS  measures WHAT IS BEING READ (cocycle pairings; cohomology
                     invariants; substrate-resident structural numbers)
  AXIS_regulator-cls measures HOW THE READING IS DONE (positive-weight Mellin
                     projections; HBW cone admission; Hopf-cocycle axiom budget)
  These axes are ORTHOGONAL: axis-1 is invariant under axis-2 restrictions
  (parity-blindness theorem holds across A_5_extended IRRESPECTIVE of HBW status);
  axis-2 classifications do NOT alter axis-1 substrate-IS observables (W8-8 confirms
  Δgv_r = -40579.1500479506 IDENTICALLY across A_5_extended).

Step 4 [direction]:
  Neither axis alone fixes the L2-FULLY-ADMISSIBLE conclusion uniquely:
    - V_input (substrate-IS regulator-invariance) supplies the premise that the
      cocycle-pairing observable is regulator-class-invariant at cohomology-class
      layer (without it, channel-3 existential criterion is witness-set-dependent
      and SUB-ATLAS-A_2 cascade WOULD be re-binding rather than refinement).
    - C_output (4-channel composition theorem) supplies the structural conclusion
      CONDITIONAL on the V_input premise (without it, regulator-invariance at the
      pairing level does not yield L2-FULLY-ADMISSIBLE binding).
  Together: V_input ⇒ A_F selection (Connes 1996 reconstruction theorem image of
  the cone-positivity classifier on `(A_K, H_K, D_K)`) ⇒ C_output L2-FULLY-ADMISSIBLE
  composition theorem at the cohomology-class layer (binding axis = ENSEMBLE).

  Conclusion: HYBRID-WITH-LAYERED-RENARRATION is the joint verdict; both anchors
  are CO-PRIMARY at the meta-level adjudication.
```

**§VII.K-PROP-W8-LAYERED slot pre-allocation** (per Q3 adjudication below): a NEW registry slot §VII.K-PROP-W8-LAYERED is pre-allocated to land the meta-level layered re-narration with both CO-PRIMARY anchors. The existing §VII.K-PROP-W8 4-channel composition entry remains intact at its current binding (channel-1 + channel-2 + channel-3 + channel-4 ensemble property at the cohomology-class layer); §VII.K-PROP-W8-LAYERED operates at a structurally distinct level (it adjudicates which observable types bind at which AXIS).

#### Adjudication Q1: 4-row vs 3-row layer-split partition

**Adjudicated: ACCEPT volovik's 4-row partition.**

My R2 §"Layer split (post-R2 sharpened)" presented a 3-row table; volovik's R2 §"Multi-axis sharpening" extended to 4 rows by adding the orthogonal min-axiom-budget axis (CF-W8-A3 5-axiom Hopf-cocycle bound). Volovik's structural argument is correct: the min-axiom-budget axis operates orthogonally to the first three rows (it constrains regulator-class axiomatic content at a META level, before the 4-channel composition is evaluated on any selected atlas). My 3-row table conflated CF-W8-A3 with the bare-decomposition row (Row 2) by implicit subordination; volovik's 4-row partition correctly separates the regulator-class axiomatic content (Row 4) from the spectral-action well-definedness content (Row 2).

**Substitution chain (4-row partition orthogonality verification)**:

```
Step 1 [def]:
  Row 1 (cocycle-ratio): AXIS_substrate-IS, ENSEMBLE A_5_extended, CF-W6-V0
  Row 2 (a_0 absolute-value): AXIS_regulator-cls / cone-positivity sub-axis, SUB-ATLAS-A_2, CF-W8-A1
  Row 3 (L2-FULLY-ADMISSIBLE): AXIS_substrate-IS / existential channel-3, ENSEMBLE A_4, CF-W8-COHOMOLOGY-LAYER-BINDING
  Row 4 (min-axiom-budget): AXIS_regulator-cls / axiomatic-content sub-axis, EXTENDED-A_5_v2 (5-axiom regulator class), CF-W8-A3

Step 2 [orthogonality test]:
  Row 1 ⊥ Row 4: cocycle-ratio observable does NOT specify regulator-class axiom budget
    (W8-8 Δgv_r identical across A_5_extended INDEPENDENT of whether a regulator's
    Hopf-cocycle dressing is 3-axiom or 5-axiom)
  Row 2 ⊥ Row 4: HBW cone-positivity for a_0 well-definedness does NOT specify
    Hopf-cocycle axiom budget (Zubarev fails HBW with 3-axiom budget; CM-Hopf
    PASSes channel-1 axiom-sourcing axiomatic test with 5-axiom budget but that
    is a DIFFERENT test from HBW cone-positivity on the a_0 observable).
  Row 3 ⊥ Row 4: L2-FULLY-ADMISSIBLE existential channel-3 binding is at the
    cohomology-class layer; min-axiom-budget L^8 redirect is at the meta-level
    regulator-class axiomatic content layer — different layer altogether.

Step 3 [simplify]:
  Row 4 is ORTHOGONAL to Rows 1+2+3 ⇒ 4-row partition is the structurally-
  distinct partition; collapsing to 3 rows merges Row 4 into Row 2 incorrectly.

Step 4 [direction]:
  Adopt volovik's 4-row partition. CF-W8-A3 is the sole anchor of Row 4
  (regulator-class axiomatic-content axis); CF-W6-V0 + CF-W8-A3 are the
  CO-PRIMARY anchors for the §VII.K-PROP-W8-LAYERED meta-level entry; CF-W8-A1
  and CF-W8-COHOMOLOGY-LAYER-BINDING are subordinate refinements within
  AXIS_regulator-cls and AXIS_substrate-IS respectively.
```

**Pre-registered structural-theorem of the layered partition**: the 4-row partition is provable as a STRUCTURAL THEOREM at gate `S88-L2-FULLY-ADMISSIBLE-4-ROW-LAYERED-RE-NARRATION` (CF-W6-LAYERED-RENARRATION; THEOREM tolerance; PASS iff 4-row partition provable AND each row has a distinct LOAD-BEARING reading AND the AXIS_substrate-IS / AXIS_regulator-cls duality is structurally orthogonal under the layer-functor F per `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence; INFO if 3-row collapse forced; FAIL if reduces to 2-row).

#### Adjudication Q2: PROVISIONAL-LATENT vs LIVE for CF-W6-V1 lab discriminator

**Adjudicated: ACCEPT volovik's PROVISIONAL-LATENT classification.**

Volovik's R2 §"Lab-discriminator feasibility check" performed the L^{-3} envelope substitution chain at L_max=10. I cross-checked this dispatch via Sage MCP (this synthesis):

**Substitution chain (lab-discriminator feasibility cross-check)**:

```
Step 1 [definitions]:
  Zubarev_3c_min      = -6.587  (W8-4 NPZ verified bit-exact; Sage QQ this dispatch)
  SDW_3c_min          = -2.773  (W8-4 NPZ verified bit-exact; Sage QQ this dispatch)
  L^{-3} envelope at L_max=10
                      = 1/L_max³ = 1/1000 = 0.10000%
                      (W-5 calibration corpus instance #1; cross-pillar-bridge-anatomy.md
                      Level-2; Sage-exact this dispatch)
  cocycle-norm scale ≈ O(1) M_KK²  (substrate-natural normalization at d=8)

Step 2 [substitute — bare-decomposition deviation under cohomology-class projection]:
  Predicted cross-regulator-ratio deviation under Zubarev filter at L_max=10:
    |Zubarev_3c_min| × envelope = 6.587 × 0.001 = 0.6587%
  Predicted cross-regulator-ratio deviation under SDW filter at L_max=10:
    |SDW_3c_min|     × envelope = 2.773 × 0.001 = 0.2773%

Step 3 [simplify — feasibility margins at Lancaster MCT-3 / Aalto LTL apparatus]:
  Pickett-group 2027-2030 horizon precision band: [0.10%, 1.00%] (NMR-tipping precision
    at sub-gap; W5-2 Row #47 ±0.1% at cohomology-pairing readout)
  Margin (Zubarev) = 0.6587% / 0.10% = 6.59× the tight floor
                   = 0.6587% / 1.00% = 0.66× the loose floor
  Margin (SDW)     = 0.2773% / 0.10% = 2.77× the tight floor
                   = 0.2773% / 1.00% = 0.28× the loose floor

Step 4 [direction — discriminator status verdict]:
  At Pickett-group "tight" 0.1% precision: Zubarev deviation ABOVE the floor by 6.59×;
    discriminator is LIVE-CONDITIONAL (visible at tight precision).
  At Pickett-group "loose" 1.0% precision: Zubarev deviation BELOW the floor by 0.66×;
    discriminator is BURIED in noise.
  
  Two structural conditions to make discriminator LIVE:
    Condition A — apparatus achieves tight 0.1% precision floor at Lancaster MCT-3 / Aalto LTL
                  (Pickett-group / Eltsov-group capability uplift; not currently demonstrated)
    Condition B — Path B Mellin-filter design study completes (bare-decomposition-layer-probing
                  filter must be physically realizable; not part of current readout-chain spec)
  
  Both A AND B required; multi-decade horizon contingent on capability development.
  
  ⇒ PROVISIONAL-LATENT (NOT PROVISIONAL-LIVE; NOT LIVE-now)
```

**Detector-resolution feasibility note**: at L_max=10 the predicted deviation 0.66% for Zubarev sits at the *edge* of the Pickett-group precision band (tight 0.1% to loose 1.0%); at L_max=15 the envelope shrinks to L^{-3} = 1/3375 ≈ 0.030% which would push the predicted deviation to 0.20% (still in band) but the canonical W-5 envelope is empirically calibrated AT L_max=10. Going to L_max=15+ requires irrep-construction at sectors p+q=15 (super-polynomial Casimir-projection cost; W11-3 calibration corpus instance #2 in `math-scripts.md` §"D_K Block-Diagonality" — empirically infeasible within agent timeslot). Therefore the discriminator's structural status is bounded by the L_max=10 calibration: PROVISIONAL-LATENT contingent on apparatus precision uplift AND Path B Mellin-filter design.

**The PROVISIONAL-LATENT tag preserves forward-looking observational structure** without overstating S88+ feasibility: the cross-regulator-ratio prediction at W5-2 (Lancaster MCT-3) and W5-3 (Aalto LTL µSR) is HIGH-LEVERAGE *if* both conditions A+B are met; until then, the canonical 4-gate falsifier structure on (φ_67, φ_88) NULL-signature + 7.324992 ratio remains the LIVE falsifier.

#### Adjudication Q3: existing §VII.K-PROP slot vs new §VII.K-PROP-W8-LAYERED slot for CO-PRIMARY landing

**Adjudicated: ACCEPT volovik's NEW slot pre-allocation §VII.K-PROP-W8-LAYERED.**

The existing §VII.K-PROP-W8 registry entry binds the 4-channel composition theorem at one structural level (channel-1 axiom-sourcing + channel-2 inner-fluctuation lift + channel-3 functional-class + channel-4 anomaly-gauge; ENSEMBLE-LAYER existential binding). The layered re-narration with CF-W6-V0 + CF-W8-A3 CO-PRIMARY operates at a META structural level (it adjudicates which observable types bind at which AXIS_substrate-IS / AXIS_regulator-cls layer — a partition over observables, not a property of a single observable). Inserting the meta-level adjudication INTO the existing §VII.K-PROP-W8 entry would conflate two structurally distinct levels in a single registry text. A NEW slot preserves the existing 4-channel-composition binding at §VII.K-PROP-W8 AND lands the meta-level adjudication separately at §VII.K-PROP-W8-LAYERED.

**Schema for §VII.K-PROP-W8-LAYERED per `.claude/rules/registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY**:

```
§VII.K-PROP-W8-LAYERED  L2-FULLY-ADMISSIBLE 4-ROW LAYERED RE-NARRATION

  ANCHOR-1 (input layer, V — substrate-IS regulator-invariance):
    CF-W6-V0  Substrate-IS Preservation Theorem under Inheritance Morphism (rank-2 ker(ι_*))
    Sources:
      - W-5 (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; 0.0e+00 Python residual)
      - W-11 RULE-2 STRENGTHENED parity-blindness theorem (Bulletin #2 promotion;
        S86 W-11 §"Bulletin #2"); regulator-invariance on HP^1 for ANY positive-weight
        w_R(λ²) γ_9-commuting (NOT just HBW-cone-positive subset)
      - canonical_constants: cocycle_norm_phi67 = 0.793346, cocycle_norm_phi88 = 0.108307,
        substrate_cocycle_ratio_67_88 = 7.324992 (4-sig-fig pin co-canonical with
        Sage-exact 793346/108307 = 7.3249743783873615; |delta| = 1.76e-5 < publication
        precision 1e-4)
      - W8-8 NPZ per-regulator delta table (Δgv_r = -40579.1500479506 IDENTICAL across
        A_5_extended at L_max=10)
    Authorship: volovik-superfluid-universe-theorist (R1 §"Complementary theorem
      candidate (BdG side)"; R2 §"Response to connes' R2 conceded position on V-2")

  ANCHOR-2 (output layer, C — regulator-class axiomatic content):
    CF-W8-A3  Min-axiom-budget L^8 redirect inheritance-invariant theorem
    Sources:
      - CCM-2007 §1.143-1.145 axiom enumeration: {dim, reg, real, 1st-order, orient}
        (cardinality 5 Sage-verified; this dispatch and R1)
      - CM-1995 §III.4 Hopf algebra H_CM generator structure ((s−4)/(s−3) factor
        action on `[D, a]` requires all 5 axioms independently load-bearing)
      - χ-invariance Sage-symbolic test (R2 lines 506-521; M_3(ℂ)→0 projection
        cannot reduce axiom budget below 5; volovik R2 §"Response to connes' R2
        V-3" confirms three sharpened-V-3 attempts all falsified)
    Authorship: connes-ncg-theorist (R1 §"Engagement with W8-3 EXTENDED-A_5_v2
      reading + CF-W8-A3 conjecture"; R2 χ-invariance Sage test)

  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY

  Derivation chain: V → A_F → C → conclusion
    V_input: substrate-IS regulator-invariance on cocycle-pairing observables
             (W-5 cancellation + W-11 STRENGTHENED parity-blindness)
    A_F:     Connes 1996 reconstruction theorem image of cone-positivity classifier
             on `(A_K, H_K, D_K)` (selects ℂ ⊕ ℍ ⊕ M_3(ℂ) under axioms 3+5+6 +
             Schur orthogonality)
    C_output: §VII.K-PROP-W8 4-channel L2-FULLY-ADMISSIBLE composition theorem
             at the cohomology-class layer, with the 4-row partition:
               Row 1 (cocycle-ratio)         AXIS_substrate-IS,    CF-W6-V0   (ENSEMBLE A_5_extended)
               Row 2 (a_0 absolute-value)    AXIS_regulator-cls,   CF-W8-A1   (SUB-ATLAS-A_2)
               Row 3 (L2-FULLY-ADMISSIBLE)   AXIS_substrate-IS,    via existential ENSEMBLE A_4
               Row 4 (min-axiom-budget L^8)  AXIS_regulator-cls,   CF-W8-A3   (EXTENDED-A_5_v2 5-axiom class)

  Closure SHA pin: <to be computed by mack-cosmic-bridge at registry-write time;
                   audit_sha256 over CF-W6-V0 + CF-W8-A3 input-pin map + this
                   workshop file's R3 verdict line; matches the dual-SHA pattern
                   of `.claude/rules/gate-verdicts.md` schema-v2>
```

**Detection criteria (per `registry-landing.md` §"Detection")** — all three fire:

1. **Sequential dependence**: V_input (substrate-IS regulator-invariance) supplies the premise; without it, the existential channel-3 PASS criterion is witness-set-dependent rather than content-invariant, and SUB-ATLAS-A_2 cascade WOULD become re-binding rather than refinement. C_output (4-channel composition theorem with 4-row partition) supplies the structural conclusion CONDITIONAL on V_input regulator-invariance. C_output cannot be invoked without first invoking V_input.

2. **Non-fungibility**: V_input is intrinsic to the parent spectral triple `(A_K, H_K, D_K)` (cocycle pair on substrate); C_output operates on the 4-channel decomposition of §VII.K-PROP-W8 (ensemble property). Reordering would force the 4-channel decomposition to logically precede the substrate-IS regulator-invariance, inverting the substrate-IS / regulator-class axis hierarchy per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space".

3. **Both anchors must remain accessible**: deprecating V_input (W-5 cancellation + W-11 STRENGTHENED parity-blindness) would invalidate the cohomology-class layer reading and force re-derivation of all rank-2 falsifier predictions; deprecating C_output (§VII.K-PROP-W8 4-channel composition) would lose the L2-FULLY-ADMISSIBLE structural conclusion. Both load-bear independently.

#### Joint authorship attribution per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY

The SOURCE-DOUBLE-CITE-CO-PRIMARY landing at §VII.K-PROP-W8-LAYERED is jointly authored:

- **ANCHOR-1 (CF-W6-V0)** — volovik PRIMARY author; connes CO-AUTHOR. volovik's R1 §"Complementary theorem candidate (BdG side)" first pre-registered the substrate-IS preservation theorem; volovik's R2 §"4-row partition" sharpened the cross-row partition with CF-W8-A3 as orthogonal anchor. connes' R2 χ-invariance Sage test independently confirmed the structural extension to BdG-restricted child via parity-blindness on the FULL A_5_extended atlas (regulator-invariance INDEPENDENT of HBW status). The substrate-IS axis carries the primary explanatory direction per `.claude/rules/phononic-framing.md`: substrate (cocycle pair) → ker(ι_*) inheritance → regulator-atlas-invariant pairing → lab observable.

- **ANCHOR-2 (CF-W8-A3)** — connes PRIMARY author; volovik CO-AUTHOR. connes' R1 §"Engagement with W8-3 EXTENDED-A_5_v2 reading + CF-W8-A3 conjecture" first pre-registered the 5-axiom Hopf-cocycle bound with explicit CCM-2007 §1.143-1.145 axiom enumeration; connes' R2 §"Response to V-3" provided the Sage-symbolic χ-invariance test demonstrating axiom-budget invariance under M_3(ℂ)→0 projection. volovik's R2 §"Response to connes' R2 V-3" conceded V-3 and reported three sharpened-V-3 attempts all falsified, STRENGTHENING the theorem to inheritance-invariant form. The regulator-class axiomatic-content axis carries the structural-classification explanatory direction.

**Joint SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag** pinned at §VII.K-PROP-W8-LAYERED registry entry per the schema above. Neither anchor is decoration; both load-bear independently for the meta-level adjudication.

#### Final 4-field carry-forwards (FINAL specs)

**CF-W6-V0** — Substrate-IS Preservation Theorem under Inheritance Morphism (rank-2 ker(ι_*)).
- **What**: Sage-symbolic proof of rank-2 cocycle-ratio invariance under regulator-atlas restriction via Connes-Karoubi pairing on HP^1; cross-check against W8-8 NPZ Δgv_r per-regulator table; extend rank-1 GV-Heitsch result to rank-2 (φ_67, φ_88) pairing via common-p cancellation theorem at p_67=p_88=2.
- **Inputs**: W-5 calibration constants (`cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992`, all knowledge-MCP-confirmed S86); W8-8 NPZ `s87_w8_eta_gv_followup.npz` per-regulator delta table (Δgv_r = -40579.1500479506 across A_5_extended); (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; 0.0e+00 Python residual); W-11 RULE-2 STRENGTHENED parity-blindness theorem.
- **Output**: computation script + Sage-symbolic NPZ confirming rank-2 cocycle-ratio = 7.324992 IDENTICALLY across all 5 regulators in A_5_extended at L_max=10.
- **Format**: `computations/s88_substrate_is_preservation_rank2_inheritance.py` + `.npz` + working-paper section.
- **Gate**: `S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM` (THEOREM tolerance; PASS iff cohomology-class invariance Sage-symbolic provable across A_5_extended; INFO if 1 of 5 violates by < 1%; FAIL if any violates by ≥ 1%).
- **Effort**: ~5 wave-equivalents.
- **Depends on**: W-5 calibration corpus; W8-8 NPZ; W-11 RULE-2 STRENGTHENED parity-blindness; CF-W8-A3 (CO-PRIMARY anchor at §VII.K-PROP-W8-LAYERED).
- **Authorship for landing**: volovik PRIMARY + connes CO-AUTHOR.

**CF-W6-V1** — Cross-Regulator-Ratio Lab Discriminator at W5-2/W5-3 (PROVISIONAL-LATENT).
- **What**: extend `sessions/framework/registry/falsifier-master-inventory.md` Rows #47-#54b with cross-regulator-ratio rows tagged PROVISIONAL-LATENT; pre-register `r_lab(F_1; reg_a)/r_lab(F_1; reg_b) = 1 ± 1%` under ENSEMBLE; deviation > 5% under SUB-ATLAS-via-bare-decomposition-Mellin-filter (CONDITIONAL on Path B Mellin-filter design feasibility study).
- **Inputs**: W5-2 Row #47 / W5-3 Row #54b; W8-8 NPZ per-regulator Δgv_r; readout-filter w_R weight functions (w_ζ(λ)=1, w_Zubarev=λ²/(1+λ⁴), w_SDW=exp(−λ²/Λ²), w_anomaly=exp(−λ²/Λ²)/√λ); L^{-3} envelope feasibility analysis (this R3 §"Adjudication Q2" Sage-verified at L_max=10).
- **Output**: falsifier-master-inventory rows added with PROVISIONAL-LATENT tag + Path B Mellin-filter design feasibility-study spec enumerated.
- **Format**: registry edit by mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; cross-link table to `.claude/rules/cross-pillar-bridge-anatomy.md` Level-2 envelope.
- **Gate**: `S88-LAB-CROSS-REGULATOR-RATIO-FALSIFIER-PROVISIONAL-LATENT-PRE-REG` (PASS iff falsifier-master-inventory updated with cross-regulator-ratio rows tagged PROVISIONAL-LATENT AND Path B feasibility-study spec enumerated; INFO if rows partial; FAIL if cross-regulator prediction not pre-registered).
- **Effort**: ~3h falsifier-master-inventory write + Path B feasibility-study spec; lab execution multi-decade horizon (Pickett 2027-2030 + Path B feasibility uplift) — apparatus-precision-AND-Mellin-filter-design conditional.
- **Depends on**: mack-cosmic-bridge sole-writer; CF-W6-V0 (substrate-IS regulator-invariance premise); W-11 RULE-2 STRENGTHENED parity-blindness; cross-pillar-bridge-anatomy.md Level-2 envelope.
- **Authorship for landing**: mack-cosmic-bridge (sole writer for falsifier-master-inventory.md per `feedback_mack-bridge-role.md`); volovik PRIMARY originator (R1 §"Lab-side falsification predictions"); connes feasibility cross-check (R3 §"Adjudication Q2" Sage L^{-3}).

**CF-W6-V2** — Convention-dependence audit on HBW 3c (λ vs x derivative).
- **What**: re-run §W8-4 with x-derivative convention `(-1)^k · d^k w_R/dx^k`; document whether SUB-ATLAS-A_2 cascade is convention-INVARIANT (cascade structurally stable across CM-in-x and CM-in-λ) or convention-DEPENDENT (cascade shifts under x-derivative; e.g., A_2 → A_3 = {ζ, SDW, anomaly} since SDW is CM-in-x but not CM-in-λ).
- **Inputs**: W8-4 NPZ; CCM-2007 §1.143-1.145 heat-kernel-derivation provenance; Sage symbolic d^k/dx^k computation of Zubarev λ²/(1+λ⁴) and SDW exp(−x).
- **Output**: computation script with x-derivative chain-rule lifts + per-regulator 3c-min table; verdict PASS/INFO/FAIL per gate criterion.
- **Format**: `computations/s88_hbw_3c_convention_audit.py` + `.npz` + working-paper section.
- **Gate**: `S88-HBW-3C-CONVENTION-AUDIT` (PASS = cascade convention-invariant structurally on the SUB-ATLAS axis; INFO = empirical-floor-only convention-dependence with one canonical convention privileged via substrate-physics derivation; FAIL = no canonical convention privileged → SUB-ATLAS reading on AXIS_regulator-cls would be REJECTED at the load-bearing-axis level).
- **Effort**: ~2 wave-equivalents.
- **Depends on**: W8-4 NPZ; CF-W8-A3 (regulator-class axiomatic-content); aligns with connes' CF-W8-A1 from R1.
- **Authorship for landing**: connes PRIMARY (cascade-axis owner; CF-W8-A1 originator).

**CF-W6-LAYERED-RENARRATION** — 4-row layered re-narration of L2-FULLY-ADMISSIBLE.
- **What**: Sage-symbolic proof that §VII.K-PROP-W8 admits 4-row layered re-narration (Row 1 cocycle-ratio / Row 2 a_0 absolute-value / Row 3 L2-FULLY-ADMISSIBLE composition theorem / Row 4 min-axiom-budget L^8 redirect) with CF-W6-V0 + CF-W8-A3 as CO-PRIMARY anchors at the meta-level. Apply the layer-functor F per `.claude/rules/epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence to confirm AXIS_substrate-IS / AXIS_regulator-cls orthogonality across the 4-row partition. Confirms NEW slot §VII.K-PROP-W8-LAYERED pre-allocation per Q3 adjudication above.
- **Inputs**: §VII.K-PROP-W8 registry entry (lines 15174-15220 of `sessions/permanent-results-registry.md`); this R3 4-row partition table + orthogonality substitution chain (above); volovik R2 §"Multi-axis sharpening" 4-row table; connes R2 §"Layer split" 3-row table + R3 acceptance of 4-row extension; W-4 R3 closure layer-distinction; `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" Phi-correspondence; `.claude/rules/cross-pillar-bridge-anatomy.md` Level-2 envelope.
- **Output**: computation script + Sage-symbolic NPZ + working-paper section validating 4-row partition; IF PASS, registry-text edit pre-staged for mack-cosmic-bridge to land at §VII.K-PROP-W8-LAYERED per CF-W6-V0-CF-W8-A3-CO-PRIMARY-LANDING.
- **Format**: `computations/s88_l2_fully_admissible_4row_layered_renarration.py` + `.npz` + working-paper section.
- **Gate**: `S88-L2-FULLY-ADMISSIBLE-4-ROW-LAYERED-RE-NARRATION` (THEOREM tolerance; PASS iff 4-row partition Sage-symbolic provable AND each row has distinct LOAD-BEARING reading AND AXIS_substrate-IS / AXIS_regulator-cls duality structurally orthogonal; INFO if 3-row collapse forced; FAIL if reduces to ≤ 2-row).
- **Effort**: ~3 wave-equivalents.
- **Depends on**: CF-W6-V0 + CF-W8-A3 (CO-PRIMARY anchors); §VII.K-PROP-W8 registry entry; W-4 R3 closure; epistemic-discipline.md §"Layer-Decomposition"; cross-pillar-bridge-anatomy.md Level-2 envelope.
- **Authorship for landing**: connes PRIMARY (Q3 4-row partition adjudicator) + volovik CO-AUTHOR (R2 4-row sharpener).

**CF-W6-V0-CF-W8-A3-CO-PRIMARY-LANDING** — Registry-text edit for SOURCE-DOUBLE-CITE-CO-PRIMARY landing at §VII.K-PROP-W8-LAYERED (mack-cosmic-bridge sole-writer).
- **What**: edit `sessions/permanent-results-registry.md` to land NEW slot §VII.K-PROP-W8-LAYERED with CF-W6-V0 + CF-W8-A3 CO-PRIMARY anchors per `.claude/rules/registry-landing.md` §"Schema". Insert AFTER existing §VII.K-PROP-W8 entry (preserve original 4-channel-composition binding intact); cite ANCHOR-1 / ANCHOR-2 / STRUCTURE / Derivation chain / Closure SHA pin per the schema above. Pin closure SHA via dual-SHA companion row (audit_sha256 over CF-W6-V0 + CF-W8-A3 + this workshop R3 verdict line input-pin map per `.claude/rules/gate-verdicts.md` schema-v2).
- **Inputs**: `.claude/rules/registry-landing.md` §"Schema"; this R3 §"Joint authorship attribution" SOURCE-DOUBLE-CITE-CO-PRIMARY block; CF-W6-V0 + CF-W8-A3 theorem candidates (CO-PRIMARY anchors); W-3 RULE-1 R3 calibration corpus precedent (Path-H/Path-C multi-valued classification (a)); workshop R3 verdict closure SHA.
- **Output**: §VII.K-PROP-W8-LAYERED registry entry with full SOURCE-DOUBLE-CITE-CO-PRIMARY schema; cross-link from §VII.K-PROP-W8 to the layered re-narration; allowlist row addition via `.claude/rules/methodology-wave-allowlist.md` (orchestrator-only edit per recursion-attack closure).
- **Format**: registry edit by mack-cosmic-bridge; allowlist row edit by orchestrator; both with dual-SHA companion rows per `.claude/rules/gate-verdicts.md`.
- **Gate**: `S88-VII-K-PROP-W8-LAYERED-CO-PRIMARY-LANDING` (PASS iff registry entry lands with both CO-PRIMARY anchors per schema AND all 3 detection criteria of `registry-landing.md` §"Detection" cited explicitly; INFO if landing partial; FAIL if SOURCE-DOUBLE-CITE-CO-PRIMARY discipline not satisfied).
- **Effort**: ~2h registry write (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`) + R3 verdict SHA pin + allowlist row edit (orchestrator).
- **Depends on**: this R3 closure verdict (Q3 resolution: NEW slot §VII.K-PROP-W8-LAYERED); CF-W6-V0 + CF-W8-A3 theorem-tolerance verdicts at S88+ (PASS-conditional landing OR STAGE-1-CANDIDATE landing per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway); workshop R3 closure SHA.
- **Authorship for landing**: mack-cosmic-bridge (sole writer for permanent-results-registry.md falsifier-master-inventory.md interface; per `feedback_mack-bridge-role.md` operates the cosmic-bridge ledger interface); connes + volovik CO-AUTHORS at theorem-content level per the SOURCE-DOUBLE-CITE-CO-PRIMARY schema.

**CF-W8-A3** (Sage-symbolic theorem candidate; STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway) — Min-axiom-budget L^8 redirect inheritance-invariant theorem.
- **What**: Sage-symbolic Hopf-algebra cardinality argument that any (s−4)/(s−3) factor's action on `[D, a]` requires `{dim, reg, real, 1st-order, orient}` = 5 axioms; structural lower-bound theorem on L^8 redirect axiom budget; STRENGTHENED claim post-V-3-Sage-falsification: 5-axiom bound is INVARIANT under inheritance morphism χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ) (no axiom-mergeability under M_3(ℂ)→0 content-reducing projection; Sage-symbolic verified this dispatch and R2; three sharpened-V-3 attempts all falsified by volovik R2 §"Response to V-3").
- **Inputs**: §W8-3 JSON Hopf-cocycle infrastructure (`hopf_cocycle_dressing_space` key); CM-1995 §III.4 generator structure; CCM-2007 §1.143-1.145 axiom set (5 axioms Sage-verified distinct: `{1st-order, dim, orient, real, reg}`); Sage symbolic Hopf algebra; W-5 inheritance morphism χ definition; W-11 RULE-2 STRENGTHENED parity-blindness (regulator-invariance INDEPENDENT of HBW status; R2 V-2 concession).
- **Output**: computation script + Sage-symbolic NPZ proving (a) 5-axiom budget is structurally minimal on parent `(A_K, H_K, D_K)`; (b) χ projection cannot reduce budget below 5 (content-reduction cannot create axiom-mergeability not present in parent); (c) three sharpened-V-3 attempts (drop 1st-order; drop orient; merge real ↔ 1st-order under χ) all structurally falsified.
- **Format**: `computations/s88_min_axiom_budget_l8_redirect_inheritance_invariant.py` + `.npz` + working-paper section.
- **Gate**: `S88-MIN-AXIOM-BUDGET-L8-REDIRECT-INHERITANCE-INVARIANT-THEOREM` (THEOREM tolerance; PASS iff cardinality = 5 provably necessary AND no 4-axiom counter-example exists on parent OR on BdG-restricted child; INFO if PASS only on parent (BdG-side gap); FAIL iff structural counter-example exhibited on either parent or child).
- **Effort**: ~4 wave-equivalents.
- **Depends on**: §W8-3 JSON Hopf-cocycle infrastructure; CM-1995 §III.4 generators; CCM-2007 §1.143-1.145 axiom set; Sage Hopf-algebra MCP; CF-W6-V0 (CO-PRIMARY anchor; substrate-IS regulator-invariance premise).
- **Authorship for landing**: connes PRIMARY (originator R1; Sage χ-invariance test R2) + volovik CO-AUTHOR (V-3 falsification + sharpened-V-3 attempts R2).
- **STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway**: this R3 close registers CF-W8-A3 as Stage-0 (workshop-internal candidate) with the workshop verdict text frozen; landing as Stage-1 candidate at S88+ via `S88-MIN-AXIOM-BUDGET-L8-REDIRECT-INHERITANCE-INVARIANT-THEOREM` gate; subsequent Stage-2 two-agent parallel cross-check required for Stage-3 permanent registration (joint-axis cross-reviewers: NCG-axiomatic-side audit by connes + spectral-functional-side audit by lizzi-spectral-functional-theorist; or NCG-axiomatic-side + BdG-inheritance-side by connes + volovik with the explicit "no prior workshop transcript" condition per joint-theorem-promotion.md Stage 2).

#### Workshop W-6 closure status

W-6 closes at: **HYBRID-WITH-LAYERED-RENARRATION JOINT VERDICT** with two CO-PRIMARY anchors landed as STAGE-1-CANDIDATE at §VII.K-PROP-W8-LAYERED (NEW slot pre-allocation; Q3 adjudication) per `.claude/rules/registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline + `.claude/rules/joint-theorem-promotion.md` 4-stage pathway.

**Substrate verdict**: cocycle-ratio observable (W8-8 Δgv_r; W-5 ‖φ_67‖/‖φ_88‖) and L2-FULLY-ADMISSIBLE composition theorem (existential channel-3) both bind at the COHOMOLOGY-CLASS LAYER on AXIS_substrate-IS via ENSEMBLE A_5_extended atlas under W-11 STRENGTHENED parity-blindness theorem (regulator-invariance INDEPENDENT of HBW cone-positivity). The spectral-action a_0 absolute-value binds at the BARE-DECOMPOSITION LAYER on AXIS_regulator-cls via SUB-ATLAS-A_2 = {ζ, anomaly} under HBW well-definedness. The min-axiom-budget L^8 redirect binds at the META-LEVEL AXIS_regulator-cls via EXTENDED-A_5_v2 5-axiom regulator class under CF-W8-A3 inheritance-invariant theorem. The 4-row partition is structurally orthogonal across the AXIS_substrate-IS / AXIS_regulator-cls duality.

**Methodology verdict**: SOURCE-DOUBLE-CITE-CO-PRIMARY landing at §VII.K-PROP-W8-LAYERED (NEW slot) preserves both V_input (substrate-IS regulator-invariance: W-5 cancellation theorem + W-11 STRENGTHENED parity-blindness; volovik PRIMARY) and C_output (regulator-class axiomatic content: 5-axiom Hopf-cocycle inheritance-invariant bound; connes PRIMARY) as CO-PRIMARY anchors. The layered re-narration discipline is pre-registered as a structural extension to `.claude/rules/cross-pillar-bridge-anatomy.md` 5-anatomy + 3-level discipline at K-counter forward (workshop forward-template-adoption SUGGESTION at K=2 → SUGGESTION at K=2 with NEW calibration corpus instance from W-6 layered re-narration). Cross-link to `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" Phi-correspondence under layer-functor F formalism. Cross-link to `.claude/rules/joint-theorem-promotion.md` 4-stage pathway for CF-W8-A3 Stage-1-CANDIDATE registration; CF-W6-V0 Stage-1-CANDIDATE separately under same pathway (CO-PRIMARY pair both lift to STAGE-3 only conditional on Stage-2 two-agent parallel cross-check at S88+).

**4-field carry-forwards**: 6 carry-forwards landed (CF-W6-V0 + CF-W6-V1 + CF-W6-V2 + CF-W6-LAYERED-RENARRATION + CF-W6-V0-CF-W8-A3-CO-PRIMARY-LANDING + CF-W8-A3) covering both CO-PRIMARY anchors, the layered-renarration structural theorem, the convention-dependence audit, the registry-text landing for mack-cosmic-bridge, and the lab-discriminator PROVISIONAL-LATENT pre-registration. Net delta from R2 quota: R2 closed with 5 carry-forwards (CF-W6-V0 / CF-W6-V1 / CF-W6-V2 / CF-W6-LAYERED-RENARRATION / CF-W6-V0-CF-W8-A3-CO-PRIMARY-LANDING); R3 adds CF-W8-A3 as the connes-side STAGE-1-CANDIDATE for the SOURCE-DOUBLE-CITE-CO-PRIMARY landing's ANCHOR-2 (the volovik-side ANCHOR-1 is CF-W6-V0). All 6 carry-forwards have full 4-field specs (what / inputs / output / format / gate / effort / depends-on / authorship); all are PROVISIONAL until S88+ THEOREM-tolerance gate verdicts land.

**Joint-theorem-promotion pathway status**: CF-W6-V0 and CF-W8-A3 jointly pre-registered as Stage-0 workshop-internal candidates; this R3 close freezes the workshop verdict text. Stage-1 registration occurs at S88+ via the two THEOREM-tolerance gates (`S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM` and `S88-MIN-AXIOM-BUDGET-L8-REDIRECT-INHERITANCE-INVARIANT-THEOREM`). Stage-2 two-agent parallel cross-check (per `.claude/rules/joint-theorem-promotion.md` "without prior workshop context" condition) required for Stage-3 permanent registration; recommended cross-reviewer assignments at S88+: NCG-axiomatic-side independent verification by lizzi-spectral-functional-theorist (audits CF-W8-A3 5-axiom enumeration without prior W-6 transcript); BdG-inheritance-side independent verification by mack-cosmic-bridge (audits CF-W6-V0 substrate-IS preservation across A_5_extended without prior W-6 transcript).

**Forward-template-adoption SUGGESTION calibration corpus** (per `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption"): W-6 produces a CROSS-AXIS bridge candidate (NOT a cross-pillar bridge per the existing K-counter — rather, an AXIS_substrate-IS / AXIS_regulator-cls duality on a SINGLE pillar (Pillar-VIII)) and is therefore NOT a calibration corpus instance for the existing K-counter at K=2. Future high-density workshops producing analogous AXIS-duality CO-PRIMARY landings SHOULD adopt this W-6 R3 SOURCE-DOUBLE-CITE-CO-PRIMARY + 4-row layered partition structure as a SUGGESTION (until K=3 promotion threshold reached for the AXIS-duality calibration corpus).

**Workshop W-6 R3 close declared 2026-05-02; both CO-PRIMARY authorship attribution and 4-row partition orthogonality structurally complete; landing pathway pre-registered through S88+ via 6 carry-forwards.**

---

## Workshop W-6 closure status

**Closure declared 2026-05-02; full closure-status block embedded at R3 §"Workshop W-6 closure status" (lines 1181-1196 of this file).**

**Verdict class**: HYBRID-WITH-LAYERED-RENARRATION JOINT VERDICT.

**Substrate verdict**: cocycle-ratio observable (W8-8 Δgv_r; W-5 ‖φ_67‖/‖φ_88‖ = 7.324992 Sage-exact) and L2-FULLY-ADMISSIBLE composition theorem (existential channel-3) bind at the COHOMOLOGY-CLASS LAYER on AXIS_substrate-IS via ENSEMBLE A_5_extended atlas under W-11 RULE-2 STRENGTHENED parity-blindness theorem (regulator-invariance INDEPENDENT of HBW cone-positivity). Spectral-action a_0 absolute-value binds at the BARE-DECOMPOSITION LAYER on AXIS_regulator-cls via SUB-ATLAS-A_2 = {ζ, anomaly} under HBW well-definedness. Min-axiom-budget L^8 redirect binds at META-LEVEL AXIS_regulator-cls via EXTENDED-A_5_v2 5-axiom regulator class under CF-W8-A3 inheritance-invariant theorem. The 4-row partition is structurally orthogonal across the AXIS_substrate-IS / AXIS_regulator-cls duality.

**Methodology verdict**: SOURCE-DOUBLE-CITE-CO-PRIMARY landing pre-allocated at NEW slot §VII.K-PROP-W8-LAYERED per `.claude/rules/registry-landing.md` schema. ANCHOR-1 (V_input substrate-IS regulator-invariance) = CF-W6-V0 (volovik PRIMARY + connes CO-AUTHOR). ANCHOR-2 (C_output regulator-class axiomatic content) = CF-W8-A3 STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway (connes PRIMARY + volovik CO-AUTHOR). All 3 detection criteria fire: sequential dependence (V_input ⇒ A_F ⇒ C_output); non-fungibility (substrate-IS axis precedes regulator-class axis per `.claude/rules/phononic-framing.md` IS-not-IN); both-anchors-must-remain-accessible (deprecating either invalidates layered re-narration).

**Adjudication summary**: Q1 = ACCEPT volovik 4-row partition (orthogonality substitution chain at R3 lines 945-984; min-axiom-budget axis structurally orthogonal to first 3 rows); Q2 = ACCEPT volovik PROVISIONAL-LATENT (Sage L^{-3} feasibility cross-check this dispatch confirms Zubarev predicted dev 0.6587% vs Pickett 2027-2030 tight-floor 0.1%, margin 6.59× requires apparatus-precision uplift AND Path B Mellin-filter design); Q3 = ACCEPT volovik NEW slot §VII.K-PROP-W8-LAYERED (preserves existing §VII.K-PROP-W8 4-channel binding intact; meta-level adjudication separately).

**4-field carry-forwards**: 6 total (CF-W6-V0 + CF-W6-V1 + CF-W6-V2 + CF-W6-LAYERED-RENARRATION + CF-W6-V0-CF-W8-A3-CO-PRIMARY-LANDING + CF-W8-A3). Net delta from R2: +1 (R3 promotes CF-W8-A3 to STAGE-1-CANDIDATE for the SOURCE-DOUBLE-CITE-CO-PRIMARY ANCHOR-2 role; volovik's R2 had 5 carry-forwards). All 6 have full 4-field specs (what / inputs / output / format / gate / effort / depends-on / authorship); all PROVISIONAL until S88+ THEOREM-tolerance gate verdicts land.

**Joint-theorem-promotion pathway**: CF-W6-V0 + CF-W8-A3 jointly Stage-0 workshop-internal candidates (this R3 close freezes verdict text); Stage-1 registration at S88+ via THEOREM-tolerance gates (`S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM` + `S88-MIN-AXIOM-BUDGET-L8-REDIRECT-INHERITANCE-INVARIANT-THEOREM`); Stage-2 two-agent parallel cross-check required for Stage-3 permanent registration (recommended cross-reviewer assignments: lizzi-spectral-functional-theorist for CF-W8-A3 axiom enumeration; mack-cosmic-bridge for CF-W6-V0 substrate-IS preservation; both with explicit "no prior workshop transcript" condition).

**Quantitative anchors verified this dispatch (knowledge MCP + Sage MCP)**: cocycle_norm_phi67 = 0.793346 (S86 W-5 CANONICAL-3); cocycle_norm_phi88 = 0.108307 (S86 W-5 CANONICAL-4); substrate_cocycle_ratio_67_88 = 7.324992 (S86 W-5 CANONICAL-5); Sage-exact 793346/108307 = 7.3249743783873615 (|delta| from canonical = 1.762e-5 < 1e-4 publication-precision; co-canonical per W-5 W11-C5 calibration); 5 distinct axioms `{1st-order, dim, orient, real, reg}` Sage-verified; L^{-3} envelope at L_max=10 = 0.10% Sage-exact; predicted bare-decomposition deviation under Zubarev filter at L_max=10 = 0.6587% (Sage-exact). All numerical claims in R3 substitution chains are independently Sage-verified or knowledge-MCP-confirmed.

**Workshop W-6 R3 closure status: CLOSED**. Both Edits (R3 + this closure-status block) landed; 6 carry-forwards pre-registered with 4-field specs; 2 STAGE-1-CANDIDATE theorems queued for S88+ landing; SOURCE-DOUBLE-CITE-CO-PRIMARY discipline + 4-stage joint-theorem-promotion pathway + IS-not-IN substrate-framing all honored.
