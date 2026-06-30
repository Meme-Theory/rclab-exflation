# Acoustic Black Holes: Horizons, Ergospheres, and Hawking Radiation

**Author(s):** Matt Visser
**Year:** 1998
**Journal:** Classical and Quantum Gravity 15 (1998) 1767
**arXiv:** gr-qc/9712010
**Relevance:** CRITICAL

---

## Abstract

It is a deceptively simple question to ask how acoustic disturbances propagate in a non-homogeneous flowing fluid. Subject to suitable restrictions, this question can be answered by invoking the language of Lorentzian differential geometry. I begin this paper with a pedagogical derivation of the following result: If the fluid is barotropic and inviscid, and the flow is irrotational (though possibly time dependent), then the equation of motion for the velocity potential describing a sound wave is identical to that for a minimally coupled massless scalar field propagating in a (3+1)-dimensional Lorentzian geometry $\Delta\psi \equiv \frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,g^{\mu\nu}\partial_\nu\psi) = 0$. The acoustic metric $g_{\mu\nu}(t,\mathbf{x})$ governing the propagation of sound depends algebraically on the density, flow velocity, and local speed of sound. Even though the underlying fluid dynamics is Newtonian, non-relativistic, and takes place in flat space plus time, the fluctuations (sound waves) are governed by an effective (3+1)-dimensional Lorentzian space-time geometry. This rather simple physical system exhibits a remarkable connection between classical Newtonian physics and the differential geometry of curved (3+1)-dimensional Lorentzian spacetimes, and is the basis underlying a deep and fruitful analogy between the black holes of Einstein gravity and supersonic fluid flows. Many results and definitions can be carried over directly from one system to another.

---

## Key Arguments and Derivations

### Derivation of the Acoustic Metric

Starting from the fundamental equations of fluid dynamics -- the continuity equation $\partial_t\rho + \nabla\cdot(\rho\mathbf{v}) = 0$ and Euler's equation $\rho\,d\mathbf{v}/dt = -\nabla p - \rho\nabla\phi - \rho\nabla\Phi$ (where $\phi$ is the Newtonian gravitational potential and $\Phi$ is an external driving potential) -- Visser assumes the fluid is inviscid, barotropic ($\rho = \rho(p)$), and irrotational ($\mathbf{v} = -\nabla\psi$). The Euler equation then reduces to Bernoulli's equation: $-\partial_t\psi + h + \frac{1}{2}(\nabla\psi)^2 + \phi + \Phi = 0$.

Linearizing around background $(p_0, \rho_0, \psi_0)$ with $\psi = \psi_0 + \epsilon\psi_1$, combining the linearized continuity and Euler equations, and defining $c^{-2} = \partial\rho/\partial p$, the wave equation for $\psi_1$ is rewritten as $\partial_\mu(f^{\mu\nu}\partial_\nu\psi_1) = 0$ where:
$$f^{\mu\nu} = \frac{\rho_0}{c^2}\begin{pmatrix} -1 & -v_0^j \\ -v_0^i & c^2\delta^{ij} - v_0^i v_0^j \end{pmatrix}$$

Identifying $\sqrt{-g}\,g^{\mu\nu} = f^{\mu\nu}$ and computing the determinant $\det(f^{\mu\nu}) = -\rho_0^4/c^2$, the acoustic metric is:
$$g_{\mu\nu} = \frac{\rho_0}{c}\begin{pmatrix} -(c^2 - v_0^2) & -v_0^j \\ -v_0^i & \delta_{ij} \end{pmatrix}$$

with acoustic line element $ds^2 = \frac{\rho_0}{c}[-c^2\,dt^2 + \delta_{ij}(dx^i - v_0^i\,dt)(dx^j - v_0^j\,dt)]$.

### Ergo-regions and Horizons

**Ergo-region:** $g_{tt} = -(c^2 - v^2)$ changes sign when $\|\mathbf{v}\| > c$. Any supersonic region is an ergo-region.

