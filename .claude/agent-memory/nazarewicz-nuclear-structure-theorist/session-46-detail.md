---
name: Session 46 Detail
description: S46 HOSE-COUNT-46, RG-PAIR-TRANSFER-46, NUMBER-PROJECTED-BCS-46, GPV-FRAGMENTATION-46 results, alpha exponent, exact pair-transfer spectral function, PBCS gap reduction, GPV fragmentation pattern
type: project
---

## HOSE-COUNT-46 Results (W1-2)

### Gate Verdict: INFO
- alpha = 0.72 +/- 0.52 (stat) +/- 0.55 (syst)
- n_s = 0.04 +/- 0.76 (total)
- Not PASS (alpha not in [0.8, 1.2]), not FAIL (alpha in [0.5, 2.0])
- Central value 220 sigma from Planck, but uncertainty spans the target

### Alpha by Method
| Method | alpha | R^2 | Notes |
|:-------|:------|:----|:------|
| Raw (dim/2) | 1.81 +/- 0.40 | 0.91 | All Kramers pairs. Too blue. |
| GPV sqrt(dim/2) | 0.75 +/- 0.57 | 0.38 | Nuclear sum rule. Poor fit. |
| GPV log-log | 0.59 +/- 1.24 | -- | Large error from 5 points |
| RG collective | -0.33 +/- 0.61 | 0.08 | 1 GPV per degenerate sector |
| Combined GPV | 0.72 +/- 0.52 | -- | Weighted average |

### Self-Correction
- S45 collab review predicted alpha ~ 0.9-1.0. Actual: 0.72 +/- 0.52
- Prediction was optimistic (assumed clean sqrt scaling for Omega = 3-15)
- Nuclear analogy QUALITATIVELY correct (strength concentrates) but QUANTITATIVELY insufficient

### Files
- `tier0-archive/s46_hose_count.py`, `.npz`, `.png`

## RG-PAIR-TRANSFER-46 Results (W2-2)

