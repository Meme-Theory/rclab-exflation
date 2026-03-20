# Observation of High-Energy Neutrino Reactions and the Existence of Two Kinds of Neutrinos (1962)

## Bibliographic Information

- **Authors**: G. Danby, J-M. Gaillard, K. Goulianos, L.M. Lederman, N. Mistry,
  M. Schwartz, J. Steinberger
- **Title**: "Observation of High-Energy Neutrino Reactions and the Existence of Two
  Kinds of Neutrinos"
- **Journal**: *Physical Review Letters* 9, 36-44 (1962)
- **Institution**: Columbia University and Brookhaven National Laboratory
- **Facility**: Brookhaven Alternating Gradient Synchrotron (AGS)
- **Nobel Prize**: Leon Lederman, Melvin Schwartz, Jack Steinberger (1988)
- **Citation**: "for the neutrino beam method and the demonstration of the doublet
  structure of the leptons through the discovery of the muon neutrino"

---

## 1. Theoretical Motivation

### 1.1 The Two-Neutrino Question

By the late 1950s, the existence of both electron ($e$) and muon ($\mu$) leptons
was well established, and both underwent weak interactions. A fundamental question
emerged: does the neutrino associated with muon processes ($\pi \to \mu + \nu$)
differ from the neutrino in beta decay ($n \to p + e^- + \bar{\nu}$)?

Two hypotheses were in play:

**One-neutrino hypothesis**: $\nu_e = \nu_\mu = \nu$. A single neutrino species
couples to both electrons and muons. In this case, neutrinos produced in pion decay
should produce both electrons AND muons when they interact:

$$\nu + n \to p + e^- \quad \text{(sometimes)}$$
$$\nu + n \to p + \mu^- \quad \text{(sometimes)}$$

**Two-neutrino hypothesis**: $\nu_e \neq \nu_\mu$. Separate neutrino species couple
exclusively to their respective charged leptons. Neutrinos from pion decay ($\nu_\mu$)
should produce ONLY muons:

$$\nu_\mu + n \to p + \mu^- \quad \text{(yes)}$$
$$\nu_\mu + n \to p + e^- \quad \text{(no)}$$

### 1.2 Why It Mattered

The question was not merely taxonomic. If only one neutrino existed, then the process
$\mu \to e + \gamma$ should occur at a calculable rate through one-loop diagrams with
$W$-boson exchange:

$$\text{BR}(\mu \to e\gamma) \sim \frac{\alpha}{4\pi} \sim 10^{-4}$$

This rate was already experimentally excluded by several orders of magnitude. The
non-observation of $\mu \to e\gamma$ strongly suggested either:
1. Two distinct neutrino species (lepton flavor conservation), or
2. Some other unknown suppression mechanism

### 1.3 Pontecorvo and Schwartz

Bruno Pontecorvo (1959) and Melvin Schwartz (1960) independently proposed using
high-energy neutrino beams from accelerators to resolve the question. Schwartz's
key insight was that the newly commissioned Brookhaven AGS, producing 15 GeV protons,
could generate neutrinos energetic enough to produce muons (requiring $E_\nu > m_\mu
\approx 106$ MeV), while providing a controlled, directional beam.

---

## 2. The Neutrino Beam

### 2.1 Production Mechanism

The beam was created through the following chain:

**Step 1**: 15 GeV protons from the AGS struck a beryllium target, producing pions:

$$p + \text{Be} \to \pi^+ + X$$
$$p + \text{Be} \to \pi^- + X$$

**Step 2**: Pions decayed in a 21-meter decay region:

$$\pi^+ \to \mu^+ + \nu_\mu \quad (\tau_\pi = 26 \text{ ns}, \text{BR} = 99.99\%)$$

**Step 3**: A massive steel shield absorbed everything except neutrinos.

### 2.2 The Steel Wall

The critical element was 13.5 meters (44 feet) of steel -- composed of armor plate
from a decommissioned battleship (the USS *Missouri*, according to some accounts,
though this is debated) and other scrap steel. This constituted approximately:

$$13.5 \text{ m} \times 7.87 \text{ g/cm}^3 = 1062 \text{ g/cm}^2 \approx 60 \text{ interaction lengths}$$

This attenuated the hadron (pion, proton) flux by a factor of $e^{-60} \sim 10^{-26}$,
and the muon flux was attenuated by ionization energy loss:

$$\text{Range of 5 GeV } \mu \text{ in steel} \approx 6 \text{ m}$$

Thus, only neutrinos (and negligible backgrounds) penetrated the shield.

### 2.3 Beam Characteristics

