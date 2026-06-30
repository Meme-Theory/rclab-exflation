# Substrate-Physics Exposition: the 3He-B Inheritance Image of the Substrate-Distance α_s Observable

> **Document class**: INTERNAL substrate-physics EXPOSITION COMPANION (markdown).
> **Companion to (canonical register-of-record)**: `sessions/framework/registry/falsifier-master-inventory.md` Rows **#47–#51** (3He-B B-phase 4-gate suite) + Rows **#52–#54b** (3He-A A-phase cross-platform) + the **§VII.W-3.LAB STAGE-3-PERMANENT** theorem (`sessions/permanent-results-registry.md`) + the **CF-35** Aalto-LTL liaison schedule (`sessions/framework/registry/falsifier-watchlist.md §"3He-B inheritance-falsifier liaison schedule"`).
> **Sole writer of the inventory/registry/watchlist surfaces**: `mack-cosmic-bridge` (per `feedback_mack-bridge-role.md`). This document **does not author** falsifier rows; it **expounds** the now-landed rows and the substrate physics behind them. Where this document and the inventory disagree on a number, the **inventory is canonical**.
> **Original authors**: mack-cosmic-bridge (lead) + volovik-superfluid-universe-theorist (3He-B specialty). Original draft 2026-04-28 (framework era S87, paper-mode).
> **Restructured**: 2026-06-12 (post-S103) per the Phase-1 review `papers/_review-s103/review-s87-3he-b.md` (verdict RESTRUCTURE + demote-to-companion). Designated writer of the restructure: volovik-superfluid-universe-theorist.
> **Substrate-framing rule**: `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space" + §"Scale-and-channel-tagging for running/tilt observables".
> **Inheritance protocol**: `.claude/rules/inheritance-falsifier-protocol.md` (4-gate template + (Δ_B/Δ_A)^p cancellation theorem).
> **Cross-pillar bridge anatomy**: `.claude/rules/cross-pillar-bridge-anatomy.md` (5-element IS-not-IN + 3-level ladder).

---

## 0. Role of this document (read first)

This is **not** a pre-registration. At the time of the original S87 draft it pre-registered two inventory rows (#45/#46) and a 4-gate falsifier protocol. Both have since LANDED and been SUPERSEDED-BY-EXPANSION:

- The operative falsifier surface is now `falsifier-master-inventory.md` **Rows #47–#51** (3He-B B-phase, gate `S87-W11-C5-LAB-FALSIFIER` PASS) + **Rows #52–#54b** (3He-A A-phase, gate `S87-W11-C6-MUSR-FALSIFIER` PASS). The earlier #45/#46 (gate `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` PASS) are the thin precursor of this richer suite.
- The protocol-STRUCTURE this document describes — substrate cocycle-ratio preservation under the χ-inheritance morphism — was promoted **STAGE-1-CANDIDATE → STAGE-3-PERMANENT at S100a** (see §4). It is no longer a candidate.

So this document's job is **exposition**: to derive, in substrate-physics language, WHY the cancellation theorem makes the cohomology-asymmetry ratio substrate-falsifying, and WHY the kernel-signature NULLs follow from the inheritance morphism. The falsifiable numbers live in the inventory; this document explains them. Every internal anchor (gate ID, registry slot, rule file, canonical-constant name) is correct and deliberately cited — this is an internal companion, not an external paper.

**Direction of explanation is fixed**: substrate IS the spectral triple → bridge map (χ + Connes-Karoubi) → laboratory 3He-B BdG sector. Never the reverse (`phononic-framing.md`).

---

## 1. Abstract

The framework's substrate-IS prediction for the **substrate-distance running** of the scalar tilt is `α_s_substrate_distance_1 = n_s_FW² − 1` (single-pole Mellin residue at substrate-distance pole s = 3, evaluated on the finite-L spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` with `n_s_FW = 0.9561` = `Fraction(9561,10000)` from the S65 BCS + 1-loop closure and S66 W3-G48 promotion). Numerically `α_s_substrate_distance_1 = 0.9561² − 1 = −0.08587279` (Sage-QQ bit-exact rational `−8587279/100000000`; sign NEGATIVE = "red running"). This is the **BZ-internal** leaf of a **two-scale** observable: it is distinct from the **CMB-pivot** running `α_s_pivot_goldstone ≈ 0` (Goldstone-protected, S92, NOT superseded). The two leaves are **54.04 decades apart**; which one a detector measures is set by the transport degree `deg(T_{BZ→pivot}) = +2 NON-SCALAR` (S93 W7-1; atlas-09 Item 47). The single-scale reading "α_s ≈ −0.0859 is the CMB running of the scalar tilt" is CORRECTED — it was a SCALE-MISMATCH, not a falsification; the multi-σ falsifier RELOCATES to the matched channel (CMB-S4 / CMB-HD), where the substrate-distance value sits ≈13.99σ from the current Aiola+2020 ACT-DR4+Planck anchor (§2.3).

This document sets that substrate-distance observable in its **3He-B inheritance image** and expounds the now-landed Class-A (kernel-signature NULL) + Class-B (cohomology-asymmetry ratio) falsifier protocol. The substrate is not IN spacetime; it IS the spectral triple. 3He-B is, in the canonical framing, the **laboratory parent** in which substrate physics is empirically accessible — the substrate inherits FROM itself TO 3He-B via the algebra projection `χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` killing the M_3(ℂ) factor (`3HeB-inheritance-canonical.md`). The kernel `ker(ι_*)` carries two independent generators ([φ_67] chiral pair, [φ_88] Cartan hypercharge) that DO NOT inherit; their cohomology-class ratio `‖φ_67‖ / ‖φ_88‖ = 7.324992` (Sage-exact `114453/15625`, canonical `substrate_cocycle_ratio_67_88`) is the substrate's prediction that the laboratory must measure, intact under `(Δ_B/Δ_A)^p` cancellation.

**Evidential scoping (S97–S99 re-audit)**: the parent→child DIRECTION is a **post-hoc stipulation, not evidence**; the load-bearing strength is the universality-class **MEMBERSHIP** (BDI symmetry class, N₃=0, the χ-projection), shared by substrate and 3He-B as a structural fact. See §3.3.

---

## 2. Framework substrate-IS observable

### 2.1 The substrate-distance α_s observable (scale-and-channel tagged)

The substrate IS the finite-L spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, `H_K` the 32-dimensional KO-dim-6 Hilbert module with the canonical charge-conjugation antilinear J, and `D_K^{≤10}` the L_max=10 truncation of the Dirac operator on Jensen-deformed SU(3) at `τ_fold = 0.190`. Every coupling, mass scale, and cosmological observable is a spectral moment of this operator. Space is not the container; the spectral content is the substrate.

