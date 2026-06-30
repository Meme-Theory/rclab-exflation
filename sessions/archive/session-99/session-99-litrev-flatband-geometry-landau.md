# Session 99 Synthesis: Flat-Band Quantum Geometry / Multiband BdG Laboratory Platforms (Group G7)

**Date**: 2026-06-04
**Agent**: landau-condensed-matter-theorist (Landau)
**Source Documents**:
- `downloads/research-sweep-s99/flatband-quantum-geometry/00-INDEX.md` (10 fetched-text paper summaries; primary source)
- `downloads/research-sweep-s99/flatband-quantum-geometry/01..10_*.pdf` (PDFs beside the index, spot-verification only)
- Canonical anchors via knowledge MCP (`search_knowledge`, `get_constant`, `trace_entity`) — enumerated inline

---

## I. Session Outcome

This is a literature-sweep synthesis (NO new computation, NO gate verdicts, NO registry edits). The ten G7 papers saturate the framework's strongest-evidenced laboratory channel — the quantum-metric superfluid-weight bridge — with 2024–2026 theory and two landmark *Nature* (2025) measurements. The decisive structural finding of this review is a **registry-slot labeling correction the index propagates and the synthesis must surface**: the index's channel legend assigns the Peotta–Törmä integrated-quantum-metric-trace bridge `R_geom = ∫_BZ Tr g_ab^(P0) d^d k` to **§VII.W**, but canonical (`atlas-07-permanent-results`, `permanent-results-registry.md`) shows §VII.W proper is the **HP parity-grading orthogonality of HP_*(A_F)** theorem (Pillar III internal cohomology; volovik PRIMARY + connes CO-AUTHOR; PERMANENT), while the **R_geom quantum-metric cross-pillar bridge is §VII.AF.1.OP-PROJ** (S87; substrate-IS = Pillar III HP^1 cohomology, laboratory-IN = Pillar IV Peotta–Törmä BZ-trace, bridge map = HKR). The ten papers' relevance is real and substantial; the slot label they attach to it is wrong. With that correction in hand, papers 03/06/09/10 independently confirm the **structural choices** §VII.AF.1 already made (BdG-state projector; non-Abelian trace; the geometry-dominated stiffness is measured), and papers 02/05/08/04 supply laboratory templates for the Leggett-channel DM lifetime falsifier, the MCT-3 Caroli–Matricon ladder-asymmetry falsifier (§VII.W-3.LAB), the van-Hove-fold transit, and the flat-vs-dispersive channel hierarchy respectively. No framework state changes; the constraint map sharpens at the §VII.AF.1 laboratory-IN element and at four falsifier rows.

---

## II. Key Results

### Result 1 — Registry-slot identity correction: the R_geom bridge is §VII.AF.1.OP-PROJ, not §VII.W

**Result**: §VII.W = HP parity-grading orthogonality of HP_*(A_F) (Pillar III internal; PERMANENT). §VII.AF.1.OP-PROJ = the cross-pillar bridge R_universal = ⟨[φ_g^sym], [Ch(P_0(τ_fold))]⟩ ≡ ∫_BZ Tr g_ab^(P0)(k; τ_fold) d^d k (substrate-IS Pillar III HP^1 ↔ laboratory-IN Pillar IV Peotta–Törmä trace; HKR bridge map). **Classification: GEOMETRIC** (spectral-triple cohomology + quantum-metric trace; the fabric, not its excitations).

