# Landau Paper Index

**Researcher**: Lev Davidovich Landau (and related condensed matter / integrable pairing / superfluid cosmology authors)
**Papers**: 40 (1927-2024)
**Primary domain**: Phase transitions, superfluidity, Fermi liquids, BCS pairing, Richardson-Gaudin integrability, Kibble-Zurek, GGE, BCS-BEC crossover, superfluid vacuum, spectral geometry
**Project relevance**: Core condensed matter for phonon-exflation framework. BCS on SU(3) fiber, RG integrability, GGE permanence, KZ transit, VHS/Pomeranchuk, GPV, emergent spacetime.

---

## Dependency Graph

```
QUANTUM & STATISTICAL FOUNDATIONS (1927-1935)
  01 (Density Matrix) --> 04 (Phase Transitions)  [statistical --> thermodynamic]
  02 (Landau Levels) --> 13 (Abrikosov Vortices)  [Landau levels --> H_c2 derivation]
  03 (Domain Walls) --> 04 (Phase Transitions)     [order parameter dynamics --> general theory]

PHASE TRANSITIONS & SUPERFLUIDITY (1937-1947)
  04 (Phase Transitions) --> 05 (Superfluidity I)  [Landau free energy --> two-fluid model]
  04 --> 08 (GL Superconductivity)                  [F(eta) --> F[psi,A]]
  04 --> 09 (TDGL)                                  [static --> dynamic]
  05 (Superfluidity I) --> 06 (Landau Damping)     [quasiparticle gas --> kinetic theory]
  05 --> 07 (Superfluidity II)                      [revised roton parameters]
  05 --> 11 (Fermi Liquid)                          [quasiparticle concept generalized]

GL, FERMI LIQUID & QFT (1950-1958)
  08 (GL) --> 13 (Abrikosov Vortices)              [GL eqs --> vortex lattice solution]
  08 --> 09 (TDGL)                                  [static GL --> dynamic GL]
  08 --> 15 (BCS)                                   [phenomenological --> microscopic via Gor'kov]
  10 (LAK Running Coupling) --> 14 (Vertex Parts)  [leading-log --> general analyticity]
  11 (Fermi Liquid) --> 12 (Zero Sound)            [Landau parameters --> collective mode]
  11 --> 15 (BCS)                                   [quasiparticles --> pairing instability]

BCS & INTEGRABLE PAIRING (1957-2004)
  15 (BCS) --> 16 (Richardson Exact)               [mean-field --> exact solution]
  15 --> 25 (BCS-BEC Crossover)                    [weak-coupling --> full crossover]
  16 (Richardson) --> 17 (DPS Review)              [single paper --> full review of RG models]
  16 --> 24 (Claeys Broken Integ.)                 [exact --> broken integrability]
  17 (DPS Review) --> 24 (Claeys)                  [RG models --> variational + Floquet]

SUPERFLUID VACUUM & COSMOLOGY (2001-2020)
  05 (Superfluidity I) --> 18 (Volovik Analogies)  [He-4 --> cosmological analogies]
  11 (Fermi Liquid) --> 18 (Volovik Analogies)     [Fermi liquid --> vacuum universality classes]
  18 (Volovik Analogies) --> 19 (Helium Droplet)   [paper --> monograph]
  18 --> 20 (Berezhiani-Khoury DM)                 [superfluid vacuum --> DM superfluidity]
  18 --> 21 (Zloshchastiev SVT)                    [acoustic metric --> emergent gravity from GPE]

GGE & INTEGRABILITY (2006-2018)
  16 (Richardson) --> 22 (Rigol GGE)               [integrals of motion --> GGE construction]
  22 (Rigol GGE) --> 23 (Vidmar-Rigol Review)      [founding paper --> comprehensive review]
  17 (DPS Review) --> 24 (Claeys)                  [RG integrability --> breaking thereof]

BCS-BEC CROSSOVER & KZ (2018-2024)
  15 (BCS) --> 25 (Strinati BCS-BEC)              [BCS --> full crossover phenomenology]
  08 (GL) --> 29 (Zurek KZ)                        [GL free energy --> KZ defect production]
  09 (TDGL) --> 29 (Zurek KZ)                      [critical slowing --> freeze-out]
  25 --> 26 (Ko KZ-BCS-BEC)                        [crossover + KZ experiment]
  25 --> 27 (Nakagawa Gate BCS-BEC)                [crossover in 2D solid-state]
  25 --> 28 (Lanaro Finite-Size)                   [crossover + finite-size effects]
  29 --> 30 (Enomoto WKB-LZ)                       [KZ/LZ --> cosmological particle production]

GPV & NUCLEAR STRUCTURE (2015-2024)
  15 (BCS) --> 31 (Cappuzzello GPV 14C)            [BCS pairing --> giant pair vibration]
  31 --> 32 (Fortunato GPV Heavy)                  [light nuclei --> heavy nuclei searches]
  31 --> 33 (GPV Fragmentation)                    [bare GPV --> dressed by particle-vibration]
  15 --> 34 (Takahashi Higgs Nuclear)              [BCS gap --> Higgs mode in nuclei]
  15 --> 35 (Nesterenko Cranking)                  [pairing --> moments of inertia]
  15 --> 36 (Lei Shape Coexistence)                [pair condensate --> shape coexistence]

VHS, POMERANCHUK & SPECTRAL GEOMETRY (2024)
  11 (Fermi Liquid) --> 37 (Beidenkopf Pomeranchuk) [Pomeranchuk instability --> kagome expt]
  37 --> 38 (Classen VHS Review)                    [HOvHS --> systematic classification]
  11 --> 39 (Xing NFL-VHS)                          [Fermi liquid breakdown --> NFL from VHS]
  02 (Landau Levels) --> 40 (Zeng Dirac Spectrum)  [quantization --> spectral bounds]

CROSS-THEME LINKS
  04,08,09    --[order parameter dynamics]--> 29 (KZ)  [static + dynamic GL --> quench]
  11,37,38,39 --[Fermi surface instabilities]--> 15 (BCS) [Pomeranchuk/VHS --> pairing]
  16,17,22,23 --[integrability]--> 24 (broken integrability)
  15,25,26,27 --[BCS-BEC]--> 28 (finite-size) [bulk --> finite system]
  18,19,21    --[superfluid vacuum]--> 04 (phase transitions) [emergent SM as SSB]
```

## Topic Map

### Quantum & Statistical Foundations
Papers: 01, 02, 03
Density matrix (01), Landau quantization/diamagnetism (02), and domain wall dynamics (03). Paper 01 introduces the statistical operator and partial trace -- foundational for the GGE (Paper 22) and decoherence in the framework. Paper 02 introduces Landau levels, whose KK analog is the Dirac spectrum on SU(3). Paper 03 establishes the Landau-Lifshitz equation and domain wall solitons as topological defects classified by homotopy groups.

### Phase Transitions & Superfluidity
Papers: 04, 05, 06, 07
The conceptual core. Paper 04 introduces the order parameter, symmetry breaking, and free energy expansion -- the language of the entire framework (Jensen parameter tau as order parameter, V_eff(tau) as Landau free energy). Paper 05 establishes the two-fluid model and phonon-roton spectrum -- the physical prototype for phonon-exflation. Paper 06 introduces Landau damping (collisionless energy transfer) and the Landau contour. Paper 07 refines roton parameters to 3-sigma agreement with later neutron scattering.

### Ginzburg-Landau, Fermi Liquid & QFT
Papers: 08, 09, 10, 11, 12, 13, 14
Paper 08 (GL theory) provides the most direct mathematical bridge: GL functional = GPE energy functional, kappa = lambda/xi classifies Type I/II, Higgs mechanism = Meissner effect. Paper 09 introduces the TDGL/LK equation governing critical slowing down. Paper 10 derives the running coupling and Landau pole. Paper 11 introduces Fermi liquid theory, quasiparticles, Landau parameters, and Pomeranchuk stability -- the framework for particles as quasiparticles of the vacuum. Paper 12 derives zero sound. Paper 13 solves the Abrikosov vortex lattice. Paper 14 derives the Landau equations for Feynman diagram singularities.

### BCS & Integrable Pairing
Papers: 15, 16, 17
The microscopic pairing backbone. Paper 15 (BCS) provides the gap equation, ground state, and quasiparticle spectrum. Paper 16 (Richardson) shows the pairing Hamiltonian is exactly solvable -- the foundation for the framework's GGE permanence result. Paper 17 (Dukelsky-Pittel-Sierra) is the comprehensive review of Richardson-Gaudin models, electrostatic mapping, and conserved integrals -- the direct source for Sessions 33-38.

