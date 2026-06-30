# Landau Classification of Phonon-Exflation

**Author**: Landau Condensed Matter Theorist
**Date**: 2026-05-25 (comprehensive S93-era expansion; original S44, 2026-03-15)
**Status**: Living document (updated each session) — comprehensively rewritten S45→S93 (session-X W7)
**Source**: S44 collab review Section 4, expanded with full S7–S93 context
**Papers**: `researchers/Landau/` (index at `researchers/Landau/index.md`)

---

## Preamble

The phonon-exflation framework claims that Standard Model particles are phononic excitations of M⁴ × SU(3), with cosmogenesis driven by internal spectral complexification — *exflation*, not metric inflation. Over Sessions 7 through 93, a systematic mapping has emerged between every structural element of this framework and a precise condensed-matter counterpart in Landau's classification program. This document makes that mapping explicit, complete, and current.

The mapping is not metaphorical. It is a statement about mathematical structure: the same symmetry-breaking patterns, order-parameter spaces, free-energy functionals, and quasiparticle descriptions that govern superfluids, superconductors, and Fermi liquids also govern the internal geometry of the phonon-exflation framework. Where the mapping holds, it constrains. Where it breaks, it diagnoses.

**Direction of explanation (substrate-IS, not container).** Every identification below flows FROM the substrate spectral triple TOWARD the condensed-matter classification, never the reverse. The substrate is not "modelled by" a superconductor; the substrate IS a finite spectral triple `(A_K, H_K, D_K)` whose BCS sector exhibits the 3D-Ising universality class. The eigenvalue spectrum of `D_K` on Jensen-deformed SU(3) IS the order-parameter manifold; the BCS gap `Δ(τ)` IS the superconducting order parameter on the fiber; the Leggett inter-band mode IS a phason of the B2–B3 sector; the GGE IS the post-transit integrable relic. A laboratory superfluid (³He-B most precisely) is a *child* of this parent structure under an inheritance morphism — a projection of the substrate's algebra onto a continuum BdG observable — not an analogy to it.

Every claim below is grounded in specific Landau papers (cited as Paper NN) and specific framework computations (cited as session-gate). The document is self-contained.

**What changed in this revision (S45→S93).** The single most consequential correction: the S44 document's central open prediction — that the occupied-state spectral action `S_occ(τ)` develops a non-monotone minimum near τ=0.19 — was tested at S45 and **failed**. `S_occ` is monotone decreasing (the "28th equilibrium closure"). The Landau-`F(η₀)` intuition was correct in spirit (the condensation energy is negative) but quantitatively dominated: the BCS off-diagonal content is effaced at the 0.002% level and cannot overturn the Weyl-law monotonicity. This is the one-body/many-body partition (§III) confirming itself. Beyond the correction, the framework produced a large body of new Landau-CM physics now folded in: the Leggett-channel dark-matter mass anchor (§VIII), the Volovik free-energy partition (§IX), the integrability of the post-transit relic (§X), BKT and the superfluid-stiffness tensor on the discrete fabric (§XI), and — most importantly for the §VII "no laboratory" limitation — the ³He-B inheritance morphism that supplies an actual laboratory falsifier (§XII).

---

## I. The Complete Mapping

The following table maps every framework concept to its Landau condensed-matter equivalent, with the session that established the connection and the Landau paper that provides the theoretical foundation. The original ~33 rows are refreshed to their current S93 fate; the new-since-S44 correspondences are appended in a second block.

### I.A. Foundational Mapping (S7–S44 rows, refreshed to S93)

