# S45 Formula Audit Report

**Agent**: gen-physicist
**Date**: 2026-03-15
**Gate**: FORMULA-AUDIT-REPORT (META -- process quality)
**Context**: S44 had 3 formula errors (Sakharov normalization, Stieltjes ordering, Vol(SU(3))), all sharing the same signature: correct arithmetic, wrong formula provenance. S45 introduced mandatory audit protocol: (a) formula stated with units, (b) dimensional check, (c) limiting case, (d) citation. This report evaluates compliance across all completed S45 computations.

---

## Audit Criteria

For each completed computation, four items are checked:

| Criterion | Description | Mark |
|:----------|:-----------|:-----|
| **(a) Formula with units** | Central formula explicitly stated with dimensions of every quantity | PASS / PARTIAL / FAIL |
| **(b) Dimensional check** | All equations verified for dimensional consistency | PASS / PARTIAL / FAIL |
| **(c) Limiting case** | At least one limiting case verified against known result | PASS / PARTIAL / FAIL |
| **(d) Citation** | Original derivation cited (paper, textbook, or prior session) | PASS / PARTIAL / FAIL |

---

## Computation-by-Computation Audit

### 1. W1-2: KZ-NS-45 (Bogoliubov Spectrum for n_s)
**Agent**: volovik-superfluid-universe-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | |beta_k|^2 = ((E_in - E_out)/(2 sqrt(E_in E_out)))^2. [E] = M_KK stated. Ratio dimensionless. |
| (b) Dimensional | **PASS** | Numerator [M_KK^2], denominator [M_KK^2]. Verified explicitly. |
| (c) Limiting case | **PASS** | |beta|^2 = 0 when E_in = E_out (no quench). Verified to machine epsilon. |
| (d) Citation | **PASS** | Parker (1968) Phys. Rev. 183, 1057; Birrell-Davies (1982) Ch. 3; S38 W4. |

**Violations**: None.

---

### 2. W1-2x: Einstein Cross-Check of KZ-NS-45
**Agent**: einstein-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | |beta_k|^2 = (E_in - E_out)^2 / (4 E_in E_out). E_k = sqrt(lambda_k^2 + Delta^2) [M_KK]. |
| (b) Dimensional | **PASS** | Numerator [M_KK^2], denominator [M_KK^2]. Verified. |
| (c) Limiting case | **PASS** | No quench: |beta|^2 = 0 exactly (synthetic test). Maximum mixing: |beta|^2 -> E_out/(4 E_in). Both verified. |
| (d) Citation | **PASS** | Parker (1969); Birrell-Davies (1982) Ch. 3; Bogoliubov (1958) Nuovo Cim. 7, 794. |

**Violations**: None. **Note**: Parker date discrepancy (1968 in primary vs 1969 in cross-check). The paper was published in 1969 (Phys. Rev. 183, 1057, received 1968). Not a formula error but a bibliographic inconsistency.

---

### 3. W1-R1: Q-THEORY-KK-45 (q-Theory Self-Tuning)
**Agent**: volovik-superfluid-universe-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PARTIAL** | TL = (1/2) sum_k ln(lambda_k^2/mu^2) stated. The Gibbs-Duhem construction rho_gs = epsilon - tau * d(epsilon)/d(tau) is described verbally in the method section, but the exact formula for epsilon(tau) in terms of TL is not explicitly written with units in a single self-contained equation. |
| (b) Dimensional | **PASS** | TL is dimensionless (argument of ln is dimensionless). rho_gs in M_KK^4 stated. |
| (c) Limiting case | **PASS** | mu_ref independence verified (cancels exactly). S43 baseline reproduced to 0.0%. Epsilon convexity verified. |
| (d) Citation | **PASS** | Volovik Papers 05, 15-16 (q-theory). S43 QFIELD-43 reproduced. |

