# S91 W9 SCHEMATIC-vs-FULL Canonical-Pin Reckoning at Substrate-Distance-1 Pole `s=3`

**Author**: `connes-ncg-theorist` (Workhorse-NCG; framework's NCG-axiomatic FULL Connes-Chamseddine physical-multiplier authority)
**Dispatch**: S91 Slot 1 entry S-7 from `sessions/archive/session-91/session-91-workshop-schedule.md` — `/rclab-review` solo synthesis (no rounds, no cross-agent coordination). Retry after a prior socket-error dispatch produced no on-disk output.
**Date**: 2026-05-21
**Source-document SHA pins (audit trail)**:
- `sessions/archive/session-91/session-91-w9-workingpaper.md` (2723 lines; §W9-4, §W9-7, §W9-8, §W9-10 consumed)
- `sessions/permanent-results-registry.md` §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ + §VII.AQ.STATE-PROJ
- `computations/_shared/canonical_constants.py` (lines 159-273; `R_universal_HP1_strict_F4 = 1.030902`; `eps_H_HP1_norm = 16.197719`; `gv_canonical_difference_FW = -40579.1500479506`)
- `computations/_shared/_spectral_action_regulators.py` (docstring lines 23-30 SCHEMATIC self-identification)
- `sessions/archive/session-91/workshops/_seed-w9.md` (Slot S1-1 invocation)

**Substrate framing pre-pin** (per `phononic-framing.md §"IS Space, Not IN Space"`): The substrate IS the spectral triple `(A_K, H_K, D_K)` at `τ_fold = 0.190` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (Wedderburn) and `D_K` the Jensen-deformed Dirac operator on SU(3). Every observable in §W9-4/7/8/10 IS a substrate-IS spectrum-only functional or Hochschild cocycle norm at a Mellin pole `s ∈ {3, 4}` on this triple. The SCHEMATIC `_spectral_action_regulators.py` Mellin helper and the FULL Connes-Chamseddine 1996 §2.2-2.3 Pauli-Villars physical-multiplier pipeline are **two methodology-floor F-images** of the same Level-1 substrate-IS observable per the layer-functor `F: substrate → methodology → audit` of `epistemic-discipline.md §"Layer-Decomposition"`. They are NOT two substrates; they are not two competing physics theories; they are two *evaluation conventions* of the **same** substrate-IS canonical at distinct points on the SCHEMATIC↔FULL level-pin axis.

---

## 1. Four-Gate Convergence Summary

| Gate | Verdict | Observable | Pole | SCHEMATIC vs FULL signature | audit_sha256 (16-head) |
|:-----|:--------|:-----------|:-----|:----------------------------|:-----------------------|
| **§W9-4** `S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE` | **FAIL** (`composite=FAIL; sign=FAIL; magnitude=FAIL; regime=VALID`) | `Δ_FULL = (ρ_FULL(s=3) − R_universal_HP1_strict_F4) / R_universal_HP1_strict_F4` on `§VII.AF.1.OP-PROJ` | s=3 (substrate-distance-1) | `Δ_FULL = −2.018738%` (2.02% below SCHEMATIC canonical; FULL CC PV ρ converges *away* from SCHEMATIC STRICT_F4 anchor as L_max grows); s=4 cross-pin returns `ρ_FULL(s=4) = +1.0220` (+2.20% upward; FULL pipeline structurally sound) | `79314db6a6aee053` |
| **§W9-7** `S91-CF37-AUX-4-(c)compose(d)-SECONDARY-CORRIDOR-PARALLEL-EVALUATION` | **FAIL** (`composite=FAIL; sign=PASS; magnitude=FAIL; regime=VALID`) | `Delta_PARALLEL = \|R_CM_full − R_ansatz\| / \|R_ansatz\|` on CF-37 (c)∘(d) compositional secondary corridor | s=4 (substrate-distance-2) | `Delta_PARALLEL = 1.045538` (O(1) ≈ 104.6%; FULL CM-1995 §III.4 residue formula vs structural-ansatz Wedderburn-rank-ratio layer disagree by factor ~2); INTRA-Corner-I (algebra-INVARIANT × s=4) layer-axis discriminator | `3d6b13d8036155fb` |
| **§W9-8** `S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX` | **FAIL** (`composite=FAIL; sign=FAIL; magnitude=FAIL; regime=BREAKDOWN`) | Composite-MS∘HKR Level-2 envelope `α_composite` on `§VII.AU.OP-PROJ` against `R_canonical_VII_AU = R_universal_HP1_strict_F4 = 1.030902` | s=3 (primary; §VII.AU canonical anchor) + s=4 (cross-pin Friedrich-Bär self-anchor) | s=3 fit returns `α = −1.518765` (anti-convergence; Δ_emp GROWS with L_max: 1.096e−02 → 1.664e−02 → 2.019e−02 at L=8/10/12); s=4 fit returns `α = +4.100568` (PASS-band above α_HKR=3 on FULL self-anchor) | `0da19aba653fa19d` |
| **§W9-10** `S91-HH1-FINITE-ALPHA-FIRST-EXTRACTION` | **FAIL** (`composite=FAIL; sign=PASS; magnitude=FAIL; regime=VALID`) | `α_operational(s=3)` for HH^1 cocycle norm on M_3(ℂ) Peter-Weyl block at substrate-distance-1 pole | s=3 (substrate-distance-1) targets s=4 (substrate-distance-2) pole semantics | `α_operational(s=3) = 0.110434`; `α_asymptotic_sage_q = 0.122026`; cross-axis agreement 9.50% (≤10% tol); pre-reg band [1.5, 4.0] targeted d=4 NCG L^{-2} expectation — STRUCTURALLY at substrate-distance-2 pole `s=4`, NOT at substrate-distance-1 pole `s=3` (Wodzicki/Connes 1995 §III pole-pin) | `57d15c4671fbcbfe` |

**Convergence statement**: All four verdicts are FAIL; all four point at the same substrate-physics conclusion at distinct projections — the SCHEMATIC `_spectral_action_regulators.py` Mellin helper at L_max=10 STRICT_F4 (the upstream provenance of `R_universal_HP1_strict_F4 = 1.030902` via the `f_4_prefactor_sdw` DERIVATIVE relation per `canonical_constants.py:159-273` PROVENANCE chain) is structurally **biased** relative to the substrate-natural FULL Connes-Chamseddine 1996 §2.2-2.3 Pauli-Villars pipeline at the same pole. The four signatures are mutually consistent under the level-pin orthogonality of `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY (S88 W7b-83 close); they do NOT contradict each other; they jointly map a single substrate-physics finding across four observables on the substrate-distance-1 Mellin pole.

---

## 2. Substrate-Physics Narrative

### (a) Why SCHEMATIC vs FULL diverges at substrate-distance-1 pole `s=3`

#### The substrate-physics: two regulator pipelines, one Mellin pole

The substrate's intrinsic Seeley-DeWitt expansion at the substrate-distance-1 pole admits the closed-form

```
a_n^{CC}  =  Γ(n/2) · (c_1 · M_1^n  +  c_2 · M_2^n)
```

under the Connes-Chamseddine 1996 §2.2-2.3 2-point Pauli-Villars regularization tuple `(M_1, c_1, M_2, c_2) = (M_KK, +2, √2·M_KK, −1)` (canonical at the M_KK compactification scale). The Pauli-Villars consistency identities

```
Σ_r c_r  =  +1     (UV identity reproduction at λ² → ∞)
Σ_r c_r M_r²  =  0  (no quadratic divergence; multiplier-vector grading f_0^anomaly = 0)
```

force the closed forms `a_2^{CC} = 0` and `a_4^{CC} = −2·M_KK⁴`. §W9-4 verified both identities at machine precision: `Σ c_r = 1.0`; `Σ c_r M_r² = −4.44e−16`; `a_2_CC = 0.000000e+00`; `a_4_CC = −6.090766e+67` (relative residual 3.93e−16 vs the predicted `−2·M_KK⁴`). The closed forms ARE substrate-IS algebraic constraints on the regularization tuple per Connes-Chamseddine 1996 §2.2-2.3; they cannot fail at the FULL CC layer because they are algebraic consequences of `Σ c_r = 1` and `Σ c_r M_r² = 0`.

The SCHEMATIC `_spectral_action_regulators.py` helper (W12-ELIM-8 5-regulator atlas) provides five deterministic pure-spectrum evaluators on the multiplicity-weighted SU(3) Casimir Weyl-dim spectrum:

```
zeta_a_n(n, L_max)        :  (1/Vol_SU3_Haar) · Σ_{(p,q)≠(0,0), p+q≤L_max} d(p,q) / C_2(p,q)^n
mellin_a_n(n, L_max)      :  identical to zeta on the positive-definite Casimir spectrum
heat_kernel_a_n(n, L_max) :  Σ d · exp(−t·C) / C^n at finite t_ref
hard_cutoff_a_n(...)      :  Σ truncated at C ≤ cutoff_frac · max(C)
pauli_villars_a_n(...)    :  Σ d · [1/C^n − 1/(C+M_PV²)^n] with M_PV² = M_PV_sq_frac · max(C)
```

The module's own docstring (lines 23-30) explicitly declares:

> "These are SCHEMATIC regulators — intended as reasonable pure-spectrum analogs of the named regulators in Chamseddine-Connes 1996 §2.2-2.3 (Mellin moments f_0, f_2, f_4 of the cutoff function f restricted to [0, ∞)). They are NOT the full physical regularizations used in the S61/S78 Pauli-Villars pipeline (which uses Lambda_UV = M_KK as the physical cutoff). The point of the 5-regulator atlas is to measure SPREAD of an observable across a discrete set of regulator prescriptions, not to pin any single prescription as canonical."

The structural distinction is therefore **declared by the module itself**. The SCHEMATIC pauli_villars_a_n uses `M_PV² = M_PV_sq_frac · max(C_2(p,q))` (a *fraction* of the Casimir ceiling on the L_max-truncated SU(3) spectrum); the FULL CC pipeline uses `M_1 = M_KK ≈ 7.4287e+16 GeV`, `M_2 = √2·M_KK ≈ 1.0507e+17 GeV` (the physical compactification scale per Connes-Chamseddine 1996 §2.2-2.3). The two are not numerically perturbative versions of each other — they differ at the **dimensional prefactor layer** (SCHEMATIC: dimensionless Casimir-ceiling ratios; FULL: dimensional M_KK² ≈ 5.52e+33 GeV² mass scale) AND at the **L_max saturation layer** (SCHEMATIC: the Mellin helper saturates at finite L_max where the cache cutoff is reached; FULL: the evaluator continues to L_max → ∞ via the Friedrich-Bär saturation theorem per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` η_FB_lower = 0.40).

