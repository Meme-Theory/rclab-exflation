# Session 56 Plan: Z Warriors Assemble -- The Fabric Partition Function

**Date**: 2026-03-22
**Author**: Quantum Acoustics Theorist (planner)
**Format**: Parallel single-agent computations across 4 waves
**Source**: S55 results (34 computations, master gate FAIL), 6 collaborative reviews (QA, Naz, Vol, Ein, Bap, QF) + master synthesis, S55 framework update (1,974 lines)
**Motivation**: S55 proved every single-cell stabilization functional monotone on the continuum (46+ closures). It simultaneously discovered the fabric is superfluid (E_J/E_c = 194). All 6 reviewers unanimously identified the systematic error: Z_cell is the wrong thermodynamic object. The physical partition function is Z_fabric, which includes Bogoliubov-Anderson phonons, Josephson plasma modes, inter-cell phase correlations, and BCS gap structure that Z_cell^N structurally cannot encode. S56 computes Z_fabric and tests whether collective modes break the single-cell monotonicity barrier.
**Results file**: `sessions/archive/session-56/session-56-results-workingpaper.md`

---

## I. Session Objective

Compute the fabric partition function Z_fabric for the 32-cell superfluid Josephson array on Jensen-deformed SU(3) and determine whether collective inter-cell physics produces a free energy minimum that single-cell physics cannot.

**Pre-registered master gate**:
- **FABRIC-STABILIZATION-56**: Does Z_fabric(tau) have a minimum near the fold that Z_cell does not?
- **PASS**: F_fabric(tau) has a minimum in [0.10, 0.30] with barrier > 1% of |F_fabric(0)|
- **FAIL**: F_fabric(tau) is monotone (or minimum outside target range, or barrier < 1%)
- **Null hypothesis**: Collective modes inherit single-cell monotonicity; the fabric does not stabilize the modulus

**Secondary gates** (see individual computations):
- FABRIC-INTEGRABILITY-56: Does Josephson coupling break integrability at the fabric level?
- MU-SHIFT-56: Does inter-cell coupling generate nonzero effective chemical potential?
- NPAIR3-ED-56: Does integrability breaking reach GOE statistics at N_pair=3?

---

## II. The Central Physics

The partition function of a lattice of coupled oscillators is not the product of single-oscillator partition functions raised to the Nth power. Every S55 monotonicity theorem has domain of validity: one isolated cell. The physical system has:

1. **E_J = 7.042 M_KK per bond** (Josephson coupling from BCS anomalous density, S55 W3-16)
2. **E_J/E_c = 194** (superfluid regime, 40x above SIT)
3. **E_J/H = 231** (entire Hubble volume = one phase domain)
4. **93 bonds** on the 32-cell CG graph (mean coordination z = 5.81)
5. **omega_J = 0.715 M_KK** (Josephson plasma frequency, comparable to Delta = 0.464)
6. **omega_J/Delta = 1.54 < 2** (plasma mode INSIDE BCS gap, undamped)

The fabric partition function Z_fabric = Tr exp(-beta H_fabric) where H_fabric = Sum_i H_BCS(i) + Sum_{<ij>} H_Josephson(ij) includes:
- Bogoliubov-Anderson phonons (31 nonzero modes with linear dispersion, d_s = 2 Weyl class)
- Josephson plasma mode at omega_J = 0.715 M_KK
- Phase stiffness ~ -z * E_J / 2 per cell = -20.5 M_KK/cell (mean-field)
- BCS quasiparticle spectrum with gap Delta = 0.464 M_KK
- Volovik: inter-cell Josephson energy = -E_J * N_bonds = -655 M_KK (390x single-cell E_GGE)

---

## III. Wave Structure

### Dependency Graph

```
Wave 0 (ZERO-COST, from existing S54/S55 data, ~15 min):
  W0-1: BA-SPECTRUM-56       W0-2: NEFF-56
  W0-3: CBA-SOUND-56         W0-4: BKT-TEST-56

  ---- Decision Point 0: Does BA spectrum have nontrivial tau-dependence? ----
  ---- Does N_eff << 992? Does T_BKT > T_GH at the fold? ----

Wave 1 (DECISIVE GATES, parallel, ~3 hrs):
  W1-1: ROTOR-MF-56          W1-2: FABRIC-INTEG-56
  W1-3: NPAIR3-ED-56         W1-4: MU-JOSEPHSON-56

  ---- Decision Point 1: THE FABRIC FORK ----
  ---- If W1-1 PASS: collective stabilization found ----
  ---- If W1-1 FAIL + W1-2 PASS: CC path at fabric scale ----
  ---- If both FAIL: dynamic transit only ----

Wave 2 (FOLLOW-UPS, conditional on W0/W1):
  W2-1: EUCLID-FABRIC-56     W2-2: PVAC-FABRIC-56
  W2-3: STRUTINSKY-FABRIC-56  W2-4: LEGGETT-FABRIC-56

Wave 3 (CATCH-ALL FINAL -- every remaining collab suggestion):
  W3-1: ATENSOR-FRUSTRATION-56    W3-2: POST-TRANSIT-COH-56
  W3-3: NS-FABRIC-56              W3-4: SPECTRAL-DIM-FLOW-56
  W3-5: EJ-UNCERTAINTY-56         W3-6: GGE-FABRIC-56
  W3-7: OMEGA-ATT-CONFIRM-56      W3-8: MASS-VARIATION-56
```

### Agent Roster

All physics agents use **opus**. Max 3-4 agents per parallel batch.

| Agent | Waves | Specialty |
|:------|:------|:----------|
| `quantum-acoustics-theorist` | W0-1, W0-3, W2-4 | BA phonons, sound velocity, Leggett dispersion |
| `landau-condensed-matter-theorist` | W0-2, W0-4, W1-1 | Mode count, BKT, quantum rotor mean-field |
| `volovik-superfluid-universe-theorist` | W1-2, W2-2, W3-6 | Fabric integrability, Volovik identity, GGE |
| `nazarewicz-nuclear-structure-theorist` | W1-3, W2-3, W3-5 | N_pair=3, Strutinsky, uncertainty |
| `spectral-geometer` | W1-4, W3-4 | mu-shift, spectral dimension flow |
| `baptista-spacetime-analyst` | W3-1, W3-8 | A-tensor frustration, mass variation |
| `einstein-theorist` | W3-2, W3-3 | Post-transit coherence, spectral index |
| `phonon-first-cosmologist` | W2-1, W3-7 | Fabric Euclidean F, omega_att confirmation |

---

## IV. Wave 0: Zero-Cost Diagnostics (from existing S54/S55 data)

All Wave 0 computations use ONLY existing .npz files. No new spectrum computations.

---

### W0-1: BA-SPECTRUM-56 -- Bogoliubov-Anderson Phonon Spectrum on 32-Cell Graph

**Agent**: `quantum-acoustics-theorist` | **Model**: opus | **Cost**: ZERO

**Prompt**:

Compute the Bogoliubov-Anderson (BA) phonon spectrum on the 32-cell CG graph at 50 tau values. The BA modes are the normal modes of phase fluctuations in the superfluid fabric. Their frequencies determine the collective contribution to Z_fabric.

**Physics**: In a Josephson array, the quantum rotor Hamiltonian H = -E_J Sum_{<ij>} cos(phi_i - phi_j) + E_c Sum_i n_i^2, expanded to quadratic order in phase fluctuations around the uniform ground state, gives H_quad = (1/2) rho_s(tau) Sum_{ij} L_ij phi_i phi_j + (1/2) E_c Sum_i n_i^2, where L_ij is the weighted graph Laplacian. The normal mode frequencies are:

  omega_n(tau) = sqrt(E_c(tau) * rho_s(tau) * lambda_n)

where lambda_n are the graph Laplacian eigenvalues (the eigenvalues from s54_tb_hamiltonian.npz normalized by J_C2(tau) give the graph Laplacian eigenvalues: lambda_n = E_n(tau) / J_C2(tau)).

The superfluid stiffness rho_s(tau) = E_J(tau) per bond, where E_J(tau) = J_C2(tau)^2 * F_anomalous(tau). F_anomalous uses BCS coherence factors computed from the 32-cell eigenvalues at each tau.

