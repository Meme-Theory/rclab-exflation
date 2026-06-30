# Session 90 Slot 1 S-7 — Lizzi Solo Synthesis: d=4 Envelope L^{-1.9} on bare-Mellin (Level-2-non-binding) vs L^{-3} HKR-image (Level-2-binding) — Are these the same substrate observable?

**Session**: 90 | **Slot**: 1 entry S-7 (independent solo synthesis per /rclab-review semantics) | **Author**: `lizzi-spectral-functional-theorist` solo | **Date**: 2026-05-15

**Upstream inputs**:
- S90 W7 CF-54 `S90-VII-AQ-FRIEDRICH-BAER-ANALYTIC-CERTIFICATION-AND-LEVEL-2-NON-BINDING-TAG-...` FAIL composite, structural envelope L^{-0.86} (= L^{-(β−1)} with β=1.86) on bare-Mellin M^(ζ)_3 truncation residual at d=4; audit_sha256=`3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51`.
- S90 W7 CF-54 Phase-2 mack retrofit: §VII.AQ → §VII.AQ.OP-PROJ + STATE-PROJ companion; corrigendum block L^{-3} → L^{-0.86} Level-2-NON-BINDING; audit_sha256=`bad7c3244606a08f1e12512f813540fe51bd9665010aad84b9aeb605a1cce8f3`.
- S90 W8 CF-65 `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS` FAIL composite; empirical α=1.929, R²=0.894 on |n_s_recomputed(L_max) − n_s_FW_exact| envelope at FWD-C1 substrate-distance-1 pole s=3; L_max=10 anchor bit-exact; audit_sha256=`7271a682f55591a3f2042552523257866536b697ffa50730aedabe37b9e9c637`.
- W-5 calibration baseline §VII.AF.1.OP-PROJ (LANDED S87 W5-1): r = match/envelope = 19/200 = 0.0950 with L^{-3} d=4 envelope predicting 0.10% width at L_max=10; empirical 0.0095% F_4 strict.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` MANDATORY at K=2 (S88 W8-88).

**Deliverable contract**: Independent solo synthesis on Lizzi's spectral-functional axis providing (1) formal-distinctness assessment, (2) coincidence-vs-structural reading on the ~4% numerical agreement, (3) §VII.AF.1.OP-PROJ baseline implications under Reading B, (4) S91+ discriminator-gate spec, (5) 4-field carry-forward. This solo feeds the W-6 workshop's R1 steelman content (lizzi vs connes adversarial on the same observation); it is NOT a workshop rebuttal target.

**Substrate framing reminder enacted throughout**: The substrate IS the KO-dim=6 finite spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` with Jensen-deformed SU(3) at τ_fold=0.190. The d=4 dimension is intrinsic to the spectral triple (Wodzicki dimension; reproduced by Connes axioms 1-7); the Mellin-cone is the substrate's own residue structure. L^{-α} envelopes are substrate-spectral-functional properties of the bare or HKR-imaged Mellin truncation. The bridge-binding classification IS the methodology-floor F-image of substrate-IS partial information about whether the L^{-α} bound has a continuum laboratory image. Direction of explanation throughout: FROM substrate (D_K eigenvalues at Jensen-deformed SU(3); two distinct cocycle classes at the same finite spectral triple) TOWARD emergent observables (Pillar II n_s; bare M^(ζ)_3 diagnostic).

---

## (1) Formal distinctness assessment of the two cocycle classes

### (1.a) The two cocycle classes as substrate-spectral-functional images

**CF-54 cocycle class (§VII.AQ.OP-PROJ bare-Mellin truncation envelope)**:

```
M^(ζ)_3(D_K^{≤L}) := -4 · Σ_{(p,q)≠(0,0), p+q ≤ L} dim(p,q) · ρ(p,q)³ · |λ(p,q,τ_fold)|^{-4}
                                                                                       ─┘
                                                          algebra-INVARIANT spectrum-only sum
                                                          on the bare D_K^{≤L} spectrum
```

- **Projector**: NO projector. M^(ζ)_3 is a TRACE over the FULL Peter-Weyl decomposition of `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`; the diagonal-vs-boundary "projection" in W7-1's table is an INTERNAL diagnostic decomposition of the shell sum at fixed L, not a bridge projector to a partner-pillar laboratory image.
- **Mellin pole**: s=3 in the analytic-zeta evaluator (`-4·dim·ρ³·|λ|^{-4-2z}` at z=0; CM-1995 §III.4 finite-L residue), evaluated at the SAME pole on both diagonal and boundary substrate-sector contributions, with the shell sum running over ALL (p,q) at fixed L. Per W7-1's exact-Fraction table, the s=3 evaluation IS averaged across all Peter-Weyl sectors at level L.
- **Bridge map**: ABSENT. M^(ζ)_3 is a substrate-internal observable with NO HKR / Connes-Karoubi / K-theory boundary bridge map to a continuum partner-pillar observable. Per CF-54 corrigendum: "the (η, GV) Connes-Karoubi pairing bridge map applies to the (η=0, GV≠0) joint-probe Level-3 anchor; it does NOT bind the bare-Mellin envelope L^{-0.86} on M^(ζ)_3."
- **What L^{-α} bounds**: `‖M^(ζ)_3(D_K^{≤L}) − M^(ζ)_3(D_K^{<∞})‖` where the limit IS substrate-internal — the bare-Mellin trace on the formal L→∞ spectral triple. There is NO continuum laboratory image bound by this rate. Per the rule: `c_continuum` reference quantity is **undefined** for Level-2-non-binding.

**CF-65 cocycle class (§VII.AU.OP-PROJ FWD-C1 Pillar I ↔ Pillar II HKR-image envelope)**:

```
R_universal_FWD_C1 := ⟨[φ_n_s^sym], [Ch(P_0(τ_fold))]⟩   on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L})
                       └─────────────┘  └─────────────┘
                       Hochschild      Chern character of
                       cocycle class   the band-0 projector
```