The index's channel legend (line 5) reads "§VII.W = Pillar III↔IV cross-pillar bridge ... R_geom = ∫_BZ Tr g_ab^(P0) ... first registered bridge, R_geom→0.0950 PASS via §VII.AF three-level ladder." Canonical disambiguation (knowledge MCP):
- `atlas-07-permanent-results`: **§VII.W** | "First Cross-Pillar Bridge Theorem (Pillar III ↔ Pillar IV; **HP parity-grading orthogonality of HP_*(A_F)**)" | S86 W-5 | volovik PRIMARY + connes CO-AUTHOR | PERMANENT.
- `permanent-results-registry.md`: "**W-5 §VII.AF.1 instance #1** anchors: substrate-IS pillar = Pillar III (HP^1 cohomology); laboratory-IN pillar = Pillar IV (Peotta–Törmä continuum BZ-trace); bridge map = H[KR]". The `.OP-PROJ` suffix is canonical (`§VII.AF.1.OP-PROJ`), marking the operator-projection (algebra-side, algebra-INVARIANT) reading per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`.
- `s86-hp1-cohomology-quantum-metric-bridge.md` carries the equation `R_universal ≡ ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k (V1 claim)` with anchor `eps_H_HP1_norm = 16.197719` (`get_constant` confirms the value; no PROVENANCE entry).

The two are not interchangeable. §VII.W is a *grading-orthogonality* statement (even-grading regulator-weighted Mellin moments cannot decode odd-grading HP^1 content — the W17 parity-blindness wall is its companion). §VII.AF.1 is the *integrated-trace bridge* whose laboratory-IN target is the Peotta–Törmä quantum metric. All seven quantum-metric papers (01/03/04/06/07/09/10) bear on **§VII.AF.1**, not §VII.W. This is a `feedback_framework-hygiene.md` "index is an idea-generator, not a register" instance: the candidate-validation content is sound, but any carry-forward must re-anchor to §VII.AF.1 before landing. The "R_geom → 0.0950 PASS" the index cites is the §VII.AF three-level-ladder Level-3/Level-2 ratio (match/envelope = 0.0950, i.e. the empirical anchor sits 10× inside the L^{-3} algebraic envelope at L_max=10) — that part is correctly attributed to the §VII.AF ladder.

### Result 2 — Porlles–Chen quasihole metric independently confirms the BdG-projector choice in §VII.AF.1 (paper 03)

**Result**: The diamagnetic-relevant quantum metric is the quasihole/BdG-state quantum metric, not the normal-state band metric — confirming §VII.AF.1's use of the BdG projector P_0 on (A_K, H_K, D_K). **Classification: GEOMETRIC.**

Porlles–Chen (arXiv:2505.17349) generalize the geometric account of superfluid weight from flat-band-only to any s-wave superconductor of arbitrary band structure, and identify the controlling object as the **quasihole quantum metric of the superconducting state** (overlap of fully antisymmetric quasihole states), written in London form as the momentum integral of quantum-metric elements times quasiparticle energy. Substrate-first reading: §VII.AF.1's bridge observable is built from the BdG projector P_0 — a superconducting-state (quasihole) projection on the spectral triple, NOT a normal-state band projection. Porlles–Chen reach the same conclusion laboratory-side. This closes a potential ambiguity in the §VII.AF.1 → §VII.AF anchor chain: had the physically correct integrand been the normal-state metric, the bridge would have targeted the wrong object. Their site-resolved "superfluid weight marker" is the laboratory analog of the finite-L Hochschild-pairing local decomposition — both are local resolutions of the same BZ-integrated geometric invariant. This is a structural-consistency confirmation, not a numerical gate: it tells us §VII.AF.1's projector choice was correct, which the framework had asserted on spectral-triple grounds (the BdG sector is the physical superconducting-state projection) and now has laboratory corroboration for.

### Result 3 — Chen–Karki–Hosur non-Abelian Tr[R_μν] is the algebra-correct object for A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) (paper 06)

**Result**: For N degenerate bands, the geometric superfluid weight is D^QM_μν ∝ ∫_BZ Tr[R_μν], R_μν = Re of the non-Abelian QGT, and Tr R ≠ Σ(per-band Abelian QMs) because inter-band-within-degenerate-subspace terms survive. Measured geometric fractions: ≈20% (MoS₂), ≈50% (TiSe₂). **Classification: GEOMETRIC.**

This is the most structurally apt sharpening for the framework's *specific* algebra. The canonical substrate algebra is A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) (`get_constant`/MEMORY: AZ class BDI, KO-dim=6) — intrinsically **non-Abelian and degenerate** (the ℍ and M₃(ℂ) summands carry matrix-valued, U(N)-structured fiber content; the Peter-Weyl sectors of D_K are degenerate, e.g. the (0,0) BCS sector B3 mult 3 / B2 mult 4 / B1 mult 1×2). The Abelian single-band quantum metric is therefore the *wrong* idealization for the substrate fiber; §VII.AF.1's `Tr g_ab^(P0)` is already a trace over a projector, and Chen–Karki–Hosur's `Tr[R_μν]` is the faithful non-Abelian realization. The non-additivity Tr R ≠ Σ(per-band) mirrors the framework's permanent structural fact that inter-sector coherence (Leggett/GGE physics) is not reducible to single-sector contributions — D_K is block-diagonal by Peter-Weyl (Wall 2, MEMORY), but the *quantum-geometric* trace over a degenerate sector still carries off-diagonal-within-sector content. The 20%/50% measured fractions establish that the non-Abelian trace object is physically substantial and extractable in degenerate-band systems matching the substrate's matrix-algebra structure. Note the sign/positivity anchor: D_geom from interband transitions is ≥ 0 by Cauchy–Schwarz (`s86-r-dual-pathway-bk-array-and-nT.md`), consistent across the canonical record.

**Caveat (regime of validity).** Chen–Karki–Hosur derive D_μν = D^N_μν + D^QM_μν *near T_c* for conventional s-wave pairing in a time-reversal-symmetric system, via the sewing matrix B_k and a small-q BdG expansion. The substrate's AZ class is BDI (T²=+1), which is time-reversal-symmetric and admits the sewing-matrix construction; the near-T_c regime is the appropriate one for the order-parameter-onset (Landau-expansion) physics §VII.AF.1 lives in. The mapping is regime-consistent.

### Result 4 — Tanaka MATBG (T²) + Banerjee MATTG (T-linear): the two-platform empirical anchor (papers 09/10)

**Result**: MATBG superfluid stiffness measured (cQED) to be geometry-dominated — exceeds Fermi-liquid prediction; power-law T-dependence; GL-consistent quadratic current dependence (Tanaka, Nature 638, 99). MATTG stiffness ρ_s(T) linear-in-T at low temperature → nodal gap; linear ρ_s(0)↔T_c correlation (Banerjee, Nature 638, 93). **Classification: GEOMETRIC** (the measured object is the integrated quantum metric; PHONONIC by inheritance — the lab condensate is a child of the substrate fiber).

Tanaka et al. is the measured datum behind §VII.AF.1's laboratory-IN element. The stiffness exceeds the band-velocity (Fermi-liquid) prediction **because the geometric (quantum-metric) contribution carries it** — this is the empirical confirmation that R_geom is not a formal device but a measured, anomalously-large stiffness, supplying the Level-3-analog anchor the §VII.AF three-level ladder requires. The GL-consistent quadratic current dependence is substrate-resonant: the framework treats the order parameter and supercurrent in a Ginzburg–Landau free-energy language inherited from the same a_2/a_4 spectral-moment structure (the canonical Landau form F = F_0 + a_0(T−T_c)η² + b η⁴, MEMORY; GL κ = λ/ξ). Banerjee's MATTG T-linear ρ_s on a second, independent (trilayer, nodal) platform strengthens the laboratory-IN element beyond a single material: the differing thermal scaling (T² vs T-linear) is the laboratory readout of different gap-node structures projected from the same substrate geometric object — a platform-robustness cross-check, not a single-material coincidence. The dual-platform structure is exactly what the cross-pillar-bridge anatomy wants for a Level-3 anchor that is not platform-fragile.

**Dimensional/sign discipline.** Tanaka's "stiffness exceeds Fermi-liquid prediction" is a magnitude statement: D_s = D_s^conv + D_s^geom with D_s^geom ≥ 0 (Cauchy–Schwarz), and the measured D_s exceeding D_s^conv (the band-curvature Drude weight) requires D_s^geom > 0 and comparable-or-larger than D_s^conv. This is the *correct direction* for §VII.AF.1's claim that the geometric channel is real and dominant at the magic angle. It does NOT by itself establish the framework's separate "flat bands squeeze less" hierarchy (Result 6) — that hierarchy is about the *substrate's full spectrum*, where the dispersive acoustic channel dominates the geometric one; the two statements are scale-separated and must not be conflated (see Result 6 caveat).

### Result 5 — Hirobe node-resolved D^geom(T): a falsifiable thermal probe of the §VII.AF.1 bridge object (paper 01)

**Result**: Node-and-band-resolved power laws for the geometric superfluid weight D^geom_μν(T), built from the band-resolved quantum metric g^nm_μν(k) = 2 Re⟨u_n|∂_μ u_m⟩⟨∂_ν u_m|u_n⟩; flat-band geometric weight obeys strictly *weaker* power laws than the dispersive-band geometric weight at equal node structure (full gap → e^{−Δ/T}; line node → T^{1/(l+1)}; with nodal-line crossing → −T^{1/(l+1)} ln T). MATBG T² → point/line-node gap; MATTG T-linear → flat-band-crosses-Dirac with K-point node. **Classification: GEOMETRIC.**

Hirobe et al. promote §VII.AF.1's static T=0 integrated trace to a **temperature-resolved, node-resolved observable** carrying the same band-resolved g^nm_μν(k) integrand. This is the laboratory route to thermally probing whether the substrate's quantum-metric trace, given a thermal handle, reproduces the *flat-band* geometric power law rather than the conventional Fermi-liquid law — a falsifiable consequence of §VII.AF.1's bridge being a geometric (not band-velocity) object. The flat-vs-dispersive scaling separation (flat strictly weaker than dispersive at equal node structure) is the laboratory echo of the framework's flat/geometric channel being sub-dominant to the dispersive/acoustic channel, and a place to test its *sign*. The Hirobe node-classification table directly assigns the Tanaka/Banerjee measurements to gap-node structures, which is the bridge between Result 4's two-platform anchor and the node-discriminant the substrate sector geometry must reproduce.

### Result 6 — Penttilä flat-band-ratio moderation vs the framework's flat-vs-dispersive hierarchy (paper 04)

**Result**: Within finite-T DMFT, the flat-band ratio and quantum metric remain good predictors of superconductivity (order parameter, T_c, superfluid weight, BKT T) outside the idealized isolated-flat-band + uniform-pairing limit, but the geometric channel is *moderated* by the flat-band ratio in non-isolated settings; BKT temperature well-guided by T=0 superfluid weight + flat-band ratio. **Classification: GEOMETRIC.**

Penttilä et al. provide the laboratory framework for the comparison the framework's "flat bands squeeze less" result asserts: the flat-band ratio quantifies how much band content is flat vs dispersive, and the superfluid response tracks it. Substrate-first: the substrate's Peter-Weyl sector structure of D_K determines an intrinsic flat-vs-dispersive partition; a modified Lieb lattice's tunable flat-band ratio is an inheritance-child realization. The finding that the geometric channel stays predictive but is moderated by the flat-band ratio is the laboratory analog of the substrate's acoustic dominance.

**CAVEAT — the "37×" figure is the index's, not a canonical pin.** The index repeatedly cites "B1 acoustic dominates by factor 37." Knowledge-MCP search does NOT surface a canonical "37×" constant. What IS canonical: (i) the squeeze amplification `F_squeeze_bare = 5.4060e+01` (54.06×, `s74_as_from_bogoliubov_output.txt`); (ii) the band identities E_B1 = 0.819 (1 mode, ground tone / acoustic) and E_B2 = 0.845 (4 modes, flat optical band = the van Hove singularity, `session-38-naz-tesla-workshop.md`); (iii) the partition-stability result that B2 (flat band) carries the lowest gap-to-temperature ratio K_R5 = 1.922 (`session-83-volovik-synthesis.md`). The specific "37×" B1/B2 dominance figure is plausibly a derived ratio but I could not pin it to a canonical source in this pass; it is carried here as the **index's figure pending canonical-pin verification** (CF V.6). The structural claim (acoustic dispersive channel dominates the flat geometric channel in the substrate's full spectrum) is canonical in direction; the exact multiplier is not yet verified.

### Result 7 — Hou necklace-CdGM ±l phase-resolved spectroscopy: experimental template for the MCT-3 falsifier (§VII.W-3.LAB) (paper 05)

**Result**: STM/STS at 0.4 K resolves a "necklace-like" vortex-bound-state pattern in KCa₂Fe₄As₄F₂ (K12442; T_c ≈ 33.5 K, Δ₀ = 5.2 meV, lowest VBS ≈±1.0 meV), explained as selective off-shell two-level interference between CdGM states of opposite angular momentum ±l; local DOS ρ ∝ [1 + |α_l|² + 2|α_l| cos(2lφ + φ_0l)]|ψ_l|² with single fit parameter α_l; first experimental measurement of the *phase* (angular momentum l) of CdGM states; demonstrated ladder-ratio tunability 1:3:5 → 1:2:3. **Classification: PARTICLE** (representation-theoretic content of the BdG/vortex-core spectrum — angular-momentum selection rules) with PHONONIC inheritance.

This is the most advanced laboratory state of exactly the MCT-3 observable. Canonical (`atlas-07-permanent-results`, `inheritance-falsifier-protocol.md`): §VII.W-3.LAB is the Lancaster MCT-3 inheritance-kernel falsifier — rank-2 ker(ι_*) = ⟨[φ_67], [φ_88]⟩ under the χ inheritance morphism χ : ℂ⊕ℍ⊕M₃(ℂ) → M₂(ℂ) (ker χ = M₃(ℂ); `s87-atlas-cardinality-cascade-vs-ensemble.md`), 4-gate protocol, Class-A NULL on F1+F2+F5 (decisive) + F3+F4 (supporting), **Class-B cohomology-asymmetry ratio 7.3250 ± 0.1%** (canonical band: ratio_band_lower = 7.3177, ratio_band_upper = 7.3323, `session-88-plan-w4c.md`). Substrate-first: the substrate's BdG spectrum on (A_K, H_K, D_K), restricted through χ to a vortex-core sector, IS the parent of the CdGM ladder; a K12442 (or 3He-B) vortex core is the laboratory projection where the ladder-asymmetry cocycle becomes a measured level-spacing ratio. The two load-bearing experimental capabilities this paper demonstrates: (i) the ±l-phase-resolution technique — precisely the opposite-angular-momentum readout a cohomology-asymmetry signature needs; (ii) the demonstrated 1:3:5 → 1:2:3 ladder-ratio tunability — the empirical handle proving the CdGM ratio is materially tunable and measurable, which the 7.3250 prediction requires. The cohomology-asymmetry test is substrate-falsifying-by-construction: per `inheritance-falsifier-protocol.md`, the (Δ_B/Δ_A)^p lab-conversion factor cancels between numerator and denominator (machine-precision 0.0 residual), so the substrate-derived ratio is preserved INTACT independent of the lab-conversion details. K12442 is a solid-state inheritance-child; the canonical decisive platform remains 3He-B (Lancaster MCT-3 / Helsinki ROTA cells), but Hou et al. demonstrate the measurement *modality* on a more accessible system.

### Result 8 — Yuan MgB₂ THz Leggett-mode selective excitation: laboratory anchor for the Leggett-channel DM lifetime (paper 02)

**Result**: THz-pump/THz-probe disentangles the Leggett mode (relative interband phase oscillation) from the Higgs amplitude mode in two-band s-wave MgB₂ (T_c = 30–40 K; Δ_π, Δ_σ), using multi-cycle vs single-cycle pump selectivity; nonlinear signals at ω and 2ω with resonant enhancement. **Classification: PHONONIC** (the Leggett mode is the laboratory realization of the framework's DM degree of freedom — an inter-band relative-phase coherence mode). **[INCOMPLETE: the index did not capture the extracted Leggett frequency / damping from the math-heavy PDF; full numbers on disk.]**

The framework's dark matter IS a Leggett-channel GGE quasiparticle — an inter-band coherence (relative-phase) mode that is CPT-neutral and non-annihilating. Canonical (`get_constant Mass_LeggettDM_over_Delta_BCS = 11.97`, S70 LEGGETT-MOMENT-70): the substrate-IS DM mass anchor sits at 11.97 × Δ_BCS on the BCS gap scale; `Ω_DM h² = 0.1200` from the Leggett inter-band coherence mode (0.6% from Planck). MgB₂'s Leggett mode is the canonical laboratory realization of exactly that DOF: a relative-phase oscillation between two pairing condensates, with the substrate's two-or-more D_K spectral sectors playing the role of the two MgB₂ bands. A THz-driven, selectively-excited Leggett mode with measurable damping gives the framework an experimental handle on the lifetime/spectral-function question for its DM mode through the χ projection.

**CRITICAL nuance the index omits — the lifetime is CONDITIONAL and the index's absolute figure is unverified.** The index cites "non-annihilation / τ_DM = 4.93e82 s." Canonical does NOT carry that absolute-seconds figure. What IS canonical: (i) `Mass_LeggettDM_over_Delta_BCS = 11.97` is "CONDITIONAL on Γ_grav < H_0 (the gravitational decay rate of the Leggett mode stays below the Hubble rate, so the relic survives)" — pinned S96 W7-2; (ii) the gate LEGGETT-GRAV-DECAY-73a PASS reports `tau_DM/t_univ = 1.13e+65` with Z_2 parity P_L from J-evenness of the condensate; (iii) LEGGETT-GRAV-DECAY-67 is flagged CRITICAL: "If Γ_grav > H_0, DM sector collapses (Ω_DM h²=0.120 meaningless)"; (iv) "Single-Leggett gravitational decay: FORBIDDEN" (S67 synthesis, PROVEN). So the framework's DM-relic survival rests on the *ratio* tau_DM/t_univ ≈ 1.13e65 (a survival margin), conditional on Γ_grav < H_0 — NOT on a free-standing "4.93e82 s." The MgB₂ Leggett-damping measurement is valuable precisely because it bounds the laboratory analog of the inter-band-coherence decay channel that the substrate's non-annihilation claim must be consistent with. Any carry-forward citing the lifetime must use the canonical conditional-ratio form, not the index's absolute figure (CF V.8).

### Result 9 — Luo AV₃Sb₅ van-Hove-singularity-driven flat bands: ARPES-visible analog of the τ_fold van Hove transit (paper 08)

**Result**: High-resolution ARPES on kagome AV₃Sb₅ (A = K, Rb, Cs) observes four branches of flat bands spanning the entire BZ, NOT anticipated from band-structure calculations and not explained by known flat-band mechanisms; the emergence is tied to the evolution of van Hove singularities (vHs at BZ boundary, Dirac cone at zone corner, intrinsic kagome flat band). **Classification: GEOMETRIC + PHONONIC** (DOS reorganization at a saddle point — the substrate van-Hove-fold transit mechanism in miniature).

The framework's cosmogenesis IS a supersonic transit (Mach = 13.75; `get_constant Mach_max_framework = 13.75`, c_fabric = 209.97 M_KK) through a **van Hove fold** at τ_fold = 0.190 (`get_constant tau_fold = 0.19`, S12/S42 CONST-FREEZE-42) — a first-order phase transition where the substrate's spectral density reorganizes across a van Hove singularity, NOT a slow-roll inflation. Luo et al. demonstrate laboratory-side that van Hove singularities *drive* flat-band emergence — exactly the substrate mechanism in miniature: as a control parameter (here doping/momentum; in the substrate, the Jensen deformation τ) moves the system across a vHs, the spectral weight reorganizes into flat (high-DOS, geometric) structure. Substrate-first: the substrate's van Hove fold in the D_K spectrum is the parent event; the AV₃Sb₅ vHs-driven flat-band emergence is an inheritance-child where the same DOS-reorganization-at-a-saddle-point physics is ARPES-visible. It uniquely couples *two* framework channels in one material family — the geometric/quantum-metric channel (these flat bands carry the superfluid weight of papers 01/04/07) and the van-Hove-transit channel — making it the natural laboratory testbed for the substrate's complexity reorganization at τ_fold. (Note: this is an analog of the *mechanism*, not a measurement of the substrate; the substrate transit is impulsive/supersonic at Mach 13.75, whereas an ARPES doping scan is quasi-static — the analogy is in the saddle-point DOS-reorganization topology, not the transit velocity.)

### Result 10 — Peotta–Törmä review: the load-bearing foundational citation for the §VII.AF.1 laboratory-IN element (paper 07)

**Result**: Foundational review deriving the multiband superfluid weight D_s = D_s^conv + D_s^geom; in a single band D_s ∝ inverse effective mass (flat band → zero supercurrent naively), but multiband D_s acquires a geometric quantum-metric contribution nonzero even for perfectly flat bands, with a topological lower bound (D_s ≥ minimal quantum metric / Chern or winding number); flat-band T_c linear in interaction U. **Classification: GEOMETRIC (FOUNDATIONAL).**

This review is the canonical definition + topological lower bound for the §VII.AF.1 bridge target. It is the load-bearing citation for any claim that the substrate's R_universal ↔ R_geom identification lands on a well-defined, bounded, geometry-controlled laboratory observable (it anchors the §VII.AF three-level ladder's laboratory-IN element). The framework already cites Peotta–Törmä as Pillar IV / Paper 14 (`session-66-einstein-phonon-first-workshop.md`: D_s = (2e²/ℏ²)·Δ²·g_geom). The review's central tension — a flat band's supercurrent comes entirely from geometry, not dispersion — is the substrate-side counterpart to "flat bands squeeze less"; the framework adds that, across its full spectrum, the dispersive acoustic channel still dominates the geometric one.

---

## III. Gate Verdicts

No gates. This is a literature sweep — NO computation, NO pre-registered gate evaluated, NO registry edit. All framework-state claims are anchored to existing canonical entries via the knowledge MCP (enumerated inline in Section II). Per `epistemic-discipline.md`, a literature sweep produces *organizational* findings (useful, not evidential); the only thing that changes the state of knowledge is a pre-registered gate against new computation, of which there are none here.

---

## IV. Structural Implications

**What sharpened (no state change):**

1. **§VII.AF.1 laboratory-IN element is now multiply-confirmed and dual-platform-anchored.** Tanaka (MATBG, T²) + Banerjee (MATTG, T-linear) measure the integrated-quantum-metric trace as real and dominant on two independent platforms; Porlles–Chen confirm the BdG-projector choice; Chen–Karki–Hosur confirm the non-Abelian trace is the algebra-correct object for A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ). The bridge's laboratory-IN observable (Level-3-analog anchor) is in its strongest empirical state to date. This is a `cross-pillar-bridge-anatomy.md` Element-5 (empirical anchor) strengthening — but it does NOT change the registry status of §VII.AF.1, which is already LANDED with its three-level ladder.

2. **The MCT-3 falsifier (§VII.W-3.LAB) now has a demonstrated measurement modality.** Hou et al.'s ±l-phase-resolution + ladder-ratio tunability is the experimental template the 7.3250 ± 0.1% cohomology-asymmetry prediction was waiting for. The falsifier remains "not yet measured" (atlas-04 row 12-bonus); its *measurability* is now demonstrated on a solid-state cousin.

3. **The Leggett-channel DM lifetime question has a laboratory anchor (MgB₂) and a corrected canonical form.** The survival claim is the conditional ratio tau_DM/t_univ ≈ 1.13e65 (Γ_grav < H_0), NOT the index's absolute "4.93e82 s." MgB₂ Leggett damping bounds the inter-band-coherence decay analog.

**Constraint-map corrections this synthesis flags (must propagate before any landing):**

- **Slot-label conflation**: the index assigns the R_geom bridge to §VII.W; canonical is §VII.AF.1.OP-PROJ. §VII.W is HP parity-grading orthogonality. Any §VII-citing carry-forward MUST re-anchor to §VII.AF.1.
- **"37×" unverified**: carried as the index's figure pending canonical-pin (canonical squeeze amplification is 54.06×; B1/B2 dominance multiplier not pinned).
- **τ_DM absolute figure unverified**: use the canonical conditional ratio (1.13e65, Γ_grav < H_0), not "4.93e82 s."

**What did NOT open or close:** No mechanism opened, closed, or shifted. No new constraint eliminated a region of solution space (no computation). The framework's open problems (A_s closure, μ_eff shortfall, CC gap) are untouched by this sweep. The honest recency gaps (SW2 FeSe NMR, SW3 173Yb — the index flags these as field-moves-slower-than-window, not filled from training knowledge) remain open and are NOT addressed here.

---

## V. Carry-Forward Computations

**These are candidate validation angles as 4-field specs. None is a gate verdict; each is a pre-registrable computation or registry-hygiene action for a future session. All §VII-slot references use the canonical §VII.AF.1 / §VII.W-3.LAB labels, correcting the index's §VII.W conflation.**

```
V.1. Registry-slot label reconciliation: R_geom bridge is §VII.AF.1, not §VII.W
   - What: Registry-hygiene action (NOT a computation). Confirm in sessions/permanent-results-registry.md
     and any S99-sweep-derived candidate that the Peotta–Törmä R_geom = ∫_BZ Tr g_ab^(P0) bridge is
     §VII.AF.1.OP-PROJ (substrate-IS Pillar III HP^1, laboratory-IN Pillar IV Peotta–Törmä, HKR bridge),
     and that §VII.W is the HP parity-grading orthogonality theorem. Flag the index legend's conflation
     so downstream sweeps inherit the correct slot.
   - Inputs: atlas-07-permanent-results.md (§VII.W, §VII.AF.1 rows); permanent-results-registry.md
     (W-5 §VII.AF.1 instance #1 anchor block); registry-landing.md §"Operator-Projection naming hygiene";
     00-INDEX.md line 5 (the conflated legend).
   - Gate: feeds the mack-cosmic-bridge sole-writer registry-hygiene queue (§VII.W / §VII.AF.1 are
     mack-cosmic-bridge sole-writer territory per feedback_mack-bridge-role.md). No PASS/FAIL — it is a
     label-correctness reconciliation. INFO if the registry already carries the correct labels (likely);
     the deliverable is the index-legend caveat note.
   - Effort: 0.5–1 hour, 1 agent session (orchestrator-direct or mack-cosmic-bridge).

V.2. Quasihole-vs-normal-state metric: confirm §VII.AF.1 integrand is the BdG-projector metric
   - What: Verify (Sage/numerical) that the §VII.AF.1 integrand Tr g_ab^(P0) is built from the BdG
     (quasihole/superconducting-state) projector P_0 on (A_K, H_K, D_K), not a normal-state band
     projector, matching Porlles–Chen (arXiv:2505.17349). Compute the substrate-side quasihole-state
     overlap quantum metric and compare its trace to the normal-state-projector trace at τ_fold.
   - Inputs: P_0(τ_fold) BdG projector from s86-hp1-cohomology-quantum-metric-bridge.md; D_K spectrum
     cache (s84_spectrum_cache_L12_tau019.npz); eps_H_HP1_norm = 16.197719; Porlles–Chen quasihole-metric
     definition (paper 03).
   - Gate: NEW gate S{N}-AF1-BDG-PROJECTOR-CONFIRM. PASS if the BdG-projector trace reproduces the
     R_universal = ∫_BZ Tr g_ab^(P0) anchor and the normal-state-projector trace does NOT (i.e. the
     bridge target is provably the BdG metric); INFO if both coincide at τ_fold (projector choice
     immaterial there); FAIL if the normal-state projector matches and BdG does not (would re-open the
     §VII.AF.1 → §VII.AF anchor ambiguity).
   - Effort: 3–4 hours, 1 agent session (lizzi or connes axis; GPU torch.linalg for the BZ trace).

V.3. Non-Abelian Tr[R_μν] on the substrate degenerate Peter-Weyl sectors
   - What: Compute the non-Abelian quantum-geometric trace Tr[R_μν] (R = Re part of the non-Abelian QGT)
     over the substrate's degenerate Peter-Weyl sectors of D_K at τ_fold, per Chen–Karki–Hosur
     (arXiv:2501.16965), and verify Tr R ≠ Σ(per-sector Abelian QMs) — i.e. the within-degenerate-subspace
     inter-band terms are nonzero on A_K = C ⊕ H ⊕ M_3(C). Report the geometric fraction analog of the
     paper's 20%/50% (MoS2/TiSe2).
   - Inputs: degenerate-sector eigenvectors from the D_K block-diagonal decomposition (Peter-Weyl
     (p,q) blocks; (0,0) BCS sector B3 mult 3 / B2 mult 4 / B1 mult 1×2); sewing-matrix B_k construction
     (time-reversal BDI, T²=+1); Chen–Karki–Hosur Eq. 2/Eq. 8 (non-Abelian QGT, Tr R).
   - Gate: NEW gate S{N}-AF1-NONABELIAN-TRACE. PASS if Tr R − Σ(per-band Abelian QM) > tolerance
     (inter-band within-degenerate-subspace content is nonzero and substantial, ≥ O(10%) of the trace,
     matching the paper's measured fractions); INFO if nonzero but < tolerance; FAIL if Tr R = Σ(per-band)
     to machine precision (would contradict the algebra-correctness claim and reduce to the Abelian case).
   - Effort: 4–6 hours, 1 agent session (connes/lizzi axis; degenerate-subspace QGT is the technically
     demanding part).

V.4. Hirobe node-resolved D^geom(T) substrate power-law cross-check
   - What: Given the substrate's BCS gap structure (Δ_BCS = 0.4643 M_KK; node structure of the (0,0)
     sector), predict the thermal power law of the substrate's geometric superfluid-weight analog
     D^geom(T) using Hirobe's node-resolved classification (full gap e^{−Δ/T}; line node T^{1/(l+1)};
     crossing −T^{1/(l+1)} ln T), and test whether it falls in the flat-band (geometric) class rather
     than the dispersive/Fermi-liquid class.
   - Inputs: Delta_BCS = 0.4643; (0,0)-sector node structure; band identities E_B1=0.819 (acoustic),
     E_B2=0.845 (flat, vHs); Hirobe Tables 1–2 power-law classification (paper 01).
   - Gate: NEW gate S{N}-AF1-THERMAL-SCALING. PASS if the substrate D^geom(T) reproduces a flat-band
     geometric power law (strictly weaker than dispersive at equal node structure, per Hirobe); INFO if
     the substrate gap is full-gap (activated e^{−Δ/T}, no power-law discriminant available); FAIL if it
     reproduces the conventional Fermi-liquid law (would indicate the geometric channel is NOT the
     dominant thermal contributor in the substrate's BCS sector).
   - Effort: 2–3 hours, 1 agent session (landau/volovik axis).

V.5. Two-platform node-discriminant: MATBG T² vs MATTG T-linear against substrate sector geometry
   - What: Map the Tanaka MATBG (T²) and Banerjee MATTG (T-linear) thermal scalings onto Hirobe's
     node classes (T² → point/line node; T-linear → flat-crosses-Dirac K-node) and check which the
     substrate's projected quantum metric reproduces. This is the platform-robustness cross-check for
     §VII.AF.1's Level-3 anchor.
   - Inputs: Tanaka Nature 638, 99 (T² stiffness, paper 09); Banerjee Nature 638, 93 (T-linear ρ_s,
     paper 10); Hirobe node table (paper 01); substrate (0,0)-sector node structure; §VII.AF.1 R_geom
     anchor + three-level ladder envelope (match/envelope = 0.0950).
   - Gate: feeds §VII.AF Element-5 (empirical anchor) robustness — extends the laboratory-IN anchor from
     single-material to dual-platform. INFO-class (strengthens an already-LANDED anchor; does not move
     registry status). Document as a §VII.AF.1 Element-5 dual-platform note, NOT a new PASS gate.
   - Effort: 2 hours, 1 agent session (mack-cosmic-bridge for the Element-5 note; landau for the
     node-class mapping).

V.6. Canonical-pin verification of the "B1 acoustic dominates by 37×" figure
   - What: Registry-hygiene + small computation. Locate or recompute the canonical source of the "37×"
     B1/B2 (acoustic/flat) dominance multiplier the index cites. Reconcile against the canonical squeeze
     amplification F_squeeze_bare = 54.06× and the band identities; if "37×" is a derived ratio, pin its
     derivation; if unverifiable, down-tag the index figure.
   - Inputs: s74_as_from_bogoliubov_output.txt (F_squeeze_bare = 5.4060e+01); E_B1=0.819, E_B2=0.845
     (session-38-naz-tesla-workshop.md); K_R5=1.922 B2-minimum (session-83-volovik-synthesis.md);
     s43_flat_band.npz (FLATBAND-43); the project insight file flat-bands-squeeze-less.
   - Gate: SOURCE-RECON-class hygiene (epistemic-discipline.md §"Source Reconciliation"). PASS if a
     canonical source for 37× is found and the derivation reproduces it; INFO if 37× is a documented
     derived figure with a now-confirmed provenance; FAIL-with-remediation if no canonical source exists
     (down-tag the index figure; do not propagate "37×" into any registry text).
   - Effort: 1–2 hours, 1 agent session.

V.7. Hou ±l CdGM phase-resolution → MCT-3 cohomology-asymmetry readout protocol
   - What: Translate Hou et al.'s ±l angular-momentum phase-resolution technique (local DOS
     ρ ∝ [1+|α_l|²+2|α_l|cos(2lφ+φ_0l)]|ψ_l|²) into the MCT-3 measurement protocol: specify how the
     opposite-angular-momentum (±l) CdGM level-asymmetry maps to the substrate's 7.3250 ± 0.1%
     cohomology-asymmetry ratio under the (Δ_B/Δ_A)^p cancellation, on a 3He-B vortex core.
   - Inputs: Hou necklace-CdGM DOS formula + ladder-ratio tunability 1:3:5→1:2:3 (paper 05);
     lancaster-mct3-protocol-pre-registration.md; inheritance-falsifier-protocol.md 4-gate structure;
     ratio_band_lower=7.3177, ratio_band_upper=7.3323; ker(ι_*)=⟨[φ_67],[φ_88]⟩; χ morphism (ker χ=M_3(C)).
   - Gate: feeds the §VII.W-3.LAB falsifier protocol (Gate 2 cohomology-asymmetry, 7.3250±0.1%). Protocol-
     design deliverable (NOT a numerical PASS) — produces a pre-registered measurement-protocol mapping
     that mack-cosmic-bridge can append to falsifier-master-inventory.md. INFO/protocol-class.
   - Effort: 3–4 hours, 1 agent session (volovik PRIMARY for the inheritance-kernel mapping; mack-cosmic-
     bridge for the inventory row).

