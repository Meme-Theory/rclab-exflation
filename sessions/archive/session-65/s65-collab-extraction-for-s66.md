# S65 Extraction for S66 Planning

**Generated**: 2026-04-03
**Sources**: 8 collab reviews, master synthesis, Lizzi synthesis, CC-budget, investigation-phonon-strings, EVOI framework
**Method**: Exhaustive extraction of every computation suggestion, pre-registered gate, open question, and falsification test

---

## CRITICAL PRIORITY (from CC-budget + Lizzi + user directive)

**DILUTION-CC-66 is #1.** The CC-budget document (Section IV, VII) identifies this as "the single most consequential uncomputed mechanism." Track rho_vac(a) through expansion:
- Decompose into a_0-constant and GGE-dynamical parts
- GGE excitations redshift per mode EOS w_k
- Determine whether a_0 enters Friedmann as true constant (w=-1) or dynamical (w>-1)
- Gate: PASS if rho_vac(today) < 10 * rho_obs; FAIL if > 10^10 * rho_obs; INFO if intermediate
- OOM at stake: 30-120 (the entire CC budget hinges on this)

---

## Computation Suggestions (Deduplicated)

### CONVERGENT (2+ proposers)

| # | Title | Proposers | Gate | Priority |
|:--|:------|:----------|:-----|:---------|
| C1 | **AMPLITUDE-NORM-66**: Rigorous A_s from GGE graph-mode occupation -> curvature perturbation -> Bardeen potential | Volovik, Mack, Sagan, Hawking, Landau, Connes, Kitaev (7) | \|log10(A_s/2.1e-9)\| < 1.0 | CRITICAL |
| C2 | **TENSOR-TRANSFER-66**: n_T transfer function from k_transit to k_CMB via GGE mechanism | Sagan, Mack, Hawking (3) | n_T(k_CMB) > 0 and \|n_T\| > 0.01 | HIGH |
| C3 | **CUTOFF-NS-66**: n_s for exp(-x), sqrt(x), (1-x)^4_+ cutoff functions | Sagan, Connes (2) | Range of n_s across 3 cutoffs < 0.005 = prediction; > 0.005 = fit | HIGH |
| C4 | **GOLDSTONE-GAP-SCALING**: omega_min(N) for CG(N), N = 12, 24, 48, 96 | Sagan, Landau (2) | omega_min ~ const (PASS) vs omega_min ~ 1/N (FAIL) | HIGH |
| C5 | **BCS-CW-SELFCONSISTENT-66**: Coleman-Weinberg determinant on BCS-dressed D_K | Landau (S3-5), Connes (2) | n_s > 0.9607 (1 sigma Planck) | HIGH |
| C6 | **BA-WEIGHT-REFINE-66**: Collective projection of BA energy for Omega_DM h^2 | Volovik, Mack (2) | Omega_DM h^2 within 2x of 0.121 | HIGH |
| C7 | **3-PARAM-YUKAWA-66**: Y_{ab} on Baptista 3-parameter family off Jensen | Baptista (CS-1), Connes (3.4) (2) | max(Y_i/Y_j) > 10 | HIGH |
| C8 | **ENTROPY-SA-CC-66**: a_0^S/a_2^S for thermodynamic cutoff f_S (CCS Paper 15) | Connes, Lizzi (endorsed) (2) | a_0^S/a_2^S < 0.1 * bare ratio | HIGH |

### UNIQUE (1 proposer)

