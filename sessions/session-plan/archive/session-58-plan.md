# Session 58 Plan: I CC You -- The Cosmological Constant: Integrability, Partition, and Self-Tuning

**Date**: 2026-03-23
**Author**: volovik-superfluid-universe-theorist (planner)
**Format**: Parallel single-agent computations across 4 waves
**Source**: S57 results (25 computations, 5 collaborative reviews, Volovik-SP workshop, Sagan probability update)
**Motivation**: S57 established the Shattering as a quantitative DM/CC partition mechanism: Omega_DM h^2 = 0.120 falls inside the predicted [0.017, 0.188] bracket, the CC sign is correct (+1.709 M_KK), and the gap collapses with N (alpha = -1.84). All five S57 reviewers unanimously identify the Josephson-to-Lambda partition as the single bottleneck. The CC remains 114 OOM too large, locked by Richardson-Gaudin integrability. S58 attacks this bottleneck from three directions: rebuilding the Bayesian emulator under the Volovik partition, testing multi-pair integrability, and computing the Hessian in integral space that determines whether a "Penrose process" (CC reduction without breaking integrability) is algebraically possible.
**Results file**: `sessions/archive/session-58/session-58-results-workingpaper.md`

---

## I. Session Objective

Resolve the Josephson-to-Lambda partition and identify whether the CC gap is permanently locked or admits a relaxation channel.

**The CC problem in this framework is now precisely stated (Volovik-SP workshop, E4):** Lambda_eff is spacelike initial data, set once at the Shattering by the GGE occupation mismatch, propagated forever by the Einstein equations. The q-theory relaxation mechanism (Paper 15-16) is the correct framework (verified to 5% by W3-3), but integrability prevents the q-variable from adjusting. The CC problem is an initial-data problem, not a dynamical-tuning problem. Three attack vectors:

1. **Volovik partition**: Does F_Josephson -> Lambda (rather than -> matter) produce NROY > 5%? This is the single gate that determines whether the DM prediction survives. (5/5 unanimous)
2. **Multi-pair integrability**: Does Richardson-Gaudin integrability survive at N_pair = 2? If it breaks, the CC solution path opens. (4/5 recommended)
3. **Integral-space Hessian**: Does the GGE sit at a saddle in Richardson-Gaudin integral space (I^8)? If a negative eigenvalue exists, the "Penrose process" can reduce delta_q without breaking integrability. (Workshop E5, highest-priority emergent idea)

**Pre-registered master gate**:

- **VOLOVIK-PARTITION-58**: Does the Volovik partition (F_Josephson = vacuum energy) produce NROY > 5%?
- **PASS**: NROY > 5% (framework viable; DM prediction stands)
- **FAIL**: NROY = 0% even under Volovik partition (framework dead for DM)
- **INFO**: NROY in (0%, 5%] (marginal, needs epsilon refinement)

**Secondary decisive gate**:

- **NPAIR2-INTEG-58**: Does integrability survive at N_pair = 2 on the 2-cell system?
- **PASS**: <r> > 0.45 (integrability broken; CC solution path opens)
- **FAIL**: <r> < 0.40 (integrability persists; CC locked)
- **INFO**: <r> in [0.40, 0.45] (intermediate, 3-pair needed)

---

## II. The Central Physics

### The Josephson-to-Lambda Partition

The S57 energy budget (W0-2): F_Josephson = -336.6 M_KK (95.9%), F_BCS = -4.38 (1.25%), F_BA = +7.02 (2.0%), F_Leggett = +3.01 (0.86%). The equilibrium theorem (Paper 05 eq 3.1; Paper 15 sec 3): the ground-state superfluid stiffness does not gravitate. Only quasiparticle excitations contribute to the gravitational mass. Therefore F_Josephson is vacuum energy, and E_matter = E_BCS + E_BA + E_Leggett = 5.65 M_KK. Under this partition, f_DM = E_L/E_matter = 0.312 and Omega_DM h^2 = 0.142 (18% from observation).

The Bayesian emulator (W3-5) returned NROY = 0% because it placed F_Josephson in the matter budget. Rebuilding under the Volovik partition is the single computation that determines whether the DM mechanism lives or dies.

### The Integrability Lock

The GGE departs from equilibrium by ||delta_n||/N = 0.195 (W0-3, 56 OOM above threshold). The near-cancellation in the Volovik formula (+0.316 - 0.315 = +0.00145, W2-3) shows the system is TRYING to self-tune but integrability prevents completion. The 0.46% residual multiplied by M_KK^4 gives 114 OOM above Lambda_obs.

Five integrability-breaking candidates from the master collab:
1. Pomeranchuk instability of GGE (Landau)
2. Phonon-phonon scattering at N_pair >> 1 (QA)
3. Off-Jensen Hamiltonian variation (Phonon)
4. Multi-mode parametric resonance (Tesla)
5. Particle-hole channel beyond BCS (Landau)

Plus the workshop emergent idea:
6. Penrose process in Richardson-Gaudin integral space (Volovik-SP, E5)

### Input Data (all existing .npz)

| File | Contents | Source |
|:-----|:---------|:-------|
| `s57_bayesian_fabric.npz` | Bayesian emulator output, NROY=0% | S57 W3-5 |
| `s57_cc_sign.npz` | Lambda_eff=+1.709, sector decomposition | S57 W2-3 |
| `s57_gge_equilibrium_gap.npz` | ||delta_n||=0.195, 3 method comparison | S57 W0-3 |
| `s57_channel_energy_budget.npz` | E_J/E_BCS/E_BA/E_L fractions | S57 W0-2 |
| `s57_leggett_partition.npz` | f_DM=0.119/0.312, squeezing params | S57 W1-2 |
| `s57_gap_scaling.npz` | alpha=-1.84, Model A/B data | S57 W1-3 |
| `s57_off_jensen_ej.npz` | Saddle at (0.200, 0), Hessian | S57 W3-4 |
| `s57_chi_q_microscopic.npz` | chi_q(SA)=317863, chi_q(BCS)=2.73 | S57 W3-3 |
| `s57_phase_diagram.npz` | E_J/E_c sweep, omega_J=1.429 | S57 W3-12 |
| `s57_parker_ba.npz` | |beta|^2=1.015, mode-independent | S57 W2-1 |
| `s57_andreev_integ.npz` | <r>=0.407, rank-1 | S57 W1-4 |
| `s57_domain_wall.npz` | E_DW=0, universality theorem | S57 W3-6 |
| `s57_fabric_dm_abundance.npz` | Omega_DM h^2 bracket [0.017, 0.188] | S57 W2-4 |
| `s57_sub_gap_partition.npz` | 31/31 sub-gap at fold | S57 W3-9 |
| `s56_leggett_fabric.npz` | omega_L at 50 tau, dispersions | S56 |
| `s56_ba_spectrum.npz` | 31 BA phonon frequencies at 50 tau | S56 |
| `s56_gge_fabric.npz` | 2-cell P_exc=6.6e-4, gap=13.04 | S56 |
| `s56_fabric_integ.npz` | <r> values, E_J sweep | S56 |
| `s54_tb_hamiltonian.npz` | 50 tau values, 32 TB eigenvalues, 93 bonds | S54 |
| `s54_ed_sweep.npz` | Pairing matrix V_kl at each tau | S54 |
| `s54_scale_factor.npz` | H(tau) at 10 points | S54 |

---

## III. Wave Structure

### Dependency Graph

```
Wave 0 (THROUGHLINE: The Volovik Partition, 4 computations [Mack: +1], ~2.5 hrs):
  W0-1: VOLOVIK-PARTITION-58      W0-2: CC-CANCELLATION-SWEEP-58
  W0-3: EPSILON-DIRECT-58         W0-4: W-DESI-58 [Mack] (after W0-1,W0-2)

  ---- Decision Point 0 ----
  ---- Does NROY > 5% under Volovik partition? ----
  ---- Is the near-cancellation structural across 50 tau? ----
  ---- Is epsilon refined to <10%? ----
  ---- [Mack] What is w_0 under the Volovik partition? ----

Wave 1 (THROUGHLINE: Multi-Pair and Integral-Space, 3 computations, ~3 hrs):
  W1-1: NPAIR2-INTEG-58           W1-2: RG-HESSIAN-58
  W1-3: ANHARMONIC-LEGGETT-58

  ---- Decision Point 1 ----
  ---- If W1-1 PASS: integrability breaks at N=2, CC path OPEN ----
  ---- If W1-2 negative eigenvalue: Penrose process exists ----
  ---- If W1-1 FAIL + W1-2 all positive: CC permanently locked ----

Wave 2 (THROUGHLINE: Gap Scaling and Off-Jensen Physics, 4 computations, ~2 hrs):
  W2-1: GAP-CG-58                 W2-2: OFF-JENSEN-TRANSIT-58
  W2-3: POMERANCHUK-GGE-58        W2-4: MULTIMODE-RESONANCE-58

  ---- Decision Point 2 ----
  ---- alpha on CG(24) consistent with chain? ----
  ---- Does physical trajectory deviate from Jensen? ----

Wave 3 (CATCH-ALL -- EVERY remaining suggestion, 16 computations [Mack: +3]):
  W3-1: ACOUSTIC-METRIC-58        W3-2: ANDREEV-PHASE-58
  W3-3: SA-SADDLE-58              W3-4: EJ-3D-LANDSCAPE-58
  W3-5: BKT-KUBO-58              W3-6: SQ-OMEGA-GGE-58
  W3-7: IMPEDANCE-BOUNDARY-58    W3-8: OMEGA-J-SWEEP-58
  W3-9: OFF-JENSEN-DW-58         W3-10: MASS-VARIATION-58
  W3-11: SQUEEZING-COVARIANCE-58 W3-12: OFF-JENSEN-BCS-58
  W3-13: EPSILON-CONSISTENCY-58
  W3-14: TRANSFER-FUNCTION-58 [Mack]  (depends on W3-6)
  W3-15: FREE-STREAMING-58 [Mack]     (depends on W3-10)
  W3-16: FRIEDMANN-DERIVATION-58 [Mack] (depends on W3-1, W0-1)
```

### Agent Roster

ALL physics agents use **opus**. Max 3-4 agents per parallel batch.