E_c(tau) = (E_k(N/2) - E_k(N/2-1)) / 2, the charging energy from the level spacing at the Fermi surface.

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz` for eigenvalues (50 x 32), J_C2_tau (50,).
2. At each tau:
   a. Compute graph Laplacian eigenvalues: lambda_n = eigenvalues_n / J_C2(tau). The zero mode lambda_0 = 0.
   b. Compute BCS coherence factors from the 32 eigenvalues: xi_k = E_k - mu, E_qp_k = sqrt(xi_k^2 + Delta^2), uv_k = Delta/(2 E_qp_k). Delta = 0.4643 M_KK (canonical).
   c. Compute F_anomalous(tau) = Sum_k (uv_k / E_qp_k) = Sum_k Delta / (2 E_qp_k^2).
   d. Compute E_J(tau) = J_C2(tau)^2 * F_anomalous(tau).
   e. Compute E_c(tau) = (eigenvalue[N/2] - eigenvalue[N/2-1]) / 2.
   f. Compute omega_n(tau) = sqrt(E_c(tau) * E_J(tau) * lambda_n) for n = 1,...,31 (skip zero mode).
3. Compute F_BA(tau, T_GH) = Sum_{n=1}^{31} [omega_n/2 + T_GH * ln(1 - exp(-omega_n/T_GH))].
   Load T_GH(tau) from `computations/s54_scale_factor.npz`: T_GH = H/(2*pi).
4. Plot: (a) omega_n(tau) dispersion at 5 representative tau values, (b) F_BA(tau) vs tau, (c) E_J(tau) and E_c(tau), (d) omega_J(tau) = omega_1(tau) * sqrt(N) (the uniform plasma frequency).
5. Check monotonicity of F_BA(tau).

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `computations/s54_scale_factor.npz`, `from canonical_constants import *`
**Gate**: BA-SPECTRUM-56 -- INFO: BA phonon spectrum characterization. If F_BA(tau) has a minimum in [0.10, 0.30], flag for W1-1 integration.
**Output**: Script `s56_ba_spectrum.py`, data `s56_ba_spectrum.npz`, plot `s56_ba_spectrum.png`. Working paper W0-1.

---

### W0-2: NEFF-56 -- Effective Mode Count in Z_fabric vs Z_cell^N

**Agent**: `landau-condensed-matter-theorist` | **Model**: opus | **Cost**: ZERO

**Prompt**:

Compute the effective number of thermodynamic degrees of freedom in the fabric and compare to the single-cell independent-mode prediction. The "mode count wins" argument (S55 W2-1) assumes all 992 continuum modes contribute independently. Phase coherence in the superfluid reduces this.

**Physics**: The effective mode count measures how many independent degrees of freedom contribute to the entropy. In a superfluid Josephson array:
- The phase sector is rigid: all 32 cells share one global phase, contributing O(1) modes, not O(N).
- The 31 nonzero BA phonon modes replace 31 independent single-cell modes.
- The remaining (992 - 31) single-cell modes are modified by the BCS gap but remain approximately independent.

The metric: N_eff(tau) = S_fabric(tau) / S_single_mode, where S_fabric is the entropy of the coupled system and S_single_mode is the mean entropy per mode in the uncoupled system. Alternatively: N_eff = 2 * F_fabric / (T_GH * ln 2) for Fermi modes at high temperature.

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz` (eigenvalues at 50 tau), `computations/s54_scale_factor.npz` (H(tau) for T_GH).
2. At each tau:
   a. Compute the single-cell partition function Z_cell = Prod_{k=1}^{8} (1 + exp(-E_k/T_GH)) using the 8 BCS-active modes from the lowest Voronoi cell spectrum. Note: 8 modes per cell, 32 cells. For the independent-cell estimate, use Z_cell^32 and S_independent = 32 * S_cell.
   b. Compute the entropy of the BA phonon sector: S_BA = Sum_{n=1}^{31} [beta*omega_n/(exp(beta*omega_n)-1) - ln(1 - exp(-beta*omega_n))]. This requires BA frequencies from W0-1 data (OR compute them inline from graph Laplacian and E_J/E_c).
   c. Compute N_eff = S_BA / (S_independent / (32 * 8)) = effective modes from collective sector compared to per-mode entropy.
3. Also compute: ratio Z_fabric_phase / Z_cell_phase, where Z_fabric_phase = Prod_{n=1}^{31} [2 sinh(omega_n/(2T_GH))]^{-1} (bosonic phonon) and Z_cell_phase = [2 sinh(omega_single/(2T_GH))]^{-32} (32 independent oscillators at single-cell frequency).
4. Plot: N_eff(tau) vs tau. If N_eff << 992, the "mode count wins" assumption fails.

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `computations/s54_scale_factor.npz`, `from canonical_constants import *`
**Gate**: NEFF-56 -- INFO: N_eff(tau) characterization. If N_eff < 100 at the fold, flag "mode count wins" as invalidated for Z_fabric.
**Output**: Script `s56_neff.py`, data `s56_neff.npz`, plot `s56_neff.png`. Working paper W0-2.

---

### W0-3: CBA-SOUND-56 -- Bogoliubov Sound Velocity on the Fabric

**Agent**: `quantum-acoustics-theorist` | **Model**: opus | **Cost**: ZERO

**Prompt**:

Compute the Bogoliubov-Anderson sound velocity c_BA(tau) on the 32-cell CG graph. This is the inter-cell acoustic velocity -- distinct from the intra-cell c_Gold. It determines the acoustic metric for collective phase modes.

**Physics**: The BA sound velocity on a graph is:
  c_BA = a_graph * sqrt(E_J * E_c) / hbar
where a_graph is the effective lattice spacing (1/k_min, with k_min = pi/D, D = graph diameter = 6). Equivalently, from the lowest nonzero BA frequency:
  c_BA = omega_1 / k_min = omega_1 * D / pi

The tau-dependence comes from E_J(tau) * E_c(tau). Since E_J ~ J_C2^2 * F_anomalous and E_c ~ delta_E_F, both vary with tau. The competition between these factors determines whether c_BA has a minimum, maximum, or is monotone.

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz`.
2. At each of 50 tau values:
   a. Compute omega_1(tau) = sqrt(E_c(tau) * E_J(tau) * lambda_1_graph), where lambda_1_graph = eigenvalue_1(tau) / J_C2(tau).
   b. c_BA(tau) = omega_1(tau) * D / pi, where D = 6 (graph diameter).
3. Compute the ratio c_BA(tau) / c_Gold(tau), where c_Gold = 0.915 M_KK (canonical constant, from GL dispersion S53). Note c_Gold has only 0.21% tau variation.
4. Compute the acoustic scale factor: a_inter(tau) ~ 1/c_BA(tau). Check if a_inter has a maximum (natural acoustic stabilization point).
5. Compare two acoustic metrics: a_intra ~ 1/c_Gold(tau) vs a_inter ~ 1/c_BA(tau). Report the tau-dependence of each.
6. Check for roton minimum: plot the full BA dispersion omega_n(tau_fold) vs n. If the dispersion has a local minimum before the Brillouin zone edge (analogous to the He-4 roton), report its location and depth.

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `from canonical_constants import *`
**Gate**: CBA-SOUND-56 -- INFO: c_BA(tau) profile and comparison to c_Gold. If c_BA has a minimum near the fold, flag for acoustic stabilization analysis.
**Output**: Script `s56_cba_sound.py`, data `s56_cba_sound.npz`, plot `s56_cba_sound.png`. Working paper W0-3.

---

### W0-4: BKT-TEST-56 -- Berezinskii-Kosterlitz-Thouless Temperature vs T_GH

**Agent**: `landau-condensed-matter-theorist` | **Model**: opus | **Cost**: ZERO

**Prompt**:

Compute the BKT transition temperature T_BKT(tau) on the d_s = 2 CG graph and compare it to T_GH(tau). On a 2D lattice, the superfluid transition is BKT (vortex-antivortex unbinding), not mean-field. If T_GH(tau) crosses T_BKT(tau) at some tau_BKT, the fabric undergoes a phase transition -- a potential stabilization mechanism.

**Physics**: The BKT temperature on a lattice with coordination z is:
  T_BKT = (pi / 2) * rho_s_eff
where rho_s_eff = E_J (the superfluid stiffness per bond). On a graph with mean coordination z:
  T_BKT(tau) = (pi / 2) * E_J(tau)

The Gibbons-Hawking temperature: T_GH(tau) = H(tau) / (2*pi).

The Nelson-Kosterlitz universal jump: at T_BKT, the superfluid stiffness jumps from rho_s = 2*T_BKT/pi to zero.

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz`, `computations/s54_scale_factor.npz`.
2. At each tau:
   a. Compute E_J(tau) = J_C2(tau)^2 * F_anomalous(tau) (same as W0-1).
   b. T_BKT(tau) = (pi/2) * E_J(tau).
   c. T_GH(tau) = H(tau)/(2*pi). Interpolate H(tau) from 10-point scale factor data.
