# Session 71 Plan: Spectral Zeta Threshold + S70 Carry-Forward

**Date**: 2026-04-09
**Author**: Phonon-First Cosmologist (cross-domain planner)
**Format**: Parallel single-agent computations across 4 waves
**Source**: S70 Hawking-Phonon workshop (11 carry-forward), S70 Landau-Lizzi workshop, S70 VdD-Mack workshop, S70 Connes synthesis, S70 Gen-Physicist synthesis, S70 working paper (46/46 computations), EVOI framework
**Motivation**: S70 closed the Leggett vacuum (r_L=0.617, PASS) and reduced the A_s gap from 0.485 to 0.267 OOM. The single highest-EVOI computation remaining is SPECTRAL-ZETA-THRESHOLD -- computing S_inf directly from the spectral zeta function without PW decomposition, which ALL S70 workshops identify as the convergence bottleneck. The remaining 19 carry-forward computations span the six-layer causal structure (Hawking workshop), higher-order CCM corrections, entanglement entropy, decoherence band verification, and observational chain refinement.
**Results file**: `sessions/archive/session-71/session-71-results-workingpaper.md`

---

## I. Session Objective

Session 71 attacks two interlocked priorities:

1. **SPECTRAL-ZETA-THRESHOLD-71** (CRITICAL, all workshops): The PW decomposition suffers oscillatory convergence at L >= 7 (S70 LMAX7-PW-70). The spectral zeta function approach bypasses PW entirely, computing S_inf = sum_n lambda_n^{-s}|_{s->0} directly from the 992-mode D_K spectrum. This resolves the convergence question and, if S_inf falls in [1.995, 2.895], yields a converged Higgs mass prediction. This is the single computation that determines whether the amplitude normalization crisis (7C) is resolved or structural.

2. **S70 carry-forward resolution**: S70 produced a six-layer causal structure (two sonic horizons, entry + exit), an INVERTED A_s result via Route B (-0.42 OOM overclosure), compound SU(1,1) squeeze requirements, universal chirp rate prediction, decoherence band [1.12, 26.5], and 11 Hawking-workshop carry-forwards plus 9 from other workshops. All 20 items receive full-fidelity prompts below.

**Pre-registered master gates**:

- **SPECTRAL-ZETA-THRESHOLD-71**: PASS if S_inf uniquely determined AND in [1.995, 2.895]. FAIL if S_inf divergent or outside [0.5, 10.0]. INFO if converged but outside [1.995, 2.895].
- **HIGHER-ORDER-CCM-71**: PASS if delta(lambda_CCM)/lambda_CCM > 0.25 (a_6 breaks f_0 anti-correlation). FAIL if < 0.05.
- **INTER-SITE-ENTANGLE-71**: PASS if S_ent within 20% of 2*r_spatial^2/ln(2). FAIL if factor > 3 discrepancy.
- **DECOHERENCE-BAND-71**: PASS if pair count conserved <1% AND decoherence in [1.12, 26.5]. FAIL if pair count violated >5%.

---

## II. Wave Structure

### Dependency Graph

```
Wave 1 (parallel, no dependencies -- 4 CRITICAL + 4 HIGH):
  W1-A: SPECTRAL-ZETA-THRESHOLD-71 (CRITICAL)
  W1-B: HIGHER-ORDER-CCM-71 (CRITICAL)
  W1-C: INTER-SITE-ENTANGLE-71 (CRITICAL)
  W1-D: DECOHERENCE-BAND-71 (CRITICAL)
  W1-E: NON-TRIVIAL-FIBRATION-CSQUARED-71 (HIGH)
  W1-F: WEYL-TWO-LOOP-71 (HIGH)
  W1-G: BH-THIRD-LAW-71 (HIGH)
  W1-H: THREE-CELL-GSL-71 (HIGH)

    Decision Point: W1-A determines whether PW convergence is the A_s bottleneck
    Decision Point: W1-B determines whether f_0 anti-correlation is breakable
    Decision Point: W1-C/D validate the A_s Route B entanglement + decoherence channels

Wave 2 (parallel, independent of W1 -- 5 MEDIUM + 2 HIGH):
  W2-A: R-SPATIAL-SCAN-71 (MEDIUM)
  W2-B: CHIRP-UNIVERSALITY-71 (MEDIUM)
  W2-C: ENTRY-HORIZON-SPECTRUM-71 (MEDIUM)
  W2-D: CAUSAL-MOMENT-MAP-71 (MEDIUM)
  W2-E: DESI-DR3-SCENARIO-B-PRECISE-71 (MEDIUM)
  W2-F: 21CM-ISW-PREREGISTRATION-71 (MEDIUM)
  W2-G: DISCRETE-RW-UNIVERSALITY-71 (MEDIUM)

    Decision Point: W2-A finds r_spatial_critical for compound OOM
    Decision Point: W2-B validates chirp rate universality across reference frames

Wave 3 (parallel, depends on W1-A for spectral zeta results -- 4 LOW):
  W3-A: ALPHA-S-BAYESIAN-SHADOW-71 (LOW)
  W3-B: CORRELATED-SENSITIVITY-71 (LOW)
  W3-C: CC-FROM-GGE-RESIDUAL-71 (LOW)
  W3-D: BCS-BACKREACTION-a4-71 (LOW)

    Decision Point: W3-C tests whether GGE residual matches Volovik CC

Wave 4 (parallel, no dependencies -- 1 LOW):
  W4-A: GGE-HAWKING-ANALOG-71 (LOW)

    Decision Point: W4-A validates analog experiment prediction
```

---

## III. Wave 1: Critical + High Priority

### W1-A: SPECTRAL-ZETA-THRESHOLD-71 -- Spectral Zeta Function for S_inf

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: HIGH

**Prompt**:

This is the single highest-EVOI computation in the project. The PW (partial-wave) decomposition of the spectral action suffers oscillatory convergence beyond L_max=7 (S70 LMAX7-PW-70 showed 992 modes with oscillatory partial sums). The spectral zeta function approach bypasses this entirely.

The physical question: what is S_inf -- the spectral action evaluated at the fold (tau=0.19) -- computed directly from the D_K eigenvalue spectrum without PW decomposition? If S_inf is uniquely determined, it resolves the PW convergence bottleneck. If it falls in [1.995, 2.895], the A_s gap budget closes to within the remaining 0.267 OOM.

**Background**: The spectral action is S = Tr f(D_K^2 / Lambda^2) where f is the spectral function. For the zeta-function approach, we use the Mellin transform: Tr f(D_K^2/Lambda^2) = (1/Gamma(s)) * integral_0^inf t^{s-1} * Tr(exp(-t*D_K^2/Lambda^2)) * f_hat(t) dt, where the heat trace Tr(exp(-t*D_K^2)) = sum_n exp(-t*lambda_n^2) is computed directly from the eigenvalues. The spectral zeta function is zeta_D(s) = sum_n |lambda_n|^{-2s} = (1/Gamma(s)) * integral_0^inf t^{s-1} * Tr(exp(-t*D_K^2)) dt.

For f(x) = sqrt(x) (the canonical spectral function), the spectral action becomes S = Tr |D_K| = zeta_D(-1/2). This is the analytic continuation of the spectral zeta function to s = -1/2.

Import all constants from `computations/canonical_constants.py`. Key values: a0_fold = 6440, a2_fold = 2776.17, a4_fold = 1350.72, tau_fold = 0.19.

