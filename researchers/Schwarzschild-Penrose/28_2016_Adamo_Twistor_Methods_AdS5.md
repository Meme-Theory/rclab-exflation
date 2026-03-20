# Twistor Methods for AdS5

**Author(s):** Adamo, Skinner, Williams
**Year:** 2016
**Journal:** Journal of High Energy Physics 08:167

---

## Abstract

This paper extends twistor methods from flat Minkowski space to anti-de Sitter (AdS) space, in particular focusing on AdS5 relevant for the AdS/CFT correspondence. The authors develop a twistor formulation of Yang-Mills and gravity in AdS5, showing how scattering amplitudes and correlation functions in the boundary CFT correspond to momentum space structures in AdS twistor space. The key result is that amplitudes in AdS5 can be computed using a holomorphic form similar to flat space, but with modifications due to the curvature. The paper also discusses the dimensional reduction to 4D and connections to Kaluza-Klein compactification, showing how internal symmetries and charges emerge from higher-dimensional twistor geometry.

---

## Historical Context

The AdS/CFT correspondence (Juan Maldacena, 1997) is one of the most profound discoveries in theoretical physics: a duality between gravity in anti-de Sitter space and gauge theory (Yang-Mills or conformal field theory) on the boundary.

In AdS/CFT, scattering amplitudes in the boundary CFT are related to correlation functions of Wilson loops or vertex operators in the AdS bulk. The specific mapping is non-trivial and depends on the details of the AdS geometry.

With the amplitudes revolution (2000s), it became apparent that flat-space amplitudes have remarkable holomorphic and integrable structure. A natural question arose: **do amplitudes in AdS5 preserve this structure?**

The answer is subtle. AdS5 has **positive curvature** (negative cosmological constant), which modifies the conformal structure relative to flat space. However, AdS5 is still a **conformally flat metric**: the Weyl tensor vanishes, and the metric is conformal to a flat metric.

The 2016 Adamo-Skinner-Williams paper develops the twistor geometry of AdS5, showing that:

1. Twistor space for AdS5 is **fibered over AdS5** in a natural way
2. Amplitudes in AdS5 retain much of their flat-space holomorphic structure
3. The boundary CFT correlation functions are recovered via residue integrals over twistor space
4. Dimensional reduction from AdS5 to AdS4 (relevant for 4D/3D duality) is geometrically transparent in twistor language

---

## Key Arguments and Derivations

### AdS5 Twistor Space Geometry

The metric of AdS5 (in Poincaré coordinates) is:
$$ds^2 = \frac{-dt^2 + d\vec{x}^2 + dz^2}{z^2}$$

where $z > 0$ is the radial ("bulk" or "holographic") coordinate, $t$ is time, $\vec{x} = (x, y)$ are spatial coordinates, and the boundary is at $z = 0$.

The **conformal structure** is the key feature: the metric is conformally equivalent to a flat metric via a rescaling:
$$ds^2_{\text{AdS}} = \Omega^2(z) ds^2_{\text{flat}}$$

with $\Omega(z) = 1/z$.

The **twistor space** for AdS5 is not simply $\mathbb{CP}^3$ (as for flat space), but rather a **bundle** over AdS5:
$$\mathbb{PT}_{\text{AdS}} = \text{Twistor fibration of AdS5}$$

Each fiber is a $\mathbb{CP}^1$ (the Riemann sphere), corresponding to the null directions at a point in AdS5.

Locally, a twistor $Z^\alpha = (\lambda^a, \mu^{\dot{a}})$ in AdS5 twistor space can be parameterized as:
$$(\lambda^a, \mu^{\dot{a}}) \in \mathbb{CP}^3 \quad \text{with} \quad \text{constraint: } |\mu|^2 = |z|^2 |\lambda|^2$$

This constraint reflects the **AdS curvature**: the inner product of spinors is modified relative to flat space.

### Scattering Amplitudes in AdS5 Twistor Space

In flat space, the MHV amplitude is:
$$A_n^{\text{MHV}} = \frac{1}{\prod_{i=1}^n \langle i, i+1 \rangle}$$

where $\langle i, j \rangle = \lambda_i \cdot \lambda_j$ is the spinor inner product.

In AdS5, amplitudes depend on both momenta **and** positions (due to lack of translational invariance). The generalization is more complex, but can be written in terms of **momentum twistors** that incorporate both information:

$$Z_i = (\lambda_i, \pi_i)$$

where $\pi_i$ encodes both the momentum and position of the $i$-th particle.

The key result is that AdS5 amplitudes can be written as:
$$\mathcal{A}_n^{\text{AdS}} = \int d^4\pi \, \frac{\mathcal{N}(\lambda_i, \pi)}{\text{denominators}}$$

where the integral is over auxiliary "boundary momentum" variables $\pi$, and the numerator and denominators are holomorphic (or rational) functions of the twistor variables.

### Connection to Boundary CFT Correlation Functions

The **holomorphic collinear limits** in AdS5 amplitudes correspond to **soft limits** in the boundary CFT:

$$\mathcal{A}_n \xrightarrow{\text{particle } i \text{ soft}} \frac{1}{\langle i, i+1 \rangle} \mathcal{A}_{n-1}$$

This is the same structure as flat space, but with modifications from curvature.

The **boundary 3-point function** of operators with dimensions $(\Delta_1, \Delta_2, \Delta_3)$ is recovered via:
$$\langle O_1 O_2 O_3 \rangle_{\text{CFT}} = \int_{\text{boundary}} dZ_1 dZ_2 dZ_3 \, \frac{\text{[AdS amplitude]}}{(\text{correlation measure})}$$

This integral is evaluated via residues in twistor space, showing explicitly how the AdS/CFT correspondence works at the amplitude level.

### Dimensional Reduction and Kaluza-Klein Structure

