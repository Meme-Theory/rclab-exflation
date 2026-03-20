# Evidence for High-Energy Extraterrestrial Neutrinos at the IceCube Detector

**Authors:** M. G. Aartsen et al. (IceCube Collaboration)
**Year:** 2013
**Journal:** *Physical Review Letters*, **111**(2), 021103 (PeV events); *Science*, **342**(6161), 1242856 (28-event sample)

---

## Abstract

The IceCube Neutrino Observatory, a cubic-kilometer Cherenkov detector embedded in the Antarctic ice cap at the South Pole, reported in 2013 the first observation of high-energy neutrinos of astrophysical origin. Two initial events with deposited energies of $1.04 \pm 0.16$ PeV and $1.14 \pm 0.17$ PeV -- nicknamed "Bert" and "Ernie" -- were identified in a search for ultra-high-energy neutrinos using 615.9 days of livetime data. The probability of observing two or more such events from atmospheric backgrounds alone was $2.9 \times 10^{-3}$ ($2.8\sigma$). A subsequent analysis of two years of data using a high-energy starting event (HESE) selection found 28 neutrino candidates above 30 TeV, where the expected atmospheric background was $10.6^{+5.0}_{-3.6}$ events, establishing the astrophysical signal at $4.1\sigma$. The energy spectrum was consistent with an $E^{-2}$ power law, as expected from Fermi acceleration at cosmic sources. IceCube opened the era of high-energy neutrino astronomy, later identifying the blazar TXS 0506+056 (2018) and the Seyfert galaxy NGC 1068 (2022) as neutrino point sources.

---

## Historical Context

### The Dream of Neutrino Astronomy

The concept of using neutrinos as astronomical messengers dates to the 1960s. Frederick Reines and Clyde Cowan had detected reactor antineutrinos in 1956, and Markov (1960) proposed detecting high-energy cosmic neutrinos using large-volume natural water or ice as both the target and the detection medium. The appeal of neutrino astronomy is fundamental:

**Neutrinos are unique messengers.** Unlike photons, they are unattenuated by the cosmic microwave background (the GZK cutoff limits cosmic ray protons above $\sim 5 \times 10^{19}$ eV) and undeflected by magnetic fields (unlike charged cosmic rays). Unlike gravitational waves, they carry flavor information that traces the nuclear processes at the source. A neutrino produced at the edge of the observable universe arrives at Earth with its energy and direction intact.

**The cosmic ray puzzle.** Ultra-high-energy cosmic rays (UHECRs) have been observed with energies exceeding $10^{20}$ eV, but their sources remain unknown because magnetic deflection scrambles their directions. If UHECRs are produced at astrophysical accelerators (active galactic nuclei, gamma-ray bursts, starburst galaxies), then hadronic interactions at the source should produce neutrinos via pion decay:

$$p + \gamma \to \Delta^+ \to \begin{cases} n + \pi^+ \to n + \mu^+ + \nu_\mu \to n + e^+ + \nu_e + \bar{\nu}_\mu + \nu_\mu \\ p + \pi^0 \to p + 2\gamma \end{cases}$$

The neutrino flux from these interactions is directly related to the cosmic ray flux, and detecting astrophysical neutrinos would identify the cosmic ray sources.

### Predecessors: DUMAND, Baikal, AMANDA

**DUMAND** (Deep Underwater Muon and Neutrino Detector): Proposed in the 1970s for deployment in the deep Pacific Ocean off Hawaii. After decades of development, the project was canceled in 1995 due to technical difficulties, but it established the detector concept.

**Baikal NT-200**: Deployed in Lake Baikal (Siberia) in 1998. With an effective volume of $\sim 10^5$ m$^3$, it was too small for astrophysical neutrino detection but demonstrated the feasibility of underwater Cherenkov neutrino telescopy and detected atmospheric neutrinos.

**AMANDA** (Antarctic Muon And Neutrino Detector Array): Deployed at the South Pole between 1996 and 2000. Using 677 optical modules on 19 strings frozen into the ice at depths of 1500-2000 m, AMANDA had an effective volume of $\sim 0.01$ km$^3$. It detected atmospheric neutrinos up to $\sim$100 TeV and set upper limits on the astrophysical flux, but it was too small to detect the astrophysical signal.

