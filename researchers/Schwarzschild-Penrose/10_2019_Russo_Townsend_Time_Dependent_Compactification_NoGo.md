# Time-dependent compactification to de Sitter space: a no-go theorem

**Author(s):** J. G. Russo (ICREA and Departament de Fisica Cuantica i Astrofisica, Universitat de Barcelona) and P. K. Townsend (Department of Applied Mathematics and Theoretical Physics, University of Cambridge)
**Year:** 2019 (v3 posted 17 Aug 2021)
**Journal:** JHEP (arXiv preprint in this version)
**arXiv:** 1904.11967
**Relevance:** CRITICAL

**NOTE on filename.** The filename "Saha_Sahoo_Sen" was specified by the batch instructions but the actual authors are Russo and Townsend. Filename retained as assigned; citation is accurate to the PDF.

---

## Abstract

It is known that the Einstein gravitational field equations in D > 4 spacetime dimensions have no time-independent non-singular compactification solutions to de Sitter space if the D-dimensional stress tensor satisfies the Strong Energy Condition (SEC). Here we show, by example, that the SEC alone does not exclude time-dependent non-singular compactifications to de Sitter space, in Einstein conformal frame. However, this possibility is excluded by the combined SEC and Null Energy Condition (NEC) because the NEC forces a time-evolution towards a singular D-metric.

(In the published version the dominant energy condition (DEC) was stated as the premise but only the weaker NEC was actually used — see "Note Added" at the end of the paper.)

---

## Key Arguments and Derivations

**Section 1: Introduction.** The observed accelerated expansion of the Universe is consistent with a de Sitter phase, which creates tension with string/M-theory because its low-energy effective supergravity in 10/11 dimensions does not admit time-independent dS compactifications. The Gibbons-Maldacena-Nunez (GMN) no-go theorem rules this out when the higher-dimensional stress tensor satisfies the SEC. Two possible escape routes: (a) allow innocuous singularities (KKLT); (b) allow time-dependence of the compact space metric. This paper explores (b) and shows that the Einstein-frame condition (an integral over the compact space) has typically been implemented in an **unaveraged** form that is sufficient but not necessary. The unaveraged form is what produces the strong GMN result; using only the true averaged form, the SEC does **not** rule out time-dependent dS compactifications. Counter-example exhibited. However, the counter-example violates the DEC, and the paper proves that the DEC (and in fact only the weaker NEC) rules out **any** non-singular dS compactification with strictly time-dependent compact metric, because the NEC forces evolution toward a singular D-metric.

**Section 2: Warped cosmological compactifications.** The D-dimensional metric ansatz for compactification to a general FLRW spacetime of dimension d < D:

  ds_FLRW^2 ≡ g_mu_nu dx^mu dx^nu = -dt^2 + S^2(t) g_bar_ij dx^i dx^j     (Eq. 2.1)

with S(t) = e^{H t} for flat slicing k = 0 (Eq. 2.2). The D-metric:

  ds_D^2 = Omega^2(y; t) ds_FLRW^2 + h_alpha_beta(y; t) dy^alpha dy^beta     (Eq. 2.3)

Einstein-frame condition:

  integral_B d^n y sqrt(det h) Omega^{d-2} = G_D/G_d     (Eq. 2.4)

Taking a time derivative:

  0 = integral_B d^n y sqrt(det h) Omega^{d-2} X ≡ <X>     (Eq. 2.5)

with

  X = (1/2) tr(h^{-1} h_dot) + (d-2)(Omega_dot/Omega)     (Eq. 2.6)

This is the **first-order Einstein-frame condition** <X> = 0. Although X ≡ 0 suffices, it is not required; this is the crucial observation that gives the new counter-example. Computing R_00 from (2.3):

  R_00 = -(d-1)[(S_dotdot/S) + (Omega_dotdot/Omega) - (Omega_dot/Omega)^2 + (Omega_dot/Omega)(S_dot/S)]
         - (1/2) tr(h^{-1} h_dotdot) + (1/2)(Omega_dot/Omega) tr(h^{-1} h_dot) + (1/4) tr(h^{-1} h_dot)^2
         + (d-1) |nabla Omega|^2 + Omega nabla^2 Omega     (Eq. 2.8)

