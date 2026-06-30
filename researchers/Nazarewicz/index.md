# Nazarewicz Paper Index

**Researcher**: Witold Nazarewicz (and collaborators across nuclear DFT, pairing, fission, and astrophysics)
**Papers**: 26 (1985-2024)
**Primary domain**: Nuclear density functional theory, BCS/HFB pairing, shell structure, collective inertia, fission dynamics, superheavy elements, Bayesian UQ, Richardson-Gaudin integrability, ultrasmall superconductivity, pair transfer, seniority, compound nucleus theory, nuclear astrophysics
**Project relevance**: Provides the nuclear many-body physics backbone for the framework's BCS pairing on the SU(3) fiber. The library spans the exact tools used in every framework computation from S31 onward: HFB self-consistency (Papers 02, 03), Richardson-Gaudin integrability (Paper 15), ultrasmall BCS benchmarks (Paper 17), collective inertia for transit dynamics (Papers 16, 20, 24), Strutinsky shell corrections (Papers 07, 08), Bayesian uncertainty quantification (Paper 06), and the nuclear analogs (backbending, GPV, seniority, doorway states) that calibrate every confirmed analogy.

**KNOWN ISSUES**:
- Paper 10: Authors listed as Caurier/Sieja/Nazarewicz in filename; actual authors of the Nature 433, 705 paper are Cwiok/Heenen/Nazarewicz.
- Paper 13: arXiv 0912.2650 is Yao/Meng/Ring/Vretenar (PRC 81, 044311), NOT Rodriguez/Nazarewicz. Content is valid GCM work but by different authors.

---

## Dependency Graph

```
BCS PAIRING & SUPERFLUIDITY (core formalism)
  03 (HFB pairing Hamiltonian) --> 02 (HFB continuum, drip-line)
  03 --> 15 (Richardson-Gaudin exact solution)
  15 --> 17 (ultrasmall BCS, von Delft)
  17 --> 15 [Richardson exact solution benchmarks ultrasmall grains]
  03 --> 08 (high-spin pairing collapse)
  08 --> 26 (backbending chronicle)
  15 --> 18 (pair transfer, GPV nuclear analog)
  18 --> 19 (GPV heavy nuclei review)

SHELL STRUCTURE & DEFORMATION (single-particle spectra)
  07 (Woods-Saxon deformed) --> 01 (shell evolution exotic)
  07 --> 08 (high-spin, Nilsson diagrams)
  07 --> 09 (octupole deformation)
  01 --> 10 (shape coexistence superheavy)
  07 --> 10

COLLECTIVE INERTIA & FISSION (large-amplitude motion)
  16 (ATDHFB cranking) --> 20 (pairing-induced speedup)
  16 --> 05 (spontaneous fission superheavy)
  16 --> 24 (iterative ATDHFB, 2024)
  20 --> 05
  05 --> 21 (NN fission emulator)
  24 --> 21

COMPUTATIONAL METHODS & UQ (model calibration)
  12 (UNEDF mass table) --> 06 (Bayesian UQ)
  04 (NNLO_sat chiral) --> 12
  06 --> 21 (GP emulation applied to fission)
  12 --> 11 (r-process rates, mass sensitivity)
  13 (GCM beyond mean field) --> 10 [both do configuration mixing]

GPV & PAIR TRANSFER (pairing probes)
  18 (pair transfer review) --> 19 (GPV heavy nuclei)
  03 --> 18 [HFB provides spectroscopic amplitudes]
  15 --> 18 [exact solution benchmarks pair correlations]

COMPOUND NUCLEUS & SENIORITY (reaction theory + algebraic structure)
  22 (compound nucleus theory) -- standalone
  23 (seniority isomers) --> 15 [quasi-spin algebra underlies both]
  26 (backbending chronicle) --> 08 [historical complement]
  23 --> 08 [seniority blocking connects to pairing collapse]

SYNTHESIS & ASTROPHYSICS
  14 (structure at the limits) --> 01, 02, 10, 11 [synthesizes all themes]
  11 (r-process rates) --> 12, 14
  25 (dense matter EOS) --> 04, 12

CROSS-THEME LINKS
  03,15,17 --[pairing formalism]--> 08,20,26 [pairing dynamics at high spin/fission]
  07,01    --[shell structure]--> 05,10 [deformation in superheavy]
  16,20,24 --[collective inertia]--> 05,21 [fission applications]
  06,12    --[UQ methodology]--> 21 [emulation]
  18,19    --[pair transfer]--> 15,17 [exact/ultrasmall benchmarks]
  22       --[reaction theory]--> 14 [synthesis context]
  23       --[seniority algebra]--> 15 [quasi-spin = Richardson-Gaudin]
```

## Topic Map

### BCS Pairing & Superfluidity
Papers: 02, 03, 08, 15, 17, 18
The theoretical core: HFB formalism in coordinate space with continuum (02), Bogoliubov transformation and odd-even treatment (03), Richardson-Gaudin exact integrability (15), ultrasmall grain BCS with parity effects and Anderson criterion (17), pairing collapse at high spin (08), and pair transfer as the specific probe of Cooper pair correlations (18). This cluster provides every equation used in the framework's BCS sector.

### Shell Structure & Deformation
Papers: 01, 07, 09, 10
Single-particle spectra in deformed potentials: Woods-Saxon with spin-orbit (07), tensor-driven shell evolution in exotic nuclei (01), octupole (parity-breaking) deformation (09), and shape coexistence with triaxiality in superheavy elements (10). These establish the nuclear analog of the framework's D_K(tau) eigenvalue spectrum and its tau-dependent shell gaps.

### Collective Inertia & Fission
Papers: 05, 16, 20, 21, 24
Large-amplitude collective dynamics: ATDHFB collective mass tensor formalism (16), pairing-induced speedup of fission tunneling (20), symmetry-unrestricted fission of superheavy elements (05), neural network emulation of DFT fission observables (21), and iterative non-perturbative ATDHFB (24). This cluster provides the methodology for the framework's tau-transit collective inertia computation.

### Computational Methods & UQ
Papers: 04, 06, 12, 13
Model calibration and prediction: chiral NN+NNN optimization with emergent saturation (04), Bayesian inference with GP emulator for nuclear DFT (06), large-scale HFB mass table for 9,400 nuclei (12), and GCM configuration mixing beyond mean field (13). Paper 06 is the methodological template for the framework's probability trajectory and gate system.

### GPV & Pair Transfer
Papers: 18, 19
The giant pairing vibration: pair transfer as the specific probe of Cooper pair correlations (18), and the experimental status and theoretical challenges of the GPV in heavy nuclei (19). The framework's GPV with 85.5% strength concentration (S37) maps directly onto this nuclear mode.

### Compound Nucleus & Seniority
Papers: 22, 23, 26
Reaction theory and algebraic structure: Hauser-Feshbach formalism with doorway states and Ericson fluctuations (22), quasi-spin algebra and seniority isomers across the nuclear chart (23), and the historical discovery of backbending (26). Paper 22 underlies S42's HF-KK analysis; Paper 23 provides the seniority algebra that maps onto the framework's Richardson-Gaudin integrals.