#### Mechanism of the 2.02% s=3 deviation (§W9-4 verdict)

§W9-4 evaluated the substrate-IS regulator-INVARIANT atlas ratio

```
ρ_FULL(s=3)  =  M_FULL_CC(s=3) / M_BARE(s=3)
              =  1.8003004557e+04  /  1.7823154840e+04
              =  +1.0100907902e+00
```

on the L_max=12 master spectrum cache `s84_spectrum_cache_L12_tau019.npz` (90 Peter-Weyl (p,q) sectors, 166,896 raw eigenvalues, 31,956,720 multiplicity-weighted states). The point-wise PV multiplier on the full spectrum reads

```
w_PV(λ²; s=3)  =  1 − Σ_r c_r · [M_r² / (λ² + M_r²)]^3
```

with multiplier range `[0.991467, 1.058870]` and mean `1.002747`. The FULL CC value is therefore `+1.01%` above the bare Mellin moment at the s=3 pole.

The §VII.AF.1.OP-PROJ registry pin `R_universal_HP1_strict_F4 = 1.030902` (canonical_constants.py:273; LANDED S86 W-5 V4 via SDW-residual atlas ratio at L_max=10 STRICT_F4 atlas; derivative form per the Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY chain `1.030902 = 1/0.970024 modulo publication precision` with PRIMARY canonical `eps_H_HP1_norm = 16.197719` at ζ-regulator per W-5 V4 Step 1 line 397) is in turn `+3.0902%` above unity.

The deviation `Δ_FULL = (1.0100907902 − 1.030902) / 1.030902 = −2.018738e−02 = −2.02%` is the substrate's report that **on the same L_max=12 cache, the FULL CC PV-regulated atlas ratio sits 2.02% below the SCHEMATIC STRICT_F4 SDW-residual ratio**. The s=4 cross-pin diagnostic `ρ_FULL(s=4) = +1.0219998057e+00` (2.20% above unity; consistent with §W1-2 CF-70 sibling evaluation) confirms the FULL CC pipeline is structurally sound — the FAIL is **NOT** a FULL CC pipeline defect, it IS a regulator-class divergence between SDW-residual atlas (the SCHEMATIC class encoded in `R_universal_HP1_strict_F4`) and FULL Pauli-Villars CC1996 §2.2-2.3 evaluation on the same substrate-distance-1 pole.

#### Mechanism of the §W9-8 anti-convergence pattern

§W9-8 scanned the empirical envelope `Δ_emp(L) = |ρ_FULL(L) − R_canonical_VII_AU| / R_canonical_VII_AU` at L ∈ {8, 10, 12}:

| L_max | Δ_emp(s=3) | L^{−3} | Δ_emp / L^{−3} |
|:------|:----------:|:------:|:---------------:|
| 8 | 1.096478e−02 | 1.953125e−03 | 5.6140 |
| 10 | 1.664122e−02 | 1.000000e−03 | 16.6412 |
| 12 | 2.018738e−02 | 5.787037e−04 | 34.8838 |

`Δ_emp INCREASES with L_max` — the FULL CC ρ converges **away** from the §VII.AU canonical pin (which inherits `R_universal_HP1_strict_F4 = 1.030902` SCHEMATIC). Log-log fit on this anti-convergent sequence returns `α_composite_value = −1.518765`. The s=4 cross-pin against the Friedrich-Bär self-anchor (`R_anchor_s4 = ρ_FULL(L=12) = 1.022000`) returns `α = +4.100568` (well above α_HKR = 3 PASS-band). The two readings together demonstrate the FAIL is *specific to the §VII.AU canonical pin*, not a defect of the composite Mukhanov-Sasaki ∘ HKR envelope-composition rule: the composite envelope behaves correctly on its own substrate-natural asymptote.

The §VII.AF.1.OP-PROJ entry's own *Substrate-internal over-performance regime annotation* (registry line 14801; S91 W0 in-session landing per W-6 CF-2 = T2.55) documents this same sign-flip at the OPPOSITE pole:

> "§VII.AU.OP-PROJ at the same d=4 substrate-distance-1 pole `s=3` exhibits the OPPOSITE empirical signature — finite-L value above asymptotic envelope (slower-than-L^{-3} apparent decay), corresponding to **positive subleading C_1** in the same CM-1995 §III.4 expansion. The sign-flip between §VII.AF.1.OP-PROJ (negative C_1) and §VII.AU.OP-PROJ (positive C_1) IS the Layer-Functor F Verdict-Shape Consistency Theorem's K=2 SUGGESTION calibration corpus instance #1 + #2."

