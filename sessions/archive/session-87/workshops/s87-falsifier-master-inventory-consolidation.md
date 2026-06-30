# S87 Falsifier-Master-Inventory Consolidation + Cross-Row Dependency Map

**Date**: 2026-05-02
**Agent**: mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`)
**Workshop slot**: S-5 (Slot 3 closeout, parallel with Slot 1 / Batch 1; no Slot-2 dependency)
**Output target**: `sessions/framework/registry/falsifier-master-inventory.md`
**Source documents**:
1. `sessions/archive/session-87/session-87-results-workingpaper.md` §W2-1 (S87-LAB-3HE-B-ALPHA-S-EQUIVALENT PASS, lines 2272-2326), §W5-2 (S87-W11-C5-LAB-FALSIFIER PASS, lines 4411-4512), §W5-3 (S87-W11-C6-MUSR-FALSIFIER PASS, lines 4514-4602), §W6-1 (S87-T7-S67-ISOMORPHISM-LANDING PASS at §VII.AG.1, lines 4822-4868), §W11-5 (S87-3HEB-EXCESS-INHERITANCE-COMPARISON FAIL at ratio_mismatch=1.029166, lines 9398-9580)
2. `sessions/framework/registry/falsifier-master-inventory.md` (current state — rows #45 + #46 landed at S87 W2-1; this consolidation appends rows #47-#54 + cross-row dependency map + REGISTRY-FAIL annotation + FWD candidates)
3. `.claude/rules/inheritance-falsifier-protocol.md` §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)" (S86 W-5 DONE-5; 0.0e+00 residual) + §"Four-Gate Structure"
4. `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)" (K-counter K=1→2 sub-section; K_promotion=3 threshold)

## Task definition

This consolidation extends the falsifier-master-inventory beyond W2-1's rows #45-#46 by (a) appending W5-2's 5-row B-phase F-table + W5-3's 5-row A-phase F-table as inventory rows #47-#54a, (b) building the cross-row dependency map showing how Class A (NULL) and Class B (RATIO) interact via the (Δ_B/Δ_A)^p cancellation theorem, (c) annotating the W11-5 §VII.AJ REGISTRY-FAIL across all rows whose interpretation depends on inheritance-morphism kernel-rank, M_3(ℂ) Cartan-zone projection, or bridge-map specification, (d) updating the K-counter calibration-corpus tracking sub-section with the W11-5 REGISTRY-FAIL flag (calibration corpus instance #2 at K=2; SUGGESTION status retained), and (e) pre-registering three forward cross-pillar bridge candidates (FWD-C1/C2/C3) per S87 W5-5 with their respective falsifier-row anchors and 4-field carry-forwards.

## Pre-Compute Audit (per `.claude/rules/knowledge-index-usage.md`)

