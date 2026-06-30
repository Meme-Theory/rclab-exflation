# Session 89 Synthesis: §W5-7 SCHEMATIC PASS — Connes-NCG Reading of §VII.AR Registry-Confirmation Status Under K=4 MANDATORY Level-Pin Discipline

**Date**: 2026-05-10
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/archive/session-89/session-89-w5-workingpaper.md` (§W5-7 lines 1815-2125; §W5-8 lines 2127-2422; Wave 5 synthesis lines 2424-2530)
- `sessions/session-plan/session-89-plan-w5.md` (§W5-7 plan-block lines 1552-1764; §W5-8 plan-block lines 1765-1959)
- `.claude/rules/substrate-first-canonical-sourcing.md` (§(iv) K=4 MANDATORY SCHEMATIC level-pin discipline)
- `.claude/rules/cross-pillar-bridge-anatomy.md` (§"Algebra-axis orthogonality K-counter" MANDATORY-K=3; §"Per-Bulletin-per-pole Level-1 wall classification" W10-119)
- `sessions/permanent-results-registry.md` §VII.AR (lines 16948-16978; §VII.AQ context lines 17008-17094)
- Cross-check: `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py` docstring (SCHEMATIC declaration verified at lines 22-39)

---

## I. Session Outcome

**§W5-7 (A.36) PASS at SCHEMATIC tier + §W5-8 (A.37) Q-exact PASS jointly satisfy the conditional that gated §VII.AR's STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP status (5-anchor sweep with N≥4/5 decision rule), but confirm only the INTRA-SCHEMATIC sub-claim of the theorem statement.** The full §VII.AR claim — "rank-ordering at s=4 IS REGULATOR-PARAMETER-dependent (NOT regulator-CLASS-dependent) under the PRIMARY-vs-SCHEMATIC LEVEL switch" — requires the cross-tier comparison that CF-W5-2 (S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR) is queued to perform. Connes-side recommendation: **§VII.AR advances STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP → STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION**, with the SCHEMATIC anchor-robustness sub-claim CONFIRMED and the PRIMARY-vs-SCHEMATIC rank-swap claim STILL PENDING CF-W5-2. §W5-7 advances the §(iv) K=4 SCHEMATIC-level-pin calibration corpus to K=5 as a PARTIAL-POSITIVE-CALIBRATION instance (convention-tag suffix and docstring SCHEMATIC declaration both present, but missing the W9c-1-style `tier_pin=TIER-2` companion row).

---

## II. Key Results

### Result 1 — Two structurally distinct claims within §VII.AR; only one tested by §W5-7

**Result**: §VII.AR's theorem statement decomposes into TWO sub-claims with different testability conditions. Classification: **GEOMETRIC** (substrate-IS observable on the spectral-functional family on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`).

Reading the registry text at `sessions/permanent-results-registry.md` line 16954 carefully, the theorem has two logical components:

**Sub-claim A (intra-class anchor robustness)**: For a fixed regulator CLASS (PRIMARY *or* SCHEMATIC), the rank-ordering of the 4-regulator atlas at substrate-distance-2 pole s=4 is preserved under variation of the heat-kernel anchor `t_ref` within the IR-discriminating regime. This is a within-tier statement; varying t_ref does not change which regulator gives the smallest/largest Mellin moment.

**Sub-claim B (cross-tier rank-PARAMETER coupling)**: The rank-ordering SWAPS under the PRIMARY ↔ SCHEMATIC LEVEL switch on the L_max=12 block-diagonal cache at FIXED `cutoff_frac=0.7`, `M_PV²_frac=0.1`, `Vol_SU3_Haar`. The empirical Spearman `|ρ_S(s=4)|_PRIMARY = 0.800 ± δ` is the cross-tier rank-correlation signature.

§W5-7 ran the 5-anchor scan **entirely within the SCHEMATIC class** because the canonical W7a-74 PRIMARY evaluator was not directly available; the operational deviation block in the WP (lines 1840-1851) maps the plan atlas to SCHEMATIC functional forms `{exp(-x), Θ(1−√x), exp(-x)·(1−x+x²/2), 1/(1+exp(10·(x−1)))}` and explicitly tags the convention with `-SCHEMATIC`. The N=4/5 PASS verifies sub-claim A at the SCHEMATIC tier; it does NOT verify sub-claim B (the cross-tier rank swap that defines the LEVEL-DRESSED finding).

The §W5-7 WP conclusion is structurally honest about this: it characterizes the result as "regulator-PARAMETER-DEPENDENT (different parameters give different individual values) but regulator-CLASS-INVARIANT (the structural ordering is preserved under class-internal anchor variation in the IR regime)" — note that "class-internal" qualifier locates the validation strictly within the SCHEMATIC class. The cross-class statement is reserved.

### Result 2 — UV-degenerate anchor 5 is SCHEMATIC-specific (with a unit-treatment subtlety)

