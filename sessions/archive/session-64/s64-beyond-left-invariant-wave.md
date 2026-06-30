# Wave Specification: Beyond Left-Invariant Metrics on SU(3)

**Author**: Baptista-Spacetime-Analyst
**Date**: 2026-04-02
**Priority**: Lower (Wave 6-8 in S65)
**Rationale**: All CC paths within left-invariant metrics are closed or trapped. R-monotonicity (W1-A, permanent) closes Jensen. The a_0/a_2 trap (W2-A, permanent) closes all volume-preserving off-Jensen directions. The only remaining geometric escape requires qualitatively different internal metrics. This wave specifies four concrete directions and the computations needed to evaluate each.

---

## Governing Structure

The current framework operates entirely within the 36-dimensional space Met_L(SU(3)) of left-invariant Riemannian metrics on SU(3). A left-invariant metric g_K is determined by a positive-definite symmetric bilinear form on su(3), i.e., a point in the 36D cone Sym^2_+(su(3)^*). The Jensen deformation is a 1D curve in this space. The volume-preserving subspace is 35D. All S7-S64 computations live here.

Beyond this space, the universe of Riemannian metrics on SU(3) is infinite-dimensional: Riem(SU(3)) = Gamma(Sym^2_+(T^*SU(3))). Left-invariant metrics form a finite-dimensional submanifold. The four directions below explore controlled departures from this submanifold, ordered by increasing mathematical difficulty.

---

## Direction A: Inhomogeneous Metrics (Position-Dependent Fiber Geometry)

### What This Means

In the full KK framework (Paper 15, eq. 1.5), the internal metric g_K is a field on M4, not a constant. The covariant derivative d_A g_K measures how g_K varies across the base. The term |d_A g_K|^2 in the fibre-integrated action is the kinetic energy of this variation. Setting g_K = const (homogeneous fiber) kills this term. Relaxing it means the fiber at base point x looks different from the fiber at base point y.

The spectral action coefficients a_0, a_2 then become LOCAL quantities: a_k(x) depends on g_K(x). The CC ratio a_0(x)/a_2(x) can vary across spacetime. Even if the trap holds pointwise, spatial averaging could produce a different effective ratio.

### The Computation

**INHOM-PERTURBATION-65**: Compute the linearized response of a_0 and a_2 to a slowly-varying perturbation g_K(x) = g_K^fold + epsilon * h(x), where h(x) is a TT-tensor eigenmode of the 4D Laplacian with eigenvalue k^2.

Specifically: expand a_2[g_K(x)] to second order in epsilon, integrate over a 4D ball of radius L, and extract the spatially-averaged ratio <a_0>/<a_2> as a function of (epsilon, k*L).

**Inputs**: Fold metric g_K^fold from s64_hessian_descent.npz. The 35 volume-preserving tangent directions and their R-Hessian eigenvalues from W2-A. The Seeley-DeWitt integrand formula from Paper 13 eq. 2.40: a_2 = (4pi)^{-4} * (20R_K/3) * Vol_K.

**Output**: The function delta(a_0/a_2)(epsilon, kL) for the leading perturbation modes. Whether spatial averaging improves, worsens, or leaves invariant the CC ratio.

**Pre-registered gate**: INHOM-CC-65. PASS: there exists a perturbation mode (h, k) for which the spatially-averaged <a_0/a_2> < a_0/a_2|_fold. FAIL: <a_0/a_2> >= a_0/a_2|_fold for all modes. INFO: <a_0/a_2> depends on k in a non-trivial way that warrants further study.

**Mathematical prerequisites**: The Seeley-DeWitt coefficients for a metric that varies over the base require the FULL heat kernel on M4 x K, not the factored form. The standard factorization K(t) = K_M(t) * K_K(t) holds only when the submersion has totally geodesic fibers and zero A-tensor. For inhomogeneous g_K(x), the O'Neill A-tensor is nonzero and couples base and fiber. Computing a_2 for the coupled system requires the O'Neill curvature decomposition (Paper 15, Section 2). The leading correction is order epsilon^2 and involves the integral of |A|^2 over K. This is NEW infrastructure -- the O'Neill A-tensor for a perturbation of the product metric has not been computed in the project.

**Baptista corpus**: Paper 15, Section 2 gives the full R_P decomposition including |F_A|^2, |S|^2, |N|^2 terms. The gauged sigma-model interpretation (Paper 15, eq. 1.5) frames g_K(x) as a sigma-model field with target Met(K)/Diff(K). Paper 36 (Cheeger deformations on fiber bundles, Theorem 3.1) gives the sectional curvature decomposition for deformed fiber bundles with the non-negative remainder z_t >= 0.

