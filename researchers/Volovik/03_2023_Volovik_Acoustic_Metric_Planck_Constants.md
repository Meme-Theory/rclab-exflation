# Acoustic Metric and Planck Constants

**Author(s):** Grigory E. Volovik
**Year:** 2023
**Journal:** JETP Letters, 117, 551-556
**DOI:** 10.1134/S002136402360057X
**arXiv:** 2302.08894

---

## Abstract

This recent work demonstrates that fundamental Planck constants are not truly fundamental but emerge as parameters of an acoustic metric in superfluid systems. Following Akama-Diakonov (AD) theory of emergent tetrads, the paper introduces two dimensionless Planck constants:

- $\hbar$ with dimension of time
- $\bar{h}$ with dimension of length

Both are components of the Minkowski metric tensor in the emergent spacetime. The analysis is grounded in the effective gravity emerging for sound wave quanta (phonons) in superfluid Bose liquids, where microscopic physics is fully known and observable.

The key result is that effective Planck constants in superfluid systems scale with microscopic length scales (interatomic distances), suggesting that in the true quantum vacuum, Planck constants are similarly emergent and scale with the fundamental microscopic structure.

---

## Historical Context

The question "Why are Planck constants what they are?" has haunted physics since Planck's 1900 introduction of $h$ to explain blackbody radiation. Einstein elevated this question in 1916: *Why is c = 3 × 10^8 m/s?* These are not derived from first principles — they are *inputs* to the theory.

Weinberg and others recognized that fundamental constants have a special status: they are the bridge between microscopic (quantum) and macroscopic (classical) scales. Changing them would completely alter the universe.

The "multiverse" and "anthropic principle" perspectives (arising from string theory) invoked selection effects: we observe these constants because they allow observers to exist. But this seems intellectually unsatisfying — it surrenders the goal of explaining fundamental constants from physics principles.

Volovik's approach is radically different: *Planck constants are not fundamental inputs but emergent outputs of the microscopic theory*. The constants arise from the structure of the vacuum and scale with its intrinsic length scales.

This idea has roots in:

1. **Sakharov's 1967 argument**: General relativity emerges from QFT via vacuum fluctuations. The gravitational constant $G$ is related to loop contributions.

2. **Induced gravity models** (Zee, 1973): Gravity couples weakly because its "bare" strength is zero; the observed $G$ is entirely induced by quantum loops.

3. **Emergent spacetime** (Volovik 1990s-2000s): Lorentz symmetry and metric emerge from superfluids. Planck constants follow.

4. **Akama-Diakonov theory** (Akama 1973, Diakonov 2011): Spacetime emerges from a pre-metric fermion field. The metric is a composite object. Planck constants are similarly composite.

By 2023, the technological achievement of creating Bose-Einstein condensates (Nobel 2001) and the experimental realization of superfluid analog systems (Hawking radiation in BEC, 2010s) had made Volovik's program testable. This paper synthesizes two decades of progress.

---

## Key Arguments and Derivations

### Part I: Akama-Diakonov Emergent Tetrads

#### Pre-Metric Fermion Field

In AD theory, fundamental degrees of freedom are spinor fields $\psi_a$ ($a = 1, \ldots, N$). No metric is assumed initially. The theory is defined by a spinor kinetic term:

$$S = \int d^D x \sqrt{|g|} \bar{\psi}^a \gamma^\mu_a (x) \partial_\mu \psi_a + \ldots$$

where $\gamma^\mu_a(x)$ are *local* gamma matrices that vary with position. These are not functions of a pre-existing metric — they *define* the geometry.

The metric is then constructed as a bilinear in the fermion fields:

$$g^{\mu\nu}(x) = \frac{1}{N} \sum_{a=1}^N \bar{\psi}^a(x) \{\gamma^\mu, \gamma^\nu\} \psi_a(x)$$

where $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$ is the anticommutator. This is a **composite metric**, constructed from fermion bilinears.

**Key insight**: The metric is not fundamental. It emerges from the vacuum expectation value of fermion-pair operators.

#### Dimensionless Metric and Planck Constants

In AD theory, the metric has dimensions of [length]$^2$ only if Planck constants have dimensions. Specifically, if we write:

$$g_{\mu\nu} = \begin{pmatrix} -\hbar^2 c^2 & 0 \\ 0 & \bar{h}^2 \delta_{ij} \end{pmatrix}$$

