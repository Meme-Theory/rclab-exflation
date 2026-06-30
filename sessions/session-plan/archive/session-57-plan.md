# Session 57 Plan: The Shattering -- Dark Matter, Dark Energy, and the Leggett Partition

**Date**: 2026-03-22
**Author**: Gen-Physicist (planner)
**Format**: Parallel single-agent computations across 4 waves
**Source**: S56 results (20 computations, 4 workshops, 8 collaborative reviews, 3 targeted reviews, DM synthesis), S55 framework update
**Motivation**: S56 closed static fabric stabilization (47th closure) and discovered the two-speed hierarchy: Josephson channel (gap 13.04 M_KK, adiabatic) vs Leggett channel (gap 0.07-0.14 M_KK, diabatic). The DM synthesis identifies a single testable claim: the 70/30 Omega_Lambda/Omega_DM split is channel-selective adiabaticity at the BCS freeze. The Leggett channel SHATTERS (produces DM quasiparticles). The Josephson channel HUMS (produces CC). The ratio is geometric: set by epsilon = 0.00248 from SU(3)/U(2).
**Results file**: `sessions/archive/session-57/session-57-results-workingpaper.md`

---

## I. Session Objective

Test whether channel-selective adiabaticity during the BCS freeze produces a DM/CC partition consistent with Omega_DM/Omega_Lambda = 0.43.

**CC is gravity sans mass -- infinitely weaker at mass scales, but universally pervasive enough to matter.** The CC is the energy cost of PREVENTING the universe from re-condensing. Integrability is the lock. The hum is the vibration of a system that wants to pair but cannot. The Leggett channel shatters (produces DM). The Josephson channel hums (produces CC). Same instanton gas, two fates.

**Pre-registered master gate**:

- **THE-SHATTERING-57**: Does channel-selective adiabaticity at the BCS freeze produce a DM/CC partition consistent with Omega_DM/Omega_Lambda = 0.43?
- **PASS**: P_exc^Leggett in [0.15, 0.45] AND channel decomposition shows Leggett-dominant matter production
- **FAIL**: P_exc^Leggett < 0.05 (adiabatic protection kills DM) OR P_exc^Leggett > 0.80 (no CC)
- **INFO**: P_exc^Leggett in [0.05, 0.15] or [0.45, 0.80] (intermediate, needs refinement)

**Secondary gates** (see individual computations):
- GAP-SCALING-57: Does Delta_N decrease or saturate with N? (resolves 260-OOM ambiguity)
- ANDREEV-INTEG-57: Does anisotropic quasiparticle tunneling break integrability?
- FINITE-RATE-TRANSIT-57: Does the physical finite-rate transit produce P_exc > 0.1?

---

## II. The Central Physics

### The Two-Channel Partition

The instanton gas at the BCS freeze partitions into two fractions through channel-selective adiabaticity:

| Channel | Gap (M_KK) | Adiabaticity | Fate | Cosmological role |
|:--------|:-----------|:-------------|:-----|:-----------------|
| Josephson (overall phase) | 13.04 | H/Delta_J = 0.28 (adiabatic) | Stays as vacuum noise | Cosmological constant (~70%) |
| Leggett (relative B2/B1) | 0.070-0.138 | H/Delta_L = 27-53 (diabatic) | Shatters into quasiparticles | Dark matter (~30%) |

The ratio is set by epsilon = Delta_L / Delta_J ~ 0.005-0.011, a geometric property of SU(3)/U(2) under Jensen deformation. Neither gap is a free parameter.

### The 700x Problem and Its Resolution

Cosmic-Web computed (S56 CW review): P_exc = 6.6e-4 on 2 cells gives Omega_Lambda/Omega_M = 1515. The observed ratio is 2.17. Off by 700x.

The resolution (DM synthesis, Section III): P_exc does not map to TOTAL matter. It maps to DARK matter. Baryonic matter (5% of the energy budget) comes from standard baryogenesis. The framework explains the DM/Lambda partition: why 70% is dark energy and 30% is dark matter. The GGE quasiparticles are CPT-neutral (BDI, T^2 = +1), non-annihilating (self-conjugate), collisionless (sigma/m = 5.7e-51 cm^2/g), and integrability-protected (8 Richardson-Gaudin conserved quantities).

The critical question: does the Leggett channel carry ~30% of the total instanton gas energy into quasiparticle excitations? The 2-cell sudden-quench value P_exc = 6.6e-4 is the TOTAL excitation. The channel decomposition into Josephson/BCS/Leggett has not been computed. FINITE-RATE-TRANSIT-57 observable #4 will provide P_exc^Leggett separately.

### Nuclear Fission Analog (Naz, Workshop 3)

The partition maps precisely onto nuclear fission of ^236U:

| Nuclear fission | Fabric transit |
|:---------------|:---------------|
| Center-of-mass separation (slow, adiabatic) | Josephson overall phase (gap 13.04, adiabatic) |
| Neck rupture (fast, diabatic) | Leggett relative B2/B1 amplitude (gap 0.07-0.14, diabatic) |
| Coulomb TKE (~170 MeV, smooth) | Josephson vacuum energy (self-tuned to zero, W2-2) |
| Fragment excitation (~15 MeV, quasiparticle) | GGE quasiparticle relic (dark matter) |

In nuclear fission, TXE/Q ~ 12.5%. The framework needs ~30%. Same order of magnitude, 2.4x larger.

### Input Data (all existing .npz)

| File | Contents | Source |
|:-----|:---------|:-------|
| `s54_tb_hamiltonian.npz` | 50 tau values, 32 TB eigenvalues | S54 |
| `s54_ed_sweep.npz` | Pairing matrix V_kl at each tau | S54 |
| `s54_scale_factor.npz` | H(tau) at 10 points | S54 |
| `s56_ba_spectrum.npz` | 31 BA phonon frequencies at 50 tau | S56 W0-1 |
| `s56_leggett_fabric.npz` | Leggett gap omega_L0(tau), dispersions | S56 W2-4 |
| `s56_fabric_integ.npz` | <r> values, E_J sweep, anisotropy controls | S56 W1-2 |
| `s56_gge_fabric.npz` | 2-cell P_exc = 6.6e-4, gap 13.04 M_KK | S56 W3-6 |
| `s56_npair3_ed.npz` | N_pair=3 level statistics | S56 W1-3 |
| `s56_cba_sound.npz` | c_BA, c_L velocities at 50 tau | S56 W0-3 |
| `s56_post_transit_coh.npz` | E_J/H ratio across transit | S56 W3-2 |
| `s56_strutinsky_fabric.npz` | R=0.051 Strutinsky ratio | S56 W2-3 |
| `s56_mu_josephson.npz` | mu_eff = -0.201 M_KK | S56 W1-4 |
| `s55_transit_velocity.npz` | Transit velocity profile | S55 |
| `s55_npair2_ed.npz` | N_pair=2 reference level statistics | S55 |

---

## III. Wave Structure

### Dependency Graph

