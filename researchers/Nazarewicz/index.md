# Nazarewicz Paper Index

**Researcher**: Witold Nazarewicz (Michigan State University / FRIB)
**Papers**: 14 (1985--2015)
**Primary domain**: Nuclear density functional theory, BCS/HFB pairing, shell structure, deformation, superheavy elements, Bayesian UQ
**Project relevance**: Papers 02, 03, 08 are directly relevant to the framework's BCS pairing mechanism on SU(3). Paper 06 provides the Bayesian methodology used in framework probability assessment. Papers 12, 14 give the global nuclear landscape context. The collection as a whole grounds the nazarewicz-nuclear-structure-theorist agent.

---

## Dependency Graph

```
PAIRING & SUPERFLUIDITY                   DEFORMATION & SHELL STRUCTURE
===========================               ================================

[02] Drip-line pairing (1996) --------+   [07] Woods-Saxon deformed (1987)
  |  HFB coord-space, continuum       |     |  Single-particle spectra
  v                                    |     v
[03] HFB formalism (2013) ------+     |   [01] Shell evolution (2007)
  |  Bogoliubov transform, CHFB |     |     |  Tensor force, magic numbers
  v                              |     |     v
[08] High-spin A~80 (1985)      |     |   [09] Octupole deformation (1996)
     Cranking, pairing collapse  |     |     |  Parity breaking, E1 strengths
                                 |     |     v
                                 |     |   [10] Shape coexistence (2005)
                                 |     |        GCM mixing, superheavy
                                 |     |          |
                                 v     v          v
               COMPUTATIONAL / GLOBAL METHODS
               ================================
               [04] Chiral forces NNLO_sat (2015)
                 |  Ab initio, 3-body, saturation
                 v
               [06] Bayesian UQ for DFT (2015) --------+
                 |  GP emulator, KL divergence, BF      |
                 v                                      |
               [12] UNEDF mass table (2012)             |
                 |  9400 nuclei, ~600 keV rms            |
                 v                                      |
               [13] GCM beyond mean-field (2010)        |
                    Shape mixing, symmetry restoration   |
                                                        |
               APPLICATIONS & SYNTHESIS                 |
               ================================         |
               [05] Superheavy fission (2013) <---------+
                 |  Octupole barriers, WKB lifetimes
                 v
               [11] r-Process rates (2012)
                 |  Mass uncertainties, FRIB targets
                 v
               [14] Structure at limits (2009)
                    Synthesis: halos, drip line, r-process
```

**Critical chain for BCS analogy**: 02 -> 03 -> 08 (pairing formalism -> superfluidity -> collapse)
**Critical chain for UQ methodology**: 06 -> 12 (Bayesian inference -> global mass table)

---

## Topic Map

### A. BCS Pairing and Nuclear Superfluidity (Papers 02, 03, 08)
HFB formalism in coordinate space, Bogoliubov transformation, continuum coupling via Berggren contour, pairing gap evolution with spin, Cooper pair persistence at drip line, density-dependent pairing functionals. **CRITICAL** — direct analog to framework's BCS mechanism on SU(3). Session 23a K-1e closure (BdG M_max=0.077) used HFB gap equation structure from these papers.

### B. Shell Structure and Tensor Force (Papers 01, 07, 14)
Woods-Saxon deformed potential, single-particle spectra, spin-orbit coupling, tensor-driven shell evolution, magic number erosion in neutron-rich nuclei, intruder orbitals. **HIGH** — shell gaps map to Dirac eigenvalue gaps on deformed SU(3).

### C. Deformation and Shape Coexistence (Papers 07, 08, 09, 10, 13)
Quadrupole/octupole deformation parameters, parity-violating pear shapes, competing prolate/oblate/triaxial configurations, GCM configuration mixing, shape isomerism in superheavy elements. **HIGH** — nuclear deformation as collective phonon amplitude of internal geometry.

### D. Computational Methods and UQ (Papers 04, 06, 12, 13)
Chiral EFT interactions (NNLO_sat), Bayesian uncertainty quantification, Gaussian process emulators, KL divergence for information content, GCM beyond-mean-field, UNEDF 9400-nucleus mass table. **HIGH** — Paper 06 methodology directly informs framework probability assessment (Bayes factors, posterior updates).

### E. Superheavy Elements and Fission (Papers 05, 10)
Spontaneous fission barriers, reflection-asymmetric WKB tunneling, octupole-driven barrier lowering, island of stability predictions, competing decay modes. **MEDIUM** — geometric instability analog.

### F. Nuclear Astrophysics (Papers 11, 14)
r-Process nucleosynthesis, mass uncertainty propagation, branching points, FRIB measurement priorities, neutron drip line position. **MEDIUM** — observational context for pairing predictions.

