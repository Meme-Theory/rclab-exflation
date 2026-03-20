# Session 35 Plan: N_eff Resolution and Parameter Pinning

**Date**: 2026-03-07
**Predecessor**: Session 34 (master synthesis: `sessions/session-34/session-34-master-synthesis.md`)
**Format**: Parallel single-agent computations, 4 waves
**Results file**: `sessions/session-35/session-35-results-workingpaper.md`

---

## I. Session Objective

Resolve the N_eff corridor question that Session 34 identified as the sole remaining existential gate for the BCS mechanism chain. Secondary objectives: pin the impedance, extract neutrino observables at corrected parameters, and test specificity.

**Pre-registered master gate**:
- **NEFF-35**: Does the physical system have N_eff > 5.5?
- **PASS**: N_eff > 5.5 (mechanism chain survives beyond-mean-field)
- **FAIL**: N_eff ≤ 5.5 (BCS link closed unless impedance > 1.0)
- **Null hypothesis**: N_eff = 4.0 ± 2.0 (random-phase cancellation of non-singlet contributions)

---

## II. Wave Structure

### Dependency Graph

```
Wave 1 (parallel, no dependencies):
  W1-A  W1-B  W1-C  W1-D    ← All independent, run simultaneously

Wave 2 (parallel, no dependencies on each other; W2-A/B/C can start with Wave 1):
  W2-A  W2-B  W2-C  W2-D    ← W2-C/D are medium-cost, others zero-cost

Wave 3 (depends on Wave 1 results for context):
  W3-A  W3-B  W3-C  W3-D  W3-E  ← W3-C (Sagan) MUST wait for Wave 1

Wave 4 (independent, can run anytime):
  W4-A  W4-B  W4-C            ← Lower priority, run if capacity allows
```

---

## III. Wave 1: N_eff Resolution (CRITICAL PATH)

All four computations attack the N_eff question from different angles. They run in parallel with no dependencies.

---

### W1-A: Multi-Band 3×3 Thouless Eigenvalue

**Agent**: `landau-condensed-matter-theorist`
**Model**: sonnet
**Cost**: LOW (3×3 matrix diagonalization from existing data)

**Prompt**:

You are the Landau condensed matter theorist. Your task is to resolve the N_eff question by computing the full multi-band Thouless matrix eigenvalue.

**Context**: Session 34 found M_max = 0.902 in the B2-only (5×5) Thouless matrix with step-function wall DOS. With smooth-wall van Hove DOS (rho = 14.02/mode), M_max = 1.445. The beyond-mean-field corridor requires N_eff > 5.5. The question is whether cross-channel couplings (B1-B2, B3-B2) push the effective pairing dimensionality above 5.5.

**Computation**:
1. Load the corrected spinor V matrix from `tier0-computation/s34a_dphys_kosmann.npz`:
   - V(B1,B1) = 0.000 (Trap 1, exact zero)
   - V(B1,B2) = 0.077 (at phi=gap)
   - V(B1,B3) = 0.000 (Trap 4)
   - V(B2,B2) = 0.086 (at phi=gap, off-diagonal max)
   - V(B2,B3) = 0.022 (at phi=gap)
   - V(B3,B3) = read from data
2. Load eigenvalues from `tier0-computation/s23a_kosmann_singlet.npz` at tau = 0.20 (dump point).
3. Compute the smooth-wall DOS for each branch (B1, B2, B3) using the van Hove integral with v_min = 0.012 for B2 (fold at v=0) and step-function for B1/B3 (no fold).
4. Construct the 3×3 Thouless matrix: M_{ij} = V(B_i, B_j) × rho_j / (2|xi_j|) where xi_j is the gap-edge distance.
5. Compute the largest eigenvalue of M. This IS N_eff-adjusted M_max.
6. Also construct the full 8×8 (all positive modes) Thouless matrix and compare.

**Pre-registered gate**: NEFF-THOULESS-35
- PASS: max eigenvalue > 1.0
- FAIL: max eigenvalue ≤ 1.0

