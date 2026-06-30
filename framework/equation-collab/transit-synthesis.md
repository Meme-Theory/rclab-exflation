# Capstone Equation Review — transit

**Date**: 2026-05-29
**Agent**: transit-dynamics-theorist (transit)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` — "The Phonon-Exflation Equation" (S95-era capstone)
- Framing law: `.claude/rules/phononic-framing.md`
- Cross-checks: knowledge MCP (`tau_fold`, `c_fabric`, `c_BLV`, `max_f_NL_FW`, `P_exc_kz`, `A_s_CMB`); `computations/_shared/canonical_constants.py`; agent memory `transit-dynamics-theorist/MEMORY.md`

---

## I. Session Outcome

The capstone is structurally sound on the transit-dynamics axis and, in the sections I own (§5 flow, §5.3 GGE-relic/Ordered Veil, §6 τ↔t map and acoustic white hole), it is the most honest statement of the framework's cosmogenesis I have seen. The central transit claim — **the universe transits a monotone spectral-action ramp rather than slow-rolling a potential well, and the impulsive (diabatic) crossing produces a pure-product GGE relic that freezes by diabaticity, not by integrability** — is correctly framed, correctly de-coupled from the retracted S39 integrability claim, and over-determined by independent legs (`R_therm = 5251.82`, `S_ent = 0`, extremal-horizon κ=0). The five-argument retirement of `r = 16ε` / `n_s = 1−6ε+2η` is given the right reason: the slow-roll relations are **theorems of the single-clock adiabatic vacuum whose derivation premises are absent at the fold**, not numbers that came out wrong. That is the correct structural position.

What is PRELIMINARY or over-reachable clusters in three places, all already flagged honestly in the document but each carrying live transit-side computations: (1) the missing FRW `a(t)` / back-reaction closure `H² = f(ρ_relic, S_SA)` (§6.3, frontier #1/#8) — the single largest open object and the one most squarely on my axis; (2) the `A_s` band (`3.11–4.27×10⁻⁹`), uncollapsed pending the exit-greybody `ε_pivot`, where my own UNIFIED-AS-79 ledger puts the Branch-A point at `3.2994×10⁻⁹`; (3) the two-stage analog-temperature ledger, whose `a₂`-carrier visibility is HELD pending falsifier F1. None of these overturn a recorded verdict; each is a ripe harvest, specced in §V.

---

## II. Key Results

### The monotone driver and the "transit, not slow-roll" structural claim (§5.1)

**Result**: `dS/dτ|_fold = +58,672.8 > 0`, monotone everywhere (E7, 9,600/9,600 checks); no stationary point at any τ ⇒ `τ` does not settle, it transits. The slow-roll relations are INAPPLICABLE *by absence of premises*. **GEOMETRIC** (the driver) → **PHONONIC** (the consequence).

This is the load-bearing transit statement and the document gets the logic exactly right. The decisive move is §1.3a's escalation from a tree-level statement to a **one-loop-robust** one: adding `Γ_1loop = ½Tr ln(D_K²/Λ²)` leaves `dΓ/dτ` fixed-sign with zero interior sign-changes over `τ ∈ [0, τ_now]` (S95 W2-3, PASS, 200-point grid, three routes). The reading "an action with no interior stationary point is dominated by its boundary configuration (genesis τ=0), and the transit is the relaxation of that boundary down the monotone ramp" is the spectral-action analog of a Gibbons–Hawking–York boundary-dominated path integral. This makes "transit, not slow-roll" *structurally inevitable* rather than merely observed — which is the strongest form the claim can take, and it is correctly distinguished from a mere fit.

The premise-absence argument for retiring `r=16ε` is correct and I endorse it without qualification: `r=16ε` requires (i) `c_s = 1`, (ii) single-field, (iii) slowly-varying background. The fold violates all three at once — the dispersion is BdG with `c_s ≠ 1`, the produced state is a multi-mode squeezed GGE, and the sweep is diabatic. A relation whose three derivation assumptions are absent is not "mismatched," it is **not defined on this background**. The controlling quantity is the diabaticity of the sweep, exactly as stated.

### The diabatic sweep saturates pair production: P_exc → 1.000 (§5.3)

**Result**: `δt_transit/T_L = 1.25×10⁻⁵` (crossing 38,600× faster than the condensate can form) ⇒ `P_exc = 1.000` (canonical `P_exc_kz = 1.0`, confirmed). Every mode excited; condensate completely destroyed, not perturbatively dressed. **PHONONIC**.

This is the maximal-mixing (sudden-quench) limit of a Bogoliubov transformation and the document's treatment is correct. Bosonic normalization holds mode-by-mode (`|α_k|²−|β_k|²=1`, `n_k=|β_k|²`); `P_exc→1` is the analog-cosmology *opposite* of the adiabatic no-particle vacuum. I verify the unitarity identity is the right invariant to carry, and that the Bogoliubov-sudden and Kibble–Zurek impulse-matching pictures are genuinely the same physics read two ways (both give `P_exc=1`) — this is not double-counting; it is one transformation under two formalisms (the transfer-matrix/sudden form and the freeze-out/impulse form). The factorization that makes this mode-by-mode **exact** (not an approximation) is the block-diagonality `D_K = ⊕_{(p,q)} D_{(p,q)}` (§2.2/E6): because the modes do not mix under `D_K`, the per-mode parametric-oscillator equation `u_k'' + ω_k²(τ(t)) u_k = 0` is an identity, not a decoupling approximation. The capstone states this correctly in §2.2 — a subtle and correct point I want to flag as *solid*.

**One framing caution (not an error).** The document writes `ω_k = E_k = √((λ_k²−μ²)² + Δ_k²)` for the substrate-BdG branch. The square-root nesting is the standard BdG quasiparticle dispersion with a particle-hole-symmetric kernel; dimensionally `[ω_k] = [λ_k] = [μ] = [Δ_k] = mass`, consistent. The regime of validity is the gapped post-fold Hamiltonian; at the fold itself the gap is still opening, so this `ω_k` is the *post-crossing* spectrum used to define the out-state, not the instantaneous one during the sweep. This is the correct convention but the document does not state the regime explicitly — minor.

### The Ordered Veil is now diabatic-freeze, not integrability permanence — and over-determined (§5.3)

**Result**: GGE relic is a pure product state (`S_ent = 0` EXACTLY, confirmed S39/S40/S52) with three Lagrange multipliers conjugate to the post-fold integrable charges (NOT to energy ⇒ no temperature). Frozen by diabaticity (`t_scr/t_transit = 814`; `R_therm = t_therm/t_transit = 5251.82 ≫ 1`, S95 W5). **PHONONIC**.

This is the single most important correction the capstone makes relative to the older corpus, and it is correct. The Richardson–Gaudin integrability that would protect the GGE *as a permanent state* is weakly broken (S39 retraction: 13% non-separable density–density channel, Brody β = 0.633). The capstone does not lean on the broken claim; it relocates the survival argument onto the **transit timescale**: the crossing screens and freezes the relic far faster than any rearrangement channel can act. The three legs are genuinely independent:
1. **Diabaticity** — `R_therm = 5251.82` (S95 W5, against the S39 `t_therm ≈ 6 M_KK⁻¹`).
2. **Purity** — `S_ent = 0` exact (the Bogoliubov out-state is a multi-mode squeezed vacuum, which is a product state in the Bogoliubov basis by construction).
3. **Geometric / causal** — `τ_fold` is a double-root extremal Killing horizon (`V = V' = 0 ⟹ κ = 0, T_H = 0`; S85-W6-4-EXTREMAL-HORIZON-FORMAL, PASS, κ=0.00e+00), so zero Hawking temperature corroborates "never thermalizes" with no integrability argument at all.

