# Meta-Analysis Request: Landau Condensed Matter Theorist

**Domain**: Condensed Matter Physics -- Phase Transitions, Superfluidity, BCS Theory, Fermi Liquid Theory, Quasiparticle Physics
**Date**: 2026-03-13
**Agent**: landau-condensed-matter-theorist
**Researchers Folder**: `researchers/Landau/`

---

## 1. Current Library Audit

**Papers on file**: 14 (spanning 1927-1958)
**Coverage assessment**: The library covers Landau's canonical contributions comprehensively. The four pillars -- Order Parameter (Papers 04, 08, 09), Excitation Spectrum (Papers 05, 07, 11, 12), Topological Defects (Papers 03, 13, 02), and Renormalization (Papers 10, 14, 06) -- are all well represented. However, the library has ZERO papers from after 1958 and ZERO papers from authors other than Landau's immediate circle. Given the framework's reliance on BCS in finite systems, BCS-BEC crossover, integrable many-body dynamics, Kibble-Zurek physics, and superfluid vacuum models, the gaps are severe.

| # | Current Paper | Key Topics | Adequate for Framework? |
|---|--------------|------------|-----------|
| 01 | 1927 Landau Density Matrix | Density matrix, open systems, von Neumann entropy | Yes -- foundational |
| 02 | 1930 Landau Diamagnetism | Landau levels, quantization, topological indices | Partial -- misses modern topological classification |
| 03 | 1935 Landau-Lifshitz Magnetic Dispersion | Domain walls, solitons, LL equation | Yes -- direct analog for Z_3 walls |
| 04 | 1937 Landau Phase Transitions | Order parameter, symmetry breaking, Landau free energy | Yes -- CRITICAL foundation |
| 05 | 1941 Landau Superfluidity He II | Two-fluid model, phonon-roton, critical velocity | Yes -- CRITICAL prototype |
| 06 | 1946 Landau Plasma Damping | Landau damping, collisionless dynamics, phase mixing | Partial -- misses GGE connection |
| 07 | 1947 Landau Superfluidity Sequel | Revised roton parameters, Bogoliubov spectrum | Yes |
| 08 | 1950 Ginzburg-Landau Superconductivity | GL functional, coherence length, Type I/II, flux quanta | Yes -- CRITICAL |
| 09 | 1954 Landau-Khalatnikov Sound Absorption | TDGL, critical slowing, dynamic universality | Yes -- connects to LK relaxation |
| 10 | 1954 LAK Running Coupling | Landau pole, running couplings, triviality | Yes |
| 11 | 1956 Landau Fermi Liquid Theory | Quasiparticles, Landau parameters, Pomeranchuk stability | Yes -- CRITICAL |
| 12 | 1957 Landau Zero Sound | Zero sound, collisionless oscillations | Partial |
| 13 | 1957 Abrikosov Type II Vortices | Vortex lattice, mixed state, flux quantization | Yes |
| 14 | 1958 Landau Analytic Properties | Landau singularities, Cutkosky rules | Partial -- secondary relevance |

### Identified Gaps

**CRITICAL GAPS** (directly impact framework computations):

1. **BCS Theory itself** -- The library has GL (Paper 08) but NOT the BCS paper (Bardeen-Cooper-Schrieffer 1957). The entire framework mechanism chain is BCS-based. This is an egregious omission.

2. **Richardson-Gaudin exact solution** -- The framework's GGE with 8 conserved integrals (S38) relies on the Richardson exact solution of the pairing Hamiltonian (1963). No paper on integrable pairing models.

3. **BCS-BEC crossover theory** -- The framework sits at E_vac/E_cond = 28.8 (S37), deep in the BEC side. No paper on the crossover (Eagles 1969, Leggett 1980, Nozieres-Schmitt-Rink 1985, Randeria 1990s).

4. **Kibble-Zurek mechanism** -- The framework's paradigm shift (S37-S38) is that transit = sudden quench producing defects. No paper on KZ (Kibble 1976, Zurek 1985, 1996).

5. **Superfluid vacuum theory (Volovik)** -- The closest existing framework to phonon-exflation. No paper on emergent gravity from superfluid vacuum.

6. **Generalized Gibbs Ensemble** -- The GGE is the post-transit state of the framework (S38). No paper on GGE (Rigol et al. 2007, Vidmar-Rigol 2016).

**SIGNIFICANT GAPS** (strengthen analysis and adversarial testing):

