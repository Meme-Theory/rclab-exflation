# Landau Paper Index

**Researcher**: Lev Davidovich Landau (and related condensed matter / integrable pairing / superfluid cosmology authors)
**Papers**: 40 (1927-2025)
**Primary domain**: Phase transitions, superfluidity, Fermi liquids, BCS pairing, Richardson-Gaudin integrability, Kibble-Zurek defects, GGE thermalization, BCS-BEC crossover, superfluid vacuum cosmology, spectral geometry
**Project relevance**: Core condensed matter physics for the phonon-exflation framework. Papers 01-14 are Landau originals establishing the intellectual foundations. Papers 15-40 are modern extensions directly used in Sessions 33-44: BCS on SU(3) fiber, Richardson-Gaudin integrability, GGE permanence, Kibble-Zurek transit, van Hove / Pomeranchuk instabilities, giant pairing vibrations, emergent spacetime from superfluid vacuum.

---

## Dependency Graph

```
LANDAU FOUNDATIONS (1927-1947)
  01 (density matrix) --> 06 (Landau damping, contour prescription)
  01 --> 11 (Fermi liquid, quasiparticle concept)
  02 (Landau levels) --> 13 (Abrikosov vortices, H_c2 from Landau levels)
  04 (phase transitions) --> 08 (GL superconductivity)
  04 --> 09 (LK relaxation, critical slowing)
  05 (superfluidity I) --> 07 (superfluidity II, revised roton)
  05 --> 12 (zero sound in Fermi liquid)

GL, FERMI LIQUID & QFT (1950-1958)
  08 (GL) --> 13 (Abrikosov vortices, kappa > 1/sqrt(2))
  08 --> 15 (BCS, microscopic derivation of GL)
  09 (LK relaxation) --> 21 (KZ mechanism, critical slowing + causality)
  10 (LAK running coupling) --> 14 (Landau singularities, analytic S-matrix)
  11 (Fermi liquid) --> 12 (zero sound)
  11 --> 26 (Pomeranchuk VHS kagome)
  11 --> 27 (VHS flat bands)
  11 --> 34 (non-Fermi liquid from VHS)

BCS & INTEGRABLE PAIRING (1957-2018)
  15 (BCS) --> 16 (Richardson exact solution)
  15 --> 22 (BCS-BEC crossover review)
  16 (Richardson) --> 17 (DPS RG review, Yang-Baxter)
  17 --> 33 (Claeys broken integrability)
  17 --> 20 (Rigol GGE founding)
  20 (GGE founding) --> 32 (Vidmar-Rigol GGE lattice review)

BCS-BEC CROSSOVER & FINITE SIZE (2018-2024)
  22 (Strinati review) --> 30 (gate-controlled 2D crossover)
  22 --> 28 (KZ in BCS-BEC)
  22 --> 36 (finite-size 2D crossover)
  28 (KZ in BCS-BEC) --> 21 (KZ mechanism)

GIANT PAIRING VIBRATIONS & NUCLEAR (2015-2025)
  15 (BCS) --> 23 (GPV experiment, 14C)
  23 --> 24 (GPV review, heavy nuclei)
  24 --> 25 (GPV fragmentation, many-body)
  15 --> 37 (Higgs response nuclear pair)
  15 --> 38 (cranking inertia, pairing collapse)
  38 --> 39 (shape coexistence, pair condensates)

VAN HOVE, POMERANCHUK & NON-FERMI LIQUID (2024)
  11 (Fermi liquid) --> 26 (Pomeranchuk VHS kagome)
  26 --> 27 (VHS flat bands review)
  27 --> 34 (NFL from VHS)

SUPERFLUID VACUUM & COSMOLOGY (2001-2023)
  05,07 (superfluidity) --> 19 (Volovik droplet monograph)
  19 --> 31 (Volovik superfluid analogies, Physics Reports)
  19 --> 35 (Zloshchastiev SVT emergent metric)
  19 --> 18 (Berezhiani-Khoury DM superfluidity)
  09 (LK relaxation) --> 21 (KZ mechanism)
  21 --> 29 (Enomoto-Matsuda LZ particle production)

SPECTRAL GEOMETRY (2024)
  40 (Zeng Dirac spectrum bounds) <-- independent
  40 --> framework tier0 eigenvalue computations
```

---

## Topic Map

### A. Quantum Foundations & Statistical Mechanics
Papers: 01, 06
Density matrix formalism (01) as the fundamental object for open quantum systems.
Landau damping (06) as collisionless energy transfer via phase mixing. Both provide
the conceptual infrastructure for describing the post-transit GGE relic state.

### B. Landau Phase Transition Theory
Papers: 04, 09
The order parameter concept, Landau free energy expansion, symmetry-breaking
classification (04). Time-dependent Ginzburg-Landau / Landau-Khalatnikov relaxation,
critical slowing down, dynamic critical exponent z (09). These two papers define the
language used throughout the framework: tau is the order parameter, the spectral action
is the Landau free energy, d_int=8 > d_uc=4 makes mean field exact.

### C. Superfluidity
Papers: 05, 07
Two-fluid model, phonon-roton spectrum, Landau critical velocity, second sound (05).
Revised roton parameters agreeing with neutron scattering to 3 significant figures (07).
Direct prototype for the phonon-exflation claim: particles as quasiparticle excitations
of a coherent ground state.

### D. Ginzburg-Landau Superconductivity & Vortices
Papers: 08, 13
GL free energy, coherence length xi, penetration depth lambda, kappa = lambda/xi
classification (08). Abrikosov vortex lattice, flux quantization Phi_0, type-II mixed
state (13). The GL functional IS the GPE energy functional. Vortices in the GPE
simulation are direct Abrikosov descendants.

### E. Fermi Liquid Theory & Zero Sound
Papers: 02, 11, 12
Landau levels and diamagnetic susceptibility (02). Quasiparticle concept, effective mass
m*/m = 1 + F_1^s/3, Pomeranchuk stability conditions F_l > -(2l+1) (11). Zero sound
as collisionless collective oscillation, Fermi surface deformation waves (12). Framework
Session 22c: Pomeranchuk instability confirmed with f_{0,0} = -4.687 < -3.

