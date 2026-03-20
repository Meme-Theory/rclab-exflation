# Schwarzschild's Interior Solution (1916)

## On the Gravitational Field of a Sphere of Incompressible Fluid According to Einstein's Theory

**Original title:** *Uber das Gravitationsfeld einer Kugel aus inkompressibler Flussigkeit nach der Einsteinschen Theorie*

**Author:** Karl Schwarzschild
**Communicated to:** Sitzungsberichte der Koniglich Preussischen Akademie der Wissenschaften zu Berlin
**Date:** 24 February 1916
**Pages:** 424--434
**English translation:** S. Antoci, arXiv:physics/9912033

---

## 1. Historical Context and Significance

Karl Schwarzschild communicated this paper -- his second on Einstein's gravitational theory -- from the Eastern Front during World War I, only weeks before his death on 11 May 1916. It followed his first paper of January 1916, which gave the exact vacuum solution (the exterior Schwarzschild metric) for the gravitational field outside a spherical mass.

This second paper provides the **exact interior solution**: the spacetime geometry *inside* a static, spherically symmetric sphere composed of a perfect fluid with uniform (constant) energy density. It was the **first static spherically symmetric perfect fluid solution** ever found in general relativity.

Einstein wrote to Schwarzschild upon receiving the work: *"I have read your paper with the utmost interest. I had not expected that one could formulate the exact solution of the problem in such a simple way. I liked very much your mathematical treatment of the subject."*

The interior solution is physically significant because it:

- Provides an exact, closed-form model of a relativistic star
- Establishes the first rigorous junction between a matter-filled interior and a vacuum exterior in GR
- Yields the maximum compactness bound later formalised by Buchdahl (1959)
- Remains the foundational reference model for neutron star structure

---

## 2. Physical Setup

### 2.1 Assumptions

1. **Static spacetime:** The metric is time-independent; there exists a timelike Killing vector field $`\xi^\mu = \delta^\mu_t`$.
2. **Spherical symmetry:** The spacetime admits an SO(3) isometry group acting on spacelike 2-spheres.
3. **Perfect fluid matter:** The stress-energy tensor takes the form of a perfect fluid with no viscosity or heat conduction.
4. **Uniform (constant) energy density:** $`\rho = \text{const}`$ throughout the fluid sphere. This corresponds to an incompressible fluid in the relativistic sense.
5. **Zero surface pressure:** $`p(r = R) = 0`$, defining the surface of the star at Schwarzschild radial coordinate $`r = R`$.
6. **Regularity at the centre:** All physical quantities remain finite at $`r = 0`$ (subject to the Buchdahl bound).

### 2.2 The Stress-Energy Tensor

For a perfect fluid, the stress-energy tensor is:

```
T^{\mu\nu} = (\rho c^2 + p) u^\mu u^\nu + p g^{\mu\nu}
```

where:
- $`\rho`$ is the (constant) mass-energy density
- $`p = p(r)`$ is the isotropic pressure, a function of radial coordinate only
- $`u^\mu`$ is the 4-velocity of the fluid element (purely timelike for a static configuration)

In the rest frame of the fluid, the mixed components reduce to:

```
T^\mu_{\ \nu} = \text{diag}(-\rho c^2,\ p,\ p,\ p)
```

The isotropy of the spatial diagonal components (all equal to $`p`$) reflects the perfect fluid assumption: no shear stresses exist.

---

## 3. The Metric Ansatz

### 3.1 General Static Spherically Symmetric Form

The most general static, spherically symmetric line element can be written in Schwarzschild (curvature) coordinates as:

```
ds^2 = -e^{2\Phi(r)} c^2 dt^2 + e^{2\Lambda(r)} dr^2 + r^2 (d\theta^2 + \sin^2\theta\, d\varphi^2)
```

where $`\Phi(r)`$ and $`\Lambda(r)`$ are functions to be determined from the Einstein field equations.

It is conventional to define the **mass function** $`m(r)`$ through:

```
e^{2\Lambda(r)} = \left(1 - \frac{2 G m(r)}{c^2 r}\right)^{-1}
```

