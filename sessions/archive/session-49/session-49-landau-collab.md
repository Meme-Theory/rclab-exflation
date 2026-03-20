# Landau -- Collaborative Feedback on Session 49

**Author**: Landau (Condensed Matter Theorist)
**Date**: 2026-03-17
**Re**: Session 49 Results (20 computations, 8 PASS / 7 INFO / 4 FAIL / 1 retraction)

---

## Section 1: Key Observations

### 1.1 The Bragg Gap and the Z_3 Quantization Theorem

My computation (W1-C, BRAGG-GOLDSTONE-49) established that the Bragg gap on the 32-cell tessellation sits at O(1) M_KK in all three impedance models tested (0.07 to 1.35 M_KK). The structural reason is the Z_3 domain wall: the condensate phase rotates by 2*pi/3 across each wall, producing rho_s(wall)/rho_s(bulk) = cos^2(pi/3) = 1/4 and hence an impedance ratio eta = 1/2. This ratio is topologically quantized -- it cannot be tuned continuously to 1, because the Z_3 phase jump is a discrete topological charge.

This is a Landau symmetry argument (Paper 04, Section 8). The domain wall between Z_3 sectors is classified by pi_0(Z_3) = Z_3. The wall tension and the impedance contrast are both determined by the symmetry-breaking pattern, not by microscopic parameters. No amount of deformation of the wall profile, condensate stiffness, or elastic constants can make eta exponentially close to 1. The Bragg mechanism is therefore structurally incapable of producing a hierarchically small mass gap. This closure is permanent.

What the Bragg computation also revealed is a critical geometric fact: w_wall (0.465 M_KK^{-1}) exceeds l_cell (0.152 M_KK^{-1}) by a factor of 3. The cells are immersed in their own walls. The notion of a "phononic crystal" with well-separated scatterers does not apply. The true lattice period is L_Z3 = 1.462, dominated by the inter-cell wall region. This modifies the interpretation of every fabric-level propagator: the relevant propagation medium is not "cells connected by thin walls" but "walls interrupted by small coherent patches." The condensed matter analog is a granular superconductor in the strong-coupling regime (grain size << coherence length), not a Josephson junction array of large islands.

### 1.2 The Leggett Mode: Frozen, Destroyed, then Resurrected as Mass Source

My second computation (W1-H, LEGGETT-TRANSIT-49) demonstrated that the Leggett mode ceases to exist post-transit. The chain of reasoning is tight:

1. **Frozen during transit**: omega_transit/omega_L1 = 12,721. The mode completes 1.25 x 10^{-5} oscillations during the quench. Phase accumulated: 7.86 x 10^{-5} rad. The Leggett degree of freedom is completely inert.

2. **Destroyed post-transit**: P_exc = 1 from S38 means all quasiparticles are excited. The BCS self-consistency factor (1 - 2n_k) reverses sign for every mode, making the gap equation wrong-sign. The self-consistent solution is Delta = 0 for all three sectors. With Delta = 0, the inter-sector Josephson coupling J_ij = V(i,j)|Delta_i||Delta_j| = 0. The Leggett frequency omega_L = sqrt(J/rho) = 0. The mode does not exist.

3. **Symmetry restoration**: This is a Landau symmetry argument (Paper 04). The Leggett mode is a collective excitation of the ORDERED phase. It requires nonzero order parameters in at least two sectors. Post-transit, the order parameter is zero: full U(1)_7 x U(1)_{B1} x U(1)_{B2} x U(1)_{B3} symmetry is restored. No broken symmetry implies no Goldstone-like modes. The mode is annihilated by the same mechanism that destroys the condensate.

The Leggett-GGE computation (W1-T, Nazarewicz) confirms this independently: the N=1 sector of the GGE is exactly non-interacting (density-density interaction vanishes identically when only one fermion is present). The oscillation at omega = 0.133 M_KK is the bare single-particle energy splitting E_B3 - E_B2, not a collective mode. Enhancement = 1.000 exactly.