```
Wave 0 (ZERO-COST, from existing S56 data, ~20 min):
  W0-1: LEGGETT-TAU-PROFILE-57     W0-2: CHANNEL-ENERGY-BUDGET-57
  W0-3: GGE-EQUILIBRIUM-GAP-57     W0-4: ANDREEV-ANISOTROPY-EST-57

  ---- Decision Point 0: Is the Leggett gap profile non-trivial? ----
  ---- Is the channel energy budget consistent with 30% in Leggett? ----
  ---- What is ||n^GGE - n^eq||? ----

Wave 1 (THE DECISIVE COMPUTATIONS, parallel, ~2 hrs):
  W1-1: FINITE-RATE-TRANSIT-57     W1-2: LEGGETT-PARTITION-57
  W1-3: GAP-SCALING-57             W1-4: ANDREEV-INTEG-57

  ---- Decision Point 1: THE SHATTERING FORK ----
  ---- If W1-2 PASS: DM/CC partition confirmed ----
  ---- If W1-2 FAIL + W1-1 PASS: Leggett channel active but wrong fraction ----
  ---- If both FAIL: DM mechanism dead ----

Wave 2 (FOLLOW-UPS, conditional on W1):
  W2-1: PARKER-BA-57               W2-2: DESERT-DYNAMICS-57
  W2-3: CC-SIGN-57                 W2-4: FABRIC-DM-ABUNDANCE-57

  ---- Decision Point 2: Does the CC have the right sign? ----
  ---- Does the DM abundance match Omega_DM h^2 = 0.120? ----

Wave 3 (CATCH-ALL -- EVERY remaining suggestion from ALL sources):
  W3-1: FLOQUET-PLASMA-57          W3-2: PERCOLATION-CC-57
  W3-3: CHI-Q-MICROSCOPIC-57       W3-4: OFF-JENSEN-EJ-57
  W3-5: BAYESIAN-FABRIC-57         W3-6: DOMAIN-WALL-57
  W3-7: FABRIC-KZ-QUENCH-57        W3-8: NS-MAPPING-57
  W3-9: SUB-GAP-PARTITION-57       W3-10: STUCKELBERG-DM-57
  W3-11: OMEGA-L-TAU-SWEEP-57      W3-12: PHASE-DIAGRAM-57
  W3-13: TOPOLOGY-TRANSITION-57
```

### Agent Roster

ALL physics agents use **opus**. Max 3-4 agents per parallel batch.

| Agent | Waves | Specialty | Source of assignment |
|:------|:------|:----------|:-------------------|
| `nazarewicz-nuclear-structure-theorist` | W0-1, W1-1, W2-4 | TDHFB, fission dissipation, finite-rate transit | Workshop 3 N5 |
| `quantum-acoustics-theorist` | W0-2, W1-2, W3-11 | Leggett channel, two-speed hierarchy | Workshop 3 QA, S56-qa-collab |
| `volovik-superfluid-universe-theorist` | W0-3, W2-3, W3-6 | GGE equilibrium, q-theory, CC formula | Workshop 2 V5, S56-vol-collab |
| `kitaev-quantum-chaos-theorist` | W0-4, W1-4, W3-7 | Integrability, OTOC, Andreev tunneling | Workshop 1 S5, S56-kitaev-collab |
| `gen-physicist` | W1-3, W3-3 | Gap scaling, chi_q microscopic | Workshop 2 G3 |
| `landau-condensed-matter-theorist` | W2-1, W3-12 | Parker mechanism, phase diagram | S56-landau-collab |
| `schwarzschild-penrose-geometer` | W2-2, W3-2 | Desert dynamics, percolation | Workshop 1 S4-S5 |
| `neutrino-detection-specialist` | W3-8 | Transfer function, KK-to-cosmological scales | Workshop 4 P5 |
| `tesla-resonance` | W3-1, W3-9 | Floquet stability, Mattis-Bardeen sub-gap | S56-tesla-collab (5th carry-forward) |
| `einstein-theorist` | W3-2 (co-assigned) | Percolation threshold on CG graph | Workshop 2 V5 |
| `little-red-dots-jwst-analyst` | W2-4 (co-assigned) | DM abundance observational check | Workshop 4 P3 |
| `kaku-speculative-theorist` | W3-10 | Stuckelberg oscillation DM channel | Workshop 4 cross-synthesis |
| `phonon-first-cosmologist` | W3-4, W3-5 | Bayesian fabric, off-Jensen E_J | S56-naz-collab |
| `feynman-theorist` | W1-1 (cross-check) | Overlap deficit verification | Workshop 1 S4.1 |
| `berry-geometric-phase-theorist` | W3-13 | Topology transition, Z_2 invariant | S56-qa-collab Comp 5 |

---

## IV. Wave 0: Zero-Cost Diagnostics (from existing S56 data)

All Wave 0 computations use ONLY existing .npz files. No new spectrum computations.

---

### W0-1: LEGGETT-TAU-PROFILE-57 -- Leggett Gap Profile Along Transit

**Agent**: `nazarewicz-nuclear-structure-theorist` | **Model**: opus
**Gate**: INFO -- characterize omega_L0(tau) profile for use in W1

**Method**: Extract the Leggett gap omega_L0(tau) from `s56_leggett_fabric.npz` and `s54_tb_hamiltonian.npz`. The Leggett gap formula is:

    omega_L0(tau) = sqrt(2 * epsilon * E_J(tau) * Delta_B2(tau) * Delta_B1(tau) / (Delta_B2(tau) + Delta_B1(tau)))

with epsilon = 0.00248 (S49, dipolar coupling). Compute omega_L0 at all 50 tau values. Identify:
1. Global minimum of omega_L0(tau) and its location tau_*
2. d(omega_L0)/dtau at each tau -- needed for LZ formula
3. The "scission point" where omega_L0(tau)/H(tau) is minimal (QA Workshop 3 Q2)
4. Whether omega_L0 has a non-monotonic profile (Naz Workshop 3 Q1a concern)

**Input**: `s56_leggett_fabric.npz`, `s54_tb_hamiltonian.npz`, `s54_scale_factor.npz`, `canonical_constants.py`
**Output**: `computations/s57_leggett_tau_profile.npz`, `computations/s57_leggett_tau_profile.png`

**Deliverables for W1**: tau-resolved omega_L0, d(omega_L0)/dtau, omega_L0/H ratio -- all needed by FINITE-RATE-TRANSIT-57 and LEGGETT-PARTITION-57.

---

### W0-2: CHANNEL-ENERGY-BUDGET-57 -- Energy Decomposition from W1-1 Data

**Agent**: `quantum-acoustics-theorist` | **Model**: opus
**Gate**: INFO -- decompose the 2-cell energy into Josephson, BCS, and Leggett contributions

**Method**: Using the 2-cell Hamiltonian decomposition from `s56_gge_fabric.npz`:
1. Total Josephson energy: E_J_total = Sum_{bonds} E_J(tau) * <cos(phi_i - phi_j)>
2. Intra-cell BCS condensation energy: E_BCS = Sum_cells E_cond(tau) per cell
3. Leggett relative-phase energy: E_L = epsilon * E_J * (Delta_B2 * Delta_B1)/(Delta_B2 + Delta_B1) * <cos(phi_B2 - phi_B1)>
4. Compute the energy fractions E_J/E_total, E_BCS/E_total, E_L/E_total at the fold

The question: does the Leggett channel carry a non-negligible fraction of the total energy budget? If E_L/E_total << 0.01, the DM mechanism is energetically impossible regardless of P_LZ.

**Input**: `s56_gge_fabric.npz`, `s56_leggett_fabric.npz`, `s56_ba_spectrum.npz`, `canonical_constants.py`
**Output**: `computations/s57_channel_energy_budget.npz`

---

### W0-3: GGE-EQUILIBRIUM-GAP-57 -- Distance from Equilibrium

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus
**Gate**: GGE-EQUILIBRIUM-GAP-57
- **PASS**: ||n^GGE - n^eq|| / N_pair < 10^{-57} (CC gap closeable by thermalization alone)
- **FAIL**: ||n^GGE - n^eq|| / N_pair ~ O(1) (CC gap structural)

**Method**: From S38/S55 data (8 GGE temperatures: 1.459, 2.771, 6.007 for B2, B1, B3):
1. Compute n_k^{GGE} at each of the 8 modes from the GGE Lagrange multipliers
2. Compute the thermal equilibrium distribution n_k^{eq} = 1/(exp(epsilon_k/T_eq) + 1) at the single temperature T_eq that minimizes ||n^GGE - n^eq||
3. Compute ||n^GGE - n^eq|| in L2 norm
4. Report Lambda_eff from Volovik's formula (Workshop 2, V3):
   Lambda_eff = (1/V_eff) * Sum_k [n_k^GGE - n_k^eq] * [epsilon_k - T_eq * (ds/dn)_k]