so the radial metric component encodes the gravitational mass enclosed within coordinate radius $`r`$.

### 3.2 Notation and Conventions

Throughout this document we use:

| Symbol | Definition |
|--------|-----------|
| $`c`$ | Speed of light in vacuum |
| $`G`$ | Newton's gravitational constant |
| $`\kappa = 8\pi G / c^4`$ | Einstein's gravitational coupling constant |
| $`r_s = 2GM/c^2`$ | Schwarzschild radius of total mass $`M`$ |
| $`R`$ (or $`r_g`$) | Schwarzschild radial coordinate of the star's surface |
| $`M`$ | Total gravitational mass of the sphere |
| $`\rho`$ | Constant mass-energy density |
| $`p(r)`$ | Isotropic pressure as a function of $`r`$ |
| $`\mathcal{R}`$ | Curvature radius parameter: $`\mathcal{R}^2 = 3c^2 / (8\pi G \rho)`$ |

---

## 4. Derivation from the Einstein Field Equations

### 4.1 The Einstein Equations with Perfect Fluid Source

The Einstein field equations are:

```
G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
```

For the static spherically symmetric metric, the independent non-trivial components of the Einstein tensor $`G_{\mu\nu}`$ yield three equations (the $`\theta\theta`$ and $`\varphi\varphi`$ equations are related by spherical symmetry). The Einstein tensor is **diagonal** for this metric, confirming zero shear stress.

### 4.2 The (tt) Component: Mass Equation

The time-time component of the Einstein equations gives:

```
\frac{1}{r^2} \frac{d}{dr}\!\left[r\!\left(1 - e^{-2\Lambda}\right)\right] = \frac{8\pi G}{c^2} \rho
```

This is equivalent to the **mass equation**:

```
\frac{dm}{dr} = \frac{4\pi}{c^2}\, \rho\, c^2\, r^2 = 4\pi \rho\, r^2
```

For constant density $`\rho`$, immediate integration gives:

```
m(r) = \frac{4}{3}\pi \rho\, r^3
```

Therefore the radial metric function is:

```
e^{-2\Lambda(r)} = 1 - \frac{8\pi G \rho}{3 c^2}\, r^2 = 1 - \frac{r^2}{\mathcal{R}^2}
```

where $`\mathcal{R}^2 \equiv 3c^2/(8\pi G\rho) = R^3/r_s`$.

Equivalently:

```
g_{rr} = \left(1 - \frac{r^2}{\mathcal{R}^2}\right)^{-1}
```

This has precisely the geometry of a 3-sphere of radius $`\mathcal{R}`$ in the spatial sections.

### 4.3 The (rr) Component: Pressure-Potential Relation

The radial-radial component gives:

```
e^{-2\Lambda}\!\left(\frac{2\Phi'}{r} + \frac{1}{r^2}\right) - \frac{1}{r^2} = \frac{8\pi G}{c^4}\, p
```

Substituting the known $`e^{-2\Lambda}`$ and rearranging yields a relationship between $`\Phi'(r)`$ and $`p(r)`$.

### 4.4 The Tolman-Oppenheimer-Volkoff (TOV) Equation

Combining the Einstein equations with the conservation law $`\nabla_\mu T^{\mu\nu} = 0`$ yields the **TOV equation** -- the general-relativistic generalisation of hydrostatic equilibrium:

```
\frac{dp}{dr} = -\frac{(\rho c^2 + p)\left(\frac{4\pi G}{c^2}\, p\, r^3 + G\, m(r)\right)}{c^2\, r^2\left(1 - \frac{2G\,m(r)}{c^2\,r}\right)}
```

For **constant density** $`\rho`$ with $`m(r) = \frac{4}{3}\pi\rho\,r^3`$, this becomes a separable ODE that can be integrated in closed form.

### 4.5 Integration: The Temporal Metric Function

The conservation equation $`\nabla_\mu T^{\mu\nu} = 0`$ for a static perfect fluid reduces to:

```
\frac{d\Phi}{dr} = -\frac{1}{\rho c^2 + p}\,\frac{dp}{dr}
```

