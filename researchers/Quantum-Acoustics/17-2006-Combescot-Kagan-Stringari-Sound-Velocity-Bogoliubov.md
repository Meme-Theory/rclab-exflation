# Sound Velocity and Multibranch Bogoliubov Spectrum in the BEC-BCS Crossover

**Authors:** Roland Combescot, Mikhail Yu. Kagan, Sandro Stringari
**Year:** 2006
**Journal:** Physical Review A, Vol. 73, 013613 (2006); related work Vol. 74, 042717 (2006)

---

## Abstract

This paper investigates collective excitations and sound velocities in ultracold Fermi gases throughout the BEC-BCS crossover—the transition from a weakly-interacting Bose condensate (BEC regime) to a strongly-paired fermionic superfluid (BCS regime). Using the dynamical BCS model, the authors calculate the full Bogoliubov spectrum (not just the low-energy linear approximation) and obtain analytic expressions for sound velocity as a function of interaction strength. Key findings: (1) the collective mode (Bogoliubov-Anderson branch) exhibits near-linear dispersion near the unitarity point (infinite scattering length); (2) the sound velocity peaks at unitarity and depends sensitively on pairing; (3) the collective mode merges with the fermionic excitation continuum, shifting from phonon-like (BEC side) to pair-breaking character (BCS side); (4) the Landau critical velocity (above which superfluidity breaks down) reaches maximum near unitarity. The work provides a unified understanding of collective dynamics across the entire crossover, with implications for quantum simulations, gravitational analogies, and understanding superfluid-to-normal transitions.

---

## Historical Context

The BEC-BCS crossover is a remarkable phenomenon in ultracold atoms:

1. **Fermi gas experiments (1999-2003)**: Using laser cooling of fermionic atoms (lithium-6, potassium-40), physicists realized degenerate Fermi gases and tuned interactions via Feshbach resonances. This allowed controlled variation of the scattering length $a_{ss}$ from negative (repulsive, BEC regime) through zero to positive (attractive, BCS regime).

2. **Superfluidity across crossover (2003)**: Multiple groups (MIT, Chicago, others) demonstrated that the Fermi gas becomes superfluid throughout the crossover, not just in the BCS regime. This was surprising—a Bose gas of tightly bound pairs should be superfluid (obvious), but a weakly-paired BCS gas exhibiting superfluidity with similar properties suggested a universal phenomenon.

3. **Unitarity regime (2004-2005)**: At infinite scattering length $|a_{ss}| \to \infty$, the system becomes "unitary"—the Fermi energy is the only scale. This produces remarkable universal properties independent of microscopic details (mass, interaction strength). The unitary Fermi gas became a focal point for testing universal scaling laws.

4. **Collective excitations and sound (2005-2006)**: This period saw detailed theoretical investigations of how collective excitations (sound modes, Bogoliubov branches) evolve across the crossover. Combescot et al.'s work synthesized these developments into a comprehensive theory.

The Combescot-Kagan-Stringari paper represents the state-of-the-art understanding of crossover physics circa 2006.

---

## Key Arguments and Derivations

### BEC-BCS Crossover Parametrization

The system is parametrized by the dimensionless interaction parameter:

$$\frac{k_F |a_{ss}|}{1}$$

or equivalently, the "crossover parameter":

$$\frac{1}{k_F a_{ss}}$$

where $k_F$ is the Fermi wavevector and $a_{ss}$ is the s-wave scattering length. The regimes are:

- **BEC limit**: $k_F a_{ss} \to 0^-$ (negative, shallow potential)—bound molecules dominate
- **Unitarity**: $k_F a_{ss} \to \pm \infty$ (infinite scattering length)—no microscopic scale
- **BCS limit**: $k_F a_{ss} \to 0^+$ (positive, weak pairing)—Cooper pairs form in the Fermi sea

The BCS gap in this notation is:

$$\Delta(k_F a_{ss}) = E_F \times f(k_F a_{ss})$$

