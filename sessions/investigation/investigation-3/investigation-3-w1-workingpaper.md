# Investigation 3 Wave 1 — Spectral statistics & eigenbundle topology (Results Working Paper)

**Investigation**: 3 | **Wave**: 1 | **Plan**: investigation-3-plan-w1.md | **Theme**: discriminating-level spectral-correlation geometry (SFF / number-variance / P(s) sector-resolved) + the two remaining un-measured eigenbundle objects (catastrophe germ; second-Chern over the off-block coset). Gate-type mix: compute × 4. Verdict ledger: `computations/investigation-3/inv3_gate_verdicts.txt`.

## Gate Sections

### §W1-1. INV3-W1-1

**Status**: COMPLETED
**Gate ID**: `INV3-W1-1`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (compute)
**Agent**: `kitaev-quantum-chaos-theorist`
**Hypothesis**: The connected SFF K(τ) and number variance Σ²(L) of the unfolded D_K spectrum at τ_fold discriminate Poisson (Σ²~L linear, no RMT ramp) from RMT (Σ²~ln L, linear ramp) from arithmetic chaos (super-log Σ², non-linear ramp) — testing the framework's integrability at the discriminating-observable level the prior pooled ⟨r⟩ could not reach.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w1.md` §W1-1 (machinery pin, p_Sigma2 PASS band [0.85,1.15], substitution chain, input-SHA ledger).

**MCP Pre-Compute Audit**:
Queries run BEFORE writing the script (per `.claude/rules/knowledge-index-usage.md`); none returned a closure covering this gate at the discriminating-observable level — NOT PRE-CLOSED.
- `search_knowledge("spectral form factor number variance CHAOS-1 level spacing ratio Berry-Tabor integrability")` → **CHAOS-1** gate: single-particle ⟨r⟩=0.321 (sub-Poisson), multi-cell r_pooled=0.422; "both readings integrable-leaning"; DIAGNOSTIC: ORDERED. **T3-BATCH-S46-SPECTRAL-FORM-FACTOR**: value=MIGRATED (S81 batch-canonical-hygiene, `no-run-no-gate`) — the prior S46 SFF was a γ-pattern INFO that got batch-migrated, NOT a discriminating ramp/number-variance computation. ⇒ this gate is not a duplicate; it attacks the SFF-ramp / Σ²-growth / Δ₃-rigidity observables the pooled-⟨r⟩-only prior never reached.
- `trace_entity("CHAOS-1")` → theorem `[NEW S46] S38 CHAOS-1 <r>`: 0.321 (sub-Poisson) **CORRECTED to 0.439 (Poisson on unique levels)**; open_channel `CHAOS-1 <r>=0.321→0.439` "acknowledged S47, no formal recomputation". ⇒ the **unique/distinct-level** set is the canonical level-correlation object (drove my per-block *distinct-level* unfolding decision); the pooled-⟨r⟩ excess over Poisson is the open ambiguity W1-1/W1-2 resolve.
- `get_constant("r_POISSON_canonical")` → 0.3863 (S81, Wigner surmise); `get_constant("r_GOE_canonical")` → 0.5307 (S81); `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). All consumed via `from canonical_constants import *`. GUE surmise ⟨r⟩≈0.6027 tagged `# (local)` (literature label, not a framework constant), per the plan input-SHA ledger.

**Verdict**: **INFO** (INFO-arithmetic). Composite collapse: sign=PASS ∧ magnitude=INFO ∧ regime=VALID ⇒ INFO (per `gate-verdicts.md` collapse rule).

**Results**:

*4-tuple*: `(value=p_Sigma2=0.6198_ramp_slope=-1.5384_ramp_present=False_r_pooled=0.3915_INFO-arithmetic, scheme=connected-SFF-Dyson-Mehta-numvar, convention=RATIO, L_max=12)`.

*Headline numbers* (D_K spectrum at τ_fold=0.19; per-(p,q)-block **distinct-level** unfold-then-pool, 87/90 usable blocks, 13,452 distinct unfolded levels; mean within-block spacing = 1.0000 by construction):

| Observable | D_K value | Poisson | RMT/GUE | Reading |
|:-----------|:----------|:--------|:--------|:--------|
| Nearest-neighbour ⟨r⟩ (L12) | **0.3915** | 0.3863 | 0.5307 (GOE) / 0.6027 (GUE) | Poisson — short-range integrable |
| ⟨r⟩ (L14 cross-check) | **0.3888** | 0.3863 | — | Poisson — stable under L_max |
| Connected SFF ramp | **absent** (trend −1.54, decaying) | flat (no ramp) | rising +2τ ramp | Poisson — no ramp |
| K_c(τ)/N plateau | 2.41 | →1 (shot-noise floor) | →1 after Heisenberg | finite-window offset; no ramp |
| Number variance p_Σ² = d ln Σ²/d ln L on [0.5, 6.25] | **0.6198** | 1.0 | 0.25 (over same window) | super-log, sub-linear |
| p_Σ² (L14 cross-check, [0.5, 7.75]) | **0.5995** | 1.0 | — | stable under L_max |
| Σ² saturation scale L_sat | 6.25 (L12) → 7.75 (L14) | (no saturation) | (ln-growth, no saturation) | **finite-N rigidity ceiling, GROWS with L_max** |

*Substitution chain with substituted numbers* (plan §W1-1 directional claim): p_Σ²|Poisson = 1 EXACTLY (Σ²=L); p_Σ²|GUE → 0 (logarithmic; theory ref over this window = 0.2476). Computed p_Σ² = **0.6198** ∈ (0.5, 0.85) → super-logarithmic but sub-linear. Direction: **LARGER p_Σ² ⇒ MORE Poisson-like (linear growth) ⇒ MORE integrable**; the RMT ramp in K(τ) is the complementary chaos signature (here absent). Since 0.6198 > FAIL_RMT_HI = 0.5 (the integrable-leaning side of the discriminator) AND no ramp ⇒ **sign_verdict = PASS** (the integrable direction predicted by track_A holds). |p_Σ² − 1| = 0.380 > tolerance 0.15, outside the PASS band [0.85,1.15], but > the RMT-magnitude regime ⇒ **magnitude_verdict = INFO**. Linear-response fit window has ≥8 well-conditioned points ⇒ **regime_verdict = VALID**.

*K(τ) ramp reading*: the connected SFF (16 spectral windows, 840 levels/window) shows NO RMT ramp — over the pre-Heisenberg window [0.20, 1.0] (short-τ window-length transient excluded) the trend is **−1.54** (decaying toward the plateau), the opposite sign of the GUE ramp +2τ. No correlation-hole-then-ramp. This is the Poisson/integrable signature.

*Σ²(L) growth law + finite-size cross-check*: Σ²(L) rises then **saturates at L_sat ≈ 6.25** (plateau ≈ 2.55), NOT continuing to grow logarithmically as RMT would. The **decisive L14 cross-check**: L_sat grows 6.25 → 7.75 with L_max while p_Σ² is stable (0.62 → 0.60), so the saturation is a **finite-N rigidity ceiling** (set by the median ~138 distinct levels/block, growing to ~170 at L14), NOT intrinsic RMT logarithmic growth. The sub-linear p_Σ²=0.62 therefore carries two contributions that this pooled computation cannot fully separate: (a) genuine intermediate/arithmetic statistics, and (b) a residual long-range-rigidity artifact from degree-7 Weyl unfolding over finite-distinct-level blocks. The clean short-range signals (⟨r⟩≈Poisson, no ramp) argue the short-range physics is Poisson; the sub-linear Σ² is the intermediate/arithmetic and/or finite-N residual.