This integrates to:

```
e^{\Phi(r)} = A - B\sqrt{1 - \frac{r^2}{\mathcal{R}^2}}
```

where $`A`$ and $`B`$ are constants determined by boundary conditions (junction conditions at $`r = R`$ and regularity).

Applying the boundary conditions (see Section 5), one obtains:

```
e^{\Phi(r)} = \frac{1}{2}\left(3\sqrt{1 - \frac{R^2}{\mathcal{R}^2}} - \sqrt{1 - \frac{r^2}{\mathcal{R}^2}}\right)
```

Equivalently, using $`r_s/R = R^2/\mathcal{R}^2`$:

```
e^{\Phi(r)} = \frac{1}{2}\left(3\sqrt{1 - \frac{r_s}{R}} - \sqrt{1 - \frac{r_s\, r^2}{R^3}}\right)
```

---

## 5. The Interior Schwarzschild Metric

### 5.1 Complete Line Element

Assembling the metric components, the **interior Schwarzschild metric** for $`r \leq R`$ is:

```
ds^2 = -\frac{1}{4}\left(3\sqrt{1 - \frac{r_s}{R}} - \sqrt{1 - \frac{r_s\, r^2}{R^3}}\right)^{\!2} c^2\,dt^2
       + \left(1 - \frac{r_s\, r^2}{R^3}\right)^{\!-1} dr^2
       + r^2\left(d\theta^2 + \sin^2\theta\, d\varphi^2\right)
```

where $`r_s = 2GM/c^2`$ is the Schwarzschild radius of the total mass.

### 5.2 Parametric (Curvature Radius) Form

Defining $`\mathcal{R}^2 = R^3/r_s = 3c^2/(8\pi G\rho)`$:

```
ds^2 = -\frac{1}{4}\left(3\sqrt{1 - \frac{R^2}{\mathcal{R}^2}} - \sqrt{1 - \frac{r^2}{\mathcal{R}^2}}\right)^{\!2} c^2\,dt^2
       + \left(1 - \frac{r^2}{\mathcal{R}^2}\right)^{\!-1} dr^2
       + r^2\,d\Omega^2
```

### 5.3 Angular Parametrisation

Introducing the auxiliary angle $`\eta`$ defined by:

```
\sin\eta = \frac{r}{\mathcal{R}}, \qquad \eta_g = \arcsin\frac{R}{\mathcal{R}} = \arcsin\sqrt{\frac{r_s}{R}}
```

the metric takes the elegant form:

```
ds^2 = -\left(\frac{3\cos\eta_g - \cos\eta}{2}\right)^{\!2} c^2\,dt^2
       + \mathcal{R}^2\,d\eta^2
       + \mathcal{R}^2\sin^2\!\eta\left(d\theta^2 + \sin^2\theta\, d\varphi^2\right)
```

This reveals the spatial geometry as a portion of a **3-sphere** $`S^3`$ of radius $`\mathcal{R}`$, embedded in a 4-dimensional Euclidean space. The coordinate $`\eta`$ is the polar angle on this 3-sphere.

### 5.4 Conformal Flatness

The interior Schwarzschild spacetime has **vanishing Weyl tensor**:

```
C_{\mu\nu\rho\sigma} = 0
```

This means the spacetime is **conformally flat** and can be written in the form:

```
ds^2 = \Omega^2(x^\mu)\,\eta_{\mu\nu}\,dx^\mu\,dx^\nu
```

for an appropriate conformal factor $`\Omega`$ and Minkowski-like coordinates. This is a remarkable property not shared by the exterior Schwarzschild solution.

---

## 6. The Density

The energy density is constant throughout the interior:

```
\rho = \frac{M}{\frac{4}{3}\pi R^3} = \frac{3}{\kappa c^2 \mathcal{R}^2} = \frac{3 c^2}{8\pi G \mathcal{R}^2}
```

where $`\kappa = 8\pi G/c^4`$ is the Einstein gravitational coupling constant. This is simply the total mass divided by the coordinate volume of the sphere.

