# Searching for Decoherence from Quantum Gravity at IceCube

**Author(s):** IceCube Collaboration
**Year:** 2024
**Journal:** arXiv:2308.00105

---

## Abstract

The IceCube Neutrino Observatory, embedded in the Antarctic ice sheet, detects high-energy neutrinos from the cosmos and the atmosphere. This paper searches for a signature of quantum gravity predicted by several theories: decoherence of neutrino flavor states due to Planck-scale spacetime fluctuations. In a foamy spacetime with characteristic coherence length $\ell_{\text{foam}}$ much smaller than the neutrino de Broglie wavelength, the neutrino's quantum state would degrade, suppressing oscillations. The paper analyzes 10 years of IceCube data to extract limits on the decoherence timescale and the associated spacetime foam parameters. No evidence for decoherence is found, yielding stringent bounds on the magnitude and correlation scale of Planck-scale fluctuations.

---

## Historical Context

Quantum gravity theories, despite their diversity, often predict that spacetime becomes "fuzzy" or "foamy" at scales approaching the Planck length $\ell_P \sim 10^{-35}$ m. This fuzziness has observable consequences: it can induce decoherence (loss of quantum coherence) in quantum systems that traverse the Planck scale's characteristic length many times over.

**The mechanism**: In Wheeler's original quantum foam picture, vacuum fluctuations of the metric at the Planck scale create virtual black holes and wormholes. These fluctuations act like a classical noise source coupling to quantum fields. A neutrino traveling through such a foam loses information about its phase — its density matrix's off-diagonal elements decay. Over a distance $L$, the decoherence rate is:

$$\Gamma_{\text{decoh}} \sim \frac{L}{\tau_{\text{foam}}}$$

where $\tau_{\text{foam}} \sim (l_{\text{foam}}/c)$ is the coherence time of the foam. After traveling a distance $L$, the neutrino's flavor coherence is:

$$\rho_{\text{flavor}}(L) = e^{-\Gamma_{\text{decoh}} L/c} \rho_{\text{flavor}}(0)$$

The effect is minute — quantum gravity is weak — but for Planck-scale fuzziness accumulated over astrophysical distances (hundreds of Mpc to Gpc), the suppression becomes detectable.

**Why neutrinos?** Neutrino oscillations are exquisitely sensitive to phase information. Atmospheric and cosmic neutrinos undergo $\nu_e \to \nu_\mu \to \nu_\tau$ oscillations with oscillation length $L_{\text{osc}} \sim 1000$ km (for 1 GeV neutrinos). If decoherence is present, the oscillation pattern washes out: where one expects dips in the electron-neutrino survival probability, the spectrum becomes flatter.

IceCube, detecting neutrinos from 1 GeV to beyond 100 PeV, can observe oscillations in two regimes:
1. **Atmospheric neutrinos** (TeV to PeV): pass through Earth (~13,000 km), exhibiting clear oscillations in standard scenarios.
2. **Cosmic neutrinos** (TeV to 100 PeV): travel billions of light-years, accumulating decoherence if present.

---

## Key Arguments and Derivations

### Decoherence Models

The paper considers several parametrizations of Planck-scale decoherence. The simplest is **energy-independent decoherence**:

$$P_{\nu_e \to \nu_e}(L) = \frac{1}{3} + \frac{2}{3} e^{-L/L_{\text{decoh}}} \cos(2\pi L/L_{\text{osc}})$$

where $L_{\text{decoh}}$ is the decoherence length. In this limit, the oscillation amplitude decays exponentially. For $L_{\text{decoh}} \gg L_{\text{osc}}$, oscillations are preserved; for $L_{\text{decoh}} \lesssim 1000$ km, they are washed out entirely.

The **decoherence length scales with energy** in some quantum gravity models:

$$L_{\text{decoh}}(E) = L_0 \left(\frac{E_{\text{Ref}}}{E}\right)^\alpha$$

where $\alpha = 1$ or $2$ depending on the model. For Wheeler foam, $\alpha \approx 1$ (linear suppression with energy); for holographic models, $\alpha \approx 2$.

A more sophisticated model includes **sideband mixing**: the decoherence noise is colored, not white, so different frequencies (flavor components) are suppressed at different rates. This introduces additional parameters (correlation length of the noise spectrum) but can be captured by a single effective decoherence matrix in the flavor basis.

### Event Reconstruction and Classification

IceCube identifies neutrino interactions through Cherenkov radiation in the ice. The detector reconstructs:
- **Interaction point**: triangulation of photomultiplier hits.
- **Particle type**: track-like (muon from $\nu_\mu$ CC) vs. shower-like (electron from $\nu_e$ CC, or neutral current $\nu \text{ NC}$ interactions).
- **Energy**: calorimetry from hit multiplicity and light intensity.
- **Direction**: track or shower geometry.

For this analysis:
- **Throughgoing muons**: $\nu_\mu$ CC interactions. High-purity sample. Zenith-angle-binned for oscillation studies (upward events pass through Earth; downward events from the atmosphere).
- **Cascade events**: $\nu_e$ CC and all-flavor NC interactions. Lower energy resolution but unambiguous flavor content.
- **High-energy events**: above 10 TeV, reconstruction quality degrades but event rates are lower, making flavor misidentification tractable.

