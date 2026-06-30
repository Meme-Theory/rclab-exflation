# Noncommutative Geometry and Particle Physics (2nd Edition)

**Author(s):** Walter D. van Suijlekom
**Year:** 2024 (preprint dated December 28, 2023)
**Publisher:** Springer (Mathematical Physics Studies)
**ISBN:** 978-3-031-59119-8 (hardcover), 978-3-031-59120-4 (eBook)
**Pages:** 264 (PDF); viii + 256 numbered pages
**Source PDF:** `downloads/Paasch/ncgphysics2nd.pdf`
**Relevance:** CRITICAL — primary reference for spectral triples, spectral action, and SM derivation from NCG

---

## Book Structure

### Front Matter
- Preface to the second edition ... p.ii
- Preface to the first edition ... p.iii
- Contents ... p.v

### Part 1: Noncommutative Geometric Spaces (p.7)

| Ch. | Title | Pages |
|:----|:------|:------|
| 1 | Introduction | 1--5 |
| 2 | Finite noncommutative spaces | 9--25 |
| 3 | Finite real noncommutative spaces | 27--41 |
| 4 | Riemannian spin manifolds | 43--61 |
| 5 | Noncommutative Riemannian spin manifolds | 63--73 |
| 6 | The local index formula in noncommutative geometry | 75--95 |

### Part 2: Noncommutative Geometry and Gauge Theories (p.99)

| Ch. | Title | Pages |
|:----|:------|:------|
| 7 | Gauge theories from noncommutative manifolds | 101--118 |
| 8 | Localization of gauge theories from NCG | 121--129 |
| 9 | Spectral invariants | 131--144 |
| 10 | Almost-commutative manifolds and gauge theories | 147--163 |
| 11 | The noncommutative geometry of electrodynamics | 165--176 |
| 12 | The noncommutative geometry of Yang--Mills fields | 177--184 |
| 13 | The noncommutative geometry of the Standard Model | 185--207 |
| 14 | Phenomenology of the noncommutative Standard Model | 209--219 |
| 15 | Beyond the Standard Model: Pati--Salam unification | 221--231 |
| 16 | Towards a quantum theory | 235--245 |

### Back Matter
- Bibliography ... p.247--256

---

## Part I: Noncommutative Geometric Spaces

### Chapter 1: Introduction (p.1--5)

Overview of the entire program. A spectral triple (A, H, D) consists of an involutive algebra A of operators on a Hilbert space H with a self-adjoint operator D modeled on the Dirac operator. The gauge group G arises from the unitary elements of A. Inner fluctuations of D give rise to gauge fields. The spectral action Tr f(D/Lambda) is gauge invariant by construction. The key application: the almost-commutative manifold M x F_SM yields the full Standard Model Lagrangian including Higgs spontaneous symmetry breaking, minimally coupled to gravity.

### Chapter 2: Finite Noncommutative Spaces (p.9--25)

Develops finite spectral triples (A, H, D) where A is a matrix algebra, H is a finite-dimensional Hilbert space, and D is a hermitian matrix encoding metric data. Key concepts:

- **Definition 2.1**: A *-algebra is a vector space with associative bilinear product and conjugate-linear involution.
- **Definition 2.2**: A matrix algebra is a direct sum A = direct_sum M_{n_i}(C).
- **Theorem 2.14**: Two matrix algebras are Morita equivalent iff their structure spaces have equal cardinality.
- **Theorem 2.18**: The metric d_{ij} on N points can be recovered from spectral data via d(i,j) = sup{|a(i)-a(j)| : ||[D,a]|| <= 1}. This is the finite-dimensional Connes distance formula.
- **Definition 2.19**: A finite spectral triple (A, H, D) consists of a matrix algebra A, finite-dimensional Hilbert space H with representation of A, and a symmetric operator D : H -> H.

Krajewski diagrams introduced for diagrammatic classification of finite spectral triples.

### Chapter 3: Finite Real Noncommutative Spaces (p.27--41)

Enriches finite spectral triples with a real structure J (anti-unitary operator implementing a right action of A on H).

- **Definition 3.1**: A finite real spectral triple (A, H, D; J, gamma) requires J : H -> H anti-unitary, with a^o := Ja*J^{-1} a right representation. Commutant property [a, b^o] = 0 and first-order condition [[D,a], b^o] = 0 required. The signs J^2 = epsilon, JD = epsilon'DJ, J*gamma = epsilon''*gamma*J determine the **KO-dimension k mod 8** per Table 3.1:

| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| epsilon | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 |
| epsilon' | 1 | -1 | 1 | 1 | 1 | -1 | 1 | 1 |
| epsilon'' | 1 | | -1 | | 1 | | -1 | |

- **Section 3.2**: Classification of finite real spectral triples in all KO-dimensions via Krajewski diagrams.
- **Section 3.3**: Real algebras and Krajewski diagrams. Relates to Clifford algebras.
- **Theorem 3.20** (Section 3.4): Irreducible finite real spectral triples of KO-dimension 6 have A = M_N(C) + M_N(C). With symplectic constraint, A = M_k(H) + M_{2k}(C) on H = C^{2(2k)^2}. The case k=2 yields the Standard Model finite space with H_F = C^{32}.

### Chapter 4: Riemannian Spin Manifolds (p.43--61)

Clifford algebras, spin structures, and the Dirac operator on Riemannian manifolds.

- **Definition 4.20**: The Dirac operator D_M = -i*gamma^mu*(partial_mu - (1/4)*Gamma^b_{mu a}*gamma_a*gamma_b).
- **Theorem 4.21 (Lichnerowicz formula)**: D_M^2 = Delta^S + (1/4)s, where s is scalar curvature.
- **Theorem 4.22**: D_M is essentially self-adjoint with compact resolvent and bounded commutators with C^inf(M). The commutator [D_M, f] = -ic(df) has norm equal to the Lipschitz seminorm of f.

### Chapter 5: Noncommutative Riemannian Spin Manifolds (p.63--73)

The central definitions of the framework.

- **Theorem 5.7 (Gelfand duality)**: Commutative unital C*-algebras correspond to compact Hausdorff spaces.
- **Proposition 5.8**: The Riemannian distance is recovered as d(x,y) = sup{|f(x)-f(y)| : ||[D_M, f]|| <= 1}.
- **Definition 5.9 (Spectral triple)**: A spectral triple (A, H, D) consists of a unital *-algebra A represented as bounded operators on H, with D self-adjoint such that (i+D)^{-1} is compact and [D,a] extends to bounded operators for all a in A. Even if there exists gamma with gamma*a = a*gamma and gamma*D = -D*gamma.
- **Definition 5.9 (Real structure)**: An anti-linear isometry J : H -> H with J^2 = epsilon, JD = epsilon'DJ, J*gamma = epsilon''*gamma*J (signs from Table 5.1, same as Table 3.1). Plus commutant property and order one condition: [a, b^0] = 0, [[D,a], b^0] = 0.
- **Product of spectral triples**: For even (A_1, H_1, D_1; gamma_1, J_1) and (A_2, H_2, D_2; gamma_2, J_2): D = D_1 x 1 + gamma_1 x D_2, gamma = gamma_1 x gamma_2, J = J_1 x J_2.
- **Definition 5.13 (Almost-commutative manifold)**: M x F := canonical triple on M tensored with finite spectral triple F. This is the geometric Ansatz for particle physics.

### Chapter 6: Local Index Formula (p.75--95)

Proves the local index formula of Connes--Moscovici. Technical chapter on Hochschild and cyclic cohomology, abstract differential calculus, residues, and the local (b,B)-cocycle. Applied to toric noncommutative manifolds.

---

## Part II: Noncommutative Geometry and Gauge Theories

### Chapter 7: Gauge Theories from Noncommutative Manifolds (p.101--118)

Derives gauge groups and gauge fields from any spectral triple.

- **Definition 7.1**: Inner automorphisms Inn(A) = U(A)/U(Z(A)).
- **Definition 7.4 (Gauge group)**: G(A,H;J) := {U = uJuJ^{-1} | u in U(A)}.
- **Proposition 7.5**: Short exact sequence 1 -> U(A_J) -> U(A) -> G(A,H;J) -> 1.
- **Equation (7.1.3)**: Under inner unitary equivalence, D -> UDU* = D + u[D,u*] + epsilon'*Ju[D,u*]J^{-1}.
- **Inner fluctuations** (eq. 7.2.5): D_omega := D + omega + epsilon'*J*omega*J^{-1}, where omega = omega* in Omega^1_D(A) is the gauge field (inner fluctuation of D).
- **Equation (7.2.6)**: Gauge transformation: omega -> u*omega*u* + u[D,u*].
- **Section 7.3**: Inner fluctuations without the first-order condition. Needed for Pati--Salam (Ch. 15). Introduces quadratic corrections omega^(2) beyond the linear omega^(1). The fluctuated Dirac becomes D' = D + omega^(1) + tilde{omega}^(1) + omega^(2), where omega^(2) = sum hat{a}_j[omega^(1), hat{b}_j]. Gauge covariance is preserved by the quadratic term (Lemma 7.20).

