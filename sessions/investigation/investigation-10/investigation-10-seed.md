# Investigation 10 — Seed Digest

**Date**: 2026-06-14 (S108–109 plateau)
**Mode**: investigation (`/rclab-plan --investigation 10`)
**Seed (`--from`)**: three investigation-1 survey outputs —
`investigation-1/tesla-resonance.md` + `investigation-1/quantum-acoustics-theorist.md` + `investigation-1/kitaev-quantum-chaos-theorist.md`
(3-agent survey batch). Direct-seeded (no inv-1 `_synthesis.md` exists yet).
**Invocation note**: typed `--investigation 10 --context <3 files joined by &&>`; resolved to `--from`
(the canonical agent-survey seed shape; identical precedent inv-3 / inv-4 / inv-5 / inv-6 / inv-7 / inv-8).
**Shape**: fanout (4 per-wave plan files + thin plan-index).
**Source manifest** (each agent is sole writer of its inv-1 file):

| Agent | inv-1 file | Vantage | Sections lifted |
|:------|:-----------|:--------|:----------------|
| tesla-resonance | `investigation-1/tesla-resonance.md` | resonance-first — EM/acoustic resonance, superfluid dynamics, alternative-expansion cosmologies; "what oscillates, what is the cavity, what selects the standing wave" | G1–G4, C1–C2, U1–U3, R1–R4, B1–B5, NS 1–5 |
| quantum-acoustics-theorist | `investigation-1/quantum-acoustics-theorist.md` | phonon dispersion, lattice dynamics, GGE/Bogoliubov physics, analog gravity; "dispersion first, occupation second, observable last" | G-QA-1–3, C-QA-1–3, A-QA-1–4, R-QA-1–4, B-QA-1–5, NS 1–5 |
| kitaev-quantum-chaos-theorist | `investigation-1/kitaev-quantum-chaos-theorist.md` | quantum-chaos diagnostics — OTOC/λ_L, SFF, Krylov, RMT level statistics, RP resonances; "chaos is a measured property, not a vibe" | G1–G3, C1–C3, A1–A4, R1–R4, U1–U4, NS 1–5 |

---

## Thesis (cross-agent convergence)

The framework's single most important *unbuilt* phononic gate is **TRANSIT-PS-67 — the full mode-by-mode post-fold GGE acoustic power spectrum P(k)** — and the cluster converges on assembling it and reading its observables. quantum-acoustics names it the #1 load-bearing hole ("the framework claims the CMB is the Fourier transform of a post-transit GGE interference pattern, but the object that would produce that pattern has never been assembled end-to-end"); tesla supplies its missing substrate-physics input (the post-freeze turbulent-cascade exponent); kitaev orbits the same GGE relic from the integrability side. All three vantages are native phonon/acoustic/chaos readers of the substrate's own claim — *particles are phononic excitations of M⁴×SU(3)*.

**The spine — assemble the post-fold GGE power spectrum and read its observables:**

1. **quantum-acoustics G-QA-1/B-QA-1**: build TRANSIT-PS-67 as a genuine mode-by-mode sudden-quench Bogoliubov `P(k) = Σ_k |β_k|²|mode-fn|²`; read A_s off the **finite-pair static structure factor** of the 59.8-pair GGE (O(1)), NOT off an exponential-Mach enhancement of a de Sitter template (the source of the +9.5-OOM overproduction).
2. **tesla B1/G2**: the post-freeze **turbulent-cascade exponent** E(k) (Kolmogorov k^{−5/3} vs Vinen k^{−1}) IS the substrate-physics tilt input TRANSIT-PS needs — `n_s−1 = cascade exponent` — and the freeze-out-time-vs-cascade-onset-time comparison decides whether the relic is processed (U3 false) or frozen (U3 holds, R_therm=5252).

The **A_s normalization** is genuinely contested at the mechanism layer (qa: finite-pair static structure factor / exponential-Mach double-counting; tesla: a 4.8 dB resonance-impedance step at the white-hole surface) → a Q1a workshop. The **acoustic-horizon reality** is genuinely contested (tesla: φ=0/no-superflow ⇒ the S85 "causal disconnection" is a moduli-space turning point, not a BLV spatial horizon; volovik: the τ-flow IS the effective flow ⇒ genuine analog horizon) → a Q1a workshop. kitaev supplies the **integrability-side** companion: emergent-QM from GGE-projection modular flow (not scrambling — λ_L=0 across 4 functionals), the spectral-rigidity classification (genuine-integrable vs superposition-Poisson), the RP-resonance edge-of-chaos at the fold, and ETH-violation as the positive statement of the Ordered Veil.

