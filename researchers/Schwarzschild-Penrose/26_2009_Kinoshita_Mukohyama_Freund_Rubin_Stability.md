# Thermodynamic and dynamical stability of Freund–Rubin compactification

**Author(s):** Shunichiro Kinoshita, Shinji Mukohyama
**Year:** 2009
**Journal:** arXiv preprint (UTAP-611, RESCEU-7/09, IPMU-09-0031)
**arXiv:** 0903.4782
**Relevance:** HIGH
**Fills gap**: SP-geometer agent's 2026-03-13 request for "exact solutions where higher-D dS nucleates lower-dimensional regions, with Penrose diagrams" (the original request mis-cited this as Brown-Dahlen 0904.3915 — that ID is a biostatistics paper; the actual paper SP wanted is Carroll-Johnson-Randall 0904.3115). This companion paper addresses the stability of the product-compactification endpoints of that nucleation process.

---

## Abstract

We investigate stability of two branches of Freund–Rubin compactification from thermodynamic and dynamical perspectives. Freund–Rubin compactification allows not only trivial solutions but also warped solutions describing warped product of external de Sitter space and internal deformed sphere. We study dynamical stability by analyzing linear perturbations around solutions in each branch. Also we study thermodynamic stability based on de Sitter entropy. We show complete agreement of thermodynamic and dynamical stabilities of this system. Finally, we interpret the results in terms of effective energy density in the four-dimensional Einstein frame and discuss cosmological implications.

---

## Key Arguments and Derivations

**Setup — Freund-Rubin compactification with bulk cosmological constant.** The (p+q)-dimensional action is I = (1/(16 pi)) ∫ d^{p+q} x sqrt(-g) [R − 2 Lambda − (1/q!) F_{(q)}^2], where Lambda is a bulk cosmological constant and F_{(q)} is a q-form flux threading the internal q-sphere. The Einstein equation and Maxwell equation admit two classes of solutions.

**Freund-Rubin (FR) branch — unwarped solutions.** The metric is the direct product ds^2 = −dt^2 + e^{2ht} dx_{p-1}^2 + rho^2 dOmega_q^2 with a constant flux F_{(q)} = b epsilon_{mu_1 ... mu_q}. The field equations relate b, h and rho via (p−1)(p+q−2) h^2 + (q−1) b^2 = 2 Lambda and (q−1)^2 rho^{-2} + (p−1)^2 h^2 = 2 Lambda, giving a one-parameter family of solutions.

**Warped branch — deformed-sphere solutions.** A separate one-parameter family is described by the warped ansatz ds^2 = e^{2 phi(r)} [−dt^2 + e^{2ht} dx_{p-1}^2] + e^{-2 p phi / (q-2)} [dr^2 + a^2(r) dOmega_{q-1}^2] with the q-form flux F_{(q)} = b e^{-2 p (q-1) phi / (q-2)} a^{q-1} dr ∧ dOmega_{q-1}. The Einstein equations reduce to two coupled ODEs for a(r) and phi(r) plus a constraint equation, and the boundary conditions |a'(r_±)| = 1 and phi'(r_±) = 0 enforce regularity at the poles of the internal space (which has spherical topology but is deformed for nonzero phi(r)). The two branches intersect at a single point where the warped solution becomes unwarped and reduces to an FR solution; at that intersection the FR solution is marginally stable to the l = 2 perturbation. For b^2 below the intersection value the internal space is prolate; above, it is oblate.

**Prior FR instability structure.** FR solutions are known to have two classes of dynamical instability: the **l = 0 (radion/volume modulus) mode** which becomes tachyonic when h is too large (small flux density) — this arises already at q = 2; and the **l ≥ 2 modes** (quadrupole and higher) which become tachyonic when h is too small (large flux density) and require q ≥ 4. For q ≥ 4, the two instability regions overlap so that no FR solution is stable on both ends.

**Section III — Dynamical stability via linear perturbations.** Kinoshita-Mukohyama write the perturbed (p+q)-metric in scalar gauge with two y-dependent functions Pi(y) and Omega(y) plus a scalar harmonic Y(x) on the p-dim de Sitter external space. Linearizing the Einstein + Maxwell equations produces two coupled ODEs for Pi and Omega with eigenvalue mu^2 (the KK mass squared defined by grad^2 Y = mu^2 Y) and boundary conditions (p+q-2) Pi − q Omega = Omega' = 0 at the poles B = 0 of the internal space. For the unwarped FR solution, the system reduces to a single fourth-order equation for Pi, and expanding Pi in sphere harmonics gives the closed-form mass spectrum mu_±^2 = lambda + ((q-1)(p-2)/(p+q-2)) b^2 − (p-1) h^2 ± sqrt{[((q-1)(p-2)/(p+q-2)) b^2 − (p-1) h^2]^2 + (4 (q-1)(p-1)/(p+q-2)) b^2 lambda} with lambda = l (l + q - 1) rho^{-2}. The critical Hubble rates below/above which the FR branch becomes unstable are h_{c(l=0)}^2 = 2 Lambda (p-2) / ((p-1)^2 (p+q-2)) (l = 0 radion instability for h > h_{c(l=0)}) and h_{c(l=2)}^2 = 2 Lambda [(p-1) q^2 − (3p-1) q + 2] / (q (q-3) (p-1)^2 (p+q-2)) (l = 2 shape instability for h < h_{c(l=2)}).