---

## 7. The Pressure Profile

### 7.1 Pressure as a Function of Radius

The isotropic pressure inside the fluid sphere is:

```
p(r) = \rho c^2 \cdot \frac{\sqrt{1 - \frac{r_s\,r^2}{R^3}} - \sqrt{1 - \frac{r_s}{R}}}{3\sqrt{1 - \frac{r_s}{R}} - \sqrt{1 - \frac{r_s\,r^2}{R^3}}}
```

Equivalently, in the angular parametrisation:

```
p(\eta) = \rho c^2 \cdot \frac{\cos\eta - \cos\eta_g}{3\cos\eta_g - \cos\eta}
```

### 7.2 Properties of the Pressure Profile

1. **Surface:** At $`r = R`$ (i.e. $`\eta = \eta_g`$), $`\cos\eta = \cos\eta_g`$, so:
   ```
   p(R) = \rho c^2 \cdot \frac{\cos\eta_g - \cos\eta_g}{3\cos\eta_g - \cos\eta_g} = 0
   ```
   The pressure vanishes at the surface, as required.

2. **Centre:** At $`r = 0`$ (i.e. $`\eta = 0`$, $`\cos\eta = 1`$), the central pressure is:
   ```
   p_c = p(0) = \rho c^2 \cdot \frac{1 - \cos\eta_g}{3\cos\eta_g - 1}
   ```
   Or equivalently:
   ```
   p_c = \rho c^2 \cdot \frac{1 - \sqrt{1 - r_s/R}}{3\sqrt{1 - r_s/R} - 1}
   ```

3. **Monotonicity:** The pressure is a monotonically decreasing function of $`r`$, with its maximum at the centre and zero at the surface.

4. **Positive definiteness:** For $`r_s/R < 8/9`$, the pressure is positive throughout the interior.

### 7.3 Central Pressure Divergence

The central pressure diverges ($`p_c \to \infty`$) when the denominator vanishes:

```
3\cos\eta_g - 1 = 0 \implies \cos\eta_g = \frac{1}{3}
```

This corresponds to:

```
\sqrt{1 - \frac{r_s}{R}} = \frac{1}{3} \implies 1 - \frac{r_s}{R} = \frac{1}{9} \implies \frac{r_s}{R} = \frac{8}{9}
```

That is:

```
\frac{2GM}{Rc^2} = \frac{8}{9}
```

This is the **Buchdahl limit** -- beyond this compactness, no static configuration of uniform-density incompressible fluid can exist.

---

## 8. Junction Conditions at the Surface r = R

### 8.1 The Exterior Schwarzschild Metric

For $`r > R`$, the spacetime is vacuum and described by the exterior Schwarzschild metric:

```
ds^2_{\text{ext}} = -\left(1 - \frac{r_s}{r}\right) c^2\,dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2\,d\Omega^2
```

### 8.2 Matching Conditions (Darmois-Israel)

At the junction surface $`\Sigma`$ defined by $`r = R`$, the Darmois-Israel junction conditions require:

**First junction condition** -- continuity of the induced metric on $`\Sigma`$:

```
[g_{\mu\nu}]_\Sigma = 0 \quad (\text{no jump in the metric across } \Sigma)
```

**Second junction condition** -- continuity of the extrinsic curvature (equivalently, no surface layer):

```
[K_{ij}]_\Sigma = 0
```

For the Schwarzschild interior/exterior matching, these reduce to three explicit conditions:

**(i) Continuity of $`g_{tt}`$ at $`r = R`$:**

```
\frac{1}{4}\left(3\sqrt{1 - \frac{r_s}{R}} - \sqrt{1 - \frac{r_s}{R}}\right)^{\!2} = 1 - \frac{r_s}{R}
```

This simplifies to:

```
\frac{1}{4}\left(2\sqrt{1 - \frac{r_s}{R}}\right)^2 = 1 - \frac{r_s}{R}  \qquad \checkmark
```

which is identically satisfied, confirming the correct normalisation of the temporal metric function.