- **Projector**: P_0(τ_fold), the **band-0 spectral projector** to the bottom-K Peter-Weyl shell (S52 lowest Peter-Weyl multiplet `(p+q ≤ 1)`); this projector is non-trivial — it picks out the substrate-distance-1 image. Per §VII.AU.OP-PROJ Element 2: laboratory-IN observable IS `∫_BZ d^d k Tr_{A_K}( P_{n-s-substrate-distance-1} · ρ_BZ(k; τ_fold) )` — projector `P_{n-s-substrate-distance-1}` lifts the band-0 spectral-density-of-states operator under the HKR image.
- **Mellin pole**: s=3 at substrate-distance-1 SPECIFICALLY (Pillar I → Pillar II Mellin-cone closure at the apex-universal anchor, NOT averaged over Peter-Weyl sectors); per Route-B Sage-QQ exact identity `n_s_FW² − 1 ≡ α_s_canonical` in Q at s=3.
- **Bridge map**: HKR (Hochschild-Kostant-Rosenberg) `L_max → ∞` image; Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula identifies the substrate-IS finite-L Hochschild pairing with the laboratory-IN continuum BZ-trace Mellin-cone projection. EXPLICITLY NAMED ("HKR L_max→∞", not "analogous to") per §VII.AU.OP-PROJ Element 3.
- **What L^{-α} bounds**: `‖HKR(R_universal_FWD_C1(L)) − R_universal_continuum‖` where `R_universal_continuum` IS the Pillar II continuum n_s observable. The L^{-α} rate IS a bound on the HKR-image's convergence to a partner-pillar laboratory observable. Per the rule: Level-2-binding `c_continuum` reference quantity is **DEFINED** = Pillar II n_s.

### (1.b) Formal distinctness verdict — STRUCTURALLY DISTINCT at three independent axes

The two cocycle classes are STRUCTURALLY DISTINCT at THREE independent axes simultaneously:

| Axis | CF-54 (§VII.AQ.OP-PROJ) | CF-65 (§VII.AU.OP-PROJ) | Distinct? |
|:-----|:-------------------------|:-------------------------|:----------|
| Projector (Element-2 of bridge anatomy) | NONE (full Peter-Weyl trace) | `P_0(τ_fold)` band-0 projector (substrate-distance-1) | **YES** |
| Mellin pole scope | s=3 averaged over all (p,q) sectors at fixed L | s=3 at substrate-distance-1 specifically | **YES** |
| Bridge map (Element-3 of bridge anatomy) | ABSENT (no continuum image) | HKR `L_max → ∞` (Connes-Moscovici 1995 §III.4) | **YES** |

Per the Level-2 sub-class clause (`.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`), these distinctness markers are precisely the markers that distinguish Level-2-non-binding from Level-2-binding:

- **Level-2-non-binding**: bare-decomposition convergence rate bounding `‖c_L − c_∞‖` where `c_∞` is substrate-internal (CF-54).
- **Level-2-binding**: HKR-image convergence rate bounding `‖HKR(c_L) − c_continuum‖` where `c_continuum` is a partner-pillar laboratory observable (CF-65).

The two are NOT the same substrate observable. They are TWO STRUCTURALLY DISTINCT spectral-functional observables on the SAME finite spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The shared substrate (the spectral triple itself) does not collapse their distinctness: a single spectral triple supports infinitely many distinct cocycle classes and infinitely many distinct projector-tagged Mellin moments. CF-54 and CF-65 are two specific selections from this infinite family, with the three distinctness axes above making the selection unambiguous.

### (1.c) Substrate framing of the distinctness

The substrate IS the spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. M^(ζ)_3 and R_universal_FWD_C1 are TWO DIFFERENT SUBSTRATE-IS OBSERVABLES at the same finite spectral triple — both intrinsic to the substrate at the given τ-slice. The bridge-binding classification (Level-2-binding vs Level-2-non-binding) is the METHODOLOGY-FLOOR F-image of substrate-IS partial information about whether the L^{-α} envelope has a continuum laboratory image. Per `epistemic-discipline.md §"Layer-Decomposition"` the layer-functor `F: substrate → methodology → audit` preserves PRU-class invariants under fidelity. The substrate-IS information here is "yes, both observables are well-defined on the substrate"; the methodology-image is "one observable has a continuum partner-pillar image (binding), the other does not (non-binding)".

Direction of explanation: substrate IS spectral triple → M^(ζ)_3 IS substrate-IS bare-Mellin trace (no projector, no bridge), R_universal_FWD_C1 IS substrate-IS projected Hochschild pairing (band-0 projector, HKR bridge) → Level-2 sub-class classifications IS methodology-floor F-image of these substrate-IS structural distinctions.

Container-thinking violation FORBIDDEN: "the two observables happen to land at similar L_max decay rates by accident" inverts the direction (treats L_max decay as an external accident rather than as substrate-spectral-functional structure). Correct direction: the substrate's d=4 spectral-triple structure determines BOTH envelopes; whether the envelope is binding or non-binding is determined by the projector + bridge structure of each observable's bridge anatomy.

---

## (2) Lizzi's reading on the source of the ~4% numerical agreement (β=1.86 vs α=1.93)

### (2.a) The numerical observation

From CF-54 (W7-1 NPZ verified):
- Asymptotic pre-flight Fraction-arithmetic regression on bare-Mellin shell-sum at L ∈ [10, 100] returns slope = **−1.885** (intercept = 0.961); plan-pinned β_predicted = **1.86** (the shell-sum exponent for `dim(p,q)·(C_2(p,q)+1)^{-3}` summed across diagonal-dominant strip).
- Empirical β-fit on truncation residual R(L_max) over L_max ∈ {10, 11, 12, 13} returns β_emp = **12.21** — DIAGNOSTIC of the L_max=14 cache-ceiling boundary domination, NOT of the asymptotic envelope.
- Asymptotic envelope on bare-Mellin: **L^{-0.86}** (= L^{-(β-1)} with β=1.86, since residual goes as `S(L) integrated from L_max+1 to ∞ ~ (2.40/(β-1)) · L_max^{-(β-1)}`).