### Synthesis & Astrophysics
Papers: 11, 14, 25
Broad overviews: mass uncertainty impact on r-process nucleosynthesis (11), nuclear structure at the limits of binding (14), and the dense nuclear matter equation of state from heavy-ion collisions (25). These provide astrophysical context and cross-validation for the framework's nuclear physics inputs.

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| HFB self-consistency, Bogoliubov transform, pairing tensor | Papers 03, 02 | CRITICAL |
| Richardson-Gaudin integrability, exact pairing solution | Paper 15 | CRITICAL |
| Ultrasmall BCS, Anderson criterion, d/Delta regime | Paper 17 | CRITICAL |
| Bayesian UQ, GP emulator, posterior propagation | Paper 06 | CRITICAL |
| ATDHFB collective inertia, cranking mass | Papers 16, 24 | CRITICAL |
| Pairing-induced fission speedup, M ~ Delta^{-2} | Paper 20 | HIGH |
| Pair transfer, GPV, pairing vibrations | Papers 18, 19 | HIGH |
| Shell structure evolution, tensor force, magic numbers | Papers 01, 07 | HIGH |
| Compound nucleus, Hauser-Feshbach, doorway states | Paper 22 | HIGH |
| GCM configuration mixing, symmetry restoration | Paper 13 | HIGH |
| Backbending, pairing collapse at high spin | Papers 08, 26 | HIGH |
| Superheavy fission, WKB tunneling, shape coexistence | Papers 05, 10 | MEDIUM |
| Seniority algebra, quasi-spin, isomers | Paper 23 | MEDIUM |
| r-process, mass sensitivity, astrophysics | Papers 11, 14, 25 | MEDIUM |
| Chiral EFT, nuclear saturation, ab initio | Paper 04 | MEDIUM |
| NN emulation of DFT, machine learning | Paper 21 | MEDIUM |

---

## Paper Entries

### Paper 01: Shell Structure of Exotic Nuclei
- **File**: `01_2007_Dobaczewski_Shell_Structure_Exotic_Nuclei.md`
- **arXiv**: nucl-th/0701047
- **Year**: 2007
- **Relevance**: HIGH
- **Tags**: shell evolution, tensor force, spin-orbit, Gamow shell model, continuum coupling, exotic nuclei

**Summary**: Reviews how nuclear shell structure changes with neutron excess via three mechanisms: tensor interactions modifying spin-orbit splittings through spin saturation/unsaturation, many-body correlations near drip lines, and continuum coupling in open quantum systems. Demonstrates the Gamow Shell Model using the Berggren completeness relation.

**Key Results**:
- Shell structure is a local concept that changes dramatically with neutron excess
- Tensor-induced SO splitting depends strongly on shell filling (spin saturation)
- Standard SO splitting is nearly constant; tensor contribution varies steeply
- Continuum coupling modifies effective SO interactions in weakly bound systems
- New magic numbers at N=14, 16, 32 appear far from stability

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Tensor EDF | $H_T = \frac{5}{8}[t_e \mathbf{J}_n \cdot \mathbf{J}_p + t_o(\mathbf{J}_0^2 - \mathbf{J}_n \cdot \mathbf{J}_p)]$ | Eq. (7) |
| SO form factor (neutron) | $W^{SO}_n = \frac{5t_e+5t_o}{8}\mathbf{J}_p + \frac{5t_o}{4}\mathbf{J}_n + \ldots$ | Eq. (9) |
| Berggren completeness | $\int\sum_B |u_B\rangle \langle \tilde{u}_B| = 1$ | Eq. (13) |
| Drip-line separation energy | $S_n \approx -\lambda_n - \Delta_n$ | Eq. (1) |

**Dependencies**: Builds on 07 (Woods-Saxon shell model); feeds into 10 (shell effects in superheavy)

---

### Paper 02: Mean-Field Description of Drip-Line Nuclei: Pairing and Continuum Effects
- **File**: `02_1996_Dobaczewski_Mean_Field_Drip_Line_Pairing.md`
- **arXiv**: N/A (1996 PRC 53, 2809)
- **Year**: 1996
- **Relevance**: CRITICAL
- **Tags**: HFB, coordinate space, continuum, pairing, drip line, halo nuclei, density-dependent pairing

**Summary**: Foundational paper reformulating HFB in coordinate space to properly treat the particle continuum. Demonstrates that continuum effects are mandatory for drip-line nuclei (neglecting them overestimates binding by 1-3 MeV). Shows that pairing fields extend far beyond the nuclear surface in halo systems, and that density-dependent interactions better reproduce experimental halo sizes.