**Output**: Script `tier0-computation/s35_thouless_multiband.py`, data `s35_thouless_multiband.npz`, plot `s35_thouless_multiband.png`. Write results to Section W1-A of `sessions/session-35/session-35-results-workingpaper.md`.

---

### W1-B: Exact Diagonalization at Corrected DOS

**Agent**: `quantum-acoustics-theorist`
**Model**: sonnet
**Cost**: ZERO (modify one parameter in existing script)

**Prompt**:

You are the Quantum Acoustics theorist. Your task is to rerun the beyond-mean-field exact diagonalization at the corrected smooth-wall DOS.

**Context**: Session 34's BMF-35a (`tier0-computation/s35a_beyond_mean_field.py`) ran ED at rho = 8.81 (step-function wall with old impedance). At this rho, M_max(MF) = 0.902, and the ED found zero condensation energy (vacuum ground state). The corrected smooth-wall rho = 14.02 gives M_max(MF) = 1.445 > 1.0. At this higher rho, the ED ground state MAY shift from vacuum to a paired state.

**Computation**:
1. Read `tier0-computation/s35a_beyond_mean_field.py` to understand the existing ED infrastructure (32-state Fock space, 5 modes, pair hopping Hamiltonian).
2. Modify the script to use rho = 14.02 (smooth-wall van Hove) instead of 8.81 (step with old impedance). Also test rho = 14.66 (smooth-wall with multi-sector factor 1.046).
3. Run ED at BOTH rho values. For each, report:
   - Ground state energy E_0
   - Condensation energy E_cond = E_0 - E_vacuum
   - Pair susceptibility chi_pp (exact) vs chi_pp (mean-field)
   - Suppression ratio chi_pp(ED) / chi_pp(MF)
   - Expansion parameter M^2 × L / N_eff
4. Use spinor V(B2,B2) = 0.057 (bare) or 0.086 (at phi=gap) — run both.

**Pre-registered gate**: ED-CORRECTED-35
- PASS: E_cond < 0 (paired ground state) at rho = 14.02
- FAIL: E_cond = 0 (vacuum ground state) at rho = 14.02

**Output**: Script `tier0-computation/s35_ed_corrected_dos.py`, data `s35_ed_corrected_dos.npz`, plot `s35_ed_corrected_dos.png`. Write results to Section W1-B of `sessions/session-35/session-35-results-workingpaper.md`.

---

### W1-C: 1D Wilson RG Flow for BCS Coupling

**Agent**: `feynman-theorist`
**Model**: sonnet
**Cost**: LOW (analytic + simple numerical integration)

**Prompt**:

You are the Feynman theorist. Your task is to determine whether the BCS coupling flows to strong coupling within the B2 bandwidth, which would make the N_eff question moot.

**Context**: The BCS 4-fermion interaction in the 1D domain wall is marginal. The one-loop beta function for an attractive BCS coupling in 1D is beta(g) = -g^2 + O(g^3). If g flows to O(1) within the B2 bandwidth, BCS instability is GUARANTEED regardless of N_eff.

**Computation**:
1. Compute the bare dimensionless coupling at the van Hove energy scale:
   - g_bare = V(B2,B2) × rho_smooth = 0.057 × 14.02 = 0.799 (bare V)
   - g_bare = V(B2,B2) × rho_smooth = 0.086 × 14.02 = 1.206 (V at phi=gap)
2. Define the RG scale: UV cutoff = B2 bandwidth W_B2 = 0.058 (from eigenvalue data). IR cutoff = gap scale Delta (initially unknown, set by the flow).
3. Integrate the one-loop beta function dg/d(ln mu) = -g^2 from mu = W_B2 down to mu → 0.
   - Analytic solution: 1/g(mu) = 1/g_bare + ln(W_B2/mu)
   - g diverges at mu* = W_B2 × exp(-1/g_bare)
   - For g_bare = 0.80: mu* = W_B2 × exp(-1.25) = 0.058 × 0.287 = 0.0167
   - For g_bare = 1.21: mu* = W_B2 × exp(-0.83) = 0.058 × 0.436 = 0.0253