| # | Title | Proposer | Gate | Priority |
|:--|:------|:---------|:-----|:---------|
| U1 | **DILUTION-CC-66**: rho_vac(a) through expansion history (F8) | CC-budget / user directive | PASS: rho_vac(today) < 10 * rho_obs | CRITICAL |
| U2 | **QTHEORY-NPAIR-66**: epsilon(N_pair) for integer N_pair = 55-65, test Gibbs-Duhem P_vac = 0 | Volovik | P_vac < 10^{-110} for some integer N_pair | CRITICAL |
| U3 | **GGE-VACUUM-ENERGY-66**: rho_vac of prethermal state (delta_rho from non-equilibrium) | Volovik | Compare to 10^{-117} scale | HIGH |
| U4 | **BCS-SAKHAROV-LOOP-66**: Self-consistent Delta, a_2, G_N loop | Volovik | Convergent within 3 iterations | HIGH |
| U5 | **w_a-REASSESS-66**: CPL vs actual w(z) from substrate compaction | Mack (M-65-3) | Revised w_a or honest w_a = 0 decision | HIGH |
| U6 | **n_s-r-JOINT-66**: 2D posterior from Planck chains for (r=0.033, n_s=0.9590) | Mack (M-65-2) | 2D tension (sigma) | HIGH |
| U7 | **FINITE-MU-SA-66**: Bessel-modified SDW coefficients at mu = 0.82 M_KK | Connes (3.2) | a_0(mu)/a_2(mu) improved vs zero-mu | HIGH |
| U8 | **RUNNING-NS-66**: dn_s/d(ln k) at L_max = 4 vs L_max = 3 | Sagan | \|alpha_s\| < 0.015 at L_max = 4 | HIGH |
| U9 | **z_eq-CHECK-66**: z_eq from Omega_DM h^2 = 0.400, CMB peak shift | Mack (M-65-7) | z_eq consistent with Planck 3402 +/- 26 | MEDIUM |
| U10 | **M_KK-RESOLVE-66**: gravity vs Kerner route definitive M_KK | Mack (M-65-8) | Definitive M_KK with uncertainty | HIGH |
| U11 | **ZETA-SA-66**: Compute S_zeta(tau) = a_4(tau) on Jensen-deformed SU(3) | Lizzi (VI.1) | n_s^{zeta} within 3 sigma of Planck | HIGH |
| U12 | **DILATON-POTENTIAL-66**: Weyl anomaly dilaton potential on D_K | Lizzi (VI.2) | Lambda_CC^{dilaton} < Lambda_CC^{cutoff} by >= 10 OOM | HIGH |
| U13 | **ANOMALY-CONSTRAINT-66**: Test whether anomaly derivation constrains f_0/f_2 | Lizzi (VI.3) | f_0/f_2 = 0 is anomaly-consistent (zeta valid) OR bounded away from zero (zeta excluded) | HIGH |
| U14 | **SPECTRAL-DIM-66**: Spectral dimension D_s for D_K in cutoff and zeta schemes | Lizzi (VI.5) | D_s^{zeta} = 4 (matter) and 2 (gravity) | MEDIUM |
| U15 | **OEE-NPAIR3-66**: Operator entanglement entropy growth for n_k(t) | Kitaev (C1) | alpha < 0.1 (log growth = integrable) | HIGH |
| U16 | **CLASSICAL-LYAPUNOV-36D**: Lyapunov spectrum of SA gradient flow on 36D moduli | Kitaev (C2) | lambda_max > 0: classically chaotic; = 0: integrable | HIGH |
| U17 | **SFF-NPAIR4-66**: SFF at N_pair=4 (dim=70) | Kitaev (C3) | slope/GUE < 0.1: integrability persists | MEDIUM |
| U18 | **BERTINI-ESSLER-66**: Entropy rate from Thouless energy cross-check vs ADH | Kitaev (C4) | t_BE within 2 OOM of t_ADH | MEDIUM |
| U19 | **RG-CHARGE-OVERLAP-66**: RG charge overlap with GGE density matrix | Kitaev (C5) | F > 0.95: GGE = dressed RG | LOW |
| U20 | **LOSCHMIDT-ECHO-66**: Fidelity decay under perturbation | Kitaev (C6) | Power-law = integrable; exponential = chaotic | MEDIUM |
| U21 | **SFF-BRANCH-DECOMP-66**: B1/B2/B3 contributions to SFF | Kitaev (C7) | Identifies origin of super-Poisson clustering | LOW |
| U22 | **POMERAN-4CELL-66**: Pomeranchuk F_l at 4-cell fabric | Landau (S3-2) | min F_0 > 0 | HIGH |
| U23 | **LEGGETT-SPECTRAL-66**: A(k,omega) spectral function for Leggett mode | Landau (S3-3) | Lorentzian vs Fano lineshape | HIGH |
| U24 | **AB-LANDAU-DAMPING-66**: Q_AB(k) on CG(24) across all 32 graph momenta | Landau (S3-4) | Q(k=0) protected by Goldstone theorem | MEDIUM |
| U25 | **RG-CHARGES-FABRIC-66**: Dressed Richardson-Gaudin integrals R_k* for 2-cell N_pair=3 | Landau (S3-6) | ADH bound holds at fabric level | MEDIUM |
| U26 | **VHS-CLASSIFICATION-66**: Van Hove singularity classification of D_K on SU(3) | Landau (S3-7) | (0,0) trough: accident or structural | MEDIUM |
| U27 | **BCS-ONELOOP-SELFCONSISTENT-66**: Delta^{1-loop}(tau) self-consistent gap | Landau (S3-1) | Gap strengthens or weakens at fold | HIGH |
| U28 | **ISLAND-GRAPH-66**: Island formula on CG(24) for Page curve | Hawking (H-66-3) | Matches S59 area-law S(k=N/2) = 1.381 nats | MEDIUM |
| U29 | **MOVING-MIRROR-66**: Transit Bogoliubov via Fulling-Davies cross-check | Hawking (H-66-4) | \|beta_k\|^2 within 5% of 1.015 | MEDIUM |
| U30 | **WALL-OUTER-ENTROPY-66**: Continuous monotone entropy functional for transit | Hawking (H-66-5) | dS_outer/dtau >= 0 at all tau | LOW |
| U31 | **HM-PREFACTOR-66**: One-loop determinant around HM instanton | Hawking (H-66-6) | Convergent at L_max = 4 | LOW |
| U32 | **EP-BBN-STATIC-66**: Static delta_G consistency at BBN epoch | Mack (M-65-6) | G_N(BBN) = G_N(today) | LOW |
| U33 | **ONEILL-NONPERT-66**: Full O'Neill A-tensor with tau(x) at large amplitude | Baptista (CS-2) | sgn(delta Q) at eps > 0.5 | MEDIUM |
| U34 | **COLOR-SINGLET-CC-66**: a_0/a_2 restricted to SU(3)_c-singlet PW sectors | Baptista (CS-3) | ratio < 0.5 * bare | MEDIUM |
| U35 | **KK-THRESHOLD-L5-66**: Gaussian-cutoff threshold sum at L=5 for m_H convergence | Baptista (CS-4) | Convergence ratio L5/L4 < 1.5 | HIGH |
| U36 | **YUKAWA-MODULI-66**: Map Y eigenvalue ratios across 2D (Jensen, anti-Jensen) plane | Baptista (CS-5) | 3 distinct Y eigenvalues | HIGH |
| U37 | **HESSIAN-CUTOFF-66**: One-loop Hessian at finite Lambda with SA cutoff | Baptista (CS-6) | (36+, 0-) signature preserved | MEDIUM |
| U38 | **PRODUCT-KO-DIM-66**: Product KO-dimension analysis for M^4 x SU(3) | Connes (Q3) | Resolve J^2 = +1 vs predicted J^2 = -1 at KO=4 | MEDIUM |
| U39 | **TRUNCATION-NS-ERROR-66**: Truncation error bound for n_s using Paper 28 tolerance relations | Connes (3.3) | Rigorous error on n_s at L_max=3 | MEDIUM |
| U40 | **TWISTED-YUKAWA-66**: Minimal twist on D_K for C^2 degeneracy breaking | Connes (3.4) | C^2 degeneracy broken | MEDIUM |
| U41 | **RANDOM-NCG-CC-66**: P(a_0/a_2) distribution from random Dirac ensemble on SU(3) | Connes (3.5) | Significant weight near a_0/a_2 -> 0 | LOW |
| U42 | **CHAOS-FILLING-66**: SFF + OTOC at N_pair = 5, 8 | Sagan | slope/GUE < 0.1 at N_pair = 8 | MEDIUM |