**Key Results**:
- Continuum neglect overestimates binding by 1-3 MeV at drip line
- Pairing survives at drip line: Delta ~ 0.7 MeV even in extreme cases (^32Ne)
- Extended pairing fields reach 8-10 fm in halo nuclei (vs. 3-4 fm stable)
- Two-neutron separation energies reproduced to 0.3 MeV accuracy
- Pairing-antihalo effect limits spatial extension of drip-line nuclei

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| HFB equation | $(h - \lambda, \Delta; -\Delta^*, -h^*+\lambda)(u; v) = E(u; v)$ | Main formalism |
| Pairing field | $\Delta(\mathbf{r}) = -G \sum_k u_k(\mathbf{r}) v_k(\mathbf{r})$ | Pairing section |
| Pair coherence length | $\xi_{\text{pair}} \sim \hbar / \sqrt{2m_n |E_F|}$ | Extended pairing |
| Density-dependent force | $V_{\text{pair}} = -G(1 - \eta\rho(\mathbf{r}))\delta(\mathbf{r}-\mathbf{r}')$ | Pairing functional |

**Dependencies**: Downstream of 03 (general HFB theory); feeds into 01, 14

---

### Paper 03: HFB Solution of the Pairing Hamiltonian in Finite Nuclei
- **File**: `03_2013_Dobaczewski_HFB_Pairing_Hamiltonian.md`
- **arXiv**: 1206.2600
- **Year**: 2013
- **Relevance**: CRITICAL
- **Tags**: HFB, Bogoliubov transformation, pairing tensor, Bloch-Messiah-Zumino, odd-even, blocking, regularization, equal filling approximation

**Summary**: Comprehensive overview of HFB theory for nucleonic superfluidity. Defines pairing correlations as excess probability. Derives the full HFB equations, discusses the Bogoliubov sea and truncation pitfalls, the Bloch-Messiah-Zumino theorem, pairing functionals (volume/surface/mixed), UV regularization, and blocking for odd-mass nuclei with the alispin formalism.

**Key Results**:
- Bloch-Messiah-Zumino theorem: canonical pairs exist in any Thouless state
- Truncation of Bogoliubov sea can violate Pauli principle
- Natural basis method resolves Pauli violation
- Zero-range pairing requires renormalization
- Equal filling approximation equivalent to exact blocking when time-odd fields vanish

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Pairing correlation | $P_{\mu\nu} = v^2_{\mu\nu} - v^2_\mu v^2_\nu$ | Eq. (1) |
| Thouless state | $|\Phi\rangle = \mathcal{N}\exp(\frac{1}{2}\sum Z^*_{\nu\mu}a^\dagger_\nu a^\dagger_\mu)|0\rangle$ | Eq. (6) |
| HFB matrix equation | $\mathcal{H}\mathcal{U} = \mathcal{U}\mathcal{E}$ | Eq. (7) |
| Generalized density | $\mathcal{R}^2 = \mathcal{R}$ (idempotent) | Eq. (9) |
| UV divergence | $\tilde\rho \sim -\tilde{h}M^*/(4\pi\hbar^2|x|)$ as $x \to 0$ | Eq. (17) |
| Blocked density | $\rho^{(\alpha)}_{\mu\nu} = (V^*V^T)_{\mu\nu} + U_{\mu\alpha}U^*_{\nu\alpha} - V^*_{\mu\alpha}V_{\nu\alpha}$ | Eq. (21) |

**Dependencies**: Foundational; feeds into 02, 12, 16, 18, 20

---

### Paper 04: Accurate Nuclear Radii and Binding Energies from a Chiral Interaction (NNLO_sat)
- **File**: `04_2015_Ekstrom_Chiral_Nuclear_Radii.md`
- **arXiv**: 1502.04682
- **Year**: 2015
- **Relevance**: HIGH
- **Tags**: chiral EFT, NNLO_sat, three-body forces, nuclear saturation, ab initio, coupled cluster

**Summary**: First microscopically-founded interaction simultaneously describing masses, radii, and spectra from few-body to medium-mass nuclei. Simultaneous NN+NNN optimization achieves nuclear saturation as an emergent phenomenon. Key LECs: c_1=-1.122, c_3=-3.925, c_4=3.766 GeV^{-1}. Incompressibility K=253 MeV.

**Key Results**:
- Simultaneous NN+NNN optimization essential; sequential magnifies uncertainties
- Nuclear saturation is emergent (not explicit in Lagrangian)
- NNLO_sat reproduces masses, radii, spectra from A=3 to A=40
- 3^- collective states in ^16O and ^40Ca well described

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Charge radius | $\langle r^2_{ch}\rangle = \langle r^2_{pp}\rangle + \langle R^2_p\rangle + (N/Z)\langle R^2_n\rangle + 3\hbar^2/(4m_p^2c^2)$ | Text |
| Saturation point | $E/A \approx -16$ MeV at $k_F \approx 1.33$ fm$^{-1}$ | Text |

**Dependencies**: Provides microscopic Hamiltonian context for 12; connects to 25

---

### Paper 05: Spontaneous Fission Modes and Lifetimes of Superheavy Elements
- **File**: `05_2013_Staszczak_Spontaneous_Fission_Superheavy.md`
- **arXiv**: 1208.1215
- **Year**: 2013
- **Relevance**: MEDIUM
- **Tags**: spontaneous fission, superheavy, WKB tunneling, octupole, triaxiality, action integral, SkM*

**Summary**: Systematic SF study of even-even SH nuclei (108 <= Z <= 126) using symmetry-unrestricted HFB with cranking collective mass. Two competing SF modes: reflection-symmetric (sEF) and asymmetric (aEF). Triaxiality reduces barriers by ~3 MeV; combined symmetry breaking reduces half-lives by up to 7 OOM. Longest-lived: ^294Ds (~1.5 days).

**Key Results**:
- Imposing symmetries overestimates SF half-lives by up to 7 OOM
- Two competing SF modes: sEF and aEF
- Center of enhanced stability at ^294Ds
- Barrier widths (not heights) determine dominant SF mode in many cases

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Potential energy | $V(Q_{20}) = E_{\text{tot}}(Q_{20}) - \text{ZPE}(Q_{20})$ | Text |
| WKB penetrability | $P = 1/(1 + e^{2S})$ | Text |

**Dependencies**: Uses 16 (ATDHFB mass tensor); builds on 07, 10; feeds into 21

---

### Paper 06: Uncertainty Quantification for Nuclear DFT
- **File**: `06_2015_McDonnell_Uncertainty_Quantification_DFT.md`
- **arXiv**: 1501.03572
- **Year**: 2015
- **Relevance**: CRITICAL
- **Tags**: Bayesian inference, Gaussian process emulator, MCMC, UNEDF1, model uncertainty, information content

**Summary**: Rigorous Bayesian analysis of nuclear DFT parameter uncertainties using GP emulator for the UNEDF1 functional (12 parameters, 115 data). 17 new CPT mass measurements produce only minor impact (largest shift 0.6 sigma). Propagates uncertainties to masses (+-2 MeV 90% CI), drip-line (15-20 nucleons), fission barriers. Model form error dominates parameter uncertainty.

**Key Results**:
- Bayesian posterior consistent with covariance analysis
- New measurements insufficiently constraining (largest shift 0.6 sigma)
- Mass uncertainties ~+-2 MeV (90% CI)
- Model error (EDF form) dominates statistical parameter uncertainty
- Fission barrier uncertainties change SF half-lives by many OOM

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Composite chi-squared | $\chi^2(x) = \frac{1}{n_d-n_x}\sum_t\sum_j((y_{tj}(x)-d_{tj})/\sigma_t)^2$ | Eq. (1) |
| GP training | 200-point Latin hypercube in 12D parameter space | Text |

**Dependencies**: Uses 12 (UNEDF1); methodology applied in 21

---

### Paper 07: Single-Particle Energies in Axially Deformed Woods-Saxon Potential
- **File**: `07_1987_Cwiok_Woods_Saxon_Deformed_Nuclei.md`
- **arXiv**: N/A (1987 Comput. Phys. Commun. 46, 379)
- **Year**: 1987
- **Relevance**: HIGH
- **Tags**: Woods-Saxon, deformation, Nilsson diagram, spin-orbit, single-particle energies, quadrupole moments, g-factors

**Summary**: Comprehensive computational study of the deformed Woods-Saxon potential. Tabulates single-particle energies, wave functions, quadrupole moments, and g-factors from spherical to extreme deformations. Provides the foundational Nilsson diagrams used in all subsequent shell-correction calculations.

**Key Results**:
- Magic numbers (2, 8, 20, 28, 50, 82, 126) reproduced from WS + spin-orbit
- Level ordering changes dramatically with deformation (intruder orbitals)
- Stable calculations up to extreme elongation (beta_2 > 1.0)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Woods-Saxon potential | $U_{\text{WS}}(r) = -V_0/(1 + \exp[(r-R_0)/a])$ | Main |
| Deformed radius | $R(\theta) = R_0[1 + \beta_2 P_2(\cos\theta) + \beta_4 P_4(\cos\theta)]$ | Main |
| Spin-orbit coupling | $V_{\text{SO}} = \lambda (1/r)(dU/dr) \mathbf{L}\cdot\mathbf{S}$ | Main |

**Dependencies**: Foundational; feeds into 01, 05, 08, 09, 10

---

### Paper 08: Microscopic Study of High-Spin Behaviour in A ~= 80 Nuclei
- **File**: `08_1985_Nazarewicz_High_Spin_A80_Nuclei.md`
- **arXiv**: N/A (1985 Nucl. Phys. A 435, 397)
- **Year**: 1985
- **Relevance**: HIGH
- **Tags**: high spin, cranking, backbending, pairing collapse, shape transitions, band termination, alignment

**Summary**: Analyzes collective and non-collective high-spin configurations in A~80 nuclei using shell-correction + cranking with deformed Woods-Saxon. Demonstrates backbending from high-j alignment, pairing collapse at critical frequency, shape transitions, and band termination. Key formula: Delta(omega) ~ Delta_0 * sqrt(1 - (omega/omega_c)^2).

**Key Results**:
- Backbending from h_{11/2} and g_{9/2} alignment
- Pairing collapses at predicted critical frequency
- Multiple coexisting band structures correctly identified
- Shape transitions (prolate -> oblate) near I=20

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Cranking Hamiltonian | $H_{\text{rot}} = H_0 - \omega J_x$ | Cranking section |
| Pairing gap evolution | $\Delta(\omega) = \Delta_0\sqrt{1 - (\omega/\omega_c)^2}$ | Pairing section |
| Shell-correction energy | $E_{\text{shell}} = \sum_i \epsilon_i - \int_0^{\epsilon_F} g(\epsilon)\epsilon\,d\epsilon$ | Shell correction |

**Dependencies**: Uses 07 (WS potential); connects to 26 (backbending), 23 (seniority blocking)

---

### Paper 09: Intrinsic Reflection Asymmetry in Atomic Nuclei
- **File**: `09_1996_Butler_Intrinsic_Reflection_Asymmetry.md`
- **arXiv**: N/A (1996 Rev. Mod. Phys. 68, 349)
- **Year**: 1996
- **Relevance**: MEDIUM
- **Tags**: octupole deformation, parity violation, reflection asymmetry, E1 transitions, actinides, parity doublets

**Summary**: Comprehensive review of octupole (parity-breaking) deformation in nuclei. Covers HFB with octupole constraint, experimental signatures (anomalous E1, parity doublets), and systematic regions of octupole instability (actinides Z~88-94, N~134-140). Demonstrates that octupole deformation is mean-field driven.

**Key Results**:
- Confirmed octupole deformation in Ra-223, Ra-225, Ac-225, Ra-226, Th-229
- E1 transitions 100-1000x single-particle estimates
- Parity mixing 1-10% in actinides
- Octupole instability condition: d^2E/d(beta_3)^2 < 0

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Octupole instability | $\partial^2 E/\partial\beta_3^2|_{\beta_3=0} < 0$ | Stability section |
| E1 strength | $B(E1) = (e^2/4\pi(2I+1))|\langle I'||D||I\rangle|^2$ | E1 section |

**Dependencies**: Uses 07 (deformed spectra); connects to 05 (octupole in fission)

---

### Paper 10: Shape Coexistence and Triaxiality in Superheavy Nuclei
- **File**: `10_2005_Caurier_Shape_Coexistence_Superheavy.md`
- **arXiv**: N/A
- **Year**: 2005
- **Relevance**: MEDIUM
- **Tags**: superheavy, shape coexistence, triaxiality, GCM, Gogny D1S, potential energy surface
- **KNOWN ISSUE**: Authors in filename are Caurier/Sieja; actual authors likely Cwiok/Heenen/Nazarewicz (Nature 433, 705).

**Summary**: Investigates competing shapes in superheavy nuclei using Gogny-D1S DFT + GCM. Reveals coexisting spherical, prolate, oblate, and triaxial minima within 0.1-1 MeV. Prolate ground states dominate despite Coulomb repulsion. Predicts triaxial deformation near Z=114, N=184.

**Key Results**:
- Abundant shape coexistence in SH nuclei
- Prolate ground states dominate for most SH nuclei
- Z=114 shell closure competes with prolate deformed closure
- GCM provides configuration mixing framework

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| GCM wave function | $|\Psi_\alpha\rangle = \int dq\,f_\alpha(q)|\Psi[q]\rangle$ | GCM section |
| Triaxiality parameter | $\gamma = \arctan[\sqrt{3}(b^2-a^2)/(2c^2-a^2-b^2)]$ | Triaxial section |

**Dependencies**: Builds on 07, 01; connects to 13 (GCM), 05 (fission)

---

### Paper 11: Impact of Nuclear Mass Uncertainties on the r-Process
- **File**: `11_2012_Marketin_r_Process_Rates.md`
- **arXiv**: N/A (PRC 85, 054302)
- **Year**: 2012
- **Relevance**: MEDIUM
- **Tags**: r-process, mass uncertainty, neutron separation energy, beta decay, FRIB, nucleosynthesis

**Summary**: Quantifies how nuclear mass uncertainties propagate through r-process abundance calculations. 50-100 keV mass precision needed for 5% abundance accuracy. Identifies critical bottleneck nuclei near N=50, 82 closures. 100 keV mass shift at branching points redirects 20-50% of network flow.

**Key Results**:
- 50-100 keV mass accuracy required for 5% r-process abundance precision
- Critical nuclei identified near N=50 (^80Zn, ^82Ge)
- 100 keV mass error at branching points redirects 20-50% of network flow

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Rate sensitivity | $\Delta\sigma/\sigma \approx \Delta M / k_B T$ | Mass dependence |
| Neutron separation energy | $S_n = M(A-1,Z) + m_n - M(A,Z)$ | S(n) section |

**Dependencies**: Uses 12 (mass predictions); synthesized in 14

---

### Paper 12: Large-Scale Mass Table (UNEDF)
- **File**: `12_2012_Erler_UNEDF_Large_Scale_Mass_Table.md`
- **arXiv**: N/A (Nature 486, 509)
- **Year**: 2012
- **Relevance**: HIGH
- **Tags**: mass table, UNEDF, Skyrme HFB, 9400 nuclei, drip line, deformation, leadership computing

**Summary**: State-of-the-art DFT mass calculation for ~9,400 nuclei using optimized Skyrme HFB. Achieves ~600 keV rms deviation. Correctly predicts ground-state deformations, shell closures, and the two-neutron drip line. Establishes nuclear DFT as a comprehensive predictive tool.

**Key Results**:
- 9,400 nuclei from Z=1 to Z=120 computed
- 600 keV global rms deviation from experiment
- Deformations correctly predicted (prolate/oblate)
- Neutron drip line accurate to 2 nucleons (Z>20)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Skyrme energy | $E = \int d\mathbf{r}\,\epsilon(\rho,\tau,s,\ldots)$ | Skyrme EDF |
| Density-dependent pairing | $V_{\text{pair}} = -G(1-\eta\rho)\delta(\mathbf{r}-\mathbf{r}')$ | Pairing |

**Dependencies**: Uses 04 (Hamiltonian context); feeds into 06, 11

---

### Paper 13: Configuration Mixing of Angular-Momentum Projected Triaxial RMF Wave Functions (GCM)
- **File**: `13_2010_Rodriguez_Generator_Coordinate_Method_Beyond_Mean_Field.md`
- **arXiv**: 0912.2650
- **Year**: 2010
- **Relevance**: HIGH
- **Tags**: GCM, angular momentum projection, triaxiality, K-mixing, relativistic EDF, ^24Mg, beyond mean field
- **KNOWN ISSUE**: arXiv 0912.2650 is Yao/Meng/Ring/Vretenar (PRC 81, 044311), NOT Rodriguez/Nazarewicz. Filename is misleading. Content is valid GCM.

**Summary**: Extends relativistic EDF to include symmetry restoration (3D AMP) and GCM configuration mixing for triaxial shapes. Applied to ^24Mg: triaxiality lowers energies by ~300 keV; K-mixing essential for gamma-band (2^+_2 is 87% K=2). B(E2) reproduced without effective charges. Norm eigenvalue cutoff and particle-number correction discussed.

**Key Results**:
- Triaxial shapes lower energies by ~300 keV, enhance B(E2) by 4-8%
- K-mixing essential for gamma-band structure
- ^24Mg ground state predominantly prolate (beta ~ 0.5)
- Spectra systematically stretched (projection after variation)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| GCM wave function | $|\Psi^{JM}_\alpha\rangle = \int dq\sum_K f^{JK}_\alpha(q)|JMK+,q\rangle$ | Eq. (2) |
| AMP operator | $\hat{P}^J_{MK} = \frac{2J+1}{8\pi^2}\int d\Omega D^{J*}_{MK}(\Omega)\hat{R}(\Omega)$ | Eq. (5) |
| Hill-Wheeler-Griffin | $\int dq'\sum_{K'}[H^J_{KK'} - E^J_\alpha N^J_{KK'}]f^{JK'}_\alpha = 0$ | Eq. (14) |

**Dependencies**: Connects to 10 (GCM in superheavy); uses 03 (HFB pairing)

---

### Paper 14: Nuclear Structure at the Limits
- **File**: `14_2009_Nazarewicz_Structure_at_the_Limits.md`
- **arXiv**: N/A (2009 Nucl. Phys. News 19, 5)
- **Year**: 2009
- **Relevance**: MEDIUM
- **Tags**: synthesis, drip line, halo nuclei, shell evolution, superheavy, r-process, fission, review

**Summary**: Synthesis article surveying nuclear structure across extremes: shell evolution, halo nuclei, shape coexistence, pairing persistence near drip lines, superheavy island of stability, and r-process. Argues exotic nuclei hold key to fundamental forces.

**Key Results**:
- Universal phenomena: halo, shape isomerism, pairing persistence across chart
- New magic numbers at N=14 (O chain), N=28 (Ne-Mg-Si)
- Pairing gap persists (~1 MeV) even in dilute halo systems
- Island of stability near Z=114, N=184

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Tensor shell shift | $\Delta\epsilon = \langle i|V_T^{(1)}|i\rangle\rho^{\text{opposite}}$ | Shell evolution |
| Halo radius | $r_{\text{halo}} \sim \hbar/\sqrt{2m|E_{\text{sep}}|}$ | Halo nuclei |

**Dependencies**: Synthesizes 01, 02, 10, 11; provides context for all papers

---

### Paper 15: Exactly Solvable Richardson-Gaudin Models for Many-Body Quantum Systems (Colloquium)
- **File**: `15_2004_Dukelsky_Pittel_Sierra_RG_Colloquium.md`
- **arXiv**: nucl-th/0405011
- **Year**: 2004
- **Relevance**: CRITICAL
- **Tags**: Richardson-Gaudin, exact solution, integrability, pairing model, electrostatic mapping, BCS large-N limit, ultrasmall grains, IBM, quasi-spin

**Summary**: Definitive review of Richardson-Gaudin exactly solvable pairing models. Pairing Hamiltonian is integrable with L commuting CRS quantum invariants. Electrostatic mapping: pairons as free charges, orbitons as fixed charges. BCS emerges as large-N limit via arc of pair energies. Applications to ultrasmall grains (smooth SC/FD crossover), IBM phase transitions, and fragmented boson condensates.

**Key Results**:
- Richardson's exact solution: M coupled nonlinear equations for pair energies
- L commuting CRS operators establish integrability
- Three RG families: rational, trigonometric, hyperbolic
- Exact 2D electrostatic mapping of quantum pairing
- BCS gap equation = large-N limit of Richardson equations
- SC/FD crossover completely smooth (no phase transition)
- Randomness enhances pairing correlations

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Pairing Hamiltonian | $H_P = \sum_l \varepsilon_l \hat{n}_l + (g/2)\sum_{ll'} A^\dagger_l A_{l'}$ | Eq. 4 |
| Richardson equations | $1 - 4g\sum_l d_l/(2\varepsilon_l - E_\alpha) + 4g\sum_{\beta\neq\alpha} 1/(E_\alpha - E_\beta) = 0$ | Eq. 9 |
| CRS quantum invariants | $R_l = K^0_l + 2g\sum_{l'\neq l}[\frac{1}{2}(K^+_l K^-_{l'} + \text{h.c.}) + K^0_l K^0_{l'}]/(\varepsilon_l-\varepsilon_{l'})$ | Eq. 24 |
| BCS gap equation (large-N) | $\int \rho(\varepsilon)d\varepsilon/\sqrt{(\varepsilon/2-\lambda)^2+\Delta^2} = 1/G$ | Eq. 51 |
| Electrostatic equilibrium | $e + \sum_j q_j/(z_j-z_\alpha) - \sum_{\beta\neq\alpha} q_\beta/(z_\alpha-z_\beta) = 0$ | Eq. 43 |
| Condensation energy | $E^C_b = E^{GS}_b - \langle FS|H_{BCS}|FS\rangle$ | Eq. 57 |

