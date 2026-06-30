# Sub-A4 — Corpus Digests (BH-Cosmology ↔ Exflation incursion)

**Agent**: corpus reader (careful-reader pass for Lead A)
**Campaign**: BH-Cosmology ↔ Exflation incursion
**Date**: 2026-06-13
**Mandate**: Read 7 arXiv papers IN FULL; extract only from fetched text (no training knowledge). One digest per paper: core mechanism/claim, load-bearing equations (verbatim), falsifiable prediction / observational test, negative result, global causal/thermodynamic structure.

**Source method**: PDFs extracted page-by-page with `pypdf 6.9.2` (venv312) from `downloads/bh-cosmo/{black-hole-cosmology,eco-phenomenology}/`; the HTML/PDF MCP `read_arxiv_paper` returned empty on the pre-2007 category-prefixed IDs (`hep-th/0103019`, `hep-th/0612185`), so I read the on-disk PDFs directly. Equations are transcribed from the pypdf text layer (some Unicode/sub-superscript mangling is inherent to PDF extraction; I have normalized obvious artifacts and flagged any uncertain symbol). Reference lists were stripped from the read.

**Verified arXiv IDs** (matched against both `00-INDEX.md` files): #1 hep-th/0103019; #2 hep-th/0612185; #17 2405.16673 (v3, 21 Jan 2026); #19 2602.17702 (v1, physics.gen-ph); ECO-04 1602.08759; ECO-08 1709.01525; ECO-15 2509.16310 (v2, 28 Jan 2026).

**Corpus-metadata corrections found**:
- The index lists #17 as "CQG 42, 2025"; the on-disk PDF header is `Classical and Quantum Gravity 42(6), 065017 (2025)`, arXiv `2405.16673v3 [gr-qc] 21 Jan 2026`. It is a **gr-qc** paper (NOT gen-ph) — peer-reviewed, standard GR. Flag for any "non-standard claim" tagging: #17 is the rigorous one in the Poplawski set.
- #19 IS `physics.gen-ph` as the prompt warned (non-standard claims flagged inline below).

---

## Paper 01 — Easson & Brandenberger (2001), *Universe Generation from Black Hole Interiors* [hep-th/0103019]

**Core claim.** A daughter universe born inside a black-hole interior inherits properties of the mother universe; the horizon, flatness, structure-formation, and information-loss problems of the Standard Big Bang (SBB) can be addressed **without a long period of inflation**. The conclusions are explicitly model-independent — they hold for ANY scenario (refs [1]–[8]) in which the Schwarzschild singularity at `r=0` is replaced by an initial-time surface of a de Sitter interior (the limiting-curvature construction).

