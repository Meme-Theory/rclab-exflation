# On the Gravitational Field of a Mass Point According to Einstein's Theory

## Schwarzschild, K. (1916). *Uber das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie*

**Sitzungsberichte der Koniglich Preussischen Akademie der Wissenschaften zu Berlin, Phys.-Math. Klasse, 189--196 (1916)**

Communicated by Einstein on January 13, 1916. Received December 22, 1915.

---

## 1. Historical Context

Karl Schwarzschild (1873--1916) was Director of the Astrophysical Observatory in Potsdam and one of the foremost astronomers of his generation when, at the age of 41, he volunteered for military service in the German Army at the outbreak of the First World War in August 1914. He served on both the Western Front (Belgium) and the Eastern Front (Russia), performing ballistic calculations and rising to the rank of second lieutenant in the artillery.

In November 1915, while Schwarzschild was stationed on the Russian Front, Albert Einstein presented the final form of the gravitational field equations to the Prussian Academy of Sciences over a series of four Thursday lectures (November 4, 11, 18, and 25, 1915). The November 25 paper contained the definitive field equations of general relativity:

$$R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = \frac{8\pi G}{c^4} T_{\mu\nu}$$

Einstein had already used an approximate solution to compute the anomalous perihelion precession of Mercury in his November 18 lecture, obtaining the celebrated 43 arcseconds per century. However, Einstein believed the full nonlinear equations to be too difficult for exact solutions to be found.

Schwarzschild proved him wrong within weeks. On **December 22, 1915**, Schwarzschild wrote to Einstein enclosing the first exact solution to the full vacuum field equations -- the exterior gravitational field of a spherically symmetric mass point. Einstein presented the paper to the Prussian Academy on **January 13, 1916**, writing to Schwarzschild:

> "I have read your paper with the utmost interest. I had not expected that one could formulate the exact solution of the problem in such a simple way."

Schwarzschild followed this with a second paper in February 1916, *Uber das Gravitationsfeld einer Kugel aus inkompressibler Flussigkeit nach der Einsteinschen Theorie* ("On the Gravitational Field of a Sphere of Incompressible Fluid"), giving the interior solution for a uniform-density sphere.

Tragically, Schwarzschild had already contracted pemphigus, a rare and painful autoimmune blistering disease, while serving on the Eastern Front. He was invalided home in March 1916 and died on **May 11, 1916**, at the age of 42, having produced two of the most consequential papers in the history of gravitational physics in the final months of his life.

---

## 2. Symmetry Assumptions and the Vacuum Field Equations

### 2.1 Physical Setup

Schwarzschild sought the gravitational field exterior to an isolated, spherically symmetric, non-rotating, uncharged mass $M$ situated in otherwise empty space. The problem is defined by three assumptions:

1. **Spherical symmetry**: The spacetime admits an $SO(3)$ isometry group acting on spacelike 2-spheres.
2. **Staticity**: The spacetime possesses a timelike Killing vector field that is hypersurface-orthogonal (no frame dragging, time-reversal invariant).
3. **Vacuum**: The stress-energy tensor vanishes identically, $T_{\mu\nu} = 0$, so the field equations reduce to the vanishing of the Ricci tensor:

$$R_{\mu\nu} = 0 \tag{1}$$

### 2.2 Einstein's Field Equations in 1915: The Unimodular Restriction

A crucial historical detail: Einstein's November 1915 field equations were presented not in the fully generally covariant form familiar today, but under the restriction that the coordinate system be chosen such that

$$\sqrt{-g} = 1 \tag{2}$$

where $g = \det(g_{\mu\nu})$. This **unimodular coordinate condition** was not a gauge choice in the modern sense but was treated by Einstein as a simplifying structural requirement. The vacuum field equations in this framework reduce to

$$\Gamma^{\alpha}_{\mu\nu,\alpha} + \Gamma^{\alpha}_{\mu\beta} \Gamma^{\beta}_{\nu\alpha} = 0 \tag{3}$$