**Computation**:
1. Load the 992-mode D_K eigenvalue spectrum from `computations/s70_lmax7_pw.npz`. Extract all eigenvalues lambda_n (including multiplicities).
2. Compute the spectral zeta function zeta_D(s) = sum_{n: lambda_n != 0} |lambda_n|^{-2s} for s in np.linspace(0.5, 5.0, 100). Verify convergence at each s (the sum must converge for Re(s) > d/2 = 4 for 8-dimensional K=SU(3)).
3. Analytically continue zeta_D(s) to s = -1/2 using the heat kernel expansion: zeta_D(s) has poles at s = (d-k)/2 for k = 0, 1, 2, ... with residues proportional to the Seeley-DeWitt coefficients a_k. The regularized value at s = -1/2 is: zeta_D(-1/2) = a_0 * Lambda^8 / Gamma(4) + a_2 * Lambda^6 / Gamma(3) + a_4 * Lambda^4 / Gamma(2) + a_6 * Lambda^2 / Gamma(1) + FP(-1/2) where FP is the finite part (zeta-function regularized).
4. Alternatively, use the Hurwitz zeta regularization: partition eigenvalues into shells by magnitude. For each shell j with n_j eigenvalues near |lambda| = mu_j, the contribution is n_j * mu_j^{2s}. Sum over shells with Euler-Maclaurin acceleration.
5. Compute S_inf = zeta_D(-1/2) at Lambda = M_KK. Report: (a) raw value, (b) asymptotic series truncation error, (c) comparison to PW sum at L_max=7.
6. If S_inf is uniquely determined, extract the Higgs mass: m_H^2 = (8*pi^2 / f_0) * (a_4 / a_0) * M_KK^2 * R_yukawa where R_yukawa is the Yukawa coupling ratio. Use the existing S69 KK-HIGGS result (m_H = 127.51 GeV at standard normalization) and propagate any shift from the converged S_inf.
7. Cross-check: compare zeta_D(s) at s = 1, 2, 3, 4 against the known Seeley-DeWitt coefficients a_{2s} from canonical_constants.py. Agreement to <1% validates the method.
8. Convergence diagnostic: plot |zeta_D(s) - zeta_D^{(N)}(s)| vs N (number of eigenvalues included) at s = -1/2, 0, 1, 2. Identify whether convergence is monotone or oscillatory.

**Input files**:
- `computations/canonical_constants.py` (all constants)
- `computations/s70_lmax7_pw.npz` (992-mode spectrum at L_max=7)
- `computations/s70_f0_alpha_s.npz` (f_0 scan results)
- `computations/s69_kk_higgs.npz` (Higgs mass data)

**Pre-registered gate**: **SPECTRAL-ZETA-THRESHOLD-71**
- PASS: S_inf uniquely determined (truncation error < 5%) AND S_inf in [1.995, 2.895] (normalized to S_fold units)
- FAIL: S_inf divergent or truncation error > 50% (zeta regularization fails on this spectrum)
- INFO: S_inf converged but outside [1.995, 2.895], or truncation error in [5%, 50%]

**Output files**:
- Script: `computations/s71_spectral_zeta_threshold.py`
- Data: `computations/s71_spectral_zeta_threshold.npz`
- Working paper: Section W1-A

---

### W1-B: HIGHER-ORDER-CCM-71 -- a_6 Contribution to Lambda_CCM

**Agent**: `lizzi-spectral-functional-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The cosmological constant mechanism (CCM) currently uses only a_0 and a_4 Seeley-DeWitt coefficients. The f_0 anti-correlation (S70: increasing f_0 to fix alpha_s worsens CC; decreasing f_0 to fix CC worsens alpha_s) may be broken by including the a_6 term, which enters at next order in the heat kernel expansion.

The physical question: does the a_6 contribution to lambda_CCM produce a shift delta(lambda_CCM)/lambda_CCM > 0.25, sufficient to break the f_0 anti-correlation between the CC mechanism and the alpha_s extraction?

**Background**: The spectral action expanded to sixth order gives: S = f_0*Lambda^4*a_0 + f_2*Lambda^2*a_2 + f_4*a_4 + f_6*Lambda^{-2}*a_6 + ... The CCM involves the ratio lambda_CCM = a_0 / a_4 (to leading order). At next order: lambda_CCM = (a_0 + c_6 * a_6/Lambda^2) / (a_4 + c_6' * a_6/Lambda^2) where c_6, c_6' are combinatorial coefficients from the heat kernel expansion.

Import all constants from `computations/canonical_constants.py`. Key values: a0_fold = 6440, a4_fold = 1350.72, ratio_gilkey = 0.4140 (S70).

**Computation**:
1. Load the Gilkey ratio documentation from `computations/s70_ratio_gilkey_document.npz`. The ratio a_6/a_4 = 0.4140 was established in S70.
2. Compute a_6 = a4_fold * ratio_gilkey = 1350.72 * 0.4140.
3. The CCM at next order: lambda_CCM^{(6)} = (f_0*Lambda^4*a_0 + f_6*Lambda^{-2}*a_6) / (f_4*a_4). For the canonical spectral function f(x) = sqrt(x): f_0 = Gamma(5/2)/(4*pi^2) and f_k = (-1)^k * Gamma(5/2-k)/(4*pi^2*k!). Compute f_6.
4. Evaluate delta(lambda_CCM) = |lambda_CCM^{(6)} - lambda_CCM^{(4)}| / lambda_CCM^{(4)}.
5. Test the anti-correlation: for each f_0 in np.linspace(0.5, 5.0, 50), compute both alpha_s(M_Z) (from S70 F0-ALPHA-S-70 formula) and lambda_CCM^{(6)}. Is there an f_0 where BOTH alpha_s is in [0.10, 0.13] AND lambda_CCM^{(6)} improves over the a_4-only result?
6. If delta(lambda_CCM)/lambda_CCM > 0.25, the anti-correlation is breakable at this order. If < 0.05, the anti-correlation persists through a_6 and the tension is deeper.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_ratio_gilkey_document.npz`
- `computations/s70_f0_alpha_s.npz`

**Pre-registered gate**: **HIGHER-ORDER-CCM-71**
- PASS: delta(lambda_CCM)/lambda_CCM > 0.25 (anti-correlation breakable)
- FAIL: delta(lambda_CCM)/lambda_CCM < 0.05 (anti-correlation persists)
- INFO: delta in [0.05, 0.25] (partial relief)

**Output files**:
- Script: `computations/s71_higher_order_ccm.py`
- Data: `computations/s71_higher_order_ccm.npz`
- Working paper: Section W1-B

---

### W1-C: INTER-SITE-ENTANGLE-71 -- Josephson Junction Entanglement Entropy

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: HIGH

**Prompt**:

The A_s Route B from the S70 Hawking workshop requires inter-site entanglement entropy across the Josephson junction to contribute to the squeeze budget. This computation measures the entanglement entropy of a 2-cell bipartition on CG(24) and compares to the predicted value 2*r_spatial^2/ln(2).

The physical question: is the entanglement entropy between adjacent Voronoi cells connected by a Josephson junction consistent with the spatial squeeze parameter r_spatial = 0.551 (from S70)?

**Background**: The 32-cell fabric on CG(24) has Josephson junctions between adjacent cells. Each junction carries coupling J_C2 = 0.933 M_KK. The BCS ground state of the full 2-cell system has entanglement between the cells due to pair tunneling. The von Neumann entropy of the reduced density matrix (tracing out one cell) quantifies this entanglement. For a squeezed state with squeeze parameter r, S_ent = 2*r^2/ln(2) in the Gaussian limit.

Import all constants from `computations/canonical_constants.py`. Key values: J_C2 = 0.933, Delta_BCS = 0.4643, N_cells = 32, T_acoustic = 0.112.

**Computation**:
1. Load the 2-cell BCS ground state from `computations/s70_meissner_ed.npz`. This contains the exact diagonalization results for the Meissner state on 2 cells.
2. Load the GGE occupation numbers from `computations/s56_gge_fabric.npz`.
3. Load the Josephson coupling data from `computations/s63_quantum_metric.npz` (contains the CG(24) adjacency structure and couplings).
4. Construct the 2-cell BCS Hamiltonian:
   H = H_BCS(cell_1) + H_BCS(cell_2) + H_J(junction)
   where H_BCS is the 8-mode BCS Hamiltonian (4B2+1B1+3B3 per cell) and H_J = -J_C2 * sum_{<ij>} (c_i^dagger c_j + h.c.) is the Josephson coupling.
5. Diagonalize H on the 2-cell Fock space (dimension = 256 x 256 = 65536 for full treatment; truncate to lowest N_pair sectors if needed).
6. Compute the reduced density matrix rho_1 = Tr_2(|GS><GS|) by tracing over cell 2.
7. Compute von Neumann entropy: S_ent = -Tr(rho_1 * log2(rho_1)).
8. Compare to prediction: S_predicted = 2 * r_spatial^2 / ln(2) = 2 * 0.551^2 / 0.6931 = 0.876.
9. Gate criterion: |S_ent - S_predicted| / S_predicted < 0.20 = PASS.
10. Also compute the Renyi-2 entropy S_2 = -log2(Tr(rho_1^2)) as a cross-check (less sensitive to small eigenvalues).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_meissner_ed.npz`
- `computations/s56_gge_fabric.npz`
- `computations/s63_quantum_metric.npz`

**Pre-registered gate**: **INTER-SITE-ENTANGLE-71**
- PASS: |S_ent - 2*r_spatial^2/ln(2)| / (2*r_spatial^2/ln(2)) < 0.20
- FAIL: ratio > 3.0 (entanglement and squeeze decoupled)
- INFO: ratio in [0.20, 3.0] (partial agreement)

**Output files**:
- Script: `computations/s71_inter_site_entangle.py`
- Data: `computations/s71_inter_site_entangle.npz`
- Working paper: Section W1-C

---

### W1-D: DECOHERENCE-BAND-71 -- SU(1,1) BCH Compound Squeeze with Decoherence

**Agent**: `phonon-first-cosmologist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The S70 Hawking workshop established a decoherence band [1.12, 26.5] within which the information paradox analog is resolved by spectral decoherence. This computation verifies the SU(1,1) compound squeeze parameter r_eff using the full Baker-Campbell-Hausdorff formula, checks pair count conservation, and applies the decoherence correction.

