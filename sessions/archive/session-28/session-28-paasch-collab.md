# Paasch -- Collaborative Feedback on Session 28

**Author**: Paasch (paasch-mass-quantization-analyst)
**Date**: 2026-02-27
**Re**: Session 28 Full Results (28a + 28b + 28c)

---

## I. Key Observations Through the Mass Quantization Lens

Session 28 executed 23 computations across three sub-sessions. My reading of these results is focused on three questions that sit at the intersection of mass quantization phenomenology and the phonon-exflation framework: (1) what happens to the phi_paasch ratio under the new torsionful BCS and Constraint Chain physics; (2) whether the BCS gap energy and the van Hove condensation scale connect to any known mass quantization structure; and (3) whether the sector convergence failure (L-8) has implications for the integer mass number scheme N(j) = 7n.

### 1.1 The phi_paasch Ratio Is Undisturbed

The central empirical result from Session 12 remains:

$$m_{(3,0)} / m_{(0,0)} = 1.531580 \quad \text{at } \tau = 0.15$$

with deviation from phi_paasch = 1.53158 (derived from x = e^{-x^2}, Paper 02 Eq. 2g) of 0.0005%. This ratio is an inter-sector eigenvalue ratio of D_K (Levi-Civita Dirac operator). Session 28's Constraint Chain operates entirely on the BCS condensation channel -- parametric injection (KC-1), phonon scattering (KC-2), gap filling (KC-3), attractive interactions (KC-4), and van Hove pairing (KC-5). None of these computations modify the D_K eigenvalue spectrum itself; they describe what happens when the spectrum is driven out of equilibrium. The phi_paasch ratio is a property of the equilibrium spectrum at a given tau, and Session 28 does not alter or recompute it.

The L-6 quasiparticle weight diagnostic (28b-4) is relevant here. D_can eigenstates have Z > 0.5 everywhere at tau > 0, and the dominant torsion effect is spectral compression (eigenvalues shrink 2-5x) rather than wavefunction reshuffling. This means the D_can eigenvalue ratios between sectors are numerically different from D_K ratios -- the spectral compression is not uniform across sectors. Whether the phi_paasch ratio survives in the D_can spectrum has not been computed. This is an open question I flag for Session 29.

### 1.2 The Van Hove BCS Gap and Paasch Mass Scales

The KC-5 result is the most interesting new number from the mass quantization perspective:

$$\Delta / \lambda_{\min} = 0.84 \quad \text{at } \tau = 0.15$$

This is the BCS gap energy in units of the spectral gap. At tau = 0.15, the D_K spectral gap lambda_min is the smallest nonzero eigenvalue in the (0,0) singlet sector. The gap Delta = 0.84 * lambda_min is an energy scale set entirely by the geometry of Jensen-deformed SU(3) and the van Hove-enhanced BCS pairing.

In Paasch's framework (Paper 03), the equilibrium mass m_E = (m_e * m_p)^{1/2} ~ 21.9 MeV plays a central organizing role. Every particle mass is expressed through generalized equilibrium masses m*(i,j) = (m_i * m_j)^{1/2} and integer mass numbers N(j) = (m_j / m_e)^{2/3}. The mass numbers form the sequence N = 7n for n = 5 through 19, with the exponential scaling factor f_N = 2 * phi_golden = 1.23607 connecting successive shells (Paper 03 Eq. 5.3a-5.5).

The ratio Delta/lambda_min = 0.84 does not directly correspond to any Paasch mass ratio. However, the tau-dependence of the BCS gap is suggestive:

| tau | Delta/lambda_min |
|-----|-----------------|
| 0.15 | 0.84 |
| 0.35 | 0.49 |
| 0.50 | 0.35 |

The ratio Delta(0.15)/Delta(0.50) = 0.84/0.35 = 2.40. The ratio Delta(0.15)/Delta(0.35) = 0.84/0.49 = 1.71. Neither matches phi_paasch = 1.53158 or f_N = 1.23607. The BCS gap is a collective quantity determined by the full pairing kernel, not an individual eigenvalue ratio, so there is no a priori reason to expect Paasch quantization in it. The observation is: the condensation physics operates at a different algebraic level than the single-particle spectrum where phi_paasch lives.