### IceCube: A Cubic Kilometer of Ice

AMANDA's results demonstrated that Antarctic ice is an excellent Cherenkov medium (long optical absorption length, $\sim$100 m) and that the technology worked. The natural next step was to scale up by a factor of 100. IceCube was proposed in the late 1990s and constructed between 2005 and 2010.

---

## Key Arguments and Derivations

### I. Cherenkov Detection Principle

When a neutrino interacts in or near the detector via charged current (CC) or neutral current (NC) interactions, the resulting charged particles travel faster than the speed of light in ice ($c/n$ where $n \approx 1.32$), producing Cherenkov radiation:

$$\cos\theta_C = \frac{1}{n\beta}$$

For relativistic particles ($\beta \approx 1$), the Cherenkov angle is $\theta_C = \arccos(1/1.32) \approx 41^\circ$. The Cherenkov photons are in the UV-blue range ($\lambda \sim 300-500$ nm), where the Antarctic ice has an absorption length of 100-200 m and a scattering length of 20-50 m.

The number of Cherenkov photons emitted per unit path length per unit wavelength is:

$$\frac{d^2N}{dx\;d\lambda} = \frac{2\pi\alpha}{\lambda^2}\sin^2\theta_C \approx \frac{2\pi\alpha}{\lambda^2}\left(1 - \frac{1}{n^2}\right)$$

For a minimum-ionizing muon, this gives approximately 250 photons per cm of track in the 300-500 nm range. A 1 TeV muon traverses several kilometers of ice, producing $\sim 10^8$ Cherenkov photons -- detectable by optical sensors hundreds of meters away.

### II. The IceCube Detector

**Geometry:** 5160 Digital Optical Modules (DOMs) deployed on 86 vertical strings, arranged in a hexagonal grid with 125 m horizontal spacing. Each string carries 60 DOMs at depths of 1450-2450 m below the ice surface, with 17 m vertical spacing. The instrumented volume is approximately 1 km$^3$.

**Digital Optical Module (DOM):** Each DOM consists of a 10-inch Hamamatsu R7081-02 photomultiplier tube, a high-voltage supply, digitization electronics (two Analog Transient Waveform Digitizers at 300 MHz and 40 MHz), and an LED flasher board, all sealed in a 35 cm diameter borosilicate glass pressure sphere. The DOM digitizes the PMT waveform in situ -- a crucial innovation that avoids the signal degradation of long analog cables used in earlier detectors.

**DeepCore:** A denser infill array of 8 additional strings with closer DOM spacing, optimized for neutrino energies down to $\sim$10 GeV (below the energy threshold of the standard IceCube array).

**IceTop:** A surface array of 81 stations (each with two ice-filled tanks instrumented with DOMs) for cosmic ray air shower detection and vetoing of downgoing atmospheric backgrounds.

### III. Event Topologies

IceCube observes two distinct event topologies:

**Track events ($\nu_\mu$ CC):** A $\nu_\mu$ charged-current interaction produces a muon that traverses the detector, leaving a long ($\sim$km) straight track of Cherenkov light. Advantages: excellent angular resolution ($\sim 0.5^\circ$ above 10 TeV) because the long lever arm constrains the direction. Disadvantage: the neutrino energy is poorly determined because the muon may enter or exit the detector.

$$\nu_\mu + N \to \mu + X$$

**Cascade events (all flavors):** NC interactions of all flavors, and CC interactions of $\nu_e$ and $\nu_\tau$, produce hadronic and/or electromagnetic showers that are contained within a $\sim$10 m radius sphere. These appear as roughly spherical pulses of Cherenkov light. Advantages: good energy resolution ($\sim$15% above 100 TeV) because the entire shower is contained. Disadvantage: poor angular resolution ($\sim 10-15^\circ$) because the shower is nearly point-like compared to the DOM spacing.

$$\nu_e + N \to e + X\quad(\text{cascade})$$
$$\nu_\tau + N \to \tau + X\quad(\tau\;\text{decays to cascade or "double bang"})$$
$$\nu_\ell + N \to \nu_\ell + X\quad(\text{NC, cascade})$$

