# Meta-Analysis Request: Feynman-Theorist

**Domain**: Path Integrals, QED/QFT, Renormalization, Feynman Diagrams, Quantum Computing
**Date**: 2026-03-13
**Agent**: feynman-theorist
**Researchers Folder**: `researchers/Feynman/`

---

## 1. Current Library Audit

**Papers on file**: 14 (1948--1994)
**Coverage assessment**: The QED core (path integral -> propagator -> diagrams -> renormalization) is complete and excellent. The Schwinger/Dyson/Wilson additions form a proper triad with Feynman. Liquid helium and quantum computing provide the condensed matter and computational bookends. **Major gaps**: no papers on heat kernel methods beyond Schwinger's proper-time (which is a sketch, not a manual), no functional determinant technology, no modern RG/asymptotic safety, no cosmological particle creation, no Richardson-Gaudin integrability (central to S37-42 physics), no spectral action one-loop quantization (van Suijlekom 2022, the single most relevant modern paper for this project).

| # | Current Paper | Key Topics | Adequate? |
|---|--------------|------------|-----------|
| 01 | Feynman 1948 -- Path integral (non-rel QM) | Sum over histories, stationary phase, K(b,a) | **Yes** |
| 02 | Feynman 1949 -- Theory of positrons | Feynman propagator, CPT, pair creation | **Yes** |
| 03 | Feynman 1949 -- Space-time QED | Feynman diagrams, rules, a_e=alpha/2pi | **Yes** |
| 04 | Feynman 1950 -- Mathematical QED | Feynman parameters, proper-time, renormalization | **Yes** |
| 05 | Feynman 1954 -- Liquid helium | Phonon-roton, superfluidity, quantized vortices | **Yes** |
| 06 | Feynman-Gell-Mann 1957 -- V-A theory | Chirality, weak interactions, CVC | **Yes** |
| 07 | Feynman 1963 -- Quantum gravity | Graviton propagator, ghosts, non-renormalizability | **Yes** |
| 08 | Feynman 1969 -- Parton model | DIS, Bjorken scaling, structure functions | **Partial** (low direct relevance) |
| 09 | Feynman 1982 -- Simulating physics | Quantum simulation, exponential blowup, Bell/CHSH | **Yes** |
| 10 | Feynman 1986 -- Quantum computers | Gates, CNOT, universality, Trotter | **Partial** (low direct relevance) |
| 11 | Schwinger 1948 -- QED I | Proper-time, effective action, pair production | **Yes** (CRITICAL) |
| 12 | Dyson 1949 -- Equivalence proof | Wick theorem, power counting, all-orders renormalizability | **Yes** |
| 13 | Wilson 1974 -- RG and critical phenomena | Fixed points, universality, epsilon expansion, EFT | **Yes** (CRITICAL) |
| 14 | Shor 1994 -- Quantum factoring | QFT, period-finding, polynomial algorithm | **Partial** (low direct relevance) |

**Coverage gaps by topic**:

| Topic | Current Coverage | Gap Severity |
|:------|:----------------|:-------------|
| Path integrals (non-rel + QED) | Complete (01-04) | None |
| Heat kernel / Seeley-DeWitt expansion | Schwinger proper-time only (11) | **CRITICAL** -- project computes spectral action via heat kernel at every session |
| Spectral action quantization | None | **CRITICAL** -- van Suijlekom 2022 is THE paper for one-loop spectral action |
| Functional determinants on Lie groups | None | **HIGH** -- framework needs det(D_K) on SU(3) |
| Cosmological particle creation (Parker) | None | **HIGH** -- S38 identified Parker mechanism as the framework's transit physics |
| Schwinger pair creation in curved spacetime | Schwinger flat-space only (11) | **HIGH** -- S38 found Schwinger-instanton duality (S_Schwinger = S_inst = 0.069) |
| Richardson-Gaudin integrability / GGE | None | **HIGH** -- GGE permanence is central to S38-42 framework |
| BCS path integral / Hubbard-Stratonovich | None | **MEDIUM** -- BCS on compact manifold is the framework's many-body sector |
| Asymptotic safety / modern RG | Wilson 1974 only (13) | **MEDIUM** -- adversarial perspective on UV completion |
| Kibble-Zurek mechanism | None | **MEDIUM** -- S42 fabric domain formation uses KZ scaling |
| Hauser-Feshbach / compound nucleus decay | None | **MEDIUM** -- S42 HF-KK-42 is a major computation |