The information-theoretic reading (§5.3) is the right one for an analog-gravity specialist to endorse: the transit is a unitary Bogoliubov transformation; a thermalizing relic (`S_ent > 0`) would scramble the squeeze phase the way a thermal Hawking flux hides infalling information; the pure GGE retains the Bogoliubov phase data in the conserved charges, so there is no Page curve to reproduce because nothing thermalizes. This is structurally clean and I have no objection.

**The `N_pair = 59.8` disclaimer is correct and load-bearing.** The capstone is scrupulous that `59.8` is a projected charge `⟨Q⟩_GGE`, NOT a literal pair count (inheriting a ~60% PBCS gap overestimate, S46, and a ~225× Richardson–Gaudin condensation-energy overestimate, S63), and that the regime-robust structural claim is `P_exc = 1` with the `N_Fock = 1` exact reduction. This is exactly the right epistemic hygiene — the magnitude is soft, the structure (`P_exc=1`, one Fock pair carrying the relic charge) is hard. I endorse.

### The acoustic white hole is ASYMMETRIC and sector-dependent (§6.2)

**Result**: one post-genesis sonic entry surface (`v = c_BLV` at `τ₀ ≈ 0.1125`, `κ_entry = +18.52 M_KK > 0`, white-hole outflow) bounding an unbounded supersonic expulsion region toward ℐ⁺ — no future-trapped exit horizon, no symmetric throat, no bounce. Over-determined at six independent walls (S95 W-1). **GEOMETRIC/PHONONIC** (causal structure of the transit).