### F. Quantum Field Theory
Papers: 10, 14
Running coupling alpha_eff, Landau pole, triviality of QED, Moscow zero-charge (10).
Landau equations for Feynman diagram singularities, analytic S-matrix program,
Coleman-Norton theorem (14). Framework connection: gauge couplings from SU(3) geometry
(g_1/g_2 = e^{-2tau}), UV completion via KK spectrum.

### G. BCS Theory & Richardson-Gaudin Integrability
Papers: 15, 16, 17
BCS ground state, gap equation Delta_0 ~ exp(-1/VN(E_F)), Cooper instability as 1D
theorem (15). Richardson exact eigenstates via pair rapidities z_a, complete
integrability of pairing Hamiltonian (16). DPS review: Yang-Baxter structure, Bethe
ansatz, ultrasmall grain limit L/xi_GL << 1, conserved integrals I_k (17). These three
papers are the BACKBONE of framework Sessions 33-38: BCS on SU(3) fiber is a
Richardson-Gaudin integrable system with 8 conserved quantities.

### H. Generalized Gibbs Ensemble
Papers: 20, 32
Rigol-Olshanii founding paper: integrable systems relax to GGE, not Gibbs (20).
Vidmar-Rigol lattice review: generalized eigenstate thermalization, GGE universality,
boundaries of applicability (32). Framework prediction: post-transit relic is a permanent
GGE with 8 Richardson-Gaudin integrals. These papers provide the rigorous proof.

### I. Richardson-Gaudin Models & Broken Integrability
Paper: 33
Claeys thesis: unified framework for RG models, variational approach for broken
integrability, Floquet resonances, Yangian symmetry. Framework: off-Jensen perturbations
are weak integrability breaking in the Claeys sense.

### J. BCS-BEC Crossover & Finite Size
Papers: 22, 28, 30, 36
Strinati review of BCS-BEC crossover from cold atoms to nuclear (22). Ko experimental
KZ scaling across entire BCS-BEC crossover, universal exponent d*nu/(d*nu+z) = 0.25
(28). Gate-controlled 2D crossover in ZrNCl (30). Finite-size effects in 2D crossover,
gap suppression, BKT shift (36). Framework: E_vac/E_cond = 28.8 places it in BEC
regime. L/xi_GL = 0.031 is extreme finite-size limit.

### K. Giant Pairing Vibrations & Nuclear Structure
Papers: 23, 24, 25, 37, 38, 39
GPV first observation in 14C/15C via MAGNEX (23). GPV review for heavy nuclei,
fragmentation mechanism (24). GPV fragmentation from many-body coupling, 30-50% in main
peak for heavy nuclei (25). Higgs response and pair condensation energy via QRPA (37).
Cranking moments of inertia, pairing collapse at high deformation (38). Shape
coexistence as generic pairing-deformation competition (39). Framework: omega_att=1.430,
85.5% GPV concentration -- anti-fragmentation from integrability protection.

### L. Van Hove Singularities, Pomeranchuk & Non-Fermi Liquid
Papers: 26, 27, 34
Pomeranchuk instability from higher-order VHS on distorted kagome (26). VHS-flat band
unification review, interaction enhancement, design principles (27). NFL/MFL from VHS
coupled to critical bosons, pair-density-wave superconductivity (34). Framework Session
22c: B2 flat band hosts VHS, Pomeranchuk at f=-4.687, Jensen deformation ~8.4% is
analogous to kagome distortion 5-10%.

### M. Kibble-Zurek Mechanism & Cosmological Particle Production
Papers: 21, 29
Zurek's Kibble-Zurek scaling: defect density n ~ (tau_Q)^{-d*nu/(d*nu+z)} (21).
Enomoto-Matsuda exact WKB + Landau-Zener, Schwinger-instanton duality S_Schwinger =
S_inst (29). Framework S37-38: transit is a KZ quench, instanton gas with S_inst=0.069.
Schwinger-instanton duality confirmed at 1% (S_Schwinger=0.070 vs S_inst=0.069).

### N. Superfluid Vacuum & Emergent Spacetime
Papers: 18, 19, 31, 35
Berezhiani-Khoury DM superfluidity: phonons mediate MOND-like gravity, dual phase
(superfluid galaxies / normal clusters) (18). Volovik monograph: universe as helium
droplet, Weyl fermions from nodal points, gauge fields from Berry phase, cosmological
constant from gap energy (19). Volovik Physics Reports: superfluid analogies,
baryon-number violation via instantons, axial anomaly (31). Zloshchastiev SVT: explicit
metric derivation from GPE, speed of light from sound speed, gravity from quantum
pressure (35). Framework foundational paradigm: bottom-up emergence of spacetime,
particles, and forces from a superfluid substrate on SU(3).

### O. Spectral Geometry
Paper: 40
Zeng: extrinsic eigenvalue bounds for Dirac operator on compact manifolds,
Lichnerowicz-type and Reilly-type inequalities, dimension-independent universal bounds,
Atiyah-Singer index constraints. Framework: provides rigorous bounds on the Dirac
spectrum of SU(3) that validate tier0 numerical computations.

---

## Quick Reference

