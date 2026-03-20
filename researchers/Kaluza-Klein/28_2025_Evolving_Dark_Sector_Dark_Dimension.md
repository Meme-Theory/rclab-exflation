# Evolving Dark Sector and the Dark Dimension Scenario

**Author(s):** Anchordoqui, L. A., et al.
**Year:** 2025
**Journal:** arXiv:2507.03090

---

## Abstract

The observed acceleration of the universe and the nature of dark matter remain among the most profound mysteries in cosmology. We propose a unified dark sector model in which both dark energy and dark matter originate from extra spatial dimensions. Specifically, dark energy is identified with a scalar field controlling the radius of a micron-sized extra dimension, while dark matter consists of Kaluza-Klein graviton excitations of this dimension. As the scalar field evolves, the dimension's size changes, modulating both the dark energy density and the mass of KK dark matter. This creates a fundamental correlation between the evolution of dark energy and dark matter properties. We demonstrate that the model achieves excellent agreement with recent observational data from DESI DR2 combined with Type Ia supernovae measurements, naturally explaining apparent phantom crossing (w<-1) without ad-hoc parameterizations. The framework remains consistent with fifth-force constraints and outperforms standard Lambda-CDM in Bayesian model selection.

---

## Historical Context

The "coincidence problem" — why dark matter and dark energy densities are comparable today, billions of years into cosmic history — has motivated numerous unified dark sector models since the 1990s. Early attempts (coupled quintessence models, 2000-2005) introduced ad-hoc interaction terms between the scalar field and matter. More elegant approaches emerged from higher-dimensional theories: Braneworld cosmology (Randall-Sundrum, ADD), DGP modified gravity, and emergent spacetime scenarios each offered geometric explanations for cosmic acceleration.

However, these frameworks struggled to simultaneously explain two observational facts: (1) the recent DESI DR1 and DR2 tension (w possibly evolving, phantom crossing), and (2) the mild but persistent S8 tension between CMB-inferred growth and late-time weak lensing measurements.

The dark-dimension scenario (Anchordoqui et al., 2024-2025) takes a bold step: it unifies dark energy and dark matter through the dynamics of a single extra dimension whose radius is controlled by a quintessence-like scalar field. This goes beyond traditional KK theory (which treats the extra dimension as static) by allowing the dimension to evolve with cosmic time. The result is a correlated evolution of dark matter mass and dark energy density — a prediction that distinguishes the model from independent dark energy and dark matter sectors.

---

## Key Arguments and Derivations

### The Extra Dimension with Evolving Radius

In the dark dimension scenario, spacetime is $(4+1)$-dimensional with metric:

$$ds^2 = -dt^2 + a^2(t) dx^i dx^i + R^2(t) dy^2$$

where $y \in [0, \pi]$ is the compact extra coordinate and $R(t)$ is the (time-dependent) compactification radius. Unlike static KK theory, $R$ evolves as:

$$R(t) = R_0 e^{-c \phi(t)}$$

where $\phi(t)$ is a cosmological scalar field and $c > 0$ is a coupling constant. The scalar field obeys:

$$\ddot{\phi} + 3H\dot{\phi} + V'(\phi) = 0$$

with potential:

$$V(\phi) = V_0 e^{-c_V \phi}$$

The exponential form is motivated by supergravity and string theory (Wetterich, 1988; Amendola, 2000).

### KK Graviton Spectrum and Dark Matter Mass

The 5D metric yields a Kaluza-Klein tower via dimensional reduction:

$$g_{MN}(x,y) = \sum_n g_{MN}^{(n)}(x) \psi_n(y)$$

The lowest-lying graviton mode ($n=1$) has mass:

$$m_\chi^{(1)} = \frac{\pi}{R(t)} = \frac{\pi}{R_0} e^{c \phi(t)}$$

As the scalar field evolves, $\phi(t)$ increases, causing $R(t)$ to shrink and $m_\chi^{(1)}$ to grow. The equation of state parameter is:

$$w_\phi = \frac{\langle \phi \rangle}{\langle V(\phi) \rangle}$$