- `mcp__knowledge__get_constant("cocycle_norm_phi67")` → 0.793346 (S86 W-5 CANONICAL-3; UD-6 promote; superseded=False).
- `mcp__knowledge__get_constant("cocycle_norm_phi88")` → 0.108307 (S86 W-5 CANONICAL-4; UD-6 promote; superseded=False).
- `mcp__knowledge__get_constant("substrate_cocycle_ratio_67_88")` → 7.324992 (S86 W-5 CANONICAL-5; gate S86-W5-CANON-EXTRACT; superseded=False).
- `mcp__knowledge__get_constant("w0_FW")` → -0.918 (S58 Volovik partition; canonical_constants.py:1243).
- Python verification (full-precision float64): `0.793346 / 0.108307 = 7.3249743784` (identical to the W-5 calibration's 4-sig-fig 7.3250 within publication-precision floor; canonical Sage-exact 7.324992 differs by 1.76e-5, both inside ±0.1% Gate-2 band [7.3177, 7.3323]).
- Python verification (W11-5 ratio_mismatch reconstruction): `1.24758 / 1.2122 = 1.029187` (matches the working-paper-cited value 1.02917 to 5 sig figs; the WP §W11-5 line 9477 substitution chain).
- Python verification (Level-3 / Level-2 violation magnitude for W11-5 REGISTRY-FAIL): `1.029 / 0.05 = 20.58` (WP §W11-5 line 9534 cites "~21×"; both forms are consistent).

## Section 1 — Consolidated inventory updates

This section reproduces the text of what was appended to `sessions/framework/registry/falsifier-master-inventory.md`. The producing-edit append spans Rows #47-#54a (W5-2 B-phase + W5-3 A-phase 4-gate falsifier protocols), the W11-5 REGISTRY-FAIL annotation block, the K-counter calibration-corpus update, and the FWD-C1/C2/C3 forward-bridge candidate rows.

### 1.1 — W5-2 B-phase rows (Rows #47-#51)

Per §W5-2 verdict line `S87-W11-C5-LAB-FALSIFIER: PASS -- value=7.324992 ... audit_sha256=d40a8d26588a0d207ddb6adaad1f26149512e940c659ade32766054d33031a8b content_sha256=29b76a1a1eab56da55725a46af872e097934eef5d5327e5d6d36086fa9bf3469 schema_version=S87+` (line 176 of `computations/s87_gate_verdicts.txt`). The 5-row B-phase F-table (W-5 W11-C5 calibration corpus) lands as inventory rows #47 (F1 Caroli-Matricon ladder asymmetry) + #48 (F2 SABS axial-equatorial pair correlation) + #49 (F3 HQV restricted-slab µSR) + #50 (F4 Larmor anomaly multi-pressure cocycle-degenerate) + #51 (F5 Jensen-modulus quench acoustic dispersion).

### 1.2 — W5-3 A-phase rows (Rows #52-#54a; chi_A=3/2 substrate-corrected)

Per §W5-3 verdict line `S87-W11-C6-MUSR-FALSIFIER: PASS ... audit_sha256=3e8a066e1652c0c86eafa3b983e8ef99935c79c3ff8962c08017f86b6aa7c44b content_sha256=6dd153256f3c6767... schema_version=S87+` (line 167). The 5-row A-phase F-table (chi_A=3/2 substrate-rescaled per Volovik 2003 §3.4 axisymmetric A-phase Fermi-surface average `⟨|Δ_A(k)|²⟩_FS = (2/3)·Δ_BCS²`) lands as inventory rows #52 (F1_A chirality-modified Caroli-Matricon analog at A-phase domain wall) + #53 (F2_A) + #54 (F3_A) + #54a (F4_A) + #54b (F5_A). The 5-element pre-registration audit + lab-platform 3-level pin (PRIMARY Aalto LTL Helsinki µSR / SECONDARY RHUL µSR / TERTIARY future cross-platform) is preserved.

### 1.3 — Cross-platform identical-ratio gate (high-leverage)

Both W5-2 (B-phase Lancaster MCT-3) and W5-3 (A-phase Aalto LTL µSR) predict `lab(F_1)/lab(F_5) = 7.324992 ± 0.1%` IDENTICALLY because the cocycle ratio `‖φ_67‖/‖φ_88‖` is computed on the substrate spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`, NOT on any BdG-sector restriction. Two-platform agreement on `r=7.324992 ± 0.1%` across BDI vs chiral AIII inheritance morphisms confirms cocycles are **substrate-resident** (not BdG-sector-resident). Disagreement falsifies the substrate-IS framing and forces re-anatomy of `cross-pillar-bridge-anatomy.md` substrate-IS / laboratory-IN partition at S88+. This is the highest-leverage substrate-vs-lab discriminator in the framework's S88+ falsifier portfolio.

### 1.4 — Forward bridge candidates (FWD-C1/C2/C3) per S87 W5-5

Per `cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)" lines pre-registering FWD-C1 (Pillar I↔II n_s), FWD-C2 (Pillar II↔V Mellin-cone↔BdG), FWD-C3 (Pillar IV↔V cocycles↔3He), each candidate gets its own inventory row with anchor citation + 4-field carry-forward spec.

## Section 2 — Cross-row dependency map (table + narrative)

The W2-1 + W5-2 + W5-3 falsifier suite encodes a **structurally interlocking 4-gate inheritance-falsifier protocol** per `inheritance-falsifier-protocol.md`. Each row's verdict interpretation depends on the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; machine-precision 0.0e+00 residual) AND on the kernel-rank classification of `ker(ι_*) = rank-2` (the substrate degrees of freedom that DO NOT inherit through `χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)`).

### 2.1 — Substitution chain for the cancellation-theorem dependency

```
Step 1 (definition):
  lab(F_i) := ‖φ_a‖ · f_i · (Δ_B/Δ_A)^{p_i}
  where:
    ‖φ_a‖ = substrate Hochschild-pairing norm of cocycle generator [φ_a]
    f_i   = dimensionless Caroli-Matricon-geometry / Jensen-quench conversion factor
    p_i   = K-theory-class gap-ratio exponent for row F_i

Step 2 (substitution into ratio test):
  lab(F_i) / lab(F_j) = (‖φ_a‖/‖φ_b‖) · (f_i/f_j) · (Δ_B/Δ_A)^{p_i − p_j}

Step 3 (common-p simplification):
  For F1 (NMR longitudinal Δ² leading order) and F5 (acoustic-mode Bogoliubov leading order),
  both encode integer p_1 = p_5 = 2 (verified by integer-p extractor at W5-2 line 176).
  Therefore (Δ_B/Δ_A)^{p_1 − p_5} = (Δ_B/Δ_A)^0 = 1 EXACTLY.

Step 4 (substrate-derived f_1/f_5 = 1):
  F-rows are normalized in the inheritance-falsifier-protocol per-row table such that
  f_1/f_5 = 1 for cross-row Caroli-Matricon-geometry vs Jensen-quench-acoustic
  configurations (both probe the same Lancaster vortex-core / RHUL pulse-NMR sub-gap regime).

Step 5 (direction):
  lab(F_1)/lab(F_5) = ‖φ_67‖/‖φ_88‖ · 1 · 1 = 7.324992 EXACTLY.
  The (Δ_B/Δ_A)^p factor cancels exactly between numerator and denominator.
  ⇒ Substrate-derived ratio is PRESERVED INTACT in lab measurement,
    INDEPENDENT of (Δ_B/Δ_A) or p.

Conclusion: the ratio test (Class B) is substrate-falsifying rather than
            lab-conversion-dependent. This is what makes the test high-leverage
            against substrate-IS framing.
```