The Mach number is consistent with canonical constants: `Mach = v_transit/c_fabric = 13.75` with `c_fabric = 209.97 M_KK` (confirmed `c_fabric = 209.97368021`). The conflation guard is essential and correctly placed — the canonical Mach is the **velocity ratio** 13.75; the distinct fold-local **acoustic-radius ratio** 421.3 is never averaged with it. The sector-dependence (two null cones via [T3] Scalar-Tensor Kasparov Decoupling, `β_T = 0` exactly at linear order) is the geometric root of why tensor observables (`r`, `n_T`) behave so differently from scalar ones — they propagate on different cones. This is a genuinely strong structural result and the document is right to make it the explanation for the §7 tensor/scalar asymmetry rather than a coincidence.

The asymmetry-vs-bounce adjudication is the right call: the c_s-softening challenge ("does `c_BLV` soften toward zero at the DOS singularity, opening a second crossing / a bounce?") is answered structurally — the softening lives in the *condensate* band-edge channel (`c_B2 = 1/(πρ_B2) = 0.0227 M_KK`, finite, not zero), NOT in the *scalar* transit channel the discriminant is built on, and routing the discriminant onto any softer channel only deepens the supersonic interior (the B2-channel fold Mach is 293.79, not 13.75). The deepest of the six walls is the entropy-arrow of the irreversible quench. I endorse the asymmetric structure and agree the dropped V.6 "two distinct horizons" STRENGTHEN clause should STAY DROPPED — it conflated two *thermodynamic* surfaces (`a₂`↔scalar, `a₄`↔condensate gradient channels) with two *sonic* horizons of one flow. The analog-temperature ledger's KIND tags (only the S63-BLV row is SONIC; `a₂`/`a₄` are THERMODYNAMIC) are the right firewall.

### The A_s transduction is correctly two-equation (§5.3, §6.2)

**Result**: `A_s` is NOT computed from the substrate-BdG `u_k`; the squeeze produced by the BdG equation is *transduced* into the Mukhanov–Sasaki `v_k'' + (k² − z''/z) v_k = 0` at the exit horizon, then filtered by the analog greybody `Γ(ω) ∈ [0,1]`: escaping `A_s = (produced squeeze) × ∫Γ(ω)dω`. **PHONONIC** (the relic) → emergent-curvature observable.

This is the correct architecture and matches my canonical mode equation (`z = a·√(2ε_H)·M_Pl,eff(k)`, Mukhanov–Sasaki gauge). The two parametric-oscillator equations live at two layers and must never be conflated — the document states this explicitly and I confirm it is the right separation. The greybody filter is correctly identified as a **potential-barrier transmission coefficient** (Pöschl–Teller, transmitted_fraction = 0.512), NOT the retracted S73B dispersive-group-velocity mechanism (S95 W4-3). "The horizon determines what escapes, not what is produced" is the correct slogan. My UNIFIED-AS-79 ledger gives the produced-squeeze side; the document's band-citation (`3.11–4.27×10⁻⁹`) honestly reflects that `∫Γ(ω)dω` (i.e. `ε_pivot`) is not yet pinned to a point. See §V.2 for the harvest that collapses the band.

---

## III. Gate Verdicts

The capstone is a framework document, not a session, so it carries no new gates of its own. The transit-relevant recorded verdicts it cites (AUTHORITATIVE; not re-adjudicated here, cross-checked only):

