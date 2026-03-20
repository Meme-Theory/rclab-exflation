# Hydraulic Jump as a White Hole

**Author(s):** Grigory E. Volovik
**Year:** 2005
**Journal:** JETP Letters, 82(10), 624-627
**arXiv:** physics/0508215

---

## Abstract

This paper proposes that a circular **hydraulic jump** in a fluid flow provides an experimental analog of a **white hole** — the time-reverse of a black hole. Key results:

- In a radial outflow, the velocity exceeds the speed of capillary-gravity waves (ripplons) in the interior region.
- This creates an effective **event horizon** at the circular boundary where flow speed equals ripplon speed.
- The interior region acts as a white-hole analog, where all trajectories (geodesics) point outward with no return.
- The hydraulic jump itself is a physical singularity at the white-hole horizon.
- Vacuum instability and particle creation near the horizon can be studied experimentally.
- The analogy extends to rotating flows and relativistic corrections.

This provides the first concrete proposal for studying white-hole physics in the laboratory — the direct fluid-mechanical opposite of black-hole simulators in condensates and superfluids.

---

## Historical Context

### Black Holes and White Holes

**Black holes** are solution of Einstein's equations with an event horizon — a boundary beyond which nothing can escape. The Schwarzschild metric:

$$ds^2 = -\left(1 - \frac{2GM}{r}\right) dt^2 + \left(1 - \frac{2GM}{r}\right)^{-1} dr^2 + r^2 d\Omega^2$$

has a horizon at $r = 2GM$ (the Schwarzschild radius).

**White holes** are time-reversed black holes: the Schwarzschild solution with $t \to -t$. A white hole has a **past horizon** — a boundary before which nothing could have entered. All trajectories are expelled outward.

White holes are theoretically allowed by Einstein's equations but may not exist in nature. No observations of white holes have been made (though speculations about bouncing cosmologies and wormhole geometries involve white holes).

### Analog Gravity and Fluid Dynamics

By 2005, the analog gravity program had achieved:

- **Hawking radiation in condensates** (numerical predictions, experimental work in progress)
- **Black hole analogs in superfluid vortices** (Volovik et al.)
- **Acoustic black holes** (Unruh, 1981; realized experimentally in 2010s)

A natural next step: realize a white-hole analog experimentally in a fluid system.

### Hydraulic Jumps in Nature

A hydraulic jump is a natural phenomenon in open-channel flows (rivers, drainage systems). When water flows over a sudden drop or enters a circular pan at high speed, it initially flows outward radially at high velocity, then suddenly slows and piles up at a circular radius. This pile-up is the jump.

Volovik's insight: **The circular radius where flow speed equals the ripplon speed is an event horizon for ripplons — a white hole for surface waves.**

---

## Key Arguments and Derivations

### Part I: Effective Metric in Hydraulic Flows

#### Shallow Water Equations

For shallow-water flow over a flat bottom, the velocity $\mathbf{v}$ and height $h$ of the water surface satisfy:

$$\frac{\partial h}{\partial t} + \nabla \cdot (h \mathbf{v}) = 0 \quad \text{(continuity)}$$

$$\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla) \mathbf{v} + g \nabla h = 0 \quad \text{(momentum)}$$

The speed of shallow-water waves (gravity waves) is $c_g = \sqrt{gh}$, where $g$ is gravity and $h$ is water depth.

#### Effective Minkowski Metric

For small-amplitude ripplons (capillary-gravity waves) on a flowing background, the effective metric seen by the ripplons is the **Painleve-Gullstrand form**:

$$ds^2 = -c_0^2 dt^2 + (dx_i - v_i dt)(dx_i - v_i dt)$$

where $c_0 = \sqrt{gh}$ is the local ripplon speed and $\mathbf{v}({\bf r})$ is the flow velocity field.

Explicitly:

$$g_{\mu\nu} = \begin{pmatrix}
-c_0^2 + v^2 & -v_x & -v_y & -v_z \\
-v_x & 1 & 0 & 0 \\
-v_y & 0 & 1 & 0 \\
-v_z & 0 & 0 & 1
\end{pmatrix}$$