### Chapter 8: Localization of Gauge Theories (p.121--129)

Localization via C*-bundles on a background topological space. Gauge group acts fiberwise. Gauge fields appear as sections.

### Chapter 9: Spectral Invariants (p.131--144)

Defines and expands the spectral action.

- **Definition 9.1 (Spectral action)**: S_b[omega] := Tr f(D_omega / Lambda), where f is a positive even cutoff function and Lambda is a real cutoff parameter. (eq. 9.1.1)
- **Definition 9.1 (Topological spectral action)**: S_top[omega] = Tr gamma*f(D_omega/Lambda). (eq. 9.1.2)
- **Definition 9.3 (Fermionic action)**: S_f[omega, psi] = (J*psi_tilde, D_omega*psi_tilde) with psi_tilde in H^+_{cl}. Skew-symmetric in KO-dimension 2 mod 8.
- **Theorem 9.2**: S_b and S_top are gauge invariant.
- **Proposition 9.5**: S_top[omega] = f(0) * index(D_omega), via McKean--Singer formula.
- **Proposition 9.7 (Asymptotic expansion)**: Tr f(D/Lambda) ~ sum_{beta in S_d} f_beta * Lambda^beta * (2/Gamma(beta/2)) * c_{-beta/2} + f(0)*c_0 + O(Lambda^{-1}), where f_beta = integral f(v)*v^{beta-1} dv and S_d is the dimension spectrum. (eq. 9.2.3)
- **Section 9.3**: Perturbative (Taylor) expansion of S_b in powers of omega. Uses divided differences. Introduces bracket notation <X_0, ..., X_n>_{t,n} for heat kernel integrals over simplices. (eq. 9.3.1): S_b[omega] = sum (1/n!) S^(n)_b(0)(omega,...,omega). The brackets satisfy Ward identity (eq. 9.3.5): <a*omega_1,...,omega_n> - <omega_1,...,omega_n*a> = <[D,a],omega_1,...,omega_n>.

### Chapter 10: Almost-Commutative Manifolds and Gauge Theories (p.147--163)

The workhorse chapter connecting spectral triples to physical Lagrangians.

- **Gauge symmetries**: For M x F, the gauge group G(F) = U(A_F) / H(F), with Lie algebra g(F) = u(A_F) / h(F).
- **Fluctuated Dirac operator** (eq. 10.2.6): D_omega = D_M x 1 + gamma^mu x B_mu + gamma_M x Phi, where B_mu = A_mu - J_F*A_mu*J_F^{-1} and Phi = D_F + phi + J_F*phi*J_F^{-1}.
- **Proposition 10.6 (Generalized Lichnerowicz formula)**: D_omega^2 = Delta^E - F, with F = -(1/4)s x 1 - 1 x Phi^2 + (1/2)i*gamma^mu*gamma^nu x F_{mu nu} - i*gamma_M*gamma^mu x D_mu*Phi. (eq. 10.3.6)
- **Theorem 10.7 (Heat expansion)**: Tr(e^{-t*H}) ~ sum_{k>=0} t^{(k-n)/2} a_k(H) as t -> 0. (eq. 10.3.7)
- **Theorem 10.8 (Seeley--DeWitt coefficients)**:
  - a_0(x,H) = (4*pi)^{-n/2} Tr(id)
  - a_2(x,H) = (4*pi)^{-n/2} Tr(s/6 + F)
  - a_4(x,H) = (4*pi)^{-n/2} (1/360) Tr(-12*Delta*s + 5s^2 - 2*R_{mu nu}*R^{mu nu} + 2*R_{mu nu rho sigma}*R^{mu nu rho sigma} + 60sF + 180F^2 - 60*Delta*F + 30*Omega^E_{mu nu}*(Omega^E)^{mu nu})
- **Proposition 10.10 (Canonical spectral action on 4-manifold)**: L_M = (f_4*Lambda^4)/(2*pi^2) - (f_2*Lambda^2)/(24*pi^2)*s + (f(0))/(16*pi^2)*(1/30*Delta*s - 1/20*C_{mu nu rho sigma}^2 + 11/360*R*R*). (eq. 10.4.2)
- **Proposition 10.12 (Spectral action on AC manifolds)**: The full Lagrangian is L = N*L_M + L_B + L_phi, with:
  - L_B = (f(0))/(24*pi^2) Tr(F_{mu nu}*F^{mu nu})
  - L_phi = -(2*f_2*Lambda^2)/(4*pi^2)*Tr(Phi^2) + (f(0))/(8*pi^2)*Tr(Phi^4) + (f(0))/(24*pi^2)*Delta(Tr(Phi^2)) + (f(0))/(48*pi^2)*s*Tr(Phi^2) + (f(0))/(8*pi^2)*Tr((D_mu*Phi)(D^mu*Phi)). (eq. 10.4.10)