3. Plot T_BKT(tau) and T_GH(tau) on the same axes. Identify crossings.
4. Compute the ratio T_GH/T_BKT at the fold. Report: "superfluid" if T_GH < T_BKT, "normal" if T_GH > T_BKT.
5. If T_BKT has a minimum near the fold: report tau_min and T_BKT(tau_min).

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `computations/s54_scale_factor.npz`, `from canonical_constants import *`
**Gate**: BKT-CROSSING-56 -- INFO: T_BKT(tau) vs T_GH(tau) crossing analysis. If crossing in [0.05, 0.40], flag for fabric phase transition analysis.
**Output**: Script `s56_bkt_test.py`, data `s56_bkt_test.npz`, plot `s56_bkt_test.png`. Working paper W0-4.

---

## Decision Point 0

| W0-1 BA spectrum | W0-2 N_eff | W0-3 c_BA | W0-4 BKT | Assessment |
|:----------------|:-----------|:----------|:---------|:-----------|
| Non-trivial tau-dep | N_eff << 992 | c_BA has minimum | T_GH < T_BKT at fold | Full fabric frontier OPEN. W1-1 is decisive. |
| Monotone | N_eff ~ 992 | c_BA monotone | T_GH > T_BKT | Fabric collective modes inherit single-cell monotonicity. Direction B (dynamic transit) likely. Still run W1-1 with full mean-field. |
| Any | N_eff < 100 | Any | Any | "Mode count wins" OVERTURNED. Single-cell continuum FAIL (W2-1 in S55) may not extend to fabric. |

---

## V. Wave 1: The Decisive Gates

Four computations that determine whether the fabric provides stabilization, breaks integrability, or shifts the chemical potential. Max 3-4 agents in parallel -- run W1-1 and W1-2 in batch 1, W1-3 and W1-4 in batch 2 if needed.

---

### W1-1: ROTOR-MF-56 -- Quantum Rotor Mean-Field Free Energy on 32-Cell Graph

**Agent**: `landau-condensed-matter-theorist` | **Model**: opus | **Cost**: MEDIUM

**THIS IS THE SINGLE MOST IMPORTANT COMPUTATION OF S56.**

**Prompt**:

Compute F_fabric(tau) on the 32-cell CG graph using self-consistent mean-field theory for the quantum rotor model, combined with the Bogoliubov-Anderson phonon contribution and the BCS quasiparticle contribution. Test whether F_fabric has a minimum in [0.10, 0.30].

**Physics**: The fabric free energy decomposes into three contributions (Nazarewicz decomposition):

  F_fabric(tau, T) = F_cell(tau, T) * N_cells + F_Josephson(tau, T) + F_BA(tau, T)

where:
- F_cell = single-cell BCS free energy (KNOWN, monotone from S55 W0-2/W2-1)
- F_Josephson = -N_bonds * E_J(tau) * <cos(phi)>(tau, T) = Josephson phase stiffness contribution
- F_BA = Sum_{n=1}^{31} [omega_n(tau)/2 + T * ln(1 - exp(-omega_n(tau)/T))] = BA phonon contribution

The self-consistency condition: <cos(phi)> depends on E_J and T through the quantum rotor model. At temperature T with Josephson coupling E_J, the mean-field order parameter on a z-coordinated lattice is:

  <cos(phi)> = I_1(z * E_J * <cos(phi)> / T) / I_0(z * E_J * <cos(phi)> / T)