| Agent | Waves | Specialty | Source of assignment |
|:------|:------|:----------|:-------------------|
| `phonon-first-cosmologist` | W0-1 | Bayesian emulator rebuild | Master T1-1, 5/5 unanimous |
| `volovik-superfluid-universe-theorist` | W0-2, W1-2 | CC self-tuning sweep, RG Hessian | Master T1-1, Workshop E5 |
| `quantum-acoustics-theorist` | W0-3, W1-3, W3-1, W3-11 | Epsilon, anharmonic, acoustic metric | Master T1-3/T2-1, QA-collab |
| `landau-condensed-matter-theorist` | W1-1, W2-3, W3-5 | Multi-pair ED, Pomeranchuk, BKT | Master T1-2/T2-5, LAN-collab |
| `gen-physicist` | W2-1 | Gap scaling on CG(24) | Master T1-4, 3/5 |
| `schwarzschild-penrose-geometer` | W2-2, W3-9 | Off-Jensen transit dynamics, domain walls | Master T2-2, Workshop S5 |
| `tesla-resonance` | W2-4, W3-7, W3-8, W3-13 | Multi-mode resonance, impedance, omega sweep, epsilon check | Master T2-4, TES-collab |
| `baptista-spacetime-analyst` | W3-3, W3-4, W3-10 | SA saddle, 3D landscape, mass variation | BAP-collab 3.1-3.4 |
| `berry-geometric-phase-theorist` | W3-2 | Andreev phase shift, pi-junctions | QA-collab Comp 5 |
| `kitaev-quantum-chaos-theorist` | W3-6 | S(q,omega) dynamic structure factor | TES-collab 3.4, LAN implicit |
| `nazarewicz-nuclear-structure-theorist` | W3-12 | Off-Jensen BCS spectrum | PHO-collab 4b, BAP implicit |
| `feynman-theorist` | W2-1 (cross-check) | Gap scaling analytical derivation | BAP-collab 3.2 |

---

## IV. Wave 0: The Volovik Partition (THROUGHLINE)

The three computations that determine whether the DM prediction survives and characterize the CC self-tuning.

---

### W0-1: VOLOVIK-PARTITION-58 -- Bayesian Emulator Rebuild Under Volovik Partition

**Agent**: `phonon-first-cosmologist` | **Model**: opus
**Gate**: VOLOVIK-PARTITION-58
- **PASS**: NROY > 5% (framework viable for DM)
- **FAIL**: NROY = 0% even under Volovik partition (framework dead for DM)
- **INFO**: NROY in (0%, 5%]

**This is the single most important computation of S58 (5/5 unanimous).**

**Method**: Take the existing `s57_bayesian_fabric.py` and rebuild with the Volovik partition:
1. Reassign F_Josephson = -336.6 M_KK to the VACUUM sector (not matter)
2. Define E_total_matter = E_BCS + E_BA + E_Leggett = 11.4 M_KK (excitations only)
3. Recompute all derived observables under this partition:
   - f_DM = E_Leggett / E_matter (not E_Leggett / E_total)
   - Omega_DM h^2 from the revised f_DM and the S57 abundance bracket
   - Omega_Lambda from the GGE departure (Lambda_eff = +1.709 M_KK)
   - w from the GGE equation of state (w = P_vac / rho_vac)
4. Run the GP emulator over the same 6D parameter space used in W3-5
5. Compute NROY at 3-sigma implausibility threshold
6. Report sensitivity analysis: which parameter dominates the NROY surface?

**Variant B**: Also compute NROY under the intermediate partition where Leggett ZPE is included in DM (f_DM = 0.440 from W1-2). This addresses the QA-identified ambiguity (QA-collab Section 2).

**Pre-registered benchmark**: The S57 NROY = 0% was driven by f_DM elasticity -0.63 on E_J. Under the Volovik partition, E_J is removed from the matter denominator, which should dramatically reduce this elasticity.

**[Mack note]:** The w observable in this emulator needs careful treatment. The pre-Shattering w_0 in [-0.430, -0.589] was computed under a static GGE picture. The Shattering paradigm (S57) changed the physical picture fundamentally. The emulator MUST document which w values it uses and whether they have been recalculated post-Shattering. The Volovik partition changes the vacuum energy definition (P_vac, rho_vac both change when 95.9% of the budget is reassigned), so w MUST be recomputed as part of this gate -- not inherited from pre-Shattering values. See new gate W-DESI-58 below.

**Input**: `s57_bayesian_fabric.npz`, `s57_channel_energy_budget.npz`, `s57_leggett_partition.npz`, `s57_fabric_dm_abundance.npz`, `canonical_constants.py`
**Output**: `computations/s58_volovik_partition.npz`, `computations/s58_volovik_partition.png`

---

### W0-2: CC-CANCELLATION-SWEEP-58 -- Near-Cancellation Across 50 Tau Points

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus
**Gate**: INFO -- structural or accidental?

**Method**: Extend W2-3 (CC-SIGN-57) to 50 tau values. At each tau:
1. Compute the BCS ground state and GGE occupation numbers
2. Apply the per-mode Volovik formula: Lambda_eff(tau) = Sum_k delta_n_k(tau) * (E_k(tau) - mu_eff(tau))
3. Decompose into B2, B1, B3 sector contributions
4. Compute the cancellation ratio R_cancel(tau) = Lambda_eff / max(|Lambda_B2|, |Lambda_B1+B3|)
5. Track the residual Lambda_eff(tau) across the full transit

**Pre-registered criterion** (Workshop V7, SP Q3): If R_cancel stays in [0.001, 0.01] at all 50 tau points, the near-cancellation is structural (consequence of BCS algebra). If R_cancel varies by more than one order of magnitude, it is partially accidental.

**Physical significance**: The near-cancellation +0.316 - 0.315 = +0.00145 at the fold is the microscopic fingerprint of the equilibrium theorem. If it is structural, then Lambda_eff/M_KK^4 is always O(10^{-3}), and the CC problem is "only" 111 OOM (not 114). If accidental, some tau values may have much larger or smaller residuals.

**[Mack note -- STRENGTHEN]:** Add a derivative computation: at each of the 50 tau points, compute dLambda_eff/dtau. If this quantity maps to a late-time w_a through the BLV metric, the computation gains direct DESI DR2/DR3 relevance. Also compute w(tau) = P_vac(tau)/rho_vac(tau) at each point -- this is a trivial extension of the existing sweep and would show whether the dark energy equation of state evolves during transit. The tau-dependence of Lambda_eff is directly related to w(z): if Lambda_eff evolves during transit, the dark energy equation of state evolves too.

**Input**: `s54_ed_sweep.npz`, `s54_tb_hamiltonian.npz`, `s57_cc_sign.npz`, `s57_gge_equilibrium_gap.npz`, `canonical_constants.py`
**Output**: `computations/s58_cc_cancellation_sweep.npz`, `computations/s58_cc_cancellation_sweep.png`

---

### W0-3: EPSILON-DIRECT-58 -- Dipolar Coupling from Full V_bare Matrix

**Agent**: `quantum-acoustics-theorist` | **Model**: opus
**Gate**: EPSILON-DIRECT-58
- **PASS**: epsilon_direct in [0.001, 0.005] (confirms S49 and reduces uncertainty)
- **FAIL**: epsilon_direct outside [0.0005, 0.010] (S49 value wrong, Leggett predictions need revision)

**Method**: Project the V_bare matrix (from `s54_ed_sweep.npz`) onto the B2-B1 inter-band channel to extract epsilon directly:
1. Identify B2 (4 modes) and B1 (1 mode) at the fold from the eigenvalue classification
2. Extract V_{B2,B1} = <B2 | V_bare | B1> matrix elements (4x1 block)
3. Compute epsilon = ||V_{B2,B1}||^2 / (V_{B2,B2} * V_{B1,B1})
4. Propagate uncertainty from the V_bare numerical precision
5. Compare to S49 determination: epsilon = 0.00248 +/- 50%

**Physical significance**: epsilon determines the Leggett gap (omega_L0 = sqrt(2*epsilon*E_J*Delta_harm)), which controls the DM energy fraction. The current 50% uncertainty in epsilon dominates the uncertainty budget for omega_L0 (25.4% from W0-1/W3-11). Reducing sigma(epsilon) from 50% to ~5% would tighten the DM prediction from a bracket to a range.

**[Mack note]:** The gate FAIL bounds [0.0005, 0.010] are generous. If epsilon_direct = 0.001 (factor 2.5 below S49), the Leggett gap drops by factor sqrt(2.5) and the DM energy fraction drops correspondingly. The downstream consequences for Omega_DM h^2 should be mapped explicitly at whatever epsilon value emerges.

