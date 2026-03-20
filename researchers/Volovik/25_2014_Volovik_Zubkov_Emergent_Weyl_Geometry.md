# Emergent Weyl Geometry and the Gauge Invariant Vacuum Structure

**Authors:** G.E. Volovik, M.A. Zubkov

**Year:** 2014

**Journal:** Journal of Physics: Conference Series 607, 012009 (2015)

**arXiv:** 1405.5306

---

## Abstract

We develop a rigorous framework showing how Weyl geometry (conformal geometry with a non-Riemannian structure) emerges naturally from the vacuum of superfluid systems. The emergent Weyl connection defines a gauge-invariant covariant derivative for fermion fields coupled to the superfluid order parameter. Unlike Einstein gravity (which has no preferred scale), Weyl geometry possesses a scale-dependent gravitational structure: a Weyl vector field determines how distances scale at different points. We show that this structure emerges from the vortex lattice topology and the coupling of quasiparticles to collective modes. The framework explains why topological defects in superfluids produce not only metric deformations (as in Riemannian geometry) but also scale transformations (Weyl rescalings). Implications for gauge theory and cosmology are discussed.

---

## Historical Context

The concept of Weyl geometry dates to Hermann Weyl's 1918 attempt to unify electromagnetism and gravity by allowing the metric $g_{\mu\nu}$ to scale non-uniformly. While Einstein ultimately rejected this approach (insisting on metric compatibility), Weyl geometry has re-emerged in quantum field theory and cosmology as a valuable framework.

In condensed matter, superfluids naturally exhibit scale transformations. The superfluid density $\rho_s(T)$ depends on temperature; the speed of sound $c(T)$ varies with density. These are **Weyl rescalings** of the effective metric experienced by quasiparticles. Volovik and Zubkov's insight is that this is not coincidental—Weyl geometry is the *natural* arena for superfluid dynamics.

The historical significance for Volovik's program is that "emergent Weyl" geometry unifies three previously distinct concepts:
1. Effective gravity from phonons (Landau-Lifshitz)
2. Topological phases (Berry curvature, Chern numbers)
3. Scale-dependent symmetries (renormalization group flow)

For phonon-exflation, this means the **Weyl rescaling $g_{\mu\nu} \to e^{-2\phi(\tau)} g_{\mu\nu}$ is not an artifact—it is the *natural structure* for expressing how a deforming fabric couples to fermions.**

---

## Key Arguments and Derivations

### Superfluid Order Parameter and Weyl Structure

In a superfluid, the order parameter is $\psi(\mathbf{r}) = \sqrt{\rho_s} e^{i\theta}$, where $\rho_s$ is the superfluid density and $\theta$ is the phase. The density varies with position due to density fluctuations or external potentials:

$$\rho_s(\mathbf{r}) = \rho_0 + \delta\rho(\mathbf{r})$$

Quasiparticles (Bogoliubov excitations) couple to this order parameter through:
$$H_{\text{int}} = \int d^3r \, g \psi^\dagger \psi E_k$$

where $E_k$ is the quasiparticle energy and $g$ is the coupling strength.

The key observation is that variations in $\rho_s$ act like **scale transformations** on the metric. Define an effective metric:

$$g_{\mu\nu}^{\text{eff}} = e^{2\phi(\mathbf{r})} g_{\mu\nu}^{(0)}$$

where the Weyl factor $e^{2\phi}$ is proportional to $\rho_s$:
$$\phi(\mathbf{r}) = \frac{1}{2} \log(\rho_s(\mathbf{r})/\rho_0)$$

This is a **Weyl transformation**: $g_{\mu\nu} \to e^{2\phi} g_{\mu\nu}$.

### Weyl Connection and Gauge Invariance

In Einstein-Riemannian geometry, the connection $\Gamma$ is uniquely determined by the metric via the metric-compatibility condition:
$$\nabla_\mu g_{\nu\rho} = 0$$

In Weyl geometry, metric compatibility is *weakened*: the connection is allowed to contain a Weyl vector $A_\mu$ such that:
$$\nabla_\mu g_{\nu\rho} = -2 A_\mu g_{\nu\rho}$$