where $\Gamma^{\alpha}_{\mu\nu}$ are the Christoffel symbols of the second kind. Schwarzschild worked within this unimodular framework, and his derivation reflects it. Einstein abandoned the unimodular restriction by mid-1916, embracing full general covariance in the published version of the theory (*Annalen der Physik*, 1916), but Schwarzschild's paper predates this shift.

---

## 3. Schwarzschild's Original Derivation

### 3.1 The Metric Ansatz

Schwarzschild began with the most general static, spherically symmetric line element in Cartesian-like coordinates $(x, y, z, t)$:

$$ds^2 = F(r)\, dt^2 - G(r)(dx^2 + dy^2 + dz^2) - H(r)(x\, dx + y\, dy + z\, dz)^2 \tag{4}$$

where $r = \sqrt{x^2 + y^2 + z^2}$, and the boundary conditions at spatial infinity require

$$\lim_{r \to \infty} F = 1, \quad \lim_{r \to \infty} G = 1, \quad \lim_{r \to \infty} H = 0 \tag{5}$$

ensuring asymptotic flatness (the Minkowski metric is recovered at infinity).

### 3.2 Schwarzschild's Trick: Unimodular Coordinates

To satisfy the determinant condition $\sqrt{-g} = 1$, Schwarzschild introduced an ingenious coordinate transformation -- his celebrated "trick." He replaced the standard spherical coordinates $(r, \theta, \phi, t)$ with a new set:

$$x_1 = \frac{r^3}{3}, \quad x_2 = -\cos\theta, \quad x_3 = \phi, \quad x_4 = t \tag{6}$$

Under this transformation, the coordinate differentials become:

$$dx_1 = r^2\, dr, \quad dx_2 = \sin\theta\, d\theta, \quad dx_3 = d\phi, \quad dx_4 = dt$$

The line element takes the form:

$$ds^2 = f_4\, dx_4^2 - f_1\, dx_1^2 - f_2 \frac{dx_2^2}{1 - x_2^2} - f_3(1 - x_2^2)\, dx_3^2 \tag{7}$$

where $f_1, f_2, f_3, f_4$ are functions of $x_1$ alone (equivalently, of $r$). The determinant condition becomes:

$$f_1 \cdot f_2^2 \cdot f_4 = 1 \tag{8}$$

This reduces the number of independent metric functions from four to three.

### 3.3 Solution of the Vacuum Field Equations

At the equatorial plane ($x_2 = 0$, i.e., $\theta = \pi/2$), the vacuum conditions $R_{\mu\nu} = 0$ yield three coupled ordinary differential equations for $f_1$, $f_2$, and $f_4$ as functions of $x_1$. These equations, combined with the determinant constraint (8) and the asymptotic boundary conditions, admit a unique solution.

Schwarzschild found, upon rewriting in terms of a new auxiliary radial variable $R$:

$$R^3 = r^3 + \alpha^3 \tag{9}$$

where $\alpha$ is an integration constant determined by the mass. The line element in terms of $R$ is:

$$ds^2 = \left(1 - \frac{\alpha}{R}\right) dt^2 - \frac{dR^2}{1 - \alpha/R} - R^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right) \tag{10}$$

The constant $\alpha$ is identified with the Newtonian limit as:

$$\alpha = \frac{2GM}{c^2} \equiv r_s \tag{11}$$

where $r_s$ is what is now called the **Schwarzschild radius**.

### 3.4 Schwarzschild's Original vs. the Modern (Droste) Form

A point of considerable historical subtlety: in Schwarzschild's original coordinates, the radial variable $R$ defined by (9) satisfies $R = \alpha$ when $r = 0$. That is, **Schwarzschild placed what we now call the event horizon at the origin of his coordinate system** ($r = 0$). His line element is not singular at this origin -- the apparent singularity occurs only at $R = \alpha$, which maps to the physical mass point at $r = 0$.

The Dutch physicist **Johannes Droste** independently derived the same solution in 1916 using a more direct approach, in which the modern radial coordinate $r$ is used directly and the line element takes the now-standard form. What textbooks universally call "the Schwarzschild metric" is actually the Droste form, though priority belongs to Schwarzschild.