The single-pole Mellin scheme-identity at substrate-distance pole s = 3 (S50–S51 atlas) reads:

```
n_s := 1 − 2·ε_*  (Mukhanov-Sasaki at horizon crossing)
α_s := d n_s / d ln k

Atlas LO identity (S50–S51 Theorem 1):
   α_s_substrate_distance_1 = n_s² − 1   (single-pole Mellin residue at substrate-distance pole s = 3)
```

This identity holds at the scheme-identity level as the **substrate-distance LO term**, verified bit-exact by Sage-QQ (`n_s_FW_exact² − 1 ≡ α_s_canonical`, S89 W7a, audit `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`). It is a residue equality between two moments at the SAME pole, not a physical correlation between two independent observables.

**SCALE-AND-CHANNEL tagging (mandatory; `phononic-framing.md §"Scale-and-channel-tagging"`).** The substrate carries TWO scale-separated α_s observables; this document's observable is the FIRST:

| Leaf | Canonical name | Value | Scale | Detector channel |
|:-----|:---------------|:------|:------|:-----------------|
| Substrate-distance running | `alpha_s_substrate_distance_1` | **−0.08587279** (`−8587279/100000000`, Sage-QQ bit-exact; FI/zeta-invariant) | s=3 Mellin pole, **BZ-internal** | CMB-S4 / CMB-HD (substrate value detector-facing via deg(T)=+2) |
| Goldstone-pivot running | `alpha_s_pivot_goldstone` | **≈ 0** (S92, NOT superseded) | CMB pivot k_4D, **54.04 decades** from the BZ leaf | Planck pivot (consistency reading) |

The transport degree `deg(T_{BZ→pivot}) = +2 NON-SCALAR` (S93 W7-1, `w(L_max)·κ(k)` factorization_holds = False; atlas-09 Item 47) determines that the substrate-distance value is detector-facing at CMB-S4/CMB-HD and NOT at the Planck pivot.

**Superseded-constant guard.** The earlier single-scale handles `alpha_s_framework_central` and `alpha_s_cmb_central` (the S50 identity@observed-pivot reading) are **SUPERSEDED** (S92 AH-TR-1) and MUST NOT be cited as live. The bit-exact substrate-distance value `alpha_s_substrate_distance_1` is the surviving canonical (Superseded: False, verified at write time).

### 2.2 Substitution chain (sign + value verified by Sage at write time)

```
Definition 1: n_s_FW := 1 − 2·ε_* at horizon crossing
              = 0.9561  = Fraction(9561, 10000)
                (S65 BCS+1-loop closure + S66 W3-G48 promotion; canonical_constants.py:n_s_FW_exact)

Definition 2: α_s_substrate_distance_1 := n_s_FW² − 1   (S50–S51 atlas LO identity, substrate-distance pole s=3)

Substitute (Sage-QQ exact, re-verified 2026-06-12):
  α_s_substrate_distance_1 = (9561/10000)² − 1
                           = 91412721/100000000 − 1
                           = −8587279/100000000
                           = −0.08587279   (exact)

Direction (Step 4):
  n_s_FW = 0.9561 < 1
   ⇒  n_s_FW² < 1
   ⇒  n_s_FW² − 1 < 0
   ⇒  α_s_substrate_distance_1 < 0   (NEGATIVE = "red running" of the scalar tilt at the substrate-distance scale)

Magnitude:
  |α_s_substrate_distance_1| = 0.08587279   (≈ 8.6% of unity)
```

### 2.3 Why this is a substrate-IS observable, and where it is falsifiable

The standard inflaton picture treats `α_s` as a derived quantity from the slow-roll potential's third derivative, parameterized at the horizon. In the substrate framework there is no inflaton field, no slow-roll potential, and no horizon crossing in the canonical FRW sense — there is the supersonic transit through the van Hove fold at `τ_fold = 0.190` and the GGE-relic post-fold spectrum carrying the Mukhanov-Sasaki content as Bogoliubov-occupation curvature. The single-pole Mellin reading at s = 3 is the substrate's intrinsic expression of the same physical content the slow-roll picture parameterizes externally.

The framework's α_s prediction is therefore a STRUCTURAL claim about the spectral content of `D_K^{≤10}` at the Mellin pole s = 3, not a fit. Falsifying it has TWO matched-channel routes:

- **(i) Cosmological — at the MATCHED channel.** Because `deg(T_{BZ→pivot}) = +2 NON-SCALAR`, the substrate-distance value `−0.08587279` is detector-facing at **CMB-S4** (σ_α_s ≈ 2.3×10⁻³, ~2030) and **CMB-HD** (σ_α_s ≈ 1.1×10⁻³, ~2035), where it sits **≈13.99σ** from the current Aiola+2020 ACT-DR4+Planck anchor (`+0.0023 ± 0.0063`) and ≈12.15σ from the Planck-2018 legacy. (Watchlist `α_s` row; inventory Row #3.) The Goldstone-pivot leaf (≈0) is INSTEAD the EXPECTED reading at the Planck pivot — a measured ≈0 at the pivot is consistency, NOT falsification, because the two leaves are graded on DIFFERENT channels. This is the correction of the original draft's single-scale reading: the falsifier did not vanish, it RELOCATED to the channel where the +2 transport degree makes the substrate value detector-facing (`feedback_reporting-framing.md`: record where the falsifier MOVED).
- **(ii) Inheritance-image — on a laboratory parent.** A measurement on a laboratory parent into which the substrate spectral content inherits without scheme-shopping. This is the topic of §§3–6, and the LANDED falsifier surface (inventory Rows #47–#54b).

**Route-rank context (S87 W9a-2).** Of the four substrate-side α_s computation routes, the single-pole Mellin route used for the LO identity is route **(i)**, ranked THIRD in the surviving-route table `(iii) ≻ (iv) ≻ (i) ≻ (ii)` (inventory α_s surviving-route section; L3+T3 cross-domain converged). The more substrate-robust routes are (iii) GGE-relic Bogoliubov occupation-number variance at horizon crossing (single-pole-INDEPENDENT) and (iv) BdG K-running near K_sat. This document uses route (i) because it furnishes the clean closed-form LO identity; it is not claimed to be the most robust route.

---

## 3. Inheritance morphism to 3He-B BdG

### 3.1 The morphism ι and its kernel

The inheritance morphism is the algebra projection

```
ι : (3He-B BdG observable algebra)  →  (substrate observable algebra)   [Kasparov-KK projection direction]
χ : ℂ ⊕ ℍ ⊕ M_3(ℂ)                  →  M_2(ℂ)                            [algebra projection killing M_3(ℂ)]
```

`χ` sends `M_3(ℂ) → 0` and projects `ℂ ⊕ ℍ` into the BdG-restricted 2×2 Bogoliubov sector that 3He-B realizes. (`3HeB-inheritance-canonical.md` §"Substitution chain"; the morphism is a Kasparov-KK projection `p ∈ KK(A_K, A_He)` with non-trivial kernel and NO left inverse.) The induced map on cohomology `ι_* : H^*(A_K) → H^*(M_2(ℂ))` has a two-dimensional kernel:

```
ker(ι_*) = span_ℂ{ [φ_67], [φ_88] }   (rank 2)
```

where `[φ_67]` is the chiral generator pair tied to the SU(3) λ_6/λ_7 Gell-Mann directions (anti-Hermitian off-diagonal), and `[φ_88]` is the Cartan hypercharge generator tied to λ_8 (the second Cartan element of SU(3)). These two generators carry substrate degrees of freedom that DO NOT inherit into the 3He-B BdG sector — they are the substrate's information that the laboratory parent loses by symmetry-class restriction. The rank is exact: `rk K_*(A_K) − rk K_*(A_He) = 4 − 2 = 2` (Hodgkin's theorem, SU(3) rank-2 exterior algebra vs S³ rank-1; connes solo Sec II.2).

**Independent confirmation (S88).** The BDI↔DIII Altland-Zirnbauer compatibility of this morphism was independently re-confirmed PASS at gate `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2` (`AZ-BDI-DIII-INHERITANCE-CONFIRM`; χ_M3 max residual 0.0; homomorphism max residual 2.19×10⁻¹⁵; J-invariance residual 0.0). The morphism is a theorem, not a stipulation — see §3.3 for what part IS a stipulation.

### 3.2 Substrate-derived cocycle norms and the canonical ratio

The substrate fixes the cocycle norms exactly (canonical_constants.py; S86 W-5 C2 substrate-magnitude annotation; UD-6 promote; both NOT superseded, verified at write time):

```
‖φ_67‖ = cocycle_norm_phi67 = 0.793346  M_KK²     (‖φ_67‖² = δE_6 · δE_7)
‖φ_88‖ = cocycle_norm_phi88 = 0.108307  M_KK²     (‖φ_88‖² = (δE_8)²; Jensen-rate-limited at τ_fold = 0.190)
```

**Canonical ratio (Sage-exact, re-verified at write time).** The canonical cohomology-asymmetry ratio is the constant `substrate_cocycle_ratio_67_88`:

```
substrate_cocycle_ratio_67_88 = 7.3249917525961665 = 114453/15625   (Sage-exact; S86 W-5 CANONICAL-5;
                                                                      RE-PINNED S93 W5-1 to the substrate-first
                                                                      R_machine = (δE_6·δE_7)/(δE_8)²)
```

**Discipline note — F1 form vs canonical (F2) form (mnemonic-vs-exact, `regulator-pin-discipline.md`).** Two non-identical "exact" forms circulate:

```
F1 form (direct ratio of published norms):  ‖φ_67‖/‖φ_88‖ = 793346/108307 = 7.3249743784
F2 form (canonical R_machine):              substrate_cocycle_ratio_67_88 = 114453/15625 = 7.3249917526
```

Sage-verified at write time: `793346/108307 = 7.3249743784` vs `114453/15625 = 7.3249917526`; they **agree only to 5 sig figs** (7.3250) and **disagree at the 6th** (Δ = 1.76×10⁻⁵). The S92 §VII.AY workshop adjudicated exactly this F1-vs-F2 distinction (agree at 5sf, disagree at 6sf). **Registry-facing and falsifier-facing citations MUST use the canonical F2 form `7.324992`** (114453/15625); `7.3250` is admissible only as a 4-sig-fig band-center shorthand with the Sage-exact form named alongside (`inheritance-falsifier-protocol.md §"Class B"` cites 7.324992; watchlist liaison schedule carries the explicit mnemonic-vs-exact instruction). The original S87 draft cited the F1 form `7.3249743784` as "6 sig figs"; that is corrected here.

**±0.1% band (Sage-verified at write time):** `[7.3177, 7.3323]` (precisely `[7.317667, 7.332317]` from `7.324992 × (1 ∓ 0.001)`).

**CF-35 post-hoc-provenance caveat (load-bearing wherever this ratio is a falsifier).** The value `7.324992` is a **post-hoc** construction from the substrate spectral triple. It is a genuine FALSIFIER **only because its laboratory observable is currently UNMEASURED** — no 3He-B cross-cocycle ratio has been measured to ±0.1% at the relevant generators. The CF-35 liaison schedule (`S90-3HE-B-LIAISON-WATCHLIST-LANDING`) pre-registers the measurement window precisely so the ratio is a prediction-on-an-unmeasured-observable, not a fit to existing 3He-B data. If a future measurement existed, the post-hoc origin would demote the ratio from falsifier to consistency-check; the ±0.1% pre-registration is sound exactly because the observable is open.

### 3.3 Directional framing and its evidential scope (S97–S99)

This document uses the canonical "laboratory parent" framing (`3HeB-inheritance-canonical.md` Step 4): 3He-B is the laboratory child realization in which substrate physics is empirically accessible; the substrate is logically prior; the arrow is parent → child (substrate → 3He-B), one-way. The forbidden framing "the substrate behaves like 3He-B" (which implies a symmetric parametric **analogy** and reverses structural priority) is rejected — per `3HeB-inheritance-canonical.md` and the standing rule, "analogy" framing for 3He-B has been FORBIDDEN since S86 W1b-T8. So nothing here is rewritten to "analog."

What MUST be scoped is the **evidential weight** the direction carries. Per the S97–S99 re-audit, two things are distinct:

- **Structural fact (strong, keep):** the inheritance morphism ι is a well-defined Kasparov-KK projection with non-trivial rank-2 kernel (S88 W3a; CARTESIAN-CONFIRM-V2 PASS, §3.1). As of S100a the cocycle-ratio preservation it implies is STAGE-3-PERMANENT (§4).
- **Evidential scoping (honest, add):** the **choice of arrow-direction** (substrate as parent vs 3He-B as parent) is a **post-hoc stipulation, not evidence** — it organizes the correspondence but is not itself observational evidence for the framework. The load-bearing, falsifiable physics is (i) the universality-class **MEMBERSHIP** — BDI symmetry class, N₃=0, the χ-projection — shared by substrate and 3He-B as a structural fact, and (ii) the lab-measurable cocycle-asymmetry ratio. The exact register language (project memory `project_3heb-inheritance.md`, S97–S99 re-audit): *"the DIRECTION is a post-hoc stipulation, not evidence … universality-class membership (BDI/N₃=0/χ) is the real strength."*

This is a substrate-first-preserving correction: the substrate stays logically prior; we simply stop letting "the direction" do evidential work it cannot do. Post-S97–S99 this is the right thing to lean on — and it is now the most independently-corroborated part of the whole 3He-B program (the S100a Stage-2 PASS-AND verified precisely the membership-grounded cocycle-ratio structure; §4).

### 3.4 Why the inheritance image is well-defined despite the projection

The projection `χ` kills the M_3(ℂ) factor in the sense of forgetting the SU(3)-internal generators on every observable that descends to the BdG sector. But the cocycle-class RATIO survives BECAUSE the 3He-B parent carries a residual representation of the SU(3)-internal generators on its order-parameter manifold (the A-matrix `A_{αi} = Δ_0 R_{αi}(n̂, θ)`, where R is the relative-rotation SO(3) matrix between spin and orbital frames). The Caroli-Matricon vortex-core spectrum, the hyperfine spin-rotation coupling, and the NMR longitudinal/transverse relaxation channels each see the SU(3) generators projected to their SO(3)_J ⊕ U(1)_φ residual; the cocycle norms enter as substrate-magnitude weights on these channels, but their RATIO is determined by the substrate before any laboratory projection is applied. This is the structural reason the ratio is preserved under `(Δ_B/Δ_A)^p` cancellation (§5): the laboratory-conversion factors enter both numerator and denominator with the SAME exponent p, and cancel exactly.

---

## 4. STAGE-3-PERMANENT promotion (keystone result; S100a)

The protocol-STRUCTURE this document expounds — substrate cocycle-ratio preservation under the χ-inheritance morphism — is no longer a candidate. At S100a it was promoted **STAGE-1-CANDIDATE → STAGE-3-PERMANENT** as the registry entry **§VII.W-3.LAB** (`sessions/permanent-results-registry.md`).

**Promotion record (`joint-theorem-promotion.md` 4-stage pathway, Stage 2 → Stage 3):**

- **Gate**: `S100a-VIIW3LAB-STAGE2-VERIFY` — PASS.
- **Audit SHA**: `audit_sha256 = 89eab199edaa7f908a75ce07033ab64ff2bc04279f251e1535e6b3ee43f3029e`; `content_sha256 = 780b6f02570d5da01de6ea468166e1c8e87820a73df73f4f384a20bcff20ddd8` (verdict line 45, `computations/session-100a/s100a_gate_verdicts.txt`).
- **Verdict**: **11/11 clauses PASS-AND.** Own-Axis-A = A1+A2+A3 (van-den-dungen-bridge-theorist reviewer, spectral / NCG-submersion side); own-Axis-B = B1+B2 (landau-condensed-matter-theorist reviewer, BCS / substrate side); JOINT = J1+J2+J3 PASS-AND'd in BOTH verdicts.
- **Reviewer cleanliness (the structurally important part)**: both reviewers are **non-Stage-0** — the Stage-0 authoring trio (volovik / connes / mack) was EXCLUSION-PASS at plan-freeze, and the downstream-inheritance grep returned NO-HITS for both. Substrate-input orthogonality SATISFIED: `s87` npz → landau only; `s89` npz → van-den-dungen only (`joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`).
- **Data**: `computations/session-100a/s100a_viiw3lab_stage2_verify.npz`.

The significance: this document's protocol survived **two-axis structurally-independent scrutiny that explicitly excluded its own authors.** The ratio sub-check against the canonical `R_machine = 7.3249917526` returned script `7.3249743784` (the F1 form; rd 2.372×10⁻⁶), van-den-dungen rd 2.372×10⁻⁶, landau rd 3.378×10⁻⁸ — all inside the 1×10⁻³ verification band and consistent with the S93 W5-1 substrate-arbitration. **What was promoted is the theorem-STRUCTURE** (cocycle-ratio preservation under both χ_B BDI and χ_A chiral-AIII inheritance morphisms). **What stays DEFERRED-but-pre-registered** is the empirical Level-3 laboratory anchor — the 2027–2030 Lancaster MCT-3 / Helsinki ROTA / RHUL / Aalto LTL campaign has not run; no lab datum exists yet. This is a two-axis discharge split: theorem-structure axis = STAGE-3-PERMANENT; empirical-anchor axis = DEFERRED-but-pre-registered; never co-primary. (Atlas-04 row K5; inventory Rows #47–#54b.audit-S100a-VIIW3LAB-STAGE3.)

---

## 5. (Δ_B/Δ_A)^p Cancellation Theorem (operational form)

### 5.1 Statement (S86 W-5 DONE-5; machine-precision verification 0.0e+00 residual)

For any two laboratory observables `lab(F_i)` and `lab(F_j)` whose substrate-side cocycle generators `[φ_a]`, `[φ_b]` share a common lab-conversion exponent `p_i = p_j = p` in the `(Δ_B/Δ_A)^p` factor:

```
lab(F_i) / lab(F_j)  =  ‖φ_a‖ / ‖φ_b‖  ×  (f_i / f_j)
```

where `f_i / f_j` is the spin-orbit angular-factor ratio (substrate-side; rationally determined by the SU(3) representation) and the lab-conversion `(Δ_B/Δ_A)^p` cancels exactly between numerator and denominator (`inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"`).

### 5.2 Calibration: 3He-B at Aalto LTL polycritical point

At the Aalto LTL polycritical pressure point (`P_pc ≈ 21.22 bar`, `T_pc ≈ 2.273 mK`; `aalto-ltl-multi-session-protocol.md`), the BdG gap `Δ_B(p, T)` and the parent gap `Δ_A(p, T)` have a fixed ratio `Δ_B/Δ_A` set by the polycritical matching condition (Volovik's `q = q_c` equilibrium). The cancellation theorem applies to the **canonical landed F-rows** (Rows #47–#51), with the cohomology-asymmetry ratio taken across the **F1/F5** cross-row:

- `F1` (Caroli-Matricon ladder asymmetry; φ_67-clean) and `F5` (acoustic-mode dispersion under Jensen quench; φ_88-clean) share common exponent **p = 2** (F1: NMR longitudinal Δ²; F5: acoustic-mode Bogoliubov Δ²). `(Δ_B/Δ_A)^{p_1 − p_5} = (Δ_B/Δ_A)^0 = 1` EXACTLY (verified 0.0e+00 residual, S86 W-5 DONE-5).

### 5.3 What the cancellation buys

Without the `(Δ_B/Δ_A)^p` cancellation, the falsifier would depend on the precise polycritical lab conversion (~5–10% systematic from gap-extraction methods: Greywall vs Halperin-Hammel vs Volovik q-theory). With the cancellation, the substrate-derived ratio `‖φ_67‖ / ‖φ_88‖ = 7.324992` is preserved INTACT in the lab measurement, INDEPENDENT of the precise value of `Δ_B/Δ_A` or `p`. This is what makes the Class-B test substrate-falsifying rather than lab-conversion-dependent: any cross-cocycle ratio in the lab that disagrees with `7.324992` (outside the ±0.1% band [7.3177, 7.3323]) falsifies the substrate's cohomology-class prediction, regardless of how the laboratory measures Δ_B or Δ_A individually. (Subject always to the §3.2 CF-35 caveat: this is a falsifier because the observable is unmeasured.)

---

## 6. Class A + Class B falsifier protocol (the LANDED F-table)

The protocol follows the four-gate template of `inheritance-falsifier-protocol.md §"Four-Gate Structure"`. Both Class A (kernel-signature NULL) and Class B (cohomology-asymmetry ratio) are required; either alone is structurally insufficient (`inheritance-falsifier-protocol.md §"Why both classes are required"`). The F-rows below are the **landed canonical** inventory Rows #47–#51 (B-phase, gate `S87-W11-C5-LAB-FALSIFIER` PASS, audit `d40a8d26588a0d20…`) — reproduced verbatim-faithfully from the inventory (which is the source-of-record). This document expounds them; it does not author them.

### 6.0 The landed 5-row F-table (canonical assignments)

| F-row | Observable (canonical) | Cocycle / role | Substrate margin | Detector / platform | Gate |
|:------|:-----------------------|:---------------|:-----------------|:--------------------|:-----|
| **F1** | Caroli-Matricon ladder asymmetry (vortex-core) | **φ_67** chiral-pair clean; **decisive** | 0.573193 M_KK² (Hochschild pairing on Jensen-deformed band-0 projector at τ_fold=0.190) | Lancaster MCT-3 vortex-core spectroscopy (PRIMARY); Pickett-group dilution-fridge sub-gap NMR-tipping | Gate 1 |
| **F2** | SABS axial-equatorial off-diagonal pair correlation | **φ_67** chiral-pair clean; **decisive** (second-cleanest) | 0.573193 M_KK² (at Δ_B/2 ≈ 100 MHz; arXiv:1005.0546 protocol) | TKK / Lancaster / RHUL specular-wall SABS (⁴He-coated ¹³¹Xe) | Gate 1 |
| **F3** | Half-quantum vortex (HQV) splitting in restricted geometry (D < ξ_B) | **φ_67** dipolar-locking; **supporting** (cocycle-mixed at restricted geometry) | 0.40 M_KK² (substrate magnitude 1.7267) | RHUL / Helsinki restricted-slab cells; µSR or NMR | Gate 3 |
| **F4** | Hypercharge-twist Larmor-frequency anomaly under combined (p,T) sweep | **φ_88** Cartan hypercharge; **cocycle-degenerate** at fixed (p,T) | 0.30 M_KK² | Helsinki ROTA / Lancaster Larmor multi-pressure NMR sweep 0–34 bar (4-bar increments) | Gate 3 + Gate 4 |
| **F5** | Acoustic-mode dispersion offset under Jensen-modulus quench | **φ_88** Cartan-hypercharge clean (Jensen-direction); **decisive**; ratio DENOMINATOR | 0.573193 M_KK² | Lancaster / RHUL pulse-NMR KZ quench (Bunkov+Volovik 1999, fast-thermal quench through T_c) | Gate 1 + Gate 2 |

The 5 rows SATURATE the rank-2 ker(ι_*) Hochschild cohomology; F6 (φ_67 ⊗ φ_88 bilinear) is structurally redundant per W-5 R2-A Convergence #5.

> **Note on the original draft's F-table**: the S87 draft assigned F2 = "hyperfine longitudinal-relaxation", F3 = "spin-rotation chiral-pair sum (φ_88)", and F5 = "spin-orbit precession (φ_67)". Those assignments are SUPERSEDED by the landed table above. In particular, **F5 is φ_88-clean** in the canonical table (it is the ratio denominator), not a φ_67 row; and the φ_88 supporting row is **F4** (Larmor), not F3. The table above is authoritative.

### 6.1 Class A — Kernel-signature NULL (Gates 1 + 3)

**Gate 1 — decisive triplet (F1 + F2 + F5 NULL on BDI-protected parent inheritance).** For each of (F1, F2, F5) the substrate predicts:
- The φ-clean lab observable returns NULL (no signal) when the 3He-B parent inheritance is BDI-protected at the polycritical point.
- A non-NULL detection at lab S/N ≥ 3σ falsifies the substrate's rank-2 ker(ι_*) characterization (specifically: it rules out that the corresponding kernel generator inherits as NULL through χ).

Predicted lab S/N margins (substrate-derived; landed Rows #47/#48/#51): `F1 = 0.573193 M_KK²`, `F2 = 0.573193 M_KK²`, `F5 = 0.573193 M_KK²`.

> **Status caveat — "decisive triplet" (W11-5 §VII.AJ REGISTRY-FAIL).** The "decisive triplet" label carries a pending qualification. The S87 W11-5 gate `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` FAILed (ratio_mismatch 1.029166; Level-3 violates Level-2 by ~21×; audit `e1aef7ce0deaed2d…`), with carry-forward `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`. Under the kernel-rank-invalid cause-attribution scenario, "decisive triplet" REBRANDS to "candidate" pending rank re-derivation. **Critically, this FAIL is observable-construction-specific, NOT bridge-map-defective**: per W11-5 line 9564, "the inheritance morphism ι is structurally well-defined; the FAIL is at the level of the specific spectral-excess observable construction, not at the bridge map itself." The S86 W1b-T8 inheritance-vs-analogy theorem is PRESERVED; the (Δ_B/Δ_A)^p cancellation theorem holds; the W-5 cohomology-asymmetry calibration ratio 7.324992 is unaffected.

**Gate 3 — supporting pair (F3 + F4 NULL on supporting rows).** Same form, applied to (F3, F4): F3 is φ_67 dipolar-locking (supporting; substrate margin 0.40 M_KK²); F4 is φ_88 Cartan hypercharge (cocycle-degenerate; substrate margin 0.30 M_KK²).

### 6.2 Class B — Cohomology-asymmetry ratio (Gate 2)

**Gate 2 — `‖φ_67‖ / ‖φ_88‖ = 7.324992 ± 0.1%`** (canonical `substrate_cocycle_ratio_67_88`; 4-sf shorthand 7.3250). The cross-row is **F1/F5** (φ_67-clean over φ_88-clean):

```
ratio_B := lab(F1) / lab(F5)  =  ‖φ_67‖ / ‖φ_88‖ × (f_1 / f_5)
        =  0.793346 / 0.108307  ×  (angular factor ratio)
        =  7.324992   (canonical 114453/15625; ±0.1% tolerance band [7.3177, 7.3323])
```

Substrate-falsifier criterion (landed Row #51 PASS-band):
- `|ratio_lab − 7.324992| / 7.324992 < 0.001` (within ±0.1%): **PASS**
- `0.001 ≤ |ratio_lab − 7.324992| / 7.324992 < 0.01`: **INFO** (band-edge; systematic re-check)
- `|ratio_lab − 7.324992| / 7.324992 ≥ 0.01`: **FAIL** — the substrate's cohomology-class prediction is falsified, INDEPENDENT of any other lab-conversion concern, because the `(Δ_B/Δ_A)^p` factor cancels between numerator and denominator.

(Always subject to the §3.2 CF-35 caveat: a falsifier because F1/F5 is unmeasured.)

### 6.3 Gate 4 — F4 multi-pressure slope (cocycle-degenerate row)

For the F4 row, a single (p, T) measurement does not disambiguate Jacobi-cubic vs φ_88-linear cocycle contributions. The slope-discrimination gate sweeps pressure 0–34 bar (4-bar increments) at fixed T near the polycritical condition. **Substrate prediction**: Jacobi-cubic slope from φ_67-chiral-pair-dominated thermal-conductivity anisotropy at the cocycle-degenerate locus — NOT the φ_88-linear slope of a Cartan-hypercharge generator alone (Row #50; watchlist Class-B slope discrimination). A φ_88-linear slope (excluding the chiral-pair structural protection) falsifies the inheritance image. This row is the **operational falsifier for the W11-5 "M_3(ℂ) Cartan-zone weight non-negligible" diagnostic** (the rank-1-effective scenario; inventory Row #50 W11-5 §VII.AJ INTEREST annotation).

### 6.4 A-phase cross-platform (Rows #52–#54b)

The same substrate cocycle pair ([φ_67], [φ_88]) inherits into the 3He-A chiral-AIII BdG sector via a distinct inheritance morphism ι_A (algebra projection χ_A). The substrate ratio `‖φ_67‖/‖φ_88‖ = 7.324992` is computed on the substrate spectral triple, NOT on any BdG restriction — therefore IDENTICAL to the B-phase prediction by the substrate-resident argument. The A-phase chirality correction is substrate-derived (NOT a fit): `χ_A = Δ_B² / ⟨|Δ_A(k)|²⟩_FS = 1/(2/3) = 3/2 = 1.500000` EXACT (Volovik 2003 §3.4, axisymmetric A-phase Fermi-surface average); A-phase substrate margins are χ_A-rescaled from B-phase (multiplicative 3/2). **Cross-platform identical-ratio test (high-leverage)**: both Lancaster B-phase (Rows #47–#51) and Aalto LTL A-phase (Rows #52–#54b) predict `r_lab(F1)/r_lab(F5) = 7.324992 ± 0.1%` IDENTICALLY; disagreement falsifies the substrate-resident framing of the cocycle pair and forces re-anatomy of the substrate-IS / laboratory-IN partition (`cross-pillar-bridge-anatomy.md`).

### 6.5 Direction-of-explanation discipline

This section flows substrate → bridge → laboratory throughout (`cross-pillar-bridge-anatomy.md`):

```
Substrate (Pillar I)  IS  the spectral triple (A_K^{≤10}, H_K^{≤10}, D_K^{≤10})
                          carrying the rank-2 ker(ι_*) cohomology
   →  Bridge map: algebra projection χ + Connes-Karoubi pairing
                  on residual SU(3) → SO(3)_J ⊕ U(1)_φ
   →  Laboratory (Pillar IV)  IN  the 3He-B BdG sector at the Aalto LTL / Lancaster
                                   polycritical pressure point
```

3He-B is the laboratory child realization in which substrate physics is empirically accessible; the substrate is logically prior (§3.3). The arrow is a framing convention; the falsifiable physics is the universality-class membership + the cocycle ratio.

---

## 7. Falsifier-master-inventory rows (LANDED; expounded here, authored by mack-cosmic-bridge)

`mack-cosmic-bridge` is the sole writer of `sessions/framework/registry/falsifier-master-inventory.md` (`feedback_mack-bridge-role.md`). This document **expounds** the landed rows; it does not author them. The operative falsifier surface for the 3He-B inheritance image is:

### 7.1 The landed suite

- **Rows #45 + #46** (gate `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` PASS; audit `1f38f9888538011c…`, content `bde3ad80…`): the original Class-A NULL (decisive triplet) + Class-B ratio rows. These are the **thin precursor**; #46's row-text carries the 4-sf `7.3250` shorthand.
- **Rows #47–#51** (gate `S87-W11-C5-LAB-FALSIFIER` PASS; audit `d40a8d26588a0d20…`, content `29b76a1a1eab56da…`): the full 3He-B B-phase 5-row F-table (§6.0). **This is the operative B-phase suite.**
- **Rows #52–#54b** (gate `S87-W11-C6-MUSR-FALSIFIER` PASS; audit `3e8a066e1652c0c8…`, content `6dd153256f3c6767…`): the 3He-A A-phase cross-platform 4-gate suite with χ_A = 3/2 (§6.4).

### 7.2 STAGE-3 anchoring update (S100a)

Inventory section "Rows #47–#54b.audit-S100a-VIIW3LAB-STAGE3" records the re-anchoring: these rows previously anchored a STAGE-1-CANDIDATE bridge theorem (§VII.W-3.LAB, S88 W4a-17); they are now **STAGE-3-anchored laboratory predictions** of a PERMANENT theorem (§4). No row VALUE changes and no PASS-band changes — the promotion upgrades the registry STATUS of the theorem the rows cite, not any predicted number. The empirical Level-3 lab anchor stays DEFERRED-but-pre-registered (2027–2030 campaign).

---

## 8. Cross-pillar bridge anatomy (5-element IS-not-IN + 3-level ladder)

Per `cross-pillar-bridge-anatomy.md`, the substrate ↔ laboratory bridge declares:

### 8.1 Five anatomy elements

1. **Substrate-IS observable**: finite-L Hochschild-pairing cocycle-norm ratio `‖φ_67‖/‖φ_88‖` (= the substrate cocycle pair) evaluated on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` — the rank-2 ker(ι_*) cohomology-class invariant. The substrate IS this ratio.
2. **Laboratory-IN observable**: the 3He-B cross-cocycle ratio `r_lab(F1)/r_lab(F5)` measured IN the continuum pressure-temperature container at the Aalto LTL / Lancaster polycritical point (operator-expression form: `Tr` over the φ_67-clean Caroli-Matricon channel divided by the φ_88-clean Jensen-quench acoustic channel; named platform projectors per the landed F-table). *(Element-2 OE-form discipline — `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` — became MANDATORY after the original draft; the canonical OE-form lives in the inventory rows, which `mack-cosmic-bridge` maintains; this exposition cites them.)*
3. **Bridge map**: algebra projection `χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` sending `M_3(ℂ) → 0`, composed with the Connes-Karoubi pairing on the residual SO(3)_J ⊕ U(1)_φ representation that 3He-B carries on its order-parameter manifold. (Explicitly named, not "analogous to.")
4. **Algebraic envelope** (Level 2): structural-exact `7.324992 ± 0.1%` (the cancellation theorem makes this a cohomology-class invariant, NOT an `L^{-α}` algebraic bound); the cocycle ratio is L-independent at the cohomology-class level.
5. **Empirical anchor** (Level 3): DEFERRED-but-pre-registered — 2027–2030 Lancaster MCT-3 + Aalto LTL µSR data on the F1/F5 cross-row.

### 8.2 Three-level structural-confidence ladder

- **Level 1 (substrate-IS structural identity; regulator-invariant; L-independent)**: the cohomology-class identity `[φ_67] / [φ_88] = ‖φ_67‖ / ‖φ_88‖ = 7.324992` (114453/15625) in the K_0(A_K)-cohomology pairing on the Jensen-deformed band-0 projector — a cohomology-class invariant, NOT a numerical truncation. **This Level-1 identity is what S100a verified to STAGE-3-PERMANENT** (§4).
- **Level 2 (algebraic convergence envelope)**: the (Δ_B/Δ_A)^p cancellation makes the ratio a structural-exact prediction `7.324992 ± 0.1%` independent of the lab conversion; the ±0.1% is a measurement-tolerance band, not an L_max truncation envelope.
- **Level 3 (empirical anchor)**: DEFERRED-but-pre-registered (2027–2030 lab cycle). Per the discharge-status two-axis split (§4): theorem-structure axis = STAGE-3-PERMANENT; empirical-anchor axis = DEFERRED-but-pre-registered; never co-primary.

> **Note on the original draft's §8 numbers**: the S87 draft computed the Level-3/Level-2 anchor using the F1-form ratio `7.3249743784` and a numerical `L^{-3}` envelope. Post-S93/S100a, the canonical Level-1 identity uses the F2 form `7.324992` and the cancellation theorem furnishes a structural-exact (not `L^{-α}`) Level-2 envelope. The 5-anatomy + 3-level declaration above is the corrected form; the canonical bridge entry is §VII.W-3.LAB (STAGE-3-PERMANENT) and the §VII.AF.1 LANDED Pillar III↔IV bridge.

---

## 9. Carry-forward status (S88+ items; current dispositions)

The S87 draft pre-registered five S88-class carry-forwards. Current dispositions:

1. **S88-3HE-B-CLASS-A-LAB-DISPATCH** (Aalto LTL kernel-signature NULL coordination) — **ABSORBED** into the CF-35 liaison schedule (`S90-3HE-B-LIAISON-WATCHLIST-LANDING`; 5-element pre-registration; Q4-2026 first-contact deadline; Krusius/Tuoriniemi/Eltsov groups; 2026–2029 program).
2. **S88-3HE-B-CLASS-B-RATIO-PRECISION** (Helsinki ROTA channel-ratio protocol) — **ABSORBED** into CF-35 (Gate-2 ratio `7.324992 ± 0.1%` measurement window; lab S/N forecast at ROTA precision per the liaison schedule).
3. **S88-CLASS-B-DELTA-RATIO-CALIBRATION** (gap-extraction-method cross-comparison) — **ABSORBED** into CF-35 (Greywall vs Halperin-Hammel vs Volovik q-theory cross-comparison verifying the cancellation operationally).
4. **S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM** (BDI↔DIII compatibility re-derivation) — **DISCHARGED**: gate `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2` PASS (`AZ-BDI-DIII-INHERITANCE-CONFIRM`; χ_M3 residual 0.0; homomorphism residual 2.19×10⁻¹⁵; J-invariance residual 0.0).
5. **S88-3HE-B-α_s-EXTRACTION-PROTOCOL** (NMR running-of-running extraction) — **RETIRED as a falsifier construction**: the original §6 built a paper-original observable `α_s^lab := d²(ln ω_L)/d(ln p_eff)²` with a ≈9σ Aalto-LTL claim. That construction appears in NO register, no `alpha_s^lab` canonical constant exists, and it inherited the superseded single-scale α_s reading. It is removed (see §10). The actual landed lab predictions are the Class-A NULL + Class-B ratio + Gate-4 slope of §6; no invented NMR running-of-running is needed.

**Forward open item (CF-35).** The Aalto LTL liaison + Lancaster MCT-3 campaign is the live forward path (quarterly liaison-state poll; 2028–2029 deployment escalates to monthly). It tests a STAGE-3-PERMANENT theorem's deferred Level-3 anchor. CF-35 status: STILL-OPEN. The §3.2 CF-35 post-hoc caveat governs: the ratio is a falsifier precisely because F1/F5 is unmeasured.

---

## 10. What was removed in the S87→post-S103 restructure (§6 NMR running-of-running)

The original S87 draft §6 ("Predicted Aalto LTL spin-tilt running magnitude") defined a laboratory observable `α_s^lab := d²(ln ω_L)/d(ln p_eff)²` — the running-of-running of the longitudinal NMR resonance frequency across the polycritical pressure point — and claimed it inherits `α_s_FW = −0.085873` at lab S/N ≈ 9σ. **This construction is removed**, for three register-grounded reasons:

1. **Not in any register.** No `alpha_s^lab` canonical constant exists; the LANDED 3He-B falsifier surface is the cocycle-ratio (Class B) + kernel-NULL (Class A) + Gate-4 slope (§6), not an NMR running-of-running. The ≈9σ figure was never a landed gate.
2. **Inherited superseded scope.** §6 carried the single-scale α_s reading ("inherits the magnitude of α_s_FW modulo (Δ_B/Δ_A)²"), which is the SCALE-MISMATCH corrected in §2.1/§2.3 (the substrate-distance value is detector-facing at CMB-S4/CMB-HD, not transported to a lab NMR running by a single power of the gap ratio).
3. **Paper-original, unverified.** It was neither a derived substrate-side prediction with a pre-registered threshold nor an inventory row — neither falsifiable-as-landed nor cross-checked.

If a future session wants this observable, the correct path is a substrate-side derivation gate (substrate-derived prediction + pre-registered threshold) so that an NMR-running observable either becomes a real landed falsifier or is honestly retired. As written in S87 it was neither. The §6 of this restructured document instead expounds the actual landed Class-A/Class-B/Gate-4 surface.

---

## 11. Substrate framing audit

This document passes the substrate-framing checks:

- **Container-thinking inversion** (`phononic-framing.md`): every explanation flows substrate → bridge → laboratory; no statement treats 3He-B as fundamental and the substrate as derived.
- **Scale-and-channel tagging** (`phononic-framing.md §"Scale-and-channel-tagging"`): the α_s observable carries its matched (scale, channel) pair — substrate-distance/BZ leaf at CMB-S4/CMB-HD vs Goldstone-pivot leaf at the Planck pivot; the single-scale reading is corrected (§2.1).
- **Direction of explanation** (`cross-pillar-bridge-anatomy.md`): Substrate (Pillar I) IS the spectral triple → bridge map (χ + Connes-Karoubi) → Laboratory (Pillar IV) IN the 3He-B BdG sector.
- **Substrate-first canonical sourcing** (`substrate-first-canonical-sourcing.md`): all numerical pins (`n_s_FW_exact`, `cocycle_norm_phi67`, `cocycle_norm_phi88`, `substrate_cocycle_ratio_67_88`, `alpha_s_substrate_distance_1`, `Delta_BCS`, `tau_fold`) are sourced from `canonical_constants.py` with explicit provenance and re-verified at write time, NOT from external-paper provenance.
- **Mnemonic-vs-exact ratio discipline** (`regulator-pin-discipline.md`): the canonical ratio is cited as the Sage-exact `7.324992` (114453/15625); the F1 form `7.3249743784` and the 4-sf `7.3250` are flagged as a non-canonical direct-ratio and a band-center shorthand respectively (§3.2).
- **Evidential-grading honesty** (S97–S99): the parent→child direction is scoped as a post-hoc stipulation; universality-class membership is the load-bearing strength (§3.3).

---

## 12. References (canonical-source pins)

- `canonical_constants.py`: `n_s_FW_exact = Fraction(9561,10000)` (S88 W-15); `alpha_s_substrate_distance_1 = −0.08587279` (S92, NOT superseded); `alpha_s_pivot_goldstone = 0.0` (S92, NOT superseded); `cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.3249917525961665 = 114453/15625` (S86 W-5; re-pinned S93 W5-1); `Delta_BCS = 0.4642547394830737`; `tau_fold = 0.190`.
- **SUPERSEDED (do NOT cite as live)**: `alpha_s_framework_central`, `alpha_s_cmb_central` (S92 AH-TR-1).
- `sessions/framework/correspondence/3HeB-inheritance-canonical.md` — canonical inheritance statement (parent → child; NOT analogy); S86 W1b-T8.
- `.claude/rules/inheritance-falsifier-protocol.md` — 4-gate template + (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 W11-C5/C6 calibration).
- `.claude/rules/cross-pillar-bridge-anatomy.md` — 5 IS-not-IN elements + 3-level ladder.
- `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space" + §"Scale-and-channel-tagging".
- `sessions/permanent-results-registry.md` **§VII.W-3.LAB** — STAGE-3-PERMANENT (S100a `S100a-VIIW3LAB-STAGE2-VERIFY` PASS; audit `89eab199edaa7f908a75ce07033ab64ff2bc04279f251e1535e6b3ee43f3029e`; 11/11 clause PASS-AND; reviewers van-den-dungen × landau).
- `sessions/framework/registry/falsifier-master-inventory.md` — Rows #45/#46 (precursor), **#47–#51** (B-phase operative suite), **#52–#54b** (A-phase cross-platform); STAGE-3 anchoring update section.
- `sessions/framework/registry/falsifier-watchlist.md` §"3He-B inheritance-falsifier liaison schedule" — **CF-35** (`S90-3HE-B-LIAISON-WATCHLIST-LANDING`); the α_s two-scale row (substrate-distance −0.08587279 / Goldstone-pivot ≈0; deg(T)=+2; 13.99σ).
- `sessions/framework/Atlas/atlas-09-retractions.md` **Item 47** — α_s SCALE-AND-CHANNEL separation CORRECTION (S92 AH-TR-1 made → S93 W7-1 corrected); **Item 49** — GW→LSS flagship migration (context).
- `sessions/framework/Atlas/atlas-04-assumptions.md` **K5** — §VII.W-3.LAB STAGE-3-PERMANENT row.
- Gate `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2` PASS — BDI↔DIII morphism confirmation.
- S87 W9a-2 α_s surviving-route rank `(iii) ≻ (iv) ≻ (i) ≻ (ii)` (inventory α_s surviving-route section).
- S89 W7a `audit_sha256 = 01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` — Sage-QQ exact `n_s_FW_exact² − 1 ≡ α_s_canonical`.

---

## 13. Provenance + verdict pointers

- **Original gate (paper-mode PASS)**: `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT: PASS — value='paper_artifact_present_with_substrate_IS_prediction' scheme=single-pole-Mellin-substrate-distance-1 convention=inheritance-morphism-3He-B-BdG-canonical L_max=10 audit_sha256=1f38f9888538011cea9b71cbd0c09853b4dc7dd0e47a46e769d371eb5084f383 content_sha256=bde3ad80d7622260e8b635af06b230b88da8d7bddd77a0b2a9ab99a8f416d389 schema_version=S84+` (`computations/s87_gate_verdicts.txt`).
- **Audit script (original)**: `computations/session-87/s87_w2_3he_b_alpha_s_paper_audit.py`.
- **Operative B-phase suite gate**: `S87-W11-C5-LAB-FALSIFIER: PASS — value=7.324992 … audit_sha256=d40a8d26588a0d207ddb6adaad1f26149512e940c659ade32766054d33031a8b …` (`computations/s87_gate_verdicts.txt:176`).
- **A-phase suite gate**: `S87-W11-C6-MUSR-FALSIFIER: PASS … audit_sha256=3e8a066e1652c0c86eafa3b983e8ef99935c79c3ff8962c08017f86b6aa7c44b …` (`computations/s87_gate_verdicts.txt:167`).
- **STAGE-3 promotion gate**: `S100a-VIIW3LAB-STAGE2-VERIFY: PASS — audit_sha256=89eab199edaa7f908a75ce07033ab64ff2bc04279f251e1535e6b3ee43f3029e content_sha256=780b6f02570d5da01de6ea468166e1c8e87820a73df73f4f384a20bcff20ddd8` (`computations/session-100a/s100a_gate_verdicts.txt:45`).
- **Restructure review**: `papers/_review-s103/review-s87-3he-b.md` (Phase-1, verdict RESTRUCTURE + demote-to-companion; 2026-06-12).

This document is a substrate-physics exposition companion. The falsifiable numbers are canonical in `falsifier-master-inventory.md` (Rows #47–#54b) and `permanent-results-registry.md §VII.W-3.LAB`; this document explains them. No new physical claim is made here beyond the exposition.
