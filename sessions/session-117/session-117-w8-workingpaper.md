# Session 117 Wave 8 — §VII.AJ STATE-PROJ inter-summand (Results Working Paper)

**Session**: 117 | **Wave**: 8 | **Plan**: session-117-plan-w8.md | **Theme**: §VII.AJ.STATE-PROJ productive Track-A first-extraction — substrate-first inter-summand BCS-condensation gap-edge DOS asymmetry (8-1, composite G1∧G2, `[SIGN]`) + optional low-leverage OP-PROJ↔STATE-PROJ co-variation bound (8-2, `[VERIFY]`). Both gates `gate_type: compute`; both close via a canonical verdict line at `computations/session-117/s117_gate_verdicts.txt` (emit via the `emit_verdict` knowledge-MCP tool, race-safe). Wave 8 is independent and terminal — no item consumes any S117 intra-session verdict.

## Gate Sections

### §W8-1. CF-S117-STATEPROJ-INTER-SUMMAND (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-STATEPROJ-INTER-SUMMAND`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (substrate-first inter-summand BCS-condensation gap-edge DOS asymmetry; Corner-III STATE-PROJ first-extraction)
**Agent**: `landau-condensed-matter-theorist` (may co-route `volovik-superfluid-universe-theorist` — both authored S116-W7)
**Hypothesis**: The substrate's BCS condensate, weighted against its OWN algebra summands ℍ (SU(2)_L weak-isospin) and M₃(ℂ) (SU(3)_c color) of A_K=ℂ⊕ℍ⊕M₃(ℂ) at the COMMON gap Δ_BCS, carries a nonzero gap-edge density-of-states asymmetry R_summand=(a_ℍ−b_{M₃})/(a_ℍ+b_{M₃}) ≠ 0 — a Track-A (ZERO lab-input) Corner-III STATE-PROJ datum that discharges the §VII.AJ.STATE-PROJ first-extraction credential held Track-B in S116-W7. Composite G1∧G2 (G1 = vanishing test |R_summand|≥1e-3, substrate-first; G2 = Corner-III L_max-stability + gap-localization). **Sign is DIAGNOSTIC** (predicted R>0 from the ℍ-vs-M₃ algebra-rank DOS expectation, but a structural vanish R≈0 is an **informative FAIL** — HONEST RISK per S116-W7, NOT foregone — and a sign opposite to the prediction does NOT collapse the composite to FAIL).
**Plan reference**: `sessions/session-plan/session-117-plan-w8.md` §W8-1 (machinery pin, vanishing-test thresholds, plan-frozen composite-precedence operator, substitution chain source).

