"""
One-shot Python in-place editor for §W11-5 of session-87-results-workingpaper.md.

Bypasses Edit-tool mtime-conflict gate under parallel-writer race per
.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race" (calibration corpus precedent: S86 W1c-5/6
_s86_w1c_5_wp_patcher.py / _s86_w1c_6_wp_inplace_edit.py).

Strategy: read whole file as text; replace exact stub-block string with
the substantive §W11-5 block; write whole file back atomically.
"""

import sys
from pathlib import Path

WP = Path(r"C:\sandbox\Ainulindale Exflation\sessions\archive\session-87\session-87-results-workingpaper.md")

OLD_BLOCK = """### §W11-5. S87-3HEB-EXCESS-INHERITANCE-COMPARISON (connes-ncg-theorist)

**Status**: NOT STARTED
**Gate ID**: `S87-3HEB-EXCESS-INHERITANCE-COMPARISON`
**Trigger**: `VERIFY`
**Classification**: **PHONONIC** (3He-B excess-quasiparticle inheritance comparison against substrate prediction)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The 3He-B excess-quasiparticle inheritance signature, computed under the rank-2 inheritance-kernel ker(ι_*) per `inheritance-falsifier-protocol.md`, agrees with the substrate-derived ratio 7.3250 across the decisive triplet (F1+F2+F5).
**Plan reference**: `sessions/session-plan/session-87-plan-w11.md` §W11-5.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: per-row F1/F2/F5 substrate-prediction match, ratio 7.3250 ± 0.1% verification, 4-tuple, CC1 (Δ_B/Δ_A)^p cancellation cite, CC2 cohomology-asymmetry test PASS, dual-SHA, artifacts)*

---

### §W11-6. S87-MONODROMY-DEPTH-EXTENSION (connes-ncg-theorist)"""