---

## 4. The Schwarzschild Metric in Modern Notation

### 4.1 The Line Element

In geometrized units ($G = c = 1$) with the standard Schwarzschild coordinates $(t, r, \theta, \phi)$, the exterior Schwarzschild metric is:

$$\boxed{ds^2 = -\left(1 - \frac{2M}{r}\right) dt^2 + \left(1 - \frac{2M}{r}\right)^{-1} dr^2 + r^2\, d\Omega^2} \tag{12}$$

where $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\phi^2$ is the metric on the unit 2-sphere, and $M$ is the gravitational mass.

In SI units, restoring $G$ and $c$:

$$ds^2 = -\left(1 - \frac{2GM}{rc^2}\right) c^2\, dt^2 + \left(1 - \frac{2GM}{rc^2}\right)^{-1} dr^2 + r^2\, d\Omega^2 \tag{13}$$

### 4.2 The Metric Tensor Components

The metric tensor in the coordinate basis $(t, r, \theta, \phi)$ is diagonal:

$$g_{\mu\nu} = \text{diag}\!\left(-\left(1 - \frac{r_s}{r}\right),\; \left(1 - \frac{r_s}{r}\right)^{-1},\; r^2,\; r^2 \sin^2\theta\right) \tag{14}$$

with determinant:

$$g = \det(g_{\mu\nu}) = -r^4 \sin^2\theta \tag{15}$$

Note that $\sqrt{-g} = r^2 \sin\theta$, which is **not** unity -- the modern Schwarzschild coordinates do not satisfy Einstein's original unimodular condition.

### 4.3 Killing Vectors and Conserved Quantities

The Schwarzschild spacetime admits four independent Killing vector fields:

- $\xi^{\mu}_{(t)} = (\partial/\partial t)^{\mu}$: timelike for $r > r_s$, generating time-translation symmetry. The associated conserved quantity for geodesic motion is the **specific energy**:

$$E = \left(1 - \frac{r_s}{r}\right) \frac{dt}{d\tau} \tag{16}$$

- Three rotational Killing vectors generating $SO(3)$. The conserved **specific angular momentum** is:

$$L = r^2 \frac{d\phi}{d\tau} \tag{17}$$

(restricting to equatorial orbits $\theta = \pi/2$ without loss of generality by spherical symmetry).

---

## 5. Singularity Structure

### 5.1 The Coordinate Singularity at $r = r_s$

The metric components (14) are manifestly singular at

$$r = r_s = \frac{2GM}{c^2} \tag{18}$$

Both $g_{tt} \to 0$ and $g_{rr} \to \infty$ as $r \to r_s$. Schwarzschild himself, and the physics community for decades afterward, regarded this surface as a genuine physical singularity -- the "Schwarzschild singularity" or "magic sphere."

The resolution came in stages:

- **Lemaitre (1933)** showed that the surface $r = r_s$ could be crossed by freely falling observers in finite proper time.
- **Eddington (1924)** and later **Finkelstein (1958)** introduced coordinates that are regular at $r = r_s$:

$$ds^2 = -\left(1 - \frac{r_s}{r}\right) dv^2 + 2\, dv\, dr + r^2\, d\Omega^2 \tag{19}$$

where $v = t + r + r_s \ln|r/r_s - 1|$ is the advanced Eddington-Finkelstein coordinate.

- **Kruskal (1960)** and **Szekeres (1960)** constructed the maximal analytic extension:

$$ds^2 = \frac{32M^3}{r} e^{-r/2M} (-dT^2 + dX^2) + r^2\, d\Omega^2 \tag{20}$$

where $r$ is defined implicitly by $T^2 - X^2 = (1 - r/2M) e^{r/2M}$.

These coordinate systems demonstrate conclusively that $r = r_s$ is a **coordinate singularity**: an artifact of the Schwarzschild coordinate chart, not an intrinsic feature of the geometry. The surface $r = r_s$ is the **event horizon** -- a null hypersurface that acts as a one-way causal membrane.

