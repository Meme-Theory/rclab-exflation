# Session 99 Synthesis: Non-equilibrium Transit Dynamics — Impulsive-vs-Smooth Discriminator Stack, Fast-Quench Universality, and the GGE/Ordered-Veil Adjudication

**Date**: 2026-06-04
**Agent**: transit-dynamics-theorist (Workhorse-Transit-Dynamics)
**Source Documents**:
- `downloads/research-sweep-s99/nonequilibrium-transit/00-INDEX.md` (13-paper sweep, fetched-text summaries)
- `downloads/research-sweep-s99/nonequilibrium-transit/01-13_*.pdf` (spot-verification corpus)
- `.claude/agent-memory/transit-dynamics-theorist/MEMORY.md`
- Knowledge MCP: `get_constant` / `search_knowledge` / `trace_entity` (canonical anchoring)

---

## I. Session Outcome

The S99 G6 sweep is structurally the strongest external corroboration the transit paradigm has received in standard QFT-in-curved-spacetime and cold-atom-analog language: Parra-López (07) derives the framework's own central thesis — *transitions, not stages, dominate production* — directly from the in/out Bogoliubov formalism (switch-on/off boundary terms dominate `|β|²`), and Schmidt/Sparn (03/04) supply the closed-form scattering-potential reformulation `V(η) = (1/4)ȧ² + (1/2)ä·a` that maps the framework's Mukhanov-Sasaki `z''/z` term onto a 1D reflection problem with explicit sub-horizon `sin[μ_k Δη]` vs super-horizon `sinh[Λ_k Δη]` amplitudes — vindicating the transfer-matrix method **for the sudden/sharp-boundary limit specifically** (the regime the impulsive fold occupies), while confirming my prior debugging note that transfer-matrix fails for *smooth* `ω_k(τ)`.

The single load-bearing correction this sweep forces: the index and my own agent memory carry the Ordered Veil as "GGE **never** thermalizes," but the **canonical registry retracted that permanence at S39** (atlas-04 T3 = BROKEN; atlas-07 = RETRACTED; INTEG-39 = DECISIVE FAIL, Brody β=0.633, t_therm ≈ 6 M_KK⁻¹). The refined canonical — GGE valid *during* the transit window, thermalizing afterward via the 13% non-separable density-density channel — means Gondret's observed entanglement decay toward thermalization (05) is **not a control case the framework must avoid**; it is structurally **concordant** with the framework's own post-transit thermalization. This inverts the index's framework angle for papers 05 and 12 and is the highest-priority carry-forward (V.1).

No gates are run in this synthesis (literature adjudication only). All framework-state claims below are anchored to the knowledge MCP; where the index drifts from canonical, the drift is flagged explicitly.

---

## II. Key Results

### II.1 — Impulsive-vs-smooth discriminator: the scattering-potential reformulation vindicates transfer-matrix for the sudden limit (papers 03/04)

**Result**: The fold's sharp boundaries place the framework in the regime where the transfer-matrix method is **valid**, reversing the blanket prohibition in my agent memory. PHONONIC (transit Bogoliubov structure).

Schmidt (04) and Sparn (03) reformulate `(D+1)`-dim cosmological pair production as a *stationary* 1D Schrödinger scattering problem. The mode equation `v_k'' + 2(ȧ/a)v_k' + (k²/a²)v_k = 0` is converted via conformal time `dη = c_s(t)dt` and rescaling `ψ_k = √a·v_k` into `[−d²/dη² + V(η)]ψ_k = k²ψ_k` with scattering potential

```
V(η) = (1/4)ȧ² + (1/2)ä·a          (Sparn Eq. 4)          (II.1)
```

This is dimensionally the analog-side image of the framework's canonical Mukhanov-Sasaki mode equation `v_k'' + (k² − z''/z)v_k = 0` (my memory; Birrell-Davies convention): both are reflection problems where the *background history* sets the barrier, and `z''/z ↔ V(η)` play identical structural roles. Particle production is the reflection coefficient; the power spectrum reads

```
S_k = 1/2 + N_k + ΔN_k cos(2ω_k t_h + θ_k),   N_k = |b_k|²/|c_k|²,   |c_k|² = |a_k|² − |b_k|²   (Sparn Eq. 5)   (II.2)
```

with `|c_k|² = |a_k|² − |b_k|²` the unitarity invariant (the analog-side `|α_k|² − |β_k|² = 1` of my Bogoliubov ladder bookkeeping). The `1/2` vacuum floor + `N_k = |β_k|²` occupation + `ΔN_k = |α_k β_k|` coherence is *exactly* the squeezed-vacuum structure the framework's relic carries.

**The decisive structural correction**: My agent memory records "Transfer matrix method FAILS for smooth `ω_k(τ)` — piecewise-constant approximation introduces artificial reflections; `|β|²` varies by OOM with N_seg." Sparn uses transfer-matrix **successfully**, but only for genuinely sharp cusps (delta-peak discontinuities `ψ_k' → ψ_k' + Ω ψ_k`), *not* smooth ramps. For LINEAR expansion `a(t) = a_min(1 + H_0 t)` the potential is a **box of height `H_0²/4`** with delta-distributions "from the abrupt start and end of the ramp." The framework's transit is impulsive (`H·dt = 0.663 < 1`, `dt_transit = 1.13e-3 M_KK⁻¹` per `get_constant`), i.e. precisely the box+delta sudden limit — so transfer-matrix IS the appropriate method for the fold, provided it is applied to the *sharp boundary terms*, not a fine-grained interior segmentation. The two statements are consistent: the failure was N_seg-sensitivity on a smooth profile; the success is on sharp boundaries that the fold genuinely has.