4. Compare mu* with the B2 bandwidth. If mu* > 0 and mu* < W_B2, the coupling reaches strong coupling WITHIN the bandwidth.
5. Report the Landau pole scale mu*, the effective gap Delta ~ mu*, and whether the BCS instability is guaranteed.
6. Also compute the two-loop correction to check whether the one-loop result is qualitatively stable.

**Pre-registered gate**: RG-BCS-35
- PASS: g(IR) > 1.0 within B2 bandwidth (BCS guaranteed, N_eff moot)
- FAIL: g(IR) < 1.0 throughout bandwidth (mean-field + BMF corridor analysis applies)
- NOTE: g_bare > 1 at phi=gap means the coupling STARTS above the critical value. Report whether this is a genuine strong-coupling result or an artifact of the one-loop truncation.

**Output**: Script `tier0-computation/s35_rg_bcs_flow.py`, data `s35_rg_bcs_flow.npz`, plot `s35_rg_bcs_flow.png`. Write results to Section W1-C of `sessions/session-35/session-35-results-workingpaper.md`.

---

### W1-D: K_7 Charge-Resolved Thouless Criterion

**Agent**: `gen-physicist`
**Model**: sonnet
**Cost**: ZERO (reanalysis of existing data)

**Prompt**:

You are the General Physicist. Your task is to determine whether the conserved K_7 charge restricts or enhances the BCS pairing channel.

**Context**: Session 34 proved [iK_7, D_K] = 0 at all tau. The iK_7 eigenvalues on B2 are +1/4 (2 modes) and -1/4 (2 modes). If Cooper pairs must conserve K_7 charge (total q = 0), pairing is restricted to the (+1/4) × (-1/4) channel. This may change the effective Thouless matrix structure.

**Computation**:
1. Load K_7 eigenvalues from `tier0-computation/s35a_grand_canonical_mu.npz`.
2. Load the spinor V matrix from `tier0-computation/s34a_dphys_kosmann.npz`.
3. Decompose the B2 quartet into q = +1/4 doublet and q = -1/4 doublet.
4. Compute V matrix elements BETWEEN the two charge sectors: V(+1/4, -1/4) = the charge-conserving channel.
5. Compute V matrix elements WITHIN each charge sector: V(+1/4, +1/4) and V(-1/4, -1/4) = the charge-violating channels.
6. Construct the charge-resolved Thouless matrix (2×2 in the (+1/4, -1/4) pairing channel) and compute M_max.
7. Compare with the charge-mixed 4×4 (full B2) Thouless matrix.
8. Report whether charge conservation enhances (by concentrating pairing into the allowed channel) or suppresses (by reducing available channels) M_max.
9. Also track the K_7 eigenvalue of each B2 mode as tau sweeps through [0.15, 0.25] to verify charge conservation through the fold.

**Pre-registered gate**: K7-THOULESS-35 (INFORMATIVE)
- If M_max(charge-resolved) > M_max(charge-mixed): charge conservation ENHANCES pairing
- If M_max(charge-resolved) < M_max(charge-mixed): charge conservation RESTRICTS pairing
- Report the ratio and whether q_7 is conserved through the fold (q flips → modes hybridize → N_eff changes)

**Output**: Script `tier0-computation/s35_k7_thouless.py`, data `s35_k7_thouless.npz`. Write results to Section W1-D of `sessions/session-35/session-35-results-workingpaper.md`.

---

## IV. Wave 2: Parameter Pinning & Validation

Can start in parallel with Wave 1 (no dependencies). W2-C and W2-D are medium-cost; W2-A and W2-B are zero-cost.

---

### W2-A: Van Hove Sensitivity Across Tau

**Agent**: `gen-physicist`
**Model**: sonnet
**Cost**: ZERO

**Prompt**: Compute the van Hove smooth-wall DOS integral at 5 tau evaluation points within the wall region [0.15, 0.25] (tau = 0.16, 0.18, 0.20, 0.22, 0.24). For each, compute M_max with spinor V = 0.057 and impedance = 1.0. Confirm M_max > 1.0 is generic across the wall, not specific to tau_idx = 3.