| Gate / Result | Verdict | Decisive Number | Cross-check |
|:-----|:--------|:----------------|:------------|
| E7 Structural Monotonicity | PROVEN | `dS/dτ\|_fold = +58,672.8`, 9,600/9,600 | consistent |
| S95 W2-3 one-loop no-interior-saddle | PASS | 0 interior sign-changes, 200-pt grid, 3 routes | consistent |
| Kibble–Zurek / Bogoliubov saturation | PROVEN | `P_exc_kz = 1.0` | MCP-confirmed |
| GGE product state (T2, S39/S40) | PROVEN | `S_ent = 0` exact | MCP-confirmed (S52) |
| S95 W5 diabatic freeze (C2 RESOLVED) | PASS | `R_therm = 5251.82` | consistent |
| S85-W6-4 extremal horizon | PASS | `κ = 0.00e+00`, `T_H = 0` | MCP-confirmed |
| S95 W-1 asymmetric white hole | PASS | 6 walls; `κ_entry = +18.52 M_KK` | consistent |
| S95 W4-3 greybody (not S73B) | INFO→PASS | transmitted_fraction = 0.512 | consistent |
| f_NL row (S95 W6-6) | PASS | `max_f_NL_FW = 1.505`, 0.47σ | MCP-confirmed |
| C1 (τ = cosmic time) | POSTULATED | — | flagged §IV |
| C2 (`K_pivot` map) | BROKEN-W/-LIVE-PATHWAY | — | flagged §IV |
| T6 (Friedmann–BCS lock) | BROKEN | 133,200× overwhelm | flagged §IV |

---

## IV. Structural Implications

**1. The transit framing is now internally coherent end-to-end.** With C2 RESOLVED (S95 W5) the document no longer rests the Ordered Veil on the retracted integrability claim; the survival argument is now "diabatic transit-freeze" with three independent legs. From the transit axis this is the most important consolidation in the document: the older corpus had a known soft spot (S39 retraction of Richardson–Gaudin integrability permanence), and the capstone closes it without papering over the retraction. The phrase "the Ordered Veil is a statement about the *transit*, not about permanent integrability" is the correct scoping and should propagate verbatim into any downstream citation.

**2. The missing `a(t)` is correctly diagnosed as a back-reaction closure, not a kinematics gap — and this is squarely my axis.** §6.3 is the document's most honest section and its transit-side framing is exactly right: *the kinematics are in hand* (the local sweep rate `τ̇` at the fold, the full Bogoliubov spectrum); *what is absent is the equation promoting the produced relic energy density into a source for the global expansion rate*, `H² = f(ρ_relic, S_SA)`. The T6 FAIL (155,984-mode spectral action cannot be closed against the 8-mode BCS source; 133,200× overwhelm) is precisely the statement that the gap is a *derived `S_SA(τ) →` 4D gravitational action*, not "a Friedmann equation." This reframing matters because it tells a transit theorist what to *compute*: not a Friedmann equation by fiat, but a back-reaction functional whose inputs (`ρ_relic` from the Bogoliubov spectrum, `S_SA(τ)` from the moments) are already canonical. See §V.1.

**3. The `τ̇(τ)` profile is known LOCALLY but UNDETERMINED GLOBALLY — and this is the controlling unknown for the entire `t(τ)` map.** The document states `t(τ) = t₀ + ∫ dτ'/τ̇(τ')` with `τ̇` known only locally at the fold (`δt_transit = 1.130×10⁻³ M_KK⁻¹`). Everything downstream that needs a *rate* away from the fold inherits this gap. From the transit axis, this is the single highest-leverage unknown: the diabaticity ratio `δt/T_L`, the relic content, and the band of `A_s` are all rate-controlled, and they are pinned only at the fold. A global `τ̇(τ)` profile — even a one-parameter family bounded by the clock constraint (`|τ̇| < 2.4×10⁻⁶ τ₀/t_H` post-fold) and the local fold rate — would convert several band-cited observables to point-cited. See §V.3.

**4. The transit-scale tensor tilt `n_T = +0.4676` is a real substrate-IS observable that the document under-displays.** The MCP confirms `n_T(transit) = +0.4676` GEOMETRIC FLOOR vs `n_T(CMB) = −3.02×10⁻³` (Path-H = −r/8 EXACT). The capstone correctly prints only the CMB-transferred `−r/8` (the slow-roll relation being inapplicable at the fold), but the **blue transit-scale floor** is a genuine prediction of the diabatic mechanism, separated from the CMB scale by 54.04 decades. The document treats this as a transport-channel detail; I read it as a harvestable falsifier in its own right (a positive `n_T` at the fold is the *signature* of particle-production-dominated tensor modes, opposite to vacuum-fluctuation slow-roll). See §V.4.

