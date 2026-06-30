# Richardson-Gaudin models and broken integrability

**Author(s):** Pieter W. Claeys (supervisors: D. Van Neck, S. De Baerdemacker)
**Year:** 2018 (PhD Dissertation, Ghent University)
**Journal:** Ghent University PhD Thesis (174 pages)
**arXiv/DOI:** arXiv:1809.04447v1
**Relevance:** CRITICAL

---

## Abstract

PhD thesis reviewing and extending Richardson-Gaudin (RG) integrable models, developing eigenvalue-based frameworks for numerical solution, inner products, and form factors, and extending the formalism to broken-integrability settings (central spin model with external fields, periodically-driven Heisenberg chains, Floquet resonances, variational integrability-breaking methods). Compilation of 12 published papers (2015–2018) into a unified thesis.

---

## Key Arguments and Derivations

**Part I: Richardson-Gaudin models**

**Chapter 2 (RG integrability).** Classical integrability (Liouville-Arnol'd, 2.1.1) vs quantum integrability (2.1.2). Quantum integrability requires non-trivial structure — naive "L commuting charges" trivially satisfied by spectral projectors. Structure imposed via non-ergodicity: conserved charges scaling extensively with system size, producing Poissonian (vs Wigner-Dyson) level statistics.

Construction of RG models from non-interacting su(2) spin chain $H = \sum_i \omega_i S^z_i/2$ with trivial conserved charges $Q_i = S^z_i$. Interactions introduced via:
$Q_i = S^z_i + g\sum_{j\ne i}[X_{ij}(S^+_i S^-_j + S^-_i S^+_j) + Z_{ij}S^z_i S^z_j]$ (Eq. 2.12).

**Gaudin equations:** $X_{ij} + X_{ji} = 0$, $Z_{ij} + Z_{ji} = 0$ (Eq. 2.13); $X_{ij}X_{jk} - X_{ik}(Z_{ij}+Z_{jk}) = 0$ (Eq. 2.14). Three Gaudin solution classes: rational, trigonometric, hyperbolic (Eqs. 2.15–2.17).

**Generalized Gaudin Algebra (§2.3).** Operators $S^x(u), S^y(u), S^z(u)$ with commutation relations Eqs. 2.18–2.21 parameterized by functions $X(u,v), Y(u,v), Z(u,v)$. Continuous family of commuting operators $\mathbb{S}^2(u) = S^x(u)^2 + S^y(u)^2 + S^z(u)^2$ (Eq. 2.22) with $[\mathbb{S}^2(u), \mathbb{S}^2(v)] = 0$ (Eq. 2.23). Consistency (Jacobi) condition Eq. 2.25. XXZ constraint $X(u,v)^2 - Z(u,v)^2 = \Gamma$ (Eq. 2.26).

**Bethe ansatz (§2.5).** $|v_1\ldots v_N\rangle = \prod_{a=1}^N S^+(v_a)|0\rangle$ (Eq. 2.32) with vacuum satisfying $\mathbb{S}^2(u)|0\rangle = F_2(u)|0\rangle$, $S^z(u)|0\rangle = F_z(u)|0\rangle$, $S^-(u)|0\rangle = 0$ (Eq. 2.33).

**§2.7 Physical realizations.**
- Central spin model (2.7.1)
- Reduced BCS Hamiltonian (2.7.2)
- $p_x + ip_y$-wave pairing (2.7.3), topological superconductor

**Chapter 3: Eigenvalue-based framework.** Numerical approach solving for conserved-charge eigenvalues directly instead of rapidities, avoiding singular points where rapidities diverge. Weak-coupling limit (§3.2.1); Hellmann-Feynman theorem (§3.2.3); handling of degenerate models (§3.2.5).

**Chapter 4: Inner products.** Gaudin determinant, Izergin-Borchardt determinant, Cauchy matrix properties. Dual-state construction connecting eigenvalue-based to Slavnov determinants. Extension to hyperbolic models. From inner products to form factors (rapidity-based and eigenvalue-based).

**Chapter 5: Contraction limit and Dicke model.** Pseudo-deformation of the quasispin (§5.1); Dicke model as contraction limit (§5.2); extended $p_x + ip_y$ pairing (§5.3).

**Part II: Applications**

**Chapter 6: Read-Green resonances** in topological superconductor coupled to a bath. Mean-field theory (6.1.1) and Bethe ansatz (6.1.2); interaction with a bath (§6.2); signatures of the topological phase transition (§6.3).

**Part III (chapters on broken integrability)** includes:
- Variational method for integrability-breaking RG models (Phys. Rev. B 96, 155149)
- Breaking the Heisenberg model integrability through periodic driving (arXiv:1708.07324)
- RG-Configuration Interaction for nuclear pairing (arXiv:1712.01673)
- Spin polarization through Floquet resonances in driven central spin (arXiv:1712.03117, later PRL 121, 080401)
- Integrability and duality in spin chains
- Floquet resonances in quench-driven XY spin chain

**Broken integrability concepts.** Integrable Floquet dynamics (Ref. 284); absence of thermalization in finite driven Floquet systems (268); pre-thermalization in driven many-body systems (274, 295); Floquet-Magnus theory and high-frequency expansions (296, 297, 265); adiabatic perturbation theory and geometry of periodically driven systems (270).

## Key Results

1. Unified eigenvalue-based framework for Richardson-Gaudin integrable models avoiding rapidity singularities.
2. Determinant representations for scalar products and form factors in XXZ RG models.
3. Dicke model obtained as contraction limit of pseudo-deformed RG model.
4. Read-Green resonances characterized in topological $p+ip$ superconductor coupled to a bath.
5. Variational method for integrability-breaking RG models (GCI — Generalized Configuration Interaction).
6. Periodic driving breaks integrability of Heisenberg model — Floquet resonances identified.
7. Spin polarization controlled through Floquet resonances in driven central spin model.
8. RG-Configuration Interaction demonstrated for realistic nuclear pairing correlations (Sn isotopes).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| su(2) algebra | $[S^z_i, S^\pm_j] = \pm\delta_{ij}S^\pm_i$, $[S^+_i, S^-_j] = 2\delta_{ij}S^z_i$ | Eq. 2.10 |
| RG conserved charges | $Q_i = S^z_i + g\sum_{j\ne i}[X_{ij}(S^+_i S^-_j + S^-_i S^+_j) + Z_{ij}S^z_i S^z_j]$ | Eq. 2.12 |
| Gaudin eqs (antisym) | $X_{ij} + X_{ji} = 0$, $Z_{ij} + Z_{ji} = 0$ | Eq. 2.13 |
| Gaudin eqs (3-index) | $X_{ij}X_{jk} - X_{ik}(Z_{ij} + Z_{jk}) = 0$ | Eq. 2.14 |
| Rational model | $X_{ij} = 1/(\epsilon_i - \epsilon_j)$, $Z_{ij} = 1/(\epsilon_i - \epsilon_j)$ | Eq. 2.15 |
| Trigonometric model | $X_{ij} = 1/\sin(\epsilon_i-\epsilon_j)$, $Z_{ij} = \cot(\epsilon_i-\epsilon_j)$ | Eq. 2.16 |
| Hyperbolic model | $X_{ij} = 1/\sinh(\epsilon_i-\epsilon_j)$, $Z_{ij} = \coth(\epsilon_i-\epsilon_j)$ | Eq. 2.17 |
| GGA commutators | $[S^x(u), S^y(v)] = i(Y(u,v)S^z(u) - X(u,v)S^z(v))$ (and cyclic) | Eqs. 2.18–2.20 |
| Commuting family | $[\mathbb{S}^2(u), \mathbb{S}^2(v)] = 0$, $\mathbb{S}^2(u) = \sum_\alpha S^\alpha(u)^2$ | Eqs. 2.22–2.23 |
| GGA consistency | $X(u,v)Y(v,w) + Y(w,u)Z(u,v) + Z(v,w)X(w,u) = 0$ | Eq. 2.25 |
| XXZ constraint | $X(u,v)^2 - Z(u,v)^2 = \Gamma$ | Eq. 2.26 |
| XXZ $Z$-only eq | $Z(u,v)Z(v,w) + Z(w,u)Z(u,v) + Z(v,w)Z(w,u) = \Gamma$ | Eq. 2.27 |
| Raising/lowering | $S^\pm(u) = S^x(u) \pm iS^y(u)$ | Eq. 2.28 |
| XXZ commutator | $[S^-(u), S^+(v)] = -2X(u,v)(S^z(u) - S^z(v))$ | Eq. 2.30 |
| Bethe state | $\|v_1\ldots v_N\rangle = \prod_{a=1}^N S^+(v_a)\|0\rangle$ | Eq. 2.32 |
| Vacuum conditions | $\mathbb{S}^2(u)\|0\rangle = F_2(u)\|0\rangle$, $S^z(u)\|0\rangle = F_z(u)\|0\rangle$, $S^-(u)\|0\rangle = 0$ | Eq. 2.33 |

## Relevance to Phonon-Exflation

CRITICAL to S38 GGE permanence claim. The thesis provides the full toolkit behind the Ordered Veil:

1. **Integrability foundations (Ch. 2)** underpin the project's claim of 8 conserved charges in the N=8 BCS pairing on Dirac spectrum. The rational model Eq. 2.15 applies directly.

2. **Eigenvalue-based framework (Ch. 3)** gives computational method for the $L_{\max}=10$ eigenvalue problem (155,984 eigenvalues of $D_K$) — avoiding Bethe-root singularities.

3. **Inner products and form factors (Ch. 4)** provide the determinant structure needed for computing transition amplitudes in the substrate.

4. **Read-Green resonances in $p+ip$ (Ch. 6)** direct analog for topological phase transition across the van Hove fold — relevant to transit-cosmogenesis.

5. **Broken integrability via periodic driving** parallels the project's "transit physics, not equilibrium" paradigm. The GGE relic survives because the integrable structure is preserved; perturbations shift but do not destroy the non-thermal character.

6. **Floquet resonances and pre-thermalization** are directly analogous to the 59.8 quasiparticle pairs being prethermal (GGE) rather than fully thermal. The extensive conserved-charge set protects the Ordered Veil from thermalization on all timescales shorter than integrability-breaking corrections.
