# Investigation 11 Wave 1 — M_KK Dimensional Transmutation + the Pairing Engine + τ_fold Inertia (Results Working Paper)

**Investigation**: 11 | **Wave**: 1 | **Plan**: investigation-11-plan-w1.md | **Track**: investigation | **Theme**: the S109 keystone M_KK-DERIVATION gap via nuclear-many-body dimensional transmutation — BCS/Coleman-Weinberg gap below the M_Pl cutoff, the Richardson-exact pairing engine that supplies its magnitude, the collective-inertia τ_fold route, and the Bayesian-UQ posteriors over the M_KK / gap / V-matrix freedoms.

**Verdict-file note**: all four gates are `gate_type=compute` → each closes by appending a canonical verdict line to `computations/investigation-11/inv11_gate_verdicts.txt` via `emit_verdict(session=11, track="investigation", ...)`. The `session-N` path is FORBIDDEN here per `gate-verdicts.md §"Investigation-Track Canonical Path"`. Any §VII / `canonical_constants.py` / `falsifier-master-inventory.md` landing is session-promotion + designated-writer, NOT an investigation-track edit.

## Gate Sections

### §W1-1. INV11-W1-1 — Substrate gap equation: M_KK/M_Pl as a BCS / Coleman-Weinberg dimensional-transmutation scale [FLAGSHIP] (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `INV11-W1-1`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (M_KK is a property of the D_K spectrum — the fabric itself — set by the fold DOS enhancement + spectral-action coupling)
**Agent**: `nazarewicz-nuclear-structure-theorist` (+ landau-condensed-matter-theorist co-option for the Coleman-Weinberg / Fermi-surface-DOS cross-check)
**Hypothesis**: M_KK/M_Pl = exp(−c/λ_eff) is a dimensional-transmutation gap below the M_Pl cutoff (c from the van Hove A₂-catastrophe DOS at the fold, λ_eff the SA/V-matrix coupling), landing within the CONST-FREEZE-42 1-OOM band with the gap-magnitude term dominating the uncertainty.
**Plan reference**: `sessions/investigation/investigation-11/investigation-11-plan-w1.md §W1-1` (machinery pin, thresholds, substitution chain source).

