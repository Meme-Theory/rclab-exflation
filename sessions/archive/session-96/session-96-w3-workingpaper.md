# Session 96 Wave W3 — NNLO Casimir EP discriminator + `Γ_grav/H_0` margin (Results Working Paper)

**Session**: 96 | **Wave**: W3 | **Plan**: session-96-plan-w3.md | **Theme**: CRITICAL equivalence-principle / Leggett-DM-survival axis — resolves convergence cluster C3 (first value-bearing substrate EP prediction beyond the generic-identity ceiling) and dissonance D1 (the `Γ_grav/H_0` margin for `LEGGETT-GRAV-DECAY-67`), plus the one-loop no-interior-saddle full-domain robustness companion.

## Gate Sections

### §W3-1. S96-EP-NNLO-CASIMIR (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S96-EP-NNLO-CASIMIR`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (second-order curvature response of the band-bottom D_K eigenvalues; spectral-moment property, not excitation)
**Agent**: `gen-physicist`
**Hypothesis**: At NNLO (second order in fiber curvature R_K), the inter-band EP ratio acquires a band-specific Casimir contribution the LO+NLO Lichnerowicz–Bochner universal-(1/4) coupling annihilates; the deliverable Δκ = κ_EP^NNLO(B1) − κ_EP^NNLO(B3) is a nonzero function of C₂(B1)−C₂(B3) = −4/3 (the first VALUE-bearing substrate EP prediction) iff the a₆/R² heat-kernel polynomial introduces an R_K-linear piece into ν_b via the rep-specific field strength F_b ~ C₂(b).
**Plan reference**: `sessions/session-plan/session-96-plan-w3.md` §W3-1 (machinery pin, thresholds, substitution chain source, dual_prior Track A/B, fb_pair).

**Verdict**: **PASS** (composite). sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID.
The substrate makes its **first VALUE-bearing equivalence-principle prediction at NNLO**: `Δκ = −0.00839709 ≠ 0` with the symbolically-predicted sign and `|Δκ| = 8.397×10⁻³ > 1e-4`. Frontier #8 (emergent EP) escapes the generic-identity ceiling that `κ_EP^NLO = 1` sits on. The discriminator is **FI** (regulator-invariant: `a₆^{Mellin}` and `a₆^{zeta}` agree on sign). Dual-prior posterior re-allocated **Track A 0.9 / Track B 0.1**.

**Output Artifacts** (closure-verification checklist; verified on disk by content-presence regex, NEVER by line/byte counts):
- Script `computations/_shared/s96_w3_1_ep_nnlo_casimir.py` — present (44409 B); `grep -E 'from canonical_constants import|append_verdict'` → both match (`from canonical_constants import (`, `def append_verdict(...)`).
- Data `computations/session-96/s96_w3_1_ep_nnlo_casimir.npz` — present (24024 B); full-float64 round-trip of Δκ (`Delta_kappa=-8.397089937375313e-03`), all cross-check fields.
- Plot `computations/session-96/s96_w3_1_ep_nnlo_casimir.png` — present (130953 B); Panel 1 κ_EP^NNLO(C₂) band-dependence + NLO baseline=1; Panel 2 EP frontier ladder (NLO generic vs NNLO value-bearing) + CC1 FI partition.
- Verdict line `computations/session-96/s96_gate_verdicts.txt` (CANONICAL path) — `^S96-EP-NNLO-CASIMIR:.* audit_sha256=[a-f0-9]{64}` matches (line 60); dual-SHA companion row (61); schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row (62). `audit_sha256=ac85fd406f5afa76f7075edd7d00b54ad7d51415cda15b32a8e5b287f4960cec` (full 64, sig_5-unique), `content_sha256=376637776b87320bd65844f81235e83c83917a7d10cfb2f3e7d79c0b8f79401b`.
- WP §W3-1 (this section) — Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit, Results all present.

**MCP Pre-Compute Audit** (executed BEFORE writing the script, per CLAUDE.md query-first discipline; NOT pre-closed):
- `search_knowledge("equivalence principle NNLO Casimir kappa_EP a_6")` → only `Delta_kappa = kappa_EP^NNLO(B1) - kappa_EP^NNLO(B3)` and the Step-2/Step-3 equations, ALL sourced from `session-96-plan-w3.md` (the pre-registration being executed here) — **NOT a prior closure**. No `closed`/`gates` row pre-covers this gate.
- `trace_entity("emergent EP")` → `S95-W3-5-EMERGENT-EP-NLO` PASS (`κ_EP=1.000000000000`, reading A geometric Bochner universal quarter), and the open frontier "generally-covariant emergent 4D action ⇒ EP". The NLO baseline this gate EXTENDS; the NNLO value-content is the live frontier, uncomputed → gate is GENUINE.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). `get_constant("M_KK_gravity")` → 7.428660036284456e16 GeV.
- `search_knowledge("Peter-Weyl Casimir C_2 fundamental triplet 4/3 singlet")` → `SU3_Casimir_normalization = Gell-Mann_T_a_T_a=4/3 on fundamental`; `C_2(p,q)=(p²+q²+pq)/3+(p+q)`; cached `E_B1=0.819140 (C_2=0)`, `E_B3=0.978224 (C_2=4/3)`. Confirms C₂(B1)=0, C₂(B3)=4/3.
- `get_constant("a_6_FW_zeta")` → 765.593826 (S96, gate `S96-SDW-EFT-CONTROL`; n=6 zeta moment). `get_constant("a_4_FW_zeta")` → 1350.7216 (S75). These anchor the NNLO/NLO substrate moment ratio (no free magnitude knob).
- `query_entity(gates, S95-W3-5-EMERGENT-EP-NLO)` → confirms the PASS baseline + the foil `κ_Casimir=9/13` (NOT the discriminator). **Conclusion: gate NOT pre-closed; canonical values pulled with provenance.**

**Results**:

*Deliverable.* `Δκ = κ_EP^NNLO(B1) − κ_EP^NNLO(B3) = −0.00839709` (6 sig figs; full float64 `−8.397089937375313e-03` → `.npz` per Class 8.3 round-trip). Canonical closed form `−(16/3)·g0` matches the band-difference to <1e-14. `κ_EP^NNLO(B1)=1.007061056793` (C₂=0), `κ_EP^NNLO(B3)=1.015458146731` (C₂=4/3).

*NLO κ_EP=1 re-confirmation.* `κ_EP^NLO = (1/4)/(1/4) = 1.000000000000`, `|κ_EP^NLO − 1| = 0.000e+00 < TOL_EXACT=1e-12` → **re-confirmed**. At NLO `d(λ_b²)/dR_K = 1/4` band-independently (the connection-Laplacian ν_b carries C₂ at LO but is annihilated by ∂/∂R_K) — generic-identity-cored, any spin Dirac operator. Cache band-bottoms reproduce the S95 baseline exactly: `ν_B1=0.16743950`, `ν_B3=0.19418197`, `(1/4)R_K=0.50453599`.

*Symbolic d(Δκ)/dC₂ from the a₆ Gilkey polynomial.* `d(Δκ)/dC₂ = −4·g0 = −6.297817×10⁻³` (Sage-symbolic: `d/dC₂[4 g0 (C₂(B1) − C₂)] = −4 g0`), `|d(Δκ)/dC₂| = 6.30e-3 > 1e-9` floor → **nonzero**. Nonzero ⟺ the EP prediction is value-bearing (a function of C₂), i.e. a₆ introduces a genuine band-asymmetry the NLO 1/4 lacked.

*Substrate-anchored NNLO coefficients (no free magnitude knob).* `g0 = c_ROmega2·(a₆/a₄)/dim_adj = (1/45)·(765.594/1350.722)/8 = 1.574454363258×10⁻³` (Sage-exact QQ `127598971/81043296000`, match to 1e-15). `b0 = c_R3·(a₆/a₄) = (1/1296)·0.5668036 = 4.373484×10⁻⁴`. The Gilkey rationals `c_ROmega2=8/360=1/45` (R·Ω² a₆ coefficient, Gilkey 1995 Thm 4.8.16 / Vassilevich Phys.Rept.388 eq 4.39) and `c_R3=(35/9)/7!=1/1296` (pure-scalar a₆ R³-family lead) are EXACT; the magnitude scale is the substrate's own NNLO/NLO moment ratio `a₆_FW_zeta/a₄_FW_zeta = 0.5668036`. The rep-dependence is the Casimir-trace identity `Tr_{V_b}(Ω²)/dim = [C₂(b)/dim_adj]·Fsq` (Dynkin cross-check: T(B3)=1/2, the standard fundamental normalization).

