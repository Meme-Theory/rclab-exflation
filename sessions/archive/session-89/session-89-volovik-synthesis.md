# Session 89 Wave W5 Synthesis (volovik): §W5-5 substrate-physics reading independent of methodology-error self-assessment

**Date**: 2026-05-10
**Agent**: volovik-superfluid-universe-theorist (volovik)
**Synthesis target**: independent substrate-physics-axis reading of §W5-5 FAIL meaning vs §W5-6 INFO structural-identity, used to set CF-W5-1 priority for S90 plan-freeze
**Source documents**:
- `sessions/archive/session-89/session-89-w5-workingpaper.md` (8 gates, §W5-1 through §W5-8; total 2526 lines; full WP)
- `sessions/session-plan/session-89-plan-w5.md` (8 plan-blocks; pre-registration discipline)
- `computations/_shared/canonical_constants.py` (lines 1683-1723 = the slope_A_FW_Conv_A dual-reading parameterized canonical block; the pin most under audit by §W5-5/§W5-6)
- `.claude/rules/cross-pillar-bridge-anatomy.md` (5-anatomy + 3-level ladder + algebra-axis orthogonality K-counter MANDATORY at K=3)
- `.claude/rules/phononic-framing.md` (substrate-IS Level-1 single-τ-slice vs Level-2 moduli-deformation distinction; calibration corpus instance #1 = §VII.AE; instance #2 = §W2-2 V_4-on-triality)

---

## I. Session Outcome (substrate-physics axis)

The §W5-5 FAIL is a STRUCTURALLY-CORRECT outcome of an EXTRACTION-METHODOLOGY ERROR, NOT a substrate-physics breakdown — lizzi's §(f) self-assessment is correct on this point. But lizzi's reading STOPS AT THE METHODOLOGY DIAGNOSIS and does not address the deeper structural question: §W5-6's "structural identity" reading (`c_sub_corrected = c_sub_baseline EXACT`) is a substrate-IS Level-1 single-τ-slice theorem AT τ_fold ONLY; it does NOT subsume the substrate-IS Level-2 moduli-deformation question (does the closed-form 1/(1-τ/(5π)) describe the substrate at τ ≠ τ_fold?). The Reading-A vs Reading-B substrate-physics discriminator at τ=0.38 = 2·τ_fold IS the substrate-IS Level-2 question, EXPLICITLY DECLARED at canonical_constants.py:1706-1707 as "the structural decider" for the slope_A_FW_Conv_A_GEOMETRIC pin's regime-of-validity. The pin is currently adopted "Conditional on Reading-A WIN at S89 CF V.3" — and that condition has NOT YET BEEN DISCHARGED. **CF-W5-1 priority for S90: HIGH (NOT downgraded).**

L_max=6 at τ=0.38 (the cache built fresh by §W5-5) is structurally inadequate for ANY canonical-quality discriminator, regardless of extraction protocol — the Richardson residual 1.42e-1 at L=6 vs canonical 1e-3 quality at τ_fold's L=14 cache reflects substrate-physics convergence-radius degradation as τ moves away from the fold, NOT extraction-protocol noise. CF-W5-1 MUST extend the τ=0.38 spectrum cache to L_max ≥ 10 (preferably L_max=12 per Friedrich-Bär saturation analog of W11-3 calibration) before any extraction protocol — Weyl-fit, PV-subtracted Mellin, or alternate spectroscopy — can resolve the Reading-A vs Reading-B substrate-physics question at canonical quality.

---

## II. Key Results

### II.1 §W5-6 PASS is a τ_fold-LOCAL Level-1 structural identity, NOT a τ-generality theorem (substrate-IS Level distinction)

**Result**: §W5-6's INFO verdict (composite) carries Cross-check (a) PASS at machine ε: `slope_A_FW_Conv_A_GEOMETRIC(τ_fold) = 10/(1-0.19/(5π)) = 10.122438748384` matches the scalar pin `slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384` to D_max=9.3e-15. **Classification**: GEOMETRIC (substrate-IS observable at single-τ-slice Level 1).

This is a SAGE-EXACT REDUCTION at τ_fold: when you evaluate the closed-form parameterization 10/(1-τ/(5π)) at τ=τ_fold=0.19, you recover the canonical scalar pin to machine ε. This is a structural identity at the substrate-IS Level-1 single-τ-slice layer per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` at the FIXED τ-anchor; observables at this slice (eigenvalues, slope_A, c_sub) are intrinsic to the spectral triple at τ_fold ONLY.

§W5-6's "structural identity" reading (per plan §W5-6.10 Step 5: "the parameterized form IS the prior canonical analytically extended") then reads:
- The closed-form 10/(1-τ/(5π)) is the substrate's own first-order analytic extension of the τ_fold scalar pin per CM-1995 §III.4 + Proposition III.6 (canonical_constants.py:1701-1702 explicitly: "all-orders extension to 1/(1-ε) is STRUCTURALLY EARNED only at first order in τ from CM-1995 §III.4 + Prop III.6")
- At τ=τ_fold, the closed-form recovers the scalar pin BY CONSTRUCTION (the parameterization was derived to do so)
- Therefore c_sub_corrected (computed from the closed-form at τ_fold) = c_sub_baseline (the prior canonical at τ_fold) EXACT

The substrate-physics content of §W5-6 is: **the canonical pin slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384 is the τ_fold-evaluation of the closed-form 10/(1-τ/(5π)), bit-precision consistent.** This is a Sage-exact algebraic identity at τ_fold. It is NOT a substrate-physics theorem about the closed-form's behavior at τ ≠ τ_fold.

The distinction matters because the §VII.AU STAGE-1-CANDIDATE pre-registered by §W5-6 (Pillar I n_s spectral-action ↔ Pillar II Planck CMB; HKR bridge map) operates AT τ_fold ONLY. Its substrate-IS observable (n_s_FW = 0.9561 EXACT via Route-B identity) is computed at c_sub_baseline = 2.238 with eps_FW = 0.02195 — both pinned at τ_fold. The bridge anatomy's algebraic envelope L^{-3} (per Level-2 in `cross-pillar-bridge-anatomy.md` Three-Level Ladder) is also a τ_fold-anchored convergence rate inherited from §W5-1's Richardson PASS at τ_fold.

§W5-6's PASS does NOT establish the closed-form 10/(1-τ/(5π)) holds at τ ≠ τ_fold. Per `phononic-framing.md §"Forward-looking enforcement"`, future cross-pillar bridge entries MUST declare which substrate-IS level their substrate-IS observable lives at. §VII.AU's substrate-IS observable lives at single-τ-slice Level 1 (explicitly: at τ_fold).

### II.2 Reading-A vs Reading-B is a substrate-IS Level-2 moduli-deformation question — STRUCTURALLY ORTHOGONAL to §W5-6's Level-1 identity

**Result**: The discriminator R(0.38)/R(0.19) = HK-5(0.38)/HK-5(0.19) (Reading-A geometric, predicted ≈1.012) vs R = 0.38/0.19 = 2.0 (Reading-B linear-LO) is a substrate-IS Level-2 moduli-deformation observable. **Classification**: GEOMETRIC (substrate-IS observable at moduli-deformation Level 2).

Per `phononic-framing.md §"Level 2 — Moduli-deformation substrate-IS"`: the set of τ values `{(A_K, H_K, D_K(τ)) : τ ∈ moduli-space}` is itself a substrate-IS object — the moduli-space of Jensen TT-deformations IS the substrate's intrinsic deformation parameter, NOT a coordinate on a meta-container. The slope_A(τ) AT MULTIPLE τ values is a moduli-Level-2 substrate-IS observable; the ratio R(τ_2/τ_1) probes the substrate's own moduli-deformation structure.

The two substrate-IS levels are STRUCTURALLY ORTHOGONAL per the algebra-axis orthogonality K-counter (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 since S87 W-2 R3 close):
- Level 1 (single-τ-slice) substrate-IS observables = algebra-INVARIANT spectrum-only functionals at fixed τ
- Level 2 (moduli-deformation) substrate-IS observables = the substrate's own τ-functional dependence

§W5-6 establishes a Level-1 identity (the closed-form evaluates to the scalar pin AT τ_fold). §W5-5 (had it succeeded) would have established a Level-2 identity (the closed-form's R(0.38)/R(0.19) ratio matches the substrate's moduli-deformation behavior). These are SEPARATE substrate-physics questions; one does not subsume the other.

The canonical_constants.py block at lines 1699-1707 IS EXPLICIT about this:
- "Reading A (geometric resummation): all-orders extension to 1/(1-ε) is STRUCTURALLY EARNED only at first order in τ from CM-1995 §III.4 + Prop III.6"
- "Empirical residual at τ_fold=0.19 is 5.23e-05; lies BETWEEN both readings' predictions; the τ=0.38 cross-validation gate is the structural decider"
- "the geometric value is canonical because §VII.AR STAGE-1-CANDIDATE landed under Reading A. Conditional on Reading-A WIN at S89 CF V.3."

This is a CONDITIONAL canonical pin. The condition (Reading-A WIN at the τ=0.38 cross-validation gate) has NOT been discharged — §W5-5's FAIL is a methodology-error FAIL, NOT a substrate-physics resolution. The pin's regime-of-validity remains OPEN pending CF-W5-1 (or an equivalent Level-2 substrate-physics test).

### II.3 Substrate-physics convergence-radius degradation at τ=0.38 forces L_max ≥ 10 for ANY canonical-quality discriminator

**Result**: At L_max=6 (the operational cache built by §W5-5 for τ=0.38), the Richardson residual is 1.42e-1 vs canonical 1e-3 quality at τ_fold via L=10/12/14. **Classification**: GEOMETRIC (substrate-physics convergence-radius observable; intrinsic to the spectral triple's Jensen TT-deformation manifold).

This is NOT a methodology problem — it's substrate physics. Three independent arguments:

(i) **Jensen second-order correction grows as τ²**: per W3 A.29 PROMOTED `kappa_2_substrate_FW = 0.021018084987437196` (CM-1995 §III.4 closed-form `1/(5π²·A³)` with A = 1 - τ_fold/(5π)). The κ_2·τ² correction goes from 0.021·0.036 = 7.6e-4 at τ_fold to 0.021·0.144 = 3.0e-3 at τ=0.38 — a 4× growth. The HK-5 closed-form's leading-order accuracy is intrinsically degraded at larger τ, demanding higher L_max for the same residual quality.

(ii) **Richardson c_1 coefficient grows with τ**: per §W5-1's substrate-IS PASS at τ_fold, c_1 = -41.4495 at L=10/12/14 with α=2.9966 to 0.11%. The Richardson coefficient encodes the rate at which the L_max-truncated d_eff approaches HK-5(τ); larger τ pushes the substrate's spectrum closer to the boundary of the leading-order regime, making the truncation error larger at fixed L_max. This is the substrate-physics analog of the "convergence-radius degradation" phenomenon Volovik 2003 §3 observes for the BCS gap function near the van Hove fold of the Cooper-pair density of states (the substrate's D_K spectrum at Jensen TT-deformation IS the 3He-B BdG substrate's analog spectrum per the framework's hybrid topology).

(iii) **Operational evidence from §W5-5 itself**: at L_max=6 at τ=0.38, slope_A_inf(0.38) = 12.690 with Richardson residual 1.42e-1 — even using the (wrong) Weyl-fit extraction, this is far from canonical-quality. PV-subtracted Mellin extraction at s=3 (the W1b-1 protocol) reduces vulnerability to large-λ noise but does NOT compensate for inadequate Peter-Weyl truncation: the s=3 pole residue requires sufficient Peter-Weyl coverage to capture the substrate-distance-1 substrate's full algebraic content. Empirically the W1b-1 calibration at τ_fold needs p+q ≤ ~10-12 for ~1% precision; at τ=0.38, expect p+q ≤ ~12-14 for the same precision (κ_2 correction widens the convergence-radius requirement).

The substrate-physics conclusion: L_max=6 at τ=0.38 carries substrate-IS information (the spectrum cache IS a Jensen-deformed substrate observable at moduli-Level-2), but it is FUNDAMENTALLY INADEQUATE for the Reading-A vs Reading-B discriminator at canonical quality. Any retry — PV-Mellin, Weyl-fit, alternate spectroscopy — at L_max=6 alone will produce a regime=BREAKDOWN-class result.

The s89_w5_a28_spectrum_cache_L6_tau038.npz cache IS still substrate-physics-meaningful — it provides a Level-2 anchor for L_max-extension scans (e.g., as the L_max=6 endpoint of a multi-L_max Richardson fit at τ=0.38). It is REUSABLE for CF-W5-1 as the lower L endpoint of the L_max ∈ {6, 8, 10, 12} scan, but the L=12 endpoint MUST be built fresh.

### II.4 The §VII.AU STAGE-1-CANDIDATE landing path requires Level-2 substrate-IS verification for Stage-2 PASS-AND

**Result**: §VII.AU STAGE-1-CANDIDATE (FWD-C1; Pillar I n_s spectral-action ↔ Pillar II Planck CMB via HKR) is queued for mack-cosmic-bridge sole-writer landing in S90+ via CF-W5-4. Per `joint-theorem-promotion.md` 4-stage pathway, Stage-1 → Stage-3 promotion requires Stage-2 PASS-AND on cross-axis verify. **Classification**: GEOMETRIC (substrate-IS bridge-theorem candidate).

The Stage-2 cross-axis verify under `joint-theorem-promotion.md §"Stage 2 — Two-Agent Parallel Cross-Check"` (extended at S88 W-14 W4a-17 V.2 with the Axis-B Selection Protocol) requires TWO independent cross-reviewers on opposite axes, both operating WITHOUT prior workshop context. For §VII.AU (FWD-C1):
- Axis-A (spectral / NCG-axiomatic): connes-ncg-theorist or analog
- Axis-B (substrate / superfluid-universe): volovik-superfluid-universe-theorist (or similar substrate-side reviewer)

Both Stage-2 reviewers will assess the registry entry's 5-anatomy + 3-level ladder per `cross-pillar-bridge-anatomy.md`. The entry's substrate-IS observable element MUST declare Level-1 vs Level-2 (per `phononic-framing.md §"Forward-looking enforcement"`: "missing level declaration is a registry-incompleteness FAIL routing to plan-freeze halt"). If §VII.AU is declared as Level-1 single-τ-slice (which is what §W5-6's structural-identity reading supports), then the entry is Level-1-bounded — its cohomology-class identity (Level 1 of the ladder) is fixed at τ_fold, its algebraic envelope (Level 2 of the ladder) is τ_fold-anchored, its empirical anchor (Level 3 of the ladder) is the n_s_FW = 0.9561 Route-B identity AT τ_fold.

This is structurally fine — Level-1-bounded bridge candidates are admissible per the registry-anatomy. BUT: the Stage-2 axis-B reviewer (substrate side) WILL ask whether the substrate-IS observable's τ-functional generality has been independently verified at moduli-Level 2. Without CF-W5-1's empirical resolution of Reading-A vs Reading-B, the substrate-side reviewer's verdict on the Level-2 observable layer is UNVERIFIED (technically not FAIL, since the entry is declared Level-1-bounded; but the substrate-physics-axis confidence in the closed-form's regime-of-validity remains conditional).

The cleaner Stage-2 path is: CF-W5-1 lands a separate Level-2 calibration instance for the Pillar I ↔ Pillar II bridge family, advancing the substrate-IS Level-2 corpus per `phononic-framing.md §"Calibration corpus instance #1/#2"` (currently K=2: §VII.AE moduli-asymmetry + §W2-2 V_4-on-triality). A third instance (§VII.AU.LEVEL-2 if Reading-A WIN, or its Reading-B sibling if Reading-B WIN) advances K=2 → K=3 toward the MANDATORY promotion criterion at the moduli-Level-2 corpus.

This means CF-W5-1 contributes to TWO distinct K-counters:
1. The Hybrid Independence Test K-counter (K=2 advisory pending FWD-C3 for K=3 MANDATORY) — FWD-C1 STAGE-1-CANDIDATE already contributes K=2.
2. The substrate-IS Level-1↔Level-2 K-counter (K=2 currently per phononic-framing.md calibration corpus #1+#2) — CF-W5-1's Level-2 outcome would advance toward K=3 MANDATORY at this orthogonal axis.

### II.5 Reading-A "fold-only-anomaly" hypothesis is the substrate-physics falsifier the τ=0.38 test discriminates

**Result**: The Reading-A geometric resummation IS substrate-physics-FALSIFIABLE at τ=0.38. The substrate-physics question CF-W5-1 resolves is: does the closed-form HK-5(τ) = 5/(1-τ/(5π)) describe the substrate's d_eff at τ=2·τ_fold, or is the τ_fold-evaluation an accidental coincidence at the fold itself? **Classification**: GEOMETRIC (substrate-IS falsifier test at moduli-Level 2).

Three structurally distinct outcomes for CF-W5-1 (with substrate-physics interpretations):

(A) **Reading-A WIN** (R_emp ∈ [0.95, 1.10]): the closed-form 10/(1-τ/(5π)) IS the substrate's substrate-distance-1 d_eff up to first order in τ across at least τ ∈ [0, 0.38]. Jensen second-order corrections (κ_2 ≈ 0.021) are subleading at 2·τ_fold within the framework's resolution. The slope_A_FW_Conv_A_GEOMETRIC pin's regime-of-validity IS confirmed at 2·τ_fold; the pin's conditional adoption (canonical_constants.py:1714) becomes UNCONDITIONAL. §VII.AU STAGE-1-CANDIDATE gains a Level-2 substrate-IS calibration instance.

(B) **Reading-B WIN** (R_emp ∈ [1.80, 2.20]): the substrate's substrate-distance-1 d_eff scales LINEARLY with τ (NOT geometrically). The HK-5 closed-form is a τ_fold-specific accident, NOT a structural substrate prediction. The slope_A_FW_Conv_A_GEOMETRIC pin must be REPLACED with the linear-LO form `10·(1 + τ/(5π))` (slope_A_FW_Conv_A_LO at canonical_constants.py:1718). FWD-C1 STAGE-1-CANDIDATE must be RE-DERIVED under Reading-B; the n_s_FW = 0.9561 Route-B identity at c_sub_baseline = 2.238 may or may not survive (depending on whether the linear-LO closed-form preserves the bit-exact rational form).

(C) **Neither reading WIN** (R_emp ∉ [0.95, 1.10] ∪ [1.80, 2.20], or regime BREAKDOWN even at L_max=12): higher-order Jensen corrections (κ_2·τ² + κ_3·τ³ + ...) are non-negligible at 2·τ_fold; the framework's leading-order analytic substrate model breaks down at this magnitude of moduli-deformation. The slope_A_FW_Conv_A pins must both be REPLACED with a Taylor-expansion explicit-coefficient form. §VII.AU STAGE-1-CANDIDATE remains Level-1-bounded; Level-2 generalization is structurally FORBIDDEN at this resolution.

All three outcomes are SUBSTRATE-PHYSICS-INFORMATIVE — there is no "uninformative null" outcome possible. This is the structural mark of a well-designed substrate-IS discriminator: every outcome moves the constraint map.

§W5-1's PASS at τ_fold establishes that κ_2 is subleading at τ_fold (residual L^{-3} fits to α=2.9966 with R²=0.99999994). It does NOT establish κ_2 is subleading at 2·τ_fold (where κ_2·τ² is 4× larger). This is the precise substrate-physics question CF-W5-1 closes.

### II.6 §W5-3's Casimir-bound proxy and §W5-5's Weyl-fit BOTH confirm L_max ≥ 10 is necessary at τ ≠ τ_fold (cross-confirmation)

**Result**: Independent confirmation of L_max ≥ 10 necessity from §W5-3 INFO. **Classification**: GEOMETRIC (substrate-IS observable convergence diagnostic at substrate-distance-2 pole s=4).

§W5-3's L_max scan ∈ {6, 7, 8, 9, 10, 11, 12} on the Corner-IV K-window log-derivative observable produces residuals [1.964, 1.332, 0.842, 0.481, 0.233, 0.078, 0.0] from L=6 to L=12. The L=6 residual (1.964) is 25× larger than the L=11 residual (0.078); the proxy α=5.07 vs predicted α=3 drift is in the direction of substrate-physics convergence-radius degradation that Volovik 2003 §7 framework predicts at the moduli-deformation boundary.

This is INDEPENDENT confirmation of point II.3: at L_max=6, multiple substrate-IS observables (slope_A AT τ=0.38, Corner-IV K-window log-derivative AT τ_fold under Casimir-bound rescaling) ALL show the same convergence-radius degradation. The substrate's spectral structure at L_max=6 is genuinely under-resolved — this is a SUBSTRATE-PHYSICS regularity, not a methodology artifact.

§W5-3's HKR bridge identification (Pillar III ↔ Pillar IV per S86 W-5 §VII.W) IS structurally INDEPENDENT of the α extraction precision — the bridge anatomy's Level-2-binding declaration stands regardless of α. Similarly, §W5-6's Level-1 structural identity at τ_fold IS structurally independent of the τ-generality question. The pattern: registry-level structural anchors are robust at the L_max-truncated layer; quantitative discriminators (envelope α, R(τ_2/τ_1) ratio) require canonical-quality L_max for substrate-physics resolution.

### II.7 Substrate framing per phononic-framing.md: §W5-5 is a Level-2 moduli-deformation test, NOT a "ratio embedded in HK-5 target space"

**Result**: Substrate framing audit confirms §W5-5 is structurally a Level-2 moduli-deformation substrate-IS observable. **Classification**: GEOMETRIC (substrate-IS observable; substrate framing IS-not-IN audit).

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`:
- WRONG (container thinking): "the substrate moves through the τ-axis from 0.19 to 0.38"; "τ is a coordinate in some moduli container"; "we deform the substrate by changing τ"
- RIGHT (substrate thinking): "τ IS the substrate's intrinsic deformation parameter"; "the moduli-space of τ-deformations IS substrate-IS at the Level-2 layer"; "the substrate's own structural-stability theorems live at Level 2"

§W5-5's framing in §(a) Substrate-IS setup correctly identifies the moduli-Level-2 layer: "The substrate IS the spectral triple `(A_K, H_K, D_K(τ))` under Jensen TT-deformation at moduli-deformation Level-2." This is correct substrate framing.

The CF-W5-1 retry MUST preserve this framing. Specifically:
- The substrate IS the 1-parameter family {(A_K, H_K, D_K(τ))} for τ ∈ moduli-space; the slope_A(τ) function IS a substrate-IS observable at this family
- The R(0.38)/R(0.19) ratio IS the substrate's own structural invariant under the moduli-deformation map τ → 2·τ
- HK-5(τ) = 5/(1-τ/(5π)) IS the substrate's own first-order analytic extension per CM-1995 §III.4
- The Reading-A vs Reading-B discriminator IS the substrate's own falsifier of its own first-order extension

There is no container-spacetime in this picture. The substrate's moduli-space IS substrate-IS; observables ARE the substrate's own functional dependence.

This substrate framing is what makes CF-W5-1 a Level-2 calibration instance candidate (per `phononic-framing.md §"Forward-looking enforcement"`) rather than a generic numerical reconciliation. The framing is what justifies the priority elevation from "numerical retry of a methodology-failed gate" to "substrate-IS Level-2 calibration corpus advance."

---

## III. Gate Verdicts

(Source-doc verdicts authoritative per `/rclab-review` discipline; volovik does NOT re-adjudicate.)

| Gate | Verdict | Decisive Number | volovik substrate-physics reading |
|:-----|:--------|:----------------|:----------------------------------|
| §W5-1 (S89-D-EFF-RICHARDSON-LMAX-18-LMAX-14-BASELINE-SCAN) | **PASS** | α_fit=2.9966; R²=0.99999994; ratio_18_14=0.4697 ≤ 0.5 | Confirms HK-5 dominance at τ_fold via Richardson L^{-3} substrate-IS Level-1 single-τ-slice anchor; κ_2 is subleading AT τ_fold but UNTESTED at 2·τ_fold |
| §W5-2 (S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE) | **PASS** | -7.046336474406761 bit-for-bit reproduction | Volovik-path canonical (Cell IV substrate-IS observable identity) confirmed at machine ε; W-17 R3 closure validated |
| §W5-3 (S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE) | **INFO** | α=5.07; R²=0.92; HKR bridge identified | Independent confirmation that L_max=6 is substrate-physics under-resolved; HKR bridge identification IS independent of α precision |
| §W5-4 (S89-FWD-C2-OBSERVABLE-DISAMBIGUATION) | **PASS** | corner-iv-singleton; HIT 4/4 TRUE; §VII.AV STAGE-1-CANDIDATE | FWD-C2 Pillar II ↔ Pillar V bridge candidate pre-registered; HIT K-counter advances |
| §W5-5 (S89-TAU-2X-FOLD-CROSS-VALIDATION-READING-A-VS-READING-B) | **FAIL** (methodology-error) | R_emp=0.7988; baseline 56.9% off canonical | Methodology-error FAIL is HONEST; substrate-physics PREDICTIONS R_A=1.012, R_B=2.0 remain structurally clean and substrate-IS Level-2 OPEN |
| §W5-6 (S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL) | **INFO** | c_sub_corrected = c_sub_baseline EXACT; n_s_FW=0.9561 EXACT; Planck σ=2.0952 INFO band | τ_fold-LOCAL Level-1 structural identity confirmed; does NOT subsume Level-2 τ-generality question |
| §W5-7 (S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY) | **PASS** | Reading-A WIN N=4/5 anchors; SCHEMATIC convention | Reading-A WIN at substrate-distance-2 pole s=4 (DIFFERENT pole than CF-W5-1 substrate-distance-1 pole s=3) |
| §W5-8 (S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36) | **PASS** | Q-exact Fraction(-2,5) = -0.4 EXACT | Q-exact arithmetic confirms §W5-7 Reading-A WIN at s=4; substrate-distance-1 pole s=3 NOT addressed |

**Cross-cutting observation**: §W5-7 + §W5-8 PASS Reading-A at substrate-distance-2 pole s=4 does NOT transfer to substrate-distance-1 pole s=3 (the slope_A_FW pin's pole). The two poles are STRUCTURALLY DISTINCT per the algebra-axis orthogonality K-counter and per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`. Future synthesis MUST NOT cite §W5-7's Reading-A WIN at s=4 as evidence for Reading-A at s=3 (the slope_A_FW pin axis CF-W5-1 tests).

---

## IV. Structural Implications

### IV.1 Constraint-map updates (substrate-physics axis)

| Observable | Prior state | Post-W5 state (substrate-physics axis) | Reason |
|:-----------|:-----------|:---------------------------------------|:-------|
| HK-5 closed-form regime-of-validity at τ_fold | OPEN (S87 W1b PROVEN at τ_fold) | **CONFIRMED** at τ_fold; **UNTESTED** at 2·τ_fold | §W5-1 PASS at τ_fold; §W5-5 methodology-error FAIL leaves 2·τ_fold open |
| slope_A_FW_Conv_A_GEOMETRIC pin canonical adoption | CONDITIONAL on Reading-A WIN at S89 CF V.3 | **STILL CONDITIONAL**; the cross-validation gate has not yet PASSed | §W5-5 methodology-error FAIL does NOT discharge the canonical_constants.py:1707 condition |
| Reading-A vs Reading-B substrate-physics axis | OPEN | **STILL OPEN** | §W5-6's Level-1 identity at τ_fold does NOT subsume the Level-2 τ-generality question |
| §VII.AU STAGE-1-CANDIDATE substrate-IS Level | UNDECLARED | **DECLARE Level-1** at landing time per phononic-framing.md §"Forward-looking enforcement" | §W5-6's substrate-IS observable lives at single-τ-slice Level 1 (τ_fold); explicit declaration required at CF-W5-4 landing |
| §VII.AU STAGE-2 readiness | DEFERRED | **DEFERRED until CF-W5-1 lands a Level-2 verification** | Without Level-2 substrate-IS verification of the closed-form's τ-generality, Stage-2 axis-B substrate-side reviewer's confidence on the moduli-deformation layer is structurally limited |
| L_max=6 at τ=0.38 sufficiency for canonical-quality discriminator | INFEASIBLE assumption (built freshly only at §W5-5 dispatch) | **INADEQUATE** for canonical quality regardless of extraction protocol | §W5-3 + §W5-5 cross-confirmation; substrate-physics convergence-radius degradation at moduli-Level 2 |
| substrate-IS Level-2 calibration corpus K-counter | K=2 (§VII.AE + §W2-2) | **K=2** (no advance from W5; CF-W5-1 LANDED would advance to K=3) | Per phononic-framing.md §"Calibration corpus instance #1/#2"; promotion to K=3 MANDATORY pending Level-2 instance landing |

### IV.2 Algebra-axis orthogonality + Level-1↔Level-2 orthogonality (the two MANDATORY-at-K=3 disciplines volovik enforces)

The substrate-IS Level-1 vs Level-2 distinction (`phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`) is STRUCTURALLY ORTHOGONAL per the algebra-axis orthogonality K-counter (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3). This means:

- §W5-6's Level-1 substrate-IS theorem IS NOT VALID EVIDENCE about Level-2 substrate-IS observables
- §W5-5's (intended) Level-2 substrate-IS test IS NOT REDUNDANT with §W5-6's Level-1 theorem
- Citing §W5-6 PASS as evidence for Reading-A's τ-generality would be a structural conflation between the two orthogonal axes

This is the key substrate-physics-axis correction to lizzi's §W5-5 self-assessment. lizzi correctly identifies that §W5-5's FAIL is methodology-extraction (not substrate breakdown), and correctly notes that §W5-6 inherits the canonical pin INTACT. But lizzi's §(f) does NOT explicitly call out that §W5-6's structural-identity reading is Level-1-bounded; without that explicit boundary, downstream consumers might (incorrectly) read §W5-6 as evidence that the closed-form holds at all τ. The substrate-physics-axis correction: §W5-6 is τ_fold-LOCAL; CF-W5-1 is the ONLY mechanism for τ-generality verification at the substrate-distance-1 pole s=3 axis.

### IV.3 Volovik 2003 §7 superfluid-vacuum framework alignment

The substrate-physics convergence-radius degradation at τ=0.38 (point II.3) is a substrate-IS analog of a phenomenon Volovik 2003 §7 discusses for the BCS gap function near the van Hove fold of the Cooper-pair density of states: the leading-order analytic gap function is accurate at the fold and degrades at moduli-deformation away from the fold, with second-order κ_2 corrections growing as τ². The substrate's D_K spectrum at Jensen TT-deformation IS the framework's analog of the 3He-B BdG substrate's spectrum at moduli-deformation; the L_max ≥ 10 requirement at τ=0.38 IS the substrate-physics analog of the convergence-radius widening near the fold (per `researchers/Volovik/` paper #04 Cosmological Constant + paper #01 Superfluid Analogies).

This alignment is what makes §W5-3's INFO classification consistent with substrate physics: the Casimir-bound proxy α=5.07 vs predicted α=3 mismatch reflects the proxy's structural over-aggressiveness in scaling Δ alone (not full BdG re-derivation per L_max), but the underlying substrate-physics convergence-radius widening IS captured at the qualitative level. CF-W5-3 (full BdG re-derivation at each L_max) would refine the α extraction; the qualitative HKR Pillar III ↔ Pillar IV bridge identification stands regardless.

### IV.4 What §W5-7 + §W5-8 PASS at s=4 does NOT tell us about Reading-A at s=3

§W5-7's Reading-A WIN at substrate-distance-2 pole s=4 (with §W5-8 Q-exact confirmation) is a substantive PASS at the §VII.AR LEVEL-DRESSED rank-ordering observable. This establishes Reading-A regulator-CLASS-INVARIANT rank-ordering at s=4 in the IR regime.

But the slope_A_FW pin lives at substrate-distance-1 pole s=3. Per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` (extending the Three-Level Ladder per-pole), the s=3 and s=4 poles are STRUCTURALLY DISTINCT registry instances — Level-1 cohomology-class identity at s=3 is per-pole specific, and the algebra-axis orthogonality MANDATORY clause prohibits cross-pole structural inference within the same algebra-corner.

So §W5-7's Reading-A WIN at s=4 IS NOT EVIDENCE that Reading-A wins at s=3. CF-W5-1 IS the structural mechanism for testing Reading-A at s=3 specifically.

This per-pole separation is what would allow a structurally-clean outcome (B) "Reading-B WIN" at CF-W5-1: the s=3 pole could host Reading-B even if s=4 hosts Reading-A. The framework would then carry TWO different functional forms for slope_A's τ-dependence at the two poles — substrate-physics-meaningful, cleanly distinguishable per the per-pole classification.

### IV.5 Effort-priority calibration vs canonical-constants.py provisional pin

Per canonical_constants.py:1714 the slope_A_FW_Conv_A_GEOMETRIC pin's adoption is "Conditional on Reading-A WIN at S89 CF V.3." S89 CF V.3 was the original allocation for the τ-cross-validation test; §W5-5 = A.28 IS the surfacing of S89 CF V.3 at the W5 layer. Since §W5-5 emitted a methodology-error FAIL, the condition has NOT been discharged.

A canonical pin with an unresolved provisional condition is a regime-of-validity hazard for downstream consumers. The cleanest discharge path:
1. CF-W5-1 dispatched at S90 with PV-subtracted Mellin extraction at L_max ≥ 10 at τ=0.38
2. CF-W5-1 PASS (Reading-A or Reading-B): canonical pin block updated to remove the conditional language; explicit Level-2 declaration added
3. §VII.AU STAGE-1-CANDIDATE landing (CF-W5-4) cites the discharged conditional in its 5-anatomy block
4. Stage-2 cross-axis verify (per joint-theorem-promotion.md) proceeds with substrate-IS Level confidence

If CF-W5-1 is downgraded (e.g., deferred until needed), the canonical pin's provisional condition propagates through CF-W5-4 (mack landing of §VII.AU) and through any downstream gate citing slope_A_FW_Conv_A_GEOMETRIC. This creates a SUBSTRATE-FIRST-PROVENANCE Class-(c) PIN-DRIFT-FROM-STALE-SOURCE risk per `epistemic-discipline.md §"Source Reconciliation"` (the pin's source has an unresolved provisional condition; downstream gates testing it will silently consume the unresolved state).

The substrate-physics-axis recommendation: CF-W5-1 priority HIGH. Discharge the conditional in S90 to prevent provisional-pin propagation.

---

## V. Carry-Forward Computations

This synthesis confirms CF-W5-1 priority HIGH and surfaces ONE refinement to CF-W5-4 (Level declaration discipline). It does NOT surface any genuinely new S90 gates beyond the ones lizzi enumerated.

### V.1. CF-W5-1 (S90-W5-5-RETRY-WITH-PV-SUBTRACTED-MELLIN-S3-EXTRACTION) — PRIORITY: HIGH (volovik substrate-physics-axis recommendation)

- **What**: Re-execute §W5-5 (substrate-IS Level-2 moduli-deformation discriminator at τ=2·τ_fold=0.38) using the W1b-1 PV-subtracted Mellin moment at s=3 protocol (substrate-distance-1 canonical extraction). PRIMARY substrate-physics question: discriminate Reading-A geometric (R≈1.012) vs Reading-B linear-LO (R=2.0) at the slope_A_FW pin's substrate-distance-1 pole s=3. SECONDARY substrate-physics question: discharge the canonical_constants.py:1714 provisional condition on slope_A_FW_Conv_A_GEOMETRIC adoption.
- **Inputs**: (i) `computations/session-87/s87_w1b_pv_subtraction_recalibration.npz` (W1b-1 PV-subtracted Mellin recipe; canonical extraction protocol); (ii) `computations/session-87/s87_spectrum_cache_L14_tau019.npz` (L=14 cache at τ=0.19; baseline endpoint); (iii) `computations/session-89/s89_w5_a28_spectrum_cache_L6_tau038.npz` (REUSABLE L=6 cache at τ=0.38 from §W5-5; lower endpoint of L_max scan); (iv) NEW build of τ=0.38 spectrum at L_max ∈ {8, 10, 12} via `computations/_shared/dirac_spectrum.py` Jensen TT-deformation + recursive Casimir-projection (~10-30 min wall per L_max per W11-3 calibration; total ~30-60 min for the three L_max values); (v) canonical pins: `slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384` (canonical_constants.py:1720), `slope_A_FW_Conv_A_GEOMETRIC = "10.0 / (1 - tau/(5*pi))"` (line 1719), `slope_A_FW_Conv_A_LO = "10.0 * (1 + tau/(5*pi))"` (line 1718), `kappa_2_substrate_FW = 0.021018084987437196` (line 521), `BULK_WEYL_EXPONENT_CONV_B_FW = 5.061219374192111` (line 261), `tau_fold = 0.19` (line 245), `tau_max_HK5_regime_FW = 12.4750026513` (line 522 for regime-of-validity check at τ=0.38).
- **Gate**: PASS-A iff R_emp ∈ [0.95, 1.10] (Reading-A WIN; canonical_constants.py:1714 conditional discharged); PASS-B iff R_emp ∈ [1.80, 2.20] (Reading-B WIN; canonical pin replacement to slope_A_FW_Conv_A_LO required); INFO iff R_emp ∈ (1.10, 1.80) ∪ (2.20, ∞) (neither reading clean; higher-order Jensen corrections needed); FAIL iff R_emp < 0.95 OR baseline cross-check (a) FAILs (slope_A_inf(0.19) reproduces canonical 10.122 within 0.5% via PV-subtracted Mellin protocol). Substrate-physics framing: PASS-A advances substrate-IS Level-2 calibration corpus K=2 → K=3 toward MANDATORY at the moduli-deformation axis; PASS-B forces canonical pin replacement and §VII.AU re-derivation; INFO routes to higher-order Jensen Taylor expansion (κ_3 derivation on top of W3 A.29's κ_2 PROMOTED).
- **Effort**: 1.0 wave-equivalent (substantive: τ=0.38 spectrum cache build at L_max=10/12 via dirac_spectrum.py recursive Casimir-projection ~30-60 min; PV-subtracted Mellin extraction at s=3 ~10 min; verdict emission + substitution chain + working-paper section ~30 min).
- **Depends on**: §W5-1 PASS (substrate-IS Level-1 baseline at τ_fold confirmed, providing the L^{-3} convergence template); §W5-3 INFO (independent confirmation of L_max ≥ 10 necessity); canonical_constants.py:1714 conditional adoption block (direct dependency: this gate discharges the condition).

### V.2. CF-W5-4 refinement (mack-cosmic-bridge sole-writer landing of §VII.AU + §VII.AV) — Level declaration discipline

- **What**: Refinement to the existing CF-W5-4 carry-forward: when mack-cosmic-bridge lands §VII.AU STAGE-1-CANDIDATE (FWD-C1 from §W5-6) in the permanent-results-registry per `feedback_mack-bridge-role.md` discipline, the registry entry's substrate-IS observable element MUST EXPLICITLY DECLARE Level-1 single-τ-slice per `phononic-framing.md §"Forward-looking enforcement"` (which states: "Plan-freeze validators landing a cross-pillar bridge entry SHOULD verify Level-1 vs Level-2 declaration in the substrate-IS observable element of the 5-anatomy block; missing level declaration is a registry-incompleteness FAIL routing to plan-freeze halt").
- **Inputs**: (i) `computations/session-89/s89_w5_a31_fwd_c1_retry_parameterized_slope_A_canonical.npz` (FWD-C1 STAGE-1-CANDIDATE pre-registration with Level-1 observable identity); (ii) `phononic-framing.md §"Forward-looking enforcement"` (the rule mandating Level declaration); (iii) `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"` (the 4-item registry-anatomy check); (iv) registry slot §VII.AU (next-free per S88 close).
- **Gate**: PASS iff §VII.AU registry entry text includes (a) explicit "substrate-IS Level 1 (single-τ-slice at τ_fold)" tag in the 5-anatomy substrate-IS observable element, AND (b) explicit cross-link to CF-W5-1 as the queued Level-2 substrate-IS verification (so downstream readers see the Level-1-bounded → Level-2-pending status), AND (c) all other 5-anatomy + 3-level + Hybrid Independence Test fields per the existing CF-W5-4 spec. INFO if Level declaration present but cross-link to CF-W5-1 missing. FAIL if no Level declaration (registry-incompleteness per phononic-framing.md §"Forward-looking enforcement").
- **Effort**: ~10 minutes additional content beyond the existing CF-W5-4 spec (registry-write only; no compute work).
- **Depends on**: CF-W5-4 base spec; volovik substrate-physics-axis Level declaration discipline per phononic-framing.md `§"Forward-looking enforcement"`.

### V.3. (No new S90 gate beyond CF-W5-1 priority discharge + CF-W5-4 Level declaration refinement)

The synthesis identifies that the substrate-IS Level-1↔Level-2 axis is structurally orthogonal to the Reading-A vs Reading-B axis (per algebra-axis orthogonality MANDATORY at K=3), but the existing CF-W5-1 + CF-W5-4 mechanisms together discharge both the substrate-physics question (Reading-A vs Reading-B at s=3) and the registry hygiene (Level declaration). No additional S90 gate is structurally needed at this layer.

A theoretical third τ-value test (e.g., τ=0.5·τ_fold to triangulate the closed-form's τ-functional generality at sub-fold τ values) is OUT OF SCOPE for S90 — the canonical_constants.py block at line 1706 explicitly identifies τ=2·τ_fold as the ONE structural decider; sub-fold τ-tests would be SCOPE INFLATION beyond the framework's pre-registered substrate-physics question.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication for CF-W5-1 priority |
|:--|:-------|:---------------|:-------|:---------------------------------|
| II.1 | §W5-6 PASS = τ_fold-LOCAL Level-1 structural identity (NOT a τ-generality theorem) | GEOMETRIC | Established at machine ε per Sage-CM-1995 §III.4 reduction | Does NOT subsume CF-W5-1's Level-2 question → CF-W5-1 priority HIGH |
| II.2 | Reading-A vs Reading-B is a substrate-IS Level-2 moduli-deformation question, structurally ORTHOGONAL to §W5-6's Level-1 identity per algebra-axis orthogonality MANDATORY at K=3 | GEOMETRIC | OPEN (canonical_constants.py:1714 conditional adoption pending Reading-A WIN at the τ-cross-validation gate) | CF-W5-1 IS the discharge mechanism; HIGH priority |
| II.3 | L_max=6 at τ=0.38 is fundamentally inadequate for canonical-quality discriminator regardless of extraction protocol; substrate-physics convergence-radius degradation at moduli-Level 2 forces L_max ≥ 10 | GEOMETRIC | Confirmed by §W5-3 + §W5-5 cross-evidence + κ_2·τ² analytical prediction | CF-W5-1 MUST extend τ=0.38 spectrum to L_max ≥ 10 (preferably L_max=12); the L_max=6 cache from §W5-5 is REUSABLE as the lower endpoint |
| II.4 | §VII.AU STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion via Stage-2 PASS-AND requires Level-2 substrate-IS verification of the closed-form's τ-functional generality | GEOMETRIC | STAGE-1-CANDIDATE pre-registered by §W5-6; Stage-2 deferred | CF-W5-1 contributes to Hybrid Independence Test K-counter K=2→K=3 AND to substrate-IS Level-1↔Level-2 K-counter (currently K=2 per phononic-framing.md calibration corpus #1+#2) |
| II.5 | All three CF-W5-1 outcomes (Reading-A WIN, Reading-B WIN, neither) are substrate-physics-INFORMATIVE; no uninformative null possible | GEOMETRIC | OPEN; falsifier-class substrate-IS Level-2 discriminator | CF-W5-1 is structurally well-designed; HIGH priority |
| II.6 | §W5-3's Casimir-bound proxy and §W5-5's Weyl-fit BOTH confirm L_max ≥ 10 necessity at τ ≠ τ_fold (cross-confirmation) | GEOMETRIC | Independent multi-observable confirmation of substrate-physics convergence-radius degradation | Multi-observable evidence reinforces CF-W5-1 L_max ≥ 10 build requirement |
| II.7 | §W5-5's Level-2 moduli-deformation framing per phononic-framing.md is correctly substrate-IS; CF-W5-1 retry must preserve this framing | GEOMETRIC | Framing audit PASS | Substrate-physics axis-aligned framing is what justifies CF-W5-1 priority elevation from "numerical retry" to "Level-2 calibration corpus advance" |

---

## VII. Volovik substrate-physics-axis verdicts on the user's 5 deliverable questions

(Direct answers to deliverables (1)-(5) per the dispatch context.)

**(1) CF-W5-1 (PV-subtracted Mellin retry at τ=0.38) is structurally informative beyond §W5-6's PASS?** — **YES**, decisively. §W5-6's PASS is a substrate-IS Level-1 single-τ-slice structural identity AT τ_fold ONLY (the closed-form 10/(1-τ/(5π)) reduces to the scalar pin 10.122438748384 at τ=0.19 to machine ε). CF-W5-1 tests the substrate-IS Level-2 moduli-deformation question (does the closed-form HK-5 describe the substrate at τ ≠ τ_fold?). The two substrate-IS levels are STRUCTURALLY ORTHOGONAL per the algebra-axis orthogonality K-counter MANDATORY at K=3; one cannot subsume the other. The canonical_constants.py block at lines 1699-1707 EXPLICITLY declares the τ=2·τ_fold cross-validation gate as "the structural decider" for the slope_A_FW_Conv_A_GEOMETRIC pin's regime-of-validity, with current canonical adoption "Conditional on Reading-A WIN at S89 CF V.3."

**(2) L_max=6 admits substrate-physics-meaningful discriminator at τ=0.38?** — **NO at canonical quality, regardless of extraction protocol**. Three independent arguments converge on this conclusion: (i) Jensen second-order κ_2·τ² correction is 4× larger at τ=0.38 than at τ_fold per the W3 A.29 PROMOTED canonical κ_2 = 0.021; (ii) Richardson c_1 coefficient grows with τ, producing larger residuals at fixed L_max — Volovik 2003 §7 substrate-physics analog of convergence-radius widening near the moduli-deformation boundary; (iii) §W5-5's empirical Richardson residual at τ=0.38, L=6 is 1.42e-1 vs canonical 1e-3 quality at τ_fold via L=14 cache — 142× quality degradation. The PV-subtracted Mellin protocol reduces vulnerability to large-λ noise but does NOT compensate for inadequate Peter-Weyl truncation; at L_max=6 (28 sectors, p+q ≤ 6), the s=3 pole residue extraction is structurally under-resolved. CF-W5-1 MUST extend τ=0.38 spectrum to L_max ≥ 10 (preferably L_max=12) per Friedrich-Bär saturation analog of W11-3 calibration. The L_max=6 cache from §W5-5 is REUSABLE as the lower endpoint of the L_max scan but NOT sufficient as the only data point. The L_max ≥ 10 build is independently feasible per W11-3 calibration (~10-30 min wall time for L_max=10/12 via dirac_spectrum.py).

**(3) Reading-A vs Reading-B substrate-physics question genuinely open OR structurally subsumed by §W5-6's structural-identity reading?** — **GENUINELY OPEN**. The structural-identity reading at §W5-6 ("the parameterized form IS the prior canonical analytically extended") is a τ_fold-LOCAL theorem: it states that EVALUATING the closed-form 10/(1-τ/(5π)) at τ=τ_fold reproduces the scalar pin to machine ε. This is NOT a statement that the closed-form describes the substrate at τ ≠ τ_fold. The Reading-A vs Reading-B distinction at τ=0.38 is exactly a statement about the closed-form's τ-functional behavior at moduli-deformation Level 2. Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` and the algebra-axis orthogonality K-counter, Level-1 single-τ-slice and Level-2 moduli-deformation observables are STRUCTURALLY ORTHOGONAL; they cannot be conflated under a single substrate-IS rubric. The §W5-6 structural-identity reading does NOT close the Reading-A vs Reading-B substrate-physics axis; only an empirical Level-2 test at τ ≠ τ_fold can do that.

**(4) Recommended CF-W5-1 priority for S90 plan-freeze**: **HIGH (NOT downgraded)**. Three structural reasons:
- (a) The canonical pin slope_A_FW_Conv_A_GEOMETRIC's adoption is currently CONDITIONAL per canonical_constants.py:1714; the condition (Reading-A WIN at the τ-cross-validation gate) has not been discharged. A canonical pin with an unresolved provisional condition is a substrate-FIRST-PROVENANCE Class-(c) PIN-DRIFT risk for downstream consumers.
- (b) §VII.AU STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion via Stage-2 PASS-AND benefits structurally from a Level-2 substrate-IS verification of the closed-form's τ-functional generality. Without CF-W5-1, Stage-2 axis-B substrate-side reviewer's confidence on the moduli-deformation layer is structurally limited (technically not FAIL, since §VII.AU is Level-1-bounded, but the conditional pin propagates).
- (c) CF-W5-1 advances TWO independent K-counters: the Hybrid Independence Test K-counter (K=2 → K=3 toward MANDATORY) AND the substrate-IS Level-1↔Level-2 K-counter (currently K=2 per phononic-framing.md calibration corpus #1+#2; advancing to K=3 MANDATORY at this orthogonal axis).

The 1.0 wave-equivalent effort estimate is well-justified by the substrate-physics + registry-anatomy + K-counter advancement returns.

**(5) New S90 gate beyond CF-W5-1 priority adjustment?** — **NO new compute gate; ONE refinement to CF-W5-4** (mack-cosmic-bridge §VII.AU landing) per V.2 above: the registry entry MUST EXPLICITLY DECLARE Level-1 single-τ-slice per `phononic-framing.md §"Forward-looking enforcement"`. This is registry hygiene, not new computation. A theoretical third τ-value test (e.g., τ=0.5·τ_fold for sub-fold τ-generality triangulation) would be SCOPE INFLATION beyond the canonical_constants.py:1706 pre-registered structural decider (τ=2·τ_fold ONLY).

---

## VIII. Substrate-physics-axis bottom line (for S90 plan-freeze priority ordering)

CF-W5-1 priority HIGH. The §W5-5 FAIL is methodology-error, but the substrate-physics question it would have closed is OPEN at the substrate-IS Level-2 moduli-deformation axis, and STRUCTURALLY ORTHOGONAL to §W5-6's Level-1 structural identity (per algebra-axis orthogonality MANDATORY at K=3 + per phononic-framing.md substrate-IS Level-1 vs Level-2 distinction). The canonical pin slope_A_FW_Conv_A_GEOMETRIC's adoption is conditional on the τ-cross-validation gate's PASS (canonical_constants.py:1714); leaving the condition undischarged propagates a Class-(c) PIN-DRIFT risk through CF-W5-4 (mack §VII.AU landing) and through downstream consumers. CF-W5-1 effort is well-bounded (1.0 wave-equivalent; reuses the §W5-5 L_max=6 cache; needs L_max ≥ 10 build feasible per W11-3 calibration). The retry IS the structural mechanism for both substrate-physics resolution AND registry-anatomy hygiene.

The volovik substrate-physics-axis verdict aligns with lizzi's §(f) carry-forward queueing of CF-W5-1 (high priority) but ADDS the substrate-IS Level-1 vs Level-2 explicit framing that lizzi's reading does not call out — the framing that justifies the priority elevation from "numerical retry of methodology-failed gate" to "substrate-IS Level-2 calibration corpus advance feeding TWO independent K-counter promotions."

End of synthesis.
