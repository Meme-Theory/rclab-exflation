# Search for Neutrinos from the Sun: The Homestake Experiment (1968--1998)

## Bibliographic Information

- **Authors**: Raymond Davis, Jr., Don S. Harmer, Kenneth C. Hoffman
- **Title**: "Search for Neutrinos from the Sun"
- **Journal**: *Physical Review Letters* 20, 1205-1209 (1968)
- **Institution**: Brookhaven National Laboratory
- **Location**: Homestake Gold Mine, Lead, South Dakota (4,850 feet underground)
- **Duration**: 1968--1994 (data taking); analysis continued through 1998
- **Nobel Prize**: Raymond Davis, Jr. (2002, shared with Masatoshi Koshiba and
  Riccardo Giacconi)
- **Citation**: "for pioneering contributions to astrophysics, in particular for the
  detection of cosmic neutrinos"

---

## 1. Scientific Motivation

### 1.1 Solar Energy and the pp Chain

The Sun generates energy through nuclear fusion in its core, primarily via the
proton-proton (pp) chain:

$$4p \to {}^4\text{He} + 2e^+ + 2\nu_e + 26.73 \text{ MeV}$$

This overall reaction proceeds through several sub-chains, each producing neutrinos
of characteristic energies:

| Branch | Reaction | $E_\nu$ (max) | Fraction |
|:-------|:---------|:--------------|:---------|
| pp | $p + p \to {}^2\text{H} + e^+ + \nu_e$ | 0.420 MeV | 91% |
| pep | $p + e^- + p \to {}^2\text{H} + \nu_e$ | 1.442 MeV (mono) | 0.4% |
| $^7$Be | ${}^7\text{Be} + e^- \to {}^7\text{Li} + \nu_e$ | 0.862 MeV (mono) | 7% |
| $^8$B | ${}^8\text{B} \to {}^8\text{Be}^* + e^+ + \nu_e$ | 14.06 MeV | 0.02% |
| hep | ${}^3\text{He} + p \to {}^4\text{He} + e^+ + \nu_e$ | 18.77 MeV | $10^{-5}$% |

Although the $^8$B neutrinos constitute only $\sim 0.02\%$ of the total solar neutrino
flux, their high energy makes them the easiest to detect -- and they were the primary
target of the Homestake experiment.

### 1.2 Pontecorvo's Proposal (1946)

Bruno Pontecorvo proposed in 1946 that the reaction:

$$\nu_e + {}^{37}\text{Cl} \to {}^{37}\text{Ar} + e^-$$

could serve as a neutrino detector. The key advantages were:

1. **Low threshold**: $E_{\text{th}} = 0.814$ MeV (accessible to $^7$Be and $^8$B
   neutrinos)
2. **Noble gas product**: $^{37}$Ar is a noble gas, chemically inert, and can be
   extracted from a large volume of liquid by purging with helium
3. **Radioactive product**: $^{37}$Ar decays by electron capture with $\tau_{1/2}
   = 35.04$ days, producing Auger electrons detectable in small proportional counters
4. **Cheap target material**: Perchloroethylene (C$_2$Cl$_4$, dry cleaning fluid)
   contains $\sim 25\%$ chlorine by mass and costs less than \$1/gallon

### 1.3 Bahcall's Solar Model Predictions

John Bahcall, Davis's theoretical collaborator, constructed detailed Standard Solar
Models (SSMs) predicting the neutrino flux from each branch. The critical prediction
for the Homestake experiment was the capture rate in Solar Neutrino Units (SNU):

$$1 \text{ SNU} = 10^{-36} \text{ captures per target atom per second}$$

Bahcall's SSM predictions evolved over the decades:

| Year | Predicted Rate (SNU) | Dominant Contribution |
|:-----|:---------------------|:---------------------|
| 1964 | $7.5 \pm 3$ | $^8$B (77%), $^7$Be (14%) |
| 1968 | $7.5 \pm 1.5$ | $^8$B (78%), $^7$Be (13%) |
| 1988 | $7.9 \pm 2.6$ (3$\sigma$) | $^8$B (77%), $^7$Be (14%) |
| 1998 | $7.6^{+1.3}_{-1.1}$ | $^8$B (76%), $^7$Be (15%) |
| 2005 (BS05) | $8.1 \pm 1.2$ | Updated nuclear cross-sections |

