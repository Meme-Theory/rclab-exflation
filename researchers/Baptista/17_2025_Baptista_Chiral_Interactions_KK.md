# Chiral interactions of fermions and massive gauge fields in Kaluza-Klein models

**Author(s):** Joao Baptista
**Year:** 2025
**Journal:** Not stated in PDF
**arXiv:** 2506.09126
**Relevance:** CRITICAL

---

## Abstract

In Kaluza-Klein theory, gauge fields on M4 arise as components of a higher-dimensional metric defined on M4 x K. The traditional expectation is that all the gauge fields of the Standard Model are linked to exact Killing vector fields on the internal space. This paper questions that assumption and investigates the properties of 4D gauge fields linked to non-Killing fields on K. It is shown that they have massive yet arbitrarily light bosons; they can mix fermions with different masses; and they can have asymmetric couplings to left- and right-handed fermions. None of these properties is easily satisfied by gauge fields linked to internal isometries. So the massive gauge fields produced in this manner circumvent traditional no-go arguments and offer a geometric source of chiral interactions with fermions. This may help to model the weak force within the Kaluza-Klein framework. Technically, the paper uses the language of spin geometry and Riemannian submersions. It studies the higher-dimensional Dirac operator with non-trivial background metrics. The results are derived for a general K. They are illustrated explicitly in the simpler cases where K is the two-sphere and the two-torus.

---

## Key Arguments and Derivations

### Section 2: Spinors on Riemannian submersions

**Spinor decomposition.** For P = M4 x K with submersion metric g_P = (g_M, A, g_K), the higher-dimensional spinor bundle decomposes as S_C(P) = S_C(H) tensor S_C(V), with Clifford multiplication:
- U . (phi^H tensor psi) = (gamma_5 . phi)^H tensor (U . psi) [vertical]
- X^H . (phi^H tensor psi) = (X . phi)^H tensor psi [horizontal]

Any spinor on P can be written as Psi(x,y) = sum_b phi^H_b(x) tensor psi_b(x,y). When g_K is constant along M4, the spinor expands as Psi(x,y) = sum_alpha phi^H_alpha(x) tensor psi_alpha(y) using /D_K-eigenspinors.

### Section 3: Higher-dimensional Dirac operator

**Main decomposition (Proposition 3.3).** For a spinor Psi = phi^H(x) tensor psi(x,y):

/D_P Psi = g^{mu nu}_M (X_mu . nabla^M_nu phi)^H tensor psi
           + g^{mu nu}_M A^a_nu (X_mu . phi)^H tensor [L_{e_a} + (1/2) div(e_a)] psi
           + (gamma_5 . phi)^H tensor /D_K psi
           + (1/8)(F^a_A)_{mu nu} (X_mu . X_nu . gamma_5 . phi)^H tensor (e_a . psi)
           + derivative terms along M4

**For constant g_K (Corollary 3.4):**

/D_P(phi^H tensor psi) = g^{mu nu}_M (X_mu . nabla^M_nu phi)^H tensor psi
                        + g^{mu nu}_M A^a_nu (X_mu . phi)^H tensor [L_{e_a} + (1/2) div(e_a)] psi
                        + (gamma_5 . phi)^H tensor /D_K psi
                        + (1/8)(F^a_A)_{mu nu} (X_mu . X_nu . gamma_5 . phi)^H tensor (e_a . psi)

The gauge fields couple to spinors through the Kosmann-Lichnerowicz derivative L_{e_a}. This is key: both Killing and non-Killing vector fields couple through the same derivative.

**4D Dirac equation.** After dimensional reduction, /D_P Psi = 0 gives for each /D_K-eigenspinor psi_alpha with eigenvalue m_alpha:

i gamma^mu nabla^{M,A}_{X_mu} phi'_alpha + m_alpha phi'_alpha + (1/8)(F^a_A)_{mu nu} <psi_alpha, e_a . psi_beta>_{L^2} gamma^mu gamma^nu phi'_beta = 0

