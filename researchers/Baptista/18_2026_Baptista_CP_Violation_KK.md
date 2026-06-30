# The geometry of CP violation in Kaluza-Klein models

**Author(s):** Joao Baptista
**Year:** 2026
**Journal:** Not stated in PDF
**arXiv:** 2601.08902
**Relevance:** CRITICAL

---

## Abstract

We investigate the free, massless Dirac equation /D Psi = 0 on a higher-dimensional manifold M4 x K equipped with a submersion metric. These background metrics generalize the Kaluza ansatz. They encode 4D massive gauge fields and Higgs-like scalars, alongside the usual 4D metric and massless gauge fields. We show that the dimensional reduction of the Dirac equation on these backgrounds naturally violates CP symmetry in four dimensions. This provides a new geometric path to constructing models with intrinsic CP violation. In this framework, massive gauge fields can break CP for three different reasons: i) a misalignment between the mass eigenspinors and the spinors in the representation basis; ii) a new non-minimal term coupling 4D fermions to massive gauge fields; iii) the presence of a non-abelian Pauli term. All this derives from the higher-dimensional Dirac equation. Technically, the paper uses the language of spin geometry and Riemannian submersions. Along the way, it develops detailed geometric descriptions of several constructions. It finds that the gauge representations are always anomaly-free, discusses fermion generations, and introduces a new Lie derivative of spinors along non-Killing vector fields induced by actions of compact groups.

---

## Key Arguments and Derivations

### Section 1: Introduction

The paper addresses the origin of CP violation in physics. In the Standard Model, CP violation is introduced through complex phases in the CKM and PMNS matrices -- an ad hoc adjustment. The paper shows that in the Kaluza-Klein framework, CP violation arises naturally from the higher-dimensional Dirac equation when the background metric encodes massive gauge fields.

Three sources of CP violation are identified:
1. **Misalignment** between /D_K-eigenspinors and the spinors in the gauge representation basis
2. **Non-minimal coupling** of massive gauge fields to 4D fermions (tau_{e_a} correction)
3. **Non-abelian Pauli term** in the dimensionally reduced Dirac equation

### Section 2: Spinors on Riemannian submersions

Recapitulates the framework from Paper 17 with the key decomposition:
- R_{g_P} = R_{g_M} + R_{g_K} - (1/4)|F_A|^2 - (1/4)|d_A g_K|^2 + |d_A(vol_{g_K})|^2
- S_C(P) = S_C(H) tensor S_C(V)
- Dirac operator decomposition as in Paper 17, with gauge fields coupling through the Kosmann-Lichnerowicz derivative

### Section 3: Spinor symmetries induced by 4D reflections and parity

**Key constructions.** Reflections R and parity inversions P on M4 extend to diffeomorphisms of P = M4 x K that do not change internal coordinates. These are NOT isometries of the submersion metric in general. The transformation g_P -> P* g_P encapsulates the usual parity transformation rules for 4D gauge fields.

The diffeomorphisms R and P lift to transformations of spinors, but they map between different spinor bundles (S_{g_P} and S_{R* g_P} or S_{P* g_P}), since the background metric is not preserved. Despite this, they induce symmetries of the higher-dimensional Dirac equation /D_P Psi = 0.

### Section 4: Conjugation symmetries on spinor bundles

**Conjugation maps j_sigma.** For signature (s,t), there exist conjugate-linear automorphisms j_sigma: Gamma(S_{g_P}) -> Gamma(S_{g_P}) with:
- j_sigma(V . psi) = sigma V . j_sigma(psi)
- j_sigma(nabla_V psi) = nabla_V (j_sigma psi)
- j_sigma(L_V psi) = L_V (j_sigma psi) [commutes with Kosmann-Lichnerowicz]
- j_sigma(/D psi) = sigma /D(j_sigma psi)

So j_sigma is always a symmetry of /D Psi = 0. The composed maps j_sigma P combine conjugation with parity.

**Proposition 4.6:** j_sigma P satisfies j_sigma P(/D Psi) = -sigma /D(j_sigma P Psi), so it is also a symmetry of the Dirac equation.

### Section 5: Actions of compact groups on K and its spinors

**New Lie derivative for non-isometric actions.** When a compact group G acts on K through non-isometric diffeomorphisms, the standard Kosmann-Lichnerowicz derivative L_V does not satisfy the closure relation [L_U, L_V] = L_{[U,V]}. The paper introduces a modified derivative:

L_V psi = L_V psi + (1/4) sum_{j != k} g(alpha^{-1}(L_V alpha)(v_j), v_k) v_j . v_k . psi

where alpha: TK -> TK is the unique positive-definite automorphism relating g and the averaged metric g_hat. This modified derivative satisfies [L_U, L_V] = L_{[U,V]} for all fundamental vector fields of the G-action.

**Construction.** The averaged metric g_hat(U,V) = integral_G (r_h* g)(U,V) vol_G is G-invariant. All fundamental fields are Killing for g_hat. The Kosmann-Lichnerowicz derivative L_hat_V on S_{g_hat} satisfies closure. Transporting back to S_g via the map alpha gives the new derivative L_V.

### Section 6: Representation spaces vs /D-eigenspaces

**Representation decomposition.** The space of L^2-spinors decomposes in two ways:
1. By /D_K-eigenspaces: L^2(S_g) = direct_sum_m E_m
2. By G-representation spaces: L^2(S_g) = direct_sum_{m,pi} n_{m,pi} W_{m,pi}

For non-isometric G-actions, the representation spaces W_{m,pi} are NOT contained in /D-eigenspaces E_m. This misalignment is the first source of CP violation.

**Anomaly-free.** In the chiral decomposition with W^+_{m,pi} and W^-_{m,pi}, conjugate representations always appear with equal multiplicity: n_{m,pi} = n_{m,pi_bar}. This guarantees freedom from local gauge anomalies.

**Fermion generations.** A perturbation of the internal metric that breaks the isometry group from G to G' reduces the degeneracy of /D-eigenvalues. Former /D-eigenspaces split into multiple eigenspaces with slightly different eigenvalues. Each such eigenspace can be identified with a "generation" of fermions having the same gauge representation but different masses. The number of generations equals the degeneracy of the original eigenvalue.

### Section 7: Dimensionally reduced equations and CP violation

**Full 4D Dirac equation.** After dimensional reduction of /D_P Psi = 0, each eigenspinor component phi_alpha satisfies:

i gamma^mu (nabla^M_{X_mu} phi_alpha + A^a_mu [R^alpha_beta(e_a) + tau^alpha_beta(e_a)] phi_beta)
+ m_alpha phi_alpha + Pauli term = 0

where:
- R^alpha_beta(e_a) = <psi_alpha, [L_{e_a} + (1/2)div] psi_beta> (representation matrix elements)
- tau^alpha_beta(e_a) = <psi_alpha, tau_{e_a} psi_beta> (correction from non-isometric action)

**Three sources of CP violation:**

1. **Misalignment (R-matrices).** The matrix R^alpha_beta involves the /D-eigenspinors psi_alpha, not the G-representation spinors. When G acts non-isometrically, these two bases are misaligned. The misalignment introduces complex phases that cannot be removed by unitary redefinitions -- these are the geometric analogues of CKM phases.

2. **tau-correction.** The additional term tau^alpha_beta(e_a) = (1/4) sum g(alpha^{-1}(L_{e_a} alpha)(v_j), v_k) <psi_alpha, v_j . v_k . psi_beta> is non-zero only for non-Killing e_a. It introduces an additional source of CP violation beyond the R-matrices.

3. **Pauli term.** The term (1/8) F^a_{mu nu} <psi_alpha, e_a . psi_beta> gamma^mu gamma^nu phi_beta breaks CP when the matrix elements are complex.

**CP transformation.** The composed map j_sigma P transforms the 4D Dirac equation. CP invariance requires that the equation for j_sigma P phi_alpha (the CP-conjugate) is equivalent to the original equation. This fails when the R or tau matrices have irremovable complex phases.

### Section 8: Conclusions

The paper concludes that CP violation in the Kaluza-Klein framework is a geometric consequence of encoding massive gauge fields in the higher-dimensional metric. The mechanism is natural and requires no ad hoc complex phases. The three sources of CP violation (misalignment, tau-correction, Pauli term) all stem from the same geometric origin: the internal vector fields e_a are non-Killing with respect to g_K.

---

## Key Results