---

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| BCS gap equation, pairing mechanism | 02, 03 | CRITICAL |
| Pairing collapse, high-spin behavior | 08, 03 | CRITICAL |
| HFB equations, Bogoliubov transformation | 03, 02 | CRITICAL |
| Bayesian model comparison, Bayes factors | 06 | CRITICAL |
| Shell structure, magic numbers | 01, 07, 14 | HIGH |
| Deformation parameters, shape coexistence | 07, 09, 10, 13 | HIGH |
| Nuclear DFT, Skyrme functionals | 12, 04 | HIGH |
| GCM, beyond mean-field, configuration mixing | 13, 10 | HIGH |
| Chiral forces, ab initio nuclear structure | 04 | HIGH |
| Octupole deformation, parity breaking | 09, 05 | HIGH |
| Superheavy elements, fission barriers | 05, 10 | MEDIUM |
| r-Process, nucleosynthesis, FRIB | 11, 14 | MEDIUM |
| Uncertainty quantification, GP emulators | 06 | MEDIUM |
| Continuum effects, drip-line physics | 02, 14 | MEDIUM |

---

## Paper Entries

### Paper 01: Shell Structure of Exotic Nuclei
- **File**: `01_2007_Dobaczewski_Shell_Structure_Exotic_Nuclei.md`
- **Year**: 2007
- **Authors**: Dobaczewski, Michel, Nazarewicz, Ploszajczak, Rotureau
- **Relevance**: HIGH
- **Tags**: shell-evolution, tensor-force, magic-numbers, exotic-nuclei, continuum

**Summary**: Reviews how nuclear shell structure evolves in neutron-rich nuclei far from stability. The tensor force — subdominant in stable nuclei — becomes critical as N-Z asymmetry grows, driving new magic numbers (N=14, 28) while erasing traditional closures (N=8, 20). Continuum coupling and many-body correlations become essential at the drip line.

**Key Results**:
- Monopole tensor force shifts shell closures measurably in exotic isotopes
- N=8 and Z=8 closures erode in oxygen chain; new closure at N=14
- Continuum HFB mandatory for weakly bound systems (omitting it overestimates binding by 1-3 MeV)
- Ab initio methods confirm tensor forces are as important as central forces

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| $\epsilon_i = \langle i \| U_0 \| i \rangle + \langle i \| V_C \| i \rangle$ | Single-particle energy in mean field | Sec. 2 |
| $\alpha = (N-Z)/(N+Z)$ | Neutron asymmetry parameter | Sec. 2 |
| $g(\mathbf{r}_1,\mathbf{r}_2)$ | Two-body correlation function | Sec. 3 |
| $\|\Psi\rangle = \prod_k(u_k + v_k c^\dagger_k)\|0\rangle$ | Continuum HFB wave function | Sec. 4 |

**Dependencies**: Upstream from 14 (synthesis). Draws on 07 (shell model basis).

---

### Paper 02: Mean-Field Description of Drip-Line Nuclei: Pairing and Continuum Effects
- **File**: `02_1996_Dobaczewski_Mean_Field_Drip_Line_Pairing.md`
- **Year**: 1996
- **Authors**: Dobaczewski, Nazarewicz, Werner, Berger, Chinn, Decharge
- **Relevance**: CRITICAL
- **Tags**: HFB, pairing, continuum, drip-line, Cooper-pairs, density-dependent

**Summary**: Foundational paper reformulating HFB theory in coordinate space to treat continuum effects rigorously. Studies pairing in nuclei with extreme neutron excess where separation energies approach zero. Demonstrates that pairing correlations persist at the drip line despite very low density, with extended pair amplitudes reaching 8-10 fm in halo systems.

**Key Results**:
- Neglecting continuum overestimates binding by 1-3 MeV in drip-line nuclei
- Pairing gap survives at drip line: Delta ~ 0.7 MeV in ^32Ne
- Pair amplitude extends to 8-10 fm in halo nuclei (vs. 3-4 fm in stable)
- Density-dependent pairing better reproduces halo sizes
- Two-neutron separation energies agree with experiment to 0.3 MeV

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| HFB matrix equation | $(h-\lambda, \Delta; -\Delta^*, -h^*+\lambda)(u;v) = E(u;v)$ | Core |
| Pairing field | $\Delta(\mathbf{r}) = -G \sum_k u_k v_k$ | Sec. 3 |
| Pair amplitude | $\kappa(\mathbf{r}) = \sum_k u_k v_k$ | Off-diagonal density |
| Pair coherence length | $\xi_{\rm pair} \sim \hbar/\sqrt{2m_n\|E_F\|}$ | Sec. 4 |
| Berggren contour | Complex-k integration for continuum completeness | Sec. 5 |