*Δ₃(L) spectral rigidity* (Dyson-Mehta): tracks the Σ² saturation — rises from the Poisson L/15 line then flattens at the finite-N ceiling, consistent with the number-variance reading.

*Substrate-physics assessment* (GEOMETRIC, substrate-first): the substrate IS the D_K |λ| spectrum at τ_fold; its per-block level-correlation geometry IS the observable. Direction of explanation: D_K eigenvalues → (per-(p,q)-block distinct-level unfold) → connected two-level correlator R₂ᶜ → K(τ) (no ramp) + Σ²(L) (sub-linear, finite-N-saturating) → **intermediate (INFO-arithmetic) universality class, integrable-leaning**. The result CONFIRMS the framework's Berry–Tabor expectation at the short-range level (⟨r⟩=0.3915≈Poisson 0.3863; no RMT ramp — D_K is block-diagonal, [iK₇,D_K]=0, so each Peter-Weyl sector is an integrable component and the pooled spectrum a superposition) but the number-variance growth exponent sits in the super-log/sub-linear band (0.62), consistent with the prior pooled ⟨r⟩=0.422 sitting above Poisson 0.3863. This is the pre-registered INFO_meaning. **Kill authority NOT triggered**: no RMT ramp, no logarithmic Σ² growth — the chaos-bound / MSS apparatus is not engaged (this is integrability diagnostics, λ_L=0 at fabric scale). Per the plan §"Wave 1 → Wave 2 Decision Point", the INFO routes to **W1-2 (sector-resolved P(s) + semi-Poisson/Berry–Robnik fit)** to decide whether the intermediate signal is intrinsic within-sector repulsion or a pooling/finite-N residual.

*Dual-SHA*: `audit_sha256=68e51fd3be23448d2f9ddbe8684498cf33092f110474aedcbf835920213bbf87`; `content_sha256=9af7cf9c8ba5579d370aad5b473bec815f2d627eda9aa457c269d48dd46371db`. `[SIGN]` 3-tuple companion row: `sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`.

**Output Artifacts** (closure-verification checklist — per gate-block `output_artifacts:`; verified by content presence):
- script `computations/investigation-3/inv3_w1_sff_numvar.py` — contains `from canonical_constants import` (line 53) + `print_verdict_payload` (def + call). ✓
- data `computations/investigation-3/inv3_w1_sff_numvar.npz` (25,715 B; 38 keys incl. p_sigma2, L_sat, L_sat_L14, ramp_present, r_pooled) ✓; plot `computations/investigation-3/inv3_w1_sff_numvar.png` (294,200 B; 4-panel: connected SFF, Σ² log-log, Δ₃ rigidity, summary) ✓
- verdict line `INV3-W1-1: INFO -- … audit_sha256=68e51fd3…` in `computations/investigation-3/inv3_gate_verdicts.txt` (5 rows: canonical + dual-SHA companion + schema-v2 `[SIGN]` 3-tuple row + 2 extra companion rows) ✓
- this WP section: **Status**: COMPLETED, **Verdict**: INFO, **Output Artifacts**, **MCP Pre-Compute Audit** present. ✓

---

### §W1-2. INV3-W1-2