**Dependencies**: Foundational for integrability; connects to 17, 23

---

### Paper 16: Quadrupole Collective Inertia in Nuclear Fission: Cranking Approximation (ATDHFB)
- **File**: `16_2011_Baran_ATDHFB_Collective_Inertia.md`
- **arXiv**: 1007.3763
- **Year**: 2011
- **Relevance**: CRITICAL
- **Tags**: ATDHFB, collective inertia, cranking, GOA, fission, mass tensor, level crossings, ^256Fm

**Summary**: Derives and compares collective mass tensor from cranking (ATDHFB-C), perturbative cranking (ATDHFB-Cp), and GOA for ^256Fm fission. Non-perturbative mass shows sharp peaks at level crossings correlated with shell structure changes. Perturbative treatment misses these. Canonical approximation validated. Perturbative derivatives cannot be justified.

**Key Results**:
- Non-perturbative ATDHFB-C mass: sharp peaks at level crossings
- Perturbative cranking underestimates mass variations
- ATDHFB-C close to canonical approximation ATDHFB-Cc
- Peak structures correlate with configuration changes
- Perturbative treatment cannot be justified quantitatively

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| ATDHFB kinetic energy | $K = (i/4)\text{Tr}(\dot{\mathcal{R}}_0[\mathcal{R}_0,\mathcal{R}_1])$ | Eq. 14 |
| Mass tensor | $M_{ij} = (i/2\dot{q}_i\dot{q}_j)\text{Tr}(F^{i*}Z^j - F^iZ^{j*})$ | Eq. 32 |
| Cranking mass | $M^C_{ij} = (1/2\dot{q}_i\dot{q}_j)\sum_{\mu\nu}(F^{i*}_{\mu\nu}F^j_{\mu\nu} + \text{c.c.})/(E_\mu+E_\nu)$ | Eq. 34 |
| Perturbative cranking | $M^{Cp} \approx \sum_{\mu\nu}\langle\mu|h^i|\nu\rangle\langle\nu|h^j|\mu\rangle/(\breve{E}_\mu+\breve{E}_\nu)^3(\eta^+)^2$ | Eq. 60 |
| GOA mass | $M^{\text{GOA}} = S^{(2)}[S^{(1)}]^{-1}S^{(2)}$ | Eq. 62 |

