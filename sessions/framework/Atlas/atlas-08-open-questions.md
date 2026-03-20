# Atlas D08: Open Questions

**Total**: 42
**Decisive**: 6 | **Structural**: 12 | **Observational**: 4 | **Carry-Forward**: 20

---

## I. Decisive Questions (one computation answers it)

### Q1: EFOLD-MAPPING-52 -- Does exflation produce >= 3.1 e-folds?
- **What decides it**: Full expansion history from tau=0 to present with physical initial conditions, including stiff epoch (w=1), BCS transit, GGE relic epoch (w=-0.43), and transition to radiation domination. Extract the physical K_pivot mapping from total e-folds.
- **If YES**: SA-Goldstone mixing produces n_s = 0.965 at K < K* = 0.087 M_KK with beta > 0.9 and alpha_s in [-0.040, 0]. The alpha_s identity is broken at the physical pivot.
- **If NO**: All cosmological predictions excluded. Mathematics survives as pure spectral geometry.
- **Estimated effort**: One session, one agent. Requires modulus equation of motion, Hubble friction, initial condition tau_i from round-metric quantum cosmology.
- **Threshold**: PASS if K_pivot(physical) < K* = 0.087 M_KK. FAIL if K_pivot(physical) > 0.5 M_KK.
- **Source**: S51 W2-A, collective analysis Section III.
- **Priority**: HIGHEST -- the single question to which 51 sessions reduce.

### Q2: N-PAIR-FULL -- Physical pair number from full spectrum
- **What decides it**: Exact diagonalization of BCS Hamiltonian with 992-mode (or 16-mode singlet) spectrum at the fold. Does N_pair >= 2?
- **If YES**: Q-theory CC crossing reappears at tau* = 0.170. CC problem reduces from 120 orders to q-theory adjustment form.
- **If NO**: CC problem has no surviving mechanism within the framework. 120-order gap persists.
- **Estimated effort**: One computation on existing data (s44_dos_tau.npz). The 992-mode spectrum exists.
- **Source**: S46 collab (Volovik, Hawking, Dirac, String, quicklook). First flagged S46, never executed through S51.
- **Priority**: CRITICAL -- gates the sole surviving CC mechanism.

### Q3: GOLDSTONE-MASS-FROM-DISORDER -- Finite correlation length mass
- **What decides it**: Compute effective mass from finite correlation length in disordered su(2)/u(1) directions. m^2 ~ 1/xi_disorder^2 where xi_disorder is set by the non-C^2 Josephson couplings J_su2 = 0.059, J_u1 = 0.034.
- **If m in [0.01, 1] M_KK**: Opens a physical origin for the Goldstone mass distinct from (and potentially smaller than) the Leggett mass.
- **If m << 0.01 M_KK**: Disorder-induced mass too small; mass problem persists.
- **Source**: S47 texture-framework Section 3.3 candidate (b), C-6b.
- **Priority**: HIGH -- directly addresses the 170x mass problem.

### Q4: STRUTINSKY-DECOMPOSITION-AT-HIGH-PW -- Smooth n_s from Lambda
- **What decides it**: Strutinsky decomposition of chi_SA at max_pq_sum >= 12. Does the smooth (Thomas-Fermi) part produce n_s near 0.965 at Lambda ~ 12 M_KK?
- **If n_s(smooth) in [0.93, 0.98]**: The mass problem is a category error (Naz S50 reframe). n_s is a cutoff observable, not a collective-mode observable.
- **If n_s(smooth) far from target**: Strutinsky reframe fails; mass problem is real.
- **Source**: S51 STRUTINSKY-51 (n_s_smooth = -0.80 at current truncation, N=6). Requires Window 4 (higher PW truncation).
- **Priority**: HIGH -- requires computational infrastructure from Q5.

### Q5: HIGH-PW-EIGENVALUES -- Do eigenvalues reach 12 M_KK at N=30?
- **What decides it**: Weight-space irrep construction for max_pq_sum=30, then Dirac matrix diagonalization (7936x7936 at (30,0)). Does max|lambda| reach 12 M_KK?
- **If YES**: Characterizes SA correlator at the scale where 170x mass ratio resolves.
- **If NO**: Lowers effective mass scale; SA correlator mixing model needs revision.
- **Source**: S51 HIGH-PW-51 (scaling law predicts R = 12.05 at N=30). Bottleneck is weight-space algorithm, not diagonalization.
- **Priority**: MEDIUM-HIGH -- gates Q4.

