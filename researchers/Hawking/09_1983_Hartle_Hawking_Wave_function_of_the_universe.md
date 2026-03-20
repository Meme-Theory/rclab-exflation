# Wave Function of the Universe

**Authors**: James B. Hartle, Stephen W. Hawking
**Year**: 1983
**Journal**: *Physical Review D*, **28**, 2960--2975

---

## Abstract (Analytical Summary)

Hartle and Hawking propose that the quantum state of the universe is defined by a Euclidean path integral over compact four-geometries with no boundary. The "no-boundary proposal" (NBP) states that the wave function of the universe $\Psi[h_{ij}, \phi]$ -- a functional of the three-metric $h_{ij}$ and matter field configuration $\phi$ on a spacelike surface $\Sigma$ -- is given by:

$$\Psi[h_{ij}, \phi] = \int_{\mathcal{C}} \mathcal{D}[g_{\mu\nu}] \, \mathcal{D}[\Phi] \, e^{-I[g, \Phi]}$$

where the integral is over all compact Euclidean four-geometries $(M, g_{\mu\nu})$ whose only boundary is $\Sigma$ (with induced metric $h_{ij}$ and field $\phi$), and $I$ is the Euclidean gravitational action. The proposal eliminates the need for initial conditions -- the universe has no initial boundary, no "beginning," and the singularity of classical cosmology is replaced by a smooth Euclidean cap. In the WKB approximation, the no-boundary wave function predicts a de Sitter-like inflationary phase, providing a natural initial condition for the inflationary universe.

---

## Historical Context

### The Problem of Initial Conditions

Classical general relativity, by the singularity theorems of Hawking and Penrose, predicts that the universe began with a singularity where physics breaks down. This raises the question: what are the initial conditions of the universe? In classical physics, initial conditions are external inputs to the theory. In quantum cosmology, one hopes to derive them from a quantum principle.

### The Wheeler--DeWitt Equation

DeWitt (1967) and Wheeler formulated quantum gravity in the canonical (Hamiltonian) framework. The quantum state of the universe is described by a wave functional $\Psi[h_{ij}, \phi]$ on the superspace of three-metrics and matter fields. The Hamiltonian constraint of general relativity becomes the Wheeler--DeWitt equation:

$$\hat{H} \Psi[h_{ij}, \phi] = 0$$

This is a second-order functional differential equation (a kind of Schrodinger equation without time -- "the problem of time" in quantum gravity). The Wheeler--DeWitt equation has infinitely many solutions; a boundary condition is needed to select the physical wave function.

### The Euclidean Approach

Hawking, building on the success of the Gibbons--Hawking Euclidean method (1977), proposed that the path integral provides both the solution and the boundary condition. The Euclidean path integral naturally selects a particular solution of the Wheeler--DeWitt equation through the choice of integration contour.

### Vilenkin's Alternative

Vilenkin (1982, 1984) independently proposed a "tunneling" wave function that also uses the Euclidean path integral but with a different contour/sign convention. Where Hartle--Hawking gives $\Psi \propto e^{-I_E}$ (selecting the compact saddle point with smallest action), Vilenkin gives $\Psi \propto e^{+I_E}$ (selecting the "tunneling" contour). The two proposals make different physical predictions, particularly for the probability of inflation.

---

## Key Arguments and Derivations

### Minisuperspace Model

The full path integral over all four-geometries is intractable. Hartle and Hawking work in a "minisuperspace" approximation, restricting to homogeneous, isotropic geometries:

$$ds^2 = \sigma^2 \left[ N^2(\lambda) d\lambda^2 + a^2(\lambda) d\Omega_3^2 \right]$$

where $a(\lambda)$ is the scale factor, $N(\lambda)$ is the lapse function, $d\Omega_3^2$ is the round metric on $S^3$, and $\sigma$ is a normalization constant. The matter content is a homogeneous scalar field $\phi(\lambda)$.

The Einstein--Hilbert action in this minisuperspace becomes a quantum mechanics problem with finitely many degrees of freedom ($a$ and $\phi$):

$$I = \frac{1}{2}\int d\lambda \, N \left[ -\frac{a \dot{a}^2}{N^2} + a - \frac{\Lambda}{3} a^3 + a^3 \left(\frac{\dot{\phi}^2}{2N^2} - V(\phi)\right) \right]$$

(where dots are $d/d\lambda$ and we have set $\sigma = 1$, $3/(4\pi G) = 1$ for simplicity).