V.8. MgB₂ Leggett damping → Leggett-channel DM inter-band-coherence lifetime bound (corrected form)
   - What: Extract the MgB₂ Leggett-mode frequency-to-gap ratio and damping rate from paper 02 (the
     index marked these [INCOMPLETE]; pull from the on-disk PDF via read_arxiv_paper 2412.13830), and
     compute the bound it places on the substrate's inter-band-coherence decay channel through the χ
     projection — expressed as the CONDITIONAL ratio tau_DM/t_univ (canonical 1.13e65, Γ_grav<H_0), NOT
     the index's unverified absolute "4.93e82 s."
   - Inputs: paper 02 PDF (extract Leggett ω/Δ and damping Γ_Leggett); Mass_LeggettDM_over_Delta_BCS=11.97
     (CONDITIONAL on Γ_grav<H_0); LEGGETT-GRAV-DECAY-67 (CRITICAL); LEGGETT-GRAV-DECAY-73a (tau_DM/t_univ
     =1.13e65); Delta_BCS=0.4643; omega_L1=0.138 M_KK, Q=18.6 (Leggett DM mode, MEMORY).
   - Gate: feeds the LEGGETT-GRAV-DECAY line. PASS if the MgB₂-anchored laboratory Leggett-damping
     universality is CONSISTENT with the substrate's non-annihilation (Γ_grav < H_0 survival margin
     intact); INFO if the lab damping bounds only the lab analog without constraining the gravitational
     channel; FAIL if the lab Leggett-damping universality class is incompatible with the claimed
     non-annihilating coherence mode. MUST use the conditional-ratio canonical form.
   - Effort: 3–4 hours, 1 agent session (landau for the universality-class argument; first pull the
     [INCOMPLETE] MgB₂ numbers from the PDF).