**Double bang events ($\nu_\tau$ CC at PeV):** At very high energies, the $\tau$ lepton produced in a $\nu_\tau$ CC interaction travels a macroscopic distance before decaying ($c\tau_\tau \approx 87\;\mu\text{m}$, so $L \approx 50\;\text{m} \times (E_\tau/\text{PeV})$). This produces two distinct cascades -- one at the $\nu_\tau$ interaction vertex and one at the $\tau$ decay point -- a "double bang" signature that uniquely identifies $\nu_\tau$.

### IV. Backgrounds

The dominant backgrounds for astrophysical neutrino searches are:

**Atmospheric muons:** Cosmic ray interactions in the atmosphere produce downgoing muons at a rate of $\sim 10^{11}$ per year in IceCube ($\sim$3000 Hz). These are rejected by selecting upgoing events (the Earth filters out muons) or by requiring that the event starts inside the detector (the HESE veto).

**Atmospheric neutrinos (conventional):** Decays of pions and kaons in cosmic ray air showers produce a neutrino flux that falls steeply with energy:

$$\frac{d\Phi_{\nu}^{conv}}{dE_\nu} \propto E_\nu^{-(\gamma + 1)} \approx E_\nu^{-3.7}$$

where $\gamma \approx 2.7$ is the cosmic ray spectral index and the additional power of $E_\nu$ arises because higher-energy mesons are more likely to interact before decaying.

**Atmospheric neutrinos (prompt):** Decays of charmed mesons ($D^\pm, D^0, \Lambda_c$) produce a harder spectrum ($\propto E_\nu^{-2.7}$) because the short lifetime of charmed particles means they always decay before interacting. This "prompt" flux has not been definitively detected and is a source of systematic uncertainty.

**Astrophysical neutrinos:** Expected to follow $\propto E_\nu^{-2}$ from Fermi acceleration (first-order diffusive shock acceleration gives $dN/dE \propto E^{-2}$). The different spectral indices mean that astrophysical neutrinos dominate above some crossover energy, expected to be in the 100 TeV range.

### V. The PeV Events: Bert and Ernie

In a search for extremely high energy (EHE) neutrinos above 1 PeV using 615.9 days of data from the partially completed (79-string) and completed (86-string) IceCube detector, two cascade events were found:

| Event | Deposited Energy | Arrival Direction | Morphology |
|:------|:----------------|:------------------|:-----------|
| "Bert" | $1.04 \pm 0.16$ PeV | Southern sky | Cascade |
| "Ernie" | $1.14 \pm 0.17$ PeV | Southern sky | Cascade |

The expected background from atmospheric neutrinos (conventional + prompt) at these energies was 0.082 events. The probability of observing 2 or more events from background alone was $2.9 \times 10^{-3}$ ($2.8\sigma$).

These energies correspond to neutrino energies of $\sim$1-2 PeV (the deposited energy is a lower bound on the neutrino energy). At 1 PeV, a neutrino has a center-of-mass energy of:

$$\sqrt{s} = \sqrt{2 m_p E_\nu} = \sqrt{2 \times 0.938 \times 10^6}\;\text{GeV} \approx 1370\;\text{GeV} \approx 1.4\;\text{TeV}$$

This is comparable to the center-of-mass energy of the first LHC runs -- IceCube was probing neutrino cross sections at TeV center-of-mass energies.

### VI. The 28-Event HESE Sample

A follow-up analysis using the High-Energy Starting Event (HESE) selection -- requiring the neutrino interaction vertex to be inside the detector and using the outer layer of DOMs as a veto against incoming muons -- found 28 events above 30 TeV in 662 days of data:

- **Expected atmospheric background:** $10.6^{+5.0}_{-3.6}$ events (conventional: $6.0$, prompt: up to $3.5$, atmospheric muons: $1.1$)
- **Observed:** 28 events
- **Excess over background:** $\sim$17 events, significant at $4.1\sigma$

The energy distribution of the 28 events was:

| Energy Range | Observed | Expected Background |
|:-------------|:---------|:-------------------|
| 30-100 TeV | 16 | 8.3 |
| 100 TeV - 1 PeV | 10 | 2.2 |
| > 1 PeV | 2 | 0.08 |

### VII. Energy Spectrum

The astrophysical neutrino flux was fit to a power law:

$$\frac{d\Phi}{dE_\nu} = \Phi_0 \left(\frac{E_\nu}{100\;\text{TeV}}\right)^{-\gamma}$$

