# The Gravitational Equations and the Problem of Motion

**Authors:** Albert Einstein, Leopold Infeld, Banesh Hoffmann
**Year:** 1938
**Journal:** *Annals of Mathematics*, **39**(1), 65--100

---

## Abstract

This paper demonstrates one of the most remarkable features of general relativity: the equations of motion of gravitating bodies do not need to be postulated independently but follow as necessary consequences of the gravitational field equations themselves. In Newtonian gravity, the field equation (Poisson) and the equation of motion (Newton's second law) are separate postulates. In GR, the geodesic equation -- and its post-Newtonian corrections -- can be derived from the Einstein field equations $G_{\mu\nu} = \kappa T_{\mu\nu}$ alone. Einstein, Infeld, and Hoffmann (EIH) develop a systematic surface-integral method for extracting the equations of motion of $N$ compact bodies from the vacuum field equations, expanding in powers of $v/c$ and $Gm/(rc^2)$. The EIH equations of motion, valid to first post-Newtonian order, underlie modern calculations of gravitational wave templates, binary pulsar dynamics, and post-Newtonian celestial mechanics.

---

## Historical Context

### The Problem of Motion in GR

In Newtonian gravity, the structure of the theory is dualistic: the gravitational field is determined by the Poisson equation $\nabla^2\Phi = 4\pi G\rho$, and the motion of test particles in this field is governed by Newton's second law $\mathbf{F} = m\mathbf{a}$. These are independent postulates -- the field equation does not imply the equation of motion or vice versa.

From the earliest days of general relativity, it was suspected that this dualism might be resolved. The geodesic equation:

$$\frac{d^2 x^\alpha}{d\tau^2} + \Gamma^\alpha_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau} = 0$$

describes the motion of a test particle (a body whose own gravitational field is negligible). Einstein and Grommer (1927) had already shown that the geodesic equation could be derived from the field equations for the special case of infinitesimal test particles, using the requirement that the metric be singularity-free everywhere.

The much harder problem is the motion of massive bodies whose own gravitational fields cannot be neglected. A planet orbiting the Sun is not a test particle -- it curves spacetime in its own right, and the full problem is one of two (or more) interacting gravitational sources. The EIH paper solves this problem systematically.

### The Singularity Approach

The EIH method treats each body as a singularity (or effectively point-like source) of the gravitational field. The field equations are solved in the vacuum region outside the bodies, and the equations of motion are extracted from regularity conditions on the field. This approach sidesteps the need to model the internal structure of the bodies -- the motion depends only on the masses (and, at higher orders, on the spins and multipole moments).

This is a profound result: it means that the motion of compact bodies is universal -- it depends on their masses and spins but not on their internal composition. This is the strong equivalence principle in action.

---

## Key Arguments and Derivations

### I. The Strategy: Surface Integrals

The fundamental idea is to surround each body with a small surface $S_a$ (a 2-sphere in the spatial sections). The vacuum field equations hold everywhere outside the bodies. By integrating the field equations over surfaces enclosing each body, one obtains conditions that constrain the worldlines of the singularities -- these conditions are the equations of motion.

The metric is expanded in a post-Newtonian series:

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}^{(2)} + h_{\mu\nu}^{(4)} + \cdots$$

where the superscript denotes the order in the small parameter $\epsilon \sim v^2/c^2 \sim Gm/(rc^2)$ (these are of the same order for gravitationally bound systems by the virial theorem).

### II. The Newtonian Limit (Zeroth Order)

At lowest order, the $00$ component of the linearized field equations gives:

$$\nabla^2 h_{00}^{(2)} = 0 \quad \text{(vacuum)}$$

with the boundary condition that $h_{00}^{(2)}$ has the form $-2Gm_a/(c^2|\mathbf{r} - \mathbf{r}_a|)$ near each body $a$. The solution for $N$ bodies is:

$$h_{00}^{(2)} = -\frac{2}{c^2}\sum_{a=1}^N \frac{Gm_a}{|\mathbf{r} - \mathbf{r}_a|}$$

which is the Newtonian potential $\Phi = -\sum_a Gm_a/|\mathbf{r} - \mathbf{r}_a|$, giving $g_{00} \approx -(1 + 2\Phi/c^2)$.

The equations of motion at this order reproduce Newton's law of gravitation:

$$m_a\ddot{\mathbf{r}}_a = -\sum_{b\neq a}\frac{Gm_a m_b(\mathbf{r}_a - \mathbf{r}_b)}{|\mathbf{r}_a - \mathbf{r}_b|^3}$$