| Framework Concept | CM Equivalent | Session | Paper | Status (S93) |
|:--|:--|:--|:--|:--|
| Jensen deformation τ | Order parameter η | S17a | 04 | PROVEN |
| SU(3) → U(1)_7 | Symmetry breaking G → H | S34 | 04 | PROVEN |
| Spectral action S(τ) | Landau free energy F(η) | S17a, S20b, S54 | 04 | STRUCTURAL |
| V'''(0) = −7.2 | Cubic term forces first-order | S17a, S22c | 04 sec. 8 | PROVEN |
| d_int = 8 > d_uc = 4 | Mean-field exact above d_uc | S17a | 04 sec. 7 | STRUCTURAL |
| Transit τ=0 to fold | First-order phase transition | S37–38 | 04, 09 | PROVEN |
| BCS condensation at fold (E_cond = −0.13685 M_KK) | Superconducting transition | S35, S36 | 08, 15 | PROVEN |
| BCS instanton gas | Giant pair vibration (GPV) | S37 | 23, 24, 25 | PROVEN |
| S_inst = 0.069 | Quantum critical point | S38 | 29 | PROVEN |
| Post-transit GGE | Normal component at rest | S38, S67 | 05, 20 | STRUCTURAL |
| Dark energy | Superfluid condensation energy | S44 W6-4, S58 | 05 | OPEN |
| Dark matter | Quasiparticle energy at rest → **Leggett-channel mass anchor** | S44 W1-2, **S70** | 05, 11, 20 | **PROMOTED** (see §VIII) |
| DM/DE ratio | Specific heat exponent α | S44 W6-4 | 04, 05 | OPEN (framework/obs = 2.74×) |
| G_N | Effective mass / response coeff. | S44 W1-1, S53, S75 | 11 | **PROVEN-CONDITIONAL** (Λ-dependent; see §III.A) |
| Spectral triple dissolution | Effective theory emergence | S44 W6-7 | 04 (universality) | PROVEN |
| CC fine-tuning | Universality class mismatch | S44 W5-5, **S66** | 04 sec. 7 | STRUCTURAL → **reframed by DILUTION-CC** (§VII.A7) |
| n_s = 0.9561 | ~~Quench dynamics / Kibble-Zurek~~ → **geometric tilt** | S43–44, **S57/S73a/S86** | 04, 09, 21 | **SUPERSEDED-by-mechanism-shift** (KZ → geometry; §VI.C) |
| ε_H invariance | Ratio invariance (intensive) | S44 W4-3 | 04 | PROVEN (theorem); value pin refreshed (§VI) |
| Van Hove singularities | Phase transition classification | S34–44 | 27 | PROVEN |
| Block-diagonal theorem | Selection rules (Schur / Peter-Weyl) | S22b | 04 (rep. theory) | PROVEN (permanent wall) |
| 8-temperature GGE | Non-Fermi liquid | S44 W6-5, S63 | 11, 20 | STRUCTURAL |
| Negative heat capacities | Saddle directions in F | S44 W6-5 | 04, 11 | PROVEN |
| Euler deficit = E_cond | Gibbs-Duhem violation | S44 W6-5 | 05 | OPEN |
| Effacement wall (0.002%) | Off-diagonal LRO invisible | S44 W5-4, S61, S75 | 11, 15 | PROVEN |
| K_7 Cooper pairs | BCS order parameter | S35 | 08, 15 | PROVEN |
| Pomeranchuk f_0 = −4.687 | Fermi surface instability | S22c | 11 | PROVEN (robust at L=5,7) |
| B2 mult-8 optical band edge | Finite large BCS-driving DOS edge (rho_smooth = 14.02 M_KK⁻¹; the N(0) feeding g·N(0)=3.24, S22c; 43–51× enhancement, S28c). NOT a dispersionless "flat band" and NOT an "infinite-order van Hove": the band disperses LINEARLY (n=1, v_g(fold)=0.0227≠0) above a FIXED mult-8 Clifford/ℂ¹⁶ degeneracy; the canonical DOS is the finite velocity-slaved continuum branch (14.02 = 1/(π·v_g)), not a δ-divergence. The infinite-order / flat-band reading is REFUTED (W7-22). [Open: whether the mult-8 δ-WEIGHT licenses the noun "van Hove singularity" on a finite triple — see CF-S95-W2-VAN-HOVE-NOUN.] | S22c (DOS-edge g·N(0)); S28c (1D BCS theorem); W7-22 (dispersion + order scope, REFUTED) | 27, 16 | PROVEN (finite DOS-edge BCS driver); "infinite-order van Hove" + "flat band" DEMOTED (W7-22) |
| M_max = 1.674 | Thouless criterion | S35 | 15 | PROVEN |
| L/ξ_GL = 0.031 | Ultrasmall grain limit | S38 | 17, 36 | PROVEN |
| E_vac/E_cond = 28.8 | BEC regime of crossover | S37, **S61** | 22 | PROVEN (N-refined at S61) |
| ω_att = 1.430 | Pair vibration frequency | S37 | 23 | PROVEN |
| Schwinger-instanton duality | WKB tunneling = pair creation | S37 | 29 | PROVEN (1%) |
| Second sound Q = 75,989 | Undamped two-fluid mode | S44 W6-2, S68 | 05 | PROVEN (obs horizon at S68) |
| 12 Van Hove trajectories | Band structure topology | S44 W6-8 | 27 | PROVEN |
| Gap stability (−1.63%) | Fully gapped spectrum | S44 W5-3 | 08 | PROVEN |
| BDI class, T² = +1 | Altland-Zirnbauer symmetry | S17c, **S88** | 15 | PROVEN (KO-dim=6; inheritance-confirmed) |
| g_1/g_2 = e^{−2τ} | Geometric running coupling | S17a | 10 | PROVEN |
| CDM T^{0i} = 0 | Pressureless dust / normal fluid | S44 W1-2 | 05 | PROVEN |
| OCC-SPEC-45 | Landau free energy at phys. state | S45 | 04, 15, 08 | **CONTRADICTED — RAN + FAILED: S_occ monotone (§V/§VI)** |

### I.B. New Framework↔Landau-CM Correspondences (established S45→S93)

These rows did not exist in the S44 document. They are the substance of the 49-session interval. Each is grounded in a session-gate and a Landau-domain paper; the prose section that develops it is cited in the last column.

| Framework Concept | CM Equivalent | Session / Gate | Paper | Status | Prose |
|:--|:--|:--|:--|:--|:--|
| Leggett inter-band mode mass | First Type-F dark-matter mass anchor (Mass/Δ_BCS = 11.97; Ω_DM h² = 0.1200 Leggett-only) | S70 LEGGETT-MOMENT-70 | 05, 11, 20 | PROVEN-CONDITIONAL | §VIII |
| Leggett mode quality factor | Undamped collective (second-sound class), Q = 670,000 | S70; S50 LEGGETT-DAMPING-50 | 05 | PROVEN-CONDITIONAL | §VIII |
| Leggett Goldstone mass | Phason gap from U(1)_7 breaking (m_L1 = 0.070 M_KK; ω_L1 = 0.138; c_Gold = 0.915) | S48 MASS-48; S66; S80 | 08, 11 | PROVEN | §VIII, §XI |
| Volovik free-energy partition | Condensation-energy split: vacuum vs quasiparticle sectors (F_Josephson = −336.6 M_KK → 95.9% vacuum; F_BCS+F_BA+F_Leggett = 14.411 → matter) | S58/S62 PARTITION | 04, 05 | PROVEN | §IX |
| GGE two-fluid model | Generalized Landau-Khalatnikov (GGE normal component) | S67 GGE-TWO-FLUID/FLUID-67 | 05, 09, 20 | STRUCTURAL | §X |
| Superfluid-stiffness anisotropy tensor | GL phase stiffness on the Lie algebra (ρ_s(C²)=7.96 vs ρ_s(u(1))=0.33; 24× anisotropic) | S47 TENSOR-47 | 08 | STRUCTURAL | §XI |
| BKT on the finite graph | Berezinskii-Kosterlitz-Thouless vortex unbinding (T_BKT = (π/2)·ρ_s_eff; sector-resolved) | S56 TEST-56; S58 KUBO-58; S74 RESOLVED-74 | 21, BKT | PROVEN | §XI |
| GGE permanence | Richardson-Gaudin integrability (Ordered Veil; ⟨r⟩≈0.33 Poisson, Brody β≈0; t_Th from Cayley-graph Laplacian) | S38/S39/S53/S60/S61/S62 | 16, 20 | STRUCTURAL (sector-resolved; see §X) | §X |
| ³He-B inheritance morphism | BDI substrate → laboratory child (cocycle ratio φ_67/φ_88 = 7.324992; Caroli-Matricon vortex ladder) | S86/S87/S90 (W11-C5 PASS) | 15, 19 | PROVEN (lab falsifier) | §XII |
| DILUTION-CC | Universality-class mismatch reframed (114→0.01 OOM via tracking vacuum; CC_OOM = 115.5) | S66 DILUTION-CC-66 | 04, Volovik 25/35 | SUPERSEDED-context | §VII.A7 |
| Kohn-anomaly / Ginzburg number on fabric | Phonon softening + fluctuation criterion (Gi ≈ 0.5–0.94; backaction-drag reclass) | S53 FABRIC-53 | 04 (Ginzburg), 11 | STRUCTURAL | §II.C |
| n_s geometric tilt | Tilt from spectral geometry, not quench (n_s = 1 − 2ε_H; Mode-Independent Occupation Theorem) | S57; S73a COMPOUND-NS-73a; S86 W1c-8 | 04, 09, 21 | SUPERSEDED-by-mechanism-shift | §VI.C |
| α_s = n_s² − 1 | Running coupling as Mellin residue (substrate-distance −0.08587279; pivot ≈ 0) | S50/S84/S86/S89 | Landau-pole heritage | PROVEN | §IV.F |
| Resolvent–Fermi-liquid correspondence | Resolvent of D_K ↔ quasiparticle propagator | S63 VdD-Vol workshop | 11 | STRUCTURAL | §III.B |
| Pomeranchuk-on-GGE | Pomeranchuk test on the post-transit GGE (no Fermi surface) | S58 POMERANCHUK-GGE-58 (FAIL) | 11 | CURRENT (informative FAIL) | §III, §X |
| Mott-transition CC inaccessibility | Mott insulator transition on the Josephson array (E_J/E_C = 194, 571× above critical) | S65 | 08, 22 | PROVEN | §II.C |
| Second-sound observational horizon | Two-sound CMB hierarchy (ℓ_second_sound = 720.9 = π·c_fabric/c_Gold) | S53 CMB-53; S68 OBS-68 | 05, 09 | CURRENT | §VIII |
| Multi-instanton / instanton liquid | Dilute-gas → liquid crossover; modulus effective mass (V_eff monotonic) | S75; S76-C4-INST-LIQUID (FAIL) | 29; 23,24,25 | CURRENT (informative FAIL) | §V |
| GL κ = λ/ξ classification | Type-I vs Type-II via GL parameter κ = λ/ξ_BCS | Paasch-potential collab; S38 | 08, 17, 36 | CURRENT | App. A |

**Reading guide**: PROVEN = computed to machine precision or proven as a theorem. PROVEN-CONDITIONAL = proven contingent on an explicitly stated condition (a UV cutoff, a survival criterion). STRUCTURAL = the identification is mathematically exact but relies on an analogy whose full consequences are partly unexplored. OPEN = the mapping exists but the quantitative prediction is not yet confirmed. SUPERSEDED-by-mechanism-shift = the row is correct but its *resolution route* moved to other physics. SUPERSEDED-context = the row is correct but the framework's resolution is now cosmological, not CM-internal. CONTRADICTED = a standing prediction was tested and failed (a result, not a deficiency).

---

## II. Phase Classification Table

Landau's program classifies all ordered phases by their symmetry-breaking pattern, order parameter, transition type, universality class, and critical exponents. The following applies this classification to every phase and transition the framework has identified across Sessions 7 through 93.

### II.A. Equilibrium Phases

| Phase | Symmetry Group | Order Parameter | Physical Content |
|:--|:--|:--|:--|
| τ = 0 (round SU(3)) | (SU(3)_L × SU(3)_R)/Z_3 | τ = 0 | Bi-invariant metric. Full isometry. Unstable maximum of V_eff. |
| 0 < τ < τ_fold (transit) | (SU(3)_L × SU(2)_R × U(1)_R)/Z_6 | τ > 0 | Jensen deformation. [iK_7, D_K] = 0 forces SU(3) → U(1)_7. |
| τ ≈ 0.19 (fold, BCS) | + U(1)_7 → Z_2 | Δ (BCS gap = 0.4642 M_KK) | Van Hove near-crossing in B2. Cooper pairing with K_7 charge ±1/2. |
| Post-transit (GGE relic) | (SU(3)_L × SU(2)_R × U(1)_R)/Z_6 | Δ = 0 | Condensate destroyed (P_exc = 1.000). GGE protected by 8 Richardson-Gaudin integrals. |

### II.B. Transitions

| Transition | Type | Order Parameter | Universality Class | z | ν | β | α |
|:--|:--|:--|:--|:--|:--|:--|:--|
| τ = 0: SU(3) → U(1)_7 | First-order | τ (scalar) | None (first-order) | — | — | — | — |
| τ ≈ 0: Lifshitz (Type I) | Topological | Fermi pocket creation | Lifshitz z=2 | 2 | 1/2 (MF) | — | — |
| τ ≈ 0.19: BCS onset | Second-order (GL) | Δ (complex scalar) | 3D Ising (Z_2, n=1) | 2.024 | 0.6301 | 0.3265 | 0.110 |
| Vortex unbinding (Josephson array) | Infinite-order (BKT) | phase coherence (θ) | 2D-XY / BKT | — | ∞ (essential) | — | — |
| Transit completion: BCS destruction | Sudden quench | P_exc → 1.000 | Kibble-Zurek (frozen) | 2.024 | 0.6301 | — | — |
| Post-transit relic | Integrable fixed point | 8 conserved I_k | Richardson-Gaudin (no thermal fixed point) | — | — | — | — |

**Notes on the classification.**

1. The τ = 0 transition is first-order because V'''(0) = −7.2 (Paper 04, §8: a cubic invariant forces first-order). The cubic term exists because τ → −τ is NOT a symmetry of the spectral action — the Jensen deformation is one-directional. This is now hardened by the **Perturbative Exhaustion Theorem** (S22c, baseline-findings #12): with H1–H5 verified, the perturbative free energy is not the true free energy, and the transition is first-order. It is the *only* escape from the spectral-action monotonicity theorem (§V).

2. The BCS transition at τ ≈ 0.19 is classified as **3D Ising** (S43, BCS-CLASS-43; PERMANENT). The order parameter Δ is a complex scalar, but the K_7 charge pinning ([iK_7, D_K] = 0, S34) reduces the continuous U(1) phase to a discrete Z_2 (sign of Δ). The universality class is Z_2, d = 3, n = 1: ν = 0.6301, β = 0.3265, γ = 1.2372, α = 0.110. The dynamic class is Model A (Paper 09: overdamped relaxational dynamics, no conservation laws coupling to the order parameter), giving z = 2.024. This is a *permanent wall* of the framework, not a tunable result.

3. The Lifshitz transition at τ = 0 is Type I (S43, LIFSHITZ-43): a Fermi pocket appears as the Jensen deformation lifts the degeneracy of the bi-invariant SU(3) spectrum. The 32-fold degeneracy at τ = 0 splits into 8.27-fold residual degeneracy at any τ > 0 (S44 W5-3). For d_int = 8, the transition is far above its upper critical dimension d_uc = 3, so mean-field exponents are exact (Paper 04, §7).

4. **NEW (S56/S74) — BKT on the discrete fabric.** The 32-cell coarse-grained Cayley-graph fabric is a Josephson-junction array (the phase field θ_i lives on each cell; E_J couples neighbours). The relevant phase-coherence transition is therefore Berezinskii-Kosterlitz-Thouless, not a symmetry-breaking transition: it has no local order parameter, an essential singularity (not a power law) in the correlation length, and proceeds by vortex unbinding. The BKT temperature on a lattice with coordination z is T_BKT = (π/2)·ρ_s_eff (S56 plan; S74 RESOLVED-74), evaluated sector-by-sector. At the fold, E_J = 3.890 M_KK gives T_BKT = 6.111 M_KK (S56). Cosmologically this matters: vortex production through the BKT transition is exponentially suppressed (exp(−708)), which closes the cosmic-string GW channel (`closed-gw-channels.md`) without fine-tuning. The substrate-IS reading: the *fabric IS a 2D-XY system on its coarse-grained graph*, and its phase stiffness ρ_s (§XI) sets the vortex-unbinding scale.

5. **NEW (S38/S62) — the post-transit relic is an integrable fixed point, not a thermal endpoint.** The transit completion is a sudden quench, not a phase transition. The Landau-Zener probability P_LZ = exp(−2π Δ²/(ℏ|v̇|)) gives P_exc = 1.000 (S38; Paper 29): the system passes through the fold too fast for the BCS condensate to follow (quench time τ_Q ≪ Landau-Khalatnikov relaxation time τ_LK, Paper 21). The post-transit state is NOT thermal — it is a GGE determined by 8 Richardson-Gaudin conserved integrals (Paper 16, 20). Its level statistics are sub-Poisson (⟨r⟩ ≈ 0.33, Brody β ≈ 0 in the (2,1) sector, S53), the signature of integrability (Berry-Tabor) and the absence of level repulsion. This is developed in §X.

### II.C. d_uc and the Role of Internal Dimensionality (with the Kohn-anomaly/Ginzburg refinement)

A subtlety that pervades the framework. The internal space SU(3) has dimension 8. For fluctuations of the τ modulus — a single scalar mode in an 8-dimensional space — the effective dimensionality for critical fluctuations is d_eff = 8. Since d_uc = 4 for the standard Landau-Wilson φ⁴ theory (Paper 04), internal fluctuations of τ are ALWAYS mean-field. Mean-field exponents are exact for the moduli sector.

The BCS transition, however, involves gap fluctuations spatially local in the 4D external space. For these, d_eff = 3, below d_uc = 4, so fluctuation corrections are quantitatively important. The Ginzburg number Gi = 0.25 (S43, BCS-CLASS-43; N_eff = 4 B2 modes) confirms fluctuations dominate near T_c.

**NEW (S53) — the Ginzburg number on the fabric and the Kohn-anomaly reclassification.** S53 (FABRIC-53) computed the Ginzburg fluctuation criterion directly on the deformed geometry: Gi_fluct ≈ 0.94 at d_eff = 8 and ≈ 0.51 in the 1D-modulus reduction — both O(1), confirming that the fabric sits in the strong-fluctuation regime near the fold (consistent with the BEC character, §VII.A4). S53 also examined whether the modulus effective mass softens at a specific τ — the geometric analog of a Kohn anomaly, where a phonon frequency is softened by a divergent (here spinor) density of states at a particular wavevector. After review (S53 baptista-volovik workshop) this was **reclassified from a Kohn anomaly to a backaction-drag effect**: the softening does not signal a structural instability of the kind a true Kohn anomaly implies, because the relevant Jensen-velocity projection v_J·(1,3,4) = 0 removes the destabilizing channel. The substrate-IS reading: the *fabric's modulus phonon is dressed by the spinor DOS*, but the dressing is a drag, not an instability.

**NEW (S65) — Mott inaccessibility.** Read as a Bose-Hubbard / Josephson-array system, the fabric could in principle undergo a superfluid→Mott-insulator transition when the charging energy E_C overwhelms the Josephson coupling E_J. It does not: E_J/E_C = 194 (S65), 571× above the critical ratio (E_J/E_C)_c ≈ 0.34 for the relevant coordination. The fabric sits deep in the superfluid (phase-coherent, Josephson-dominated) regime; the Mott insulator is inaccessible. The cosmological-constant route that would have exploited a Mott gap (S65 vortex_cc) is therefore closed by the substrate's own E_J/E_C ratio.

This *dual dimensionality* — d_int = 8 > d_uc for moduli, d_ext = 3 < d_uc for pairing — is a structural feature with no simple CM analog. Landau theory is simultaneously exact (internal geometry) and insufficient (BCS fluctuations) in the same system.

---

## III. The One-Body / Many-Body Partition

### III.A. The Diagnostic Pattern (refreshed to S93)

Session 44 produced the framework's sharpest structural separation between success and failure. The pattern survives intact to S93, and OCC-SPEC vindicates it.

**Successes (one-body spectral properties / response coefficients):**
- G_N from induced gravity: **PROVEN-CONDITIONAL**. Ratio 2.29 (0.36 OOM) at Λ = 10 M_KK (W1-1; three routes agree); 26.8 (1.43 OOM) at Λ = M_Pl. The framework does not fix the 4D UV cutoff, so the row is conditional, not bare. Post-S44 refinements SAKHAROV-PHONON-53 and SAKHAROV-GN-DIRAC (S75) reproduce the methodology.
- CDM by construction: PASS, T^{0i} = 0 algebraic (W1-2).
- Tensor-to-scalar ratio: PASS, self-consistently below all experiments (W3-4).
- DM/DE ratio: best route 1.060 (framework/observed = 2.74×; W6-4), with the post-S44 Leggett-channel route giving the actual DM mass anchor (§VIII).
- Bosonic a_2^{ζ}: PASS, a_2^{bos}/a_2^{Dirac} = 61/20 exact (W4-2).
- Second sound: PASS, Q = 75,989, undamped at all cosmological scales; observational horizon ℓ = 720.9 (S68; §VIII).
- Dissolution scaling: PASS, ε_c ~ 1/√N (W6-7).

**Failures (many-body correlations / ground-state properties):**
- Cosmological constant (CM-internal): FAIL/INFO. f_4/f_2 ~ 10⁻¹²¹. *Reframed* by DILUTION-CC (§VII.A7): the mismatch is real but the resolution is the cosmological tracking vacuum, not a CM-internal mechanism.
- Spectral tilt n_s via Lifshitz/KZ: FAIL. *Resolution moved* to geometry (§VI.C): n_s = 1 − 2ε_H = 0.9561.
- FRG/effacement: FAIL. BCS deviation 0.002% of the spectral action (W5-4); BDG-SA-61 condensate invisible at 1.36×10⁻⁴.
- **OCC-SPEC-45: CLOSED as FAIL — S_occ monotone decreasing (S45). This is the partition confirming itself** (§V/§VI).
- Pomeranchuk-on-GGE: FAIL (POMERANCHUK-GGE-58) — and *correctly* so: the GGE has no Fermi surface to destabilize. The Pomeranchuk criterion f_0 < −3 is a *one-body* Fermi-liquid statement (PERMANENT for the τ=0.30 spectrum, f_0 = −4.687); applied to the *many-body* GGE relic it has no Fermi surface to act on. The FAIL is informative, not a deficiency.

### III.B. Why the Partition Exists: Landau Theory

This partition has a precise origin in Landau's theory of interacting quantum systems, and it is not accidental.

**The spectral action is a one-body functional.** The spectral action S = Tr f(D²/Λ²) depends only on the eigenvalues {λ_k} of the Dirac operator — single-particle energies. In Landau's language (Paper 11, §3), it sees the quasiparticle dispersion ε_k (the renormalized single-particle spectrum) but not the interaction function f_{kk'}. It is the analog of computing a Fermi liquid's kinetic energy from the dispersion alone, ignoring the Landau parameters F_l^{s,a}.

