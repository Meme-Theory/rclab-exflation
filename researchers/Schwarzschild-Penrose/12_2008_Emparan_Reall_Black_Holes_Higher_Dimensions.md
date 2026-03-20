# Black Holes in Higher Dimensions

**Author(s):** Roberto Emparan, Harvey S. Reall
**Year:** 2008
**Journal:** Living Reviews in Relativity, 11:6

---

## Abstract

We review black hole solutions of higher-dimensional vacuum gravity and higher-dimensional supergravity theories. The existence of black holes in extra dimensions has profound consequences: unlike four-dimensional spacetime, where black hole event horizons must be topologically spherical, higher dimensions permit event horizons with non-spherical topologies (black rings, black strings, etc.). This review covers Myers-Perry black holes (rotating solutions), black rings, black strings, and exact solutions in supergravity, emphasizing the rich phenomenology and stability properties of higher-dimensional black holes.

---

## Historical Context

Black hole thermodynamics and the laws of black hole mechanics, established by Bekenstein, Hawking, and others in four dimensions, raised fundamental questions when extra dimensions were hypothesized. Two key puzzles emerged:

1. **Uniqueness in Four Dimensions**: In 4D, black holes are classified by three parameters (mass, angular momentum, charge)—the "no-hair theorem." Does this hold in higher dimensions?

2. **Hawking-Page Transitions**: In anti-de Sitter space (AdS), black holes undergo phase transitions. How does this affect the AdS/CFT correspondence?

The Myers-Perry solution (1986) first extended rotating black holes to arbitrary dimensions. However, the discovery by Emparan, Reall, and others that black rings (toroidal event horizons) exist in five and higher dimensions shattered the assumption of spherical topology. This opened a vast landscape of black hole solutions impossible in four dimensions.

The Gregory-Laflamme instability (1993) revealed that black strings (products of a 4D black hole with a compact dimension) are generically unstable, fragmenting into higher-dimensional black holes. This suggests a non-trivial vacuum structure and has implications for compactification stability.

For the phonon-exflation framework (which uses M4 x SU(3), a 10D spacetime), understanding the stability and classification of higher-dimensional black holes is essential. Could the internal compact space support non-trivial black hole configurations? What constraints does higher-dimensional black hole physics place on internal geometry?

---

## Key Arguments and Derivations

### Myers-Perry Black Holes

The Myers-Perry metric in $D$ dimensions with $\lfloor D/2 \rfloor$ independent angular momenta $a_i$ is:

$$ds^2 = -\left(1 - \frac{\mu}{\Sigma} \right) dt^2 + \frac{\Sigma}{(1 - \Sigma)}d\Sigma^2 + \sum_{i=1}^{\lfloor D/2 \rfloor} \left( \Sigma + a_i^2 \right) (d\theta_i^2 + \sin^2\theta_i \, d\phi_i^2)$$

where $\Sigma$ is a complicated function involving the radius and angular coordinates, and $\mu$ is a parameter related to mass. Key features:

- **Number of angular momenta**: In $D$ dimensions, one can have $\lfloor (D-1)/2 \rfloor$ independent rotation planes, each with a separate angular momentum parameter.
- **Rotating in higher dimensions**: Multiple rotations occur simultaneously. In five dimensions (one extra dimension), one has two independent angular momenta $a_1, a_2$.
- **Ergosphere**: Exists outside the event horizon when $a_i \neq 0$, allowing Penrose-process energy extraction.
- **Temperature and entropy**: The Hawking temperature and Bekenstein-Hawking entropy $S = A/4$ (in Planck units) generalize to higher dimensions:
  $$T_H = \frac{\kappa}{2\pi}, \quad S = \frac{\text{Area}}{4}$$
  where $\kappa$ is the surface gravity at the horizon.

### Black Rings

In five or more dimensions, a remarkable solution family exists: **black rings**. These have toroidal event horizon topology $S^1 \times S^{D-3}$ rather than the spherical $S^{D-2}$ topology of Myers-Perry or Schwarzschild.

The simplest black ring is a product:
$$\text{Horizon} = S^1 \times S^{D-3}$$
where $S^1$ is the azimuthal loop and $S^{D-3}$ is the equatorial sphere.

**Key properties**:
- Exist only in $D \geq 5$ dimensions
- Have singular curvature or instabilities in thin-ring limits (unlike Myers-Perry)
- Can co-rotate with a Myers-Perry black hole in a bound state
- Likely unstable under generic perturbations, fragmenting into lower-dimensional objects
- Dimensionally reduce to nothing in 4D (no black ring counterpart in Kerr spacetime)

Black rings exemplify the **richness of higher-dimensional black hole physics**: the dimensional reduction from 4D to 3D loses an entire solution family.

