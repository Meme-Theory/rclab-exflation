# W3-2: BBN Without Hot -- Landau Condensed Matter Review (REVISED)

**Author**: Landau Condensed Matter Theorist
**Date**: 2026-03-13 (revised after PI correction)
**Re**: Session 41 W3-2 -- What does the crystal's phase transition produce, and does it connect to observed primordial abundances?
**Input**: W3-1 results (Tesla + QA), W2-1 through W2-5, PI narrative + PI directive, S38 transit physics (KZ, GGE, Schwinger-instanton), S37 instanton gas, Landau Papers 04/05/08/09/11/13
**Status**: CONCEPTUAL EXPLORATION (not gated)
**Revision note**: The original analysis assumed standard thermal BBN as an axiom, then checked whether the crystal could replicate it. The PI correctly identified this as circular. The revised analysis starts from the crystal's own phase transition dynamics and asks what it produces.

---

## 0. Revised Framing

The question is NOT "can the crystal replace the thermal bath in standard BBN?" The question is: **what does the transit through the BCS condensation at the fold produce, and does the output have any connection to observed light element abundances?**

This is a condensed matter question. In condensed matter, when a system undergoes a rapid phase transition (quench), the final state is determined by the quench dynamics -- the KZ mechanism, the Landau-Zener transition probabilities, the topology of the order parameter space -- not by thermal equilibrium. The framework says the universe underwent exactly such a quench at the fold. What precipitates from it?

The condensed matter analogy I will use throughout: the transit through the fold is analogous to rapid cooling of a superconductor through T_c, or to a quantum quench in a cold atom system. In both cases, the final state is a non-equilibrium state whose properties are set by the quench parameters, not by the equilibrium phase diagram.

---

## 1. The Quench and Its Products

### 1.1 What S38 Established

The transit through the van Hove fold is a **sudden quench** with the following parameters:

| Quantity | Value | Physical meaning |
|:---------|:------|:----------------|
| tau_Q/tau_0 | 8.71 x 10^{-4} | Quench speed / relaxation time |
| P_LZ | 0.999 | Landau-Zener: diabatic passage |
| P_exc | 1.000 | All 8 BCS modes excited |
| n_Bog per mode | 0.999 | Near-maximal Bogoliubov pair creation |
| Pairs created | 59.8 | DOS-weighted total |
| E_exc / |E_cond| | 443 | Total condensate destruction |
| Backreaction | 3.7% | Perturbative, underdamped |
| L/xi_GL | 0.031 | Zero-dimensional limit |
| BDI winding | 0 | No topological protection |

The quench is sudden (tau_Q/tau_0 << 1), zero-dimensional (L/xi_GL << 1), and complete (P_exc = 1). The BCS condensate is totally destroyed. Every Bogoliubov mode is excited to near-maximal occupation.

### 1.2 The GGE as the Primordial State

The post-transit state is a Generalized Gibbs Ensemble (GGE) with 8 Richardson-Gaudin conserved integrals. Three-layer integrability protection guarantees it never thermalizes:

1. Richardson-Gaudin integrability within B2
2. Block-diagonal theorem (D_K exact in Peter-Weyl) forbids inter-sector scattering
3. 4D coupling suppressed by (l_KK/l_4D)^2

The GGE Lagrange multipliers are computed from the ground state + unitary evolution through the quench. They are NOT free parameters -- they are the unique, deterministic output of the transit.

This GGE is the **primordial state of the internal space**. Whatever the 4D observer sees, it must be the 4D projection of this GGE.

### 1.3 The Phase Transition Produces Specific Occupation Numbers

The quench produces 59.8 Bogoliubov pairs distributed across the 3 spectral branches. From the S37 GPV decomposition:

| Branch | Modes | Pair-addition fraction | Character |
|:-------|:------|:----------------------|:----------|
| B2 | 4 | 85.5% (GPV) | Flat optical band |
| B3 | 3 | 13.3% | Dispersive optical |
| B1 | 1 | 0.45% | Acoustic-like |

The GPV (Giant Pair Vibration) at omega = 0.792 concentrates 85.5% of the pair-addition strength. The pair creation is overwhelmingly in the B2 sector. B3 gets 13.3%. B1 gets a trace.

These fractions are determined by the BCS pairing matrix V_ij, the density of states rho(E), and the quench parameters. They are geometry-dependent, parameter-free outputs of the crystal at the fold.

### 1.4 Condensed Matter Analog: What Phase Transitions Produce

