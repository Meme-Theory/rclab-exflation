# S84 Solo Synthesis — Structural-Elimination Bulletins (Gen-Physicist, S-3/1-of-2)

**Agent**: gen-physicist (cross-domain workhorse)
**Slot**: S-3 solo synthesis, 1 of 2
**Focus**: five S84 structurally-significant FAILs, each recast as a Structural-Elimination Bulletin (H_FALSE / H_SURVIVING / evidence class / solution-space delta)
**Source docs**: `sessions/archive/session-84/session-84-synthesis-collation.md` (primary) + W1 / W4 / W6 / W7 / W10 working papers
**Date**: 2026-04-20

Classification frame: constraint mapping per `.claude/rules/epistemic-discipline.md`. PASS and FAIL are equally informative; what matters is the structural position of each closed mechanism relative to surviving corridors. Substrate framing per `.claude/rules/phononic-framing.md`: explanations flow from D_K eigenvalues → spectral action moments → emergent physics; never GR-as-container.

---

## §I. Scope and Method

S84 closed 127 gate verdicts across 10 waves (`computations/s84_gate_verdicts.txt`). Most FAILs are expected confirmation-of-wall results at pre-registered thresholds (e.g., W1a-2 F_supp_max 56 ppt short; W4-37 σ(n_T) boundary; W4-43 SKA-1 SNR 71.8× below 2). Five FAILs are different in kind: they each **eliminate a named physical or methodological path** from the solution-space map. This document lifts each into an explicit bulletin form so the corpus carries the closure as a load-bearing wall, not as a tally entry.

Bulletin fields (mandatory for each of the 5):
- **(a) H_FALSE**: the closed mechanism written as an explicit hypothesis now false.
- **(b) H_SURVIVING**: enumerated surviving mechanisms / corridors inheriting the load.
- **(c) Evidence class**: one of {ALGEBRAIC theorem, METHODOLOGICAL redirect, STRUCTURAL FAILURE, PLAN-DEFECT}.
- **(d) Solution-space delta**: dimensionality reduction with explicit count.

Direction claims follow `.claude/rules/math-scripts.md` substitution-chain discipline. Quantitative ratios Python-verified in the working notebook before statement.

---

## §II. Structural-Elimination Bulletins (5)

### §II.1 — W1a-3 SV2 — Branch-(iv) w_0 = −0.842 RETRACTED

**Verdict line**: `S84-W0-REGULATOR-RESOLUTION-SV2: FAIL -- value=10.077109 scheme=zeta convention=branch-iv L_max=8 sha256=e1843c278cad62bebffc2e16905eec15247f74aa8cb5870f00de231c56593ffc`

**Numerical evidence**: R_JE = ξ_J / ξ_E_GGE drifts 0.4536 (L=5) → 1.041 (L=6) → 2.411 (L=7) → 4.985 (L=8). L=8/L=5 ratio = **10.99×** (Python: 4.985/0.4536 = 10.98986…). PASS band [0.40, 0.50] breach at L=6 is **+108.2%** above ceiling ((1.041−0.50)/0.50). Mellin-cone Connes-Moscovici s=3 residue differences 1.91e4 → 3.11e4 → 3.84e4 — **not monotone-decaying** (Cauchy-tail check fails).

**Substitution chain for the direction claim** (ξ_E_GGE drop → R_JE growth, Josephson sector inverts dominance):

- Step 1 (definitions). ξ_J := (Zubarev-dressed Josephson response) / (zeta-bare Josephson response) = 0.008911, TB-pinned at τ_fold from (Δ_BCS, μ, τ_fold), STRUCTURALLY L-independent (BCS 32-mode TB Hamiltonian has no D_K sector-truncation label).  ξ_E_GGE(L) := S_Zub_E(L) / S_ζ_E(L) with S_X_E(L) the energy-weighted second-moment spectral sum truncated at L_max.
- Step 2 (substitute). R_JE(L) = ξ_J / ξ_E_GGE(L) = 0.008911 / ξ_E_GGE(L).
- Step 3 (L-scaling). S_ζ_E(L) ~ L^4 (polynomial multiplicity times linear-λ weight). S_Zub_E(L) Gaussian-saturates beyond λ ~ 1. Therefore ξ_E_GGE(L) = S_Zub_E(L) / S_ζ_E(L) falls as 1/L^4-corrected from L=5 upward.
- Step 4 (simplify). ξ_E_GGE(5) / ξ_E_GGE(8) = R_JE(8) / R_JE(5) = 4.985 / 0.4536 = 10.99. Therefore ξ_E_GGE has dropped by 11× between L=5 and L=8.
- Step 5 (direction). ξ_E_GGE ↓ ⇒ R_JE = ξ_J / ξ_E_GGE ↑ monotonically. At L=6 already R_JE = 1.041 > 0.50 PASS ceiling by factor 2.08. At L=8 the Josephson sector dominates the GGE sector by factor 4.985 (INVERTED from the L=5 ordering R_JE = 0.4536 where GGE dominated). Under Josephson dominance, w_0 is pushed TOWARD −1 (pure Josephson limit); branch (iv)'s claim w_0 = −0.842 (above −1) is directionally false in the L→∞ limit.

**Bulletin (W1a-3)**:

- **(a) H_FALSE**: "Branch (iv) of the w_0 regulator-resolution tree is a stable canonical — the L_max=5 value w_0 = −0.842454, derived under the SDW-KMS mixed scheme with Zubarev-J and ζ-GGE dressings, persists as the framework's single zero-free-parameter prediction for w_0 (Jensen-phase equation of state) across L_max ∈ {5, 6, 7, 8}, with R_JE stable in [0.40, 0.50]."