V.9. AV₃Sb₅ vHs-driven flat-band emergence as analog of the τ_fold DOS reorganization
   - What: Use Luo et al.'s ARPES vHs-driven flat-band emergence (paper 08) to construct the laboratory-
     analog map for the substrate's van-Hove-fold transit: as the substrate's Jensen τ crosses τ_fold=0.19,
     the D_K spectral density reorganizes across a saddle point (Mach 13.75 supersonic). Compute the
     substrate DOS reorganization at τ_fold and compare its saddle-point topology to the kagome vHs→flat-band
     reorganization. Scope explicitly: analog of the MECHANISM (saddle-point DOS topology), NOT the transit
     velocity (substrate impulsive vs ARPES quasi-static).
   - Inputs: tau_fold=0.19; Mach_max_framework=13.75, c_fabric=209.97 M_KK; D_K spectral-density cache near
     τ_fold (s84/s85 transit caches, e.g. transit-flow-genesis-to-now.md); Luo AV₃Sb₅ vHs/flat-band ARPES
     structure (paper 08, four flat-band branches).
   - Gate: feeds the Transit dynamics channel (TRANSIT-PS-67, OPEN; power spectrum pending). INFO-class
     analog-construction (the substrate is the parent; AV₃Sb₅ is an inheritance-child mechanism analog).
     NOT a falsification of the substrate — it is a laboratory-mechanism cross-check. Document the saddle-
     point-topology correspondence; do NOT claim a velocity match.
   - Effort: 2–3 hours, 1 agent session (volovik/landau axis).