*4-tuple.* `(value=Δκ=−0.00839709, scheme=Mellin, convention=EMERGENT-CONE-NNLO-EXPANSION, L_max=10)`. CLASS=FULL (closed-form a₆ Gilkey polynomial + cached bare D_K band-bottoms; NO SCHEMATIC helper; the Mellin cross-check uses the FULL physical `analytic_zeta`, not `_spectral_action_regulators.py` → no `-SCHEMATIC` suffix). `regulator_pin = a_6^{Mellin}` (Connes-Moscovici 1995 §III.4 dimension-spectrum residue; bare a₆ FORBIDDEN), cross-checked `a_6^{zeta}`.

*CC1 — a₆^{Mellin} vs a₆^{zeta} FI/RD sign-agreement.* `a₆^{zeta} = 0.5·ζ_D(6,L=3) = 765.59382642` (= canonical `a_6_FW_zeta`); `a₆^{Mellin} = 0.5·analytic_zeta(6,L=3) = 765.59382642` (off-pole `analytic_zeta == zeta_D_direct` bit-exact by the Mellin↔Dirichlet identity). Both moments positive → `Δκ^zeta = Δκ^Mellin = −8.39709×10⁻³`, `sign=−1` in both → **CC1 sign-agree = True → FI-class (regulator-INVARIANT)**. Structural reason: g0 inherits sign(Fsq) and `Tr(F²)≥0` is a positive-definite quadratic form no regularization can sign-flip.

*CC2 — band-bottom curvature-response fit vs symbolic d²/dR_K².* On the 40-pt R_K-axis `[0.6, 1.4]·R_K(fold) = [1.211, 2.825]`, the substrate NNLO dispersion `λ_b²(R_K) = ν_b + (1/4)R_K + b0 R_K² + g0 C₂(b) R_K` (ν_b from the cached L_max=10 band-bottoms; NO re-diagonalization) gives finite-difference `d²(λ_B1²)/dR_K² = 8.7469686847e-04` and `d²(λ_B3²)/dR_K² = 8.7469686846e-04` vs symbolic `2·b0 = 8.7469686848e-04`; residuals 3.63e-15 / 1.36e-14 (both <1e-6) → **CC2 ok**. The d²/dR_K² is band-INDEPENDENT (=2 b0); the EP asymmetry lives in the FIRST derivative via the g0 C₂(b) R_K cross-term (the Δκ source). Kinematic cross-check (20-pt q-grid): NNLO coupling-strength ratio B1/B3 = 0.991730737535 (q-independent; consistency with κ-ratio = 0.00e+00) — the discriminator is the coupling-strength bracket, not a kinematic artifact; squeezing separated.

*Substitution chain (Step 1→4, substituted numbers; PRE-REGISTERED — sign NOT re-decided post-hoc).*
  - Step 1: `R_K(fold)=2.01814396`, `dR_K/dτ(fold)=0.27603275`; `ν_B1=0.16743950`, `ν_B3=0.19418197`; `C₂(B1)=0`, `C₂(B3)=4/3`, `Δ_C2 = C₂(B1)−C₂(B3) = −1.333333`. LB identity `λ_b²=ν_b+(1/4)R_K`; a₆ Gilkey R·Ω² ~ C₂(b).
  - Step 2: `λ_b²(NNLO)=ν_b+(1/4)R_K+b0 R_K²+g0 C₂(b) R_K`; `d(λ_b²)/dR_K|_NNLO = 1/4 + 2 b0 R_K + g0 C₂(b)`; `κ_EP^NNLO(b) = 1 + 8 b0 R_K + 4 g0 C₂(b)`.
  - Step 3: `κ(B1)=1+8 b0 R_K` (C₂=0); `κ(B3)=1+8 b0 R_K + (16/3) g0` (C₂=4/3); `Δκ = −(16/3) g0` (band-indep b0 R_K term cancels) `= −0.00839709`; `d(Δκ)/dC₂ = −4 g0 = −0.00629782`.
  - Step 4: with `C₂(B3)−C₂(B1)=+4/3>0` and `g0>0` (Tr(F²)≥0 ⇒ Fsq>0 ⇒ g0>0), `sign(Δκ) = −sign(g0) = NEGATIVE`. **Predicted sign −1; computed sign −1 → sign_verdict PASS.** Magnitude `|Δκ|=8.397e-3 > 1e-4 ∧ |d(Δκ)/dC₂|>1e-9 → magnitude PASS`.

*Dual-prior posterior re-allocation.* PASS → **Track A 0.9 / Track B 0.1** (Reading-NNLO-substrate-prediction; the a₆ field-strength term IS band-specific, Δκ≠0, frontier #8 escapes the genericity ceiling). Track B (genericity-persists) priors collapse from 0.4 → 0.1.

*Solution-space.* Opens a new falsifiable substrate EP corridor: the substrate predicts band-dependent free fall at second order in curvature, distinguishing it from a generic single-metric emergent-gravity / Brans–Dicke / bimetric model where the NLO κ_EP=1 universality would persist. The first EP discriminator with substrate value-content. Forward consumers (`fb_pair.backward`): frontier #8 promotion record; the §7 capstone scorecard EP row; any future N3LO EP gate; the FI/RD partition is settled FI (no FI-repin needed).

*Substrate framing (GEOMETRIC; arrow held).* D_K eigenvalues (cached band-bottoms λ_b at L_max=10) → Lichnerowicz–Bochner `λ_b²=ν_b+(1/4)R_K + a₆ NNLO curvature polynomial` → the band-specific field-strength coupling `Tr(F^b F^b)~C₂(b)` → emergent free-fall trajectory on g_M. The excitations fall ON the fabric; g_M IS the a₂ Seeley-DeWitt moment, R_K is the fiber Ricci scalar sourcing it. The EP is an EMERGENT property of the a₂/a₆ moment structure, derived FROM D_K — NOT a postulate the substrate satisfies. The NNLO band-difference is what makes it substrate-PREDICTIVE rather than generic-identity-cored (the container-thinking error reviewers flagged in reading κ_EP^NLO=1 as a substrate prediction).

*Artifacts.* `computations/_shared/s96_w3_1_ep_nnlo_casimir.py`; `computations/session-96/s96_w3_1_ep_nnlo_casimir.npz`; `computations/session-96/s96_w3_1_ep_nnlo_casimir.png`; verdict line 60 + companion 61 + 3-tuple 62 in `computations/session-96/s96_gate_verdicts.txt`.

---

### §W3-2. S96-LEGGETT-GAMMA-GRAV (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S96-LEGGETT-GAMMA-GRAV`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (Leggett inter-band relative-phase mode of the multi-band fabric condensate; its gravitational decay is a phononic relic-fate question)
**Agent**: `gen-physicist`
**Hypothesis**: The Leggett-channel GGE dark-matter quasiparticle's gravitational decay rate Γ_grav (the PHYSICAL surviving rate), computed from the canonical Eq. QA-9 graviton-vertex family with substrate-pinned parameters, satisfies Γ_grav < H_0 by a large dimensionless margin (Γ_grav/H_0 ≪ 1) — discharging the CRITICAL conditional under Ω_DM h² = 0.120 (`LEGGETT-GRAV-DECAY-67`) with an explicit first-principles margin rather than a cited archive figure.
**Plan reference**: `sessions/session-plan/session-96-plan-w3.md` §W3-2 (Eq. QA-9 form, ε-band scan, dual_prior D1 Track A/B, fb_pair, writer_agent split).

**Verdict**: **PASS** (composite). `sign_verdict=PASS`, `magnitude_verdict=PASS`, `regime_verdict=VALID`. Physical surviving margin Γ_grav/H_0 = **3.31e-66** (margin_OOM = **65.5**), ratio < 1 across the whole ε-band; D1 RESOLVED. [Value reconciled from a prior emission of 1.11e-68 — see "Value reconciliation" note below; composite verdict unchanged.]

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML; all confirmed on disk, size > 0):
- **script** `computations/_shared/s96_w3_2_leggett_gamma_grav.py` (42,084 B) — `grep -E 'from canonical_constants import'` → matches (`from canonical_constants import *` + explicit-name block); `grep -E 'append_verdict'` → matches (def + call).
- **data** `computations/session-96/s96_w3_2_leggett_gamma_grav.npz` (18,177 B) — full float64 round-trip of all band arrays + headline scalars.
- **plot** `computations/session-96/s96_w3_2_leggett_gamma_grav.png` (117,840 B) — 2-panel (margin-vs-ε log scale incl. both channels; two-channel suppression budget).
- **verdict_line** `computations/session-96/s96_gate_verdicts.txt` — `grep -E '^S96-LEGGETT-GAMMA-GRAV:.* audit_sha256=[a-f0-9]{64}'` → matches TWO canonical lines (original + corrective, per Option A). **CANONICAL (latest non-superseded)**: `audit_sha256=d1c7bd610951eb8a477b941133e1005d7a306246ae90808ef9867595fa51cd0f` (unique as `audit_sha256=`, count=1), `content_sha256=b1af3c643561a299a7cb34ffbfe0c7e13621bf7d02f1dce25406dff62a9891e5`, carries `supersedes=37c46ca0…277fcd9c` in its value= field. **Original (RETAINED, superseded)**: `audit_sha256=37c46ca0…277fcd9c` (value 1.11e-68). Both carry dual-SHA companion + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple rows ([SIGN] trigger).
- **wp_section** this `### §W3-2. S96-LEGGETT-GAMMA-GRAV` (Status COMPLETED / Verdict PASS / Output Artifacts / MCP Pre-Compute Audit all present).