- **(b) H_SURVIVING**:
  1. **H-SUR-1.1**: At L_max ≥ 8, the Josephson-dominant regime (ξ_J > ξ_E_GGE) supports a different branch family whose w_0 converges toward the Zubarev-at-L=9 value −0.997 (framework is driven toward pure Josephson limit).
  2. **H-SUR-1.2**: The zeta-at-L=9 limit −0.494 remains a candidate if the regulator family re-canonicalizes on ζ (would require re-closing branches (i)/(ii) which were closed by W0-workshop Md1 asymptotic + monotone-family argument).
  3. **H-SUR-1.3**: An alternative non-Zubarev / non-ζ regulator (e.g., SDW-KMS extended, heat-kernel direct, or one of the 8 MP-admissible regulators from W7b-81) could anchor a genuinely L-stable branch; W4-CF.5 Zubarev-convergence-to-(−1) and W4-CF.7 SDW-L_max extension are the pre-registered probes.
  4. **H-SUR-1.4**: w_0 is permanently UNSPECIFIED pending S85 re-audit (per plan reversion protocol); R_842 rectangle [−0.942, −0.742] × [−0.2, 0.2] remains locked as infrastructural commitment (no resizing per LOCKOUT-C), but its physical anchoring is conditional on S85 branch re-audit.

- **(c) Evidence class**: **STRUCTURAL FAILURE** (not PLAN-DEFECT). The reversion protocol is plan-specified and triggered correctly; the defect is physical — the L_max=5 anchor is a truncation artifact of a divergent Mellin-cone sampling. The Cauchy-tail check (CC-v) failing non-monotone independently certifies the spectral-functional choice is on a non-convergent sampling of its own tower. Not METHODOLOGICAL-REDIRECT: the methodology (PRDR-pinned SV chain with L ∈ {5,6,7,8} probes) worked as designed; it found a wall.

- **(d) Solution-space delta**:
  - Eliminated: branch-(iv) single-value canonical at L=5 (one point in the (regulator × branch × L) 3-cube).
  - Provisionally eliminated (pending re-audit): SDW-KMS mixed-scheme branch family at L_max < 8 (the whole L=5-anchored sub-tree).
  - Dimensionality reduction count: **1 point eliminated (the L=5 anchor) + 1 branch-sub-tree provisionally closed**; the w_0 enumeration space at L_max ≥ 8 is **re-opened** under an inverted ξ_J / ξ_E_GGE covariance ordering — the surviving corridor is NEW, not retained. Net effect on the 3-cube: L=5 slice lost; L≥8 Josephson-dominant slice newly promoted to primary.
  - Collateral closure: SV3 (Δ_BCS cusp scan) and SV4 (τ off-fold scan) ABORTED as vacuous (scanning sensitivity of a retracted branch). Collateral preservation: SV5 (R_842 rectangle migration audit bookkeeping) PASS independent.

**Cascade pointer**: feeds W1b-9 DR3-RESPONSE-PROTOCOL (R_842 physical-anchor interpretation deferred to S85) and W4-46 (SCHEME-DEPENDENT flag for w_0 becomes permanent under companion evidence from L-convergence scan). See §III cascade.

---

### §II.2 — W4-46 — w_0 Scheme-Dependence is STRUCTURAL

**Verdict line**: `W4-46 | S84-G51-LMAX-CONVERGENCE | split growth factor 6.22× (L=5→9) | Zubarev-E-weighted | structural FAIL (not truncation artifact)`  — closure SHA head `72d522e3…0f5f99`.

**Numerical evidence**: split(L) ≡ w_0^ζ(L) − w_0^Z(L): split(5) = +0.0809, split(7) = +0.3390, split(9) = +0.5028. |split(9)|/|split(5)| = **6.22×** (Python: 0.5028/0.0809 = 6.215…). Monotone-increasing, not asymptotically shrinking. Zubarev-L9 → −0.997; zeta-L9 → −0.494.

**Substitution chain** (already written out in W4 §VII.2 S-2; re-verified):

- Step 1 (definition). split(L) ≡ w_0^ζ(L) − w_0^Z(L). w_0^R(L) is the canonical-candidate derived at D_K truncation L_max=L with spectral-action regulator R ∈ {ζ, Zubarev}.
- Step 2 (substitute). split(5) = (−0.917227) − (−0.998116) = +0.080889. split(7) = (−0.658001) − (−0.997025) = +0.339023. split(9) = (−0.493961) − (−0.996783) = +0.502822.
- Step 3 (simplify). |split(L)| is monotone-increasing in L across the scanned points: 0.081 < 0.339 < 0.503. Ratio |split(9)|/|split(5)| = 6.22 (NOT 1 + O(L^{−k}) decay).
- Step 4 (direction). |split(L)| ↑ as L ↑ (growing, not shrinking) ⇒ split is structural, not a truncation artifact. No single ζ-vs-Zubarev L_max regime produces a common limit; the two regulators converge to DIFFERENT w_0 values.

**Bulletin (W4-46)**:

- **(a) H_FALSE**: "w_0 is a zero-free-parameter framework prediction — the canonical value w0_FW = −0.918 (L=5, heat-kernel-matched regulator) is the substrate's single unambiguous equation-of-state prediction, regulator-invariant modulo a truncation artifact that will shrink as L_max increases; increasing L_max will close the zeta/Zubarev gap."