**Numerical spectrum for p = q = 4.** For the warped branch, the eigenvalue problem cannot be solved in closed form and is tackled numerically. Figure 2 of the paper shows the KK mass spectrum for the l = 0, 1, 2±, 3± modes. The crucial finding: in the low-Hubble regime h^2 < h_{c(l=2)}^2 = Lambda/18 where the FR l = 2− mode is tachyonic, the warped-branch l = 2− mode has positive mu^2 — the warped branch is dynamically **stable** precisely where the FR branch is dynamically **unstable**, and vice versa. The l = 2− mode of the warped branch intersects zero at exactly the critical h^2 where the two branches merge. Kinoshita-Mukohyama interpret this as: deformation of the internal space and warping stabilize the tachyonic shape modulus by the condensation of the modulus itself.

**Section IV — Thermodynamic stability via de Sitter entropy.** The de Sitter entropy is defined as S = A/4 where A is the total area of the de Sitter horizon integrated over the internal space: S = (Omega_{p-2} Omega_{q-1} / (4 h^{p-2})) ∫_{r_-}^{r_+} dr e^{-2(p+q-2) phi / (q-2)} a^{q-1}. The total flux is a conserved quantity Phi = b Omega_{q-1} ∫_{r_-}^{r_+} dr e^{-2 p (q-1) phi / (q-2)} a^{q-1}. Kinoshita-Mukohyama evaluate the on-shell Euclidean action (assuming SO(p+1) × SO(q) isometry) and show I_{Euclid} = −S. By computing the first variation of I_{Euclid} with respect to the fields a(r), phi(r), psi(r) (where psi is the form-field potential), only the boundary term survives because of the equations of motion, and this yields the **first law of de Sitter thermodynamics for Freund-Rubin compactifications**: dS = −(Omega_{p-2} b / (4 (p-1) h^p)) dPhi (Eq. 1/Eq. 41). The entropy is therefore a thermodynamic potential with respect to Phi as the natural variable; for fixed Phi the higher-entropy configuration is thermodynamically favored. Extending to variable Lambda by dimensional scaling, a generalized first law dS = −(Omega_{p-2} b / (4(p-1) h^p)) dPhi − [(p+q-2)/2 · S + (q-1)/2 · (Omega_{p-2} b / (4(p-1) h^p)) Phi] dLambda/Lambda also holds.

**FR branch has two sub-branches.** Substituting a(r) = rho sin(r/rho) and phi = 0 gives S = Omega_{p-2} Omega_q rho^q / (4 h^{p-2}) and Phi = b Omega_q rho^q in the FR branch. S(Phi) turns out to be a double-valued function of Phi, splitting into a lower-entropy sub-branch and a higher-entropy sub-branch joined at a single critical point where dPhi/dh = dS/dh = 0. Solving this gives h_{c(l=0)}^2 = 2 Lambda (p-2) / ((p-1)^2 (p+q-2)) — **identical** to the dynamical l = 0 instability threshold. So the thermodynamically unfavorable FR sub-branch coincides exactly with the dynamically l = 0-unstable sub-branch.

**FR vs warped entropy comparison (p = q = 4).** Numerically comparing S_{FR} and S_w for a grid of total flux values, Kinoshita-Mukohyama find that S_w − S_{FR} changes sign at Phi = 32 sqrt(3) pi^2 Lambda^{-3/2}, equivalent to h^2 = Lambda / 18. For h^2 < Lambda/18 the warped branch has larger entropy; for h^2 > Lambda/18 the FR branch does. The critical value h^2 = Lambda/18 coincides exactly with the dynamical l = 2 instability threshold h_{c(l=2)}^2 for p = q = 4. This gives the main result of the paper: **complete agreement between thermodynamic and dynamical stability** for both the FR-vs-warped comparison and the two FR sub-branches.