The sensitivity to $^8$B neutrinos dominates because the chlorine cross-section rises
steeply with energy ($\sigma \propto E_\nu^2$ to first approximation), heavily weighting
the high-energy tail.

---

## 2. Experimental Design

### 2.1 The Tank

The heart of the experiment was a tank containing 100,000 gallons (615 tons) of
perchloroethylene (C$_2$Cl$_4$), located 4,850 feet (1,478 meters) underground in the
Homestake Gold Mine. Key parameters:

| Parameter | Value |
|:----------|:------|
| Target volume | 100,000 US gallons (378,541 liters) |
| Target mass | 615 metric tons |
| $^{37}$Cl atoms | $2.16 \times 10^{30}$ |
| Tank dimensions | 6.1 m diameter, 14.6 m long (horizontal cylinder) |
| Depth | 4,850 feet (4,200 m.w.e.) |
| Cosmic ray muon flux | $\sim 4.4$ muons/m$^2$/hour |

### 2.2 Why Underground?

At the surface, cosmic ray interactions would produce $^{37}$Ar at a rate far exceeding
the expected solar neutrino signal. The 4,850-foot rock overburden provided:

$$\text{Shielding} \approx 4,200 \text{ meters water equivalent (m.w.e.)}$$

This reduced the cosmic ray muon flux by a factor of $\sim 10^6$ compared to the
surface. The residual muon-induced $^{37}$Ar production was estimated at $\sim 0.1$
atom/day, comparable to but not overwhelming the expected solar signal of $\sim 0.5$
atoms/day.

### 2.3 Rock Backgrounds

In addition to cosmic rays, several rock-related backgrounds produced $^{37}$Ar:

- **Fast neutrons** from ($\alpha$, n) reactions in the surrounding rock, with
  $\alpha$ particles from U/Th decay chains
- **Radon** dissolved in the perchloroethylene
- **Proton recoils** from fast neutrons producing $^{37}$Ar via $^{37}$Cl(n,p)$^{37}$S
  followed by $^{37}$S beta decay

These backgrounds were estimated at $\lesssim 0.1$ atoms/day combined, and were
measured using calibration runs with the tank "blind" (covered to block all external
radiation except neutrinos, which cannot be blocked).

---

## 3. The Radiochemical Method

### 3.1 Exposure

Each experimental "run" consisted of:

1. **Exposure period**: $\sim 60$--$90$ days (approximately 2--3 $^{37}$Ar half-lives)
2. During this time, solar neutrinos convert $^{37}$Cl to $^{37}$Ar at a rate
   proportional to the neutrino flux
3. The number of $^{37}$Ar atoms at time $t$ is:

$$N_{\text{Ar}}(t) = \frac{R}{\lambda_{\text{Ar}}} \left(1 - e^{-\lambda_{\text{Ar}} t}\right)$$

where $R$ is the production rate (atoms/day) and $\lambda_{\text{Ar}} = \ln 2 / 35.04$
days.

4. At equilibrium ($t \gg \tau_{1/2}$): $N_{\text{Ar}} \to R/\lambda_{\text{Ar}}
   \approx 50 R$ atoms for $R$ in atoms/day

For the predicted rate of $\sim 7.6$ SNU, the expected production was:

$$R = 7.6 \times 10^{-36} \times 2.16 \times 10^{30} / 86400 \approx 0.19 \text{ atoms/day}$$

After a 60-day exposure: $N_{\text{Ar}} \approx 0.19 \times 50 \times (1 - e^{-60/50.5})
\approx 6$ atoms.

### 3.2 Extraction

The extraction of $\sim 6$ atoms of $^{37}$Ar from $2.16 \times 10^{30}$ atoms of
$^{37}$Cl (a dilution of 1 part in $10^{29}$) is one of the most extraordinary
chemical procedures ever performed:

**Step 1: Helium purge**. Approximately 10,000 liters of helium gas was bubbled through
the perchloroethylene for $\sim 20$ hours. Because argon is a noble gas, it does not
bond to the C$_2$Cl$_4$ and is swept out by the helium stream. The extraction efficiency
was measured at $> 95\%$ using known quantities of non-radioactive $^{36}$Ar carrier gas
($\sim 0.1$ cm$^3$ STP) added before each extraction.