**Input**: `s54_ed_sweep.npz`, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s58_epsilon_direct.npz`

---

### W0-4 [Mack addition]: W-DESI-58 -- Equation of State Under Volovik Partition

**Agent**: `phonon-first-cosmologist` (extends W0-1) | **Model**: opus
**Gate**: W-DESI-58
- **PASS**: |w_0(Volovik) - w_0(DESI DR2)| < 3-sigma (framework consistent with DESI)
- **FAIL**: |w_0(Volovik) - w_0(DESI DR2)| > 5-sigma (framework excluded by DESI)
- **INFO**: tension between 3-sigma and 5-sigma (marginal)

**This is a missing cosmological confrontation that should accompany W0-1.**

**Method**: Compute w_0 under the Volovik partition and compare to DESI DR2.
1. Under the Volovik partition: rho_vac = Lambda_eff = +1.709 M_KK (from S57 W2-3)
2. Compute P_vac from the GGE pressure: P_vac = -rho_vac + Sum_k delta_n_k * dE_k/dV (thermodynamic identity)
3. w_0 = P_vac / rho_vac
4. Compare to DESI DR2: w_0 = -0.752, w_a = -0.73 (approximate from framework docs)
5. Compare to pre-Shattering prediction: w_0 = -0.509 +/- 0.079 (S49 P-8)
6. Report tension in sigma units using DESI DR1 error bars (sigma_w0 = 0.08, sigma_wa = 0.31)

**Why this matters [Mack]:** The pre-registered w_0 = -0.509 is already 3.1-sigma from DESI DR2. The S57 W2-3 value w_GGE = -0.408 is 4.3-sigma from DR2. The tension is WORSENING with each refinement. The Volovik partition changes rho_vac and P_vac simultaneously (95.9% of the energy budget is reassigned), so w MUST change. Whether it moves toward or away from -0.752 is the cleanest available observational test. DESI DR3 will sharpen this to definitive levels within a year.

**Observational reference**: DESI DR1: w_0 = -0.72 +/- 0.08, w_a = -0.41 +/- 0.31 (Paper 30). Planck 2018: w = -1.03 +/- 0.03 (Paper 29, assuming constant w). LCDM: w_0 = -1, w_a = 0.

**Input**: W0-1 output (`s58_volovik_partition.npz`), W0-2 output (`s58_cc_cancellation_sweep.npz`), `s57_cc_sign.npz`, `canonical_constants.py`
**Output**: `computations/s58_w_desi.npz`

---

## V. Decision Point 0

Read W0-1 through W0-3. Three questions:

1. **NROY > 5% under Volovik partition?** If PASS: the DM mechanism survives and the energy partition is validated. If FAIL: the framework cannot produce the observed DM abundance regardless of partition choice. If FAIL, re-examine the emulator's parameter space -- does epsilon refinement (W0-3) open a new NROY region?

2. **Is the near-cancellation structural?** If R_cancel in [0.001, 0.01] at all tau: the equilibrium theorem's near-cancellation is a structural consequence of BCS algebra. If R_cancel varies wildly: the fold value is partially accidental and the CC problem is tau-dependent.

3. **Is epsilon refined?** If sigma(epsilon) < 10%: all downstream Leggett predictions tighten by 5x. If epsilon_direct disagrees with S49: the Leggett gap and DM fraction need revision.

4. **[Mack] What is w under the Volovik partition?** If w_0 moves toward -0.752 (DESI DR2): the framework gains DESI consistency. If w_0 moves away from -0.752: the w tension is structural and the framework faces a serious observational challenge. If w_a != 0: the GGE is evolving and the integrability-protection assumption for DM stability needs revisiting.

Proceed to W1 regardless. W0 results inform interpretation but do not gate W1 execution.

---

## VI. Wave 1: Multi-Pair and Integral Space (THROUGHLINE)

The three computations that attack the integrability lock directly.

---

### W1-1: NPAIR2-INTEG-58 -- N_pair = 2 Exact Diagonalization on 2-Cell System

**Agent**: `landau-condensed-matter-theorist` | **Model**: opus
**Gate**: NPAIR2-INTEG-58
- **PASS**: <r> > 0.45 (integrability broken at N_pair = 2; CC path opens)
- **FAIL**: <r> < 0.40 (integrability persists; CC remains locked)
- **INFO**: <r> in [0.40, 0.45] (intermediate; N_pair = 3 needed)

**This is the next decisive frontier identified by 4/5 reviewers.**

**Method**: Exact diagonalization of the BCS Hamiltonian at N_pair = 2 on a 2-cell Josephson array.
1. Fock space: C(16,4) = 1820 states (16 single-particle modes, 4 particles for 2 pairs). Actually for 2 cells of 8 modes: C(16,4) = 1820, but with pair constraint this reduces to ~560 two-pair states.
2. Construct H = H_BCS^{(1)} + H_BCS^{(2)} + H_J at the fold (tau = 0.194)
3. Diagonalize exactly (560x560 matrix)
4. Compute level statistics: nearest-neighbor spacing ratio <r> (Wigner-Dyson threshold 0.53, Poisson 0.386)
5. Compute GGE occupation numbers at N_pair = 2 after sudden quench
6. Compare to N_pair = 1 GGE: does the occupation mismatch ||delta_n|| change?
7. Compute domain wall energy E_DW at N_pair = 2: with two pairs, can inter-cell phase mismatches develop?
8. Count Richardson-Gaudin conserved quantities: at N_pair = 2, are there still 8 independent integrals per cell, or does the inter-pair interaction break some?

**Pre-registered benchmarks**:
- N_pair = 1: <r> = 0.367-0.407 (Poisson, confirmed S56-S57)
- N_pair = 2 with E_J = 0: <r> should remain Poisson (isolated cells)
- N_pair = 2 with full E_J: the test

**Physical significance**: At N_pair = 1, integrability is trivially guaranteed (non-interacting). At N_pair = 2, pair-pair interactions emerge. If these interactions break Richardson-Gaudin integrability, the GGE can thermalize and the CC can relax. This is the minimal multi-body test.

**From S57 Landau collab**: "The physically relevant regime is N_pair >> 1... I suggest S58 should include an N_pair = 2 computation on the 2-cell system as a minimal test of multi-pair physics. The Fock space grows from 120 to 560 states, which is still tractable by exact diagonalization."

**[Mack note]:** Even if integrability breaks (<r> > 0.45), the thermalization TIMESCALE matters for cosmology. A thermalization time of 10^100 Planck times would not solve the CC problem within the age of the universe (4.3 x 10^60 t_Pl). The computation should report the thermalization rate (inverse participation ratio decay, or entanglement entropy growth rate), not just the level statistics. The gate criterion (<r>) tests the existence of the path; the timescale determines whether it is cosmologically relevant.

**Input**: `s54_tb_hamiltonian.npz`, `s54_ed_sweep.npz`, `s56_gge_fabric.npz`, `canonical_constants.py`
**Output**: `computations/s58_npair2_integ.npz`, `computations/s58_npair2_integ.png`

---

### W1-2: RG-HESSIAN-58 -- Richardson-Gaudin Hessian in Integral Space I^8

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus
**Gate**: RG-HESSIAN-58
- **PASS**: At least one negative eigenvalue (Penrose process direction exists; CC reduction possible without breaking integrability)
- **FAIL**: All eigenvalues positive (GGE is stable minimum in integral space; CC permanently locked by integrability)

**This is the single most decisive computation proposed by the Volovik-SP workshop (E5).**

**Method**: Compute the 8x8 Hessian of the thermodynamic potential Omega in Richardson-Gaudin integral space.
1. The 8 Richardson-Gaudin integrals I_k (k = 1,...,8) are the conserved quantities of the BCS Hamiltonian. At N_pair = 1, these are the single-particle occupation numbers n_k.
2. The thermodynamic potential is Omega(I_1,...,I_8) = E(I) - Sum_k lambda_k * I_k, where lambda_k are the GGE Lagrange multipliers (the 8 effective temperatures from S43 GGE-TEMP-43).
3. Compute the Hessian H_{jk} = d^2 Omega / dI_j dI_k at the GGE point p = (I_1^GGE,...,I_8^GGE)
4. Diagonalize H. Report eigenvalues and eigenvectors.
5. If any eigenvalue is negative, the GGE sits at a SADDLE in integral space. The corresponding eigenvector is the "Penrose process direction" -- the canonical transformation that reduces Lambda_eff without breaking integrability.
6. Also compute the cross-susceptibility d^2 Omega / dN dI_k for each k (Workshop E1). If any is nonzero, pair-number fluctuations couple to integral fluctuations, providing a channel for delta_q reduction.

**Physical significance**: In the Kerr black hole, the ergosphere allows energy extraction through the Penrose process. In the framework, the "ergosphere" would be the region of integral space where the Hessian has negative eigenvalues. If the GGE is in such a region, canonical transformations (NOT scattering -- these preserve integrability) can reduce the vacuum energy. This would be a CC reduction mechanism that operates through phase space geometry rather than through thermalization.

**From Workshop E5**: "The computation for S58: evaluate the 8x8 Hessian H_{jk} = d^2 Omega / dI_j dI_k at the GGE point p. If all eigenvalues are positive, the GGE is a stable fixed point in integral space and the CC is permanently locked. If any eigenvalue is negative, the GGE is a saddle, and the 'Penrose process' direction is the corresponding eigenvector."

**[Mack note]:** A negative eigenvalue in I^8 means the GGE is a saddle of the thermodynamic potential, but it does NOT mean the system can access the lower-energy state. Integrability constrains allowed trajectories to surfaces of constant I_k. The computation should check whether the negative eigenvalue direction is ACCESSIBLE given the integrability constraints -- i.e., whether the direction requires changing an I_k that is exactly conserved. If it does, the saddle is irrelevant. The "Penrose process" requires a mechanism to convert between different integrals of motion; the Hessian alone does not establish that such a mechanism exists.

**Input**: S38 GGE data (from session files), `s54_ed_sweep.npz`, `s57_gge_equilibrium_gap.npz`, `s57_cc_sign.npz`, `canonical_constants.py`
**Output**: `computations/s58_rg_hessian.npz`

---

### W1-3: ANHARMONIC-LEGGETT-58 -- Cubic and Quartic Leggett Mode Coupling

**Agent**: `quantum-acoustics-theorist` | **Model**: opus
**Gate**: ANHARMONIC-LEGGETT-58
- **PASS**: Gamma_3^2 * rho / omega_L > 1/dt_transit (harmonic approximation breaks; mode-mode redistribution during transit)
- **FAIL**: Gamma_3^2 * rho / omega_L < 1/dt_transit (harmonic safe; W1-2 independent-mode result is exact)

**Method**: Expand the Josephson potential E_J * cos(phi) beyond the quadratic (harmonic) approximation to 4th order:
1. Write cos(phi) = 1 - phi^2/2 + phi^4/24 where phi = phi_B2 - phi_B1 is the relative phase
2. Express phi in terms of the 31 normal mode amplitudes a_n: phi = Sum_n phi_n * (a_n + a_n^dag) / sqrt(2*omega_n)
3. The cubic coupling vertex: Gamma_3(n,m,p) = (E_J / 6) * phi_n * phi_m * phi_p / sqrt(8 * omega_n * omega_m * omega_p)
4. The quartic coupling vertex: Gamma_4(n,m,p,q) = (E_J / 24) * phi_n * phi_m * phi_p * phi_q / (16 * sqrt(omega_n * omega_m * omega_p * omega_q))
5. Compute the 3-phonon scattering rate: Gamma_scat = Sum_{m,p} |Gamma_3(n,m,p)|^2 * (n_m + n_p + 1) / omega_n
6. Compare Gamma_scat * dt_transit to 1

**QA pre-estimate** (QA-collab Section 5, Q1): "Gamma_3 ~ epsilon * E_J * phi_ZPF ~ 0.01 M_KK, giving Gamma_3^2/omega_L ~ 10^{-3} M_KK, and Gamma_3^2/omega_L * dt_transit ~ 10^{-6}. If this holds, the harmonic approximation is safe."

**Physical significance**: W1-2 (S57) treated each Leggett mode as independently squeezed. If anharmonic coupling is strong, modes redistribute energy during the transit, potentially changing the DM energy fraction by a factor of 2 (QA estimate).

**Input**: `s56_leggett_fabric.npz`, `s54_tb_hamiltonian.npz`, `s57_leggett_partition.npz`, `canonical_constants.py`
**Output**: `computations/s58_anharmonic_leggett.npz`

---

## VII. Decision Point 1: THE INTEGRABILITY FORK

This is the decisive junction. Read W1-1 through W1-3.

**If W1-1 PASS (<r> > 0.45)**: Integrability breaks at N_pair = 2. The CC solution path is OPEN. The thermalization rate at N_pair = 2 determines the timescale. Follow-up: compute thermalization rate and extrapolate to N_pair >> 1. This is the most important outcome -- it would establish that the CC gap is a finite-N artifact that vanishes in the thermodynamic limit.

**If W1-2 PASS (negative Hessian eigenvalue)**: The Penrose process exists. The CC can be reduced through canonical transformations in integral space without breaking integrability. Follow-up: compute the relaxation rate along the negative eigenvalue direction.

**If W1-1 FAIL AND W1-2 FAIL**: The CC is permanently locked at 114 OOM. The q-theory relaxation mechanism is algebraically inaccessible. The only remaining path would be a qualitative change in the microscopic Hamiltonian (beyond BCS, beyond Richardson-Gaudin).

**If W1-3 PASS**: The harmonic approximation for Leggett modes breaks. The DM energy fraction needs revision. Proceed to W2 with revised Leggett energetics.

Proceed to W2 regardless. W1 results inform interpretation of W2 but do not gate execution.

---

## VIII. Wave 2: Gap Scaling and Off-Jensen Physics

Four computations testing the robustness of the DM prediction and the off-Jensen escape route.

---

### W2-1: GAP-CG-58 -- Gap Scaling on the Physical CG(24) Graph

**Agent**: `gen-physicist` | **Model**: opus
**Cross-check**: `feynman-theorist` (analytical derivation of alpha from tensor product structure, BAP-collab 3.2)
**Gate**: GAP-CG-58
- **PASS**: alpha on CG(24) within 20% of chain value (-1.84)
- **FAIL**: alpha > 0 on CG(24) (DM prediction collapses; gap grows with N on physical graph)
- **INFO**: alpha in [-2.5, -1.47] or alpha in [-1.47, 0] (intermediate)

**Method**: Compute the many-body gap Delta_N on the actual Cayley graph CG(24) for N = 2, 4, 8, 16, 32 cells.
1. At each N, construct the N-cell Hamiltonian H = 1_N x H_cell + (-E_J) * A_CG x J_inter
2. A_CG is the adjacency matrix of the CG(24) graph (degree 2-4, not the linear chain used in W1-3)
3. Diagonalize at the fold (tau = 0.194) for each N
4. Extract Delta_N = E_1 - E_0 (gap between ground and first excited state)
5. Fit Delta_N ~ N^alpha. Compare to chain alpha = -1.84
6. Also measure the spectral dimension d_s from the pair return probability P(t) ~ t^{-d_s/2} on the CG graph for N = 2, 4, 8, 16, 32 (PHO-collab suggestion 3)
7. Extract the dynamical exponent z from alpha = -z/d_s. Compare to the PHO-derived z = 3.68

**From BAP-collab 5.1**: "The physical fabric is the Cayley graph CG(24) with higher connectivity (degree 2-4 vs chain degree 2). The Fiedler eigenvalue lambda_1 = 1.016 (S35) suggests faster gap collapse."

**Input**: `s54_tb_hamiltonian.npz`, `s54_ed_sweep.npz`, CG(24) adjacency matrix (from `s54_tb_hamiltonian.npz`), `canonical_constants.py`
**Output**: `computations/s58_gap_cg.npz`, `computations/s58_gap_cg.png`

---

### W2-2: OFF-JENSEN-TRANSIT-58 -- Transit Dynamics in the 2D Potential

**Agent**: `schwarzschild-penrose-geometer` | **Model**: opus
**Gate**: INFO -- sigma(tau_fold) > 0.01?

**Method**: Solve the equations of motion for (tau(t), sigma(t)) in the full 2D off-Jensen potential landscape.
1. The 2D Lagrangian (Paper 15 eq 3.79): L = (1/2)*G_J*dtau^2 + (1/2)*G_T2*dsigma^2 - V(tau, sigma)
2. G_J from S54 DeWitt metric, G_T2 = 26.2 * G_J (BAP master collab)
3. V(tau, sigma) from the off-Jensen E_J landscape (W3-4 data, `s57_off_jensen_ej.npz`)
4. Initial conditions: (tau_0, sigma_0) = (0, 0) with dtau/dt from S54 scale factor
5. Add small perturbation in sigma: sigma_0 = 10^{-6}, 10^{-4}, 10^{-2}
6. Integrate forward using RK4 adaptive step
7. Track sigma(tau) to determine: does sigma grow, oscillate, or decay?
8. Report sigma(tau_fold) for each initial perturbation amplitude

**Pre-registered constraint** (Workshop V4/V8 convergence): "Growth time t_grow ~ 17.5 M_KK^{-1} vs transit time 6.84e-4 M_KK^{-1}. Growth factor exp(3.9e-5) = 1.000039." The transit dynamics should confirm sigma remains frozen. If sigma grows beyond 0.01, the off-Jensen direction is dynamically accessed despite the kinematic suppression.

**Physical significance**: If the physical trajectory stays on Jensen (sigma = 0), the 1D moduli space assumption is justified. If it deviates, the entire DM/CC partition changes because E_J(tau, sigma != 0) differs from E_J(tau, 0).

**Input**: `s57_off_jensen_ej.npz`, `s54_scale_factor.npz`, `canonical_constants.py`
**Output**: `computations/s58_off_jensen_transit.npz`, `computations/s58_off_jensen_transit.png`

---

### W2-3: POMERANCHUK-GGE-58 -- Landau Parameters and Stability

**Agent**: `landau-condensed-matter-theorist` | **Model**: opus
**Gate**: POMERANCHUK-GGE-58
- **PASS**: Any F_l violates stability bound -(2l+1) (GGE spontaneously deforms; integrability-breaking candidate)
- **FAIL**: All F_l satisfy stability bounds (GGE is Pomeranchuk-stable)

**Method**: Compute the Landau Fermi-liquid parameters from the GGE occupation distribution.
1. The GGE has non-thermal occupation numbers n_k spanning effective temperatures from 0.178 to 0.668 M_KK (S43 GGE-TEMP-43)
2. For a discrete 8-mode system, the Landau parameters are:
   F_l = N(0) * Sum_k V(k,k') * P_l(cos theta_{kk'})
   where V(k,k') is the quasiparticle interaction matrix and P_l are Legendre polynomials
3. The interaction matrix V(k,k') comes from the BCS interaction `s54_ed_sweep.npz`
4. Compute F_0, F_1, F_2 (s-wave, p-wave, d-wave Landau parameters)
5. Test stability: F_l > -(2l+1) for all l. If violated for any l, the GGE is Pomeranchuk-unstable
6. If unstable: compute the growth rate of the instability. Determine whether the instability breaks the Richardson-Gaudin conservation laws.

**From LAN-collab Section 5, Q5**: "A computation of the Landau parameters from the GGE distribution would determine whether the post-transit state is Pomeranchuk-stable or whether it spontaneously deforms."

**Note**: The 0D discrete system may not strictly admit Landau parameter decomposition (no angular momentum quantum number for 8 discrete modes). Map the 8 modes onto effective angular channels using the representation-theoretic decomposition: B2 (4 modes, l=0 singlet under U(2)), B1 (1 mode, l=0 singlet), B3 (3 modes, l=1 triplet under SU(2)). The stability analysis then reduces to checking F_0 for B2 and B1, and F_1 for B3.

**Input**: `s57_gge_equilibrium_gap.npz`, `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s58_pomeranchuk_gge.npz`

---

### W2-4: MULTIMODE-RESONANCE-58 -- Three-Mode Resonance Census

**Agent**: `tesla-resonance` | **Model**: opus
**Gate**: INFO -- any resonance within Gamma (transit-induced broadening)?

**Method**: Enumerate all 3-mode resonance conditions among 63 collective modes at the fold.
1. The 63 modes: 31 BA (frequencies from `s56_ba_spectrum.npz`), 31 Leggett (from `s56_leggett_fabric.npz`), 1 plasma (omega_J = 1.429 M_KK from W3-12)
2. For each triplet (a, b, c) from the 63 modes, compute delta_abc = |omega_a - omega_b - omega_c|
3. The transit-induced broadening Gamma = 1/dt_transit = 1/(1.13e-3) ~ 885 M_KK. This is enormous -- every mode is broadened well beyond its natural frequency.
4. Count resonances: N_res = number of triplets with delta_abc < Gamma
5. If N_res > 0 with meaningful coupling, compute the parametric gain coefficient g = Gamma_3^2 / (Gamma * delta_abc)
6. Also check 4-mode resonances (Gamma_4 processes)

**Pre-registered concern**: The broadening Gamma ~ 885 M_KK is so large that EVERY triplet satisfies the resonance condition (all mode frequencies < 4 M_KK). The physical question is not whether resonances exist but whether the COUPLING STRENGTH is sufficient to produce energy transfer. This computation must report coupling coefficients, not just resonance counts.

**From TES-collab 3.1**: "Enumerate all 3-mode resonance conditions omega_a = omega_b + omega_c among 63 collective modes at the fold. Count how many satisfy |omega_a - omega_b - omega_c| < Gamma."

**[Mack note -- DEPRIORITIZE]:** The sudden-quench limit has been confirmed so thoroughly (S57 W1-1: P_exc saturates above 10 M_KK, physical rate is 442 M_KK) that in-transit energy redistribution is implausible. The broadening Gamma ~ 885 M_KK means every triplet satisfies the resonance condition, so the computation reduces to coupling coefficients -- and the effective interaction time dt_transit ~ 10^-3 M_KK^-1 is too short for any resonance to develop. This computation is very likely to confirm the sudden-quench picture rather than discover new physics. Recommend running only if Wave 2 batch has spare capacity.

**Input**: `s56_ba_spectrum.npz`, `s56_leggett_fabric.npz`, `s57_phase_diagram.npz`, `canonical_constants.py`
**Output**: `computations/s58_multimode_resonance.npz`

---

## IX. Decision Point 2

Read W2-1 through W2-4.

1. **Does alpha on CG(24) match the chain?** If within 20%: the gap scaling is universal and the DM prediction is robust against graph topology. If alpha > 0: the DM prediction collapses (Sagan BF ~ 0.1).

2. **Does the trajectory stay on Jensen?** If sigma < 0.01 at fold: Jensen is validated. If sigma > 0.01: the off-Jensen direction is dynamically accessed, and the energy partition changes.

3. **Is the GGE Pomeranchuk-stable?** If unstable: first concrete integrability-breaking mechanism. If stable: one candidate eliminated.

4. **Are multi-mode resonances coupled?** If coupling coefficients are negligible (as expected given the sudden-quench limit): Tesla's channel is closed for S58. If significant: a new thermalization path opens.

---

## X. Wave 3: Catch-All (EVERY Remaining Suggestion + Mack Cosmological Gates)

All remaining suggestions from the five S57 collab reviews and the Volovik-SP workshop, plus 3 new cosmological gates from the Mack review. Nothing deferred to S59.

---

### W3-1: ACOUSTIC-METRIC-58 -- Unruh Acoustic Metric Construction

**Agent**: `quantum-acoustics-theorist` | **Model**: opus
**Gate**: ACOUSTIC-METRIC-58
- **PASS**: |T_acoustic/T_GH - 1| < 0.5 (phononic and geometric pictures self-consistent)
- **INFO**: T_acoustic computed but ratio outside range

**Method**: Construct the explicit Unruh (1981) acoustic metric for phonon propagation on the 32-cell fabric.
1. The acoustic metric: ds^2 = (rho/c) * [-c^2 dt^2 + (dx - v*dt)^2] where c = c_BA(tau) and v = dtau/dt
2. Compute at 50 tau values using c_BA from `s56_ba_spectrum.npz` and a(tau) from `s54_scale_factor.npz`
3. Compute the Ricci scalar R_acoustic(tau) from the metric
4. Compute the acoustic Hawking temperature T_acoustic(tau) = hbar * kappa_acoustic / (2*pi*c_BA) where kappa_acoustic is the surface gravity
5. Compare T_acoustic to T_GH(tau) at each tau

**From QA-collab Computation 4**: "If T_acoustic = T_GH, the phononic and geometric pictures are self-consistent. If T_acoustic differs, the acoustic metric provides an independent prediction for the particle creation rate."

**[Mack note -- PROMOTE to Wave 1 or early Wave 2]:** This computation builds the bridge between the internal SU(3) physics and the 4D FRW observer. It is more cosmologically relevant than several Wave 1 computations (e.g., W1-3 anharmonic Leggett). The acoustic metric provides the physical interpretation of the sound speed hierarchy c_fabric/c_Gold = 229.5, which enters the CMB multipole prediction (l ~ 721). If T_acoustic = T_GH, the framework's two descriptions (phononic and geometric) are unified -- this is prerequisite to deriving the Friedmann equation and therefore prerequisite to every distance-based cosmological prediction (BAO, SN Ia, CMB distances). Without this bridge, the framework cannot make contact with precision cosmology.

**Input**: `s56_ba_spectrum.npz`, `s54_scale_factor.npz`, `canonical_constants.py`
**Output**: `computations/s58_acoustic_metric.npz`, `computations/s58_acoustic_metric.png`

---

### W3-2: ANDREEV-PHASE-58 -- Sub-Gap Andreev Phase Shift and Pi-Junction Search

**Agent**: `berry-geometric-phase-theorist` | **Model**: opus
**Gate**: INFO -- any loop phase within 5% of pi?

**Method**: Compute the Andreev reflection phase shift for each of the 31 sub-gap BA modes at the fold.
1. Phase shift formula: phi_A(n) = arccos(omega_BA(n) / Delta_GL) for each BA mode with omega_BA(n) < 2*Delta_GL
2. For each of the 62 independent loops on the CG(24) graph (b_1 = 93 - 32 + 1 = 62):
   - Sum the Andreev phase shifts around the loop: Phi_loop = Sum_{bonds in loop} phi_A(n) for representative mode n
   - Check: |Phi_loop - pi| < 0.05*pi for any loop?
3. If pi-junction detected: the fabric has frustrated ground states (topological effect)
4. Report the distribution of loop phases

**From QA-collab Computation 5**: "If any loop phase equals pi (mod 2pi), the fabric contains pi-junctions with frustrated ground states -- a topological effect connecting to Z_3 impedance."

**Input**: `s56_ba_spectrum.npz`, `s54_ed_sweep.npz`, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s58_andreev_phase.npz`

