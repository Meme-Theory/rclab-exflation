# The Development of Irregularities in a Single Bubble Inflationary Universe

**Authors**: S. W. Hawking
**Year**: 1982
**Journal**: *Physics Letters B*, **115**, 295--297

---

## Abstract (Analytical Summary)

Hawking calculates the spectrum of density perturbations generated during inflation in the "new inflation" (slow-roll) scenario. He shows that quantum fluctuations of the inflaton field, amplified by the exponential expansion, produce a nearly scale-invariant (Harrison--Zel'dovich) spectrum of adiabatic perturbations with amplitude $\delta\rho/\rho \sim H^2/\dot{\phi}$. This paper, along with simultaneous and independent work by Starobinsky (1982), Guth and Pi (1982), and Bardeen, Steinhardt, and Turner (1983), established the theory of inflationary perturbations that is now the standard framework for understanding the origin of cosmic structure and the CMB anisotropies measured by COBE, WMAP, and Planck.

---

## Historical Context

### The Inflationary Revolution

In 1981, Alan Guth proposed "old inflation" to solve the horizon, flatness, and monopole problems. The idea was that the universe underwent an exponential expansion driven by the vacuum energy of a scalar field (the inflaton) stuck in a false vacuum. The problem with old inflation was the "graceful exit" -- the phase transition to the true vacuum would proceed by bubble nucleation, and the bubbles would never percolate (the space between them expands too fast).

Linde (1982) and Albrecht and Steinhardt (1982) proposed "new inflation" (slow-roll inflation), where the inflaton slowly rolls down a potential, generating quasi-exponential expansion. The exit from inflation occurs smoothly as the field reaches the potential minimum. This solved the graceful exit problem.

### The Perturbation Question

With inflation solving the horizon and flatness problems, the next question was: can inflation also explain the observed structure of the universe? The CMB has temperature anisotropies of order $\delta T/T \sim 10^{-5}$ on large scales, and the galaxy distribution shows structure on scales up to $\sim 100$ Mpc. Where did these come from?

The answer, proposed independently by Hawking, Starobinsky, Guth and Pi, and others in 1982, is that quantum vacuum fluctuations of the inflaton field during inflation are stretched to macroscopic scales and become the seeds of cosmic structure.

### The Cambridge 1982 Workshop

The key results were presented at the Nuffield Workshop on the Very Early Universe in Cambridge (June--July 1982). This is one of the most consequential workshops in the history of cosmology. Hawking, Starobinsky, Guth, and others presented their calculations, and the broad framework was established.

---

## Key Arguments and Derivations

### The Inflaton and Slow-Roll

The inflaton field $\phi$ with potential $V(\phi)$ drives inflation when the slow-roll conditions are met:

$$\epsilon = \frac{M_P^2}{2}\left(\frac{V'}{V}\right)^2 \ll 1, \qquad |\eta| = M_P^2 \left|\frac{V''}{V}\right| \ll 1$$

where $M_P = (8\pi G)^{-1/2}$ is the reduced Planck mass. During slow roll, the Hubble parameter is approximately constant:

$$H^2 \approx \frac{V(\phi)}{3M_P^2}$$

and the field evolves as:
$$3H\dot{\phi} \approx -V'(\phi)$$

### Quantum Fluctuations of the Inflaton

The inflaton field can be decomposed into a homogeneous background $\phi_0(t)$ and perturbations $\delta\phi(t, \mathbf{x})$:

$$\phi(t, \mathbf{x}) = \phi_0(t) + \delta\phi(t, \mathbf{x})$$

The perturbation $\delta\phi$ is a quantum field in the de Sitter background. In Fourier space, each mode $\delta\phi_k$ satisfies:

$$\ddot{\delta\phi}_k + 3H\dot{\delta\phi}_k + \frac{k^2}{a^2}\delta\phi_k = 0$$

where $a(t) = e^{Ht}$ is the scale factor. The solution is:

$$\delta\phi_k = \frac{H}{\sqrt{2k^3}} \left(1 + \frac{ik}{aH}\right) e^{ik/aH}$$

(choosing the Bunch--Davies vacuum). The key behavior:

- **Sub-horizon** ($k \gg aH$): oscillatory, $|\delta\phi_k| \sim 1/\sqrt{2k} \cdot a^{-1}$ (standard vacuum fluctuations, redshifting)
- **Super-horizon** ($k \ll aH$): frozen, $|\delta\phi_k| \to H/\sqrt{2k^3}$

When a mode "exits the horizon" (its physical wavelength exceeds the Hubble radius $H^{-1}$), its amplitude freezes at:

$$|\delta\phi_k|_{\text{freeze}} = \frac{H}{(2\pi)^{3/2}} \cdot \frac{(2\pi)^{3/2}}{\sqrt{2k^3}} = \frac{H}{\sqrt{2k^3}}$$

The power spectrum of field fluctuations is:

$$\mathcal{P}_{\delta\phi}(k) = \frac{k^3}{2\pi^2} |\delta\phi_k|^2 = \left(\frac{H}{2\pi}\right)^2$$

This is **scale-invariant**: the amplitude $H/2\pi$ is the same for all modes (since $H$ is approximately constant during slow roll). The connection to the Gibbons--Hawking temperature is direct: $H/2\pi = T_{\text{GH}} / k_B$ (in natural units).

### From Field Fluctuations to Density Perturbations

The inflaton fluctuation $\delta\phi$ translates to a density perturbation. The key insight is that $\delta\phi$ causes different regions of space to end inflation at slightly different times:

$$\delta t = \frac{\delta\phi}{\dot{\phi}_0}$$

This time delay produces a curvature perturbation:

$$\mathcal{R} = H \, \delta t = \frac{H \, \delta\phi}{\dot{\phi}_0}$$

The power spectrum of the comoving curvature perturbation is:

$$\mathcal{P}_{\mathcal{R}}(k) = \left(\frac{H^2}{2\pi \dot{\phi}_0}\right)^2 = \frac{1}{2\epsilon} \left(\frac{H}{2\pi M_P}\right)^2$$

Evaluated at horizon exit ($k = aH$) for each mode. Since $H$ and $\dot{\phi}$ change slowly during inflation, the spectrum is nearly but not exactly scale-invariant.

### The Spectral Index

The departure from exact scale invariance is parameterized by the spectral index $n_s$:

$$\mathcal{P}_{\mathcal{R}}(k) \propto k^{n_s - 1}$$

To first order in slow-roll parameters:

$$n_s - 1 = -6\epsilon + 2\eta$$

A perfectly scale-invariant spectrum has $n_s = 1$ (the Harrison--Zel'dovich spectrum). Slow-roll inflation generically predicts $n_s$ slightly less than 1 (a "red tilt"), because $\epsilon > 0$ dominates. Planck (2018) measures $n_s = 0.9649 \pm 0.0042$, beautifully confirming this prediction.

### The Amplitude

The amplitude of the power spectrum is:

$$A_s = \mathcal{P}_{\mathcal{R}} = \frac{V}{24\pi^2 M_P^4 \epsilon}$$

Planck measures $A_s \approx 2.1 \times 10^{-9}$. This constrains the inflationary energy scale:

$$V^{1/4} \sim 10^{16} \text{ GeV} \times \left(\frac{\epsilon}{0.01}\right)^{1/4}$$

This is close to the GUT scale, which is suggestive but also means that detecting the tensor perturbations (gravitational waves, with amplitude $\propto \epsilon$) requires extraordinary sensitivity.

### Hawking's Specific Calculation

Hawking's 1982 paper works in the context of the "new inflation" potential (a Coleman--Weinberg type with a very flat plateau). His specific formula (in the notation of the paper) is:

$$\frac{\delta\rho}{\rho} \sim \frac{H^2}{\dot{\phi}}$$

evaluated at horizon crossing. This is equivalent to the modern formula $\mathcal{P}_{\mathcal{R}}^{1/2} = H^2/(2\pi\dot{\phi})$. Hawking estimates the numerical value and finds it consistent with the observed galaxy distribution if the inflaton potential has the appropriate shape.

### Gravitational Waves (Tensor Perturbations)

Hawking also notes that inflation produces gravitational waves with a nearly scale-invariant spectrum:

$$\mathcal{P}_T(k) = \frac{2}{\pi^2}\left(\frac{H}{M_P}\right)^2$$

The tensor-to-scalar ratio is:
$$r = \frac{\mathcal{P}_T}{\mathcal{P}_{\mathcal{R}}} = 16\epsilon$$

The consistency relation $r = -8 n_t$ (where $n_t$ is the tensor spectral index) is a prediction of single-field slow-roll inflation. Detecting $r$ would determine the energy scale of inflation.

---

## Physical Interpretation

### Quantum-to-Classical Transition

The inflationary perturbation mechanism involves a remarkable quantum-to-classical transition. Sub-horizon modes are genuine quantum fluctuations (zero-point oscillations of a harmonic oscillator). Once stretched beyond the horizon, the modes become classical (their quantum uncertainty is in the amplitude, not in whether they are there). The classicality arises because super-horizon modes have $k/aH \to 0$, and the commutator $[\delta\phi, \dot{\delta\phi}]$ becomes negligible relative to the anticommutator. This is decoherence without an environment (or rather, the environment is the sub-horizon modes that have been stretched beyond accessibility).

### The Gibbons--Hawking Connection

The amplitude of inflaton fluctuations $\delta\phi \sim H/2\pi$ is directly the Gibbons--Hawking temperature (in natural units). This connects inflationary perturbations to the thermal nature of the de Sitter vacuum. The perturbations can be thought of as thermal fluctuations at the de Sitter temperature, "frozen in" by the rapid expansion.

### Why Nearly Scale-Invariant?

Scale invariance follows from the approximate time-translation invariance of de Sitter space. Each mode exits the horizon at the same Hubble rate $H$, so each gets the same amplitude $H/2\pi$. The slight tilt ($n_s \neq 1$) comes from the slow evolution of $H$ and $\dot{\phi}$ during inflation -- i.e., from the departure from exact de Sitter symmetry.

---

## Impact and Legacy

### Observational Confirmation

The inflationary perturbation spectrum has been spectacularly confirmed:
- **COBE** (1992): First detection of CMB anisotropies, consistent with scale-invariant spectrum
- **WMAP** (2003--2010): Precise measurement of $n_s < 1$ (red tilt confirmed)
- **Planck** (2013--2018): $n_s = 0.9649 \pm 0.0042$, ruling out $n_s = 1$ at $> 8\sigma$

### The Standard Cosmological Paradigm

The inflationary perturbation calculation, together with the hot Big Bang model and dark energy, forms the standard $\Lambda$CDM cosmological paradigm. The six-parameter model fits all CMB observations to extraordinary precision.

### Non-Gaussianity

Hawking's calculation assumes linear (Gaussian) perturbations. Higher-order effects produce non-Gaussian correlations (three-point function, etc.). Planck's constraints on non-Gaussianity ($f_{\text{NL}} < 5$) strongly constrain alternatives to single-field slow-roll inflation.

### Multi-Field Inflation

In models with multiple fields (as in many string theory realizations), the perturbation spectrum can have isocurvature components and non-standard correlations. These are constrained but not excluded by Planck.

---

## Connections to Modern Physics

1. **CMB B-modes and tensor perturbations**: The BICEP/Keck experiments constrain $r < 0.036$ (2021), pushing the inflationary energy scale below $\sim 1.6 \times 10^{16}$ GeV. The next generation (CMB-S4, LiteBIRD) aims to probe $r \sim 10^{-3}$.

2. **Stochastic inflation**: For very long-wavelength modes, quantum fluctuations dominate over classical drift. Starobinsky's stochastic inflation (1986) treats $\delta\phi$ as a random walk. This leads to eternal inflation and the multiverse.

3. **Primordial black holes**: Large fluctuations on small scales can collapse to form primordial black holes. These are constrained by various observations and are candidates for (some of) the dark matter.

4. **Cosmological collider physics**: Heavy particles with mass $\sim H$ during inflation leave imprints in the non-Gaussian correlations of the CMB and large-scale structure (the "cosmological collider" signal). This is a window into particle physics at the inflationary energy scale.

5. **For the exflation framework**: In the exflation model, the inflationary expansion is driven by internal compactification rather than an inflaton potential. The perturbation spectrum would be determined by fluctuations in the compactification rate $\dot{\sigma}/\sigma$ rather than $\dot{\phi}$. The scale invariance would follow from the approximate constancy of $H$ during the exflation epoch, but the detailed spectrum (tilt, running, tensor-to-scalar ratio) would differ from standard single-field predictions. The multi-component nature of the internal geometry (multiple moduli fields for $SU(3)$) could produce distinctive non-Gaussian and isocurvature signatures.
