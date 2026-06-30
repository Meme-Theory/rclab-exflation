# Session 74 Context Package

**Date**: 2026-04-11
**Topic**: "Actually Probably the Biggest Compute Session Yet"
**Planner**: quantum-acoustics-theorist
**Source directive**: "all session-73a/73b carry forward computations"
**User emphasis**: biggest compute session yet — execute the accumulated carry-forward queue in parallel

---

## I. Framework State (post-S73B)

**Mechanism chain**: 9/11 links complete at 8/9 PASS + 1 FAIL (spectral functional selection FAIL-PERMANENT per S73B W1-C). Multi-cell integrability PASS at <r> = 0.4044 (S73B W3-B). Leggett DM Z_2 parity PASS-PERMANENT at tau_DM = 4.93e82 s / 65 OOM margin (S73A W1-B).

**27 gates closed since S66 freeze** (9 PASS, 12 FAIL, 6 INFO; 8 of the FAILs are PERMANENT structural theorems).

**The Four Crises (S73B Reset)**:
1. **Spectral functional crisis — RESOLVED to FAIL-PERMANENT** (S73B W1-C). Shape and boundary channels are algebraically independent. f is genuine UV data. No zero-parameter selection principle.
2. **Amplitude normalization crisis — NARROWED BUT OPEN**. Combined decoherence (Mott 0.336 + Dispersive 0.150 = 0.486 OOM) OVER-closes residual budget. Gate: which E_C (BCS 12.4 / OES 0.464 / GL 0.066 M_KK; 189x spread) is canonical?
3. **Alpha_s falsification threat — REFRAMED**. S73B W1-A gave alpha_s(CMB-naive) = +0.833 (125 sigma from Planck) via direct Bogoliubov. Requires multifield transfer function to resolve.
4. **Moduli stabilization crisis — NEW**. S73B W1-D: modulus overshoots to tau = 1.614 with NO V_eff minimum in bare spectral action. Planck n_s target at tau = 0.539. No stabilization mechanism computed.

**Observational scorecard (post-S73B)**:
- m_H = 133.4 GeV vs 125.1 (6.6% off, L_max=7 + RGE, 0 free params)
- n_s = 0.9567 vs 0.9649 (1.95 sigma, TRIPLE-CONFIRMED Bogoliubov-invariant)
- Omega_DM h^2 = 0.120 vs 0.1186 (0.7 sigma, Leggett-only)
- tau_DM = 4.93e82 s (65 OOM margin)
- r = 0.024-0.033 vs < 0.036 (BICEP/Keck PASS)
- CC: DILUTION-CC-66 Scenario B PASS at 0.01 OOM (rho_vac(today)/rho_obs = 1.032 via Volovik q-theory). But BBN ADDITIVE FAIL => non-additive G-renormalization REQUIRED.
- w_0 = -0.918 (1.4 sigma tension with DESI DR2 including SN calibration systematic)
- w_a = 0 exact (four-fold lock)
- f_NL = 0.853 equilateral (CMB-S4 testable)
- sin^2_W: L_max-FRAGILE. PW-resolved: -0.046 unphysical. Only surviving channel: LEFT/RIGHT asymmetry per Baptista Paper 13 eq 3.41.
- alpha_s = +0.833 raw (125 sigma, requires multifield transfer)

**Probability**: 9/11 mechanism links * fraction approaching observation. 21 permanent theorems. P(at least one Level 1 resolved in S74) > 0.95 given four targets with P(pass) in [0.30, 0.55].

---

## II. Key References

- **EVOI framework**: `sessions/evoi-framework.md` (authoritative priority table, 21 items, post-S73B reset)
- **Framework chapter**: `sessions/framework/framework-parametric-amplification.md` §10 (5 top-priority + 5 deferred carry-forwards from the parametric-amplification workshop)
- **S73A results**: `sessions/archive/session-73a/session-73a-results-workingpaper.md` (18 computations across 4 waves, includes no-exit-horizon closure, n_bar=85.2, gamma table)
- **S73B results**: `sessions/archive/session-73b/session-73b-results-workingpaper.md` (15 complete + 3 pending, includes multi-cell integrability PASS, spectral functional FAIL)
- **S73B plan (reference structure)**: `sessions/session-plan/session-73b-plan.md`
- **Permanent results registry**: `sessions/permanent-results-registry.md` (112+ proven theorems)
- **Framework hypothesis**: `sessions/framework/Phononic-framework-hypothesis.md`
- **baseline-findings-s66.md**: authoritative CC status (DILUTION-CC-66 PASS at 0.01 OOM, 114 OOM is exflation)

---

## III. EVOI Priority Table (Authoritative)

From `sessions/evoi-framework.md`. Ordered by EVOI descending.