- **Limiting-curvature / singularity replacement.** Near the would-be Schwarzschild singularity, high Weyl curvature triggers a matching to a locally de Sitter metric. The singularity at `r=0` becomes the initial time surface `t=0` of a baby de Sitter universe. This is implemented (in cited prior work) via higher-derivative gravity with a non-dynamical scalar `φ` and potential `V(φ)` engineered so the metric becomes locally de Sitter at high curvature. **The de Sitter core replaces the singularity — it is NOT a long inflationary epoch** (the de Sitter bounce is "presumably of too short duration to solve the problems of standard cosmology" by inflation's mechanism — the problems are instead solved by the BH-interior geometry).
- **Coordinate role-swap (load-bearing geometric fact).** Crossing the horizon, `r` and `t` switch roles (`g_tt`, `g_rr` change sign). Matter falling to `r=0` at DIFFERENT Schwarzschild times all enters the baby universe at the SAME time `t=0` but at DIFFERENT places. This is the geometric engine for homogenizing the daughter universe.

- **Horizon problem — solved by causal pre-contact, not inflation.** Photon orbits around the BH are studied via the Schwarzschild geodesic equation. The orbit equation:
  ```
  φ(u) = − ∫ du / sqrt( 2mu³ − u² + (2mκ/L²)u − κ/L² + E²/L² )      (Eq. 7, u = 1/r)
  ```
  Three regimes: (1) **large r / small u**: `φ(u) = arcsin(−Lu/E)` (Eq. 9, photons κ=0) — bound orbits circle many times, reach thermal equilibrium before plunging. (2) **near-horizon** (`r_i ≈ 1.9m → 0`): photon sweeps `≈ 114°` — "probably not enough" to homogenize. (3) **deep interior / large u**: `φ(Δr) = 2√(2m) (Δr)^{1/2}` (Eq. 11), maximum `φ ≈ 80°` — cannot bend ~180°. **NEGATIVE result (internal):** one CANNOT solve the horizon problem by interior interactions alone (regimes 2, 3 fall short); the resolution must rely on matter reaching equilibrium BEFORE crossing the horizon (regime 1, large-r bound orbits) plus the causality fact that the `t=0` de Sitter surface is in causal contact along the radial direction.
- **Flatness problem — topological argument singling out k=0.** Reformulated via the FRW `k` parameter:
  ```
  ρ₀ = (3/8πG)( k/R₀² + H₀² )      (Eq. 13);   flatness ⇔ k=0
  ```
  Interior metric after `r → −t` substitution: `ds² = (1+2m/t)dr² − dt²/(1+2m/t)` (Eq. 14; horizon now at `t=−2m`). Spatial size of the daughter universe (Schwarzschild side):
  ```
  s = ∫_{−∞}^{∞} sqrt(1 + 2m/t) dr  → ∞ (linearly)      (Eq. 15)
  ```
  De Sitter side scale factor: `R ∝ {sinh Hτ (k=−1), cosh Hτ (k=+1), exp Hτ (k=0)}` (Eq. 16). Matching the linearly-divergent length forces **k=0**: "the only value of k which causes the integral to linearly approach infinity is k=0, flat." So the model **singles out the observed flat FRW universe by a topology-matching argument** (not by an inflationary attractor).
- **Structure formation — qualitative only.** No quantitative fluctuation theory. Two ideas floated: (a) cosmic-string defects from a daughter-universe matter phase transition (noted to have trouble with the narrow first Doppler peak); (b) **Hawking radiation of the PARENT black hole** appears as quantum fluctuations in the de Sitter interior; modes with `λ >> c/H` freeze as classical amplitudes seeding structure. This is the paper's distinctive structure mechanism: parent-BH Hawking quanta seed the daughter's perturbations.
- **Information-loss problem — resolved by construction.** Pure state `ρ=|ψ⟩⟨ψ|` collapsing to a Hawking-mixed state `ρ = Σ_n p_n |ψ_n⟩⟨ψ_n|` (Eq. 18) with entropy `~ M²/m_pl²` would lose information; here pure states fall in and **emerge in the new universe as pure states** — information is transferred parent→daughter, never destroyed.

**Falsifiable content.** Weak. The flatness `k=0` is a postdiction matching observation; structure-formation is unspecified. No sharp numerical prediction. The paper's value is structural: a proof-of-concept that interior-of-BH cosmogenesis addresses SBB problems by GEOMETRY rather than by an inflaton.

**Global causal/thermodynamic structure (framework-relevant).** Pre/post-transit causal disconnection is built in: the `r↔t` role-swap means the daughter's `t=0` surface is causally sealed from the parent exterior — **structurally the GR-side analog of the framework's acoustic white hole** (pre/post-transit causal disconnection via supersonic flow at τ_fold). Direction-of-explanation note: this is a GEOMETRIC-class laboratory-IN model (the de Sitter core is engineered into the metric), NOT a substrate mechanism — the substrate transit is a first-order van Hove phase transition, not a curvature-bounce.

---

## Paper 02 — Smolin (2006), *The Status of Cosmological Natural Selection* [hep-th/0612185]

**Core claim.** Cosmological Natural Selection (CNS) is presented as the ONLY known landscape theory that yields **falsifiable predictions for doable experiments WITHOUT the anthropic principle**. Black-hole singularities bounce to initial states of new expanding universes; at each bounce the low-energy parameters `p ∈ P` change by a small random amount. The ensemble converges to one peaked near LOCAL extrema of the fitness function `f(p)` = average number of black holes a universe with parameters `p` produces.

- **The four conditions for a landscape theory to be falsifiable** (the paper's logical spine):
  1. The generating process `M` yields a **highly non-random** distribution `ρ_P`; our universe is a typical (random) member.
  2. There exist observables `A_i` whose values are typical of the ensemble — these are "explained."
  3. There exist further, **yet-unmeasured** properties `B_i` true in almost all ensemble members — these are the **predictions**.
  4. (To solve the special-tuning problem) the ensemble evolution at `l ∈ L` must be **highly sensitive to the low-energy parameters** `p = I(l)` — otherwise it cannot preferentially populate the narrow stars/chemistry-friendly region of `P`.
- **The master prediction M (verbatim):** *"Almost every small change in p from its present value either leaves f(p) unchanged or leads to a decrease in f(p)... almost no change in the parameters of the standard model from the present values will increase the numbers of black holes produced."* This is a type-B property — local, not global (the paper is explicit that CNS does NOT predict a global maximum of `f`, because that needs unknown details of the map `I : L → P`).

**The three published, falsifiable, CURRENTLY-HOLDING predictions** (this is the falsifiability payload):
  1. **Neutron-star upper mass limit.** CNS ⇒ neutron stars are kaon-condensate stars with `M_uml ≈ 1.6 M_⊙`. Rationale: the strange-quark mass can be varied to raise/lower `M_uml` WITHOUT strongly affecting massive-star formation or supernovae — so if `M_uml` could be pushed much higher (more BH production via more massive remnants) the parameters would not be at a local `f` maximum. **Kill condition: a well-measured neutron star with `M > 1.6 M_⊙` (a kaon condensate cannot support it) falsifies CNS.** Status (2006): all well-measured NS between 1.3–1.45 M_⊙; one imprecise dangerous case exceeds the bound at <1σ.
  2. **Single-parameter inflation.** If inflation is true, the inflaton coupling controlling `δρ/ρ` must ALSO control the e-folding number `N`, so the two are **anti-correlated** (you cannot raise `δρ/ρ` to make more primordial BHs without lowering `N` → exponentially smaller universe → fewer BHs overall). CNS predicts single-field, single-parameter inflation; multi-parameter models with independent `δρ/ρ` and `N` are disfavored. Status: holds.
  3. **Little early star formation.** If non-carbon massive-star channels existed they would operate at high `z` (low C/O abundance) → many more high-z supernovae. Status: not observed.

- **Reply to Vilenkin's anthropic objection (the adversarial core).** Vilenkin's argument: a small `Λ₀ ≈ 10⁻¹²² l_Pl⁻²` ⇒ eternal de Sitter with temperature `T₀ = 1/(2πR)` (Eq. 1, `R⁻¹ = H = √(Λ/3)`); de Sitter spontaneously nucleates BHs at rate `Γ = l_Pl⁻⁴ e^{−M/T₀}` (Eq. 2, Ginsparg-Perry), maximized for Planck-mass BHs at `Γ_max = l_Pl⁻⁴ e^{−2πR/t_Pl} ≈ l_Pl⁻⁴ e^{−10⁶¹}` (Eq. 3). Because de Sitter volume grows exponentially, after `t_N ≈ R·10⁶¹` the nucleated BHs SWAMP astrophysical BH production — and the count is INCREASED by raising `Λ₀`, so our universe is NOT optimized for BH production ⇒ CNS false.
- **Smolin's five-pronged refutation** (each is a stated reason Vilenkin's assumptions are unreliable):
  1. **Vast-scale extrapolation.** The argument extrapolates current laws `10⁶⁰×` beyond tested scales; the least-understood parameter (`Λ`) is exactly the one required to be stable over that range.
  2. **CMB evidence of new physics at the present Hubble scale.** Lack of power > 60°, the "axis of evil" (`l=2`–`5`), `l`-up-to-40 hemispheric asymmetry — anomalies suggesting ΛCDM may already break down NOW, undermining extrapolation to `t_N`.
  3. **IR-completion sensitivity.** Quintessence/ghost-condensate/non-local modifications would all change the late-time evolution; e.g. quintessence `Λ` could decay to zero before the BH-nucleation era.
  4. **Euclidean-path-integral invalidity.** Ginsparg-Perry uses the Euclidean path integral, which assumes thermal equilibrium (KMS condition). But **gravitons never thermalize**: `τ(t) > t` (Eq. 4) — the mean free time always exceeds the age. Also, Euclidean QG above d=2 has no critical point to define a continuum limit (dynamical-triangulation result); Lorentzian and Euclidean path integrals lie in DIFFERENT universality classes.
  5. **UV-completion sensitivity (uv-ir mixing).** `Γ ≈ E_Pl⁻⁴ e^{−E_Pl/T}` (Eq. 6) is dominated by Planck-mass BHs, so the result is exponentially sensitive to UV physics. Doubly/deformed special relativity (forced in 2+1 QG) cuts the Planck spectrum off at `λ ≈ l_Pl`, possibly **completely suppressing BH nucleation** at finite positive `Λ`.
  6. **Reductio (freak-observer parallel).** The SAME argument would falsify Darwinian biology's prediction `D` ("almost every DNA sequence in nature is in a reproducing creature") via spontaneous de Sitter thermal nucleation of DNA `Γ(A) ≈ e^{−α m(A) R}` (Eq. 7). One saves biology by restricting the ensemble to biologically-produced DNA; the SAME move (restrict to astrophysical-BH-produced universes) saves CNS. So either Vilenkin's argument is wrong or it has no force against CNS.

**Negative result / philosophical claim.** No landscape theory lacking conditions 1–4 can produce falsifiable predictions or genuinely solve special tuning — and the anthropic principle / eternal inflation require the principle of mediocrity, which is too flexible (ensemble choice is unconstrained). CNS is the only constructive existence proof.

**Falsifiable content (HIGHEST of the 7).** The neutron-star `M_uml ≈ 1.6 M_⊙` ceiling is a sharp, doable, presently-testable kill condition with a clean physical mechanism (kaon condensation softens the EoS). It is the single most falsifiable prediction in the corpus.

**Framework-relevant note.** CNS connects to `project_cosmic-reproduction.md` (measurement = vacuum decay = baby universe). Smolin's prong 4 ("gravitons never thermalize," `τ(t)>t`) is a striking parallel to the framework's NON-equilibrium transit physics — the substrate's GGE relic likewise never reaches thermal equilibrium (Ordered Veil; though the framework's "GGE never thermalizes" headline is RETRACTED-S39 / atlas-04 T3 BROKEN, the diabatic transit-freeze survives). Smolin's anti-equilibrium argument is GEOMETRIC/PARTICLE-class, not substrate, but the structural resonance (decisive non-equilibrium ⇒ semiclassical-equilibrium calc invalid) is notable.

