# Spontaneous Compactification of Extra Space Dimensions

**Author(s):** Eugène Cremmer, Joël Scherk
**Year:** 1977
**Journal:** Nucl. Phys. B118 (1977) 61

---

## Abstract

We investigate the possibility that extra spatial dimensions present in higher-dimensional theories can acquire finite size through a dynamical mechanism, without artificial compactification by hand. We show that when 5D or 11D Yang-Mills theory is coupled to gravity, the equations of motion admit solutions where the extra dimensions form a compact manifold of finite radius determined by the gravitational backreaction of the gauge field. The compactification is "spontaneous" in the sense that it emerges dynamically at scales set by the Yang-Mills coupling, without external constraints. We apply the mechanism to unified theories and show how it generates the observed hierarchy between the Planck scale and electroweak scale.

---

## Historical Context

The path to modern extra-dimensional theories was forged through two parallel developments in the 1970s:

1. **String theory emergence** (1970-1976): Ramond, Schwarz, and Green discovered that the bosonic string and superstring naturally live in 10D (or 11D for M-theory). Early string theorists immediately faced the "compactification problem": how do 6 extra dimensions become invisible?

2. **Kaluza-Klein revival** (1974-1977): The old 5D gravity-electromagnetism unification of Kaluza (1921) and Klein (1926) was revived by Thaddeus Kaluza-Klein theorists who recognized that 5D Einstein gravity with appropriate boundary conditions yields both the Einstein equations (for 4D gravity) and Maxwell's equations (from 5D geometry), plus a scalar (the radion). But the mechanism of dimensional reduction remained mysterious — why should a 5D space naturally organize into 4D spacetime plus a circle?

Cremmer and Scherk's breakthrough paper addressed this foundational question: they showed that gravitational backreaction, arising from the energy density of a Yang-Mills field, naturally generates a stable compact extra dimension. This was the first rigorous demonstration that compactification is not an ad-hoc choice but an emergent phenomenon from well-known physics.

---

## Key Arguments and Derivations

### 5D Yang-Mills + Gravity Action

The starting point is the 5D action:

$$S = \int d^5 x \sqrt{-g} \left[ \frac{M_5^3}{2} R - \frac{1}{4g_5^2} F_{MN} F^{MN} + L_m \right]$$

where $M_5$ is the 5D Planck mass, $g_5$ is the 5D gauge coupling, $F_{MN} = \partial_M A_N - \partial_N A_M$ is the field strength, and $L_m$ includes matter. Variation with respect to the metric $g_{MN}$ yields Einstein's equations:

$$R_{MN} - \frac{1}{2} R g_{MN} = \frac{1}{M_5^3} \left( T_{MN}^{\text{gauge}} + T_{MN}^{\text{matter}} \right)$$

### Ansatz: Diagonal Metric with Warp Factor

Cremmer-Scherk proposed a metric of the form:

$$ds^2 = e^{2A(y)} \eta_{\mu\nu} dx^\mu dx^\nu + b^2(y) dy^2$$

where $\mu, \nu = 0,1,2,3$ are 4D Lorentz indices, $y$ is the fifth coordinate, $A(y)$ is a warp factor, and $b(y)$ is the scale of the extra dimension. For compactification, assume periodicity:

$$y \equiv y + \pi R_0$$

so the extra dimension is a circle of initial ("bare") radius $R_0$.

### Yang-Mills Energy-Momentum Tensor

The gauge field energy-momentum tensor is:

$$T_{MN}^{\text{gauge}} = \frac{1}{g_5^2} \left( F_{MP} F_N^P - \frac{1}{4} g_{MN} F_{PQ} F^{PQ} \right)$$

For a homogeneous background (independent of spacetime coordinates $x^\mu$), the only non-zero components are the temporal $T_{00}$ and $yy$ components:

$$T_{00}^{\text{gauge}} = \frac{1}{2g_5^2} \left( E_i^2 + B_i^2 \right)$$

where $E_i = F_{0i}$ and $B_i = \epsilon^{ijk} F_{jk} / 2$. The $yy$ component (pressure in the extra dimension) is:

$$T_{yy}^{\text{gauge}} = \frac{1}{4g_5^2} \left( E_i^2 - B_i^2 \right)$$

### Self-Consistency Equations

Requiring the metric and gauge field to satisfy Einstein's equations simultaneously (self-consistent backreaction) yields a coupled ODE system. For a purely electric Yang-Mills background ($E_i \neq 0$, $B_i = 0$), the equations simplify. The energy density in the extra dimension creates a "pressure" that compresses the fifth dimension.

