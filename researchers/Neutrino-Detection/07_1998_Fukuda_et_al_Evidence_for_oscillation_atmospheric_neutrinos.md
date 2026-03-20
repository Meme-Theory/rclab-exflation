# Evidence for Oscillation of Atmospheric Neutrinos (Super-Kamiokande)

## Bibliographic Information

- **Authors**: Y. Fukuda, T. Hayakawa, E. Ichihara, K. Inoue, ... T. Kajita, ...
  et al. (Super-Kamiokande Collaboration, ~120 authors)
- **Title**: "Evidence for Oscillation of Atmospheric Neutrinos"
- **Journal**: Physical Review Letters, Vol. 81, No. 8, pp. 1562--1567
- **Year**: 1998
- **DOI**: 10.1103/PhysRevLett.81.1562
- **Submitted**: July 10, 1998 (presented at Neutrino '98 conference, Takayama,
  Japan, June 5, 1998)
- **Nobel Prize**: 2015 (Takaaki Kajita, "for the discovery of neutrino
  oscillations, which shows that neutrinos have mass")

---

## Historical Context

### The Atmospheric Neutrino Anomaly

Cosmic rays (primarily protons and heavier nuclei) striking the Earth's
atmosphere produce showers of secondary particles, predominantly pions:

$$p + N \to \pi^{\pm} + X$$

The pions decay via:

$$\pi^+ \to \mu^+ + \nu_\mu, \qquad \mu^+ \to e^+ + \nu_e + \bar{\nu}_\mu$$

(and charge-conjugate processes). Counting the neutrino flavors in the full
chain, the naive expectation is:

$$R \equiv \frac{N(\nu_\mu + \bar{\nu}_\mu)}{N(\nu_e + \bar{\nu}_e)} \approx 2$$

(two muon-type neutrinos for every electron-type neutrino). This ratio is
modified at higher energies where muons reach the ground before decaying,
increasing $R$ above 2.

Beginning in the mid-1980s, underground detectors reported anomalous values of
this ratio:

- **Kamiokande** (1988): $R_{\text{obs}} / R_{\text{pred}} = 0.60 \pm 0.07$
  for sub-GeV events.
- **IMB** (1992): Similar deficit.
- **Soudan 2** (1997): $R_{\text{obs}} / R_{\text{pred}} = 0.64 \pm 0.11$.

The deficit was consistent with $\nu_\mu$ disappearing (oscillating to another
flavor) while $\nu_e$ remained unchanged. However, the statistical significance
was insufficient for a discovery claim, and alternative explanations (systematic
errors in atmospheric neutrino flux calculations, nuclear interaction
uncertainties) could not be excluded.

### The Super-Kamiokande Detector

Super-Kamiokande was designed to provide a definitive answer. Key specifications:

- **Location**: Mozumi mine, Kamioka, Gifu Prefecture, Japan. 1,000 m
  underground (2,700 m water equivalent overburden).
- **Detector volume**: 50,000 tonnes of ultrapure water in a cylindrical
  stainless steel tank (39.3 m diameter, 41.4 m height).
- **Inner detector**: 32,000 tonnes fiducial volume, instrumented with **11,146
  inward-facing 20-inch PMTs** (Hamamatsu R3600), providing 40% photocathode
  coverage.
- **Outer detector**: 18,000 tonnes water shielding, instrumented with 1,885
  outward-facing 8-inch PMTs for cosmic ray veto and containment check.
- **Energy threshold**: ~5 MeV (for supernova neutrinos); ~100 MeV for
  atmospheric neutrino analysis.
- **Angular resolution**: ~25 degrees for sub-GeV $e$-like events, ~3 degrees
  for multi-GeV $\mu$-like events.
- **Particle identification**: Cherenkov ring pattern -- $e$-like (fuzzy,
  showering) vs. $\mu$-like (sharp, non-showering) -- distinguished with
  >98% accuracy via likelihood analysis.
- **Construction**: 1991--1996. First data: April 1, 1996.

### Data Sample

The 1998 paper was based on **535 days** of data (April 1996 -- February 1998),
corresponding to a **33.0 kiloton-year** exposure. The dataset contained:

- **Sub-GeV events** ($E_{\text{vis}} < 1.33$ GeV): Fully contained in the
  inner detector.
  - $e$-like: 2,389 events (predicted without oscillations: ~2,500)
  - $\mu$-like: 2,134 events (predicted without oscillations: ~2,900)

- **Multi-GeV events** ($E_{\text{vis}} > 1.33$ GeV):
  - Fully contained (FC) and partially contained (PC) events.
  - $e$-like (FC): 516 events
  - $\mu$-like (FC + PC): 558 events (predicted: ~800)

Total analyzed events: ~5,400.

---

## The Smoking Gun: Zenith Angle Distribution

### The Key Observable

The crucial innovation of the Super-Kamiokande analysis was not simply measuring
the flavor ratio, but examining the **zenith angle distribution** of muon
neutrino events.

Atmospheric neutrinos are produced uniformly around the Earth. A detector
therefore sees neutrinos from all directions:

- **Downward-going** ($\cos\theta_z \approx +1$): produced in the atmosphere
  directly above, travel $L \sim 15$ km.
- **Horizontal** ($\cos\theta_z \approx 0$): produced near the horizon, travel
  $L \sim 500$ km.
- **Upward-going** ($\cos\theta_z \approx -1$): produced on the opposite side of
  the Earth, travel $L \sim 13,000$ km (Earth's diameter).

If neutrino oscillations occur with $\Delta m^2 \sim 10^{-3}$ eV$^2$ and
$E \sim 1$ GeV, the oscillation length is $L_{\text{osc}} \sim 1,000$ km. This
means:

- Downward-going neutrinos ($L \sim 15$ km) have not yet oscillated
  significantly: $P(\nu_\mu \to \nu_\mu) \approx 1$.
- Upward-going neutrinos ($L \sim 13,000$ km) have oscillated through many
  cycles, averaging to $P(\nu_\mu \to \nu_\mu) \approx 1 - \frac{1}{2}\sin^2(2\theta_{23})$.

The prediction: **upward-going muon neutrino events should be depleted relative
to downward-going events**, while electron neutrino events should show no
up-down asymmetry.

### The Data

This is precisely what was observed. The up/down asymmetry:

$$A_{\mu} = \frac{N_{\text{up}} - N_{\text{down}}}{N_{\text{up}} + N_{\text{down}}}$$

For multi-GeV $\mu$-like events:

$$A_{\mu}^{\text{data}} = -0.296 \pm 0.048 \pm 0.01$$

while without oscillations: $A_{\mu}^{\text{pred}} \approx 0$ (slight positive
asymmetry expected from geomagnetic effects).

For $e$-like events:

$$A_e^{\text{data}} = -0.036 \pm 0.067 \pm 0.02$$

consistent with zero, as expected (electron neutrinos are not oscillating at
this baseline/energy).

The zenith angle distributions showed:

- **$e$-like events**: flat in $\cos\theta_z$, consistent with no oscillation
  for both sub-GeV and multi-GeV samples.
- **$\mu$-like sub-GeV events**: mild depletion of upward-going events.
- **$\mu$-like multi-GeV events**: dramatic depletion of upward-going events,
  with the upward rate approximately **half** the downward rate.

### Statistical Significance

The no-oscillation hypothesis was rejected at greater than **6 standard
deviations** based on a chi-squared analysis of the zenith angle distributions.
The combined fit to all data samples yielded:

$$\chi^2_{\text{no-osc}} - \chi^2_{\text{best-fit}} > 40 \quad (\text{for 2 d.o.f.})$$

corresponding to a confidence level exceeding 99.99997% (approximately
$6\sigma$).

---

## Oscillation Parameter Determination

### Two-Flavor Fit

Interpreting the data as $\nu_\mu \to \nu_\tau$ oscillations (the $\nu_\mu \to
\nu_e$ channel was excluded because $e$-like events showed no anomaly), the
oscillation probability is:

$$P(\nu_\mu \to \nu_\mu) = 1 - \sin^2(2\theta_{23}) \sin^2\!\left(\frac{1.27 \, \Delta m^2_{\text{atm}} [\text{eV}^2] \cdot L [\text{km}]}{E [\text{GeV}]}\right)$$

The best-fit parameters from the 1998 analysis were:

$$\boxed{\Delta m^2_{\text{atm}} = 2.2 \times 10^{-3} \text{ eV}^2, \qquad \sin^2(2\theta_{23}) = 1.0}$$

The allowed region at 90% CL:

- $1.5 \times 10^{-3} < \Delta m^2_{\text{atm}} < 5 \times 10^{-3}$ eV$^2$
- $\sin^2(2\theta_{23}) > 0.82$

### L/E Analysis

A subsequent analysis (published in 2004 with more data) examined the
$L/E$ dependence directly by plotting the survival probability as a function of
the reconstructed $L/E$ ratio. The data showed the characteristic **sinusoidal
dip** predicted by quantum mechanical oscillation:

$$P(\nu_\mu \to \nu_\mu) = 1 - \sin^2(2\theta) \sin^2\!\left(\frac{1.27 \, \Delta m^2 \cdot L/E}{1}\right)$$

with a first minimum at $L/E \approx 500$ km/GeV, perfectly consistent with
$\Delta m^2 \approx 2.5 \times 10^{-3}$ eV$^2$.

This sinusoidal pattern definitively excluded alternative explanations:

- **Neutrino decay**: would produce $P \propto \exp(-L/E)$, not a sinusoid.
- **Quantum decoherence**: would produce $P \to 0.5$ monotonically, not
  oscillating.

### Modern Values

With over 20 years of accumulated data and improved analysis techniques, the
current best-fit values (combining Super-K with long-baseline accelerator
experiments T2K, NOvA, and MINOS) are:

$$|\Delta m^2_{32}| = (2.507 \pm 0.026) \times 10^{-3} \text{ eV}^2$$

$$\sin^2\theta_{23} = 0.546^{+0.021}_{-0.023} \quad (\text{normal ordering})$$

The mixing is near-maximal ($\theta_{23} \approx 49°$) but the data now slightly
favor the second octant ($\theta_{23} > 45°$) over the first octant.

---

## Detector Physics and Systematic Checks

### Cherenkov Ring Identification

The key to atmospheric neutrino analysis is distinguishing muon events from
electron events. In a water Cherenkov detector:

- **Muons** produce sharp, well-defined Cherenkov rings because they are
  minimum-ionizing particles that travel in straight lines.
- **Electrons** produce diffuse, "fuzzy" rings because they initiate
  electromagnetic showers (bremsstrahlung and pair production), with many
  particles each producing overlapping Cherenkov cones.

Super-K developed a likelihood-based particle identification algorithm using the
PMT hit pattern. The misidentification rate was demonstrated to be <2% using
control samples from cosmic ray muons and test beam data.

### Systematic Uncertainties

Major sources of systematic uncertainty included:

1. **Atmospheric neutrino flux** (~15--20%): The absolute flux prediction from
   Monte Carlo simulations (Honda et al., Bartol group) had significant
   uncertainties due to hadronic interaction models. However, the up/down
   asymmetry and the double ratio $R_{\text{data}}/R_{\text{MC}}$ largely
   cancel these uncertainties.

2. **Neutrino cross sections** (~10%): Deep inelastic scattering, quasi-elastic,
   and resonance production cross sections in water at GeV energies. Partially
   constrained by the K2K near detector.

3. **Detector response** (~5%): Energy scale, vertex reconstruction, ring
   counting, particle identification.

4. **Fiducial volume** (~2%): Definition of the fiducial volume boundary.

The analysis was specifically designed so that the observable (zenith angle
asymmetry) was robust against the dominant systematic (overall flux
normalization). This is why the result was so convincing despite large
individual systematic uncertainties.

### Cross-Checks

- **Anti-neutrino analysis**: Separating neutrinos from antineutrinos using
  statistical methods (different cross-section energy dependence). Both showed
  the deficit.
- **Multi-ring events**: Events with multiple Cherenkov rings showed consistent
  oscillation signature.
- **Contained vs. partially contained**: Both FC and PC samples showed consistent
  parameters.
- **Upward-going muons** (from neutrino interactions in the rock below the
  detector): Showed depletion consistent with the same oscillation parameters.

---

## Impact and Legacy

### Proof of Neutrino Mass

The discovery of atmospheric neutrino oscillations constituted the first
definitive evidence that neutrinos have mass. This was revolutionary because:

1. The Standard Model (as formulated in the 1970s) assumed massless neutrinos.
2. Massive neutrinos require either right-handed neutrino states (Dirac mass) or
   lepton number violation (Majorana mass) -- both require new physics.
3. The mass scale ($\sqrt{\Delta m^2_{\text{atm}}} \approx 0.05$ eV) is at least
   $10^{10}$ times smaller than the next lightest fermion (the electron),
   suggesting a fundamentally different mass generation mechanism.

### Maximal Mixing

The near-maximal mixing ($\theta_{23} \approx 45°$) was unexpected. In the quark
sector, mixing angles are small (the Cabibbo angle $\theta_C \approx 13°$, and
$V_{cb}$ and $V_{ub}$ are much smaller). The near-maximality of $\theta_{23}$
hints at a symmetry -- possibly $\mu$--$\tau$ symmetry -- in the neutrino mass
matrix:

$$M_\nu = \begin{pmatrix} a & b & b \\ b & c & d \\ b & d & c \end{pmatrix}$$

This matrix has exact $\mu$--$\tau$ interchange symmetry, which predicts
$\theta_{23} = 45°$ and $\theta_{13} = 0$. The measured $\theta_{13} \neq 0$
(Daya Bay, 2012) shows that this symmetry, if present, is approximate.

### Subsequent Confirmations

- **K2K** (KEK to Kamioka, 250 km, 1999--2004): First long-baseline accelerator
  neutrino experiment to confirm atmospheric oscillations.
- **MINOS** (Fermilab to Soudan, 735 km, 2005--2012): Precise $\Delta m^2$
  measurement; separated $\nu_\mu$ and $\bar{\nu}_\mu$.
- **T2K** (Tokai to Kamioka, 295 km, 2010--): Precise $\theta_{23}$ and
  $\Delta m^2_{32}$; first indication of $\theta_{13} \neq 0$ (2011).
- **NOvA** (Fermilab to Ash River, 810 km, 2014--): Off-axis beam;
  complementary to T2K for mass hierarchy and CP violation.
- **IceCube/DeepCore** (2012--): High-statistics atmospheric neutrino
  oscillation measurements using the deep ice at the South Pole.

---

## The Neutrino '98 Announcement

The result was first presented by Takaaki Kajita at the XVIII International
Conference on Neutrino Physics and Astrophysics (Neutrino '98) in Takayama,
Japan, on June 5, 1998. The audience of ~350 physicists gave a standing
ovation -- an extremely rare occurrence at a physics conference.

John Learned (University of Hawaii, IMB collaborator) was quoted as saying:
"Nobody in their right mind would say this was not oscillations."

The paper was published in Physical Review Letters on August 24, 1998, and has
been cited over 9,000 times.

---

## Connection to Phonon-Exflation Framework

### Atmospheric Oscillations and the Eigenvalue Gap

The atmospheric mass-squared difference $\Delta m^2_{\text{atm}} = 2.5 \times
10^{-3}$ eV$^2$ directly constrains the **eigenvalue spacing** of the internal
Dirac operator $D_K(s)$ in the phonon-exflation framework. Specifically, if
$\nu_2$ and $\nu_3$ correspond to mass eigenstates with eigenvalues $\lambda_2$
and $\lambda_3$ of $D_K(s_0)$, then:

$$|\lambda_3^2 - \lambda_2^2| \propto \Delta m^2_{\text{atm}}$$

where the proportionality constant involves the Yukawa coupling and the Higgs
VEV. This is the **largest neutrino mass splitting** and therefore the most
constraining measurement on the low end of the Dirac spectrum.

### Maximal Mixing as a Geometric Symmetry

The near-maximal atmospheric mixing angle $\theta_{23} \approx 49°$ has a
natural interpretation in the phonon-exflation framework. The SU(3) internal
space possesses a discrete symmetry under exchange of the second and third
generations -- related to the $Z_3$ triality established in Session 17a
(deliverable B-4).

In the bi-invariant limit ($s = 0$), the SU(3) geometry has the full left-right
symmetry $\text{SU}(3)_L \times \text{SU}(3)_R$. The Jensen deformation breaks
this to $\text{SU}(3)_L \times \text{U}(1)^2_R$, but an approximate $\mu$--$\tau$
symmetry can survive if the $(p,q)$ and $(q,p)$ sectors remain nearly degenerate.

Session 12 showed that the deformed Dirac spectrum satisfies:

$$\lambda_{(p,q)}(s) \neq \lambda_{(q,p)}(s) \quad \text{for } s \neq 0$$

but the splitting is controlled by $s$ and can be small. If $\theta_{23}$ is
determined by the overlap of the $\mu$ and $\tau$ flavor states with the second
and third mass eigenstates, and these mass eigenstates live in conjugate
representations, then near-maximal mixing follows from the approximate $(p,q)
\leftrightarrow (q,p)$ symmetry of the mildly deformed spectrum.

### The Up-Down Asymmetry as Spectral Signature

The zenith angle distribution measured by Super-K is a direct map of the
oscillation probability $P(\nu_\mu \to \nu_\mu; L/E)$. In the phonon-exflation
framework, this probability is:

$$P(\nu_\mu \to \nu_\mu) = 1 - 4|U_{\mu 3}|^2(1 - |U_{\mu 3}|^2) \sin^2\!\left(\frac{\Delta \lambda^2(s_0) \cdot L}{4E}\right)$$

where $\Delta \lambda^2(s_0)$ is the eigenvalue-squared difference of $D_K$ at
the stabilized deformation. The $L/E$ sinusoidal pattern observed by Super-K
(in the 2004 L/E analysis) is a direct measurement of this eigenvalue spacing.

### Exclusion of Alternative Scenarios

The Super-K L/E analysis excluded neutrino decay and quantum decoherence as
explanations for the atmospheric neutrino deficit. This is significant for the
phonon-exflation framework because:

1. **Neutrino decay** would require the Dirac operator $D_K$ to have
   non-Hermitian components (or equivalently, the spectral triple to be
   non-unitary). Session 17b (deliverable B-3) confirmed that $D_K$ is Hermitian
   to machine precision, ruling out this possibility within the framework.

2. **Quantum decoherence** would require the internal geometry to have a
   stochastic component (fluctuating $s$). While quantum fluctuations of $s$
   around $s_0$ are expected, the coherence length of the oscillation pattern
   ($L_{\text{coh}} > 10^4$ km, from the sharpness of the L/E dip) constrains
   the variance of $s$ fluctuations to be extremely small:
   $\delta s / s_0 < 10^{-3}$.

### The 50 kTon Scale and Spectral Completeness

Super-K's 50,000-tonne detector volume collected ~5,400 atmospheric neutrino
events in 535 days, yielding the first definitive oscillation measurement. The
statistical power of this dataset constrained two oscillation parameters
($\Delta m^2$, $\sin^2 2\theta$) to a bounded region, but could not determine
the mass hierarchy or CP phase.

In the phonon-exflation framework, a **complete determination** of the neutrino
sector requires measuring all six oscillation parameters ($\Delta m^2_{21}$,
$\Delta m^2_{31}$, $\theta_{12}$, $\theta_{13}$, $\theta_{23}$,
$\delta_{\text{CP}}$) plus the absolute mass scale and the Dirac/Majorana
nature. Each parameter constrains a different aspect of the lowest Dirac
eigenvalues on the deformed SU(3). Current and next-generation experiments
(DUNE, Hyper-K, JUNO) are designed to complete this program.

---

## Key Equations Summary

1. **Atmospheric $\nu$ flux ratio**: $R = N(\nu_\mu)/N(\nu_e) \approx 2$ (naive)

2. **Up-down asymmetry**: $A_\mu = (N_{\text{up}} - N_{\text{down}})/(N_{\text{up}} + N_{\text{down}}) = -0.296 \pm 0.048$

3. **Survival probability**: $P(\nu_\mu \to \nu_\mu) = 1 - \sin^2(2\theta_{23}) \sin^2(1.27 \Delta m^2 L / E)$

4. **Best-fit parameters (1998)**: $\Delta m^2 = 2.2 \times 10^{-3}$ eV$^2$, $\sin^2(2\theta_{23}) = 1.0$

5. **Modern values**: $|\Delta m^2_{32}| = 2.507 \times 10^{-3}$ eV$^2$, $\sin^2\theta_{23} = 0.546$

6. **Statistical significance**: no-oscillation excluded at $>6\sigma$

---

## References

1. Y. Fukuda et al. (Super-Kamiokande Collaboration), "Evidence for Oscillation
   of Atmospheric Neutrinos," Phys. Rev. Lett. **81**, 1562 (1998).
   [arXiv:hep-ex/9807003]
2. Y. Ashie et al. (Super-Kamiokande Collaboration), "Evidence for an
   Oscillatory Signature in Atmospheric Neutrino Oscillation," Phys. Rev. Lett.
   **93**, 101801 (2004). [The L/E analysis paper]
3. Y. Ashie et al. (Super-Kamiokande Collaboration), "Measurement of atmospheric
   neutrino oscillation parameters by Super-Kamiokande I," Phys. Rev. D **71**,
   112005 (2005).
4. M. Honda et al., "Calculation of atmospheric neutrino flux using the
   interaction model calibrated with atmospheric muon data," Phys. Rev. D **75**,
   043006 (2007).
5. K.S. Hirata et al. (Kamiokande Collaboration), "Observation of a small
   atmospheric muon-neutrino/electron-neutrino ratio in Kamiokande," Phys. Lett.
   B **280**, 146 (1992).
6. T. Kajita, "Nobel Lecture: Discovery of atmospheric neutrino oscillations,"
   Rev. Mod. Phys. **88**, 030501 (2016).
7. K. Abe et al. (Super-Kamiokande Collaboration), "Atmospheric neutrino
   oscillation analysis with external constraints in Super-Kamiokande I-IV,"
   Phys. Rev. D **97**, 072001 (2018).