### The No-Boundary Condition

The path integral is over compact four-geometries. In minisuperspace, this means integrating over histories $a(\lambda)$ that start at $a = 0$ (the "South Pole" of the Euclidean four-geometry) and end at a prescribed value $a = a_1$:

$$\Psi(a_1, \phi_1) = \int \mathcal{D}[N] \, \mathcal{D}[a] \, \mathcal{D}[\phi] \, e^{-I[N, a, \phi]}$$

with boundary conditions:
- At $\lambda = 0$: $a = 0$ (no boundary -- just a regular point, like the South Pole of a sphere)
- At $\lambda = 1$: $a = a_1$, $\phi = \phi_1$ (the boundary where the wave function is evaluated)

Regularity at $a = 0$ requires $\dot{a}(0)/N(0) = 1$ (the geometry looks like the origin of polar coordinates).

### Saddle-Point Approximation (WKB)

The path integral is evaluated in the saddle-point (WKB) approximation:

$$\Psi \approx e^{-I_E[\text{saddle}]}$$

The saddle-point geometry is the solution of the Euclidean Einstein equations that satisfies the boundary conditions. For pure cosmological constant (no scalar field), the Euclidean Einstein equation in minisuperspace is:

$$\left(\frac{\dot{a}}{Na}\right)^2 = 1 - H^2 a^2$$

where $H^2 = \Lambda/3$. The solution (with $N = 1$) is:

$$a(\tau) = \frac{1}{H} \sin(H\tau)$$

This is a portion of the four-sphere $S^4$ of radius $1/H$. At $\tau = 0$, $a = 0$ (South Pole); the geometry rounds off smoothly. At $\tau = \pi/(2H)$, $a = 1/H$ (the "equator"), and the geometry can be analytically continued to Lorentzian signature.

### Analytic Continuation to Lorentzian Signature

At the equator ($a = 1/H$), the Euclidean solution matches onto a Lorentzian de Sitter solution. Setting $\tau = \pi/(2H) + it$:

$$a(t) = \frac{1}{H} \cosh(Ht)$$

This is the expanding de Sitter universe. The full geometry is: a Euclidean hemisphere (the four-sphere cap) smoothly joined to a Lorentzian de Sitter expansion. The universe has no initial singularity -- it has "no boundary," just a smooth Euclidean cap.

### The Wave Function

The Euclidean action of the four-sphere cap is:

$$I_E = -\frac{3}{8G\Lambda}\left(1 - (1 - H^2 a_1^2)^{3/2}\right) + \frac{3}{8G\Lambda}$$

For $a_1 \gg 1/H$ (large universe):

$$I_E \approx -\frac{3}{8G\Lambda} + i \cdot (\text{phase})$$

The wave function in the WKB approximation has two contributions (from the two saddle points related by complex conjugation):

$$\Psi(a_1) \approx \exp\left(\frac{3}{8G\Lambda}\right) \cos\left(\text{oscillatory phase}\right)$$