In condensed matter, phase transitions produce specific stoichiometries determined by the free energy landscape, not by thermal kinetics (Paper 04, Section 4: the equilibrium order parameter is set by the coefficients a, b in the Landau expansion, which are determined by the symmetry and the microscopic Hamiltonian).

Specific examples:

1. **Eutectic solidification**: A binary liquid cooled through the eutectic point produces a specific ratio of two solid phases (e.g., alpha-Fe + Fe_3C in pearlite, with the ratio set by the lever rule on the phase diagram). The ratio depends on composition and cooling rate, not on thermal equilibrium of the solid.

2. **BCS quench in cold atoms**: A rapid quench through the BCS transition in a fermionic cold atom gas produces a specific pattern of quasiparticle excitations. The occupation numbers n_k are set by the Landau-Zener formula applied to each mode independently (Barankov & Levitov 2004, Yuzbashyan et al. 2005). The final state is a GGE, not a thermal state.

3. **Superfluid He-3 quench**: Rapid cooling through T_c in He-3 produces a network of quantized vortices whose density is set by the KZ mechanism (Bauerle et al. 1996, Ruutu et al. 1996). The number of vortices is a precise function of the cooling rate.

The framework's transit is closest to case 2: a BCS quench producing specific occupation numbers in a GGE.

---

## 2. The GGE-to-Abundance Mapping

### 2.1 The Central Question

The GGE has specific, computable occupation numbers. The 4D projection maps internal Digamma-modes to SM particles. If this mapping exists, then the GGE occupation numbers ARE the primordial abundances -- not of elements (which are composite), but of the fundamental excitations from which elements are built.

The question has two layers:
(a) What are the GGE occupation numbers per branch/mode?
(b) What SM particles do the branches correspond to?

### 2.2 Branch-to-SM Mapping (What Is Known)

The 8 singlet eigenvalues of D_K at the fold decompose into 3 branches. The subalgebra decomposition of su(3) under the Jensen deformation gives:

| Branch | Algebra | Eigenmodes | SM identification |
|:-------|:--------|:-----------|:-----------------|
| B1 | u(1) (K_7 direction) | 1 | Hypercharge/U(1)_Y sector |
| B2 | C^2 (coset su(3)/u(2)) | 4 | Higgs/broken generators |
| B3 | su(2) (complement in u(2)) | 3 | Weak isospin SU(2)_L sector |

This identification comes from Session 6 (CG algebra): B1 corresponds to the u(1) hypercharge direction, B2 to the coset directions (which become the Higgs field in the NCG Standard Model), and B3 to the su(2) weak isospin generators.

The C^16 spinor Psi_+ (Session 7) decomposes under this branching into the SM fermion multiplets: (nu_L, e_L, u_L, d_L) and their right-handed partners, plus antiparticles. The quantum numbers (hypercharge, weak isospin, color) are EXACTLY the SM quantum numbers -- this was verified to machine epsilon in Sessions 7-8.

### 2.3 The Numerical Coincidence Question

The PI asks: do the GGE numbers have any numerical relationship to D/H, Y_P, or Li-7/H?

The pair-addition fractions from the GPV decomposition are:

    B2 : B3 : B1 = 85.5% : 13.3% : 0.45%

or equivalently:

    B2/B3 = 6.43
    B1/(B2+B3) = 4.6 x 10^{-3}
    B3/(B2+B3) = 0.135
    B1/total = 4.5 x 10^{-3}

The observed abundances:

    Y_P = 0.245 (He-4 mass fraction)
    D/H = 2.53 x 10^{-5}
    Li-7/H = 1.6 x 10^{-10}

Is there a numerical relationship?

**Direct comparison**: B3/total = 0.135 is within a factor of 2 of Y_P/4 = 0.061 (He-4 number fraction per baryon). B1/total = 4.5 x 10^{-3} is 178 times larger than D/H = 2.53 x 10^{-5}. Neither B2 nor B3 nor B1 fractions are within an order of magnitude of the Li-7 abundance.

**Honest assessment**: The pair-addition fractions describe the distribution of PAIR EXCITATIONS across spectral branches. These are not directly particle abundances -- they are the weights with which the quench deposits energy into each branch of the internal phononic crystal. The mapping from "internal branch excitation weight" to "4D particle abundance ratio" requires the full KK reduction, including the multiplicity factors dim(p,q)^2, the 4D phase space, and the coupling between internal and external sectors. This mapping has not been computed.

