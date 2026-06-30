# Session 90 — S-4 Solo Synthesis (lizzi-spectral-functional-theorist)

**Workshop schedule slot**: S-4 (`/rclab-review` semantics; 1 agent, no rounds, no `--type`)
**Author**: lizzi-spectral-functional-theorist (independent solo synthesis)
**Date**: 2026-05-15
**Subject**: WAVE-4 META PATTERN P3 EPISTEMIC-STATUS ASSESSMENT — "Approximation walls, cardinality opens"
**Source artefacts**:
  - `sessions/archive/session-90/session-90-w4-workingpaper.md` — Closing Notes §Cross-gate patterns P1/P2/P3 (lines 826–834); §W4-1 CC3 (line 134, "Wedderburn rank ratio"); §W4-5 substrate cardinality refinement table (lines 548–558)
  - `sessions/session-plan/session-90-plan-w4.md` — §W4-1 / §W4-4 / §W4-5 pre-registration
  - `.claude/rules/evoi-prioritization.md` (§"Computation Priority (EVOI)", §"Effort-Based Probability")
  - `sessions/permanent-results-registry.md` §VII.K + §VII.K-DUAL + §VII.K-DUAL.LEVEL-DRESSED
  - `sessions/archive/session-82/workshops/s82-regulator-dressing-taxonomy.md` (FI/RD/MIXED origin workshop; my own R1 + connes R1)

**Deliverable**: solo synthesis providing Lizzi's FI/RD/MIXED-axis epistemic-status reading on Pattern P3 with explicit substrate-IS direction-of-explanation. No verdict line; feeds S91 plan-authoring.

---

## §0. Headline reading