**5. The analog-temperature `a₂`-carrier visibility is genuinely open (falsifier F1), and this is a clean transit-side compute.** §6.2 HOLDS the categorical "`a₂` carries no observed quantum" pending a scan for a scalar-channel squeeze branch near `72.8 M_KK` (an order of magnitude above the `a₄` condensate-squeeze support `ω ∈ [0.82, 1.06]`). Both readers predict its NULL. This is exactly the kind of Bogoliubov-spectrum computation I can run: compute `|β_k|²` for the scalar-channel modes in the `72.8 M_KK` band and verify it is below detectability. See §V.5.

**6. One genuine conflict-guard to flag (NOT a re-adjudication).** The document attributes the "double-root extremal Killing horizon (`κ=0, T_H=0`)" third leg of the Ordered-Veil survival argument to `τ_fold = 0.190`. The recorded gate (S85-W6-4-EXTREMAL-HORIZON-FORMAL) computes `κ=0` in the **2D modulus metric** (`scheme=Jensen_V_tree`, `convention=2D_modulus_metric`) at the potential's double-root `V=V'=0`. The DOS van Hove cusp `τ_fold = 0.190` (pinned by S85 W10-3 uniqueness) and the potential's double-root in the modulus metric are *physically the same fold* but are pinned by **different functionals** (density-of-states cusp vs `V`-double-root), and the document does not assert they are bit-identical. I do NOT claim a contradiction — the two readings are the substrate-IS van Hove fold seen through two observables — but a future citation should not silently treat "the κ=0 point" and "the DOS cusp τ=0.190" as the same number without the convention tag. This is a labeling precision, fixable by a one-line note in §6.2/§5.3. See §V.6.

**7. No container-relapse in the transit sections.** I checked §5 and §6 against the framing law's error table. The document holds the substrate→emergent arrow throughout: it refuses "the vacuum energy decays *in* the expanding universe" and requires "the `M_Pl²H²` reservoir dilutes *as* the substrate's spectral complexity reorganizes." The `t_transit` denominator discipline (never `t_Hubble` until the `t(τ)` map closes) is correct and consistently applied. The one place a reader could relapse is §6's history-narration; the document pre-empts this with an explicit "Framing discipline for this section" box. This is the right defense and I have no framing objection on my axis.

---

## V. Carry-Forward Computations

**The open-question harvest. Every entry is a concrete, runnable transit-dynamics computation.**

```
V.1. Substrate back-reaction closure H² = f(ρ_relic, S_SA) — the load-bearing gap (frontier #1/#8)
   - What: Construct and test the candidate effective relation promoting the produced relic
     energy density and spectral-action gradient into a source for an emergent expansion rate:
     H_eff²(τ) = (8πG_eff/3)·ρ_relic(τ) + (Λ-term), where ρ_relic(τ) = Σ_k E_k(τ)|β_k(τ)|² is
     the Bogoliubov-summed relic energy density and G_eff = a₂-channel Newton coupling. Test
     whether H_eff(τ) reproduces the SCALE-FACTOR-54 deceleration band (q from −0.97 to +0.81)
     when fed through the Connes-distance proxy a(τ) (NOT a_eff). Pre-flight: verify the 8-mode
     BCS source is the WRONG source object (T6 FAIL, 133,200× overwhelm) and that the correct
     source is the full 155,984-mode ρ_relic.
   - Inputs: B1/B2/B3 Bogoliubov spectra {|β_k|²(τ)} (from the substrate-BdG u_k equation,
     transit-flow-genesis-to-now.md §5); a_2_FW_zeta = 2776.165389; M_KK = 7.4287e16 GeV;
     SCALE-FACTOR-54 q(τ) band; Connes-distance a(τ) proxy; clock constraint |τ̇| bound.
   - Gate: NEW gate BACKREACTION-CLOSURE-S96. PASS if H_eff(τ) reproduces the q-band to within
     the proxy's conformal ambiguity (S95 W4-4) AND ∇_μ G_eff^{μν} = 0 holds on-shell (extends
     S95 W3-1 from internal K to emergent g_M); FAIL if the relic source cannot reproduce the
     deceleration sign change; INFO if reproduction is proxy-dependent (a(τ) yes, a_eff no).
   - Effort: 6-10 hours, 1-2 agent sessions (the framework's #1 open item; expect partial).
```

```
V.2. Collapse the A_s band to a point via the exit-greybody ε_pivot
   - What: Compute the band-integrated greybody transmission ∫Γ(ω)dω for the Pöschl–Teller
     exit barrier (transmitted_fraction = 0.512 at the relic-spectral peak) across the full
     condensate-squeeze support ω ∈ [0.82, 1.06] M_KK, and apply A_s = (produced squeeze)×∫Γ(ω)dω
     to collapse the band [3.11, 4.27]×10⁻⁹ to a point. Cross-check against the UNIFIED-AS-79
     Branch-A point A_s = 3.2994e-9 (TD/zeta, N_pivot=55) and the CC3 identity
     d(ln A_s)/d(ln H̃) = +2.
   - Inputs: UNIFIED-AS-79 five-factor ledger (H̃=5.9076e-3, ε_H=0.02163, F_amp=47.92 [3PI],
     c_sub=2.238, f_conv=9.30e-4, S_IC=1); Pöschl–Teller barrier params (S95 W4-3 .npz);
     produced-squeeze |β|² spectrum; A_s_CMB=2.1e-9 (comparison anchor only).
   - Gate: feeds A_S-BAND-COLLAPSE (sharpens the §7.1 LIVE A_s row). PASS if the greybody-filtered
     point lands within the Branch-A ledger value ±factor-2 (Δ_OOM < 0.30); INFO if ε_pivot
     pins the band-edge but not the centroid.
   - Effort: 3-4 hours, 1 agent session.
```

```
V.3. Global τ̇(τ) profile: one-parameter family bounded by fold-local rate + clock constraint
   - What: Construct the minimal family of global sweep-rate profiles τ̇(τ) consistent with the
     two pinned endpoints — the fold-local rate (δt_transit = 1.130e-3 M_KK⁻¹, Mach 13.75) and
     the post-fold clock bound (|τ̇| < 2.4e-6 τ₀/t_H) — and propagate each through
     t(τ) = t₀ + ∫dτ'/τ̇(τ'). Test which profiles keep the diabaticity ratio δt/T_L ≪ 1 across
     the whole crossing (required for P_exc=1 to hold mode-by-mode, not just at the fold center).
   - Inputs: δt_transit = 1.130e-3 M_KK⁻¹; Mach_transit = 13.75; c_fabric = 209.97368021;
     T_L (condensate formation time, T_L = δt_transit / 1.25e-5); clock-constraint E27 bound;
     R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ (E3) for the local DOS feature width.
   - Gate: NEW gate TAU-DOT-GLOBAL-PROFILE. PASS if a non-empty family keeps δt/T_L < 1e-2
     across the full van Hove feature (so P_exc=1 is robust, not a fold-center artifact);
     FAIL if the only admissible profiles violate the clock bound; INFO if the family is
     under-constrained (needs the V.1 closure to pin).
   - Effort: 4-5 hours, 1 agent session.