For time-independent h (and time-independent Omega as demanded by the unaveraged Einstein-frame condition X ≡ 0), R_00 >= 0 becomes

  d(d-1) sqrt(det h) Omega^{d-2} (S_dotdot/S) <= sqrt(det h) nabla^2 Omega^d     (Eq. 2.9)

Integration over B yields S_dotdot <= 0, which excludes accelerated expansion and hence a dS universe. This is essentially the GMN theorem.

**Section 3: A time-dependent de Sitter compactification.** 5D counter-example:

  ds_5^2 = Omega^2(t + y) ds_dS^2 + phi^2(t + y) dy^2, y ~ y + 2 pi L     (Eq. 3.1)

The compact space is topologically a circle. With flat-slicing dS (k = 0), R_00 is given by (Eq. 3.2). The Einstein-frame condition becomes integral_0^{2 pi L} dy phi(t+y) Omega^2(t+y) = G_5/G_4 (Eq. 3.3), which is time-independent due to periodicity. The first-order Einstein-frame condition <X> = 0 holds even though X ≠ 0. Choose

  Omega = 2 A [1 + a sin((t+y)/L)], phi = A [1 + 2 a sin((t+y)/L)]     (Eq. 3.4)

For a = 0, R_00 = -3 H^2 < 0 (SEC violated). For a ≠ 0, R_00 is periodic in t + y; for appropriate a and LH, R_00 > 0 over one period. Example: a = 1/5, LH = 0.1 works (figure in paper). Similar examples exist for toroidal compactification from any D > 4. Hence **the SEC alone does not forbid time-dependent compactification to de Sitter space**. But: the 5D stress tensor supporting this SEC-compliant solution violates the DEC.

**Section 4: The DEC and a no-go theorem.** The d x d block of the Einstein tensor matches a perfect-fluid T_mu_nu: T_00 = -rho g_00, T_ij = P g_ij (Eq. 4.1). The DEC requires rho >= |P|, i.e. rho ± P >= 0. Computing these combinations (Eqs. 4.2):

  rho - P = (d-2)(S_dotdot/S) + (d-2)^2 (S_dot/S)^2 + (2d-3)(S_dot/S) X + X_dot + X^2
             - (d-1)[2 Omega nabla^2 Omega + (d-2) |nabla Omega|^2] + R(h) + (d-2)^2 (k/S^2)
  rho + P = -(d-2)(S_dotdot/S) + (d-2)(S_dot/S)^2 + (S_dot/S) X - X_dot + (1/(d-2)) X^2
             - (1/(4(d-2))) [tr(h^{-1} h_dot)]^2 - (1/4) tr[(h^{-1} h_dot)^2] + (d-2) k/S^2

Note: rho + P has **no** term involving nabla Omega or R(h). The time-derivative of X has the property <X_dot> = -<X^2> (Eq. 4.3). For flat-slicing dS, the DEC inequality rho + P >= 0 becomes

  -X_dot + H X + (1/(d-2)) X^2 >= (1/(4(d-2))) [tr(h^{-1} h_dot)]^2 + (1/4) tr[(h^{-1} h_dot)^2]     (Eq. 4.4)

The LHS vanishes if X ≡ 0. Then (4.4) can only hold if h is time-independent — but then the compactification is time-independent and the SEC rules out dS (GMN).

When X ≠ 0, <X> = 0 forces X to take both positive and negative values on B. In the example of Section 3, X has at least two zeros per period and X_dot is negative at one zero and positive at another. At the latter, X = 0 and X_dot > 0, which makes the LHS of (4.4) negative — contradicting DEC. So the Section-3 example violates DEC.

**General argument.** At any given time t_0, B partitions into B_- ∪ B_0 ∪ B_+ (Eq. 4.5) according to the sign of X. Assume the compact space metric is strictly time-dependent. Then the strict inequality

  -(d-2) X_dot + (d-2) H X + X^2 > 0     (Eq. 4.6)

