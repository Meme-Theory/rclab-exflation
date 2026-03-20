# Heat Kernels on Covering Spaces and Topological Invariants

**Author(s):** John Lott

**Year:** 1992

**Journal:** Journal of Functional Analysis, Vol. 110, pp. 419-443

---

## Abstract

Lott develops a framework for computing heat kernel asymptotics on covering spaces and relates them to topological invariants. The key result is that the heat kernel trace on an infinite covering space (or a fundamental domain with periodic boundary conditions) encodes information about the fundamental group and the cover structure. This work is essential for understanding spectral geometry on spaces with quotient structures, which is relevant to compact Lie groups viewed as quotients of universal covers.

---

## Historical Context

By the early 1990s, heat kernel asymptotics were well-understood on compact manifolds (via Gilkey and others), but the behavior on non-compact covering spaces or fundamental domains was less clear.

Lott's 1992 paper extended the heat kernel machinery to covers, showing that:

1. The heat kernel trace on a covering space can be decomposed using the automorphism group (deck transformations).
2. Each irreducible representation of the fundamental group contributes to the heat kernel asymptotic expansion.
3. The "twisted" heat kernel (twisted by a representation) encodes topological information.

This is particularly relevant to the phonon-exflation framework, where SU(3) is a compact Lie group that can be viewed as a quotient of its universal cover (which is simply connected and typically non-compact or has fundamental domain structure).

---

## Key Arguments and Derivations

### Covering Spaces and Deck Transformations

For a covering map $\pi: \tilde{M} \to M$ (with $\tilde{M}$ the covering space and $M$ the base), the fundamental group $\pi_1(M)$ acts on $\tilde{M}$ as deck transformations (automorphisms that preserve the cover structure).

For example:
- SU(3) is a quotient of Spin(6) (its universal cover) by a finite group (the center).
- A compact Lie group $G$ can be viewed as $\tilde{G} / \Gamma$, where $\tilde{G}$ is the universal cover (simply connected) and $\Gamma$ is the center.

The Laplacian $\tilde{\Delta}$ on $\tilde{M}$ is invariant under the action of $\pi_1(M)$:

$$\gamma^* \tilde{\Delta} = \tilde{\Delta} \gamma^*$$

for any deck transformation $\gamma$.

### Trace Formula on Covering Spaces

The heat kernel trace on the covering space includes contributions from the fixed points of deck transformations:

$$\text{Tr}(e^{-t\tilde{\Delta}}) = \sum_{\gamma \in \pi_1(M)} \int_{\tilde{M}^\gamma} K_t(x, \gamma \cdot x) dV_x$$

where $\tilde{M}^\gamma$ is the fixed set of $\gamma$.

For a generic (non-identity) deck transformation, $\tilde{M}^\gamma$ is typically empty (the transformation has no fixed points). Only the identity contributes a full-manifold integral.

However, when the cover is finite (as in SU(3) as a quotient of Spin(6)), each non-identity transformation $\gamma$ still contributes a smaller integral.

### Twisted Spectral Sum and Representation Theory

One can define a "twisted" trace by inserting a character $\chi_\rho$ (a representation of $\pi_1(M)$) into the trace formula:

$$\text{Tr}_\rho(e^{-t\tilde{\Delta}}) = \sum_{\gamma \in \pi_1(M)} \chi_\rho(\gamma) \int_{\tilde{M}^\gamma} K_t(x, \gamma \cdot x) dV_x$$

When averaged over all irreducible representations (characters), this recovers the standard heat kernel on the base $M$:

$$\text{Tr}(e^{-t\Delta_M}) = \frac{1}{|\pi_1(M)|} \sum_\rho d_\rho \, \text{Tr}_\rho(e^{-t\tilde{\Delta}})$$

where $d_\rho$ is the dimension of representation $\rho$.

This relationship directly mirrors the Peter-Weyl decomposition for compact Lie groups!

### Heat Kernel Asymptotics on the Cover

