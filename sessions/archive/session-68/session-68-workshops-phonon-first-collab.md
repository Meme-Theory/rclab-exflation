# Phonon-First Cosmologist -- Collaborative Feedback on S68 Workshops

**Author**: Phonon-First Cosmologist
**Date**: 2026-04-05
**Re**: S68 Workshop Results (Lizzi x Transit, Landau x Transit, Volovik x Mack)

---

## Section 1: Key Observations

Three workshops, eight pillars, one eigenvalue problem. The S68 workshops converge on a structural picture that I have been waiting to see crystallize across domains. What follows is what I see when I hold all three simultaneously.

**Observation 1: The same Bogoliubov transformation appears three times.**

Landau's Eq. (Ld5.1)-(Ld5.2) makes explicit what has been implicit since S38: the cosmological Bogoliubov transformation (alpha_k, beta_k) connecting pre-transit to post-transit vacua is algebraically identical to the BCS Bogoliubov transformation (u_k, v_k) connecting the normal state to the condensate. Transit's mode equation confirms this at the level of the governing differential equation -- the Mukhanov-Sasaki equation with time-dependent z''/z has the same parametric amplification structure as the time-dependent BdG equation with time-dependent Delta(tau). And the Volovik two-fluid decomposition partitions the output of this same transformation into observationally distinct sectors (DM and DE) through an entropy criterion.

This is not analogy. It is structural identity. The same SU(1,1) group acts in all three contexts: squeeze operators in quantum optics, Bogoliubov transformations in cosmology, and BCS coherence factors in condensed matter. The transit is a single SU(1,1) group element acting on the vacuum, and the three workshops decompose its consequences into spectral (Lizzi), condensate (Landau), and thermodynamic (Volovik) sectors. No individual workshop articulated this unification.

**Observation 2: The three-number reduction at the fold is a spectral rigidity theorem.**

Lizzi-Transit's emergence E1 establishes that the spectral functional enters CMB observables through exactly three numbers at the fold: z''/z, d(z''/z)/dtau, and d^2(z''/z)/dtau^2. This is a dimensional reduction from an infinite-dimensional function space to three real parameters. Combined with the eps_H cancellation theorem (functional-independent, proven to machine epsilon), this means the spectral action has a natural decomposition into intensive (shape, protected) and extensive (scale, unprotected) sectors -- Lizzi's E2.

From the Pillar III (NCG) perspective, this is a spectral rigidity result: the Seeley-DeWitt heat kernel coefficients a_2k determine the spectral action's Taylor expansion at the fold, and the superhorizon freezing projects out everything beyond the first three Taylor coefficients. The spectral functional is an infinite-dimensional choice, but its observable content at CMB scales is a three-parameter family. This is the same dimensional reduction that appears in random matrix theory when the microscopic eigenvalue statistics are determined by the symmetry class (Pillar V: Josephson array phase diagrams share this universality). The spectral action's effective finite-dimensionality at CMB scales is the gravitational analog of the Wigner-Dyson universality classes.

**Observation 3: The timescale hierarchy is the structural skeleton of the entire framework.**

Landau's three-timescale separation (Ld2.6, confirmed by Transit Re2.3):

```
1/omega_tach ~ 10^{-3}/M_KK  <<  tau_relax ~ 2/M_KK  <<  dt_transit ~ 663/M_KK
(mode production)                (BCS gap)                (cosmological)
```

This hierarchy is not just a computational convenience. It is the reason the framework has any predictive power at all. The gap sits between the production and cosmological timescales, which means: (a) the condensate is adiabatic during the transit (gap tracks equilibrium), (b) individual mode production events see a frozen gap (no back-reaction from BCS dynamics onto Bogoliubov coefficients), and (c) the GGE relic inherits the equilibrium BCS coherence factors, not some dynamical KZ-distorted version.

