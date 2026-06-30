# Investigation 13 Wave 1 — Cross-domain compute: collider spectroscopy, strong-field corrections, DR3 readiness (Results Working Paper)

**Investigation**: 13 | **Wave**: 1 | **Plan**: investigation-13-plan-w1.md | **Track**: investigation (verdict ledger `computations/investigation-13/inv13_gate_verdicts.txt`, emit via `emit_verdict(session=13, track="investigation")`) | **Theme**: the three cross-domain compute carry-forwards surviving inv-1…inv-12 dedup — GGE cosmological-collider squeezed-limit f_NL spectroscopy, a₄ higher-curvature QNM/tidal correction, branch-(iv) w₀ DR3-readiness truncation test. Gate-type mix: compute×3, mutually independent (no intra-wave pins).

## Gate Sections

### §W1-1. INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (cosmological-collider squeezed-limit spectroscopy of the GGE branch-multipliers)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The post-transit GGE quasiparticle spectrum imprints a computable non-analytic squeezed-limit feature in f_NL(k1,k2,k3) at a characteristic D_K eigenvalue ratio (collider "spectroscopy" of the three SU(3)-branch Lagrange multipliers as heavy-field content), distinct from a structureless local/τ_NL amplitude.
**Plan reference**: `sessions/investigation/investigation-13/investigation-13-plan-w1.md` §W1-1 (machinery pin, discriminant |Δ_fit|≥0.05 + feature-localization ≤5%, dual prior, in-script SOURCE-FIRST prereq).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:`):

- **script** `computations/investigation-13/inv13_w1_gge_collider_squeezed_fnl.py` — EXISTS (27,849 B). `grep` confirms both must_contain patterns:
  - `from canonical_constants import` → line 92 (`from canonical_constants import *`) + line 93 (explicit-names block).
  - `print_verdict_payload` → defined (Section 6) and called (Section 8 `main`).
- **data** `computations/investigation-13/inv13_w1_gge_collider_squeezed_fnl.npz` — EXISTS (9,082 B); 24 keys (`shape_class=ANALYTIC-LOCAL`, `verdict=INFO`, `Delta_fit=0.0`, `S_Htilde`, `S_Hfold`, `mu_Htilde`, `mu_Hfold`, dual-SHA).
- **plot** `computations/investigation-13/inv13_w1_gge_collider_squeezed_fnl.png` — EXISTS (90,917 B); 2-panel (assembled S(r) both anchors; collider exponent Δ(μ) with branch markers).
- **verdict_line** `computations/investigation-13/inv13_gate_verdicts.txt` — EXISTS; matches `^INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL:.* audit_sha256=[a-f0-9]{64}` with its dual-SHA companion row + the source-first SHA-drift extra-row (3 lines via `emit_verdict`, cross-process locked, sig_5 unique).

**MCP Pre-Compute Audit**:
- `search_knowledge("GGE bispectrum f_NL folded cosmological collider squeezed limit branch Lagrange multipliers")` → confirmed GGE-BISPECTRUM-67 (f_NL folded-triangle, HIGH); atlas-07/S39 `λ_B2=1.459, λ_B1=2.771, λ_B3=6.007` (PROVEN, analytic, SU(3)-branch); `f_NL^folded=0.1293` (S67/S83). NOT pre-closed for the *collider squeezed-limit* reading (distinct object; no prior collider-exponent gate found).
- `get_constant("lambda_B1")`, `get_constant("f_NL_folded")` → **not found** (confirmed ABSENT from `canonical_constants.py` at plan-freeze — the SOURCE-FIRST prereq is genuine).
- `get_constant("max_f_NL_FW")` → 1.505 (S95 F-NL-ROW; my own envelope — the cross-check anchor).
- `get_constant("H_tilde")` → suggests `H_tilde_canonical_TD=5.9076e-3` (S82 Branch-A); `H_fold=586.5268` (S38) found via grep. Both are the candidate collider-clock anchors.
- **SOURCE-FIRST prereq (knowledge-MCP action, run BEFORE import)**: `update_constant("lambda_B1",2.771,...)`, `update_constant("lambda_B2",1.459,...)`, `update_constant("lambda_B3",6.007,...)`, `update_constant("f_NL_folded",0.1293,...)` — all 4 added to SECTION C with PROVENANCE (atlas-07/S39 for the λ; S83 GGE-BISPECTRUM-67 for f_NL_folded). Verified import-resolved post-promotion.

**Verdict**: **INFO** — `value='ANALYTIC-LOCAL:Delta_fit=0.000000e+00'`, scheme=`AHM-collider-squeezed-limit`, convention=`RATIO`, L_max=10. `audit_sha256=1015fc17d38ae7ac5b7275a83a3dfcc6d7ca182ace72b6ce348b1e1c73409509`, `content_sha256=0a07b5ff322bf03ed3b877fcfa7257299803ce9179bc7efba41f01a9171e0e6a` (schema_version=S84+). [SIGN]=N/A (no signed Δ vs threshold; set-membership gate). Pre-registered INFO outcome under Track_B.

**Results**:

**Shape class = ANALYTIC-LOCAL** (Δ_fit = 0.0 < 0.05 discriminant; feature-localization residual = ∞, no recoverable non-analytic feature). 4-tuple `(value='ANALYTIC-LOCAL:Delta_fit=0.000000e+00', scheme=AHM-collider-squeezed-limit, convention=RATIO, L_max=10)`.

**Why local, on BOTH anchors (the decisive substrate-physics finding).** The branch dimensionless masses `μ_a = λ_Ba / H_transit` land OUTSIDE the observable cosmological-collider window `μ ~ O(1)` under either physically-motivated clock:

| Anchor | H (M_KK units) | μ_B1 | μ_B2 | μ_B3 | Series | Collider exponent | Amplitude |
|:-------|:---------------|:-----|:-----|:-----|:-------|:------------------|:----------|
| **H_tilde_TD** (PRIMARY; inflation-analog clock, S82 Branch-A) | 5.9076e-3 | 469.1 | 247.0 | 1016.8 | deep **principal** (μ≫3/2) | Δ_re=3/2, oscillatory clock μ̃≈μ | Boltzmann `e^{−πμ̃}` → **0.0** (float64 underflow; physically annihilated) |
| **H_fold** (CROSS-CHECK; literal fold Hubble, S38) | 586.53 | 4.72e-3 | 2.49e-3 | 1.02e-2 | deep **complementary** (μ≪3/2) | Δ = 3/2−√(9/4−μ²) ≈ μ²/3 ~ 10⁻⁶–10⁻⁵ | O(1) but Δ indistinguishable from the local plateau |

The principal/complementary boundary is `μ_crit = 3/2` (μ²=9/4). Under H_tilde_TD the branches are ~165–680× *above* it (Boltzmann-killed clock signal); under H_fold they are ~150–600× *below* it (massless-limit, Δ→0). Neither produces a resolvable `|Δ_fit| ≥ 0.05` non-analytic feature. The substitution-chain discriminant is verified at the **Δ=0 local null**: the assembled `S(k_long/k1) = f_NL_local + Σ_a c_a (k_long/k1)^{Δ(μ_a)}` reduces to the scale-invariant plateau `S = f_NL_folded = 0.1293` to within the 1e-6 fit-residual floor (the departure tail `|S − f_local|` is below floor ⇒ Δ_fit := 0 by convention).

**Cross-check vs the canonical envelope (PASS).** `max|S|_TD = 0.1293 ≤ max_f_NL_FW = 1.505` — the assembled bispectrum stays inside my own S95 f_NL envelope. This is consistent with the PERMANENT result that the post-transit squeezed vacuum is Gaussian-by-Wick to O(eps) with `f_NL` bounded by ±1.505 and NO non-analytic squeezed enhancement (the collider reading confirms this from an independent angle: τ_NL-amplitude-only, no collider spectroscopy).

**Substitution chain (verified at the Δ=0 null).** Def-1 `S := B(k1,k1,k_long)/[P(k1)P(k_long)]`; Def-2 `μ_a = λ_Ba/H_transit`; Def-3 (AHM 1503.08043) `Δ(μ)=3/2−√(9/4−μ²)`, oscillatory clock `μ̃=√(μ²−9/4)` for μ>3/2 with amplitude `e^{−πμ̃}`. Substitute → `S = f_NL_local + Σ_a c_a (k_long/k1)^{Δ(μ_a)}`. Simplify as k_long/k1→0: complementary terms with Δ≈μ²/3≈0 give a plateau; principal terms carry `e^{−πμ̃}≈0`. Canonical form → `S → f_NL_folded` (plateau). Direction: Δ_fit = 0 ⇒ ANALYTIC-LOCAL ⇒ INFO (the pre-registered Track_B outcome).

**Dual-prior reallocation**: INFO (Δ_fit==0 plateau) → **0.9 to Track_B (local-only)** per the plan discriminator. The GGE bispectrum is a structureless local/τ_NL amplitude with no collider non-analyticity.

**Constraint-map consequence**: closes the gen UB-2 "highest-leverage untraveled bridge" (collider spectroscopy of the GGE branch-multipliers) as a **NULL** — there is no `μ ~ O(1)` heavy field in the GGE branch content addressable by the cosmological collider, on either clock anchor. The framework predicts NO particle-content-off-CMB collider falsifier distinct from the τ_NL amplitude; the GGE non-Gaussianity is the folded-template amplitude `f_NL_folded=0.1293` and nothing more. This is a boundary, not a failure: it eliminates the collider-spectroscopy corridor and reinforces (from an independent direction) the Gaussian-by-Wick / envelope-bounded f_NL permanent result. NOTE — this NULL is recorded here; the session-track promotion (recording the UB-2 NULL in the falsifier inventory) is an action an investigation cannot perform and routes to the `/rclab-investigate --investigation 13` close.

**Source-first SHA drift (per `substrate-first-canonical-sourcing.md §(ii.B)`)**: `canonical_constants.py` plan-freeze SHA `e6829db0…bba34` → runtime SHA `e5a7587f…568a` after the 4 `update_constant` promotions (λ_B1/B2/B3, f_NL_folded). The runtime SHA enters this gate's `audit_sha256` (the plan-freeze SHA is the pre-promotion baseline); the drift is recorded in the verdict-file extra-row and the npz (`canon_runtime_sha`/`canon_plan_freeze_sha`).

Artifacts: `inv13_w1_gge_collider_squeezed_fnl.py` / `.npz` / `.png`.

---

### §W1-2. INV13-W1-2-A4-HIGHER-CURVATURE-QNM-TIDAL (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `INV13-W1-2-A4-HIGHER-CURVATURE-QNM-TIDAL`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (a₄ Seeley-DeWitt → emergent higher-curvature strong-field correction)
**Agent**: `spectral-geometer`
**Hypothesis**: The a₄ moment (a₄/a₂ = 1000:1 at the fold) generates emergent R²+Weyl²+Gauss-Bonnet corrections that shift the BH QNM ringdown off Kerr by a definite-sign δω/ω and correct the NS tidal Love number by a definite-sign δk₂/k₂, both with computable M_KK-scale magnitude and zero new free parameters.
**Plan reference**: `sessions/investigation/investigation-13/investigation-13-plan-w1.md` §W1-2 (Gilkey a₄ basis, Cardoso-EFT-ringdown shift, D_thr=1e-3 LISA/NICER floor, a_n^{ζ} regulator pin, predicted + blue-shift direction).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:`):
- **script** `computations/investigation-13/inv13_w1_a4_higher_curvature_qnm_tidal.py` — EXISTS (33,351 bytes). `grep` confirms both must_contain patterns: `from canonical_constants import` (Section 1 import of `a_2_FW_zeta, a_4_FW_zeta, M_KK, G_N, c_light, GeV_to_kg`) and `print_verdict_payload` (Section 3 + main()).
- **data** `inv13_w1_a4_higher_curvature_qnm_tidal.npz` — EXISTS (8,736 bytes); 33 keys incl. `qnm_M_BH_dwo_eps_kQNM` (8×4 grid), `ns_M_dk2_eps_k2GR` (2×4 grid), `composite='INFO'`, `sign_verdict='PASS'`, `magnitude_verdict='INFO'`, `regime_verdict='VALID'`.
- **plot** `inv13_w1_a4_higher_curvature_qnm_tidal.png` — EXISTS (192,068 bytes); 4-panel diagnostic (δω/ω vs M_BH; ε_QNM vs M_BH; RW barrier + Kretschmann localization showing δV>0 inside the barrier; summary text).
- **verdict_line** in `computations/investigation-13/inv13_gate_verdicts.txt` — matches `^INV13-W1-2-A4-HIGHER-CURVATURE-QNM-TIDAL:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row PRESENT; the `[SIGN]` 3-tuple companion row (`schema_v2_3tuple_required: true`) PRESENT (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`); 2 extra rows (regulator_pin + sign_chain).

