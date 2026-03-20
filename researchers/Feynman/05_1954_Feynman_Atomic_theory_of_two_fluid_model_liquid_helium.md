# Atomic Theory of the Two-Fluid Model of Liquid Helium

**Author:** Richard P. Feynman
**Year:** 1954
**Journal:** *Physical Review*, 94(2), 262--277

---

## Abstract

Feynman applies the path integral formulation of quantum mechanics to derive the macroscopic properties of liquid helium-4 from its microscopic atomic physics. He demonstrates that the superfluid behavior of helium below the lambda transition temperature ($T_\lambda \approx 2.17$ K) can be understood as a consequence of Bose-Einstein statistics and the indistinguishability of helium atoms in the path integral: permutation cycles of atomic worldlines, which would be suppressed by the hard-core repulsion in a classical fluid, become important at low temperatures due to quantum coherence. The excitation spectrum of the superfluid is derived from variational wave functions, yielding the phonon-roton spectrum that Landau had postulated phenomenologically. Feynman shows that the critical velocity for superfluid breakdown corresponds to the minimum of $\epsilon(p)/p$ (the Landau criterion), occurring at the roton minimum, and provides a microscopic basis for the two-fluid model in which the normal component arises from thermal excitation of phonons and rotons.

---

## Historical Context

### The Helium Problem

Liquid helium-4 undergoes a phase transition at $T_\lambda = 2.172$ K from an ordinary fluid (He I) to a superfluid (He II) with remarkable properties: zero viscosity for flow through narrow channels, quantized circulation, a fountain effect, and second sound (temperature waves). These phenomena were discovered experimentally by Kapitza and by Allen and Misener in 1938.

### Landau's Phenomenological Theory

Landau proposed in 1941 that the superfluid could be described by a two-fluid model: a superfluid component (carrying no entropy, flowing without friction) and a normal component (carrying all the entropy, behaving as an ordinary viscous fluid). The normal component was identified with thermally excited quasiparticles. Landau postulated an excitation spectrum $\epsilon(p)$ with a linear (phonon) region at small momenta and a minimum (roton) at finite momentum:

$$\epsilon(p) = \begin{cases} c_s p & \text{(phonons, small } p\text{)} \\ \Delta + \frac{(p - p_0)^2}{2\mu} & \text{(rotons, near } p_0\text{)} \end{cases}$$

where $c_s$ is the speed of sound, $\Delta$ is the roton energy gap, $p_0$ is the roton momentum, and $\mu$ is an effective mass. This spectrum was confirmed by neutron scattering experiments (Henshaw and Woods, 1961), but Landau did not derive it from first principles.

### The London-Tisza Picture

An alternative approach, due to London (1938) and Tisza (1938), attributed superfluidity to Bose-Einstein condensation (BEC). In an ideal Bose gas, a macroscopic fraction of particles condenses into the zero-momentum state below a critical temperature. London argued that the superfluid component of helium was analogous to this condensate. The difficulty was that liquid helium is strongly interacting (not an ideal gas), and the connection between BEC and superfluidity was not rigorous.

### Feynman's Approach

Feynman's contribution was to bridge the gap between the microscopic (atomic) and macroscopic (two-fluid) descriptions using the path integral. His approach was neither pure BEC (London-Tisza) nor pure phenomenology (Landau), but a first-principles derivation that encompassed both perspectives.

---

## Key Arguments and Derivations

### 1. Path Integral for the Partition Function

For a system of $N$ identical bosons at temperature $T = 1/k_B\beta$, the partition function is:

$$Z = \frac{1}{N!}\sum_P \int \prod_{i=1}^N d\mathbf{r}_i \, \rho(\mathbf{r}_1, \ldots, \mathbf{r}_N; \mathbf{r}_{P(1)}, \ldots, \mathbf{r}_{P(N)}; \beta)$$

where the sum is over all permutations $P$ of the $N$ particles (Bose statistics requires symmetrization), and $\rho$ is the density matrix, expressed as a Euclidean path integral:

$$\rho(\mathbf{R}; \mathbf{R}'; \beta) = \int \mathcal{D}[\mathbf{R}(\tau)] \exp\left(-\frac{1}{\hbar}\int_0^{\hbar\beta} \left[\sum_i \frac{m}{2}\dot{\mathbf{r}}_i^2 + V(\mathbf{R}(\tau))\right] d\tau\right)$$

with boundary conditions $\mathbf{R}(0) = \mathbf{R}'$ and $\mathbf{R}(\hbar\beta) = \mathbf{R}$.

The key insight is that each permutation $P$ corresponds to a specific topology of the particle worldlines in imaginary time: particle $i$ at $\tau = 0$ connects to particle $P(i)$ at $\tau = \hbar\beta$. The identity permutation gives worldlines that close on themselves; non-trivial permutations create cycles where worldlines link through each other.

### 2. Permutation Cycles and the Lambda Transition

Feynman argues that at high temperatures, the dominant contributions come from short worldlines (small thermal wavelength $\lambda_T = \sqrt{2\pi\hbar^2/mk_BT}$), and the hard-core repulsion between helium atoms ($\sigma \approx 2.6$ A) prevents worldlines from overlapping enough to permute. Only the identity permutation contributes significantly, and the system behaves classically.

As the temperature decreases, $\lambda_T$ grows. When $\lambda_T$ becomes comparable to the interparticle spacing $d \approx 3.6$ A, the worldlines of neighboring atoms begin to overlap, and permutation cycles of length $\ell > 1$ contribute appreciably. Feynman estimates the transition temperature from:

$$\lambda_T \sim d \implies T_\lambda \sim \frac{2\pi\hbar^2}{mk_B d^2}$$

Plugging in $m = 4$ amu and $d = 3.6$ A gives $T_\lambda \approx 3.1$ K, in reasonable agreement with the experimental 2.17 K. The discrepancy is due to the strong interactions, which reduce the effective overlap.

The lambda transition is identified with the onset of macroscopic permutation cycles -- cycles that span the entire system. Below $T_\lambda$, a finite fraction of atoms participate in a single permutation cycle of length $\sim N$, which is the path-integral signature of Bose-Einstein condensation. The superfluid fraction is identified with the fraction of atoms in these macroscopic cycles.

### 3. Excitation Spectrum: Variational Approach

To derive the excitation spectrum, Feynman constructs variational wave functions for the excited states of the superfluid. The ground state is $\Phi_0(\mathbf{r}_1, \ldots, \mathbf{r}_N)$, and Feynman proposes that the lowest-lying excited states have the form:

$$\Phi_\mathbf{k} = \rho_\mathbf{k} \, \Phi_0$$

where $\rho_\mathbf{k}$ is the Fourier component of the density:

$$\rho_\mathbf{k} = \sum_{j=1}^N e^{i\mathbf{k}\cdot\mathbf{r}_j}$$

This ansatz has a clear physical interpretation: the excitation is a density fluctuation with wavevector $\mathbf{k}$, created on top of the correlated ground state.

The variational energy is:

$$\epsilon(k) = \frac{\langle \Phi_\mathbf{k} | H | \Phi_\mathbf{k} \rangle}{\langle \Phi_\mathbf{k} | \Phi_\mathbf{k} \rangle} - E_0$$

The numerator involves the commutator $[H, \rho_\mathbf{k}]$, which for a system with kinetic energy $T = -\frac{\hbar^2}{2m}\sum_i \nabla_i^2$ gives:

$$[T, \rho_\mathbf{k}] = \frac{\hbar^2 k^2}{2m}\rho_\mathbf{k} + \frac{\hbar^2}{m}\sum_j e^{i\mathbf{k}\cdot\mathbf{r}_j} (i\mathbf{k}\cdot\nabla_j)$$

After algebra, the excitation energy simplifies to:

$$\epsilon(k) = \frac{\hbar^2 k^2}{2mS(k)}$$

where $S(k) = \langle \rho_\mathbf{k}\rho_{-\mathbf{k}} \rangle / N$ is the static structure factor of the liquid, measurable by X-ray or neutron scattering.

### 4. The Phonon-Roton Spectrum

The structure factor $S(k)$ of liquid helium has been measured experimentally:

- At small $k$: $S(k) \to \hbar k / (2mc_s)$ (compressibility sum rule), giving $\epsilon(k) \to \hbar c_s k$ -- **phonons** (sound waves).
- At intermediate $k$: $S(k)$ has a pronounced peak near $k_0 \approx 2\pi/d \approx 1.9$ A$^{-1}$ due to the short-range order in the liquid. This peak causes a **minimum** in $\epsilon(k)$ -- the **roton minimum**.
- At large $k$: $S(k) \to 1$, giving $\epsilon(k) \to \hbar^2 k^2 / 2m$ -- free-particle behavior.

Feynman's formula $\epsilon(k) = \hbar^2 k^2 / (2mS(k))$ thus naturally produces the phonon-roton spectrum without any adjustable parameters, using only the measured $S(k)$. The roton gap comes from the peak in $S(k)$, which itself arises from the hard-core repulsion between helium atoms at short distances.

Quantitatively, Feynman's variational estimate gives the roton gap $\Delta/k_B \approx 11.5$ K, compared to the experimental value of $8.65$ K. The overestimate is expected because the variational ansatz $\rho_\mathbf{k}\Phi_0$ does not capture multi-phonon processes (backflow corrections). Feynman and Cohen (1956) later improved the ansatz by including backflow:

$$\Phi_\mathbf{k}^{\text{BF}} = \sum_j e^{i\mathbf{k}\cdot\mathbf{r}_j}\left(1 + \sum_{l \neq j} f(r_{jl})\hat{\mathbf{k}}\cdot\hat{\mathbf{r}}_{jl}\right)\Phi_0$$

which reduces the roton gap to $\Delta/k_B \approx 9.6$ K.

### 5. The Landau Critical Velocity

Feynman derives the Landau criterion for superfluidity from energy-momentum conservation. If the superfluid flows through a tube with velocity $v_s$, it can lose kinetic energy by creating an excitation with energy $\epsilon(p)$ and momentum $p$. The excitation is energetically favorable only if:

$$\epsilon(p) - v_s p < 0 \implies v_s > \frac{\epsilon(p)}{p}$$

The critical velocity is therefore:

$$v_c = \min_p \frac{\epsilon(p)}{p}$$

For the phonon-roton spectrum, the minimum of $\epsilon(p)/p$ occurs at the roton minimum:

$$v_c = \frac{\Delta}{p_0} \approx \frac{8.65 \text{ K} \cdot k_B}{1.9 \text{ A}^{-1} \cdot \hbar} \approx 58 \text{ m/s}$$

This is much smaller than the speed of sound ($c_s \approx 238$ m/s) because the roton minimum provides a low-energy pathway for dissipation.

### 6. Quantized Vortices

Feynman argues that the superfluid velocity field $\mathbf{v}_s$ is irrotational ($\nabla \times \mathbf{v}_s = 0$) because the condensate wave function has a well-defined phase $\theta$:

$$\mathbf{v}_s = \frac{\hbar}{m}\nabla\theta$$

Circulation is quantized:

$$\oint \mathbf{v}_s \cdot d\mathbf{l} = \frac{h}{m}n, \quad n \in \mathbb{Z}$$

Feynman proposes that vortex lines (one-dimensional singularities where $\theta$ winds by $2\pi$) are the mechanism by which the superfluid acquires angular momentum. The core of a vortex line has a radius of order the healing length $\xi$, inside which the superfluid density vanishes. The energy per unit length of a vortex line is:

$$\frac{E}{L} = \frac{\pi\rho_s \hbar^2}{m^2}\ln\frac{R}{\xi}$$

where $R$ is the container size.

---

## Physical Interpretation

### Superfluidity as Topological Order

Feynman's path-integral picture reveals superfluidity as a fundamentally topological phenomenon. The superfluid state is characterized by macroscopic permutation cycles -- worldlines that wind through the entire system. These cycles cannot be unwound continuously; destroying superfluidity requires breaking the cycles, which costs a macroscopic amount of energy. This is the prototype for all subsequent understanding of topological order in condensed matter physics.

### The Phonon-Roton Duality

The excitation spectrum reveals a deep connection between collective (phonon) and single-particle (roton) physics. At long wavelengths, the excitations are sound waves -- collective density oscillations. At short wavelengths (near $k_0$), the excitations are localized disturbances of the atomic arrangements -- quasi-particles. The smooth interpolation between these regimes, captured by $\epsilon(k) = \hbar^2 k^2/(2mS(k))$, shows that phonons and rotons are the same type of excitation at different wavelengths.

### Why Helium-3 is Not Superfluid at 2 K

Feynman's argument makes clear why $^3$He (a fermion) does not become superfluid at the same temperature as $^4$He: the Fermi statistics require anti-symmetrization rather than symmetrization of the worldlines, and the sign alternation suppresses rather than enhances the long permutation cycles. $^3$He does become superfluid, but only below 2.5 mK, via Cooper pairing into bosonic pairs.

---

## Impact and Legacy

### Quantized Vortices

Feynman's prediction of quantized vortex lines was confirmed experimentally by Vinen (1961) through measurements of the vibration frequency of a wire in rotating He II. The study of quantized vortices became a major subfield, with connections to:
- Rotating neutron stars (pulsars)
- Type-II superconductors (Abrikosov vortex lattice)
- Bose-Einstein condensates in cold atomic gases
- Cosmological defects (cosmic strings)

### Path Integral Monte Carlo

Feynman's expression for the partition function as a sum over permutation cycles is the theoretical basis for path integral Monte Carlo (PIMC) simulations, developed by Ceperley and Pollock (1986). PIMC provides essentially exact results for the thermodynamic properties of superfluid helium and is now a standard computational tool for quantum fluids and solids.

### Superfluidity and Superconductivity

The conceptual framework -- macroscopic coherence, quantized circulation, order parameter, excitation spectrum -- applies with modifications to all superfluids and superconductors. The Ginzburg-Landau and BCS theories of superconductivity share the same deep structure: a macroscopic wave function with a well-defined phase, whose topological properties determine the superfluid/superconducting behavior.

---

## Connections to Modern Physics

1. **Cold atom BEC:** The experimental achievement of BEC in dilute atomic gases (Cornell, Wieman, Ketterle, 1995) provided a controlled system for studying superfluidity. The phonon-roton spectrum, quantized vortices, and the critical velocity -- all predicted by Feynman for helium -- have been observed in these systems.

2. **Gross-Pitaevskii equation:** The mean-field description of a weakly interacting BEC via the GPE:
$$i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi + g|\psi|^2\psi$$
is the natural extension of Feynman's approach to weakly interacting systems, where the condensate wave function $\psi$ plays the role of the superfluid order parameter.

3. **Phonon-exflation connection:** The identification of elementary excitations as collective modes (phonons/rotons) of an underlying condensate is the direct analog of the phonon-exflation hypothesis, where Standard Model particles are identified as phononic excitations of a higher-dimensional condensate. Feynman's derivation of the excitation spectrum from $S(k)$ demonstrates that the detailed properties of "particles" can emerge from the structure factor of the underlying medium.

4. **Quantum turbulence:** The study of tangled vortex lines in superfluids (quantum turbulence) is an active research area connecting superfluidity to classical turbulence, cosmological phase transitions, and quantum information. Feynman's original paper initiated this entire direction.

5. **Topological phases:** The modern understanding of topological phases of matter (topological insulators, topological superconductors) descends from the realization that quantum ground states can be characterized by topological invariants, an idea first encountered in the context of superfluid helium's quantized vortices.
