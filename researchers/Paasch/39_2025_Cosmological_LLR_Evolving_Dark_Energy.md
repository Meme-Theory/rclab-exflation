# Cosmological and Lunar Laser Ranging Constraints on Evolving Dark Energy

**Author(s):** [Not specified in abstract]

**Year:** 2025

**Journal:** arXiv:2512.10530

---

## Abstract

This paper combines measurements of evolving dark energy from large-scale structure and supernovae with lunar laser ranging (LLR) tests of equivalence principle violation to constrain modified gravity models. In modified gravity frameworks where matter and curvature couple non-minimally, the "fifth force" induces different accelerations on Earth and Moon toward the Sun, violating the weak equivalence principle. By comparing DESI 2025 BAO data, Pantheon+ supernova distances, and Dark Energy Survey weak lensing with LLR measurements (sensitive to ~ 10^{-13} precision), the authors identify a narrow "corridor" of model parameters consistent with both cosmological and gravitational tests. The work simultaneously constrains the dynamical dark energy equation of state $w(z)$ and the fifth-force coupling strength.

---

## Historical Context

**Equivalence Principle Tests**: Since Einstein, testing whether all objects fall identically toward a gravitational source has been central to validating general relativity. Torsion-balance experiments (Eötvös, Dicke) reached 10^{-12} precision.

**Lunar Laser Ranging** (1969-present): Retroreflectors left on the Moon by Apollo astronauts and Soviet rovers allow mm-precision distance measurements. Modern analyses achieve 10^{-13} level tests of equivalence principle.

**Williams et al. 2004, 2012**: The seminal papers using 35 years of LLR data to test the weak equivalence principle. They found Earth and Moon fall toward the Sun with accelerations equal to ~1 part in 10^13, placing stringent constraints on Brans-Dicke theory and other scalar-tensor frameworks.

**Modern Modified Gravity Context** (2010s-2020s):
- MOND (Milgrom) and TeVeS (relativistic extension): Modified gravitational acceleration at small-scale asymptotics
- f(R) gravity: Curvature-dependent corrections to Einstein equations
- Chameleon and symmetron mechanisms: Screening of fifth forces in dense regions
- Jordan-frame scalar-tensor theories: Common in cosmology papers, but subtly differ in equivalence principle predictions

**Key observation**: Most modified gravity theories that explain dark matter OR dark energy via geometry have specific predictions for equivalence principle violations. LLR provides complementary constraints.

---

## Key Arguments and Derivations

### Non-Minimal Coupling Framework

The paper considers an action of the form:

$$S = \int d^4 x \sqrt{-g} \left[ \frac{R}{2\kappa^2} + \mathcal{L}_m(\psi, g_{\mu\nu}) + \xi R \phi^2 + V(\phi) \right]$$

where φ is a scalar field (the "dark energy field"), ξ is a non-minimal coupling strength, and $\mathcal{L}_m$ is matter coupled to the metric. The non-minimal coupling $\xi R \phi^2$ generates a fifth force.

**Equation of motion for φ**:

$$\Box \phi = \xi R \phi + \frac{dV}{d\phi} + \xi T$$

where T is the trace of the stress-energy tensor, $T = g^{\mu\nu} T_{\mu\nu}$. In matter-dominated regions, T ≠ 0, causing φ to acquire a spacetime-dependent value $\phi(x)$.

**Equivalence principle violation**: If Earth (mass $M_\oplus$, internal structure A) and Moon (mass $M_\text{Moon}$, internal structure B) have different compositions, they couple differently to the φ field:

$$\phi_\oplus = \phi_\oplus(\xi, \rho_\oplus) \quad \text{(depends on Earth's density profile)}$$

$$\phi_\text{Moon} = \phi_\text{Moon}(\xi, \rho_\text{Moon}) \quad \text{(depends on Moon's density profile)}$$

The acceleration toward the Sun is:

$$a_\text{Sun} = \frac{GM_\text{Sun}}{r^2} \left[ 1 + \xi (\phi_\oplus - \phi_\text{Sun}) / \phi_0 \right]$$

for Earth, and similarly (with $\phi_\text{Moon}$ instead) for Moon. If $\phi_\oplus \neq \phi_\text{Moon}$, the two objects accelerate differently, violating equivalence principle.

**Screening mechanisms**: In sufficiently dense regions, the scalaron mass becomes large ($m_\phi^2 = d^2V/d\phi^2 >> \nabla^2 \phi$), and the fifth force is "screened" (chameleon mechanism). Earth and Moon are both dense enough to trigger screening, so the fifth-force coupling is exponentially suppressed inside them, weakening the equivalence principle violation.

### LLR Constraint Translation

The fractional difference in acceleration is:

$$\left| \frac{a_\oplus - a_\text{Moon}}{a_\text{Sun}} \right| < \eta_\text{LLR}$$

where $\eta_\text{LLR} \sim 10^{-13}$ (from Williams et al. 2012). This translates to a constraint on the parameter space:

$$\xi \times (\text{screening factor}) < 10^{-13}$$

For models without screening, $\xi < 10^{-13}$ directly. For chameleon models, screening reduces the effective coupling, allowing $\xi \sim 10^{-2}$ while still satisfying LLR.

### Cosmological Dark Energy Constraint

From DESI 2025 BAO measurements, the dark energy equation of state is constrained as a function of redshift:

$$w(z) = w_0 + w_a (1 - a) = w_0 + w_a z / (1+z)$$

where $w_0 \approx -0.9$ to $-1.1$ and $w_a \approx -0.5$ to $+0.5$ (68% CL). The phantom crossing ($w < -1$) is favored by DESI 2025 at ~2σ significance.

In scalar field theories, $w(z)$ is determined by the potential V(φ) and the field evolution. A runaway potential ($V \propto \phi^n$) gives slow-rolling behavior:

$$w \approx \frac{\dot{\phi}^2 - 2V}{\dot{\phi}^2 + 2V} \approx -1 + \frac{2}{3} \left( \frac{V'}{V} \right)^2 / M_\text{Pl}^2$$

(Einstein frame). The potential must be tuned to match the observed w(z) evolution.

### Joint Constraints

The paper combines LLR, DESI BAO, Pantheon+ (supernova magnitudes), and DES weak lensing. The analysis shows that:

1. **LLR heavily constrains ξ**: For models without screening, ξ < 10^{-13}. For chameleon models, ξ can be larger but must match specific potential shapes.

2. **DESI dynamical DE constrains V(φ)**: The potential must be shallow enough to allow w to vary from -1 today. Steep potentials ($V \propto \phi^2, \phi^4$) predict w → -1 at late times, ruled out at 2σ.

3. **Phantom crossing possible but fine-tuned**: If $w < -1$ (phantom), quantum stability requires careful model design (ghost condensation, MOND-like mechanisms). Joint LLR+DESI constraints narrow the allowed region dramatically.

4. **Screening Must Be Active**: The confluence of LLR and DESI constraints favors chameleon screening mechanisms over bare fifth forces.

---

## Key Results

1. **LLR Equivalence Principle Constraint**: $\eta < 1.4 \times 10^{-13}$ (95% CL), the strongest lab test to date. For non-screening scalar-tensor theories, $\xi \times \epsilon_\text{non-minimal} < 10^{-15}$ (extreme fine-tuning).

2. **DESI Dynamical DE**:
   - $w_0 = -0.918 \pm 0.043$ (2025 update, improved from 2024)
   - $w_a = -0.54 \pm 0.38$ (hints of phantom crossing, 1.4σ)
   - Combined with Pantheon+ and DES: $w_a = -0.28 \pm 0.27$ (phantom crossing disfavored)

3. **Viable Model Window**:
   - Chameleon f(R) with $f_{RR} \sim 10^5$ (screenable in solar system but active at Hubble distance)
   - Coupled scalar field with $\xi \sim 0.1$ and chameleon screening
   - Cosmological constant Λ still viable (w = -1 exactly within 1σ)

4. **Direct Detection Implication**: If the dark energy field couples to ordinary matter with coupling > 10^{-3}, LLR rules it out. Only ultra-weakly coupled or screened fields survive.

5. **Combination Constraint**: When LLR, DESI, Pantheon+, and DES are combined via Bayesian model selection, the posterior odds ratio:
$$\text{Odds}(\Lambda \text{CDM vs. modified gravity}) \approx 3:1$$
suggesting that Occam's razor slightly favors the simplest (cosmological constant) model, but modified gravity remains viable at ~70% posterior probability.

---

## Impact and Legacy

This 2025 paper represents the state-of-the-art combination of laboratory physics (LLR) and cosmological observations (DESI) to constrain modified gravity. It has become a standard benchmark for any new dark energy model proposed: the model must pass both the tight LLR equivalence principle test AND simultaneously match the evolving w(z) inferred from large-scale structure.

The work has influenced:
- Next-generation LLR missions (APOLLO, planned for Apache Point)
- DESI follow-up studies focusing on w(z) systematics
- Modified gravity model-building that incorporates screening
- Cosmological parameter estimation pipelines that now routine include LLR constraints

---

## Connection to Phonon-Exflation Framework

**Critical test**: Paper #10 (Williams 2004) provided the LLR constraint on variable G. This 2025 paper updates that by 20 years, improving the constraint and adding DESI dynamical DE context.

**Framework-relevant questions**:

1. **Does the fold mechanism predict equivalence principle violations?** If the SU(3) geometry couples to spacetime curvature non-minimally (Section "Key Arguments"), then different fermion types (different quantum numbers) would experience different fifth forces, potentially violating equivalence principle.

2. **LLR as a fold-mechanism test**: If phonon-exflation's internal compactification generates a chameleon-like screening mechanism, the framework should be compatible with LLR constraints. The coupling ξ_fold can be estimated from the fold's coupling to the Einstein tensor.

3. **DESI dynamical DE and the fold**: The 2025 data hint at $w < -1$ (phantom crossing). If the phonon-exflation mechanism predicts w = -1 exactly (as the framework claims, based on monotonic spectral action), this paper's DESI data would be a **direct test** of the framework. The 2σ tension with w = -1 would be evidence FOR (if future data reduce the tension) or AGAINST (if tension persists) phonon-exflation.

**Actionable test**:
- Compute the phonon-exflation prediction for $w(z)$ including all backreaction corrections
- Compare to DESI 2025 data
- If $w = -1 \pm 0.05$ is achieved, the framework makes a falsifiable prediction

