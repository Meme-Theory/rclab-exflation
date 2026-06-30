# Investigation 8 Wave 2 — The Dimensionful-Scale Knot, Precision-GR & Quantum Foundations (Results Working Paper)

**Investigation**: 8 | **Wave**: 2 | **Plan**: investigation-8-plan-w2.md | **Track**: investigation (verdict file `computations/investigation-8/inv8_gate_verdicts.txt`) | **Theme**: principle-theoretic attack on the single dimensionful-scale dof — Jacobson entanglement-equilibrium → CC magnitude, emergent PPN/MICROSCOPE-η falsifier, Born-rule derive-or-no-go, running-vacuum c₁ vs substrate n=2.

## Gate Sections

### §W2-1. INV8-W2-1 (einstein-theorist)

**Status**: COMPLETED
**Gate ID**: `INV8-W2-1`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the CC IS the a₀ spectral moment; the entanglement entropy IS the GGE half-trace; the modular flow IS Tomita-Takesaki on A_hor)
**Agent**: `einstein-theorist`
**Hypothesis**: Imposing entanglement equilibrium (δS_ent = 0 at fixed causal-diamond volume) on the GGE entanglement entropy read through the §VII.BZ modular weight `A_hor = A_K ⋊_{σ^ω} ℝ` fixes a CC magnitude Λ_substrate, attacking JACOBSON-NONLOCAL-64.