holds. From (4.6) on B_0 we get X_dot < 0. All points in B_0 at time t_0 > T migrate to B_- at time t_0 + dt. By continuity, points near the boundary of B_0 that were in B_+ migrate to B_0 ∪ B_-. Thus there is a flow from B_+ to B_0 ∪ B_-, and the volume of B_+ decreases monotonically. Since <X> = 0 always, a delta-function singularity of X must develop if vol(B_+) shrinks to zero, inevitable unless X_dot -> 0 on B_0, which requires h_dot -> 0. If h_dot -> 0, either the D-metric evolves to X ≡ 0 (which needs Omega_dot -> 0 and gives a time-independent dS compactification — excluded by SEC), or X ≠ 0 but h is time-independent with time-dependent warp factor. In the latter case X = (d-2) Omega_dot/Omega, and (4.4) becomes -(d-2) X_dot + (d-2) H X + X^2 >= 0. On B_0 (where X = 0), X_dot <= 0; near B_0, -X_dot - H epsilon + O(epsilon^2) >= 0 (Eq. 4.8) forces X_dot < 0 in this region, and the boundary between B_- and B_0 shrinks to zero, leading to a discontinuity of X and hence a singular D-metric (reached in finite time or asymptotically).

**Section 5: Summary.** If the SEC holds in D > 4 dimensions (as it does for effective supergravity theories of string/M-theory), the GMN theorem rules out time-**independent** dS compactifications. The combined SEC and NEC (here the NEC is the weakened form of DEC that is actually needed; see Note Added) rule out time-**dependent** non-singular dS compactifications too, because the NEC forces evolution toward a singular D-metric. Together, these results imply that non-singular dS compactifications are excluded by SEC + NEC combined, whether time-independent or time-dependent. This cannot be derived from either alone: positive Lambda violates SEC and permits dS compactification; the Section 3 example satisfies SEC and permits dS but violates NEC.

**Note Added: DEC vs NEC.** The published version stated DEC; the proof only used NEC. NEC for the stress-energy tensor T_MN requires T_MN n^M n^N >= 0 for null D-vectors. Choosing n^M partial_M = partial_t + n^i partial_i with g_ij n^i n^j = 1, NEC reduces to rho + P >= 0, which is implied by DEC but strictly weaker. The no-go proof in Section 4 uses only this weaker NEC condition (in addition to SEC). Energy conditions needed: **SEC + NEC**.

## Key Results

