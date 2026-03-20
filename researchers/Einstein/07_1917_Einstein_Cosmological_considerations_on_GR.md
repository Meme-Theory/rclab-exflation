# Cosmological Considerations in the General Theory of Relativity

**Author:** Albert Einstein
**Year:** 1917
**Journal:** *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 142--152

---

## Abstract

In this paper, Einstein applies the field equations of general relativity to the universe as a whole, inaugurating relativistic cosmology as a science. Confronted with the fact that his original field equations do not admit a static, spatially finite solution with a uniform mass distribution, Einstein modifies the equations by introducing the cosmological constant $\Lambda$. The resulting "Einstein static universe" is a spatially closed (3-sphere) geometry with constant positive curvature, filled with pressureless matter ("dust") at constant density. Einstein motivates the modification by an appeal to Mach's principle -- the desire that the geometry of spacetime be entirely determined by the distribution of matter. The cosmological constant would later be called Einstein's "greatest blunder" (though this attribution to Einstein is disputed), yet it has returned as the dominant component of the cosmic energy budget, interpreted as dark energy driving the accelerating expansion of the universe.

---

## Historical Context

### The Pre-Cosmological Universe

Before 1917, there was essentially no scientific cosmology. Newtonian gravity applied to a uniform, infinite matter distribution suffers from well-known pathologies (Seeliger's paradox: the gravitational potential diverges, or Olbers' paradox: the night sky should be blindingly bright). The prevailing assumption among most physicists was that the universe was static and eternal -- the stars appeared to be more or less stationary on large scales.

The observational evidence available to Einstein was limited. The "spiral nebulae" (later recognized as galaxies) had been observed, and Slipher had measured Doppler shifts suggesting they were receding. However, the extragalactic distance scale was not established until Hubble's work in the 1920s. Einstein had no compelling observational evidence for either expansion or contraction.

### Mach's Influence

Einstein was deeply influenced by Ernst Mach's critique of Newton's absolute space. Mach argued that inertia should be relational -- determined not by motion relative to absolute space but by motion relative to the totality of matter in the universe. Einstein hoped that general relativity would realize Mach's vision: the metric tensor $g_{\mu\nu}$ (which determines inertial properties) should be entirely determined by the stress-energy tensor $T_{\mu\nu}$ (the matter distribution).

This Machian aspiration motivated Einstein to seek cosmological solutions in which the geometry is uniquely fixed by the matter content. A spatially infinite universe with matter concentrated in a finite region would have the metric approach Minkowski space at infinity -- a boundary condition that introduces absolute structure independent of matter, violating Mach's principle.

---

## Key Arguments and Derivations

### I. The Newtonian Analogy

Einstein begins by reviewing the analogous problem in Newtonian gravity. Consider Poisson's equation:

$$\nabla^2\Phi = 4\pi G\rho$$

For a uniform, infinite matter distribution ($\rho = \text{const}$), the only solution consistent with symmetry is $\Phi = \text{const}$, which gives $\nabla^2\Phi = 0$ -- contradicting $4\pi G\rho \neq 0$. The Newtonian problem has no self-consistent static solution for a uniform infinite distribution.

One might modify Poisson's equation to:

$$\nabla^2\Phi - \lambda\Phi = 4\pi G\rho$$

which admits the solution $\Phi = -4\pi G\rho/\lambda = \text{const}$. The additional $\lambda\Phi$ term introduces a "cosmological" modification that allows a static solution. This is the Newtonian analog of the cosmological constant.

### II. The Problem with the Original Field Equations

Einstein considers a static, spatially homogeneous universe filled with pressureless matter (dust, $p = 0$). The stress-energy tensor is:

$$T_{\mu\nu} = \rho u_\mu u_\nu$$

where $\rho$ is the matter density and $u^\mu = (c, 0, 0, 0)$ for matter at rest.

For a static metric (all $g_{\mu\nu}$ time-independent, no $g_{0i}$ cross-terms), Einstein's field equations $G_{\mu\nu} = \kappa T_{\mu\nu}$ require:

The spatial curvature must be constant (homogeneity) and the time-time equation must be consistent with the spatial equations. Einstein finds that no static solution with $\rho > 0$ exists for the original equations. A spatially flat static universe requires $\rho = 0$ (vacuum). A spatially curved static universe requires either $\rho < 0$ (unphysical) or inconsistent equations.

### III. Introduction of the Cosmological Constant

Einstein resolves this by modifying the field equations:

$$R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}$$

The additional term $\Lambda g_{\mu\nu}$ satisfies all the requirements:
- It is a symmetric, rank-2 tensor.
- It is divergence-free: $\nabla_\mu(\Lambda g^{\mu\nu}) = 0$ (since $\nabla_\mu g^{\mu\nu} = 0$ and $\Lambda$ is constant).
- It does not affect the Newtonian limit for solar-system scales (if $\Lambda$ is small enough).

The modified equations can be written equivalently as:

$$G_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu} - \Lambda g_{\mu\nu}$$

or, absorbing $\Lambda$ into an effective stress-energy:

$$G_{\mu\nu} = \frac{8\pi G}{c^4}\left(T_{\mu\nu} + T^{(\Lambda)}_{\mu\nu}\right)$$

where:

$$T^{(\Lambda)}_{\mu\nu} = -\frac{\Lambda c^4}{8\pi G}g_{\mu\nu}$$

This effective stress-energy has the equation of state of a perfect fluid with:

$$\rho_\Lambda = \frac{\Lambda c^2}{8\pi G}, \qquad p_\Lambda = -\rho_\Lambda c^2$$

The negative pressure is the key: it provides a repulsive gravitational effect that can balance the attractive gravity of matter.

### IV. The Einstein Static Universe

Einstein seeks a spatially homogeneous, isotropic, static solution. The metric ansatz is:

$$ds^2 = -c^2 dt^2 + a^2\left(\frac{dr^2}{1 - kr^2} + r^2 d\Omega^2\right)$$

where $a$ is a constant scale factor and $k$ is the spatial curvature ($k = +1$ for a 3-sphere, $k = 0$ for flat, $k = -1$ for hyperbolic).

For $k = +1$ (the 3-sphere), the modified field equations give:

**Time-time component:**
$$\frac{3}{a^2} = \frac{8\pi G}{c^2}\rho + \Lambda$$

**Space-space component:**
$$\frac{1}{a^2} = \Lambda$$

From the space-space equation: $\Lambda = 1/a^2 > 0$. Substituting into the time-time equation:

$$\frac{3}{a^2} = \frac{8\pi G}{c^2}\rho + \frac{1}{a^2}$$

$$\frac{2}{a^2} = \frac{8\pi G}{c^2}\rho$$

$$a^2 = \frac{c^2}{4\pi G\rho}$$

And:

$$\Lambda = \frac{4\pi G\rho}{c^2}$$

The Einstein static universe is a 3-sphere of radius $a$, with a specific relationship between the cosmological constant, matter density, and radius.

### V. Properties of the Einstein Static Universe

**Spatial volume:**
$$V = 2\pi^2 a^3$$

**Total mass:**
$$M = \rho V = 2\pi^2 \rho a^3 = \frac{\pi c^3}{2G}\sqrt{\frac{c^2}{4\pi G\rho}}$$

The universe is spatially finite but unbounded -- like the surface of a sphere in one higher dimension. A light ray traveling in a "straight line" (geodesic) would eventually return to its starting point after circumnavigating the 3-sphere.

**Instability:** Einstein did not recognize that his static solution is unstable. Eddington showed in 1930 that the Einstein static universe is like a ball balanced on the peak of a hill: the slightest perturbation in $a$ causes either expansion (if $a$ increases slightly, the repulsive $\Lambda$ term dominates and the universe expands forever) or collapse (if $a$ decreases, matter gravity dominates and the universe contracts). This instability is fundamental -- it shows that a truly static universe is not possible in GR, with or without $\Lambda$.

---

## Physical Interpretation

### Mach's Principle: Partial Realization

Einstein's explicit motivation was Machian: the geometry ($a$, and hence all of spacetime geometry) is completely determined by the matter density $\rho$. There are no arbitrary boundary conditions. The 3-sphere topology eliminates spatial infinity and its associated boundary conditions.

However, GR does not fully realize Mach's principle. De Sitter (1917) immediately found a vacuum solution ($\rho = 0$) with $\Lambda > 0$ -- the de Sitter space -- which has non-trivial geometry without any matter. This violated Einstein's Machian aspiration and led to an extended debate between Einstein and de Sitter.

### The Cosmological Constant as Vacuum Energy

In modern physics, the cosmological constant is naturally interpreted as the energy density of the quantum vacuum. Quantum field theory predicts that the vacuum has a nonzero energy density due to zero-point fluctuations. The predicted value is:

$$\rho_{vac} \sim \frac{m_P^4 c^5}{\hbar^3} \sim 10^{113}\;\text{J/m}^3$$

while the observed value (from the accelerating expansion) is:

$$\rho_\Lambda \sim 10^{-9}\;\text{J/m}^3$$

The discrepancy of $\sim 10^{122}$ is the "cosmological constant problem" -- one of the deepest puzzles in theoretical physics.

### Static vs. Expanding

The most significant historical aspect of this paper is what Einstein got wrong. The universe is not static. Friedmann (1922) showed that GR naturally predicts expanding or contracting universes. Lemaitre (1927) independently derived the expanding solution and connected it to Slipher's redshift observations. Hubble (1929) confirmed the expansion observationally.

Einstein reportedly came to regret introducing $\Lambda$, though whether he actually called it his "greatest blunder" (as attributed by Gamow) is uncertain. Regardless, the cosmological constant refused to stay dead.

---

## Impact and Legacy

### De Sitter's Response (1917)

Within months, Willem de Sitter found a vacuum solution ($T_{\mu\nu} = 0$) of the modified equations:

$$ds^2 = -\left(1 - \frac{\Lambda r^2}{3}\right)c^2 dt^2 + \frac{dr^2}{1 - \Lambda r^2/3} + r^2 d\Omega^2$$

This is the de Sitter space -- an exponentially expanding universe with no matter. It demonstrated that $\Lambda$ alone could drive expansion and showed that GR did not fully implement Mach's principle.

### Friedmann and Lemaitre

Alexander Friedmann (1922, 1924) found the general class of homogeneous, isotropic solutions to Einstein's equations (with or without $\Lambda$), the Friedmann equations:

$$\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda}{3}$$

$$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}\left(\rho + \frac{3p}{c^2}\right) + \frac{\Lambda}{3}$$

These equations govern all of observational cosmology.

### The Return of Lambda: Dark Energy

In 1998, observations of Type Ia supernovae by two independent teams (Perlmutter et al.; Riess et al.) demonstrated that the expansion of the universe is accelerating. The simplest explanation is a positive cosmological constant:

$$\Omega_\Lambda \approx 0.69, \qquad \Lambda \approx 1.1 \times 10^{-52}\;\text{m}^{-2}$$

This corresponds to an energy density $\rho_\Lambda \approx 5.9 \times 10^{-27}$ kg/m$^3$ and constitutes about 69% of the total energy budget of the universe. The cosmological constant, introduced by Einstein for the wrong reasons, has returned as the dominant component of cosmic energy.

---

## Connections to Modern Physics

### The Cosmological Constant Problem

The mismatch between the QFT prediction and the observed value of $\Lambda$ is perhaps the most severe fine-tuning problem in all of physics. Various approaches have been proposed:
- Anthropic selection (Weinberg, 1987)
- Quintessence (dynamical dark energy fields)
- Modified gravity theories ($f(R)$, massive gravity)
- Vacuum energy cancellation mechanisms (sequestering)

None is universally accepted.

### De Sitter Space and Inflation

The exponential expansion of de Sitter space is the prototype for cosmic inflation (Guth, 1981; Linde, 1982; Albrecht and Steinhardt, 1982). During inflation, the universe expands exponentially, driven by the potential energy of an inflaton field -- effectively a temporary cosmological constant. This solves the horizon, flatness, and monopole problems and generates the primordial density perturbations that seed structure formation.

### Holography and the de Sitter Entropy

The de Sitter horizon has a thermodynamic entropy (Gibbons and Hawking, 1977):

$$S_{dS} = \frac{A}{4G\hbar/c^3} = \frac{3\pi c^3}{G\hbar\Lambda}$$

This connects Einstein's cosmological constant to black hole thermodynamics and the holographic principle. Understanding the microscopic origin of de Sitter entropy is a major open problem in quantum gravity.

### Alternative Cosmological Frameworks

The observed cosmic acceleration has also motivated frameworks that reinterpret the data without a cosmological constant. Models based on backreaction (the effect of inhomogeneities on average expansion), modified dispersion relations, or emergent gravity propose that the "dark energy" is an artifact of interpreting observations within an assumed FLRW framework. Whether such alternatives can match the full observational dataset (SNe Ia, CMB, BAO, BBN) remains an active area of research. The epistemological lesson of Einstein's paper -- that even the creator of GR could be led astray by theoretical prejudice (the assumption of a static universe) -- remains salutary.