### 5.2 The Physical Singularity at $r = 0$

The singularity at $r = 0$ is genuine and irremovable. This is established by examining curvature invariants, which are coordinate-independent scalar quantities. The **Kretschmann scalar** is:

$$K = R_{\alpha\beta\gamma\delta} R^{\alpha\beta\gamma\delta} = \frac{48\, G^2 M^2}{c^4\, r^6} = \frac{48\, M^2}{r^6} \tag{21}$$

(the latter in geometrized units). Since $K \to \infty$ as $r \to 0$ in any coordinate system, the singularity at $r = 0$ represents a genuine divergence of the spacetime curvature -- a point where tidal forces become infinite and the classical theory breaks down.

### 5.3 What Schwarzschild Did Not Know

Schwarzschild's 1916 paper contains no discussion of the event horizon as a causal boundary, no concept of a "black hole," and no awareness that the singularity at his $R = \alpha$ (our $r = r_s$) is removable. The term "black hole" was not coined until 1967 (by John Archibald Wheeler, though earlier usage is debated). The full causal structure of the Schwarzschild spacetime was not understood until the Kruskal-Szekeres extension of 1960, forty-four years after Schwarzschild's paper.

---

## 6. The Derivation in Modern Notation

For completeness and pedagogical clarity, we present the standard textbook derivation that follows the logical structure (if not the coordinate choices) of Schwarzschild's original work.

### 6.1 The General Static, Spherically Symmetric Metric

By the symmetry assumptions, the most general line element can be written:

$$ds^2 = -A(r)\, dt^2 + B(r)\, dr^2 + r^2\, d\Omega^2 \tag{22}$$

where $A(r) > 0$ and $B(r) > 0$ for $r > r_s$. The angular part $r^2\, d\Omega^2$ is fixed by the requirement that surfaces of constant $t$ and $r$ are metrically round 2-spheres of area $4\pi r^2$ (this defines the **areal radius** coordinate $r$). The functions $A$ and $B$ depend on $r$ alone by staticity and spherical symmetry.

### 6.2 Christoffel Symbols

The non-vanishing Christoffel symbols $\Gamma^{\lambda}_{\mu\nu}$ for the metric (22) are:

$$\Gamma^t_{tr} = \Gamma^t_{rt} = \frac{A'}{2A} \tag{23a}$$

$$\Gamma^r_{tt} = \frac{A'}{2B} \tag{23b}$$

$$\Gamma^r_{rr} = \frac{B'}{2B} \tag{23c}$$

$$\Gamma^r_{\theta\theta} = -\frac{r}{B} \tag{23d}$$

$$\Gamma^r_{\phi\phi} = -\frac{r \sin^2\theta}{B} \tag{23e}$$

$$\Gamma^{\theta}_{r\theta} = \Gamma^{\theta}_{\theta r} = \frac{1}{r} \tag{23f}$$

$$\Gamma^{\phi}_{r\phi} = \Gamma^{\phi}_{\phi r} = \frac{1}{r} \tag{23g}$$

$$\Gamma^{\theta}_{\phi\phi} = -\sin\theta \cos\theta \tag{23h}$$

$$\Gamma^{\phi}_{\theta\phi} = \Gamma^{\phi}_{\phi\theta} = \cot\theta \tag{23i}$$

where primes denote differentiation with respect to $r$.

### 6.3 Ricci Tensor Components

Computing $R_{\mu\nu} = \partial_{\alpha} \Gamma^{\alpha}_{\mu\nu} - \partial_{\nu} \Gamma^{\alpha}_{\mu\alpha} + \Gamma^{\alpha}_{\alpha\beta}\Gamma^{\beta}_{\mu\nu} - \Gamma^{\alpha}_{\nu\beta}\Gamma^{\beta}_{\mu\alpha}$, the independent non-vanishing components are:

$$R_{tt} = \frac{A''}{2B} - \frac{A'}{4B}\left(\frac{A'}{A} + \frac{B'}{B}\right) + \frac{A'}{rB} \tag{24a}$$

$$R_{rr} = -\frac{A''}{2A} + \frac{A'}{4A}\left(\frac{A'}{A} + \frac{B'}{B}\right) + \frac{B'}{rB} \tag{24b}$$

$$R_{\theta\theta} = -1 + \frac{r}{2B}\left(\frac{A'}{A} - \frac{B'}{B}\right) + \frac{1}{B} \tag{24c}$$

$$R_{\phi\phi} = R_{\theta\theta} \sin^2\theta \tag{24d}$$

All off-diagonal components vanish identically by symmetry.

### 6.4 Solving the Vacuum Equations

Setting $R_{\mu\nu} = 0$:

**Step 1.** From the combination $\frac{R_{tt}}{A} + \frac{R_{rr}}{B} = 0$:

$$\frac{A'}{rAB} + \frac{B'}{rB^2} = 0 \implies \frac{d}{dr}\!\left[\ln(AB)\right] = 0 \tag{25}$$

Therefore $A(r) B(r) = \text{const}$. The boundary condition at infinity, $A \to 1$ and $B \to 1$ as $r \to \infty$, fixes:

$$A(r)\, B(r) = 1 \tag{26}$$

**Step 2.** Substituting $B = 1/A$ into $R_{\theta\theta} = 0$:

$$-1 + rA' + A = 0 \implies \frac{d}{dr}(rA) = 1 \tag{27}$$

Integrating:

$$rA(r) = r + C \implies A(r) = 1 + \frac{C}{r} \tag{28}$$

where $C$ is an integration constant.

**Step 3.** Matching to the Newtonian limit. For $r \gg |C|$, the weak-field expansion of $g_{tt}$ must reproduce the Newtonian potential:

$$g_{tt} \approx -\left(1 + \frac{2\Phi}{c^2}\right) = -\left(1 - \frac{2GM}{rc^2}\right) \tag{29}$$

Therefore $C = -2GM/c^2 = -r_s$, giving:

$$A(r) = 1 - \frac{r_s}{r}, \quad B(r) = \left(1 - \frac{r_s}{r}\right)^{-1} \tag{30}$$

**Step 4.** Verification. One confirms that $R_{tt} = 0$ and $R_{rr} = 0$ are identically satisfied with these functions (they provide no additional constraints beyond what was already extracted). The solution is **unique** up to the single parameter $M$.

---

## 7. Physical Predictions

The Schwarzschild solution underpins the three classical tests of general relativity proposed by Einstein, each of which is derivable from geodesic motion in the metric (12).

### 7.1 Gravitational Redshift

A photon emitted at radius $r_{\text{em}}$ and received at radius $r_{\text{obs}}$ (both at rest in the Schwarzschild coordinates) experiences a frequency shift:

$$\frac{\nu_{\text{obs}}}{\nu_{\text{em}}} = \frac{\sqrt{-g_{tt}(r_{\text{em}})}}{\sqrt{-g_{tt}(r_{\text{obs}})}} = \sqrt{\frac{1 - r_s/r_{\text{em}}}{1 - r_s/r_{\text{obs}}}} \tag{31}$$

For a photon escaping to infinity ($r_{\text{obs}} \to \infty$) from a source at $r_{\text{em}} = r$:

$$\frac{\nu_{\infty}}{\nu_{\text{em}}} = \sqrt{1 - \frac{r_s}{r}} \approx 1 - \frac{GM}{rc^2} + \mathcal{O}\!\left(\frac{r_s}{r}\right)^2 \tag{32}$$

The fractional redshift in the weak-field limit is:

$$z = \frac{\Delta\nu}{\nu} \approx \frac{GM}{rc^2} = \frac{r_s}{2r} \tag{33}$$

For the Sun's surface: $z_{\odot} \approx 2.12 \times 10^{-6}$, confirmed by Pound and Rebka (1960) using the Mossbauer effect in a terrestrial tower experiment, and by solar spectral line measurements.

### 7.2 Orbital Precession (Perihelion Advance)

The geodesic equation for a massive test particle in the equatorial plane ($\theta = \pi/2$) yields the effective one-dimensional orbit equation. Defining $u = 1/r$, the relativistic Binet equation is:

$$\frac{d^2 u}{d\phi^2} + u = \frac{M}{L^2} + 3Mu^2 \tag{34}$$

The last term, $3Mu^2$, is the general-relativistic correction absent in Newtonian gravity. For a nearly circular orbit of semi-latus rectum $p = L^2/M$, perturbation theory gives the perihelion advance per orbit:

$$\Delta\phi = \frac{6\pi G M}{c^2\, p} = \frac{6\pi M}{p} = \frac{6\pi G M}{c^2\, a(1 - e^2)} \tag{35}$$

where $a$ is the semi-major axis and $e$ the eccentricity.

For Mercury: $a = 5.791 \times 10^{10}$ m, $e = 0.2056$, $M = M_{\odot}$:

$$\Delta\phi_{\text{Mercury}} = 42.98 \text{ arcseconds per century} \tag{36}$$

in precise agreement with the anomalous precession measured since Le Verrier (1859). This was Einstein's first successful prediction (November 1915) and remains one of the most precisely confirmed predictions of general relativity.

### 7.3 Deflection of Light

For a photon (null geodesic, $ds^2 = 0$) passing a mass $M$ with impact parameter $b$, the orbit equation becomes:

$$\frac{d^2 u}{d\phi^2} + u = 3Mu^2 \tag{37}$$

(the $M/L^2$ term vanishes for massless particles when the equation is parametrized in terms of $b = L/E$). The total deflection angle for a photon passing at closest approach distance $r_0 \gg r_s$ is:

$$\Delta\phi = \frac{4GM}{c^2\, r_0} = \frac{2r_s}{r_0} \tag{38}$$

For light grazing the solar limb ($r_0 \approx R_{\odot}$):

$$\Delta\phi_{\odot} = \frac{4GM_{\odot}}{c^2 R_{\odot}} \approx 1.75 \text{ arcseconds} \tag{39}$$

This is exactly **twice** the Newtonian prediction of $2GM/c^2 r_0 = 0.875''$ -- the factor-of-two enhancement is a purely general-relativistic effect arising from the spatial curvature contribution to $g_{rr}$. The prediction was confirmed by Dyson, Eddington, and Davidson during the solar eclipse expedition of May 29, 1919, launching Einstein to international fame.

### 7.4 Shapiro Time Delay

A fourth test, proposed by Irwin Shapiro in 1964 (not available to Schwarzschild or Einstein in 1916), concerns the excess travel time of a radar signal passing near a massive body. For a signal passing the Sun at closest approach $r_0$:

$$\Delta t = \frac{4GM}{c^3}\left[\ln\left(\frac{4 r_{\text{em}}\, r_{\text{obs}}}{r_0^2}\right) + 1\right] \tag{40}$$

This has been measured to $\sim 0.001\%$ accuracy using Viking lander transponders (1977) and the Cassini spacecraft (2003), confirming the Schwarzschild geometry with extraordinary precision.

---

## 8. Birkhoff's Theorem

### 8.1 Statement

**Theorem (Jebsen 1921, Birkhoff 1923).** *Any spherically symmetric solution of the vacuum Einstein field equations $R_{\mu\nu} = 0$ is necessarily static and isometric to a region of the Schwarzschild spacetime.*

More precisely: if $(M, g)$ is a spherically symmetric spacetime satisfying $R_{\mu\nu} = 0$, then in the region where the $SO(3)$ orbits are spacelike 2-spheres, the metric is locally isometric to the Schwarzschild metric (12) for some value of $M$.

### 8.2 Significance

Birkhoff's theorem is the general-relativistic analogue of Newton's shell theorem. Its consequences include:

1. **No gravitational monopole radiation**: A spherically symmetric body cannot emit gravitational waves, regardless of how violently it pulsates -- provided the pulsation preserves spherical symmetry. The exterior geometry remains Schwarzschild; only the location of the stellar surface changes.

2. **Uniqueness**: The one-parameter family of Schwarzschild metrics (parametrized by $M$) exhausts all spherically symmetric vacuum solutions. There is no time-dependent spherically symmetric vacuum spacetime.

3. **Collapse**: During spherically symmetric gravitational collapse (e.g., Oppenheimer-Snyder 1939), the exterior spacetime is exactly Schwarzschild at all times, even as the interior is dynamical.

### 8.3 Historical Note

The theorem was first proved by the Norwegian physicist **Jorg Tofte Jebsen** in a 1921 paper in *Arkiv for Matematik, Astronomi och Fysik*. It was independently rediscovered by the American mathematician **George David Birkhoff** in his 1923 monograph *Relativity and Modern Physics*. Birkhoff's version became widely known due to the greater accessibility of his publication, and the result is conventionally (if somewhat unjustly) named for him alone.

### 8.4 Proof Sketch

The proof proceeds by noting that the most general spherically symmetric metric can be written in the form:

$$ds^2 = -e^{2\alpha(t,r)} dt^2 + e^{2\beta(t,r)} dr^2 + r^2 d\Omega^2 \tag{41}$$

where both $\alpha$ and $\beta$ are now allowed to depend on $t$ as well as $r$. Computing the vacuum field equations:

- The $R_{tr} = 0$ component yields $\partial_t \beta = 0$, so $\beta = \beta(r)$ only.
- The remaining equations then imply $\partial_t \alpha = 0$ as well, and the solution reduces to the static Schwarzschild metric.

The stationarity is not assumed but **derived** -- it is a consequence of spherical symmetry plus the vacuum condition, a far stronger result than Schwarzschild's original assumption of staticity.

---

## 9. Geodesic Structure and the Effective Potential

### 9.1 The Effective Potential for Timelike Geodesics

The conserved quantities $E$ and $L$ (equations 16--17), combined with the normalization $g_{\mu\nu} \dot{x}^{\mu} \dot{x}^{\nu} = -1$ for timelike geodesics, yield:

$$\frac{1}{2}\left(\frac{dr}{d\tau}\right)^2 + V_{\text{eff}}(r) = \frac{1}{2}(E^2 - 1) \tag{42}$$

where the effective potential is:

$$V_{\text{eff}}(r) = -\frac{M}{r} + \frac{L^2}{2r^2} - \frac{ML^2}{r^3} \tag{43}$$

The three terms are: (i) the Newtonian gravitational potential, (ii) the centrifugal barrier (also Newtonian), and (iii) the **relativistic correction** $-ML^2/r^3$, which is attractive and dominates at small $r$. This last term is responsible for the existence of an innermost stable circular orbit (ISCO) at:

$$r_{\text{ISCO}} = 6M = 3r_s \tag{44}$$

and of an unstable circular photon orbit at:

$$r_{\text{photon}} = 3M = \frac{3}{2}r_s \tag{45}$$

### 9.2 Null Geodesics

For null geodesics ($ds^2 = 0$), the orbit equation in terms of the impact parameter $b = L/E$ is:

$$\left(\frac{dr}{d\lambda}\right)^2 = E^2 - \left(1 - \frac{r_s}{r}\right)\frac{L^2}{r^2} \tag{46}$$

or equivalently, with $u = 1/r$:

$$\left(\frac{du}{d\phi}\right)^2 = \frac{1}{b^2} - u^2 + r_s\, u^3 \tag{47}$$

The critical impact parameter separating capture from scattering orbits is:

$$b_{\text{crit}} = 3\sqrt{3}\, M = \frac{3\sqrt{3}}{2}\, r_s \tag{48}$$

---

## 10. The Schwarzschild Radius in Astrophysical Context

The Schwarzschild radius for an object of mass $M$:

$$r_s = \frac{2GM}{c^2} \approx 2.95\left(\frac{M}{M_{\odot}}\right) \text{ km} \tag{49}$$

Representative values:

| Object | Mass | $r_s$ |
|--------|------|-------|
| Earth | $5.97 \times 10^{24}$ kg | 8.87 mm |
| Sun | $1.989 \times 10^{30}$ kg | 2.95 km |
| Sgr A* | $\sim 4 \times 10^6 \, M_{\odot}$ | $\sim 1.2 \times 10^7$ km |
| M87* | $\sim 6.5 \times 10^9 \, M_{\odot}$ | $\sim 1.9 \times 10^{10}$ km |

For ordinary astrophysical bodies (stars, planets), $r_s$ lies deep within the interior where the vacuum Schwarzschild solution does not apply; the interior solution (Schwarzschild's second paper, or more realistic stellar structure models) must be used. Only when matter is compressed within its own Schwarzschild radius does a black hole form and the full vacuum solution, including the event horizon, become physically realized.

---

## 11. Summary and Legacy

Schwarzschild's 1916 paper accomplished the following:

1. Provided the **first exact solution** to Einstein's gravitational field equations, demonstrating that the full nonlinear theory admitted closed-form solutions.
2. Established the mathematical framework for all subsequent work on spherically symmetric gravitational fields.
3. Implicitly contained (though Schwarzschild did not recognize it) the seed of **black hole physics** -- the existence of a critical radius at which the redshift becomes infinite and a causal horizon forms.
4. Enabled exact (not approximate) calculations of the three classical tests of general relativity.
5. Together with Birkhoff's theorem (1921/1923), established that the Schwarzschild geometry is the **unique** exterior field of any spherically symmetric body in vacuum.

The solution has since been generalized to include:

- **Electric charge**: the Reissner-Nordstrom metric (1916/1918)
- **Rotation**: the Kerr metric (1963)
- **Charge and rotation**: the Kerr-Newman metric (1965)
- **Cosmological constant**: the Schwarzschild-de Sitter (Kottler) metric (1918)

Yet the original Schwarzschild solution remains the foundational exact solution of general relativity: the simplest non-trivial curved spacetime, the prototype for all black hole physics, and a monument to the extraordinary achievement of a dying man working by lamplight on the Eastern Front.

---

## References

- Schwarzschild, K. (1916). *Uber das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie.* Sitzungsber. Preuss. Akad. Wiss. Berlin (Math. Phys.), 189--196. [English translation: arXiv:physics/9905030](https://arxiv.org/abs/physics/9905030).
- Schwarzschild, K. (1916). *Uber das Gravitationsfeld einer Kugel aus inkompressibler Flussigkeit nach der Einsteinschen Theorie.* Sitzungsber. Preuss. Akad. Wiss. Berlin (Math. Phys.), 424--434.
- Droste, J. (1917). *The field of a single centre in Einstein's theory of gravitation, and the motion of a particle in that field.* Proc. Royal Acad. Amsterdam **19**, 197--215.
- Birkhoff, G. D. (1923). *Relativity and Modern Physics.* Harvard University Press.
- Jebsen, J. T. (1921). *Uber die allgemeinen kugelsymmetrischen Losungen der Einsteinschen Gravitationsgleichungen im Vakuum.* Ark. Mat. Ast. Fys. **15**, 1--9.
- Kruskal, M. D. (1960). *Maximal Extension of Schwarzschild Metric.* Phys. Rev. **119**, 1743--1745.
- Eddington, A. S. (1924). *A comparison of Whitehead's and Einstein's formulae.* Nature **113**, 192.
- Finkelstein, D. (1958). *Past-Future Asymmetry of the Gravitational Field of a Point Particle.* Phys. Rev. **110**, 965--967.
- Antoci, S. & Loinger, A. (1999). *On the gravitational field of a mass point according to Einstein's theory.* [arXiv:physics/9905030](https://arxiv.org/abs/physics/9905030).
- Sundermeyer, K. (2023). *Schwarzschild's trick and Einstein's s(h)tick.* [arXiv:2312.01865](https://arxiv.org/html/2312.01865v1).
- Fromholz, P., Poisson, E., & Will, C. M. (2013). *The Schwarzschild metric: It's the coordinates, stupid!* [arXiv:1308.0394](https://arxiv.org/abs/1308.0394).
