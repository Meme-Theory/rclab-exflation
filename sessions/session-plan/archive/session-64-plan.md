# Session 64 Plan: CCCCCC-ombo Breaker

**Date**: 2026-04-01
**Author**: Team-lead (main agent, /rclab-plan)
**Format**: Parallel single-agent computations across 8 waves
**Source**: S63 workshops (Hawking-QA, Volovik-VdD), 7 CC path investigations, S62 carry-forward, framework-cc-oom.md
**Motivation**: All 7 CC path agents converged on Path C (transit-as-relaxation) as the sole path with the correct OOM. S-ASYMPTOTIC-64 is the single most important computation in the framework's history. This session resolves it, tests Path B as the complementary channel, and advances the observational chain.
**Results file**: `sessions/archive/session-64/session-64-results-workingpaper.md`

---

## I. Session Objective

Determine whether the cosmological constant problem has a dynamical resolution through transit-as-relaxation (Path C), supported by gravitational integrability breaking (Path B). Secondary: advance the observational chain (tensor spectrum, A_s transfer function, n_s refinement) and close carry-forward items from S62-S63.

**Pre-registered master gate**:
- **CC-COMBO-64**: The combined B+C path
- **PASS**: S-ASYMPTOTIC-64 PASS AND (R-G-CHARGE-DECOMPOSITION-64 PASS OR SA-VERSUS-JACOBSON-64 PASS)
- **FAIL**: S-ASYMPTOTIC-64 FAIL (Path C blocked, regardless of Path B)
- **Null hypothesis**: The spectral action does not relax beyond the fold (a_2 asymptotes to nonzero constant). The CC remains a single 114-OOM monolithic problem.

## II. Wave Structure

### Dependency Graph

```
Wave 1 (parallel, no dependencies — THE CRITICAL WAVE):
  W1-A  W1-B  W1-C  W1-D  W1-E

    Decision Point: If W1-A FAIL → pivot entire session to Path A/E/observational
    Decision Point: If W1-C PASS → 114 OOM gap is category error (transformative)

Wave 2 (parallel, depends on W1 results for interpretation):
  W2-A  W2-B  W2-C  W2-D  W2-E

Wave 3 (parallel, some depend on W1-W2):
  W3-A  W3-B  W3-C  W3-D  W3-E

Wave 4 (parallel, observational chain):
  W4-A  W4-B  W4-C  W4-D

Wave 5 (parallel, CC deep structure):
  W5-A  W5-B  W5-C  W5-D

Wave 6 (parallel, observational confrontation — depends on W3-W4):
  W6-A  W6-B  W6-C  W6-D

Wave 7 (parallel, carry-forward + remaining):
  W7-A  W7-B  W7-C  W7-D

Wave 8: Workshops + Synthesis (depends on all prior waves)
```

---

## III. Wave 1: The Critical Wave — Path C + B Foundation

### W1-A: S-ASYMPTOTIC-64 — Spectral Action Beyond the Fold

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW (eigenvalue computation at 6 tau values, minutes not hours)

**Prompt**:

The single most important computation in the framework's history. Compute the spectral action S(tau) and its Seeley-DeWitt coefficients a_0, a_2, a_4 at tau values BEYOND the fold (tau = 0.190).

**Context**: The transit-as-relaxation mechanism (Path C) predicts rho_vac(t) ~ S_fold * (t_fold/t_0)^{-2} ~ 2.5e-116 M_KK — within 2 OOM of observed Lambda. But Theorem T14 says a_0 = const (tau-independent), creating a floor. The question: does S(tau) approach a_0*f(0) from above, with the excess relaxing as a power law?

**Method**:
1. Read the D_K eigenvalue computation code (computations/s42_gradient_stiffness.py or similar)
2. Modify the Jensen deformation parameter to compute eigenvalues at tau = 0.30, 0.50, 1.0, 2.0, 5.0, 10.0
3. For each tau, compute the full heat kernel K(t) = sum_n d_n exp(-lambda_n^2 * t) at 20 t-values
4. Extract a_0, a_2, a_4 from small-t polynomial regression of t^4 * K(t)
5. Compute S(tau) = sum_n d_n f(lambda_n^2/Lambda^2) with Gaussian cutoff f(x) = exp(-x), Lambda = M_KK
6. Compute dS/dtau by finite difference
7. Fit a_2(tau) to power law a_2 ~ tau^{-alpha} on log-log plot. Extract alpha and R^2.
8. Verify a_0(tau) = const = 6440 at all tau (calibration check)

**Pre-registered gate**: S-ASYMPTOTIC-64
- PASS: a_2(tau) monotonically decreasing for tau > 0.19; power-law fit alpha > 0, R^2 > 0.9; S(tau) approaches 6440 from above
- FAIL: a_2(tau) NOT monotone decreasing (increases, oscillates, or asymptotes with a_2(10)/a_2(0.19) > 0.5)
- INFO: a_2 decreases but alpha < 1 (partial relaxation, exponent determination)