**Step 2: Gas processing**. The helium/argon mixture was passed through:
- A charcoal trap at liquid nitrogen temperature to capture the argon
- Chemical getters to remove trace contaminants (O$_2$, N$_2$, H$_2$O)

**Step 3: Separation**. The argon was separated from helium by gas chromatography.

**Step 4: Volume measurement**. The recovered carrier $^{36}$Ar was measured to verify
$> 95\%$ extraction efficiency. If less than 90% was recovered, the run was discarded.

### 3.3 Counting

**Step 5: Proportional counting**. The extracted argon ($\sim 0.1$--$0.5$ cm$^3$ STP)
was loaded into a small ($\sim 1$ cm$^3$) proportional counter and counted for
$\sim 200$--$400$ days.

$^{37}$Ar decays by electron capture:

$$^{37}\text{Ar} + e^- \to {}^{37}\text{Cl} + \nu_e$$

The K-shell capture produces a 2.82 keV Auger electron (90% of decays) or a 0.27 keV
L-shell Auger electron (10%). The proportional counter detected these low-energy
electrons with:

- Energy resolution: $\sim 20\%$ FWHM at 2.82 keV
- Background rate: $\sim 0.05$ counts/day in the 2.82 keV peak
- Counting efficiency: $\sim 50\%$ for K-capture events

**Step 6: Decay curve analysis**. The time distribution of counts was fitted to:

$$n(t) = A \cdot e^{-\lambda_{\text{Ar}} t} + B$$

where $A$ is the $^{37}$Ar amplitude (fit parameter = number of $^{37}$Ar atoms) and
$B$ is the constant background rate. The known 35.04-day half-life provided a powerful
constraint.

---

## 4. Results: The Solar Neutrino Problem

### 4.1 Thirty Years of Data

The Homestake experiment ran 108 extractions between 1970 and 1994. The combined result:

$$R_{\text{measured}} = 2.56 \pm 0.16 \text{ (stat)} \pm 0.16 \text{ (syst) SNU}$$

compared to the Standard Solar Model prediction:

$$R_{\text{SSM}} = 7.6^{+1.3}_{-1.1} \text{ SNU (Bahcall-Pinsonneault 2000)}$$

The ratio:

$$\frac{R_{\text{measured}}}{R_{\text{SSM}}} = 0.34 \pm 0.06$$

Only about one-third of the expected solar neutrinos were being detected.

### 4.2 The Deficit Decomposition

The SSM prediction can be decomposed by source:

| Source | Predicted (SNU) | Measured Sensitivity |
|:-------|:----------------|:--------------------|
| $^8$B | 5.76 | Yes (dominant) |
| $^7$Be | 1.15 | Yes |
| pep | 0.22 | Yes |
| CNO | 0.48 | Yes |
| pp | 0.0 | No ($E_\nu < 0.814$ MeV threshold) |
| **Total** | **7.6** | **2.56 (measured)** |

If the SSM were correct and all neutrinos remained as $\nu_e$, the prediction was
$\sim 7.6$ SNU. The measured 2.56 SNU implied either:

1. The SSM was wrong (reduced $^8$B flux), or
2. Some $\nu_e$ were converting to $\nu_\mu$ or $\nu_\tau$ (which the Cl detector
   cannot see), or
3. The experiment was wrong

### 4.3 Time Variation

Davis reported hints of anti-correlation between the measured rate and the 11-year
sunspot cycle, suggesting a possible connection to solar magnetic fields. This generated
considerable discussion but was never established at a statistically significant level.
Modern analysis shows no significant temporal variation in the Homestake data beyond
statistical fluctuations.

---

## 5. Attempted Resolutions

### 5.1 Astrophysical Solutions

For nearly 30 years, the community debated whether the deficit was due to solar physics
or new particle physics. Proposed astrophysical solutions included:

1. **Lower core temperature**: Since $\Phi(^8\text{B}) \propto T_c^{18}$, a reduction
   of core temperature by $\sim 5\%$ could reduce the $^8$B flux by a factor of 2--3.
   However, this conflicted with helioseismology data (which by the 1990s constrained
   the solar sound speed profile to $\sim 0.1\%$).

2. **Modified nuclear cross-sections**: The critical $S_{17}$ factor for
   $^7\text{Be}(p,\gamma)^8\text{B}$ was uncertain by $\sim 15\%$ in the 1960s.
   Improved measurements narrowed this but could not account for the full deficit.