**Verdict**: **FAIL** (composite). 3-tuple: **sign=PASS** (Λ_substrate > 0, de-Sitter-like, sign-consistent with the observed positive ρ_Λ) / **magnitude=FAIL** (D_OOM = 53.60 ≫ 3.0 info-band ceiling) / **regime=VALID** (small-diamond regime holds across the entire ℓ scan window, frac_valid = 1.000). Composite collapse (gate-verdicts.md, PRE-REGISTERED): `magnitude=FAIL ∧ regime=VALID ⇒ FAIL`. This is the **informative FAIL** the plan's FAIL_meaning rubric anticipates — the entanglement-equilibrium corridor does NOT recover the CC magnitude to ≤1 OOM, so the absolute magnitude (G-2) stays in the a₀·M_KK⁴ normalization and JACOBSON-NONLOCAL-64 remains open *from this side*. The route is nonetheless a strong partial constraint: it closes ~62 of the bare 116-OOM gap (see Results).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/investigation-8/inv8_w2_1_jacobson_entanglement_equilibrium_cc.py` — script (contains `from canonical_constants import`, `print_verdict_payload`). EXISTS.
- `computations/investigation-8/inv8_w2_1_jacobson_entanglement_equilibrium_cc.npz` — data. EXISTS.
- `computations/investigation-8/inv8_w2_1_jacobson_entanglement_equilibrium_cc.png` — plot (OOM-gap ladder + diamond scan + S_ent disclosure). EXISTS.
- `computations/investigation-8/inv8_gate_verdicts.txt` — canonical verdict line `INV8-W2-1: FAIL ... audit_sha256=241d15b06c492d02…a687418` (64-hex) + dual-SHA companion row + schema-v2 [SIGN] 3-tuple row + regulator-pin / S_ent-disclosure / routes / composite extra-rows. EXISTS.
- `audit_sha256 = 241d15b06c492d02d3a1155454d816b5eb3e0e347b05eafd00bb02c42a687418`; `content_sha256 = 2d4ca396f8f1c2980c0d665abc7fd573c883f6d2a2a6faade253b250173122c9`.
- (grep confirmations pasted in the closure checklist at the foot of this section.)

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge('Jacobson entanglement equilibrium cosmological constant')` → S62 `Λ_Jacobson ~ T_U × dS_ent/dA ~ T_U × 1.10 × M_KK²` (QR2.11); S64 `Λ = Λ_SA = (f_0/f_2)(a_0/a_2)Λ_sp²` (SA-VERSUS-JACOBSON-64); `Cosmological constant family` class (a₀ vs ρ_Λ, ~10¹²⁰ ratio). **Not PRE-CLOSED** — the entanglement-equilibrium *variation* magnitude functional is distinct.
- `trace_entity('JACOBSON-NONLOCAL-64')` → the open CC/A_s-magnitude gate; `R₁ = a₀a₄/a₂² = 1.12865`; gauge-vs-gravity M_KK incompatibility framing. Confirms target gate OPEN.
- `search_knowledge('VII.BZ crossed product modular weight horizon faithfulness')` → **K12** (S105) §VII.BZ BDI Horizon-Faithfulness, faithful normal modular weight ω|_{A_hor} on `A_hor = A_K ⋊_{σ^ω} ℝ`, STAGE-3-PERMANENT (S105–S106, blind Stage-2 PASS-AND). The modular machinery this gate consumes EXISTS and is permanent.
- `search_knowledge('DILUTION-CC cosmological constant magnitude OOM gap')` → DILUTION-CC: 114-OOM gap closed to 0.01 OOM via Volovik tracking vacuum, `rho_vac/rho_obs = 1.032`, `CC_OOM = 115.5` (S66 W1-A PROVEN). DIFFERENT (equilibrium-departure) route; the entanglement-equilibrium route is independent.
- `get_constant`: `a_0_FW_zeta = 6440.0`, `a_2_FW_zeta = 2776.165389`, `M_KK = 7.428660036284456e16` GeV, `rho_Lambda_obs = 2.7e-47` GeV⁴, `M_Pl_reduced = 2.435e18` GeV, `CC_OOM = 115.5`, `f_2_default = 2.34` (`f_0`/`f_2`/`Lambda_sp` absent → f_0/f_2 = 1 Gaussian-cutoff per S64; Λ_sp = M_KK). All a_n carry the `a_n^{ζ}` regulator pin.
- **Cross-investigation dedup** (per seed §"Cross-investigation dedup"): DISTINCT functional from inv-4 (Euclidean replica → ¼ area coefficient), inv-5 (entropy-functional a₀/a₂), inv-7 (modular-horizon S∝A/4G) on the SAME §VII.BZ crossed product — here the *entanglement-equilibrium VARIATION* reads off the MAGNITUDE.

**Results**:

**Canonical deliverable**: `D_OOM = 53.5961` (4-tuple `(value=53.5961, scheme=FW-zeta, convention=ABSOLUTE, L_max=10)`). `Λ_substrate = 8π G_eff (δS_ent/δV) > 0` (sign computed +1; de-Sitter-like). Anchor: substrate-first causal-diamond half-trace `S_diamond = 0.1384 nats` (W1-1 fallback; see below).

**Substitution chain with substituted numbers** (the [SIGN] directional pre-registration):
- Step 2 — Newton coupling (PB-8): `G_eff⁻¹ = Λ_cutoff² f_2 a_2 = (7.4287e16)² · 2.34 · 2776.165389 = 3.5849e37 GeV²` ⇒ `G_eff = 2.789e-38 GeV⁻²` > 0. `a_0 = 6440`, `a_2 = 2776.165389` (both `a_n^{ζ}`).
- Step 3 — matter entanglement: `S_ent(GGE, ℓ)` = causal-diamond half-trace of ρ_GGE = `0.1384 nats` (substrate-first B1+B3 sub-region). Bogoliubov amplitudes `u=0.93248734, v=0.36120266` (s52, AMP-52, SHA ecfbce08…).
- Step 5 — released volume variation: `Λ_substrate = 8π G_eff [δS_ent/δV]_eq = (8π / (Λ_cutoff² f_2 a_2)) · [δS_ent/δV]`, with `δS_ent/δV = S_anchor · M_KK³ = 5.672e49 GeV³`.
- Step 6 — **sign read-off**: `δS_ent/δV > 0` (entanglement entropy increases with diamond volume — more modes inside, more boundary entanglement) ∧ `G_eff > 0` ∧ `8π > 0` ⇒ **Λ_substrate > 0** (de-Sitter-like positive CC, sign-consistent with the observed positive ρ_Λ). **sign_verdict = PASS** (Sage-verified, all factors positive).

**Two dimensionalization routes** (the gap depends entirely on WHICH magnitude the modular flow selects):
- **ROUTE 1 — bare a₀ spectral-action variation** (NOT this gate's functional): `Λ_SA = (f_0/f_2)(a_0/a_2)M_KK² = 1.280e34 GeV²`; `ρ_SA = Λ_SA M_Pl²/8π = 3.020e69 GeV⁴`; `D_OOM_bare = 116.05`. Reproduces the canonical NAIVE 114–115.5-OOM gap (S64 Eq. 13) — the object DILUTION-CC closes via Volovik tracking. Entanglement equilibrium does NOT integrate a₀ over the 4-volume, so it does NOT incur this gap.
- **ROUTE 2 — Jacobson-2015 entanglement-equilibrium** (the gate's functional, CANONICAL): `ρ_ent = T_modular · (δS_ent/δV)` with `T_modular = T_U = H_0/2π = 1.878e-43 GeV` (present-day comoving Unruh temp) and `δS_ent/δV = 5.672e49 GeV³` ⇒ `ρ_ent = 1.065e7 GeV⁴` ⇒ **`D_OOM_ent_cosmo = 53.60`**. Closes **~62 of the bare 116 OOM** (116.05 − 53.60), leaving ~54 OOM — a strong partial-magnitude constraint but NOT a ≤1-OOM closure.

**Dimensional-rigor finding (principle-theoretic)**: the S62 workshop (QR2.13) claimed a **17-OOM residual** for the Jacobson route, but that estimate was **dimensionally inconsistent** — it divided `Λ_Jac` (dim GeV²) directly by `M_Pl⁴` (GeV⁴) and read the resulting GeV⁻² quantity as a pure ratio. The dimensionally-correct area-law magnitude (`ρ = Λ·M_Pl²/8π`) is `D_OOM_ent_area = 55.23`, and the volume form gives `D_OOM = 53.60`. The Jacobson-2015 entanglement-equilibrium route, done with dimensional consistency, leaves a **~54-OOM** residual, not 17. *Everything must be made as simple as possible, but not simpler* — and not dimensionally inconsistent.

**The S_ent three-entropy disclosure** (plan-mandated; three *different* entropies of three *different* objects):
1. `S_ent = 0.000` nats — global BCS entanglement (product state in the R-G eigenbasis; ENT-39).
2. `S_GGE = 1.6875` nats — full 8-mode von-Neumann (per-mode-occupation form; the plan cites `2.2125` for the full Richardson-Gaudin many-body von-Neumann including pair correlations, a slightly different functional — disclosed as such, not in conflict).
3. `S_diamond = 0.1384` nats — the **causal-diamond half-trace** (B1+B3 sub-region of the 8-mode GGE), which is what Jacobson's diamond variation needs. (W1-1 seed `1.039` and the S62 free-fermion reference `8×0.138 = 1.104` are also disclosed.) **The diamond uses the half-trace (3), never the global BCS (1) or the full von-Neumann (2)** — the permanent lesson "NEVER confuse S_vac (kinematic) with S_matter (the GGE causal-diamond half-trace)."

**W1-1 fallback disclosure**: the only `INV8-W1-1*` verdict on disk is `INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM: FAIL` (value `I_PBH = 1.80e-299`, a PBH/fold-transit-spectrum producer — it emitted NO usable causal-diamond `S_ent`). Per the plan §"Discipline on the S_ent discrepancy" (the W1-1 `S_ent` is an INPUT VALUE, not a structural prerequisite, so the gate is runnable regardless), the diamond is anchored by the **substrate-first half-trace** `S_diamond = 0.1384 nats` (s52 B1+B3), `fallback_active = True`. The fallback shifts D_OOM only marginally (53.60 with `0.1384` vs 54.47 with `1.039`) — the ~54-OOM verdict is robust to the anchor choice.

**Constraint-map consequence**: the FAIL **closes the entanglement-equilibrium corridor to the CC magnitude** at ≤1 OOM — entanglement equilibrium on the substrate's own modular flow (§VII.BZ) does NOT transfer to the absolute CC magnitude. The CC magnitude remains in the `a₀·M_KK⁴` normalization (consistent with the standing 110–115-OOM gap living entirely there); JACOBSON-NONLOCAL-64 stays OPEN from this side. What the FAIL *positively* establishes: (i) the **sign** is structurally fixed positive (de-Sitter), independent of the magnitude route — a genuine principle-theoretic result; (ii) the modular machinery built for horizon-faithfulness does **not** carry the magnitude, isolating the residual to the `T_modular × δS_ent/δV` dimensionalization (the substrate's internal vs cosmological modular temperature is the open lever); (iii) the prior S62 "17-OOM" closure claim is corrected to ~54 OOM. Per `evoi-prioritization.md`, a FAIL that eliminates a corridor STRENGTHENS the surviving DILUTION-CC (Volovik-tracking) route, the framework's only ≤1-OOM CC-magnitude mechanism.

**Substrate-first assessment**: the CC IS the a₀ spectral moment of D_K — NOT a bare vacuum energy in a pre-existing spacetime. Direction of explanation held throughout: `D_K eigenvalues → a₀ (zeroth Seeley-DeWitt moment) → Λ via the entanglement-equilibrium stationarity of the GGE causal-diamond half-trace → emergent ρ_Λ`. The modular flow `σ_t^ω` on `A_hor = A_K ⋊_{σ^ω} ℝ` IS the substrate's own Tomita-Takesaki structure (the GNS cyclic-separating vector of the faithful normal weight ω); it is the Unruh boost BECAUSE the substrate's acoustic metric IS an Unruh metric (S58 addendum §I), not because Rindler physics was imported. GR's Λ is the second-order volume variation of the substrate's entanglement equilibrium — not the other way around (`phononic-framing.md` §"IS Space, Not IN Space"). This gate turned the framework's own modular machinery onto the CC for the first time; the FAIL is the structurally-honest report that the machinery built for horizon-faithfulness does not by itself fix the absolute magnitude.

**Closure checklist (grep confirmations)**: see the fenced block immediately below.

```
$ ls -la computations/investigation-8/inv8_w2_1_*    # all three present
inv8_w2_1_jacobson_entanglement_equilibrium_cc.py / .npz / .png
$ grep -nE 'from canonical_constants import|print_verdict_payload' inv8_w2_1_jacobson_entanglement_equilibrium_cc.py
  -> both patterns match (canonical import line + print_verdict_payload def)