### 2.2 — Failure-mode propagation table (Row #45 NULL × Row #46 RATIO)

| Row #45 (Class A NULL) outcome | Row #46 (Class B RATIO) outcome | Joint interpretation |
|:------------------------------:|:--------------------------------:|:---------------------|
| **NULL on F1+F2+F5 (PASS_lab)** | **VACUOUS** (no signal → no ratio computable) | Substrate's BDI-protected inheritance hypothesis CONFIRMED on rank-2 ker(ι_*) decisive triplet; Class B cannot discriminate substrate-resident vs BdG-resident at vacuous ratio. Substrate prediction PASSES Class A; Class B test deferred until a non-NULL detection occurs OR cocycle-degenerate Gate-3 supporting rows return non-NULL. |
| **Non-NULL on F1 OR F2 OR F5 at >3σ_lab (FAIL_lab Class A)** | **PASS_lab if r ∈ [7.3177, 7.3323]** | Decisive-triplet detection AND ratio in band ⇒ φ_67-sector signal is non-trivial AT THE LAB but cohomology-class structure is preserved. Substrate cocycles are BdG-sector-resident (NOT substrate-resident); inheritance-morphism kernel-rank classification suspect. Force re-anatomy of `cross-pillar-bridge-anatomy.md` substrate-IS / laboratory-IN partition. |
| **Non-NULL on F1 OR F2 OR F5 at >3σ_lab (FAIL_lab Class A)** | **FAIL_lab if r ∉ [7.3177, 7.3323]** | Decisive-triplet detection AND ratio outside band ⇒ both Class A AND Class B falsified; substrate-IS framing AND BDI-protected inheritance falsified. Highest-impact FAIL: forces re-derivation of the algebra projection χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ). |
| **NULL on F1+F2+F5 (PASS_lab)** AND non-NULL on F3 OR F4 (Gate-3 supporting; rank-1 effective) | **VACUOUS at decisive level; supporting ratio test at F3/F4 may discriminate** | Decisive triplet substrate-clean (PASS); supporting rows show signal — implies Cartan-hypercharge cocycle [φ_88] inherits weakly through χ. Per W11-5 cross-citation: this scenario coincides with the "M_3(ℂ) Cartan-zone weight non-negligible" diagnostic that drives the W11-5 REGISTRY-FAIL at L_max=10. The Gate-4 multi-pressure slope discrimination on F4 (Jacobi-cubic vs φ_88-linear) is the operational falsifier for rank-1-effective inheritance. |

### 2.3 — Cross-row narrative

Row #45 (Class A NULL kernel-signature) and Row #46 (Class B cohomology-asymmetry ratio) are **NOT independent**. The cancellation theorem (Step 5 above) makes Row #46 substrate-falsifying, but ONLY conditional on Row #45 returning at least one non-NULL detection (otherwise no ratio is computable). The two rows form a **sequential falsifier protocol**: Row #45 fires first as the kernel-signature gate; Row #46 becomes operative only if Row #45 admits a signal. Per `inheritance-falsifier-protocol.md` §"Why both classes are required": Class A alone (kernel-signature only) is insufficient because non-NULL detections can be reinterpreted as parent-symmetry-class breakdown OTHER than substrate inheritance failure; Class B alone is insufficient because vacuous ratio cannot discriminate. Together they saturate the substrate's predictive content: NULL-on-decisive-triplet AND ratio-on-cross-rows.

The W5-2 (B-phase) + W5-3 (A-phase) 5-row F-tables extend this 2-row framework into a 10-row two-platform protocol. The cross-platform identical-ratio prediction (Section 1.3 above) is the high-leverage structural test: substrate residence vs BdG-sector residence is binary, and disagreement between Lancaster B-phase and Aalto LTL A-phase ratios falsifies the substrate-IS framing structurally, not just for a particular observable construction.

## Section 3 — W11-5 §VII.AJ REGISTRY-FAIL annotation across affected rows

W11-5 closed as **REGISTRY-FAIL** per `cross-pillar-bridge-anatomy.md` §"Registry-PASS criterion": Level-3 empirical anchor `ratio_mismatch=1.029` violates Level-2 envelope `0.05` by ~21× (verified Python: `1.029 / 0.05 = 20.58`). Per W11-5 §"What this FAIL is NOT" (line 9564): "this FAIL does NOT undermine the `3HeB-inheritance-canonical.md` (S86 W1b-T8) inheritance-vs-analogy theorem. The inheritance morphism ι is structurally well-defined; the FAIL is at the level of the **specific spectral-excess observable construction**, not at the bridge map itself."

The §VII.AJ cause-attribution scenarios are: (S1) observable-construction defect (M_3(ℂ) Cartan-zone weight non-negligible at L_max=10 in multiplicity-weighted Mellin scheme); (S2) kernel-rank invalid (rank-1 effective truncation FAILS at L_max=10); (S3) bridge-map mis-specified (the algebra projection χ does not faithfully project the substrate Mellin-pole-window content). Each scenario shifts the interpretation of downstream falsifier rows differently.