**BCS pairing is off-diagonal long-range order.** The BCS ground state |BCS⟩ = ∏_k (u_k + v_k c†_↑ c†_↓)|0⟩ has a nonzero anomalous expectation ⟨c_↑ c_↓⟩ (Paper 15, §3). This off-diagonal order is invisible to any functional depending only on the diagonal one-body density matrix n_k = ⟨c†_k c_k⟩. The spectral action, a trace over one-body eigenvalues, is exactly such a diagonal functional. The effacement wall (S44 W5-4; BDG-SA-61 at 1.36×10⁻⁴) quantifies this: the BCS modification of the spectral action is 0.002–0.016%. The non-perturbative content — the exponential gap Δ_0 ~ exp(−1/V N(E_F)) (Paper 15), the phase coherence, the topological winding — lives in the off-diagonal sector no diagonal trace can access.

**Response coefficients are one-body; ground-state properties are many-body.** In Fermi-liquid theory (Paper 11, §5), susceptibilities χ, the effective mass m*, and the compressibility κ are expressible through the Landau parameters F_l and the quasiparticle spectrum — one-body quantities dressed by interactions. G_N, being the gravitational susceptibility (the metric's response to matter fluctuations), is exactly such a response coefficient, correctly captured by the spectral action. The vacuum energy, by contrast, is a ground-state property requiring the CORRELATED occupation numbers of all modes — a many-body quantity needing the full ground-state wavefunction. In Landau's language, the condensation energy E_cond = α²(T_c − T)²/(4β) (Paper 04, §4; Paper 08, §3) is the free-energy difference between ordered and disordered phases, which requires knowledge of BOTH phases, i.e. the interaction.

**NEW (S63) — the Resolvent–Fermi-liquid correspondence.** The S63 van-den-Dungen/Volovik workshop established a precise structural identity between the *resolvent* of D_K, (D_K − z)⁻¹, and the Fermi-liquid quasiparticle propagator G(ω, k) = [ω − ε_k − Σ(ω, k)]⁻¹. The resolvent's pole structure IS the quasiparticle dispersion; its residue IS the quasiparticle weight Z (computed at S85 as the ε_pivot/ε_fold ratio, Z ≈ 0.993). This sharpens the one-body statement: the spectral action is the trace of a function of the resolvent's poles, and so sees Z and ε_k but never the off-diagonal self-energy that encodes pairing. The substrate-IS reading: *the substrate's resolvent IS the quasiparticle propagator*; the framework's response-coefficient successes are exactly the quantities a Fermi-liquid propagator computes.

**Summary**: The framework's successes are response coefficients (G_N, χ, m*, transport). Its failures are ground-state properties (E_cond, Λ, Δ). The spectral action is the right description for the former and the wrong description for the latter. This is the expected behavior of any one-body trace functional applied to a many-body system. OCC-SPEC (§V) was the attempt to bridge the gap *within* the spectral-action formalism by weighting the trace with BCS occupation numbers; it failed because the BCS weighting is effaced. The next phase of the research must operate at the genuinely many-body level (the GGE response matrix, §IV.D).

---

## IV. The Specific Heat Exponent and DM/DE

### IV.A. The Observation

The observed ratio Ω_DM/Ω_DE = 0.264/0.685 = 0.385 is O(1). Both absolute scales — ρ_DM ~ 1.1×10⁻²⁹ g/cm³ and ρ_Λ ~ 5.96×10⁻³⁰ g/cm³ — are ~113 orders below Planck units. Yet their RATIO is O(1), with no small parameters.

Session 44 (W6-4, DM-DE-RATIO-44) computed this ratio through 11 methods, of which 7 fall within a factor 10 of observation. The best result: flat-band partition with Volovik vacuum response gives **1.060**.

### IV.B. The substitution chain for the "2.74×" tag

The S44 row called this "OPEN (2.7x)". Direction must be stated explicitly (math-scripts.md §"Double-Check Logic Before Compute"):

```
Claim: "the framework over-predicts the DM/DE ratio by 2.74×"
Step 1: Omega_DM_obs / Omega_DE_obs = 0.264 / 0.685 = 0.385          [canonical_constants: Planck 2020 DR2]
Step 2: framework best-route ratio (flat-band + Volovik vacuum)  = 1.060   [S44 DM-DE-RATIO-44]
Step 3: ratio_of_ratios = framework / observed = 1.060 / 0.385      [definition]
Step 4: = 2.753                                                     [simplified]
Step 5: 2.753 > 1  ⇒  the framework OVER-predicts the DM/DE ratio   [direction read from canonical form]
Conclusion: the "2.7x" tag is framework/observed ≈ 2.75 (an over-prediction), NOT a 2.7× suppression.
```

So the equilibrium flat-band route lands within a factor ~2.75 of observation. The exact factor depends on the dark-energy normalization; the *direction* is over-prediction.

### IV.C. The Normal / Superfluid Partition (Landau two-fluid)

In the two-fluid model (Paper 05, §2), the total density splits as ρ = ρ_s(T) + ρ_n(T). At T = 0, ρ_s = ρ; at T_c, ρ_n = ρ. The normal density at low T:

    ρ_n(T) ~ T⁴/c⁵    (phonon contribution)
    ρ_n(T) ~ T^{−1/2} exp(−Δ/k_B T)    (roton contribution)

**The cosmological analog.** Map ρ_s → Ω_DE (the "condensate" vacuum response), ρ_n → Ω_DM (the quasiparticle excitation energy gravitating as CDM), T → the effective GGE temperature. The ratio Ω_DM/Ω_DE is the cosmological analog of ρ_n/ρ_s, which is O(1) at temperatures of order T_c. The "coincidence problem" maps onto: why is the effective GGE temperature of order T_c for the BCS transition?

### IV.D. Why α_eff = 0.39 Requires Non-Equilibrium

The observed ratio implies α_eff ~ 0.39. In equilibrium, the known values are:

| System | α | Physical Origin |
|:--|:--|:--|
| Bose gas | 3 | C ~ T³ from phonons |
| Fermi gas | 2 | C ~ T from Pauli |
| 3D Ising | 0.110 | Critical fluctuations |
| Mean-field | 0 (jump) | No divergence |
| Flat band | 1 | C ~ T from flat DOS |
| XY (He-4) | −0.0146 | Weakly divergent (negative!) |

None match 0.39. The flat-band value α = 1 gives ratio 1.06 (over-prediction by 2.75×); the 3D Ising value α = 0.110 is too small. The GGE is NOT an equilibrium system: it has 8 independent temperatures (S44 W6-5, MULTI-T-JACOBSON-44), 3 of them negative. The effective specific heat is

    C_GGE = Σ_k (∂E/∂T_k)(∂T_k/∂T_eff)

where the effective temperature and projection depend on the thermodynamic prescription. Session 44 found w_eff ranges from 0.132 (grand potential) to 0.387 (Jacobson), so the GGE admits no unique EOS parameter.

**The computation that would nail it** (a well-posed S94+ gate): (1) take the 8 Richardson-Gaudin integrals I_k at the post-transit state; (2) compute the GGE Lagrange multipliers (the "8 temperatures") from ⟨I_k⟩_initial = ⟨I_k⟩_GGE; (3) form the response matrix C_{kl} = ∂E_k/∂T_l; (4) diagonalize (3 negative eigenvalues from MULTI-T-JACOBSON-44); (5) define α_eff = Ω_DM/Ω_DE from the eigenvalue spectrum. The negative-temperature sectors may produce the sublinear α_eff. **This remains the open quantitative DM/DE computation.** It is distinct from the Leggett-channel route (§VIII), which gives a DM *mass anchor* rather than the DM/DE *ratio*.

### IV.E. Connection to Landau Papers

Paper 04 (Phase Transitions), §4: the specific-heat jump ΔC = a_0²/(2b T_c) is material-specific, but the *existence* of a finite jump (α = 0 mean-field) is universal. Paper 05 (Superfluidity), §2: ρ_n/ρ = 1 at T_c and 0 at T = 0; at intermediate T it depends on the excitation spectrum through universal functions — the direct basis for the DM/DE = 1.060 flat-band result. Paper 11 (Fermi Liquid), §5: γ = (π²/3)k_B² N(0) = (m*/m)γ_free — thermodynamic ratios depend on a few dimensionless parameters, not the UV cutoff.

### IV.F. NEW (S50/S84/S89) — α_s = n_s² − 1 as a Mellin-residue running coupling

The framework carries a running-coupling identity with a Landau-pole heritage: the scalar-running α_s satisfies the algebraic identity α_s = n_s² − 1, exact in ℚ (S88 W-15: n_s_FW_exact = 9561/10000, n_s² − 1 = −8587279/10⁸ a perfect-square identity). For n_s < 1 (red tilt) this is automatically negative — a purely algebraic consequence of any single-pole rational propagator (S84 Feynman synthesis), i.e. of the resolvent's single-pole structure (§III.B). **Scale-and-channel-tagging (S92 AH-TR-1)**: the substrate carries TWO scale-separated α_s observables — a substrate-distance running −0.08587279 (Mellin residue at the s=3 pole, *inside* the Brillouin zone) and a Goldstone-pivot running ≈ 0 (P_{∇φ} = K⁰ at the CMB pivot). Which one a detector measures is set by the transport degree deg(T_{BZ→pivot}). The substrate-IS reading: α_s is a Mellin residue of D_K's spectral zeta function, not a phenomenological QCD coupling; its sign is locked to the tilt by the rational-propagator structure.

---

## V. The Occupied-State Spectral Action — the Bridge that FAILED

> **This section is rewritten to its closed verdict.** The S44 document presented OCC-SPEC as "the single most important open computation in the framework" and predicted a non-monotone minimum near τ=0.19. The gate ran at S45 and the prediction was falsified. The corrected account follows.

### V.A. The Problem

The S37 Structural Monotonicity Theorem (CUTOFF-SA-37) proved that for any monotone-decreasing cutoff f, the vacuum spectral action S(τ) = Tr f(D_K(τ)²/Λ²) is monotone increasing in τ. This closed τ-stabilization through the vacuum spectral action; 27 subsequent mechanisms followed (`spectral-post-mortem.md`). The spectral action, summing over all modes with equal weight, cannot develop a minimum because the high-eigenvalue tail dominates and grows monotonically (Weyl's law on the deformed SU(3)).

### V.B. The Proposed Loophole

The S37 theorem sums over all modes EQUALLY. The physical system does not. In the BCS ground state the occupation numbers are

    n_k(τ) = v_k(τ)² = (1/2)(1 − ξ_k(τ)/E_k(τ)),    E_k = √(ξ_k² + Δ(τ)²)

which depend on τ through both the eigenvalues λ_k(τ) AND the self-consistent gap Δ(τ). The occupied-state spectral action (Connes/16, Dong-Khalkhali-van Suijlekom 2022; pre-registered as OCC-SPEC-45) is

    S_occ(τ) = Σ_k d_k · n_k(τ) · f(λ_k(τ)²/Λ²)        (1)

The n_k(τ) weighting breaks condition 3 of the S37 theorem (unit weight on all modes), because n_k is not monotone in τ. The hope was that S_occ — the Landau free energy at the *physical state* F(η_0), as opposed to the vacuum F(0) — could develop the well that the vacuum S cannot.

### V.C. The Landau Identification (correct in spirit)

In Landau theory the physical free energy is F(η_0) evaluated at the equilibrium order parameter, and F(η_0) − F(0) = −a_0²(T_c − T)²/(4b) = F_cond < 0. The vacuum spectral action S(τ) is F(0); the occupied-state S_occ(τ) is F(η_0). The S37 theorem proves F(0) monotone but says nothing about F(η_0). The intuition — that the negative condensation energy F_cond, peaking near the van Hove near-crossing at τ=0.19, could pull S_occ down into a well — is a correct *Landau* intuition. It is simply quantitatively dominated.

### V.D. The Van Hove Near-Crossing at τ = 0.19

S44 W6-8 (VAN-HOVE-TRACK-44) tracked 12 van Hove trajectories; at τ=0.19 three (T3, T4, T5) approach within δ = 0.0008. This concentrates the DOS, spiking the BCS pairing (the gap equation 1/g = Σ_k 1/(2E_k) is dominated by modes near the van Hove point where 1/E_k ~ 1/Δ is large). The gap Δ(τ) therefore peaks near τ=0.19 and the gap-edge occupation numbers change rapidly. The hope: if these modes' eigenvalues are simultaneously stiffening, the product n_k·f(λ_k²) could decrease, creating a turning point.

### V.E. The Verdict — S_occ is MONOTONE DECREASING (OCC-SPEC-45 FAIL)

At S45 the gate ran. **`OCC-SPEC-45` returned FAIL: S_occ(τ) is monotone decreasing at all Λ and all τ in [0.00, 0.50]** — the "28th equilibrium closure" (atlas-07 #42; session-45-results-workingpaper). There is no local minimum. The pre-registered PASS criterion (a minimum in [0.10, 0.25] with barrier > 0.01·S_occ) was not met; there was not even an INFO-level shallow minimum.

**Why it failed — the partition confirming itself.** The substitution chain is the one-body/many-body partition of §III:

```
Claim: "the BCS occupation weighting cannot overturn the Weyl-law monotonicity"
Step 1: S_occ(τ) = Σ_k d_k n_k(τ) f(λ_k²/Λ²);  dS_occ/dτ = Σ_k [(dn_k/dτ) f + n_k f' · 2λ_k (dλ_k/dτ)]   [definition, eq. (1)]
Step 2: the SECOND term has the S37 sign (f' < 0, Σ λ_k dλ_k/dτ > 0 ⇒ negative contribution to dS/dτ for the standard convention)   [S37 theorem]
Step 3: the FIRST term (occupation-change) is the ONLY term that could flip the sign; its weight relative to the vacuum trace is the effacement ratio ≈ 0.002%   [W5-4 effacement wall; BDG-SA-61 = 1.36e-4]
Step 4: |first term| / |second term| ~ 10^{-5} ≪ 1     [effacement wall magnitude]
Step 5: the occupation-change term cannot overwhelm the monotone term ⇒ S_occ inherits the monotonicity   [direction from canonical form]
Conclusion: S_occ is monotone — the same effacement that makes BCS invisible to the vacuum action makes it
            unable to bend the occupied action. The one-body/many-body partition (§III) IS the reason OCC-SPEC failed.
```

The Landau-`F(η_0)` non-monotonicity is real *in the off-diagonal sector* — but that sector contributes only 0.002% of the one-body trace, far too little to overturn Weyl's law. OCC-SPEC was the cleanest possible test of whether the one-body/many-body bridge could be built inside the spectral-action formalism. The answer is no. This is not a failure of the framework; it is the partition diagnosing its own boundary. The genuinely many-body bridge must be the GGE response matrix (§IV.D), not a reweighted one-body trace.

### V.F. Consequence for the e-fold count

S22d found that the Friedmann equation with the *vacuum* spectral-action potential gives ~1 e-fold near τ=0.3 (60× too few for inflation). The S44 doc speculated that if S_occ had a minimum, the well's oscillation could supply the missing e-folds. With OCC-SPEC FAIL, that route is closed: there is no occupied-state well. This is consistent with the framework's mature paradigm (`project_friedmann-wrong-question`): exflation is a *supersonic transit* through the fold (Mach 13.75, impulsive), not slow-roll in a potential well — so the absence of a well is expected, not a deficit. The n_s tilt does not come from oscillation in a well; it comes from spectral geometry (§VI.C).

---

## VI. Predictions from the Landau Mapping — Scored at S93

The S44 document made five predictions for S45. They have since been scored. This section reports the outcomes honestly.

### VI.A. OCC-SPEC-45 — predicted non-monotone; **OUTCOME: FAIL (monotone)** ✗

The prediction was a non-monotone minimum near τ=0.19. **It was falsified** (§V.E): S_occ is monotone decreasing. The Landau intuition (negative condensation energy peaking at the van Hove point) was structurally correct but quantitatively dominated by the effacement wall (~10⁻⁵). Scored: the mapping did its job — it generated a sharp, falsifiable prediction, and the framework's own effacement physics falsified it. A wrong prediction tested and closed is worth more than a vague one left open.

### VI.B. q-Theory on the GGE — predicted ρ(q_0) = 0 post-transit — **OUTCOME: borne out, with caveat** ✓(cond.)

In Volovik's q-theory the vacuum variable self-tunes to ρ(q_0) = 0 through the Gibbs-Duhem identity. Post-transit Δ = 0 (P_exc = 1.000), so all BCS condensation energy vanishes identically (S44 W1-4); the GGE energy gravitates as CDM. The Landau analog: in the disordered phase the condensation energy is exactly zero. This is borne out — and it is the seed of DILUTION-CC (§VII.A7), where the *residual* vacuum tracks ρ_matter via ρ_vac ~ M_Pl² H², closing the 114-order hierarchy to CC_OOM = 115.5 with ρ_vac/ρ_obs = 1.032 (S66). **Caveat preserved**: this uses q-theory's *equilibrium* Gibbs-Duhem identity; whether the GGE's 8 conserved integrals produce a generalized Gibbs-Duhem relation is the open computation of §IV.D.

### VI.C. KZ Bogoliubov spectrum — predicted n_s too red — **OUTCOME: CONFIRMED, and the resolution moved off KZ** ✓

The S44 prediction: the Kibble-Zurek formula with the framework's dynamic exponents CANNOT give n_s = 0.965. With d=3, z=2.024, ν=0.6301 the KZ formula gives n_s − 1 = −d·z·ν/(1+z·ν) = −1.681 ⇒ n_s = −0.68; even the d=1 reduction gives n_s = 0.44. **This was confirmed**: no combination of d ∈ {1,2,3} with the framework's exponents lands in the Planck window. The mapping was constraining, not confirming — and it was *right* to constrain.

**The resolution then moved entirely off Kibble-Zurek onto spectral geometry** (the post-S44 development the S44 doc could not see). The **Mode-Independent Occupation Theorem** (S57, baseline-findings #21) proves that the scalar tilt is independent of the Bogoliubov occupation — it comes from geometry only, not from quench dynamics. The current result is

    n_s = 1 − 2ε_H  =  0.9561                              (geometric tilt; S57/S73a COMPOUND-NS-73a/S86 W1c-8)

cutoff-INDEPENDENT, where the tilt-relevant slow-roll bound is ε_H_W6 = 0.02163 (S80 dS/dτ at the fold), NOT the Lifshitz-η value 3.0 (a different quantity the S44 doc conflated). So the S44 "most severe deficit" is resolved: the KZ route is genuinely too red (confirmed), but the substrate never used the KZ route — the tilt is a geometric property of D_K's spectral action. The substrate-IS reading: *n_s IS the second spectral moment ratio of D_K's slow-roll evolution*, an intrinsic property of the spectral triple, measured at the CMB pivot.

### VI.D. Non-equilibrium α from the GGE — predicted 0.2 < α_eff < 0.6 — **OUTCOME: open** ○

The prediction range brackets the observed α_eff ≈ 0.39. The full GGE response-matrix computation (§IV.D) has not been run; w_eff ranges 0.132–0.387 across prescriptions (S44 W6-5), consistent with the range but not yet a single value. This remains the open quantitative DM/DE computation. The S44 framing stands: α_eff is likely a property of the specific quench protocol (the transit), not an equilibrium critical exponent — which would make DM/DE a *prediction* (computable from the transit) rather than an input.

### VI.E. Quasiparticle lifetime — predicted infinite — **OUTCOME: confirmed (integrability-protected)** ✓

In a Fermi liquid 1/τ_qp ~ (ε − ε_F)² (Paper 11). In the integrable GGE relic, the Richardson-Gaudin conserved integrals protect the quasiparticles: Γ_q(BCS) = 0 exactly (S62). The relic's excitations are infinitely long-lived — the Ordered Veil (§X). This is the deepest structural reason the relic never thermalizes.

### VI.F. Summary of the Scorecard

| Prediction | S44 expectation | S93 outcome | Basis |
|:--|:--|:--|:--|
| OCC-SPEC-45 | non-monotone, min near τ=0.19 | **FAIL (monotone)** | effacement wall 10⁻⁵ dominates (§V.E) |
| q-theory on GGE | ρ_vac = 0 post-transit | borne out → DILUTION-CC | disordered-phase E_cond = 0 (§VII.A7) |
| KZ Bogoliubov n_s | too red | confirmed; resolution → geometry | n_s = 1 − 2ε_H = 0.9561 (§VI.C) |
| GGE α_eff | 0.2 < α < 0.6 | open (w_eff 0.132–0.387) | constrained-saddle thermodynamics (§IV.D) |
| Quasiparticle lifetime | infinite | confirmed (Γ_q = 0) | Richardson-Gaudin integrability (§X) |

Three confirmed, one falsified, one open. The falsified one (OCC-SPEC) is the most informative: it closed a corridor and vindicated the one-body/many-body partition.

---

## VII. Limitations of the Mapping (refreshed; one lifted, one reframed)

### VII.A. Where the Analogy Breaks

1. **No laboratory — PARTIALLY LIFTED (S86/S87).** The S44 doc's first limitation was that the framework IS the universe, with no external bath, reference frame, or probe. This is still true of the *whole* system — but the framework now has a genuine laboratory falsifier via the **³He-B inheritance morphism** (§XII). The substrate's BDI cocycle structure projects (under the inheritance morphism χ: ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)) onto a ³He-B BdG observable: the Caroli-Matricon vortex-core spectroscopy, with a substrate-derived cocycle ratio φ_67/φ_88 = 7.324992 preserved INTACT in the laboratory measurement (the (Δ_B/Δ_A)^p conversion factor cancels exactly). Lancaster MCT-3 and Helsinki ROTA cells can test it (Window-11; S87-W11-C5 PASS). So one CM system — ³He-B — IS a child of the substrate, not merely an analogy to it, and it provides an external probe. The limitation is lifted *for the ³He-B sector*; it stands for the framework as a whole.

2. **The dimensionality mismatch (unchanged).** The internal space is 8-dimensional; no laboratory system has d_int = 8. d_uc = 4 ≪ d_int makes mean-field exact for internal fluctuations — a regime never achieved in real materials. The quantitative predictions for internal fluctuations are in an untested regime of Landau theory. (The BCS-sector predictions at d_ext = 3 are *not* in this regime; they are testable, and ³He-B tests them.)

3. **The modulus is not a local field (unchanged, with substrate-IS refinement).** In standard Landau theory the order parameter φ(x) is a local field. The Jensen modulus τ is GLOBAL — it describes the metric on the entire SU(3) fiber. There is no τ(x) varying in 4D space within the homogeneous framework. Substrate-IS refinement: this is not a defect of the substrate but a *fact about what the substrate IS* — the fiber is not in space; it is the structure at each point. The two substrate-IS levels (single-τ-slice vs the moduli-space of τ-deformations, per `phononic-framing.md`) are both intrinsic, neither a coordinate on a meta-container. Kibble-Zurek (assuming a spatially varying order parameter) does not apply to a global modulus — which is *why* the n_s tilt is geometric, not KZ (§VI.C).

4. **The BCS-BEC crossover position — refined (S61).** The framework sits at E_vac/E_cond = 28.8 (S37), deep in the BEC regime (g·N = 2.18). S61 (BEC-61) refined this with an N-pair scan: N=1 is BEC (n_0/N = 1.0), N=2 BEC-crossover (0.52), N=3 crossover (0.35), N=4 BCS-crossover (0.27). The single-cell physics is BEC; the multi-cell physics crosses toward BCS as pairs are added. Standard BCS formalism (gap equation, Bogoliubov amplitudes) is used in a regime where the Gross-Pitaevskii description of tightly-bound pairs (Paper 08 GL functional) may be more appropriate. The S37 "fluctuations dominate by 29×" is consistent with BEC character, as is Gi ≈ 0.94 (§II.C).

5. **Time-reversal and the arrow of time (unchanged).** In CM the system cools from disorder into order. In the framework the transit goes from an unstable maximum (τ=0) THROUGH the ordered BCS phase to a disordered GGE (Δ=0). The direction is REVERSED: the condensate is created and destroyed during the transit, not maintained as a stable ground state. This inverts the standard order/energy relationship.

6. **No external tuning parameter (unchanged).** The transit is AUTONOMOUS — τ evolves under the spectral-action gradient dV/dτ with no external control. τ is both order parameter and driving force. This self-referential structure resembles self-consistent mean-field (Hartree-Fock) but has no direct CM analog.

7. **The CC problem — REFRAMED by DILUTION-CC (S66).** No CM system has a "cosmological constant problem"; the zero-point energy of a crystal or superfluid is finite, calculable, and Casimir-measurable. The Landau mapping correctly identifies the 121-order hierarchy as a **universality-class mismatch** — G_N (second spectral moment a_2) and Λ (zeroth moment a_0) are controlled by different physics, "computing one from the other is a category error" (App. C). What is NEW: the framework's cosmological resolution is the **Volovik tracking vacuum** (DILUTION-CC-66): the residual vacuum tracks ρ_matter via ρ_vac ~ M_Pl² H², diluting the 114-order excess to CC_OOM = 115.5 with ρ_vac/ρ_obs = 1.032. So the mismatch is real *as CM physics* (the moments differ), but the resolution is *cosmological* (the tracking vacuum), not CM-internal. No CM system exhibits the tracking because no CM system is its own expanding cosmology.

8. **Emergent spacetime (unchanged — the deepest limitation).** Landau theory assumes a pre-existing thermodynamic framework (temperature, volume, pressure), which requires spacetime. If spacetime emerges from the order parameter (the framework's claim), the Landau expansion itself is part of the emergent description, not a fundamental one. This is the deepest limitation, and it is the one the substrate-IS framing is built to handle: the spectral action IS the sum over geometries, gravity IS the second spectral moment, so the "thermodynamic framework" the Landau expansion presupposes is itself a derived a_2 image. Landau theory is the effective-description layer; the spectral triple is logically prior.

### VII.B. What the Limitations Teach (refreshed)

The limitations still cluster around a single theme: the phonon-exflation framework is a CLOSED SYSTEM describing the entire universe, while Landau theory was developed for OPEN SUBSYSTEMS in a larger environment. But the cluster has shifted in two ways since S44:

- **Limitation #1 (no laboratory) is now partly lifted** — ³He-B is a genuine child, with a falsifier. The framework is no longer purely closed for observational purposes; it has a window onto a laboratory analog of one of its sectors.
- **Limitation #7 (CC) is reframed, not just diagnosed** — DILUTION-CC supplies the cosmological resolution the CM analogy could not.

The mapping works wherever the framework is a subsystem with effective parameters (G_N as response coefficient, DM/DE as specific-heat exponent, BCS universality class, van Hove classification, ³He-B inheritance). It fails wherever the SELF-REFERENTIAL nature becomes essential (the residual after DILUTION-CC, emergent spacetime). The mapping tells you WHERE to look for new physics — at the boundary between open and closed system descriptions — and that boundary is now mapped more finely than it was at S44.

---

## VIII. The Leggett-Channel Dark Matter (NEW, S49→S70)

> The first explicit dark-matter *mass anchor* the framework produced. It is the single most important post-S44 addition to the DM side of the mapping, and it is a pure Landau two-fluid / Fermi-liquid result.

### VIII.A. The Leggett mode IS a phason of the B2–B3 sector

In a two-band superconductor the relative phase of the two condensates oscillates: the **Leggett mode** (A. J. Leggett, 1966), an inter-band collective excitation. In the substrate, the B2 and B3 bands carry distinct K_7 content, and their relative U(1)_7 phase is the substrate's Leggett mode — a phason of the B2–B3 sector. Its mass comes from the inter-band Josephson coupling: when the mass m in the Ornstein-Zernike propagator G⁻¹_{ab}(K) = ρ_s^a K² δ_{ab} + M²_{ab} arises from inter-band Josephson coupling rather than an on-site potential, the propagator's mass gap IS the Leggett frequency (S49 landau-collab):

    ω²(n) = ω_L1² + c_G² K²,    ω_L1 = 0.138 M_KK,   m_L1 = 0.070 M_KK,   c_Gold = 0.915

(m_L1 is the Goldstone mass from U(1)_7 breaking — a `# (local)` quantity, S80 WP / S49 DIPOLAR-CATALOG, *not* a canonical constant.) The substrate-IS reading: dark matter IS a phason of the substrate's B2–B3 inter-band sector — an inter-band phase excitation of D_K's spectrum, not a relic particle propagating through a spatial container.

### VIII.B. The mass anchor (LEGGETT-MOMENT-70)

S70 (LEGGETT-MOMENT-70; atlas-10 #23; Door-S70) established the first Type-F dark-matter mass anchor at zero geometric free parameters:

    Mass_LeggettDM / Δ_BCS = 11.97

with Δ_BCS = 0.4642547 M_KK the canonical (R-protected) BCS gap. "Type-F" means the observable is a single-summand-projection trace on the substrate algebra — algebra-INVARIANT, spectrum-only, the cleanest class in the algebra-axis orthogonality classification. The Leggett mode closes as a Type-F observable (W18, Door-S70): the DM mass is a spectral moment of the B2–B3 inter-band sector, computed from D_K's eigenvalues, not fitted.

### VIII.C. The abundance and the undamped mode

The Leggett-only contribution to the relic abundance is Ω_DM h² = 0.1200 (Leggett-only = 0.03985 × 3.010), at **0.6% from the Planck value** 0.1200 ± 0.0012. The mode is essentially undamped — a two-fluid undamped collective oscillation in the second-sound class — with quality factor

    Q_Leggett = 670,000

(S50 LEGGETT-DAMPING-50; get_constant Q_Leggett = 6.7×10⁵). This is the Landau two-fluid signature: an inter-band phase oscillation that does not decay because there is no normal-fluid channel to dissipate into (the relic is integrable, §X). The substrate-IS reading: the DM relic IS an undamped phason whose abundance is set by its spectral mass and the transit's pair-production yield, gravitating as CDM (T^{0i} = 0) because it is a phase oscillation at rest.

### VIII.D. Status: PROVEN-CONDITIONAL

The anchor is CONDITIONAL (atlas-04 C11/P2) on (i) the gravitational survival Γ_grav < H_0 (LEGGETT-GRAV-DECAY-67) and (ii) the dipolar-mass calibration (within 18% of the ³He analog). The "mass problem" — a 170× discrepancy in one normalization — is what the conditionality tracks. But the central result stands: the framework produces a DM mass within 0.6% of the observed relic abundance from zero geometric free parameters, as a Landau inter-band collective mode. Per the framework's evidence-weighting (`evoi-prioritization.md`), a PASS within 0.6% across a multi-OOM prediction space from zero free parameters is strong evidence, not a coincidence.

### VIII.E. The second-sound observational horizon

The Leggett/second-sound physics has an observational signature in the CMB (S53 CMB-53; S68 OBS-68): the two-sound hierarchy gives a geometric horizon ℓ_geom = π (full sky) and a pair-acoustic horizon ℓ_second_sound = π·c_fabric/c_Gold = 720.9. The substrate carries two sound speeds — the fast geometric c_fabric and the slow Goldstone c_Gold = 0.915 — and their ratio (229×) sets the second-sound CMB multipole. This is the acoustic signature of the GGE relic, not thermal equilibrium radiation.

---

## IX. The Volovik Free-Energy Partition (NEW, S58/S62)

> How the condensation free energy of the BCS sector divides between the vacuum and the matter channels. This is the quantitative content the S44 doc's §IV.C two-fluid argument anticipated but could not compute.

### IX.A. The partition

S58/S62 (PARTITION-58/62; baseline-findings #27) computed the partition of the total condensation free energy at the fold into a Josephson (vacuum) channel and the quasiparticle (matter) channels:

    F_Josephson = −336.6 M_KK   →  95.9% → vacuum
    F_BCS + F_BA + F_Leggett = 14.411 M_KK  →  matter

The matter-channel BCS condensation energy is the canonical E_cond = −0.13685 M_KK (S36 ED-CONV-36, 8-mode 4B2+1B1+3B3, 256-state exact diagonalization; the GL functional gives the close value E_cond_GL = −0.156 M_KK). This is the same condensation energy that appears in the instanton ratio E_exc/|E_cond| = 443 (§II.B note 5) and the BCS gap Δ_BCS = 0.4642547 M_KK; the Josephson channel above is ~2460× larger because it is the phase-coherence energy of the entire coarse-grained fabric, not the pairing energy of the 8-mode BCS subsystem.

The substitution chain for the direction:

```
Claim: "the Josephson channel carries 95.9% of the partition → vacuum"
Step 1: F_Josephson = -336.6 M_KK  (Josephson coupling free energy)        [S58 PARTITION-58]
Step 2: F_matter = F_BCS + F_BA + F_Leggett = 14.411 M_KK  (quasiparticle channels)  [S58]
Step 3: |F_Josephson| / (|F_Josephson| + F_matter) = 336.6 / (336.6 + 14.411)  [definition of the fraction]
Step 4: = 336.6 / 351.0 = 0.959                                            [simplified]
Step 5: 0.959 > 0.5 ⇒ the Josephson (vacuum) channel DOMINATES the partition  [direction]
Conclusion: 95.9% of the condensation free energy is in the Josephson channel → vacuum; 4.1% → matter quasiparticles.
```

### IX.B. The substrate-IS reading

This is the Landau condensation-energy partition (Paper 04, §4; Paper 05) made concrete on the substrate. The Josephson channel — the phase-coherence energy of the coarse-grained fabric — IS the vacuum response (it feeds the canonical w0_FW = −0.918, with the effacement efficiency Γ_eff = 0.99970, S58). The quasiparticle channels (BCS pairing, Bogoliubov-Anderson sound, Leggett phason) ARE the matter. The substrate-IS direction: the condensation free energy of the BCS sector partitions itself; the 95.9% Josephson fraction is the vacuum's share, the 4.1% quasiparticle fraction is matter's share. This is NOT "the universe has dark energy"; it is "the spectral triple's condensation free energy divides between its Josephson and quasiparticle channels in a 24:1 ratio."

### IX.C. Connection to DILUTION-CC

The Volovik partition is the bridge between the BCS condensation energy and the cosmological constant. The Josephson-channel vacuum energy is not a static Λ; it is a *tracking* vacuum (q-theory, §VI.B/§VII.A7) whose residual after the matter-tracking response is CC_OOM = 115.5 below the bare value (DILUTION-CC-66). So the partition (S58) and the dilution (S66) compose: the partition says 95.9% goes to vacuum; the dilution says that vacuum then tracks ρ_matter, leaving the observed Λ. Both are Volovik's self-sustained-vacuum physics (Paper 04 q-theory), expressed in the substrate's BCS sector.

---

## X. GGE Permanence and the Ordered Veil (NEW; the deepest post-S44 structural result)

> The post-transit relic never thermalizes — but this is a *sector-resolved* statement, and the honesty of the distinction matters. This section states it precisely.

### X.A. The two-layer subtlety (stated honestly)

The phrase "the GGE never thermalizes" is true in one sector and false in another:

- **At the FULL-isometry level: RETRACTED (S39).** The early "GGE permanence" claim (S38) was *retracted* at S39: the full physical Hamiltonian V_phys is 13% non-separable, Brody β = 0.633 (63% GOE — level repulsion, the signature of chaos), and t_therm ~ 6 natural units. The GGE is valid *during the transit* but the full isometry algebra does thermalize on a finite timescale (atlas-04 T3, BROKEN).
- **In the BCS sector: PERMANENT (S62).** The BCS-sector relic — the one that carries the dark matter and the Meissner physics — IS integrable. Door-S62-Meissner establishes that Meissner permanence follows from Richardson-Gaudin integrability, not from the spectral action. At the physical filling 0.15 the level statistics are sub-Poisson (⟨r⟩ ≈ 0.321–0.337 < 0.45, Brody β ≈ 0.001 in the (2,1) sector, S53), the Berry-Tabor signature of integrability and the *absence* of level repulsion.

The substrate-IS reading: the *BCS sector* of the spectral triple is an integrable system protected by 8 Richardson-Gaudin conserved integrals; that sector's relic is the Ordered Veil and it does not thermalize. The *full isometry algebra* is not integrable and does thermalize. G2 readers must not flatten this into "the universe never thermalizes" — the permanence is a property of the BCS sector, and it is what protects the Leggett DM relic (§VIII).

### X.B. The Richardson-Gaudin integrals

The BCS pairing Hamiltonian on a discrete level set is exactly solvable by Richardson's 1963 ansatz (Paper 16):

    ε_a + G/2 = Σ_{b≠a} 2G/(z_a − z_b) + Σ_i G/(z_a − ε_i)        (Richardson equations)

with 8 conserved integrals I_k (the Gaudin Hamiltonians) for the 8-mode BCS system (4 B2 + 1 B1 + 3 B3). The GGE density matrix is ρ_GGE = Z⁻¹ exp(−Σ_k λ_k I_k) (Paper 20). The conserved integrals freeze the post-transit occupation numbers: f_GGE(ω_k) = 1/(exp(Σ_i β_i I_i(k)) − 1), and the relic carries S_GGE = 3.542 bits of entropy (S38). Because the integrals are conserved, the quasiparticle decay rate Γ_q(BCS) = 0 exactly (S62) — infinite lifetime (§VI.E).

### X.C. The Thouless time from the Cayley-graph Laplacian

The permanence question reduces to a diffusion problem on the 24-vertex Cayley graph CG(24) = Cayley(S_4, all 6 transpositions). The Thouless time — the timescale over which a perturbation diffuses across the graph — is set by the spectral gap of the graph Laplacian:

    t_Th = 1 / (E_J · λ_1(L_graph))        (S60/S61 thouless_cayley, THERM-61)

A large Thouless time relative to the transit time means the relic cannot equilibrate across the fabric during the transit — the structural origin of the Ordered Veil (S38: t_scr/t_transit = 814). The substrate-IS reading: the relic IS a non-thermal state on the fabric's graph, and the graph's spectral gap sets how long it stays non-thermal.

### X.D. Generalized Landau-Khalatnikov / two-fluid (S67)

The standard Landau-Khalatnikov relaxation dφ/dt = −(1/τ_0)(dF/dφ) (Paper 09) assumes equilibrium relaxation toward the free-energy minimum. S67 (GGE-TWO-FLUID-67/FLUID-67) generalized the two-fluid model to a GGE normal component: the "normal fluid" is not a thermal gas of quasiparticles but the GGE relic, with frozen (non-thermal) occupation numbers. The relaxation is then governed by the conserved integrals, not by a single relaxation time τ_0. This is the framework's two-fluid model: a superfluid (the surviving condensate / vacuum) plus a GGE normal component (the relic). The substrate-IS reading: the post-transit fabric IS a two-fluid system whose normal component is integrable, not thermal — so Landau-Khalatnikov relaxation generalizes to GGE dynamics, and the relic persists.

---

## XI. BKT and the Superfluid-Stiffness Tensor on the Discrete Fabric (NEW, S47/S56/S74)

> The Ginzburg-Landau phase-coherence physics, computed on the substrate's coarse-grained Cayley-graph fabric. The phase stiffness is a tensor on the Lie algebra, and it is strongly anisotropic.

### XI.A. The superfluid-stiffness tensor (S47)

The superfluid density is not a scalar on the substrate; it is a tensor ρ_s^{ab} measuring the free-energy cost of a phase gradient in direction a of the Lie algebra (S47 wave3d):

    F(q) = F(0) + (1/2) Σ_{ab} ρ_s^{ab} q_a q_b

S47 (TENSOR-47) computed it: ρ_s(C²) = 7.96 (the C² Casimir direction) vs ρ_s(u(1)) = 0.33 (the U(1) direction) — a **24× anisotropy**. The Casimir direction is 24× stiffer than the U(1) direction.

```
Claim: "the phase stiffness is 24× anisotropic (C² stiffer than u(1))"
Step 1: rho_s(C^2) = 7.96   (Casimir-direction superfluid stiffness)        [S47 TENSOR-47]
Step 2: rho_s(u(1)) = 0.33  (U(1)-direction superfluid stiffness)           [S47 TENSOR-47]
Step 3: anisotropy ratio = rho_s(C^2) / rho_s(u(1)) = 7.96 / 0.33           [definition]
Step 4: = 24.1                                                              [simplified]
Step 5: 24.1 > 1 ⇒ the C² direction is 24× STIFFER than the u(1) direction  [direction]
Conclusion: the phase stiffness tensor is 24× anisotropic; the Casimir direction dominates.
```

S47 also found a curvature-stiffness anti-correlation, r = −0.906 (p = 0.002): directions of high Ricci curvature have low phase stiffness. The substrate-IS reading: the fabric's phase stiffness IS a tensor on su(3), and its anisotropy IS a property of the Jensen-deformed geometry — the C² Casimir direction resists phase gradients 24× more than the U(1) direction.

### XI.B. The Goldstone phase propagator and the Leggett mass

The Goldstone phase propagator on the Josephson lattice is G⁻¹(K) = ρ_s K² + m_G², with the K² term protected by the Goldstone theorem and m_G = 0.070 M_KK the Leggett mass (§VIII; S47–48, MASS-48). So the same stiffness tensor that sets the BKT temperature (below) sets the dispersion of the Leggett DM mode. The substrate-IS reading: the DM phason propagates through the fabric with a stiffness-set sound speed c_Gold = 0.915 and a Leggett mass gap m_L1 = 0.070 M_KK.

### XI.C. BKT on the finite graph (S56/S74)

With the stiffness tensor in hand, the Berezinskii-Kosterlitz-Thouless vortex-unbinding transition on the fabric follows. For a 2D-XY system the universal BKT relation is

    T_BKT = (π/2) · ρ_s_eff

(S56 plan; S74 RESOLVED-74, sector-resolved). At the fold (τ = 0.1939), E_J = 3.890 M_KK gives T_BKT = 6.111 M_KK; the BKT temperature ranges from 16.633 M_KK at τ = 0 to 0.879 M_KK at τ = 0.5 (S56). Because the transition is BKT (infinite-order, essential singularity), vortex production is exponentially suppressed (exp(−708)) — which is why the cosmic-string GW channel is closed (`closed-gw-channels.md`) and why the fabric's phase coherence is robust. The substrate-IS reading: the coarse-grained fabric IS a 2D-XY system, its phase-coherence transition IS BKT, and the exponential vortex suppression IS the reason the framework predicts no observable cosmic-string GW background. S74 resolved the sector-by-sector structure: different (p,q) sectors have different BKT temperatures, and the transition is dominated by the stiffest (C²) direction.

---

## XII. The ³He-B Inheritance Morphism — a Cross-Pillar Bridge to a Laboratory Falsifier (NEW, S86/S87/S90)

> This is the section that lifts limitation #1 ("no laboratory"). It is written with the 5-anatomy + 3-level cross-pillar-bridge discipline (`cross-pillar-bridge-anatomy.md`): substrate-IS observable → bridge map → laboratory-IN observable, with the direction of explanation flowing FROM the substrate TOWARD the laboratory.

### XII.A. The inheritance morphism (parent → child, NOT analogy)

The substrate's finite spectral triple is `(A_K, H_K, D_K)` with A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ). The **inheritance morphism** is the algebra projection

    χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ),   sending M_3(ℂ) → 0

onto the ³He-B BdG sector. ³He-B is in the same Altland-Zirnbauer class as the substrate's BCS sector — class BDI, T² = +1, KO-dimension 6 (S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2: AZ-BDI-DIII inheritance confirmed with χ_M3 residual 0, homomorphism residual 2.2×10⁻¹⁵). The kernel ker(ι_*) carries the substrate degrees of freedom that do NOT inherit into the laboratory parent — and it has rank 2 (the chiral pair φ_67 and the Cartan hypercharge φ_88). The direction is parent → child: the substrate IS the parent BDI structure; ³He-B IS a child realization of it under χ, not an analogy to it (`3HeB-inheritance-canonical.md`).

### XII.B. The 5-anatomy of the bridge

Per `cross-pillar-bridge-anatomy.md`, the bridge declares all five elements:

1. **Substrate-IS observable** — the Hochschild cocycle norms of the two ker(ι_*) generators on the finite spectral triple at τ_fold = 0.19: cocycle_norm(φ_67) = 0.793346 M_KK² and cocycle_norm(φ_88) = 0.108307 M_KK², and their ratio.
2. **Laboratory-IN observable** — the Caroli-Matricon vortex-core ladder asymmetry in ³He-B vortex spectroscopy (Lancaster MCT-3 cell: ν_pump scan, ladder-spacing asymmetry between left/right circulation; Helsinki ROTA cell: ladder-spacing parity).
3. **Bridge map** — the inheritance morphism χ composed with the (Δ_B/Δ_A)^p laboratory-conversion. The cocycle-asymmetry ratio is preserved INTACT because the (Δ_B/Δ_A)^p factor cancels exactly between numerator and denominator (inheritance-falsifier-protocol.md, machine-precision identity).
4. **Algebraic envelope** — the substrate-IS cocycle ratio is Sage-exact at machine precision.
5. **Empirical anchor** — the substrate-derived ratio

       cocycle_norm(φ_67) / cocycle_norm(φ_88) = 0.793346 / 0.108307 = 7.3249917525961665

   (4-sig-fig form 7.3250), to be measured in ³He-B as 7.3250 ± 0.1%.

### XII.C. The 4-gate falsifier protocol

Because ker(ι_*) has rank 2, the falsifier protocol (`inheritance-falsifier-protocol.md`) pre-registers both a kernel-signature class (NULL predictions) and a cohomology-asymmetry class (the ratio):

- **Gate 1** — kernel-signature NULL on the decisive rows F1 + F2 + F5 (the substrate predicts no signal in a specific cohomology pattern when the parent inheritance is BDI-protected).
- **Gate 2** — cohomology-asymmetry ratio 7.3250 ± 0.1% on any non-NULL detection (the high-leverage test: the ratio is substrate-derived and survives the lab conversion).
- **Gate 3** — kernel-signature NULL on the supporting rows F3 + F4.
- **Gate 4** — discriminating slope analysis on cocycle-degenerate rows (F4 multi-pressure slope, 0–34 bar: Jacobi-cubic vs φ_88-linear).

S87-W11-C5-LAB-FALSIFIER returned PASS with value 7.324992 (scheme: Sage-exact zeta-regulated Hochschild-pairing cancellation theorem; convention: 3He-B-BDI-vortex-core-Caroli-Matricon). S90 landed the liaison watchlist (50/50 checks PASS; cocycle_norm_phi67 = 0.793346 confirmed).

### XII.D. The substrate-IS direction (the bridge cannot be inverted)

The direction of explanation MUST flow: the substrate (Pillar III/IV) IS the BDI cocycle structure → bridge map (χ ∘ inheritance) → ³He-B laboratory (Pillar V) IN the Caroli-Matricon ladder asymmetry. Inverting this — treating ³He-B as fundamental and the substrate as an analogy to it — is a container-thinking violation. ³He-B is a *projection* of the substrate's algebra under χ; the substrate's cocycle ratio is logically prior, and the laboratory measurement is the F-image of the substrate index pairing. This is what makes the test substrate-*falsifying*: if Lancaster or Helsinki measure the Caroli-Matricon asymmetry ratio and it diverges from 7.3250, the substrate's cohomology prediction is wrong — a genuine laboratory falsifier for a cosmological framework, which is exactly what limitation #1 said could not exist.

---

## Appendix A: Key Equations from Landau Papers

For reference by other agents. Equation numbers match the index at `researchers/Landau/index.md`.

**Landau free energy** (Paper 04, eq. 1):  F(η, T) = F_0(T) + a_0(T − T_c)η² + b η⁴
**Two-fluid model** (Paper 05, eq. 1):  ρ = ρ_s(T) + ρ_n(T)
**Critical velocity** (Paper 05, eq. 2):  v_c = min_p [ε(p)/p]
**Second sound** (Paper 05, eq. 3):  u_2² = ρ_s s² T / (ρ_n c_p)
**GL superconductivity** (Paper 08, eq. 1):  f_s = α|ψ|² + (β/2)|ψ|⁴ + (1/2m*)|(−iℏ∇ − eA/c)ψ|² + B²/(8π)
**GL κ classification** (Paper 08; Paasch-potential collab):  κ = λ/ξ_BCS;  Type I if κ < 1/√2, Type II if κ > 1/√2
**LK relaxation** (Paper 09, eq. 1):  dφ/dt = −(1/τ_0)(dF/dφ)
**Critical slowing** (Paper 09, eq. 2):  τ = τ_0 / (a|T − T_c|)
**Effective mass** (Paper 11, eq. 1):  m*/m = 1 + F_1^s/3
**Quasiparticle lifetime** (Paper 11, eq. 2):  1/τ_qp ~ (ε − ε_F)²
**Pomeranchuk stability** (Paper 11, eq. 3):  F_l^{s,a} > −(2l+1) for all l
**BCS gap** (Paper 15, eq. 1):  Δ_0 = 2ℏω_D exp(−1/(V N(E_F)))
**Richardson exact solution** (Paper 16, eq. 1):  ε_a + G/2 = Σ_{b≠a} 2G/(z_a − z_b) + Σ_i G/(z_a − ε_i)
**GGE density matrix** (Paper 20, eq. 1):  ρ_GGE = Z⁻¹ exp(−Σ_k λ_k I_k)
**Kibble-Zurek defect density** (Paper 21, eq. 1):  n_defect ~ (τ_Q)^{−dν/(dν+z)}
**Landau-Zener probability** (Paper 29, eq. 1):  P_LZ = exp(−2π Δ²/(ℏ|v̇|))

**NEW key equations (post-S44):**
**Leggett dispersion** (Paper 11; S49):  ω²(K) = ω_L1² + c_G² K²,  ω_L1 = 0.138 M_KK
**Goldstone phase propagator** (Paper 08; S47–48):  G⁻¹_{ab}(K) = ρ_s^a K² δ_{ab} + M²_{ab}
**Superfluid-stiffness tensor** (Paper 08; S47):  F(q) = F(0) + (1/2) Σ_{ab} ρ_s^{ab} q_a q_b
**BKT temperature** (BKT; S56/S74):  T_BKT = (π/2) ρ_s_eff
**Volovik partition** (Paper 04 q-theory; S58):  F_total = F_Josephson(→ vacuum) + (F_BCS + F_BA + F_Leggett)(→ matter)
**Volovik tracking vacuum** (Paper 04 q-theory; S66):  ρ_vac ~ M_Pl² H²  (DILUTION-CC; CC_OOM = 115.5)
**(Δ_B/Δ_A)^p cancellation** (inheritance-falsifier-protocol; S87):  lab(F_i)/lab(F_j) = ‖φ_a‖/‖φ_b‖ × (f_i/f_j), the (Δ_B/Δ_A)^p factor cancels exactly
**Generalized Gibbs-Duhem (GGE, OPEN)** (Paper 20; §IV.D):  whether Σ_k λ_k dI_k satisfies a Gibbs-Duhem relation for the integrable relic is the open computation

---

## Appendix B: Session-Gate Cross-Reference

Every framework gate that maps onto a Landau condensed-matter result, with the mapping direction. Refreshed to S93.

| Gate | Session | Verdict | CM Concept | Paper |
|:--|:--|:--|:--|:--|
| BCS-CLASS-43 | S43 | PASS | Universality class = 3D Ising | 04 |
| LIFSHITZ-43 | S43 | INFO | Type I Lifshitz transition | 27 |
| LIFSHITZ-ETA-44 | S44 | FAIL | Weyl's law, not anomalous dim | 04 (d_uc) |
| DM-DE-RATIO-44 | S44 | PASS | Specific heat exponent α (ratio 2.75× over) | 04, 05 |
| CDM-CONSTRUCT-44 | S44 | PASS | Normal component at rest | 05 |
| SAKHAROV-GN-44 | S44 | PASS (cond.) | Effective mass (response); Λ-dependent | 11 |
| SAKHAROV-PHONON-53 | S53 | — | Sakharov induced gravity (phonon route) | 11 |
| SAKHAROV-GN-DIRAC | S75 | — | Sakharov induced gravity (Dirac route) | 11 |
| FRG-PILOT-44 / BDG-SA-61 | S44 / S61 | FAIL | ODLRO invisible to diagonal (1.36e-4) | 11, 15 |
| MULTI-T-JACOBSON-44 | S44 | INFO | Saddle directions in F (3 negative C eigenvalues) | 04, 11 |
| CUTOFF-SA-37 | S37 | Theorem | Monotonicity of vacuum F | 04 (Weyl) |
| **OCC-SPEC-45** | **S45** | **FAIL** | **S_occ monotone; 28th equilibrium closure** | **04, 15, 08** |
| RG-BCS-35 | S35 | PASS | Cooper instability 1D theorem | 15 |
| TRAP-1 (S34) | S34 | Theorem | U(2) singlet selection rule | 04 (rep theory) |
| Block-diagonal (S22b) | S22b | Theorem | Peter-Weyl / selection rules | 04 (G/H) |
| Pomeranchuk (S22c) | S22c | PASS | f_0 = −4.687 < −3 (robust L=5,7) | 11 |
| POMERANCHUK-GGE-58 | S58 | FAIL | GGE has no Fermi surface (informative) | 11 |
| DISSOLUTION-44 | S44 | PASS | Effective theory emergence | 04 (universality) |
| N3-BDG-44 | S44 | FAIL | 3He-B, not 3He-A class | 19 (Volovik) |
| 2ND-SOUND-ATTEN-44 / OBS-68 | S44 / S68 | INFO/PASS | Undamped two-fluid mode; ℓ=720.9 horizon | 05, 09 |
| STRUTINSKY-DIAG-44 | S44 | PASS | Shell correction hierarchy | 11 (N(E_F)) |
| VAN-HOVE-TRACK-44 | S44 | INFO | Band structure topology; T3/T4/T5 near-crossing | 27 |
| **LEGGETT-MOMENT-70** | **S70** | **PASS** | **Type-F DM mass anchor (11.97; Ω_DM h²=0.1200)** | **05, 11, 20** |
| MASS-48 | S48 | — | Leggett Goldstone mass (m_L1=0.070) | 08, 11 |
| LEGGETT-DAMPING-50 | S50 | — | Undamped mode Q=670,000 | 05 |
| **PARTITION-58 / PARTITION-62** | **S58/S62** | **PASS** | **Volovik free-energy partition (95.9% vacuum)** | **04, 05** |
| GGE-TWO-FLUID-67 / FLUID-67 | S67 | — | Generalized Landau-Khalatnikov two-fluid | 05, 09, 20 |
| TENSOR-47 / RESPONSE-47 | S47 | Computed | Superfluid-stiffness tensor (24× anisotropic) | 08 |
| TEST-56 / KUBO-58 / RESOLVED-74 | S56/S58/S74 | PASS | BKT on finite graph (T_BKT=(π/2)ρ_s) | 21, BKT |
| INTEG-39 / INTEG-40 / THERM-61 | S39/S40/S61 | — | Richardson-Gaudin integrability; t_Th | 16, 20 |
| **S87-W11-C5-LAB-FALSIFIER** | **S87** | **PASS** | **³He-B inheritance; cocycle ratio 7.324992** | **15, 19** |
| S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2 | S88 | PASS | AZ-BDI-DIII inheritance (χ_M3 residual 0) | 15 |
| S90-3HE-B-LIAISON-WATCHLIST-LANDING | S90 | PASS | ³He-B watchlist 50/50; Lancaster/Helsinki | 15, 19 |
| **DILUTION-CC-66** | **S66** | **PASS** | **Tracking vacuum (114→0.01 OOM; CC_OOM=115.5)** | **04** |
| FABRIC-53 | S53 | — | Ginzburg number / Kohn→backaction-drag | 04, 11 |
| BEC-61 | S61 | — | BCS-BEC crossover N-scan | 22 |
| Mott CC (S65) | S65 | PASS | Mott inaccessible (E_J/E_C=194) | 08, 22 |
| S82-XI-BCS-VS-L-PHONON-CLASSIFICATION | S82 | PASS | BCS-vs-Landau-phonon classification | 04, 08 |
| S63 VdD-Vol (Resolvent–FL) | S63 | — | Resolvent ↔ quasiparticle propagator | 11 |

---

## Appendix C: What Landau Would Have Said (extended for the S45→S93 arc)

A final section in the spirit of the agent, not the formalism.

Landau classified physical systems by their symmetry, their order parameter, and their universality class. He would have recognized the phonon-exflation framework immediately: a first-order phase transition in an 8-dimensional internal space, with a complex scalar order parameter (the BCS gap), in the 3D Ising universality class, with a post-transition state that is a non-equilibrium GGE. He would have written the Landau free energy, identified the cubic term V'''(0) = −7.2, concluded the transition is first-order, and moved on.

He would NOT have tolerated 20 sessions searching for a minimum in the spectral action. The monotonicity is obvious from Weyl's law: the spectral action sums positive quantities over a spectrum that grows with τ. The sum is monotone. He would have proven it in one line.

**On OCC-SPEC's failure** (the S45 result he would have predicted): "Of course S_occ stays monotone. You weighted the trace with BCS occupation numbers, but the BCS condensate changes 0.002% of the trace — the effacement wall told you that. You cannot bend a monotone sum of 250,000 weighted eigenvalues by perturbing it at the fifth decimal place. The one-body trace does not see the condensate, whether you weight it by occupation numbers or not. If you want the condensate, compute the *interaction* — the GGE response matrix — not a reweighted spectrum. Stop trying to smuggle many-body physics into a one-body functional."

**On the Leggett dark-matter anchor** (he would have been satisfied): "Good. The dark matter is an inter-band phase mode — a Leggett mode. Its mass is a spectral moment of the two-band gap, and it is undamped because the relic is integrable. Mass over the gap is 11.97, abundance within 0.6% of observation, no free parameters. *This* is a Landau result: a collective mode whose properties are fixed by the spectrum and the symmetry, not fitted. The dipolar-mass calibration needs work, but the structure is right."

**On the Volovik partition** (he would have nodded): "The condensation free energy partitions 24:1 between the Josephson channel and the quasiparticles. The Josephson channel is the vacuum; the quasiparticles are the matter. This is the two-fluid model with the numbers filled in. And the vacuum tracks the matter density — Volovik's self-sustained vacuum — so the cosmological constant dilutes itself by 115 orders. The mismatch between the zeroth and second moments was always a category error; the dilution is how the geometry resolves it."

**On the integrability** (he would have insisted): "The relic does not thermalize because the pairing Hamiltonian is integrable — Richardson solved it in 1963. Eight conserved integrals, Poisson level statistics, no level repulsion, infinite quasiparticle lifetime. But be careful: that is the *BCS sector*. The full isometry algebra is not integrable and does thermalize in six natural units. Do not confuse the two. The dark matter lives in the integrable sector, which is why it survives."

**On the ³He-B falsifier** (he would have demanded it): "Finally, a laboratory. You said this framework was the whole universe with no external probe — but ³He-B is in the same symmetry class, BDI, and your algebra projects onto its BdG sector. The cocycle ratio 7.3250 is preserved in the vortex-core spectroscopy because the conversion factor cancels. So go to Lancaster, go to Helsinki, measure the Caroli-Matricon ladder asymmetry. If it is not 7.3250, your cohomology is wrong. A cosmology with a tabletop falsifier — that is worth something."

**On the n_s tilt** (still uninterested in the dynamical question, satisfied by the geometric answer): "I told you the tilt was not a quench problem. The Kibble-Zurek formula gives n_s = −0.68 — absurd — because the modulus is global, not a local field, so there is no spatial quench. The tilt is geometric: n_s = 1 − 2ε_H, fixed by the spectral action's slow-roll evolution, cutoff-independent, equal to 0.9561. The equilibrium phase diagram never entered. Compute the geometry, not the quench."

**On the cosmological constant** (his original dismissal, vindicated): "The vacuum energy is the zeroth moment of the free energy. The gravitational constant is the second moment. They belong to different universality classes. Computing one from the other is a category error — and the framework now agrees: the resolution is not to compute Λ from G_N, but to let the vacuum track the matter density. Different moments, different physics, and the dilution is geometric."

He would have been right — and he would have been pleased that, 49 sessions on, the framework stopped looking for a well that Weyl's law forbids and started computing the many-body and laboratory physics where the answers actually live.