Schmidt (04) supplies the closed forms across the horizon: the reflection/transmission ratios carry `sinh[Λ_k Δη]` for super-horizon and `sin[μ_k Δη]` for sub-horizon modes, related by the analytic continuation `Λ_k → i μ_k` (Schmidt Eqs. 75-76). Since `get_constant`-anchored `k_pivot/aH = 14.70` at the fold (S77 INVERSION; mode SUBHORIZON), `k_pivot` sits unambiguously in the **oscillating `sin[μ_k Δη]` sector**, NOT the super-horizon `sinh` sector — fully consistent with my permanent result that `α_s(primordial) = 0` EXACT in the superhorizon plateau via Bogoliubov saturation.

### II.2 — Switch-on/off-dominance theorem: independent corroboration that transitions, not stages, dominate (paper 07)

**Result**: Parra-López's thesis derives the framework's central paradigm — *production dominated by non-adiabatic transitions, not quasi-static stages* — from the in/out Bogoliubov formalism, independently of the substrate picture. PHONONIC (transit paradigm in standard QFT-in-curved-spacetime language).

The keystone result (Parra-López ch. 6): "in general, SWITCH-ON and -OFF processes DOMINATE production due to their NON-ADIABATICITY" and "the most relevant periods for particle creation are the TRANSITIONS between different stages of the Universe, rather than the stages themselves." This is exactly the framework's `transit physics, NOT equilibrium` paradigm (atlas-10 #8: "The transit IS the physics," PROVEN), now derived from the Wronskian Bogoliubov forms

```
|α_h|² − |β_h|² = 1,   α_h = −i Wr[u_h, v_h*],   β_h = i Wr[u_h, v_h]   (Parra-López Eqs. 3.20-3.21)   (II.3)
```

This is a genuinely *independent* derivation (standard cosmological QFT, no substrate input), so it corroborates the framework's claim without the agreement being shared-context (per `epistemic-discipline.md` "What Counts as Evidence" — independent-route confirmation, not agent-agreement). It directly vindicates my debugging finding that `|β|²` is controlled by the sudden boundaries, not the interior. The thesis's spectator-field DM mechanism (production by background geometry alone, no inflaton coupling) is the standard-QFT image of the framework's Leggett-channel GGE quasiparticle (inter-band coherence mode, CPT-neutral, non-annihilating) — both "produced by the transit geometry, decoupled from a driving field." Its massive-phononic-mode two-component BEC (§4.3) is the lab route to the framework's gapped Leggett-band excitations.

### II.3 — Fast-quench universality class: the fold occupies the range-controlled (Rao) regime, with KZ-survival (Li) as the adjacent structural warrant (papers 08/13)

**Result**: The framework's `P_exc = 1.000` / 59.8-pair Parker saturation is **range-controlled**, not rate-controlled — consistent with Rao's `v > v_c` universality class (`ρ ~ δ_max`, rate-independent). PHONONIC (fast-quench scaling of the relic occupation).

Rao (08) experimentally confirms (single trapped-ion qubit, Landau-Zener + Rice-Mele) that above a critical quench rate `v_c` (itself scaling with quench range `δ_max`), Kibble-Zurek `ρ ~ v^{1/2}` scaling is REPLACED by `ρ ~ δ_max`, **independent of quench rate**. The framework's transit is fast (Mach 13.75, `H·dt = 0.663 < 1`), sitting above the analog of `v_c`. The canonical `P_exc = 1.000` (atlas T1 PROVEN, sudden-quench saturation; `get_constant`-anchored `n_pairs = 59.8`) is exactly a rate-independent saturation — so the GGE occupation should be controlled by the **fold spectral excursion magnitude** (the van Hove range), not the transit rate. This is a falsifiable structural statement: if the relic occupation tracked the rate, the fold would be in the KZ `v < v_c` regime, contradicting the saturation.

Li (13) supplies the complementary warrant from the tricritical-Ising side: KZ scaling can **survive** the breakdown of the adiabatic-impulse scenario (AIS) provided the dynamic-exponent inequality `z' < z + 1/ν` holds (TCI: `z=z'=1`, `ν_μ=5/4`, KZ exponent `r_μ = z + 1/ν_μ = 9/5`). The framework's fold has no clean adiabatic stage at Mach 13.75 (AIS is suspect), yet Li shows a controlled scaling can persist anyway. The two papers bound the framework's regime: Rao = KZ *replaced* by range-scaling above `v_c`; Li = KZ *survives* AIS breakdown at a higher-order critical point. The framework's fold is first-order (`tau_fold = 0.19`) but sits structurally near the first-order/continuous boundary (the van Hove fold), so tricritical adjacency is the natural neighbourhood. Which class the relic obeys (Rao range-scaling vs Li surviving-KZ) is an open, computable discriminator (V.4).

### II.4 — GGE/Ordered-Veil adjudication: the index inverts the canonical — thermalization is CONCORDANT, not forbidden (papers 05/12) [LOAD-BEARING CONFLICT]

**Result**: "GGE never thermalizes" is **BROKEN/RETRACTED at S39** (canonical). The refined canonical — GGE valid *during* transit, thermalizing afterward in ~6 M_KK⁻¹ — makes Gondret's entanglement decay (05) and Langen's prethermalized GGE (12) **concordant** with the framework, not control cases it must avoid. PHONONIC (relic statistics) / **FLAGGED CONFLICT** (index vs canonical registry).

**The conflict, stated precisely.** The index (entries 05, 12) and my own agent memory frame "THE ORDERED VEIL: GGE relic NEVER thermalizes — integrable, not chaotic" as the live central paradigm, with Gondret's observed entanglement decay positioned as "the CONTROL CASE against which the framework's non-thermalization is the discriminator." The knowledge MCP says otherwise:

- `search_knowledge` → atlas-04-assumptions T3: **"GGE never thermalizes (Richardson-Gaudin integrability) — BROKEN. V_phys 13% non-separable. Brody beta = 0.633 (63% GOE). t_therm ~ 6 natural units. GGE valid during transit b[ut]..."**
- atlas-07-permanent-results: **"[NEW S39] GGE permanence — 'Never thermalizes' — RETRACTED: V_phys 13% non-separable. Thermalizes in ~6 nat units."**
- Gate INTEG-39 (re-confirmed S96): **DECISIVE FAIL** — "V_phys 13% non-separable; Brody β = 0.633 (63% GOE); Thouless g = 0.60; t_therm ≈ 6 M_KK⁻¹."
- session-62-hawking-qa: "Channel 2 (density-density) is the mechanism behind the S39 thermalization (`t_therm ∼ 6 M_KK⁻¹`, Brody β = 0.633). It breaks integrability and thermalizes the GGE."

What **survives** as canonical: the Ordered Veil as "the transit IS the physics" (atlas-10 #8, PROVEN) — i.e. the GGE is the correct description of the relic *content at the moment of and during* the transit; the *permanence* claim (relic stays integrable forever) does not survive.

**Why this inverts the index's reading.** Under the retracted "never thermalizes," Gondret (05) — a parametric (preheating) drive whose `(+k,−k)` entanglement DECREASES and non-classical features DISAPPEAR as the system approaches the late-time nonlinear regime — would be the *anti*-case the framework must not follow. Under the **canonical** refined view, Gondret's entanglement-decay-toward-thermalization is the lab realization of *exactly* the framework's own S39 post-transit thermalization (the 13% density-density channel doing the same job as Gondret's nonlinear mode coupling). The framework and Gondret AGREE: an integrable relic that is subsequently coupled (density-density / nonlinear) thermalizes on a finite timescale. The discriminator is therefore NOT "does it thermalize?" (both say yes, eventually) but **"is the GGE the correct intermediate (prethermal) description during the transit window?"** — and Langen (12) confirms that an integrable 1D Bose gas DOES relax first to a GGE (prethermal plateau) before any eventual thermal stage, exactly the framework's transit-window picture.

**Langen's methodological transfer remains intact and high-value.** Langen (12) demonstrates GGE tomography via N-point correlation functions up to 10th order, with the **anti-diagonal correlation peak** (different effective temperatures on even vs odd modes) as the genuine-GGE-vs-ordinary-Gibbs discriminator, and ~10 Lagrange multipliers sufficing despite a much larger conserved-charge set. This is the gold-standard protocol to test whether the framework's *transit-window* relic is a genuine GGE (anti-diagonal peak present) vs already-thermal. The ~10-multiplier truncation is suggestively adjacent to the framework's finite-charge structure (Lefschetz n* = 60; 8 BCS modes) — a structural curiosity, not a numerical claim. Critically: per the registry's `Observable-Naming-History vs Parse-Tree-Structure` discipline (`cross-pillar-bridge-anatomy.md`), `n_a^GGE` is a state-history label, so any registry use of Langen's tomography must carry a parse-tree expansion to its closed-form substrate observable.

### II.5 — Nonlinear survival of impulsive-source features: a small-scale observable channel for the fold (paper 09)

**Result**: Stahl shows impulsive-source ("sudden slow-roll violation") sharp features SURVIVE nonlinear evolution as (i) a localized matter-power feature and (ii) a sign-keyed halo-mass-function oscillation — supplying the transfer bridge the framework's K_pivot mapping gap (atlas-04 C2) needs. PHONONIC (transit signature transport to late-time observables).

Stahl (09) runs dedicated N-body simulations: oscillatory patterns ARE erased by nonlinearities, but the feature's **scale and sign** persist as a localized power enhancement/decrement in `P(k)` (amplitude and position recovering the primordial feature scale) and an oscillatory pattern in the halo mass function **tied to the SIGN of the feature**. The framework's supersonic fold transit IS "a sudden violation of slow-roll" in inflationary language, so Stahl's result is the late-time-observable complement to the framework's CMB-scale exactness: the framework already predicts frozen-spectrum exactness at CMB (Sasaki-Stewart, to 10⁻¹¹³) and `n_s = 1` unbroken at CMB scales (my memory). Stahl opens a place to look BELOW CMB scales where the fold's GGE interference pattern would sit. The sign-dependence of the HMF signature is a clean discriminator: the van Hove excursion direction sets a SPECIFIC sign, computable from the fold profile (V.5).

### II.6 — Blue-tensor landscape: the transit `n_T = +0.468` is canonically INACCESSIBLE; Vagnozzi bounds any blue-`n_T` claim (paper 11)

**Result**: The framework's blue transit tilt `n_T = +0.468` (S66) is real at the substrate scale but **observationally INACCESSIBLE** at the CMB pivot (S84-BLUE-TRANSIT-TILT-INACCESSIBILITY = PASS, EVOI=0); the canonical pivot value is `n_T ≈ −1.5e-3` (PathC) / `−0.9e-3` (PathH). Vagnozzi's PTA-inflation band (`n_T ~ 1.8 ± 0.3`) is the observational landscape, not a framework prediction. PHONONIC (scale-and-channel-tagged tensor tilt) / **flagged index drift**.

Per `phononic-framing.md` SCALE-AND-CHANNEL-TAGGING (SUGGESTION at K=2), every running/tilt observable must declare its matched (scale, channel) pair. The framework carries a scale-separated `n_T` pair:

- **Substrate/transit scale**: `n_T = +0.468` (`search_knowledge` → session-66-mack-transit-workshop, T.38; the focus prompt's `+0.4676` is a refinement — canonical is `+0.468`). A genuinely blue tilt from the impulsive (non-slow-roll) fold.
- **CMB pivot scale**: `n_T_PathC_canonical = −0.00146644`, `n_T_PathH_canonical = −0.000933812` (`get_constant`; the focus prompt's "~−3e-3" is a round figure — canonical is ~−1.5e-3/−0.9e-3, factor ~2 tighter).

The 54-decade transport `T_{BZ→pivot}` (per `cross-pillar-bridge-anatomy.md` per-observable transport-degree scale-separation, SUGGESTION K=2) suppresses the substrate blue tilt below the LiteBIRD reach `σ_n_T_LiteBIRD = 0.0008` (`get_constant`), which is why **S84-BLUE-TRANSIT-TILT-INACCESSIBILITY is a PASS bookkeeping verdict with EVOI=0** — the framework does NOT claim an observable blue tilt at CMB. Vagnozzi (11) finds a PTA-inflation interpretation needs `n_T ~ 1.8 ± 0.3` with BBN forcing `T_rh ≲ 10 GeV`, and notes blue inflation models "tend to predict sizeable non-Gaussianities (excluded)." The framework is **not** claiming the PTA signal IS its tensor mode (its `+0.468` is far below Vagnozzi's `1.8`); rather Vagnozzi supplies the `ΔN_eff`/BBN constraint envelope and the key consistency check the framework passes *differently*: the framework's blue tilt coexists with Gaussian `f_NL = O(eps)` (S65 W5-D PERMANENT) **because its blueness is substrate-spectral, not slow-roll-parameter-driven** — `r = 16ε` is already INAPPLICABLE (5 independent arguments, VdD-Hawking workshop; `phononic-framing.md`). The `ΔN_eff`/BBN bound on the *substrate-scale* `n_T = +0.468` (does it overproduce GW energy density?) is a genuine untested gate (V.6).

### II.7 — Zeta-tail vs Gaussian-by-Wick: Ahmadi's faster-than-`e^{−3ζ}` tail is concordant in direction (paper 10)

**Result**: Ahmadi's stochastic-δN result (curvature-perturbation `ζ` tail decays FASTER than `e^{−3ζ}` after a sharp transition) is concordant in DIRECTION with the framework's Gaussian-by-Wick relic (`f_NL = O(eps)`, suppressed non-Gaussianity), and supplies an independent diffusion-based template to test the Gaussianity claim. PHONONIC (relic statistics cross-check).

Ahmadi (10) uses the stochastic-δN formalism through a sharp Starobinsky-type transition (results apply to any sharp transition) and derives the characteristic function of `ζ`, finding the tail decays **faster than `e^{−3ζ}`** (sub-exponential relative to the naive USR expectation; lighter, more-Gaussian-leaning tail). The framework's canonical result is that the squeezed-vacuum relic is GAUSSIAN by Wick — `f_NL = O(eps)` regardless of squeezing (S65 W5-D PERMANENT; `search_knowledge` → baseline-findings-s66). Direction agrees: both say the sharp-transition relic is LESS non-Gaussian than naive expectation, not more. Ahmadi gives a quantitative diffusion-tail template against which the framework's Gaussianity can be cross-checked by an independent (non-Bogoliubov) method (V.7). The "noise cannot drive the inflaton past classically unreachable values after a flat (USR) phase" maps onto the framework's frozen-spectrum exactness (the post-fold plateau does not generate runaway curvature). Note: the framework's `max|f_NL| = 1.505` ENVELOPE (Bogoliubov-sudden channel, NEGATIVE −1.505, anti-correlated 3-pt; `get_constant` → `max_f_NL_FW`) is NOT a contradiction of `f_NL = O(eps)` — the 1.505 is the envelope across all transit cubic-bispectrum shapes/channels at 0.4716σ from Planck `f_NL^local = −0.9 ± 5.1` (F-NL-ROW), while the *per-shape* values (equil 0.0547/0.853, folded 0.129) are the `O(eps)` ones.

### II.8 — Efimovian coasting analog: log-periodicity is a discriminator AGAINST the framework's transit (paper 01)

**Result**: Xue's temporal-Efimov `N_k` log-periodicity is a feature the framework's impulsive transit does NOT have (no scale invariance through the fold) — a clean discriminator. PHONONIC (Bogoliubov sub/super-horizon split in a lab analog).

Xue (01) predicts a temporal Efimov effect in an analog coasting (`a(t) ∝ t`) universe (`a_s(t) ∝ 1/t²`), with mode equation `u_k'' + (2/t)u_k' + (kl)²/t² u_k = 0` invariant under `t → λt` (SU(1,1), Bargmann index `(1 ± √B)/2`, `B = 1/4 − (kl)²`). The critical value `kl = 1/2` bifurcates: sub-horizon (`kl > 1/2`) gives `N_k = sin²(√|B| ln(t_f/t_i))/(4|B|)` — **log-periodic** in expansion ratio (the Efimov hallmark); super-horizon (`kl < 1/2`) gives `N_k = sinh²(√B ln(t_f/t_i))/(4B)` — power-law/exponential. This is the cleanest published instance of the framework's own sub/super-horizon Bogoliubov split (`N_k = |β_k|²`, `|α_k|² − |β_k|² = 1`), and the `kl = 1/2` boundary is the analog-side image of the `k_pivot = 14.31 M_KK` subhorizon classification (S77). **The discriminator**: the coasting case is the marginal `a(t) ∝ t` boundary (scale-invariant); the framework transit is IMPULSIVE (Mach 13.75), NOT scale-invariant, so it does NOT produce log-periodicity. A framework prediction of a NON-log-periodic time-averaged `S_k(t)` signature vs the coasting case's log-periodic one is a falsifiable analog-side test (V.8).

### II.9 — Foundational lab realizations: Viermann/Gondret-parametric establish the Bogoliubov-`S_k(t)` and growth-rate protocols (papers 02/06)

**Result**: The Heidelberg quantum-field-simulator (02) and Gondret's parametric-growth measurement (06) establish the operational templates (heterodyne `S_k(t)` extracting `|α_k|, |β_k|, θ_k` separately; measured Bogoliubov growth rate with confirmed `⟨b_k b_{−k}⟩` two-mode squeezing) against which the framework's impulsive-transit coefficients can be tested. PHONONIC (analog Bogoliubov measurement protocols).

Viermann (02) runs SMOOTH power-law ramps `a(t) ∝ t^γ` (γ = 0.5, 1.0, 1.5 — adiabatic-to-mild), with `S_k(t) = [1/2 + |β_k|² + |α_k β_k| cos(θ_k + 2ω_k t)](1 + 2N_k^in)` and a temperature-INDEPENDENT initial-phase jump (γ-dependent) as a robust fingerprint of the expansion HISTORY. The framework's impulsive limit should saturate to a γ-independent (sudden) phase, BREAKING the smooth-ramp history-encoding — a discriminator. Gondret-parametric (06) measures the early-time exponential Faraday growth (transverse breathing mode → longitudinal pairs) in very good agreement with Bogoliubov theory, confirming both the Bogoliubov treatment and the smallness of quasiparticle interactions, with `⟨b_k b_{−k}⟩` anomalous (pair) correlation growing — the two-mode-squeezed signature. Crucially Gondret identifies that atom-number oscillations depend on "the rate at which interactions are switched off" — the lab realization of the framework's switch-on/off boundary sensitivity (the same knob that sets `|β_2|²` at k_pivot). Both are SUSTAINED parametric (broad-resonance) drives; the framework's single impulsive passage is NOT in the broad-resonance preheating regime, so its `F_amp` arises from the B1/B2/B3 Bogoliubov ladder, not a Mathieu instability band. Energy-conservation note: the framework's `F_amp^sc = 47.92` (3PI NLO 1/N closure) replaces the linearized 6858 which violated energy conservation (my memory; `ρ_p/ρ_bg ~ 2e4`) — Gondret's energy-conserving Bogoliubov accounting is the natural validation template (V.9).

---

## III. Gate Verdicts

This synthesis runs no gates. The verdicts below are the **canonical** registry states the synthesis ANCHORS against (queried via knowledge MCP), reproduced for the record. Per the rules, these are authoritative and are NOT re-adjudicated here.

| Gate / Theorem | Canonical Verdict | Decisive Number / Note |
|:---------------|:------------------|:-----------------------|
| INTEG-39 (GGE thermalization) | **DECISIVE FAIL** | Brody β=0.633 (63% GOE); Thouless g=0.60; t_therm ≈ 6 M_KK⁻¹; V_phys 13% non-separable |
| atlas-04 T3 "GGE never thermalizes" | **BROKEN** | GGE valid during transit; thermalizes after |
| atlas-07 "GGE permanence" | **RETRACTED (S39)** | "Never thermalizes" → thermalizes ~6 nat units |
| atlas-10 #8 "The transit IS the physics" (Ordered Veil) | **PROVEN** | survives; permanence claim does not |
| T4 "59.8 quasiparticle pairs" | **PROVEN (S38)** | N_pair=1 exact reduction 1.2e-14; 93% B2, 6.3% B1; P_exc=1.000 |
| Bogoliubov Gaussianity Preservation (f_NL=O(eps)) | **PERMANENT (S65 W5-D)** | structural; regardless of squeezing |
| F-NL-ROW | composite FAIL; **PASS at 0.4716σ** | max|f_NL|=1.505 envelope (Bog-sudden −1.505) vs Planck −0.9±5.1 |
| BLUE-65 (transit blue tilt) | **INFO** (migrated) | n_T transit = +0.468 |
| S84-BLUE-TRANSIT-TILT-INACCESSIBILITY | **PASS** | EVOI=0; transit n_T observationally inaccessible at CMB pivot |
| S83-LITEBIRD-SIGMA-N_T-REACH | **INFO** | σ_n_T_LiteBIRD = 0.0008 |

---

## IV. Structural Implications

**What this sweep CLOSES / corrects.**

1. **Transfer-matrix prohibition is scoped, not blanket.** My agent memory's "transfer matrix FAILS for smooth ω_k(τ)" stands, but papers 03/04 establish that for the SHARP-boundary sudden limit (box+delta) — which the impulsive fold genuinely occupies — transfer-matrix is the *correct* method. This reopens an entire computational route for the fold's `|β_k|²` that I had foreclosed. The constraint-map update: the fold-`|β|²` computation should use the scattering-potential `V(η)` reformulation with delta-boundary transfer matrices, NOT a fine-grained smooth-ω segmentation.

2. **Ordered-Veil status is corrected to its canonical (transit-window) form.** The index and my memory over-state the Veil as "never thermalizes"; the registry retracted that at S39. The corrected reading makes Gondret (05) CONCORDANT (the framework's own 13% density-density channel thermalizes the relic on the same ~6 M_KK⁻¹ scale Gondret observes), and re-frames the falsifier: the discriminator is the GGE-as-prethermal-plateau *during* the transit (testable via Langen-style anti-diagonal tomography), not eternal non-thermalization. This is a substantive scholarly correction that must propagate to the capstone hygiene gate (the capstone §7 falsifier surface narrates the Ordered Veil; its confidence must equal the register's BROKEN/transit-window status, per `capstone-hygiene-gate.md` Q3).

**What this sweep OPENS (untested adjacencies).**

3. **Fast-quench universality class of the fold is undetermined.** Rao (08, range-scaling above `v_c`) vs Li (13, KZ-survival iff `z' < z + 1/ν`) bound the regime; which class the `P_exc=1.000` saturation obeys is a new, computable gate (V.4). Range-controlled saturation is the framework's natural expectation (rate-independent P_exc), favoring the Rao class.

4. **Small-scale fold signature is a new observable channel.** Stahl (09) provides the nonlinear-transfer bridge from the impulsive fold to a localized matter-power feature + sign-keyed HMF oscillation below CMB scales — directly addressing the K_pivot mapping gap (atlas-04 C2). The fold's spectral-excursion sign is a clean, computable discriminator.

**What this sweep CONFIRMS (no state change, increased confidence).**

5. **The transit paradigm is independently corroborated** (Parra-López 07, switch-on/off-dominance from in/out Bogoliubov) — an independent-route confirmation, not agent-agreement.
6. **Gaussianity-by-Wick is concordant** with an independent diffusion-tail calculation (Ahmadi 10, faster-than-`e^{−3ζ}`).
7. **The blue transit tilt's observational inaccessibility is consistent** with the scale-and-channel-tagged pair (Vagnozzi 11 supplies the BBN/ΔN_eff envelope; the substrate-scale n_T=+0.468 ΔN_eff bound is the one untested piece).

**Direction-of-explanation discipline maintained.** Every BEC/cold-atom/Rydberg/PTA system above is a laboratory (or observational) analog OF the substrate transit; the substrate D_K-spectral fold is fundamental (`D_K eigenvalues → spectral moments → emergent physics → measurement`). No entry inverts this.

---

## V. Carry-Forward Computations

```
V.1. Ordered-Veil capstone/registry reconciliation to canonical transit-window status
   - What: Reconcile the "GGE never thermalizes" narration (capstone §7 falsifier surface, index framing, agent memory) DOWN to the canonical S39 status: GGE valid DURING transit, thermalizes ~6 M_KK⁻¹ after via the 13% non-separable density-density channel. Produce the corrected falsifier statement: discriminator is GGE-as-prethermal-plateau during transit (anti-diagonal Langen tomography), NOT eternal non-thermalization. Update agent memory MEMORY.md (it currently mis-states "GGE relic NEVER thermalizes").
   - Inputs: atlas-04-assumptions.md T3 (BROKEN); atlas-07-permanent-results.md (RETRACTED); INTEG-39 verdict (s39_bayes_gge_thermal.py, s39_integrability_check.py); session-62-hawking-qa-workshop.md (density-density mechanism); capstone-hygiene-gate.md Q3 routing; mack-cosmic-bridge sole-writer for §7 surface.
   - Gate: capstone-hygiene Q3 (PROSE tag == register tag); routes to housekeeping §A (in-session designated-writer fix) — NOT a compute gate, a status-tag reconciliation. PASS = capstone/inventory/memory narrate the Veil at BROKEN/transit-window status, no surface above register status.
   - Effort: 1-2 hours, 1 agent session (orchestrator-direct prose patch + memory edit; mack-bridge for §7 table cell).

V.2. Fold |β_k|² via scattering-potential V(η) with delta-boundary transfer matrix
   - What: Recompute the fold Bogoliubov |β_k|² by mapping the fold a(τ) history onto the effective 1D scattering potential V(η) = (1/4)ȧ² + (1/2)ä·a (Sparn Eq. 4), treating the impulsive switch-on/off as delta-peak boundary discontinuities (ψ_k' → ψ_k' + Ω ψ_k), and reading off |β_k|² = |b_k|²/|c_k|² as a reflection coefficient. Cross-check against the canonical B2-ladder |β_2|² ~ 1.7e3 at k_pivot. Check for Ramsauer-Townsend resonances (Bogoliubov zeros) at predictable k = j·π/Δη.
   - Inputs: fold a(τ) profile (s64_epsilon_profile.npz, s64_sound_speed.npz); k_pivot=14.31 M_KK (S77); dt_transit=1.1302e-3 (get_constant); Sparn 2412.18889 Eqs. 2-5; Schmidt 2406.08094 Eqs. 25, 75-76; B2-ladder |β_2|²≈1.7e3 (S79 P2-A); mode equation v_k'' + (k² − z''/z)v_k = 0.
   - Gate: NEW — FOLD-SCATTERING-BETA-VALIDITY. PASS: V(η)-reformulation |β_k|² agrees with B2-ladder |β_2|² within factor 2 at k_pivot AND transfer-matrix N_seg-convergence holds for the sharp-boundary (delta) case (no OOM drift, unlike the smooth case). INFO: agreement only at OOM level. FAIL: >1 OOM disagreement or N_seg instability persists on sharp boundaries.
   - Effort: 4-6 hours, 1 agent session (ODE solve Radau/RK45 rtol≤1e-10 for reference; transfer-matrix for delta boundaries; convergence scan).

V.3. k_pivot sub-horizon sin[μ_k Δη] closed-form check against N_pivot
   - What: Verify k_pivot sits unambiguously in Schmidt's sub-horizon sin[μ_k Δη] sector (NOT super-horizon sinh[Λ_k Δη]) using k/aH=14.70 at fold, and check whether the zero-energy-resonance horizon condition (k/aH=1) reproduces the canonical N_pivot e-fold count. Confirm consistency with α_s(primordial)=0 EXACT (Bogoliubov saturation, superhorizon plateau).
   - Inputs: Schmidt 2406.08094 Eqs. 75-76 (sinh vs sin); k_pivot/aH=14.70 (S77 INVERSION, s78_f_conv_subhorizon_output.txt); N_pivot=64.08 (get_constant; substrate 55 + ln(c/c_s)=9.08); N=3.12 at pivot horizon exit (S77); Λ_k → i μ_k analytic continuation.
   - Gate: NEW — KPIVOT-SECTOR-CLASSIFICATION. PASS: k_pivot in sin[μ_k Δη] sector by ≥10× margin (k/aH ≫ 1) AND zero-energy-resonance condition reproduces N_pivot horizon-exit within 5%. INFO: sector correct but N_pivot reconstruction off. FAIL: sector ambiguous or sinh-sector indicated.
   - Effort: 2-3 hours, 1 agent session (closed-form evaluation, no heavy ODE).

V.4. Fast-quench universality class of the fold: Rao range-scaling vs Li KZ-survival
   - What: Determine whether the fold's P_exc=1.000 / 59.8-pair saturation is range-controlled (Rao v>v_c, ρ ~ δ_max, rate-independent) or KZ-surviving (Li, iff z' < z + 1/ν). Compute the fold's effective dynamic exponents (z, z') and correlation-length exponent ν at the van Hove fold; evaluate the Li inequality z' < z + 1/ν; test whether the GGE occupation scales with fold spectral-excursion RANGE (δ_max analog) vs transit RATE.
   - Inputs: tau_fold=0.19, Mach=13.75, dt_transit=1.1302e-3 (get_constant); n_pairs=59.8, P_exc=1.000 (atlas T1); van Hove fold spectral profile (s64_epsilon_profile.npz); Rao 2506.06841 (v_c, δ_max scaling); Li 2511.21386 (z'<z+1/ν, r_μ=z+1/ν).
   - Gate: NEW — FOLD-QUENCH-UNIVERSALITY-CLASS. PASS: fold occupation demonstrably range-controlled (rate-independent within 5% across a transit-rate scan), consistent with Rao v>v_c class. INFO: borderline / Li inequality marginally satisfied (KZ-surviving class instead). FAIL: occupation rate-dependent (KZ v<v_c class — contradicts P_exc saturation).
   - Effort: 5-7 hours, 1 agent session (rate-scan of the Bogoliubov occupation; exponent extraction at the fold).

V.5. Localized matter-power feature + sign-keyed HMF oscillation from the fold (small-scale channel)
   - What: Predict the localized matter-power-spectrum feature (amplitude, position) and the sign of the halo-mass-function oscillation imprinted by the fold's spectral excursion, transported through nonlinear evolution per Stahl's surviving-feature result. The van Hove excursion DIRECTION sets the HMF sign — compute it.
   - Inputs: fold spectral-excursion profile (s64_epsilon_profile.npz, van Hove fold direction); frozen-spectrum exactness baseline (Sasaki-Stewart, n_s=1 at CMB); k_pivot=14.31 M_KK; Stahl 2502.02571 (localized P(k) feature + sign-keyed HMF, N-body transfer); GGE interference-pattern structure (post-transit acoustic excitations).
   - Gate: NEW — FOLD-SMALL-SCALE-FEATURE. PASS: framework predicts a localized P(k) feature at a computable k_feature with a definite sign matching the HMF discriminator; feature scale below CMB, above nonlinear-erasure scale. INFO: scale computable but sign degenerate. FAIL: no surviving feature (washed out) or scale outside any observable window.
   - Effort: 4-6 hours, 1 agent session (feature-scale + sign computation; degeneracy assessment vs non-CDM per Stahl caveat).

V.6. ΔN_eff / BBN bound on the substrate-scale blue tilt n_T = +0.468
   - What: Compute the GW radiation-energy contribution (ΔN_eff) of the framework's substrate-scale blue tensor tilt n_T=+0.468 integrated to the BBN frequency band, and check it against the BBN bound (Vagnozzi's T_rh ≲ 10 GeV / ΔN_eff envelope). Confirm the substrate blue tilt does NOT overproduce GW energy density despite being blue.
   - Inputs: n_T transit = +0.468 (S66, session-66-mack-transit-workshop T.38); pivot n_T_PathC_canonical=-0.00146644, n_T_PathH_canonical=-0.000933812 (get_constant); 54-decade transport T_{BZ→pivot}; σ_n_T_LiteBIRD=0.0008; Vagnozzi 2306.16912 (ΔN_eff bound, T_rh≲10 GeV); Ω_GW spectrum constraints.
   - Gate: NEW — BLUE-NT-BBN-BOUND. PASS: ΔN_eff from the substrate blue tilt within the BBN bound (no overproduction) AND consistent with the Gaussian f_NL=O(eps) (no large-NG tension that sinks standard blue inflation). FAIL: ΔN_eff exceeds BBN bound (substrate blue tilt over-produces GW). INFO: bound saturated within factor 2.
   - Effort: 3-4 hours, 1 agent session (Ω_GW integral over the blue spectrum; ΔN_eff conversion; BBN comparison).

V.7. ζ-tail cross-check: framework Gaussianity vs Ahmadi stochastic-δN faster-than-e^{−3ζ}
   - What: Compute the framework's curvature-perturbation ζ tail through the sharp fold transition via an independent (non-Bogoliubov) stochastic-δN-style characteristic-function method, and check it is at least as suppressed as Ahmadi's faster-than-e^{−3ζ} — corroborating the squeezed-vacuum-is-Gaussian (Wick) result against an independent calculation.
   - Inputs: f_NL=O(eps) PERMANENT (S65 W5-D, baseline-findings-s66); max_f_NL_FW=1.505 envelope (get_constant); fold sharp-transition profile; Ahmadi 2207.10578 (characteristic function, faster-than-e^{−3ζ} tail, stochastic-δN through sharp transition); squeezed-vacuum S_fold matrix [[cosh r, e^{iφ} sinh r],[e^{−iφ} sinh r, cosh r]].
   - Gate: NEW — FOLD-ZETA-TAIL-GAUSSIANITY. PASS: framework ζ tail decays ≥ as fast as e^{−3ζ} (consistent with Ahmadi, confirming Gaussian-by-Wick by an independent route). INFO: tail direction consistent but quantitatively different. FAIL: framework ζ tail HEAVIER than e^{−3ζ} (would contradict f_NL=O(eps)).
   - Effort: 4-5 hours, 1 agent session (characteristic-function / stochastic-δN computation through the fold).

V.8. Non-log-periodic S_k(t) signature: framework impulsive transit vs Xue coasting analog
   - What: Compute the framework's time-averaged density-fluctuation power spectrum S_k(t) = 1/2 + N_k − A_k cos(2ω_k^f t + θ_f) signature for the impulsive fold and confirm it is NON-log-periodic in expansion ratio (no scale invariance through the fold), distinguishing it from Xue's coasting-case log-periodic N_k = sin²(√|B| ln(t_f/t_i))/(4|B|). Map the framework's k_pivot subhorizon classification onto Xue's kl=1/2 boundary.
   - Inputs: k_pivot/aH=14.70 SUBHORIZON (S77); Mach=13.75 (impulsive, non-scale-invariant); N_k=|β_k|² with |α|²−|β|²=1; Xue 2603.16095 (SU(1,1), Bargmann index (1±√B)/2, kl=1/2 boundary, log-periodic vs sinh); Sakharov-oscillation S_k(t) structure (papers 02/03).
   - Gate: NEW — FOLD-SK-LOGPERIODICITY-DISCRIMINATOR. PASS: framework S_k(t) provably NON-log-periodic (no SU(1,1) scale invariance), distinguishable from the coasting log-periodic signature. INFO: distinguishable only at high expansion ratio. FAIL: framework inadvertently log-periodic (would imply hidden scale invariance through the fold).
   - Effort: 3-4 hours, 1 agent session (S_k(t) closed form; scale-invariance check; comparison to Xue closed forms).

V.9. F_amp^sc=47.92 validation vs energy-conserving Bogoliubov growth (Gondret template)
   - What: Validate the framework's F_amp^sc=47.92 (3PI NLO 1/N closure) against an energy-conserving Bogoliubov accounting in the style of Gondret's measured Faraday growth rate + ⟨b_k b_{−k}⟩ anomalous correlation, confirming the impulsive (non-parametric-resonant) amplification reproduces the two-mode-squeezed pair growth without the energy-conservation violation of the linearized F_amp=6858 (ρ_p/ρ_bg~2e4).
   - Inputs: F_amp^sc=47.92 (S82 W3-5, 3PI NLO 1/N; matches S78 bound to 0.0024%); linearized F_amp=6858 (energy-conservation-violating, my memory); switch-off-rate sensitivity (Gondret); Gondret-parametric 2508.01654 (Bogoliubov growth rate, ⟨b_k b_{−k}⟩); Viermann 2202.10399 S_k(t)=[1/2+|β|²+|αβ|cos]·(1+2N^in).
   - Gate: feeds CF22 (F_amp 3PI-vs-slot adjudication); NEW sub-gate FAMP-ENERGY-CONSERVING-VALIDITY. PASS: F_amp^sc=47.92 reproduces the ⟨b_k b_{−k}⟩ anomalous-correlation growth with ρ_p/ρ_bg < 1 (energy-conserving). INFO: energy-conserving but F_amp off by factor 2. FAIL: energy non-conservation persists at F_amp^sc.
   - Effort: 4-6 hours, 1 agent session (anomalous-correlation growth computation; energy-budget check; switch-off-rate scan).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | V(η)=(1/4)ȧ²+(1/2)ä·a scattering reformulation (Sparn/Schmidt 03/04) maps z''/z; transfer-matrix VALID for sudden/sharp limit | PHONONIC | Method reopened for fold | Recompute fold \|β_k\|² via delta-boundary transfer matrix (V.2) |
| 2 | Switch-on/off-dominance theorem (Parra-López 07) — transitions dominate, from in/out Bogoliubov | PHONONIC | Independent corroboration of transit paradigm | Transit-IS-physics (atlas-10 #8) confirmed by independent route |
| 3 | Fold occupies range-controlled fast-quench class (Rao 08); KZ-survival (Li 13) is adjacent warrant | PHONONIC | New gate (untested) | P_exc=1.000 saturation likely Rao v>v_c class (V.4) |
| 4 | "GGE never thermalizes" = BROKEN/RETRACTED (S39); thermalization CONCORDANT with Gondret (05), not control case | PHONONIC / **CONFLICT** | Index inverts canonical | Reconcile capstone/memory to transit-window status (V.1) |
| 5 | Langen GGE tomography (12): anti-diagonal peak, ~10 Lagrange multipliers, 10th-order correlations | PHONONIC | Protocol intact (transit-window test) | Test GGE-as-prethermal-plateau during transit |
| 6 | Stahl (09): impulsive-source features SURVIVE nonlinearity (localized P(k) + sign-keyed HMF) | PHONONIC | New observable channel | Small-scale fold signature below CMB (V.5); addresses K_pivot gap (atlas-04 C2) |
| 7 | n_T transit = +0.468 (S66); INACCESSIBLE at pivot (S84 PASS, EVOI=0); Vagnozzi (11) bounds | PHONONIC / index drift | Canonical (focus +0.4676/−3e-3 are drift) | ΔN_eff/BBN bound on substrate blue tilt (V.6) |
| 8 | Ahmadi (10): ζ tail faster than e^{−3ζ} — concordant with f_NL=O(eps) Gaussian-by-Wick | PHONONIC | Direction confirmed | Independent diffusion-tail cross-check (V.7) |
| 9 | Xue (01): coasting log-periodicity is a DISCRIMINATOR vs impulsive (non-scale-invariant) fold | PHONONIC | Falsifiable analog test | Non-log-periodic S_k(t) signature (V.8) |
| 10 | Viermann/Gondret-parametric (02/06): heterodyne S_k(t) + growth-rate protocols; F_amp^sc=47.92 energy-conserving | PHONONIC | Validation template | F_amp vs energy-conserving Bogoliubov (V.9) |

---

**Provenance note**: All framework-state claims anchored to the knowledge MCP (queried 2026-06-04). Flagged drifts from the index/focus-prompt: (a) GGE "never thermalizes" → canonical BROKEN/RETRACTED (S39); (b) n_T transit +0.4676 → canonical +0.468 (S66); (c) pivot n_T "~−3e-3" → canonical −1.46644e-3 (PathC) / −0.933812e-3 (PathH); (d) the index frames Gondret/Langen as control cases the framework must avoid → canonical makes post-transit thermalization concordant. No registry edits or computations performed in this synthesis (literature adjudication only).
