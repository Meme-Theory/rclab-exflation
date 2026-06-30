# Higher-dimensional routes to the Standard Model fermions

**Author(s):** Joao Baptista
**Year:** 2021
**Journal:** Not stated in PDF
**arXiv:** 2105.02901
**Relevance:** CRITICAL

---

## Abstract

In the old spirit of Kaluza-Klein, we consider a spacetime of the form P = M4 x K, where K is the Lie group SU(3) equipped with a left-invariant metric that is not fully right-invariant. We observe that a complete generation of fermionic fields can be encoded in the 64 components of a single spinor over the 12-dimensional spacetime. The behaviour of the spinorial function along the internal space K can be chosen so that, after pairing and fibre-integration over K, the resulting Dirac kinetic terms in four dimensions couple to the u(1) + su(2) + su(3) gauge fields in the exact chiral representations present in the Standard Model. Although we describe the action of the internal Dirac operator on the 12-dimensional spinor, the full calculation of the fermionic mass terms produced by the model is longer and is not carried out here. We calculate instead the action of the internal Laplace operator on the spinor components.

---

## Key Arguments and Derivations

### Section 2: Spinorial functions on M4 x K

**12-dimensional gamma matrices.** The 64-dimensional spinor space Delta_12 is identified with 8x8 complex matrices. A set of (11,1)-dimensional gamma matrices {Gamma_a} are constructed from 4D gamma matrices gamma_mu, Pauli matrices sigma_b, and Euclidean gamma matrices gamma^E_k via Kronecker products. Key relations:
- Gamma_0 Psi = (gamma_0 tensor I_2) Psi
- Gamma_b Psi = (gamma_0 gamma_5 tensor sigma_b) Psi for b = 1,2,3
- Gamma_{3+k} Psi = (gamma_5 tensor I_2) Psi (I_2 tensor gamma^E_k) for k = 1,...,4
- Gamma_{7+l} Psi = (gamma^l_E gamma^4_E tensor I_2) Psi (sigma_3 tensor gamma_5)
- Gamma_11 Psi = (gamma_5 tensor I_2) Psi (i sigma_2 tensor gamma_5)

The 12D chiral operator is Gamma_hat Psi = -(gamma_5 tensor I_2) Psi (sigma_1 tensor gamma_5).

**Spinor vertical behaviour (the key prescription).** The 8x8 spinor Psi = [psi_+, psi_-] is extended from M4 to P = M4 x K via:

Psi_P(x, h) = [(S(h) tensor I_2) psi_+(x) S_bar(h), (S(h) tensor I_2) psi_-(x) S_bar(h)]

where S(h) is the 4x4 matrix:
S(h) = [[s(h), 0], [0, h]]

and s(h) = sqrt(2) [(h_11)^2 + (h_21)^2 + (h_31)^2] = sqrt(2) (h^T h)_{11}.

The components psi_pm decompose as 4x4 matrices of Weyl spinors:
psi_pm = [[a_pm, c_pm^T], [b_pm, D_pm]]

with vertical transformations:
- a^P_pm(x,h) = |s(h)|^2 a_pm(x)
- b^P_+(x,h) = s(h) h b_+(x), b^P_-(x,h) = s_bar(h) h b_-(x)
- c^P_+(x,h) = s(h) h^dagger c_+(x), c^P_-(x,h) = s_bar(h) h^T c_-(x)
- D^P_+(x,h) = h D_+(x) h_bar, D^P_-(x,h) = h D_-(x) h_bar

**Gauge representations (component D).** After fibre-integration, the D-components couple to gauge fields through:
nabla^A_mu D_1 = partial_mu D_1 + sum_{j=1}^4 A^j_L(X_mu) e_j D_1 - sum_{j=1}^8 A^j_R(X_mu) D_1 e_j

The strong force A_R acts on each row of D through the fundamental SU(3) representation. The electroweak A_L acts by left-multiplication by u(2) matrices. This gives the identification:
D_+(x) = [[d_R^T], [u_L^T], [d_L^T]]

**Gauge representations (component b).** The b-components satisfy:
nabla^A_mu b_1 = partial_mu b_1 + sum_{j=1}^4 A^j_L(X_mu) [2(e_j)_{11} I_3 + e_j] b_1

Crucially, A_R does NOT couple to b, so b represents leptons:
b_+(x) = [[e^-_R], [nu_L], [e^-_L]]