where I_0, I_1 are modified Bessel functions. This is the standard self-consistency equation for the XY model on a lattice (Fazio-van der Zant, Paper 19).

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz` (eigenvalues, J_C2_tau, adj_C2).
2. Load `computations/s54_scale_factor.npz` (H(tau) -> T_GH(tau) = H/(2*pi)).
3. Load `computations/s55_pair_mobility.npz` (for cross-check of rho_s).
4. At each of 50 tau values in [0, 0.50]:
   a. Compute E_J(tau) = J_C2^2 * F_anomalous(tau) (same BCS anomalous density formula as s55_fabric_coupling.py).
   b. Compute E_c(tau) = level spacing at Fermi surface / 2.
   c. Compute T_GH(tau) = H(tau)/(2*pi) (interpolate H from scale factor data).
   d. Solve the mean-field self-consistency equation for <cos(phi)>(tau):
      - Initialize m = 0.99 (deep superfluid).
      - Iterate: m_new = I_1(z_mean * E_J(tau) * m / T_GH(tau)) / I_0(z_mean * E_J(tau) * m / T_GH(tau)).
      - Converge to |m_new - m| < 1e-12. z_mean = 5.8125 from adj_C2.
   e. Compute F_Josephson(tau) = -N_bonds * E_J(tau) * m(tau), where N_bonds = sum(adj_C2)/2.
   f. Compute BA phonon frequencies omega_n(tau) = sqrt(E_c * E_J * lambda_n_graph) for n = 1..31.
   g. Compute F_BA(tau) = Sum_{n=1}^{31} [omega_n/2 + T_GH * ln(1 - exp(-omega_n/T_GH))].
   h. Compute F_cell(tau) = -T_GH * ln(Prod_k (1 + exp(-E_k/T_GH))) using 8 BCS eigenvalues per cell. F_cells_total = 32 * F_cell.
   i. F_fabric(tau) = F_cells_total + F_Josephson + F_BA.
5. Plot:
   a. F_fabric(tau), F_cells_total(tau), F_Josephson(tau), F_BA(tau) on the same axes.
   b. <cos(phi)>(tau) (order parameter) vs tau.
   c. d(F_fabric)/d(tau) vs tau -- sign changes = extrema.
6. Search for minima: dF_fabric/dtau = 0 with d^2F_fabric/dtau^2 > 0 in [0.10, 0.30].
7. If minimum found: compute barrier height = max(F_fabric(0), F_fabric(0.50)) - F_fabric(tau_min). Report barrier as percentage of |F_fabric(0)|.
8. Report also: the relative contribution of each term at the fold. Which term dominates dF_fabric/dtau? Is it F_Josephson (the new term) or F_cells (the old term)?

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `computations/s54_scale_factor.npz`, `computations/s55_pair_mobility.npz`, `from canonical_constants import *`
**Gate**: FABRIC-FREE-ENERGY-56 -- PASS: F_fabric has minimum in [0.10, 0.30] with barrier > 1%. FAIL: monotone.
**Output**: Script `s56_rotor_mf.py`, data `s56_rotor_mf.npz`, plot `s56_rotor_mf.png`. Working paper W1-1.

---

### W1-2: FABRIC-INTEG-56 -- Fabric-Level Integrability Diagnostic

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus | **Cost**: HIGH

**Prompt**:

Test whether Josephson inter-cell coupling breaks the single-cell Richardson-Gaudin integrability. The CC = integrability thesis requires integrability to prevent thermalization of the GGE relic. If the fabric coupling breaks integrability, the GGE can partially thermalize through inter-cell phase diffusion -- a CC resolution path at the fabric scale.

**Physics**: Each isolated cell has an exactly integrable Richardson-Gaudin Hamiltonian with 8 conserved quantities. The Josephson coupling H_J = -E_J * Sum_{<ij>} cos(phi_i - phi_j) couples the conserved quantities of different cells. The combined H_fabric is NOT Richardson-Gaudin integrable in general.

The test: for a 2-cell system, construct H_2cell = H_BCS(1) + H_BCS(2) + alpha * H_J(1,2), where alpha parametrizes the coupling strength. The uncoupled system (alpha=0) is integrable (Poisson level statistics, <r> = 0.386). The fully coupled system (alpha=1) may be chaotic (GOE, <r> = 0.531) or remain integrable.

**Method**:
1. Construct the 2-cell Hilbert space. Each cell has 8 single-particle levels. At half-filling (4 particles per cell), the Fock space dimension per cell is C(8,4) = 70. The 2-cell space is 70 x 70 = 4,900 states (NOT 2^16 = 65,536 -- that would be 16 modes with arbitrary filling).
   CORRECTION: The BCS Hamiltonian conserves pair number. At N_pair = 1 per cell (framework convention), each cell has C(8,1) = 8 pair states. The 2-cell space is 8 x 8 = 64 (two pairs, one per cell). BUT the density-density interaction couples pair sectors. For a tractable computation: use the single-pair sector (N_pair_total = 2 on 2 cells, dim = C(16,2) = 120) or the two-pair sector (N_pair_total = 2, one per cell, dim = 8 x 8 = 64).
   Choose: 2 pairs on 16 modes, dim = C(16,2) = 120. This is feasible.
2. Build H_2cell at the fold (tau = 0.194):
   a. H_BCS for each cell from s54 eigenvalues + Kosmann pairing kernel.
   b. H_J = -E_J * cos(phi_1 - phi_2). In the number basis, represent cos(phi_1 - phi_2) using pair creation/annihilation operators: cos(phi_1 - phi_2) = (1/2)(b_1^dag b_2 + b_2^dag b_1), where b_i = Sum_k c_{k,down} c_{k,up} is the pair annihilation operator on cell i.
3. Compute eigenvalues of H_2cell at 10 values of alpha in [0, 1].
4. At each alpha: compute <r> = <min(delta_n, delta_{n+1})/max(delta_n, delta_{n+1})>.
5. Plot <r>(alpha). Report <r> at alpha = 1 (physical coupling).
6. Also compute at 5 tau values near the fold to check tau-dependence.

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `computations/s54_ed_sweep.npz`, `computations/s27_multisector_bcs.npz`, `from canonical_constants import *`
**Gate**: FABRIC-INTEGRABILITY-56 -- PASS: <r>_fabric > 0.48 at alpha=1 (integrability broken). FAIL: <r> < 0.40 (Poisson, persists).
**Output**: Script `s56_fabric_integ.py`, data `s56_fabric_integ.npz`, plot `s56_fabric_integ.png`. Working paper W1-2.

---

### W1-3: NPAIR3-ED-56 -- N_pair=3 Exact Diagonalization on Single Cell

**Agent**: `nazarewicz-nuclear-structure-theorist` | **Model**: opus | **Cost**: MEDIUM

**Prompt**:

Perform exact diagonalization of the 3-pair BCS Hamiltonian on 8 modes. S55 W1-4 showed <r>_fold = 0.509 (+2.0 sigma from Poisson) at N_pair=2, but dim=28 was too small for definitive statistics. At N_pair=3, dim = C(8,3) = 56, providing better statistics and testing whether integrability breaking grows with pair number.

**Physics**: The Richardson-Gaudin model is exactly integrable for the pure BCS pairing interaction. At N_pair >= 2, the density-density interaction V_dd * n_k * n_{k'} breaks integrability. The question: does the breaking grow to GOE levels (<r> = 0.531) at N_pair = 3?

**Method**:
1. Construct the 3-pair Fock space on 8 modes: C(8,3) = 56 basis states.
2. Build H_BCS + H_dd:
   a. H_BCS = Sum_k 2*eps_k * n_k - V * Sum_{k,k'} c^dag_{k,up} c^dag_{k,down} c_{k',down} c_{k',up}.
   b. H_dd = alpha_dd * Sum_{k!=k'} n_k * n_{k'} (density-density, S55 W1-4 convention).
   c. Use eigenvalues from `computations/s54_tb_hamiltonian.npz` at the fold.
   d. Use V matrix from `computations/s27_multisector_bcs.npz` (singlet sector).
3. Diagonalize the 56x56 matrix at 10 tau values near the fold [0.10, 0.30].
4. Compute <r> at each tau with the standard nearest-neighbor spacing ratio.
5. Perform the alpha_dd sweep from 0 to 2 (20 values) at the fold, mapping the Poisson-to-GOE transition curve.
6. Compute:
   a. Ground state occupation distribution: {<n_k>} for k = 1..8.
   b. IPR (inverse participation ratio) of ground state in the Fock basis.
   c. Vacuum pressure P_vac from the diagonal ensemble vs GGE.
   d. Quench overlap: prepare the ground state at tau = 0, project onto eigenstates at tau_fold. Report adiabaticity (IPR of |psi_0(tau=0)> in the tau_fold eigenbasis).

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `computations/s54_ed_sweep.npz`, `computations/s27_multisector_bcs.npz`, `from canonical_constants import *`
**Gate**: NPAIR3-ED-56 -- PASS: <r> >= 0.53 at alpha_dd = 1.0 (GOE, integrability definitively broken). FAIL: <r> < 0.45 (near-Poisson, integrable). INFO: 0.45 <= <r> < 0.53 (transition regime, inconclusive at dim=56).
**Output**: Script `s56_npair3_ed.py`, data `s56_npair3_ed.npz`, plot `s56_npair3_ed.png`. Working paper W1-3.

---

### W1-4: MU-JOSEPHSON-56 -- Chemical Potential Shift from Inter-Cell Coupling

**Agent**: `spectral-geometer` | **Model**: opus | **Cost**: MEDIUM

**Prompt**:

Compute the effective chemical potential mu_eff generated by Josephson inter-cell coupling. The S34 mu = 0 theorem requires particle-hole symmetry of the single-cell Dirac spectrum. Josephson coupling broadens each single-cell level into a BAND of width ~ 4*J. Band formation generically breaks PH symmetry because band centers are not symmetrically placed.

**Physics**: At mean-field level, the effective single-particle Hamiltonian on the fabric is:
  H_eff(k) = eps_k + Sigma_J(k)
where eps_k is the single-cell eigenvalue and Sigma_J is the self-energy from Josephson coupling. For the tight-binding model on the CG graph, the bandwidth of each level is W_n = 4 * J_C2 * delta_n, where delta_n depends on the eigenvector structure.

The effective chemical potential is the value of mu_eff that satisfies:
  Sum_k f(eps_k + Sigma_J(k) - mu_eff) = N_fill
where f is the Fermi function. If PH symmetry is exact, mu_eff = 0. If the band structure breaks PH symmetry, mu_eff != 0.

S55 W1-3 showed that dS_f/dtau > 0 in [0.025, 0.125] on the continuum when mu != 0. If |mu_eff| > 0, the fermionic spectral action non-monotonicity at mu != 0 becomes physical.

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz` (eigenvalues at 50 tau, J_C2_tau, hamiltonians).
2. At each tau:
   a. The TB Hamiltonian H(tau) is 32x32. It describes the hopping of one particle across 32 cells. At half-filling (16 particles), the chemical potential mu is the midpoint of the 16th and 17th eigenvalues.
   b. Compute mu(tau) = (E_16(tau) + E_17(tau)) / 2. The deviation from the PH-symmetric value mu_PH = 0 (or the spectral midpoint) quantifies the PH breaking.
   c. Compute the PH asymmetry: A_PH(tau) = Sum_{k=1}^{32} (E_k + E_{33-k}) / (2 * BW). If PH is exact, each pair sums to a constant.
3. For the Josephson-broadened spectrum: construct the mean-field BdG Hamiltonian on the fabric.
   a. For each single-cell level eps_k, the Josephson coupling generates a band. The band center is eps_k (unchanged). The band edges are eps_k +/- z * J_C2 * |u_k|^2, where |u_k|^2 is the local amplitude squared.
   b. Compute the density of states rho(E, tau) of the fabric Hamiltonian (32 eigenvalues per cell x 32 cells = 1024 levels if fully resolved, but the TB Hamiltonian already hybridizes them into 32 fabric levels).
   c. At half-filling on the fabric, compute mu_fabric(tau) = midpoint of levels 16 and 17.
4. Report: mu_fabric(tau) vs tau. Is there a tau where |mu_fabric| > 0.1 M_KK?
5. If mu_eff != 0: compute dS_f/dtau at the physical mu_eff and check if the sign differs from the mu=0 result.

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `computations/s55_sf_sign.npz`, `from canonical_constants import *`
**Gate**: MU-SHIFT-56 -- PASS: |mu_eff| > 0.1 M_KK at any tau in [0.10, 0.30]. FAIL: |mu_eff| < 0.01 M_KK everywhere (PH effectively unbroken).
**Output**: Script `s56_mu_josephson.py`, data `s56_mu_josephson.npz`, plot `s56_mu_josephson.png`. Working paper W1-4.

---

## Decision Point 1: THE FABRIC FORK

| W1-1 F_fabric | W1-2 Integrability | W1-3 N_pair=3 | W1-4 mu-shift | Assessment |
|:--------------|:-------------------|:-------------|:-------------|:-----------|
| PASS (minimum) | Any | Any | Any | **COLLECTIVE STABILIZATION FOUND.** Fabric Z resolves the 55-session stabilization search. W2 characterizes the mechanism. |
| FAIL | PASS (<r> > 0.48) | Any | Any | **CC PATH AT FABRIC SCALE.** No stabilization, but integrability breaks through inter-cell coupling. GGE can partially thermalize. W2 quantifies the CC reduction. |
| FAIL | FAIL | PASS (<r> > 0.53) | Any | **CC PATH AT SINGLE-CELL N_pair >= 3.** Fabric does not break integrability, but higher pair number does. |
| FAIL | FAIL | FAIL | PASS | **MU-SHIFT OPENS S_f CHANNEL.** The non-monotone fermionic spectral action at mu != 0 becomes physical. New stabilization route. |
| FAIL | FAIL | FAIL | FAIL | **DIRECTION B: DYNAMIC TRANSIT ONLY.** The fabric inherits single-cell monotonicity. The "dynamic transit of the superfluid as a whole" is the sole surviving cosmology. W2 characterizes transit dynamics. |

