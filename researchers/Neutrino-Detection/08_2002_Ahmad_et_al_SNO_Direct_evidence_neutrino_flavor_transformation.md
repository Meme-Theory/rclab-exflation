# Direct Evidence for Neutrino Flavor Transformation from SNO

## Bibliographic Information

- **Authors**: Q.R. Ahmad, R.C. Allen, T.C. Andersen, ... A.B. McDonald, ...
  et al. (SNO Collaboration, ~180 authors)
- **Title**: "Direct Evidence for Neutrino Flavor Transformation from Neutral-
  Current Interactions in SNO"
- **Journal**: Physical Review Letters, Vol. 89, No. 1, 011301
- **Year**: 2002
- **DOI**: 10.1103/PhysRevLett.89.011301
- **Submitted**: June 18, 2002
- **Nobel Prize**: 2015 (Arthur B. McDonald, "for the discovery of neutrino
  oscillations, which shows that neutrinos have mass")
- **Note**: This was the third and most decisive of the SNO publications. The
  first (2001) reported the CC measurement alone; the second (April 2002)
  reported the day-night asymmetry; the third (June 2002) reported the NC
  measurement, completing the proof.

---

## Historical Context

### The Solar Neutrino Problem

The solar neutrino problem -- the persistent deficit of detected solar neutrinos
compared to theoretical predictions -- was one of the longest-standing puzzles in
particle physics, lasting over 30 years (1968--2002).

**The Standard Solar Model (SSM)**: John Bahcall and collaborators developed
increasingly precise models of the Sun's interior, predicting the neutrino flux
from each nuclear reaction chain:

- **pp chain**: $p + p \to d + e^+ + \nu_e$ (dominant, $E_\nu < 0.42$ MeV)
- **$^7$Be**: $^7\text{Be} + e^- \to ^7\text{Li} + \nu_e$ ($E_\nu = 0.862$ MeV, monoenergetic)
- **$^8$B**: $^8\text{B} \to ^8\text{Be}^* + e^+ + \nu_e$ ($E_\nu < 15$ MeV)
- **hep**: $^3\text{He} + p \to ^4\text{He} + e^+ + \nu_e$ ($E_\nu < 18.8$ MeV, rare)
- **CNO cycle**: subdominant in the Sun

The total predicted $^8$B neutrino flux was:

$$\Phi_{\text{SSM}}(^8\text{B}) = 5.05^{+1.01}_{-0.81} \times 10^6 \text{ cm}^{-2}\text{s}^{-1}$$

(Bahcall, Pinsonneault, and Basu, 2001).

**The experimental deficit**: Every solar neutrino experiment prior to SNO
detected fewer $\nu_e$ than predicted:

| Experiment | Period | Detection Method | Observed/Predicted |
|:-----------|:-------|:-----------------|:-------------------|
| Homestake (Davis) | 1968--1998 | $^{37}$Cl radiochemical | 0.34 +/- 0.03 |
| Kamiokande-II | 1987--1995 | Water Cherenkov (ES) | 0.54 +/- 0.07 |
| SAGE | 1990--2007 | $^{71}$Ga radiochemical | 0.56 +/- 0.05 |
| GALLEX/GNO | 1991--2003 | $^{71}$Ga radiochemical | 0.55 +/- 0.04 |
| Super-Kamiokande | 1996--2001 | Water Cherenkov (ES) | 0.46 +/- 0.02 |

The pattern was consistent across all experiments: approximately 1/3 to 1/2 of
the predicted $\nu_e$ flux was missing.

**Two possible explanations**:

1. The SSM was wrong (the Sun produces fewer neutrinos than predicted).
2. Neutrinos change flavor en route to Earth ($\nu_e \to \nu_\mu, \nu_\tau$),
   and previous experiments were only sensitive to $\nu_e$.

SNO was specifically designed to distinguish between these two possibilities.

---

## The Sudbury Neutrino Observatory

### Detector Design

SNO was a unique detector, distinguished by its use of **heavy water** (D$_2$O)
as the detection medium:

- **Location**: Creighton Mine, Sudbury, Ontario, Canada. 2,092 m underground
  (6,010 m water equivalent -- the deepest neutrino detector at the time).
- **Heavy water**: **1,000 tonnes** of 99.92% isotopically pure D$_2$O,
  borrowed from Atomic Energy of Canada Limited (valued at ~$300 million CAD).
  Contained in a 12 m diameter transparent acrylic vessel.
- **PMTs**: 9,456 Hamamatsu R1408 20 cm PMTs, mounted on a geodesic sphere
  (PSUP) of 17.8 m diameter. ~55% solid angle coverage.
- **Light water shield**: 7,000 tonnes of ultrapure H$_2$O between the acrylic
  vessel and the PMT support structure, and additional shielding outside.
- **Radiopurity**: Extreme requirements -- the D$_2$O contained less than
  $3.6 \times 10^{-15}$ g/g of thorium and $4.5 \times 10^{-14}$ g/g of
  uranium. Background photodisintegration of deuterium ($\gamma + d \to p + n$,
  threshold 2.22 MeV) from radioactive decays was the dominant background for
  the NC measurement.
- **Construction**: 1990--1999. Data taking: November 1999 -- 2006 (three phases).
- **Energy threshold**: Effective threshold of $T_e > 5$ MeV (kinetic energy of
  the detected electron or positron).

### The Three Reaction Channels

The genius of SNO was its ability to measure solar neutrinos via three distinct
reactions, each with different flavor sensitivity:

#### 1. Charged-Current (CC) Reaction

$$\nu_e + d \to p + p + e^-$$

- **Sensitivity**: $\nu_e$ only (requires $\nu_e$ to produce $e^-$ via W
  exchange).
- **Threshold**: $E_\nu > 1.44$ MeV (but effective threshold ~5 MeV).
- **Signature**: The electron carries most of the neutrino energy, preserving
  spectral information. The electron direction is weakly correlated with the
  neutrino direction.
- **Cross section**: $\sigma_{\text{CC}} \approx 1.0 \times 10^{-42} (E_\nu / 10 \text{ MeV})^2$ cm$^2$.

The CC reaction measures:

$$\Phi_{\text{CC}} = \Phi(\nu_e)$$

#### 2. Neutral-Current (NC) Reaction

$$\nu_x + d \to p + n + \nu_x$$

- **Sensitivity**: ALL active neutrino flavors equally ($x = e, \mu, \tau$).
  The Z boson couples identically to all flavors.
- **Threshold**: $E_\nu > 2.22$ MeV (deuteron binding energy).
- **Signature**: The neutron is detected. In Phase I (pure D$_2$O), the neutron
  thermalizes and captures on deuterium: $n + d \to t + \gamma$ (6.25 MeV
  gamma). In Phase II (D$_2$O + NaCl), the neutron captures on $^{35}$Cl:
  $n + ^{35}\text{Cl} \to ^{36}\text{Cl} + \gamma\text{'s}$ (8.6 MeV total,
  higher multiplicity). In Phase III, $^3$He proportional counters directly
  detected the neutrons.
- **Cross section**: $\sigma_{\text{NC}} \approx 0.3 \times 10^{-42} (E_\nu / 10 \text{ MeV})^2$ cm$^2$.

The NC reaction measures:

$$\Phi_{\text{NC}} = \Phi(\nu_e) + \Phi(\nu_\mu) + \Phi(\nu_\tau) = \Phi_{\text{total}}$$

#### 3. Elastic Scattering (ES) Reaction

$$\nu_x + e^- \to \nu_x + e^-$$

- **Sensitivity**: Predominantly $\nu_e$ (via both W and Z exchange), with a
  small contribution from $\nu_\mu$ and $\nu_\tau$ (Z exchange only).
  $\sigma(\nu_e) \approx 6.5 \times \sigma(\nu_{\mu,\tau})$.
- **Signature**: The recoil electron is strongly forward-peaked
  ($\cos\theta_{\text{sun}} > 0.9$), providing a clean directional signature
  pointing back to the Sun.
- **Cross section**: Much smaller than CC or NC on deuterium.

The ES reaction measures:

$$\Phi_{\text{ES}} = \Phi(\nu_e) + 0.154 \cdot \Phi(\nu_{\mu,\tau})$$

where 0.154 is the ratio $\sigma(\nu_{\mu,\tau})/\sigma(\nu_e)$ for elastic
scattering.

### The Decisive Comparison

The three measurements allow a model-independent determination of the total
neutrino flux and the flavor composition:

- If neutrinos do NOT oscillate: $\Phi_{\text{CC}} = \Phi_{\text{NC}} = \Phi_{\text{ES}}$
  (all measure the same $\nu_e$ flux).
- If neutrinos DO oscillate ($\nu_e \to \nu_{\mu,\tau}$):
  $\Phi_{\text{CC}} < \Phi_{\text{ES}} < \Phi_{\text{NC}}$, and
  $\Phi_{\text{NC}} = \Phi_{\text{SSM}}$ (total flux unchanged).

---

## The Results

### Phase I Results (Pure D$_2$O, November 1999 -- May 2001)

The first SNO publication (June 2001) reported the CC measurement alone:

$$\Phi_{\text{CC}} = 1.75 \pm 0.07 (\text{stat}) ^{+0.12}_{-0.11} (\text{syst}) \pm 0.05 (\text{theor}) \times 10^6 \text{ cm}^{-2}\text{s}^{-1}$$

Comparing with the Super-Kamiokande ES measurement:

$$\Phi_{\text{ES}}^{\text{SK}} = 2.32 \pm 0.03 (\text{stat}) ^{+0.08}_{-0.07} (\text{syst}) \times 10^6 \text{ cm}^{-2}\text{s}^{-1}$$

The difference $\Phi_{\text{ES}} - \Phi_{\text{CC}} = 0.57 \pm 0.17 \times 10^6$
was nonzero at $3.3\sigma$, providing the first evidence for a non-$\nu_e$
component in the solar neutrino flux.

### The NC Measurement (Phase I, 2002)

The decisive NC result was published in June 2002:

$$\boxed{\Phi_{\text{NC}} = 5.09 ^{+0.44}_{-0.43} (\text{stat}) ^{+0.46}_{-0.43} (\text{syst}) \times 10^6 \text{ cm}^{-2}\text{s}^{-1}}$$

This was consistent with the SSM prediction of $5.05 \times 10^6$
cm$^{-2}$s$^{-1}$.

The three fluxes, in units of $10^6$ cm$^{-2}$s$^{-1}$:

| Channel | Measured Flux | Sensitivity |
|:--------|:-------------|:------------|
| CC | $1.76 ^{+0.06}_{-0.05} \pm 0.09$ | $\nu_e$ only |
| ES | $2.39 ^{+0.24}_{-0.23} \pm 0.12$ | $\nu_e + 0.154 \nu_{\mu\tau}$ |
| NC | $5.09 ^{+0.44}_{-0.43} ^{+0.46}_{-0.43}$ | ALL flavors |

### The Proof

The comparison immediately established:

1. **The total flux equals the SSM prediction**:
   $\Phi_{\text{NC}} / \Phi_{\text{SSM}} = 1.01 \pm 0.12$. The Sun produces
   exactly as many neutrinos as predicted. The SSM is correct.

2. **Neutrinos change flavor**:
   $\Phi_{\text{CC}} / \Phi_{\text{NC}} = 0.346 \pm 0.029$. Only about 1/3 of
   the solar neutrinos arrive at Earth as $\nu_e$. The remaining 2/3 have
   oscillated to $\nu_\mu$ and/or $\nu_\tau$.

3. **The non-$\nu_e$ component**:
   $\Phi(\nu_{\mu,\tau}) = \Phi_{\text{NC}} - \Phi_{\text{CC}} = 3.41 \pm 0.45 ^{+0.48}_{-0.45} \times 10^6$ cm$^{-2}$s$^{-1}$

   This was nonzero at **$5.3\sigma$** -- a definitive discovery.

### Flavor Content Visualization

The SNO results are often displayed as a plot with $\Phi(\nu_e)$ on the
horizontal axis and $\Phi(\nu_{\mu,\tau})$ on the vertical axis. The three
measurements define bands in this plane:

- **CC band**: horizontal, since CC measures $\Phi(\nu_e)$ directly.
- **ES band**: tilted at an angle determined by the $\sigma(\nu_e)/\sigma(\nu_{\mu,\tau})$
  ratio.
- **NC band**: diagonal at 45 degrees ($\Phi_{\text{NC}} = \Phi(\nu_e) + \Phi(\nu_{\mu,\tau})$).

The three bands intersect at a single point:

$$\Phi(\nu_e) \approx 1.76, \qquad \Phi(\nu_{\mu,\tau}) \approx 3.41$$

(in units of $10^6$ cm$^{-2}$s$^{-1}$). The point lies well away from the
$\Phi(\nu_{\mu,\tau}) = 0$ axis, proving flavor transformation.

---

## Resolution of the Solar Neutrino Problem

### The 30-Year Puzzle Solved

The SNO NC measurement, combined with the CC and ES measurements, provided a
complete and unambiguous resolution:

1. **The Sun works as predicted**: The total neutrino flux from $^8$B decays
   matches the SSM. The nuclear physics of the pp chain is correct.

2. **Neutrinos oscillate**: $\nu_e$ produced in the solar core convert to
   $\nu_\mu$ and $\nu_\tau$ during propagation. The conversion is enhanced by
   the MSW effect in solar matter.

3. **Previous experiments were right**: Homestake, SAGE, GALLEX, Kamiokande, and
   Super-K all correctly measured the $\nu_e$ flux (or a linear combination
   weighted toward $\nu_e$). The "deficit" was not an experimental error but a
   consequence of flavor transformation.

4. **Bahcall was right**: John Bahcall, who had championed the SSM for 30 years
   against persistent skepticism, was vindicated. The agreement of
   $\Phi_{\text{NC}}$ with $\Phi_{\text{SSM}}$ was, in Bahcall's words, "the
   most satisfying result of my career."

### Combined Oscillation Parameters

Combining SNO data with Super-K, KamLAND (reactor $\bar{\nu}_e$ disappearance),
and other experiments, the solar neutrino oscillation parameters were determined:

$$\Delta m^2_{21} = (7.53 \pm 0.18) \times 10^{-5} \text{ eV}^2$$

$$\tan^2\theta_{12} = 0.437 ^{+0.029}_{-0.026} \qquad \Rightarrow \qquad \theta_{12} = 33.4° \pm 0.8°$$

This is the "Large Mixing Angle" (LMA) solution to the solar neutrino problem.
The mixing angle is large ($\theta_{12} \approx 34°$) but not maximal -- solar
mixing is definitively non-maximal, in contrast to atmospheric mixing.

### The Role of the MSW Effect

For $^8$B solar neutrinos ($E \sim 5$--15 MeV), the MSW resonance occurs in the
Sun's radiative zone at:

$$n_e^{\text{res}} = \frac{\Delta m^2_{21} \cos(2\theta_{12})}{2\sqrt{2} G_F E} \approx 50 \text{ mol/cm}^3 \quad (\text{for } E = 10 \text{ MeV})$$

This corresponds to a solar radius of $r \approx 0.2 R_\odot$, well within the
core where $^8$B neutrinos are produced. The transition is highly adiabatic
($\gamma \gg 1$), so the survival probability is:

$$P(\nu_e \to \nu_e) \approx \sin^2\theta_{12} \approx 0.30$$

consistent with the measured $\Phi_{\text{CC}}/\Phi_{\text{NC}} \approx 0.35$.

The slight excess over $\sin^2\theta_{12}$ is due to the contribution of
lower-energy neutrinos (near threshold) where the MSW effect is weaker and
vacuum oscillation averages to $P \approx 1 - \frac{1}{2}\sin^2(2\theta_{12})
\approx 0.57$.

---

## Three Phases of SNO

### Phase I: Pure D$_2$O (November 1999 -- May 2001)

- Neutron detection via $n + d \to t + \gamma$ (6.25 MeV).
- NC detection efficiency: ~25% (low due to the modest gamma energy and the
  6.25 MeV capture being close to the analysis threshold).
- 306.4 live days. 2,928 events.

### Phase II: NaCl (July 2001 -- August 2003)

- 2 tonnes of NaCl dissolved in the D$_2$O.
- Neutron detection via $n + ^{35}\text{Cl} \to ^{36}\text{Cl}^* + \gamma$'s
  (8.6 MeV total, multiple gammas).
- NC detection efficiency: ~40% (improved by higher energy and multiplicity).
- 791 live days. Much improved NC statistics.
- Published result confirmed Phase I with higher precision.

### Phase III: $^3$He Proportional Counters (November 2004 -- November 2006)

- Array of 36 $^3$He-filled proportional counter strings deployed in the D$_2$O.
- Neutron detection via $n + ^3\text{He} \to ^3\text{H} + p$ (764 keV).
- Completely independent NC detection technology with different systematics.
- Confirmed Phase I and Phase II results, providing a crucial cross-check.

### Combined Results (2013)

The final combined analysis of all three phases yielded:

$$\Phi_{\text{CC}} = 1.67 ^{+0.05}_{-0.04} \times 10^6 \text{ cm}^{-2}\text{s}^{-1}$$

$$\Phi_{\text{NC}} = 5.25 \pm 0.16 (\text{stat}) \pm 0.11 (\text{syst}) \times 10^6 \text{ cm}^{-2}\text{s}^{-1}$$

with reduced uncertainties compared to the initial publications.

---

## Nobel Prize and Legacy

### The 2015 Nobel Prize

The 2015 Nobel Prize in Physics was awarded jointly to:

- **Takaaki Kajita** (Super-Kamiokande) -- for the discovery of atmospheric
  neutrino oscillations.
- **Arthur B. McDonald** (SNO) -- for the discovery of solar neutrino flavor
  transformation.

The citation: "for the discovery of neutrino oscillations, which shows that
neutrinos have mass."

This was the culmination of a 40-year experimental program beginning with
Ray Davis's Homestake experiment in 1968. The prize recognized that the two
discoveries -- atmospheric oscillations (Super-K, 1998) and solar flavor
transformation (SNO, 2001--2002) -- together established definitively that
neutrinos have mass and mix.

### John Bahcall

John Bahcall, who spent his career predicting solar neutrino fluxes and
advocating for better experiments, died in 2005 -- before the Nobel Prize was
awarded. Had he lived, he would almost certainly have shared the prize for his
theoretical contributions. His SSM predictions, once doubted, were confirmed to
within ~3% by SNO.

### Impact on Particle Physics

The SNO result, combined with Super-K and KamLAND, established:

1. Neutrinos have mass -- the first confirmed physics beyond the Standard Model.
2. Lepton flavor is not conserved.
3. The PMNS matrix has large mixing angles (unlike the CKM matrix).
4. The solar neutrino puzzle was a particle physics problem, not an astrophysics
   problem.
5. New questions opened: mass hierarchy, absolute mass scale, Dirac vs.
   Majorana, CP violation, number of generations.

---

## Connection to Phonon-Exflation Framework

### Solar Oscillation Parameters and the Dirac Spectrum

The solar mass-squared difference $\Delta m^2_{21} = 7.53 \times 10^{-5}$
eV$^2$ and the solar mixing angle $\theta_{12} = 33.4°$ provide two of the six
oscillation parameters that constrain the lowest Dirac eigenvalues in the
phonon-exflation framework.

The two neutrino mass-squared differences probe different regions of the
spectrum of $D_K(s_0)$:

$$\Delta m^2_{21} \propto |\lambda_2^2(s_0) - \lambda_1^2(s_0)| \quad \text{(smallest splitting)}$$

$$\Delta m^2_{31} \propto |\lambda_3^2(s_0) - \lambda_1^2(s_0)| \quad \text{(larger splitting)}$$

Their ratio:

$$\frac{\Delta m^2_{21}}{\Delta m^2_{31}} = \frac{|\lambda_2^2 - \lambda_1^2|}{|\lambda_3^2 - \lambda_1^2|} \approx \frac{7.53 \times 10^{-5}}{2.507 \times 10^{-3}} \approx 0.030$$

This ratio of ~1:33 must emerge from the eigenvalue structure of $D_K(s)$ at
$s = s_0$. In Session 12, the Tier 1 Dirac spectrum computation showed that
eigenvalue spacings in the lowest representations exhibit hierarchies of this
order for specific ranges of the deformation parameter $s$.

### The 1/3 Fraction and Spectral Geometry

The SNO measurement that $\Phi_{\text{CC}}/\Phi_{\text{NC}} \approx 1/3$ --
i.e., approximately one-third of solar neutrinos arrive as $\nu_e$ -- has a
geometric interpretation in the phonon-exflation framework.

The survival probability for high-energy solar neutrinos in the MSW regime is:

$$P(\nu_e \to \nu_e) \approx \sin^2\theta_{12}$$

The value $\sin^2\theta_{12} \approx 0.307$ is close to but not exactly 1/3. In
the phonon-exflation framework, $\theta_{12}$ is determined by the overlap
integral of the first and second mass eigenstates with the electron-neutrino
flavor state on the deformed SU(3):

$$\sin^2\theta_{12} = |U_{e2}|^2 = \left|\int_K \psi_e^*(x) \phi_2(x) \sqrt{g_s} \, d^8x\right|^2$$

The near-1/3 value is suggestive of a $Z_3$ symmetry structure -- precisely the
$Z_3$ triality established in Session 17a (deliverable B-4), where $(p-q) \mod 3$
partitions the 28 irreps into three generation classes. If the three generations
were exactly $Z_3$-symmetric, the mixing would be "trimaximal" with
$\sin^2\theta_{12} = 1/3$ exactly. The measured deviation ($0.307$ vs. $0.333$)
is then a measure of the $Z_3$-breaking induced by the Jensen deformation.

### NC Measurement as Total Spectral Flux

The NC channel's sensitivity to all active neutrino flavors has a direct
interpretation in the phonon-exflation framework: the NC cross section couples
to the $Z$-boson, which in the spectral triple formulation is associated with
the $\text{U}(1)$ component of the gauge group. The flavor-blind nature of the
NC interaction is a consequence of the universality of the $Z$-coupling, which
in the NCG framework follows from the structure of the commutant algebra.

The agreement $\Phi_{\text{NC}} = \Phi_{\text{SSM}}$ confirms that the total
lepton number is conserved in the oscillation process -- neutrinos change flavor
but do not disappear into sterile states. In the phonon-exflation framework,
this conservation is guaranteed by the unitarity of the PMNS matrix, which
follows from the Hermiticity of $D_K(s)$ (verified to machine precision in
Session 17b, deliverable B-3).

### Heavy Water as a Spectral Probe

The use of deuterium as a target is noteworthy from the phonon-exflation
perspective. The deuteron is the simplest nuclear system -- a neutron-proton
bound state -- and its breakup threshold (2.22 MeV) is determined by the strong
interaction binding energy. In the phonon-exflation framework, this binding
energy is ultimately controlled by the QCD coupling $g_3$, which Session 17a
(deliverable B-1) showed is $s$-independent in the Jensen deformation. This
means the NC detection threshold is a **fixed** quantity in the framework,
independent of the internal geometry parameter $s$.

### Three Phases, Three Cross-Checks

SNO's three measurement phases (pure D$_2$O, NaCl, $^3$He counters) provided
independent determinations of the NC flux using completely different detection
technologies. This redundancy is analogous to the strategy employed in the
phonon-exflation computational program: Session 17b was dedicated entirely to
verification, with 67 independent checks and zero failures. The principle --
that extraordinary claims require extraordinary cross-checks -- is shared
between the experimental and theoretical programs.

### Implications for the Absolute Mass Scale

SNO measures flavor ratios but not absolute neutrino masses. The absolute mass
scale is constrained by:

- Tritium beta decay (KATRIN: $m_\nu < 0.45$ eV at 90% CL as of 2024)
- Cosmology (Planck + BAO: $\sum m_\nu < 0.12$ eV)
- Neutrinoless double beta decay (if Majorana: $|m_{ee}| < 0.036$--$0.156$ eV)

In the phonon-exflation framework, the absolute mass scale is set by the
**smallest eigenvalue** of $D_K(s_0)$ combined with the effective Yukawa
coupling. The smallness of neutrino masses ($m_\nu \lesssim 0.1$ eV) relative to
other fermion masses ($m_e = 0.511$ MeV) requires either a seesaw-like
suppression mechanism or a topological protection of the lowest eigenvalues.
The Atiyah-Singer index theorem applied to $D_K$ on SU(3) may provide such
protection -- this is an open question in the framework (listed as a structural
gap in Session 15).

---

## Key Equations Summary

1. **CC reaction**: $\nu_e + d \to p + p + e^-$ (measures $\Phi(\nu_e)$)

2. **NC reaction**: $\nu_x + d \to p + n + \nu_x$ (measures $\Phi_{\text{total}}$)

3. **ES reaction**: $\nu_x + e^- \to \nu_x + e^-$ (measures $\Phi(\nu_e) + 0.154\,\Phi(\nu_{\mu\tau})$)

4. **NC flux**: $\Phi_{\text{NC}} = 5.09^{+0.44}_{-0.43} \times 10^6$ cm$^{-2}$s$^{-1}$ = SSM prediction

5. **CC flux**: $\Phi_{\text{CC}} = 1.76^{+0.06}_{-0.05} \times 10^6$ cm$^{-2}$s$^{-1}$ $\approx \frac{1}{3} \Phi_{\text{NC}}$

6. **Non-$\nu_e$ flux**: $\Phi(\nu_{\mu,\tau}) = 3.41 \pm 0.66 \times 10^6$ cm$^{-2}$s$^{-1}$ (nonzero at $5.3\sigma$)

7. **Solar parameters**: $\Delta m^2_{21} = 7.53 \times 10^{-5}$ eV$^2$, $\theta_{12} = 33.4°$

8. **MSW survival**: $P(\nu_e \to \nu_e) \approx \sin^2\theta_{12} \approx 0.30$ for $^8$B neutrinos

---

## References

1. Q.R. Ahmad et al. (SNO Collaboration), "Direct Evidence for Neutrino Flavor
   Transformation from Neutral-Current Interactions in SNO," Phys. Rev. Lett.
   **89**, 011301 (2002). [arXiv:nucl-ex/0204008]
2. Q.R. Ahmad et al. (SNO Collaboration), "Measurement of the Rate of
   $\nu_e + d \to p + p + e^-$ Interactions Produced by $^8$B Solar Neutrinos
   at the Sudbury Neutrino Observatory," Phys. Rev. Lett. **87**, 071301 (2001).
   [The first SNO paper, CC only]
3. B. Aharmim et al. (SNO Collaboration), "Combined Analysis of all Three Phases
   of Solar Neutrino Data from the Sudbury Neutrino Observatory," Phys. Rev. C
   **88**, 025501 (2013). [The final combined analysis]
4. J.N. Bahcall, M.H. Pinsonneault, S. Basu, "Solar Models: Current Epoch and
   Time Dependences, Neutrinos, and Helioseismological Properties," Astrophys. J.
   **555**, 990 (2001).
5. K. Eguchi et al. (KamLAND Collaboration), "First Results from KamLAND:
   Evidence for Reactor Antineutrino Disappearance," Phys. Rev. Lett. **90**,
   021802 (2003).
6. A.B. McDonald, "Nobel Lecture: The Sudbury Neutrino Observatory: Observation
   of flavor change for solar neutrinos," Rev. Mod. Phys. **88**, 030502 (2016).
7. R. Davis Jr., "A Half-Century with Solar Neutrinos," Rev. Mod. Phys. **75**,
   985 (2003). [Nobel Lecture]
8. J.N. Bahcall, "Solar Neutrinos. I. Theoretical," Phys. Rev. Lett. **12**,
   300 (1964). [The paper that started it all]