**Dependencies**: Foundational for fission dynamics; feeds into 20, 05, 24, 21

---

### Paper 17: Superconductivity in Ultrasmall Metallic Grains
- **File**: `17_2001_vonDelft_Ultrasmall_BCS.md`
- **arXiv**: cond-mat/0101021
- **Year**: 2001
- **Relevance**: CRITICAL
- **Tags**: ultrasmall grains, BCS breakdown, Anderson criterion, parity effects, blocking, Richardson exact solution, canonical pairing, SC/FD crossover

**Summary**: Comprehensive review of BCS in ultrasmall metallic grains (d ~ Delta). Single-electron tunneling spectroscopy experiments, discrete BCS model, blocking effects, generalized variational BCS (each eigenstate needs own pairing parameter), paramagnetic breakdown, Richardson's exact solution showing smooth SC/FD crossover. Key benchmarks: Anderson criterion d >= Delta, Matveev-Larkin parameter minimum at d/Delta ~ 0.5.

**Key Results**:
- Anderson criterion for BCS breakdown: d >= Delta
- Each eigenstate requires its own pairing parameter Delta_{s,B}
- Blocking: singly-occupied levels excluded from pair scattering
- SC/FD crossover completely smooth (no phase transition)
- "Minimal superconductivity" regime: d/Delta in [0.77, 2.36]
- Randomness enhances pairing correlations

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Level spacing | $d = 2\pi^2\hbar^2/(mk_F \cdot \text{Vol})$ | Eq. 1 |
| Discrete BCS Hamiltonian | $\hat{H} = \sum_{j,\sigma}(\varepsilon_j-\mu-\sigma h)c^\dagger_{j\sigma}c_{j\sigma} - \lambda d\sum_{ij}b^\dagger_i b_j$ | Eq. 6 |
| Bulk gap | $\tilde{\Delta} = \omega_D/\sinh(1/\lambda)$ | Eq. 8 |
| Canonical pairing parameter | $\Delta^2_{\text{can}} = (\lambda d)^2\sum_{ij}(C_{ij} - \langle c^\dagger_{i+}c_{j+}\rangle\langle c^\dagger_{i-}c_{j-}\rangle)$ | Eq. 22 |
| CC critical field | $h_{CC} = \tilde{\Delta}/\sqrt{2}$ | Sec. 7 |

**Dependencies**: Uses Richardson's solution from 15; provides benchmarks for framework's d/Delta regime

---

### Paper 18: Pairing Interaction and Two-Nucleon Transfer Reactions
- **File**: `18_2014_Potel_Pair_Transfer.md`
- **arXiv**: 1404.1317
- **Year**: 2014
- **Relevance**: CRITICAL
- **Tags**: pair transfer, Cooper pairs, pairing vibrations, pairing rotations, two-nucleon transfer, DWBA, induced interaction, ^11Li halo

**Summary**: Reviews nuclear pairing through two-nucleon transfer reactions. Dual origins: bare NN + phonon-mediated induced. Pairing vibrations condense into superfluid phase. Successive transfer dominates (xi ~ 36 fm >> R). In ^11Li, induced pairing via pygmy resonance exchange dominates. Gap equation modified by Z-factors from self-energy.