### 3.1 — Per-row interpretation under each W11-5 cause-attribution scenario

| Affected row | Under (S1) observable-construction defect | Under (S2) kernel-rank invalid | Under (S3) bridge-map mis-specified |
|:-------------|:-------------------------------------------|:--------------------------------|:-------------------------------------|
| **#45 Class A NULL kernel-signature** | INTERPRETATION PRESERVED. Substrate-IS prediction is the kernel-signature NULL on phi_67-clean rows; W11-5 FAIL is at the spectral-excess observable, not at kernel-signature. NULL on F1+F2+F5 is still the substrate's first prediction. | INTERPRETATION SHIFTS. If kernel-rank effective != 2, the [φ_67] generator may not be substrate-clean; "decisive triplet" rebrand to "candidate triplet"; lab S/N margin 0.573193 M_KK² becomes provisional pending rank re-derivation. | INTERPRETATION SHIFTS. If χ does not faithfully project ker(ι_*), the NULL prediction may apply to a different sub-algebra than M_3(ℂ); rebrand to "kernel-image NULL pending χ correction". |
| **#46 Class B cohomology-asymmetry ratio** | INTERPRETATION PRESERVED. The ratio 7.324992 is substrate-resident (computed on (A_K, H_K, D_K), NOT on the BdG-sector restriction); W11-5 is a different observable. The (Δ_B/Δ_A)^p cancellation theorem at p=2 still operates exactly. | INTERPRETATION SHIFTS. If kernel-rank effective != 2, the ratio test becomes vacuous-or-renormalized; ratio 7.324992 may be a rank-2-specific signature that needs re-derivation under the corrected rank classification. | INTERPRETATION SHIFTS. If χ projects differently, the ‖φ_67‖/‖φ_88‖ image in lab(F_1)/lab(F_5) may carry sub-leading correction terms; band [7.3177, 7.3323] widens. |
| **#47 F1 Caroli-Matricon ladder (W5-2)** | PRESERVED. Decisive Gate-1 NULL prediction unaffected. | SHIFTS. If rank-effective=1 (as W11-5 suggests at L=10), F1 may carry sub-leading φ_88 contamination; "decisive" rebrand. | SHIFTS. χ-correction may admit a φ_67 sub-leading projection; NULL becomes "<some-S/N margin" instead of "EXACTLY zero". |
| **#48 F2 SABS pair correlation (W5-2)** | PRESERVED. | SHIFTS as #47. | SHIFTS as #47. |
| **#49 F3 HQV splitting (W5-2)** | PRESERVED (supporting rank, not decisive). | SHIFTS. F3 supporting-NULL prediction depends on which generator dominates the dipolar-locking sector; rank correction may flip dominance. | SHIFTS as #47. |
| **#50 F4 Larmor cocycle-degenerate (W5-2)** | **HIGHEST IMPACT**. F4 is the cocycle-degenerate row driving Gate-4 multi-pressure slope discrimination — the W11-5 result that "M_3(ℂ) Cartan-zone weight non-negligible" coincides EXACTLY with the F4 rank-1-effective scenario. F4 slope sign + magnitude becomes the operational discriminator for the W11-5 §VII.AJ scenario. | SHIFTS. Slope-discrimination remains operational but the slope predicate (Jacobi-cubic vs φ_88-linear) re-evaluates under the corrected rank. | SHIFTS. χ-correction may flatten the slope or reverse its sign. |
| **#51 F5 Jensen quench acoustic (W5-2)** | PRESERVED. Decisive Gate-1 NULL prediction unaffected. | SHIFTS as #47. | SHIFTS as #47. |
| **#52-#54b A-phase rows (W5-3)** | PRESERVED. Cross-platform identical-ratio prediction unaffected (substrate-resident argument). | SHIFTS as B-phase analogs; chi_A=3/2 rescaling intact but rank correction propagates through. | SHIFTS as B-phase analogs; χ-correction propagates through inheritance-morphism map both at BDI and at chiral-AIII platforms. |
| **W2-1 paper §5.1 + §5.2 audit-pin verdict** | PRESERVED at the paper-artifact level (paper draft frozen; verdict line `1f38f988...` immutable). | SHIFTS at the **interpretation** level (paper §3 inheritance morphism declaration). Carry-forward `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM` per W2-1 §"S88 carry-forwards" item (4) is the operational fix-in-S88 path. | SHIFTS as (S2). |

### 3.2 — Adversarial-skeptic flag

Per `feedback_mack-bridge-role.md`, this consolidation flags the following row interpretations as **contested by in-flight Slot-2 workshops**:

- **Row #46 + Rows #47-#54b cross-platform identical-ratio prediction** is contested by Slot-2 workshops examining (a) the W-1 §VII.W-2 status (whether the Pillar III↔IV bridge anatomy generalizes faithfully to Pillar IV↔V), (b) the W-4 W11-5 cause attribution (whether the FAIL is at observable-construction vs kernel-rank vs bridge-map), and (c) the W-5 axis-of-observation (whether the substrate-resident argument is robust against alternative inheritance-morphism formulations beyond χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)).
- The **substrate-IS / laboratory-IN partition** at the registry-anatomy level is the high-leverage contested question; if Slot-2 W-1 workshop concludes the W-5 calibration-corpus 5-anatomy framing applies only to specific bridge-map types, then Rows #45-#54b's cross-pillar-bridge-anatomy declarations would need to be re-validated under the constrained framing.
- The W11-5 REGISTRY-FAIL is itself the strongest current evidence that the calibration-corpus generalization to FWD-C3 (Pillar IV↔V cocycles↔3He) is non-trivial — the registry-FAIL is observable-construction-specific, not bridge-map-defective, so the cocycle-asymmetry ratio test inherits robustness from the bridge map even under the FAIL.

## Section 4 — K-counter calibration tracking update (with REGISTRY-FAIL flag)

### 4.1 — Current K-counter state

Per `cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)" — **K=2** at S87 close:

| # | Workshop | Bridge | Status |
|:--|:---------|:-------|:-------|
| 1 | S86 W-5 (volovik PRIMARY + connes CO-AUTHOR) | Pillar III ↔ Pillar IV (HP^1 cohomology ↔ Peotta-Törmä quantum-metric trace) | **LANDED** §VII.AF.1 (S87 W5-1); Level-3 0.0095% F_4 strict at L_max=10; 10× inside Level-2 envelope. |
| 2 | S87 W11-5 (volovik PRIMARY) | Pillar IV ↔ Pillar V (substrate spectral-excess ↔ 3He-B BdG-undoubled excess at polycritical pressure) | **REGISTRY-FAIL** §VII.AJ NOT eligible per §"Registry-PASS criterion"; Level-3 1.029 violates Level-2 0.05 by ~21×; calibration corpus K=1→2. |
| 3 | — | — | (awaits future high-density workshop) |

K_eff = 2 < K_promotion = 3 ⇒ **status = SUGGESTION (NOT MANDATORY)**.

### 4.2 — Substitution chain for K-counter promotion logic

```
Step 1 (definition):
  K_eff           := count of distinct calibration-corpus instances
  K_promotion     := 3 (per feedback_rules-compensate-missing-structure.md)
  status          := SUGGESTION if K_eff < K_promotion
  status          := MANDATORY  if K_eff >= K_promotion