3. **Non-standard solar models**: Rapidly rotating core, strong magnetic fields, WIMPs
   transporting energy -- all proposed, none consistent with the totality of data.

### 5.2 The "Smoking Gun" Against Astrophysics

By the 1990s, four experiments observed the solar neutrino problem at different energy
thresholds:

| Experiment | Threshold | Measured/Predicted |
|:-----------|:----------|:-------------------|
| Homestake (Cl) | 0.814 MeV | $0.34 \pm 0.06$ |
| Kamiokande (water) | 7.5 MeV | $0.46 \pm 0.08$ |
| SAGE (Ga) | 0.233 MeV | $0.56 \pm 0.06$ |
| GALLEX/GNO (Ga) | 0.233 MeV | $0.56 \pm 0.05$ |

The deficit was ENERGY-DEPENDENT: $\sim 56\%$ of pp neutrinos arrived (gallium),
$\sim 34\%$ of $^8$B neutrinos arrived (chlorine), and $\sim 46\%$ of the highest-energy
$^8$B neutrinos arrived (water Cherenkov). No modification of the solar model could
simultaneously explain all four results, because reducing the core temperature affects
all branches in a correlated way.

---

## 6. Resolution: Neutrino Oscillations

### 6.1 The MSW Effect

Mikheev, Smirnov, and Wolfenstein showed that neutrino flavor oscillations can be
dramatically enhanced by matter effects. The effective Hamiltonian for neutrino
propagation in matter is:

$$H = \frac{1}{2E}\begin{pmatrix} -\Delta m^2 \cos 2\theta + A & \Delta m^2 \sin 2\theta \\ \Delta m^2 \sin 2\theta & \Delta m^2 \cos 2\theta - A \end{pmatrix}$$

where:
- $\Delta m^2 = m_2^2 - m_1^2$ is the mass-squared difference
- $\theta$ is the vacuum mixing angle
- $A = 2\sqrt{2} G_F N_e E$ is the matter potential (with $N_e$ the electron density)

**Resonance condition**: When $A = \Delta m^2 \cos 2\theta$, the effective mixing becomes
maximal ($\theta_{\text{eff}} = \pi/4$), regardless of the vacuum mixing angle. For
solar conditions:

$$E_{\text{res}} = \frac{\Delta m^2 \cos 2\theta}{2\sqrt{2} G_F N_e} \sim 2\text{--}10 \text{ MeV}$$

This means high-energy $^8$B neutrinos undergo adiabatic MSW conversion in the Sun,
while low-energy pp neutrinos undergo vacuum oscillations. The different suppression
factors at different energies are a natural consequence of the MSW effect.

### 6.2 SNO: The Definitive Answer (2001--2002)

The Sudbury Neutrino Observatory (SNO) in Canada used heavy water (D$_2$O) to measure
three reactions:

$$\nu_e + d \to p + p + e^- \quad \text{(CC: } \nu_e \text{ only)}$$
$$\nu_x + d \to p + n + \nu_x \quad \text{(NC: all flavors)}$$
$$\nu_x + e^- \to \nu_x + e^- \quad \text{(ES: all flavors, } \nu_e \text{ enhanced)}$$

SNO found:

$$\Phi_{\text{NC}} = 5.21 \pm 0.27 \pm 0.38 \times 10^6 \text{ cm}^{-2}\text{s}^{-1}$$
$$\Phi_{\text{CC}} = 1.76 \pm 0.05 \pm 0.09 \times 10^6 \text{ cm}^{-2}\text{s}^{-1}$$

The total flux (NC) agreed perfectly with the SSM prediction. The electron-neutrino
flux (CC) was only $\sim 1/3$ of the total. The other $\sim 2/3$ had oscillated into
$\nu_\mu$ and $\nu_\tau$.

**Davis was right. Bahcall was right. The Sun was right. The neutrinos were oscillating.**

### 6.3 Oscillation Parameters

The solar neutrino problem, combined with KamLAND reactor data, determined:

$$\Delta m^2_{21} = (7.53 \pm 0.18) \times 10^{-5} \text{ eV}^2$$
$$\tan^2\theta_{12} = 0.437 \pm 0.029 \quad (\theta_{12} \approx 33.4^\circ)$$

This is the "Large Mixing Angle" (LMA) MSW solution, now established beyond any doubt.