---

### W3-3: SA-SADDLE-58 -- Spectral Action Hessian at the Fold

**Agent**: `baptista-spacetime-analyst` | **Model**: opus
**Gate**: INFO -- det(H_S) < 0?

**Method**: Compute the 2D Hessian of the spectral action at (tau_fold, sigma=0).
1. The spectral action S[D_K(tau, sigma)] depends on the full 992-eigenvalue Dirac spectrum
2. Compute d^2S/dtau^2, d^2S/dtau dsigma, d^2S/dsigma^2 at the fold
3. Use the heat kernel factorization from Paper 33: a_4^{MxK} = a_4^M a_0^K + a_2^M a_2^K + a_0^M a_4^K
4. Compute det(H_S) = (d^2S/dtau^2)(d^2S/dsigma^2) - (d^2S/dtau dsigma)^2
5. If det(H_S) < 0: the spectral action ALSO has a saddle at the fold, and the tension between geometric (SA) and many-body (BCS) physics identified in S37 would be resolved
6. Compare the SA Hessian eigenvalues to the E_J Hessian eigenvalues [-0.0856, +0.0841]

**From BAP-collab 3.3**: "If the spectral action landscape has NO saddle where E_J does, this would be a diagnostic of the tension between geometric (spectral action) and many-body (BCS) physics."