7. **Giant Pair Vibrations in nuclear physics** -- The framework's GPV (S37, omega=0.792) is a direct nuclear analog. No nuclear BCS reference.

8. **Pomeranchuk instability in modern materials** -- f_0=-4.687 (S22c) triggers instability. Recent kagome metal discoveries directly relevant.

9. **Van Hove singularities and flat bands** -- M_max=1.674 from van Hove DOS (S35). Modern higher-order VHS literature missing.

10. **Topological classification (Altland-Zirnbauer)** -- BDI class (S17c) from modern topological insulator/superconductor classification. No paper on AZ classes.

11. **Coleman-Weinberg on compact spaces** -- CW mechanism tested and closed (S18). Compact-space version never properly referenced.

12. **Landau-Zener in cosmological context** -- P_LZ=0.999 (S38) for the transit. Recent exact WKB work on cosmological particle production via LZ.

---

## 2. Web-Fetch Requests

Papers that SHOULD be in `researchers/Landau/` but are NOT. Prioritized by relevance to the framework.

### Priority A -- Critical (directly addresses open gates or framework mechanisms)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| 1 | Theory of Superconductivity | Bardeen, Cooper, Schrieffer | 1957 | Phys. Rev. 108, 1175 | **The BCS paper.** The entire mechanism chain (S32-S38) is BCS. We reference BCS constantly but do not have the source. Gap equation, condensation energy, coherence length -- all load-bearing for the framework. |
| 2 | A restricted class of exact eigenstates of the pairing-force Hamiltonian | Richardson | 1963 | Phys. Lett. 3, 277 | **Richardson exact solution.** The 8 conserved integrals of the GGE (S38) are Richardson-Gaudin integrals. The proof that our BCS system is integrable -- and hence that the GGE is permanent -- rests on this. |
| 3 | Colloquium: Exactly solvable Richardson-Gaudin models for many-body quantum systems | Dukelsky, Pittel, Sierra | 2004 | Rev. Mod. Phys. 76, 643 | **Comprehensive RG review.** Covers the algebraic Bethe ansatz, applications to ultrasmall grains, nuclear pairing, and quantum dots. Our 0D limit (L/xi_GL=0.031) puts us squarely in the "ultrasmall grain" regime where the RG solution is essential. |
| 4 | Theory of Dark Matter Superfluidity | Berezhiani, Khoury | 2015 | Phys. Rev. D 92, 103510; arXiv:1507.01019 | **Most direct competitor/complement.** DM superfluidity with phonon-mediated MOND force. Framework predicts CDM-like DM (S42 DM-PROFILE-42), while Khoury predicts superfluid DM. Direct comparison needed. |
| 5 | The Universe in a Helium Droplet (key chapters) | Volovik | 2003 | ISBN 978-0198507826 | **Superfluid vacuum theory.** Emergent Weyl fermions, gauge fields, and gravity from He-3 topology. The philosophical ancestor of phonon-exflation. Volovik's framework derives SM-like particles as quasiparticles of a superfluid vacuum -- exactly what this framework attempts on SU(3). |
| 6 | Relaxation in a completely integrable many-body quantum system: An ab initio study of the dynamics of the highly excited states of 1D lattice hard-core bosons | Rigol, Dunjko, Yurovsky, Olshanii | 2007 | Phys. Rev. Lett. 98, 050405 | **GGE founding paper.** Establishes that integrable systems relax to GGE, not Gibbs. Our S38 result (GGE permanent, 8 conserved quantities) is a direct application. The prethermalization plateau and its permanence are central framework claims. |
| 7 | Cosmological consequences of the Kibble mechanism | Zurek | 1985 | Nature 317, 505 | **KZ mechanism.** Framework paradigm shift (S37): transit = KZ quench. Defect density formula n ~ (tau_Q/tau_0)^{-d*nu/(1+z*nu)}. Our P_LZ=0.999 and xi_KZ=0.269 depend on this. |

