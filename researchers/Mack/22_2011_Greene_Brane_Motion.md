# Brane-World Motion in Compact Dimensions

**Author(s):** Brian Greene, Janna Levin, Maulik Parikh
**Year:** 2011
**Journal/ArXiv:** arXiv:1103.2174

---

## Abstract

The topology of extra dimensions can break global Lorentz invariance, singling out a globally preferred frame even in flat spacetime. Through experiments that probe global topology, an observer can determine her state of motion with respect to the preferred frame. This scenario is realized if we live on a brane universe moving through flat space with compact extra dimensions. The authors identify three experimental effects due to the motion of our universe that could potentially be detected using gravitational probes: (1) peculiar properties of the twin paradox in multiply-connected spacetimes, (2) modifications to Kaluza-Klein mode boundary conditions, and (3) modifications to the Newtonian potential on a moving brane.

---

## Historical Context

The question of whether absolute motion is observable in special relativity is resolved differently on manifolds with nontrivial topology. On infinite flat Minkowski space R^n with Lorentz metric, relativity of motion holds: no experiment can distinguish an inertial observer at rest from one in uniform motion.

However, compact extra dimensions alter this picture fundamentally. When extra dimensions are compactified by identifying coordinates (e.g., y ~ y + L), the identification direction picks out a preferred spatial axis. This breaks global Lorentz invariance while preserving local Lorentz invariance (the metric is locally Minkowski).

The implications are striking: the twin paradox on cylindrical spacetime (product of circle and time) can be resolved without acceleration. Both twins follow geodesics, yet they age differently when they reunite. This signals a preferred frame.

The paper extends this observation to brane cosmology: if our 4D universe is a brane moving through flat extra dimensions (as in ADD models), then the topology of the compactification picks out an absolute rest frame for the brane. Brane observers can experimentally determine their velocity through the extra dimensions.

---

## Key Arguments and Derivations

### Lorentz Invariance Breaking from Topology

Consider 2D Minkowski spacetime with topology R x S^1 (time x circle):

$$ds^2 = -dt^2 + dy^2$$

with identification y ~ y + L. Despite the Minkowski metric (which is locally Lorentz-symmetric), the identification breaks global Lorentz symmetry by singling out the y-direction.

For a preferred observer O at rest (with worldline orthogonal to y-axis), light signals sent around the circle return in time L. For a boosted observer O' moving with velocity beta in the +y direction, massless probes sent in opposite directions return at different times:

$$t'_A = \frac{L}{\gamma(1+\beta)} \quad t'_B = \frac{L}{\gamma(1-\beta)}$$

where gamma = 1/sqrt(1-beta^2). The return times differ, and the observer can deduce:

$$\beta = \frac{s' |\tau_{\text{long}} - \tau_{\text{short}}|}{\tau_{\text{long}} + \tau_{\text{short}}}$$

Thus observers measure absolute velocity by sending light around the compact dimension.

### Einstein Synchronization Failure

In the preferred frame, clocks at different points along the circle can be synchronized globally using Einstein's method (exchanging light signals). But for moving observers O', synchronization fails: light propagates with different speeds in the two directions around the circle (due to Doppler), yielding inconsistent synchronization.

In primed (moving) coordinates, the identification becomes:

$$t' \sim t' - \gamma\beta L, \quad y' \sim y' + \gamma L$$

This mixes time and space. A globally continuous time coordinate is impossible for moving observers; discontinuities in time arise at arbitrary points (analogous to the International Date Line on Earth).

### Brane-World Setup

Consider a 3-brane (our 4D universe) embedded in 5D flat space with compact extra dimension:

$$ds^2 = -dt^2 + d\vec{x}^2 + dy^2$$

with y ~ y + L. The brane is located at y = beta*t (for a moving brane with constant velocity beta).

In brane coordinates (t', x', y'), the identification is:

$$t' \sim t' - \gamma\beta L, \quad y' \sim y' + \gamma L$$

This leads to three measurable effects.

### Effect 1: Time-Delayed Fireworks

When bulk particles (e.g., gravitons) are produced at the LHC on the moving brane, they escape into the extra dimension and return at different times. If the brane is stationary, particles moving in opposite directions return simultaneously. If the brane is moving, they return at times:

$$t_{\text{long}} = \frac{\tau_{\text{long}}}{\gamma}, \quad t_{\text{short}} = \frac{\tau_{\text{short}}}{\gamma}$$

where tau_long/short are proper times. The difference

$$\Delta \tau = \tau_{\text{long}} - \tau_{\text{short}}$$

encodes the brane velocity. Including tangential displacement x_long and x_short:

$$\beta = \frac{\sqrt{(\tau_{\text{long}}^2 - \tau_{\text{short}}^2) - (x_{\text{long}}^2 - x_{\text{short}}^2)}}{\sqrt{(\tau_{\text{long}} + \tau_{\text{short}})^2 - (x_{\text{long}} - x_{\text{short}})^2} \sqrt{(\tau_{\text{long}} + \tau_{\text{short}})^2 - (x_{\text{long}} + x_{\text{short}})^2}}$$

The brane's absolute velocity is measurable via timing of multiple graviton return vertices.

### Effect 2: Split Kaluza-Klein Tower

For Kaluza-Klein modes (treating gravitons as waves), the dispersion relation in the preferred frame is:

$$\omega^2 = k^2 + m^2 + \left(\frac{2\pi n}{L}\right)^2$$

with n integer. Left and right-moving modes (n > 0 and n < 0) are degenerate.

In the moving frame, the boundary condition becomes:

$$\gamma\beta \omega' + \gamma q' = \frac{2\pi n}{L} = q$$

This mixes the temporal and spatial momentum components. The dispersion relation becomes:

$$\omega' = \gamma\sqrt{k'^2 + m^2 + \left(\frac{2\pi n}{L}\right)^2 - \beta \frac{2\pi n}{L} \gamma}$$

For massless modes with small k':

$$\omega'_{\text{right}} \approx \frac{2\pi n}{\gamma L(1-\beta)} \quad (n > 0)$$
$$\omega'_{\text{left}} \approx \frac{2\pi |n|}{\gamma L(1+\beta)} \quad (n < 0)$$

The Kaluza-Klein tower splits into two towers with different spacings:

$$\Delta \omega_{\text{right}} = \frac{2\pi}{\gamma L(1-\beta)}, \quad \Delta \omega_{\text{left}} = \frac{2\pi}{\gamma L(1+\beta)}$$

As beta -> 1, right-moving modes become easier to excite (omega -> 0), left-moving modes harder (omega -> infinity).

### Effect 3: Modified Newtonian Potential

The Newtonian gravitational potential on the moving brane, derived from the graviton propagator with periodic boundary conditions, is:

$$V_{\text{brane}}(r) = -\frac{Gm_1 m_2}{\gamma Lr} \frac{1 + e^{-2\pi r/(\gamma L)}}{1 - e^{-2\pi r/(\gamma L)}}$$

At short distances r << gamma*L:

$$V_{\text{brane}}(r) \approx -\frac{G m_1 m_2}{\pi r^2}$$

which is the 5D Newtonian potential. At large distances r >> gamma*L:

$$V_{\text{brane}}(r) \approx -\frac{G m_1 m_2}{\gamma L r}$$

This is the 4D potential with an effective Newton constant:

$$G_N = \frac{G}{\gamma L}$$

**Key insight**: The effective size of the extra dimension is NOT L but gamma*L. For a moving brane, the Lorentz factor magnifies the apparent size of the compact dimension.

This occurs because, in the moving observer's tilted spatial slices, the identification loop extends over proper length gamma*L, not L.

---

## Key Results

1. **Global Lorentz breaking from topology alone**: Even in flat spacetime with Minkowski metric, compact topology breaks global Lorentz invariance and selects a preferred frame.

2. **Brane velocity is measurable**: Observers on a moving brane can determine absolute velocity through timing of bulk particle returns and gravitational measurements.

3. **Graviton travel time splitting**: Left and right-moving gravitons return at different times; the difference encodes brane velocity. Multiple events yield beta via equation (12).

4. **Kaluza-Klein spectrum splits**: The two-fold degeneracy of the standard KK tower is lifted. Spacings become (1+/-beta)^{-1} times the unperturbed spacing.

5. **Newtonian potential modified**: Deviation from 1/r form occurs at length scale gamma*L, not L. Moving observer measures effective N.C. as G_N = G/(gamma*L).

6. **Small ED detection possible**: Even millimeter-scale extra dimensions become detectable if brane moves at ultra-relativistic speed (gamma >> 1).

7. **Backreaction constraint**: For backreaction to be negligible, brane tension T_0 and Lorentz factor gamma must satisfy (gamma T_0 / l_Planck^4) << 1.

---

## Impact and Legacy

This paper established that brane motion in compact extra dimensions is not merely a theoretical curiosity but has observable signatures. The work opened avenues for testing higher-dimensional cosmology via precision gravity measurements and collider searches for displaced vertices.

The modification to the Newtonian potential offers a new window: even if extra dimensions are small (TeV-scale or smaller), an ultra-relativistic brane could render them observable. This challenges the common assumption that small extra dimensions are permanently hidden.

The paper also deepened understanding of how topology interacts with physics: global properties of spacetime can break symmetries that are locally present. This insight is relevant to topological defects, cosmic strings, and domain walls in cosmology.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework posits that M4 x SU(3) is the fundamental geometry, with Standard Model particles as phononic excitations. The connection to this paper's work is subtle but important:

1. **Topology breaks symmetries**: Just as compact topology in this paper breaks global Lorentz invariance, the topology of SU(3) fiber breaks U(1)_Y globally and selects a preferred orientation. Observers embedded in the M4 x SU(3) spacetime cannot perform experiments to detect motion "through" SU(3) the way this paper describes, because Standard Model fields are confined to the M4 brane. However, dark sectors (dark matter, dark energy) could probe the fiber.

2. **Brane confinement mechanism**: The paper's framework (flat space + moving brane) provides a structural analogy to the phonon-exflation picture: Standard Model fields are confined to an effective 4D "brane" in M4 x SU(3), unable to excite fiber modes (large mass gap).

3. **Effective coupling suppression**: The paper shows gravity is suppressed by the volume factor V ~ gamma*L in the Kaluza-Klein picture, yielding G_N = G/(gamma*L). Similarly, in phonon-exflation, Standard Model couplings are suppressed by SU(3) fiber structure and spectral geometry.

4. **Dark matter as fiber excitations**: The framework predicts dark matter could be quasiparticle excitations of the fiber, distinct from Standard Model phonons. This paper's split Kaluza-Klein tower suggests multiple distinct towers of excitations, analogous to light vs. heavy sectors.

However, the paper does not address the spectral action principle or how Dirac eigenvalues determine particle masses. The phonon-exflation framework fills this gap by connecting geometry to particle physics via NCG.