Volovik's pre-assessment: ||n^GGE - n^eq|| is O(1) because the 8 temperatures span a factor 3.75. This computation confirms arithmetically. Source: Workshop 2, V5 Computation 1.

**Input**: S38 GGE data (from session files), `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s57_gge_equilibrium_gap.npz`

---

### W0-4: ANDREEV-ANISOTROPY-EST-57 -- Anisotropy from BCS Coherence Factors

**Agent**: `kitaev-quantum-chaos-theorist` | **Model**: opus
**Gate**: INFO -- characterize the mode-dependent Andreev coupling t_k for use in W1-4

**Method**: Compute the quasiparticle tunneling amplitude t_k = J_C2(tau) * (u_k^2 - v_k^2) at the fold for all 8 BCS-active modes. From `s56_fabric_integ.npz` (W1-2 data):
1. Extract the BCS coherence factors u_k, v_k at the fold
2. Compute t_k for each mode
3. Compute the anisotropy parameter epsilon_A = std(t_k)/mean(t_k) (estimated at ~7% in Workshop 1, K1)
4. Compare the physical t_k structure to the random-anisotropy control from W1-2 (<r> = 0.446)
5. Estimate: if epsilon_A < 0.07, the physical Andreev channel is LESS chaotic than the control

**Input**: `s56_fabric_integ.npz`, `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s57_andreev_anisotropy.npz`

---

## V. Decision Point 0

Read W0-1 through W0-4. Four questions:

1. **Is omega_L0(tau) non-monotonic?** If yes, identify the minimum. If omega_L0 has a minimum tau_* where d(omega_L0)/dtau = 0, the adiabaticity parameter is larger there (LZ applies at tau_* with modified rate). This affects LEGGETT-PARTITION-57 design.

2. **Is E_L/E_total consistent with ~30%?** If E_L/E_total < 0.001, the Leggett channel is energetically negligible. The DM mechanism requires either (a) a different energy counting (probability vs energy fraction -- DM synthesis Section III), or (b) the 2-cell decomposition misses multi-cell amplification.