**Difficulty**: MODERATE. The linearized expansion is standard perturbation theory. The new ingredient is computing the O'Neill A-tensor contribution to a_2 at the fold.

**Agent**: gen-physicist or connes-ncg-theorist (requires spectral action + O'Neill formalism).

---

## Direction B: Less-Symmetric Metrics (U(1) x U(1) Invariant)

### What This Means

Left-invariant metrics on SU(3) are invariant under the full left SU(3)_L action. This is an 8-dimensional symmetry group acting on an 8-dimensional manifold. Reducing the symmetry to the maximal torus T^2 = U(1) x U(1) of SU(3)_L enlarges the moduli space dramatically.

The flag manifold SU(3)/T^2 is 6-dimensional. A T^2-invariant metric on SU(3) is parametrized by a metric on the T^2-orbits (which is T^2-invariant, hence given by a 2x2 positive-definite matrix at each point of SU(3)/T^2) plus a metric on the horizontal distribution. The moduli space of T^2-invariant metrics is infinite-dimensional (functions on the 6D base SU(3)/T^2), but the restriction to T^2-invariant metrics that are also homogeneous under SU(3)/T^2 gives a finite-dimensional space.

Paper 35 (Grama-Martins, Ricci flow on SU(3)/T) studies exactly this space. The tangent space of SU(3)/T decomposes into three irreducible Ad(T)-modules m_12, m_13, m_23, and an invariant metric is parametrized by three positive constants (lambda_12, lambda_13, lambda_23). This is a 3D moduli space, a strict subspace of the 36D left-invariant space -- but the FLAG manifold geometry is different from the GROUP manifold geometry. The distinction: on the flag manifold, the structure group is T^2, not SU(3). The moduli space of T^2-invariant metrics on the GROUP SU(3) is larger than either.

### The Computation

**TORUS-INVARIANT-65**: Compute a_0, a_2, a_4, and the ratio a_0/a_2 for the 3-parameter family of T^2-invariant metrics on SU(3) parametrized by (lambda_12, lambda_13, lambda_23) from Paper 35. These are NOT left-invariant in general -- they are left-T^2-invariant, which is a weaker condition.

Step 1: Parametrize the metric. On su(3) = t + m_12 + m_13 + m_23, the T^2-invariant metric is g = lambda_T * g|_t + lambda_12 * g|_{m_12} + lambda_13 * g|_{m_13} + lambda_23 * g|_{m_23}, where lambda_T controls the torus fiber size independently. This gives a 4D family (adding lambda_T to the 3 coset parameters).

Step 2: Compute the scalar curvature R(lambda_T, lambda_12, lambda_13, lambda_23) using the Koszul formula. The Ricci components are given in Paper 35 eq. (3).

Step 3: Compute the volume form Vol(lambda) and the Seeley-DeWitt integrand (20R/3) * Vol.

Step 4: Evaluate a_0/a_2 over a grid in the 4D parameter space. Identify whether any point has a_0/a_2 < a_0/a_2|_fold = 2.320.

**Inputs**: Structure constants of su(3) (from canonical_constants.py or s44 data). Ricci tensor formulas from Paper 35 eq. (3).

**Output**: Contour plots of a_0/a_2 in the (lambda_12, lambda_13, lambda_23, lambda_T) space. Identification of the minimum of a_0/a_2 and comparison to the fold value 2.320.

**Pre-registered gate**: TORUS-CC-65. PASS: min(a_0/a_2) over the 4D T^2-invariant family is < a_0/a_2|_fold * 0.9 (10% improvement). FAIL: min(a_0/a_2) >= a_0/a_2|_fold everywhere. INFO: marginal improvement (< 10%).

**CRITICAL CAVEAT**: The T^2-invariant metrics that are ALSO SU(3)_L-invariant form the 1D Jensen family (restricted to the diagonal). The question is whether moving off the left-invariant locus within T^2-invariant metrics opens new CC directions. If the 4-parameter family has a_0/a_2 bounded below by the same trap, the obstruction is more general than left-invariance.

**Mathematical prerequisites**: The Ricci tensor formulas in Paper 35 are for SU(3)/T (the flag manifold), not for SU(3) itself. The translation to T^2-invariant metrics on SU(3) requires lifting the flag manifold metric to the group via the principal T^2-bundle T^2 -> SU(3) -> SU(3)/T^2. The Kaluza-Klein decomposition of R_{SU(3)} = R_{SU(3)/T} + R_T - |F|^2 (where F is the curvature of the T^2-connection) provides the bridge. This is standard submersion geometry.

**Baptista corpus**: Paper 35 gives the Ricci flow ODE for the 3 parameters. Paper 13 Section 2.3 gives the general left-invariant metric parametrization. Paper 30 (Schwahn) gives the Lichnerowicz Casimir formula for TT-tensors, which controls the stability of Einstein metrics in this family. Paper 46 (Derdzinski-Gal) proves that the Killing-form metric on SU(3) has curvature operator eigenvalue 1 in Spec(Omega) -- the ONLY simple group where this happens -- meaning non-isolated Einstein deformations may exist even within left-invariant metrics.

**Difficulty**: MODERATE. The geometry of SU(3)/T^2 is classical (flag manifold). The new computation is evaluating the Seeley-DeWitt coefficients on the lifted metrics, not just the scalar curvature.

**Agent**: baptista-spacetime-analyst (submersion formalism) or gen-physicist (numerical evaluation).

---

## Direction C: Topological Transitions (U(1) Collapse)

### What This Means

The anti-Jensen flow (W2-A) collapses the U(1) fiber: c_u1 -> 0 while SU(2) expands. At c_u1 = 0 exactly, the metric on SU(3) degenerates. The Riemannian manifold (SU(3), g) becomes a singular space. The topology may change.

The key question from the CC perspective: a_0 = (4pi)^{-4} * N_fiber * Vol_K is proportional to the number of D_K eigenvalues times the volume. Under volume-preserving deformations, a_0 is constant (the trap). But a topology change is NOT a continuous deformation. If the limiting space at c_u1 = 0 has FEWER eigenvalues (smaller N_fiber), then a_0 jumps downward. This is the only identified mechanism for changing a_0 discretely.

The geometric picture: as c_u1 -> 0, the U(1) fiber of the submersion SU(3) -> SU(3)/U(1) = CP^2 shrinks to zero size. In the limit, SU(3) collapses to CP^2 (a 4-dimensional space, not 8-dimensional). The D_K spectrum on CP^2 is much smaller than on SU(3).

This is analogous to the conifold transition in string theory (Kaku investigation, Section III.D), where a 3-cycle shrinks to zero and a 2-cycle inflates.

### The Computation

**U1-COLLAPSE-65**: Compute the D_K eigenvalue spectrum, a_0, a_2, and a_0/a_2 as c_u1 -> 0 along the anti-Jensen flow.

Step 1: Parametrize the metric as g(epsilon) = diag(a_su2, a_su2, a_su2, b_c2, b_c2, b_c2, b_c2, epsilon) in the su(2) + C^2 + u(1) basis, with volume constraint a_su2^3 * b_c2^4 * epsilon = const.

Step 2: For each epsilon in {1.0, 0.5, 0.1, 0.01, 0.001, 1e-6}, compute the full D_K eigenvalue spectrum (992 eigenvalues at L_max = 3, or extend to L_max = 4 if feasible).

Step 3: Track N_eff(epsilon) = number of eigenvalues below Lambda, a_0(epsilon), a_2(epsilon), and a_0/a_2(epsilon).

Step 4: Identify whether a_0/a_2 has a minimum at some epsilon > 0, or whether it decreases monotonically as epsilon -> 0.

Step 5: Compute the LIMITING spectrum on CP^2 (4-dimensional) for comparison. The Dirac spectrum on CP^2 is known analytically (see Cahen-Gutt-Trautman classification). Compare the limiting a_0/a_2 to the SU(3) value.

**Inputs**: D_K computation infrastructure from s44_dos_tau.py (corrected for the (1,2) missing irrep per S61 PW-AUDIT). Structure constants of su(3). The anti-Jensen trajectory from s64_hessian_descent.npz.

**Output**: Plot of a_0/a_2 vs. epsilon (log scale). Identification of whether the collapse improves the CC ratio. Eigenvalue flow diagram showing mode coalescence or splitting as epsilon -> 0.

**Pre-registered gate**: CONIFOLD-CC-65. PASS: a_0/a_2 at epsilon = 0.001 is < 50% of a_0/a_2|_fold (> 2x improvement). FAIL: a_0/a_2 increases or stays within 10% of fold value at all epsilon. INFO: a_0/a_2 decreases but by < 50%.

**Mathematical prerequisites**: Computing D_K on a degenerate metric requires regularization. As epsilon -> 0, some eigenvalues diverge (modes with U(1) momentum) while others converge (modes independent of U(1)). The surviving modes at epsilon = 0 are those with zero U(1) charge. This is a selection rule from representation theory: irreps V_{(p,q)} of SU(3) decompose under SU(2) x U(1), and only the U(1)-neutral components survive the collapse.

Counting: in each V_{(p,q)}, the U(1)-neutral states have hypercharge Y = 0. The number of such states depends on (p,q). For the adjoint (1,1): 2 states (the su(2) triplet has Y=0 component, and the U(1) generator has Y=0). This counting determines the limiting N_fiber and hence a_0.

NEW INFRASTRUCTURE NEEDED: The current D_K code (s44_dos_tau.py) parametrizes the metric by the single Jensen parameter tau. This computation requires the 3-parameter metric (a_su2, b_c2, epsilon). The structure constants are the same; only the metric tensor g_ab changes. The Dirac operator formula D_K = gamma^a e_a^i (partial_i + omega_i) requires the vielbein e_a^i = sqrt(g^{aa}) delta_a^i (diagonal metric) and the spin connection omega_i from the Koszul formula. The generalization from 1-parameter to 3-parameter is straightforward but requires rewriting the metric-dependent parts of the code.

**Baptista corpus**: Paper 13, Section 2.3 gives the general left-invariant metric including the independent scales for u(1), su(2), C^2. The volume form formula (Paper 13, below eq. 2.40) gives Vol = f(a_su2, b_c2, epsilon). Paper 15, Section 3.6-3.8 discusses the instability of the Einstein metric and the Jensen deformation as the symmetry-breaking direction. The ANTI-Jensen direction is the reverse: it breaks toward the U(1) collapse.

Paper 12 (Vortices as degenerate metrics) establishes Baptista's expertise with degenerate Riemannian metrics. The key insight: vortex moduli spaces are preserved under metric degeneration (Paper 10, Biswas-Baptista, Proposition 2.1). If an analogous stability holds for the Dirac spectrum, the limiting spectrum at epsilon = 0 could be well-defined despite the degeneration.

**Difficulty**: HARD. The D_K computation for 3-parameter metrics requires new code. The degenerate limit epsilon -> 0 requires regularization and careful eigenvalue tracking. The comparison to CP^2 requires independent spectral data.

**Agent**: gen-physicist (D_K numerics) with baptista-spacetime-analyst verification.

---

## Direction D: Orbifold Limits (Discrete Quotients)

### What This Means

Instead of degenerating the metric continuously, one can quotient SU(3) by a discrete subgroup Gamma to obtain the orbifold SU(3)/Gamma. The Dirac operator on SU(3)/Gamma inherits from D_K on SU(3) by restricting to Gamma-invariant sections. This REDUCES the number of eigenvalues (hence a_0) while potentially preserving a_2 (curvature is a local quantity, unchanged by quotienting).

The relevant discrete subgroups of SU(3) are:
- Cyclic Z_n embedded in U(1) center: SU(3)/Z_3 = PSU(3) (the projective special unitary group)
- Finite subgroups of the maximal torus T^2: e.g., Z_3 x Z_3
- Exceptional finite subgroups: the Hessian group Hess(216), the trihexaflexagon group of order 648

The simplest case is SU(3)/Z_3. The center Z_3 = {I, omega*I, omega^2*I} (omega = e^{2pi*i/3}) acts freely, so SU(3)/Z_3 is a smooth manifold (not a singular orbifold). The D_K eigenvalues on SU(3)/Z_3 are those of D_K on SU(3) that are Z_3-invariant. Since Z_3 acts by multiplication by omega^k on V_{(p,q)}, an irrep is Z_3-invariant iff p - q = 0 mod 3.

### The Computation

**ORBIFOLD-CC-65**: Compute a_0, a_2, and a_0/a_2 on SU(3)/Z_3 and SU(3)/(Z_3 x Z_3) by restricting the D_K spectrum to invariant sectors.

Step 1: For SU(3)/Z_3, select the PW sectors V_{(p,q)} with p - q = 0 mod 3. These are: (0,0), (1,1), (3,0), (0,3), (2,2), (4,1), (1,4), (3,3), ... From the existing L_max = 6 data, filter to Z_3-invariant irreps and recompute a_0, a_2.

Step 2: For SU(3)/(Z_3 x Z_3), the invariance condition is more restrictive. The second Z_3 acts on T^2 and selects p = 0 mod 3 AND q = 0 mod 3. Surviving irreps: (0,0), (3,0), (0,3), (3,3), ... This dramatically reduces the spectrum.

Step 3: Compute a_0/a_2 for both quotients. Since Vol(SU(3)/Z_n) = Vol(SU(3))/n and R is unchanged, a_2 scales as 1/n. But a_0 = (4pi)^{-4} * N_fiber * Vol also scales by 1/n times the fraction of surviving modes. The ratio a_0/a_2 scales as (N_surviving/N_total) / 1, i.e., the FRACTION of modes that survive.

Step 4: Determine whether the surviving fraction favors a_0 or a_2. If high-eigenvalue modes (which contribute more to a_2 per mode) survive preferentially, a_0/a_2 decreases. If low-eigenvalue modes survive, a_0/a_2 could increase.

**Inputs**: Full D_K spectrum at L_max = 6 from s63_kk_threshold.npz. Peter-Weyl sector labels (p,q) for each eigenvalue. Z_3 triality: p - q mod 3 for each sector.

**Output**: Table of (a_0, a_2, a_0/a_2) for SU(3), SU(3)/Z_3, and SU(3)/(Z_3 x Z_3). Assessment of whether discrete quotienting improves the CC ratio.

**Pre-registered gate**: ORBIFOLD-CC-65. PASS: a_0/a_2 on SU(3)/Z_3 is < a_0/a_2|_{SU(3)} * 0.9 (10% improvement). FAIL: a_0/a_2 increases or stays within 10%. INFO: marginal change that depends sensitively on the cutoff.

**Mathematical prerequisites**: MINIMAL. The Z_3 selection rule on (p,q) irreps is elementary representation theory. The only subtlety is the spin structure: SU(3)/Z_3 may not admit the same spin structure as SU(3). Since SU(3) is simply connected (pi_1 = 0), it has a unique spin structure. SU(3)/Z_3 has pi_1 = Z_3, and spin structures are classified by H^1(SU(3)/Z_3, Z_2) = 0 (since Z_3 has no Z_2 quotient). So SU(3)/Z_3 admits a unique spin structure inherited from SU(3), and the Dirac operator is well-defined.

**Baptista corpus**: Paper 15, Section 3.8 discusses the isometry breaking (SU(3) x SU(3))/Z_3 -> (SU(3) x SU(2) x U(1))/Z_6. The Z_3 quotient is already present in the gauge group structure. Paper 18, Section 6 discusses how fermion generations arise from splitting degenerate D_K eigenspaces under symmetry breaking, which is directly relevant to how the spectrum changes under quotienting. Paper 10 (singular vortices with Biswas) shows orbifold vortex moduli are preserved -- a structural parallel to eigenvalue preservation under quotienting.

**Difficulty**: TRIVIAL to MODERATE. Step 1-3 require only filtering existing spectral data. The spin structure analysis (Step 4 subtlety) is standard algebraic topology. No new numerical infrastructure is needed.

**Agent**: gen-physicist or any agent with access to the D_K spectral data.

---

## Dependencies

```
D (Orbifold)  ----independent----  B (Torus-invariant)
     |                                    |
     v                                    v
C (U(1) collapse)  <--- shares infrastructure --->  A (Inhomogeneous)
```

- **D is independent of all others** and should run FIRST (trivial difficulty, uses existing data).
- **B is independent of D** and can run in parallel.
- **C depends on new 3-parameter D_K code** that also benefits A (both need metrics beyond 1-parameter Jensen).
- **A requires O'Neill A-tensor computation** that is independent of B, C, D.
- **Recommended execution order**: D first (immediate, zero infrastructure), then B (moderate, flag manifold geometry), then C (hard, new code + degenerate limit), then A (moderate but needs new formalism).

---

## Risk Assessment

| Direction | P(actionable result) | Worst case | Best case |
|:----------|:---------------------|:-----------|:----------|
| A: Inhomogeneous | 25% | O'Neill coupling vanishes at linear order; a_0/a_2 invariant under slow variation. Result: the trap is local, not just global. | Spatial averaging of a_0/a_2 over a domain wall profile reduces the effective ratio by O(1). CC relaxation through geometric inhomogeneity. |
| B: Torus-invariant | 30% | The 4D T^2-family has a_0/a_2 bounded below by the same value as the Jensen curve. The trap extends beyond left-invariance. | An entirely new valley in the (lambda_12, lambda_13, lambda_23, lambda_T) space with a_0/a_2 << 2.3. The CC problem is an artifact of the Jensen parametrization. |
| C: U(1) collapse | 40% | a_0/a_2 diverges as epsilon -> 0 (both a_0 and a_2 blow up, ratio worsens). The topology change is pathological. | a_0 drops by orders of magnitude at the transition (mode count collapses), while a_2 is protected by curvature. The CC ratio jumps from ~2.3 to ~0.01 at the conifold point. This would be a major structural breakthrough. |
| D: Orbifold | 35% | Z_3 selection removes modes uniformly, a_0/a_2 unchanged. The quotient is CC-neutral. | High-eigenvalue modes preferentially survive the Z_3 filter, reducing a_0/a_2. A discrete mechanism for CC relaxation with no continuous obstruction (the trap only constrains continuous deformations). |

---

## Connection to Existing Results

### Anti-Jensen U(1) Collapse (W2-A) -> Direction C

The W2-A result directly motivates Direction C. The anti-Jensen flow drives c_u1 -> 0 with a_su2 expanding and b_c2 expanding. This is the DYNAMICAL trajectory that the gradient flow follows (along the steepest R-descent direction). If the spectral action dynamics drives the internal geometry toward c_u1 = 0, then the conifold-like transition in Direction C is not speculative -- it is the ENDPOINT of the physical evolution. The 27 descent directions of R all have negative U(1) component (W2-A, gradient decomposition), confirming that U(1) collapse is generic, not fine-tuned.

### Breathing Mode (Non-Volume-Preserving) -> Direction A

Direction A is the SPATIAL version of the breathing mode question. The breathing mode (overall volume change at a single point) modifies a_0 through Vol_K. An inhomogeneous metric g_K(x) has a position-dependent volume Vol_K(x). Even if the TOTAL integrated volume is fixed, the local a_0(x)/a_2(x) varies. The spatially-averaged ratio can differ from the pointwise ratio. This is Jensen's inequality applied to the CC ratio: <a_0/a_2> != <a_0>/<a_2> when a_0 and a_2 covary.

### Proven Theorem Survival

| Theorem | A: Inhom | B: T^2 | C: Collapse | D: Orbifold |
|:--------|:---------|:-------|:------------|:------------|
| R-monotonicity (Jensen) | Irrelevant (off-Jensen) | Irrelevant (off-Jensen) | Irrelevant (off-Jensen) | Irrelevant (off-Jensen) |
| a_0/a_2 trap (vol-pres) | MODIFIED: spatial averaging adds new structure | APPLIES within vol-pres subspace; may be evaded by lambda_T | BROKEN at epsilon = 0 (topology change) | BROKEN (discrete quotienting is not a continuous deformation) |
| H2 (r = 0.033) | Survives if perturbation is traceless | Survives if 4-param family is volume-preserving | Uncertain (degenerate metric may alter DeWitt decomposition) | Survives (quotienting preserves volume-preservation) |
| Block-diagonality of D_K | Survives (local property) | Survives (T^2 subgroup of SU(3)_L) | UNCERTAIN at epsilon = 0 (block structure may merge) | Survives (Z_3 commutes with block structure) |
| Fold = saddle (8+, 27-) | Not directly applicable (infinite-dim perturbation) | Restricted to 4D subspace of 36D | Modified (different Hessian at general (a,b,epsilon)) | Modified (restricted to Z_3-invariant subspace) |

The critical observation: Directions C and D are the only ones that can BREAK the a_0/a_2 trap, because they involve discontinuous changes (topology change and discrete quotienting respectively) rather than continuous deformations. The trap is a statement about continuous paths in the moduli space. It says nothing about discrete jumps.

---

## Summary Table

| # | Computation ID | Agent | Difficulty | Gate | Priority within wave |
|:--|:--------------|:------|:-----------|:-----|:--------------------|
| D | ORBIFOLD-CC-65 | gen-physicist | TRIVIAL | a_0/a_2 < 0.9 * fold | 1 (first) |
| B | TORUS-CC-65 | gen-physicist + baptista | MODERATE | a_0/a_2 < 0.9 * fold | 2 |
| C | CONIFOLD-CC-65 | gen-physicist + baptista | HARD | a_0/a_2 < 0.5 * fold | 3 |
| A | INHOM-CC-65 | connes + baptista | MODERATE | <a_0/a_2> < fold | 4 (last) |
