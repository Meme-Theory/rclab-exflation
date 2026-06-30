# Internal symmetries in Kaluza-Klein models

**Author(s):** Joao Baptista
**Year:** 2023 (v3: March 2024)
**Journal:** Not stated in PDF
**arXiv:** 2306.01049
**Relevance:** CRITICAL

---

## Abstract

The usual approach to Kaluza-Klein considers a spacetime of the form M4 x K and identifies the isometry group of the internal vacuum metric, g^0_K, with the gauge group in four dimensions. In these notes we discuss a variant approach where part of the gauge group does not come from full isometries of g^0_K, but instead comes from weaker internal symmetries that only preserve the Einstein-Hilbert action on K. Then the weaker symmetries are spontaneously broken by the choice of vacuum metric and generate massive gauge bosons within the Kaluza-Klein framework, with no need to introduce ad hoc Higgs fields. Using the language of Riemannian submersions, the classical mass of a gauge boson is calculated in terms of the Lie derivatives of g^0_K. These massive bosons can be arbitrarily light and seem able to evade the standard no-go arguments against chiral fermionic interactions in Kaluza-Klein. As a second main theme, we also question the traditional assumption of a Kaluza-Klein vacuum represented by a product Einstein metric. This should not be true when that metric is unstable. In fact, we argue that the unravelling of the Einstein metric along certain instabilities is a desirable feature of the model, since it generates inflation and allows some metric components to change length scale. In the case of the Lie group K = SU(3), the unravelling of the bi-invariant metric along an unstable perturbation also breaks the isometry group from (SU(3) x SU(3))/Z_3 down to (SU(3) x SU(2) x U(1))/Z_6, the gauge group of the Standard Model. We briefly discuss possible ways to stabilize the internal metric after that first symmetry breaking and produce an electroweak symmetry breaking at a different mass scale.

---

## Key Arguments and Derivations

### Section 1: Introduction and overview

The central insight is that the gauge group in a KK model need not be limited to isometries of the vacuum metric. The full diffeomorphism group Diff(K) preserves the Einstein-Hilbert action, and gauge fields can be associated to non-isometric diffeomorphisms. These fields naturally have massive bosons, with mass controlled by the Lie derivative of the vacuum metric:

(Mass A^a_mu)^2 proportional to integral_K <L_{e_a} g^0_K, L_{e_a} g^0_K> vol_{g^0_K} / (2 integral_K g^0_K(e_a, e_a) vol_{g^0_K})

This has three important consequences:
1. Massive gauge bosons arise naturally when the vacuum metric breaks some symmetries
2. The bosons can be arbitrarily light (small Lie derivatives)
3. Non-Killing gauge fields can evade the Atiyah-Hirzebruch no-go theorem against chiral fermions

### Section 2: Scalar curvature of submersive metrics

**Decomposition of R_{g_P}.** For a general Riemannian submersion g_P = (g_M, A, g_K):
R_{g_P} = R_{g_M} + R_{g_K} - |F|^2 - |S_ring|^2 - |N|^2 - 2 delta_check N

where S_ring is the traceless part of the second fundamental form and N is the mean curvature. The key new formula for the norm of the traceless second fundamental form:
|S_ring|^2 = (1/4) <d_A g_K, d_A g_K> - (1/k) |d_A(vol_{g_K})|^2

where d_A g_K(X)(U,V) = (L_X g_K)(U,V) + A^a(X) (L_{e_a} g_K)(U,V) is the covariant derivative of the internal metric.

**Gauged sigma-model.** After fibre-integration, the full action decomposes as:
integral_P R_{g_P} vol_{g_P} = integral_P [R_{g_M} + R_{g_K} - (1/4)|F_A|^2 - (1/4)|d_A g_K|^2 + |d_A(vol_{g_K})|^2] vol_{g_P}

The term |d_A g_K|^2 acts as the kinetic term for the internal metric viewed as a gauged sigma-model field, with target space = space of metrics on K modulo diffeomorphisms.

### Section 3: Dynamical models

**Gauge boson mass formula:**
(Mass A^a_mu)^2 = integral_K [<L_{e_a} g^0_K, L_{e_a} g^0_K> + 4(lambda - 1)(div_{g^0_K} e_a)^2] vol_{g^0_K} / (2 integral_K g^0_K(e_a, e_a) vol_{g^0_K})

where lambda is a free parameter in the generalized action. For divergence-free vector fields, the mass is manifestly non-negative.

**Stability of product Einstein solutions.** Perturbations g^t_K = g^e_K + t(h + f g^e_K) lead to Klein-Gordon equations on M with squared-mass parameters:
- (Mass h_n)^2 = sigma_n - (2/k) R_{g^e_K} (for TT-tensor modes)
- (Mass f_n)^2 = (k-2)[(k-1) tau_n - R_{g^e_K}] / [k(k - lambda k - 1)] (for scalar modes)

The f_0 mode (constant on K) always has negative mass^2 for positive curvature Einstein metrics -- the product metric is unstable.

**Einstein frame.** Introducing g_K = a_1 e^{-b_1 phi} g_bar_K with phi measuring the volume of internal space, the action transforms to the Einstein frame. The inflaton-like field phi has a potential:
V(phi) = -(1/2 kappa_P) R_{g_bar_K} a_1 e^{-b_1 phi} Vol(K, g_bar_K) e^{-k b_1 phi/2}

### Section 3.7-3.8: Left-invariant metrics on SU(3) and symmetry breaking