**Background**: The A_s budget requires compounding three squeeze contributions: (1) BCS squeeze r_BCS per mode, (2) spatial thermal squeeze r_spatial = 0.551, (3) Leggett channel r_L = 0.617 (S70 LEGGETT-VACUUM-70 PASS). These are SU(1,1) operations that do not commute. The BCH formula for SU(1,1) gives the compound: S_compound = exp(alpha*K_+) * exp(beta*K_0) * exp(gamma*K_-) where K_{+,-,0} are the SU(1,1) generators. The pair count N_pair = <K_0> must be conserved to < 1%.

Import all constants from `computations/canonical_constants.py`. Key values: Delta_BCS = 0.4643, omega_L1 = 0.138, E_B2_mean = 0.845.

**Computation**:
1. Load the SU(1,1) matrices from `computations/s70_phi_eff_compound.npz`. This contains r_k and phi_k for each BCS mode, plus the compound result from S70 W2-D.
2. Load the squeeze reconciliation from `computations/s69_squeeze_reconciled.npz`.
3. For each BCS mode k (8 modes total):
   a. Construct the SU(1,1) matrix for BCS squeeze: S_BCS(k) in the Bargmann representation [[cosh(r_k), e^{i*phi_k}*sinh(r_k)], [e^{-i*phi_k}*sinh(r_k), cosh(r_k)]].
   b. Construct the spatial thermal squeeze: S_spatial with r_spatial = 0.551, phase averaged over von Mises distribution (kappa = J_C2/T_acoustic = 0.933/0.112 = 8.33).
   c. Construct the Leggett squeeze: S_L with r_L = 0.617, phi_L = pi (anti-phase from sudden quench).
   d. Compute the EXACT BCH compound: S_eff = S_L * S_spatial * S_BCS. Extract r_eff and phi_eff from the compound matrix.
4. Pair count conservation check: compute N_pair_in = sum_k sinh^2(r_k) and N_pair_out = sum_k sinh^2(r_eff_k). Gate: |N_pair_out - N_pair_in| / N_pair_in < 0.01.
5. Decoherence correction: the decoherence timescale t_dec from the Hawking workshop is bounded by [1.12, 26.5] in units of t_transit. The squeeze parameter after decoherence is r_eff_dec = r_eff * exp(-t_transit/t_dec). Compute for t_dec/t_transit in {1.12, 5.0, 10.0, 26.5}.
6. Compute the compound A_s correction: delta_OOM = log10(cosh(2*r_eff_dec)) for each decoherence time. Report the range.
7. Cross-check: the SU(1,1) Casimir C = K_0^2 - (1/2)*(K_+*K_- + K_-*K_+) must be preserved by each operation. Verify |C_in - C_out|/|C_in| < 1e-10.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_phi_eff_compound.npz`
- `computations/s69_squeeze_reconciled.npz`
- `computations/s70_leggett_vacuum.npz`

**Pre-registered gate**: **DECOHERENCE-BAND-71**
- PASS: |N_pair_out - N_pair_in|/N_pair_in < 0.01 AND compound decoherence parameter in [1.12, 26.5]
- FAIL: pair count violation > 5% (SU(1,1) representation inconsistency)
- INFO: pair count conserved but decoherence outside [1.12, 26.5]

**Output files**:
- Script: `computations/s71_decoherence_band.py`
- Data: `computations/s71_decoherence_band.npz`
- Working paper: Section W1-D

---

### W1-E: NON-TRIVIAL-FIBRATION-CSQUARED-71 -- Sound Speed and Running from Principal Bundle

**Agent**: `van-den-dungen-bridge-theorist`
**Model**: opus
**Cost**: HIGH

**Prompt**:

All framework predictions to date assume a trivial fibration M4 x K (product geometry). Real KK compactifications involve non-trivial principal SU(3)-bundles over M4, with A-tensor corrections to the metric and curvature. This computation evaluates the SIMULTANEOUS impact on c_s^2 (sound speed of DE perturbations) and alpha_s (spectral index running).

The question: does going from trivial to non-trivial fibration change c_s^2 and alpha_s in opposite directions (opening the solution space) or the same direction (closing it)?

**Background**: Van den Dungen's NCG submersion framework (Papers 1-6 of VdD library) gives the non-trivial fibration correction to the spectral action via the O'Neill A-tensor. For a principal G-bundle P -> M with connection omega, the Dirac operator on the total space P splits as D_P = D_M tensor 1 + gamma^mu A_mu + 1 tensor D_K, where the A-tensor contribution gamma^mu A_mu mixes base and fiber.

The A-tensor correction to the a_2 coefficient (which determines c_s^2 via the q-theory): delta(a_2)/a_2 = -|A|^2/(12*R_K) where |A|^2 is the norm-squared of the A-tensor and R_K is the fiber scalar curvature. The correction to alpha_s comes through delta(a_4)/a_4 which has a different dependence on |A|^2.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Parameterize the A-tensor strength: |A|^2 = kappa * R_K where kappa in [0, 0.5] (kappa = 0 is trivial bundle, kappa = 0.5 is maximal O'Neill curvature before instability).
2. Compute the correction to a_2: delta_a2 = -(kappa/12) * a2_fold.
3. Compute the correction to a_4 from the Gilkey-Seeley formula including the mixed curvature term: delta_a4 = (kappa/360) * (5*kappa - 2) * a4_fold. (The sign and coefficient come from the dimension-8 heat kernel on a fiber bundle -- derive from the VdD submersion formula or reference Paper 3 of VdD library.)
4. Compute delta(c_s^2): in q-theory, c_s^2 depends on whether a_0 acquires a kinetic term. The A-tensor generates a kinetic mixing between a_0 and the gauge connection. Estimate: delta(c_s^2) = kappa^2 * (g_3^2 / (16*pi^2)) from the one-loop gauge-scalar mixing diagram.
5. Compute delta(alpha_s) = d(n_s)/d(ln k) where n_s depends on the ratio a_2/a_0 (spectral tilt) and alpha_s depends on a_4/a_2 (running). From the corrections in steps 2-3: delta(alpha_s)/alpha_s = delta(a_4)/a_4 - delta(a_2)/a_2.
6. Gate: delta(c_s^2) < 10^{-3} (c_s^2 = 0 robust against fibration) AND delta(alpha_s)/alpha_s > 0.5 (alpha_s tension relieved by fibration).
7. Plot: delta(c_s^2) vs kappa and delta(alpha_s)/alpha_s vs kappa on the same figure. Identify the allowed band.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_q_sound.npz` (c_s^2 = 0 derivation)
- `computations/s70_f0_alpha_s.npz` (alpha_s tension data)

**Pre-registered gate**: **NON-TRIVIAL-FIBRATION-CSQUARED-71**
- PASS: delta(c_s^2) < 10^{-3} AND delta(alpha_s)/alpha_s > 0.5
- FAIL: delta(c_s^2) > 0.1 (c_s^2 = 0 prediction destroyed)
- INFO: one criterion met but not both

**Output files**:
- Script: `computations/s71_non_trivial_fibration_csquared.py`
- Data: `computations/s71_non_trivial_fibration_csquared.npz`
- Working paper: Section W1-E

---

### W1-F: WEYL-TWO-LOOP-71 -- Two-Loop BCS Weyl Correction

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The Weyl tensor |C|^2 (conformally invariant part of curvature) enters the spectral action at the a_4 level. BCS backreaction modifies the effective metric and hence |C|^2. The one-loop BCS correction was computed in S69 (SECTOR-BCS-A4-69). This computation extends to two-loop to test whether BCS-protection of the gravitational sector holds to all orders.