The reduction from AdS5 to AdS4 (or further to AdS3) can be understood as a **compactification of one direction**:

$$AdS_5 = AdS_4 \times S^1 / \text{identification}$$

(more precisely, a fibration rather than a direct product, but topologically similar).

In twistor language, this corresponds to restricting the twistor variables to a **submanifold**:
$$(Z^{(5)}) \xrightarrow{\text{KK reduction}} (Z^{(4)}, \text{winding mode})$$

where the winding mode (charge around the compactified direction) becomes a separate quantum number in the lower-dimensional theory.

The charges in the lower-dimensional theory emerge from the **angular momentum** in the higher-dimensional twistor space.

### Recursion Relations in AdS Twistor Space

Even with curvature, **BCFW recursion relations** can be formulated in AdS twistor space. The key is to define a **holomorphic deformation** of the twistor variables:
$$\lambda_i(z) = \lambda_i + z \lambda_j$$
$$\tilde{\lambda}_i(z) = \tilde{\lambda}_i$$

Under this deformation, the amplitude $\mathcal{A}_n(z)$ is a rational function of $z$, with poles at specific values $z_k$. The residue theorem gives:
$$\mathcal{A}_n = \sum_k \frac{\text{Res}_{z=z_k} \mathcal{A}_n(z)}{z_k} = \sum_k \text{[recursion relation]}$$

The recursion relations in AdS differ from flat space only by the **positions** of the poles, which are modified by curvature effects.

---

## Key Results

1. **AdS5 twistor space formulation**: Twistor methods generalize to AdS5 via a fibered bundle structure with modified inner product constraints.

2. **Holomorphic amplitude structure retained**: Amplitudes in AdS5 remain rational (holomorphic or meromorphic) functions of twistor variables, with modifications due to curvature.

3. **Curvature-modified pole locations**: The poles of AdS5 amplitudes are shifted relative to flat space by terms proportional to the curvature; these shifts encode AdS/CFT dynamics.

4. **Boundary CFT integrals**: Correlation functions in the boundary CFT are recovered via residue integrals over AdS5 twistor space, providing explicit amplitude/correlation function dictionary.

5. **Soft theorems in curved space**: AdS5 amplitudes obey modified soft theorems reflecting the loss of translational invariance; these are captured by conformal ward identities in twistor space.

6. **Dimensional reduction transparency**: Compactification from AdS5 to lower dimensions appears geometrically in twistor space as a restriction of twistor variables.

7. **Recursion relations in AdS**: BCFW recursion holds in AdS5 with curvature-modified pole structure; this enables efficient computation of AdS amplitudes.

8. **Superamplitudes**: The formalism extends to superconformal Yang-Mills in AdS5 via **supertwistors** (twistors with Grassmann variables), with explicit formulas for supergravity amplitudes.

---

## Impact and Legacy

The 2016 work solidified twistor methods as tools for AdS/CFT:

- **AdS/CFT dictionary**: Provided explicit formulas relating bulk amplitudes to boundary correlation functions
- **Soft limits and asymptotic symmetries**: Revealed how boundary conformal symmetry manifests as soft limits in the bulk
- **Integrability in AdS**: Connected to integrable structures in the AdS5/N=4 SYM system
- **Loop amplitudes**: Extended to loop-level computations, showing that loop integrals in AdS also have holomorphic structure
- **Applications to cosmology**: AdS/CFT techniques adapted to dS (de Sitter) for cosmological amplitudes

---

## Connection to Phonon-Exflation Framework

**Framework-relevant**: The phonon-exflation framework operates on M4 x SU(3), a product manifold analogous to AdS/CFT's dimensional reduction structure. The Adamo-Skinner-Williams results are applicable in several ways:

1. **Internal SU(3) as a compactified direction**: The SU(3) fiber in phonon-exflation can be understood as a compactification analogous to the S^1 in AdS5->AdS4 reduction. Twistor methods show how charges and quantum numbers emerge from this geometry.

2. **Kaluza-Klein modes and amplitude structure**: The phonon-exflation particle spectrum (quarks, leptons) corresponds to KK modes of the internal manifold. Twistor methods make explicit how these modes appear as poles in scattering amplitudes.

3. **Spectral action as holomorphic amplitude**: The phonon-exflation spectral action $S_{\text{spec}} = \text{Tr}[f(D_K/\Lambda)]$ can potentially be rewritten as an "amplitude" in an internal twistor space. The holomorphic structure would reveal which geometric configurations are dynamically favored.

4. **Dimensional reduction of gauge couplings**: In phonon-exflation, the gauge coupling $g_i$ emerges from the SU(3) curvature via dimensional reduction. The Adamo-Skinner-Williams framework shows explicitly how couplings depend on internal geometric and topological data.

5. **Conformal symmetries of internal space**: The internal SU(3) has conformal symmetries (conformal Killing vectors of the group manifold). These map to asymptotic symmetries of 4D gravity in twistor language, providing a unified picture of internal and external symmetries.

**Closest connection**: The **dimensional reduction framework** from curved (AdS) internal spaces to lower-dimensional physics, and the emergence of **charges/quantum numbers from internal geometry**, are directly applicable to phonon-exflation's M4 x SU(3) structure.

---

## References

- Adamo, T., Skinner, D., Williams, J. (2016). "Twistor methods for AdS5." *JHEP* 08:167.
- Maldacena, J. (1997). "The large-N limit of superconformal field theories and supergravity." *Adv. Theor. Math. Phys.* 2:231.
- Witten, E. (2004). "Perturbative gauge theory as a string theory in twistor space." *Commun. Math. Phys.* 252:189.
- Hodges, A. (2013). "Eliminating spurious poles from gauge-theoretic amplitudes." *JHEP* 05:135.