where $f$ is a universal function. At unitarity ($|1/(k_F a_{ss})| \to 0$), the gap is proportional to the Fermi energy with a universal constant.

### Bogoliubov-de Gennes Equations

Quasiparticles in a superfluid are described by the Bogoliubov-de Gennes (BdG) equations:

$$\begin{pmatrix} \hat{H}_0 - \mu & \Delta(\mathbf{r}) \\ \Delta^*(\mathbf{r}) & -\hat{H}_0^* + \mu \end{pmatrix} \begin{pmatrix} u(\mathbf{r}) \\ v(\mathbf{r}) \end{pmatrix} = E \begin{pmatrix} u(\mathbf{r}) \\ v(\mathbf{r}) \end{pmatrix}$$

where:
- $\hat{H}_0 = -\nabla^2/(2m) - \mu$ is the single-particle kinetic energy
- $\Delta(\mathbf{r})$ is the pairing gap (order parameter)
- $u(\mathbf{r}), v(\mathbf{r})$ are the particle and hole components of the quasiparticle wave function
- $E$ is the quasiparticle energy

In a uniform system, solutions are Bloch waves:

$$u(\mathbf{r}) = u_\mathbf{k} e^{i\mathbf{k}\cdot\mathbf{r}}, \quad v(\mathbf{r}) = v_\mathbf{k} e^{i\mathbf{k}\cdot\mathbf{r}}$$

The spectrum is:

$$E_\mathbf{k}^\pm = \pm \sqrt{(\epsilon_\mathbf{k} - \mu)^2 + \Delta^2}$$

for positive and negative branches. The "+" branch (particle-like) disperses as the excitation momentum $\mathbf{k}$ is varied.

### Collective Modes and Lindhard Dielectric Function

Collective excitations (sound modes) arise when the mean-field gap $\Delta$ self-consistently responds to density oscillations. The response is governed by the Lindhard dielectric function:

$$\chi(\mathbf{q}, \omega) = \sum_{\mathbf{k}, n, n'} \frac{f_n(\mathbf{k}) - f_{n'}(\mathbf{k+q})}{E_{\mathbf{k}+\mathbf{q}}^{n'} - E_{\mathbf{k}}^n - \omega - i0^+}$$

where $f_n(\mathbf{k})$ is the occupation of state $\mathbf{k}$ in band $n$. Collective modes occur where the response function has poles, corresponding to zero of the Lindhard determinant:

$$\det[\hat{1} + V \chi(\mathbf{q}, \omega)] = 0$$

where $V$ is the interaction vertex.

For a uniform superfluid, this yields the Bogoliubov dispersion relation. In the long-wavelength limit ($\mathbf{q} \to 0$), the spectrum becomes:

$$\omega(q) = \sqrt{c^2 q^2 + \text{gap-related terms}}$$

where $c$ is the sound velocity:

$$c = \frac{\partial \omega}{\partial q} \bigg|_{q=0}$$

### Sound Velocity in the Crossover

Combescot et al. calculate the sound velocity as a function of crossover parameter using hydrodynamic and BCS theory:

$$c(k_F a_{ss}) = c_F \times f(k_F a_{ss})$$

where $c_F = \hbar k_F / m$ is the Fermi velocity (an intrinsic scale) and $f$ is a universal crossover function. Numerically:

- **BEC limit** ($k_F a_{ss} \to 0^-$): $c \approx \sqrt{2} c_F / \sqrt{2N}$ (low, sound in dilute gas of molecules)
- **Unitarity** ($1/(k_F a_{ss}) \approx 0$): $c \approx 0.4 c_F$ (intermediate)
- **BCS limit** ($k_F a_{ss} \to 0^+$): $c \approx c_F / \sqrt{3}$ (moderate, suppressed by pairing)

The remarkable result: the sound velocity is **continuous** across the crossover, with a maximum near unitarity. This reflects the universal nature of the unitary Fermi gas.

### Landau Critical Velocity

Superfluidity breaks down when the Landau critical velocity is exceeded. A quasiparticle moving with velocity $v$ through the superfluid creates a wake (Cherenkov radiation) if $v > c$ (speed exceeds sound speed). The critical velocity is the minimum speed at which this becomes possible:

$$v_c = \min_q \frac{\omega(q)}{q}$$

In the BCS limit, $v_c \approx c_F \Delta / E_F$ (small, since $\Delta \ll E_F$). In the BEC limit, $v_c \approx c_F$ (order unity). At unitarity, Combescot et al. find:

$$v_c \approx 0.5 c_F$$

This maximum value at unitarity explains why the unitary Fermi gas has the longest-lived superfluidity: the critical velocity is maximal, allowing the largest flow velocities before breakdown.

---

## Key Results

1. **Universal sound velocity at unitarity**: The collective mode at unitarity has sound velocity $c \approx 0.4 c_F$, independent of microscopic details. This universality reflects the scale-invariant nature of the infinite-scattering-length regime.

2. **Continuous spectrum across crossover**: The Bogoliubov spectrum smoothly transitions from Bogoliubov-phonon-like (BEC side) to pair-breaking-like (BCS side), with no singularity at the crossover point. Collective modes remain well-defined throughout.

3. **Landau critical velocity maximized at unitarity**: The critical velocity peaks at $v_c \approx 0.5 c_F$ near unitarity, larger than either the BEC or BCS limit. This explains enhanced robustness of the unitary Fermi gas superfluid.

4. **Mode-continuum merging**: The collective mode merges with the fermionic excitation continuum as momentum increases. On the BEC side, the mode is clearly separated (phononic); on the BCS side, it broadens (pair-breaking decay opens at lower energy).

5. **Gap evolution across crossover**: The pairing gap transitions from molecular binding energy (~2× scattering length interaction) to BCS pairing energy (exponential in $1/(k_F a_{ss})$). The maximum gap occurs near unitarity.

6. **Hydrodynamic relation**: The sound velocity satisfies the hydrodynamic relation:

$$c^2 = \frac{\partial P}{\partial n} \bigg|_S$$

(derivative of pressure with respect to density at fixed entropy), confirming that collective modes are true hydrodynamic phonons, not artifacts of the theory.

---

## Impact and Legacy

This work has been highly influential in ultracold atom physics:

1. **Experimental verification**: Subsequent measurements of collective mode frequencies in trapped Fermi gases confirmed Combescot et al.'s predictions for sound velocity and mode structure across the crossover.

2. **Universal scaling**: The discovery of universal properties at unitarity (maximum critical velocity, specific heat ratios, etc.) spawned a subfield of "unitary Fermi gas physics." The universality allowed precision tests of quantum statistics and thermodynamics.

3. **Quantum simulations**: The BEC-BCS crossover became a testbed for simulating other quantum systems. Fermi gases with tunable interactions can mimic condensed matter (high-temperature superconductors) and nuclear (neutron star crusts) systems.

4. **Connections to strong-coupling phenomena**: The crossover illustrates how quantum systems transition between weak-coupling and strong-coupling regimes. This has implications for understanding superconductivity, nuclear superfluidity, and quark-gluon plasmas.

5. **Transport and hydrodynamics**: Understanding collective modes is essential for computing transport coefficients (viscosity, thermal conductivity) in quantum fluids. The work provided tools for this.

6. **Gravitational analogies**: The hydrodynamic structure of the crossover resonates with emergent spacetime ideas (Jacobson, Volovik). A Fermi gas at unitarity exhibits universal properties analogous to critical phenomena in gravity.

---

## Connection to Phonon-Exflation Framework

**Relevance: PHONON DYNAMICS AT THE K_7 PAIRING THRESHOLD**

The Combescot-Kagan-Stringari work on BEC-BCS crossover sound velocity provides crucial insights for the K_7 pairing dynamics in phonon-exflation:

1. **K_7 as a BEC-BCS crossover system**: The framework proposes that the K_7 compactification undergoes a BCS pairing instability (Sessions 22-35 explored the landscape; Sessions 35-38 confirmed instability and computed the BCS gap). The K_7 system is analogous to a trapped Fermi gas being driven from weak-coupling (high $\tau$) to strong-coupling (low $\tau$, where BCS condensate forms).

2. **Sound velocity as a cosmological observable**: In the framework, the collective mode sound velocity on K_7 should determine the propagation speed of density fluctuations (phonon excitations) in the condensate. Cosmologically, this could affect:
   - Structure formation timescales (how fast perturbations grow)
   - Gravitational wave speeds in the compact dimension
   - Particle production rates during the transit (Sessions 37-38)

Combescot et al.'s result that sound velocity is continuous and maximized at unitarity suggests that the K_7 condensate sound velocity should also be robust and continuous as $\tau$ evolves.

3. **Critical velocity and particle stability**: The Landau critical velocity determines when superfluidity breaks down. In K_7, the analogous critical velocity would define the maximum "flow velocity" (rate of change of order parameter) that maintains coherence. If the geometric transit occurs with $d\tau/dt$ exceeding the K_7 critical velocity, the condensate destabilizes—a mechanism for the "sudden quench" observed in Session 38.

4. **Bogoliubov spectrum and phonon excitations**: SM particles in phonon-exflation are phonons (collective excitations of K_7). The Bogoliubov spectrum calculated by Combescot et al. for a uniform Fermi superfluid should be paralleled by the K_7 phonon spectrum. The paper's finding that collective modes merge with fermionic continuum is particularly relevant: as the transit proceeds and the condensate evolves, single-particle excitations (unpaired fermions) and collective modes (phonons) have different energies. Their interaction/merging determines the final state (Sessions 37-38).

5. **Universality at the pairing threshold**: Just as the unitary Fermi gas exhibits universal properties, the K_7 system at the BCS instability threshold (unitarity analog) should also exhibit universality. This means certain observables (SM coupling constants, particle mass ratios) should be determined by dimensional analysis and topology alone, independent of microscopic compactification details—a testable prediction.

6. **Gap and sound velocity relation**: Combescot et al. show that the BCS gap and sound velocity are intimately related (both depend on interaction strength and density). In the framework, the K_7 gap $\Delta(\tau) = 0.115$ (Session 35) and the K_7 sound velocity should obey a similar relationship:

$$\Delta \propto c^2 \times (\text{pairing strength})$$

This could be used to compute $\Delta$ from other known quantities (Fermi surface area, sound velocity) without solving the full BCS equation—a computational shortcut.

7. **Hydrodynamic limit and 4D emergence**: The crossover physics becomes hydrodynamic (phonon-dominated) in the BEC regime. In phonon-exflation, the 4D cosmological dynamics (Friedmann equations) should emerge from the hydrodynamic limit of K_7 phonons. The paper's hydrodynamic relations ($c^2 = \partial P / \partial n$, etc.) provide tools for deriving 4D hydrodynamics from 5D+1 (M4 x K_7) compactified dynamics.

8. **Excitation spectrum and observable particles**: The Bogoliubov spectrum's structure (phonon branch vs. pair-breaking continuum) determines which excitations are "stable" (long-lived) vs. "unstable" (quick to decay). In the framework, this determines which SM particles are long-lived (electrons, quarks, stable under the weak force) vs. rare/inaccessible (top quark, Higgs unstable without mass parameters). The topology of the K_7 Bogoliubov spectrum encodes SM particle stability.

**Specific prediction**: If the K_7 condensate sound velocity has a maximum near the critical point (analogous to unitarity for Fermi gases), then the transit dynamics should exhibit special smoothness or symmetry near this point—a "phase transition" in the effective $\tau$ dynamics. Session 38 found that the instanton gas properties cluster around $S_{\text{inst}} \approx 0.069$ with near-critical fluctuations; this may be the K_7 analog of unitarity.

