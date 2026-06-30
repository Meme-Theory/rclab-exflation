# Deriving the Gibbons-Maldacena-Nunez no-go theorem from the Raychaudhuri equation

**Author(s):** Mir Mehedi Faruk (Department of Physics, McGill University)
**Year:** 2024
**Journal:** arXiv preprint
**arXiv:** 2402.08805
**Relevance:** CRITICAL

---

## Abstract

In this article, we point out that to solve the null Raychaudhuri equation for higher dimensional spacetime with accelerating FRW solution in external directions and static compact internal directions, it is necessary to violate the Strong Energy condition in higher dimensions. This constraint is well-known in obtaining accelerating cosmological solutions in string compactification, first described by Gibbons-Maldacena-Nunez. In deriving this constraint, we do not make any assumptions regarding the matter content.

---

## Key Arguments and Derivations

**Motivation and context.** The observed accelerated expansion of the Universe is consistent with a de Sitter (dS) phase, which creates tension with string/M-theory because its low-energy effective supergravity theories in 10/11 dimensions do not admit time-independent compactifications to de Sitter space in most settings. The Gibbons-Maldacena-Nunez (GMN) no-go theorem rules out such compactifications when the higher-dimensional stress tensor satisfies the Strong Energy Condition (SEC). A recent article by Das, Haque, and Underwood [60 in Faruk] claimed a stronger result using the Raychaudhuri equation: that accelerating backgrounds in string theory can only solve the Raychaudhuri equation when the null energy condition (NEC) is violated or the internal directions have positive curvature. Faruk's paper revisits this claim and argues that in fact the Raychaudhuri equation only requires (averaged) SEC violation, recovering the GMN no-go statement.

**Section I: Energy conditions.** The NEC for a null vector l^M is R_MN l^M l^N >= 0 (Eq. 1). The SEC for a timelike vector t^M is R_MN t^M t^N >= 0 with t^2 < 0 (Eq. 2). For a FRW metric in physical time coordinates g_tilde_{mu nu} dx^mu dx^nu = -dt^2 + a^2(t) delta_ij dx^i dx^j (Eq. 3), accelerating solutions satisfy a_dotdot/a = H_dot + H^2 > 0 (Eq. 4). For power-law scale factor a(t) ~ t^gamma, SEC is equivalent to 0 < gamma <= 1 (Eq. 5) and NEC to gamma >= 0 (Eq. 6). NEC violation is much harder to produce than SEC violation; no known classical energy-momentum source violates NEC.

**Section II: Null Raychaudhuri equation.** For null geodesic congruences with affine parameter lambda,

  d theta/d lambda = -[1/(D-2)] theta^2 - sigma^2 - R_MN l^M l^N      (Eq. 7)

with expansion theta = (1/sqrt(-g_D)) partial_M(sqrt(-g_D) l^M) (Eq. 8) and shear sigma_MN defined in Eq. 9. The transverse metric h_hat_MN satisfies h_hat_MN l^M = 0 (Eq. 10).

**Section III: GMN no-go theorem review.** Consider a warped product D = d + n dimensional manifold with external FRW factor and time-independent compact internal manifold:

  ds^2 = e^{-2 A(y^m)} g_mu_nu dx^mu dx^nu + e^{2 A(y^m)} g_mn(y^m) dy^m dy^n     (Eq. 11)

Equivalently, via conformal rescaling of the internal metric,

  ds^2 = Omega^2(y^m) [g_tilde_{mu nu} dx^mu dx^nu + h_tilde_mn(y^m) dy^m dy^n]     (Eq. 12)

with Omega the warp factor, assumed non-singular on a compact manifold without boundary. The D-dimensional Ricci tensor in the external direction is

  R^{(D)}_mu_nu = R^{(d)}_mu_nu(g_tilde) - g_tilde_mu_nu [nabla^2 (ln Omega) + (D-2)(nabla ln Omega)^2]     (Eq. 13)

Using Einstein's equation for the full metric gives R^{(D)}_mu_nu = T_mu_nu - [Omega^2/(D-2)] g_tilde_mu_nu T^M_M (Eq. 14). Comparing (13) and (14) and taking the trace over g_tilde:

  [1/(D-2)] nabla^2 Omega^{D-2}/Omega^{D-2} = R^{(d)} + Omega^2 (-T^mu_mu + [d/(D-2)] T^M_M)     (Eq. 15)

Positive curvature R^{(d)} > 0 requires (D - d - 2) T^mu_mu > d T^m_m (Eq. 16). In physical time coordinates,

  R^{(D)}_00 = -(d-1)(H_dot + H^2) + [Omega^{-(D-2)}/(D-2)] nabla^2 Omega^{(D-2)}     (Eq. 17)