**Background**: The spectral action a_4 term contains |C|^2 with coefficient proportional to the number of modes. Under BCS condensation, the effective metric receives corrections from the pair field Delta. At one-loop, delta(|C|^2)/|C|^2 ~ (Delta/M_KK)^2 ~ (0.464)^2 = 0.215. The two-loop correction involves pair-pair interactions and goes as (Delta/M_KK)^4.

Import all constants from `computations/canonical_constants.py`. Key values: Delta_BCS = 0.4643, a4_fold = 1350.72.

**Computation**:
1. Load the one-loop BCS a_4 correction from `computations/s69_sector_bcs_a4.npz`.
2. The two-loop correction to |C|^2 from BCS pairing:
   delta_2(|C|^2) / |C|^2 = (Delta_BCS / M_KK)^4 * (N_modes^2 / (16*pi^2)) * C_2loop
   where C_2loop is the two-loop combinatorial factor from the sunrise diagram. For BCS: C_2loop = 7*zeta(3)/(16*pi^2) (standard BCS two-loop, see Abrikosov-Gorkov).
3. Compute: N_modes = 8, Delta_BCS/M_KK = 0.4643 (dimensionless). So (Delta_BCS/M_KK)^4 = 0.0464.
4. Full two-loop: delta_2(|C|^2)/|C|^2 = 0.0464 * (64/(16*pi^2)) * 7*zeta(3)/(16*pi^2).
5. Gate: if delta_2(|C|^2)/|C|^2 < 10^{-6}, the BCS protection of the gravitational sector holds to two-loop precision. This would extend the one-loop protection theorem to all-orders (the series is asymptotic with Gi = 13.7, so two-loop establishes the pattern).
6. Cross-check: compare to the Ginzburg number Gi = 13.7 (S62). The loop expansion is asymptotic but the leading terms give the correct description to ~1% (flat-band BCS is correct, S62 SP-Phonon workshop).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_sector_bcs_a4.npz`

**Pre-registered gate**: **WEYL-TWO-LOOP-71**
- PASS: delta_2(|C|^2)/|C|^2 < 10^{-6} (all-orders BCS protection)
- FAIL: delta_2(|C|^2)/|C|^2 > 10^{-3} (two-loop breaks protection)
- INFO: delta in [10^{-6}, 10^{-3}]

**Output files**:
- Script: `computations/s71_weyl_two_loop.py`
- Data: `computations/s71_weyl_two_loop.npz`
- Working paper: Section W1-F

---

### W1-G: BH-THIRD-LAW-71 -- Black Hole Third Law from D_K Spectrum

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The S70 Hawking workshop derived the information paradox as a projection artifact: projecting the full D_K spectrum onto only the a_2 (gravitational) content loses information that remains in the higher spectral moments. This computation tests the black hole third law: is the projected entropy S_projected consistent with the Bekenstein-Hawking formula S = pi*Q^2 (in appropriate units)?

**Background**: The substrate picture says: a black hole is a region where the a_2 content of D_K dominates over a_4 (gauge) and a_0 (cosmological) content. The projected spectrum (keeping only a_2 contributions) gives a truncated density of states. The entropy from this truncated spectrum should reproduce S_BH = A/(4*G_N) = pi*Q^2 for a charged black hole.

Import all constants from `computations/canonical_constants.py`. Key values: a0_fold = 6440, a2_fold = 2776.17, a4_fold = 1350.72.

**Computation**:
1. Load the 992-mode D_K spectrum from `computations/s70_lmax7_pw.npz`.
2. Decompose each eigenvalue lambda_n into spectral moment contributions: lambda_n = a_0(n) + a_2(n) + a_4(n) + ... where a_k(n) is the contribution of eigenvalue n to the k-th Seeley-DeWitt coefficient (weighted by the heat kernel coefficient).
3. Construct the a_2-projected spectrum: keep only the a_2(n) components. This gives a reduced density of states rho_2(E) = sum_n delta(E - a_2(n)).
4. Compute the microcanonical entropy from the projected spectrum: S_projected = ln(rho_2(E)) at E = E_BH (a characteristic black hole energy scale).
5. For the comparison, use Q = sqrt(a_2 / (4*pi*G_N)) in natural units. Compute pi*Q^2 = pi * a2_fold / (4*pi*G_N * M_KK^2). Express G_N in M_KK units via G_N = 1/(8*pi*M_Pl_reduced^2) and M_Pl_reduced/M_KK.
6. Gate: S_projected / (pi*Q^2) in [0.5, 2.0] means the BH entropy is reproduced to within a factor of 2 from the spectral triple projection. This would validate the "information paradox = projection artifact" interpretation from S70.
7. Compute the entropy deficit: S_full - S_projected = information carried by non-gravitational spectral moments (a_0, a_4, a_6). This is the "lost information" in the Hawking radiation analog.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_lmax7_pw.npz`
- `computations/s70_kretschner_bcs.npz`

**Pre-registered gate**: **BH-THIRD-LAW-71**
- PASS: S_projected / (pi*Q^2) in [0.5, 2.0]
- FAIL: ratio < 0.1 or > 10.0 (projection does not reproduce BH entropy)
- INFO: ratio in [0.1, 0.5] or [2.0, 10.0]

**Output files**:
- Script: `computations/s71_bh_third_law.py`
- Data: `computations/s71_bh_third_law.npz`
- Working paper: Section W1-G

---

### W1-H: THREE-CELL-GSL-71 -- Generalized Second Law on 3-Cell Ring

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: HIGH

**Prompt**:

The S70 Hawking workshop established the generalized second law (GSL) on a 2-cell system (KRETSCHNER-BCS-70, MEISSNER-ED-70). This computation extends to a 3-cell ring to test whether GSL holds with a non-trivial graph topology (the 3-cell ring on CG(24) has 3 Josephson junctions forming a loop).

**Background**: The GSL states that the generalized entropy S_gen = S_BH + S_matter is non-decreasing. In the substrate, S_BH corresponds to the a_2-projected spectral entropy and S_matter to the BCS condensate entropy. The 3-cell ring introduces frustration: with odd-parity ring geometry, the BCS phases on the 3 cells cannot simultaneously minimize all junction energies. This frustration is the simplest non-trivial test of GSL beyond 2-cell.

Import all constants from `computations/canonical_constants.py`. Key values: J_C2 = 0.933, Delta_BCS = 0.4643.

**Computation**:
1. Construct the 3-cell BCS Hamiltonian on a ring: H = sum_{i=1}^{3} H_BCS(cell_i) + sum_{<ij>} H_J(junction_ij) where the sum is over 3 junctions forming a closed ring.
2. Diagonalize on the 3-cell Fock space (8 modes per cell, 3 cells: truncate to manageable sector by restricting total pair number).
3. Prepare initial state: BCS ground state at tau slightly above tau_fold (pre-transit).
4. Evolve through 4 stages of the transit (following S70 GSL structure):
   Stage 1: Pre-transit equilibrium (tau = 0.22)
   Stage 2: During transit (tau = 0.19, fold crossing)
   Stage 3: Post-transit GGE formation (tau = 0.16)
   Stage 4: Late-time GGE relaxation (tau = 0.10)
5. At each stage, compute:
   a. S_gen(cell_i) = S_a2(cell_i) + S_BCS(cell_i) for each cell
   b. S_gen(total) = sum_i S_gen(cell_i) + S_junction(ij) (include junction entropy)
6. Gate: S_gen monotonically non-decreasing at ALL 4 stages = PASS.
7. Check for frustration effects: does the 3-cell ring show enhanced pair-breaking compared to the 2-cell linear chain? The frustrated junction should have lower pair current, increasing S_matter.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_meissner_ed.npz` (2-cell reference)
- `computations/s70_kretschner_bcs.npz` (BCS curvature data)

**Pre-registered gate**: **THREE-CELL-GSL-71**
- PASS: S_gen monotone at all 4 stages (GSL extends to frustrated topology)
- FAIL: S_gen decreases at any stage (GSL violated by frustration)
- INFO: S_gen monotone for 3/4 stages (partial violation)

**Output files**:
- Script: `computations/s71_three_cell_gsl.py`
- Data: `computations/s71_three_cell_gsl.npz`
- Working paper: Section W1-H

---

## IV. Wave 2: Medium Priority

### W2-A: R-SPATIAL-SCAN-71 -- Compound OOM vs r_spatial Parameter Scan

**Agent**: `phonon-first-cosmologist`
**Model**: opus
**Cost**: LOW

**Prompt**:

The S70 compound squeeze used r_spatial = 0.551 (from SU11-PHASE-69). This computation scans r_spatial over a range to find r_spatial_critical -- the value at which the compound A_s OOM gap closes to zero.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the compound squeeze data from `computations/s70_phi_eff_compound.npz`.
2. For each r_spatial in {0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70}:
   a. Recompute the SU(1,1) compound squeeze r_eff using the BCH formula with r_BCS, r_L = 0.617, and the scanned r_spatial.
   b. Compute the compound delta_OOM = log10(cosh(2*r_eff)).
   c. Subtract from the current A_s gap: remaining_gap = 0.267 - delta_OOM.
3. Find r_spatial_critical where remaining_gap = 0 by interpolation.
4. Report: r_spatial_critical, the sensitivity d(gap)/d(r_spatial), and whether the S70 value r_spatial = 0.551 is close to critical.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_phi_eff_compound.npz`
- `computations/s70_leggett_vacuum.npz`