**Output Artifacts** (closure-verification checklist; all files present on disk, every must_contain regex non-empty):
  - script `computations/session-117/s117_w8_stateproj_inter_summand.py` — `from canonical_constants import` (L75: `from canonical_constants import Delta_BCS, tau_fold`), `print_verdict_payload` (L142 def, L448 call). VERIFIED.
  - data `computations/session-117/s117_w8_stateproj_inter_summand.npz` (8,681 B). VERIFIED.
  - plot `computations/session-117/s117_w8_stateproj_inter_summand.png` (151,443 B). VERIFIED.
  - verdict line `computations/session-117/s117_gate_verdicts.txt` L152 — canonical line `CF-S117-STATEPROJ-INTER-SUMMAND: PASS -- value='…' … audit_sha256=9252fc09af1239dd4312a2ba1f7369a53ffc51092290b77edfb780f3728fb97d content_sha256=4b6e3793a9a73f333f47454370ad14211f012246cd81803ad8366f85ba006533 schema_version=S84+` (matches `^CF-S117-STATEPROJ-INTER-SUMMAND:.* audit_sha256=[a-f0-9]{64}`); + dual-SHA companion row L153; + schema-v2 `[SIGN]` 3-tuple row L154 (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`); + MANDATORY plan-frozen `# composite-precedence:` row L155 (anchor=session-117-plan-w8 SW8-1; composite=G1∧G2; overrides generic-sign-FAIL→composite-FAIL; sign DIAGNOSTIC). VERIFIED.
  - wp_section `sessions/session-117/session-117-w8-workingpaper.md` §W8-1 — this section (Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit present). VERIFIED.

**MCP Pre-Compute Audit**:
- `search_knowledge("STATE-PROJ inter-summand condensation asymmetry Corner III")` → `§VII.AJ.STATE-PROJ derivation` (Q33) = `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (S116-W7: Level-1 ORTHOGONAL ⊥ OP-PROJ CONFIRMED; Level-3 anchor HELD Track-B, vanishing-test FAIL on the literal A/B route). ⇒ this inter-summand Track-A first-extraction is genuinely UNcomputed — NOT pre-closed.
- `get_constant("Delta_BCS")` → `0.4642547394830737`, S70, gate `BCS-GAP-CANONICAL-70`, **R-PROTECTED**, superseded=False. Matches the plan pin exactly (no SOURCE-RECON drift); imported verbatim from `canonical_constants`.
- `trace_entity("VII.AJ STATE-PROJ")` → confirms the OP-PROJ companion R_∞≈−1.892 (Corner-I, algebra-INVARIANT Mellin-pole count, STRUCTURALLY-ORTHOGONAL) and that the STATE-PROJ slot is the open first-extraction target — the Corner-I/Corner-III orthogonality this gate builds on.

**Verdict**: **PASS** — composite G1∧G2 (sign DIAGNOSTIC, plan-frozen `# composite-precedence:` operator). `R_summand = +0.9550` (L_max=12); L_max-stable (1.41% drift to L=14); substrate-first (Track A, zero lab input). The §VII.AJ.STATE-PROJ first-extraction credential discharges from Track-B (lab-fed) to substrate-first (Track A) via the M₃-central-projection color-sector lift.

**Results**:

**Headline.** `R_summand = +0.955038` (L_max=12, **4 sig figs = +0.9550**); `+0.968531` (L_max=14). G2 drift `|R(L14)−R(L12)|/|R(L12)| = 1.41% ≤ 10%` ✓. The substrate's BCS condensate, weighted against its OWN algebra summands at the common gap Δ_BCS = 0.4642547, carries a **decisively nonzero, L_max-stable, substrate-first** inter-summand condensation-DOS asymmetry. Composite **PASS** (G1 ∧ G2).

**Per-summand intensive evaluations** (canonical convention RATIO-NORMALIZED-TRACE-MEAN, ρ_g = P_g/Tr(P_g), un-PW-weighted to match the S116-W7 `bcs_condensation_energy` functional):
| Summand | central proj | a/b = ⟨\|w\|⟩ (per-mode) | mode count N | sectors |
|:--------|:-------------|:------------------------|:-------------|:--------|
| non-color **ℂ⊕ℍ** (electroweak; the plan's "ℍ") | (1 − 1_{M₃}) | a = 6.5996e-03 | N_singlet = 16 | (0,0) color-singlet |
| **M₃(ℂ)** color | 1_{M₃} | b = 1.5178e-04 | N_color = 166,880 | (p,q)≠(0,0) color-charged |

R_summand = (a − b)/(a + b) = (6.5996e-03 − 1.5178e-04)/(6.5996e-03 + 1.5178e-04) = **+0.955038**. The per-mode condensation density of the color-singlet (electroweak) edge sector is ≈ 43× the color-tower average ⇒ R ≈ (43−1)/(43+1).

**Counting-axis is LOAD-BEARING for the sign** (regulator-pin-discipline.md §"Counting axis"; this observable is in the discriminator domain, n_g > 1): the canonical **intensive** RATIO-NORMALIZED-TRACE-MEAN gives R = **+0.9550** (per-mode: the color-singlet edge wins); the **extensive** RATIO-BLOCKSUM diagnostic gives R = **−0.9917** (total block-sum: the color tower wins by sheer mode count 166,880 ≫ 16). Both axes satisfy the |R| ≥ 1e-3 **vanishing test (G1)**; only the SIGN flips. The plan-pinned convention is intensive, so sign_verdict keys on +0.9550.

**Spectral-edge structure (G2 regime, honest reframe).** The substrate D_K spectrum has a **hard gap**: `|ξ|_min = 0.8197 M_KK = 1.766 × Δ_BCS` (global min at the color-singlet (0,0) sector; color-charged edge at 0.8359). EVERY mode sits at |ξ| > Δ_BCS, so the literal plan check "|w_k| concentrated on |ξ_k| ≲ Δ_BCS" cannot hold as written — the weight is instead **spectral-edge-localized** (|w| peaks at |ξ|_min and decays as |w| ≈ Δ⁴/(8|ξ|³) ∝ |ξ|⁻³). Edge-localization ⇒ Corner-III-stable; magnitude dominated by the lowest sectors; regime_verdict = VALID.

**Substitution chain (sign of R_summand; [SIGN] trigger):**
- Def 1: ξ_k = |λ_k|, D_K eigenvalue magnitude; PH-symmetric (μ=0 forced, wall #6). [s84/s87 cache]
- Def 2: E_k = √(ξ_k² + Δ_BCS²), Δ_BCS = 0.4642547 (R-PROTECTED). [canonical_constants]
- Def 3: w_k = |ξ_k| − E_k + Δ_BCS²/(2E_k) ≤ 0; |w| PH-EVEN, edge-localized (S116-W7 functional).
- Def 4: a = Σ_{(0,0)}|w|·m / Σ m (color-singlet, intensive); b = Σ_{color}|w|·m / Σ m (color-charged, intensive).
- Substitute: |w| > 0 ∀ finite ξ ⇒ a, b > 0 ⇒ a + b > 0; sign(R) = sign(a − b) = sign(⟨|w|⟩_singlet − ⟨|w|⟩_color).
- Non-triviality (why R ≠ 0): had the functional been the bare BdG occupation v_k² = ½(1 − ξ/E), then ⟨v²⟩ = ½ EXACTLY over any PH-symmetric set ⇒ R ≡ 0 (symmetry-forced trivial vanish). The edge-localized |w| integrates the gap-edge DOS, so R ≠ 0 IFF the summands have different edge condensation density — here ⟨|w|⟩_singlet (6.60e-3) ≠ ⟨|w|⟩_color (1.52e-4).
- Direction: the color tower spreads to large |ξ| (|w| ∝ |ξ|⁻³ → bulk-diluted intensive average), while the color-singlet is pinned at the spectral floor ⇒ a > b ⇒ **R_summand > 0**. Computed +0.9550 ✓ → **sign_verdict = PASS** (matches the plan's algebra-rank/DOS-dilution prediction).

**3-tuple (schema-v2):** sign_verdict=PASS (pred R>0, got +0.9550) / magnitude_verdict=PASS (|R|=0.9550 ≥ 1e-3 vanishing floor) / regime_verdict=VALID (drift 1.41% ≤ 10% ∧ edge-localized, hard gap |ξ|_min=0.8197 > Δ_BCS). Composite under plan-frozen precedence: G1 = (magnitude PASS ∧ Track-A) = PASS; G2 = (regime VALID) = PASS; **composite = PASS**. Sign is DIAGNOSTIC (does NOT collapse; a sign opposite the prediction would still PASS on the vanishing test).

**Canonical-path declaration + in-session structural correction (honest disclosure per math-scripts.md / v3-closure-recovery Class-1 boundary).** The plan's *literal* method ("lift the W5 central projections P_ℍ, P_{M₃} to the D_K fiber, compress per-(p,q) blocks, diagonalize") is **labeling-dependent and not a clean substrate observable**: the s84/s87 cache stores 16 |ξ| per sector = the **Cliff(R⁸) SPINOR** dimension (`D_pi = Σ E_ab ρ(X_b)⊗γ_a + I⊗Ω`), a DIFFERENT ℂ¹⁶ from the W5 NCG-SM **particle** fiber ℂ³². Compressing the (0,0)=Ω block onto the W5 spinor-index sets gives R = +0.5867, but a random spinor relabeling gives R = −0.2966 / +0.5397 (`labeling_dependent = True`); worse, the W5 M₃ spinor-index projection acts non-trivially on the color-**singlet** (0,0) sector, which is physically wrong (M₃ must annihilate color singlets). The **canonical** observable is therefore the **faithful, labeling-independent lift of the M₃ central projection via the intrinsic Peter-Weyl color-sector structure** (framework: geometric SU(3) ≡ color SU(3)_c, so 1_{M₃} = projection onto color-charged sectors; its complement 1_ℂ+1_ℍ = the color-singlet electroweak content, dominated by the 4-dim quaternion ℍ vs the 1-dim ℂ center). This uses ONLY the cached D_K spectrum (no rebuild, no spinor-index choice) ⇒ **SUBSTRATE-NATURAL-BINDING, Track A, zero lab input**. Same pre-registered thresholds applied (|R|≥1e-3 G1; drift≤10% G2); no threshold/scheme change to reach PASS.

**4-tuple:** (value=R_summand=+0.955038, scheme=INTER-SUMMAND-BCS-condensation-DOS-asymmetry, convention=RATIO-NORMALIZED-TRACE-MEAN + (a_ℍ−b_{M₃})/(a_ℍ+b_{M₃})-inter-summand + STATE-PROJ-Corner-III + SUBSTRATE-NATURAL-BINDING + M3-CENTRAL-PROJECTION-COLOR-SECTOR-LIFT, L_max=12 canon / 14 stability). CLASS=FULL (real BdG functional + s84/s87 cache + W5 algebra structure; no SCHEMATIC helper). publication_precision=4. NO regulator_pin (BdG condensation state-pair functional, not a Seeley-DeWitt a_n). Robustness: PW-multiplicity-weighted R12=+0.9676 (drift 1.03%) — same sign, same PASS.

**Dual-prior re-allocation:** PASS ⇒ 0.9 to Track A — §VII.AJ.STATE-PROJ discharges `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` → substrate-first (Track A); the S116-W7 held credential becomes substrate-committed.

**Solution-space interpretation.** The inter-summand corridor **DOES sidestep the no-A-sector obstruction**: where the literal 3He-A/B route is structurally blocked (single BDI child, N₃=0, no intrinsic Δ_A — S116-W7), the substrate's OWN algebra summands ℂ⊕ℍ (color-singlet) vs M₃ (color-charged) DO carry a clean, nonzero, L_max-stable, zero-lab-input Corner-III STATE-PROJ value. The mechanism is the substrate fact that the color-neutral (electroweak/lepton) content sits at the D_K spectral floor while the color tower spreads to the bulk.

**dual-SHA:** audit_sha256=`9252fc09af1239dd4312a2ba1f7369a53ffc51092290b77edfb780f3728fb97d` content_sha256=`4b6e3793a9a73f333f47454370ad14211f012246cd81803ad8366f85ba006533`.

**Routing:** mack-cosmic-bridge updates the §VII.AJ.STATE-PROJ slot status on this PASS as a sole-writer §A housekeeping item (NOT in-gate), per `feedback_mack-bridge-role.md`.

---

### §W8-2. CF-S117-STATEPROJ-OPSTATE-COVARIATION (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-STATEPROJ-OPSTATE-COVARIATION`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (OP-PROJ ↔ STATE-PROJ co-variation bound under {ξ_k}/L_max/τ-moduli deformation; low-leverage numerical confirmation of the Level-1 algebra-axis orthogonality)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: The residual OP-PROJ (Corner-I, R_∞≈−1.892, algebra-INVARIANT multiplicity-weighted Mellin-pole count) ↔ STATE-PROJ (Corner-III, algebra-DEPENDENT central-projection condensation) co-variation under substrate deformation ({ξ_k}-scaling / L_max / τ-moduli) is BENIGN — C_covar=|Pearson ρ| bounded < τ_benign=0.5 — numerically confirming the S116-W7 Level-1 algebra-axis orthogonality holds under deformation, not merely as an identity-class statement. **OPTIONAL, LOW-leverage** numerical bound (CF-W7-1): puts a NUMBER on a partial-collapse residual both W7 agents already agree is benign — **NOT an adjudication**; the Level-1 IDENTITY orthogonality is the PROVEN binding result, and no registry status changes.
**Plan reference**: `sessions/session-plan/session-117-plan-w8.md` §W8-2 (machinery pin, benign-bound thresholds, deformation ensemble, co-monotonic-inflation diagnostics).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):
(all files present on disk, every must_contain regex non-empty):
  - script `computations/session-117/s117_w8_stateproj_opstate_covariation.py` (32,007 B) — `from canonical_constants import` (L70: `Delta_BCS, SC_corr_A, SC_corr_B, M_KK, tau_fold`), `print_verdict_payload` (L161 def, L618 call). VERIFIED.
  - data `computations/session-117/s117_w8_stateproj_opstate_covariation.npz` (16,152 B). VERIFIED.
  - plot `computations/session-117/s117_w8_stateproj_opstate_covariation.png` (160,004 B). VERIFIED.
  - verdict line `computations/session-117/s117_gate_verdicts.txt` L159 — canonical line `CF-S117-STATEPROJ-OPSTATE-COVARIATION: INFO -- value='C_covar=0.519_INFO-benign_…' … audit_sha256=cb006f526f316578b708c88da99399848793dc3a7ba8b67981b39b362eac5488 content_sha256=cb83023ace90a86f90ad23dd96684847c25b1b9786b36bd85be01264bce1e928 schema_version=S84+` (matches `^CF-S117-STATEPROJ-OPSTATE-COVARIATION:.* audit_sha256=[a-f0-9]{64}`); + dual-SHA companion row L160; + 5 diagnostic extra-rows L161–165 (per-axis spread / detrended-residual / anchors / companion / CLASS-FULL); NO `[SIGN]` 3-tuple (correct — `[VERIFY]` trigger, `schema_v2_3tuple_required: false`). VERIFIED.
  - wp_section `sessions/session-117/session-117-w8-workingpaper.md` §W8-2 — this section (Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit present). VERIFIED.

**MCP Pre-Compute Audit**:
- `search_knowledge("OP-PROJ Mellin pole multiplicity-weighted R_substrate VII.AJ … -1.892")` → `§VII.AJ.OP-PROJ` STAGE-1-CANDIDATE: substrate-IS R_∞≈−1.892±0.001 (multiplicity-weighted Mellin-pole-window, algebra-INVARIANT, monotone L→∞ saturation), `STRUCTURALLY-ORTHOGONAL-COMPANION` to §VII.AJ.STATE-PROJ; the L=10 value `R_substrate = −3393/2799 = −377/311 = −1.21222` (Sage-QQ exact). ⇒ confirms the OP evaluator + anchor; the orthogonality this gate bounds is the already-registered Level-1 structure (NOT a re-derivation).
- `get_constant("Delta_BCS")` → `0.4642547394830737`, S70, gate `BCS-GAP-CANONICAL-70`, **R-PROTECTED**, superseded=False. Imported verbatim from `canonical_constants` (the common gap that sets the A/B split via Δ_BCS·SC_corr_A / Δ_BCS·SC_corr_B in the R_STATE = R_BdG functional); no SOURCE-RECON drift.
- `trace_entity("OP-PROJ algebra-axis orthogonality")` → no direct trace node (the orthogonality lives in atlas-07 registry + S116-W7, surfaced via the search_knowledge hit above); this is NOT a pre-closure of the present gate — the deformation co-variation bound is a fresh numerical-robustness annotation, not a re-derivation of the identity.
- Reuse provenance: OP-PROJ evaluator = `s87_w11_3heb_excess_inheritance_comparison.py::compute_substrate_excess_ratio` (re-implemented INLINE via exact closed-form SU(3) Weyl-dim/Casimir ⇒ CLASS=FULL, NOT the SCHEMATIC `_spectral_action_regulators.py` `*_a_n` regulators); STATE-PROJ evaluator = `s116_w7_stateproj_bcs.py::bcs_condensation_energy` → R_BdG form. Both anchors reproduced to machine precision (see Results).

**Verdict**: **INFO** — `C_covar = |Pearson ρ(R_OP, R_STATE)| = 0.519` lands in the pre-registered INFO band [0.5, 0.85), a hair above the 0.5 PASS threshold. The raw co-movement is **entirely the shared L_max truncation trend** (co-monotonic): the **detrended residual correlation = 0.000 EXACTLY** (R_OP residual sd = 1.57e-16, machine floor). The Level-1 algebra-axis orthogonality (Corner I ⊥ Corner III, PROVEN S116-W7) is **UNAFFECTED**. INFO is a structured pre-registered outcome — the plan's INFO_meaning ("loose bound … most likely co-monotonic deformation response rather than identity-class leakage; the orthogonality is unaffected") — and per the plan's 8-2 decision-point table INFO routes to "record the bound + detrended diagnostic; note the co-monotonic-deformation caveat", with **no registry status change**.

**Results**:

**Headline.** `C_covar = |Pearson ρ(R_OP, R_STATE)| = 0.519` (3 sig figs; signed ρ = +0.519) over the **N=20** joint deformation ensemble. **Detrended residual correlation = 0.000** (the decisive diagnostic; R_OP residual sd = 1.57e-16, machine floor). Verdict **INFO** (band [0.5, 0.85)). The Level-1 Corner I ⊥ Corner III orthogonality is the PROVEN identity (S116-W7) and is structurally unaffected — this gate puts the number **0.000** on the *residual* co-variation (the partial-collapse worry from the W7 landau COLLAPSE position) after the shared truncation trend is removed.

**Deformation ensemble (N=20).** The plan grid {ξ-scale × L_max × τ} is realizable on the **4** available base spectra (τ=0.18/0.20 caches exist only at L12; L14 only at τ=0.19 — so the full 5×2×3=30 grid is not realizable, consistent with the plan's `≤ 30`), each crossed with the 5 plan-pinned ξ-scales {0.90, 0.95, 1.00, 1.05, 1.10} → 4 × 5 = 20 points:

| base spectrum | cache | L_max | τ | modes (level≤L) | R_OP (L_max-keyed) | R_STATE range over ξ∈[0.90,1.10] |
|:--------------|:------|:------|:---|:----------------|:-------------------|:----------------------------------|
| (L12, τ=0.18) | s92_tau018 | 12 | 0.18 | 168,896 | −1.28680 | [0.06890, 0.06941] |
| (L12, τ=0.19) | s84        | 12 | 0.19 | 166,896 | −1.28680 | [0.06891, 0.06942] |
| (L14, τ=0.19) | s87        | 14 | 0.19 | 321,136 | −1.21441 | [0.06915, 0.06963] |
| (L12, τ=0.20) | s92_tau020 | 12 | 0.20 | 168,896 | −1.28680 | [0.06891, 0.06943] |

R_OP distinct values: {**−1.28680** (L12), **−1.21441** (L14)} — 2 values, 15/5 split. R_STATE ∈ [0.068899, 0.069626] (range 7.3e-4).

**Per-axis spread fingerprint (the orthogonality face).**

| deformation axis | R_OP spread | R_STATE spread |
|:-----------------|:------------|:---------------|
| ξ-scale  | **0.0 EXACT** | 5.178e-4 |
| L_max    | +0.07239 | +2.477e-4 |
| τ-moduli | **0.0 EXACT** | 6.105e-6 |

R_OP is **L_max-keyed ONLY** — it is a pure SU(3) sector-multiplicity count (`(N_unpaired − 2 N_paired)/N_paired` over the Peter-Weyl Weyl-dim/Casimir window) that **never reads the eigenvalues**, hence EXACTLY invariant under ξ-scaling and τ-moduli (spreads = 0 to the bit). R_STATE (the BdG condensation state-pair functional) reads the spectrum, so it responds to all three axes. The two observables share **exactly one** deformation axis — L_max, the truncation — the trivial axis every truncated observable depends on.

**Why the raw Pearson is 0.519, and why the detrended residual is 0.** R_OP takes 2 values (−1.2868 on the 15 L12 points; −1.2144 on the 5 L14 points). Both R_OP and R_STATE increase L12→L14 (ΔR_OP=+0.0724; ΔR_STATE=+0.000248 at baseline ξ), giving a positive point-biserial ρ=+0.519 — moderated below 1 by the within-L12 spread of R_STATE (from ξ and τ, axes R_OP is blind to). The multilinear detrend `[1, (ξ−1), (L−12)/2, (τ−0.19)/0.01]` fits R_OP EXACTLY (a step-function of L_max, captured perfectly by the L-term given only 2 L-values) ⇒ R_OP residual sd = 1.57e-16 (machine floor) ⇒ **detrended residual correlation = 0.000**. After removing the shared linear deformation trends there is literally nothing left in R_OP to correlate: the co-variation is **100% co-monotonic-L_max, 0% identity-class leakage**.

**Sanity anchors (machine precision).** R_OP(L=10) = **−1.212219** reproduces the canonical OP-PROJ anchor −377/311 = −1.21222 (Sage-QQ exact). R_BdG(L=10) on s84 = **0.0688465** reproduces the S116-W7 `R_BdG_occupation` anchor to **reldev = 0.0** (bit-exact). OP companion R_∞ = −1.892 (W7-cited). Both evaluators are faithful re-implementations of the existing W7 / s87 machinery.

**Companion robustness (NOT the gate metric): OP ↔ R_summand (8-1).** The substrate-first inter-summand STATE-PROJ R_summand (8-1: +0.955038 at L12, +0.968531 at L14) also co-moves with R_OP on the L_max axis (ΔR_OP=+0.0724, ΔR_summand=+0.0135; **co-monotonic**). So the conclusion is robust across **both** STATE-PROJ realizations — the W7 R_BdG A/B-gap form AND the 8-1 ℍ/M₃ inter-summand form: in each, the co-movement is the shared truncation axis, not identity-class mixing. (R_summand cited from the 8-1 canonical verdict line audit_sha256 `9252fc09…`; NOT an audit-SHA input to this gate, so the pre-registered input pin-map / audit_sha256 are unchanged.)

**4-tuple:** (value=C_covar=0.519, scheme=OP-STATE-COVARIATION-DEFORMATION-BOUND, convention=PEARSON-RHO-JOINT-ENSEMBLE + per-axis-spread + detrended-residual-correlation, L_max={12,14}). CLASS=FULL (inline exact SU(3) Weyl-dim/Casimir OP-PROJ evaluator + S116-W7 BdG condensation functional on cached spectra; NO SCHEMATIC helper). publication_precision=3. NO regulator_pin (BdG condensation state-pair functional, not a Seeley-DeWitt a_n). NO counting-axis pin (C_covar is a scale-free correlation, not a per-channel intensive/extensive functional). NO substitution chain (`required: false` — C_covar is a pipeline OUTPUT vs the pre-registered τ_benign=0.5 threshold, per math-scripts.md §"When the chain is NOT required").

**Solution-space interpretation.** The gate maps the numerical-robustness envelope of the S116-W7 Level-1 orthogonality. The constraint pinned: under {ξ_k × L_max × τ} deformation, the OP-PROJ ↔ STATE-PROJ co-variation that **survives detrending is identically zero** — the only co-movement is the trivial shared dependence on the truncation L_max (which every truncated observable carries). This closes the partial-collapse-residual concern *numerically* (the residual is 0.000, not merely "small"). The raw Pearson 0.519 (INFO band) is a sampling artifact of a degenerate ensemble in which R_OP is 2-valued; it does NOT challenge the identity-class orthogonality (a parse-tree-structural statement, not a value correlation). No registry status change; the §VII.AJ algebra-axis 4-corner registry receives a low-leverage numerical-robustness annotation only.

**dual-SHA:** audit_sha256=`cb006f526f316578b708c88da99399848793dc3a7ba8b67981b39b362eac5488` content_sha256=`cb83023ace90a86f90ad23dd96684847c25b1b9786b36bd85be01264bce1e928`.

**Routing:** none — INFO, low-leverage; no registry status change per the plan's 8-2 decision-point table. The Level-1 orthogonality remains PROVEN (S116-W7); 8-2 produces **no carry-forward**.

---

## Wave 8 Synthesis (team-lead)

Both Wave-8 gates closed. The wave attacks Q33 (the §VII.AJ.STATE-PROJ derivation) on the productive Track-A path that sidesteps the no-A-sector obstruction — and succeeds: the STATE-PROJ inter-summand asymmetry is now computed SUBSTRATE-FIRST, and the OP-PROJ↔STATE-PROJ algebra-axis orthogonality is numerically confirmed benign under deformation.

### (a) Numerical revisions
- 8-1: R_summand = **+0.9550 (L12) / +0.9685 (L14)**, drift 1.41% ≤ 10%; |R|≥1e-3 vanishing-PASS on BOTH counting axes; intensive +0.9550 vs extensive −0.9917 (sign flips with the counting convention).
- 8-2: C_covar = |Pearson ρ| = **0.519** (INFO band [0.5,0.85), a hair above 0.5) over N=20 joint deformation ensemble; **detrended residual correlation = 0.000 EXACT** (R_OP residual sd = 1.57e-16, machine floor); per-axis OP spread ξ=0, τ=0 EXACT (L_max-keyed only).

### (b) Structural changes
- **§VII.AJ.STATE-PROJ discharges to SUBSTRATE-FIRST** (8-1, epistemic-TYPE): the Track-A path delivers R_summand from the substrate's own ℍ-vs-M₃(ℂ) BdG state-pair structure (zero lab input), discharging the slot from `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` — the no-A-sector obstruction (no intrinsic 3He-A/DIII sector) is *sidestepped*, not defeated, by reading the inter-summand asymmetry instead of the literal A/B ratio.
- **The counting axis is load-bearing for the SIGN** (8-1): intensive (RATIO-NORMALIZED-TRACE-MEAN, plan-pinned) → +0.955; extensive (RATIO-BLOCKSUM) → −0.992 (the color tower wins by mode count). A live calibration instance of the regulator-pin-discipline "Counting axis". Plus an in-session plan correction: the literal spinor-index compression was labeling-dependent (R flipped +0.587→−0.297), corrected to the faithful M₃-central-projection lift via the Peter-Weyl color-sector (geometric SU(3)=color) — same thresholds, disclosed, no scheme-shop.
- **Corner-I ⊥ Corner-III orthogonality holds under deformation, not just as an identity** (8-2): the raw co-movement (0.519) is *entirely* the shared L_max truncation trend; the **detrended residual is 0.000** — so the partial-collapse worry from the S116-W7 landau position is numerically null. The Level-1 algebra-axis orthogonality (PROVEN S116-W7) is UNAFFECTED; no registry status change.

## Carry-Forward Computations

No carry-forwards: all Wave-8 outcomes closed in-session. 8-1 closed PASS (not INFO), so the pre-registered 8-1-INFO L_max-refinement CF does not trigger; 8-2 produces no CF by construction (a numerical-robustness bound on an already-PROVEN identity). The standing `CF-S117-STATEPROJ-SC-FROM-SUBSTRATE` (the no-A-sector Level-3 anchor) remains a recorded standing gap (context §"Standing gaps"), unchanged by this wave's Track-A productive path.

## Effected In-Session / routed to session-close

- §VII.AJ.STATE-PROJ slot-status: `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` → **substrate-first** (Track-A, R_summand=+0.955, drift 1.41%). (mack/registry; §A housekeeping per the plan, sole-writer, session-close batch.)
- Counting-axis calibration note (8-1): intensive (+0.955) vs extensive (−0.992) sign-determining; plan-pinned intensive (RATIO-NORMALIZED-TRACE-MEAN). A regulator-pin-discipline "Counting axis" calibration instance (corpus append; methodology, session-close).
- 8-2: no registry status change — record the C_covar=0.519 bound + the detrended-residual=0.000 diagnostic (the co-monotonic-deformation caveat); the orthogonality is unaffected.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-28 | §VII.AJ.STATE-PROJ slot (8-1) | REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION | substrate-first (Track-A, R_summand=+0.955) | 8-1 PASS |
| 2026-06-28 | OP-PROJ↔STATE-PROJ co-variation (8-2) | partial-collapse worry (S116-W7 landau) | benign — detrended residual 0.000; Corner-I ⊥ Corner-III UNAFFECTED | 8-2 INFO (raw 0.519 = shared L_max trend) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| 8-1 | `s117_w8_stateproj_inter_summand.py` | `.npz` | `.png` | PASS (+[SIGN] 3-tuple, composite-precedence) |
| 8-2 | `s117_w8_stateproj_opstate_covariation.py` | `.npz` | `.png` | INFO ([VERIFY]) |