### Priority B -- Important (foundational or fills significant gap)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| 8 | The BCS-BEC crossover: From ultra-cold Fermi gases to nuclear systems | Strinati, Pieri, Roepke, Schuck, Urban | 2018 | Phys. Rep. 738, 1; arXiv:1802.05997 | **Comprehensive crossover review.** E_vac/E_cond=28.8 (S37) places us in BEC regime. This review covers the full crossover from weak-coupling BCS to strong-coupling BEC, including finite-size and nuclear systems. |
| 9 | Signatures of the Giant Pairing Vibration in 14C and 15C | Cappuzzello et al. | 2015 | Nature Comms. 6, 6743 | **First experimental GPV evidence.** S37 found GPV analog at omega=0.792, 85.5% of pair-addition strength. This paper provides the nuclear benchmarks for comparison. |
| 10 | The Giant Pairing Vibration in Heavy Nuclei: Present Status and Future Studies | Fortunato, Vitturi, Lubian | 2019 | arXiv:1905.01339 | **GPV review.** Comprehensive survey of theoretical predictions and experimental searches. Predicted to lie at ~20 MeV excitation with L=0 character. |
| 11 | Fragmentation of the Giant Pairing Vibration induced by many-body processes | (various) | 2025 | Phys. Rev. Lett. 134, 062501 | **Latest GPV fragmentation.** Many-body processes fragment the GPV -- directly relevant to our B2 sector's 85.5% single-mode concentration vs. potential fragmentation mechanisms. |
| 12 | Pomeranchuk instability induced by an emergent higher-order van Hove singularity on the distorted kagome surface of Co3Sn2S2 | Beidenkopf et al. | 2024 | arXiv:2410.01994 | **Modern Pomeranchuk-VHS connection.** Framework has f_0=-4.687 (S22c) and M_max=1.674 from VHS (S35). This paper shows the same physics in kagome metals: higher-order VHS triggers Pomeranchuk instability. Direct experimental analog. |
| 13 | High-order Van Hove singularities and their connection to flat bands | (review) | 2024 | Ann. Rev. Cond. Matt. Phys.; arXiv:2405.20226 | **VHS-flat band review.** B2 flat band (v_B2~0) creates VHS. This review covers the classification of higher-order VHS and their physical consequences. |
| 14 | Kibble-Zurek universality in a strongly interacting Fermi superfluid | Ko, Li, Chen, Huang, Aubin, Bhongale, Bhatt, Chin, DeSalvo | 2019 | Nature Physics 15, 1227 | **KZ in BCS-BEC crossover.** Experimental demonstration that KZ universality persists across the BCS-BEC crossover. Constant scaling exponent from U(1) symmetry. Directly tests our S38 quench physics. |
| 15 | The exact WKB and the Landau-Zener transition for asymmetry in cosmological particle production | Enomoto, Matsuda | 2022 | JHEP 02 (2022) 131; arXiv:2104.02312 | **LZ in cosmological particle production.** Exact WKB analysis of LZ transition for particle creation during cosmological phase transitions. Our P_LZ=0.999 and Schwinger-instanton duality (S38) connect directly. |