**Pre-registered gate**: **R-SPATIAL-SCAN-71**
- INFO: Report r_spatial_critical. If in [0.45, 0.65] = gap closeable with modest parameter change. If > 1.0 = gap not closeable by this channel alone.

**Output files**:
- Script: `computations/s71_r_spatial_scan.py`
- Data: `computations/s71_r_spatial_scan.npz`
- Working paper: Section W2-A

---

### W2-B: CHIRP-UNIVERSALITY-71 -- Chirp Rate in 3 Reference Frames

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The S70 Hawking workshop derived a universal chirp rate k_chirp for the spectral flow of D_K eigenvalues during the transit. This computation verifies the chirp rate in three reference frames: (1) the lab frame (fixed tau), (2) the comoving frame (moving with the transit), (3) the conformal frame (using conformal time). Universality means k_chirp is frame-independent in the stationary (long-wavelength) limit.

Import all constants from `computations/canonical_constants.py`. Key values: v_terminal = 26.545, dt_transit = 0.00113, tau_fold = 0.19.

**Computation**:
1. Load the spectral flow data from `computations/s70_chirp_penumbra.npz`.
2. In the lab frame: k_chirp_lab = d^2(lambda_n)/dt^2 evaluated at the fold. Compute for the 8 BCS modes.
3. In the comoving frame: transform t -> xi = t - v_terminal * tau, so k_chirp_comov = d^2(lambda_n)/dxi^2. The transformation involves the transit velocity.
4. In the conformal frame: transform t -> eta = integral dt / a(t) where a(t) is the scale factor. For the transit, a(t) ~ exp(H_fold * t) locally. k_chirp_conf = a^2 * d^2(lambda_n)/deta^2.
5. Compare all three: compute |k_chirp_lab - k_chirp_comov| / k_chirp_lab and |k_chirp_lab - k_chirp_conf| / k_chirp_lab.
6. Gate: all ratios < 10% in the stationary limit (k*dt_transit << 1).
7. For modes with k*dt_transit ~ 1, the chirp rate is frame-dependent. Report the correction factor.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_chirp_penumbra.npz`

**Pre-registered gate**: **CHIRP-UNIVERSALITY-71**
- PASS: |k_chirp difference| / k_chirp < 10% for all 3 frames in stationary limit
- FAIL: > 50% disagreement in stationary limit
- INFO: < 10% for 2/3 frames

**Output files**:
- Script: `computations/s71_chirp_universality.py`
- Data: `computations/s71_chirp_universality.npz`
- Working paper: Section W2-B

---

### W2-C: ENTRY-HORIZON-SPECTRUM-71 -- D_K Eigenvalue Tracking Across Entry Sonic Horizon

**Agent**: `spectral-geometer`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The S70 Hawking workshop identified a six-layer causal structure with two sonic horizons (entry at tau ~ 0.22-0.25, exit at tau ~ 0.14-0.17). This computation tracks D_K eigenvalues across the ENTRY sonic horizon to count level crossings and identify any spectral reorganization.

**Background**: At a sonic horizon, the local flow velocity equals the sound speed. In the substrate, this means v_terminal = c_fabric at the entry horizon. Level crossings of D_K eigenvalues at this point would indicate spectral reorganization analogous to Hawking radiation. The number of crossings constrains the effective temperature of the entry horizon.

Import all constants from `computations/canonical_constants.py`. Key values: v_terminal = 26.545, c_fabric = 209.97, tau_fold = 0.19.

**Computation**:
1. Load the D_K eigenvalue spectrum at multiple tau values from available spectral data. If a continuous tau-scan is not available, use the spectral action gradient data from `computations/s70_off_jensen_hess.npz` and `computations/s70_spectral_dim_flow.npz` to interpolate.
2. Identify the entry sonic horizon: tau_entry where v(tau) = c_s(tau). The transit velocity v(tau) = v_terminal * (1 - (tau - tau_fold)^2 / sigma^2)^{1/2} and c_s(tau) = sqrt(a_2(tau) / (M_ATDHFB * a_0(tau))).
3. Track each of the 8 BCS eigenvalues through tau in [0.22, 0.25] with step dtau = 0.001.
4. Count level crossings: events where lambda_m(tau) = lambda_n(tau) for m != n.
5. For each crossing, compute: (a) the gap at closest approach, (b) the crossing velocity d(lambda_m - lambda_n)/dtau, (c) whether the crossing is avoided (gap > 0) or exact (gap = 0 by symmetry).
6. The effective temperature of the entry horizon is T_entry = (1/2*pi) * |d(v - c_s)/dtau|_{tau_entry} (analog of surface gravity). Compare to T_compound from canonical_constants.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_off_jensen_hess.npz`
- `computations/s70_spectral_dim_flow.npz`
- `computations/s70_lmax7_pw.npz`

**Pre-registered gate**: **ENTRY-HORIZON-SPECTRUM-71**
- INFO: Report N_crossings and T_entry. If N_crossings > 0, the entry horizon has non-trivial spectral content.

**Output files**:
- Script: `computations/s71_entry_horizon_spectrum.py`
- Data: `computations/s71_entry_horizon_spectrum.npz`
- Working paper: Section W2-C

---

### W2-D: CAUSAL-MOMENT-MAP-71 -- Dominant Spectral Moment at Each Tau-Slice

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The S70 Hawking workshop W3-H produced a conformal diagram with six causal zones. This computation maps the dominant spectral moment (a_0, a_2, or a_4) at each tau-slice through the transit, producing a "spectral moment profile" that shows how the substrate's information content redistributes across the fold.

Import all constants from `computations/canonical_constants.py`. Key values: a0_fold = 6440, a2_fold = 2776.17, a4_fold = 1350.72.

**Computation**:
1. Load the Penrose sequence data from `computations/s70_penrose_sequence.npz`.
2. For tau in np.linspace(0.10, 0.30, 50):
   a. Compute the Seeley-DeWitt coefficients a_0(tau), a_2(tau), a_4(tau) using the spectral action at each tau. Use the polynomial interpolation from prior sessions or the gradient stiffness data.
   b. Normalize: f_k(tau) = a_k(tau) / (a_0(tau) + a_2(tau) + a_4(tau)) for k = 0, 2, 4.
   c. Record which a_k dominates (largest f_k).
3. Plot the spectral moment profile: f_0(tau), f_2(tau), f_4(tau) vs tau. Mark the fold, entry horizon, and exit horizon.
4. Identify transitions: tau values where the dominant moment changes (e.g., a_0-dominated to a_2-dominated). These are "spectral horizon" transitions.
5. Correlate with the six-layer causal structure from S70 W3-H. Do the spectral moment transitions align with the causal zone boundaries?

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_penrose_sequence.npz`
- `computations/s70_spectral_dim_flow.npz`

**Pre-registered gate**: **CAUSAL-MOMENT-MAP-71**
- INFO: Report the spectral moment profile and any transitions. Correlate with causal structure.

**Output files**:
- Script: `computations/s71_causal_moment_map.py`
- Data: `computations/s71_causal_moment_map.npz`
- Working paper: Section W2-D

---

### W2-E: DESI-DR3-SCENARIO-B-PRECISE-71 -- Fisher Forecast for Framework in DESI DR3 Scenario B

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The framework predicts w_0 = -0.918 (Volovik Scenario B, S59). DESI DR2 measured w_0 = -0.752 +/- 0.065 (2.9 sigma tension with framework). DESI DR3 will have roughly 2x the effective volume. This computation produces a Fisher forecast for the framework's discriminating power in DESI DR3.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the DESI DR2 update from `computations/s70_desi_dr3_update.npz` (contains DR2 posteriors and forecast volumes).
2. DESI DR3 Fisher matrix: scale the DR2 Fisher matrix by the volume ratio V_DR3/V_DR2 ~ 2.0 (approximate; actual depends on redshift bins). This gives sigma(w_0)_DR3 ~ sigma(w_0)_DR2 / sqrt(2) ~ 0.046.
3. Framework prediction: w_0 = -0.918 (Scenario B, S59). The tension with DR3 center: |(-0.918) - (-0.752)| / 0.046 = 3.6 sigma.
4. But: if DR3 shifts toward more negative w_0 (as hinted by DR1->DR2 trend), the tension could reduce. Compute the probability P(|w_FW - w_DR3| < 2*sigma_DR3) assuming the DR3 central value shifts by delta_w per data release.
5. Scenario B: w_a = 0.066 (framework) vs w_a ~ -1.0 (DESI DR2). Fisher forecast for w_a discrimination in DR3.
6. Report: expected sigma(w_0), sigma(w_a) for DR3, framework tension in sigma, and the posterior probability of the framework given DR3 data under Scenario B.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_desi_dr3_update.npz`
- `computations/s70_full_cov_pantheon.npz`