$ grep -E '^INV8-W2-1:.* audit_sha256=[a-f0-9]{64}' computations/investigation-8/inv8_gate_verdicts.txt
INV8-W2-1: FAIL -- value='53.5961' ... audit_sha256=241d15b06c492d02...a687418 content_sha256=2d4ca396...173122c9 schema_version=S84+
# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID # INV8-W2-1 3-tuple annotation (schema-v2)
```

---

### §W2-2. INV8-W2-2 (einstein-theorist)

**Status**: COMPLETED
**Gate ID**: `INV8-W2-2`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the PPN parameters are properties of the emergent metric g_M = a₂ moment; the test is of the fabric's emergent geometry, not its excitations)
**Agent**: `einstein-theorist`
**Hypothesis**: The emergent PPN (γ, β) and the emergent Eötvös η_emergent of g_M, from the a₂/a₄ moment structure + NNLO band-dependence of free-fall, satisfy γ=β=1 to the a₂/a₄ residual and η_emergent < 1e-15 — OR η_emergent > 1e-15, falsifying the framework against existing MICROSCOPE/Cassini data.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **Script** `computations/investigation-8/inv8_w2_2_emergent_ppn_eotvos.py` — EXISTS. `grep -E 'from canonical_constants import|print_verdict_payload'`:
  - `from canonical_constants import *   # noqa: F401,F403  (a_2_FW_zeta, a_4_FW_zeta, a_6_FW_zeta, M_KK_gravity, M_Pl_reduced, tau_fold, ...)`
  - `def print_verdict_payload(verdict, value, audit_sha, content_sha,`