### Priority C -- Supplementary (strengthens coverage, recent developments)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| 16 | Gate-controlled BCS-BEC crossover in a two-dimensional superconductor | Nakagawa et al. | 2021 | Science 372, 190 | **Experimental BCS-BEC in 2D.** Demonstrates tunable crossover in a solid-state system. Provides experimental benchmarks for crossover physics in compact geometries. |
| 17 | Superfluid analogies of cosmological phenomena | Volovik | 2001 | Phys. Rep. 351, 195 | **Superfluid-cosmology dictionary.** Systematic mapping of CM phenomena to cosmological analogs: horizons, Hawking radiation, dark energy, cosmic strings. Our framework needs this dictionary. |
| 18 | Generalized Gibbs ensembles in integrable lattice models | Vidmar, Rigol | 2016 | J. Stat. Mech. 064007 | **GGE review.** Comprehensive treatment including what determines the GGE, how to construct it, and when it breaks down. Relevant to our claim that GGE is permanent. |
| 19 | Richardson-Gaudin models and broken integrability | Claeys | 2018 | PhD thesis, Ghent | **RG models with perturbations.** What happens when integrability is weakly broken? Our off-Jensen BCS (B2-OFFJ-41, 0.17% change at epsilon=0.1) tests exactly this. |
| 20 | Non-Fermi-Liquid/Marginal-Fermi-Liquid Signatures Induced by Van Hove Singularity | (various) | 2024 | arXiv:2401.10707 | **Non-Fermi liquid from VHS.** Framework has VHS at the fold. This paper analyzes when VHS drives the system away from Fermi liquid behavior -- relevant to the quasiparticle description. |
| 21 | Derivation of emergent spacetime metric, gravitational potential and speed of light in superfluid vacuum theory | Zloshchastiev | 2023 | Universe 9, 234 | **Recent SVT.** Derives 4D curved spacetime from 3D quantum Bose liquid. Shows c is derived, not postulated. Relevant to c_fabric = c (S42 C-FABRIC-42). |
| 22 | Finite-size effects in the two-dimensional BCS-BEC crossover | (various) | 2024 | arXiv:2401.06054 | **Finite-size BCS-BEC.** Our system is 0D (L/xi_GL=0.031). This paper treats finite-size corrections to the crossover, directly applicable. |
| 23 | Higgs response and pair condensation energy in superfluid nuclei | Shimoyama | 2023 | PTEP 2023, 083D01 | **Nuclear Higgs mode.** The amplitude mode of the pairing gap in nuclei. Our QRPA stable result (S40, 8 modes, omega_min=2.665) is the analog. |
| 24 | Moments of inertia in light deformed nuclei: pairing and mean-field impacts | (various) | 2023 | arXiv:2304.10873 | **Cranking inertia in sd-shell.** Our M_ATDHFB=1.695 (S40) is a collective inertia for the SU(3) deformation. This paper computes the same quantity for nuclear deformations in the mass region (A~24) identified as our analog. |
| 25 | The pervasiveness of shape coexistence in nuclear pair condensates | (various) | 2024 | arXiv:2402.11276 | **Shape coexistence in pair condensates.** The BCS condensate on SU(3) exhibits coexisting shapes (Jensen vs off-Jensen). This paper demonstrates that shape coexistence is generic in nuclear BCS, strengthening the analog. |
| 26 | Spectrum of the Dirac operator on compact Riemannian manifolds | (various) | 2024 | arXiv:2402.14247 | **Dirac spectrum on compact manifolds.** The entire framework is built on the spectrum of D_K on Jensen-deformed SU(3). This mathematical reference provides the rigorous spectral theory background. |

---

## 3. New Researcher / Field Recommendations

### Complementary (would strengthen or extend the framework)

| Researcher or Field | Why Complementary | Key Papers (1-3) | Proposed Folder Name |
|--------------------|-------------------|-------------------|---------------------|
| **Volovik (Grigory)** -- Superfluid Vacuum Theory | The most developed existing framework where SM particles emerge as quasiparticles from a superfluid vacuum. He-3 provides all the ingredients: Weyl fermions, gauge fields, gravity, horizons. The phonon-exflation framework on SU(3) is a higher-dimensional, NCG-structured version of Volovik's program. | 1. *The Universe in a Helium Droplet* (2003). 2. *Superfluid analogies of cosmological phenomena*, Phys. Rep. 351 (2001). 3. *Field theory in superfluid 3He: Lessons for particle physics, gravity, and high-Tc*, PNAS 96 (1999). | `researchers/Volovik/` |
| **Richardson-Gaudin / Integrable Pairing** | The exact solvability of the BCS pairing Hamiltonian is the mathematical backbone of the GGE permanence claim (S38). The Richardson-Gaudin framework provides the conserved quantities, the Bethe ansatz solution, and the conditions for integrability breaking. | 1. Richardson, Phys. Lett. 3, 277 (1963). 2. Dukelsky-Pittel-Sierra, Rev. Mod. Phys. 76, 643 (2004). 3. Claeys, *RG models and broken integrability*, PhD thesis (2018). | `researchers/Richardson-Gaudin/` |
| **Khoury (Justin)** -- Dark Matter Superfluidity | The primary competitor framework for DM-from-superfluidity. Khoury's MOND-phonon mechanism contrasts sharply with our CDM-from-GGE prediction (S42). A detailed comparison would sharpen what distinguishes the two approaches. | 1. *Theory of DM superfluidity*, Phys. Rev. D 92 (2015). 2. *DM Superfluidity*, SciPost Phys. Lect. Notes 42 (2022). 3. *Relativistic corrections and structure formation in DM superfluidity*, arXiv:2409.02953 (2024). | `researchers/Khoury/` |
| **Nuclear Giant Resonances** | The framework's compound nucleus analog (HESS-40, S42 HF-KK-42) and GPV (S37) require nuclear many-body benchmarks. Giant resonances -- monopole (breathing mode), dipole, and the GPV itself -- are the nuclear collective modes closest to the framework's QRPA spectrum. | 1. Cappuzzello et al., Nature Comms. 6, 6743 (2015). 2. Fortunato-Vitturi-Lubian, arXiv:1905.01339 (2019). 3. *Fragmentation of the GPV*, Phys. Rev. Lett. 134, 062501 (2025). | `researchers/Nuclear-BCS/` (or extend `researchers/Neutrino/`) |
| **Kibble-Zurek / Quench Dynamics** | The framework's paradigm shift (S37-S38): transit = sudden quench, not adiabatic evolution. KZ defect formation, Landau-Zener transition probabilities, and prethermalization are all load-bearing for the GGE relic picture. | 1. Zurek, Nature 317, 505 (1985). 2. Ko et al., Nature Physics 15, 1227 (2019). 3. Enomoto-Matsuda, JHEP 02, 131 (2022). | `researchers/Kibble-Zurek/` |