**Gauge representations (component c).** The c-components couple to A_R through the fundamental representation and to A_L only through the U(1) hypercharge. This identifies:
c_+(x) = u_R(x) (3-vector of color components)

**Gauge representations (component a).** The a-component decouples from ALL gauge fields. This is the right-handed neutrino: a_+(x) = nu_R(x).

**Complete fermion identification.** The full 8x8 spinor matrix encodes one complete generation:

Psi(x) = [[nu_R, u^r_R, u^g_R, u^b_R, nu_L, u^r_L, u^g_L, u^b_L],
           [e^-_R, d^r_R, d^g_R, d^b_R, e^+_L, d^r_L, d^g_L, d^b_L],
           [nu_L, u^r_L, u^g_L, u^b_L, nu_R, u^r_R, u^g_R, u^b_R],
           [e^-_L, d^r_L, d^g_L, d^b_L, e^+_R, d^r_R, d^g_R, d^b_R]]

(each entry is a 2-component Weyl spinor, {r,g,b} are color indices)

**Electromagnetic charges and coupling constants.** The positron charge is:
e = sqrt(6 kappa_M / beta(gamma_phi, gamma_phi))

The gauge coupling constants in terms of the metric parameters lambda_1, lambda_2, lambda_3:
- g'/2 = sqrt(3/lambda_1)
- g/2 = 1/sqrt(lambda_2)
- g_s/2 = 2 sqrt(2) / sqrt(lambda_1 + 3 lambda_2 + 4 lambda_3)
- e = 2 sqrt(3) / sqrt(lambda_1 + 3 lambda_2)

**Uniqueness.** The vertical transformation is not unique. A family of scalar functions s_phi(h) = alpha [s_1(h) - 2(1 + e^{2i phi}) s_2(h)] parametrized by a phase phi all produce the correct gauge representations, where s_1(h) = (h_11)^2 + (h_21)^2 + (h_31)^2 and s_2(h) = h_11 h_21 + h_11 h_31 + h_21 h_31.

### Section 3: Masses induced in four dimensions

**Dirac operator on K.** For the left-invariant metric g_phi, the Dirac operator on K can be written as:
D_K psi = sum_j Gamma_j L_{v^L_j} psi + sum_{j<k<l} alpha_{jkl} Gamma_j Gamma_k Gamma_l psi

where the coefficients alpha_{jkl} involve the metric g_phi and the Lie bracket structure.

**Laplacian eigenvalues.** The action of the scalar Laplacian Delta_K on each spinor component produces mass matrices:
- For D_pm: mass matrix Omega^D_g = sum_j e_j e_j + (1/3) Tr(e_j e_j) I_3
- For b_pm: mass matrix Omega^b_g depends on the scalar function s_phi and the metric
- For c_pm: mass matrix Omega^c_g is proportional to I_3
- For a_pm: the integral involves |grad |s|^2|^2

The full Dirac mass calculation is noted as important but not carried out in this paper.

---

## Key Results