---

## 2. Web-Fetch Requests

### Priority A -- Critical (directly addresses open gates or framework mechanisms)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| 1 | Heat kernel expansion: user's manual | D.V. Vassilevich | 2003 | arXiv:hep-th/0306138 | THE reference for Seeley-DeWitt coefficients a_0, a_2, a_4. Every spectral action computation in the project (S14-S42) uses heat kernel expansion. We compute a_2/a_0 and a_4/a_2 ratios at every tau -- this manual gives the explicit formulas, boundary condition treatments, and singularity handling. Currently we cite Schwinger's proper-time (Paper 11) as a sketch; Vassilevich is the complete technology. |
| 2 | One-loop corrections to the spectral action | T.D.H. van Nuland, W.D. van Suijlekom | 2022 | arXiv:2107.08485 | Establishes one-loop renormalizability of the spectral action within the NCG framework. Uses perturbative expansion in higher Yang-Mills and Chern-Simons forms. Ward identities play crucial role. This is the ONLY paper that quantizes the spectral action at one loop while staying within spectral geometry. Directly addresses our Feynman Test Step 4 (power counting) and Step 6 (unitarity) for the spectral action itself. The framework's post-transit EFT (Computation C from S40) needs exactly this technology. |
| 3 | The Spectral Action Principle | A. Chamseddine, A. Connes | 1997 | arXiv:hep-th/9606001 | The founding paper of the spectral action. Tr(f(D/Lambda)) = integral L_SM + Einstein + Weyl + CC. We reference this throughout but do not have it in the Feynman folder. The path integral interpretation of the spectral action -- summing over all Dirac operators -- is the path integral formulation of this geometry. Every session since S7 uses this. |
| 4 | Fifty years of cosmological particle creation | L. Parker, J. Navarro-Salas | 2017 | arXiv:1702.07132 | Comprehensive review of Parker's cosmological particle creation mechanism. S38 W3 identified the framework's transit as Parker-type creation (not Hawking: no horizon, no thermal spectrum). The Bogoliubov coefficient computation, adiabatic regularization, and WKB connection are all needed for Computation C (post-transit EFT). Parker's original 1966 thesis is also now freely available (arXiv:2507.05372). |
| 5 | Richardson-Gaudin models and broken integrability | P.W. Claeys | 2018 | arXiv:1809.04447 | Thesis covering exact BCS solutions, conserved quantities, GGE formation, and broken integrability dynamics. The framework's GGE (S38 permanent result: 8 Richardson-Gaudin conserved quantities, integrability-protected non-thermal relic) is built on this mathematics. Quench dynamics of pairing Hamiltonians (Claeys+ PRB 2019, arXiv:1811.09591) directly models our BCS transit. |