| # | Year | First Author | Short Title | Relevance |
|:--|:-----|:-------------|:------------|:----------|
| 01 | 1927 | Landau | Density matrix | MEDIUM |
| 02 | 1930 | Landau | Diamagnetism / Landau levels | MEDIUM |
| 03 | 1935 | Landau-Lifshitz | Domain walls / LL equation | MEDIUM |
| 04 | 1937 | Landau | Phase transitions / order parameter | **HIGH** |
| 05 | 1941 | Landau | Superfluidity I | **HIGH** |
| 06 | 1946 | Landau | Landau damping | MEDIUM |
| 07 | 1947 | Landau | Superfluidity II (revised) | MEDIUM |
| 08 | 1950 | Ginzburg-Landau | GL superconductivity | **HIGH** |
| 09 | 1954 | Landau-Khalatnikov | Sound absorption / TDGL | **HIGH** |
| 10 | 1954 | LAK | Running coupling / Landau pole | MEDIUM |
| 11 | 1956 | Landau | Fermi liquid theory | **HIGH** |
| 12 | 1957 | Landau | Zero sound | MEDIUM |
| 13 | 1957 | Abrikosov | Type-II vortices | MEDIUM |
| 14 | 1958 | Landau | Analytic vertex parts | LOW |
| 15 | 1957 | BCS | BCS superconductivity | **CRITICAL** |
| 16 | 1963 | Richardson | Exact pairing eigenstates | **CRITICAL** |
| 17 | 2004 | Dukelsky-Pittel-Sierra | RG review | **CRITICAL** |
| 18 | 2015 | Berezhiani-Khoury | DM superfluidity | MEDIUM |
| 19 | 2003 | Volovik | Universe in helium droplet | **HIGH** |
| 20 | 2007 | Rigol et al. | GGE founding | **CRITICAL** |
| 21 | 1985 | Zurek | Kibble-Zurek mechanism | **CRITICAL** |
| 22 | 2018 | Strinati et al. | BCS-BEC crossover review | **HIGH** |
| 23 | 2015 | Cappuzzello et al. | GPV in 14C/15C | HIGH |
| 24 | 2019 | Fortunato et al. | GPV heavy nuclei | MEDIUM |
| 25 | 2025 | (contemporary) | GPV fragmentation | HIGH |
| 26 | 2024 | Beidenkopf et al. | Pomeranchuk VHS kagome | HIGH |
| 27 | 2024 | Classen-Betouras | VHS flat bands review | HIGH |
| 28 | 2019 | Ko et al. | KZ in BCS-BEC | HIGH |
| 29 | 2022 | Enomoto-Matsuda | WKB / LZ particle production | **HIGH** |
| 30 | 2021 | Nakagawa et al. | Gate-controlled crossover | MEDIUM |
| 31 | 2001 | Volovik | Superfluid analogies | **HIGH** |
| 32 | 2016 | Vidmar-Rigol | GGE lattice review | HIGH |
| 33 | 2018 | Claeys | RG broken integrability | HIGH |
| 34 | 2024 | Xing-Liu | NFL from VHS | MEDIUM |
| 35 | 2023 | Zloshchastiev | Emergent metric SVT | HIGH |
| 36 | 2024 | Lanaro-Bighin | Finite-size BCS-BEC 2D | MEDIUM |
| 37 | 2023 | Takahashi et al. | Higgs response nuclear | HIGH |
| 38 | 2023 | Nesterenko et al. | Cranking inertia deformed | MEDIUM |
| 39 | 2024 | Lei-Qi et al. | Shape coexistence | MEDIUM |
| 40 | 2024 | Zeng | Dirac spectrum bounds | MEDIUM |

---

## Paper Entries

### Paper 01: Density Matrix (Landau 1927)
- **File**: `01_1927_Landau_Density_matrix_wave_mechanics.md`
- **Key content**: Density operator rho = sum p_i |psi_i><psi_i|, von Neumann equation, partial trace, decoherence. Independent of von Neumann at age 19.
- **Key equations**: <A> = Tr(rho*A); S_vN = -Tr(rho ln rho); purity Tr(rho^2)
- **Framework use**: GGE relic density matrix, spectral action as thermal partition function

### Paper 02: Diamagnetism / Landau Levels (Landau 1930)
- **File**: `02_1930_Landau_Diamagnetism_of_metals.md`
- **Key content**: Landau quantization E_n = hbar*omega_c*(n+1/2), degeneracy = flux quanta, chi_L = -chi_Pauli/3, dHvA oscillations
- **Key equations**: E(n,k_z) = hbar*omega_c*(n+1/2) + hbar^2*k_z^2/(2m)
- **Framework use**: KK spectrum as "internal Landau levels", degeneracy lifting by Jensen deformation

### Paper 03: Domain Walls / LL Equation (Landau-Lifshitz 1935)
- **File**: `03_1935_Landau_Lifshitz_Magnetic_permeability_dispersion.md`
- **Key content**: LL equation dM/dt = -gamma*(M x H_eff) + damping, Bloch wall theta(x) = 2*arctan(exp(x/delta)), delta = sqrt(A/K), sigma = 4*sqrt(A*K)
- **Key equations**: LL equation; wall width delta = sqrt(A/K_u); wall energy sigma = 4*sqrt(A*K_u)
- **Framework use**: Topological defect classification pi_0(domain walls), pi_1(vortices), pi_2(skyrmions)