The exponential prefactor $e^{+3/(8G\Lambda)}$ (for the Hartle--Hawking choice) means the wave function is large for small $\Lambda$ -- the no-boundary proposal favors a large universe with small cosmological constant. (Vilenkin's tunneling proposal gives $e^{-3/(8G\Lambda)}$, favoring large $\Lambda$.)

### Including a Scalar Field

With a scalar field $\phi$ and potential $V(\phi)$, the no-boundary saddle point involves both $a(\tau)$ and $\phi(\tau)$ evolving in Euclidean time. At the South Pole:

$$a = 0, \quad \dot{a}/N = 1, \quad \dot{\phi} = 0$$

(regularity requires $\dot{\phi} = 0$ at the South Pole). The scalar field starts near the top of its potential (if $V$ has a plateau) and rolls slowly. This naturally provides initial conditions for slow-roll inflation: the scalar field begins at the top of the potential with zero velocity -- exactly the conditions needed for inflation.

The probability of inflation with $N$ e-folds is (in the Hartle--Hawking prescription):

$$P(N) \propto \exp\left(\frac{3}{8G \, V(\phi_N)}\right)$$

This exponentially favors configurations with small $V$ (many e-folds of inflation), predicting a long inflationary epoch.

---

## Physical Interpretation

### "The Universe from Nothing"

The no-boundary proposal provides a mathematical realization of the idea that the universe could have "come from nothing." There is no initial singularity, no moment of creation, no external input of initial conditions. The universe simply *is* -- a self-contained four-geometry with no boundary. The question "what happened before the Big Bang?" is like asking "what is north of the North Pole?" -- the question has no answer because the geometry simply does not extend in that direction.

### The Problem of Time

In the no-boundary proposal, time is not fundamental. The Euclidean section has no time at all -- it is a four-dimensional Riemannian manifold. Time "emerges" at the Euclidean-to-Lorentzian transition, where the oscillatory behavior of the wave function allows a WKB interpretation in terms of classical trajectories in superspace.

### Probabilities and the Measure Problem

The wave function $|\Psi|^2$ is interpreted as a probability measure on the space of three-geometries and field configurations. For the minisuperspace model, $|\Psi(a, \phi)|^2$ gives the probability of finding a universe with scale factor $a$ and field value $\phi$. Extending this to the full superspace and defining a proper probability measure (the "measure problem" of cosmology) remains an open problem.

---

## Impact and Legacy

### The No-Boundary Proposal as a Research Program

The NBP has generated an enormous body of work:

1. **Perturbation theory around the no-boundary saddle**: Halliwell and Hawking (1985) computed the perturbation spectrum generated by the no-boundary state, finding consistency with inflation.

2. **The Lorentzian path integral**: Feldbrugge, Lehners, and Turok (2017) challenged the NBP by arguing that the Lorentzian path integral (which is the physically correct starting point) does not converge for the no-boundary condition. This sparked a vigorous debate.

3. **Picard--Lefschetz theory**: The saddle-point approximation of the gravitational path integral requires careful treatment of the complex integration contour (thimbles). Different choices of thimble correspond to different proposals (Hartle--Hawking, Vilenkin, etc.).

4. **No-boundary proposal in string theory**: The NBP can be embedded in string theory via Euclidean instantons in the string landscape.

### Hartle--Hawking vs. Vilenkin

The two main proposals for the wave function of the universe differ in the sign of the exponential:

| Feature | Hartle--Hawking | Vilenkin |
|---|---|---|
| Wave function | $e^{-I_E} = e^{+|I_E|}$ | $e^{+I_E} = e^{-|I_E|}$ |
| Favors | Small $\Lambda$, long inflation | Large $\Lambda$, short inflation |
| Classical limit | No boundary | Tunneling |

The Hartle--Hawking proposal has been criticized for predicting a Boltzmann brain problem (it favors very long inflation, leading to enormous empty de Sitter regions). The Vilenkin proposal avoids this but has convergence issues.

### Quantum Cosmology as a Framework

Regardless of the specific proposal, the Hartle--Hawking paper established quantum cosmology as a field: the application of quantum mechanics to the universe as a whole. The Wheeler--DeWitt equation, the minisuperspace approximation, and the interpretation of the wave function of the universe are now standard tools.

---

## Connections to Modern Physics

1. **Holography and the wave function**: In the dS/CFT proposal (Maldacena, 2002; Hertog and Hartle, 2011), the Hartle--Hawking wave function is dual to the partition function of a Euclidean CFT on $S^3$. This provides a holographic interpretation of the no-boundary proposal.

2. **Eternal inflation and the multiverse**: The no-boundary wave function, combined with the string landscape, leads to a multiverse of pocket universes. The measure problem (how to assign probabilities to different vacua) is the central unsolved problem of the multiverse.

3. **Loop quantum cosmology**: Loop quantum gravity provides an alternative approach to quantum cosmology where the big bang singularity is replaced by a "big bounce." The bounce occurs at Planck density $\rho \sim \rho_P$ and is followed by slow-roll inflation. This is an alternative to the Euclidean cap of the no-boundary proposal.

4. **Gravitational path integral and topology change**: The no-boundary proposal requires summing over topologies (not just metrics). This is a radical departure from classical GR, where topology is fixed. The sum over topologies connects to string theory (where topology change occurs naturally via worldsheet instantons) and to the recent work on the gravitational path integral (replica wormholes, islands).

5. **For the exflation framework**: In a Kaluza--Klein context, the no-boundary proposal would involve a Euclidean path integral over compact geometries of the form $M_4 \times K$, where both the 4D geometry and the internal space $K$ are specified on the boundary. The "no-boundary" condition would constrain the initial configuration of the internal space, potentially providing a natural starting point for the exflation mechanism. The Euclidean section could determine the initial "size" and geometry of $K$ (e.g., why $SU(3)$ rather than another group manifold), connecting the no-boundary proposal to the gauge group selection problem.