**(ii) Continuity of $`g_{rr}`$ at $`r = R`$:**

```
\left(1 - \frac{r_s R^2}{R^3}\right)^{-1} = \left(1 - \frac{r_s}{R}\right)^{-1}
```

This is trivially satisfied since $`r_s R^2/R^3 = r_s/R`$.

**(iii) Continuity of $`g_{rr}'`$ (or equivalently, vanishing surface pressure):**

The condition $`p(R) = 0`$ is equivalent to the smooth matching of the extrinsic curvature. This ensures no thin shell of matter exists at the surface -- the star has a clean boundary.

### 8.3 Physical Interpretation

The junction conditions ensure:

- The coordinate time $`t`$ has the same normalisation inside and outside
- The radial coordinate $`r`$ is continuous and measures the same circumferential radius on both sides
- An observer crossing the surface experiences no discontinuity in tidal forces
- The total mass $`M`$ as measured by distant observers equals the integral $`M = \frac{4}{3}\pi\rho R^3`$

Note that the **proper mass** (integral of $`\rho`$ over the proper volume) exceeds $`M`$ due to the gravitational binding energy. The proper volume element $`\sqrt{g_{rr}}\,r^2\sin\theta\,dr\,d\theta\,d\varphi`$ exceeds the flat-space volume element.

---

## 9. The Buchdahl Limit

### 9.1 Statement

For a static, spherically symmetric perfect fluid sphere with non-increasing energy density ($`d\rho/dr \leq 0`$) and isotropic pressure, the compactness is bounded by:

```
\frac{2GM}{Rc^2} \leq \frac{8}{9}
```

or equivalently:

```
\frac{GM}{Rc^2} \leq \frac{4}{9} \approx 0.444
```

This is the **Buchdahl bound** (H.A. Buchdahl, 1959). For the specific case of uniform density (the Schwarzschild interior solution), the bound is **saturated** -- the uniform density configuration is the most compact possible static fluid sphere.

### 9.2 Derivation from the Interior Solution

The bound follows directly from requiring finite central pressure:

**Step 1.** The central pressure is:

```
p_c = \rho c^2 \cdot \frac{1 - \sqrt{1 - 2GM/(Rc^2)}}{3\sqrt{1 - 2GM/(Rc^2)} - 1}
```

**Step 2.** Physical viability requires $`p_c < \infty`$, hence the denominator must be strictly positive:

```
3\sqrt{1 - \frac{2GM}{Rc^2}} - 1 > 0
```

**Step 3.** Solving:

```
\sqrt{1 - \frac{2GM}{Rc^2}} > \frac{1}{3}
```
```
1 - \frac{2GM}{Rc^2} > \frac{1}{9}
```
```
\frac{2GM}{Rc^2} < \frac{8}{9}
```

### 9.3 Equivalent Formulations

The Buchdahl limit can be expressed in several equivalent ways:

| Form | Expression |
|------|-----------|
| Compactness bound | $`2GM/(Rc^2) < 8/9`$ |
| Radius bound | $`R > (9/8)\,r_s = (9/4)\,GM/c^2`$ |
| Surface redshift bound | $`z_{\text{surf}} < 2`$ |
| Angular parameter bound | $`\eta_g < \arccos(1/3) \approx 70.53°`$ |
| Density-radius relation | $`R^2 < 3c^2/(2\pi G\rho) \cdot (1 - 1/9)`$ |

### 9.4 Gravitational Surface Redshift

A photon emitted from the surface at $`r = R`$ and received at infinity experiences the gravitational redshift:

```
1 + z_{\text{surf}} = \frac{1}{\sqrt{g_{tt}(R)}} = \frac{1}{\sqrt{1 - r_s/R}} = \frac{1}{\cos\eta_g}
```

The Buchdahl bound $`\cos\eta_g > 1/3`$ therefore implies:

```
z_{\text{surf}} < 2
```

This is a **universal upper bound** on the surface redshift of any static, spherically symmetric perfect fluid star with monotonically non-increasing density. It was first derived by Bondi (1964) and Buchdahl.

---

## 10. Proper Volume

