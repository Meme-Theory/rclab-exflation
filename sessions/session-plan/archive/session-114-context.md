# Session 114 — Plan Context (carry-forward corpus)

**Built by**: `/rclab-plan --session 114` (Phase 1b/1c).
**Carry-forward source**: the S113 EVOI-frontier workshop-campaign synthesis `sessions/session-113/session-113-workshop-campaign-synthesis.md` §3 (the 8 workshop-derived forward gates + `CF-S113-B5A-TFD`) + §4 (the §VII YUKSHAPE Stage-1 theorem registration). S113 ran NO compute waves (workshops-first); the campaign verdicts ARE the carry-forward stream (`Investigating-Workshops.md §"Cross-references"`: workshop OUTCOMES feed the next plan). Each gate carries a 4-field spec deduplicated + EVOI-ordered by the synthesis.
**Register consume (1c-REGISTERS)**: re-confirms NO additional tractable register candidate beyond these — K8 §VII.AF.1.STATE-PROJ stays PENDING-VERIFICATION (no dispatch-ready Stage-2 gate); branch-iv w₀(L) capacity-deferred (~2027 DR3); the conditional capstone down-tags (τ_fold/A_s/CCRESID) are designated-writer patches that LAND WHEN THEIR GATE RESOLVES (not S114 compute gates). EVOI §6 ⊆ this corpus by construction.
**Mode**: fanout. **Planner default**: gen-physicist. **Prompter**: gen-physicist.

---

## Corpus (10 items, EVOI-ordered; deduplicated)