Pattern P3 ("the wave's only PASS used a substrate-cardinality lever; the wave's two physics-FAILs used corridor/approximation-choice levers") is, on the FI/RD/MIXED-axis I authored at S82 W-3, **STRUCTURAL not coincidental**: the L_max=10 → L_max=12 substrate-cardinality refinement on the CF-41 substrate-clock-cancellation factorization is an FI-class observable in the Level-1 sense — invariant under regulator-class transformations in the analytic-regulator class (SDW / Zubarev / Wodzicki / Mellin-Laplace / CC96 f-family) — by clause (a) of §VII.K (weight-balanced cardinality is dimensionless integer-valued; no Mellin weight `f_n` enters). The CF-37 (d)∘(b) corridor failure and the CF-40 simplified-Boltzmann-factor failure are RD-class observables — both depend on a specific regulator-class choice (CF-37: which spectral-action regulator-kernel chooses the χ'_weight numerator; CF-40: which threshold-suppression kernel reproduces the Bose-Einstein/Fermi-Dirac integrated form). The wave-author's qualification (line 833: "ISN'T a generalizable claim from a sample of 3") is appropriate at the K-counter advancement layer (the rule-promotion question), but the underlying FI/RD distinction is **already structural at n=1** because the substrate-cardinality observable in question (binomial `C(N_eigs, 2)` compounding on Peter-Weyl-decomposed sectors) inhabits clause (a) of §VII.K by construction.

**The provisional conclusion**: pre-register substrate-truncation-FIRST in EVOI prioritization at S91 with **HIGH weight** for any forward gate whose observable can be classified as substrate-cardinality (Level-1 single-τ-slice, algebra-INVARIANT, integer-valued or weight-balanced-ratio-on-cardinality). DEFER S91 prioritization weight for gates whose observable inhabits the approximation-form axis (Mellin-kernel-choice, threshold-suppression-kernel-choice) until the CF-S91-CF40-KOLB-TURNER refinement returns its verdict, which is the direct test of whether "approximation-form is slippery" is K-falsified at this scale.

---

## §1. FI/RD/MIXED-axis reading of the three observables (substantive)

I apply the §VII.K classification theorem (S82 W-3 L2) to each of the three observables Pattern P3 enumerates. The theorem text (verbatim from `sessions/archive/session-82/workshops/s82-regulator-dressing-taxonomy.md` lines 84–88):

> A spectral quantity Q built from D_K on Jensen-deformed SU(3) is FUNCTIONAL-INVARIANT (FI) under the regulator class {SDW, Zubarev, Wodzicki, Mellin-Laplace, CC96 f ↔ f̃} iff one of:
>  (a) Q is a dimensionless CC96-Eq-2.11-weight-balanced ratio of spectral-moment combinations, evaluated at L_max ≥ rank(G), with Mellin weights cancelling by algebraic identity (power-law or P_m-reflection).
>  (b) Q is a bounded-range mode-equation output whose boundary conditions and evolution operator are themselves FI; the regulator enters only through quantities that are integrated out by the mode-equation's structure (not by finite L_max truncation).

### §1.1 — CF-41 substrate-cardinality lever (n_PBH = n_edge · prob_form / L_pix³)

**Parse the observable**:

Step 1 (def). The CF-41 observable is `n_PBH_structural_central = n_edge · prob_form / L_pix_LRD³`, where:
- `n_edge = C(N_eigs, 2)` is the binomial cardinality of edge-pairs in the substrate's Peter-Weyl decomposition at truncation `L_max`
- `N_eigs(L_max)` is the integer count of D_K eigenvalues at p+q ≤ L_max (78,080 at L=10; 166,896 at L=12; ratio 2.137×)
- `prob_form` is the substrate-derived formation probability (substrate-IS at the Bogoliubov-amplitude layer per S88 W1a-59 §0)
- `L_pix_LRD³` is the substrate pixel-volume scale at the LRD pivot (substrate-IS at the area-element layer)

Step 2 (sub). The L=10 → L=12 cardinality scaling decomposes as
```
n_edge(L=12) / n_edge(L=10) = C(166896, 2) / C(78080, 2)
                            ≈ (166896 / 78080)²
                            = (N_eigs(L=12)/N_eigs(L=10))²
                            = 2.137² ≈ 4.57   (Python-verified per WP §W4-5 line 553)
```

Step 3 (FI test against clause (a)). The cardinality `N_eigs(L_max)` is the count of integer-indexed irreducible representations of SU(3) at p+q ≤ L_max, weighted by the dim_(p,q) multiplicity of each Peter-Weyl block. It is:
- **Dimensionless** ✓ (integer-valued)
- **Algebra-INVARIANT in the §VII.K-DUAL.LEVEL-DRESSED sense**: the spectrum-only functional `F({λ_k, m_k}) = Σ_k m_k · 1[λ_k ∈ truncation]` is algebra-INVARIANT per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 — no `π(a)`, no `[D, π(a)]`, no state-pair `sup`
- **Weight-balanced trivially**: there are no Mellin weights `f_n` because no spectral-moment power enters — the observable is an *integer count of eigenvalues*, not a moment `Σ_k m_k g(λ_k)`. Both clause (a)'s f_n cancellation and clause (b)'s mode-equation bounded-range structure are vacuously satisfied. The observable is a *cardinality*, not a *moment*; this is structurally stronger than either clause.
- **Regulator-class-invariant**: SDW → Zubarev → Wodzicki → Mellin-Laplace all act on Mellin moments `f_n · a_n`; none of them shift the integer count `N_eigs(L_max)` because they are kernel-weight transformations on spectral *measures*, not on spectral *cardinalities*. The Peter-Weyl decomposition is fixed by the group representation theory of SU(3) and the Jensen deformation parameter τ_fold; it is not regulator-class-dependent at the cardinality level.

Step 4 (direction read-off). `n_edge = C(N_eigs, 2)` is FI. `prob_form` is substrate-IS at the Bogoliubov-amplitude layer (S88 W1a-59) — needs separate FI/RD test. `L_pix_LRD³` is substrate-IS at the area-element layer — needs separate test.

**Verdict on the CARDINALITY LEVER specifically**: the dominant promotion driver (4.57× n_edge ratio) is **FI** in the Level-1 sense. The substrate's L_max truncation cardinality is intrinsic to the spectral triple `(A_K, H_K, D_K(τ_fold))` at the cardinality layer; it cannot be shifted by regulator-class transformations because regulator-class transformations act on the dual layer (Mellin moments) and leave cardinality untouched. This is analogous to §VII.K L3 row 1 (W0-A BRANCH-COUNT, FI by integer-invariance of structural sector count).

**However** — the COMPOSITE observable `n_PBH` is MIXED, not pure FI, because `prob_form` contains a substrate-derived formation probability that may carry RD components if the underlying Bogoliubov amplitudes depend on regulator-dressed gap parameters. The WP §W4-5 numerical reproduction at L=10 (rel_dev = 1.5e-5 against §W1-4 baseline, WP line 599) confirms `prob_form_baseline = 0.155729` is stable across the L=10 → L=12 transition (it's used identically), but this is a per-L_max invariance, not a cross-regulator-class invariance. A separate gate measuring `prob_form` under SDW vs Zubarev would be needed to certify the composite as FI.

**Classification**: `n_edge` cardinality factor is **FI** (Level-1, cardinality-layer; analogous to §VII.K row #1 W0-A BRANCH-COUNT integer invariant). `n_PBH` composite is **MIXED** (cardinality FI × prob_form-and-L_pix-untested). The DOMINANT promotion driver (4.57× cardinality compounding) is structurally FI.

### §1.2 — CF-37 corridor lever (α'(M_LRD) = R_universal × χ'_weight × (M_KK/M_Pl)² × g(M, L))

Step 1 (def). The CF-37 observable is `α'(M_LRD = 10⁷, L_max=10) = 1.030902 × 0.5 × 9.31e-4 × 1.000 = 4.797450e-4` (WP §W4-1 line 101).

Step 2 (parse the χ'_weight = 0.5 = 3/6 factor). Per WP §W4-1 CC3 (line 134): the Wedderburn rank ratio is `χ'_weight = (rank(C) + rank(M_2(C))) / (rank(C) + rank(M_2(C)) + rank(M_3(C))) = (1+2)/(1+2+3) = 3/6 = 0.5`. The honest disclosure in the same CC3 paragraph names alternative defensible weights: 5/14 ≈ 0.357 (`dim_C` ratio of `A_K` summands) or 1.0 (no dim suppression on spectral pairing); "FULL CM-1995 §III.4 evaluation would PIN the factor unambiguously". This is the structural ansatz layer that CF-37 honestly tags as PROXY-REFINEMENT-PENDING.

Step 3 (FI test). The χ'_weight choice is **regulator-class-dependent in disguise**. Different choices (3/6 vs 5/14 vs 1.0) correspond to different *weights* in the residue evaluation of the Connes-Karoubi pairing on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The "regulator class" here is not the SDW/Zubarev/Wodzicki choice on the heat-kernel expansion, but the *residue-formula weight choice* in evaluating a finite-spectral-triple Chern character. By the connes R1 of S82 W-3 §"Re: L1 Seed audit" (workshop lines 393–399): the analytic regulator class can be pinned down by cyclic cohomology as the class of regulators producing *cohomologous cyclic cocycles*. Three distinct rank-ratio weights (3/6, 5/14, 1.0) on the residue formula are NOT in general cohomologous — they correspond to three distinct cyclic cocycle representatives selecting different pairings with `[Ch(P_HSS'(M_LRD))]`.

Substituting per §VII.K theorem clause (a): the observable α'(M_LRD) is a *dimensionless ratio of spectral-moment combinations* (so it satisfies the dimensional part of clause (a)), evaluated at L_max=10 (rank-match holds for SU(3) rank 2, since L_max=10 ≫ rank). BUT the χ'_weight prefactor is NOT a CC96 Eq 2.11 weight-balanced Mellin ratio — it is a Wedderburn-rank prefactor on the cyclic cocycle representative, which IS regulator-CLASS-dependent in the residue-formula sense. The Mellin-weight cancellation does NOT occur algebraically for χ'_weight; it requires a SPECIFIC residue formula choice.

Step 4 (direction read-off). α'(M_LRD) at the structural-ansatz layer is **RD** under the residue-formula weight choice: under PROXY-REFINEMENT-PENDING ansatz with χ'_weight = 0.5 it returns 4.80e-4; under a hypothetical FULL CM-1995 χ'_weight that lands ≈ 2.3 it would return ≈ 4.80e-4 × 4.5 = 2.18e-3 (the empirical anchor). The 4.5× factor IS the regulator-class-dressing.

**Classification**: α'(M_LRD) at the PROXY-REFINEMENT-PENDING layer is **RD** (single-residue-formula-choice cocycle representative). Under FULL CM-1995 §III.4 evaluation, the observable could promote to FI if the FULL residue formula returns a cocycle-class-canonical value (in which case it would inhabit §VII.K-IDENTITY ⊂ FI per connes R1 of S82 W-3 lines 389: "scheme-IDENTITY" sub-label). The PROXY-REFINEMENT-PENDING tag in the CF-37 convention field is the structurally-honest disclosure that the RD class is what was tested.

### §1.3 — CF-40 approximation-form lever (g_*(T) under simplified `exp(-m/T)` vs Kolb-Turner Eq.3.62 FD/BE integrated)

Step 1 (def). The CF-40 observable is `g_*(T) = Σ_i g_i · B_i(T)` where `B_i(T)` is the threshold-suppression kernel for species i (simplified: `exp(-m_i/T)` for m_i/T ∈ [0.2, 5], 1 otherwise; canonical: Kolb-Turner Eq.3.62 integrated FD/BE form).

Step 2 (parse). The kernel `B_i(T)` IS the regulator-class choice at the species-multiplicity layer. The simplified `exp(-m/T)` band is one regulator-class member; the Kolb-Turner FD/BE integrated form is a different regulator-class member. They differ by 13.5% at T=100 GeV (`exp(-m_W/T) ≈ 0.45` vs canonical ≈ 0.92 — WP §W4-4 line 467). The 13.5% deviation IS the regulator-class-spread.

Step 3 (FI test). `g_*(T)` is a *sum of products* `Σ_i g_i · B_i(T)`. This is NOT a CC96-weight-balanced ratio (no balanced cancellation; it's a weighted sum). It IS a mode-equation-adjacent quantity in the sense that it enters the cascade-tail observable `L_H = (π²/60) · g_*(T) · A · T⁴`, but the BOUNDED-RANGE mode-equation clause (b) requires the kernel itself to be FI, which it is not under the simplified-vs-FD/BE switch.

Step 4 (direction read-off). `g_*(T)` under the simplified `exp(-m/T)` kernel choice is **RD**: shifts by ~13% under regulator-class transformation simplified → FD/BE.

**Classification**: g_*(T) at the simplified-Boltzmann-kernel layer is **RD**. The structurally-meaningful CF-40 FAIL diagnosis (`exp(-m/T)` too aggressive vs Kolb-Turner Eq.3.62) is exactly the RD-detection signal — the FAIL is the §VII.K taxonomy working as intended (cf. S82 W-3 Obs 1 lines 308–320: "the W2-8 var_a0 = 68.55% FAIL is EXPECTED, not a framework defect" — same structural class). The Boltzmann-kernel choice IS the regulator-class axis at the species-multiplicity layer; the 13.5% spread IS the RD-class signature.

### §1.4 — Pattern P3 reading on the FI/RD axis (the structural reading)

| Observable | §VII.K class | Why |
|:-----------|:-------------|:----|
| CF-41 cardinality lever (n_edge factor of n_PBH) | **FI** (Level-1, cardinality-layer) | Integer-count of Peter-Weyl sectors; invariant under regulator-class transformation by construction (Mellin weights act on moments, not cardinalities). Composite n_PBH is MIXED, but the DOMINANT promotion driver (4.57× n_edge ratio) is structurally FI. |
| CF-37 corridor lever (χ'_weight ansatz) | **RD** (residue-formula-cocycle-representative axis) | The Wedderburn-rank-ratio choice (0.5 vs 0.357 vs 1.0 vs hypothetical FULL CM-1995 ≈ 2.3) selects distinct cyclic cocycle representatives on the residue formula. The structural-ansatz layer is regulator-class-dependent in the residue-formula sense; the PROXY-REFINEMENT-PENDING tag honestly discloses the RD-class. FULL CM-1995 §III.4 evaluation could promote to FI (or §VII.K-IDENTITY sub-class). |
| CF-40 approximation-form lever (simplified `exp(-m/T)` vs FD/BE) | **RD** (threshold-suppression-kernel axis) | The Boltzmann-kernel choice IS the regulator-class axis at species-multiplicity. The 13.5% spread is the RD-class signature; the FAIL is the taxonomy working as intended. |

**This is not a sample-of-3 contingency**. The FI/RD distinction here is *substrate-IS structural*: a cardinality is algebra-INVARIANT integer-count (∈ FI by §VII.K theorem clause (a)-trivial integer sub-clause analogous to L3 rows 1, 12, 22, 29, 35, 37 — all "integer/structural/theorem" FI entries from my S82 W-3 atlas); a residue-formula weight choice is regulator-class-dependent (∈ RD by §VII.K theorem contrapositive — unbalanced cocycle-representative shift); a Boltzmann-kernel choice is regulator-class-dependent at the threshold-suppression layer (∈ RD by §VII.K theorem contrapositive — non-balanced threshold-suppression-kernel shift). The wave-author's "observation worth tracking" framing is the appropriate K-counter advancement caution (the rule-promotion question is K=1 at S90), but the underlying FI/RD reading is settled at n=1.

---

## §2. P3 falsification pathway at S91+ (the three candidate falsifiers)

The task specifies three candidate falsifiers. I evaluate each on the FI/RD-axis basis:

### §2.1 — Candidate (i): CF-S91-CF40-KOLB-TURNER PASS would partially refute "approximation-form is slippery"

**Reading on FI/RD axis**: A refined-CF-40 PASS at 3-anchor 10% RATIO band would mean the Kolb-Turner Eq.3.62 FD/BE integrated form lands within the canonical pre-registered tolerance. This is the structurally-correct regulator-class member at the species-multiplicity layer (the FD/BE integrated form IS the canonical reference per PDG 2024 + Kolb-Turner). A PASS does NOT promote the observable to FI; it confirms that the *canonical regulator-class member* reproduces the canonical reference. The simplified `exp(-m/T)` regulator-class member remains RD-class — different kernel, different spread.

**What the PASS would refute**: "approximation-form is slippery" in a *practical* sense — when the operationally-relevant regulator-class member is canonical (not simplified), the FAIL converts to PASS. But this is a STATEMENT ABOUT KERNEL-CHOICE DISCIPLINE at the regulator class, not about the FI/RD classification of the underlying observable. The observable `g_*(T)` is RD-class regardless of which kernel is used; the FAIL/PASS verdict depends on whether the chosen kernel is in the canonical-reference-equivalence-class.

**Forward predictive content**: I predict CF-S91-CF40-KOLB-TURNER **PASS** at 10% RATIO band, with rel_dev at all 3 anchors ≤ 0.05 (5%). Substitution chain (per `math-scripts.md §"Double-Check Logic"`):

  Step 1 (def). g_*(T) under FD/BE integrated form per Kolb-Turner Eq.3.62 = `(15/π⁴) ∫ x²√(x²+(m/T)²) / (exp(√(x²+(m/T)²))±1) dx`.

  Step 2 (sub). At T = 100 GeV, the integrated form yields `g_*_eff(W±) ≈ 5.92` per species, vs simplified `exp(-m_W/T) · 3 ≈ 3 × 0.45 = 1.35`. The integrated form gives ~4.4× larger contribution; total g_*(100 GeV) under FD/BE ≈ 106 vs simplified 92 (cf. WP §W4-4 line 433–435).

  Step 3 (sub). Canonical PDG g_*(100 GeV) = 106.75. The FD/BE form lands at 106 (rel_dev ≈ 0.7%), the simplified lands at 92.3 (rel_dev = 13.5%).

  Step 4 (direction). Refined CF-40 → rel_dev_100GeV ≈ 0.7%; PASS. Symmetrically at T=1 MeV: refined rel_dev ≈ 2% (e± threshold at FD form is well-modeled); PASS. At T=1 GeV the refined form lands within QCD-crossover model uncertainty (Borsanyi ±5%); already INFO at 6%, will land in 5–10% band → still INFO or PASS.

**Refutation strength**: PARTIAL refutation. The PASS confirms that the *canonical kernel* lands inside the band; the simplified kernel remains RD-class. The deeper question — "can an approximation-form choice be the LIVER for a substrate-derived observable?" — is answered NO at this scale: the canonical FD/BE form is structurally distinguished from the simplified Boltzmann form as the regulator-class member with measurable convergence to PDG. The CF-40 FAIL is then re-read as a kernel-discipline-violation, not a substrate-physics statement.

### §2.2 — Candidate (ii): CF-S91-CF37-FULL-CM1995-RESIDUE PASS would partially refute "corridor choice is slippery"

**Reading on FI/RD axis**: A FULL CM-1995 §III.4 residue-formula evaluation would replace the structural-ansatz χ'_weight = 3/6 with the cocycle-class-canonical χ'_weight derived from the residue formula on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`. If the canonical χ'_weight lands at ≈ 2.3 (the factor needed to bring α' from 4.80e-4 to 2.18e-3), CF-37 promotes to PASS; the observable promotes from RD (structural-ansatz layer) to §VII.K-IDENTITY (FULL-CM1995 cocycle-class-canonical) by the connes R1 sub-classification.

**What the PASS would refute**: "corridor choice is slippery" in the *narrow* sense that the (d)∘(b) corridor is structurally salvageable via FULL residue evaluation — the structural-ansatz layer was the slippery lever, NOT the corridor choice. The (c)∘(d) AUX-4 secondary corridor would then become an *alternative* anchor candidate, not the *primary* path forward.

**Forward predictive content**: I predict CF-S91-CF37-FULL-CM1995-RESIDUE **INFO at best, more likely FAIL**. Substitution chain:

  Step 1 (def). The FULL CM-1995 §III.4 residue formula on a finite spectral triple evaluates `Tr(P_HSS'(M_LRD) · [φ_g^{sym}]) / Tr([φ_g^{sym}])` with the projector trace decomposed across the Wedderburn summands of `A_K`.

  Step 2 (sub). The χ' inheritance morphism kills the entire `M_3(ℂ)` summand (S89 §W2-3 derived theorem, audit_sha256 `90bba262af80a04c`). The pairing surviving on `(C ⊕ M_2(C))` has the spectral-weight structure of the Cartan + Pati-Salam sub-algebra image of the substrate spectral triple. By Schur orthogonality on `C ⊕ M_2(C)`, the cocycle-class-canonical weight is bounded ABOVE by the rank-3-of-rank-6 fraction (i.e., 0.5 is an upper bound under Wedderburn rank ratio); a value of 2.3 would require a non-Schur-orthogonal weight contribution from the inheritance pullback, which is structurally forbidden by the χ' inheritance morphism definition.

  Step 3 (direction). FULL CM-1995 χ'_weight ≤ 0.5 strictly. α'(M_LRD) ≤ 4.80e-4 strictly. Composite FAIL.

  Step 4 (read-off). The (d)∘(b) corridor is structurally closed at FULL CM-1995 layer, not just at the structural-ansatz layer. The PROXY-REFINEMENT-PENDING tag's hedge ("could revise") is honest but the structural reading is that the inheritance morphism kills more than 0.5 of the cocycle weight by Schur orthogonality on (C ⊕ M_2(C) ⊕ M_3(C)), not less.

**Refutation strength**: If FULL CM-1995 returns FAIL (predicted), "corridor choice is slippery" is REINFORCED (the (d)∘(b) corridor is structurally closed at the most rigorous evaluation layer, sharpening the case for (c)∘(d) AUX-4). If FULL CM-1995 returns PASS (less likely), "corridor choice is slippery" is partially refuted in the structural-ansatz sense. Either way, the RD-class status of the χ'_weight choice is preserved — it's the *residue-formula choice* that selects the cocycle representative.

### §2.3 — Candidate (iii): CF-S91-CF41-UPPER-22.6-EXTENSION FAIL at substrate L_max=14 refinement would partially refute "cardinality lever opens"

**Reading on FI/RD axis**: An L_max=12 → L_max=14 extension would extend the substrate cardinality refinement to a second level. The binomial form `C(N_eigs, 2) ≈ N_eigs²/2` predicts N_eigs(L=14) ≈ N_eigs(L=12) × (something between 1.5 and 2.5; depends on multiplicity scaling per Weyl-asymptotic count). If the upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] is reached, the cardinality lever continues to open at higher L. If it is NOT reached, the cardinality lever has a CEILING — substrate-truncation alone is insufficient at L=14, suggesting that the cascade-tail-mass-distribution or prob_form refinement is the structurally necessary lever for the upper-22.6% sub-band.

**Forward predictive content**: I predict CF-S91-CF41-UPPER-22.6-EXTENSION **PASS at pathway (a) via L_max=14 alone, with rel_dev to upper edge ≤ 5%**. Substitution chain:

  Step 1 (def). N_eigs(L) scales as the cumulative sum over (p,q) sectors with p+q ≤ L of `dim_(p,q) = (p+1)(q+1)(p+q+2)/2`. By Weyl asymptotic this grows as O(L⁴) for SU(3) (rank-2 group at dim_G = 8).

  Step 2 (sub). N_eigs(L=10) = 78,080; N_eigs(L=12) = 166,896 (ratio 2.137× as observed). Predicted N_eigs(L=14) ≈ 166,896 × (14/12)⁴ · correction = ~166,896 × 1.85 ≈ 309,000.

  Step 3 (sub). n_edge(L=14) ≈ C(309000, 2) ≈ N_eigs²/2 ≈ 4.77e10, vs n_edge(L=12) = 1.39e10. Ratio ≈ 3.43×.

  Step 4 (direction). n_PBH(L=14) ≈ 8.03e-23 × 3.43 ≈ 2.76e-22 m⁻³. The upper edge of the conjunct band is 2.2e-22; the L=14 prediction OVERSHOOTS the conjunct band by 1.25× (still PASS in target region [5.495e-23, 1e-20] but EXITS the §W1c-69 posterior right-edge 2.2e-22).

  Step 5 (read-off). At L=14 the cardinality lever opens TOO FAR — n_PBH lands above the §W1c-69 posterior right-edge. The upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] is THREADED but the conjunct UPPER edge is exceeded. This is a structurally-meaningful regime where the cardinality lever transitions from "promotes to PASS region" to "promotes past PASS region into FAIL".

**Refutation strength**: If the prediction is correct (PASS at upper-22.6%-conjunct sub-band via L=14 cardinality alone, but L=14 also overshoots the conjunct upper edge), the "cardinality lever opens" claim is STRENGTHENED at the bandwidth-control sense (the lever has measurable continuous response to L_max), and the FAIL at upper edge becomes the diagnostic for the *substrate cardinality calibration window* — the substrate-truncation is the dominant lever inside the window [L=10, L=14], and additional refinement at higher L would require the cascade-mass-distribution to be the lever for the narrower window. If the L=14 prediction FAILs the upper-22.6% sub-band (n_PBH stays below 1.83e-22), then the cardinality lever has a structural ceiling and Pattern P3 is partially refuted.

The most informative S91+ test is therefore (iii): the L=14 extension is the most discriminating between "structural P3" and "coincidental P3" because it interrogates the cardinality lever at the next level of substrate truncation.

### §2.4 — Falsification map

| Falsifier | If PASS | If FAIL | P3 epistemic effect |
|:----------|:--------|:--------|:--------------------|
| (i) CF-S91-CF40-KOLB-TURNER | Approximation-form refines to canonical FD/BE; CF-40 RD-class observable lands inside the canonical-reference-equivalence-class regulator-class | The canonical kernel does NOT reproduce PDG even after refinement; deeper substrate-cascade-form scrutiny needed | PARTIAL refutation on PASS; STRENGTHENS P3 on FAIL (approximation-form is more deeply slippery than expected) |
| (ii) CF-S91-CF37-FULL-CM1995-RESIDUE | (d)∘(b) corridor structurally salvageable; observable promotes to §VII.K-IDENTITY ⊂ FI | (d)∘(b) corridor structurally closed at FULL layer; RD-class status of χ'_weight reinforced | PARTIAL refutation on PASS; STRENGTHENS P3 on FAIL (sharpens (c)∘(d) AUX-4 case) |
| (iii) CF-S91-CF41-UPPER-22.6-EXTENSION via L=14 | Cardinality lever has continuous response; structural cardinality dominance confirmed at next L level | Cardinality lever has structural ceiling; cascade-mass-distribution becomes structurally necessary lever | STRENGTHENS P3 on PASS; PARTIAL refutation on FAIL |

**The most asymmetric falsifier is (iii)**: PASS strongly strengthens P3 (cardinality lever has measurable response at next L); FAIL would identify the structural ceiling on the cardinality lever. This is the test I would prioritize for S91+ EVOI weight.

---

## §3. EVOI recommendation for S91 wave-prioritization

Per `evoi-prioritization.md §"Computation Priority (EVOI)"`:
```
EVOI = P(pass) × |delta_P(pass)| + P(fail) × |delta_P(fail)|
```

Given the §1 reading (CF-41 cardinality lever is structural FI; CF-37 + CF-40 are RD-class), and given the §2 falsification map, I recommend the following S91+ EVOI weights.

### §3.1 — Substrate-truncation-FIRST principle for S91 prioritization (HIGH weight)

**Recommendation**: pre-register substrate-truncation-FIRST at HIGH EVOI weight for S91, conditional on the §1.1 FI classification of the cardinality observable.

**Justification (substitution chain)**:

  Step 1 (def). P(pass) for CF-S91-CF41-UPPER-22.6-EXTENSION via L=14 cardinality alone = my prior from §2.3 substitution chain = 0.65 (PASS predicted but with non-zero risk of cardinality-ceiling FAIL).

  Step 2 (sub). |delta_P(pass)| = significant: the PASS extends the §VII registry STAGE-1-CANDIDATE landing (CF-S91-CF41-VII-LANDING) to a *narrower* prediction band, which strengthens the framework's bridge-anatomy K-counter for the substrate-cardinality ↔ BBN-PBH-abundance bridge by promoting Level 3 anchor satisfaction tighter (Level-2 envelope `L^{-α}` at α derivable from binomial-cardinality scaling). Per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`, this is a candidate K-counter advancement entry.

  Step 3 (sub). P(fail) = 0.35 (cardinality-ceiling outcome); |delta_P(fail)| = significant in the opposite direction: identifies the structural ceiling on the cardinality lever, redirecting future-session work to cascade-mass-distribution refinement.

  Step 4 (direction). EVOI(CF-S91-CF41-UPPER-22.6-EXTENSION) ≈ 0.65 × 0.4 + 0.35 × 0.3 = 0.26 + 0.105 = 0.365. This is HIGH compared to the typical EVOI of refinement gates (~0.1–0.2).

**Substrate-truncation-FIRST as a META-principle**: per §1 reading and §2 falsification map, the substrate's truncation L_max is an FI-class control parameter (the cardinality lever IS the substrate-IS dimensional parameter at the spectral-triple-cardinality layer). Any S91+ gate whose observable can be expressed as a substrate-cardinality function `f(N_eigs(L_max))` is structurally well-defined and should be prioritized over gates whose observable depends on regulator-class kernel choices (RD-class). This is the structural reading of Pattern P3.

### §3.2 — Approximation-form-LATER for S91 prioritization (DEFERRED-PENDING-DATA weight)

**Recommendation**: defer S91 EVOI weight for approximation-form-refinement gates (CF-S91-CF40-KOLB-TURNER, CF-S91-CF37-FULL-CM1995-RESIDUE, CF-S91-CF37-AUX-4-SECONDARY-CORRIDOR) until the §2.1 / §2.2 outcomes return at K=2 (need ≥ 2 distinct calibration instances per the FI/RD-axis confidence-building protocol).

**Justification**: per §2.1 prediction, CF-S91-CF40-KOLB-TURNER probably PASSes (P(pass) ≈ 0.85); per §2.2 prediction, CF-S91-CF37-FULL-CM1995 probably FAILs (P(pass) ≈ 0.30). The combined EVOI for both is dominated by their joint coverage of the approximation-form-refinement axis:

  EVOI(CF-40 KOLB-TURNER) = 0.85 × 0.20 + 0.15 × 0.10 = 0.185 (LIGHT effort 1.0 we; unblocks CF-39 cascade)
  EVOI(CF-37 FULL-CM1995) = 0.30 × 0.30 + 0.70 × 0.15 = 0.195 (HEAVY effort 3.5 we; mostly confirms (d)∘(b) closure)
  EVOI(CF-37 AUX-4) = 0.40 × 0.40 + 0.60 × 0.20 = 0.28 (HEAVY effort 3.5 we; opens new corridor)

The CF-40 KOLB-TURNER is HIGH EVOI per wave-equivalent (0.185 / 1.0 we = 0.185 EVOI/we), as the WP §"Highlights for next session" line 838 also identifies. It's also the *only* candidate that directly tests falsifier (i) on Pattern P3. **PRIORITIZE CF-S91-CF40-KOLB-TURNER as the LIGHT-effort approximation-form discriminator on Pattern P3.**

CF-S91-CF37-FULL-CM1995 and CF-S91-CF37-AUX-4 are HEAVY effort with comparable EVOI/we (≈ 0.06 and ≈ 0.08 respectively); they should be queued AFTER the CF-40 KOLB-TURNER outcome is known, because the FI/RD-axis reading on Pattern P3 will be sharpened by the CF-40 outcome.

### §3.3 — Effort-Based Probability framing

Per `evoi-prioritization.md §"Effort-Based Probability"`: "framework probability is tracked as: (mechanism links complete / total) × (fraction approaching observation). This goes UP when work is done."

The S90 W4 wave already advanced this metric: CF-41 PASS adds a mechanism-link (substrate cardinality ↔ BBN-PBH-abundance) and approaches observation. The S91+ substrate-truncation-FIRST extension via CF-S91-CF41-UPPER-22.6-EXTENSION continues to advance the metric in the SAME structural class (cardinality lever, FI-class). The approximation-form-refinement gates (CF-40 KOLB-TURNER, CF-37 FULL-CM1995, CF-37 AUX-4) advance the metric in a DIFFERENT structural class (RD-class regulator-discipline). Both classes are necessary; their priority ordering should reflect their EVOI/we and their FI/RD-axis status.

**Net recommendation**: substrate-truncation-FIRST at S91 high EVOI weight. CF-S91-CF40-KOLB-TURNER second-highest (LIGHT effort discriminator on Pattern P3 falsifier (i)). CF-S91-CF37-AUX-4 and FULL-CM1995 deferred to S92+ pending CF-40 outcome.

---

## §4. Carry-forward suggestions for K-counter calibration if P3 strengthens at S92+

If S91+ outcomes confirm Pattern P3 (CF-S91-CF41-UPPER-22.6-EXTENSION PASSes via L=14 cardinality, AND CF-S91-CF37-FULL-CM1995 FAILs at FULL layer, AND CF-S91-CF40-KOLB-TURNER PASSes at canonical-kernel discipline), then the cardinality-lever-as-FI-class observation reaches K=2 (S90 W4 CF-41 as K=1, S91 CF-S91-CF41-UPPER-22.6-EXTENSION as K=2). For MANDATORY status at K=3 per `feedback_rules-compensate-missing-structure.md`, a third structurally-distinct calibration instance is required.

### §4.1 — K=3 calibration candidates queued for S92+

Three forward candidates whose observables qualify as substrate-cardinality (FI-class, Level-1, algebra-INVARIANT integer-count):

(a) **Substrate cardinality on the §VII.AJ.partition-stability bot-20 sector occupation at higher L_max** — extend the S88 W2-6 cardinality vector (2, 4, 8, 6) classification per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level 1 single-τ-slice. At L_max=12 the cardinality vector is bit-identical (confirmed S87 W11-2 via Casimir-bound + cache cross-check, audit `8b4efec59c3b7b05`); at L_max=14+ extend the bottom-N partition to test the cardinality lever for the partition-stability observable.

(b) **Substrate Peter-Weyl sector count at the substrate-distance-2 Mellin-cone pole s=4 vs s=5 cardinality** — the §VII.K-DUAL.LEVEL-DRESSED §VII.AR calibration corpus K=1 instance (S88 W-22 §V.4) operates on rank-ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} regulator-atlas members; substitute the cardinality observable `N_eigs at pole s_k` (integer count of sectors contributing to the substrate-distance-N Mellin-cone residue) for a parallel calibration. This is a candidate Pattern-P3-compatible observable on a different substrate-physics axis.

(c) **Substrate triality-fold count at HP^1 cohomology layer** — extend the S88 W-7 V_4-on-triality landing (audit `4a23fbbb2f6d073e`, Level-1 + Level-2 simultaneous-demonstration corpus instance #2 per `phononic-framing.md §"Single-τ-slice vs moduli-deformation"`). The bot20 sector occupation IS invariant under the cocycle functor F: m(p,q) → Δ_0(m); extend to the L=12 → L=14 cardinality-axis stability of the same invariant. This would also bridge to the §VII.K-DUAL.LEVEL-DRESSED forward calibration corpus for K=2 → K=3 promotion (`sessions/permanent-results-registry.md §VII.K-DUAL.LEVEL-DRESSED` line 4307 reserves K=2/K=3 rows pending S89+ instances).

### §4.2 — Forward calibration enforcement

Per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold: if S91+ produces the second cardinality-lever calibration instance via CF-S91-CF41-UPPER-22.6-EXTENSION (K=2 advancement on the cardinality-lever-as-FI-class axis), the rule-promotion question becomes:

  *"Should the cardinality-lever-as-FI-class be promoted from META-OBSERVATION at K=1 (S90 W4 CF-41) to RULE-SUGGESTION at K=2 (S91 CF-S91-CF41-UPPER-22.6-EXTENSION)?"*

I recommend pre-registering this as an S91+ Wave-Synthesis META-OBSERVATION (not a formal rule promotion) per the W4 author's appropriate caution. The K=3 calibration instance from (a)/(b)/(c) candidates would then enable formal rule-promotion at S92+ MANDATORY status per the existing K-counter advancement protocol.

**The forward methodology is settled**: cardinality-lever observables that satisfy the 3-criterion FI test (§1.1 Step 3 above — dimensionless + algebra-INVARIANT + regulator-class-invariant at cardinality layer) are the structural class that Pattern P3 identifies. Each new such observable that LANDS a registry entry advances K toward the K=3 promotion threshold.

---

## §5. 4-field carry-forward (per `feedback_fix-in-session-never-defer.md`)

### CF-S91-LIZZI-S4-CARDINALITY-LEVER-FI-CLASSIFICATION

| Field | Value |
|:------|:------|
| **What** | Pre-register S91+ wave-synthesis META-OBSERVATION promoting the "cardinality lever is FI-class structural" reading of Pattern P3 from K=1 (S90 W4 CF-41 only) to K=2 (S91 CF-S91-CF41-UPPER-22.6-EXTENSION as 2nd calibration instance). Authoring agent: lizzi-spectral-functional-theorist (FI/RD/MIXED taxonomy origin author, S82 W-3) + connes-ncg-theorist (cyclic-cohomology cross-check on cardinality-layer regulator-invariance) + mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md` if entry lands at §VII registry). Synthesis includes: (i) substrate-IS direction-of-explanation declaration that cardinality is intrinsic to the spectral triple at the cardinality layer (`phononic-framing.md §"IS Space, Not IN Space"`); (ii) FI/RD/MIXED-axis classification of CF-41 cardinality factor as FI per §VII.K theorem clause (a)-trivial integer sub-clause; (iii) cross-link to §VII.K-DUAL.LEVEL-DRESSED forward K-counter calibration; (iv) ENFORCEMENT clause for future §VII registry entries citing cardinality-layer observables: SHOULD tag the entry as cardinality-FI subclass. |
| **Inputs** | (1) `sessions/permanent-results-registry.md §VII.K` (FI/RD/MIXED trichotomy origin); (2) `sessions/archive/session-90/session-90-w4-workingpaper.md` §W4-5 Substrate cardinality refinement table (lines 548–558) — K=1 baseline; (3) CF-S91-CF41-UPPER-22.6-EXTENSION verdict line + npz (S91 dispatch outcome — K=2 candidate); (4) `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (algebra-INVARIANT spectrum-only family criterion); (5) `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold (K=3 MANDATORY); (6) `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level 1 single-τ-slice classification. |
| **Gate** | META-OBSERVATION landing at `sessions/archive/session-91-w{N}-workingpaper.md §"Cross-gate patterns"` extension to Pattern P3, citing K=1 (S90 W4 CF-41) + K=2 (S91 CF-S91-CF41-UPPER-22.6-EXTENSION conditional on PASS at upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] m⁻³). Status: META-OBSERVATION at K=2 (informal); promotes to RULE-SUGGESTION at K=2 only if user adjudicates per `feedback_framework-hygiene.md`; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md` K-counter threshold (requires 3rd distinct calibration instance at S92+). |
| **Effort** | ~0.3 we (META-OBSERVATION extension to S91 wave-synthesis; pattern-extension authoring by lizzi-spectral-functional-theorist; no compute gate; pure synthesis-text landing). |

---

## §6. Substrate framing summary (per `phononic-framing.md §"IS Space, Not IN Space"`)

The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` and `D_K` on Jensen-deformed SU(3). The cardinality `N_eigs(L_max)` is intrinsic to the substrate at the cardinality layer of the Peter-Weyl decomposition — it is NOT a container-coordinate, NOT a regulator-output, NOT an emergent observable downstream of an action. The L_max truncation is a structural pin on the substrate's spectral-triple-cardinality observable; the cardinality is what the substrate IS at that truncation level, not what the substrate looks like *in* some pre-existing arithmetic container.

Direction of explanation for Pattern P3:

```
Substrate IS spectral triple at (A_K, H_K, D_K(τ_fold))
   → Substrate IS the Peter-Weyl decomposition at integer truncation L_max
   → Cardinality N_eigs(L_max) IS the integer count of Peter-Weyl sectors at the truncation
   → Binomial cardinality C(N_eigs, 2) IS the substrate-clock-cancellation factorization's n_edge factor
   → n_edge IS substrate-IS at the cardinality layer (Level-1 single-τ-slice per phononic-framing.md)
   → BBN-PBH abundance n_PBH(z=z_BBN) IS the laboratory-IN observable
   → Bridge map IS the substrate-clock-cancellation factorization (S88 W1a-59 §0)
```

The cardinality lever IS the substrate's own truncation choice. The corridor lever (CF-37 χ'_weight) and approximation-form lever (CF-40 Boltzmann kernel) are NOT substrate's own truncation choices; they are *regulator-class members* selecting cocycle representatives at the cyclic-cohomology layer (CF-37) or threshold-suppression-kernel members at the species-multiplicity layer (CF-40). The FI/RD distinction at this level IS the structural difference between substrate-intrinsic cardinality and regulator-extrinsic cocycle/kernel choice. Pattern P3 IS the substrate-physics observation that substrate-intrinsic cardinality is more reliable than regulator-extrinsic choice — and per the FI/RD-axis reading of §1, this is settled at n=1 in the structural sense even though the K-counter advancement requires K=3 distinct calibration instances per the rule-promotion protocol.

Container-thinking violations FORBIDDEN: do NOT read this as "the substrate has more eigenvalues at higher L" (suggests "in some container of eigenvalues"); INVERT to "the substrate IS the spectral triple at the chosen truncation, and the cardinality of that truncation is intrinsic to that substrate instance". Do NOT read the corridor choice as "selecting a coordinate system on residue space"; INVERT to "the corridor IS the residue-formula choice on the cyclic cocycle, which IS regulator-class-dependent at the cocycle-representative layer".

---

## §7. Closing notes (researcher-reflection)

I am the FI/RD/MIXED-axis author from S82 W-3, and Pattern P3 IS the structural reading my taxonomy was built for. The W4 author's qualification ("ISN'T a generalizable claim from a sample of 3") is appropriate methodological caution at the K-counter rule-promotion layer — but on the underlying FI/RD-axis the reading is settled at n=1: cardinality is FI (clause (a)-trivial integer); residue-formula weight is RD (regulator-class-dependent cocycle-representative); Boltzmann-kernel-choice is RD (regulator-class-dependent threshold-suppression-kernel). Pattern P3 IS the FI/RD-axis classification of the wave's three observables, restated in pattern-form.

The recommendation for S91 prioritization is therefore: substrate-truncation-FIRST at HIGH EVOI weight (the FI-class structural lever); CF-40 KOLB-TURNER as second-priority LIGHT-effort discriminator on falsifier (i); CF-37 FULL-CM1995 + AUX-4 deferred to S92+ pending CF-40 outcome. The K-counter advancement to K=2 via CF-S91-CF41-UPPER-22.6-EXTENSION is also the strongest forward calibration anchor for the cardinality-lever-as-FI-class observation.

The S82 W-3 atlas's 30/42 = 71.4% FI count is consistent with the S90 W4 reading: cardinality-class observables are typically FI (W4 §W4-5 CF-41 promotion driver); corridor-and-approximation-form choices are typically RD (W4 §W4-1 CF-37 PROXY-REFINEMENT-PENDING; W4 §W4-4 CF-40 Boltzmann band). The framework's regulator-class transparency is again working as intended — the taxonomy classifies which gates pass cleanly (FI on cardinality), which gates flag scheme-dependence (RD on corridor/kernel), and which gates are MIXED (composite observables thread multiple structural classes).

If the S91 outcome confirms my §2 predictions (CF-40 KOLB-TURNER PASSes, CF-37 FULL-CM1995 FAILs, CF-41 UPPER-22.6-EXTENSION PASSes via L=14 alone), then Pattern P3 reaches K=2 on the cardinality-lever-as-FI-class observation with substantial structural support, and the K=3 calibration instance from §4 candidates (a)/(b)/(c) becomes the natural S92+ target. The Wave 4 signature "Approximation walls, cardinality opens" IS the §VII.K theorem applied at the wave-aggregation layer — not a coincidence but the substrate's own classification of which levers are intrinsic and which are regulator-class-extrinsic.

---

**End of S90 S-4 solo synthesis (lizzi-spectral-functional-theorist).** No verdict line; output feeds S91 plan-authoring as background per `/rclab-review` semantics. Cross-links: §VII.K (S82 R2-B FI/RD/MIXED trichotomy origin); §VII.K-DUAL.LEVEL-DRESSED (S88 W-22 §V.4 4-class extension forward K-counter); `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (Level 1 cardinality classification); `evoi-prioritization.md` (EVOI scoring + Effort-Based Probability); `feedback_rules-compensate-missing-structure.md` (K=3 promotion threshold); `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY-K=3 algebra-INVARIANT spectrum-only family criterion underlying §1.1 FI test).