**Input data**: `tier0-computation/s35a_vh_impedance_arbiter.npz`, `tier0-computation/s23a_kosmann_singlet.npz`.
**Gate**: VH-SENS-35. PASS if M_max > 1.0 at ≥ 3 of 5 points.
**Output**: Script `s35_vh_sensitivity.py`, results to Section W2-A of working paper.

---

### W2-B: Intra-B2 Coherence Under Wall Transport

**Agent**: `gen-physicist`
**Model**: sonnet
**Cost**: ZERO

**Prompt**: Compute the transported pairing overlap: take BdG pairing amplitudes at the fold center (tau = 0.20) and transform using the eigenvector overlap matrix O between tau = 0.20 and tau = 0.15 / tau = 0.25. Report the fraction of pairing coherence surviving transport across the wall.

**Input data**: Eigenvectors from `tier0-computation/s23a_kosmann_singlet.npz`, overlap data from `s35a_vh_impedance_arbiter.npz`.
**Gate**: COH-35. INFORMATIVE. Overlap > 0.7 = coherence preserved. Overlap < 0.5 = coherence destroyed.
**Output**: Script `s35_b2_coherence.py`, results to Section W2-B of working paper.

---

### W2-C: Impedance Wave-Matching at Smooth Wall

**Agent**: `baptista-spacetime-analyst`
**Model**: sonnet
**Cost**: MEDIUM

**Prompt**: Compute the WKB or transfer-matrix transmission coefficient for a B2 mode propagating through the smooth domain wall profile. The wall profile tau(x) comes from the Turing instability (approximate as tanh with width from Session 32). The B2 eigenvalue lambda(tau) varies through the wall, with v_B2 = 0 at tau = 0.190 (turning point). Use Airy function connection formulas near the turning point. Report the physical transmission T and impedance = 1/(1-R).

**Input data**: Eigenvalue curves from `s23a_kosmann_singlet.npz`, wall profile from `s33w3_modulus_equation.npz`.
**Gate**: IMP-35. Pins impedance to single value.
**Output**: Script `s35_impedance_wavematch.py`, data `s35_impedance_wavematch.npz`, results to Section W2-C of working paper.

---

### W2-D: Multi-Sector B2 Spectrum at (1,0) Sector

**Agent**: `baptista-spacetime-analyst`
**Model**: sonnet
**Cost**: MEDIUM

**Prompt**: Compute the Dirac spectrum of D_K in the (1,0) Peter-Weyl sector at 9 tau values in [0, 0.50]. Identify the B2-like branch. Determine if it has a fold (v = 0) within [0.15, 0.25]. If yes, compute the Kosmann matrix elements V((1,0)_B2, (0,0)_B2) — the cross-sector pairing. Report whether the (1,0) sector contributes additional modes to N_eff.

**Input data**: D_K construction code from `tier0-computation/s23a_kosmann_singlet.py` (extend to (1,0) sector).
**Gate**: SECT-B2-35. INFORMATIVE. If fold exists AND V_cross > 0.01 → sector contributes to N_eff.
**Output**: Script `s35_sector_10_spectrum.py`, data `s35_sector_10_spectrum.npz`, results to Section W2-D of working paper.

---

## V. Wave 3: Physics Extraction

W3-C (Sagan) MUST wait for Wave 1 results. Others can start with Wave 2 or earlier.

---

### W3-A: Wall-Localized PMNS with Corrected V

**Agent**: `neutrino-detection-specialist`
**Model**: sonnet
**Cost**: MEDIUM

**Prompt**: Rerun the wall-localized PMNS extraction (`s33w3_wall_pmns.py`) with corrected inputs: spinor V(B1,B2) = 0.077, V(B2,B3) = 0.022, and BCS gap Delta computed self-consistently from rho_smooth = 14.02 and V(B2,B2) = 0.086 (at phi=gap). Extract theta_23, sin^2(theta_13), and mass-squared ratio R. Compare with NuFIT 5.3 global fit values.