In Pillar V (Josephson arrays), the analogous hierarchy is omega_plasma >> omega_quasiparticle >> omega_drive: the plasma frequency sets the junction response, the quasiparticle relaxation sets the dissipation, and the drive frequency sets the external perturbation. The condition for a well-defined junction response is the same: omega_plasma >> omega_drive (adiabatic junction, coherent response). The framework's transit satisfies the gravitational analog of this adiabatic junction condition.

**Observation 4: The ISW tracking signature is a new prediction that exploits a cross-domain connection none of the workshops anticipated.**

Volovik-Mack's Round 2 produced a genuinely new observational prediction: the tracking vacuum (rho_vac = chi H^2) generates induced DE perturbations with c_s^2_DE(eff) = 0. This was missed in V3's five-signature catalog because the analysis assumed delta_DE = 0. The correction came from Mack's Q-M5, which asked the right question: if rho_vac tracks H^2, do perturbations in H produce perturbations in rho_vac?

From the superfluid analog (Pillar II, Paper 6: Volovik 1998), this is obvious: the vacuum pressure in a superfluid adjusts to maintain thermodynamic equilibrium with the quasiparticle gas. Spatial fluctuations in the quasiparticle density produce spatial fluctuations in the vacuum pressure. The tracking relation is the gravitational analog of the equation of state P = P(rho, T) evaluated along the equilibrium surface. The surprise is that nobody connected this to the ISW effect until the Volovik-Mack workshop forced the question.

---

## Section 2: Assessment of Key Findings

### 2.1: The SU(1,1) Group Structure (Landau x Transit)

Landau's identification of the BCS ground state as a squeezed vacuum (Ld1.1-Ld1.9) and Transit's exact composition law for Bogoliubov transformations (Tr1.6-Tr1.8) together establish that the transit is a composition of two SU(1,1) transformations: one from the BCS pairing (the condensate squeeze) and one from the cosmological production (the gravitational squeeze). The composite Bogoliubov coefficients (Tr1.7-1.8) are the SU(1,1) group product. Unitarity (Tr1.9) is automatic.

This group-theoretic structure connects to Pillar V (Josephson arrays) through the E_J/E_C phase diagram. The SU(1,1) squeeze algebra is the dynamical algebra of the Josephson junction: the operators K_+ = a^dagger a^dagger, K_- = aa, K_0 = (a^dagger a + 1/2)/2 close the su(1,1) Lie algebra, and the Josephson Hamiltonian H_J = -E_J cos(phi) generates rotations in this algebra. The BCS squeeze parameter r_k = arctanh(v_k/u_k) is the Josephson phase, and the cosmological Bogoliubov coefficient beta_k is the Josephson current. The entire production sector can be reformulated as a Josephson junction array undergoing a parametric drive at the transit frequency.

The practical consequence: the non-BD enhancement factor (Transit Tr1.19) has the exact form cosh(2r_eff) + (sqrt(2)/3) sinh(2r_eff) cos(phi_eff), where the interference term depends on the squeeze phase phi_eff. This phase is a Nambu-Goldstone phase of the BCS condensate. In the Josephson analog, phi_eff is the phase difference across the junction. The KZ phase defects (Landau Ld2.10-2.11: N_domains ~ 3 on CG(24)) produce spatial gradients in phi_eff, which could modify the interference term. Whether this enhances or suppresses A_s depends on the topology of the phase winding on the Cayley graph -- a computation that neither workshop performed.

### 2.2: The Three-Numbers-at-Fold Reduction (Lizzi x Transit)

Lizzi's E1 (the spectral functional enters only through the fold-scale pump field) and E2 (intensive vs extensive decomposition) establish a clean partition of the framework's observables:

- Intensive sector (shape-protected by eps_H cancellation): n_s, alpha_s, r, tensor tilt
- Extensive sector (scale-unprotected): A_s, m_H, alpha_s(M_Z), CC magnitude