**MCP Pre-Compute Audit** (executed before writing the script, per CLAUDE.md + `knowledge-index-usage.md`; NOT pre-closed-by-fresh-compute — the result was only CITED, never re-pinned, which IS the D1 dissonance):
- `search_knowledge("Leggett gravitational decay Gamma_grav H_0 LEGGETT-GRAV-DECAY-67")` → gate `LEGGETT-GRAV-DECAY-67` (`PASS: Γ_grav<H_0; FAIL: Γ_grav>H_0`, CRITICAL 1/5); theorem "Single-Leggett gravitational decay: FORBIDDEN" [PROVEN S67]; Eq. QA-9 equation entry recovered verbatim; `LEGGETT-GRAV-DECAY-CONDITIONAL` (S95) `Gamma_grav/H_0~8.85e-66 (65 OOM margin); cites_S67_S73a; no_PASS_` — i.e. CITED not re-pinned.
- `trace_entity("LEGGETT-GRAV-DECAY-67")` → simultaneously a defined gate AND in `open_channel: UNCOMPUTED decisive tests / 4 CRITICAL` (TRANSIT-PS-67, **LEGGETT-GRAV-DECAY-67**, FUNCTIONAL-SELECT-67, BBN-VOLOVIK-67). **This defined-PASS ∧ UNCOMPUTED-CRITICAL simultaneity IS the D1 dissonance this gate discharges.**
- `get_constant("omega_L1")` → 0.138 (M_KK); `get_constant("Delta_BCS")` → 0.4642547394830737 (R-protected, M_KK; BCS-GAP-CANONICAL-70); `get_constant("M_KK_gravity")` → 7.428660036284456e16 GeV (CONST-FREEZE-42); `get_constant("M_Pl_reduced")` → 2.435e18 GeV (CODATA 2018); `get_constant("H_0_inv_s")` → 2.184e-18 s⁻¹; `get_constant("H_0_GeV")` → 1.438e-42 GeV; `get_constant("Omega_DM")` → 0.2657; `get_constant("rho_crit_GeV4")` → 4.08e-47 GeV⁴. All pins match the plan §W3-2 values exactly. (Note: an S75 entry lists `Γ_grav=9.42e10 GeV / τ_decay=7.0e-36 s` — that is the **transit-epoch** decay R2.8/R2.9, a DISTINCT, faster channel, NOT the gravitational-decay-vs-H₀ survival question; not used here.)
- **PRE-CLOSED status**: NO. The kinematic-protection *theorem* is PROVEN (S67), but the explicit dimensionless margin from a fresh canonical-pinned compute was genuinely uncomputed — exactly the D1 carry-forward this gate executes.

**Results**:

*Headline (physical surviving channel = the gate deliverable).* Γ_grav/H_0 = **3.31e-66** (3 sig figs); **margin_OOM = log10(H_0/Γ_grav) = 65.5** (1 decimal). Full float64 in the npz (`ratio_mid=3.310863e-66`, `margin_OOM_mid=65.48`). The physical pair channel is **ε-INDEPENDENT** (see "Value reconciliation"), so the headline is a single canonical value, not a band midpoint.

*Whole-ε-band robustness* (ε ∈ [0.005, 0.011], 11-pt linspace, S56 Leggett-Josephson gap-ratio band): ratio_band is **flat at [3.311e-66, 3.311e-66]**, margin_OOM_min = **65.5**, `whole_band_below_1 = True`. The PASS holds across the entire band by ~65 OOM. Note ε does NOT enter the physical pair channel (it enters only the *forbidden* single-Leggett channel (a) below, where its band [1.14e39, 5.53e39]·H_0 is the open-problem-flag suppression chain) — so band-flatness here is the physically-correct ε-independence, not a degenerate scan.

*4-tuple.* `(value=3.311e-66, scheme=QA-9-graviton-vertex, convention=GAMMA-GRAV-OVER-H0-DIMENSIONLESS-MARGIN, L_max=N/A)`.

*The two-channel resolution (the substance of D1).* The gate margin is the *physical surviving* rate, which required disentangling two channels the single-label "Eq. QA-9 margin" conflated:
- **Channel (a) — naive single-Leggett L→g+g (Eq. QA-9 literal).** `Γ_KK = ε²·ω_L³·Δ²/(64π M_Pl⁴)·(ω_L/M_KK)⁴` with canonical GeV pins gives `Γ_KK/H_0 ~ 2.93e39` mid-band (band [1.14e39, 5.53e39]) — reproducing the S66 workshop Eq. QA-10 "cosmologically instant" **OPEN-PROBLEM flag** (the `UNCOMPUTED CRITICAL` reading). This channel is **FORBIDDEN EXACTLY** (Γ_single = 0): Z₂ parity `a_2(φ_23)=a_2(−φ_23)` (cos even, Δn_L=−1 ODD → forbidden to all orders, S67/S73a PROVEN) AND graviton-gap kinematic protection (2·m_graviton ~ 2·M_KK ≫ ω_L=0.138 M_KK).
- **Channel (b) — physical surviving pair annihilation 2L→2g (Δn_L=−2 EVEN → ALLOWED).** `⟨σv⟩=ξ_eff²·m_L²/(960π M_Pl⁴)`, `Γ_pair=n_L·⟨σv⟩`, `n_L=Ω_DM·ρ_crit/m_L`, with the **canonical** `ξ_eff = frac_d2a2·φ_zp²(GL) = 0.2755·2.781² = 2.131` (substrate frac_d2a2/φ_zp from the S67 pinned npz; **NO ε factor** — ε enters only channel (a)). This is `Γ_grav := Γ_pair`, the deliverable margin = **3.31e-66 · H_0**.

This reconciles the `defined-PASS-gate ∧ UNCOMPUTED-CRITICAL` simultaneity: the naive QA-9 vertex magnitude is huge (the open-problem flag), but Z₂-killed to exactly zero; the physical surviving channel is ~65 OOM below H_0.

*Value reconciliation (between-waves fix per no-technical-debt; verdict UNCHANGED).* A prior emission of this gate (audit_sha256 `37c46ca0…277fcd9c`, value 1.11e-68 / margin_OOM 68.0) applied an **unjustified ansatz** `ξ_eff·(ε/ω_L1)` to the pair channel, scaling ξ_eff down by ~13–28× and pushing the headline ~2.5 OOM **below its own CC2 archive re-pin** (which already computed the canonical 3.31e-66) — an internal inconsistency with no physical basis. **First-principles fix:** the S67/S73a canonical pair channel carries **no ε-dependence** (`ξ_eff = frac_d2a2·φ_zp²`, S67 `s67_leggett_grav_decay.py:448`; ε appears only in the *forbidden* single-Leggett `Γ_eps = ε²·…`, S67:550). The φ_zp pin is the **GL/S52 value** (φ_zp = 1/√(2·ω_L·I_L) with the plan-pinned ω_L = ω_L1 = 0.138; V_bare/S59 uses the non-canonical ω_L=0.04923 and is the cross-check sibling). With the canonical GL prescription the headline = **3.31e-66**, which reproduces the S67 archive `Gamma_pair_over_H0_S52 = 3.309792e-66` (rel-diff 3.2e-4, the Ω_DM/ρ_crit canonical-vintage drift) and **equals the CC2 re-pin exactly** (`headline_eq_CC2 = True`). Re-emitted per `gate-verdicts.md §"Option A"`: original line retained byte-for-byte; corrective line appended with `supersedes=37c46ca0…277fcd9c`, new `audit_sha256=d1c7bd61…fa51cd0f`. The composite verdict stays **PASS** (Γ_grav/H_0 ≪ 1 by ~65–66 OOM under GL, ~65 under V_bare — every channel/φ_zp treatment); only value / margin_OOM / the 4-tuple changed.