**Gate**: PMNS-CORRECTED-35. PASS if theta_23 in [35,55] AND sin^2(theta_13) in [0.01, 0.05] AND R in [10, 100].
**Output**: Script `s35_pmns_corrected.py`, data `s35_pmns_corrected.npz`, plot `s35_pmns_corrected.png`, results to Section W3-A of working paper.

---

### W3-B: Poschl-Teller Bound States at Fold

**Agent**: `paasch-mass-quantization-analyst`
**Model**: sonnet
**Cost**: LOW

**Prompt**: Construct the effective Poschl-Teller potential at the B2 fold using wall profile from `s33w3_modulus_equation.npz` and fold curvature a_2 = 0.588 (Berry classification). Solve for bound states analytically (Poschl-Teller spectrum is exactly solvable). Count bound states and compute energy ratios.

**Gate**: PT-RATIO-35. PASS if |E_2/E_1 - 1.53158| / 1.53158 < 0.10.
**Output**: Script `s35_poschl_teller.py`, data `s35_poschl_teller.npz`, results to Section W3-B of working paper.

---

### W3-C: Sagan Probability Update

**Agent**: `sagan-empiricist`
**Model**: sonnet
**Cost**: LOW (analysis, not computation)

**Prompt**: Produce the formal post-Session-34 probability assessment. You MUST wait for Wave 1 results before writing. Account for: TRAP-33b retraction (BF reduction), van Hove correction (new BF), three permanent structural results, Wave 1 N_eff results, and the self-correction pattern. Apply the Seager Framework and Venus Rule. State the updated P(framework) with uncertainty range and BF decomposition.

**Input**: Session 34 master synthesis (`sessions/session-34/session-34-master-synthesis.md`), Wave 1 results from working paper.
**Gate**: N/A (assessment).
**Output**: Results to Section W3-C of working paper.

---

### W3-D: Spectral Entropy at Fold

**Agent**: `connes-ncg-theorist`
**Model**: sonnet
**Cost**: ZERO

**Prompt**: Compute the von Neumann spectral entropy S = -sum[n_k ln(n_k) + (1-n_k)ln(1-n_k)] where n_k = 1/(exp(beta × lambda_k) + 1), using the 16 singlet eigenvalues at each of 9 tau values. Plot S vs tau at beta = 0.5, 1.0, 2.0, 5.0. Determine if S has a maximum at or near tau = 0.190 (the fold).

**Input data**: Eigenvalues from `tier0-computation/s23a_kosmann_singlet.npz`.
**Gate**: ENTROPY-35. INFORMATIVE. If S peaks at fold → entropy-driven stabilization mechanism (Paper 15).
**Output**: Script `s35_spectral_entropy.py`, data `s35_spectral_entropy.npz`, plot `s35_spectral_entropy.png`, results to Section W3-D of working paper.

---

### W3-E: Pfaffian with Corrected J

**Agent**: `dirac-antimatter-theorist`
**Model**: sonnet
**Cost**: ZERO

**Prompt**: Reconstruct the antisymmetric matrix M = C2 × D_K where C2 = gamma_1 × gamma_3 × gamma_5 × gamma_7 (the corrected J from Session 34). Compute sgn(Pf(M)) at the same tau values used in Session 17c. Verify BDI classification survives the J correction.

**Input data**: D_K matrices from `tier0-computation/s23a_kosmann_singlet.npz`, C2 construction from `s34a_dphys_fold.py`.
**Gate**: PF-J-35. PASS if sgn(Pf) = +1 at all tau values.
**Output**: Script `s35_pfaffian_corrected_j.py`, data `s35_pfaffian_corrected_j.npz`, results to Section W3-E of working paper.

---

## VI. Wave 4: Structural & Theoretical

Lower priority. Run if capacity allows or in parallel with earlier waves.

---

### W4-A: [iK_7, D_phys] Computation

