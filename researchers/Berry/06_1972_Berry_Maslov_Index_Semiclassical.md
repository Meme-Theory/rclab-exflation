# The Maslov Index and Semiclassical Mechanics

**Author(s):** Michael V. Berry and K.E. Mount

**Year:** 1972

**Journal:** Reports on Progress in Physics, Vol. 35, pp. 315-397

---

## Abstract

The WKB (Wentzel-Kramers-Brillouin) approximation is a widely used semiclassical method for solving the Schrodinger equation in the limit $\hbar \to 0$. However, the WKB wave function near a caustic (turning point) is singular, and the connection formulas (matching solutions across caustics) were historically obtained through ad-hoc arguments. Berry and Mount showed that the Maslov index—a topological invariant counting the number of caustics encountered along a classical trajectory—provides the rigorous mathematical foundation for WKB connection formulas. The Maslov index $\mu$ enters the WKB phase as an additional geometric contribution:

$\phi_{\text{WKB}} = \frac{1}{\hbar} \int p \, dq - \frac{\pi \mu}{2}$

This unifies the seemingly diverse WKB corrections and reveals a deep connection between differential geometry and the semiclassical limit of quantum mechanics.

---

## Historical Context

The WKB approximation dates to the 1920s and was developed to solve the Schrodinger equation in the classical limit. For a particle in a potential $V(x)$:

$\psi(x) \approx \frac{A}{\sqrt{p(x)}} e^{i \phi(x) / \hbar}$

where $p(x) = \sqrt{2m(E - V(x))}$ is the classical momentum and $\phi(x) = \int p \, dx$ is the classical action.

However, the WKB approximation breaks down near turning points (caustics), where $p(x) = 0$. Near these points, the potential is well-approximated by a linear function, and the Schrodinger equation resembles an Airy equation. Matching WKB solutions across turning points requires "connection formulas" that historically were derived through ad-hoc calculations or physical arguments.

Maslov (1972, independently of Berry) discovered that the phase corrections in WKB connection formulas are determined by a topological invariant—the Maslov index—which counts caustics. Berry and Mount's 1972 review developed this insight and showed how the Maslov index elegantly resolves the long-standing problem of WKB normalization and connection formulas.

---

## Key Arguments and Derivations

### Classical Caustics and the Lagrangian Manifold

In the semiclassical approximation, the quantum wave function encodes the classical trajectory information. The phase of the wave function:

$\psi(x, t) \sim e^{i S(x,t) / \hbar}$

where $S(x, t) = \int_0^t \mathcal{L} \, dt'$ is the classical action along a trajectory from initial position to $(x, t)$.

A caustic is a point where the Jacobian of the map from initial conditions to final position vanishes:

$\det \left( \frac{\partial x_f}{\partial x_i} \right) = 0$

Caustics represent focusing or defocusing of classical trajectories. Near a caustic, many different classical paths arrive at the same final position with nearly the same action. The WKB wave function becomes singular at caustics because the denominator factor $\sqrt{|\det J|}$ (the Jacobian determinant) vanishes.

### The Maslov Transformation

To handle caustics rigorously, Maslov introduced a canonical transformation that locally straightens the caustic structure. The key insight is that the phase of the wave function experiences a sudden change as one crosses a caustic.

For each isolated caustic encountered along a path, the phase shifts by $\pi/2$. If a trajectory encounters $\mu$ caustics, the total phase shift is $\pi \mu / 2$.

The WKB wave function should be written as:

$\psi_{\text{WKB}}(x) = A(x) e^{i[\phi_0(x) - \pi \mu / 2] / \hbar}$