Multiplying by Omega^{D-2} and integrating over compact internal space,

  (d-1)(G_D/G_d)(H_dot + H^2) = -integral d^n y_tilde sqrt(h_tilde) Omega^{(D-2)} R^{(D)}_00     (Eq. 18)

For accelerating solutions (H_dot + H^2 > 0), the SEC must be violated in an integrated sense: integral d^n y_tilde sqrt(h_tilde) Omega^{D-2} R^{(D)}_00 < 0 (Eq. 19). For accelerating FRW, R^{(4)} = 3(a_dotdot/a + (a_dot/a)^2) > 0 (Eq. 20).

**Section IV: Raychaudhuri equation and GMN.** Take affine null vectors N^M = (1/Omega^2)(1, 0, 0, 0, n_tilde^m) (Eq. 21) where n_tilde^m is an affine unit n-dimensional spacelike vector with respect to h_tilde_mn: h_tilde_mn n_tilde^m n_tilde^n = 1, n_tilde^m nabla_tilde_m n_tilde^n = 0 (Eq. 22). The expansion parameter is theta = N^m partial_m [ln(Omega^{D-2} sqrt(h_tilde))] + 3 H/Omega^2 (Eq. 23), with sqrt(h_tilde) = det(h_tilde_mn)^{1/2}. Shear components are listed in Eqs. 24-27. Combining the Raychaudhuri equation with expansion and shear yields

  3(H^2 + H_dot^2) = R_tilde^{(n)}_mn n_tilde^m n_tilde^n + A_mn(Omega) n_tilde^m n_tilde^n - Omega^4 R^{(D)}_MN N^M N^N     (Eq. 28)

with A_mn(Omega) = (D-2)[partial_m(ln Omega) partial_n(ln Omega) - nabla_m partial_n(ln Omega)]. Rewriting as

  3(H^2 + H_dot) = R_tilde^{(n)}_mn n_tilde^m n_tilde^n + A_mn(Omega) n_tilde^m n_tilde^n - R^{(D)}_00 - R^{(D)}_mn n_tilde^m n_tilde^n     (Eq. 29)

Using the conformal relationship between R^{(D)}_mn and R_tilde^{(n)}_mn (analog of Eq. 13 for the internal directions; Eq. 30), Faruk shows the A_mn(Omega) contribution cancels exactly with the last term in (30). The result (Eq. 31):

  3(H^2 + H_dot) = -R^{(D)}_00 + [(D-2) partial_p ln Omega partial^p ln Omega + box ln Omega] h_tilde_mn n_tilde^m n_tilde^n

Using h_tilde_mn n_tilde^m n_tilde^n = 1 and multiplying both sides by Omega^{D-2} and integrating over the compact internal space (noting the Laplacian of the warp factor integrates to zero because the warp factor is non-singular and the manifold has no boundary),

  **3(H^2 + H_dot)(G_D/G_d) = -integral d^n y_tilde sqrt(h_tilde) Omega^{D-2} R^{(D)}_00**     (Eq. 33)

For dS (H_dot = 0) and for other accelerating FRW (H_dot + H^2 > 0), the LHS is positive, so the RHS must be positive. This requires

  **integral d^n y_tilde sqrt(h_tilde) Omega^{D-2} R^{(D)}_00 < 0**     (Eq. 34)

i.e. an integrated (averaged) SEC violation in the higher-dimensional directions. This is precisely the GMN no-go statement, recovered purely from the Raychaudhuri equation and the conformal transformation of the Ricci tensor, without any presumption on matter content.

**Divergence from Das-Haque-Underwood.** Faruk notes his conclusion differs from [60] because those authors did not use the conformal relation (30) to relate R_tilde^{(n)}_mn with R^{(D)}_mn. When (30) is used, the spacelike-part contribution vanishes and the warp factor contribution is removed by integration over the compact space, leaving only an R_00-only constraint indicating averaged SEC violation, not pointwise NEC violation. The chain back to Einstein equations is reinforced by Jacobson's thermodynamic derivation: even without invoking Einstein's equation explicitly, the Raychaudhuri equation plus delta Q = T dS implies it.

## Key Results