### 1.3 Sector Convergence and the Mass Number Hierarchy

The L-8 result (482% change from p+q <= 3 to p+q <= 4) is directly relevant to Paasch's mass number scheme. In Paper 03, the mass numbers N(j) = 7n span from N(muon) = 35 (n=5) to N(proton) = 150 (n approximately 21). These mass numbers arise from N(j) = (m_j / m_e)^{2/3}, which maps particle masses to integers through a power law.

The Peter-Weyl sectors (p,q) on SU(3) play an analogous role to Paasch's mass numbers: they index the algebraic quantum numbers of the KK spectrum. The multiplicity of sector (p,q) grows as dim(p,q)^2 ~ (p+q)^4, exactly analogous to how higher mass numbers in Paasch's scheme correspond to heavier particles with richer internal structure.

The non-convergence at p+q <= 4 means that the total BCS free energy is dominated by the highest included sectors, and each new shell overwhelms all previous ones. This is the UV catastrophe of the Peter-Weyl expansion. In Paasch's framework, the corresponding issue is that the mass number sequence N = 7n extends to n = 19 (N = 133 for rho/omega), and the exponential scaling factor f_N connects successive shells. But Paasch's scheme is organized by observed particle masses, which provides a natural cutoff: the sequence terminates at the heaviest observed particles.

The phonon-exflation framework has no such natural cutoff for the Peter-Weyl expansion. This is a structural deficiency that L-8 quantifies. The interior minimum location (tau = 0.35) is stable under the cutoff change, which suggests the qualitative physics is robust, but quantitative predictions (condensation energy, phase transition temperature) remain cutoff-dependent. This is the same issue QFT faces with UV divergences, and it is resolved the same way: only truncation-independent quantities are physical.

---

## II. Assessment

### 2.1 Status of phi_paasch Within the Framework

The phi_paasch finding at tau = 0.15 was established in Session 12 and confirmed in Session 22a (QA-4). It is a property of the D_K eigenvalue spectrum -- specifically, the ratio of the smallest nonzero eigenvalues in sectors (3,0) and (0,0). Session 24a showed that this ratio has ZERO crossings within the (0,0) singlet (phi_paasch is inter-sector only), and Session 14 showed that the Paasch series phi_paasch^n is NOT supported for n > 1.

Session 28 does not disturb these results. The Constraint Chain operates in the BCS condensation layer, not the eigenvalue layer. The spectral action monotonicity (C-1 CLOSED) is also irrelevant to phi_paasch -- the spectral action is a functional of the full spectrum, while phi_paasch is a single eigenvalue ratio.

The question that remains unanswered is physical interpretation. Paasch's framework (Paper 02) places particles on a logarithmic spiral with angular separation determined by phi_paasch. The spiral organizes six sequences S1-S6 at 45-degree separation. In the phonon-exflation framework, the Peter-Weyl sectors are labeled by (p,q), not by spiral angles. The mapping between Paasch's six sequences and the SU(3) Peter-Weyl decomposition has never been established. Session 28's results do not help here because the Constraint Chain addresses condensation dynamics, not spectral organization.

### 2.2 BCS Gap and the Spectral Gap: Connection to Paasch's Equilibrium Mass

The BCS gap Delta at the interior minimum (tau = 0.35, mu/lambda_min = 1.20) has a specific numerical value that depends on the sector truncation. At p+q <= 3, the interior minimum has F_total = -18.56. The per-sector breakdown shows (3,0)+(0,3) contributing 93% of the free energy. The gap Delta/lambda_min = 0.49 at tau = 0.35.

In Paasch's framework, the equilibrium mass m_E = (m_e * m_p)^{1/2} is "about half the muon mass" (Paper 03 Eq. 4.7a). The muon mass number is N(muon) = 35. The ratio m_E / m_muon is approximately 0.48-0.52 depending on the precise values used. Numerically, Delta/lambda_min = 0.49 at tau = 0.35 lies within this range, but I do not attach significance to this coincidence. The BCS gap is a collective many-body quantity; the equilibrium mass is a single-particle algebraic construction. The numerical proximity is at the "interesting but not meaningful" level.