**Input**: D_K eigenvalue code from computations/, canonical_constants.py
**Output**:
1. Script: `computations/s64_s_asymptotic.py`
2. Data: `computations/s64_s_asymptotic.npz`
3. Plot: `computations/s64_s_asymptotic.png` (S(tau), a_0(tau), a_2(tau), a_4(tau) vs tau, log-log for a_2)
4. Results: Section W1-A of working paper

---

### W1-B: R-G-CHARGE-DECOMPOSITION-64 — Which Charges Does Gravity Break?

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM (Richardson-Gaudin charge algebra on 8 modes)

**Prompt**:

Decompose the 8 Richardson-Gaudin conserved charges of the BCS condensate on D_K into their spectral content. Determine which charges are broken by the O(alpha_G) gravitational perturbation (EIH self-energy). Compute the overlap of each charge with the vacuum energy density operator rho_ZP.

**Context**: The gravitational channel breaks Gaudin integrability by 3.88% (S63 W6-02). But the dominant condensate mode B2[0] has C_2(0,0)=0 for Peter-Weyl Casimir, though C_2^{iso}=3 for isometry Casimir (cc-path-g.md correction). The question: do the broken charges include those conjugate to the vacuum energy?

**Method**:
1. Construct the 8 Richardson-Gaudin conserved charges R_k = sum_j [S_j^+ S_k^- / (eps_j - eps_k)] for the 8 BCS modes on D_K
2. Apply the gravitational perturbation delta_eps_k = -(1/2) alpha_G eps_k^2 (1 + C_2^{iso}(k)/3) to each mode
3. Compute the commutator [R_k, H_grav] for each charge
4. Identify which charges have [R_k, H_grav] ≠ 0 (broken) vs = 0 (preserved)
5. Compute the overlap <R_k | rho_ZP> where rho_ZP = (1/2) sum_j omega_j n_j
6. Classify: charges broken by gravity that overlap with rho_ZP are the CC-relevant channels

**Pre-registered gate**: R-G-CHARGE-DECOMPOSITION-64
- PASS: At least one charge with |<R_k|rho_ZP>| > 0.01 * max(|<R_j|rho_ZP>|) is broken
- FAIL: All broken charges have |<R_k|rho_ZP>| < 0.01 * max

**Input**: BCS mode data from S52/S61, canonical_constants.py, alpha_G = 9.3e-4
**Output**:
1. Script: `computations/s64_rg_charge_decomp.py`
2. Data: `computations/s64_rg_charge_decomp.npz`
3. Results: Section W1-B of working paper

---

### W1-C: SA-VERSUS-JACOBSON-64 — Is the 114 OOM Gap a Category Error?

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: ZERO (purely analytical — variational calculus)

**Prompt**:

Determine whether the spectral action's vacuum energy (rho_SA = a_0 M_KK^4 / (8 pi G)) is the SAME quantity as the Jacobson integration constant Lambda. If they are different quantities, the 114-OOM gap is a category error — we are comparing apples to oranges.

**Context**: The Jacobson derivation (dQ = T dS at Rindler horizons) produces G_ab + Lambda g_ab = 8 pi G T_ab with Lambda undetermined. The spectral action produces the Einstein-Hilbert action with a cosmological term proportional to a_0. The question: does varying the spectral action produce the SAME Lambda that appears in Jacobson's equation, or are they different objects?

**Method**:
1. Write the spectral action S = Tr f(D^2/Lambda_cutoff^2) in the Seeley-DeWitt expansion
2. Vary with respect to the metric: delta S / delta g^{mu nu} = 0
3. Identify the cosmological constant term Lambda_SA in the variational equations
4. Compare Lambda_SA with the Jacobson integration constant Lambda_J
5. Determine: are they the same object (Lambda_SA = Lambda_J) or different?

**Pre-registered gate**: SA-VERSUS-JACOBSON-64
- PASS: Lambda_SA ≠ Lambda_J (they are different quantities; the 114 OOM gap compares the wrong things)
- FAIL: Lambda_SA = Lambda_J = rho_SA / (8 pi G) (the gap is real and both quantities are the same)

**Input**: Spectral action formalism from Chamseddine-Connes-van Suijlekom 2019 (Paper 20 in researchers/)
**Output**:
1. Analysis: Section W1-C of working paper (no script needed — analytical)
2. If PASS: identify what Lambda_J actually IS in terms of spectral data

---

### W1-D: OCC-SPEC-45 — Occupied-State Spectral Action

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute the occupied-state spectral action S_occ(tau=0.190) using BCS occupation numbers from S35/S38. This is the single highest-EVOI computation for the amplitude chain (A_s, f_DM, sigma_8).

**Context**: The full spectral action S_fold = 250,361 sums over ALL 12,880 eigenvalues. But only occupied modes contribute to physical observables. The BCS occupation numbers n_k from S35/S38 weight each mode. If S_occ ~ 5 (only (0,0) sector), the A_s gap drops from 7.6 OOM to 2.93 OOM. If S_occ ~ 0.005, the gap closes.

