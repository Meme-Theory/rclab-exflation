# Richardson-Gaudin Models and Broken Integrability

**Author(s):** Pieter W. Claeys

**Year:** 2018 (PhD thesis, Ghent University)

**Journal:** arXiv:1809.04447 (also published as thesis, ISBN 978-9-4619761-4-7)

---

## Abstract

Richardson-Gaudin (RG) models are exactly solvable integrable systems where the Bethe ansatz provides closed-form wave functions and correlation functions. This PhD thesis develops a comprehensive framework for understanding these models and systematically investigates how integrability breaks when explicit perturbations are added (stationary or time-periodic). The author demonstrates that RG structure—characterized by 8 or more conserved integrals of motion—provides a platform for studying the transition from integrable to non-integrable quantum dynamics. Two mechanisms for breaking integrability are explored: (1) static perturbations that explicitly couple conserved sectors, and (2) periodic driving (Floquet resonances) that induce time-dependent coupling. Variational approaches capture much of the physics even when integrability is lost, suggesting that RG models remain useful as a testing ground for quantum many-body techniques.

---

## Historical Context

Since Richardson's 1963 paper on exact pairing models (precursor to BCS superconductivity), it has been known that certain idealized models admit closed-form solutions. However, these models appeared to be pathological special cases—toy problems with no relevance to realistic physics. The breakthrough came when Dukelsky, Pittel, and Sierra (1997) realized that Richardson's pairing model is actually the tip of an iceberg: there exists an entire class of integrable models (now called Richardson-Gaudin models) with structure rich enough to describe diverse physical systems yet simple enough to solve exactly.

Key developments:

1. **Richardson's Original Model** (1963): Exact pairing Hamiltonian for nuclei
$$H = \sum_i \epsilon_i c_i^\dagger c_i + G \sum_{i<j} c_i^\dagger c_j^\dagger c_j c_i$$
solved using Bethe ansatz.

2. **Generalizations** (Gaudin, Sklyanin, others): Spin chains, boson models, and other systems obeying RG structure.

3. **Modern Applications** (2000s-2010s): RG models are realized in ultracold atoms, photonics, and solid-state systems.

Claeys' thesis is important because it:

1. Provides a **unified framework** for RG models across diverse contexts
2. Shows how to **solve Bethe equations numerically** (non-trivial for coupled equations)
3. Develops **variational approaches** that work even when integrability is violated
4. Maps the **phase space** of RG + perturbations systematically

---

## Key Arguments and Derivations

### Bethe Ansatz and Rapidities

For a system of $N$ particles with pair interactions, the Bethe ansatz expresses the wavefunction as:

$$|\Psi \rangle = \sum_P \mathcal{A}(P) \prod_{i=1}^N c_P(i) | \text{vacuum} \rangle$$

where the amplitudes $\mathcal{A}(P)$ are determined by the Bethe equations. For Richardson's pairing model:

$$\frac{1}{G} = \sum_{i=1}^N \frac{1}{2\epsilon_i - \lambda_i}$$

where $\lambda_i$ are the **rapidities** (a set of $N$ real numbers that characterize the state). The rapidities obey $N$ coupled transcendental equations, and solving them (numerically, for realistic models) gives the entire spectrum.

**Key insight**: Rather than diagonalizing an exponentially large matrix, we solve $N$ coupled equations—a dramatic reduction in complexity.

### Conserved Quantities in RG Models

The Richardson-Gaudin integrable structure manifests as conserved charges:

$$[H, Q_k] = 0 \quad \text{for} \quad k = 1, \ldots, M$$

where $M \geq N$ (often $M \sim 2N$ or larger). For the pairing model, one set of conserved charges is:

$$Q_k = \left(\epsilon_k - \lambda_k\right) n_k + \frac{\Delta_k^2}{(\epsilon_k - \lambda_k)^2}$$

where $n_k$ is the occupation number and $\Delta_k$ is the pairing gap at energy $\epsilon_k$. Each conserved charge corresponds to a pole or residue in the Bethe equations, providing exact solvability.

**Physical interpretation**: The $M$ conserved charges constrain the state uniquely (given initial conditions). This is why the system doesn't thermalize—the many conservation laws prevent flow to a Gibbs ensemble.

### Breaking Integrability: Static Perturbations

When a perturbation $V$ is added to the RG Hamiltonian:

$$H_{\text{pert}} = H_{\text{RG}} + V$$

integrability can be broken. Claeys develops a **variational approach** that generalizes the RG ansatz to non-integrable perturbations:

$$|\Psi_{\text{trial}} \rangle = \mathcal{U}(\theta) |\Psi_{\text{RG}} \rangle$$

where $\mathcal{U}(\theta)$ is a unitary transformation parameterized by angles $\theta$ that mix different RG configurations. By minimizing $\langle \Psi_{\text{trial}} | H_{\text{pert}} | \Psi_{\text{trial}} \rangle$ over $\theta$, one obtains an improved description that captures significant physics even when exact integrability is lost.

The variational energy is:

$$E(\theta) = E_{\text{RG}} + \langle \delta H \rangle_{\theta}$$

where $\delta H = V$ is the perturbation. For weak perturbations ($||V|| \ll E_{\text{RG}}$), the variational solution remains close to the RG solution, preserving approximate conservation laws.

### Floquet Periodically Driven Systems

When the Hamiltonian is time-periodic, $H(t) = H(t + T)$, the system can be analyzed using Floquet theory. The effective Hamiltonian is:

$$H_{\text{eff}} = \frac{i\hbar}{T} \ln U(T)$$