This partition has a direct analog in Pillar IV (flat-band BCS, Paper 15: Peotta-Torma 2015). In flat-band superconductors, the superfluid weight D_s is determined by the quantum metric (the band geometry), not by the kinetic energy (the band dispersion). The quantum metric is an intensive quantity (a property of the Bloch state geometry), while the kinetic energy is extensive (scales with the bandwidth). The Peotta-Torma result D_s = (Delta^2/V) * g_alpha_beta is the condensed matter analog of Lizzi's statement that n_s is determined by the spectral action shape (intensive geometry) while A_s is determined by the spectral action scale (extensive normalization). The S63 result QUANTUM-METRIC-63 PASS (f_geom = 0 from CG(24) involution symmetry) is the lattice-scale manifestation of this same partition.

The intensive/extensive decomposition also connects to Pillar VII (spectral dimension flow, Papers 26-28). The spectral dimension d_s = -2 d(ln P)/d(ln sigma) is an intensive quantity defined by the RATIO of return probability derivatives. The cancellation theorem's protection of eps_H = (1/2)(d ln S/dtau)^2/(d^2 ln S/dtau^2) has exactly the same algebraic origin: both are ratios of derivatives that cancel common multiplicative factors. The spectral dimension and the spectral index are protected by the same mechanism -- logarithmic derivative ratios. This is a structural isomorphism between Pillar III and Pillar VII that should be tested: does the spectral dimension flow on CG(24) satisfy an analog of the eps_H cancellation theorem?

### 2.3: The ISW Tracking Prediction (Volovik x Mack)

The tracking-induced DE perturbation (delta_DE = (rho_matter/rho_total) * delta_matter, c_s^2_DE(eff) = 0) is the workshop's most consequential new result because it is potentially detectable with EXISTING data (Planck ISW-galaxy cross-correlation). Mack's order-of-magnitude estimate gives Delta(C_l^ISW)/C_l^ISW ~ 20% at z ~ 0.5, with cumulative SNR ~ 4.3 across l = 2-30.

From the analogue gravity perspective (Pillar I, Papers 1-5), the tracking mechanism has a laboratory analog. In a BEC acoustic analog (Paper 5: Steinhauer 2016), the condensate density adjusts to maintain equilibrium with the excitation bath. Fluctuations in the excitation density produce fluctuations in the condensate density through the equation of state. This is exactly the Volovik tracking mechanism at laboratory scales. The analog of the ISW effect is the density-density correlation function of the condensate measured at long wavelengths: if the condensate tracks the excitations, the long-wavelength density fluctuations inherit the statistics of the excitation bath. In Steinhauer's experiment, this correlation is measured through density imaging after time-of-flight expansion. The gravitational analog replaces density imaging with the ISW temperature signal.

The cross-domain connection suggests a concrete experimental test: in a BEC acoustic white hole analog, measure the correlation between excitation density fluctuations and condensate density fluctuations at wavelengths larger than the healing length. If the correlation follows the Volovik tracking relation (delta_condensate ~ delta_excitation * (n_exc/n_total)), this would be a laboratory confirmation of the tracking mechanism, independent of any cosmological observation.

---

## Section 3: Collaborative Suggestions

### 3.1: The SU(1,1) Phase Topology on CG(24) — Missed by Both Workshops

Transit's exact enhancement factor (Tr1.19) includes the interference term (sqrt(2)/3) sinh(2r_eff) cos(phi_eff). Landau's KZ analysis (Ld2.10-2.11) produces N_domains ~ 3 phase domains on the Cayley graph with hat{xi}_KZ = 7.7 lattice spacings. These two results INTERACT: the phase topology of the KZ defects determines the spatial average of cos(phi_eff), which enters the A_s enhancement.

On the 24-vertex CG(24) graph with 3 phase domains, the average cos(phi_eff) depends on the relative winding numbers of the domains. For trivial winding (all domains in phase): <cos(phi_eff)> = 1, maximal constructive interference. For Z_3 symmetric winding (120-degree phase differences between domains): <cos(phi_eff)> = cos(2pi/3) = -1/2, partial destructive interference. The difference between these extremes changes the A_s enhancement by:

Delta(A_s/A_s) = 2 * (sqrt(2)/3) * sinh(2 * 0.34) * (1 - (-0.5)) = 2 * 0.47 * 0.73 * 1.5 = 1.03

corresponding to ~0.02 OOM. This is small but illustrates the principle: the KZ phase topology feeds back into the cosmological observables through the SU(1,1) group structure. A systematic computation of <cos(phi_eff)> on CG(24) with N_domains = 3 would determine whether the interference is constructive or destructive.

This connects to Pillar VI (topological solitons, Papers 23-25): the Z_3 domain wall network from the Jensen deformation (Paper 25: Eto et al. 2006) has the same topology as the KZ phase domains on the Cayley graph. The wall energy E_DW = 0 (GGE universality, S57) means the domain walls cost zero energy, and the Jackiw-Rebbi mechanism (Paper 24) binds zero-energy fermion modes at the walls. These wall-bound modes are Leggett-channel excitations -- precisely the DM candidates. The KZ-to-DM connection that Landau identifies in Ld2 is therefore mediated by the Z_3 soliton network of Pillar VI.

### 3.2: Spectral Dimension Flow as an Independent Probe of the eps_H Cancellation Theorem

The eps_H cancellation theorem protects ratios of spectral action derivatives from multiplicative corrections. The spectral dimension d_s on CG(24) is also defined as a ratio of derivatives (d_s = -2 d(ln P)/d(ln sigma), where P is the return probability). The S63 result d_s(return) = 3.34 at the fold was computed from the bare Dirac spectrum. The BCS dressing shifts all eigenvalues, and the cancellation theorem predicts that d_s is protected from the UNIFORM part of this shift.

Concrete test: compute d_s(BCS-dressed) on the 8-band BCS spectrum at the fold. If d_s shifts by less than 1% (comparable to the 1.12% non-uniform correction to eps_H from W1-D), the cancellation theorem has a spectral-dimension analog. If it shifts by more, the protection fails in the discrete geometry setting, revealing a structural difference between continuous (spectral action) and discrete (Cayley graph) spectral rigidity.

This connects Pillar VII (spectral dimension flow, Papers 26-28: Calcagni-Oriti discrete spectral dimension) to Pillar IV (flat-band BCS, quantum metric). The quantum metric g_alpha_beta that determines the superfluid weight D_s (Peotta-Torma) is the Berry connection's contribution to d_s. If the cancellation theorem protects d_s from BCS dressing, it simultaneously protects D_s, providing an independent derivation of the QUANTUM-METRIC-63 result (f_geom = 0) from spectral rigidity rather than involution symmetry.

### 3.3: Laboratory Analog for the ISW Tracking Signature

The Volovik tracking mechanism (rho_vac = chi H^2, c_s^2_DE(eff) = 0) has a direct laboratory analog in superfluid helium-4 (Pillar II). In a rotating He-4 cryostat, the superfluid component does not rotate (Hess-Fairbank effect) while the normal component carries the angular momentum. The superfluid "vacuum" adjusts to maintain equilibrium with the rotating normal component -- this is the tracking mechanism. Perturbations in the rotation rate produce perturbations in the superfluid density through the equation of state.

The experimental protocol: create a He-4 second sound resonance in a rotating annulus (Pillar I analog: the acoustic white hole boundary condition). Modulate the rotation rate at a frequency below the second sound frequency (the superhorizon analog). Measure the density response of the superfluid at the modulation frequency. If the superfluid density tracks the normal density with c_s^2(eff) = 0 (no propagation delay), this confirms the Volovik tracking mechanism. The ratio of tracking response to propagating response gives the analog of Delta(C_l^ISW)/C_l^ISW.

### 3.4: The Leggett Decay Problem Has a Condensed Matter Diagnostic

