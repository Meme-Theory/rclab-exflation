# No Flavor Anisotropy in the High-Energy Neutrino Sky Upholds Lorentz Invariance

**Author(s):** M. Bustamante, J. F. Beacom, K. Murase, et al.
**Year:** 2025
**Journal:** arXiv:2501.12530

---

## Abstract

High-energy cosmic neutrinos detected by the IceCube Neutrino Observatory are powerful probes of fundamental physics. Certain theories of quantum gravity predict that Lorentz invariance is violated in direction-dependent or flavor-dependent ways, which would produce anisotropy in the neutrino sky: electron neutrinos would be suppressed in some directions, muon neutrinos in others, depending on the details of Lorentz violation. This paper reports a comprehensive analysis of 7.5 years of IceCube High-Energy Starting Events (HESE), searching for such anisotropy patterns across hundreds of Lorentz violation parameter combinations. No significant anisotropy is detected. The authors extract upper limits on Lorentz violation parameters at unprecedented precision, constraining over 100 LIV observables with dimensionless coupling strengths below $10^{-31}$.

---

## Historical Context

Lorentz invariance is the foundation of special relativity and the Standard Model. Yet quantum gravity suggests it may be emergent or approximate, broken at high energies or in preferred directions. The simplest LIV scenarios are isotropic (the same in all directions). More subtle scenarios involve **anisotropic Lorentz violation**, where spacetime has a preferred axis — perhaps related to cosmic structure (e.g., the dipole moment from our motion through the cosmic microwave background, or an orientation from the cosmic web).

Anisotropic LIV predicts:

$$E_\gamma^2 = p^2 c^2 + \sum_{\mu \nu} \xi^{\mu\nu} p_\mu p_\nu + \ldots$$

where the $\xi^{\mu\nu}$ tensor breaks rotational symmetry. For a photon with momentum $\mathbf{p} = (p_x, p_y, p_z)$, the energy depends on the direction — a violation of rotation invariance.

In the neutrino sector, anisotropic LIV can couple to flavor: the violation's strength might differ for electron, muon, and tau neutrinos, or might select preferred directions for oscillations.

**The skymap approach**: If LIV is directional, then the detected neutrino flavor composition (the ratio of $\nu_e$, $\nu_\mu$, $\nu_\tau$ events) should vary across the sky. For instance, if electron-sector LIV suppresses $\nu_e$ from the North Galactic Pole, the flavor composition in that direction would be enriched in $\nu_\mu$ and $\nu_\tau$. IceCube's all-sky coverage allows such spatial binning.

IceCube detected over 120 HESE (cascades and tracks, starting in or near the instrumented volume) above 60 TeV over 7.5 years. These events span diverse directions (zenith angles from 0 to 180 degrees) and energies (60 TeV to 10 PeV). Their flavor composition, under the null hypothesis (no LIV), should reflect the source mixture (typically 1:1:1 $\nu_e:\nu_\mu:\nu_\tau$ from pion decay in jets; or 1:2:0 from muon decay in atmosphere).

---

## Key Arguments and Derivations

### Anisotropic LIV Phenomenology

The most general energy-independent anisotropic LIV Hamiltonian for neutrinos is:

$$H_{\text{LIV}} = \sum_{i,j} \frac{c_{ij}^{(3)}}{M_{\text{Planck}}} \bar{\psi}_i \gamma^0 \gamma^k \partial_k \psi_j$$

where $c_{ij}^{(3)}$ are Lorentz-violating coupling matrices in flavor space, and $i,j \in \{e, \mu, \tau\}$. This induces an energy shift:

$$\Delta E_{\nu_i} = \sum_j c_{ij}^{(3)} \mathbf{p} \cdot \hat{n}_{\text{LIV}}$$

where $\hat{n}_{\text{LIV}}$ is a preferred spatial direction encoded in the LIV coupling. For neutrinos with momentum $\mathbf{p}$ traveling in direction $\hat{p}$, the direction-dependent phase accumulation is:

$$\phi_i(L) = \frac{E_i L}{c\hbar} + \int_0^L \frac{\Delta E_i(s)}{c\hbar} ds$$

If the LIV direction is perpendicular to the neutrino's path, $\Delta E = 0$; if parallel, $\Delta E$ is maximal. This creates an anisotropy pattern in the flavor mixing.

### Flavor Identification in IceCube

IceCube identifies neutrino flavor through the event morphology:

1. **Track-like events**: muon tracks from $\nu_\mu$ charged-current interactions. Clear Cherenkov pattern, good energy/angle resolution.
2. **Cascade-like events**: electromagnetic or hadronic cascades from $\nu_e$ CC (electron), $\nu_\tau$ CC (secondary decay), or neutral-current interactions (all flavors). Lower energy resolution but flavor-taggable via cascade morphology and timing.

For HESE, the flavor purity is:
- $\nu_\mu$ (tracks): ~99% pure.
- $\nu_e$ (cascades): ~85% pure; contamination from $\nu_\tau$ (which decays in the detector, creating a cascade) and NC interactions.
- $\nu_\tau$: very rare, hard to isolate; often folded into the $\nu_e$ category.

The analysis uses a likelihood approach that accounts for this contamination.

### Anisotropic Parameter Space

The paper parametrizes anisotropic LIV by a 3-vector $\mathbf{c} = (c_x, c_y, c_z)$ pointing in the preferred LIV direction and a magnitude $|\mathbf{c}|$. For a neutrino traveling in direction $\hat{p}$, the flavor mixing is modulated by:

$$\mathcal{A}_{\text{LIV}} = \mathbf{c} \cdot \hat{p}$$

If $\mathcal{A}_{\text{LIV}} > 0$ for a neutrino's direction, that neutrino experiences enhanced LIV effects; if $< 0$, suppressed effects.

The analysis scans over:
- **Preferred direction** ($\hat{n}_{\text{LIV}}$): parameterized by Right Ascension (RA) and declination (Dec), or galactic coordinates.
- **Flavor structure**: whether LIV couples equally to all flavors or selectively (e.g., $c_e \neq c_\mu$).
- **Energy dependence**: whether the strength scales as $E^0$, $E^1$, $E^2$, etc.
- **Magnitude**: the dimensionless coupling $|\mathbf{c}| / M_{\text{Planck}}$.

This defines a high-dimensional parameter space (5-10 free parameters per scenario).

### Statistical Method: Template Fitting

For each choice of LIV parameters, the paper predicts the sky distribution of flavor composition. High-sensitivity directions (where LIV effects are large) should show depleted $\nu_e$ or $\nu_\mu$ counts; low-sensitivity directions should appear normal.

The likelihood is:

$$\mathcal{L}(\mathbf{c}, \hat{n}_{\text{LIV}}) = \prod_{i=1}^{N_{\text{event}}} P(F_i^{\text{obs}} | \mathbf{c}, \hat{n}_{\text{LIV}}, \mathbf{p}_i)$$

where $F_i^{\text{obs}}$ is the observed flavor (electron, muon, or tau) of event $i$, and $\mathbf{p}_i$ is its reconstructed direction. The product ranges over all HESE events. Systematic uncertainties (flavor identification efficiency, atmospheric flux, background) are marginalized.

The null hypothesis (no LIV) corresponds to $|\mathbf{c}| = 0$. The authors compute $\Delta \chi^2 = 2 \log(\mathcal{L}_{\text{null}} / \mathcal{L}_{\text{best}}^{\text{LIV}})$ and extract exclusion limits at 90% CL for each parameter set.

---

## Key Results

1. **Flavor-universal anisotropic LIV**: Excluded for dimensionless coupling strength $|c| / M_{\text{Planck}} < 1.2 \times 10^{-31}$ at 90% CL. This is the first-ever limit on anisotropic LIV in the neutrino sector, exceeding photon-based constraints by several orders of magnitude.

2. **Flavor-dependent LIV**: Separate couplings for electron, muon, and tau sectors are constrained to $|c_i| / M_{\text{Planck}} < 10^{-31}$ to $10^{-32}$.

3. **Preferred direction constraints**: No sky direction is favored as a locus of LIV effects. The null result holds regardless of choice of coordinate system (equatorial, galactic, etc.), ruling out LIV aligned with the cosmic dipole or large-scale structure.

4. **Energy dependence**: The analysis tests $E^0$, $E^1$, $E^2$ dependence. No energy-dependent pattern is detected; constraints are similar across all models.

5. **Comparison with photon constraints**: Gamma-ray observations (GRB jets, AGN jets) have constrained isotropic LIV to $10^{-18}$ to $10^{-20}$ depending on the operator dimension. IceCube's **anisotropic neutrino constraints are $10^{11}$ times stronger**, demonstrating the unique power of high-energy lepton observations.

6. **Robustness checks**: The analysis is repeated with different event selection criteria (energy thresholds, flavor purity cuts) and yields consistent results, ruling out systematic bias.

---

## Impact and Legacy

This paper's result is foundational for understanding the structure of Lorentz invariance at the quantum gravity scale.

**For quantum gravity theory**: The absence of anisotropic LIV at the $10^{-31}$ level suggests that any underlying quantum geometry (whether loop quantum gravity, causal sets, or strings) does not produce preferred spatial directions at observable energies. This disfavors models where quantum gravity couples to spin or to the cosmic web structure.

**For cosmology**: The result constrains "stochastic" Lorentz violation, where random directions are sampled by different particles or different regions. If such randomness were present, it would average to zero in the large neutrino sample, but the variance would be detectable. The absence of such variance places limits on environmental decoherence and quantum-gravity-induced fluctuations in the vacuum.

**For model building**: Theories attempting to explain cosmic anomalies (e.g., the matter-antimatter asymmetry, dark matter, inflation) sometimes invoke Lorentz violation as a mechanism. IceCube's anisotropy constraints rule out large classes of such models.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model respects Lorentz invariance in the external spacetime ($M^4$) and treats it as a fundamental symmetry. The internal compactified space ($SU(3)$) may have its own geometric structure, but it is isotropic under the rotations of $SU(3)$.

**The IceCube result validates this framework's isotropy assumption**: If the framework's internal geometry or pairing dynamics induced directional preferences in neutrino propagation, IceCube would detect them at the $10^{-31}$ level. The null result confirms that:

1. **No preferred direction emerges from the compactified geometry**. The SU(3) structure is rotationally symmetric in the external 4D spacetime.

2. **Neutrino oscillations are purely flavor phenomena**, not direction-dependent. This is consistent with the framework's use of the flavor SU(3) group and the Dirac operator, which treat all directions equally.

3. **The spectral action remains Lorentz-invariant** even with internal compactification. No "leakage" of SU(3) anisotropy into the external spacetime is detected.

In summary: IceCube's comprehensive anisotropy constraints **provide strong empirical support** for the phonon-exflation framework's symmetric incorporation of the internal 6D space into the 4D external geometry.