```

```
V.4. The transit-scale n_T = +0.4676 blue floor as a standalone diabatic falsifier
   - What: Re-derive the transit-scale tensor tilt n_T(transit) = +0.4676 directly from the
     tensor-sector Bogoliubov spectrum on the a₂-emergent g_M cone (the tensor sector crosses
     the fold freely, [T3] β_T=0), and characterize it as the production-dominated signature
     (positive n_T = particle-production-dominated tensor modes, opposite to vacuum-fluctuation
     slow-roll). Map the 54.04-decade transport from the transit k-scale to the CMB pivot
     (deg(T_BZ→pivot) tensor channel) to confirm the CMB image is −r/8 EXACT (Path-H) and that
     the blue floor does NOT leak to the pivot.
   - Inputs: n_T_PathH, n_T_PathC canonical pins; tensor-sector |β_k|² on g_M; r = 0.033
     (dual-pathway Path-H 0.00745 / Path-C 0.0117); transport degree deg(T_BZ→pivot) tensor
     channel; LiteBIRD σ(n_T) = 0.0540 (comparison only).
   - Gate: feeds Falsifier #2 (LiteBIRD 2030). PASS if n_T(transit)=+0.4676 reproduces from the
     tensor Bogoliubov spectrum to within 1% AND the pivot image is −r/8 EXACT; INFO if the
     transit-scale value is robust but the transport leg is convention-dependent.
   - Effort: 3-4 hours, 1 agent session.