**Agent**: `baptista-spacetime-analyst`
**Model**: sonnet
**Cost**: ZERO (one matrix commutator)

**Prompt**: Compute [iK_7, D_phys] at tau = 0.190 with phi at gap-edge value (0.133) in the H_j direction. Report ||[iK_7, D_phys]|| / ||D_phys||. If near-zero → U(1)_7 preserved under inner fluctuations (stronger symmetry). If O(0.1) → broken (extract electroweak mixing angle).

**Input data**: K_7 from `s35a_grand_canonical_mu.npz`, D_phys from `s34a_dphys_fold.npz`.
**Gate**: K7-DPHYS-35. INFORMATIVE.
**Output**: Script `s35_k7_dphys.py`, results to Section W4-A of working paper.

---

### W4-B: Specificity Test on Alternative Manifolds

**Agent**: `spectral-geometer`
**Model**: sonnet
**Cost**: MEDIUM

**Prompt**: Construct the Dirac operator on SU(2)×SU(2) (dim 6, nearest comparable compact simple group product) with a comparable one-parameter metric deformation. Compute the spectral action curvature d^2S/dtau^2 at the deformation midpoint. Compare with SU(3)'s d2S = 20.43 (bare). If the curvature is comparable → SU(3) is not special. If much smaller → SU(3) is anomalously curved (evidence for specificity).

**Gate**: SPEC-35. INFORMATIVE.
**Output**: Script `s35_specificity_su2su2.py`, data `s35_specificity_su2su2.npz`, results to Section W4-B of working paper.

---

### W4-C: Optical Theorem on V Matrix

**Agent**: `feynman-theorist`
**Model**: sonnet
**Cost**: ZERO

**Prompt**: From the stored V_5x5 matrix (s34a data), compute the T-matrix via the Lippmann-Schwinger equation T = V + V×G×T where G is the BdG Green's function. Verify Im(T_ii) = sum_j |T_ij|^2 × rho_j (optical theorem / unitarity check). Report the fractional violation.

**Input data**: V matrix from `s34a_dphys_kosmann.npz`, eigenvalues from `s23a_kosmann_singlet.npz`.
**Gate**: OPT-35. PASS if violation < 10%.
**Output**: Script `s35_optical_theorem.py`, results to Section W4-C of working paper.

---

## VII. Execution Notes

### Agent Spawning

Each computation is a **single agent task** (not a team). Spawn via the Agent tool with the agent definition and the prompt above. Parallel tasks within each wave have NO dependencies and can be spawned simultaneously.

**Recommended parallel groups**:
- **Group 1** (spawn all at once): W1-A, W1-B, W1-C, W1-D
- **Group 2** (spawn when Group 1 running): W2-A, W2-B, W2-C, W2-D
- **Group 3** (spawn after Group 1 completes): W3-A, W3-B, W3-C, W3-D, W3-E
- **Group 4** (spawn when capacity allows): W4-A, W4-B, W4-C

### Python Environment

ALL scripts use the GPU venv:
```
"phonon-exflation-sim/.venv312/Scripts/python.exe" script.py
```

### Output Discipline

- Each agent writes results ONLY to their designated section in `sessions/session-35/session-35-results-workingpaper.md`
- Each agent produces a script in `tier0-computation/s35_*.py` with corresponding `.npz` and `.png`
- No agent modifies another agent's section
- The synthesis section is written LAST by the coordinator after all waves complete

### Decision Points

After Wave 1 completes, evaluate:
- If W1-C shows g_bare > 1 at phi=gap → BCS is in strong coupling regime → N_eff question may be MOOT → escalate to full non-perturbative analysis
- If W1-A shows multi-band M_max > 1.0 → N_eff > 5.5 confirmed → proceed to Wave 3 with confidence
- If W1-B shows paired ground state at rho = 14.02 → BMF-35a verdict OVERTURNED → major revision
- If ALL of W1-A through W1-D give N_eff ≤ 5.5 → BCS link CLOSED at impedance = 1.0 → pivot to impedance determination (W2-C becomes CRITICAL)