| Rank | ID | Level | EVOI | Computation | P(pass) |
|:-----|:---|:-----|:-----|:-----------|:--------|
| 1 | **N1 TRANSFER-FUNCTION-74** | 1 | 18.2% | k-dependent multifield delta-N transfer from fiber P(k) to CMB P(k). Resolves TRANSIT-PS FAIL (alpha_s +0.833). Gate: |alpha_s(k_CMB)| < 0.015. | 0.45 |
| 2 | **N2 MODULI-STABILIZATION-74** | 1 | 12.0% | What halts tau drift after EFOLD-MAPPING overshoot to tau=1.614. Multi-candidate: instanton back-reaction, BCS dressing, GGE relic, untruncated SA. Gate: V_eff minimum in tau in [0.45, 0.70]. | 0.40 |
| 3 | **N3 L-MAX-BIDIRECTIONAL-74** | 1 | 10.5% | Audit convergence of a_0, a_2, a_4 at L_max in {3, 5, 7, 9}. Triggered by SDW-VALIDATION FAIL. Gate: ratio-of-ratios (a_0/a_2)/(a_2/a_4) stable to 5%. | 0.30 |
| 4 | **N4 E_C-RESOLUTION-74** | 1 | 10.2% | Canonical E_C from BCS compressibility (12.4) vs OES (0.464) vs GL (0.066) — 189x spread. Determines A_s closure. | 0.55 |
| 5 | N5 GGE-TRANSFER-74 | 2 | 9.5% | GGE relic -> CMB angular power transfer. Per S73B W1-D "this is what ACTUALLY determines n_s." | 0.50 |
| 6 | N7 EC-UNIFIED-74 | 2 | 8.8% | Reconcile 3 E_C routes (companion to N4). | 0.40 |
| 7 | N6 SIN2-LR-NORMALIZATION-74 | 2 | 8.5% | Baptista Paper 13 eq 3.41 LEFT/RIGHT connection normalization asymmetry. Sole surviving sin^2_W route after W2-B FAIL. | 0.35 |
| 8 | N8 CC-M1-REGULARIZATION-74 | 2 | 8.1% | f*-scheme CC via absolute M_1 (first spectral moment). | 0.45 |
| 9 | N9 INSTANTON-STABILIZATION-74 | 2 | 8.0% | Instanton back-reaction on modulus potential at kappa < 1 (tau > 0.48). Create V_eff minimum near tau = 0.48? | 0.50 |
| 10 | N17 FRAMEWORK-RESCALE-74 | 2* | 7.35% | Recompute sin^2_W, m_H, CC ratio at L_max in {5, 7, 9}. Conditional promotion. | 0.35 |
| 11 | N10 B1-WEIGHT-AUDIT-74 | 2 | 7.2% | Verify W_B1 = 0.150 correctly represents B1 contribution (TRANSIT-PS W1-A diagnostic). | 0.40 |
| 12 | N11 DC-PERMANENCE-74 | 2 | 6.8% | Test 20% DC component (VIRTUAL-PARTICLE W4-A) on larger multi-cell systems (8-cell, 12-cell). | 0.60 |
| 13 | N15 MODULUS-DECAY-74 | 3 | 5.1% | Modulus decay rate into radiation via instanton-mediated gauge field production. Determines T_rh. | 0.55 |
| 14 | N14 BAYESIAN-FUNCTIONAL-74 | 3 | 4.5% | Planck evidence Z_i for surviving functionals. Status: SUPERSEDED post W1-C FAIL. | 0.50 |
| 15 | N12 DEGENERACY-LIFT-ALPHA-S-74 | 3 | 4.5% | Treat 8 BCS modes individually (not 3 branches) for alpha_s fit. | 0.30 |
| 16 | N16 RATIO-OF-RATIOS-PROTECTED-74 | 3 | 4.4% | Catalog framework observables depending on (a_0/a_2)/(a_2/a_4) vs individual ratios. | 0.70 |
| 17 | N13 GGE-BISPECTRUM-74 | 3 | 4.2% | f_NL from in-in formalism. S70 prediction: f_NL^{equil} = 0.853. | 0.60 |
| 18 | N19 BA-LIFETIME-FABRIC-74 | 4 | 3.5% | BA phonon thermalization on CG(24). SUPERSEDED. | 0.50 |
| 19 | N18 HIGHER-MOMENT-74 | 4 | 2.5% | Compute a_8, a_10 at L_max=3. Check (a_n)^(1/n) convergence. | 0.50 |
| 20 | N20 OSC-METRIC-74 | 4 | 1.9% | Standardize power-law-vs-exponential fit. | 0.90 |
| 21 | N21 VIRTUAL-REFRAME-74 | 4 | 1.0% | Revise framework documents using "virtual particle" language. | 0.95 |

---

## IV. Carry-Forward Computations from S73A Workshop Wrap-Ups

### S73A Phonon-First x Hawking Workshop (16 items — E_C resolution + entry horizon + Lefschetz)