**MCP Pre-Compute Audit**:
- `search_knowledge("a_4 higher curvature QNM ringdown tidal Love Weyl correction Seeley-DeWitt")` → hits are the plan itself + heat-kernel coefficient facts (Gilkey a_4 basis `(1/360)(5/2 R² − 2 Ric² + 2 Riem²)`, a_4(fold)=1350.72, a_4/a_2=1000:1 S20a). **NOT PRE-CLOSED** — no prior gate evaluates the QNM/tidal correction; this is the inaugural strong-field-exterior leg (distinct from inv-11 W5-2 interior construction).
- `get_constant("a_2_FW_zeta")` → 2776.165389 (S88, S88-A-N-FW-CANONICALIZATION). `get_constant("a_4_FW_zeta")` → 1350.7216 (S75). The plan's `a_2_fold`/`a_4_fold` are aliases for these zeta-regulated FW values (confirmed: not separate constants; CONST-FREEZE-42 lineage).
- `get_constant("M_KK")` → 7.428660036284456e16 GeV (S42, CONST-FREEZE-42, alias of M_KK_gravity). `list_constants("a_[024]_")` → confirms the zeta triple a_0/a_2/a_4_FW_zeta.
- Canonical pins consumed substrate-first (CONST-FREEZE-42 / S88); `G_N`, `c_light`, `GeV_to_kg` from `canonical_constants.py`; `hbar`=1.054571817e-34 (CODATA 2018) + `M_SUN_KG`=1.98841e30 added locally with provenance (= `M_sun_g`/1000).

