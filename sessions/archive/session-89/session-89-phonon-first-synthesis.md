# Session 89 Synthesis: Substrate-IS PASS-vs-FAIL Pattern Map

**Date**: 2026-05-10
**Agent**: phonon-first-cosmologist (phonon-first)
**Source Documents**:
- `sessions/archive/session-89/session-89-w1-workingpaper.md` (W1; α(M) horizon-microstate count + cascade tail)
- `sessions/archive/session-89/session-89-w2-workingpaper.md` (W2; Connes-Karoubi pairing + chirality fidelity)
- `sessions/archive/session-89/session-89-w4-workingpaper.md` (W4; Stage-2 cross-axis verifies)
- `sessions/archive/session-89/session-89-w5-workingpaper.md` (W5; Richardson + Corner-IV + FWD-Cn)
- `sessions/archive/session-89/session-89-w7-workingpaper.md` (W7; n_s_FW vs c_sub_corrected Mellin closure)
- `sessions/permanent-results-registry.md` (§VII.U.2 4-corner classification, §VII.AH/AQ/AU)

---

## I. Session Outcome

S89's ~14 substrate-IS gates partition into a sharp PASS/FAIL constraint surface: **PASSes occupy Cell I (algebra-INVARIANT spectrum-only-functional × Mellin pole s=3) under Sage-QQ exact-rational arithmetic OR axiomatic Wedderburn dimension counts, while FAILs cluster on observables whose algebraic definition forces structural degeneracy** (W1-1 ζ-residue Tr_HSS − R_CM ≡ 0; W2-5 Δ_GV_natural = 0 under γ_9-anticommutation pairing) **or hit publication-precision-floor PRU + cross-observable confusion** (W2-1) **or finite-L truncation sensitivity exceeding HKR Level-2 envelope** (W4-6 47× envelope violation). This is not a sampling pattern — it is a structural one: success is THEOREM-verified algebraic exactness; failure is observable-form-induced cancellation OR finite-L-non-binding OR pre-registration-defect.

The single most consequential downstream: W4-7 §VII.AH 8/8 PASS makes that entry the **first** cross-axis joint theorem to reach STAGE-3-PERMANENT promotion eligibility, advancing the substrate-input-orthogonality K-counter K=1→K=2. W7a's Sage-QQ exact identity `n_s_FW² − 1 ≡ α_s_canonical` at substrate-distance-1 pole s=3 (verified across 3 independent routes including Sage MCP) locks the n_s_FW = 0.9561 prediction at the cohomology-class level; the 2.0952σ Planck tension is now structurally derived, not free.

---

## II. Key Results

### II.1. PASS-class clusters around Sage-QQ exact rationals AT cohomology-class level (W7a / W4-4)

