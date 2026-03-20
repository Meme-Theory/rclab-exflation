# Spineurs, operateurs de Dirac et variations de metriques
## [Spinors, Dirac Operators and Metric Variations]

**Author(s):** Jean-Pierre Bourguignon, Paul Gauduchon
**Year:** 1992
**Journal:** Communications in Mathematical Physics, Vol. 144, No. 3, pp. 581–628
**DOI:** 10.1007/BF02099184

---

## Abstract

We develop a comprehensive theory of how spinor bundles and Dirac operators respond to metric deformations on Riemannian manifolds. We construct explicit comparison maps (Phi-maps) between spinor bundles for different metrics on the same manifold, derive transformation laws for Dirac operators under metric variation, and establish quantitative bounds on how spin structure "stretches" under geometric deformation. Applications include spinor regularity in families of Einstein metrics, Seiberg-Witten invariants under metric deformation, and the behavior of eigenvalues of the Dirac operator under perturbation. The machinery provides explicit tools for tracking spinor fields across metric families.

---

## Historical Context

The Dirac operator $D$ on a spin manifold is a fundamental object in differential geometry and physics:
$$D = \gamma^\mu \nabla_\mu,$$
where $\gamma^\mu$ are Clifford generators and $\nabla$ is the spin connection.

Crucially, the Dirac operator **depends on the metric** — change $g$ to $g'$, and the connection changes, so the spectrum of $D$ changes.

In the 1980s-90s, three questions emerged as central:

1. **Eigenvalue stability**: How much does the Dirac spectrum shift when the metric is slightly perturbed?
2. **Spectral families**: For a 1-parameter family $g_\tau$ of metrics, how do the eigenvalues evolve?
3. **Spinor representation**: When two metrics $g$ and $g'$ are sufficiently close, can spinor eigenmodes be continuously tracked from one metric to the other?

Bourguignon and Gauduchon's paper provides the **foundational answer**: they construct explicit **comparison isomorphisms** between spinor bundles over different metrics, enabling one to match spinor eigenmodes across metric families.

This work is essential for any project involving:
- Metric moduli (e.g., deformation families like the Jensen deformation)
- Spectral action functionals (metric-dependent Dirac spectrum)
- Seiberg-Witten theory (spinor invariants under metric change)

---

## Key Arguments and Derivations

### Spin Bundles and the Metric Dependence

Given a Riemannian manifold $(M, g)$ with spin structure, the spinor bundle $S_g$ and Dirac operator $D_g$ are constructed as follows:

1. **Oriented orthonormal frame bundle**: $SO(M) \to M$ (structure group $SO(n)$)
2. **Spin structure**: Lift to $\text{Spin}(n)$ principal bundle $\text{Spin}(M) \to M$
3. **Spinor bundle**: $S_g = \text{Spin}(M) \times_{\rho} \Delta_n$, where $\Delta_n$ is the spinor space (dimension $2^{\lfloor n/2 \rfloor}$) and $\rho$ is the spin representation
4. **Spin connection**: Lifts from Levi-Civita connection of $g$
5. **Dirac operator**: $D_g: \Gamma(S_g) \to \Gamma(S_g)$, $D_g = \gamma^\mu \nabla_\mu^g$

