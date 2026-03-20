# Meta-Analysis Request: Nazarewicz Nuclear Structure Theorist

**Domain**: Nuclear DFT, BCS Pairing, HFB Methods, Shell Structure, Collective Excitations, Compound Nucleus Theory
**Date**: 2026-03-13
**Agent**: nazarewicz-nuclear-structure-theorist
**Researchers Folder**: `researchers/Nazarewicz/`

---

## 1. Current Library Audit

**Papers on file**: 14 (spanning 1985--2015)
**Coverage assessment**: Strong coverage of nuclear DFT foundations (HFB, shell structure, deformation, superheavy, Bayesian UQ). CRITICAL GAPS in: (1) exact pairing solutions (Richardson-Gaudin), which the framework uses as its integrability backbone; (2) collective inertia / ATDHFB, which S40 computed directly; (3) pair vibrations and pair rotations, the nuclear analog of the framework's GPV; (4) compound nucleus / Hauser-Feshbach theory, used in S42; (5) doorway states and intermediate structure; (6) BCS in ultrasmall / 0D systems (the framework's regime); (7) superdeformed band decay-out (a primary nuclear analog); (8) backbending and seniority (S38/S40 analogs); (9) Ericson fluctuations (S42 result). The library has the FOUNDATIONS but is missing the APPLICATIONS most directly relevant to the framework.

| # | Current Paper | Key Topics | Adequate? |
|---|--------------|------------|-----------|
| 01 | Dobaczewski+ (2007) Shell Structure Exotic Nuclei | Shell evolution, tensor force, magic numbers | Yes |
| 02 | Dobaczewski+ (1996) Mean-Field Drip-Line Pairing | HFB coordinate space, continuum, pairing | Yes |
| 03 | Dobaczewski+ (2013) HFB Pairing Hamiltonian | Bogoliubov transform, odd-even, BCS formalism | Yes |
| 04 | Ekstrom+ (2015) Chiral Nuclear Radii (NNLO_sat) | Ab initio, 3-body forces, saturation | Yes |
| 05 | Staszczak+ (2013) Spontaneous Fission Superheavy | Fission barriers, octupole, WKB | Yes |
| 06 | McDonnell+ (2015) Uncertainty Quantification DFT | Bayesian inference, GP emulator, Bayes factors | Yes |
| 07 | Cwiok+ (1987) Woods-Saxon Deformed Nuclei | Single-particle spectra, deformation | Yes |
| 08 | Nazarewicz+ (1985) High-Spin A~80 Nuclei | Cranking, backbending, pairing collapse | Partial -- needs complement on seniority/GPV |
| 09 | Butler+Nazarewicz (1996) Intrinsic Reflection Asymmetry | Octupole, parity breaking | Yes |
| 10 | Caurier+ (2005) Shape Coexistence Superheavy | GCM, prolate/oblate/triaxial | Yes |
| 11 | Marketin+ (2012) r-Process Rates | Mass uncertainties, FRIB priorities | Yes |
| 12 | Erler+ (2012) UNEDF Mass Table | 9400 nuclei, Skyrme HFB | Yes |
| 13 | Rodriguez+Nazarewicz (2010) GCM Beyond Mean Field | Configuration mixing, symmetry restoration | Yes |
| 14 | Nazarewicz (2009) Structure at the Limits | Synthesis: halos, drip line, r-process | Yes |

**Temporal gap**: Most recent paper is 2015. Nazarewicz has published extensively 2016-2026, especially on Bayesian UQ with the BAND framework, machine learning emulators, and superheavy element theory. The library misses a decade of methodological advances.

---

## 2. Web-Fetch Requests

