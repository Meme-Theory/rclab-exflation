# First Results from KamLAND: Evidence for Reactor Antineutrino Disappearance

**Authors:** K. Eguchi et al. (KamLAND Collaboration)
**Year:** 2003
**Journal:** *Physical Review Letters*, **90**(2), 021802

---

## Abstract

The KamLAND experiment detected electron antineutrinos ($\bar{\nu}_e$) produced by nuclear reactors at an average baseline of approximately 180 km using a 1 kiloton liquid scintillator detector located in the Kamioka mine in Japan. In a 162 ton-year exposure, the collaboration observed 54 candidate $\bar{\nu}_e$ events where $86.8 \pm 5.6$ were expected in the absence of neutrino oscillation, yielding an observed-to-expected ratio of $0.611 \pm 0.085\text{(stat)} \pm 0.041\text{(syst)}$. This deficit excluded the no-disappearance hypothesis at the 99.95% confidence level and provided the first terrestrial confirmation of the large mixing angle (LMA) solution to the solar neutrino problem. Combined with solar neutrino data, KamLAND constrained the oscillation parameters to $\Delta m^2_{21} \approx 7.9 \times 10^{-5}\;\text{eV}^2$ and $\tan^2\theta_{12} \approx 0.40$, firmly establishing reactor antineutrino disappearance as the terrestrial mirror of solar neutrino oscillation under CPT invariance.

---

## Historical Context

### The Solar Neutrino Problem

The deficit of solar electron neutrinos had been observed since Ray Davis's pioneering Homestake experiment in 1968, which detected only about one-third of the predicted solar $\nu_e$ flux. For three decades, this "solar neutrino problem" admitted two possible explanations: either the solar models were wrong (the Sun produces fewer neutrinos than predicted), or something happens to the neutrinos in transit (they change flavor).

By the late 1990s, the solar neutrino experiments -- Homestake, Kamiokande, GALLEX/GNO, SAGE, and Super-Kamiokande -- had collectively established that the deficit was energy-dependent and could not be explained by reasonable modifications to solar models. The theoretical framework of neutrino oscillation, proposed by Pontecorvo (1957) and developed by Maki, Nakagawa, and Sakata (1962), provided a natural explanation: if neutrinos have mass and the flavor eigenstates differ from the mass eigenstates, then a $\nu_e$ produced in the Sun can oscillate into $\nu_\mu$ or $\nu_\tau$ before reaching Earth.

### The LMA Solution

The MSW (Mikheyev-Smirnov-Wolfenstein) effect -- resonant flavor conversion in matter -- predicted four possible regions of the oscillation parameter space that could explain the solar data: the large mixing angle (LMA), small mixing angle (SMA), low $\Delta m^2$ (LOW), and vacuum oscillation (VAC) solutions. Each predicted different behavior for reactor antineutrinos at baselines of order 100 km.

SNO's 2001-2002 results (Paper 08) demonstrated that the total neutrino flux matched the solar model prediction, confirming that $\nu_e \to \nu_{\mu,\tau}$ conversion was occurring. However, SNO alone could not uniquely determine which MSW solution was correct. The LMA solution, with $\Delta m^2_{21} \sim 10^{-5}-10^{-4}\;\text{eV}^2$ and $\sin^2 2\theta_{12} \sim 0.8$, predicted observable $\bar{\nu}_e$ disappearance at baselines of 100-200 km -- precisely the regime accessible to a long-baseline reactor experiment.

### From Kamiokande to KamLAND

The Kamioka mine in Gifu Prefecture, Japan, had housed the Kamiokande and Super-Kamiokande water Cherenkov detectors. The KamLAND (Kamioka Liquid scintillator Anti-Neutrino Detector) experiment was designed specifically to test the LMA solution by detecting $\bar{\nu}_e$ from Japan's fleet of commercial nuclear reactors. Japan's concentration of nuclear power plants -- approximately 55 reactor cores within several hundred kilometers -- provided a powerful antineutrino source with a flux-weighted average baseline of about 180 km, ideally matched to the LMA oscillation length.

KamLAND began data collection in January 2002 and announced first results in December 2002, published in January 2003.

---

## Key Arguments and Derivations

### I. Reactor Antineutrino Production

Nuclear reactors produce electron antineutrinos through the beta decay of neutron-rich fission products. Each fission of $^{235}$U, $^{238}$U, $^{239}$Pu, or $^{241}$Pu releases approximately 200 MeV of energy and produces about 6 $\bar{\nu}_e$ with energies in the range 1-8 MeV. The $\bar{\nu}_e$ spectrum from each fissile isotope has been measured and parametrized:

$$\frac{dN_{\bar{\nu}_e}}{dE_\nu} = \sum_i f_i \phi_i(E_\nu)$$

where $f_i$ is the fission fraction for isotope $i$ and $\phi_i(E_\nu)$ is the $\bar{\nu}_e$ spectrum per fission. For a reactor with thermal power $P_{th}$, the $\bar{\nu}_e$ emission rate is:

$$\dot{N}_{\bar{\nu}_e} = \frac{P_{th}}{\sum_i f_i \langle E_i \rangle} \sum_i f_i \langle n_i \rangle$$

where $\langle E_i \rangle \approx 200$ MeV is the energy release per fission and $\langle n_i \rangle \approx 6$ is the average number of $\bar{\nu}_e$ per fission. A typical 3 GW$_{th}$ reactor produces approximately $6 \times 10^{20}$ $\bar{\nu}_e$ per second.

KamLAND received flux from approximately 55 Japanese reactor cores. The 80% of the flux came from reactors at distances of 138-214 km, and the flux-weighted average baseline was:

$$\langle L \rangle = \frac{\sum_j P_j/L_j^2 \cdot L_j}{\sum_j P_j/L_j^2} \approx 180\;\text{km}$$

where the sum runs over all reactor cores $j$ with thermal power $P_j$ at distance $L_j$.

### II. Oscillation Formalism at Reactor Baselines

For two-flavor oscillation between $\bar{\nu}_e$ and $\bar{\nu}_x$ (where $x = \mu, \tau$), the survival probability is:

$$P(\bar{\nu}_e \to \bar{\nu}_e) = 1 - \sin^2 2\theta_{12}\;\sin^2\left(\frac{\Delta m^2_{21} L}{4E_\nu}\right)$$

At the average KamLAND baseline of 180 km and for $E_\nu \approx 3.5$ MeV (the peak of the detected spectrum), the oscillation argument evaluates to:

$$\frac{\Delta m^2_{21} L}{4E_\nu} = \frac{7.9 \times 10^{-5} \times 1.8 \times 10^5}{4 \times 3.5}\;\frac{\text{eV}^2 \cdot \text{m}}{\text{MeV}} \times \frac{1}{197.3\;\text{MeV}\cdot\text{fm}}$$

Converting to natural units (with the standard formula $\Delta m^2 L / 4E = 1.267\;\Delta m^2[\text{eV}^2]\;L[\text{m}]/E[\text{MeV}]$):

$$\frac{\Delta m^2_{21} L}{4E_\nu} = 1.267 \times \frac{7.9 \times 10^{-5} \times 1.8 \times 10^5}{3.5} \approx 5.2\;\text{rad}$$

This means the oscillation has undergone more than one full cycle, and the survival probability averaged over the detected energy range gives a characteristic suppression of order $1 - \frac{1}{2}\sin^2 2\theta_{12} \approx 0.58$, roughly consistent with the observed ratio of 0.611.

### III. The KamLAND Detector

**Location:** 1 km underground in the Kamioka mine (Mozumi, Gifu Prefecture, Japan), at the former site of the Kamiokande detector. The 2700 m.w.e. (meters water equivalent) of rock overburden suppresses the cosmic ray muon flux by a factor of $\sim 10^5$.

**Detection Volume:** 1 kiloton (1000 tonnes) of ultra-pure liquid scintillator -- a mixture of 80% dodecane and 20% pseudocumene (1,2,4-trimethylbenzene) with 1.36 g/L of PPO (2,5-diphenyloxazole) as fluor. The scintillator was contained in a 13-meter-diameter spherical balloon of 135 $\mu$m thick nylon/EVOH film.

**Photomultiplier Tubes:** 1879 PMTs (1325 specially developed 17-inch Hamamatsu tubes and 554 20-inch tubes masked to 17-inch effective area) mounted on a 18-meter-diameter stainless steel sphere, providing approximately 34% solid angle coverage. The PMTs detected scintillation photons with a light yield of approximately 300 photoelectrons per MeV.

**Buffer Region:** The space between the balloon and the PMT sphere was filled with non-scintillating mineral oil to shield against external radioactivity.

**Outer Detector:** A 3.2 kiloton water Cherenkov detector surrounding the stainless steel sphere served as a cosmic ray muon veto with >99.5% efficiency.

