# Detection of the Free Neutrino: The Cowan-Reines Experiment (1956)

## Bibliographic Information

- **Authors**: Clyde L. Cowan, Jr., Frederick Reines, F.B. Harrison, H.W. Kruse, A.D. McGuire
- **Title**: "Detection of the Free Neutrino: A Confirmation"
- **Journal**: *Science* 124, 103-104 (1956)
- **Full paper**: *Physical Review* 113, 273-279 (1959)
- **Institution**: Los Alamos Scientific Laboratory
- **Location**: Savannah River Plant, Aiken, South Carolina
- **Nobel Prize**: Frederick Reines, 1995 (Cowan died in 1974)

---

## 1. The Challenge: Detecting the Undetectable

### 1.1 The Cross-Section Problem

By the early 1950s, Pauli's neutrino had been part of physics for two decades, yet no
one had observed it directly. The fundamental obstacle was quantitative: Bethe and
Peierls (1934) had estimated the neutrino interaction cross-section as:

$$\sigma(\bar{\nu}_e + p \to n + e^+) \approx \frac{G_F^2 E_\nu^2}{\pi} \sim 10^{-44} \text{ cm}^2$$

for neutrinos of a few MeV. To appreciate how small this is:

- A neutrino beam would need to traverse $\sim 10^{18}$ meters (~100 light-years) of
  water to have a 50% probability of a single interaction
- The mean free path in lead is $\sim 10^{16}$ m
- At the Savannah River flux, fewer than $\sim 3$ neutrinos per hour would interact in
  a multi-ton detector

### 1.2 Why Nuclear Reactors?

Nuclear fission reactors are prolific sources of electron antineutrinos. Each fission
event produces $\sim 6$ beta decays (from neutron-rich fission products), and each beta
decay emits one $\bar{\nu}_e$. A 1 GW thermal reactor produces approximately:

$$\Phi_{\bar{\nu}_e} \approx \frac{6 \times P_{\text{th}}}{200 \text{ MeV}} \approx 2 \times 10^{20} \text{ } \bar{\nu}_e/\text{s}$$

At a distance of $\sim 11$ meters from the reactor core (as at Savannah River), the
flux at the detector was:

$$\phi \approx \frac{\Phi}{4\pi r^2} \approx 1.3 \times 10^{13} \text{ } \bar{\nu}_e / \text{cm}^2 / \text{s}$$

This enormous flux compensates partially for the tiny cross-section.

### 1.3 Reines' Bold Idea

Frederick Reines, working at Los Alamos on nuclear weapons testing, conceived the
neutrino detection experiment in 1951. His original plan was to use a nuclear bomb
test as the neutrino source -- the brief but intense burst would provide a pulsed
signal distinguishable from steady-state backgrounds. However, Clyde Cowan persuaded
him that a reactor experiment, while more challenging in terms of background rejection,
would allow repeated measurements and systematic studies.

---

## 2. The Detection Method

### 2.1 Inverse Beta Decay

The detection reaction is the inverse of neutron beta decay:

$$\bar{\nu}_e + p \to n + e^+$$

This reaction has a threshold energy:

$$E_{\text{th}} = \frac{(m_n + m_e)^2 - m_p^2}{2 m_p} = \frac{(939.565 + 0.511)^2 - 938.272^2}{2 \times 938.272} \approx 1.806 \text{ MeV}$$

The cross-section at typical reactor antineutrino energies ($E_\nu \sim 3$ MeV) is:

$$\sigma \approx 9.5 \times 10^{-44} \text{ cm}^2 \times \left(\frac{E_\nu}{\text{MeV}}\right)^2$$

which gives $\sigma \sim 10^{-43}$ cm$^2$ at $E_\nu = 3$ MeV.

### 2.2 The Two-Flash Signature

The brilliance of the Cowan-Reines experiment was the use of a delayed-coincidence
technique that provided a distinctive two-flash signature:

**Flash 1 (Prompt, $t = 0$):** The positron produced in inverse beta decay immediately
thermalizes and annihilates with an electron:

$$e^+ + e^- \to 2\gamma \quad (E_\gamma = 0.511 \text{ MeV each})$$

These two 511-keV gamma rays are detected simultaneously (within nanoseconds) in the
liquid scintillator. The total prompt energy deposited is:

$$E_{\text{prompt}} = T_{e^+} + 2 m_e c^2 \approx (E_\nu - (m_n - m_p) - m_e) + 2m_e = E_\nu - (m_n - m_p) + m_e \approx E_\nu - 0.782 \text{ MeV}$$