**Key Results**:
- Nuclear pairing: bare + induced contributions comparable
- Two-nucleon transfer = specific probe of Cooper pairs
- Successive transfer dominates (xi ~ 36 fm >> R)
- ^11Li: induced pairing dominates (pygmy resonance bootstrap)
- Sn isotopes: clearest pairing rotational bands

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Correlation length | $\xi \approx \hbar v_F/\Delta \approx 36$ fm | Sec. 2 |
| Gap with Z-factors | $\Delta_j = -\sum_k V^{\text{eff}}_{jk}\Delta_k/(2E_k Z_k)$ | Sec. 3 |
| Gap with fluctuations | $\Delta = (\Delta_0^2 + S_0(\text{RPA})/2)^{1/2}$ | Sec. 3 |

**Dependencies**: Uses HFB amplitudes from 03; connects to 15, 19

---

### Paper 19: The Giant Pairing Vibration in Heavy Nuclei: Present Status and Future Studies
- **File**: `19_2019_GPV_Heavy_Nuclei_Review.md`
- **arXiv**: 1905.01339
- **Year**: 2019
- **Relevance**: HIGH
- **Tags**: giant pairing vibration, pair transfer, Q-value mismatch, continuum coupling, ^14C, ^15C, Sn, Pb, alpha decay

**Summary**: Reviews the GPV at ~65/A^{1/3} MeV excitation from second major shell. Identified in ^14,15C but elusive in heavy nuclei due to Q-value mismatch and continuum broadening. Weakly-bound projectiles (^6He, ^11Li) best candidates for Pb. Connection to alpha-decay clustering provides independent evidence.

**Key Results**:
- GPV at ~65/A^{1/3} MeV, carrying 20-100% of gs cross section
- Identified in ^14,15C but elusive in Sn, Pb
- Q-value mismatch exponentially suppresses standard (p,t) population
- Continuum makes two-neutron GPV in heavy nuclei very broad
- GPV connected to alpha-decay clustering

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| RPA dispersion | $F(E) = \sum_j(2j+1)/(E-2e_j) = 2/G$ | Eq. 2 |
| GPV cross section | $\sigma(\text{GPV}) \sim \Omega \cdot \sigma_{\text{sp}}$ | Eq. 4 |
| Q-value quenching | $\sigma \sim \exp[-(Q-Q_{\text{opt}})^2/(2\hbar^2\kappa r_0)]$ | Eq. 5 |

**Dependencies**: Extends 18; uses pairing from 03, 15

---

### Paper 20: Pairing-Induced Speedup of Nuclear Spontaneous Fission
- **File**: `20_2014_Sadhukhan_Pairing_Speedup_Fission.md`
- **arXiv**: 1410.1264
- **Year**: 2014
- **Relevance**: HIGH
- **Tags**: pairing speedup, fission dynamics, least-action, ATDHFB, dynamic pairing, ^264Fm, ^240Pu

**Summary**: Pairing correlations are dynamically enhanced along the least-action fission path, reducing collective inertia (M ~ Delta^{-2}) and shortening SF half-lives by ~3 OOM. For ^240Pu, pairing fluctuations completely restore axial symmetry, replacing triaxiality. Particle-particle correlations must be treated on same footing as shape.

**Key Results**:
- Pairing dynamically enhanced along least-action path
- M ~ Delta^{-2}: larger gap -> lower inertia -> faster tunneling
- SF half-life reduced by ~3 OOM (^264Fm)
- ^240Pu: pairing fluctuations restore axial symmetry
- Static barrier picture dramatically modified by dynamics

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Fission action | $S(L) = (1/\hbar)\int\sqrt{2M_{\text{eff}}(V-E_0)}\,ds$ | Eq. 1 |
| Constrained HFB | $\hat{H}' = \hat{H}_{\text{HFB}} - \sum_\mu\lambda_\mu\hat{Q}_{2\mu} - \sum_\tau(\lambda_\tau\hat{N}_\tau - \lambda^2_\tau\Delta\hat{N}^2_\tau)$ | Eq. 2 |
| Inertia-pairing | $M \sim \Delta^{-2}$ | Text |

**Dependencies**: Uses 16 (ATDHFB); applies to 05 (fission)

---

### Paper 21: Neural Network Emulation of Spontaneous Fission
- **File**: `21_2024_Lay_NN_Fission_Emulator.md`
- **arXiv**: 2310.01608
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: neural network, emulation, fission, PES, collective inertia, r-process, Gogny D1S

**Summary**: NN emulation of DFT fission observables across the nuclear chart. PES to ~500 keV RMSE; diagonal inertia within ~1 OOM. SF half-lives within 10^3 across 70+ OOM. Eigenvalue decomposition of inertia tensor enables multi-scale training.

**Key Results**:
- PES RMSE ~500 keV, architecture-independent
- Diagonal inertia within ~1 OOM
- SF half-lives within 10^3 over 70+ OOM
- Exit points well-reproduced

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| ATDHFB inertia | $M_{\mu\nu} = (\hbar^2/2\dot{q}_\mu\dot{q}_\nu)\sum_{\alpha\beta}(|F|^2+\text{c.c.})/(E_\alpha+E_\beta)$ | Eq. (5) |
| WKB tunneling | $P_{\text{fis}} = 1/(1+\exp(2S))$ | Eq. (1) |

**Dependencies**: Uses 16 (ATDHFB); applies 06 methodology to 05 context

---

### Paper 22: Theoretical Descriptions of Compound-Nuclear Reactions
- **File**: `22_2014_Kawano_Compound_Nucleus.md`
- **arXiv**: 1403.0923
- **Year**: 2014
- **Relevance**: HIGH
- **Tags**: compound nucleus, Hauser-Feshbach, Feshbach projection, KKM theory, doorway states, Ericson fluctuations, pre-equilibrium, surrogate

**Summary**: Modern review of compound nuclear reactions. Hauser-Feshbach with width fluctuation corrections (elastic enhancement 2-3x), Feshbach projection theory, KKM energy-averaging, doorway states (escape + spreading widths), Ericson correlation function, exciton pre-equilibrium model, and surrogate reactions.

**Key Results**:
- HF with width fluctuations: elastic enhancement 2 (overlapping) to 3 (isolated)
- KKM: incoherent sum of optical and fluctuation cross sections
- Doorway transmission: Breit-Wigner with escape and spreading widths
- Ericson correlation width gives CN lifetime
- Equal-occupation assumption violated for low exciton numbers

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Hauser-Feshbach | $\sigma_{cc'} = T_c T_{c'}/\sum_{c''}T_{c''}$ | Eq. (3) |
| Doorway transmission | $P_{00} = \Gamma^{\uparrow}\Gamma^{\downarrow}/[(E-E_D)^2+(\Gamma_D/2)^2]$ | Eq. (35) |
| Ericson correlation | $C(\varepsilon) = \langle\sigma\rangle^2/[1+(\varepsilon/\Gamma_{\text{corr}})^2]$ | Eq. (41) |
| KKM fluctuation | $\sigma^{\text{fl}} = (P_{cc}P_{c'c'}+P_{cc'}P_{c'c})/\text{Tr}(P)$ | Eq. (26) |

**Dependencies**: Standalone reaction theory; applied in S42

---

### Paper 23: Overview of Seniority Isomers
- **File**: `23_2022_Maheshwari_Seniority_Isomers.md`
- **arXiv**: 2212.06258
- **Year**: 2022
- **Relevance**: MEDIUM
- **Tags**: seniority, quasi-spin, isomers, parabolic B(EL), generalized seniority, multi-j, GSSM

**Summary**: Reviews seniority isomers across the nuclear chart. Quasi-spin algebra (SU(2)) for pair creation/annihilation. Seniority reduction formulae for odd-tensor (preserving) and even-tensor (parabolic, vanishing at mid-shell). Generalized seniority for multi-j shells with (-1)^{l_j} phase. Novel odd-electric seniority isomers. Berry phase can destroy isomers at mid-shell.