### From CC-Budget Priority List (Section VII)

| # | Title | Resolves | OOM at stake | Priority |
|:--|:------|:---------|:-------------|:---------|
| CB1 | DILUTION-CC-66 (= U1 above) | F8 scenario | 30-120 | #1 |
| CB2 | ZETA-ACTION-66 (= U11 above) | Level B exact | 5 | #2 |
| CB3 | MOTT-ACCESS-66: Can any spectral functional change drive E_J/E_C -> 1? | N1 accessibility | 59 | #3 |
| CB4 | BF-SPLIT-FINITE-66: B/F splitting in the finite spectral triple (KO=6) vs fiber (KO=0) | N3 | 60 | #4 |
| CB5 | TWO-COMPONENT-66: Separate a_0-constant from GGE-dynamical in Friedmann | F7 decomposition | Clarifies F8 | #5 |

### From Phonon-Strings Investigation (S64)

| # | Title | Proposer | Gate | Priority |
|:--|:------|:---------|:-----|:---------|
| PS1 | Odd Seeley-DeWitt a_3 on SU(3) | Kaku | a_3 != 0: theta-scanning OPEN | CLOSED by S65 W6-D (a_3 = 0 structurally) |
| PS2 | D_K spectrum at U(1) collapse (c_u1 -> 0) | Kaku | a_0 changes: topology-change CC channel OPEN | HIGH |
| PS3 | Anti-Jensen instability timescale | Kaku | tau_inst < tau_transit: Jensen curve unstable | DONE (S65 W3-E: all 36 modes faster than transit) |
| PS4 | Eigenvalue density phase transition (GWW-type) | Kaku | Non-analytic behavior at critical Lambda | MEDIUM |
| PS5 | Partition function convergence (no Hagedorn) | Kaku | Z(beta) < inf for all beta | MEDIUM |
| PS6 | T-dual-like spectral inversion (c_u1 -> 1/c_u1) | Kaku | a_0/a_2 improved on "T-dual" metric | MEDIUM |
| PS7 | IR B/F spectral splitting from BCS (KO-grading) | Kaku | Splitting > 10%: CC channel OPEN | HIGH |