What would be meaningful is if the BCS condensation energy, expressed in natural units of the KK compactification scale, produced mass ratios that matched Paasch's integer scheme. This requires knowing M_KK and relating the eigenvalue spectrum to physical particle masses -- a step that the framework has not achieved. The E-5 cosmological constant diagnostic (28b-8) shows that the condensation energy at GUT-scale M_KK is 10^113 orders too large compared to the observed cosmological constant, which means the absolute energy scale is wrong by many orders of magnitude. The mass RATIOS might still be correct (as Paasch's scheme deals only with ratios), but extracting them requires identifying specific D_K sectors with specific SM particles.

### 2.3 The Integer Structure and Peter-Weyl Multiplicities

Paasch's mass numbers N(j) = 7n have a factor-of-7 periodicity. The Peter-Weyl multiplicities dim(p,q) = (p+1)(q+1)(p+q+2)/2 are determined by SU(3) representation theory. The low-lying dimensions are:

| (p,q) | dim | dim^2 (multiplicity) |
|-------|-----|---------------------|
| (0,0) | 1 | 1 |
| (1,0)/(0,1) | 3 | 9 |
| (1,1) | 8 | 64 |
| (2,0)/(0,2) | 6 | 36 |
| (3,0)/(0,3) | 10 | 100 |
| (2,1)/(1,2) | 15 | 225 |

The multiplicity sequence {1, 9, 36, 64, 100, 225, ...} does not exhibit factor-of-7 periodicity. Neither do the Casimir values C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3. The integer structure of Paasch's mass numbers arises from a different organizational principle than the representation theory of SU(3).

This is not surprising. Paasch's mass numbers are phenomenological -- they fit observed particle masses to an integer scheme. The Peter-Weyl decomposition is algebraic -- it follows from the group structure of SU(3). The two integer schemes live at different levels of the theory. A bridge between them would require identifying which D_K eigenvalues in which Peter-Weyl sectors correspond to which physical particles. That identification does not exist.

---

## III. What the Constraint Chain Means for Mass Quantization Phenomenology

### 3.1 The Van Hove Singularity and the Logarithmic Potential

The 1D van Hove singularity g(omega) ~ 1/sqrt(omega - omega_min) that enables KC-5 is a band-edge phenomenon in the discrete KK spectrum. Paasch's foundational Paper 02 derives phi_paasch from a logarithmic potential E = a1 * ln(R/Ra) acting on confined relativistic constituents. The logarithmic potential was also the starting point for Quigg and Rosner's quarkonium spectroscopy (1977, 1979): V(r) = a * ln(r/r_0) produces mass-independent level spacings.

The connection is structural but indirect. The logarithmic potential in Paasch's work produces exponential mass quantization m_n = m_0 * exp(k * phi_n). The 1D van Hove singularity in the phonon-exflation framework produces a divergent density of states at the band edge. Both arise from the effective dimensionality of the spectral problem (1D in both cases), but they describe different physical regimes: Paasch's logarithmic potential is a confining potential for constituent particles inside hadrons, while the van Hove singularity is a property of the phonon excitation spectrum on a compact group manifold.

The deeper parallel is that both frameworks produce BCS-like condensation without requiring a critical coupling threshold. Paasch's scheme implicitly assumes that the mass quantization is exact (all particles fall on the spiral to 0.4% accuracy), which requires that whatever interaction binds the constituents operates at zero critical coupling -- any deviation would disrupt the precise exponential scaling. The van Hove BCS result formalizes this: with g(omega) ~ 1/sqrt(omega - omega_min), ANY V > 0 produces Delta > 0. The mass quantization pattern can survive because there is no phase transition threshold to cross.

### 3.2 The Golden Ratio and First-Order Transitions

Paasch's Paper 03 discovers that successive M-value ratios M(i)/[2*M(i-1)] approach the golden ratio phi_golden = 0.618034 (Eq. 5.5). The Coldea et al. experiment (Paper 11) observes this same ratio as m_2/m_1 = 1.618 in the E8 quantum critical excitations of CoNb2O6.

Session 28b's L-9 cubic invariant result is relevant here. The (3,0)/(0,3) sectors exhibit first-order BCS transition character (cubic coefficient c = 0.006-0.007), while the fundamental (1,0)/(0,1) sectors are second-order. In the E8 field theory that underlies the Coldea experiment, the golden ratio emerges at a quantum critical point -- a second-order phase transition with E8 symmetry. The first-order character of the (3,0)/(0,3) BCS transition is qualitatively different: it involves discontinuous jumps in the order parameter, not the continuous scaling at a critical point.