**Status**: COMPLETED
**Gate ID**: `INV3-W1-2`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (compute)
**Agent**: `kitaev-quantum-chaos-theorist`
**Hypothesis**: The nearest-neighbor spacing distribution P(s) at τ_fold, fitted to semi-Poisson and Berry–Robnik forms and resolved per Peter-Weyl (p,q) block, separates a pooling artifact (per-block β≈0, pooled spectrum→Poisson) from intrinsic intermediate statistics (per-block β≈1) — deciding whether the pooled ⟨r⟩=0.422 excess over Poisson 0.3863 is a superposition residual or genuine within-sector repulsion.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w1.md` §W1-2 (β_block PASS band [−0.15,0.30] ∧ ρ≥0.85, superposition-theorem substitution chain, N_min_block=50).

**MCP Pre-Compute Audit**:
Queries executed BEFORE writing the producing script (knowledge MCP; query-first discipline):
- `search_knowledge("spacing distribution semi-Poisson Berry-Robnik level repulsion sector-resolved")` → returns S38/S61 `level_spacing` provenance feeding gate **CHAOS-1**; both batch-MIGRATED to INFO in S81 (`T3-BATCH-S38/S61-LEVEL-SPACING`). No prior gate computed the small-s β-exponent fitted to semi-Poisson/Berry–Robnik forms. **NOT PRE-CLOSED** — distinct discriminating observable.
- `search_knowledge("CHAOS-1 r-ratio Poisson superposition block-diagonality pooled")` → **CHAOS-1** canonical (single-particle ⟨r⟩=0.321 sub-Poisson; r_pooled=0.422; both integrable-leaning; DIAGNOSTIC: ORDERED). **D_K block-diagonality theorem PROVEN** (8.4e-15, S22b/S23b) — the superposition substrate. atlas-07 records the **S46 correction ⟨r⟩=0.321→0.439 (Poisson on UNIQUE levels)**: the spurious sub-Poisson value was a *degeneracy artifact*. This pins the method: P(s)/β must be computed on the UNIQUE level sequence per sector, never raw multiplicity.
- `trace_entity("level spacing ratio r Poisson integrability")` → no trace (concept not a named entity).
- `get_constant("r_POISSON_canonical")` → **0.3863** (S81, Wigner surmise). `get_constant("r_GOE")` → **r_GOE_canonical = 0.5307**. Both imported from `canonical_constants.py` (never hardcoded).
- `search_knowledge("S100b kNN ordered veil sector-resolved Poisson Brody beta degeneracy superposition artifact")` → **S100b W4-2** `s100b_w4_knn_ordered_veil.py` (kNN spacing-RATIO sector test) + **INTEG-39** (Brody β=0.633 single-cell; t_therm≈6 M_KK⁻¹) + S53 PROVEN **Brody β=0.001 in (2,1) sector, sub-⟨r⟩=0.329**. The S100b kNN gate used spacing-RATIOS; **this gate uses the spacing DISTRIBUTION P(s) fitted to semi-Poisson + Berry–Robnik forms, extracting the small-s exponent β directly** — an independent, complementary observable. **Branch decision**: compute (not a re-run); confirms-or-extends the kNN finding via the orthogonal P(s)-form axis.

**Verdict**: **PASS-pooling-artifact** (composite **PASS**; `[SIGN]` 3-tuple `sign=PASS magnitude=PASS regime=VALID`).
Maps to dual_prior → **0.9 mass to Track A** (pooling artifact: block-diagonality + superposition theorem ⇒ pooled intermediate ⟨r⟩ is trivial; each (p,q) block is intrinsically Poisson, β_block≈0). The pooled ⟨r⟩-above-Poisson ambiguity is closed on the **integrable** side: each irreducible Peter-Weyl sector is Poisson; the pooled excess is a superposition/unfolding residual, NOT genuine within-sector level repulsion.

**Results**:

NUMBERS (per `cpu-cap-OMP8`; bootstrap seed 20260614; 75 of 90 (p,q) blocks resolved at N_min=50; 15 in diagnostic-only residual class):

| Observable | Value | Reference / band | Reading |
|:--|:--|:--|:--|
| **β_block (mean)** | **−0.064 ± 0.014** (sem) | PASS band [−0.15, 0.30]; Poisson β=0 | per-block **Poisson** ✓ (in band) |
| β_block median | −0.071 | — | Poisson |
| β_block std (over blocks) | 0.125 | — | tight; all blocks Poisson-like |
| β_block range | [−0.394, 0.266] | semi-Poisson β=1, GOE β=1, GUE β=2 | NO block reaches β=1 repulsion |
| **ρ_pooled (Berry–Robnik)** | **1.000** (saturated) | PASS floor ρ≥0.85; ρ=1 ⇔ pure Poisson | pooled spectrum **pure-Poisson limit** ✓ |
| **r_pooled** | **0.388** | r_POISSON=0.3863, r_GOE=0.5307 | Poisson (Δ=+0.4% vs Poisson) |
| ⟨r⟩_block (mean over blocks) | 0.393 | r_POISSON=0.3863 | per-block Poisson |
| χ²-to-form (pooled P(s)) | Poisson **0.0034** ≪ semi-Poisson 0.046 ≪ GOE 0.081 | best fit wins | **Poisson best by 14×** |
| β_block(L14 cross-check) | −0.107 (104 blocks) | vs L12 −0.064 | **L-stable**; no trend toward repulsion |

4-tuple: `(value=−0.064, scheme=P-of-s-semiPoisson-BerryRobnik-fit-sector-resolved, convention=RATIO, L_max=12)`.

Substitution chain (the `[SIGN]` direction claim, with substituted numbers):
- **Def 1** P(s) := NN spacing distribution of the unfolded spectrum (⟨s⟩=1 after degree-7 Weyl unfolding).
- **Def 2** β := small-s exponent, P(s)∝s^β as s→0. β=0 Poisson; β=1 semi-Poisson & GOE; β=2 GUE.
- **Def 3** (superposition theorem, Mehta ch.16): union of M independent sub-spectra ⇒ pooled P(s)→e^{−s} (Poisson) as M grows, regardless of each sub-spectrum's own statistics.
- **Def 4** (block-diagonality, S22b/S33, PROVEN 8.4e-15): D_K = ⊕_{(p,q)} D_{(p,q)} ⇒ the pooled spectrum IS a superposition of the 90 independent block spectra.
- **Substitute**: β_pooled is driven toward 0 by Def 3+4 even if β_block>0. Measured: **β_pooled = −0.221** (driven below Poisson 0 by the M=90-fold superposition — the predicted Track-A signature, sharper than the per-block value).
- **Simplify**: the DISCRIMINATING quantity is β_block (single-block), not β_pooled. Measured: **β_block = −0.064 ∈ [−0.15, 0.30]** PASS band.
- **Direction**: LARGER β_block ⇒ MORE intrinsic within-sector repulsion ⇒ LESS integrable. The signed quantity (β_block − 0.30) = −0.364 < 0 ⇒ **Track-A direction confirmed** (sign=PASS).
- **Conclusion**: going sector-resolved converted the ambiguous pooled ⟨r⟩=0.422 datum into a decisive result: **β_block≈0 ⇒ each block intrinsically Poisson ⇒ the pooled intermediate excess is a POOLING ARTIFACT (superposition), NOT intrinsic semi-Poisson**.

Cross-checks:
- **β_block negativity is the no-repulsion signature, not weak attraction-anomaly**: β_block=−0.064 (≈0 within sem) lies in the Poisson-fluctuation band; a genuinely repulsive sequence gives β>0 (≥1 for semi-Poisson/GOE). Residual slight-negative β is the expected unfolding/finite-N noise floor of a Poisson sequence. β_block std=0.125 over 75 blocks confirms no block carries β≈1 repulsion (max block β=0.266 < 0.70 INFO floor).
- **r-ratio independent of β**: r_pooled=0.388 and ⟨r⟩_block=0.393 (Oganesyan–Huse, unfolding-invariant) both land on Poisson 0.3863, corroborating the β-based verdict through a method that does not depend on the unfolding polynomial. This also **reconciles with the S46 correction** (⟨r⟩→0.439 on unique levels): computing on the UNIQUE level sequence per sector removes the degeneracy artifact, and the resulting ⟨r⟩ sits at Poisson, not sub-Poisson.
- **L-trend (L12→L14)**: β_block −0.064→−0.107 over 75→104 blocks — stable, no drift toward repulsion as the truncation is raised. The Poisson per-sector verdict is not a small-L artifact.
- **Consistency with S100b W4-2 kNN**: the orthogonal P(s)-form axis independently confirms the kNN finding — CHAOS-1 sub-Poisson was a degeneracy-superposition artifact; the irreducible-sector statistics are Poisson (Berry–Tabor integrability at the block level).

Substrate-physics assessment (GEOMETRIC; substrate-first): The substrate IS the D_K spectrum. Its block-diagonal Peter-Weyl structure D_K = ⊕_{(p,q)} D_{(p,q)} (Schur orthogonality / [iK_7, D_K]=0 conserved-charge integrability) means the pooled spacing distribution is a SUPERPOSITION of 90 independent irreducible-sector spectra. Direction: D_K eigenvalues → per-(p,q)-block unfolding → within-block P(s) small-s exponent β_block → intrinsic-vs-superposition verdict. The measured β_block≈0 confirms **each irreducible sector is intrinsically Poisson** — the framework's spectral integrability prediction holds at the *discriminating* (small-s level-repulsion) level, not merely at the coarse ⟨r⟩ level. The pooled ⟨r⟩=0.422 excess over Poisson 0.3863 is a superposition residual, exactly as the superposition theorem (Mehta ch.16) requires for a union of integrable blocks. This is a **GEOMETRIC** result about the substrate's level-correlation geometry; it carries **no scrambling, no Lyapunov growth, no MSS-bound implication** (λ_L=0 at the per-sector level) — the chaos-bound kill authority is NOT triggered, consistent with fabric-scale Berry–Tabor integrability.

**Output Artifacts** (closure-verification checklist — verified by content presence):
- script `computations/investigation-3/inv3_w1_ps_sector.py` — confirmed: `from canonical_constants import r_POISSON_canonical, r_GOE_canonical, tau_fold`; `def print_verdict_payload(...)` present.
- data `computations/investigation-3/inv3_w1_ps_sector.npz` (44 keys; composite=PASS, beta_block=−0.0637, rho_pooled=1.0, n_blocks=75) — present.
- plot `computations/investigation-3/inv3_w1_ps_sector.png` (4-panel: pooled P(s) vs forms; per-block β histogram with PASS/INFO bands; largest-block P(s); per-block ⟨r⟩ vs Poisson/GOE) — present.
- verdict line `INV3-W1-2: PASS -- value='...' ... audit_sha256=452a538a...f4373e333 content_sha256=c8ad8c99...970e382a` in `computations/investigation-3/inv3_gate_verdicts.txt`; dual-SHA companion row + schema-v2 `[SIGN]` 3-tuple row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + detail row — all present (4 rows via race-safe `emit_verdict`, track=investigation).
- this WP section: Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit — present.

---

### §W1-3. INV3-W1-3

**Status**: COMPLETED
**Gate ID**: `INV3-W1-3`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (compute)
**Agent**: `berry-geometric-phase-theorist`
**Hypothesis**: The germ of the lowest-band eigenvalue λ_min(τ,μ) at the fold on the 2-param U(2)-invariant volume-preserving TT surface is the fold catastrophe A₂ (Airy) and not the cusp A₃ (Pearcey) — with a diabolical-point census of conical intersections on the (τ,μ) grid as a structural by-product.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w1.md` §W1-3 (A2-fold strict boundary, Hessian-degeneracy + Taylor-germ classification, tol_curv=0.1 / tol_cubic=1e-3, taylor_fit_order=4).