### Chapter 11: NCG of Electrodynamics (p.165--176)

Two-point space as simplest example. Derives U(1) gauge theory and QED Lagrangian from the spectral action. Appendix on Grassmann variables and Pfaffians.

### Chapter 12: NCG of Yang--Mills Fields (p.177--184)

Non-abelian gauge theory from algebra bundles. Derives Yang--Mills Lagrangian and topological spectral action (instanton number).

### Chapter 13: NCG of the Standard Model (p.185--207)

**THE CENTRAL CHAPTER.** Derives the full Standard Model from M x F_SM.

- **Section 13.1 (The finite space)**: Starting from irreducible geometries of KO-dimension 6 (Theorem 3.20), with k=2: A = M_2(H) + M_4(C), H_F = C^{32}. The even subalgebra A_ev = H_R + H_L + M_4(C). Imposing the first-order condition determines the maximal subalgebra:
  - **Proposition 13.1**: A_F = C + H + M_3(C) (embedded as lambda -> q_lambda in H_R and diag(lambda, m) in M_4(C)). This is the Standard Model algebra.
  - The Hilbert space decomposes into lepton space H_l and quark space H_q with basis vectors {nu_R, e_R, (nu_L, e_L)} and {u_R, d_R, (u_L, d_L)}, with three colors and three generations: H_F = (H_l + H_q)^{+3} + (H_l_bar + H_q_bar)^{+3}.
  - The finite Dirac operator D_F has components: Yukawa matrices Y_nu, Y_e, Y_u, Y_d acting on 3 generations, and Majorana mass matrix Y_R for right-handed neutrinos.

- **Section 13.2 (The gauge theory)**:
  - **Proposition 13.3**: G(F_SM) = (U(1) x SU(2) x U(3)) / {1,-1}.
  - With unimodularity: **G_SM = U(1) x SU(2) x SU(3) / mu_6** (Proposition 13.4).
  - The gauge field B_mu decomposes into U(1) field Lambda_mu, SU(2) field Q_mu, and SU(3) field V_mu, with hypercharges exactly reproducing the SM values:

  | Particle | nu_R | e_R | nu_L | e_L | u_R | d_R | u_L | d_L |
  |:---------|:-----|:----|:-----|:----|:----|:----|:----|:----|
  | Hypercharge | 0 | -2 | -1 | -1 | 4/3 | -2/3 | 1/3 | 1/3 |

  - The scalar field phi gives the Higgs doublet H = (phi_1 + 1, phi_2), transforming in the defining representation of SU(2) with hypercharge -1.

- **Section 13.3 (The spectral action)**:
  - **Lemma 13.6**: Tr(F_{mu nu}*F^{mu nu}) = 80*Lambda_{mu nu}^2 + 12*Tr(Q_{mu nu}^2) + 24*Tr(V_{mu nu}^2).
  - **Lemma 13.7**: Tr(Phi^2) = 4a|H|^2 + 2c; Tr(Phi^4) = 4b|H|^4 + 8e|H|^2 + 2d; where a,b,c,d,e are traces over Yukawa matrices (eq. 13.3.2).
  - **Coupling constant unification** (eq. 13.3.5): g_3^2 = g_2^2 = (5/3)*g_1^2 at the cutoff scale.
  - **Theorem 13.10 (Full bosonic SM Lagrangian)**: The spectral action yields:
    - Cosmological constant: 48*f_4*Lambda^4 / pi^2
    - Einstein--Hilbert: -(c*f(0)/(24*pi^2) - 4*f_2*Lambda^2/pi^2)*s
    - Conformal gravity: -3*f(0)/(10*pi^2)*C_{mu nu rho sigma}^2
    - Gauge kinetic: (1/4)*(Y_{mu nu}^2 + W^a_{mu nu}^2 + G^i_{mu nu}^2) [properly normalized]
    - Higgs potential: (b*pi^2)/(2*a^2*f(0))*|H|^4 - (2*a*f_2*Lambda^2 - e*f(0))/(a*f(0))*|H|^2
    - Higgs kinetic: (1/2)*|D_mu*H|^2
    - Higgs-gravity coupling: (1/12)*s*|H|^2

  - **Section 13.3.2 (Higgs mechanism)**: When 2*a*f_2*Lambda^2 > e*f(0), the Higgs potential has a non-trivial minimum at |H|^2 = (2*a^2*f_2*Lambda^2 - a*e*f(0))/(b*pi^2) (eq. 13.3.9). Vacuum state (v,0) breaks U(1) x SU(2) -> U(1)_em. The W and Z boson masses: M_W = (1/2)*v*g_2, M_Z = (1/2)*v*g_2/cos(theta_w) (eq. 13.3.14).