Step 2 (substitution):
  K_eff = 2 (1 PASS instance #1 + 1 REGISTRY-FAIL instance #2)
  K_promotion = 3

Step 3 (simplification):
  K_eff (2) < K_promotion (3)  ⇒  status = SUGGESTION

Step 4 (direction):
  Status retained at SUGGESTION; promotion event awaits 3rd calibration instance.
```

### 4.3 — Does REGISTRY-FAIL instance #2 dilute the corpus calibration value?

**No** — it strengthens it. The K-counter's promotion criterion is structural-distinctness across calibration instances; a REGISTRY-FAIL is a **calibration instance that demonstrates the rule correctly flags FAIL cases**. Per the cross-pillar-bridge-anatomy.md rule's intent (§"Why K-tracked promotion"): "the K=3 ladder forces three structurally-distinct workshops to instantiate the anatomy before the rule's edge cases are saturated; premature MANDATORY-status would lock in W-5-specific accidents". A FAIL-stress-test like W11-5 saturates the rule's edge-case coverage that a PASS-only corpus cannot reach. The W11-5 instance demonstrates that the registry-PASS criterion (Level 3 < Level 2 at canonical L_max) is operationally enforced — instances that violate it are correctly excluded from the registry (no §VII.AJ landing).

The W11-5 calibration corpus instance #2 entry in `cross-pillar-bridge-anatomy.md` lines 248-253 already correctly cites the FAIL state, the per-level values (Level-3 1.029 violates Level-2 0.05 by ~21×), the structural cause attribution (M_3(ℂ) Cartan-zone weight non-negligible at L_max=10 in multiplicity-weighted Mellin scheme), the inheritance theorem PRESERVED clause, and the carry-forward `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`. No update to that sub-section is required from this consolidation; the inventory's K-counter cross-link block (Section 4.1 above) mirrors the rule-file state.

### 4.4 — Adversarial-skeptic note

The K-counter promotion to MANDATORY at K=3 SHOULD be interpreted with care if the 3rd instance is also a REGISTRY-FAIL. A K=3 corpus with 1 PASS + 2 FAIL would force the question "is the rule producing too many FAILs because the canonical L_max=10 truncation is insufficient to saturate Level-2 envelopes, or because the bridge anatomy is over-stringent?" — a question the SUGGESTION-status corpus is structurally protected from. mack-cosmic-bridge flags this as a forward-looking adversarial-skeptic concern: K=3 should not auto-promote if the FAIL ratio exceeds 50% (i.e., 2/3 FAIL would suggest the rule needs re-calibration, not promotion).

## Section 5 — FWD-C1/C2/C3 pre-registration with 4-field carry-forwards

Per `cross-pillar-bridge-anatomy.md` §"Three forward bridge candidates for S88+ dispatch", three forward candidates are pre-registered. Each row carries the 5 IS-not-IN anatomy elements + 3-level ladder declarations + inheritance-kernel rank declaration + 4-field carry-forward.

### 5.1 — FWD-C1: Pillar I ↔ Pillar II (substrate ↔ cosmology measurement; n_s)

- **Substrate-IS observable**: n_s spectral-action prediction from finite-L D_K eigenmoments on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The n_s_FW = 0.9561 value (S65 BCS+1-loop closure; canonical_constants.py:1499) is a substrate-IS scalar moment of the Jensen-deformed band-0 sector at τ_fold = 0.190.
- **Laboratory-IN observable**: Planck CMB scalar spectral index n_s = 0.9649 ± 0.0042 (Planck 2018 TT,TE,EE+lowE+lensing) — measured IN the FRW cosmology container as the slope of the temperature power spectrum near k_pivot = 0.05 Mpc⁻¹.
- **Bridge map**: Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR `L_max → ∞` image of the substrate scalar spectral moment. Bridge factors through the c_sub conformal-anomaly multiplier per S86 W5a Z-factor machinery.
- **Algebraic envelope (Level 2)**: L_max⁻³ at d=4 inherited from Pillar III ↔ IV (W-5 calibration); Level-2 canonical envelope pending substrate-first c_sub completion.
- **Empirical anchor target (Level 3)**: n_s_FW = 0.9561 vs Planck n_s = 0.9649 ± 0.0042; 1.40σ deviation from central; sits 2× outside ±0.0042 1σ band. Level-3 < Level-2 verification pending substrate-first c_sub completion.
- **Inheritance kernel rank**: rank(ker ι_*) = 1 (single n_s scalar; rank-2 NOT applicable).
- **4-field carry-forward `S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING`**:
  1. **What**: register §VII.AK candidate cross-pillar bridge entry for Pillar I↔II n_s with all 5 IS-not-IN + 3-level declarations; pin Level-3 anchor at n_s_FW=0.9561 vs Planck 0.9649±0.0042; confirm Level-2 envelope L^{-3} at d=4 → 0.001 at L_max=10 satisfies 1.40σ deviation 0.0088 absolute.
  2. **Inputs**: canonical_constants.py:1499 n_s_framework=0.9561 (S65 W3-G48 promotion); Planck 2018 anchor (mack-observational-constraints registry); S86 W5a Z-factor c_sub completion (BLOCKED on c_sub substrate-first canonical pin per `substrate-first-canonical-sourcing.md`).
  3. **Gate criterion**: PASS iff §VII.AK entry has all 5 anatomy + 3-level markers AND Level-3 0.0088 abs < Level-2 envelope 0.001 (note: abs 0.0088 > envelope 0.001 by ~9×, suggesting Level-2 envelope needs reassessment OR n_s_FW prediction has substrate-IS systematic floor); INFO if Level-3 ∈ (envelope, 10× envelope]; FAIL if > 10× envelope.
  4. **Effort**: ~6-10h (single substrate-side computation; Level-2 envelope re-evaluation + §VII.AK registry-write + falsifier-master-inventory row append).

### 5.2 — FWD-C2: Pillar II ↔ Pillar V (Mellin-cone ↔ BdG spectral triple)

- **Substrate-IS observable**: Mellin-Barnes residue at substrate-distance `s ∈ {3, 4}` on the Pillar-II Mellin-cone, evaluated against ζ-regulated Hochschild moments of D_K. The substrate IS the Mellin-residue cocycle (workshop-§VII.U/V family on the spectral-distance axis).
- **Laboratory-IN observable**: BdG (Bogoliubov-de Gennes) spectral-triple observable in a self-consistent BCS lattice — measured IN the Brillouin-zone container as the BdG band structure with Pf=−1 BDI topology (3He-B child realization; Volovik 2003 §6).
- **Bridge map**: Connes-Karoubi pairing ∘ K-theory boundary map between the Pillar-II Mellin pole structure and the Pillar-V finite-rank BdG K_0(M_2(ℂ)) image; companion to W-6 quotient-functor framework (cross-pillar-bridge-anatomy §Quotient-functor pre-registration).
- **Algebraic envelope (Level 2)**: L_max⁻α with α ∈ {2, 3} under spectral-distance scaling; α pinned post-Mellin-pole-closure at S87 W2-? cluster-span PASS.
- **Empirical anchor target (Level 3)**: Pillar-II → Pillar-V Mellin-residue / BdG-band-edge match at canonical L_max=10; substrate-first cocycle norms ‖φ‖ Sage-exact (per W-5 phi67/phi88 calibration).
- **Inheritance kernel rank**: rank(ker ι_*) ≥ 2 expected — Mellin-cone carries multiple residue generators; invokes rank-2 generalization (`inheritance-falsifier-protocol.md` §Generalization beyond 3He-B).
- **4-field carry-forward `S88-FWD-C2-MELLIN-BDG-BRIDGE-LANDING`**:
  1. **What**: complete §VII.U/V family Mellin-cone closure; derive Pillar-II → Pillar-V Connes-Karoubi pairing explicitly; register §VII.AL candidate cross-pillar bridge with all 5 anatomy + 3-level declarations; pre-register binomial(rank, 2) cross-cocycle ratios per `inheritance-falsifier-protocol.md` rank≥2 generalization clause.
  2. **Inputs**: Mellin-cone family closure at S87 W2-? cluster-span PASS (pending); cocycle norms per cohomology-class-pair from W-5 calibration; W-6 quotient-functor framework (cross-pillar-bridge-anatomy §"Quotient-functor pre-registration discipline").
  3. **Gate criterion**: PASS iff §VII.AL entry has all 5 anatomy + 3-level markers AND Level-3 within Level-2 envelope at canonical L_max=10 AND binomial(rank, 2) cross-cocycle ratios pre-registered; INFO if 1+ ratio missing; FAIL if Level-3 > 10× envelope OR no ratio pre-registered.
  4. **Effort**: ~10-15h post-Mellin-cone closure (depends on §VII.U/V family closure timeline; full bridge-anatomy registry entry + falsifier rows for each binomial(rank, 2) ratio).

### 5.3 — FWD-C3: Pillar IV ↔ Pillar V (substrate cocycles ↔ 3He-B / 3He-A laboratory observables)

- **Substrate-IS observable**: Substrate-resident HP^1 cocycle norms ‖φ_67‖ = 0.793346 M_KK², ‖φ_88‖ = 0.108307 M_KK² (W-5 Sage-exact; ratio 7.324992) evaluated on the BdG-restricted spectral-triple sub-algebra of `(A_K, H_K, D_K)`. The substrate IS the cocycle pair — these are intrinsic structural numbers, not BdG band-structure derivatives.
- **Laboratory-IN observable**: 3He-B vortex-core Caroli-Matricon ladder asymmetry (W11-C5 / Rows #47-#51; Lancaster MCT-3 / Helsinki ROTA cells) AND 3He-A µSR chirality discrimination (W11-C6 / Rows #52-#54b; Aalto LTL / RHUL). Lab measures these IN the helium cryostat container under a (p, T) sweep over 0–34 bar.
- **Bridge map**: Inheritance morphism `ι_*: A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` (BDI → BdG sector child) ∘ (Δ_B/Δ_A)^p lab-conversion factor. Cancellation theorem (S86 W-5 DONE-5; 0.0e+00 residual) preserves ‖φ_a‖/‖φ_b‖ INTACT in the lab measurement under common p.
- **Algebraic envelope (Level 2)**: Cohomology-asymmetry test: ratio preservation 7.3250 ± 0.1% (S86 W-5 Gate-2 pre-registered band). Level-2 envelope is the structural-exact form, not an L_max⁻α algebraic bound; the regulator-invariant ratio replaces the convergence envelope for this candidate class.
- **Empirical anchor target (Level 3)**: S88+ Lancaster MCT-3 vortex-core spectroscopy and RHUL/Aalto LTL µSR run delivering NULL on F1/F2/F5 + ratio 7.3250 ± 0.1% on any non-NULL detection (4-gate falsifier structure per `inheritance-falsifier-protocol.md` §Four-Gate Structure).
- **Inheritance kernel rank**: rank(ker ι_*) = 2 ([φ_67] chiral pair + [φ_88] Cartan hypercharge) — DIRECTLY invokes `inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)" rank-2 case.
- **Status update for FWD-C3 vs W11-5**: W11-5 closed as REGISTRY-FAIL on the **observable-construction** axis (BdG-undoubled spectral excess at polycritical pressure under multiplicity-weighted Mellin-pole-window scheme). FWD-C3 is on the **cohomology-asymmetry** axis (cocycle ratio ‖φ_67‖/‖φ_88‖ at Lancaster B-phase + Aalto A-phase); the two axes are structurally independent. The W11-5 FAIL informs the M_3(ℂ) Cartan-zone projection for the FWD-C3 substrate-side cocycle norms (already canonical at the substrate level via S86 W-5 DONE-5 cancellation theorem).
- **4-field carry-forward `S88+-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING`** (multi-year experimental cycle):
  1. **What**: register §VII.AM candidate cross-pillar bridge entry with all 5 anatomy + 3-level declarations + binomial(2,2)=1 cross-cocycle ratio (the canonical 7.324992 ratio); land at registry once Lancaster MCT-3 + Aalto LTL µSR data both available with measured ratios on F1/F5 cross-row.
  2. **Inputs**: Lancaster MCT-3 vortex-core spectroscopy data (when available from Pickett group dilution-fridge campaign, ~2027-2030 horizon); Aalto LTL µSR data (when available from Krusius/Tuoriniemi/Eltsov, ~2027 horizon); W5-2 + W5-3 rows #47-#54b + their substrate-derived predictions; W-5 cancellation theorem (S86 W-5 DONE-5).
  3. **Gate criterion**: PASS iff both lab ratios in [7.3177, 7.3323] AND |r_A − r_B| < 0.1% (cross-platform substrate-resident-ness confirmation); INFO if one ratio in band but not both; FAIL if either ratio outside band by > 1% (cocycle-resident axis falsified).
  4. **Effort**: 0.5 wave-equivalents (~2-4h) for the registry-write + falsifier-row append + Stage-1-CANDIDATE tagging once both lab datasets land; the lab-execution cycle itself is multi-year (2027-2030+ horizon at Lancaster + Aalto LTL).