**Flash 2 (Delayed, $t \sim 5 \text{ } \mu$s):** The neutron produced in the reaction
thermalizes by elastic scattering on hydrogen nuclei (taking $\sim$ microseconds), then
is captured by a cadmium nucleus:

$$n + ^{108}\text{Cd} \to ^{109}\text{Cd}^* \to ^{109}\text{Cd} + \gamma\text{'s} \quad (\sum E_\gamma \approx 9 \text{ MeV})$$

The cadmium capture produces a burst of gamma rays totaling about 9 MeV, easily
distinguishable from natural radioactivity backgrounds (which rarely exceed 3 MeV).

**The coincidence requirement:**
- Two flashes separated by $3$--$10$ $\mu$s
- Flash 1: energy consistent with positron annihilation ($\sim 1$--$8$ MeV)
- Flash 2: energy consistent with neutron capture on Cd ($\sim 9$ MeV)

This double signature reduced backgrounds by orders of magnitude.

---

## 3. Detector Design

### 3.1 The Sandwich Architecture

The detector used a layered "sandwich" configuration:

```
    +---------------------------------+
    |   Liquid Scintillator (Tank I)  |  110 PMTs
    +---------------------------------+
    |   Water + CdCl2 (Target A)      |  200 liters
    +---------------------------------+
    |   Liquid Scintillator (Tank II) |  110 PMTs
    +---------------------------------+
    |   Water + CdCl2 (Target B)      |  200 liters
    +---------------------------------+
    |   Liquid Scintillator (Tank III)|  110 PMTs
    +---------------------------------+
```

- **Target**: Two tanks of water doped with cadmium chloride (CdCl$_2$, $\sim 40$ kg
  of Cd per tank). The hydrogen in the water provided the target protons. The cadmium
  provided efficient neutron capture.
- **Detectors**: Three tanks of liquid scintillator (terphenyl in triethylbenzene),
  each viewed by 110 photomultiplier tubes (PMTs), for a total of 330 PMTs.
- **Total target mass**: Approximately 400 liters of target water containing about
  $2.7 \times 10^{28}$ free protons.

### 3.2 Shielding and Location

The detector was placed approximately 11 meters from the core of one of the Savannah
River Site's heavy-water production reactors. Shielding against cosmic rays and reactor
neutrons included:

- Lead and paraffin shielding surrounding the detector
- The reactor building itself provided some overburden
- Earth and concrete between the reactor and detector

Even so, cosmic ray backgrounds were significant. The experiment relied heavily on
the delayed-coincidence technique to reject them.

### 3.3 Electronics and Triggering

The electronics required:
1. A prompt signal in at least one scintillator tank above threshold
2. A delayed signal in an adjacent scintillator tank within a $\sim 5 \mu$s window
3. Anti-coincidence with signals indicating through-going cosmic ray muons

The timing resolution was $\sim 0.2 \mu$s, adequate for measuring the neutron
thermalization and capture delay.

---

## 4. Results

### 4.1 The Measurement

The experiment ran in two major campaigns:

**Hanford (1953):** A preliminary experiment at the Hanford reactor in Washington
State yielded suggestive but not conclusive results, with a signal-to-background
ratio of only $\sim 1:1$.

**Savannah River (1955-1956):** The improved detector at the more powerful Savannah
River reactor produced definitive results:

| Quantity | Value |
|:---------|:------|
| Reactor ON rate | $36.0 \pm 1.5$ events/hour |
| Reactor OFF rate | $33.0 \pm 1.5$ events/hour |
| **Signal (ON - OFF)** | **$3.0 \pm 0.2$ events/hour** |
| Expected from theory | $\sim 2.9$ events/hour |
| Measured cross-section | $(11 \pm 2.6) \times 10^{-44}$ cm$^2$ |
| Predicted cross-section | $\sim 6 \times 10^{-44}$ cm$^2$ (energy-averaged) |

The reactor ON/OFF comparison was critical: the $\sim 3$ events/hour excess was
directly correlated with reactor operation, confirming that the signal was produced
by reactor antineutrinos.

### 4.2 Systematic Checks

The experimenters performed extensive systematic checks:

1. **Reactor power correlation**: Signal rate scaled linearly with reactor thermal power
2. **Timing distribution**: The delay between prompt and delayed signals followed the
   expected exponential with $\tau \sim 5 \mu$s for Cd capture
3. **Energy spectra**: Both prompt (positron) and delayed (neutron capture) energy
   distributions matched expectations
4. **Accidental coincidence rate**: Measured independently and subtracted
5. **Cd concentration variation**: Changing Cd loading changed the capture time as
   expected

### 4.3 Statistical Significance

The signal of $3.0 \pm 0.2$ events/hour above a background of $33$ events/hour
represented a signal-to-noise ratio of approximately 1:11. However, over extended
running periods, the statistical significance exceeded $5\sigma$.

---

## 5. The Telegram to Pauli

On June 14, 1956, Cowan and Reines sent a telegram to Wolfgang Pauli:

> "We are happy to inform you that we have definitely detected neutrinos from fission
> fragments by observing inverse beta decay of protons. Observed cross section agrees
> well with expected six times ten to minus forty-four square centimeters."

Pauli is said to have shared the telegram at a CERN gathering that evening and
reportedly replied:

> "Everything comes to him who knows how to wait."

Pauli had waited 26 years since his original hypothesis. He died in 1958, just two
years after this confirmation.

---

## 6. The Cross-Section: Theory vs. Experiment

### 6.1 Theoretical Prediction

The inverse beta decay cross-section, computed from Fermi's theory with V-A coupling
(as established by 1958), is:

$$\sigma(E_\nu) = \frac{G_F^2 \cos^2\theta_C}{\pi} (1 + 3g_A^2) \, p_e \, E_e$$

where:
- $G_F = 1.166 \times 10^{-5}$ GeV$^{-2}$ is the Fermi constant
- $\theta_C$ is the Cabibbo angle ($\cos^2\theta_C \approx 0.974$)
- $g_A \approx 1.27$ is the axial coupling constant
- $E_e = E_\nu - (m_n - m_p) \approx E_\nu - 1.293$ MeV
- $p_e = \sqrt{E_e^2 - m_e^2}$

### 6.2 Energy-Averaged Cross-Section

The reactor antineutrino spectrum peaks around 3-4 MeV and extends to about 8 MeV.
Averaging over this spectrum:

$$\langle \sigma \rangle = \int_0^{\infty} \sigma(E_\nu) \, \frac{d\Phi}{dE_\nu} \, dE_\nu \bigg/ \int_0^{\infty} \frac{d\Phi}{dE_\nu} \, dE_\nu \approx 6.3 \times 10^{-44} \text{ cm}^2$$

The Cowan-Reines measured value of $(11 \pm 2.6) \times 10^{-44}$ cm$^2$ was consistent
within the uncertainties of the reactor flux prediction and the still-uncertain value
of $g_A$ at the time.

---

## 7. Technical Innovations and Legacy

### 7.1 Techniques Pioneered

The Cowan-Reines experiment established several techniques that remain standard in
neutrino physics:

1. **Delayed coincidence**: Used in virtually all reactor neutrino experiments today
   (Daya Bay, Double Chooz, RENO, JUNO)
2. **Gadolinium/cadmium doping**: Neutron capture agents in water remain standard
   (Super-Kamiokande added Gd in 2020)
3. **Liquid scintillator detectors**: The workhorse of neutrino detection (KamLAND,
   Borexino, SNO+, JUNO)
4. **Reactor ON/OFF comparison**: The gold standard for reactor experiments
5. **Underground/shielded deployment**: Now standard practice (though Savannah River
   was above ground)

### 7.2 The Nobel Prize

Frederick Reines received the Nobel Prize in Physics in 1995 "for the detection of
the neutrino." The prize was shared with Martin Perl (for the discovery of the tau
lepton). Clyde Cowan had died in 1974 and could not share the award.

