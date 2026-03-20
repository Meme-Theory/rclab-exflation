# Topological Order in Superfluid 3He-B: BDI Classification and Majorana Bound States

**Author:** G.E. Volovik

**Year:** 2009

**Journal:** JETP Letters 90, 587-591 (2009)

**arXiv:** 0904.4113

---

## Abstract

Superfluid 3He-B is one of the first identified topologically ordered materials—a phase of matter protected by subtle interplay of symmetry and topology rather than by a conventional energy gap. We apply the Altland-Zirnbauer (AZ) symmetry classification to 3He-B and show that it belongs to class BDI: systems with time-reversal symmetry T (with T²=+1), particle-hole symmetry C (with C²=+1), and chiral symmetry S. We analyze the topological invariants protecting this phase and predict the existence of zero-energy Majorana bound states on the surface and at topological defects (vortex cores, domain walls). These Majorana states are robust against disorder and weak interactions respecting the AZ class symmetry. The framework explains why 3He-B is stable against perturbations and why surface Andreev reflection exhibits a distinctive experimental signature. We also discuss the relationship between topological order and conventional superconductivity, and the role of the weak strong-interaction regime.

---

## Historical Context

Superfluid 3He was discovered in 1971 by Cornell, Osheroff, and Richardson (later earning them the Nobel Prize). It occurs at temperatures below 2.6 mK and exhibits two phases: the A-phase and the B-phase, with different order parameters and symmetries.

The 3He-B phase has an order parameter $\mathbf{d}$-vector and pair potential $\Delta(\hat{\mathbf{k}})$ of p-wave form:

$$\Delta(\hat{\mathbf{k}}) = \Delta_0 (\hat{\mathbf{k}} \cdot \hat{\mathbf{d}})$$

This is fundamentally different from s-wave superconductors (where $\Delta$ is isotropic). The p-wave nature means:
- Fermions with different orbital angular momenta pair differently
- Zero modes exist in vortex cores
- The phase is strongly protected against disorder

In 2008-2009, the Altland-Zirnbauer classification of topological phases was developed, showing that matter could be organized into 10 symmetry classes (5 in 2D, 5 in 3D, with another 5 arising from magnetic systems). Volovik immediately recognized that 3He-B fits precisely into class BDI.

For phonon-exflation, 3He-B serves as the **experimental model system**. The framework's BCS gap structure and Majorana modes are direct analogues of 3He-B physics. If the framework is correct, real 3He-B experiments could provide validation.

---

## Key Arguments and Derivations

### Altland-Zirnbauer Classification

The AZ classification organizes topological phases by three discrete symmetries:
1. **Time-reversal T**: $\hat{T} \psi(\mathbf{r}) \hat{T}^{-1} = U_T \psi(-\mathbf{r})$, with $\hat{T}^2 = \pm 1$
2. **Particle-hole C**: $\hat{C} \psi(\mathbf{r}) \hat{C}^{-1} = U_C \psi^c(-\mathbf{r})$, with $\hat{C}^2 = \pm 1$
3. **Chiral S**: product $S = CT$ (or sometimes defined as sublattice symmetry)

For 3He-B:
- T-symmetry: YES, with $\hat{T}^2 = +1$ (bosonic time-reversal for fermion pairs)
- C-symmetry: YES, with $\hat{C}^2 = +1$ (particle-hole for BCS quasiparticles)
- Chiral symmetry: YES (emergent from the gap structure)

This combination places 3He-B in **class BDI**.

The ten AZ classes are organized in a periodic table (Bott periodicity) where certain topological invariants repeat every 8 classes in 3D. Class BDI has a **topological invariant Z** (integer quantization), meaning topological phases in this class are indexed by integers.

### Order Parameter and Symmetry

The 3He-B order parameter is:
$$\Delta_{ab}(\hat{\mathbf{k}}) = \Delta_0 d_a k_b + \text{(other terms)}$$

where $a, b$ are spin indices and $\hat{\mathbf{k}} = \mathbf{k}/|\mathbf{k}|$.

The symmetry group is:
- Spin SU(2) rotation: $\psi \to e^{i\sigma \theta} \psi$
- Orbital rotations: $\hat{\mathbf{d}} \to R \hat{\mathbf{d}}$ (SO(3) in spin space)
- Gauge U(1): $\psi \to e^{i\alpha} \psi$ (number conservation)

These form the full symmetry group **SO(3)_spin × SO(3)_orbital × U(1)_gauge**.

The ground state breaks most of these symmetries:
- Spin SU(2) → U(1) (spin singlet pairs)
- Orbital SO(3) → SO(2) (rotations around $\hat{\mathbf{d}}$)
- Gauge U(1) is spontaneously broken (BCS condensation)

The resulting residual symmetry is much smaller, making the phase **stable** against perturbations.

### Majorana Zero Modes in Vortices

A quantized vortex (Abrikosov vortex) in 3He-B has circulation:
$$\oint_C \nabla \theta = 2\pi$$

where $\theta$ is the condensate phase. The vortex core has radius $\xi \sim \hbar / \Delta_0$ (the coherence length).

In the vortex core, the order parameter $\Delta$ varies spatially and passes through zero at the center. This creates a bound state—a fermion trapped in the potential well of the vanishing gap.

The crucial result: for p-wave superfluids in class BDI, **vortex bound states are Majorana fermions**—zero-energy states $E = 0$ that are their own antiparticles:

$$\psi_{\text{vortex}} = \psi_{\text{vortex}}^\dagger$$

The Majorana condition is protected by particle-hole symmetry: if $\psi$ is a solution to the BdG equations with energy E, then $\psi^c = C \psi^*$ is a solution with energy -E. At E=0, these are identical, forcing $\psi = \psi^c$ (Majorana).