**Trapped surfaces:** Closed 2-surfaces where the inward-pointing normal component of fluid velocity exceeds the local speed of sound everywhere.

**Event horizon:** Boundary of the region from which phonons (null geodesics) cannot escape. In stationary geometries, the apparent and event horizons coincide.

### Vortex Geometry (Draining Bathtub)

For a (2+1)-dimensional flow with a sink at the origin, the velocity potential $\psi(r,\theta) = A\ln(r/a) + B\theta$ gives $\mathbf{v} = (A\hat{r} + B\hat{\theta})/r$. The acoustic metric becomes:
$$ds^2 = -c^2\,dt^2 + \left(dr - \frac{A}{r}dt\right)^2 + \left(r\,d\theta - \frac{B}{r}dt\right)^2$$

The ergosphere forms at $r_{\mathrm{ergo}} = \sqrt{A^2 + B^2}/c$ and the event horizon at $r_{\mathrm{horizon}} = |A|/c$. For $A < 0$: future (black hole) horizon; for $A > 0$: past (white hole) horizon. This is distinct from a spinning cosmic string metric.

### Painleve-Gullstrand Connection

The acoustic metric is naturally in Painleve-Gullstrand form. Setting $c$ constant, $v = \sqrt{2GM/r}$, and using continuity to get $\rho \propto r^{-3/2}$, the acoustic metric is conformal to the Painleve-Gullstrand form of Schwarzschild:
$$ds^2 \propto r^{-3/2}\left[-dt^2 + \left(dr \pm \sqrt{\frac{2GM}{r}}\,dt\right)^2 + r^2\,d\Omega^2\right]$$

The conformal factor is irrelevant for surface gravity and Hawking temperature (which are conformal invariants), so the Hawking radiation analysis is fully valid.

### Canonical Acoustic Black Hole

For incompressible fluid with spherical symmetry: $v = c\,r_0^2/r^2$. The acoustic metric in Schwarzschild-like coordinates is:
$$ds^2 = -c^2[1 - (r_0/r)^4]\,d\tau^2 + \frac{dr^2}{1 - (r_0/r)^4} + r^2\,d\Omega^2$$

This is not a standard GR geometry but is the canonical acoustic black hole. A time-dependent version is physically realized by the acoustic metric around a spherically symmetric bubble with oscillating radius ($r_0 = R\sqrt{\dot{R}/c}$), and cavitating bubbles can reach Mach 10.

### Surface Gravity and Hawking Radiation

**Static case:** Setting up fiducial observers (FIDOs) with $V_{\mathrm{FIDO}} = K/\|K\|$, computing their 4-acceleration, and taking the limit $|v| \to c$:
$$g_H = \frac{1}{2}\frac{\partial(c^2 - v^2)}{\partial n}\bigg|_H = c\frac{\partial(c - v_\perp)}{\partial n}\bigg|_H$$

This generalizes Unruh's result to position-dependent speed of sound.

**General stationary case:** The surface gravity is computed via the horizon-generating null vector field $L^\mu = (1; v_\parallel^i)$, using $L^\alpha\nabla_\alpha L^\mu|_H = g_H(L^\mu/c_s)|_H$, yielding the same formula.

**Static condition:** An acoustic geometry is static (not merely stationary) if $\nabla \times [\mathbf{v}/(c^2 - v^2)] = 0$, i.e., $\mathbf{v} \times \nabla(c^2 - v^2) = 0$. This requires either parallel flow and acceleration, or the Chaplygin gas equation of state $p = -k\rho^{-1} + C$.

---

## Key Results