### Q6: V-TAU-SWEEP -- V_{kk'}(tau) sweep for Delta_B3 > 0.13
- **What decides it**: Compute the full Kosmann V matrix at a sweep of tau values in [0.15, 0.25]. Does Delta_B3 exceed the q-theory CC threshold 0.13 at any tau?
- **If YES**: CC crossing survives self-consistent gap at some tau point.
- **If NO**: Self-consistent gap kills CC crossing at all physical tau values. CC problem terminal.
- **Source**: S46 collab (Volovik, String). Partially addressed by S47 scale-bridge but not the V matrix sweep itself.
- **Priority**: HIGH -- determines whether Q2 matters.

---

## II. Structural Questions (new mathematics required)

### Q7: What selects the cutoff function f?
- **Status**: ASSUMED (S2 in D04). NCG says f is arbitrary; only moments a_0, a_2, a_4 matter in asymptotic expansion. But chi_SA depends on f' and f''. The SA correlator's sector weights vary at 33% across cutoff choices (S51 CUTOFF-CONV-51), though alpha_eff is stable at 4.7%.
- **What is needed**: An NCG selection principle for f, or a proof that no such principle exists.
- **Source**: D04 entry S2, S51 W1-D.

### Q8: What is the 4D effective action for modulus dynamics?
- **Status**: ASSUMED (S3 in D04). The spectral action is the standard NCG functional, but F.5 showed it penalizes BCS pairing (wrong sign, 93x). SA is a spectral moment, not a total energy. The true modulus effective action may be a different functional.
- **What is needed**: Derivation of the modulus kinetic term and potential from first principles (path integral over internal fluctuations), not assumed from Tr f(D^2).
- **Source**: D04 entry S3, spectral-post-mortem Section 5.

### Q9: Off-Jensen 5D moduli landscape
- **Status**: UNTESTED (Window 3 in D05). The Jensen line is a 1-parameter family within the 5-parameter U(2)-invariant family (or 28-parameter full left-invariant family). T4 instability at tau=0.60, eps=+0.15 suggests U(2) surface is itself unstable.
- **What is needed**: Full 5D Hessian of spectral action + BCS at a single off-Jensen point. Dirac spectrum and Pfaffian off-Jensen. The monotonicity theorem is proven ONLY on Jensen.
- **Estimated effort**: 2-5 hours for Dirac + Pfaffian at one off-Jensen point.
- **Source**: D05 Window 3.

### Q10: Does the order-one condition survive for D_total?
- **Status**: BROKEN (N3 in D04). C-6 gate: 6/7 NCG axioms pass but axiom 5 (orientability) fails at 4.000. Order-one norm = 3.117. The D_K satisfies axioms; the full D including the finite part does not.
- **What is needed**: Either repair D_total or prove that partial axiom satisfaction is structurally sufficient for the framework's physics.
- **Source**: D04 entry N3, S28.

### Q11: Complete A_F extraction via o-map route
- **Status**: CONDITIONAL (N2 in D04). C + M3(C) extracted (dim 20). H (quaternions) requires bimodule structure not yet computed. The o-map route was identified in S10 but never executed.
- **What is needed**: Explicit construction of the bimodule action that yields H = quaternion factor of A_F.
- **Source**: D04 entry N2, S10.

### Q12: tau=0 initial conditions from quantum cosmology
- **Status**: ASSUMED (C1 in D04). The natural initial condition for EFOLD-MAPPING-52 is "near-round metric" (tau_i << 10^{-5}), providing ample e-fold margin. But this is an assumption -- the WDW wavefunction could peak elsewhere.
- **What is needed**: Wheeler-DeWitt equation for Psi(tau) on the minisuperspace. Does Psi peak near tau=0?
- **Source**: D05 Window 1, collective analysis Section III.

