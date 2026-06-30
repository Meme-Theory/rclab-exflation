# Atlas D07: Permanent Results Catalog (Updated Through Session 88)

**Original registry**: S1-S28 (`sessions/permanent-results-registry.md`)
**Atlas extension**: S29-S88 (this document)
**Generated**: 2026-03-20 | **Updated**: 2026-05-09 (S67-S88 uplift; +60 §VII slot inventory rows added; Section XVI introduced)
**Novelty audit**: 2026-03-20 (6 web-research agents) + 2026-05-09 round-trip audit (~37/66 §VII slots flagged for `/weave --update` entity-extractor refinement)

**Honest count (post-S88)**: 10 Level A novel + 5 Level B partial + 25 known/textbook/retracted + 17 permanent theorems (S63 T1-T17) + 18 structural results (S64-S66) + ~60 §VII registry slots S52-S88 (63 PERMANENT + 1 STAGE-1-CANDIDATE + 1 CANDIDATE-PENDING + 2 INFO + 2 CORRIGENDUM + 4 OPEN + 2 DEPRECATED; K-cohort synced to canonical at S109 MAINTAIN — 10 joint theorems STAGE-1-CANDIDATE→STAGE-3-PERMANENT, only K8 §VII.AF.1.STATE-PROJ remains pending) = **~150+ total publishable + STAGE-1-CANDIDATE registry landings**

---

## I. Publishable Standalone Mathematics

### Level A: Genuinely Novel (6 results — publishable standalone)

These fill documented gaps in the literature. No prior art found by systematic web search.

| # | Result | Session | Precision | Target | Novelty Basis |
|:--|:-------|:--------|:----------|:-------|:--------------|
| A1 | **Spectral Action Monotonicity Theorem** -- a_{2k} monotone for k=0,1,2,3. Spectral action monotone under both connections, all smooth cutoffs, all temperatures, all Lambda > 0. Periodic orbit corrections bounded at 10^{-39}. | 24a+28c | 10^{-39} | JGP/CMP | Connes 2019 review confirms no monotonicity framework exists in NCG literature. Genuine gap. |
| A2 | **Structural Monotonicity Theorem** -- <lambda^2>(tau) increases monotonically under volume-preserving Jensen deformation on SU(3). For any monotone cutoff f, S_f(tau) inherits monotonicity sector-by-sector. All 10 Peter-Weyl sectors individually monotone in same direction. No minimum possible. 9,600 individual checks. | 37 | Machine epsilon | JGP/CMP | Strengthens A1. Combine into single paper. No prior work on spectral action behavior under metric flows. |
| A3 | **8D Petrov Classification of Jensen-Deformed SU(3)** -- Type D at tau=0 (Einstein manifold), algebraically general with 8 distinct eigenvalues at all tau > 0. Stable multiplicity structure {3,4,1,2,4,3,3,8}. | 25 | Machine epsilon | GRG | No CMPP classification of SU(3) Weyl tensor exists in literature. |
| A4 | **Lorentzian CMPP Type D** -- Physical spacetime (Lorentzian signature, complexified null frames) is algebraically special Type D. Corrects S49 "Type II locked" which was Riemannian artifact. | 50 | Exact | GRG | Combine with A3 into single classification paper. |
| A5 | **alpha_s = n_s^2 - 1 Structural Theorem** -- Five independent proofs that within K^2 propagators on compact Josephson lattices, the running is locked. 3-pole degeneracy, running mass bound gamma < 0.035, zero-mode protection, RPA suppression, Goldstone theorem dispersion. | 50 | Exact | CMP/PRD | ZERO prior art found. Highest novelty, highest risk. Either paradigm-shifting or framework artifact. Requires rapid peer review. |
| A6 | **Anderson-Higgs Impossibility for U(1)_7** -- [iK_7, D_K] = 0 prevents gauging at ALL orders. K_7 is Kosmann derivative (diffeomorphism), not inner automorphism (gauge). Two structurally distinct arguments (commutant obstruction with all-orders corollary; categorical inner/outer) + computational verification — the 2026-03-20 peer-review restructure demoted the former "third proof" (numerical) to verification status; row re-worded to match the corrected paper, 2026-06-12 papers review campaign. Categorical. | 51 | Exact | JGP/CMP | Inner vs outer automorphism distinction known (Connes), but all-orders impossibility for specific U(1)_7 on Jensen SU(3) is new. |

| A7 | **CF-9 Algebraic Identity (Berry = NCG = KK A-tensor)** -- |A_coset|^2 = 3/2 + (3/2)e^{-4*tau} verified at machine epsilon (dev < 2e-14) across tau = [0, 0.5]. The A-tensor on the submersion SU(3) -> CP^2 decomposes into tau-independent u(1) (topological, 1.000) and exponentially decaying su(2) components. Exactly 16/136,480 modes couple to 4D (Peter-Weyl selection rule, trivial (0,0) irrep only). | 62 | 2e-14 | JGP/CMP | No prior quantitative verification of the Berry-NCG-KK triple identification on SU(3). The Peter-Weyl selection rule and mode decomposition are new. |
| A8 | **Cauchy-Schwarz Spectral Moment Bound** -- For any spectral triple with discrete spectrum and non-negative cutoff f: F_0 F_{k+l} >= F_k F_l (Cauchy-Schwarz hierarchy). The Gaussian cutoff saturates the bound exactly (F_2 = F_1^2/F_0). Proved from positive semidefinite bilinear form on the spectral weights. The bound is PERMANENT, cutoff-independent, and holds for ALL spectral triples. Numerical verification on the 992-mode D_K spectrum at fold: all 6 cutoff families satisfy the discrete bound (excess 0.7-43.3%). | 62 | Exact proof | JGP/CMP | General theorem for spectral triples. Novel: the moment hierarchy constrains the spectral action cutoff function. Gaussian saturation property singled out as unique. |
| A9 | **CC Monotonicity Theorem (q-theory)** -- dE_ZP/dq = (1/4) sum (2N_n + 1) d_n / omega_n(q) > 0 for all q > -lambda_min^2. The zero-point energy of any spectrum with positive weights is monotonically increasing in the shift parameter q. No interior equilibrium exists. Applied to SU(3) with GGE occupations: Lambda_CC = 0.838 M_KK^4 (114 OOM above observed). CC = integrability. | 62 | Exact proof | CMP/PRD | The monotonicity is elementary (sum of positive terms), but its application to the CC problem via q-theory and GGE occupations is novel. Connects Volovik q-theory to Richardson-Gaudin integrability. |
| A10 | **Filter-Independence of Tree-Level Higgs Mass** -- The CCM spectral action Higgs mass depends only on g_3^2(M_KK) and a_4/a_2, NOT on the cutoff function shape. Specifically lambda_h = (4/3)g_3^2(M_KK)(a_4/a_2), giving m_H = 134.04 GeV for ALL 6 tested filter families. The cutoff enters only through f_4 (CC) and higher moments. | 62 | Structural | PRD/CMP | The structural independence follows from CCM Paper 10 eq 3.37 but has never been numerically verified across multiple filter families on a specific KK geometry. |

| A11 | **Volovik Gibbs-Duhem Relaxation** -- rho_vac = epsilon(q) - mu*q -> 0 as q adjusts. Applied to spectral action: rho_vac ~ M_Pl^2 H^2 tracking. Landing at rho_vac(today)/rho_obs = 1.032 (0.01 OOM). FUNCTIONAL-INDEPENDENT: holds for any spectral functional. | 66 | 0.01 OOM | CMP/PRD | Novel application of Volovik q-theory to spectral action CC. The combination of Gibbs-Duhem identity with spectral action expansion history is new. |
| A12 | **Chebyshev Monotonicity Theorem** -- Q^eff >= Q^bare for all UV-suppressing cutoffs. Protection cascade: monotonicity guarantees Gibbs-Duhem tracking. Proved from Chebyshev integral inequality on spectral sums with ordered weights. | 66 Workshop 1 | PERMANENT | JGP/CMP | Novel: establishes monotonicity protection for spectral action vacuum tracking. No prior art on Chebyshev bounds applied to spectral action. |
| A13 | **Epsilon_H Sign Reversal** -- eps_H changes SIGN between cutoff families (sqrt(x): +0.022 vs zeta: negative). Scheme-dependent at the sign level. n_s spread across functionals: 0.164 (39x Planck error). | 66 W2-A | PERMANENT (negative result) | PRD | Novel negative result: demonstrates that the spectral index prediction is spectral-functional-dependent at the qualitative level. Forces functional selection as a physical requirement. |

**Recommended papers (5+2):**
1. "Monotonicity of the Spectral Action Under Jensen Deformation" (A1+A2) -> JGP/CMP
2. "Algebraic Classification of the Weyl Tensor on Jensen-Deformed SU(3)" (A3+A4) -> GRG
3. "Ungaugeability of Kosmann Symmetries of the Dirac Operator on Compact Lie Groups" (A6; retitled at the 2026-03-20 peer-review revision) -> JGP/CMP
4. alpha_s = n_s^2 - 1 (A5) -> PRD **only if derivation survives external scrutiny**
5. "Cauchy-Schwarz Hierarchy for Spectral Moments and Gaussian Saturation" (A8) -> JGP/CMP
6. "Berry-NCG-KK Triple Identification on the SU(3) Submersion" (A7+A10) -> JGP/CMP
7. "Volovik Relaxation of the Cosmological Constant in Spectral Action Cosmology" (A11+A12) -> CMP/PRD
8. "Scheme Dependence of the Spectral Index in NCG Spectral Action" (A13) -> PRD

### Level B: Partially Novel (5 results — need further work before submission)

These contain novel elements but require deeper literature comparison, rigorous proof, or engagement with prior art.