| # | Gate ID | Wave | Executor (`agent_type`) | EVOI tier |
|:--|:--------|:-----|:------------------------|:----------|
| 1 | `CF-S113-FSIGMA8-EUCLID-7BIN` | W1 | mack-cosmic-bridge | Tier-1 (the #1 non-CMB falsifier) |
| 2 | `CF-S114-CO-SIGNDISC-FRIB-L-SCOPE` | W1 | nazarewicz-nuclear-structure-theorist | Tier-3 (scope constructibility first) |
| 3 | `CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN` | W2 | baptista-spacetime-analyst | Tier-2 |
| 4 | `CF-S114-TAUFOLD-CUSP-CROSSING` (Gate A1′) | W2 | transit-dynamics-theorist | Tier-2 |
| 5 | `CF-S114-CCRESID-CHI-Q-SCALING` | W2 | volovik-superfluid-universe-theorist | Tier-2 |
| 6 | `CF-S114-YUK-RIGHTREG-CONNECTION` | W3 | connes-ncg-theorist | Tier-2 |
| 7 | `CF-S114-LEGGETT-INTERBAND-25P5` | W3 | landau-condensed-matter-theorist | Tier-2 |
| 8 | `CF-S114-YUK-SHAPE-WALL-VII-LANDING` | W3 | gen-physicist (registry landing) | Tier-2 (structural) |
| 9 | `CF-S114-AS-FUNCTIONAL-SELECTION` | W4 | transit-dynamics-theorist | Tier-2 |
| 10 | `CF-S113-B5A-TFD` | W4 | hawking-theorist | Tier-3 NON-BLOCKING |

> Gate-ID note: the synthesis used mixed prefixes (`S113-YUK-…`, `CCRESID-CHI-Q-…`, etc.). Canonicalized to `CF-S114-…` here so the S114 verdict-file namespace is consistent and collision-free vs the S113 workshop IDs. The B5A-TFD gate retains its `CF-S113-B5A-TFD` ID (a pre-existing S112 WP carry-forward ID). Planners: use these IDs verbatim.

---

## Item specs (4-field; lift into R3 gate blocks)

### 1. `CF-S113-FSIGMA8-EUCLID-7BIN` — W1 — mack-cosmic-bridge  [Tier-1, the #1 non-CMB falsifier]
- **What**: test the framework's 0-param f·σ8(z) curve (`f_FW(0)=0.5254916357`, `σ8_growth_a2=0.79317`, **−4.058% PRODUCT suppression @ z=0.51**) as a joint χ² against Euclid RSD f·σ8 across the 7 spectroscopic z-bins (z≈0.9–1.8); DESI-DR2 (~1.013σ) the near-term anchor. **Anti-rescue fence**: σ8_growth=0.79317 (NOT O-Z 0.799); the −4.058% PRODUCT (NOT bare-f −0.311%); zero branch/scheme freedom.
- **Inputs**: substrate-first chain `D_K → a₂ Seeley-DeWitt → D(a) → f(z) → f·σ8(z)`; `s96_obs_fsigma8_forecast.npz` (fetched DESI-Y5/Euclid covariance); canonical `f_FW`, `σ8_growth_a2`.
- **Gate**: PASS = suppressed FW curve within the joint Euclid 1σ envelope; FAIL = joint σ ≥ pre-registered decisive threshold (a₂-growth channel excluded). Pinned: Euclid 7-bin joint ≈1.534σ.
- **Effort**: ~1 wave. **Source**: synthesis §3 #1 (WS-6 OBSAXIS verdict §4 Gate #1). **Falsifier-row already landed S113** (Row #71.audit-S113-WS6) — this gate is the COMPUTE that fills the σ-distance.

### 2. `CF-S114-CO-SIGNDISC-FRIB-L-SCOPE` — W1 — nazarewicz-nuclear-structure-theorist  [Tier-3, constructibility-scope]
- **What**: SCOPE whether a weight-free dense-matter discriminant (the WS-6 W2-1 SIGN-PASS `dΔ_CFL/dμ>0`, dimensionless, M_KK-free; tied to the symmetry-energy slope L) has ANY detector-reachable σ against FRIB `L≈40–70 MeV` (Sorensen+ 2024) — this gates whether the #2 dense-matter axis is constructible at all. REPLACES the free-dial M_max-in-M_⊙ gate (which rides M_KK, §VII.BS NNU). Discipline: NO M_max-in-M_⊙ comparison (ansatz-forced PASS, PROHIBITED Class 4).
- **Inputs**: the W2-1 SIGN-PASS npz (`dΔ_CFL/dμ` scan); FRIB symmetry-energy band (Sorensen+ 2024 χEFT+HIC+NS combined); `S110-CF-CO1-EOS` self-consistent μ_eff; canonical M_KK.
- **Gate**: PASS (constructible) = a weight-free dimensionless discriminant maps to FRIB L with a detector-reachable σ; FAIL (not constructible) = the dense-matter axis is a structural no-go (Track-B intrinsic dilute, M_KK-weighted all the way down) ⇒ the growth axis is the sole non-CMB falsifier; INFO = partial.
- **Effort**: ~2–3 waves (genuinely not-yet-constructed — this S114 gate is the constructibility CHECK, not the full build). **Source**: synthesis §3 #8 (WS-6 verdict §4 Gate #2; watchlist `S113-CO-SIGNDISC-FRIB-L-WATCH` already landed S113).

### 3. `CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN` — W2 — baptista-spacetime-analyst  [Tier-2]
- **What**: run a `w(L_max)·κ(k)` factorization on the BZ-edge→K* transfer (the 1.66-decade even-sector leg, 2.0 → K*≈0.0435 M_KK), with the transport degree as an **OPEN factorization OUTPUT** — NOT the pre-imported α_s/d_s `+2` (importing it is the §23.0(5) dedup-flag-iii category error; hard-coding `=+2` is ansatz-forced). Parity pre-flight: `R_BZ-edge` is `d_A=0` ⇒ verify the extracted degree is EVEN (a morphism degree, not a scale-leg).
- **Inputs**: D_K eigenvalue tiling on `(A_K^{≤L},H_K^{≤L},D_K^{≤L})` at τ_fold; the multiplicative-normalization factorization machinery (`math-scripts.md §"Multiplicative-normalization cancellation invariants"`); the §VII bridge `L^{-α}` envelope.
- **Gate**: PASS = even degree extracted + bridge image lands K* within envelope (Reading-A, ratio-to-K* leg ONLY; magnitude stays external); SCALAR (`factorization_holds=True`) → trivial conversion → Reading-B; non-even / no convergent image → full Reading-B. CANNOT reach the M_KK¹ magnitude (settled external) NOR the closed-negative edge=pivot identification.
- **Effort**: 1 wave. **Source**: synthesis §3 #3 (WS-1 KPIVOT verdict §4.2). Substrate framing: GEOMETRIC.

### 4. `CF-S114-TAUFOLD-CUSP-CROSSING` (Gate A1′) — W2 — transit-dynamics-theorist  [Tier-2]
- **What**: compute the van Hove cusp-**CROSSING** location (flank `dS/dτ≠0` supersonic point, distinguished from the DOS-peak) from-scratch on a τ-grid bracketing [0.18,0.23] with **NO injected 0.190**, at L_max ∈ {5,8,10,12}; report the L_max-convergence TREND vs the Friedrich-Bär saturation band (NOT a mixed-L_max PASS/FAIL tally — coarse-L drift is expected). Zero continuous free params.
- **Inputs**: `s84_spectrum_cache_L12_tau019.npz`; `dirac_spectrum.collect_spectrum(τ,…,max_pq_sum=L)` rebuild on the τ-grid at L∈{5,8,10,12}; canonical `dS_fold`, `d2S_fold`; the `S84-ALTERNATIVE-TAU-MESH-UNIQUENESS` mesh (mesh-robustness arm).
- **Gate**: PASS (→Reading-A) = crossing → 0.190±0.5%, L_max-monotone-convergent, mesh-robust (τ_fold van-Hove-SELECTED structural constant; EMPIRICAL-τ_fold fallback RETIRED); FAIL (→Reading-B) = no convergence to 0.190 (value-imported flank-point; τ_fold joins the external-import set); INFO = converges to a value in [0.19,0.221] (substrate-pinned window, flank-subchoice — HYBRID, stronger than M_KK).
- **Effort**: ~1 wave (L≤12 cached/feasible; recursive-Casimir ceiling L≥13 NOT triggered). **Source**: synthesis §3 #2 (WS-2 TAUFOLD verdict §4A). Substrate framing: GEOMETRIC (Level-2 moduli-deformation).

### 5. `CF-S114-CCRESID-CHI-Q-SCALING` — W2 — volovik-superfluid-universe-theorist  [Tier-2]
- **What**: compute the q-channel compressibility `χ_q(τ)` (and, if a substrate→a(t) map is available, `χ_q(a)`) scaling first-principles from the D_K spectrum across the Jensen family; test whether `χ_q` runs the required 118.7 OOM fold→today OR is fold-frozen (`χ_q ~ S_fold`, ΔS/S=2.2%). The τ-scan leg alone settles the crux.
- **Inputs**: the D_K eigenfreq data underlying the S97 W2-2 curvature `k=+3586.5 M_KK` (the grand-potential `d²ε/dq²`); S43 `χ_q(fold)=300,338 M_KK⁴`; `S_fold(τ)` across the Jensen family (the 2.2% spread); canonical `Ω_m`, `ρ_Λ_obs`, `M_KK`.
- **Gate**: PASS-Reading-A / FAIL-of-limitation = `χ_q` runs ≥100 OOM AND `ρ_m²/χ_q` reproduces 0.032±0.005 (RATIO tol `|frac−0.032|/0.032 ≤ 0.156`); PASS-of-limitation / Reading-B = fold-frozen (<10 OOM run, consistent with `χ_q~S_fold` to 2.2%); INFO = partial run.
- **Effort**: LOW–MEDIUM (the `d²ε/dq²` machinery exists; re-evaluation across the Jensen τ-scan). **Source**: synthesis §3 #6 (WS-3 CCRESID verdict §4.2). Substrate framing: PHONONIC (q-departure / Gibbs–Duhem channel). Pole-set / regulator pin: a₀-channel.

### 6. `CF-S114-YUK-RIGHTREG-CONNECTION` — W3 — connes-ncg-theorist  [Tier-2; dual prior 0.40 internal / 0.60 external]
- **What**: construct the right-regular generation operator `Y_R = Σ_a c_a R_{X_a}` (right-translation SU(3)_R generators on the multiplicity leg `ℂ^{m(p,q)}`) at τ_fold; test the 4-part discriminator: (i) left/G-invariance `[L_g,Y_R]=0`; (ii) sign-changing on the t=0,1,2 generation copies; (iii) `[J,D_K+Y_R]=0` block-by-block; **(iv) load-bearing**: is `Y_R ∈ closure(Ω¹_{D_K}(A_K))` (external ε_LX, Reading-B) or a connection on the substrate's OWN SU(3)_R isometry bundle reachable without enlarging A_K / dropping Axiom 5 (internal, Reading-A)?
- **Inputs**: `dirac_spectrum.py` block-diagonal machinery (left-regular D_K built); the right-regular generators `R_{X_a}` on the Peter-Weyl multiplicity leg (NEW construction — right-translation analog of the existing left-action); `J` (BDI); canonical `tau_fold`, `M_KK`. AMD RX 9070 XT per-block path.
- **Gate**: PASS (i∧ii∧iii∧iv-internal → off-Casimir route exists; the §VII SHAPE-wall theorem (gate #8) gains the "A_K-LEFT-built" scope qualifier); FAIL (iv-external → D4 closed, homogeneity-obstruction genus COMPLETE — SHAPE irreducibly external like M_KK); INFO (discriminator (iv) convention-dependent → representation-pinning workshop).
- **Effort**: 1 wave. **Source**: synthesis §3 #5 (WS-7 YUKSHAPE verdict §4b). NOTE: no prior quark-Yukawa gate (W4-15, S101-W3, S110-CF1/CF2) constructed the right-regular generators. Substrate framing: GEOMETRIC/PARTICLE.

### 7. `CF-S114-LEGGETT-INTERBAND-25P5` — W3 — landau-condensed-matter-theorist (+ mack clause-α cross-check)  [Tier-2; 3-outcome]
- **What**: compute the Leggett-branch B2⊕B3 inter-band BdG coherence-mode frequency `ω_Leggett^{B2-B3}` on the FULL B2⊕B3 sector at τ_fold (`ω² = (4Δ_2Δ_3/J_12)·(n_2⁻¹+n_3⁻¹)⁻¹·γ_12`); PLUS a clause-α provenance sub-check — does any independent DM free-streaming derivation require the Leggett DM mass = 25.5×Δ_BCS, or is 25.5× solely the n_s SA-Goldstone Wall-W9 number transplanted (Window-1 / EFOLD-MAPPING-52 escape)?
- **Inputs**: B2(mult4)⊕B3(mult3) BdG; `J_12` full-sector inter-band pair-transfer; `Δ_2,Δ_3` Richardson–Gaudin exact gap; `n_2,n_3` band-edge DOS; canonical `Δ_BCS=0.4642547`, `omega_H3=11.465`, `Mass_LeggettDM/Δ_BCS=11.97`; the EFOLD-MAPPING-52 / Window-1 record for the clause-α sub-check.
- **Gate (3-outcome; Z₂-pre-flight GATES the band eval)**: PASS (→Reading-A) = `ω/Δ_BCS ∈ [24,27]` AND Z₂-gauge-invariant on the full sector AND abundance-preserving (Z₂-odd, Ω_DM h²=0.120 survives); FAIL (→Reading-B) = the only mode at 25.5× is the Higgs amplitude branch (24.7×) ⇒ prefactor irreducible; INFO (→mis-attribution) = clause-α confirms 25.5× is solely the n_s Wall-W9 transplant ⇒ HK-170X-DM re-scoped OUT of the DM ledger. (Z₂-degenerate on full sector ⇒ INFO-blocked, NOT PASS.)
- **Effort**: 1 wave. **Source**: synthesis §3 #4 (WS-4 DMMASS verdict §4.2). Substrate framing: PHONONIC (Leggett-channel inter-band coherence). σ_SI NULL anchor-robustness already landed S113 (Row #79.audit-S113-WS4).

### 8. `CF-S114-YUK-SHAPE-WALL-VII-LANDING` — W3 — gen-physicist  [Tier-2 structural; §VII registry landing]
- **What**: register the **SHAPE-Branch Homogeneity Obstruction theorem** as a §VII STAGE-1-CANDIDATE permanent-wall entry: on `(A_K,H_K,D_K,γ₉,J)`, NO G-invariant functional in the class {Casimir-graded `f(C₂,C₃)` / γ₉-graded odd-power trace / γ₉-graded even spectral moment / γ₉-graded A_K-orientation cyclic cocycle} supplies a non-monotone sign-changing per-GENERATION (multiplicity-leg `t`) scalar. Proof: **D1** `Tr[γ₉D_K^odd]≡0` by `{γ₉,D_K}=0` (verify `Tr[γ₉D_K]=Tr[γ₉D_K³]=0` Sage-QQ machine-exact); **D2** `Tr[γ₉f(D_K²)]` conjugation-even ⇒ C₂ by `[J,D_K]=0`; **D3** Skolem-Noether leg-membership ⇒ A_K-built forms multiplicity-scalar. Scope qualifier: class `{A_K-built ∪ Casimir ∪ γ₉-traced}`; D4 (right-regular, gate #6) NOT covered, OPEN.
- **Inputs**: the WS-7 YUKSHAPE verdict §4a text (frozen Stage-0); `permanent-results-registry.md` next-free §VII slot; the D1/D2/D3 verification npz (Sage-QQ `Tr[γ₉D_K^odd]`); `{γ₉,D_K}=0` (S34/S56), the multiplicity-leg generation identification (`proven_384`).
- **Gate**: artifact-existence + structural — PASS = §VII entry written (STAGE-1-CANDIDATE tag; 5-anatomy N/A intra-pillar; STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BV/§VII.BL; NON-PROMOTION-BY-HELD-NUMBER sign-lock differentia) AND D1 machine-exact verification reproduced (`Tr[γ₉D_K]`, `Tr[γ₉D_K³]` both 0 to machine-ε). This is a COMPUTE/registry-landing gate (substrate-physics D1-D3 verification, NOT a mechanical Edit ⇒ NOT METHODOLOGY-class; per the S108 registry-completion precedent).
- **Effort**: ~0.5 wave. **Source**: synthesis §4 (YUKSHAPE 4a). Stage-2 cross-axis verify is a FUTURE gate (after gate #6 D4 resolves). Substrate framing: GEOMETRIC/PARTICLE.

### 9. `CF-S114-AS-FUNCTIONAL-SELECTION` — W4 — transit-dynamics-theorist (+ lizzi)  [Tier-2]
- **What**: test whether the substrate selects a UNIQUE spectral functional for the post-transit A_s amplitude (impulse-quench vs UNIFIED-AS-79 vs Parker-adiabatic) OR functional-choice is a genuine physical d.o.f. (lizzi-signature). Decisive sub-test: does `aH|_fold=0.975 M_KK` carry the a_0/a_2 SDW/Zubarev split (→ openness universal, impulse-quench inherits it) or is it transit-trajectory-fixed (→ openness confined to the UNIFIED route, the WS-5 Object-1 floor-origin finding holds with margin)? NOT a Planck-comparison gate (no scheme-independent number exists).
- **Inputs**: `s100b_box_delta_bogoliubov.npz` (the `|β_k̂|²` spectrum + `aH|_fold` barrier); the SDW vs Zubarev a_0/a_2 readings (S82 Obs 6.3, 181× Path-B split); inv5/inv6/UNIFIED A_s values; s64-clock `H_fold=586.527` provenance; canonical `xi_KZ_FW`, `A_s_FW`.
- **Gate**: PASS (functional SELECTED) = a substrate-canonical argument pins ONE functional (the 1.26-OOM spread collapses + scheme-tag retired); FAIL (functional-pluralism PERMANENT) = no canonical selector ⇒ A_s magnitude is a physical d.o.f. like the CC ratio (the §EVOI.BF liability becomes "open, structurally"); INFO = `aH|_fold`'s a_0/a_2-dependence partial / regime-conditional.
- **Effort**: ~1 wave. **Source**: synthesis §3 #7 (WS-5 AS-HTILDE verdict §5). A_s floor-point/scheme-dependent annotation already landed S113 (Row #12.audit-S113-WS5). Substrate framing: PHONONIC.

### 10. `CF-S113-B5A-TFD` — W4 — hawking-theorist  [Tier-3 NON-BLOCKING]
- **What**: re-compute the white-hole exit-slice microstate count via a TWO-SIDED thermofield-double (TFD) island construction (the surviving route — single-sided exit slice undershoots to R≈0.53, full island overshoots to R≈1.38; A/4 sits between). Test the TFD microstate count against the emergent area-law `A_horizon_FW/4`.
- **Inputs**: the L12 GGE bulk-EE profile (`computations/session-111/s111_b5a_island.npz` cum_S_bulk); a TFD doubling of the exit-slice causal patch; `A_horizon_FW=71226.26338976152` (canonical, S92); `c_conical=0.25` (a₂^{Pauli-Villars}).
- **Gate**: `|R_TFD − 1| ≤ 0.10` PASS; `(0.10, 0.25]` INFO; `> 0.25` FAIL. `[SIGN]` — monotone in the TFD-accessible bulk-EE fraction.
- **Effort**: ~1 wave (reuses the S111 L12 bulk-EE profile; new machinery = the TFD doubling geometry). **Source**: `session-112-w3-workingpaper.md §"Carry-Forward Computations"` (the lone S112 WP carry-forward; synthesis §3 #9). Substrate framing: GEOMETRIC.

---

## Source manifest
- `sessions/session-113/session-113-workshop-campaign-synthesis.md` §3 (gates 1–9) + §4 (gate 8, the §VII landing) — PRIMARY (deduplicated, EVOI-ordered).
- `sessions/session-113/workshops/ws-s113-{1..7}-*/ws-s113-{N}-*-verdict.md` — the 7 underlying verdicts (full 4-field detail per gate).
- `sessions/session-112/session-112-w3-workingpaper.md §"Carry-Forward Computations"` — `CF-S113-B5A-TFD` (item 10).
- EVOI §6 (S114 queue) + atlas-04 C1/C2/A4/C10 (S112/S113 freshness) — the consumed forward registers.

## Standing gaps (high-leverage, NO tractable S114 gate — leverage ≠ tractability)
- **K8 §VII.AF.1.STATE-PROJ** — PENDING-VERIFICATION, empty companion slot (needs a Stage-1 derivation, not a Stage-2 verify); not lifted.
- **branch-iv w₀(L) truncation-stability** — GT-builder route, capacity-deferred ~2027 DR3.
- **The conditional capstone down-tags** (τ_fold / A_s / CCRESID) — designated-writer patches that LAND WHEN gates #4 / #9 / #5 resolve (NOT S114 compute gates).