### Q13: What maps tau-evolution to cosmic time?
- **Status**: ASSUMED (C1 in D04). The identification of internal modulus evolution with FRW expansion is the framework's core postulate, never derived from first principles. The DeWitt supermetric G_mod = 5.0 is computed but the full Friedmann-modulus coupling is approximate.
- **What is needed**: Rigorous derivation of the modulus equation of motion from the 12D Einstein equations reduced to the M^4 x SU(3) ansatz.
- **Source**: D04 entry C1.

### Q14: Non-Abelian Berry phase for 492 degenerate multiplets (WILSON-LOOP)
- **Status**: UNCOMPUTED since S46. The total pi-count is predicted in [13, 50]. May connect to SM particle count (16). The non-Abelian Wilson loop on the space of degenerate eigenvectors at each tau is computable with existing code.
- **What is needed**: Wilson loop holonomy computation in the degenerate subspaces.
- **Source**: S47 wayforward D-3, S46 Berry addendum.

### Q15: Self-consistent HFB gap equation on SU(3) (sector-resolved)
- **What is needed**: Full Hartree-Fock-Bogoliubov iteration with sector-resolved Delta_{(p,q)} at the fold. Currently only mean-field (60% overestimate, S46).
- **Source**: S47 wayforward C-2 (Naz 3.1), priority 1 from Nazarewicz. Never executed.

### Q16: Curvature-gap correlation function across tau
- **What is needed**: Compute V(B2,B2)(tau) and K_soft(tau) across [0, 0.50]. Check anti-correlation r < -0.9 at all tau.
- **If confirmed**: Promotes the soft-pairing anti-correlation observation to a structural result.
- **Source**: S47 wayforward B-1 / Naz 3.2.

### Q17: Topological defect correlations (outside Bogoliubov paradigm)
- **Status**: NOT ATTEMPTED. Power-law correlations from universality class, outside single-particle or collective-mode frameworks.
- **Source**: S47 wayforward C-4 Path B.

### Q18: Z_3 domain wall energy and homotopy classification
- **What is needed**: Domain wall energy from GL parameters. Order parameter manifold U(1) x Z_3. Vortex support classification on T^2.
- **Source**: S47 wayforward C-1 (Landau S-3), C-3 (Volovik 3.3).

---

## III. Observational Questions (external data required)

### Q19: DESI DR3 (expected 2026-2027)
- **What it tests**: w_0-w_a joint constraint. Current DESI DR2: w_0 = -0.75, w_a = -0.73. Framework predicts w_a = 0 (triple-locked) and w_0 = -1 (frozen modulus). DR3 sigma ~ 0.035 on w_0 discriminates framework from DESI's dynamical DE signal.
- **Framework implication**: If DESI w_a reverts toward 0 with more data, framework survives on w_a. If w_a stays at -0.73, framework's frozen-modulus assumption is wrong.
- **Source**: S49 DESI-DR3-PREP-49.

### Q20: CMB-S4 / Simons Observatory alpha_s measurement
- **What it tests**: alpha_s = dn_s/d(ln k). Framework rigid prediction: alpha_s = -0.069 (Josephson sector) or alpha_s in [-0.040, 0] (SA-Goldstone mixing at K < K*). Planck: alpha_s = -0.008 +/- 0.010. CMB-S4 target sigma ~ 0.005.
- **Framework implication**: If alpha_s measured in [-0.040, 0], SA-Goldstone mixing is vindicated. If alpha_s measured near -0.008, both framework predictions fail.
- **Source**: S49 ALPHA-S-BAYES-49, S51 W2-A.

### Q21: Lensing sigma_8 convergence
- **What it tests**: sigma_8 = 0.799 (framework zero-parameter prediction). Planck: 0.811 +/- 0.006. Lensing: ~0.766 +/- 0.03. The framework prediction sits between them.
- **Framework implication**: If sigma_8 tension resolves toward lensing value, framework's prediction is closest. If toward Planck, framework is 2 sigma away.
- **Source**: S50 W2-F.

