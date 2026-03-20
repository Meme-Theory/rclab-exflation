# Kaluza-Klein Dimensional Reduction and Gauss-Codazzi-Ricci Equations

**Author(s):** Maia, Chaves
**Year:** 2008
**Journal:** arXiv:0805.4479

---

## Abstract

This paper provides a systematic treatment of dimensional reduction from higher-dimensional Einstein gravity to lower dimensions, with emphasis on the Gauss-Codazzi-Ricci (GCR) equations that govern the decomposition of curvature under foliation. The authors develop a unified framework showing how curvature invariants in D dimensions decompose into curvature of the base manifold and extrinsic curvature of a hypersurface. Applications include: explicit derivation of Einstein equations in lower dimensions from higher-D Einstein gravity with compact internal manifolds; relationships between Weyl tensor components in different dimensions; and the emergence of scalar fields (moduli) from the internal metric components. The framework is illustrated with examples: Kaluza-Klein reduction from D=5 to D=4, from D=11 M-theory to D=10, and reduction on arbitrary compact manifolds.

---

## Historical Context

When Einstein first proposed general relativity in 1915, the theory was 4-dimensional. In 1921, Kaluza and Klein proposed a 5D extension to unify gravity with electromagnetism. The key question was: **how does 5D gravity with a compact fifth dimension reduce to 4D gravity plus electromagnetism?**

The answer involves decomposing the 5D metric as:
$$g^{(5)}_{\mu\nu} = \begin{pmatrix} g_{\mu\nu}^{(4)} & A_\mu \\ A_\nu & \phi \end{pmatrix}$$

where $g^{(4)}$ is the 4D metric, $A_\mu$ is the Maxwell potential, and $\phi$ is a scalar (the dilaton).

However, the precise relationship between the 5D Einstein equations and the 4D Einstein equations plus Maxwell equations required careful analysis of how the **Ricci tensor** and **Weyl tensor** decompose under the foliation.

The Gauss-Codazzi-Ricci (GCR) equations are the tools for this decomposition. They relate:
- Extrinsic curvature $K_{\mu\nu}$ (how the hypersurface bends in the higher-D space)
- Intrinsic curvature $R^{(n)}$ (Ricci tensor of the hypersurface)
- Higher-D Ricci tensor $R^{(D)}$

For decades, these equations were relegated to differential geometry textbooks. In the 1990s-2000s, as string theory and extra-dimensional models became central, the GCR equations gained importance for understanding how 10D or 11D supergravity reduces to 4D phenomenology.

The 2008 Maia-Chaves paper consolidates this into a comprehensive framework, with explicit applications to modern string/M-theory scenarios.

---

## Key Arguments and Derivations

### Hypersurface Foliation and Extrinsic Curvature

Consider a D-dimensional Riemannian manifold $(\mathcal{M}, g)$ foliated by (D-1)-dimensional hypersurfaces $\Sigma_t$ (parameterized by a coordinate $t$).

At each point, define the **unit normal** $n^\mu$ perpendicular to $\Sigma_t$:
$$n^\mu n_\mu = 1, \quad g_{\mu\nu} n^\mu \xi^\nu = 0 \quad (\xi \in T\Sigma)$$

The **extrinsic curvature** (or second fundamental form) measures how the hypersurface bends:
$$K_{\mu\nu} = -\nabla_\mu n_\nu$$

where $\nabla$ is the covariant derivative in the D-dimensional space.

The extrinsic curvature is symmetric and decomposes into trace and traceless parts:
$$K_{\mu\nu} = K g_{\mu\nu} + \left(K_{\mu\nu} - \frac{K}{D-1} g_{\mu\nu}\right)$$

where $K = g^{\mu\nu} K_{\mu\nu}$ is the **mean curvature** (trace).

### Gauss-Codazzi Equations

The Gauss equation relates the Riemann tensor of the base manifold to the extrinsic curvature:

$$R^{(D)}_{\mu\nu\rho\sigma} = R^{(n)}_{\mu\nu\rho\sigma} + K_{\mu\rho} K_{\nu\sigma} - K_{\mu\sigma} K_{\nu\rho}$$

where $R^{(n)}$ is the Riemann tensor of the hypersurface (lowered indices).

This equation shows that the higher-D curvature is **not simply the lower-D curvature**, but includes a term depending on the extrinsic curvature.