---

## VI. Wave 2: Follow-Ups (conditional on Wave 0/1)

Four computations that develop the fabric picture regardless of the fork outcome.

---

### W2-1: EUCLID-FABRIC-56 -- Euclidean Free Energy on Fabric Including All Contributions

**Agent**: `phonon-first-cosmologist` | **Model**: opus | **Cost**: MEDIUM
**Depends on**: W0-1 (BA spectrum), W1-1 (quantum rotor mean-field)

**Prompt**:

Extend the S55 Euclidean free energy computation (W0-2 and W2-1) to the full fabric. The S55 lattice result (PASS with 29% barrier on 8 modes) became FAIL on the 992-mode continuum because "mode count wins." The fabric reduces the effective mode count through phase coherence. Does the minimum survive on the fabric?

**Method**:
1. Load results from W0-1 (BA spectrum: omega_n(tau)) and W1-1 (F_fabric decomposition).
2. Construct F_Euclidean_fabric(tau) = F_BCS_quasiparticle + F_Josephson + F_BA, where:
   a. F_BCS_quasiparticle uses the BCS quasiparticle spectrum (with gap Delta) instead of the free spectrum. This replaces the 992 independent modes with gapped quasiparticles.
   b. F_Josephson from W1-1.
   c. F_BA from W0-1.
3. Compare to the S55 results: F_fabric(tau) vs F_sp(tau) (S55 W2-1, monotone on 992 modes).
4. If W1-1 found a minimum: verify it is reproduced in this independent construction.
5. If W1-1 did NOT find a minimum: test whether adding the BCS gap (which the rotor model misses) changes the qualitative behavior.

**Inputs**: W0-1 data, W1-1 data, `computations/s55_euclid_continuum.npz`, `computations/s55_euclid.npz`, `from canonical_constants import *`
**Gate**: EUCLID-FABRIC-56 -- INFO: cross-check of W1-1 with gap-corrected partition function.
**Output**: Script `s56_euclid_fabric.py`, data `s56_euclid_fabric.npz`, plot `s56_euclid_fabric.png`. Working paper W2-1.

---

### W2-2: PVAC-FABRIC-56 -- Volovik Vacuum Pressure on the Coupled Fabric

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus | **Cost**: MEDIUM
**Depends on**: W1-1 (for <cos(phi)>), W1-2 (for 2-cell eigenvalues)

**Prompt**:

Compute the Volovik vacuum pressure P_vac on the coupled fabric and compare to the single-cell value P_vac = -0.688 M_KK. The Josephson energy (-655 M_KK for 93 bonds) dominates the single-cell E_GGE (1.688 M_KK per cell x 32 = 54 M_KK). Whether the Josephson energy is at its EQUILIBRIUM value determines its contribution to P_vac.

**Physics**: In q-theory (Papers 15-16), the vacuum pressure at equilibrium is P_vac = 0 (Volovik equilibrium theorem). The departure from equilibrium determines the cosmological constant. The single-cell Euler tautology gives P_vac = N_pair - E_GGE = -0.688. On the fabric:

  P_vac_fabric = N_pair_total - E_GGE_fabric

where E_GGE_fabric = Sum_i E_GGE(i) + Sum_{<ij>} (-E_J * <cos(phi_i - phi_j)>_GGE).

The question: is <cos(phi)>_GGE = <cos(phi)>_ground_state (equilibrium, contributing 0 to P_vac), or does the transit disrupt phase alignment (non-equilibrium, contributing to P_vac)?

**Method**:
1. Use W1-1 mean-field order parameter m(tau) = <cos(phi)>(tau) at T_GH.
2. Compute: E_Josephson(tau) = -N_bonds * E_J(tau) * m(tau).
3. Compute: E_GGE_fabric(tau) = 32 * E_GGE_single + E_Josephson(tau).
   Use E_GGE_single = 1.688 M_KK (from S55 W3-5).
4. Compute P_vac_fabric = 32 - E_GGE_fabric.
5. For the 2-cell system from W1-2: compute the exact ground state energy E_gs(alpha=1) and compare to the sum of single-cell ground state energies. The difference is the inter-cell correlation energy.
6. Report: sign of P_vac_fabric, magnitude, comparison to P_vac_single = -0.688.

**Inputs**: W1-1 data, W1-2 data, `computations/s55_volovik_identity.npz`, `from canonical_constants import *`
**Gate**: FABRIC-PVAC-56 -- INFO: |P_vac_fabric| < |P_vac_cell| (fabric moves toward q-theory self-tuning). Report sign.
**Output**: Script `s56_pvac_fabric.py`, data `s56_pvac_fabric.npz`, plot `s56_pvac_fabric.png`. Working paper W2-2.

---

### W2-3: STRUTINSKY-FABRIC-56 -- Strutinsky Decomposition of Fabric Hamiltonian

**Agent**: `nazarewicz-nuclear-structure-theorist` | **Model**: opus | **Cost**: MEDIUM
**Depends on**: W0-1 (BA spectrum)

**Prompt**:

Perform the Strutinsky shell-correction decomposition on the FABRIC Hamiltonian (32-cell TB + Josephson), not just the single-cell Dirac spectrum. The S55 W2-5 Strutinsky gradient ratio was 0.71 on the single cell, meaning the shell correction provides 71% of the restoring force. Does the fabric Hamiltonian's shell correction close the gap?

**Physics**: In nuclear physics, the Strutinsky shell correction delta_E_shell = E_exact - E_smooth determines the deformation energy surface. The MEAN-FIELD Hamiltonian (not the bare interaction) is what gets decomposed. For the fabric, the relevant spectrum is the 32 eigenvalues of H_TB(tau) plus the 31 BA phonon frequencies.

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz`.
2. At each tau (50 values):
   a. Extract the 32 TB eigenvalues.
   b. Compute the Strutinsky smooth energy E_smooth using polynomial fitting (order 3-5) to the cumulative level density.
   c. Compute delta_E_shell = E_exact - E_smooth. E_exact = Sum_{k=1}^{16} E_k (half-filling, 16 occupied).
   d. Include the 31 BA phonon zero-point energies: E_BA_ZP = (1/2) Sum_n omega_n(tau).
   e. Total fabric energy: E_fabric = E_exact + E_BA_ZP + F_Josephson(tau).
3. Compute the gradient ratio: (d(delta_E_shell)/dtau) / (d(E_smooth)/dtau). If > 1.0, the shell correction can overcome the smooth trend.
4. Compare to the S55 single-cell ratio 0.71. Does the fabric increase or decrease the gradient ratio?

**Inputs**: `computations/s54_tb_hamiltonian.npz`, W0-1 data, `from canonical_constants import *`
**Gate**: STRUTINSKY-FABRIC-56 -- INFO: gradient ratio on fabric vs single-cell (0.71). If > 1.0, shell corrections SUFFICIENT.
**Output**: Script `s56_strutinsky_fabric.py`, data `s56_strutinsky_fabric.npz`, plot `s56_strutinsky_fabric.png`. Working paper W2-3.

---

### W2-4: LEGGETT-FABRIC-56 -- Leggett Mode Dispersion on 32-Cell Graph

**Agent**: `quantum-acoustics-theorist` | **Model**: opus | **Cost**: LOW
**Depends on**: W0-1 (BA spectrum for comparison)

**Prompt**:

Compute the Leggett mode dispersion on the 32-cell CG graph. The Leggett mode is the relative phase oscillation between B2 and B1 sectors. On the fabric, this becomes a propagating collective mode with dispersion omega_L^2(k) = omega_L^2 + c_L^2 * k^2, where omega_L = 0.138 M_KK (from S38 frequency hierarchy via S49). The velocity c_L is the Leggett mode propagation speed -- the massive Goldstone boson of the framework.

**Physics**: The Leggett mode on the fabric couples through the SAME Josephson channels as the BA phonon. The Leggett Hamiltonian on the graph is:

  H_Leggett = Sum_i [(delta omega_L)^2 / 2 * (theta_i)^2 + Sum_{<ij>} J_Leggett * (theta_i - theta_j)^2]

where theta_i is the relative B2-B1 phase at cell i, and J_Leggett = epsilon * E_J (epsilon = 0.00248 from DIPOLAR-CATALOG-49). The dispersion is omega_L^2(n) = omega_L^2 + c_L^2 * (pi*n/D)^2, with c_L = sqrt(J_Leggett * a^2 / m_L).

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz` for graph Laplacian eigenvalues.
2. At the fold (tau = 0.194):
   a. omega_L = 0.138 M_KK (S49 Leggett value -- could also use omega_L1 = 0.070, omega_L2 = 0.107 from dipolar catalog; use all three and report).
   b. epsilon = 0.00248 from DIPOLAR-CATALOG-49.
   c. E_J(tau_fold) = 7.042 M_KK (from S55 W3-16).
   d. J_Leggett = epsilon * E_J = 0.00248 * 7.042 = 0.01747 M_KK.
   e. omega_L(n) = sqrt(omega_L^2 + J_Leggett * lambda_n_graph), where lambda_n_graph are the graph Laplacian eigenvalues normalized to the lattice.
