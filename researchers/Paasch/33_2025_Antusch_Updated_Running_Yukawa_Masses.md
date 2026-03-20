# Updated Running Quark and Lepton Parameters at Various Scales

**Author(s):** Stefan Antusch, Kevin Hinze, Shaikh Saad

**Year:** 2025

**Journal:** arXiv:2510.01312

---

## Abstract

The running of quark and lepton Yukawa couplings across multiple energy scales is a cornerstone of flavor physics and tests of physics beyond the Standard Model. This paper revisits the evolution of these parameters incorporating the latest 2024 Particle Data Group determinations, which feature significantly smaller uncertainties compared to 2022 data. The authors present evolved parameter values at benchmark scales from the Z-boson mass (91.2 GeV) to the GUT scale (10^16 GeV) within both the Standard Model and the minimal supersymmetric extension (MSSM). For MSSM scenarios, results include various tan(β) values with supersymmetry breaking at 3 and 10 TeV, incorporating approximate threshold corrections.

---

## Historical Context

The renormalization group evolution (RGE) of Yukawa couplings was first systematically studied in the 1980s following the development of the Standard Model. These running parameters are essential because:

1. **High-scale constraints**: GUT-scale predictions require evolved values from low-energy measurements
2. **SUSY thresholds**: The MSSM predicts significant corrections at the SUSY-breaking scale
3. **Precision tests**: Small improvements in PDG measurements propagate through RGE codes to constrain BSM models
4. **Hierarchy testing**: Yukawa running encodes the flavor problem at the quantum level

The 2024 PDG update represents a quadrennial refinement with improved lepton mass measurements and more precise CKM determinations. This paper's primary contribution is numerical: providing the community with the latest baseline running masses for phenomenology and model-building purposes.

---

## Key Arguments and Derivations

### Standard Model RGE

The one-loop running of the up-type Yukawa coupling $Y_u^i$ (for generation $i$) follows:

$$\frac{d Y_u^i}{d \ln \mu} = \frac{1}{16\pi^2} Y_u^i \left( 3 \text{Tr}(Y_u^\dagger Y_u) + \text{Tr}(Y_d^\dagger Y_d) + \text{Tr}(Y_e^\dagger Y_e) - \frac{16}{3} g_3^2 - 3 g_2^2 - \frac{13}{9} g_1^2 \right)$$

where $g_i$ are the gauge couplings, and the trace terms represent contributions from all three generations. Down-type and charged lepton Yukawas evolve similarly, with different coefficients for the gauge interactions.

The quark mixing matrix CKM and neutrino mixing matrix PMNS evolve differently. In the SM, the CKM matrix receives corrections that preserve unitarity to machine precision. The lepton sector is more complex due to the presence of neutrino masses via the seesaw mechanism.

### Benchmark Scales

The paper reports results at six benchmark energy scales:

- **M_Z** = 91.2 GeV (electroweak scale, primary output scale)
- **M_W** = 80.4 GeV (W boson mass)
- **M_top** = 172.8 GeV (top quark pole mass)
- **M_GUT** = 2 × 10^16 GeV (approximate unification scale)
- **Intermediate scales** for SUSY phenomenology

At each scale, the evolution accounts for the threshold corrections from all heavier fermions and bosons that decouple.

### MSSM Modifications

In the MSSM, the Yukawa couplings run differently due to:

$$\frac{d Y_u^i}{d \ln \mu} = \frac{1}{16\pi^2} Y_u^i \left( 3 \text{Tr}(Y_u^\dagger Y_u) + \text{Tr}(Y_d^\dagger Y_d) + \text{Tr}(Y_e^\dagger Y_e) - \frac{16}{3} g_3^2 - 3 g_2^2 - \frac{13}{9} g_1^2 + \text{SUSY corrections} \right)$$

The SUSY corrections depend on tan(β), the ratio of Higgs VEVs. Large tan(β) scenarios (tan(β) > 10) can significantly modify the bottom and tau Yukawas due to enhanced corrections. The paper includes threshold effects at the SUSY-breaking scale (M_SUSY = 3 TeV and 10 TeV).

### Numerical Improvements

The 2024 PDG update improves precision in several areas:

- **Lepton masses**: electron, muon, tau measured to better than 0.1% accuracy
- **CKM elements**: improvements in |V_ub|, |V_cb|, phase δ from B-factory data
- **Quark masses**: running masses at 2 GeV determined from lattice QCD with reduced systematic uncertainty

These improvements propagate multiplicatively through RGE evolution, resulting in tighter constraints on BSM models that predict or constrain Yukawa values.

---

## Key Results

1. **Quark Yukawa running**: At M_Z, the top Yukawa is $y_t \approx 0.925$. At M_GUT in the SM, $y_t$ evolves to approximately 0.45-0.52 depending on the running scheme.

2. **Lepton Yukawa values**: The electron Yukawa at M_Z is $y_e \approx 2.8 \times 10^{-6}$, while the tau Yukawa is $y_\tau \approx 1.0 \times 10^{-2}$. The ratio $y_\tau / y_e \approx 3500$ at the electroweak scale.

3. **CKM unitarity**: Running CKM parameters remain unitary to better than 0.01% at all scales tested.

4. **SUSY threshold effects**: For tan(β) = 10 and M_SUSY = 3 TeV, the bottom Yukawa receives corrections of order +5% to +15% depending on stop/sbottom mixing parameters.

5. **Convergence**: The paper confirms that PDG 2024 updates yield numerical changes of 2-8% for most parameters compared to 2022 values, with larger changes (10-20%) in less-well-determined quantities like |V_ub|.

---

## Impact and Legacy

This paper serves a critical bookkeeping function for the flavor physics community. RGE running is a prerequisite for almost all flavor-symmetry models, BSM phenomenology, and GUT-scale predictions. By providing updated baseline values with 2024 precision, the paper eliminates ambiguity in comparisons between theory and experiment.

The work is frequently cited in papers proposing new flavor structures (e.g., discrete symmetries, extra dimensions, technicolor) because such models must first match the running SM values before proposing modifications. It also provides the baseline against which new physics searches (LHC flavor anomalies, rare decays, precision electroweak) are benchmarked.

---

## Framework Relevance

**Direct connection to phonon-exflation**: The Paasch relations (Papers 01-18) make quantitative predictions for particle mass ratios at a given renormalization scale. This paper's provision of running masses at multiple scales (especially M_Z and M_GUT) is essential for testing whether Paasch's formulae hold universally or only at a specific τ-determined mass scale.

In the phonon-exflation framework, particle masses emerge from Dirac spectral gaps in the SU(3) geometry at the fold (τ ≈ 0.2). Those gap values define an effective "natural" mass scale that may differ from M_Z or GUT convention. By providing evolved masses at many scales, this paper allows the framework to determine at which renormalization scale Paasch's empirical relations are best satisfied—a strong constraint on the mechanism.

**Application**: Use Antusch et al.'s running values to test Paasch's mass ratios at benchmark scales (M_Z, M_top, M_GUT). If ratios are scale-independent (as Paasch's classical phenomenological relations suggest), this validates that the framework's mass-gap origin is fundamental, not a low-scale artifact.