### III. The First Post-Newtonian Correction (EIH Equations)

At the next order ($\epsilon \sim v^2/c^2$), the field equations generate corrections to both the metric and the equations of motion. The EIH method systematically solves the field equations order by order and extracts the motion from surface integrals.

The result for two bodies (masses $m_1$, $m_2$, separation $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$, $r = |\mathbf{r}|$, velocities $\mathbf{v}_1$, $\mathbf{v}_2$) is the EIH equation of motion for body 1:

$$m_1\mathbf{a}_1 = -\frac{Gm_1 m_2}{r^2}\hat{\mathbf{r}} + \frac{Gm_1 m_2}{c^2 r^2}\Bigg\{$$
$$\hat{\mathbf{r}}\left[-v_1^2 - 2v_2^2 + 4(\mathbf{v}_1\cdot\mathbf{v}_2) + \frac{3}{2}(\hat{\mathbf{r}}\cdot\mathbf{v}_2)^2 + \frac{5Gm_1}{r} + \frac{4Gm_2}{r}\right]$$
$$+ (\mathbf{v}_1 - \mathbf{v}_2)\left[4(\hat{\mathbf{r}}\cdot\mathbf{v}_1) - 3(\hat{\mathbf{r}}\cdot\mathbf{v}_2)\right]\Bigg\}$$

where $\hat{\mathbf{r}} = \mathbf{r}/r$ and the expression involves velocity-dependent and nonlinear-in-$G$ terms that have no Newtonian counterpart.

Key features of the 1PN (first post-Newtonian) corrections:

1. **Velocity-dependent forces:** The acceleration depends on the velocities of both bodies, not just their positions. This is analogous to the velocity-dependent magnetic force in electrodynamics.

2. **Nonlinear gravitational self-energy:** The term $5Gm_1/r + 4Gm_2/r$ represents the gravitational potential energy's contribution to inertia (via $E = mc^2$). Gravitational binding energy gravitates.

3. **Perihelion precession:** For a test particle ($m_2 \to 0$) in a nearly circular orbit, the 1PN correction produces the same perihelion precession as the Schwarzschild geodesic calculation:

$$\Delta\phi = \frac{6\pi GM}{c^2 a(1-e^2)}$$

4. **No dipole radiation:** The conservation of center-of-mass momentum at 1PN implies that gravitational "dipole radiation" is absent -- a key difference from electrodynamics, where accelerating charges radiate at the dipole level.

### IV. The Derivation Mechanism: Why Field Equations Imply Motion

The deep reason that the field equations determine the motion is the Bianchi identity:

$$\nabla_\mu G^{\mu\nu} \equiv 0$$

Combined with the field equations $G^{\mu\nu} = \kappa T^{\mu\nu}$, this gives:

$$\nabla_\mu T^{\mu\nu} = 0$$

For a system of point particles, $T^{\mu\nu}$ involves delta functions supported on the worldlines. The covariant conservation equation $\nabla_\mu T^{\mu\nu} = 0$ constrains these worldlines to be geodesics (for test particles) or to satisfy the EIH equations (for mutually gravitating bodies).

In other words, the four Bianchi identities reduce the ten independent field equations to six, and the four "redundant" equations are precisely the equations of motion.

### V. Higher-Order Extensions

The EIH method can be extended systematically to higher post-Newtonian orders:

- **2PN** ($v^4/c^4$): Computed by Ohta et al. (1974) and Damour and Deruelle (1981).
- **2.5PN** ($v^5/c^5$): The first dissipative order -- this is where gravitational radiation reaction appears. Energy is lost to gravitational waves:

$$\dot{E}_{GW} = -\frac{G}{5c^5}\langle\dddot{Q}_{ij}\dddot{Q}_{ij}\rangle$$

where $Q_{ij}$ is the mass quadrupole moment.

- **3PN, 3.5PN, ... up to ~5PN**: Required for LIGO/Virgo gravitational wave template construction for compact binary inspiral.

---

## Physical Interpretation

### Motion from Geometry

The EIH result embodies the deepest insight of general relativity: there is no separate "law of motion." The geometry (field equations) is everything. Bodies move as they do because the gravitational field -- which they themselves source -- leaves them no other option. Motion is not imposed on spacetime; it is a consequence of the internal consistency of spacetime's geometry.