**Pre-registered gate**: **DESI-DR3-SCENARIO-B-PRECISE-71**
- INFO: Report expected sigma(w_0), framework tension in sigma, P(framework|DR3).

**Output files**:
- Script: `computations/s71_desi_dr3_scenario_b.py`
- Data: `computations/s71_desi_dr3_scenario_b.npz`
- Working paper: Section W2-E

---

### W2-F: 21CM-ISW-PREREGISTRATION-71 -- Full Prediction Chain Pre-Registration

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: LOW

**Prompt**:

The framework's ISW tracking signal (c_s^2 = 0, Q-SOUND-70 PASS) predicts a distinctive 21cm signal. This computation compiles the complete prediction chain -- from spectral action to q-variable to c_s^2 = 0 to ISW modification to 21cm brightness temperature -- into a pre-registration document with specific numerical predictions.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the ISW tracking data from `computations/s70_class_isw.npz` (Boltzmann ISW with c_s^2 = 0).
2. Load the 21cm prediction components from prior sessions. The 21cm brightness temperature T_b(z) depends on the neutral fraction x_HI(z), the gas temperature T_gas(z), and the matter power spectrum P(k,z). The ISW effect modifies P(k,z) at large scales.
3. Compile the prediction chain:
   a. Spectral action q-theory -> c_s^2 = 0 (Q-SOUND-70, PASS)
   b. c_s^2 = 0 -> modified ISW at low l (CLASS-ISW-70, Delta C_l > 5%)
   c. Modified ISW -> modified 21cm power at k < 0.01 h/Mpc
   d. Specific prediction: delta(T_b) / T_b at z = 10-20 from ISW modification
4. Write the pre-registration with:
   a. Central prediction: delta(T_b)/T_b at z = 15 for k = 0.01 h/Mpc
   b. Error budget: from c_s^2 uncertainty, cosmological parameter uncertainty, reionization uncertainty
   c. Discriminating power: SNR for SKA-Low, HERA distinguishing FW from LCDM at these redshifts
5. Report the full chain with numerical values at each step.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_class_isw.npz`
- `computations/s70_q_sound.npz`

**Pre-registered gate**: **21CM-ISW-PREREGISTRATION-71**
- INFO: Produce the pre-registration document with central prediction and error budget.

**Output files**:
- Script: `computations/s71_21cm_isw_preregistration.py`
- Data: `computations/s71_21cm_isw_preregistration.npz`
- Working paper: Section W2-F

---

### W2-G: DISCRETE-RW-UNIVERSALITY-71 -- Exact Velocity Distribution on CG(S_N) Graphs

**Agent**: `kitaev-quantum-chaos-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The GGE lives on the Cayley graph CG(24) of S_4 (32 vertices). The spectral dimension, return probability, and velocity distribution on this graph determine the emergent geometry. This computation extends to the family CG(S_N) for N in {24, 48, 120, 240} (corresponding to S_4, S_4xZ_2, S_5, and a larger permutation group) to test whether the velocity distribution is universal across graph sizes.

**Background**: The velocity distribution P(v) of a quantum walker on a graph encodes the transport properties. For CG(24), lambda_1 = 4 (S61, Ramanujan graph) and the spectral gap determines diffusion. If P(v) converges to a universal form as N grows, the emergent geometry is well-defined in the continuum limit.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. For each N in {24, 48, 120, 240}:
   a. Construct the Cayley graph CG(S_N) using the standard generating set (transpositions for S_N, or the relevant group presentation).
   b. Compute the graph Laplacian L = D - A where D is the degree matrix and A is the adjacency matrix.
   c. Diagonalize L: eigenvalues mu_0 = 0 < mu_1 <= ... <= mu_{N-1}.
   d. Compute the quantum walk propagator U(t) = exp(-i*L*t) for t in np.linspace(0, 10*2*pi/mu_1, 1000).
   e. Compute the mean-square displacement <r^2(t)> = sum_j |U(t)_{0j}|^2 * d(0,j)^2 where d is the graph distance.
   f. Extract the velocity distribution P(v) from the Fourier transform of <r^2(t)>.
2. Compare P(v) across the 4 graph sizes. Compute the KL divergence D_KL(P_N || P_24) for each N.
3. Gate: if D_KL < 0.1 for all N, the velocity distribution is universal.
4. Extract the spectral dimension d_s = 2 * d(ln <r^2>)/d(ln t) at large t. Compare to S63 SPECTRAL-DIMENSION-63 result (d_s = 3.34 from return probability).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s63_spectral_dimension.npz`

**Pre-registered gate**: **DISCRETE-RW-UNIVERSALITY-71**
- PASS: D_KL(P_N || P_24) < 0.1 for N in {48, 120, 240} (universal)
- FAIL: D_KL > 1.0 for any N (graph-dependent, not universal)
- INFO: intermediate KL divergences

**Output files**:
- Script: `computations/s71_discrete_rw_universality.py`
- Data: `computations/s71_discrete_rw_universality.npz`
- Working paper: Section W2-G

---

## V. Wave 3: Low Priority (depends on W1-A for spectral zeta context)

### W3-A: ALPHA-S-BAYESIAN-SHADOW-71 -- Maximum Systematic Error in a_0/a_2 from Pantheon+

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: LOW

**Prompt**:

The framework extracts a_0/a_2 from the spectral action, which determines the cosmological constant. The Pantheon+ supernova dataset constrains the expansion history and hence provides an observational bound on a_0/a_2 systematics. This computation quantifies the maximum systematic error in a_0/a_2 compatible with Pantheon+ data.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the Pantheon+ fit from `computations/s70_full_cov_pantheon.npz`.
2. The framework predicts w_0 = -0.918, which determines H(z). From H(z), the luminosity distance d_L(z) is computed. Any error in a_0/a_2 shifts w_0 and hence shifts d_L(z).
3. Propagate: delta(a_0/a_2) -> delta(w_0) -> delta(d_L) -> delta(chi^2_Pantheon).
4. Find the maximum delta(a_0/a_2) such that delta(chi^2) < 1 (1-sigma) and delta(chi^2) < 4 (2-sigma).
5. Report: max_systematic(a_0/a_2) at 1-sigma and 2-sigma.
6. Compare to the spectral zeta truncation uncertainty from W1-A (if available by Wave 3; otherwise use the PW L_max=7 truncation error from S70).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_full_cov_pantheon.npz`

**Pre-registered gate**: **ALPHA-S-BAYESIAN-SHADOW-71**
- INFO: Report max systematic and compare to spectral zeta uncertainty.

**Output files**:
- Script: `computations/s71_alpha_s_bayesian_shadow.py`
- Data: `computations/s71_alpha_s_bayesian_shadow.npz`
- Working paper: Section W3-A

---

### W3-B: CORRELATED-SENSITIVITY-71 -- d(ln omega_L)/d(alpha) on L_max=6 Spectrum