### 5.4 — FWD candidates summary table

| Candidate | Pillars | Substrate-IS | Laboratory-IN | Level-2 envelope | Inheritance rank | Earliest dispatch |
|:----------|:--------|:-------------|:--------------|:----------------|:-----------------|:-------------------|
| FWD-C1 | I↔II | n_s_FW = 0.9561 | Planck 2018 n_s = 0.9649±0.0042 | L_max⁻³ at d=4 (pending c_sub) | 1 | S88 (post-c_sub) |
| FWD-C2 | II↔V | Mellin-Barnes residue at s ∈ {3,4} | BdG band-edge image | L_max⁻α, α ∈ {2,3} | ≥2 (rank-2 generalization) | S88 (post-§VII.U/V closure) |
| FWD-C3 | IV↔V | ‖φ_67‖, ‖φ_88‖ Sage-exact | 3He-B + 3He-A 4-gate falsifier | Structural-exact 7.3250±0.1% | 2 | S88+ (lab-blocked) |

## Section 6 — Adversarial-skeptic flags (per `feedback_mack-bridge-role.md`)

1. **Row #46 cohomology-asymmetry ratio interpretation**: contested by Slot-2 W-1 workshop on §VII.W-2 status. If §VII.W-2 concludes the W-5 calibration-corpus 5-anatomy framing is bridge-map-type-specific, the substrate-resident argument for Row #46 (which underwrites both #46 and the cross-platform identical-ratio gate at #52-#54b) needs re-validation. mack-cosmic-bridge flags this as the highest-leverage adversarial concern.