The **Codazzi equations** are:
$$\nabla_\rho K_{\mu\nu} - \nabla_\mu K_{\rho\nu} = R^{(D)}_{\rho\mu\nu\sigma} n^\sigma$$

These relate derivatives of the extrinsic curvature to higher-D Ricci curvature.

### Ricci Decomposition

Contracting the Gauss equation gives the **Ricci scalar decomposition**:

$$R^{(D)} = R^{(n)} + K^2 - K_{\mu\nu}^2 + 2 \nabla_\mu (n^\nu \nabla_\nu n^\mu)$$

The last term (involving second derivatives of the normal) is a divergence and vanishes upon integration.

More crucially, the Ricci tensor components decompose as:

**Perpendicular to the hypersurface** (components $R^{(D)}_{tt}$, etc.):
$$R^{(D)}_{\mu\nu} = -\nabla_\mu \nabla_\nu \log A + \text{terms in } K$$

where $A$ is a function related to the metric component orthogonal to the hypersurface.

**Parallel to the hypersurface** (components $R^{(D)}_{\mu\rho}$ with $\mu, \rho \in T\Sigma$):
$$R^{(D)}_{\mu\rho} = R^{(n)}_{\mu\rho} + K K_{\mu\rho} - K_{\mu\lambda} K^\lambda_\rho - \nabla_\mu \nabla_\rho K$$

These equations show explicitly how the higher-D Einstein equations project onto the lower-D manifold.

### Kaluza-Klein Reduction Example

For the 5D metric:
$$ds^2_5 = g_{\mu\nu}^{(4)} dx^\mu dx^\nu + e^{2\alpha \phi} (dz + A_\mu dx^\mu)^2$$

where:
- $g^{(4)}$ is the 4D metric
- $\phi$ is the dilaton (size of the fifth dimension)
- $A_\mu$ is the Kaluza-Klein one-form
- $\alpha$ is a coupling constant (often $\alpha = \sqrt{3/2}$)

The extrinsic curvature of the $z = \text{const}$ hypersurfaces is:
$$K_{\mu\nu} = \alpha \partial_z \phi \, g^{(4)}_{\mu\nu} + ...$$

The GCR equations give:
$$R^{(5)}_{\mu\nu} = R^{(4)}_{\mu\nu} - \frac{1}{4} F_{\mu\lambda}^2 + ... = R^{(4)}_{\mu\nu} + (\text{Maxwell field terms})$$

After integrating over $z$, the 5D Einstein equations reduce to:
$$R^{(4)}_{\mu\nu} - \frac{1}{2} g^{(4)}_{\mu\nu} R^{(4)} = T^{(\phi)}_{\mu\nu} + T^{(F)}_{\mu\nu}$$

which is the 4D Einstein equations plus contributions from the dilaton and electromagnetic stress-energy.

### Moduli Fields and Internal Geometry

More generally, if the internal manifold has a modulus (e.g., size or shape), this modulus becomes a **scalar field** in the lower-dimensional theory:

$$\phi^a(x) = \text{metric components of internal manifold}$$

The kinetic energy of these fields appears in the 4D action:
$$S_4 = \int d^4x \sqrt{-g_4} \left[ \frac{R_4}{16\pi G_4} - \frac{1}{2} G_{ab} \partial_\mu \phi^a \partial^\mu \phi^b - V(\phi^a) \right]$$

where $G_{ab}$ is the metric on the moduli space, and $V(\phi)$ is a potential arising from the internal geometry.

### Weyl Tensor Decomposition

The Weyl tensor in D dimensions also decomposes:
$$C^{(D)} = C^{(n)} + \text{terms in } K \text{ and } R^{(n)}$$

The important result is that **the Weyl tensor of the base manifold is not simply the "internal part" of the higher-D Weyl tensor**. Instead, part of the higher-D Weyl tensor projects onto the base manifold, and part is "internal" (living on the compact manifold).

This explains why 5D empty space (Weyl = 0) can reduce to 4D spacetime with curvature: the higher-D flatness distributes curvature between the external 4D space and the internal geometry.

---

## Key Results

1. **GCR equations**: Complete set of relations between D-dimensional Riemann/Ricci tensors and (D-1)-dimensional intrinsic and extrinsic curvatures.