### Adversarial (would challenge, constrain, or stress-test the framework)

| Researcher or Field | Why Adversarial | Key Papers (1-3) | Proposed Folder Name |
|--------------------|-----------------|-------------------|---------------------|
| **Finite-size BCS skepticism** | The framework operates at 0D (L/xi_GL=0.031, 16 modes). At this level, the BCS mean-field description is questionable: Anderson's "BCS is destroyed in ultrasmall grains" argument (1959) and subsequent exact diagonalization studies show that pairing gaps are suppressed by level-spacing effects when delta/Delta > 1. Our delta/Delta ratio needs quantitative benchmarking. | 1. Anderson, J. Phys. Chem. Solids 11, 26 (1959) -- *Theory of dirty superconductors*. 2. von Delft, Ralph, *Spectroscopy of discrete energy levels in ultrasmall metallic grains*, Phys. Rep. 345, 61 (2001). 3. Braun, von Delft, *Fixed-N superconductivity: The crossover from the bulk to the few-electron limit*, PRL 81, 4712 (1998). | `researchers/Finite-Size-BCS/` |
| **Non-Fermi liquid critique** | The Pomeranchuk instability (f_0=-4.687) and the VHS at the fold push the system toward non-Fermi liquid behavior. If the quasiparticle description breaks down, the entire Fermi liquid / BCS edifice is undermined. The question is whether the instability produces a non-Fermi liquid with no well-defined quasiparticles, invalidating the BCS mechanism chain. | 1. Varma et al., *Phenomenology of the normal state of Cu-O high-Tc superconductors*, PRL 63, 1996 (1989). 2. Lee, *From high-Tc to a holon-pair boson*, APS Physics 3, 36 (2010). 3. arXiv:2401.10707 -- *Non-Fermi-Liquid from VHS* (2024). | `researchers/Non-Fermi-Liquid/` |
| **Cosmological constant problem critique** | The framework inherits a 80-127 OOM CC overshoot (S42 W-Z-42). Any serious framework for emergent gravity must address the CC problem. The Weinberg no-go theorem and its modern extensions constrain what structural mechanisms can reduce the CC. | 1. Weinberg, *The Cosmological Constant Problem*, Rev. Mod. Phys. 61, 1 (1989). 2. Padilla, *Lectures on the Cosmological Constant Problem*, arXiv:1502.05296. 3. Bernardo et al., *Cosmological Constant Problem: Deflation and Nativeness*, arXiv:2211.11461. | `researchers/CC-Problem/` |
| **BCS in curved / non-Euclidean geometry** | The internal space is SU(3) (curved, 8-dimensional). Pairing on curved manifolds differs from flat-space BCS: the gap equation is modified by curvature, the DOS changes, and topological effects emerge. If curvature corrections are large, the flat-space BCS analogy that all Tier-0 computations rely on would need revision. | 1. Benfenati et al., *Vortex nucleation barrier in superconductors beyond the Bean-Livingston approximation*, Phys. Rev. B 101, 220505 (2020). 2. Herbut, *Interactions on the Dirac spectrum*, arXiv:hep-th/0304037 (on coset spaces). 3. Turner et al., *BCS in strong gravitational fields*, relevant for neutron star crusts. | `researchers/Curved-BCS/` |

---

## 4. Framework Connections (S41/S42)

### Session 41 connections