### IV. Inverse Beta Decay Detection

KamLAND detected $\bar{\nu}_e$ via the inverse beta decay (IBD) reaction:

$$\bar{\nu}_e + p \to e^+ + n$$

This reaction has a well-known cross section:

$$\sigma(E_\nu) \approx \frac{2\pi^2}{m_e^5 f_n \tau_n}\;p_e E_e \approx 9.52 \times 10^{-44}\left(\frac{E_\nu}{\text{MeV}}\right)^2\;\text{cm}^2$$

where $E_e = E_\nu - (M_n - M_p) \approx E_\nu - 1.293$ MeV is the positron energy (neglecting the small neutron recoil), $p_e$ is the positron momentum, $f_n \approx 1.7152$ is the neutron decay phase space factor, and $\tau_n \approx 880$ s is the neutron lifetime.

The energy threshold is:

$$E_\nu^{th} = M_n + m_e - M_p = 1.806\;\text{MeV}$$

The IBD signature is a time-correlated pair of events:

1. **Prompt signal:** The positron deposits its kinetic energy in the scintillator and then annihilates with an electron, producing two 0.511 MeV gamma rays. Total visible energy: $E_{visible} \approx E_\nu - 0.782$ MeV.

2. **Delayed signal:** The neutron thermalizes ($\sim$200 $\mu$s) and is captured on a proton, producing a 2.225 MeV gamma ray: $n + p \to d + \gamma\;(2.225\;\text{MeV})$. The mean capture time in the KamLAND scintillator was approximately 210 $\mu$s.

This delayed coincidence provides a powerful background rejection technique. The prompt energy gives the neutrino energy, and the delayed signal confirms the IBD interaction.

### V. Expected Signal Without Oscillation

The expected number of IBD events in the absence of oscillation was calculated from:

$$N_{expected} = N_p \cdot T \cdot \sum_j \frac{1}{4\pi L_j^2} \int \frac{P_j(t)}{\sum_i f_i^j \langle E_i \rangle} \sum_i f_i^j \frac{d\phi_i}{dE_\nu}\;\sigma(E_\nu)\;\epsilon(E_\nu)\;dE_\nu$$

where $N_p$ is the number of free protons in the fiducial volume, $T$ is the livetime, and $\epsilon(E_\nu)$ is the detection efficiency. For the first data set (162 ton-year exposure), this yielded:

$$N_{expected} = 86.8 \pm 5.6$$

The uncertainty was dominated by the reactor power measurements ($\sim$2% per reactor), fission fractions ($\sim$1%), antineutrino spectrum shape ($\sim$2.5%), fiducial volume ($\sim$4.6%), and detection efficiency ($\sim$2.1%).

### VI. Observed Results

In the prompt energy window of 2.6 MeV $< E_{prompt} <$ 8.5 MeV, KamLAND observed:

$$N_{observed} = 54\;\text{events}$$

The backgrounds were estimated at $0.95 \pm 0.99$ events, dominated by accidental coincidences ($0.86 \pm 0.01$), fast neutrons from cosmic muons, and $^9$Li/$^8$He cosmogenic isotopes.

The ratio of observed to expected events was:

$$R = \frac{N_{obs} - N_{bkg}}{N_{expected}} = \frac{54 - 0.95}{86.8} = 0.611 \pm 0.085\text{(stat)} \pm 0.041\text{(syst)}$$

This ratio is inconsistent with unity (no oscillation) at the 99.95% confidence level ($3.5\sigma$).

### VII. Oscillation Parameter Extraction

A $\chi^2$ analysis of the rate deficit and the prompt energy spectrum yielded the allowed regions in the $(\Delta m^2_{21}, \tan^2\theta_{12})$ plane. The first KamLAND data alone allowed a band:

$$5.1 \times 10^{-5}\;\text{eV}^2 < \Delta m^2_{21} < 1.2 \times 10^{-4}\;\text{eV}^2\quad(95\%\;\text{CL})$$

Combined with solar neutrino data, the allowed region sharpened to:

$$\Delta m^2_{21} = (7.9^{+0.6}_{-0.5}) \times 10^{-5}\;\text{eV}^2$$
$$\tan^2\theta_{12} = 0.40^{+0.10}_{-0.07}$$

All solutions to the solar neutrino problem other than the LMA region were excluded.

---

## Subsequent KamLAND Results

### Spectral Distortion (2004)