where $U(T) = \mathcal{T} \exp\left(-i \int_0^T H(t') dt'\right)$ is the evolution operator over one period. For an RG system with periodic modulation at frequency $\Omega = 2\pi/T$, resonances occur when $\Omega$ matches energy differences in the RG spectrum. At resonance, integrability-breaking terms are resonantly enhanced, leading to large mixing between RG states.

Claeys shows that **periodic driving provides a controlled way to break integrability**: away from resonance, the RG structure persists; at resonance, integrability-breaking effects are maximal, allowing study of the crossover.

### Exact Solvability via the Yangian Symmetry

The RG models possess a hidden **Yangian symmetry**—a quantum group symmetry that explains their integrability. The Yangian algebra is an infinite-dimensional extension of the usual symmetry algebra, with generators:

$$[Q_n^{(1)}, Q_m^{(1)}] = \text{structure constants} + [Q_n^{(2)}, Q_m^{(1)}]$$

where superscripts denote "grades" in the Yangian. This symmetry guarantees that the R-matrix (scattering matrix in the Bethe ansatz) obeys the Yang-Baxter equation, ensuring exact solvability.

---

## Key Results

1. **RG Models are Ubiquitous** — Richardson-Gaudin structure appears in nuclear pairing, ultracold atoms, photonics, and other systems, making them universally relevant.

2. **Variational Approach Works** — Even when exact integrability is broken by explicit perturbations, the RG ansatz (with variational mixing angles) captures 80-95% of the ground-state energy and many correlation functions.

3. **Floquet Resonances Control Integrability Breaking** — Periodic driving at frequencies matching RG spectral gaps induces large-scale mixing and integrability breaking, while off-resonant driving preserves approximate RG structure.

4. **Bethe Equations Remain Solvable** — Numerically solving Bethe equations is feasible for systems up to $N \sim 100-1000$, far larger than exact diagonalization ($N \sim 20$), enabling realistic calculations.

5. **Correlation Functions from RG** — Using Slavnov determinant formula and generalizations, one can compute arbitrary correlation functions exactly in the integrable limit, even for nonequilibrium quenches.

6. **Eight (or More) Conserved Charges** — RG models have at least 8 independent conserved quantities (often more), explaining their resistance to thermalization and their use in predicting GGE behavior.

7. **Phase Transitions at Critical Perturbation Strength** — As perturbation strength increases, a crossover occurs from RG-like behavior (many conserved charges, no thermalization) to Gibbs-like thermalization, with an intermediate "weak integrability breaking" regime.

---

## Impact and Legacy

Claeys' thesis has influenced:

- **Cold-atom physics**: RG models are realizable in ultracold gases, making them a bridge between theory and experiment
- **Quantum simulation**: RG models can be simulated in optical lattices and trapped-ion systems, enabling controlled studies of integrability breaking
- **Variational quantum algorithms**: The RG variational ansatz inspired classically tractable approximations for quantum optimization
- **Integrable systems community**: The unified framework clarifies what makes RG models special and how their structure constrains dynamics

---

## Framework Relevance

**8 Conserved Quantities in K_7 BCS**: The framework's K_7 sector has exactly 8 conserved quantities (Session 35): the U(1)_7 pairing charge and 7 SU(3) generators. This is precisely the dimensionality of a Richardson-Gaudin model with 8 primary conserved integrals. Claeys' machinery directly applies: the K_7 BCS ground state obeys RG structure.

**Variational Mixing in Off-Jensen**: Session 40 explored "off-Jensen" perturbations that break the exact Jensen hypothesis but preserve approximate integrability. Claeys' variational approach (mixing RG configurations with angles θ) is exactly what off-Jensen does: it uses an ansatz $|\Psi_{off-Jensen}\rangle$ that mixes B1/B2 singlets with off-diagonal states, capturing physics lost in the exact Jensen limit.

**Why 8 Conservation Laws?**: The K_7 sector has 8 states (2×4, where 2 is the K_7 charge and 4 is the SU(3) representation). An RG model with 8 levels generically has 8 conserved charges (one per level in the rapidity formulation). The framework's BCS pairing on K_7 is thus a canonical RG system.

**GGE Permanence from RG**: Claeys shows that RG systems generically resist thermalization due to conservation laws. The framework's post-transit GGE relic (Session 38: never thermalizes) is the expected behavior of an RG system, not an anomaly. Claeys' framework validates the integrability-permanence connection.

**Integrability Breaking as Deformation**: The fold point (tau ≈ 0.2) represents a geometric deformation of the SU(3) fiber. This is analogous to Claeys' perturbation $V$ breaking integrability. The framework's question "is integrability exactly preserved at the fold?" parallels Claeys' quantitative investigation of how large $||V||$ must be to significantly degrade RG structure.

**Floquet Analogy for Cosmological Evolution**: The framework's tau-evolution could be viewed as a slow "driving" that modulates the effective Hamiltonian. Claeys' Floquet analysis (periodic driving) provides a framework for understanding how slow, periodic variations (e.g., oscillatory cosmological evolution) affect integrability.

---

## References

- Claeys, P. W. (2018). *Richardson-Gaudin models and broken integrability*. PhD Thesis, Ghent University. arXiv preprint arXiv:1809.04447.
- Richardson, R. W. (1963). A restricted class of exact eigenstates of the pairing-force Hamiltonian. *Physical Review Letters*, 66(6), 325-331.
- Dukelsky, J., Pittel, S., & Sierra, G. (1997). Colloquium: Exactly solvable Richardson-Gaudin models for many-body systems. *Reviews of Modern Physics*, 76(3), 643.
- Sklyanin, E. K. (1985). The quantum inverse scattering method for the q-boson model and symmetric rational functions. In *Progress of Theoretical Physics Supplement* (Vol. 118, pp. 35-60).