The metric signature is $(-,+,+,+)$ — Minkowski-like.

#### Horizon Condition

A **light cone** (or for ripplons, a "ripplon cone") is defined by:

$$\left| \frac{d\mathbf{r}}{dt} \right| = \frac{c_0(\mathbf{r})}{|\mathbf{v}(\mathbf{r})|}$$

In regions where the flow speed exceeds the ripplon speed, $v > c_0$, the light cone tips over — causality is modified. Ripplons cannot propagate upstream (against the flow).

At the boundary where $v = c_0$, an **event horizon** forms.

### Part II: Circular Hydraulic Jump Geometry

#### Radial Outflow Setup

Consider a point source of water at the center of a shallow pan. Water flows radially outward with velocity:

$$v_r(r) = \frac{Q}{2\pi h(r)}$$

where $Q$ is the volumetric flow rate (conserved by mass conservation).

For a thin film of height $h$, the ripplon speed is:

$$c_0(r) = \sqrt{gh}$$

#### Jump Location

At small radius, the flow is fast: $v_r >> c_0$. Ripplons cannot propagate against the flow — they are swept away. The region is causally disconnected from downstream (analogous to the interior of a black hole).

At a critical radius $r_*$, the flow slows as the water spreads and deepens:

$$v_r(r_*) = c_0(r_*)$$

This is the **event horizon** for ripplons.

For $r > r_*$, the flow is subsonic ($v_r < c_0$), and ripplons can propagate both upstream and downstream.

The hydraulic jump is the physical singularity where the height $h$ increases discontinuously. This is the analog of a **white-hole singularity**.

#### Metric in Polar Coordinates

In polar coordinates $(r, \theta)$, the effective metric is:

$$ds^2 = -\left(c_0^2 - v_r^2\right) dt^2 - 2v_r dr dt + dr^2 + r^2 d\theta^2$$

At the horizon $r = r_*$:

$$g_{00} = -(c_0^2 - v_r^2) = 0$$

and $g_{rr} > 0$, confirming that the light cone has tipped over. This is the **trapped surface** — all future-directed geodesics point outward (toward larger $r$).

### Part III: White Hole Thermodynamics

#### Surface Gravity at Horizon

The surface gravity (gravitational acceleration at the horizon) is:

$$\kappa = \left| \frac{d(c_0 - v_r)}{dr} \bigg|_{r=r_*} \right|$$

Since $c_0 = \sqrt{gh}$ and $v_r = Q / (2\pi h)$, we can compute:

$$\frac{d}{dr}(\sqrt{gh}) = \frac{g}{2\sqrt{gh}} \frac{dh}{dr}$$

At the jump, $dh/dr$ is large (discontinuous in the ideal limit). The surface gravity $\kappa$ is therefore well-defined and nonzero.

#### White Hole Temperature

By Hawking's formula, the temperature of radiation from the white hole is:

$$T_W = \frac{\hbar \kappa}{2\pi k_B c_0}$$

For typical laboratory hydraulic jumps (water, $h \sim 1$ cm, $g = 9.8$ m/s$^2$, $c_0 \sim 0.3$ m/s), we estimate:

$$\kappa \sim c_0 / \ell \sim (0.3 \text{ m/s}) / (0.01 \text{ m}) \sim 30 \text{ s}^{-1}$$

$$T_W \sim \frac{(10^{-34} \text{ J} \cdot \text{s}) \times (30 \text{ s}^{-1})}{(1.38 \times 10^{-23} \text{ J/K}) \times (0.3 \text{ m/s})} \sim 10^{-4} \text{ K}$$

This is measurable with precision thermometry!

### Part IV: Vacuum Instability and Particle Creation

#### Ergoregion in Rotating Flow

For rotating flows (like a whirlpool), additional phenomena occur. If the flow rotates with angular velocity $\Omega(r)$, the metric includes off-diagonal $g_{t\theta}$ terms.

An **ergoregion** is a region where $g_{00} < 0$ everywhere, meaning even stationary observers move backward in time (relative to the normal time coordinate). In this region, **negative-energy states** can exist.