### Superfluid Vacuum & Cosmology
Papers: 18, 19, 20, 21
Volovik's program of emergent spacetime from condensed matter. Paper 18 classifies fermionic vacua by momentum-space topology and derives the acoustic metric and CC=0 result. Paper 19 (monograph) extends to Weyl fermions, gauge fields, and gravity from He-3. Paper 20 applies superfluidity to dark matter (MOND+CDM unification). Paper 21 derives a seven-term gravitational potential from a logarithmic GPE, producing FLRW cosmology and galactic rotation curves from a single condensate wavefunction.

### GGE & Integrability
Papers: 22, 23, 24
The theoretical infrastructure for the framework's permanent non-thermal relic. Paper 22 (Rigol et al.) founds the GGE -- maximizing entropy subject to all conserved quantities. Paper 23 (Vidmar-Rigol) reviews GGE in lattice models, proving generalized eigenstate thermalization. Paper 24 (Claeys thesis) develops Richardson-Gaudin models with broken integrability, eigenvalue-based numerics, and Floquet dynamics.

### BCS-BEC Crossover & Kibble-Zurek
Papers: 25, 26, 27, 28, 29, 30
The dynamical framework for the transit. Paper 25 is the comprehensive BCS-BEC crossover review (cold atoms to nuclear matter). Paper 26 observes KZ universality across the BCS-BEC crossover. Paper 27 demonstrates gate-controlled BCS-BEC crossover in 2D. Paper 28 analyzes finite-size effects. Paper 29 (Zurek) establishes the KZ freeze-out mechanism -- the direct analog of the framework's transit dynamics. Paper 30 connects the Landau-Zener transition to cosmological particle production via exact WKB.

### GPV & Nuclear Structure
Papers: 31, 32, 33, 34, 35, 36
Nuclear BCS phenomenology relevant to the framework's pair vibration results. Paper 31 reports the first GPV observation in 14C. Paper 32 reviews GPV searches in heavy nuclei. Paper 33 treats GPV fragmentation by particle-vibration coupling. Paper 34 introduces the Higgs response function for nuclear pair condensates. Paper 35 computes cranking moments of inertia showing pairing collapse effects in 24Mg. Paper 36 surveys shape coexistence in pair condensates.

### VHS, Pomeranchuk & Spectral Geometry
Papers: 37, 38, 39, 40
Modern Fermi surface physics connecting to the framework's Van Hove singularity and Pomeranchuk results. Paper 37 observes distortion-induced HOvHS driving Pomeranchuk instability in kagome Co3Sn2S2. Paper 38 systematically classifies HOvHS and their connection to flat bands. Paper 39 derives NFL and MFL signatures from VHS. Paper 40 establishes eigenvalue bounds for the Dirac operator on compact Riemannian manifolds -- directly applicable to D_K on SU(3).

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Order parameter, symmetry breaking, Landau free energy | 04, 08 | CRITICAL |
| BCS pairing on SU(3), gap equation | 15, 16, 17 | CRITICAL |
| GGE permanence, integrability, conserved quantities | 16, 17, 22, 23, 24 | CRITICAL |
| Kibble-Zurek transit, defect production | 29, 09, 26 | CRITICAL |
| Phonon-roton spectrum, quasiparticle concept | 05, 07, 11 | CRITICAL |
| Pomeranchuk stability, Fermi surface instabilities | 11, 37, 38 | HIGH |
| Van Hove singularity, DOS divergence | 37, 38, 39 | HIGH |
| Superfluid vacuum, emergent spacetime | 18, 19, 21 | HIGH |
| BCS-BEC crossover physics | 25, 26, 27, 28 | HIGH |
| Running coupling, Landau pole, QFT analyticity | 10, 14 | HIGH |
| GPV, nuclear pair vibrations | 31, 32, 33, 34 | HIGH |
| GL theory, vortices, Type I/II | 08, 13, 29 | HIGH |
| Density matrix, open systems, decoherence | 01 | MEDIUM |
| Landau levels, dHvA, topological classification | 02, 40 | MEDIUM |
| Critical slowing, dynamic universality | 09 | MEDIUM |
| Nuclear cranking, shape coexistence | 35, 36 | MEDIUM |
| Landau-Zener, WKB particle production | 30 | MEDIUM |
| DM superfluidity, MOND | 20 | MEDIUM |

---

## Paper Entries

### Paper 01: Das Dampfungsproblem in der Wellenmechanik (Density Matrix)
- **File**: `01_Landau_1927_Density_Matrix.md`
- **arXiv**: N/A
- **Year**: 1927
- **Relevance**: MEDIUM
- **Tags**: density matrix, open systems, decoherence, von Neumann entropy, partial trace

**Summary**: At age 19, Landau independently introduces the density operator rho = sum_i p_i |psi_i><psi_i| for mixed quantum states, solving the "damping problem" of how irreversibility arises from unitary dynamics via tracing over environmental degrees of freedom. Establishes the trace formalism, purity criterion Tr(rho^2), and von Neumann entropy S = -Tr(rho ln rho).

**Key Results**:
- Density matrix as fundamental quantum object (simultaneously with von Neumann)
- Partial trace and reduced density matrices for open systems
- Von Neumann equation: i hbar d(rho)/dt = [H, rho]
- Purity criterion: Tr(rho^2) = 1 iff pure state
- Decoherence from system-environment entanglement

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 1.1 | Density operator | rho = sum_i p_i \|psi_i><psi_i\|, Section 3.2 |
| eq 1.2 | Expectation value | <A> = Tr(rho A), Section 4.1 |
| eq 1.3 | Von Neumann entropy | S = -Tr(rho ln rho), Section 4.3 |
| eq 1.4 | Thermal density matrix | rho = exp(-beta H)/Z, Section 6.1 |

**Dependencies**: Upstream of 04 (thermal free energy requires statistical operator), 22 (GGE density matrix)

---

### Paper 02: Diamagnetismus der Metalle (Landau Levels)
- **File**: `02_Landau_1930_Diamagnetism.md`
- **arXiv**: N/A
- **Year**: 1930
- **Relevance**: MEDIUM
- **Tags**: Landau levels, diamagnetism, de Haas-van Alphen, quantum Hall, Fermi surface

**Summary**: Resolves the Bohr-van Leeuwen paradox by quantizing orbital electron motion in a magnetic field into discrete Landau levels E(n,k_z) = hbar omega_c (n+1/2) + hbar^2 k_z^2/(2m). Derives the diamagnetic susceptibility chi_L = -chi_Pauli/3. Predicts de Haas-van Alphen oscillations for Fermi surface mapping.

**Key Results**:
- Landau level spectrum: E_n = hbar omega_c (n+1/2), degeneracy = eB/(2 pi hbar c)
- chi_L = -mu_B^2 N(E_F)/3 = -chi_Pauli/3
- dHvA period: Delta(1/B) = 2 pi e/(hbar c A_ext)
- Magnetic length: l_B = sqrt(hbar c/(eB))
- Foundation for quantum Hall effect and topological classification

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 2.1 | Landau level energy | E(n,k_z) = hbar omega_c(n+1/2) + hbar^2 k_z^2/(2m), Section 2.3 |
| eq 2.2 | Cyclotron frequency | omega_c = eB/(mc), Section 2.2 |
| eq 2.3 | Diamagnetic susceptibility | chi_L = -mu_B^2 N(E_F)/3, Section 3.3 |
| eq 2.4 | dHvA oscillation period | Delta(1/B) = 2pi e/(hbar c A_ext), Section 4.1 |

**Dependencies**: Upstream of 13 (H_c2 from Landau levels in GL), 40 (Dirac spectral bounds)

---

### Paper 03: Domain Walls (Landau-Lifshitz Equation)
- **File**: `03_Landau_Lifshitz_1935_Domain_Walls.md`
- **arXiv**: N/A
- **Year**: 1935
- **Relevance**: MEDIUM
- **Tags**: Landau-Lifshitz equation, domain walls, topological defects, magnetization dynamics, solitons

**Summary**: Introduces the Landau-Lifshitz equation dM/dt = -gamma(M x H_eff) + (alpha/M_s) M x (M x H_eff) governing magnetization dynamics. Solves for the domain wall profile theta(x) = 2 arctan(exp(x/delta)) with width delta = sqrt(A/K) and energy sigma = 4 sqrt(A K). Classifies topological defects by homotopy groups.