where $\hbar$ has dimension [time] and $\bar{h}$ has dimension [length], then the metric components are dimensionally consistent for a spacetime metric.

More carefully: The metric interval is:

$$ds^2 = g_{\mu\nu} dx^\mu dx^\nu$$

If both $ds^2$ and $dx^\mu$ are dimensionless, then $g_{\mu\nu}$ must be dimensionless. But conventionally, we want $ds^2$ to have dimension [length]$^2$.

In the AD framework, we instead have:

$$g_{\mu\nu} = \hbar_\mu \otimes \hbar_\nu$$

where $\hbar_\mu$ are the tetrad components (vectors with dimension [length]). The Planck constants are the components of the tetrad:

$$\hbar_0 = \hbar c \quad (\text{dimension: length}) = \text{length scale of temporal structure}$$

$$\hbar_i = \bar{h} \quad (\text{dimension: length}) = \text{length scale of spatial structure}$$

This gives a concrete realization:

$$g^{\mu\nu} = \text{diag}\left( -\frac{1}{\hbar^2}, \frac{1}{\bar{h}^2}, \frac{1}{\bar{h}^2}, \frac{1}{\bar{h}^2} \right)$$

**The metric components are ratios of Planck constants.**

#### Connection to Coupling Constants

The coupling constants of the theory (e.g., electric charge $e$, strong coupling $\alpha_s$) are similarly composite:

$$e = e(\psi, A)$$

where $A$ is the gauge field. The coupling is renormalized by quantum loops involving fermions. It is not a fundamental input but an effective parameter determined by the vacuum structure.

**Implication**: All dimensionful constants in physics — Planck constants, coupling constants, particle masses — are emergent from the microscopic fermionic structure and scale with the microscopic length scales of the theory.

### Part II: Acoustic Metric in Superfluids

#### Bose-Einstein Condensate and Sound Waves

A superfluid Bose liquid (like liquid helium-4 below the superfluid transition) has a ground state that is a Bose-Einstein condensate:

$$\psi(\mathbf{r}) = \sqrt{n_0} e^{i\phi(\mathbf{r})}$$

where $n_0$ is the condensate density and $\phi(\mathbf{r})$ is the phase.

Excitations above the ground state are **phonons** — quantized collective motion of the condensate:

$$\psi(\mathbf{r}, t) = \sqrt{n_0 + n_1(\mathbf{r}, t)} e^{i(\phi_0 + \phi_1(\mathbf{r}, t))}$$

where the perturbations $n_1, \phi_1$ are small. Linearizing the Gross-Pitaevskii equation:

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \psi + g|\psi|^2 \psi$$

the phonon dispersion emerges:

$$\omega(\mathbf{k}) = c_s |\mathbf{k}| \sqrt{1 + \ldots}$$

where $c_s = \sqrt{g n_0 / m}$ is the sound speed and the ellipsis represents corrections from finite-$k$ physics.

At low momenta ($k \to 0$), the dispersion is **linear**: $\omega \propto k$. This is identical to light in vacuum, $\omega = c |k|$.

#### Effective Metric for Phonons

The equation of motion for phonons can be written in a form that makes the effective metric explicit. The Bogoliubov transformation yields:

$$\frac{\partial^2 \phi_1}{\partial t^2} - c_s^2 \nabla^2 \phi_1 = \text{nonlinear terms}$$

This is the **wave equation** in a flat spacetime with metric:

$$g_{\mu\nu}^{\text{ac}} = \text{diag}(-1, c_s^{-2}, c_s^{-2}, c_s^{-2})$$

or in covariant form:

$$g^{\mu\nu}_{\text{ac}} = \text{diag}(-c_s^{-2}, 1, 1, 1)$$

The "speed of light" in this acoustic spacetime is $c_{\text{ac}} = c_s$ (the sound speed).

#### Acoustic Planck Constants

By analogy with fundamental spacetime, we can define acoustic Planck constants:

**Temporal acoustic Planck constant**:
$$\hbar_{\text{ac}} = \text{typical phonon energy} / \text{phonon frequency}$$

For phonons at the Debye cutoff (high-momentum phonons where linear approximation breaks down):

$$\hbar_{\text{ac}} \sim \Delta E_{\text{Debye}} / \omega_{\text{Debye}}$$