NEW_BLOCK = """### §W11-5. S87-3HEB-EXCESS-INHERITANCE-COMPARISON (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S87-3HEB-EXCESS-INHERITANCE-COMPARISON`
**Trigger**: `VERIFY`
**Classification**: **PHONONIC** (3He-B BdG-undoubled spectral-excess inheritance comparison against substrate prediction at the polycritical pressure point)
**Agent**: `volovik-superfluid-universe-theorist` (3He-B substrate authority per `feedback_agent-roster.md`; plan §W11-5 line 500 explicit assignment; orchestrator-flagged WP-shell attribution drift to `connes-ncg-theorist` corrected here)
**Hypothesis**: The substrate's BdG-undoubled spectral excess at first-order coexistence (τ_fold = 0.190) inherits to 3He-B at the polycritical pressure point (P_pc ≈ 21.22 bar, T_pc ≈ 2.273 mK; A-B-N triple coexistence point — Greywall 1986 + Volovik 2003 Ch.7 phase-diagram canonical) via the inheritance morphism ι : (A_K, H_K, D_K) → BdG-3He-B sector with (Δ_B/Δ_A)^p cancellation theorem at p = 0 (both observables are dimensionless ratios of countable BdG-state weights — no Δ-scaling re-weighting).
**Plan reference**: `sessions/session-plan/session-87-plan-w11.md` §W11-5.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):

- `mcp__knowledge__search_knowledge("3He-B BdG undoubled spectral excess polycritical inheritance")` → 10 hits; salient: `tau_fold = 0.19 (S80 W0-8, 3He-B inheritance)` from `s83-mu_BC-geometric-derivation.md`; `xi_E_GGE_inv = 13.642473 # 3He-B parent inheritance` from `canonical_constants.py`; `rank(E) = 3 ⇒ substrate excess is THREE-DIMENSIONAL` from `session-85-1b-3heb-inversion-landau.md`; `d_spec = 1 BdG-restricted child realization` from `3HeB-inheritance-canonical.md`. Substrate-IS canonical confirmed; no prior closure covers this specific cross-pillar inheritance-comparison gate.
- `mcp__knowledge__search_knowledge("Volovik 2003 polycritical pressure BdG quasiparticle 3He-B")` → 10 hits; salient: `# Volovik 2003 Ch. 7 weak-coupling BCS:  Δ(0)/(k_B T_c) = π e^{−γ_E} ≈ 1.7639` from `s84_w5_k_star_lab_framework_match.py`; `Measured 3He-B (p-wave, strong-coupling enhanced):  Δ/(k_B T_c) ≈ 1.96`; `coset_3HeB = Coset(G_3HeB, H_3HeB, "3He-B G/H (Volovik 2003 Ch. 7)")` from `s84_w5_landau_symmetry_class.py`. Lit-path canonical Δ ratios confirmed.
- `mcp__knowledge__search_knowledge("inheritance morphism kernel ker iota cancellation theorem cocycle 3He-B")` → 10 hits; salient: `# Substitution chain (inheritance != analogy via Connes' spectral-triple morphism iota)` and `13) "certify inheritance != analogy" theorem-level statement.` from `s86_w1b_t8_3heb_inheritance_land.py`. Inheritance-morphism canonical confirmed.
- `mcp__knowledge__get_constant("tau_fold")` → 0.19, S12/S42, gate `CONST-FREEZE-42`, NOT superseded. Used canonical pin in script.
- `mcp__knowledge__get_constant("M_KK")` → 7.428660036284456e+16 (no PROVENANCE entry — known gap; not load-bearing here, since the substrate-IS observable is a dimensionless ratio).

**Status**: NOT PRE-CLOSED — no prior gate computed substrate-IS BdG-undoubled spectral excess vs 3He-B polycritical-point laboratory observable. Proceed with computation.

**Verdict**: **FAIL** — composite (sign mismatch + magnitude over-prediction) at `ratio_mismatch = 1.029166` >> 0.25 FAIL band ceiling.

| Band     | Threshold rule (per plan §W11-5 §5)              | Outcome |
|:---------|:--------------------------------------------------|:--------|
| PASS     | ratio_mismatch ≤ 0.05                             | NO      |
| INFO     | ratio_mismatch ∈ (0.05, 0.25]                     | NO      |
| **FAIL** | **ratio_mismatch > 0.25**                         | **YES** |
| Computed | ratio_mismatch = **1.0292** (≈ 4.1× FAIL ceiling; ≈ 21× PASS ceiling) | — |

**Verdict-line dual-SHA pin** (canonical line + dual-SHA companion appended at `computations/session-87/s87_gate_verdicts.txt` lines 292-293):

- `audit_sha256` = `e1aef7ce0deaed2d85d8031fce1d009384ed0842ffb25585e880a5f475efd9aa` (full-64; short16: `e1aef7ce0deaed2d`) — closure_hash over input-pin map (canonical_constants.py + s84_spectrum_cache_L12_tau019.npz + _spectral_action_regulators.py + Volovik papers #03 + #10 + permanent-results-registry.md, tagged with gate-ID + scheme + convention + L_max + path_used).
- `content_sha256` = `9c23976f1a02b3d1e687d98f4e48f87dfcbc0ee83abafff73746267d3fe8ca1d` (full-64; short16: `9c23976f1a02b3d1`) — sha256 over JSON-serialized run-output 4-tuple.
- `schema_version` = `S84+`.

**Results**:

#### Substitution chain (re-derived per plan §W11-5 §9; verified by Python execution)

```
Step 1 (definitions):
  - sector_evals = {(p, q) → eigenvalues of D_K^2 in irrep (p, q)}, p+q ≤ L_max=10
  - C_2(p, q) = (p² + p·q + q² + 3(p+q)) / 3      [SU(3) quadratic Casimir]
  - d(p, q)   = (p+1)·(q+1)·(p+q+2)/2            [SU(3) Weyl dimension]
  - C_pole := median(C_2(p, q) over (p,q) ≠ (0,0), p+q ≤ L_max)
                = 21.3333  (substrate-distance-1 Mellin-pole scale)
  - Mellin-pole window: |C_2 − C_pole| / C_pole ≤ 0.5
  - 'paired'   = sectors inside window;  'unpaired' = sectors outside
  - N_paired_substrate   = Σ_{(p,q) paired}   d(p, q) = 2799
  - N_unpaired_substrate = Σ_{(p,q) unpaired} d(p, q) = 2205
  - δN_substrate := N_unpaired − 2·N_paired (BdG-doubling subtraction)
                  = 2205 − 5598 = −3393

Step 2 (substrate-IS observable):
  R_substrate := δN_substrate / N_paired_substrate
              = −3393 / 2799 = −1.21222

Step 3 (laboratory-IN observable, lit-path Volovik 2003 Ch.7 + Serene-Rainer 1983):
  Δ_BCS_weak / (k_B T_c) = π·e^{−γ_E} ≈ 1.7639         [weak-coupling BCS]
  SC_corr_A (P=P_pc) = 1.151;  SC_corr_B (P=P_pc) = 1.111  [strong-coupling at 21 bar]
  Δ_A / (k_B T_c) = 1.7639 × 1.151 = 2.0302
  Δ_B / (k_B T_c) = 1.7639 × 1.111 = 1.9597
  Polycritical-point coordinates: P_pc = 21.22 bar; T_pc = 2.273 mK
                                  T_pc/T_c(P_pc) = 2.273/2.491 = 0.9125
  R_3HeB_lit := (Δ_A² − Δ_B²) / (Δ_A² + Δ_B²)
              = (4.122 − 3.840) / (4.122 + 3.840)
              = 0.282 / 7.962
              = +0.03536

Step 4 ((Δ_B/Δ_A)^p cancellation theorem at p = 0):
  Both R_substrate and R_3HeB_lit are dimensionless ratios of countable
  BdG-state weights → p = 0 trivially (no Δ-scaling re-weighting).
  R_3HeB_predicted_from_substrate = R_substrate × (Δ_B/Δ_A)^0
                                  = R_substrate × 1
                                  = R_substrate

Step 5 (PASS criterion evaluation):
  |R_substrate − R_3HeB_lit| = |−1.2122 − 0.03536| = 1.24758
  max(|R_substrate|, |R_3HeB_lit|) = max(1.2122, 0.03536) = 1.2122
  ratio_mismatch = 1.24758 / 1.2122 = 1.02917

  Direction: ratio_mismatch (1.0292) >> FAIL ceiling (0.25)  →  FAIL.
```

#### Numerical results

| Quantity                       | Value            | Source                                   |
|:-------------------------------|:-----------------|:------------------------------------------|
| R_substrate                    | **−1.21222**     | Mellin-pole-window decomposition at L=10 |
| R_3HeB_lit                     | **+0.03536**     | Volovik 2003 Ch.7 + Serene-Rainer 1983   |
| ratio_mismatch                 | **1.02917**      | per plan §5 tolerance rule                |
| inheritance_kernel_rank        | 1 (effective at p=0) | rank-1 reduction of W-5 rank-2 ker(ι_*) |
| path_used                      | `lit`            | (fresh-BdG fallback NOT invoked)         |
| N_paired_substrate             | 2799             | multiplicity-weighted Casimir count       |
| N_unpaired_substrate           | 2205             | multiplicity-weighted Casimir count       |
| δN_substrate                   | −3393            | N_unpaired − 2·N_paired                   |
| C_pole (Casimir median)        | 21.3333          | substrate-distance-1 scale at L=10       |
| Δ_A at P_pc (units k_B·T_c)    | 2.0302           | weak-BCS 1.7639 × SC_A 1.151             |
| Δ_B at P_pc (units k_B·T_c)    | 1.9597           | weak-BCS 1.7639 × SC_B 1.111             |

#### 4-tuple (per plan §W11-5 §8)

`(value=1.029166e+00, scheme=Mellin-cone-substrate-distance-1-vs-Volovik-2003-polycritical, convention=BdG-undoubled-excess-ratio, L_max=10)`.

#### CC1 — (Δ_B/Δ_A)^p cancellation theorem (per `inheritance-falsifier-protocol.md`)

Both R_substrate and R_3HeB_lit are dimensionless ratios of countable BdG-state weights. Under the inheritance-morphism cancellation theorem `lab(F_i)/lab(F_j) = ‖φ_a‖/‖φ_b‖ × (f_i/f_j)` with common p_i = p_j = p, the (Δ_B/Δ_A)^p factor cancels exactly between numerator and denominator. For the BdG-undoubled-excess ratio observable here, **p = 0 trivially** (neither R_substrate nor R_3HeB_lit carries Δ-scaling — both are pure counting ratios of state weights). The cancellation theorem applies with p = 0; the substrate ratio is structurally **predicted to be preserved INTACT** in the lab measurement under any (Δ_B, Δ_A) values. Citation: `inheritance-falsifier-protocol.md` §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)" + S86 W-5 DONE-5 (machine-precision Python verification at 0.0e+00 residual). The FAIL of the equality test therefore signals a structural mismatch at the substrate-IS observable construction — NOT a lab-conversion artifact, NOT a Δ-rescaling artifact.

#### CC2 — Cohomology-asymmetry test (Class-B per `inheritance-falsifier-protocol.md`)

The W-5 calibration rank-2 ker(ι_*) carries two cocycles (φ_67 chiral pair + φ_88 Cartan hypercharge) with Sage-exact ratio ‖φ_67‖/‖φ_88‖ = 7.324992. For this gate's effective rank-1 ker(ι_*) at the p=0 ratio observable (only the Cartan U(1)_φ cocycle survives; chiral-pair generators cancel under the dimensionless ratio because their multiplicity-weighted contributions enter symmetrically into both numerator and denominator), the cohomology-asymmetry test is **structurally vacuous** — a single cocycle norm is a single number, not a ratio. Per `inheritance-falsifier-protocol.md` §"Why both classes are required": "If both lab observables return NULL, no ratio can be computed — the test is vacuous". The rank-1 reduction here forces Class-A (kernel-signature equality) to be the sole diagnostic; **the Class-A FAIL is therefore decisive without a Class-B counter-balance**. The 103% mismatch reading on Class-A alone is structurally insufficient to invoke W-5's 4-gate falsifier template (which requires Class-B preservation for non-vacuous discrimination); the cohomology-asymmetry test outcome is **FAIL-vacuous** at rank-1, consistent with the Class-A FAIL.

---

#### Cross-pillar bridge anatomy declaration (calibration corpus instance #2 to `.claude/rules/cross-pillar-bridge-anatomy.md`)

Per the STRUCTURAL REQUIREMENT (`cross-pillar-bridge-anatomy.md` §"IS-not-IN Anatomy (5 elements)" + §"Three-Tier Structural-Confidence Ladder"), all 5 anatomy elements + 3-level ladder are declared explicitly. **Instance #1**: S86 W-5 §VII.W (Pillar III ↔ IV; HP^1 cohomology ↔ Peotta-Törmä quantum-metric trace). **This gate (W11-5) is calibration corpus instance #2** (substrate-IS Pillar I/II spectral-excess ↔ 3He-B Pillar V BdG-quasiparticle laboratory at polycritical point). K-counter advances: **K = 1 → 2** (toward MANDATORY promotion at K = 3 per `feedback_rules-compensate-missing-structure.md`).

##### 5 IS-not-IN anatomy elements

1. **Substrate-IS observable**: `δN_BdG_substrate(τ_fold) = N_unpaired(τ_fold) − 2·N_paired(τ_fold)` evaluated on the multiplicity-weighted Casimir spectrum of `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` via the Mellin-cone substrate-distance-1 pole at C_pole = 21.3333. Numerical: δN_substrate = −3393, N_paired_substrate = 2799, R_substrate = −1.2122. The substrate **IS** this dimensionless excess ratio; it is not "in" any cosmological container. Per `phononic-framing.md` §"IS Space, Not IN Space": the substrate's spectral-action moment IS the BdG-undoubled excess; there is no pre-existing geometric container "around" the spectral triple holding this observable.

2. **Laboratory-IN observable**: 3He-B BdG-undoubled spectral excess at the polycritical point P_pc ≈ 21.22 bar, T_pc ≈ 2.273 mK (Greywall 1986 PRB 33, 7520 + Volovik 2003 Ch.7 phase-diagram triple point — A-B-N coexistence). Computed as `R_3HeB_lit = (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²)` with strong-coupling-corrected gap ratios Δ_A/(k_B T_c) = 2.0302, Δ_B/(k_B T_c) = 1.9597 (Volovik 2003 Ch.7 + Serene-Rainer 1983). Numerical: R_3HeB_lit = +0.03536. The laboratory measures this quantity **IN** the 3He cryostat container (e.g., Lancaster MCT-3, Helsinki ROTA, Aalto LTL cells) under (P, T) sweep at the A-B-N triple point.

3. **Bridge map**: inheritance morphism ι : (A_K, H_K, D_K) → BdG-3He-B sector per `inheritance-falsifier-protocol.md`, projecting A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) (M_3(ℂ) → 0 in ker(ι_*)). At the p = 0 dimensionless-ratio observable, the (Δ_B/Δ_A)^p cancellation theorem reduces the bridge to direct ratio-preservation: `R_3HeB_predicted = R_substrate × 1`. The bridge map is the inheritance-morphism (Connes spectral-triple morphism), NOT an analogy — per `phononic-framing.md` §"Cross-pillar bridge anatomy" + `3HeB-inheritance-canonical.md` (S86 W1b-T8): substrate IS the parent algebra; 3He-B IS the child realization, NOT a metaphor.

4. **Algebraic envelope**: at leading order in the inheritance-kernel rank-truncation (rank-1 effective at p = 0), R_3HeB_predicted = R_substrate to machine precision; the rank-1 truncation envelope is 0% deviation in the limit ker(ι_*) M_3(ℂ) Cartan-zone contributions are sub-leading. Sub-leading corrections from non-negligible M_3(ℂ) Cartan-zone weight bound the discrepancy at ≤ 5% per Volovik 2003 Ch.7 reported lit-uncertainty band (strong-coupling factors at 21 bar carry ~3-5% systematic per Serene-Rainer 1983). **Level-2 envelope: 0.05.** The empirical Level-3 measurement (1.029) **violates this envelope by ~21×** → the rank-1 effective-truncation assumption FAILS at L_max=10 in this scheme; M_3(ℂ) Cartan-zone contributions are **NOT** sub-leading at the multiplicity-weighted Mellin-pole-window decomposition.

5. **Empirical anchor**: Volovik 2003 Ch.7 reported gap-ratio at polycritical point (Δ_A, Δ_B) yields R_3HeB_lit = +0.0354 (positive, ~3.5% gap-asymmetry between A and B at coexistence). Substrate prediction R_substrate = −1.2122. Ratio mismatch 1.029 fails the 5% PASS band by a factor of ~21× (4.1× the FAIL ceiling of 0.25). **Level-3 anchor: 1.029.**

##### 3-level structural-confidence ladder

| Tier | Form                                              | Status / value at L_max=10                       |
|:-----|:--------------------------------------------------|:-------------------------------------------------|
| **Level 1** | Substrate-IS structural identity (regulator-invariant; cohomology-class level): `R_substrate = ‖δN_BdG‖_{spectral-distance-1 Mellin pole} / ‖N_paired‖`, dimensionless ratio on multiplicity-weighted Casimir spectrum. | STRUCTURAL THEOREM — regulator-invariant in the analytic-continuation sense (numerator and denominator are both Mellin-window counts on the same Casimir spectrum; the Mellin-window-fraction parameter 0.5 is a scheme choice — varying it within (0.3, 0.7) is a sensitivity carry-forward; structural form invariant). |
| **Level 2** | Algebraic convergence envelope (L_max-dependent; rank-1 effective ker(ι_*) → ratio preservation at leading order). | STRUCTURAL PREDICTION — bound: ≤ 0.05 (5%) at L_max = 10, given rank-1 effective-truncation assumption + Volovik lit ±5% systematic. |
| **Level 3** | Empirical anchor at canonical L_max = 10. | EMPIRICAL — `ratio_mismatch = 1.029`; **Level 3 (1.029) FAILS Level 2 (0.05) by ~21×**. |

**Registry-PASS criterion** (`cross-pillar-bridge-anatomy.md` §"Registry-PASS criterion"): Level-3 numerical value < Level-2 envelope at canonical L_max. Here: 1.029 ≮ 0.05 → **REGISTRY-FAIL**. Per the rule: "If Level 3 violates Level 2, the bridge theorem entry FAILs registry-PASS (the empirical observation does not lie inside the algebraic prediction)". This bridge entry is **NOT registry-eligible** at the falsifier-master-inventory; it is **NOT** a §VII.AJ candidate. The structural cause: M_3(ℂ) Cartan-zone contributions are non-negligible at L_max = 10 in the multiplicity-weighted Mellin-pole-window scheme, falsifying the rank-1 effective-truncation assumption that underwrites Level 2.

##### Direction of explanation (per `phononic-framing.md` §"IS Space, Not IN Space" mandatory reframe)

```
Substrate (Pillar I) IS the BdG-undoubled spectral excess R_substrate
   →  Bridge map (ι : A_K = C ⊕ H ⊕ M_3(C) → M_2(C); p=0 cancellation)
   →  Laboratory (Pillar V; 3He-B cryostat at P_pc, T_pc) IN the polycritical-point gap-asymmetry R_3HeB_lit
```

Inverting this direction (treating the 3He-B laboratory observable as fundamental and the substrate prediction as derived) is a container-thinking violation per `phononic-framing.md`. The FAIL signal flows substrate → bridge → laboratory: the substrate's structural prediction does NOT match the laboratory measurement at this scheme/L_max, so the bridge map is not faithful at L_max = 10 in the multiplicity-weighted Mellin-pole-window decomposition. The laboratory measurement (R_3HeB_lit = +0.035) is correct; the substrate's substrate-IS construction (R_substrate = −1.21) under this scheme is the locus of the FAIL.

**Substrate framing**: the substrate IS the BdG-undoubled spectral-excess observable — there is no pre-existing 4D spacetime container "around" the spectral triple in which excess states "live"; the multiplicity-weighted Casimir spectrum at C_pole IS the spectral content. The 3He-B cryostat laboratory measures IN a continuum geometric container (the helium cell at well-defined (P, T)) under a sweep of the canonical (Pressure, Temperature) thermodynamic axes; the polycritical point is a geometric point IN that container. The IS-not-IN distinction is structural: R_substrate is one finite-L spectral-triple structural number; R_3HeB_lit is one continuum measurement at one (P, T) point.

---

#### Solution-space interpretation (per plan §W11-5 §10 FAIL clause + `math-scripts.md` §"All Results Are Good Results")

The FAIL closes the corridor "the multiplicity-weighted Mellin-pole-window decomposition on the SU(3) Casimir spectrum at L_max = 10 is the substrate-IS analog of the 3He-B BdG-undoubled excess at the polycritical point". Per plan §W11-5 §10 FAIL branch: "ratio mismatch > 25% — inheritance morphism does NOT preserve the spectral-excess structure into 3He-B at polycritical pressure. Closes the corridor 'substrate's spectral-excess prediction is universal (in the inheritance-morphism sense)'; substrate's prediction is τ_fold-specific (or platform-specific to the substrate's own SU(3) fiber). Forces re-examination of inheritance kernel ker(ι_*) — the M_3(ℂ) sub-algebra contributions may not be negligible."

**Two structurally separable contributions to the FAIL**:

1. **Sign mismatch (dominant)**: R_substrate = −1.21 (negative; "unpaired-poor" partition because SU(3) Weyl-dimension multiplicities concentrate at low Casimir below the median); R_3HeB_lit = +0.035 (positive; A-phase gap exceeds B-phase gap by ≈ 3.5%). The substrate's multiplicity-weighted decomposition does not reproduce the **sign** of the 3He-B coexistence gap-asymmetry — δN_substrate = −3393 is dominated by Cartan-zone sectors clustering below C_pole. The sign mismatch alone disqualifies the scheme from the PASS band regardless of magnitude.

2. **Magnitude mismatch (sub-dominant)**: even with a hypothetical sign-corrected variant, |R_substrate| = 1.21 ≫ |R_3HeB_lit| = 0.035, a ~34× over-prediction. The substrate's "excess area" at the Mellin pole is two orders of magnitude larger than the lit-path gap-asymmetry. The Mellin-pole window captures bulk Cartan-zone (M_3(ℂ)) contributions that have no 3He-B BdG-quasiparticle correspondent at coexistence (3He-B BdG sector is M_2(ℂ); M_3(ℂ) is in ker(ι_*) and disappears under the inheritance morphism).

**Implication for the inheritance-morphism program**: substrate's BdG-undoubled spectral-excess prediction at L_max = 10 in this scheme is **NOT** a universal-inheritance observable. The "universal inheritance" interpretation (substrate's prediction transfers to 3He-B unchanged under the (Δ_B/Δ_A)^0 cancellation) FAILS because the substrate-IS construction at this scheme carries M_3(ℂ) Cartan-zone weight that the BdG-3He-B sector child algebra ι(A_K) = M_2(ℂ) does not project onto. The 3He-B inheritance is real (per S86 W1b-T8 canonical) — but the **specific observable** "BdG-undoubled spectral excess at first-order coexistence" requires pre-projection of the M_3(ℂ) Cartan zone before Mellin-pole-window decomposition, otherwise the substrate-side calculation includes contributions that the inheritance morphism subsequently kills.

**What this FAIL is NOT**: this FAIL does NOT undermine the `3HeB-inheritance-canonical.md` (S86 W1b-T8) inheritance-vs-analogy theorem. The inheritance morphism ι is structurally well-defined; the FAIL is at the level of the **specific spectral-excess observable construction**, not at the bridge map itself. The (Δ_B/Δ_A)^0 cancellation theorem (CC1) holds as stated — both observables are dimensionless ratios. The W-5 cohomology-asymmetry calibration ratio 7.3250 (rank-2 ker(ι_*)) is unaffected. Only the corridor "substrate's spectral-excess prediction is universal under naive multiplicity-weighted Mellin-pole-window scheme" is closed.

---

#### Carry-forward (per `feedback_fix-in-session-never-defer.md` 4-field spec)

1. **What**: re-run substrate-IS observable with explicit M_3(ℂ) Cartan-zone pre-projection BEFORE Mellin-pole-window decomposition; test whether projecting out the ker(ι_*) ⊃ M_3(ℂ) Cartan zone brings R_substrate into the PASS band against R_3HeB_lit. Hypothesis: post-projection R_substrate ≈ R_3HeB_lit at relative ≤ 5% (matches lit ±5%).
2. **Inputs**: cached `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (D_K(τ_fold) sector eigenvalues); M_3(ℂ) Cartan-zone projector matrix (constructable from sector identification — Cartan zone = (p = q ≠ 0) sectors at the level of SU(3) irrep block-diagonalization); Volovik 2003 Ch.7 strong-coupling factors (already canonical at SC_corr_A = 1.151, SC_corr_B = 1.111 at P_pc = 21.22 bar).
3. **Gate**: `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY` — PASS if `ratio_mismatch_M3C_projected ≤ 0.05`; INFO if (0.05, 0.25]; FAIL > 0.25. Pre-registered threshold identical to W11-5 ratio band.
4. **Effort**: ~3-5h (single substrate-side recomputation with one-line M_3(ℂ) projector insertion; lit-path R_3HeB_lit is canonical and reusable).

#### Artifacts (verified on disk before TaskUpdate; SHAs match verdict-line dual-SHA)

- **Script**: `computations/session-87/s87_w11_3heb_excess_inheritance_comparison.py` (21,052 bytes; ~440 lines; canonical-constants imports from `canonical_constants.py`; uses `_spectral_action_regulators._enumerate_sectors` for SU(3) Casimir sectors).
- **Data**: `computations/session-87/s87_w11_3heb_excess_inheritance_comparison.npz` (5,012 bytes; keys: `R_substrate=-1.21222`, `R_3HeB_lit=0.03536`, `ratio_mismatch=1.02917`, `inheritance_kernel_rank=1`, `path_used=lit`, plus diagnostics: `N_paired_substrate=2799`, `N_unpaired_substrate=2205`, `delta_N_substrate=-3393`, `C_pole=21.3333`, `Delta_A_at_pc=2.0302`, `Delta_B_at_pc=1.9597`, `P_pc_bar=21.22`, `T_pc_mK=2.273`, `L_max=10`, `verdict=FAIL`, `audit_sha`, `content_sha`).
- **Plot**: `computations/session-87/s87_w11_3heb_excess_inheritance_comparison.png` (51,993 bytes; bar comparison of R_substrate vs R_3HeB_lit with uncertainty bands ±1% substrate Mellin-window systematic, ±5% Volovik lit; FAIL-band shading; ratio_mismatch annotation).
- **Verdict line**: appended to `computations/session-87/s87_gate_verdicts.txt` (canonical line + dual-SHA companion at lines 292-293).

---

### §W11-6. S87-MONODROMY-DEPTH-EXTENSION (connes-ncg-theorist)"""


def main():
    text = WP.read_text(encoding="utf-8")
    if OLD_BLOCK not in text:
        print("ERROR: stub block not found in working paper. Aborting (no write).", file=sys.stderr)
        # Diagnostic: check for the key signature lines
        if "### §W11-5. S87-3HEB-EXCESS-INHERITANCE-COMPARISON" in text:
            print("§W11-5 heading present, but stub block has been modified.", file=sys.stderr)
        return 1
    if "### §W11-5. S87-3HEB-EXCESS-INHERITANCE-COMPARISON (volovik" in text:
        print("ERROR: §W11-5 already populated by volovik. Aborting (no write).", file=sys.stderr)
        return 2
    new_text = text.replace(OLD_BLOCK, NEW_BLOCK, 1)
    if new_text == text:
        print("ERROR: replace produced no change. Aborting.", file=sys.stderr)
        return 3
    WP.write_text(new_text, encoding="utf-8")
    delta = len(new_text) - len(text)
    print(f"OK. Delta size: {delta:+d} bytes.")
    print(f"  old text size: {len(text)}")
    print(f"  new text size: {len(new_text)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