- **Data** `computations/investigation-8/inv8_w2_2_emergent_ppn_eotvos.npz` — EXISTS (37 keys: γ/β, η_internal/η_lab, Δκ, transport_ratio, the a₂/a₄/a₆ moments, the full 3-tuple verdict).
- **Plot** `computations/investigation-8/inv8_w2_2_emergent_ppn_eotvos.png` — EXISTS (2-panel: PPN deviation vs Cassini/Will bounds; Eötvös η at fiber scale vs laboratory scale vs MICROSCOPE).
- **Verdict line** `computations/investigation-8/inv8_gate_verdicts.txt` — `INV8-W2-2: PASS … audit_sha256=53d125de2f52f207642e154a4bbb36a27315f4c5731d977a3c0fd2cffa62c846 content_sha256=4615f68c7a7693ebd4ca742d547dbd75c17d5c927ca856d8f9edef65dd971fc6` + dual-SHA companion row + schema-v2 [SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + regulator-pin row + scale-tag row (5 rows total).

**MCP Pre-Compute Audit**:

- `search_knowledge('PPN parameters gamma beta emergent metric equivalence principle Eotvos')` → no PRE-CLOSED PPN/Eötvös gate; the Akama-Diakonov emergent-metric open_channel (CF19) is the nearest neighbour; Einstein researcher index confirms equivalence-principle / experimental-tests ownership. **NOT pre-closed.**
- `search_knowledge('EMERGENT-EP-NLO kappa_EP band-blind Bochner quarter coupling B1 B3 Casimir')` → **S95-W3-5-EMERGENT-EP-NLO = PASS** (`κ_EP=1.000000000000`, `C1_B1=C1_B3=0.25`, `reading=A_geometric_Bochner_universal_quarter`, `κ_Casimir_foil=0.69230769(9/13)` REJECTED); the canonical NNLO band-difference form `Δκ = κ^NNLO(B1)−κ^NNLO(B3)` lives in `session-96-plan-w3.md`. **Leading EP coupling is band-BLIND (the load-bearing input).**
- `search_knowledge('S96-EP-NNLO-CASIMIR Delta_kappa verdict')` → **S96-EP-NNLO-CASIMIR = PASS**, `Δκ = -0.00839709`, `g0 = 1.574454363258e-03` (a₆ field-strength coeff), `b0 = 4.373484e-04`, `dDk_dC2 = -6.297817e-03`, `cc1_class=FI`, `a6_zeta=a6_mellin=765.593826`. **S97-EP-N3LO-CASIMIR = PASS**, `Δκ_N3LO = -0.0109607` (sign-stable). **The NNLO band-difference is already computed and audited — this gate maps it to the laboratory scale.**
- `get_constant('a_2_FW_zeta')` → 2776.165389 (S88, FW zeta). `get_constant('a_4_FW_zeta')` → 1350.7216 (S75). `get_constant('a_6_FW_zeta')` → 765.593826 (S96). `get_constant('M_KK_gravity')` → 7.428660036284456e16 GeV. `get_constant('M_Pl_reduced')` → 2.435e18 GeV. All present in `canonical_constants.py` (imported via `*`).
- `trace_entity('transport degree deg T_BZ pivot scale separation')` → no trace; the scale-and-channel-tagging discipline is the `phononic-framing.md §"Scale-and-channel-tagging"` rule (not a registry entity).

**Verdict**: **PASS** (composite; sign=PASS, magnitude=PASS, regime=VALID). `audit_sha256=53d125de2f52f207642e154a4bbb36a27315f4c5731d977a3c0fd2cffa62c846`.

**Results**:

**(1) Emergent PPN (γ, β) of g_M — γ = β = 1 EXACTLY at long range.**
The emergent metric g_M is generated by the a₂ Seeley-DeWitt coefficient: `S_grav = (1/16πG_eff)∫R√g d⁴x`, `G_eff⁻¹ ~ Λ²f₂a₂` (PB-8). A pure Einstein-Hilbert action is the UNIQUE PPN point with γ=β=1 (Will 2014). The departure carrier is the a₄ (Weyl²/higher-curvature) moment, with maximal-possible PPN shift = the dimensionless moment ratio **a₄/a₂ = 1350.7216/2776.165389 = 0.4865421943**. But the a₄ higher-curvature term is **SHORT-RANGE**: its Yukawa range is ~1/M_KK = **2.66e-33 m**, so at any solar-system / laboratory distance `r` the suppression is `exp(−M_KK·r)` with exponent ~**3.76e32** at r~1 m → underflows to 0.0 in float64. The long-range (Cassini / MICROSCOPE) PPN parameters are therefore the a₂-only values:

| Quantity | Value | Bound | Pass |
|:---------|:------|:------|:-----|
| `γ_emergent` | 1.000000000000000 | — | — |
| `\|γ−1\|` | 0.000e+00 | Cassini < 2.3e-5 | ✓ |
| `β_emergent` | 1.000000000000000 | — | — |
| `\|β−1\|` | 0.000e+00 | Will < 1e-4 | ✓ |

**(2) Emergent Eötvös η of g_M — two scales (the structural crux).**
The S95 result that the LEADING a₂-channel coupling is band-BLIND (universal Bochner ¼; `C1_B1=C1_B3=0.25`; the Casimir-foil 9/13 REJECTED) is WHY the O(1) free-fall term cancels in the inter-band difference and η is suppressed to the NNLO field-strength cross-term. The S96-EP-NNLO-CASIMIR gate already computed that band-difference (audited PASS):

`Δκ = κ_EP^NNLO(B1) − κ_EP^NNLO(B3) = −(16/3)·g₀ = −8.397089937e-03`, with `g₀ = (1/45)·(a₆/a₄)/dim_adj = 1.574454363e-03` (Gilkey R·Ω² coefficient 1/45, SU(3) adjoint dim 8), C₂(B1)=0 vs C₂(B3)=4/3 (Δ_C₂ = −4/3). Sage-QQ cross-check (exact rationals): `g₀ = 127598971/81043296 = 1.5744544`, `Δκ = −0.0083970899`, `η_internal = |Δκ|/2 = 0.0041985450` — bit-matching the script; the script-vs-S96 rel-err is **6.404e-15**.

The decisive scale distinction:

| Eötvös observable | Value | Nature | Falsifier-relevant |
|:------------------|:------|:-------|:-------------------|
| `η_internal = \|Δκ\|/2` | **4.198545e-03** | substrate-IS, at the **fiber-curvature scale** R_K(τ_fold)=2.018 (~M_KK²); the S96 frontier-#8 VALUE-bearing EP prediction **INSIDE the BZ** | NO (not a lab observable) |
| `η_lab` (MICROSCOPE) | **1.833638e-91** | laboratory-IN, at the **Earth-field external curvature** | **YES** — the binding falsifier |

`η_internal` is **NOT** the laboratory Eötvös parameter. Δκ is a `d(λ_b²)/dR_K`-type response in units of the fiber curvature R_K; the laboratory free-fall test rides on the EXTERNAL (terrestrial) curvature, ~89 OOM below M_KK². The transport from substrate-internal to laboratory scale is a curvature rescaling (`phononic-framing.md §"Scale-and-channel-tagging"`; the `deg(T_{BZ→lab})` degree):
`η_lab = (1/2)·|Δκ|·(R_lab/R_K(fold))`, where R_lab = Earth-field tidal curvature `G·M_⊕/(c²r³) = 1.249e-23 m⁻²` at the 710 km MICROSCOPE orbit, made dimensionless in M_KK² units (`M_KK² = 1.417e65 m⁻²`): `R_lab_dimensionless = 8.814e-89`, `transport_ratio = R_lab/R_K = 4.367e-89`. Result: **η_lab = 1.83e-91 ≪ MICROSCOPE 1e-15 (≈73–76 OOM margin)**.

**(3) Operator (3-way set-membership) — all three pass.**
`(|γ−1| < 2.3e-5 Cassini) ∧ (|β−1| < 1e-4 Will) ∧ (η_lab < 1e-15 MICROSCOPE)` → True ∧ True ∧ True = **PASS**.

**(4) Schema-v2 [SIGN] 3-tuple (4-tuple: value=η_lab=1.83e-91, scheme=FW-zeta, convention=ABSOLUTE, L_max=10).**
- `sign_verdict=PASS`: predicted directions all hold — η_internal > 0 (C₂(B1)=0 ≠ C₂(B3)=4/3 ⇒ the substrate DOES break band-degeneracy at NNLO, a genuine nonzero EP signal at the fiber scale), η_lab on the SAFE side of MICROSCOPE, and γ−1=β−1=0 (the GR point, long-range a₂-only).
- `magnitude_verdict=PASS`: all three external bounds satisfied.
- `regime_verdict=VALID`: S96 Δκ cross-check 6.4e-15 < 1e-6; the a₄ Yukawa genuinely underflows (long-range shift identically 0); transport ratio finite and positive.

**(5) Substitution chain (substituted numbers).** Plan §W2-2 Step-1→6: `κ_EP^NNLO(b) = 1 + 8β_b R_K + 4γ_b C₂(b)`; with `C₂(B1)=0, C₂(B3)=4/3` the leading ¼ band-blind term cancels in `Δκ = 8(β_{B1}−β_{B3})R_K − (16/3)γ_{B3}` → canonical `Δκ = −(16/3)g₀ = −8.397e-3`. The plan's hypothesis that "η is NNLO-suppressed" is CONFIRMED in DIRECTION but SHARPENED in magnitude: η_internal = 4.20e-3 is O(10⁻³) at the FIBER scale (8 OOM ABOVE 1e-15 — a naive `η = |Δκ|/2` reading would have FALSIFIED the framework), and the resolution is the scale separation: the laboratory η is the fiber-scale η rescaled by R_lab/R_K = 4.37e-89, landing at η_lab = 1.83e-91. **The framework is NOT falsified; it is decisively consistent with MICROSCOPE/Cassini.**

**Constraint-map consequence.** PASS on all three precision-GR bounds with ZERO continuous free parameters (every input — a₂/a₄/a₆ moments, B1/B3 Casimir labels, the S95 band-blind coupling, the S96 Δκ — is on disk). This is the natural endpoint of the EIH program (motion-from-field-equations for g_M, tested against precision GR): the emergent metric g_M is **observationally indistinguishable from GR at the tightest EP/PPN precision frontier in physics**, WITHOUT new observation. Frontier #8 (emergent EP) is promoted from "structurally derived" (S95 leading-order band-blindness) to "consistent with MICROSCOPE η < 1e-15 + Cassini |γ−1| < 2.3e-5". The OBSERVATION-FREE falsifier did NOT fire — but its non-firing is contingent on the curvature-transport map: the substrate carries a genuine (4.2e-3) inter-band EP signal at the fiber scale, killed at the laboratory scale by 89 OOM of curvature-scale separation, NOT by an exact cancellation. **Substrate-first framing**: GR's equivalence principle IS the leading band-blindness of the substrate's a₂-channel Bochner-Lichnerowicz coupling; the NNLO band-difference is the substrate's predicted departure from it, and it is undetectable IN the laboratory only because the laboratory's external curvature is 89 OOM below the fiber curvature where the substrate computes the EP-violation. We do NOT explain the emergent EP by GR's EP postulate; we derive both the leading EP and its tiny NNLO violation FROM D_K.

---

### §W2-3. INV8-W2-3 (einstein-theorist)

**Status**: COMPLETED
**Gate ID**: `INV8-W2-3`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (the GGE state, the 8 Richardson-Gaudin integrals, and the reduced density matrix are all substrate excitation structure)
**Agent**: `einstein-theorist`
**Hypothesis**: Tracing over the GGE's 8 Richardson-Gaudin integrals to the reduced density matrix for one phonon mode yields probabilities equal to |ψ|² (Born rule DERIVED from substrate coarse-graining) — or it does not, and the Born rule is an INPUT (a no-go, like the metric signature). Genuine two-track outcome, dual-prior pre-registered.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/investigation-8/inv8_w2_3_born_rule_gge_coarse_grain.py` — on disk; `grep` confirms `from canonical_constants import` + `print_verdict_payload`.
- `computations/investigation-8/inv8_w2_3_born_rule_gge_coarse_grain.npz` — on disk (per-mode eigenvalues, |ψ|² candidates, purities, basis-gaps, verdict).
- `computations/investigation-8/inv8_w2_3_born_rule_gge_coarse_grain.png` — on disk (left: per-mode eigenbasis test; right: basis-misalignment structural probe).
- Verdict line `computations/investigation-8/inv8_gate_verdicts.txt` — `INV8-W2-3: INFO ... audit_sha256=1d970e667b0f5b49708492785b0bbb0ff044a80c033fd2849240e390b8aa42df content_sha256=0ab824d5fbfd7ffb6644706e625b46bb6738ce2e73b5158950d2bfe249b3d00f` + dual-SHA companion row (no schema-v2 3-tuple — [VERIFY], not [SIGN]).

**MCP Pre-Compute Audit** (query-first discipline; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge('Born rule GGE coarse-graining reduced density matrix')` → open_channel **Born rule (L² norm)** S16 = **DEFENSIBLE** ("Gleason dim≥3 + geometric L² fiber integration eq 2.26"); NOT closed/derived. S62 hawking-qa already computes `ρ_A = Tr_B(ρ_GGE)` + `S_ent = −Tr(ρ_A ln ρ_A)` over CG(24) bonds — but for ENTROPY, a DIFFERENT functional, not a Born-probability=|ψ|² test.
- `search_knowledge('Richardson-Gaudin 8 integrals von Neumann entropy')` → `ρ_GGE = Z⁻¹ exp(−Σ_{k=1}^{8} λ_k I_k)` (S64 Eq.9); `S_ent=0` (BCS product state, ENT-39/S52); `S_GGE=2.2125 nats` (full 8-mode von-Neumann). The three-entropy distinction the plan flags is confirmed.
- `trace_entity('Born rule')` → 1 open_channel (S16 DEFENSIBLE) + eq_11423 (S58 "ALL of QM is substrate coarse-graining"). No closure, no prior derive-or-no-go gate. **Foundations cluster FRESH** — branch on no pre-closed result.
- `get_constant('u_bogoliubov')` / `get_constant('v_bogoliubov')` → not canonical constants; the Bogoliubov amplitudes live in `s52_bogoliubov_amp.npz` (u_k, v_k per mode, on disk; the plan's substrate-first source).
- Source addendum read in full: `sessions/archive/session-58/session-58-addendum-substrate-measurement.md §VI.1` — "Trace over the 8 internal integrals → reduced density matrix for one phonon mode. Verify measurement probabilities are |ψ|²" — explicitly flagged "a defined computation but not yet attempted" (line 159). This gate executes it.

**Prerequisite resolution**: `INV8-W1-1` is NOT in `inv8_gate_verdicts.txt` (the file was empty at dispatch). Per plan §"INV8-W2-3 prereq", the Bogoliubov amplitudes ARE on disk (`s52`, SHA `ecfbce08…`), so W2-3 is runnable on the **substrate-first fallback**: the W1-1 prereq governs only WHICH 8-integral λ_k weighting labels the GGE, NOT the numbers entering the |ψ|² test. The post-transit P_exc=1.000 marginal occupation in the pairing basis is `u_k²/v_k²` from the Bogoliubov coefficients regardless of the λ_k values. `w1_1_present=False` is recorded in the verdict companion note and the npz.

**Verdict**: **INFO** (Branch B — no-go: the Born rule is a substrate **INPUT**, not derived from GGE coarse-graining; Gleason supplies CONSISTENCY only). `audit_sha256=1d970e667b0f5b49708492785b0bbb0ff044a80c033fd2849240e390b8aa42df`. Per the dual-track pre-registration and `math-scripts.md` exit-code semantics, a no-go is INFO, not FAIL; FAIL is reserved for script breakage (not reached — wall 0.14s, exit 0).

**Results** (NUMBERS first, gate second, interpretation third):

**(1) Eigenbasis two-track test: `max_dev = 0.000000e+00` over all 8 modes.**
The GGE `ρ_GGE = (1/Z)∏_k exp(−λ_k I_k)` is diagonal in the quasiparticle (Richardson-Gaudin) eigenbasis — the 8 integrals are mutually-commuting occupation operators — so it FACTORIZES over modes, and tracing out 7 of 8 modes is a marginalization that leaves the 8th's single-mode factor exactly. For the post-transit pure-Bogoliubov state the per-mode reduced state in the pairing basis is `ρ_A = diag(u_k², v_k²)`. The L²/Gleason candidate (S16 eq 2.26) builds `|ψ_i|²` from the SAME Bogoliubov coefficients, so `{p_i} = {u_k², v_k²} = {|ψ_i|²}` exactly:

| mode | u | v | u²+v² | ρ_A eigenvalues {p_i} | {\|ψ_i\|²} | max_dev | Σp_i |
|:-----|--:|--:|------:|:----------------------|:-----------|--------:|-----:|
| B2[0..3] | 0.932487 | 0.361203 | 1.000000 | [0.869533, 0.130467] | [0.869533, 0.130467] | 0.000e+00 | 1.000000 |
| B1 | 1.000000 | 0.000000 | 1.000000 | [1.000000, 0.000000] | [1.000000, 0.000000] | 0.000e+00 | 1.000000 |
| B3[0..2] | 0.996042 | 0.088889 | 1.000000 | [0.992099, 0.007901] | [0.992099, 0.007901] | 0.000e+00 | 1.000000 |

Retained-mode B1 (the unpaired/normal mode, u=1) eigenbasis dev = 0.000e+00. **Necessary, but not sufficient** — this match is FORCED by construction (the marginal eigenvalues ARE the squared amplitudes in the eigenbasis), so it cannot by itself distinguish "derived" from "input."

**(2) Basis-misalignment STRUCTURAL probe — the discriminator.**
A sub-KK observer is free to pick a measurement direction `|θ⟩ = cosθ|0⟩ + sinθ|pair⟩` misaligned from the quasiparticle eigenbasis. Gleason's theorem GUARANTEES `p(θ) = Tr(ρ_A P_θ)` is the unique frame function for the density operator `ρ_A`. The L²-reading instead posits the PURE-state frame function `|⟨ψ|θ⟩|²`. These agree IFF `ρ_A = |ψ⟩⟨ψ|` (pure). But the GGE marginal of a paired mode is **MIXED**:

| mode | u | v | purity Tr(ρ_A²) | max basis gap \|Tr(ρ_A P_θ) − \|⟨ψ\|θ⟩\|²\| | kind |
|:-----|--:|--:|---------------:|:--------------------------------------------|:-----|
| B1 | 1.000000 | 0.000000 | 1.000000 | 0.000e+00 | PURE |
| B2 | 0.932487 | 0.361203 | **0.773109** | **3.368169e-01** | MIXED |
| B3 | 0.996042 | 0.088889 | 0.984322 | 8.853737e-02 | MIXED |

For every paired mode the GGE marginal is a mixed state (purity < 1), and its Born frame function departs from the pure-`|ψ|²` reading by up to **0.337** in a misaligned basis — five orders of magnitude above the 1e-6 tolerance. `mixed_basis_gap = 3.368e-01 > 1e-6` ⇒ **structural NO-GO**.

**Gate**: eigenbasis `max_dev = 0 < 1e-6` (PASS-shaped) AND `mixed_basis_gap = 0.337 > 1e-6` with a structural reason (the GGE trace yields a MIXED operator, not the pure state the L²-amplitude posits) ⇒ composite **INFO** (Branch B no-go).

**Dual-prior reallocation** (per `epistemic-discipline.md §"Dual-prior pre-registration"`):
- **track_A** = Born rule DERIVED from coarse-graining (reduced-ρ eigenvalues = |ψ|²), prior **0.35**.
- **track_B** = Born rule is an INPUT / no-go (Gleason supplies CONSISTENCY only, not derivation), prior **0.65**.
- Discriminator fired: INFO/no-go WITH a structural reason → reallocate **0.9 to track_B**. The GGE coarse-graining produces a mixed density operator; Gleason then says IF probabilities are a frame function THEN they are Tr(ρ P) — a CONSISTENCY statement — but the trace does NOT single out the pure `|ψ|²` rule the L²-reading needs for a derivation. The eigenbasis coincidence is the trivial alignment, not a derivation.

**Substitution chain (two-track logic, realized)**: Step 1–3 build `ρ_A` (diagonal, eigenvalues {u², v²}); Step 4 builds the L²-candidate `|ψ_i|² = {u², v²}`; Step 5 Branch A (eigenbasis, max_dev<1e-6) vs Branch B (misaligned basis, mixed_basis_gap>1e-6 with structural reason). Step 5 lands Branch B: the necessary eigenbasis match holds, but the sufficient basis-independent match FAILS because the marginal is mixed. The honest principle-theoretic reading (my R-2): the Born rule is an element of physical reality (EPR criterion); the theory has a CONSISTENCY argument (Gleason) for it, NOT a derived counterpart — and a no-go is itself a result, distinct from the prior S16 "DEFENSIBLE" limbo.

**Constraint-map consequence**:
- The Born-rule open_channel (S16) moves from **DEFENSIBLE** (a consistency tag) to a sharper position: **INPUT** (no-go from GGE coarse-graining) — on the same footing as the metric signature. This does NOT close G-3 (the un-derived-QM program) via derivation; it closes the GGE-coarse-graining CORRIDOR to a Born-rule derivation, which is informative.
- Points (per einstein B-2) toward **Penrose-Diósi gravitational decoherence** `E_G(a₂, band-difference)` as the DERIVED measurement scale — the next constructive attack on WHY a frame function is selected, replacing the S58 `F_J` coincidence.
- Consistent with the INV8-W4-1 M2 split's expectation (Born rule potentially derivable for the classical thermodynamic layer, an input for the entanglement layer): this gate tests ONE mode's marginal and finds the coarse-graining gives a mixed state, not the pure `|ψ|²` — the entanglement structure (the off-eigenbasis content) is exactly what the thermodynamic trace cannot derive.

**Substrate-first framing**: measurement IS substrate probing substrate; the Born weight is a property of the GGE marginal, here shown OBSTRUCTED as a derivation. Direction of explanation preserved (`phononic-framing.md`): D_K eigenvalues → post-transit GGE → trace out 7 modes → reduced ρ_A → its eigenvalues are the measured probabilities. IF the Born rule holds it is because the GGE coarse-graining produces it; Gleason (frame-function ⇒ Tr(ρP)) is the CONSISTENCY check, not the origin — and the computation shows the trace produces a MIXED operator whose frame function is not the pure `|ψ|²` the L²-reading posits. NON-PHONONIC caveat: Gleason's theorem itself is pure mathematics (used as the analytic TARGET for the derived branch, not a substrate result).

**Dual-SHA**: `audit_sha256=1d970e667b0f5b49708492785b0bbb0ff044a80c033fd2849240e390b8aa42df`, `content_sha256=0ab824d5fbfd7ffb6644706e625b46bb6738ce2e73b5158950d2bfe249b3d00f`. Artifacts: `inv8_w2_3_born_rule_gge_coarse_grain.py/.npz/.png`.

---

### §W2-4. INV8-W2-4 (einstein-theorist)

**Status**: COMPLETED
**Gate ID**: `INV8-W2-4`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the q-theory tracking vacuum is the substrate's effacement-residual / Volovik partition; the H² coefficient is a substrate spectral quantity)
**Agent**: `einstein-theorist`
**Hypothesis**: The running-vacuum (Solà Peracaula) RG coefficient c₁ of Λ(H)=c₀+c₁H²+… matches the substrate q-theory n=2 tracking coefficient (k=+3586.5 M_KK) — grounding C10's borrowed external-H in RG running; and the RG Λ(H_BBN) either does or does not relieve the S99 ~2.087× ΔN_eff shortfall.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script** `computations/investigation-8/inv8_w2_4_running_vacuum_rg_vs_n2.py` — PRESENT; `grep -E 'from canonical_constants import|print_verdict_payload'` → both patterns match (3 hits: the `import *` line, the explicit-name import, and the `def print_verdict_payload`).
- **Data** `computations/investigation-8/inv8_w2_4_running_vacuum_rg_vs_n2.npz` — PRESENT (all c1/D_c1/BBN/grid fields + dual-SHA + provenance).
- **Plot** `computations/investigation-8/inv8_w2_4_running_vacuum_rg_vs_n2.png` — PRESENT (3-panel: c1-bar log, ρ_vac/M_Pl² vs H/H₀ same-power-different-coeff, BBN-relief bar).
- **Verdict line** `computations/investigation-8/inv8_gate_verdicts.txt` — PRESENT; `grep -E '^INV8-W2-4:.* audit_sha256=[a-f0-9]{64}'` matches: `INV8-W2-4: FAIL -- value='composite=FAIL;D_c1=3.0587;...' ... audit_sha256=68e8bc865e5b7ce3fe38cb8d12be4c3233421db7874737e7ca2f10a8db58b55e content_sha256=c5452deb52cc0cba587909b7d097a1c104d499d2d1870ac88405d6e65f00d419 schema_version=S84+`; dual-SHA companion row + schema-v2 [SIGN] 3-tuple row (`sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`) + 5 substitution-chain/BBN/n_eff/regulator companion rows present.
- **WP section** (this section) carries `**Status**: COMPLETED`, `**Verdict**`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` markers. Verification by content-presence (regex match), NEVER line/byte counts.

**MCP Pre-Compute Audit**:
Queries executed before writing the script (per CLAUDE.md knowledge-MCP mandate). **FRESH** — no prior investigation computed the RG c₁ H² comparison; the gate is not pre-closed.

- `search_knowledge('running vacuum RG c1 H^2 coefficient Sola Peracaula')` → returns ONLY the plan-text equation hit ("n=2 coefficient … compare to the RVM c₁") + the c₁~(1/6π)Σm²/M_Pl² RVM-structure note; no computed c₁-vs-n=2 gate exists. CONFIRMS fresh.
- `search_knowledge('q-theory tracking vacuum n=2 coefficient kcurv 3586')` → `S101-W1-QEQ-SELFCONS` PASS (n2tracking=2.0001, kcurv=+3586.53, omega=59.888); `n_eff = 2 + Σ_k(dp_k/dH)n_k/(Σ ω_k n_k)` (S66 Gibbs-Duhem simple-fluid, correction→0 at fold); `DILUTION-CC` 114-OOM closed via Volovik tracking (rho_vac/rho_obs=1.032).
- `search_knowledge('BBN Delta_N_eff shortfall rho_vac rho_rad 0.474 0.227')` → `delta_N_eff(vac)=(rho_vac/rho_rad)/(7/8(4/11)^{4/3})~/0.227`; `delta_N_eff_vacuum_BBN_below=2.0873`, `rho_vac_over_rho_rad_BBN_below=0.474049`.
- `get_constant('rho_vac_over_rho_rad_BBN_below')` → 0.474049 (S98-MK3-2-BBN-VACUUM-FRACTION; n_eff=1.978111 from-below V.9-HARD; lever X=ln(H_BBN/H_0)=40.2756). `get_constant('delta_N_eff_vacuum_BBN_below')` → 2.0873 (=0.474049/0.227113). `get_constant('rho_vac_over_rho_obs')` → 1.032 (DILUTION-CC-66, FRAMEWORK-PREDICTION). `get_constant('M_Pl_reduced')` → 2.435e18; `get_constant('M_KK')` → 7.428660036284456e16.
- `search_knowledge('n_eff sign dispute … reconcile S100b')` → R-3 dispute (S66 G_eff-route n_eff=2.3 vs S98/S99 lever-route 1.978111<2) RECONCILED S100b (same-observable theorem; S66 escape priced 7.29 OOM). Used the canonical from-below 1.978111.
- RVM coefficient extracted from the corpus, NOT memory: Solà Peracaula `researchers/Einstein/08_2022…Running_Vacuum_Cosmology.md` Eq. 5.10/8.1 (`ρ_vac=ρ⁰_vac+(3ν_eff/8π G_N)(H²−H₀²)`, `ν_eff~10⁻³`) + `07_2024…Vacuum_Energy_CC.md` Eq. 27/28 (`ν_eff~10⁻⁵–10⁻³`, GUT-scale).

**Verdict**: **FAIL** (Part 1 coefficient match: `D_c1 = 3.0587 > 1.0`, sign_verdict=FAIL, magnitude_verdict=FAIL, regime_verdict=VALID). `audit_sha256=68e8bc865e5b7ce3fe38cb8d12be4c3233421db7874737e7ca2f10a8db58b55e`. Per `math-scripts.md` "All Results Are Good Results": this FAIL is informative — it CLOSES the corridor "C10's n=2 tracking IS the Solà running-vacuum RG-running" and distinguishes the substrate q-theory mechanism from the RVM. The substrate tracking and the RVM share the H²-POWER (both n=2 exactly) but differ by ~3 orders of magnitude in COEFFICIENT (substrate O(1) vs RVM O(ν), |ν|≪1). 4-tuple: `(value=3.058703, scheme=RVM-Sola, convention=RATIO, L_max=N/A)`.

**Results** (NUMBERS first, gate second, interpretation third):

**(1) PART 1 — coefficient match: `D_c1 = 3.0587` (best case, ν_eff=10⁻³); `D_c1_worst = 5.0587` (ν_eff=10⁻⁵). FAIL (> 1.0).**

| quantity | value | source |
|:---------|------:|:-------|
| `c1_substrate = α_V` (PRIMARY, S98-consistent) | **3.4342** | `α_V = ρ_vac(H₀)/(M_Pl² H₀²) = (rho_vac_over_rho_obs·ρ_crit)/(M_Pl² H₀²)`; ρ_crit=4.08e-47 GeV⁴ |
| `c1_substrate` (reduced-Planck identity) | 3.0960 | `= 3·rho_vac_over_rho_obs = 3·1.032`; reading-spread 0.045 dex (h~0.7 ρ_crit vs reduced identity) |
| `c1_RVM = 3 ν_eff` (best, ν=10⁻³) | 3.000e-03 | Solà Eq. 27/5.10, reduced-Planck units `1/(8πG_N)=M_Pl²` |
| `c1_RVM` (worst, ν=10⁻⁵) | 3.000e-05 | Solà ν_eff band `10⁻⁵–10⁻³` (GUT-scale; Eq. 28) |
| `D_c1 = |log10(c1_RVM_best) − log10(c1_sub)|` | **3.0587** | the most-generous-to-PASS discriminator |

The substrate `c1 = α_V ≈ 3.4` is **O(1)** — the DILUTION-CC tracking vacuum is full-strength (it tracks ρ_crit at order unity, not as a loop correction). The RVM `c1 = 3ν_eff ~ 10⁻⁵–10⁻²` is **O(ν), |ν|≪1** — the QFT running parameter `ν_eff ≈ (1/2π) ξ̄ (m²/m_Pl²) ln(m²/H₀²)` is doubly suppressed (deviation-from-conformal `ξ̄=ξ−1/6` × the loop factor m²/m_Pl² × log). The two H²-coefficients are NOT the same number; they differ by 3–5 orders of magnitude. **C10's tracking law is NOT grounded in the Solà RG-running** — A-2's "borrowed external-H" assumption is NOT discharged by this route.

**(2) PART 1 detail — SAME power, DIFFERENT magnitude.** `power_substrate = 2` (n2tracking=2.0001 → exactly 2; S101 slope_selfcons=1.000074, kcurv=3586.53 confirms the integer) and `power_RVM = 2` (RVM leading O(H²) term): `power_match = True`. The substrate fixes the H²-power to be exactly 2 by Gibbs-Duhem simple-fluid thermodynamics (n_eff = 2 + Σ(dp_k/dH)n_k/(Σ ω_k n_k), the correction → 0 at the fold per S66) — the SAME H² power the RVM derives from RG-running. So the POWER agrees; the discriminator is the COEFFICIENT, and that is where the gate FAILs. **The FAIL is in the coefficient magnitude, not the power.**

**(3) PART 2 (secondary axis) — BBN relief check.** Substrate lever-route reproduces the canonical exactly: `frac_substrate_BBN = (ρ_vac/ρ_rad)_BBN = 0.474049` (n_eff=1.978111 from-below; X_BBN=40.2756 reproduced from the rad-dom Friedmann path to <1e-3), which OVERSHOOTS the bound `0.227113` by `0.4740/0.2271 = 2.0873×` (ΔN_eff=2.0873). RVM route: since `ρ_rad_BBN = 3 M_Pl² H_BBN²` (rad-dom) and `ρ_vac^RVM/M_Pl² ≈ 3ν_eff H_BBN²` (H_BBN≫H₀), `(ρ_vac/ρ_rad)_BBN^RVM = ν_eff ~ 10⁻⁵–10⁻³ ≪ 0.227113` → **the RVM route RELIEVES** (`rvm_relief = True`). But — and this is the honest coupling — the RVM relief is bought PRECISELY by the coefficient difference: it relieves *because* `c1_RVM ≪ c1_substrate` (relief factor `frac_RVM/frac_substrate ≈ 2.1e-03`). The substrate's overshoot and the RVM's relief are **two different laws with the same power**, not the same mechanism evaluated two ways.

**(4) Substitution chain (substituted numbers; plan §W2-4 Steps 5–6).** Step 5: `(ρ_vac/ρ_rad)_BBN = (ρ_vac/M_Pl²)·M_Pl²/ρ_rad` at H_BBN; substrate = 0.474049 (2.087× over), RVM = ν_eff (relief). "IF c1_RVM = c1_substrate THEN same 0.474 overshoot (no relief); relief requires c1_RVM < c1_substrate OR a different effective n_eff" — and indeed `c1_RVM < c1_substrate` by 3–5 dex is exactly why the RVM relieves. Step 6: `sign_verdict` keys on D_c1 (coefficients agree?) → DISAGREE (D_c1=3.06>0.5) → sign=FAIL; the plan's pre-registered expectation ("a successful match IMPLIES the same ~2.087× overshoot") is INVERTED here — there is no match, and the no-match is exactly what lets the RVM relieve.

**(5) n_eff sign-dispute disclosure (R-3).** S66 G_eff-route n_eff=2.3 vs S98/S99 lever-route n_eff=1.978111<2 (from-below, V.9 HARD); RECONCILED at S100b (same-observable theorem). This dispute is ORTHOGONAL to the Part-1 finding: it is a sub-percent correction to a POWER that is 2 on BOTH the substrate and RVM sides, whereas the D_c1 FAIL lives in the O(1)-vs-O(ν) COEFFICIENT. The dispute does not affect the coefficient-match verdict.

**Constraint-map consequence.** D_c1=3.0587>1.0 → **FAIL**: the substrate q-theory tracking is a DISTINCT law from the Solà RVM RG-running, NOT reducible to QFT vacuum-energy running. C10 stays `CONFIRMED-TRACKING-FORM` but is NOT promoted to RG-GROUNDED — the "C10 is grounded in Solà's running" corridor is closed. A-2's borrowed-external-H is NOT discharged by the RVM route. The deeper structural reading (sharpening R-3): the substrate-overshoot-vs-RVM-relief question is NOT the same-coefficient n_eff-direction question the plan's Step 5 anticipated; it is a coefficient-MAGNITUDE difference (O(1) vs O(ν)) that the n_eff sign dispute cannot reach. **Substrate-first**: the running vacuum IS the q-theory tracking condensate (a₀ Seeley-DeWitt zeroth moment tracking H; Volovik partition); the RVM c₁ would be its QFT-language emergent image IF the magnitudes matched — they do not, so the substrate tracking is its own object, and the RVM is a different (loop-suppressed) law that happens to share the n=2 power. Dual-SHA `audit_sha256=68e8bc865e5b7ce3…`, `content_sha256=c5452deb52cc0cba…`; schema-v2 3-tuple `sign=FAIL/magnitude=FAIL/regime=VALID`. Artifacts: `inv8_w2_4_running_vacuum_rg_vs_n2.py/.npz/.png`.

---

## Wave 2 Synthesis (team-lead)

Wave 2 closed 4/4 (W2-1 FAIL · W2-2 PASS · W2-3 INFO · W2-4 FAIL). Precision-GR + quantum-foundations cluster: the framework's emergent metric passes the tightest GR bounds, but the two new CC/H attacks did not close the dimensionful knot, and the Born rule is settled as an input.

- **W2-1 (FAIL; sign=PASS, magnitude=FAIL)** — the Jacobson entanglement-equilibrium route fixes the CC **sign** structurally (Λ_substrate > 0, de-Sitter-like, every chain factor positive) — a real principle-theoretic result — but the **magnitude** leaves ~54 OOM (closes ~62 of the bare 116). It also corrected a standing framework number: the S62 "17-OOM Jacobson closure" was **dimensionally inconsistent** (GeV²/GeV⁴ read as a ratio); the correct residual is ~54 OOM. Net: the entanglement-equilibrium corridor closes and **strengthens DILUTION-CC as the sole ≤1-OOM CC-magnitude mechanism**.
- **W2-2 (PASS)** — emergent PPN `γ = β = 1` EXACT at long range (a₂ Seeley-DeWitt IS Einstein-Hilbert; the a₄ departure is short-range Yukawa, ~1/M_KK), and Eötvös `η_lab = 1.83×10⁻⁹¹ ≪ MICROSCOPE 1e-15` (≈73 OOM margin). The substrate carries a genuine `η_internal = 4.2×10⁻³` EP signal at the *fiber* scale (frontier-#8), undetectable in the lab by 89 OOM of curvature-scale separation — NOT by cancellation. An OBSERVATION-FREE falsifier (all inputs on disk, tested vs existing MICROSCOPE/Cassini).
- **W2-3 (INFO, Branch-B no-go)** — the Born rule is a substrate **INPUT**, not derivable from GGE coarse-graining: the eigenbasis test is forced-zero (necessary-not-sufficient), but the off-eigenbasis purity gap (0.337) shows the thermodynamic trace yields a *mixed* operator, not the pure `|ψ|²` a derivation requires. Gleason supplies consistency only. S16 Born-rule open_channel: DEFENSIBLE → INPUT.
- **W2-4 (FAIL; sign=FAIL)** — running-vacuum substrate `c₁ = α_V ≈ 3.43` is **O(1)**; the Solà RVM `c₁ = 3ν_eff ~ 10⁻⁵–10⁻²` is **O(ν)** — 3–5 OOM apart. The two share the H²-**power** exactly (n_eff=2) but differ radically in **coefficient magnitude**. "C10 is RG-grounded by Solà running" is CLOSED; C10 stays CONFIRMED-TRACKING-FORM.

### What Changed
**(a) Numerical revisions** — `D_OOM(Jacobson) = 53.60` (was the dimensionally-wrong 17); `η_lab = 1.83×10⁻⁹¹`, `η_internal = 4.2×10⁻³`, `γ=β=1` (|γ−1|=|β−1|=0); `D_c1 = 3.06` (substrate c₁≈3.43 vs RVM ~10⁻⁵–10⁻²); Born-rule `mixed_basis_gap = 0.337`.
**(b) Structural changes** — Born rule re-typed DEFENSIBLE → substrate-INPUT (the GGE-coarse-graining derivation corridor closes); frontier-#8 EP promoted "structurally-derived" → "consistent with the tightest EP/PPN bounds in physics"; the S62 17-OOM Jacobson number RETRACTED as dimensionally inconsistent.

### Effected In-Session (non-math)
All W2 non-math findings are SESSION-track promotions, routed OUT to the `/rclab-investigate --investigation 8` close per the track-local boundary — NOT effected here (catalogued in `investigation-8-housekeeping.md §B`):
- **HY3-adjacent** — the corrected Jacobson residual (~54 OOM; S62 17-OOM retraction) updates the CC-magnitude register; DILUTION-CC re-affirmed as the sole ≤1-OOM route.
- frontier-#8 EP promotion + a candidate `η_lab` falsifier-master-inventory row (mack sole-writer).
- Born-rule open_channel DEFENSIBLE→INPUT status change; C10 CONFIRMED-TRACKING-FORM (not RG-GROUNDED) note.
No investigation-local non-math edits were required.

## Carry-Forward Computations

### CF-INV8-W2-3-PENROSE-DIOSI — derived measurement/objective-collapse scale from a₂ band-difference
| Field | Spec |
|:------|:-----|
| **What** | Compute the Penrose–Diósi gravitational self-energy `E_G(a₂, band-difference)` as the candidate *derived* measurement / objective-collapse scale — the next constructive attack on why the Born frame-function is selected, after W2-3 closed the GGE-coarse-graining *derivation* route (Gleason = consistency-only). |
| **Inputs** | the a₂ Seeley-DeWitt band-difference machinery; W2-3 npz (GGE marginal purities, `purity_B2=0.7731`); the Penrose–Diósi `E_G` formula; M_KK. |
| **Gate** | does `E_G` yield a substrate-derived collapse timescale/scale consistent with the measurement regime (pre-register the threshold + tolerance at plan time)? PASS = a substrate-fixed collapse scale; FAIL = no separation from the GGE-thermal scale (collapse not substrate-derived either). |
| **Effort** | ~1–2 wave-equivalents. |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | Jacobson entanglement-equilibrium → CC magnitude (W2-1) | OPEN | CLOSED (~54 OOM from this side); CC sign fixed >0 | magnitude route closes ~62/116 OOM only |
| 2026-06-15 | S62 "17-OOM Jacobson closure" | asserted | RETRACTED — dimensionally inconsistent (~54 OOM correct) | GeV²/GeV⁴ misread as ratio |
| 2026-06-15 | DILUTION-CC | one of several CC routes | sole surviving ≤1-OOM CC-magnitude mechanism | W2-1 closes the entanglement route |
| 2026-06-15 | emergent PPN/Eötvös of g_M (W2-2) | untested | PASS (γ=β=1; η_lab=1.83e-91 ≪ 1e-15) | a₂=EH long-range; a₄ Yukawa short-range |
| 2026-06-15 | frontier-#8 EP | structurally derived | consistent with tightest EP/PPN bounds | η_internal 4.2e-3 fiber-scale; η_lab safe by 89 OOM |
| 2026-06-15 | Born rule (W2-3) | DEFENSIBLE (S16) | substrate INPUT (Branch-B no-go) | Gleason consistency-only; mixed-basis gap 0.337 |
| 2026-06-15 | C10 running-vacuum RG-grounding (W2-4) | candidate | CLOSED — CONFIRMED-TRACKING-FORM, not RG-grounded | c₁ O(1) vs RVM O(ν), 3–5 OOM |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| INV8-W2-1 | `inv8_w2_1_jacobson_entanglement_equilibrium_cc.py` | ✓ | ✓ | FAIL |
| INV8-W2-2 | `inv8_w2_2_emergent_ppn_eotvos.py` | ✓ | ✓ | PASS |
| INV8-W2-3 | `inv8_w2_3_born_rule_gge_coarse_grain.py` | ✓ | ✓ | INFO |
| INV8-W2-4 | `inv8_w2_4_running_vacuum_rg_vs_n2.py` | ✓ | ✓ | FAIL |

All under `computations/investigation-8/`; verdicts in `inv8_gate_verdicts.txt`.