- **(b) H_SURVIVING**:
  1. **H-SUR-2.1**: w_0 is PERMANENTLY SCHEME-DEPENDENT (per W4-48 rigor-registry entry, flag upgraded from "pending W4-46" to definitive). No single ZFP prediction exists; the framework's honest evidence column at w_0 carries a SCHEME-DEPENDENT tag, not a ZFP tag.
  2. **H-SUR-2.2**: Both limits (Zubarev-L9 → −0.997, zeta-L9 → −0.494) remain physically admissible — they represent two different regulator families' limit values. Neither is the canonical; both are outputs of a legitimate spectral-action choice.
  3. **H-SUR-2.3**: A Zubarev-convergence-to-(−1) analytic corollary (CF-W4.5) may upgrade H-SUR-2.2 to a Zubarev-only ZFP if Zubarev regulator structurally forces w_0 → −1 as L_max → ∞. Open S85 gate.
  4. **H-SUR-2.4**: Observational binding: DR3 outcome interpretation becomes regulator-conditional. R_842 (centered −0.842, half-width 0.1) locked as infrastructural commitment, but W4-CF.2 successor tree layers a regulator-conditional branch on top (sequential pre-registration clause in W4-49).

- **(c) Evidence class**: **STRUCTURAL FAILURE**. The L-scan methodology is clean (two regulators, three L_max points, same script, consistent convention). The failure is a physical property of the spectral-action moments, not a plan defect or methodology artifact.

- **(d) Solution-space delta**:
  - Eliminated: the ZFP-column entry for w_0. Under the falsifier-rigor-registry taxonomy (W4-48), row 11 moves from pending-ZFP to definitive SCHEME-DEPENDENT. **ZFP-count stays at 11/18**, not 12/18.
  - Dimensionality reduction count: **1 evidence-column slot eliminated** (w_0 from ZFP → SCHEME-DEPENDENT); **2 regulator-conditional w_0 corridors opened** (Zubarev-limit, ζ-limit). The solution space GAINS dimensionality at the regulator axis while LOSING dimensionality at the evidence axis.
  - Meta-consequence: establishes the precedent that spectral-moment-derived observables can be regulator-sensitive at the moment-label (here a_2-related w_0 integration), not just at the prefactor level. Feeds W6-67 f_conv cluster reclassification as companion evidence.

**Cascade pointer**: feeds S85 CF-W4.1 regulator-invariance taxonomy (every a_k tagged regulator-invariant or regulator-sensitive); cascades into W2-CF.5 Zubarev L_max convergence carry-forward.

---

### §II.3 — W7a-74 — det(P)=1 is NOT K-theoretically Witten-liftable

**Verdict line**: `S84-DET-P-K-THEORY: FAIL -- homotopy_level=1 scheme=Kasparov_KK convention=Witten_1998 L_max=NA` — closure SHA head `def5d0cd…`.

**Numerical evidence**: 4 independent obstructions identified:
1. KO-dim gap: Witten K-theory uses complex K^0 of 10D spacetime; framework's det(P)=1 lives in KO-dim=6. Complexification kills the KO-torsion class (Z/2 → 0), breaking the map.
2. Rank mismatch: framework's K_0(A_F) rank = 3 (from ℂ⊕ℍ⊕M_3(ℂ)); Witten's Type IIB D-brane K_0 rank = 1 per normalization. 16.0/1.0 = 16.0 rank-gap.
3. Torsion mismatch: Witten's KO^6 carries Z/2 torsion essential for anomaly cancellation. Framework's det(P)=1 is torsion-free. Any uplift to real K-theory requires a class the framework doesn't carry; any uplift to complex K-theory kills the torsion Witten needs.
4. Normalization incompatibility: the framework's Poincaré pairing det(P)=1 does NOT map to Witten's anomaly integral (single-brane charge +1 vs framework det=1 from 3×1 Dirac pairing).

**Substitution chain for homotopy-level classification**:

- Step 1 (definition). homotopy_level ∈ {0 = no map, 1 = weak Z-linear map, 2 = classifying-space equivalence, 3 = structure-preserving map at K_0}. Pre-registered pass-rule: homotopy_level ≥ 2 ⇒ PASS.
- Step 2 (substitute). Level-3 test: rank-preserving? 3 ≠ 1. FAIL. Level-2 test: classifying-space homotopy equivalent? complexification kills torsion. FAIL. Level-1 test: weak Z-linear map (ignoring torsion and normalization)? rank-3 → rank-1 projection exists trivially. PASS.
- Step 3 (simplify). homotopy_level = 1 (weak only).
- Step 4 (direction). homotopy_level = 1 < 2 ⇒ FAIL per pre-registered threshold.

**Bulletin (W7a-74)**:

- **(a) H_FALSE**: "The framework's K-theoretic identity det(P) = 1 (Poincaré duality pairing of the KO-dim=6 spectral triple) admits a structure-preserving uplift to Witten's 1998 D-brane anomaly-cancellation identity via a Kasparov KK-map phi: KK^6(A_F, A_F°) → K^0(M^4 × X_fiber). The framework's spectral-triple identity is inheritable from, or structurally isomorphic to, the string-theoretic K-theoretic content."