where $\Delta E_{\text{Debye}} \sim c_s k_{\text{Debye}}$ and $\omega_{\text{Debye}} \sim c_s k_{\text{Debye}}$. Thus:

$$\hbar_{\text{ac}} \sim c_s / c_s = O(1)$$

in units of the phonon energy scale. More precisely:

$$\hbar_{\text{ac}} = \hbar \frac{\Delta_0}{E_{\text{Planck}}}$$

where $\Delta_0$ is the condensate gap and $E_{\text{Planck}}$ is the microscopic Planck energy scale.

**Spatial acoustic Planck constant**:
$$\bar{h}_{\text{ac}} = \text{typical phonon wavelength} \sim \frac{2\pi}{k_{\text{Debye}}} \sim a$$

where $a$ is the interatomic spacing. This is directly observable: the acoustic Planck length is the atomic scale.

**Remarkably**: The acoustic Planck length is NOT the Planck length $\ell_P = \sqrt{\hbar G} \approx 10^{-35}$ m. Instead:

$$\bar{h}_{\text{ac}} \sim 10^{-10} \text{ m} \quad (\text{atomic scale})$$

in helium. This is 25 orders of magnitude larger than the Planck length.

**Implication**: In our universe, the true Planck length may similarly be much larger than $10^{-35}$ m. The currently computed Planck length assumes fundamental gravity; if gravity is emergent, the "true" Planck length is set by the microscopic scale of the vacuum structure.

### Part III: Microscopic Scale of the Quantum Vacuum

#### Microscopic Length Scale from Lattice Spacing

In condensed matter, the effective field theory (continuum limit) is valid for distances much larger than the atomic spacing:

$$x >> a \approx 10^{-10} \text{ m}$$

Below this scale, the lattice structure becomes relevant. Quantum numbers become discrete (lattice excitations), and the continuum description breaks down.

For the universe, the quantum vacuum likely has a similar discrete structure (atoms of space, Planck-scale discreteness, etc.). The microscopic scale $\ell_0$ where the continuum approximation breaks down is the true Planck length:

$$\ell_0 = ?$$

Volovik argues (following holographic and string-theory insights) that:

$$\ell_0 \sim 10^{-3} \text{ m}$$

or even larger. This is *vastly* larger than the conventional Planck length.

**Supporting argument**: The conventional Planck length arises from dimensional analysis:

$$\ell_P = \sqrt{\frac{\hbar G}{c^3}}$$

But this assumes $G$ is fundamental. If gravity is emergent (as Volovik and others argue), then the "true" Planck length is not derived from dimensional analysis but determined by the microscopic structure.