For exponential potentials, $w_\phi$ approaches a fixed value if $3H = c_V \sqrt{3(1+w_\phi)}$ (tracking solution):

$$w_\phi^{\text{track}} = \frac{c_V^2 - 3}{c_V^2 + 3}$$

For $c_V = 1$: $w_\phi^{\text{track}} = -1/2$ (intermediate between matter and radiation). For $c_V = 0.5$: $w_\phi^{\text{track}} \approx -0.8$ (approaching dark energy).

### Energy Density and Friedmann Equations

The total energy density is split as:

$$\rho_{\text{tot}} = \rho_m + \rho_r + \rho_\phi$$

where $\rho_\phi = \dot{\phi}^2 / 2 + V(\phi)$ is the scalar field energy. The Friedmann equation is:

$$H^2 = \frac{\kappa^2}{3} \rho_{\text{tot}}$$

with $\kappa^2 = 8\pi G = 1/M_{\text{Pl}}^2$. The evolution of the scale factor $a(t)$ and scalar field $\phi(t)$ are coupled:

$$\frac{d}{dt} \ln a = H$$
$$\frac{d\phi}{dt} = \dot{\phi}$$

Substitution into the Friedmann equations yields a 2D system:

$$\frac{d}{dt} \ln a = \frac{\sqrt{3}}{3} \sqrt{1 + \frac{2V(\phi)}{\dot{\phi}^2}}$$

$$\ddot{\phi} = -3H\dot{\phi} - V'(\phi) = -\sqrt{3}(1 + w_\phi) H\dot{\phi} - V'(\phi)$$

### DESI DR2 Fit and Observational Constraints

The dark energy equation of state is parameterized as:

$$w(a) = w_0 + (1-a) w_a$$

or more precisely as $w(z) = w_0 + w_a \frac{z}{1+z}$ in redshift space. The DESI DR2 BAO measurements (combined with CMB from Planck) constrain:

$$w_0 = -0.72 \pm 0.05$$
$$w_a = 0.32 \pm 0.15$$

The dynamical-DE hint ($\sim 3.1\sigma$ tension with $\Lambda$CDM, Adame et al. 2024) becomes a natural **prediction** in the dark dimension model:

$$w(z) = \frac{\phi(z)}{3(1+\phi(z)/3)}$$

evolves from $w(z=0) \approx -0.72$ (today) to $w(z \to \infty) \approx -0.33$ (early universe), matching the DESI-favored direction of evolution.

### Correlation: Dark Energy and Dark Matter

The key innovation is that $m_\chi$ and $\rho_\phi$ evolve together. Define the ratio:

$$\mathcal{C}(t) = \frac{\dot{m}_\chi / m_\chi}{\dot{\rho}_\phi / \rho_\phi} = \frac{c \dot{\phi}}{2(V(\phi) + \dot{\phi}^2/2)/\rho_\phi}$$

For tracking solutions, this ratio is approximately **constant**, creating a non-trivial prediction for cosmological structure growth at early times (redshift $z \sim 10-1000$) when the DM mass was significantly different.

### Fifth-Force Constraints

Additional coupling of the scalar field to ordinary matter would generate a fifth force. The Compton wavelength is:

$$\lambda_C = \frac{1}{m_\phi} \approx \frac{1}{\sqrt{V''(\phi)}} \sim \text{mm (depending on parameters)}$$

Lunar ranging and atomic interferometry constraints (Adelberger et al., 2003) limit the effective Yukawa coupling:

$$\alpha_5 = \frac{1}{4\pi M_{\text{Pl}}^2} < 10^{-3}$$

The dark dimension model satisfies this by ensuring the scalar couples primarily to gravity (through geometry), not to Standard Model particles directly. Fifth-force tests thus allow:

$$c' \lesssim 0.2 \quad (\text{dimensionless coupling})$$

### Bayesian Model Comparison

The dark dimension model is compared to $\Lambda$CDM and other dynamical DE models using Deviance Information Criterion (DIC) and Bayes factors. The analysis shows:

$$\Delta \text{DIC}_{\text{dark dim}} - \Delta \text{DIC}_{\Lambda\text{CDM}} \approx +15 \, (\text{relative to data})$$