**Verdict**: **INFO** — emitted via `emit_verdict(session=13, track="investigation", gate_id="INV13-W1-2-A4-HIGHER-CURVATURE-QNM-TIDAL", ...)`. `[SIGN]` 3-tuple: **sign_verdict=PASS · magnitude_verdict=INFO · regime_verdict=VALID** → composite collapse (gate-verdicts.md): `magnitude_verdict==INFO ⇒ composite=INFO`. audit_sha256 `86e848e88cb1b5391f084482590c8ae27cf55bc137843f8dcd46b9ac0a3dd50d`, content_sha256 `e2cc913cd12cde8c8f01cccba1183e8f4633c855e31a7a3e1f986ecd24e3ee38`.

**Results**:

**Numbers first.** Emergent higher-curvature coupling (zero new free parameters): a_4^{ζ}/a_2^{ζ} = 1350.7216/2776.165389 = **0.4865** (numerical); structural hierarchy 1000:1 (atlas-04 S5). M_KK Compton length ℓ_KK = ℏ/(M_KK c) = **2.656×10⁻³³ m**; α_HC = (a_4/a_2)·ℓ_KK² = **3.433×10⁻⁶⁶ m²**. Gilkey a_4 Weyl² coefficient on the Ricci-flat (Schwarzschild/Kerr) background: c_W = +2/360 = **+5.556×10⁻³ > 0** (Riem² coefficient inherited since Weyl²=Riem² when R=Ric=0; Gauss-Bonnet is a 4D total derivative → no local EOM).