The key equation (obtained by contracting Einstein's equations and integrating over $y$) is:

$$\frac{d^2 A}{dy^2} + \frac{1}{b^2} \left( \frac{db}{dy} \right)^2 - \frac{1}{2} \frac{d^2 b}{dy^2} = \frac{1}{4M_5^3 g_5^2} E_i^2$$

This is a nonlinear ODE for $A(y)$ and $b(y)$. The solution exhibits **oscillatory behavior** in the extra dimension: the warp factor $A(y)$ oscillates, and the radius $b(y)$ varies periodically.

### Compactification Mechanism

The energy density term on the RHS acts as a "source" for curvature. For sufficiently strong gauge field ($E_i \sim M_5$), the curvature becomes so large that the metric effectively "folds" the extra dimension. The radius shrinks to a stable value:

$$b_{\text{eq}} \approx \frac{g_5}{\sqrt{M_5^3 E_i}}$$

This equilibrium radius is determined by the balance between:
- **Gravitational attraction** (trying to shrink the dimension)
- **Gauge field pressure** (trying to inflate it)

Unlike Kaluza's original theory (where the radius was a free parameter), here $b_{\text{eq}}$ emerges from the equations of motion.

### Dimensional Reduction and Gauge Coupling

After compactification, the 5D fields decompose into Kaluza-Klein modes. The lowest mode (4D extension, independent of $y$) yields an effective 4D theory with:

$$M_{Pl}^4 \sim M_5^3 \times b_{\text{eq}}$$

and

$$g_4^2 \sim g_5^2 / b_{\text{eq}}$$

This is crucial: the 4D gauge coupling is now related to the compactification radius, providing a *geometric origin* for gauge unification. In the original Kaluza-Klein theory, the couplings were unrelated; here they emerge from a single source.

### Hierarchy Problem Application

Cremmer and Scherk showed that if the 5D fundamental scale is $M_5 \sim 10^{18}$ GeV and the extra dimension compactifies at $b \sim 10^{-30}$ cm (corresponding to $M_{\text{KK}} \sim 10^{15}$ GeV), then the *observed* 4D Planck scale is:

$$M_{Pl} \sim M_5^3 b^{1/2} \approx 10^{18} \text{ GeV}$$

And the electroweak scale emerges from a renormalization flow triggered by the KK tower. This was a first hint that extra dimensions might explain the hierarchy.

---

## Key Results

1. **Spontaneous compactification is possible**: Extra dimensions are not infinitely large or uncompactified; they naturally acquire finite size through gravitational backreaction of gauge fields.

2. **Radius is dynamically determined**: The compactification radius $b$ is not a free parameter but emerges from the self-consistency of Einstein-Yang-Mills equations. It depends on the 5D Planck mass, gauge coupling, and field configuration.

3. **Mechanism is generic**: The principle applies to any 5D or higher-D theory with gauge fields. It does not require special symmetries or fine-tuning.

4. **Hierarchy from geometry**: The Planck-electroweak hierarchy can be attributed (partially) to the compactification radius rather than to coupling constants alone.

5. **Moduli fields appear naturally**: The compactification radius becomes a dynamical field (the radion) in the 4D effective theory, with its own potential and dynamics.

6. **Implications for unification**: The mechanism suggests that unification might not require extremely high energies but rather emerges at intermediate scales where extra dimensions become important.

---

## Impact and Legacy

Cremmer-Scherk's 1977 paper was pivotal for three reasons:

**1. String theory motivation**: It provided a mechanism for *why* the 10D superstring naturally compactifies to 4D. Without this paper, string compactification would have remained a purely abstract mathematical exercise. Subsequent work (Witten, Vafa, Horava-Witten) built directly on the spontaneous-compactification principle.

**2. Gauge unification**: The geometric origin of gauge couplings inspired the later development of GUT-like structures from higher dimensions. This eventually led to the AdS/CFT correspondence and gauge/gravity duality, where the geometric structure of extra dimensions is identified with the renormalization group flow of the gauge theory.

**3. Modern cosmology**: The idea that the size of extra dimensions evolves dynamically is central to modern cosmological scenarios:
- Braneworld inflation (Randall-Sundrum cosmology, 2000s)
- Moduli stabilization (KKLT, Large Volume, 2003-2005)
- Dynamical dark energy from radion evolution (this decade)

Every modern extra-dimensional cosmology starts with the premise that compactification is not static but dynamical — a direct legacy of Cremmer and Scherk.

**4. Lattice field theory**: The mechanism can be studied numerically on a lattice, enabling precision tests of spontaneous compactification in various gauge theories. This has become a vibrant research area.

---

## Framework Relevance

The phonon-exflation framework adopts the principle of spontaneous compactification but applies it to *internal* geometry:

**Parallel**: Both Cremmer-Scherk and phonon-exflation treat the compactification radius as dynamical. In Cremmer-Scherk, the radius is stabilized by gauge fields. In phonon-exflation, the SU(3) fiber size (parameter $\tau$) is dynamically driven by the spectral-action evolution and instanton tunneling.

**Key difference**: Cremmer-Scherk operates in 5D spacetime (one large 4D + one small extra spatial dimension). Phonon-exflation operates entirely on the internal fiber M4 x SU(3) — the internal compactification IS the compactification (no external extra dimensions required).

**Connection to framework**: Spontaneous compactification demonstrates that a finite-size internal manifold is not imposed by fiat but emerges from self-consistent physics (gravitational backreaction). This validates the framework's ansatz: the SU(3) fiber does not need to be "rolled up by hand"; its emergence from $\tau=0$ (unified) to $\tau > 0$ (unfolded) is a consequence of instanton dynamics and the spectral geometry of the Dirac operator.

**Prediction**: Just as Cremmer-Scherk showed that the compactification radius becomes observable (via the radion field), the phonon-exflation framework predicts that the internal fiber size $\tau(t)$ becomes observable — via the spectral action, which couples $\tau$ to all particle masses. This is why the framework can make precise predictions for particle physics and cosmology that pure higher-dimensional theories cannot.

---