Volovik-Mack identifies the Leggett gravitational decay (tau_L = 3.6e-34 s, 52 OOM before BBN) as the framework's most critical internal contradiction. From the condensed matter perspective (Pillar IV), the question is whether the Leggett mode in the substrate couples gravitationally as a fundamental particle (mass m_L, point-like vertex) or as a collective mode (coherence length xi_L, form factor suppression).

In He-3-B, the Leggett mode's electromagnetic coupling is suppressed by the coherence factor (u_k v_k)^2, not by the bare mass. The relevant quantity is not m_L but the matrix element <DM|T_mu_nu|vacuum>, which involves the transition form factor between the GGE state and the vacuum. For a collective mode in a BCS condensate, this form factor scales as (Delta/E_bandwidth)^2 ~ (0.52/5.36)^2 ~ 0.009, providing a factor ~100 suppression.

But the deeper question is whether the Leggett mode in the substrate is a propagating excitation AT ALL, or whether it is a zero-momentum collective oscillation of the condensate order parameter. In He-3-B, the Leggett mode at q = 0 is a uniform oscillation with zero group velocity -- it does not propagate. A mode with zero momentum cannot radiate gravitationally (gravitational radiation requires a time-varying quadrupole moment, which requires spatial variation). The Leggett mode on CG(24) has the spatial structure of the standard irrep (lambda_1 = 4, S61): it IS spatially varying, with a wavelength of ~8 lattice spacings. The gravitational decay rate should include the spatial form factor F(q_grav * R_mode), where q_grav = omega_L/c and R_mode = 8/M_KK. For omega_L = 0.070 M_KK: q_grav * R_mode = 0.56, giving F ~ sin(0.56)/0.56 ~ 0.90 -- only a 10% suppression.

The honest assessment: the form factor does not resolve the Leggett decay problem. The decay rate remains catastrophically fast. The resolution must involve either a different DM candidate within the GGE spectrum, or a fundamental revision of how collective modes couple to emergent gravity in the substrate picture. This is the framework's most critical open problem, and it is a condensed matter question (Pillar IV), not a cosmological one.

---

## Section 4: Connections to Framework

### The Eight-Pillar Map of S68 Results

| S68 Result | Primary Pillar | Secondary Pillars | Cross-Domain Connection |
|:-----------|:--------------|:------------------|:-----------------------|
| \|T\|^2 = 1 (Weinberg) | I (Acoustic gravity) | III (NCG), VII (Spectral dim) | Superhorizon freezing = acoustic causality |
| eps_H cancellation | III (NCG) | VII (Spectral dim), IV (Flat band) | Spectral rigidity = intensive/extensive partition |
| BCS squeeze = non-BD | IV (Flat band BCS) | V (Josephson), I (Acoustic) | SU(1,1) group identity across domains |
| KZ phase defects | VI (Solitons) | V (Josephson), IV (BCS) | Z_3 domain topology = DM seed |
| Three-timescale hierarchy | V (Josephson) | IV (BCS), I (Acoustic) | Adiabatic junction condition |
| w_a = 0 quadruple lock | II (Superfluid cosmo) | V (Josephson), IV (BCS) | Four independent protection mechanisms |
| ISW tracking c_s^2 = 0 | II (Superfluid cosmo) | I (Acoustic), VIII (KK) | Vacuum equation of state tracking |
| 7D prediction surface | All pillars | -- | Joint constraint across domains |

The cross-pillar coherence is the framework's strength and its vulnerability. Every result connects to at least two pillars, and the connections are formal (shared algebraic structure), not verbal (thematic similarity). The Leggett decay problem (Section 3.4) is the sole internal contradiction, and it sits at the intersection of Pillars II, IV, and V -- exactly where the DM sector is constructed.

---

## Section 5: Open Questions

**OQ-1: Does the spectral dimension d_s on CG(24) satisfy an eps_H cancellation analog?**