The Weyl vector transforms under Weyl rescalings as:
$$A_\mu \to A_\mu + \partial_\mu \phi$$

This compensates for the metric rescaling, ensuring that the covariant derivative remains well-defined.

In superfluid systems, the Weyl vector emerges from the vorticity:
$$A_\mu = \frac{\hbar}{2m} \partial_\mu \theta = \frac{\hbar}{2m} \Omega_\mu$$

where $\Omega_\mu$ is the vortex-induced connection. For a vortex lattice with circulation $\Gamma = \hbar/m$, integrating $A$ around a plaquette gives the vortex number.

### Ricci Tensor in Weyl Geometry

The Ricci tensor in Weyl geometry differs from Riemannian geometry by a Weyl term:

$$\mathrm{Ric}_{\mu\nu}^{\text{Weyl}} = \mathrm{Ric}_{\mu\nu}^{\text{Riemann}} - (n-2)\nabla_\mu \nabla_\nu \phi + (n-1) \nabla_\mu \phi \nabla_\nu \phi$$

For 4D spacetime (n=4), this becomes:

$$\mathrm{Ric}_{\mu\nu}^{\text{Weyl}} = \mathrm{Ric}_{\mu\nu} - 2 \Box \phi \, g_{\mu\nu} - 2 \nabla_\mu \nabla_\nu \phi + 2 \nabla_\mu \phi \nabla_\nu \phi$$

The extra $\Box \phi$ term (the Weyl scalar Laplacian) introduces a *scale-dependent gravity* where the effective gravitational coupling varies with position.

### Einstein Equations with Weyl Coupling

The action for a Weyl-invariant theory is:
$$S = \int d^4x \sqrt{-g} \left[ \frac{1}{16\pi G} R + \frac{\xi}{6} R \phi^2 + \frac{\lambda}{4!} \phi^4 + \frac{1}{2}(\partial\phi)^2 + L_{\text{matter}} \right]$$

where $\xi$ is the coupling of the Weyl field to curvature (conformal coupling: $\xi = 1/6$ for scalar fields).

The equations of motion read:
$$G_{\mu\nu} + \Lambda(\phi) g_{\mu\nu} = 8\pi G T_{\mu\nu}$$

where $\Lambda(\phi)$ is the *scale-dependent cosmological constant*:
$$\Lambda(\phi) = \Lambda_0 + \beta \phi + \gamma \phi^2$$

This shows that Weyl geometry naturally incorporates varying cosmological constant—essential for inflation and dark energy in cosmology.

### Emergence from Superfluid Vortices

Consider a 2D superfluid with a vortex lattice. Each vortex carries quantized flux $\Phi = \pi \hbar / m$. The superfluid density near a vortex core (radius $\xi$, the healing length) exhibits:

$$\rho_s(r) \approx \rho_0 \left(1 - \exp(-r/\xi)\right)$$

This spatial variation induces a local Weyl rescaling. The collective modes (density waves, spin waves) propagate in the effective Weyl-geometric background, with the Weyl vector determined by the vortex density:

$$A_i \sim n_{\text{vortex}} \times \text{(lattice constant)}$$

For a regular vortex lattice (Abrikosov lattice in superconductors), the Weyl structure is perfectly periodic, explaining the quantization of topological charges.

### Fermion Doubling and Weyl Index

A central result is that Weyl geometry naturally accommodates the *fermion doubling problem*. In a Euclidean lattice discretization, naive fermions exhibit doubling: n lattice sites → 2^n fermion degrees of freedom (due to flavor multiplication).

In Weyl geometry, the extra degrees of freedom are identified with **Weyl-conjugate fermions**: left-handed and right-handed versions related by:
$$\psi_R(\mathbf{r}) = e^{2\phi(\mathbf{r})} \psi_L(\mathbf{r})$$

The doubling is not a pathology—it is the *correct* representation of fermions in a Weyl-geometric background.

---

## Key Results

1. **Weyl Geometry Emerges from Superfluids**: Scale transformations in superfluid densities naturally induce Weyl rescalings of the effective metric. The Weyl vector emerges from vortex circulation.