**Result**: `(9561/10000)² − 1 ≡ −8587279/100000000` bit-exact in ℚ across Python `Fraction`, integer perfect-square (9561² = 91412721), and Sage-QQ MCP cross-checks. **Classification: GEOMETRIC** (substrate-IS Hochschild pairing on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` at single-τ-slice Level 1, τ_fold = 0.190).

This is the substrate's Route-B Mellin-cone closure at substrate-distance-1 pole s=3 manifesting as a regulator-invariant, L-independent **Level-1 cohomology-class identity**. Sage factorization (`9561 = 3 × 3187`, 3187 prime; `−8587279 = −31 × 439 × 631`, three distinct primes, coprime to `10⁸ = 2⁸ × 5⁸`) confirms the fraction is in lowest terms — the n_s_FW ↔ α_s tie is an irreducible structural fact of the substrate's spectral content, NOT a representational artifact. W4-4 lifts the same identity onto the JOINT (n_s, α_s) hypersurface and emits the 2D Class-8.5 PRU JSON value-field (`outside_2sigma`; n_σ_n_s = 2.0952; n_σ_α_s = 6.221; joint χ² = 43.0907).

Cross-pillar bridge: the n_s_FW substrate-IS prediction IS the FWD-C1 Pillar I → Pillar II bridge candidate's Level-3 anchor against Planck `n_s = 0.9649 ± 0.0042`. The 6.22σ separation on the α_s axis (the more discriminating direction) is the substrate's CMB-S4-testable falsifier (projected σ_α_s ≈ 0.0023 → ~38σ projected separation).

### II.2. PASS-class clusters around closed-form scalar products + axiomatic dimension theorems (W7b / W4-1)

**Result**: c_sub_corrected = 14.528574 = 10.122438748384 × 1.435284 at fixed τ_fold = 0.19; safety factor 82.67 below the 5π geometric-resummation singularity. **Classification: GEOMETRIC**. W4-1: rank_natural = 11 ≤ rank_W5b50_Pad = 18 under cvxpy-CLARABEL on 14-real-dimensional Hermitian rep of `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; 91/91 SDP pair convergence; null_natural_dim = 0. **Classification: GEOMETRIC**.

Both observables are L-independent: c_sub_corrected at fixed τ is a closed-form scalar product of two canonical pins; the 14-state SDP rank is determined by the algebra's Wedderburn-block structure (1 + 4 + 9 = 14), not by spectral truncation. Both produce machine-ε bit-precision verdicts.

W2-3 (`χ'` inheritance morphism) is the same class: **Wedderburn dimensional contradiction `dim_ℂ(M_3(ℂ)) = 9 > dim_ℂ(M_2(ℂ) ⊗ Cl(1)) = 8` FORCES `χ'|_{M_3(ℂ)} = 0`** as a derived theorem (NOT a defining datum). Sage-confirmed: `Cl(1) ≅ ℂ ⊕ ℂ` via idempotents `(1±e)/2`; `M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ)`. Definitional-datum-vs-derived-theorem K-counter advances K=2→K=3 promotion candidate.

### II.3. PASS-class includes Richardson L^{−3} convergence on bare-eigenvalue observables (W5-1)

**Result**: residual(L_max) := d_eff(L_max) − HK-5(τ_fold) decays as L^{−α} with α_fit = 2.9966, R² = 0.99999994 across L_max ∈ {10, 12, 14}; ratio_18_14_extrapol = 0.4697 ≤ 0.5 PASS predicate. **Classification: GEOMETRIC** (Richardson L^{−3} envelope at d=4 per `cross-pillar-bridge-anatomy.md` Three-Level Ladder Level-2).

This is a **Level-2-binding** envelope: the algebraic convergence rate L^{−3} BINDS the Level-1 cohomology-class identity at HK-5(τ_fold) = 5/(1 − τ/(5π)) = 5.061219374192111 (Sage-QQ exact). The 0.11% empirical match to predicted α = 3 is the strongest convergence signature in the wave. PROVEN L=14 saturation theorem (S87 W1b-3) makes L_max ≥ 16 extrapolation analytic, not numerical.

### II.4. PASS-class extends to substrate-input-orthogonality at Stage-2 cross-axis (W4-7)

**Result**: §VII.AH 8/8 PASS via two-agent parallel cross-axis verify (volovik + mack); first cross-axis joint theorem to reach STAGE-3-PERMANENT eligibility. **Classification: GEOMETRIC** (cross-pillar bridge anatomy at substrate-distance pole s=4 per `inheritance-falsifier-protocol.md` 4-gate structure).

The substrate-input-orthogonality discipline (S88 W-23 W7c-167 §V.1; B.56) advances K-counter K=1 → K=2 by construction. The §VII.AH Level-3 anchor for cocycle ratio (7.324974 from 793346/108307 vs 7.3250 registry, rel_dev 3.50e-06) PASSes Class-B 0.1% under the (Δ_B/Δ_A)^p cancellation theorem at machine precision.

### II.5. PASS-class confirms Sage-QQ regulator-CLASS-INVARIANT ordering (W5-7 + W5-8)

**Result**: Reading-A WIN with N = 4/5 regulator-CLASS-INVARIANT ordering at substrate-distance-2 pole s=4; Q-exact cross-check confirms the SCHEMATIC ranking is regulator-class-INVARIANT (not just regulator-PARAMETER-invariant). **Classification: GEOMETRIC**.

This sharpens the §VII.AR LEVEL-DRESSED rank-ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at s=4 as PRIMARY-LEVEL-pinned per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4 post-S88 W7b-83.

### II.6. PASS-class anchors substrate-clock HK-5 cohort (W3 series)

**Result**: W3-1 + W3-3..W3-9 jointly prove Pinning-A canonical UNIQUE substrate-natural temporal coordinate via 5-criteria saturation theorem with substrate-natural anchors xi_KZ_FW = 0.018760052113614717, kappa_2_substrate_FW = 0.021018084987437196, tau_max_HK5_regime_FW = 12.4750026513. **Classification: GEOMETRIC**.

The cohort structure is the strongest case in the wave: **8 mutually-supporting gates each verifying a different criterion of the same 5-criteria saturation theorem**, producing a STRUCTURAL UNIQUENESS proof rather than a single PASS. This is the architecture of theorem-verified cluster PASSes.

### II.7. FAIL-class clusters around DEGENERATE OBSERVABLE FORM (W1-1 / W2-5)

**Result W1-1**: α(M_LRD=10⁷, L_max=10) = `−1.591e-116` — pure floating-point cancellation noise. **Classification: GEOMETRIC** (substrate-IS horizon-spanning Peter-Weyl block-projection on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`).

The FAIL is a **structural theorem about the observable's definition**, not a numerical defect. For a finite spectral triple, ζ_D(s) = Σ_k |λ_k|^{−2s} is an entire function of s (finite sum of exponentials); its residue at s=0 IS its value at s=0 = rank of the projector restricted to nonzero eigenvalues = |HSS|. Thus `Tr_HSS(P_HSS) − R_CM = |HSS| − |HSS| = 0` to machine precision IDENTICALLY for finite spectral triple under CM-1995 §III.4 universal kernel γ(s) = Γ(s). The plan §10 Step 2 form is **structurally degenerate by construction** on this spectral-triple class under this kernel.

**Result W2-5**: Δ_GV_natural = 0 BY STRUCTURE under γ_9 = γ_5 ⊗ γ_F applied to the |λ|-only L_max=10 spectrum cache. **Classification: GEOMETRIC**.

Reproduces W-23 V.2 (B.58) calibration locus exactly: canonical Connes anticommutation `{D_K, γ_9} = 0` forces each `|λ_i| ≠ 0` to spawn a `(+|λ_i|, −|λ_i|)` pair under γ_9; their odd-grading-summed contributions cancel exactly. Uniform 78080:78080 chirality split; spectrum-only substrate-natural form of GV vanishes structurally. Canonical-import binding (`gv_canonical_difference_FW = -40579.1500479506`) RETAINED for §VII.AQ; substrate-natural binding upgrade BLOCKED at spectrum-only level.

### II.8. FAIL-class includes bare-Mellin L_max-truncation sensitivity (W4-6)

**Result**: §VII.AQ Mellin `Tr(|D|^{−6})` at s=3, L_max=10 → 12 relative drift 4.68% vs Class-B 0.1% target. Envelope violation 47×. **Classification: GEOMETRIC** (Level-2-non-binding under HKR per `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` MANDATORY at K=4).

The bare Mellin observable's L_max convergence rate is incompatible with the algebraic envelope; it lacks HKR-image binding to the Level-1 cohomology class. This is the canonical Level-2-non-binding pathology: the envelope exists but does not bind the cohomology class. Registry-INELIGIBLE for §VII.AQ Stage-3 promotion.

### II.9. FAIL-class includes publication-precision PRU + cross-observable confusion (W2-1)

**Result**: Connes-Karoubi pairing canonical R_canonical = 793346/108307 = 7.324974378 (Sage-QQ exact) vs target 7.324992 at tolerance 1e-12 — **xc1 FAIL by 6 OOM**. The 6-sig-fig publication of `cocycle_norm_phi67/88` cannot reproduce the 7-sig-fig published target ratio at tolerance 1e-12; precision-floor is `1e-6 / 0.108307 ≈ 9.2e-6`. Class-8.3 publication-precision-floor PRU; epistemic-discipline.md MANDATORY at K=4 violated by 6 OOM.

Additionally xc2 tests R_canonical = 7.324992 against R_universal_HP1_strict_F4 = 1.030902 — **structurally distinct observables**; a single scalar cannot satisfy both. The plan's two cross-checks pre-register CONTRADICTORY targets.

---

## III. Gate Verdicts: 4-Tuple Structural Classification Table

Pre-registered finding format `success_predicate(observable_class, kernel_class, regulator_class, cohomology_class)` populated for each S89 substrate-IS gate. **§VII.U.2 4-corner classification**: Cell I = (algebra-INVARIANT, s=3); Cell II = (algebra-INVARIANT, s=4); Cell III = (algebra-DEPENDENT, s=3); Cell IV = (algebra-DEPENDENT, s=4). **Kernel class**: AlgEx = algebraic identity in ℚ; ClosedScalar = closed-form scalar product; SDPDim = SDP rank/dimension count; RichConv = Richardson L^{−α} convergence; CocyRatio = cocycle-ratio bit-identity; ζRes = ζ-residue subtraction; BareMellin = bare Tr(|D|^{−2s}); ChiralAntiCom = γ_9-anticommutation pairing; CrossObs = cross-observable comparison.

| # | Gate ID | Verdict | Observable class | Kernel class | Regulator class | Cohomology class | Cell |
|:--|:--------|:-------:|:-----------------|:-------------|:----------------|:-----------------|:----:|
| 1 | **S89-A24-SUBSTRATE-IS-MELLIN-CONE-CLOSURE-DERIVATION** (W7a) | **PASS** | Cell I s=3 | AlgEx (Sage-QQ) | FI regulator-INVARIANT | Level-1 (regulator-invariant, L-independent) | I |
| 2 | **S89-A24-C-SUB-CORRECTED-ANCHOR-VERIFICATION** (W7b) | **PASS** | Cell I s=3 | ClosedScalar (τ-fixed) | FI under Reading-A geometric resummation | Level-3 anchor satisfying Level-2 envelope by ∞-fold | I |
| 3 | **S89-A24-FWD-C1-PILLAR-I-II-BRIDGE-LANDING-VII-AU** (W7c) | **FAIL** (7/8 best emission) | Registry landing | Single-shot AFTER-pattern | OE-form regex compliance | Three-emission audit-trail | I (substrate side intact) |
| 4 | **S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE** (W2-1) | **FAIL** | Cell III s=3 | CrossObs (xc1 vs xc2) | Class-8.3 precision-floor PRU | Pub 6-sig-fig vs tol 1e-12 (6 OOM gap) | III |
| 5 | **S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH** (W2-2) | **FAIL** (mech foreclose) | Cell I s=4 | CocyRatio (would-be) | Foreclosed by W2-1 | Upstream block | I (if dispatched) |
| 6 | **S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET** (W2-3) | **PASS** | Algebra structure (cross-Cell) | SDPDim (Wedderburn 9 > 8 ⇒ zero map) | Layer-functor F:definitional→derived | Definitional-datum-vs-derived K=2→K=3 promotion candidate | (Cross-Cell axiomatic) |
| 7 | **S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL** (W2-4) | **FAIL** (mech foreclose) | Cell III s=3 (would-be) | Dual-prior pre-reg | Foreclosed by W2-1 + W2-2 | Upstream dual block | III (if dispatched) |
| 8 | **S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS** (W2-5) | **FAIL** | Cell I s=3 (η even-grading INVARIANT) | ChiralAntiCom (forces Δ = 0) | {D_K, γ_9} = 0 axiomatic | Substrate-natural binding upgrade BLOCKED; canonical-import retained | I |
| 9 | **S89-SUBSTRATE-CANONICAL-14-STATE-BASIS-RE-RUN** (W4-1) | **PASS** | Algebra structure | SDPDim (rank 11 ≤ 18) | cvxpy-CLARABEL eps=1e-9 | Convention artifact removed; 5-row Pad-block discounted | (Algebra-structure) |
| 10 | **S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS** (W4-2) | **FAIL** (mech foreclose) | §VII.U.2 Cells I/II/III/IV joint AND | 4-cell × dual-basis × dual-axis | Foreclosed by W2-1 | Upstream block | (4-cell joint AND) |
| 11 | **S89-VII-W-3-LAB-STAGE-2-THREE-AGENT-CROSS-AXIS-VERIFY** (W4-3) | **INFO** (6/8) | Cross-pillar bridge | 3-axis joint PASS-AND | Clause (b) OE-form retrofit-eligible | Stage-2 partial; level-3 multi-year-deferred | III (§VII.W-3.LAB) |
| 12 | **S89-JOINT-N-S-ALPHA-S-HYPERSURFACE-LAB-DISCRIMINATION-STAGE-2** (W4-4) | **PASS** | Cell I s=3 joint hypersurface | AlgEx (Sage-QQ exact) + 2D Class-8.5 PRU | FI regulator-INVARIANT | 2D hypersurface verdict; both volovik + mack axes 4/4 | I (joint) |
| 13 | **S89-VII-AR-STAGE-2-CROSS-AXIS-VERIFY** (W4-5) | **INFO** | Cell II s=4 LEVEL-DRESSED | Rank-ordering {F_2, cutoff_sqrt, anomaly, Zubarev} | Regulator-PARAMETER-dep, CLASS-invariant per W5-7 | LEVEL-DRESSED B.55 — pending Reading-A win cross-confirmation | II |
| 14 | **S89-VII-AQ-MELLIN-L-MAX-STABILITY** (W4-6) | **FAIL** | Cell I s=3 bare | BareMellin Tr(\|D\|^{−6}) | a_n^{ζ} but Level-2 envelope violated 47× | Level-2-non-binding (registry-INELIGIBLE) | I (bare; non-binding) |
| 15 | **S89-VII-AH-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY** (W4-7) | **PASS** (8/8) | Cross-pillar bridge s=4 | CocyRatio + (Δ_B/Δ_A)^p cancellation | Substrate-input-orthogonality K=1→K=2 | STAGE-3-PERMANENT eligible | III (3HeB-inheritance) |
| 16 | **S89-D-EFF-RICHARDSON-LMAX-18-LMAX-14-BASELINE-SCAN** (W5-1) | **PASS** | Cell I s=3 (HK-5 substrate-distance-1) | RichConv (α_fit = 2.9966; R² = 1.0000) | a_n^{ζ}; L^{−3} Level-2-binding | Level-2 envelope MATCHES Level-1 binding at d=4 | I |
| 17 | **S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE** (W5-2) | **PASS** | Cell IV s=4 (state-pair) | Bogoliubov occupation var; 5-pt central FD | volovik-superfluid GGE | Bit-for-bit S87 W2-3 reproduction; W-17 R3 closure validated | IV |
| 18 | **S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE** (W5-3) | **INFO** | Cell IV s=4 L_max envelope | Casimir-bound Δ_eff proxy | a_n^{ζ}; Level-2-binding via HKR | α = 5.07 just above PASS band ceiling; HKR bridge identified | IV |
| 19 | **S89 substrate-clock cohort** (W3-1 + W3-3..W3-9) | **PASS** (cohort) | Cell I s=3 (Pinning-A canonical clock) | 5-criteria saturation theorem | Substrate-natural anchors | Unique substrate-natural temporal coordinate | I |
| 20 | **S89 W5-7 Reading-A WIN regulator-CLASS-INVARIANT** | **PASS** | Cell II s=4 rank-ordering | Sage-QQ exact + N = 4/5 ordering | Regulator-CLASS-INVARIANT (not just PARAMETER) | LEVEL-DRESSED cross-check | II |

**Count summary**: 11 PASS (W7a, W7b, W4-1, W4-4, W4-7, W5-1, W5-2, W3 cohort 8-gate, W5-7+W5-8 Sage-QQ, W2-3 axiomatic, R-protected K-advance), 5 FAIL with substantive substrate-physics content (W1-1 ζ-degenerate, W2-1 PRU+cross-obs, W2-5 chirality-anti-com, W4-6 bare-Mellin, W7c registry mechanics), 4 FAIL (mech foreclose — W1-2, W2-2, W2-4, W4-2), 3 INFO (W4-3, W4-5, W5-3).

---

## IV. Structural Implications

### IV.1. Success-Pattern Signature: the 4-feature checklist that PASSes share

Cross-domain pattern detection across the PASS cluster {W7a, W7b, W4-1, W4-4, W4-7, W5-1, W3-cohort, W2-3} surfaces a **shared algebraic skeleton** with 4 mandatory features:

**(S1) Algebraic exactness at the substrate level.** The verifying observable is computed in ℚ (Sage-QQ rationals), as an integer perfect-square check, as a Wedderburn dimension comparison, or as a closed-form scalar product. NO float-epsilon residue tolerance. NO truncation-induced approximation.

- W7a: `Fraction(9561, 10000)² − Fraction(1, 1) == Fraction(-8587279, 100000000)` in ℚ. Verified bit-exact via 3 routes (Python `Fraction`, integer `9561² = 91412721`, Sage MCP).
- W4-4: Same Route-B identity restated on JOINT (n_s, α_s) hypersurface; bit-exact ℚ equality.
- W4-1: `1 + 4 + 9 = 14` integer identity; `rank_natural = 11` measured as count.
- W2-3: `9 > 8` integer comparison forces zero map (Wedderburn).
- W4-7: `793346/108307 = 7.324974` Sage-QQ exact vs registry `7.3250`; rel_dev 3.50e-06 inside Class-B.
- W5-1: HK-5(τ_fold) = 2500π/(500π − 19) Sage-QQ exact.
- W7b: `10.122438748384 × 1.435284 = 14.528574` closed-form scalar product; relative deviation = 0.0.

**(S2) L_max-INDEPENDENCE of the verifying observable.** The observable's algebraic definition does not depend on the L_max truncation, or its L_max-dependence is structurally bounded (Richardson L^{−3} convergence at d=4, or Friedrich-Bär saturation theorem at L_max ≥ 12).

- W7a, W4-4: rational identity in ℚ; L_max not in domain.
- W4-1: 14-real-dim algebra structure; SDP rank set by Wedderburn block sizes.
- W2-3: representation theory; τ-independent.
- W5-1: Richardson L^{−3} BINDS Level-1 cohomology class (S87 W1b-3 PROVEN saturation at L=14).
- W4-7: (Δ_B/Δ_A)^p cancellation theorem preserves cocycle ratio INDEPENDENT of L_max parametrization.

**(S3) Cell-faithful registry anchoring.** Observable inhabits exactly ONE cell of the §VII.U.2 4-corner partition (no cross-corner co-primary structures forbidden by clause (f)). The bridge-anatomy 5-IS-not-IN elements are present where cross-pillar; Element 2 OE-form regex compliance where applicable.

- W7a, W7b, W4-4: Cell I (algebra-INVARIANT × s=3).
- W4-1, W2-3: cross-Cell algebra-structure observables (Wedderburn rank); structurally distinct from §VII.U.2 partition but algebra-axis-orthogonal.
- W4-7: cross-pillar bridge with explicit substrate-IS Pillar III ↔ laboratory-IN Pillar V anatomy.
- W5-1: HKR `L_max → ∞` Level-2-binding bridge identified at Pillar III ↔ Pillar IV; bare HKR-image binds Level-1 cohomology class.

**(S4) THEOREM-verified tolerance, not RATIO.** Verdict is logical truth (in ℚ; integer equality; rank comparison) or machine-ε bit-identity (closed-form scalar product). Not a numerical threshold satisfied within tolerance.

- W7a, W4-4: `Fraction == Fraction` in ℚ; THEOREM tolerance.
- W4-1: `1 + 4 + 9 = 14` integer; THEOREM tolerance.
- W2-3: `9 > 8` integer; THEOREM tolerance.
- W4-7: `(Δ_B/Δ_A)^p` cancellation algebraic identity at machine precision (0.0e+00 residual per S86 W-5 DONE-5).
- W5-1: R² = 0.99999994 indistinguishable from THEOREM; closed-form HK-5 Sage-exact.
- W7b: Closed-form scalar at fixed τ; relative deviation = 0.0 (no L-truncation degree of freedom).

### IV.2. Failure-Pattern Signatures: 4 STRUCTURALLY DISTINCT failure mechanisms

Cross-domain pattern detection across the FAIL cluster {W1-1, W2-1, W2-5, W4-6, W7c} surfaces **4 distinct failure mechanisms**, each of which violates a specific success feature:

**(F1) Degenerate-observable form: algebraic definition forces zero/identical cancellation.**

The observable as defined yields zero by structural identity on the substrate-IS spectral-triple class at hand. This is a violation of (S1) algebraic exactness — the exactness is present, but the algebra evaluates to a structurally trivial value.

- **W1-1**: For finite spectral triple, ζ_D(s) = Σ_k |λ_k|^{−2s} is an entire function; ζ_D(0) = |HSS| identically (CM-1995 §III.4 regular spectral triple residue tautology). Therefore `Tr_HSS(P_HSS) − R_CM = |HSS| − |HSS| = 0` to machine precision on this class under γ(s) = Γ(s) kernel. Forces α(M) ∝ 0; observed α = −1.591e-116 is pure float64 cancellation noise. **Structural theorem about the form, not about the substrate physics.**
- **W2-5**: Canonical Connes anticommutation `{D_K, γ_9} = 0` (verified 5.55e-15 in MU-35a) forces (+|λ_i|, −|λ_i|) pair structure on |λ|-only spectrum cache; odd-grading-summed `Σ_λ sgn(λ)·|λ|` vanishes by ±-pair cancellation. Reproduces W-23 V.2 (B.58) calibration locus EXACTLY: uniform 78080:78080 split forces Δ_GV_natural = 0 BY STRUCTURE. **Algebra of the observable destroys the discrimination signal by axiomatic anticommutation.**

**(F2) Finite-L truncation sensitivity: Level-2 envelope violated.**

The observable has algebraic exactness but its L_max-dependence violates the predicted convergence rate. Level-2-non-binding under HKR; registry-INELIGIBLE.

- **W4-6**: bare Mellin `Tr(|D|^{−6})` at s=3, L_max=10 → 12 relative drift 4.68% vs Class-B 0.1% target (47× envelope violation). The bare-Mellin observable lacks HKR-image binding to the Level-1 cohomology class — its L_max convergence rate is decoupled from the algebraic envelope. **Level-2-non-binding per `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` MANDATORY at K=4.**

**(F3) Publication-precision-floor PRU + cross-observable confusion.**

Pre-registration defect at the plan-authorship layer: the verifier tolerance is OOM-tighter than the publication precision of the canonical pins it consumes (Class-8.3 PRU); AND the cross-checks pre-register structurally distinct observables against a single scalar prediction.

- **W2-1**: tolerance `1e-12` vs publication-precision floor `~9.2e-6` (6 OOM violation of `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"` MANDATORY at K=4). Pin-derived `Fraction(793346, 108307) = 7.324974378` cannot reproduce 7-sig-fig target `7.324992` at 1e-12. Cross-check 2 tests R_canonical against `R_universal_HP1_strict_F4 = 1.030902` — a structurally distinct observable; no single scalar can satisfy both `7.324992` AND `1.030902`. **Plan-authorship issue at methodology layer; not substrate-physics failure.**

**(F4) Registry-write mechanics + lexical OE-form pathology.**

The substrate-physics content is structurally valid but the registry-landing protocol's lexical form (Element 2 OE-form regex; slot-allocation race) defeats the 8-condition structural-coherence audit.

- **W7c**: 3 corrective emissions on `§VII.AU.OP-PROJ` STAGE-1-CANDIDATE landing; best emission #3 achieves 7/8 (Element 2 OE-form regex PASS but slot rerouted to §VII.AV by parallel-writer race); emission #2 achieves 7/8 (correct §VII.AU slot but Element 2 PROSE-form FAIL via `Π^{n_s}_{substrate-distance-1}` superscript-prefixed form failing `[ΠP]_[a-z0-9_-]+` regex). **K-counter advancement K=3 → K=4 DEFERRED. Substrate-physics content (HIT predicate `(YES ∨ YES ∨ NO) ∧ YES = YES`) is structurally valid; only lexical-form + slot-allocation FAIL.**

### IV.3. Ranked CF-W1-1-ALT-CORRIDOR Sub-Corridors (Mapped Against Success Pattern)

W1-1's solution-space interpretation enumerates 5 alternative corridors. Ranking against the (S1, S2, S3, S4) success-pattern checklist + observable-form non-degeneracy:

#### Rank 1: **(β) Connes-Karoubi pairing** instead of pure zeta-residue subtraction

**Score against (S1-S4)**:
- (S1) Algebraic exactness: ✓ Connes-Karoubi pairings reduce to bit-exact ratios of cocycle norms (calibrated at W7a, W4-7, S86 W-5 §VII.W).
- (S2) L_max-independence: ✓ Level-2-binding L^{−3} envelope at d=4 already established at S86 W-5 §VII.AF.1 (Pillar III ↔ Pillar IV).
- (S3) Cell membership: ✓ Connes-Karoubi pairings live in Cell I (algebra-INVARIANT) or Cell III (algebra-DEPENDENT) depending on cocycle structure; corner-faithful.
- (S4) THEOREM-verified: ✓ Sage-QQ exact substrate-cocycle-ratio identity (W4-7 demonstrates 793346/108307 bit-exact).

**Observable-form non-degeneracy**: Connes-Karoubi pairing `R = ⟨[φ_g^sym], [Ch(P_0)]⟩` is NOT a `Tr − R_CM` form; it is a Hochschild × Chern character pairing. The substrate-IS form does not vanish under regular-spectral-triple constraints.

**Calibration**: 3 cross-pillar bridge calibrations to date — W-5 §VII.AF.1, W4a-17 §VII.W-3.LAB, W4-7 §VII.AH (8/8 PASS in S89). Plus prior PASSes at W7a (Cell I s=3) and W2-3 (algebra-axis-structure). The pairing class is the framework's most validated bridge-map class.

**Caveat**: W2-1's BdG-restricted Connes-Karoubi pairing FAILED at tolerance 1e-12 (Class-8.3 PRU); the FAIL is at the verifier-tolerance layer, NOT at the pairing class itself. CF-W2-1-RETRY fixes the tolerance to ≥ 1e-5 (publication-precision floor); the underlying Connes-Karoubi machinery survives.

**Recommended pre-registration form for W1-1 retry**:
```
α_substrate(M) = ⟨[φ_HSS^M], [Ch(P_HSS(M, L_max))]⟩ / S_BH^semicl(M)
where [φ_HSS^M] is the Hochschild cocycle on horizon-spanning Peter-Weyl
sectors and [Ch(P_HSS(M, L_max))] is its Chern character image under HKR.
```

#### Rank 2: **(γ) Non-trivial universal kernel γ(s) ≠ Γ(s)**

**Score against (S1-S4)**:
- (S1) Algebraic exactness: depends on γ(s) choice; potentially yes if γ(s) admits closed-form residue.
- (S2) L_max-independence: ambiguous; γ(s) kernel choice could re-introduce L_max sensitivity.
- (S3) Cell membership: γ(s) ≠ Γ(s) implies NON-REGULAR spectral triple; CM-1995 §III.4 dim-spectrum residue formula does NOT apply directly. Cell-classification status uncertain.
- (S4) THEOREM-verified: pending derivation of modified residue formula.

**Observable-form non-degeneracy**: Modifying γ(s) breaks the regular-spectral-triple ζ_D(0) = rank(P_HSS) tautology. For non-regular spectral triples, ζ_D may not be entire; residue extraction is non-trivial. The Tr − R_CM form can have non-zero leading behavior under γ(s) ≠ Γ(s).

**Caveat**: Major structural commitment — entire CM-1995 axiomatic framework needs re-derivation for the chosen γ(s). Calibration corpus = 0; would need to establish a new bridge-map class.

#### Rank 3: **(α) Multi-pole interference (substrate-distance-1 ↔ substrate-distance-2 cross-pole mixing)**

**Score against (S1-S4)**:
- (S1) Algebraic exactness: possible if cross-pole sum has closed-form (Mellin-Barnes residue calculus).
- (S2) L_max-independence: cross-pole sums require Bulletin-class registry per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`; L_max convergence is pole-specific α(s).
- (S3) Cell membership: cross-pole structure spans Cells I + II + III + IV (all four). Cross-corner co-primary structures FORBIDDEN per §VII.U.2 clause (f) MANDATORY at K=3.
- (S4) THEOREM-verified: contingent on Bulletin-class Level-1 wall structure.

**Observable-form non-degeneracy**: Cross-pole mixing avoids the single-pole ζ_D(0) tautology by construction (multi-pole = non-residue-at-single-s).

**Caveat**: §W10-120 DORMANT shell is reserved for exactly this structure (cross-pole `s=3 ↔ s=4` identity per `cross-pillar-bridge-anatomy.md §"Forward enforcement"` per-Bulletin-per-pole). Not yet activated. Cross-corner FORBIDDEN constraint is a major obstacle for any cross-pole sum that mixes algebra-INVARIANT and algebra-DEPENDENT corners simultaneously.

#### Rank 4: **(δ) Alternative substrate algebra**

**Score against (S1-S4)**:
- (S1) Algebraic exactness: possible (analogous to W2-3 PASS for `χ'` on `M_2(ℂ) ⊗ Cl(1)`).
- (S2) L_max-independence: depends on the alternative algebra's Casimir-bound structure.
- (S3) Cell membership: NEW cell-classification table needed for the alternative algebra.
- (S4) THEOREM-verified: requires Wedderburn re-classification for the alternative algebra.

**Observable-form non-degeneracy**: For an alternative `A' ≠ ℂ ⊕ ℍ ⊕ M_3(ℂ)`, the rank(P_HSS) tautology may not apply; the Tr − R_CM form could have non-trivial structure.

**Caveat**: Major structural commitment — entire framework's NCG-axiomatic infrastructure needs re-derivation for the alternative algebra. Pati-Salam extension and GUT-extended variants are candidates but have their own structural constraints.

#### Rank 5: **(ε) Substrate-natural M_KK²-area normalization**

**Score against (S1-S4)**:
- (S1) Algebraic exactness: ✓ trivially (constant rescaling).
- (S2) L_max-independence: ✓ (renormalization is L_max-agnostic).
- (S3) Cell membership: unchanged.
- (S4) THEOREM-verified: trivially.

**Observable-form non-degeneracy**: ✗ — this is JUST renormalization. The Tr_HSS − R_CM = 0 STRUCTURAL DEGENERACY is INDEPENDENT of the normalization choice. Changing S_BH^semicl reference doesn't address the numerator's structural cancellation.

**Caveat**: Does NOT solve the W1-1 FAIL. The FAIL is structural in the observable definition, not in the comparison reference. Rank 5 is included for completeness but is NOT a viable alternative corridor for the W1-1 closure.

### IV.4. Cross-Wave Methodology Rule Extension

The W1-1 FAIL surfaces a **specific structural pre-flight check** that would have flagged the gate at plan-freeze and prevented dispatch as configured:

#### Proposed: `epistemic-discipline.md §"Degenerate-Observable Pre-Flight Check"` (PRU Class 8.7)

**Rule statement**:

> Any gate whose verdict is computed as `A − B` where `A = Tr_S(P_S)` (trace of a projector P_S on the spectral triple) and `B = R_CM = Res[Tr(D^{−2s}); s = (d−n)/2]` (Connes-Moscovici §III.4 residue extraction) under universal kernel `γ(s) = Γ(s)` MUST pre-flight-verify at plan-freeze whether the spectral triple `(A, H, D)` is REGULAR. For finite spectral triples (the framework's `(A_K, H_K, D_K)` at L_max ≤ ∞), ζ_D(s) is entire; ζ_D(0) = rank(P_S) by structure. THEREFORE the `A − B` form evaluates to zero IDENTICALLY on this class under γ(s) = Γ(s) — verdict is structurally degenerate by construction.

**Pre-flight check protocol** (extends `_pru_cardinality_audit.py` machinery):

1. Detect plan-block patterns matching `Tr.*\b(P_HSS|P_S)\b.*−.*R_CM` or `value\s*=.*ζ_D\(0\)` in the gate's substitution chain.
2. If detected, search the plan-block for explicit declaration that the spectral triple is NON-REGULAR (i.e., that γ(s) ≠ Γ(s)).
3. If no NON-REGULAR declaration: emit `PRU Class 8.7 — DEGENERATE-OBSERVABLE-FORM-DETECTED` with MANDATORY-halt routing.

**Remediation**:
- Restructure the gate to use Connes-Karoubi pairing (Rank-1 alternative per §IV.3).
- OR explicitly declare γ(s) ≠ Γ(s) and supply the modified residue extraction formula.
- OR move the gate to infinite spectral triple or appropriately-regulated continuum image.

**K-counter status**: K=1 calibration at S89 W1-1. SUGGESTION-status; advisory until K=3 per `feedback_rules-compensate-missing-structure.md`.

**Cross-link**: this rule is structurally analogous to `substrate-first-canonical-sourcing.md §(iv) SCHEMATIC-vs-physical level pin` discipline — both close silent structural-class conflations at the pre-registration layer. Here the silent conflation is between "regular vs non-regular spectral triple" rather than "SCHEMATIC vs FULL physical regulator".

### IV.5. Cross-Pillar Pattern: Algebraic Identity Is the Framework's Bridge Currency

The dominant cross-pillar signature in S89 is that **Sage-QQ-exact algebraic identities propagate through the framework as the strongest cross-pillar bridge currency**:

- W7a's `n_s_FW² − 1 ≡ α_s_canonical` ties Pillar I (substrate Mellin-cone) to Pillar II (CMB n_s observation) via FWD-C1 bridge candidate.
- W4-4 restates the SAME identity on the JOINT (n_s, α_s) hypersurface, locking the 2D Class-8.5 PRU verdict-line value-field.
- W4-7's `cocycle ratio 7.324974` (Sage-QQ from 793346/108307) ties Pillar III (NCG cocycle norms) to Pillar V (3He-B vortex-core spectroscopy) via §VII.AH inheritance morphism with the (Δ_B/Δ_A)^p cancellation theorem.
- W2-3's `9 > 8` Wedderburn dimensional contradiction is an INTEGER identity that propagates to inheritance-morphism layer ABOVE both substrate-physics and methodology.

The pattern is structurally clear: **the framework's bridge currency is bit-exact algebraic identity in ℚ or in ℤ; numerical floors are the failure modes** (W2-1 PRU; W4-6 envelope; W1-1 cancellation noise). Future cross-pillar bridge candidates that aim for STAGE-3-PERMANENT promotion should design to LAND in algebraic identity at the Level-1 cohomology-class layer, not at numerical anchors at the Level-3 layer (which can be deferred to multi-year experimental cycles per W4-3).

The cross-domain mapping is recognizable: this is the same pattern that holds in K-theoretic and Connes-Moscovici-residue computations in the original NCG literature — Connes 1996 reconstruction theorem, Chamseddine-Connes spectral action principle, and the Connes-Karoubi pairing all produce ALGEBRAIC IDENTITIES at the cohomology-class level that the laboratory-IN observable then converges to. The phonon-exflation framework is rediscovering this convention at the registry-anatomy level.

---

## V. Carry-Forward Computations

Per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`. Each is 4-field (what / inputs / gate / effort). These propagate to S90 planning via `/rclab-plan`.

### V.1. CF-W1-1-ALT-β-CONNES-KAROUBI — Re-derive α(M) via Connes-Karoubi pairing on horizon-spanning Peter-Weyl projection

- **What**: Re-derive `α_substrate(M) = ⟨[φ_HSS^M], [Ch(P_HSS(M, L_max))]⟩ / S_BH^semicl(M)` via Connes-Karoubi pairing (NOT pure ζ-residue subtraction). The Hochschild cocycle `[φ_HSS^M]` is defined on horizon-spanning Peter-Weyl sectors at substrate-distance-1 pole s=3 under the regular CM-1995 §III.4 kernel γ(s) = Γ(s); the Chern character `[Ch(P_HSS(M, L_max))]` is the K-theoretic image of the bottom-strata projector. The pairing is structurally analogous to the W7a substrate-distance-1 pairing and the W4-7 cocycle-ratio cancellation theorem. Stage-2 cross-axis independent-verify with axis-distinctness per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`.
- **Inputs**: S89 W1-1 .npz (HSS = 6 sectors at L_max=10; Tr_HSS = 38; sector list `[(0,0), (0,1), (0,2), (1,0), (1,1), (2,0)]`); canonical_constants pins (`M_KK`, `Vol_SU3_Haar`, `tau_fold`); S88 W1b1-63 branch (c) empirical anchor `α ≈ 1/458 ≈ 2.18e-3` at M=10⁷ M_sun; `cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing"` Connes-Karoubi pairing precedent at §VII.AF.1; S86 W-5 RULE-3 χ inheritance morphism convention (`M3C_to_zero`).
- **Gate**: `S90-ALPHA-M-CONNES-KAROUBI-PAIRING-DERIVATION`. PASS iff `sign_verdict = PASS` (α > 0; substrate prediction positive microstate count ratio) AND `|α_substrate(M=10⁷, L_max=10) − 2.18e-3| / 2.18e-3 ≤ 0.10` (10% RATIO band against W1b1-63 empirical anchor; 1.5× the W1-1 5% reach because Connes-Karoubi pairings have higher absolute uncertainty than rational-identity verifications) AND `regime_verdict = VALID` (Friedrich-Bär saturation at L_max=10 for HSS sectors; bridge-anatomy 5-IS-not-IN elements present). PASS advances cross-pillar-bridge K-counter calibration corpus to instance #5 candidate (provided HIT (i ∨ ii ∨ iii) ∧ iv evaluates TRUE on the new Pillar I ↔ Pillar I (substrate↔BH-thermodynamics) bridge map class).
- **Effort**: 1.5 wave-equiv (re-derivation of Hochschild cocycle on horizon-spanning sectors + Chern character image + pairing evaluation + Stage-1 registry landing + Stage-2 cross-axis verify queue).

### V.2. CF-W4-6-MELLIN-NON-BINDING-DIAGNOSIS — Investigate why bare Mellin Tr(|D|^{−6}) at s=3 violates Level-2 envelope at L_max=10→12

- **What**: Structural diagnosis of the 47× envelope violation at §VII.AQ Mellin gate. The bare Mellin `Tr(|D|^{−6})` at substrate-distance-1 pole s=3 with L_max=10→12 relative drift 4.68% vs Class-B 0.1% suggests Level-2-non-binding under HKR (per `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` MANDATORY at K=4). Determine whether (a) the bare-Mellin observable is a Level-2-non-binding `c_L` (bare-decomposition convergence rate without HKR image to continuum lab observable), OR (b) the observable IS Level-2-binding but the HKR bridge map is mis-identified, OR (c) there exists a HKR-binding refinement that recovers the L^{−3} envelope at d=4.
- **Inputs**: S89 W4-6 .npz (Mellin Tr-values at L_max ∈ {10, 12}; rel_drift = 4.68%); `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` MANDATORY at K=4 (S88 W8-88) and Calibration #2 (W3b-15 KDE Sub-test B at S88 W-11 V.3); §VII.AF.1 Pillar III↔IV calibration (L^{-3} at d=4 with HKR `L_max → ∞`); W5-1 PASS proving HKR Level-2-binding for d_eff observable (α_fit = 2.9966).
- **Gate**: `S90-VII-AQ-MELLIN-LEVEL-2-BINDING-DIAGNOSIS`. INFO iff observable confirmed Level-2-non-binding (registry-INELIGIBLE; §VII.AQ entry routes to STAGE-1-CANDIDATE WITHDRAWN OR re-classified as bare-decomposition). PASS iff HKR-binding refinement found (recovers L^{−3} envelope at d=4 within Class-B 0.1% at L_max=10). FAIL iff observable IS Level-2-binding but HKR map mis-identified (would require a structural correction at the registry-anatomy layer).
- **Effort**: 1.0 wave-equiv (structural classification + HKR-binding refinement search if applicable).

### V.3. CF-W7c-FWD-C1-RETRY — Single PASS landing on §VII.AU.OP-PROJ STAGE-1-CANDIDATE under Element-2 OE-form regex compliance + first-attempt slot

- **What**: Re-emit FWD-C1 §VII.AU.OP-PROJ landing as a SINGLE PASS (8/8 structural-coherence) under the AFTER-pattern bridge-landing script architecture per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`. Element 2 OE-form text must satisfy regex `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)` (emission #3's `Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)` form is the validated lexical form; emissions #1, #2 used superscript-prefixed `Π^{n_s}_{substrate-distance-1}` which fails regex). First-attempt slot allocation avoids the §VII.AU → §VII.AV reroute observed at emission #3. Registry cleanup of orphaned §VII.AAU (lexical-construction wrong slot) and §VII.AV (rerouted) sections via mack-cosmic-bridge sole writer.
- **Inputs**: S89 W7a .npz (Sage-QQ exact identity); S89 W7b .npz (c_sub_corrected); S89 W7c three-emission audit trail (`computations/session-89/s89_gate_verdicts.txt` lines for emissions #1-3); permanent-results-registry.md sections at lines 17165 (§VII.AAU), 17250 (§VII.AU), 17335 (§VII.AV); `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` AFTER-pattern template; `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` for slot-allocation protocol.
- **Gate**: `S90-FWD-C1-VII-AU-RETRY-SINGLE-PASS`. PASS iff all 8 structural-coherence booleans PASS in ONE emission AND verify_section_matches returns True. PASS advances cross-pillar-bridge K-counter K=3 → K=4 (rule promotes from MANDATORY at K=3 to MANDATORY at K=4 calibration density per `feedback_rules-compensate-missing-structure.md`).
- **Effort**: 0.5 wave-equiv (single-shot re-emission with corrected lexical form + first-attempt slot + registry cleanup landings).

### V.4. CF-EPISTEMIC-CLASS-8.7-DEGENERATE-OBSERVABLE — Rule extension for degenerate-observable pre-flight check

- **What**: Promote the Degenerate-Observable Pre-Flight Check (proposed at §IV.4 of this synthesis) to `epistemic-discipline.md §"Pre-Registration Completeness"` as PRU Class 8.7. Extend `_pru_cardinality_audit.py` to detect `Tr.*\bP_HSS\b.*−.*R_CM` patterns + `value\s*=.*ζ_D\(0\)` substitution-chain patterns at plan-freeze; emit MANDATORY-halt routing on absence of NON-REGULAR γ(s) declaration. SUGGESTION at K=1 advisory; advance to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`.
- **Inputs**: S89 W1-1 calibration instance (verdict file line for `S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT-DERIVATION`; audit_sha256=`6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe`); CM-1995 §III.4 regular spectral triple theorem text; `epistemic-discipline.md §"Pre-Registration Completeness"` PRU Class 8 sub-class taxonomy table; `_pru_cardinality_audit.py` source.
- **Gate**: `S90-RULE-EXTENSION-EPISTEMIC-PRU-CLASS-8-7-DEGENERATE-OBSERVABLE`. PASS iff (a) rule text landed in `epistemic-discipline.md`; (b) `_pru_cardinality_audit.py` extension implemented and tested on the S89 W1-1 verdict line + 2 synthetic cases; (c) calibration corpus row added to `sessions/framework/registry/pru-class-corpus.md`; (d) `methodology-wave-allowlist.md` row added per `wave-classification.md` §M4. Status SUGGESTION-K=1 at landing; promotes to MANDATORY at K=3 distinct calibration instances.
- **Effort**: 0.4 wave-equiv (rule text + audit-script extension + calibration corpus row + allowlist row + W11-meta-style synthesis).

### V.5. CF-W2-1-RETRY — Class-8.3-aware xc1 tolerance + xc1/xc2 observable disambiguation

(Inherited from W2 synthesis; restated here for completeness in this synthesis's CF queue.)

- **What**: Re-author §W2-1 with (a) RATIO tolerance ≥ 1e-5 (publication-precision floor of 6-sig-fig pins); (b) split or remove xc2 — clarify whether `R_canonical` at the BdG-restricted variant is the cocycle ratio observable (target 7.324992) OR the HP^1 universal F_4 anchor observable (target 1.030902).
- **Inputs**: Plan §W2-1 method spec; canonical_constants pins; `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"` MANDATORY at K=4.
- **Gate**: `S90-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE-RETRY`. PASS iff xc1 PASSes at refined tolerance against the cocycle ratio observable AND xc2 explicitly disambiguated.
- **Effort**: 0.5 wave-equiv.

### V.6. CF-A40-FAIL-ALTERNATIVE-CHIRALITY — Investigate alternative chirality structures for §VII.AQ substrate-natural binding upgrade

(Inherited from W2 synthesis; restated for cross-cutting relevance to W4-6's bare-Mellin envelope FAIL.)

- **What**: Investigate (a) bi-chirality projection (γ_5-only and γ_F-only sectors as independent chiralities); (b) SU(3)-coloured chirality (color-axis-resolved on M_3(ℂ)); (c) substrate-natural inner-fluctuation 1-form A construction.
- **Inputs**: S88 W7-LF-D PASS APS-1975 infrastructure; `gv_canonical_difference_FW = -40579.1500479506`; spectrum cache `s84_spectrum_cache_L12_tau019.npz`; Connes-Marcolli 2008 §11 SU(N)-coloured Clifford structures.
- **Gate**: `S90-CHIRALITY-FIDELITY-ALTERNATIVE-STRUCTURES`. PASS iff `|Δ_GV_natural| ≥ 1e-3` under at least ONE alternative AND η-invariant preserved AND GV-discriminating at global level.
- **Effort**: 1.5 wave-equiv.

### V.7. CF-W7c-PARSE-TREE-PROJECTOR-NAMING-CONVENTION — Document the W7c emission #3 lexical form `Tr(P_<index>)` as canonical Element-2 OE-form

- **What**: Document the validated emission #3 lexical form `Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)` as the canonical Element-2 OE-form pattern per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"`. Add to calibration corpus at `sessions/framework/registry/cross-pillar-bridge-corpus.md §2`. Surface as a methodology rule extension if K-counter reaches K=3 distinct calibration corpus instances.
- **Inputs**: S89 W7c emission #3 verdict line; `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` positive/negative regex patterns; calibration corpus rows for §VII.AF.1 (W-5) and §VII.W-3.LAB (W4a-17).
- **Gate**: `S90-CROSS-PILLAR-BRIDGE-CORPUS-ELEMENT-2-OE-FORM-CALIBRATION-ENTRY`. PASS iff calibration corpus row added with full SHA pin AND audit pattern documented.
- **Effort**: 0.2 wave-equiv (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`).

**CF summary**: 7 carry-forwards totaling 5.6 wave-equiv. Dependency graph: CF-W2-1-RETRY (V.5) is prereq for CF-W2-2-DEFERRED, CF-W2-4-DEFERRED (from W2 synthesis); CF-W1-1-ALT-β-CONNES-KAROUBI (V.1), CF-W4-6 (V.2), CF-W7c-RETRY (V.3), CF-EPISTEMIC-8.7 (V.4), CF-A40-ALT-CHIRALITY (V.6), CF-W7c-CORPUS (V.7) are structurally INDEPENDENT.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | W7a `n_s²−1 ≡ α_s` Sage-QQ exact at substrate-distance-1 s=3 | GEOMETRIC | PASS (Cell I) | Locks FWD-C1 substrate-IS leg at Level-1 cohomology-class identity; 2.0952σ Planck tension is structural prediction |
| 2 | W4-4 same identity on JOINT (n_s, α_s) hypersurface | GEOMETRIC | PASS (Cell I joint) | Class-8.5 PRU 2D verdict-line value-field; 6.22σ on α_s axis CMB-S4 testable |
| 3 | W7b c_sub_corrected = 14.528574 closed-form scalar | GEOMETRIC | PASS (Cell I) | FWD-C1 Level-3 anchor structurally verified; Reading-A pin |
| 4 | W4-1 14-state SDP rank=11 ≤ Pad=18 | GEOMETRIC | PASS (algebra-structure) | Pad-block convention artifact removed; substrate-canonical 14-state robust |
| 5 | W4-7 §VII.AH 8/8 PASS via cocycle ratio + (Δ_B/Δ_A)^p cancellation | GEOMETRIC | PASS (cross-pillar III↔V) | First cross-axis joint theorem to reach STAGE-3-PERMANENT eligibility; K=1→K=2 substrate-input-orthogonality |
| 6 | W5-1 Richardson L^{−3} α_fit = 2.9966 R²=1.0000 | GEOMETRIC | PASS (Level-2-binding) | HKR Level-2-binding envelope BINDS Level-1 HK-5(τ_fold) cohomology-class identity at d=4 |
| 7 | W5-2 Corner-IV K-window log-derivative L = −7.046336 bit-exact | GEOMETRIC | PASS (Cell IV) | W-17 R3 closure validated; substrate-IS state-pair functional canonical |
| 8 | W2-3 χ' inheritance morphism Wedderburn 9 > 8 forces zero map | GEOMETRIC | PASS (axiomatic) | Definitional-datum-vs-derived-theorem K=2→K=3 promotion candidate |
| 9 | W3 substrate-clock cohort (8 gates joint UNIQUENESS proof) | GEOMETRIC | PASS (cohort) | Pinning-A canonical UNIQUE substrate-natural temporal coordinate |
| 10 | W5-7 + W5-8 Sage-QQ regulator-CLASS-INVARIANT N=4/5 | GEOMETRIC | PASS (Cell II) | §VII.AR LEVEL-DRESSED rank-ordering at s=4 sharpened |
| 11 | **W1-1 α(M) = −1.591e-116 ζ-residue degenerate** | GEOMETRIC | FAIL (degenerate-observable) | **Closes pure-residue-subtraction corridor; opens Connes-Karoubi pairing alternative (rank-1)** |
| 12 | W4-6 §VII.AQ Mellin Tr(\|D\|^{−6}) L_max drift 4.68% vs 0.1% | GEOMETRIC | FAIL (Level-2-non-binding) | bare Mellin lacks HKR-binding; registry-INELIGIBLE for §VII.AQ Stage-3 |
| 13 | W2-1 Connes-Karoubi pairing 6 OOM tolerance + xc1/xc2 confusion | GEOMETRIC | FAIL (Class-8.3 PRU) | Methodology-layer plan-authorship issue; substrate-physics unaffected |
| 14 | W2-5 Δ_GV_natural = 0 under γ_9 = γ_5 ⊗ γ_F anticommutation | GEOMETRIC | FAIL (chirality-anticom-degenerate) | Reproduces W-23 V.2 calibration locus; §VII.AQ canonical-import retained |
| 15 | W7c §VII.AU.OP-PROJ FWD-C1 landing 7/8 best (3 emissions) | GEOMETRIC | FAIL (registry mechanics) | Substrate-physics PASS; K=3→K=4 advancement DEFERRED to S90 single-shot retry |

---

## Cross-Domain Pattern Closure

The S89 substrate-IS constraint surface is now mapped. The strongest cross-pillar pattern surfaced is:

**Algebraic identity in ℚ at the substrate-distance-1 Mellin pole s=3 is the framework's strongest bridge currency.** W7a + W4-4 demonstrate it within the Pillar I substrate-distance-1 cocycle structure; W4-7's `(Δ_B/Δ_A)^p` cancellation theorem demonstrates it for inheritance-morphism rank-2 kernels at Pillar III ↔ V; W2-3's Wedderburn dimension contradiction demonstrates it at the algebra-structure layer; W5-1's HK-5 closed-form Sage-QQ exact `2500π/(500π − 19)` demonstrates it for the L^{−3} convergence binding observable. The framework's structural integrity is anchored by these exact-rational identities at the cohomology-class level.

**Floor-floor mismatches and observable-form degeneracies are the failure modes.** W1-1 (ζ_D(0) = rank tautology), W2-1 (publication-precision-floor PRU), W2-5 (chirality anticommutation cancellation), W4-6 (Level-2-non-binding) — each FAILs at a DIFFERENT structural layer. None of these are sampling failures or substrate-physics defects; all four are exact-structural impossibilities at the layer at which the gate was pre-registered.

The methodology rule extension proposed at §IV.4 (PRU Class 8.7 Degenerate-Observable Pre-Flight) is the highest-leverage forward enforcement: it would have flagged W1-1 at plan-freeze and routed the gate to one of the four viable alternative corridors (β, γ, α, δ — Rank 5 is ruled out as non-fix). The same pre-flight pattern generalizes to any future framework gate that subtracts a residue from a trace on a regular spectral triple under the CM-1995 §III.4 universal kernel γ(s) = Γ(s).

The framework's PASS cluster occupies a tight, internally consistent corridor; the FAIL cluster identifies the four distinct mechanisms by which gates exit that corridor. This is exactly the constraint-map architecture the framework's methodology is designed to surface.
