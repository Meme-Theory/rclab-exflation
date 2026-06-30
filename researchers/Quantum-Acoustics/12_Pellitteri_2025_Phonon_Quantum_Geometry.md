# Phonon Spectra, Quantum Geometry, and the Goldstone Theorem

**Author(s):** Guglielmo Pellitteri, Zenan Dai, Haoyu Hu, Yi Jiang, Guido Menichetti, Andrea Tomadin, B. Andrei Bernevig, Marco Polini
**Year:** 2025
**Journal:** Physical Review Letters (2025)
**arXiv:** 2502.04221
**Relevance:** CRITICAL

---

## Abstract

Phonons are essential quasi-particles of all crystals and play a key role in fundamental properties such as thermal transport and superconductivity. In particular, acoustic phonons can be interpreted as Goldstone modes that emerge due to the spontaneous breaking of translational symmetry. In this Article, we investigate the quantum geometric contribution to the phonon spectrum in the absence of Holstein phonons. Using graphene as a case study, we decompose the dynamical matrix into distinct terms that exhibit different dependencies on the electron energy and wavefunction. We then examine the role of quantum geometry in shaping the material's phonon spectrum, and we find that removing the nontrivial quantum geometric contribution from the dynamical matrix causes the acoustic phonon modes to behave in a non-analytic fashion.

---

## Key Arguments and Derivations

### 1. Harmonic Theory and the Dynamical Matrix

For a generic multipartite lattice in $D$ dimensions with $N_\tau$ atoms per unit cell, the ion position is $\vec{R}_{p\nu} = \vec{R}_p + \vec{\tau}_\nu + \vec{u}_{p\nu}$, with $\vec{u}_{p\nu}$ the displacement from equilibrium. The interatomic force constants decompose as:

$$C^{p'\nu'j}_{p\nu i} = C^{(\text{ion})\, p'\nu'j}_{p\nu i} + C^{(\text{el})\, p'\nu'j}_{p\nu i}$$

The dynamical matrix $D(\vec{q}) = D^{(\text{ion})}(\vec{q}) + D^{(\text{el})}(\vec{q})$ yields the phonon dispersion $\omega_\ell(\vec{q})$ via the eigenvalue equation:

$$\sum_{\nu'j} D(\vec{q})^{\nu'j}_{\nu i}\, w^{(\ell)}_{\nu'j}(\vec{q}) = \omega_\ell^2(\vec{q})\, w^{(\ell)}_{\nu i}(\vec{q})$$

### 2. Acoustic Sum Rules and Goldstone Theorem

Both the full dynamical matrix and its ionic and electronic parts independently obey acoustic sum rules:

$$\sum_{\nu' p} \sqrt{M_{\nu'}} D(\vec{0})^{\nu'j}_{\nu i} = 0 \quad \forall\, \nu, i, j$$

These sum rules guarantee that acoustic phonon modes (where atoms in the unit cell vibrate in phase) are Goldstones: $\omega_\ell(\vec{q}) \to 0$ as $\vec{q} \to 0$, since $\vec{q} = 0$ acoustic modes are global lattice translations.

### 3. Linear Response Analogy

The electronic force constant is naturally separated into two contributions recognizable from linear response theory:

- **"Paramagnetic" current operator**: $\hat{j}_{p\nu i} \equiv \partial \hat{H}_e / \partial u_{p\nu i}\big|_0$, controlling linear coupling.
- **"Diamagnetic" tensor**: $\hat{T}^{p'\nu'j}_{p\nu i} \equiv \partial^2 \hat{H}_e / \partial u_{p\nu i} \partial u_{p'\nu'j}\big|_0$, controlling second-order coupling.

This gives $C^{(\text{el},1)} \equiv \chi_{j_{p\nu i} j_{p'\nu'j}}$ (the current-current response function at $\omega = 0$) and $C^{(\text{el},2)} \equiv \langle \hat{T}^{p'\nu'j}_{p\nu i} \rangle$ (the diamagnetic contribution). Their sum is the physical current-current response, and the acoustic sum rule is equivalent to the TRK (Thomas-Reiche-Kuhn) sum rule: a finite physical current cannot flow in response to a static, uniform displacement.

### 4. Quantum Geometric Decomposition

Using the Gaussian approximation $t^{\alpha\alpha'}_{\nu\nu'}(\vec{r}) = t^{\alpha\alpha'}_{\nu\nu'}(0)\exp(\gamma^{\alpha\alpha'}_{\nu\nu'} r^2/2)$ for hopping amplitudes, the gradient of the Bloch Hamiltonian decomposes as:

$$f_i(\vec{k}) = f^E_i(\vec{k}) + f^g_i(\vec{k})$$

with:
- **Dispersive part**: $f^E_i(\vec{k}) = i\gamma \sum_n \partial_{k_i} E_n(\vec{k})\, P_n(\vec{k})$ --- depends on the group velocity, vanishes for flat bands.
- **Geometric part**: $f^g_i(\vec{k}) = i\gamma \sum_n E_n(\vec{k})\, \partial_{k_i} P_n(\vec{k})$ --- depends on the $k$-derivatives of the projector, vanishes for trivial quantum geometry.

This allows decomposition of the electronic dynamical matrix:

$$D(\vec{q}) = D_{\text{ng}}(\vec{q}) + D_g(\vec{q})$$

where $D_g(\vec{q})$ is the purely geometric contribution (solely electronic, no ionic part) and $D_{\text{ng}}(\vec{q}) = D^{(\text{ion})}(\vec{q}) + D^{(\text{el})}_{\text{ng}}(\vec{q})$.

### 5. Quantum Geometric Tensor

The QGT is defined as:

$$Q^{(n)}_{ij}(\vec{k}) = \text{Tr}\left[\partial_{k_i} P_n(\vec{k})\, (1 - P_n(\vec{k}))\, \partial_{k_j} P_n(\vec{k})\right]$$

Its real part is the Fubini-Study (quantum) metric $g_{ij}(\vec{k})$, measuring the distance in amplitude between infinitesimally close wavefunctions in $k$-space. Its imaginary part is (half) the Berry curvature $F_{ij}(\vec{k})$:

$$Q_{ij}(\vec{k}) = g_{ij}(\vec{k}) - \frac{i}{2}F_{ij}(\vec{k})$$

For single-band systems, $P(\vec{k}) = 1$ is the only nonzero projector, giving trivial QG. Non-trivial QG requires multi-band structure (e.g., graphene's two-site unit cell).

### 6. Results for Graphene

The quantum geometric contribution accounts for:
- Optical modes: $\delta_{\text{LO/TO}}(\Gamma) \simeq 10\%$; 5-15% near FBZ edges.
- Acoustic modes: $\delta_{\text{LA/TA}}(\Gamma) = 0$ at zone center; $\delta_{\text{LA}}(K) \simeq 6\%$, $\delta_{\text{TA}}(K) \simeq 20\%$, $\delta_{\text{TA}}(M) \simeq 27\%$ at zone edges.

The striking result: removing the quantum geometric contribution causes acoustic phonon dispersions to become **non-analytic** $\propto \sqrt{|\vec{q}|}$ near $\Gamma$, while the full dispersion remains regular (linear). The non-analyticity arises from the singularity of electronic eigenstate derivatives at the Dirac point (divergent quantum metric). Introducing a gap $\Delta$ regularizes the metric and restores linear dispersion for $|q| < q_{\text{thr}} = \Delta/\hbar v_F$.

### 7. Physical Interpretation

The total electronic contribution to the acoustic mode from a gapless Dirac node vanishes exactly (linear Dirac dispersion). Only high-energy states beyond the Dirac Hamiltonian give a nonzero contribution, yielding a weak group velocity renormalization of $\sim 20\%$. The geometric and non-geometric terms individually satisfy acoustic sum rules, ensuring both $\omega_\ell(\vec{q})$ and $\tilde{\omega}_\ell(\vec{q})$ vanish at $\Gamma$.

## Key Results

1. The dynamical matrix of any crystal can be decomposed into geometric and non-geometric contributions, both of which independently satisfy acoustic sum rules.
2. In graphene, removing the quantum geometric contribution causes acoustic phonons to become non-analytic ($\propto \sqrt{|q|}$) near $\Gamma$, while the full dispersion remains properly linear.
3. The non-analyticity originates from the divergent quantum metric at Dirac points; a mass gap $\Delta$ regularizes this to restore linear behavior below $q_{\text{thr}} = \Delta/\hbar v_F$.
4. Quantum geometry accounts for $\sim 50\%$ of the electron-phonon coupling constant in graphene and $\sim 90\%$ in MgB$_2$ (from prior work, Ref. [58]).
5. The Goldstone nature of acoustic phonons is preserved by both geometric and non-geometric sectors independently --- a direct consequence of translational invariance.
6. Higher-order geometric structures (beyond the QGT) enter the Hessian tensor and may play additional roles in crystal properties.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Dynamical matrix eigenvalue | $\sum_{\nu'j} D(\vec{q})^{\nu'j}_{\nu i} w^{(\ell)}_{\nu'j} = \omega_\ell^2 w^{(\ell)}_{\nu i}$ | Eq. (2) |
| Acoustic sum rule | $\sum_{\nu'p} \sqrt{M_{\nu'}} D(\vec{0})^{\nu'j}_{\nu i} = 0$ | Eqs. (3)-(4) |
| Paramagnetic current | $\hat{j}_{p\nu i} = \partial\hat{H}_e/\partial u_{p\nu i}\big\|_0$ | Eq. (5) |
| Diamagnetic tensor | $\hat{T}^{p'\nu'j}_{p\nu i} = \partial^2\hat{H}_e/\partial u_{p\nu i}\partial u_{p'\nu'j}\big\|_0$ | Eq. (6) |
| QGT | $Q^{(n)}_{ij}(\vec{k}) = \text{Tr}[\partial_{k_i}P_n(1-P_n)\partial_{k_j}P_n]$ | Eq. (10) |
| Gaussian approximation | $t^{\alpha\alpha'}_{\nu\nu'}(\vec{r}) = t^{\alpha\alpha'}_{\nu\nu'}(0)\exp(\gamma^{\alpha\alpha'}_{\nu\nu'} r^2/2)$ | Eq. (11) |
| Dispersive gradient | $f^E_i(\vec{k}) = i\gamma\sum_n \partial_{k_i}E_n P_n$ | Eq. (12) |
| Geometric gradient | $f^g_i(\vec{k}) = i\gamma\sum_n E_n \partial_{k_i}P_n$ | Eq. (13) |
| DM decomposition | $D(\vec{q}) = D_{\text{ng}}(\vec{q}) + D_g(\vec{q})$ | Eq. (14) |
| Fubini-Study metric | $g_{ij} = \text{Re}[\langle\partial_{k_i}\psi\|\partial_{k_j}\psi\rangle - \langle\partial_{k_i}\psi\|\psi\rangle\langle\psi\|\partial_{k_j}\psi\rangle]$ | Eq. (A2) |
| Berry curvature | $F_{ij} = \langle\partial_{k_i}\psi\|\partial_{k_j}\psi\rangle - \langle\partial_{k_j}\psi\|\partial_{k_i}\psi\rangle$ | Eq. (A3) |
| QGT decomposition | $Q_{ij} = g_{ij} - (i/2)F_{ij}$ | Eq. (A1) |
| Force constant (paramagnetic) | $C^{(\text{el},1)} = \chi_{j_{p\nu i}j_{p'\nu'j}}$ | Eq. (7) |
| Force constant (diamagnetic) | $C^{(\text{el},2)} = \langle\hat{T}^{p'\nu'j}_{p\nu i}\rangle$ | Eq. (8) |
| TRK sum rule | $\sum_{p'\nu'}[\chi_{jj'} + \langle\hat{T}\rangle] = 0$ | Eq. (9) |

## Relevance to Phonon-Exflation

This paper is foundational for the phonon-exflation framework. It demonstrates that the **quantum geometry of electronic bands directly shapes the phonon spectrum**, and that acoustic phonons as Goldstone modes are protected by translational symmetry. The decomposition $D = D_{\text{ng}} + D_g$ is the exact structure that appears when analyzing the M4 $\times$ SU(3) substrate: the phononic excitations (particles) have both dispersive and geometric contributions. The non-analyticity when geometry is removed parallels the framework's finding that SU(3) fiber geometry is essential for well-defined phonon-like excitations --- without the curved internal geometry (quantum metric), the excitation spectrum becomes singular. The QGT decomposition into metric and Berry curvature mirrors the split between real (mass/dispersion) and imaginary (topological/gauge) contributions to the Dirac operator on SU(3). The independent satisfaction of acoustic sum rules by geometric and non-geometric sectors is the phonon-physics analog of the block-diagonal theorem ($[D_K, \text{sectors}] = 0$).