Yet the dipolar catalog (W1-S, Volovik) identifies the Leggett mode as the MECHANISM that generates the Goldstone mass: J_23 couples K_7-charged B2 pairs to K_7-neutral B3 pairs, breaking U(1)_7 explicitly. The mass is m_G = omega_L1 = 0.070 M_KK, which is 18% above the m_req = 0.059 M_KK needed for n_s = 0.965 at the lowest fabric mode.

This creates a precise tension: the Leggett mode is the mass source PRE-transit but ceases to exist POST-transit. The framework needs the mass during the transit or at the fold, not after. This is physically consistent -- the Goldstone mass is set by the Josephson coupling in the ordered phase, and the power spectrum P(K) is imprinted during or at the end of the BCS epoch. The post-transit Leggett destruction does not erase the mass already generated. The condensed matter analog: in MgB2, the Leggett mode exists below T_c. Above T_c, it vanishes. But the Bragg scattering pattern recorded at T < T_c carries the information about inter-band coupling even after the sample is warmed past T_c.

### 1.3 HFB Backreaction and State-Independent V

The HFB computation (W1-I, Nazarewicz) confirms that the BCS interaction matrix V_{kk'} is determined by SU(3) representation theory (Clebsch-Gordan coefficients in the Peter-Weyl basis) and is therefore state-independent. The backreaction through the particle-hole channel is 1.2% at the nuclear benchmark coupling g_ph = 0.03. This validates the S38 estimate of 3.7% as a conservative upper bound and establishes that BCS is a 1% perturbation on the geometry.

The structural significance: V being state-independent means the self-consistency problem is SIMPLER than nuclear HFB. In nuclei (Paper 02, Skyrme DFT), the effective NN interaction depends on the local density, creating a nonlinear feedback loop between the mean field and the pairing field. Here, the interaction is fixed by the mathematical structure of SU(3), and the only feedback is through the occupations (which affect the single-particle energies at the 1% level). This is the ideal case for Landau theory: the order parameter dynamics decouple from the microscopic interaction to a precision that makes perturbation theory exact for all practical purposes.

### 1.4 The Multi-Temperature Friedmann as a Pressure Amplifier

The multi-T Friedmann computation (W1-E, Einstein) shows that the 8-temperature GGE structure shifts w_0 from -0.323 (single-T) to -0.430 (GGE), a 33% shift toward DESI. The mechanism is a pressure redistribution: high-T modes (B2, T=0.59 M_KK) have per-mode alpha = 1.29, while low-T modes (B3, T=0.15) have alpha = 6.38. The GGE concentrates 95% of energy in B2, pulling the weighted average toward lower alpha (higher P/E).

In condensed matter terms, this is a multi-component normal fluid with anisotropic effective temperatures. Landau's two-fluid model (Paper 05, Paper 07) separates superfluid and normal components. The post-transit GGE is entirely normal fluid (rho_s = 0), but it is not a single-temperature normal fluid -- it is a generalized Gibbs ensemble with 8 effective temperatures. The equation of state w = -1/(1+alpha) depends on the partition of energy among sectors, and the non-equilibrium GGE partition differs from thermal equilibrium by exactly the amount that matters: the 33% shift in w_0.

The shortfall is still 4.0x in P/E relative to DESI. The question for the next session is whether fabric-level effects (inter-cell coupling, spatial gradients of the GGE temperatures) can close this gap.

---

## Section 2: Assessment

### 2.1 The O-Z Form and the alpha_s Rigidity

The Bayesian analysis (W1-L, Nazarewicz) established that the O-Z power spectrum P(K) = T/(J K^2 + m^2) produces the EXACT algebraic identity alpha_s = n_s^2 - 1. At n_s = 0.9649, this gives alpha_s = -0.069, which is 6.0 sigma from Planck's measurement of alpha_s consistent with zero.

The question the session raises but does not answer: is the O-Z form the correct propagator?

In condensed matter systems, the Ornstein-Zernike form arises from the mean-field Gaussian approximation to the two-point correlation function of the order parameter near a second-order phase transition (Paper 04, Section 7). It is the leading-order term in the expansion G(K) = 1/(xi^{-2} + K^2) and is EXACT in two limits: (a) above the upper critical dimension d > d_uc, and (b) at mean-field level for any d. Corrections to O-Z come from:

1. **Anomalous dimension eta**: G(K) ~ 1/(K^{2-eta} + xi^{-2+eta}) with eta > 0. For the 3D Ising universality class (BCS-CLASS-43), eta = 0.0364. This is a 3.6% correction to the K^2 term and modifies the running: alpha_s = -(1 - n_s^2) * (1 + eta + ...). At eta = 0.036, this changes alpha_s from -0.069 to approximately -0.067 -- a 3% correction that does not resolve the 6 sigma tension.

2. **Lattice corrections**: The fabric is a 32-cell lattice, not a continuum. On a lattice, G(K) = 1/(sum_a 2J_a(1-cos K_a) + m^2). Near the zone boundary, this differs from K^2 by terms of order K^4/12. The S48 finite-difference measurement of alpha_s = -0.038 was sampling this lattice curvature, but the Bayesian analysis shows this is an artifact of the measurement method, not a genuine modification: the angular-averaged running is -0.069 regardless of lattice discretization.

3. **Inter-band coupling (Leggett mass)**: This is the critical question. When the mass m in the O-Z propagator arises from inter-band Josephson coupling rather than from a simple on-site potential, the propagator structure changes. In a multiband superconductor, the phase propagator is NOT a single O-Z pole. It is a MATRIX propagator with structure:

    G^{-1}_{ab}(K) = rho_s^a K^2 delta_{ab} + M^2_{ab}

where M^2_{ab} is the mass matrix from the Josephson couplings J_{ab}. The eigenvalues of M^2 give the physical masses (omega_L1 and omega_L2 from S48). The TILT (n_s) depends on the propagator of the LIGHTEST mode (the pseudo-Goldstone), which has mass omega_L1 = 0.070 M_KK from the Josephson coupling.

The crucial difference: the O-Z form assumes a SINGLE propagating mode with mass m. The Leggett mechanism introduces a COUPLED system of 3 phases (B1, B2, B3) with a 3x3 mass matrix. The lightest eigenvalue is omega_L1, but the spectral index is determined by the FULL matrix propagator, not just the lightest mass.

Specifically, the power spectrum of phase fluctuations in a 3-band system is:

    P(K) = sum_alpha |u_alpha|^2 T_alpha / (rho_alpha K^2 + omega_alpha^2)

where alpha = {Goldstone, L1, L2}, u_alpha are the eigenvectors, T_alpha the effective temperatures, and rho_alpha the stiffness projected onto each mode. The spectral tilt n_s is determined by the K-derivative of log P(K), which receives contributions from ALL three poles, not just the lightest. The running alpha_s is then NOT given by the single-mode formula n_s^2 - 1 but by a weighted sum over the three poles.

This is the key structural insight: the alpha_s = n_s^2 - 1 identity is an artifact of the SINGLE-POLE O-Z approximation. In the MULTI-POLE Leggett propagator, alpha_s receives corrections proportional to the mass splittings omega_L2/omega_L1 and the stiffness anisotropy rho_B2/rho_B3. Whether these corrections can bring alpha_s from -0.069 to the Planck window (|alpha_s| < 0.016 at 2 sigma) is a computable question.

### 2.2 The Multi-T Friedmann Pressure Amplifier

In condensed matter, a system with multiple effective temperatures violates the standard equation of state. The deviation from single-T behavior is parameterized by the Lagrange multipliers of the conserved quantities (Paper 20, Rigol GGE). For a Fermi system with 8 conserved charges, the pressure is:

    P = sum_k (dp_k/dV) / (exp(sum_alpha lambda_alpha I_alpha^k) + 1)

where lambda_alpha are the 8 GGE temperatures and I_alpha^k the conserved charge eigenvalues. The standard Fermi-Dirac P-E relation P = E/3 (for massless relativistic fermions) or P = (2/3)E (nonrelativistic) is modified to a non-trivial function of {lambda_alpha}.

The multi-T computation shows this modification shifts w_0 by 33% toward DESI. In condensed matter, similar "pressure amplification" occurs in:

- **Spin-charge separated systems**: Where spin and charge degrees of freedom thermalize at different rates. The total pressure is NOT the thermal value at any single temperature but depends on the partition of energy between spin and charge sectors.

- **Multi-gap superconductors (MgB2, iron pnictides)**: Where each gap channel has a different effective temperature after a quench. The transient equation of state differs from equilibrium by the inter-band temperature difference.

The framework is in the second category. The 8-temperature GGE is a multi-gap system where the "bands" are the B1, B2, B3 sectors with their individual quasiparticle temperatures. The pressure amplification is a DIRECT consequence of the non-thermal energy partition -- a prediction that standard cosmology (single T) cannot make.

### 2.3 The n_s = 0.965 Near-Miss: Leggett Mass Within 18%

The dipolar catalog's central finding -- omega_L1/m_req = 1.18 -- is the first mechanism in 12+ routes to produce a mass at the correct order of magnitude. Every previous attempt either gave m = 0 (exact symmetry) or m ~ 10^{-59} M_KK (Hubble scale). The Leggett mechanism gives m = 0.070 M_KK against a target of 0.059 M_KK.

The 18% discrepancy is NOT negligible in a framework that claims parameter-free predictions. But in condensed matter, 18% is within the range of mean-field-to-exact corrections. The Leggett frequency omega_L = sqrt(J_23 Delta_B3 / rho_B2) depends on: (a) J_23 from the inter-sector V-matrix, (b) Delta_B3 from the BCS gap, and (c) rho_B2 from the B2 density of states. Each has uncertainty at the 10-30% level (V-matrix model selection, BCS mean-field vs ED, DOS approximation). A 18% discrepancy could be absorbed by a 10% shift in any one of these inputs.

However, this must be tested, not assumed. The correct path forward is to compute n_s and alpha_s from the FULL 3-pole Leggett propagator rather than from the single-pole O-Z form. If the multi-pole corrections to alpha_s are of order omega_L2/omega_L1 - 1 ~ 0.54, the running could shift substantially from the single-pole value.

---

## Section 3: Collaborative Suggestions

### S-1: The GL Free Energy with the Leggett Degree of Freedom

The S47 collab review (Section 1, eq. (1)) wrote the 0D GL free energy for three sectors:

    F[{Delta_s}] = sum_s [ a_s(tau) |Delta_s|^2 + b_s |Delta_s|^4 ] + sum_{s != s'} g_{ss'} |Delta_s|^2 |Delta_s'|^2

This is the AMPLITUDE free energy. The Leggett mode lives in the PHASE sector, which is omitted. The complete GL free energy including phases is:

    F[{Delta_s, phi_s}] = sum_s [ a_s |Delta_s|^2 + b_s |Delta_s|^4 + rho_s (nabla phi_s)^2 ]
                        + sum_{s != s'} [ g_{ss'} |Delta_s|^2 |Delta_s'|^2
                        - J_{ss'} |Delta_s| |Delta_s'| cos(phi_s - phi_{s'}) ]    (1)

The Josephson terms -J_{ss'} cos(phi_s - phi_{s'}) are the mass-generating terms for the relative phases. The Leggett modes are the small oscillations of (phi_B2 - phi_B3) and (phi_B1 - phi_B2) around the equilibrium values phi_s = 0.

The fabric-level order parameter for the 32-cell system is then a FIELD on the tessellation:

    F_fabric = sum_cells sum_s [ ... ] + sum_{NN cells} sum_s J_pair^s cos(phi_s^i - phi_s^j)

where the inter-cell Josephson coupling J_pair^s links the SAME sector on neighboring cells, and the intra-cell Leggett coupling J_{ss'} links DIFFERENT sectors on the same cell. The full propagator is a 3N_cells x 3N_cells matrix, and the lowest-lying mode is neither pure Goldstone (inter-cell) nor pure Leggett (intra-cell) but a hybridized mode.

The computation for S50: Diagonalize the full 3 x 32 = 96 coupled-phase system. Extract the lowest eigenfrequency and its eigenvector character (Goldstone vs Leggett content). If the hybridized mode has mass closer to m_req = 0.059 than the pure Leggett omega_L1 = 0.070, the near-miss improves.

### S-2: The Multi-Pole Propagator and Modified Running

The O-Z single-pole assumption must be replaced by the 3-pole Leggett propagator. For the fabric phase-fluctuation power spectrum:

    P_fabric(K) = sum_{alpha=1}^{3} w_alpha / (rho_alpha K^2 + m_alpha^2)    (2)

where alpha runs over the Goldstone (m_1 = omega_L1), upper Leggett (m_2 = omega_L2), and the amplitude/Higgs mode (m_3 = 2*Delta_B2, the pair-breaking threshold). The weights w_alpha are determined by the coupling of each collective mode to the observable (density-density correlator or phase-phase correlator, depending on what n_s measures).

The spectral index is:

    n_s - 1 = d log P / d log K |_{K = K_pivot}

For a multi-pole propagator, this gives:

    n_s - 1 = -2 * [ sum_alpha w_alpha rho_alpha K^2 / (rho_alpha K^2 + m_alpha^2)^2 ]
              / [ sum_alpha w_alpha / (rho_alpha K^2 + m_alpha^2) ]              (3)

This is no longer the simple formula n_s = 1 - 2m^2/(rho K^2 + m^2). The running alpha_s acquires corrections from the pole structure. The computation for S50: evaluate eq. (3) at K_pivot and extract alpha_s. If the upper Leggett pole at m_2 = 0.107 contributes significantly, alpha_s is modified.

### S-3: What Order Parameter Describes the Fabric?

The fabric is a Josephson junction array of 32 cells, each containing a 3-component BCS condensate. The order parameter space for the FULL fabric is:

    M_fabric = [ (C^3 / R_+^3) x T^2 ]^{32} / (Z_3)^{32}

-- at each cell, a 3-component order parameter (amplitude and phase for B1, B2, B3), modulo the Z_3 identifications from the domain walls. The T^2 factor is the Cartan torus of SU(3), encoding the relative phases. The Z_3 quotient is the domain wall constraint: phases across walls jump by 2*pi/3.

In condensed matter, this is the order parameter space of a GRANULAR multi-band superconductor. The relevant universality class for the fabric phase transition is determined by the topology of M_fabric. With 32 cells and 3 phases per cell, the effective U(1) for the overall Goldstone mode emerges from a 96-dimensional phase space through progressive freezing of the massive modes.

The S47 superfluid density tensor rho_s^{ab} was computed within a SINGLE cell. The fabric rho_s requires the inter-cell phase rigidity, which involves the Josephson network stiffness. The effective fabric-scale rho_s is reduced from the single-cell value by a factor determined by the Josephson network connectivity and the Mott crossover physics (W1-B: J/E_C = 0.152, crossover regime). This reduction modifies the Goldstone velocity c_G, the correlation length xi, and ultimately n_s.

### S-4: Running Mass from Anomalous Dimension

The recommendation RUNNING-MASS-50 asks whether m(K) ~ K^gamma with gamma > 1.7 can resolve the alpha_s tension. In condensed matter, mass running is equivalent to the ANOMALOUS DIMENSION of the order parameter field. The anomalous dimension eta introduces:

    G(K) = 1 / (K^{2-eta} + m^{2/(2-eta)})

For the 3D Ising class, eta = 0.036 (insufficient: need gamma_eff ~ 1.7). But the framework is NOT a simple 3D Ising critical point at the CMB pivot scale. At the fabric scale, the system is a Josephson array in the Mott crossover regime. The phase propagator on a lattice with strong disorder (Mach > 1 on 78% of T^2, from W1-G) is modified by Anderson localization effects:

    G(K) ~ 1 / (D_{eff}(K) K^2 + m^2)

where D_eff(K) is a K-dependent effective diffusion constant that reflects the disordered condensate landscape. If D_eff decreases with K (as in a localization-enhanced system), the effective running is steeper than K^2, which modifies alpha_s. This is computable from the explicit condensate texture on T^2.

---

## Section 4: Constraint Map Assessment

### What was computed (summary of load-bearing numbers):

| Result | Value | Constrains |
|:-------|:------|:-----------|
| m_Bragg | 0.07-1.35 M_KK | Bragg gap CLOSED for hierarchical mass |
| eta (Z_3) | 1/2 exactly | Impedance ratio topologically quantized |
| omega_L1 post-transit | 0 | Leggett mode destroyed (Delta = 0) |
| omega_L1 pre-transit | 0.070 M_KK | Mass source identified (18% from target) |
| alpha_s (O-Z) | -0.069 +/- 0.008 | 6.0 sigma from Planck (single-pole artifact?) |
| HFB backreaction | 1.2% | V state-independent, BCS perturbative |
| w_0 (multi-T) | -0.430 | 25% closer to DESI than single-T |
| P_exc post-transit | 1.000 | Superfluid destroyed, condensate = 0 |
| KZ 3-component | 59.82 / 59.8 | S38 identity confirmed to 0.04% |

### What region of solution space survives:

The n_s problem has narrowed to one viable mechanism: the Leggett mass from inter-sector Josephson coupling. All other routes are closed:
- Friedmann-Goldstone: 115 orders too small
- Bragg gap: 30-60 orders too large (Z_3 quantization)
- Geometric breaking: 16-58 orders too large
- Pure O-Z with m: alpha_s = n_s^2 - 1 produces 6 sigma tension

The ONLY surviving n_s route that avoids the alpha_s crisis is a propagator that is NOT single-pole O-Z. The multi-pole Leggett propagator (eq. (2)-(3) above) is the natural candidate. Whether the pole structure modifies alpha_s sufficiently is the decisive computation for S50.

The CC crossing survives at fabric level (ec_fabric = 1.586 > ec_min = 1.264) but is conditional on J_pair > 0.096 M_KK.

The w_0 prediction is in a structurally interesting position: 21x preferred over LCDM in w_0 alone, but the w_a = 0 prediction creates 14x disfavor in the 2D (w_0, w_a) plane. The multi-T mechanism is a genuine prediction -- no other cosmological model generates a non-thermal equation of state from first principles -- but its quantitative shortfall (4.0x in P/E) needs fabric-level corrections.

### What remains uncomputed (decisive gates for S50):

1. **LEGGETT-PROPAGATOR-50**: n_s and alpha_s from the 3-pole Leggett propagator (eq. (2)-(3)). Pre-registered criterion: if |alpha_s| < 0.016, the O-Z crisis is resolved. If alpha_s is unchanged from -0.069, the O-Z form is indeed the correct propagator and the 6 sigma tension is structural.

2. **FABRIC-PHASE-96**: The full 96-mode (3 phases x 32 cells) coupled oscillator diagonalization. The hybridized Goldstone-Leggett mode frequency determines whether the 18% discrepancy improves at the fabric level.

3. **J-PAIR-CALIBRATE-50**: Independent calibration of J_pair from the pair-transfer matrix element. FABRIC-NPAIR-49 PASS is conditional on this.

---

## Section 5: Closing Observations

### The Session's Structural Achievement

Session 49 ran 20 computations and delivered 13 permanent structural results. The session's central discovery -- that the Leggett mode IS the 3He dipolar analog, breaking U(1)_7 through inter-sector Josephson coupling with a computable epsilon = 0.00248 -- is the first mechanism in the framework's history to produce a Goldstone mass at the correct order of magnitude.

From the Landau perspective, this is the correct structural identification. In 3He-A, the spin-orbit dipolar interaction is an external perturbation to the BCS Hamiltonian that locks the relative orientation of spin and orbital order parameters, breaking the SO(3)_S x SO(3)_L symmetry to SO(3)_{S+L}. The Leggett frequency omega_L ~ sqrt(F_D/chi) emerges from the competition between dipolar stiffness (F_D, small) and the susceptibility of the relative orientation (chi, set by the BCS gap). The framework's J_23 plays the role of F_D, and rho_B2 plays the role of chi. The ratio omega_L1/Delta_B2 = 0.095 is 95x larger than the 3He ratio (~10^{-3}), reflecting the strong inter-sector coupling in the compact SU(3) geometry compared to the weak spin-orbit interaction in helium.

### The alpha_s Tension as a Structural Diagnostic

The alpha_s = n_s^2 - 1 identity (W1-L) is the kind of result Landau valued most: an algebraic identity that follows from the functional form of the propagator, independent of all coupling constants. It is structurally clean. Its tension with Planck (6 sigma) is therefore not a failure of parameter tuning but a test of the FUNCTIONAL FORM of the propagator.

If the multi-pole Leggett propagator (Section 3, S-2) resolves the tension, then alpha_s becomes a SUCCESS of the framework: the running is sensitive to the pole structure of the inter-band Josephson coupling, which is a framework-specific prediction. If the multi-pole corrections are insufficient, then the O-Z form is the wrong effective theory for the CMB power spectrum, and the framework needs a different mechanism entirely to connect fabric-scale physics to the CMB.

The decisive computation is the 3-pole running (eq. (3)). It is analytic, requires no new data beyond the existing S48 Leggett parameters, and can be completed in a single computation. This should be the highest priority for Session 50.

### What Condensed Matter Theory Says About the Path Forward

The framework has arrived at a recognizable condensed matter problem: a multi-band superconductor on a disordered lattice, with inter-band Josephson coupling providing the pseudo-Goldstone mass, and the power spectrum of phase fluctuations encoding the observational tilt n_s.

The technology for solving this problem exists in the condensed matter literature. The phase-fluctuation propagator in multi-band superconductors has been computed for MgB2 (two bands), iron pnictides (up to five bands), and nuclear pairing (multiple shells). The general result is that inter-band coupling modifies the low-energy propagator in ways that depend on the NUMBER of bands, the HIERARCHY of Josephson couplings (J_12 >> J_23 >> J_13 in the framework), and the STIFFNESS anisotropy (rho_B2 >> rho_B1, rho_B3).

The framework has a specific structure: 3 bands with strong hierarchy (J_12/J_23 = 19.52, algebraic constant), extreme stiffness anisotropy (rho_C2/rho_su2 = 24.4x from S47), and a granular fabric (32 cells with Z_3 walls). This determines the propagator completely. The remaining question -- whether the multi-pole structure resolves the alpha_s tension or confirms it as structural -- is a well-posed computation that Landau theory is designed to answer.

---

**Files referenced in this review:**
- `tier0-computation/s49_bragg_goldstone.{py,npz,png}` (my computation, W1-C)
- `tier0-computation/s49_leggett_transit.{py,npz,png}` (my computation, W1-H)
- `tier0-computation/s49_dipolar_catalog.{py,npz,png}` (W1-S, Volovik)
- `tier0-computation/s49_alpha_s_bayes.{py,npz,png}` (W1-L, Nazarewicz)
- `tier0-computation/s49_multi_t_friedmann.{py,npz,png}` (W1-E, Einstein)
- `tier0-computation/s49_hfb_backreaction.{py,npz,png}` (W1-I, Nazarewicz)
- `tier0-computation/s49_leggett_gge.{py,npz,png}` (W1-T, Nazarewicz)
- `tier0-computation/s48_leggett_mode.{py,npz,png}` (S48 Leggett data)
- `sessions/session-47/session-47-crystal-geometry-landau-collab.md` (S47 collab)
- `sessions/framework/landau-classification-of-phonon-exflation.md` (classification document)