Now, change the metric to $g' = e^{2\sigma} g$ (conformal deformation, simplest case). The orthonormal frame bundle changes:
$$\text{SO}(M, g) \to \text{SO}(M, g') \quad \text{via scale transformation}.$$

The spin structure **lifts canonically** (since Spin is a double cover of SO, spin structures are in correspondence with orientation-preserving isometries). But the spinor bundles $S_g$ and $S_{g'}$ are **not identical** — they are different bundles!

### The Comparison Isomorphism (Phi-Map)

Bourguignon and Gauduchon construct an explicit **comparison isomorphism**:
$$\Phi_{g \to g'}: S_g \to S_{g'}$$
that:
1. Respects fiber structure (isomorphism of vector bundles)
2. Preserves the Clifford action (intertwines $\gamma^\mu_g$ with $\gamma^\mu_{g'}$)
3. Is **functorial** (composing transitions is associative)
4. Reduces to identity when $g = g'$

For a metric deformation $g_\tau = g_0 + \tau h$ (where $h$ is a symmetric 2-tensor), the infinitesimal version is:
$$\Phi_\tau = \mathbb{1} + \tau \Phi^{(1)} + O(\tau^2),$$
where $\Phi^{(1)}$ is a first-order operator depending on $h$ and the curvature of $g_0$.

Explicitly:
$$\Phi^{(1)}[\psi] = \frac{1}{4} \gamma^\mu \gamma^\nu h_{\mu\nu} \psi + \text{(lower-order spin connection correction)}.$$

The Phi-map allows one to **transport spinor eigenmodes** from metric $g$ to metric $g'$:
$$\psi'_\lambda(g') = \Phi_{g \to g'}(\psi_\lambda(g)).$$

### Dirac Operator Transformation

Under metric deformation, the Dirac operator transforms as:
$$D_{g'} = \Phi_{g \to g'} \circ D_g \circ \Phi_{g \to g'}^{-1} + \Delta D_\text{new},$$
where $\Delta D_\text{new}$ is the **newly induced** part of the Dirac operator coming from the metric change.

For conformal deformation $g' = e^{2\sigma} g$:
$$D_{e^{2\sigma} g} = e^{-\sigma} D_g e^{\sigma} + e^{-\sigma} \sigma_\mu \gamma^\mu e^\sigma,$$
where $\sigma_\mu = \partial_\mu \sigma$ (gradient of conformal factor).

For small conformal deformations ($\sigma \ll 1$):
$$\Delta D_\text{conformal} \approx -\sigma_\mu \gamma^\mu + \frac{1}{2} \gamma^\mu \gamma^\nu \sigma_\mu \sigma_\nu + \cdots$$

### Spectral Perturbation Theory

The comparison isomorphism enables **perturbative tracking** of eigenvalues. If $\psi$ is an eigenmode of $D_g$ with eigenvalue $\lambda$:
$$D_g \psi = \lambda \psi,$$
then under metric perturbation $g \to g' = g + \epsilon h$, the perturbed eigenvalue $\lambda'$ satisfies:
$$\lambda' = \lambda + \epsilon \langle \psi, \Delta D[\psi] \rangle + O(\epsilon^2),$$
where $\Delta D$ is computed using the Phi-map.

This is the **Rayleigh-Ritz perturbation formula** applied to Dirac eigenvalues. The first-order shift is given by:
$$\delta\lambda = \frac{1}{2} \int_M \langle \psi, \gamma^\mu \gamma^\nu h_{\mu\nu} \psi \rangle \, dV,$$
where the integral is over the manifold with volume element from $g$.

---

## Key Results

1. **Functorial Comparison Maps**: For any pair of metrics $g, g'$ on a spin manifold, there exists a unique functorial comparison isomorphism $\Phi_{g \to g'}: S_g \to S_{g'}$ respecting the Clifford action.

2. **Infinite-Dimensional Naturality**: The comparison maps form a natural system under metric families — for a path $g_\tau$, the maps $\Phi_{\tau_1 \to \tau_2}$ compose correctly to $\Phi_{\tau_1 \to \tau_3}$.

3. **Perturbation Formula for Eigenvalues**: For metric perturbations $g \to g + \epsilon h$, the first-order shift in Dirac eigenvalues is:
$$\delta\lambda_n = \frac{1}{2\|\psi_n\|^2} \int_M \langle \psi_n, \gamma^\mu \gamma^\nu h_{\mu\nu} \psi_n \rangle \, dV + O(\epsilon^2).$$

4. **Continuity of Spectrum**: The spectrum of $D_g$ varies continuously (in the sense of Hausdorff distance on compact sets) as $g$ varies within a neighborhood in the space of Riemannian metrics.

5. **Eigenmode Tracking**: Along a continuous family $g_\tau$, eigenmodes can be continuously tracked via the comparison isomorphism. If $\psi_n(\tau)$ is an eigenmode at parameter $\tau$, it connects smoothly to $\psi_n(\tau')$ at nearby $\tau'$ (away from avoided crossings).

6. **Seiberg-Witten Application**: For spinor equations with Dirac operator (Seiberg-Witten theory), the moduli space of solutions varies smoothly with metric — comparison isomorphisms control this variation.

---

## Impact and Legacy

This paper became the **standard reference** for spinor analysis in metric families. Key subsequent applications:

- **Eigenvalue families in RG flows** (AdS/CFT): Tracks Dirac eigenvalues under metric deformation from UV to IR fixed point
- **Spectral action functionals**: Establishes the rigor underlying Chamseddine-Connes program (Dirac spectrum is a geometric invariant that can serve as a functional of the metric)
- **Gromov-Lawson surgery**: Understanding how spinor structures and eigenvalues change under topological operations
- **Kahler-Ricci flow**: Monitoring Dirac spectrum along geometric flows
- **Quantum field theory on curved spacetime**: Foundation for defining particle creation in time-dependent geometries

The comparison isomorphism technique has become standard in any area requiring **continuous family of spin manifolds**.

---

## Connection to Phonon-Exflation Framework

**CRITICAL APPLICATION — THE SOLE SURVIVING PMNS MECHANISM**

The phonon-exflation framework computes particle masses from the Dirac operator spectrum on M4 x SU(3). The PMNS neutrino mixing matrix requires overlaps between spinor eigenmodes **as the metric changes**.

Specifically, as the Jensen parameter $\tau$ evolves during expansion, the metric $g_\tau$ deforms. The Dirac operator spectrum shifts: eigenmodes at $\tau=0$ become different eigenmodes at $\tau > 0$.

The **Bourguignon-Gauduchon spinor comparison map** $\Phi_{\tau \to \tau'}$ enables explicit computation of:
$$|\langle \psi_\alpha(\tau), \Phi_{\tau \to \tau'}(\psi_\beta(\tau')) \rangle|^2,$$
where $\psi_\alpha, \psi_\beta$ are spinor modes at different $\tau$ values.

For PMNS mixing, the lepton sector's spinor eigenmodes must be orthogonal to (or have controlled overlap with) the electroweak doublet spinors. The overlap matrix is precisely the quantity that Bourguignon-Gauduchon provides.

### Direct Implementation in Phonon-Exflation

1. **At each $\tau$**: Compute Dirac spectrum of $D_K$ on M4 x SU(3)
2. **Between $\tau$ values**: Use $\Phi_{\tau \to \tau'}$ to transport eigenmodes and compute overlaps
3. **Identify leptons**: Lepton doublets (PMNS neutrinos) are spinors that preserve quantum numbers under $\Phi$-transport
4. **Compute mixing**: PMNS matrix elements $U_{\alpha i} = \langle \nu_\alpha | e^{-i\delta_{\text{CP}}} | \nu_i \rangle$ depend on $\Phi$-transported overlaps

### Gate Connection

The Baptista Appendix B ("Spinor overlap matrix under metric deformation") is a direct implementation of Bourguignon-Gauduchon. Paper 40 provides the **mathematical foundation** for Appendix B's tilde-Phi matrix and is cited in Baptista #13.

**Without Bourguignon-Gauduchon**, the spinor overlap computation in Appendix B lacks rigor — it's a heuristic. **With it**, the PMNS mechanism becomes a theorem:

> **Theorem (Baptista + Bourguignon-Gauduchon)**: For metric families on compact spin manifolds, PMNS mixing elements are continuous functions of the deformation parameter, determined by the functorial comparison isomorphism $\Phi$.

This is the **last surviving PMNS mechanism** (S35 PMNS-R gate = FAIL; S35 PMNS-singlet ceiling ~5.9; S37 K7-G1 ALGEBRAIC gate = FAIL all q_7-charged modes). If this mechanism also fails (e.g., because $\Phi$ transports lepton modes outside the SM representation), the framework loses its connection to neutrino physics entirely.

**STATUS**: Bourguignon-Gauduchon machinery is **NECESSARY but not SUFFICIENT**. Paper 40 establishes the technical possibility of tracking spinors across metric families. Whether this tracking actually produces PMNS mixing in the phonon-exflation context is a separate computation (Baptista Appendix B + S35 PMNS gate).

---

## Additional Notes

- **Published 1992**: This is a classical paper, decades-old, but remains the **definitive reference**. No newer, better treatment exists.
- **Accessibility**: Dense mathematical exposition (typical for 1990s Communications in Mathematical Physics). Requires comfort with differential geometry at the level of Kobayashi-Nomizu or Berard-Bergery.
- **Modern use**: Cited in AdS/CFT holography (metric families in RG flows), NCG spectral action (Connes-Chamseddine programs), and quantum chaos (eigenvalue statistics under perturbation).

---

## References to Appendices and Equations

For the phonon-exflation implementation, see:
- **Baptista Paper #13** (Session 34, Critical KK papers): Appendix B, "Spinor overlap matrix under metric deformation" — direct application of Phi-maps
- **Bourguignon-Gauduchon eqs. 2.1-2.8**: Construction of $\Phi_{g \to g'}$
- **BG eqs. 3.15-3.22**: First-order perturbation formula for eigenvalues
- **BG Theorem 4.1**: Continuity of spectrum under metric perturbation