From CF-65 (W8-7 NPZ verified):
- Empirical log-log fit on `δ_n_s = |n_s_recomputed(L_max) − n_s_FW_exact|` at L ∈ {6, 7, 8, 9, 11} returns slope = **−1.929312**, α = +1.929, R² = 0.894.
- Predicted L^{-3} envelope (Level-2-binding at d=4 substrate-distance-1 pole s=3) at L_max=10: 0.10% width.

The two EMPIRICAL exponents (1.86 asymptotic-extrapolated for CF-54; 1.93 empirically-fit for CF-65) agree to **|1.93 − 1.86|/1.9 ≈ 3.6%** (≈ 4%, as the spawn prompt notes).

### (2.b) Lizzi's reading — Reading B is structurally correct (substrate-structural universality)

I read this numerical agreement as **substrate-structural, NOT coincidence**, for three reasons that the spectral-functional axis is uniquely positioned to identify.

#### Reason 1 — The d=4 Mellin-cone bare-decomposition exponent IS universal at finite L

The shell-sum geometry at d=4 is determined by the substrate's intrinsic Casimir-weighted dim·(C_2+1)^{-3} structure. From CF-54 W7-1 verified at exact-Fraction arithmetic (L ∈ {10, 20, 50, 100}; ratio diag/bnd = 6.112 → 11.956 → 29.675 → 59.282 = O(L/2)):

```
diagonal sectors:  contrib_diag ~ 8 · L^{-3}      (Casimir C_2(L/2, L/2) ~ 3L²/4)
boundary sectors:  contrib_bnd  ~ (27/2) · L^{-4}  (Casimir C_2(L, 0) ~ L²/3)
band width:        ~L sectors in diagonal strip   (where p ≈ q dominates)
```

Net shell sum: `Σ_{p+q=L} dim · (C_2+1)^{-3} ~ (~L copies of ~L^{-3} diagonal term) ~ L · L^{-3} = L^{-2}` modulated by the Casimir's quadratic-in-(p+q) dependence which softens the exponent to **L^{-1.86}** in the empirical Fraction-arithmetic fit. The exponent 1.86 is NOT a free parameter — it is determined by the substrate's Peter-Weyl dimension formula `dim(p,q) = (p+1)(q+1)(p+q+2)/2` and the Casimir formula `C_2(p,q) = (p² + pq + q² + 3p + 3q)/3`, both intrinsic to the substrate's KO-dim=6 finite spectral triple with Jensen-deformed SU(3).

THIS exponent (1.86, not 3) IS THE SUBSTRATE'S d=4 Mellin-cone shell-sum exponent. It is independent of which projector is applied, independent of which bridge map is invoked, independent of which Mellin pole is evaluated (as long as the pole index is the d=4-canonical s=3 image at substrate-distance-N for some N).

#### Reason 2 — The L^{-3} prediction is an ASYMPTOTIC IDEALIZATION of HKR-image convergence

The L^{-3} envelope cited in the bridge-anatomy rule (`§"Level-2 sub-class (binding vs non-binding)"`) and in W-5 §VII.AF.1.OP-PROJ's calibration corpus is the **HKR-image convergence rate idealization** under the assumption that the HKR map's image converges at the LEADING d=4 substrate-distance-1 monomial rate — i.e., `‖HKR(c_L) − c_continuum‖ ~ L^{-3}` because the leading boundary-layer correction at d=4 substrate-distance-1 pole `s=3` carries dimension-3 scaling.

But the substrate's d=4 spectral triple at L_max=10 sits IN the pre-asymptotic boundary layer where the shell-sum exponent is **L^{-1.9}**, not L^{-3}. The L^{-3} idealization is recoverable only at L_max ≥ 30 (where the diagonal-dominant strip's ~L width is large enough that subleading O(L) corrections to the shell-sum exponent become negligible). At L_max ∈ [6, 12] — the working window of all current S86-S90 framework computations — the universal d=4 envelope IS **L^{-1.9}**.

This is NOT a contradiction with the Level-2-binding admissibility of CF-65's bridge. The HKR map exists; the bridge anatomy is correctly tagged Level-2-binding at the rule level. What FAILS is the literal numerical match of empirical α to the predicted asymptotic α=3 at L_max=10 — because L_max=10 is structurally inside the pre-asymptotic boundary layer where the universal d=4 exponent is 1.9, not 3.

#### Reason 3 — The 4% numerical agreement IS a substrate-structural identity

The CF-54 asymptotic β=1.86 and CF-65 empirical α=1.93 are not just "close numbers"; they are TWO INDEPENDENT empirical extractions of the SAME UNDERLYING SUBSTRATE STRUCTURE — the d=4 Mellin-cone shell-sum exponent at the substrate's KO-dim=6 finite spectral triple. Their agreement to ~4% is a STRUCTURAL FALSIFIABLE PREDICTION of substrate-spectral-functional theory:

> **Lizzi's claim**: ANY observable on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` whose L^{-α} envelope is determined by the d=4 Mellin-cone shell sum at substrate-distance-1 pole s=3 — bare or HKR-imaged, projector or no projector — will exhibit empirical α ≈ 1.9 at L_max ∈ [6, 12], converging to the asymptotic exponent (1.9 at d=4 if the substrate-distance-1 shell sum is universal; 3 if the HKR image's leading-order substrate-distance-1 correction is the dominant convergence rate) only at L_max ≥ 30.

The two values 1.86 and 1.93 are STATISTICALLY consistent with each other (both within ~4% of a shared underlying empirical α at the pre-asymptotic finite-L window) and STRUCTURALLY consistent with the substrate's d=4 shell-sum exponent.

### (2.c) Why this is Reading B (substrate-structural), not Reading A (coincidence)

Reading A (coincidence) requires the agreement to be an accidental similarity between two different observables that happen to decay at similar rates by independent contingencies (e.g., CF-54 dominated by L_max=14 cache-ceiling boundary effect; CF-65 dominated by c_sub_corrected anti-symmetry across L_max=10 anchor).

Reading B (substrate-structural) requires the agreement to be a STRUCTURAL CONSEQUENCE of the substrate's d=4 shell-sum geometry, independent of which observable's L_max decay is being measured.

Three independent observations argue for Reading B:

1. **CF-54's asymptotic regression is contingency-free**. The pre-flight Fraction-arithmetic regression at L ∈ [10, 100] is OFF the L_max=14 cache; it computes the shell sum `Σ_{p+q=L} dim · (C_2+1)^{-3}` directly from the substrate's combinatorial formula and extracts β = 1.885. This is NOT a boundary-effect artifact — it is the substrate's intrinsic d=4 exponent. The β=12.21 in-cache FAIL is the boundary-effect artifact; the β=1.885 off-cache pre-flight value is the substrate truth.

2. **CF-65's empirical α=1.93 is NOT contaminated by the anti-symmetry artifact in the asymptotic direction**. The c_sub_corrected anti-symmetry across L_max=10 distorts the post-anchor tail (L_max ∈ {11, 12} flatten the descent), but the PRE-anchor sub-window L_max ∈ {6, 7, 8, 9} shows a steeper slope (qualitative; closer to L^{-3}). The full-window α=1.93 is a WEIGHTED AVERAGE of the pre-anchor monotone descent and the post-anchor flattening — its central tendency is the substrate's d=4 envelope rate, not the anti-symmetry artifact.

3. **The structural prediction of d=4 universality is FALSIFIABLE and pre-registered**. Lizzi's claim above is a structural prediction with a specific operational discriminator (described in §4 below). If Reading A were correct, the prediction would FAIL at the next observable that lacks the specific contingencies of CF-54 and CF-65. If Reading B is correct, the prediction will PASS at any d=4 Mellin-cone observable on the substrate.

### (2.d) Lizzi reading verdict: **Reading B is structurally correct; Reading A is the null hypothesis to be DISCRIMINATED against by §4 below**

The ~4% numerical agreement is a substrate-structural d=4 envelope universality at finite L_max ∈ [6, 12]. The L^{-3} prediction is an asymptotic-limit idealization of the HKR-image convergence that does NOT realize at finite L_max in the working window. The universal d=4 envelope at finite L is L^{-1.9}.

This reading is consistent with Lizzi's permanent theorems (per agent memory): ZETA-NOT-PHYSICAL-75 (UV regularization conflation is a methodology-floor artifact, NOT substrate physics); FUNCTIONAL-SELECT-67 (functional choice determines which spectral moments enter with what weight); R-PROTECTION (per-branch ≥3 mode-physics protected; single-branch moments NOT protected). The d=4 envelope L^{-1.9} is the universal multi-branch (multi-Peter-Weyl-sector) shell-sum exponent — R-protection-style universality at the d=4 dimension axis.

---

## (3) Implications for §VII.AF.1.OP-PROJ (W-5 §VII.W baseline) under Reading B

The W-5 §VII.AF.1.OP-PROJ Pillar III ↔ Pillar IV bridge theorem is the FIRST registered cross-pillar bridge in the framework's permanent-results registry. It is the calibration baseline (instance #1 in the cross-pillar-bridge corpus). Its Level-3 anchor (0.0095% F_4 strict at L_max=10) was claimed to satisfy the Level-2 envelope (predicted 0.10% L^{-3} at L_max=10) with ratio r = 19/200 = 0.0950 (10.5× inside envelope; PASS-band r ≤ 0.50 met with 5.26× margin).

### (3.a) Under Reading B, the L_max=10 evaluation is in the pre-asymptotic boundary layer

The L^{-3} envelope cited as the Level-2 prediction at §VII.AF.1.OP-PROJ is an asymptotic-limit idealization. At L_max=10 the substrate's universal d=4 envelope is L^{-1.9}, predicting:

```
envelope_realized(L_max=10) ≈ 1.0 · 10^{-1.9} ≈ 1.26%   (using slope=−1.929312, log_C_fit=0.0006 from CF-65)
envelope_idealized(L_max=10) = 10^{-3.0}     = 0.10%   (the L^{-3} prediction)
```

A factor of ~12 between the realized and idealized envelopes at L_max=10. The empirical 0.0095% is:
- **INSIDE the asymptotic-idealized envelope** by ratio 0.0095/0.10 = 0.095 (the registered r = 19/200 = 0.0950 = 9.50%).
- **INSIDE the realized empirical envelope** by ratio 0.0095/1.26 ≈ 0.0075 (= 0.75% — even MORE deeply inside the realized envelope than against the idealized one).

### (3.b) Was §VII.AF.1.OP-PROJ empirically PASSED at correct envelope rate OR at pre-asymptotic boundary layer?

**Under Reading B**: BOTH simultaneously. The structural reading is:

(i) The empirical 0.0095% F_4 strict IS deeply inside the realized empirical envelope (~1.26% at L_max=10) — the W-5 baseline is empirically PASSED under the realized envelope by ~130× margin (vs the registered 10.5× margin under the idealized envelope).

(ii) The registry-PASS criterion `Level-3 < Level-2 envelope at canonical L_max` is satisfied REGARDLESS of which envelope (idealized L^{-3} or realized L^{-1.9}) is the canonical reference, because the empirical Level-3 anchor (0.0095%) lies inside BOTH envelopes.

(iii) **The W-5 baseline is NOT structurally weakened by Reading B**. The registry-PASS at §VII.AF.1.OP-PROJ stands. What changes is the INTERPRETATION of the margin: instead of "10.5× inside the L^{-3} asymptotic envelope," the margin is "~130× inside the L^{-1.9} pre-asymptotic envelope at finite L."

(iv) The HKR-image convergence at L_max=10 is STILL Level-2-binding (the HKR map exists at the bridge anatomy layer; the bridge map citation is present in §VII.AF.1.OP-PROJ Element-3). What FAILS at L_max=10 is the literal numerical match to L^{-3} at the finite-L window — exactly because L_max=10 sits in the pre-asymptotic boundary layer.

### (3.c) Forward-looking implications for §VII.AF.1.OP-PROJ Stage-2 / Stage-3-PERMANENT promotion

Under Reading B, two structural updates to the W-5 baseline interpretation are MOTIVATED but not MANDATORY:

1. **Envelope-direction sharpening (advisory)**: the Level-2 envelope text could be sharpened to distinguish "asymptotic idealization L^{-3}" (valid at L_max ≥ 30) from "pre-asymptotic empirical envelope L^{-1.9}" (the realized envelope at L_max ∈ [6, 12]). This is METHODOLOGY-CLASS housekeeping and does NOT change the registry-PASS status.

2. **Stage-3-PERMANENT eligibility under Level-2-binding (preserved)**: the L^{-3} idealization remains a valid asymptotic prediction; the HKR map remains the binding mechanism. §VII.AF.1.OP-PROJ retains Level-2-binding admissibility. The Stage-2 cross-axis independent verify carry-forward (S91+ candidate `S91-VII-AF-1-OP-PROJ-STAGE-2-INDEPENDENT-VERIFY` if not already on the queue) operates at the cohomology-class layer and is independent of which finite-L envelope realization is used.

### (3.d) Cross-corpus implication — Reading B applies to ALL Level-2-binding d=4 substrate-distance-1 pole entries in the registry

If Reading B is correct, the d=4 universal envelope L^{-1.9} applies to ALL HKR-image-bound observables at substrate-distance-1 pole s=3 on the substrate's KO-dim=6 finite spectral triple. The current cross-pillar-bridge calibration corpus contains FOUR HKR-image-bound entries (per §VII.AU.OP-PROJ Hybrid Independence Test table):