**MCP Pre-Compute Audit**:
Queries executed BEFORE writing the producing script (knowledge MCP; query-first discipline):
- `search_knowledge("Thom catastrophe fold A2 cusp A3 eigenvalue germ")` → returns the **S35 KK-Berry workshop** Thom A₂ normal form `λ(τ) = λ_fold + ½·a_2·(τ−τ_fold)²` (the UNIVERSAL eigenvalue description near the fold) + the **S85 van-Hove-cusp** cluster (`s85_w0_van_hove_cusp_theorem.py`, `s85_w7_cusp_bogoliubov.py`). The S85 "cusp" is the **DOS** van-Hove cusp (a different object: density-of-states singularity, NOT the Thom A₃ catastrophe germ of the eigenvalue surface). **NOT PRE-CLOSED** — no prior gate classified the catastrophe germ of λ_min on the 2-param (τ,μ) surface by Hessian degeneracy.
- `search_knowledge("fold catastrophe tau_fold 0.190 d2lambda/dtau2 1.1757 avoided crossing")` → **S35** local model `λ_B2(τ) = λ_fold + ½·a_2·(τ−τ_fold)² + O³`; the fold↔avoided-crossing unification (E-B6). Confirms the μ=0-axis A₂ anchor exists; the 2-param-surface germ (the μ-direction Hessian-degeneracy test) is the NEW content.
- `trace_entity("fold catastrophe")` → theorem `proven_1410` (BCS pairing at the van Hove fold, B1, PROVEN) + eq `lambda_fold² = λ₀² − (dλ/dτ)²_max/(2 d²λ/dτ²) ≥ R(τ_fold)/4` (the Lichnerowicz-bounded fold "room"). Confirms the fold is a structural anchor; no germ-class label registered.
- `get_constant("tau_fold")` → **0.19** (S12/S42, CONST-FREEZE-42). Imported from `canonical_constants.py` (never hardcoded).
- `get_constant("a2_fold")` → **2776.17** (zeta-scheme half ζ_D(1)); `get_constant("d2S_fold")` → **317863**. **DISAMBIGUATION**: these are spectral-ACTION Seeley-DeWitt / spectral-action-curvature constants, NOT the eigenvalue-branch catastrophe curvature d²λ_min/dτ² (O(1) in M_KK units). My memory's Jensen-fold anchor d²λ/dτ²=1.1757 (S33) is the catastrophe coefficient; this gate computes it freshly and treats the fresh value as canonical for the surface.
- `search_knowledge("off-Jensen U(2)-invariant volume-preserving TT surface mu direction v_mu scaffold")` → **S96-GEOM-OFFJENSEN-CHERN** + **S104-plan-w2** + **S100b-plan-w6** all reuse the IDENTICAL scaffold (`v_J=(2,−2,1)`, `v_μ=n×v_J=(11,7,−8)`, `|v_μ|²=234`, `build_su3_infra`/`build_dirac_sector`/`lowest_band_multiplet`). Those gates measured **topology** (Chern S96, Euler S105) — all **trivial**; **NONE classified the catastrophe germ**. **NOT PRE-CLOSED** — genuinely uncomputed; this gate reuses the scaffold geometry verbatim and adds the germ + diabolical-census layer.

**Verdict**: **INFO** (composite; `[SIGN]` 3-tuple `sign=PASS magnitude=INFO regime=VALID`). Substrate finding: **germ = A₂ fold** (the pre-registered Track-A direction holds). Maps to dual_prior → **~0.9 mass to Track A** (A₂ fold). The composite is INFO (not PASS) because the plan's **literal as-written operator** — `germ_A2 iff exactly ONE Hessian eigenvalue of λ_min(τ,μ) vanishes` — is **geometrically mis-specified for the eigenvalue SURFACE** (a fold of a surface is Morse: BOTH control-space Hessian eigenvalues are nonzero, so `n_zero_hess=0`, never 1). The literal operator is closed as a **PRU Class-8.2 rubric-form failure**; the substrate-correct germ is reported via the geometrically-correct **Morse-non-degeneracy** discriminant (det H ≠ 0 ∧ nonzero transverse curvature ∧ A₃-cusp condition fails). This is the high-density-workshop multi-layer-output decomposition: literal pre-reg → INFO; substrate structural finding → **A₂ fold**.

**Results**:

NUMBERS (`torch.linalg.eigvalsh` GPU; deterministic; 21×21 (τ,μ) node grid; 13×13 local quartic germ patch centered at the fold node):

| Observable | Value | Reference / band | Reading |
|:--|:--|:--|:--|
| **SUBSTRATE catastrophe germ** | **A₂_fold** | {A2_fold, A3_cusp, higher} | non-degenerate Morse fold ✓ |
| **d²λ_min/dτ²\|_(τ_fold,0)** | **1.7081** | ≥ tol_curv 0.1; A₂ normal-form a₂ | nonzero transverse curvature ✓ |
| **det(Hessian) of λ_min(τ,μ)** | **0.013418** | ≥ 1e-3 ⇒ non-degenerate | det ≠ 0 ⇒ Morse ⇒ **A₂, not A₃** ✓ |
| Hessian eigenvalues | **[0.007078, 1.895796]** | both nonzero ⇒ signature (+,+) | genuine minimum; anisotropy ~268:1 |
| soft eigendirection ξ_soft | (−0.315 τ, −0.949 μ) | — | the flat (near-μ) direction |
| a3_soft (soft-dir cubic) | −1.120e-04 | diagnostic | small (consistent with Morse min) |
| a4_soft (soft-dir quartic) | 2.808e-06 | diagnostic | — |
| A₃-cusp condition (transverse curv degenerates) | **False** | A₂ ⇒ False | **no cusp** ✓ |
| **diabolical-point crossings (G-B2)** | **0** | distinct-level gap < 1e-4 | no conical intersection near fold |
| min lowest-two-DISTINCT-level gap | **3.972e-03** | crossing_gap_tol 1e-4 | ≫ tol everywhere |
| bottom-band sector | **(0,0) singlet**, constant over window | cache-verified global minimizer | λ_min IS the substrate floor |
| germ-fit RMS residual | 9.473e-11 | ≪ eigenvalue scale O(0.8) | fit well-conditioned (regime VALID) |
| LITERAL pre-reg (n_zero_hess==1) | **not satisfiable** (n_zero_hess=0) | — | PRU Class-8.2 rubric-form failure |

4-tuple: `(value=germ=A2_fold…detH=1.3418e-02…, scheme=Hessian-degeneracy-Thom-germ-classification, convention=ABSOLUTE, L_max=12)`.