**Dependencies**: Foundation for 03 (HFB formalism review). Upstream for all pairing-related papers.

---

### Paper 03: Hartree-Fock-Bogoliubov Solution of the Pairing Hamiltonian in Finite Nuclei
- **File**: `03_2013_Dobaczewski_HFB_Pairing_Hamiltonian.md`
- **Year**: 2013
- **Authors**: Dobaczewski, Nazarewicz
- **Relevance**: CRITICAL
- **Tags**: HFB, Bogoliubov-transformation, nuclear-superfluidity, pairing-functional, BCS

**Summary**: Pedagogical review of the complete HFB formalism for nuclear superfluidity, published in the "50 Years of Nuclear BCS" volume. Covers the Bogoliubov transformation, truncation effects, pairing functional forms (contact, Gogny, density-dependent), continuum HFB via Berggren contour, odd-particle blocking, and regularization. The definitive reference for HFB theory as applied to finite nuclei.

**Key Results**:
- HFB correctly describes both halo nuclei and magic nuclei with single unified theory
- Pairing gap predictions match odd-even mass staggering to 0.1 MeV across nuclear chart
- Gradual superfluid transition: gap maximal at mid-shell (filling fraction f~0.5)
- Deformed superfluids correctly described (identical bands phenomenon)
- Separable pair approximation recovers generalized BCS for finite systems

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| HFB ansatz | $\|\Psi_{\rm HFB}\rangle = \prod_k(u_k + v_k c^\dagger_k c^\dagger_{\bar{k}})\|{\rm vac}\rangle$ | Fundamental |
| Bogoliubov transform | $a_k = u_k\gamma_k + v_k^\dagger\gamma^\dagger_{\bar{k}}$ | Sec. 2 |
| Energy functional | $E[\rho,\kappa] = {\rm Tr}[h\rho] + \frac{1}{2}{\rm Tr}[V\rho\rho] + {\rm Tr}[\Delta\kappa^*]$ | Variational |
| Density-dependent pairing | $\Delta(\mathbf{r}) = -G_0[1-\eta\rho(\mathbf{r})]\kappa(\mathbf{r})$ | Sec. 4 |
| Berggren completeness | $\sum_{\rm bound}\|\phi_k\rangle\langle\phi_k\| + \int_{\rm contour}\frac{dk}{2\pi i}\|\phi_k\rangle\langle\phi_k\| = 1$ | Sec. 5 |

**Dependencies**: Builds on 02 (coordinate-space HFB). Upstream for 08 (high-spin pairing collapse).

---

### Paper 04: Accurate Nuclear Radii and Binding Energies from a Chiral Interaction
- **File**: `04_2015_Ekstrom_Chiral_Nuclear_Radii.md`
- **Year**: 2015
- **Authors**: Ekstrom, Jansen, Wendt, Hagen, Papenbrock, Carlsson, Forssen, Hjorth-Jensen, Navratil, Nazarewicz
- **Relevance**: HIGH
- **Tags**: chiral-EFT, ab-initio, three-body-forces, coupled-cluster, saturation-point, NNLO_sat

**Summary**: Introduces the NNLO_sat chiral interaction — optimized simultaneously to NN scattering data, few-body binding energies/radii, and the empirical nuclear matter saturation point. Using coupled-cluster calculations, achieves accurate binding energies and radii from ^4He to ^40Ca. Demonstrates that a single chiral interaction can provide unified description across multiple scales.

**Key Results**:
- NNLO_sat simultaneously fits scattering data, binding energies to ^40Ca, and charge radii
- Saturation at rho_0 = 0.16 fm^-3, E_0 = -16.0 MeV reproduced
- Collective 3^- states in ^16O and ^40Ca correctly predicted
- Coupled-cluster converges smoothly: CCSD(T) improves by 0.5-1 MeV over CCSD
- Nuclear matter equation of state reliable for neutron star applications

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| OPE potential | $V_\pi \propto g_A^2\sigma_1\cdot\mathbf{q}\sigma_2\cdot\mathbf{q}/(q^2+m_\pi^2)$ | Sec. 2 |
| Chiral expansion | $V_{NN} = V_\pi^{(0)} + V_\pi^{(2)} + V_C^{(0)} + \ldots$ | NNLO |
| CC wave function | $\|\Psi_{\rm CC}\rangle = e^T\|\Phi_0\rangle$ | Coupled-cluster |
| Saturation constraint | $\chi^2 = \chi^2_{NN} + \chi^2_{BE} + \chi^2_{radii} + w_{\rm sat}(\rho_0^{\rm calc}-\rho_0^{\rm exp})^2$ | Optimization |
| Charge radius | $\langle r^2\rangle = (1/Z)\int r^2\rho_{\rm charge}d\mathbf{r}$ | Observable |