| Observable | Value (lightest/representative) | Sign | ε coupling |
|:--|:--|:--|:--|
| δω/ω QNM l=2 (10 M_⊙) | **+4.581×10⁻⁷⁸** | + (blue-shift) | ε_QNM=1.574×10⁻⁷⁴ |
| δω/ω QNM l=2 (10⁸ M_⊙) | +4.581×10⁻⁹² | + | 1.574×10⁻⁸⁸ |
| δk₂/k₂ tidal (1.4 M_⊙, C=0.172) | **+1.324×10⁻⁷⁶** | + | ε_NS=2.384×10⁻⁷⁴ |
| δk₂/k₂ tidal (2.0 M_⊙, C=0.246) | +1.324×10⁻⁷⁶ | + | 2.384×10⁻⁷⁴ |

Composite magnitude **m = max(|δω/ω|, |δk₂/k₂|) = 1.324×10⁻⁷⁶**, vs D_thr=1×10⁻³ ⇒ **m/D_thr ≈ 1.3×10⁻⁷³ (≈73 OOM below detectability)**. GR fundamental anchor: Leaver l=2,n=0 M·ω = 0.373672 − 0.088962i; independent WKB(1) real-part cross-check 0.3890 (4.1% — confirms the GR mode is self-consistently sourced, not only quoted). QNM susceptibility k_QNM = 8.125×10⁻⁵ (from the first-order potential-perturbation overlap of the localized WKB mode with the positive-definite Kretschmann source +c_W·48M²/r⁶·f). EFT first-order regime VALID throughout (ε ≪ 1e-2 by ~72 OOM).

**[SIGN] substitution chain (substituted numbers, read off the canonical form):**
- Step 1: a_2 = a_2_FW_zeta = 2776.165389 (a_2^{ζ}, CONST-FREEZE-42 / S88) — emergent Einstein-Hilbert, G_N⁻¹ ~ a_2 M_KK².
- Step 2: a_4 = a_4_FW_zeta = 1350.7216 (a_4^{ζ}, S75) — emergent higher-curvature; a_4/a_2 = +0.4865 > 0.
- Step 3: c_W = +2/360 > 0 (Gilkey Riem² coeff, Ricci-flat). On Schwarzschild R=Ric=0 ⇒ Weyl² source = Kretschmann = +48M²/r⁶ > 0, localized INSIDE the RW barrier (panel c).
- Step 4 (canonical form): δω/ω = + |c_W (a_4/a_2) k_QNM| · (α_HC/M_geo²) / (2 Re(ω)²). sign(δω/ω) = sign(c_W)·sign(a_4/a_2)·sign(k_QNM) = **(+)·(+)·(+) = +** (a positive Weyl² coupling STIFFENS the Regge-Wheeler potential ⇒ raises Re(ω) ⇒ blue-shift). δk₂/k₂ inherits the same c_W>0 in the static l=2 response ⇒ **+** (star marginally more deformable).
- **sign_verdict=PASS**: all computed signs match the pre-registered + (blue-shift) direction.

**Regulator pin** (companion row): a_4^{ζ} + a_2^{ζ} (zeta-regulated Seeley-DeWitt; a_2_FW_zeta=2776.165389, a_4_FW_zeta=1350.7216; bare a_n FORBIDDEN per `regulator-pin-discipline.md`).

**Internal consistency note (factor-counting, methodology-mandated):** the script normalizes ε by M_geo² = (GM/c²)² (geometrized mass, the natural M=1 QNM scale); an r_S² = (2GM/c²)² = 4·M_geo² normalization differs by exactly factor 4 (verified). Both are legitimate geometrized scales; the M=1 QNM convention (M·ω) is the script's choice. The OOM (ε ~ 10⁻⁷⁴–10⁻⁷⁵) and the verdict (INFO, sign PASS, ~73 OOM sub-detectable) are invariant to this factor — Sage-cross-checked.

**4-tuple**: `(value='dwo_max=4.581e-78_dk2_max=1.324e-76_m=1.324e-76_Dthr=1e-03_sign=+blue-shift_a4a2=0.4865', scheme=Gilkey-a4-heat-kernel-basis+Cardoso-EFT-ringdown, convention=RATIO, L_max=N/A)`.