- **Section 13.4 (Fermionic action)**: **Theorem 13.11** gives the full fermionic Lagrangian:
  - L_kin: kinetic terms for all fermions
  - L_gf: gauge-fermion couplings with correct hypercharges, W/Z couplings with (1+gamma_M)/2 projection for left-handedness
  - L_Hf: Yukawa couplings to the Higgs field (mass generation)
  - L_R: Majorana mass terms for right-handed neutrinos

- **Summary (p.207)**: The spectral action on M x F_SM geometrically derives: (1) full particle content, (2) full Lagrangian including Higgs SSB and masses, (3) minimal coupling to gravity. Plus coupling constant relations at unification.

### Chapter 14: Phenomenology of the NCG Standard Model (p.209--219)

- **Section 14.1**: Mass relations from the spectral action at the unification scale. Fermion mass relation: sum(m_f^2) = 8*M_W^2. Higgs mass prediction (tree-level): m_H^2 = (8*b)/(a^2) * M_W^2.
- **Section 14.2**: Renormalization group flow. Running coupling constants from Lambda_GUT to M_Z. The original NCG prediction gave m_H ~ 170 GeV (too high; experimental: 125.1 GeV), motivating the Pati--Salam extension.

### Chapter 15: Beyond the Standard Model: Pati--Salam Unification (p.221--231)

The 2nd edition's major physics addition.

- **Section 15.1**: Uses the full irreducible algebra A = M_2(H) + M_4(C) (without truncation to A_F). Even subalgebra A_ev = H_R + H_L + M_4(C). The Pati--Salam algebra A_PS = H_R + H_L + M_4(C) with gauge group SU(2)_R x SU(2)_L x SU(4).
- **Proposition 15.1**: F_PS is a finite real even spectral triple of KO-dimension 6 with first-order condition on the SM subalgebra.
- **Section 15.2**: Scalar content: phi^b_dot{a} in (2_R, 2_L, 1), Delta_{dot{a}I} in (2_R, 1, 4), Sigma^I_J in (1, 1, 15). Composite Higgs fields arise from quadratic inner fluctuations omega^(2) (Section 7.3).
- **Gauge coupling unification** (eq. 15.2.1): g_R = g_L = g at the PS scale.
- **Section 15.3**: Truncation to SM reproduces all SM content plus an additional real singlet field sigma.
- **Section 15.4**: Phenomenology. Unification at Lambda ~ 2.5 x 10^{15} GeV with intermediate scale m_R ~ 4.25 x 10^{13} GeV. The Higgs mass can be made compatible with 125 GeV via the sigma field. RG equations for lambda_h, lambda_{h sigma}, lambda_sigma provided.

### Chapter 16: Towards a Quantum Theory (p.235--245)

Second quantization of spectral triples and one-loop corrections.

- **Section 16.1**: Fermionic second quantization. The Clifford algebra C = Cliff_C(H_R) carries a dynamical system sigma_t generated by exp(itD). KMS states at inverse temperature beta exist and are unique (Proposition 16.2). The physical Fock representation uses the complex structure I = i*sign(D) (Proposition 16.5). The creation/annihilation operators split according to the sign of D.
- **Theorem 16.9**: The von Neumann entropy of the KMS state equals the spectral action Tr(h(beta*D)) for the spectral function h(x) = E(e^{-x}), where E(x) = log(x+1) - x*log(x)/(x+1). This is the entropy-spectral action duality.
- **Section 16.2**: One-loop corrections using background field method. The gauge propagator G_{kl} = 1/f'[lambda_k, lambda_l] is bounded (unlike ordinary QFT). Ward identities (16.2.3, 16.2.4) are established diagrammatically. Two-point functions computed at one-loop; only the second and third diagrams in Table 16.1 are potentially divergent.
- **Theorem 16.10**: The divergent part of the one-loop quantum effective spectral action has the same form as the classical spectral action (Chern--Simons + Yang--Mills terms), ensuring one-loop renormalizability as a gauge theory. The counterterms are absorbed by a transformation phi -> phi + tilde{phi}, psi -> psi + tilde{psi} in the space of noncommutative integrals.