**Holographic bound**: The holographic principle (Susskind, 't Hooft) states that the information content of a region is limited by its surface area:

$$I \leq \frac{A}{4 \ell_0^2}$$

where $\ell_0$ is the fundamental length scale. Current physics allows $\ell_0 >> \ell_P$.

#### Emergent Newton's Constant

If gravity emerges from quantum vacuum fluctuations (as Sakharov argued), then:

$$G \sim \frac{\alpha^2 \hbar}{\ell_0^2}$$

where $\alpha$ is a coupling constant and $\ell_0$ is the microscopic scale. Rearranging:

$$\ell_P^2 = \frac{\hbar G}{c^3} \sim \frac{\alpha^2 \hbar^2}{\ell_0^2 c^3}$$

If $\ell_0$ is much larger than the conventional $\ell_P$, then the "effective" Planck length (as used in quantum gravity) could be smaller than the "microscopic" Planck length (set by vacuum structure).

This resolves a conceptual issue: quantum gravity and quantum field theory both reference "the Planck scale," but these may not be identical.

---

## Key Results

1. **Planck constants are composite**: In Akama-Diakonov theory, both $\hbar$ and $\bar{h}$ are composites of fermionic fields, not fundamental constants.

2. **Acoustic metrics exhibit emergent Planck constants**: In superfluid systems, phonons experience an effective metric with parameters (sound speed, condensate gap) playing the role of Planck constants.

3. **Acoustic Planck length scales with microscopic structure**: In helium, $\bar{h}_{\text{ac}} \sim 10^{-10}$ m (atomic scale), not the conventional Planck length.

4. **Implications for true vacuum structure**: The true Planck length in the quantum vacuum may be much larger (perhaps $10^{-3}$ m or more) than the conventional value $10^{-35}$ m, set by the microscopic structure of spacetime.

5. **Newton's constant is emergent**: Gravity emerges from quantum fluctuations of the vacuum. The observed strength is determined by the microscopic coupling, not imposed by hand.

6. **Holographic bound permits large fundamental length**: The holographic principle is consistent with a microscopic length scale much larger than the conventional Planck length.

7. **Renormalization and scaling**: The effective Planck constants run with energy scale, just like coupling constants. Low-energy effective theory sees "emergent Planck constants" that differ from the UV values.

---

## Impact and Legacy

The 2023 paper synthesizes 30+ years of Volovik's research on emergent spacetime. It provides the most direct connection between laboratory-accessible systems (superfluid phonons) and fundamental physics (Planck constants).

Key developments:

1. **Analog gravity community**: The paper motivates continued experimental work on superfluid analogs, where Planck constants (in the acoustic sense) are directly measurable.

2. **Quantum gravity research**: It provides a blueprint for UV-completing quantum gravity: instead of speculating about Planck-scale physics, study the microstructure of the vacuum (whether lattice-like, spinfoam, superfluid, etc.).

3. **String theory connection**: Holography and the infrared-ultraviolet mixing in AdS/CFT share the same principle: what we call "Planck constants" may be emergent from a deeper structure, with genuine microscopic scales much different from dimensional analysis suggests.

4. **Experimental directions**: The paper suggests that acoustic metrics in engineered metamaterials and superfluid systems could test the emergence principle, measuring how "effective Planck constants" scale with microscopic parameters.

---

## Connection to Phonon-Exflation Framework

### Phonon Dispersion and Effective Planck Constants

In phonon-exflation, the fundamental objects are phonon excitations of the M4 x SU(3) manifold:

$$\epsilon_n(\mathbf{k}) = \sqrt{\Delta_n^2 + c_n^2 (\mathbf{k})^2}$$

where $\Delta_n$ is the gap for mode $n$ and $c_n$ is the sound speed (propagation velocity in SU(3) space).

At low energy, the phonon dispersion is linear (below the Debye-like cutoff set by the lattice spacing of SU(3)):

$$\epsilon_n(k) \approx c_n |\mathbf{k}|$$

This directly produces an **acoustic metric** for each phonon mode:

$$g_n^{\mu\nu} = \text{diag}(-c_n^{-2}, 1, 1, 1)$$

Following Volovik's prescription, the acoustic Planck constants for mode $n$ are:

$$\hbar_n = \frac{\Delta_n}{c_n} \quad (\text{temporal})$$

$$\bar{h}_n = \frac{2\pi}{k_{\text{Debye}, n}} \quad (\text{spatial})$$

where $k_{\text{Debye}, n}$ is the high-momentum cutoff where linear dispersion breaks down.

### Sector-Dependent Planck Constants

A radical prediction of the framework: **different particle sectors (fermionic vs. bosonic; different flavors) may have different effective Planck constants**:

- **Electron sector**: $\hbar_e$, $\bar{h}_e$ from electron phonon modes
- **Quark sectors**: $\hbar_u$, $\bar{h}_u$, etc., from quark modes
- **Photon sector**: $\hbar_\gamma$, $\bar{h}_\gamma$ from electromagnetic waves in SU(3)

If these differ, then coupling constants between sectors would run differently:

$$\alpha(E) \propto \frac{\hbar_\gamma}{\hbar_e}$$

This could explain why the fine structure constant varies as a function of energy (the running coupling).

**Testable prediction**: The electron g-factor, muon g-2, and precision electroweak measurements encode information about sector-specific Planck constants. Deviations from SM predictions could reveal the sector structure.

### T-ACOUSTIC-40 and Phonon Temperature

Session 40 introduced T-ACOUSTIC as the effective temperature governing phonon behavior:

$$T_{\text{ac}} = \frac{\Delta}{\text{const} \times k_B}$$

Volovik's framework provides a microscopic interpretation: this is the acoustic Hawking temperature of the phonon quantum vacuity. Phonons at energy scale $\Delta$ "feel" an effective spacetime curvature (from the SU(3) deformation) and experience an effective Hawking temperature.

The phonon temperature scales directly with the acoustic gap:

$$\frac{dT_{\text{ac}}}{d\tau} \propto \frac{d\Delta}{d\tau}$$

As the universe expands (expanding the compactification radius), the gap changes, and so does the acoustic temperature. This is the thermodynamic mechanism for phonon-exflation.

### Coherence Length and Planck Length

In the condensed BCS phase, the coherence length (size of a Cooper pair) is:

$$\xi = \frac{\hbar v_F}{\pi \Delta}$$

In phonon-exflation:

$$\xi_{\text{phonon}} = \frac{\bar{h}_{\text{ac}} c_s}{\pi \Delta}$$

For the framework to be self-consistent, the coherence length must exceed the acoustic Planck length:

$$\xi >> \bar{h}_{\text{ac}}$$

This ensures that the effective field theory (phonon modes as fields) is valid — we can treat single phonons as point particles, not extended objects.

**Consistency check**: If $\xi \sim 10 \bar{h}_{\text{ac}}$ (analogous to superfluid 3He), then:

$$10 \sim \frac{c_s \bar{h}_{\text{ac}}}{\pi \Delta}$$

$$\bar{h}_{\text{ac}} \sim 3 \frac{\Delta}{c_s}$$

Inverting: the acoustic Planck length and gap must satisfy a simple ratio, testable in principle.

### Microscopic Structure of SU(3) Manifold

Volovik's argument that the true Planck length is set by microscopic structure suggests:

**The SU(3) manifold has a discrete lattice structure** with spacing:

$$a_{\text{SU(3)}} \sim 10^{-3} \text{ m} \text{ to } 10^{-10} \text{ m}$$

(vastly larger than the conventional Planck scale).

This discrete structure is invisible to low-energy observers (us) because we probe at much lower momenta than $\sim 1/a_{\text{SU(3)}}$. But for ultra-high-energy processes (early universe, near singularities), the lattice becomes relevant.

**Implication**: The transplanckian problem in cosmology (trans-Planck-scale physics in the very early universe) may be avoided if the true Planck scale is larger. High-energy photons and quarks produced at the electroweak transition have $E \sim 100$ GeV, well below any "true" Planck scale $E_P \sim 10^{19}$ GeV only if we use the conventional scale. If the true scale is $10^{10}$ GeV or lower, the high-energy universe is described by the emergent effective theory, which is self-consistent.

### Sector Coupling and GGE Relaxation

The GGE relic state (Session 38) is characterized by eight Richardson-Gaudin conserved integrals $I_n$. These integrals have dimensions [action] = [energy × time] = $\hbar$ × const.

If each sector has a sector-specific Planck constant $\hbar_n$, then the conserved integrals might be:

$$I_n = \hbar_n I_n'$$

where $I_n'$ is dimensionless. The coupling between sectors would then go through the Planck constants:

$$V_{\text{int}} \propto \hbar_e / \hbar_q$$

or similar ratios. The rate of GGE relaxation (presently assumed infinite due to integrability) could in principle decay slowly if weak breaking of the Richardson-Gaudin structure occurs via coupling terms proportional to Planck constant ratios.

**Prediction**: If sectors have different effective Planck constants, then the GGE relic is not truly eternal but decays on a timescale proportional to the sector coupling strength. This is a new observable signature.

---

## References and Further Reading

- Volovik, G.E. (2023). "Acoustic Metric and Planck Constants". *JETP Letters* 117, 551-556. arXiv:2302.08894.
- Volovik, G.E. (2003). *The Universe in a Helium Droplet*. Oxford University Press.
- Volovik, G.E. (2021). "Graphene and Topological Insulator as Dirac Materials." (*JETP Letters* 114, 508-517).
- Akama, K. (1973). "Pregeometry as a Framework for Physics". YITP Research Reports.
- Diakonov, D. (2011). "Towards Lattice-Free Quantum Gravity". arXiv:1109.0091.
- Sakharov, A.D. (1967). "Vacuum Quantum Fluctuations in Curved Space and the Theory of Gravitation". *Soviet Physics Doklady* 12, 1040.
- Zee, A. (1973). "Spontaneously Broken Symmetry and Gravity". *Phys. Rev. D* 23, 858.
- Susskind, L. (1995). "The World as a Hologram". *J. Math. Phys.* 36, 6377.
- 't Hooft, G. (1993). "Dimensional Reduction in Quantum Gravity". arXiv:gr-qc/9310026.