where $\phi_0(x) = \int_0^x p(x') dx'$ is the naive WKB phase (without Maslov correction), and $\mu$ is the Maslov index counting caustics from 0 to $x$.

### Maslov Index as a Topological Invariant

The Maslov index is an integer invariant that counts, with sign, the number of times a curve in phase space crosses a caustic surface. For a closed trajectory (periodic orbit), the Maslov index is:

$\mu = \frac{1}{\pi} \oint \nabla \theta \cdot d\vec{q}$

where $\theta$ is the polar angle in phase space.

For a particle in a 1D potential with two turning points (classical turning points where $E = V$), a closed orbit encloses both turning points. Each turning point contributes $\mu = 1$ to the index, giving $\mu = 2$ for a round trip. The quantization condition becomes:

$\oint p \, dq = 2\pi \hbar (n + \frac{\mu}{4}) = 2\pi \hbar (n + \frac{1}{2})$

where $n = 0, 1, 2, \ldots$ is the quantum number. This is the Bohr-Sommerfeld quantization condition, reproduced from first principles using the Maslov index.

### WKB Connection Formulas

Near a simple turning point $x = x_0$ where $E = V(x_0)$, expand:

$V(x) \approx V(x_0) + V'(x_0)(x - x_0) = E + \alpha(x - x_0)$

where $\alpha = V'(x_0) > 0$ for a left turning point.

The Schrodinger equation becomes:

$-\frac{\hbar^2}{2m} \psi'' + \alpha(x - x_0) \psi = 0$

This is the Airy equation with solution:

$\psi(x) \sim \text{Ai}(\zeta)$

where $\zeta = \left( \frac{2m\alpha}{\hbar^2} \right)^{1/3} (x - x_0)$ is the scaled coordinate.

For $x < x_0$ (classically forbidden region), the WKB solution is:

$\psi_{\text{WKB}} = \frac{C}{\sqrt{|p(x)|}} e^{-|S(x)| / \hbar}$

For $x > x_0$ (classically allowed region):

$\psi_{\text{WKB}} = \frac{C}{\sqrt{p(x)}} e^{i[S(x) - \pi\hbar/4] / \hbar}$

The phase shift of $-\pi/4$ is the Maslov correction for a single caustic.

### Generalization to Multidimensional Systems

For a particle in $N$ dimensions, the Maslov index is an integer associated with each closed curve in phase space. The generalized quantization condition is:

$\oint \vec{p} \cdot d\vec{q} = 2\pi \hbar \left( n + \frac{\mu}{4} \right)$

where $n$ is a multi-index labeling quantum numbers and $\mu$ is the Maslov index for the $N$-dimensional orbit.

For systems with rotational symmetry (e.g., atoms), the Maslov index can be computed from geometric properties of the orbit and determines the angular momentum quantization.

---

## Key Results

1. **Maslov index theorem**: The Maslov index is a topological invariant that counts caustics with sign, providing the rigorous phase correction to WKB.

2. **Bohr-Sommerfeld quantization from first principles**: The Maslov index reproduces the Bohr-Sommerfeld quantization rule with corrections of order $\hbar$:

   $E_n = E(\text{$n+\mu/4$-th orbit})$

3. **WKB connection formulas**: At each caustic, the WKB wave function phase shifts by $\pi/2$, determined by the Airy function asymptotics.

4. **Universality**: The Maslov index method applies to any dimension and any integrable system. The caustic structure encodes all the topological information needed for semiclassical quantization.

5. **Periodic orbit quantization**: For closed orbits, the Maslov index combined with the action integral gives precise quantization conditions superior to older WKB methods.

---

## Impact and Legacy

Berry and Mount's clarification of the Maslov index became standard in semiclassical quantum mechanics:

- **Foundational rigor**: Replaced ad-hoc connection formulas with a systematic topological approach.
- **Periodic orbit theory**: The Maslov index is essential in Gutzwiller's semiclassical trace formula for computing quantum spectra from classical periodic orbits.
- **Molecular spectroscopy**: Used to correct WKB predictions for molecular vibrational-rotational levels.
- **Quantum-classical correspondence**: Established that caustic topology (a purely classical geometric property) determines quantum phase structure.
- **Quantum chaos**: Combined with periodic orbit sums, the Maslov index explains level spacing statistics and spectral correlations.

The Maslov index is now indispensable in any semiclassical analysis of quantum systems.

---

## Connection to Phonon-Exflation Framework

In the semiclassical quantization of the phonon-exflation model, the Maslov index plays a crucial role:

1. **Periodic orbits in internal space**: The classical limit of the phonon system (phonons as oscillations in the internal SU(3) space) admits periodic orbits. The Maslov index of these orbits determines the semiclassical quantization of phonon energies.

2. **Caustics from avoided crossings**: The avoided crossings in the Dirac spectrum (e.g., sector (3,0)-(2,0) near $s = 0.15$) correspond to caustics in the "classical" limit where the Dirac operator is treated as a classical differential operator. The Maslov index counts these caustics.

3. **WKB approximation for the spectral action**: When computing the spectral action $S_{\text{spec}} = \text{Tr} f(D^2/\Lambda^2)$ in the semiclassical limit, the Maslov index corrections ensure that eigenvalue spacings are correctly accounted for near avoided crossings.

4. **Quantization of the modulus**: If the cosmological modulus $s$ is treated as a "coordinate" and the expansion of the universe as "classical motion" in modulus space, the Maslov index determines how $s$ should be quantized. Turning points in the modulus potential (minima of $V_{\text{eff}}(s)$) create caustics in modulus space.

5. **Bohr-Sommerfeld-like quantization**: The phonon modes in the internal space might obey a Bohr-Sommerfeld-like quantization condition with Maslov corrections:

   $\oint p_s \, ds = 2\pi \hbar (n + \mu/4)$

   where $p_s$ is the momentum conjugate to $s$ and $\mu$ is the Maslov index.

The Maslov index is particularly relevant when treating the phonon-exflation system in a semiclassical regime where classical-like behavior is approaching quantum behavior.
