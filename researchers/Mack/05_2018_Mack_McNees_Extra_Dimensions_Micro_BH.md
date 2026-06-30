# Bounds on Extra Dimensions from Micro Black Holes in Context of Metastable Higgs Vacuum

**Author(s):** Katherine J. Mack, Robert McNees
**Year:** 2018
**Journal/ArXiv:** arXiv:1809.05089, Physical Review D

---

## Abstract

The Standard Model of particle physics indicates that the Higgs field potential becomes unstable at extremely high energy scales (~10^11 GeV), above which the vacuum decays catastrophically. However, our universe remains in the electroweak vacuum despite the universe reaching temperatures well above this scale in the hot Big Bang. Extra-dimensional theories offer potential resolution by modifying the running of the Higgs mass and changing vacuum stability properties. Mack and McNees examine constraints on extra-dimensional models from considering an alternative hazard: ultra-high energy cosmic ray (UHECR) collisions producing micro black holes. In extra-dimensional models with lowered gravitational scale (TeV-scale gravity), UHECR collisions readily produce black holes that rapidly evaporate via Hawking radiation. However, if such black holes produce high-energy particles (including Higgs bosons) that trigger vacuum decay, their absence in cosmic ray data constrains the extra-dimensional parameter space. The authors find that the excluded range is approximately 10^17 eV ≲ E* ≲ 10^18.8 eV for single extra dimensions, with tighter bounds for additional spatial dimensions, identifying previously inaccessible parameter space unconstrained by collider experiments, laboratory gravity tests, or stellar observations.

---

## Historical Context

The Higgs boson's discovery at the Large Hadron Collider in 2012 opened a door to understanding the weakest fundamental force and electroweak symmetry breaking. However, precision measurements of the Higgs mass reveal a troubling property: the Standard Model Higgs potential is not stable at all energy scales. Above approximately 10^11 GeV, quantum loop corrections flip the sign of the Higgs mass term, rendering the potential unstable. At such energies, vacuum tunneling becomes possible, and the universe would decay into a lower-energy state, destroying all structure.

Historically, this was not a concern for distant astrophysical phenomena. However, the universe did experience temperatures far exceeding 10^11 GeV in the hot Big Bang. The fact that we observe a universe in the electroweak vacuum at today's vastly lower temperature (0.0001 eV) presents a puzzle: why did the universe not decay in the early universe?

Several resolutions have been proposed: (1) the measured Higgs mass is slightly different than currently determined; (2) additional physics (supersymmetry, or new particles) stabilizes the vacuum; (3) extra dimensions modify the running of the Higgs mass term. Theories with extra spatial dimensions, motivated by string theory and other frameworks, can indeed alter the high-scale behavior of the Standard Model.

Mack and McNees explore a different but related constraint. In extra-dimensional theories with TeV-scale gravity, the gravitational coupling constant is enhanced compared to four dimensions. This allows ultra-high energy cosmic ray (UHECR) collisions to produce black holes with masses of order TeV or higher. Such micro black holes rapidly evaporate through Hawking radiation, producing energetic Standard Model particles. If these particles include high-energy Higgs bosons above the instability scale, they could trigger vacuum decay. The absence of such catastrophic vacuum decay events in the observable universe constrains extra-dimensional models.

---

## Key Arguments and Derivations

### Higgs Vacuum Stability

The Higgs potential in the Standard Model, running under quantum corrections (renormalization group equations), is written:

$$V(\phi) = \lambda(\mu) \left( \phi^2 - v^2 \right)^2 / 4$$

where $\lambda(\mu)$ is the running Higgs self-coupling and $\mu$ is the energy scale. At low energy ($\mu \sim 100$ GeV), $\lambda > 0$, and the minimum is at $\phi \neq 0$ (electroweak symmetry broken). However, the running of $\lambda$ due to top quark and gauge loops is such that:

$$\beta_\lambda \approx -12 y_t^4 + \ldots$$

where $y_t$ is the top quark Yukawa coupling. The negative beta function causes $\lambda$ to decrease and eventually turn negative at high scales. The instability scale $M_{inst}$ is where $\lambda(M_{inst}) = 0$.