**Violations**: **(a) PARTIAL** -- The Gibbs-Duhem construction is described procedurally (steps 1-7 in Method) but the central equation relating rho_gs to TL is distributed across steps rather than stated as a single formula with units. The key relation rho_gs(tau) = [epsilon(tau) - epsilon(0)] - tau * d_epsilon/dtau appears in the Physical Interpretation but not in the Formula Audit subsection.

---

### 4. W1-R2: OCC-SPEC-45-LANDAU (Landau Free Energy)
**Agent**: landau-condensed-matter-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | F_BCS = sum d_k [E_k - |xi_k|] - Delta^2/g. E_k = sqrt(xi_k^2 + Delta^2), xi_k = |lambda_k|, mu=0. Units: [M_KK]. |
| (b) Dimensional | **PASS** | [Delta] = [lambda] = M_KK. [d_k] = 1. [g] = M_KK (from gap eq). [F_BCS] = M_KK. Explicit. |
| (c) Limiting case | **PASS** | Delta=0 gives F_BCS=0 (normal state). Constant-DOS limit gives -N_0 Delta^2/2 (textbook BCS). Self-consistency identity verified to 1e-12. |
| (d) Citation | **PASS** | BCS (1957) Paper 15; Tinkham Ch. 3; S34 (PH forces mu=0); S36 (ED-CONV-36 E_cond). |

**Violations**: None. Exemplary formula audit.

---

### 5. W2-R1: ALPHA-EFF-45 (Non-Equilibrium Specific Heat for DM/DE)
**Agent**: volovik-superfluid-universe-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PARTIAL** | Method 7c formula alpha = S_GGE / (S_max - S_GGE) stated clearly with S_GGE and S_max in nats (dimensionless). However, 10 other methods are described with varying levels of formula explicitness. Methods 2a-2c and Method 3 have formulas that are described qualitatively ("use negative eigenvalues to suppress") rather than written as equations. |
| (b) Dimensional | **PASS** | All quantities in M_KK units for energies, dimensionless for ratios. S_GGE in nats. alpha_eff dimensionless. Stated limiting case S = S_max => alpha -> infinity. |
| (c) Limiting case | **PASS** | S = S_max gives alpha -> infinity (thermal equilibrium, no vacuum energy from non-thermality). Method 1a reproduces S44 (alpha = 1.060) exactly. |
| (d) Citation | **PARTIAL** | Zubarev (non-equilibrium thermodynamic potential) referenced by name but no specific paper/equation number. Volovik Paper 05 cited for equilibrium theorem. The Zubarev formalism citation should include: D.N. Zubarev, "Nonequilibrium Statistical Thermodynamics" (1974), or the specific equation from which alpha = S/(S_max - S) is derived. |

**Violations**: **(a) PARTIAL** -- 11 methods tested but formulas for Methods 2a-2c and Method 3 are descriptive rather than explicit. **(d) PARTIAL** -- Zubarev formalism cited by author name only, no specific publication or equation number. This is the S44-pattern signature: the formula provenance is incomplete. Given that the Zubarev method is the ONLY one reaching the PASS window, its derivation source must be pinned precisely.

---

### 6. W2-R2: UNEXPANDED-SA-45 (Full Spectral Action for CC)
**Agent**: connes-ncg-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | S(Lambda) = sum_k d_k f(lambda_k^2/Lambda^2). Taylor: S = sum_n [f^(n)(0)/n!] (-1)^n A_{2n}/Lambda^{2n}. A_{2n} = sum_k d_k (lambda_k^2)^n. All stated. |
| (b) Dimensional | **PASS** | [lambda_k] = [Lambda] = M_KK. A_{2n} dimensionless. S dimensionless. |
| (c) Limiting case | **PASS** | 20-term Taylor vs exact at Lambda=5: relative error 1.56e-16 (machine epsilon). Convergence: absolute for Lambda^2 > max(lambda_k^2). |
| (d) Citation | **PASS** | Connes-Chamseddine spectral action. Gilkey (1975). The structural theorem (Taylor exactness for finite spectra) is stated and proved in the results section. |

