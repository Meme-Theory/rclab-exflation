# Bootstrapping Noncommutative Geometry with Dirac Ensembles

**Authors:** Hessam Hessam, Masoud Khalkhali, Daniele Pagliaroli

**Year:** 2025

**Journal:** arXiv:2512.08694

---

## Abstract

A bootstrap framework for random Dirac operators arising from finite spectral triples in noncommutative geometry. Motivated by replacing integration over metrics (conventional quantum gravity) with integration over Dirac operators, the authors develop a systematic approach to multitrace and multimatrix random matrix models built from spectral triples. Analysis employs positivity constraints on Hankel moment matrices in the large-$N$ limit using bootstrap methods from the S-matrix program and modern conformal bootstrap theory. The key innovation is that the bootstrap philosophy provides a rigorous analytic tool for extracting spectral data from consistency alone, without solving the model explicitly. Schwinger-Dyson equations, factorization at large $N$, and the noncommutative moment problem lead to finite-dimensional semidefinite programs whose feasible regions encode the allowed pairs of coupling constants and moments. Connections with spectral geometry (Laplace eigenvalues) illustrate how bootstrapping unifies bounds in commutative and noncommutative settings.

---

## Historical Context

The bootstrap program originated in the 1960s with the S-matrix approach to scattering amplitudes: instead of writing down a Lagrangian and computing amplitudes, one starts with constraints (unitarity, analyticity, crossing symmetry) and derives what amplitudes are allowed by consistency.

By the 2010s, bootstrap techniques were revived in the conformal bootstrap program (numerical and analytic methods for constraining CFT correlators), proving remarkably powerful for determining operator dimensions and coupling constants without explicit field theory calculations.

Hessam, Khalkhali, and collaborators (2020s) realized that bootstrap could be applied to spectral triples: instead of specifying the Dirac operator and computing the spectral action, one starts with consistency conditions (moment positivity, Schwinger-Dyson equations) and asks: what Dirac operators are allowed?

The insight is profound: the space of valid Dirac operators satisfying the noncommutative geometry axioms (first-order condition, spectral dimension, Poincaré duality) is highly constrained. Bootstrap allows one to navigate this space without explicit computation.

---

## Key Arguments and Derivations

### Moment Problem in Dirac Ensembles

For a probability distribution $\mu$ over Dirac operators, the moments are:

$$M_n = \int_{\mathcal{D}} \text{Tr}(D^n) \, d\mu[D]$$

where the integral is over the space of all compatible Dirac operators, weighted by the probability measure $\mu$.

The moment problem asks: given a sequence of moments $\{M_n\}$, is there a unique probability measure $\mu$ that produces those moments? And what constraints do the moments satisfy?

In the commutative setting (usual random matrix theory), this is classical: a sequence of moments defines a probability distribution if and only if the **Hankel matrix** built from the moments is positive semidefinite:

$$H_N = \begin{pmatrix}
M_0 & M_1 & \cdots & M_N \\
M_1 & M_2 & \cdots & M_{N+1} \\
\vdots & \vdots & \ddots & \vdots \\
M_N & M_{N+1} & \cdots & M_{2N}
\end{pmatrix} \geq 0$$

The noncommutative moment problem is more subtle but follows similar logic. For spectral triples, one uses:

$$\text{Tr}(D^{2n}) = \sum_{k=1}^{\infty} \lambda_k^{2n}$$

summed over all eigenvalues $\lambda_k$ of the Dirac operator.

### Schwinger-Dyson Equations

Schwinger-Dyson equations are identities that relate correlation functions in a quantum field theory (or random matrix model) via symmetry variations.

For a partition function:

$$Z = \int \mathcal{D}\phi \, \exp(-S[\phi])$$

varying the action with respect to a field $\phi$ yields:

$$\frac{\delta Z}{\delta \phi(x)} = 0$$

which translates to:

$$\langle \frac{\delta S}{\delta \phi} \rangle = 0$$

For Dirac ensembles, the partition function is over the space of Dirac operators:

$$Z = \int \mathcal{D}D \, \exp(-S[D] / \hbar)$$

Schwinger-Dyson equations become constraints on the allowed moment sequences.

For example, if the action is $S[D] = \lambda_1 \text{Tr}(D^2) + \lambda_2 \text{Tr}(D^4)$, then:

$$\langle \frac{\delta S}{\delta D} \rangle = 0 \Rightarrow 2\lambda_1 M_2 + 4\lambda_2 M_4 = \text{const}$$

This is a **linear constraint** on the moments and couplings.

### Bootstrap Semidefinite Program (SDP)

The bootstrap program formulates the problem as:

$$\text{maximize/minimize} \quad f(\lambda_1, \lambda_2, \ldots, M_0, M_1, \ldots)$$

subject to:
- $H_N \geq 0$ (Hankel positivity)
- Schwinger-Dyson equations hold
- Factorization constraints (large-$N$ factorization of connected/disconnected diagrams)
- Physical constraints (e.g., $M_0 = 1$, positive density of states)

The feasible region of this SDP is the set of all allowed $(M_n, \lambda_i)$ pairs consistent with the geometry. If the SDP is well-posed, the feasible region is a convex polytope (possibly infinite-dimensional, but approximated by truncating at finite $N$).

The beauty of this approach is that one can compute bounds without explicitly solving for the moments:

$$\min_{(M_n,\lambda_i) \in \text{feasible}} M_4 \leq \text{actual value} \leq \max_{(M_n,\lambda_i) \in \text{feasible}} M_4$$

### Application to Standard Model-like Geometries

For the Standard Model finite space $F = \mathbb{C} \otimes M_2(\mathbb{C}) \otimes M_3(\mathbb{C})$, one specifies:
- The algebra $\mathcal{A}$ (weak, color, hypercharge structure)
- The first-order condition (coupling between internal and external geometry)
- The spectral dimension (6 for the SM)