1. A complete generation of Standard Model fermions (16 Weyl spinors) fits into a single 12-dimensional spinor with 64 complex components (an 8x8 matrix).
2. The vertical behaviour of the spinor along K = SU(3), prescribed by the transformation S(h), produces after fibre-integration exactly the chiral gauge representations of the Standard Model.
3. The right-handed neutrino (component a) decouples from all gauge fields -- it appears naturally as a sterile particle.
4. Leptons (component b) do not couple to the strong force because the integral of s_bar(L_{v_R} s) over K vanishes.
5. The electromagnetic charges are correctly reproduced, with the photon field identified as the component of A_L along gamma_phi.
6. The rho_L representation does NOT define a Lie algebra homomorphism from the full su(3) + su(3) to su(Delta_12), but it DOES when restricted to u(2) + su(3) -- the Standard Model gauge algebra.
7. The vertical transformation S(h) is not unique but belongs to a family parametrized by a phase phi and symmetric polynomials in |h_{k1}|^2.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spinor space | Delta_12 = M_{8x8}(C) | eq (2.1) |
| 12D gamma matrices | Gamma_{3+k} Psi = (gamma_5 tensor I_2) Psi (I_2 tensor gamma^E_k) | eq (2.8) |
| 12D chiral operator | Gamma_hat Psi = -(gamma_5 tensor I_2) Psi (sigma_1 tensor gamma_5) | eq (2.10) |
| Vertical transformation | S(h) = [[s(h), 0], [0, h]] with s(h) = sqrt(2)(h^T h)_{11} | eqs (2.15)-(2.16) |
| Extension to P | Psi_P(x,h) = [(S(h) tensor I_2) psi_+(x) S_bar(h), ...] | eq (2.17) |
| D covariant derivative | nabla^A_mu D = partial_mu D + A^j_L e_j D - A^j_R D e_j | eq (2.27) |
| b covariant derivative | nabla^A_mu b = partial_mu b + A^j_L [2(e_j)_{11} I_3 + e_j] b | eq (2.40) |
| c covariant derivative | nabla^A_mu c = partial_mu c - 2 A^j_L (e_j)_{11} c + A^j_R e_j c | eq (2.51) |
| Gauge representations | rho^L_v(psi) = [[0, -2v_{11} c^T], [(2v_{11} I_3 + v) b, v D]], rho^R_v(psi) = [[0, (vc)^T], [0, -Dv]] | eq (2.62) |
| Fermion identification | Psi(x) = 8x8 matrix encoding nu_R, e^-_R, u_{L,R}, d_{L,R} + antiparticles | eq (2.66) |
| Positron charge | e = sqrt(6 kappa_M / beta(gamma_phi, gamma_phi)) | eq (2.78) |
| Coupling constants | g'/2 = sqrt(3/lambda_1), g/2 = 1/sqrt(lambda_2), g_s/2 = sqrt(kappa_M / lambda_tilde) | eqs (2.93) |
| EM circle length | e = 6 pi sqrt(2 kappa_M) / l_gamma | eq (2.81) |
| Closure defect | [rho^L_u, rho^L_v] - rho^L_{[u,v]} = [[0, 2[u,v]_{11} c^T], [-2[u,v]_{11} b, 0]] | eq (2.65) |
| Dirac operator on K | D_K psi = sum_j Gamma_j L_{v^L_j} psi + sum_{j<k<l} alpha_{jkl} Gamma_j Gamma_k Gamma_l psi | eq (3.6) |
| Dirac coefficients | alpha_{jkl} = (3/4) beta([v_j,v_k], v_l) + phi-dependent terms | eq (3.8) |
| D-mass matrix | Omega^D_g = sum_j e_j e_j + (1/3) Tr(e_j e_j) I_3 | eq (3.19) |
| b-mass matrix | Omega^b_g = sum_j e_j e_j + 4(e_j)_{11} e_j + [2(e_j)^2_{11} + (e_j e_j)_{11}/(1+8cos^2(phi))] I_3 | eq (3.22) |
| Uniqueness family | s_phi(h) = alpha [s_1(h) - 2(1 + e^{2i phi}) s_2(h)] | eq (2.104) |
| Normalization factor zeta | zeta = (Vol K)^{-1} integral_K \|s\|^4 vol_K = 4/3 | eq (2.64) |

---

## Relevance to Phonon-Exflation

This paper is the fermionic companion to Paper 13 and provides the spinorial foundation for the project:

1. **The 64-component spinor Psi = C^{16} decomposition** (eq 2.66) is the basis for the project's KO-dim = 6 result (Session 7-8). The identification Delta_12 = M_{8x8}(C) with the 16 Weyl spinors of one generation maps directly to the Psi_+ = C^{16} structure used throughout.

2. **The closure defect** (eq 2.65) -- [rho^L, rho^L] fails to be a homomorphism on all of su(3) but succeeds on u(2) + su(3) -- is the algebraic root of the project's [iK_7, D_K] = 0 result (Session 34). The Jensen direction K_7 = gamma_phi generates the unique U(1) that commutes with everything.

3. **The vertical transformation S(h)** and its non-uniqueness family s_phi(h) are directly relevant to the project's BCS analysis, where different choices of s(h) correspond to different internal oscillation modes of the spinor.

4. **The Dirac operator formula** (3.6) with its alpha_{jkl} coefficients depending on phi is the starting point for all spectral computations of D_K in the project (Sessions 12+). The phi-dependence of these coefficients is what generates the tau-dependent Dirac spectrum.

5. **The Laplacian mass matrices** Omega^D_g and Omega^b_g give the leading-order mass structure. The project's phi_paasch ratio m_{(3,0)}/m_{(0,0)} = 1.531580 at tau = 0.15 derives from diagonalizing these matrices at specific tau values.

6. **The representation rho^L** (eq 2.62) is the key operator appearing in the project's Kosmann-Lichnerowicz derivative computations, connecting the internal geometry to the 4D gauge couplings.