This is unlike any other theory in physics. In electrodynamics, the Maxwell equations determine the field and the Lorentz force law determines the motion -- they are separate postulates. In GR, the Einstein equations alone suffice.

### The Strong Equivalence Principle

The EIH equations show that the motion of a body depends only on its mass and velocity (at 1PN), not on its internal structure or composition. A neutron star and a black hole of the same mass follow the same orbit (at this order). This is the strong equivalence principle -- the universality of gravitational dynamics extends to self-gravitating bodies.

At higher orders, internal structure effects appear: spin-orbit coupling (1.5PN), spin-spin coupling (2PN), and tidal deformability (5PN). These effects are small corrections that depend on the nature of the compact object.

### The Effacement Property

Damour (1983) generalized the EIH result to show that the internal structure of compact bodies is "effaced" at low post-Newtonian orders -- it does not affect the orbital dynamics. This effacement property is a strong prediction of GR that can be tested with binary pulsar observations. The Hulse-Taylor pulsar timing agrees with the "effaced" prediction to better than 0.2%.

---

## Impact and Legacy

### Binary Pulsars

The discovery of the Hulse-Taylor binary pulsar PSR B1913+16 (1974) provided the first precision test of the EIH framework (and its extensions) for strongly gravitating bodies. The observed orbital decay, due to gravitational wave emission at 2.5PN order, matches the GR prediction to within 0.2%. Hulse and Taylor received the 1993 Nobel Prize.

### Gravitational Wave Astronomy

The LIGO/Virgo detection of gravitational waves from compact binary mergers (2015-present) relies crucially on the post-Newtonian expansion initiated by EIH. The gravitational waveform templates used for matched filtering are computed using the post-Newtonian equations of motion (for the inspiral phase), numerical relativity (for the merger), and black hole perturbation theory (for the ringdown).

The inspiral waveform is:

$$h(t) \propto \frac{(G\mathcal{M})^{5/4}}{c^4 d_L}\left(\frac{t_c - t}{5G\mathcal{M}/c^3}\right)^{-1/4}\cos\left[\Phi(t)\right]$$

where $\mathcal{M} = (m_1 m_2)^{3/5}/(m_1 + m_2)^{1/5}$ is the chirp mass and $\Phi(t)$ includes PN corrections to all known orders.

### The Effective One-Body (EOB) Formalism

Buonanno and Damour (1999) developed the EOB approach, which maps the two-body problem in GR to an effective one-body problem in a deformed Schwarzschild geometry. The EOB Hamiltonian encodes the PN expansion to all known orders and provides the most accurate analytical waveform models for gravitational wave data analysis. The EIH equations are the 1PN limit of the EOB Hamiltonian.

### Parameterized Post-Newtonian (PPN) Framework

Will and Nordtvedt (1972) generalized the post-Newtonian expansion to a parameterized form (PPN) that allows systematic tests of alternative theories of gravity. The 10 PPN parameters quantify deviations from GR; all have been measured to be consistent with GR values to high precision.

---

## Connections to Modern Physics

### Numerical Relativity

For the merger phase of compact binaries (where the post-Newtonian expansion breaks down), the full Einstein equations must be solved numerically. The first successful numerical binary black hole merger simulation (Pretorius, 2005; Baker et al., 2006; Campanelli et al., 2006) confirmed the post-Newtonian predictions for the inspiral and provided the merger waveform for the first time.

### Gravitational Self-Force

For extreme mass-ratio inspirals (a small black hole orbiting a supermassive one), the EIH expansion in mass ratio is more useful than the post-Newtonian expansion in velocity. The gravitational self-force program (Mino, Sasaki, and Tanaka 1997; Quinn and Wald 1997) extends the EIH idea to first order in the mass ratio, with the small body's motion perturbed by its own gravitational field scattered off the background geometry.

### The Two-Body Problem in GR

Unlike in Newtonian gravity, the two-body problem in GR has no closed-form solution. The EIH approach provides an approximate analytical solution valid in the weak-field, slow-motion regime. The full solution requires numerical relativity. The interplay between analytical (PN/EOB) and numerical methods is one of the most active areas in gravitational physics.

### Motion and Radiation in Other Theories

The EIH framework has been extended to other theories of gravity (scalar-tensor theories, massive gravity) to compute the predicted orbital dynamics and gravitational radiation. Differences from GR appear at specific PN orders and can be tested observationally. For example, scalar-tensor theories predict dipole gravitational radiation at 1.5PN (absent in GR), which is strongly constrained by binary pulsar observations.