**Dependencies**: Ab initio alternative to DFT approach in 12. Provides nuclear force context for 06.

---

### Paper 05: Spontaneous Fission Modes and Lifetimes of Superheavy Elements
- **File**: `05_2013_Staszczak_Spontaneous_Fission_Superheavy.md`
- **Year**: 2013
- **Authors**: Staszczak, Baran, Nazarewicz
- **Relevance**: MEDIUM
- **Tags**: superheavy, fission, octupole, WKB-tunneling, island-of-stability, GCM

**Summary**: Calculates competing decay modes of superheavy nuclei (Z=108-126) using DFT+GCM. Key finding: reflection-asymmetric (octupole) fission paths lower barriers by 0.5-2 MeV, reducing predicted lifetimes by up to 10^7. Redefines the island of stability as centered on ^294Ds rather than ^298Fl.

**Key Results**:
- Octupole deformations lower fission barriers by 0.5-2 MeV (10^3-10^7 lifetime reduction)
- Island of stability centered on ^294Ds (Z=110), half-life ~1.5 days
- For Z>110, alpha decay/beta decay/spontaneous fission all compete
- Triaxial configurations appear as ground states in some superheavy nuclei
- GCM configuration mixing enhances tunneling rates vs. pure mean-field

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| PES | $E(\beta) = E_{\rm LDM}(\beta) + E_{\rm shell}(\beta)$ | Sec. 2 |
| WKB tunneling | $T_{1/2}^{SF} \propto \exp(-2\int\sqrt{2m_{\rm eff}(V-E)}dx/\hbar)$ | Sec. 3 |
| GCM overlap | $G(\beta,\beta') = \langle\Psi[\beta]\|\Psi[\beta']\rangle$ | Sec. 2 |
| Octupole energy | $E_{\rm oct} \propto (\int r^3 Y_3^0 \rho d\mathbf{r})^2$ | Sec. 3 |

**Dependencies**: Uses GCM from 13. Connects to octupole physics in 09. Application of DFT from 12.

---

### Paper 06: Uncertainty Quantification for Nuclear Density Functional Theory
- **File**: `06_2015_McDonnell_Uncertainty_Quantification_DFT.md`
- **Year**: 2015
- **Authors**: McDonnell, Schunck, Higdon, Sarich, Wild, Nazarewicz
- **Relevance**: CRITICAL (methodology)
- **Tags**: Bayesian-inference, uncertainty-quantification, Gaussian-process, Bayes-factor, KL-divergence, Skyrme

**Summary**: Applies Bayesian inference with Gaussian process emulators to quantify how new mass measurements constrain nuclear DFT parameters. Introduces KL divergence and Bayes factors for assessing information content of experiments. Finds that individual Penning trap measurements (10 keV precision) don't strongly constrain Skyrme parameters, revealing a ~0.5 MeV theoretical error floor in nuclear DFT.

**Key Results**:
- Canadian Penning Trap data: BF ~ 1.2 (weak evidence), doesn't sharply constrain Skyrme
- Different observables constrain different parameter combinations (radii -> symmetry energy, gaps -> effective mass)
- Drip-line predictions uncertain by +/-2 nucleons despite improved mass data
- Theoretical error floor: sigma_th ~ 0.5 MeV for typical Skyrme functional
- No single parametrization unambiguously preferred — only joint observables sharpen posterior

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Bayes theorem | $p(\theta\|\mathcal{D}) = p(\mathcal{D}\|\theta)p(\theta)/p(\mathcal{D})$ | Core |
| Likelihood | $p(M^{\rm exp}\|\theta) \propto \exp(-(M^{\rm th}-M^{\rm exp})^2/2(\sigma_{\rm exp}^2+\sigma_{\rm th}^2))$ | Sec. 2 |
| GP posterior mean | $\mu(\theta^*) = \mathbf{k}^T(\mathbf{K}+\epsilon^2 I)^{-1}\mathbf{M}$ | Sec. 3 |
| KL divergence | $D_{\rm KL} = \int p_{\rm new}\log(p_{\rm new}/p_{\rm old})d\theta$ | Sec. 4 |
| Bayes factor | $BF = p(\mathcal{D}_{\rm new}\|M_1)/p(\mathcal{D}_{\rm new}\|M_0)$ | Sec. 4 |

**Dependencies**: Methodology applicable to all DFT papers (12, 04). Directly informs framework probability assessment.

---