V.10. Penttilä flat-band-ratio moderation vs substrate flat-vs-dispersive partition (BKT cross-check)
   - What: Use Penttilä et al.'s finite-T DMFT result (flat-band ratio + T=0 superfluid weight guide the
     BKT temperature in non-isolated flat bands; paper 04) to cross-check the substrate's flat-vs-dispersive
     channel hierarchy: compute the substrate's intrinsic flat-band ratio (flat B2 weight / total) from the
     Peter-Weyl sector partition and test whether the geometric channel is moderated by it as the framework's
     acoustic-dominance hierarchy requires. Pairs with V.6 (37× verification).
   - Inputs: Peter-Weyl sector partition of D_K (B1 acoustic 1 mode / B2 flat 4 modes / B3 color 3 modes);
     Delta_BCS=0.4643; T_acoustic; BKT-sector-resolved result (s74_bkt_sector_resolved_result.md);
     Penttilä flat-band-ratio↔superfluid-weight↔BKT relation (paper 04).
   - Gate: feeds the BKT / flat-vs-dispersive hierarchy. PASS if the substrate's geometric channel is
     moderated by the flat-band ratio in the direction Penttilä reports AND consistent with acoustic
     dominance; INFO if the substrate is in the isolated-flat-band limit (moderation not testable); FAIL if
     the substrate geometric channel does NOT track the flat-band ratio (would contradict the hierarchy).
     Depends on V.6 for the dominance multiplier.
   - Effort: 2–3 hours, 1 agent session (volovik/landau axis). Depends on V.6.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | R_geom bridge is §VII.AF.1.OP-PROJ, NOT §VII.W (= HP parity-grading orthogonality) | GEOMETRIC | Canonical correction (index conflation) | All §VII-citing carry-forwards must re-anchor to §VII.AF.1 |