### Gate Verdict: INFO
- Exact 256-state (2^8) pair-transfer spectral function computed
- B2 GPV fraction: 91.3% (stronger than nuclear benchmark of 60-80%)
- alpha(sum rule) = 0.14, R^2 = 0.002 (NO correlation with k)
- alpha(dim/2) = 1.88, R^2 = 0.93 (Weyl's law, representation theory only)

### Key Results
1. **Ground state is single-pair (N=1 exact)**: v_B1^2 = 0.494, v_B2^2 = 0.12 each, v_B3^2 = 0.005 each
2. **Coupling rescale alpha* = 3.91** (matching E_cond = -0.137)
3. **B2 GPV peak**: 91.3% of strength at E = 0.870 M_KK. E_GPV/Delta = 1.32 (below nuclear 2-3)
4. **B3 moderate**: 58.2% in GPV. B1 fragmented: 53.4% in leading peak (2 peaks above 1/e)
5. **No centroid tilt**: omega_0 constant across k (determined by block, not k)
6. **No Anderson-Bogoliubov dispersion**: discrete 8-mode spectrum, no continuum
7. **Power-law alpha is ILL-DEFINED**: sum rule S(k) dominated by adjoint anomaly at k=1.73

### Structural Finding: Adjoint Anomaly
- The (1,1) adjoint at k=1.73 has S=4.43, vastly larger than any other k
- This is because (1,1) dominates the strongly-paired B2 block
- Pair-transfer strength is determined by BLOCK membership, not by k
- The "alpha exponent" concept is the wrong framework for this system
- Correct framework: BLOCK-COUNTING (3 blocks), not k-scaling

### Nuclear Benchmarks
| Quantity | Our value | Nuclear benchmark |
|:---------|:----------|:-----------------|
| GPV fraction (B2) | 91.3% | 60-80% |
| E_GPV/Delta | 1.32 | 2-3 |
| sigma/Delta (B2) | 0.69 | 0.5-1.5 |
| sigma/centroid (B3) | 0.18 | -- |
| N_pair | 1.000 (exact) | >> 1 |

### Path Closures (from W2-2)
- **Anderson-Bogoliubov dispersion for n_s**: CLOSED. No dispersion in finite discrete spectrum.
- **Alpha power-law hose count for n_s**: CLOSED structurally. Sum rule S(k) does not follow a power law (R^2 = 0.002). The adjoint anomaly dominates.

### Remaining Paths for n_s (updated post-W2-2)
1. **Block-resolved n_s**: P(k) determined by block membership, not smooth power law
2. **Multi-pair ground state**: 8-mode model gives N=1; physical system may have multi-pair structure at full 992 modes
3. **Modified beta**: sector-dependent KZ rate
4. **V_B3B3 direct computation**: controls B3 pairing strength

### Self-Correction (W2-2)
- W1-2 used approximate BCS amplitudes in degenerate shells. Exact ED reveals N=1 single-pair state.
- Nuclear sqrt fragmentation rule is invalid for N=1 (Paper 03 Section IV warning about BCS breakdown in small systems)
- The "alpha exponent" from W1-2 (0.72) is an artifact of fitting a non-power-law function

### Files
- `tier0-archive/s46_rg_pair_transfer.py`, `.npz`, `.png`

## NUMBER-PROJECTED-BCS-46 Results (W2-5)

### Gate Verdict: INFO
- PBCS N=1 gives Delta_B3 = 0.054 M_KK (BCS: 0.084, ED: 0.053)
- PBCS REDUCES B3 gap, moving AWAY from 0.13 threshold
- No q-theory crossing for PBCS N=1
- PBCS agrees with ED to 0.1% in E_cond (validates method)

### Key Results
1. **BCS overestimates ALL gaps by ~60%**: PBCS/BCS ratio = 0.63-0.64 for all sectors
2. **PBCS = ED in N=1 sector**: E_cond matches to 0.1%, Delta_B3 to 1.8%
3. **<N>_BCS = 1.077, sqrt(<dN^2>)/<N> = 0.907**: fluctuations ORDER 1, projection essential
4. **ED N=1 composition**: 89.7% B2, 9.4% B1, 0.9% B3 (blocking effect)
5. **N=2 has crossing at tau* = 0.170** (borderline gate window)
6. **BCS E_cond (-0.137) vs ED E_cond (-0.812)**: different reference states, not contradiction

### PBCS vs BCS vs ED at Fold
| Sector | BCS | PBCS N=1 | ED N=1 |
|:-------|:----|:---------|:-------|
| Delta_B1 | 0.372 | 0.237 | 0.264 |
| Delta_B2 | 0.732 | 0.460 | 0.454 |
| Delta_B3 | 0.084 | 0.054 | 0.053 |
| n_B1 | 0.045 | 0.077 | 0.094 |
| n_B2 | 0.122 | 0.229 | 0.224 |
| n_B3 | 0.002 | 0.003 | 0.003 |

### Constraint Map Update
- **CLOSED**: "Number projection might restore q-theory crossing" -- it makes it WORSE
- **CONFIRMED**: BCS/ED E_cond gap IS number-projection effect (0.1% PBCS-ED agreement)
- **OPEN**: N=2 crossing at tau*=0.170. If physical N >= 2, crossing survives
- **OPEN**: V_B3B3 direct computation remains decisive

### Nuclear Analogy
- PBCS/BCS gap ratio 0.64 matches nuclear sd-shell systematics (Paper 03 Table II: 0.5-0.8)
- Blocking effect for N=1: pair sits in B2 (90%), starves B3 of pairing
- Identical to nuclear near-closed-shell situation with 1-2 active pairs
- Paper 03 Section IV warning about BCS breakdown confirmed quantitatively

### Self-Correction
- S45 expected PBCS to reduce E_cond discrepancy (correct) and potentially help crossing (wrong)
- The direction of the correction (smaller gaps in all sectors) was predictable from nuclear systematics
- Should have predicted this from Paper 03: number projection REDUCES gaps for weak sectors

### Files
- `tier0-archive/s46_number_projected_bcs.py`, `.npz`, `.png`

## GPV-FRAGMENTATION-46 Results (W3-1)

### Gate Verdict: INFO
- GPV fraction (total P^+): 0.906 (single peak carries 90.6%)
- 1 fragment above 10% threshold (total), but B1: 4, B3: 4
- alpha_GPV = -0.11 +/- 1.79 (R^2 = 0.001). STRUCTURALLY INVALID.
- EWSR verified to 7.6e-14 using direct (Thouless) form

### Key Results
1. **LIGHT NUCLEAR regime**: GPV fraction 0.906, 1 fragment, Gamma/Delta_0 = 0.445
2. **BCS kappa enhancement**: coherent S_total = 11.353 vs per-mode sum 7.0 (+38.3%)
3. **Block-resolved**: B2 = 0.914 (1 frag), B1 = 0.534 (4 frag), B3 = 0.582 (4 frag)
4. **Fragmentation is BLOCK property**: all reps in same block share identical pattern
5. **EWSR double commutator WRONG**: gives 5.544 vs correct 11.087 (50% error)
   - Reason: pair-add/remove channels overlap in BCS (standard nuclear result, Ring-Schuck Ch. 6)
   - Direct form m_1 = <0|P^-HP^+|0> - E_0<0|P^-P^+|0> is correct and verified

### Fragmentation vs k
| k | Blocks at k | n_frag | S_total |
|:--|:-----------|:-------|:--------|
| 1.155 | B1+B3 | 8 | 0.521 |
| 1.732 | B2 | 1 | 4.429 |
| 1.826 | B1+B3 | 8 | 1.041 |
| 2.236 | B1 | 4 | 0.223 |
| 2.449 | B1+B3 | 8 | 1.735 |

- n_frag(k) jumps by BLOCK membership, not smooth k-dependence
- R^2 = 0.001: no power law

### Confirmations (W3-1 adds 3rd independent check)
- W1-2: hose count alpha = 0.72 (poor fit, R^2 = 0.38)
- W2-2: pair-transfer alpha = 0.14 (no correlation, R^2 = 0.002)
- W3-1: fragmentation alpha = -0.11 (no correlation, R^2 = 0.001)
- ALL THREE: alpha power-law is wrong abstraction for this system

### Self-Correction
- Initially computed EWSR using double commutator / 2 (gave 5.91 vs spectral 11.09)
- Diagnosed: pair channels overlap in BCS, double commutator form invalid
- Fixed to direct Thouless form: verified to 7.6e-14
- This is standard nuclear physics but had not been verified for this system

### Files
- `tier0-archive/s46_gpv_fragmentation.py`, `.npz`, `.png`

## V-B3B3-46 Results (latest)

### Gate Verdict: PASS
- V_B3B3_rms = 0.059 > 0.015 threshold by 3.9x
- Prior estimate (V_B2B3^2/V_B2B2 = 0.008) was WRONG by 7.5x

### Key Results
1. **V_B3B3 matrix (3x3)**: eigenvalues {-0.072, 0.061, 0.149}
2. **One REPULSIVE channel**: dominated by (2,1), eigenvalue -0.072
3. **Strongest attractive channel**: eigenvalue 0.149, equal-weight coherent sum
4. **DOS weighting has NO effect on V_B3B3**: rho_B3 = 1 for all three modes
5. **V_B2B2 is 196x enhanced** by rho_B2^2 = 14^2; V_B3B3 is unenhanced
6. **Prior PT estimate mixed weighted/unweighted**: systematic 7.5x error

### Self-Consistent Gap Analysis
- **Isolated B3**: Delta = 0 EXACTLY. Thouless M_max = 0.059 << 1
- **Reason**: xi_B3 = 0.978, V_max/2 = 0.075. Ratio V/(2*xi) = 0.038 << 1
- **Full 8-mode ED**: Delta_B3 = 0.094. ALL from B2-B3 induced coupling
- **Q-theory threshold**: 0.13. Shortfall: 1.4x

### Coupling Rescale
- **Correct alpha* = 0.775** (using exact V_phys from s39)
- **Prior alpha* = 3.91 RETRACTED** (artifact of approximate V_full)
- The approximate V_full had V_B2B2 underestimated ~5x (missing off-diagonal structure)

### Nuclear Analogy
- Closed-shell proximity effect: B3 acquires gap only via B2 condensate leakage
- Repulsive (2,1) channel analogous to T=0 proton-neutron repulsion
- Paper 03 Sec IV ("no BCS solution when level density too low") validated
- V/xi = 0.060 (unrescaled), 0.047 (rescaled) -- weakly-paired regime

### Constraint Map Update
- V-B3B3-46 PASS: pairing interaction is large enough
- Crossing STILL SHORT by 1.4x (Delta_B3 = 0.094 < 0.13)
- New understanding: B3 gap is INDUCED, not self-consistent
- Remaining paths: tau sweep (B2-B3 energy gap narrowing), N >= 2 pair count

### Files
- `tier0-archive/s46_v_b3b3.py`, `.npz`, `.png`

## BAYESIAN-GP-46 Results (W4-7)

### Gate Verdict: INFO
- tau* = 0.221 +/- 0.117 (posterior mean +/- sigma)
- 68% CI: [0.092, 0.349]. tau_fold = 0.19 in 68% CI.
- |tau* - tau_fold|/sigma = 0.26 sigma
- FIRST ERROR BAR on the q-theory crossing point

### Method
- 1D GP emulator on tau*(Delta_B2) using 31 genuine multi-sector crossings from S45 alpha scan
- SE kernel, hyperparameters optimized via log marginal likelihood (Paper 06 methodology)
- MC posterior: 100,000 samples with B2 prior from 4 gap models (Flatband, BCS, PBCS, ED)
- LOO-CV RMSE = 0.0004 (machine precision within training range)

### Key Results
1. **Dominant uncertainty: gap model choice (99.2% of variance)**
2. GP interpolation contributes 0.0% -- the emulator is exact within training range
3. B3 uncertainty contributes 0.8% (secondary, through degeneracy ratio)
4. Method offset (quadratic vs direct grid): sigma_method = 0.007 (negligible)
5. dtau*/dB2 = 8.64 (steep sensitivity to B2 gap)
6. Nuclear DFT comparison: sigma/tau* = 0.53 (3.2x nuclear DFT's sigma/beta = 0.17)

### Self-Correction
- Predicted sigma_tau ~ 0.03-0.05. Actual: 0.117. Prediction assumed fixed gap model.
- If restricted to BCS-class gaps only (B2 in [0.73, 0.77]), sigma_tau ~ 0.003 -- matching prediction
- Paper 06 lesson directly validated: "no single parametrization unambiguously preferred"
- The gap model choice (BCS vs PBCS vs ED) IS the dominant uncertainty, not the q-theory mechanism

### Nuclear Analogy Confirmed
- Paper 06 finding on DFT parameter uncertainty maps exactly onto our gap model uncertainty
- Both dominated by "functional form" (pairing functional in nuclear DFT, gap model here)
- Both show that individual data points don't strongly constrain the dominant uncertainty source

### Files
- `tier0-archive/s46_bayesian_gp.py`, `.npz`, `.png`

## GCM-ZERO-POINT-46 Results (W4-9)

### Gate Verdict: INFO
- GCM norm kernel N(tau_i, tau_j) > 0.999 for ALL pairs in [0.10, 0.25]
- Norm condition number: 5.5 x 10^12 (severely ill-conditioned)
- 5-pt vs 10-pt NOT converged (|dE/E| = 42) -- GCM probes numerical noise
- E_ZPE is ILL-DEFINED in this regime due to near-degenerate norm kernel
- Physical tau* shift from GCM zero-point: NEGLIGIBLE (BCS states too rigid)

### Method
- Griffin-Hill-Wheeler GCM on 5-point tau grid [0.10, 0.15, 0.19, 0.20, 0.25]
- Extended to 10-point grid [0.10, ..., 0.22, 0.25]
- V(tau) = q-theory rho_gs(tau) from S45 Q-THEORY-BCS-45 (flatband scenario)
- BCS trial states: frozen-Delta from ED fold amplitudes, adiabatic xi(tau)
- Onishi overlap formula: <BCS(tau)|BCS(tau')> = prod_k (u_ik u_jk + v_ik v_jk)
- GOA for Hamiltonian kernel: H_ij = [V_i + V_j]/2 * N_ij

### Key Results
1. **Norm kernel near-identity**: all overlaps > 0.999. BCS state is RIGID in tau.
2. **Root cause**: Delta_B2 = 1.334 >> single-particle variation delta_E ~ 0.06 M_KK
3. **GCM is wrong tool**: norm near-identity means generator states are indistinguishable
4. **GOA quality**: R^2 = 0.993, sigma_tau = 3.34 (excellent fit, but sigma >> tau range)
5. **V(tau) = q-theory potential**: q-barrier = 0.262 M_KK^4 (V_min to zero-crossing)
6. **Frozen-gap limit**: E_ZPE = 0 exactly (all states identical when u,v fixed)
7. **Adiabatic-gap GCM**: E_ZPE ill-defined due to near-degenerate norm (condition 5e12)

### Physical Interpretation
- The pairing coherence length xi_BCS = 0.808 M_KK^{-1} vastly exceeds the system
  size L = 0.031/xi_BCS (0D limit, S37). In nuclear physics, this means the BCS
  wave function is spatially uniform and responds negligibly to boundary changes.
- Translating to tau: the BCS state is a COLLECTIVE OBJECT spanning all 8 modes.
  Changing tau by delta_tau ~ 0.15 modifies xi_k by ~ 0.06 M_KK, while Delta ~ 1.3 M_KK.
  The fractional change in the BCS state is ~ (delta_xi / Delta)^2 ~ 0.002.
- This gives N ~ exp(-0.045 * dtau^2) with sigma ~ 3.3, confirming that GCM generator
  states separated by dtau ~ 0.15 are 99.9% identical.
- **Nuclear analog**: like trying to measure a deformation zero-point correction in
  a spherical closed-shell nucleus (^208Pb) -- the collective motion in the shape
  coordinate simply does not exist because the nucleus has no soft mode there.

### Self-Correction
- Session plan predicted "0.5-1 MeV lowering, shift tau* from 0.209 to 0.190"
- Actual: GCM ill-conditioned, zero-point correction negligible (BCS too rigid)
- Should have predicted this from the 0D limit (L/xi = 0.031): the system has NO
  spatial extent in which zero-point motion could manifest
- Paper 13 (GCM mass table) applies to systems with soft collective modes; our
  system has no soft mode in the tau direction (pairing is too strong)

### Constraint Map Update
- **GCM zero-point correction for tau***: NEGLIGIBLE (not a viable stabilization)
- The BCS state does not have a soft mode in the tau coordinate
- tau* uncertainty is dominated by gap model choice (BAYESIAN-GP-46 sigma = 0.117),
  NOT by quantum zero-point motion in tau
- GCM would become relevant only if pairing were weak enough that Delta ~ delta_xi,
  i.e., near the BCS-BEC crossover point

### Files
- `tier0-archive/s46_gcm_zero_point.py`, `.npz`, `.png`