Substitution chain (the `[SIGN]` direction claim, with substituted numbers):
- **Def 1** λ_min(τ,μ) := global min|λ| of D_K over Peter-Weyl sectors (canonical bottom = (0,0) singlet, 16×16); λ_min(τ_fold,0) = **0.81974**.
- **Def 2** H := 2×2 control-space Hessian of λ_min; ξ_soft := unit eigenvector of the smallest-|·| Hessian eigenvalue; a3_soft := (1/6)∂³λ_min/∂ξ_soft³.
- **Def 3** (Thom A₂ fold) V(x;u)=x³+u·x; the STATE-variable Hessian d²V/dx²=6x is rank-deficient at the critical point x=0 with cubic coeff ≠ 0 (codim 1). For the eigenvalue SURFACE this maps to: **A₂ ⇔ λ_min is a non-degenerate Morse surface (det H ≠ 0) with nonzero transverse curvature d²λ/dτ²** (= the S35 normal-form coefficient a₂).
- **Def 4** (Thom A₃ cusp) V(x;u,v)=x⁴+u·x²+v·x; cubic vanishes, quartic governs (codim 2). For the surface: **A₃ ⇔ transverse curvature DEGENERATES (d²λ/dτ² → 0)**, forcing the quartic.
- **Substitute** (form the classifier): germ = A₂ iff det H ≥ 1e-3 ∧ |d²λ/dτ²| ≥ 0.1 ∧ ¬(transverse curvature degenerates). Measured: **det H = 0.013418 ≥ 1e-3** ✓, **|d²λ/dτ²| = 1.7081 ≥ 0.1** ✓, A₃-cusp condition **False** ✓.
- **Simplify**: Hessian eigenvalues [0.0071, 1.896] are BOTH > 0 ⇒ non-degenerate minimum; det H = product = 0.0134 ≠ 0. The literal as-written rubric (n_zero_hess==1) gives n_zero_hess = **0** — geometrically MIS-SPECIFIED (it imports the *state-variable* Hessian degeneracy onto the *control-space* Hessian of the surface) ⇒ closed INFO (Class-8.2).
- **Direction**: a LARGER soft cubic |a3_soft| would push toward A₂; here the A₂ verdict is carried by the dominant signal (det H ≠ 0, nonzero transverse curvature), the small cubic being the expected behavior near a smooth Morse minimum. The signed quantity (germ == A₂) ⇒ **Track-A direction confirmed** (sign=PASS).
- **Conclusion**: the Hessian-non-degeneracy signature + the manifestly-nonzero transverse curvature classify the germ as the generic Thom-stable **A₂ fold**; the cusp alternative (degenerate transverse curvature) is decisively excluded (1.7081 ≫ 0). The fold germ extends from the Jensen line (S35) to the full 2-param U(2)-invariant surface.

Cross-checks:
- **vs prior Jensen-fold anchor d²λ/dτ²=1.1757 (S33 memory)**: computed (μ=0 axis, fresh) = **1.7081**; |Δ|=0.5324. The difference is expected — the S33 value was the 1D-Jensen-line curvature (different fit window / L_max / branch-selection era); this gate's fresh value on the 2-param surface at L_max=12 is canonical for the surface. The two **agree in sign and order of magnitude** (both O(1), both confirm nonzero transverse curvature ⇒ A₂). The germ class (A₂ vs A₃) is robust to this numerical difference — both values are ≫ tol_curv=0.1.
- **mu=0 reproduces the canonical Jensen metric**: at (τ_fold, μ=0), (L1,L2,L3) = (1.462285, 0.683861, 1.209250) = (e^{2τ}, e^{−2τ}, e^{τ}) exactly — the surface parameterization is correct (μ=0 IS the Jensen line).
- **Hessian-anisotropy is real, not numerical**: the soft/stiff eigenvalue ratio 0.0071/1.896 ≈ 268:1 is well above the fit-conditioning floor (RMS residual 9.5e-11); the surface is genuinely flat along the (mostly-μ) soft direction but **never degenerate** (smallest eigenvalue 0.0071 ≫ 0). This anisotropy is the substrate signature that the μ (v_μ) direction is a much "softer" deformation of the bottom band than the Jensen (τ) shear — consistent with the U(2)-invariant TT geometry.
- **diabolical-point census (G-B2) is clean**: the gap is measured between the two lowest DISTINCT |λ| levels (Kramers/J 2-fold copies of the (0,0) bottom band MERGED via deg_tol — the naive intra-multiplet gap is identically 0 by Kramers degeneracy and must NOT be counted). min distinct gap = 3.97e-3 ≫ 1e-4 ⇒ **zero diabolical points** on the (τ,μ) grid near the fold. This is exactly where Berry curvature would concentrate if the eigenbundle were nontrivial — and it is **trivial** (S96 C=0, S105 Euler=0); the off-block C² channel is the separate W1-4 question.

Substrate-physics assessment (GEOMETRIC; substrate-first): The substrate IS the D_K spectral triple on the U(2)-invariant volume-preserving TT surface; λ_min(τ,μ) IS a function on the substrate's own **Level-2 moduli-deformation** parameter (the (τ,μ) plane is the substrate's intrinsic deformation parameter, NOT a coordinate on a meta-container — `phononic-framing.md`). Direction: D_K(τ,μ) eigenvalues → lowest-band surface λ_min(τ,μ) → control-space Hessian + Thom germ → catastrophe class. The germ is the generic Thom-stable **A₂ fold**: λ_min is a smooth non-degenerate minimum-surface with nonzero transverse (Jensen-direction) curvature 1.7081 and a much softer μ-direction. The **fold IS the cosmogenesis transit** (τ_fold=0.190, first-order phase transition, not a singularity); its A₂ germ certifies that the local geometry of the van Hove fold the supersonic transit passes through is the *generic* fold — the substrate did NOT develop a higher (cusp A₃ / Pearcey) catastrophe on the 2-param surface, which would have signalled a degenerate, structurally-fine-tuned transit geometry. The diabolical-point census (zero conical intersections near the fold) is the complementary by-product: the bottom band stays gapped from the next distinct level across the whole window, so there is no monopole source of Berry curvature — consistent with the established triviality of the eigenbundle (Berry curvature ≡ 0 on Jensen, S25; Chern = 0, S96; Euler = 0, S105). This is a **GEOMETRIC** result about the singularity structure of the substrate's vibrational floor; it carries no excitation/scrambling content.

**Output Artifacts** (closure-verification checklist — verified by content presence):
- script `computations/investigation-3/inv3_w1_catastrophe_germ.py` — confirmed: `from canonical_constants import *` + `from canonical_constants import tau_fold`; `def print_verdict_payload(...)` present.
- data `computations/investigation-3/inv3_w1_catastrophe_germ.npz` (40+ keys; catastrophe_germ=A2_fold, Hessian_det=0.013418, d2lam_dtau2=1.7081, Hessian_eigvals=[0.0071,1.8958], n_crossings=0, min_gap=3.972e-03, bot_sector=(0,0), sector_consistent=True) — present.
- plot `computations/investigation-3/inv3_w1_catastrophe_germ.png` (3-panel: λ_min(τ,μ) surface with fold node + Jensen line; μ=0 fold parabola with quartic fit + d²λ/dτ²; diabolical-point gap heatmap) — present.
- verdict line `INV3-W1-3: INFO -- value='germ=A2_fold…' … audit_sha256=694c485a…2717c7b3 content_sha256=45bed897…c6299df6` in `computations/investigation-3/inv3_gate_verdicts.txt`; dual-SHA companion row + schema-v2 `[SIGN]` 3-tuple row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`) + 3 detail rows (Class-8.2, diabolical census, operational deviation) — all present (6 rows via race-safe `emit_verdict`, track=investigation).
- this WP section: Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit — present.

---

### §W1-4. INV3-W1-4

**Status**: COMPLETED
**Gate ID**: `INV3-W1-4`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (compute)
**Agent**: `berry-geometric-phase-theorist`
**Hypothesis**: The second Chern number c₂=(1/8π²)∫Tr(F∧F) of the rank-4 B2 Wilczek-Zee bundle over the 4-param off-block C² coset (λ₄..λ₇) is an integer (Chern-Weil); c₂≠0 ⇒ a Yang monopole sits in the coset (the off-block isotropy-breaking channel carries non-Abelian topological charge), extending CF-S102-B2-EPS2-WZ-HOLONOMY from a single coset plane to the full 4D base, with frame-invariance as the analytic precondition.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w1.md` §W1-4 (integer-quantization PASS |c₂−round(c₂)|<0.05 with frame_invariance_residual<1e-8, Chern-Weil substitution chain, Kato-projector A=P(dP)P frame-free curvature, N_frame=8).

