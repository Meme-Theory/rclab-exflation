# Session 99 Synthesis: C10/CC Residual — Substrate Early-Vacuum Time-Profile ρ_vac(a) vs the Joint BBN+CMB+BAO ΔN_eff Budget (X-cut, Tier-1 #2)

**Date**: 2026-06-04
**Agent**: volovik-superfluid-universe-theorist (volovik)
**Cross-cutting layer**: X1 second-layer review — bridges the G2 dark-energy/BBN observational frontier and the G1 emergent-spacetime/q-theory frontier onto the standing C10/CC residual (Tier-1 #2).
**Source Documents**:
- `downloads/research-sweep-s99/dark-energy-observational/00-INDEX.md` (G2; papers 09 Allali-Notari-Rompineve, 10 Seto-Toda, 11 Goldstein-Hill the load-bearing BBN trio)
- `downloads/research-sweep-s99/emergent-spacetime-superfluid/00-INDEX.md` (G1; papers 02 Volovik dS-thermo, 04 Klinkhamer-Savelainen-Volovik q-theory relaxation, 06 Klinkhamer-Volovik DM-from-DE)
- `sessions/archive/session-99/session-99-litrev-dark-energy-mack.md` (R1, G2, mack — INPUT, not authority)
- `sessions/archive/session-99/session-99-litrev-dark-energy-sagan.md` (R1, G2, sagan — INPUT, not authority)
- `sessions/archive/session-99/session-99-litrev-emergent-spacetime-volovik.md` (R1, G1, volovik — INPUT, not authority)
- `sessions/archive/session-99/session-99-litrev-emergent-spacetime-phonon-first.md` (R1, G1, phonon-first — INPUT, not authority)
- Canonical state via knowledge MCP (queried 2026-06-04): gates `S98-MK3-2-BBN-VACUUM-FRACTION`, `S99-W2-BBN-RELIEF`, `S99-W2-RELAXATION-CLOSURE`, `S99-W1-Q-NONRATIO-OBSERVABLE`, `S98-MK3-1-C10-SUBLEADING-SIGN`, `DILUTION-CC-66`; constants `delta_N_eff_vacuum_BBN_below`, `rho_vac_over_rho_rad_BBN_below`, `rho_vac_over_rho_obs`, `N_eff_SM`, `T_BBN_GeV`, `z_BBN`, `a_0_FW_zeta`; plan `session-99-plan-w2.md` §W2-2; WP `session-99-w2-workingpaper.md` §W2-2

---

## I. Session Outcome

The C10/CC-residual constraint surface, as it stands at S99 close, is mischaracterized by "the BBN arm FAILs ~19.5× short." The canonical `S99-W2-BBN-RELIEF` gate FAILed on **one specific axis** — the **magnitude axis at a fixed all-history exponent**: it asked whether a larger from-below shift Δn, an epoch-dependent α_V, or a distinct mode-count dilution channel could reduce the BBN-epoch fraction `(ρ_vac/ρ_rad)_BBN = 0.474049` to `ΔN_eff ≤ 1` while ρ_vac remains **present at BBN with full magnitude**, and found none substrate-justified. That corridor is canonically CLOSED (structural). It is NOT the corridor the literature opens. Papers 09 (Allali-Notari-Rompineve), 10 (Seto-Toda), and 04/02 (Klinkhamer-Savelainen-Volovik / Volovik) open the **orthogonal time-profile / epoch-placement axis** — whether ρ_vac is *present at BBN at all* — which neither S98 nor S99 has tested. On that axis the relief is not "shrink ρ_vac" but "the substrate's a₀ tracking-vacuum may be negligible at the BBN epoch and build up later," in which case the BBN-epoch fraction the C10 gate computes is not the operative number.

The decisive reconciliation against canonical: **the ΔN_eff < 0.107 budget the G2 sweep (papers 09/11) and all four R1 syntheses score against is NOT a canonical pin** — `list_constants` returns no match; the canonical bound is the gate's own `0.227107 = (7/8)(4/11)^{4/3}` (i.e. `ΔN_eff ≤ 1`). The substrate value 2.0873 fails BOTH (2.087× over the canonical bound, **19.51× over the external 0.107**, Sage-exact). Adopting 0.107 roughly **doubles** the required relief: the extra suppression factor goes from ×0.479 (to clear `ΔN_eff ≤ 1`) to **×0.051** (to clear 0.107). This makes the magnitude axis even more hopeless — and makes the **time-profile axis the only surviving corridor**, exactly as papers 09/10 argue for dark radiation and EDE.

The deliverable below is a **relief-corridor map** (which corridors are open/closed/conditional and on what) plus a pre-registerable BBN-arm relief gate (`S100-X-C10-RHOVAC-EPOCH-PROFILE`) and its composition with the live `CF-S100-W2-1-QEQ-DRIVE` successor. No gate verdict is re-adjudicated; all four R1 adjudications are treated as input.

---

## II. Key Results

### II.1 — The S99-W2-BBN-RELIEF FAIL is an axis-FAIL, not an arm-FAIL: the magnitude corridor closed, the time-profile corridor was never opened

**Result**: `S99-W2-BBN-RELIEF` = **FAIL** (canonical; audit `8fe0ef45…`), 3-tuple `sign=PASS / magnitude=FAIL / regime=VALID`, Track-B structural. The three tested relief mechanisms (`s99_w2_bbn_relief.npz`, WP §W2-2 table) each reach `ΔN_eff = 1` only at a non-substrate parameter: (a) larger from-below shift requires `n_eff = 1.959839` (1.835× the HARD substrate shift; Sage-confirmed) vs substrate `n_eff = 1.978111`; (b) epoch-dependent α_V requires `α_V,BBN/α_V,0 = 0.479080` (DILUTION-CC-66 uses ONE α_V); (c) distinct dilution channel requires 475 of 992 D_K modes contributing (all 992 gravitate, `a₀ = ζ_{D_K}(0) = Tr(1)`). Classification: **PHONONIC** (the BBN-epoch fraction is the a₀ tracking-vacuum `ρ_vac = α_V M_Pl² H^{n_eff}` evaluated at the radiation-dominated BBN epoch).

The structural reading the canonical gate text makes explicit (WP §W2-2): all three mechanisms vary the **amplitude or exponent of an all-history tracking law** while holding ρ_vac **present at BBN with full magnitude 0.474**. None of them is the question papers 09/10 pose. Papers 09/10 ask whether ρ_vac is *present at BBN at all* — i.e. whether the substrate's a₀ tracking-vacuum has an **EDE-like time-profile** (peaked near matter-radiation equality, ρ_vac ∝ a^{−n} with n ≥ 4, negligible at T ~ 1 MeV) or is **post-BBN-produced** (ρ_vac ≈ 0 for T > 1 MeV, builds later). On the EDE-like or post-BBN profile, `(ρ_vac/ρ_rad)_BBN → ~0` **regardless** of the present-epoch tracking exponent n_eff = 1.978 — because the operative quantity is the fraction *at the BBN epoch*, not the present-epoch normalization the lever X = ln(H_BBN/H_0) = 40.2756 transports.

This is a genuine opening, not a re-run of a closed gate. The S99 lever `(ρ_vac/ρ_rad)_BBN = frac_base · exp((n_eff−2)·X)` assumes the tracking law `ρ_vac = α_V M_Pl² H^{n_eff}` holds **continuously from BBN to today** (all-history). That is precisely the "radiation-like / all-history constant-fraction" worst-case paper 10 (Seto-Toda) identifies and contrasts with the EDE-like (epoch-localized) case. The C10 arm currently bakes in the worst case. Whether the substrate's a₀ profile is worst-case or EDE-like is a **substrate-physics question the framework has not answered** — and it is the load-bearing question for whether C10's BBN arm is robustly falsified or relieved.

### II.2 — The external budget is non-canonical; adopting 0.107 doubles the relief requirement and forces the combined-window evasion

**Result**: `ΔN_eff < 0.107` (Goldstein-Hill 2026, paper 11, combined BBN+CMB+BAO, N_eff = 2.990 ± 0.070) is **NOT a canonical constant** (`list_constants("N_eff|delta_N|BBN|107")` returns `delta_N_eff_vacuum_BBN_below = 2.0873`, `N_eff_SM = 3.044`, and the BBN η/g_star/z pins — no 0.107). The canonical bound the gate scores against is `0.227107 = (7/8)(4/11)^{4/3}` (`ΔN_eff ≤ 1`). Classification: **NON-PHONONIC** (an external observational threshold; the substrate value is the PHONONIC object).

**Conflict flag (volovik R1 conflict #1 confirmed and sharpened).** The volovik R1 synthesis flagged that the index's "0.107 bound" matches no canonical pin; I confirm this against `list_constants`. The mack and sagan R1 syntheses both score the FAIL against 0.107 (giving 19.51×); the phonon-first R1 treats 0.107 as "the external bound, 2.0873 the framework value, no conflict." All three readings are defensible because they are about *different objects*: 2.0873 is the framework PREDICTION; 0.107 and 0.227 are two BUDGETS at different tightness. The honest accounting (Sage-exact):

| Budget | Source | Status | Exceedance of 2.0873 | Extra suppression to clear |
|:-------|:-------|:-------|:---------------------:|:--------------------------:|
| `ΔN_eff ≤ 1` (`ratio ≤ 0.227107`) | canonical S66 formula; the gate's own bound | **CANONICAL** | **2.087×** | ×0.479 |
| `ΔN_eff < 0.46` (fluid DR) / `< 0.39` (free-stream), CMB-era | paper 09 (Allali et al., DESI+Planck+Pantheon+) | external, looser | 4.54× / 5.35× | ×0.110 / ×0.092 |
| `ΔN_eff < 0.107` (combined BBN+CMB+BAO, 95%) | paper 11 (Goldstein-Hill 2026), N_eff=2.990±0.070 | external, tightest | **19.51×** | **×0.051** |

The structural consequence is sharp: against the canonical bound the time-profile relief needs ρ_vac at BBN suppressed by ×0.479 (a factor ~2); against 0.107 it needs ×0.051 (a factor ~20). Crucially, paper 11's bound is **combined BBN + CMB + BAO**, so a time-profile relief must show ρ_vac negligible at **both** the BBN epoch (T ~ 1 MeV) AND the CMB-N_eff-sensitive epoch (recombination) — strictly stronger than paper 10's BBN-only evasion. An EDE-like profile peaked *at* matter-radiation equality (between BBN and recombination) could in principle clear BBN while remaining visible at recombination, FAILing the combined window. This is the discriminator the relief gate must resolve.

**Do not propagate 0.107 as canonical** (per `substrate-first-canonical-sourcing.md §(i)`; volovik R1 conflict #1). The relief gate below pre-registers BOTH budgets as thresholds with explicit currency tags: canonical `ΔN_eff ≤ 1` as the PASS gate, external 0.107 as the INFO/stretch gate.

### II.3 — Corridor (a) post-BBN production (paper 09) is OPEN, gated by the substrate transit/GGE chronology, NOT yet checked

**Result**: Paper 09 (Allali-Notari-Rompineve) — BBN element-abundance bounds on ΔN_eff "are avoided if DR is produced AFTER Big Bang Nucleosynthesis." Classification: **PHONONIC** (the substrate analog is whether the a₀ tracking-vacuum / GGE-relic complexification builds up post-BBN).

In substrate language: if the spectral reorganization that sources ρ_vac (the a₀ zeroth-moment buildup / GGE occupation) completes **after** the BBN window (T < 1 MeV, T_BBN_GeV = 0.001 canonical, z_BBN = 4×10⁸), then `(ρ_vac/ρ_rad)_BBN = 0.474049` the C10 gate computes is **not** the BBN-time value — it is the present-epoch tracking value transported back via the lever X under the all-history assumption. The element-abundance bounds (D/H, Y_P) would then not apply, exactly as for post-BBN dark radiation.

**What gates this corridor (the substrate-physics it requires).** The framework's reheating/transit chronology places the fold transit and GGE-relic formation at the van Hove fold (τ_fold = 0.19) at extremely high energy. The R1 syntheses cite T_RH = 1.70e15 GeV (mack/sagan), but **I could not confirm T_RH as a canonical constant** (`get_constant("T_RH")` returned not-found — flagged as a hygiene item). If GGE-relic formation completes at T_RH ≫ T_BBN, the question is whether the a₀ tracking-vacuum that DILUTION-CC-66 carries to today is **continuously present** from T_RH down through BBN (all-history, the current C10 assumption), or whether the *gravitating* part of ρ_vac (the part that enters the modified Friedmann lever) only becomes significant at lower H. The Volovik equilibrium theorem (`ρ_V(q) = ε(q) − q dε/dq = 0` at equilibrium, paper 04 / S95 EQUILIBRIUM-CC-WARRANT) is the structural handle: the *gravitating* vacuum energy is the deviation from equilibrium, and if the substrate is near-equilibrium during the radiation era and only departs as H drops, the gravitating ρ_vac at BBN could be far below the all-history tracking value. **This is unchecked.** It is the substrate-chronology computation the relief gate needs.

**Status: OPEN, conditional on the substrate transit/GGE chronology placing the *gravitating* ρ_vac buildup post-BBN.** This corridor is distinct from everything S99-W2-BBN-RELIEF tested (which assumed full-magnitude presence at BBN). Per `epistemic-discipline.md`, it is a math/physics adjudication (whether the gravitating-ρ_vac time-profile is post-BBN), not a registry re-tag.

### II.4 — Corridor (b) EDE-like dilution (paper 10) is OPEN with a known residual side-channel; the Volovik f(R) profile (paper 02) is the concrete substrate candidate

**Result**: Paper 10 (Seto-Toda, FOUNDATIONAL) — EDE "significantly contributes only around matter-radiation equality to recombination and its energy density decreases quickly [ρ_DE ∝ a^{−n}, n=4 or 6], whereas extra radiation exists throughout the whole history." EDE's BBN-epoch density is negligible ⇒ evades the *direct expansion-rate* channel, BUT is "subject to BBN constraints by increasing the order-unity χ²" through the **inferred Ω_b h² → D/H** side-channel. Classification: **PHONONIC** (the substrate's a₀ profile epoch-dependence).

The substrate candidate for the EDE-like profile is concrete: paper 02 (Volovik 2025, dS thermodynamics) gives `ε_vac(H) = f(R = 12H²)` with equilibrium curvature `2f(R) = R·df/dR`, where the "cosmological constant is NOT fundamental but a part of the gravitational DOF that relaxes through interactions with matter" (the m→3m triplication avalanche). In the Volovik↔project mapping (volovik R1 Result 2, phonon-first R1 II.2), `K = df/dR ↔` spectral gradient-stiffness Z(τ) and `G = 1/16πK ↔ a₂` second spectral moment. The early-time ρ_vac(a) implied by a given f(R) form has a **computable** radiation-era behavior. If the substrate-fixed f(R) gives an EDE-like (epoch-peaked, fast-diluting) profile, the direct expansion-rate BBN channel is evaded — but paper 10's warning stands: the framework must then check the **Ω_b h² → D/H side-channel** separately (fitting the CMB requires increased Ω_b h², which reduces D/H and raises χ²_Cooke).

**The two-stage structure of corridor (b)** (faithful to paper 10):
1. **Stage 1 — direct expansion-rate evasion**: ρ_vac(a_BBN)/ρ_rad(a_BBN) ≪ 0.227 under the f(R)-emergent profile (evades H² = (8πG/3)(ρ_rad + ρ_vac) at BBN). This is the gate's primary PASS condition.
2. **Stage 2 — Ω_b h² → D/H residual**: the CMB-fit-required Ω_b h² shift propagates to D/H vs Cooke+18 (2.527±0.030 ×10⁻⁵). This is a CONDITIONAL sub-gate, fires only if Stage 1 passes.

**Status: OPEN, conditional on (i) the substrate f(R) form yielding an EDE-like profile AND (ii) clearing the Ω_b h² → D/H side-channel AND (iii) — under the 0.107 combined budget — remaining negligible at recombination, not just BBN.** The triple conjunction is what makes this corridor genuinely hard, not automatic.

### II.5 — The S66 n_eff direction is the key un-exploited lever: from-ABOVE (n_eff > 2) historically PASSed the 2% G_eff bound; the S98/S99 from-BELOW pin (n_eff < 2) is the one that FAILs

**Result**: Canonical S66 workshop (`session-66-mack-transit-workshop.md`, surfaced via `search_knowledge`): `n_eff = 2.3 → α(BBN) ~ 0.01, G_eff ~ 1.03G, within 2% bound, PASS`; `n_eff = 2 (Volovik baseline) → α(BBN) = 0.67, EXCLUDED (G_eff = 3G)`; `n_eff < 2 (Mack acoustic-GGE-pressure estimate) → α(BBN) > 0.67, EXCLUDED`. Classification: **PHONONIC** (the Gibbs-Duhem exponent of the a₀ tracking-vacuum).

This is a load-bearing canonical anchor the G2 sweep did not surface and the R1 syntheses did not connect. The BBN relief is **monotone in the tracking exponent**: a steeper exponent (n_eff > 2, from-ABOVE) suppresses ρ_vac MORE strongly at high H (BBN), because `(ρ_vac/ρ_rad)_BBN = frac_base · exp((n_eff−2)·X)` with X = +40.2756, so `(n_eff − 2) > 0 ⇒ exp((n_eff−2)·X) ≫ 1` — wait, the sign goes the OTHER way for the *fraction* but the right way for the *G_eff* bound. The substitution chain must be written explicitly:

```
Claim: the direction in n_eff that relieves the BBN tension.
Def 1: (ρ_vac/ρ_rad)_BBN = frac_base · exp((n_eff − 2)·X),  X = ln(H_BBN/H_0) = +40.2756  [S99 W2-2 lever, canonical]
Def 2: ρ_vac/ρ_rad and ρ_rad both scale; the falsifier is ΔN_eff = (ρ_vac/ρ_rad)_BBN / 0.227107
Substitute the two n_eff cases:
  from-below n_eff = 1.978111: (n_eff−2) = −0.021889 < 0 ⇒ exp(−0.021889·40.2756) = 0.4141 ⇒ frac = 0.474, ΔN_eff = 2.087  [the S98/S99 FAIL]
  from-above n_eff = 2.3:       (n_eff−2) = +0.3 > 0      ⇒ exp(+0.3·40.2756) = e^{12.08} ≫ 1                    ⇒ frac ≫ 1, EXCLUDED HARD
Read off: in the LEVER form the from-ABOVE direction makes the BBN fraction LARGER (worse), the from-BELOW makes it smaller (better).
```

So the **lever-form** (S98/S99) and the **G_eff-form** (S66) point in OPPOSITE directions on n_eff, which is a genuine tension between two canonical sessions and MUST be flagged. The S66 reading had `n_eff = 2.3 PASS` via the G_eff(BBN) = 1.03G route (a 2% gravitational-constant bound at BBN); the S98/S99 reading has `n_eff = 1.978 FAIL` via the ΔN_eff lever route. **These cannot both be the operative BBN constraint with the same sign convention on n_eff.** Resolving which (G_eff 2% bound vs ΔN_eff lever) is the correct BBN falsifier — and which n_eff direction relieves it — is a pre-requisite for any relief gate. I flag this as a conflict between canonical sessions (§IV.1), not resolved here.

### II.6 — The q-theory relaxation profiles (papers 04/02/06) are candidate ρ_vac(a) time-profiles, and the live CF-S100-W2-1-QEQ-DRIVE successor is the right place to compute them — but it currently targets the WRONG observable for the BBN arm

**Result**: `CF-S100-W2-1-QEQ-DRIVE` (canonical carry-forward, `session-99-w2-workingpaper.md §"Carry-Forward Computations"`) derives a substrate-internal `q_eq(H)` drive for the **unforced n=2 attractor test** (the W2-1 relaxation-closure leg), NOT for the BBN time-profile. Classification: **PHONONIC** (the q-variable relaxation IS the substrate's a₀ vacuum dynamics).

The papers supply three candidate drives, each a computable ρ_vac(a):
- **Paper 04** (Klinkhamer-Savelainen-Volovik): the friction ODE `q″ + 3Hq′ + V′(q) = 0` with quadratic dissipation `qS = Γ_q(∂_t q)² + Γ_H(∂_t H)²` IS the C10 Object-C ODE (volovik R1 Result 2, phonon-first R1 II.4). Its `u_eff(τ)` trajectory `−0.883133 → −1/3` is a concrete vacuum-energy time-profile; the Minkowski endpoint is reached only on a measure-zero separatrix. The "de Sitter must decay" conclusion aligns with the transit-not-equilibrium paradigm.
- **Paper 02** (Volovik dS-thermo): `ε_vac(H) = f(R = 12H²)`, matter-coupled relaxation via m→3m. The early-time ρ_vac(a) is set by the chosen f(R) form (corridor (b), §II.4).
- **Paper 06** (Klinkhamer-Volovik): static δq (DE) + oscillating q₀ξ (DM) split; the static-δq is the present-epoch offset, not an early-time profile.

**Critical scope correction (the central X-cut finding).** The S99 W2-1 FAIL established (WP §W2-1, confirmed canonical) that `d ln q/d ln H = 1` (n=2) emerges ONLY under an imposed linear closure `q_eq = c·H`; the bare substrate friction-ODE is a lightly-damped oscillator (complex roots −0.75±59.9i, k_curv = +3586.5) with no monotone H-tracking tail. The exponent-on-q = 2 leg is substrate-forced; the `d ln q/d ln H = 1` leg is the imposed closure. `CF-S100-W2-1-QEQ-DRIVE` correctly targets deriving a substrate `q_eq(H)` to make the slope-1 *unforced*. **But the BBN arm needs a different output from the SAME machinery**: not the late-time *attractor slope* but the **early-time radiation-era ρ_vac(a) profile** — specifically the *gravitating* part (deviation from Gibbs-Duhem equilibrium) at the BBN epoch. The friction-ODE integration from a high-H (radiation-era) initial condition down to today produces ρ_vac(a) for free; the BBN-arm question reads `ρ_vac(a_BBN)/ρ_rad(a_BBN)` off that trajectory. The two legs (late-time slope, early-time BBN fraction) are **outputs of one ODE integration** but are currently split across one named CF (W2-1, slope only) and an unnamed gap (BBN profile). The relief gate `S100-X-C10-RHOVAC-EPOCH-PROFILE` (§V.1) closes that gap and composes with CF-S100-W2-1-QEQ-DRIVE by consuming the same `q_eq(H)` drive.

**Status: the q-theory drives are candidate ρ_vac(a) profiles; CF-S100-W2-1-QEQ-DRIVE is the right machinery but is scoped to the late-time slope only. The BBN-arm time-profile read-off is an un-named, un-gated output of the same integration.**

### II.7 — The DILUTION-CC-66 present-epoch closure is UNAFFECTED by the BBN arm; this is a high-z-arm tension, not a CC-residual reopening

**Result**: `DILUTION-CC-66` = PROVEN (S66, canonical; `rho_vac_over_rho_obs = 1.032`, CC_OOM = 115.5; closes the 114-OOM CC gap to 0.01 OOM, conditional on C10 + external FRW H). The present-epoch closure uses z = 0 lever = 1, leaving `ρ_vac/ρ_obs = 1.032` untouched by the BBN-epoch fraction. Classification: **PHONONIC** (the a₀ tracking-vacuum at z = 0).

This is the scope boundary the synthesis must hold precisely (WP §W2-2 makes it explicit, both R1 G2 syntheses corroborate). The C10/CC residual that is the X-cut target is **the high-z (BBN) arm of the same tracking-vacuum**, NOT the present-epoch CC magnitude. The 115.5-OOM CC closure does not reopen if the BBN arm FAILs; what is at stake is whether the *same* Volovik tracking-vacuum `ρ_vac ~ M_Pl² H²` that closes the present-epoch CC is **consistent with the BBN ΔN_eff datum at high z**. A radiation-like all-history profile that closes z = 0 (ρ_vac/ρ_obs = 1.032) over-produces at BBN (2.087× over budget). The time-profile corridors are the framework's route to having BOTH: a present-epoch tracking-vacuum AND a BBN-epoch suppression — which requires the gravitating ρ_vac to be **epoch-dependent**, not a single all-history power law. This is the substrate-physics content of the entire X-cut.

---

## III. Gate Verdicts

All verdicts are CANONICAL (knowledge MCP, 2026-06-04), surfaced to anchor the corridor map. NONE re-adjudicated (per the Focus: R1 syntheses are input, gate verdicts authoritative).

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S98-MK3-2-BBN-VACUUM-FRACTION` | **FAIL** | ΔN_eff = 2.0873; frac_below = 0.4740; bound = 0.2271 (gate's own, ΔN_eff≤1) |
| `S99-W2-BBN-RELIEF` | **FAIL** | mech_a n_req = 1.959839 (1.835× shift); mech_b α_req = 0.479080; mech_c 475/992 modes; all non-substrate; corridor CLOSED (magnitude axis) |
| `S99-W2-RELAXATION-CLOSURE` | **FAIL** | slope_bare = 3.4159 (R²=0.079, no tracking tail); slope_driven = 1.0083 (imposed q_eq=c·H); n=2 NOT unforced; exponent-on-q substrate-forced, slope-leg imposed |
| `S99-W1-Q-NONRATIO-OBSERVABLE` | **INFO** | composite INFO; band_frac=0.490; finite-across-crossing=True; non-stationary backbone relvar=0.38866 (5.72 OOM > a_eff floor) — the a(t) frame escape ADVANCED |
| `S98-MK3-1-C10-SUBLEADING-SIGN` | **PASS** | n_eff = 1.978111 (HARD from-below, divergence_type=A); a3_q0_analytic = −881.5351 |
| `DILUTION-CC-66` | **PROVEN (S66)** | ρ_vac/ρ_obs = 1.032; CC_OOM = 115.5; present-epoch closure UNAFFECTED by BBN arm |
| C10 (Atlas-04 status) | **ASSUMED-PARTIALLY-PROVEN** | ρ_vac ~ M_Pl²H² scaling assumed; q_eq(H) drive NOT derived; both legs (slope + BBN) conditional |

---

## IV. Structural Implications

### Relief-corridor map (the primary deliverable)

The C10/BBN constraint surface has FOUR axes. The S99-W2-BBN-RELIEF gate exhausted ONE; three are open.

| Corridor | Axis | Source | Status | Open/Closed on what |
|:---------|:-----|:-------|:-------|:--------------------|
| **Magnitude — larger Δn** | tracking exponent (all-history) | S99 W2-2 mech (a) | **CLOSED** (structural) | n_eff = 1.959839 not substrate-derived; HARD pin is 1.978111 |
| **Magnitude — epoch-dependent α_V** | normalization (all-history) | S99 W2-2 mech (b) | **CLOSED** (structural) | α_V,BBN/α_V,0 = 0.479 not substrate-forced; one α_V in DILUTION-CC-66 |
| **Magnitude — mode-count dilution** | spectral-support count | S99 W2-2 mech (c) | **CLOSED** (structural) | 475/992 not sub-selected; all 992 gravitate (a₀ = ζ_{D_K}(0)) |
| **(a) Post-BBN production** | epoch placement of gravitating ρ_vac | paper 09 | **OPEN — conditional** | substrate transit/GGE chronology placing *gravitating* ρ_vac buildup post-BBN (T < 1 MeV); UNCHECKED |
| **(b) EDE-like dilution** | early-time ρ_vac(a) profile shape | papers 10, 02 | **OPEN — conditional (triple)** | (i) substrate f(R) gives EDE-like profile AND (ii) clears Ω_b h²→D/H side-channel AND (iii) negligible at recombination (0.107 combined window) |
| **(c) q-theory relaxation profile** | friction-ODE early-time trajectory | papers 04, 02, 06 | **OPEN — computable now** | the gravitating ρ_vac(a_BBN) read off the q_eq(H)-driven friction-ODE; same machinery as CF-S100-W2-1-QEQ-DRIVE |
| **n_eff direction (from-ABOVE)** | sign of tracking exponent | S66 (canonical) | **CONFLICTED** | S66 G_eff-route had n_eff=2.3 PASS; S98/S99 lever-route has n_eff<2 FAIL — opposite-direction tension between canonical sessions (§IV.1) |

**What is closed**: the magnitude axis at fixed all-history exponent (all three S99 mechanisms). This is a real structural finding — the framework cannot relieve BBN by shrinking ρ_vac at a single all-history power law.

**What is open**: the time-profile / epoch-placement axis (corridors a/b/c). Neither S98 nor S99 has computed the substrate's gravitating ρ_vac(a) across the radiation era. This is the load-bearing open computation for whether the BBN arm is robustly falsified or relieved — and it is the SAME quantity (an early-time read-off of the friction-ODE) that CF-S100-W2-1-QEQ-DRIVE already integrates for the late-time slope.

**What is conditional**: corridor (b) carries a triple conjunction (EDE-like profile ∧ Ω_b h²→D/H ∧ recombination-negligible under 0.107). Corridor (a) is conditional on the substrate chronology. Corridor (c) is computable now but its PASS depends on the f(R)/friction-ODE form yielding a sufficiently early-diluting profile.

### IV.1 — Conflicts flagged (per source-fidelity discipline)

1. **CONFLICT — n_eff direction: S66 G_eff-route (n_eff=2.3 PASS) vs S98/S99 lever-route (n_eff<2 FAIL).** The canonical S66 workshop passed n_eff = 2.3 via a 2% G_eff(BBN) bound (G_eff = 1.03G); the canonical S98/S99 gates FAIL n_eff = 1.978 via the ΔN_eff lever. In the lever form `(ρ_vac/ρ_rad)_BBN = frac_base·exp((n_eff−2)·X)` with X > 0, the from-ABOVE direction (n_eff > 2) makes the BBN fraction LARGER, not smaller — opposite to the S66 G_eff reading. These cannot both be the operative BBN falsifier with the same n_eff sign convention. **Resolving which BBN constraint (2% G_eff bound vs ΔN_eff lever) is canonical, and which n_eff direction relieves it, is a prerequisite for any relief gate.** Flagged, not resolved here; routed to §V.4. (This conflict is UPSTREAM of the literature sweep — it is internal to the framework's own canonical sessions.)

2. **CONFLICT — the 0.107 budget is non-canonical (volovik R1 conflict #1 confirmed).** `list_constants` returns no 0.107; the canonical bound is 0.227107 (ΔN_eff ≤ 1). The G2 sweep and the mack/sagan R1 syntheses score against 0.107; the canonical gates score against 0.227. Both are valid (different budgets); the relief gate pre-registers BOTH with currency tags. Do NOT propagate 0.107 as canonical.

3. **HYGIENE — T_RH not canonical.** The mack/sagan R1 syntheses cite T_RH = 1.70e15 GeV as the reheating scale gating corridor (a); `get_constant("T_RH")` returns not-found. The post-BBN-production corridor's chronology check needs a canonical reheating/GGE-formation scale. Flagged for registration (§V.4).

4. **REGISTRY — `CF-S100-W2-1-QEQ-DRIVE` is a named carry-forward, not yet a registry gate** (confirmed: no canonical gate entity). It is scoped to the late-time slope only; the BBN-arm time-profile read-off is an un-named gap. The relief gate §V.1 creates the BBN-arm gate and composes it with the QEQ-DRIVE machinery.

### IV.2 — What does NOT change

- The DILUTION-CC-66 present-epoch CC closure (115.5 OOM, ρ_vac/ρ_obs = 1.032) is UNAFFECTED by the BBN arm (§II.7). This is a high-z-arm consistency question, not a CC-residual reopening.
- The N_3 = 0 BDI substrate assignment and the q-theory-required chain (volovik/phonon-first R1 Results 3) are unchanged; q-theory is the only CC mechanism available given the gapped-BDI vacuum's absence of Fermi-point protection. The relief corridors are WITHIN q-theory (the f(R)/friction-ODE relaxation), not alternatives to it.
- The equilibrium theorem (`ρ_V = ε − q dε/dq = 0` at equilibrium) remains the wall. The *gravitating* ρ_vac is the deviation from equilibrium — which is precisely why an epoch-dependent gravitating ρ_vac(a) is structurally permitted (the substrate can be near-equilibrium at BBN and depart as H drops), and is the physical basis for corridors (a)/(c).

---

## V. Carry-Forward Computations

```
V.1. S100-X-C10-RHOVAC-EPOCH-PROFILE — the substrate gravitating ρ_vac(a) across the radiation era vs the BBN ΔN_eff budget [genuine-math; the X-cut's load-bearing gate]
   - What: From the substrate friction-ODE q″ + 3Hq′ + V′(q)=0 (V(q)=δρ_vac, k_curv=+3586.5,
     the bare-ODE solution in s99_w2_relaxation_closure.npz) integrated from a HIGH-H
     (radiation-era) initial condition down to today, compute the GRAVITATING part of ρ_vac(a)
     — the deviation from Gibbs-Duhem equilibrium ρ_V(q)=ε(q)−q dε/dq — and read off
     (ρ_vac/ρ_rad)_BBN at T~1 MeV AND (ρ_vac/ρ_rad)_rec at recombination. Classify the profile:
     radiation-like (constant fraction, all-history — the current C10 worst-case), EDE-like
     (∝ a^−n, n≥4, peaked near matter-radiation equality), or post-BBN-produced (≈0 at T>1 MeV).
     Output: ρ_vac(a) array + profile-class tag + ΔN_eff(BBN epoch) + ΔN_eff(rec epoch) under the
     actual gravitating profile (NOT the all-history lever transport).
   - Inputs: s99_w2_relaxation_closure.npz (bare-ODE oscillator, k_curv=+3586.5, q_boundary,
     q0_ref/rho0_ref); s98_mk3_2_bbn_vacuum_fraction.npz (baseline 0.474049, lever X=40.2756);
     s98_mk3_1_c10_subleading_sign.npz (n_eff=1.978111, divergence_type=A); equilibrium ρ_V=ε−q dε/dq
     (S95 EQUILIBRIUM-CC-WARRANT); canonical S66 formula ΔN_eff=(ρ_vac/ρ_rad)/(7/8·(4/11)^(4/3));
     T_BBN_GeV=0.001, z_BBN=4e8, N_eff_SM=3.044; a_0_FW_zeta=6440.0; paper 02 f(R) ε_vac(H)=f(R=12H²)
     + paper 04 friction ODE (methodological source). Depends on: CF-S100-W2-1-QEQ-DRIVE (consumes
     the same q_eq(H) drive — see V.2).
   - Gate: NEW S100-X-C10-RHOVAC-EPOCH-PROFILE [SIGN]. Pre-register BOTH budgets with currency tags:
     PASS iff the gravitating (ρ_vac/ρ_rad) at BOTH BBN and recombination yields ΔN_eff ≤ 1
     (canonical bound 0.227107) AND the profile is EDE-like-or-later (not radiation-like);
     INFO iff it clears the canonical ΔN_eff≤1 at BBN but NOT the external 0.107 combined window,
     OR clears BBN but the Ω_b h²→D/H side-channel (V.3) is unchecked;
     FAIL iff the gravitating profile is radiation-like (flat ⇒ the 2.087× / 19.51× exceedance stands)
     — then the BBN arm of the C10 discharge is robustly conditional/falsified on the radiation-like reading.
   - Effort: 4-6 hours, 1 agent session (the ODE integration exists; the early-time gravitating-ρ_vac
     read-off + equilibrium-deviation extraction + profile classification is the new content).

V.2. CF-S100-W2-1-QEQ-DRIVE — substrate-internal q_eq(H) drive [canonical CF; re-scope to dual-output]
   - What: Derive a substrate-internal q_eq(H) drive (an H-dependent equilibrium from the substrate's
     own back-reaction, e.g. a Hubble-sourced chemical-potential shift in the Volovik Gibbs-Duhem
     relation, NOT the imposed q∝H simple-fluid closure) and re-integrate the friction ODE WITHOUT the
     imposed linear closure. RE-SCOPE: emit BOTH the late-time attractor slope (the W2-1 leg) AND the
     early-time radiation-era ρ_vac(a) trajectory (feeds V.1) from the SAME integration.
   - Inputs: s99_w2_relaxation_closure.npz (bare-ODE solution, k_curv=+3586.5); s99_w1_q_nonratio_observable.npz
     (arr_H_bare_t backbone); Volovik Gibbs-Duhem ρ_vac(eq)=0 (S95); S62 #19 (q=0 interior equilibrium);
     paper 04 ODE (Eqs. 11/13/19/21); paper 02 f(R) ε_vac(H)=f(R=12H²); canonical_constants (a_0_FW_zeta).
   - Gate: [SIGN] (existing CF spec): PASS iff substrate q_eq(H) yields |slope−1|≤0.05 UNFORCED
     (C10 Object-C → substrate-forced, §8.5 OPEN→CLOSED); INFO iff slope narrows but a residual closure
     parameter survives; FAIL iff no substrate q_eq(H) exists (n=2 structurally a fluid-closure input).
     The early-time ρ_vac(a) output feeds V.1 regardless of the slope verdict.
   - Effort: 6-8 hours, 1-2 agent sessions (the substrate back-reaction q_eq(H) derivation is the hard part;
     the dual-output re-scope adds the radiation-era read-off, cheap once the integration runs).
   - Depends on: nothing new (consumes existing S98/S99 npz). V.1 depends on V.2's q_eq(H) drive.

V.3. S100-X-C10-OMEGAB-DH-SIDECHANNEL — the Ω_b h² → D/H residual under EDE-like relief [genuine-math; CONDITIONAL]
   - What: IF V.1 returns EDE-like (corridor b Stage 1 passes), compute the residual BBN constraint
     through the inferred-baryon-density channel (paper 10's warning): the CMB-fit-required Ω_b h²
     shift under the EDE-like ρ_vac(a) and its propagated effect on D/H vs Cooke+18. Output: Δ(Ω_b h²)
     required, predicted D/H, χ²_Cooke contribution.
   - Inputs: V.1 ρ_vac(a) profile (EDE-like branch); framework Ω_b h² (query get_constant — omega_H2 / Omega_b
     in canonical; if absent derive from substrate baryon sector); paper 10 (Seto-Toda) EDE-vs-N_eff
     baryon-density mechanism; Cooke+18 D/H=2.527±0.030 ×10⁻⁵; paper 11 compressed Ω_b h²=0.022371.
   - Gate: NEW S100-X-C10-OMEGAB-DH-SIDECHANNEL [SIGN], CONDITIONAL (trigger-first; fires only if V.1=EDE-like):
     PASS iff |D/H_pred − D/H_obs| < 2σ_Cooke under the EDE-like Ω_b h² shift; FAIL iff the baryon-density
     channel reintroduces a >2σ D/H tension (EDE-like relief incomplete — corridor b Stage 2 fails).
   - Effort: 2-3 hours, 1 agent session (conditional on V.1=EDE-like).
   - Depends on: V.1 (only fires if EDE-like).

V.4. S100-X-C10-BBN-CONSTRAINT-RECONCILE — resolve the n_eff-direction conflict + re-pin the budget [genuine-math + registry hygiene]
   - What: Resolve the canonical conflict (§IV.1.1) between the S66 G_eff-route (n_eff=2.3 PASS via 2% G_eff
     bound) and the S98/S99 lever-route (n_eff<2 FAIL via ΔN_eff). Determine which BBN constraint (2% G_eff
     bound vs ΔN_eff lever) is the operative falsifier on the tracking-vacuum, and which n_eff direction
     (from-above vs from-below) relieves it — they point OPPOSITE in the lever form. Separately: register
     the external Goldstein-Hill 2026 budget ΔN_eff<0.107 as a NAMED constant with explicit non-canonical-
     budget provenance (so downstream gates cite the right threshold), and register/locate T_RH (reheating
     scale) needed by corridor (a).
   - Inputs: session-66-mack-transit-workshop.md (n_eff=2.3 PASS, 2% G_eff bound, G_eff=1.03G);
     S98/S99 lever (n_eff=1.978, exp((n_eff−2)·X), X=40.2756); paper 11 ΔN_eff<0.107 (N_eff=2.990±0.070);
     paper 09 ΔN_eff<0.39/0.46; delta_N_eff_vacuum_BBN_below=2.0873.
   - Gate: [VERIFY] + registry. PASS iff the operative BBN falsifier + relieving n_eff direction are pinned
     with a Sage-exact substitution chain AND the 0.107 budget + T_RH are registered with provenance.
     INFO iff the two canonical routes are shown structurally distinct (different observables: G_eff vs ΔN_eff)
     and both retained with explicit scope tags. update_constant for delta_N_eff_budget_GoldsteinHill_2026=0.107
     (non-canonical-external tag) + T_RH if locatable.
   - Effort: 2-3 hours, 1 agent session (the n_eff-direction substitution chain + budget registration).

V.5. S100-X-METASTRING-VS-QTHEORY-BBN — cross-domain: paper 10 (Hur-Minic) metastring w(z) vs the framework
     tracking-vacuum, BOTH against DESI + the BBN ΔN_eff budget [cross-domain comparison; G2 cross-link]
   - What: Benchmark the framework's substrate-derived w(z) (canonical branches w0_FW=−0.918, the
     two-fluid w0=−0.918087/wa=−0.000575) against paper 10's single-parameter metastring CPL curve
     w₀=−1−ξ₀⁴e^{−ξ₀}/(18{1−b(ξ₀)}), BOTH vs DESI DR2 AND the BBN ΔN_eff budget. The discriminator the
     framework has that the metastring lacks: a BBN-epoch ρ_vac(a) constraint (V.1). Map whether the
     metastring CC mechanism (dual-spacetime curvature) carries any analog BBN constraint, or whether the
     framework's tracking-vacuum is UNIQUELY constrained at BBN among emergent-spacetime CC mechanisms.
   - Inputs: paper 10 Eqs. 19/33/34; canonical w0_FW=−0.918, wa_FW=0, two-fluid w0=−0.918087/wa=−0.000575
     (s65_desi_dr3_prep_log); DESI DR2 (w0,wa); V.1 BBN ρ_vac(a) result; ΔN_eff budget (canonical 0.227 + external 0.107).
   - Gate: NEW S100-X-METASTRING-VS-QTHEORY-BBN (INFO-class cross-domain): report whether the framework and
     metastring are DESI-distinguishable at DR2/DR3 precision AND whether the BBN-arm constraint is a
     framework-specific discriminator (the metastring's CC has no BBN-epoch tracking analog). No PASS/FAIL on
     the competing model.
   - Effort: 2-3 hours, 1 agent session (G2 cross-link; lowest leverage of this set).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | S99-W2-BBN-RELIEF FAIL is an AXIS-fail (magnitude at fixed all-history exponent), not an arm-fail | PHONONIC | CLOSED (magnitude axis) | The 3 tested mechanisms exhaust the magnitude axis; the time-profile axis was never opened |
| 2 | External 0.107 budget is NON-canonical; canonical bound is 0.227107 (ΔN_eff≤1) | NON-PHONONIC (budget) | CONFLICT flagged (volovik R1 #1) | 2.087× over canonical / 19.51× over 0.107; adopting 0.107 needs ×0.051 suppression (vs ×0.479) |
| 3 | Corridor (a) post-BBN production: gravitating ρ_vac builds up post-BBN | PHONONIC | OPEN — conditional | Gated by substrate transit/GGE chronology; UNCHECKED; needs T_RH (non-canonical) |
| 4 | Corridor (b) EDE-like dilution: f(R) ε_vac(H)=f(R=12H²) candidate profile | PHONONIC | OPEN — conditional (triple) | EDE-like ∧ Ω_b h²→D/H side-channel ∧ recombination-negligible (0.107 combined window) |
| 5 | S66 from-ABOVE n_eff=2.3 PASSed (G_eff route) vs S98/S99 from-BELOW n_eff<2 FAIL (lever route) | PHONONIC | CONFLICT (canonical sessions) | Lever and G_eff routes point OPPOSITE on n_eff; operative falsifier unresolved (§IV.1.1) |
| 6 | q-theory drives (papers 04/02/06) = candidate ρ_vac(a); CF-S100-W2-1-QEQ-DRIVE is the machinery | PHONONIC | OPEN — computable now | CF scoped to late-time SLOPE only; BBN-arm early-time read-off is an un-named gap (V.1 fills it) |
| 7 | DILUTION-CC-66 present-epoch closure (115.5 OOM, ρ_vac/ρ_obs=1.032) UNAFFECTED by BBN arm | PHONONIC | PROVEN (S66), unchanged | High-z-arm consistency question, NOT a CC-residual reopening |
| — | CF-S100-W2-1-QEQ-DRIVE is a named CF, not a registry gate; scoped to slope only | — | FLAGGED (§IV.1.4) | V.1 creates the BBN-arm gate + composes via the QEQ-DRIVE drive |

---

**Substrate-first closing note.** The C10/BBN residual is not "the framework over-predicts vacuum energy at BBN by 20×." It is: *the same Volovik a₀ tracking-vacuum that closes the present-epoch CC to 0.01 OOM has an unknown gravitating-ρ_vac(a) profile across the radiation era, and whether that profile is radiation-like (falsified at BBN) or EDE-like/post-BBN (relieved) is a substrate-physics question — an early-time read-off of the same friction-ODE that CF-S100-W2-1-QEQ-DRIVE integrates for the late-time slope — that the framework has not yet computed.* The S99-W2-BBN-RELIEF FAIL closed the magnitude axis honestly; it did not touch the time-profile axis, which is where papers 09/10 (dark-radiation and EDE) locate the only surviving relief. The arrow holds throughout: D_K eigenvalues → a₀ zeroth spectral moment → gravitating ρ_vac(a) (deviation from Gibbs-Duhem equilibrium) → (ρ_vac/ρ_rad)_BBN → ΔN_eff. The substrate IS the tracking-vacuum; BBN N_eff is the laboratory-IN falsifier; the time-profile is the un-computed substrate-IS object that decides the verdict. No probability moves until `S100-X-C10-RHOVAC-EPOCH-PROFILE` fires.

*Anchoring note: every framework-state claim verified against canonical via knowledge MCP (get_constant / search_knowledge / query_entity / list_constants) on 2026-06-04. Indexes and R1 syntheses treated as idea-generators / input, not registers (per Focus). Four conflicts flagged: (1) n_eff-direction tension between canonical S66 and S98/S99; (2) 0.107 non-canonical (volovik R1 #1 confirmed via list_constants); (3) T_RH not canonical; (4) CF-S100-W2-1-QEQ-DRIVE is a named CF scoped to the slope leg, not the BBN-arm. Exceedance factors (2.087× / 19.51×), suppression factors (×0.479 / ×0.051), and the n_eff shift ratio (1.835×) are Sage-exact.*