---

## Key Definitions

| Term | Definition | Location |
|:-----|:----------|:---------|
| *-algebra | Vector space with associative product and conjugate-linear involution (ab)* = b*a* | Def. 2.1, p.9 |
| Matrix algebra | Direct sum A = direct_sum M_{n_i}(C) | Def. 2.2, p.10 |
| Representation | *-algebra map pi: A -> L(H) | Def. 2.4, p.11 |
| Morita equivalence | E tensor_A F ~ B and F tensor_B E ~ A as bimodules | Def. 2.12, p.15 |
| Finite spectral triple | (A, H, D) with A matrix algebra, H inner product space, D symmetric operator | Def. 2.19 (implicit), p.19 |
| Finite real spectral triple | (A, H, D; J, gamma) with J anti-unitary, commutant + first-order conditions, KO-signs | Def. 3.1, p.27 |
| KO-dimension | Integer k mod 8 determined by signs epsilon, epsilon', epsilon'' | Table 3.1, p.28 |
| Krajewski diagram | Bipartite graph classifying finite real spectral triples | Section 3.2, p.30 |
| First-order condition | [[D, a], b^o] = 0 for all a, b in A | Eq. 3.1.1, p.27 |
| Commutant property | [a, b^o] = 0 for all a, b in A | Eq. 3.1.1, p.27 |
| Clifford algebra | Cl(V,Q) = T(V) / (v tensor v + Q(v)) | Def. 4.1, p.43 |
| Dirac operator (Riemannian) | D_M = -i*gamma^mu*(nabla^S_mu) | Def. 4.20, p.55 |
| C*-algebra | Complete *-algebra with ||a*a|| = ||a||^2 | Def. 5.1, p.63 |
| Spectral triple | (A, H, D): A unital *-algebra on H, D self-adjoint, compact resolvent, bounded [D,a] | Def. 5.9, p.65 |
| Real structure J | Anti-linear isometry with J^2=epsilon, JD=epsilon'DJ, J*gamma=epsilon''*gamma*J | Def. 5.9 cont., p.66 |
| Almost-commutative manifold | M x F = canonical triple tensor finite triple | Def. 5.13, p.68 |
| Gauge group G(A,H;J) | {U = uJuJ^{-1} : u in U(A)} | Def. 7.4, p.103 |
| Gauge Lie algebra g(A,H;J) | {T = X + JXJ^{-1} : X in u(A)} | Def. 7.7, p.104 |
| Inner fluctuation / gauge field | omega in Omega^1_D(A), self-adjoint; D_omega = D + omega + epsilon'*J*omega*J^{-1} | Eq. 7.2.5, p.110 |
| Connes differential 1-forms | Omega^1_D(A) = {sum a_k[D, b_k] : a_k, b_k in A} | Def. 5.15, p.68 |
| Spectral action | S_b[omega] = Tr f(D_omega/Lambda) | Def. 9.1, p.131 |
| Topological spectral action | S_top[omega] = Tr gamma*f(D_omega/Lambda) | Def. 9.1, p.131 |
| Fermionic action | S_f[omega, psi] = (J*psi_tilde, D_omega*psi_tilde) | Def. 9.3, p.132 |
| Seeley--DeWitt coefficients | a_0, a_2, a_4 in heat expansion Tr(e^{-tH}) ~ sum t^{(k-n)/2} a_k | Thm. 10.8, p.157 |
| Generalized Lichnerowicz formula | D_omega^2 = Delta^E - F | Prop. 10.6, p.155 |
| SM finite algebra A_F | C + H + M_3(C) | Prop. 13.1, p.186 |
| SM gauge group G_SM | U(1) x SU(2) x SU(3) / mu_6 | Prop. 13.4, p.190 |
| Higgs doublet H | (phi_1 + 1, phi_2), from scalar inner fluctuation of D_F | Eq. 13.2.2, p.192 |
| KMS state | State phi satisfying analytic boundary condition on strip I_beta | Def. 16.1, p.236 |

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Connes distance formula | d(x,y) = sup{|f(x)-f(y)| : ||[D,f]|| <= 1} | Prop. 5.8, p.65 |
| KO-dimension signs | J^2 = epsilon, JD = epsilon'DJ, J*gamma = epsilon''*gamma*J | Def. 3.1, Table 3.1, p.27--28 |
| Product Dirac operator | D = D_1 tensor 1 + gamma_1 tensor D_2 | p.68 |
| Inner fluctuation | D_omega = D + omega + epsilon'*J*omega*J^{-1} | Eq. 7.2.5, p.110 |
| Gauge transformation | omega -> u*omega*u* + u[D,u*] | Eq. 7.2.6, p.110 |
| Quadratic inner fluctuation | omega^(2) = sum hat{a}_j[omega^(1), hat{b}_j] = sum hat{a}_j*a_k*[[D,b_k], hat{b}_j] | Eq. 7.3.3, p.112 |
| Spectral action | S_b[omega] = Tr f(D_omega/Lambda) | Eq. 9.1.1, p.131 |
| Fermionic action | S_f = (J*psi_tilde, D_omega*psi_tilde) | Def. 9.3, p.132 |
| Asymptotic expansion | Tr f(D/Lambda) ~ sum f_beta*Lambda^beta * (2/Gamma(beta/2))*c_{-beta/2} + f(0)*c_0 | Eq. 9.2.3, p.133 |
| Taylor expansion of S_b | S_b[omega] = sum_{n>=0} (1/n!) S^(n)_b(0)(omega,...,omega) | Eq. 9.3.1, p.135 |
| Fluctuated Dirac on AC | D_omega = D_M tensor 1 + gamma^mu tensor B_mu + gamma_M tensor Phi | Eq. 10.2.6, p.151 |
| Generalized Lichnerowicz | D_omega^2 = Delta^E - F; F = -(1/4)s - Phi^2 + (i/2)*gamma^{mu nu}*F_{mu nu} - i*gamma_M*gamma^mu*D_mu*Phi | Eq. 10.3.6, p.155 |
| Seeley--DeWitt a_0 | a_0 = (4pi)^{-n/2} Tr(id) | Thm. 10.8, p.157 |
| Seeley--DeWitt a_2 | a_2 = (4pi)^{-n/2} Tr(s/6 + F) | Thm. 10.8, p.157 |
| Seeley--DeWitt a_4 | a_4 = (4pi)^{-n/2} (1/360) Tr(-12*Delta*s + 5s^2 - 2R_{mu nu}^2 + 2R_{mu nu rho sigma}^2 + 60sF + 180F^2 - 60*Delta*F + 30*Omega^E_{mu nu}^2) | Thm. 10.8, p.157 |
| Einstein--Hilbert from spectral | L_M = (f_4*Lambda^4)/(2pi^2) - (f_2*Lambda^2)/(24pi^2)*s + f(0)/(16pi^2)*(1/30*Delta*s - 1/20*C^2 + 11/360*R*R*) | Prop. 10.10, p.159 |
| Scalar Lagrangian on AC | L_phi = -(2f_2*Lambda^2)/(4pi^2)*Tr(Phi^2) + (f(0))/(8pi^2)*Tr(Phi^4) + ... + (f(0))/(8pi^2)*Tr((D_mu*Phi)^2) | Eq. 10.4.10, p.161 |
| SM hypercharges | nu_R:0, e_R:-2, (nu,e)_L:-1, u_R:4/3, d_R:-2/3, (u,d)_L:1/3 | p.191 |
| SM Higgs potential | L_pot = (b*pi^2)/(2a^2*f(0))*|H|^4 - (2a*f_2*Lambda^2 - e*f(0))/(a*f(0))*|H|^2 | Eq. 13.3.8, p.199 |
| Higgs VEV | |H|^2 = (2a^2*f_2*Lambda^2 - a*e*f(0))/(b*pi^2) | Eq. 13.3.9, p.199 |
| GUT coupling unification | g_3^2 = g_2^2 = (5/3)*g_1^2 | Eq. 13.3.5, p.198 |
| W and Z boson masses | M_W = (1/2)*v*g_2; M_Z = (1/2)*v*g_2/cos(theta_w) | Eq. 13.3.14, p.202 |
| Pati--Salam coupling | g_R = g_L = g | Eq. 15.2.1, p.225 |
| Entropy = spectral action | S(psi_beta) = Tr(h(beta*D)), h(x) = E(e^{-x}) | Thm. 16.9, p.240 |
| Ward identity (classical) | <a*omega_1,...,omega_n> - <omega_1,...,omega_n*a> = <[D,a],omega_1,...,omega_n> | Eq. 16.2.2, p.240 |