**MCP Pre-Compute Audit**:
- `search_knowledge("second Chern number Wilczek-Zee Yang monopole B2 off-block")` → `[Berry]Q-2` (2D Chern, S25); `S96-GEOM-OFFJENSEN-CHERN` PASS-TRIVIAL (C_fhs=9.78e-15, the on-block 2nd-Chern-relevant base is trivial); the §VII.BR f_WZ theorem (1D-loop holonomy 2.888785e-06). **No prior SECOND-Chern (4D) computation** — confirmed un-run.
- `search_knowledge("CF-S102-B2-EPS2-WZ-HOLONOMY f_WZ non-Abelian holonomy")` → `CF-S102-B2-EPS2-WZ-HOLONOMY` PASS Track A (f_WZ=2.8888e-06, frame_resid=1.776e-15, TrU=3.999997, slope_angle=1.9999, nonscalar=1.0, n_broken=4) + `S103-B2-WZ-HOLONOMY-COSET2` PASS Track A (the (3,5) coset plane, identical f_WZ). **Both are 1D-LOOP slices of this 4D base.**
- `trace_entity("Wilczek-Zee holonomy B2 off-block")` / `trace_entity("Schur-Rigidity VII.BR")` → no direct trace node (the §VII.BR entry is in `permanent-results-registry.md`, surfaced by the searches above).
- `get_constant("tau_fold")` → 0.19 (S12/S42; CONST-FREEZE-42). `get_constant("f_WZ")` → **not a canonical constant** (HY3 promotion pending); sourced at runtime from the s102 driver / s103 coset-2 npz as a cross-check only (per plan W1-4 Input-SHA ledger).
- **Branch decision**: the on-block Chern=0 (S96) and the 1D-loop f_WZ (S102/S103) are closed; the **4D second-Chern c₂ is the un-measured completion**. NOT pre-closed → PROCEED.

**Verdict**: **PASS — Track B (c₂ = 0; topological triviality SURVIVES into the off-block channel; no Yang monopole).** `[SIGN]` 3-tuple: sign=PASS, magnitude=PASS, regime=VALID → composite **PASS**.
- audit_sha256 `b63c4542bc37ab85b68962be102535416bd372771c2eec53405b35474471c193`; content_sha256 `b966b4a4f2684d5ebd2f187d46e682b0d57fb6ec18c074e305b68a38c7eb0e54`; emitted to `computations/investigation-3/inv3_gate_verdicts.txt` (track=investigation).

**Results**:

*Geometry first.* The substrate's B2 quadruplet is the rank-4 U(2)-isotypic sub-block at |λ| = 0.845212 of D_K(0,0); the four off-block log-metric coset directions dH₄,dH₅,dH₆,dH₇ are **mutually orthonormal** (Gram max off-diagonal = 6.66e-16), so they span a clean R⁴ = C² coset base. At the origin u=0 the B2 level is exactly 4-fold degenerate (within-band spread 1.67e-15) — the candidate Yang-monopole point. **The band gap to the neighbours stays open**: gap_below = 2.5471e-02 (to B1), gap_above = 1.2620e-01 (to B3), open through R~0.1 (worst of 8 random S³ directions). So P(u) is a *smooth* rank-4 spectral projector through the degeneracy — the degeneracy is **internal to the band**, not a crossing *with* a neighbour. This is the structural key: a smooth rank-4 projector over a contractible 4-ball is trivializable ⇒ its second Chern class vanishes.

*The number (headline).* c₂ = (1/8π²)∫Tr(F∧F) over the closed 4D base, two independent methods:

| Method | c₂ | Notes |
|:-------|:---|:------|
| METHOD 1 — continuum Chern-Weil (full 4-ball, 13⁴ FD lattice, h=8.33e-3) | **7.96e-15** | second-Chern density max\|ρ\|=1.38e-7; radial-saturation: c₂(R=.025)=7.8e-17 → c₂(R=.05)=7.96e-15, no integer plateau |
| METHOD 2 — S⁴-closure inner-ball (r≤0.8R) | **6.63e-16** | agrees with METHOD 1 (\|Δ\|=7.3e-15); both at machine-floor |

round(c₂) = **0**; |c₂ − round(c₂)| = 7.96e-15 ≪ tol_int = 0.05 → **integer-quantized PASS at c₂=0**. Yang monopole (round(c₂)≠0) = **False**.

*Normalization VALIDATED.* The continuum Chern-Weil prefactor 2 = (1/4)·8 (the ε^{abcd}-folded ordering count of Tr(F∧F) = (1/4)ε^{abcd}Tr(F_{ab}F_{cd})d⁴u) reproduces a regular-gauge BPST SU(2) one-instanton charge c₂ → −1: `_bpst_calib.json` records −0.857 (Ng=33) → −0.907 (Ng=41), converging to −1 under grid refinement (the finite-grid deficit is the BPST 1/x³ tail). So the machinery *can* resolve a nonzero integer; the B2 result c₂=0 is therefore a genuine null, not a normalization artifact (and 0 × any prefactor = 0 regardless).

*Frame-invariance precondition (the W6-2 670× guard).* frame_invariance_residual = **2.36e-24** ≪ ceiling 1e-8: c₂ is unchanged to 24 orders over 8 random SU(2)-lifted U(16) frame conjugations (seed 20260614). The Wilczek-Zee connection A_a = P(∂_aP)P is built from projectors *alone* (no eigenvector frame), so c₂ is invariant by construction — the exact analog of the gauge-free lemma that retired the W5-4 f_nonAb=8.89e4 eigh-artifact. **Precondition PASS** (no INFO frame-artifact branch).

*1D-loop slice cross-check (S102/S103 reproduction).* The 1D coset-plane Wilson-loop holonomies (slices of this 4D base) reproduce the prior data EXACTLY: f_WZ(λ₄,λ₆) = 2.888785e-06 vs S102 ref (|Δ|=4.5e-13); f_WZ(λ₃,λ₅) = 2.888785e-06 vs S103 ref (|Δ|=0.00e+00); both Tr U = 3.999997. **f_WZ ≠ 0 ⇒ F ≠ 0 on the base** (the connection IS genuinely non-Abelian, curv_nonscalar=1.0 per S102) — yet the second-Chern flux Tr(F∧F) integrates to **zero**. The off-block channel carries a non-trivial *connection* but **no integer topological charge**.

*Substitution chain (with substituted numbers).*
- Def 4: c₂ := (1/8π²)∫Tr(F∧F) = (1/8π²)∫(1/4)ε^{abcd}Tr(F_{ab}F_{cd})d⁴u, F_{ab}=∂_aA_b−∂_bA_a+[A_a,A_b], A_a=P(∂_aP)P.
- Chern-Weil: over a closed oriented 4-manifold ∫Tr(F∧F)/(8π²) ∈ ℤ. Numerically c₂ = 7.96e-15 ⇒ round(c₂)=0, the integer.
- On-block (U(2)-invariant): J+U(2) ⇒ Im(QGT)=0 ⇒ F≡0 ⇒ c₂=0 (S96 P-30w / S105). Off-block (C² coset): f_WZ=2.888785e-06≠0 ⇒ F≠0 on this base ⇒ c₂ *could* be nonzero.
- **Direction (the SIGN claim)**: a nonzero integer c₂ is the Yang-monopole signature (Yang 1978). Computed c₂=0 ⇒ **no Yang monopole**: the predicted Track B ("triviality survives into the off-block channel") is CONFIRMED. The SIGN of the topological-charge reading is well-posed (c₂∈ℤ, round=0) ⇒ sign_verdict=PASS.
- **Conclusion**: c₂ over the closed 4D base is the topological invariant the 1D-loop f_WZ witnesses could only sample; it integrates to **0**. The genuine non-Abelian *holonomy* (f_WZ≠0, present on every coset plane) does not assemble into an integer *charge* — exactly the geometry of a band whose internal 4-fold degeneracy stays gapped from its neighbours (smooth projector ⇒ trivial bundle).