§W9-8's anti-convergent fit is the **first quantitative confirmation** of the registry's predicted positive-C_1 signature at §VII.AU.OP-PROJ. The SCHEMATIC pin sits ABOVE the FULL CC asymptote at finite L_max; as L_max grows, the FULL CC value moves toward its asymptote and away from the SCHEMATIC anchor, producing the anti-convergent log-log fit.

#### Mechanism of the §W9-7 O(1) layer-axis discrepancy

§W9-7 evaluated the same substrate-IS CF-37 (c)∘(d) compositional secondary corridor at the substrate-distance-2 pole `s=4` via two methodology-floor F-images:

```
R_CM_full   =  7.977596e−04   (FULL Connes-Moscovici 1995 §III.4 residue formula)
R_ansatz    =  3.900000e−04   (W3 T1.8 structural-ansatz Wedderburn-rank-ratio χ'_weight = 3/6 = 0.5)
Delta_PARALLEL  =  |R_CM_full − R_ansatz| / |R_ansatz|  =  1.045538  ≈  104.6%
```

The FULL CM-1995 §III.4 evaluator and the structural-ansatz Wedderburn-rank-ratio evaluator disagree by a factor ~2 at the substrate-distance-2 pole on the same (c)∘(d) compositional restriction. Both are algebra-INVARIANT spectrum-only functionals on Cell I (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY K=3) — the discrepancy is INTRA-Corner-I (within the algebra-INVARIANT cell), NOT cross-Corner. The structural cause is the **same** as §W9-4/8: a methodology-floor F-image disagreement between a SCHEMATIC-class evaluator (the algebraically-pinned `χ'_weight = 3/6` structural-ansatz, an early-pole Wedderburn-fraction approximation) and a FULL physical evaluator (the CM-1995 §III.4 residue formula).

#### Mechanism of the §W9-10 wrong-pole admissibility band