**Input**: `s54_ed_sweep.npz` (for Dirac spectrum at sigma=0 and nearby), `s57_off_jensen_ej.npz`, `canonical_constants.py`
**Output**: `computations/s58_sa_saddle.npz`

---

### W3-4: EJ-3D-LANDSCAPE-58 -- Full U(2)-Invariant E_J Surface

**Agent**: `baptista-spacetime-analyst` | **Model**: opus
**Gate**: INFO -- does the saddle persist or is it lifted?

**Method**: Extend E_J(tau, sigma) to the full 3D U(2)-invariant surface including the T1 breathing mode.
1. Paper 15 eq 3.60: metric g = lambda_1 g_0|_{u(1)} + lambda_2 g_0|_{su(2)} + lambda_3 g_0|_{C^2}
2. The Jensen family constrains lambda_1 * lambda_2^3 * lambda_3^4 = 1 (volume-preserving)
3. The T1 direction breaks volume preservation: lambda_1 -> lambda_1 * (1 + delta_1)
4. Compute E_J(tau, sigma, delta_1) at the fold on a 3D grid
5. Compute the 3x3 Hessian and diagonalize
6. Report: does the saddle from W3-4 persist on the 3D surface, or is it lifted by the T1 direction?

**From BAP-collab 3.1**: "If the saddle structure persists on the full 3D surface, this would be a strong geometric constraint; if it is resolved (saddle lifted), this tells us the volume constraint is essential for the instability."

**Input**: `s57_off_jensen_ej.npz`, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s58_ej_3d_landscape.npz`, `computations/s58_ej_3d_landscape.png`

---

### W3-5: BKT-KUBO-58 -- Superfluid Stiffness and BKT on Finite Graph

**Agent**: `landau-condensed-matter-theorist` | **Model**: opus
**Gate**: INFO -- exact T_BKT vs mean-field estimate

**Method**: Compute the superfluid stiffness rho_s(T) from the Kubo formula on CG(24).
1. The Kubo formula: rho_s = (1/N) * lim_{q->0} [f_xx(q,0) / q^2]
2. For a discrete graph, replace q by the graph Laplacian eigenvalue lambda_1 (Fiedler)
3. Compute rho_s at 20 temperature values from T = 0 to T = 2*T_BKT^MF
4. Identify the universal jump: rho_s(T_BKT) = 2*T_BKT / pi
5. Compare exact T_BKT to the mean-field estimate T_BKT^MF = pi*E_J/(2*z) from W3-12 (z = 5.81)
6. Quantify the finite-size correction: T_BKT(exact) / T_BKT^MF

**From LAN-collab Section 3**: "A quantitative BKT analysis should compute the superfluid stiffness rho_s(T) from the Kubo formula on the 32-cell graph and identify the temperature where the universal jump condition is satisfied."

**Input**: `s54_tb_hamiltonian.npz`, `s57_phase_diagram.npz`, `canonical_constants.py`
**Output**: `computations/s58_bkt_kubo.npz`

---

### W3-6: SQ-OMEGA-GGE-58 -- Dynamic Structure Factor S(q, omega) of Post-Transit GGE

**Agent**: `kitaev-quantum-chaos-theorist` | **Model**: opus
**Gate**: INFO -- hard gap visible? Non-thermal occupation resolvable?

**Method**: Compute the dynamic structure factor of the post-transit GGE state.
1. S(q, omega) = Sum_{n,m} |<m|rho_q|n>|^2 * f_n * (1 - f_m) * delta(omega - E_m + E_n)
2. rho_q is the density operator projected onto the BA and Leggett mode basis
3. f_n are the GGE occupation numbers (non-thermal, 8 effective temperatures)
4. Compute at the fold for q spanning the CG graph Laplacian eigenvalues
5. Plot S(q, omega) as a 2D heat map
6. Identify features: hard gap at 2*Delta_GL, sub-gap BA continuum, non-thermal Leggett excitations
7. Compare to thermal equilibrium S(q, omega) at the single best-fit temperature

**From TES-collab 3.4**: "Computing S(q, omega) would produce the first direct prediction of what the 'dark matter' excitation spectrum looks like."

**[Mack note -- PROMOTE to Wave 2]:** S(q, omega) is the DM excitation spectrum -- "what dark matter looks like" in this framework. It is a necessary precursor to the phononic DM transfer function T(k), which is the single most impactful cosmological computation the project could do (Phononic-to-Cosmos Section 8.1, Paper 15 methods). The hard gap, sub-gap continuum, and non-thermal Leggett features are observable signatures that distinguish phononic DM from CDM/WDM. The comparison with thermal equilibrium S(q, omega) at the best-fit temperature (step 7) is the right test: non-thermal features in S(q, omega) would be a genuine novel prediction. Promote to Wave 2 and add a follow-up computation (TRANSFER-FUNCTION-58, see new gate below) that converts S(q, omega) to T(k).

**Input**: `s57_gge_equilibrium_gap.npz`, `s56_ba_spectrum.npz`, `s56_leggett_fabric.npz`, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s58_sq_omega_gge.npz`, `computations/s58_sq_omega_gge.png`

---

### W3-7: IMPEDANCE-BOUNDARY-58 -- Acoustic Impedance at Domain Boundaries

**Agent**: `tesla-resonance` | **Model**: opus
**Gate**: INFO -- T > 0.5 (transparent) or T < 0.5 (trapped)?

**Method**: Compute the acoustic impedance mismatch at C2 bond boundaries post-reconnection.
1. Z_cell = rho_cell * c_BA_cell for a single isolated cell
2. Z_bond = rho_bond * c_BA_bond for a C2-connected pair
3. Reflection coefficient: R = (Z_cell - Z_bond) / (Z_cell + Z_bond)
4. Transmission coefficient: T = 1 - R^2
5. Compute at 20 tau values spanning the reconnection event (tau ~ 0.487 from W3-2)
6. Report: are post-transit excitations trapped within cells or do they propagate?

**From TES-collab 3.2**: "Compute Z_cell, Z_bond, and transmission coefficient T = 1 - R^2 to determine if post-transit excitations are trapped or propagate."

**Input**: `s57_percolation_cc.npz`, `s56_ba_spectrum.npz`, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s58_impedance_boundary.npz`

---

### W3-8: OMEGA-J-SWEEP-58 -- omega_J vs omega_att Full Transit Verification

**Agent**: `tesla-resonance` | **Model**: opus
**Gate**: INFO -- |omega_J/omega_att - 1| < 1% at all tau?

**Method**: Track omega_J(tau) = sqrt(8*E_J(tau)*E_c(tau)) and omega_att(tau) at 50 tau values.
1. E_J(tau) from `s54_tb_hamiltonian.npz` (J_C2 coupling)
2. E_c(tau) = e^2 / (2*C_J(tau)) from the charging energy
3. omega_att(tau) from S38 attractor frequency data
4. Compute the ratio omega_J(tau)/omega_att(tau) at each tau
5. Report: does the identification hold across the full transit or only at the fold?
6. If they diverge: identify the tau range where the identification breaks

**From TES-collab Section 5, Q1**: "Does omega_J(tau) track omega_att(tau) across the full transit, or only at the fold?"

**Input**: `s54_tb_hamiltonian.npz`, `s54_ed_sweep.npz`, S38 data (from session files), `canonical_constants.py`
**Output**: `computations/s58_omega_j_sweep.npz`, `computations/s58_omega_j_sweep.png`

---

### W3-9: OFF-JENSEN-DW-58 -- Domain Walls from Off-Jensen Cell Differentiation

**Agent**: `schwarzschild-penrose-geometer` | **Model**: opus
**Gate**: INFO -- E_DW(delta_sigma) > 0?

**Method**: If cells deform to different sigma values, compute the interface energy.
1. At the fold, take two adjacent cells: cell 1 at sigma = 0, cell 2 at sigma = delta_sigma
2. Compute E_J(bond) between cells at different sigma values
3. The domain wall energy: E_DW(delta_sigma) = E_J(sigma_1, sigma_2) - E_J(0, 0)
4. Scan delta_sigma from 10^{-4} to 0.1 in 20 steps
5. Report: is E_DW > 0 (walls cost energy) or < 0 (walls are energetically favorable)?
6. If E_DW > 0: this is the first mechanism for non-trivial domain walls, circumventing the GGE universality theorem (which assumes identical Hamiltonians in all cells)

**From PHO-collab suggestion 4c**: "If cells deform to different sigma values, compute the interface energy. First mechanism for non-trivial domain walls circumventing GGE universality."

**Input**: `s57_off_jensen_ej.npz`, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s58_off_jensen_dw.npz`

