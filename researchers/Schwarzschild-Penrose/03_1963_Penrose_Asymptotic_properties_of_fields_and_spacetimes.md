# Penrose (1963): Asymptotic Properties of Fields and Space-Times

**Paper:** R. Penrose, *Asymptotic Properties of Fields and Space-Times*, Physical Review Letters **10**, 66--68 (1963).
**DOI:** [10.1103/PhysRevLett.10.66](https://doi.org/10.1103/PhysRevLett.10.66)
**Companion lecture:** R. Penrose, *Conformal Treatment of Infinity*, in *Relativity, Groups and Topology* (Les Houches 1963), ed. C. DeWitt and B. DeWitt, Gordon and Breach, 1964.
**Extended treatment:** R. Penrose, *Zero Rest-Mass Fields Including Gravitation: Asymptotic Behaviour*, Proc. R. Soc. London A **284**, 159--203 (1965).

---

## 1. Historical Context and Motivation

By the early 1960s, the study of gravitational radiation in general relativity faced a fundamental technical obstacle: infinity is infinitely far away. Questions about the asymptotic behaviour of fields---whether a spacetime is "asymptotically flat," whether gravitational waves carry energy to infinity, what symmetries the gravitational field possesses at large distances---all required careful limiting procedures along families of geodesics receding to infinite affine parameter.

Bondi, van der Burg, and Metzner (1962) and Sachs (1962) had developed the retarded-time formalism and discovered both the news function (encoding outgoing radiation) and the unexpectedly large BMS symmetry group at null infinity. Sachs had also established the "peeling" property of the Riemann tensor along outgoing null geodesics. But these results were obtained through painstaking coordinate-based expansions in inverse powers of a luminosity distance parameter $r$.

Penrose's 1963 paper introduced a single geometric idea that unified, clarified, and extended all of these results: **conformal compactification**. By rescaling the physical metric with a conformal factor that vanishes at infinity, one *brings infinity to a finite boundary* and converts asymptotic analysis into local differential geometry on that boundary.

This three-page letter is one of the most influential short papers in the history of general relativity.

---

## 2. The Core Idea: Conformal Rescaling

### 2.1 The Conformal Transformation

Given a physical spacetime $(M, g_{\mu\nu})$, Penrose introduces an **unphysical** (or **conformally compactified**) spacetime $(\tilde{M}, \tilde{g}_{\mu\nu})$ related by:

$$
\boxed{\tilde{g}_{\mu\nu} = \Omega^2 \, g_{\mu\nu}}
$$

where $\Omega$ is a smooth scalar field called the **conformal factor**. The physical spacetime $M$ is an open submanifold of $\tilde{M}$, and the boundary $\partial M = \tilde{M} \setminus M$ represents "points at infinity."

### 2.2 Why Conformal?

A conformal rescaling preserves the **null cone structure**: if $g_{\mu\nu} k^\mu k^\nu = 0$, then $\tilde{g}_{\mu\nu} k^\mu k^\nu = 0$ as well. This means:

- Light cones are preserved.
- Causal relationships (timelike, null, spacelike) between events are unchanged.
- Null geodesics remain null geodesics (though their affine parametrisation changes).

What changes is the *scale* of distances and times. A conformal factor $\Omega \sim 1/r$ compresses large distances into finite ones, effectively "crunching" infinity down to a boundary surface.

### 2.3 The Key Slogan

> *Infinity is just a place where $\Omega = 0$.*

The entire programme of asymptotic analysis---limits, fall-off conditions, boundary terms---is replaced by *local* analysis of fields at the smooth boundary $\mathscr{I}$ where $\Omega$ vanishes.

---

## 3. The Conformal Factor $\Omega$ and Its Properties

The conformal factor $\Omega: \tilde{M} \to \mathbb{R}$ must satisfy:

1. **$\Omega > 0$ in the physical interior $M$.**
   The physical metric $g_{\mu\nu} = \Omega^{-2} \tilde{g}_{\mu\nu}$ is well-defined and nondegenerate.

2. **$\Omega = 0$ on the conformal boundary $\mathscr{I}$.**
   This is what *defines* $\mathscr{I}$ as the locus of "infinity."

3. **$\tilde{\nabla}_\mu \Omega \neq 0$ on $\mathscr{I}$.**
   The boundary is a smooth, non-degenerate hypersurface---$\Omega$ vanishes to first order, not higher. This ensures $\mathscr{I}$ has a well-defined normal vector $n_\mu = \tilde{\nabla}_\mu \Omega$.

4. **$\tilde{g}_{\mu\nu}$ extends smoothly to $\mathscr{I}$.**
   The unphysical metric and its derivatives are regular at the boundary, so that standard differential geometry applies there.

### 3.1 Gauge Freedom

The conformal factor is not unique. If $\Omega$ is a valid conformal factor, then so is $\Omega' = \omega \, \Omega$ for any smooth positive function $\omega$. This gauge freedom corresponds to the freedom to choose different "rates" at which infinity is approached. Physical results must be invariant under this rescaling.

### 3.2 The Normal to $\mathscr{I}$

On $\mathscr{I}$, the normal covector is:

$$
n_\mu \big|_{\mathscr{I}} = \tilde{\nabla}_\mu \Omega \big|_{\mathscr{I}}
$$

The **character** of $\mathscr{I}$ (null, spacelike, or timelike) is determined by:

$$
\tilde{g}^{\mu\nu} n_\mu n_\nu \big|_{\mathscr{I}} = \tilde{g}^{\mu\nu} \tilde{\nabla}_\mu \Omega \, \tilde{\nabla}_\nu \Omega \big|_{\mathscr{I}}
$$

For asymptotically flat spacetimes satisfying the vacuum Einstein equations near $\mathscr{I}$, this quantity **vanishes**, making $\mathscr{I}$ a **null hypersurface**---one of Penrose's central results.

---

## 4. The Structure of Conformal Infinity

For an asymptotically flat spacetime, Penrose showed that "infinity" resolves into five distinct components:

### 4.1 Future Null Infinity: $\mathscr{I}^+$ ("scri-plus")

$$
\mathscr{I}^+ = \{\text{future endpoints of outgoing null geodesics}\}
$$

- Topology: $S^2 \times \mathbb{R}$
- Character: **null hypersurface**
- Physical meaning: the "celestial sphere at future infinity" --- the destination of all outgoing light rays and gravitational radiation
- This is where the Bondi news function lives, and where the BMS group acts

### 4.2 Past Null Infinity: $\mathscr{I}^-$ ("scri-minus")

$$
\mathscr{I}^- = \{\text{past endpoints of incoming null geodesics}\}
$$

- Topology: $S^2 \times \mathbb{R}$
- Character: **null hypersurface**
- Physical meaning: the source of all incoming radiation from the infinite past

### 4.3 Spacelike Infinity: $i^0$

$$
i^0 = \{\text{endpoint of spacelike geodesics at } r \to \infty \text{ with } t = \text{const}\}
$$

- Topology: a **single point**
- Character: spacelike
- Physical meaning: "spatial infinity" --- the common asymptotic region of all Cauchy surfaces
- Technically, $i^0$ is a singular point of $\mathscr{I}$ where $\mathscr{I}^+$ and $\mathscr{I}^-$ meet; the conformal structure is not smooth there

### 4.4 Future Timelike Infinity: $i^+$

$$
i^+ = \{\text{future endpoint of timelike geodesics at } t \to +\infty\}
$$

- Topology: a **single point**
- Character: timelike
- Physical meaning: the asymptotic future of all massive particles (in the absence of black holes)

### 4.5 Past Timelike Infinity: $i^-$

$$
i^- = \{\text{past endpoint of timelike geodesics at } t \to -\infty\}
$$

- Topology: a **single point**
- Character: timelike
- Physical meaning: the asymptotic past of all massive particles

### 4.6 Summary Diagram (Schematic)

```
                    i⁺
                   /  \
                  /    \
                 /      \
           I⁺  /        \  I⁺
               /   M      \
              /  (physical  \
             /  spacetime)   \
        i⁰  ·                · i⁰
             \              /
              \            /
               \          /
           I⁻  \        /  I⁻
                 \      /
                  \    /
                   \  /
                    i⁻
```

For Minkowski spacetime with spherical symmetry suppressed, this is the **Penrose diamond** (or triangle if one restricts to $r \geq 0$).

---

## 5. Application to Minkowski Spacetime: Explicit Construction

### 5.1 Step 1: Null Coordinates

Begin with the Minkowski metric in spherical coordinates:

$$
ds^2 = -dt^2 + dr^2 + r^2 \, d\Omega^2_{S^2}
$$

Introduce **retarded** and **advanced** null coordinates:

$$
u = t - r, \qquad v = t + r
$$

so that:

$$
ds^2 = -du \, dv + \frac{(v - u)^2}{4} \, d\Omega^2_{S^2}
$$

with $-\infty < u \leq v < +\infty$.

### 5.2 Step 2: Compactifying Transformation

Apply the arctangent map to bring the infinite range to a finite interval:

$$
p = \arctan(u), \qquad q = \arctan(v)
$$

so that $p, q \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ and $p \leq q$.

Then:

$$
du = \frac{dp}{\cos^2 p}, \qquad dv = \frac{dq}{\cos^2 q}
$$

### 5.3 Step 3: New Time and Radial Coordinates

Define:

$$
T = q + p, \qquad R = q - p
$$

These are **Penrose coordinates** with ranges:

$$
-\pi < T < \pi, \qquad 0 \leq R < \pi, \qquad |T| + R < \pi
$$

The constraint $|T| + R < \pi$ defines the **interior** of the Penrose triangle.

### 5.4 Step 4: The Conformal Factor and Compactified Metric

Substituting into the Minkowski metric, one obtains:

$$
ds^2 = \frac{1}{4 \cos^2 p \, \cos^2 q} \left[ -dT^2 + dR^2 + \sin^2 R \, d\Omega^2_{S^2} \right]
$$

The expression in square brackets is the **metric of the Einstein static universe** $\mathbb{R} \times S^3$:

$$
ds^2_{\text{ESU}} = -dT^2 + dR^2 + \sin^2 R \, d\Omega^2_{S^2}
$$

The conformal factor relating Minkowski space to the Einstein static universe is therefore:

$$
\boxed{\Omega = 2 \cos p \, \cos q = \cos T + \cos R}
$$

and:

$$
\tilde{g}_{\mu\nu} = \Omega^2 \, g_{\mu\nu} \quad \Longrightarrow \quad d\tilde{s}^2 = -dT^2 + dR^2 + \sin^2 R \, d\Omega^2_{S^2}
$$

The physical Minkowski metric $g_{\mu\nu}$ is related to the Einstein static universe metric by $g_{\mu\nu} = \Omega^{-2} \tilde{g}_{\mu\nu}$, which blows up as $\Omega \to 0$ (at the boundary), while the unphysical metric $\tilde{g}_{\mu\nu}$ remains perfectly regular there.

### 5.5 Step 5: Identification of Boundary Components

In the compactified coordinates $(T, R)$:

| Component | Location | Coordinates |
|-----------|----------|-------------|
| $i^+$ | Future timelike infinity | $T = \pi, \; R = 0$ |
| $i^-$ | Past timelike infinity | $T = -\pi, \; R = 0$ |
| $i^0$ | Spacelike infinity | $T = 0, \; R = \pi$ |
| $\mathscr{I}^+$ | Future null infinity | $T + R = \pi, \; 0 < R < \pi$ |
| $\mathscr{I}^-$ | Past null infinity | $-T + R = \pi, \; 0 < R < \pi$ |

At each of these, $\Omega = \cos T + \cos R = 0$ (or the appropriate limit).

### 5.6 The Penrose Triangle for Minkowski Space

Suppressing the angular coordinates $(\theta, \phi)$, the Minkowski Penrose diagram is a **triangle** (for $r \geq 0$):

```
                i⁺  (T=π, R=0)
               / \
              /   \
             /     \
        I⁺ /       \ I⁻ does not
           / Interior\   appear on
          /  (Mink.)  \  this side
         /             \
    i⁰  ·---------------· i⁻  (T=-π, R=0)
   (T=0, R=π)
```

More precisely, the right triangle has:
- **Right edge** ($R = 0$): the worldline of $r = 0$ (the spatial origin), a timelike line from $i^-$ to $i^+$
- **Upper-left edge** ($T + R = \pi$): $\mathscr{I}^+$, a null line from $i^0$ to $i^+$
- **Lower-left edge** ($-T + R = \pi$): $\mathscr{I}^-$, a null line from $i^-$ to $i^0$

If one includes negative $r$ (the full $t$-axis extended in both directions), the diagram becomes a **diamond** (two triangles glued along $R = 0$). For the standard physical Minkowski space ($r \geq 0$), it is a triangle.

### 5.7 The Einstein Static Universe Embedding

Penrose's construction reveals that Minkowski spacetime is **conformally embedded** as a finite region of the Einstein static universe $\mathbb{R} \times S^3$. The Penrose diagram is the projection of this region onto the $(T, R)$ plane, with each interior point representing an $S^2$ of radius $\sin R$.

---

## 6. Application to Schwarzschild Spacetime

### 6.1 Kruskal--Szekeres Extension

The maximally extended Schwarzschild solution in Kruskal--Szekeres coordinates $(U_K, V_K)$ takes the form:

$$
ds^2 = -\frac{32 M^3}{r} e^{-r/(2M)} \, dU_K \, dV_K + r^2 \, d\Omega^2_{S^2}
$$

where $r$ is defined implicitly by:

$$
U_K \, V_K = \left(\frac{r}{2M} - 1\right) e^{r/(2M)}
$$

### 6.2 Compactification of Kruskal Coordinates

One applies the same arctangent compactification to the Kruskal null coordinates:

$$
p = \arctan(U_K), \qquad q = \arctan(V_K)
$$

with $p, q \in (-\pi/2, \, \pi/2)$. The resulting double-null Penrose chart metric is:

$$
d\tilde{s}^2 = -\frac{64 M^3}{r} \cdot \frac{e^{-r/(2M)}}{\sin(2p)\,\sin(2q)} \, dp \, dq + r^2 \, d\Omega^2_{S^2}
$$

where $r$ is expressed via the Lambert $W$-function:

$$
r = 4M\!\left(1 + W\!\left(\frac{\tan p \, \tan q}{2M}\right)\right)
$$

Although the coordinate expression appears to develop a singularity at $r = 2M$, the metric coefficient is in fact smooth across the horizon, as can be verified by a careful limiting argument.

### 6.3 The Schwarzschild--Kruskal Penrose Diagram

The maximal extension has **four regions**:

```
              singularity (r = 0, future)
         ┌─────────────────────────────┐
        /  \         II              /  \
       /    \    (Black Hole)       /    \
      /      \    interior        /      \
     / I⁺     \                 /    I⁺   \
    /  (left)   \             /   (right)   \
   /              \         /                \
  · i⁰(L)    III  ·───────·   I    · i⁰(R)
   \     (Parallel  \     /  (Our       /
    \    Universe)    \  /  Universe)   /
     \  I⁻             \/        I⁻   /
      \  (left)       /  \   (right) /
       \            /      \        /
        \    IV   /    IV   \      /
         \  (White Hole)     \    /
          └─────────────────────┘
              singularity (r = 0, past)
```

Key features:
- **Region I**: the exterior Schwarzschild geometry ("our universe"), with $r > 2M$
- **Region II**: the black hole interior (future singularity), $r < 2M$, $T_K > 0$
- **Region III**: a "parallel universe," another copy of the exterior with $r > 2M$
- **Region IV**: the white hole interior (past singularity), $r < 2M$, $T_K < 0$
- **Horizons** ($r = 2M$): the diagonal lines at 45 degrees separating the regions
- **Singularities** ($r = 0$): the horizontal **spacelike** boundaries at top and bottom (drawn as jagged/wavy lines)
- **$\mathscr{I}^+_R, \mathscr{I}^-_R$**: future and past null infinity of Region I
- **$\mathscr{I}^+_L, \mathscr{I}^-_L$**: future and past null infinity of Region III
- **$i^0_R, i^0_L$**: spacelike infinities of Regions I and III

The diagram makes visually manifest that:
- Nothing escapes from Region II (the black hole) to $\mathscr{I}^+$
- The singularity is in the *future*, not at a "place"
- Regions I and III are causally disconnected (no signal can pass between them without crossing a horizon)

---

## 7. The Definition of Asymptotic Flatness

Penrose converts the vague intuition "looks like Minkowski space far away" into a precise geometric definition.

### 7.1 Asymptotically Simple Spacetimes

A smooth spacetime $(M, g_{\mu\nu})$ is **asymptotically simple** if there exists a smooth Lorentzian manifold $(\tilde{M}, \tilde{g}_{\mu\nu})$ such that:

1. $M$ is an open submanifold of $\tilde{M}$ with smooth boundary $\mathscr{I} = \partial M$.
2. There exists a smooth function $\Omega$ on $\tilde{M}$ such that $\tilde{g}_{\mu\nu} = \Omega^2 g_{\mu\nu}$ on $M$.
3. $\Omega > 0$ on $M$, $\Omega = 0$ on $\mathscr{I}$, and $\tilde{\nabla}_\mu \Omega \neq 0$ on $\mathscr{I}$.
4. Every null geodesic in $M$ acquires a **future and a past endpoint** on $\mathscr{I}$.

### 7.2 Asymptotically Flat Spacetimes

An asymptotically simple spacetime is **asymptotically flat** if, additionally:

5. The Ricci tensor $R_{\mu\nu}$ vanishes in a neighbourhood of $\mathscr{I}$ (the vacuum Einstein equations hold near infinity).

Under these conditions, $\mathscr{I}$ is necessarily a **null hypersurface** with two connected components $\mathscr{I}^+$ and $\mathscr{I}^-$, each with topology $S^2 \times \mathbb{R}$.

### 7.3 Weakly Asymptotically Simple Spacetimes

Schwarzschild (and other black hole spacetimes) fail condition (4) because some null geodesics terminate at the singularity rather than reaching $\mathscr{I}$. Penrose therefore introduces the notion of **weakly asymptotically simple** spacetimes: a spacetime is weakly asymptotically simple if there exists an asymptotically simple spacetime such that a neighbourhood of $\mathscr{I}$ in the first is isometric to a corresponding neighbourhood in the second.

This allows black holes while retaining the full conformal boundary structure at infinity.

### 7.4 Conformal Boundary Conditions

At $\mathscr{I}$, the following conditions hold:

$$
\Omega\big|_{\mathscr{I}} = 0
$$

$$
\tilde{\nabla}_\mu \Omega\big|_{\mathscr{I}} \neq 0
$$

$$
\tilde{g}^{\mu\nu} \tilde{\nabla}_\mu \Omega \, \tilde{\nabla}_\nu \Omega \big|_{\mathscr{I}} = 0 \quad \text{(null character of } \mathscr{I}\text{)}
$$

The last condition follows from the vacuum Einstein equations near $\mathscr{I}$ and is equivalent to the statement that $\mathscr{I}$ is a null hypersurface.

---

## 8. Gravitational Radiation at Null Infinity

### 8.1 The Bondi News Function

One of the triumphs of the conformal approach is a clean geometric characterisation of gravitational radiation.

In the Bondi--Sachs framework, one foliates $\mathscr{I}^+$ by cross-sections (topological $S^2$'s labelled by retarded time $u$). The **intrinsic metric** on each cross-section is a conformal $2$-sphere metric, and the **extrinsic geometry** of these cross-sections within $\mathscr{I}^+$ encodes the radiation.

The **Bondi news tensor** $N_{ab}$ is defined on $\mathscr{I}^+$ as:

$$
N_{ab} = \tilde{\nabla}_a \tilde{\nabla}_b \Omega \big|_{\mathscr{I}^+}
$$

projected onto the $S^2$ cross-sections (trace-free part). In a Bondi coordinate system $(u, \theta, \phi)$ on $\mathscr{I}^+$, the news reduces to a complex function $N(u, \theta, \phi)$---the **Bondi news function** $c_{,u}$ where $c$ is the shear of the outgoing null geodesic congruence.

The **key physical statement** is:

> **Gravitational radiation is present at $\mathscr{I}^+$ if and only if the news tensor $N_{ab}$ is nonvanishing.**

A spacetime with $N_{ab} = 0$ everywhere on $\mathscr{I}^+$ is stationary near infinity.

### 8.2 The Bondi Mass-Loss Formula

The Bondi mass $M_B(u)$ at retarded time $u$ satisfies:

$$
\boxed{\frac{dM_B}{du} = -\frac{1}{4\pi} \oint_{S^2} |N|^2 \, d\Omega_{S^2}}
$$

Since $|N|^2 \geq 0$, the Bondi mass is **monotonically non-increasing**: gravitational radiation always carries *positive* energy to infinity. This resolved the long-standing question of whether gravitational waves carry energy.

### 8.3 Freely Specifiable Data at $\mathscr{I}^+$

In the characteristic initial-value formulation, the news function is the **freely specifiable datum** at infinity. Given initial data on a null cone and the news function on $\mathscr{I}^+$, the entire spacetime (in a neighbourhood of $\mathscr{I}^+$) is determined. This makes the news function the gravitational analogue of the radiation field in electromagnetism.

---

## 9. The Peeling Theorem

### 9.1 Background: Newman--Penrose Formalism

The **Newman--Penrose (NP) formalism** (1962) decomposes the Weyl conformal curvature tensor $C_{\alpha\beta\gamma\delta}$ into five complex scalar components $\Psi_0, \Psi_1, \Psi_2, \Psi_3, \Psi_4$ with respect to a null tetrad $(l^\mu, n^\mu, m^\mu, \bar{m}^\mu)$.

For an outgoing null geodesic with affine parameter $r$ (serving as a luminosity distance), the **peeling theorem** states that the Weyl scalars fall off as:

### 9.2 Statement of the Peeling Theorem

$$
\boxed{
\Psi_n = \frac{\Psi_n^{(0)}}{r^{5-n}} + O\!\left(\frac{1}{r^{6-n}}\right), \qquad n = 0, 1, 2, 3, 4
}
$$

Explicitly:

| Weyl Scalar | Fall-off | Petrov Type of Leading Term | Physical Interpretation |
|:-----------:|:--------:|:---------------------------:|:----------------------:|
| $\Psi_0$ | $O(r^{-5})$ | --- | Incoming transverse radiation |
| $\Psi_1$ | $O(r^{-4})$ | --- | Incoming longitudinal radiation |
| $\Psi_2$ | $O(r^{-3})$ | Type D | Coulomb / mass-monopole ("Newtonian" part) |
| $\Psi_3$ | $O(r^{-2})$ | Type III | Outgoing longitudinal radiation |
| $\Psi_4$ | $O(r^{-1})$ | Type N | Outgoing transverse radiation |

### 9.3 Interpretation

The peeling theorem reveals a nested algebraic structure: as one moves outward along a null geodesic toward $\mathscr{I}^+$, the dominant part of the Weyl tensor becomes **algebraically more special** at each order:

$$
C_{\alpha\beta\gamma\delta} = \underbrace{\frac{C^{(N)}_{\alpha\beta\gamma\delta}}{r}}_{\text{Type N}} + \underbrace{\frac{C^{(III)}_{\alpha\beta\gamma\delta}}{r^2}}_{\text{Type III}} + \underbrace{\frac{C^{(II)}_{\alpha\beta\gamma\delta}}{r^3}}_{\text{Type II}} + \underbrace{\frac{C^{(I)}_{\alpha\beta\gamma\delta}}{r^4}}_{\text{Type I}} + O(r^{-5})
$$

The leading $1/r$ term is **Petrov type N** (the algebraic type of pure gravitational radiation), confirming that at large distances the gravitational field is purely radiative. The sub-leading terms encode progressively more complex multipolar structure.

### 9.4 Penrose's Conformal Derivation

Penrose showed that the peeling theorem follows *automatically* from the assumption of a smooth conformal boundary. Define the **rescaled Weyl tensor**:

$$
K_{\alpha\beta\gamma\delta} = \Omega^{-1} C_{\alpha\beta\gamma\delta}
$$

If $\tilde{M}$ is smooth and $\Omega$ is a smooth conformal factor, then $K_{\alpha\beta\gamma\delta}$ extends smoothly to $\mathscr{I}$. Since $\Omega \sim 1/r$ near $\mathscr{I}^+$, the physical Weyl tensor satisfies:

$$
C_{\alpha\beta\gamma\delta} = \Omega \, K_{\alpha\beta\gamma\delta}
$$

Expanding $K_{\alpha\beta\gamma\delta}$ in a Taylor series about $\mathscr{I}$ (i.e., in powers of $\Omega \sim 1/r$) immediately yields the peeling expansion. The smoothness of $K_{\alpha\beta\gamma\delta}$ at $\mathscr{I}$ *is* the peeling theorem, expressed in the conformal language.

This elegant derivation replaces the laborious coordinate-based calculations of Sachs (1961--62) with a single geometric argument: **peeling is a consequence of the smooth conformal compactifiability of spacetime.**

### 9.5 Connection to Gravitational Radiation

The leading peeling coefficient $\Psi_4^{(0)}$ is directly related to the Bondi news function:

$$
\Psi_4^{(0)} = -\ddot{\bar{\sigma}}^0 = -\frac{\partial^2 \bar{\sigma}^0}{\partial u^2}
$$

where $\sigma^0$ is the asymptotic shear, and the news function is $N = \dot{\sigma}^0 = \partial \sigma^0 / \partial u$. Thus:

$$
\Psi_4^{(0)} = -\dot{\bar{N}}
$$

The $\Psi_4$ scalar encodes the outgoing gravitational wave signal, which is why gravitational wave observatories effectively measure $\Psi_4$.

---

## 10. Key Equations: Summary

### 10.1 Conformal Transformation of Curvature

Under $\tilde{g}_{\mu\nu} = \Omega^2 g_{\mu\nu}$, the Ricci tensors are related by:

$$
\tilde{R}_{\mu\nu} = R_{\mu\nu} - \frac{2}{\Omega} \nabla_\mu \nabla_\nu \Omega - g_{\mu\nu} g^{\alpha\beta} \frac{1}{\Omega} \nabla_\alpha \nabla_\beta \Omega + \frac{4}{\Omega^2} \nabla_\mu \Omega \, \nabla_\nu \Omega - g_{\mu\nu} g^{\alpha\beta} \frac{1}{\Omega^2} \nabla_\alpha \Omega \, \nabla_\beta \Omega
$$

More compactly, using the notation $\Upsilon_\mu = \Omega^{-1} \nabla_\mu \Omega$:

$$
\tilde{R}_{\mu\nu} = R_{\mu\nu} - 2 \nabla_\mu \Upsilon_\nu - g_{\mu\nu} g^{\alpha\beta} \nabla_\alpha \Upsilon_\beta + 2 \Upsilon_\mu \Upsilon_\nu - 2 g_{\mu\nu} \Upsilon_\alpha \Upsilon^\alpha
$$

### 10.2 The Weyl Tensor Under Conformal Rescaling

The Weyl tensor is **conformally invariant**:

$$
\boxed{\tilde{C}^{\alpha}{}_{\beta\gamma\delta} = C^{\alpha}{}_{\beta\gamma\delta}}
$$

This is the fundamental reason conformal methods work: the Weyl tensor, which encodes the gravitational degrees of freedom (tidal forces, gravitational waves), is unaffected by conformal rescaling. It is the same tensor in both the physical and unphysical spacetimes.

### 10.3 The Bianchi Identity as a Field Equation

In vacuum ($R_{\mu\nu} = 0$), the contracted Bianchi identity becomes:

$$
\nabla^\alpha C_{\alpha\beta\gamma\delta} = 0
$$

This is a first-order equation for the Weyl tensor, structurally analogous to the source-free Maxwell equations $\nabla^\alpha F_{\alpha\beta} = 0$. Penrose emphasised this analogy: just as Maxwell's equations govern the propagation of electromagnetic radiation, the Bianchi identity governs the propagation of gravitational radiation. The conformal framework makes this analogy precise by treating both on an equal footing as **zero-rest-mass field equations**.

### 10.4 The Rescaled Weyl Tensor

$$
K_{\alpha\beta\gamma\delta} = \Omega^{-1} C_{\alpha\beta\gamma\delta}
$$

is smooth at $\mathscr{I}$, and its value there encodes the leading-order radiation field:

$$
K_{\alpha\beta\gamma\delta}\big|_{\mathscr{I}^+} \sim \Psi_4^{(0)}
$$

(in the NP decomposition adapted to $\mathscr{I}^+$).

---

## 11. The BMS Group

### 11.1 Discovery

One of the surprising consequences of Penrose's conformal framework is the structure of the asymptotic symmetry group. Bondi, van der Burg, and Metzner (1962) and Sachs (1962) independently discovered that the symmetry group of $\mathscr{I}^+$ is **not** the ten-parameter Poincare group, but an infinite-dimensional group now called the **Bondi--Metzner--Sachs (BMS) group**.

### 11.2 Structure

The BMS group is a semi-direct product:

$$
\text{BMS} = \text{SL}(2, \mathbb{C}) \ltimes \mathcal{S}
$$

where:
- $\text{SL}(2, \mathbb{C}) \cong \text{Lorentz group (proper orthochronous)}$ acts as the group of global conformal transformations of $S^2$
- $\mathcal{S}$ is the infinite-dimensional abelian group of **supertranslations**, which are angle-dependent translations along the null generators of $\mathscr{I}^+$

Ordinary spacetime translations form a **four-dimensional normal subgroup** of $\mathcal{S}$, but they are not uniquely singled out within the full supertranslation group. This leads to the well-known difficulty of defining angular momentum at null infinity.

### 11.3 Physical Significance

- The supertranslations encode the **gravitational memory effect**: a burst of gravitational radiation shifts the relative positions and clock readings of distant detectors by a BMS supertranslation.
- Weinberg's soft graviton theorem (1965) is equivalent to the Ward identity associated with BMS supertranslation invariance of the gravitational S-matrix (Strominger, 2014).
- The BMS group is an invariant of the conformal structure at $\mathscr{I}$, independent of the particular conformal factor $\Omega$ chosen.

---

## 12. Broader Impact and Legacy

### 12.1 What This Paper Made Possible

Penrose's 1963 construction provided the foundation for:

1. **Penrose (Carter--Penrose) diagrams**: now a standard tool in general relativity for visualising global causal structure.
2. **Rigorous definitions of black holes**: a black hole is the region of spacetime not in the causal past of $\mathscr{I}^+$, i.e., $B = M \setminus J^-(\mathscr{I}^+)$. This definition is impossible without a conformal boundary.
3. **The singularity theorems** (Penrose 1965, Hawking--Penrose 1970): the concept of a trapped surface and the notion of geodesic incompleteness within a globally well-defined causal structure.
4. **The positive energy theorem**: the Bondi mass-loss formula and its positivity properties.
5. **Friedrich's conformal field equations**: a regular system of PDEs on $\tilde{M}$ that includes $\mathscr{I}$ as an ordinary hypersurface, enabling numerical computation of radiative spacetimes.
6. **The modern understanding of gravitational wave extraction** in numerical relativity: waveforms are extracted at $\mathscr{I}^+$ using Cauchy-characteristic extraction or hyperboloidal methods.
7. **The infrared triangle** (Strominger): the equivalence of BMS supertranslations, Weinberg's soft graviton theorem, and the gravitational memory effect.

### 12.2 Conceptual Revolution

Before Penrose, "infinity" in general relativity was a vague limiting notion requiring coordinate-dependent prescriptions. After Penrose, infinity became a *place*---a well-defined boundary with its own geometry, topology, symmetry group, and field equations. Asymptotic analysis became local differential geometry.

The construction also revealed something profound: the gravitational field at infinity is **conformally invariant**. Only the conformal structure of spacetime---its null cone geometry---survives at $\mathscr{I}$. This is consonant with the fact that gravitational radiation propagates at the speed of light: it is the null-cone structure that carries the radiative degrees of freedom to infinity.

---

## 13. Notation and Conventions Reference

| Symbol | Meaning |
|--------|---------|
| $(M, g_{\mu\nu})$ | Physical spacetime and metric |
| $(\tilde{M}, \tilde{g}_{\mu\nu})$ | Unphysical (conformally compactified) spacetime and metric |
| $\Omega$ | Conformal factor; $\tilde{g}_{\mu\nu} = \Omega^2 g_{\mu\nu}$ |
| $\mathscr{I}$ | Conformal boundary ("scri"); $\Omega = 0$ locus |
| $\mathscr{I}^+$ | Future null infinity ("scri-plus") |
| $\mathscr{I}^-$ | Past null infinity ("scri-minus") |
| $i^0$ | Spacelike infinity |
| $i^+$ | Future timelike infinity |
| $i^-$ | Past timelike infinity |
| $C_{\alpha\beta\gamma\delta}$ | Weyl conformal curvature tensor |
| $K_{\alpha\beta\gamma\delta}$ | Rescaled Weyl tensor $\Omega^{-1} C_{\alpha\beta\gamma\delta}$ |
| $\Psi_0, \ldots, \Psi_4$ | Newman--Penrose Weyl scalars |
| $N_{ab}$ / $N$ | Bondi news tensor / news function |
| $\sigma^0$ | Asymptotic shear |
| $M_B(u)$ | Bondi mass at retarded time $u$ |
| BMS | Bondi--Metzner--Sachs asymptotic symmetry group |
| $\mathcal{S}$ | Supertranslation subgroup of BMS |

---

## References

- R. Penrose, "Asymptotic Properties of Fields and Space-Times," *Phys. Rev. Lett.* **10**, 66--68 (1963). [ADS](https://ui.adsabs.harvard.edu/abs/1963PhRvL..10...66P/abstract)
- R. Penrose, "Conformal Treatment of Infinity," in *Relativity, Groups and Topology*, ed. C. DeWitt and B. DeWitt (Gordon and Breach, 1964). Reprinted in *Gen. Rel. Grav.* **43**, 901--922 (2011).
- R. Penrose, "Zero Rest-Mass Fields Including Gravitation: Asymptotic Behaviour," *Proc. R. Soc. London A* **284**, 159--203 (1965).
- H. Bondi, M.G.J. van der Burg, and A.W.K. Metzner, "Gravitational Waves in General Relativity. VII. Waves from Axi-Symmetric Isolated Systems," *Proc. R. Soc. London A* **269**, 21--52 (1962).
- R.K. Sachs, "Gravitational Waves in General Relativity. VIII. Waves in Asymptotically Flat Space-Time," *Proc. R. Soc. London A* **270**, 103--126 (1962).
- E.T. Newman and R. Penrose, "An Approach to Gravitational Radiation by a Method of Spin Coefficients," *J. Math. Phys.* **3**, 566--578 (1962).
- J. Frauendiener, "Conformal Infinity," *Living Rev. Relativ.* **3**, 4 (2000). [Springer](https://link.springer.com/article/10.12942/lrr-2000-4)
- R.M. Wald, *General Relativity* (University of Chicago Press, 1984), Ch. 11.
- S.W. Hawking and G.F.R. Ellis, *The Large Scale Structure of Space-Time* (Cambridge University Press, 1973), Ch. 6.