---

## Pre-Registered Gates

### From Master Collab Section V (20 prioritized)

| ID | Gate Criterion | Source |
|:---|:---------------|:-------|
| AMPLITUDE-NORM-66 | \|log10(A_s/2.1e-9)\| < 1.0 | Master #1 |
| QTHEORY-NPAIR-66 | P_vac < 10^{-110} for some integer N_pair in 55-65 | Master #2 |
| CUTOFF-NS-66 | Range of n_s across 3 cutoffs < 0.005 | Master #3 |
| GOLDSTONE-GAP-SCALING | omega_min ~ const (PASS) vs ~ 1/N (FAIL) | Master #4 |
| ENTROPY-SA-CC-66 | a_0^S/a_2^S < 0.1 * bare ratio | Master #5 |
| TENSOR-TRANSFER-66 | n_T(k_CMB) > 0 and \|n_T\| > 0.01 | Master #6 |
| BCS-CW-SELFCONSISTENT-66 | n_s > 0.9607 (within 1 sigma of Planck) | Master #7 |
| w_a-REASSESS-66 | Revised w_a or honest w_a = 0 decision | Master #8 |
| BA-WEIGHT-REFINE-66 | Omega_DM h^2 within 2x of 0.121 | Master #9 |
| GGE-VACUUM-ENERGY-66 | Compare to 10^{-117} scale | Master #10 |
| 3-PARAM-YUKAWA-66 | max(Y_i/Y_j) > 10 | Master #11 |
| FINITE-MU-SA-66 | a_0(mu)/a_2(mu) improved vs zero-mu | Master #12 |
| RUNNING-NS-66 | \|alpha_s\| < 0.015 at L_max = 4 | Master #13 |
| OEE-NPAIR3-66 | alpha < 0.1 (log growth = integrable) | Master #14 |
| CLASSICAL-LYAPUNOV-36D | lambda_max > 0: classically chaotic; = 0: integrable | Master #15 |
| SFF-NPAIR4-66 | slope/GUE < 0.1: integrability persists at N_pair=4 | Master #16 |
| n_s-r-JOINT-66 | 2D tension (sigma) from Planck posterior | Master #17 |
| KK-THRESHOLD-L5-66 | Convergence ratio L5/L4 < 1.5 | Master #18 |
| POMERAN-4CELL-66 | min F_0 > 0 | Master #19 |
| LEGGETT-SPECTRAL-66 | Lorentzian vs Fano lineshape determination | Master #20 |

### From Lizzi Section VI

| ID | Gate Criterion | Source |
|:---|:---------------|:-------|
| ZETA-SA-66 | n_s^{zeta} within 3 sigma of Planck (0.9649 +/- 0.0042) | Lizzi VI.1 |
| DILATON-POTENTIAL-66 | Lambda_CC^{dilaton} < Lambda_CC^{cutoff} by >= 10 OOM | Lizzi VI.2 |
| ANOMALY-CONSTRAINT-66 | f_0/f_2 = 0 anomaly-consistent (zeta valid) OR bounded away from zero | Lizzi VI.3 |
| SPECTRAL-DIM-66 | D_s^{zeta} = 4 (matter), 2 (gravity) | Lizzi VI.5 |

### From CC-Budget Section IV