| Property | Value |
|:---------|:------|
| Proton energy | 15 GeV |
| Protons on target | $\sim 3 \times 10^{17}$ (total) |
| Pion decay length | 21 m |
| Steel shielding | 13.5 m |
| Mean neutrino energy | $\sim 1$ GeV |
| Neutrino flux at detector | $\sim 10^6$ $\nu$/cm$^2$/pulse |
| Running time | $\sim 8$ months (1961-1962) |

---

## 3. The Detector

### 3.1 Spark Chamber Design

The detector consisted of 10 modules of aluminum spark chambers, with a total mass
of approximately 10 tons. Each module contained:

- Aluminum plates (1 inch thick) serving as both neutrino target and spark chamber
  electrodes
- Gas gaps filled with neon (90%) and helium (10%) at atmospheric pressure
- High-voltage pulsing system triggered by scintillation counters

When a charged particle traversed the chamber, it ionized the gas. If triggered, a
high-voltage pulse (10-20 kV) caused sparks to form along the ionization trail, making
the particle track visible. Photographs were taken of each event.

### 3.2 Why Aluminum?

Aluminum was chosen because:
1. It served as the target nuclei for neutrino interactions
2. It provided uniform density for consistent track quality
3. Its radiation length ($X_0 = 8.9$ cm) allowed electrons to shower visibly within
   the detector while muons traversed it as minimum-ionizing particles
4. It was affordable in the required quantity

### 3.3 Particle Identification

The key discriminant between muons and electrons was their behavior in the aluminum:

**Muons**: Produced long, straight, minimum-ionizing tracks that penetrated many plates.
A 1 GeV muon would traverse the entire detector ($\sim 10$ interaction lengths of
aluminum) with only modest multiple scattering.

**Electrons**: Initiated electromagnetic showers within 1-2 radiation lengths, producing
broad, bushy cascades of $e^+e^-$ pairs and photons. A 1 GeV electron would create a
shower spreading over $\sim 20$ cm in the aluminum.

The visual distinction between a single clean track (muon) and a broad shower (electron)
was unambiguous at these energies.

---

## 4. Results

### 4.1 Event Classification

After extensive running and analysis, the data yielded:

| Event Type | Count |
|:-----------|:------|
| Single muon tracks | **29** |
| Electron showers | **6** |
| Expected electron background (from $K_{e3}$ decays, etc.) | $\sim 5$ |
| Cosmic ray background | $\sim 2$--$3$ |
| Vertex-associated events | $\sim 56$ total |

### 4.2 The Critical Comparison

The experimental test was straightforward:

**If $\nu_\mu = \nu_e$ (one-neutrino hypothesis)**:
The ratio of muon events to electron events should be approximately:

$$\frac{N_\mu}{N_e} \approx \frac{\sigma(\nu + n \to \mu^- + p)}{\sigma(\nu + n \to e^- + p)} \approx 1$$

(modified slightly by phase space and form factors)

**If $\nu_\mu \neq \nu_e$ (two-neutrino hypothesis)**:
Neutrinos from pion decay should produce essentially ONLY muons:

$$\frac{N_\mu}{N_e} \gg 1$$

with any observed electrons attributable to backgrounds.

### 4.3 The Verdict

The observation of 29 muon events versus 6 electron events (consistent with
the expected 5 from known backgrounds) was decisive:

$$\frac{N_\mu}{N_e - N_{\text{bkg}}} = \frac{29}{6 - 5} \approx 29$$

This ratio was completely inconsistent with the one-neutrino hypothesis (which predicted
$\sim 1$) and fully consistent with the two-neutrino hypothesis (which predicted
$N_e \approx N_{\text{bkg}}$).

The probability of the one-neutrino hypothesis producing the observed result was
estimated at less than $10^{-6}$.

### 4.4 Statistical Significance

The 29 single-muon events compared to an expected background of $\sim 5$ events
from all non-neutrino sources represented a signal significance exceeding $5\sigma$.
More importantly, the *absence* of electron events above background was the
discriminating observation.

---

## 5. Physics Implications

### 5.1 Lepton Flavor Conservation

The two-neutrino result established lepton flavor as a conserved quantum number (at
least approximately). Defining:

$$L_e = N(e^-) + N(\nu_e) - N(e^+) - N(\bar{\nu}_e)$$
$$L_\mu = N(\mu^-) + N(\nu_\mu) - N(\mu^+) - N(\bar{\nu}_\mu)$$

each is separately conserved in all observed processes. This explained the
non-observation of $\mu \to e\gamma$ and other lepton-flavor-violating processes.