**Structure of left-invariant metrics on SU(3).** Using the decomposition su(3) = u(1) + su(2) + C^2, a general left-invariant metric is parametrized by: an inner product on u(1), an inner product on su(2), an inner product on C^2, and a linear map T: C^2 -> u(2) encoding the off-diagonal terms. The TT-deformation that breaks SU(3) x SU(3) down to SU(3) x SU(2) x U(1) corresponds to the Jensen deformation, which changes the relative scaling of the u(2) and C^2 blocks.

**Unstable mode and symmetry breaking.** The bi-invariant metric on SU(3) is Einstein but unstable. The Jensen TT-deformation increases the scalar curvature. The unravelling of the bi-invariant metric along this direction breaks:
(SU(3) x SU(3)) / Z_3 --> (SU(3) x SU(2) x U(1)) / Z_6

This is exactly the gauge group of the Standard Model. The unravelling process is akin to inflation.

### Section 4: Comments on fermions

**No-go circumvention.** The Atiyah-Hirzebruch theorem only applies to gauge fields linked to isometries. Non-Killing gauge fields evade it because they do not preserve the /D-eigenspaces. A massive gauge boson linked to a non-Killing field can mix fermions of different masses AND can have chiral representations.

**Universal spinors.** The paper introduces the concept of "universal spinors" -- sections of a spinor bundle constructed from a reference metric g_hat (the average metric under the gauge group action) that can be transported to any nearby metric. This provides a framework for defining spinors consistently across a family of internal metrics.

---

## Key Results

1. The gauge boson mass formula: mass^2 proportional to ||L_e g^0_K||^2 / (2 ||e||^2), making mass generation purely geometric.
2. Product Einstein metrics on M x K with positive curvature are always unstable under rescaling of the relative sizes.
3. For K = SU(3), the bi-invariant Einstein metric is unstable under TT-deformations. The unstable Jensen direction breaks the isometry from SU(3) x SU(3) to SU(3) x SU(2) x U(1).
4. This symmetry breaking is analogous to inflation and provides a geometric origin for the Standard Model gauge group.
5. Massive gauge bosons naturally evade the Atiyah-Hirzebruch no-go theorem, opening the door to chiral fermion interactions in KK models.
6. The internal metric g_K plays the role of geometric Higgs fields in a gauged sigma-model.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Gauge boson mass | (Mass A^a_mu)^2 = integral_K <L_{e_a} g^0_K, L_{e_a} g^0_K> vol / (2 integral_K g^0_K(e_a,e_a) vol) | eq (3.7) |
| Action decomposition | integral_P R_{g_P} vol = integral_P [R_{g_M} + R_{g_K} - (1/4)\|F_A\|^2 - (1/4)\|d_A g_K\|^2 + \|d_A(vol)\|^2] vol | eq (1.5) |
| Covariant derivative of g_K | (d_A g_K)_X(U,V) = (L_X g_K)(U,V) + A^a(X)(L_{e_a} g_K)(U,V) | below eq (1.5) |
| Generalized action | E(g_P) = (1/2 kappa_P) integral_P [R_{g_P} + (1-lambda)(1-1/k)\|N\|^2 - 2 Lambda] vol | eq (3.2) |
| TT-tensor mass | (Mass h_n)^2 = sigma_n - (2/k) R_{g^e_K} | eq (3.19) |
| Scalar mode mass | (Mass f_n)^2 = (k-2)[(k-1)tau_n - R_{g^e_K}] / [k(k - lambda k - 1)] | eq (3.19) |
| Trace/traceless decomposition | \|L_V g\|^2 - (4/n)(div V)^2 = \|eta_V\|^2 >= 0 | eq (3.8) |
| Mass scaling under rescaling | (Mass)^2 at tilde{g}^0_K = omega^{-2} (Mass)^2 at g^0_K | eq (3.9) |
| Einstein relations | R_{g^e_K} = (k/m) R_{g^e_M} = 2 Lambda k / (m+k-2) | eq (3.13) |
| Jensen deformation on SU(3) | h_J = c [(1/4) g\|_{u(2)} - (1/3) g\|_{C^2}] (traceless, transverse) | Section 3.7 |
| Symmetry breaking | (SU(3) x SU(3))/Z_3 -> (SU(3) x SU(2) x U(1))/Z_6 | Section 3.8 |
| Scalar curvature of beta_tilde | R_{beta_tilde} = 3(1/lambda_2 + 4/lambda_3 - (lambda_1 + lambda_2)/(2 lambda_3^2)) | Section 3.7 |

---

## Relevance to Phonon-Exflation

This paper provides the conceptual backbone for the entire exflation paradigm:

1. **The gauge boson mass formula** (eq 3.7) is the structural foundation for the project. The mass of gauge bosons as ||L_e g_K||^2 connects directly to the project's study of how the spectrum changes as tau evolves.

2. **The Einstein instability result** -- product metrics with positive curvature are always unstable -- is the mathematical justification for the exflation mechanism. The internal space MUST evolve.

3. **The Jensen deformation breaking SU(3)xSU(3) -> SU(3)xSU(2)xU(1)** is exactly the tau-evolution studied in the project. The Jensen parameter IS the project's tau. Sessions 7-12 computed the spectral consequences of this deformation.

4. **The sigma-model interpretation** -- g_K as a field on M4 with |d_A g_K|^2 kinetic term -- frames the project's dynamical picture: the internal geometry evolves, and this evolution IS the physics.

5. **The inflation analogy** (Section 3.6) is a precursor to the project's exflation mechanism. The unravelling of the Einstein metric along the unstable direction generates expansion.

6. **The no-go circumvention** for chiral fermions using massive (non-Killing) gauge fields is the theoretical basis for why the weak force can be chiral in this framework -- a point the project relies on but does not rederive.

7. **The universal spinor construction** (Section 4.4) provides the mathematical framework for defining the project's D_K(tau) consistently as tau varies.