---

## What's New in the 2nd Edition

The preface to the second edition (p.ii) identifies the following additions relative to the 1st edition (2015):

1. **Perturbation semigroup and cyclic cocycles** in the Taylor expansion of the spectral action (Section 7.3.2 and Section 9.3.2). The semigroup structure of inner perturbations replaces the ad hoc treatment of gauge fields when the first-order condition fails.

2. **Pati--Salam unification** (Chapter 15). The full irreducible geometry M_2(H) + M_4(C) is explored without truncation to the SM subalgebra. Composite Higgs fields arise from the quadratic inner fluctuations omega^(2). Phenomenology includes coupling constant unification at ~ 2.5 x 10^{15} GeV and a Higgs mass compatible with 125 GeV.

3. **Towards a quantum theory** (Chapter 16). Second quantization of spectral triples via the Clifford algebra and KMS condition. The entropy-spectral action connection (Theorem 16.9). One-loop corrections to the spectral action with Ward identities and proof of one-loop renormalizability.

4. **Expanded Part I**: More details on analytical properties of the Dirac operator on compact Riemannian spin^c manifolds (essential self-adjointness, compact resolvent). The noncommutative torus as a key example of a spectral triple (Section 5.3.1). Cyclic cocycles illustrated for the noncommutative torus (Section 6.2.1).