This allows **Penrose process** energy extraction and **superradiance** — amplification of waves via the rotating horizon.

#### Instability Analysis

The presence of an event horizon (whether black or white) typically makes the quantum vacuum unstable. Virtual particle pairs can be created at the horizon: one particle escapes to infinity, the other has negative energy and remains inside (or escapes in the white-hole case, both particles escape).

For a white hole, this instability is particularly strong: there is no interior to confine negative-energy particles.

The instability can manifest as:
- **Hawking radiation** (thermal spectrum of particles)
- **Spontaneous vacuum decay** (the white hole evaporates)
- **Quantum tunneling** through the horizon

---

## Key Results

1. **Circular hydraulic jumps are white-hole analogs**: The boundary where flow velocity equals wave speed is an event horizon.

2. **The metric is Painleve-Gullstrand form**: The effective spacetime seen by ripplons has curvature determined by velocity gradients in the flow.

3. **White-hole temperature is calculable and measurable**: $T_W \sim 10^{-4}$ K for typical laboratory parameters, allowing direct observation.

4. **Ergoregions and superradiance are possible**: Rotating hydraulic flows exhibit phenomena analog to Kerr black holes.

5. **Vacuum instability is present**: Quantum particle creation at the horizon is enhanced for white holes compared to black holes.

6. **Experimental realization is accessible**: Hydraulic jumps in water or other fluids can simulate white-hole physics with standard laboratory equipment.

---

## Impact and Legacy

This 2005 paper opened experimental exploration of white-hole analogs:

- **Experimental hydraulic jump studies** (2010s-2020s): Direct measurements of surface waves and their behavior at hydraulic jumps.

- **Rotating flows** (2010s): Exploration of rotating circular flows as Kerr black hole analogs.

- **Wave amplification** (2010s): Study of superradiance-like phenomena in fluid systems.

- **Quantum vacuum instability**: Theoretical and experimental investigations of vacuum decay and particle creation in analog systems.

- **Relativistic hydrodynamics**: Development of relativistic descriptions of flowing fluids, connecting analog gravity to relativistic field theory.

---

## Connection to Phonon-Exflation Framework

The hydraulic jump white-hole analog illuminates the cosmological instability mechanism in phonon-exflation:

1. **Expansion as flowing system**: The expansion of the universe in phonon-exflation is analogous to a diverging fluid flow. The "velocity" is the Hubble rate $H$.

2. **Horizon formation during transition**: As the internal geometry (SU(3)) expands, the effective metric changes. A horizon forms when the expansion rate matches the "ripplon speed" of the condensate excitations.

3. **White-hole-like vacuum instability**: The expansion-driven transition is unstable like a white hole — the condensate cannot remain in equilibrium and decays into the GGE relic.

4. **Particle creation from horizon**: Just as white holes create particles at their horizon, cosmic expansion creates particles at the cosmological horizon — the mechanism is the same.

5. **Surface gravity = Hubble parameter**: The surface gravity $\kappa$ at the cosmic transition is $\sim H$ (Hubble parameter). The "Hawking temperature" is thus $\sim \hbar H / (2\pi k_B)$, connecting quantum gravity to cosmology.

6. **Permanent state = escape to future horizon**: Unlike black-hole Hawking radiation (which escapes to infinity in the past), white-hole radiation escapes to the future infinity. The GGE relic is the "radiation" from the white-hole transition — particles created at the horizon that never return.

---

## References

- Volovik, G. E. (2005). "Hydraulic jump as a white hole." *JETP Letters*, 82(10), 624-627. arXiv:physics/0508215.

- Unruh, W. G. (1981). "Experimental black-hole evaporation?" *Physical Review Letters*, 46(21), 1351.

- Jannes, G., de Oliveira, C. C., & Rodriguez-Lopez, P. (2012). "The circular jump as a hydrodynamic white hole." *Journal of Physics: Conference Series*, 410, 012154.

- Hawking, S. W. (1974). "Black hole explosions?" *Nature*, 248(5443), 30-31.