3. Plot the Leggett dispersion alongside the BA phonon dispersion. Identify the gap.
4. Report: c_L (Leggett mode velocity), omega_L(k_max) at the zone edge, and the ratio omega_L_gap/T_GH.

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `from canonical_constants import *`
**Gate**: LEGGETT-FABRIC-56 -- INFO: omega_L(k) has real c_L > 0. Report c_L and compare to c_BA.
**Output**: Script `s56_leggett_fabric.py`, data `s56_leggett_fabric.npz`, plot `s56_leggett_fabric.png`. Working paper W2-4.

---

## VII. Wave 3: Catch-All (nothing deferred)

Every remaining suggestion from all 6 collab reviews gets a computation slot. These are lower priority but are carried forward per project rules.

---

### W3-1: ATENSOR-FRUSTRATION-56 -- A-Tensor Gauge Frustration in Josephson Coupling

**Agent**: `baptista-spacetime-analyst` | **Model**: opus | **Cost**: LOW

**Prompt**:

Compute the effect of the A-tensor gauge phase on Cooper pair hopping between cells. The A-tensor |A_coset|^2 = 3/2 + (3/2)e^{-4tau} generates a gauge phase when pairs hop along C^2 bonds. The resulting phase-dependent Josephson coupling is E_J^{gauge} ~ J_C2^2 * cos(Delta_phi - A*d), where d is the inter-cell distance. This frustration could modify the ground state from uniform phase ordering to a nontrivial pattern.

**Method**:
1. Compute |A_coset|^2(tau) at the fold using the proven formula: |A|^2 = 3/2 + (3/2)*exp(-4*tau).
2. The gauge phase acquired per hop: Phi_gauge = integral of A along the C^2 geodesic between adjacent cells. On the CG graph, estimate the geodesic length d_C2 from the Connes distance between adjacent cells (from s54_connes_latt.npz).
3. Compute the frustration parameter: f = Phi_gauge / pi. If f is close to 0 or 1, the frustration is weak. If f ~ 0.5, maximum frustration (antiferromagnetic-like phase ordering).
4. Construct the frustrated Josephson Hamiltonian: H_J^{frust} = -E_J * Sum_{<ij>} cos(phi_i - phi_j - A_{ij}), where A_{ij} is the gauge phase for bond (i,j).
5. Solve the mean-field self-consistency with frustration and compare <cos(phi)>_frustrated to <cos(phi)>_unfrustrated from W1-1.
6. If frustration is significant (> 10% modification of <cos(phi)>): flag for revision of all W1 results.

**Inputs**: `computations/s55_atensor_gauge.npz`, `computations/s54_connes_latt.npz`, `computations/s54_tb_hamiltonian.npz`, `from canonical_constants import *`
**Gate**: ATENSOR-FRUSTRATION-56 -- INFO: frustration parameter f and modification of <cos(phi)>.
**Output**: Script `s56_atensor_frustration.py`, data `s56_atensor_frustration.npz`. Working paper W3-1.

---

### W3-2: POST-TRANSIT-COH-56 -- Post-Transit Superfluid Coherence

**Agent**: `einstein-theorist` | **Model**: opus | **Cost**: LOW

**Prompt**:

Compute E_J/H in the post-transit era (tau > 0.22, where BCS freeze occurs). The superfluid coherence argument for the horizon problem requires phase coherence AFTER the transit. After the transit, the condensate is destroyed (P_exc = 1.000). What maintains causal contact across the Hubble volume? (Einstein collab, Section 3.3)

**Method**:
1. Load `computations/s54_scale_factor.npz` for H(tau) and `computations/s54_tb_hamiltonian.npz` for J_C2(tau).
2. Compute E_J(tau) at all 50 tau values (same formula as W0-1).
3. Compute the ratio E_J(tau)/H(tau) for tau > 0.22 (post-BCS freeze).
4. The condensate amplitude Delta(tau) goes to zero post-transit (P_exc = 1.000). The anomalous density F_anomalous(tau) also vanishes. Therefore E_J -> J_C2^2 * 0 = 0 in the destroyed-condensate limit.
5. BUT: the GGE relic preserves non-zero pair correlations <c^dag c^dag c c>_GGE != 0 (integrability protects the conserved quantities). Estimate the GGE-averaged E_J using the GGE occupation numbers.
6. Report: does phase coherence survive the transit? If not, what replaces it for the horizon problem?

**Inputs**: `computations/s54_scale_factor.npz`, `computations/s54_tb_hamiltonian.npz`, `computations/s55_volovik_identity.npz`, `computations/s55_bogoliubov_992.npz`, `from canonical_constants import *`
**Gate**: POST-TRANSIT-COH-56 -- INFO: E_J/H at tau = 0.30, 0.40, 0.50. If E_J/H > 1, phase coherence survives. If E_J/H < 1, horizon problem returns.
**Output**: Script `s56_post_transit_coh.py`, data `s56_post_transit_coh.npz`. Working paper W3-2.

---

### W3-3: NS-FABRIC-56 -- Spectral Index from Fabric Collective Modes

**Agent**: `einstein-theorist` | **Model**: opus | **Cost**: MEDIUM

**Prompt**:

Estimate the spectral index n_s from the fabric's Bogoliubov-Anderson collective mode spectrum. The single-cell spectral index n_s = -4.45 (S45, all routes CLOSED) is catastrophically wrong. The fabric's collective modes have different dispersion (linear BA phonons, d_s = 2 Weyl class) from the single-cell Dirac spectrum (d = 8 Weyl class). Does the collective spectrum produce a spectral index closer to the observed n_s = 0.965?

**Method**:
1. Load BA spectrum from W0-1.
2. The spectral index in the phonon-exflation framework is n_s = 1 + 2*eta_eff, where eta_eff is determined by the ratio of the spectral tilt to the Hubble rate.
3. For BA phonons with dispersion omega ~ k^alpha on a d_s = 2 lattice:
   a. The power spectrum P(k) ~ k^{d_s - 2*alpha - 1} for a scale-invariant source.
   b. With alpha = 1 (linear BA phonons) and d_s = 2: P(k) ~ k^{-1}.
   c. This gives n_s = d_s - 2*alpha = 2 - 2 = 0. Still wrong.
4. The tau-dependence of c_BA(tau) modifies the tilt. If c_BA varies during the transit:
   a. n_s - 1 = -2*epsilon - eta, where epsilon = -(d/dtau)(ln c_BA)/H and eta = d(epsilon)/dtau / (epsilon * H).
   b. Compute epsilon and eta from c_BA(tau) data (from W0-3).
5. Report: n_s from the fabric calculation. If still catastrophically wrong, note the residual gap.

**Inputs**: W0-1 data, W0-3 data, `computations/s54_scale_factor.npz`, `from canonical_constants import *`
**Gate**: NS-FABRIC-56 -- INFO: n_s estimate from fabric collective modes. If in [0.93, 0.99], PASS.
**Output**: Script `s56_ns_fabric.py`, data `s56_ns_fabric.npz`. Working paper W3-3.

---

### W3-4: SPECTRAL-DIM-FLOW-56 -- Spectral Dimension Flow from Collective Modes

**Agent**: `spectral-geometer` | **Model**: opus | **Cost**: LOW

**Prompt**:

Compute the spectral dimension d_s as a function of energy/diffusion time on the 32-cell graph, accounting for the collective mode spectrum. The graph Laplacian gives d_s = 2.0 at long wavelengths (S54). At energies above omega_J = 0.715 M_KK, the Josephson plasma mode opens a new channel. Above 2*Delta = 0.929 M_KK, pair-breaking excitations add further channels. The spectral dimension should show steps. (QF collab, Pattern 3)

**Method**:
1. Load `computations/s54_graph_laplacian_ds.npz` for graph Laplacian eigenvalues.
2. Compute the heat kernel return probability P(t) = (1/N) Sum_n exp(-lambda_n * t) at the fold.
3. Extract d_s(t) = -2 * d(ln P)/d(ln t) as a function of diffusion time t.
4. Convert diffusion time to energy scale: E ~ 1/t.
5. Mark the energy thresholds: omega_J = 0.715, 2*Delta = 0.929 M_KK.
6. Plot d_s(E) and identify plateau values at each regime.