- **(b) H_SURVIVING**:
  1. **H-SUR-3.1**: The framework's det(P)=1 is **framework-independent**: it is the Poincaré pairing of a KO-dim=6 NCG spectral triple, not a special case of Witten's 10D KO^6 Z/2-torsion identity. Surviving meaning: det(P)=1 derives its content purely from Connes-Chamseddine-Marcolli A_F = ℂ⊕ℍ⊕M_3(ℂ) axioms + KO-dim=6 (W8 §W8-87b singleton theorem), not from any string-theoretic uplift.
  2. **H-SUR-3.2**: Witten-1998 anomaly cancellation and framework det(P)=1 are ANTI-CORRESPONDENCE entries in the W7b-78 correspondence table (11 ANTI / 5 GENUINE / 12 STRUCTURAL / 3 SUGGESTIVE). The relationship is structural distinctness, not structural identity.
  3. **H-SUR-3.3**: W7a-72 HET-DECOMP PASS (16/16 hypercharge-matched) and W7a-73 FTH-UPLIFT INFO (framework base_dim=12 incompatible with F-theory's canonical 6) together with W7a-74 FAIL establish the "rep-content guest, structural stranger" pattern: framework SM content admits heterotic decomposition at the representation level only, while spectral-triple identity and compactification geometry remain framework-independent.
  4. **H-SUR-3.4**: The framework's structural-uniqueness claim (§VII.O landed post-W7b-83) does not rely on string-theoretic uplift; the 4-proof chain (Mellin-cone singleton, CCM KO-dim=6 sign table, power-law b_finiteL with SDW asymptote, twist-triple non-extension) is self-contained.

- **(c) Evidence class**: **ALGEBRAIC theorem** (closure by 4 algebraic obstructions, each independent). This is the cleanest of the five closures: the failure lives at the level of K-theoretic rank and torsion invariants, which are topological obstructions — permanent once established.

- **(d) Solution-space delta**:
  - Eliminated: one class of "uplift-to-parent" hypotheses (Witten 1998 K-theory route specifically). The broader "string-uplift" class is also narrowed: Witten 1998 is the closest K-theoretic neighbor in the string literature; its closure hardens the case that NO string construction simultaneously matches (KO-dim=6 irreducible-rep structure AND |E_cond(L)| ~ L^b with b ∈ [4.58, 4.78] at L=3..8 AND b → 7 asymptotic) — the two-scale falsifier from §VII.O.
  - Dimensionality reduction count: **1 uplift-class eliminated** (K-theoretic Witten route); **65-paper equivalence-class catalog** (W7a-79) now carries stronger evidentiary weight since the "obvious" uplift candidate is closed. Solution-space region of string-uplift-candidate frameworks: one large sub-region (Witten K-theoretic route) definitively closed.
  - Feeds the framework's "structural stranger" position: framework lives in the solution space alone at the spectral-triple level, shared only in SM-rep-content with heterotic.

**Cascade pointer**: feeds §VII.O two-scale falsifier (strengthened by closing the closest K-theoretic neighbor) and W7a-79 EQUIV-CLASS-FALSIF (65-paper catalog extends monotone-provisionally to S85–S90).

---

### §II.4 — W6-67 — Z_R Counterterm DOES NOT EXIST at a_2 Slot

**Verdict line**: `S84-Z-R-COUNTERTERM-EXISTENCE: FAIL -- value=107466.188041 scheme=zeta-reference convention=heat-kernel-matching L_max=5 sha256=67b3761187b49e805588f6903718922f9c0210f55c98230abeaf285957ff510a`

**Numerical evidence**: cluster_Z_a2 = **107,466** at L_max=5; grows with L_max (Python-verified): 1234 (L=3) → 1.07e5 (L=5) → 1.41e7 (L=7). Growth factor 3→5 is **86.7×**; growth factor 5→7 is **132×** (ratio ACCELERATING, not saturating).

**Substitution chain** (from W6-67 §VII.B Step 4-7, re-verified):

- Step 1 (definition). Z_R := multiplicative counterterm for regulator R, defined by Z_R = f_conv^ζ / f_conv^R (zeta-reference convention, CC-1 PASS by construction Z_ζ = 1). cluster_Z_a2 := max_R(Z_R · a_2^R) / min_R(Z_R · a_2^R) across R ∈ {ζ, Zubarev, SDW, dim-reg, lattice-BR}.
- Step 2 (algebraic substitute). f_conv = π^4 / (9216 · M_0²), so Z_R · a_2^R = (M_0^R / M_0^ζ)² · a_2^R. Numerics: M_0²·a_2 values are 1.44e13 (zeta/dim-reg/lattice-BR), 1.34e8 (Zubarev), 5.81e12 (SDW).
- Step 3 (simplify). cluster_Z_a2 = max(M_0^R² · a_2^R) / min(M_0^R² · a_2^R) = 1.4431e+13 / 1.3429e+08 = 1.0747e+5.
- Step 4 (L-scan direction). cluster_Z_a2(L=3) = 1234; cluster_Z_a2(L=5) = 1.07e5; cluster_Z_a2(L=7) = 1.41e7. Substitute: 1.41e7/1.07e5 = 131.8, and 1.07e5/1234 = 86.7. Direction: cluster_Z_a2 GROWS with L_max, and the growth factor ACCELERATES (131.8 > 86.7). Not truncation-asymptotic.
- Step 5 (threshold direction). Pre-registered FAIL threshold: cluster_Z_a2 ≥ 2.5. Substitute 1.07e5. Direction: FAIL by 4.63 OOM at L=5, worsening with L.

**Bulletin (W6-67)**:

- **(a) H_FALSE**: "A multiplicative counterterm Z_R exists such that Z_R · f_conv^R (zeroth Mellin moment) and Z_R · a_2^R (second Seeley-DeWitt moment) are simultaneously R-protected (balanced across the 5-regulator family {ζ, Zubarev, SDW, dim-reg, lattice-BR}) at L_max=5. Equivalently: the S83-G28 f_conv cluster=1766 is an un-dressed-coupling artifact repairable by single-scalar multiplicative renormalization."

- **(b) H_SURVIVING**:
  1. **H-SUR-4.1**: The renormalization obstruction is **VERTICAL** (regulator-dependent a_2 at a specific Mellin slot), NOT **PERTURBATIVE** (1/N-series divergence). The f_conv slot has a regulator-dependent a_2 response that cannot be corrected by any single-scalar dressing — the correction required would have to be rank-matrix (simultaneously rescaling M_0 and a_2 independently), which is not what "multiplicative counterterm" means in heat-kernel matching.
  2. **H-SUR-4.2**: S83-G28 f_conv cluster=1766 is reclassified: NOT un-dressed-coupling artifact; IS **STRUCTURAL REGULATOR OBSTRUCTION**. Retroactive reclassification is part of the structural harvest.
  3. **H-SUR-4.3**: 2-loop heat-kernel expansion OR alternative non-multiplicative counterterm structure (e.g., mixed-rotation rather than rescaling) OR formal certification of f_conv as physically scheme-dependent (G48 falsifier class extension) remain open (CF-W7.1 = D.1).
  4. **H-SUR-4.4**: R-protected atlas (W6-68) remains PASS on all 10 intrinsic atlas entries + 2 new k=2 + 1 bonus k=4. The R-protection meta-principle (§VII.K-META) stands; f_conv is now **excluded** from the atlas rather than a claimed-balanced entry retroactively dressed.
  5. **H-SUR-4.5**: A_s = 5.08e-9 field-theoretic amplitude closure remains intact at the field-sector dressing level (W6-69 clause-(b) FI at machine ε, W6-70 1/N_field convergent); the obstruction is specifically at the f_conv / a_2 slot pair, not in the 1/N-series.

- **(c) Evidence class**: **STRUCTURAL FAILURE**. The failure is a structural property of the 5-regulator family's second-moment responses at L=5 — and L-worsens, ruling out truncation artifact. Not ALGEBRAIC theorem: the failure is quantitative (threshold-based). Not PLAN-DEFECT: the plan is correctly constructed; the physics is the culprit. Companion evidence class to W4-46 (both vertical regulator-dependences at specific spectral-moment slots).

- **(d) Solution-space delta**:
  - Eliminated: the "multiplicative single-scalar Z_R dressing" class of f_conv rescue hypotheses. This is NOT equivalent to eliminating "R-protection for f_conv": the latter could still be recovered via 2-loop, non-multiplicative, or rotation-type counterterms — surviving corridor H-SUR-4.3.
  - Dimensionality reduction count: **1 counterterm-class eliminated** (single-scalar multiplicative) + **1 reclassification of S83-G28** (1766 cluster from un-dressed-coupling → structural regulator obstruction). The 5-regulator × 2-moment response map at f_conv / a_2 is now known to be rank-inseparable under single-scalar dressing.
  - Feeds W6-71 Mellin-balance-pre-declaration template: f_conv is now correctly flagged as a "claimed-balanced-but-unbalanced" precedent (alongside historical G15/G28/G34), validating the template by construction.

**Cascade pointer**: feeds W7 D.1 (2-loop investigation OR alternative renormalization scheme OR G48 falsifier extension) and the A_s SCHEME-DEPENDENT flag in W4-48 (row 8). Couples with W4-46 as the two vertical regulator-dependence results of the session.

---

### §II.5 — W10-119 — Γ1' Near-Stationarity PREDICATE INCOMPATIBLE with τ_fold Definition

**Verdict line**: `S84-ALTERNATIVE-TAU-MESH-UNIQUENESS: FAIL -- value=(0/2001 joint; 2001/2001 Γ5'; 1/2001 Γ6; 0/2001 Γ1')` — FAIL is on a broken predicate.

**Numerical evidence** (from W10-119 tables 932–935):

| Gear | Criterion | Mesh cardinality |
|:-----|:----------|:-----------------|
| Γ1' | `|dS/dτ(τ)| / |dS_fold| < 1.34e-3` | **0 / 2001** |
| Γ5' | `d²S/dτ²(τ) > 0` | 2001 / 2001 |
| Γ6 | `|3/(3+exp(12τ)) − s²_pin| ≤ 1e-4` | **1 / 2001** (uniquely picks τ = 0.190) |
| JOINT | (Γ1' ∧ Γ5' ∧ Γ6) | **0 / 2001** |

**Substitution chain — Γ1' empty cardinality** (reproducing W10-119 §substitution, Python-verified):

- Step 1 (definition). Γ1'(τ) := |dS/dτ(τ)| / |dS_fold|. dS_fold := +58,672.80 (canonical, S42 permanent, nonzero by van Hove / first-order-transit definition of τ_fold). d²S_fold := +317,862.85 (S70 canonical).
- Step 2 (Taylor model). dS/dτ(τ) ≈ dS_fold + d²S_fold · (τ − τ_fold) = 58,672.80 + 317,862.85 · (τ − 0.190).
- Step 3 (substitute into Γ1'). Γ1'(τ) = |58,672.80 + 317,862.85 · (τ − 0.190)| / 58,672.80 = |1 + 5.4174 · (τ − 0.190)|.
- Step 4 (solve Γ1'(τ) < 1.34e-3). |1 + 5.4174 · (τ − 0.190)| < 1.34e-3. ⇒ τ ∈ (0.190 + (−1 − 1.34e-3)/5.4174, 0.190 + (−1 + 1.34e-3)/5.4174) = **(0.005162, 0.005657)**. (Python-verified: tlow = 0.0051622549…, thigh = 0.0056569572…)
- Step 5 (simplify). The Γ1' acceptance band (0.005162, 0.005657) lies ENTIRELY OUTSIDE the search interval [0.10, 0.30] by a factor of ~19 (the near-stationarity band is near τ ≈ 0.005, not τ = 0.190). Python-verified: thigh = 0.00566 < 0.10.
- Step 6 (direction). Γ1' selects the dS/dτ = 0 stationarity zero (≈ τ = 0.00541 per the Taylor model); this is NOT τ_fold. τ_fold is defined as a van Hove singularity / first-order-transit point with definitionally NONZERO dS_fold. The predicate "where is dS/dτ ≈ 0?" and the framework answer "at τ_fold" are STRUCTURALLY MUTUALLY EXCLUSIVE.

**Bulletin (W10-119)**:

- **(a) H_FALSE**: "A triple-gear uniqueness machinery of the form (Γ1' near-stationarity ∧ Γ5' convexity ∧ Γ6 cubic-BC) uniquely selects τ_fold = 0.190 on the mesh, because τ_fold is a stationary point of the Jensen-flow spectral action S(τ) where dS/dτ ≈ 0 and d²S/dτ² > 0 — the standard differential-topology critical-point characterization applies."

- **(b) H_SURVIVING**:
  1. **H-SUR-5.1**: τ_fold = 0.190 IS unique on the mesh under **Γ6 alone** (cubic-BC pin at a=12). Single-gear uniqueness is recoverable without invoking Γ1'; Γ6 cardinality = 1 with τ = 0.190 exact (0 mesh-step deviation).
  2. **H-SUR-5.2**: τ_fold is **NOT** a smooth-extremum critical point of the bare spectral action. It is a van Hove cusp of the eigenvalue density ρ(λ; τ) / first-order transit point. The operative S85 target is a van Hove-cusp theorem reformulation (S85-VAN-HOVE-CUSP-THEOREM from W8-85 audit + W9b-105 FAIL analysis).
  3. **H-SUR-5.3**: An alternative triple-gear using a transit-character identifier (e.g., curvature-consistency `|d²S/dτ²(τ) − d2S_fold|/d2S_fold < ε`, or van Hove density lock) could re-establish the triple-gear picture without the stationarity-mismatch defect. Open S85 target.
  4. **H-SUR-5.4**: §VII-B gear registry's cubic-BC entry at a=12 retains the load-bearing role it already had; Γ5' convexity (2001/2001) remains the d²S-positivity check; what is retracted is Γ1' (the stationarity member of the triple-gear). Same structural fact was unanimously identified in W8a-85 by three independent audits (connes-ncg, baptista, spectral-geometer).

- **(c) Evidence class**: **PLAN-DEFECT**. The plan's Γ1' definition contradicts the framework's τ_fold definition. This is a plan-authoring error at the predicate level, not a physics failure and not a methodology failure. The dispatched agent refused to convention-shop a PASS (PROHIBITED_ACTIONS §1), produced the structural diagnosis instead, and recorded the FAIL correctly per `.claude/rules/gate-verdicts.md`. Same class as W8-85 and W8-90 (plan-defect family — 3 occurrences this session). Plan-level audit S85-PLAN-PRDR-CONSISTENCY-CHECK pre-registered to prevent recurrence.

- **(d) Solution-space delta**:
  - Eliminated: the "smooth-extremum τ_fold" hypothesis (τ_fold as interior critical point of bare CC Gaussian spectral action). This class was already weakened by W8-85 FAIL + 3-agent audit; W10-119 delivers the structured predicate-level confirmation.
  - Dimensionality reduction count: **1 plan-predicate eliminated** (Γ1' as stationarity gear); **τ_fold uniqueness under Γ6 alone promoted** from "sufficient condition" to "the only operative condition". Net: the gear-machine triple gets down-ranked to single-gear-sufficient at τ_fold, simplifying the uniqueness machinery.
  - Collateral: the "plan-defect" taxonomy now has 3 members this session (W8-85, W8-90, W10-119). This motivates the pre-registered S85-PLAN-PRDR-CONSISTENCY-CHECK audit (hypothesis IMPLIES or CONTRADICTS each cross-check?) as a structural plan-layer upgrade.

**Cascade pointer**: feeds S85-VAN-HOVE-CUSP-THEOREM (from W8-85 carry-forward) and S85-PLAN-PRDR-CONSISTENCY-CHECK. Consistent with W9b-105 spectral-dimension FAIL at d_spec = 4.895 (both results trace to the van Hove / first-order-transit character of τ_fold, not to a smooth-differential-geometry picture).

---

## §III. Structural-Eliminations Cascade Timeline

The five closures do not stand alone; three independent dependency chains link them.

**Chain A — Regulator-dependence cascade (W1a-3 → W4-46 → W6-67)**:

W1a-3 SV2 FAIL establishes that branch (iv)'s L=5 anchor is on a non-convergent Mellin-cone sampling (ξ_E_GGE drops 11× across L ∈ {5,6,7,8}). W4-46 establishes that the zeta-vs-Zubarev split of w_0 grows 6.22× across L ∈ {5,7,9} — so regulator differences are structural, not truncation. W6-67 establishes that at the a_2 Seeley-DeWitt slot, cluster_Z_a2 grows from 1234 (L=3) to 1.41e7 (L=7), making the f_conv / a_2 vertical regulator-dependence structural. **Joint reading**: three independent probes (branch-tree stability, w_0 regulator-split, f_conv / a_2 counterterm) all FAIL on the same structural ground — the spectral-action moments are regulator-sensitive at specific Mellin slots, and the sensitivity DOES NOT vanish with increasing L_max.

Directional cascade: W1a-3 **casts conditional shadow on R_842 anchor** (rectangle's physical interpretation now pending S85 re-audit); W4-46 **cascades into W2-CF.5 Zubarev-L_max-convergence** (open S85 probe of whether Zubarev converges to w_0 = −1 structurally); W6-67 **feeds W7 D.1 2-loop investigation** (surviving rescue path).

**Chain B — Structural-stranger closure (W7a-74)**:

Closes the closest K-theoretic neighbor to the framework's spectral-triple identity. Combined with W7a-72 PASS (heterotic rep-content) and W7a-73 INFO (F-theory base-dim incompatible), the **"rep-content guest, structural stranger" pattern** is now a three-point characterization. Feeds §VII.O two-scale falsifier (structurally strengthened — the best K-theoretic uplift candidate is shown to be an ANTI-CORRESPONDENCE, not a GENUINE correspondence).

**Chain C — Plan-defect family (W10-119 → W8-85 → W8-90)**:

W10-119 is the third plan-defect FAIL of the session, joining W8-85 (stationarity hypothesis contradicting cross-check #2's nonzero dS_fold) and W8-90 (inherited plan-defect). All three trace to the same conceptual error: treating τ_fold as a smooth-critical-point of a differentiable action rather than as a van Hove cusp / first-order-transit point. **Joint cascade**: motivates S85-VAN-HOVE-CUSP-THEOREM (unified positive reformulation) and S85-PLAN-PRDR-CONSISTENCY-CHECK (plan-layer predicate-audit tool).

---

## §IV. Aggregate Solution-Space Delta Post-5-Eliminations

Counting each bulletin's (d) entry:

- W1a-3: 1 L=5 anchor point eliminated + 1 branch-sub-tree provisionally closed (L≥8 regime newly primary).
- W4-46: 1 ZFP evidence-column slot eliminated (w_0 → SCHEME-DEPENDENT) + 2 regulator-conditional corridors opened.
- W7a-74: 1 uplift-class eliminated (Witten K-theoretic route).
- W6-67: 1 counterterm-class eliminated (single-scalar multiplicative Z_R) + 1 reclassification (S83-G28 cluster from un-dressed-coupling to structural regulator obstruction).
- W10-119: 1 plan-predicate eliminated (Γ1' stationarity gear) + 1 promotion (τ_fold uniqueness under Γ6 alone).

**Aggregate closure count**: 5 distinct physical/methodological paths definitively eliminated. 2 newly-opened / newly-promoted surviving corridors (W1a-3 L≥8 Josephson-dominant regime; W10-119 Γ6 single-gear uniqueness). 2 regulator-conditional corridors preserved pending S85 (W4-46 Zubarev-limit, ζ-limit). 1 rescue path open pending 2-loop probe (W6-67 H-SUR-4.3).

Per `.claude/rules/epistemic-discipline.md` evidence hierarchy: **the constraint surface after W-5 eliminations is a STRICTLY MORE CONSTRAINED region of the solution space** (5 paths closed), with **DIMENSIONAL REORGANIZATION** (2 newly-primary corridors at the w_0 / Josephson axes and the τ_fold-uniqueness axis) rather than simple dimensionality reduction. This is the profile of a session that advances the map in both walls and windows, not just walls.

---

## §V. Pre-Registered Next-Elimination Gates (Carry-Forward, 4-field)

Each surviving corridor from §II carries its own failure mode. If that surviving path also fails, the next-elimination gate is pre-registered here per `.claude/rules/session-handoffs.md` mandatory-carry-forward.

| # | What | Inputs | Gate | Effort |
|:--|:-----|:-------|:-----|:-------|
| ELIM-1 | S85 branch-(iv) re-audit at L_max ∈ {8, 10, 12} under inverted Josephson-dominant regime (H-SUR-1.1 probe) | W1a-3 SV2 .npz; L_max=10 D_K eigenspectrum cache; Zubarev regulator infrastructure | S85-W0-BRANCH-REAUDIT: PASS iff R_JE(L≥10) stabilizes in [4.5, 5.5] (Josephson-dominant asymptote); FAIL iff drift persists (closes entire branch family) | 1.5 session (L=10 GPU eigvalsh per L_max; ~10-12h torch.linalg batch) |
| ELIM-2 | Zubarev-convergence-to-(−1) analytic corollary (CF-W4.5, H-SUR-2.3 probe) | W4-46 L=5,7,9 data; Zubarev regulator formal definition | S85-ZUBAREV-W0-LIMIT: PASS iff analytic proof w_0^Z → −1 as L→∞ with explicit rate OR numerical extrapolation band ±0.01; FAIL iff no structural forcing (w_0 stays genuinely SCHEME-DEPENDENT with no ZFP rescue) | 1 session |
| ELIM-3 | Extended equivalence-class falsifier catalog S85–S90 (65 → 150 papers) for W7a-79 (H-SUR-3.2 hardening) | W7a-79 65-paper catalog baseline; arXiv + zbMATH + MathSciNet search pipes | S90-EQUIV-CLASS-150: PASS iff falsification_count stays 0 at 150 papers; FAIL iff any matching construction found (would falsify §VII.O uniqueness claim) | 6-month literature review, distributed across S85–S90 |
| ELIM-4 | 2-loop Z_R heat-kernel expansion OR non-multiplicative counterterm scan (H-SUR-4.3 probe) | W6-67 data + L_max={3,5,7} scan; Connes-Chamseddine a_2 regulator-invariance theorem; spectral-action RG flow from S80 | S85-Z-R-2LOOP: PASS iff 2-loop or mixed-rotation Z_R structure balances cluster_Z_a2 < 2.5; FAIL iff certifies f_conv as physically SCHEME-DEPENDENT (G48 falsifier class extension) | HIGH — 2 sessions |
| ELIM-5 | Van Hove-cusp τ_fold theorem reformulation (unified closure of W10-119 + W8-85 + W8-90 plan-defect family) | W8-85 3-audit synthesis; W9b-105 d_spec FAIL analysis; ρ(λ; τ) eigenvalue-density framework | S85-VAN-HOVE-CUSP: PASS iff τ_fold uniquely recovered as cusp of ρ(λ; τ) with stated smoothness class; FAIL iff no unified positive reformulation (τ_fold stays empirical with causal-censorship pairing only) | 1 session |
| ELIM-6 | Plan-layer PRDR consistency audit tool (hypothesis IMPLIES or CONTRADICTS each cross-check?) | 3 plan-defect instances (W8-85, W8-90, W10-119); PRU cardinality audit infrastructure from W9a-97 | S85-PLAN-PRDR-CONSISTENCY: PASS iff tool flags all 3 known cases + at least 1 novel case in S85 plan pre-freeze; FAIL iff tool misses any of the 3 known precedents | 1 session |
| ELIM-7 | DR3 regulator-conditional successor tree (CF-W4.2, H-SUR-2.4 probe) | W4-44 frozen JSON; W4-46 w_0^Zubarev(L=9) = −0.997 | S85-DR3-SUCCESSOR: PASS iff layered branch SHA-pinned without parent re-registration; FAIL iff registration collision with R_842 LOCKOUT-C | 2-3h |
| ELIM-8 | W0-regulator-invariance taxonomy (CF-W4.1, companion probe to ELIM-4) | S84 W4-46 numerics; S83 G51 NPZ; SV1 KK-sign resolution | S85-REGULATOR-INVARIANCE-TAXONOMY: PASS iff every a_k tagged regulator-invariant or regulator-sensitive; FAIL iff any a_k carries mixed classification (would reveal more W4-46-class structural failures latent in the moment ledger) | 10-12h (L=9 GPU required per moment) |

---

## §VI. Classification Sign-Off

Per `.claude/rules/phononic-framing.md` — each bulletin's physics classification:

- **W1a-3**: PHONONIC (Josephson / GGE phononic sectors ξ_J / ξ_E_GGE are direct excitations of D_K); GEOMETRIC at the regulator-sensitivity level.
- **W4-46**: GEOMETRIC (w_0 derives from spectral-moment a_2-related integration; regulator-sensitivity is a property of the spectral triple's heat-kernel expansion).
- **W7a-74**: GEOMETRIC (K-theoretic identity det(P)=1 is a property of the spectral triple's Poincaré pairing; W8 §W8-87b singleton theorem establishes this uniquely).
- **W6-67**: GEOMETRIC (Seeley-DeWitt heat-kernel expansion is geometric property of (D_K, H, A_F); closure at regulator-kernel-moment-independence).
- **W10-119**: GEOMETRIC (τ_fold as van Hove cusp of ρ(λ; τ) is a property of the eigenvalue density of D_K under Jensen deformation — substrate structure, not a property of an emergent field theory).

All five bulletins sit on the fabric side of the IS/IN-space distinction. None explains substrate via GR; none treats the fabric as something IN a container. W10-119 specifically inverts the GR default ("τ_fold is a critical point of an action on a manifold") to the substrate picture ("τ_fold is a van Hove cusp of the eigenvalue density of D_K under Jensen deformation"), which was already the W8-85 3-agent audit consensus.

---

## §VII. Artifact Pointers (on-disk verification)

- W1a-3 SV2 data: `computations/s84_w1a_w0_sv2.npz` (referenced in W1 §W1-3.SV2 line 582)
- W4-46 Zubarev-E-weighted L-scan: `computations/s84_gate_verdicts.txt` line 316 (closure SHA `72d522e3…0f5f99`)
- W7a-74: `computations/s84_w7a_det_p_k_theory.py` + npz (W7 §W7-74)
- W6-67: `computations/s84_w6_z_r_counterterm.npz` (9,865 bytes) + `s84_w6_z_r_counterterm.png` (101,591 bytes), closure SHA head `67b37611…`
- W10-119: data in W10 §W10-119 tables; closure in `computations/s84_gate_verdicts.txt`; linked to W8-85 3-agent audit record

Primary source: `sessions/archive/session-84/session-84-synthesis-collation.md` (131,249 bytes).

---

*End of S84 solo S-3 elimination synthesis (gen-physicist, 1 of 2). Five bulletins, three cascade chains, aggregate solution-space delta tallied, eight next-elimination gates pre-registered for S85. No probability statements, no PASS/FAIL ratio, no session-wide master-gate tally — per `.claude/rules/epistemic-discipline.md`. Written ONLY to this output file.*