**Key Results**:
- LL equation with precession and Gilbert damping terms
- Bloch wall solution as topological soliton (kink)
- Domain wall width delta = sqrt(A/K_u), energy sigma = 4 sqrt(A K_u)
- Homotopy classification: pi_0 walls, pi_1 vortices, pi_2 monopoles, pi_3 textures
- LL equation integrable in 1+1D (Lakshmanan equivalence to NLS)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 3.1 | LL equation | dM/dt = -gamma(M x H_eff) + (alpha/M_s) M x(M x H_eff), Section 2.1 |
| eq 3.2 | Domain wall profile | theta(x) = 2 arctan(exp(x/delta)), Section 4.1 |
| eq 3.3 | Exchange energy | E_ex = A integral \|grad m\|^2 d^3r, Section 3.2 |

**Dependencies**: Upstream of 04 (order parameter concept); parallel to 08 (GL functional)

---

### Paper 04: On the Theory of Phase Transitions
- **File**: `04_Landau_1937_Phase_Transitions.md`
- **arXiv**: N/A
- **Year**: 1937
- **Relevance**: CRITICAL
- **Tags**: order parameter, symmetry breaking, Landau free energy, universality, mean field, critical exponents, Ginzburg criterion

**Summary**: Foundational paper establishing the universal theory of phase transitions based on symmetry. Introduces the order parameter eta, the free energy expansion F = F_0 + a(T-T_c) eta^2 + b eta^4, and derives mean-field critical exponents (beta=1/2, gamma=1, delta=3, alpha=0). Classifies transitions by group-subgroup relationship G -> H. The cubic term criterion determines first- vs second-order. The Ginzburg criterion identifies when fluctuations dominate.