### Gregory-Laflamme Instability

A black string is a product solution:
$$\mathcal{M} = \text{BH}_{4D} \times S^1$$
where a 4D Schwarzschild or Kerr black hole is extended along a compact fifth dimension.

**Gregory-Laflamme instability**: For a black string with horizon radius $r_h$ and compactification radius $R$, if $r_h > R$, the string is unstable to perturbations that modulate the black hole's size around the compact direction. Physically, the string fragments into higher-dimensional black holes.

The instability is captured by a dispersion relation $\omega(k)$ where $k$ is the wavenumber along the compact direction. For $k < k_c$ (critical wavenumber), $\omega$ becomes imaginary, signaling exponential growth of perturbations.

**Threshold condition**:
$$k_c \sim 1/r_h$$

**Physical picture**: If a black string is too thick relative to the compactification size, it cannot sustain a uniform horizon. Instead, it breaks apart. This has profound implications for KK theories: if one compactifies spacetime on a circle to unify gravity with other forces, black strings would be unstable unless the compactification radius is very large.

### Black Hole Thermodynamics in Higher Dimensions

In $D$ dimensions, the first law of black hole thermodynamics is:
$$dM = T_H dS + \Omega_i dJ_i + \Phi dQ$$

where:
- $T_H = \kappa / (2\pi)$ is the Hawking temperature
- $S = A_H / 4$ is the Bekenstein-Hawking entropy (in Planck units)
- $\Omega_i$ are angular velocities conjugate to angular momenta $J_i$
- $\Phi$ is the electrostatic potential conjugate to charge $Q$

**Entropy scaling**: In $D$ dimensions, $A_H$ scales as $r_h^{D-2}$. Thus:
$$S \sim M^{(D-2)/D}$$
Compare this to 4D: $S \sim M^{2/4} = M^{1/2}$.

For $D=10$ (as in the phonon-exflation M4 x SU(3) scenario), entropy scales as $S \sim M^{8/10}$, a significantly weaker power law.

### Supergravity Black Holes