With current precision measurements of the Higgs mass and top quark mass, the instability scale is estimated at approximately:

$$M_{inst} \sim 10^{11} \text{ GeV}$$

with theoretical uncertainties of order a factor of a few in the exponent.

### Gravitational Scale in Extra Dimensions

In theories with $n$ extra spatial dimensions, the observed Newton's constant $G_N$ in four dimensions is related to the fundamental Planck scale $M_*$ (the true scale where quantum gravity becomes strong) by:

$$G_N \sim \frac{1}{M_*^{2+2n} V_{extra}}$$

where $V_{extra}$ is the volume of the compactified extra dimensions. This can be rewritten as:

$$M_{Pl}^2 = M_*^{2+2n} V_{extra} / (8\pi^{3+n})$$

where $M_{Pl} \approx 2.4 \times 10^{18}$ GeV is the reduced Planck mass. If the extra dimensions have size $R$, then $V_{extra} \sim R^n$, and:

$$M_* \sim M_{Pl} \left( \frac{M_{Pl} R}{1} \right)^{-n/(2+2n)}$$

For large extra dimensions, $M_*$ can be much lower than $M_{Pl}$, potentially in the TeV range.

### Micro Black Hole Production from Cosmic Rays

Ultra-high energy cosmic rays with center-of-mass energy $E_{cm}$ can produce a black hole if the impact parameter is less than the gravitational radius:

$$r_s = \frac{2 G M}{c^2} = \frac{M}{M_*^{1+n}}$$

where $M \sim E_{cm}$ is the black hole mass. The cross section for black hole production is:

$$\sigma_{BH} \sim \pi r_s^2 \sim \pi M^{2/(1+n)} / M_*^{2}$$

For $M \sim E_{cm}$ and $n=1$ (single extra dimension), a cosmic ray with $E_{cm} \sim 10$ TeV readily produces a black hole if $M_* \sim 1$ TeV.

### Hawking Evaporation and Higgs Emission

A black hole of mass $M$ evaporates via Hawking radiation with temperature:

$$T_H = \frac{\hbar c^3}{8 \pi k_B G M} = \frac{M_* M^{1+n}}{M_*^2 (1+n) \pi k_B}$$

As the black hole evaporates, it passes through all energy scales. If the maximum temperature $T_H$ exceeds the Higgs instability scale $M_{inst}$, the black hole can emit a Higgs boson at energy $E_H \sim M_{inst} >> m_h$ (where $m_h \approx 125$ GeV is the Higgs mass). Such a high-energy Higgs can trigger vacuum decay through tunneling.

The probability of vacuum decay via tunneling is suppressed by an action $S_{tunnel}$, which depends exponentially on the Higgs energy and mass. For Higgs bosons at energy $E_H > M_{inst}$, the decay rate becomes significant.

### Vacuum Decay Constraint

If a micro black hole from cosmic ray collision evaporates and emits a high-energy Higgs boson with probability P and tunnel rate $\Gamma_{tunnel}$, the expected number of vacuum decay events in the observable universe is:

$$N_{decay} = N_{UHECR} \times P_{BH} \times P_{H} \times \Gamma_{tunnel} \times t_0$$

where $N_{UHECR}$ is the total number of UHECR events observed, $P_{BH}$ is the probability a collision produces a black hole, $P_H$ is the probability it emits a Higgs, $\Gamma_{tunnel}$ is the vacuum decay rate, and $t_0$ is the age of the observable universe.

For $N_{decay} < 1$ (no observed vacuum decay), the fundamental scale $M_*$ and number of extra dimensions $n$ are constrained.

---

## Key Results