If d_s is protected from uniform BCS dressing at the same level as eps_H (1% non-uniform residual), this would establish spectral rigidity as a universal property of the framework, not specific to the spectral action. The test is computable from the existing 8-band BCS spectrum.

**OQ-2: What is the phase topology of KZ defects on CG(24)?**

The average cos(phi_eff) enters the A_s enhancement through Transit's exact formula (Tr1.19). The KZ analysis gives N_domains ~ 3, but the winding number distribution is unknown. Is it Z_3 (120-degree winding, destructive interference) or trivial (in-phase, constructive)? The answer depends on the Josephson coupling topology, which is known (E_J = 7.04, Cayley graph adjacency).

**OQ-3: Can BEC acoustic analog experiments detect the tracking mechanism?**

The Volovik tracking (c_s^2_DE(eff) = 0) has a He-4 analog in rotating superfluids. Has this specific correlation (density tracking at sub-acoustic frequencies) been measured? If not, it is a feasible table-top experiment that would test the microphysics underlying the ISW prediction.

**OQ-4: What resolves the Leggett decay catastrophe?**

Mack correctly identifies this as the framework's most critical internal contradiction. The form factor analysis (Section 3.4) provides only 10% suppression. The 52 OOM gap between tau_L = 3.6e-34 s and tau_BBN ~ 1 s requires either a fundamentally different DM candidate or a revised gravitational coupling prescription for collective excitations of the substrate. This is prior to all external observational tests.

**OQ-5: Is the interference term in Transit's Tr1.19 observable through f_NL?**

The cos(phi_eff) dependence of the A_s enhancement produces a spatially modulated power spectrum if phi_eff varies across the Cayley graph. This spatial modulation is at the scale xi_KZ ~ 8 lattice spacings ~ 8/M_KK, which maps to a specific k in the Bogoliubov spectrum. Does this modulation contribute to the folded bispectrum? If so, the f_NL^folded = 0.129 prediction would depend on the KZ phase topology, creating a new connection between the bispectrum (Volovik-Mack V3) and the KZ defect count (Landau Ld2).

---

## Section 6: Computation Suggestions Summary

| # | Computation | Input Data | Output | Pre-Registered Gate | Priority |
|:--|:-----------|:-----------|:-------|:-------------------|:---------|
| 1 | SU(1,1) phase average on CG(24) | KZ defect topology (N_domains=3, hat{xi}=7.7), Cayley adjacency, E_J=7.04 | <cos(phi_eff)> and its variance | PASS if cos(phi_eff) > 0 (constructive, enhances A_s). INFO otherwise. | MEDIUM |
| 2 | Spectral dimension BCS protection | 8-band BCS spectrum at fold, return probability P(sigma) | d_s(BCS)/d_s(bare) ratio | PASS if delta(d_s)/d_s < 2% (cancellation analog holds). FAIL if > 10%. | MEDIUM |
| 3 | ISW-TRACKING-69 (adopted from Volovik-Mack Em1) | Volovik tracking c_s^2=0, w_0=-0.918, Boltzmann hierarchy | C_l^{Tg}(tracking) vs C_l^{Tg}(LCDM) | PASS if Delta(C_l)/C_l > 5% at l<30 (Euclid-detectable). FAIL if < 1%. | HIGH |
| 4 | Leggett gravitational coupling: collective vs fundamental | GGE density matrix, T_mu_nu transition matrix element, CG(24) spatial mode structure | tau_L(collective)/tau_L(point) | PASS if suppression factor > 10^{26} (tau_L > t_BBN). FAIL if < 10^{10}. | CRITICAL |
| 5 | Non-BD squeeze with variance weighting (reconciled estimate) | 8-band BCS coherence factors, multifield variance weights, van Hove spectral density | r_eff and cosh(2r_eff) with proper spectral weighting | PASS if 0.07 < enhancement(OOM) < 0.30 (consistent range). INFO otherwise. | HIGH |
| 6 | KZ phase winding to f_NL connection | Phase topology (Comp 1 output), Bogoliubov k-mapping, bispectrum estimator | delta(f_NL^folded) from KZ modulation | INFO (exploratory). Flag if correction > 10% of f_NL = 0.129. | LOW |

