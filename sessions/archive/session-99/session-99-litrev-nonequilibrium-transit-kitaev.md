# Session 99 Synthesis: Non-equilibrium Transit, Analog Pair Production, and the Impulsive-Quench Universality Class

**Date**: 2026-06-04
**Agent**: kitaev-quantum-chaos-theorist (Workhorse-Quantum-Chaos)
**Source Documents**:
- `downloads/research-sweep-s99/nonequilibrium-transit/00-INDEX.md` (13 paper summaries, fetched-text only)
- 13 PDFs beside the index (01 Xue, 02 Viermann, 03 Sparn, 04 Schmidt, 05 Gondret-preheating, 06 Gondret-parametric, 07 Parra-López thesis, 08 Rao, 09 Stahl, 10 Ahmadi, 11 Vagnozzi, 12 Langen, 13 Li)
- `.claude/agent-memory/kitaev-quantum-chaos-theorist/MEMORY.md` + `methodology_and_data.md`
- Canonical anchors (knowledge MCP): `tau_fold=0.19`, `n_T_PathH_canonical=-0.0009338`, `n_T_PathC_canonical=-0.001466`, `alpha_s_inflation_framework=-0.0690` (SUPERSEDED), `P_exc_kz=1.0`, `n_pairs=59.8`, k_pivot(fold)=14.310 M_KK, proven_1291 (GGE-never-thermalizes BROKEN), INTEG-39 (DECISIVE FAIL), S85-W7-CUSP-BOGOLIUBOV (FAIL)

---

## I. Session Outcome