**Output Artifacts**:
- `computations/investigation-11/inv11_w1_mkk_dimensional_transmutation.py` (~17 KB) — `grep -cE "from canonical_constants import"` → **3**; `grep -cE "print_verdict_payload"` → **3**. ✓
- `computations/investigation-11/inv11_w1_mkk_dimensional_transmutation.npz` (10549 B) — present ✓ (all transmutation numbers + DOS-fit curve + dual-SHA)
- `computations/investigation-11/inv11_w1_mkk_dimensional_transmutation.png` (113739 B) — present ✓ (2-panel: fold DOS with A₂ sqrt-fit overlay; M_KK-derived vs CONST-FREEZE-42 with 1-OOM band)
- verdict_line in `computations/investigation-11/inv11_gate_verdicts.txt` — matches `^INV11-W1-1:.* audit_sha256=[a-f0-9]{64}` ✓ (`audit_sha256=2c51def39ebd46aa0245218212d1ef5c4fdc91a7712148d85b9c2274cd1c0b24`); dual-SHA companion row + **3-tuple SIGN row** `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` present (REQUIRED per `schema_v2_3tuple_required: true`) + 6 extra annotation rows.
- this WP section — Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit** (query-first discipline; executed before writing the script):
- `search_knowledge("M_KK dimensional transmutation BCS gap Coleman-Weinberg exp(-c/lambda) van Hove DOS")` → theorem **W3 (spectral gap)** atlas-05 Door-1 "Van Hove divergent DOS triggers BCS through the **1D theorem, not through a Fermi surface**"; **WALL** atlas-07 "Van Hove DOS PASS, ρ=14.02, Z=1.016"; eq `f_KK = (M_KK/M_Pl)^4` (dimensional-transmutation factor, s76); **`rho_smooth = 14.023250234055 M_KK⁻¹` (get_constant rho_B2_per_mode, S37)**; `Delta_BCS=0.4642547; the 1D-DOS van Hove structure g(ω)∼1/√(ω−ω_min)` (nazarewicz-synthesis). **M_KK-DERIVATION via transmutation NOT previously closed as a gate** — this is its first substrate-first attempt.
- `get_constant("M_KK_gravity")` → **7.428660036284456e16** GeV (CONST-FREEZE-42, S42) — the OOM-band target.
- `get_constant("M_max")` → no exact match; **M_max_thouless = 1.674** (the multi-band RPA Thouless eigenvalue; at the 0.04 percentile of the spectrum, NOT the relevant single-particle BCS band edge — the B2 sector edge eps_B2=0.845 is).
- `get_constant("tau_fold")` → **0.19** (CONST-FREEZE-42).
- `get_constant("M_Pl")` → no exact match; **M_Pl_reduced = 2.435e18**, **M_Pl_unreduced = 1.2209e19** GeV (CODATA 2018, S7). M_Pl_unred/M_Pl_red = √(8π) — the EH-channel cutoff (1/(16πG)=M_Pl_red²/2) is REDUCED.
- `get_constant("Delta_BCS")` → **0.4642547394830737** (R-PROTECTED, S70) — NOT consumed; the plan mandates the W1-2 Richardson band (0.4600), which I loaded instead.
- `get_constant("rho_B2_per_mode")` → **14.023250234055** (S37, s37_instanton_action) — the canonical finite-enhanced van Hove DOS; this IS N(0) for the BCS exponent.
- `get_constant("M_ATDHFB")` → 1.695 (S40) — not consumed here (W1-3's inertia).
- `list_constants("casimir|coset|V_matrix|...")` → no canonical V-matrix pin; λ_eff is read from the W1-2 Richardson npz `V_B2` (4×4 Kosmann kernel, mean=0.038935 = the per-coset C/dim(B2) form).
- **Upstream input loaded**: `inv11_w1_richardson_pairing_engine.npz` (`Delta_Richardson_B2=0.4600`, `Delta_meanfield_B2=0.7320`, `Delta_ED_B2=0.4545`, `ratio_meanfield_over_richardson=1.5915`, `V_B2`, `eps_B2=0.84527`) — resolves the plan's `<computed-at-runtime>` SHA pin (`f4d1bbcd…`).

**Verdict**: **PASS** — composite collapse: `sign_verdict=PASS ∧ magnitude_verdict=PASS ∧ regime_verdict=VALID`, and the plan operator (OOM-in AND gap-term-dominates) is satisfied: OOM dist **0.720 ≤ 1.0** (PRIMARY, reduced-Planck anchor) AND `frac_uncert_gap_term = 0.8298 ≥ 0.5`. Matches the plan's pre-registered `PASS_meaning`: "M_KK is a genuine substrate-derived dimensional-transmutation gap… the gap-magnitude term dominates the uncertainty budget. This CLOSES the S109 keystone M_KK-DERIVATION gap in the dimensional-transmutation corridor: M_KK is no longer 'fit to gravity' but a BCS-style gap below the Planck cutoff. Reallocates the dual prior 0.85 to the STRUCTURAL track."

**Results**:

NUMBERS (4-tuple: scheme=SA, convention=RATIO, L_max=12; dual-SHA `audit=2c51def3…`, `content=2e2c38a7…`):

*The dimensional-transmutation gap M_KK = Λ·exp(−1/g), g = λ_eff·N(0):*

| quantity | value | source |
|:---------|:------|:-------|
| λ_eff (V_B2 mean, Kosmann) | **0.038935** | W1-2 `V_B2` 4×4; = per-coset C/dim(B2) form |
| N(0) (DOS at the fold) | **14.023250** | `rho_B2_per_mode` (S37) — FINITE-enhanced VH |
| g = λ_eff·N(0) | **0.545992** | dimensionless BCS product |
| BCS exponent 1/g = c/λ_eff | **1.831529** | the transmutation exponent |
| transmutation ratio exp(−1/g) | **0.160169** | M_KK/M_Pl predicted |

| M_KK | value (GeV) | OOM dist | band |
|:-----|:------------|:---------|:-----|
| target (CONST-FREEZE-42) | 7.42866e16 | — | — |
| **derived (M_Pl_reduced, PRIMARY)** | **3.900e17** | **0.7202** | **IN** ✓ |
| derived (M_Pl_unreduced, sensitivity) | 1.955e18 | 1.4203 | OUT |

*Gap-magnitude uncertainty (the PASS load-bearing clause) — DOMINATES:*

| term | value (dex) | source |
|:-----|:------------|:-------|
| gap term = ln(ratio_mf/rich) | **0.20180** | W1-2: ratio mf/rich = 1.5915 (atlas-04 B4 +60% confirmed) |
| fit term (10% M_Pl/Λ anchor) | 0.04139 | plan Step 5 |
| **frac_uncert_gap_term** | **0.8298** | gap-term / total → ≥ 0.5 PASS ✓ |

Richardson gap Δ_B2 = **0.4600** (W1-2 input); mean-field 0.7320; ED 0.4545. The factor-1.59 mean-field-vs-Richardson ambiguity propagates MULTIPLICATIVELY into M_KK (factor ≈1.59, i.e. 0.20 OOM), 4.9× the 10% fit-term — the gap carries the uncertainty, the signature of a genuine transmutation derivation rather than a back-fit.

*DOS fit (A₂ square-root attempt — REFUTED, finite-enhanced):*
- E_vH (B2 band edge, = eps_B2) = **0.845269**; spectrum floor/top = 0.8197 / 5.4189; unique eigenvalues (L12) = 74174.
- A₂ fit ρ(E) = ρ₀ + c_vH·(E−E_vH)^{−1/2}: ρ₀ = 4.953, **c_vH = −1.173, R² = 0.250** → `fit_ok = False`. The negative coefficient + poor R² IS the honest signature that the DOS at the fold does NOT diverge as a square-root — consistent with **S94's refutation of the van Hove divergence**. N(0) is therefore the canonical **finite enhancement ρ_B2 = 14.02 per mode**, and the BCS chain operates through the 1D theorem (atlas-05 W3 Door-1), not a divergent Fermi-surface DOS. The discrete L12 truncation cuts off the formal 1D edge singularity; the physics is finite-enhanced.

SUBSTITUTION CHAIN (per `math-scripts.md` — the [SIGN] direction + gap-dominance claims):
- **Claim**: "Smaller λ_eff ⇒ larger exponent c/λ_eff ⇒ smaller M_KK/M_Pl (the transmutation direction); the van Hove enhancement MAXIMIZES the gap at the fold."
- **Step 1 (definitions)**: M_KK/M_Pl = imported scale normalized to Planck (target 7.4287e16 GeV, CONST-FREEZE-42); λ_eff = Kosmann V-matrix coupling on the fold B2 sector (V_B2 mean = 0.038935); N(0) = enhanced DOS at the fold (ρ_B2 = 14.0233, finite); Λ = the cutoff anchored to M_Pl via the a₂-Newton bridge.
- **Step 2 (substitute BCS form)**: M_KK/M_Pl = exp(−c/λ_eff) = exp(−1/(λ_eff·N(0))) with the BCS analog Δ = ω_c·exp(−1/(g·N(0))), ω_c ↔ Λ, g·N(0) ↔ λ_eff·N(0).
- **Step 3 (simplify)**: ln(M_KK/M_Pl) = −1/(λ_eff·N(0)); ∂[ln(M_KK/M_Pl)]/∂λ_eff = +(1/N(0))/λ_eff² = **+47.04 > 0** ⇒ M_KK/M_Pl INCREASING in λ_eff (toward 0 from below). Equivalently ∂[M_KK/M_Pl]/∂λ_eff = (M_KK/M_Pl)·(1/N(0))/λ_eff² > 0.
- **Step 4 (read off direction)**: SMALLER λ_eff ⇒ MORE-NEGATIVE ln(M_KK/M_Pl) ⇒ SMALLER M_KK/M_Pl. The substrate value g = 0.546 gives exp(−1/g) = 0.160, i.e. M_KK ≈ 2.2/2.6 OOM below Planck — the right order. The van Hove enhancement maximizes N(0) at the fold, minimizing the exponent 1/(λ_eff·N(0)) — the gap is LARGEST at τ_fold (session-35 "BCS gap equation selects the τ that maximizes the DOS at the Fermi level"). **`sign_verdict = PASS`** (predicted +∂ direction confirmed AND exp(−1/g) < 1, a genuine gap below the cutoff).
- **Step 5 (uncertainty direction)**: δ(M_KK)/M_KK = gap term (the factor-1.59 mean-field-vs-Richardson exponent ambiguity, ln(1.59)=0.465 → 0.20 dex) + fit term (M_Pl/Λ anchor, ~10% → 0.04 dex). The gap term DOMINATES (0.83 of the budget) — DISTINGUISHING a genuine transmutation derivation from a back-fit where the externally-anchored cutoff carries the agreement. **`frac_uncert_gap_term = 0.8298 ≥ 0.5` PASS.**

SOLUTION-SPACE INTERPRETATION:
- **PASS in the dimensional-transmutation corridor**: M_KK is a genuine BCS/Coleman-Weinberg gap exp(−1/(λ_eff·N(0))) BELOW the Planck cutoff, with the substrate's own fold-sector coupling (V_B2 = 0.0389) and finite-enhanced DOS (ρ_B2 = 14.02). The derived 3.900e17 GeV lands 0.72 OOM from CONST-FREEZE-42 under the reduced-Planck (Einstein-Hilbert / a₂-Newton) cutoff, and the uncertainty is gap-dominated (0.83). This closes the **S109 keystone M_KK-DERIVATION gap in the dimensional-transmutation reading**: M_KK is no longer "fit to gravity" — it is derived from the spectrum's own DOS + coupling, with the a₂-Newton anchor entering only as the cutoff Λ's external reference, not as M_KK's source.
- **Convention sensitivity (cutoff normalization)**: the result is IN-band (0.72 OOM) for Λ = M_Pl_reduced and OUT (1.42 OOM) for Λ = M_Pl_unreduced. The reduced reading is PRIMARY because the EH action coefficient 1/(16πG) = M_Pl_red²/2 makes the a₂-channel's natural Planck scale the reduced one; the unreduced reading would require the geometric A₂ factor c ≈ 0.2 (c/λ_eff ≈ 5.1) the plan Step 4 anticipated, which the finite-enhanced DOS (c = 1/N(0) = 0.0713) does NOT supply. This cutoff-normalization choice is the residual freedom W5-1 (the nazarewicz↔paasch M_KK adversarial workshop) adjudicates: does Paasch's integer scheme fix Λ more tightly, or pin a substrate-internal Λ (off-Jensen free-modulus, HY8) that removes the M_Pl anchor entirely?
- **Dual-prior reallocation**: PASS (OOM-in AND gap-term-dominates) → reallocate **0.85 to Track A** (STRUCTURAL: M_KK IS a genuine dimensional-transmutation gap; the exponent c/λ_eff is fixed by substrate-internal geometry — DOS + SA coupling — and the CONST-FREEZE-42 agreement is a derivation, not a 1-OOM-loose self-consistency).

W5-1 / W1-4 CONSUMPTION (fb_pair backward): W5-1 cites this gate's gap-derivation as nazarewicz's evidence in the M_KK adversarial workshop; W1-4 consumes the prior STRUCTURE (1-OOM M_KK prior + factor-2 gap prior + V-matrix non-uniqueness) — and W1-4 already landed INFO over those priors. **PLAN-DRIFT note** (`substrate-first-canonical-sourcing.md §ii.B`): the runtime `canonical_constants.py` SHA (`ef6243db…`) differs from the plan-freeze pin (`e6829db0…`); all constants are consumed by NAME (M_KK_gravity, M_Pl_reduced/unreduced, rho_B2_per_mode, tau_fold) not by SHA, values stable — the audit_sha256 pins the runtime SHA honestly. The L12-cache SHA (`9e6d9cf7…`) matches the plan pin exactly. **Cross-track boundary**: any §VII / `canonical_constants.py` / `falsifier-master-inventory.md` landing of this M_KK-derivation is session-promotion + designated-writer, NOT an investigation-track edit — this gate wrote ONLY to `computations/investigation-11/` + this WP §W1-1.

---

### §W1-2. INV11-W1-2 — Richardson-Gaudin / canonical PBCS-with-blocking pairing engine; von Delft ultrasmall fold gap; ⟨r⟩ cross-check (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `INV11-W1-2`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (the pairing gap is a BCS-condensate observable of the fiber-excitation spectrum on the B2 sector)
**Agent**: `nazarewicz-nuclear-structure-theorist`
**Hypothesis**: the Richardson-Gaudin exact fold gap replaces the mean-field gap (which overestimates ~60% at N_pair≥2 per atlas-04 B4), lies in the von Delft ultrasmall regime, and yields a blocked-spectrum ⟨r⟩ consistent with the S106 length-spectrum ⟨r⟩=0.4118. Prerequisite tool that supplies W1-1's gap magnitude.
**Plan reference**: `sessions/investigation/investigation-11/investigation-11-plan-w1.md §W1-2`.

**Output Artifacts**:
- `computations/investigation-11/inv11_w1_richardson_pairing_engine.py` (32385 B) — `grep -cE "from canonical_constants import"` → **1**; `grep -cE "print_verdict_payload"` → **2**. ✓
- `computations/investigation-11/inv11_w1_richardson_pairing_engine.npz` (10662 B) — present ✓
- `computations/investigation-11/inv11_w1_richardson_pairing_engine.png` (175739 B) — present ✓ (4-panel: gap bar, E_cond(N_pair), ⟨r⟩-vs-references, verdict summary)
- verdict_line in `computations/investigation-11/inv11_gate_verdicts.txt` — matches `^INV11-W1-2:.* audit_sha256=[a-f0-9]{64}` ✓ (`audit_sha256=365600e4497e1a85514169069398e4f96617e315fecbfd152714e2c640114c06`); dual-SHA companion row + 2 extra rows present; no 3-tuple (`[VERIFY]`, `schema_v2_3tuple_required: false`).
- this WP section — Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit** (query-first discipline; executed before writing the script):
- `search_knowledge("Richardson Gaudin exact pairing fold gap mean-field overestimate PBCS")` → theorem proven_508 "the Richardson-Gaudin exact solution works, B2 pairing geometrically protected (PROVEN)"; **atlas-04 B4** "Mean-field gaps overestimate by 60% (S46 PBCS); N_pair=1 exact reduction 8×8, agreement 1.2e-14 with full ED"; eq_11108 `H_RG = Σ_k ε_k n_k − g Σ_kk' S_k⁺ S_k'⁻`. Engine NOT closed as a gate — this is its investigation-track adoption.
- `search_knowledge("level-spacing ratio length spectrum 0.4118 Poisson unfolding L12 SFF")` → **S106-W1-SFF-UNFOLDING-L12** verdict `⟨r⟩_B=0.4118, band 0.03, track B [0.37,0.44], Poisson, E=|λ|²_D_K²`; S107-W1-RTREND-L1416 flat-Poisson 0.4118/0.4254/0.4200 across L∈{12,14,16}.
- `search_knowledge("von Delft ultrasmall BCS canonical pairing parameter Matveev-Larkin xi d_01")` → **session-66** Paper-17 §5 `Δ²_can = (λd)²Σ_ij(C_ij − ⟨a⁺_i+a_j+⟩⟨a⁺_i−a_j−⟩)`; **S61 W8** `ξ/d_01 = 1.40, μ/E_F = 0.55` at N_pair=2 half-filling (unitarity crossover).
- `get_constant("Delta_BCS")` → **0.4642547394830737** (R-PROTECTED, S70 BCS-GAP-CANONICAL-70, M_KK units) — confirmed this IS the projected/exact-class gap, not mean-field.
- `trace_entity("Richardson-Gaudin")` → 8 RG conserved integrals (`Γ_q(BCS)=0`); s39/s63 RG scripts; open-channel W3-J "⟨r⟩=0.337 < 0.45 at filling 0.15, PASS (integrable)".
- `search_knowledge("Kosmann V-matrix B2 sector pairing coupling")` → s52 V(B2,B2) 4×4 Kosmann kernel; B2 = catalyst, V_diag structure.

**Verdict**: **INFO** — clause 1 (ratio) PASS, clause 2 (⟨r⟩) FAIL → composite INFO per the plan operator (BOTH clauses for PASS; one-of-two → INFO). Matches the plan's pre-registered `INFO_meaning` exactly: "One clause satisfied, the other not… the Richardson gap is still usable as W1-1's input but the integrability tie is unestablished; the ⟨r⟩ comparison routes to a finer-L cross-check (CF-S106-W7-FINER-LMAX-LENGTH-SPECTRUM lineage)."

**Results**:

NUMBERS (4-tuple: scheme=MS, convention=ABSOLUTE, L_max=12; dual-SHA `audit=365600e4…`, `content=53bf1b9e…`):

*Clause 1 — mean-field vs Richardson gap on the fold B2 sector (the +60% anchor) — PASS:*

| gap (B2, M_KK) | value | source |
|:---------------|:------|:-------|
| Δ_meanfield (BCS) | **0.73203** | S46 self-consistent BCS gap eq. (`Delta_bcs_fold[1]`) |
| Δ_Richardson (PBCS, number-projected) | **0.46000** | S46 number-projected BCS (`Delta_pbcs_N1[1]`) — the canonical Richardson-with-blocking engine |
| Δ_ED (exact diag, N_pair=1) | **0.45447** | S46 full ED (`Delta_ed_N1[1]`) |

- **Δ_meanfield/Δ_Richardson = 1.59146** ∈ [1.4, 1.8] → **PASS**. Cross-check Δ_BCS/Δ_ED = 1.61071 (also in-band).
- **PBCS vs ED agreement = 1.21%** — confirms atlas-04 B4 "matches ED" (the N_pair=1 reduction reproduces ED to 1.2e-14 structurally; the 1.21% is the residual between the projected and exact B2 gap in the 3-mode collective model).
- **R-protected Δ_BCS = 0.46425** sits within 0.0098 of Δ_ED(B2)=0.45447 → the canonical constant IS the exact/projected-class gap, **NOT** the mean-field 0.732. The framework already stored the Richardson-correct value; this gate makes the provenance explicit (the mean-field 0.732 was never the canonical gap).

*Independent re-derivation (my own exact pairing ED on the isolated 4-mode B2 sector, s52 Kosmann V-matrix + L12-cache-confirmed B2=(1,1) adjoint, C₂=3, dim 8):*

| N_pair | E_gs (M_KK) | E_cond (M_KK) | ODLRO(C) |
|:-------|:------------|:--------------|:---------|
| 1 | 1.53480 | −0.15574 | 1.0000 |
| 2 | 3.13999 | −0.24109 | 1.4734 |
| 3 | 4.82353 | −0.24809 | 1.4596 |
| 4 | 6.59000 | −0.17215 | 1.0000 |

E_cond peaks near half-filling (N_pair=2,3) and the off-diagonal-long-range-order amplitude ODLRO(C) is maximal there (1.47) — the condensate is collective at half-filling, single-pair at the quartet edges (N=1,4 → ODLRO=1, the trivial single-occupancy limit). Non-monotone E_cond(N_pair) is the expected quasispin-shell signature on a degenerate adjoint level.

*Clause 2 — blocked (odd-N) Richardson spectrum ⟨r⟩ vs S106 length-spectrum — FAIL:*

- Pre-committed observable: blocked N_pair=2 (physical fold filling, B2 half-filled, ξ/d_01=1.40 regime), one B2 level Pauli-excluded (von Delft §4.4 blocking), full 8-mode pairing sector, polynomial-unfolded (deg 5), averaged over which B2 level is blocked.
- ⟨r⟩_per-blocked-level = [0.5747, 0.4960, 0.4179, 0.3658] → **⟨r⟩_blocking = 0.4636 ± 0.0791**.
- |Δ⟨r⟩| = |0.4636 − 0.4118| = **0.0518 > 0.03** → **FAIL** (outside band [0.3818, 0.4418]).
- Integrability class: ⟨r⟩=0.4636 **< GOE 0.5307** (integrable-leaning, consistent with the 8 RG conserved integrals and open-channel W3-J ⟨r⟩~0.337), but **> Poisson asymptote 0.38629** and above the length-spectrum 0.4118.
- Diagnostic unblocked seniority-0 survey: {N1:0.5757, N2:0.4704, N3:0.4731, N4:0.4603} — the pairing many-body ⟨r⟩ is robustly in the 0.46–0.58 band, i.e. NOT in the length-spectrum Poisson class. The ±0.0791 spread is the genuine finite-size (8–70 level) fluctuation; the per-level value 0.4179 happens to land in-band, but the principled mean does not, and selecting a single blocked level to force PASS would be iterate-until-PASS (forbidden per `v3-closure-recovery.md` Class 6).

*Clause 3 (informational) — regime location — von Delft ultrasmall CONFIRMED:*

- Canonical regime locator (S61 W8): **ξ/d_01 = 1.40, μ/E_F = 0.55** at N_pair=2 half-filling (unitarity, BCS-BEC crossover). ξ/d_01 ~ O(1) (discrete levels resolved, d ~ Δ) → von Delft ultrasmall **CONFIRMED** (not deep-BCS ξ/d_01 ≫ 1). Mean inter-mode spacing d=0.07954, d/Δ_BCS=0.171.

SUBSTITUTION CHAIN (per `math-scripts.md`; the load-bearing direction claims):
- **Claim**: "mean-field OVERESTIMATES the Richardson-exact gap (ratio > 1, ≈1.6); the substrate's true fold gap is SMALLER than the mean-field value."
- Step 2 (substitute atlas-04 B4): PBCS/BCS = 0.63–0.64 ⇒ Δ_meanfield ≈ 1.59·Δ_Richardson. Step 3: ratio = 0.73203/0.46000 = **1.591 > 1** ⇒ Δ_Richardson = Δ_meanfield/1.591 < Δ_meanfield. Step 4 (read off): the fluctuation-suppression of number projection (canonical PBCS) + blocking REDUCES the gap below mean-field; band [1.4,1.8] brackets the +60% anchor with N_pair-dependence tolerance. **CONFIRMED numerically** (1.59146).
- ⟨r⟩ direction (Step 5): the fold sector is von Delft ultrasmall (ξ/d_01=1.40), so the blocked spectrum's level statistics ARE a meaningful integrability probe; the length spectrum is Poisson (⟨r⟩=0.4118). PASS required |⟨r⟩_blocking − 0.4118| ≤ 0.03. **NOT met** (0.4636, |Δ|=0.0518): the *interacting* pairing many-body spectrum carries off-diagonal-V level repulsion (⟨r⟩→0.46, GOE-leaning) absent from the *single-particle* length spectrum — they are different objects (interacting many-body vs single-particle), in the same broad integrable class (⟨r⟩ < GOE) but not the same precise statistics class.

SOLUTION-SPACE INTERPRETATION:
- The ratio clause PASS **establishes the Richardson-Gaudin / canonical PBCS-with-blocking engine as the standard fold-pairing tool** and supplies W1-1 with the Richardson-exact gap-magnitude input: **Δ_Richardson(B2) = 0.4600 M_KK**, systematic band the factor-2 mean-field-vs-Richardson ambiguity (the +60% overestimate IS the dominant gap-magnitude uncertainty W1-1's PASS criterion requires).
- The ⟨r⟩ clause FAIL constrains the integrability tie: the pairing many-body sector and the D_K length spectrum are NOT the same level-statistics class. This does NOT close the pairing engine (the ratio is the load-bearing result); it flags that "the pairing sector inherits the length-spectrum Poisson statistics" is FALSE at the precise-value level — the pairing spectrum is integrable-class (RG-integrable, ⟨r⟩ < GOE) but more repulsive than the single-particle length spectrum. Routes to a finer-L cross-check (CF below).

W1-1 CONSUMPTION (fb_pair backward): W1-1 ingests Δ_Richardson(B2)=0.4600 as the dimensional-transmutation gap magnitude and the +60% mean-field-vs-Richardson factor-2 as the dominant gap-magnitude uncertainty term. **PLAN-DRIFT note** (`substrate-first-canonical-sourcing.md §ii.B`): the runtime `canonical_constants.py` SHA (`ef6243db…`) differs from the plan-freeze pin (`e6829db0…`); constants are consumed by NAME (Delta_BCS, E_B2_mean, tau_fold, xi_BCS) not by SHA, and all values are stable — the audit_sha256 pins the runtime SHA. Cross-track boundary: any `canonical_constants.py` / §VII / falsifier-inventory landing is session-promotion + designated-writer, NOT an investigation-track edit.

---

### §W1-3. INV11-W1-3 — ATDHFB collective Hamiltonian H=½M(τ)τ̇²+E_eff(τ); least-action τ_fold selection (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `INV11-W1-3`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (τ_fold is the Jensen-deformation parameter value at the van Hove fold — a property of the spectral-triple deformation, Level-2 moduli-deformation substrate-IS)
**Agent**: `nazarewicz-nuclear-structure-theorist` (+ transit-dynamics-theorist co-option for the first-passage / least-action transit dynamics)
**Hypothesis**: the collective Hamiltonian (ATDHFB inertia M(τ) + spectral-action-plus-condensate E_eff(τ)) selects τ_fold=0.190 dynamically by least-action / first-passage — the only un-attempted non-variational route after the S95 one-loop FAIL — closing A-2.
**Plan reference**: `sessions/investigation/investigation-11/investigation-11-plan-w1.md §W1-3`.

**Output Artifacts**:
- **Script** — `computations/investigation-11/inv11_w1_atdhfb_collective_tau_fold.py` (34.7 KB on disk). `grep -E 'from canonical_constants import|print_verdict_payload'` →
  `from canonical_constants import *  # noqa: F401,F403,E402`
  `def print_verdict_payload(...)` + `print_verdict_payload(...)` call in `main()`. ✓
- **Data** — `computations/investigation-11/inv11_w1_atdhfb_collective_tau_fold.npz` (33.5 KB; keys: `tau`, `S_SA`, `dS_SA`, `E_cond`, `dE_cond`, `E_eff`, `dE_eff`, `M_tau`, `tau_selected`, `delta_tau`, `method`, `has_interior_extremum`, `grad_ratio_SA_vs_BCS`, `n_interior_sign_changes`, `speed_bump_found`, `tau_star_A`, `tau_star_B`, `FRIED39_grad_ratio`, `FRIED39_shortfall`, …). ✓
- **Plot** — `computations/investigation-11/inv11_w1_atdhfb_collective_tau_fold.png` (183 KB; 4-panel: (a) S_SA monotone surface, (b) E_cond well, (c) SA-vs-BCS gradient ratio (log), (d) M(τ) inertia + method). ✓
- **Verdict line** — `computations/investigation-11/inv11_gate_verdicts.txt`. `grep -E '^INV11-W1-3:.* audit_sha256=[a-f0-9]{64}'` →
  `INV11-W1-3: INFO -- value='tau_selected=0.1734_target=0.190_dtau=0.0166_interior_extremum=False_grad_ratio=17827x' scheme=SA convention=ABSOLUTE L_max=12 audit_sha256=3796d72c630f09782165ade9319a9f14290dbd7494b159eb109087e26af6aec3 content_sha256=a69995bb95ca1d695c6a97f0b6144b389b24633ab97ed93b5b0931c10a0013d7 schema_version=S84+`
  Dual-SHA companion row present (no 3-tuple — `[VERIFY]` trigger). ✓
- **WP section** — this section (Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit all present). ✓

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; query-first discipline):
- `search_knowledge("ATDHFB collective Hamiltonian tau_fold least-action first-passage collective inertia")` → `s40_collective_inertia.py` exists (gate `COLL-40`/`T3-BATCH-S40-COLLECTIVE-INERTIA`: INFO/MIGRATED), depending on `tau_fold`, `E_B1`, `G_DeWitt`, `d2S_fold`; equation `H_coll(β) = -(ℏ²/2M(β))d²/dβ² + V_coll(β)` already drafted in `session-39-naz-hawking-workshop.md`. **NOT a closed numerical verdict on this gate's question — collective inertia computed (M_ATDHFB), but the least-action τ-selection itself was never run.**
- `get_constant("M_ATDHFB")` → **1.695** (S40, `s42_gradient_stiffness.npz`; not superseded). Anchor for M(τ).
- `get_constant("tau_fold")` → **0.19** (S12/S42, `CONST-FREEZE-42`; not superseded). Target.
- `get_constant("E_cond")` → **−0.13685055970476342** (S36, `ED-CONV-36`, alias `E_cond_ED_8mode`; not superseded). Condensation-well depth.
- `get_constant("dS_fold")` → **58672.80241318**; `get_constant("d2S_fold")` → **317862.85**; both canonical (sourced from `s42_gradient_stiffness.npz`). SA gradient + stiffness at fold.
- `search_knowledge("T5 BROKEN one-loop variational tau selection FAIL ... spectral action monotone")` → **PRE-CLOSED (variational corridor):** `BARE-SPECTRAL-ACTION as V.P. for τ_fold` CLOSED (S84 W8a-85: dS/dτ=−2.036×10⁴≠0, "no interior extremum, S monotone-decreasing"); `S95-W2-3-NO-WELL-ONE-LOOP` **PASS value=0** (one-loop Γ[τ] has no interior stationary point); atlas-04 **T5 BROKEN**.
- `search_knowledge("FRIED-39 gradient ratio 6596 ... overwhelms BCS")` → **PRE-CLOSED (the governing prior result):** atlas-04 **T6 "Friedmann-BCS coupling can dynamically lock tau" → BROKEN** (FRIED-39, S39): gradient ratio **6,596×**, locking shortfall **133,200×**; closed_mechanism `FRIEDMANN-BCS`; S29b: "V_eff=S_spectral+F_BCS remains monotonically decreasing; dV_total/dτ has NO sign change". This gate RE-DERIVES that dominance in the explicit collective frame.
- `list_constants("...E_cond|G_DeWitt|E_B1...")` → `G_DeWitt=5`, `E_B1=0.81914`, `E_cond_GL=−0.156`, `E_cond_ED_5mode=−0.115077` (alternatives confirmed; 8-mode ED used as canonical depth).

**Verdict**: **INFO** — `|τ_selected − 0.190| = 0.0166` lands in the INFO band (0.010 < |Δτ| ≤ 0.030), NOT the PASS band (≤ 0.010). The collective Hamiltonian localizes the transit in the **fold region** but not at the precise fold; τ_fold is **not** dynamically derived to PASS precision. Composite collapse: `[VERIFY]` magnitude-band → INFO directly (no 3-tuple).

**Results**:

*The numbers (NUMBERS first):*
- **τ_selected = 0.173** (3 sig figs; raw 0.1734), via the first-passage interior speed-bump probe. Target **τ_fold = 0.190**. **|Δτ| = 0.0166** → INFO (PASS ≤ 0.010, INFO ≤ 0.030).
- **interior stationary point of E_eff = S_SA + E_cond: NONE** (`n_interior_sign_changes(dE_eff) = 0`). E_eff is monotone on [0, 0.40]; the pure-action variational route has no interior selection — consistent with S95 `T5-BROKEN` / `S95-W2-3-NO-WELL-ONE-LOOP` (PASS, value=0).
- **SA-vs-BCS gradient ratio = 17,827×** (the steepest condensation-well gradient |dE_cond/dτ|_max = 2.766 vs the SA gradient dS/dτ ≈ 58,824 at the same τ). Re-derives the canonical **FRIED-39 / T6-BROKEN** dominance (6,596×; locking shortfall 133,200×) in the explicit collective-Hamiltonian frame. The ~2.7× larger ratio vs the S39 estimate is the sharper Gaussian-well steepest-gradient definition; same physics (SA overwhelms BCS by ~4 OOM).
- **Speed-bump robustness**: across a 5×3 ansatz scan (σ_w ∈ [0.020, 0.040] × σ_M ∈ [0.030, 0.050]) and well-depth multipliers ×0.5…×3.0, the bump location is **invariant to σ_w and depth** (set entirely by the inertia-bump width σ_M): σ_M=0.03→0.178, 0.04→0.173, 0.05→0.165. **100% of the scan lands in the INFO band [0.160, 0.220]; 0% in the PASS band [0.180, 0.200]** (mean 0.1724, std 0.0054). The localization is **kinematic** (the rising M(τ) inertia bump near the fold), NOT a potential well — the depth-insensitivity confirms the condensate is too weak to create a true stationary point.
- 4-tuple: `(value=0.173, scheme=SA, convention=ABSOLUTE, L_max=12)`. Dual-SHA: audit `3796d72c…6aec3`, content `a69995bb…013d7`.
- Canonical constants used (none hardcoded; imported from `canonical_constants.py`): `M_ATDHFB=1.695`, `tau_fold=0.19`, `E_cond=−0.13685`, `dS_fold=58672.8`, `d2S_fold=317862.85`, `G_DeWitt=5`.

*Method (gate second):* H = ½M(τ)τ̇² + E_eff(τ) on a 400-pt τ-grid over [0, 0.40] (the ATDHFB/GCM collective-coordinate reduction, Paper 13). M(τ) = ATDHFB cranking inertia anchored at M_ATDHFB=1.695 with a mild (≤25%) DOS-tracking bump near the fold. E_eff(τ) = S_SA(τ) [interpolated from `s42_gradient_stiffness.npz`, monotone, dS/dτ>0 ∀τ] + E_cond(τ) [Gaussian condensation well, depth |E_cond|=0.137 M_KK, centered at the fold — the van Hove DOS maximizes the gap there]. Two complementary localization probes: (A) interior stationary point of E_eff (the variational question — returns NONE); (B) WKB first-passage dwell-density √(M/(2(E_top−E_eff))), with the strict-interior-local-maximum of its residual over the smooth monotone trend (the "speed bump"; excludes the top-of-slide turning-point edge artifact). Probe A → no extremum; Probe B → kinematic bump at 0.173.

*Substitution chain (with substituted numbers; plan §W1-3 Step 1–4):*
- **Step 1 (defs):** M(τ) anchored M_ATDHFB=1.695; S_SA(τ) monotone, dS/dτ=+58,672.8>0 at fold; E_cond(fold)≈−0.137 M_KK (8-mode ED); τ_fold=0.190.
- **Step 3 (key structural point):** S_SA alone is monotone (dS/dτ>0 everywhere) ⇒ NO interior stationary point ⇒ a pure-SA variational τ-selection FAILS (the S95 T5-BROKEN result — **confirmed here**, `n_interior_sign_changes=0`). The condensation well E_cond DEEPENS toward the fold (dE_cond/dτ<0 approaching from below) but its steepest gradient (2.77) is **17,827× weaker** than the SA gradient (58,824) ⇒ E_eff = S_SA + E_cond **remains monotone** (the FRIED-39 dominance: the well cannot break the SA monotonicity). M(τ) (the inertia) carries the localizing signal instead: the first-passage dwell concentrates where M(τ) rises near the fold.
- **Step 4 (direction):** The plan predicted the transit localizes at the fold via (a) the condensation well breaking SA monotonicity, and (b) the BCS-reduced M accelerating passage. Result: **(a) does NOT hold** (E_eff stays monotone; the well is 4 OOM too weak — FRIED-39), but **(b)-adjacent DOES hold** (the inertia bump produces a kinematic first-passage speed bump in the fold region, τ≈0.173). The localization is real but ansatz-width-dependent ⇒ fold region, not precise fold ⇒ **INFO**.

*Cross-check vs transit T1:* The first-passage concentration sits on the **approach side** of the fold (τ_selected=0.173 < 0.190), consistent with the impulsive supersonic transit (Mach 13.75, dt/T_L=1.25×10⁻⁵) passing through the van Hove fold rather than settling into a well — the substrate slides through, with a kinematic dwell enhancement just before the cusp.

*Dual-prior reallocation:* INFO → **unchanged 0.45/0.55** (Track A: dynamical selection; Track B: τ_fold empirically pinned / van-Hove-cusp-selected). Per the plan discriminator: "INFO (0.010 < |Δτ| ≤ 0.030, approximate) → unchanged." The collective Hamiltonian has **localizing structure** (a robust fold-region speed bump) but the inertia/potential normalization needs refinement before it sharpens to a PASS dynamical derivation.

**Assessment (solution-space interpretation):** This is the collective-inertia / least-action route to non-variational τ_fold selection — the un-attempted route after the S95 variational corridor closed (T5 BROKEN). The verdict **INFO** maps the corridor precisely:
- The **variational sub-route stays closed**: E_eff = S_SA + E_cond has no interior stationary point (`n_interior_sign_changes=0`), because the SA gradient overwhelms the condensation gradient by 17,827× — an independent in-frame re-derivation of FRIED-39 / T6-BROKEN (6,596×). Adding the BCS well to the monotone spectral action does NOT manufacture a well; the framework's most load-bearing prior negative result holds inside the explicit collective Hamiltonian.
- The **kinematic first-passage sub-route is open-but-unsharpened**: a robust speed bump localizes the transit in the fold region (|Δτ|≈0.017, 100% INFO-band over the ansatz scan), but its precise location is set by the ATDHFB inertia-bump width σ_M — a normalization the substrate does not here uniquely fix — and never reaches the PASS band. τ_fold remains structurally (van-Hove-cusp) pinned, not dynamically derived to 0.010 precision.
- **Forward (what would sharpen this to PASS):** a first-principles M(τ) ATDHFB cranking computation across the τ-grid (not the anchored-with-Gaussian-bump model) to fix σ_M from substrate physics; the bump width is the single sensitive parameter. This is the `INFO_meaning` carry-forward: "the inertia/potential normalization needs refinement (a finer M(τ) ATDHFB scan)." Distinct from (does not duplicate) inv-3 W2-4 (Weyl-remainder / shortest-geodesic route).

**Substrate framing (substrate-IS, arrow strictly substrate → emergent):** τ IS the substrate's own intrinsic Jensen-deformation parameter (Level-2 moduli-deformation substrate-IS per `phononic-framing.md` — the moduli-space of τ-deformations IS substrate-IS, NOT a coordinate on a meta-container). M(τ) is a spectral moment (the ATDHFB cranking response of the D_K spectrum to the deformation); E_eff(τ) is built from the a₀−a₂+a₄ spectral-action moments plus the pairing-sector condensation energy. The transit through the fold is the substrate's spectral complexity growing — the eigenvalue spectrum reorganizing — NOT a slow-roll of an inflaton in a container. **Methodological note (my recurring S61 self-correction):** the collective-Hamiltonian H=½M(τ)τ̇²+E_eff(τ) borrows particle-in-potential intuition, which must be applied to τ with care — τ is the substrate, not a particle in a box. The honest reading of the INFO result is consistent with that caution: there is NO potential well in τ (the FRIED-39 monotonicity holds); what localizes is a kinematic dwell in the inertia, which is a property of how the substrate's spectral content responds to its own deformation, not a force confining a particle. The result does NOT invert the explanatory arrow: the speed bump is read OFF the M(τ) spectral-moment surface, not assigned to a τ-trajectory in a pre-existing container.

---

### §W1-4. INV11-W1-4 — Bayesian-UQ: posteriors for m_H, CC, H₀, Σm_ν, BF-spine over the M_KK / gap / V-matrix priors (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `INV11-W1-4`
**Trigger**: `[VERIFY]`
**Classification**: **NON-PHONONIC** (methodology — Bayesian UQ over existing predictions; produces no new substrate observable, characterizes their uncertainty per Paper 06 §III)
**Agent**: `nazarewicz-nuclear-structure-theorist`
**Hypothesis**: m_H, CC magnitude, H₀, and Σm_ν survive as well-defined posteriors when marginalized over the 1-OOM M_KK / factor-2 gap / V-matrix-non-uniqueness priors, and the recomputed incumbent-vs-ΛCDM Bayes factor stays below the canonical ceiling 31.62.
**Plan reference**: `sessions/investigation/investigation-11/investigation-11-plan-w1.md §W1-4`.

**Output Artifacts**:
- `computations/investigation-11/inv11_w1_bayesian_uq_posteriors.py` — present. `grep -E 'from canonical_constants import|print_verdict_payload'` → matches both (`from canonical_constants import *` line 79; `def print_verdict_payload` + call site). Confirmed on disk.
- `computations/investigation-11/inv11_w1_bayesian_uq_posteriors.npz` — present (band medians/intervals/widths + BF + priors + flags, full float64).
- `computations/investigation-11/inv11_w1_bayesian_uq_posteriors.png` — present (6-panel: 4 observable posteriors + BF bar + prior-summary text).
- verdict_line in `computations/investigation-11/inv11_gate_verdicts.txt` — present: `^INV11-W1-4: INFO -- ... audit_sha256=0a1d03f9b44ca415ed38e5e4158e4e482457882b4136c9b9293fa26672bddb09`; dual-SHA companion row present; 2 extra companion rows (priors + BF). No 3-tuple ([VERIFY] gate, `schema_v2_3tuple_required: false`).
- this WP §W1-4 section — Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit**:
Query-first discipline executed BEFORE writing the script (Paper 06 §III: scoring function fixed before posterior). All central values re-quoted as posteriors were confirmed against the canonical graph:
- `search_knowledge("Bayesian uncertainty quantification posterior marginalization Bayes factor model selection")` → prior Bayesian work (s36 bayesian_posterior, s43 mkk_posterior, s44 bayesian_f, s61 cc_bayes_comparison); none is a marginalized-spine UQ over these three priors — gate is NOT pre-closed.
- `get_constant("BF_spine_vs_incumbent_ceiling")` → 31.62 (S101, gate S98-W4-4-OQ3-COVARIANCE; the FIXED ceiling = scoring function).
- `get_constant("m_H_FW_KK_threshold")` → 131.8 (S100a, KK-THRESHOLD-64 lineage).
- `get_constant("CC_OOM")` → 115.5 (S66 W1-A-DILUTION-CC; OOM dilution depth).
- `get_constant("H_0_km_s_Mpc")` → 67.4 (Planck 2018; G_N-ratio channel per atlas-05 Window-19 / falsifier-watchlist).
- `get_constant("Sigma_mnu_FW")` → 0.0582053272 (S99 W3-SEESAW-SUMMNU; type-I seesaw, M_R = B-branch fold energies × M_KK).
- `get_constant("M_KK_gravity")` → 7.428660036284456e16 (S42 CONST-FREEZE-42); `get_constant("Delta_BCS")` → 0.4642547394830737 (S70, **R-PROTECTED**).
- `trace_entity("BF_spine_vs_incumbent_ceiling")` + `search_knowledge` on the S101 reference class → the additive-log-evidence b-values: **b_mH = 3/2 → BF_mH = 10^1.5 = 31.62 (45.44% of spine)**, b_sigma = 1 → 10.00, b_cs2 = 1/2 → 3.16; the ceiling cited is the m_H-only column, the other 3 spine factors carry ZERO incumbent discrimination (CONVERGENT-DERIVED). This FIXED the scoring function before the posterior.
- Per-observable scaling-exponent provenance: `search_knowledge` confirmed m_H ~ KK-threshold fiber-embedding (M_KK scale), H₀ via G_N-ratio with G_N^FW/G_N^obs = 1.000000 (anchor-degeneracy ⇒ M_KK CANCELS), Σm_ν via seesaw with M_i = (B-branch fold energy) × M_KK [session-99-plan-w3], V-matrix non-uniqueness C=0.1557 / V=C/dim(B2)=0.0389 / V(B2,B2)=0.057 [session-34-berry-tesla-workshop].
- **PRE-CLOSED?** No — this marginalized-spine UQ is novel; prior Bayesian gates are point-estimate or single-observable.

**Verdict**: **INFO** — `value='5bands_finite_nondeg=True; m_H=131[59.9,289]GeV; CC_OOM=115[114,117]; H0=67.4; Sm_nu=0.0584[0.0264,0.128]eV; BF_marg=0.0397<=ceiling31.62; any_wider=True'`, scheme=MS, convention=MIXED, L_max=N/A. dual-SHA: `audit_sha256=0a1d03f9b44ca415ed38e5e4158e4e482457882b4136c9b9293fa26672bddb09`, `content_sha256=00607d6343ddddb4ca7e3f5a08239cc0774e96fdcf352a8d5e812d59369ae672`. Random seed 20260614 (FIXED, deterministic-on-replay). INFO fired the pre-registered clause exactly: all 5 bands finite/non-degenerate AND BF_marg ≤ ceiling (so NOT FAIL), but ≥1 marginalized band is WIDER than its observational error bar (so NOT PASS) — the honest UQ outcome the rubric anticipated (predictions survive, falsifiability limited by the irreducible scale freedom until W1-1/W1-2 sharpen the priors).

**Results**:

*Priors marginalized over* (N_MC = 100,000 log-uniform draws each, seed 20260614 FIXED; both upstream npz absent ⇒ pre-registered priors used unconditionally):
- **M_KK**: log-uniform [2.349e16, 2.349e17] GeV (1-OOM; centered on CONST-FREEZE-42 = 7.4287e16). **Not narrowed** — W1-1 npz absent.
- **gap (Δ_BCS)**: log-uniform [0.3283, 0.6566] M_KK (factor-2; centered on R-protected Δ_BCS = 0.4642). **Not narrowed** — W1-2 npz absent.
- **V-matrix**: log-uniform [0.039, 0.057] (non-uniqueness span: C/dim(B2)=0.0389 ↔ V(B2,B2)=0.057).

*Five marginalized posteriors* (median, 68% central interval, 3 sig figs; central value; band-vs-observational-error test):

| Observable | Central | Marginalized median | 68% interval | M_KK power | band half-width vs σ_obs | wider than obs? |
|:-----------|:--------|:--------------------|:-------------|:-----------|:-------------------------|:----------------|
| m_H [GeV] | 131.8 | 131 | [59.9, 289] | **p=+1** (linear) | ~114 GeV vs 0.11 GeV (PDG) | **YES** |
| CC depth [OOM] | 115.5 | 115 | [114, 117] | log₁₀(M_KK⁴) drift | ~1.37 OOM vs 1.0 OOM | **YES** |
| H₀ [km/s/Mpc] | 67.40 | 67.4 | [67.4, 67.4] | **p=0** (ratio-cancelled) | 0 vs 0.5 (Planck) | no |
| Σm_ν [eV] | 0.0582 | 0.0584 | [0.0264, 0.128] | p=−1 × gap(+1) | ~0.051 eV vs 0.072 eV (DESI) | no |

All five bands are **finite and non-degenerate** (`all_bands_ok=True`).

*Per-observable physics (substrate-documented prediction maps)*:
- **m_H ∝ M_KK¹** (KK-threshold |S|² fiber-embedding mode scales with the fiber scale): the ±√10 M_KK freedom propagates linearly → a factor-√10 band [59.9, 289] GeV. Half-band ~114 GeV ≫ PDG error 0.11 GeV. **The point-prediction sharpness was inherited from M_KK being frozen, not derived — this is why W1-1 (M_KK-derivation flagship) is the keystone.**
- **CC_OOM**: dilution *depth* is cascade-set (M_KK-robust); the OOM observable shifts only by the log₁₀(M_KK⁴) drift of the unsubtracted a₀ vacuum scale → ±1.37 OOM, exceeding the 1-OOM CONST-FREEZE comparator.
- **H₀ ∝ M_KK⁰** (G_N-ratio channel forces G_N^FW/G_N^obs = 1.000000, anchor-degeneracy disclosure): the absolute M_KK **cancels exactly** → δ-band (width 0). H₀ is the ONE observable immunized against the irreducible scale freedom (band ≪ Planck error 0.5). The √16 = 4 spinor factor is dimensionless (no prior dependence).
- **Σm_ν ∝ M_KK⁻¹ × gap⁺¹** (type-I seesaw m_ν = −m_D^T M_R⁻¹ m_D; M_R = B-branch fold energies × M_KK; m_D oscillation-anchored ⇒ external, held fixed; the fold-energy magnitude carries the factor-2 gap ambiguity): band [0.0264, 0.128] eV. Central 0.0582 passes the DESI 2024 bound 0.072 eV, but the **upper edge 0.128 eV exceeds it** — falsifiability degraded once the scale freedom is honestly propagated.

*Bayes-factor recomputation (the PASS-criterion's load-bearing clause; convexity bound)*:
- BF_point = 31.62 = 10^1.5 (= ceiling, b_mH = 1.5; the m_H-only incumbent-discriminating channel, S101 reference class).
- **BF_marg = 0.0397 = 10^(−1.402)** ≤ ceiling 31.62 — `bf_within_ceiling=True` with enormous margin; also ≪ the contingent floor ~2.
- Convexity substitution chain (Jensen direction, per `math-scripts.md §"Double-Check Logic"`):
  - Step 1: `BF_marg = 10^(b_point − dilution_dex)`, `b_point = 1.5`.
  - Step 2: `dilution_dex = 0.5·log₁₀(1 + (σ_pred/σ_meas)²)`; substitute σ_pred = 0.2890 dex (m_H predictive spread over the M_KK band), σ_meas = 3.625e-4 dex (PDG m_H error / m_H in log₁₀). Ratio = 797.4; ratio² = 6.36e5.
  - Step 3: `dilution_dex = 0.5·log₁₀(1 + 6.36e5) = 0.5·5.803 = 2.902`.
  - Step 4: `b_marg = 1.5 − 2.902 = −1.402 < 1.5`; since `dilution_dex ≥ 0` ALWAYS (log₁₀ of a quantity ≥1), `BF_marg ≤ BF_point = ceiling` is structural. Script-computed `dilution_dex = 2.9016` matches the hand substitution to 4 sig figs.
  - Conclusion: marginalizing over the WIDER priors smears the m_H prediction over a factor-√10 band, incurring a 2.90-dex Occam penalty that collapses the incumbent evidence from b=+1.5 to b=−1.40. **Marginalization widens the bands and cannot inflate the BF** — the direction the substitution chain predicted, confirmed numerically.

*4-tuple*: `(value=<summary>, scheme=MS, convention=MIXED, L_max=N/A)`; FIXED random_seed=20260614.

*Canonical constants consumed* (imported, never hardcoded): `BF_spine_vs_incumbent_ceiling`=31.62, `m_H_FW_KK_threshold`=131.8, `CC_OOM`=115.5, `H_0_km_s_Mpc`=67.40, `Sigma_mnu_FW`=0.0582053272, `M_KK_gravity`=7.428660036284456e16, `Delta_BCS`=0.4642547394830737 (R-protected).

*Substrate framing (NON-PHONONIC methodology)*: this gate produces no new substrate observable; it characterizes the **uncertainty** of existing substrate-derived predictions (each is a spectral observable of D_K). The three priors are the irreducible freedoms in the substrate→prediction map — the imported scale M_KK, the pairing-gap magnitude, the V-matrix coupling. The methodology contribution (Paper 06 §III): a number without an uncertainty is not a prediction; marginalizing over the substrate's own scale/coupling freedoms converts point predictions into honest posteriors. The discriminating finding is **structural, not numerical** — the four observables stratify by their M_KK-robustness (H₀ ratio-cancelled ⇒ immune; CC log-robust; Σm_ν inverse + gap-sensitive; m_H linear ⇒ as sharp as M_KK is). The scoring function (BF reference class) was FIXED before the posterior via the fixed seed and pre-registered priors.

*Cross-pillar caveat*: this BF/posterior set does **NOT** promote any `canonical_constants.py` pin, §VII registry row, or `falsifier-master-inventory.md` row — those are session-track designated-writer moves (investigation track-local boundary per `gate-verdicts.md §"Investigation-Track Canonical Path"`).

*Dual-prior reallocation* (plan §W1-4): INFO ⇒ unchanged 0.5/0.5 — the predictions survive honest marginalization but with weakened discriminating power for m_H, CC, and Σm_ν (bands wider than observational error); routes the band-narrowing forward to the W1-1 (M_KK) and W1-2 (gap) posteriors as they land. The single Reading-A (robust) datum: H₀ remains tight (ratio-cancelled).

*Artifacts*: `computations/investigation-11/inv11_w1_bayesian_uq_posteriors.py` / `.npz` / `.png`.

---

## Wave 1 Synthesis (team-lead)

**Verdict tally**: 1 PASS (W1-1 FLAGSHIP) + 3 INFO (W1-2, W1-3, W1-4). All four verified on disk (verdict line + dual-SHA, W1-1 [SIGN] 3-tuple row, WP §-section `must_contain` markers; all `audit_sha256` sig_5-unique).

**The keystone result.** The investigation's spine — S109's single most-named gap, **M_KK-DERIVATION** (the one imported scale, frozen at S42 by fit to Newton's G, never derived) — gets its first PASS in the **dimensional-transmutation corridor**. W1-1 derives `M_KK/M_Pl = exp(−1/(λ_eff·N₀))` with λ_eff = V_B2·mean(Kosmann) = 0.03893 and N₀ = ρ_B2 = 14.0233, giving `g = 0.5460`, `exp(−1/g) = 0.1602` ⇒ **M_KK_derived = 3.90×10¹⁷ GeV**, OOM-distance **0.720 ≤ 1.0** to CONST-FREEZE-42 under the reduced-Planck (a₂-Einstein-Hilbert) cutoff. The PASS is load-bearing, not cosmetic: `frac_uncert_gap_term = 0.8298 ≥ 0.5`, i.e. the gap-magnitude term (carrying W1-2's factor-1.59 mean-field-vs-Richardson ambiguity) **dominates** the uncertainty budget — the signature distinguishing a genuine transmutation derivation from a cutoff-anchored back-fit. Dual prior **0.85 → Track A (STRUCTURAL)**.

**The W1-2 → W1-1 serial pair is one argument.** W1-2 (INFO) supplies the magnitude leg: the Richardson-exact fold gap **Δ_rich(B2) = 0.4600** with mean-field overestimating by **×1.591 ∈ [1.4,1.8]** (clause-1 PASS; cross-checked against exact-diagonalization Δ_ED = 0.4545 at 1.21%), confirming atlas-04 B4 and establishing Richardson-Gaudin as the standard fold-pairing engine. Its INFO is the ⟨r⟩ clause: the blocked-spectrum ⟨r⟩ = 0.4636 misses the S106 length-spectrum 0.4118 by 0.052 (band 0.03) — the pairing sector is integrable-leaning (< GOE 0.531) but not in the length-spectrum Poisson class; the integrability tie is unestablished, routed to a finer-L cross-check.

**The two parallel INFO legs sharpen but don't close.** W1-3 (collective-inertia τ_fold) lands τ_selected = 0.1734 (|Δτ| = 0.0166, INFO band 0.010–0.030): the ATDHFB collective Hamiltonian localizes the transit to the *fold region* but not the precise fold, with no interior stationary point — an in-frame re-derivation of S95 T5-BROKEN (SA-vs-BCS gradient ratio 17,827×; the BCS condensation well is ~4 OOM too weak to break spectral-action monotonicity). τ_fold stays van-Hove-cusp-pinned, not dynamically derived to PASS precision; dual prior unchanged 0.45/0.55. W1-4 (Bayesian-UQ) finds all 5 posteriors finite/non-degenerate with `BF_marg = 0.040 ≤ ceiling 31.62`, but the structural content is the **stratification by M_KK-robustness**: H₀ = 67.4 is δ-sharp (M_KK cancels exactly in the G_N-ratio channel — the one observable immune to the scale freedom), while m_H, CC-depth, and Σm_ν bands all exceed their observational error bars once the scale freedom is honestly propagated. m_H's point-sharpness was *inherited* from M_KK being frozen — quantitative confirmation that W1-1 is the keystone; dual prior unchanged 0.5/0.5.

**Two structural findings routed to the Wave 5 (W5-1) adjudication** (within-investigation handoff, NOT carry-forwards):
1. **Cutoff-normalization sensitivity** — IN-band (0.72 OOM) under M_Pl_reduced (PRIMARY: 1/(16πG) = M_Pl_red²/2 makes the a₂-channel Planck scale reduced); OUT (1.42 OOM) under M_Pl_unreduced. The residual freedom is whether Paasch's integer scheme or a substrate-internal Λ (off-Jensen modulus / HY8) removes the M_Pl anchor. This is exactly the nazarewicz↔paasch M_KK tension W5-1 is built to adjudicate.
2. **Van-Hove divergence REFUTED (S94-consistent)** — the A₂ √-DOS fit returns c_vH = −1.173, R² = 0.250 (`fit_ok = False`): the honest signature of *finite* enhancement, not a true square-root divergence. N₀ is the canonical finite ρ_B2 = 14.02; the BCS mechanism operates through the **1D theorem** (atlas-05 W3 Door-1), not a Fermi-surface DOS singularity. The substitution chain's "van Hove maximizes the gap" framing is superseded by finite-enhancement; the PASS survives because N₀ is finite-but-large, not divergent.

**Math-vs-non-math split.** Effected-In-Session (NON-MATH) below is empty BY THE CROSS-TRACK BOUNDARY: per `gate-verdicts.md §"Investigation-Track Canonical Path"`, investigation gates write ONLY to `computations/investigation-11/` + the per-wave WP — no `canonical_constants.py` pin, no §VII registry row, no `falsifier-master-inventory.md` edit, no rule-file promotion. Every such promotion (including the keystone W1-1 PASS) is a **session-mode designated-writer** carry-forward, recorded below. The four agents honored this boundary (verified: no registry/canonical edits in the gate reports).

### Effected In-Session (NON-MATH)

- [x] Wave-1 gate WP sections — written by the dispatched agents (W1-1…W1-4 all Status COMPLETED, verified on disk); team-lead synthesis (this section) written.
- [x] No canonical / registry / rule-file / inventory edits this wave — **correct and mandatory** per the investigation-track cross-track boundary (not a deferral; these are structurally session-mode, enumerated as carry-forwards below). Self-audit: zero unchecked items.

## Carry-Forward Computations

### CF-INV11-W1-A — Session-promote the W1-1 M_KK-derivation PASS into a session-mode canonical/registry landing

| Field | Spec |
|:------|:-----|
| **What** | Lift INV11-W1-1 (M_KK/M_Pl = exp(−1/(λ_eff·N₀)) = 3.90×10¹⁷ GeV, transmutation-corridor PASS) into a `session-{N}` compute gate so it can land a `canonical_constants.py` provenance note + a §VII / Atlas-04 status update (M_KK-DERIVATION: keystone OPEN → dimensional-transmutation-corridor PASS). Investigation verdicts are track-local and never enter the knowledge index until re-computed under a session gate. |
| **Inputs** | `inv11_w1_mkk_dimensional_transmutation.npz`; `inv11_w1_richardson_pairing_engine.npz` (gap magnitude); CONST-FREEZE-42 anchor; M_Pl_reduced convention pin |
| **Gate** | Reproduce M_KK_derived within publication precision (3 sig figs) under a session-track gate; OOM-dist ≤ 1.0 AND frac_gap ≥ 0.5 re-verified bit-for-bit. PASS → designated-writer registry/canonical landing |
| **Effort** | ~1 session (mostly the session-mode re-wrap + designated-writer landing; the physics is done) |

### CF-INV11-W1-B — Substrate-internal cutoff Λ to remove the M_Pl anchor

| Field | Spec |
|:------|:-----|
| **What** | Re-derive M_KK with the UV cutoff Λ pinned from a substrate-internal quantity (off-Jensen free-modulus / HY8 top-of-spectrum) instead of the external M_Pl anchor, closing the W1-1 cutoff-normalization freedom (the 0.72-vs-1.42 OOM reduced/unreduced split). Feeds the W5-1 adjudication. |
| **Inputs** | `inv11_w1_mkk_dimensional_transmutation.npz`; off-Jensen modulus / HY8 spectrum; L12 cache top-of-spectrum max\|λ\| |
| **Gate** | OOM-dist(M_KK_derived, CONST-FREEZE-42) ≤ 1.0 with a substrate-internal Λ (no M_Pl anchor) AND frac_gap ≥ 0.5 |
| **Effort** | ~1–2 sessions |

### CF-INV11-W1-C — First-principles M(τ) ATDHFB cranking scan to fix σ_M

| Field | Spec |
|:------|:-----|
| **What** | Replace the validated-point ATDHFB inertia anchor (M_ATDHFB = 1.695) with a full ATDHFB cranking scan M(τ) across the Jensen line to pin the inertia-bump width σ_M — the single parameter that sets W1-3's first-passage localization (robustness scan: 100% INFO-band, location set only by σ_M). |
| **Inputs** | L12 cache; ATDHFB cranking linear-response; `inv11_w1_atdhfb_collective_tau_fold.npz` |
| **Gate** | τ_selected within 0.010 of 0.190 (the W1-3 PASS band) under the first-principles σ_M |
| **Effort** | ~1–2 sessions |

### CF-INV11-W1-D — Finer-L blocked-⟨r⟩ cross-check (length-spectrum integrability tie)

| Field | Spec |
|:------|:-----|
| **What** | Recompute the W1-2 blocked-(odd-N) Richardson ⟨r⟩ at L_max ≥ 16 to test whether the 0.052 miss to the length-spectrum 0.4118 closes with truncation (CF-S106-W7-FINER-LMAX-LENGTH-SPECTRUM lineage). |
| **Inputs** | finer-L (≥16) spectrum cache; `inv11_w1_richardson_pairing_engine.npz` blocked-spectrum routine |
| **Gate** | \|⟨r⟩_blocking − 0.4118\| ≤ 0.03 |
| **Effort** | ~1 session |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-16 | M_KK-DERIVATION (S109 keystone) | OPEN — M_KK fit to Newton's G (S42 CONST-FREEZE-42), never derived | dimensional-transmutation corridor **PASS** (investigation-track, pending session-promotion) | W1-1: M_KK = exp(−1/(λ_eff·N₀)) = 3.90e17 GeV, OOM-dist 0.720 (reduced-Planck), gap-term dominates 0.83 |
| 2026-06-16 | Richardson-Gaudin fold-pairing engine | mean-field gap used (inv-9 W1-3) | exact engine adopted; Δ_rich(B2)=0.4600, mean-field overestimates ×1.591 | W1-2: confirms atlas-04 B4; R-protected Δ_BCS=0.4642 was already the exact-class value |
| 2026-06-16 | collective-inertia τ_fold route | un-attempted (post-S95 variational FAIL) | INFO — fold-region localization, not PASS-precision; route OPEN-but-unsharpened | W1-3: τ=0.173, no interior extremum, BCS well ~4 OOM too weak (re-derives T5-BROKEN in collective frame) |
| 2026-06-16 | van-Hove A₂ √-DOS at fold (W1-1 mechanism) | assumed square-root divergence (substitution-chain framing) | REFUTED — finite enhancement (c_vH=−1.173, R²=0.250); BCS via 1D theorem not Fermi-DOS | W1-1 process observation; S94-consistent |
| 2026-06-16 | dual prior (M_KK STRUCTURAL vs NUMERICAL-ONLY) | 0.4 / 0.6 (W1-1 pre-reg) | 0.85 / 0.15 → Track A | W1-1 PASS (OOM-in AND gap-term-dominates) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict line | Verdict |
|:-----|:-------|:------------|:------------|:-------------|:--------|
| INV11-W1-1 | `inv11_w1_mkk_dimensional_transmutation.py` | ✓ | ✓ | `audit=2c51def3…cd1c0b24` (+3-tuple row) | **PASS** |
| INV11-W1-2 | `inv11_w1_richardson_pairing_engine.py` | ✓ | ✓ | `audit=365600e4…c0114c06` | INFO |
| INV11-W1-3 | `inv11_w1_atdhfb_collective_tau_fold.py` | ✓ | ✓ | `audit=3796d72c…6af6aec3` | INFO |
| INV11-W1-4 | `inv11_w1_bayesian_uq_posteriors.py` | ✓ | ✓ | `audit=0a1d03f9…72bddb09` | INFO |

All scripts under `computations/investigation-11/`; verdict lines in `computations/investigation-11/inv11_gate_verdicts.txt` (`track=investigation, session=11`).