---

## Paper 17 — Poplawski (2025), *Black Holes in the Expanding Universe* [2405.16673v3, CQG 42(6) 065017; gr-qc]

**Core claim (a SELF-CONSISTENCY / no-go-then-fix analysis).** The standard McVittie metric **does NOT describe a physical black hole in an expanding FRW universe** because its curvature scalar and pressure DIVERGE at the event horizon unless `Ḣ=0`. Poplawski extends McVittie to an **inhomogeneous scale factor** `a(τ,ρ)` and shows the infinities are removed by imposing, at the horizon, constancy of the Hubble parameter plus a constraint on the scale-factor gradient. Consequence: **all centrally-symmetric BHs have the SAME horizon Hubble parameter `H_hor = (Λ/3)^{1/2}`, and black holes do NOT grow with the expansion of the universe.**

- **McVittie metric & its pathology.**
  ```
  ds² = ((1−M)/(1+M))² dτ² − (1+M)⁴ a²(dρ² + ρ²dΩ²),   M(τ,ρ)=Gm/(2aρ)      (Eq. 1)
  κϵ = 3H²,   κp = −3H² − 2Ḣ (1+M)/(1−M)      (Eq. 2);  Ricci = −12H² − 6Ḣ(1+M)/(1−M)
  ```
  Event horizon at `M=1` (`ρ_hor = Gm/2a`, Eq. 8). The `Ḣ/(1−M)` term ⇒ **pressure and Ricci scalar diverge at the horizon unless `Ḣ=0`** (constant H ⇒ exponential / de Sitter expansion only). So McVittie is finite ONLY for a static or pure-de-Sitter universe — **not the real, matter-filled, `Ḣ≠0` universe**. This is the central self-consistency tension Poplawski identifies.
- **Equivalence to Kottler (Schwarzschild–de Sitter).** Radial transform `r = aρ(1+M)²` (Eq. 4) → metric with `f(τ,r) = 1 − 2Gm/r − H²r²` (Eq. 5). If `H` is constant, a further time transform (Eq. 6) diagonalizes to the **Kottler metric** `ds² = (1 − 2Gm/r − Λr²/3)dt² − dr²/(...) − r²dΩ²` (Eq. 7), `Λ = 3H²`. "Because of the equivalency to the Kottler metric, the McVittie metric with constant H does not provide any new information" and "does not describe a black hole in the real Universe with the presence of matter." Only time-varying `H` is of interest — but that is exactly what diverges.
- **The fix — inhomogeneous scale factor (Tolman embedding).** Generalize to `a(τ,ρ)` (Eq. 16), a special case of the Tolman metric. Define `H(τ,ρ) = (∂lna/∂τ)_ρ` (Eq. 18, inhomogeneous Hubble), `F(τ,ρ) = (∂lna/∂ρ)_τ` (Eq. 19, scale-factor gradient). Field equations Eqs. 21–24 give inhomogeneous, anisotropic `ϵ, p_r, p_t, S`. **Regularity at the horizon requires** `Ḣ_hor = 0` (Eq. 25) AND `(F/ρ + F')_hor = 0` (constraint on the gradient).
- **Special-case solution.** `F/ρ + F' = 0 ⇒ F = A(τ)/ρ` (Eq. 26) ⇒ scale factor `a(τ,ρ) = B(τ) ρ^{A(τ)}` (Eq. 27). The regularity condition becomes a relation between `A`, `B` (Eq. 30). The `Ḣ/(1−M)` indeterminacy (0/0) is resolved by L'Hôpital (Eq. 31) and is **finite** because `(lnB)·· `is finite and `B ≫ Gm`. Requires `|A(τ)| ≪ 1` (Eq. 32; near-homogeneity) and `A → 0` as `τ → ∞`.
- **The universal horizon-Hubble result (verbatim spirit):**
  ```
  H_hor = (Λ/3)^{1/2}      (Eq. 34),  independent of the black hole's mass.
  ```
  This equates two boundary values of `H` at opposite ends of the interval (horizon `ρ_hor` and future infinity `τ→∞`); it is consistent with the horizon FORMING only after infinite cosmic time (gravitational time dilation). As `τ→∞`, `H → (Λ/3)^{1/2}` (with Λ) or `H → 0` (without), and `Ḣ → 0` in both cases — "the regularization of an event horizon occurs in the same time limit as its formation."