### Cross-agent convergence map

| Convergence | tesla | quantum-acoustics | kitaev | Investigation route |
|:------------|:------|:------------------|:-------|:--------------------|
| **TRANSIT-PS-67 / post-fold GGE P(k)** (the #1 CRITICAL gate) | B1/G2 (cascade exponent = tilt input) | G-QA-1/B-QA-1 (build P(k); A_s from static structure factor) | (GGE is the shared object) | W2-1 (TRANSIT-PS shape) + W1-1 (cascade) + W4-1 (A_s mechanism workshop) |
| **A_s normalization mechanism** (3.15-under vs 9.5-over, a 12-OOM sign-flip) | G3 (impedance step, 4.8 dB) | G-QA-2/C-QA-2/B-QA-1 (finite-pair static structure factor) | — | W4-1 (qa ↔ tesla adjudication workshop) |
| **Roton / Landau critical velocity / dispersion** | R1/B3 (Leggett = substrate roton; v_c=Δ_rot/p₀) | B-QA-2/R-QA-4 (roton as 2nd DM; 4-speed dispersion) | — | W1-2 (roton + Landau v_c) |
| **D_K spectral statistics / spectral dimension** | G1/B2 (M⁴-summand d_s, NEVER computed) | G-QA-3 (d_s(σ) flow through fold) | U3/R3/G2/A3 (Σ²(L) + SFF rigidity) | W3-3 (Σ²/SFF rigidity) + standing gap (M⁴ d_s) |
| **Fold dynamics / edge-of-chaos / arrow-of-time** | U1/B5 (synthetic-(τ)-dim Zak phase) | R-QA-1/B-QA-5 (S101 parametric resonance / Floquet) | U2/R2/A4 (RP resonances; power-law decay) | W1-4 (Zak phase) + W2-4 (Floquet) + W3-2 (RP resonances) |
| **Emergent-QM from the integrable GGE** | — | (GGE relic character) | G1/A1/U1 (GGE-projection modular flow, λ_L=0-compatible) | W3-1 (GGE-projection Born-rule structure) |
| **Acoustic-horizon reality (φ=0 / no superflow)** | C1 (moduli-turning-point) | (acoustic-metric language) | C3 (Page-time on non-holographic substrate) | W4-2 (tesla ↔ volovik adjudication workshop) |
| **CMB acoustic features** | B4/G4/R4 (second-sound horizon ℓ≈721) | B-QA-3/R-QA-2/B-QA-4 (Sakharov peaks; bispectrum + τ_NL) | — | W1-3 (ℓ≈721) + W2-2 (Sakharov) + W2-3 (bispectrum/τ_NL) |
| **GGE-permanence mechanism hygiene** | (C2 ³He-B two-fluid retracted) | C-QA-1 (S43 infinite-κ scrub) | C1/C2/R1/R4 (chaos-doc down-tag; ADH vs t_therm) | Routed OUT (Q2 HY1–HY3) — session-track curated docs |
| **Ordered Veil as a positive structural property** | U3 (frozen-GGE-as-final) | — | U4/C2 (ETH-violation; cell-vs-fabric) | W3-4 (ETH-violation test) |

---

## Candidate gate table (deduped; per-wave bucketing)

Owner = reviewer-origin, except W4 (NEUTRAL `gen-physicist` planner — the workshops' participants include the W1/W2 owners). Suggested exec = substrate-match. Every item traces to a specific seed finding.

### Wave 1 — tesla-resonance: resonance-first (cascade, dispersion, second-sound, synthetic topology)

| # | Gate ID | gate_type | Suggested exec | Seed anchor | One-line scope |
|:--|:--------|:----------|:---------------|:------------|:---------------|
| 1 | INV10-W1-1 | compute | transit-dynamics-theorist (tesla-origin) | tesla B1/G2/U3, NS-1 | Post-fold GGE turbulent-cascade exponent E(k) from the Bogoliubov amplitudes \|β_k\|² (Kolmogorov k^{−5/3} vs Vinen k^{−1} vs substrate-specific); compare freeze-out time vs cascade-onset time → does turbulence process the relic (U3 false) or is the diabatic freeze fast enough to suppress it (R_therm=5252, U3 holds)? `n_s−1 = cascade exponent`. |
| 2 | INV10-W1-2 | compute | tesla-resonance | tesla B3/R1, NS-2 | Substrate roton parameters (Δ_rot, p₀, μ_r) from the B3/optical dispersion (`s62_phonon_dispersion_full`) + Landau critical velocity v_c = Δ_rot/p₀: is the Mach-13.75 transit dissipative (v_transit > v_c ⇒ roton/Leggett emission = a 2nd DM-production channel) or dissipationless (v_transit < v_c ⇒ coherent horizon)? Adjudicates C1. The Leggett mode IS the substrate roton (S58). |
| 3 | INV10-W1-3 | compute | tesla-resonance (mack-routed inventory row) | tesla B4/G4/R4, NS-3 | Re-derive the second-sound CMB horizon ℓ_second_sound = π·(c_fabric/c_Gold) with CURRENT four-speed values; place against Planck TT; revive-or-retire (falsifier row → mack sole-writer). The CMB-side companion to the first-sound BAO ring (Row #72). Second sound PROVEN Q=75,989 (S44/S68). |
| 4 | INV10-W1-4 | compute | tesla-resonance (baptista/berry co-option for the topology) | tesla B5/U1, NS-4 | Zak phase across the fold in synthetic (τ) dimension: is τ_fold=0.190 a topologically-protected band-touching (a Weyl/Dirac node in the (k,τ) extended zone)? Compute the Zak/Berry-phase WINDING across the fold (NOT the already-zero local Berry curvature, W5). If protected ⇒ τ_fold is a topological invariant, not an empirical input (U1). |
| 5 | INV10-W1-5 | solo | tesla-resonance | tesla R2, NS-5 | Reconcile the three analog temperatures — T_acoustic=0.112 M_KK (GGE-relic) vs BLV acoustic surface-gravity vs Hawking-analog T_H=ħκ/2π — their agreement is a direct internal-consistency test of the acoustic-white-hole claim (bears on C1/W4-2). (The T_acoustic PROVENANCE write is session-track HY4.) |

### Wave 2 — quantum-acoustics-theorist: TRANSIT-PS assembly + bispectrum + parametric resonance

| # | Gate ID | gate_type | Suggested exec | Seed anchor | One-line scope |
|:--|:--------|:----------|:---------------|:------------|:---------------|
| 1 | INV10-W2-1 | compute | quantum-acoustics-theorist (transit-dynamics co-author) | qa G-QA-1/B-QA-1, NS-1 | BUILD TRANSIT-PS-67: the full mode-by-mode sudden-quench Bogoliubov P(k)=Σ_k\|β_k\|²\|mode-fn\|² through the fold at the highest tractable L_max; produce the spectrum SHAPE → n_s(k). (The A_s amplitude NORMALIZATION mechanism is the contested W4-1 question; W2-1 builds the shape, W4-1 adjudicates the amplitude.) The framework's own constraint matrix calls this CRITICAL; only partial scripts (s67/s73b/s85_w1b) exist. |
| 2 | INV10-W2-2 | compute | quantum-acoustics-theorist | qa B-QA-3, NS-2 | Sakharov acoustic-peak prediction: extract the oscillation phase from the substrate sound horizon (c_BLV·η_fold), giving P(k) ∝ [n_k]×[1−cos(2 c_s k η_fold)]; confront the already-recorded BAO θ_A 0.78% / 2.6σ residual (B1 carries 99.08% of the amplitude). The framework's first acoustic-peak-position prediction. Consumes W2-1. |
| 3 | INV10-W2-3 | compute | quantum-acoustics-theorist | qa R-QA-2/B-QA-4, NS-3 | Bispectrum shape triple — complete the PRE-REG-INC `S88-F-NL-EQUILATERAL` arm → (f_NL^local, f_NL^equil, f_NL^folded) — AND compute τ_NL from the two-mode-squeezed structure; test Suyama-Yamaguchi saturation (single-source-squeezed-vacuum consistency). f_NL_total=1.03 already PASSES (S96); this is the trispectrum falsifier. |
| 4 | INV10-W2-4 | compute | quantum-acoustics-theorist (transit-dynamics co-option) | qa R-QA-1/B-QA-5/A-QA-2 | Characterize the S101 in-band parametric resonance (ω_q=2.0128 M_KK, γ=29.7532, §VII.BP COINCIDENCE-BOUNDED) as a FLOQUET/preheating phenomenon: compute the Floquet exponent μ_F across the period-2 (ω≈ω_drive/2) tongue (the old FLOQUET-CLOSED μ_F=0 was a DIFFERENT drive); discrete-time-crystal candidate? + the pump-coupling constrains the modulus effective action (A-QA-2). |

### Wave 3 — kitaev-quantum-chaos-theorist: integrability, spectral statistics, emergent-QM, edge-of-chaos

| # | Gate ID | gate_type | Suggested exec | Seed anchor | One-line scope |
|:--|:--------|:----------|:---------------|:------------|:---------------|
| 1 | INV10-W3-1 | compute | kitaev-quantum-chaos-theorist (connes co-option for the modular algebra) | kitaev U1/G1/A1, NS-2 | GGE-projection origin of quantum uncertainty (the surviving QM-emergence route, compatible with λ_L=0 + N₃=0): compute the subsystem entanglement-entropy / measurement statistics of the certified Type III₁ GGE under the Tomita-Takesaki modular flow σ_t^ω restricted to the K₇=0 visible subalgebra; does Born-rule-structured (irreducible, not-removable-by-more-charges) fluctuation emerge? Replaces the dead scrambling mechanism (C1). |
| 2 | INV10-W3-2 | compute | kitaev-quantum-chaos-theorist | kitaev U2/R2/A4 | Ruelle-Pollicott resonance spectrum / branch-point structure of the BdG Liouvillian L[ρ]=−i[H_BdG,ρ] at τ∈{0.15, 0.175, 0.190, 0.205, 0.25}: is the late-time correlation decay at τ_fold power-law C(t)~t^{−1/2} (edge-of-chaos + a dynamical arrow-of-time at the fold) or τ-independent exponential/non-decay (the fold is a DOS feature, not dynamical criticality)? Settles A4. |
| 3 | INV10-W3-3 | compute | kitaev-quantum-chaos-theorist (spectral-geometer co-option for the deep-truncation spectrum) | kitaev U3/R3/G2/A3 | Number variance Σ²(L) + connected SFF on the FULL deep-truncation D_K spectrum (L=12→14, S105 GT-builder) across a RANGE of L: Σ²(L)~L (Poisson, genuine-integrable-leaning) vs ~ln L (RMT-rigid) vs super-Poisson (Berry-Tabor superposition artifact, Σ²(5)≈9.92 fingerprint). Settles whether fabric "integrability" is genuine complete-charge or superposition-Poisson — and ties it to the spectrum the cosmological observables are computed from. |
| 4 | INV10-W3-4 | compute | kitaev-quantum-chaos-theorist | kitaev U4/C2 | ETH-violation test on the L12 cache: eigenstate-to-eigenstate fluctuation of a substrate-local operator (gap Δ or a Peter-Weyl sector occupation) at fixed D_K energy. Large + size-independent fluctuation = ETH-violation = the rigorous POSITIVE statement of the Ordered Veil; a direct cell-vs-fabric discriminator (the weakly-chaotic single cell approaches ETH per INTEG-39; the Poisson fabric violates it). Resolves C2 at the structural level. |

### Wave 4 — cross-vantage adjudications (the two genuine Q1a workshops)

| # | Gate ID | gate_type | Agents (EXACTLY 2, 2 rounds) | Seed anchor | One-line scope |
|:--|:--------|:----------|:-----------------------------|:------------|:---------------|
| 1 | INV10-W4-1 | workshop | quantum-acoustics-theorist ↔ tesla-resonance | qa G-QA-2/C-QA-2/B-QA-1 vs tesla G3 | A_s normalization MECHANISM: the substrate over/under-produces the scalar amplitude (3.15-under vs 9.5-over, a 12-OOM sign-flip) — is the fix the finite-pair static structure factor of the 59.8-pair GGE (qa: the +9.5-OOM overproduction is exponential-Mach double-counting; exp-Mach → GGE temperature, NOT amplitude) OR a resonance-impedance closure (tesla: the 3.02× is a 4.8 dB uncorrected impedance step at the white-hole surface; A_s = transmitted/incident power)? STRUCTURAL VERDICT on the A_s mechanism. |
| 2 | INV10-W4-2 | workshop | tesla-resonance ↔ volovik-superfluid-universe-theorist | tesla C1 | Acoustic-horizon reality: is the S85 transit "causal disconnection" a genuine BLV acoustic horizon or a moduli-space turning point dressed in horizon language? tesla: the BLV acoustic metric + Mach-1 horizon need a background SUPERFLOW v, but φ=0 (no superflow, atlas-09 Item 22 PERMANENT) ⇒ the "horizon" is in modulus-time, not space. volovik: the τ-flow (modulus velocity dτ/dt) IS the effective flow that sources the analog metric; spatial superflow is not required for an analog horizon. STRUCTURAL VERDICT on the nature of the transit horizon. |

**gate_type rationale (Q1/Q2/Q3 per `Investigating-Workshops.md`)**:
- **W4-1 + W4-2 are genuine Q1a workshops** — opposed first-principles readings of a SPECIFIC tension, essential cross-rebuttal, STRUCTURAL VERDICT. W4-1: qa holds the finite-pair-static-structure-factor reading, tesla holds the resonance-impedance reading — two competing MECHANISMS for the same A_s discrepancy (decidable by physics argument, not by running TRANSIT-PS). W4-2: tesla holds the moduli-turning-point reading (φ=0 ⇒ no BLV spatial horizon), volovik holds the genuine-analog-horizon reading (τ-flow IS the flow) and owns the emergent-acoustic-spacetime-from-superfluids program — the S85 causal-disconnection result is the shared object.
- **The cascade-vs-freeze question is a COMPUTE, not a workshop** — tesla's W1-1 settles it by a NUMBER (freeze-out time vs cascade-onset time), no first-principles reading-tension.
- **The integrability classification is a COMPUTE** — kitaev's W3-3 settles genuine-vs-superposition-Poisson by a MEASUREMENT (Σ²/SFF), not adjudication.
- **The emergent-QM question is a COMPUTE** — kitaev's W3-1 (GGE-projection Born-rule structure); cross-referenced to inv-8 W2-3 (einstein Born rule) + inv-8 W4-1 (Bell, where kitaev is the S70 advocate), distinct machinery (modular flow σ_t^ω vs 8-RG-integrals trace).

---

## Routed OUT — Q2 session-track hygiene (NOT investigation gates)

An investigation cannot mutate curated session-track registers / framework docs (track-local boundary). These route to session-promotion at `/rclab-investigate --investigation 10` close.

| HY | Item | Seed anchor | Session-track target |
|:---|:-----|:------------|:---------------------|
| HY1 | Down-tag `framework-chaotic-instantons.md` §4/§7.1(B)/§8.2: the "lossy compression marginally viable" scrambling-origin-of-QM corridor is CLOSED (λ_L=0 across 4 functionals S38–S104; Hayden-Preskill clock never starts) + add an atlas-09 retraction row. | kitaev C1/R1, NS-1 | curated `sessions/framework/framework-chaotic-instantons.md` (designated-writer patch) + `atlas-09-retractions.md` |
| HY2 | Scrub the S43-era "infinite thermal conductivity protects the GGE" + "two independent protection mechanisms" language → the R_therm=5252 diabatic transit-freeze statement (T3 already BROKEN in the register; the mechanism narrative is not). | qa C-QA-1, NS-5 | curated `sessions/framework/` + S43/S62-era WPs (designated-writer note) |
| HY3 | Reconcile the ADH dephasing time (10^578 t_univ) vs the interaction-thermalization time (6 M_KK⁻¹) wherever both appear — a one-paragraph clarifying note (dephasing ≠ interaction-thermalization). | kitaev C2/R4 | curated `sessions/framework/framework-chaotic-instantons.md` §2.5 |
| HY4 | Add the `T_acoustic = 0.112` PROVENANCE entry (the reconciliation COMPUTE is INV10-W1-5; the canonical_constants WRITE is session-track). | tesla R2, NS-5 | `canonical_constants.py` PROVENANCE |
| HY5 | The A_s canonical-value reconciliation (the 3.15-under-vs-9.5-over 12-OOM spread; `Omega`-style register hygiene) + the falsifier-inventory A_s row — the W4-1 workshop produces the structural verdict; the canonical-value / inventory update is session-track. | qa G-QA-2 | `canonical_constants.py` + `falsifier-master-inventory.md` (mack sole-writer) |
| HY6 | Verify the SW1/SW3 lab-falsifier projection (M_KK → 58.96 MHz, 54 decades) uses the deg(T_BZ→pivot)=+2 NON-SCALAR transport machinery (atlas-09 Item 47), not a silent scalar (deg=0) projection. | tesla R3 | `falsifier-master-inventory.md` / `falsifier-watchlist.md` (mack sole-writer) |

---

## Surveyed-but-not-elevated bridges + standing gaps (context cross-refs, NOT gates)

- **tesla G1/B2 — the M⁴-summand spectral dimension d_s^{M4}(σ)** (the single largest unforced gap): NEVER computed; S93 proved the SU(3) FIBER d_s does not reduce, leaving any CDT-like reduction in the M⁴ summand near d_s≈3.91 (where `n_s−1=(d_s−4)/2` needs it). tesla explicitly ranks this a BRIDGE not a quick gate — it needs a foam/path-integral model on M⁴ the framework does not have. Recorded as a **STANDING GAP** (leverage ≠ tractability), cross-ref INV10-W3-3 (the spectral-statistics it would complement) + inv-8 W3-3 (the fiber-d_s CDT comparison) + inv-3 W2-1 (d_s-flow as K→K* map).
- **qa B-QA-2 — the roton as an immortal (Umklapp-impossible) 2nd DM candidate**: partly covered by INV10-W1-2 (roton parameters + Landau v_c); the DM-abundance angle (the flat band IS a degenerate roton; SU(3)'s no-zone-boundary makes Umklapp structurally impossible ⇒ the roton is eternal) is a cross-ref for W1-2.
- **kitaev C3 — black-hole/Page-time/Hayden-Preskill machinery on an integrable, non-holographic substrate** (§VII.AM framing): §VII.AM passed Stage-2 (S100a 9/9), so the lock condition is sound; the framing tension is noted but not elevated (framing, not substrate-physics adjudication).
- **qa B-QA-4 / kitaev U-context** — the relic's pure two-mode-squeezed-vacuum character feeds both INV10-W2-3 (τ_NL / Suyama-Yamaguchi) and the emergent-QM question (INV10-W3-1).

---

## Cross-investigation dedup (load-bearing — each gate block MUST carry its cross-reference)

Every adjacency to prior inv-2…inv-8 clusters is **complementary (distinct machinery / observable), NOT duplicate**:

- **INV10-W2-1 (BUILD TRANSIT-PS-67)** — the MASTER A_s/P(k) gate (the full mode-by-mode assembly), distinct from the FIVE partial/proxy A_s routes (inv-3 W2-3 near-floor-DOS, inv-4 W1-4 exit-horizon greybody, inv-5 W2-1 impulse-quench, inv-6 W2-2, inv-7 W3-2 GFT-resummation). INV10-W2-1 is the end-to-end transfer function those routes each approximate one leg of.
- **INV10-W3-3 (Σ²(L) + SFF spectral RIGIDITY)** ↔ inv-8 W3-3 (phonon-first P(σ) @ L_max=14-16, heat-trace d_s / CDT) + inv-3 W2-1/W2-2 (d_s-flow as K→K* map / isospectral rigidity): all read the deep-truncation D_K spectrum, but INV10-W3-3 is the INTEGRABILITY-classification rigidity functional (number variance / SFF ramp), distinct from the heat-trace dimension (inv-8) and the scale-transport map (inv-3). Same spectrum, orthogonal functionals.
- **INV10-W3-1 (GGE-projection Born-rule via modular flow σ_t^ω)** ↔ inv-8 W2-3 (einstein Born rule via the 8-RG-integrals trace) + inv-8 W4-1 (Bell-vs-hidden-variable, where kitaev is the S70 advocate): the SAME founding-conceit (emergent QM), DISTINCT machinery (Type III₁ modular flow on the K₇=0 restriction vs the GGE coarse-graining trace). kitaev plays complementary roles across inv-8 (Bell advocate) and inv-10 (GGE-projection author) — same agent, distinct gates.
- **INV10-W3-2 (RP resonances) + INV10-W2-4 (S101 Floquet) + INV10-W1-4 (Zak phase)** — three FRESH attacks on the fold's dynamical character (irreversibility / parametric amplification / synthetic-dimension topology); no prior investigation computed an RP-resonance spectrum, a Floquet exponent across the §VII.BP tongue, or a synthetic-(τ)-dimension Zak phase.
- **INV10-W1-1 (turbulent cascade) + INV10-W2-2 (Sakharov peaks) + INV10-W1-3 (second-sound ℓ≈721)** — FRESH post-fold-spectrum + CMB-acoustic-feature computes (the first-sound BAO ring Row #72 is banked, but the cascade exponent, the Sakharov phase, and the second-sound horizon are unbanked).

A result that must become permanent is **promoted into a session** (lifted as a carry-forward into a session-mode `/rclab-plan` plan and re-computed under a `session-{N}` gate), not held here — `gate-verdicts.md §"Investigation-Track Canonical Path"`.