With increased statistics (766 ton-year), KamLAND observed not just a rate deficit but the characteristic $L/E$-dependent oscillation pattern in the prompt energy spectrum. The survival probability showed a clear spectral distortion around the flux-weighted average $L_0/E_\nu \sim 50$ km/MeV. The theoretical first oscillation minimum (where $\sin^2(\Delta m^2_{21} L / 4E) = 1$) occurs at:

$$\frac{\Delta m^2_{21} L}{4E} = \frac{\pi}{2} \implies \frac{L}{E} \approx \frac{\pi}{2 \times 1.267 \times \Delta m^2_{21}} \approx 15.7\;\text{km/MeV}$$

This spectral distortion was inconsistent with alternative explanations (neutrino decay, decoherence) and provided definitive evidence for the oscillation interpretation.

### Precision Measurement (2008)

With 2881 ton-year of data, KamLAND achieved:

$$\Delta m^2_{21} = (7.59 \pm 0.21) \times 10^{-5}\;\text{eV}^2$$
$$\tan^2\theta_{12} = 0.47^{+0.06}_{-0.05}$$

The $\Delta m^2_{21}$ measurement was dominated by KamLAND, while $\theta_{12}$ was better determined by solar experiments. Together, they provided a complete characterization of the "solar" oscillation parameters.

### Geoneutrino Detection

KamLAND also detected geoneutrinos -- $\bar{\nu}_e$ produced by the decay of $^{238}$U and $^{232}$Th in the Earth's crust and mantle. This measurement provided the first experimental constraint on the Earth's radiogenic heat production, establishing $\bar{\nu}_e$ as a probe of geophysics.

---

## Physical Interpretation

### Terrestrial Confirmation of Solar Oscillation

The critical importance of KamLAND was the terrestrial confirmation: the same oscillation parameters that explain the solar neutrino deficit also produce observable $\bar{\nu}_e$ disappearance at reactor baselines. Under CPT invariance ($P(\nu_e \to \nu_e) = P(\bar{\nu}_e \to \bar{\nu}_e)$), this provides a model-independent test of the oscillation hypothesis that is independent of solar model uncertainties.

### Three-Flavor Consistency

By 2005, three independent sets of oscillation parameters had been measured:

1. **Atmospheric** (Super-Kamiokande): $\Delta m^2_{32} \approx 2.5 \times 10^{-3}\;\text{eV}^2$, $\theta_{23} \approx 45^\circ$
2. **Solar + reactor** (SNO + KamLAND): $\Delta m^2_{21} \approx 7.9 \times 10^{-5}\;\text{eV}^2$, $\theta_{12} \approx 34^\circ$
3. **Reactor** (CHOOZ): $\theta_{13} < 10^\circ$ (upper limit only)

All three were consistent with the standard three-flavor PMNS framework. The mass-squared differences satisfied $\Delta m^2_{21} \ll \Delta m^2_{32}$, and the mixing matrix was approximately:

$$U_{PMNS} \approx \begin{pmatrix} 0.82 & 0.55 & <0.16 \\ -0.39 & 0.58 & 0.71 \\ 0.42 & -0.58 & 0.70 \end{pmatrix}$$

The near-maximality of $\theta_{23}$ and the largeness of $\theta_{12}$ were surprising -- the neutrino mixing pattern is very different from the quark mixing pattern (CKM), where all mixing angles are small.

### The Mass Hierarchy Question

KamLAND's measurement of $\Delta m^2_{21} > 0$ (from the matter effect in the Sun, combined with KamLAND's vacuum oscillation measurement) established the "solar" mass ordering: $m_2 > m_1$. However, the sign of $\Delta m^2_{32}$ -- whether $m_3$ is the heaviest (normal hierarchy: $m_1 < m_2 < m_3$) or lightest (inverted hierarchy: $m_3 < m_1 < m_2$) neutrino mass eigenstate -- remained undetermined.

---

## Impact and Legacy

### Closing the Solar Neutrino Problem

KamLAND completed a 35-year saga. Davis observed the solar neutrino deficit in 1968. Super-Kamiokande confirmed atmospheric oscillation in 1998. SNO proved solar neutrino flavor conversion in 2001-2002. KamLAND, by reproducing the same effect with a controlled terrestrial source, closed the loop: neutrino oscillation is real, the parameters are known, and the Standard Model must be extended to include neutrino masses.

### Foundation for Precision Neutrino Physics