### 2.4 What Can Be Said Without the Full Mapping

Even without the explicit KK reduction, the structure of the GGE tells us something:

1. **The state is non-thermal.** The GGE is NOT a Boltzmann distribution. It has 8 independent Lagrange multipliers, not one temperature. If the 4D projection of this state produces particle abundances, those abundances are NOT the predictions of any thermal model.

2. **The state is deterministic.** Given the BCS ground state and the transit trajectory tau(t), the GGE is uniquely determined. There are zero free parameters. This is a stronger prediction than BBN, which has one free parameter (eta, the baryon-to-photon ratio).

3. **The branch hierarchy is steep.** B2 dominates overwhelmingly (85.5%), B3 is subdominant (13.3%), B1 is trace (0.45%). If the 4D projection preserves this hierarchy, the primordial state has a dominant "Higgs-sector" excitation, a subdominant "weak-sector" excitation, and a trace "hypercharge-sector" excitation. The observed universe DOES have a hierarchy: baryons (from the strong/weak sector) dominate over light elements (involving electromagnetic and weak processes).

4. **The ratio B2/(B2+B3) = 0.865.** In standard BBN, the mass fraction going into He-4 is approximately (2 * n/p) / (1 + n/p) where n/p ~ 1/7. This gives Y_P ~ 0.25. If B2 maps to "inert" (He-4-like) and B3 maps to "reactive" (hydrogen-like), then B2/(B2+B3) = 0.865 >> 0.25. The quench deposits too much energy into the "Higgs" sector relative to the "weak" sector to match the observed He-4 fraction -- unless the 4D projection redistribution is highly non-trivial.

---

## 3. The n/p Ratio from Symmetry

### 3.1 Isospin in the Crystal

The neutron and proton are members of the SU(2) isospin doublet. In the crystal, SU(2) isospin corresponds to the B3 branch (the su(2) subalgebra of su(3) preserved by the Jensen deformation).

The B3 branch has 3 modes. Under SU(2), the adjoint representation decomposes as 3 = triplet (the generators T_1, T_2, T_3). The isospin doublet (proton, neutron) lives in the FUNDAMENTAL representation of SU(2), not the adjoint. So the n/p question is: what determines the relative occupation of the two states in the fundamental doublet?

### 3.2 Symmetry Argument

At the round SU(3) point (tau = 0), the full SU(3) symmetry is unbroken. The Jensen deformation breaks SU(3) -> U(1)_7 x U(2), where U(2) = U(1) x SU(2). The SU(2) subgroup survives the deformation. Therefore:

**Any quantity that transforms as a non-trivial representation of SU(2) must have equal components** (by Schur's lemma), as long as SU(2) is an exact symmetry of the dynamics.

The isospin doublet (p, n) transforms as the fundamental 2 of SU(2). If SU(2) is exact, n = p. Therefore:

    n/p = 1    (from exact SU(2) symmetry of the crystal)    (1)

This is the crystal's prediction for the n/p ratio at the transit epoch: equal numbers of neutrons and protons.

### 3.3 How Standard BBN Gets n/p = 1/7

In standard BBN, n/p departs from 1 because the weak interaction (which mediates n <-> p conversion) breaks isospin: the mass difference Q = m_n - m_p = 1.293 MeV is an explicit isospin-breaking effect from the difference in u and d quark masses and electromagnetic self-energy. The thermal bath provides the energy scale (temperature) against which Q is measured. The equilibrium n/p = exp(-Q/T) departs from 1 when T drops below Q.

### 3.4 What the Crystal Must Provide

For the crystal picture to produce n/p different from 1, it needs an isospin-breaking mechanism. The candidates:

1. **The Jensen deformation itself.** The deformation preserves SU(2) as an exact symmetry (Session 34: U(2) is the residual symmetry group). So the deformation does NOT break isospin. n/p = 1 from symmetry.

2. **The quark mass difference.** In the NCG framework, quark masses come from the Yukawa sector of the finite spectral triple (the "internal" part of the product geometry M_4 x F). The Yukawa couplings are NOT determined by the SU(3) crystal alone -- they involve the finite geometry F. If the Yukawa couplings break isospin (as they must, since m_u is not equal to m_d), then n/p departs from 1.

3. **Electromagnetic self-energy.** The proton-neutron mass difference gets ~1 MeV from QED effects (proton has charge, neutron does not). This requires the electromagnetic coupling alpha_em, which is set by the Seeley-DeWitt coefficient a_4/a_2 at the frozen tau.

**Critical observation**: The crystal's SU(3) geometry determines the GAUGE sector (couplings, symmetry breaking pattern) but NOT the Yukawa sector (fermion masses, mixing angles). The n/p ratio depends on isospin breaking, which comes from the Yukawa sector. The crystal alone predicts n/p = 1 (isospin exact). Departures from n/p = 1 require input from the finite geometry F, which is outside the scope of the D_K computation.

### 3.5 The n/p = 1 Problem

If the crystal's 4D projection preserves exact SU(2) isospin, the primordial n/p = 1. Then:

    Y_P = 2*(n/p)/(1 + n/p) = 2*(1)/(1+1) = 1.0    (2)

This would mean ALL baryons end up as He-4 (every neutron pairs with a proton). Y_P = 1.0 vs observed Y_P = 0.245. This is a catastrophic failure -- off by a factor of 4.

To avoid this, the framework MUST break isospin. Either:
(a) The finite geometry F provides the quark mass difference, giving m_n > m_p, and some dynamical process (analogous to weak freeze-out) converts the initial n/p = 1 into n/p ~ 1/7 before nucleosynthesis completes. This requires a 4D dynamical process -- whether thermal or not.
(b) The GGE occupation numbers are NOT uniformly distributed within each branch's internal SU(2) structure, i.e., the quench itself breaks isospin. This would require the transit trajectory tau(t) to couple differently to the isospin-up and isospin-down components.

Option (a) is more natural: the Yukawa sector provides the seed for isospin breaking (Q = m_n - m_p), and some post-transit dynamics amplifies it. But "post-transit dynamics" that converts n -> p at specific rates IS weak-interaction physics -- whether it occurs in a thermal bath or not, the rate is set by G_F and the available phase space.

### 3.6 A Non-Thermal n/p Mechanism?

In condensed matter, population inversion is achieved without thermal equilibrium. For example, in a laser-pumped system, the population of excited vs ground states is set by the pump rate, decay rate, and stimulated emission rate -- not by temperature.

Could an analogous mechanism set n/p in the crystal?

Consider: the quench creates 59.8 Bogoliubov pairs. Each pair consists of a quasiparticle and a quasi-hole. In the BCS language, these are excitations above and below the Fermi level. If the 4D projection maps quasiparticles to neutrons and quasi-holes to protons (or vice versa), then n/p is set by the quasiparticle/quasi-hole asymmetry of the GGE.

In the sudden-quench limit, n_Bog = 0.999 for all modes. The occupation is nearly maximal and nearly equal across all modes. There is NO quasiparticle/quasi-hole asymmetry -- the quench creates pairs symmetrically. Therefore n/p = 1 from the quench alone, confirming the symmetry argument.

Departures from n/p = 1 require breaking the particle-hole symmetry, which in the BCS framework requires mu != 0 (chemical potential). But Session 34 proved: mu = 0 is forced by PH symmetry of the spectrum. There is no chemical potential to break particle-hole symmetry. The quench produces exactly equal numbers of particles and holes.

**Structural conclusion**: The crystal's BCS quench, with mu = 0 forced by PH symmetry, produces n/p = 1 exactly. Any departure from n/p = 1 requires physics beyond the internal BCS sector -- specifically, the isospin-breaking Yukawa sector and some dynamical mechanism to convert the initial n/p = 1 into the observed n/p ~ 1/7.

---

## 4. The Lithium Problem as a Topological Constraint

### 4.1 The PI's Suggestion

The PI suggests: "If Li-7 abundance is set by defect topology (the number of defects with winding number 3), it has nothing to do with thermal reaction rates." The working paper (Section 8.3) already proposes that Li-7 corresponds to a "higher-order topological defect" that is preferentially dissipated.

### 4.2 What S38 Says About Topological Defects

Session 38 established definitively:

1. **L/xi_GL = 0.031**: The BCS system is zero-dimensional. No spatial direction exists for topological defects to form.
2. **BDI winding number = 0** at mu = 0: No topologically protected defects exist in the BDI classification. Pfaffian sign = -1 at all tau -- no topological phase transition.
3. **No 4D domain walls**: "There are no 4D domain walls (because the gap field is internal, 0D). The excitation is spatially uniform, not localized."

These results close the topological defect route for the INTERNAL space. The BCS quench in 0D does not produce vortices, domain walls, or any spatially extended defect.

### 4.3 But Topology Could Enter Through the 4D Projection

The internal quench is 0D, but the 4D spacetime is extended. If the quench produces excitations that couple to 4D spatial degrees of freedom, the resulting 4D field configurations COULD have topological structure.

The relevant homotopy groups for the order parameter space (Paper 03, Section on domain walls; Paper 13, Section on vortices):

For U(1)_7 breaking by BCS:
- pi_0(U(1)) = 0: no domain walls
- pi_1(U(1)) = Z: vortex lines (quantized circulation)
- pi_2(U(1)) = 0: no monopoles

But Session 38 established: "NG mode ceases to exist post-transit." The U(1)_7 symmetry is restored after the quench. If U(1)_7 is restored, the order parameter space is trivial (a point), and all homotopy groups are trivial. No topological defects of the BCS order parameter survive.

### 4.4 What COULD Produce Topological Content

Even without BCS topological defects, the 4D effective theory has its own topological content:

1. **Baryon number as a topological charge.** In the Skyrme model (and in QCD at large N_c), baryons are topological solitons -- skyrmions with winding number B in pi_3(SU(2)) = Z. The baryon number B is the topological charge. In this picture, a proton is a winding-1 skyrmion and a nucleus with mass number A is a winding-A skyrmion.

2. **Nuclear binding as topological binding.** Deuterium (B=2) would be a winding-2 skyrmion, He-4 (B=4) would be winding-4, and Li-7 (B=7) would be winding-7. The formation rate for higher-winding skyrmions from the quench COULD follow a topological scaling:

    n(B) ~ exp(-c * B^alpha)    (3)

where c and alpha depend on the quench parameters. For skyrmion production in 3+1D, Monte Carlo simulations (Battye & Sutcliffe 1997) suggest alpha ~ 1 for large B.

3. **The Li-7 problem as a winding-number effect.** If equation (3) holds with alpha ~ 1:
   - n(B=1)/n(B=2) ~ exp(-c) / exp(-2c) = exp(c) ~ 10^5 (from D/H ~ 10^{-5})
   - n(B=7)/n(B=1) ~ exp(-7c) / exp(-c) = exp(-6c) ~ (D/H)^6 ~ 10^{-30}

This predicts Li-7/H ~ 10^{-30}, which is 20 orders of magnitude BELOW the observed 1.6 x 10^{-10}. The topological scaling underpredicts lithium even more severely than thermal BBN overpredicts it.

### 4.5 Assessment of the Topological Route

The topological defect picture for primordial abundances has three obstacles:

1. **No internal defects.** The 0D limit and BDI winding = 0 kill all internal-space topological defects.
2. **No BCS defects post-transit.** U(1)_7 is restored; no order parameter manifold for defects to live in.
3. **Skyrmion scaling gives wrong numbers.** Even if baryons ARE skyrmions, the winding-number scaling gives abundances that are exponentially suppressed with B, predicting Li-7/H ~ 10^{-30} rather than 10^{-10}.

The topological route is not closed by axiom -- it is closed by the specific numbers. The framework's 0D quench produces no spatial defects, and the skyrmion scaling that would replace thermal BBN gives the wrong abundances by 20 orders of magnitude.

---

## 5. What the Transit DOES Produce: The GGE Relic

### 5.1 Reframing: Abundances from the GGE

Set aside the question of how the GGE maps to specific element abundances (which requires the uncomputed KK reduction). Focus on what the GGE IS and what it PREDICTS qualitatively.

The GGE state has:
- 59.8 Bogoliubov pairs (near-maximal occupation n_Bog ~ 0.999 per mode)
- 8 conserved Richardson-Gaudin integrals I_alpha
- Energy E_exc = 443 * |E_cond|
- Non-thermal distribution: 8 independent Lagrange multipliers, not one temperature

### 5.2 The GGE as a Chemical Composition

In a BCS system, the Bogoliubov quasiparticles carry quantum numbers. Each mode k has a quasiparticle with definite K_7 charge, branch membership (B1/B2/B3), and spin. The GGE occupation n_k specifies how many of each type of quasiparticle exist.

If we think of the quasiparticle species as "chemical species," the GGE is a specific chemical composition:

| "Species" | Branch | Modes | n_k | Total quasiparticles |
|:----------|:-------|:------|:----|:--------------------|
| Higgs-sector excitations | B2 | 4 | 0.999 | 4 x 0.999 x N_DOS(B2) |
| Weak-sector excitations | B3 | 3 | 0.999 | 3 x 0.999 x N_DOS(B3) |
| Hypercharge excitations | B1 | 1 | 0.999 | 1 x 0.999 x N_DOS(B1) |

The DOS weighting is critical: N_DOS(B2) = 4 x 14.02 = 56.08 (4 modes, van Hove rho = 14.02), N_DOS(B3) = 3 x 1 = 3 (estimated, smooth DOS), N_DOS(B1) = 1 x 1 = 1 (estimated). The exact DOS numbers give the 59.8 total pairs.

### 5.3 What WOULD Match Abundances

For the GGE to directly encode primordial abundances, we would need a mapping:

    Y_P = f(n_{B2}, n_{B3}, n_{B1}, I_1, ..., I_8)    (4)
    D/H = g(n_{B2}, n_{B3}, n_{B1}, I_1, ..., I_8)    (5)
    Li-7/H = h(n_{B2}, n_{B3}, n_{B1}, I_1, ..., I_8)    (6)

where f, g, h are the 4D projection functions determined by the KK reduction. Computing these functions requires:

1. The explicit KK mode expansion of the 4D fields in terms of D_K eigenmodes
2. The coupling between internal Bogoliubov quasiparticles and 4D particle states
3. The 4D phase space integration for composite objects (nuclei)

This is an enormous computation that has not been performed. Without it, we cannot say whether the GGE numbers match the observed abundances.

### 5.4 What We CAN Say: Structure of the Prediction

Even without the explicit mapping, the structure of the GGE prediction differs from thermal BBN in specific ways:

**Thermal BBN**: One parameter (eta). Abundances determined by competition between reaction rates (proportional to T^n) and expansion rate (proportional to T^2). All abundances are functions of a single number eta.

**GGE prediction (if it existed)**: Eight parameters (the 8 Richardson-Gaudin conserved integrals). Abundances determined by the quench dynamics of 8 coupled modes. All 8 parameters are computed from the geometry -- zero free parameters.

The structure is different: 0 free parameters (GGE) vs 1 free parameter (BBN). The GGE is more constrained. If the numbers match, it is a prediction. If they fail, it is a falsification.

---

## 6. Critical Evaluation of the PI's Claims (Revised)

### 6.1 Claims That Gain Traction in the Revised Framing

| Claim | Status | Assessment |
|:------|:-------|:-----------|
| "Phase transitions produce specific stoichiometries" | **STRUCTURALLY CORRECT** | This is standard condensed matter. The BCS quench at the fold produces specific occupation numbers (B2:B3:B1 = 85.5:13.3:0.45). These are the transit's "stoichiometry." |
| "The GGE IS the final state" | **ESTABLISHED** (S38) | The post-transit state is a permanent GGE. Three-layer integrability protection. |
| "Quench dynamics determine final state, not equilibrium" | **STRUCTURALLY CORRECT** | The GGE occupation numbers are set by the Landau-Zener transition probabilities and the Bogoliubov transformation, not by thermal equilibrium. |

### 6.2 Claims That Face Structural Obstacles

| Claim | Obstacle | Assessment |
|:------|:---------|:-----------|
| "GGE occupation numbers ARE the abundances" | The mapping from internal-space quasiparticle numbers to 4D particle abundances requires the full KK reduction, which has not been computed. | **OPEN but UNTESTED** |
| "The order parameter decomposition produces baryons as defects" | BDI winding = 0, L/xi_GL = 0.031, U(1)_7 restored post-transit. No topological defects in 0D. | **CLOSED for internal space.** Open for 4D skyrmions but scaling wrong by 10^20. |
| "n/p from crystal symmetry, not temperature" | Crystal's SU(2) is exact => n/p = 1. Need isospin breaking from Yukawa sector (outside D_K). | **n/p = 1 from crystal alone** -- catastrophically wrong. Need Yukawa sector. |

### 6.3 Claims That Are Refuted

| Claim | Reason |
|:------|:-------|
| "Spectral refinement drives nucleosynthesis" | N_eff is step function (W2-1). Crystal always resolves nuclear scales (W2-4). No refinement epoch. |

### 6.4 The Deep Issue: The Missing Link

The PI's physical intuition -- that the transit is a phase transition producing specific outputs -- is correct as condensed matter physics. The problem is the LINK between the internal-space quench (which produces GGE occupation numbers of Bogoliubov quasiparticles in the 8D internal phononic crystal) and the 4D particle content (quarks, leptons, photons, nuclei).

The GGE tells us what the internal space is doing. It does not tell us what the 4D observer sees, because the 4D projection has not been computed.

In condensed matter language: we know the phonon occupation numbers of the crystal after the quench. We do NOT know how those phonon occupations translate into the SURFACE properties that an external observer measures. The "surface" here is the 4D spacetime; the "crystal" is the 8D internal space.

This is not a dismissal -- it is a statement of what must be computed. The GGE is a concrete, parameter-free state. The KK reduction is a concrete, computable mapping. The combined output WOULD be a parameter-free prediction for the primordial abundances. The computation simply has not been done.

---

## 7. What CAN'T Work (Honestly)

### 7.1 Pure Internal Quench Cannot Produce Nuclei Directly

Nuclei are composite objects in 4D spacetime. They have spatial extent (fm scale), binding energies (MeV scale), and specific quantum numbers (baryon number, charge, isospin). The internal-space BCS quench produces excitations of the Dirac operator D_K on SU(3). These excitations live in the internal space, not in 4D.

The excitations of D_K carry INTERNAL quantum numbers (K_7 charge, SU(2) representation labels, (p,q) sector) but not 4D spatial structure. A deuteron is not a pair of internal-space excitations -- it is a bound state of two baryons in 4D, held together by the strong force (mediated by gluons, which are 4D gauge fields from the KK reduction of the metric on SU(3)).

The GGE gives the internal quantum numbers of the primordial state. Translating those into 4D particle abundances requires the full chain:

    D_K eigenmodes -> KK reduction -> 4D fields -> QCD -> hadrons -> nuclear physics -> abundances

Each step in this chain is a well-defined computation. But the chain has not been traversed.

### 7.2 n/p = 1 Is Fatal Without Isospin Breaking

As shown in Section 3, the crystal's exact SU(2) symmetry predicts n/p = 1. This gives Y_P = 1.0 (100% helium-4), which is off by a factor of 4 from the observed Y_P = 0.245. Some isospin-breaking mechanism is essential. The crystal's D_K does not provide it -- the Yukawa sector (finite geometry F in the NCG product M_4 x F) must be included.

### 7.3 The Hierarchy Problem for D/H

The observed D/H = 2.53 x 10^{-5} is a very small number. In standard BBN, it arises from the near-cancellation between deuterium production (n + p -> D + gamma) and photodissociation (gamma + D -> n + p). The small residual is the "deuterium bottleneck."

In the crystal picture, D/H must come from the GGE occupation numbers or from the topological content of the 4D projection. Neither mechanism naturally produces a number as small as 10^{-5}:

- The GGE occupation numbers are all near 1 (n_Bog ~ 0.999). There is no small number in the GGE.
- The branch fractions are B1/total = 0.0045 ~ 10^{-2.3}. This is 2.7 orders of magnitude above D/H.
- The skyrmion scaling gives D/H ~ exp(-c) with c ~ 11.5 (from D/H ~ 10^{-5}), predicting Li-7/H ~ exp(-7c) ~ 10^{-35}. Way too suppressed.

The small number D/H = 10^{-5} is not naturally produced by ANY mechanism that starts from O(1) occupation numbers. It requires either a near-cancellation (as in standard BBN) or a suppression mechanism with a specific exponent. The crystal picture does not provide either -- at least not without the full KK reduction.

---

## 8. Open Questions (Revised)

### O-BBN-1: The KK Reduction of the GGE (DECISIVE)

**What must be computed**: The explicit 4D particle content of the post-transit GGE state. This requires:
1. Expand D_K eigenmodes in terms of 4D fields using the KK reduction on SU(3)
2. Compute the Bogoliubov transformation relating internal quasiparticles to 4D particles
3. Evaluate the 4D particle number operators in the GGE state
4. Sum over all internal modes with Peter-Weyl multiplicities

**Output**: The number density of each 4D particle species (quarks, leptons, gauge bosons, Higgs) in the post-transit state, as a function of zero free parameters.

**Pre-registerable gate**: If the KK reduction of the GGE produces particle number densities with ratios matching observed primordial abundances to within an order of magnitude, the non-thermal BBN picture is viable. If the ratios are off by more than 3 orders of magnitude, the picture is falsified.

### O-BBN-2: Isospin Breaking from the Finite Geometry

**What must be computed**: The Yukawa sector of the NCG Standard Model (finite geometry F) evaluated at the transit epoch. This determines the quark mass difference m_d - m_u and hence the neutron-proton mass difference Q.

**Why it matters**: Without isospin breaking, n/p = 1 and Y_P = 1.0 -- fatal. The Yukawa sector is the only source of isospin breaking in the NCG framework.

### O-BBN-3: Post-Transit 4D Dynamics (Thermal or Not?)

**What must be determined**: After the internal quench deposits its energy into 4D fields via the KK coupling, what happens? Does the 4D sector thermalize (producing a hot plasma and standard BBN)? Or does the integrability protection extend to the 4D sector (producing a non-thermal primordial state)?

Key distinction: The three-layer integrability protection applies to the INTERNAL space. The 4D sector has its own dynamics (QCD, QED, weak interactions) which are NOT integrable in general. If the internal GGE couples to 4D fields that then thermalize, the net effect is standard BBN with modified initial conditions -- not "BBN without hot."

### O-BBN-4: The 59.8 Pairs in Physical Units

**What must be computed**: The physical energy of the 59.8 Bogoliubov pairs in GeV (using M_KK from W1-4). If E_pair ~ O(M_KK) ~ 10^9 to 10^13 GeV, these are GUT-scale excitations. Their decay products would cascade down to SM-scale particles, potentially thermalizing through QCD interactions. This cascade COULD produce a hot plasma -- in which case the framework's prediction is "standard BBN, with the thermal bath originating from the transit quench rather than from reheating after inflation."

This would be a different ORIGIN for the hot plasma, not a different PHYSICS of nucleosynthesis.

---

## 9. Structural Summary (Revised)

### The Constraint Map

**Proven structures:**
1. The transit is a sudden BCS quench producing a specific, deterministic GGE with 8 conserved integrals and 59.8 Bogoliubov pairs. (S38)
2. The GGE never thermalizes in the internal space. (Three-layer protection, S38)
3. The crystal's SU(2) is exact => n/p = 1 from internal symmetry alone. (S34, this analysis)
4. No topological defects in the internal space. (BDI winding = 0, L/xi_GL = 0.031, S38)
5. N_eff is a step function; no gradual spectral refinement. (W2-1)
6. Crystal always resolves nuclear scales. (W2-4)

**Open region (viable but uncomputed):**
1. The KK reduction of the GGE could produce 4D particle abundances that match observations. This is the decisive computation (O-BBN-1).
2. The 59.8 Bogoliubov pairs at GUT-scale energies could decay and thermalize in 4D, producing a hot plasma. This would give standard BBN with a non-standard ORIGIN for the plasma. (O-BBN-4)
3. The Yukawa sector (finite geometry F) provides isospin breaking, departing from n/p = 1. (O-BBN-2)

**Excluded regions:**
1. Spectral refinement as nucleosynthesis driver. (N_eff step function)
2. Topological defects from internal quench as nuclei. (0D limit, BDI winding = 0)
3. Skyrmion scaling for nuclear abundances. (Li-7/H off by 10^20)
4. n/p from crystal symmetry alone. (SU(2) exact => n/p = 1, Y_P = 1.0)

### The Key Insight

The transit IS a phase transition that produces specific outputs. The outputs are Bogoliubov quasiparticle pairs with specific occupation numbers in a GGE. This is a genuine, parameter-free prediction of the framework. But the mapping from internal GGE to 4D particle abundances (the KK reduction) has not been computed, and the n/p = 1 prediction from crystal symmetry is catastrophically wrong without the Yukawa sector.

The most plausible scenario, given the numbers: the GUT-scale energy of the transit quench (E_exc ~ 10^9-10^13 GeV per pair, times 59.8 pairs) cascades into 4D particles through KK couplings, thermalizes via QCD interactions (which are NOT integrable -- the internal integrability protection does not extend to 4D QCD), and produces a hot plasma at T ~ 10^{10-15} GeV. This plasma then cools through standard cosmological expansion, and nucleosynthesis proceeds via standard BBN.

In this picture, the framework's prediction for BBN is: **standard BBN, with the hot plasma originating from the transit quench rather than from inflationary reheating.** The framework does not predict "BBN without hot" -- it predicts a specific, geometric origin for the heat.

### The One Sentence (Revised)

The transit quench produces a deterministic GGE with 59.8 Bogoliubov pairs at GUT-scale energies; the decisive question is whether the KK coupling to 4D thermalizes these pairs (giving standard BBN with a geometric origin for the heat) or preserves their non-thermal character (giving parameter-free but uncomputed abundance predictions from the GGE) -- and either way, isospin breaking from the Yukawa sector is essential because the crystal's exact SU(2) predicts n/p = 1.