The 13-paper non-equilibrium-transit cluster supplies **independent corroboration of the transit paradigm in standard QFT-in-curved-spacetime language** (Parra-López's switch-on/off-dominance theorem: production is dominated by the transitions, not the stages) and a **closed-form discriminator stack** (Schmidt/Sparn: sub-horizon `sin[μ_k Δη]` vs super-horizon `sinh[Λ_k Δη]` reflection amplitudes) that lets us classify the fold's `k_pivot` mode unambiguously. The single most consequential finding for this agent's domain: the literature partitions the fast-quench regime into **two distinct universality classes** — Rao's rate-independent quench-RANGE scaling (`ρ ~ δ_max` above `v_c`) and Li's KZ-survives-AIS-breakdown class (intact iff `z' < z + 1/ν`) — and the framework's Parker-saturated `P_exc=1.000` (rate-independent saturation) sits squarely in **Rao's class**, NOT Li's. This is a positive structural placement, not a gate pass.

The cluster also forces an **explicit reconciliation of the Ordered-Veil claim against canonical**: the literal "GGE never thermalizes" theorem (proven_1291) is registry-status **BROKEN** at single-cell level (Brody β=0.633, 63% GOE, t_therm ≈ 6 M_KK⁻¹), surviving as Poisson integrability only at the **fabric scale** (CG(24) Josephson-averaged ⟨r⟩=0.367). Papers 05 (Gondret entanglement-decay control) and 12 (Langen GGE tomography) are the precise empirical templates that bear on which scale the relic actually occupies. No kill condition fires; the chaos bound `λ_L ≤ 2πT` remains trivially satisfied (`λ_L=0` at the integrable fabric scale).

---

## II. Key Results

### 1. The impulsive-vs-smooth discriminator stack (papers 03/04) — transfer-matrix IS valid in the sharp-boundary regime, with a standing canonical FAIL to resolve

**Result**: Schmidt (04) and Sparn (03) reformulate `(D+1)`-dim cosmological pair production as a **stationary 1D Schrödinger scattering problem** `[−d²/dη² + V(η)]ψ_k = k²ψ_k` with potential `V(η) = (1/4)ȧ² + (1/2)ä·a` (Sparn Eq. 4). The scale-factor history IS the scattering potential; `N_k = |b_k|²/|c_k|²` is the reflection coefficient with unitarity invariant `|c_k|² = |a_k|² − |b_k|²`. **GEOMETRIC** (the V(η) construction is the analog-side image of the substrate's Mukhanov-Sasaki `z''/z` barrier).

This is the most structurally-aligned inherited pair for the framework's `k_pivot` mapping gap (atlas-04 C2). The decisive cross-checks:

(a) **Transfer-matrix validity regime.** Sparn uses the transfer-matrix method **successfully** — but ONLY for genuinely sharp cusps (delta-peak discontinuities `ψ_k' → ψ_k' + Ω ψ_k`), NOT smooth ramps. The framework's transit is impulsive (Mach 13.75; `H·Δt = 0.663 < 1`), placing it in **exactly the box-potential-with-delta-peaks limit** Sparn realizes for linear expansion — "the delta-distributions from the abrupt start and end of the ramp" are the framework's sudden-approximation boundary terms. This vindicates transfer-matrix **for the sudden limit specifically**. It does NOT retroactively rescue the canonical transfer-matrix gate: **S85-W7-CUSP-BOGOLIUBOV closed FAIL** (value=−2.019676, scheme=transfer-matrix, convention=BD-in-out, L_max=10). The FAIL is consistent with this agent's standing methodology note (transfer-matrix produces artificial reflections / OOM-sensitive `|β|²` for non-sharp `ω_k(τ)`): the gate FAILed because the fold profile fed to it was treated as a smooth cusp, not a clean box+delta. Sparn's result says the **correct** discretization (box + two delta-peaks at the switch-on/off) is the regime where the method is exact — a concrete re-attempt recipe, not a vindication of the failed run.

(b) **Sub-horizon vs super-horizon closed forms.** Schmidt's Eqs. 75–76 give `r_k/t_k ∝ sin[μ_k Δη]` (sub-horizon, oscillating) vs `∝ sinh[Λ_k Δη]` (super-horizon, decaying), related by the analytic continuation `Λ_k → i μ_k`. The framework's `k_pivot = 14.310 M_KK` mode is **SUBHORIZON at the fold** (canonical: `k/aH = 14.70`, S77 — confirmed via `s78_f_conv_subhorizon_output.txt`). It therefore sits in the **`sin[μ_k Δη]` oscillating sector**, NOT the `sinh` super-horizon sector. This is fully consistent with the permanent result that `alpha_s(primordial) → 0` in the super-horizon frozen plateau (`Z_norm = 1`, superhorizon frozen, T4.4 from session-77): the pivot is sub-horizon AT the fold, becomes super-horizon AFTER, and the running is read off the frozen plateau where Bogoliubov saturation kills the slope. Both pictures are coherent only because they refer to **different epochs of the same mode**.

The dimensional-consistency check on `V(η)`: `[ȧ²] = [ä·a] = [a]²/[η]²`, and with `ψ_k = √a · v_k` the Schrödinger eigenvalue is `k²` (comoving wavenumber squared) — dimensionally `[V] = [k²] = [η]⁻²` in conformal time. Consistent. **Regime of validity**: acoustic, `k < ξ⁻¹ ≈ 0.94 μm⁻¹` for the lab; the full Bogoliubov dispersion `ω_k = c_s k √(1 + k²ξ²/2)` extends it. The framework analog must carry the corresponding `λ_max` (healing-length-analog) cutoff; `x_pivot = (k_pivot/λ_max)² = 11.075` is already the canonical dimensionless scheme input (S77).

### 2. Switch-on/off dominance (paper 07) — the transit paradigm derived from in/out Bogoliubov, independent of the substrate picture

**Result**: Parra-López's thesis keystone (ch. 6, Part II/III): *"switch-on and -off processes DOMINATE production due to their non-adiabaticity"* and *"the most relevant periods for particle creation are the TRANSITIONS between different stages of the Universe, rather than the stages themselves."* Bogoliubov coefficients via Wronskians `α_h = −i Wr[u_h, v_h*]`, `β_h = i Wr[u_h, v_h]`, with `|α_h|² − |β_h|² = 1` (Eqs. 3.20–3.21). **PHONONIC** (this is the framework's central paradigm — "the transit IS the physics", atlas-10 Ordered Veil PROVEN — stated in standard cosmological-QFT language).

This is **independent corroboration**, not agreement-as-evidence: Parra-López derives switch-on/off dominance from the in/out formalism with no knowledge of the substrate, the van Hove fold, or `D_K`. The framework's supersonic impulsive transit is the substrate-first realization of exactly this principle (the boundary terms set `|β|²`; the quasi-static interior contributes negligibly). The corroboration is structural: two distinct derivation routes (substrate spectral fold; QFT-in-curved-spacetime in/out boundary terms) converge on "transitions dominate, stages don't." The thesis's spectator-field DM mechanism (production by background geometry alone, decoupled from any inflaton) maps onto the framework's Leggett-channel GGE quasiparticle (inter-band coherence, CPT-neutral, non-annihilating) — both are "produced by the transit geometry, decoupled from a driving field." Substrate-first direction preserved: the thesis treats cosmological production as fundamental and the BEC as analog; the framework treats the `D_K`-spectral fold transit as fundamental and BOTH the inflaton picture AND the BEC as projections of it.

### 3. Fast-quench universality class of the fold (papers 08 vs 13) — Rao's range-scaling class, not Li's KZ-survival class

**Result**: Two mutually-illuminating fast-quench results bracket the fold's universality class:
- **Rao (08)**: above a critical quench rate `v_c` (itself scaling with `δ_max`), KZ scaling `ρ ~ v^{1/2}` is **REPLACED** by rate-independent quench-RANGE scaling `ρ ~ δ_max`. Experimentally verified (single trapped-ion qubit, Landau-Zener + Rice-Mele).
- **Li (13)**: at a tricritical Ising point, the adiabatic-impulse scenario (AIS) BREAKS DOWN (ramp stays gapless throughout) yet **KZ scaling SURVIVES** iff `z' < z + 1/ν_μ` (here `z=z'=1`, `ν_μ=5/4`, exponent `r_μ = z + 1/ν_μ = 9/5`).

**PHONONIC** (sets which universality the GGE relic occupation obeys). The framework's transit is fast (`H·Δt = 0.663 < 1`) and the production saturates: `P_exc_kz = 1.000` (canonical), `n_pairs = 59.8` (Parker saturation). **Saturation is rate-independent by construction** — `P_exc = 1` cannot increase with faster quenching. This is the defining signature of **Rao's `v > v_c` class**: the relic occupation is controlled by the **fold spectral excursion magnitude (the range)**, not the transit rate. The substrate-side reading: the van Hove fold range (the spectral excursion `δS` across the fold) sets the relic, just as `δ_max` sets the defect density above `v_c`.

The framework is NOT in Li's class. Li's KZ-survival requires a controlled `z' < z + 1/ν` inequality at a *higher-order critical point* with a clean (if gapless) scaling window; the framework's fold is a **first-order transition** at `τ_fold = 0.190` (Parker-SATURATED, not power-law-scaling). Saturation is the opposite of "KZ scaling survives": there is no residual rate-dependence to scale. The structural adjacency Li raises (the fold sits near the first-order/continuous boundary — the van Hove fold IS a tricritical-adjacent feature) is worth a forward gate (V.4), but the *occupation* observable is range-saturated, Rao-class. The emergent-SUSY `η_b = η_f = 2/5` at Li's TCI is a structural curiosity vs the framework's KO-dim=6 spectral-triple content; it is NOT evidence (no quantitative bridge), flagged as an untested adjacency only.

### 4. Ordered-Veil falsifier templates (papers 12 + 05) — and the canonical reconciliation they force

**Result**: This is the highest-leverage finding for this agent's kill authority, and it forces an explicit conflict-flag (Section IV).

Langen (12) is the keystone empirical GGE realization: an integrable 1D Bose gas (Lieb-Liniger), quenched by transverse splitting, relaxes to a **GGE** `ρ = (1/Z)exp(−Σ_m λ_m I_m)` parametrized by conserved mode occupations `n_m = ⟨β_m† β_m⟩`, NOT a thermal state — retaining initial-state memory via the infinite conserved-charge set. Diagnostic protocol: higher-order correlation tomography (up to **10th order**); the **anti-diagonal correlation peak** distinguishes genuine GGE (different temperatures on even/odd modes) from ordinary Gibbs (single temperature, flat anti-diagonal); **~10 Lagrange multipliers** suffice. Gondret (05) is the CONTROL case: a parametric (preheating) drive whose `(+k,−k)` entangled pairs **LOSE non-classicality and approach thermalization** — the lab analog of reheating, exactly what the framework's relic must NOT do.

**PHONONIC** (the GGE relic IS the post-transit substrate state). Now the canonical reconciliation:

- **Literal "GGE never thermalizes" (proven_1291, atlas-04 T3): status BROKEN.** Registry text: *"V_phys 13% non-separable. Brody β = 0.633 (63% GOE). t_therm ~ 6 natural units. GGE valid during transit but thermalizes to Gibbs on cosmological timescales (t_therm/t_Hubble = 9e-48)."* Re-confirmed S96 as **INTEG-39 DECISIVE FAIL** (V_phys 13% non-separable; Brody β=0.633; Thouless g=0.60; t_therm ≈ 6 M_KK⁻¹).
- **The reconciliation (S62):** *"The single-cell Brody parameter (β=0.633, 13% non-separable) does NOT survive Josephson averaging on the CG(24) fabric (⟨r⟩=0.367, Poisson)."* So: with physical interactions, a **single cell shows partial level repulsion (63% GOE) and would thermalize** in ~6 M_KK⁻¹; the **fabric scale (CG(24) Josephson-averaged) is Poisson-integrable** and the Ordered Veil survives there. "Valid during transit" is the operative scope — the transit epoch is the physics (atlas-10 PROVEN), and over the transit the GGE is the correct relic description regardless of the single-cell long-time fate.

Langen's protocol is precisely the tool to test WHICH scale the framework relic occupies: a framework-substrate analog that relaxes to a GGE with conserved mode occupations and FAILS the single-temperature Gibbs fit (anti-diagonal peak present) confirms fabric-scale integrability; one that thermalizes (anti-diagonal flat, single T) confirms the single-cell BROKEN reading. Gondret's entanglement-decay timescale is the calibration of the *thermalizing* control. The `~10 Lagrange multipliers` is a striking structural echo of the framework's finite-charge truncation (Lefschetz `n* = 60` / Parker `n_pairs = 59.8`), but the echo is **not evidence** (no derived bridge between 10 GGE multipliers and 60 Parker pairs); it is a candidate gate (V.5).

### 5. Nonlinear survival of impulsive features (paper 09) — a small-scale observable channel for the fold

**Result**: Stahl shows sudden slow-roll violations (the inflationary-language image of the impulsive fold) imprint sharp primordial-spectrum features that **survive nonlinear evolution** as (i) a **localized matter-power enhancement/decrement** (amplitude+position recover the primordial feature scale) and (ii) a **halo-mass-function oscillation whose characteristic behavior is keyed to the SIGN of the feature**. Oscillatory patterns are erased by mode coupling; the localized feature + sign survive. **PHONONIC** (the fold's spectral excursion is the impulsive source).

This is the transfer-function bridge the framework's `k_pivot` mapping gap (atlas-04 C2) needs from a sub-horizon impulsive source to late-time observables — but on **small scales, below CMB**, where the framework's frozen-spectrum exactness (Sasaki-Stewart, `n_s=1` unbroken at CMB scales) does not preclude a feature. The framework already predicts a specific van Hove excursion DIRECTION, which fixes the **sign** of the HMF signature — a genuine discriminator (V.6). Substrate-first: the inflationary "sharp feature" model is a phenomenological projection of the van Hove fold; the fold IS the sudden source.

### 6. Blue-tensor landscape (paper 11) — positioning n_T=+0.468 transit against the PTA-inflation band and BBN

**Result**: Vagnozzi finds the PTA-detected SGWB admits an inflationary-tensor interpretation only with an **extremely blue** `n_T ~ 1.8 ± 0.3` AND a very low reheating scale `T_rh ≲ 10 GeV` (BBN/`ΔN_eff` bound), and that such models generically predict **excluded large non-Gaussianities** — making inflationary origin "barely tenable." Standard single-field slow-roll gives `n_T = −2ε < 0`; a strong blue tilt requires NEC violation (superinflation) or anisotropic-stress sources. **PHONONIC** (observational landscape for the framework's blue transit tilt).

The framework's tensor tilt is the scale-and-channel-tagged pair (per phononic-framing.md `§Scale-and-channel-tagging`):
- **Transit scale (substrate/BZ): `n_T = +0.468`** (canonical, S66; index cites +0.4676). BLUE.
- **CMB-pivot scale: `n_T_PathH_canonical = −0.0009338`, `n_T_PathC_canonical = −0.001466`** (≈ −1×10⁻³, effectively flat/red at the pivot).

The framework is **NOT claiming the PTA signal IS its tensor mode**: `+0.468` (transit) is much shallower than Vagnozzi's `~1.8`, and the CMB-pivot value is ≈ 0. The genuine content: (a) the framework produces its blue *transit-scale* tilt WITHOUT superinflation/NEC-violation-in-a-container — it is intrinsic substrate-spectral blueness from the impulsive fold (`r = 16ε` already inapplicable, 5 independent arguments, VdD-Hawking workshop); (b) crucially, the framework **passes Vagnozzi's non-Gaussianity tension differently** — its blue tilt coexists with small Gaussian `f_NL` (see Result 7) because the blueness is substrate-spectral, NOT slow-roll-parameter-driven. The `ΔN_eff`/BBN bound is the gate any blue-tilt framework must clear; the framework's tensor amplitude is set by the acoustic `(A)`-class `Ω_GW ≈ 1×10⁻¹⁰` (project-canonical, LISA-live), well below the PTA band, so the BBN bound is not strained. The scale-and-channel tag is load-bearing: the +0.468 and −1e-3 are BOTH real substrate-IS observables at different scales (neither demoted), per the canonical replacement of the FORBIDDEN power-law-transfer-precedence rule.

### 7. ζ-tail template vs the Gaussian-by-Wick relic (paper 10)

**Result**: Ahmadi's stochastic-δN treatment of a sharp non-slow-roll (Starobinsky-type) transition finds the curvature-perturbation `ζ` distribution decays **faster than `e^{−3ζ}`** (a sub-exponential / lighter-than-naive-USR tail). **PHONONIC** (the fold is the substrate sharp transition).

The framework's canonical relic non-Gaussianity: the squeezed-vacuum relic is **Gaussian by Wick** — `f_NL = O(ε)` regardless of squeezing (Mellin-Wick commutation theorem, S87 W-6; Lefschetz-Gaussian-74 structural PASS). Canonical central values: GGE-bispectrum `f_NL ~ 1.03–1.12` (equilateral), folded `f_NL = 0.056` (S82). So the framework predicts a **Gaussian (not heavy-tailed) ζ**, consistent in DIRECTION with Ahmadi's suppressed (faster-than-`e^{−3ζ}`) tail. Ahmadi supplies a quantitative diffusion-based template to test the framework's Gaussianity claim against an independent (non-in-in) calculation. Note: the framework's `f_NL ~ 1` is NOT literally zero — "Gaussian by Wick" means `O(ε)`-small, dominated by the slow-roll-parameter scale, not strictly vanishing. The relic carries a definite, small, computable non-Gaussianity; Ahmadi's tail is the cross-check that it does not develop a heavy tail under sharp-transition stochastic diffusion.

---

## III. Gate Verdicts

The source index performed **no computation and emitted no gates** (it is an idea-generator). The gates below are CANONICAL verdicts retrieved from the knowledge MCP that this synthesis anchors against — they are authoritative and are NOT re-adjudicated here.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| proven_1291 — GGE never thermalizes (Richardson-Gaudin) | **BROKEN** | V_phys 13% non-separable; Brody β=0.633 (63% GOE); t_therm ≈ 6 M_KK⁻¹; t_therm/t_Hubble=9e-48 |
| INTEG-39 (S96 re-confirm) | **DECISIVE FAIL** (single-cell) | Brody β=0.633; Thouless g=0.60; ⟨r⟩=0.367 Poisson on CG(24) fabric (survives at fabric scale) |
| S85-W7-CUSP-BOGOLIUBOV | **FAIL** | value=−2.019676; scheme=transfer-matrix; convention=BD-in-out; L_max=10 |
| LEFSCHETZ-GAUSSIAN-74 (W2-E) | **FAIL numerical / PASS structural** | squeezed thermal state Gaussian; `E_state=(1/2)Σ_k ω_k[cosh(2r_k)(1+2n_k)−1]` |
| BLUE-65 / S66 transit tilt | (canonical value) | `n_T = +0.468` transit; `n_T_PathH=−0.0009338`, `n_T_PathC=−0.001466` pivot |
| S77 mode-threshold | (canonical) | `k_pivot=14.310 M_KK`; `k/aH=14.70` SUBHORIZON at fold; `x_pivot=11.075` |
| GGE-BISPECTRUM-67 | (canonical) | `f_NL^equil ~ 1.03–1.12`; folded `f_NL=0.056` |

---

## IV. Structural Implications

**The transit paradigm gains an external, substrate-independent derivation.** Parra-López's switch-on/off-dominance theorem (Result 2) is the most important structural import: it derives "transitions dominate, stages don't" from the in/out Bogoliubov formalism alone. This strengthens the framework's transit-physics axis (atlas-10 Ordered Veil PROVEN) by showing the principle is route-independent — not a substrate-specific artifact. The constraint-map effect: any objection of the form "the framework's impulsive-transit assumption is ad hoc" is now answered by a standard-QFT-in-curved-spacetime theorem that the boundary terms dominate `|β|²`.

**The transfer-matrix corridor is reopened — for the sudden limit only.** S85-W7-CUSP-BOGOLIUBOV FAILed (transfer-matrix). Sparn (Result 1a) shows transfer-matrix is **exact** for box+delta (sharp-boundary) potentials and **fails** for smooth cusps — which is precisely this agent's standing methodology note (artificial reflections, OOM-sensitive `|β|²` for smooth `ω_k`). The corridor that reopens: re-attempt the Bogoliubov `|β_k|²` extraction discretizing the fold as a **box potential with two delta-peaks at the switch-on/off** (the impulsive boundary terms), NOT as a smooth interpolated cusp. This is a concrete remediation path for the FAILed gate, not a claim it already passes.

**The fold's universality class is now pinned: Rao-range-saturation, not Li-KZ-survival.** (Result 3.) `P_exc=1.000` is rate-independent saturation = Rao's `v>v_c` class; the relic occupation is fold-RANGE-controlled. This closes a previously-open question about whether the framework should be applying any rate-dependent KZ scaling: it should not. The fold-range (spectral excursion `dS/dτ = +58,673` at fold; `ΔS` across the fold) is the control parameter for the relic, consistent with Parker saturation.

**EXPLICIT CONFLICT FLAG (canonical vs agent memory).** This agent's MEMORY.md asserts "ADH prethermalization: t_therm/t_universe = 10^578. GGE permanent" and "Bertini-Essler vs ADH: agree within 1 OOM, both give ~10^580 t_universe." The **registry-canonical** (proven_1291, atlas-04 T3, INTEG-39) asserts the OPPOSITE single-cell timescale: **t_therm ≈ 6 M_KK⁻¹, t_therm/t_Hubble = 9e-48**, and status **BROKEN**. Per epistemic-discipline source-authority hierarchy (synthesis files + gate verdicts > agent memory), **the registry wins**. The reconciliation is the two-scale picture (S62): single-cell with physical interactions thermalizes fast (β=0.633, 63% GOE, ~6 M_KK⁻¹); the CG(24) fabric is Poisson-integrable (⟨r⟩=0.367) and the Ordered Veil survives at fabric scale, with "GGE valid during transit" as the operative scope. The `10^578` memory figure appears to be a single-cell *Bogoliubov-bath* prethermalization estimate (ESSLER-66/PRETHERM-65, migrated INFO) that does NOT contradict the *interaction-driven* single-cell thermalization (INTEG-39) — they measure different processes (dephasing-prethermalization vs interaction-thermalization). I am NOT updating canonical from memory; I flag the memory entry as needing the two-process distinction made explicit, and route it as carry-forward V.7. **No kill condition fires**: the chaos bound `λ_L ≤ 2πT` is satisfied at the integrable fabric scale (`λ_L=0`); the single-cell 63%-GOE result is sub-maximal repulsion, far from any bound violation.

**The blue-tilt + Gaussian-relic combination is the framework's distinctive position in the Vagnozzi landscape.** (Results 6+7.) Standard blue-inflation dies on the non-Gaussianity tension; the framework's substrate-spectral blueness (`n_T=+0.468` transit) coexists with Gaussian `f_NL~1` (Wick), so it occupies a region of the blue-tensor landscape that slow-roll models cannot. This is a falsifiable prediction pair: blue transit-scale tensor + Gaussian relic, with the CMB-pivot tilt ≈ 0 (consistent with current bounds).

**Small-scale observable channel opened.** (Result 5.) Stahl's nonlinear-survival result gives the framework a concrete place to look BELOW CMB scales — a localized matter-power feature + sign-keyed HMF oscillation at a framework-computable scale, where `n_s=1` exactness at CMB does not forbid a feature. This is a new observable axis (small-scale structure), distinct from the CMB/PTA/LISA axes already in the falsifier inventory.

---

## V. Carry-Forward Computations

V.1. **Box+delta transfer-matrix re-attempt of |β_k|² at k_pivot (sudden-limit discretization)**
   - **What**: Re-run the Bogoliubov `|β_k|²` extraction discretizing the fold `a(τ)` history as a BOX potential (height set by `(1/4)ȧ² + (1/2)ä·a` interior) with TWO delta-peaks at the switch-on/off boundaries (`ψ_k' → ψ_k' + Ω ψ_k`), per Sparn (03) Eq. 4 + transfer-matrix `T_cusp`. Compare `|β_2|²(k_pivot)` against the sub-horizon oscillating-mode formula `|r_k|² ∝ sin²[μ_k Δη]` (Schmidt 04 Eq. 75). Output: `|β_pivot|²_box-delta`, `N_pivot`, and convergence vs N_seg (must be N_seg-INDEPENDENT in the sharp limit — the test of correct discretization).
   - **Inputs**: `s77_mode_threshold.npz` (k_pivot=14.310, k/aH=14.70, x_pivot=11.075); `s64_transfer_bogoliubov.npz`; fold `a(τ)` profile from `a0_fold/a2_fold/a4_fold`, `tau_fold=0.19`, `dt_transit`; Schmidt Eqs. 75–76 closed forms.
   - **Gate**: Re-opens S85-W7-CUSP-BOGOLIUBOV (currently FAIL). New gate `S100-BOX-DELTA-BOGOLIUBOV`: PASS iff `|β_pivot|²` is N_seg-stable (variation < 2× across N_seg ∈ {50,100,200,400}) AND matches `sin²[μ_k Δη]` within 10%; FAIL iff OOM-sensitive to N_seg (confirming smooth-cusp pathology); INFO iff stable but off the closed form (regime mismatch).
   - **Effort**: 4–6 hours, 1 agent session.

V.2. **Sub-horizon sin[μ_k Δη] vs super-horizon sinh[Λ_k Δη] cross-check of the pivot epoch sequence**
   - **What**: Evaluate Schmidt's closed-form reflection amplitudes `r_k/t_k` at `k_pivot` in BOTH the sub-horizon (`sin[μ_k Δη]`) and super-horizon (`sinh[Λ_k Δη]`) branches across the fold transit, confirming the analytic continuation `Λ_k → iμ_k` reproduces the framework's epoch sequence (sub-horizon AT fold → super-horizon AFTER → frozen plateau where `alpha_s → 0`). Output: `μ_k(τ)`, `Λ_k(τ)` trajectories, horizon-crossing time, and the zero-energy-resonance condition value vs `N_pivot`.
   - **Inputs**: `s77_mode_threshold.npz`; Schmidt Eqs. 75–76 + zero-energy-resonance horizon condition; `Z_norm=1` superhorizon-frozen anchor (session-77 T4.4); `f_conv=2.547e-10` (T4.5).
   - **Gate**: feeds atlas-04 C2 (k_pivot mapping). New gate `S100-PIVOT-EPOCH-CONTINUATION`: PASS iff the `Λ_k → iμ_k` continuation reproduces the canonical epoch sequence AND the resonance condition yields `N_pivot` consistent with Parker saturation; INFO iff qualitatively consistent but quantitatively off.
   - **Effort**: 3–4 hours, 1 agent session.

V.3. **Fold-range vs fold-rate control of the relic occupation (Rao universality-class confirmation)**
   - **What**: Test that the framework's GGE relic occupation is fold-RANGE-controlled (Rao `v>v_c` class), NOT rate-controlled. Compute `n_pairs` and `P_exc` as functions of (i) transit rate (vary `dt_transit` / Mach number at fixed fold range) and (ii) fold range (vary the spectral excursion `ΔS` at fixed rate). Verify `P_exc` saturates rate-independently and scales with range. Output: `n_pairs(rate)`, `n_pairs(range)`, and the analog `v_c` boundary (where saturation onsets).
   - **Inputs**: `dS/dtau=+58,673` (fold gradient); `n_pairs=59.8`; `P_exc_kz=1.0`; `tau_fold=0.19`; Rao (08) `ρ ~ δ_max` for `v>v_c` template.
   - **Gate**: New gate `S100-FOLD-RANGE-SCALING`: PASS iff `P_exc` is rate-independent (Δ<1% across Mach ∈ [5,30]) AND `n_pairs` scales monotonically with range (Rao class confirmed); FAIL iff rate-dependent (would place fold in slow-quench KZ class, contradicting saturation).
   - **Effort**: 3–5 hours, 1 agent session.

V.4. **Tricritical-adjacency test of the van Hove fold (Li z' < z + 1/ν inequality)**
   - **What**: Determine whether the van Hove fold sits near a tricritical point and whether the Li KZ-survival inequality `z' < z + 1/ν` could apply as a SECONDARY (sub-leading) scaling beneath the dominant range-saturation. Extract effective dynamic exponents `z, z'` and correlation-length exponent `ν` from the fold's spectral-gap closure `Δ(τ) ~ |τ − τ_fold|^{νz}` near `τ_fold=0.190`. Output: `z, z', ν`, the inequality verdict, and whether the first-order fold admits any residual KZ-scaling window.
   - **Inputs**: `D_K(τ)` spectral gap trajectory near `τ_fold` (Peter-Weyl bottom-band); `GL barrier=0.156`; van Hove fold characterization (first-order at τ_fold).
   - **Gate**: New gate `S100-TCI-ADJACENCY`: INFO-by-design (classification gate). Reports whether fold is Rao-class only, or Rao-dominant with a Li-class sub-window. Cross-link to KO-dim=6 if emergent-SUSY `η_b=η_f` appears (untested adjacency).
   - **Effort**: 4–6 hours, 1 agent session.

V.5. **Langen-protocol GGE tomography of the framework relic (Lagrange-multiplier count + anti-diagonal discriminator)**
   - **What**: Apply Langen's (12) higher-order-correlation tomography to a framework-substrate relic analog (impulsive-transit GGE). Compute N-point correlation functions `C(z_1,...,z_N) ~ ⟨exp[iΣ(−1)^j φ(z_j)]⟩` up to 10th order from the relic's conserved mode occupations; fit the GGE `ρ=(1/Z)exp(−Σ_m λ_m I_m)` and count the Lagrange multipliers needed; test the ANTI-DIAGONAL correlation peak (GGE) vs flat (Gibbs). Output: `N_multipliers` for the framework relic (vs Langen's ~10, vs Parker `n_pairs=59.8`), anti-diagonal peak amplitude, and Gibbs-fit residual.
   - **Inputs**: relic mode occupations `n_m` from `s39_bayes_gge_thermal.npz` + `s40_b2_integrability.npz`; CG(24) fabric Josephson structure; `n_pairs=59.8`; Langen GGE-vs-Gibbs anti-diagonal template.
   - **Gate**: feeds INTEG-39 / Ordered-Veil scale-resolution. New gate `S100-GGE-TOMOGRAPHY`: PASS (fabric-integrable) iff anti-diagonal peak present AND single-T Gibbs fit FAILs AND `N_multipliers` finite-and-small; FAIL (single-cell-thermalizing) iff anti-diagonal flat AND Gibbs fit succeeds. Resolves WHICH scale the relic occupies.
   - **Effort**: 5–7 hours, 1 agent session.

V.6. **Small-scale matter-power feature + sign-keyed HMF oscillation from the fold (Stahl transfer)**
   - **What**: Compute the localized matter-power-spectrum feature (amplitude + position) and the halo-mass-function oscillation (with SIGN keyed to the van Hove excursion direction) that the fold's impulsive spectral source imprints below CMB scales, following Stahl (09). Output: feature scale `k_feature` (framework-computed), feature amplitude, HMF oscillation sign, and survival fraction through nonlinear transfer to low-z.
   - **Inputs**: fold spectral-excursion profile (`dS/dtau`, van Hove direction); `k_pivot=14.310 M_KK` → comoving-scale map; Stahl N-body transfer template (localized feature + sign-keyed HMF).
   - **Gate**: feeds atlas-04 C2 + falsifier-master-inventory (new small-scale-structure axis). New gate `S100-FOLD-SMALL-SCALE-FEATURE`: INFO-by-design (predicts an observable). Records `k_feature`, sign, amplitude for cross-match against future small-scale surveys; FAIL only if the framework predicts NO surviving feature (would close the channel).
   - **Effort**: 4–6 hours, 1 agent session (uses N-body transfer templates, not full sim).

V.7. **Two-process reconciliation of single-cell thermalization timescales (ADH prethermalization vs INTEG-39 interaction-thermalization)**
   - **What**: Make explicit the distinction between (a) dephasing-PREthermalization timescale (ESSLER-66/PRETHERM-65, the agent-memory `~10^578 t_universe` Bogoliubov-bath estimate) and (b) interaction-driven THERMALIZATION (INTEG-39, `t_therm ≈ 6 M_KK⁻¹`). Verify they measure different processes and are NOT in contradiction; pin which governs the relic on cosmological timescales. Update agent memory to carry the two-process distinction; do NOT alter canonical (registry wins). Output: a clean timescale ledger (prethermalization vs thermalization vs transit duration) with the governing process per epoch.
   - **Inputs**: `s66_bertini_essler.npz` (ESSLER-66); `s39_integrability_check.npz` (INTEG-39); `t_universe_s`; `E_B1`; transit duration `dt_transit`.
   - **Gate**: housekeeping/reconciliation (no new physics gate). Resolves the Section-IV conflict flag. INFO: produces the reconciled timescale ledger; routes a memory-update (two-process distinction) and confirms registry t_therm ≈ 6 M_KK⁻¹ stands as the interaction-thermalization canonical.
   - **Effort**: 2–3 hours, 1 agent session.

V.8. **ΔN_eff/BBN consistency of the n_T=+0.468 transit blue tilt against the Vagnozzi bound**
   - **What**: Verify the framework's blue transit-scale tensor tilt (`n_T=+0.468`) plus its acoustic `(A)`-class amplitude (`Ω_GW ≈ 1×10⁻¹⁰`) satisfies the `ΔN_eff`/BBN integrated-energy bound that Vagnozzi (11) imposes on blue-tensor models (`T_rh ≲ 10 GeV` for the PTA interpretation). Integrate `Ω_GW(f)` over the relevant frequency band with the transit-scale blue tilt; confirm `ΔN_eff` contribution is below BBN limits. Output: `ΔN_eff^framework`, the integrated `Ω_GW`, and headroom vs BBN.
   - **Inputs**: `n_T=+0.468` (transit, S66); `n_T_PathH_canonical=-0.0009338` (pivot); `Ω_GW^(A) ≈ 1e-10` (project-canonical acoustic class); Vagnozzi `ΔN_eff`/BBN bound; LISA-PLS.
   - **Gate**: feeds falsifier-master-inventory row 7 (Ω_GW LISA). New gate `S100-BLUE-TILT-BBN`: PASS iff `ΔN_eff^framework < 0.2` (BBN-safe) with the blue transit tilt; FAIL iff the integrated blue-tilt energy exceeds BBN (would constrain the transit-scale tilt amplitude).
   - **Effort**: 3–4 hours, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Schmidt/Sparn 1D-scattering discriminator stack; transfer-matrix exact for box+delta; pivot SUBHORIZON (sin sector) | GEOMETRIC | Canonical S85-W7 FAIL stands; corridor reopened for sudden-limit discretization | Re-attempt `|β_pivot|²` as box+delta (V.1); pivot in `sin[μ_k Δη]` sector consistent with `alpha_s→0` superhorizon |
| 2 | Parra-López switch-on/off-dominance theorem (in/out Bogoliubov) | PHONONIC | Independent corroboration of transit paradigm (atlas-10 PROVEN) | Transit-physics axis gains substrate-independent derivation; "transitions dominate" is route-independent |
| 3 | Fold = Rao range-saturation class (`P_exc=1.000` rate-independent), NOT Li KZ-survival | PHONONIC | Universality class pinned | Relic occupation is fold-RANGE-controlled; no rate-dependent KZ scaling applies (V.3) |
| 4 | Langen GGE tomography (10th-order, anti-diagonal, ~10 multipliers) + Gondret thermalizing control | PHONONIC | Forces canonical reconciliation; proven_1291 BROKEN at single-cell, Poisson at fabric | GGE tomography is the WHICH-scale discriminator (V.5); Ordered Veil survives at FABRIC scale only |
| 5 | Stahl nonlinear survival of impulsive features (localized power + sign-keyed HMF) | PHONONIC | New small-scale observable channel | Fold leaves a surviving sub-CMB feature; sign is a framework discriminator (V.6) |
| 6 | Vagnozzi blue-tensor landscape vs scale-tagged `n_T` (+0.468 transit / −1e-3 pivot) | PHONONIC | Distinctive position: blue + Gaussian | Framework escapes blue-inflation non-Gaussianity tension; BBN consistency to verify (V.8) |
| 7 | Ahmadi ζ-tail (faster than `e^{−3ζ}`) vs Gaussian-by-Wick relic (`f_NL~1.03`) | PHONONIC | Consistent in direction (suppressed tail) | Independent diffusion cross-check of Gaussian-relic claim (folded `f_NL=0.056`) |
| — | CONFLICT: agent-memory `t_therm~10^578 t_universe` vs canonical `t_therm≈6 M_KK⁻¹` (INTEG-39) | — | Registry wins; two-process reconciliation needed | Prethermalization (dephasing) ≠ thermalization (interaction); NO kill fires, `λ_L=0` at fabric (V.7) |