*CC1 — M_KK→GeV dimensional bookkeeping.* `(ω_L/M_KK)⁴ = (0.138)⁴ = **3.6267e-4**` is DIMENSIONLESS (ratio of two M_KK quantities; matches plan 3.6266e-4 to <1e-7). Unit closure verified both ways: s⁻¹ vs GeV convention agree to max-reldev **3.23e-4** (`conv_consistent=True`; residual is the H_0_GeV/H_0_inv_s canonical rounding). ω_L³·Δ²=GeV⁵, /M_Pl⁴=GeV⁻⁴ → net GeV¹ → s⁻¹ via `hbar_GeV_s=6.582119569e-25 GeV·s`. Supporting `(M_KK/M_Pl)⁴=8.663e-7`.

*CC2 — S67/S73a archive cross-check (ANCHOR, not pin); now cross-checks the ACTUAL headline.* Archive `Gamma_physical_over_H0` (S73a) / `Gamma_pair_over_H0_S59` (S67, V_bare) = **9.2774e-66** recovered exactly from the pinned npz; S95-cited anchor `~8.85e-66`. The headline (canonical GL φ_zp) **= the CC2 re-pin EXACTLY** (`headline_eq_CC2 = True`: both 3.310863e-66 — same canonical GL prescription, so the deliverable is now identical to its own cross-check, the inconsistency resolved). It lands **|OOM gap| = 0.43** vs the cited anchor (`CC2_consistent=True`, tol 1.5 OOM) and 0.45 OOM vs the S73a/V_bare archive. The ~0.5-OOM offset is the GL/S52 (3.31e-66) vs V_bare/S59 (9.28e-66) φ_zp choice — both bracket the anchor; GL is the canonical pin (plan-pinned ω_L=0.138), V_bare the sibling. Cross-check only — the gate margin is RE-DERIVED from canonical pins, NOT taken from the archive (the D1 cited→re-pinned conversion).

*Graviton-gap kinematic protection (the structural REASON).* The margin is enormous BECAUSE the single-Leggett channel is kinematically gapped: each KK graviton costs ≥ ~M_KK, and 2·m_graviton ~ 2·M_KK ≫ ω_L=0.138 M_KK, so L→g+g is energetically forbidden — the same kinematic protection the BCS gap gives quasiparticle decay. Substrate-IS framing: D_K eigenvalues → Leggett mode ω_L → graviton-gap → margin; H_0 is the READOUT of the emergent expansion rate the relic must outlive, NOT an external clock it decays in. Z₂ parity independently sends even the soft-graviton single channel to exactly zero.

*Substitution chain (Step-1→4, substituted canonical numbers; PRE-REGISTERED — sign read off ONLY at Step 4).*
  - Step 1 (defs): channel-a `Γ_KK=ε²·ω_L³·Δ²/(64π M_Pl⁴)·(ω_L/M_KK)⁴`; Z₂ → Γ_single=0; channel-b `⟨σv⟩=ξ_eff²m_L²/(960π M_Pl⁴)`, `Γ_pair=n_L⟨σv⟩`. Pins: ω_L1=0.138, Δ_BCS=0.4642547394830737, M_KK_gravity=7.428660036284456e16 GeV, M_Pl_reduced=2.435e18 GeV, Ω_DM=0.2657, ρ_crit=4.08e-47 GeV⁴, H_0_inv_s=2.184e-18 s⁻¹, hbar_GeV_s=6.582119569e-25 GeV·s.
  - Step 2 (substitute, M_KK→GeV): ω_L_GeV=m_L=1.0252e16 GeV; Δ_BCS_GeV=3.4488e16 GeV; (ω_L/M_KK)⁴=3.6267e-4 (dimensionless); canonical ξ_eff(GL)=2.131; ⟨σv⟩(canon)=4.501e-45 GeV⁻², n_L(canon)=1.058e-63 GeV³.
  - Step 3 (simplify to margin): Γ_grav:=Γ_pair=4.760e-108 GeV (canonical GL, ε-independent) → 7.231e-84 s⁻¹; ratio=Γ_grav/H_0=3.311e-66; margin_OOM=65.5.
  - Step 4 (direction ONLY now): ratio=3.31e-66 ≪ 1 ⇒ Γ_grav < H_0 ⇒ relic survives a Hubble time ⇒ Ω_DM h²=0.120 stands. `sign_verdict=PASS` (ratio<1 across whole band), `magnitude_verdict=PASS` (margin_OOM>1 everywhere), `regime_verdict=VALID` (CC1 ✓, conv ✓, CC2 ✓ — and headline≡CC2 by construction) → composite **PASS**.

*Dual-prior posterior re-allocation (D1).* Per §W3-2 dual_prior: PASS → **Track A (nazarewicz PASS-confirm) 0.97**; D1 RESOLVED — the gate PASS-confirms nazarewicz's reading WHILE supplying the explicit margin (3.31e-66, 65.5 OOM) the open-CRITICAL readers (landau V.5 / mack CF-MACK-5 / hawking Constraint 2) correctly flagged as uncomputed. The "PASS gate vs UNCOMPUTED CRITICAL" split is reconciled structurally (naive QA-9 ~10³⁹·H_0 open-problem flag → Z₂-forbidden to 0; physical pair channel ~3e-66·H_0).

*Solution-space.* The CRITICAL conditional `LEGGETT-GRAV-DECAY-67` is discharged with an explicit first-principles margin; the strongest DM claim (structural σ/m=0, superselection-protected) is no longer hostage to an uncomputed rate. No corridor closed; the Leggett-channel-DM corridor is confirmed open by ~65 OOM (GL canonical; ~65 V_bare — survival robust to the φ_zp choice).

*fb_pair.* forward: S67 LEGGETT-GRAV-DECAY-67 (Eq. QA-9 vertex + kinematic protection PROVEN), S73a pair-channel archive (anchor), canonical pins (ω_L1, Δ_BCS, M_KK_gravity, M_Pl_reduced, Ω_DM, ρ_crit, H_0_inv_s, hbar_GeV_s), S56 ε-band, S67 substrate frac_d2a2/φ_zp. backward: Ω_DM h²=0.120 conditional (CRITICAL dependency); falsifier-master-inventory Leggett-DM row + §7.1 D1 framing correction (**mack-cosmic-bridge** sole-writer downstream); C11 Leggett-channel DM mass anchor (LEGGETT-MOMENT-70).

*Writer split (per §W3-2 `writer_agent`).* gen-physicist computed and landed the Γ_grav/H_0 margin VALUE + verdict + this WP §W3-2 ONLY. `mack-cosmic-bridge` (sole writer per `feedback_mack-bridge-role.md`) lands the corrected `falsifier-master-inventory.md` Leggett-DM margin row + the capstone §7.1 D1 framing correction in a downstream write — NOT touched here.

*Artifacts.* `computations/_shared/s96_w3_2_leggett_gamma_grav.py`, `computations/session-96/s96_w3_2_leggett_gamma_grav.npz`, `computations/session-96/s96_w3_2_leggett_gamma_grav.png`; CANONICAL (latest non-superseded) verdict in `computations/session-96/s96_gate_verdicts.txt` (`audit_sha256=d1c7bd61…fa51cd0f`, `supersedes=37c46ca0…277fcd9c`). The original line (`audit_sha256=37c46ca0…277fcd9c`, value 1.11e-68) is RETAINED on disk byte-for-byte per `gate-verdicts.md §"Option A"`; downstream consumers cite the d1c7bd61 line.

---