| 2 | Porlles–Chen: diamagnetic metric is the quasihole/BdG-state metric (paper 03) | GEOMETRIC | Structural confirmation | Confirms §VII.AF.1's BdG-projector choice in R_geom |
| 3 | Chen–Karki–Hosur non-Abelian Tr[R_μν] is algebra-correct for A_K=ℂ⊕ℍ⊕M₃(ℂ); 20%/50% (paper 06) | GEOMETRIC | Structural confirmation | The substrate fiber is non-Abelian/degenerate; Abelian metric is the wrong idealization |
| 4 | Tanaka MATBG (T²) + Banerjee MATTG (T-linear): geometry-dominated stiffness, dual-platform (papers 09/10) | GEOMETRIC (PHONONIC inherit.) | Empirical anchor strengthened | §VII.AF.1 Level-3 anchor now dual-platform, not single-material |
| 5 | Hirobe node-resolved D^geom(T) power-law table (paper 01) | GEOMETRIC | Falsifiable thermal probe | Thermal handle to test §VII.AF.1 is a geometric (not band-velocity) object |
| 6 | Penttilä flat-band-ratio moderation (paper 04); "37×" is index's figure, NOT canonical-pinned | GEOMETRIC | Direction canonical; multiplier unverified | Acoustic dominance is canonical in direction; 37× needs canonical pin (V.6) |
| 7 | Hou ±l phase-resolved CdGM + ladder-ratio tunability 1:3:5→1:2:3 (paper 05) | PARTICLE (PHONONIC inherit.) | Measurement modality demonstrated | Experimental template for the MCT-3 / §VII.W-3.LAB 7.3250±0.1% falsifier |
| 8 | Yuan MgB₂ Leggett-mode selective excitation (paper 02); τ_DM is CONDITIONAL ratio 1.13e65, NOT "4.93e82 s" | PHONONIC | Lab anchor + canonical correction | Bounds Leggett-channel DM coherence-decay; survival conditional on Γ_grav<H_0 |
| 9 | Luo AV₃Sb₅ vHs-driven flat bands (paper 08) | GEOMETRIC + PHONONIC | Mechanism analog (not measurement) | ARPES-visible analog of τ_fold=0.19 van-Hove transit (topology, not velocity) |
| 10 | Peotta–Törmä review: D_s=D_conv+D_geom, topological lower bound (paper 07) | GEOMETRIC (FOUNDATIONAL) | Load-bearing citation | Defines + bounds the §VII.AF.1 laboratory-IN observable |