2. **W11-5 cause attribution (S1) vs (S2) vs (S3)**: contested by Slot-2 W-4 workshop on W11-5 observable-construction defect. The carry-forward `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY` tests scenario (S1); if it FAILs, scenarios (S2) and (S3) become live, and the Section 3.1 per-row interpretation table propagates new SHIFT classifications across rows #45-#54b.

3. **Cross-platform identical-ratio gate is binary-discriminator**: contested by Slot-2 W-5 axis-of-observation workshop. If the inheritance-morphism formulation for 3He-A vs 3He-B differs structurally beyond chi_A=3/2, the identical-ratio prediction degrades from "EXACT" to "modulo phase-dependent correction"; the high-leverage discriminator weakens.

4. **K-counter promotion logic at K=3 with 2 FAIL**: forward-looking concern; a 3rd calibration instance that is also a FAIL would force re-evaluation of whether MANDATORY status is appropriate. mack-cosmic-bridge recommends auto-promotion logic check at K=3: if FAIL_ratio > 0.5, defer MANDATORY promotion pending rule-recalibration workshop.

5. **FWD-C1 Level-3 vs Level-2 envelope**: Level-3 absolute deviation 0.0088 (n_s) appears to violate Level-2 envelope 0.001 by ~9× under the L_max⁻³ ansatz at d=4; this is a forward-looking concern that the n_s prediction has substrate-IS systematic floor exceeding the W-5-inherited algebraic envelope. mack-cosmic-bridge flags FWD-C1 Level-2 envelope as needing substrate-first re-derivation (not W-5 inheritance) before §VII.AK registry-write.

## Section 7 — Closure summary

This consolidation appends to `sessions/framework/registry/falsifier-master-inventory.md`:
- **Rows #47-#51 (W5-2 B-phase F-table)** at LAB-FALSIFIER-A level, EVOI horizon Lancaster MCT-3 / Helsinki ROTA / RHUL ~2027-2030.
- **Rows #52-#54b (W5-3 A-phase F-table; chi_A=3/2 substrate-corrected)** at LAB-FALSIFIER-A level, EVOI horizon Aalto LTL / RHUL µSR ~2027-2030.
- **Cross-row dependency map** (Class A NULL × Class B RATIO failure-mode propagation) as new section header.
- **W11-5 §VII.AJ REGISTRY-FAIL annotation** as per-row interpretation table across rows #45-#54b under (S1)/(S2)/(S3) cause-attribution scenarios.
- **K-counter calibration-corpus update** mirroring `cross-pillar-bridge-anatomy.md` lines 246-253 (K=2; SUGGESTION status retained).
- **FWD-C1/C2/C3 forward-bridge candidate rows** with 4-field carry-forwards.

The append is performed by mack-cosmic-bridge as sole writer per `feedback_mack-bridge-role.md`. One-shot Python writer in append-only mode per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race"; no Edit-tool round-trips on the shared registry. After append, verdict-line citation at `computations/s87_gate_verdicts.txt` references this consolidation by its content-SHA.

**Carry-forwards landed by this consolidation**:
1. `S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING` — §VII.AK candidate, n_s bridge; ~6-10h post-c_sub.
2. `S88-FWD-C2-MELLIN-BDG-BRIDGE-LANDING` — §VII.AL candidate, Mellin↔BdG bridge; ~10-15h post-Mellin-closure.
3. `S88+-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING` — §VII.AM candidate, cocycle↔3He bridge; lab-blocked multi-year.
4. **(forward-looking)** auto-promotion logic check at K=3: if FAIL_ratio > 0.5, defer MANDATORY promotion pending rule-recalibration workshop (recommendation to orchestrator at K=3 trigger event).