**Constraint-map consequence** (per the plan rubric, INFO branch): the framework predicts a **definite-sign (positive, blue-shifting) QNM ringdown deviation and a definite-sign (positive) tidal-Love deviation** with magnitude set ENTIRELY by the canonical a_4/a_2 and M_KK — **zero new free parameters** — but the magnitude (≈10⁻⁷⁶) is ~73 OOM below the LISA/NICER detectability floor. This is a **clean, falsifiable NULL**: the empty compact-object sector gains a definite SIGN prediction from the a_4 moment that current detectors cannot resolve. It is a pre-registered, expected outcome under Track_B (the a_4/a_2 × M_KK⁻² suppression is OOM-large), reallocating prior mass to "definite-sign sub-detectable" — NOT an incomplete result and NOT a substrate falsification. The suppression is the universal (ℓ_fundamental/r_observable)² hierarchy: ℓ_KK ≈ 2.7×10⁻³³ m vs r_S ≈ 3×10⁴ m for a 10 M_⊙ BH (~37 decades, squared → ~74 OOM). **Substrate-first framing**: the a_4 moment IS the substrate's higher-curvature content; GR (the a_2 term) is the leading consequence; the QNM ringdown and tidal Love number are the laboratory-IN images of the substrate's fourth spectral moment under the heat-kernel/spectral-action bridge map (we do NOT add R² corrections to GR — the substrate's spectral moments generate both). The 1000:1 a_4/a_2 hierarchy is the substrate's own scale separation (16-component spinor on the 8-manifold), refracted into a strong-field observable with M_KK as the sole scale.

**Dual-prior reallocation**: INFO (definite-sign, m < D_thr) → **0.9 to Track_B (definite-sign sub-detectable future-falsifier null)** per the plan discriminator. The a_4 strong-field correction is real and sign-definite but OOM below current detector reach.

**Dual-SHA**: audit_sha256 `86e848e88cb1b5391f084482590c8ae27cf55bc137843f8dcd46b9ac0a3dd50d` · content_sha256 `e2cc913cd12cde8c8f01cccba1183e8f4633c855e31a7a3e1f986ecd24e3ee38`. **Artifacts**: `inv13_w1_a4_higher_curvature_qnm_tidal.py/.npz/.png`.

---

### §W1-3. INV13-W1-3-BRANCH-IV-W0-L1516-DR3 (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `INV13-W1-3-BRANCH-IV-W0-L1516-DR3`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (DR3-class L_max-stability of the branch-(iv) w₀ secondary prediction)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: Pushing the branch-(iv) spectral-triple-direct w₀(L) evaluator to L_max ∈ {15,16} converges the CAC cross-L_max spread below the 0.025 PASS band (R_842-window secondary prediction is truncation-stable, DR3-ready), or it stays in the 0.025–0.05 INFO band (reproduces w₀_B but does not converge below the Friedrich-Bär envelope).
**Plan reference**: `sessions/investigation/investigation-13/investigation-13-plan-w1.md` §W1-3 (S106 high-L cache feasibility-lift, CAC binding form MANDATORY, offset-cancellation cross-check, moment-sentinel bit-exact pre-check).

**Verdict**: **FAIL** — `spread_CAC = 0.0629703` over L ∈ {12,13,14,15,16}, **> 0.05 INFO ceiling** (band: PASS ≤ 0.025 / INFO (0.025, 0.050] / FAIL > 0.050). Emitted via `emit_verdict(session=13, track="investigation", …)`; `audit_sha256=ffafc349b81ad4239c87a982978d6be3566af671838cdd32bc884a2fe1072c9e`, `content_sha256=8fe9003b8afea1b222844786e155ea6820df63e0e7830c5559b9ab40284700a4`. The deep-truncation set **DIVERGES rather than converges** — adding L=15 (the genuinely-new point; L=16 is FB-saturated ≡ L=15) GREW the spread by +0.018456 (the S105 hope that the Friedrich-Bär tail pulls the spread below 0.025 is falsified). This is a truncation-instability finding **on the L_max axis ONLY**; it is NOT a branch-(iv) survival retraction (the derivation-admissibility was separately closed at `S101-W0-BRANCH-IV-EVALUATOR`, INFO; this gate tested only whether the secondary R_842-window prediction is truncation-stable). All consistency guards PASS (`guard_ok=True`); the FAIL is a robust, well-cross-checked divergence on a settled-derivation branch.

**Results**:

**Numbers first** (per-L branch-(iv) Zubarev moment ρ_B(L) and CAC-anchored late-time w₀^CAC(L)):

| L (= p+q) | ρ_B(L) (Zubarev branch-IV moment) | w₀^CAC(L) = ρ_B(L) + offset_B | n_modes (w/ mult) | data path |
|:----------|:----------------------------------|:------------------------------|:------------------|:----------|
| 10 (anchor) | −0.575207 | −0.918000 (= w₀_FW EXACTLY) | 80,080 | L14-dict |
| 12 | −0.633204 | −0.975997 | 168,896 | L14-dict |
| 13 | −0.656884 | −0.999678 | 236,096 | L14-dict |
| 14 | −0.677718 | −1.020511 | 323,136 | L14-dict |
| **15** | **−0.696174** | **−1.038968** | 434,112 | **L16-dict ≤15 (NEW)** |
| 16 | −0.696174 | −1.038968 | 434,112 | L16-dict ≤16 ≡ ≤15 (FB-saturated) |

- **Spread (the gate):** `spread_CAC = max_L w₀^CAC(L) − min_L w₀^CAC(L) = 0.0629703` over {12,…,16} → **FAIL** (> 0.05). Recomputed {12,13,14}-only window = 0.044514 (continuous with the S105 record 0.0443091; INFO band — see (4,4)-completeness note below); the L=15 point added **+0.018456** to the spread (it is the new minimum; ρ_B argmin at L=15, argmax at L=12).
- **Monotone-decreasing, decelerating-but-NOT-closing:** decrements ρ_B(13)−ρ_B(12) = −0.023680, ρ_B(14)−ρ_B(13) = −0.020834, ρ_B(15)−ρ_B(14) = −0.018456 (15→16 = +0.000000 by FB-saturation). The decrement magnitude shrinks but the moment keeps falling — the truncation envelope does not close before the band; Track_B ("saturated-not-converged", prior 0.5) is *under*-shot, the data are divergent rather than merely non-converged. Posterior reallocates to the FAIL branch (deep-truncation moments diverge).
- **4-tuple:** `(value=spread_CAC=0.0629703, scheme=zeta [Zubarev late-time], convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max={12,13,14,15,16})`. **CAC binding-form tag MANDATORY** per `regulator-convention-lockdown.md` — `w₀^CAC(L=10) = ρ_B(10) + (w₀_FW − ρ_B(10)) = w₀_FW = −0.918` EXACTLY (`cac_anchor_resid = 0.0e+00`; effacement-preservation criterion satisfied by construction). RDC (no offset) is OUTSIDE the admissibility class and FORBIDDEN.
- **Offset-cancellation identity (the substitution-chain core, [VERIFY] cross-check):** offset_B = w₀_FW − ρ_B(10) = −0.342793 is **L-INDEPENDENT** ⇒ it cancels exactly in the difference: `spread_CAC = max_L[ρ_B(L)+offset_B] − min_L[ρ_B(L)+offset_B] = max_L ρ_B(L) − min_L ρ_B(L) = spread_rho`. Verified: `spread_CAC = 0.06297029148561906`, `spread_rho = 0.06297029148561917`, `|spread_CAC − spread_rho| = 1.11e-16` (machine epsilon). The CAC-vs-RDC choice does NOT change the spread (only the per-L anchored values); CAC is mandatory because the per-L w₀^CAC(L) ARE the DR3-comparable late-time predictions. Cross-report: OFFSET_ZUBAREV_S86 = −0.340827 (diff vs runtime offset_B = 1.97e-3, the (4,4)-completeness shift).
- **L_max_plan = {14,16}, L_max_operational = 15** (recorded in npz per `math-scripts.md` §"D_K Block-Diagonality" item 3). L=16 is **Friedrich-Bär-saturated at operational L=15**: the 17 level-16 sectors (p+q=16) are FB-bounded (`eta_FB_lower=0.3928`; their |λ|_min ≥ eta_FB_lower·√(C₂+1) exceeds the bottom-K observable ceiling), absent from the cache → `|ρ_B(16) − ρ_B(15)| = 0.0e+00` EXACTLY. This is NOT a PRE-REG-INC fallback; cache-existence IS the Casimir cross-check.
- **Moment-sentinel (MANDATORY, GATING — ran BEFORE consuming any new sector):** ρ_B(8,10,12) recomputed on the s84 cache vs the EXPECT_RHO anchors → `max_diff = 0.00e+00` (bit-exact; SENTINEL_TOL=1e-10). The Zubarev evaluator is self-consistent. S106's own GT-vs-cache spectral sentinel (inherited, NOT re-run) = 7.51e-14, ok.
- **(4,4)-completeness reconciliation:** the S106 dicts are the COMPLETE per-level union (every (p,q) with p+q≤L present); the s84 cache was missing ONE level-8 sector (4,4) (8/9 sectors at level 8 — an S84-era gap S106 rebuilt, dim=125, 2000 eigenvalues, listed in S106 `build_times_json`). Hence ρ_B(12) on the COMPLETE S106 dict (−0.633204) differs from the s84-INCOMPLETE evaluation S105 recorded by 1.68e-3. This is a **sector-set difference (both correct on their own set), NOT an evaluator failure**. Apples-to-apples continuity: ρ_B(12) on the SAME incomplete s84 set = −0.634885 = S105 record EXACTLY (`rho12_continuity_s84 = 0.00e+00`). The complete-set evaluation (p+q≤L literally = all such sectors) is the canonical truncation; this gate uses it.
- **Cache-consistency cross-checks:** L14-dict vs L16-dict shared-sector |λ| agreement over 120 sectors = 0.0e+00; s84 vs S106-L16 overlap over 90 sectors = 0.0e+00.
- **Substrate-first framing:** w₀ IS a spectral moment of the substrate (the Zubarev branch-(iv) Mellin-zeta moment ρ_B of D_K's eigenvalue spectrum at τ_fold, Level-1 single-τ-slice substrate-IS); its truncation-stability under L_max → {15,16} is the substrate's own convergence to its continuum image. The arrow runs D_K eigenvalues → ρ_B(L) → CAC-anchored late-time w₀ → DESI DR3 w₀–w_a — we do NOT fit w₀ to a cosmological model. The FAIL says: this substrate-IS moment, on the branch-(iv) channel, does NOT stabilize under deep truncation — the secondary R_842-window prediction is not DR3-defensible on this branch.
- **Functional-sensitivity note (Lizzi, SCHEME-DEPENDENT):** spread_CAC is a property of the **Zubarev (heat-kernel-Gaussian-weighted) late-time functional** ρ_B = ⟨|λ|⟩_Z/λ_max − 1, where w_Z = exp(−|λ|²/Λ_Z²), Λ_Z=1.0 M_KK. The divergence is a statement about THIS spectral functional's truncation behavior on the branch-(iv) channel — classified **SCHEME-DEPENDENT** (the late-time w₀ moment-functional choice is itself a regularization degree of freedom; a different late-time functional could in principle converge where Zubarev diverges). But the CAC lockdown pins the functional for DR3-class gates, so within the pre-registered scheme the divergence IS the canonical result. The offset-cancellation identity (spread invariant under the CAC↔RDC additive-anchor choice) is **FUNCTIONAL-INDEPENDENT** — it holds for any additive anchor by construction (algebraic, machine-ε).

**Constraint-map consequence:** the branch-(iv) w₀ secondary (R_842-window) prediction is **truncation-unstable on the L_max axis** — it cannot be defended as a stable w₀ against the ~2027 DESI DR3 w₀–w_a measurement on this branch. This closes the optimistic Track_A (Friedrich-Bär tail converges below 0.025) as falsified and updates the EVOI Q37 (DESI DR3 / branch-iv) register from "S105 INFO, GT-builder-landed, FB-envelope-bounded" to "deep-truncation DIVERGES at L∈{12,…,16}". The finding is orthogonal to (and does NOT retract) the separately-settled branch-(iv) derivation-admissibility (`S101-W0-BRANCH-IV-EVALUATOR`). Session-track promotion (EVOI Q37 update + branch-iv truncation-status) is an investigation-track-boundary action routed to the `/rclab-investigate --investigation 13` close per `gate-verdicts.md §"Investigation-Track Canonical Path"`.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:`):
- **Script** `computations/investigation-13/inv13_w1_branch_iv_w0_l1516_dr3.py` (41,154 B) — `grep -E 'from canonical_constants import'` → `from canonical_constants import (` ✓; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + call site ✓.
- **Data** `computations/investigation-13/inv13_w1_branch_iv_w0_l1516_dr3.npz` (14,945 B, 70 keys) — present, non-optional; carries `verdict=FAIL`, `spread_CAC=0.06297029…`, `spread_rho`, `offset_cancellation_residual=1.11e-16`, `cac_anchor_resid=0.0`, `rho16_eq_15=0.0`, `L_max_plan=[14,16]`, `L_max_operational=15`, `guard_ok=True`, dual-SHA.
- **Plot** `computations/investigation-13/inv13_w1_branch_iv_w0_l1516_dr3.png` (89,907 B) — present, non-optional; 2-panel (ρ_B(L) trajectory with L=15/16 highlighted; w₀^CAC(L) with FAIL-band frame).
- **Verdict line** `computations/investigation-13/inv13_gate_verdicts.txt` — canonical line matches `^INV13-W1-3-BRANCH-IV-W0-L1516-DR3:.* audit_sha256=[a-f0-9]{64}` ✓, with dual-SHA companion row + 2 annotation rows (regulator_pin a₂^{Mellin} poleconv-A-double; L_max-plan/operational + FB-saturation + canonical-drift §(ii.B)).

**MCP Pre-Compute Audit** (queries executed before writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("branch-iv w0 DR3 CAC spread truncation L_max stability")` → confirmed prior state: `S105-BRANCH-IV-DIRECT-L1314` INFO at spread_CAC=0.0443091 over {12,13,14}; `S103-BRANCH-IV-DEEP-TRUNCATION` FB-envelope INFO; the CAC offset-cancellation equation `spread = max_L ρ_B(L) − min_L ρ_B(L)`; EVOI Q37 (DESI DR3 / branch-iv). NOT pre-closed — this gate extends the L-window, a genuine new computation.
- `get_constant("w0_FW")` → **−0.918** (S58 four-fold-lock, Volovik vacuum partition + effacement Γ_eff=0.99970). The CAC L=10 anchor. (Plan-text name `w_0_FW` not found; canonical name is `w0_FW`.)
- Input-SHA verification: s84 cache (`9e6d9cf7…` ✓ matches plan pin), S106 high-L cache (`e6bc3af8…` ✓), S105 evaluator (`10119df9…` ✓). `canonical_constants.py` runtime SHA `e5a7587f…` drifted from plan-freeze baseline `e6829db0…` — EXPECTED per `substrate-first-canonical-sourcing.md §(ii.B)` (W1-1 update_constant prereq + in-session promotions); w0_FW value −0.918 unchanged; runtime SHA pinned into the closure hash + documented in the verdict annotation row.

---

## Wave 1 Synthesis (team-lead)

Three mutually-independent cross-domain compute gates (the inv-1…inv-12 dedup survivors) closed: **2 INFO + 1 FAIL**. None is a substrate falsification; each maps a distinct boundary on the constraint surface, and the two INFOs are pre-registered Track_B outcomes (not incomplete results).

**Per-gate — what was computed, what region it constrains:**

- **§W1-1 GGE collider (INFO, ANALYTIC-LOCAL).** The squeezed-limit bispectrum reduces to the scale-invariant plateau `S → f_NL_folded = 0.1293`; Δ_fit = 0 on BOTH physically-motivated clock anchors (under H_tilde_TD the branch masses μ_a∈[247,1017] are deep-**principal**, Boltzmann-killed `e^{−πμ̃}→0`; under H_fold μ_a∈[2.5e-3,1.0e-2] are deep-**complementary**, Δ≈μ²/3~10⁻⁶ — indistinguishable from the local plateau). **Constrains:** closes gen UB-2 (the survey's named "highest-leverage untraveled bridge", collider spectroscopy of the GGE branch-multipliers) as a **NULL** — no μ~O(1) heavy field in the GGE branch content is addressable by the cosmological collider on either clock. Reinforces, from an independent direction, the Gaussian-by-Wick / f_NL-envelope-bounded permanent result (`max|S|=0.1293 ≤ max_f_NL_FW=1.505`).

- **§W1-2 a₄ higher-curvature QNM/tidal (INFO, definite-sign sub-detectable null).** `sign_verdict=PASS`: a definite **+ (blue-shift)** QNM correction and **+** tidal-Love correction, sign read off the canonical form `sign(δω/ω)=sign(c_W)·sign(a₄/a₂)·sign(k_QNM)=(+)(+)(+)`. Magnitude m=1.324×10⁻⁷⁶ ≪ D_thr=10⁻³ (~73 OOM below the LISA/NICER floor), zero new free parameters. **Constrains:** the empty compact-object sector gains a definite **SIGN** prediction from the a₄ moment that current detectors cannot resolve — a clean falsifiable future-null. The (ℓ_KK/r_obs)² ≈ 74-OOM suppression is the structural reason; the prediction is real, not absent.

- **§W1-3 branch-iv w₀ DR3 (FAIL, truncation-divergent).** spread_CAC=0.0629703 over L∈{12..16} > 0.05 FAIL ceiling; adding L=15 GREW the spread by +0.018456 (it is the new minimum; L=16 FB-saturated ≡ L=15). The S105 hope that the Friedrich-Bär tail pulls the spread below 0.025 is **falsified**: ρ_B is monotone-decreasing with decelerating-but-not-closing decrements. **Constrains:** the branch-(iv) w₀ secondary (R_842-window) prediction is **truncation-unstable on the L_max axis** — not DR3-defensible on this branch against the ~2027 DESI DR3 w₀–w_a measurement. **Scope:** L_max axis ONLY — does NOT retract branch-(iv) derivation-admissibility (separately closed at `S101-W0-BRANCH-IV-EVALUATOR`). The offset-cancellation identity held to machine-ε (`|spread_CAC − spread_rho| = 1.11e-16`) — the functional-independent structural core; CAC anchor exact (`w₀^CAC(L=10)=w₀_FW=−0.918`, resid 0.0).

**What changed (`output-standards.md` numerical-vs-structural split):**

- *(a) Numerical revisions:* spread_CAC `0.0443091` (S105, {12,13,14}) → `0.0629703` ({12..16}); Δ_fit confirmed `0`; QNM/tidal magnitude `m=1.324e-76`, a₄^{ζ}/a₂^{ζ}=0.4865.
- *(b) Structural changes:* UB-2 collider-spectroscopy corridor `untraveled` → **CLOSED-as-NULL**; branch-iv w₀ DR3-readiness `S105 INFO / FB-envelope-bounded` → **deep-truncation DIVERGES** (optimistic Track_A falsified).

## Carry-Forward Computations

**No carry-forwards: all Wave-1 outcomes closed in-session.** Two pre-registered Track_B nulls (W1-1 ANALYTIC-LOCAL; W1-2 definite-sign sub-detectable) and one well-cross-checked FAIL on a CAC-pinned scheme (W1-3) — none yields a fillable 4-field compute item. W1-3's SCHEME-DEPENDENT classification does NOT license a functional-shopping CF (the CAC lockdown pins the Zubarev late-time functional for DR3-class gates; re-running under an alternative functional to seek convergence would be `v3-closure-recovery.md` Class-6-adjacent iterate-until-PASS, not a legitimate forward compute).

The three **session-track promotions** named in the plan's terminal decision point are investigation-track-boundary actions an investigation CANNOT perform (`gate-verdicts.md §"Investigation-Track Canonical Path"`); they route to the `/rclab-investigate --investigation 13` close as housekeeping-ledger lift candidates (logged in `investigation-13-housekeeping.md §B`), NOT into this CF block: (1) UB-2 collider NULL → falsifier-inventory record (mack sole-writer); (2) W1-2 definite-sign sub-detectable strong-field falsifier → candidate falsifier-master-inventory row constraining M_KK; (3) W1-3 → EVOI Q37 (DESI DR3 / branch-iv) update from "S105 INFO / FB-bounded" to "deep-truncation DIVERGES".

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-17 | gen UB-2 GGE cosmological-collider spectroscopy | untraveled "highest-leverage bridge" | **CLOSED-as-NULL** (INV13-W1-1) | branch masses off the μ~O(1) collider window on both clock anchors; Δ_fit=0; τ_NL-amplitude-only |
| 2026-06-17 | a₄ higher-curvature QNM/tidal (strong-field exterior) | untested | **definite-sign sub-detectable null** (INV13-W1-2) | + blue-shift + tidal, m≈10⁻⁷⁶ ≪ 10⁻³; zero free params; falsifiable SIGN, OOM below reach |
| 2026-06-17 | branch-iv w₀ DR3-readiness (L_max axis) | S105 INFO 0.0443091 / FB-envelope-bounded | **FAIL — deep-truncation DIVERGES** (INV13-W1-3) | spread_CAC 0.0630 > 0.05; L=15 grows spread; Track_A falsified; branch-iv derivation-admissibility UNAFFECTED (S101) |
| 2026-06-17 | s84 cache `s84_spectrum_cache_L12_tau019.npz` completeness (process observation) | assumed complete | **missing level-8 (4,4) sector (S84-era gap; S106 rebuilt)** | ρ_B on complete S106 union vs s84-incomplete S105 basis differ 1.68e-3 = sector-set difference, NOT evaluator drift; complete S106 union is canonical truncation. Documented WP §W1-3 + lizzi memory |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| INV13-W1-1 | `inv13_w1_gge_collider_squeezed_fnl.py` (27.8 KB) | `…_fnl.npz` (9.1 KB) | `…_fnl.png` (90.9 KB) | INFO |
| INV13-W1-2 | `inv13_w1_a4_higher_curvature_qnm_tidal.py` (33.4 KB) | `…_tidal.npz` (8.7 KB) | `…_tidal.png` (192.1 KB) | INFO (sign=PASS) |
| INV13-W1-3 | `inv13_w1_branch_iv_w0_l1516_dr3.py` (41.2 KB) | `…_dr3.npz` (14.9 KB) | `…_dr3.png` (89.9 KB) | FAIL |

All under `computations/investigation-13/`; verdicts in `inv13_gate_verdicts.txt` (dual-SHA, sig_5 unique; W1-2 carries the [SIGN] 3-tuple companion row).
