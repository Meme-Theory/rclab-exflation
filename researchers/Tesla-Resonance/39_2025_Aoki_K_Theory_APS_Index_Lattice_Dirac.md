# K-Theoretic Computation of the Atiyah-Patodi-Singer Index of Lattice Dirac Operators

**Authors:** Shoto Aoki, Hidenori Fukaya, Mikio Furuta, Shinichiroh Matsuo, Tetsuya Onogi, Satoshi Yamaguchi

**Year:** 2025

**Journal:** Progress of Theoretical and Experimental Physics (PTEP), accepted

**arXiv:** 2503.23921

---

## Abstract

This paper demonstrates that Wilson Dirac operators in lattice gauge theory can be naturally embedded in K-theory and KO-theory frameworks, with spectral flow directly equaling the topological index. The authors compute the Atiyah-Singer index on flat tori and the Atiyah-Patodi-Singer (APS) index on lattices with nontrivial boundaries. No Ginsparg-Wilson relation is required. Numerical verification confirms that K and KO group formulas reproduce continuum index theorems. The work extends to mod-two index computations, providing a lattice-regularized route to topological invariant calculations essential for quantum simulations and future lattice QCD computations of topological quantities.

---

## Historical Context

Index theory—the deep mathematical framework relating topological properties of differential operators to global geometric invariants—has been central to modern theoretical physics. The Atiyah-Singer index theorem, proved in the 1960s, states that for an elliptic operator on a compact manifold, the number of zero modes (kernel dimension minus cokernel dimension) is a topological quantity independent of perturbations.

A critical challenge arises when moving to **lattices**: discretization of spacetime (necessary for numerical simulations) breaks the smooth manifold structure and makes index theory ill-defined. The Ginsparg-Wilson relation was introduced to restore chiral symmetry on the lattice, but even with this constraint, computing topological indices on lattices remained problematic—no fully satisfactory framework existed that both preserved lattice structure AND recovered continuum topology.

This paper resolves this tension by using **K-theory and KO-theory**, the natural language for topological classification of operators in various symmetry classes. The remarkable insight is that the Wilson Dirac operator—the standard discretization of the continuum Dirac operator—naturally lives in K-theory without requiring any special relation or constraint.

For the phonon-exflation framework, this is critical: the framework's internal Dirac operator $D_K$ acts on the SU(3) fiber, which can be viewed as a discrete lattice of oscillators (the "phononic crystal"). Understanding how to compute topological indices in this latticed setting is prerequisite to rigorous numerical investigations.

---

## Key Arguments and Derivations

### Wilson Dirac Operator and K-Theory

The standard Wilson Dirac operator on a 4D lattice with spacing $a$ is:

$$D_W = \sum_{\mu=1}^4 \gamma^\mu \left( \frac{\mathcal{D}_\mu^+ + \mathcal{D}_\mu^-}{2a} \right) + m$$

where $\mathcal{D}_\mu^\pm$ are forward and backward lattice differences, and $m$ is the mass parameter.

In the continuum limit $a \to 0$, $D_W \to \gamma^\mu \partial_\mu + m$, recovering the continuum Dirac operator.

The key insight is that **$D_W$ is a bounded operator** (unlike the continuum Dirac operator, which is unbounded). Its spectrum lies in a bounded region of the complex plane. This makes it a valid **Fredholm operator** in functional analysis.

The K-theory group $K^0(X)$ classifies equivalence classes of Fredholm operators on a space $X$. A Fredholm operator has:

1. **Kernel** (zero-mode subspace)
2. **Cokernel** (orthogonal complement of range)

Both are finite-dimensional for Fredholm operators. The **Fredholm index** is:

$$\text{ind}(D) = \dim(\ker D) - \dim(\text{coker } D)$$

The theorem states:

$$\boxed{\text{ind}(D_W) = \text{topological invariant independent of small perturbations}}$$

### Atiyah-Singer Index Theorem on Lattices

On a **flat torus** (lattice with periodic boundary conditions), the authors compute the index by imposing **anti-periodic boundary conditions in one temporal direction**:

$$\psi(t + L) = -\psi(t) \quad \text{(temporal)}$$
$$\psi(x_i + L) = \psi(x_i) \quad \text{(spatial)}$$

The anti-periodic condition lifts the zero mode (which would exist with periodic conditions) and is essential for computing the index correctly.

Under this choice, the index is computed via the **heat kernel** method:

$$\text{ind}(D_W) = \text{Tr}[e^{-\beta D_W^\dagger D_W}] - \text{Tr}[e^{-\beta D_W D_W^\dagger}]$$

in the limit $\beta \to 0^+$.

The authors prove numerically that:

$$\text{ind}(D_W) = \text{Chern number of the lattice bundle}$$

for a 2D Dirac operator, matching the continuum ADS prediction.

### Atiyah-Patodi-Singer Index with Boundaries

When the manifold has a boundary (e.g., a half-space or a strip), the Atiyah-Singer theorem breaks down—there is no finite-dimensional index because the operator is no longer Fredholm on the full space.

The **Atiyah-Patodi-Singer (APS) index** remedies this by introducing **spectral boundary conditions**: on the boundary, one projects onto eigenmodes with eigenvalue $> \lambda$ (a threshold parameter). This projects out the "problematic" boundary modes and restores Fredholm property.

On a lattice with a **boundary at $x = 0$**, the authors define:

$$D_W^{APS} = D_W \quad \text{for } x > 0$$

with boundary conditions specifying that at $x = 0$, only modes with $\lambda > 0$ (positive eigenvalues) are allowed.

The **APS index** is then:

$$\text{ind}_{APS}(D_W) = \dim(\ker D_W^{APS}) - \dim(\text{coker } D_W^{APS})$$

The remarkable result is:

$$\text{ind}_{APS}(D_W) = \text{(bulk Chern number)} + \text{(boundary phase shift)}$$

The boundary phase shift (determined by edge modes) gives a fractional contribution that precisely cancels the mismatch between bulk and edge, restoring index equality.

### K-Theory Formalism and Spectral Flow

The authors use the **K-theory classification** to formulate this more abstractly. In the periodic case, elements of $K^0(\mathbb{T}^d)$ (K-theory of a $d$-torus) are represented by **virtual vector bundles**:

$$[E_+] - [E_-]$$

where $E_+$ and $E_-$ are vector bundles over the torus. For the Dirac operator, $E_+$ is the bundle of positive-energy eigenmodes, $E_-$ the negative-energy bundle.

The index is the **first Chern class** of this virtual bundle:

$$\text{ind}(D) = c_1([E_+] - [E_-])$$

For the APS case, the formalism extends to K-theory relative to the boundary, denoted $K^0(X, \partial X)$, which naturally encodes the spectral boundary conditions.

### No Ginsparg-Wilson Relation Required

A critical finding is that **the Ginsparg-Wilson relation is not necessary**. The Ginsparg-Wilson relation requires:

$$\gamma_5 D_W + D_W \gamma_5 = a^2 D_W^\dagger D_W$$

This is an extra constraint imposed to preserve chiral symmetry at finite lattice spacing. The authors show that **K-theory automatically handles chirality through the formal structure of Fredholm operators**—no additional constraint needed.

This is significant because the Ginsparg-Wilson relation is difficult to implement in practice for nonabelian gauge theories and for fermions in curved space (as would arise in the phonon-exflation framework's internal SU(3) geometry).

---

## Key Results

1. **K-Theory Isomorphism:** Wilson Dirac operators on periodic lattices are in bijection with elements of $K^0(\mathbb{T}^d)$. Spectral flow equals the topological index, resolving the index-definition crisis on lattices.

2. **Continuum Recovery:** Numerical verification shows that K and KO group computations reproduce known continuum indices (Chern numbers for 2D, winding numbers for 1D) to machine precision.

3. **Boundary Extension:** The APS index extends seamlessly to lattices with nontrivial boundaries or corners. Boundary modes are naturally incorporated via the relative K-theory $K^0(X, \partial X)$.

4. **Mod-2 Classification:** For systems with time-reversal and particle-hole symmetry (BdG systems), the framework extends to $KO$-theory, capturing $\mathbb{Z}_2$ topological invariants (Majorana zero modes, topological insulators).

5. **Chiral Symmetry Preserved:** No Ginsparg-Wilson constraint required. Chiral properties are captured by the $K^1$ group (odd K-theory), automatically accounting for the $\gamma_5$ structure.

6. **Computational Advantage:** For lattice simulations, this provides a direct pathway to compute topological invariants without ad hoc relations or artificial cutoffs.

---

## Impact and Legacy

This paper establishes the definitive framework for index theory on lattices and has immediate applications:

- **Topological Quantum Simulators:** Numerical studies of topological matter on quantum computers can now rigorously compute topological invariants without Ginsparg-Wilson overhead.
- **Lattice QCD Anomalies:** Future calculations of axial anomalies and CP-violation in lattice QCD gain rigorous topological foundation.
- **Discretized Curved Spaces:** For field theory on curved spacetime backgrounds (relevant to cosmology and black holes), lattice regularization via K-theory allows consistent treatment of topology.

---

## Connection to Phonon-Exflation Framework

**CRITICAL FOR NUMERICS.** The framework's core claims rest on the properties of the Dirac operator $D_K$ on the SU(3) fiber. To move from analytic (symbolic) computations to numerical simulations, the internal space must be discretized as a lattice.

This paper provides the exact mathematical framework needed:

1. **Lattice SU(3) Formulation:** The internal SU(3) space can be approximated as an $N \times N \times N$ cubic lattice (for some $N$) with periodic boundary conditions. The Dirac operator $D_K$ is then a Wilson Dirac operator on this lattice (possibly with a curved metric term, captured via background-field formalism).

2. **Index Computation:** The framework's claim that KO-dim = 6 (Sessions 7-8) relies on the structure of the Dirac spectrum. Computing this rigorously on a discretized SU(3) lattice requires the K-theory methods in this paper.

3. **Boundary Modes at Domain Walls:** The BCS walls (Section #37, variable-mass domain walls) create boundaries in the SU(3) fiber. The APS index formula directly gives the count of protected zero modes at such boundaries, independent of the microscopic details.

4. **Spectral Action Discretization:** For future quantum simulations of the framework, the spectral action $S_{spec}(tau) = Tr[f(D_K/M)]$ must be evaluated on a discretized $D_K$. K-theory ensures that topological contributions (the $\eta$-invariant and spectral determinant) are computed correctly on the lattice.

5. **No Ginsparg-Wilson Constraint:** The framework's SU(3) fiber is curved (its Ricci tensor is non-zero, confirmed in Session 35). Imposing Ginsparg-Wilson would be unnatural. This paper's result—that K-theory works without GW—is essential.

**Quantitative Link:** The framework identifies KO-dim = 6 as the K-theoretic dimension of the spectral triple. This paper's K-theoretic framework, applied to the discretized SU(3) internal space, should recover this dimension as the alternating sum of Betti numbers (via Atiyah-Hirzebruch spectral sequence), providing an independent numerical verification.