**Key Results**:
- Seniority v governs isomerism via electric matrix element cancellation
- Odd-tensor: preserve seniority; even-tensor: Delta_v = 0, +-2
- Generalized seniority extends single-j rules with (-1)^{l_j}
- GSSM explains g-factors without fitting
- Berry phase at mid-shell destroys seniority isomers

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Pair creation | $S^+_j = \sum_{m>0}(-1)^{j-m}a^+_{jm}a^+_{j,-m}$ | Eq. (1) |
| Quasi-spin | $[S^+, S^-] = \hat{n} - \Omega = 2S^0$ | Eq. (5) |
| Pairing eigenvalues | $E(n,v) = -G(n-v)(2\Omega+2-n-v)/2$ | Eq. (7) |
| Even-tensor reduction | $\langle j^n v||Y^L||j^n v\rangle = [(\Omega-n)/(\Omega-v)]\langle j^v||Y^L||j^v\rangle$ | Eq. (13) |

**Dependencies**: Quasi-spin algebra underlies 15; blocking connects to 08, 17

---

### Paper 24: Iterative Solutions of the ATDHFB Equations
- **File**: `24_2024_ATDHFB_Iterative.md`
- **arXiv**: 2411.18404
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: iterative ATDHFB, time-odd mean fields, collective inertia, SVD decomposition, HFODD

**Summary**: Iterative method for ATDHFB without full two-body stability matrix. Time-odd mean fields increase rotational inertia by 1.2-1.4x over Inglis-Belyaev. SVD decomposition of time-odd density constructs adiabatic basis. Validated against dynamical cranking for ^20Ne (axial) and ^126Ba (triaxial). Vibrational mass tensor for ^74Ge to 1% diagonal / 4% off-diagonal.

**Key Results**:
- Iterative ATDHFB = dynamical cranking (exact agreement)
- Time-odd fields: 1.2-1.4x enhancement over Inglis-Belyaev
- Only one-body operators needed
- Dominant: current density j(r) and spin density s(r)
- Full single-particle space required for convergence

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Collective inertia | $M = -i\,\text{Tr}(\dot{\rho}_0[\rho_1,\rho_0])/\dot{q}^2$ | Eq. (5) |
| Iterative update | $\rho^{(n+1)}_{1,ph} = (\epsilon_p-\epsilon_h)^{-1}[i\dot{q}(\partial\rho_0/\partial q)_{ph} - \Gamma^{(n)}_{1,ph}]$ | Eq. (6) |
| SVD of rho_1 | $\rho_1 = \begin{pmatrix}0 & UrV^+\\VrU^+ & 0\end{pmatrix}$ | Eq. (7) |

**Dependencies**: Extends 16; provides non-perturbative benchmark for 20, 21

---

### Paper 25: Dense Nuclear Matter Equation of State from Heavy-Ion Collisions
- **File**: `25_2023_Dense_Nuclear_Matter_EOS.md`
- **arXiv**: 2301.13253
- **Year**: 2024 (v4)
- **Relevance**: MEDIUM
- **Tags**: EOS, heavy-ion collisions, BUU transport, symmetry energy, neutron stars, chiral EFT, Bayesian, FRIB

**Summary**: White paper on nuclear EOS from heavy-ion collisions at intermediate energies (0.3-5 n_0). BUU transport, chiral EFT, neutron star constraints (TOV, tidal deformability), collective flow, Bayesian multi-source combination. Symmetry energy slope L ~ 40-70 MeV. Non-equilibrium transport essential for EOS extraction.

**Key Results**:
- Heavy-ion collisions probe 0.3-5 n_0
- S_v ~ 30-34 MeV, L ~ 40-70 MeV
- Transport model uncertainties dominate
- Bayesian HIC + NS + chiral EFT narrows EOS band

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| EOS expansion | $E/A(n,\delta) = E/A(n,0) + S(n)\delta^2 + \ldots$ | Sec. 1 |
| BUU transport | $\partial f/\partial t + (\partial\epsilon/\partial\mathbf{p})\cdot\nabla_r f - (\partial\epsilon/\partial\mathbf{r})\cdot\nabla_p f = I_{\text{coll}}$ | Sec. 2.1 |
| TOV equation | $dP/dr = -G(\epsilon+P)(m+4\pi r^3 P)/[r(r-2Gm)]$ | Sec. 2.3 |

**Dependencies**: Connects to 04, 12

---

### Paper 26: Chronicle of the Discovery of the Back-Bending Phenomenon
- **File**: `26_2021_Ryde_Backbending_Chronicle.md`
- **arXiv**: 2109.08144
- **Year**: 2021
- **Relevance**: MEDIUM
- **Tags**: backbending, historical, ^160Dy, ^162Er, pairing collapse, Mottelson-Valatin, detector technology

**Summary**: Personal recollection by Hans Ryde of backbending discovery 50 years earlier. First observed in ^160Dy (1970), archetypal S-curve in ^162Er. Mechanism: rotational alignment breaks Cooper pairs (pairing collapse), analogous to magnetic pair breaking in superconductors (Mottelson-Valatin 1960). Enabled by systematic surveys + Ge(Li) detector precision.

**Key Results**:
- Backbending = anomalous moment of inertia increase at critical omega
- First observed ^160Dy (1970), archetypal ^162Er
- Mechanism: Cooper pair breaking by rotation
- Mottelson-Valatin analogy: rotation <-> magnetic field
- Standard plot: I vs omega^2 (Bohr, 1969)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Critical frequency | $\omega_c \sim \Delta/j_\perp$ | Standard result |
| MV analogy | Rotation <-> magnetic field; nuclear pairs <-> electron pairs | Ref. [13] |

**Dependencies**: Historical complement to 08; connects to 23

---

## Cross-Paper Equation Concordance

### HFB Matrix Equation
Referenced in: Papers 02, 03, 12, 13
$$\begin{pmatrix} h-\lambda & \Delta \\ -\Delta^* & -h^*+\lambda \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} = E \begin{pmatrix} u \\ v \end{pmatrix}$$

### Pairing Gap / BCS Gap Equation
Referenced in: Papers 02, 03, 08, 15, 17, 18
Various forms. Most general: $\Delta_k = -(1/2)\sum_{k'} V_{kk'} \Delta_{k'}/E_{k'}$ where $E_k = \sqrt{(\varepsilon_k-\lambda)^2 + \Delta_k^2}$.
Large-N limit (Paper 15): $\int \rho(\varepsilon)d\varepsilon/\sqrt{(\varepsilon/2-\lambda)^2+\Delta^2} = 1/G$.

### Shell Correction (Strutinsky)
Referenced in: Papers 07, 08, 10
$$E_{\text{shell}} = \sum_i \varepsilon_i - \int_0^{\varepsilon_F} g(\varepsilon)\varepsilon\,d\varepsilon$$

### ATDHFB Collective Inertia
Referenced in: Papers 05, 16, 20, 21, 24
Core form: $M_{ij} = (i/2\dot{q}_i\dot{q}_j)\text{Tr}(F^{i*}Z^j - F^iZ^{j*})$.
Pairing dependence: $M \sim \Delta^{-2}$ (Papers 16, 20).

### WKB Fission Action Integral
Referenced in: Papers 05, 20, 21
$$S(L) = (1/\hbar)\int_{s_{\text{in}}}^{s_{\text{out}}} \sqrt{2M_{\text{eff}}(s)(V(s)-E_0)}\,ds$$

### Richardson Equations
Referenced in: Papers 15, 17
$$1 - 4g\sum_l \frac{d_l}{2\varepsilon_l - E_\alpha} + 4g\sum_{\beta\neq\alpha}\frac{1}{E_\alpha - E_\beta} = 0$$

