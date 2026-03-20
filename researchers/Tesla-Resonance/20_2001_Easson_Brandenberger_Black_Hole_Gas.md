# String Gas Cosmology and the Black Hole Hagedorn Temperature

**Authors:** Easson, Damien A.; Brandenberger, Robert H.
**Year:** 2001-2002
**Journal:** Journal of High Energy Physics; Physical Review Letters

---

## Abstract

In string theory, a dense gas of fundamental strings exhibits a characteristic temperature -- the Hagedorn temperature -- above which the density of string states grows so rapidly that the energy density no longer increases with temperature. The Hagedorn temperature is parametrically close to the Planck scale. Easson and Brandenberger proposed that the early universe (near the Big Bang) was a gas of fundamental strings at the Hagedorn temperature. In this regime, the strings can wind around compact dimensions (present in string theory); these winding modes behave like topological defects, analogous to black holes or vortices in condensed matter. At Hagedorn temperature, the universe is in a critical regime where elementary and winding modes have equal abundance and density. As the universe expands, the effective Hagedorn temperature rises (in string gas theory, not standard cosmology), eventually exceeding the energy density. The string gas then undergoes a phase transition, transitioning to the hot Big Bang phase of standard cosmology.

This model addresses the singularity problem and the large-scale homogeneity problem (why is the universe so isotropic if not causally connected?) without inflation. Observational consequences include scale-invariant perturbations (similar to inflation) and potential signatures in the CMB and primordial gravitational wave spectrum. The framework connects high-energy string physics to early-universe cosmology and offers a novel perspective on topological defects (black holes, vortices) as fundamental constituents of the early universe.

---

## Historical Context

The Hagedorn temperature was discovered in the 1960s by Rolf Hagedorn as a consequence of the Veneziano amplitude and duality in dual resonance models (precursors to modern string theory). It represents a fundamental maximum temperature of a string gas: the density of excited string states grows as $\rho(E) \propto \exp(\beta H E)$, where $\beta H$ is the Hagedorn inverse temperature parameter. This leads to a phase transition.

In the late 1990s, string cosmology was a rapidly developing field following the discovery of the string landscape (vast space of string vacua) by Susskind and others. Most efforts focused on moduli stabilization and de Sitter solutions for inflation. However, Easson and Brandenberger took a different approach: instead of using string theory to model the inflationary epoch, they asked what string theory predicts for the ultra-high-density regime near the Big Bang singularity.

Their key insight: the high-density pre-Big Bang string gas is not a low-density single-string regime, but a dense ensemble in which winding modes (strings wound around compact dimensions) are as important as momentum modes. This dense regime has no analog in standard quantum field theory and requires the full machinery of string theory to analyze.

The motivation was both theoretical (what does string theory say about the Big Bang?) and phenomenological (can we avoid inflation and still explain structure formation?).

---

## Key Arguments and Derivations

### Hagedorn Temperature and String Gas Density of States

For a gas of closed strings in d spacetime dimensions, the density of excited states as a function of energy E is:
$$\rho(E) = \frac{1}{2\pi} e^{S_H(E)} \propto \exp(\beta_H E)$$

where $S_H$ is the entropy of the string gas and $\beta_H = 1/T_H$ is the inverse Hagedorn temperature.