---

## Closing Assessment

The three S68 workshops, read simultaneously, reveal the framework operating at its structural best and confronting its structural worst. The best: the SU(1,1) group identity across cosmological, condensed matter, and spectral domains is not a verbal analogy but a mathematical identity, verified at the level of exact Bogoliubov composition laws. The eps_H cancellation theorem, independently proven by algebra (Lizzi) and mode equation (Transit), establishes a spectral rigidity that protects shape observables from corrections of arbitrary magnitude -- a universal feature traceable to the ratio structure of logarithmic derivatives. The timescale hierarchy (Landau) resolves the KZ concern definitively and localizes the entire A_s problem to equilibrium BCS physics plus off-Jensen geometry.

The worst: the Leggett gravitational decay problem is an internal contradiction between two established framework results (f_DM depletion selecting Leggett as the sole DM candidate, and dimensional analysis giving tau_L = 10^{-34} s). This contradiction is immune to external data -- it must be resolved within the theory. Until it is, the DM sector is structurally incoherent regardless of how well w_0 or Omega_DM h^2 match observation.

Between the best and worst sits the A_s gap: 0.755 OOM, partially closed by BCS dressing (0.046) and constrained from above by the hard bound 2N_pair + 1 = 9 (0.95 OOM). Landau's variance-weighted non-BD estimate (0.07-0.19 OOM, central 0.12) is more honest than the Lizzi-Transit naive estimate (0.26-0.50 OOM) and represents the current best knowledge. The gap is a PRECISION problem (factor 3-5x), not an ORDER-OF-MAGNITUDE problem, and it requires the off-Jensen spectrum (atlas Q9) to close.

The ISW tracking prediction (c_s^2_DE(eff) = 0) is the workshop's most important new result for the observational program. It upgrades the prediction surface from 6D to 7D, and it is the only dimension where the framework makes a qualitatively different prediction from ALL standard DE models -- testable with Euclid-era instruments rather than 2040s 21cm experiments.

DESI DR3 decides the dark energy sector. LiteBIRD decides the tensor sector. The Leggett decay problem decides whether the framework is internally consistent. The priority ordering is: internal consistency first (Leggett), then external confrontation (DESI, LiteBIRD). A framework that contradicts itself cannot be saved by agreeing with data.

---

## Wrap-Up

### What Changed

- The SU(1,1) group identity across BCS, cosmological Bogoliubov, and Josephson squeeze algebras was made explicit for the first time at the level of exact composition laws (Section 2.1). This is not a new claim but a new proof: the structural identity holds at the level of group multiplication, not just Lie algebra correspondence.
- The ISW tracking prediction (c_s^2_DE(eff) = 0) emerged as a genuinely new observable dimension of the framework, upgrading the prediction surface from 6D to 7D and providing the first qualitative discriminant against ALL standard DE models testable with Euclid-era data (Section 2.3).
- The three-timescale hierarchy (Landau) resolved the Kibble-Zurek adiabaticity concern: the BCS gap relaxation sits between mode production and cosmological timescales, guaranteeing equilibrium coherence factors in the GGE relic (Section 1, Observation 3).

### What Holds