- **No-growth conclusion.** Near the horizon (where `a` does not vary with `ρ`) the metric transforms to Kottler (Eq. 7) ⇒ horizon radius `r_hor` (cubic `1 − 2Gm/r_hor − Λr_hor²/3 = 0`) is **constant in time**. *"A black hole does not grow with the expansion of the Universe; it can grow only as a result of accretion"* or merger. Points near the horizon recede as space expands, but the horizon size is fixed.

**Falsifiable / observational test.** Indirect but real: **explicitly contradicts the cosmological-coupling hypothesis** of Croker–Zevin–Farrah–Nishimura–Tarlé (ApJ Lett. 921, L22, 2021 = the `k~3` DE-from-BHs idea, ref [17]) that BHs grow as the universe expands (proposed to explain SMBH masses). Poplawski's result agrees with Gaur–Visser (JHEP 05, 172, 2024, ref [18]). So the paper is a **theory-side falsifier of cosmological-coupling growth**: if BHs are described by the (regularized) McVittie/Kottler geometry, they cannot be cosmologically coupled in mass. (The observational side of this debate is Farrah #15 vs Rodriguez #16 in the same folder.)

**Negative result.** The headline IS a negative result: the widely-used McVittie metric is UNPHYSICAL at the horizon for any real (`Ḣ≠0`) universe. Tension Poplawski himself acknowledges: the special-case scale factor `a = Bρ^A` is exact only if the BH is the ONLY body in the universe; for realistic settings its validity is limited to not-too-large `ρ` (other bodies averaged into the background `B(τ)`); a fully complete treatment "must use comoving coordinates to describe gravitational collapse."

**Global causal/thermodynamic structure & "universe inside a BH" consistency.** The paper is the GR-consistency check the prompt asked about: a BH embedded in expanding FRW is globally consistent ONLY if the near-horizon region effectively decouples from the global expansion (horizon `H` pinned to `(Λ/3)^{1/2}`, horizon size fixed, accretion-induced growth time-dilated to a constant `m`). This SUPPORTS the "universe-inside-a-BH" picture in the sense that the interior cosmology and the exterior horizon are mutually consistent (the horizon does not get dragged by external expansion). The closing remark ties it to Einstein–Cartan torsion: in vacuum torsion vanishes and the theory reduces to GR with these same regularizing conditions; at extreme density torsion gives the nonsingular big-bounce (the rest of the Poplawski program).

---

## Paper 19 — Gaztañaga (2026), *Cosmological Bounce Relics: Black Holes, Gravitational Waves, and Dark Matter* [2602.17702v1; **physics.gen-ph**]

**Core claim.** A new relic-generation mechanism in a bouncing ("Black Hole Universe", BHU) cosmology. Relics — black holes, GWs, and dark matter — arise through TWO channels: (i) compact objects + GWs from pre-bounce collapse that stay super-horizon and re-enter after the bounce; (ii) DM halos formed during collapse that exit the horizon and collapse to BHs upon re-entry. Proposes **"Bounce Dark Matter" (BDM)** = a population of relic black holes (and neutron stars) spanning sub-solar to supermassive masses, offering a unified origin for DM, the GW background, and early SMBH/galaxy seeds.

- **Bounce mechanism (BHU, classical GR).** High-density collapse drives a stiff equation of state; energy density saturates at a constant ground-state value `ρ_G` where `ρ̇ = 0` and `ω = −1`, saturating the null energy condition (`T_μν k^μ k^ν → 0`). Closed spatial slices (`k=+1`) violate the non-compact-Cauchy-surface assumption of Penrose's theorem, evading the singularity.
  ```
  P = −ρ²/ρ_G   (generalized Chaplygin gas, α=2)      (from Eq. 7 / [25])
  a(τ)/a_B = cosh(τ/R_B) = ½(e^{+τ/R_B} + e^{−τ/R_B})      (Eq. B4)
  ä/a = +8πG ρ_G/3 ≡ r_S/R_G³,  ρ̇_G = 0      (Eq. B1);  R_B = √(3/(8πGρ_G))
  ```
  Post-bounce `τ>0` ⇒ exponential expansion `a ∝ e^{τ/R_B}` — a **natural inflationary phase** solving horizon + flatness, ending when the fluid transitions from vacuum-domination (`p≈−ρ`) to matter/radiation. **Λ reinterpreted as a boundary effect**: `Λ = 3/r_S²` (Eq. B5), `r_S = 2GM`, so Λ reflects the total mass of the universe (`R_Λ = r_S`).
- **Halo virialization (sets compact-object formation).** Spherical top-hat in EdS virializes at:
  ```
  Δ_V = ρ_V/ρ̄ = 1 + δ_V = 2GM/(H²R_V³) = 18π² ≃ 178      (Eq. 3)
  σ_V² = 2K_V = GM/R_V ∝ M^{2/3}      (Eq. 1, virial)
  M ≃ 10¹¹ h⁻¹ M_⊙ (R_V/120h⁻¹kpc)³ (Ω_m/0.3)(1+z_V)³      (Eq. 4)
  ```
  Halos reaching `δ ≈ 200` before the bounce collapse to BHs on re-entry (far above the relativistic-collapse threshold).
- **Press–Schechter high-mass tail (verbatim):**
  ```
  dn/dM ≈ (1/√π)(M/M*)^{1/2} exp(−M/M*) ρ̄/M²      (Eq. 5)
  ```
  "extremely massive halos are rare but allowed."