| ID | Gate Criterion | Source |
|:---|:---------------|:-------|
| DILUTION-CC-66 | PASS: rho_vac(today) < 10 * rho_obs; FAIL: > 10^10 * rho_obs | CC-budget VII |
| TWO-COMPONENT-66 | Clean separation of a_0-constant from GGE-dynamical in Friedmann | CC-budget VII |
| MOTT-ACCESS-66 | Any spectral functional change can drive E_J/E_C toward 1 | CC-budget VII |
| BF-SPLIT-FINITE-66 | B/F splitting exists in finite spectral triple (KO=6) vs fiber (KO=0) | CC-budget VII |

---

## Open Questions

### From Volovik (Section 5)

1. **Q-theory epsilon(N_pair)**: Does epsilon(N_pair) - N_pair * d(epsilon)/d(N_pair) = 0 at any integer? Discrete q-theory self-tuning test.
2. **Prethermal vacuum energy**: What is rho_vac(GGE) = 0 + delta_rho(non-eq)? Compute delta_rho from GGE occupation deviation from thermal equilibrium.
3. **Self-consistent BCS + Sakharov loop**: Close Delta -> a_2 -> G_N -> gap equation -> Delta.
4. **Leggett mode DM abundance normalization**: Refine BA phonon collective weight (S57 E_BA = 7.0 M_KK from mode-counting or actual collective projection?).
5. **Scale transfer amplitude chain**: Rigorous curvature perturbation derivation from CG(24) graph-mode occupation numbers.

### From Landau (Section 5)

1. **Residual n_s gap of 0.006**: Which dominates -- higher-order BCS (v_k^2), self-consistent CW cross-term, or non-perturbative instanton effects?
2. **Leggett mass stability under cosmological cooling**: Does T_eff^GGE change with cosmological evolution?
3. **Mott transition via quantum fluctuations**: Could moduli fluctuations transiently push E_J/E_C toward Mott boundary?
4. **Spectral action cutoff function f**: Is f determined by the spectral triple, or additional input?
5. **Generation hierarchy from off-Jensen quantum fluctuations**: Do Boltzmann-weighted off-Jensen fluctuations produce non-degenerate Yukawa matrix?
6. **Physical interpretation of anti-Jensen instability**: Do quantum zero-point occupations of unstable modes contribute to observables?
7. **A_s amplitude normalization status**: W2-B preliminary chain needs rigorous computation.

### From Mack (Section 5)

1. **Scale transfer normalization**: Rigorous curvature perturbation from graph-mode Bogoliubov occupations.
2. **w_a physical interpretation**: Is KZ tau-variance a fiber-internal or 4D cosmological effect?
3. **Yukawa hierarchy**: Minimal deformation producing 3-generation mass hierarchy.
4. **n_T at CMB scales**: Does GGE acoustic spectrum preserve blue character at k_CMB?
5. **CP violation from beyond the fiber**: Topological CP from non-orientable compactification analog?
6. **Running of n_s**: Does GGE acoustic spectrum inherit transit-scale running or set its own k-dependence?
7. **Omega_DM h^2 overprediction and z_eq**: Does 3.3x overshoot change z_eq enough to create independent CMB peak tension?
8. **Bounce action route dependence**: Resolving M_KK (gravity vs Kerner) is existential.

### From Connes (Section 5)

1. **Entropy cutoff function f_S**: Does f_S from Paper 15 have qualitatively different a_0^S/a_2^S?
2. **Finite-mu spectral action coefficients**: a_0(mu)/a_2(mu) at mu = 0.82 M_KK.
3. **Product KO-dimension**: KO(M^4 x SU(3)) = 4 gives J^2 = -1, contradicting verified J^2 = +1. How is the product constructed?
4. **Truncation error in n_s**: Paper 28 tolerance bounds at L_max = 3. Is 1.4-sigma gap within truncation error?
5. **Generation hierarchy from twists**: Do Paper 33 minimal twist extra scalars break C^2 coset degeneracy?

### From Sagan (Section 5)

1. **Is f(x) = sqrt(x) derivable or a choice?** If choice, n_s has one free parameter.
2. **Goldstone gap in thermodynamic limit?** If omega_min ~ 1/N_cells, f_DM resolution fails.
3. **Why is dn_s/d(ln k) 6x too large?** Truncation artifact or genuine prediction conflicting with Planck?
4. **CP violation mechanism?** Every identified source is closed.
5. **Can the amplitude normalization chain close A_s gap to < 1 OOM?**
6. **Does chaos transition shift at larger filling?** N_pair = 3 is near the edge (g_T = 0.6).
7. **Route dependence for vacuum stability**: Which M_KK is physical?