### Paper 07: Single-Particle Energies in Axially Deformed Woods-Saxon Potential
- **File**: `07_1987_Cwiok_Woods_Saxon_Deformed_Nuclei.md`
- **Year**: 1987
- **Authors**: Cwiok, Dobaczewski, Heeger, Magierski, Nazarewicz
- **Relevance**: HIGH
- **Tags**: Woods-Saxon, deformed-potential, spin-orbit, single-particle, quadrupole-moment, g-factor

**Summary**: Comprehensive tabulation of single-particle energies, wave functions, quadrupole moments, and g-factors for the axially deformed Woods-Saxon potential. Covers prolate and oblate geometries from near-spherical to extreme elongation approaching scission. The foundational computational reference for deformed shell-model calculations.

**Key Results**:
- Shell closures at N/Z = 8, 20, 50, 82, 126 reproduced with Woods-Saxon + spin-orbit
- Level ordering changes dramatically with deformation: intruder orbitals cross at beta_2 ~ 0.4-0.6
- Quadrupole moments range from ~0 (magic) to ~10 b (well-deformed)
- g-factors within a few percent of experiment when configuration mixing included
- Stable computation extends to extreme elongations (beta_2 > 1.0)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| WS potential | $U_{\rm WS}(r) = -V_0/(1+\exp[(r-R_0)/a])$ | Sec. 2 |
| Deformed radius | $R(\theta) = R_0[1+\beta_2 P_2(\cos\theta)+\beta_4 P_4(\cos\theta)]$ | Sec. 2 |
| Spin-orbit | $V_{\rm SO}\mathbf{L}\cdot\mathbf{S}$ with $V_{\rm SO}\approx\lambda(1/r)(dU/dr)$ | Sec. 3 |
| Quadrupole moment | $Q_0 = e\langle r^2 P_2(\cos\theta)\rangle$ | Sec. 4 |
| g-factor | $g_j = g_\ell\langle\mathbf{L}\cdot\mathbf{J}\rangle/J(J+1) + g_s\langle\mathbf{S}\cdot\mathbf{J}\rangle/J(J+1)$ | Sec. 5 |

**Dependencies**: Foundational for 01 (shell evolution), 08 (high-spin), 09 (octupole). Pre-DFT era reference.

---

### Paper 08: Microscopic Study of High-Spin Behaviour in A~80 Nuclei
- **File**: `08_1985_Nazarewicz_High_Spin_A80_Nuclei.md`
- **Year**: 1985
- **Authors**: Nazarewicz, Dobaczewski, Carlsson, Magnusson, Bengtsson, Cederwall
- **Relevance**: CRITICAL
- **Tags**: cranking, high-spin, backbending, pairing-collapse, shape-transition, superdeformation

**Summary**: Analyzes collective and non-collective high-spin configurations in A~80 nuclei using the cranking model with a deformed Woods-Saxon potential. Demonstrates the competition between collective rotation, single-particle alignment (backbending), and pairing correlations that weaken with increasing angular momentum. Predicts shape transitions and superdeformation at extreme spin.

**Key Results**:
- Collective moments of inertia reproduced within 10-20%
- Backbending from high-j neutron alignment (1h_{11/2}, 1g_{9/2}) predicted correctly
- Pairing collapse at predictable frequency matches experiment
- Shape staggering (prolate -> prolate+oblate) near I=20 in N=46 isotopes
- Superdeformed bands predicted for extreme elongation (beta_2 ~ 0.8-1.0)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Cranking Hamiltonian | $H_{\rm rot} = H_0 - \omega J_x$ | Sec. 2 |
| Moment of inertia | $\mathcal{I} = dJ/d\omega$ | Sec. 2 |
| Pairing gap vs. spin | $\Delta(\omega) = \Delta_0\sqrt{1-(\omega/\omega_c)^2}$ | Sec. 3 |
| Shell correction | $E_{\rm shell} = \sum_i\epsilon_i - \int_0^{\epsilon_F}g(\epsilon)\epsilon d\epsilon$ | Sec. 4 |
| Rotational energy | $E_{\rm rot} = \hbar^2 I(I+1)/(2\mathcal{I})$ | Sec. 2 |

**Dependencies**: Uses 07 (Woods-Saxon basis). Pairing formalism from 02/03. Directly relevant to framework's treatment of pairing collapse as phonon damping.

---

### Paper 09: Intrinsic Reflection Asymmetry in Atomic Nuclei
- **File**: `09_1996_Butler_Intrinsic_Reflection_Asymmetry.md`
- **Year**: 1996
- **Authors**: Butler, Nazarewicz
- **Journal**: Reviews of Modern Physics
- **Relevance**: HIGH
- **Tags**: octupole, parity-breaking, E1-transitions, parity-doublets, actinides, mean-field