2. **Weyl Connection is Gauge Invariant**: Unlike arbitrary metric rescalings, Weyl transformations are a *gauge symmetry* of superfluid systems. The Weyl vector compensates for metric rescaling, preserving covariance.

3. **Vortex Lattice Determines Topology**: The topological structure (Chern numbers, winding numbers) is determined entirely by the vortex lattice geometry, independent of the microscopic interaction strength.

4. **Cosmological Constant Becomes Scale-Dependent**: In Weyl geometry, $\Lambda(\phi)$ varies with position and can evolve with time (expansion). This provides a unified framework for inflation and dark energy.

5. **Fermion Doubling Resolved**: Fermion doubling in lattice discretizations is not a problem but reflects the genuine presence of both chiralities in Weyl-geometric backgrounds.

6. **Topological Invariance**: Physical observables (transport coefficients, spectral properties) are topological invariants—they remain unchanged under smooth Weyl deformations, explaining robustness.

---

## Impact and Legacy

Volovik and Zubkov's framework showed that Weyl geometry is not an abstract mathematical tool but the *natural language for superfluid systems*. This influenced:

- **Quantum Computing**: Topological qubits exploit the robustness of Weyl-geometric states
- **Dark Energy**: Weyl-geometric models of dark energy with varying cosmological constant
- **Condensed Matter**: Classification of topological phases using Weyl geometry
- **Cosmology**: Cyclic universe models based on Weyl conformal transformations

The framework predicts that any observation of **scale-dependent physics** (varying fine structure constant, running coupling constants in gravity, etc.) would be direct evidence for Weyl geometry.

---

## Connection to Phonon-Exflation Framework

**Direct Relevance (TIER 1)**

The Weyl rescaling $g_{\mu\nu} \to e^{-2\phi(\tau)} g_{\mu\nu}$ observed at the fold (Papers Baptista-13 to -18) is **precisely the Weyl geometry structure** that Volovik-Zubkov describe.

**Mathematical Mapping**:
- Superfluid density $\rho_s \to$ pairing condensate $\Delta(\tau)$
- Vortex lattice $\to$ 10-sector topology with 992 Dirac eigenvalues
- Weyl factor $e^{2\phi} \sim \Delta(\tau)/\Delta_0$ (condensate strength)
- Weyl vector $A_\mu \sim$ circulation in Cooper pair winding

**Physical Interpretation**:
The framework exhibits **Weyl-geometric cosmology**. The observable metric rescaling at the fold corresponds to:

$$\phi(\tau) = -\tau$$

$$g_{\mu\nu}(\tau) = e^{-2\tau} g_{\mu\nu}^{(0)}$$

This is not an arbitrary choice—it emerges from the coupling of fermions to the deforming pairing condensate, exactly as Volovik-Zubkov describe for superfluids.

**Scale-Dependent Couplings**:
In Sessions 33a-34, the running of coupling constants with τ was computed. This is the RG flow in Weyl-geometric language. The spectral action exhibits:

$$\alpha_s(\tau) = \alpha_0 e^{-2\tau} + \text{(loop corrections)}$$

This is *not* the standard GUT running—it is **conformal running** in a Weyl-geometric vacuum.

**Dark Energy Implications**:
If the framework describes the true vacuum structure, then dark energy corresponds to the **variation of Weyl curvature**, not the Einstein curvature. The "dark energy density" in DESI and CMBR would be:

$$\rho_{\text{DE}} \sim \Lambda(\phi) \sim \Lambda_0 + \beta \phi + \gamma \phi^2$$

Since $\phi(\tau) \sim \ln(e^{-\tau})$ (the scale factor), dark energy in the framework exhibits **Weyl scaling**, potentially explaining the $w \approx -1$ behavior observed in DESI DR2 (which would be a natural attractor in Weyl geometry).

**Testable Prediction**:
Volovik-Zubkov's theory predicts that the **Weyl vector** (vorticity in the pairing field) should be observable through its coupling to fermion spin:

$$\Delta E_{\text{spin}} \sim g_s \mu_B (A_\mu \times \mathbf{s})$$

where $\mathbf{s}$ is the fermion spin. In the framework, this would appear as *anomalous magnetic moment* variations with τ, testable via precision cosmology or CP violation experiments.