**Section V — Cosmological implications in the 4D Einstein frame.** For general warping A^2(x, y), the 4D effective theory is Einstein frame with conformal factor Omega^2 = (M_{4+q}^{2+q} / M_4^2) ∫ d^q y sqrt(q) A^2 relating gauge-dependent to gauge-invariant metrics. The 4D Einstein-frame Hubble rate is h_E = Omega^{-1} h and the effective de Sitter entropy S_E equals the integrated horizon entropy S (Eq. 55). The Einstein-frame energy density rho_E = 3 M_4^4 h^2 (M_{4+q}^{2+q})^{-1} (∫ d^q y sqrt(q) A^2)^{-1} satisfies rho_E / (3 M_4^4) = 8 pi^2 / S, so lower rho_E corresponds to higher entropy. **Dynamically stable branches always have lower rho_E**, which strongly suggests evolution from unstable to stable configurations at fixed Phi. If Lambda is dynamical (e.g., sourced by a slowly rolling scalar field), as Lambda decreases h likewise decreases and eventually crosses the critical value h_{c(l=2)}; at that point the stable and unstable branches merge, and below it the warped branch takes over. This is a **second-order phase transition between unwarped and warped compactifications**, analogous to the end of hybrid inflation, and the authors suggest it provides a new mechanism for inflation in higher-dimensional theories.

**Section VI — Discussion and Gubser-Mitra correspondence.** The complete agreement between thermodynamic and dynamical stability for Freund-Rubin compactifications is the first explicit confirmation of the Gubser-Mitra correlated-stability conjecture outside the black-brane/string context. The Jeans-instability interpretation is that high internal flux density (small external Hubble rate) analogously destabilizes the internal manifold against long-wavelength deformations, with the warped branch playing the role of the deformed structure.

## Key Results

1. **Two distinct one-parameter families** of Freund-Rubin compactification solutions exist for given (p, q, Lambda): the unwarped FR branch (direct product dS_p × S^q) and the warped branch (warped product of dS_p with a deformed q-sphere).
2. **The two branches intersect at a single point** where the warped solution becomes unwarped and reduces to a marginally-stable FR solution with respect to the l = 2 (shape) perturbation.
3. **Dynamical l = 2 instability threshold**: h_{c(l=2)}^2 = 2 Lambda [(p-1) q^2 − (3p-1) q + 2] / (q (q-3) (p-1)^2 (p+q-2)), requiring q ≥ 4.
4. **Dynamical l = 0 instability threshold**: h_{c(l=0)}^2 = 2 Lambda (p-2) / ((p-1)^2 (p+q-2)), present already for q = 2.
5. **First law of de Sitter thermodynamics**: dS = −(Omega_{p-2} b / (4(p-1) h^p)) dPhi, derived from the first variation of the Euclidean action using I_{Euclid} = −S.
6. **FR branch is double-valued in S(Phi)**, splitting into a thermodynamically favored (higher-entropy) sub-branch and an unfavored (lower-entropy) sub-branch. The split occurs exactly at h_{c(l=0)}, matching the dynamical l = 0 instability boundary.
7. **Warped branch is thermodynamically favored over FR for h^2 < Lambda/18** (for p = q = 4); FR is favored for h^2 > Lambda/18. The critical value coincides with h_{c(l=2)}.
8. **Complete agreement between thermodynamic and dynamical stability** — stable branches have larger entropy, unstable branches have smaller entropy, in both the FR-vs-warped and the two-FR-sub-branch comparisons. This extends the Gubser-Mitra correlated-stability conjecture from black branes to de Sitter flux compactifications.
9. **In the 4D Einstein frame**, S_E = S and rho_E / (3 M_4^4) = 8 pi^2 / S, so dynamically stable configurations always have lower effective energy density — suggesting natural dynamical evolution from unstable toward stable branches at fixed total flux.
10. **Second-order phase transition** between unwarped and warped compactifications as Lambda (and hence h) decreases through the critical value, proposed as a novel mechanism for higher-dimensional hybrid inflation.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Action | I = (1/(16 pi)) ∫ d^{p+q} x sqrt(-g) [R − 2 Lambda − (1/q!) F_{(q)}^2] | Eq. 2 |
| FR metric | ds^2 = −dt^2 + e^{2 h t} dx_{p-1}^2 + rho^2 dOmega_q^2 | Eq. 5 |
| FR flux | F_{(q)} = b epsilon_{mu_1 ... mu_q} | Eq. 6 |
| FR constraints | (p−1)(p+q−2) h^2 + (q−1) b^2 = 2 Lambda; (q−1)^2 rho^{-2} + (p−1)^2 h^2 = 2 Lambda | Eqs. 7–8 |
| Warped metric | ds^2 = e^{2 phi(r)} [−dt^2 + e^{2 h t} dx_{p-1}^2] + e^{-2 p phi / (q-2)} [dr^2 + a^2(r) dOmega_{q-1}^2] | Eq. 9 |
| Warped flux | F_{(q)} = b e^{-2 p (q-1) phi / (q-2)} a^{q-1} dr ∧ dOmega_{q-1} | Eq. 10 |
| Warped boundary conditions | |a'(r_±)| = 1, phi'(r_±) = 0 at a(r_±) = 0 | Eq. 13 |
| FR mass spectrum | mu_±^2 = lambda + ((q-1)(p-2)/(p+q-2)) b^2 − (p-1) h^2 ± sqrt{[((q-1)(p-2)/(p+q-2)) b^2 − (p-1) h^2]^2 + (4 (q-1)(p-1)/(p+q-2)) b^2 lambda}, lambda = l(l+q-1) rho^{-2} | Eq. 25 |
| l = 0 critical Hubble | h_{c(l=0)}^2 = 2 Lambda (p-2) / ((p-1)^2 (p+q-2)) | Eq. 26 |
| l = 2 critical Hubble | h_{c(l=2)}^2 = 2 Lambda [(p-1) q^2 − (3p-1) q + 2] / (q (q-3) (p-1)^2 (p+q-2)) | Eq. 27 |
| de Sitter entropy | S = A/4 = (Omega_{p-2} Omega_{q-1} / (4 h^{p-2})) ∫_{r_-}^{r_+} dr e^{-2(p+q-2) phi/(q-2)} a^{q-1} | Eq. 28 |
| Total flux | Phi = b Omega_{q-1} ∫_{r_-}^{r_+} dr e^{-2 p (q-1) phi/(q-2)} a^{q-1} | Eq. 29 |
| First law | dS = −(Omega_{p-2} b / (4 (p-1) h^p)) dPhi | Eq. 1, 41 |
| Euclidean action = entropy | I_{Euclid} = −S on shell | Eq. 36, B4 |
| Generalized first law | dS = −(Omega_{p-2} b / (4(p-1) h^p)) dPhi − [(p+q-2)/2 · S + (q-1)/2 · (Omega_{p-2} b / (4(p-1) h^p)) Phi] dLambda/Lambda | Eq. 44 |
| 4D Einstein-frame conformal factor | Omega^2 = (M_{4+q}^{2+q} / M_4^2) ∫ d^q y sqrt(q) A^2 | Eq. 50 |
| Einstein-frame entropy | S_E = 8 pi^2 M_4^2 h_E^{-2} = S | Eqs. 54–55 |
| Einstein-frame energy density | rho_E / (3 M_4^4) = 8 pi^2 / S | Eq. 57 |