---

### W3-10: MASS-VARIATION-58 -- Paper 16 eq 7.1 Mass Variation Integral

**Agent**: `baptista-spacetime-analyst` | **Model**: opus
**Gate**: INFO -- dm/dtau integral changes DM prediction by > 10%?

**Method**: Compute the geometric mass variation integral along the transit from Paper 16 eq 7.1.
1. Paper 16 eq 7.1: dm/dtau = m * tr(g_K^{-1} * dg_K/dtau) / (2*(d_K+4))
2. g_K(tau) is the Jensen-deformed metric on SU(3) at each tau
3. For the Jensen family: g_K = diag(e^{2s}, e^{-2s}, e^{-2s}, e^{-2s}, e^s, e^s, e^s, e^s) in the Ad(U(2)) basis
4. Compute the trace at 50 tau values
5. Integrate: delta_m/m = integral_0^{0.5} [tr(g_K^{-1} dg_K/dtau)] dtau / (2*14)
6. Report: does the geometric mass variation change the DM density prediction by > 10%?

**From BAP-collab 5.3**: "Paper 16 eq 7.1 gives the mass variation rate for a test particle on M^4 x K. Flagged since S53, still uncomputed."

**[Mack note -- STRENGTHEN]:** Pair this computation with a free-streaming constraint check. Compute the phononic DM velocity dispersion at production and compare to the Paper 16 bound z_tr > 6.2 x 10^7. The Leggett mode group velocity c_Gold = 0.915 M_KK sets the initial velocity dispersion; the mass variation integral determines how it redshifts. This would be the first direct confrontation between the DM candidate and hidden-sector constraints from Paper 16 (Lin-Chen-Ganjoo-Hou-Mack 2023). See new gate FREE-STREAMING-58 below.