**Inputs**: `computations/s54_graph_laplacian_ds.npz`, `computations/s54_tb_hamiltonian.npz`, `from canonical_constants import *`
**Gate**: SPECTRAL-DIM-FLOW-56 -- INFO: d_s(E) profile with energy thresholds.
**Output**: Script `s56_spectral_dim_flow.py`, data `s56_spectral_dim_flow.npz`, plot `s56_spectral_dim_flow.png`. Working paper W3-4.

---

### W3-5: EJ-UNCERTAINTY-56 -- Systematic Uncertainty on E_J and Fabric Parameters

**Agent**: `nazarewicz-nuclear-structure-theorist` | **Model**: opus | **Cost**: LOW

**Prompt**:

Quantify systematic uncertainties on the key S55 fabric parameters: E_J = 7.042, E_c = 0.036, E_J/E_c = 194, omega_J = 0.715. The S55 W3-16 computation used second-order perturbation theory (BCS anomalous density method). What are the uncertainties from: (a) higher-order corrections, (b) choice of pairing interaction (OES vs GL gap), (c) truncation to 32 cells, (d) BCS vs exact Richardson ground state? (Nazarewicz collab, Section 5.3)

"A prediction without an error bar is not a prediction -- it is a number." -- Naz, citing Paper 06.