**Violations**: None. Clean structural theorem with full formula presentation.

---

### 7. W2-R3: ANALYTIC-TORSION-45 (Ray-Singer Torsion)
**Agent**: spectral-geometer

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | T = exp(-(1/2) zeta'(0)). zeta(s) = sum_k d_k |lambda_k|^{-2s}. zeta(0) = sum d_k. zeta'(0) = -2 sum d_k ln|lambda_k|. All stated in script header and results. |
| (b) Dimensional | **PASS** | zeta(0) dimensionless (count). zeta'(0) dimensionless (sum of logs). T dimensionless (exponential of dimensionless). rho_torsion = (M_KK^4 / 32 pi^2) |zeta'(0)| in [GeV^4]. |
| (c) Limiting case | **PARTIAL** | zeta'(0) verified via numerical differentiation at eps = 10^{-6} (agreement to 5 parts in 10^5). However, no KNOWN RESULT limiting case is cited. E.g., for S^1 with N modes, the analytic torsion is exactly computable and could serve as a cross-check. The numerical differentiation is a self-consistency check, not a verification against an independent known result. |
| (d) Citation | **PASS** | Ray-Singer (1971); Cheeger (1979); Fried (1986); Gilkey textbook. All in script header. |

**Violations**: **(c) PARTIAL** -- The limiting case is a self-consistency check (numerical vs analytic derivative of zeta) rather than a verification against an independently known torsion value. A proper limiting case would be: compute T for round SU(3) (tau=0) and compare against known results for homogeneous spaces, or compute T for S^1 (trivially known) to validate the code path.

---

### 8. W2-R4: KZ-NS-KMAP-45 (EIH k-Mapping)
**Agent**: einstein-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | k = |lambda_k(tau_fold)| [M_KK]. g = 1/d_{(p,q)} (Schur orthogonality). P(k) = sum (1/d) |beta_k|^2 [EQ.3]. k_phys in Mpc^{-1} via hbar*c conversion. |
| (b) Dimensional | **PASS** | [lambda] = dimensionless. [M_KK] = GeV. k = GeV -> Mpc^{-1} via hbar*c. Verified. |
| (c) Limiting case | **PARTIAL** | The working paper states: "singlet (0,0) has lambda = 0.866 at tau=0, lambda = 0.82-0.97 at fold. NOT k=0." The text then corrects itself: k=0 is the zero mode of the 4D Laplacian, a different object. This is an important physical distinction but it means the stated limiting case (singlet -> k=0 homogeneous) was WRONG and then self-corrected. No clean pass of a pre-stated limiting case. |
| (d) Citation | **PASS** | Baptista Paper 14 (KK spinor reduction), S22b (block-diagonal theorem), S44 W2-3 (EIH singlet projection). |

**Violations**: **(c) PARTIAL** -- The limiting case for singlet (0,0) was initially stated as "k=0 (homogeneous)" but then corrected in-text because the singlet has nonzero eigenvalue. The corrected statement is physically right, but this is a failed limiting case that was caught and corrected in the report. A clean limiting case (e.g., for free particles Delta=0 the result reduces to W1-2 values) would strengthen this.

---

### 9. W2-R5: Q-THEORY-BCS-45 (BCS-Corrected q-Theory)
**Agent**: volovik-superfluid-universe-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | TL_BCS = (1/2) sum_k ln((lambda_k^2 + Delta_k^2)/mu^2), dimensionless. Stated. |
| (b) Dimensional | **PASS** | Argument of ln is dimensionless (eigenvalues and Delta in M_KK, mu in M_KK). |
| (c) Limiting case | **PASS** | Delta -> 0 recovers vacuum result (W1-R1, diff < 1e-15). Delta -> infinity gives TL -> (N/2) ln(Delta^2/mu^2), always positive. mu_ref cancels. Condensation energy contribution 3e-6 of TL (negligible). All verified. |
| (d) Citation | **PASS** | Volovik Papers 05, 15-16. FLATBAND-43 for gap hierarchy. S36 ED-CONV-36 for E_cond. |

**Violations**: None. Six explicit limiting cases checked.

---

### 10. W3-R1: SIGMA-SELECT-45 (Scale Selection for n_s)
**Agent**: connes-ncg-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | K(sigma) = Tr exp(-sigma D_K^2) = sum_k mult_k exp(-sigma lambda_k^2). d_s = -2 sigma d(ln K)/d(sigma). n_s - 1 = -d(d_s)/d(tau). All in script header [Eqs. (a)-(d)]. |
| (b) Dimensional | **PASS** | [sigma] = M_KK^{-2}. [lambda_k^2] = M_KK^2 (so sigma * lambda_k^2 is dimensionless). d_s dimensionless. n_s dimensionless. |
| (c) Limiting case | **PASS** | sigma -> 0: d_s -> 0 (finite truncation, stated as ~9280 modes) vs d_s -> dim(M) = 8 (continuum). sigma -> infinity: d_s -> 0 (compact space). Both stated and verified. |
| (d) Citation | **PASS** | Connes Paper 28 (spectral truncations). S44 W2-2 (DIMFLOW-44). CDT formula referenced. |

**Violations**: None.

---

### 11. W3-R2: MKK-TENSION-45 (M_KK Tension Resolution)
**Agent**: baptista-spacetime-analyst

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | Script header references Baptista Paper 13 eq. (5.21), Paper 14 eqs. (2.85), (2.88), (2.92)/(2.93). Kerner (1968) formula. Vol(SU(3)) from Macdonald formula. |
| (b) Dimensional | **PASS** | M_KK in [GeV]. Vol(SU(3)) dimensionless (Haar measure, cross-checked against analytic Macdonald). |
| (c) Limiting case | **PARTIAL** | The working paper section for this computation is sparse ("Results written by agent -- see above" with no explicit audit subsection visible). The script header lists the computation steps but the working paper does not contain a dedicated formula audit block. Relying on the script's internal checks. |
| (d) Citation | **PASS** | Baptista Papers 13, 14. Kerner (1968). canonical_constants.py. |

**Violations**: **(c) PARTIAL** -- No explicit limiting case stated in the working paper results section. The script header describes the steps but the results section (`W3-R2`) is a stub ("Results written by agent -- see above") with no formula audit subsection. The audit must be inferred from the script.

---

### 12. W3-R3: TRUNCATED-TORSION-45 (Singlet Torsion)
**Agent**: spectral-geometer

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | Same torsion formula as W2-R3 restricted to 16 singlet modes. T_singlet = exp(-(1/2) zeta'_singlet(0)). |
| (b) Dimensional | **PASS** | Same dimensional structure as W2-R3. |
| (c) Limiting case | **PARTIAL** | Inherited from W2-R3. Same deficiency: no independent known-result comparison. |
| (d) Citation | **PASS** | Same references as W2-R3. |

**Violations**: **(c) PARTIAL** -- Same issue as W2-R3.

---

### 13. W3-R4: DOS-FINE-SCAN-45 (Van Hove Fine Scan)
**Agent**: quantum-acoustics-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | DOS N(E) = sum_k d_k delta(E - |lambda_k|), Gaussian-broadened. Stated in script header line 19. |
| (b) Dimensional | **PASS** | [N(E)] = M_KK^{-1}. [E] = M_KK. |
| (c) Limiting case | **PASS** | tau=0: 9 VH points (round SU(3) symmetry). tau>0: 12 VH points (Jensen lifts degeneracies). Stated in script header. |
| (d) Citation | **PASS** | Van Hove (1953). S44 W5-3 (DOS-TAU-44). S44 W6 (VAN-HOVE-TRACK-44). |

**Violations**: None.

---

### 14. W3-R5: CC-HIERARCHY-CUBED-45
**Agent**: gen-physicist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | S = f_0 Lambda^4 A_0 + f_2 Lambda^2 A_2 + f_4 A_4 + ... A_{2n} = sum_k d_k (lambda_k/M_KK)^{2n}. Stated in script header. |
| (b) Dimensional | **PASS** | A_{2n} dimensionless (ratios of eigenvalues). Lambda in [M_KK]. S dimensionless. |
| (c) Limiting case | **PASS** | A_0 = 6440 (mode count, matches a_0). Moment ratios A_0/A_2 and A_2/A_4 computed and shown to be O(1), disproving the 10^{36} hypothesis. |
| (d) Citation | **PASS** | Connes-Chamseddine spectral action. Gilkey (1975). canonical_constants.py. |

**Violations**: None.

---

### 15. W4-R1: RUNNING-GN-45 (Running G_N)
**Agent**: volovik-superfluid-universe-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | Formula B: 1/(16 pi G_Sak) = (1/(48 pi^2)) sum_k d_k [Lambda^2 - m_k^2 ln(1 + Lambda^2/m_k^2)]. Formula Q: 1/(16 pi G_quad) = M_KK^2/(48 pi^2) sum_k d_k lambda_k^2. Both stated in script header. |
| (b) Dimensional | **PASS** | [m_k] = [Lambda] = GeV. 1/(16 pi G) in [GeV^2]. |
| (c) Limiting case | **PARTIAL** | Working paper reports G_N varies 2.5% over [0, 0.50] and ratio to observed = 0.436. No explicit limiting case such as "round SU(3) recovers known sum" or "Lambda -> infinity gives Formula Q." The near-constancy is a physical result, not a limiting case verification. |
| (d) Citation | **PASS** | Sakharov (1968). Volovik superfluid 3He analog described. S44 W1-1. |

**Violations**: **(c) PARTIAL** -- No clean limiting case stated. "Formula Q is the Lambda -> infinity limit of Formula B" is implicit in the structure but not explicitly verified.

---

### 16. W4-R2: EULER-DEFICIT-45 (Euler Deficit Identity)
**Agent**: volovik-superfluid-universe-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | sum_k T_k S_k^{Shannon} = N_pair = 1 EXACTLY. T_k = -1/ln(f_k). S_k = -f_k ln(f_k). Analytic proof in script header (lines 26-42). |
| (b) Dimensional | **PASS** | T_k in M_KK (energy). S_k in nats (dimensionless). Product T_k S_k in M_KK. Sum = N_pair (dimensionless) only if energies are normalized. Checked: E_k = 2 xi_k, f_k = n_k, sum f_k = 1. |
| (c) Limiting case | **PASS** | Single-mode (f_1 = 1): T_1 S_1 = 0 * infinity (handled via L'Hopital, correctly gives 1). Uniform f_k = 1/8: sum T_k S_k = sum (1/ln(8)) * (ln(8)/8) = 1 exactly. |
| (d) Citation | **PASS** | S44 W6-5 claim being tested. Shannon entropy vs Fermi-Dirac entropy distinction cited. |

**Violations**: None.

---

### 17. W4-R3: GL-GGE-STABILITY-45 (GL Free Energy Landscape)
**Agent**: landau-condensed-matter-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | F({T_k}) = sum_k [rho_k - T_k S_k]. H_ij = d^2F/dT_i dT_j = -dS_i/dT_j. H_ij = C_ij / T_i. All three equations stated in script header with derivation chain. |
| (b) Dimensional | **PASS** | [F] = M_KK. [T_k] = M_KK. [S_k] = dimensionless. [H_ij] = M_KK^{-1}. [C_ij] = dimensionless. |
| (c) Limiting case | **PARTIAL** | Morse index 3 stated. Hessian eigenvalue decomposition performed. No comparison against an analytically solvable limit (e.g., 2-mode system with known Morse index). |
| (d) Citation | **PASS** | S44 W6-5 (C_kl matrix). Morse theory. |

**Violations**: **(c) PARTIAL** -- No explicit limiting case. The Morse index is computed numerically but not checked against a reduced system where the answer is known analytically.

---

### 18. W4-R4: TWO-FLUID-DESI-45 (Two-Fluid Cosmology)
**Agent**: volovik-superfluid-universe-theorist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | w_eff = P_total/rho_total. P_total = P_DM + P_DE = 0 + (-rho_DE). rho_DE = -rho_DM/alpha. Tracking vs non-tracking clearly distinguished. Script explicitly identifies the tracking formula as WRONG and derives the correct two-fluid Friedmann version. |
| (b) Dimensional | **PASS** | All energy densities in GeV^4. w dimensionless. Omega dimensionless. |
| (c) Limiting case | **PASS** | alpha = 1: rho_total = 0 (degenerate, stated). alpha = 2: w_eff = 1 (stiff). alpha = 3: w_eff = 1/2. The script correctly identifies these as the tracking (wrong) limits and proceeds to the Friedmann evolution. |
| (d) Citation | **PASS** | Volovik Papers 05, 35, 37. DESI DR1 CPL parameterization with error bars. |

**Violations**: None.

---

### 19. W4-R6: ACOUSTIC-NS-45 (Acoustic Dispersion n_s)
**Agent**: tesla-resonance

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | Five methods explicitly stated. Method 1: n_s - 1 = -2 alpha (k_pivot/k_max)^2. Method 2: n_s = 1 - 2 d(ln v_g)/d(ln k). Method 5: omega^2 = omega_0^2 + A k^2 + B k^4. All with units. |
| (b) Dimensional | **PASS** | omega in [M_KK]. k = sqrt(C_2) dimensionless in M_KK units. k_pivot in [Mpc^{-1}], k_max in [M_KK], conversion stated. |
| (c) Limiting case | **PASS** | k_pivot/k_max ~ 10^{-57} gives n_s = 1 exactly (Method 1). This IS a known result: zero curvature at zero k gives Harrison-Zel'dovich. |
| (d) Citation | **PASS** | Standard condensed matter dispersion theory. S44 W5-3, W6-8 for prior spectral data. |

**Violations**: None.

---

### 20. W4-R7: HEAT-KERNEL-AUDIT-45 (Heat Kernel Validity)
**Agent**: spectral-geometer

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a)-(d) | **N/A** | This is a meta-audit, not a computation producing new numbers. It classifies prior results as VALID, ARTIFACT, or APPROXIMATE. The heat kernel formula K(sigma) = sum_k d_k exp(-sigma lambda_k^2) is the starting point, not a new derivation. Audit criteria do not apply to meta-analyses. |

**Violations**: N/A.

---

### 21. W5-R2: CC-GAP-UPDATE-45 (CC Balance Sheet)
**Agent**: gen-physicist

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a)-(d) | **N/A** | This is a consolidation/reconciliation of prior results, not a new computation. All input numbers are cited from their source computations. No new formulas introduced. Audit criteria apply to the source computations, not the aggregation. |

**Violations**: N/A.

---

### 22. W5-R4: COLLECTIVE-NS-45 (Collective Phonon Pair Creation for n_s)
**Agent**: team-lead (s45_collective_ns_v2.py)

| Criterion | Status | Detail |
|:----------|:-------|:-------|
| (a) Formula | **PASS** | |beta_k|^2 = ((E_dressed - E_undressed) / (2 sqrt(E_dressed E_undressed)))^2. E_dressed = sqrt(lambda_k^2 + Delta^2). E_undressed = |lambda_k|. Stated in script. |
| (b) Dimensional | **PASS** | Same structure as W1-2. All energies in M_KK. |
| (c) Limiting case | **PASS** | Delta = 0: |beta|^2 = 0 (no condensate, no pairs). Verified in script line 66-67 (cross-check, max |beta|^2 should be 0). |
| (d) Citation | **PARTIAL** | The script references S38 for Delta_0 and prior computations but does not cite the original source for the collective mode pair creation framework. The key physics claim -- that COLLECTIVE modes differ from single-particle modes -- is stated but the derivation source is not cited. In practice, the computation uses the same single-particle Bogoliubov formula as W1-2, applied at fixed tau rather than across the transit. This is NOT a collective mode computation despite the name. |

**Violations**: **(d) PARTIAL** -- The computation name suggests "collective phonon pair creation" but the actual formula is the same single-particle Bogoliubov coefficient from Parker (1968). The distinction between single-particle and collective modes claimed in the task description (Anderson-Bogoliubov phonons vs BdG quasiparticles) is not implemented in the code. The script computes condensate-destruction pair creation at fixed tau, which is a valid calculation, but the citation should acknowledge that this is NOT the collective-mode computation described in the prompt.

---

## Summary Table

| # | Computation | (a) Formula | (b) Dimensional | (c) Limiting | (d) Citation | Overall |
|:--|:-----------|:------------|:----------------|:-------------|:-------------|:--------|
| 1 | KZ-NS-45 | PASS | PASS | PASS | PASS | CLEAN |
| 2 | Einstein cross-check | PASS | PASS | PASS | PASS | CLEAN |
| 3 | Q-THEORY-KK-45 | PARTIAL | PASS | PASS | PASS | 1 violation |
| 4 | OCC-SPEC-45-LANDAU | PASS | PASS | PASS | PASS | CLEAN |
| 5 | ALPHA-EFF-45 | PARTIAL | PASS | PASS | PARTIAL | 2 violations |
| 6 | UNEXPANDED-SA-45 | PASS | PASS | PASS | PASS | CLEAN |
| 7 | ANALYTIC-TORSION-45 | PASS | PASS | PARTIAL | PASS | 1 violation |
| 8 | KZ-NS-KMAP-45 | PASS | PASS | PARTIAL | PASS | 1 violation |
| 9 | Q-THEORY-BCS-45 | PASS | PASS | PASS | PASS | CLEAN |
| 10 | SIGMA-SELECT-45 | PASS | PASS | PASS | PASS | CLEAN |
| 11 | MKK-TENSION-45 | PASS | PASS | PARTIAL | PASS | 1 violation |
| 12 | TRUNCATED-TORSION-45 | PASS | PASS | PARTIAL | PASS | 1 violation |
| 13 | DOS-FINE-SCAN-45 | PASS | PASS | PASS | PASS | CLEAN |
| 14 | CC-HIERARCHY-CUBED-45 | PASS | PASS | PASS | PASS | CLEAN |
| 15 | RUNNING-GN-45 | PASS | PASS | PARTIAL | PASS | 1 violation |
| 16 | EULER-DEFICIT-45 | PASS | PASS | PASS | PASS | CLEAN |
| 17 | GL-GGE-STABILITY-45 | PASS | PASS | PARTIAL | PASS | 1 violation |
| 18 | TWO-FLUID-DESI-45 | PASS | PASS | PASS | PASS | CLEAN |
| 19 | ACOUSTIC-NS-45 | PASS | PASS | PASS | PASS | CLEAN |
| 20 | HEAT-KERNEL-AUDIT-45 | N/A | N/A | N/A | N/A | META |
| 21 | CC-GAP-UPDATE-45 | N/A | N/A | N/A | N/A | META |
| 22 | COLLECTIVE-NS-45 | PASS | PASS | PASS | PARTIAL | 1 violation |

---

## Aggregate Statistics

- **Computations audited**: 19 (excluding 2 meta-analyses and 1 N/A meta-audit)
- **Fully CLEAN**: 11 / 19 = **57.9%**
- **With at least one violation**: 8 / 19 = **42.1%**
- **By criterion**:
  - (a) Formula stated: 17 PASS, 2 PARTIAL, 0 FAIL
  - (b) Dimensional check: 19 PASS, 0 PARTIAL, 0 FAIL
  - (c) Limiting case: 12 PASS, 7 PARTIAL, 0 FAIL
  - (d) Citation: 17 PASS, 2 PARTIAL, 0 FAIL

---

## Violation Classification

### CRITICAL violations (could affect gate verdicts): **0**
No formula errors were found that could change a PASS to FAIL or vice versa. All dimensional checks pass. All central formulas are correct.

### MODERATE violations (incomplete provenance, S44-pattern risk): **2**

1. **ALPHA-EFF-45 (d)**: Zubarev formalism cited by author name only, no publication or equation. This is the S44 signature (correct arithmetic, incomplete provenance). The Zubarev formula is the ONLY method reaching the PASS window; its derivation chain must be pinned. **Recommendation**: Cite Zubarev, "Nonequilibrium Statistical Thermodynamics" (Consultants Bureau, 1974), and trace the specific formula alpha = S/(S_max - S) to its equation number, or explicitly state if this is a NEW derivation original to this framework.

2. **COLLECTIVE-NS-45 (d)**: Computation named "collective phonon pair creation" but uses single-particle Bogoliubov formula. The physics distinction (Anderson-Bogoliubov vs BdG) is not implemented. **Recommendation**: Either rename the computation to reflect what it actually computes (condensate-destruction pair creation at fixed tau), or implement the collective mode RPA/GRPA computation described in the prompt.

### MINOR violations (limiting cases incomplete but non-critical): **6**

3. **Q-THEORY-KK-45 (a)**: Gibbs-Duhem formula distributed across method steps rather than stated compactly.
4. **ANALYTIC-TORSION-45 (c)**: Numerical self-consistency used instead of comparison to known torsion.
5. **KZ-NS-KMAP-45 (c)**: Limiting case (singlet -> k=0) stated incorrectly then self-corrected.
6. **MKK-TENSION-45 (c)**: Working paper results section is a stub; limiting case must be inferred from script.
7. **RUNNING-GN-45 (c)**: No explicit limiting case (e.g., Lambda -> infinity recovers quadratic formula).
8. **GL-GGE-STABILITY-45 (c)**: No analytically solvable limiting case for the Morse index.
9. **TRUNCATED-TORSION-45 (c)**: Inherits the ANALYTIC-TORSION-45 limiting case deficiency.

---

## Comparison to S44

S44 had **3 formula errors**: Sakharov normalization, Stieltjes ordering, Vol(SU(3)). All shared the signature: correct arithmetic, wrong formula provenance (incorrect equation transcribed from source).

S45 has **0 formula errors** (no incorrect formulas). The violations are all in the COMPLETENESS category: incomplete citations (2), incomplete limiting cases (7), and one naming mismatch. The mandatory audit protocol introduced at the start of S45 has eliminated the S44-type errors.

The most significant remaining risk is the ALPHA-EFF-45 Zubarev citation gap. If the formula alpha = S/(S_max - S) turns out to be a specific approximation within Zubarev's formalism (rather than the general result), the PASS-window agreement (alpha = 0.410 vs observed 0.388) could be an artifact of the approximation choice. Pinning the derivation source is necessary to assess this risk.

---

## Recommendations for S46

1. **Enforce**: Every formula audit section must contain the four items (a)-(d) as a formatted block, not distributed through the method section. S45 compliance was 57.9% fully clean; target 80%+ for S46.

2. **Pin Zubarev**: Before citing alpha = 0.410 as a framework prediction, trace the derivation to a specific equation in a published source or prove it from first principles within the framework.

3. **Rename COLLECTIVE-NS**: The computation does not implement collective modes. Either rename or implement.

4. **Torsion limiting case**: Compute T for a simple space (S^1, S^3, or flat torus) using the same code path to validate the zeta'(0) computation against a known analytic result.

5. **Stub sections**: W3-R2 (MKK-TENSION), W3-R3 (TRUNCATED-TORSION), W4-R1 (RUNNING-GN), and W4-R3 (GL-GGE) have incomplete working paper entries. Their scripts contain the calculations but the results sections are stubs. For the working paper to be self-contained, these need to be filled.
