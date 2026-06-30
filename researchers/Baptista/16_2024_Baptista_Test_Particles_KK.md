# Test particles in Kaluza-Klein models

**Author(s):** Joao Baptista
**Year:** 2024 (v3: December 2024)
**Journal:** Not stated in PDF
**arXiv:** 2406.09503
**Relevance:** CRITICAL

---

## Abstract

Geodesics in general relativity describe the behaviour of test particles in a gravitational field. In 5D Kaluza-Klein, geodesics reproduce the Lorentz force motion of particles in an electromagnetic field. This paper studies geodesic motion on a higher-dimensional M4 x K with background metrics encoding general 4D gauge fields and Higgs-like scalars. It shows that the classical mass and charge of a test particle become variable quantities when the geodesic traverses regions of spacetime with massive gauge fields, such as the weak force field, or with non-constant Higgs scalars. This agrees with the physical fact that interactions mediated by massive bosons can change the mass and charge of particles. The variation rates of mass and charge along a geodesic are given by natural geometric formulae. In regions where mass is preserved, there are additional constants of motion, one for every abelian or simple summand in the Killing algebra of K. The last part of the paper discusses traditional difficulties of Kaluza-Klein models, such as the low q/m ratios in the 5D model. It suggests possible ways to circumvent them. It also remarks the naturalness of a model in which elementary particles always travel at the speed of light in higher dimensions.

---

## Key Arguments and Derivations

### Sections 2-4: Geodesics on Riemannian submersions

**Setting.** A submersion metric g_P on P = M4 x K is equivalent to a triple (g_M, A, g_K) where A is a gauge one-form on M4 with values in vector fields on K. For a geodesic gamma(s) on (P, g_P) with tangent vector p(s) = sigma d gamma/ds, the rest mass is defined as:
m(s) = sigma d tau / ds

where tau is 4D proper time.

**Key result on geodesics.** For horizontal vector fields X_H and vertical vector fields V on P, the geodesic equation nabla_{dot gamma} dot gamma = 0 decomposes into horizontal and vertical components that couple through the second fundamental form S and the tensor F.

### Sections 5-6: Constants of motion

**Charge definition.** For a Killing vector field xi on (K, g_K), the charge is:
q_xi(s) = -g_P(xi, p) = -g_K(xi, p_V)

In regions with only massless gauge fields and constant g_K, q_xi is conserved. More generally, there is one constant of motion for each summand in the decomposition of the Killing algebra k = a_1 + ... + a_m.

**Higher-dimensional momentum.** The covariantly conserved momentum p(s) = sigma dot gamma decomposes into horizontal (4D) and vertical (internal) components. Internal momentum is perceived as mass in 4D.

### Section 7: Rest mass variation

**Main formula:**
c^2 d/ds m^2(s) = -(d_A g_K)_{dot gamma_M}(p_V, p_V)

where p_V is the vertical component of momentum and (d_A g_K) is the covariant derivative of the internal metric. Rest mass is conserved iff g_K is covariantly constant, i.e., in regions with only massless gauge fields.

**Physical interpretation.** Mass variation occurs when:
- The internal metric g_K changes along M4 (non-constant Higgs-like fields)
- Massive gauge fields are present (L_{e_a} g_K != 0)

This describes the physical fact that interactions with massive bosons (like the W boson) can change particle mass.

### Section 8: Charge variation

**Charge evolution:**
d/ds q_xi(s) = A^a(dot gamma_M) g_P([xi, e_a], p)

Charge is conserved when either A^a = 0 or [xi, e_a] = 0 for all relevant gauge fields. Charge can vary only when massive, charged gauge bosons are present -- matching the physics of W-boson mediated interactions.

### Section 9: A unique speed in higher dimensions

**Null geodesics.** The paper observes that if all particles travel at the speed of light in higher dimensions (null geodesics on P), then the observed 4D rest mass comes entirely from internal motion. This provides a natural explanation for why mass is related to internal degrees of freedom.