**B2-OFFJ-41 PASS (0.17% change at epsilon=0.1)**: This result tests the robustness of BCS under perturbation away from the Jensen path. From the Landau perspective, the question is whether the broken-integrability literature (Claeys 2018, Priority C #19) predicts this level of robustness. Richardson-Gaudin integrability is exact ON Jensen. Off Jensen, the integrability-breaking perturbation epsilon couples the 8 conserved quantities. The 0.17% change at epsilon=0.1 is consistent with the integrable perturbation theory result delta(Delta)/Delta ~ epsilon^2 for small epsilon (quadratic onset), but this needs to be checked against the RG broken-integrability framework. If the system is "near-integrable" at physically relevant epsilon, the GGE permanence claim (S38) extends to the full fabric. If not, the GGE thermalizes on a timescale set by the integrability-breaking scale.

**SF-TRANSIT-41 FAIL (S_F monotonic)**: The fermionic spectral action was the last untested linear-in-D functional. Its monotonicity strengthens the spectral action closure wall. From the Landau free energy perspective, this confirms that no fermionic bilinear generates a non-trivial effective potential for the order parameter tau. The structural result S_F^Connes = 0 (from BDI T-symmetry) is a permanent contribution to the NCG literature, independent of the framework's fate.

**N-EFF-41 (step function)**: The degeneracy count jumps 32 to 240 at infinitesimal tau. This is the Landau picture of symmetry breaking applied to the spectral geometry: the full SU(3)_L x SU(3)_R isometry group is broken by ANY Jensen deformation, immediately lifting all accidental degeneracies. The residual degeneracies (d_avg=5.13) are representation-theoretic (Schur's lemma, Kramers pairs) and cannot be lifted by smooth metric deformations. This is a direct application of the group-subgroup classification from Paper 04.

**Signed logarithmic sum (LOG-SIGNED-41)**: The gap-edge weighted variant E with minimum at tau~0.15 introduces a BCS-state-dependent B/F modulation. From the Fermi liquid perspective, this is the first functional that uses the anomalous occupation (u_k v_k) as a spectral weight. The parameter A encoding the gap-edge F/B asymmetry is physically the Bogoliubov amplitude at the chemical potential -- a quantity determined by the pairing interaction, not by free choice. Computing A from Baptista's KK branching rules is the decisive next step for this mechanism.

### Session 42 connections

**Z-FABRIC-42 PASS (Z=74,731, Z/|dS/dtau|=1.27)**: The gradient stiffness establishes that the fabric has O(1) spatial rigidity. From the Landau-Ginzburg perspective, Z is the gradient coefficient kappa in the GL functional F = alpha|psi|^2 + beta|psi|^4 + kappa|nabla psi|^2. The ratio Z/|dS/dtau| = 1.27 means the gradient and potential terms are comparable -- the system is NOT in the London limit (Z >> V) nor the Pippard limit (Z << V). This places the fabric in an intermediate regime where spatial structure and potential energy compete at O(1).

**c_fabric = c (Lorentz invariant)**: This is the most important structural result of S42 from the condensed matter perspective. In ordinary superfluids, the sound speed c_s = sqrt(partial P / partial rho) is always subluminal. Here, the "sound speed" of tau perturbations equals the speed of light because the spectral action descends from the Lorentz-invariant Dirac operator squared. This means the fabric is NOT a superfluid in the traditional sense -- it is a relativistic field theory where the modulus tau plays the role of a massive Klein-Gordon field. The analogy to superfluid vacuum theory (Volovik) is structural but the causal structure is fundamentally different: Volovik's superfluid breaks Lorentz invariance at the condensate scale, while this fabric preserves it exactly.

**DM-PROFILE-42 PASS (NFW, 1/r cusp, sigma/m=5.7e-51)**: I computed this result. The GGE quasiparticles are collisionless CDM with zero effective free-streaming and negligible self-interaction. The Landau quasiparticle framework applies exactly: infinite lifetime (from integrability), well-defined spectral function (8 modes in 3 branches), and Fermi liquid stability (Pomeranchuk criteria satisfied for the GGE). The prediction is standard CDM phenomenology derived from the internal geometry with zero DM-sector free parameters. The cusp-core problem is inherited. Khoury's DM superfluidity (Priority A #4) provides the contrasting prediction: superfluid cores with phonon-mediated MOND forces. The two frameworks make distinct predictions for dwarf galaxy rotation curves.

**TAU-DYN-REOPEN-42 FAIL (35,393x shortfall survives)**: The gradient stiffness Z is irrelevant for homogeneous dynamics -- this is a structural theorem (nabla tau = 0 for uniform evolution). The Thouless-Valatin mass renormalization from fabric fluctuations is delta_M/M = 2.6e-6, suppressed by c_fabric^3 ~ 10^7. In nuclear physics, TV enhancement factors of 1.5-3x occur because nuclear sound speeds are O(1). Here c_fabric = 210, and the enhancement goes as c^{-3}. This is a permanent closure of the mass renormalization route.

**W-Z-42 FAIL (w = -1 + O(10^{-29}))**: The effacement ratio |E_BCS|/S_fold ~ 10^{-6} is the structural bottleneck. In nuclear physics, the ratio of pairing energy to total binding energy is O(10^{-2}) -- pairing MATTERS for nuclear structure. Here, the BCS energy is 6 orders below the spectral action. This inversion (vacuum energy >> interaction energy) is the root cause of both the CC problem and the w = -1 prediction. They are the same structural feature.

### Open questions this literature could address

1. **Anderson criterion for ultrasmall grains**: Is delta/Delta > 1 for our 16-mode system? If so, the BCS description is unreliable and the mechanism chain collapses. The von Delft-Ralph review (Adversarial #1) provides the quantitative criterion.

2. **RG broken integrability at fabric scale**: Does the off-Jensen perturbation (epsilon ~ tau gradient across fabric) break the Richardson-Gaudin integrability enough to thermalize the GGE on cosmological timescales? Claeys's thesis (Priority C #19) provides the formalism.

3. **Volovik comparison**: How does the phonon-exflation framework on SU(3) compare structurally to He-3-A vacuum? Both produce emergent Weyl fermions. The key difference: Volovik's framework breaks Lorentz invariance at the condensate scale; this framework preserves it (c_fabric = c). Which is more physically realistic?

4. **KZ defect density in 0D**: The standard KZ formula assumes spatial extent >> correlation length. Our system has L/xi_GL = 0.031 (zero-dimensional). How does KZ modify in the 0D limit? S38 replaced KZ with Landau-Zener, but the systematic treatment of the crossover from KZ (spatial) to LZ (0D) is missing.

5. **GPV fragmentation**: The S37 GPV concentrates 85.5% in one mode. Recent nuclear results (Priority B #11) show that many-body processes fragment the GPV. Does the B2 sector's near-integrability (<r>=0.401, S40) protect against fragmentation?

6. **Non-Fermi liquid at the fold**: The VHS divergence at B2 combined with Pomeranchuk instability (f_0=-4.687) pushes toward non-Fermi liquid behavior. Recent kagome metal results (Priority B #12) show this explicitly. If the quasiparticle description breaks down at the fold, the BCS gap equation must be replaced by a non-perturbative treatment. The Thouless matrix eigenvalue M_max=1.674 (S35) assumes well-defined quasiparticles.

---

## 5. Self-Assessment

- **Biggest gap in current library**: The BCS paper itself (Bardeen-Cooper-Schrieffer 1957) and Richardson's exact solution (1963). The framework lives and dies on BCS in an integrable finite system, and neither foundational paper is in the library. This is not an oversight -- it is a structural deficiency that must be corrected immediately.

- **Most promising new direction**: The Volovik superfluid vacuum program. The phonon-exflation framework is, in essence, a higher-dimensional NCG-structured version of Volovik's "universe in a helium droplet." Volovik's 30-year body of work provides both the conceptual scaffolding (emergent relativity from superfluidity) and the adversarial challenges (Lorentz violation at the condensate scale, the nullification of the CC by topology). A systematic comparison would clarify what the NCG structure on SU(3) adds to the Volovik program -- and what constraints it inherits.

- **Second most promising direction**: The Richardson-Gaudin integrable pairing literature, combined with broken integrability (Claeys). The GGE permanence claim is the framework's most distinctive prediction (S38): a non-thermal relic that NEVER thermalizes due to exact integrability. If the fabric's spatial coupling breaks integrability, the GGE thermalizes and the relic becomes ordinary thermal matter. The integrability-breaking scale sets the effective thermalization time, which must exceed the age of the universe for the prediction to survive.

- **Confidence in recommendations**: HIGH for Priority A (these are obvious, load-bearing gaps). MEDIUM-HIGH for Priority B (well-motivated by specific framework results, but not strictly blocking). MEDIUM for Priority C (useful context, but the framework can proceed without them). HIGH for all adversarial recommendations -- every one targets a specific quantitative vulnerability in the mechanism chain.