---

**Honest-gap note (carried verbatim from the index, not filled):** The index flags SW2 (FeSe NMR) and SW3 (173Yb optical lattice, λ_8 / Γ_3B three-body loss) as slow-moving channels whose load-bearing results predate the 2024–2026 sweep window; no 2024–2026 preprint surfaced via search_arxiv + WebSearch. These are NOT addressed in this synthesis and are NOT filled from training knowledge. Pre-window anchors (pointers only, not downloaded): 173Yb SU(6) Mott/AFM (arXiv:2010.07730), FeSe multiband BCS-BEC vortex core (arXiv:1901.09141), orbital Feshbach 173Yb (arXiv:1509.04257).

**Provenance discipline:** All paper content derives from the index's fetched-text summaries (sweep protocol: summaries drawn ONLY from fetched abstract/PDF text; none from training knowledge). All framework-state claims are anchored to canonical knowledge-MCP entries enumerated inline (eps_H_HP1_norm=16.197719; tau_fold=0.19; Mass_LeggettDM_over_Delta_BCS=11.97 CONDITIONAL; Mach_max_framework=13.75; ratio band 7.3177–7.3323; ker(ι_*)=⟨[φ_67],[φ_88]⟩; χ:ℂ⊕ℍ⊕M₃(ℂ)→M₂(ℂ); §VII.W = HP parity-grading orthogonality; §VII.AF.1.OP-PROJ = R_geom bridge). Three index figures are explicitly flagged as unverified-against-canonical: the §VII.W slot label (→ §VII.AF.1), the "37×" multiplier (canonical squeeze is 54.06×), and the "τ_DM=4.93e82 s" absolute lifetime (→ canonical ratio 1.13e65, Γ_grav<H_0).