with covariant derivative:
nabla^{M,A}_{X_mu} phi_alpha = nabla^M_{X_mu} phi_alpha + A^a_mu <psi_alpha, [L_{e_a} + (1/2) div(e_a)] psi_beta>_{L^2} phi_beta

### Section 4: Properties of the Kosmann-Lichnerowicz derivative

**Definition:**
L_X psi = nabla_X psi - (1/8) g^{ir} g^{js} [g(nabla_{v_r} X, v_s) - g(nabla_{v_s} X, v_r)] v_i . v_j . psi

**Key property -- commutator with /D_K:**
[/D_K, L_X] psi = (1/2) sum_{i,j} (L_X g_K)(v_i, v_j) v_i . nabla_{v_j} psi
                 + (1/4) sum_{i,j} {[nabla_{v_i}(L_X g_K)](v_i, v_j) - [nabla_{v_j}(L_X g_K)](v_i, v_i)} v_j . psi

This vanishes when X is Killing (L_X g_K = 0) but is non-zero otherwise. This is the mechanism for mass mixing and chirality.

**Compatibility with chirality:** L_X always commutes with Gamma_K (chirality operator). So it preserves Weyl spinor spaces V_+ and V_-.

**Formal anti-self-adjointness:**
integral_K {(L_X psi_1, psi_2) + (psi_1, L_X psi_2) + div(X)(psi_1, psi_2)} vol_g = 0

### Section 5: Chiral fermions

