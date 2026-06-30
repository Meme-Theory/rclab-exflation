# Berry phase, topology, and diabolicity in quantum nano-magnets

**Author(s):** Patrick Bruno
**Year:** 2005
**Journal:** [not stated in PDF; preprint]
**arXiv:** quant-ph/0511186
**Relevance:** MEDIUM

---

## Abstract

A topological theory of the diabolical points (degeneracies) of quantum magnets is presented. Diabolical points are characterized by their diabolicity index, for which topological sum rules are derived. The paradox of the missing diabolical points for Fe8 molecular magnets is clarified. A new method is also developed to provide a simple interpretation, in terms of destructive interferences due to the Berry phase, of the complete set of diabolical points found in biaxial systems such as Fe8.

---

## Key Arguments and Derivations

### Diabolical Points and the von Neumann-Wigner Theorem

The paper begins from the von Neumann-Wigner theorem: in a family of parameter-dependent Hermitian Hamiltonians, accidental degeneracies of two successive eigenvalues occur on submanifolds of codimension 3 of the parameter manifold. For a Hamiltonian depending on 3 external real parameters (e.g., the 3 components of magnetic field), degeneracies are isolated points -- the "diabolical points," named for the double-cone (diabolo) shape of eigenenergy surfaces near degeneracies.

Berry showed these diabolical points behave as magnetic monopoles in parameter space: a system adiabatically transported around a closed circuit near a diabolical point acquires a Berry phase proportional to the enclosed solid angle. The Berry curvature is divergenceless except at diabolical points, where monopole sources are located.

### Topological Characterization via Diabolicity Index

For a spin-J system with Hamiltonian H = H_0(J) - H . J, the paper defines a diabolicity index for each diabolical point. The topological charge Q_i(mu) is the Chern number obtained from the flux of Berry curvature through a surface enclosing the diabolical point. Two topological sum rules are derived: (i) for each diabolical point, the sum of topological charges over all levels vanishes; (ii) summing over all diabolical points for a given level yields 2*mu.

The diabolicity index D for pairs of successive levels satisfies sum rules that constrain the total count and distribution of diabolical points. For the biaxial system, all diabolical points have diabolicity index 1.

### The Fe8 Missing Diabolical Points Paradox

For the biaxial Hamiltonian H_0 = -K J_z^2 + D(J_x^2 - J_y^2), the exact locations of diabolical points are given analytically. Only 4 of the predicted 10 diabolical points were observed in Fe8 experiments. Bruno shows that adding a small fourth-order tetragonal anisotropy C(J_+^4 + J_-^4) causes diabolical points to migrate: they collide on the hard axis and bifurcate away, preserving the topological sum rules. The "missing" points are displaced, not destroyed.

### Berry Phase Interpretation via Enlarged Hilbert Space

To interpret diabolical points at nonzero H_z as due to Berry phase interference, Bruno introduces an enlarged Hilbert space of 2J spins-1/2. This maps the original tunneling problem onto that of a fictitious spin J_tilde = J - j in an effective field H_z^eff = H_z - 2jK. The Wess-Zumino (Berry phase) action S_WZ = i*M_tilde * integral of (1 - cos theta_u) d*phi_u governs the quantum interference. The parity alternation discovered experimentally (integer vs. half-integer J_tilde) is naturally explained.

## Key Results

1. Diabolical points are topologically characterized by their diabolicity index, with sum rules constraining their distribution.
2. The sum rule for topological charges: sum_i Q_i(mu) = 2*mu.
3. The total diabolicity is D = 2J(J+1)(2J+1)/3.
4. The "missing" diabolical points in Fe8 are not destroyed but displaced by higher-order anisotropy, preserving topological sum rules.
5. All diabolical points in biaxial systems can be interpreted as destructive Berry phase interference via an enlarged Hilbert space mapping.
6. Conjecture: a spin Hamiltonian H_0 is completely determined by its set of diabolical points and diabolicity indices (plus its trace).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Diabolical point locations (z) | $H_z = (M - M')H_z^0$ | Eq. (1a) |
| Diabolical point locations (x) | $H_x = \left(\frac{M + M' - 1}{2} - n\right)H_x^0$ | Eq. (1b) |
| Characteristic fields | $H_x^0 \equiv 2\sqrt{2D(K+D)},\quad H_z^0 \equiv \sqrt{K^2 - D^2}$ | Below Eq. (1b) |
| Berry curvature | $\mathbf{B}_{(\mu)} \equiv -\mathrm{Im}\sum_{\mu'\neq\mu}\frac{\langle\mu\mid\hat{\mathbf{J}}\mid\mu'\rangle \times \langle\mu'\mid\hat{\mathbf{J}}\mid\mu\rangle}{(E_\mu - E_{\mu'})^2}$ | Sec. 2 |
| Topological charge (Chern number) | $Q_{i(\mu)} \equiv \frac{-1}{2\pi}\oint_{\Sigma_i}\mathbf{B}_{(\mu)}\cdot d\mathbf{S} \in \mathbb{Z}$ | Sec. 2 |
| Sum rule (per level) | $\sum_i \mathcal{D}^{(\mu-1)}_{i(\mu)} = (J+\mu)(J-(\mu-1))$ | Eq. (2a) |
| Total diabolicity | $\mathcal{D} = \frac{2J(J+1)(2J+1)}{3}$ | Eq. (2b) |
| Wess-Zumino action | $\mathcal{S}_{WZ}[\mathbf{u}(\tau)] = i\tilde{M}\int(1-\cos\theta_{\mathbf{u}})\,d\varphi_{\mathbf{u}}$ | Sec. 4 |

## Relevance to Phonon-Exflation

Diabolical points -- parameter-space degeneracies acting as Berry curvature monopoles -- are directly relevant to the fold catastrophe structure in the phonon-exflation framework, where the Dirac spectrum on M4 x SU(3) passes through degeneracies as the compactification parameter tau evolves. The topological sum rules for diabolicity indices mirror the Chern number quantization governing the spectral action. The Fe8 paradox resolution (displaced, not destroyed degeneracies under perturbation) provides a concrete physical example of how topological invariants constrain spectral flow even when the Hamiltonian is perturbed -- directly analogous to the framework's robustness under higher-order corrections to the KK fiber.