### §W3-3. S96-W3-SADDLE-FULLDOMAIN (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S96-W3-SADDLE-FULLDOMAIN`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (statement in the modulus τ about the spectral-action moment combination S_SA(τ) and the one-loop fluctuation determinant; spectral-triple property, not excitation)
**Agent**: `gen-physicist`
**Hypothesis**: The one-loop effective action Γ[τ] = S_SA(τ) + ½ Tr ln(D_K²/Λ²) has NO interior stationary point (dΓ/dτ fixed sign, zero interior sign-changes) on the FULL physical τ-domain [0, τ_NEC=1.383] — extending the S95-W2-3 PASS from [0, τ_now] to the NEC boundary and the overshoot turnaround τ=1.614 — so Z = Σ exp(−Γ) is boundary-dominated (Gibbons–Hawking–York) everywhere the censoring barrier admits the modulus.
**Plan reference**: `sessions/session-plan/session-96-plan-w3.md` §W3-3 (300-pt grid, three-route machinery, region partition at τ_NEC/τ_overshoot, dual_prior Track A/B, fb_pair).

**Verdict**: **PASS** — `n_interior_sign_changes(dΓ/dτ on [0, τ_NEC=1.383]) = 0`; `dΓ/dτ` fixed positive sign throughout; composite-collapse 3-tuple (sign=PASS, magnitude=PASS, regime=VALID). The S95-W2-3 no-interior-saddle / boundary-domination result is hardened from the [0, τ_now] window to the full physical domain up to the NEC boundary, and (informatively) through the censored overshoot τ=1.614 as well.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — all confirmed on disk, size > 0):
- Script: `computations/_shared/s96_w3_3_oneloop_saddle_fulldomain.py` (48.5 KB) — `grep -E "from canonical_constants import"` ✓ (line 113 `from canonical_constants import *` + explicit-name import); `grep -E "append_verdict"` ✓ (def + call).
- Data: `computations/session-96/s96_w3_3_oneloop_saddle_fulldomain.npz` (64.3 KB) ✓ — full float64 round-trip of all grids + region counts + verdict fields.
- Plot: `computations/session-96/s96_w3_3_oneloop_saddle_fulldomain.png` (184.6 KB) ✓ — 4-panel: Γ(τ)/S/Γ₁ full domain; dΓ/dτ (FD + Jacobi) symlog with censored band; rep-B cross-check arm; CC2 600-pt refinement + Jacobi-vs-FD dev.
- Verdict line: `computations/session-96/s96_gate_verdicts.txt` — `grep -E "^S96-W3-SADDLE-FULLDOMAIN:.* audit_sha256=[a-f0-9]{64}"` ✓; canonical line + dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row (3 lines). `audit_sha256=c25a6909b56743690a453fa41e77cd26e13ea920fe5d7c7c417e6035a0cfc5dd`, `content_sha256=14c3bee21362f85ed8e0accdacf900d7b7f5316238fe8da119a32429b06d395d`. SHA unique across all 23 canonical lines in the file (sig_5 clean).
- WP §W3-3: this section (Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit, Results all present).

**MCP Pre-Compute Audit** (queries executed before writing the script, per CLAUDE.md + plan §W3-3; one-line salient return each — NOT PRE-CLOSED: the full-domain extension is genuinely uncomputed; only the [0, τ_now] baseline was closed):
- `search_knowledge("one-loop effective action no interior saddle boundary domination S_SA spectral action")` → returns the gate's own Γ[τ] equation + the S95-W2-3-NO-WELL-ONE-LOOP gate (value=0, PASS) on [0, τ_now] — the baseline this gate extends; the full-domain [0, τ_NEC] count is NOT in the graph.
- `trace_entity("E7 structural monotonicity")` → E7 τ-flow PROVEN (`dS_SA/dτ` fixed sign, 9,600/9,600; `dS/dτ|_fold = +58672.8`); confirms the tree-term monotonicity backbone and pins τ_NEC=1.383, τ_overshoot=1.614 as the domain boundaries.
- `search_knowledge("Gibbons-Hawking-York boundary dominated partition function transit not slow-roll tau_NEC")` → confirms τ_NEC=1.383 (NEC onset, S95 W4-5 12D censorship; hawking V.3/V.9) and the transit-not-slow-roll reading (TRANSIT-279-48 INFO: ε_SR=0.027, η_SR=1.27 NOT slow-roll).
- `get_constant("a_0_FW_zeta")` → 6440.0 (S88 A-N-FW-CANONICALIZATION). `get_constant("a_2_FW_zeta")` → 2776.165389 (S88). `get_constant("a_4_FW_zeta")` → 1350.7216 (S75). `get_constant("dS_fold")` → 58672.80241318. `get_constant("d2S_fold")` → 317862.84898132.
- `get_constant("tau_NEC")` → **NOT FOUND** in the knowledge DB (and absent from `canonical_constants.py`; only `tau_overshoot=1.614` was present at line 2035). Per CLAUDE.md / math-scripts.md (add-to-canonical-first), I added `tau_NEC = 1.383` to `canonical_constants.py` adjacent to `tau_overshoot` with full provenance (NEC-violation onset / physical-domain boundary; S95 W4-5 12D censorship; hawking V.3/V.9; capstone 3-decimal canonical; sp-synthesis fine value 1.382334), then imported it. The knowledge DB will pick it up on the next `/weave --update` extractor run. **Plan-ledger correction note**: the plan §"Wave 3 Input-SHA Ledger" claimed "All present in `canonical_constants.py`" for the consumed canonicals — `tau_NEC` was NOT present; this is the in-session fix.

**Results**

**Canonical value (integer, exact)**: `n_interior_sign_changes(dΓ/dτ) = 0` on the physical domain [0, τ_NEC=1.383].

**Region partition** (interior sign-changes of dΓ/dτ, representation-A canonical):

| Region | n_interior_sign_changes | Note |
|:-------|:------------------------:|:-----|
| [0, τ_now=0.6] | **0** | S95-W2-3 baseline window (was 0; re-confirmed under the LB closed-form flow) |
| **[0, τ_NEC=1.383]** | **0** | *** CANONICAL VERDICT VALUE *** (target 0) → PASS |
| (τ_NEC=1.383, τ_overshoot=1.614] | **0** | censored region (NEC-violating); no sign-change here either → no INFO downgrade needed |
| [0, 1.65] full grid | **0** | the entire computed domain is saddle-free |

**dΓ/dτ diagnostics** (4 sig figs): on [0, τ_NEC], min = **0.3859**, max = **5.852×10⁴**; strictly positive — the min (0.3859) is the τ=0 boundary point where R_K′(0)=0 (finite-difference endpoint residue, still ≫ tol=1e-6); the smallest *interior* value (τ>0) is 1.537. **Fixed-sign confirmation**: `dΓ/dτ` is constant-sign (positive, `sign = +`) across the entire [0, τ_NEC] interior — TRUE. This is the [SIGN] Step-4 prediction confirmed.

**4-tuple**: `(value=0, scheme=SA, convention=EFFECTIVE-ACTION-MONOTONICITY-TREE-PLUS-ONELOOP-FULL-DOMAIN, L_max=10)`.

**Extrapolation-free eigenvalue model (the key full-domain design choice)**: S95-W2-3 Jensen-scaled the cached fold spectrum by a quadratic fit of `ln(1/r)` calibrated on the S36 slices [0.05, 0.22]; extrapolating that quadratic to τ=1.65 is a ~7× extrapolation whose derivative-zero would be a *fit artifact* (the linear `d ln(1/r)/dτ = 2aτ+b` has a single zero at τ*=−b/(2a) that can fall spuriously inside [0, τ_NEC]). This gate instead drives every eigenvalue by the **Lichnerowicz–Bochner identity** `λ_k²(τ) = ν_k + ¼R_K(τ)` (the same closed-form object the sibling S95-W3-5 uses), with `R_K(τ)` the E3 closed form valid for ALL τ — no extrapolation. Runtime-verified: `ν_min = 0.16743950` (= ν_B1, matches S95-W3-5), all 78,080 ν_k > 0, so `λ_k²(τ) = ν_k + ¼R_K(τ) > 0` for all τ (min λ² over grid = 0.6674 at τ=0) ⇒ Tr-ln finite, no zero modes, regime VALID across [0, 1.65].