---

## 7. Legacy

### 7.1 Davis's Achievement

The Homestake experiment was a 30-year tour de force of experimental physics:

- Extracting $\sim 15$ atoms of $^{37}$Ar from $10^{30}$ atoms of $^{37}$Cl every two
  months -- a dilution of 1 part in $10^{29}$ -- with $> 95\%$ efficiency
- Operating for three decades with consistent results
- Withstanding sustained skepticism from the community for two decades before
  vindication

Davis received the Nobel Prize in 2002 at age 87, shared with Masatoshi Koshiba
(for Kamiokande's confirmation of the deficit and detection of SN 1987A neutrinos)
and Riccardo Giacconi (for X-ray astronomy).

### 7.2 Impact on Physics

The solar neutrino problem:
1. **Proved neutrinos have mass** (oscillations require $m_1 \neq m_2$)
2. **Established neutrino oscillations** as a real phenomenon
3. **Confirmed the Standard Solar Model** to remarkable precision
4. **Opened the field of neutrino astronomy**
5. **Provided the first evidence for physics beyond the Standard Model**

### 7.3 The Bahcall-Davis Partnership

John Bahcall and Ray Davis maintained a 40-year collaboration between theory and
experiment. Bahcall continually refined his solar model predictions while Davis
continually improved his extraction and counting techniques. Their partnership is
one of the great examples of theory-experiment collaboration in physics. Bahcall died
in 2005, three years after Davis received the Nobel Prize. Both are commemorated at
Brookhaven National Laboratory.

---

## 8. The Solar Neutrino Unit (SNU)

The SNU deserves special mention as a unit unique to this field:

$$1 \text{ SNU} = 10^{-36} \text{ captures/(target atom} \cdot \text{second)}$$

For the Homestake experiment with $2.16 \times 10^{30}$ $^{37}$Cl atoms:

$$1 \text{ SNU} = 10^{-36} \times 2.16 \times 10^{30} = 2.16 \times 10^{-6} \text{ captures/second}$$
$$= 0.187 \text{ captures/day} = 5.6 \text{ captures/month}$$

So 7.6 SNU corresponds to about 42 $^{37}$Ar atoms produced per month, of which
roughly half decay before extraction. The actual number extracted per run was
typically 10--15 atoms.

---

## 9. Connection to Phonon-Exflation Framework

### 9.1 Neutrino Masses from the Dirac Spectrum

The solar neutrino problem's resolution established that neutrinos have non-zero masses
with $\Delta m^2_{21} = 7.53 \times 10^{-5}$ eV$^2$, implying at least one neutrino
mass $m_i \geq \sqrt{\Delta m^2_{21}} \approx 8.7 \times 10^{-3}$ eV.

In the phonon-exflation framework, neutrino masses arise from the lightest eigenvalues
of the internal Dirac operator $D_K(s)$ on the Jensen-deformed $SU(3)$. The Peter-Weyl
decomposition yields eigenvalues $\lambda_{(p,q)}(s)$ for each irreducible representation
$(p,q)$, and the neutrino mass eigenvalues are:

$$m_{\nu_i} = \frac{\lambda_i(s_0)}{\Lambda_{\text{KK}}}$$

where $\Lambda_{\text{KK}}$ is the Kaluza-Klein scale set by the internal radius and
$s_0$ is the deformation parameter fixed by $V_{\text{eff}}$.

The mass-squared differences:

$$\Delta m^2_{ij} = \frac{\lambda_i^2(s_0) - \lambda_j^2(s_0)}{\Lambda_{\text{KK}}^2}$$

are geometric predictions of the framework. The ratio:

$$\frac{\Delta m^2_{21}}{\Delta m^2_{32}} = \frac{\lambda_1^2 - \lambda_2^2}{\lambda_2^2 - \lambda_3^2} \approx 0.031$$

must be reproduced by the eigenvalue spectrum.

### 9.2 The MSW Effect and Internal Geometry

The MSW resonance condition involves the matter potential $A = 2\sqrt{2} G_F N_e E$,
which depends on $G_F$. In the phonon-exflation framework, $G_F$ is determined by the
$SU(2)_L$ gauge coupling and W-boson mass, both of which are outputs of the spectral
action on the deformed internal space.

The MSW effect is therefore fully determined by the internal geometry: the mass-squared
differences come from $D_K(s_0)$ eigenvalues, the mixing angles come from the
misalignment between $Z_3$ flavor eigenstates and mass eigenstates, and $G_F$ comes
from the spectral action. No free parameters are involved beyond $s_0$.

### 9.3 Solar Neutrino Data as Constraints

The Homestake experiment's measured rate of $2.56 \pm 0.23$ SNU, combined with the
SSM prediction of $7.6$ SNU, constrains the survival probability:

$$P(\nu_e \to \nu_e) \approx 0.34 \quad \text{(for } ^8\text{B neutrinos)}$$

This survival probability depends on $\Delta m^2_{21}$, $\theta_{12}$, and the solar
electron density profile -- all quantities that the phonon-exflation framework must
reproduce. The $\sim 8.7$ meV lower bound on neutrino masses, while far below the
framework's natural KK scale, requires the lightest Dirac eigenvalues to be suppressed
relative to the charged lepton and quark masses by several orders of magnitude.

### 9.4 The Hierarchy Problem for Neutrinos

The extreme lightness of neutrinos compared to charged fermions ($m_\nu / m_e \lesssim
10^{-6}$) is one of the most striking features of the particle spectrum. In the
phonon-exflation framework, this hierarchy could arise from:

1. **Sector-specific suppression**: The $(p,q)$ representations corresponding to
   neutrinos may have eigenvalues that are intrinsically small at the physical $s_0$
2. **See-saw-like mechanism**: The internal Dirac operator may contain both Dirac and
   Majorana-type mass terms, with the effective light neutrino mass suppressed by a
   heavy right-handed neutrino mass scale
3. **Topological protection**: In the BdG class DIII classification (Session 11),
   certain modes may be topologically protected near zero energy

The resolution of the neutrino mass hierarchy (normal vs. inverted ordering) by future
experiments (JUNO, DUNE, Hyper-Kamiokande) will provide a decisive test. The
phonon-exflation framework predicts one definite ordering from the eigenvalue structure
of $D_K(s_0)$ -- no parameter freedom allows switching between normal and inverted.

### 9.5 Davis's Experiment as a Founding Constraint

The Homestake experiment launched the neutrino oscillation program that ultimately
established neutrinos have mass. For the phonon-exflation framework, the neutrino
mass eigenvalues are among the most precisely known outputs that the Dirac spectrum
must reproduce. The 30-year dataset from Homestake, combined with SNO, KamLAND, and
atmospheric neutrino data, provides the tightest constraints on the lightest modes
of $D_K(s_0)$ -- the very modes where the geometric predictions are most sensitive
to the details of the Jensen deformation.

---

## References

1. Davis, R., Harmer, D.S., and Hoffman, K.C. (1968). "Search for Neutrinos from the
   Sun." *Physical Review Letters* 20, 1205-1209.
2. Bahcall, J.N. (1964). "Solar Neutrinos. I. Theoretical." *Physical Review Letters*
   12, 300-302.
3. Bahcall, J.N., Pinsonneault, M.H., and Basu, S. (2001). "Solar Models: Current
   Epoch and Time Dependences, Neutrinos, and Helioseismological Properties."
   *Astrophysical Journal* 555, 990-1012.
4. Cleveland, B.T. et al. (1998). "Measurement of the Solar Electron Neutrino Flux
   with the Homestake Chlorine Detector." *Astrophysical Journal* 496, 505-526.
5. Ahmad, Q.R. et al. (SNO Collaboration) (2002). "Direct Evidence for Neutrino Flavor
   Transformation from Neutral-Current Interactions in SNO." *Physical Review Letters*
   89, 011301.
6. Wolfenstein, L. (1978). "Neutrino oscillations in matter." *Physical Review D* 17,
   2369-2374.
7. Mikheev, S.P. and Smirnov, A.Yu. (1985). "Resonance enhancement of oscillations
   in matter and solar neutrino spectroscopy." *Soviet Journal of Nuclear Physics*
   42, 913-917.
8. Pontecorvo, B. (1946). "Inverse beta process." Chalk River Laboratory report
   PD-205.
9. Davis, R. (2003). "A half-century with solar neutrinos." Nobel Lecture, *Reviews
   of Modern Physics* 75, 985-994.
10. Bahcall, J.N. (2005). "Solar models and solar neutrinos." *Physics of Plasmas*
    12, 072301.