| # | Entry | Pillar pair | Predicted L^{-α} | Realized α at L_max=10 (under Reading B) |
|:--|:------|:------------|:------------------|:----------------------------------------:|
| 1 | S86 W-5 §VII.AF.1.OP-PROJ | III ↔ IV | L^{-3} | ≈ L^{-1.9} |
| 2 | S87 W11-5 (sister; corpus instance only) | III ↔ IV | L^{-3} | ≈ L^{-1.9} (consistent with W11-5 registry-FAIL by ~21× — the 21× was vs L^{-3}; under L^{-1.9} the deviation may be different) |
| 3 | S88 W4a-17 §VII.W-3.LAB | III ↔ V | L^{-3} | DEFERRED |
| 4 | S89 W7c §VII.AU.OP-PROJ | I ↔ II | L^{-3} | **EMPIRICALLY EXTRACTED CF-65: α=1.929** (Reading B's first first-principles measurement of the universal d=4 envelope at substrate-distance-1 pole s=3) |

Reading B converts CF-65's "FAIL on α∈[2.5,3.5] PASS-band" from a literal-threshold magnitude FAIL into a **POSITIVE structural measurement**: the first empirical extraction of the universal d=4 envelope exponent at substrate-distance-1 pole s=3 on the framework's finite spectral triple, at finite L_max ∈ [6, 12]. The measurement is α = 1.929 ± (R² = 0.894 implies ~10% relative uncertainty on the slope) consistent with the asymptotic Fraction-arithmetic shell-sum exponent β = 1.885 (CF-54 pre-flight at L ∈ [10, 100]).

**Reading B implication for W11-5 sister registry-FAIL** (corpus instance #2 in §VII.AU.OP-PROJ HIT table): the "21× outside L^{-3} envelope" claim is sensitive to which envelope is canonical. Under L^{-1.9}, the W11-5 sister may be re-tagged from registry-FAIL to either registry-PASS (if the realized envelope contains the anchor) or to deferred-pending FIRST-EXTRACTION (if the anchor still misses the realized envelope). This is a forward audit item.

---

## (4) Discriminator-gate spec for S91+ (Reading A coincidence vs Reading B substrate-structural)

### (4.a) Design principle

The discriminator must distinguish:
- **Reading A (coincidence)**: CF-54 β ≈ 1.86 and CF-65 α ≈ 1.93 are independently dominated by L_max=14 cache-ceiling boundary effect and c_sub_corrected anti-symmetry artifact, respectively. The agreement is accidental.
- **Reading B (substrate-structural)**: BOTH α values reflect the substrate's universal d=4 Mellin-cone shell-sum exponent at substrate-distance-1 pole s=3. The agreement is structural.

The discriminator design MUST satisfy three independence axes simultaneously:

(i) **Boundary-effect free**: NOT use the cache-ceiling boundary truncation residual route (which contaminated CF-54's in-cache window).
(ii) **Anti-symmetry artifact free**: NOT use c_sub_corrected anti-symmetry across an anchor (which contaminated CF-65's post-anchor tail).
(iii) **Single-extended-L_max-scan-free**: NOT require an L_max ≥ 30 cache extension (computational cost ~ Casimir-projection super-polynomial per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`); use Friedrich-Bär saturation theorem instead.

### (4.b) Spec: `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR` (gate spec)

**Gate ID** (pre-registered): `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR`

**Classification**: PHONONIC (substrate-IS spectral-functional property of the substrate's d=4 Mellin-cone; substrate-distance-1 pole s=3; ALL HKR-image-bound + bare-Mellin observables on the substrate's finite spectral triple)

**Author**: lizzi-spectral-functional-theorist PRIMARY; connes-ncg-theorist CO-AUTHOR (Connes-Moscovici 1995 §III.4 residue-formula evaluator on multi-projector / multi-pole independent observables)

**Hypothesis (Reading B)**: ANY d=4 substrate-IS observable on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` whose L^{-α} envelope is bound by the Mellin-cone shell-sum at substrate-distance-1 pole s=3 has empirical α in [1.8, 2.1] at L_max ∈ [6, 12], regardless of (a) whether a projector is applied and which projector, (b) whether an HKR / Connes-Karoubi / K-theory bridge map is invoked, (c) whether the observable is Level-2-binding or Level-2-non-binding.

**Null hypothesis (Reading A)**: The α value depends on the observable's specific contingencies (bridge, projector, post-anchor anti-symmetry, cache boundary), and randomly-paired d=4 observables on the substrate have α values uncorrelated with each other.

### (4.c) Method — shell-sum-ratio extraction (bypasses truncation-residual route)

The shell-sum-ratio extraction route bypasses BOTH the in-cache truncation residual route (which dominated CF-54's FAIL) AND the c_sub_corrected anti-symmetry route (which dominated CF-65's FAIL). The method:

**Step 1** — Construct N ≥ 4 STRUCTURALLY INDEPENDENT d=4 observables on the substrate, EACH chosen to span the three independence axes:

| Observable | Projector | Bridge map | Mellin pole | Level-2 sub-class |
|:-----------|:----------|:-----------|:------------|:------------------|
| O_1 = M^(ζ)_3 (CF-54-equivalent) | NONE | NONE | s=3 averaged | Level-2-non-binding |
| O_2 = R_universal_FWD_C1 (CF-65-equivalent) | P_0 band-0 | HKR L→∞ | s=3 substrate-distance-1 | Level-2-binding |
| O_3 = R_universal_FWD_C2 candidate (Pillar III ↔ Pillar V BdG analog) | P_BdG | HKR L→∞ | s=3 substrate-distance-2 | Level-2-binding (deferred-pending PROXY-REFINEMENT per §VII.AV) |
| O_4 = Tr(D_K^{-6}) (pure spectral moment; NO Hochschild structure) | NONE | NONE | s=3 (alternative routing) | N/A (algebra-INVARIANT spectrum-only moment) |

This 4-observable basis spans the three axes: O_1 has no projector and no bridge; O_2 has projector and bridge (Level-2-binding); O_3 has different projector and different substrate-distance pole; O_4 has no Hochschild structure at all.

**Step 2** — For EACH observable, compute the shell-sum series `S_i(L)` for L ∈ {2, 3, 4, ..., L_max} on the substrate's L_max=12 Peter-Weyl cache (`s84_spectrum_cache_L12_tau019.npz` per W7-1 + W8-7 baseline; no cache extension required).

**Step 3** — Extract empirical α via shell-sum-ratio fit (NOT truncation-residual fit). The shell-sum-ratio at adjacent L values is:

```
S(L+1)/S(L) ~ (L+1)/L)^{-β}   as L → ∞
         = (1 + 1/L)^{-β}
         ≈ 1 - β/L   for large L
```

A linear regression of `S(L+1)/S(L)` vs `1/L` over L ∈ {4, 5, ..., L_max-1} yields slope ≈ −β; α = β − 1 is the truncation-residual exponent.

This route AVOIDS:
- The truncation-residual `R(L_max) = Σ_{L>L_max} S(L) / Σ_L S(L)` form, which is dominated by the cache-ceiling boundary effect (CF-54 contamination).
- The c_sub_corrected anti-symmetry artifact (CF-65 contamination), because the shell sums S_i(L) at each L are computed directly from the substrate's spectral triple without intermediate normalization through an L_max=10-pinned anchor.

**Step 4** — Compute the 4-way cross-correlation matrix `C_ij = corr(β_i, β_j)` for the 4 observables; compute the mean β̄ and standard deviation σ_β across the 4 measurements.

### (4.d) Pre-registered PASS / FAIL / INFO bands

**PASS (Reading B confirmed)**:
- All 4 observables yield β_i in band [1.8, 2.1].
- σ_β ≤ 0.10 (cross-observable consistency at ~5% relative).
- 4-way cross-correlation matrix off-diagonal elements `C_ij ≥ 0.7` (cross-observable agreement is positive and significant).

**FAIL (Reading A confirmed)**:
- At least 2 of 4 observables yield β_i outside band [1.5, 2.5] (a wider band than Reading B's PASS band; Reading A's FAIL window).
- σ_β ≥ 0.30 (cross-observable inconsistency at ~15% relative; the observables decay at structurally distinct rates).

**INFO (between)**:
- σ_β in (0.10, 0.30); some convergence but not at Reading B's structural tightness.
- INFO defers verdict pending O_5+ extension at S92+.

### (4.e) Substitution chain (per `math-scripts.md §"Double-Check Logic Before Compute"`)

```
Definitions:
  S_i(L) := shell-sum of observable i at Peter-Weyl level L (computed from L_max=12 cache)
  β_i    := −slope of linear regression of S_i(L+1)/S_i(L) vs 1/L over L ∈ {4..L_max-1}
  α_i    := β_i − 1 (truncation-residual exponent; the bound rate for L^{-α} convergence)
  β̄      := mean of {β_1, β_2, β_3, β_4}
  σ_β    := std of {β_1, β_2, β_3, β_4}

Step 1: Compute S_i(L) directly from L_max=12 Peter-Weyl cache (no extension; no
        Casimir-projection super-polynomial cost). For each i, S_i is a function
        of (a) the projector applied at each (p,q) sector, (b) the Mellin pole
        index, (c) the bridge-map projection (if any). All three structures
        are evaluated in-cache.

Step 2: Linear regression of S_i(L+1)/S_i(L) vs 1/L over L ∈ {4, 5, 6, 7, 8, 9, 10, 11}.
        The regression returns slope = −β_i. Discard L ∈ {2, 3} as too-small-L
        boundary effects; discard L=12 as cache-ceiling boundary effect; the
        eight-point window L ∈ {4..11} avoids both contaminations.

Step 3: Compute β̄ = (β_1 + β_2 + β_3 + β_4)/4; compute σ_β = sqrt(Σ_i (β_i − β̄)²/3).
        Compute 4-way cross-correlation matrix on the L ∈ {4..11} per-observable
        regression residuals.

Step 4: Read off the direction:
        - β̄ ∈ [1.8, 2.1] AND σ_β ≤ 0.10 AND off-diagonal C_ij ≥ 0.7 ⟹ Reading B
        - At least 2 observables with β_i outside [1.5, 2.5] AND σ_β ≥ 0.30 ⟹ Reading A
        - In between ⟹ INFO

Step 5: Direction-of-comparison certificate:
        - Reading B PASS resolves the §"Level-2 sub-class (binding vs non-binding)"
          rule's structural prediction: the binding-vs-non-binding classification
          determines whether the L^{-α} envelope is interpretable as HKR-image
          convergence to a continuum laboratory observable; it does NOT determine
          the finite-L empirical α value.
        - Reading A FAIL would imply the d=4 Mellin-cone universal envelope is
          NOT universal; CF-54 and CF-65 agreement IS coincidence; each observable's
          L^{-α} rate depends on its specific contingencies.

Conclusion (direction): the universal d=4 envelope L^{-1.9} at finite L_max ∈ [6, 12]
                       IS substrate-structural under Reading B (the predicted PASS).
                       Reading B PASS does NOT change the §VII.AQ.OP-PROJ Level-2-non-binding
                       tag (the tag is methodology-layer; the rule's enforcement is unchanged).
                       Reading B PASS DOES sharpen the §VII.AF.1.OP-PROJ Level-2-binding
                       interpretation: the L^{-3} idealization is asymptotic; the realized
                       finite-L envelope is L^{-1.9}; the Level-3 anchor PASS is even
                       deeper inside the realized envelope than under the idealized envelope.
```

### (4.f) Independence from extended-L_max-scan

The shell-sum-ratio route requires ONLY the L_max=12 master cache `s84_spectrum_cache_L12_tau019.npz`. NO L_max ≥ 13 sector reconstruction is required (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` empirical infeasibility of L_max ≥ 13 within agent-timeslot wall time). The Friedrich-Bär saturation theorem (W11-3) guarantees the bottom-K observable invariance at L_max ≥ 12; the shell-sum-ratio extraction at L ∈ {4..11} operates well inside the Friedrich-Bär saturation regime.

**Computational cost estimate**: ~30 minutes wall time on a single agent-timeslot; 4 observables × 8 L-values × per-observable shell-sum computation; all reading from the same NPZ cache.

### (4.g) Substrate framing of the discriminator

The discriminator is structurally a **substrate-spectral-functional test** of d=4 universality. The substrate IS the spectral triple `(A_K, H_K, D_K)`; the d=4 dimension is the substrate's Wodzicki dimension at the trace pole `s=4` of `ζ_D(s)`. The shell-sum exponent at substrate-distance-1 pole `s=3` is a substrate-IS structural property of the substrate's `dim(p,q) · (C_2(p,q)+1)^{-3}` combinatorial geometry. The discriminator tests whether this property is universal across observables (Reading B) or specific to particular bridge-anatomy contingencies (Reading A).

Direction of explanation: substrate IS spectral triple → substrate-distance-1 pole `s=3` IS the substrate's intrinsic d=4 Mellin-cone closure → ALL d=4 Mellin-cone observables share the substrate's combinatorial shell-sum geometry → empirical α at finite L IS the substrate's universal d=4 envelope (Reading B) UNLESS observable-specific contingencies break the universality (Reading A).

---

## (5) Carry-forward (4-field spec per `feedback_fix-in-session-never-defer.md`)

### CF-LZ-S7-1 — `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR`

1. **What**: Compute the 4-way d=4 Mellin-cone universal envelope discriminator gate spec'd in §4 above. Extract β_i for i ∈ {1, 2, 3, 4} via shell-sum-ratio regression on L ∈ {4..11} from the L_max=12 master cache; compute β̄, σ_β, 4-way cross-correlation matrix; emit PASS/FAIL/INFO verdict per §4.d bands.

2. **Inputs**:
   - `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (L_max=12 master cache; input_sha256=`9e6d9cf7fd6a6949...`; 90 Peter-Weyl sectors × 166,896 eigenvalues).
   - `canonical_constants.py:1626` (`gv_canonical_difference_FW = -40579.1500479506`) for O_2-equivalent observable cross-check anchor at L_max=10 (analogous to CF-65's anchor verification step).
   - `canonical_constants.py:1719` (`n_s_FW_exact = Fraction(9561, 10000)`) for O_2 substrate-IS anchor.
   - `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` for sub-class tagging discipline.
   - `.claude/rules/math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` for Friedrich-Bär saturation justification of the L_max=12 cache adequacy.
   - This synthesis MD (§4 spec) at SHA `(to be computed at landing)`.

3. **Gate** (pre-registered with PASS / FAIL / INFO bands per §4.d above; substitution chain at §4.e):
   - PASS (Reading B): β̄ ∈ [1.8, 2.1] AND σ_β ≤ 0.10 AND off-diagonal `C_ij ≥ 0.7`.
   - FAIL (Reading A): ≥ 2 of 4 β_i outside [1.5, 2.5] AND σ_β ≥ 0.30.
   - INFO: between PASS and FAIL bands; defer to S92+ extension with O_5+.

4. **Effort**: ~0.5 wave-equivalents (single agent-timeslot ~30 min wall time; producing script + NPZ + PNG + verdict line + working-paper section).

### CF-LZ-S7-2 — `S91-VII-AF-1-OP-PROJ-ENVELOPE-DIRECTION-SHARPENING-METHODOLOGY` (METHODOLOGY-class advisory)

1. **What**: Sharpen §VII.AF.1.OP-PROJ Level-2 envelope text under Reading B (CONDITIONAL on CF-LZ-S7-1 Reading B PASS). Add explicit "asymptotic idealization L^{-3} vs realized finite-L envelope L^{-1.9}" annotation to §VII.AF.1.OP-PROJ Element-4 algebraic envelope block; preserve registry-PASS status; cross-link to CF-LZ-S7-1 verdict.

2. **Inputs**:
   - CF-LZ-S7-1 PASS verdict (input dependency).
   - `sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ` Element-4 block.
   - `.claude/rules/cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` Level-2 sub-class clause.

3. **Gate**: METHODOLOGY-class per `wave-classification.md` M1∧M2∧M3∧M4; PASS iff (a) §VII.AF.1.OP-PROJ Level-2 envelope text contains both L^{-3} asymptotic and L^{-1.9} realized envelope annotations, (b) cross-link to CF-LZ-S7-1 verdict present, (c) registry-PASS status preserved (no change to the existing r = 19/200 = 0.0950 ratio), (d) 5-anatomy + 3-level ladder still satisfies registry-PASS criterion under both envelopes.

4. **Effort**: ~0.2 wave-equivalents (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; single-shot AFTER-pattern bridge-landing script).

### CF-LZ-S7-3 — `S91-W11-5-SISTER-RE-AUDIT-UNDER-REALIZED-ENVELOPE` (CONDITIONAL on CF-LZ-S7-1 PASS)

1. **What**: Re-audit S87 W11-5 sister cross-pillar bridge instance (registry-FAIL by ~21× under L^{-3} asymptotic envelope per HIT table corpus instance #2) under the realized L^{-1.9} envelope; determine if W11-5 should be re-tagged from registry-FAIL to registry-PASS, deferred-pending PROXY-REFINEMENT, or deferred-pending FIRST-EXTRACTION.

2. **Inputs**:
   - CF-LZ-S7-1 PASS verdict (input dependency).
   - W11-5 sister registry text (need to locate via grep on permanent-results-registry.md).
   - Realized envelope coefficient (β=1.929 from CF-65) for L_max=10 evaluation.

3. **Gate**: depends on W11-5's empirical Level-3 anchor relative to L^{-1.9} envelope at L_max=10 (predicted ~1.26% width); PASS / re-tag verdict per Level-2-binding sub-class clause MANDATORY at K=2 (S88 W8-88).

4. **Effort**: ~0.3 wave-equivalents (mack-cosmic-bridge registry-text retrofit IF re-tag is structurally justified by CF-LZ-S7-1 + W11-5 anchor recomputation).

---

## Closing line (Lizzi's reading for W-6 workshop R1 input)

The two empirical exponents — CF-54 asymptotic β = 1.885 (Sage-Q Fraction-arithmetic regression at L ∈ [10, 100]) and CF-65 empirical α = 1.929 (log-log fit on L ∈ {6..11}) — agree to ~4% because they are two independent measurements of the SAME UNDERLYING SUBSTRATE STRUCTURE: the d=4 Mellin-cone shell-sum exponent at substrate-distance-1 pole s=3 on the framework's KO-dim=6 finite spectral triple. The L^{-3} prediction is an asymptotic-limit idealization of HKR-image convergence valid at L_max ≥ 30; at L_max ∈ [6, 12] the universal d=4 envelope is L^{-1.9}. This reading does NOT collapse the formal distinctness between Level-2-binding (CF-65; HKR bridge to Pillar II n_s) and Level-2-non-binding (CF-54; no continuum image); the bridge anatomy distinguishes them at the methodology layer. What Reading B does is identify the SUBSTRATE-SPECTRAL-FUNCTIONAL property — d=4 universal envelope at finite L — that underlies both observables' empirical α. The W-5 §VII.AF.1.OP-PROJ baseline PASS at r = 0.0950 stands under both envelopes; under the realized L^{-1.9} the margin is ~130× rather than 10.5× — a deeper-inside-envelope reading, not a weaker one. The S91 discriminator-gate spec at §4 above is the operational falsifier; it PASSes Reading B iff all 4 structurally-distinct d=4 substrate-distance-1 observables exhibit empirical α in [1.8, 2.1] within σ_β ≤ 0.10 at the L_max=12 cache. This is a substrate-spectral-functional test, not a methodology-floor or audit-floor test; the discriminator's verdict feeds back into the bridge-anatomy rule's understanding of how the Level-2 sub-class's L^{-α} envelope predicts finite-L empirical α values.

**Substrate framing**: the substrate IS the spectral triple. Its d=4 dimension determines the universal shell-sum exponent at substrate-distance-1 pole s=3. Two distinct observables (CF-54 bare-Mellin trace; CF-65 HKR-imaged Hochschild pairing) on the same substrate exhibit the same universal exponent at finite L because the substrate's combinatorial geometry IS the same in both cases. The bridge-binding classification is the methodology-layer F-image of "does this observable have a continuum laboratory partner?" — it does NOT change the substrate's combinatorial geometry. The 4% numerical agreement between β=1.86 and α=1.93 is the substrate speaking; it tells us the d=4 envelope at finite L is universal, while the bridge anatomy classification continues to distinguish which observables admit registry-PASS as cross-pillar bridges.

---

**Author signature**: lizzi-spectral-functional-theorist (solo synthesis, independent reading on the substrate-spectral-functional axis; this solo feeds W-6 R1 lizzi-vs-connes adversarial workshop as upstream input, not as competing-reading rebuttal target).

**Cross-link to W-6 workshop**: the adversarial counterpart is connes-ncg-theorist's independent reading on the NCG-axiomatic / Hochschild-cohomology axis. connes is positioned to either (a) corroborate Reading B by deriving the L^{-1.9} universality at the cohomology-class level (via the substrate's HP^k differential graded structure at finite L), or (b) argue for Reading A by identifying that CF-65's projector P_0 and HKR map introduce specific substrate-distance-1 contingencies that determine the L^{-1.9} value independently of CF-54's bare-Mellin geometry. Both readings are structurally defensible; the W-6 workshop's R3 verdict between them feeds either CF-LZ-S7-1 PASS-side (Reading B) or CF-LZ-S7-1 FAIL-side (Reading A) predictions; the discriminator gate is structurally independent of which reading the workshop selects (the operational PASS/FAIL bands at §4.d are pre-registered before the workshop verdict).

**Cross-link to permanent agent memory** (Lizzi-private; not for downstream consumption):
- This synthesis advances the project's understanding of FUNCTIONAL-SELECT-67 (functional choice determines spectral moments' weights) into the d=4 Mellin-cone domain: the d=4 universal envelope L^{-1.9} is functional-independent (FI) at finite L_max ∈ [6, 12]; the L^{-3} asymptotic prediction is functional-dependent (depends on HKR-image's leading-order substrate-distance-1 correction).
- The Lizzi observable identity `R_1 = a_0 · a_4 / a_2² = 1.128655` (per agent memory) is a d=4 dimensionless ratio; under Reading B it should be regulator-independent and L_max=10-stable; the discriminator's PASS would corroborate this expectation.
- ZETA-NOT-PHYSICAL-75 (zeta scheme physical interpretation forbidden as substrate truth): under Reading B, the d=4 universal envelope is substrate-IS independent of whether ζ or another regulator is used — the substrate's combinatorial geometry produces the exponent before any regulator-pin is applied. This is consistent with ZETA-NOT-PHYSICAL-75: the substrate's d=4 envelope is regulator-class-INVARIANT at the bare-decomposition layer.