The proper 3-volume of the fluid sphere exceeds the Euclidean volume due to spatial curvature:

```
V_{\text{proper}} = \int_0^R \frac{4\pi r^2}{\sqrt{1 - r^2/\mathcal{R}^2}}\,dr
```

Evaluating:

```
V_{\text{proper}} = 2\pi\mathcal{R}^2\left(\mathcal{R}\,\arcsin\frac{R}{\mathcal{R}} - R\sqrt{1 - \frac{R^2}{\mathcal{R}^2}}\right)
```

Or equivalently:

```
V_{\text{proper}} = 2\pi\left(\frac{R^{9/2}\,\arcsin\sqrt{r_s/R}}{r_s^{3/2}} - \frac{R^4\sqrt{1 - r_s/R}}{r_s}\right)
```

This always exceeds $`\frac{4}{3}\pi R^3`$. The ratio $`V_{\text{proper}}/V_{\text{Euclidean}}`$ grows with compactness.

---

## 11. Isotropic Coordinate Form

### 11.1 Coordinate Transformation

The exterior Schwarzschild metric can be transformed to isotropic coordinates $`(t, \bar{r}, \theta, \varphi)`$ via:

```
r = \bar{r}\left(1 + \frac{r_s}{4\bar{r}}\right)^2
```

yielding:

```
ds^2_{\text{ext}} = -\frac{\left(1 - \frac{r_s}{4\bar{r}}\right)^2}{\left(1 + \frac{r_s}{4\bar{r}}\right)^2}\,c^2\,dt^2 + \left(1 + \frac{r_s}{4\bar{r}}\right)^4\!\left(d\bar{r}^2 + \bar{r}^2\,d\Omega^2\right)
```

### 11.2 Interior Isotropic Form

For the interior, the transformation from Schwarzschild coordinates to isotropic coordinates proceeds by requiring the spatial part of the metric to be conformally flat:

```
ds^2_{\text{int}} = -e^{2\Phi(\bar{r})}\,c^2\,dt^2 + \Psi^4(\bar{r})\left(d\bar{r}^2 + \bar{r}^2\,d\Omega^2\right)
```

The coordinate transformation relating the interior Schwarzschild radial coordinate $`r`$ to the isotropic coordinate $`\bar{r}`$ is obtained by requiring:

```
\frac{dr}{\sqrt{1 - r^2/\mathcal{R}^2}} = \Psi^2(\bar{r})\,d\bar{r}
```

The integration yields:

```
r = \mathcal{R}\sin\!\left(C_1 \ln\bar{r} + C_2\right)
```

for integration constants $`C_1`$ and $`C_2`$ determined by boundary matching.

### 11.3 Conformal Flat Form

Since the interior Schwarzschild spacetime is conformally flat ($`C_{\mu\nu\rho\sigma} = 0`$), there exist coordinates $`(T, \mathbf{X})`$ in which the full 4-metric takes the form:

```
ds^2 = \Omega^2(T, |\mathbf{X}|)\left(-c^2\,dT^2 + d\mathbf{X}\cdot d\mathbf{X}\right)
```

The conformal factor has the general structure:

```
\Omega(\bar{t}, \bar{r}) = B\left[\cos\bar{r} \pm \cos(\bar{t} - t_0)\right]
```

where $`B`$ and $`t_0`$ are parameters related to the density and total mass. This form makes manifest the embedding of the constant-time spatial sections as a portion of $`S^3`$.

### 11.4 Subtlety: Non-Uniqueness

Buchdahl (1983) showed that when the interior Schwarzschild solution is expressed in isotropic coordinates, a given density $`\rho`$ and isotropic coordinate radius $`\bar{R}`$ generically correspond to **two distinct physical configurations** with different total masses $`M`$ and different proper radii. This arises from the non-monotonic relationship between the Schwarzschild coordinate $`r`$ and the isotropic coordinate $`\bar{r}`$ in highly compact configurations.

---

## 12. Physical Implications

### 12.1 Maximum Mass for a Given Density