The 39-year gap between the experiment (1956) and the Nobel Prize (1995) is notable.
It reflects both the importance that grew with time as neutrino physics expanded into
a major field, and perhaps the Nobel Committee's conservatism regarding experimental
particle physics confirmations.

### 7.3 Modern Reactor Neutrino Experiments

The Cowan-Reines technique, scaled up and refined, has led to some of the most
important measurements in modern physics:

- **KamLAND (2002)**: Confirmed neutrino oscillations using reactor antineutrinos at
  $\sim 180$ km baseline. Measured $\Delta m^2_{21} = 7.9 \times 10^{-5}$ eV$^2$.
- **Daya Bay (2012)**: Measured $\theta_{13}$ with unprecedented precision
  ($\sin^2 2\theta_{13} = 0.084 \pm 0.005$), opening the door to CP violation
  searches.
- **JUNO (under construction)**: Will determine the neutrino mass hierarchy using
  reactor antineutrinos at $\sim 53$ km, with $\sim 20$ kiloton liquid scintillator.

---

## 8. The Reactor Antineutrino Anomaly

### 8.1 The Flux Discrepancy

Beginning in 2011, re-evaluations of the reactor antineutrino flux predictions by
Mueller et al. and Huber revealed a $\sim 6\%$ deficit in the observed-to-predicted
ratio across all short-baseline reactor experiments, including Cowan-Reines-era data.
This "reactor antineutrino anomaly" was initially interpreted as possible evidence
for sterile neutrinos with $\Delta m^2 \sim 1$ eV$^2$.