**The main chiral asymmetry result.** For two /D_K-eigenspinors phi_{m'} and psi_m with positive eigenvalues:

integral_K <phi, [/D, rho_V] Gamma_K psi> vol = (mu + mu') integral_K {<phi_+, rho_V psi_+> - <phi_-, rho_V psi_->} vol

When [/D, rho_V] != 0 (i.e., V is non-Killing), the matrix elements <phi_+, rho_V psi_+> and <phi_-, rho_V psi_-> are generally different. This is the emergence of chirality.

**Strong vs. weak chiral symmetry.** The paper distinguishes:
- Strong chiral symmetry: <phi_+, L_X psi_+> = <phi_-, L_X psi_-> for all eigenspinors
- Weak chiral symmetry: equality up to unitary redefinition of eigenspinors

Gauge fields linked to Killing vectors have strong chiral symmetry. Those linked to non-Killing vectors generally have neither.

**Anomaly-free representations.** In decomposition (6.4), the chiral subspaces W^+_{m,pi} and W^-_{m,pi} always transform under the same g-representation with the same multiplicity n_{m,pi} = n_{m,pi_bar}. This guarantees that gauge interactions are free of local gauge anomalies.

### Sections 6-7: Explicit examples

**K = T^2 (two-torus).** A simple model with two deformation parameters. Non-Killing vector fields produce massive gauge bosons with chiral interactions. The Dirac spectrum and Kosmann-Lichnerowicz matrix elements are computed explicitly.

**K = S^2 (two-sphere).** A model with SO(3) isometry group broken to U(1). The paper computes the Dirac spectrum, the mass formula for the gauge bosons, and demonstrates chiral couplings for the massive gauge fields explicitly.

---

## Key Results

1. Gauge fields linked to non-Killing internal vector fields automatically have: (a) massive bosons, (b) the ability to mix fermions of different masses, and (c) chiral couplings to fermions. These three properties always appear together.
2. The 4D Dirac equation derived from /D_P Psi = 0 contains a Pauli term coupling the gauge field strength to fermions.
3. The Kosmann-Lichnerowicz derivative L_X plays the central role: it determines ALL gauge-fermion couplings, for both Killing and non-Killing X.
4. [/D_K, L_X] != 0 for non-Killing X is the mechanism producing chiral asymmetry and mass mixing.
5. Gauge representations are always anomaly-free (conjugate pairs in chiral subspaces).
6. Explicit examples on S^2 and T^2 confirm the general results.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spinor decomposition | S_C(P) = S_C(H) tensor S_C(V) | eq (2.19) |
| Dirac operator on P | /D_P(phi^H tensor psi) = kinetic + A^a_nu [L_{e_a} + (1/2)div(e_a)] psi + gamma_5 /D_K psi + Pauli | eq (3.8) |
| 4D covariant derivative | nabla^{M,A}_{X_mu} phi_alpha = nabla^M phi_alpha + A^a_mu <psi_alpha, [L_{e_a} + (1/2)div] psi_beta> phi_beta | eq (3.10) |
| 4D Dirac equation | i gamma^mu nabla^{M,A} phi'_alpha + m_alpha phi'_alpha + (1/8) F_{mu nu} <psi_alpha, e_a . psi_beta> gamma^mu gamma^nu phi'_beta = 0 | eq (3.12) |
| Kosmann-Lichnerowicz | L_X psi = nabla_X psi - (1/8)[g(nabla_{v_r} X, v_s) - g(nabla_{v_s} X, v_r)] v_i . v_j . psi | eq (4.1) |
| Commutator [/D, L_X] | = (1/2)(L_X g)(v_r,v_s) v_i . nabla_{v_j} psi + covariant derivative terms | eq (4.7) |
| Chirality commutation | L_X Gamma_K psi = Gamma_K L_X psi | eq (4.5) |
| Formal anti-self-adjointness | integral {(L_X psi_1, psi_2) + (psi_1, L_X psi_2) + div(X)(psi_1,psi_2)} = 0 | eq (4.9) |
| Chiral asymmetry | integral <phi, [/D, rho_V] Gamma_K psi> = (mu+mu') integral {<phi_+, rho_V psi_+> - <phi_-, rho_V psi_->} | eq (6.6) |
| Representation | rho_V(psi) = L_V psi + (1/2) div(V) psi | eq (6.1) |
| Gauge boson mass | (Mass A^a)^2 proportional to integral <L_{e_a} g_K, L_{e_a} g_K> / (2 integral g_K(e_a,e_a)) | eq (1.2) |
| Closure defect | [L_X, L_Y] - L_{[X,Y]} = (1/4) [(L_X g)(L_Y g) - antisym] v_i . v_j . psi | eq (4.11) |
| Anti-self-adjoint matrix elements | <[L_{e_a} + (1/2)div] psi_alpha, psi_beta> + <psi_alpha, [L_{e_a} + (1/2)div] psi_beta> = 0 | eq (3.13) |

---

## Relevance to Phonon-Exflation

This paper provides the mathematical machinery for the project's fermionic sector:

1. **The Dirac operator decomposition** (eq 3.8) is the exact formula used in the project's computation of D_K(tau). The project's Dirac spectrum calculations (Sessions 12+) are numerical evaluations of this operator for specific SU(3) metrics.

2. **The Kosmann-Lichnerowicz derivative** L_X appearing in the gauge-fermion coupling is the operator studied in the project's BCS analysis. The matrix elements <psi_alpha, L_{e_a} psi_beta> determine the project's V-matrix elements.

3. **The commutator [/D_K, L_X]** (eq 4.7) is non-zero for the Jensen deformation direction -- this is the mechanism behind the project's result that [iK_7, D_K] = 0 (K_7 is Killing) while other directions do not commute with D_K.

4. **The closure defect** (eq 4.11) shows that the Kosmann-Lichnerowicz derivative does NOT form a Lie algebra representation for non-Killing fields. This is directly related to the project's finding that rho^L is not a homomorphism on all of su(3) but only on u(2) + su(3) (Paper 14, eq 2.65).

5. **The anomaly-free result** (Section 6) guarantees that the project's gauge representations are consistent at the quantum level.

6. **The chiral asymmetry formula** (eq 6.6) is the theoretical basis for the project's expectation that the weak force acquires chiral couplings through the Jensen deformation of the internal metric.