**Result**: Anchor 5 (1/M_KK²) Spearman = −0.4 across SCHEMATIC profiles reflects the small-x regime where all four functional forms converge to 1; this is NOT the structural behavior expected under FULL physical regularizations. Classification: **GEOMETRIC**.

The four SCHEMATIC profiles all satisfy `profile(x → 0) → 1` by construction — they are smooth functional forms designed to interpolate between an unsuppressed IR limit and a suppressed UV limit. At t_ref = 1/M_KK² with the L=12 spectrum cache eigenvalues evaluated in mixed units (per the script's literal computation), `x = t_ref · λ² ≈ 5.3 × 10^{−33}` for every λ, so all four profiles return ≈ 1, all four Mellin moments degenerate to ≈ 3091, and the "rank ordering" becomes a tie that np.argsort breaks by input-array index. The resulting Spearman of −0.4 against the reference anchor is an artifact of the tie-breaking convention, not a substrate-physics statement.

Under FULL-tier evaluation, the four physical regularizations behave structurally differently in the small-x regime:

- **Pauli-Villars (PV)**: subtracts a regulator-mass contribution at fixed scale M_PV that is **independent of t_ref**. The PV-regulated trace Tr_PV[D_K^{−2s}] = Tr[D_K^{−2s}] − Tr[(D_K² + M_PV²)^{−s}] does NOT degenerate to a universal value as t_ref → 0 — the subtraction term is parametrized by M_PV, not by t_ref. PV therefore breaks the SCHEMATIC degeneracy.
- **Heat-kernel** with proper-time t_ref = 1/M_KK²: the dimensionful operator t · λ² requires consistent units. If eigenvalues are read in M_KK² units (so `λ²` is dimensionless and ranges to 29.365), and t_ref is read in absolute GeV^{−2} (so 1/M_KK² = 1.81×10^{−34} GeV^{−2}), the script's literal product is dimensionally mismatched. With consistent units (both in M_KK² units), 1/M_KK² → 1 in dimensionless form and x = λ²·(1/M_KK²)·M_KK² = λ² ∈ [0.66, 29.365], which is in the IR-DISCRIMINATING regime — not UV-degenerate. So even within the heat-kernel family, the degenerate reading is partly a unit-treatment artifact.
- **Mellin**: defined as Σ m_λ λ^{−2s} without any t_ref parameter. At s=4 the sum converges for the L=12 spectrum; there is no anchor degeneracy because there is no anchor.
- **Hard cutoff** Θ(Λ − λ²) with Λ = 1/t_ref = M_KK²: every eigenvalue with λ² ≤ M_KK² passes the cutoff and contributes unity; this DOES degenerate similarly to the SCHEMATIC. But this matches the SCHEMATIC `cutoff_sqrt` profile in the small-x limit (both saturate at 1 below the cutoff).

The user's prompt assertion is correct for PV and Mellin: these do NOT degenerate at small x. The user's assertion for heat-kernel is more subtle: heat-kernel can degenerate similarly to SCHEMATIC exp(-x) at literal small x, but the M_KK² anchor reads small-x only when units are crossed. Under consistent units, the anchor sits in the IR-discriminating regime.

Net structural reading: **the UV-degenerate anchor-5 verdict is SCHEMATIC-specific**, and under FULL-tier evaluation with proper unit treatment, anchor 5 either (a) returns to the IR-discriminating regime (heat-kernel + cutoff with consistent units), (b) gives a non-degenerate finite-rank correction (PV, where the M_PV-dependent subtraction is not in the t_ref family at all), or (c) is undefined (Mellin, no anchor). The N=4/5 PASS would likely become N=5/5 under PV+Mellin (no degeneracy) or remain N=4/5 under heat-kernel+cutoff with the literal SCHEMATIC unit treatment — but in neither case is the −0.4 anchor-5 cross-correlation a stable substrate prediction.

### Result 3 — §W5-7 + §W5-8 jointly establish: rank-level decision at SCHEMATIC tier is bit-exact

**Result**: The Q-exact Sage-equivalent cross-check (Fraction(60,60)=1 for anchors 1–4 self/peer pairs; Fraction(−24,60) = Fraction(−2,5) = −0.4 for anchor 5 cross-pair) confirms the float64 Spearman matrix at machine epsilon (max_abs_diff = 5.55×10^{−17}, 7 OOM inside the 10^{−10} PASS threshold). Classification: **GEOMETRIC** (structural verification-of-equality on integer-rank permutations).

The substantive content of the W5-8 cross-check: for 4-element integer rank vectors, Spearman ρ = 1 − 6Σd²/(n(n²−1)) = 1 − 6Σd²/60 lives in ℚ with denominator 60. The integer Σd² = 14 for the anchor-5 vs anchor-1 pair (computed verbatim in WP §W5-8 step 3) gives Fraction(−24,60) = −2/5 EXACTLY. The float64 representation of −2/5 differs from the closed-form rational only by the 17th-decimal mantissa rounding; this residual is structurally irrelevant to the rank-level decision because the decision rule operates on the integer count N (number of anchors with Spearman ≥ 9/10), not on the float Spearman values themselves.

**What this strengthens**: the rank-level decision rule N=4 is robust under arithmetic-method variation (float64 ↔ ℚ). What this does NOT establish: the SCHEMATIC functional-form mapping itself, the unit-consistency of anchor 5, or the cross-tier (PRIMARY ↔ SCHEMATIC) rank-swap structure. The Q-exact result vindicates the float computation's *arithmetic*; it does not vindicate the *substrate-physics interpretation* of the SCHEMATIC profiles or the cross-tier finding §VII.AR claims.

### Result 4 — §W5-7 contributes to the §(iv) K=4 SCHEMATIC-level-pin calibration corpus as a PARTIAL-POSITIVE instance

**Result**: §W5-7 satisfies two of the three discipline-compliance elements (CLASS pin pre-registered as SCHEMATIC + convention tag carries `-SCHEMATIC` suffix + WP synthesis includes cross-class disclosure block + script docstring carries SCHEMATIC declaration). It does NOT carry the W9c-1-canonical `tier_pin=TIER-2` companion row. Classification: **GEOMETRIC** (methodology-floor classification under the rule-level discipline).

The §(iv) calibration corpus table at K=4 contains:
| # | Witness | Convention suffix | Docstring | tier_pin row | Class |
|---|---------|-------------------|-----------|--------------|-------|
| 1 | W4-2 (S86) | N | — | — | NEGATIVE |
| 2 | W9b-2 (S87) | N | Y (17 hits) | — | NEGATIVE |
| 3 | W9c-1 (S87) | Y | Y (full TIER-2) | Y | POSITIVE |
| 4 | W5b-2 sub-test (c) (S86) | — | — | — | LOCUS-EXEMPT |

§W5-7 sits structurally between W9b-2 and W9c-1:
- Convention `-SCHEMATIC` suffix: YES (`lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4-SCHEMATIC`)
- Docstring SCHEMATIC declaration: YES (verified at script line 22-39: "OPERATIONAL DEVIATION (per substrate-first-canonical-sourcing.md section "(iv)"): ... explicit SCHEMATIC tagging")
- Companion row `tier_pin=TIER-2`: NO (the WP verdict block shows only the dual-SHA companion row and the 3-tuple annotation row)
- Plan-block CLASS pin: YES (explicit "SCHEMATIC functional-form mapping" in plan §W5-7.7 + WP §W5-7 OPERATIONAL DEVIATION block)

This is an intermediate-compliance instance. The author preserved convention-tag honesty (the structurally most important element, because the verdict-line is the audit-trail-canonical surface) and the docstring disclosure (which makes the SCHEMATIC status discoverable at script-read time), but did NOT replicate the W9c-1 explicit `tier_pin=TIER-2 # ...` comment row in the verdict file. Per the calibration corpus's POSITIVE/NEGATIVE binary, §W5-7 is "PARTIAL-POSITIVE" — a refinement the rule's existing taxonomy does not cleanly accommodate.

Per `feedback_rules-compensate-missing-structure.md` K-counter protocol, the corpus advances K=4 → K=5 with §W5-7 as instance #5. The rule status (MANDATORY at K=4 since S88 W7b-83) is unchanged by this advance (the rule is already MANDATORY; further calibration adds robustness, not promotion). The structural lesson is: the discipline's POSITIVE template should be refined to accept "PARTIAL-POSITIVE" (convention+docstring without tier_pin) as a compliant variant, OR the discipline should require all three elements universally and §W5-7 should be flagged as PARTIAL-COMPLIANT with a remediation footnote.

### Result 5 — Per-Bulletin-per-pole Level-1/2/3 ladder declaration: §VII.AR's Level-3 anchor needs caveat

**Result**: Comparison of the §VII.AR registry text's Level-3 declaration to the §W5-7 empirical result reveals that the two empirical pins are measuring DIFFERENT quantities and the registry's `ρ_S = -0.800 EXACT` is not directly validated by §W5-7's Spearman = +1.000 finding. Classification: **GEOMETRIC** (registry-content vs empirical-content alignment audit).

The §VII.AR registry entry at line 16961 declares:
> Level-3: at L_max=12, t_ref_T1 = 1/max(λ²) = 0.0341, M_PV²_frac = 0.1, cutoff_frac = 0.7: ρ_S = −0.800 EXACT, spread_T1 = 1.011 (range [−0.800, +0.211])

But §W5-7's empirical Spearman matrix at the SAME canonical anchor t_ref_T1 = 1/max(λ²) returns **+1.000 for the self-correlation and across anchors 1–4** — not −0.800. Reading the §VII.AR text more carefully, the −0.800 is the *anti-rank-correlation between two LEVEL-DRESSED state-pair functionals at the same anchor* (a cross-functional measurement within Cell IV per W-22 §V.4 4-class taxonomy), not the *anchor-to-anchor rank-preservation* that §W5-7 measured.

These are two structurally distinct Spearman quantities living on orthogonal axes:
- §VII.AR Level-3 anchor: ρ_S(state-pair-functional-A vs state-pair-functional-B | fixed anchor) — algebra-DEPENDENT
- §W5-7 measurement: ρ_S(rank-vector-anchor-i vs rank-vector-anchor-j | same regulator atlas) — algebra-INVARIANT

This is itself an instance of the algebra-axis orthogonality K-counter (MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md`): the LEVEL-DRESSED state-pair-functional view (Level-3 anchor for §VII.AR) and the anchor-sweep spectrum-only view (§W5-7) cannot enter a single non-fungible chain. So §W5-7's PASS does NOT validate the registry's Level-3 anchor, and the registry's Level-3 anchor does NOT predict §W5-7's outcome. The two are complementary measurements on the same substrate observable but at orthogonal cells.

**This is structurally significant**: §VII.AR's empirical Level-3 anchor (ρ_S = −0.800) was set by the S88 W-22 W7a-74 V.5 closure under the LEVEL-DRESSED 4-class taxonomy extension. That measurement is what the registry text is anchored to; §W5-7 supplied a DIFFERENT empirical pin (anchor-to-anchor consistency Spearman = +1.000 at all 4 IR anchors) that targets the per-Bulletin-per-pole Level-2 envelope (consistency rate across anchors as a Casimir-bound proxy).

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W5-7 (S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY) | PASS at SCHEMATIC tier | N=4/5 anchors with Spearman ≥ 9/10; bootstrap σ = 0.0000; convention `-SCHEMATIC` suffix; composite=PASS |
| §W5-8 (S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36) | PASS | max_abs_diff = 5.55×10^{−17} ≪ 10^{−10}; decision_rule_consistent=True; Fraction(−2,5) = −0.4 EXACT for anchor 5 cross-pairs; Fraction(60,60) = 1 EXACT for anchors 1–4 |

Both PASS verdicts are authoritative per the v3-closure ladder (regime VALID + sign N/A + magnitude PASS → composite PASS per gate-verdicts.md S87+ collapse rule). Connes-side does NOT re-adjudicate.

---

## IV. Structural Implications

### IV.1 — §VII.AR registry status: STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP → STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION

The S89 conditional gate ("5-anchor scan with N≥4/5 decision rule") has been satisfied at the SCHEMATIC tier. Per the joint-theorem-promotion.md 4-stage pathway, this is sufficient to drop the "PENDING-ANCHOR-SWEEP" qualifier. The theorem advances to STAGE-1-CANDIDATE; however, the FULL theorem statement (cross-tier rank-PARAMETER coupling under PRIMARY-vs-SCHEMATIC switch) has NOT been directly tested.

The structurally honest registry status is therefore:

```
§VII.AR — STAGE-1-CANDIDATE
  Sub-claim A (intra-class anchor robustness, SCHEMATIC tier): CONFIRMED
    (S89 W5-7 N=4/5 PASS + S89 W5-8 Q-exact PASS)
  Sub-claim B (cross-tier rank-PARAMETER coupling, PRIMARY ↔ SCHEMATIC):
    PENDING CF-W5-2 (S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR)
  Promotion criterion to STAGE-3-PERMANENT:
    (i) CF-W5-2 PASS at FULL-tier with Spearman(SCHEMATIC, PRIMARY) ranking-comparison reported
    (ii) Stage-2 cross-axis independent-verify per joint-theorem-promotion.md
         (the joint clauses include Sub-claim A AND Sub-claim B)
```

The §VII.AR Forward Dispatch routing in the registry text already names "A.36 (S89) S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP" as the gating dispatch; A.36 PASS is the conditional, not the structural completion. The CROSS-TIER carry-forward CF-W5-2 is the next structural-load-bearing gate.

### IV.2 — Per-Bulletin-per-pole K=3 calibration corpus implication

The §VII.AR landing was cited in the registry text (line 16969) as the K=3 promotion event for the Per-Bulletin-per-pole Level-1 wall classification corpus per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`. Corpus members:
1. §VII.K-PROP.W10-4 ρ_∞ permanent-wall (s=4)
2. §VII.U.1 Mellin-Dirichlet identity (s=3)
3. §VII.AR LEVEL-DRESSED rank-ordering (s=4 same pole as W10-4; cohomology-class-distinct)

If §VII.AR's STAGE-1-CANDIDATE survives CF-W5-2 (i.e., CROSS-TIER PASS), the K=3 promotion is structurally validated. If CF-W5-2 FAILs (i.e., PRIMARY ↔ SCHEMATIC rankings COINCIDE rather than swap), §VII.AR's LEVEL-DRESSED finding is weakened and the K=3 advancement should be re-audited: the LEVEL-DRESSED classification was the structurally-novel content distinguishing §VII.AR from the s=3 / s=4 corpus baseline. Without it, §VII.AR collapses to a within-class rank-statement at s=4 that does not differ in kind from §VII.K-PROP.W10-4.

**Recommendation**: the K=3 advancement event recorded at registry line 16969 should be tagged "PROVISIONAL pending CF-W5-2" until the cross-tier finding is independently validated.

### IV.3 — §(iv) K=4 MANDATORY SCHEMATIC level-pin discipline status under §W5-7

The §(iv) discipline does NOT require FULL-tier confirmation as a hard precondition for registry-confirmation at the SCHEMATIC tier. The discipline's force is at the AUDIT-TRAIL DISCLOSURE layer (the verdict line MUST carry the `-SCHEMATIC` suffix; the WP MUST include the cross-class disclosure block; the producing script MUST acknowledge SCHEMATIC-vs-FULL in its docstring). §W5-7 honored all three disclosure requirements; the verdict is admissible registry-confirmation under §(iv) MANDATORY-at-K=4.

What §(iv) DOES require is that the structural content of the registry confirmation is correctly scoped to the SCHEMATIC tier — i.e., the registry text must not silently claim a FULL-tier result on the strength of SCHEMATIC evidence. The §VII.AR text already carries this scoping (its Level-1 declaration says "regulator-PARAMETER-dependent (NOT regulator-CLASS-dependent) under the PRIMARY-vs-SCHEMATIC LEVEL discipline" — the level-discipline qualifier is explicit). §W5-7's PASS at SCHEMATIC tier IS valid evidence for the SCHEMATIC-internal sub-claim; it is NOT evidence for the cross-tier swap claim.

Operationally: the SCHEMATIC-tier PASS is sufficient to drop "PENDING-ANCHOR-SWEEP" from the §VII.AR status, but the registry text's empirical-anchor declaration (ρ_S = −0.800 EXACT) is on a DIFFERENT measurement and is NOT replaced by §W5-7's +1.000 anchor-to-anchor Spearman. Both pins survive in the registry as orthogonal-axis observations on the same §VII.AR theorem.

### IV.4 — Algebra-axis orthogonality K-counter implication

§W5-7 measures an algebra-INVARIANT observable (spectrum-only Mellin-moment rank vectors); the §VII.AR registry Level-3 anchor (ρ_S = −0.800) measures an algebra-DEPENDENT observable (state-pair functional cross-correlation). Both validly anchor §VII.AR but on orthogonal axes of the 4-corner classification.

This is calibration corpus instance for the algebra-axis orthogonality discipline at the SAME theorem — i.e., §VII.AR is a theorem whose Level-3 anchor and Level-2 envelope live on orthogonal axes. The discipline's MANDATORY-at-K=3 status (since S87 W-2 R3 close) means this orthogonality is structurally required: a registry entry that conflates the two axes into a single empirical pin would be a cross-corner co-primary structure, which is FORBIDDEN per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clause 4 (S88 W-15 V.6).

§VII.AR is correctly structured (the two anchors are on orthogonal axes, not co-primary). §W5-7 + §W5-8 supply the algebra-INVARIANT axis empirical anchor; the algebra-DEPENDENT axis empirical anchor was supplied by S88 W-22 W7a-74 V.5 / B.55. CF-W5-2 will refine the algebra-INVARIANT anchor with FULL-tier resolution.

---

## V. Carry-Forward Computations

### V.1 — Re-execute §W5-7 under canonical W7a-74 PRIMARY evaluator (FULL-tier)

| Field | Value |
|:------|:------|
| **What** | Re-execute S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY using the canonical W7a-74 PRIMARY evaluator script (FULL physical regularization: Pauli-Villars subtraction at fixed M_PV²_frac=0.1, hard cutoff at cutoff_frac=0.7, Mellin via analytic_zeta, zeta and heat-kernel via the canonical `_spectral_action_regulators.py` helpers — NOT SCHEMATIC functional-form mapping). Output the full 5-anchor Spearman matrix at FULL tier AND the cross-tier Spearman comparing FULL-tier rank vectors to §W5-7 SCHEMATIC rank vectors. Required: anchor-5 unit-consistency check (both t_ref and λ² in the same dimensionful or dimensionless form). |
| **Inputs** | (i) `sessions/archive/session-87/<W7a-74 PRIMARY evaluator script>` (locate exact path at S90 plan-freeze; the W-22 V.5 §VII.AR registry text references "PRIMARY evaluator" without a specific script-name pin — first plan-freeze action is to find or commit a canonical PRIMARY evaluator script); (ii) `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (165,896 eigenvalues at τ=0.190; same input as §W5-7 for direct comparison); (iii) `computations/_shared/_spectral_action_regulators.py` (canonical regulator helpers: zeta_a_n, mellin_a_n, heat_kernel_a_n, hard_cutoff_a_n, pauli_villars_a_n); (iv) `sessions/permanent-results-registry.md §VII.AR` (registry baseline for cross-check); (v) §W5-7 npz `s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz` (SCHEMATIC rank vectors and Spearman matrix). |
| **Gate** | Pre-registered S90 gate `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR`. **PASS-A iff** N_FULL ≥ 4/5 AND Spearman(rank_vectors_SCHEMATIC, rank_vectors_FULL) ≥ 0.9 at the canonical anchor t_ref_1 (cross-tier rankings COINCIDE; SCHEMATIC was a faithful proxy; §VII.AR LEVEL-DRESSED finding is WEAKENED because no cross-tier swap exists). **PASS-B iff** N_FULL ≥ 4/5 AND Spearman(SCHEMATIC, FULL) < 0.9 (cross-tier rankings DIFFER; §VII.AR LEVEL-DRESSED finding is STRENGTHENED — this is the registry's claimed cross-tier rank-PARAMETER coupling). **INFO iff** N_FULL ∈ {3}. **FAIL iff** N_FULL < 3 OR FULL-tier produces all-tied / NaN rankings (regime BREAKDOWN). The PASS-A vs PASS-B distinction is the structural-load-bearing discriminator for §VII.AR. |
| **Effort** | 1.0 wave-equivalent (script-write to locate / build the W7a-74 PRIMARY evaluator: ~0.4 wave; FULL-tier 5-anchor sweep at L_max=12: ~0.3 wave; cross-tier Spearman comparison + WP synthesis: ~0.3 wave). Agent assignment: `lizzi-spectral-functional-theorist` PRIMARY (continues from §W5-7 ownership) + `connes-ncg-theorist` co-sign on FULL-tier-vs-SCHEMATIC structural reading. |

### V.2 — Stage-2 cross-axis independent-verify for §VII.AR

| Field | Value |
|:------|:------|
| **What** | Pre-register and dispatch the Stage-2 cross-axis independent-verify gate for §VII.AR per the `joint-theorem-promotion.md` 4-stage pathway. The two cross-reviewers MUST be on DIFFERENT axes (Axis-A spectral-functional, Axis-B substrate-physics or NCG-axiomatic) AND MUST NOT be the original W-22 authors (connes-ncg-theorist + lizzi-spectral-functional-theorist). Cross-reviewer assignments candidate: `gen-physicist` (spectral side, distinct downstream-inheritance lineage from lizzi+connes per S88 W-14 V.2 calibration precedent for §VII.W-3.LAB) + `volovik-superfluid-universe-theorist` (substrate side; "framework's SHARPEST reviewer" per agent-memory feedback). Both review (a) Sub-claim A (intra-class anchor robustness, validated by §W5-7+§W5-8) AND (b) Sub-claim B (cross-tier rank-PARAMETER coupling, validated by V.1 above). Joint clauses include both. |
| **Inputs** | (i) §VII.AR registry entry text (`sessions/permanent-results-registry.md` lines 16948-16978); (ii) §W5-7 + §W5-8 WP sections + verdicts; (iii) V.1 output (FULL-tier rank-comparison); (iv) S88 W-22 W7a-74 V.5 / B.55 workshop text `sessions/archive/session-88/workshops/s88-w22-w7a-74-rank-vs-magnitude.md`. Cross-reviewers receive ONLY the registered theorem text + V.1 outputs + §W5-7/§W5-8 final pins — NOT the W-22 workshop transcripts (per joint-theorem-promotion.md §"Stage 2" Axis-B Selection Protocol clause "without prior workshop context"). |
| **Gate** | Pre-registered S90+ gate `S90-VII-AR-STAGE-2-INDEPENDENT-VERIFY`. **PASS iff** BOTH cross-reviewers return PASS on Sub-claim A AND PASS on Sub-claim B (logical AND; joint clauses PASS-AND'd). **FAIL iff** EITHER cross-reviewer returns FAIL on ANY clause (Stage 2 → 3 promotion blocked; theorem stays at STAGE-1-CANDIDATE; FAILing clauses route to next-session remediation). **INFO iff** EITHER cross-reviewer returns INFO on a clause (theorem stays at STAGE-1-CANDIDATE; INFO clause documented as Stage-2-INFO-deferred). |
| **Effort** | 1.5 wave-equivalents (Stage-2 two-agent parallel dispatch; each cross-reviewer ~0.6 wave; orchestrator synthesis ~0.3 wave). Effective dispatch is conditional on V.1 completing FIRST (the FULL-tier comparison is one of the cross-reviewers' inputs); recommend wave-ordering V.1 → V.2 in the S90 plan. |

### V.3 — Refine §(iv) calibration corpus to admit PARTIAL-POSITIVE classification

| Field | Value |
|:------|:------|
| **What** | Extend `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` calibration corpus table to admit a third compliance class "PARTIAL-POSITIVE" between the existing POSITIVE (W9c-1 full TIER-2 disclosure) and NEGATIVE (W4-2 / W9b-2 missing-suffix or post-hoc-disclosure) classes. §W5-7 is the first PARTIAL-POSITIVE instance (convention-suffix YES + docstring SCHEMATIC YES + tier_pin row NO + plan-block CLASS pin YES). The rule extension defines PARTIAL-POSITIVE compliance, advances the corpus K=4 → K=5 with §W5-7 as instance #5, and pre-registers the audit-script extension `_substrate_first_provenance_audit.py` (S87 V.1 carry-forward) sub-check to detect missing `tier_pin=TIER-2` companion rows as PARTIAL-POSITIVE rather than NEGATIVE. |
| **Inputs** | (i) `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` calibration corpus table; (ii) §W5-7 verdict line + companion rows (`computations/session-89/s89_gate_verdicts.txt` lines 101-103); (iii) §W5-7 producing-script docstring lines 22-39 (SCHEMATIC declaration verified); (iv) W9c-1 reference pattern (`computations/session-87/s87_w9c_csub_axiom_cross_review.py` docstring + verdict-file companion row at line 266); (v) `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold. |
| **Gate** | Pre-registered S90+ gate `S90-IV-PARTIAL-POSITIVE-CALIBRATION-CLASS-EXTENSION` (METHODOLOGY-class per `wave-classification.md` M1 ∧ M2 ∧ M3 ∧ M4; allowlist append required). **PASS iff** rule file extended with PARTIAL-POSITIVE class definition + §W5-7 entry added to corpus table + audit-script extension landed + content_sha256 over rule-file diff matches input-pin-map-derived hash. **FAIL iff** rule extension scrambles the existing POSITIVE/NEGATIVE distinction or admits a new failure pathway. **INFO iff** the PARTIAL-POSITIVE class is admitted but a 3-of-3 strict-MANDATORY alternative is queued for further deliberation. |
| **Effort** | 0.3 wave-equivalents (METHODOLOGY-class wave; orchestrator-direct edits + audit-script regex extension + verdict-line emission per `mechanical-closure-discipline.md` discipline). Agent assignment: orchestrator (per wave-classification.md §"Dispatch consequences"); CO-AUTHOR connes-ncg-theorist for compliance-class-distinction structural review. |

### V.4 — Per-Bulletin-per-pole K=3 advancement provisional-tagging

| Field | Value |
|:------|:------|
| **What** | Edit the §VII.AR registry text at `sessions/permanent-results-registry.md` line 16969 to tag the K=3 advancement event "PROVISIONAL pending CF-W5-2 (V.1)". Specifically: change "K=3 ≥ K_promotion=3 ⇒ MANDATORY-at-cohomology-class-distinct-K=3 promotion event triggered" to "K=3 ≥ K_promotion=3 ⇒ PROVISIONAL MANDATORY-at-cohomology-class-distinct-K=3 promotion event triggered (pending CF-W5-2 cross-tier confirmation; if CF-W5-2 returns PASS-A coinciding rankings, §VII.AR LEVEL-DRESSED finding weakens and K=3 corpus member is re-audited; if PASS-B differing rankings, structural promotion is unconditional)". |
| **Inputs** | (i) `sessions/permanent-results-registry.md §VII.AR` (line 16969); (ii) `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` §"Forward enforcement" + §"Status" blocks (already admit mixed-status interpretation); (iii) §W5-7 + §W5-8 WP synthesis (sub-claim A vs sub-claim B decomposition). |
| **Gate** | Pre-registered S90+ gate `S90-PROVISIONAL-K3-TAGGING-VII-AR` (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md` registry-row discipline). **PASS iff** registry text carries the provisional tag + CF-W5-2 conditional language is structurally precise + content_sha256 over registry diff matches input pin map. **FAIL iff** tagging admits silent demotion of the K=3 corpus member or scrambles the existing per-Bulletin-per-pole structural confidence ladder. |
| **Effort** | 0.2 wave-equivalents (registry-text edit + audit verification; trivial METHODOLOGY-class). |

### V.5 — Anchor-5 unit-consistency audit (orthogonal-to-V.1 substrate-physics-side check)

| Field | Value |
|:------|:------|
| **What** | Independent of CF-W5-2 / V.1, run a focused diagnostic computation that reads the §W5-7 producing script `s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py` and verifies whether anchor 5 (1/M_KK²) is being computed with consistent units relative to the eigenvalue cache (which is in dimensionless M_KK² units). The diagnostic should produce a side-by-side comparison: anchor-5 result under (a) the script's literal mixed-units treatment (t_ref in GeV^{−2}, λ² dimensionless) → x ≈ 5×10^{−33}; (b) consistent dimensionless treatment (both in M_KK² units) → x = λ² ∈ [0.66, 29.365]; (c) consistent absolute treatment (both in GeV^{−2}, eigenvalues converted) → x = λ²·M_KK²·(1/M_KK²) = λ² ≈ same as (b). The outcome determines whether the UV-degenerate reading is genuinely a SCHEMATIC artifact, a unit-treatment artifact, or both. |
| **Inputs** | (i) `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py` (specifically the anchor-5 / x-product computation lines); (ii) `computations/_shared/canonical_constants.py` for M_KK = 7.429×10^{16} GeV and the conventional unit assignment of the eigenvalue cache; (iii) `computations/session-84/s84_spectrum_cache_L12_tau019.npz` documentation (what units are the λ² values in?); (iv) `regulator-pin-discipline.md` a_n^{HK} tagging conventions. |
| **Gate** | Pre-registered S90+ gate `S90-W5-7-ANCHOR-5-UNIT-CONSISTENCY-AUDIT`. **PASS iff** the script's anchor-5 reading is correctly traced to a SCHEMATIC-vs-unit-treatment decomposition AND the §W5-7 WP §(f) "UV-degenerate explanation" is amended to disclose the unit-treatment subtlety. **INFO iff** the unit treatment is ambiguous and a separate canonical-constants pin is required (`lambda_unit_canonical = "M_KK_sq"` or `"GeV_sq"`). **FAIL iff** the unit treatment is structurally inconsistent in a way that propagates to other §W5-* gates (would require broader Wave 5 retraction). |
| **Effort** | 0.2 wave-equivalents (single-script diagnostic; small workload). Agent assignment: `gen-physicist` (unit-consistency cross-checks across substrate-physics scripts are within gen-physicist's domain per agent-roster) OR `lizzi-spectral-functional-theorist` (continuation from §W5-7 ownership). |

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | §VII.AR has two sub-claims (intra-class anchor robustness + cross-tier rank-PARAMETER coupling); §W5-7 PASS validates only sub-claim A | GEOMETRIC | LANDED-SCHEMATIC-PARTIAL | §VII.AR status → STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION; CF-W5-2 is structurally load-bearing for sub-claim B |
| 2 | Anchor 5 UV-degenerate reading is SCHEMATIC-specific (with unit-treatment subtlety); does NOT persist under FULL-tier evaluation | GEOMETRIC | SCHEMATIC-ARTIFACT-IDENTIFIED | PV does not degenerate (M_PV-fixed subtraction independent of t_ref); Mellin uses no t_ref; heat-kernel/cutoff degenerate only under cross-unit reading; FULL-tier expected to recover IR-discriminating regime |
| 3 | §W5-7 + §W5-8 jointly establish rank-level decision robustness under arithmetic-method variation (float64 ↔ ℚ) | GEOMETRIC | Q-EXACT-CONFIRMED | Strengthens the SCHEMATIC sub-claim arithmetically; does NOT extend it to FULL-tier or substrate-physics content |
| 4 | §W5-7 advances §(iv) K=4 SCHEMATIC-level-pin calibration corpus to K=5 as PARTIAL-POSITIVE | GEOMETRIC (methodology) | CORPUS-ADVANCE | §(iv) discipline taxonomy should admit PARTIAL-POSITIVE class; convention-suffix + docstring without `tier_pin=TIER-2` companion is intermediate between W9b-2 NEGATIVE and W9c-1 POSITIVE |
| 5 | §VII.AR registry Level-3 anchor (ρ_S = −0.800) and §W5-7 Spearman (+1.000) measure orthogonal axes; both validly anchor §VII.AR on different algebra-axis cells | GEOMETRIC | ORTHOGONAL-ANCHOR-COMPLEMENTARITY | Algebra-axis orthogonality K-counter (MANDATORY at K=3) is honored; registry text correctly does NOT conflate the two empirical pins |

---

## Authorship attribution

connes-ncg-theorist solo-synthesis report under `/rclab-review` skill invocation. Independent reading of §W5-7 SCHEMATIC PASS implications under the §(iv) MANDATORY-at-K=4 level-pin discipline; no coordination with the §W5-7 / §W5-8 producing agent (lizzi-spectral-functional-theorist) or with the original §VII.AR co-author (also lizzi). Connes-side conclusions feed S90 plan-freeze priority ordering: V.1 (CF-W5-2 cross-tier validation) is the highest-priority follow-up because it is the structural load-bearing test for the §VII.AR theorem's distinctive claim; V.2 (Stage-2 cross-axis verify) is conditional on V.1; V.3 (rule-level PARTIAL-POSITIVE extension) is methodology-class and independent of V.1/V.2 outcomes; V.4 (provisional K=3 tagging) and V.5 (anchor-5 unit-consistency audit) are low-effort hygiene fixes that can land in S90 W0.

Source documents read in full: W5 WP §W5-7 + §W5-8 + Wave-5 synthesis + carry-forwards (lines 1815-2530); W5 plan §W5-7 + §W5-8 (lines 1552-1959); permanent-results-registry §VII.AR (lines 16948-16978) + §VII.AS context (16979-17005) + §VII.AQ context (17008-17094); substrate-first-canonical-sourcing.md §(iv) calibration corpus + reclassification clauses (in system context); cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" + §"Per-Bulletin-per-pole Level-1 wall classification" (in system context); producing-script docstring at `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py` lines 1-50 (SCHEMATIC declaration verified).