1. **ROUTE2-OES-FULL-CG24-74** (highest EVOI from the pair) — E_C via OES pair-addition on full 24-cell Josephson graph, not cluster approximation. Central target [0.3, 0.6] M_KK. Feeds Mott delta_OOM.
2. **BRANCH-NBAR-D_K-74** — v_g(k_i) and dv_g/dtau at tau_entry for all 8 BCS modes from D_K eigenvalue derivatives. Produce n_bar(B2), n_bar(B1), n_bar(B3) triple. Gate: weighted mean in [51.8, 80].
3. **HFB-HORIZON-BACKREACTION-74** — Fold-squeeze backreaction on entry-horizon Bogoliubov mixing. Target 5-6% surface gravity reduction, INDEPENDENT of branch-resolved n_bar correction.
4. **PHASE-COVARIANCE-3X3-74** — All six off-diagonal elements of inter-branch phase covariance matrix (B1-B2, B1-B3, B2-B3). Full trace-weighted Var(phi) and dispersive delta_OOM.
5. **SPECTRAL-RATIO-INDEPENDENCE-74** — Cross-check Route 2 E_C, branch-resolved n_bar, horizon backreaction for double-counting. Individual + combined beta_k computations.
6. **OVERLAP-CG24-OLLIVIER-74** — Josephson ground-state overlap F on full CG(24) Laplacian (triangle-free 6-regular, Ollivier ~ -0.1). Gate: F in [0.38, 0.50].
7. **T-ENTRY-D_K-74** — T_H at entry horizon from kappa_entry = dv_g/dtau at tau_entry on D_K directly. Resolve kappa = 79,386 vs 2*pi*T_H = 457 M_KK units inconsistency.
8. **QCD-OPENING-74** — alpha_s contribution from instantons in Region II (marginal Kasparov product) at tau > 0.48. Gate: |alpha_s(M_KK, Region II) - alpha_s(M_KK, perturbative)| < 10%.
9. **GS-OVERLAP-74** — Verify closed-form F = (2/pi)^(N/4) * (E_J/E_C)^(N/8) against explicit CG(24) Josephson ground-state wavefunction.
10. **BRANCH-KAPPA-74** — Verify kappa_eff(k_i) ~ (k_i * xi_BCS)^2 dispersive form. Test B3 branch 5-10% surface gravity reduction vs B2.
11. **ENTRY-TH-DERIV-74** — Structural T_entry = kappa_entry/(2*pi) from D_K first principles, independent of analog-gravity S70 derivation.
12. **BDI-MORSE-STABILITY-74** — One-loop Hessian determinant at fold saddle for Leggett Z_2 vertex. BDI block-diagonal structure + non-zero eigenvalues.
13. **LEFSCHETZ-GAUSSIAN-74** — Gaussian quantum state around fold classical saddle as squeezed thermal state with covariance matching one-loop Z_fold determinant.
14. **ISLAND-LEFSCHETZ-CONSISTENCY-74** — S72 ISLAND-GRAPH-72 Page curve vs one-time Lefschetz thimble. Entanglement entropy reproduction without ensemble averaging.
15. **S70-S72-EXIT-HORIZON-AUDIT-74** — Reread S70/S72/S73A scripts referencing exit horizon. Update vocabulary to "post-fold spectral relaxation" or "parametric amplification tail".
16. **S71-THREE-CELL-GSL-CROSS-CHECK-74** — Compare W1-E Route 2 cell-phase variance (delta_phi ~ 0.66 rad, Var ~ 0.44) against S71 THREE-CELL-GSL.

### S73A Mack x Van den Dungen Workshop (8 items — w_0 zeta, HP4 pairing, heterotic)