In maximal supergravity (e.g., 11D supergravity), black holes carry additional structure:
- **Charges**: In 11D supergravity, black holes can carry various charges (M2-brane charges, M5-brane charges, etc.).
- **BPS saturation**: Some black holes are BPS (Bogomol'nyi-Prasad-Sommerfield), meaning they saturate a bound relating mass to charge.
- **Uniqueness**: Unlike pure gravity, supergravity often exhibits black hole uniqueness theorems (e.g., all BPS 11D M-theory black holes with a given charge are unique).

These solutions are relevant if the internal SU(3) sector couples to a supergravity extension of the standard model.

---

## Key Results

1. **Topological Diversity in Higher Dimensions**:
   Black hole event horizons in $D \geq 5$ can be topologically non-spherical (rings, multiple components, exotic topologies). In 4D, topology is fixed by the Gauss-Bonnet theorem and energy conditions.

2. **Myers-Perry Metric**:
   Provides a complete family of asymptotically flat, vacuum black hole solutions in $D \geq 5$ with independent angular momenta. Reduces to Schwarzschild in $D=4$, Kerr for one non-zero $a_i$.

3. **Gregory-Laflamme Instability**:
   Black strings are unstable unless the compactification is larger than the black hole radius. This constrains KK compactification scenarios: either compactifications must be large (explaining weakness of gravity), or black strings are non-physical in consistent theories.

4. **Entropy Hierarchy**:
   Among black holes of equal mass in $D$ dimensions, configurations with different topologies and angular momenta arrangements have different entropies. The second law (entropy increase in black hole mergers) applies but configurations are rich.

5. **Uniqueness Lost**:
   In higher dimensions, black hole uniqueness fails: multiple non-isometric solutions can have identical asymptotic charges. This suggests a landscape of black hole solutions analogous to string theory's landscape.

---

## Impact and Legacy

The Emparan-Reall review established higher-dimensional black holes as a central topic in theoretical physics. Key impacts:

- **AdS/CFT**: Black holes in AdS space are essential to understanding thermalization in gauge theory (via the black hole-thermalization correspondence).
- **String theory compactifications**: Extra-dimensional black holes are phenomenologically relevant if extra dimensions exist at TeV scales (some versions of ADD or Randall-Sundrum models).
- **Quantum gravity phenomenology**: Small extra dimensions could lead to TeV-scale black hole production at the LHC. Emparan-Reall's results constrain such scenarios.
- **Information paradox**: Black holes in higher dimensions raise acute questions about information loss. The Gregory-Laflamme instability suggests that information is not destroyed but redistributed among many black hole fragments.
- **Holographic duality**: In AdS/CFT, black holes correspond to thermal states of the boundary CFT. Multi-black hole solutions (e.g., rings) correspond to exotic thermal phases.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework posits a 10-dimensional spacetime M4 x SU(3), where M4 is 4D Minkowski (or FLRW) and SU(3) is the internal 6-dimensional gauge group. Several connections to higher-dimensional black hole physics emerge:

### 1. Dimensional Hierarchy and Black Hole Stability

The framework's compactification (6D internal, 4D external) is a 10D product geometry. Emparan-Reall's analysis of Gregory-Laflamme instability becomes directly relevant:

- **Question**: If a black hole forms in the 4D M4 sector, does it fragment along the internal SU(3) dimension?
- **Constraint**: For the compactification to be stable, either:
  - The internal radius (characteristic size of SU(3)) is large compared to any black hole horizon in M4, OR
  - The 10D effective geometry is stable against black string fragmentation (perhaps due to internal curvature and metric structure preventing classical Gregory-Laflamme modes).

Session 35 computations confirm that the SU(3) fiber has high intrinsic curvature (Ricci scalar $\rho_{SU(3)} \sim$ few GeV in natural units). This might stabilize black strings by suppressing Gregory-Laflamme perturbations—a novel mechanism not covered in Emparan-Reall's vacuum gravity review.

### 2. Topological Constraints on Internal Geometry

If the internal SU(3) fiber is truly compact and smooth (no singularities), then black hole solutions in the 10D product spacetime must respect the internal topology. Black rings and other higher-dimensional topological solutions are impossible if the internal space itself is topologically constrained (e.g., if SU(3) is a principal SU(3) bundle rather than a direct product).

This may offer a uniqueness theorem: in M4 x SU(3), the only black hole solutions are M4-izations of Myers-Perry type (where rotation is in the external 4D directions only, not the internal 6D directions).

### 3. Entropy and Thermodynamic Stability

In 10D, the entropy of a black hole scales as $S \sim M^{8/10}$. This is a much weaker power law than 4D: $S \sim M^{1/2}$. The implications:

- **Small black holes are cold**: $T_H \propto M^{-2/10}$ is very shallow. Even low-mass black holes have small Hawking temperature.
- **Large black holes are cold**: High-mass black holes are also cold in 10D (compared to 4D).
- **Thermodynamic stability**: In 4D, black holes are thermodynamically unstable (specific heat is negative). In 10D, might they be more stable?

For the phonon-exflation mechanism, this affects whether black holes can form as byproducts of internal geometry evolution. If 10D black holes are thermodynamically stable, they might persist and complicate the effective 4D cosmology.

### 4. Kaluza-Klein Reduction and Black Hole Spectra

In the Kaluza-Klein ansatz used in the framework, the 10D metric is written as:
$$g_{MN}^{(10)} = \begin{pmatrix} g_{\mu\nu} + A_\mu A_\nu & A_\mu \\ A_\nu & 1 \end{pmatrix}$$
where $g_{\mu\nu}$ is 4D, $A_\mu$ is the gauge field, and the internal metric is encoded in the reduction.

A 10D black hole (e.g., Myers-Perry with two angular momenta) reduces to a 4D black hole plus gauge field structure. The spectrum of the 4D-effective theory includes not only the graviton but also KK states from the internal dimension. Emparan-Reall's higher-dimensional solutions inform how these KK towers are populated.

### 5. Stability of the Fold Transition

During the framework's transition from tau=0 to the fold (Sessions 35-38), the internal SU(3) geometry is evolving. Does this evolution induce a Gregory-Laflamme-like instability in the product geometry M4 x SU(3)?

- If the evolution is quasi-static (adiabatic), Gregory-Laflamme instability may be suppressed—the geometry remains stable.
- If the evolution is rapid (sudden quench, as modeled in Session 37), perturbative instabilities might be triggered.

Session 37 results show the transit is integrable, not chaotic—suggesting stability. However, a full higher-dimensional analysis of the 10D metric's stability during tau evolution is needed.

**Related framework gates**: KK-BH-STAB-12, GL-INSTAB-INTERNAL-12, ENTROPY-10D-12 (to be defined).

---

## References

- Emparan, R., & Reall, H. S. (2008). "Black holes in higher dimensions." *Living Reviews in Relativity*, 11(1), 6.
- Myers, R. C., & Perry, M. J. (1986). "Black holes in higher-dimensional spacetime." *Annals of Physics*, 172(2), 304–347.
- Gregory, R., & Laflamme, R. (1993). "Black strings and p-branes are unstable." *Physical Review Letters*, 70(20), 2837.
- Hawking, S. W., & Page, D. N. (1983). "Thermodynamics of black holes in anti-de Sitter space." *Communications in Mathematical Physics*, 87(4), 577–588.