The vortex core thus hosts a **non-abelian Majorana zero mode**, which can be manipulated to perform topological quantum computations.

### Robustness Against Disorder

A key property of topological phases in class BDI is their robustness against weak disorder that respects the time-reversal and particle-hole symmetries.

In conventional superconductors, disorder destroys the superconducting gap via Anderson localization. In 3He-B, however, the topological protection prevents localization:

**Anderson's theorem (modified)**: In a topological superconductor, weak impurities do not suppress the gap if they conserve particle-hole and time-reversal symmetries.

This is because the gap-opening mechanism is topological (winding of the order parameter in momentum space), not conventional (interaction-induced).

Quantitatively, for impurity potential $V_{\text{imp}}$ with mean free path $\ell_{\text{mfp}}$, the gap suppression scales as:

$$\frac{\Delta}{\Delta_0} \approx 1 - (\ell_{\text{mfp}} / \xi)^2 + O((\ell_{\text{mfp}} / \xi)^4)$$

The quadratic dependence (rather than linear, as in s-wave) reflects topological protection.

### Surface Andreev Reflection

On the surface of 3He-B, quasiparticles undergo **Andreev reflection**—an electron incident on the surface is reflected as a hole, with a Cooper pair transferred to the condensate.

In topological superfluids, surface Andreev reflection exhibits exotic behavior:
$$r_{\text{Andreev}} \propto \frac{E}{\Delta}$$

(energy-dependent reflection probability). This is distinct from s-wave superfluids, where $r_{\text{Andreev}} \approx 1$ (nearly perfect reflection).

The energy-dependent reflection arises because the surface state is a **chiral fermion**: it has definite chirality (handedness) and exhibits anomalous transport properties.

### Topological Invariant: The Z Index

The topological invariant for class BDI in 3D is an **integer winding number**:

$$W = \frac{1}{2\pi i} \oint dE \, \text{tr}\left[\hat{G}(E) \partial_E \hat{G}(E)\right]$$

where $\hat{G}(E)$ is the Green's function of the superfluid.

For 3He-B, this evaluates to $W = 1$, indicating a singly-wound topological phase.

Different values of W distinguish different topological phases within class BDI:
- $W = 0$: topologically trivial (s-wave superconductor)
- $W = 1$: singly topological (3He-B, some heavy fermion superconductors)
- $W = 2$: doubly topological (not yet observed, but theoretically possible)

---

## Key Results

1. **BDI Classification**: 3He-B belongs to Altland-Zirnbauer class BDI (T²=+1, C²=+1, S). This classification is protected by symmetry and is stable under perturbations respecting BDI.

2. **Majorana Vortex Modes**: Quantized vortices host zero-energy Majorana fermions, non-abelian topological states enabling topological quantum computation.

3. **Robustness Against Disorder**: The topological gap is protected against weak disorder respecting time-reversal and particle-hole symmetry, unlike conventional superconductors.

4. **Surface Chiral Fermions**: The 3He-B surface exhibits chiral fermion modes with anomalous transport properties and energy-dependent Andreev reflection.

5. **Topological Index Z**: The winding number W=1 distinguishes 3He-B from trivial s-wave phases (W=0) and higher topological phases (W>1).

6. **Domain Wall Zero Modes**: Domain walls between regions with different orientations of the $\hat{\mathbf{d}}$-vector also host Majorana modes, enabling braiding.

---

## Impact and Legacy

Volovik's identification of 3He-B as a topological phase in class BDI unified superfluidity and topological order. This motivated:
- Experimental searches for Majorana modes in vortices (via STM tunneling spectroscopy)
- Topological quantum computing proposals exploiting Majorana braiding
- Classification of iron-pnictide and organic superconductors as topological phases
- Development of time-reversal invariant topological insulators and superconductors

3He-B became a paradigm: the "test bed" for all predictions of topological phase physics.

---

## Connection to Phonon-Exflation Framework

**Direct Relevance (TIER 1)**

The framework is **exactly 3He-B analog** in internal-space geometry. Session 17c proved AZ class BDI with T²=+1. Volovik's 2009 analysis applies directly.

**Mapping**:
- 3He-B p-wave order parameter: $\Delta(\hat{\mathbf{k}}) \to$ BCS pairing condensate $\Delta(\tau)$ in SU(3)-color
- Vortex Majorana modes: 10 sectors with gapped structure at fold, topological defects host zero modes
- Robustness against disorder: the framework's stability under RG flow (Sessions 33a-34)
- Surface Andreev reflection: quasiparticle-sector coupling at the fold boundary

**Vortex Identification**:
In 3He-B, vortices have winding number 1 (singly-quantized). In the framework, Cooper pairs carry K_7 charge ±1/2, creating effective "color vortices" in the internal space.

The 10 sectors can be thought of as 10 distinct **vortex orientations**, each hosting a Majorana-like mode.

**Topological Quantum Computation**:
If the framework is correct, the GGE relic (which has 8 conserved integrals from Richardson-Gaudin integrability) represents a **topologically protected state**.

Braiding of the 10-sector "vortex positions" would generate non-abelian statistics, enabling topological computation.

This is experimentally testable: the framework predicts that high-redshift observations (z>10) should exhibit **topological charge conservation** in particle scattering events, distinct from standard QCD.

**Majorana Surface States**:
The fold defines a "surface" in the internal-space fabric. According to Volovik's BDI analysis, this surface should host **chiral fermion modes**.

These would manifest observationally as anomalies in CP violation at the fold (where surface Andreev reflection occurs). Session 38's computations did NOT find enhanced CP violation, so either:
1. The surface is not a geometric boundary (more plausibly, it is a smooth deformation)
2. CP violation is protected by some other mechanism

This is an open question for Session 43+.