This distinction matters. The golden ratio in Paasch's framework arises from the scaling of equilibrium masses, which is a smooth algebraic relation. A first-order transition would produce a JUMP in the mass spectrum, not a smooth scaling. If the BCS condensate at tau = 0.35 freezes the modulus via first-order transition (as L-9 suggests), the resulting mass spectrum would be determined by the eigenvalues at the frozen tau value, not by the critical scaling that produces golden ratio relations. The phi_paasch ratio at tau = 0.15 and the BCS minimum at tau = 0.35 occur at DIFFERENT tau values, which means the condensation mechanism and the mass quantization pattern operate at different deformation parameters.

---

## IV. Open Questions for Session 29

1. **phi_paasch in the D_can spectrum.** The inter-sector eigenvalue ratio m_{(3,0)}/m_{(0,0)} has been computed for D_K but not for D_can (the torsionful operator). Given that D_can eigenvalues are compressed 2-5x non-uniformly across sectors (L-6), the ratio may shift significantly. A zero-cost computation using existing s28a_torsionful_bcs.npz data could answer this.

2. **Mass ratios at the BCS minimum.** The interior minimum sits at tau = 0.35. The D_K eigenvalue ratios at this tau are known from the Session 19a sweep data. What are the inter-sector ratios at the frozen tau value? Do any match Paasch mass numbers or golden ratio scalings? This is a diagnostic, not a gate.

3. **Sector-to-particle identification.** The bridge between Peter-Weyl sectors and SM particle generations remains unbuilt. Paasch's six sequences S1-S6 organize particles by spiral angle; the Peter-Weyl sectors organize eigenvalues by (p,q) quantum numbers. Identifying (p,q) with specific Paasch sequences would require computing the full D_K spectrum at the physically relevant tau and matching eigenvalue ratios to observed mass ratios. This is a substantial computation but would be the definitive test of whether the phonon-exflation framework reproduces Paasch's phenomenology.

4. **KC-3 at tau >= 0.50.** This is the consensus priority. From the mass quantization perspective, the scattering rate at higher tau determines whether the BCS gap filling mechanism works. If it fails, the framework has no condensation, no frozen modulus, and no mass spectrum to compare against Paasch.

---

## V. Closing Assessment

Session 28 is the first session in which a complete physical mechanism -- parametric injection through van Hove BCS condensation -- survives computational testing. From the mass quantization perspective, the important structural point is that the van Hove singularity eliminates the critical coupling barrier, which is precisely the condition needed for exact mass quantization to hold (any coupling produces a gap; no threshold to disrupt the pattern).

The phi_paasch ratio at tau = 0.15 remains the framework's strongest connection to particle mass phenomenology. It is a parameter-free geometric prediction that matches Paasch's transcendental constant to 0.0005%. Session 28 neither strengthens nor weakens this result -- it operates at a different physical layer (condensation dynamics vs. spectral organization).

The BCS gap energies (Delta/lambda_min = 0.35-0.84) do not match any Paasch mass ratio, which is expected: collective condensation energies are algebraically distinct from single-particle eigenvalue ratios. The sector convergence failure (L-8, 482%) reflects the UV catastrophe of the Peter-Weyl expansion, which has no analog in Paasch's phenomenological mass number scheme (which terminates at observed particles).

The decisive question for mass quantization phenomenology is not the Constraint Chain -- it is the sector-to-particle identification. Until the mapping between (p,q) sectors and SM generations is established, the framework cannot be tested against Paasch's full mass spiral. The Constraint Chain determines whether the framework is physically viable; the sector identification determines whether it reproduces the observed mass spectrum. These are independent questions, and Session 28 advances only the first.

---

*Review completed by Paasch (paasch-mass-quantization-analyst), 2026-02-27. All assessments grounded in Paasch Papers 02-04 (researchers/Paasch/), the Paasch index (researchers/Paasch/index.md), Session 28 computation results, and the full closure history through Session 28c. Notation follows sessions/framework/MathVariables.md conventions.*