### Priority B -- Important (foundational or fills significant gap)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| 1 | Conformal anomaly and gravitational pair production | A. del Rio, J. Navarro-Salas | 2023 | arXiv:2306.03892 | Heat-kernel approach to gravitational particle creation analogous to Schwinger effect. Spacetime curvature takes the role of electric field strength. Directly connects to our S38 Schwinger-instanton duality (S_Schwinger = S_inst = 0.069). |
| 2 | Effective action and gravitational pair production in (A)dS spacetime | Various | 2024 | arXiv:2410.20949 | Euclidean heat kernel method for effective action in (A)dS, revealing non-trivial imaginary part reminiscent of Schwinger effect. The spectral action IS a heat kernel; this connects our computation directly to pair production rates. |
| 3 | Noncommutative Geometry and Particle Physics (2nd ed.) | W.D. van Suijlekom | 2024 | ISBN:978-3-031-59119-8 (book) | Updated textbook covering NCG Standard Model, inner fluctuations, spectral action, heat kernel coefficients, and the finite geometry F. Available as PDF at waltervansuijlekom.nl. The BDI classification of our spectral triple and the fermionic action S_F^Connes = 0 theorem (S41) should be checkable against this reference. |
| 4 | Colloquium: Exactly solvable Richardson-Gaudin models for many-body quantum systems | J. Dukelsky, S. Pittel, G. Sierra | 2004 | arXiv:nucl-th/0405011 | Review of Richardson-Gaudin exact solutions. Our N=8 BCS system on the Dirac spectrum is an explicit Richardson-Gaudin model. This paper gives the Bethe ansatz equations, conserved charges, and the map to nuclear pairing that our Nazarewicz agent uses. |
| 5 | Spectral geometry for the standard model without fermion doubling | L. Dabrowski, F. D'Andrea | 2020 | DOI:10.1103/PhysRevD.101.075038 | Addresses fermion doubling in the NCG Standard Model. Our S41 result (S_F^Connes = 0 from BDI T-symmetry) may be related to or constrained by this alternative approach. Important adversarial check. |
| 6 | Generalized Gibbs ensemble in integrable lattice models | L. Vidmar, M. Rigol | 2016 | arXiv:1604.03990 | Review of GGE in integrable systems. Our permanent GGE relic (S38) is this object applied to the Richardson-Gaudin BCS model. Establishes when GGE applies, what it predicts, and the role of conserved quantities. |
| 7 | Quantum Gravity and the Functional Renormalization Group | M. Reuter, F. Saueressig | 2019 | Cambridge Univ. Press | Book-length treatment of asymptotic safety. Our spectral action has power-counting non-renormalizability issues at two loops (Paper 07). Asymptotic safety provides the main alternative UV completion scenario. Critical for adversarial assessment. |

### Priority C -- Supplementary (strengthens coverage, recent developments)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| 1 | Conformally-flat gravitational analogues to the Schwinger effect | Various | 2025 | arXiv:2602.18578 | Latest development on gravitational Schwinger analogy in radiation-dominated universe. Confirms Bogoliubov coefficient approach. |
| 2 | Self-consistent graviton spectral function in Lorentzian quantum gravity | Various | 2025 | arXiv:2507.22169 | Positive graviton spectral function with massless peak and multi-graviton continuum. Addresses unitarity of quantum gravity -- relevant to our Feynman Test Step 6 for the gravitational sector. |
| 3 | BRST symmetry violation and limitations of asymptotic safety | Various | 2026 | Symmetry 18(1), 140 | Recent critique arguing asymptotic safety encounters fundamental BRST violations above the gravitational cutoff. Relevant adversarial literature for UV completion question. |
| 4 | The asymptotic expansion of the heat kernel on a compact Lie group | Various | 2011 | arXiv:1111.2643 | Heat kernel specifically on compact Lie groups (our SU(3)). Gives the convolution kernel and its asymptotic expansion. Would allow cross-checking our numerical Seeley-DeWitt coefficients against analytic formulas. |
| 5 | Backreaction inclusive Schwinger effect in de Sitter | Various | 2024 | arXiv:2412.09436 | Backreaction effects on pair creation in de Sitter. Our S38 backreaction was 3.7% (perturbative). This paper provides the self-consistent framework. |
| 6 | Nonthermal heavy dark matter from a first-order phase transition | Various | 2024 | JHEP12(2024)190 | Non-thermal DM production from phase transition dynamics. Closest existing literature to our BCS transit -> GGE dark matter mechanism (S42 DM-PROFILE-42). |
| 7 | Kibble-Zurek universality in a strongly interacting Fermi superfluid | Various | 2019 | Nature Physics 15, 1177 | KZ mechanism in BCS superfluids. Direct experimental analog of our BCS transit domain formation. Measures KZ scaling exponents for U(1) breaking in paired fermions. |
| 8 | Stochastic Schwinger effect | Various | 2025 | arXiv:2510.14468 | Extends Schwinger pair creation to stochastic fluctuating backgrounds. Our instanton gas (S37: n_inst x xi = 1.35-4.03) operates in a regime where the "field" fluctuates. |