1. CP violation arises naturally from the higher-dimensional Dirac equation when the background metric encodes massive gauge fields (non-Killing vector fields).
2. Three distinct geometric sources of CP violation are identified: basis misalignment, tau-correction, and non-abelian Pauli term.
3. A new Lie derivative L_V of spinors is introduced for non-isometric group actions, satisfying the closure relation for all fundamental vector fields.
4. Gauge representations in this framework are always anomaly-free (conjugate pairs with equal multiplicities).
5. Fermion generations arise naturally from the splitting of degenerate /D-eigenspaces when symmetries are broken.
6. The conjugation map j_sigma always commutes with the Kosmann-Lichnerowicz derivative (and with L_V).
7. Appendix E gives an explicit example with (SU(3) x SU(2) x U(1))/Z_6 symmetries.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Action decomposition | integral_P R_{g_P} vol = integral [R_{g_M} + R_{g_K} - (1/4)\|F_A\|^2 - (1/4)\|d_A g_K\|^2 + \|d_A(vol)\|^2] vol | eq (1.1) |
| Gauge boson mass | (Mass A^a)^2 proportional to integral <L_{e_a} g_K, L_{e_a} g_K> / (2 integral g_K(e_a,e_a)) | eq (1.2) |
| Kosmann-Lichnerowicz | L_V psi = nabla_V psi - (1/8)[g(nabla_{v_r} V, v_s) - g(nabla_{v_s} V, v_r)] v_i . v_j . psi | eq (1.3) |
| New Lie derivative | L_V psi = L_V psi + (1/4) sum g(alpha^{-1}(L_V alpha)(v_j), v_k) v_j . v_k . psi | eq (1.4) |
| Closure relation | [L_U, L_V] psi = L_{[U,V]} psi for all U, V in g | eq (5.5) |
| Averaged metric | g_hat(U,V) = integral_G (r_h* g)(U,V) vol_G | eq (5.6) |
| Transport formula | L_V = alpha^{-1} circ L_hat_V circ alpha | eq (5.10) |
| Conjugation j_sigma | j_sigma(V . psi) = sigma V . j_sigma(psi), j_sigma(/D psi) = sigma /D(j_sigma psi) | Prop 4.1 |
| j_sigma P symmetry | j_sigma P(/D Psi) = -sigma /D(j_sigma P Psi) | Prop 4.6 |
| Representation | rho_V(psi) = L_V psi + (1/2) div(V) psi | eq (6.1) |
| Chiral decomposition | L^2(S_g) = direct_sum_{m >= 0} direct_sum_pi n_{m,pi} (W^+_{m,pi} + W^-_{m,pi}) | eq (6.4) |
| Anomaly-free | n_{m,pi} = n_{m,pi_bar} (conjugate multiplicities equal) | Remark 6.1 |
| 4D Dirac with CP violation | i gamma^mu nabla^{M,A} phi_alpha + m_alpha phi_alpha + tau-correction + Pauli term = 0 | Section 7 |
| Closure defect (standard L) | [L_X, L_Y] - L_{[X,Y]} = (1/4)(L_X g)(L_Y g) antisymmetrized on spinors | eq (5.1) |

---

## Relevance to Phonon-Exflation

This is the most recent and most advanced paper in the Baptista series, published January 2026:

1. **CP violation from geometry** is a prediction the project has not yet explored. The three sources of CP violation identified here provide new observational handles: the misalignment between /D-eigenspinors and representation bases could produce measurable effects.

2. **The new Lie derivative L_V** (eq 1.4/5.10) resolves the closure defect that appears throughout the project. The project's computations use the Kosmann-Lichnerowicz derivative L_V, which does NOT satisfy closure for non-Killing fields. This paper shows how to construct a proper Lie algebra representation using the averaged metric g_hat. The project should consider whether this modification affects the BCS computations.

3. **Fermion generations from symmetry breaking** (Section 6) provides a geometric mechanism for the three generations. When the bi-invariant metric on SU(3) is perturbed (the Jensen deformation = exflation), degenerate /D-eigenspaces split, producing multiple generations with the same gauge representation but different masses. This is directly relevant to the project's PMNS analysis.

4. **Anomaly-free representations** (n_{m,pi} = n_{m,pi_bar}) is a structural constraint the project should verify in its spectral computations.

5. **The tau-correction term** in the 4D Dirac equation represents a new non-minimal coupling that the project has not accounted for. It vanishes for Killing fields but is non-zero for the Jensen deformation direction.

6. **Appendix E** with (SU(3) x SU(2) x U(1))/Z_6 symmetries provides a concrete model directly applicable to the project's framework.

7. **The conjugation maps j_sigma** and their commutation with L_V are relevant to the project's CPT analysis (Session 17a: [J, D_K(tau)] = 0). The paper's j_sigma P is the higher-dimensional version of the project's J operator.