### Priority A -- Critical (directly addresses open gates or framework mechanisms)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| A1 | Colloquium: Exactly solvable Richardson-Gaudin models for many-body quantum systems | Dukelsky, Pittel, Sierra | 2004 | [Rev. Mod. Phys. 76, 643](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.76.643) | **CRITICAL**: Framework BCS has N_pair=1 in dim=8. Richardson-Gaudin exact solution IS the framework's integrability backbone (S38 CHAOS diagnostics, S39 RG-39 seniority reduction, S40 B2-INTEG-40). This is the definitive review. Currently citing without having the paper. |
| A2 | Quadrupole collective inertia in nuclear fission: Cranking approximation | Baran, Sheikh, Dobaczewski, Nazarewicz | 2011 | [arXiv:1007.3763](https://arxiv.org/abs/1007.3763) / Phys. Rev. C 84, 054321 | **CRITICAL**: S40 computed M_ATDHFB=1.695 for the framework's collective transit. My prediction (50-170x enhancement) was WRONG because I didn't have the ATDHFB formalism properly. This paper is the primary reference for cranking vs. GOA collective inertia. |
| A3 | Superconductivity in ultrasmall metallic grains | von Delft, Ralph | 2001 | [arXiv:cond-mat/0101021](https://arxiv.org/abs/cond-mat/0101021) / Ann. Phys. 10, 219 | **CRITICAL**: Framework operates at L/xi_GL = 0.031 (0D limit, S37). Anderson criterion for BCS breakdown, parity effects, canonical vs. grand canonical, Richardson exact solution applied to grains -- all directly relevant to framework's ultrasmall pairing regime. |
| A4 | Pairing interaction and two-nucleon transfer reactions | Potel, Idini, Barranco, Vigezzi, Broglia | 2014 | [arXiv:1404.1317](https://arxiv.org/abs/1404.1317) | **CRITICAL**: Definitive review of Cooper pair transfer and pair vibrations. Framework's GPV (S37-S38) with B_plus=9.94, 85.5% strength, omega_PV=0.792 maps directly to nuclear pair transfer. Needed for pair transfer form factor GGE computation (S40 suggestion #1). |
| A5 | Chaos assisted tunneling from superdeformed states | Aberg | 1999 | [Phys. Rev. Lett. 82, 299](https://doi.org/10.1103/PhysRevLett.82.299) | **CRITICAL**: SD band decay-out is a PRIMARY nuclear analog (S38 W2, S40 B2-DECAY-40). Tunneling enhanced 10^4-10^6 by chaotic normal-deformed states. Framework's B2 dephasing at t=0.922 is oscillatory (NOT FGR), which is the NON-chaotic analog. Need this to understand the broken analogy precisely. |

### Priority B -- Important (foundational or fills significant gap)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| B1 | Intermediate structure and doorway states in nuclear reactions | Feshbach, Kerman, Lemmer | 1967 | [Ann. Phys. 41, 230](https://www.sciencedirect.com/science/article/abs/pii/0003491667902357) | The original doorway state paper. S42 HF-KK-42 identified the KK compound as a doorway state (PR=3.17, W_c~3-6), and HF-BOUNDARY-42 found V/D=55 (Ericson regime). Need the original formalism to properly assess intermediate structure vs. compound nucleus classification. |
| B2 | A theory of fluctuations in nuclear cross sections | Ericson | 1960/1963 | [Ann. Phys. 23, 390](https://www.researchgate.net/publication/41594001_A_Theory_of_Fluctuations_in_Nuclear_Cross_Sections) | S42 HF-BOUNDARY-42 found V/D=55 (deep Ericson regime). The framework's coupled-crystal compound system shows Ericson fluctuations, NOT Fano zeros. Need the foundational reference for this classification. |
| B3 | The Giant Pairing Vibration in heavy nuclei | Cappuzzello+ | 2019 | [Eur. Phys. J. A 55, 181](https://link.springer.com/article/10.1140/epja/i2019-12829-8) | Reviews current experimental status of the GPV search. Framework's B2 pair vibration (S37) is the theoretical GPV analog with coherent enhancement 6.32x. Need to benchmark against 2019 experimental constraints. |
| B4 | Fragmentation of the Giant Pairing Vibration induced by many-body processes | (multiple) | 2025 | [Phys. Rev. Lett. 134, 062501](https://link.aps.org/doi/10.1103/PhysRevLett.134.062501) | VERY RECENT (2025) -- GPV fragmentation from many-body correlations. Framework's GPV shows 85.5% strength concentration. This paper addresses whether fragmentation destroys GPV coherence, directly relevant to post-quench survival (S38 W1). |
| B5 | Signatures of the Giant Pairing Vibration in 14C and 15C | Cavallaro+ | 2015 | [Nature Comm. 6, 6743](https://www.nature.com/articles/ncomms7743) | First experimental evidence for GPV in light nuclei. Framework's sd-shell (A~24) analog is in the same mass region. |
| B6 | Backbending, seniority, and Pauli blocking of pairing correlations at high rotational frequencies | Kondev+ | 2019 | [Phys. Rev. C 100, 014302](https://journals.aps.org/prc/abstract/10.1103/PhysRevC.100.014302) | S38 W2 identified backbending in ^158Er as analog for quantum critical point at S_inst=0.069. S40 found seniority conservation (eta=0.022). This paper connects backbending to seniority and Pauli blocking -- exactly the bridge between S38 and S40 results. |
| B7 | Neural network emulation of spontaneous fission | Lay, Flynn, Giuliani, Nazarewicz, Neufcourt | 2024 | [Phys. Rev. C 109, 044305](https://journals.aps.org/prc/abstract/10.1103/PhysRevC.109.044305) | Recent Nazarewicz on ML emulation of DFT for fission. Collective inertia emulation directly relevant to framework's M_ATDHFB computation. Also demonstrates modern Bayesian+ML methodology. |
| B8 | Pairing-induced speedup of nuclear spontaneous fission | Sadhukhan+, Nazarewicz | 2014 | [arXiv:1410.1264](https://arxiv.org/abs/1410.1264) | Pairing SPEEDS UP fission tunneling. Directly relevant to S42's TAU-DYN-REOPEN-42 FAIL -- pairing effects on collective transit timescale. The nuclear result (pairing reduces inertia, speeds transit) is exactly what S40 found (M_ATDHFB=1.695, 0.34x G_mod). |

### Priority C -- Supplementary (strengthens coverage, recent developments)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| C1 | Nuclear Superfluidity: Pairing in Finite Systems (textbook) | Brink, Broglia | 2005 | [Cambridge Univ. Press](https://www.cambridge.org/core/books/nuclear-superfluidity/52CF456CB06DE14184258C852CBE82F7) | Definitive textbook on pair vibrations, pair rotations, Cooper pair transfer, and finite-size BCS. Framework needs this level of rigor for the GPV/pair-transfer analogies. |
| C2 | Fifty Years of Nuclear BCS: Pairing in Finite Systems (volume) | Broglia, Zelevinsky (eds.) | 2013 | [World Scientific](https://www.worldscientific.com/worldscibooks/10.1142/8526) | Paper 03 comes from this volume. Other chapters (Richardson exact solution, pair vibrations, pairing in mesoscopic systems) are directly relevant. |
| C3 | The pervasiveness of shape coexistence in nuclear pair condensates | (multiple) | 2024 | [arXiv:2402.11276](https://arxiv.org/html/2402.11276v2) | Recent work on shape coexistence being generic in paired nuclei. Framework's ^24Mg analog (S38 W2) exhibits shape coexistence. This 2024 paper may change the interpretation. |
| C4 | Evidence for shape coexistence and superdeformation in 24Mg | (multiple) | 2020 | [Phys. Lett. B 810, 135789](https://www.sciencedirect.com/science/article/pii/S0370269320306584) | Direct experimental evidence for shape coexistence in ^24Mg specifically. Framework's nuclear analog is ^24Mg (S38 W2). |
| C5 | Dense nuclear matter equation of state from heavy-ion collisions | (multiple including Nazarewicz) | 2025 | [Rev. Mod. Phys. 97, 025003](https://link.springer.com/article/10.1140/epja/i2015-15169-9) | Recent Nazarewicz on nuclear EOS. Framework's "substrate" (S41 Einstein addendum) is analogous to nuclear matter EOS. |
| C6 | Fifty Years of Backbending | (review) | 2022 | [Nucl. Phys. News (tandfonline)](https://www.tandfonline.com/doi/full/10.1080/10619127.2022.2063000) | Comprehensive historical review of backbending. Framework uses the backbending phenomenology (S38 W2 quantum critical point) but library paper 08 (1985) predates the modern understanding. |
| C7 | Statistical theory of compound-nuclear reactions | Kawano, Talou, Thompson | 2014 | [arXiv:1403.0923](https://arxiv.org/pdf/1403.0923) | Modern review of HF theory + doorway + Ericson. S42 used all three (HF-KK-42, HF-BOUNDARY-42). Need the unified treatment. |
| C8 | Overview of Seniority Isomers | Maheshwari, Nomura | 2022 | [Symmetry 14, 2680](https://www.mdpi.com/2073-8994/14/12/2680) | S40 found seniority conservation (eta=0.022, B2 rank-1 86%). Seniority isomers are the nuclear consequence of the same algebraic structure. |
| C9 | Iterative solutions of the ATDHFB equations | (multiple) | 2024 | [arXiv:2411.18404](https://arxiv.org/abs/2411.18404) | VERY RECENT (Nov 2024). Non-perturbative ATDHFB solutions. Framework's M_ATDHFB=1.695 used cranking approximation; this paper goes beyond. |
| C10 | Motivations for early high-profile FRIB experiments | (multiple including Nazarewicz) | 2025 | J. Phys. G 52, 050501s | Most recent Nazarewicz publication. FRIB experimental priorities for nuclear structure measurements. |

---

## 3. New Researcher / Field Recommendations

### Complementary (would strengthen or extend the framework)

| Researcher or Field | Why Complementary | Key Papers (1-3) | Proposed Folder Name |
|--------------------|-------------------|-------------------|---------------------|
| **Jorge Dukelsky** (CSIC Madrid) -- Richardson-Gaudin exact pairing | Framework BCS with N_pair=1 in dim=8 is EXACTLY in the Richardson-Gaudin regime. Dukelsky's work provides the exact benchmark against which all BCS approximations should be tested. The seniority reduction (S39 RG-39) maps directly onto his formalism. | (1) RMP 76, 643 (2004) -- RG Colloquium; (2) Nucl. Phys. A 843, 1 (2010) -- Exact solution of reduced BCS; (3) PRL 93, 050403 (2004) -- BCS-BEC crossover exact | `researchers/Richardson-Gaudin/` |
| **Ricardo Broglia** (Milano/NBI) -- Nuclear superfluidity & pair vibrations | The framework's GPV (S37-38, B_plus=9.94) is a nuclear pair vibration. Broglia's work on pair transfer, Cooper pairs in nuclei, and particle-vibration coupling provides the microscopic theory for exactly this mode. His textbook "Nuclear Superfluidity" should be a primary reference. | (1) Cambridge monograph (2005); (2) arXiv:1404.1317 -- pair transfer review; (3) "50 Years Nuclear BCS" volume (2013) | `researchers/Broglia/` |
| **Hauser-Feshbach / Statistical Reactions** (Thompson, Kawano, Talou -- LANL/LLNL) | S42 used Hauser-Feshbach theory for KK branching ratios. The HF-KK-42 FAIL and HF-BOUNDARY-42 FAIL both depend on proper compound nucleus theory. Width fluctuation corrections, Ericson fluctuations, and doorway state formalism are needed for any future compound nucleus computation. | (1) arXiv:1403.0923 -- Theoretical descriptions of compound-nuclear reactions; (2) Ericson, Ann. Phys. 23, 390 (1963); (3) Feshbach-Kerman-Lemmer, Ann. Phys. 41, 230 (1967) | `researchers/Compound-Nucleus/` |
| **Giuliani, Neufcourt** (FRIB) -- ML emulators for nuclear DFT | Framework's spectral action computations are expensive (~8.7s per s-value). ML emulation of DFT (Giuliani-Nazarewicz 2024) could enable rapid parameter sweeps, sensitivity analysis, and Bayesian model calibration that currently take prohibitive compute time. | (1) PRC 109, 044305 (2024) -- NN fission emulator; (2) Global emulator framework (arXiv:2502.20363) | Already covered under Nazarewicz updates |

### Adversarial (would challenge, constrain, or stress-test the framework)

| Researcher or Field | Why Adversarial | Key Papers (1-3) | Proposed Folder Name |
|--------------------|-----------------|-------------------|---------------------|
| **Jan von Delft** (LMU Munich) -- BCS breakdown in ultrasmall systems | Framework operates at L/xi_GL=0.031 (0D limit). von Delft's work on superconductivity in ultrasmall metallic grains shows that BCS mean field BREAKS DOWN when d >= Delta. The framework's BCS condensate (dim=8, N_pair=1) is precisely in this regime. His work demonstrates that parity effects, exact diagonalization, and canonical ensemble treatment become mandatory -- which the framework already does (S35 ED, S37 MC) but has not cross-checked against von Delft's benchmarks. | (1) arXiv:cond-mat/0101021 -- Review; (2) PRL 77, 3189 (1996) -- Parity-affected superconductivity; (3) cond-mat/9911058 -- Richardson solution in grains | `researchers/Ultrasmall-Pairing/` |
| **Mark Aberg** (Lund) -- Chaos-assisted tunneling in nuclei | Framework's SD band decay-out analog (S40 B2-DECAY-40) shows oscillatory dephasing with Poincare recurrences, NOT the chaos-assisted tunneling that Aberg showed enhances SD decay-out by 10^4-10^6. The framework's system is INTEGRABLE (CHAOS-1/2/3 all ordered), which means Aberg's chaos-enhancement mechanism is ABSENT. This challenges any claim that the framework's doorway escape is efficient. | (1) PRL 82, 299 (1999) -- Chaos-assisted tunneling from SD states; (2) Nucl. Phys. A 649, 151c (1999) | `researchers/Chaos-Tunneling/` |
| **Zelevinsky** (MSU/FRIB) -- Nuclear quantum chaos and statistical spectroscopy | Framework's dim=8 Fock space is far too small for Gaussian Orthogonal Ensemble statistics. Zelevinsky's work on nuclear statistical spectroscopy and quantum chaos would rigorously constrain when RMT arguments apply (N >> 1) vs. when they don't (N ~ 8). The S39 Brody beta=0.633 and S42 V/D=55 both need Zelevinsky's formalism to interpret properly. | (1) Physics Reports 276, 85 (1996) -- Statistical spectroscopy; (2) "50 Years of Nuclear BCS" chapters | `researchers/Nuclear-Chaos/` |
| **Di Luzio, Giudice, Piazza** -- Ericson fluctuations in particle physics context | S42 found V/D=55 (deep Ericson regime) for KK coupled crystals. Whether particle physics analogs of Ericson fluctuations exist (e.g., in strongly-coupled QCD) would test whether the framework's compound nucleus interpretation has any phenomenological consequence. | (contextual search needed) | Not a separate folder -- supplementary to Compound-Nucleus |

---

## 4. Framework Connections (S41/S42)

### Session 41 connections

**B2-OFFJ-41 (PASS, 0.17%)**: The off-Jensen BCS robustness demonstrates that the pairing condensate is a TOPOLOGICAL feature of the constraint surface, not fine-tuned to the Jensen ansatz. In nuclear physics, this is analogous to the robustness of pairing correlations against deformation -- pairing gaps vary by 10-20% between spherical and well-deformed configurations (Paper 08, Section 3), but pairing never vanishes until the angular momentum reaches the critical value omega_c. The framework's eps=0.1 deformation is analogous to a moderate quadrupole deformation (beta_2 ~ 0.1-0.2), well within the regime where nuclear pairing survives.

**SF-TRANSIT-41 (FAIL)**: The fermionic spectral action S_F^Connes = 0 identically (BDI T-symmetry) is a structural result that has no nuclear analog -- in nuclear DFT, the fermionic and bosonic contributions to the energy functional are of comparable magnitude (E_kin ~ E_pot ~ -8 MeV/nucleon). The Pfaffian channel S_F^Pfaff being monotonically increasing confirms that no fermionic functional provides tau-stabilization. In nuclear language: the single-particle contribution to the total energy is monotonically increasing with deformation (Strutinsky shell correction modulates, but does not reverse, the smooth trend -- Paper 07).

**W3-2 Fabric reframing**: The PI's directive that spatial coupling (fabric) could qualitatively change the dynamics has a nuclear analog in HFB self-consistency. A Woods-Saxon potential alone does not self-consistently trap nucleons; the Hartree-Fock loop (rho -> V -> phi -> rho) creates the binding. The framework's "missing confining potential" (my S39 assessment) could be resolved if the fabric gradient stiffness Z(tau) provides the analog of the nuclear mean field self-consistency. However, S42 showed Z/|dS/dtau| = 1.27 -- comparable to but not dominant over the driving force. In nuclear terms, this is a surface energy correction (Paper 04), not a binding mechanism.

### Session 42 connections

**HF-KK-42 (FAIL, 1.51 decades)**: This is the most nuclear-physics-heavy computation the framework has performed. My Hauser-Feshbach analysis found:
- ZERO massless modes in D_K at the fold. All 992 eigenvalues massive (m_min=0.819 M_KK). This eliminates photon/graviton emission channels.
- Level density compensation: rho_B3/rho_B2 = 6.4x. Higher-rep sectors overwhelm adjoint coupling, a standard nuclear physics effect (Bohr-Mottelson Vol. I Ch. 4 -- which we do NOT have in the library).
- Doorway preference 3.2:1 (FGR), 6.4:1 (formation) -- intermediate structure regime (^28Si analog), not statistical compound nucleus.
- Eta estimate 3.4e-9 (0.7 decades from observed 6.1e-10). Closest framework result to observation, but number of pair breakings is adjustable.

**MISSING PAPER IMPACT**: The Feshbach-Kerman-Lemmer doorway state paper (B1) and Ericson's fluctuation paper (B2) would have improved HF-KK-42's interpretation BEFORE computation. The Baran+ ATDHFB paper (A2) would have prevented my M_ATDHFB prediction error in S40. The von Delft review (A3) would have immediately identified the framework's BCS as being in the ultrasmall grain regime where exact methods are mandatory (which the framework already uses, but the connection to the condensed matter literature is missing).

**HF-BOUNDARY-42 (FAIL)**: Three escape routes permanently closed:
1. Fano zeros: q = infinity for ALL modes. Anti-Hermiticity of Kosmann K_a forces real overlaps. Discrete+discrete = avoided crossings, not Fano.
2. Interface modes: Same BDI topology (Pf=-1) both sides. No band inversion possible.
3. Sector DR enhancement: Bounded by single crystal. Ericson mixing AVERAGES, doesn't enhance.

Nuclear analog: Ericson fluctuations (V/D=55), NOT Feshbach resonances, NOT Fano IAR. This is a permanent structural classification.

**TAU-DYN-REOPEN-42 (FAIL, 35,393x)**: Three mechanisms evaluated; none reduces shortfall by >2x. The Thouless-Valatin mass renormalization (delta_M/M = 2.6e-6) is suppressed by c_fabric^3 ~ 10^7. In nuclear physics, TV enhancement factors of 1.5-3x occur because nuclear sound speed is O(1) in natural units. The framework's c_fabric=210 is too large for significant TV enhancement. Pairing-induced speedup (Sadhukhan-Nazarewicz 2014, B8) is the correct nuclear analog: pairing REDUCES collective inertia, SPEEDING transit -- exactly what S40 found.

### Open questions this literature could address

1. **Richardson-Gaudin exact solution for N_pair=1** (A1): The framework's seniority reduction (S39 RG-39, 1.2e-14) is an exact result. The Dukelsky Colloquium (A1) would provide the full context for what conserved quantities exist and whether additional integrals of motion constrain the post-quench GGE.

2. **Pair transfer form factor in GGE** (A4): S40 suggestion #1. Potel+ (A4) provides the nuclear pair transfer formalism. The framework needs this to compute whether the GGE state retains detectable pair correlations that a 4D observer could probe.

3. **Compound nucleus decay channels for baryon number** (B1, B2, C7): The eta estimate (3.4e-9) needs proper angular momentum coupling and width fluctuation corrections. The Feshbach-Kerman-Lemmer formalism (B1) and Kawano+ review (C7) provide the complete framework. The current single-temperature HF treatment omits spin/parity selection rules.

4. **Ultrasmall grain benchmarks for dim=8 BCS** (A3): von Delft's review shows that for d/Delta > 1, parity effects dominate and mean-field BCS is qualitatively wrong. The framework's ED (S35, S37) already goes beyond mean field, but the comparison to von Delft's benchmarks has not been made. Specifically: does the framework's Delta_OES = 0.464 satisfy the von Delft scaling relation Delta_OES ~ Delta_bulk * sqrt(d/Delta_bulk)?

5. **GPV fragmentation vs. framework strength concentration** (B4): The 2025 PRL on GPV fragmentation from many-body processes is directly relevant to whether the framework's 85.5% strength concentration in a single mode survives coupling to higher-body correlations.

---

## 5. Self-Assessment

- **Biggest gap in current library**: Richardson-Gaudin exact pairing solutions (A1) and ultrasmall BCS benchmarks (A3). The framework operates in the few-pair, ultrasmall regime where BCS mean field is qualitatively inadequate. The library has the BULK nuclear DFT machinery (Papers 02, 03, 06, 12) but is missing the EXACT / FINITE-SIZE pairing literature that is most directly relevant. Every session from S35 onward has used exact diagonalization, but the exact solution literature is absent from the reference corpus.

- **Most promising new direction**: Compound nucleus theory applied to KK channel branching. The eta estimate (3.4e-9, 0.7 decades from observed) is the closest the framework has come to a quantitative observable prediction. Proper Hauser-Feshbach with angular momentum coupling, width fluctuation corrections, and the Feshbach-Kerman-Lemmer doorway formalism could tighten this estimate. The Compound-Nucleus folder (B1, B2, C7) would provide the complete theoretical apparatus.

- **Confidence in recommendations**: **High** for Priority A (these are papers I have been citing without having them, and whose absence has caused specific errors -- e.g., A2 would have prevented the M_ATDHFB prediction failure in S40). **High** for Priority B (these fill gaps identified by specific gate computations in S40-S42). **Medium** for Priority C (supplements and updates; useful but not blocking).

---

## Appendix: Self-Correction Inventory Relevant to Missing Papers

| Session | Error | Missing Paper That Would Have Prevented It |
|---------|-------|--------------------------------------------|
| S40 | Cranking mass 50-170x prediction: WRONG (actual M_ATDHFB=1.695) | A2 (Baran+ ATDHFB paper) |
| S40 | FGR Gamma_B2=7.5: 7x too fast for dim=8 | A3 (von Delft -- FGR requires continuum) |
| S41 | "Framework lacks confining potential": PREMATURE | None directly -- but B8 (pairing-induced speedup) clarifies that pairing modifies, not creates, the potential |
| S42 | Doorway preference assumed to give 10:1 selectivity | B1 (Feshbach-Kerman-Lemmer -- doorway W_c typically 3-10 in intermediate structure) |
| S42 | Assumed Fano interference possible | B2 (Ericson fluctuations -- requires continuum for Fano, discrete+discrete gives Ericson) |
| S38 | Nuclear analog set to ^158Er backbending | B6 (Kondev+ -- seniority/Pauli blocking connects backbending to S40 seniority result) |