1. **W0-ZETA-74** (PRIORITY #1, DR3 timeline driver) — w_0 from zeta regularization of modular trace Tr_zeta(D^(-s)) at s=4 on framework KMS state. Expected band [-0.925, -0.910] +/- 0.005-0.015.
2. **F-STAR-JOINT-74** (PRIORITY #2, category-4 lock test) — Refit f = c_0 + c_1*sqrt + c_2*exp + c_3*compact against (n_s, m_H, r, w_0, alpha_s) jointly. Gate: chi^2/dof < 1.
3. **HP4-PAIRING-74** (PRIORITY #3, CC falsifiability) — Connes-Chern character pairing <[ch(D_K)], [e_q]> in M_Pl^4 units. Gate: within 1 OOM of rho_Lambda/M_Pl^4 ~ 10^{-123}.
4. **JENSEN-THRESHOLD-74** (PRIORITY #4, sin^2_W single-epoch diagnostic) — Full threshold sum Sum_k log(Lambda/E_k(tau)) with Jensen-dependent KK energies at tau_fold = 0.19. Report sin^2(tree-level) 0.1% precision.
5. **MODULAR-SIN2-74** (Conditional on #4) — lambda_i(tau(z)) trajectory from tau_fold to tau_today, convolved with threshold log. Gate: within 1% of PDG 0.23122.
6. **MODULAR-WA-74** (Conditional on DR3 w_a != 0) — dtau/dH back-reaction coefficient from D_K(H) dependence, propagated to w_a.
7. **PS-THRESHOLD-74 / EXTENDED-M_H-74** — Paper 05 rank-775 extended gauge module decomposition. Dynkin indices per sector. m_H on extended space vs base 131.8 GeV.
8. **NS-W0-JOINT-74** — 2D (n_s, w_0) prediction under f*. Joint tension forecast against DR3 scenarios.

### S73A Landau x Baptista Workshop (12 items — Mott refinement + Lefschetz + heterotic sin^2_W)

1. **S74-CF-1** — Refined Mott with E_C_total = 0.464 (Route 2 OES) + 3 sector-specific J_a values. Gate: delta_OOM_Mott in [0.18, 0.28], C^2 contribution = 0. Owner: landau.
2. **S74-CF-2** — Sector-resolved BKT phase diagram on CG(24): T_BKT for (C^2, su(2), u(1)). Gate: ratio 24 : 1.5 : 1. Owner: landau.
3. **S74-CF-3** — Lefschetz measure factorization proof (candidate fifth theorem). Thimble integral on Higgs line bundle L_Y over Jensen-deformed SU(3) at fold. Gate: dominant winding = N_pair = 59.8. Owner: baptista.
4. **S74-CF-4** — Heterotic spectral triple (Brain-Mesland-van Suijlekom Paper 20) with separate A_L, A_R. Gate: sin^2(theta_W) within 10% of PDG 0.2315 when (lambda_1, lambda_2, lambda_3) fixed by gauge couplings + M_Z/M_W. Owner: baptista.
5. **S74-CF-5** — Three-coupling lambda consistency: 5 constraints on 3 unknowns (lambda_1, lambda_2, lambda_3) compatible to 5%? Gate: PASS if consistent; sin^2 becomes zero-parameter. Owner: baptista.
6. **S74-CF-6** — Partition function convergence / thimble contour prescription at bi-invariant point. Gate: identify analytic continuation or determine scheme dependence. Owner: baptista.
7. **S74-CF-7** — Spatial tau(x) field-theoretic thimble: allow delta(x) variations. Gate: suppression factor vs global-tau differs by > 10x => field treatment required. Owner: shared.
8. **S74-CF-8** — Mott gap renormalization M_KK -> present horizon. Gate: identify present-day energy scale (GeV, eV, Planck). Owner: landau.
9. **S74-CF-9** — Dimer zero-mode selection rule: discrete subgroup commuting with J_su2/J_u1 but not J_C2. Gate: PASS opens dimer DM route. Owner: baptista.
10. **S74-CF-10** — N_EFF from Morse-Bott degeneration: S65 Hessian signature (36+, 0-, 0 zero modes) -> SM relativistic dof. Gate: physically motivated mapping. Owner: baptista.
11. **S74-CF-11** — A_s budget closure audit with revised Mott (delta_OOM ~ 0.20-0.25) + Josephson phase diffusion at BKT + thimble measure + uncomputed channels. Gate: combined delta_OOM reaches 0.716 target. Owner: landau.
12. **S74-CF-12** — sin^2(theta_W) connection-layer direct computation via Paper 13 eq 3.41 + 5.21 with (lambda_1, lambda_2, lambda_3) fixed. Gate: sin^2 in [0.21, 0.25]. Most consequential sin^2_W closure. Owner: baptista.

---

## V. Carry-Forward Computations from S73B Workshop Wrap-Ups

### S73B Phonon-First x Hawking Workshop (12 items — transfer function + moduli + soft-hair f_DM)

1. **TRANSFER-FUNCTION-74** (same as EVOI N1, phonon-first refinement) — Substrate greybody factor from first principles. Pipeline: overlap matrix <B_i|branch_b> from S56, horizon-crossing tau per branch, per-branch Planck factor, composed T_{B_i}(k) at pivot. Gate: T_{B1}^2/T_{B3}^2 ~ 0.025. Highest-priority Wave 1.
2. **MODULI-STABILIZATION-74** (multi-candidate):
   - (a) **INSTANTON-BACKREACTION-74** (hawking preferred) — dV_inst/dtau at tau = 0.480. Gate: dV_inst/dtau < 0 AND |dV_inst/dtau| >= 58,673.
   - (b) **BCS-DRESSING-MODULI-74** — Extend Delta-tau self-consistent solution beyond fold window.
   - (c) **GGE-RELIC-MODULI-74** — <H_GGE(tau)> profile from 59.8 KZ pairs, check tau-profile for minimum.
   - (d) **SPECTRAL-ACTION-UNTRUNCATED-74** (phonon-first) — S(tau) at L_max in {3, 5, 7, 10}. Check untruncated V(tau) minimum. Cheapest decisive gate.
3. **SELF-CONSISTENCY-74** — Iterate (T_b, tau_min) fixed-point between TRANSFER-FUNCTION and MODULI-STABILIZATION. Three outcomes: unique, multiple, no fixed point.
4. **BDSPT-ANOMALY-74** — Euclidean path integral over D_K commutes with J at non-perturbative level? Stronger than infinitesimal [J, D_K] = 0. Gate: PASS confirms Block-Diagonal Sector Protection Theorem rigorous.
5. **SOFT-HAIR-FDM-74** — Scale R-G sector count from 4-cell N_pair=2 to cosmological N_pair. Gate: unused/populated sector ratio within 1 OOM of f_DM = 0.27. New DM mechanism candidate.
6. **OVERLAP-MATRIX-74** — <B_i|branch_b> matrix from s56_gge_fabric.npz + BCS eigenmodes at fold. Prereq for TRANSFER-FUNCTION-74. Deliverable: 3x3 overlap matrix.
7. **W5F-REVERIFY-74** — Re-verify 4 NEEDS_REVERIFY theorems from W5-F catalog at L_max=7. Determines structural floor 21 vs 22 theorems.
8. **W2E-INTEG-LINK-74** — Does W4-A 2.4% R-G variance residual = W2-E <r> = 0.4625 intermediate chaos? Both V_kl off-diagonal residuals.
9. **STRUCTURE-RG-SCALE-74** — 80/20 partition: BAO or galaxy bias feature at R-G level spectrum scale?
10. **SUBSTRATE-INFO-PARTITION-THEOREM** — Formalize: local perturbations deposit 20% into superselection-locked R-G sector + 80% into coherent ballistic transport. Candidate theorem #23.
11. **GAP-DOMINATED-DISPERSION-74** — Observational consequences of Leggett and optical branches deep in gap-dominated regime at CMB scales. Structure-formation or BAO crossover feature.
12. **ZERO-MODE-WINDING-74** — Is tau compact with periodicity? If yes, winding number conservation provides additional stabilization.

### S73B Mack x Van den Dungen Workshop (15 items — external comm + zeta threshold + R-family)

1. **EXTERNAL-COMM-REFRAME-74** (Wave 1 priority) — Audit external-facing docs, retire "0.01 OOM PASS" CC language, "n_s PASS Planck 1-sigma" language, "131.8 GeV matches to 5%" language. Replace with structural-floor vocabulary. Deliverable: updated working paper + scorecard + audit log.
2. **SPECTRAL-ZETA-THRESHOLD-74** — a_0^zeta, a_2^zeta, a_4^zeta, a_6^zeta as Wodzicki residues via zeta-regularized sum_n d_n^2 * |lambda_n|^(-2s). Expected: O(1) difference from L_max=3 partial sums. Enters canonical_constants.py as a_k_zeta.
3. **HP4-REGIME-74** — Bare-vs-effective ambiguity in HP^4 pairing. Cyclic 4-cocycle c_4 from (A, H, D_K) via JLO construction pairs to BARE or EFFECTIVE spectral action? Decision document, prereq for HP4-PAIRING-74.
4. **HP4-PAIRING-74** — rho_HP4 = <c_4, [D_K]> * H^2 * M_Pl^2 with chi_2 = 0.747 normalization. Gate: |log10(rho_HP4/rho_obs)| < 0.05 PASS, < 0.2 INFO, > 0.5 FAIL.
5. **R-FAMILY-STABILITY-74** — Compute a_8 at L_max = 3, 5, 7. R_2 = a_2*a_6/a_4^2 and R_3 = a_4*a_8/a_6^2. Gate: (A) stability shift < 5% from L=3 to L=7; (B) |R_2 - R_1| < 0.2 AND |R_3 - R_1| < 0.2. PASS unlocks R-family m_H convergence claim.
6. **LEGGETT-VACUUM-CC-74** — chi_Leggett from Leggett ZPE over (0,0)-sector L_max=7 eigenvalues, normalized to chi_2 = 0.747. Gate: |chi_Leggett - 0.47 OOM| < 0.1 PASS. Binary pre-registration.
7. **SCORECARD-BAYES-CALIBRATION-74** — Rewrite observational scorecard with layer tags {STRUCTURAL | PREDICTION_LAYER}. BF via prior-range/posterior-width. Joint framework BF = structured product.
8. **R-FAMILY-OBSERVABLE-SCAN-74** — Catalog L_max-fragile predictions rewritable via R-family or tau-derivatives. Candidates: sin^2_W via d log(g_2/g_1)/dtau, BBN Y_p via rate ratios, CC via a_0*a_4/a_2^2 = R_1.
9. **HARDENING-RATE-DECAY-74** — Meta-gate: new permanent theorems per session across S74-S76. Baseline S73B=6, S73A=5. Gate: S76 <= 3 PASS, 4-5 INFO, >= 6 FAIL.
10. **FOUNDATIONAL-AUDIT-75** (post-S74 carry) — Vary each foundational assumption by one DOF, check 21 permanent theorems survive.
11. **MULTIFIELD-DELTA-N-L7-74** — alpha_s escape via multifield delta-N transfer (overlaps TRANSFER-FUNCTION-74). Highest observational stakes.
12. **MODULI-STABILIZATION-74** (same as phonon-first workshop) — Address W1-D runaway modulus.
13. **JOINT-AUDIT-ATLAS-74** — Merge W5-A + W5-D + W5-F + W5-G into single L_max-independence reference.

### S73B Landau x Baptista Workshop (10 items — R-family triple + multi-cell Plancherel + Noether chain)

1. **R_protected_fold = 1.1287 addition to canonical_constants.py** — Immediate action (not computation). Provenance: curvature invariant at Jensen fold tau=0.190, dressed by SA constants; Vol(K) cancels exactly per baptista B2. 1.74% L_max drift from L=3 to L=7.
2. **ZETA-REGULATED-A_K-74** — Triple-route computation: (a) zeta analytic continuation at s = 0, 1, 2, 3, 4; (b) R-family heat-kernel small-t expansion Tr e^(-t D_K^2); (c) Pade/Euler-Maclaurin acceleration of L_max=3..10 partial sums. Pre-register all three routes. Gate: triple agreement to 2-3%.
3. **R-PROTECTED-TRIPLE-74** — R_protected_fold = a_0 * a_4 / a_2^2 via (a) spectral partial sum L_max=7, (b) direct curvature invariant from Jensen metric, (c) zeta-regulated a_k. Gate: three routes agree within 3% PASS, any two differ > 10% FAIL.
4. **MULTI-CELL-PLANCHEREL-74** — Richardson-Gaudin integrability on 10 PW irreps at L_max=3 with dim(p,q)^2 weights {1, 9, 9, 64, 36, 36, 100, 100, 225, 225}. N_pair=60 distributed by thermal weight at fold. Gate: <r> < 0.45 across all sectors. Expected: PASS with LARGER margin than W3-B (0.404) because physical filling 0.074 is 13x more dilute.
5. **NOETHER-CHAIN-VERIFICATION-74** — Verify Noether chain: Haar bi-invariance => U(1)_{N_pair} current conservation => stress-energy trace => Gibbs-Duhem => Volovik partition => w_0. Check each step: (a) current conservation to 1e-14, (b) E + PV - TS - mu*N identity, (c) Volovik partition rho_J/rho_GGE stable under L_max perturbation.
6. **DR3-W0-FALSIFIER-BAND-REGISTRATION-74** — Pre-register w_0 = -0.918 with falsifier band [-0.94, -0.88]. Methodology action.
7. **A-TENSOR-CORRECTION-74** — Leading O(H/Lambda)^2 A-tensor mixing correction to per-irrep D_K eigenvalues at fold. Gate: corrections < 1% to CORE quantities.
8. **MULTI-LAYER-PROTECTION-THEOREM-74** — Formal statement + proof: six-layer composite for (0,0) sector protection (right-invariance/Schur, [J,D_K]=0, homogeneity, Cl(8), Kosmann, particle-hole). Write-up action.
9. **HARMONIC-ANALYTIC-SPT-CLASSIFICATION-74** — Write purely harmonic-analytic SPT protection as new symmetry-protection category. Contrast solid-state SPT.
10. **EVOI-RECALIBRATION-74** — Update EVOI table with S73B findings. Proposed reweighting: N1 > N2 > (N3+ZETA-REGULATED combined at 16-18%) > (MULTI-CELL-PLANCHEREL at 12-15%) > N4 > A-TENSOR > NOETHER-CHAIN.

---

## VI. Framework Chapter §10 Carry-Forward Computations

From `sessions/framework/framework-parametric-amplification.md` (finalized S73B). Five top-priority + five deferred.

### Top-Priority (S74 Wave 1)

1. **s74_friedmann_from_a2.py** (HIGHEST EVOI per chapter) — Non-circular Friedmann: 3 H^2 = 8 pi G_N <T_{00}>_{GGE}. Direct evaluation on 8-mode squeezed vacuum. f_conv scan [0.1, 10]. Gate: H_0 within factor 3 of Planck 67.4 km/s/Mpc for f_conv in [0.3, 3]. Unblocks every late-time observational comparison.
2. **s74_gge_partition.py** — Three-channel partition (E_a2, E_Leggett, E_effacement) including BCS zero-point contribution. Resolves Q2 factor-30 tension (E_a2/E_Leggett ~ 0.08 back-of-envelope vs observed 2.6). Gate: Omega_m / Omega_DM / Omega_Lambda match within factor 2.
3. **A_S-FROM-BOGOLIUBOV-74** — Primordial A_s in emergent 4D from 8-mode squeezed vacuum + PW sector filter (S65) + c_BLV = 0.485. Closes chapter's largest observational tension (3.15 OOM). Gate: within factor 10 of Planck 2.1e-9.
4. **s74_flatness_from_a2.py** — R^(3) from a_2 Seeley-DeWitt on (M^4 x SU(3)). Expected Omega_k = 0 by SU(3) isotropy. Gate: |Omega_k| < 0.005.
5. **NS-1LOOP-SPECTRAL-74** — 1-loop correction to d^2 S / dtau^2 at fold. Expected delta n_s ~ 0.02 > 1.95 sigma residual 0.008. Gate: n_s within Planck 1-sigma [0.9607, 0.9691].

### Deferred (queued for later sessions, include in Wave 3+ if effort permits)

6. **s75_transfer_function.py** — Mode evolution fold -> recombination (depends on s74_friedmann). Output: framework-computed C_l via emergent KG equation.
7. **BRANCH-COMB-AMPLITUDE-74** — LSS branch-structure modulation amplitude (depends on s75_transfer_function).
8. **ASYMMETRIC-FOLD-LOW-L-74** — Low-l TT signature from asymmetric fold (depends on s75_transfer_function).
9. **LEGGETT-JEANS-74** — Leggett Jeans k_J in 4D units. Independent, can be queued.
10. **BCS-GAP-K-SCALE-74** — BCS gap imprint k_BCS on LSS P(k). Independent, can be queued.

---

## VII. Deduplicated Master Carry-Forward Table (~60 unique items after merge)

Overlap resolution:
- **TRANSFER-FUNCTION-74** = N1 EVOI = MULTIFIELD-DELTA-N-L7-74 (S73B mack-vdd) = s75_transfer_function.py (framework §10) = TRANSFER-FUNCTION-74 (S73B pf-h). **ONE computation.**
- **MODULI-STABILIZATION-74** = N2 EVOI = MODULI-STABILIZATION-74 (S73B pf-h multi-candidate) = MODULI-STABILIZATION-74 (S73B mack-vdd). **ONE computation with 4 sub-gates (a-d).**
- **E_C resolution** = N4 EVOI + N7 EVOI + ROUTE2-OES-FULL-CG24-74 (S73A pf-h #1) + S74-CF-1 (S73A lb #1). **ONE computation cluster.**
- **L_max audit** = N3 EVOI + ZETA-REGULATED-A_K-74 (S73B lb #2) + SPECTRAL-ZETA-THRESHOLD-74 (S73B mack-vdd #2) + R-FAMILY-STABILITY-74 (S73B mack-vdd #5). **ONE computation cluster.**
- **HP4-PAIRING-74** = S73A mack-vdd #3 + S73B mack-vdd #4 (with HP4-REGIME-74 prereq). **ONE computation + 1 decision document prereq.**

**Expected wave structure** (planner will finalize):
- **Wave 1 (CRITICAL, highest EVOI, Level 1 resolution)**: ~12-15 computations including all N1-N4 + framework §10 top 5 + W0-ZETA-74 + R_protected_fold addition + MULTI-CELL-PLANCHEREL-74 + NOETHER-CHAIN-VERIFICATION-74 + OVERLAP-MATRIX-74 (prereq for TRANSFER-FUNCTION)
- **Wave 2 (Level 2 + framework entry-horizon refinements)**: ~15-20 computations including N5-N11 + BRANCH-NBAR-D_K-74 + PHASE-COVARIANCE-3X3-74 + HFB-HORIZON-BACKREACTION-74 + S74-CF-1,2 Mott + SELF-CONSISTENCY-74 + HP4-REGIME-74 + HP4-PAIRING-74 + F-STAR-JOINT-74
- **Wave 3 (Level 3 + S73A/B supporting computations)**: ~15-20 computations including N12-N17 + remaining S73A Lefschetz program + heterotic L/R (S74-CF-4) + three-coupling consistency (S74-CF-5) + sin^2 connection-layer (S74-CF-12) + SOFT-HAIR-FDM-74 + BDI-MORSE-STABILITY-74
- **Wave 4 (infrastructure + documentation + deferred framework §10)**: ~10-15 items including R_protected_fold canonical constant + EXTERNAL-COMM-REFRAME-74 + SCORECARD-BAYES-CALIBRATION-74 + S70-S72-EXIT-HORIZON-AUDIT-74 + VIRTUAL-REFRAME-74 + W5F-REVERIFY-74 + deferred framework §10 items (s75_transfer_function, BRANCH-COMB, etc)

**Total**: ~55-65 computations across 4 waves. This IS "the biggest compute session yet."

---

## VIII. Gate ID Collision Check

Existing gate IDs from closures (S66 through S73B) — DO NOT reuse:
- TRANSIT-PS-73B, LEGGETT-GRAV-DECAY-67, FUNCTIONAL-SELECT-67, BBN-VOLOVIK-67
- COMPOUND-NS, GIBBS-DUHEM, CF4, CF6, CF11, CF13, CF14, Q14
- EXIT-HORIZON-BOG-73, PW-THRESHOLD-RATIOS-73, DOS-THRESHOLD-73a, GRAPH-SPECTRAL-DECOHERENCE-73a, LUTTINGER-SUPERSONIC-73a, JJ-KAPPA-MAP-73a, ALPHA-S-JOSEPHSON-73a, SECTOR-RK-73a
- SDW-VALIDATION-73B, WILSON-LOOP-73B, SIGNED-BF-LOG-73B, RAMANUJAN-73B, THREE-PHONON-73B, VIRTUAL-PARTICLE-73B, EFOLD-MAPPING
- DILUTION-CC-66

Fresh gate IDs for S74 use the `-74` suffix and the specific topic (e.g., TRANSFER-FUNCTION-74, MODULI-STABILIZATION-74, HP4-PAIRING-74). Confirm no collisions with the knowledge-index gates table before finalizing the plan.

---

## IX. Operational Context for Planner

- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- **Script prefix**: `s74_` for all computation scripts (compute format, no sub-sessions)
- **Output directory**: `computations/`
- **Canonical constants**: MUST import from `computations/canonical_constants.py` (per `.claude/rules/math-scripts.md`)
- **Results working paper**: `sessions/archive/session-74/session-74-results-workingpaper.md`
- **Format**: compute (wave-based parallel independent agents, no teams, full self-contained prompts)
- **Agent model**: opus for ALL physics/computation agents
- **Substrate framing**: Every prompt must enforce substrate-first direction (.claude/rules/phononic-framing.md)
- **Source authority hierarchy**: Skeptic verdicts > Synthesis files > Gate verdicts > Session minutes > Raw output
- **Gate verdict standards**: Pre-register PASS/FAIL thresholds BEFORE computation (.claude/rules/gate-verdicts.md)

---

## X. Instructions for QA Planner

1. **Read the full context file first**. Then read:
   - `.claude/templates/plan-compute.md` (plan structure)
   - `.claude/rules/epistemic-discipline.md` (gate methodology)
   - `.claude/rules/phononic-framing.md` (substrate framing — every prompt must enforce it)
   - `sessions/session-plan/session-73b-plan.md` (recent compute plan for reference style)
   - `sessions/framework/framework-parametric-amplification.md` §10 (the 10 chapter carry-forwards with full specs)

2. **The deduplicated master carry-forward table is a CHECKLIST, not a suggestion list**. Every row in Sections III, IV, V, VI becomes a planned computation. The planner designs the full-fidelity prompt (method, equations, inputs, outputs, gate criteria) from the bare-metal spec. No deferrals.

3. **Organize into 4 waves by EVOI priority**:
   - Wave 1: Level 1 EVOI (N1-N4) + framework §10 top-5 + other top-EVOI items (~12-15 computations). Must include OVERLAP-MATRIX-74 as prereq for TRANSFER-FUNCTION-74 and HP4-REGIME-74 as prereq for HP4-PAIRING-74.
   - Wave 2: Level 2 EVOI (N5-N11) + entry horizon refinements from S73A pf-h + Mott/BKT/thimble from S73A lb + heterotic/w_0 from S73A mack-vdd (~15-20 computations)
   - Wave 3: Level 3 EVOI (N12-N17) + remaining S73A/B specific items (~15-20 computations)
   - Wave 4: Infrastructure + documentation + deferred framework §10 (~10-15 items)

4. **EVERY computation gets a COMPLETE self-contained prompt** in the plan file — method, equations, input file paths, output file paths, pre-registered gate ID with PASS/FAIL criteria, assigned agent type. Agents cannot communicate with each other; they see only their prompt and the context in the working paper.

5. **Agent assignments** — distribute across physics agents by domain:
   - **quantum-acoustics-theorist** (QA): acoustic/phonon computations, Bogoliubov, Leggett, ringdown
   - **hawking-theorist**: horizon physics, entropy, moduli stabilization, instanton back-reaction
   - **landau-condensed-matter-theorist**: BCS, Mott, BKT, sector-resolved condensed matter, E_C resolution
   - **baptista-spacetime-analyst**: Lefschetz, heterotic spectral triple, sin^2 L/R asymmetry, three-coupling consistency, Peter-Weyl decomposition
   - **einstein-theorist**: GR reduction, Friedmann, flatness, transfer function, CC regularization
   - **van-den-dungen-bridge-theorist**: NCG HP4 pairing, zeta threshold, R-family stability, Noether chain verification
   - **connes-ncg-theorist**: spectral action 1-loop, f-functional refinement, NS-1LOOP-SPECTRAL
   - **phonon-first-cosmologist**: overlap matrix, transfer function, soft-hair f_DM, structure-formation predictions
   - **mack-cosmic-bridge**: observational scorecard, BBN-VOLOVIK refinement, DR3 preparation, external communication reframe
   - **kitaev-quantum-chaos-theorist**: multi-cell Plancherel, R-G integrability, SFF
   - **lizzi-spectral-functional-theorist**: spectral functional Bayesian, F-STAR-JOINT, R-family observable scan
   - **spectral-geometer**: R_protected_fold, curvature invariants, SU(3) Gilkey formulas

6. **Cost estimate each computation**: ZERO / LOW / MEDIUM / HIGH based on recent benchmarks (Dirac spectrum ~8.7s per s-value, BCS gap ~5 min, full Bogoliubov ~30 min to 2 hr, zeta regularization ~15 min, multi-cell integrability ~1-3 hr for 4-cell).

7. **Decision points between waves**: state explicitly what Wave 1 results trigger Wave 2 dispatch choices, what Wave 2 results feed Wave 3, etc. Self-consistency checks (SELF-CONSISTENCY-74) belong in Wave 2 after Wave 1's TRANSFER-FUNCTION and MODULI-STABILIZATION are complete.

8. **Do NOT execute computations** — plan only. Do NOT modify canonical_constants.py, MEMORY.md, agent memory, or knowledge index. Write ONLY the plan file at `sessions/session-plan/session-74-plan.md`.

---

## Context Manifest

| Source | Extracted |
|:-------|:----------|
| MEMORY.md (framework probability, closed mechanisms) | ~200 lines |
| EVOI framework (priority table Level 1-4, closures, four crises) | ~250 lines |
| QA agent memory (key constants, session history) | ~100 lines |
| Permanent results registry (112+ theorems) | ~100 lines |
| S73A phonon-first-hawking workshop wrap-up (16 items) | 40 lines |
| S73A mack-vdd workshop wrap-up (8 items) | 60 lines |
| S73A landau-baptista workshop wrap-up (12 items) | 30 lines |
| S73B phonon-first-hawking workshop wrap-up (12 items) | 35 lines |
| S73B mack-vdd workshop wrap-up (15 items) | 45 lines |
| S73B landau-baptista workshop wrap-up (10 items) | 45 lines |
| Framework chapter §10 (5 top + 5 deferred) | 100 lines (from recently-finalized doc) |
| S73B plan (structure reference) | referenced path only |
| plan-compute.md template | in context |
| **Total carry-forward items identified** | **~60 unique after dedup** |