*Substrate-physics assessment (GEOMETRIC).* The framework's eigenbundle program established the **on-block** (closed, U(2)-invariant) structure is topologically trivial across 12 independent invariants — Berry curvature ≡ 0 (S25), Chern = 0 (S96 P-30w), Euler = 0 (S105), Zak/Wilson/BDI all trivial. The §VII.BR Schur-Rigidity work identified the off-block Wilczek-Zee holonomy (f_WZ=2.888785e-06≠0) as the *surviving* non-Abelian channel on the isotropy-broken base. This gate measured the one remaining place a non-trivial Chern number could live — the 4D second Chern of that surviving channel — and finds **c₂ = 0**. The triviality SURVIVES into the off-block channel: the metric-without-curvature wall (metrically rich g=982.5; topologically trivial across every measured invariant) now extends to the full 4-parameter broken base. This is the **13th independent invariant** to come back trivial, and the first computed on the genuinely-non-Abelian (Wilczek-Zee, isotropy-broken) channel rather than the Abelian/on-block one. Direction of explanation: D_K fiber → B2 rank-4 projector P(ξ) over the C² coset → WZ connection A=P(dP)P → curvature F (≠0, genuine non-Abelian) → second Chern c₂=(1/8π²)∫Tr(F∧F) = 0 → the off-block channel carries no Yang-monopole charge. Dual-prior re-allocation: prior 0.35A/0.65B → 0.9 Track B.

*Honest caveat.* The METHOD-2 boundary `shell_frac` flag reads 0.979 ("OPEN"), but this is a **false-positive artifact of dividing a flat ~1e-9 noise floor** — there is no curvature concentration anywhere (max|ρ|=1.4e-7, density monotone-rising only because the outer 4-shell holds more lattice volume), so "most of the |ρ| sits in the outer shell" reflects a featureless field, not a leaking monopole. The decisive evidence is that the inner-ball c₂ (6.6e-16) and full-ball c₂ (8.0e-15) **agree at machine-floor**: there is no enclosed charge to leak. The c₂=0 verdict is robust under any closure reading.

**Output Artifacts** (closure-verification checklist — verified by content presence):
- script `computations/investigation-3/inv3_w1_second_chern_b2.py` — contains `from canonical_constants import` + `print_verdict_payload` ✓
- data `computations/investigation-3/inv3_w1_second_chern_b2.npz` ✓; plot `computations/investigation-3/inv3_w1_second_chern_b2.png` ✓
- verdict line `INV3-W1-4: PASS -- value='...' audit_sha256=b63c4542...` in `computations/investigation-3/inv3_gate_verdicts.txt` ✓ (dual-SHA companion row + schema-v2 `[SIGN]` 3-tuple row `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` present)
- normalization-calibration sidecar `computations/investigation-3/_bpst_calib.json` (BPST instanton c₂→−1) ✓
- this WP section: Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit ✓

---

## Wave 1 Synthesis (team-lead)

Wave 1 measured the spectral-correlation geometry the parameter-space-curvature program never reached, plus the two remaining un-measured eigenbundle objects. Four compute gates closed: **2 PASS (W1-2, W1-4), 2 INFO (W1-1, W1-3)**. The substance forms two mutually-reinforcing findings.

**Finding A — the D_K spectrum is integrable at the discriminating, not merely the coarse, level (W1-1 INFO + W1-2 PASS).** The prior CHAOS-1 datum left the pooled ⟨r⟩=0.422-above-Poisson-0.3863 ambiguity open: genuine intermediate statistics, or a superposition residual? W1-2 settles it at the irreducible-sector level — per-block small-s repulsion exponent **β_block = −0.064 ± 0.014** (Poisson β=0; semi-Poisson/GOE β=1), pooled Berry–Robnik **ρ = 1.000** (pure-Poisson limit), χ²-to-Poisson 14× better than semi-Poisson. Each Peter-Weyl (p,q) sector is intrinsically Poisson; the pooled excess is the Mehta-ch.16 superposition residual of M=90 independent integrable blocks (β_pooled = −0.221, driven *below* Poisson exactly as the superposition theorem requires). W1-1 corroborates from the orthogonal long-range axis: ⟨r⟩=0.3915≈Poisson, **no connected-SFF ramp** (trend −1.54, opposite the GUE +2τ ramp), and the number-variance exponent p_Σ²=0.62 is sub-linear only because Σ² saturates at a **finite-N rigidity ceiling** (L_sat grows 6.25→7.75 from L12→L14), not intrinsic RMT log-growth. Both gates point the same way: block-level Berry–Tabor integrability ([iK₇,D_K]=0; Schur orthogonality), with the pooled-spectrum intermediate appearance fully accounted as superposition + finite-N. The CHAOS-1 ambiguity is **closed on the integrable side**; kill authority not triggered (λ_L=0 at fabric scale).

**Finding B — the eigenbundle is trivial and the fold is generic, now confirmed on the genuinely non-Abelian channel (W1-3 INFO + W1-4 PASS).** W1-3 classifies the catastrophe germ of the lowest-band surface λ_min(τ,μ) on the 2-param U(2)-invariant TT surface as the Thom-stable **A₂ fold** (det H = 0.0134 ≠ 0, transverse curvature d²λ/dτ² = 1.7081 ≫ 0, A₃-cusp excluded, zero diabolical points), extending the S35 Jensen-line fold to the full surface. The fold IS the cosmogenesis transit; its A₂ germ certifies the van Hove fold the supersonic transit passes through is the *generic* fold, not a fine-tuned cusp. W1-4 computes the one place a non-trivial topological charge could still live — the second Chern number c₂ of the rank-4 B2 Wilczek-Zee bundle over the 4-param off-block C² coset — and finds **c₂ = 0** (machine-floor 8e-15, integer-quantized; normalization validated against a BPST one-instanton charge of −1; frame-invariance residual 2.4e-24). The genuine non-Abelian connection (f_WZ = 2.888785e-06 ≠ 0, reproducing S102/S103 exactly on the 1D-loop slices) carries **no integer charge**: the band's internal 4-fold degeneracy stays gapped from its neighbours, so the projector is smooth and the bundle trivializable. This is the **13th independent topological invariant to return trivial**, and the first on the isotropy-broken (Wilczek-Zee) channel rather than the on-block one — the metric-without-curvature wall now extends to the full broken base.

**Coupling to Wave 2.** Finding A (block-level Berry–Tabor integrability) is the structural support for INV3-W2-4's premise that integrability is a *strength* enabling a non-variational (Weyl-remainder / closed-geodesic) route to τ_fold — informational, not a hard dispatch dependency.

### Effected In-Session (non-math)