**Agent**: `lizzi-spectral-functional-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

The Leggett frequency omega_L = 0.138 M_KK was computed from the L_max=6 spectrum. This computation measures the sensitivity of omega_L to the spectral function parameter alpha (the exponent in f(x) = x^alpha), which quantifies how robust the Leggett prediction is against spectral function uncertainty.

Import all constants from `computations/canonical_constants.py`. Key values: omega_L1 = 0.138.

**Computation**:
1. Load the spectral data at L_max=6 from relevant prior computations (use `computations/s70_lmax7_pw.npz` truncated to L_max=6, or reconstruct from stored eigenvalues).
2. The spectral function f(x) = x^alpha gives the spectral action via S = Tr f(D_K^2/Lambda^2). The canonical choice is alpha = 1/2 (f(x) = sqrt(x)).
3. For alpha in {0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0}:
   a. Recompute the BCS pairing interaction using the modified spectral function.
   b. Diagonalize the BCS Hamiltonian to get the pair spectrum.
   c. Extract omega_L (Leggett frequency) from the pair excitation spectrum.
4. Compute d(ln omega_L)/d(alpha) = (1/omega_L) * d(omega_L)/d(alpha) numerically.
5. Report: the sensitivity coefficient and the range of omega_L across the alpha scan.
6. A sensitivity |d(ln omega_L)/d(alpha)| < 0.5 means omega_L is robust; > 2.0 means it is strongly spectral-function-dependent.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s70_lmax7_pw.npz`

**Pre-registered gate**: **CORRELATED-SENSITIVITY-71**
- INFO: Report sensitivity coefficient and omega_L range.

**Output files**:
- Script: `computations/s71_correlated_sensitivity.py`
- Data: `computations/s71_correlated_sensitivity.npz`
- Working paper: Section W3-B

---

### W3-C: CC-FROM-GGE-RESIDUAL-71 -- Lambda_GGE from Conserved RG Charges

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The Volovik CC mechanism (Scenario B, 0.01 OOM PASS in S66) uses the self-tuning q-variable. An alternative extraction uses the GGE conserved charges (Richardson-Gaudin integrals) directly: the vacuum energy is the ground-state energy of the GGE Hamiltonian minus the contribution from the occupied quasiparticle states. This gives Lambda_GGE without invoking q-theory.

**Background**: The GGE has 8 conserved Richardson-Gaudin integrals {R_k}. The vacuum state satisfies H_BCS|vac> = E_vac|vac> with the GGE constraint that <R_k> = r_k (fixed by the pre-transit preparation). The CC is the residual: Lambda_GGE = E_vac - sum_k r_k * epsilon_k where epsilon_k are the single-particle energies.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the GGE data from `computations/s56_gge_fabric.npz`.
2. Load the Richardson-Gaudin exact solution from `computations/s63_richardson_gaudin_n1.npz`.
3. Compute the GGE vacuum energy: E_vac = sum_k epsilon_k * <n_k> + sum_{k<l} V_{kl} * <n_k n_l> where <n_k> are the GGE occupations and V_{kl} is the pair interaction.
4. Compute the normal-state reference: E_normal = sum_k epsilon_k * theta(epsilon_F - epsilon_k).
5. Lambda_GGE = E_vac - E_normal (the condensation energy contribution to CC).
6. Convert to physical units: Lambda_GGE_phys = Lambda_GGE * M_KK^4 / Vol_SU3_Haar.
7. Compare to rho_Lambda_obs = 2.7e-47 GeV^4. Compute the gap in orders of magnitude.
8. Cross-check with the Volovik Scenario B result (0.01 OOM, S66). If consistent, the two independent extractions agree.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s56_gge_fabric.npz`
- `computations/s63_richardson_gaudin_n1.npz`

**Pre-registered gate**: **CC-FROM-GGE-RESIDUAL-71**
- PASS: |log10(Lambda_GGE_phys / rho_Lambda_obs)| < 1.0 (within 1 OOM of observation, consistent with Volovik Scenario B)
- FAIL: gap > 10 OOM (GGE residual does not reproduce CC)
- INFO: gap in [1, 10] OOM

**Output files**:
- Script: `computations/s71_cc_from_gge_residual.py`
- Data: `computations/s71_cc_from_gge_residual.npz`
- Working paper: Section W3-C

---

### W3-D: BCS-BACKREACTION-a4-71 -- Falsification Test for a_4 Under BCS

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The spectral action a_4 coefficient determines the gauge coupling constants and Higgs mass. BCS condensation modifies the effective Dirac operator D_K -> D_K + Delta, which changes a_4. This is a falsification test: if delta(a_4)_BCS / a_4 > 0.1, the BCS condensate significantly shifts the gauge couplings away from their observed values, and the framework has a problem.

Import all constants from `computations/canonical_constants.py`. Key values: a4_fold = 1350.72, Delta_BCS = 0.4643.

**Computation**:
1. Load the BCS a_4 sector data from `computations/s69_sector_bcs_a4.npz`.
2. The BCS modification to D_K: D_BCS = D_K + Delta * gamma_5 (gap matrix). The a_4 coefficient of D_BCS is:
   a_4(BCS) = a_4(D_K) + delta_a4
   where delta_a4 = Tr(Delta^4) / (4*pi^2) * (combinatorial factors from the heat kernel).
3. Compute delta_a4 using the 8-mode BCS gap structure: Delta = diag(Delta_B2, Delta_B2, Delta_B2, Delta_B2, 0, Delta_B3, Delta_B3, Delta_B3) where Delta_B2 = Delta_BCS = 0.4643 and Delta_B3 = 0.176.
4. delta_a4 / a_4 = [sum_k Delta_k^4 / (4*pi^2)] / a4_fold.
5. Gate: delta_a4/a_4 < 0.01 = PASS (BCS backreaction negligible, gauge couplings safe). delta_a4/a_4 > 0.1 = FAIL (significant shift, gauge coupling predictions compromised).
6. If PASS, compute the shift in alpha_s(M_Z) from the BCS modification: delta(alpha_s)/alpha_s = -delta_a4/a_4 (to leading order).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_sector_bcs_a4.npz`

**Pre-registered gate**: **BCS-BACKREACTION-a4-71**
- PASS: delta(a_4)_BCS / a_4 < 0.01
- FAIL: delta(a_4)_BCS / a_4 > 0.1 (gauge couplings compromised)
- INFO: ratio in [0.01, 0.1]

**Output files**:
- Script: `computations/s71_bcs_backreaction_a4.py`
- Data: `computations/s71_bcs_backreaction_a4.npz`
- Working paper: Section W3-D

---

## VI. Wave 4: Low Priority (independent)

### W4-A: GGE-HAWKING-ANALOG-71 -- BEC Analog Experiment Prediction

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

The S70 Hawking workshop's six-layer causal structure and chirp rate prediction should have an analog in BEC experiments. This computation predicts the specific heat C_V(T_eff) for a BEC analog of the transit, which is the most accessible quantity for laboratory verification.

**Background**: In a BEC analog gravity experiment, the transit corresponds to a rapidly accelerating flow that crosses the speed of sound. The GGE relic in the BEC produces a non-thermal phonon distribution. The specific heat C_V(T_eff) of this distribution deviates from the Debye T^3 law in a characteristic way that depends on the number of quasiparticle modes.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the BEC analog data from `computations/s69_bec_analog.npz`.
2. The GGE phonon distribution in the BEC analog: n_k = 1/(exp(epsilon_k / T_eff) - 1) where epsilon_k = c_s * |k| (linear dispersion) and T_eff is the effective temperature set by the quench rate.
3. Map framework parameters to BEC: T_compound -> T_eff_BEC = T_compound * (c_BEC / c_fabric) * (a_BEC / a_lattice) where c_BEC ~ 1 mm/s (typical BEC sound speed) and the lattice spacing a_BEC ~ 1 micrometer.
4. Compute C_V(T) = dE/dT for the GGE distribution:
   C_V(T) = sum_k (epsilon_k^2 / T^2) * n_k * (1 + n_k)