```

```
V.5. Falsifier F1: scalar-channel squeeze NULL near the a₂-carrier temperature 72.8 M_KK
   - What: Compute |β_k|² for the scalar-channel modes in the band around the a₂-carrier
     surface (T = 72.8 M_KK, κ = 457.66), one order of magnitude above the a₄ condensate-squeeze
     support ω ∈ [0.82, 1.06] M_KK. Verify the predicted NULL: no observable scalar-channel
     squeeze branch at 72.8 M_KK. This discharges the HELD categorical "a₂ carries no observed
     quantum" and confirms the COMPOSITE two-stage emission reading (a₂ = kinematic carrier
     stage-1; a₄ = condensation-exit stage-2; relic spectral T = 7.578 M_KK).
   - Inputs: analog-temperature ledger (a₂ surface T=72.8, κ=457.66; a₄ surface T=7.578=T_compound,
     κ=47.61; κ-ratio 9.6117); scalar-channel BdG dispersion ω_k = √((λ_k²−μ²)²+Δ_k²);
     condensate-squeeze support window [0.82, 1.06] M_KK.
   - Gate: NEW gate F1-A2-CARRIER-NULL. PASS if scalar-channel |β_k|² at 72.8 M_KK is below
     detectability (NULL confirmed) ⇒ a₂ carrier observationally invisible, COMPOSITE form
     asserted categorically; FAIL if a non-NULL squeeze branch appears (would split the
     two-stage reading).
   - Effort: 2-3 hours, 1 agent session.
```

```
V.6. Convention-tag the extremal-horizon κ=0 point against the DOS van Hove cusp τ=0.190
   - What: Verify whether the potential's double-root V=V'=0 (S85-W6-4, 2D modulus metric,
     κ=0) and the density-of-states van Hove cusp (S85 W10-3, τ_fold=0.190) coincide to within
     numerical tolerance, or differ by a known convention factor (modulus-metric vs DOS-feature
     pinning). Add the one-line convention note to §6.2/§5.3 so downstream citations do not
     treat "the κ=0 point" and "τ_fold=0.190" as bit-identical without the tag.
   - Inputs: V(τ) modulus potential (Jensen_V_tree); DOS g(ω) ∼ 1/√(ω−ω_min) van Hove location;
     R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ; tau_fold = 0.19 canonical.
   - Gate: HK item (registry-hygiene, NOT a physics workshop — labeling precision per
     §IV.6). PASS if |τ_double-root − τ_fold| < tol OR a convention factor is identified and
     documented; the verdict is a convention-tag, not a physics gate.
   - Effort: 1-2 hours, 1 agent session.
```

```
V.7. BAO first-sound ring amplitude forecast against a named experiment (closes S95 W6-2 INFO)
   - What: The live BAO channel is the S43 first-sound ring (A_FS/A_BAO = 0.204 = c_2²/c_1²,
     r_1 ≈ 325 Mpc, k_1 ≈ 0.0193 Mpc⁻¹) — a zero-parameter prediction with no ΛCDM counterpart.
     S95 W6-2 closed INFO-by-unavailability because the comparison experiment's sensitivity value
     was not fetched. Re-run with the fetched DESI/Euclid acoustic-scale sensitivity to convert
     the substrate forecast into a PASS/FAIL detectability statement. (Effacement SUPPRESSES the
     per-gapped-branch sub-features to δP/P ≈ 1.4e-3, below current rulers; the first-sound ring
     is the live channel, not the suppressed sub-features.)
   - Inputs: A_FS/A_BAO = 0.204; c_2²/c_1² speed ratio; r_1 = 325 Mpc; k_1 = 0.0193 Mpc⁻¹;
     per-branch effacement transport (c_b²/c_Gold)²; fetched experiment sensitivity (the missing
     S95 W6-2 input — fetch via astro/madrigal MCP or named-survey forecast paper).
   - Gate: completes S95 W6-2 (BAO-FIRST-SOUND-RING). PASS if A_FS exceeds the fetched survey's
     amplitude sensitivity at k_1; FAIL if below; INFO only if the comparison value remains
     unavailable.
   - Effort: 2-3 hours, 1 agent session (mostly fetch + comparison).