3. **Is ||n^GGE - n^eq|| = O(1)?** Confirms the CC gap is structural (Volovik's pre-assessment). The computation makes this arithmetic, not estimate.

4. **Is epsilon_A < 0.07 (physical) or > 0.07?** Determines whether ANDREEV-INTEG-57 needs full OTOC or whether perturbative estimate suffices.

Proceed to W1 regardless. W0 results inform W1 computation parameters but do not gate W1 execution.

---

## VI. Wave 1: The Decisive Computations

### W1-1: FINITE-RATE-TRANSIT-57 -- Exact Time Evolution of 2-Cell Fabric

**Agent**: `nazarewicz-nuclear-structure-theorist` | **Model**: opus
**Cross-check agent**: `feynman-theorist` (overlap deficit verification, Workshop 1 S4.1)
**Gate**: FINITE-RATE-TRANSIT-57
- **PASS**: P_exc(tau_final) > 0.1 at physical transit rate. Sufficient excitation for non-trivial GGE.
- **FAIL**: P_exc(tau_final) < 0.01. Adiabatic protection survives at finite rate.
- **INFO**: 0.01 < P_exc < 0.1. Partial excitation; channel decomposition decisive.

**This is THE computation of S57.** Naz specified it fully in Workshop 3, N5. The 120x120 Hamiltonian at each tau step, evolved by 4th-order Runge-Kutta with adaptive step size.

**Physical setup**: 2-cell Josephson array. Each cell has 8 BCS-active modes with single-particle energies epsilon_k(tau) from Jensen-deformed SU(3). Inter-cell coupling H_J = -(E_J/2) * (B_1^dag B_2 + h.c.). Collective coordinate tau sweeps from tau_i to tau_f at rate dtau/dt = H(tau)/M_KK from S54 scale factor data.

**Method**: Time-dependent BdG (nuclear TDHFB adapted to the framework).

    i * d|Psi>/dt = H(tau(t)) * |Psi>

with H = H_BCS^{(1)} + H_BCS^{(2)} + H_J(tau), initial condition |Psi(0)> = |GS(tau_i)>.

For 2-cell at N_pair = 1: dim = C(16,2) = 120. Estimated runtime: ~1.2 seconds (120,000 matrix operations at ~10 us per 120x120 diag).

**Output observables** (at each tau along the transit):
1. P_exc(tau) = 1 - |<GS(tau)|Psi(tau)>|^2 (total excitation probability)
2. E_exc(tau) = <Psi|H(tau)|Psi> - E_GS(tau) (excitation energy)
3. S_DE(tau) = -Sum |c_n|^2 ln|c_n|^2 (diagonal ensemble entropy)
4. **Channel decomposition**: project P_exc onto (a) Josephson bonding/antibonding, (b) intra-cell BCS quasiparticles, (c) Leggett relative phase (THE observable for THE-SHATTERING-57)
5. n_k(tau) for each mode
6. delta_P_vac = P_vac(fabric, t_final) - P_vac(ground state) (CC contribution)

**Pre-registered limiting cases** (benchmarks):
1. dtau/dt -> 0 (adiabatic limit): P_exc -> 0
2. dtau/dt -> infinity (sudden quench): P_exc -> 6.6e-4 (matches W3-6)
3. E_J -> 0 (isolated cells): P_exc -> 1.000 per cell (matches S38)
4. Leggett gap -> 0: P_exc^Leggett -> 1.000 (complete Leggett excitation)

**CPT constraint** (Dirac, Workshop 3): verify ||JU - UJ|| < 10^{-10} at each time step.
**Foam constraint** (W-FOAM-10): compute P_exc AND <cos(phi)> simultaneously.
**Desert test** (CW): track E_J_GGE(tau)/H(tau) during evolution.

**Sub-computations** (outputs of the same time evolution):
- **LEGGETT-LZ-57**: LZ at each mode's omega_L(n,tau) minimum. Compare to full TD result. Gate: P_LZ^Leggett > 0.5.
- **CHANNEL-DECOMP-57**: Project final state onto P_J, P_BCS, P_L. Report energy and entropy in each channel.
- **RATE-SCAN-57**: Scan transit rate from 0.01*H to 100*H. Map P_exc vs rate. Identify critical rate.

**Input**: `s54_tb_hamiltonian.npz`, `s54_ed_sweep.npz`, `s54_scale_factor.npz`, W0-1 output (omega_L0(tau) profile), `canonical_constants.py`
**Output**: `computations/s57_finite_rate_transit.npz`, `computations/s57_finite_rate_transit.png`

---

### W1-2: LEGGETT-PARTITION-57 -- The DM/CC Energy Fraction

**Agent**: `quantum-acoustics-theorist` | **Model**: opus
**Gate**: LEGGETT-PARTITION-57 (= THE-SHATTERING-57 sub-gate)
- **PASS**: P_exc^Leggett in [0.15, 0.45] (consistent with Omega_DM = 0.25-0.35)
- **FAIL**: P_exc^Leggett < 0.05 (DM mechanism dead) OR P_exc^Leggett > 0.80 (no CC)
- **INFO**: P_exc^Leggett in [0.05, 0.15] or [0.45, 0.80]

**Method**: This computation uses the FINITE-RATE-TRANSIT-57 output (W1-1 channel decomposition, observable #4) to extract P_exc^Leggett specifically. If W1-1 is still running, compute independently using the Leggett-mode-only approximation:

1. Construct the Leggett subspace: the 31 Leggett modes with omega_L(n,tau) from W0-1 and `s56_leggett_fabric.npz`
2. For each mode n with omega_L(n) < 0.15 M_KK (QA estimate: 5-10 of the lowest 31 modes), apply the LZ formula:
   P_LZ(n) = exp(-pi * omega_L(n)^2 / (2 * |d(omega_L(n))/dt|))
3. Compute the energy deposited per mode: E_n = P_LZ(n) * omega_L(n)/2
4. Total Leggett excitation energy: E_L = Sum_n E_n
5. Total instanton gas energy: E_total = P_vac * M_KK^4 (from `s56_pvac_fabric.npz`)
6. P_exc^Leggett = E_L / E_total

**The distinction between energy fraction and excitation probability** (DM synthesis, Section III): If Omega_DM is proportional to the PROBABILITY of mode excitation (number of shattered modes), the Leggett channel provides ~30% because most low modes are diabatic. If Omega_DM is proportional to ENERGY, then 0.1% may be too small. This computation resolves which mapping applies.

**Input**: W0-1 output, `s56_leggett_fabric.npz`, `s56_pvac_fabric.npz`, `s54_scale_factor.npz`, `canonical_constants.py`
**Output**: `computations/s57_leggett_partition.npz`, `computations/s57_leggett_partition.png`

---

### W1-3: GAP-SCALING-57 -- Many-Body Gap for N = 2, 4, 8 Cells

**Agent**: `gen-physicist` | **Model**: opus
**Gate**: GAP-SCALING-57
- **PASS**: Delta_N decreases with N (alpha < 0 in Delta_N ~ N^alpha). BA phonon gap (0.209 M_KK) controls.
- **FAIL**: Delta_N increases or saturates (alpha >= 0). Adiabatic protection strengthens.
- **INFO**: Non-monotonic or insufficient data points.

**Why decisive**: Resolves the 260-OOM disagreement (Workshop 1, S1.7):
- Hawking: gap ~ N_bonds * E_J -> P_exc(32) ~ 10^{-258}
- Feynman: overlap deficit additive -> P_exc(32) ~ 0.022
- Berry: BA phonon gap controls -> Delta_32 ~ 0.209 M_KK
- SP: desert decouples cells -> P_exc(32) ~ 1.000

**Method**: For N = 2, 4, 8 cells at the fold (tau = 0.194):
1. Construct the N-cell Hamiltonian on a subgraph of the CG(24) graph
2. For N=2: dim = C(16,2) = 120 (existing from W3-6)
3. For N=4: dim = C(32,2) = 496 (exact diag feasible, ~0.5 GB)
4. For N=8: dim = C(64,2) = 2016 (exact diag feasible, GPU-accelerated on RX 9070 XT)
5. Extract the gap Delta_N between ground state and first excited state
6. Fit scaling: Delta_N = A * N^alpha. Report alpha with uncertainty.

Note: At N_pair=1 per 2-cell unit, the Hilbert space dimension is C(8*N, N_pair). For N_pair=1 (the W3-6 protocol): dim(N=2) = 120, dim(N=4) = 496, dim(N=8) = 2016. All feasible for exact diag.

**Also compute**: P_exc(N) = 1 - |<GS_fold(N)|GS_init(N)>|^2 at each N. This gives the gap-scaling-to-P_exc correspondence directly.

**Source**: Workshop 1, Gates 1 (S5); Workshop 2, V5 Computation 3; S56-vol-collab; S56-naz-collab; endorsed by 5/7 S56 reviewers.

**Input**: `s54_tb_hamiltonian.npz`, `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s57_gap_scaling.npz`, `computations/s57_gap_scaling.png`

---

### W1-4: ANDREEV-INTEG-57 -- Explicit Andreev Hamiltonian and Integrability Test

**Agent**: `kitaev-quantum-chaos-theorist` | **Model**: opus
**Gate**: ANDREEV-INTEG-57
- **PASS**: <r> > 0.48 (Andreev channel breaks integrability at fabric level)
- **FAIL**: <r> < 0.40 (BCS coherence factor structure preserves more R-G symmetry than random anisotropy)
- **INFO**: 0.40 < <r> < 0.48

**Method**: Construct the explicit Andreev Hamiltonian:

    H_A = Sum_k t_k * gamma_k^{(1)dag} * gamma_k^{(2)} + h.c.

where t_k = J_C2 * (u_k^2 - v_k^2) from the BCS coherence factors (W0-4 output).

1. Build H_full = H_BCS^{(1)} + H_BCS^{(2)} + H_J(isotropic) + alpha * H_A on the 120-dim Fock space
2. Diagonalize at alpha = 0, 0.1, 0.5, 1.0 (physical), 2.0
3. Compute <r> at each alpha
4. If <r> > 0.45 at alpha = 1.0: compute OTOC C(t) = <[gamma_k^{(1)}(t), gamma_l^{(2)}(0)]^2> to extract lambda_L
5. Test Kitaev's falsification criteria (Workshop 1 K2, pre-registered):
   - K(t,tau) ramp-plateau in SFF at any tau in [0.08, 0.22]?
   - <r> > 0.48 at any tau in [0.08, 0.22]?
   - OTOC lambda_L > 0.1 M_KK?

**Also compute**: ||[H_A, Q_j]|| / ||Q_j|| for the 8 Richardson-Gaudin conserved quantities Q_j (Connes request, Workshop 3 QA Part 3). If > 0.1 for any j, integrability is broken.

**Source**: Workshop 1, Gate 3 (S5); S56-kitaev-collab; S56-vol-collab.

**Input**: `s56_fabric_integ.npz`, W0-4 output, `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s57_andreev_integ.npz`, `computations/s57_andreev_integ.png`

---

## VII. Decision Point 1: THE SHATTERING FORK

Read W1-1 through W1-4. The master gate THE-SHATTERING-57 is evaluated from W1-1 (channel decomposition) and W1-2 (Leggett partition fraction).

**Branch A** -- W1-2 PASS (P_exc^Leggett in [0.15, 0.45]):
- THE-SHATTERING-57 = PASS. The DM/CC partition is confirmed.
- Proceed to W2 with focus on abundance matching (W2-4) and CC sign (W2-3).
- W3 computations test robustness and fill remaining carry-forwards.

**Branch B** -- W1-2 FAIL (P_exc^Leggett < 0.05 or > 0.80) BUT W1-1 PASS (P_exc > 0.1):
- THE-SHATTERING-57 = INFO. Leggett channel active but wrong DM fraction.
- The DM/CC partition requires refinement: either the energy-vs-probability distinction (DM synthesis, Section III) resolves the discrepancy, or a different channel carries the DM.
- Proceed to W2 with modified focus.

**Branch C** -- Both FAIL (P_exc^Leggett < 0.05 AND P_exc < 0.01):
- THE-SHATTERING-57 = FAIL. Adiabatic protection kills DM production on the fabric.
- The DM mechanism is dead. The mathematical theorems (mass ordering, three generations, NNI texture) survive but the cosmological mechanism is closed.
- W2-W3 proceed as post-mortem and carry-forward completion.

**Branch D** -- W1-3 outcome:
- If Delta_N decreases with N: CC hierarchy may emerge from N-scaling. A structural breakthrough.
- If Delta_N saturates: adiabatic protection is fixed, CC problem structural.
- Report alpha and its implications for CC regardless of W1-2 outcome.

---

## VIII. Wave 2: Follow-Up Computations (Conditional on W1)

### W2-1: PARKER-BA-57 -- BA Phonon Mode Equation with Physical Transit Rate

**Agent**: `landau-condensed-matter-theorist` | **Model**: opus
**Gate**: PARKER-BA-57
- **PASS**: <n> > 1 for any BA mode at any tau in [0.10, 0.30]. Dynamic excitation substantial.
- **FAIL**: <n> < 0.01 at all tau. Adiabatic protection wins dynamically.

**Method**: Solve the mode equation for all 31 BA modes:

    d^2(phi_n)/dt^2 + omega_n(t)^2 * phi_n = 0

with omega_n(t) from `s56_ba_spectrum.npz` and transit velocity from `s54_scale_factor.npz`. Compute the Bogoliubov coefficient |beta_n|^2 (particle number per mode).

This is the Parker mechanism applied to the BA phonon spectrum. It does not require crossing a phase boundary and does not require E_J/E_c ~ 1. It operates on the time-dependent frequencies.

**Source**: Workshop 1, Gate 4 (S5); S56-landau-collab (Computation 1).

**Input**: `s56_ba_spectrum.npz`, `s54_scale_factor.npz`, `canonical_constants.py`
**Output**: `computations/s57_parker_ba.npz`

---

### W2-2: DESERT-DYNAMICS-57 -- Time-Dependent Schrodinger Through Coherence Desert

**Agent**: `schwarzschild-penrose-geometer` | **Model**: opus
**Gate**: DESERT-DYNAMICS-57
- **PASS**: P_exc > 0.1 at the BCS freeze point tau = 0.22. Desert decouples cells.
- **FAIL**: P_exc < 0.01. Josephson gap persists through desert.
- **INFO**: 0.01 < P_exc < 0.1. Intermediate regime.

**Method**: Solve the time-dependent Schrodinger equation for the 2-cell system where E_J(tau(t)) evolves through the coherence desert (E_J/H < 1 during tau in [0.08, 0.22]):
1. Use W1-1 infrastructure but focus on the desert epoch specifically
2. Track <cos(phi_1 - phi_2)>(tau) -- inter-cell phase correlation
3. If correlation drops below 0.5 during desert: cells genuinely decouple
4. Compare P_exc at tau = 0.22 between full-coupled and desert-decoupled scenarios

**Source**: Workshop 1, Gate 2 (S5); S56-sp-collab.

**Input**: W1-1 time-evolution code, `s56_post_transit_coh.npz`, `canonical_constants.py`
**Output**: `computations/s57_desert_dynamics.npz`

---

### W2-3: CC-SIGN-57 -- Is the CC Anti-Binding Energy of Shattered Condensate?

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus
**Gate**: CC-SIGN-57
- **PASS**: Lambda_eff > 0 (positive, consistent with accelerating expansion)
- **FAIL**: Lambda_eff < 0 (negative, deceleration)

**Method**: From Naz's review of the final synthesis (Section 5.1): the nuclear condensation energy E_cond is NEGATIVE (binding). Removing the condensation RAISES the energy. The post-transit GGE has HIGHER energy than the pre-transit BCS state. Test:
1. Compute E_GGE - E_BCS at the fold using known GGE temperatures and BCS ground state energy
2. Verify the sign: the CC should be positive (the unshattered fraction has positive vacuum energy)
3. Use Volovik's correct formula (Workshop 2, V3):
   Lambda_eff = (1/V_eff) * Sum_k [n_k^GGE - n_k^eq] * [epsilon_k - T_eq * (ds/dn)_k]
4. Does the Leggett-channel contribution have the correct sign?

**Source**: S56-final-synthesis-naz-collab (Section 5.1), sign concern.

**Input**: W0-3 output, S38 GGE data, `canonical_constants.py`
**Output**: `computations/s57_cc_sign.npz`

---

### W2-4: FABRIC-DM-ABUNDANCE-57 -- Does Leggett-Channel DM Match Omega_DM h^2?

**Agent**: `nazarewicz-nuclear-structure-theorist` (primary), `little-red-dots-jwst-analyst` (observational check) | **Model**: opus
**Gate**: FABRIC-DM-ABUNDANCE-57
- **PASS**: Predicted Omega_DM h^2 within factor of 3 of 0.120
- **FAIL**: Predicted Omega_DM h^2 off by > 10x
- **INFO**: Depends on unresolved scale bridge (M_KK to eV)

**Method**: Using W1-1 and W1-2 outputs:
1. Extract P_exc^Leggett and E_L (energy deposited in Leggett channel per 2-cell unit)
2. Scale to 32 cells using W1-3 gap scaling
3. Compute the DM energy density: rho_DM = E_L * n_KZ_cells / V_Hubble
4. Convert to Omega_DM h^2 using the scale bridge M_KK = 7.43e16 GeV

**Critical issue**: The scale bridge M_KK -> eV is unresolved since S42 (Level 4 blocked). This computation can report rho_DM/M_KK^4 exactly but converting to physical units requires the M_KK identification, which IS established (M_KK = 7.43e16 GeV from Paper 14 eq 2.85/2.88).

The observational benchmark (LRD, Workshop 4 P3): Omega_DM h^2 = 0.120 +/- 0.001.

**Source**: Workshop 4 P3, S56-lrd-collab, S56-cw-collab.

**Input**: W1-1, W1-2, W1-3 outputs, `canonical_constants.py`
**Output**: `computations/s57_fabric_dm_abundance.npz`

---

## IX. Decision Point 2

Read W2-1 through W2-4. Two questions:

1. **Does the CC have the correct sign?** If Lambda_eff < 0, the noise-floor picture is inconsistent with accelerating expansion.

2. **Is the predicted Omega_DM h^2 within striking distance of 0.120?** Even order-of-magnitude agreement would be significant for a zero-parameter prediction.

---

## X. Wave 3: Catch-All (Every Remaining Recommendation)

Every computation below is a carry-forward from one or more S56 sources. Nothing deferred.

---

### W3-1: FLOQUET-PLASMA-57 -- Floquet Stability of Josephson Plasma Mode

**Agent**: `tesla-resonance` | **Model**: opus
**Gate**: FLOQUET-PLASMA-57
- **PASS**: Floquet exponent mu_F > 0 at any tau. Parametric instability exists.
- **FAIL**: mu_F <= 0 everywhere. Plasma mode stable.

**Method**: Compute the Floquet exponent mu_F(tau) for the Josephson plasma mode omega_J(tau) = sqrt(E_J(tau) * E_c(tau)) under the parametric drive from the transit. Test resonance condition 2*omega_J = d(omega_J)/dtau * t.

**THIS IS THE 5th CARRY-FORWARD**: S53 -> S54 -> S55 -> S56 -> S57. Tesla has proposed this computation since S53. It tests whether parametric resonance in the plasma mode provides a non-perturbative excitation channel that bypasses both BCS and Josephson gaps.

**Source**: S56-tesla-collab (T-3), Workshop 1 Gate 5.

**Input**: `s56_ba_spectrum.npz`, `s54_scale_factor.npz`, `canonical_constants.py`
**Output**: `computations/s57_floquet_plasma.npz`

---

### W3-2: PERCOLATION-CC-57 -- Percolation Threshold on CG Graph

**Agent**: `schwarzschild-penrose-geometer` (structure), `einstein-theorist` (physical interpretation) | **Model**: opus
**Gate**: PERCOLATION-CC-57
- INFO: Map domain size vs tau. Characterize percolation fraction.

**Method** (Einstein, Workshop 2 V5 Computation 4): Compute the percolation threshold for the CG(24) graph at which the coherence desert (E_J/H < 1) fragments the fabric into isolated domains:
1. At each tau, compute which bonds have E_J(tau)/H(tau) > 1 (connected) vs < 1 (broken)
2. Find the largest connected component
3. Map domain size distribution vs tau
4. If domain size = 1 cell during the transit epoch [0.08, 0.22], single-cell GGE physics applies

**Source**: Workshop 2, V5 Computation 4; S56-einstein-collab.

**Input**: `s56_post_transit_coh.npz`, `s54_tb_hamiltonian.npz`, `s54_scale_factor.npz`
**Output**: `computations/s57_percolation_cc.npz`

---

### W3-3: CHI-Q-MICROSCOPIC-57 -- Vacuum Compressibility from BCS Hamiltonian

**Agent**: `gen-physicist` | **Model**: opus
**Gate**: CHI-Q-MICROSCOPIC-57
- INFO: Is chi_q computable from the BCS Hamiltonian, or does it require the microscopic theory?

**Method** (Volovik, Workshop 2 V5 Computation 5): The spectral action gives chi_q(SA) = 317,863 M_KK^4 (S53). The PHYSICAL chi_q for CC self-tuning requires the microscopic Hamiltonian.
1. Compute chi_q^{BCS} = d^2 F_BCS / d(mu)^2 at mu = 0 from the BCS Hamiltonian on the fabric
2. Compare to chi_q(SA) = 317,863 M_KK^4
3. If chi_q^{BCS} differs from chi_q(SA): the spectral action susceptibility is NOT the microscopic one. Path A (q-theory) requires specification beyond the spectral action.
4. Report Lambda_eff = (delta_q)^2 / (2 * chi_q^{BCS}) using delta_q from W0-3

**Source**: Workshop 2, V5 Computation 5; S56-vol-collab.

**Input**: `s54_ed_sweep.npz`, `s56_pvac_fabric.npz`, `canonical_constants.py`
**Output**: `computations/s57_chi_q_microscopic.npz`

---

### W3-4: OFF-JENSEN-EJ-57 -- Is E_J Non-Monotonic Off-Jensen?

**Agent**: `phonon-first-cosmologist` (designated, per S56-naz-collab recommendation) | **Model**: opus
**Gate**: OFF-JENSEN-EJ-57
- **PASS**: E_J(tau, sigma) has a saddle point or minimum at sigma != 0
- **FAIL**: E_J remains monotone in all explored directions

**Method** (Naz S56 collab, Computation 3): The Jensen deformation is a one-parameter family. The off-Jensen T2 direction (S54) provides a second modulus sigma. Compute E_J(tau, sigma) at a grid of (tau, sigma) values:
1. Use `s54_off_jensen_t2.npz` for the off-Jensen metric
2. Compute J_C2(tau, sigma) and F_anom(tau, sigma) at a 10x10 grid
3. E_J(tau, sigma) = J_C2^2 * F_anom
4. Is E_J non-monotonic in the (tau, sigma) plane? Gen proved (Workshop 2 A3) that on the Jensen line, J_C2 monotonicity is protected by volume preservation + coupling running. Off-Jensen: this protection may fail.

**Source**: S56-naz-collab Computation 3.

**Input**: `s54_off_jensen_t2.npz`, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s57_off_jensen_ej.npz`

---

### W3-5: BAYESIAN-FABRIC-57 -- Paper 06 History Matching

**Agent**: `phonon-first-cosmologist` | **Model**: opus
**Gate**: INFO -- Does the Bayesian history-matching framework from Paper 06 constrain the fabric parameters?

**Method** (Naz S56 collab, Computation 5): Apply the Paper 06 methodology (Bayesian spectroscopic analysis) to the fabric:
1. Define the parameter space: {E_J, E_c, epsilon, N_cells}
2. Define observables: {Omega_DM, Omega_Lambda, Delta m^2, theta_13}
3. Construct the implausibility function I(x) from S56/S57 computations
4. Identify the Not Ruled Out Yet (NROY) region
5. Does the NROY region include the physical parameters?

**Source**: S56-naz-collab Computation 5.

**Input**: All W1-W2 outputs, Paper 06 methodology
**Output**: `computations/s57_bayesian_fabric.npz`

---

### W3-6: DOMAIN-WALL-57 -- Volovik Domain Wall Structure

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus
**Gate**: INFO -- characterize domain wall structure on the CG graph

**Method** (S56-vol-collab, Computation 4): During the transit, the three-phase chronology (coherent -> desert -> recoherent) may produce domain walls between cells with different GGE states:
1. Compute the domain wall energy E_DW between two cells with different GGE temperatures
2. Determine whether domain walls are topologically stable on the CG graph (Z_3 structure)
3. Estimate the domain wall density during the desert epoch
4. If domain walls persist post-transit: they could contribute to DM or modify the CC

**Source**: S56-vol-collab Computation 4.

**Input**: `s56_post_transit_coh.npz`, `s54_tb_hamiltonian.npz`, `canonical_constants.py`
**Output**: `computations/s57_domain_wall.npz`

---

### W3-7: FABRIC-KZ-QUENCH-57 -- Kibble-Zurek Defect Density on Fabric

**Agent**: `kitaev-quantum-chaos-theorist` | **Model**: opus
**Gate**: INFO -- KZ defect density from the BCS quench

**Method** (S56-foam-collab, FABRIC-KZ-QUENCH): Compute the Kibble-Zurek defect density for the BCS phase transition on the 32-cell fabric:
1. Determine the critical exponents: z (dynamical), nu (correlation length)
2. The BCS transition at the fold has Delta(tau) vanishing at some tau_c
3. KZ predicts defect density n_def ~ (tau_Q)^{-d*nu/(1+z*nu)} where tau_Q is the quench rate
4. Use H(tau) as the quench rate
5. Compare to W2-2 desert dynamics: do the KZ defects form during the desert?

**Source**: S56-foam-collab.

**Input**: `s54_scale_factor.npz`, `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s57_fabric_kz_quench.npz`

---

### W3-8: NS-MAPPING-57 -- Transfer Function KK to Cosmological Scales

**Agent**: `neutrino-detection-specialist` | **Model**: opus
**Gate**: INFO -- map the KK-scale DM properties to cosmological observables

**Method** (Workshop 4 P5, S56-neutrino-collab): The DM properties computed in M_KK units must be translated to cosmological observables:
1. Mass spectrum: m_DM in eV from the GGE quasiparticle energies * M_KK
2. Cross-section: sigma/m in cm^2/g (S42: 5.7e-51, recompute on fabric)
3. Phase space distribution: non-thermal GGE vs thermal WIMP
4. Observational consequences: halo mass function, matter power spectrum P(k), Lyman-alpha forest
5. Can any ground-based or space-based experiment (JUNO, DUNE, KATRIN, Euclid) distinguish GGE-relic DM from standard CDM?

**Source**: Workshop 4 P5, S56-neutrino-collab.

**Input**: W1-1, W1-2 outputs, S42 cross-section data, `canonical_constants.py`
**Output**: `computations/s57_ns_mapping.npz`

---

### W3-9: SUB-GAP-PARTITION-57 -- Mattis-Bardeen Protected Modes + Tesla Characterization Bundle

**Agent**: `tesla-resonance` | **Model**: opus
**Gate**: SUB-GAP-BA-57
- **PASS**: |dF_above-gap/dtau| < 0.1 * |dF_sub-gap/dtau| at fold (leakage negligible)
- **FAIL**: ratio exceeds 0.1 (above-gap leakage significant)

**Method** (S56-tesla-collab, T-1 through T-6): This computation bundles four Tesla carry-forwards:

**(T-1) Sub-gap BA mode partition function**: Partition the 31 BA modes into sub-gap (omega_n < 2*Delta = 0.929 M_KK) and above-gap (omega_n > 2*Delta) at each tau. Compute F_BA restricted to each partition separately. If the above-gap contribution to dF/dtau is small compared to sub-gap, adiabatic protection extends to the full BA spectrum.

**(T-2) Quasiparticle decay rate of above-gap modes**: Compute Gamma_decay(omega_n) for the 16 above-gap modes using Mattis-Bardeen formula. Report Gamma_decay * t_transit for each. If > 1 for any mode, that mode fully thermalizes into the quasiparticle sector.

**(T-4) BLV 8D acoustic metric exponent** (3rd carry-forward from S53): The BLV acoustic metric in d spatial dimensions gives N_e corrections with exponent (d-1)/(2d-2). For d=8 (SU(3)): exponent = 7/14 = 1/2 (same as 3D). Confirm or deny by explicit computation. Gate: INFO.

**(T-6) Josephson plasma line**: Compute g(omega) for the full coupled fabric spectrum. Verify whether omega_J = 0.715 M_KK is resolved as a discrete spectral feature. Gate: PASS if spectral weight at omega_J exceeds 3x smooth background.

**Source**: S56-tesla-collab (T-1 through T-6). T-5 (impedance at domain walls) is covered by W2-2 + W3-6.

**Input**: `s56_ba_spectrum.npz`, `s54_ed_sweep.npz`, `s56_leggett_fabric.npz`, `canonical_constants.py`
**Output**: `computations/s57_sub_gap_partition.npz`

---

### W3-10: STUCKELBERG-DM-57 -- Stuckelberg Oscillation DM Channel

**Agent**: `kaku-speculative-theorist` | **Model**: opus
**Gate**: INFO -- does the Stuckelberg interference at intermediate tau produce a new DM channel?

**Method** (Workshop 4 cross-synthesis, Kaku identification): At intermediate tau, level quasi-crossings produce Stuckelberg oscillations (constructive/destructive interference between different Landau-Zener paths). Kaku identified gamma = 39.2 and P_exc ~ 10^{-17} for the finite-rate transit, but Stuckelberg oscillations could enhance this:
1. Identify all level quasi-crossings in the 2-cell spectrum between tau = 0.10 and tau = 0.40
2. Compute the Stuckelberg phase phi_S = integral(Delta(tau') dtau', tau_1, tau_2) for consecutive crossings
3. If phi_S = (2n+1)*pi: constructive interference, P_exc enhanced
4. Map P_exc^{Stuckelberg} vs tau for the strongest quasi-crossings

**Source**: Workshop 4, Kaku cross-synthesis.

**Input**: `s54_tb_hamiltonian.npz`, `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s57_stuckelberg_dm.npz`

---

### W3-11: OMEGA-L-TAU-SWEEP-57 -- Leggett Frequency Minimum Search

**Agent**: `quantum-acoustics-theorist` | **Model**: opus
**Gate**: INFO -- precise location and depth of omega_L0(tau) minimum

**Method** (S56-qa-collab, Q1 response): QA identified that omega_L0(tau) is likely non-monotonic because E_J(tau) decreases while Delta_eff(tau) peaks near the fold. The minimum of omega_L0 sets the most diabatic point for the Leggett LZ transition:
1. Compute omega_L0(tau) at fine tau spacing (100 points in [0, 0.5])
2. Identify the global minimum and all local minima
3. At each minimum, compute the adiabaticity parameter gamma = pi*omega_L0^2 / (2*|d(omega_L0)/dt|)
4. If gamma < 0.01 at the minimum: Leggett excitation is essentially complete there
5. If gamma > 1 at the minimum: Leggett excitation is partially adiabatic, reducing P_LZ

This is a refinement of W0-1 with finer tau resolution. If W0-1 already provides sufficient resolution, report that and skip to the gamma computation.

**Source**: S56-qa-collab (Q1 response).

**Input**: `s56_leggett_fabric.npz`, `s54_tb_hamiltonian.npz`, `s54_scale_factor.npz`, `canonical_constants.py`
**Output**: `computations/s57_omega_l_tau_sweep.npz`

---

### W3-12: PHASE-DIAGRAM-57 -- Full E_J/E_c vs T_GH/T_BKT Map

**Agent**: `landau-condensed-matter-theorist` | **Model**: opus
**Gate**: INFO -- complete phase diagram of the fabric

**Method** (S56-landau-collab, Computation 5): Map the full phase diagram of the Josephson array as the transit evolves:
1. At each tau, compute E_J/E_c and T_GH/T_BKT
2. Plot the transit trajectory on the Fazio-van der Zant phase diagram (Paper 19)
3. Identify which phases the system traverses: superfluid, Bose glass, Mott insulator, normal
4. Does the transit cross any phase boundary?
5. If yes: what are the critical exponents at the crossing? This feeds into W3-7 (KZ defects)

**Source**: S56-landau-collab Computation 5.

**Input**: `s56_ba_spectrum.npz`, `s56_bkt_test.npz`, `canonical_constants.py`
**Output**: `computations/s57_phase_diagram.npz`

---

### W3-13: TOPOLOGY-TRANSITION-57 -- Level Quasi-Crossing at tau = 0.449

**Agent**: `berry-geometric-phase-theorist` | **Model**: opus
**Gate**: INFO -- is the tau = 0.449 gap closure a genuine topological transition?

**Method** (S56-qa-collab, Computation 5): At tau = 0.449 (W0-3 data), the TB spectrum shows a quasi-crossing with gap ~0.003 M_KK. Is this a genuine topological transition (band inversion, change in Z_2 invariant) or a discretization artifact?
1. Compute the Z_2 invariant (Pfaffian signature) at tau = 0.44, 0.449, 0.46
2. If sgn(Pf) changes: genuine topological transition. Compute KZ defect density and excitation energy
3. If sgn(Pf) unchanged: numerical near-degeneracy, not topological
4. Connection to Volovik program: topological transitions in internal space produce zero-mode fermions

**Source**: S56-qa-collab Computation 5 (TOPOLOGY-TRANSITION-57), Workshop 3 N3 channel 7.

**Input**: `s54_tb_hamiltonian.npz`, `s54_ed_sweep.npz`, `canonical_constants.py`
**Output**: `computations/s57_topology_transition.npz`

---

## XI. Agent Batch Assignments

Max 3-4 agents per parallel batch (per project rules).

### Wave 0 (4 agents, parallel)
| Batch | Agents |
|:------|:-------|
| 0A | Naz (W0-1), QA (W0-2), Volovik (W0-3), Kitaev (W0-4) |

### Wave 1 (4 agents, parallel)
| Batch | Agents |
|:------|:-------|
| 1A | Naz (W1-1), QA (W1-2), Gen (W1-3) |
| 1B | Kitaev (W1-4), Feynman (W1-1 cross-check) |

### Wave 2 (4 agents, parallel, conditional on W1)
| Batch | Agents |
|:------|:-------|
| 2A | Landau (W2-1), SP (W2-2), Volovik (W2-3), Naz+LRD (W2-4) |

### Wave 3 (13 computations, 4 batches of 3-4)
| Batch | Agents |
|:------|:-------|
| 3A | Tesla (W3-1, W3-9), SP+Einstein (W3-2), Gen (W3-3) |
| 3B | Phonon (W3-4, W3-5), Volovik (W3-6), Kitaev (W3-7) |
| 3C | Neutrino (W3-8), Kaku (W3-10), QA (W3-11), Landau (W3-12) |
| 3D | Berry (W3-13) |

---

## XII. Execution Notes

- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for ALL scripts
- **Script prefix**: `s57_`
- **Output directory**: `computations/`
- **Constants**: Import from `canonical_constants.py` (mandatory S34+)
- **GPU**: Available on RX 9070 XT (17.1 GB VRAM) for W1-3 (N=8 exact diag, dim=2016)
- **Estimated total runtime**: W0 ~20 min, W1 ~2 hrs (dominated by W1-1 rate scan), W2 ~1 hr, W3 ~3 hrs
- **Working paper**: `sessions/archive/session-57/session-57-results-workingpaper.md` (created at session start)

### Strutinsky-First Design (QA Workshop 3 Q3 recommendation)

Following the S56 design lesson: compute the smooth Josephson background FIRST, subtract it, and study the residual. Every computation that reports an energy or free energy should decompose it as:

    F_full = F_smooth (Josephson background) + delta_F (shell correction)

This prevents repeating the S56 error of mistaking a 0.8% ripple for a significant feature.

---

## XIII. What Each Outcome Means

### If THE-SHATTERING-57 = PASS

The framework produces BOTH dark matter (Leggett-channel quasiparticles, ~30%) AND the cosmological constant (Josephson-channel vacuum noise, ~70%) from ONE event -- the shattering of the BCS condensate at the Jensen fold. The DM/Lambda ratio is set by the gap hierarchy. Zero free parameters. No other framework in physics derives both quantities from the same event.

Dark matter IS the debris of a quantum phase transition on the internal geometry of spacetime. Non-annihilating by BDI algebraic identity. Non-thermal by integrability protection. Abundance set by the coset geometry SU(3)/U(2).

### If THE-SHATTERING-57 = FAIL

The pattern was pareidolia. The eigenvalue theorems survive (mass ordering, three generations, NNI texture). The 47 closures survive. The mathematical structure of the framework is intact. But the claim that the internal geometry of SU(3) determines the energy budget of the observable universe dies with one number.

### If GAP-SCALING-57 shows Delta_N ~ N^alpha with alpha > 0

The CC hierarchy may emerge from fabric geometry. The 260-OOM ambiguity collapses. If alpha = 1 (linear gap growth), Lambda ~ exp(-N^2) -- a double exponential that could bridge the 115-order gap with N ~ 5-8 cells. This would be a structural breakthrough independent of the DM question.

### If ANDREEV-INTEG-57 shows <r> > 0.48

Integrability is broken at the fabric level. The 8 Richardson-Gaudin conserved quantities are approximate, not exact. The GGE thermalizes on some timescale. The CC then self-tunes to zero by the equilibrium theorem, with a residual set by the thermalization rate. This opens Path B for the CC (Workshop 2, V3).

---

## XIV. Carry-Forward Registry

Every computation in this plan traces to a specific S56 source. The table below documents provenance and ensures nothing was lost.

| Computation | Source(s) | Originally proposed by |
|:------------|:---------|:----------------------|
| LEGGETT-TAU-PROFILE-57 | Workshop 3 Q1a, S56-qa-collab | Naz (Q1a), QA (response) |
| CHANNEL-ENERGY-BUDGET-57 | DM synthesis Section III | Phonon-First Cosmologist |
| GGE-EQUILIBRIUM-GAP-57 | Workshop 2, V5 Comp 1 | Volovik |
| ANDREEV-ANISOTROPY-EST-57 | Workshop 1 K1, S56-kitaev-collab | Kitaev |
| FINITE-RATE-TRANSIT-57 | Workshop 3 N5 (full spec) | Naz (spec), all 6 W3 reviewers (endorsed) |
| LEGGETT-PARTITION-57 | DM synthesis Section IV | Phonon-First Cosmologist |
| GAP-SCALING-57 | Workshop 1 Gate 1, Workshop 2 V5 Comp 3 | Berry, Hawking, Feynman, Landau, Volovik (5/7 endorsed) |
| ANDREEV-INTEG-57 | Workshop 1 Gate 3, S56-kitaev-collab | Kitaev, Feynman, Berry |
| PARKER-BA-57 | Workshop 1 Gate 4, S56-landau-collab Comp 1 | Landau |
| DESERT-DYNAMICS-57 | Workshop 1 Gate 2, S56-sp-collab | SP, Berry |
| CC-SIGN-57 | S56-final-synthesis-naz-collab Sec 5.1 | Naz |
| FABRIC-DM-ABUNDANCE-57 | Workshop 4 P3, S56-lrd-collab | LRD, Neutrino |
| FLOQUET-PLASMA-57 | Workshop 1 Gate 5, S56-tesla-collab T-3 | Tesla (5th carry-forward: S53->S54->S55->S56->S57) |
| PERCOLATION-CC-57 | Workshop 2, V5 Comp 4 | Einstein |
| CHI-Q-MICROSCOPIC-57 | Workshop 2, V5 Comp 5 | Volovik |
| OFF-JENSEN-EJ-57 | S56-naz-collab Comp 3 | Naz |
| BAYESIAN-FABRIC-57 | S56-naz-collab Comp 5 | Naz |
| DOMAIN-WALL-57 | S56-vol-collab Comp 4 | Volovik |
| FABRIC-KZ-QUENCH-57 | S56-foam-collab | Foam |
| NS-MAPPING-57 | Workshop 4 P5, S56-neutrino-collab | Neutrino |
| SUB-GAP-PARTITION-57 (+ T-2, T-4, T-6) | S56-tesla-collab T-1,T-2,T-4,T-6 | Tesla |
| T-5 (impedance at domain walls) | S56-tesla-collab T-5 | Tesla (covered by W2-2 + W3-6) |
| STUCKELBERG-DM-57 | Workshop 4 cross-synthesis | Kaku |
| OMEGA-L-TAU-SWEEP-57 | S56-qa-collab Q1 | QA |
| PHASE-DIAGRAM-57 | S56-landau-collab Comp 5 | Landau |
| TOPOLOGY-TRANSITION-57 | S56-qa-collab Comp 5 | QA |
| LEGGETT-ENTROPY-57 | S56-qa-collab Comp 4 | QA (subsumed into W1-2: DM synthesis reframes entropy-stabilization as DM-partition) |
| FABRIC-LZ-57 | S56-vol-collab Comp 2 | Volovik (subsumed into W1-1 RATE-SCAN sub-computation) |
| GAMMA-ANDREEV-57 | S56-vol-collab Comp 5 | Volovik (subsumed into W1-4 Andreev integrability) |
| ANISO-JOSEPHSON-57 | S56-landau-collab Comp 3 | Landau (= W1-4 ANDREEV-INTEG-57, same channel) |
| FINITE-RATE-LZ-57 | S56-landau-collab Comp 4 | Landau (subsumed into W1-1 LEGGETT-LZ-57 sub-computation) |
| QP-TUNNEL-57 | S56-naz-collab Comp 2 | Naz (= W1-4 ANDREEV-INTEG-57) |

**Total**: 25 computations across 4 waves (13 in W3). Every S56 recommendation accounted for. 7 subsumed into parent computations. Nothing deferred.

---

## XV. The Structural Position Entering S57

The framework sits at a precise crossroads visible from eight pillars simultaneously:

**Pillar I** (acoustic gravity): BLV metric confirmed, T_GH = 0.590 M_KK, greybody factor Gamma = 6.6e-4 on the 2-cell fabric.

**Pillar II** (Volovik program): Equilibrium theorem confirmed at fabric level (W2-2). Lambda_eq = 0 is a theorem. CC is entirely non-equilibrium.

**Pillar III** (NCG spectral action): D_K spectrum determines everything -- but everything it determines is monotone. Block-diagonal theorem holds at fabric scale.

**Pillar IV** (flat band BCS): Van Hove singularity drives pairing (M_max = 1.674). BCS instability is a 1D theorem.

**Pillar V** (Josephson arrays): E_J/E_c = 194. Deep superfluid. Two-speed hierarchy discovered. Leggett channel identified as primary surviving excitation mechanism.

**Pillar VI** (topological solitons): Z_3 wall network gives three generations. Domain walls connect to the coherence desert.

**Pillar VII** (spectral dimension flow): d_s = 1.73 at the fold. CDT connection.

**Pillar VIII** (KK geometry): Jensen deformation is the unique volume-preserving family. J_C2 monotonicity is permanent.

All eight pillars converge on: a superfluid quantum vacuum on a compact Lie group, transiting through a van Hove fold, shattering its condensate into two channels separated by a gap hierarchy, leaving a permanent non-thermal relic protected by exact integrability. The CC is the noise floor. The dark matter is the debris. The ratio is set by the geometry.

Whether this convergence is real or pareidolia is determined by one number: P_exc^Leggett from FINITE-RATE-TRANSIT-57.

The computation is sub-second on a laptop. The answer determines whether the universe remembers its own geometry.