### Q22: ALPHA-ENV-43 -- Void vs filament fine-structure variation
- **What it tests**: delta_alpha/alpha ~ 10^{-6} between cosmic voids and filaments. Discriminant for LSS imprint of modulus rolling.
- **Status**: Queued since S43. Requires spectroscopic surveys with void/filament classification.
- **Source**: MEMORY.md, S43.

---

## IV. Carry-Forward Items (not yet promoted to questions)

Items from S47 wayforward (Parts A-H) and S49 wayforward that were neither executed in S48-S51 nor closed by subsequent computations. Listed by priority tier.

### Tier 2 carry-forwards (high priority, never executed)

| # | Item | Source | Description |
|:--|:-----|:-------|:-----------|
| CF1 | TT 2-tensor Lichnerowicz | S47 B-5 | Flagged "next decisive computation" in S47. Uses curvature anatomy data. |
| CF2 | Q-theory Goldstone self-tuning | S47 C-5 | m ~ 10^{-39} GeV estimate. Needs rigorous computation. |
| CF3 | Sakharov curvature-weighted sum | S47 B-4 | S(tau) = sum K_a * rho_a(tau). Tests G_N improvement from 0.36 OOM. |
| CF4 | Three-phonon vertex | S46 D-2 | omega_B2 ~ 2*omega_B1 resonant friction. Never tested. |

### Tier 3 carry-forwards (topological, never executed)

| # | Item | Source |
|:--|:-----|:-------|
| CF5 | DISSOLUTION-BERRY-47 | S46 D-3. 13 pi-phase survival at eps = 0.5*eps_c |
| CF6 | CLOSED-LOOP-47 | S46 D-3. Round-trip Berry phase consistency with S25 |
| CF7 | Sector-resolved R(p,q) BCS pair ratio | S46 D-3. CPT pair symmetry test |
| CF8 | (2,1) pi-phase count = 5 derivation | S46 D-3 |

### Tier 4 carry-forwards (DM/DE and mass ratios)

| # | Item | Source |
|:--|:-----|:-------|
| CF9 | GIBBS-DUHEM-GGE | S46 D-4. Multi-T Gibbs-Duhem with 20% Zubarev/Keldysh discrepancy |
| CF10 | Keldysh sigma with pair-pair interactions | S46 D-4 |

### Tier 5 carry-forwards (Paasch, String, QA backlog)

| # | Item | Source |
|:--|:-----|:-------|
| CF11 | LOG-SIGNED-40 | S40. Signed boson-fermion log sum on 2912 eigenvalues. Uncomputed since S40 |
| CF12 | PHI-GOLDEN-22 | S47 D-5. Tau sweep of (2,2)/(0,0) ratio toward golden ratio |
| CF13 | Six-sequence test | S47 D-5. Zero-cost: 2912 eigenvalues on Paasch spiral |
| CF14 | Swampland c(tau) | S47 D-6. de Sitter conjecture on q-theory potential |
| CF15 | Poisson-Lie T-duality | S47 D-6. Monotonicity may break in dual frame |

### Tier 6 carry-forwards (longer-term investigations)

| # | Item | Source |
|:--|:-----|:-------|
| CF16 | Dirac eigenvector retention (Chladni patterns) | S47 B-6 |
| CF17 | C^2 isotropization / Lifshitz transition | S47 Landau Q-1 / Volovik Q-2 |
| CF18 | Anisotropic KZ defect production | S47 Landau S-5 |
| CF19 | Akama-Diakonov emergent metric | S47 Volovik 3.1. Analog horizon from condensate |
| CF20 | 279-mode tachyonic transit velocity | S46 D-8 |

### S46 Corrections Still Not Propagated

| Correction | Status |
|:-----------|:-------|
| alpha* = 3.91 -> 0.775 | Not propagated. FN-CENTROID-47 unexecuted |
| CHAOS-1 <r> = 0.321 -> 0.439 | Acknowledged S47, no formal recomputation |

---

*Compiled from: session-50-51-collective-analysis.md, atlas-05-walls-doors-windows.md, atlas-04-assumptions.md, session-49-wayforward.md, session-47-wayforward.md, and MEMORY.md. Every item checked against S48-S51 computation records. Items closed by S48-S51 results are excluded.*