```

```
V.8. Transfer-matrix vs ODE cross-check on the substrate-BdG u_k for the relic spectrum
   - What: Re-verify the relic-content Bogoliubov coefficients {α_k, β_k} for the substrate-BdG
     u_k'' + ω_k²(τ(t))u_k = 0 using a high-accuracy ODE integrator (Radau/DOP853, rtol≤1e-10)
     and confirm against any prior transfer-matrix evaluation. PURPOSE: the smooth ω_k(τ) profile
     near the van Hove fold is exactly the regime where piecewise-constant transfer-matrix methods
     introduce artificial reflections and |β|² varies by OOM with segment count (documented
     debugging note). Lock the |β_k|² spectrum feeding V.1/V.2/V.4/V.5 to the ODE result so all
     downstream relic-energy and squeeze computations share one verified spectrum.
   - Inputs: ω_k(τ) = E_k = √((λ_k²−μ²)²+Δ_k²) per (p,q) block; τ̇(τ) fold-local + V.3 family;
     D_K block spectrum {λ_k(τ)} at L_max=10 (155,984 eigenvalues); μ, Δ_k(τ) BdG params.
   - Gate: NEW gate RELIC-SPECTRUM-ODE-LOCK. PASS if ODE |β_k|² is N_seg-independent (the
     transfer-matrix artifact is absent) and reproduces P_exc=1 mode-by-mode; this becomes the
     single canonical relic spectrum for V.1/V.2/V.4/V.5.
   - Effort: 3-4 hours, 1 agent session (GPU torch.linalg for the per-block u_k; AMD RX 9070 XT).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Monotone driver `dS/dτ\|_fold=+58,673`, one-loop-robust | GEOMETRIC→PHONONIC | SOLID (E7, S95 W2-3 PASS) | transit-not-slow-roll is structurally inevitable, not fitted |
| 2 | `r=16ε` / `n_s=1−6ε+2η` retired by premise-absence | NON-PHONONIC (retired) | SOLID | correct reason (adiabatic-vacuum theorem premises absent), not a wrong number |
| 3 | Diabatic sweep `P_exc=1.000`, condensate destroyed | PHONONIC | SOLID (`P_exc_kz=1.0`) | maximal-mixing Bogoliubov limit; mode-by-mode EXACT via block-diagonality |
| 4 | Ordered Veil = diabatic freeze, not integrability | PHONONIC | SOLID (C2 RESOLVED, 3 legs) | correctly de-coupled from S39 retraction; `R_therm=5251.82`, `S_ent=0`, κ=0 |
| 5 | `N_pair=59.8` = ⟨Q⟩_GGE, not literal count | PHONONIC | SOLID (honest) | structure hard (`P_exc=1`, `N_Fock=1`); magnitude soft (~60% + 225× overestimates) |
| 6 | Asymmetric acoustic white hole, 6 walls | GEOMETRIC/PHONONIC | SOLID (S95 W-1 PASS) | no bounce; two null cones explain scalar/tensor asymmetry; SONIC-vs-THERMODYNAMIC firewall |
| 7 | `A_s` two-equation transduction + greybody | PHONONIC→emergent | SOLID architecture; band PRELIMINARY | band `[3.11,4.27]e-9` uncollapsed pending `ε_pivot` → §V.2 |
| 8 | Missing FRW `a(t)` = back-reaction closure | (the gap) | OPEN, honestly stated | frontier #1/#8; kinematics in hand, source-promotion absent → §V.1 |
| 9 | Global `τ̇(τ)` known only at fold | (the gap) | OPEN | controlling rate for diabaticity/relic/A_s away from fold → §V.3 |
| 10 | `n_T(transit)=+0.4676` blue floor | PHONONIC | SOLID but under-displayed | production-dominated tensor signature, 54 decades from CMB → §V.4 |
| 11 | `a₂`-carrier visibility (F1) | PHONONIC | HELD pending NULL scan | clean Bogoliubov-spectrum compute → §V.5 |
| 12 | κ=0 point vs DOS cusp τ=0.190 convention | GEOMETRIC | labeling precision | same fold, two functionals; tag before silent identification → §V.6 |

---

**Bottom line (transit axis).** The capstone is honest, structurally coherent, and correctly de-coupled from the framework's one retracted load-bearing claim (S39 integrability). On my axis the strong results are genuinely strong — the monotone-ramp transit, the diabatic `P_exc=1` saturation, the pure-product Ordered Veil over-determined at three legs, and the asymmetric acoustic white hole — and they are stated at the right strength with the right caveats. The open frontiers are real and, crucially for the user's "ripe harvest" framing, **computable**: the back-reaction closure `H²=f(ρ_relic,S_SA)` (§V.1) is the single highest-leverage transit-side computation in the framework, and the `A_s`-band collapse (§V.2), global `τ̇(τ)` profile (§V.3), and falsifier F1 NULL scan (§V.5) are each a clean one-session run on inputs that are already canonical. Nothing in the transit sections requires re-adjudication; everything requires more compute, and §V is where that compute is queued.