1. **Section 3 counter-example** (Eqs. 3.1-3.4): 5D time-dependent dS compactification on a circle that satisfies the higher-dimensional SEC for appropriate choice of parameters (a = 1/5, LH = 0.1 works). This shows that SEC alone does **not** forbid time-dependent dS compactification.
2. **Einstein-frame condition is an integral**, not a pointwise constraint. Only the **first-order** version <X> = 0 (Eq. 2.5) is truly required; the unaveraged X ≡ 0 is sufficient but unnecessarily restrictive. Previous GMN-type arguments implicitly used X ≡ 0.
3. **Main no-go result**: combined SEC and NEC (originally stated as DEC) rule out all non-singular dS compactifications in D > 4, whether time-independent or strictly time-dependent. For strictly time-dependent h, the NEC forces a flow on B that shrinks vol(B_+) to zero and creates a delta-function singularity of X, signalling a singular D-metric.
4. **Residual case**: if h becomes time-independent with time-dependent warp factor only, the inequality (4.7) on B_0 leads to X_dot <= 0 and, via the limit X = -epsilon near B_0, the boundary between B_- and B_0 shrinks to zero — producing a discontinuous X and hence (asymptotically or at finite time) a singular D-metric.
5. **Joint implication with GMN**: excluding SEC violation, non-singular dS compactifications require either NEC violation or an ultra-violet completion of higher-dimensional GR.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| FLRW metric | ds_FLRW^2 = -dt^2 + S^2(t) g_bar_ij dx^i dx^j | Eq. 2.1 |
| dS scale factor (k=0) | S = e^{H t} | Eq. 2.2 |
| D-metric ansatz | ds_D^2 = Omega^2(y; t) ds_FLRW^2 + h_alpha_beta(y; t) dy^alpha dy^beta | Eq. 2.3 |
| Einstein-frame condition | integral_B d^n y sqrt(det h) Omega^{d-2} = G_D/G_d | Eq. 2.4 |
| First-order EF condition | <X> = 0 | Eq. 2.5 |
| X definition | X = (1/2) tr(h^{-1} h_dot) + (d-2)(Omega_dot/Omega) | Eq. 2.6 |
| R_00 formula | R_00 = -(d-1)[...] - (1/2) tr(h^{-1} h_dotdot) + ... | Eq. 2.8 |
| Unaveraged GMN | d(d-1) sqrt(det h) Omega^{d-2}(S_dotdot/S) <= sqrt(det h) nabla^2 Omega^d | Eq. 2.9 |
| 5D metric (Section 3) | ds_5^2 = Omega^2(t+y) ds_dS^2 + phi^2(t+y) dy^2 | Eq. 3.1 |
| 5D R_00 | [formula involving H, phi, Omega, etc.] | Eq. 3.2 |
| Specific example | Omega = 2A[1 + a sin((t+y)/L)], phi = A[1 + 2a sin((t+y)/L)] | Eq. 3.4 |
| rho - P | (d-2)(S_dotdot/S) + (d-2)^2(S_dot/S)^2 + (2d-3)(S_dot/S) X + X_dot + X^2 - ... + R(h) | Eq. 4.2 |
| rho + P | -(d-2)(S_dotdot/S) + (d-2)(S_dot/S)^2 + (S_dot/S) X - X_dot + X^2/(d-2) - ... | Eq. 4.2 |
| Identity | <X_dot> = -<X^2> | Eq. 4.3 |
| DEC/NEC inequality (dS) | -X_dot + H X + X^2/(d-2) >= (1/(4(d-2)))[tr(h^{-1} h_dot)]^2 + (1/4) tr[(h^{-1} h_dot)^2] | Eq. 4.4 |
| Strict DEC/NEC (h time-dep) | -(d-2) X_dot + (d-2) H X + X^2 > 0 | Eq. 4.6 |
| Warp-factor-only DEC | -(d-2) X_dot + (d-2) H X + X^2 >= 0 | Eq. 4.7 |
| Near-B_0 limit | -X_dot - H epsilon + O(epsilon^2) >= 0 | Eq. 4.8 |

## Relevance to Phonon-Exflation

This paper is a **direct** no-go for one of the most natural framework escape routes. The phonon-exflation framework postulates M4 x SU(3) with a Jensen-deformed internal SU(3) fiber, and the driving role of the tau deformation means the internal geometry is **dynamical** (not static) during the cosmogenetic transit. Russo-Townsend show that dynamical-internal compactification to de Sitter is **not** freely available: the NEC (or equivalently DEC, originally stated) forces evolution toward a singular D-metric if the internal metric is strictly time-dependent. This is the key no-go that the framework's NEC audit must engage. Three comments: (1) the framework's NEC violation at the DNP crossing tau ~ 0.285 is **precisely** what is needed to escape the Russo-Townsend no-go, because Russo-Townsend relies on NEC holding; the framework's NEC violation is a predicted, specific, localized feature. (2) The GMN-type unaveraged X ≡ 0 assumption that underlies most older no-gos is distinguished from the true integrated Einstein-frame condition <X> = 0; the framework's "dump point" spectral-action treatment is implicitly a statement about averaged rather than pointwise behavior. (3) The Section 3 counter-example — a time-dependent dS compactification on a circle satisfying SEC but violating NEC — is of the same architectural class as what the framework must realize at the fold: the emergent-M4 description is dS-like, the internal SU(3) "circle" is periodically/dynamically deformed, and NEC violation at the DNP crossing is the mechanism that makes the configuration consistent with dynamical compactification. The framework's "block-diagonality theorem for D_K = analog of Birkhoff rigidity" plays the role of the "strict time-dependence" assumption — if D_K blocks are time-dependent (under tau-flow), then a flow on B_+ ∪ B_0 ∪ B_- is induced, and the framework's prediction that NEC is violated at the DNP crossing is exactly the permission slip that keeps this flow from producing the singular D-metric Russo-Townsend construct in the SEC-only counter-example. This paper therefore codifies the external wall that the framework claims to pass by dynamical internal geometry plus localized NEC violation.