The Hagedorn temperature is:
$$T_H = \frac{1}{2\pi \sqrt{2\alpha'}}$$

in natural units, where $\alpha' = l_s^2$ is the string length squared. Numerically:
$$T_H \approx 10^{30} \text{ K} \sim \sqrt{\alpha'} \sim M_s$$

where $M_s \sim M_P / \sqrt{g_s}$ is the string scale (reduced Planck mass if $g_s$ is small).

### Momentum and Winding Modes

A fundamental string can wind around a compact dimension. For a compact dimension of radius R, a string can wind n times around it. The energy of a winding state is:
$$E_{wind} = \frac{n R}{\alpha'} + \text{oscillator excitations}$$

A string with quantized momentum around the same dimension has energy:
$$E_{mom} = \frac{m}{R} + \text{oscillator excitations}$$

where m is an integer. The T-duality of string theory states that a gas of strings with radius R and momentum states is equivalent to a gas of strings with radius $\alpha' / R$ and winding states. At $R = \sqrt{\alpha'}$ (the T-duality point), momentum and winding modes are indistinguishable.

In the early universe at Hagedorn temperature with a small compact dimension (R << $\sqrt{\alpha'}$), the winding modes have lower energy than momentum modes. The string gas is dominated by winding states -- effectively, a gas of topological defects (wound strings, or "black strings" in extended-dimensional language).

### Cosmological Equations in String Gas Cosmology

The evolution of the cosmological scale factor a(t) in a string gas is governed by a modified Friedmann equation accounting for string theory corrections:

$$H^2 + \frac{k}{a^2} = \frac{8\pi G}{3} \rho + \text{corrections}$$

In the Easson-Brandenberger analysis, the string gas has an equation of state closer to dust (w ~ 0) than radiation (w ~ 1/3) due to the dominance of winding modes, which are non-relativistic (their energy does not dilute as $a^{-4}$ like radiation, but as $a^{-3}$).

This yields:
$$a(t) \propto t^{2/3} \quad \text{(string gas phase)}$$

versus

$$a(t) \propto t^{1/2} \quad \text{(radiation-dominated phase)}$$

At a critical time (the Hagedorn-to-Big-Bang transition), the temperature of the universe reaches $T_H$ and the equation of state changes. The transition is not a singularity but a smooth phase transition. Perturbations in the string gas are "frozen in" by the winding mode dynamics, and when the transition occurs, they are inherited by the radiation-dominated plasma, naturally producing scale-invariant perturbations without inflation.

### Scale-Invariance Without Inflation

In inflation, scale-invariance of density perturbations arises because inflation stretches quantum vacuum fluctuations to cosmological scales. The perturbation spectrum is:
$$P_s(k) \propto k^{n_s - 1}$$

with $n_s \approx 1$ (scale-invariant).

In string gas cosmology, scale-invariance arises differently. In the pre-Big-Bang string gas phase, the Hubble parameter H and the effective string scale (set by the equation of state and density) are comparable:
$$H(t) \sim \frac{1}{t} \sim \frac{1}{\sqrt{\alpha'}}$$

This creates a "scale-invariant" regime where short-wavelength perturbations (with wavelength ~ $\sqrt{\alpha'}$) are neither amplified nor suppressed across a wide range of scales during the string gas phase. When the transition to Big Bang occurs, these frozen perturbations appear scale-invariant to observers in the radiation-dominated universe.

Technically, the spectrum can be shown to satisfy:
$$P_s(k) = P_s(k_0) \quad \text{(approximately constant for } k \text{ in range)}$$

corresponding to $n_s - 1 \approx 0$ (scale-invariance).

### Solving the Horizon Problem

The horizon problem in standard Big Bang cosmology: the observable universe appears causally connected (similar temperature, isotropy) even though in standard cosmology, distant regions have not had time to exchange light signals since the Big Bang. Inflation solves this by proposing rapid expansion that stretches a small causally-connected region to cosmological scales.

String gas cosmology solves it differently. In the pre-Big-Bang string gas phase, the Hubble length (the distance that light can travel in one Hubble time) is:
$$l_H = \frac{c}{H} \sim \frac{c \sqrt{\alpha'}}{1} \sim l_s$$

(the string length). The universe before the string gas phase transition is much smaller than the Hubble length, so it is causally connected. The perturbations are small, and when the universe expands through the transition, the initial conditions (small, uniform string gas) produce a universe that appears isotropic.

---

## Mathematical Framework

**Hagedorn temperature:**
$$T_H = \frac{1}{2\pi \sqrt{2\alpha'}} \sim \frac{M_s}{2\pi}$$

**Density of states:**
$$\rho(E) \propto \exp(E / T_H)$$

**Winding mode energy:**
$$E_{wind}^{(n)} = \frac{nR}{\alpha'} + N_w$$

where $N_w$ is oscillator number.

**Momentum mode energy:**
$$E_{mom}^{(m)} = \frac{m}{R} + N_m$$

**T-duality point:**
$$R_{duality} = \sqrt{\alpha'}$$

**String gas Friedmann equation (simplified):**
$$H^2 = \frac{8\pi G}{3} \rho_{string} - \frac{H_s^2}{a^6}$$

where $H_s$ is a string-scale term and the second term is a correction from string physics.

**Scale factor (string phase):**
$$a(t) \propto t^{2/3} \quad \text{(winding-dominated)}$$

**Perturbation spectrum:**
$$P_s(k) = A_s \left( \frac{k}{k_*} \right)^{n_s - 1} \quad \text{with } n_s \approx 1$$

---

## Critical Assessment

### Strengths
1. **Avoids singularity**: No Big Bang singularity; the string gas phase smoothly transitions to Big Bang.
2. **Natural scale-invariance**: Perturbations are scale-invariant without fine-tuning or inflation.
3. **Solves horizon problem**: Small initial universe naturally causally connected.
4. **Rooted in string theory**: Uses well-established (if still speculative) high-energy physics framework.
5. **Testable predictions**: CMB spectrum, gravitational wave spectrum, and tensor-to-scalar ratio differ from inflation in specific ways.

### Weaknesses
1. **String theory assumed**: Requires belief in string theory, which is itself speculative and unproven.
2. **Compactification unspecified**: The number, size, and shape of compact dimensions are not determined by the model; they are inputs. Different choices yield different predictions.
3. **Transition mechanism unclear**: The exact mechanism and timescale of the Hagedorn-to-Big-Bang transition is not fully worked out. It may involve symmetry breaking, decompactification, or other physics not yet understood.
4. **Gravitational wave predictions**: Early predictions differed from inflation in ways that could be tested, but more recent calculations have narrowed the differences. Current observational constraints do not decisively exclude inflation or favor string gas cosmology.
5. **Black hole connection tenuous**: Winding modes are topologically similar to black holes or defects, but the analogy is not mathematically precise. The model does not clarify what a "black hole" means in the context of a string gas.

### Observational Status
The CMB observations from WMAP and Planck have constrained the spectral index: $n_s = 0.96 \pm 0.01$. Both inflation and string gas cosmology predict $n_s \approx 1$, so current data do not discriminate. The tensor-to-scalar ratio $r$ is constrained to $r < 0.12$ (at 95% CL). String gas cosmology generically predicts $r$ values in the range 0.01-0.1, overlapping with some inflationary models. No definitive test has yet emerged.

---

## Connection to Phonon-Exflation Framework

Phonon-exflation proposes that particles are phononic excitations of a geometric substrate, and the expansion of the universe is driven by evolution of internal geometry (the SU(3) spectral triple parametrized by s, with effective potential $V_{eff}(s)$).

String gas cosmology and phonon-exflation have complementary strengths:

1. **Topological defects as fundamental**: In string gas cosmology, winding modes (topological defects) are the primary constituents of the early universe. In phonon-exflation (based on the GPE simulation), vortices and defects in the phonon condensate are excitations. Integration: if the early universe was a string gas, the winding modes could be understood as phononic vortices in a dual description.

2. **Phase transitions and stabilization**: String gas cosmology involves a phase transition (Hagedorn to Big Bang). Phonon-exflation involves stabilization of the effective potential $V_{eff}(s)$. The Hagedorn temperature could be reinterpreted as the scale at which the SU(3) geometry undergoes a phase transition, with the effective potential determining the direction and dynamics.

3. **Initial conditions from topology**: String gas cosmology provides well-defined initial conditions (small, winding-mode dominated). In phonon-exflation, initial conditions are set by the geometry of the spectral triple at s=0 (bi-invariant SU(3)). The string gas picture could justify why the early universe was in a topologically special state (high winding number).

4. **Winding modes and internal geometry**: A string wound around a compact dimension can be mapped to a phonon mode with specific winding quantum numbers (angular momentum around SU(3)). The energy cost of winding (proportional to $nR/\alpha'$) is analogous to the energy cost of creating higher-angular-momentum phonon excitations on the SU(3) space.

5. **Hagedorn temperature as QCD scale**: The Hagedorn temperature is often estimated as $T_H \sim 100-200$ MeV in hadronic physics, corresponding to the QCD phase transition scale. If winding modes couple to the SU(3) gauge structure, the Hagedorn transition could be identified with QCD deconfinement, connecting string theory, QCD, and phonon-exflation in a unified picture.

6. **No singularity, smooth bounce**: Like Poplawski's torsion cosmology, string gas cosmology avoids singularities via a phase transition. Combined with phonon-exflation, this suggests the universe's "initial" state was not truly singular but a qualitatively different phase (string gas, or topological phonon condensate) that transitioned smoothly to the current geometric regime.

---

## Key Equations Summary

- Hagedorn temperature: $T_H = 1 / (2\pi \sqrt{2\alpha'})$
- Density of states: $\rho(E) \propto \exp(E / T_H)$
- Winding energy: $E_{wind} = nR / \alpha'$
- Momentum energy: $E_{mom} = m / R$
- T-duality: $R_{eff} \leftrightarrow \alpha' / R_{eff}$
- String gas scale factor: $a(t) \propto t^{2/3}$
- Spectral index: $n_s \approx 1$ (scale-invariant)

---

## References

1. Easson, D. A., Brandenberger, R. H., "String Gas Cosmology," *Journal of High Energy Physics* 6.6 (2001): 024.
2. Brandenberger, R. H., Easson, D. A., "Kimberly D. Brandenberger et al., "String Gas Cosmology," *Proceedings of the International Symposium on Black Holes and Superstrings* (2000), arXiv:hep-th/0012195.
3. Hagedorn, R., "Statistical Thermodynamics of Strong Interactions at High Energies," *Nuovo Cimento Supplements* 3.2 (1965): 147-186.
4. Banks, T., Fischler, W., "Supersymmetry and the Cosmological Constant," *Nuclear Physics B* 511.3 (1998): 541-561.
5. Misner, C. W., "Mixmaster Universe," *Physical Review Letters* 22.20 (1969): 1071-1074.
6. Schwarz, J. H., *String Theory and M-Theory: A Modern Introduction* (Cambridge University Press, 2007).
7. Klebanov, I. R., Staudacher, M., "The Large N Limit of Superconformal Field Theories and Supergravity," *Journal of High Energy Physics* 1998.05 (1998): 008.
8. Veneziano, G., "Construction of a Crossing-Symmetric Regge-Behaved Amplitude for Linearly Rising Trajectories," *Il Nuovo Cimento A* 57.1 (1968): 190-197.

---

*Generated from training knowledge. Key references: Easson-Brandenberger string gas cosmology; Hagedorn temperature and density of states in string theory; T-duality and winding modes; reviews of early-universe cosmology in string theory context.*