---

## 3. New Researcher / Field Recommendations

### Complementary (would strengthen or extend the framework)

| Researcher or Field | Why Complementary | Key Papers (1-3) | Proposed Folder Name |
|--------------------|-------------------|-------------------|---------------------|
| **Walter van Suijlekom** (Radboud) | The single most active researcher on quantizing the spectral action. One-loop renormalizability (2022), inner fluctuations, spectral Standard Model. His textbook is THE reference for NCG particle physics. His work on the perturbative path integral over inner fluctuations is exactly what our Computation C (post-transit EFT) requires. | 1. arXiv:2107.08485 (one-loop spectral action). 2. "NCG and Particle Physics" 2nd ed (2024 textbook). 3. arXiv:1209.3595 (renormalization of asymptotically expanded YM spectral action) | `researchers/van-Suijlekom/` |
| **Pieter Claeys** (Flatiron/Max Planck) | Leading expert on Richardson-Gaudin integrability, broken integrability, and quench dynamics of pairing models. Our GGE permanence (S38), B2 integrability (S40 Poisson statistics), and compound nucleus dissolution all live in his mathematical territory. His broken-integrability results constrain what happens when our exact integrability is perturbed by fabric coupling. | 1. arXiv:1809.04447 (thesis: RG models + broken integrability). 2. arXiv:1811.09591 (quench dynamics of nonintegrable pairing). 3. SciPostPhys 3, 028 (eigenvalue-based RG models) | `researchers/Claeys/` |
| **Dmitri Vassilevich** (UFABC Sao Paulo) | Author of the heat kernel "user's manual" -- the standard reference for Seeley-DeWitt coefficients. His work covers manifolds with and without boundaries, various singularities, and explicit formulas for all coefficients we compute. Essential for making our a_0, a_2, a_4 computations rigorous and for extending to finite-density heat kernels (Computation A). | 1. arXiv:hep-th/0306138 (heat kernel manual). 2. Various on spectral geometry and heat kernel with torsion | `researchers/Vassilevich/` |
| **Leonard Parker** (deceased) + Jose Navarro-Salas (Valencia) | Parker invented cosmological particle creation (1966). Navarro-Salas continues the program with modern heat-kernel methods linking gravitational pair creation to the Schwinger effect. Our S38 transit IS Parker creation. Their Bogoliubov coefficient technology is what computes the GGE occupation numbers from first principles rather than from our approximate sudden-quench model. | 1. arXiv:1702.07132 (50 years review). 2. arXiv:2306.03892 (conformal anomaly + grav pair production). 3. arXiv:2507.05372 (Parker 1966 thesis, retyped 2025) | `researchers/Parker-Navarro-Salas/` |
| **Functional determinants on Lie groups** (field) | The one-loop path integral around the BCS saddle on SU(3) is a functional determinant det'(D_BdG) on a compact Lie group. Berline-Getzler-Vergne provide the index theorem framework. Freed's lecture notes provide a physicist-friendly introduction. This is the mathematical backbone for our Computation C (post-transit EFT Feynman rules). | 1. Berline, Getzler, Vergne "Heat Kernels and Dirac Operators" (1992 book). 2. D. Freed "Geometry of Dirac Operators" (lecture notes). 3. arXiv:1111.2643 (heat kernel on compact Lie group) | `researchers/Spectral-Geometry/` |

### Adversarial (would challenge, constrain, or stress-test the framework)