### From Hawking (Section 5)

1. **Correct entropy functional for transit GSL?** Bogoliubov entanglement fails. Wall's outer entropy?
2. **Blue tensor tilt at CMB scales?** Does transfer function flatten the tilt?
3. **Island formula on CG(24)?** Natural discretization of quantum extremal surface.
4. **M_KK tension physically resolvable?** Determines eternal stability vs dangerous metastability.
5. **CP violation mechanism for baryogenesis?** Framework's deepest open wound.

### From Kitaev (Section 5)

1. **Classical Lyapunov spectrum of 36D SA gradient flow**: Sole potentially chaotic element.
2. **SFF ramp at any filling N_pair >= 4?** Tests whether Pauli blocking maintains integrability.
3. **Bertini-Essler prethermalization connection**: Independent t_BE cross-check vs ADH.
4. **Operator entanglement entropy growth rate**: Log vs linear growth confirms integrable vs scrambling.
5. **Google Willow-style echo protocol**: Fidelity decay test (Peres-Jalabert-Pastawski).
6. **Origin of super-Poisson number variance**: Branch-specific or inter-branch clustering?

### From Baptista (Section 5)

1. **3-parameter Yukawa eigenvalue ratios**: What lambda_C2/lambda_su2 ratio gives 40:1 splitting?
2. **Breathing mode and Casimir energy**: Can Casimir reverse the SA gradient to drive volume contraction?
3. **Hessian convergence at finite Lambda**: Does cutoff f(D_K^2/Lambda^2) render Hessian sum absolutely convergent?
4. **Anti-Jensen Swampland transverse flatness**: Could flat directions be lifted by quantum corrections into generation-counting?
5. **Product spectral triple M^4 x F x SU(3)**: How does KO-dim 0 for SU(3) affect the full construction?

### From Lizzi (Section VII)

1. **Does the spectral functional choice affect n_s at the 0.006 level?** Compute eps_H in zeta action.
2. **Can the dilaton provide CC relaxation?** Transit-as-relaxation (Path C) may be VIABLE in zeta scheme since a_0 floor is removed.
3. **Is the physical functional the zeta action?** The anomaly derivation: phi=0 gives only a_4 (zeta); phi != 0 switches on a_0, a_2.
4. **Compute in multiple functionals**: Every CC-sensitive quantity in at least cutoff AND zeta schemes.

---

## Sagan's Falsification Tests

### Gate Softness Reclassification

Sagan reclassifies 6 PASS gates as soft:
1. **BCS-DRESSED-65** -> INFO (1% threshold trivially passed by any non-zero gap)
2. **OFF-JENSEN-65** -> INFO (18.2% passes 5% gate but is "dynamically irrelevant")
3. **GAP-ANTIJENSEN-65** -> INFO (10% threshold when result is 97.5% survival; BDI guarantees this)
4. **SPHALERON-65** -> PASS for baryon violation but FAIL for baryogenesis overall (CP bottleneck)
5. **EP-65** -> INFO (trivially expected for M_KK ~ 10^16 GeV)
6. **BOUNCE-36D-65** -> INFO (PASS gravity route, FAIL Kerner route; split verdict)

Sagan's honest count: 5 genuine PASS, 7 FAIL, 6 soft PASS/INFO

### Explicit Falsification Challenges

1. **Cutoff function test**: Compute n_s for 3 cutoff functions. If range spans Planck value, result is accommodation, not prediction.
2. **Goldstone thermodynamic limit**: omega_min(N_cells) scaling. If ~ 1/N, f_DM resolution fails.
3. **A_s amplitude chain**: Must be a COMPUTATION, not a chain of estimates.
4. **Running of n_s**: dn_s/d(ln k) = -3.89e-2 is 5.8 sigma from Planck's -0.0045 +/- 0.0067. Potential FALSIFICATION.
5. **Scale transfer for tensor tilt**: Without transfer function, n_T prediction is "observationally irrelevant."
6. **Baryogenesis overall**: CP bottleneck (11 OOM shortfall) means framework cannot produce baryon asymmetry. FAIL for baryogenesis.
7. **Venus standard**: 65 sessions, zero novel predictions confirmed by independent observation.

---

## Nice-to-Haves