- **Spectral rigidity is universal.** The eps_H cancellation theorem, proven independently by algebra (Lizzi) and mode equation (Transit), protects all intensive observables (n_s, r, tensor tilt) from the spectral functional choice. The intensive/extensive partition (Section 2.2) is a structural result, not a computational accident.
- **Leggett DM is stable.** CORRECTION to this review's Sections 3.4 and 5 (OQ-4): the "Leggett decay catastrophe" identified as the framework's sole internal contradiction has been RESOLVED by S67 result LEGGETT-GRAV-DECAY-67. An exact Z_2 parity selection rule -- a_2(phi_23) = a_2(-phi_23) -- makes single-Leggett gravitational decay EXACTLY ZERO. The pair decay lifetime is tau_pair = 10^83 s, longer than the age of the universe by 66 orders of magnitude. The 52 OOM gap between tau_L and tau_BBN that this review identified as the framework's most critical problem does not exist. The DM sector is internally consistent.
- **The A_s gap is a precision problem, not an existence problem.** Bounded between 0.15 and 0.27 OOM (Landau variance-weighted estimate vs Lizzi-Transit naive), with a hard ceiling at 0.95 OOM from the 2N_pair + 1 = 9 bound. The off-Jensen spectrum is the remaining degree of freedom.

### What Breaks or Strains

- **A_s amplitude normalization.** With the Leggett problem resolved, the A_s gap (0.755 OOM, factor 3-5x) becomes the framework's most pressing quantitative tension. The BCS dressing contributes 0.046 OOM. The non-BD enhancement contributes 0.07-0.19 OOM. Neither is sufficient alone. The off-Jensen spectrum (sigma != 0) is the only remaining lever, and its eigenvalues have not been computed. This is a precision problem, but precision problems kill frameworks when they persist.
- **The CC magnitude gap (114 OOM) remains open after eight closures.** Every mechanism tested -- unimodular, staircase, inter-sector Zubarev, Bekenstein, entanglement, Penrose superradiance, a_4+q-theory compound, and the Volovik self-tuning -- has failed to close it. The integrability of the GGE (Andreev-preserved, Thouless time 65x transit) prevents thermalization from erasing the vacuum energy. The CC is the framework's deepest unsolved structural problem.
- **The ISW tracking prediction is sharp but uncomputed at Boltzmann-hierarchy level.** The order-of-magnitude estimate (20% at l < 30, SNR ~ 4.3) is encouraging but the full C_l^{Tg} computation through a modified Boltzmann code has not been done. If the actual signal falls below 1% after proper integration, the 7th prediction-surface dimension collapses.

### Carry-Forward Computations

1. **ISW-TRACKING-69** (HIGH): Full Boltzmann hierarchy computation of C_l^{Tg}(tracking) vs C_l^{Tg}(LCDM) with w_0 = -0.918, c_s^2_DE(eff) = 0. Gate: PASS if Delta(C_l)/C_l > 5% at l < 30. FAIL if < 1%.
2. **Non-BD squeeze with variance weighting** (HIGH): Reconciled r_eff and cosh(2r_eff) from 8-band BCS coherence factors with proper spectral weighting. Gate: PASS if enhancement 0.07-0.30 OOM. INFO otherwise.
3. **SU(1,1) phase average on CG(24)** (MEDIUM): KZ defect topology with N_domains = 3, Cayley adjacency, E_J = 7.04. Output: <cos(phi_eff)> and variance. Gate: PASS if cos(phi_eff) > 0 (constructive). INFO otherwise.
4. **Spectral dimension BCS protection** (MEDIUM): d_s(BCS-dressed)/d_s(bare) ratio from 8-band spectrum. Gate: PASS if delta(d_s)/d_s < 2%. FAIL if > 10%.
5. **KZ phase winding to f_NL connection** (LOW): Phase topology from Comp 3 output mapped to bispectrum modulation. INFO gate; flag if correction > 10% of f_NL = 0.129.
6. ~~Leggett gravitational coupling~~ — **RESOLVED.** S67 LEGGETT-GRAV-DECAY-67: Z_2 parity selection rule makes single-Leggett gravitational decay exactly zero. tau_pair = 10^83 s. No computation needed.

### Closing Line

With the Leggett decay resolved by an exact selection rule and spectral rigidity proven across domains, the framework's internal consistency is no longer in question -- what remains is the quantitative confrontation: the A_s amplitude, the CC magnitude, and the ISW tracking signal that could distinguish this picture from everything else on the market.