**Method**:
1. Load `computations/s55_fabric_coupling.py` methodology and `computations/s54_tb_hamiltonian.npz`.
2. Recompute E_J at the fold using:
   a. Delta = Delta_OES = 0.4643 M_KK (primary), Delta_GL = 0.5 M_KK (S53 GL fit). Compare.
   b. F_anomalous from 8 modes (lattice) vs estimate for 992 modes (continuum enhancement factor from S55 W1-1: 6-9x in E_cond). The anomalous density sum converges faster than E_cond -- estimate the convergence.
   c. Fourth-order perturbation theory correction: E_J^(4) = J^4 * Sum_{k,k'} (uv_k uv_{k'}) / (E_k + E_{k'})^3. Compute ratio E_J^(4)/E_J^(2).
3. Propagate uncertainties through to E_J/E_c and omega_J.
4. Report: E_J = X +/- Y M_KK, E_J/E_c = A +/- B, omega_J = C +/- D M_KK.
5. Also propagate through the DM/DE ratio alpha = 0.408 and the 2.92 e-fold count from S55.

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `computations/s55_erich_continuum.npz`, `from canonical_constants import *`
**Gate**: EJ-UNCERTAINTY-56 -- INFO: error bars on E_J, E_J/E_c, omega_J, alpha, N_e.
**Output**: Script `s56_ej_uncertainty.py`, data `s56_ej_uncertainty.npz`. Working paper W3-5.

---

### W3-6: GGE-FABRIC-56 -- Generalized Gibbs Ensemble on the Coupled Fabric

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus | **Cost**: MEDIUM

**Prompt**:

Characterize the GGE on the coupled 2-cell system from W1-2. The single-cell GGE has 8 Richardson-Gaudin conserved integrals. On the 2-cell system, the Josephson coupling modifies the conserved quantities. Identify the GGE conserved integrals of the coupled system and compute the GGE temperatures.

**Physics**: If the 2-cell system is integrable (W1-2 FAIL: <r> < 0.40), it has a set of conserved quantities {Q_n} and the GGE is rho_GGE = exp(-Sum lambda_n Q_n) / Z_GGE. If the system is chaotic (W1-2 PASS: <r> > 0.48), the GGE reduces to the canonical ensemble and the system thermalizes.

**Method**:
1. Use the 2-cell Hamiltonian from W1-2 at the fold.
2. Prepare the ground state at tau = 0, evolve to tau_fold (sudden quench, same as S55 W3-3).
3. Compute the diagonal ensemble rho_DE = Sum_n |c_n|^2 |n><n|.
4. If integrable: identify conserved quantities by searching for operators Q that commute with H_2cell. Compute GGE temperatures lambda_n from <Q_n>_DE = Tr(Q_n * rho_GGE).
5. Compute P_vac_GGE = N_pair_total - <H>_GGE.
6. Compare to P_vac_DE = N_pair_total - <H>_DE.

**Inputs**: W1-2 data, `computations/s55_volovik_identity.npz`, `from canonical_constants import *`
**Gate**: GGE-FABRIC-56 -- INFO: GGE structure of the coupled system and P_vac comparison.
**Output**: Script `s56_gge_fabric.py`, data `s56_gge_fabric.npz`. Working paper W3-6.

---

### W3-7: OMEGA-ATT-CONFIRM-56 -- Tau-Sweep of omega_att = 9*(B3-B1) Near-Resonance

**Agent**: `phonon-first-cosmologist` | **Model**: opus | **Cost**: LOW

**Prompt**:

The S38 finding omega_att = 9*(B3-B1) at 0.08% precision was flagged as OPEN pending a tau-sweep. Confirm or deny this near-resonance across the tau range [0, 0.50]. If it holds at all tau, it is algebraic (structural). If it drifts, it is a coincidence at the fold.

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz` for eigenvalues at 50 tau values.
2. At each tau:
   a. Identify B1 and B3 modes from the 32-cell spectrum. B1 = acoustic (lowest non-zero). B3 = dispersive optical (highest sub-band). Use the S54 branch classification.
   b. Compute omega_att(tau) from the S38 formula: omega_att = 1.430 M_KK at the fold (geometric attractor frequency).
   c. Compute 9*(E_B3 - E_B1)(tau). Report the ratio omega_att / (9*(B3-B1)).
3. Plot the ratio vs tau. If constant to 1%, it is algebraic.

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `from canonical_constants import *`
**Gate**: OMEGA-ATT-CONFIRM-56 -- INFO: Is omega_att = 9*(B3-B1) algebraic or coincidental?
**Output**: Script `s56_omega_att_confirm.py`, data `s56_omega_att_confirm.npz`. Working paper W3-7.

---

### W3-8: MASS-VARIATION-56 -- Paper 16 Eq 7.1 Mass Variation Integral

**Agent**: `baptista-spacetime-analyst` | **Model**: opus | **Cost**: MEDIUM

**Prompt**:

Compute the mass variation rate d(m_k)/dtau along the transit for each Dirac eigenvalue, using Paper 16 (Baptista) eq 7.1. This gives a purely geometric expansion mechanism independent of condensate physics. Flagged in the Baptista S53 collab and again in S55 as uncomputed.

**Physics**: Paper 16 eq 7.1 relates the mass spectrum of KK modes to the internal metric deformation. The mass variation integral:
  dm_k/dtau = Integral over SU(3) of |psi_k|^2 * (delta g / delta tau) * vol_SU3

For the Jensen deformation, delta g / delta tau is given by the variation of the Jensen metric g(tau).

**Method**:
1. Load `computations/s54_tb_hamiltonian.npz` for eigenvalues at 50 tau.
2. Compute dm_k/dtau by finite differences: dm_k = (E_k(tau + dtau) - E_k(tau - dtau)) / (2*dtau).
3. The mass variation integral per mode gives the spectral flow. The TOTAL mass variation:
   M_total(tau) = Sum_k m_k(tau). Compute dM_total/dtau.
4. Compare to the geometric quantity: Vol(SU(3)) * Tr(dg/dtau), which is known analytically for Jensen.
5. Report: the rate of spectral change during the transit as a purely geometric observable.

**Inputs**: `computations/s54_tb_hamiltonian.npz`, `from canonical_constants import *`
**Gate**: MASS-VARIATION-56 -- INFO: dm_k/dtau profile. Purely geometric expansion diagnostic.
**Output**: Script `s56_mass_variation.py`, data `s56_mass_variation.npz`, plot `s56_mass_variation.png`. Working paper W3-8.

---

## VIII. Execution Notes

### Batch Sizing
- **Wave 0** (4 computations): Run all 4 in one batch (zero-cost, existing data only, fast).
- **Wave 1** (4 computations): Run in 2 batches of 2: {W1-1, W1-2}, then {W1-3, W1-4}. W1-1 is THE computation; do not risk it being starved by batch competition.
- **Wave 2** (4 computations): Run in 2 batches after Wave 1 results are known.
- **Wave 3** (8 computations): Run in 3 batches of 3-3-2.

### Script Conventions
- All scripts: `s56_*.py` in `computations/`
- All data: `s56_*.npz` in `computations/`
- All plots: `s56_*.png` in `computations/`
- All scripts: `from canonical_constants import *`
- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`

### Working Paper
- File: `sessions/archive/session-56/session-56-results-workingpaper.md`
- Structure: copy S55 working paper structure. Each computation gets a subsection with: prompt recap, gate, results, key numbers, assessment.
- Working paper writer: designated per wave (TBD at execution).

### Data Dependencies

| Computation | Inputs (existing data) | Depends on S56 computations |
|:-----------|:----------------------|:---------------------------|
| W0-1 BA-SPECTRUM | s54_tb_hamiltonian.npz, s54_scale_factor.npz | None |
| W0-2 NEFF | s54_tb_hamiltonian.npz, s54_scale_factor.npz | None (can use W0-1 inline) |
| W0-3 CBA-SOUND | s54_tb_hamiltonian.npz | None (can use W0-1 inline) |
| W0-4 BKT-TEST | s54_tb_hamiltonian.npz, s54_scale_factor.npz | None (can use W0-1 inline) |
| W1-1 ROTOR-MF | s54_tb_hamiltonian.npz, s54_scale_factor.npz, s55_pair_mobility.npz | None (W0 results are informative but not required) |
| W1-2 FABRIC-INTEG | s54_tb_hamiltonian.npz, s54_ed_sweep.npz, s27_multisector_bcs.npz | None |
| W1-3 NPAIR3-ED | s54_tb_hamiltonian.npz, s54_ed_sweep.npz, s27_multisector_bcs.npz | None |
| W1-4 MU-JOSEPHSON | s54_tb_hamiltonian.npz, s55_sf_sign.npz | None |
| W2-1 EUCLID-FABRIC | s55_euclid.npz, s55_euclid_continuum.npz | W0-1, W1-1 |
| W2-2 PVAC-FABRIC | s55_volovik_identity.npz | W1-1, W1-2 |
| W2-3 STRUTINSKY-FABRIC | s54_tb_hamiltonian.npz | W0-1 |
| W2-4 LEGGETT-FABRIC | s54_tb_hamiltonian.npz | W0-1 (for comparison) |
| W3-1 ATENSOR-FRUST | s55_atensor_gauge.npz, s54_connes_latt.npz, s54_tb_hamiltonian.npz | None |
| W3-2 POST-TRANSIT-COH | s54_scale_factor.npz, s54_tb_hamiltonian.npz, s55_volovik_identity.npz | None |
| W3-3 NS-FABRIC | s54_scale_factor.npz | W0-1, W0-3 |
| W3-4 SPECTRAL-DIM-FLOW | s54_graph_laplacian_ds.npz, s54_tb_hamiltonian.npz | None |
| W3-5 EJ-UNCERTAINTY | s54_tb_hamiltonian.npz, s55_erich_continuum.npz | None |
| W3-6 GGE-FABRIC | s55_volovik_identity.npz | W1-2 |
| W3-7 OMEGA-ATT-CONFIRM | s54_tb_hamiltonian.npz | None |
| W3-8 MASS-VARIATION | s54_tb_hamiltonian.npz | None |

---

## IX. Pre-Registered Gates (consolidated)

| Gate ID | Description | Criterion | Priority |
|:--------|:-----------|:----------|:---------|
| **FABRIC-STABILIZATION-56** | **MASTER**: Does F_fabric(tau) have a fold minimum? | Min in [0.10, 0.30], barrier > 1% | MASTER |
| FABRIC-FREE-ENERGY-56 | Quantum rotor MF + BA + BCS on 32 cells | Min in [0.10, 0.30], barrier > 1% | 1 |
| FABRIC-INTEGRABILITY-56 | 2-cell Josephson-coupled <r> | <r> > 0.48 | 2 |
| NPAIR3-ED-56 | Single-cell N_pair=3 level statistics | <r> >= 0.53 (GOE) | 3 |
| MU-SHIFT-56 | Effective mu from inter-cell coupling | |mu_eff| > 0.1 M_KK | 4 |
| BA-SPECTRUM-56 | BA phonon spectrum characterization | INFO | W0 |
| NEFF-56 | Effective mode count | INFO (N_eff < 100 flags "mode count wins" failure) | W0 |
| CBA-SOUND-56 | Bogoliubov sound velocity | INFO | W0 |
| BKT-CROSSING-56 | T_BKT vs T_GH crossing | INFO (crossing in [0.05, 0.40]) | W0 |
| EUCLID-FABRIC-56 | Gap-corrected fabric Euclidean F | INFO (cross-check W1-1) | W2 |
| FABRIC-PVAC-56 | Volovik vacuum pressure on fabric | INFO (|P_vac_fabric| < |P_vac_cell|) | W2 |
| STRUTINSKY-FABRIC-56 | Shell correction gradient ratio on fabric | INFO (ratio vs 0.71) | W2 |
| LEGGETT-FABRIC-56 | Leggett mode dispersion | INFO (real c_L > 0) | W2 |
| ATENSOR-FRUSTRATION-56 | A-tensor gauge frustration | INFO | W3 |
| POST-TRANSIT-COH-56 | Post-transit E_J/H | INFO (E_J/H > 1?) | W3 |
| NS-FABRIC-56 | Spectral index from fabric | INFO (n_s in [0.93, 0.99]?) | W3 |
| SPECTRAL-DIM-FLOW-56 | d_s(E) profile with thresholds | INFO | W3 |
| EJ-UNCERTAINTY-56 | Error bars on E_J, E_J/E_c, omega_J | INFO | W3 |
| GGE-FABRIC-56 | GGE on 2-cell coupled system | INFO | W3 |
| OMEGA-ATT-CONFIRM-56 | omega_att = 9*(B3-B1) tau-sweep | INFO | W3 |
| MASS-VARIATION-56 | Paper 16 eq 7.1 dm_k/dtau | INFO | W3 |

---

## X. Provenance: Which Collab Suggested What

Every computation in this plan traces to a specific collab review. Nothing deferred.

| Computation | Primary Source | Supporting Sources |
|:-----------|:-------------|:------------------|
| W0-1 BA-SPECTRUM | QA Section 3.2 | Naz Section 4, QF Section 4 |
| W0-2 NEFF | QA Section 3.4 | Naz Section 4.1 |
| W0-3 CBA-SOUND | QA Section 5.2 | QA Section 4.2 |
| W0-4 BKT-TEST | QA Section 3.5 | QF Pattern 2 |
| W1-1 ROTOR-MF | All 6 unanimous | Master synthesis Priority 1 |
| W1-2 FABRIC-INTEG | Vol C2 | QF Pattern 5, Ein Section 5.1 |
| W1-3 NPAIR3-ED | Naz Section 5.1 | Ein Section 5.1, Vol C2 |
| W1-4 MU-JOSEPHSON | QA Section 5.4 | Vol Section 3, Naz Priority 3 |
| W2-1 EUCLID-FABRIC | QF Section 4 | Naz Section 4.2 |
| W2-2 PVAC-FABRIC | Vol C3 | QF Section 2 |
| W2-3 STRUTINSKY-FABRIC | Naz Section 5.1 (#3) | |
| W2-4 LEGGETT-FABRIC | Vol C5 | |
| W3-1 ATENSOR-FRUST | Bap Section 5.3 | QF Pattern 4 |
| W3-2 POST-TRANSIT-COH | Ein Section 3.3 | |
| W3-3 NS-FABRIC | Ein Section 3.2, 5.3 | |
| W3-4 SPECTRAL-DIM-FLOW | QF Pattern 3 | |
| W3-5 EJ-UNCERTAINTY | Naz Section 5.3 | |
| W3-6 GGE-FABRIC | Vol C3 (expanded) | QF Pattern 5 |
| W3-7 OMEGA-ATT-CONFIRM | QF (S38 follow-up) | |
| W3-8 MASS-VARIATION | Bap Section 4 (#4) | |

---

## XI. What Success Looks Like

**If FABRIC-STABILIZATION-56 PASSES**: The 55-session stabilization search is resolved. The collective modes of a superfluid Josephson array on Jensen-deformed SU(3) provide the free energy minimum that single-cell physics cannot. The mechanism is identified by which term in F_fabric dominates. The framework transitions from "searching for stabilization" to "characterizing the stable state."

**If FABRIC-STABILIZATION-56 FAILS**: The single-cell monotonicity extends to the fabric at mean-field level. Two paths remain:
1. Beyond-mean-field corrections (quantum rotor fluctuations, vortex-antivortex contributions, A-tensor frustration) could still produce a minimum. This is S57 territory.
2. Direction B: the dynamic transit of the superfluid as a coherent whole IS the cosmology. No static fixed point exists. The conformal diagram (S55 W3-2) already shows viable cosmology without a fixed point.

Either way, Z_fabric is characterized. The single-cell era is over. The fabric era begins with 20 computations and 21 pre-registered gates.