For the covering space $\tilde{M}$, the heat kernel trace expands as:

$$\text{Tr}(e^{-t\tilde{\Delta}}) = (4\pi t)^{-n/2} \left[\tilde{a}_0 + \tilde{a}_2 t + \ldots \right]$$

where the coefficients $\tilde{a}_k$ are the Seeley-DeWitt coefficients for the (typically) non-compact cover.

However, if we restrict to a fundamental domain with suitable boundary conditions (e.g., periodic boundary conditions matching the cover structure), the computation is similar to the compact case.

For SU(3) viewed as Spin(6)/center, the universal cover Spin(6) is a simply-connected Lie group, and the heat kernel on Spin(6) is readily computed using Peter-Weyl decomposition.

### Application: SU(3) as Quotient of Spin(6)

SU(3) has center $\mathbb{Z}_3$ (three elements), so:

$$SU(3) = Spin(6) / \mathbb{Z}_3$$

The fundamental group is $\pi_1(SU(3)) = \mathbb{Z}_3$.

The deck transformations are multiplication by the three elements of the center: $\{e, e^{2\pi i/3}, e^{4\pi i/3}\}$ (as central elements of the universal cover).

The heat kernel trace on SU(3) is:

$$\text{Tr}(e^{-t\Delta_{SU(3)}}) = \frac{1}{3} \sum_{k=0}^{2} \text{Tr}(e^{-t\tilde{\Delta}_{Spin(6)}} \cdot e^{2\pi i k / 3})$$

where the sum is over the three characters of $\mathbb{Z}_3$.

Each term is a "twisted" heat kernel on Spin(6), which can be computed using character theory.

### Relation to Analytic Torsion

Lott showed that the heat kernel on covering spaces directly relates to the analytic torsion (as developed by Mueller):

$$\log \tau(M) = \int_0^\infty \frac{dt}{t} \left[\text{Tr}(e^{-t\Delta_M}) - \text{(zeta function regularization)}\right]$$

For a finite cover, the torsion of $M$ is related to the torsion of $\tilde{M}$ by a formula involving the size of the cover:

$$\tau(M)^{|\pi_1(M)|} = \tau(\tilde{M}) / \text{(Reidemeister correction)}$$

### Return Probability and Fundamental Domain

For a random walk on the spectrum of the Laplacian, the return probability (starting and ending at the same point) is related to the heat kernel on the fundamental domain:

$$p_t(x, x) = \int_{\text{fund. domain}} K_t(x, y) \, dV_y$$

When summed over the entire covering space (with periodic boundary conditions), this becomes:

$$\text{Tr}(e^{-t\tilde{\Delta}}) = \int_{\tilde{M}} K_t(x, x) \, dV_x$$

Lott's analysis shows how to extract the fundamental domain contribution from the full cover trace.

### Application to Spin Structures

For a manifold with spin structure, the fundamental domain analysis applies to both the gravitational Laplacian (on scalars) and the Dirac operator (on spinors).

For SU(3) as a spin manifold (with a spin structure inherited from Spin(6)), the Dirac operator on Spin(6) projects down to the Dirac operator on SU(3) via the quotient map.

Lott's formulas show how to relate the Dirac spectrum on SU(3) to the Dirac spectrum on Spin(6).

---

## Key Results

1. **Trace formula on covers**: Trace of heat kernel on base = averaged trace over representations of $\pi_1(M)$ on cover.

2. **Twisted heat kernels**: Inserting character gives "twisted" trace; averaging recovers base trace.

3. **Peter-Weyl decomposition as heat kernel formula**: For Lie groups, the Peter-Weyl decomposition emerges as the fundamental domain version of Lott's covering space formula.

4. **Analytic torsion on covers**: Relationship between torsion on base and universal cover.

5. **Dirac spectrum on quotient Lie groups**: Spectrum of $G/\Gamma$ relates to spectrum of simply-connected cover $\tilde{G}$ via representation theory.