## Relevance to Phonon-Exflation

Kinoshita-Mukohyama provides the stability-analysis companion to Carroll-Johnson-Randall and is directly relevant to two open questions in the phonon-exflation framework. First, the existence of a **warped-sphere branch** (deformed internal geometry with lower SO(q) symmetry than the unwarped SO(q+1)) as a classical endpoint of Freund-Rubin compactification is the exact classical analog of the **Jensen-deformed SU(3) fiber** in the framework. The warped branch is described by a second-order ODE for the warp factor phi(r) with pole-regularity boundary conditions — mathematically parallel to the Dirac operator D_K acting on the Jensen-deformed fiber and picking out eigenmodes consistent with pole regularity. Second, the central result that **thermodynamic and dynamical stability coincide** and that the warped branch is favored in the low-Hubble (high flux density) regime is directly relevant to the framework's question of what structure the internal SU(3) fiber should adopt post-fold: an unwarped (symmetric) sphere is unstable below the threshold, while a deformed (warped) internal geometry is the stable endpoint. This parallels the framework's claim that the symmetric pre-fold SU(3) is an unstable maximum and the Jensen-deformed post-fold SU(3) is the stable configuration. Third, the proposed **second-order phase transition** between unwarped and warped compactifications as Lambda (or equivalently h) decreases through the critical value is a classical gravitational mirror of the phonon-exflation first-order transit through tau ~ 0.19 — the direction of flow (symmetric → deformed) and the identification of the transition with inflation-like physics align with the framework's "transit physics, not equilibrium" paradigm. Finally, the I_{Euclid} = −S identity and the first law dS = −(Omega_{p-2} b / (4(p-1) h^p)) dPhi give a clean template for how flux quantization and bulk entropy should be related in the framework's spectral-action accounting, where the internal-geometry flux plays the role of Q/Phi and the a_0 spectral moment plays the role of Lambda.