KamLAND's determination of $\Delta m^2_{21}$ set the baseline for the next generation of oscillation measurements. Knowing $\Delta m^2_{21}$ precisely was essential for designing and interpreting experiments to measure $\theta_{13}$ (Daya Bay, Paper 10), the mass hierarchy (JUNO), and the CP-violating phase $\delta_{CP}$ (DUNE, T2HK).

### The Reactor Neutrino Method

KamLAND demonstrated that commercial nuclear reactors are powerful neutrino sources for fundamental physics. The technique of using multiple reactors at known baselines, with the $\bar{\nu}_e$ flux predicted from thermal power monitoring and fission fraction measurements, was refined and extended by the next generation of reactor experiments (Double Chooz, Daya Bay, RENO) to measure $\theta_{13}$.

---

## Connection to Phonon-Exflation Framework

### Oscillation Parameters from Internal Geometry

In the phonon-exflation framework, neutrino masses and mixing arise from the eigenvalue spectrum of the internal Dirac operator $D_K(s)$ on the compactification manifold $K = \text{SU}(3)$ with Jensen deformation parameter $s$. The PMNS mixing matrix is not a set of free parameters but is determined by the geometry of $K$ -- specifically, by the overlap integrals between the eigenmodes of $D_K(s)$ in different irreducible representations.

KamLAND's measurement of $\Delta m^2_{21} = (7.9 \pm 0.6) \times 10^{-5}\;\text{eV}^2$ directly constrains the splitting between the two lightest mass eigenvalues of $D_K(s)$:

$$\Delta m^2_{21} = m_2^2 - m_1^2 = \lambda_2^2 - \lambda_1^2$$

where $\lambda_1, \lambda_2$ are the two smallest positive eigenvalues of $D_K(s_0)$ at the stabilized deformation $s_0$. Since $m_i \ll \Delta m^2_{32}^{1/2} \sim 0.05$ eV, the neutrino sector probes the very bottom of the Dirac spectrum -- the lightest modes, which are the most sensitive to the geometry of $K$.

### Mixing Angle as Geometric Overlap

The mixing angle $\theta_{12}$ measured by KamLAND and solar experiments has a geometric interpretation in the framework. The flavor eigenstates $|\nu_e\rangle, |\nu_\mu\rangle, |\nu_\tau\rangle$ correspond to specific representations of the unbroken gauge group, while the mass eigenstates $|\nu_1\rangle, |\nu_2\rangle, |\nu_3\rangle$ are eigenmodes of $D_K(s)$. The mixing angle is:

$$\cos\theta_{12} = \langle \nu_e | \nu_1 \rangle_K = \int_K \psi_e^\dagger(x)\;\psi_1(x)\;\sqrt{g_s}\;d^8x$$

where $\psi_e$ is the internal wavefunction of $\nu_e$ and $\psi_1$ is the first eigenmode of $D_K(s)$. The large value of $\theta_{12} \approx 34^\circ$ implies substantial overlap between the electron neutrino flavor state and both $\nu_1$ and $\nu_2$ mass eigenstates -- a non-trivial geometric prediction.

### CPT as Geometric Identity

KamLAND's confirmation that reactor $\bar{\nu}_e$ oscillate with the same parameters as solar $\nu_e$ tests CPT invariance: $P(\nu_e \to \nu_e) = P(\bar{\nu}_e \to \bar{\nu}_e)$. In the phonon-exflation framework, CPT is not an independent symmetry but is hardwired into the spectral triple structure. The result D-1 from Session 17a established that $[J, D_K(s)] = 0$ identically, where $J$ is the real structure implementing charge conjugation. This means CPT invariance of the neutrino oscillation parameters is a theorem of the internal geometry, not an assumption.

### Reactor Neutrinos as Spectral Probes

From the framework's perspective, KamLAND's measurement of the $L/E$ oscillation pattern is a direct probe of the eigenvalue spacing of $D_K(s)$. The oscillation length:

$$L_{osc} = \frac{4\pi E}{\Delta m^2_{21}} = \frac{4\pi E}{\lambda_2^2 - \lambda_1^2}$$

is determined entirely by the internal geometry. The fact that KamLAND observes a clean sinusoidal pattern (no anomalous frequency components) constrains the framework to have well-separated, non-degenerate neutrino mass eigenvalues -- consistent with the Dirac spectrum computations showing distinct eigenvalues for different $(p,q)$ sectors at $s \neq 0$.