| Researcher or Field | Why Adversarial | Key Papers (1-3) | Proposed Folder Name |
|--------------------|-----------------|-------------------|---------------------|
| **Asymptotic Safety Program** (Reuter, Saueressig, Percacci, Eichhorn) | Our spectral action is non-renormalizable at two loops (Paper 07, QG-5: D = 2 + 2L). The asymptotic safety program claims a non-perturbative UV fixed point saves gravity. If correct, it provides an ALTERNATIVE UV completion that competes with the NCG spectral action. If wrong (BRST violation paper, 2026), it strengthens the case that the spectral action's non-perturbative character is necessary. Either way, it is the primary adversarial perspective on the gravitational sector. | 1. Reuter & Saueressig "QG and the FRG" (Cambridge 2019). 2. arXiv:2310.20603 (Lorentzian asymptotic safety 2024). 3. Symmetry 18(1) 140 (BRST violation critique 2026) | `researchers/Asymptotic-Safety/` |
| **Fermion doubling critiques** (Lizzi, Barrett, Devastato) | The fermion doubling problem in NCG was "solved" by shifting KO-dimension from 0 to 6 (our framework uses KO-dim=6). But Dabrowski & D'Andrea (2020) found an alternative resolution without fermion doubling. If the KO-dim=6 resolution is NOT the unique correct one, our entire spectral triple structure (C^16 spinor, BDI classification, [J,D_K]=0) could be built on a non-unique foundation. This is a structural challenge that would need to be addressed. | 1. Dabrowski & D'Andrea PRD 101, 075038 (2020). 2. Lizzi et al PLB 1997 (original fermion doubling). 3. Barrett JMP 48, 012303 (2007, Lorentzian spectral triples) | `researchers/NCG-Critiques/` |
| **Cosmological constant problem** (Weinberg, Bousso, Polchinski) | Our framework produces Lambda ~ 10^{80-127} x Lambda_obs (S42 W-Z-42). The effacement ratio |E_BCS|/S_fold ~ 10^{-6} ensures w = -1 to 28 OOM precision, but the CC ITSELF overshoots by 80+ orders. Weinberg's 1989 review, Bousso-Polchinski landscape (2000), and modern sequestering proposals (Kaloper-Padilla) are the primary adversarial literature. Any CC calculation in our framework must confront Weinberg's no-go argument directly. | 1. Weinberg RMP 61, 1 (1989, CC problem review). 2. Bousso & Polchinski JHEP 0006, 006 (2000, landscape). 3. Kaloper & Padilla PRL 112, 091304 (2014, sequestering) | `researchers/CC-Problem/` |

---

## 4. Framework Connections (S41/S42)

### Session 41 connections

**S_F^Connes = 0 (S41 W1-2, Theorem 1)**: The Connes fermionic action (1/2)psi^T C2 D psi vanishes identically because C2*D_K is symmetric and Grassmann variables antisymmetrize. This is a path integral statement: the fermionic path integral integral D[psi] exp(S_F^Connes) = 1 identically. The fermion functional integral contributes NO dynamics from the internal space alone. This needs the path integral interpretation from Paper 01 and the Grassmann technology from Paper 04. The vanishing is structural (BDI T-symmetry), not a fine-tuning. The Pfaffian channel S_F^Pfaff is the only non-trivial fermionic bilinear -- this is a Pfaffian of an antisymmetric matrix, which is a SQUARE ROOT of a determinant. The computation det(C1*D_K) is a functional determinant on SU(3) -- exactly the technology in the Berline-Getzler-Vergne book that we are missing.

**Spectral refinement is a step function (S41 W2-1)**: N_eff jumps from 32 to 240 at infinitesimal tau. In path integral language, the functional integral sum_histories exp(iS) has a measure that changes discontinuously when degeneracies are lifted. This is analogous to a first-order phase transition in the path integral (the saddle point structure changes). Wilson's RG (Paper 13) gives the framework: the number of relevant operators changes at a critical point. Here the "critical point" is tau = 0 (round SU(3)), and the relevant operators are the 208 newly distinguished eigenvalues.

**Signed logarithmic sum (S41 W1-3)**: Variant E produces a minimum at tau ~ 0.15 with A in [0.025, 0.295]. The BF assignment per eigenvalue requires computing the 4D KK reduction on SU(3) -- this is computing the one-loop determinant det(D_M^2 + lambda_k^2) for each KK mass lambda_k, with the sign coming from the spin-statistics connection. Feynman's Paper 02 (positrons as backward-in-time electrons) and Paper 12 (Dyson's (-1)^{fermion loops}) give the sign prescription. The computation is: for each KK eigenvalue, determine whether the 4D field it produces is bosonic (+) or fermionic (-). This is determined by the gamma_9 grading of the internal spinor -- but Variant B (gamma_9 grading) gives ZERO by spectral pairing. The correct assignment must come from the FULL spectral triple D_total = D_M x 1 + gamma_5 x D_K, which mixes 4D and internal quantum numbers. This is a computation we CAN do with van Suijlekom's technology but have not done.