### 5.2 The Doublet Structure

The result confirmed that the weak interaction has a doublet structure for leptons,
paralleling the quark doublets:

$$\binom{\nu_e}{e^-}_L \qquad \binom{\nu_\mu}{\mu^-}_L$$

Each doublet couples to the $W$ boson with the same strength $g_2/\sqrt{2}$, and
the neutrino flavors are defined by their charged-lepton partners.

### 5.3 Toward the Standard Model

The two-neutrino result was a critical input for the Glashow-Weinberg-Salam
electroweak theory (1961-1968). The model requires a specific number of lepton
doublets, with each doublet containing a distinct neutrino. The anomaly cancellation
condition:

$$\sum_f Q_f = 0 \quad \text{(per generation)}$$

requires matching the number of lepton doublets to quark doublets, connecting the
Brookhaven result to the quark sector.

### 5.4 Neutrino Beams as a Tool

Beyond the two-neutrino discovery, the experiment established high-energy neutrino
beams as a precision tool for studying the weak interaction. Subsequent neutrino beam
experiments at CERN, Fermilab, and other facilities used this technique to:

- Measure weak interaction cross-sections
- Discover neutral currents (Gargamelle, 1973)
- Measure the Weinberg angle $\theta_W$
- Study nucleon structure functions
- Search for neutrino oscillations (MINOS, NOvA, T2K, DUNE)

---

## 6. The Third Generation: $\nu_\tau$

### 6.1 Prediction and Discovery

After the discovery of the tau lepton ($\tau$) by Martin Perl at SLAC in 1975, a
third neutrino species ($\nu_\tau$) was expected. However, its direct detection
required producing $\tau$ leptons from $\nu_\tau$ interactions, which demanded:

$$E_{\nu_\tau} > \frac{m_\tau^2}{2 m_N} \approx 3.5 \text{ GeV}$$

and identifying the resulting $\tau$ by its short-lived decay products (track length
$\sim 1$ mm at these energies).

### 6.2 DONUT Experiment (2000)

The Direct Observation of NU Tau (DONUT) experiment at Fermilab used:
- A beam dump producing $D_s \to \tau + \nu_\tau$ decays
- Emulsion detectors with micrometer spatial resolution
- 9 $\nu_\tau$ candidate events (4 from $\tau \to e$ and 5 from $\tau \to$ hadrons)
- Expected background: $\sim 1.5$ events

This completed the three-generation lepton structure:

$$\binom{\nu_e}{e^-}_L \qquad \binom{\nu_\mu}{\mu^-}_L \qquad \binom{\nu_\tau}{\tau^-}_L$$

### 6.3 LEP Constraint: Exactly Three Light Neutrinos

The LEP experiments at CERN (1989-2000) measured the $Z$ boson invisible width:

$$\Gamma_{\text{inv}} = \Gamma_Z - \Gamma_{\text{had}} - 3\Gamma_\ell = N_\nu \cdot \Gamma_{\nu\bar{\nu}}$$

The result:

$$N_\nu = 2.9840 \pm 0.0082$$

This is consistent with exactly three light neutrino species ($m_\nu < M_Z/2$),
closing the possibility of a fourth generation with a light neutrino.

---

## 7. The Nobel Prize (1988)

The Nobel Prize citation recognized two achievements:

1. **The neutrino beam method**: Establishing accelerator-produced neutrino beams as
   a tool for particle physics
2. **The doublet structure**: Proving that two distinct neutrino species exist,
   establishing the generational structure of the lepton sector

The 26-year gap between experiment (1962) and prize (1988) is similar to the
Cowan-Reines case. By 1988, neutrino beams had become one of the most important
tools in particle physics, and the full significance of the two-neutrino result --
as a foundation of the Standard Model -- was clear.

---

## 8. Connection to Phonon-Exflation Framework

### 8.1 Lepton Flavor from Internal Geometry

In the phonon-exflation framework, the three lepton generations arise from the
$Z_3 \times Z_3$ structure of the internal space (Baptista Paper 18, Appendix E).
Session 17a (deliverable B-4) verified that $Z_3 = (p - q) \mod 3$ partitions the
28 irreducible representations of $SU(3)$ (at $p + q \leq 6$) into three families.

The fact that $\nu_\mu \neq \nu_e$ -- established by the Brookhaven experiment --
is therefore a consequence of the discrete symmetry structure of the Kaluza-Klein
internal space. Different neutrino flavors correspond to different $Z_3$ sectors of
the Dirac spectrum, with the flavor quantum number arising from the topological
structure of $SU(3)$ rather than being imposed by hand.