From the Buchdahl bound $`2GM/(Rc^2) < 8/9`$ combined with $`M = (4/3)\pi\rho R^3`$:

```
R < \frac{3c^2}{8\pi G\rho} \cdot \frac{8}{9 \cdot R^2/(R^2)}
```

Solving for the maximum mass:

```
M_{\text{max}} = \frac{4c^2}{9G}\sqrt{\frac{1}{6\pi G\rho}} \cdot c = \frac{4}{9}\sqrt{\frac{3c^6}{32\pi G^3 \rho}}
```

For nuclear density $`\rho_{\text{nuc}} \approx 4 \times 10^{17}\,\text{kg/m}^3`$:

```
M_{\text{max}} \sim 5\text{--}6\, M_\odot
```

This is a **theoretical upper bound** for an incompressible fluid star at nuclear density. Realistic equations of state yield lower maximum masses.

### 12.2 Connection to Neutron Star Physics

The Schwarzschild interior solution, while idealised, provides foundational context for neutron star physics:

1. **Oppenheimer-Volkoff limit (1939):** Oppenheimer and Volkoff used the TOV equation with a degenerate neutron gas equation of state to find a maximum neutron star mass of approximately $`0.7\,M_\odot`$. Modern equations of state, incorporating nuclear interactions, yield $`M_{\text{max}} \approx 2.0\text{--}2.5\,M_\odot`$.

2. **Compactness of observed neutron stars:** Typical neutron stars have $`2GM/(Rc^2) \approx 0.3\text{--}0.6`$, well within the Buchdahl bound of $`8/9 \approx 0.889`$. The most compact observed neutron stars approach $`2GM/(Rc^2) \sim 0.5`$.

3. **Gravitational wave constraints:** The LIGO/Virgo observation of GW170817 (binary neutron star merger) constrained the maximum mass to $`M_{\text{max}} \lesssim 2.17\,M_\odot`$, consistent with theoretical models.

4. **Causality bound:** The incompressible fluid has an infinite speed of sound ($`c_s^2 = dp/d\rho \to \infty`$ since $`\rho = \text{const}`$). Imposing the physical requirement $`c_s \leq c`$ tightens the compactness bound beyond $`8/9`$.

5. **Stability:** The uniform-density model is marginally stable against radial perturbations at the Buchdahl limit. Realistic stellar models must also satisfy dynamical stability criteria.

### 12.3 The Buchdahl Bound as a Black Hole Threshold

The Buchdahl limit establishes a **gap** between the most compact possible static fluid star and a black hole:

```
\text{Most compact star:} \quad R_{\text{min}} = \frac{9}{8}\,r_s = \frac{9}{4}\,\frac{GM}{c^2}

\text{Black hole horizon:} \quad R_{\text{BH}} = r_s = \frac{2GM}{c^2}
```

The ratio is $`R_{\text{min}}/R_{\text{BH}} = 9/8 = 1.125`$. No static perfect fluid configuration can exist with a radius between $`r_s`$ and $`(9/8)\,r_s`$. Any object compressed below the Buchdahl radius must undergo gravitational collapse.

---

## 13. Summary of Key Equations

### The Interior Schwarzschild Solution at a Glance

**Density:**
```
\rho = \frac{3M}{4\pi R^3} = \frac{3c^2}{8\pi G \mathcal{R}^2} = \text{const}
```

**Metric (Schwarzschild coordinates, $`r \leq R`$):**
```
ds^2 = -\frac{c^2\,dt^2}{4}\!\left(3\sqrt{1 - \frac{r_s}{R}} - \sqrt{1 - \frac{r_s r^2}{R^3}}\right)^{\!2}
     + \frac{dr^2}{1 - \frac{r_s r^2}{R^3}} + r^2\,d\Omega^2
```

**Pressure:**
```
p(r) = \rho c^2\,\frac{\sqrt{1 - r_s r^2/R^3} - \sqrt{1 - r_s/R}}{3\sqrt{1 - r_s/R} - \sqrt{1 - r_s r^2/R^3}}
```