6. **Heat kernel asymptotics inherit from cover**: Seeley-DeWitt coefficients on base are derived from those on universal cover.

---

## Impact and Legacy

Lott's 1992 paper bridged heat kernel theory and the fundamental group, enabling:

- **Spectral geometry of quotient manifolds**: Understanding how quotient structures affect the spectrum.
- **Lie group spectral theory**: Relating Lie group spectra to universal covers.
- **Fundamental group invariants**: Computing topological invariants from spectral data.
- **String theory on orbifolds**: Orbifold heat kernels and twisted sectors.

Citations: ~400+.

---

## Connection to Phonon-Exflation Framework

**Relevance: HIGH for understanding SU(3) spectrum and internal quotients**

The SU(3) manifold is a quotient of Spin(6) (or SU(2) x SU(2)/Sp(1), depending on the covering structure). Lott's framework provides a way to relate the Dirac spectrum on SU(3) to that of the universal cover.

### Direct Applications:

1. **SU(3) as quotient of Spin(6)**: The phonon-exflation framework computes the Dirac spectrum on SU(3) directly (Sessions 7-12, 20a, 24a). Lott's methods allow one to compute this from the spectrum on Spin(6), providing a consistency check.

   The heat kernel trace on SU(3) is:

$$\text{Tr}(e^{-t\Delta_{SU(3)}}) = \frac{1}{3} \sum_{k=0}^{2} (\text{twisted heat kernel on Spin(6)})$$

   Sessions 31 could verify this relationship explicitly.

2. **Character sum decomposition**: The Dirac spectrum on SU(3) can be decomposed into contributions from the three irreducible representations of $\mathbb{Z}_3$ (the center). Lott's formulas show how to extract the spectral components corresponding to each character.

3. **Fundamental domain analysis**: Rather than computing the Dirac operator on the full SU(3) manifold, one could compute it on a fundamental domain of the universal cover, with periodic boundary conditions. This is sometimes more tractable numerically.

   Sessions 7-12 effectively did this (computing eigenvalues by solving the Dirac equation on SU(3)), but Lott's framework makes the connection explicit.

4. **Covering space topology**: If the phonon-exflation framework evolves the metric on SU(3) (via the Jensen parameter $\tau$), the topology of SU(3) is fixed (it always remains SU(3), not some other group). Lott's analysis ensures that the center $\mathbb{Z}_3$ structure is preserved, guaranteeing consistency.

5. **Relation to analytic torsion**: Lott connects heat kernels on covers to analytic torsion. For SU(3), this means:

$$\tau(SU(3)) = \text{(computed from heat kernel on Spin(6) with center quotient)}$$

   This provides another check on the spectral computation: the torsion should be consistent with the heat kernel data.

6. **Twisted sectors and representation theory**: For string theory or quantum field theory on the quotient SU(3), one can include "twisted sectors" corresponding to non-trivial characters of $\mathbb{Z}_3$. Lott's twisted heat kernels directly apply to these sectors.

7. **Return probability decomposition**: The return probability (how quickly a random walk returns to its starting point) on SU(3) can be decomposed by irreducible representation of the center. Lott's fundamental domain analysis gives:

$$p_t(x,x) = \sum_{k=0}^{2} c_k p_t^{(k)}(x,x)$$

   where each $p_t^{(k)}$ is the twisted return probability. This is relevant for BA-31-1 (return probability diagnostic).

8. **Spectral dimension on quotients**: The spectral dimension extracted from the heat kernel behavior should be $\dim(SU(3)) = 8$ whether computed on SU(3) directly or via the quotient formula. Lott's analysis guarantees this consistency.

**Session 31 relevance**: BA-31-1 (spectral dimension and return probability) uses the covering space formula to decompose the return probability by representation. BA-31-3 (orientation test and torsion) uses Lott's analytic torsion on quotients. BA-31-4 (chirality test) uses twisted heat kernels.