### Session 42 connections

**Gradient stiffness Z(tau) = 74,731 (S42 W1-1)**: This is the spectral action's response to spatial tau gradients: Z = sum_k mult_k (d lambda_k/d tau)^2. In Feynman language, this is the two-point function <delta_tau(x) delta_tau(0)> at zero momentum -- it sets the propagator for the tau modulus field: G_tau(k) = 1/(k^2 + m_tau^2) with m_tau^2 = V''_eff/Z = 4.253 M_KK^2. The tau field has a MASSIVE Klein-Gordon propagator. Its Feynman rules are: propagator = i/(k^2 - m_tau^2 + i*epsilon), vertex with KK mode k = coupling proportional to d lambda_k / d tau. This is our Computation C in embryonic form.

**Hauser-Feshbach branching (S42 W1-3)**: The compound nucleus decay of the KK system has ZERO massless channels (structural: D_K spectral gap 0.819 M_KK). In Feynman diagram language, every final-state propagator has a mass gap. There is no "photon" channel -- no 1/k^2 propagator. All channels are massive: G_k = i/(k^2 - m_k^2 + i*epsilon) with m_k > 0.819 M_KK. The branching ratios are set by phase space (Boltzmann factors exp(-m/T_acoustic)) and matrix elements (V_{ij}^2). The doorway preference of 3.2:1 (B2 over B1) is weak because the level density rho_B3 compensates the small matrix element -- a standard result in Fermi's golden rule: Gamma = 2pi |V|^2 rho. The MISSING computation: the full Feynman diagram for KK mode decay into 4D continuum states at a fabric boundary. This is a discrete-state-in-continuum problem (Fano physics), not the discrete+discrete coupling that was tested. The anti-Hermitian Kosmann connection (K + K^dag = 0) means the vertex is purely imaginary -- interesting for interference effects.

**w = -1 + O(10^{-29}) (S42 W3-1)**: The spectral action IS a cosmological constant by Feynman Test Step 1: S = Tr f(D^2/Lambda^2) is a functional of the geometry, not a dynamical field. It does not propagate, does not fluctuate (at tree level), and has no time dependence once tau is frozen. In path integral language: the partition function Z = integral D[tau] exp(-S_eff[tau]) has a saddle at tau_fold, and the one-loop determinant around this saddle gives the quantum corrections. The leading correction is the zero-point energy T_ZP = 108 M_KK^4 (0.043% of S_fold), which is part of the CC, not a departure from w = -1. The Nazarewicz review identifies 5 mechanisms; ALL are defeated by the effacement ratio |E_BCS|/S_fold ~ 10^{-6}. This is the path integral's statement that the BCS sector is a PERTURBATION on the geometric background: the saddle point (spectral action) dominates over the fluctuations (BCS) by 6 orders.

**CDM from geometry (S42 DM-PROFILE-42)**: The GGE quasiparticles have Feynman propagators G_BdG(omega, k) = (omega + epsilon_k) / (omega^2 - E_k^2 + i*delta) where E_k = sqrt(epsilon_k^2 + Delta_k^2) is the BdG dispersion. These are INTERNAL-SPACE propagators -- they propagate within the SU(3) fiber, not through 4D spacetime. Their 4D gravitational effect enters through the stress-energy tensor T_{mu,nu} = diag(rho, 0, 0, 0), giving w = 0 (pressureless dust). The zero self-interaction (sigma/m ~ 10^{-51} cm^2/g) follows from the tau Compton wavelength: the interaction range is lambda_C ~ 1/m_tau ~ 10^{-25} m, and the cross-section at any astrophysical separation is exponentially suppressed. In Feynman diagram language, two GGE quasiparticles interact by exchanging a tau modulus quantum: the amplitude is M ~ g^2 / (q^2 - m_tau^2), and at q << m_tau the cross-section scales as sigma ~ g^4 / m_tau^4 ~ (M_KK)^{-4} -- negligible.