The best-fit spectral index was $\gamma = 2.2 \pm 0.4$, consistent with the $E^{-2}$ prediction from Fermi acceleration. The per-flavor flux at 100 TeV was:

$$\Phi_0 \approx 1.2 \times 10^{-8}\;\text{GeV}\;\text{cm}^{-2}\;\text{s}^{-1}\;\text{sr}^{-1}$$

This is remarkably close to the Waxman-Bahcall bound -- the upper limit on the neutrino flux derived from the observed cosmic ray flux under the assumption that cosmic ray sources are optically thin to nucleon interactions. The coincidence of the measured flux with this bound suggests that a significant fraction of the cosmic ray energy budget goes into neutrino production.

### VIII. Flavor Composition

At production (assuming pion decay at the source):

$$(\nu_e : \nu_\mu : \nu_\tau)_{source} = (1 : 2 : 0)$$

After oscillation over cosmological distances (with the measured mixing parameters):

$$(\nu_e : \nu_\mu : \nu_\tau)_{Earth} \approx (1 : 1 : 1)$$

The approximate flavor democracy at Earth is a robust prediction of the standard three-flavor oscillation framework, nearly independent of the production mechanism. The IceCube data were consistent with $(1:1:1)$, though the large uncertainties on individual flavor fractions did not provide a strong test.

---

## Subsequent Discoveries

### TXS 0506+056 (2018)

On September 22, 2017, IceCube detected a $\sim$290 TeV muon neutrino (event IC-170922A) from a direction consistent with the gamma-ray blazar TXS 0506+056, which was simultaneously in a flaring state observed by Fermi-LAT and MAGIC. The spatial and temporal coincidence had a significance of $3.0\sigma$. An archival search found an excess of 13 neutrino events from the same direction in 2014-2015, independently significant at $3.5\sigma$. This was the first association of a high-energy neutrino source with a specific astrophysical object.

### NGC 1068 (2022)

IceCube reported evidence ($4.2\sigma$) for neutrino emission from NGC 1068 (Messier 77), a nearby Seyfert II galaxy at a distance of 14.4 Mpc. The neutrino flux exceeded the gamma-ray flux by a factor of $\sim$10, indicating that the gamma rays are absorbed in the dense material surrounding the active galactic nucleus while the neutrinos escape freely. This confirmed the unique capability of neutrino astronomy to probe obscured astrophysical environments.

### The Galactic Plane (2023)

IceCube reported $4.5\sigma$ evidence for neutrino emission from the Milky Way's galactic plane, consistent with the expected flux from cosmic ray interactions with interstellar gas. This established the Milky Way as a source of high-energy neutrinos and validated the pionic production mechanism.

---

## Impact and Legacy

### Birth of High-Energy Neutrino Astronomy

IceCube's 2013 discovery opened the fourth window on the universe, after electromagnetic radiation, cosmic rays, and gravitational waves. The detection of astrophysical neutrinos demonstrated that the universe is a powerful neutrino source at TeV-PeV energies and that cubic-kilometer-scale detectors can exploit this signal.

### Multi-Messenger Astronomy

The TXS 0506+056 observation in 2018 was a landmark of multi-messenger astronomy -- the simultaneous detection of neutrinos and photons from the same astrophysical source. Combined with the LIGO/Virgo detection of gravitational waves and electromagnetic counterparts from the neutron star merger GW170817 (also in 2017), this established the era in which astronomical objects are studied through multiple independent messengers.

### Next-Generation Neutrino Telescopes

IceCube's success has motivated a suite of next-generation detectors:

- **IceCube-Gen2**: Planned 8 km$^3$ extension of IceCube with $\sim$10,000 additional optical modules, increasing the astrophysical neutrino detection rate by a factor of $\sim$5.
- **KM3NeT**: Two underwater detectors in the Mediterranean Sea (ORCA for oscillation physics, ARCA for astrophysics), providing Northern Hemisphere sky coverage complementary to IceCube.
- **Baikal-GVD**: Gigaton Volume Detector in Lake Baikal, under construction.
- **P-ONE**: Pacific Ocean Neutrino Experiment, planned for deployment in the deep Pacific.

---

## Connection to Phonon-Exflation Framework

### Neutrino Cross Sections at KK Resonance Energies