5. Compare to Debye: C_V_Debye(T) = (12*pi^4/5) * N * (T/T_D)^3.
6. The deviation delta_CV = (C_V - C_V_Debye) / C_V_Debye as a function of T/T_D. The GGE adds a bump at T ~ T_eff due to the quasiparticle modes.
7. Report: T_eff_BEC in kelvin, expected delta_CV, and the temperature range where the GGE signature is detectable.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_bec_analog.npz`

**Pre-registered gate**: **GGE-HAWKING-ANALOG-71**
- INFO: Report C_V(T_eff) prediction for BEC analog. If delta_CV > 10%, experimentally accessible.

**Output files**:
- Script: `computations/s71_gge_hawking_analog.py`
- Data: `computations/s71_gge_hawking_analog.npz`
- Working paper: Section W4-A

---

## VII. Constraint Gates Summary

| ID | Type | Condition | Fires If | Consequence |
|:---|:-----|:----------|:---------|:------------|
| SPECTRAL-ZETA-THRESHOLD-71 | CRITICAL | S_inf uniquely determined AND in [1.995, 2.895] | PASS | PW bottleneck resolved; m_H from converged S_inf |
| SPECTRAL-ZETA-THRESHOLD-71 | CRITICAL | S_inf divergent or outside [0.5, 10.0] | FAIL | Zeta regularization fails; new convergence method needed |
| HIGHER-ORDER-CCM-71 | CRITICAL | delta(lambda_CCM)/lambda_CCM > 0.25 | PASS | f_0 anti-correlation breakable at a_6 order |
| HIGHER-ORDER-CCM-71 | CRITICAL | delta(lambda_CCM)/lambda_CCM < 0.05 | FAIL | Anti-correlation persists; structural tension |
| INTER-SITE-ENTANGLE-71 | CRITICAL | |S_ent - predicted|/predicted < 0.20 | PASS | Entanglement entropy validates Route B A_s channel |
| INTER-SITE-ENTANGLE-71 | CRITICAL | ratio > 3.0 | FAIL | Entanglement and squeeze decoupled |
| DECOHERENCE-BAND-71 | CRITICAL | Pair count < 1% AND decoherence in [1.12, 26.5] | PASS | SU(1,1) compound consistent; info paradox resolved |
| DECOHERENCE-BAND-71 | CRITICAL | Pair count > 5% | FAIL | SU(1,1) representation inconsistency |
| NON-TRIVIAL-FIBRATION-CSQUARED-71 | HIGH | delta(c_s^2) < 10^{-3} AND delta(alpha_s)/alpha_s > 0.5 | PASS | c_s^2=0 robust; alpha_s relieved by fibration |
| WEYL-TWO-LOOP-71 | HIGH | delta_2(|C|^2)/|C|^2 < 10^{-6} | PASS | All-orders BCS gravitational protection |
| BH-THIRD-LAW-71 | HIGH | S_projected/(pi*Q^2) in [0.5, 2.0] | PASS | BH entropy from spectral projection |
| THREE-CELL-GSL-71 | HIGH | S_gen monotone at 4/4 stages | PASS | GSL extends to frustrated ring topology |
| R-SPATIAL-SCAN-71 | MEDIUM | INFO | Always | Reports r_spatial_critical for gap closure |
| CHIRP-UNIVERSALITY-71 | MEDIUM | k_chirp difference < 10% in stationary limit | PASS | Universal chirp rate validated |
| ENTRY-HORIZON-SPECTRUM-71 | MEDIUM | INFO | Always | Reports N_crossings and T_entry |
| CAUSAL-MOMENT-MAP-71 | MEDIUM | INFO | Always | Reports spectral moment profile |
| DESI-DR3-SCENARIO-B-PRECISE-71 | MEDIUM | INFO | Always | Fisher forecast for DR3 discrimination |
| 21CM-ISW-PREREGISTRATION-71 | MEDIUM | INFO | Always | Pre-registration document produced |
| DISCRETE-RW-UNIVERSALITY-71 | MEDIUM | D_KL < 0.1 for all N | PASS | Velocity distribution universal |
| ALPHA-S-BAYESIAN-SHADOW-71 | LOW | INFO | Always | Max systematic from Pantheon+ |
| CORRELATED-SENSITIVITY-71 | LOW | INFO | Always | omega_L sensitivity to spectral function |
| CC-FROM-GGE-RESIDUAL-71 | LOW | |gap| < 1.0 OOM | PASS | Independent CC extraction agrees with Volovik |
| BCS-BACKREACTION-a4-71 | LOW | delta(a_4)/a_4 < 0.01 | PASS | Gauge couplings safe under BCS |
| GGE-HAWKING-ANALOG-71 | LOW | INFO | Always | BEC analog prediction |

---

## VIII. Decision Points

### After Wave 1

1. **SPECTRAL-ZETA-THRESHOLD-71 (W1-A)**: This is the session's critical path.
   - If PASS (S_inf converged in [1.995, 2.895]): The PW convergence bottleneck is resolved. Propagate S_inf to all downstream quantities (m_H, a_0/a_2, alpha_s). Wave 3 computations W3-A and W3-B can use the converged value instead of the PW estimate. The A_s gap budget gains a firm spectral action normalization.
   - If FAIL (divergent): The 992-mode spectrum is insufficient for zeta regularization. Two recovery paths: (a) extend to L_max=8+ (higher computational cost), or (b) use the heat kernel coefficients directly (bypasses eigenvalue sum entirely). Carry forward to S72 as ZETA-EXTENDED-72.
   - If INFO (converged but outside range): The spectral action normalization is non-standard. Re-examine the spectral function family and check whether the Aitken extrapolation from S66 was biased by PW oscillations.

2. **HIGHER-ORDER-CCM-71 (W1-B)**: If PASS (anti-correlation broken), the f_0 optimization problem gains a new degree of freedom and the alpha_s/CC tension may have a simultaneous resolution. If FAIL, the tension is at least a_6-deep and requires either a new CC mechanism or a non-perturbative spectral function.

3. **INTER-SITE-ENTANGLE-71 (W1-C)**: If PASS, the Route B A_s channel (entanglement-based squeeze) is quantitatively confirmed. Combined with W1-D, this closes the A_s gap budget to potentially < 0.1 OOM. If FAIL, Route B is excluded and the gap remains at 0.267 OOM.

4. **DECOHERENCE-BAND-71 (W1-D)**: If PASS (pair count conserved, decoherence in band), the compound SU(1,1) squeeze is self-consistent and the information paradox analog is resolved. If pair count fails, the SU(1,1) representation for the compound operation is incorrect and the three squeeze channels cannot be simply multiplied.

### After Wave 2

5. **R-SPATIAL-SCAN-71 (W2-A)**: If r_spatial_critical is in [0.45, 0.65], modest changes to the thermal phase coherence close the A_s gap. If > 1.0, the spatial squeeze channel alone is insufficient.

6. **CHIRP-UNIVERSALITY-71 (W2-B)**: Frame-independence of the chirp rate validates its use as a universal diagnostic. If frame-dependent, the prediction must be qualified with a reference frame specification.

7. **DISCRETE-RW-UNIVERSALITY-71 (W2-G)**: If universal, the CG(24) spectral dimension and velocity distribution are independent of graph size -- supporting the emergent geometry picture. If graph-dependent, finite-size corrections are needed.

### After Wave 3

8. **CC-FROM-GGE-RESIDUAL-71 (W3-C)**: If the GGE residual extraction agrees with Volovik Scenario B (< 1 OOM), this is an independent confirmation of the CC mechanism from a completely different computational route. Two independent extractions agreeing is qualitatively stronger than either alone.

9. **BCS-BACKREACTION-a4-71 (W3-D)**: If PASS (delta < 1%), the gauge coupling predictions are safe under BCS condensation. This is a falsification test -- FAIL would mean the post-transit state modifies particle physics predictions.

### After Wave 4

10. **Full session assessment**: With all 20 gates computed, update:
    - A_s gap budget (incorporating W1-A zeta normalization, W1-C entanglement, W1-D decoherence, W2-A r_spatial scan)
    - f_0/alpha_s/CC status (W1-B higher-order CCM, W3-B sensitivity)
    - Causal structure (W2-C entry horizon, W2-D moment map)
    - Observational scorecard (W2-E DESI DR3, W2-F 21cm pre-registration)
    - Analog experiment predictions (W2-B chirp, W4-A BEC analog)

---

## IX. Execution Notes

- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- **Output directory**: `computations/`
- **Script prefix**: `s71_`
- **Results file**: `sessions/archive/session-71/session-71-results-workingpaper.md`
- **Total computations**: 20
- **Wave distribution**: W1 (8), W2 (7), W3 (4), W4 (1)
- **Estimated cost**: 20 agents x opus = HIGH total; expect 4-8 hours with parallel execution per wave
- **Input file verification**: All referenced .npz files have been verified to exist in computations/
- **Convention**: All scripts MUST `from canonical_constants import *` and MUST NOT hardcode M_KK, Delta, a_0, a_2, a_4, or tau_fold
- **Critical path**: W1-A (SPECTRAL-ZETA-THRESHOLD-71) -> spectral action normalization -> all amplitude-dependent quantities. This single computation determines the session's strategic outcome.
- **Substrate framing reminder**: All agents must frame results in substrate language (spectral action, fiber excitations, GGE physics) per the phononic framing rules. Container thinking (space expands, fields in curved spacetime) must be corrected in prompts.
- **Carry-forward compliance**: All 20 carry-forward items from S70 workshops and syntheses appear as planned computations. None deferred.