### 8.2 Lepton Flavor Violation from Jensen Deformation

While the $Z_3$ symmetry is exact at $s = 0$ (the bi-invariant, round metric), the
Jensen deformation at $s \neq 0$ can introduce mixing between sectors. This is the
geometric origin of neutrino oscillations in the framework: the mass eigenstates
$\nu_1, \nu_2, \nu_3$ (eigenstates of $D_K(s_0)$) do not align with the flavor
eigenstates $\nu_e, \nu_\mu, \nu_\tau$ (defined by the $Z_3$ sectors at $s = 0$).

The PMNS mixing matrix:

$$\begin{pmatrix} \nu_e \\ \nu_\mu \\ \nu_\tau \end{pmatrix} = U_{\text{PMNS}} \begin{pmatrix} \nu_1 \\ \nu_2 \\ \nu_3 \end{pmatrix}$$

is predicted, in principle, by the misalignment between $Z_3$ eigenstates and $D_K(s_0)$
eigenstates. The large mixing angles observed experimentally ($\theta_{12} \approx 34^\circ$,
$\theta_{23} \approx 45^\circ$, $\theta_{13} \approx 8.5^\circ$) would require
significant off-diagonal elements in $D_K(s_0)$ connecting different $Z_3$ sectors.

### 8.3 The Anomaly Cancellation Constraint

The matching of lepton and quark generations (required for gauge anomaly cancellation)
is automatic in the phonon-exflation framework. The Peter-Weyl decomposition of the
Dirac spectrum on $SU(3)$ produces representations that simultaneously accommodate
quarks and leptons in each $Z_3$ sector. The Brookhaven experiment's confirmation
of the doublet structure is therefore a test of the representation theory of the
internal space.

### 8.4 Neutrino Beam Experiments as Future Tests

Modern long-baseline neutrino beam experiments (T2K, NOvA, and the forthcoming DUNE)
measure the oscillation parameters $\Delta m^2_{ij}$ and $\theta_{ij}$ with increasing
precision. The phonon-exflation framework predicts all six oscillation parameters
(three masses, three angles, and the CP phase $\delta_{CP}$) from the eigenvalues and
eigenvectors of $D_K(s_0)$. Current measurements provide the experimental benchmarks:

| Parameter | Measured Value | Framework Status |
|:----------|:---------------|:-----------------|
| $\Delta m^2_{21}$ | $7.53 \times 10^{-5}$ eV$^2$ | Predicted from $\lambda_1, \lambda_2$ |
| $|\Delta m^2_{32}|$ | $2.507 \times 10^{-3}$ eV$^2$ | Predicted from $\lambda_2, \lambda_3$ |
| $\sin^2\theta_{12}$ | 0.307 | From $Z_3$ sector mixing |
| $\sin^2\theta_{23}$ | 0.546 | From $Z_3$ sector mixing |
| $\sin^2\theta_{13}$ | 0.0220 | From $Z_3$ sector mixing |
| $\delta_{CP}$ | $\sim 197°$ (hints, NuFIT 5.3) | From complex phase of $D_K$ |

---

## References

1. Danby, G. et al. (1962). "Observation of High-Energy Neutrino Reactions and the
   Existence of Two Kinds of Neutrinos." *Physical Review Letters* 9, 36-44.
2. Pontecorvo, B. (1959). "Electron and Muon Neutrinos." *Zh. Eksp. Teor. Fiz.* 37,
   1751-1757. [*Sov. Phys. JETP* 10, 1236-1240 (1960)].
3. Schwartz, M. (1960). "Feasibility of Using High-Energy Neutrinos to Study the
   Weak Interactions." *Physical Review Letters* 4, 306-307.
4. Lederman, L.M. (1989). "Observations in Particle Physics from Two Neutrinos to
   the Standard Model." Nobel Lecture, *Reviews of Modern Physics* 61, 547-560.
5. Schwartz, M. (1989). "The First High-Energy Neutrino Experiment." Nobel Lecture,
   *Reviews of Modern Physics* 61, 527-532.
6. Steinberger, J. (1989). "Experiments with High-Energy Neutrino Beams." Nobel
   Lecture, *Reviews of Modern Physics* 61, 533-545.
7. DONUT Collaboration, Kodama, K. et al. (2001). "Observation of Tau Neutrino
   Interactions." *Physics Letters B* 504, 218-224.
8. ALEPH, DELPHI, L3, OPAL, SLD Collaborations (2006). "Precision Electroweak
   Measurements on the Z Resonance." *Physics Reports* 427, 257-454.