### Paper 04: Phase Transitions / Order Parameter (Landau 1937)
- **File**: `04_1937_Landau_Phase_transitions_order_parameter.md`
- **Key content**: Universal theory of symmetry breaking. Order parameter eta, F(eta) = a(T-T_c)*eta^2 + b*eta^4, mean-field exponents beta=1/2, gamma=1, Ginzburg criterion, cubic term forces first-order.
- **Key equations**: F = F_0 + a_0*(T-T_c)*eta^2 + b*eta^4; eta_0 = sqrt(a_0*(T_c-T)/(2b))
- **Framework use**: tau is the order parameter; V_eff(tau) is the Landau free energy; d_int=8 > d_uc=4 means mean-field exact; V'''(0)=-7.2 forces first-order

### Paper 05: Superfluidity I (Landau 1941)
- **File**: `05_1941_Landau_Superfluidity_helium_II.md`
- **Key content**: Two-fluid model, phonon branch epsilon=c*p, roton minimum epsilon=Delta+(p-p_0)^2/(2mu*), critical velocity v_c = min(epsilon/p), second sound
- **Key equations**: v_c = min_p[epsilon(p)/p]; u_2 = sqrt(rho_s*s^2*T/(rho_n*c_p))
- **Framework use**: THE physical prototype. Phonon-roton spectrum = particle mass spectrum; v_c = vacuum stability

### Paper 06: Landau Damping (Landau 1946)
- **File**: `06_1946_Landau_Plasma_oscillations_damping.md`
- **Key content**: Initial-value approach to Vlasov equation, Landau contour prescription, collisionless damping gamma ~ exp(-1/(2k^2*lambda_D^2)), phase mixing vs dissipation, plasma echo
- **Key equations**: gamma = -sqrt(pi/8)*(omega_p/(k*lambda_D)^3)*exp(-1/(2k^2*lambda_D^2))
- **Framework use**: Resonant energy transfer without collisions; phase mixing = decoherence; i*epsilon prescription

### Paper 07: Superfluidity II (Landau 1947)
- **File**: `07_1947_Landau_Superfluidity_helium_II_sequel.md`
- **Key content**: Revised roton: Delta/k_B=8.6 K, p_0/hbar=1.92 A^-1, mu*=0.16 m_He. Confirmed by neutron scattering 14 years later to 3 figures.
- **Key equations**: rho_n^{rot} ~ T^{-1/2}*exp(-Delta/(k_B*T)); phonon-roton crossover at T~0.6 K
- **Framework use**: Roton minimum at finite p_0 maps to massive KK modes at nonzero internal quantum numbers

### Paper 08: GL Superconductivity (Ginzburg-Landau 1950)
- **File**: `08_1950_Ginzburg_Landau_Superconductivity.md`
- **Key content**: GL free energy with complex order parameter psi, gauge-covariant gradient, xi = coherence length, lambda = penetration depth, kappa = lambda/xi, Type I/II at kappa = 1/sqrt(2), flux quantum Phi_0 = h/(2e), Higgs mechanism = Meissner effect
- **Key equations**: f_s = alpha|psi|^2 + (beta/2)|psi|^4 + (1/2m*)|(-ihbar*grad - e*A/c)*psi|^2 + B^2/(8pi)
- **Framework use**: GL functional IS the GPE energy. xi = healing length = compactification scale. Meissner = gauge boson mass.

### Paper 09: LK Relaxation / TDGL (Landau-Khalatnikov 1954)
- **File**: `09_1954_Landau_Khalatnikov_Sound_absorption_phase_transitions.md`
- **Key content**: dphi/dt = -(1/tau_0)*(dF/dphi), critical slowing tau ~ |T-T_c|^{-nu*z}, anomalous sound absorption, Hohenberg-Halperin classification (Models A-H)
- **Key equations**: tau = tau_0/(a*|T-T_c|); dynamic scaling tau ~ xi^z
- **Framework use**: Dynamic universality class of exflation transition (Model A, z=2.024). Phonon freeze-out at omega*tau~1.

### Paper 10: LAK Running Coupling (Landau-Abrikosov-Khalatnikov 1954)
- **File**: `10_1954_Landau_Abrikosov_Khalatnikov_Asymptotic_Green_function.md`
- **Key content**: Leading-log summation, alpha_eff = alpha/(1-(alpha/3pi)*ln(q^2/m^2)), Landau pole at Lambda~m*exp(3pi/(2alpha)), QED triviality, Moscow zero-charge
- **Key equations**: beta(alpha) = (2*alpha^2)/(3*pi); Lambda_Landau = m*exp(3pi/(2alpha))
- **Framework use**: Geometric running g_1/g_2 = e^{-2tau} replaces loop running. UV completion by KK spectrum.

### Paper 11: Fermi Liquid Theory (Landau 1956)
- **File**: `11_1956_Landau_Fermi_liquid_theory.md`
- **Key content**: Adiabatic continuity, quasiparticle concept, effective mass m*/m = 1+F_1^s/3, lifetime 1/tau ~ (epsilon-epsilon_F)^2, Landau parameters F_l^{s,a}, Pomeranchuk stability F_l > -(2l+1)
- **Key equations**: m*/m = 1 + F_1^s/3; chi/chi_free = (m*/m)/(1+F_0^a); F_l^{s,a} > -(2l+1)
- **Framework use**: SM particles as quasiparticles of compactification. Pomeranchuk instability (S22c: f=-4.687). Central philosophical claim.

### Paper 12: Zero Sound (Landau 1957)
- **File**: `12_1957_Landau_Oscillations_Fermi_liquid.md`
- **Key content**: Collisionless collective mode propagating via self-consistent mean field, v_0 > v_F, observed in He-3 at T<100 mK. Zero-sound/first-sound crossover at omega*tau~1.
- **Key equations**: 1 = (F_0^s/2)*[1 + (u/2)*ln((u+1)/(u-1))], u = v_0/v_F
- **Framework use**: Phonon modes of condensate = zero-sound analogs. Collisionless-to-hydrodynamic crossover = confinement.

### Paper 13: Abrikosov Vortices (Abrikosov 1957)
- **File**: `13_1957_Abrikosov_Type_II_superconductors_vortices.md`
- **Key content**: kappa > 1/sqrt(2) gives negative surface energy, vortex lattice (triangular), H_c1, H_c2 = Phi_0/(2pi*xi^2), flux quantization
- **Key equations**: H_c2 = Phi_0/(2pi*xi^2); epsilon_1 = (Phi_0/(4pi*lambda))^2*ln(kappa)
- **Framework use**: BEC vortices = Abrikosov descendants. Vortex-antivortex binding determines D/H analog.

### Paper 14: Analytic Vertex Parts (Landau 1958)
- **File**: `14_1958_Landau_Analytic_properties_vertex_parts.md`
- **Key content**: Landau equations alpha_i*(q_i^2-m_i^2)=0, singularities when internal particles go on-shell. Coleman-Norton theorem. Cutkosky rules. Mandelstam representation.
- **Key equations**: Landau eqs: alpha_i*(q_i^2-m_i^2)=0; sum(alpha_i*q_i)=0 per loop
- **Framework use**: Analytic structure of spectral action S(tau). Level crossings as Landau singularities.

### Paper 15: BCS Theory (Bardeen-Cooper-Schrieffer 1957)
- **File**: `15_1957_Bardeen_Cooper_Schrieffer_BCS_Theory_Superconductivity.md`
- **Key content**: Cooper instability (1D theorem: any g>0), BCS ground state |BCS> = prod(u_k + v_k c^dag c^dag)|0>, gap equation Delta_0 = 2*omega_D*exp(-1/VN(E_F)), quasiparticle energy E_k = sqrt(epsilon_k^2+Delta^2), condensation energy, specific heat jump 1.43
- **Key equations**: Delta_0 = 2*hbar*omega_D*exp(-1/(V*N(E_F))); k_B*T_c = 1.13*hbar*omega_D*exp(-1/(V*N(E_F)))
- **Framework use**: Phonon-exflation IS BCS on SU(3) fiber. E_cond=-0.115, gap=0.137, K_7 pairing. Cooper instability is 1D theorem (S35 RG-BCS-35).

### Paper 16: Richardson Exact Solution (Richardson 1963)
- **File**: `16_1963_Richardson_Exact_Eigenstates_Pairing_Hamiltonian.md`
- **Key content**: Pairing Hamiltonian is completely integrable. Pair rapidities z_a satisfy Richardson equations. E = sum z_a. Yang-Baxter structure. Seniority conservation. No phase transition (analytic in G).
- **Key equations**: Richardson eqs: epsilon_a + G/2 = sum_{b!=a} 2G/(z_a-z_b) + sum_i G/(z_a-epsilon_i)
- **Framework use**: The 8 Richardson-Gaudin conserved integrals determine the post-transit GGE. Integrability guarantees non-thermalization (S38).

### Paper 17: DPS Richardson-Gaudin Review (Dukelsky-Pittel-Sierra 2004)
- **File**: `17_2004_Dukelsky_Pittel_Sierra_Richardson_Gaudin_Review.md`
- **Key content**: Yang-Baxter equation, Bethe ansatz, ultrasmall grain limit L/xi_GL << 1, conserved integrals I_k, pair vibrations, form factors as Cauchy determinants, thermodynamic Bethe ansatz
- **Key equations**: I_k = sum_a 1/(z_a - epsilon_k); Yang-Baxter: R_12 T_1 T_2 = T_2 T_1 R_12
- **Framework use**: L/xi_GL = 0.031 is ultrasmall grain. 8 conserved integrals. omega_att = 1.430 = universal RG pair vibration mode.

### Paper 18: DM Superfluidity (Berezhiani-Khoury 2015)
- **File**: `18_2015_Berezhiani_Khoury_Dark_Matter_Superfluidity.md`
- **Key content**: DM as superfluid at galactic scales (phonons mediate MOND-like force), normal phase at cluster scales. Bogoliubov spectrum, c_s ~ 100 m/s, vortex lattice in rotating galaxies.
- **Key equations**: omega(k) = sqrt(c_s^2*k^2 + k^4/(4m^2)); a_0 from phonon scattering
- **Framework use**: Structural parallel -- phonons mediate effective forces. Phase-dependent dynamics (superfluid vs normal).

### Paper 19: Universe in a Helium Droplet (Volovik 2003)
- **File**: `19_2003_Volovik_Universe_Helium_Droplet_Emergent_Spacetime.md`
- **Key content**: Emergent gravity, gauge fields, and Weyl fermions from He-3 superfluid. 3 pairs of Weyl points = 3 generations. Berry-phase gauge fields. Cosmological constant from gap energy Delta^4. CPT from topology.
- **Key equations**: E(p) ~ v_F|p-p_W| near Weyl points; Lambda ~ Delta^4
- **Framework use**: Foundational paradigm. SU(3) internal geometry = superfluid substrate. Particles = quasiparticles. Spacetime = emergent.

### Paper 20: GGE Founding (Rigol-Dunjko-Yurovsky-Olshanii 2007)
- **File**: `20_2007_Rigol_Dunjko_Yurovsky_Olshanii_GGE_Integrable_Systems.md`
- **Key content**: Integrable systems relax to GGE, not Gibbs. rho_GGE = Z^{-1}*exp(-sum lambda_k I_k). Lagrange multipliers from initial conditions. Diagonal ensemble = GGE. Verified for Lieb-Liniger.
- **Key equations**: rho_GGE = Z^{-1}*exp(-sum_k lambda_k*I_k); <I_k>_initial = <I_k>_GGE
- **Framework use**: Post-transit relic IS a GGE. 8 conserved integrals -> permanent non-thermal state. N_eff=2.48 (not 5.5) because GGE constrains more than energy alone.

### Paper 21: Kibble-Zurek Mechanism (Zurek 1985)
- **File**: `21_1985_Zurek_Kibble_Cosmological_Mechanism_Defect_Formation.md`
- **Key content**: Defect density n ~ (tau_Q)^{-d*nu/(d*nu+z)} from causality during symmetry breaking. Freezeout at xi = d_horizon. Universal, independent of microscopic details. Coarsening l(t) ~ t^{1/z}.
- **Key equations**: n_defect ~ xi(t_freeze)^{-d}; xi ~ |T-T_c|^{-nu}; tau ~ xi^z
- **Framework use**: Transit from tau=0 to tau_c is a KZ quench (S37-38). 59.8 quasiparticle pairs produced. P_exc=1.000 (sudden quench limit).

### Paper 22: BCS-BEC Crossover Review (Strinati et al. 2018)
- **File**: `22_2018_Strinati_BCS_BEC_Crossover.md`
- **Key content**: Leggett parameter xi = -1/(k_F*a_s), BCS (xi<<-1) to BEC (xi>>1), unitary gas at xi=0. Pseudogap above T_c. Universal E_0/E_F at unitarity. Quantum critical exponents.
- **Key equations**: Delta_0 ~ 2*omega_D*exp(-pi/(2g*N(E_F))); E_0/E_F = -0.42 (unitary)
- **Framework use**: E_vac/E_cond = 28.8 places framework in BEC regime. Fluctuations dominate. Pseudogap = no Goldstone above fold.

### Paper 23: GPV in 14C/15C (Cappuzzello et al. 2015)
- **File**: `23_2015_Cappuzzello_Giant_Pairing_Vibration_14C_15C.md`
- **Key content**: First experimental GPV observation. E_GPV ~ 9.4 MeV in 14C, L^P=0+ monopole, width ~2 MeV, via MAGNEX spectrometer. Cross section ~10 ub/sr.
- **Framework use**: Experimental benchmark. Framework GPV omega_att=1.430 with 85.5% concentration vs nuclear 10-50%.

### Paper 24: GPV Heavy Nuclei (Fortunato et al. 2019)
- **File**: `24_2019_Fortunato_GPV_Heavy_Nuclei.md`
- **Key content**: GPV predicted at 15-25 MeV in Sn/Pb but not observed. Strength fragmentation over 3-5 RPA eigenvalues. Q-value mismatch hinders detection.
- **Framework use**: Fragmentation mechanism calibrates framework's anti-fragmentation (85.5% vs 40%).

### Paper 25: GPV Fragmentation (2025)
- **File**: `25_2025_GPV_Fragmentation_Many_Body.md`
- **Key content**: Doorway-state mechanism fragments GPV into 4-6 peaks. Spreading width Gamma ~ 2-5 MeV. Strongest component 30-50%. Configuration-space convergence beyond 2p-2h.
- **Key equations**: Gamma_spread = 2pi*rho_d*V_d^2; S_n = |<n|Q^dag|GS>|^2
- **Framework use**: Framework's 85.5% single-mode concentration requires integrability protection (absent in nuclear systems).

### Paper 26: Pomeranchuk VHS Kagome (Beidenkopf et al. 2024)
- **File**: `26_2024_Beidenkopf_Pomeranchuk_VHS_Kagome.md`
- **Key content**: STM observation of higher-order VHS on distorted Co3Sn2S2 kagome surface. Logarithmic DOS divergence. Spontaneous Pomeranchuk instability (nematic). Domains 10-50 nm.
- **Key equations**: F_s^a = -1 (instability threshold); distortion lambda ~ 5-10%
- **Framework use**: Experimental validation. Framework S22c: f=-4.687 (instability). Jensen deformation ~8.4% comparable to kagome distortion.

### Paper 27: VHS Flat Bands Review (Classen-Betouras 2024)
- **File**: `27_2024_Classen_Betouras_VHS_Flat_Bands.md`
- **Key content**: Classification of VHS orders (1st through infinite). Flat bands = infinite-order VHS. Interaction enhancement at VHS. Design principles for moiré/kagome materials.
- **Key equations**: N(E) ~ |E-E_s|^alpha; flat band alpha -> infinity; T_c enhanced 10-100x near VHS
- **Framework use**: B2 sector flat band = infinite-order VHS = maximal interaction amplification. Pomeranchuk inevitable.

### Paper 28: KZ in BCS-BEC (Ko et al. 2019)
- **File**: `28_2019_Ko_Kibble_Zurek_BCS_BEC.md`
- **Key content**: Universal KZ scaling n_vortex ~ tau_Q^{-0.25} across entire BCS-BEC crossover including unitary point. Microscopic details (fermion vs boson) irrelevant.
- **Key equations**: n_defect ~ tau_Q^{-d*nu/(d*nu+z)}; exponent = 0.25 +/- 0.03
- **Framework use**: KZ scaling is universal. Framework transit necessarily produces defects following KZ laws regardless of crossover position.

### Paper 29: WKB / Landau-Zener (Enomoto-Matsuda 2022)
- **File**: `29_2022_Enomoto_Matsuda_WKB_Landau_Zener_Particle_Production.md`
- **Key content**: Exact WKB for cosmological particle production. P_LZ = exp(-2pi*Delta^2/(hbar*v_dot)). Schwinger-instanton duality: S_inst = LZ phase. P_LZ ~ 0.999 for rapid transitions.
- **Key equations**: P_LZ = exp(-2pi*Delta^2/(hbar*|v_dot|)) = exp(-S_inst/hbar)
- **Framework use**: S37 duality confirmed: S_Schwinger=0.070 = S_inst=0.069. P_exc=1.000 (sudden quench). Near-complete particle production.

### Paper 30: Gate-Controlled 2D Crossover (Nakagawa et al. 2021)
- **File**: `30_2021_Nakagawa_Kasahara_Gate_Controlled_BCS_BEC_Crossover.md`
- **Key content**: Complete BCS-BEC crossover in solid-state 2D superconductor (ZrNCl). T_c/E_F reaches BEC bound ~0.2. Pseudogap above T_c. No first-order transition.
- **Framework use**: Density-tuning analog for tau-sweep. Pseudogap = no Goldstone above fold. Finite-size regime.

### Paper 31: Superfluid Analogies (Volovik 2001)
- **File**: `31_2001_Volovik_Superfluid_Analogies_Cosmological_Phenomena.md`
- **Key content**: Systematic mapping of superfluid He-3 onto cosmology. Weyl fermions at nodal points. Gauge fields from Berry phase. Metric from order parameter. Axial anomaly reproduced. Baryon violation via instantons.
- **Key equations**: Effective metric g_mu_nu from pairing tensor; Chern-Simons anomalous current
- **Framework use**: Direct template for framework cosmology. Instantons = vortex-loop tunneling. Metric = order parameter geometry.

### Paper 32: GGE Lattice Review (Vidmar-Rigol 2016)
- **File**: `32_2016_Vidmar_Rigol_Generalized_Gibbs_Ensembles_Integrable_Lattice.md`
- **Key content**: Generalized eigenstate thermalization (GEET). GGE universality across XXX, Lieb-Liniger, sine-Gordon, etc. Subsystem observables equilibrate to GGE. Slow revivals ~1/sqrt(t). Breaking of GGE by weak perturbations.
- **Framework use**: Standard reference for GGE phenomenology. Off-Jensen perturbations = weak integrability breaking (slow approach to Gibbs).

### Paper 33: RG Broken Integrability (Claeys 2018)
- **File**: `33_2018_Claeys_Richardson_Gaudin_Models_Broken_Integrability.md`
- **Key content**: Unified RG framework. Variational approach for non-integrable perturbations. Floquet resonances. Yangian symmetry. 8+ conserved charges. Phase transition at critical perturbation strength.
- **Framework use**: Off-Jensen = weak integrability breaking in Claeys sense. Variational mixing of RG configurations. Floquet for slow cosmological driving.

### Paper 34: NFL from VHS (Xing-Liu 2024)
- **File**: `34_2024_Xing_Liu_Non_Fermi_Liquid_Van_Hove_Singularity.md`
- **Key content**: VHS coupled to critical magnons produces NFL. Disorder causes crossover to marginal FL (rho ~ T). Pair-density-wave superconductivity from nesting. Kinetic (one-particle) origin of NFL scaling.
- **Framework use**: Fold-point VHS in Dirac spectrum may induce NFL behavior. Pair-density-wave = off-Jensen condensate alternate picture.

### Paper 35: Emergent Metric SVT (Zloshchastiev 2023)
- **File**: `35_2023_Zloshchastiev_Emergent_Spacetime_Metric_SVT.md`
- **Key content**: Explicit derivation: GPE -> Madelung decomposition -> effective metric ds^2 = -c_s^2 dt^2 + (dr - v_s dt)^2. Speed of light = sound speed (derived, not postulated). Gravity = quantum pressure. Equivalence principle automatic.
- **Key equations**: c_eff = sqrt(g*n_0/m); Phi_grav = -(hbar^2/2m^2)*nabla^2(sqrt(n_0))/sqrt(n_0)
- **Framework use**: c_phonon = c (S42 prediction). Metric from K_7 BCS order parameter geometry. Gravity = quantum pressure of Cooper pair condensate.

### Paper 36: Finite-Size 2D BCS-BEC (Lanaro-Bighin 2024)
- **File**: `36_2024_Lanaro_Bighin_Finite_Size_BCS_BEC_Crossover.md`
- **Key content**: Gap scales Delta(L) = Delta_inf*(1+O(1/L)). Chemical potential shifts ~ln(L)/L^2. BKT transition shifts T_BKT(L) = T_BKT(inf)*(1-A/(L*ln(L))). Quantum fluctuations mandatory in finite 2D.
- **Framework use**: L/xi_GL = 0.031 is extreme finite-size. Gap suppressed by confinement. BKT destroyed in 0D limit -> permanent GGE.

### Paper 37: Higgs Response Nuclear Pair (Takahashi-Matsuda-Matsuo 2023)
- **File**: `37_2023_Takahashi_Matsuda_Matsuo_Higgs_Response_Nuclear_Pair.md`
- **Key content**: Higgs operator O_H = sum c^dag c^dag + h.c., QRPA linear response, strength sum m_1 ~ Delta^2*N_pairs, static polarizability chi_0 ~ 1/Delta, E_cond extractable from m_1/chi_0.
- **Key equations**: S(omega) = sum_n |<n|O_H|0>|^2 delta(omega-E_n); omega_H ~ 2*sqrt(Delta^2+xi^2)
- **Framework use**: Higgs mode in K_7 BCS. E_cond=-0.115 extractable from Higgs response. Fragmentation from finite size.

### Paper 38: Cranking Inertia Deformed Nuclei (Nesterenko et al. 2023)
- **File**: `38_2023_Nesterenko_Mardyban_Moments_Inertia_Deformed_Nuclei.md`
- **Key content**: Moment of inertia DECREASES at high deformation (beta > 0.55) due to pairing collapse. sd-shell nuclei (24Mg, 20Ne). Single particle-hole dominance after pairing collapse.
- **Framework use**: Fold = pairing collapse point. Kapitza ratio 0.03 = inverted Born-Oppenheimer (pair vibration inertia << geometric inertia). sd-shell analog to K_7 (8 states).

### Paper 39: Shape Coexistence (Lei-Qi et al. 2024)
- **File**: `39_2024_Lei_Qi_Shape_Coexistence_Nuclear_Pair_Condensates.md`
- **Key content**: Shape coexistence is generic in even-even nuclei. Entropy-like pairing measure S_pair minimal mid-shell, maximal near closure. Angular-momentum projected CI. Predicted new coexisting bands.
- **Framework use**: Pairing-deformation competition = framework's Jensen (pairing) vs off-Jensen (deformation). Shape coexistence at fold. Configuration mixing mandatory.

### Paper 40: Dirac Spectrum Bounds (Zeng 2024)
- **File**: `40_2024_Zeng_Spectrum_Dirac_Operator_Compact_Manifolds.md`
- **Key content**: Extrinsic eigenvalue bounds for D^2 on compact manifolds. Lichnerowicz: lambda_1^2 >= n*R_min/(4(n-1)). Reilly-type bounds via isoperimetric ratio. Dimension-independent universal bounds. Anghel's result generalized.
- **Key equations**: D^2 = -Delta + R/4; sum mu_k <= f(n, geometry); Einstein manifolds saturate bounds
- **Framework use**: Rigorous bounds on Dirac spectrum of SU(3). Validates tier0 computations. Einstein manifold = fold geometry.

---

## Cross-Paper Equation Concordance

### BCS Gap Equation
- Paper 15 (BCS): Delta_0 = 2*hbar*omega_D * exp(-1/(V*N(E_F)))
- Paper 16 (Richardson): E = sum_a z_a, where z_a satisfy Richardson equations
- Paper 17 (DPS): Gap from Yang-Baxter transfer matrix
- Paper 22 (Strinati): 1 = -(1/2) sum_k V_k/E_k tanh(E_k/2T)
- Framework: E_cond = -0.115 at corrected van Hove (S35)

### Landau Free Energy / Order Parameter
- Paper 04: F = F_0 + a(T-T_c)*eta^2 + b*eta^4
- Paper 08 (GL): f_s = alpha|psi|^2 + (beta/2)|psi|^4 + gradient + gauge
- Paper 09 (LK): dphi/dt = -(1/tau_0)*(dF/dphi), tau ~ |T-T_c|^{-nu*z}
- Framework: V_eff(tau) = spectral action on Jensen-deformed SU(3)

### Pomeranchuk Stability
- Paper 11: F_l^{s,a} > -(2l+1) for all l
- Paper 26: F_s^a < -1 triggers nematic instability at VHS
- Paper 27: Flat band = infinite-order VHS, maximal interaction enhancement
- Framework S22c: f_{0,0} = -4.687 < -3 (instability confirmed)

### Effective Mass
- Paper 11: m*/m = 1 + F_1^s/3
- Paper 07: mu* = 0.16 m_He (roton effective mass)
- Framework: Dirac eigenvalue ratios at tau=0.15 give phi_paasch = 1.531580

### Running Coupling / Landau Pole
- Paper 10: alpha_eff = alpha / (1 - (alpha/3pi)*ln(q^2/m^2))
- Paper 10: Lambda_Landau = m*exp(3pi/(2alpha))
- Framework S17a: g_1/g_2 = e^{-2tau} (geometric running, not loop)

### Kibble-Zurek Defect Density
- Paper 21: n_defect ~ (tau_Q)^{-d*nu/(d*nu+z)}
- Paper 28: Universal exponent 0.25 across BCS-BEC crossover
- Framework S38: 59.8 quasiparticle pairs from sudden quench, P_exc = 1.000

### Landau-Zener / Schwinger-Instanton Duality
- Paper 29: P_LZ = exp(-2pi*Delta^2/(hbar*|v_dot|)) = exp(-S_inst/hbar)
- Framework S37: S_Schwinger = 0.070, S_inst = 0.069 (duality at 1%)

### GGE Density Matrix
- Paper 20: rho_GGE = Z^{-1} exp(-sum_k lambda_k I_k)
- Paper 32: Diagonal ensemble = GGE for integrable systems
- Paper 33: 8+ conserved charges in RG models
- Framework S38: rho_relic = GGE with 8 Richardson-Gaudin integrals

### Superfluid Critical Velocity
- Paper 05: v_c = min_p[epsilon(p)/p]
- Paper 19: Weyl fermions emerge at nodal points of gap
- Paper 35: c_eff = sqrt(g*n_0/m) in SVT

### GL Parameter & Type Classification
- Paper 08: kappa = lambda/xi; Type I < 1/sqrt(2) < Type II
- Paper 13: H_c2 = Phi_0/(2pi*xi^2), Phi_0 = h/(2e)
- Framework: kappa_EW = m_W/m_H ~ 0.64 (near Bogomolnyi)

### GPV Frequency & Strength
- Paper 23: E_GPV ~ 2*Delta_0 + omega_collective, observed 9.4 MeV in 14C
- Paper 25: Main peak 30-50% in heavy nuclei, fragmented 5-7 peaks
- Framework S37: omega_att = 1.430, 85.5% in single coherent mode

### Emergent Metric from Superfluid
- Paper 19: g_mu_nu from tensor order parameter
- Paper 31: Effective Einstein equations from hydrodynamics
- Paper 35: ds^2 = -c_s^2 dt^2 + (dr - v_s dt)^2

### Dirac Spectrum Bounds
- Paper 40: lambda_1^2 >= n*R_min/(4(n-1)) (Lichnerowicz)
- Paper 40: D^2 = -Delta_spin + R/4
- Framework S07-10: Tier0 eigenvalue computations on SU(3) with Jensen deformation

---

## Notation Conventions

| Symbol | Meaning | Papers |
|:-------|:--------|:-------|
| eta, phi | Order parameter | 04, 09 |
| psi | GL/GPE complex order parameter | 08, 13 |
| Delta | Superconducting/pairing gap | 08, 15, 16, 22 |
| F_l^{s,a} | Landau parameters (dimensionless) | 11, 12 |
| m* | Effective mass | 11, 07 |
| kappa | GL parameter lambda/xi | 08, 13 |
| z_a | Richardson pair rapidities | 16, 17 |
| I_k | Richardson-Gaudin conserved integrals | 16, 17, 20, 32 |
| lambda_k | GGE Lagrange multipliers | 20, 32 |
| tau_Q | Quench timescale | 21, 28 |
| P_LZ | Landau-Zener transition probability | 29 |
| S_inst | Instanton action | 29, 31 |
| c_s | Sound speed / effective light speed | 05, 18, 35 |
| N(E_F) | Density of states at Fermi level | 11, 15, 26, 27, 34 |
| omega_c | Cyclotron frequency | 02 |
| alpha_eff | Running coupling constant | 10 |
| beta(alpha) | QED beta function | 10 |
| rho_s, rho_n | Superfluid / normal fluid density | 05, 07 |
| xi | Coherence / healing length | 08, 13, 36 |
| lambda | Penetration depth | 08, 13 |
| z | Dynamic critical exponent | 09, 21, 28 |
| nu | Correlation length critical exponent | 04, 09, 21, 28 |
| G | Pairing coupling strength | 16, 17, 33 |
| g | Contact interaction (GPE) | 35, 36 |

---

## Computational Verification Status

| Paper | Result Used in Framework | Session | Status |
|:------|:------------------------|:--------|:-------|
| 04 | V'''(0) = -7.2 (first-order by cubic term) | S17a | VERIFIED |
| 08 | GL functional = GPE energy | S01-sim | STRUCTURAL |
| 09 | tau ~ |T-T_c|^{-nu*z}, dynamic z | S43 | z=2.024 (Model A) |
| 11 | Pomeranchuk F_l > -(2l+1) | S22c | f_{0,0}=-4.687 PASS |
| 15 | BCS gap, Cooper instability 1D theorem | S35 | RG-BCS-35 PASS |
| 16 | Richardson exact integrability | S38 | 8 conserved integrals |
| 17 | Ultrasmall grain L/xi_GL << 1 | S38 | L/xi_GL = 0.031 |
| 20 | GGE for integrable systems | S38 | GGE permanence |
| 21 | KZ defect density scaling | S37-38 | 59.8 pairs, P_exc=1.000 |
| 22 | BCS-BEC crossover regime | S37 | E_vac/E_cond = 28.8 (BEC) |
| 23 | GPV frequency and strength | S37 | omega_att=1.430, 85.5% |
| 27 | Flat band = infinite-order VHS | S22c | B2 flat band confirmed |
| 29 | Schwinger-instanton duality | S37 | S_Schwinger=0.070 vs S_inst=0.069 |
| 40 | Dirac eigenvalue bounds | S07-10 | Tier0 spectrum consistent |