**Central pressure:**
```
p_c = \rho c^2\,\frac{1 - \sqrt{1 - r_s/R}}{3\sqrt{1 - r_s/R} - 1}
```

**Buchdahl limit (finite $`p_c`$ requires):**
```
\frac{2GM}{Rc^2} = \frac{r_s}{R} < \frac{8}{9}
```

**Surface redshift bound:**
```
z_{\text{surf}} = \frac{1}{\sqrt{1 - r_s/R}} - 1 < 2
```

**Mass function:**
```
m(r) = \frac{4}{3}\pi\rho\,r^3 = M\frac{r^3}{R^3}
```

**Junction condition:** Both $`g_{tt}`$ and $`g_{rr}`$ and their first derivatives are continuous at $`r = R`$, matching the exterior Schwarzschild vacuum solution with $`p(R) = 0`$.

---

## 14. Relation to Schwarzschild's First Paper (Exterior Solution)

| Property | Exterior (1st paper, Jan 1916) | Interior (2nd paper, Feb 1916) |
|----------|-------------------------------|-------------------------------|
| Domain | $`r > R`$ (vacuum) | $`r \leq R`$ (matter) |
| Matter content | $`T_{\mu\nu} = 0`$ | Perfect fluid, $`\rho = \text{const}`$ |
| Metric, $`g_{tt}`$ | $`-(1 - r_s/r)`$ | $`-\frac{1}{4}(3\sqrt{1-r_s/R} - \sqrt{1-r_sr^2/R^3})^2`$ |
| Metric, $`g_{rr}`$ | $`(1 - r_s/r)^{-1}`$ | $`(1 - r_sr^2/R^3)^{-1}`$ |
| Free parameters | $`M`$ (total mass) | $`\rho`$ (density), $`R`$ (radius) |
| Weyl tensor | $`C_{\mu\nu\rho\sigma} \neq 0`$ | $`C_{\mu\nu\rho\sigma} = 0`$ |
| Singularity | $`r = 0`$ (curvature), $`r = r_s`$ (coordinate) | None (if Buchdahl bound satisfied) |

---

## 15. Bibliographic References

1. **K. Schwarzschild**, *Uber das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie*, Sitzungsber. Preuss. Akad. Wiss. Berlin (Math. Phys.), 189--196 (1916). [Exterior solution]

2. **K. Schwarzschild**, *Uber das Gravitationsfeld einer Kugel aus inkompressibler Flussigkeit nach der Einsteinschen Theorie*, Sitzungsber. Preuss. Akad. Wiss. Berlin (Math. Phys.), 424--434 (1916). [Interior solution -- the subject of this document]

3. **S. Antoci** (translator), *On the gravitational field of a sphere of incompressible fluid according to Einstein's theory*, arXiv:physics/9912033 (1999).

4. **H.A. Buchdahl**, *General Relativistic Fluid Spheres*, Phys. Rev. **116**, 1027--1034 (1959). [Proof of the 8/9 compactness bound for general monotone density profiles]

5. **H.A. Buchdahl**, *Remark on the isotropic form of the Schwarzschild interior metric*, Am. J. Phys. **51**, 4 (1983).

6. **R.C. Tolman**, *Static Solutions of Einstein's Field Equations for Spheres of Fluid*, Phys. Rev. **55**, 364--373 (1939).

7. **J.R. Oppenheimer and G.M. Volkoff**, *On Massive Neutron Cores*, Phys. Rev. **55**, 374--381 (1939).

8. **C.W. Misner, K.S. Thorne, and J.A. Wheeler**, *Gravitation*, W.H. Freeman (1973), Chapter 23.

9. **R.M. Wald**, *General Relativity*, University of Chicago Press (1984), Chapter 6.

10. **S. Weinberg**, *Gravitation and Cosmology*, Wiley (1972), Chapter 11.

---

*This document summarises the content and implications of Schwarzschild's second 1916 paper on general relativity. The interior solution, together with the exterior vacuum solution, constitutes the complete gravitational field of a static, spherically symmetric, uniform-density perfect fluid sphere -- the simplest exact stellar model in Einstein's theory.*