| # | Title | Proposer | Priority |
|:--|:------|:---------|:---------|
| N1 | Moving-mirror Bogoliubov cross-check | Hawking | LOW |
| N2 | Wall outer entropy continuous functional | Hawking | LOW |
| N3 | HM instanton one-loop prefactor | Hawking | LOW |
| N4 | EP test at BBN epoch (static delta_G) | Mack | LOW |
| N5 | RG charge overlap with GGE density matrix | Kitaev | LOW |
| N6 | SFF branch decomposition B1/B2/B3 | Kitaev | LOW |
| N7 | Random NCG a_0/a_2 distribution | Connes | LOW |
| N8 | Partition function convergence (no Hagedorn) | Kaku | LOW |
| N9 | T-dual-like spectral inversion | Kaku | LOW |
| N10 | Eigenvalue density phase transition (GWW-type) | Kaku | LOW |

---

## Cross-Reference: Lizzi's 5 Concrete Proposals (Section VI)

| # | Lizzi ID | Title | Gate | Status in extraction |
|:--|:---------|:------|:-----|:---------------------|
| 1 | VI.1 | ZETA-SA-66: a_4(tau) profile, eps_H^{zeta}, n_s^{zeta} | n_s^{zeta} within 3 sigma Planck | = U11 |
| 2 | VI.2 | DILATON-POTENTIAL-66: Weyl anomaly dilaton potential V_eff(phi) | CC reduced by >= 10 OOM | = U12 |
| 3 | VI.3 | ANOMALY-CONSTRAINT-66: f_0/f_2 from anomaly consistency | f_0/f_2 = 0 consistent or excluded | = U13 |
| 4 | VI.4 | ENTROPY-SA-CC-66 (endorses Connes) | a_0^S/a_2^S < 0.1 * bare | = C8 |
| 5 | VI.5 | SPECTRAL-DIM-66: D_s in cutoff vs zeta | D_s = 4/2 in zeta scheme | = U14 |

---

## Cross-Reference: Master Collab 20 Deduplicated Priorities (Section V)

| Master # | Computation | Proposer Count | Status in extraction |
|:---------|:-----------|:---------------|:---------------------|
| 1 | AMPLITUDE-NORM-66 | 7 | = C1 |
| 2 | QTHEORY-NPAIR-66 | 1 (CRITICAL) | = U2 |
| 3 | CUTOFF-NS-66 | 2 | = C3 |
| 4 | GOLDSTONE-GAP-SCALING | 2 | = C4 |
| 5 | ENTROPY-SA-CC-66 | 2 | = C8 |
| 6 | TENSOR-TRANSFER-66 | 3 | = C2 |
| 7 | BCS-CW-SELFCONSISTENT-66 | 2 | = C5 |
| 8 | w_a-REASSESS-66 | 1 | = U5 |
| 9 | BA-WEIGHT-REFINE-66 | 2 | = C6 |
| 10 | GGE-VACUUM-ENERGY-66 | 1 | = U3 |
| 11 | 3-PARAM-YUKAWA-66 | 2 | = C7 |
| 12 | FINITE-MU-SA-66 | 1 | = U7 |
| 13 | RUNNING-NS-66 | 1 | = U8 |
| 14 | OEE-NPAIR3-66 | 1 | = U15 |
| 15 | CLASSICAL-LYAPUNOV-36D | 1 | = U16 |
| 16 | SFF-NPAIR4-66 | 1 | = U17 |
| 17 | n_s-r-JOINT-66 | 1 | = U6 |
| 18 | KK-THRESHOLD-L5-66 | 1 | = U35 |
| 19 | POMERAN-4CELL-66 | 1 | = U22 |
| 20 | LEGGETT-SPECTRAL-66 | 1 | = U23 |

---

## Summary Statistics

- **Total unique computations extracted**: 52 (8 convergent + 42 unique + 2 already resolved from phonon-strings)
- **CRITICAL priority**: 3 (DILUTION-CC-66, AMPLITUDE-NORM-66, QTHEORY-NPAIR-66)
- **HIGH priority**: ~25
- **MEDIUM priority**: ~14
- **LOW priority**: ~10
- **Pre-registered gates**: 28 distinct gates defined
- **Open questions**: 47 across all reviewers
- **Sagan falsification tests**: 7 explicit challenges
- **Structural deficits identified by 5+ reviewers**: CC (117 OOM), CP violation (11 OOM shortfall), A_s normalization (~1-3 OOM gap)