- **Particle horizon across the bounce.** `r_P = a ∫dτ/a = ∫_{a_B}^a da/(Ha²)` (Eq. 8); during the bounce `r_P = R_B cosh(a/a_B) sinh⁻¹(a/a_B) ∝ τ` (Eq. 9). Only `aλ > r_P(a_G)` modes survive: `aλ_min ≃ r_P(a_G)` (Eq. 10).
- **The 90 m survival floor (the sharp number).** Cold collapse: `ρ = τ⁻²/(6πG) ≃ 3.97×10⁻¹³ (M_⊙/km³)(τ/s)⁻²` (Eq. 11). Even 1 s before the would-be singularity, `ρ ≪ ρ_NS ≃ ρ_SD ≃ 1.4×10⁻⁴ M_⊙/km³` (Eq. 12). For `M = 5×10²² M_⊙` with `ρ_G > ρ_SD`:
  ```
  1/H = R_B = √(3/(8πGρ_G)) < 90 m      (Eq. 13)
  ```
  **⇒ all perturbations / compact objects / GWs with comoving scale `λ > 90 m` become super-horizon and survive the bounce as relics.**
- **Two BDM channels (the relic-population prediction).** (i) **Horizon-reentry channel**: pre-bounce virialized halos (`δ≈200`) re-enter with `δ ∼ 200 ≫ δ_PBH ∼ 0.3–0.7`, collapsing nearly instantaneously to BHs — like PBH formation but seeded by gravitational instability, not quantum fluctuations. (ii) **Horizon-shielded channel**: compact objects (BHs/NS) formed before the bounce, encapsulated by their own horizons (or simply non-relativistic & non-interacting), pass through the hot bounce intact and reappear. **Both produce a BROAD mass spectrum** — sub-solar to supermassive — explicitly NOT monochromatic.

**Falsifiable predictions / observational tests.**
  1. **Broad (non-monochromatic) BH mass spectrum** — would enhance LIGO/Virgo binary-BH merger rates; relic BDM mergers should have clustering/formation-history differing from stellar-origin BHs.
  2. **SMBH seeds `M ∼ 10⁵–10⁸ M_⊙`** formed before the bounce, alleviating the rapid-growth tension for `z>7` billion-solar-mass quasars (the "Nature" interpretation of the M–σ relation).
  3. **CMB secondary anisotropies, NOT primary.** "Their impact on the CMB would NOT appear in primary anisotropies (the acoustic peaks at `ℓ ≲ 3000`)... due to Silk damping." Instead: arcminute-scale secondary effects — gravitational lensing of CMB photons, kSZ from moving compact objects → **excess small-scale power at `ℓ ∼ 3000` and beyond** (ACT, Simons Observatory, CMB-S4). A detected small-scale excess / anomalous lensing / kSZ = evidence for BDM.
  4. Microlensing, astrometric shifts, CMB distortions as further probes.
  5. Speculative secondaries: rotational B-modes, galaxy-spin alignments, `H₀` tension from a finite collapsing cloud carrying angular momentum.

**NON-STANDARD-CLAIM FLAGS (physics.gen-ph).** (a) Our observable universe "may itself be a relic bounce structure formed during a previous cosmic cycle" — a high-mass BHU relic. (b) `Λ = 3/r_S²` as a boundary effect of the cloud's gravitational radius (not a fundamental vacuum energy). (c) During collapse, linear perturbations grow as `δ ∝ a^{−3/2}` as `a→0` (decaying-mode-becomes-growing in the time-reversed phase) — "much faster than in an expanding universe," letting modest initial fluctuations become highly overdense by the bounce. (d) PT-conjugate quantum state, decoherence-driven classicality, odd-parity CMB power excess (ref [58]).

**Negative result.** None internal; the paper is constructive/speculative. It explicitly distinguishes BDM from inflationary PBHs (different physics: BDM is slow Newtonian violent-relaxation collapse halted far outside `r_S`, then re-entry; PBH is relativistic horizon-scale collapse, `δ_PBH ∼ 0.3–0.7` vs linear `δ_c ≈ 1.686`).

**>>> ANSWER to the cross-check: does #19 keep a scale-invariant baseline that CONTRADICTS #14's large-scale-deficit claim? <<<**
**#19 does NOT contradict #14 — it RETAINS a standard scale-invariant baseline and adds relics ON TOP.** Verbatim from #19 Appendix B (lines 962–969): *"In this scenario, **relic perturbations add to the standard scale-invariant spectrum of inflated quantum fluctuations**; they are **subdominant on large scales** (since large masses are exponentially suppressed) but could dominate on smaller scales. Consequently, PBH constraints from CMB µ-distortions, which assume Gaussian scale-invariant primordial fluctuations, do not necessarily apply to these non-Gaussian relic contributions."* And in the main text: BDM relics "form on small scales (well below galactic)," re-enter "well before recombination," and so do "NOT appear in primary anisotropies (the acoustic peaks at `ℓ ≲ 3000`)" but only in arcminute-scale SECONDARY anisotropies.

By contrast, **#14 (2204.11608) makes the OPPOSITE large-scale claim**: the BHU super-horizon perturbation spectrum has a **hard cutoff for scales `λ > 2R` (`k < π/R`)**, so it is **NOT scale-invariant on the largest scales** — #14 verbatim: *"the key difference with Inflation is that in the BHU the spectrum of incoming fluctuations have a cutoff for scales larger than `λ > 2R` (`k < π/R`), while Inflation is scale invariant in all scales. This results in an anomalous lack of the largest structures in the CMB"* — and #14 claims this large-scale deficit as a positive prediction/detection (the super-horizon cutoff at scale `H_i`).

**So there is a genuine TENSION between the two Gaztañaga papers on the large-scale spectrum** (see final-message summary for the precise framing): #14's headline large-scale signature is a deficit/cutoff at `λ>2R`; #19's stated baseline is "the standard scale-invariant spectrum of inflated quantum fluctuations" with relics only on SMALL scales and explicitly subdominant on large scales. #19 neither re-derives nor invokes #14's `λ>2R` large-scale cutoff; its sole CMB target is a SMALL-scale (`ℓ≳3000`) secondary excess. The two are mechanically compatible only if one reads #19's "standard scale-invariant spectrum" as a deliberately-simplified baseline that suppresses #14's large-scale cutoff for the purpose of the relic calculation — but as WRITTEN, #19's large-scale baseline statement contradicts #14's large-scale-deficit signature.