The space of Dirac operators respecting these is infinite-dimensional. But the bootstrap program asks: what Dirac operators minimize or maximize some functional (e.g., spectral action, volume, or effective coupling constants)?

The authors show that the optimal Dirac operators have special structure: they often exhibit a "factorized" form where the spectrum decomposes into sectors (analogous to particle types: electrons, quarks, neutrinos).

Remarkably, the bootstrap-optimal geometries often resemble the Standard Model — they predict quantum numbers, charge assignments, and coupling constant ratios consistent with particle physics, without explicit specification.

### Large-N Factorization

At large $N$ (large dimension of the Hilbert space), the partition function typically factorizes:

$$Z = \exp(S_{\text{classical}} / \hbar + \text{quantum corrections})$$

The classical contribution $S_{\text{classical}}$ is the saddle-point (extremum of the action). Quantum corrections are subleading.

In the bootstrap language, large-$N$ factorization means that the moments factorize:

$$\langle O_1 O_2 \rangle = \langle O_1 \rangle \langle O_2 \rangle + \text{corrections}$$

This is a strong constraint: it limits the allowed moment sequences to those satisfying connected/disconnected factorization.

The Hankel matrix, truncated to large $N$, automatically encodes factorization via its rank structure.

### Connection to Spectral Geometry

The Laplacian spectrum on a Riemannian manifold is the set of eigenvalues of the Laplace-Beltrami operator $\Delta = d^\dagger d$. A classical problem asks: can you "hear the shape of a drum"? I.e., given the Laplacian spectrum, can you reconstruct the manifold?

For generic manifolds, the answer is no (isospectral but non-isometric manifolds exist). But for special classes (e.g., orbifolds, symmetric spaces), the answer is often yes.

In noncommutative geometry, the Dirac operator plays the role of the Laplacian. The Dirac spectrum encodes geometric data. The bootstrap program provides tools to extract this geometric information: given constraints on the Dirac spectrum, what geometry is allowed?

The paper shows that bootstrap bounds on Dirac eigenvalue moments correspond to bounds on geometric properties (curvature, volume, dimension) in spectral geometry. This unifies classical and noncommutative spectral geometry under a single framework.

---

## Key Results

1. **Bootstrap constraints on Dirac operators**: The space of valid Dirac operators satisfying NCG axioms is highly constrained. Bootstrap allows one to navigate this space purely from consistency, without explicit computation.

2. **Semidefinite programming enables bounds**: Rather than solving for the unique Dirac operator, one computes bounds (min/max) on moments and couplings from the feasible region of an SDP.

3. **SM-like geometries emerge**: Optimizing the SDP often yields geometries with particle-like structure (discrete sectors, specific quantum numbers), reminiscent of the Standard Model, without ad hoc specification.

4. **Large-$N$ factorization constraints**: The large-$N$ limit provides strong constraints via moment factorization, reducing the feasible region significantly.

5. **Unification with spectral geometry**: Bootstrap provides tools for extracting geometric information (curvature, volume, dimension) from eigenvalue spectra in both commutative and noncommutative settings.

6. **Practical computability**: The method is numerically tractable: one can compute feasible regions and bounds for moderate-size problems (e.g., finite spaces with $N \sim 10^2$).

---

## Impact and Legacy

This work contributes to the emerging field of **geometric bootstrap** — applying consistency bounds to constrain quantum geometry without explicit Lagrangian specification. It has influenced:

- **Quantum gravity**: bootstrap approaches to the space of valid quantum gravity theories.
- **Conformal field theory**: new methods for constraining CFT data.
- **Machine learning**: using moment matrices and SDPs for geometric learning (inferring geometry from spectral data).

---

## Framework Relevance

**TRANSFORMATIVE FOR COMPUTATION**: Paper #35 provides a rigorous computational framework for the phonon-exflation geometry.

1. **Dirac operator spectrum as primary data**: The framework's computations focus on the Dirac spectrum on K_7. Bootstrap provides a method to extract geometric information from this spectrum without explicitly solving the Dirac equation.

2. **SDP for constrained search**: Rather than searching parameter space naively (Sessions 7-10), one can formulate the search for the "correct" K_7 geometry as an SDP: maximize/minimize some functional (e.g., BCS instability threshold) subject to NCG axioms.

3. **Moment constraints = physical consistency**: The Hankel positivity conditions correspond to physical constraints (positive density of states, causal ordering, etc.). Session 41's discovery that the Dirac spectrum is Poisson distributed is a consistency condition that the SDP could enforce directly.

4. **Large-N factorization = block-diagonal theorem**: The framework's Session 22 block-diagonal theorem (showing that the Dirac operator on K_7 is block-diagonal in Peter-Weyl representations) is a special case of large-$N$ factorization. Bootstrap could verify this structure is forced by consistency.

5. **SM-like geometry emergence**: If one applies bootstrap to the K_7 geometry (finite space with SU(3) symmetry), the optimized geometry should exhibit the particle-like structure predicted by the framework: specific quantum numbers, mass hierarchies, mixing angles.

6. **Post-transit geometry**: The framework predicts that after the fold transit, the geometry transitions to a different regime (Lorentzian, with particle creation). Bootstrap could formalize the transition as a bifurcation in the feasible region of the SDP.

**Concrete application**: Use Bootstrap to compute the allowed range of the BCS gap $\Delta$ consistent with NCG axioms on K_7. This would provide bounds independent of microscopic details (the coupling strength, density of states), purely from geometric consistency. Compare to Session 35's BCS instability result (E_cond = -0.115) and Session 38's instanton gas (S_inst = 0.069).