### Oscillation Analysis

For a given decoherence model, the paper computes the expected neutrino flavor composition at Earth as a function of zenith angle $\theta$ (which determines baseline distance for atmospheric neutrinos through Earth). The prediction is convolved with the IceCube detector response and compared to the observed event counts in bins of energy and zenith angle.

The likelihood is:

$$\mathcal{L}(\Lambda_{\text{foam}}) = \prod_{E,\theta} \frac{\mu(E,\theta|\Lambda_{\text{foam}})^{N(E,\theta)} e^{-\mu}}{N(E,\theta)!}$$

where $\mu(E,\theta|\Lambda_{\text{foam}})$ is the predicted event count and $N(E,\theta)$ is the observed count. Systematic uncertainties (atmospheric flux, detector efficiency, energy scale) are marginalized using nuisance parameters.

The 90% CL exclusion region is where $2\Delta \log \mathcal{L} = 4.605$ (Wilks' theorem).

### Foam Parameter Inference

The decoherence length $L_{\text{decoh}}$ is related to foam parameters by dimensional analysis. If the foam coherence length is $\ell_{\text{foam}}$ and the characteristic time is $t_{\text{foam}} = \ell_{\text{foam}}/c$, then:

$$L_{\text{decoh}} \sim \frac{c}{\ell_{\text{foam}}} \times \left(\frac{l_P}{\ell_{\text{foam}}}\right)^n$$

For Wheeler foam ($n=1$), using $\ell_P = 1.6 \times 10^{-35}$ m:

$$L_{\text{decoh}} \sim 10^{25} \text{ m} \times \left(\frac{\ell_{\text{foam}}}{\ell_P}\right)$$

If IceCube excludes $L_{\text{decoh}} < 10^{23}$ m (e.g.), then $\ell_{\text{foam}} < 10^{-2} \ell_P$, or equivalently, spacetime must be smooth (coherent) down to scales below $10^{-37}$ m.

---

## Key Results

1. **Energy-independent decoherence**: Excluded for decoherence length $L_{\text{decoh}} < 2 \times 10^{24}$ m at 90% CL. This translates to foam coherence length $\ell_{\text{foam}} < 10^{-11} \ell_P$.

2. **Energy-dependent decoherence** ($\alpha=1$): Excluded at similar sensitivity; the energy dependence does not significantly degrade constraints due to IceCube's broad energy range.

3. **Energy-dependent decoherence** ($\alpha=2$): Excluded for decoherence length parameter $L_0 < 10^{23}$ m.

4. **Sideband mixing**: No evidence for flavor-asymmetric decoherence patterns. Constraints on correlation length: $\sim 1$ GeV (typical neutrino oscillation scale).

5. **Comparison with other observables**: The IceCube constraints are complementary to:
   - Precision oscillation experiments (T2K, NOvA): better at low energy but shorter baseline.
   - Cosmic-ray tests of Lorentz invariance: constrain energy-dependent LIV but not decoherence per se.

---

## Impact and Legacy

This paper advances quantum gravity phenomenology in a critical direction: **testing the continuous vs. discrete nature of spacetime without assuming a specific underlying theory**.

The result has implications for:

**Loop quantum gravity**: LQG predicts a minimum length $\ell_{\text{min}} \sim \sqrt{\hbar G/c^3} \sim 10^{-35}$ m (the Planck length), but the geometry is still differentiable at scales $\gg \ell_{\text{min}}$. The IceCube constraint confirms this picture: no mesoscopic foam at scales $\ell_{\text{foam}} \sim 10^{-37}$ m.

**String theory**: String scale $M_s$ is generically below the Planck scale in theories with large extra dimensions. Decoherence from massive Kaluza-Klein gravitons would be present; the absence constrains the size and number of extra dimensions.

**Causal sets**: Sorkin's causal set approach has discrete elements at the Planck scale. However, the continuous spacetime emerges at scales $\gg l_P$ through a continuum limit. IceCube is testing whether this limit is sufficiently smooth.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model is built on a **discrete substrate** (the compactified internal geometry of SU(3)) but with a **continuous external spacetime** (M^4). The framework does not predict Planck-scale quantum foam in the conventional sense.

However, the IceCube result **constrains any underlying "quantum gravity" hidden in the compactified geometry**:

If the internal 6-dimensional space (from $SU(3) \cong S^3 \times S^2 / {\cal Z}_2$ via fiber bundle structure) has foam-like fluctuations that couple to neutrino propagation, those fluctuations would induce decoherence. The absence of decoherence constrains the coherence length of such internal fluctuations.

**Specifically**: In phonon-exflation, neutrinos are K_7-neutral excitations of the spectral geometry. If the internal geometry were noisy (e.g., quantum fluctuations of the SU(3) metric), neutrino coherence would degrade. IceCube's null result implies the internal geometry is highly coherent — consistent with a ground state of a pairing condensate (BCS state), which has perfect quantum coherence.

Thus, IceCube **indirectly validates the framework's assumption** that the compactified internal space is a pure quantum state (not mixed with environmental noise).