### Open questions this literature could address

1. **Post-transit EFT (Computation C)**: The 8-species massive fermion EFT with known V_{kl} couplings from the Dirac spectrum. Van Suijlekom's one-loop technology + Vassilevich's heat kernel manual + the functional determinant on SU(3) give ALL the ingredients. Feynman rules: massive KK propagators, Kosmann vertices (anti-Hermitian), tau-modulus exchange. Power counting: the theory is non-renormalizable (dimension-6 operators from KK), with cutoff at M_KK. This is Computation C, identified in S40, still open.

2. **Parker creation vs sudden quench**: Our S38 model uses the sudden quench approximation (tau_Q/tau_0 << 1). Parker's exact Bogoliubov coefficient computation would give the precise GGE occupation numbers n_k without the sudden-quench assumption. The Parker-Navarro-Salas literature provides this technology. The result would upgrade the GGE from "approximate sudden quench" to "exact adiabatic + non-adiabatic Bogoliubov calculation."

3. **Heat kernel at finite density (Computation A)**: delta_a_2 = -N_pairs * Delta^2. This shifts the gravitational coupling. Vassilevich's manual covers the heat kernel with background fields; extending to the BdG operator (which includes the anomalous pairing field Delta) gives the finite-density correction to the Seeley-DeWitt coefficients. This is computable from existing data.

4. **KK graviton mass (Computation B)**: The HESS-40 eigenvalues give the Hessian of the spectral action in 22 transverse directions. These are the mass matrix for KK graviton modes. The graviton propagator in the fabric EFT has mass m_grav^2 ~ H_ii / Z_ii. Compare to BCS gap hierarchy. Feynman's Paper 07 gives the massless graviton propagator; the massive version (Fierz-Pauli) is the extension needed.

5. **Fano physics at fabric boundaries**: The discrete KK modes at a fabric boundary decay into 4D continuum channels E = sqrt(m_KK^2 + p^2). This IS the textbook Fano setup (discrete state embedded in continuum). S42 W2-3 proved that discrete+discrete gives no Fano zeros (correct). The discrete+continuum case remains open and is the physically correct question. The Feynman diagram is: KK mode propagator -> vertex (Kosmann, anti-Hermitian) -> 4D continuum propagator. The cross-section will show Fano asymmetric lineshapes if the continuum channels interfere. This could produce the mass-dependent filtering that HF-KK-42 lacked.

---

## 5. Self-Assessment

- **Biggest gap in current library**: The heat kernel / functional determinant gap is the most severe. We compute spectral action via heat kernel at every session but have no reference more detailed than Schwinger's 1948 sketch. Vassilevich (hep-th/0306138) fills this immediately. The van Suijlekom one-loop paper (2107.08485) is equally critical -- it is the ONLY existing quantization of the spectral action, and our Computation C requires exactly this technology.

- **Most promising new direction**: The **Parker-Navarro-Salas cosmological particle creation** literature could upgrade the GGE from approximate (sudden quench) to exact (Bogoliubov coefficients from the full time-dependent D_K(tau(t))). The recent heat-kernel approach to gravitational pair creation (del Rio & Navarro-Salas 2023) connects our Schwinger-instanton duality (S_Schwinger = S_inst = 0.069) to a computable one-loop effective action. This could simultaneously compute the GGE occupation numbers AND the one-loop correction to the spectral action from particle creation -- a unified computation that addresses both the transit physics and the post-transit EFT.

- **Confidence in recommendations**: **High** for Priority A papers (all directly compute quantities the project needs). **Medium-High** for Priority B (all fill identified gaps with established literature). **Medium** for Priority C (supplementary but relevant recent work). **High** for new researcher recommendations (van Suijlekom and Claeys are the two most directly relevant active researchers to this project's open computations).