1. **Excluded parameter space for single extra dimension**: The analysis excludes the range 10^17 eV ≲ E* ≲ 10^18.8 eV for models with a single extra spatial dimension. This represents a previously inaccessible region of parameter space not constrained by:
   - Collider experiments (which probe only up to ~10 TeV center-of-mass energy)
   - Laboratory gravity measurements (which test Newton's law down to ~micron scales, constraining M* > 10^4 GeV typically)
   - Astrophysical tests (neutron stars, supernova cooling)

2. **Multiple extra dimensions**: For two extra dimensions, the excluded range shifts to approximately 10^15.5 eV ≲ E* ≲ 10^17.5 eV, becoming more restrictive. For each additional extra dimension, the constraints tighten further.

3. **Cosmic ray energy dependence**: The constraint depends critically on the highest-energy cosmic rays observed. The Pierre Auger Observatory and Telescope Array detect cosmic rays up to ~10^20 eV. UHECRs at the highest energies (>10^19 eV) produce the most energetic black holes and are most likely to trigger vacuum decay, providing the strongest constraints.

4. **No observed vacuum decay events**: The fact that we do not observe sudden transitions to an alternate vacuum (e.g., no Higgs field value suddenly changing in our region of space) over cosmic timescales provides a null result that constrains new physics.

5. **Complementary to other bounds**: The constraint is complementary to direct searches for extra dimensions at the LHC. While collider searches are sensitive to light Kaluza-Klein modes and can constrain some parameter ranges, the UHECR vacuum decay constraint accesses complementary regions of parameter space.

6. **Implications for hierarchy problem**: The excluded region includes some energy scales that might be invoked to solve the hierarchy problem (why gravity is weak) via large extra dimensions. This suggests that if extra dimensions exist, they are either much larger (M* < 10^17 eV, smaller radius) or much smaller (M* > 10^18.8 eV, larger radius), limiting certain class of solutions.

---

## Impact and Legacy

This work bridges astrophysical observations (ultra-high energy cosmic rays) with fundamental physics (vacuum stability and extra dimensions). It demonstrates how macroscopic, observable phenomena can constrain fundamental physics through indirect arguments. The paper has influenced subsequent work on vacuum stability in BSM theories and connections between cosmology and collider physics.

The recognition that the stability of the electroweak vacuum across cosmic history provides a laboratory for testing fundamental theory has motivated further research into how high-energy processes in the universe constrain new physics--a field sometimes called "astroparticle physics constraints on BSM theory."

---

## Connection to Phonon-Exflation Framework

In the phonon-exflation framework, extra spatial dimensions are not compactified over fixed length scales but emerge dynamically from the geometry of the internal space (M4 x SU(3) bundle). This differs fundamentally from ADD and Randall-Sundrum models with static compactification.

Mack and McNees' constraint on extra dimensions assumes fixed Kaluza-Klein mode masses and static compactification geometry. In phonon-exflation:

1. **Dynamical compactification**: The fold in the compactified space evolves with cosmic time, modifying the effective gravitational coupling and Kaluza-Klein masses as the internal geometry unfolds during the expansion.

2. **Modified vacuum stability**: The Higgs potential in the framework would not run according to Standard Model RGE alone but would be modified by the coupling to the compactified geometry and the spectral action. The instability scale $M_{inst}$ might be shifted or eliminated by geometric effects.

3. **Black hole evaporation in curved space**: If the underlying geometry is not flat but curved (as required by the framework), Hawking radiation properties would be modified. The temperature and spectrum of Hawking radiation depend on the geometry, potentially affecting vacuum decay probabilities.

4. **No sharp extra-dimensional scale**: Rather than a discrete set of Kaluza-Klein modes with specific masses (as in traditional extra-dimensional models), the framework predicts a continuous spectrum of geometric modes corresponding to different folding modes of the SU(3) fiber. This would alter the cross section for black hole production via cosmic ray collisions.

5. **Planck-scale physics as probe**: Mack and McNees use UHECR collisions to probe Planck-scale physics. In phonon-exflation, such high-energy events would probe not just quantum gravity but the specific geometry of the compactified space, providing a test of the framework's geometric predictions.

The framework's prediction that gravity and particle physics emerge from a single geometric substrate could be tested through precise measurements of black hole production cross sections in nature or at colliders, if the framework's geometric effects differ measurably from traditional extra-dimensional models.