**Key Results**:
- Order parameter concept and G -> H symmetry classification
- F(eta,T) = F_0 + a_0(T-T_c) eta^2 + b eta^4 (Z_2 case)
- Mean-field exponents: beta=1/2, gamma=1, delta=3, alpha=0 (jump)
- Upper critical dimension d_uc = 4: mean field exact above d=4
- Cubic invariant => first-order transition (V'''(0) = -7.2 for SU(3))
- Ginzburg criterion: d_int=8 > d_uc=4 => mean field EXACT for internal space

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 4.1 | Landau free energy | F = F_0 + a_0(T-T_c) eta^2 + b eta^4, Section 4.1 |
| eq 4.2 | Equilibrium order parameter | eta_0 = sqrt(a_0(T_c-T)/(2b)), Section 4.3 |
| eq 4.3 | Goldstone theorem | dim(G/H) massless modes, Section 5.2 |

**Dependencies**: Foundation for 05, 08, 09; framework analog: V_eff(tau) = Landau F(eta)

---

### Paper 05: The Theory of Superfluidity of Helium II
- **File**: `05_Landau_1941_Superfluidity_I.md`
- **arXiv**: N/A
- **Year**: 1941
- **Relevance**: CRITICAL
- **Tags**: two-fluid model, phonon-roton spectrum, critical velocity, second sound, superfluidity

**Summary**: Establishes the two-fluid model: He II = ground-state condensate (superfluid, zero entropy) + thermal quasiparticle gas (normal fluid). The phonon-roton dispersion epsilon(p) has a linear phonon branch (c ~ 238 m/s) and a gapped roton minimum at finite momentum. Derives the Landau critical velocity v_c = min_p[epsilon(p)/p] and predicts second sound. THE prototype for phonon-exflation cosmology.

**Key Results**:
- Two-fluid model: rho = rho_s + rho_n
- Phonon dispersion: epsilon = cp (linear, Goldstone)
- Roton minimum: epsilon = Delta + (p-p_0)^2/(2 mu*)
- Landau critical velocity: v_c = min(epsilon/p)
- Second sound velocity: u_2^2 = rho_s s^2 T/(rho_n c_p)
- Quantized circulation: oint v_s dl = n kappa, kappa = h/m_He

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 5.1 | Phonon dispersion | epsilon(p) = c p, Section 3.1 |
| eq 5.2 | Roton minimum | epsilon = Delta + (p-p_0)^2/(2 mu*), Section 3.2 |
| eq 5.3 | Critical velocity | v_c = min_p[epsilon(p)/p], Section 4.1 |
| eq 5.4 | Second sound | u_2^2 = rho_s s^2 T/(rho_n c_p), Section 5.1 |

**Dependencies**: Builds on 04; refined by 07; generalized to Fermi systems in 11

---

### Paper 06: On the Vibrations of the Electronic Plasma (Landau Damping)
- **File**: `06_Landau_1946_Landau_Damping.md`
- **arXiv**: N/A
- **Year**: 1946
- **Relevance**: MEDIUM
- **Tags**: Landau damping, Vlasov equation, plasma oscillations, collisionless dynamics, phase mixing

**Summary**: Solves the initial value problem for plasma oscillations via Laplace transform, deriving collisionless (Landau) damping from resonant wave-particle interaction at v = omega/k. Phase mixing is reversible (plasma echo), not dissipative. The Landau contour prescription is structurally identical to Feynman's i-epsilon.

**Key Results**:
- Landau contour prescription for dielectric function analytic continuation
- Damping rate from df_0/dv at resonance v = omega/k
- Bohm-Gross dispersion: omega^2 = omega_p^2(1 + 3k^2 lambda_D^2)
- Phase mixing without entropy production (plasma echo confirms reversibility)
- Connection to Feynman i-epsilon prescription

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 6.1 | Dielectric function | epsilon(k,omega), Section 2.3-2.4 |
| eq 6.2 | Damping rate | gamma ~ exp(-1/(2k^2 lambda_D^2)), Section 3.1 |
| eq 6.3 | Vlasov equation | df/dt + v grad_x f + (e/m) E grad_v f = 0, Section 1.1 |

**Dependencies**: Builds on kinetic theory tradition; connects to 11 (zero sound as collisionless mode)

---

### Paper 07: Superfluidity of Helium II (Second Paper)
- **File**: `07_Landau_1947_Superfluidity_II.md`
- **arXiv**: N/A
- **Year**: 1947
- **Relevance**: HIGH
- **Tags**: roton parameters, normal fluid density, Andronikashvili experiment, specific heat

**Summary**: Revises roton parameters to Delta/k_B = 8.6 K, p_0/hbar = 1.92 A^{-1}, mu* = 0.16 m_He -- confirmed by neutron scattering to 3 significant figures 14 years later. Quantitative rho_n(T) from phonon + roton contributions matches Andronikashvili data to ~5%.

**Key Results**:
- Revised roton: Delta/k_B=8.6 K, p_0/hbar=1.92 A^{-1}, mu*=0.16 m_He
- rho_n^{phonon} ~ T^4, rho_n^{roton} ~ T^{-1/2} exp(-Delta/(k_B T))
- Phonon-roton crossover at T_cross ~ 0.6 K

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 7.1 | Phonon normal density | rho_n^{ph} = (2pi^2/45)(k_B T)^4/(hbar^3 c^5), Section 3.1 |
| eq 7.2 | Roton normal density | rho_n^{rot} ~ p_0^4 (k_B T)^{-1/2} exp(-Delta/(k_B T)), Section 3.2 |

**Dependencies**: Refines 05; provides quantitative thermodynamics underlying 11

---

### Paper 08: On the Theory of Superconductivity (Ginzburg-Landau)
- **File**: `08_Ginzburg_Landau_1950_Superconductivity.md`
- **arXiv**: N/A
- **Year**: 1950
- **Relevance**: CRITICAL
- **Tags**: Ginzburg-Landau theory, order parameter, coherence length, penetration depth, kappa, Type I/II, Higgs mechanism, flux quantization

**Summary**: Introduces the complex order parameter psi(r) for superconductivity and the GL free energy functional with gauge-covariant gradient. Derives two characteristic lengths: coherence length xi and penetration depth lambda. The GL parameter kappa = lambda/xi classifies Type I (kappa < 1/sqrt(2)) vs Type II. Predicts flux quantization Phi_0 = h/(2e). The GL functional IS the GPE energy functional.

**Key Results**:
- GL free energy: f_s = alpha|psi|^2 + (beta/2)|psi|^4 + (1/(2m*))|(-ihbar nabla - (e*/c)A)psi|^2 + B^2/(8pi)
- xi(T) = hbar/sqrt(2m*|alpha|), lambda(T) = sqrt(m*c^2 beta/(4pi e*^2 |alpha|))
- kappa = lambda/xi: Type I < 1/sqrt(2) < Type II
- H_c2 = Phi_0/(2pi xi^2), H_c1 = (Phi_0/(4pi lambda^2))(ln kappa + 0.50)
- Phi_0 = h/(2e) = 2.07 x 10^{-7} G cm^2
- Meissner effect = Higgs mechanism for photon

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 8.1 | GL free energy density | Section 2.1 |
| eq 8.2 | First GL equation | alpha psi + beta\|psi\|^2 psi + (1/(2m*))(-ihbar nabla-(e*/c)A)^2 psi = 0, Section 4.1 |
| eq 8.3 | Supercurrent | j = (e*/(2m*))[psi*(-ihbar nabla-(e*/c)A)psi + c.c.], Section 4.1 |
| eq 8.4 | GL parameter | kappa = lambda/xi, Section 3.3 |

**Dependencies**: Builds on 04; leads to 13 (vortices), 15 (microscopic via Gor'kov), 29 (KZ)

---

### Paper 09: Anomalous Absorption of Sound Near Phase Transitions (TDGL)
- **File**: `09_Landau_Khalatnikov_1954_TDGL.md`
- **arXiv**: N/A
- **Year**: 1954
- **Relevance**: HIGH
- **Tags**: TDGL, critical slowing down, dynamic critical exponent, sound absorption, relaxation, Hohenberg-Halperin

**Summary**: Introduces the kinetic equation dphi/dt = -(1/tau_0)(dF/dphi) for order parameter relaxation. Predicts critical slowing down: tau ~ |T-T_c|^{-nu z} diverges at T_c. The TDGL equation is the dissipative complement to the GPE (related by Wick rotation t -> -it). Foundation of dynamic critical phenomena and the Hohenberg-Halperin classification.

**Key Results**:
- LK equation: dphi/dt = -(1/tau_0) dF/dphi
- Critical slowing: tau ~ |T-T_c|^{-nu z}, nu z = 1 (mean field)
- Sound absorption: alpha ~ omega^2 tau (relaxation regime)
- Dynamic universality: tau ~ xi^z (defines z)
- TDGL = Wick rotation of GPE (t -> -it)
- Hohenberg-Halperin: Model A (z~2), B (z~4), C, E/F, H

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 9.1 | LK relaxation | dphi/dt = -(1/tau_0)(dF/dphi), Section 2 |
| eq 9.2 | Critical slowing | tau = tau_0/(a\|T-T_c\|), Section 3 |
| eq 9.3 | TDGL with noise | tau_0 dphi/dt = -dF/dphi + kappa nabla^2 phi + eta, Section 6 |

**Dependencies**: Builds on 04; dynamic complement to 08; feeds into 29 (KZ freeze-out)

---

### Paper 10: Running Coupling (LAK)
- **File**: `10_LAK_1954_Running_Coupling.md`
- **arXiv**: N/A
- **Year**: 1954
- **Relevance**: HIGH
- **Tags**: running coupling, Landau pole, triviality, QED, beta function, zero charge, asymptotic freedom

**Summary**: Landau, Abrikosov, and Khalatnikov sum leading logarithms of QED to all orders, deriving the running coupling alpha_eff(q^2) = alpha/(1-(alpha/(3pi))ln(q^2/m^2)). The Landau pole signals QED is not UV-complete. The "Moscow zero-charge" conjecture anticipated asymptotic freedom by 20 years.

**Key Results**:
- Running coupling: alpha_eff(q^2) = alpha/(1-(alpha/(3pi))ln(q^2/m^2))
- Landau pole: Lambda = m exp(3pi/(2alpha)) ~ 10^{280} GeV
- QED beta function: beta(alpha) = 2alpha^2/(3pi) > 0
- Zero-charge conjecture: QED trivial, only asymptotically free theories consistent
- Framework: gauge couplings from SU(3) geometry, g_1/g_2 = e^{-2tau}

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 10.1 | Running coupling | alpha_eff = alpha/(1-(alpha/(3pi))ln(q^2/m^2)), Section 3 |
| eq 10.2 | Landau pole | Lambda = m exp(3pi/(2alpha)), Section 4 |
| eq 10.3 | QED beta function | beta = 2alpha^2/(3pi), Section 6 |

**Dependencies**: Leads to 14 (vertex analyticity); framework: Weinberg angle from geometry

---

### Paper 11: The Theory of a Fermi Liquid
- **File**: `11_Landau_1956_Fermi_Liquid.md`
- **arXiv**: N/A
- **Year**: 1956
- **Relevance**: CRITICAL
- **Tags**: quasiparticle, Fermi liquid, Landau parameters, effective mass, Pomeranchuk stability, adiabatic continuity

**Summary**: Introduces the quasiparticle concept via adiabatic continuity: low-energy excitations of an interacting Fermi system are in 1-to-1 correspondence with free-particle excitations, with renormalized mass m* and finite lifetime 1/tau ~ (epsilon-epsilon_F)^2. The Landau interaction function f(k,sigma;k',sigma') parametrized by F_l^{s,a}. Pomeranchuk stability: F_l > -(2l+1). Conceptual foundation for SM particles as quasiparticles of the vacuum.

**Key Results**:
- Adiabatic continuity: interacting eigenstates evolve continuously from free ones
- m*/m = 1 + F_1^s/3
- chi/chi_free = (m*/m)/(1 + F_0^a)
- Pomeranchuk stability: F_l^{s,a} > -(2l+1) for all l
- Quasiparticle lifetime: 1/tau ~ (epsilon-epsilon_F)^2 (phase space)
- Framework: f(0,0)=-4.687 (S22c, UNSTABLE at T=0), GGE-stabilized (S58)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 11.1 | Quasiparticle energy | epsilon_k = epsilon_F + hbar k_F(\|k\|-k_F)/m*, Section 3 |
| eq 11.2 | Effective mass | m*/m = 1 + F_1^s/3, Section 5 |
| eq 11.3 | Pomeranchuk condition | F_l^{s,a} > -(2l+1), Section 6 |
| eq 11.4 | Landau energy functional | E[n] = E_0 + sum epsilon_k^0 dn_k + (1/2V) sum f dn_k dn_{k'}, Section 4 |

**Dependencies**: Builds on 05; leads to 12, 15; verified in S22c, S58

---

### Paper 12: Oscillations in a Fermi Liquid (Zero Sound)
- **File**: `12_Landau_1957_Zero_Sound.md`
- **arXiv**: N/A
- **Year**: 1957
- **Relevance**: HIGH
- **Tags**: zero sound, collisionless collective mode, Fermi surface deformation, transport equation

**Summary**: Derives zero sound -- a collective oscillation of the Fermi surface shape in the collisionless regime (omega tau >> 1), driven by the Landau interaction f rather than by collisions. Zero sound velocity v_0 > v_F is determined by an implicit equation involving F_0^s. Observed in He-3 at T < 100 mK.

**Key Results**:
- Zero sound dispersion: 1 = (F_0^s/2)[1 + (u/2)ln((u+1)/(u-1))], u = omega/(k v_F)
- v_0 > v_F always (above Fermi velocity to avoid Landau damping)
- Strong coupling: v_0 ~ v_F sqrt(F_0^s/3)
- First/zero sound crossover at omega tau ~ 1

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 12.1 | Zero sound equation | 1 = (F_0^s/2)[1+(u/2)ln((u+1)/(u-1))], Section 3.1 |

**Dependencies**: Builds on 11 (Landau parameters)

---

### Paper 13: Magnetic Properties of Superconductors of the Second Group (Abrikosov Vortices)
- **File**: `13_Abrikosov_1957_Vortices.md`
- **arXiv**: N/A
- **Year**: 1957
- **Relevance**: HIGH
- **Tags**: Abrikosov vortices, Type II superconductor, mixed state, vortex lattice, flux quantization

**Summary**: Solves the GL equations near H_c2 to derive the mixed state of Type II superconductors: a triangular array of quantized vortices, each carrying flux Phi_0 = h/(2e), with core size xi and flux tube diameter lambda. Nobel Prize 2003 (shared with Ginzburg and Leggett). GPE simulation vortices are direct descendants.

**Key Results**:
- H_c2 = Phi_0/(2pi xi^2) from linearized GL = Landau level problem
- Triangular vortex lattice (Abrikosov lattice)
- Each vortex carries Phi_0, core size xi, phase winding 2pi
- beta_A = <|psi|^4>/<|psi|^2>^2 = 1.16 (triangular)
- Vortex-vortex interaction: repulsive for kappa > 1/sqrt(2)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 13.1 | Upper critical field | H_c2 = Phi_0/(2pi xi^2) |
| eq 13.2 | Abrikosov parameter | beta_A = <\|psi\|^4>/<\|psi\|^2>^2 |

**Dependencies**: Builds on 08 (GL theory), 02 (Landau levels for H_c2)

---

### Paper 14: Analytic Properties of Vertex Parts
- **File**: `14_Landau_1958_Vertex_Parts.md`
- **arXiv**: N/A
- **Year**: 1958
- **Relevance**: MEDIUM
- **Tags**: Landau equations, Feynman diagram singularities, S-matrix analyticity, pinch singularity

**Summary**: Derives the Landau equations determining singularity locations of Feynman diagram amplitudes in external momentum space. Uses Feynman parametric representation and the pinch condition. Foundation of the analytic S-matrix program.

**Key Results**:
- Landau equations: alpha_i(q_i^2 - m_i^2) = 0 for all internal lines, plus loop constraints
- Classification of singularities: leading (all alpha_i > 0) vs subleading
- Connection to unitarity cuts and dispersion relations
- Landau gauge (xi=0) as simplest for analyticity

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 14.1 | Feynman parametric integral | Section 2.2 |
| eq 14.2 | Landau equations | alpha_i(q_i^2-m_i^2) = 0, Section 3 |

**Dependencies**: Builds on 10 (LAK perturbation theory)

---

### Paper 15: Theory of Superconductivity (BCS)
- **File**: `15_BCS_1957_Superconductivity.md`
- **arXiv**: N/A
- **Year**: 1957
- **Relevance**: CRITICAL
- **Tags**: BCS theory, Cooper pairing, gap equation, Bogoliubov quasiparticles, condensation energy

**Summary**: Microscopic theory of superconductivity. The BCS ground state is a coherent superposition of Cooper pairs with amplitudes u_k, v_k. The gap equation Delta = V sum_k u_k v_k determines the self-consistent gap. Quasiparticle energy E_k = sqrt(epsilon_k^2 + Delta^2) is gapped. Foundation for the framework's BCS on SU(3).

**Key Results**:
- BCS ground state: |BCS> = prod_k (u_k + v_k c_{kup}^dag c_{-kdn}^dag)|0>
- Gap equation: 1/V = sum_k 1/(2E_k), E_k = sqrt(epsilon_k^2 + Delta^2)
- Condensation energy: E_cond = -(1/2)N(0)Delta^2
- Cooper instability: ANY attractive interaction produces pairing (1D theorem, S35)
- Gor'kov: GL derives from BCS near T_c with e*=2e, m*=2m

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 15.1 | BCS state | \|BCS> = prod_k(u_k + v_k c^dag c^dag)\|0> |
| eq 15.2 | Gap equation | Delta = V sum_k Delta/(2E_k) |
| eq 15.3 | Quasiparticle energy | E_k = sqrt(epsilon_k^2 + Delta^2) |
| eq 15.4 | BCS amplitudes | v_k^2 = (1/2)(1-epsilon_k/E_k) |

**Dependencies**: Builds on 08, 11; leads to 16, 17, 25; verified: S35 RG-BCS-35

---

### Paper 16: Exact Eigenstates of the Pairing-Force Hamiltonian (Richardson)
- **File**: `16_Richardson_1963_Exact_Pairing.md`
- **arXiv**: N/A
- **Year**: 1963
- **Relevance**: CRITICAL
- **Tags**: Richardson equations, exact pairing, integrability, pair rapidities, conserved quantities

**Summary**: Proves the pairing Hamiltonian is exactly solvable. Eigenstates with M pairs have the product form with collective pair operators. The pair rapidities satisfy the Richardson equations -- coupled nonlinear algebraic equations. Foundation for the framework's 8 conserved integrals and GGE permanence.

**Key Results**:
- Pairing Hamiltonian completely integrable
- Richardson equations for pair rapidities z_a
- Energy eigenvalue: E = sum epsilon_i nu_i + sum E_alpha
- Reduces exponential Hilbert space to polynomial equations
- Foundation for Gaudin's generalization and conserved quantities

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 16.1 | Richardson equations | 1/G + sum Omega_j/(2epsilon_j - E_a) - sum 2/(E_a - E_b) = 0 |
| eq 16.2 | Collective pair operator | B_a^dag = sum_i 1/(2epsilon_i - E_a) A_i^dag |

**Dependencies**: Builds on 15; leads to 17, 22, 24; verified: S37-38

---

### Paper 17: Exactly Solvable Richardson-Gaudin Models (DPS Review)
- **File**: `17_Dukelsky_Pittel_Sierra_2004_RG_Review.md`
- **arXiv**: nucl-th/0405011
- **Year**: 2004
- **Relevance**: CRITICAL
- **Tags**: Richardson-Gaudin models, integrability, electrostatic mapping, conserved charges, BCS-BEC, nuclear pairing

**Summary**: Comprehensive review of Richardson-Gaudin integrable models. Three families (rational/XXX, trigonometric/XXZ, hyperbolic) with conserved charges R_l. Electrostatic mapping converts Richardson equations to 2D classical electrostatics. BCS emerges as N -> infinity limit. Direct source for Sessions 33-38.

**Key Results**:
- Three families of RG integrability: rational, trigonometric, hyperbolic
- Conserved charges R_l: [R_l, R_{l'}] = 0
- Electrostatic mapping: pair rapidities = equilibrium charges
- BCS as large-N limit of exact Richardson solution

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 17.1 | Conserved charges R_l | Section II.C |
| eq 17.2 | Generalized Richardson equations | Section II.D |
| eq 17.3 | Electrostatic analogy | Section III |

**Dependencies**: Builds on 16; leads to 24; verified: S33-38

---

### Paper 18: Superfluid Analogies of Cosmological Phenomena (Volovik)
- **File**: `18_Volovik_2001_Superfluid_Analogies.md`
- **arXiv**: gr-qc/0005091
- **Year**: 2001
- **Relevance**: HIGH
- **Tags**: superfluid vacuum, acoustic metric, emergent Lorentz invariance, CC=0, Fermi point topology, He-3

**Summary**: Derives the acoustic metric from superfluid He-4 hydrodynamics and classifies fermionic vacua by momentum-space topology. Proves vacuum energy vanishes in equilibrium for self-sustaining systems (CC = 0). The anti-GUT view: symmetries emerge at low energy from topological protection.

**Key Results**:
- Acoustic metric g^{mu nu} from two-fluid hydrodynamics
- CC = 0 in equilibrium (thermodynamic identity)
- Universality classes: Fermi surface (N_1), Fermi points (N_3), gapped
- Effective field theory underestimates by 10^{120}

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 18.1 | Acoustic metric | g^{mu nu}, Section II |
| eq 18.2 | Vacuum energy | epsilon_vac = 0 (equilibrium), Section II.G |

**Dependencies**: Builds on 05, 11; leads to 19, 20, 21

---

### Paper 19: The Universe in a Helium Droplet (Volovik)
- **File**: `19_Volovik_2003_Helium_Droplet.md`
- **arXiv**: N/A (book, Oxford UP)
- **Year**: 2003
- **Relevance**: HIGH
- **Tags**: emergent gravity, Weyl fermions, gauge fields from order parameter, superfluid vacuum, topological defects

**Summary**: Monograph: all physical laws emerge from condensed matter vacuum. He-3-A order parameter generates Weyl fermions, gauge fields, and effective gravity. Foundational for phonon-exflation.

**Key Results**:
- He-3-A order parameter A_{alpha i} generates SM-like spectrum
- Weyl fermions from topologically protected Fermi points
- Gravity from acoustic metric; domain defects by homotopy

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 19.1 | He-3-A order parameter | A_{alpha i}, Chapter 7 |
| eq 19.2 | Emergent Weyl equation | sigma^a e_a^i (p_i - p_{Fi}) chi = 0, Chapter 8 |

**Dependencies**: Extends 18; framework's conceptual ancestor

---

### Paper 20: Theory of Dark Matter Superfluidity (Berezhiani-Khoury)
- **File**: `20_Berezhiani_Khoury_2015_DM_Superfluidity.md`
- **arXiv**: 1507.01019
- **Year**: 2015
- **Relevance**: MEDIUM
- **Tags**: DM superfluidity, MOND, phonon EFT, BEC dark matter, rotation curves

**Summary**: DM as eV-mass particles forming galactic superfluid. Phonons mediate MOND-like force via L ~ X sqrt(|X|). Unifies CDM + MOND as normal and superfluid phases.

**Key Results**:
- DM phonon EFT: P(X) ~ X sqrt(|X|) gives MOND + P ~ rho^3
- Superfluid core ~ 100 kpc, cored profile
- DM mass ~ eV, T_c ~ mK

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 20.1 | Phonon Lagrangian | L = P(X) ~ X sqrt(\|X\|), Section 2 |

**Dependencies**: Builds on 18; structural parallel to framework

---

### Paper 21: Scale-Dependent Gravity in Superfluid Vacuum Theory (Zloshchastiev)
- **File**: `21_Zloshchastiev_2020_SVT_Emergent_Metric.md`
- **arXiv**: 2011.12565
- **Year**: 2020
- **Relevance**: HIGH
- **Tags**: superfluid vacuum, logarithmic GPE, emergent FLRW, rotation curves, scale-dependent gravity

**Summary**: Derives seven-term gravitational potential from logarithmic GPE for vacuum condensate. Logarithmic nonlinearity uniquely produces density-independent sound speed (Lorentz invariance). Interpolates sub-Newtonian through FLRW from single condensate.

**Key Results**:
- Log-GPE with density-independent c_s = sqrt(|b|/m)
- Seven-term gravitational potential covering all scales
- FLRW at cosmological scale from condensate dynamics
- Rotation curves without dark matter

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 21.1 | Log-GPE | Section 2 |
| eq 21.2 | Seven-term potential | Phi(r) = 7 terms, Section 3 |

**Dependencies**: Builds on 18, 19; explicit GPE-to-gravity derivation

---

### Paper 22: Relaxation in Integrable Systems -- GGE Founding (Rigol et al.)
- **File**: `22_Rigol_2006_GGE_Founding.md`
- **arXiv**: cond-mat/0604476
- **Year**: 2007
- **Relevance**: CRITICAL
- **Tags**: GGE, integrable systems, quantum quench, thermalization, conserved quantities

**Summary**: Founds the Generalized Gibbs Ensemble. For integrable systems with conserved quantities I_m, maximizing entropy subject to all constraints yields rho_GGE = Z^{-1} exp(-sum lambda_m I_m). GGE predicts post-quench observables while thermal fails. Framework: S38 GGE with 8 Richardson-Gaudin integrals.

**Key Results**:
- GGE density matrix: rho = Z^{-1} exp(-sum lambda_m I_m)
- Lagrange multipliers from initial conditions
- Reduces to grand-canonical for non-integrable systems
- GGE carries more memory of initial conditions than thermal

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 22.1 | GGE density matrix | rho = Z^{-1} exp(-sum lambda_m I_m) |
| eq 22.2 | Constraint equations | Tr(I_m rho) = <I_m>(t=0) |

**Dependencies**: Builds on 16; leads to 23; verified: S38 GGE permanence

---

### Paper 23: GGE in Integrable Lattice Models (Vidmar-Rigol)
- **File**: `23_Vidmar_Rigol_2016_GGE_Lattice.md`
- **arXiv**: 1604.03990
- **Year**: 2016
- **Relevance**: HIGH
- **Tags**: GGE review, generalized eigenstate thermalization, XX model, transverse-field Ising

**Summary**: Reviews GGE in lattice models. Proves generalized eigenstate thermalization: eigenstates with similar conserved-quantity distributions have similar observables. No spatial tracing needed. Addresses which conserved quantities suffice.

**Key Results**:
- Generalized eigenstate thermalization hypothesis (GETH)
- Three ensembles: diagonal (exact), thermal (fails), GGE (works)
- Full-system GGE without spatial subsystem tracing
- Interacting bosons map to free fermions (nonlocally)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 23.1 | Diagonal ensemble | <O>_DE = sum_n \|c_n\|^2 <n\|O\|n> |

**Dependencies**: Builds on 22; extends GGE theory

---

### Paper 24: Richardson-Gaudin Models and Broken Integrability (Claeys)
- **File**: `24_Claeys_2018_RG_Broken_Integrability.md`
- **arXiv**: 1809.04447
- **Year**: 2018
- **Relevance**: HIGH
- **Tags**: Richardson-Gaudin, broken integrability, eigenvalue-based method, Floquet, variational Bethe ansatz

**Summary**: PhD thesis on RG models and extensions to broken integrability. Eigenvalue-based numerics avoiding singular Richardson equations. RG states as variational basis for non-integrable Hamiltonians. Floquet dynamics of driven integrable systems. Framework: off-Jensen integrability breaking.

**Key Results**:
- Eigenvalue-based method (Lambda_i instead of pair rapidities)
- Three GGA families: rational, trigonometric, hyperbolic
- Physical: central spin, reduced BCS, p_x+ip_y models
- RG states as variational basis for non-integrable perturbations
- Floquet driven dynamics

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 24.1 | Conserved charges Q_i | Chapter 2 |

**Dependencies**: Builds on 16, 17; framework: integrability breaking on SU(3)

---

### Paper 25: BCS-BEC Crossover (Strinati et al.)
- **File**: `25_Strinati_2018_BCS_BEC_Crossover.md`
- **arXiv**: 1802.05997
- **Year**: 2018
- **Relevance**: HIGH
- **Tags**: BCS-BEC crossover, cold atoms, nuclear matter, unitarity, NSR, pseudogap, BdG

**Summary**: Comprehensive review from cold atoms to nuclear systems. BCS smoothly connects to BEC via (k_F a_F)^{-1}. Derives BdG equations, GL and GP limits, NSR fluctuations, pseudogap. Framework: E_vac/E_cond = 28.8, g*N(E_F) = 2.18 (S37).

**Key Results**:
- Crossover parameter (k_F a_F)^{-1}: BCS(<0), unitarity(=0), BEC(>0)
- mu drives crossover: mu>0 Fermi surface, mu<0 no Fermi surface
- BdG for inhomogeneous systems; GL and GP as limits
- NSR pair propagator for T_c
- Pseudogap from precursor pairing

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 25.1 | Crossover parameter | (k_F a_F)^{-1}, Section 2 |
| eq 25.2 | NSR pair propagator | Gamma_0(Q), Section 3 |

**Dependencies**: Builds on 15, 08; leads to 26, 27, 28

---

### Paper 26: Kibble-Zurek Universality in Fermi Superfluid (Ko et al.)
- **File**: `26_Ko_2019_KZ_BCS_BEC.md`
- **arXiv**: 1902.06922
- **Year**: 2019
- **Relevance**: HIGH
- **Tags**: Kibble-Zurek, BCS-BEC crossover, vortex formation, universal scaling, Li-6

**Summary**: Observes KZ universality across BCS-BEC crossover in Li-6. Vortex density N_v ~ t_q^{-alpha_KZ} with constant exponent independent of interaction strength. U(1) universality class preserved across crossover.

**Key Results**:
- KZ scaling N_v ~ t_q^{-alpha_KZ} across BCS-BEC crossover
- alpha_KZ constant (U(1) universality independent of coupling)
- Inhomogeneous KZ: alpha = (D-d)(1+2nu)/(1+nu z)
- Saturation from vortex core overlap

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 26.1 | KZ scaling | N_v ~ t_q^{-alpha_KZ} |
| eq 26.2 | Inhomogeneous exponent | alpha = (D-d)(1+2nu)/(1+nu z) |

**Dependencies**: Builds on 25, 29; experimental KZ in BCS-BEC

---

### Paper 27: Gate-Controlled BCS-BEC Crossover in 2D (Nakagawa et al.)
- **File**: `27_Nakagawa_2020_Gate_Controlled_BCS_BEC.md`
- **arXiv**: 2012.05707
- **Year**: 2020
- **Relevance**: MEDIUM
- **Tags**: BCS-BEC crossover, 2D superconductor, BKT transition, pseudogap, ionic gating

**Summary**: BCS-BEC crossover in 2D ZrNCl via ionic gating. T_BKT/T_F = 0.12 at low doping, consistent with BCS-BEC upper bound. Pseudogap phase. Dimensional crossover 3D -> 2D.

**Key Results**:
- T_BKT/T_F = 0.12 (theoretical BCS-BEC bound)
- Pseudogap from tunneling spectra
- 3D -> 2D dimensional crossover

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 27.1 | Halperin-Nelson BKT | rho(T) fit |

**Dependencies**: Builds on 25; solid-state BCS-BEC realization

---

### Paper 28: Finite-Size Effects in 2D BCS-BEC Crossover (Lanaro et al.)
- **File**: `28_Lanaro_Bighin_2024_Finite_Size_BCS_BEC.md`
- **arXiv**: 2401.06054
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: finite-size BCS-BEC, 2D superfluidity, infrared cutoff, BKT, RG

**Summary**: Finite-size effects on 2D BCS-BEC crossover. Gap enhanced, superfluid density suppressed by IR cutoff k_min = 2pi/L. In 2D, Cooper pairs always form bound states.

**Key Results**:
- 2D always has bound Cooper pairs (no threshold)
- Gap enhanced by finite-size
- BKT detected via RG at finite L
- Framework: SU(3) BCS is finite-size (8D manifold)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 28.1 | IR cutoff energy | epsilon_min = hbar^2 k_min^2/(2m) |

**Dependencies**: Builds on 25; finite-size relevant to SU(3) BCS

---

### Paper 29: Cosmological Experiments in Superfluids (Kibble-Zurek)
- **File**: `29_Zurek_1985_Kibble_Zurek.md`
- **arXiv**: cond-mat/9502119
- **Year**: 1985/1995
- **Relevance**: CRITICAL
- **Tags**: Kibble-Zurek mechanism, defect formation, quench dynamics, freeze-out, cosmic strings

**Summary**: Establishes the KZ freeze-out mechanism: defect density set by correlation length at freeze-out time where tau(t_hat) = t_hat. Replaces Kibble's Ginzburg temperature estimate. Applies to superfluids, superconductors, and cosmological transitions. Framework: KZ transit dynamics S37-38.

**Key Results**:
- Freeze-out: tau(epsilon(t_hat)) = t_hat
- xi_hat ~ (tau_Q tau_0)^{nu/(1+nu z)}
- n_defect ~ xi_hat^{-(D-d)}
- Global (cosmic strings) and local (flux tubes) symmetry breaking

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 29.1 | Freeze-out condition | tau(t_hat) = t_hat, Section 3 |
| eq 29.2 | Freeze-out xi | xi_hat ~ (tau_Q tau_0)^{nu/(1+nu z)}, Section 3 |
| eq 29.3 | Defect density | n ~ xi_hat^{-(D-d)}, Section 3 |

**Dependencies**: Builds on 04, 08, 09; verified: S37-38, S43

---

### Paper 30: Exact WKB and Landau-Zener for Cosmological Particle Production
- **File**: `30_Enomoto_Matsuda_2022_WKB_LZ.md`
- **arXiv**: 2104.02312
- **Year**: 2022
- **Relevance**: HIGH
- **Tags**: Landau-Zener, WKB, cosmological particle production, Stokes lines, asymmetry

**Summary**: Combines exact WKB with Landau-Zener for particle production by time-dependent fields. Time-dependent mu required for asymmetry. Framework: S38 Schwinger-instanton duality S_Schwinger(0.070) = S_inst(0.069).

**Key Results**:
- P_LZ = exp(-pi Delta^2/(2v)) (Landau-Zener probability)
- Exact WKB resolves Stokes line structure
- Constant mu gives NO asymmetry; dot-mu != 0 required

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 30.1 | Landau-Zener | P_LZ = exp(-pi Delta^2/(2v)), Section I.A |

**Dependencies**: Connects to 29 (KZ); framework: S38 instanton-Schwinger duality

---

### Paper 31: GPV Signatures in 14C (Cappuzzello et al.)
- **File**: `31_Cappuzzello_2015_GPV_14C.md`
- **arXiv**: N/A
- **Year**: 2015
- **Relevance**: HIGH
- **Tags**: GPV, giant pairing vibration, two-neutron transfer, 14C, nuclear pairing

**Summary**: First experimental GPV signatures in light nuclei 14C and 15C via two-neutron transfer. GPV is coherent pair mode from second major shell, predicted by Broglia-Bes (1977). Framework: S37 GPV analog omega=0.792, 85.5% strength.

**Key Results**:
- First GPV observation via 12C(18O,16O)14C
- GPV energy ~ 65/A^{1/3} MeV
- Cross section 20-100% of ground state transfer

**Dependencies**: Builds on 15; leads to 32, 33

---

### Paper 32: GPV in Heavy Nuclei (Fortunato et al.)
- **File**: `32_Fortunato_2019_GPV_Heavy_Nuclei.md`
- **arXiv**: 1905.01339
- **Year**: 2019
- **Relevance**: MEDIUM
- **Tags**: GPV, heavy nuclei, Sn, Pb, Q-value mismatch

**Summary**: Reviews GPV theory and searches in heavy nuclei. GPV elusive in Sn/Pb due to Q-value mismatch. Discusses weakly-bound projectiles and continuum effects.

**Key Results**:
- GPV from pairing RPA: second-shell collective mode
- Q-value mismatch hinders heavy-nucleus detection
- Formal analogy: shape (GDR) and pairing (GPV) giant modes

**Dependencies**: Builds on 31

---

### Paper 33: GPV Fragmentation in 14C (Barranco et al.)
- **File**: `33_GPV_Fragmentation_2024.md`
- **arXiv**: 2402.14166
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: GPV fragmentation, particle-vibration coupling, pp-RPA, 14C

**Summary**: GPV fragmented by coupling to quadrupole core vibrations. Four-component pp-RPA basis. PVC induces additional pairing via phonon exchange. Framework: S37 GPV as pair vibrator.

**Key Results**:
- PVC fragments GPV across excitation energies
- Self-energy effects modify effective spectrum
- Phonon exchange provides additional pairing channel

**Dependencies**: Builds on 31; adds many-body dressing

---

### Paper 34: Higgs Response in Nuclear Pair Condensates (Takahashi et al.)
- **File**: `34_Takahashi_2023_Higgs_Nuclear.md`
- **arXiv**: 2302.14214
- **Year**: 2023
- **Relevance**: HIGH
- **Tags**: Higgs mode, nuclear BCS, pair vibration, condensation energy, QRPA

**Summary**: Introduces Higgs operator P_H = P_ad + P_rm probing amplitude oscillations of nuclear pair condensate. Condensation energy from Higgs strength sum rule. QRPA on Sn isotopes. Framework: S38 pair vibration.

**Key Results**:
- Higgs operator P_H = P_ad + P_rm
- Condensation energy from strength sum
- Higgs strength concentrated at 2Delta
- Static polarizability = pair compressibility

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 34.1 | Higgs operator | P_H = P_ad + P_rm |

**Dependencies**: Builds on 15; parallel to 31-33

---

### Paper 35: Cranking Moments of Inertia (Nesterenko et al.)
- **File**: `35_Nesterenko_2023_Cranking_Inertia.md`
- **arXiv**: 2304.10873
- **Year**: 2023
- **Relevance**: MEDIUM
- **Tags**: cranking, moments of inertia, pairing collapse, 24Mg, 20Ne

**Summary**: Moments of inertia in 24Mg and 20Ne vs deformation and pairing. Pairing collapse at large beta produces anomalous dJ/dbeta < 0. Framework: "sd-shell / 24Mg regime" (Nazarewicz W2).

**Key Results**:
- Pairing collapse at beta > 0.5 (24Mg), > 0.6 (20Ne)
- Anomalous dJ/dbeta < 0 after pairing collapse
- IB, TV, adiabatic TDHF compared
- 24Mg as nuclear analog for framework

**Dependencies**: Builds on 15; framework: S38 nuclear analog

---

### Paper 36: Shape Coexistence in Pair Condensates (Lei et al.)
- **File**: `36_Lei_Qi_2024_Shape_Coexistence.md`
- **arXiv**: 2402.11276
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: shape coexistence, pair condensate, one-body entropy, nuclear structure

**Summary**: Shape coexistence across nuclear chart via variational pair condensates (VPC). Multiple minima frequent. One-body entropy S_{1b} quantifies beyond-Slater correlations: smallest mid-shell, largest near closures.

**Key Results**:
- VPC ansatz with optimized omega_{ij}
- Shape coexistence widespread (sd through pf shell)
- S_{1b}: zero for Slater, max for seniority-zero

**Dependencies**: Builds on 15, 35

---

### Paper 37: Pomeranchuk Instability from HOvHS on Kagome (Beidenkopf et al.)
- **File**: `37_Beidenkopf_2024_Pomeranchuk_VHS.md`
- **arXiv**: 2410.01994
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: Pomeranchuk instability, HOvHS, kagome, nematic order, STM

**Summary**: Distortion-induced HOvHS on Co3Sn2S2 kagome surface drives d-wave Pomeranchuk instability. DOS ~ |E|^{-1/4} from quartic dispersion. Nematic states break C_3 without translational breaking. STM visualization. Framework: S22c Pomeranchuk, S43 Van Hove.

**Key Results**:
- HOvHS from a_y -> 0 (quartic): DOS ~ |E|^{-1/4}
- d-wave Pomeranchuk from forward scattering
- Nematic cascade across ~100 meV
- Cubic Landau free energy F_3

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 37.1 | HOvHS dispersion | epsilon ~ a_x k_x^2 + b_y k_y^4 |
| eq 37.2 | Pomeranchuk order | O_1(k_x^2-k_y^2) + O_2(2k_xk_y) |

**Dependencies**: Builds on 11; verified: S22c F-1

---

### Paper 38: High-Order Van Hove Singularities and Flat Bands (Classen-Betouras)
- **File**: `38_Classen_Betouras_2024_VHS_Flat_Bands.md`
- **arXiv**: 2405.20226
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: HOVHS, flat bands, catastrophe theory, DOS divergence, moire, kagome

**Summary**: Systematic classification of HOvHS by catastrophe theory (corank, codimension, determinacy, winding). DOS ~ |E|^{-gamma} with gamma from scaling. Connection to flat bands via destructive interference. Framework: S43 gamma = -1/2.

**Key Results**:
- Classification by 4 catastrophe indices
- gamma = sum a_i - 1 from dispersion scaling
- Universal D_+/D_- ratio
- HOVHS from perturbed singular flat bands

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 38.1 | DOS divergence | rho ~ \|E\|^{-gamma}, gamma = sum a_i - 1 |

**Dependencies**: Builds on 11, 37; systematic VHS classification

---

### Paper 39: Non-Fermi-Liquid from Van Hove Singularity (Xing-Liu)
- **File**: `39_Xing_Liu_2024_NFL_VHS.md`
- **arXiv**: 2401.10707
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: non-Fermi liquid, marginal Fermi liquid, VHS, strange metal, pair density wave

**Summary**: NFL from 2D metal + critical magnons at VHS. Clean coupling: Sigma ~ |omega|^{1/2}. Disordered: Sigma ~ omega ln(1/omega) with T-linear resistivity. VHS dominates self-energy. Superconducting T_c and possible PDW.

**Key Results**:
- NFL: Sigma ~ |omega|^{1/2} (clean, VHS-dominated)
- MFL: Sigma ~ omega ln(1/|omega|) (disordered, strange metal)
- T-linear resistivity from MFL
- VHS suppresses hot-spot scattering

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 39.1 | NFL self-energy | Sigma ~ \|omega\|^{1/2} |
| eq 39.2 | MFL self-energy | Sigma ~ omega ln(1/\|omega\|) |

**Dependencies**: Builds on 11; parallel to 37, 38

---

### Paper 40: Dirac Operator Spectrum on Compact Manifolds (Zeng)
- **File**: `40_Zeng_2024_Dirac_Spectrum.md`
- **arXiv**: 2402.14247
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: Dirac spectrum, eigenvalue bounds, BLW formula, Reilly type, Atiyah-Singer

**Summary**: Eigenvalue bounds for D^2 on compact Riemannian manifolds in Euclidean space. BLW formula D^2 = nabla* nabla + R. Sum rules for consecutive eigenvalues on Dirac invariant subbundles. Universal bounds under curvature conditions. Framework: spectral bounds on D_K(tau).

**Key Results**:
- D^2 = nabla* nabla + (1/4)S (spinor case)
- Eigenvalue sum inequality involving H^2 and R
- Friedrich lower bound: Gamma^2 >= n/(4(n-1)) S_0
- Atiyah-Singer for upper bounds

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 40.1 | BLW formula | D^2 = nabla* nabla + R |
| eq 40.2 | Main theorem | sum Gamma_{j+k} <= (n+4)Gamma_j + curvature terms, Theorem 2.1 |

**Dependencies**: Connects to 02 (Dirac Landau levels); framework: D_K eigenvalue bounds

---

## Cross-Paper Equation Concordance

### Landau Free Energy F(eta)
Papers 04, 08, 09, 29 progressively generalize:
- **04**: F = F_0 + a(T-T_c) eta^2 + b eta^4 (scalar, uniform)
- **08**: f_s = alpha|psi|^2 + (beta/2)|psi|^4 + gauge-covariant gradient + B^2/(8pi) (complex, gauged)
- **09**: tau_0 dphi/dt = -dF/dphi + kappa nabla^2 phi + noise (dynamic, stochastic)
- **29**: Same as 08, applied to KZ defect production
- **Framework**: V_eff(tau) from spectral action = Landau F for Jensen parameter

### BCS Gap Equation
Papers 15, 16, 17, 25:
- **15**: Delta = V sum_k Delta/(2E_k) (mean field)
- **16**: Exact eigenvalues from Richardson equations (no gap equation)
- **17**: BCS as N -> infinity of Richardson solution
- **25**: Gap equation with crossover parameter (k_F a_F)^{-1}
- **Framework**: E_cond = -0.137, Delta_0 = 0.128 at fold (S43)

### Pomeranchuk Stability F_l > -(2l+1)
Papers 11, 37, 38:
- **11**: General condition for Fermi liquid stability
- **37**: Experimental d-wave Pomeranchuk at HOvHS
- **38**: Classification of HOvHS driving instabilities
- **Framework**: f(0,0)=-4.687 (UNSTABLE, S22c); GGE F_0=+0.060 (STABLE, S58)

### Kibble-Zurek Defect Density
Papers 09, 26, 29:
- **09**: tau ~ |T-T_c|^{-nu z} (critical slowing input)
- **29**: n_defect ~ (tau_Q/tau_0)^{-d nu/(1+nu z)} (KZ prediction)
- **26**: Verified across BCS-BEC crossover in Li-6
- **Framework**: sigma_KZ=0.831, xi_KZ=0.277 (3D Ising/Model A, S43)

### GGE Density Matrix
Papers 01, 16, 22, 23:
- **01**: rho = sum p_i |psi_i><psi_i| (density matrix concept)
- **16**: Richardson conserved integrals (quantities constraining GGE)
- **22**: rho_GGE = Z^{-1} exp(-sum lambda_m I_m) (construction)
- **23**: GETH: eigenstates with similar conserved quantities have similar observables
- **Framework**: 8 RG integrals, permanent non-thermal relic (S38)

### Acoustic Metric
Papers 05, 18, 19, 21:
- **05**: Two-fluid hydrodynamics (implicit metric)
- **18**: g^{mu nu} from superfluid phonon dynamics (explicit)
- **19**: Weyl + gauge + gravity from He-3 order parameter
- **21**: Seven-term potential from log-GPE (sub-Newtonian through FLRW)

### Richardson-Gaudin Conserved Charges
Papers 16, 17, 24:
- **16**: Exact eigenstates from pair rapidities
- **17**: R_l commuting conserved charges, three families
- **24**: Eigenvalue-based method, broken integrability extensions
- **Framework**: 8 conserved integrals in BCS on SU(3), S37-38

## Notation Conventions

| Symbol | Meaning | Papers |
|:---|:---|:---|
| eta, phi | Order parameter (scalar) | 04, 09 |
| psi, Psi | Complex order parameter / condensate wavefunction | 08, 05, 29, 21 |
| Delta | BCS gap | 15, 16, 17, 25, 34 |
| tau (Landau) | Relaxation time | 09, 29 |
| tau (framework) | Jensen deformation parameter | 04 (as s), framework |
| F_l^{s,a} | Dimensionless Landau parameters | 11, 12, 37 |
| m* | Effective mass (quasiparticle or Cooper pair) | 08, 11, 25 |
| xi | Coherence length (GL) or healing length (GPE) | 08, 29 |
| lambda | Penetration depth | 08, 13 |
| kappa | GL parameter lambda/xi | 08, 13 |
| E_k | Quasiparticle energy sqrt(epsilon_k^2+Delta^2) | 15, 25 |
| I_m | Conserved quantity (integral of motion) | 16, 17, 22, 23 |
| z | Dynamic critical exponent | 09, 29 |
| nu | Correlation length exponent | 04, 29 |
| v_c | Landau critical velocity | 05 |
| alpha_eff | Running coupling constant | 10 |
| N(0), N(E_F) | DOS at Fermi level | 11, 15 |
| g^{mu nu} | Acoustic / emergent metric | 18, 19, 21 |
| R_l | Richardson-Gaudin conserved charge | 17, 24 |
| rho | Density matrix | 01, 22, 23 |

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 04 | V'''(0) = -7.2 (cubic, first-order) | Yes | S17a SP-4 |
| 04 | d_int=8 > d_uc=4 (mean field exact) | Yes | S17a, structural |
| 08 | GL functional = GPE energy | Yes | phonon-exflation-sim |
| 10 | g_1/g_2 = e^{-2tau} from geometry | Yes | S17a B-1 |
| 11 | Pomeranchuk f(0,0) = -4.687 (UNSTABLE) | Yes | S22c F-1 |
| 11 | GGE Pomeranchuk: F_0=+0.060 (STABLE) | Yes | S58 POMERANCHUK-GGE-58 |
| 15 | Cooper instability: ANY g>0 (1D theorem) | Yes | S35 RG-BCS-35 |
| 15 | E_cond = -0.137, Delta_0 = 0.128 | Yes | S35, S43 |
| 16 | Richardson conserved integrals (8) | Yes | S37-38 |
| 17 | BCS-BEC: E_vac/E_cond = 28.8 | Yes | S37 |
| 22 | GGE permanence (non-thermal relic) | Yes | S38 |
| 29 | KZ defect scaling | Yes | S37-38 transit, S43 |
| 29 | KZ: sigma_KZ=0.831 (3D Ising) | Yes | S43 BCS-CLASS-43 |
| 37 | Pomeranchuk at VHS | Yes (analog) | S43 LIFSHITZ-43 |
| 40 | BLW formula D^2 = nabla* nabla + R | Yes | Tier 0 Dirac computations |