1. The acoustic metric theorem: linearized sound in a barotropic, inviscid, irrotational fluid satisfies the curved-space d'Alembertian with an algebraically determined Lorentzian metric.
2. The acoustic metric naturally appears in Painleve-Gullstrand (ADM) form, providing a direct bridge to black hole physics.
3. An acoustic Schwarzschild geometry can be achieved only up to a conformal factor; exact reproduction is incompatible with the continuity equation.
4. Surface gravity formula generalized to position-dependent speed of sound: $g_H = \frac{1}{2}\partial_n(c^2 - v_\perp^2)|_H$.
5. Vortex geometries (draining bathtub) distinguish between ergosphere and event horizon, analogous to rotating black holes.
6. The canonical acoustic black hole ($v \propto 1/r^2$) has a metric distinct from any standard GR solution, with horizon at $r = r_0$.
7. Cavitating bubbles provide a time-dependent version of the canonical acoustic black hole, physically achievable at Mach 10.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Continuity equation | $\partial_t\rho + \nabla\cdot(\rho\mathbf{v}) = 0$ | Eq. (5) |
| Euler equation | $\rho[(\partial_t\mathbf{v}) + (\mathbf{v}\cdot\nabla)\mathbf{v}] = -\nabla p - \rho\nabla\phi - \rho\nabla\Phi$ | Eq. (6) |
| Bernoulli equation | $-\partial_t\psi + h + \frac{1}{2}(\nabla\psi)^2 + \phi + \Phi = 0$ | Eq. (10) |
| Speed of sound | $c^{-2} = \partial\rho/\partial p$ | Eq. (19) |
| Inverse metric density | $f^{\mu\nu} = (\rho_0/c^2)\mathrm{diag}(-1, c^2\delta^{ij} - v_0^i v_0^j)$ + off-diag | Eq. (20) |
| Acoustic metric (covariant) | $g_{\mu\nu} = (\rho_0/c)\begin{pmatrix} -(c^2 - v_0^2) & -v_0^j \\ -v_0^i & \delta_{ij}\end{pmatrix}$ | Eq. (28) |
| Acoustic line element | $ds^2 = (\rho_0/c)[-c^2\,dt^2 + (dx^i - v_0^i\,dt)\delta_{ij}(dx^j - v_0^j\,dt)]$ | Eq. (29) |
| Stable causality | $g^{\mu\nu}(\nabla_\mu t)(\nabla_\nu t) = -1/(\rho_0 c) < 0$ | Eq. (31) |
| Ergo-region | $g_{tt} = -(c^2 - v^2)$ changes sign at $\|v\| > c$ | Eq. (35) |
| Draining bathtub metric | $ds^2 = -c^2\,dt^2 + (dr - \frac{A}{r}dt)^2 + (r\,d\theta - \frac{B}{r}dt)^2$ | Eq. (41) |
| Painleve-Gullstrand | $ds^2 = -dt^2 + (dr \pm \sqrt{2GM/r}\,dt)^2 + r^2\,d\Omega^2$ | Eq. (49) |
| Canonical acoustic BH | $ds^2 = -c^2[1 - (r_0/r)^4]\,d\tau^2 + \frac{dr^2}{1-(r_0/r)^4} + r^2\,d\Omega^2$ | Eq. (57) |
| Surface gravity (static) | $g_H = \frac{1}{2}\partial_n(c^2 - v^2)\big|_H$ | Eq. (70) |
| Static condition | $\nabla \times [\mathbf{v}/(c^2 - v^2)] = 0$ | Eq. (64) |

---

## Relevance to Phonon-Exflation

This is the original rigorous derivation of the acoustic metric that the phonon-exflation framework builds upon. Visser's theorem establishes that phononic excitations of any barotropic, inviscid, irrotational substrate propagate on a curved Lorentzian geometry -- the mathematical foundation for treating particles as phonons of M4 x SU(3). The Painleve-Gullstrand connection is directly relevant: the framework's effective spacetime is naturally in this form, where the "flow velocity" is determined by the internal fiber dynamics. The surface gravity formula generalizes to position-dependent $c_s$, which is essential when the speed of sound varies with the fiber modulus $\tau$. The vortex geometry section provides the template for understanding rotational features (ergo-regions) that arise when the fiber has angular momentum or vorticity.