For a null geodesic: g_P(dot gamma, dot gamma) = 0, which means:
g_M(dot gamma_M, dot gamma_M) + g_K(dot gamma_V, dot gamma_V) = 0

So the "mass" is entirely g_K(dot gamma_V, dot gamma_V), the internal kinetic energy.

**Massless 4D particles cannot interact.** The projection to M4 of a null particle travelling at the speed of light on M4 is independent of gauge fields and Higgs scalars. This is incompatible with massless neutrinos that interact weakly -- providing a geometric reason to expect massive neutrinos.

### Section 11: Difficulties with geodesics on Einstein backgrounds

The paper discusses the traditional problem of low charge-to-mass ratios in 5D KK and the hierarchy problem. It suggests that non-Einstein vacuum metrics (stabilized by higher-order corrections to the action) could help resolve these difficulties.

---

## Key Results

1. Rest mass variation formula: dm^2/ds = -(d_A g_K)(p_V, p_V), showing mass changes in regions with massive gauge fields or non-constant Higgs fields.
2. Charge is conserved in regions with only massless gauge fields. It varies only when massive, charged bosons are present.
3. Constants of motion in the massless-gauge sector: one for each simple or abelian summand of the Killing algebra.
4. Null geodesics on P (all particles at the speed of light in higher dimensions) naturally explain rest mass as internal momentum.
5. Massless 4D particles cannot interact with gauge fields or Higgs scalars classically -- disfavouring massless neutrinos.
6. Mass and charge variation are geometric consequences of the fibres not being totally geodesic in P.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Submersion metric | g_P(X,Y) = g_M(X,Y) + g_K(A(X),A(Y)), g_P(X,V) = -g_K(A(X),V) | Section 1 |
| Rest mass | m(s) = sigma d tau / ds | eq (1.1) |
| Mass variation | c^2 d/ds m^2(s) = -(d_A g_K)_{dot gamma_M}(p_V, p_V) | eq (1.2) |
| Covariant derivative of g_K | (d_A g_K)_X(U,V) = (L_X g_K)(U,V) + A^a(X)(L_{e_a} g_K)(U,V) | eq (1.3) |
| Gauge boson mass | (Mass A^a_mu)^2 proportional to integral_K <L_{e_a} g_K, L_{e_a} g_K> vol / (2 integral g_K(e_a,e_a) vol) | eq (1.4) |
| Charge definition | q_xi(s) = -g_P(xi, p) = -g_K(xi, p_V) | eq (1.6) |
| Charge variation | d/ds q_xi(s) = A^a(dot gamma_M) g_P([xi, e_a], p) | Section 8 |
| Null geodesic condition | g_M(dot gamma_M, dot gamma_M) + g_K(dot gamma_V, dot gamma_V) = 0 | Section 9 |
| Killing algebra decomposition | k = a_1 + ... + a_m (abelian or simple summands) | eq (1.7) |

---

## Relevance to Phonon-Exflation

1. **Mass variation formula** (eq 1.2) provides the classical analogue of what happens during the exflation transit: as the internal metric g_K evolves (tau changes), particle masses change. The project's quasiparticle dispersion relation is the quantum version of this classical geodesic result.

2. **The identification of g_K as geometric Higgs fields** reinforces the project's paradigm: the internal metric IS the Higgs sector, and its evolution IS the physics.

3. **The null geodesic interpretation** -- all particles at the speed of light in 12D, with mass from internal motion -- connects to the project's Parker-type particle creation mechanism. During the transit, internal motion is disrupted, creating quasiparticles.

4. **Charge conservation in massless-gauge sectors** explains why colour and electromagnetic charge are conserved during the exflation transit (the SU(3) x U(1) part of the Killing algebra is preserved), while weak charges can change.

5. **The result that massless 4D particles cannot interact** with gauge fields provides a geometric argument for the project's expectation that all fermions acquire mass through the internal Dirac operator.