1. **Null Raychaudhuri equation alone, applied to a warped compactification (Eq. 12), gives the integrated constraint 3(H^2 + H_dot)(G_D/G_d) = -integral Omega^{D-2} R^{(D)}_00 (Eq. 33).**
2. **For dS or other accelerating FRW, the LHS is positive, forcing an averaged higher-dimensional SEC violation: integral Omega^{D-2} R_00 < 0 (Eq. 34).** This reproduces the Gibbons-Maldacena-Nunez no-go theorem.
3. **NEC violation is not required**, contrary to the claim of Das-Haque-Underwood. The discrepancy traces to use of the conformal Ricci tensor relation (Eq. 30), which causes the A_mn(Omega) piece and the warp factor Laplacian to drop out when integrated over the compact internal manifold.
4. **The result is matter-agnostic.** Faruk makes no assumption about the matter content; the constraint follows purely from the geometric identity.
5. **Jacobson equivalence.** Although Einstein's equation is not invoked explicitly, Jacobson's derivation (Raychaudhuri + delta Q = T dS => Einstein eq. as equation of state) ensures the Einstein equation is implied in the background.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| NEC | R_MN l^M l^N >= 0, g_MN l^M l^N = 0 | Eq. 1 |
| SEC | R_MN t^M t^N >= 0, t^2 < 0 | Eq. 2 |
| FRW metric | ds^2 = -dt^2 + a^2(t) delta_ij dx^i dx^j | Eq. 3 |
| Acceleration | a_dotdot/a = H_dot + H^2 > 0 | Eq. 4 |
| Null Raychaudhuri | d theta/d lambda = -theta^2/(D-2) - sigma^2 - R_MN l^M l^N | Eq. 7 |
| Warped product | ds^2 = e^{-2A} g_mu_nu dx^mu dx^nu + e^{2A} g_mn dy^m dy^n | Eq. 11 |
| Conformal form | ds^2 = Omega^2 [g_tilde_{mu nu} dx^mu dx^nu + h_tilde_mn dy^m dy^n] | Eq. 12 |
| External Ricci | R^{(D)}_mu_nu = R^{(d)}_mu_nu(g_tilde) - g_tilde_mu_nu [nabla^2 ln Omega + (D-2)(nabla ln Omega)^2] | Eq. 13 |
| Trace constraint | [1/(D-2)] nabla^2 Omega^{D-2}/Omega^{D-2} = R^{(d)} + Omega^2(-T^mu_mu + [d/(D-2)] T^M_M) | Eq. 15 |
| Positive R^{(d)} | (D - d - 2) T^mu_mu > d T^m_m | Eq. 16 |
| R_00 form | R^{(D)}_00 = -(d-1)(H_dot + H^2) + [Omega^{-(D-2)}/(D-2)] nabla^2 Omega^{(D-2)} | Eq. 17 |
| Integrated GMN | (d-1)(G_D/G_d)(H_dot + H^2) = -integral d^n y_tilde sqrt(h_tilde) Omega^{(D-2)} R^{(D)}_00 | Eq. 18 |
| SEC violation | integral d^n y_tilde sqrt(h_tilde) Omega^{D-2} R^{(D)}_00 < 0 | Eq. 19 |
| Affine null vector | N^M = (1/Omega^2)(1, 0, 0, 0, n_tilde^m) | Eq. 21 |
| Conformal R_mn | R^{(D)}_mn = R_tilde^{(n)}_mn - h_tilde_mn [(D-2) partial_p ln Omega partial^p ln Omega + box ln Omega] + (D-2) partial_m(ln Omega) partial_n(ln Omega) - nabla_m partial_n(ln Omega) | Eq. 30 |
| Main Raychaudhuri result | 3(H^2 + H_dot)(G_D/G_d) = -integral d^n y_tilde sqrt(h_tilde) Omega^{D-2} R^{(D)}_00 | Eq. 33 |
| Averaged SEC violation | integral d^n y_tilde sqrt(h_tilde) Omega^{D-2} R^{(D)}_00 < 0 | Eq. 34 |

## Relevance to Phonon-Exflation

This paper is directly on-target for the framework's NEC audit. The phonon-exflation framework models reality as M4 x SU(3) with a Jensen-deformed internal fiber, and transit through tau ~ 0.19 generates the observed acceleration. Faruk's derivation establishes that if the internal compact space is **static** (time-independent h_mn and time-independent warp factor Omega), then any accelerating FRW external factor forces the higher-dimensional SEC to be violated in the averaged sense — but only the SEC, not the NEC. This is important because the framework's DNP crossing at tau ~ 0.285 is expected to produce NEC violation, which Faruk shows is **not** forced by the Raychaudhuri equation alone when the internal geometry is static. The framework escapes such no-gos by making the internal SU(3) fiber **dynamical** in tau, so the static-compactification assumptions of GMN/Faruk do not apply; this is the same escape hatch identified in the Russo-Townsend 2019 paper (arXiv:1904.11967) that is separately catalogued in this library. Faruk's clean Raychaudhuri derivation is therefore the cleanest statement of the wall that the substrate picture must cross, and his explicit dependence on the static-internal assumption (manifested as Omega = Omega(y^m) only, not Omega(y^m; t)) pinpoints exactly where the Jensen-deformation escape acts.