**Framework-relevant note.** GEOMETRIC/PARTICLE-class. The BDM relic-from-bounce structure is the GR-side cousin of the framework's GGE-relic-from-transit (both: a non-trivial relic population is the observable fingerprint of the cosmogenesis event). But the BHU bounce is a quasi-de-Sitter `cosh`-law ADIABATIC bounce at NUCLEAR density (`ρ_G > ρ_SD`, `R_B < 90 m`) — structurally OPPOSITE to the substrate's SUDDEN/diabatic supersonic transit (Mach 13.75) at the van Hove fold. (See sub-A2 for the full transit-vs-bounce adversarial comparison.)

---

# ECO DISCRIMINATORS (papers 04, 08, 15 — digested together)

These three are the horizon-vs-condensate-surface observational toolkit: a hard NEGATIVE result excluding one ECO as a specific GW remnant (#04), the echo-delay relation that turns ringdown into a Planck-scale horizon probe (#08), and the QNM spectral-instability caveat that bounds how reliably ringdown overtones can discriminate horizonless objects (#15).

## ECO-04 — Chirenti & Rezzolla (2016), *Did GW150914 produce a rotating gravastar?* [1602.08759] — THE KEY NEGATIVE RESULT

**Core claim & result.** **It is NOT possible to model the measured ringdown of GW150914 as a rotating gravastar.** The inspiral CAN be reproduced by two compact gravastars (their compactness is compatible), but the RINGDOWN eigenfrequencies of rotating gravastars do not overlap the GW150914 ringdown.

- **Why a gravastar is excluded as the remnant (the mechanism):** Gravastars (Mazur–Mottola "gravitational vacuum condensate stars") have a de Sitter core + thin stiff-matter shell; parameter space = total mass `M`, compactness `µ ≡ M/r₂`, shell thickness `δ ≡ r₂−r₁`. Their `ℓ=2=m` axial QNM eigenfrequencies `(σ_r, σ_i)` are **always distinct from the Schwarzschild/Kerr value**, independent of compactness and thickness (Fig. 2). Even ultra-thin gravastars (`δ/M = 0.0025`, surface only **4% in radius outside the horizon**) have a ringdown distinguishable from a BH over a dynamical timescale (Fig. 1).
- **Rotating-gravastar QNM model (the approximation used):** lacking a full rotating-gravastar perturbation theory, they correct nonrotating gravastar modes with rotating-compact-star f-mode relations:
  ```
  σ_r ≃ σ_{r,0}(1 + m ε σ'_r) + O(ε²)      (Eq. 1)
  σ_i ≃ σ_{i,0}(1 + m ε σ'_i) + O(ε²)      (Eq. 2)
  ε ≡ Ω/Ω_K ≃ J/(MR²)/Ω_K ≃ χ√µ      (Eq. 3),  χ ≡ J/M²
  ```
  They extrapolate the neutron-star `σ'_{r,i}(µ)` from `µ ∈ [0.10, 0.24]` to gravastar `µ ∈ [0.4, 0.5)`, with `χ = 0.68` (the GW150914 final-spin prior).
- **The exclusion.** GW150914 ringdown ⇒ Kerr with `a = 0.68^{+0.05}_{−0.06}`, `M = 62.2^{+3.7}_{−3.4} M_⊙` (ref [17/31]). The shaded region spanned by rotating-gravastar eigenfrequencies (bounded by `µ=0.40, χ=0.62` and `µ=0.48, χ=0.73`) **does NOT overlap** the Kerr `a=0.68` ringdown region (Fig. 3), and **does NOT overlap** the 90%-confidence damped-sinusoid ringdown contours (`t₀ = t_M + 1,3,5,7` ms) nor the IMR best-fit contour (Fig. 4). Conclusion holds for `µ ≤ 0.48` and extends to larger compactness; a larger `χ` (gravastars merge earlier) would only push curves further apart.
- **Compactness lower bound (cited):** the inspiral touching argument ⇒ radii < 175 km ⇒ `µ > G/c²(35M_⊙)/(175km) ∼ 0.3` (footnote 1).

**Falsifiable content.** This IS a falsification-in-action: a specific horizonless model (rotating gravastar) is excluded as the GW150914 remnant by ringdown QNMs. **Caveats the authors flag (the negative result's own limits):** (1) no full rotating-gravastar perturbation theory exists — the rotation correction is an extrapolation from neutron stars; (2) the conclusion applies to gravastars whose surface is at a SMALL but NOT infinitesimal distance from the horizon (no contradiction with Cardoso–Franzin–Pani [32], whose early-time signal matches a BH for infinitesimal `ϵ`). The proper rotating-gravastar analysis is called for as future work.

**Framework note.** Directly relevant to the framework's horizons-as-acoustic-phase-boundaries reading: a condensate-surface remnant (gravastar-like) would imprint a DISTINCT ringdown — but #04 shows the specific gravastar model is already excluded for GW150914. (Framework's own GW falsifiers are RETIRED per the index note; this is GR-side discrimination, GEOMETRIC class.)

## ECO-08 — Cardoso & Pani (2017), *Tests for the existence of horizons through GW echoes* [1709.01525]

**Core claim.** "BHs exist" is fundamentally **unfalsifiable**, but **alternatives can be ruled out or confirmed with a single observation** (Popper's black swan). GW echoes are the smoking gun: any horizonless ultracompact object with a "clean photosphere" produces a train of echoes whose detection would be evidence for new physics at (potentially Planckian) the horizon scale.

- **ECO parameterization.** Effective surface at `r₀ = r_g(1 + ε)`, `ε ≪ 1` (Eq. 1, `r_g = 2GM/c²`); proper distance to `r_g` scales as `√ε`; all observables depend on `log ε`. Planckian corrections: `ε ∼ 10⁻⁴⁰`.
- **Darkness condition.** Injected energy is radiated over longer than a Hubble time (ECO looks dark like a BH) when `ε ≪ 10⁻¹⁶ (M/10⁶M_⊙)` (Eq. 2).
- **Photosphere classification — the ClePhO threshold (load-bearing).** Light/GWs orbit at the photosphere `r = (3/2)r_g`; the circular orbit is unstable on `∼ 3√3 r_g/2c ≈ 2.5 r_g/c`. Requiring 3 e-folds to dissipate >99.7% of a pulse before it returns from the surface ⇒
  ```
  ε ≲ 0.0165      (Eq. 3)
  ```
  Objects with `ε ≲ 0.0165` are **ClePhOs** (clean photosphere objects); their EARLY-time ringdown is identical to a BH, but LATE-time they show surface signatures. UCO = ultracompact object (has a photosphere); ClePhO = the subclass satisfying Eq. 3.
- **Prompt ringdown frequencies (photosphere modes):**
  ```
  f = 12.07 (M_⊙/M) kHz,   τ = 55.37 (M/M_⊙) µs      (Eq. 4)
  ```
- **THE ECHO-DELAY RELATION (the central tool):**
  ```
  τ_echo ∼ (2 r_g / c) |log ε|      (Eq. 5)
  ```
  **The LOGARITHMIC dependence is the crucial point**: even Planckian corrections (`ε ∼ 10⁻⁴⁰`) give an OBSERVABLE (not astronomically large) echo delay, because `|log ε|` grows only logarithmically. The first echo carries the SAME high frequency content as the prompt ringdown (the burst is generated at the photosphere); subsequent echoes have progressively LOWER frequency content (Fig. 2). The early-time signal is identical to a BH up to `∼ (r_g/c)|log ε|` (causality), after which trapped waves leak out as echoes. **This converts the echo delay into a direct measurement of the surface location `ε` — i.e. a horizon-scale probe reaching Planck scales.**
- **Detectability.** Echoes detectable separately from the main burst (threshold `ρ=8`) require prompt-ringdown SNR `ρ_prompt ≳ 80/√(γ_echo(%))`, where `γ_echo` = energy ratio (first echo / prompt). For `γ_echo = 20%`, **LISA sees ≥1 event/year** even on pessimistic population models; Einstein Telescope / Voyager-class detectors can also distinguish ClePhOs from BHs.

**Other horizon null-tests (precision physics, the "no smoking gun needed" route):** (i) **No tidal heating** — horizons absorb/amplify GWs; ECOs do not, so GW phase measures surface absorption (LISA reaches Planck scales). (ii) **Nonzero tidal Love numbers** — BH Love numbers are EXACTLY ZERO; ECO Love numbers scale as `log ε`, giving a null test. (iii) **Different multipole structure** — spinning ECO multipoles differ from Kerr. (iv) **Statistical absence of high spin** — the ergoregion instability depletes angular momentum: a spinning ECO with `χ ≳ 0.2`, `ε∼10⁻⁴³` has instability timescale `τ < 3×10⁵[M/60M_⊙]` s; a population of slowly-spinning objects across all masses would indicate horizonlessness.

**Stability NEGATIVE results (which mimickers survive).** (a) Buchdahl limit `r_g/r₀ < 8/9` ⇒ isotropic constant-density fluid stars can NEVER be ClePhOs. (b) Nonspinning UCOs have logarithmically-slowly-decaying modes ⇒ conjectured NONLINEAR (Dyson–Chandrasekhar–Fermi-type) instability; endstate unknown (mass ejection OR collapse to BH). (c) Spinning UCOs/ClePhOs with ergoregions have a LINEAR ergoregion instability (final state a slowly-spinning ClePhO) — but for ClePhOs the timescale is parametrically long and may be quenched by (model-dependent) dissipation. (d) Intriguing hint: classical UCO instabilities may BE the analog of Hawking radiation, with a smooth transition to the BH limit.

**Falsifiable content.** Strong and forward-looking: the `τ_echo ∼ (2r_g/c)|log ε|` relation is a concrete, doable test (LISA/ET) that probes the horizon to Planck scale. Asymmetry of falsifiability is the paper's thesis: "BHs exist" is unfalsifiable, but a single echo / Love-number / tidal-heating detection can rule alternatives in or out.

**Framework note.** This is the laboratory the framework's "condensate surface, not absorbing horizon" reading would be tested in: a condensate boundary ⇒ partial reflectivity ⇒ echoes + nonzero Love numbers + no tidal heating. GEOMETRIC/PARTICLE class; the framework's GW-channel falsifiers are RETIRED (walls=0 EXACT, S96), so this informs GR-side discrimination, not a live framework gate.

## ECO-15 — Destounis, Malato Corrêa, Macedo & Panosso Macedo (2025), *Spectral instability of horizonless compact objects within astrophysical environments* [2509.16310v2]

**Core claim.** Modeling a matter environment as a small Gaussian "bump" (the "flea") outside the light ring (the "exotic elephant") of a purely-reflective ECO: **environmental bumps destabilize the FUNDAMENTAL QNM of LOOSELY-compact ECOs, but the fundamental mode of ULTRA-compact ECOs is remarkably ROBUST. OVERTONES, however, are spectrally unstable in all cases. Crucially, spectral instability does NOT become a modal (dynamical) instability — ECOs are "spectrally fragile yet modally robust."**

- **Setup.** ECO surface at `r_s = r_h + E`, `E ≪ 1` (Eq. 1); `E/r_h` = compactness control (smaller `E` ⇒ more compact). Exterior is Schwarzschild; Regge–Wheeler potential:
  ```
  V = f(r)/r² [ ℓ(ℓ+1) + (1−s²) r_h/r ],   f(r)=1−r_h/r      (Eq. 5)
  ```
  Surface boundary condition = **Dirichlet (perfect reflection)** `Φ(t, r*_s) = 0` (Eq. 10). Master equation `d²ϕ/dr*² + (ω² − V)ϕ = 0` (Eq. 11).
- **Environment model (the "flea on the elephant").** Perturbed potential:
  ```
  V_ε = V + ε V_bump      (Eq. 14)
  V_bump(r* − a₀) = exp[ −(r*−a₀)²/(2ϱ) ]      (Eq. 15, Gaussian at r*=a₀, width ϱ)
  ```
  Fiducial: `ε = 10⁻⁶`, `ϱ = 1`, `ℓ=2`. Methods: hyperboloidal pseudospectral (Chebyshev, N=300) + continued-fraction (Leaver) cross-check (agreement to `O(10⁻⁶)`, Table I).
- **Result 1 — compactness alone does NOT destabilize.** Varying `E/r_h` from `10⁻³` to `0.5` migrates modes CONTINUOUSLY (Fig. 3); no spectral instability. Interpretation: the ECO is ALREADY a "dramatically destabilized spectral set" relative to its Schwarzschild BH counterpart (the reflective boundary condition is a huge, discontinuous modification); once the new QNMs arise, they are stable to small changes in the boundary location.
- **Result 2 — the environmental bump DOES destabilize (the main finding).** With the bump:
  - Fundamental mode of `E/r_h = 10⁻³` (ultra-compact) and `10⁻²` (compact): **practically UNCHANGED** regardless of bump position `a₀` — **spectrally STABLE fundamental QNMs**.
  - Fundamental mode of `E/r_h = 10⁻¹` (loosely-compact): MIGRATES by `O(10⁻¹)` (real) and `O(10⁻²)` (imag) beyond `a₀ ∼ 25 r_h` — disproportionate to the `O(10⁻⁶)` bump ⇒ clear **spectral instability**. Driven by a SECONDARY trapping cavity (between light ring and bump) ⇒ "exterior trapped modes."
  - **Overtones are unstable in ALL cases** (`E/r_h = 10⁻¹` and `10⁻²` first overtones both destabilize). Ultra-compact (`10⁻³`) first overtone is robust, but "there should be some overtone beyond which the spectral instability transpires."
- **Result 3 — the OVERTAKING INSTABILITY (the qualitative phenomenon).** For `E/r_h = 10⁻¹`, beyond `a₀ ∼ 28 r_h`, the destabilized first overtone OVERTAKES the fundamental mode (its imaginary part becomes smallest in absolute value) and becomes the new **"perturbed" fundamental mode** (Figs. 6–7). This repeats: successive exterior-trapped overtones overtake as `a₀` increases. Phase-space (Fig. 8): e.g. `E/r_h = 0.3` ⇒ fundamental overtaken at `a₀ ≳ 15 r_h`; the MORE compact the ECO, the FARTHER the bump must be to destabilize. *"Loosely-compact ECOs ... are more prone to spectral instability due to environmental bumps than ultra-compact ones."*
- **Result 4 — spectral ≠ modal instability (the key caveat for discrimination).** Section C: ultra-compact ECO long-lived modes sit arbitrarily close to the real axis, but tentative searches for mode destabilization (crossing into the unstable upper-half plane) were **"inconsequential"** — fundamental long-lived interior/exterior modes are "essentially pinned at their spectral points." Same result for `ℓ=10` (≥3 very long-lived modes). *"Environmental effects, while able to amplify existing spectral instabilities, are NOT capable of inducing genuine modal instabilities. This result establishes a clear dichotomy: ECOs can be spectrally fragile yet modally robust."* The pseudospectrum protrusion into the unstable half-plane (suggested in [185]) does NOT indicate true modal instability — analogous to hydrodynamic laminar→turbulent transition where eigenvalues say stable but pseudospectrum/transient growth say otherwise.

**What this means for using ringdown to discriminate horizonless objects (the falsifiability bearing).**
  1. **Fundamental-mode spectroscopy of ULTRA-compact ECOs is ROBUST** to astrophysical environments — the dominant ringdown mode is a reliable discriminator (the bump must be astrophysically-irrelevantly far to move it). This is GOOD NEWS for using the fundamental QNM as a horizon test.
  2. **Overtone-based spectroscopy is FRAGILE** — overtones restructure (overtaking instability) under environmental bumps, in ways INVISIBLE to a purely modal analysis. Any BH-spectroscopy program relying on overtone hierarchies must account for environmental spectral instability.
  3. **Spectral instability does NOT mean the object falls apart** (no modal instability) — so a destabilized overtone spectrum is a measurement-systematics problem, not an existence argument against the ECO.
  4. Spectral-instability imprints "usually manifest in uncharted, late-time territories, where current detectors do not possess the required sensitivity" — so present-detector prompt-ringdown discrimination is relatively safe; the issue bites for LISA/3G late-time precision.

**Caveats/limits the authors flag (NEGATIVE-result honesty).** Idealized: spherically-symmetric, perfectly-reflective surface, smooth Gaussian bump, no rotation. "Nature abhors exactly spherically-symmetric configurations" — Kerr/rotating-ECO spectra are richer and only preliminary pseudospectra exist; rotation could introduce spectral-to-modal pathways not eliminated here. A lower-regularity bump or tunable surface reflectivity might behave differently. Even small partial absorption stabilizes the (otherwise ergoregion-unstable) rotating system.

**Framework note.** GEOMETRIC/PARTICLE class. Robust fundamental-mode + fragile-overtone is the relevant bound for any future substrate-side compact-object falsifier (per `inheritance-falsifier-protocol.md`): a substrate "condensate surface" discriminator should target the FUNDAMENTAL ringdown mode (environment-robust), not overtone hierarchies (environment-fragile). The "spectrally fragile yet modally robust" dichotomy parallels the framework's own pseudospectrum/non-modal cautions (Kitaev quantum-chaos integrability work, `⟨r⟩=0.367`).

---

## Cross-corpus synthesis (one paragraph)

Two structurally orthogonal threads. **BH-cosmology thread (#01, #02, #17, #19):** universe-from-BH-interior is internally consistent as GEOMETRY (#01 topological flatness, #17 horizon-Hubble pinning shows interior/exterior mutual consistency and NO cosmological growth), the bounce leaves a relic population that is observationally testable (#19 BDM: broad BH mass spectrum, small-scale CMB secondary excess, SMBH seeds), and the whole landscape program can be made falsifiable WITHOUT anthropics (#02 CNS, neutron-star mass ceiling). **ECO thread (#04, #08, #15):** the GR-side observational toolkit for horizon-vs-surface — a specific gravastar is already excluded for GW150914 (#04), echoes turn ringdown into a `|log ε|` Planck-scale horizon probe with LISA reach (#08), and fundamental-mode spectroscopy of ultra-compact objects is environment-robust while overtones are fragile (#15). All are GEOMETRIC/PARTICLE-class laboratory-IN models; the framework's substrate transit (first-order van Hove, supersonic, diabatic) is logically prior and mechanistically distinct from every bounce here, and the framework's own GW falsifiers are RETIRED — so this corpus informs GR-side discrimination and the structural-analogy map, not a live framework gate.