**Input**: Paper 16 eq 7.1 formula, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s58_mass_variation.npz`

---

### W3-11: SQUEEZING-COVARIANCE-58 -- Multi-Mode Squeezing Covariance Matrix

**Agent**: `quantum-acoustics-theorist` | **Model**: opus
**Gate**: INFO -- ||C_off-diag|| / ||C_diag|| > 0.1?

**Method**: Compute the covariance matrix of the 31-mode squeezed Leggett state after the transit.
1. C_{nm} = <a_n^dag a_m> for the 31 Leggett modes
2. Each mode is independently squeezed with parameters from W1-2 (`s57_leggett_partition.npz`)
3. For independent squeezing: C_{nm} = delta_{nm} * sinh^2(r_n) where r_n is the squeezing parameter
4. For correlated squeezing (common drive): off-diagonal elements arise from the time-ordering of the common E_J(tau) drive
5. Compute both the independent and correlated covariance matrices
6. Report the ratio ||C_off-diag|| / ||C_diag||

**From QA-collab Computation 3**: "If C_{nm} is diagonal, modes are independent and W1-2 is exact. If C_{nm} has significant off-diagonal elements, mode-mode correlations modify the energy partition."

**Input**: `s57_leggett_partition.npz`, `s56_leggett_fabric.npz`, `canonical_constants.py`
**Output**: `computations/s58_squeezing_covariance.npz`

---

### W3-12: OFF-JENSEN-BCS-58 -- BCS Spectrum at sigma != 0

**Agent**: `nazarewicz-nuclear-structure-theorist` | **Model**: opus
**Gate**: INFO -- Delta_BCS(sigma=0.01) vs Delta_BCS(sigma=0) differ by > 5%?

**Method**: Compute the Dirac eigenvalues at sigma != 0 (T2-deformed metric).
1. At the fold, deform the Jensen metric along the T2 direction: lambda_1 -> lambda_1*(1 + sigma*(-11)), lambda_2 -> lambda_2*(1 + sigma*(-7)), lambda_3 -> lambda_3*(1 + sigma*(8)), normalized to preserve volume
2. Recompute the Dirac spectrum D_K at sigma = 0, 0.001, 0.005, 0.01, 0.05
3. Extract the BCS-active 8 modes and compute Delta_BCS(sigma) at each sigma
4. Compute omega_L0(sigma) (Leggett frequency shift)
5. Compute the GGE occupation numbers at each sigma
6. Report: how sensitive is the DM/CC partition to off-Jensen deformations?

**From PHO-collab suggestion 4b**: "Compute Dirac eigenvalues at sigma != 0. Determine how the BCS gap, Leggett frequency, and GGE occupations change off-Jensen."

**Input**: `s54_ed_sweep.npz`, `s57_off_jensen_ej.npz`, `canonical_constants.py`
**Output**: `computations/s58_off_jensen_bcs.npz`

---

### W3-13: EPSILON-CONSISTENCY-58 -- Two-Speed Hierarchy Epsilon Cross-Check

**Agent**: `tesla-resonance` | **Model**: opus
**Gate**: INFO -- epsilon_implied within 20% of S49 value 0.00248?

**Method**: Invert the multi-band Leggett formula to extract epsilon from the measured two-speed hierarchy.
1. omega_L / omega_J = sqrt(2 * epsilon * rho_s_B2 * rho_s_B1 / rho_s_total^2)
2. From W3-12 (S57): E_J = 3.40, E_c = 0.075, giving omega_J = 1.429 M_KK
3. From W3-11 (S57): omega_L0 = 0.049 M_KK at fold
4. The superfluid densities rho_s_B2, rho_s_B1 from `s54_ed_sweep.npz`
5. Solve for epsilon_implied = (omega_L0/omega_J)^2 * rho_s_total^2 / (2 * rho_s_B2 * rho_s_B1)
6. Compare to S49 determination: epsilon = 0.00248 +/- 50%
7. Compare to W0-3 direct extraction (if available from Wave 0 output)

**From TES-collab 3.3**: "Using omega_J and omega_L to PREDICT epsilon -- has not been done from the S57 fabric data directly. If they agree, the two-speed hierarchy is a consistency check on the dipolar coupling."

**Input**: `s57_phase_diagram.npz`, `s57_omega_l_tau_sweep.npz`, `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s58_epsilon_consistency.npz`

---

### W3-14 [Mack addition]: TRANSFER-FUNCTION-58 -- Phononic DM Transfer Function T(k)

**Agent**: `phonon-first-cosmologist` or `mack-cosmic-bridge` | **Model**: opus
**Gate**: TRANSFER-FUNCTION-58
- **PASS**: WDM mass equivalent > 5.3 keV (Lyman-alpha compatible; DM candidate survives)
- **FAIL**: WDM mass equivalent < 2.0 keV (excluded by Lyman-alpha; DM candidate dead)
- **INFO**: WDM mass equivalent in [2.0, 5.3] keV (marginal; depends on Lyman-alpha analysis details)

**This is my top cosmological recommendation (Phononic-to-Cosmos Section 8.1).**

**Method**: Compute the matter power spectrum transfer function T(k) from the phononic DM dispersion relation.
1. The phononic DM has dispersion omega(K) = 2J(1 - cos Ka) from the tight-binding Hamiltonian
2. Use S(q, omega) from W3-6 (SQ-OMEGA-GGE-58) as the input spectrum
3. Apply Paper 15 (Ganjoo-Erickcek-Lin-Mack 2022) methods: compute the transfer function for a hidden-sector particle with known dispersion, production temperature (GGE effective temperatures from S43), and equation of state
4. T(k) = P_phononic(k) / P_CDM(k) at k = 1, 10, 100 h/Mpc
5. Identify the cutoff scale k_cut where T(k) drops below 0.5
6. Convert k_cut to an equivalent WDM thermal mass using the standard WDM-CDM transfer function mapping
7. Compare to Lyman-alpha constraint: m_WDM > 5.3 keV (Irsic et al. 2017)

**Why this matters [Mack]:** The phononic DM has a SPECIFIC dispersion relation that produces a SPECIFIC cutoff in P(k). CDM predicts T(k) = 1 (no cutoff). WDM has T(k) ~ [1 + (k/k_cut)^{2nu}]^{-5/nu} with nu ~ 1.12. Phononic DM will have a DIFFERENT functional form with oscillatory features from the lattice dispersion. This is the most discriminating cosmological observable the framework can produce. If T(k) passes Lyman-alpha, the DM candidate gains substantial credibility. If it fails, the candidate is excluded. Either way, this is decisive.

**Depends on**: W3-6 (S(q, omega)), W3-7 (impedance -- determines whether DM propagates)
**Input**: W3-6 output (`s58_sq_omega_gge.npz`), Paper 15 formulas, `canonical_constants.py`
**Output**: `computations/s58_transfer_function.npz`, `computations/s58_transfer_function.png`

---

### W3-15 [Mack addition]: FREE-STREAMING-58 -- Free-Streaming Bound from Paper 16

**Agent**: `baptista-spacetime-analyst` (extends W3-10) | **Model**: opus
**Gate**: FREE-STREAMING-58
- **PASS**: z_tr > 6.2 x 10^7 (DM becomes non-relativistic early enough; structure formation compatible)
- **FAIL**: z_tr < 6.2 x 10^7 (DM free-streams too long; conflicts with observed small-scale structure)

**Method**: Compute the characteristic redshift at which phononic DM becomes non-relativistic.
1. The DM velocity dispersion at production is set by the Leggett mode group velocity: v_prod = c_Gold = 0.915 M_KK
2. The mass variation integral from W3-10 determines the late-time mass m(z)
3. The DM becomes non-relativistic when v(z) = v_prod * (1+z_prod)/(1+z) drops below c/3
4. Compute z_tr from this criterion
5. Compare to Paper 16 (Lin-Chen-Ganjoo-Hou-Mack 2023) bound: z_tr > 6.2 x 10^7

**Why this matters [Mack]:** This is a necessary condition the DM candidate must satisfy. The computation is straightforward once the mass variation (W3-10) is known. Phononic DM is WARM at production (v = 0.915 M_KK ~ c) and must cool sufficiently by z ~ 10^7 to form the observed small-scale structure. If it fails this bound, it fails as a DM candidate regardless of the abundance prediction.

**Depends on**: W3-10 (mass variation integral)
**Input**: W3-10 output (`s58_mass_variation.npz`), Paper 16 eq 7.1, `canonical_constants.py`
**Output**: `computations/s58_free_streaming.npz`

---

### W3-16 [Mack addition]: FRIEDMANN-DERIVATION-58 -- H(z) from Spectral Action Source Terms

**Agent**: `quantum-acoustics-theorist` (extends W3-1 acoustic metric) | **Model**: opus
**Gate**: FRIEDMANN-DERIVATION-58
- **PASS**: H^2 derivable from spectral geometry source terms; H_0 within order of magnitude of 67-73 km/s/Mpc
- **FAIL**: structural obstruction prevents Friedmann equation derivation (documented with specific obstruction)
- **INFO**: partial derivation only (some terms missing or ambiguous)

**Method**: Derive or obstruct the Friedmann equation from the spectral action framework.
1. The spectral action a_2 and a_4 coefficients provide the gravitational sector: R and R^2 terms
2. The matter content is E_matter = E_BCS + E_BA + E_Leggett = 11.4 M_KK (quasiparticle excitations)
3. The vacuum content is Lambda_eff = +1.709 M_KK (GGE excess)
4. Use the acoustic metric from W3-1 to map internal SU(3) dynamics to FRW expansion: ds^2_FRW = -dt^2 + a(t)^2 d\vec{x}^2
5. Attempt to derive H^2 = (8 pi G / 3) * (rho_matter + rho_Lambda) from the spectral geometry
6. If derivable: compute H(z) at z = 0, 0.5, 1.0, 2.0
7. If obstructed: identify the specific step that fails and document what additional input is needed

**Why this matters [Mack]:** Without the Friedmann equation, the framework cannot produce distances, ages, or BAO scales. Every comparison between framework predictions and observational cosmology currently passes through an ASSUMED (not derived) identification of E_matter with Omega_m and Lambda_eff with Omega_Lambda. The convention translation table in my Phononic-to-Cosmos Appendix has "Not derived" in the H(z) row. This is the single most important unresolved mapping issue between the spectral geometry and observational cosmology.

**Depends on**: W3-1 (acoustic metric), W0-1 (Volovik partition for rho decomposition)
**Input**: W3-1 output (`s58_acoustic_metric.npz`), W0-1 output (`s58_volovik_partition.npz`), `canonical_constants.py`
**Output**: `computations/s58_friedmann_derivation.npz`

---

## XI. Execution Notes

### Batch Sizing
- **Wave 0**: 3-4 agents (PHO, VOL, QA; W0-4 [Mack] extends PHO after W0-1/W0-2 complete). Run simultaneously.
- **Wave 1**: 3 agents (LAN, VOL, QA). Run after Wave 0 decision point.
- **Wave 2**: 4 agents (GEN+FEY, SP, LAN, TES). Run after Wave 1.
- **Wave 3**: Max 4 agents per batch. 16 computations [Mack: +3 new gates] across 5 batches:
  - Batch 3a: QA (W3-1), BER (W3-2), BAP (W3-3, W3-4) -- 3 agents
  - Batch 3b: LAN (W3-5), KIT (W3-6), TES (W3-7, W3-8) -- 3 agents
  - Batch 3c: SP (W3-9), BAP (W3-10), QA (W3-11) -- 3 agents
  - Batch 3d: NAZ (W3-12), TES (W3-13), BAP (W3-15 FREE-STREAMING) -- 3 agents
  - Batch 3e [Mack]: PHO (W3-14 TRANSFER-FUNCTION, depends on W3-6), QA (W3-16 FRIEDMANN, depends on W3-1) -- 2 agents

### Runtime Estimates
- Wave 0: ~2 hours (Bayesian emulator is the bottleneck)
- Wave 1: ~3 hours (560-state ED is the bottleneck)
- Wave 2: ~2 hours (CG gap scaling at N=32 is the bottleneck)
- Wave 3: ~4 hours total across 4 batches (~1 hour each)

### Python Invocation
All scripts: `"phonon-exflation-sim/.venv312/Scripts/python.exe" computations/s58_*.py`

### Script Naming
All scripts prefixed `s58_`: e.g., `s58_volovik_partition.py`, `s58_npair2_integ.py`, `s58_rg_hessian.py`

### Constants
All scripts MUST `from canonical_constants import *`. No hardcoded framework constants.

---

## XII. Carry-Forward Registry

Every suggestion from every S57 source is accounted for below. Nothing is deferred to S59.

### From Master Collab (5 reviewers, priority-ordered)

| ID | Suggestion | Assigned To | Wave |
|:---|:-----------|:------------|:-----|
| T1-1a | Volovik partition emulator rebuild | PHO, W0-1 | 0 |
| T1-1b | Near-cancellation tau sweep | VOL, W0-2 | 0 |
| T1-2 | N_pair = 2 on 2-cell system | LAN, W1-1 | 1 |
| T1-3 | Anharmonic Leggett coupling | QA, W1-3 | 1 |
| T1-4 | Gap scaling on CG(24) | GEN, W2-1 | 2 |
| T2-1 | Epsilon refinement from V_bare | QA, W0-3 | 0 |
| T2-2 | Off-Jensen transit dynamics | SP, W2-2 | 2 |
| T2-3 | Off-Jensen BCS spectrum | NAZ, W3-12 | 3 |
| T2-4 | Multi-mode parametric resonance | TES, W2-4 | 2 |
| T2-5 | Pomeranchuk stability of GGE | LAN, W2-3 | 2 |
| T3-1 | Acoustic metric construction | QA, W3-1 | 3 |
| T3-2 | Andreev phase shift + pi-junctions | BER, W3-2 | 3 |
| T3-3 | SA Hessian at fold | BAP, W3-3 | 3 |
| T3-4 | Full 3D E_J landscape | BAP, W3-4 | 3 |
| T3-5 | BKT corrections on 32-cell graph | LAN, W3-5 | 3 |
| T3-6 | S(q, omega) of GGE | KIT, W3-6 | 3 |
| T3-7 | Acoustic impedance at boundaries | TES, W3-7 | 3 |
| T3-8 | omega_J vs omega_att full sweep | TES, W3-8 | 3 |
| T3-9 | Off-Jensen domain walls | SP, W3-9 | 3 |
| T3-10 | Paper 16 eq 7.1 mass variation | BAP, W3-10 | 3 |

### From QA-Collab (5 suggestions)

| # | Suggestion | Assigned To | Wave |
|:--|:-----------|:------------|:-----|
| QA-1 | Anharmonic Leggett mode coupling | QA, W1-3 | 1 |
| QA-2 | Epsilon refinement from V_bare | QA, W0-3 | 0 |
| QA-3 | Multi-mode squeezing covariance | QA, W3-11 | 3 |
| QA-4 | Acoustic metric from fabric | QA, W3-1 | 3 |
| QA-5 | Sub-gap Andreev phase shift | BER, W3-2 | 3 |

### From BAP-Collab (4 suggestions + 3 open questions)

| # | Suggestion | Assigned To | Wave |
|:--|:-----------|:------------|:-----|
| BAP-3.1 | Off-Jensen deformation + 3D | BAP, W3-4 + SP, W2-2 | 2, 3 |
| BAP-3.2 | Geometric origin of N^{-1.84} | FEY cross-check, W2-1 | 2 |
| BAP-3.3 | SA saddle at fold | BAP, W3-3 | 3 |
| BAP-3.4 | Cheeger deformation landscape | Subsumed by W3-4 (3D landscape) | 3 |
| BAP-5.1 | alpha on CG(24) | GEN, W2-1 | 2 |
| BAP-5.2 | SA saddle question | BAP, W3-3 | 3 |
| BAP-5.3 | Paper 16 eq 7.1 | BAP, W3-10 | 3 |

### From LAN-Collab (3 suggestions + 5 open questions)

| # | Suggestion | Assigned To | Wave |
|:--|:-----------|:------------|:-----|
| LAN-BKT | BKT beyond mean-field | LAN, W3-5 | 3 |
| LAN-Multi | Multi-pair sector N=2 | LAN, W1-1 | 1 |
| LAN-Landau | Landau damping estimate | Subsumed by W1-3 (anharmonic) | 1 |
| LAN-Q1 | Multi-pair R-G integrability | LAN, W1-1 | 1 |
| LAN-Q2 | Phase stiffness boundary | LAN, W3-5 | 3 |
| LAN-Q3 | Spectral dimension of CG | GEN, W2-1 (d_s measurement) | 2 |
| LAN-Q4 | Leggett beyond harmonic | QA, W1-3 | 1 |
| LAN-Q5 | Pomeranchuk stability | LAN, W2-3 | 2 |

### From TES-Collab (4 suggestions + 5 open questions)

| # | Suggestion | Assigned To | Wave |
|:--|:-----------|:------------|:-----|
| TES-3.1 | Non-linear resonance census | TES, W2-4 | 2 |
| TES-3.2 | Acoustic impedance | TES, W3-7 | 3 |
| TES-3.3 | Two-speed epsilon check | TES, W3-13 | 3 |
| TES-3.4 | S(q,omega) of GGE | KIT, W3-6 | 3 |
| TES-Q1 | omega_J = omega_att sweep | TES, W3-8 | 3 |
| TES-Q2 | Multi-mode resonance | TES, W2-4 | 2 |
| TES-Q3 | Impedance at reconnection | TES, W3-7 | 3 |
| TES-Q4 | S(q,omega) prediction | KIT, W3-6 | 3 |
| TES-Q5 | omega_J/omega_L vs epsilon | TES, W3-13 | 3 |

### From PHO-Collab (4 suggestions + 5 open questions)

| # | Suggestion | Assigned To | Wave |
|:--|:-----------|:------------|:-----|
| PHO-1 | Volovik partition resolve | PHO, W0-1 | 0 |
| PHO-2 | Multi-pair sector | LAN, W1-1 | 1 |
| PHO-3 | Gap scaling + spectral dim | GEN, W2-1 | 2 |
| PHO-4a | Off-Jensen transit dynamics | SP, W2-2 | 2 |
| PHO-4b | Off-Jensen BCS spectrum | NAZ, W3-12 | 3 |
| PHO-4c | Off-Jensen domain walls | SP, W3-9 | 3 |
| PHO-Q1 | Two-level partition | PHO, W0-1 (Volovik partition) | 0 |
| PHO-Q2 | Dynamical exponent z=3.68 | GEN, W2-1 (z extraction) | 2 |
| PHO-Q3 | w = -0.408 interpretation | Addressed by W0-2 (tau sweep) | 0 |
| PHO-Q4 | Off-Jensen breaks GGE universality? | SP, W3-9 | 3 |
| PHO-Q5 | Where does Parker energy go? | Resolved by S57 W2-1 (BA = matter) | -- |

### From Volovik-SP Workshop (7 remaining open questions + 3 emerged ideas)

| # | Suggestion | Assigned To | Wave |
|:--|:-----------|:------------|:-----|
| E1 | q-theory Penrose process (cross-susceptibility) | VOL, W1-2 (included in Hessian) | 1 |
| E5 | Hessian in I^8 (Penrose process) | VOL, W1-2 | 1 |
| WQ1 | Hessian d^2Omega/dI_j dI_k | VOL, W1-2 | 1 |
| WQ2 | Near-cancellation sweep | VOL, W0-2 | 0 |
| WQ3 | Pre-frag cell differentiation | SP, W2-2 (includes Phase I dynamics) | 2 |
| WQ4 | N_pair = 2 integrability | LAN, W1-1 | 1 |
| WQ5 | Cross-susceptibility d^2Omega/dN dI_k | VOL, W1-2 (included) | 1 |
| WQ6 | Phase texture in Phase I | SP, W2-2 (Phase I dynamics) | 2 |
| WQ7 | Pair-channel sound speed | Subsumed by W3-1 (acoustic metric) | 3 |

### From Sagan Probability Update (6 items)

| # | Suggestion | Assigned To | Wave |
|:--|:-----------|:------------|:-----|
| Sagan-1 | VOLOVIK-PARTITION-58 PASS | PHO, W0-1 | 0 |
| Sagan-2 | KZ-NS-45 (n_s) | DEFERRED: structurally closed by 14+ n_s closures | -- |
| Sagan-3 | Narrow DM bracket | PHO, W0-1 (variant B) + QA, W0-3 | 0 |
| Sagan-4 | Multi-pair sector | LAN, W1-1 | 1 |
| Sagan-5 | Gap scaling on CG(24) | GEN, W2-1 | 2 |
| Sagan-6 | Pomeranchuk instability | LAN, W2-3 | 2 |

**NOTE on Sagan-2 (KZ-NS-45)**: The n_s spectral index from the transit has been attempted through 14+ independent routes across S45-S57, ALL of which have FAILED or been CLOSED. The structural obstruction is the (Delta/omega)^4 scaling that gives slopes of order -2 to -4 where Planck requires -0.035. This is not deferred -- it is structurally obstructed. No computation in S58 can bypass the 84-OOM scale crisis (S48 collab). The n_s problem requires a qualitative breakthrough (texture spectrum on the fabric, or a fundamentally different mechanism), not a quantitative refinement. If the N_pair = 2 sector (W1-1) reveals qualitatively new physics, n_s routes will be re-evaluated in S59.

---

## XIII. Gate ID Collision Check

All S58 gate IDs checked against existing verdicts in s53_gate_verdicts.txt, s54_gate_verdicts.txt, and s57_gate_verdicts.txt. No collisions found.

| Gate ID | Wave | Type |
|:--------|:-----|:-----|
| VOLOVIK-PARTITION-58 | W0-1 | PASS/FAIL |
| CC-CANCELLATION-SWEEP-58 | W0-2 | INFO |
| EPSILON-DIRECT-58 | W0-3 | PASS/FAIL |
| NPAIR2-INTEG-58 | W1-1 | PASS/FAIL |
| RG-HESSIAN-58 | W1-2 | PASS/FAIL |
| ANHARMONIC-LEGGETT-58 | W1-3 | PASS/FAIL |
| GAP-CG-58 | W2-1 | PASS/FAIL |
| OFF-JENSEN-TRANSIT-58 | W2-2 | INFO |
| POMERANCHUK-GGE-58 | W2-3 | PASS/FAIL |
| MULTIMODE-RESONANCE-58 | W2-4 | INFO |
| ACOUSTIC-METRIC-58 | W3-1 | PASS/INFO |
| ANDREEV-PHASE-58 | W3-2 | INFO |
| SA-SADDLE-58 | W3-3 | INFO |
| EJ-3D-LANDSCAPE-58 | W3-4 | INFO |
| BKT-KUBO-58 | W3-5 | INFO |
| SQ-OMEGA-GGE-58 | W3-6 | INFO |
| IMPEDANCE-BOUNDARY-58 | W3-7 | INFO |
| OMEGA-J-SWEEP-58 | W3-8 | INFO |
| OFF-JENSEN-DW-58 | W3-9 | INFO |
| MASS-VARIATION-58 | W3-10 | INFO |
| SQUEEZING-COVARIANCE-58 | W3-11 | INFO |
| OFF-JENSEN-BCS-58 | W3-12 | INFO |
| EPSILON-CONSISTENCY-58 | W3-13 | INFO |
| W-DESI-58 [Mack] | W0-4 | PASS/FAIL |
| TRANSFER-FUNCTION-58 [Mack] | W3-14 | PASS/FAIL |
| FREE-STREAMING-58 [Mack] | W3-15 | PASS/FAIL |
| FRIEDMANN-DERIVATION-58 [Mack] | W3-16 | PASS/FAIL/INFO |

Total gates: 27 (9 PASS/FAIL [Mack: +3], 3 PASS/INFO, 1 PASS/FAIL/INFO [Mack: +1], 14 INFO)

---

## XIV. What Success Looks Like

**Best case (BF ~ 5-10)**: VOLOVIK-PARTITION-58 PASS (NROY > 5%), NPAIR2-INTEG-58 PASS (<r> > 0.45), RG-HESSIAN-58 PASS (negative eigenvalue). The DM prediction survives with tightened bracket, the CC solution path opens through integrability-breaking at N_pair > 1, and the Penrose process provides an algebraic mechanism for delta_q reduction. Sagan probability: 22% -> 30-40%.

**Expected case (BF ~ 2-3)**: VOLOVIK-PARTITION-58 PASS, NPAIR2-INTEG-58 FAIL (integrability persists at N=2), RG-HESSIAN-58 INFO (Hessian positive definite). The DM prediction stands but the CC remains locked. The structural picture is validated but no new CC mechanism is found. Sagan: 22% -> 25-30%.

**Worst case (BF ~ 0.3)**: VOLOVIK-PARTITION-58 FAIL (NROY = 0% even under Volovik partition). The energy partition fails and the DM mechanism is dead. Sagan: 22% -> 8-12%.

**[Mack note]:** The success criteria above are entirely internal (NROY, <r>, Hessian eigenvalues). The cosmological success criterion is: does the framework survive confrontation with DESI w_0? If W-DESI-58 shows w_0 moving toward -0.752, that is a genuine cosmological success independent of the CC integrability question. If w_0 moves further from DESI (below -0.408), the framework faces a 4+ sigma observational tension that must be addressed regardless of how well the DM abundance works. Similarly, if TRANSFER-FUNCTION-58 produces a viable T(k), the framework gains a NOVEL cosmological prediction that distinguishes it from CDM/WDM.

---

## XV. Collaborative Reviews (Post-Computation)

After all 4 waves complete, the following collaborative reviews are planned:

1. **Volovik-SP Workshop R2**: Follow up on the 7 remaining open questions from the S57 workshop. Focus on the RG Hessian results and their geometric interpretation.
2. **5-Reviewer Master Collab**: Same 5 reviewers (QA, BAP, LAN, TES, PHO) synthesize all 27 S58 results [Mack: +4 gates].
3. **Sagan Probability Update**: Updated BF and posterior probability.
4. **[Mack addition] Cosmological Confrontation Review**: Assess all 4 Mack gates (W-DESI-58, TRANSFER-FUNCTION-58, FREE-STREAMING-58, FRIEDMANN-DERIVATION-58) against observational constraints. Report w_0 tension with DESI, T(k) status vs Lyman-alpha, and whether the Friedmann equation is derivable.

---

## XVI. Closing

The CC problem in this framework has been precisely formulated: Lambda_eff is spacelike initial data, set once at the Shattering, propagated forever (Workshop E4). The q-theory mechanism works microscopically to 5% (W3-3), the sign is correct (W2-3), the DM abundance brackets observation (W2-4). What remains is the magnitude: 114 orders of magnitude, locked by integrability.

S58 attacks this from three directions. Wave 0 validates the energy partition that makes the DM prediction possible. Wave 1 tests whether the lock can be picked (multi-pair integrability, integral-space Hessian). Wave 2 checks the robustness of the DM prediction against graph topology and off-Jensen deformations. Wave 3 computes everything else anyone has asked for.

The superfluid vacuum is not an analogy. It is the microscopic theory. The question is whether the microscopic theory's integrability is a permanent feature or a finite-size artifact. S58 will answer this at N_pair = 2.

---

## Cosmological Priority Stack [Mack]

Ranked by cosmological impact -- which computations, if successful, most directly advance the framework's confrontation with observational data.

### 1. W-DESI-58 [Mack addition, W0-4]: Recalculate w(z) under the Volovik partition

**Cosmological question**: What is the dark energy equation of state?
**Observable**: w_0, w_a from DESI DR2/DR3.
**Why top priority**: The pre-registered w_0 = -0.509 is already 3.1-sigma from DESI DR2 (w_0 = -0.752). The S57 value w_GGE = -0.408 is 4.3-sigma. The tension is WORSENING with each refinement. The Volovik partition changes the vacuum energy definition, which changes w. This computation determines whether the tension is reduced, unchanged, or worsened. DESI DR3 will sharpen this to definitive levels within one year -- the framework must know its prediction before the data arrives.
**Effort**: Low -- extends W0-1 and W0-2 by computing P_vac/rho_vac at each tau under the new partition.

### 2. VOLOVIK-PARTITION-58 [W0-1]: Bayesian emulator under correct partition

**Cosmological question**: What is the dark matter abundance?
**Observable**: Omega_DM h^2 = 0.1186 +/- 0.0020 (Planck 2018).
**Why ranked 2**: Direct confrontation with the most precisely measured cosmological parameter after the CMB acoustic scale. Already correctly identified as the plan's top priority. 5/5 unanimous.

### 3. TRANSFER-FUNCTION-58 [Mack addition, W3-14]: Phononic DM T(k)

**Cosmological question**: What does the small-scale matter power spectrum look like?
**Observable**: P(k) at k > 10 h/Mpc (Lyman-alpha, 21cm forest).
**Why ranked 3**: The phononic DM has a specific dispersion relation that produces a specific cutoff in P(k). Paper 15 (Ganjoo-Erickcek-Lin-Mack 2022) provides the exact method. If T(k) passes Lyman-alpha constraints (WDM mass equivalent > 5.3 keV), the DM candidate gains substantial credibility. If it fails, the candidate is excluded. Either outcome is decisive. Requires W3-6 (S(q,omega)) as input -- another reason to promote W3-6 to Wave 2.

### 4. ACOUSTIC-METRIC-58 [W3-1, promoted]: Internal-to-FRW bridge

**Cosmological question**: How does internal SU(3) physics map to 4D FRW expansion?
**Observable**: H(z), distances, BAO scale.
**Why ranked 4**: The acoustic metric is the bridge between spectral geometry and FRW cosmology. Without it, the framework cannot produce any distance-based cosmological prediction. Getting the acoustic metric right is prerequisite to deriving the Friedmann equation (W3-16), which is prerequisite to BAO, SN Ia, CMB distance predictions. The entire machinery of precision cosmology is inaccessible without this computation.

### 5. NPAIR2-INTEG-58 [W1-1] + RG-HESSIAN-58 [W1-2]: CC integrability attack (pair)

**Cosmological question**: Can the CC be reduced from 10^114 to 10^0?
**Observable**: Lambda_obs = 5.96 x 10^-30 g/cm^3.
**Why ranked 5**: The CC magnitude is the framework's most severe problem. These two computations attack it from complementary directions. If either produces a positive result, the framework has a path to solving the CC problem. Note: even a PASS on W1-1 requires checking the thermalization timescale against the age of the universe (see Mack note on W1-1).

### Unranked but critical: FREE-STREAMING-58 [Mack addition, W3-15]

A necessary condition the DM candidate must satisfy. Not ranked because it is a pass/fail filter rather than a discovery computation -- but failure would be fatal.