| # | Result | Session | Status | Issue |
|:--|:-------|:--------|:-------|:------|
| B1 | **Cl(8) Three-Way Bridge** -- Berry phase gamma/pi ~ 1, order-one violation hierarchy 2^{1+k/2}, 6/7 NCG axioms -- all trace to Spin(8) on C^16. | 28 | Partial prior art | Furey's Cl(8) program (arXiv:1702.04336, 2206.06912) covers related ground. Specific three-way unification may be novel synthesis. Requires direct comparison to Furey. |
| B2 | **Berry Curvature Vanishing on Compact Lie Groups** -- K_a anti-Hermitian implies Berry curvature Omega = 0 identically for ALL eigenstates, ALL sectors, ALL tau. | 25 | Partial novelty | Not explicitly in literature, but may be seen as algebraically trivial by reviewers. Anti-Hermiticity -> vanishing is a short argument. Risk: medium. |
| B3 | **Spectral Bianchi Identity** -- Gauge invariance of spectral action under SU(3)_L constrains sector-weighted spectral derivatives. | 25 | Unclear | Ward identities for spectral action may be implicit in Connes' formalism. Specific sector-weighted form may be novel. Needs validation against van Suijlekom's work. |
| B4 | **Interior Mixing Theorem** -- D_F couples to interior spectral modes, not gap-edge modes, via algebraic (m+m') suppression. Generalizes to any Dirac operator perturbed by Kosmann-Lichnerowicz commutator on a compact Lie group. | 30Ab | Potentially novel | Framework-specific in derivation but claimed generalization to all compact Lie groups needs independent verification. |
| B5 | **SU(3) Anomalously Curved vs SU(2)xSU(2)** -- Opposite-sign spectral action curvature. Fold on SU(3) has no counterpart on SU(2)xSU(2). Root cause: complex representations. | 35 | Potentially novel | Specific comparison likely new. Could strengthen the monotonicity paper (A1+A2) as supporting evidence for SU(3) specificity. |

### Level C: Known Results on Specific Manifold (10 results — useful as lemmas, not standalone)

These apply established mathematical tools (Schur's lemma, Weyl's law, Cooper instability, Gilkey formula, Sakharov mechanism) to the specific spectral triple on Jensen-deformed SU(3). Correct and useful, but the novelty is in the *input data*, not the *method or statement*. Cite the original sources; use as supporting lemmas.

| # | Result | Session | Known Source |
|:--|:-------|:--------|:-------------|
| C1 | D_K Block-Diagonality Universality | 22b | Schur's lemma + equivariance. Fegan 1987, Slebarski 1985 assume this. |
| C2 | Three Algebraic Traps (F/B, b_1/b_2, e/(ac)) | 20b-22c | Weyl's law, Dynkin indices, trace factorization. Standard tools. |
| C3 | Van Hove Zero-Critical-Coupling | 28c | Cooper instability (1956). Application to compact manifolds untested but mechanism is textbook. |
| C4 | Trap 4: Schur Orthogonality Selection Rule | 32a+32c | Schur orthogonality for U(2) reps. Automatic from representation theory. |
| C5 | Trap 5: J-Reality PH Selection Rule | 32b | Real structure J with J^2=+1 on real reps. Standard NCG. |
| C6 | [iK_7, D_K] = 0 at ALL tau | 34 | Computation of a commutator on a specific deformation family. Novel fact but routine calculation. |
| C7 | Trap 1 Confirmed: V(B1,B1) = 0 | 34 | U(2) singlet selection rule. Standard representation theory. |
| C8 | B2 Geometric Protection Theorem | 39 | Schur's lemma on irreducible (1,1) subspace. |
| C9 | Sakharov Induced Gravity from KK Spectrum | 44 | Toms 1983 already established KK + Sakharov. Methodology known. |
| C10 | a_2^bos/a_2^Dirac = 61/20 Exact | 44 | Gilkey formula applied to specific reps. Computation, not theorem. |

### Level D: Textbook / Trivial / Not Publishable (13 results)

These are either standard textbook results, trivial consequences of definitions, restatements of known theorems, or retracted claims. They should NOT appear on any publishable list.

| # | Result | Session | Why Not Publishable |
|:--|:-------|:--------|:--------------------|
| D1 | LZ Retraction / Codimension Classification | 28 | LZ is for two-level systems; BCS is many-body. Physicists already know this. |
| D2 | Spectral Flow = 0 Theorem | 25 | Lichnerowicz bound (1963) applied to SU(3). Verification, not research. |
| D3 | Grading Theorem | 25 | 3-line proof from gamma_9 anticommutation + trace cyclicity. Standard NCG. |
| D4 | Perturbative Exhaustion Theorem | 22c | Standard first-order phase transition thermodynamics with metastable branches. |
| D5 | Schur's Lemma on B2 | 34 | Literally Schur's lemma applied to an irreducible rep. |
| D6 | BCS Instability Is a 1D Theorem | 35 | Cooper instability (1956). Restatement. |
| D7 | N_pair = 1 Exact Reduction | 39 | Richardson exact solution (1963) applied to finite system. |
| D8 | Geometric LCDM | 42 | Spectral action -> CC is Chamseddine-Connes 1997. CDM claims require additional fiber structure not present. Overstated. |
| D9 | CDM by Construction (T^{0i}=0) | 44 | Homogeneity -> no preferred direction -> T^{0i}=0. Basic field theory. |
| D10 | Taylor Expansion Exactness Theorem | 45 | Finite sum of analytic functions is analytic. Mathematical tautology. |
| D11 | Trace Theorem (Goldstone Mass Wall) | 48 | S[UDU^dag] = S[D] is the cyclic property of the trace. Known since before NCG existed. |
| D12 | Acoustic Hawking Temperature Agreement | 40 | Barcelo framework standard; BCS application may be new but agreement is expected, not surprising. |
| D13 | n_s > 1 Structural for KK Tower | 51 | Components exist (heat kernel, Weyl asymptotics) but the structural claim as stated needs rigorous proof. Unvalidated. |

### Level E: Retracted (2 results)

| # | Result | Session | Retraction |
|:--|:-------|:--------|:-----------|
| E1 | Schwinger-Instanton Action Equality | 37-38 | Algebraic identity retracted S39. Numerical near-agreement survives as shape factor universality kappa = 0.653, but not publishable as "equality." |
| E2 | GGE from Sudden Quench (permanence) | 38-39 | Permanence retracted S39. GGE thermalizes in ~6 natural units via 13% non-separable V_phys. |

### Audit Methodology

Six web-research agents dispatched 2026-03-20 searched: arXiv, Semantic Scholar, Google Scholar, Wikipedia, nLab, journal archives (JGP, CMP, GRG, JMP, PRD, PRL), textbooks (Connes, van Suijlekom, Friedrich, Huang-Pandzic, Peskin-Schroeder), and specific author catalogs (Chamseddine, Connes, van Suijlekom, Furey, Fegan, Slebarski, Barcelo, Richardson, Cooper, Sakharov, Toms, Lichnerowicz). Each claim evaluated for: (1) existence of identical published result, (2) whether the claim follows trivially from known results, (3) whether prior art covers the essential content.

---

## II. Machine-Epsilon Verified Infrastructure

| Result | Count | Precision | Session | Script |
|:-------|:------|:----------|:--------|:-------|
| KO-dim = 6 mod 8 (parameter-free) | 10 checks | < 1e-15 | 7-8 | `branching_computation_32dim.py` |
| SM quantum numbers from Psi_+ = C^16 | 6 multiplets | Exact | 7 | `branching_computation.py` |
| J^2 = +I (epsilon = +1) | -- | < 1e-15 | 8 | `branching_computation_32dim.py` |
| J*rho = rho*J (epsilon' = +1) | -- | < 1e-15 | 8 | `branching_computation_32dim.py` |
| J*gamma = -gamma*J (epsilon'' = -1) | -- | < 1e-15 | 8 | `branching_computation_32dim.py` |
| [J, D_K(tau)] = 0 (CPT hardwired) | 79,968 pairs | max 3.29e-13 | 17a | `d1_d3_j_compatibility.py` |
| g_1/g_2 = e^{-2tau} structural identity | Derived | Exact | 17a B-1 | `gauge_coupling_derivation.py` |
| Baptista geometry checks | 67/67 | Machine epsilon | 17b | `b2_baptista_verification.py` |
| D_K correctness audit | 39/39 | Exact zeros | 17b | `b3_dk_correctness_audit.py` |
| Riemann tensor R_{abcd}(tau) | 147/147 | Machine epsilon | 20a | `r20a_riemann_tensor.py` |
| Volume-preserving TT-deformation | det = 1.000000000 | Exact | 12 | `dirac_spectrum.py` |
| 4 curvature invariants (analytic) | Exact formulas | Rational coefficients | 17b | `sp2_analytic_derivation.py` |
| Dirac pipeline (8 validations) | All < 10^{-10} | Machine epsilon | 12 | `dirac_spectrum.py` |
| AZ class BDI, T^2 = +1 | -- | Exact | 17c | `d4_bdg_classification.py` |
| lambda^2 = n/36 algebraic spectrum | 16 integers | Exact algebraic | 12 | `dirac_spectrum.py` |
| Pfaffian Z_2 = +1 throughout | 100+ tau | Binary | 17c | `d2_pfaffian_computation.py` |
| Gauss-Bonnet chi(SU(3)) = 0 | 21 tau | 1.24e-15 | 21c | -- |
| TT stability: no tachyons | all tau in [0,2] | Positive | 20b | `l20_lichnerowicz.py` |
| Lichnerowicz code audit | 10 modules, 8/8 | Zero bugs | 20b | `l20_lichnerowicz.py` |
| D_can = M_Lie identity | -- | C1=0.00e+00, C2=0.00e+00, C3=1.11e-16 | 27 | -- |
| Spectral pairing lambda <-> -lambda | -- | 5.5e-15 | 26 | -- |
| [NEW S30] D_F construction (Baptista Approach B) | 9 tau values | D_F(0) = 6.89e-15 | 30Aa | `s30a_df_construction.py` |
| [NEW S30] D_F chirality preservation | 9 tau | 5.59e-14 | 30Aa | `s30a_df_construction.py` |
| [NEW S30] D_F block-diagonality | 9 tau | Exact zero cross-sector | 30Aa | `s30a_df_construction.py` |
| [NEW S30] Pfaffian D_total = +1 on Jensen | 75 tau | Binary, all sectors | 30Ab | `s30a_dtotal_pfaffian.py` |
| [NEW S34] J operator corrected (C2 = gamma_1*gamma_3*gamma_5*gamma_7) | all tau | Machine epsilon | 34 | -- |
| [NEW S35] BDI Pfaffian sgn(Pf) = -1 at all 34 tau | 34 tau | Binary | 35 | `s35_pfaffian_j_corrected.py` |
| [NEW S35] V matrix unitarity (optical theorem) | 4x4 + 16x16 | 2.2e-12 | 35 | -- |
| [NEW S40] HESS-40: all 22 transverse Hessian eigenvalues positive | 22 directions | min H = +1572 | 40 | `s40_hessian.py` |
| [NEW S42] w = -1 + O(10^{-29}) | -- | 10^{-29} | 42 | `s42_wz.py` |
| [NEW S45] Kretschner K(tau) monotonically increasing | [0, 0.50] | Structural | 45 | `s45_kretschner.py` |
| [NEW S45] G_N topological protection (2.5% variation) | [0, 0.50] | Structural | 45 | `s45_running_gn.py` |
| [NEW S47] Protected curvatures K(u(1),su(2))=0, K(u(1),C^2)=1/16 | 26 tau | Machine epsilon | 47 | -- |
| [NEW S47] Ric(u(1)) = 1/4 exactly at all tau | 26 tau | 2.2e-16 | 47 | -- |
| [NEW S48] TT spectrum fully positive (31 modes) | 9 tau in [0, 0.50] | All positive | 48 | `s48_tt_lich.py` |
| [NEW S50] Phi crossing omega_L2/omega_L1 = phi_paasch at tau=0.211686 | 61-point scan | 4.4e-15 | 50 | `s50_leggett_phi_confirm.py` |
| [NEW S61] a_2 = 0.728235 (10-digit S46 match) | -- | Exact | 61 | `s61_heat_kernel_a2.py` |
| [NEW S61] NCG verification chain 7/7 complete | 7 links | All PASS | 61 | Multiple s61_*.py |
| [NEW S61] Block-diagonal theorem extended to ALL compact Lie groups | -- | Theorem | 61 | `s61_block_diagonal_general.py` |
| [NEW S61] SM gauge group recovery (13/13 generators) | 13 generators | < 1e-13 | 61 | `s61_gauge_module.py` |
| [NEW S61] 36D Hessian ALL 36 eigenvalues negative | 36 directions | All negative | 61 | `s61_hessian_36d.py` |
| [NEW S61] Kasparov product 6/6 conditions | First computation | All PASS | 61 | `s61_kasparov_product.py` |
| [NEW S61] EWSR Thouless identity | 16/16 checks | 14 sig figs | 61 | `s61_ewsr_thouless.py` |
| [NEW S62] CF-9 |A_coset|^2 = 3/2 + (3/2)e^{-4tau} | 21 tau points | < 2e-14 | 62 | `s62_berry_projection.py` |
| [NEW S62] Higgs doublet gauge-invariant in End(C^48) | 10 irreps | 3.5e-14 mixing | 62 | `s62_higgs_order_one.py` |
| [NEW S62] Cauchy-Schwarz hierarchy on D_K spectrum | 6 families | All PASS (discrete) | 62 | `s62_cauchy_schwarz.py` |
| [NEW S62] Meissner D_s(GGE)/D_s(fold) = 0.9885 | 5 routes | All PASS | 62 | `s62_meissner_gge.py` |
| [NEW S62] BdG gauge fraction: gauge/gravity = 2.723 (structural formula) | 8 modes | Algebraic identity | 62 | `s62_bdg_gauge_fraction.py` |
| [NEW S62] Delta > 0.353 M_KK along softest Hessian direction | 20 points | 7.1x threshold | 62 | `s62_type_i_transit.py` |

### S63 Permanent Theorems (T1-T17) — NEW

| Result | Precision | Session | Source |
|:-------|:----------|:--------|:-------|
| [T1] Zero First-Order Tensor — homogeneous transit on M^4 x K: pi_ij=0 | Exact | 63 | VdD-Hawking |
| [T2] Breathing Mode Exclusion — delta g_ab^K = h(x)g_ab^K projects to 4D scalar, not tensor | Exact | 63 | VdD-Hawking |
| [T3] Scalar-Tensor Kasparov Decoupling — U_total = 1_M tensor U_K implies beta_T=0 exactly at linear order | Exact | 63 | VdD-Hawking |
| [T4] Exflation Tensor Theorem — r depends on exactly 3 numbers: eps(0.0216), c_s(0.485), N_e | Exact | 63 | VdD-Hawking E5 |
| [T5] Volume-Preserving No-Trapping — theta_int=0 identically; Penrose singularity theorem inapplicable | Exact | 63 | W6-14 |
| [T6] Constant-Epsilon Theorem — n_s = (1-3eps)/(1-eps) for power-law with constant eps, c_s | Exact | 63 | W4-01 |
| [T7] n_s Gauge Invariance — eps_BLV = 2 - 1/eps_SA (exact); BLV and SA give identical n_s | Exact | 63 | W1-05 |
| [T8] Hessian Cluster Structure — 10-cluster = Ad(U(2)) decomposition of Sym^2(su(3)); by Schur's lemma | Exact | 63 | W2-06 |
| [T9] Mixed B-F q-theory Exclusion — same-spectrum B/F has at most one critical point (maximum). 9th CC closure | Exact | 63 | W3-06 |
| [T10] Cartan Trace Identity — T_{SU(3)}(p,q) = T_{SU(2)}(q,p) = T_{U(1)}(q,p)/12 for ALL (p,q) | Exact | 63 | W5-07 |
| [T11] Nonlocal Form Factor Inheritance — analyticity class of F(p^2) = analyticity class of f''(z). IDG CC CLOSED | Exact | 63 | W6-01 |
| [T12] Transfer Function Factorization — T(k_4D|k_KK) = T_proj * T_evo. n_s is cutoff-independent | Exact | 63 | W6-03 |
| [T13] MaxEnt Gaussian Uniqueness — Gaussian cutoff is unique max entropy solution. Strict concavity + KL divergence | Exact | 63 | W6-21 |
| [T14] Kinetic Normalization Identity — K_DeWitt = 5.0 exact (LEADING two-derivative coeff, regulator-invariant), tau-independent; GCR-derived AND path-integral one-loop-MEASURE cross-confirmed (rel=0) † | Machine eps | 63, 116 | W6-25, S116-W4 |
| [T15] Casimir Sigma Scaling — E_Cas(sigma) = sigma^{-1/8} E_Cas(1) to machine eps. Pure power-law | Machine eps | 63 | W5-03 |
| [T16] S_3 Subgroup Edge-Weight — Josephson anisotropy max/min = 11.80, from S_3 subset S_4 | Exact | 63 | W3-08 |
| [T17] Proton Decay Tree-Level Zero — exactly zero by PW orthogonality on SU(3). tau_p = 6.26e39 yr | Exact | 63 | W4-04 |

† **[T14] scope** (S116-W4-ZNORM-PROVENANCE workshop × `S116-W4-MODULUS-PATHINT` PASS, audit `1148fd1b…`): "`= 5`" is exact and REGULATOR-INVARIANT as the **LEADING TERM** (a₂ geometric content — DeWitt contraction over SU(3)→u(2)⊕C² branching `{3,4,1}×{−2,+1,+2}²`, `w`-independent by `Σ n_i c_i = 0`, measure-confirmed: conformal/volume mode decouples, FP det τ-independent, fiber det well-defined). The **OPERATIVE** two-derivative coefficient is `5(1+δ)`, with `δ` a genuine SAME-ORDER a₄ correction (`R_K(∂τ)²`, `[τ]+2`), OPEN and `O(1)`-plausible at the fold (`ρ_B = R_K/Λ_eff² = −1.712`, single-scale); numerically-leading for `|τ−τ_fold| ≳ X` (`X` = `CF-S117-MODULUS-A4-GRADIENT` deliverable), expansion-marginal AT the fold. The four-derivative operators (`|R_{μaνb}|²`) are a SEPARATE order; the order-mixed `K_total≈7.07` is RETIRED. Standing scope: **DERIVED given S3** (SA-as-modulus-effective-action, ASSUMED, atlas-04) — prose tag = register tag.

### S64-S66 Structural Results — NEW

| Result | Precision | Session | Source |
|:-------|:----------|:--------|:-------|
| R-monotonicity on Jensen (AM-GM exact): dR/dtau >= 0 | PERMANENT | 64 W1-A | Candidate wall |
| Fermi-surface lock: v^2(B2[0]) = 1/2 identically | PERMANENT | 64 W2-C | Algebraic |
| a_0/a_2 trap (off-Jensen): decreasing a_2 INCREASES a_0/a_2 | PERMANENT | 64 W2-A | Candidate wall |
| Spectral moment decoupling: F_{-1}(CC) vs F_{+1}(NEC) are different moments | PERMANENT | 64 W5-B | Structural |
| H2 theorem: pi_ij=0 from DeWitt tracelessness (volume-preserving) | PERMANENT | 64 W3-A | Structural |
| Chirality antisymmetry: {gamma_9, dD_K/dtau}=0. Chiral pairs ADD, not cancel | PERMANENT | 64 W6-B | Algebraic |
| BdG Heat Kernel Factorization: K_BdG(t) = exp(-Delta^2 t) K_bare(t) | PERMANENT | 64-65 | Structural |
| CC Ratio from Scalar Curvature Only: d(a_0/a_2)/ds = -(a_0/a_2)/R dR/ds | PERMANENT | 65 W1-B | Structural |
| B/F Spectral Asymmetry = 0: |A|=0 EXACTLY on pure Riemannian triple | PERMANENT | 65 W1-C | Exact |
| Bogoliubov Gaussianity Preservation: f_NL = O(eps) regardless of squeezing | PERMANENT | 65 W5-D | Structural |
| EIH Casimir Monotonicity: local a_0/a_2 increases with C_2(p,q) | PERMANENT | 65 W6-A | Structural |
| Volovik Gibbs-Duhem relaxation: rho_vac = eps(q)-mu*q -> 0 as q adjusts | FUNCTIONAL-INDEPENDENT | 66 W1-A | Novel (A11) |
| Chebyshev monotonicity theorem: Q^eff >= Q^bare for all UV-suppressing cutoffs | PERMANENT | 66 Workshop 1 | Novel (A12) |
| BCS-Sakharov decoupling: a_2, a_4 orthogonal projections. r_2=0.892 | PERMANENT | 66 Workshop 1 | Structural |
| Anomaly one-parameter family: c_k(phi) = (-1)^k phi^k/k at one loop | STRUCTURAL | 66 Workshop 2 | Structural |
| Heat kernel bridge: SA <-> heat kernel <-> S-matrix via Bernstein's theorem | STRUCTURAL | 66 Workshop 5 | Structural |
| eps_H sign reversal between cutoff families: SCHEME-DEPENDENT at sign level | PERMANENT (negative) | 66 W2-A | Novel (A13) |
| KO-dimension degeneracy at d=8: B_+/B_- give identical KO signs | PERMANENT | 66 W8-A | Algebraic |

**Total proven mathematical results: 77+ publishable (Atlas D07 Levels A-C) + 17 (S63 T1-T17) + 18 (S64-S66) = 112+**

---

## III. Four Curvature Invariants (Exact Analytic, Session 17b)

All verified at machine epsilon (< 10^{-15}) across 51 tau-values. Rational coefficients.

**Scalar curvature:**
R(tau) = -(1/4)e^{-4tau} + 2e^{-tau} - 1/4 + (1/2)e^{2tau}; R(0) = 2

**Ricci squared:**
|Ric|^2(tau) = (1/12)e^{-8tau} - (1/2)e^{-5tau} + (1/8)e^{-4tau} + (13/12)e^{-2tau} - (1/2)e^{-tau} + 1/8 + (1/12)e^{4tau}

**Kretschner scalar:**
K(tau) = (23/96)e^{-8tau} - e^{-5tau} + (5/16)e^{-4tau} + (11/6)e^{-2tau} - (3/2)e^{-tau} + 17/32 + (1/12)e^{4tau}

**Weyl squared:**
|C|^2(tau) = (377/2016)e^{-8tau} - (5/7)e^{-5tau} + (79/336)e^{-4tau} + (325/252)e^{-2tau} - (17/14)e^{-tau} + 101/224 + (2/21)e^{tau} - (1/84)e^{2tau} + (5/126)e^{4tau}

---

## IV. Structural Walls

### Original Walls (Sessions 22-25)

| Wall | Name | Content | Scope |
|:-----|:-----|:--------|:------|
| W1 | Weyl Asymptotic F/B Ratio | F/B = 4/11 (fiber dim bosonic 44 vs fermionic 16). Tau-independent. | UV, tau-independent |
| W2 | Peter-Weyl Block-Diagonality | D_K exactly block-diagonal for ANY left-invariant metric on compact Lie group | Exact, 8.4e-15 |
| W3 | Spectral Gap at mu = 0 | lambda_min > 0 prevents spontaneous BCS (no Fermi surface) | Exact |
| W4 | Spectral Action Monotonicity | Tr f(D^2/Lambda^2) monotone in tau, both connections, all cutoffs, all T | Exact to 10^{-39} |
| W5 | Berry Curvature Vanishing | K_a anti-Hermitian => Berry curvature = 0 identically. Closes all topological mechanisms. | Exact |
| W6 | Thermodynamic Stabilization | Smooth functional trap + Matsubara stiffening. | Exact |

### Walls Extended (Sessions 30-40)

| Wall | Extension | Session |
|:-----|:----------|:--------|
| W4 | Extended from 1D Jensen to full 3D U(2)-invariant surface (V_spec/F_BCS ~ 8000) | 30Ba |
| W3 | BYPASSED at domain wall boundaries (W-32b: van Hove LDOS exceeds threshold) | 32b |
| W4 | CIRCUMVENTED at quantum level (RPA-32b: chi = 20.43, 38x margin) | 32b |
| W5 | Extended from Jensen to U(2)-invariant submanifold (BDI Z=+1 along T2) | 32c |

### New Walls (Sessions 37-51)

| Wall | Name | Content | Session |
|:-----|:-----|:--------|:--------|
| W7 | Structural Monotonicity | S_f(tau) monotonic for ALL smooth monotone f, ALL Lambda, ALL tau, ALL 10 sectors | 37 |
| W8 | BdG Anti-Trapping | delta_S_BdG = +12.8 (positive). Spectral action PENALIZES pairing structurally. | 37 |
| W9 | HESS Full Moduli | All 22 transverse Hessian eigenvalues positive (min +1572). Jensen is local minimum in ALL 28 dimensions. | 40 |
| W10 | Effacement Ratio | |E_BCS|/S_fold = 3e-7. Defeats ALL BCS-derived corrections to w. | 42 |
| W11 | Trace Theorem | S[UDU^dag] = S[D]. Spectral action blind to Goldstone mass (cyclic invariance). | 48 |
| W12 | Anderson-Higgs Impossibility | [iK_7, D_K] = 0 prevents U(1)_7 gauging. K_7 is diffeomorphism, not gauge. | 51 |
| W13 | n_s >= 1 for KK Tower | Bare Dirac heat kernel on compact manifolds gives n_s >= 1 structurally. | 51 |

---

## V. Closed Mechanisms (Cumulative ~50+)

### Original 21 (Sessions 17-28)

| # | Mechanism | Session | Wall |
|:--|:----------|:--------|:-----|
| 1 | V_tree minimum | 17a SP-4 | W4 |
| 2 | 1-loop Coleman-Weinberg | 18 | W1 |
| 3 | Casimir scalar + vector | 19d D-1 | W1 |
| 4 | Spectral back-reaction (scal+vec) | 19d | W1 |
| 5 | Fermion condensate (Banks-Casher) | 19a S-4 | W3 |
| 6 | D_K Pfaffian Z_2 transition | 17c D-2 | -- |
| 7 | NCG spectral action (Seeley-DeWitt) | 20a SD-1 | W4 |
| 8 | Casimir with TT 2-tensors | 20b L-3/L-4 | W1 |
| 9 | Single-field slow-roll | 19b R-1 | W4 |
| 10 | Connes 8-cutoff positive sums | 21a | W4 |
| 11 | V''_total spinodal | 21a | W4 |
| 12 | S_signed gauge-threshold | 21c | W1 |
| 13 | Coupled delta_T crossing | 22b PB-3 | W2 |
| 14 | Coupled V_IR minimum | 22b PB-2 | W2 |
| 15 | Higgs-sigma portal | 22c C-1 | W1 |
| 16 | Rolling modulus quintessence | 22d E-3 | -- |
| 17 | Kosmann-BCS condensate (mu=0) | 23a K-1e | W3 |
| 18 | Gap-edge self-coupling | 23a | W3 |
| 19 | V_spec(tau; rho) monotone | 24a V-1 | W4 |
| 20 | BCS cooling trajectories | 26 P2 | -- |
| 21 | Kerner bridge (a_6 truncation) | 26 P3 | W4 |

### Sessions 29-51 Closures (Selected Major)

| # | Mechanism | Session | Wall/Reason |
|:--|:----------|:--------|:------------|
| 22 | [NEW S30] Pfaffian D_total on Jensen | 30Ab | Pf=+1 all 75 tau (Interior Mixing Theorem) |
| 23 | [NEW S30] V_total on 3D U(2)-invariant surface | 30Ba | V_spec/F_BCS ~ 8000, no minimum |
| 24 | [NEW S34] Canonical mu != 0 | 34 MU-35a | PH forces mu=0 analytically |
| 25 | [NEW S34] Grand canonical mu != 0 | 34 GC-35a | Helmholtz F convex, mu=0 global minimum |
| 26 | [NEW S35] Singlet tridiagonal PMNS | 35 | R ceiling ~5.9, need ~33 |
| 27 | [NEW S35] Poschl-Teller phi_paasch | 35 | Zero bound states, 18x short |
| 28 | [NEW S35] Entropy attractor | 35 | S_vN monotonically decreasing |
| 29 | [NEW S37] Cutoff spectral action stabilization | 37 | W7 Structural Monotonicity Theorem |
| 30 | [NEW S37] One-loop RPA self-trapping (F.5) | 37 | W8 Wrong sign (+12.8, 93x anti-trapping) |
| 31 | [NEW S37] (B1,B3,G1) PMNS triad | 37 | Algebraic: all (1,0) weights have q_7 != 0 |
| 32 | [NEW S38] CC-through-instanton | 38 | <Delta^2>/Delta_0^2 min = 0.831, 76x above threshold |
| 33 | [NEW S39] Friedmann-BCS tau stabilization | 39 | Gradient ratio 6,596x, shortfall 133,200x |
| 34 | [NEW S39] GGE permanence (retracted) | 39 | V_phys 13% non-separable, thermalizes in ~6 nat units |
| 35 | [NEW S39] Schwinger-instanton duality (retracted) | 39 | GL ratio 4.08 (not 1), numerical coincidence |
| 36 | [NEW S40] HESS full moduli stabilization | 40 | W9: all 22 eigenvalues positive, 27th equilibrium closure |
| 37 | [NEW S42] Fano interference (discrete+discrete) | 42 | K anti-Hermitian forces q=infinity |
| 38 | [NEW S42] Polariton Higgs | 42 | Min gap 0.063 M_KK, 3.7e13x too large |
| 39 | [NEW S42] Slow-roll n_s from spectral action | 42 | eta = 0.243, structural |
| 40 | [NEW S44] Lifshitz anomalous dimension for n_s | 44 | eta_eff = 3.77, Weyl's law |
| 41 | [NEW S44] Foam stabilization of tau | 44 | 0/900 minima found |
| 42 | [NEW S45] Occupied-state spectral action | 45 | S_occ monotone decreasing |
| 43 | [NEW S45] Unexpanded spectral action CC hierarchy | 45 | Taylor exactness on finite spectrum |
| 44 | [NEW S45] Bogoliubov/KZ n_s (all k-mappings) | 45 | n_s = -4.45 (EIH), -0.588 (primary) |
| 45 | [NEW S45] Sigma-selection for n_s | 45 | 5 methods exhausted, no fixed point |
| 46 | [NEW S46] Twisted BdG NCG | 46 | BCS order parameter not algebra automorphism |
| 47 | [NEW S48] Spectral action Goldstone mass | 48 | W11 Trace theorem |
| 48 | [NEW S48] Q-theory self-tuning Goldstone mass | 48 | No finite fixed point, runaway |
| 49 | [NEW S48] k-dependent gap from rho_s anisotropy | 48 | n_s = -2.930 (927 sigma) |
| 50 | [NEW S51] Anderson-Higgs for U(1)_7 | 51 | W12 categorical |
| 51 | [NEW S51] Polariton coupling for n_s | 51 | Mass asymmetry 39x, 26x short |
| 52 | [NEW S51] Local resonance mass enhancement | 51 | Ward identity forces Sigma(0,0) = 0 |
| 53 | [NEW S51] Critical scaling n_s | 51 | Anti-critical point, eta = 1.8% |

---

## VI. Gate Verdicts (Sessions 29-51 Extension)

### Major PASS Gates (S29-S51)

| Gate | Result | Key Number | Session |
|:-----|:-------|:-----------|:--------|
| B-29a | 3-sector BCS | F_3sect = -17.22 (172x margin) | 29 |
| RPA-32b | Collective oscillation | chi = 20.43, 38x above threshold | 32 |
| W-32b | Boundary condensation | rho_wall = 12.5-21.6, 1.9-3.2x | 32 |
| NEFF-THOULESS-35 | N_eff resolution | M_max(8x8) = 1.674, N_eff_min = 2.48 | 35 |
| ED-CORRECTED-35 | Exact diag BCS | E_cond = -0.1151 < 0 | 35 |
| RG-BCS-35 | BCS 1D theorem | g -> strong coupling for ANY g > 0 | 35 |
| PF-J-35 | Pfaffian survives J correction | sgn(Pf) = -1 at all 34 tau | 35 |
| SAKHAROV-GN-44 | Induced gravity | Ratio 2.29 (0.36 OOM) at Lambda=10*M_KK | 44 |
| CDM-CONSTRUCT-44 | CDM algebraic | T^{0i} = 0 exact | 44 |
| Q-THEORY-BCS-45 | CC zero-crossing | tau* = 0.209, first CC PASS | 45 |
| LEGGETT-MODE-48 | Sharp undamped mode | omega_L1 = 0.070, Q = 670,000 | 48-50 |
| DIPOLAR-CATALOG-49 | Leggett IS 3He dipolar | 18% from n_s target mass | 49 |
| SIGMA8-OZ-50 | sigma_8 viable | 0.799 (between Planck and lensing) | 50 |
| COSMIC-CENSORSHIP-49 | Triple-layered | Energy + friction + no trapped surfaces | 49 |

### Major FAIL Gates (S29-S51)

| Gate | Result | Session |
|:-----|:-------|:--------|
| FRIED-39 | Shortfall 133,200x | 39 |
| HESS-40 | All 22 eigenvalues positive (no trapping) | 40 |
| CUTOFF-SA-37 | Structural monotonicity | 37 |
| NS-TILT-42 | n_s = 0.746 (52 sigma) | 42 |
| ALPHA-S-BAYES-49 | alpha_s = -0.069 (6 sigma from Planck) | 49 |
| SA-GOLDSTONE-MIXING-51 | FAIL at K_pivot = 2.0 (convex combination) | 51 |

---

## VII. Structural Identities & Exact Constants

### Original (Sessions 12-28)

| Identity | Value | Session | Source |
|:---------|:------|:--------|:-------|
| g_1/g_2 = e^{-2tau} | Derived from Jensen metric eq 3.71 | 17a B-1 | Structural |
| sin^2(theta_W) = e^{-4tau}/(1+e^{-4tau}) | tau_0 = 0.2994 from experiment | 17a | Structural |
| phi_paasch: m_{(3,0)}/m_{(0,0)} | 1.531580 at tau = 0.15 (0.5 ppm) | 12, 22a QA-4 | Numerical |
| F/B fiber ratio | 16/44 -> ~0.55 spectral-weighted | 20b | Weyl's law |
| b_1/b_2 = 4/9 | Triple confirmed | 21c, 22a | Algebraic |
| e/(ac) = 1/dim(spinor) = 1/16 | Trace factorization | 22c C-1 | Algebraic |
| V(gap,gap) = 0 | Exact selection rule (~10^{-29}) | 23a | Anti-Hermiticity |
| dalpha/alpha = -3.08 * tau_dot | From g_1/g_2 identity | 22d E-3 | Derived |
| a_4/a_2 ~ 985:1 at tau = 0 | Why Starobinsky fails on SU(3) | 24a | Structural |

### New (Sessions 29-51)

| Identity | Value | Session | Source |
|:---------|:------|:--------|:-------|
| [NEW S29] J_perp = 1/3 exactly | Schur's lemma (multi-sector BCS) | 29 | Algebraic |
| [NEW S30] phi_30 = m_(3,0)/m_(0,0) confirmed at N_max=6 | 1.532 at tau=0.15 (5 decimal match) | 30 | Numerical |
| [NEW S32] B2 4-fold degeneracy exact | spread < 1e-15 at all tau | 32 | U(2) representation |
| [NEW S32] B3 3-fold degeneracy exact | spread < 1e-15 at all tau | 32 | U(2) representation |
| [NEW S34] V(B1,B1) = 0 | Exact (3.4e-29, U(2) singlet) | 34 | Selection rule |
| [NEW S34] V(B1,B3) = 0 | Exact (5.8e-30, singlet x adjoint) | 35 | Selection rule |
| [NEW S35] Cooper pairs carry K_7 = +/-1/2 | V(q+,q-) = 0 exactly | 35 | Algebraic |
| [NEW S37] S_inst = 0.069 | Dense instanton gas | 37 | Numerical |
| [NEW S37] omega_att = 1.430 (fully geometric) | Zero free parameters | 37-38 | Derived |
| [NEW S38] Kapitza ratio = 0.030 | Geometry 33x faster than pairing | 38 | Structural |
| [NEW S39] GGE Lagrange multipliers | lambda_B2=1.459, lambda_B1=2.771, lambda_B3=6.007 | 39 | Analytic |
| [NEW S40] T_acoustic/T_Gibbs = 0.993 | Barcelo prescription, zero parameters | 40 | Structural |
| [NEW S42] Effacement ratio |E_BCS|/S_fold | 3e-7 | 42 | Structural |
| [NEW S42] sigma/m (CDM) | 5.7e-51 cm^2/g | 42 | Computed |
| [NEW S44] a_2^bos/a_2^Dirac = 61/20 | Representation-theoretic, tau-independent | 44 | Exact |
| [NEW S44] epsilon_H ratio invariance | Structural theorem: no rescaling changes epsilon_H | 44 | Exact |
| [NEW S45] Van Hove TRUE crossing T3-T5 | tau = 0.19104, delta_min = 3.27e-5 | 45 | Numerical |
| [NEW S45] Zubarev alpha formula | S_GGE/(S_max - S_GGE) = 0.410 | 45 | Derived |
| [NEW S46] Module dimensions tau-independent | dim(Omega^1_D) = 342 = 173+169 | 46 | Exact |
| [NEW S46] 13 pi Berry phases, Z_2 = -1 | Nontrivial Zak phase skeleton | 46 | Exact |
| [NEW S46] Gram matrix PSD theorem | Kinetic mass >= 0 for any Hermitian D | 46 | Exact |
| [NEW S47] Superfluid stiffness 24x anisotropic | rho_s(C^2)=7.96, rho_s(u(1))=0.33 | 47 | Computed |
| [NEW S47] Curvature-stiffness anti-correlation | r = -0.906 (p=0.002) | 47 | Structural |
| [NEW S47] K^{-2} texture spectrum | Goldstone theorem on fabric | 47 | Exact |
| [NEW S48] Leggett mode omega_L1 = 0.070 M_KK | Below pair-breaking at ALL tau | 48 | Computed |
| [NEW S48] alpha_s = -(1-n_s^2) from O-Z | Rigid, no free parameters | 48 | Structural |
| [NEW S48] Transversality theorem | 35 -> 31 TT modes at tau > 0 (4 C^2 constraints) | 48 | Exact |
| [NEW S49] Curvature sign-change hierarchy | K_sect=0 (0.537), Weyl=0 (0.895), Ric=0 (1.382) | 49 | Computed |
| [NEW S50] Leggett Q = 670,000 | All pair-breaking channels forbidden | 50 | Computed |
| [NEW S50] omega_L2/omega_L1 = phi_paasch at tau=0.211686 | Machine precision, 61-point scan | 50 | Exact |
| [NEW S50] w_a = 0 triple-locked | Trapping + integrability + frozen modulus | 50 | Structural |
| [NEW S51] K* = m_G/sqrt(J) = 0.087 M_KK | SA-Goldstone mixing threshold | 51 | Derived |
| [NEW S51] Convex combination theorem | n_s in [-1, +0.15] at K_pivot=2.0 | 51 | Exact |

> **[S116-W2 scope note — LIGHT-vs-HEAVY Leggett disambiguation; the entries above stay VERBATIM, this note scopes them].** The `LEGGETT-MODE-48` / `[NEW S48-S50]` below-pair-breaking + Q=670,000 SHARP results (rows above, and the §XV/summary rows `ω_L1 = 0.070 M_KK`) are CORRECT and belong to the **LIGHT dipolar Leggett mode** `ω_L1 = 0.070 M_KK = 0.1508·Δ_BCS` (`proven_1792`, "below pair-breaking at ALL τ", `DIPOLAR-CATALOG-49`) — it sits below BOTH its intra-band edge `2Δ_BCS` AND the inter-band sharp-mode ceiling `4.7308·Δ_BCS`. They MUST NOT be inherited by the **HEAVY Leggett-channel DM anchor** `m_LeggettDM = 11.97·Δ_BCS = 5.5571 M_KK` (S70 `LEGGETT-MOMENT-70`), which is a DISTINCT 79×-heavier object: under Convention M (mass) it sits `x^⊥ = m/E_edge^⊥ = 5.5571/2.196 = 2.53 > 1`, **ABOVE** the inter-band continuum edge `E_edge^⊥ = Δ_BCS + √3 = 4.7308·Δ_BCS` (S116 W2 landau × volovik, Sage-exact). The HEAVY anchor's survival is **Reading A** — CPT non-annihilation (BDI `[J, D_K]=0`) + GGE integrability (Ordered Veil, S95) + `Γ_grav < H₀` (LEGGETT-GRAV-DECAY-67, C11-CONDITIONAL) — **NOT below-edge** (the C11-conditionality is the tell; below-edge would be unconditional). Two-observable separation: survival ⊥ sharpness; below-edge SHARPNESS is the LIGHT mode's property only. See `falsifier-master-inventory.md` Row #79.compute-corrigendum-S116-W2-PROTECTION-MAGNITUDE-RESCOPE (the eq(15c) two-error correction + the √ρ_s-free sharp-mode ceiling).

---

## VIII. Selection Rules (Extended)

### Original (Session 23a)

| Pair | Coupling | Precision |
|:-----|:---------|:----------|
| V(Level 1 - Level 1) | 0 exactly | 7.1e-29 |
| V(Level 1 - Level 2) | 0.07-0.13 (grows with tau) | 2 sig figs |
| V(Level 1 - Level 3) | 0 exactly | 1.1e-29 |
| V(Level 2 - Level 2) | 0 exactly | 1.1e-28 |
| V(Level 2 - Level 3) | 0.01-0.03 | 2 sig figs |
| V(Level 3 - Level 3) | 0 exactly | 3.8e-30 |

### Branch-Level Selection Rules (Sessions 32-35)

| Rule | Value | Precision | Session |
|:-----|:------|:----------|:--------|
| V_eff(B_i, B_j) = 0 (Trap 4, Schur) | inter-branch | < 1e-55 | 32a |
| V_ph(real reps B1, B3) = 0 (Trap 5, J-reality) | within-branch PH | < 1e-14 | 32b |
| V(B1,B1) = 0 (Trap 1) | singlet self-coupling | 3.4e-29 | 34 |
| V(B1,B3) = 0 | singlet x adjoint | 5.8e-30 | 35 |
| V(q_7=+1/4, q_7=-1/4) = 0 | K_7 charge-conserving | 9.5e-29 | 35 |

---

## IX. Probability Trajectory (Extended)

```
Prior (theoretical):                     2-5%
After KO-dim=6 (Sessions 7-8):         10-15%
After SM quantum numbers (Session 7):   25-35%
After Baptista geometry (Session 17b):  40-50%
After Session 19d (TT discovery):       45-52%    <-- PEAK
After Session 20b (TT Casimir closed):  32-40%
After Session 21a (Ainur panel):        43% (panel), 36% (Sagan)
After Session 22d (clock closure):      40% (panel), 27% (Sagan)
=== K-1e DECISIVE CLOSURE (Session 23a) ===
After Session 23a:                       8% (panel),  5% (Sagan)
=== V-1 CLOSED (Session 24a) ===
After Session 24b:                       5% (panel),  3% (Sagan)
After Session 26 P1/P2/P3:              3-5% (panel), 2-4% (Sagan)
After Session 28 (KC chain):            7-10% (panel), 4-7% (Sagan)
After Session 29 (KC complete):         15-20% (panel), 3-5% (Sagan)
After Session 32 (RPA+WALL PASS):       ~18%
After Session 33 (TRAP PASS):           ~18%
After Session 35 (Unconditional BCS):   32% (Sagan 18-45%)
After Session 37 (Monotonicity theorem): 5-8%
After Session 38 (Ordered Veil):        TBD
After Session 39 (FRIED FAIL):          ~8-12%
After Session 42 (Geometric LCDM):      18% (Sagan)
After Session 44 (Sakharov, CDM):        23% (Sagan)
After Session 45 (q-theory CC PASS):     ~20%
After Session 49-50 (alpha_s crisis):    3-5%
After Session 51 (Anderson-Higgs):       2-4%
```

---

## X. Corrections & Retractions (Extended)

### Original (Sessions 17-28)

| What | Original | Corrected | Session |
|:-----|:---------|:----------|:--------|
| AZ class | DIII (T^2 = -1) | BDI (T^2 = +1) -- chiral, not Kramers | 17c |
| "4-5x coupling" | Inter-sector D_K coupling | RETRACTED: was Kosmann norm, not matrix elements | 22b |
| Berry curvature B=982.5 | Berry curvature | ERRATUM: was quantum metric. Berry = 0 exactly (W5). | 25 |
| a_6 "theorem" | All a_{2n} monotone | Downgraded to conjecture beyond a_6 | 27 |
| Baptista P_LZ = 0.97 | LZ transition probability | Retracted: LZ inapplicable (codim-1) | 28 |
| phi_paasch status | Physical prediction (BF=5) | Mathematical property (BF=2) | 28 |
| Tesla g*N(0) ~ 8-10 | Cross-sector modes counted | Corrected to 3.24 by block-diagonality | 22c |

### New Corrections & Retractions (Sessions 29-51)

| What | Original | Corrected | Session |
|:-----|:---------|:----------|:--------|
| [NEW S33-34] TRAP-33b V(B2,B2) | Frame V = 0.287 | RETRACTED: spinor V = 0.057. Different vector spaces. | 34 |
| [NEW S34] J operator formula | B = sigma_2^{x4} | C2 = gamma_1*gamma_3*gamma_5*gamma_7 (Cl(4)) | 34 |
| [NEW S39] GGE permanence | "Never thermalizes" | RETRACTED: V_phys 13% non-separable. Thermalizes in ~6 nat units. | 39 |
| [NEW S39] Schwinger-instanton duality | S_Schwinger = S_inst (identity) | RETRACTED: GL ratio 4.08. Numerical coincidence, not identity. | 39 |
| [NEW S42] S42 lambda_fs DM | 3.1e-48 Mpc (CDM) | RETRACTED: corrected to 89 Mpc (HDM). Full CDM-CONSTRUCT-44 supersedes. | 43-44 |
| [NEW S44] Euler deficit | deficit/|E_cond| = 1.000 | RETRACTED: actual 0.843. Shannon/FD mismatch. | 45 |
| [NEW S45] ALPHA-EFF 0.410 (Zubarev) | alpha = 0.410 | RETRACTED: Shannon entropy mismatch. Corrected range 0.7-1.2. | 46 |
| [NEW S46] S38 CHAOS-1 <r> | 0.321 (sub-Poisson) | CORRECTED to 0.439 (Poisson on unique levels). | 46 |
| [NEW S46] Zak phase topological | 13 pi-phases topological | RETRACTED S48: collapse at 0.1*eps_c. Index-tracking artifact. | 48 |
| [NEW S49] S48 analog horizons | Mach 54 superflow | RETRACTED: amplitude gradient, not phase gradient. No superflow. | 49 |
| [NEW S49] NEC boundary | tau = 0.778 | CORRECTED to tau = 1.382. | 49 |
| [NEW S50] S49 CMPP "Type II locked" | Riemannian Type II | CORRECTED: Lorentzian is Type D (complexified null frames). | 50 |

---

## XI. Session Productivity Ranking (Updated)

| Rank | Session | Key Permanent Results |
|:-----|:--------|:---------------------|
| 1 | 7-8 | KO-dim=6, SM quantum numbers, commutant structure |
| 2 | 22b | Block-diagonality theorem, b_1/b_2 triple confirmation |
| 3 | 35 | BCS 1D theorem, SU(3) anomalous curvature, unconditional chain, 3 closures |
| 4 | 37 | Structural monotonicity theorem, instanton gas, GPV, BCS-BEC crossover, 3 closures |
| 5 | 42 | Geometric LCDM (w=-1, CDM, NFW), 8 PASS, 4 FAIL, 8 new walls |
| 6 | 44 | Sakharov G_N, CDM construction, 61/20 exact, epsilon_H invariance, 31 computations |
| 7 | 50 | alpha_s theorem (5 proofs), Leggett Q=670k, phi crossing, Type D, sigma_8, 14 closures |
| 8 | 34 | [iK_7,D_K]=0, Schur on B2, Trap 1, J correction, TRAP-33b retraction |
| 9 | 17a | CPT hardwired, g_1/g_2 identity, 79,968 pairs |
| 10 | 40 | HESS-40 (27th equilibrium closure), T_acoustic agreement (0.7%), 11 gates |
| 11 | 45 | Q-theory BCS PASS (first CC mechanism), Taylor exactness, 15 structural results |
| 12 | 39 | N_pair=1 exact, B2 protection, analytic GGE, 3 S38 retractions, 20 computations |
| 13 | 51 | Anderson-Higgs impossibility, n_s>1 theorem, convex combination, SA mixing |
| 14 | 48 | Trace theorem, Leggett mode, transversality, 6 closures |
| 15 | 28 | Fusion: 7 publishable results, 4 walls, KC chain 4/5 PASS |

---

## XII. BCS Mechanism Chain Status (Updated Through Session 35)

| Link | Gate | Result | Key Number | Sessions |
|:-----|:-----|:-------|:-----------|:---------|
| I-1 | Spectral instability | **PASS** | d^2S = 20.43 | 28, 32, 35 |
| RPA | Thouless criterion | **PASS** | M_max = 1.674 (8x8) | 32b, 35 |
| Turing | Domain formation | **PASS** | W = 1.9-3.2x | 32b |
| WALL | Van Hove DOS | **PASS** | rho = 14.02, Z = 1.016 | 34, 35 |
| BCS | Pairing | **PASS** | E_cond = -0.115 | 34, 35 |

**Status**: 5/5 UNCONDITIONAL at mean-field, confirmed by exact diagonalization (S35).

**BUT**: Mechanism chain describes single-cell BCS. Framework viability requires connecting single-cell to 4D cosmological observables. This connection encounters:
- Effacement ratio 3e-7 (S42)
- 56-order scale hierarchy internal-to-external (S47)
- n_s crisis (10+ single-cell routes closed, S42-S51)

---

## XIII. Algebraic Trap Registry (Complete)

| Trap | Identity | Origin | Session |
|:-----|:---------|:-------|:--------|
| 1 | V(gap,gap) = 0 | Kramers (KO-dim 6) | 23a, 34 (confirmed) |
| 2 | F/B = const (UV) | Weyl's law | 21a |
| 3 | e/(a*c) = 1/16 | Trace factorization | 22c |
| 4 | V_eff(B_i,B_j) = 0 | Schur orthogonality (U(2)) | 32a |
| 5 | V_{ph}(real reps) = 0 | J-reality (KO-dim 6 + U(2)) | 32b |

---

## XIV. New Structural Categories (S29-S51)

### A. Nuclear/Condensed-Matter Structural Results

| Result | Value | Session |
|:-------|:------|:--------|
| Dense instanton gas S_inst = 0.069 | Tunneling 93%, barrier_0d = 0.0047 | 37 |
| Giant pair vibration omega = 0.792 | 85.5% of pair-addition strength | 37 |
| BCS-BEC crossover E_vac/E_cond = 28.8 | g*N(E_F) = 2.18 | 37 |
| BCS four-frequency architecture | omega_tau >> omega_att > omega_PV >> Gamma_L | 37-38 |
| Inverted Born-Oppenheimer | Geometry 33x faster than pairing | 38 |
| Pair vibration is Delta_N=+/-2, not phonon | Not a density wave | 38 |
| Nuclear analog: deformed ^24Mg (sd-shell) | Not ^16O | 38 |
| N_pair = 1 exact (8-mode IS the full singlet) | P(N=2) = 4.6e-33 | 39, 48 |
| B2 near-integrable island (<r>=0.401, g_T=0.087) | Superdeformed band analog | 40 |
| Leggett mode omega_L1 = 0.070 M_KK | Sharp (Q=670,000), undamped | 48-50 |
| Leggett IS 3He dipolar analog | omega_L1/m_required = 1.18 | 49 |
| B3 pairing entirely proximity-induced | Isolated B3: Delta = 0 | 46 |
| Pair transfer is a BLOCK property | R^2 = 0.002 (not k-dependent) | 46 |

### B. Gravitational/Cosmological Structural Results

| Result | Value | Session |
|:-------|:------|:--------|
| Acoustic Hawking T agrees with T_Gibbs to 0.7% | T_a/T_Gibbs = 0.993 | 40 |
| Geometric LCDM: w=-1 (28 decimals), CDM, NFW | Zero dark-sector parameters | 42 |
| Sakharov G_N from KK spectrum | 0.36 OOM at Lambda=10*M_KK | 44 |
| CDM by construction: T^{0i}=0 algebraic | 5 independent proofs | 44 |
| CC fine-tuning theorem | f width ~10^{-121} required | 44 |
| Q-theory BCS CC zero-crossing | tau* = 0.209, first CC PASS | 45 |
| Two-fluid DESI prediction | w_0 = -0.709, w_a = 0 exactly | 45 |
| sigma_8 = 0.799 viable | Between Planck and lensing | 50 |
| w_a = 0 triple-locked | Trapping + integrability + frozen modulus | 50 |

### C. Internal Manifold Geometry (S47-S49)

| Result | Value | Session |
|:-------|:------|:--------|
| Six curvature branches at fold | Hard, soft, protected, flat, two C^2-C^2 | 47 |
| Protected chain: q_7^2 = K(u(1),C^2) = 1/16 | Exact, all tau | 47 |
| Superfluid stiffness tensor 24x anisotropic | rho_s(C^2)=7.96, rho_s(u(1))=0.33 | 47 |
| K^{-2} texture spectrum (Goldstone) | n_s = 1.0 (Harrison-Zel'dovich) | 47 |
| Condensate identity peak contrast 3.14e6 | Z_3 center destructive interference | 47 |
| Josephson hierarchy: J_C2=0.933, J_su2=0.059 | 16x anisotropy | 47 |
| 4-zone Penrose diagram classified | Physical universe Zone I (tau in [0.19, 0.22]) | 49 |
| Triple-layered cosmic censorship | Energy + friction + no trapped surfaces | 49 |
| Curvature sign-change hierarchy | K_sect=0 (0.537), Weyl=0 (0.895), Ric=0 (1.382) | 49 |

### D. Observational Predictions (Status as of S51)

| Prediction | Value | Status | Session |
|:-----------|:------|:-------|:--------|
| w = -1 exactly | w_0 = -1 + O(10^{-29}) | CONSISTENT with LCDM; w_a = 0 possibly EXCLUDED by DESI | 42, 50 |
| r (tensor-to-scalar) | 3.86e-10 | Unobservable (9.3e7x below BICEP) | 44 |
| sigma_8 | 0.799 | VIABLE (between Planck 0.811 and lensing ~0.77) | 50 |
| n_s | 0.965 achievable at K < K* = 0.087 | CONDITIONAL on K_pivot mapping (S52 master gate) | 51 |
| alpha_s | n_s^2 - 1 = -0.069 (O-Z), or ~-0.035 (SA mixing) | O-Z at 6 sigma from Planck; SA mixing within window | 49-51 |
| f_NL | 0.014 | CONSISTENT with Planck (far below bound) | 42 |

---

## XV. Open Questions (Post-S51)

1. **K_pivot scale mapping** -- Does k_CMB = 0.05 Mpc^{-1} map to K_fabric < 0.087 M_KK? This requires tau_i <= 1.7e-5. EFOLD-MAPPING-52 pre-registered as S52 master gate.
2. **Cosmological constant** -- 110.5-order gap persists. Q-theory BCS crossing exists at tau* = 0.209 but requires fabric-level pair number.
3. **n_s from multi-correlator mixing** -- SA-Goldstone additive mixing works at K < K* but the physical K_pivot is undetermined.
4. **Off-Jensen moduli exploration** -- Full 5D space beyond U(2)-invariant family is uncharted.
5. **Self-consistent HFB on SU(3)** -- Deferred since S41. D_K -> BCS -> BdG -> tau* loop never closed.

---

*Catalog compiled from: sessions/permanent-results-registry.md (S1-S28 baseline, 340 lines), summary/session-29-final.md through summary/session-51-final.md, summary/session-43-quicklook.md through summary/session-46-quicklook.md, summary/atlas-01-session-timeline.md, and MEMORY.md. All gate verdicts taken from source documents. Cross-referenced against Sagan verdicts (canonical authority) and synthesis files.*

---

## XVI. S52-S88 §VII Registry Slot Inventory (NEW)

> **Provenance**: Section added 2026-05-09 per S88 atlas-uplift workshop. The S52-S88 era added ~60 substantive registry landings to `sessions/permanent-results-registry.md` under §VII slot identifiers. This section catalogs them with status, author(s), and substrate-IS framing per `phononic-framing.md` §"IS Space, Not IN Space".

### Status legend

- **PERMANENT** (STAGE-3): Stage-2 PASS-AND complete or proven structural identity; immune to retraction
- **STAGE-1-CANDIDATE**: registered with substantive derivation; pending Stage-2 two-agent cross-axis verify per `joint-theorem-promotion.md`
- **CANDIDATE-PENDING**: anchor-sweep / multi-year experiment blocking promotion
- **INFO**: NEEDS-DECISION or FAIL-with-remediation; documented but non-binding
- **CORRIGENDUM**: Option-A `supersedes`-tagged successor entry per `gate-verdicts.md §"Option A — sig_5 remediation"`
- **OPEN**: reserved-but-unlanded slot OR NEEDS-COMPUTATION pending derivation
- **DEPRECATED**: superseded by another slot

### XVI.A. Headline cross-pillar bridge corpus (K=3 MANDATORY)

The cross-pillar bridge corpus per `cross-pillar-bridge-anatomy.md` MANDATORY at K=3 is the framework's flagship structural development S86-S88. Three calibration corpus instances:

| §VII slot | Theorem name | Landing session | Author(s) | Status |
|:----------|:-------------|:----------------|:----------|:-------|
| **§VII.AF.1.OP-PROJ** | Pillar III ↔ Pillar IV bridge (HKR-image; 0.0095% F_4 strict at L_max=10; L^{-3} algebraic envelope at d=4 = 0.10%; Level-3/Level-2 = 0.0950, 10× inside envelope) | S87 W5-1 (S86 W-5 origin) | volovik (V_input) + connes (C_output) — SOURCE-DOUBLE-CITE-CO-PRIMARY | PERMANENT-at-Hochschild-cohomology-level (PASS-UNCONDITIONAL per W-5 Workshop Verdict L2572-2587); Stage-2 cross-axis verify queued S89 per `joint-theorem-promotion.md` 4-stage pathway (atlas-11 §IV.1 cross-link) |
| §VII.AF.1.STATE-PROJ | Pillar III ↔ Pillar IV STRUCTURALLY-ORTHOGONAL-COMPANION; allocated as state-projection counterpart | S88 W11 V.4 | mack | OPEN (PENDING-VERIFICATION) |
| §VII.AG.1 | T7 ↔ S67 cyclic-fold quotient (HKR ∘ Connes-Karoubi; substrate-distance-1 Mellin pole s=3; V_4 cyclic-fold; 0.0095% residual on T6 numbers) | S87 W6-1 (S86 W-6 origin) | lizzi + volovik | **STAGE-3-PERMANENT** (K4; promoted S105 blind Stage-2 PASS-AND 18/18, connes × transit-dynamics; audit `402d893c`; Level-3 < Level-2 exact-rational 10.55× inside envelope; atlas-04 §X K4; atlas-07 tag synced S109 MAINTAIN) |
| §VII.AG.2 | T7 ↔ S67 PASS-quotient-isomorphism with three sharpening clauses | S86 W-6 | lizzi + volovik | READY-TO-INSTALL conditional |
| §VII.AG.4 | Z_3 gauge-sector signature (512 = (2/3) × 768 plaquette count) | S86 W-6 | volovik | READY-TO-INSTALL appendix tag |
| §VII.AG.5 | D1 gauge-counting correction (n_frust ∈ {0, 2}, NOT {0, 3}) | S86 W-6 | volovik + lizzi | READY-TO-INSTALL |
| §VII.AG.6 | Cross-cluster Mellin-Wick V_4 commutation theorem ([M, W]_{c_i, c_j} = 0 IDENTICALLY at all 16/16 V_4-coset pairs; identifies Klein-V_4 not Z_4) | S87 W6-5 | lizzi + volovik | PERMANENT |
| **§VII.W-3.LAB** | 3rd cross-pillar bridge calibration instance (Lancaster MCT-3 inheritance kernel falsifier; rank-2 ker(ι_*); 4-gate Class A NULL + Class B cohomology-asymmetry ratio 7.3250 ± 0.1%) | S88 W4a-17 | volovik PRIMARY + landau + connes (CO-AUTHORS) | **STAGE-3-PERMANENT** (K5; promoted S100a blind Stage-2 PASS-AND 11/11, vdd × landau; audit `89eab199edaa7f90`; Level-3 lab anchor deferred-but-pre-registered 2027-2030; atlas-04 §X K5; atlas-07 tag synced S109 MAINTAIN) |
| §VII.W-3.ALGEBRAIC | A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) Wedderburn-Artin Frobenius rescue class theorem (algebraic side) | S88 W4a-17 | connes + volovik | PERMANENT |
| §VII.W-3.SUBSTRATE | Substrate-IS realization of Wedderburn-Frobenius rescue (axiom-5 fail at M_3 sector resolved via χ-killing per clause ii) | S88 W4a-17 | connes + volovik | PERMANENT |
| **§VII.AJ.OP-PROJ** | Operator-projection: substrate-IS universal-large-negative-R prediction R_∞ ≈ −1.892 ± 0.001 (multiplicity-weighted Mellin-pole-window observable saturating monotonically at L_max → ∞; algebra-INVARIANT) | S88 W7 + W10 | volovik + mack | STAGE-1-CANDIDATE |
| §VII.AJ.STATE-PROJ | State-projection: BCS-physics-grounded substrate-IS image of R_3HeB_lit = +0.03536 at polycritical pressure P_pc = 21.22 bar (algebraic shape (a−b)/(a+b); algebra-DEPENDENT) | S88 W7 + W10, S116 W7 | landau (PRIMARY) + volovik + connes | REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (S116-W7-ALGEBRA-AXIS: Level-1 identity-class ORTHOGONAL ⊥ OP-PROJ CONFIRMED, value-free, first PHYSICAL 3He-B instance; Level-3 anchor HELD Track-B — substrate_first_SC_ratio_available=False, value IS R_3HeB_lit, Δ_BCS-cancels, vanishing-test FAIL; literal SC_corr_A/B route BLOCKED no-A-sector; discharge → CF-S117-STATEPROJ-INTER-SUMMAND) |
| §VII.AJ.partition-stability | 4-stratum (2,4,8,6) cardinality vector at τ_fold = 0.190 (Friedrich-Bär saturation theorem; structural-saturation theorem closing finite-truncation artifact concern) [S116-W9-SATURATION-ADJUD SCOPE: the FB inequality \|λ\|_min(p,q) ≥ η_FB_lower·√(C₂+1) is a Casimir LOWER bound — saturation reach = the bottom-K floor + the bulk low-\|λ\| moments (incl. the Zubarev numerator mean_Z); structurally SILENT on λ_max (the Weyl edge, N(λ)~λ^d, ∂λ_max/∂L = 0.375). Do NOT cite FB-saturation to declare a λ_max-tail-sensitive moment "saturated": at p+q=15 the bottom-64 floor is FB-null (max\|diff\| = 0.0e+00) WHILE the branch-(iv) λ_max-driven w0 Zubarev moment SHIFTS (ρ_B = mean_Z/λ_max − 1; bottom-K ⟷ mean_Z FB-saturated ⊥ w0-shift ⟷ λ_max Weyl-drifting). Anchor: S116-W9-GTBUILDER-L15 INFO, audit_sha256 94ed48e7….] | S87 W11-2 + W11-3, S116 W9 | connes + mack — SOURCE-DOUBLE-CITE-CO-PRIMARY | PERMANENT |

### XVI.B. Algebra-axis orthogonality + Mellin-Dirichlet headline theorems

| §VII slot | Theorem name | Landing session | Author(s) | Status |
|:----------|:-------------|:----------------|:----------|:-------|
| §VII.U.1 | **Mellin-Dirichlet finite-spectrum identity** (FINITE-VECTOR class anchor; M[Tr e^{-tD²}](s/2)/Γ(s/2) = ζ_D(s); rel_diff = 0e+00 at L_max=12 across 31.9M weighted eigenvalue contributions) | S86 W-1 | connes + lizzi — SOURCE-DOUBLE-CITE-CO-PRIMARY | PERMANENT |
| §VII.U.2 | **Algebra-axis orthogonality 4-corner classification** (Cell I = INVARIANT × s=3; Cell II = INVARIANT × s=4; Cell III = DEPENDENT × s=3; Cell IV = DEPENDENT × s=4; cross-corner co-primary FORBIDDEN; cross-pole co-primary FORBIDDEN) | S88 W5b-45 | lizzi PRIMARY + connes (CO-AUTHOR clauses c, d) + mack (sole-writer) | **STAGE-3-PERMANENT** (K1; promoted S105 blind Stage-2 PASS-AND 5/5 PARENT clauses, vdd × kitaev; audit `7c535495`; Var_a SUB-row independently permanent since S92 W4-7; atlas-04 §X K1; atlas-07 tag synced S109 MAINTAIN) — K=3 MANDATORY enforcement at registry layer |
| §VII.U.6 | **T5 Mellin-Strip / Convergence-Cone Theorem** (INFINITE-VECTOR class; Zubarev profile M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s); pole set S_d = {0, 2, 4, 6, 8} for SU(3) at d=8; max_rel_err = 8.066e-28) | S86 W-1 | connes + lizzi | PERMANENT |
| §VII.U.6.k1-vs-k2 | k=1 (Wick-decomposable) vs k=2 (pair-cumulant) channel counting distinction | S87 W2 R3 / S88 W6b-56 | lizzi | PERMANENT |
| §VII.N | **Three-Layer Regulator Theorem (HKR-Connes-Lizzi-VdD)** (L1-axiomatic / L2-substrate-action / L3-observable three-layer regulator stratification on (A_K, H_K, D_K)) | S84 W2a-11 | connes + lizzi + van den Dungen | PERMANENT |

### XVI.C. F_4-MB structural wall family + α_s tension family

| §VII slot | Theorem name | Landing session | Author(s) | Status |
|:----------|:-------------|:----------------|:----------|:-------|
| §VII.Z | F_4-MB Structural Wall Family (a_0-Unsuppressed-at-LMAX10; |Λ_CC^MB|/|a_0^trunc| ≤ 0.5 fails worst-case Zubarev 9.4557; closes Pillar-III multiplier-algebra route to CC-suppression on F_4) | S86 1a-S1 | gen-physicist + volovik + connes | PERMANENT |
| §VII.V.A | WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A | S86 1a-S1 | connes | PERMANENT |
| §VII.AB.1 | α_s 11.31σ Tension + S50-S51 Sign-AND-Magnitude Lock under C1 identity α_s = n_s² − 1 (sign and magnitude are the SAME lock) | S86 W-2 | mack + volovik + connes — SOURCE-DOUBLE-CITE-CO-PRIMARY | PERMANENT |
| §VII.AB.2-§VII.AB.7 | Triple-Protection Reading at CMB pivot (K-homogeneity + GAP-ANTIJENSEN-65 + sub-threshold inter-band coupling); 7-row family with K-homogeneity ODE | S86 W-3 | volovik + transit-dynamics | PERMANENT structural |
| §VII.AB.8 | 3He-B Aalto LTL Lab-Analog Multi-Axis Falsifier (9-row lab-falsifier suite: SW1 58.9589 MHz at λ_6, SW2 364.5177 ppm at λ_7, SW3 1.4250 s^{-1} at λ_8 — UNIQUE λ_8 channel) | S86 W-3 + S86 W11-C5/C6 | mack-cosmic-bridge sole-writer | CANDIDATE-PENDING (multi-year LTL liaison; 5-yr horizon 2031) |
| §VII.X.1 | α_s = n_s² − 1 registry upgrade (Sage-exact rational form: -8587279/100000000 at u_pivot = 19649/351; substrate ceiling \|δα_substrate\| ≤ 8.65e-5 absolute; hardens 11.31σ → 16.90σ vs Fairbairn-2025) | S85 W2-9 | connes | PERMANENT |
| §VII.X.W4-1 | 9-cell tensor 3-channel bridge R^{(k)}_{p,q}(L_max=10) at k ∈ {1, 2, 3}; envelope L^{-α_k} with α_k = 2k-1 | S87 W4-1 | connes + lizzi | **STAGE-3-PERMANENT** (K7; promoted S108 W2-2 `S108-VIIXW41-W7A75-OEFORM` `25ef7594`; S107 W2-2 blind 3-channel Stage-2 PASS-AND k=1/2/3 + q=II Element-2 OE-form named-projector retrofit; 3rd blind-verified cross-pillar bridge; atlas-04 §X K7; atlas-07 tag synced S109 MAINTAIN) |
| §VII.X.2-NECESSITY | M2 axiom structural source for Λ_SA finite-L residual | S87 W1a-6 | connes | STAGE-3-PERMANENT (promoted S108 W2-4 `S108-VIIX2NEC-STAGE2to3-PROMOTION`: S107 W2-3 blind cross-axis Stage-2 PASS-AND on every necessity clause [`4d98f916…`] + 6-of-6 full-64-char anchor-SHA harvest VERIFIED on disk via the S88-LAMBDA-SA-* successor family; atlas-04 K9 + open-channel-ledger §C K9 flipped to STAGE-3-PERMANENT in lockstep; supersedes the 2026-06-12 down-correction) |

### XVI.D. Path-H/Path-C classification family + STAGE-1-CANDIDATE joint theorems

| §VII slot | Theorem name | Landing session | Author(s) | Status |
|:----------|:-------------|:----------------|:----------|:-------|
| §VII.AC.1 | Path-H/Path-C multi-valued classification (a) — first explicit V+C SOURCE-DOUBLE-CITE-CO-PRIMARY structure | S87 CF-20 | lizzi + transit-dynamics | **STAGE-3-PERMANENT** (K2; promoted S108 W2-1 `S108-ACFAMILY-S3-MELLIN-PARSE-TREE` `8ca8f479`; S107 W2-1 blind CO-PRIMARY+binary JOINT spine PASS-AND + substrate-first ζ_{D_K} Mellin residue/Corner-III parse-tree discharged the s=3 audit-substituted leg; atlas-04 §X K2 + open-channel-ledger §C K2 synced; supersedes the 2026-06-12 down-correction; atlas-07 tag synced S109 MAINTAIN) |
| §VII.AC.2 | B1/B2 block decomposition uniqueness theorem | S86 W-3 | volovik + connes | PERMANENT |
| §VII.AC.3 | Rank-2 product detector orthogonality theorem (LiteBIRD × LISA factorization) | S86 W-3 | mack + qa | PERMANENT |
| §VII.AC.4 | V1+C1 sequential-chain derivation of classification (a); calibrates SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure | S87 CF-20 | volovik + connes | **STAGE-3-PERMANENT** (K11; promoted S108 W2-1 `S108-ACFAMILY-S3-MELLIN-PARSE-TREE` `8ca8f479`; S107 W2-4 blind sequential-chain CO-PRIMARY direction Stage-2 PASS-AND + Corner-III parse-tree/a_4^ζ→a_2 re-pin discharged the s=3 audit-substituted leg; atlas-04 §X K11 + open-channel-ledger §C K11 synced; supersedes the 2026-06-13 down-correction; atlas-07 tag synced S109 MAINTAIN) |
| §VII.AH | Joint F_2-class Path-(c) theorem (A_5 4-class projection s=3; 6-clause statement with 4 corrigenda; clauses c+d JOINT) | S87 W9a-1 | lizzi + transit-dynamics | **STAGE-3-PERMANENT** (K10; promoted S90 W2 CF-20; Stage-2 PASS-AND landed S89 W4-7, audit `4fcd7d29`; calibration corpus instance #1 of joint-theorem-promotion 4-stage pathway; atlas-04 §X K10 — prior STAGE-1-CANDIDATE Corrigendum-2 tag was stale, backfill-corrected at S109 MAINTAIN) |
| §VII.AM | Universal Lock Condition (3-clause: pixelation lock + effacement lock + Page-time lock; calibration corpus N=3 — J3 BH-horizon + S58 Γ_eff = 0.99970 + W1b2-64 cascade-tail Page-time non-activation) | S88 W1b2-65 | hawking (PRIMARY) + transit-dynamics + connes | **STAGE-3-PERMANENT** (K6; promoted S100a three-agent Stage-2 PASS-AND 9/9, lizzi + volovik + schwarzschild-penrose; audit `6dc0f374ffd3ee4e`; atlas-09 Suspected flag CLEARED; calibration corpus instance #2 of joint-theorem-promotion; atlas-04 §X K6 — prior STAGE-1-CANDIDATE tag was stale, backfill-corrected at S109 MAINTAIN) |

### XVI.E. Substrate-IS partition + moduli-deformation results

| §VII slot | Theorem name | Landing session | Author(s) | Status |
|:----------|:-------------|:----------------|:----------|:-------|
| §VII.AD | Δ_0 Localization Formula (V_4 character on 4-stratum partition; Δ_0 = 4·c_{σ⁻¹((-1,-1))} on substrate (2,4,8,6) at τ_fold; QQ-exact) | S88 W2-8 | connes + volovik (CO-AUTHORS) + gen-physicist | **STAGE-3-PERMANENT** (K3; promoted S106 blind Stage-2 PASS-AND {a,b,c}, vdd × kitaev; audit `ac0bfe80`; kitaev proved the localization over GENERIC QQ, subsuming the 576-instance sweep; remains Level-1 single-τ-slice substrate-IS calibration #1 per phononic-framing.md; atlas-04 §X K3; supersedes the 2026-06-12 down-correction; atlas-07 tag synced S109 MAINTAIN) |
| §VII.AE | Moduli-Space τ-Asymmetry of Substrate Partition Cardinality Vector (negative-side anticrossing-swap at δ_τ_crit_neg = -0.0750 ± 0.005; positive-side stratum-coalescence at δ_τ_crit_pos = +0.175 ± 0.05; 2.33× asymmetry ratio) | S88 W2-9 | gen-physicist | PERMANENT (Level-2 moduli-deformation substrate-IS observable) |
| §VII.K-PROP.W10-4 | ρ_∞ permanent-wall (substrate-distance-2 pole s=4); ρ(L) = c_0 + α/L² + β/L⁴; ρ_∞ = -0.8103647022669215; structurally IRRATIONAL per CC2 PROVEN | S87 W10-2 | connes | PERMANENT |
| §VII.K-PROP-W8.CELL-OCCUPANCY | cutoff_AL2010 / cutoff_sqrt L2 status update | S86 W-8 | mack + connes | READY-TO-INSTALL |
| §VII.K-PROP-HK-2 | Windowed Pauli-Villars-as-Seeley-DeWitt refinement | S88 W11-134 | gen-physicist | PERMANENT |
| §VII.AR | LEVEL-DRESSED rank-ordering at substrate-distance-2 pole s=4 (under PRIMARY-vs-SCHEMATIC level discipline; cross-regulator-spread metric) | S88 W7a-74 V.5 | gen-physicist + connes | CONDITIONAL (on A.36 Reading A WIN swap-survives ≥4/5) |
| §VII.K-DUAL.LEVEL-DRESSED | Companion to §VII.AR | S88 | gen-physicist | PERMANENT |

### XVI.F. P-v2 HP^1-content-distinct + Mellin-cone supplementary

| §VII slot | Theorem name | Landing session | Author(s) | Status |
|:----------|:-------------|:----------------|:----------|:-------|
| §VII.P′ | (η = 0, GV ≠ 0) joint-probe official landing on (C_H, C_epsH) parity-twin pair; Bulletin #1 CONFIRMED-DEMOTED-SCHEME-DEPENDENT, Bulletin #2 CONFIRMED-PROMOTED-PARITY-BLINDNESS (composite verdict; Class-(c) PIN-DRIFT-FROM-STALE-SOURCE calibration) | S86 W-11 | lizzi + connes | PERMANENT |
| §VII.AF.2 | §VII.P-v2 HP^1-content-distinct refinement (replaces failed S86 W9 C24 HP^0-content-distinct attempt) | S87 W5-4 | connes | PERMANENT (via mechanical-edit remediation) |
| §VII.AF.3 | T6 substitution PROMOTION to PASS-UNCONDITIONAL | S86 W-5 | volovik + connes | NEEDS-DECISION |
| §VII.U.7 | PER-EVAL FINITENESS PRE-REGISTRATION (W0-20 apex + W0-7-MB rho-fit per-evaluation finiteness check for FINITE-VECTOR observables) | S87 W1a-3 | lizzi | PERMANENT |

### XVI.G. Other S52-S88 PERMANENT registry landings

| §VII slot | Theorem name | Landing session | Author(s) | Status |
|:----------|:-------------|:----------------|:----------|:-------|
| §VII.B | Two-Layer Obstruction + HP^1 Cohomology Stability | S86 W1a-1 | (collaborative) | PERMANENT |
| §VII.R | NCG-Structural-Exclusion Meta-Theorem (3-signed) | S86 W1a-2 | connes | PERMANENT |
| §VII.S | Perturbative-Ledger Immunization Family (6 Φ-branches) | S86 W1a-3 | connes | PERMANENT |
| §VII.T | Mellin Strip / Convergence Cone (sponsored, S85 W0-S6 origin; lifted into §VII.U.6 at S86) | S85 W0-S6 | lizzi-spectral-functional-theorist | PERMANENT (cross-link) |
| §VII.AA | Layer-3 \|ρ\| Analytic Closed-Form Reduction (5-regulator atlas) | S86 W12-4 | connes | PERMANENT |
| §VII.M.W10-3 | van-Hove-cusp non-stationarity uniqueness theorem (ASSERTS tau_fold = 0.190 as an imported premise per convention=canonical_constants-S85-freeze; PROVES only existence + non-stationary character dS/dtau != 0 + multiplicity-uniqueness — LOCATION-free; the cusp LOCATION is the distinct functional tau_cross_van_hove = 0.191038, registry §VII-B.TAU-CROSS-VAN-HOVE, S114 W-1 output (iii); 0.190 = 19/100 is the rational anchor, non-fungible with 0.191038) | S85 W10-3 | connes + lizzi | PERMANENT |
| §VII.O.W4 | f_NL_folded pathway adjudication (3-pathway pinning: equilateral 0.0547 / GGE-folded 0.129 / analytic-template 0.7685) | S86 W-4 | gen-physicist + transit-dynamics | PERMANENT |
| §VII.P | Borel-Summability Floor Theorem (W9-1; S_inst/Borel_thr = 5.58e+4 across τ range) | S85 W9-1 | gen-physicist | PERMANENT |
| §VII.Q | F_amp^3PI Factorization-Invariance Theorem (W9-2; machine-epsilon identity 2.22e-16 across 5-regulator atlas) | S85 W9-2 | gen-physicist | PERMANENT |
| §VII.W | First Cross-Pillar Bridge Theorem (Pillar III ↔ Pillar IV; HP parity-grading orthogonality of HP_*(A_F)) | S86 W-5 | volovik PRIMARY + connes CO-AUTHOR | PERMANENT |
| §VII.AS | Geometric-Resummation Closure | S88 W18 W6a-51 | gen-physicist | PERMANENT |
| §VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE | First fb_pair(M) construction at S86 W-7 (per `epistemic-discipline.md §"Forward-Backward Inference Closure"`) | S86 W-7 | gen-physicist | PERMANENT (methodology-floor) |

### XVI.H. Promotion-gap & deprecated slots

| §VII slot | Status | Notes |
|:----------|:-------|:------|
| §VII.AT | OPEN (recommended for S89+ housekeeping per atlas-08 Q34) | W11 Volovik CC Tracking Wall (DILUTION-CC-66) currently anchored at `framework-cc-oom.md` + `falsifier-watchlist.md`; lacks dedicated §VII slot. Recommend §VII.AT allocation (next free letter post-§VII.AS at S88 W18 W6a-51). |
| §VII.AN | RETRACTED-anchor-structure (S88 W-15 V.6 cross-corner conflation retraction per atlas-09 Item 41); ANCHOR-1 + ANCHOR-2 retained but reclassified from CO-PRIMARY to STRUCTURALLY-ORTHOGONAL-COMPANION | atlas-09 Item 41 calibration corpus instance #1 of `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"` clause 4 |
| §VII.P → §VII.AF.2 v2 | DEPRECATED (S86 W9 C24 HP^0-content-distinct attempt superseded by §VII.AF.2 HP^1-content-distinct at S87 W5-4) | atlas-09 Item 39 cross-link |
| §VII.Y → §VII.S.C-eta + §VII.S.C-theta | DEPRECATED placeholder; sub-rows relocated to §VII.S parent on 2026-04-26 | Registry hygiene |

### XVI.I. Aggregate (S52-S88)

| Status class | Count | Notes |
|:------------|:-----:|:------|
| PERMANENT (STAGE-3) | 63 | Includes Level A-E novel + S63 T1-T17 + S64-S66 structural + ~30 new S52-S88 §VII slots + the 11 K-cohort joint theorems promoted S90/S100a/S105/S106/S108 (K1 §VII.U.2, K2 §VII.AC.1, K3 §VII.AD, K4 §VII.AG.1, K5 §VII.W-3.LAB, K6 §VII.AM, K7 §VII.X.W4-1, K9 §VII.X.2-NECESSITY, K10 §VII.AH, K11 §VII.AC.4, K12 §VII.BZ) — atlas-07 cohort table synced to canonical at S109 MAINTAIN; **K12 §VII.BZ enumeration added at S110 (HK-ATLAS07-COHORT)** — K12 was promoted S106 STAGE-3-PERMANENT (blind Stage-2 PASS-AND `566cdcb5`; listed atlas-04 §X) but omitted from this K-cohort enumeration at S109 MAINTAIN; the aggregate STAGE-3 total reflects the canonical §VII census (K12 within it; the S110 fix is enumerative, not additive) |
| STAGE-1-CANDIDATE | 1 | **§VII.AF.1.STATE-PROJ (K8) only** — PENDING-VERIFICATION, no dispatch-ready Stage-2 gate; the lone remaining joint-theorem-cohort holdout. K1-K7,K9-K12 ALL promoted STAGE-3-PERMANENT (S90/S100a/S105/S106/S108) and moved to the PERMANENT row above; atlas-07 cohort table reconciled to the canonical permanent-results-registry + atlas-04 §X + open-channel-ledger §C at S109 MAINTAIN (prior "11" count lagged S90-S108 promotions); K12 §VII.BZ enumeration completed at S110 (HK-ATLAS07-COHORT) |
| CANDIDATE-PENDING | 1 | §VII.AB.8 (multi-year Aalto LTL liaison; 5-yr horizon 2031) |
| INFO | 2 | §VII.AF.3, §VII.W-2 |
| CORRIGENDUM | 2 | §VII.AN-CORRIGENDUM, §VII.AO-CORRIGENDUM (Option-A `supersedes`-tagged successor entries per `gate-verdicts.md`) |
| OPEN | 4 | §VII.AG.2 (READY-TO-INSTALL conditional), §VII.AG.3 (DEFERRED ~9 months), §VII.AJ (parent), §VII.AJ.STATE-PROJ (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION, S116-W7), §VII.AF.1.STATE-PROJ (companion slot allocation) |
| DEPRECATED | 2 | §VII.P → §VII.AF.2 v2; §VII.Y → §VII.S.C-eta + §VII.S.C-theta |

**Total**: ~60 substantive landings; ~22 distinct S88 slot landings; full count includes reserved/deprecated slots = 66 distinct slot rows.

**By landing session**: S83 = 2; S84 = 4; S85 = 5; S86 ≈ 28; S87 ≈ 12; **S88 ≈ 25**.

**By PRIMARY author**: connes-ncg-theorist 19; lizzi-spectral-functional-theorist 8; volovik-superfluid-universe-theorist 4; gen-physicist 5; knowledge-weaver 2; hawking-theorist 1; orchestrator-direct ~4; mack-cosmic-bridge sole-writer ~9 (technical content co-authored per individual rows).

### XVI.J. D3 audit knowledge.db round-trip status (S88-current)

Per atlas-07 materials packet Section 2 round-trip audit: ~37 of 66 §VII slots **lack direct knowledge-MCP slot-card entries** (PARTIAL or NO hit on most non-headline slots). This is a methodology-floor gap routed to atlas-08 Q32 (D3 audit knowledge.db round-trip). Remediation: refine `tools/extract_entities.py` regex to detect §VII.X.Y nested-slot structure (sub-slots like §VII.AF.1.OP-PROJ, §VII.K-PROP-W8-LAYERED currently surface only as PARTIAL or NO hits); rerun `/weave --update --db-sync` Phase 6.

**Slots with confirmed YES knowledge.db hits** (~8): §VII.M, §VII.N, §VII.W, §VII.W-3.ALGEBRAIC + .SUBSTRATE, §VII.W-3.LAB, §VII.X.1, §VII.X.W4-1, §VII.AD, §VII.AF parent CAT slot, §VII.AF.1.OP-PROJ, §VII.K-PROP.W10-4.

**Slots with PARTIAL coverage** (~21): FTS5 indexed but no theorem-table slot-card structure; registry text queryable via `mcp__knowledge__.search_knowledge` but not via `list_entities("theorems")` with proper slot-id/status/precision metadata.

**Slots with NO direct hits** (~37): the remediation queue for `/weave --update` Phase 6 entity extraction post-fold.

### XVI.K. Per-Bulletin-per-pole Level-1/2/3 ladder corpus (S88 W10-119 extension)

Per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` (intra-pillar Pillar-VII Mellin-cone Bulletins; SUGGESTION at K=3 cohomology-class-distinct, MANDATORY-pending pole-distinct K=3):

| Bulletin / slot | Substrate-distance pole | Level-1 (cohomology-class identity) | Level-2 (algebraic envelope) | Level-3 (empirical anchor) |
|:----------------|:------------------------|:------------------------------------|:-----------------------------|:-----------------------------|
| §VII.K-PROP.W10-4 ρ_∞ permanent-wall | s=4 (substrate-distance-2; fermionic-signed-residue) | ρ_∞ structurally IRRATIONAL per CC2 PROVEN; PERMANENT-WALL classification | simple-pole fit `ρ(L) = c_0 + α/L² + β/L⁴`; L^{-2} dominant convergence at d=4 | ρ_inf_full_f64 = -0.8103647022669215 (S87 W10-2; α = 29.916, β = -662.24, R² = 0.99995) |
| §VII.U.1 Mellin-Dirichlet identity | s=3 (substrate-distance-1; apex-universal anchor) | Mellin-Dirichlet identity at substrate-distance-1 pole; (A)-class pure-Mellin-support per F_4 | L_max-stability rel_diff = 0e+00 (S86 W-1 / S87 W1a-4 PASS) at L_max=12 | bit-identity stability across atlas members; (A)-class anchor `M^{(ζ)}_3 ≈ 2.97e-3` at L_max=10 |
| §VII.AR LEVEL-DRESSED rank-ordering | s=4 (same pole as W10-4 but distinct cohomology-class structure) | Rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at s=4 IS REGULATOR-PARAMETER-dependent under the PRIMARY-vs-SCHEMATIC LEVEL discipline | pole-specific α(s=4) per Casimir-bound saturation argument | rank-ordering value pinned in §VII.AR registry entry |

Forward enforcement (S89+ Pillar-VII Bulletin-class entries at distinct poles s ∈ {5, 6, 7, ...}) MUST declare substrate-distance pole index, Level-1 classification (regulator-invariance status: FI / RD / MIXED + structural identity: rational / irrational / structurally-IRRATIONAL-per-CC2-analog), Level-2 envelope cite pole-specific α(s) AND Casimir-bound or Friedrich-Bär saturation argument, Level-3 anchor at L_max=10 OR analytic limit per pole-specific saturation theorem.

### XVI.L. Cross-link to atlas-11 + atlas-12 (NEW atlases)

The cross-pillar bridge corpus (Section XVI.A above) is jointly cited by atlas-11 (cross-pillar-bridge-corpus, NEW) and atlas-07 (here). The methodology-floor walls (PRU Class 8.4-8.6 advisory; Hybrid Independence Test K=1; Layer-separability carve-out K=1; Closing-Paragraph-Coherence audit pattern K=1; substrate-input-orthogonality K=1; reviewer-machinery-orthogonality K=1) are jointly cited by atlas-12 (methodology-floor, NEW) and atlas-04 (assumptions §VIII Methodology-Floor Walls). The 4-stage joint-theorem-promotion pathway is jointly cited by atlas-12 (methodology) and atlas-08 (open questions §VI.A Q24-Q26 Stage-2 verifies).

---

*S52-S88 §VII Registry Slot Inventory section added 2026-05-09. Compiled from `sessions/permanent-results-registry.md` (S29-S88; ~16,000 lines as of S88), atlas-07-materials packet, knowledge MCP `mcp__knowledge__.list_entities("theorems")`, `mcp__knowledge__.search_knowledge` queries against headline §VII slots. D3 round-trip audit data cross-referenced for the ~37/66 round-trip gap.*