**CC1 — three-route agreement** (extends the S95-W2-3 routes):
- **Route 1 (tree dS_SA/dτ monotonicity)**: finite-difference `dS_full/dτ` on `S_full(τ)=Σ√(ν_k+¼R_K(τ))` ranges [0.2872, 7.237×10⁴], all > 0 for τ>0. At fold dS_full/dτ = +851.17; its SIGN matches the E7 canonical `dS_fold=+58672.8` (the magnitudes differ by normalization — the canonical +58672.8 is the S42 Σ|λ| gradient-stiffness; this is the LB-closed-form band-bottom-anchored derivative — only the SIGN is verdict-relevant, and it is POSITIVE, E7-consistent).
- **Route 2 (Tr-ln derivative via Jacobi's formula)**: `dΓ₁/dτ` by finite-difference (range [0.09872, 2.071×10⁴]) vs the analytic Jacobi closed form `dΓ₁/dτ = ⅛R_K′(τ)·Σ_k 1/λ_k²` (range [0, 2.080×10⁴]). Max FD-vs-Jacobi rel-dev over the interior = 3.297×10⁻¹, but this is a pure **boundary artifact**: it occurs at the first interior point τ=0.0055 (one-sided `np.gradient` endpoint stencil where R_K′→0); for τ>0.05 the agreement is 0.30%, for τ>0.2 it is 0.018%. Both routes confirm strictly-positive `dΓ₁/dτ` everywhere.
- **Route 3 (combined Γ′, CANONICAL)**: `dΓ/dτ = dS_full/dτ + dΓ₁/dτ` ranges [0.3859, 9.309×10⁴] over the full grid; 0 interior sign-changes on [0, τ_NEC].

**CC2 — 600-point refinement**: a 600-point grid on [0, 0.30] resolving the only place |dΓ/dτ| dips toward the tolerance floor (τ=0, where R_K′(0)=0) returns **0 interior sign-changes** — the boundary dip does not produce a spurious zero crossing.

**Cross-check arm (representation B, alternating curvature-polynomial moment; NOT the canonical verdict)**: `S_SA^(B)(τ) = a_0 − a_2·(R_K(τ)/R_K_fold) + a_4·(R_K(τ)/R_K_fold)²` (the session-96 `s96_sdw_saddle_reginv.py` convention). Its *tree* derivative `dS_SA^(B)/dτ = (−c₂ + 2c₄R_K)·R_K′(τ)` IS sign-changing — it goes negative on τ∈[0, 0.309] with its analytic zero at `R_K* = a_2·R_K_fold/(2a_4) = 2.073966` (τ≈0.31), confirmed numerically (57 grid points negative). **But the rep-B *combined* effective-action derivative `dΓ_B/dτ` stays strictly positive (min = 0.094): the one-loop term dominates and lifts the combined derivative above zero everywhere.** So rep-B yields **0 interior sign-changes of the combined Γ′ on [0, τ_NEC]** as well. The lesson: the alternating-moment tree non-monotonicity is a *representation* feature, NOT a physical interior saddle of the effective action — and even under this stringent (non-sign-fixed-tree) representation, the one-loop completion restores boundary-domination. The canonical verdict uses representation A (Σ|λ|), matching S95-W2-3 which this gate extends.

**Substitution chain (Step 1→4, with substituted numbers)** — claim: "dΓ/dτ has fixed sign with 0 interior sign-changes on [0, τ_NEC] ⇒ Γ[τ] has no interior stationary point ⇒ Z=Σexp(−Γ) is boundary-dominated":
- **Step 1 (definitions)**: `Γ[τ] = S_SA(τ) + ½Tr ln(D_K²/Λ²)`; rep-A tree `S_full = Σ|λ|` (E7 increasing); `Γ₁loop = Σ ln|λ|`; `λ_k²(τ) = ν_k + ¼R_K(τ)` (Bochner; ν_min=0.16743950>0); `R_K(τ) = −¼e^{−4τ}+2e^{−τ}−¼+½e^{2τ}` (E3); canonical a_0_FW_zeta=6440, a_2_FW_zeta=2776.165389, a_4_FW_zeta=1350.7216; E7 PROVEN `dS_SA/dτ` fixed-sign (9,600/9,600); τ_NEC=1.383, τ_overshoot=1.614.
- **Step 2 (substitute, Jacobi's formula)**: `dΓ/dτ = dS_SA/dτ + ½Tr[(D_K²)⁻¹ d(D_K²)/dτ]`. With `d(λ_k²)/dτ = ¼R_K′(τ)` (EXACT, every k, since ν_k is τ-independent), the one-loop term = `⅛R_K′(τ)·Σ_k 1/λ_k²` and the tree term = `⅛R_K′(τ)·Σ_k 1/|λ_k|`.
- **Step 3 (simplify to canonical form)**: `dΓ/dτ = ⅛R_K′(τ)·[Σ_k 1/|λ_k| + Σ_k 1/λ_k²]`. Both bracket sums are strictly positive (λ_k²(τ)>0 all k, all τ); the prefactor `⅛R_K′(τ) ≥ 0` with `R_K′(τ) = e^{−4τ}(e^{3τ}−1)² ≥ 0` (Sage-verified) vanishing ONLY at τ=0.
- **Step 4 (direction read-off, only now)**: for every interior τ∈(0, τ_NEC], R_K′(τ)>0 strict AND both sums>0 ⇒ `dΓ/dτ > 0` strictly ⇒ no interior zero ⇒ `n_sc([0,τ_NEC]) = 0`. The saddle-freeness is **analytic** (R_K′ has its only zero at the genesis boundary τ=0), not a numerical accident — substantiated by the computed values: at fold dΓ/dτ = +1143.59 (FD) / +1143.34 (Jacobi), and the interior minimum dΓ/dτ = 1.537 > 0.

**dual-prior posterior re-allocation** (plan §W3-3): outcome = PASS ⇒ **0.95 to Track A** ("Reading-extends": the tree-term dominance keeps dΓ/dτ fixed-sign to τ_NEC; boundary-domination holds on the full physical domain). Track B ("interior-saddle-appears": the one-loop Tr-ln flips the combined sign on (τ_now, τ_NEC]) is disfavored to 0.05 — the one-loop term shares the tree term's sign by the Jacobi structure (both ∝ ⅛R_K′(τ) × positive sum), so it cannot flip the combined sign.

**GPU-path declaration**: **CPU-cap-OMP8** (`OMP_NUM_THREADS=8`, `MKL_NUM_THREADS=8` set before `import numpy` per `math-scripts.md`). The eigenvalue τ-flow reuses the CACHED L_max=10 band-bottoms scaled by the CLOSED-FORM Lichnerowicz–Bochner law `λ_k²(τ)=ν_k+¼R_K(τ)`; the Tr-ln is a vector reduction over 78,080 pre-cached scalars × 300 τ-points (a CPU vector op, NOT a matrix op — NO eigendecomposition). No off-cache τ block is re-diagonalized, so `torch.linalg.eigvalsh` on the ~9792-dim Peter-Weyl block is NOT invoked (the GPU path would only fire if a block were re-diagonalized; it is not). Wall time 1.48 s.

**Substrate framing (direction held)**: D_K eigenvalues → spectral-action moments a_0(τ)−a_2(τ)+a_4(τ) = S_SA(τ) + the ½Tr ln(D_K²/Λ²) fluctuation determinant → dΓ/dτ fixed positive sign → Z boundary-dominated. The universe **TRANSITS** (supersonic Mach-13.75 sweep through the van Hove fold) because the action S_SA(τ) has no interior critical point to quantize around — only the maximally-symmetric genesis boundary τ=0 to relax FROM. This is the Gibbons–Hawking–York boundary-dominated spectral-action analog. The full-domain extension confirms it holds everywhere the censoring barrier admits the modulus, not just near the fold; r=16ε and n_s=1−6ε+2η remain INAPPLICABLE by absent premises over the entire physical τ-range. We do NOT frame this as "the inflaton field rolls in a potential well" (container / slow-roll relapse).

**CLASS / regulator pins**: CLASS=FULL (closed-form a_n + cached FULL D_K spectrum Tr-ln; NO SCHEMATIC helper; convention carries no `-SCHEMATIC` suffix). Tree moments tagged `a_n^{zeta}`; the ½Tr ln(D_K²/Λ²) one-loop term is the zeta/heat-kernel-log class, `a_n^{zeta}` for consistency.

**Constraint-surface position**: PASS hardens the no-interior-saddle / boundary-domination structural result (einstein §II.2; berry CF-BERRY-MASLOV-WKB; hawking V.9; feynman F-5) from the [0, τ_now] window to the full physical domain [0, τ_NEC=1.383] — and (a stronger-than-INFO bonus) through the censored overshoot τ=1.614 too: there is no interior saddle anywhere the modulus could in principle reach. No constraint corridor is reopened; the transit-not-slow-roll reading is reinforced over the entire physical τ-range.

---

## Wave 3 Synthesis (team-lead)

**Wave 3 (CRITICAL focused wave; 3 gates, all `gen-physicist`, all `[SIGN]`).** All three closed PASS — each verified on disk (verdict line + dual-SHA companion + schema-v2 3-tuple + WP §-section `must_contain` + script/data/plot present, nonzero). Per `feedback_reporting-framing.md`: no session-aggregate PASS/FAIL metric — each gate's constraint-surface position is reported individually.

### Gate-by-gate constraint-surface position

**§W3-1 S96-EP-NNLO-CASIMIR — PASS. C3 RESOLVED.** `Δκ = κ_EP^NNLO(B1) − κ_EP^NNLO(B3) = −0.00839709` (FI — `a₆^{Mellin}` and `a₆^{zeta}` agree on sign). The substrate makes its **first value-bearing equivalence-principle prediction** at NNLO; frontier #8 escapes the generic-identity ceiling that `κ_EP^NLO = 1` sat on. Substrate-anchored, no free magnitude knob: `g0 = (1/45)·(a₆_FW_zeta/a₄_FW_zeta)/dim_adj` — Gilkey heat-kernel rationals × the substrate's own NNLO/NLO moment ratio. Sign PRE-registered (`−sign(g0)`, `g0>0`, `C₂(B3)−C₂(B1)=+4/3>0 ⇒ Δκ<0`), confirmed. Band-dependent free fall at second order in fiber curvature distinguishes the substrate from any generic single-metric emergent-gravity / Brans–Dicke / bimetric model. Dual-prior → Track A 0.9. Opens a new falsifiable substrate EP corridor; closes none.

**§W3-2 S96-LEGGETT-GAMMA-GRAV — PASS (value reconciled in-session). D1 RESOLVED.** `Γ_grav/H_0 = 3.31e-66` (margin_OOM 65.5), ε-INDEPENDENT canonical pair channel (`2L→2g`, Δn_L=−2 even). The naive single-Leggett channel `L→g+g` (~`2.93e39·H_0` — the S66 "cosmologically instant" open-problem flag, the source of the "UNCOMPUTED CRITICAL" reading) is **Z₂-parity-forbidden to exactly zero** (Δn_L=−1 odd) + graviton-gap kinematically protected; the surviving pair channel sits ~66 OOM below H_0. The deliverable reproduces the S67/S73a archive (`3.31e-66`, rel-diff 3.2e-4) and sits 0.43 OOM from the cited anchor `8.85e-66`. D1's defined-PASS ∧ UNCOMPUTED-CRITICAL simultaneity is reconciled structurally. Dual-prior → Track A (nazarewicz PASS-confirm) 0.97 — PASS-confirms nazarewicz's reading WHILE supplying the explicit re-pinned margin the open-CRITICAL readers (landau/mack/hawking) correctly flagged as uncomputed. The Leggett-channel-DM corridor is confirmed open by ~66 OOM; the σ/m=0 superselection-protected DM claim is no longer hostage to an uncomputed rate.

**§W3-3 S96-W3-SADDLE-FULLDOMAIN — PASS.** `n_interior_sign_changes(dΓ/dτ) = 0` on the physical domain `[0, τ_NEC=1.383]` (and 0 through the censored overshoot τ=1.614; 0 on the full `[0,1.65]` grid). The no-interior-saddle / Gibbons–Hawking–York boundary-domination result is hardened from the S95-W2-3 `[0,τ_now]` window to the **full physical domain**. The PASS is analytic, not grid-numerical: `dΓ/dτ = ⅛R_K′(τ)·[Σ1/|λ| + Σ1/λ²]` with `R_K′(τ)=e^{−4τ}(e^{3τ}−1)² ≥ 0` vanishing ONLY at the genesis boundary τ=0, and all 78,080 `ν_k>0 ⇒` both bracket sums strictly positive `⇒ dΓ/dτ>0` at every interior τ. Three-route agreement (tree `dS_SA/dτ`, Tr-ln Jacobi, combined Γ′); rep-B cross-check (alternating-moment tree non-monotone but combined Γ′ still strictly positive — boundary-domination robust to representation choice). Dual-prior → Track A 0.95. Transit-not-slow-roll reinforced over the entire physical τ-range; `r=16ε`, `n_s=1−6ε+2η` remain INAPPLICABLE by absent premises everywhere, not just near the fold. Reopens no corridor.

### What Changed

**(a) Numerical revisions**
- Leggett margin: `Γ_grav/H_0 = 1.11e-68 → 3.31e-66` (margin_OOM 68.0 → 65.5); ε-dependent-band → ε-independent single value (in-session reconciliation — removed an unjustified `ξ_eff·(ε/ω_L1)` ansatz; verdict PASS unchanged; Option-A supersedes re-emit).
- First substrate EP-prediction magnitude pinned: `Δκ = −0.00839709` (6 sig figs; FI).
- `tau_NEC = 1.383` backfilled to `canonical_constants.py` (was absent; plan ledger inaccurate).

**(b) Structural changes**
- EP epistemic-type promotion: **generic-identity-cored (NLO `κ_EP=1`, Lichnerowicz universal-¼) → value-bearing substrate prediction (NNLO `Δκ≠0`)**. The EP is now substrate-PREDICTIVE, not an identity any spin Dirac operator shares.
- D1 dissonance resolution: **LEGGETT-GRAV-DECAY-67 defined-PASS-∧-UNCOMPUTED-CRITICAL simultaneity → resolved** via the two-channel structural split (Z₂-forbidden single channel + surviving pair), with an explicit re-pinned margin replacing the cited archive figure.
- Boundary-domination scope: **`[0,τ_now]` window → full physical domain `[0,τ_NEC]`** (analytic backing, not grid extension).

### C3 / D1 resolution status

- **C3 RESOLVED**: frontier #8 (emergent equivalence principle) ESCAPES the generic-identity ceiling — the substrate's first value-bearing EP prediction (`Δκ=−0.00839709`, FI).
- **D1 RESOLVED**: `LEGGETT-GRAV-DECAY-67` conditional DISCHARGED with an explicit, archive-consistent, first-principles margin (`Γ_grav/H_0=3.31e-66`, ~66 OOM); nazarewicz's PASS reading confirmed WHILE supplying the margin the open-CRITICAL readers flagged uncomputed. No D1 workshop needed (PASS, not INFO).

### Capstone-hygiene 5-question gate (`.claude/rules/capstone-hygiene-gate.md`; W3 touches capstone-governing registers)

W3 touches the §7 falsifier surface (Leggett-DM margin) and the PROVEN/CONDITIONAL status ladder (frontier #8 EP; LEGGETT-GRAV-DECAY-67), so the standing gate runs:
- **Q1 (a(t)/effective-Friedmann gap)**: NO — W3 does not touch a(t)/FRW (that is W1 / cluster C1).
- **Q2 (§7 falsifier-anchor row)**: **YES** — the Leggett-DM margin row (`Γ_grav/H_0=3.31e-66`) + the NNLO EP-prediction row → `mack-cosmic-bridge` (sole writer of the §7 falsifier surface + `falsifier-master-inventory.md`).
- **Q3 (PROVEN/CONDITIONAL/BROKEN/INFO status change)**: **YES** — frontier #8 EP generic→value-bearing; LEGGETT-GRAV-DECAY-67 CONDITIONAL-on-uncomputed → CONDITIONAL-on-PASSED-with-explicit-margin → reconcile capstone prose tags vs Atlas D04 + permanent-results registry.
- **Q4 (PROSE claim vs ledger row)**: **YES** — the §7.1 D1 framing correction (nazarewicz §IV.4 + landau V.5: "the conditional is satisfied, not open") is a PROSE change → designated-writer reviewed patch; the frontier-#8 EP scorecard row is prose.
- **Q5 (citation add/invalidate)**: **YES** — adds the S96-EP-NNLO-CASIMIR + S96-LEGGETT-GAMMA-GRAV citations; the re-pinned Leggett margin (`3.31e-66`) supersedes the cited-archive (`~8.85e-66`) annotation.

Routing: Q2/Q3/Q4/Q5 YES → capstone-update actions route to the **session-close capstone-hygiene reconciliation** (mack-cosmic-bridge for the §7 falsifier surface + `falsifier-master-inventory.md`; the designated writer for the §7.1/§9 capstone prose) — NOT bulk-appended mid-wave, NOT orchestrator-direct (sole-writer / designated-writer constraints). Recorded in `session-96-housekeeping.md §D`. This W3 run advances the capstone-hygiene K-counter (it caught real status drift: the EP frontier promotion + the D1 resolution + the Leggett margin re-pin superseding the cited archive figure).

### Effected in-session (non-math; agent/orchestrator-direct, this wave)

- [x] **`tau_NEC = 1.383` backfilled to `canonical_constants.py`** — `saddle` agent (S96-W3-SADDLE-FULLDOMAIN) added it adjacent to `tau_overshoot` (line 2036) with inline provenance matching the sibling τ-landmark convention; the plan's Input-SHA ledger wrongly claimed it present. Verified queryable (`get_constant("tau_NEC")=1.383`) and convention-consistent with `tau_overshoot` (no Section-F PROVENANCE-dict entry needed — neither τ-landmark uses one; adding one for `tau_NEC` alone would be inconsistent). — `computations/_shared/canonical_constants.py:2036`
- [x] **Leggett margin value reconciled (`1.11e-68 → 3.31e-66`)** — `leggett` agent (S96-LEGGETT-GAMMA-GRAV), via orchestrator `SendMessage` continuation, removed an unjustified `ξ_eff·(ε/ω_L1)` ε-scaling ansatz and pinned the ε-independent canonical GL pair prescription (`ξ_eff=frac_d2a2·φ_zp²=2.131`); re-emitted via Option-A supersedes (original `37c46ca0…` retained byte-for-byte; corrective `d1c7bd61…` carries the full-64-char `supersedes` pointer); composite verdict PASS unchanged. — `computations/session-96/s96_gate_verdicts.txt:63–71` + WP §W3-2

Self-audit: `grep -c '^- \[ \]'` on this Effected-in-session sub-section = 0 (no unchecked items).

## Carry-Forward Computations

One genuine math carry-forward (all three gates PASSed; only the W3-1 PASS routing seeds a forward compute). The FAIL/INFO-routed candidates in the plan's decision-point table did NOT fire (no INFO, no FAIL this wave).

### CF-S97-W3-1 — N3LO equivalence-principle confirmation gate

> Routing: from the §"Wave 3 → Wave 4 Decision Point" S96-EP-NNLO-CASIMIR **PASS** routing (c) — pre-registered as a carry-forward, NOT created this session. Confirmation/robustness gate, not blocking (W3-1 already established the NNLO escape is FI).

| Field | Spec |
|:--|:--|
| **What** | Compute `Δκ^N3LO = κ_EP^N3LO(B1) − κ_EP^N3LO(B3)` from the `a₈` Gilkey heat-kernel polynomial (third order in fiber curvature `R_K`), confirming the NNLO value-bearing EP prediction (`Δκ=−0.00839709`) is sign-stable and `|Δκ|>1e-4` persists at next order; FI cross-check `a₈^{Mellin}` vs `a₈^{zeta}`. |
| **Inputs** | `computations/session-96/s96_w3_1_ep_nnlo_casimir.npz` (`Δκ`, `g0`, `a₆/a₄` ratio); `a_8_FW_zeta=521.183178` (canonical, promoted S96 W2-5) + the `a₈` Gilkey rational coefficients; cached L_max=10 band-bottoms (`computations/session-84/s84_spectrum_cache_L12_tau019.npz`); `ν_B1`/`ν_B3`, `C₂(B1)=0`/`C₂(B3)=4/3`. |
| **Gate** | `S97-EP-N3LO-CASIMIR`. PASS iff `sign(Δκ^N3LO)=sign(Δκ^NNLO)` AND `|Δκ^N3LO|>1e-4` AND FI (`a₈^{Mellin}`/`a₈^{zeta}` sign-agree); INFO iff sub-resolvable (`1e-8<|Δκ^N3LO|≤1e-4`) OR scheme sign-disagreement (RD); FAIL iff the N3LO term flips the sign or cancels the NNLO prediction (genericity re-emerges at third order). |
| **Effort** | ~1 wave (reuses the W3-1 `a₆` machinery + cache; new work is the `a₈` polynomial's `R_K`-cubic cross-term + its FI partition). |

No other math carry-forwards: W3-2 reconciled cleanly (PASS, archive-consistent — no further compute); W3-3 PASS analytically (no compute follow-on). The W3-1/W3-2 PASS verdicts also route NON-MATH registry/capstone writes to `mack-cosmic-bridge` (sole writer) — the §7 falsifier-inventory NNLO-EP-prediction row + the Leggett-DM margin row + the §7.1 D1 framing correction + the frontier-#8 §7/§9 scorecard row + the `Ω_DM`-conditional upgrade — recorded in `session-96-housekeeping.md §D` (capstone-hygiene routing), to land at the session-close capstone-hygiene reconciliation, NOT as S97 compute.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-05-29 | C3 / frontier #8 (emergent EP) | generic-identity-cored (NLO `κ_EP=1`; Lichnerowicz universal-¼) | value-bearing substrate prediction (NNLO `Δκ=−0.00839709`, FI) | S96-EP-NNLO-CASIMIR PASS — the `a₆` field-strength cross-term `Tr(F^b F^b)~C₂(b)` is band-specific; escapes the genericity ceiling |
| 2026-05-29 | D1 / LEGGETT-GRAV-DECAY-67 | defined-PASS ∧ UNCOMPUTED-CRITICAL (margin cited from S67/S73a archive, not re-pinned) | RESOLVED — conditional discharged with explicit first-principles margin `Γ_grav/H_0=3.31e-66` (~66 OOM) | S96-LEGGETT-GAMMA-GRAV PASS (reconciled); two-channel split (Z₂-forbidden single + surviving pair) |
| 2026-05-29 | no-interior-saddle / GHY boundary-domination | PASS on `[0,τ_now]` (S95-W2-3) | hardened to full physical domain `[0,τ_NEC=1.383]` (analytic) | S96-W3-SADDLE-FULLDOMAIN PASS — `dΓ/dτ>0` strict for all interior τ |
| 2026-05-29 | (process) `tau_NEC` canonical | absent from `canonical_constants.py` (plan ledger claimed present) | added (line 2036) + queryable | in-session backfill (`saddle`); plan-ledger inaccuracy logged |
| 2026-05-29 | (process) Leggett margin deliverable | `1.11e-68` (unjustified ε-scaling ansatz) | `3.31e-66` (ε-independent canonical GL pair prescription; Option-A supersedes) | in-session reconciliation (`leggett`, via SendMessage); verdict PASS unchanged |
| 2026-05-29 | (process) WP shared-write | 3 agents editing `session-96-w3-workingpaper.md` concurrently | resolved (mtime races retried; no data loss) | process observation — >2-gate single-WP waves are a shared-write hotspot; consider per-section WP files or write-serialization for future >2-gate waves |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Size (script / data / plot, bytes) |
|:--|:--|:--|:--|:--|
| S96-EP-NNLO-CASIMIR | `computations/_shared/s96_w3_1_ep_nnlo_casimir.py` | `computations/session-96/s96_w3_1_ep_nnlo_casimir.npz` | `computations/session-96/s96_w3_1_ep_nnlo_casimir.png` | 44409 / 24024 / 130953 |
| S96-LEGGETT-GAMMA-GRAV | `computations/_shared/s96_w3_2_leggett_gamma_grav.py` | `computations/session-96/s96_w3_2_leggett_gamma_grav.npz` | `computations/session-96/s96_w3_2_leggett_gamma_grav.png` | 42084 / 18177 (regenerated) / 117840 |
| S96-W3-SADDLE-FULLDOMAIN | `computations/_shared/s96_w3_3_oneloop_saddle_fulldomain.py` | `computations/session-96/s96_w3_3_oneloop_saddle_fulldomain.npz` | `computations/session-96/s96_w3_3_oneloop_saddle_fulldomain.png` | 48514 / 64326 / 184611 |

**Also modified**: `computations/_shared/canonical_constants.py` (`tau_NEC = 1.383` added, line 2036); `computations/session-96/s96_gate_verdicts.txt` (W3 gate lines — W3-1 lines 60–62, W3-2 lines 63–65 original + 69–71 corrective via Option-A supersedes, W3-3 lines 66–68).