### 8.2 Resolution

By 2022, the STEREO, PROSPECT, and Daya Bay experiments largely resolved the anomaly
as arising from incorrect nuclear data inputs to the flux predictions (particularly
the $^{235}$U contribution), not from new physics. The story illustrates how the
systematic uncertainties Cowan and Reines grappled with in 1956 persist as active
research challenges today.

---

## 9. Connection to Phonon-Exflation Framework

### 9.1 Inverse Beta Decay as a Spectral Probe

The Cowan-Reines detection method -- inverse beta decay -- is sensitive specifically
to electron antineutrinos with $E_\nu > 1.8$ MeV. In the phonon-exflation framework,
the antineutrino is the $J$-conjugate of the neutrino in the internal Hilbert space
$\mathcal{H}_F = \mathbb{C}^{32}$. The $J$-compatibility of the Dirac operator
(verified in Session 17a, deliverable D-1: $[J, D_K(s)] = 0$ identically) guarantees
that the neutrino and antineutrino have identical mass eigenvalues -- a prediction
consistent with CPT symmetry.

The 79,968 eigenvalue pairs verified in D-3 (max error $3.29 \times 10^{-13}$) include
the neutrino sector, confirming that the geometric CPT is exact to machine precision.

### 9.2 The Cross-Section and Gauge Coupling

The inverse beta decay cross-section depends on the Fermi constant $G_F$, which in
the Standard Model (and in the phonon-exflation framework) derives from the $SU(2)_L$
gauge coupling and the $W$-boson mass:

$$G_F = \frac{g_2^2}{4\sqrt{2} M_W^2}$$

In Session 17a (B-1), the framework derived $g_1/g_2 = e^{-2s}$, which at
$s_0 = 0.2994$ gives $\sin^2\theta_W = 0.231$ (matching experiment). The gauge
couplings, and hence the weak interaction cross-sections, are geometric outputs of
the Jensen deformation -- not free parameters.

### 9.3 Reactor Neutrinos and the Mass Hierarchy

Modern descendants of the Cowan-Reines experiment (JUNO) aim to determine the neutrino
mass hierarchy by measuring the $L/E$-dependent oscillation pattern with sub-percent
energy resolution. The phonon-exflation framework predicts the mass hierarchy from
the ordering of the lightest Dirac eigenvalues $\lambda_i(s_0)$ on the Jensen-deformed
$SU(3)$. The hierarchy determination at JUNO will therefore provide a direct test of
the framework's geometric predictions.

### 9.4 Historical Significance for the Framework

The Cowan-Reines experiment established the neutrino as a real, detectable particle --
not merely a bookkeeping device. For the phonon-exflation framework, which derives all
particle content from the Dirac spectrum on the internal space, this is foundational:
the neutrino's reality as a propagating degree of freedom confirms that the lightest
modes of $D_K$ correspond to physical, observable particles.

---

## References

1. Cowan, C.L., Reines, F., Harrison, F.B., Kruse, H.W., and McGuire, A.D. (1956).
   "Detection of the Free Neutrino: A Confirmation." *Science* 124, 103-104.
2. Reines, F. and Cowan, C.L. (1959). "Free Antineutrino Absorption Cross Section.
   I. Measurement of the Free Antineutrino Absorption Cross Section by Protons."
   *Physical Review* 113, 273-279.
3. Bethe, H. and Peierls, R. (1934). "The 'neutrino'." *Nature* 133, 532.
4. Mueller, T.A. et al. (2011). "Improved Predictions of Reactor Antineutrino
   Spectra." *Physical Review C* 83, 054615.
5. Huber, P. (2011). "Determination of antineutrino spectra from nuclear reactors."
   *Physical Review C* 84, 024617.
6. An, F.P. et al. (Daya Bay Collaboration) (2012). "Observation of
   Electron-Antineutrino Disappearance at Daya Bay." *Physical Review Letters*
   108, 171803.
7. Reines, F. (1996). "The neutrino: from poltergeist to particle." Nobel Lecture,
   *Reviews of Modern Physics* 68, 317-327.