**Method**:
1. Load D_K eigenvalues at tau = 0.190 from S61/S63 data
2. Load BCS occupation numbers n_k from S35/S38 data (or recompute from Delta = 0.464 M_KK)
3. Compute S_occ = sum_n d_n * n_k * f(lambda_n^2/Lambda^2) with Gaussian cutoff
4. Compare with S_fold = 250,361
5. Compute the ratio S_occ/S_fold and the effective number of contributing modes
6. Report: revised A_s gap = log10(S_occ * M_KK^4 / A_s^{obs})

**Pre-registered gate**: OCC-SPEC-64
- INFO: Report S_occ value and revised A_s gap
- Threshold: If S_occ < 100 (< 0.04% of S_fold), A_s gap < 5 OOM — significant progress

**Input**: D_K eigenvalues, BCS data, canonical_constants.py
**Output**:
1. Script: `computations/s64_occ_spec.py`
2. Data: `computations/s64_occ_spec.npz`
3. Results: Section W1-D of working paper

---

### W1-E: EPSILON-PROFILE-64 — Slow-Roll Parameter at 6 Tau Values

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: LOW (supporting computation for TENSOR-BURST in W3)

**Prompt**:

Compute the slow-roll parameter epsilon(tau) = (1/2)(S'(tau)/S(tau))^2 at 6 tau values across the transit. This is required input for the tensor spectrum computation (W3-A).

**Method**:
1. Load S(tau) values from the existing spectral action curve (or compute if W1-A provides new data)
2. Compute S'(tau) by finite difference
3. Compute epsilon(tau) = (1/2)(S'/S)^2 at tau = 0.05, 0.10, 0.15, 0.190, 0.25, 0.30
4. Also compute eta(tau) = epsilon'/(epsilon * H) at each point
5. Report the profile and identify the transit region where epsilon > 1 (supersonic)

**Pre-registered gate**: INFO (no pass/fail — supporting data)

**Input**: S(tau) curve from S61/S63 or W1-A
**Output**:
1. Script: `computations/s64_epsilon_profile.py`
2. Data: `computations/s64_epsilon_profile.npz`
3. Plot: `computations/s64_epsilon_profile.png`
4. Results: Section W1-E of working paper

---

## V. Decision Points

**After Wave 1**:
- If W1-A (S-ASYMPTOTIC-64) **FAIL** → Path C is closed. Pivot remaining waves to Path A (Jacobson selection principle), Path E (mathematical foundation), and observational chain. The CC remains monolithic 114 OOM.
- If W1-A **PASS** → Path C is the primary CC track. All subsequent waves support it.
- If W1-A **INFO** (partial relaxation, alpha < 1) → Path C is viable for rho_curv but insufficient alone. Continue with B+C combination.
- If W1-C (SA-VERSUS-JACOBSON-64) **PASS** → The 114 OOM gap is a category error. This is TRANSFORMATIVE. Immediately spawn a dedicated investigation.
- If W1-B (R-G-CHARGE-DECOMPOSITION-64) **PASS** → Path B gains a dynamical mechanism. Feed results to W2 computations.

---

## IV. Wave 2: Path C Support + Path B Verification

### W2-A: BCS-DRESSED-SA-64 — BdG Spectral Action at Multiple Tau

**Agent**: `connes-ncg-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the BCS-dressed spectral action S^{BCS}(tau) at 5 tau values (0.19, 0.50, 1.0, 2.0, 5.0). Extract eps_H^{BCS}. Determine whether BCS dressing modifies the asymptotic profile from W1-A.

**Method**:
1. Construct the BdG Dirac operator D_BdG(tau) at each tau value using Delta = 0.464 M_KK
2. Compute S^{BCS}(tau) = Tr f(D_BdG^2/Lambda^2)
3. Extract a_2^{BCS}(tau) from heat kernel
4. Compare a_2^{BCS}(tau) profile with a_2^{bare}(tau) from W1-A
5. Extract eps_H^{BCS} = (S'^{BCS})^2 / (2 S^{BCS} S''^{BCS})

**Pre-registered gate**: BCS-DRESSED-SA-64
- PASS: |eps_H^{BCS} - eps_H^{bare}| / eps_H^{bare} > 0.01 (detectable BCS shift)
- INFO: n_s^{BCS} value and direction of shift (toward or away from Planck 0.9649)

**Input**: D_K eigenvalues, BCS gap Delta, W1-A data
**Output**: Script, data, plot, Section W2-A of working paper

---

### W2-B: SELF-CONSISTENT-NE-64 — Exact e-Fold Count

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute the self-consistent number of e-folds N_e = integral H(tau)/v_transit dtau across the transit. Current estimates: naive = 0.17, self-consistent expected ~ 0.003. This anchors the tensor burst width and r_CMB through the duty-cycle factor.

**Method**:
1. Use G_eff from the a_2 Seeley-DeWitt coefficient (not the S61 retracted H_fold)
2. Compute H(tau) = sqrt(rho(tau) / (3 M_Pl^2)) using the Friedmann equation with the spectral action potential
3. Compute v_transit from the moduli space kinetic energy
4. Integrate N_e across tau in [0.05, 0.30]

**Pre-registered gate**: SELF-CONSISTENT-NE-64
- INFO: Report N_e value. If N_e < 0.01, tensor burst is extremely narrow (duty-cycle suppression of r).

**Input**: S(tau) curve, G_eff, canonical_constants.py
**Output**: Script, data, Section W2-B of working paper

---

### W2-C: SECTOR-SELECTIVE-BREAKING-64 — Indirect Feedback to (0,0)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the indirect gravitational feedback to the (0,0) condensate mode at O(alpha_G^2). The direct shift is via isometry Casimir C_2^{iso}=3 at O(alpha_G). The indirect feedback through the BCS gap equation couples B3 shifts back to Delta and hence to v_{B2[0]}^2.

**Method**:
1. Apply gravitational eigenvalue shifts to all 8 BCS modes
2. Solve the self-consistent BCS gap equation with shifted energies
3. Extract the change in v_{B2[0]}^2 (condensate fraction of dominant mode)
4. Compute |delta_Lambda/Lambda_CC| from the shift in v_{B2[0]}^2

**Pre-registered gate**: SECTOR-SELECTIVE-BREAKING-64
- PASS: |delta_Lambda/Lambda_CC| > 10^{-6}
- Expected: ~10^{-3} (PASS with 111 OOM shortfall remaining)

**Input**: BCS mode data, alpha_G = 9.3e-4, cc-path-g.md computation design
**Output**: Script, data, Section W2-C of working paper

---

### W2-D: N-PAIR-3-RG-64 — Does N_pair=3 Break Integrability?

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the level spacing statistics for the Richardson-Gaudin model at N_pair=3 on the CG(24) fabric. If N_pair=3 shows Wigner-Dyson statistics (instead of Poisson), integrability breaks at finite N — critical for whether the CC can relax through multi-pair mechanisms.

**Method**:
1. Solve the Richardson-Gaudin equations for N_pair = 1, 2, 3 on the 8-mode D_K spectrum
2. Compute the many-body energy spectrum for each N_pair
3. Compute <r> (mean ratio of consecutive spacings) for each
4. Poisson: <r> = 0.386. GOE (Wigner-Dyson): <r> = 0.530. Transition: 0.414 (current at N_pair ~ large).

**Pre-registered gate**: N-PAIR-3-RG-64
- PASS: <r>(N=3) > 0.45 (approaching Wigner-Dyson, integrability breaking)
- FAIL: <r>(N=3) < 0.40 (Poisson persists, integrability intact)
- INFO: <r>(N=3) in [0.40, 0.45] (transition regime)

**Input**: D_K eigenvalues, BCS gap, Richardson-Gaudin solver
**Output**: Script, data, Section W2-D of working paper

---

### W2-E: FINITE-SIZE-VACUUM-ENERGY-64 — E(N=0) Verification

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute E(N=0) — the total spectral action of the unpaired substrate divided by the number of emergent cells. This is the Gibbs-Duhem prediction for the vacuum energy at N_pair=1.

**Method**:
1. Compute E(N=0) = S_fold / N_cells where N_cells is the tessellation count
2. Verify E(0) / (S_fold/N_cells) = 1.00 +/- 0.01 (Gibbs-Duhem consistency)
3. Report E(0) in M_KK units and the OOM gap vs rho_observed

**Pre-registered gate**: FINITE-SIZE-VACUUM-ENERGY-64
- INFO: Verify Gibbs-Duhem prediction. Report gap.

**Input**: S_fold = 250,361, N_cells from S43/S61
**Output**: Script, Section W2-E of working paper

---

## V-2. Decision Points (after Wave 2)

**After Wave 2**:
- If W2-D (N-PAIR-3-RG-64) shows Wigner-Dyson → Path B gains multi-pair mechanism. Spawn follow-up in W5.
- If W2-A (BCS-DRESSED-SA-64) shifts n_s toward Planck → the 1.9-sigma tension has a resolution candidate.

---

## Wave 3: Tensor + Transfer Function + Phonon Structure

### W3-A: TENSOR-BURST-64 — Full Second-Order Tensor Spectrum

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Solve the second-order tensor mode equation with the actual epsilon(tau) transit profile (from W1-E). Compute the full P_T(k) spectrum including Bogoliubov coefficients beta_k = 1.015 and duty-cycle concentration.

**Method**:
1. Load epsilon(tau) profile from W1-E
2. Solve the Mukhanov-Sasaki tensor equation: d²h_k/deta² + (k² - a''/a) h_k = 0
3. Use Bogoliubov initial conditions with |beta_k|^2 = 1.015
4. Compute P_T(k) = (2/M_Pl^2) * k^3 |h_k|^2 / (2 pi^2)
5. Compute r_CMB = P_T(k_CMB) / P_S(k_CMB)
6. Apply duty-cycle factor from N_e (W2-B if available, or use both N_e = 0.17 and 0.003)

**Pre-registered gate**: TENSOR-BURST-64
- PASS: r_CMB < 0.036 (BICEP/Keck)
- FAIL: r_CMB > 0.1
- INFO: r_CMB in [0.036, 0.1]

**Input**: epsilon(tau) from W1-E, beta_k = 1.015, c_s = 0.485
**Output**: Script, data, plot, Section W3-A of working paper

---

### W3-B: BDG-KASPAROV-64 — First BdG Seeley-DeWitt Coefficient

**Agent**: `van-den-dungen-bridge-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute a_2(D_BdG^2) at the fold (tau=0.19) using the exact BdG heat kernel on 992 eigenvalues. This is the first computation of a Seeley-DeWitt coefficient from the BdG Kasparov product — connecting NCG directly to emergent gravity at the Sakharov level.

**Method**:
1. Construct the 1984-dimensional D_BdG from the 992 D_K eigenvalues + BCS gap Delta = 0.464 M_KK
2. Compute heat kernel K_BdG(t) = Tr exp(-D_BdG^2 t) at 20 t-values
3. Extract a_2^{BdG} from small-t expansion
4. Compare with Sakharov result: delta_a2/a_2 = -0.361 (W6-13 Method 2)

**Pre-registered gate**: BDG-KASPAROV-64
- PASS: |a_2^{BdG}/(0.639 * a_2^{bare}) - 1| < 0.10
- FAIL: Disagreement > 10%

**Input**: D_K eigenvalues at tau=0.19, Delta = 0.464 M_KK
**Output**: Script, data, Section W3-B of working paper

---

### W3-C: LINEWIDTH-HIERARCHY-64 — Phonon Linewidth Ordering

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the phonon linewidths Gamma_{B1}, Gamma_{B2}, Gamma_{B3} from the imaginary part of the two-loop self-energy on the CG(24) fabric. The predicted hierarchy is Gamma_B3 > Gamma_B1 > Gamma_B2 (inverted vs occupation).

**Method**:
1. Construct the phonon self-energy Sigma_k(omega) at two-loop order for each BCS branch
2. Extract Im[Sigma_k(omega_k)] = Gamma_k / 2
3. Compare B1, B2, B3 linewidths
4. Report the hierarchy and the ratio Gamma_B3/Gamma_B2

**Pre-registered gate**: LINEWIDTH-HIERARCHY-64
- PASS: Gamma_B3 > Gamma_B1 > Gamma_B2
- FAIL: Different ordering

**Input**: BCS mode data, scattering matrix from W3-05 (S63)
**Output**: Script, data, Section W3-C of working paper

---

### W3-D: TRANSFER-BOGOLIUBOV-64 — A_s Transfer Function

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute |beta_proj|^2 for the fiber-to-4D projection of (0,0)-sector spectral action perturbations through the 16 hybridization gaps. This is the missing transfer function that bridges the 56-OOM scale hierarchy between KK and CMB.

**Method**:
1. Identify the (0,0)-sector modes in the D_K spectrum (Peter-Weyl selection)
2. Compute the Bogoliubov transformation projecting fiber perturbations to 4D scalar perturbations
3. Pass through each of the 16 hybridization gaps (from PHONON-DISP-FULL-62)
4. Compute total |beta_proj|^2
5. Test sensitivity: vary cutoff scheme (Gaussian, sharp, zeta) and check variation

**Pre-registered gate**: TRANSFER-BOGOLIUBOV-64
- PASS: |beta_proj|^2 varies by < factor 2 across cutoff choices (trans-Planckian universality)
- FAIL: Sensitive to gap details (> factor 10 variation)

**Input**: D_K eigenvalues, hybridization gap data from S62, S_gilkey = 5.15
**Output**: Script, data, Section W3-D of working paper

---

### W3-E: SOUND-SPEED-63 — Acoustic Sound Speed (S62 carry-forward)

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute c_s(tau_fold) — the acoustic sound speed at the fold from the spectral action moduli space metric. This is an S62 carry-forward item that feeds into the observational chain (n_s correction, A_s normalization).

**Method**:
1. Compute G_{tau tau} from the moduli space metric of the spectral action
2. Extract c_s = 1 / sqrt(1 + G_{tau tau})
3. Verify c_s < 1 (causality) and compare with c_s = 0.485 (S56 BLV result)

**Pre-registered gate**: SOUND-SPEED-64
- PASS: c_s < 1 (causal)
- FAIL: c_s > 1 (acausal)
- INFO: c_s value and comparison with BLV result

**Input**: S(tau) curve, moduli space metric
**Output**: Script, data, Section W3-E of working paper

---

## Wave 4: Observational Chain

### W4-A: MUKHANOV-SASAKI-64 — Acoustic Transfer Function (S62 carry-forward)

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Solve the exact Mukhanov-Sasaki mode equation with the S(tau) profile and eta_H = -22. Extract n_s at horizon exit. This is the definitive n_s computation (beyond the slow-roll approximation).

**Input**: S(tau) curve, c_s from W3-E
**Pre-registered gate**: MUKHANOV-SASAKI-64. PASS: n_s in [0.93, 0.99]. FAIL: outside [0.85, 1.00].
**Output**: Script, data, plot, Section W4-A of working paper

---

### W4-B: KK-THRESHOLD-64 — L=6 Convergence Test (S62 carry-forward, MANDATORY)

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the KK threshold correction delta g_3^{-2} at L=6 (extending S62's L=3 result of 1.41). This determines whether the Higgs mass prediction is real or an artifact of premature truncation.

**Input**: D_K eigenvalues at L_max=6, Dynkin indices T(p,q)
**Pre-registered gate**: KK-THRESHOLD-64. PASS: delta g_3^{-2} in [0.73, 1.48] (m_H in [120, 135] GeV). FAIL: outside [0.30, 5.0].
**Output**: Script, data, Section W4-B of working paper

---

### W4-C: PHASE-BOGOLIUBOV-64 — CMB Peak Phases

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute the Bogoliubov phases phi_k^{Bog} at the first 7 CMB acoustic peak wavenumbers. Construct the phase-position transfer matrix T_{nl}. This is the framework's most original pre-registerable prediction.

**Input**: S61 Bogoliubov data, CMB peak wavenumbers
**Pre-registered gate**: PHASE-BOGOLIUBOV-64. INFO: Report phases and predicted peak shifts.
**Output**: Script, data, Section W4-C of working paper

---

### W4-D: DESI-DV-64 — Model-Independent DESI Comparison

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute D_V(z)/r_s from substrate compaction w(z) at each DESI redshift bin, bypassing CPL parameterization. Pre-register DR3 decision rules.

**Input**: w(z) from substrate compaction (S59-S60), DESI DR2 data
**Pre-registered gate**: DESI-DV-64. Decision rules: w_a < -0.53 excludes at 3-sigma.
**Output**: Script, data, Section W4-D of working paper

---

## Wave 5: CC Deep Structure

### W5-A: POST-TRANSIT-THERMODYNAMICS-64 — GSL Entropy Trajectory

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Trace S_gen(tau) step by step from BCS (S=0) through transit to GGE (S=3.542 bits). Include sector-resolved entropy trajectories. Verify GSL at every stage.

**Pre-registered gate**: POST-TRANSIT-THERMODYNAMICS-64. PASS: S_gen monotone. FAIL: any decrease.
**Output**: Script, data, Section W5-A of working paper

---

### W5-B: SPECTRAL-MONOTONICITY-LINK-64 — CC ↔ Area Theorem

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: LOW (analytical)

**Prompt**:

If a Level 0 spectral modification breaks CC monotonicity, does it also break the area theorem at Level 3? Determine whether the spectral monotonicity hierarchy is rigid (CC and area theorem linked) or flexible (can break CC without breaking area theorem).

**Pre-registered gate**: SPECTRAL-MONOTONICITY-LINK-64. PASS: quantitatively linked. FAIL: decouple.
**Output**: Analysis, Section W5-B of working paper

---

### W5-C: LOCAL-ENTANGLE-64 — Local Entanglement Entropy (S62 carry-forward)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute S_ent(local) of the GGE across a Rindler cut on the CG(24) fabric using the Peschel correlation matrix method. This was identified in S62 as the "breakthrough opening" for the CC.

**Input**: GGE occupation numbers, CG(24) adjacency matrix
**Pre-registered gate**: LOCAL-ENTANGLE-64. INFO: S_ent value. If S_ent = 0, Jacobson Lambda = 0.
**Output**: Script, data, Section W5-C of working paper

---

### W5-D: JACOBSON-GGE-64 — Jacobson for Non-Thermal Matter (S62 carry-forward)

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: LOW (analytical)

**Prompt**:

Extend the Jacobson thermodynamic derivation (dQ = T dS at Rindler horizons) to GGE matter with mode-dependent temperatures. Determine if the derivation still produces Einstein's equations and what Lambda becomes.

**Input**: GGE temperatures from S63, Jacobson formalism
**Pre-registered gate**: JACOBSON-GGE-64. INFO: Does derivation extend? If yes, Lambda value.
**Output**: Analysis, Section W5-D of working paper

---

## Wave 6: Observational Confrontation

### W6-A: NS-ACOUSTIC-64 — Final n_s with All Corrections

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW

**Prompt**: Compute n_s = 1 - 2*eps_H - s_H with c_s from W3-E, BCS correction from W2-A, and one-loop from S63 W6-04. Report final n_s and tension with Planck.

**Pre-registered gate**: NS-FINAL-64. PASS: n_s in [0.955, 0.975].
**Output**: Section W6-A of working paper

---

### W6-B: CHIRALITY-SELECTION-64 — KO Chirality Cancellation

**Agent**: `dirac-antimatter-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**: Compute the KO chirality cancellation factor in r^{(2)} from N_+=N_-=6270 and D_K eigenvalue pairs.

**Pre-registered gate**: CHIRALITY-SELECTION-64. INFO: cancellation magnitude.
**Output**: Section W6-B of working paper

---

### W6-C: VAB-RANK-64 — Spectral Action Second Variation Rank

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM

**Prompt**: Compute the rank of the spectral action's second variation matrix for the third Yukawa direction. If rank >= 3, the non-separable part provides a third independent generation direction.

**Pre-registered gate**: VAB-RANK-64. PASS: rank >= 3. FAIL: rank < 3.
**Output**: Script, data, Section W6-C of working paper

---

### W6-D: QUANTUM-METRIC-64 — Peotta-Torma D_s Test (S62 carry-forward)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**: Compute D_s from the Peotta-Torma quantum metric (Fubini-Study) of the 8 BCS modes on CG(24). Compare with GGE D_s.

**Pre-registered gate**: QUANTUM-METRIC-64. PASS: D_s(PT)/D_s(GGE) in [0.95, 1.05].
**Output**: Script, data, Section W6-D of working paper

---

## Wave 7: Remaining Carry-Forward + Structure

### W7-A: SHELL-HESSIAN-64 — FRG Shell-by-Shell (S62 carry-forward)

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**: Shell-by-shell Hessian from FRG proxy (9 multiplet removals). Verify all 36 eigenvalues positive at every shell.

**Pre-registered gate**: SHELL-HESSIAN-64. PASS: all positive. FAIL: any crosses zero.
**Output**: Script, data, Section W7-A of working paper

---

### W7-B: JACOBSON-KASPAROV-64 — 10D Jacobson Derivation

**Agent**: `van-den-dungen-bridge-theorist`
**Model**: opus
**Cost**: LOW (analytical)

**Prompt**: Apply the Jacobson thermodynamic derivation to the full 10D (M^4 x SU(3)) product manifold. Determine if fiber curvature R_K constrains Lambda_eff.

**Pre-registered gate**: JACOBSON-KASPAROV-64. PASS: reduces CC gap > 10 OOM. FAIL: fiber decouples.
**Output**: Analysis, Section W7-B of working paper

---

### W7-C: GGE-KMS-64 — Generalized KMS Formulation

**Agent**: `connes-ncg-theorist`
**Model**: opus
**Cost**: LOW (analytical)

**Prompt**: Formulate the generalized KMS condition for the GGE state on the BdG spectral triple. Determine compatibility with Tomita-Takesaki modular theory.

**Pre-registered gate**: GGE-KMS-64. INFO: multiple-temperature KMS structure analysis.
**Output**: Analysis, Section W7-C of working paper

---

### W7-D: TENSOR-SCALAR-64 — r-Ratio Resolution (S62 carry-forward)

**Agent**: `kaluza-klein-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**: Decompose a_4 into scalar, vector, and R² contributions. Extract Starobinsky weight. Compute multi-field sin²(alpha) from 36D Hessian trajectory.

**Pre-registered gate**: TENSOR-SCALAR-64. PASS: r < 0.036 after R² + multi-field. FAIL: r > 0.1.
**Output**: Script, data, Section W7-D of working paper

### W7-E: SKYRMION-BARYON-64 — Skyrmion Physics on SU(3) Fiber

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Investigate skyrmion physics on the Jensen-deformed SU(3) fiber as a candidate baryogenesis mechanism. The framework has pi_3(SU(3)) = Z, giving integer-winding topological solitons on the fiber. These are the substrate's skyrmions. If the transit (first-order phase transition at the fold) produces topological defects via Kibble-Zurek, skyrmion production could be the missing baryogenesis mechanism (leptogenesis CLOSED in S60).

**Context**: S18-S19 identified pi_3(SU(3)) = Z → skyrmions as transit defects but never computed masses, sizes, or production rates. The baryogenesis mechanism is an explicit open question (framework-cc-oom.md, wrapup). Paper 27 in Phonon-First library (Manton & Sutcliffe 2004, Topological Solitons) provides the mathematical framework.

**Method**:
1. Compute the skyrmion mass on round SU(3): M_skyrm = (12 pi^2 / e^2) f_pi where f_pi and e are determined by the spectral action's a_4 coefficient. For the Skyrme model on a compact group manifold G, the static energy is E = integral [-(f_pi^2/16) Tr(L_mu L^mu) + (1/(32 e^2)) Tr([L_mu, L_nu]^2)] sqrt(g) d^8x where L_mu = U^{-1} d_mu U is the left-invariant current.
2. Map the Skyrme parameters to spectral action coefficients: f_pi^2 ~ a_2 (gravitational stiffness), 1/e^2 ~ a_4 (Yang-Mills stiffness).
3. Compute the skyrmion size R_skyrm on Jensen-deformed SU(3) at the fold (tau=0.190). The Jensen deformation breaks SO(8) → U(1) x SU(2) x SU(3), which modifies the skyrmion profile.
4. Estimate the baryon number: B = (1/2 pi^2) integral Tr(L wedge L wedge L) = winding number in pi_3(SU(3)).
5. Estimate Kibble-Zurek defect production: n_skyrm ~ (xi_0 / xi_freeze)^d where xi_0 is the correlation length at the fold, xi_freeze is the freeze-out length, and d is the effective dimension. Use the transit time t_transit and the relaxation time tau_relax from W1-E data.
6. Compare: does n_skyrm * M_skyrm give the observed baryon-to-photon ratio eta_B ~ 6e-10?

**Pre-registered gate**: SKYRMION-BARYON-64
- PASS: M_skyrm is within 2 OOM of the proton mass (0.938 GeV) AND n_skyrm gives eta_B within 3 OOM of 6e-10
- FAIL: M_skyrm is more than 5 OOM from proton mass OR n_skyrm gives eta_B more than 10 OOM off
- INFO: M_skyrm and n_skyrm reported, structural viability assessed

**Input**: a_2, a_4 from spectral action at fold, D_K eigenvalues, transit dynamics from W1-E, canonical_constants.py
**Output**:
1. Script: `computations/s64_skyrmion_baryon.py`
2. Data: `computations/s64_skyrmion_baryon.npz`
3. Results: Section W7-E of working paper

---

## Wave 8: Workshops + Synthesis

### W8-A: Volovik x Landau Workshop — Transit-as-Relaxation Deep Dive

**Agents**: volovik, landau
**Type**: /rclab-review --type workshop --rounds 2
**Trigger**: Only if W1-A PASS or INFO

**Topic**: The asymptotic profile of S(tau) and its connection to Volovik's rho_vac ~ omega^2/t^2 relaxation. Does the spectral action dynamics reproduce the superfluid vacuum relaxation? What sets the exponent?

### W8-B: Session 64 Synthesis

**Agent**: gen-physicist (solo)
**Type**: /rclab-review --agents gen-physicist

Read the complete working paper and produce the session synthesis.

---

## IV. Constraint Gates Summary

| ID | Wave | Type | PASS | FAIL |
|:---|:-----|:-----|:-----|:-----|
| S-ASYMPTOTIC-64 | W1-A | CRITICAL | a_2 monotone decreasing, power-law | a_2 asymptotes nonzero |
| R-G-CHARGE-DECOMPOSITION-64 | W1-B | HIGH | rho_ZP-overlapping charge broken | Zero overlap |
| SA-VERSUS-JACOBSON-64 | W1-C | HIGH | Lambda_SA ≠ Lambda_J | Same quantity |
| OCC-SPEC-64 | W1-D | HIGH | S_occ < 100 → A_s gap < 5 OOM | S_occ ~ S_fold |
| BCS-DRESSED-SA-64 | W2-A | MEDIUM | eps_H shift > 1% | No detectable shift |
| SELF-CONSISTENT-NE-64 | W2-B | HIGH | N_e value reported | — |
| SECTOR-SELECTIVE-BREAKING-64 | W2-C | HIGH | delta_Lambda > 10^{-6} | Below threshold |
| N-PAIR-3-RG-64 | W2-D | HIGH | <r> > 0.45 (Wigner-Dyson) | <r> < 0.40 (Poisson) |
| FINITE-SIZE-VACUUM-ENERGY-64 | W2-E | LOW | E(0) consistency | — |
| TENSOR-BURST-64 | W3-A | HIGH | r_CMB < 0.036 | r_CMB > 0.1 |
| BDG-KASPAROV-64 | W3-B | HIGH | a_2^BdG matches Sakharov ±10% | Disagrees |
| LINEWIDTH-HIERARCHY-64 | W3-C | MEDIUM | Gamma_B3 > B1 > B2 | Different order |
| TRANSFER-BOGOLIUBOV-64 | W3-D | MEDIUM | Cutoff-insensitive | Cutoff-sensitive |
| SOUND-SPEED-64 | W3-E | HIGH | c_s < 1 | c_s > 1 |
| MUKHANOV-SASAKI-64 | W4-A | HIGH | n_s in [0.93, 0.99] | Outside [0.85, 1.00] |
| KK-THRESHOLD-64 | W4-B | HIGH | Converges at L=6 | Diverges |
| PHASE-BOGOLIUBOV-64 | W4-C | MEDIUM | Peak phases reported | — |
| DESI-DV-64 | W4-D | MEDIUM | w_a prediction | — |
| POST-TRANSIT-THERMO-64 | W5-A | MEDIUM | S_gen monotone | Decrease found |
| SPECTRAL-MONO-LINK-64 | W5-B | MEDIUM | CC ↔ area linked | Decouple |
| LOCAL-ENTANGLE-64 | W5-C | HIGH | S_ent value | — |
| JACOBSON-GGE-64 | W5-D | MEDIUM | Derivation extends | — |
| NS-FINAL-64 | W6-A | HIGH | n_s in [0.955, 0.975] | Outside |
| CHIRALITY-SELECTION-64 | W6-B | MEDIUM | Cancellation factor | — |
| VAB-RANK-64 | W6-C | MEDIUM | rank >= 3 | rank < 3 |
| QUANTUM-METRIC-64 | W6-D | MEDIUM | D_s ratio ∈ [0.95, 1.05] | Outside |
| SHELL-HESSIAN-64 | W7-A | MEDIUM | All 36 positive | Any crosses zero |
| JACOBSON-KASPAROV-64 | W7-B | MEDIUM | Reduces gap > 10 OOM | Decouples |
| GGE-KMS-64 | W7-C | LOW | KMS structure | — |
| TENSOR-SCALAR-64 | W7-D | HIGH | r < 0.036 | r > 0.1 |

## VI. Execution Notes

- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Output directory: `computations/`
- Script prefix: `s64_`
- Each agent writes results ONLY to their designated section in the working paper
- No TeamCreate — all agents are independent Agent tool calls
- ALL physics agents use opus model
- Import constants from `canonical_constants.py` (mandatory for S34+ scripts)
- Substrate-first framing in all agent prompts (see phononic-framing.md "IS Space, Not IN Space")