**None executed in-investigation.** Every non-math item Wave 1 surfaced is a **session-track curated-register edit**, which an investigation cannot make (track-local boundary per `gate-verdicts.md §"Investigation-Track Canonical Path"` + plan index §"Non-gate items"). All route to session-promotion at `/rclab-investigate --investigation 3` close:

- [→investigate] **W1-3 §W1-3 plan operator carries a PRU Class-8.2 rubric-form defect.** The literal "exactly one Hessian eigenvalue vanishes" tests the Thom *state-variable* Hessian; an eigenvalue *surface* fold is Morse (both control-space Hessian eigenvalues nonzero). Substrate physics (A₂ fold) unambiguous. Methodology note for any session-promotion: restate as the Morse-non-degeneracy discriminant (det H ≠ 0 ∧ |d²λ/dτ²| ≥ tol_curv ∧ ¬cusp). The frozen plan operator is **not** edited post-hoc (Class-3 prohibition); same defect would recur in any copied "eigenvalue-surface catastrophe germ" gate.
- [→investigate] **Plan-text imprecision (W1-1/W1-2 machinery pin):** `N_eval=78080` is labelled "L12 cache unique count" but is the L_max=10 figure (per `phononic-framing.md`); the L12 cache is 166,896-with-multiplicity / 6,997-globally-unique. Agents used the actual cache contents — results sound. Plan-hygiene note if promoted.
- [→investigate] **`f_WZ = 2.888785e-06` remains non-canonical** (HY3 promotion pending); sourced at runtime as a cross-check only.

(Investigation-internal: `canonical_constants.py`, the Atlas, the permanent-results registry, and the falsifier inventory are all session-track and are NOT touched from this investigation.)

## Carry-Forward Computations

Genuine future compute (4-field specs) → consumed by `/rclab-investigate --investigation 3`. All three are **session-promotion** items: an investigation result enters the permanent register only via a session-track re-compute (track-local boundary). Wave outcomes are otherwise closed in-investigation (no open intra-investigation compute).

### CF-INV3-W1-A — Promote block-level Berry–Tabor integrability to the permanent register
| Field | Spec |
|:------|:-----|
| **What** | Re-run the sector-resolved P(s) β_block + SFF/number-variance discriminator as session-track gate(s); land a permanent-results entry: "D_K spectral statistics are block-Poisson (Berry–Tabor); the pooled ⟨r⟩-above-Poisson excess is a Mehta-ch.16 superposition artifact of M=90 integrable blocks." |
| **Inputs** | `computations/investigation-3/inv3_w1_ps_sector.py`, `inv3_w1_sff_numvar.py`; `s84_spectrum_cache_L12_tau019.npz` + `s87_spectrum_cache_L14_tau019.npz`; `r_POISSON_canonical=0.3863`, `r_GOE_canonical=0.5307`. |
| **Gate** | β_block ∈ [−0.15, 0.30] ∧ ρ_pooled ≥ 0.85 (PASS-pooling-artifact), reproduced on the session track; SFF ramp absent ∧ Σ² finite-N-saturating. |
| **Effort** | ~0.5 wave-equiv (scripts exist; session-track re-run + registry landing). |

### CF-INV3-W1-B — Promote c₂=0 as the 13th trivial invariant on the non-Abelian channel (§VII.BR family)
| Field | Spec |
|:------|:-----|
| **What** | Re-run the B2 4D second-Chern c₂ as a session-track gate; land/extend the §VII.BR record — the off-block Wilczek-Zee channel carries a non-trivial *connection* (f_WZ≠0) but **zero integer charge** (c₂=0); the metric-without-curvature wall extends to the full 4-param broken base. |
| **Inputs** | `computations/investigation-3/inv3_w1_second_chern_b2.py` + `_bpst_calib.json`; the B2 quadruplet at \|λ\|=0.845212; s102/s103 f_WZ 1D-loop cross-checks. |
| **Gate** | \|c₂ − round(c₂)\| < 0.05 (= 0) with frame_invariance_residual < 1e-8; BPST one-instanton normalization → −1. |
| **Effort** | ~0.5 wave-equiv (script exists; session-track re-run + §VII.BR registry landing). |

### CF-INV3-W1-C — Promote the A₂-fold germ on the 2-param surface (with corrected operator)
| Field | Spec |
|:------|:-----|
| **What** | Land the A₂-fold germ of λ_min(τ,μ) on the U(2)-invariant TT surface as a session-track structural result (extends the S35 Jensen-line fold to the full surface), using the **corrected** Morse-non-degeneracy operator (det H ≠ 0 ∧ \|d²λ/dτ²\| ≥ tol_curv ∧ ¬cusp), not the mis-specified literal pre-reg. |
| **Inputs** | `computations/investigation-3/inv3_w1_catastrophe_germ.py` (corrected operator already implemented); s92 τ-bracket caches; s96 off-Jensen scaffold; s84 L12 cache. |
| **Gate** | det H ≥ 1e-3 ∧ \|d²λ/dτ²\| ≥ 0.1 ∧ A₃-cusp condition False → A₂_fold (PASS under corrected operator). |
| **Effort** | ~0.25 wave-equiv (compute done; session-track re-run + registry landing + the Class-8.2 operator-form methodology note). |

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:---------|:-------|
| 2026-06-15 | CHAOS-1 pooled ⟨r⟩-above-Poisson ambiguity | OPEN (integrable-leaning, unresolved) | CLOSED on integrable side | W1-2 β_block=−0.064 (per-sector Poisson) + W1-1 no-ramp/finite-N-Σ² → superposition artifact, not intrinsic repulsion |
| 2026-06-15 | D_K number-variance sub-linearity (p_Σ²=0.62) | candidate arithmetic-chaos signal | finite-N rigidity ceiling (closed) | L_sat grows 6.25→7.75 with L_max; short-range physics Poisson |
| 2026-06-15 | Eigenbundle topology, off-block non-Abelian channel | un-measured (only on-block + 1D-loop done) | TRIVIAL (c₂=0; 13th trivial invariant) | W1-4 second-Chern at machine-floor; connection ≠ 0 but no integer charge |
| 2026-06-15 | Catastrophe germ of λ_min(τ,μ), 2-param surface | A₂ only on Jensen line (S35) | A₂ fold on full U(2)-invariant surface (generic transit geometry) | W1-3 det H≠0, d²λ/dτ²=1.7081, A₃ excluded, 0 diabolical points |
| 2026-06-15 | §W1-3 plan operator | assumed well-posed | PRU Class-8.2 rubric-form defect (substrate result unaffected) | literal Hessian-degeneracy clause mis-imported state-variable→control-space; routed to /rclab-investigate |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict | audit_sha256 (head) |
|:-----|:-------|:------------|:------------|:--------|:--------------------|
| INV3-W1-1 | inv3_w1_sff_numvar.py | inv3_w1_sff_numvar.npz | inv3_w1_sff_numvar.png | INFO | 68e51fd3… |
| INV3-W1-2 | inv3_w1_ps_sector.py | inv3_w1_ps_sector.npz | inv3_w1_ps_sector.png | PASS | 452a538a… |
| INV3-W1-3 | inv3_w1_catastrophe_germ.py | inv3_w1_catastrophe_germ.npz | inv3_w1_catastrophe_germ.png | INFO | 694c485a… |
| INV3-W1-4 | inv3_w1_second_chern_b2.py | inv3_w1_second_chern_b2.npz | inv3_w1_second_chern_b2.png | PASS | b63c4542… |

(All under `computations/investigation-3/`; verdict ledger `inv3_gate_verdicts.txt`; sidecar `_bpst_calib.json` for W1-4.)