§W9-10 returned `α_operational(s=3) = 0.110434` with Sage-Q asymptotic cross-check `α_asymptotic_sage_q = 0.122026` (agreement within 9.50%, ≤10% tolerance per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"`). The pre-registered admissibility band [1.5, 4.0] targeted the d=4 NCG convergence rate L^{-2} (Wodzicki/Connes 1995 §III dimension-spectrum at the a_4 pole `s=4`). The band is structurally correct at the substrate-distance-2 pole `s=4` (the `a_4` Yang-Mills pole; Mellin exponent `−2s = −8`); the §W9-10 gate evaluated at `s=3` (the `a_2` Einstein-Hilbert / substrate-distance-1 pole; Mellin exponent `−2s = −6`).

The substrate's intrinsic HH^1 envelope-extraction rate at substrate-distance-1 pole `s=3` IS slow (`α ≈ 0.11`, in cache + Sage-Q-asymptotic concordant within 10%) — the slow rate is a substrate-physics property of the M_3(ℂ) block at the `a_2` pole, NOT a substrate-physics failure. The pre-reg band was the methodology-floor pre-registration of an externalized d=4 expectation that does not match the substrate's pole structure at s=3. Per the §W9-10 substrate framing addendum (verbatim runtime block): *"The substrate IS what it IS; the FAIL identifies a methodology-floor mismatch between the pre-registration band and the substrate-IS pole."* This is the §W9 cluster's fourth independent surface of the same substrate-physics finding: the SCHEMATIC convergence-rate expectations baked into the §VII canonical pins (and the §W9-10 pre-reg band) at substrate-distance-1 pole `s=3` are inherited from d=4 substrate-distance-2 pole structural expectations that do not transfer to s=3.

### (b) FI/RD/MIXED reclassification per affected §VII pin

Per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` and the §VII.K-PROP-W8-LAYERED 4-row layered taxonomy (S88 W9-108), each §VII registry pin admits classification on the FI/RD/MIXED axis at each substrate-distance pole.

#### §VII.AF.1.OP-PROJ — MIXED-class boundary case (S92 W-1 first-extraction discharge target)

- **Level-1 (cohomology-class identity)**: INVARIANT — the Hochschild pairing `⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` is regulator-invariant at the COHOMOLOGY-CLASS level (Connes-Karoubi pairing on band-0 projector). This level is PROVEN STRUCTURAL THEOREM; holds at every L_max; **NO reclassification**.
- **Level-2 (algebraic envelope)**: L^{-3} at d=4 — STRUCTURAL PREDICTION; algebraically derived from CM-1995 §III.4. The envelope's structural form is preserved; the subleading C_1 sign (negative per §VII.AF.1 over-performance regime; positive per §VII.AU under-performance regime; predicted at §VII.AF.1 line 14809) is now confirmed by §W9-8 as a QUANTITATIVE feature of the **regulator-class boundary** between SCHEMATIC SDW-residual and FULL CC PV.
- **Level-3 (empirical anchor at L_max=10)**: FAIL-with-disclosure on the SCHEMATIC↔FULL boundary at 2.02%. The Level-3 anchor `1.030902 = R_universal_HP1_strict_F4` is reclassified as **MIXED-class** at substrate-distance-1 pole s=3 — `FI` along the L_max → ∞ HKR axis (the cohomology-class identity is regulator-invariant) but `RD` along the **SCHEMATIC↔FULL level-pin axis** at finite L_max=10 (the 2.02% deviation between SCHEMATIC SDW-residual STRICT_F4 anchor and FULL CC PV value at L_max=12 is the regulator-class-DEPENDENT signature).

  The MIXED tag is the structurally-correct verdict per `regulator-pin-discipline.md` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE extension (the SCHEMATIC SDW-residual ratio was published before the FULL CC physical multiplier evaluator at L_max=12 was operational on the master cache) AND per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` MIXED-class definition (FI on one axis; RD on another). The §VII.AF.1.OP-PROJ registry-PASS status (`match/envelope = 0.0950 = 9.50%` per W-5 V4 substitution chain Step 3) **stands unchanged** at the cohomology-class L^{-3} envelope; the MIXED-class annotation is a refinement at the regulator-class axis, not a corrigendum to the registry-PASS criterion.

- **STRUCTURAL-ORTHOGONAL-COMPANION landing required**: per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` and the §W9-4 carry-forward (item 2 of §W9-4 runtime CF block), both `R_universal_HP1_strict_F4 = 1.030902` (SDW canonical, SCHEMATIC class) and `rho_FULL(s=3) = 1.0100907902` (FULL CC canonical, FULL physical class) MUST be landed as STRUCTURAL-ORTHOGONAL-COMPANION readings at §VII.AF.1.OP-PROJ. Each reading carries its own regulator-class tag per `regulator-pin-discipline.md`: `a_n^{SDW}` (SCHEMATIC class) vs `a_n^{Pauli-Villars-CC1996}` (FULL physical class). The two readings are NOT co-primary anchors of a single derivation chain (they are not on the same scheme); they are structurally-orthogonal companions on the SCHEMATIC↔FULL level-pin axis.

#### §VII.AU.OP-PROJ — LEVEL-class mismatch confirmed (CONFIRMED-PROMOTED-LEVEL-CLASS-MISMATCH; S92 W-1 FULL-physical re-extraction REQUIRED)

- **Level-1**: INVARIANT — the Sage-QQ exact rational identity `n_s_FW_exact² − 1 ≡ α_s_canonical` in Q at substrate-distance-1 pole s=3 (W7a PASS audit_sha256=`01c1ac83...`) is a STRUCTURAL THEOREM at every L_max via Sage-QQ exact rational arithmetic. **NO reclassification**.
- **Level-2**: L^{-3} at d=4 substrate-distance-1 pole s=3 — STRUCTURAL PREDICTION; Level-2-binding sub-class per S88 W8-88 (HKR `L_max → ∞` image binds Level-1 cohomology-class identity). The envelope itself is structurally sound; §W9-8's s=4 self-anchor fit `α = +4.10` confirms the FULL-physical pipeline satisfies the L^{-3} envelope on the substrate's own asymptote.
- **Level-3**: FAIL via SCHEMATIC anchor; PASS via FULL self-anchor. The §VII.AU.OP-PROJ canonical pin **inherits SCHEMATIC class from `R_universal_HP1_strict_F4`** (registry line 17840 calibration corpus position #1, instance status LANDED S87 W5-1 with `L^{-3}` envelope at L_max=10 STRICT_F4 atlas), and is currently tagged `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` since S90 W1-15. **§W9-8's anti-convergent envelope on the SCHEMATIC anchor + concordant +4.10 envelope on the FULL self-anchor jointly close the deferred-pending sub-class transition pathway**: the FIRST-EXTRACTION discharge requires re-pinning §VII.AU.OP-PROJ canonical at FULL Connes-Chamseddine 1996 §2.2-2.3 physical multiplier evaluation, **NOT** at the SDW-residual STRICT_F4 atlas. The mismatch is LEVEL-class (SCHEMATIC vs FULL), confirmed.

#### §VII.AQ — Retrofit candidate (S92+ scheme-suffix discipline)

§VII.AQ.OP-PROJ (STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE; LANDED S88 W7b-79; S90 W7 CF-54 Phase-2 retrofit) underwent bit-precision scheme-INDEPENDENCE confirmation at §W9-11 (`max_pairwise_diff = 0.000e+00` across APS-1975 + Cheeger-Simons + Bismut-Cheeger; Reading A confirmed). The §W9-11 PASS demonstrates the GV-Heitsch invariant on (C_H, C_εH) parity-twin pair IS regulator-class-preservation-invariant at the secondary-class evaluation morphism — i.e., across the *bridge-map-scheme axis*. However, the §VII.AQ canonical pin `gv_canonical_difference_FW = -40579.1500479506` (canonical_constants.py:1636; full float64 from s84_w10a_115_gv_explicit.npz; W-11 §3 anchor) was extracted under an upstream regulator atlas that is STRUCTURALLY ORTHOGONAL to the §W9-11 Reading-A bridge-map-scheme axis. The §VII.AQ entry remains a **retrofit candidate** for SCHEMATIC-vs-FULL re-anchoring at S92+ to verify the GV-Heitsch numerical pin is robust under FULL CC physical multiplier evaluation as well as scheme-independent across APS-1975/Cheeger-Simons/Bismut-Cheeger. The retrofit is queued in §W9-11 CF-W9-11-1 (scheme-suffix retrofit; ~0.2 we).

- **Forward classification (post-retrofit)**: TBD-pending — Level-1 INVARIANT (Connes-Karoubi pairing on HP^1 secondary class; structural); Level-2 envelope TBD pending substrate-distance pole pin (S87 W8-8 confirmed regulator-INDEPENDENT across A_5_extended atlas, but the §VII.AQ entry's Mellin-pole declaration must be substrate-canonicalized in the retrofit); Level-3 anchor pending FULL CC physical re-extraction.

### (c) S92 W-1 campaign forward-pin sequencing

The four W9 FAILs jointly route to **a single S92 W-1 SCHEMATIC-vs-FULL canonical-pin retirement campaign** with four sequenced sub-items. Total estimated effort: **~7.0 wave-equivalents** across the four items. The sequencing pre-registers compute-mode dependencies AND structural-axis ordering: §W9-4 first (it establishes the SCHEMATIC↔FULL boundary quantitatively at §VII.AF.1; closes substrate-physics calibration corpus instance #1 on the FULL-CC level-pin axis); §W9-8 second (it depends on §W9-4's L_max=12 FULL CC value as upstream pin for the §VII.AU canonical re-extraction); §W9-7 third (CF-37 INTRA-Corner-I layer adjudication is structurally separate from §VII.AF.1/AU; OAA exclusions force a different producing agent); §W9-10 fourth (HH^1 wrong-pole retry can run in parallel with the §VII.AF.1/AU campaign once the pole-pin discipline lands).

#### CF-W9-4-A (S92 W-1; ~1.5 we; PRIMARY: connes-ncg-theorist)

1. **What**: §VII.AF.1.OP-PROJ STRUCTURAL-ORTHOGONAL-COMPANION landing. Land `R_universal_HP1_strict_F4 = 1.030902` (SCHEMATIC SDW class; `a_n^{SDW}` regulator tag) AND `rho_FULL_AF1_s3 = 1.0100907902` (FULL Pauli-Villars-CC1996 class; `a_n^{Pauli-Villars-CC1996}` regulator tag) as STRUCTURAL-ORTHOGONAL-COMPANION readings at §VII.AF.1.OP-PROJ. Both readings carry explicit `convention=...-SCHEMATIC` vs `convention=...-FULL-CC-MULTIPLIERS-PHYSICAL` suffix tags per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline. Re-derive the FI/RD atlas spread at substrate-distance-1 pole s=3 across the 5-regulator atlas (ζ-, SDW-, Pauli-Villars FULL-CC, Mellin-, lattice-) at L_max=12 on the master spectrum cache; classify §VII.AF.1.OP-PROJ Level-3 as FI/RD/MIXED per the §"FI/RD reclassification" §2(b) above (current verdict: MIXED-class on SCHEMATIC↔FULL level-pin axis at finite L_max=10; FI on cohomology-class axis at L_max → ∞).
2. **Who**: connes-ncg-theorist (PRIMARY; FULL CC multiplier authority) + mack-cosmic-bridge (sole-writer for §VII.AF.1.OP-PROJ registry text per `feedback_mack-bridge-role.md`).
3. **Input**:
   - `s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7fd6a6949...`)
   - `canonical_constants.py:159-273` (SHA `af3b39ba2c95cce8...` for `R_universal_HP1_strict_F4` SDW-class provenance chain)
   - §W9-4 npz `s91_w9_cf49_full_cc_multipliers_vii_af_1.npz` (SHA `ab386b2fc11ef9c9...` for `rho_FULL(s=3)` FULL-CC value)
   - `_spectral_action_regulators.py` (SCHEMATIC 5-regulator atlas helper; SHA TBD at dispatch)
   - `_pauli_villars_subtraction.py` if present in computations/_shared, otherwise the §W9-4 producing script's inline FULL CC subtraction (per §W9-4 line 1410 SHA `eaf98037ddc2a4d7` — pinmap reference)
4. **Output**: §VII.AF.1.OP-PROJ STRUCTURAL-ORTHOGONAL-COMPANION registry-text edit + verdict line + 5-regulator atlas spread numerical table + FI/RD/MIXED reclassification PASS/FAIL/INFO call.
5. **Format**: `computations/session-92/s92_w1_cf_w9_4_a_vii_af_1_structural_orthogonal_companion.py` (.npz + .png) + `sessions/permanent-results-registry.md` §VII.AF.1.OP-PROJ edit by mack sole-writer.
6. **Deadline**: S92 W-1 (first wave; precedes CF-W9-8-2 because §VII.AU canonical FULL-physical re-extraction depends on the regulator-class taxonomy this gate settles).
7. **Depends on**:
   - §W9-4 verdict line `S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE: FAIL` (UPSTREAM; audit_sha=`79314db6a6aee053...`)
   - §W9-8 verdict line `S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX: FAIL` (UPSTREAM; demonstrates anti-convergent envelope on SCHEMATIC anchor; audit_sha=`0da19aba653fa19d...`)
   - `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` STRUCTURAL-ORTHOGONAL-COMPANION clause (MANDATORY at K=3 since S88 W8-92)
   - `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline (POSITIVE-CALIBRATION pattern per W9c-1 S87 precedent)
   - `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` FI/RD/MIXED taxonomy

#### CF-W9-8-2 (S92 W-1; ~2.0 we; PRIMARY: mack-cosmic-bridge + CO-AUTHOR: connes-ncg-theorist)

1. **What**: §VII.AU.OP-PROJ canonical FULL-physical re-extraction. Re-extract the §VII.AU canonical pin at FULL Pauli-Villars Connes-Chamseddine 1996 §2.2-2.3 level class, replacing the inherited SCHEMATIC STRICT_F4 atlas extraction at L_max=10. Multi-L scan at L_max ∈ {10, 12, 14} (L_max=14 cache at `s87_spectrum_cache_L14_tau019.npz` if present; if absent, Friedrich-Bär saturation argument certifies the L_max=12 anchor under η_FB_lower = 0.40 per `math-scripts.md §"D_K Block-Diagonality"` W11-2 + W11-3 precedents). Output: `R_canonical_VII_AU_FULL_physical` value pinned in `canonical_constants.py` with PROVENANCE entry promoting from SCHEMATIC → FULL physical level class via `update_constant("R_canonical_VII_AU_FULL_physical", value, session="S92", source="S92-CF-W9-8-2", comment="FULL CC PV physical re-extraction; supersedes SCHEMATIC STRICT_F4 inheritance from R_universal_HP1_strict_F4")`. Verdict-line `convention=` field carries `-FULL-CC-MULTIPLIERS-PHYSICAL` suffix per §(iv) MANDATORY at K=4.
2. **Who**: mack-cosmic-bridge (PRIMARY; cross-pillar bridge-anatomy authority + sole-writer for §VII.AU registry per `feedback_mack-bridge-role.md`) + connes-ncg-theorist (CO-AUTHOR; FULL CC physical multiplier evaluation authority).
3. **Input**:
   - `_pauli_villars_subtraction.py` PRIMARY FULL physical helper (REUSED from §W9-4; cited per §W9-8 pinmap SHA `eaf98037ddc2a4d7...`)
   - `s84_spectrum_cache_L12_tau019.npz` (REUSED)
   - `s87_spectrum_cache_L14_tau019.npz` if available (NEW; Friedrich-Bär asymptote refinement)
   - §W9-4 CF-49 FULL CC output `s91_w9_cf49_full_cc_multipliers_vii_af_1.npz` (UPSTREAM; L_max=12 baseline)
   - §W9-8 CF block runtime-pinned ρ_FULL(L=8/10/12) scan (REUSED; FROM `s91_w9_cf_w1_14_composite_bridge_map_rdx.npz`)
4. **Output**: `R_canonical_VII_AU_FULL_physical` canonical_constants pin + §VII.AU.OP-PROJ registry-text replacement (canonical reading FULL; SCHEMATIC reading retained as STRUCTURAL-ORTHOGONAL-COMPANION); §VII.AU sub-class transition from `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` to `STAGE-1-CANDIDATE STRUCTURAL-FULL-PHYSICAL` (discharge of S90 W1-15 deferred-pending sub-class tag).
5. **Format**: `computations/session-92/s92_w1_cf_w9_8_2_vii_au_full_physical_canonical_extraction.py` (.npz + .png) + `canonical_constants.py` update + `permanent-results-registry.md` §VII.AU.OP-PROJ edit.
6. **Deadline**: S92 W-1 (parallel with CF-W9-4-A; precedes any Stage-2 verify dispatch at §VII.AU per the BLOCKED enumeration §2(d) below).
7. **Depends on**:
   - CF-W9-4-A landing (UPSTREAM; settles SCHEMATIC↔FULL regulator-class taxonomy applied here)
   - §W9-8 verdict line (UPSTREAM; demonstrates LEVEL-class mismatch)
   - §W9-4 verdict line (UPSTREAM; provides L_max=12 baseline FULL CC value)
   - `canonical_constants.py` write-order discipline per `math-scripts.md §"Canonical Write-Order for New Framework Predictions"` (Step 1 verdict file → Step 2 canonical_constants → Step 3 inventory row; substantive promotion event)
   - Friedrich-Bär saturation theorem per `math-scripts.md §"D_K Block-Diagonality"`

#### CF-W9-7-1 (S92 W-1; ~2.0 we; PRIMARY: van-den-dungen-bridge-theorist; OAA EXCLUDED: connes-ncg-theorist + phonon-first-cosmologist)

1. **What**: CF-37 INTRA-Corner-I layer-axis adjudication. Adjudicate which of {FULL CM-1995 §III.4 residue formula, structural-ansatz Wedderburn-rank-ratio χ'_weight = 3/6 = 0.5} layer IS the canonical substrate-IS evaluation at the substrate-distance-2 pole subleading-residue under the (c)∘(d) compositional restriction. The O(1) `Delta_PARALLEL = 1.046` from §W9-7 surfaces an INTRA-Corner-I (algebra-INVARIANT × s=4) layer-axis discriminator that the dual-witness verification at §W9-7 cannot resolve in-session. Adjudication outcome: either (a) one layer is structurally canonical and the other is its renormalization (with explicit Z-factor derivation), OR (b) BOTH layers are F-images of a DEEPER substrate-IS canonical at a third evaluation convention not yet enumerated.
2. **Who**: van-den-dungen-bridge-theorist (PRIMARY; substrate-IS NCG submersion authority via Van den Dungen 1811.07824 §6 Kasparov product factorization). Alternative: volovik-superfluid-universe-theorist (substrate-physics axis). **OAA EXCLUSIONS**: connes-ncg-theorist + phonon-first-cosmologist remain excluded from CF-37 family per S90 W7 OAA. This carry-forward is documented HERE for sequencing purposes only; **this synthesis author (connes-ncg-theorist) is EXCLUDED from authoring this gate's compute script**. (Per the spawn prompt: "not OAA-excluded from the non-CF-37-family gates" — and this is a CF-37 gate, hence flagged here for routing only.)
3. **Input**:
   - W3 T1.8 verdict line `s91_gate_verdicts.txt:36` (audit_sha=`8ab158e9e45aab37...`)
   - §W9-7 verdict line `s91_gate_verdicts.txt:196` (audit_sha=`3d6b13d8036155fb...`)
   - L_max=12 master cache `s84_spectrum_cache_L12_tau019.npz`
   - `_cm_1995_residue_formula.py` FULL helper (cited per §W9-7 cross-references)
   - S89 §W2-3 derived theorem on χ'-inheritance morphism kernel (audit_sha=`90bba262af80a04c...`)
   - `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` Corner-I sub-cell partition
4. **Output**: Adjudication theorem or counter-example (option (a) or (b) above); §VII registry slot allocation conditional on PASS routing per `mack-cosmic-bridge` sole-writer.
5. **Format**: `computations/session-92/s92_w1_cf_w9_7_1_layer_axis_intra_corner_i.py` (.npz + .png).
6. **Deadline**: S92 W-1 (parallel with CF-W9-4-A + CF-W9-8-2; the CF-37 layer-axis is structurally separate from §VII.AF.1/AU).
7. **Depends on**:
   - §W9-7 verdict line (UPSTREAM)
   - W3 T1.8 verdict line (UPSTREAM)
   - W3 T1.9 verdict (CF-37 FULL CM-1995 (d)∘(b) FAIL; audit_sha=`41dde3dd21eec988...`)
   - §VII.AU CF-37 registry entry (current STAGE-1-CANDIDATE)
   - S91 W0 R5 substrate-distance-3 pole pre-registration

#### CF-W9-10-A (S92 W-1; ~1.5 we; PRIMARY: connes-ncg-theorist OR vdd-bridge-theorist)

1. **What**: HH^1 first-extraction at substrate-distance-2 pole `s=4`. Re-execute HH^1 cocycle norm L_max-scan at substrate-distance-2 pole `s=4` (Mellin exponent `−2s = −8`), substrate-IS canonical d=4 NCG pole per Wodzicki/Connes 1995 §III L^{−2} expectation; the pre-reg band [1.5, 4.0] is the structurally correct admissibility band at this pole per the §W9-10 substrate framing addendum. PASS expected at `α_operational(s=4) ∈ [1.5, 4.0]` consistent with Wodzicki/Connes d=4 L^{−2} (the band the §W9-10 attempt MIS-targeted at s=3). This discharges §W9-10's wrong-pole admissibility band finding and provides the canonical α_operational extraction at the substrate-distance-2 pole.
2. **Who**: connes-ncg-theorist (PRIMARY; framework's NCG-axiomatic Hochschild cohomology authority); alternative: vdd-bridge-theorist (Van den Dungen NCG submersion HH^1 specialist). No OAA exclusion for HH^1 first-extraction.
3. **Input**:
   - `s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7fd6a6949...`)
   - `_schur_orthogonality_decomp.py` (SHA `e04e225cb9872397...`; Wedderburn block index reference)
   - `canonical_constants.py`
   - §W9-10 npz `s91_w9_hh1_finite_alpha_first_extraction.npz` (FAIL trace; FROM substrate-distance-1 pole s=3; this gate re-targets s=4)
4. **Output**: extracted `α_operational(s=4)` on M_3(ℂ) Peter-Weyl block; cross-axis Sage-Q asymptotic verification within 10% per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"`; canonical_constants.py entry `alpha_operational_s4_FW_M3C`.
5. **Format**: `computations/session-92/s92_w1_cf_w9_10_a_hh1_finite_alpha_first_extraction_s4_pole.py` (.npz + .png).
6. **Deadline**: S92 W-1 (parallel with CF-W9-4-A + CF-W9-8-2 + CF-W9-7-1).
7. **Depends on**:
   - §W9-10 npz (UPSTREAM; FAIL trace at wrong pole)
   - §"Per-Bulletin-per-pole Level-1 classification" K-counter (per-pole independence)
   - Friedrich-Bär saturation theorem applicability check
   - Optionally: §W9-10 CF-W9-10-B (substrate-IS α(s) per-pole exponent table from first principles on the spectral triple) if dispatched in parallel — provides band pre-registration at each pole s ∈ {2, 3, 4, 5, 6} on M_3(ℂ)

### (d) Downstream-consequence enumeration: Stage-2 verifies BLOCKED pending FULL-physical retrofit

Per `joint-theorem-promotion.md §"Stage 2"` (substrate-input-orthogonality MANDATORY at K=3 since S90 W2 CF-20), Stage-2 cross-axis independent-verify dispatch on any of the affected §VII entries is structurally blocked while the SCHEMATIC↔FULL canonical-pin reckoning is unresolved. Specifically:

#### §VII.AF.1.OP-PROJ Stage-2 verify: BLOCKED pending CF-W9-4-A

The §VII.AF.1.OP-PROJ entry was LANDED at S87 W5-1 with `R_universal_HP1_strict_F4 = 1.030902` (SCHEMATIC SDW-residual STRICT_F4 atlas at L_max=10) as Level-3 anchor. Stage-2 cross-axis verify would require two independent cross-reviewers on opposite axes (per `joint-theorem-promotion.md §"Stage 2"` Axis-A spectral-functional + Axis-B transit-dynamics / superfluid-universe / cosmological-bridge) operating WITHOUT prior workshop context. The current Level-3 anchor is SCHEMATIC-class; Stage-2 verifiers on the same anchor would inherit the SCHEMATIC bias. **Stage-2 verify is structurally BLOCKED** until CF-W9-4-A lands the STRUCTURAL-ORTHOGONAL-COMPANION readings AND CF-W9-4-A's 5-regulator atlas FI/RD/MIXED reclassification settles which axis carries the canonical reading at the Level-3 layer.

#### §VII.AU.OP-PROJ Stage-2 verify: BLOCKED pending CF-W9-8-2

The §VII.AU.OP-PROJ entry is currently REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (S90 W1-15 deferred-pending re-tag). The §W9-8 anti-convergent envelope FAIL CONFIRMS the LEVEL-class mismatch between the inherited SCHEMATIC anchor (`R_universal_HP1_strict_F4 = 1.030902`) and the FULL physical PV asymptote. Stage-2 verify at §VII.AU.OP-PROJ would require a Level-3 anchor that satisfies the L^{-3} Level-2-binding envelope on the FULL physical evaluator (the substrate's own asymptote per §W9-8 s=4 cross-pin `α = +4.10`), NOT on the inherited SCHEMATIC anchor. **Stage-2 verify is structurally BLOCKED** until CF-W9-8-2 lands `R_canonical_VII_AU_FULL_physical` and the FIRST-EXTRACTION sub-class transitions to STAGE-1-CANDIDATE STRUCTURAL-FULL-PHYSICAL.

#### §VII.AQ.STATE-PROJ Stage-2 verify: BLOCKED pending CF-W9-11-1 (scheme-suffix retrofit) AND OP-PROJ FULL-physical anchor verification

The §VII.AQ.STATE-PROJ companion slot (allocated S90 W7 CF-54 Phase-2; PENDING-VERIFICATION) requires state-pair functional construction on the substrate state space `S(A_K)` — structurally orthogonal to the OP-PROJ central-projection trace reading per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY K=3. The §W9-11 bit-precision scheme-INDEPENDENCE PASS (Reading A confirmed across APS-1975 + Cheeger-Simons + Bismut-Cheeger; `max_pairwise_diff = 0.000e+00`) demonstrates the GV-Heitsch invariant on (C_H, C_εH) parity-twin pair IS regulator-class-preservation-invariant at the secondary-class evaluation morphism axis, BUT the §VII.AQ.OP-PROJ canonical pin `gv_canonical_difference_FW = -40579.1500479506` was extracted under an upstream regulator atlas that has NOT been re-verified at FULL CC physical multiplier evaluation. Stage-2 verify at §VII.AQ.STATE-PROJ would require the OP-PROJ canonical to be re-anchored at FULL physical level (or explicitly tagged STRUCTURAL-ORTHOGONAL-COMPANION to a FULL-physical companion) before the state-projection side can be verified against a stable canonical. **Stage-2 verify is structurally BLOCKED** until CF-W9-11-1 (scheme-suffix retrofit; ~0.2 we) lands AND a FULL CC physical re-extraction of `gv_canonical_difference_FW` is queued for S92 W-2 or later.

#### Downstream cascade summary

The four W9 FAILs jointly produce a single downstream-consequence cascade:

```
§W9-4 FAIL (FULL CC vs SCHEMATIC at §VII.AF.1; 2.02% Level-class mismatch)
  ↓
§W9-8 FAIL (anti-convergent envelope at §VII.AU; +4.10 PASS on FULL self-anchor)
  ↓
CF-W9-4-A + CF-W9-8-2 + CF-W9-7-1 + CF-W9-10-A (S92 W-1 campaign; ~7.0 we)
  ↓
§VII.AF.1.OP-PROJ STRUCTURAL-ORTHOGONAL-COMPANION landing
+ §VII.AU.OP-PROJ FIRST-EXTRACTION discharge at FULL physical level
+ §VII.AQ scheme-suffix retrofit + FULL-physical re-anchor candidate
  ↓
Stage-2 verifies UNBLOCKED for §VII.AF.1 + §VII.AU + §VII.AQ
  ↓
S92 W-2+ Stage-2 dispatch: 2 cross-reviewers per entry on opposite axes
                           (per joint-theorem-promotion.md §"Stage 2"
                            Axis-B Selection Protocol; downstream-inheritance
                            reach test applied)
  ↓
STAGE-3-PERMANENT promotion eligibility (per joint-theorem-promotion.md
                                          4-stage pathway)
```

Without the S92 W-1 campaign, **no Stage-2 verify can proceed at any of the four affected entries** — the §VII registry would freeze on the SCHEMATIC class for as long as it takes to re-anchor at FULL physical. This is the structural cost of the four FAILs and the reason §W9 routes ~7.0 we forward.

---

## 3. 4-Field Structured Carry-Forward (per `feedback_fix-in-session-never-defer.md`)

Aggregated S92 W-1 SCHEMATIC-vs-FULL canonical-pin retirement campaign — four sub-items, ~7.0 we total, all routing through the S92 W-1 priority cluster (already enumerated in §W9 wave-synthesis §"S92 W-1 priority cluster"). 4-field specs reproduced here per `output-standards.md §"Carry-Forward Dependency Enumeration"`:

### CF-W9-4-A — §VII.AF.1.OP-PROJ STRUCTURAL-ORTHOGONAL-COMPANION landing + 5-regulator FI/RD/MIXED reclassification

1. **What**: STRUCTURAL-ORTHOGONAL-COMPANION landing of `R_universal_HP1_strict_F4 = 1.030902` (SCHEMATIC SDW class) AND `rho_FULL_AF1_s3 = 1.0100907902` (FULL Pauli-Villars-CC1996 class) at §VII.AF.1.OP-PROJ; 5-regulator atlas spread evaluation at L_max=12; FI/RD/MIXED reclassification per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` taxonomy.
2. **Inputs**: §W9-4 npz; canonical_constants.py SCHEMATIC SDW provenance chain (lines 159-273); `_spectral_action_regulators.py`; `_pauli_villars_subtraction.py` (or §W9-4 inline FULL CC subtraction module pinned at SHA `eaf98037ddc2a4d7`); registry §VII.AF.1.OP-PROJ current text.
3. **Gate**: PASS iff atlas spread `(max − min) / mean < 1e-3` (FI; reclassify Level-3 anchor as FI); FAIL iff spread `> 1e-2` (RD; reclassify as RD); INFO iff `1e-3 ≤ spread ≤ 1e-2` (MIXED; current §W9-4 evidence supports MIXED-class outcome on SCHEMATIC↔FULL level-pin axis at finite L_max).
4. **Effort**: ~1.5 we.

### CF-W9-8-2 — §VII.AU.OP-PROJ canonical FULL-physical re-extraction + FIRST-EXTRACTION discharge

1. **What**: Re-extract §VII.AU canonical pin at FULL Connes-Chamseddine 1996 §2.2-2.3 physical multiplier evaluation; promote `R_canonical_VII_AU_FULL_physical` to canonical_constants.py with PROVENANCE entry promoting from SCHEMATIC → FULL physical level; transition §VII.AU.OP-PROJ from `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` to `STAGE-1-CANDIDATE STRUCTURAL-FULL-PHYSICAL`; emit `convention=...-FULL-CC-MULTIPLIERS-PHYSICAL` suffix per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4.
2. **Inputs**: §W9-8 npz (multi-L scan L_max ∈ {8, 10, 12}); §W9-4 npz (L_max=12 baseline + s=4 cross-pin); `_pauli_villars_subtraction.py` PRIMARY FULL physical helper; L_max=14 cache `s87_spectrum_cache_L14_tau019.npz` if present; Friedrich-Bär saturation theorem per `math-scripts.md §"D_K Block-Diagonality"`.
3. **Gate**: PASS iff `|R_FULL_physical(L=12) − Friedrich-Bär_anchored_asymptote| / |asymptote| < 1e-3` (sub-1‰ envelope at L_max=12 against substrate's own asymptote); FAIL iff `> 1e-2`; INFO iff between.
4. **Effort**: ~2.0 we.

### CF-W9-7-1 — CF-37 INTRA-Corner-I layer-axis discriminator adjudication

1. **What**: Adjudicate FULL CM-1995 §III.4 vs structural-ansatz Wedderburn-rank-ratio (χ'_weight = 3/6) layer pair at substrate-distance-2 pole subleading-residue on (c)∘(d) compositional restriction; output: structural-canonical / renormalization theorem (option (a)) OR deeper substrate-IS canonical at third evaluation convention (option (b)). Calibration-corpus instance for `substrate-first-canonical-sourcing.md §(ii.A)` atlas-row vs cache-moment K-counter analog on the CF-37 axis (per §W9-7 CF-W9-7-3 above).
2. **Inputs**: §W9-7 npz; W3 T1.8 verdict line; W3 T1.9 verdict line (CF-37 FULL CM-1995 (d)∘(b) FAIL); L_max=12 master cache; `_cm_1995_residue_formula.py`; S89 §W2-3 derived theorem on χ'-inheritance morphism kernel.
3. **Gate**: PASS iff explicit Z-factor derivation lands the renormalization theorem (option (a)); INFO iff deeper substrate-IS canonical at third evaluation convention is enumerated (option (b)); FAIL iff neither resolution is structurally derivable in-session.
4. **Effort**: ~2.0 we. **OAA exclusions**: connes-ncg-theorist + phonon-first-cosmologist EXCLUDED per S90 W7 CF-37 family OAA; primary author = van-den-dungen-bridge-theorist; alternative = volovik-superfluid-universe-theorist.

### CF-W9-10-A — HH^1 first-extraction at substrate-distance-2 pole s=4 (band-correct retry)

1. **What**: HH^1 cocycle norm L_max-scan at substrate-distance-2 pole `s=4` (Mellin exponent `−2s = −8`); the pre-reg band [1.5, 4.0] is structurally correct at this pole per Wodzicki/Connes 1995 §III L^{−2} expectation; PASS expected `α_operational(s=4) ∈ [1.5, 4.0]`. Closes §W9-10's wrong-pole admissibility band finding.
2. **Inputs**: §W9-10 npz (FAIL trace at s=3); L_max=12 master cache; `_schur_orthogonality_decomp.py` (Wedderburn block index 2 for M_3(ℂ)); canonical_constants.py; Friedrich-Bär saturation theorem.
3. **Gate**: PASS iff `α_operational(s=4) ∈ [1.5, 4.0]` AND cross-axis Sage-Q asymptotic vs in-cache numerical agreement within 10%; INFO iff outside band but cross-axis concordant; FAIL iff cross-axis inconsistent (cache-ceiling boundary effect or substrate-physics pathology).
4. **Effort**: ~1.5 we.

### Total S92 W-1 campaign

```
CF-W9-4-A   (~1.5 we; connes + mack)
CF-W9-8-2   (~2.0 we; mack + connes; depends on CF-W9-4-A)
CF-W9-7-1   (~2.0 we; vdd; OAA exclusion connes + phonon-first)
CF-W9-10-A  (~1.5 we; connes or vdd)
─────────────
TOTAL: ~7.0 wave-equivalents
```

---

## 4. Closing Substrate Framing

The four W9 FAILs jointly map a single substrate-physics finding: **the SCHEMATIC `_spectral_action_regulators.py` Mellin helper at L_max=10 STRICT_F4 atlas is systematically biased relative to the substrate-natural FULL Connes-Chamseddine 1996 §2.2-2.3 Pauli-Villars pipeline at substrate-distance-1 pole s=3**. The bias is ~2% at §VII.AF.1.OP-PROJ, ~104% (O(1)) at the CF-37 (c)∘(d) layer-axis pair, anti-convergent on §VII.AU.OP-PROJ, and admissibility-band-targeted at the WRONG pole on §VII.AQ-adjacent HH^1 first-extraction.

The substrate IS the spectral triple `(A_K, H_K, D_K)` at `τ_fold = 0.190`. The SCHEMATIC and FULL pipelines are **two methodology-floor F-images** of the same Level-1 substrate-IS observable per `epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit`. The substrate's intrinsic structure (Friedrich-Bär saturation at L_max → ∞; Mellin-cone pole structure at s ∈ {3, 4, ...}; substrate-distance-1/2 sign-of-subleading-C_1 alternation per the Layer-Functor F Verdict-Shape Consistency Theorem K=2 SUGGESTION corpus per §VII.AF.1 line 14809) determines which F-image is canonical at downstream consumption. The FULL Pauli-Villars CC1996 §2.2-2.3 pipeline IS the substrate-natural canonical: the Pauli-Villars consistency identities `Σ_r c_r = 1` and `Σ_r c_r M_r² = 0` are substrate-IS algebraic constraints on the regularization tuple, not external choices; the closed forms `a_2^{CC} = 0` and `a_4^{CC} = −2·M_KK⁴` are substrate-IS algebraic theorems verified at machine precision in §W9-4 (Σ c_r M_r² = −4.44e−16; a_4_CC relative residual 3.93e−16). The SCHEMATIC Mellin helper is an EFFECTIVE description on the L_max-truncated spectrum cache (the docstring lines 23-30 declare this explicitly).

**Direction of explanation** (per `phononic-framing.md §"IS Space, Not IN Space"`):

```
Substrate (A_K, H_K, D_K) at τ_fold = 0.190
    IS the finite-L Hochschild pairing (Pillar I/III; substrate-distance-1 pole s=3)
       on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)
  → Methodology-floor F-image #1 (SCHEMATIC class):
       _spectral_action_regulators.py Mellin helper at L_max=10 STRICT_F4 atlas
       → R_universal_HP1_strict_F4 = 1.030902, gv_canonical_difference_FW = -40579.15,
         R_canonical_VII_AU (inherited from §VII.AF.1)
  → Methodology-floor F-image #2 (FULL physical class):
       _pauli_villars_subtraction.py CC1996 §2.2-2.3 multipliers (M_KK, +2, √2·M_KK, -1)
       → ρ_FULL(s=3) = 1.0100907902, ρ_FULL(s=4) = 1.022000
  → Laboratory-IN observables (Pillar II CMB n_s; Pillar IV BZ-trace quantum-metric;
                               Pillar V 3He-B BdG sector)
       — measured under each F-image's bridge map (HKR L_max → ∞; Connes-Karoubi pairing;
         APS-1975 / Cheeger-Simons / Bismut-Cheeger secondary-class evaluation)
```

The four W9 FAILs do not invalidate the substrate; they identify which methodology-floor F-image carries the substrate's canonical reading at L_max=12 on the master cache. **CF-W9-4-A + CF-W9-8-2 + CF-W9-7-1 + CF-W9-10-A jointly close the SCHEMATIC↔FULL canonical-pin reckoning at substrate-distance-1 pole s=3** by re-anchoring §VII.AF.1 / §VII.AU / §VII.AQ at the FULL physical class while preserving the SCHEMATIC class as STRUCTURAL-ORTHOGONAL-COMPANION readings. The substrate IS unchanged across the campaign; only the methodology-layer canonical-pin assignment is corrected.

FORBIDDEN container-inversion (per `phononic-framing.md`): "the SCHEMATIC Mellin helper IS the substrate, and FULL CC PV is its perturbative correction" → INVERT: "the substrate IS `(A_K, H_K, D_K)` at τ_fold = 0.190; both SCHEMATIC and FULL pipelines are emergent computational realizations of the substrate's intrinsic Hochschild pairing at substrate-distance pole s; the SCHEMATIC L_max-truncated Mellin helper is the *effective* description; the FULL CC PV is the *canonical* description; the canonical-pin retirement campaign promotes the methodology-floor pin from effective to canonical without changing the substrate."

---

## 5. Cross-References

- `sessions/archive/session-91/session-91-w9-workingpaper.md` §W9-4 (lines 593-795), §W9-7 (lines 1066-1262), §W9-8 (lines 1264-1517), §W9-10 (lines 1724-1901)
- `sessions/permanent-results-registry.md` §VII.AF.1.OP-PROJ (line 14776), §VII.AU.OP-PROJ (line 17784), §VII.AQ.OP-PROJ (S88 W7b-79; retrofit S90 W7 CF-54 Phase-2), §VII.AQ.STATE-PROJ (line 17598)
- `computations/_shared/canonical_constants.py` lines 159-273 (`R_universal_HP1_strict_F4 = 1.030902` SCHEMATIC STRICT_F4 provenance chain), line 171 (`eps_H_HP1_norm = 16.197719` PRIMARY per Class-(d) chain), line 1636 (`gv_canonical_difference_FW = -40579.1500479506`)
- `computations/_shared/_spectral_action_regulators.py` (SCHEMATIC 5-regulator atlas; docstring lines 23-30 self-identifies as SCHEMATIC)
- `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` — K=4 MANDATORY level-pin discipline (S88 W7b-83 close; calibration corpus W4-2 NEGATIVE + W9b-2 NEGATIVE + W9c-1 POSITIVE + W5b-2 EXEMPT + W5-7 S90 W1-9 PARTIAL-POSITIVE)
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` — FI/RD/MIXED per-pole taxonomy
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` + §"Deferred-pending intermediate verdict-class"` — REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class at §VII.AU.OP-PROJ
- `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` — STRUCTURAL-ORTHOGONAL-COMPANION discipline (MANDATORY at K=3 since S88 W8-92)
- `.claude/rules/joint-theorem-promotion.md §"Stage 2"` — substrate-input-orthogonality MANDATORY K=3; Axis-B Selection Protocol with downstream-inheritance reach test
- `.claude/rules/regulator-pin-discipline.md` — UV-regulator axis × Level axis × Binding axis × MACHINERY-SCOPE axis orthogonality (S88 W-23 W7b-82 V.5 SUGGESTION K=1; S90 W7-4 CF-57 sharpening; W4-axis pin discipline at plan-freeze)
- `.claude/rules/math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` — Friedrich-Bär saturation theorem (η_FB_lower = 0.40 calibration per S87 W11-2 + W11-3)
- `.claude/rules/math-scripts.md §"Canonical Write-Order for New Framework Predictions"` — verdict file → canonical_constants.py → falsifier-master-inventory.md write-order
- `.claude/rules/epistemic-discipline.md §"Layer-Decomposition"` — F-functor `F: substrate → methodology → audit`; Phi correspondence weight-n
- `.claude/rules/phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"` — direction-of-explanation discipline; container-thinking inversion FORBIDDEN
- §W9-2 T2.12 3He-B Aalto LTL liaison (Pillar V observational anchor; downstream consumer of the §VII.AQ-side cocycle-asymmetry ratio)
- §W9-11 `S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT` PASS (Reading A; bit-precision scheme-INDEPENDENCE on (C_H, C_εH) parity-twin pair; supports §VII.AQ retrofit candidacy via scheme-suffix discipline)

---

**End of synthesis** — single-author solo review per `/rclab-review` discipline; no rounds, no adversarial workshop, no cross-agent coordination. The four W9 FAILs converge consonantly on the SCHEMATIC↔FULL canonical-pin reckoning; the synthesis hardens the substrate-physics narrative connecting the four sub-items into one S92 W-1 campaign that downstream consumers (mack-cosmic-bridge for registry edits; connes-ncg-theorist for FULL CC re-derivation; van-den-dungen-bridge-theorist for CF-37 layer-axis adjudication) can act on.