**Summary**: Comprehensive review of experimental and theoretical evidence for pear-shaped (octupole-deformed) nuclei that spontaneously break spatial inversion symmetry. Covers mean-field theory of octupole instability, parity-doublet spectroscopy, E1/E3 transition strengths, and identifies the actinide region (Z~88-94, N~134-140) as the primary zone of octupole deformation.

**Key Results**:
- Octupole deformation confirmed in Ra-223, Ra-225, Ac-225, Ra-226, Th-229 and actinides
- E1 transition strengths 100-1000x larger than single-particle estimates (smoking gun)
- Parity mixing 1-10% measured via electron scattering and muonic atoms
- Octupole instability condition: d^2E/d(beta_3)^2 < 0 at beta_3=0
- Actinide region (Z~88-94, N~134-140) shows strongest systematic octupole effects

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Octupole radius | $R(\theta) = R_0[1+\beta_2 P_2+\beta_3 P_3]$ | Sec. 2 |
| Instability condition | $\partial^2 E/\partial\beta_3^2\|_{\beta_3=0} < 0$ | Sec. 3 |
| E1 strength | $B(E1; I\to I') = (e^2/4\pi(2I+1))\|\langle I'\|D\|I\rangle\|^2$ | Sec. 4 |
| Octupole moment | $Q_3 = \int(r^3/2)P_3(\cos\theta)\rho d\mathbf{r}$ | Sec. 4 |
| Dipole from deformation | $D_0 \sim Z\langle r^3\rangle\beta_3$ | Sec. 2 |

**Dependencies**: Octupole physics feeds into 05 (fission barriers). Builds on 07 (deformed shell model).

---

### Paper 10: Shape Coexistence and Triaxiality in Superheavy Nuclei
- **File**: `10_2005_Caurier_Shape_Coexistence_Superheavy.md`
- **Year**: 2005
- **Authors**: Caurier, Sieja, Nazarewicz
- **Journal**: Nature
- **Relevance**: HIGH
- **Tags**: shape-coexistence, triaxiality, superheavy, GCM, prolate-oblate, shell-closure

**Summary**: Reveals unexpected abundance of competing shapes (spherical, prolate, oblate, triaxial) coexisting at low excitation energy in superheavy nuclei near Z=114. Uses Gogny-D1S DFT + GCM to show that the flat potential energy landscape in superheavy nuclei produces shape isomerism as a natural consequence of the Coulomb-nuclear force balance.

**Key Results**:
- Superheavy nuclei exhibit prolate, oblate, triaxial, and spherical states within 0.5-2 MeV
- Prolate ground states dominate despite enormous Coulomb repulsion (shell effect)
- Triaxiality (gamma ~ 20-30 deg) appears as lowest configuration near Z=114, N=184
- Z=114 shell closure competes with prolate deformed closure (shape coexistence source)
- Different shapes have different decay properties (multipath decay signatures)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| PES | $E(\beta_2,\gamma) = E_{\rm HFB} + E_{\rm rot}$ | Sec. 2 |
| Triaxiality | $\gamma = \arctan[\sqrt{3}(b^2-a^2)/(2c^2-a^2-b^2)]$ | Sec. 3 |
| Coulomb energy | $E_C \approx (3/5)(e^2 Z^2/R_0)[1+0.03\beta_2^2]$ | Sec. 2 |
| GCM equation | $\int d\mathbf{q}' G(\mathbf{q},\mathbf{q}')[E-H(\mathbf{q}')]f(\mathbf{q}')=0$ | Sec. 3 |

**Dependencies**: Uses GCM from 13. Builds on deformation physics from 07, 09. Feeds into 05 (fission).

---

### Paper 11: Impact of Nuclear Mass Uncertainties on the r-Process
- **File**: `11_2012_Marketin_r_Process_Rates.md`
- **Year**: 2012
- **Authors**: Marketin, Huther, Martinez-Pinedo, Nazarewicz, Zufiria
- **Relevance**: MEDIUM
- **Tags**: r-process, nucleosynthesis, mass-uncertainty, FRIB, neutron-capture, beta-decay

**Summary**: Quantifies how nuclear mass uncertainties propagate through r-process abundance calculations. Mass errors of 50-100 keV cause 5-50% abundance variations depending on location in the network. Identifies critical "bottleneck" nuclei near N=50, 82 where precision measurements would most improve r-process predictions. Establishes FRIB measurement priorities.

**Key Results**:
- 50-100 keV mass precision needed for 5% r-process abundance accuracy
- Bottleneck nuclei: ^80Zn, ^82Ge near N=50 critically affect abundance pattern
- 100 keV mass shift redirects 20-50% of network flow at branching points
- FRIB should prioritize Z=30-50, N=50-82 mass measurements
- Current mass tables (UNEDF) sufficient for rough predictions but inadequate for precision

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Separation energy | $S_n(A,Z) = M(A-1,Z)+m_n-M(A,Z)$ | Core |
| Rate sensitivity | $\Delta\sigma/\sigma \approx \Delta M/k_BT$ | Sec. 3 |
| Beta-decay rate | $\lambda_\beta = \ln 2/t_{1/2}$ | Sec. 2 |
| Capture rate | $\lambda_{n,\gamma} = \sigma_{n,\gamma}n_n\langle v\rangle$ | Sec. 2 |

**Dependencies**: Uses mass predictions from 12 (UNEDF). Astrophysical context for 14 (synthesis review).

---

### Paper 12: Large-Scale Mass Table Calculations: UNEDF Project
- **File**: `12_2012_Erler_UNEDF_Large_Scale_Mass_Table.md`
- **Year**: 2012
- **Authors**: Erler, Birge, Kortelainen, Nazarewicz, Olsen, Sexton, Stoitsov, Xu
- **Journal**: Nature
- **Relevance**: HIGH
- **Tags**: UNEDF, mass-table, Skyrme, HFB, 9400-nuclei, drip-line, petascale

**Summary**: Landmark computational effort calculating masses for ~9400 nuclei across the entire nuclear chart using state-of-the-art Skyrme DFT on leadership-class supercomputers. Achieves ~600 keV rms deviation from experiment. Establishes DFT as a predictive tool for comprehensive nuclear structure mapping and identifies systematic deficiencies in current parametrizations.

**Key Results**:
- 9400 nuclei computed from Z=1 to Z=120, proton to neutron drip line
- Global rms deviation ~600 keV (near-stability: 200-300 keV)
- Ground-state deformations correctly predicted (prolate/oblate identification)
- Magic numbers and shell closures reproduced including exotic closures
- Two-neutron drip line within 2 nucleons in most regions
- Beta-decay Q-values accurate to ~200 keV

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Skyrme energy | $E = \int d\mathbf{r}\,\epsilon(\rho,\tau,s,\ldots)$ | Sec. 2 |
| Pairing interaction | $V_{\rm pair} = -G(1-\eta\rho)\delta(\mathbf{r}-\mathbf{r}')$ | Sec. 3 |
| Self-consistency | $\rho_{ij} = \sum_k v_{ik}^* v_{jk}$ | HFB |
| Mass excess | $\Delta M = [M(A,Z)-M_u]c^2$ | Observable |

**Dependencies**: Uses HFB formalism from 02/03. Mass predictions consumed by 11 (r-process). UQ methodology from 06.

---

### Paper 13: Generator Coordinate Method: Beyond Mean-Field Approaches
- **File**: `13_2010_Rodriguez_Generator_Coordinate_Method_Beyond_Mean_Field.md`
- **Year**: 2010
- **Authors**: Rodriguez, Nazarewicz
- **Relevance**: HIGH
- **Tags**: GCM, configuration-mixing, symmetry-restoration, collective-motion, fission, shape-isomerism

**Summary**: Reviews the GCM as the standard beyond-mean-field method for nuclear structure. Treats constrained mean-field solutions as a non-orthogonal basis, then variationally determines optimal mixing weights. Key applications: collective motion, shape isomerism, fission tunneling, symmetry restoration (angular momentum projection). Provides the mathematical framework used in 05 and 10.

**Key Results**:
- GCM naturally describes coexisting shapes with excitation energies and lifetimes
- Fission lifetime predictions improve 2-10x over static barrier approximation
- Effective moments of inertia: I ~ 0.3-0.5 I_rigid for prolate nuclei
- Configuration mixing lowers ground state by 0.5-1 MeV
- Superheavy shape isomers predicted with testable lifetimes

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| GCM state | $\|\Psi_\alpha\rangle = \sum_i f_\alpha(q_i)\|\Psi(q_i)\rangle$ | Sec. 2 |
| GCM eigenvalue | $\sum_j(H_{ij}-E_\alpha G_{ij})f_\alpha(q_j)=0$ | Core |
| Overlap kernel | $G_{ij} = \langle\Psi(q_i)\|\Psi(q_j)\rangle$ | Metric |
| Slater overlap | $G = \det(\langle\phi_k(q_i)\|\phi_l(q_j)\rangle)$ | Sec. 3 |
| Transition probability | $B(E\lambda) = \|\langle I'\|O_\lambda\|I\rangle\|^2/(2I+1)$ | Sec. 4 |

**Dependencies**: Used by 05 (fission), 10 (shape coexistence). Pfaffian overlap connects to framework's D_K Pfaffian computations.

---

### Paper 14: Nuclear Structure at the Limits
- **File**: `14_2009_Nazarewicz_Structure_at_the_Limits.md`
- **Year**: 2009
- **Authors**: Nazarewicz
- **Journal**: Nuclear Physics News
- **Relevance**: HIGH
- **Tags**: synthesis, halos, drip-line, r-process, superheavy, exotic-nuclei, FRIB

**Summary**: Comprehensive overview synthesizing the state of nuclear structure physics across the nuclear landscape. Covers shell evolution, halo nuclei, shape coexistence, pairing persistence at drip line, superheavy fission, and r-process nucleosynthesis. Best entry point for the entire collection.

**Key Results**:
- Universal phenomena: halos, shape isomerism, pairing persist from light to superheavy
- New magic numbers at N=14, 28 (exotic); traditional N=50, 126 persist in some regions
- HFB with density-dependent interactions predicts drip-line properties to 5-10%
- r-Process models with DFT inputs reproduce solar abundances
- FRIB priorities: isomeric states, beta-decay half-lives, masses to drip line

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Tensor shell shift | $\Delta\epsilon = \langle i\|V_T^{(1)}\|i\rangle\rho^{\rm opp}$ | Sec. 2 |
| Halo radius | $r_{\rm halo} \sim \hbar/\sqrt{2m\|E_{\rm sep}\|}$ | Sec. 3 |
| Pairing gap (contact) | $\Delta \approx 2\Delta_0\sqrt{\pi N(E_F)}\exp(-2/(GN(E_F)))$ | Sec. 4 |
| Alpha Q-value | $Q_\alpha = M(A,Z)-M(A-4,Z-2)-M(^4{\rm He})c^2$ | Sec. 5 |

**Dependencies**: Synthesis of all other papers. Best entry point for the collection.

---

## Cross-Paper Equation Concordance

| Equation | Papers | Context |
|:---|:---|:---|
| HFB eigenvalue equation | 02, 03, 12 | Core self-consistent pairing formalism |
| Bogoliubov transformation | 03 | Quasiparticle definition |
| Density-dependent pairing $\Delta = -G(1-\eta\rho)\kappa$ | 02, 03, 12 | Standard pairing functional |
| Woods-Saxon potential | 07, 08 | Mean-field basis potential |
| Deformed radius $R(\theta) = R_0[1+\beta_\lambda P_\lambda]$ | 07, 09, 10 | Multipole shape parametrization |
| GCM eigenvalue equation | 05, 10, 13 | Beyond-mean-field configuration mixing |
| WKB tunneling integral | 05 | Fission lifetime calculation |
| Bayes theorem + GP emulator | 06 | Uncertainty quantification |
| Shell correction energy | 08 | Strutinsky method |
| Cranking Hamiltonian $H-\omega J_x$ | 08 | Rotating frame formalism |

---

## Notation Conventions

| Symbol | Meaning | Papers |
|:---|:---|:---|
| $\beta_2, \beta_3, \beta_4$ | Quadrupole, octupole, hexadecapole deformation | 07-10, 13 |
| $\gamma$ | Triaxiality parameter (0=prolate, 60=oblate) | 10 |
| $u_k, v_k$ | Bogoliubov amplitudes (occupation/vacancy) | 02, 03 |
| $\Delta$ | Pairing gap or pairing field | 02, 03, 08 |
| $\kappa$ | Pair amplitude (off-diagonal density) | 02, 03 |
| $\rho$ | Nucleon density | All |
| $\mathcal{I}$ | Moment of inertia | 08, 13 |
| $S_n$ | Neutron separation energy | 02, 11, 14 |
| $G$ | Pairing strength (coupling constant) | 02, 03, 09 |
| $E_F, \lambda$ | Fermi energy / chemical potential | 02, 03 |
| $\sigma_{\rm th}$ | Theoretical uncertainty | 06 |

---

## Computational Verification Status

| Paper | Computation in this project | Session | Status |
|:---|:---|:---|:---|
| 02, 03 | BCS gap equation on SU(3) Dirac spectrum | 23a | K-1e CLOSED (M_max=0.077-0.149, 7-13x below threshold) |
| 02, 03 | Kosmann-BCS condensate at mu=0 | 23a | CLOSED (spectral gap prevents BCS) |
| 06 | Bayesian probability assessment methodology | 22d, 24b | Applied (BF=0.31 post-V-1) |
| 03 | BdG classification of D_K spectrum | 17c | AZ class BDI, T^2=+1 |
| 07 | Single-particle spectrum analog (D_K eigenvalues) | 12, 20a | Computed, phi found at s=1.14 |

---

**Index built**: 2026-03-02
**Method**: Solo librarian (direct read, no team)
**Agent**: nazarewicz-nuclear-structure-theorist
