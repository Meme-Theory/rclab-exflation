# Kaluza-Klein dimensional reduction and Gauss-Codazzi-Ricci equations

**Author(s):** Pei Wang
**Year:** 2008
**Journal:** arXiv preprint
**arXiv:** 0805.4479
**Relevance:** MEDIUM

Note: The filename uses "Maia_Chaves" from the batch assignment, but the actual author of arXiv:0805.4479 is Pei Wang (Northwest University, Xi'an).

---

## Abstract

In this paper we imitate the traditional method which is used customarily in the General Relativity and some mathematical literatures to derive the Gauss-Codazzi-Ricci equations for dimensional reduction. It would be more distinct concerning geometric meaning than the vielbein method. Especially, if the lower dimensional metric is independent of reduced dimensions the counterpart of the symmetric extrinsic curvature is proportional to the antisymmetric Kaluza-Klein gauge field strength. For isometry group of internal space, the SO(n) symmetry and SU(n) symmetry are discussed. And the Kaluza-Klein instanton is also enquired.

---

## Key Arguments and Derivations

### Motivation

Most KK dimensional reduction derivations use the vielbein (Cartan moving frame) method, which is elegant and fast but obscures the geometric submanifold structure. This paper instead adopts the traditional GR submanifold approach of Schouten/Yano to derive Gauss-Codazzi-Ricci equations for KK reduction. The key geometric payoff: the "extrinsic curvature" of the reduction is not symmetric -- its antisymmetric part is proportional to the Yang-Mills field strength, while its symmetric part is a submanifold-metric gradient that vanishes when the lower-dim metric is independent of the reduced coordinates. Replace lapse and shift: the shift function is replaced by the KK gauge potential; the lapse function is replaced by the scalar-field tensor N_{ij}.

### KK metric and connection setup

The standard D-dimensional -> d-dimensional KK reduction metric is
ds^2 = h_{alpha beta} dx^alpha dx^beta + N_{ij} (du^i + N^i_alpha dx^alpha)(du^j + N^j_beta dx^beta),
where for the non-Abelian case N^i_alpha = -xi^i_P A^P_alpha with xi^i_P Killing vectors on the internal space satisfying [xi_P, xi_Q]^j = C^R_{PQ} xi^j_R. Normal vectors n^i_A = (N^i_alpha, delta^i_j) and n^A_i = (0, N^{-1 ij}) allow decomposition g_{AB} = h_{AB} + N_{ij} n^i_A n^j_B. The author introduces a modified covariant operator tilde-nabla_alpha that acts on both D-dim and d-dim indices simultaneously and is metric-compatible: tilde-nabla_gamma g_{AB} = tilde-nabla_gamma h_{alpha beta} = 0.

### The K tensor (generalized extrinsic curvature)

The Gauss formula tilde-nabla_alpha h^C_beta = K^i_{alpha beta} n^C_i yields, via direct computation,
K_{alpha beta i} = -(1/2)[partial_i h_{alpha beta} + N_{ij}(D_alpha N^j_beta - D_beta N^j_alpha)].
For the non-Abelian case with Killing vectors this becomes
K_{alpha beta i} = -(1/2)(partial_i h_{alpha beta} - N_{ij} F^P_{alpha beta} xi^j_P),
where F^P_{alpha beta} = partial_alpha A^P_beta - partial_beta A^P_alpha + C^P_{QR} A^Q_alpha A^R_beta. When h_{alpha beta} is independent of u (no massive-mode gradient), the symmetric part of K vanishes and K reduces to the antisymmetric Yang-Mills field strength. This is the central geometric insight: the KK "extrinsic curvature" IS the gauge field strength, contrasting with classical submanifold theory where K is symmetric.

### Weingarten formula and L vector

The Weingarten formula gives
tilde-nabla_beta n^i_A = -h^alpha_A tilde-K^i_{beta alpha} + n^k_A L_{beta k}^i,
with L_{beta ji} = -(1/2) N^{-1 l}_i (D_beta N_{jl} + N_{lk} partial_j N^k_beta - N_{jk} partial_l N^k_beta). L satisfies tilde-L_{beta ji} + tilde-L_{beta ij} = D_beta N^{-1}_{ij}. It represents the connection on the internal-space fiber bundle.

### Gauss, Codazzi, Ricci equations

Equating two independent expressions for the antisymmetric double derivative of h^C_beta yields the Gauss equation, which after contraction and conformal rescaling g_{AB} -> (det N_{ij})^{-1/(D-2)} g_{AB} produces the Lagrangian reduction formula sqrt(-g) R = sqrt(-h) [R + terms in K, L, det N, gauge fields, scalars]. This gives the standard D-dim gravity action rewritten as d-dim gravity plus Yang-Mills plus scalar matter. The Codazzi equation gives a constraint linking the K tensor's derivatives to the off-diagonal components of the D-dim Ricci tensor R_{BA} h^B_beta n^{Ai} = (matter stress-energy constraint). The Ricci equation constrains L and couples to R_{DBjk}, with a simple i = j specialization where the right-hand side vanishes.

### Lagrangian reduction

Using the conformal transformation g_{AB} -> (det N)^{-1/(D-2)} g_{AB} so that det g_{AB} = det h_{alpha beta} det N_{ij}, the reduced Lagrangian becomes
sqrt(-g-hat) R-hat = sqrt(-h) [R + h^{alpha beta} h^{gamma delta} N^{-1 ij} (K_{alpha delta i} K_{gamma beta j} - K_{gamma delta i} K_{alpha beta j} + (1/2) partial_i h_{alpha gamma} partial_j h_{beta delta} - ...) + X(N^i_alpha, N_{kl}) + V(h_{alpha beta}) + U(det N)],
where X, V, U are explicit corrections. The author notes this gives a Lagrangian-level reduction that is essential because ansatz consistency at the equation-of-motion level does not guarantee consistency at the action level.

### SO(n) example with spherical harmonics

For SO(n) isometry with spherical internal space S^{n-1}, using Killing vectors V^{IJ}_i = y^{[I} partial_i y^{J]} built from spherical harmonics y^I with y^I y_I = 1, the author shows Kaluza-Klein fields split as N^I_alpha = (L . A_alpha)^{IJ} y_J with L the so(n) generators. Introducing the scalar-field tensor T_{IJ}(x) produces
N_{ij} = Delta^{-1} T^{-1}_{IJ} partial_i y^I partial_j y^J, Delta = T_{IJ} y^I y^J,
K_{alpha beta i} = -(1/2)[partial_i h_{alpha beta} + Delta^{-1} T^{-1}_{IJ} y_K partial_i y^I (L . F)^{KJ}].

### SU(n) example via SO(2n) embedding

Since SU(n) is a subgroup of SO(2n), the author pairs spherical harmonics as complex coordinates z^a = y^a + i y^{a+n} with SU(n) generators t = T|_{basic} and T = T|_{2n-dim}. Specific generator realizations are given for SU(2) (Pauli matrices tau, with Sigma = L_{14} + L_{23}, etc.) and SU(3) (Gell-Mann matrices lambda, with Lambda_1 = L_{15} + L_{24}, ..., Lambda_8 = (1/sqrt(3))(L_{14} + L_{25} - 2 L_{36})). The reduced SU(n) metric takes the form
ds^2 = h_{alpha beta} dx^alpha dx^beta + Delta^{-1} [dz^a + (t . A)^{ac} z_c]^dagger T^{-1}_{ab} [dz^b + (t . A)^{bd} z_d],
with constraint z^{a dagger} z_a = 1 and Delta = T_{IJ} y^I y^J.

### IIB supergravity S^5 reduction and KK monopole/instanton

The author connects the SO(n) formalism to the Cvetic-Lu-Pope-Sadrzadeh-Tran ansatz for 10D IIB supergravity reduction on S^5 to 5D gauged SO(6) supergravity, noting that an SU(3) sub-ansatz can be embedded in this SO(6) structure. For the 11D KK monopole (Section 4.2), the standard metric ds^2_{11} = e^{-phi/6} ds^2_{10} + e^{4 phi/3} (dx^{10} + A^+/-)^2 with Wu-Yang-gauged U(1) potential A^+/- = (Q_m/(2 r (y_3 +/- r))) (y_1 dy_2 - y_2 dy_1) is presented. For the KK instanton (BPST on S^4), the author writes the de Sitter-coordinate metric ds^2_4 = [dr^2 + r^2 (sigma_1^2 + sigma_2^2 + sigma_3^2)]/(1 + r^2/a^2)^2 and the corresponding self-dual SU(2) potentials (1/(2i)) tau . A^{(+)}_mu = r^2/(r^2 + a^2) i sigma . tau and (1/(2i)) tau . A^{(-)}_mu = a^2/(r^2 + a^2) i sigma . tau, which are related by a gauge transformation h = (t - i x . tau)/r across the S^4 hemispheres.

## Key Results

1. Derivation of Gauss-Codazzi-Ricci equations for KK dimensional reduction using the traditional GR submanifold method (Schouten/Yano) instead of vielbein.
2. The KK "extrinsic curvature" K^i_{alpha beta} is a mixed tensor: symmetric part is a submanifold metric gradient (vanishes if h_{alpha beta} is u-independent), antisymmetric part is proportional to the Yang-Mills field strength F^P_{alpha beta}.
3. The KK gauge potential replaces the ADM shift function; the scalar-field tensor N_{ij} replaces the lapse function.
4. A modified covariant operator tilde-nabla (using D_alpha = partial_alpha - N^i_alpha partial_i) restores metric compatibility tilde-nabla g = tilde-nabla h = 0.
5. After conformal transformation g -> (det N)^{-1/(D-2)} g, the Gauss equation yields the Lagrangian reduction formula for D-dim gravity -> d-dim gravity + Yang-Mills + scalars.
6. The Gauss equation provides a Lagrangian-level reduction that is stronger than the equation-of-motion-level consistency claimed by Pauli reductions; it may detect ansatz inconsistencies invisible at the EOM level.
7. Explicit SO(n) reduction using spherical harmonics y^I, with Killing vectors V^{IJ}_i = y^{[I} partial_i y^{J]}.
8. SU(n) reductions embedded in SO(2n) using complex pairing z^a = y^a + i y^{a+n}; explicit SU(2) and SU(3) generator realizations.
9. KK monopole over S^2 with U(1) Wu-Yang gauge and KK instanton as a fiber bundle over S^4 with SU(2) BPST connection.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| KK metric | ds^2 = h_{alpha beta} dx^alpha dx^beta + N_{ij} (du^i + N^i_alpha dx^alpha)(du^j + N^j_beta dx^beta) | Eq. 1 |
| Non-Abelian shift | N^i_alpha = -xi^i_P A^P_alpha | Eq. 2 |
| Killing algebra | [xi_P, xi_Q]^j = C^R_{PQ} xi^j_R | Eq. 3 |
| Normal vectors | n^i_A = (N^i_alpha, delta^i_j), n^A_i = (0, N^{-1 ij}) | Eq. 4 |
| Metric decomposition | g_{AB} = h_{AB} + N_{ij} n^i_A n^j_B | Eq. 5 |
| Gauss formula | tilde-nabla_alpha h^C_beta = K^i_{alpha beta} n^C_i | Eq. 16 |
| K tensor | K_{alpha beta i} = -(1/2)[partial_i h_{alpha beta} + N_{ij}(D_alpha N^j_beta - D_beta N^j_alpha)] | Eq. 21 |
| Non-Abelian K | K_{alpha beta i} = -(1/2)(partial_i h_{alpha beta} - N_{ij} F^P_{alpha beta} xi^j_P) | Eq. 22 |
| Field strength | F^P_{alpha beta} = partial_alpha A^P_beta - partial_beta A^P_alpha + C^P_{QR} A^Q_alpha A^R_beta | Eq. 23 |
| Weingarten | tilde-nabla_beta n^i_A = -h^alpha_A tilde-K^i_{beta alpha} + n^k_A L_{beta k}^i | Eq. 24 |
| L constraint | tilde-L_{beta ji} + tilde-L_{beta ij} = D_beta N^{-1}_{ij} | Eq. 28 |
| Gauss equation | h^{AB} h^{CD} R_{ADBC} = h^{alpha beta} S_{alpha gamma beta}^gamma + K-K cross terms + scalar gradient terms | Eq. 34 |
| Conformal rescaling | g_{AB} -> g-hat_{AB} = (det N_{ij})^{-1/(D-2)} g_{AB} | Eq. 42 |
| Determinant identity | det g_{AB} = det h_{alpha beta} det N_{ij} | Eq. 41 |
| Lagrangian reduction | sqrt(-g-hat) R-hat = sqrt(-h) [R + K^2 terms + X + V + U] | Eq. 43 |
| Codazzi equation | tilde-nabla_beta tilde-K^{alpha i}_alpha - tilde-nabla_alpha tilde-K^{alpha i}_beta + L-K terms = R_{BA} h^B_beta n^{Ai} | Eq. 48 |
| SO(n) Killing vectors | V^{IJ}_i = y^{[I} partial_i y^{J]} | Eq. 52 |
| SO(n) scalar tensor | N_{ij} = Delta^{-1} T^{-1}_{IJ} partial_i y^I partial_j y^J, Delta = T_{IJ} y^I y^J | Eq. 58 |
| SU(n) reduction | ds^2 = h_{alpha beta} dx^alpha dx^beta + Delta^{-1} [dz^a + (t.A)^{ac} z_c]^dagger T^{-1}_{ab} [dz^b + (t.A)^{bd} z_d] | Eq. 83 |
| SU(3) generator (Lambda_8) | Lambda_8 = (1/sqrt(3))(L_{14} + L_{25} - 2 L_{36}) | Eq. 81 |

## Relevance to Phonon-Exflation

This paper is directly relevant to the framework's M4 x SU(3) structure: the author's explicit SU(n) reduction formulas (embedded in SO(2n)) via complex-paired spherical harmonics z^a = y^a + i y^{a+n} and SU(3) generator realizations (Lambda_1 through Lambda_8) provide the machinery for doing the KK reduction of M4 x SU(3) at the Lagrangian level rather than only at the level of equations of motion. The central geometric insight -- that the KK "extrinsic curvature" K^i_{alpha beta} is an antisymmetric tensor proportional to the Yang-Mills field strength F^P_{alpha beta} rather than the symmetric extrinsic curvature of ordinary submanifold theory -- is the natural structure within which the framework's U(1)_7 gauge field emerges from the Jensen-deformed SU(3) fiber. The Lagrangian-level reduction (Gauss equation after conformal rescaling) is stronger than equation-of-motion-level reductions because it can catch ansatz inconsistencies (Pauli reductions) that would invalidate attempts to match to 4D physics; this is precisely what the framework needs when deriving the 4D Einstein-Hilbert action from the second Seeley-DeWitt coefficient a_2. The explicit SU(3) generator table in terms of SO(6) Lambda_i generators is the correct starting point for any computation of how fiber excitations (phononic relay patterns) carry KK quantum numbers. Finally, the author's observation that the Gauss-Codazzi-Ricci equations depend on the choice of gauge potential A (being defined in distinct neighborhoods) parallels the framework's use of Wu-Yang-gauge-like patches to describe the substrate geometry without singular coordinate artifacts.