2. **Ricci scalar reduction**: The D-dimensional Ricci scalar decomposes into the (D-1)-dimensional Ricci scalar, extrinsic curvature contributions, and a divergence term.

3. **Einstein equations in codimension-1 foliation**: The D-dimensional Einstein equations project to (D-1)-dimensional Einstein equations plus constraint equations (momentum and Hamiltonian constraints).

4. **Moduli fields emerge**: Metric components of the internal manifold become scalar (moduli) fields in the reduced theory, with kinetic energies and potentials determined by internal geometry.

5. **Kaluza-Klein reduction systematic**: The process of deriving 4D Einstein-Maxwell from 5D Einstein is formalized through GCR equations; extension to multi-dimensional internal manifolds is straightforward.

6. **Weyl tensor distribution**: The higher-D Weyl tensor contributes to both external and internal curvature; complete flatness in D dimensions does not imply flatness in lower dimensions.

7. **Consistency of reduction**: The GCR equations ensure that the reduced lower-dimensional equations are self-consistent and derive from a variational principle.

8. **Quantitative relationships**: Explicit formulas relate physical scales in the higher-D theory to coupling constants and masses in the reduced theory.

---

## Impact and Legacy

The Maia-Chaves paper has been influential in:

- **String theory phenomenology**: Systematic dimensional reduction from 10D or 11D to 4D, incorporating moduli stabilization and internal geometry effects
- **Effective field theory**: Understanding how UV (higher-D) physics relates to IR (lower-D) physics through geometric reduction
- **Black hole thermodynamics**: Extending to codimension-2 foliations to understand black holes with internal structure (charged black holes in KK theory)
- **Cosmological applications**: Incorporating internal geometry evolution (cosmological moduli) into 4D cosmological dynamics
- **Numerical relativity**: Implementing GCR equations in simulation codes for higher-D black hole mergers

---

## Connection to Phonon-Exflation Framework

**Framework-relevant**: The phonon-exflation framework operates on M4 x SU(3), a product manifold requiring dimensional reduction from 5D (or higher) to 4D. The Maia-Chaves GCR formalism is **directly applicable**:

1. **Systematic reduction from M4 x SU(3) to 4D**: The GCR equations provide the mathematical machinery for decomposing 5D Einstein equations (or higher) on the product space into 4D Einstein gravity plus SU(3) gauge theory.

2. **Moduli from internal geometry**: The phonon-exflation "internal moduli" (e.g., the SU(3) radius, deformation parameters) are precisely the scalar fields that emerge in GCR reduction. Their kinetic energies and potentials are determined by the internal Einstein equations.

3. **Extrinsic curvature and cosmological dynamics**: The mean curvature $K$ of the M4 hypersurface in the higher-D spacetime is related to the Hubble parameter. The phonon-exflation cosmological expansion is driven by evolution of $K$, which the GCR equations directly control.

4. **Weyl tensor distribution and gravity emergence**: The phonon-exflation framework predicts that 4D gravity emerges from internal SU(3) geometry. The GCR decomposition shows explicitly how higher-D curvature (Weyl tensor) distributes between 4D spacetime and internal manifold, formalizing this emergence.

5. **Spectral action reduction**: The spectral action of the Dirac operator on M4 x SU(3) can be reduced to lower dimensions using GCR methods, showing how the 4D effective action relates to the higher-D spectral geometry.

6. **Constraint equations and initial conditions**: The Hamiltonian and momentum constraints from the GCR reduction determine the initial state of the universe (analogous to the "no-boundary proposal"). Phonon-exflation's initial condition (vanishing Weyl curvature at the Big Bang) is a natural solution to these constraints.

**Closest connection**: The **complete formalism for dimensional reduction from higher D to 4D via GCR equations** is essential for converting the higher-dimensional M4 x SU(3) geometry into a 4D effective theory, and for understanding how 4D gravity and gauge couplings emerge.

---

## References

- Maia, M., Chaves, C. (2008). "Kaluza-Klein dimensional reduction and Gauss-Codazzi-Ricci equations." *arXiv* 0805.4479.
- Israel, W. (1966). "Singular hypersurfaces and thin shells in general relativity." *Nuovo Cim.* 44:1.
- Wald, R. (1984). "General Relativity." University of Chicago Press.
- Besse, A. (1987). "Einstein Manifolds." Springer-Verlag.