5. **Inner fluctuations without first-order condition** (Section 7.3). The quadratic correction terms omega^(2) that arise when the first-order condition fails. These are essential for the Pati--Salam model and give rise to composite Higgs fields.

**Note on BCS/BdG content**: The 2nd edition of this textbook does NOT contain BCS or BdG spectral action material. The finite-density NCG formalism (chemical potential, BdG spectral action) used in the phonon-exflation project's Sessions 37--38 comes from van Suijlekom's *research papers* (particularly the 2019 Chamseddine--Connes--van Suijlekom paper on entropy and spectral action, paper #20 in the Paasch corpus), not from this textbook. This textbook provides the mathematical foundations that those papers build upon.

---

## Relevance to Phonon-Exflation

The framework uses NCG spectral triples on M^4 x SU(3) with the spectral action as the effective potential governing the dynamics of the internal geometry parameter tau. This textbook is the primary reference for the following foundational elements:

1. **Spectral triple on M x F** (Definition 5.9, 5.13): The product construction D = D_M tensor 1 + gamma_M tensor D_K(tau) is the starting point. The finite spectral triple F encodes the internal space whose tau-dependent Dirac operator D_K(tau) is the central dynamical object of the framework.

2. **KO-dimension 6** (Theorem 3.20, Definition 3.1): The classification of irreducible geometries proves that A_F = C + H + M_3(C) is the unique algebra for the SM. The project's verification that KO-dim = 6 for the SU(3) spectral triple (Sessions 7--8) directly uses this classification.

3. **Spectral action and Seeley--DeWitt coefficients** (Theorem 10.8, Proposition 10.12): The heat kernel coefficients a_0, a_2, a_4 are the terms in the effective potential V_spec(tau) that was investigated through Sessions 17--24. The a_4/a_2 ratio governs whether a stabilization minimum exists (closed: Session 24a, V-1).

4. **Inner fluctuations** (Section 7.2, eq. 7.2.5): The gauge field omega and the fluctuated Dirac operator D_omega are the objects whose spectrum determines the spectral action. The project's D_K(tau) with left-invariant metric on SU(3) is exactly this construction.

5. **Generalized Lichnerowicz formula** (Proposition 10.6): D_omega^2 = Delta^E - F directly provides the structure used in the heat kernel computations of the spectral action on SU(3).

6. **Chapter 16 (second quantization and entropy)**: The KMS condition and fermionic Fock space construction (Proposition 16.2, 16.5) connect to the BCS instability mechanism and the entropy-spectral action duality (Theorem 16.9) used in Sessions 37--38. The complex structure I = i*sign(D) on the Fock space is the starting point for the BdG construction.

7. **Pati--Salam without first-order condition** (Chapter 15, Section 7.3): The quadratic inner fluctuations omega^(2) are directly relevant to the project's treatment of inner fluctuations on SU(3) when the first-order condition fails (Sessions 22b, block-diagonal theorem).

8. **Coupling unification** (eq. 13.3.5): The relation g_3^2 = g_2^2 = (5/3)*g_1^2 at the cutoff is the GUT prediction from the spectral action. The project's g1/g2 = e^{-2*tau} metric ratio (Session 17a) extends this to tau-dependent couplings.

The textbook does not cover: BCS/BdG spectral action at finite density (van Suijlekom research papers 2019--2023), the instanton gas interpretation (Session 37), or the specific application to SU(3) as opposed to the SM finite algebra. For those, see the Paasch research paper corpus (papers #20+).