IceCube PeV neutrinos probe neutrino-nucleon cross sections at center-of-mass energies of order 1 TeV:

$$\sqrt{s} = \sqrt{2 m_N E_\nu} \approx 1.4\;\text{TeV}\;\left(\frac{E_\nu}{\text{PeV}}\right)^{1/2}$$

In the phonon-exflation framework, the compactification of $\text{SU}(3)$ produces a Kaluza-Klein tower of massive states with masses set by the eigenvalues of $D_K(s)$. The lightest KK excitations have masses of order $M_{KK} \sim 1/R_K$, where $R_K$ is the compactification radius. If $R_K$ is near the TeV scale, the first KK resonances would appear as enhancements in the neutrino-nucleon cross section at center-of-mass energies $\sqrt{s} \sim M_{KK}$.

IceCube's measurement of the neutrino cross section at PeV energies (inferred from the Earth absorption of upgoing neutrinos and the deposited-to-total energy ratio) is consistent with Standard Model predictions. This places a lower bound on the KK mass scale: $M_{KK} \gtrsim$ a few TeV, or equivalently an upper bound on $R_K$.

### Flavor Ratio as Oscillation Diagnostic

The approximately $(1:1:1)$ flavor ratio of astrophysical neutrinos at Earth is a prediction of three-flavor oscillation with the measured PMNS parameters. In the phonon-exflation framework, the number of light neutrino species is determined by the NCG spectral triple structure. The framework predicts exactly three active neutrino flavors (from the $Z_3$ generation structure of Session 17a, result B-4). If sterile neutrinos existed with masses below the PeV scale, they would modify the flavor ratio at Earth. IceCube's consistency with $(1:1:1)$ supports the three-generation prediction.

More precisely, if the lightest sterile neutrino (a KK mode of the internal Dirac operator) has mass $m_s$ and mixes with active neutrinos with angle $\theta_s$, then the flavor ratio at Earth departs from $(1:1:1)$ by:

$$\delta(\nu_e : \nu_\mu : \nu_\tau) \sim \sin^2 2\theta_s \cdot f(m_s^2 L / E)$$

IceCube's data constrain $\sin^2 2\theta_s \lesssim 0.1$ for $m_s$ in the eV-keV range, consistent with the framework's prediction that the lightest KK excitation is far heavier than the active neutrinos.

### Spectral Index and Fermi Acceleration

The $E^{-2}$ power-law spectrum of astrophysical neutrinos is a prediction of first-order Fermi (diffusive shock) acceleration at astrophysical shocks. In the phonon-exflation framework, where particles are phononic excitations of the $M_4 \times K$ medium, the Fermi acceleration mechanism has a natural interpretation: it is the repeated scattering of phonon wavepackets off moving discontinuities (shocks) in the medium, with each crossing transferring energy proportional to the shock velocity squared. The resulting $E^{-2}$ spectrum is a universal feature of this process, independent of the microscopic nature of the "phonons." IceCube's observation of this spectrum is consistent with, but does not distinguish, the phonon interpretation from the standard particle interpretation.

### Neutrino Mass Constraints from Time-of-Flight

IceCube's detection of neutrinos from cosmological distances, combined with multi-messenger timing (as in the TXS 0506+056 event), provides a time-of-flight test of the neutrino mass. A massive neutrino arrives with a time delay relative to a massless particle:

$$\Delta t = \frac{L}{2c}\left(\frac{m_\nu c^2}{E_\nu}\right)^2 \approx 0.5\;\text{s}\;\left(\frac{L}{\text{Gpc}}\right)\left(\frac{m_\nu}{0.1\;\text{eV}}\right)^2\left(\frac{\text{PeV}}{E_\nu}\right)^2$$

For PeV neutrinos from cosmological distances, this delay is negligible for $m_\nu < 1$ eV. However, IceCube's time-of-flight data constrain exotic dispersion relations (Lorentz invariance violation) that could arise if the phonon-exflation medium has a preferred frame. Current limits constrain the Lorentz-violating energy scale to $E_{LIV} > 10^{17}$ GeV for linear modifications and $E_{LIV} > 10^{10}$ GeV for quadratic modifications, placing the phonon-exflation framework under pressure to explain why the medium does not introduce detectable Lorentz violation.