### Hauser-Feshbach Cross Section
Referenced in: Paper 22
$$\sigma_{cc'} = W_{cc'} T_c T_{c'}/\sum_{c''} T_{c''}$$

### Seniority Reduction (Even-Tensor)
Referenced in: Paper 23
$$\langle j^n v||Y^L||j^n v\rangle = \frac{\Omega-n}{\Omega-v}\langle j^v v||Y^L||j^v v\rangle$$

### Quasi-Spin Commutator
Referenced in: Papers 15, 23
$$[S^+, S^-] = \hat{n} - \Omega = 2S^0$$
(Same algebra underlies both Richardson-Gaudin integrability and seniority classification.)

---

## Notation Conventions

| Symbol | Meaning | Used in |
|:---|:---|:---|
| $\rho$ | Normal density matrix $\rho_{\mu\nu} = \langle a^\dagger_\nu a_\mu\rangle$ | All HFB papers |
| $\kappa$ | Pairing tensor $\kappa_{\mu\nu} = \langle a_\nu a_\mu\rangle$ | 02, 03, 12, 16 |
| $\Delta$ | Pairing field (pp mean field) | All pairing papers |
| $\Gamma$ | Particle-hole mean field (HF potential) | 03, 16, 24 |
| $u_k, v_k$ | Bogoliubov amplitudes | 02, 03, 12, 17 |
| $E_k$ | Quasiparticle energy $\sqrt{(\varepsilon_k-\lambda)^2+\Delta_k^2}$ | All BCS papers |
| $\lambda$ | Chemical potential (Fermi energy) | All HFB papers |
| $\beta_2, \beta_3$ | Quadrupole, octupole deformation parameters | 07, 08, 09, 10 |
| $\gamma$ | Triaxiality parameter (0=prolate, 60=oblate) | 10, 13 |
| $\omega$ | Rotational frequency (cranking) | 08, 26 |
| $g, G$ | Pairing strength (dimensionless or MeV) | 15, 17, 18, 19, 23 |
| $v$ | Seniority (number of unpaired nucleons) | 23 |
| $S^+, S^-, S^0$ | Quasi-spin operators | 15, 23 |
| $\Omega$ | Pair degeneracy $(2j+1)/2$ | 15, 17, 23 |
| $d$ | Mean level spacing (ultrasmall grains) | 17 |
| $E_\alpha$ | Richardson pair energies (complex) | 15, 17 |
| $Q_{20}, Q_{30}$ | Quadrupole, octupole multipole moments | 05, 10, 13, 16, 20, 21 |
| $M_{ij}$ | Collective mass tensor (ATDHFB) | 16, 20, 21, 24 |
| $T_c$ | Transmission coefficient (compound nucleus) | 22 |
| $\mathcal{R}$ | Generalized density matrix (2x2 block form) | 03, 16, 24 |
| $R_l$ | CRS quantum invariant (Richardson-Gaudin) | 15 |
| $B^\dagger_\alpha$ | Richardson collective pair operator | 15, 17 |

---

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 03 | HFB self-consistency (convergence) | Yes | S48 HFB-SELFCONSIST-48, S52 HFB-FULL-52 |
| 03 | PBCS vs ED correction | Yes | S46 PBCS, S52 (PBCS/ED = 0.97-1.003) |
| 03 | Blocking in odd systems | Partial | S56 NPAIR3-ED-56 |
| 15 | Richardson-Gaudin integrability | Yes | S38 CHAOS-1/2/3, 8 conserved integrals |
| 15 | BCS as large-N limit | Yes | S52 N-PAIR-FULL (bracket [1, 59]) |
| 15 | Electrostatic mapping | No | Not computed in framework |
| 17 | Anderson criterion d/Delta | Yes | S37 d/Delta=0.08, S54 d/Delta=42 |
| 17 | SC/FD smooth crossover | Yes | S38 P_exc=1.000 |
| 17 | Blocking effect on pairing | Yes | S56 NPAIR3 (<r> decreases with N_pair) |
| 16 | ATDHFB collective mass | Partial | S40 M_ATDHFB=1.695 (cranking approx.) |
| 16 | Non-perturbative vs perturbative | No | Framework uses perturbative; 24 gives correction |
| 20 | M ~ Delta^{-2} speedup | Yes | S42 TAU-DYN-REOPEN |
| 08 | Pairing collapse at critical omega | Yes | S38 P_exc=1.000 |
| 08 | Shell correction method | Yes | S44, S53, S55 STRUTINSKY-992 |
| 06 | GP emulator methodology | No | Not applied to framework spectral action |
| 22 | Hauser-Feshbach branching | Partial | S42 HF-KK-42 FAIL (1.51 decades) |
| 22 | Doorway state formalism | Partial | S42 PR=3.17, intermediate structure |
| 23 | Seniority conservation | Yes | S40 eta=0.022, B2 rank-1 86% |
| 23 | Parabolic B(EL) at half-filling | Partial | S54 half-filling confirmed |
| 13 | GCM configuration mixing | No | Framework has not implemented full GCM |
| 19 | GPV cross section scaling | Yes | S37 B_plus=9.94, 85.5% strength |
| 18 | Pair transfer form factor | Yes | S50 J_pair=0.115, F_transfer=2.13 |
| 24 | Time-odd field enhancement (1.2-1.4x) | No | S40 used perturbative; correction uncomputed |

---

## Request Fulfillment Status

Track which items from `agent-requests/nazarewicz-request.md` are now fulfilled:

| Request ID | Title | Status | Paper # |
|:---|:---|:---|:---|
| A1 | Dukelsky RG Colloquium (2004) | FULFILLED | 15 |
| A2 | Baran ATDHFB Quadrupole (2011) | FULFILLED | 16 |
| A3 | von Delft Ultrasmall BCS (2001) | FULFILLED | 17 |
| A4 | Potel Pair Transfer (2014) | FULFILLED | 18 |
| A5 | Aberg Chaos-Assisted Tunneling (1999) | NOT FULFILLED | -- |
| B1 | Feshbach-Kerman-Lemmer Doorway (1967) | NOT FULFILLED | -- |
| B2 | Ericson Fluctuations (1963) | NOT FULFILLED | -- |
| B3 | GPV Heavy Nuclei Review (2019) | FULFILLED | 19 |
| B4 | GPV Fragmentation (2025 PRL) | NOT FULFILLED | -- |
| B5 | GPV ^14C ^15C (2015 Nat. Comm.) | NOT FULFILLED | -- |
| B6 | Backbending Seniority Pauli Blocking | PARTIAL (via 23+26) | 23, 26 |
| B7 | NN Fission Emulator (2024) | FULFILLED | 21 |
| B8 | Pairing-Induced Fission Speedup (2014) | FULFILLED | 20 |
| C5 | Dense Matter EOS (2024) | FULFILLED | 25 |
| C6 | Fifty Years of Backbending | FULFILLED (2021 chronicle) | 26 |
| C7 | Compound Nuclear Reactions (2014) | FULFILLED | 22 |
| C8 | Seniority Isomers Overview (2022) | FULFILLED | 23 |
| C9 | Iterative ATDHFB (2024) | FULFILLED | 24 |
| C10 | FRIB Motivations (2025) | NOT FULFILLED | -- |

### Still Needed (unfulfilled Priority A/B items)
- **A5**: Aberg chaos-assisted tunneling from SD states (PRL 82, 299, 1999) -- critical for SD decay-out analog
- **B1**: Feshbach-Kerman-Lemmer doorway paper (1967) -- original formalism for S42 analysis
- **B2**: Ericson fluctuation theory (1963) -- foundational for V/D classification
- **B4**: GPV fragmentation (2025 PRL) -- tests whether fragmentation destroys GPV coherence
- **B5**: GPV in ^14C/^15C (Nature Comm. 2015) -- experimental benchmark for light-nucleus GPV