indicating **moderate evidence** for the dark dimension scenario over $\Lambda$CDM when DESI DR2 + SNe data are combined. This is not definitive but notable given the model has only 2 new parameters ($V_0$, $c_V$) vs. $\Lambda$CDM's 6 (baryon density, CDM density, Hubble constant, optical depth, scalar tilt, scalar amplitude).

---

## Key Results

1. **Unified dark sector**: Dark energy and dark matter arise from the dynamics of a single extra dimension, reducing degrees of freedom compared to independent-sector models.

2. **Correlated evolution**: As dark energy density decreases, the KK graviton mass (dark matter mass) increases. This correlation is testable through structure growth observations.

3. **DESI DR2 agreement**: The model fits the observed dynamical DE hint ($w_0 \approx -0.72$, $w_a \approx +0.32$) naturally, without post-hoc parameterization. Phantom crossing ($w < -1$) is explained geometrically (expansion of the internal dimension slowing as the universe ages).

4. **Phantom behavior without instability**: Traditional dynamical DE models with $w < -1$ often suffer from ghosts (negative-kinetic-energy modes) or instabilities. The dark dimension scenario avoids these by construction (the "phantom" arises from geometry, not from the effective fluid).

5. **Consistency with fifth-force tests**: The model satisfies laboratory and astrophysical constraints on additional light forces, remaining viable even as precision tests tighten.

6. **S8 tension reduced**: Preliminary analysis suggests the modified growth rate (due to evolving DM mass at high redshift) slightly reduces tension with weak-lensing measurements, though this requires further study.

---

## Impact and Legacy

This paper represents a watershed moment in the cosmological use of extra dimensions. Unlike traditional KK theory (treating the dimension as a fixed calculational artifact), the dark dimension scenario elevates the compactification radius to a dynamical variable with direct observational consequences.

**Paradigm shift**: From "extra dimensions are unobservable calculational tools" to "extra dimensions are the origin of observed cosmic acceleration and matter properties."

**Observational program**:
- DESI DR2 and DR3 (continuing BAO measurements) will test the $w(z)$ prediction
- Future weak-lensing surveys (Vera Rubin, Euclid, LSST) will probe structure growth at $z \sim 0.5-1$
- CMB-S4 will measure $N_{\text{eff}}$ and detect or exclude the predicted DM mass evolution at CMB decoupling

**Theoretical extensions**: Anchordoqui et al. have already explored connections to string theory (the scalar $\phi$ as a modulus field) and inflation (the extra dimension's size as a slow-roll field during early universe).

---

## Framework Relevance

The phonon-exflation framework proposes a qualitatively different mechanism: cosmic acceleration arises from the *internal* SU(3) compactification (driven by instanton dynamics and spectral geometry), not from the radius of an *external* fifth dimension.

**Parallels**:
- Both models treat compactification radius as dynamical
- Both predict correlations between high-energy particle masses and low-energy cosmology
- Both show tension with $\Lambda$CDM in DESI DR2

**Contrasts**:
- Dark dimension: scalar field $\phi$ controls radius; $\phi$ is coupled to an external "dark sector"
- Phonon-exflation: M4 x SU(3) geometry is *self-contained*; no external scalar. The "radius" of SU(3) is determined by BCS condensate dynamics (session 35)
- Dark dimension: predicts KK gravitons as dark matter mediators (still requires extra-dimensional particles)
- Phonon-exflation: derives dark matter from Dirac-sea topology (no new particle types)

**Critical difference**: The dark dimension model relies on a *single* extra-dimensional mediator (the KK graviton). If LHC searches exclude KK gravitons at 1-5 TeV (as #26 suggests for other models), dark dimension faces fine-tuning pressure. The phonon-exflation framework avoids this by deriving both DM and DE from *internal* structure (no TeV-scale new particles beyond the Standard Model).

**Connection**: The dark dimension scenario's success in fitting DESI DR2 validates the physics of evolving compactifications. Phonon-exflation achieves this via internal geometry — a more economical realization of the same principle.

---

