# Session 49 Plan: Fabric-Cosmological Interface

**Date**: 2026-03-17
**Author**: Team-lead
**Format**: Parallel single-agent computations, 2 waves (20 + synthesis)
**Source**: session-48-wayforward.md (4 collaborative reviews: Volovik, Einstein, Schwarzschild-Penrose, Nazarewicz)
**Motivation**: S48 closed all equilibrium Goldstone mass routes. The trace theorem (S[UDU^dag]=S[D]) is a permanent wall: no spectral-action-derived potential generates mass. Q-theory self-tuning has no finite fixed point. N=1 is exact in the singlet. S49 computes the non-equilibrium alternatives (fabric-level Friedmann coupling, Bragg gap, geometric breaking) and completes the structural characterization of the tau=0.537 geometric phase transition.
**Results file**: `sessions/session-49/session-49-results-workingpaper.md`

---

## I. Session Objective

S48's 4 collaborative reviews converged on a single structural conclusion: the Goldstone mass problem and the CC problem are the same problem, and the solution lives at the fabric-cosmological interface, not at the single-cell BCS level. The trace theorem makes all on-site mass sources vanish. The self-tuning runaway has no fixed point. The mass must emerge from the 32-cell fabric coupling to 4D Friedmann dynamics.

S49 executes 20 parallel computations that test this conclusion. Tier 1 (5 computations) attacks the central questions: Friedmann-Goldstone coupling with GGE initial conditions, fabric-level pair number, Bragg gap from tessellation, geometric breaking from phase mismatch, and multi-temperature Friedmann equation. Tier 2 (6 computations) characterizes the tau=0.537 geometric phase transition and tests cavity resonance unification. Tier 3 (4 computations) refines observational predictions. Tier 4 (5 computations) completes the geometric characterization and catalogs symmetry-breaking interactions.

All 20 computations use existing S47/S48 data as input. No inter-dependencies. Single wave.

---

## II. Wave Structure

**Wave 1**: 20 parallel computations (W1-A through W1-T). All independent, all use existing S47/S48/earlier data. No ordering constraints.

**Wave 2**: Synthesis. Gate verdicts, structural results, closures, constraint map updates, next session recommendations.

---

## III. Wave 1: All Computations

### W1-A: Friedmann-Goldstone Coupling (FRIEDMANN-GOLDSTONE-49)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus

**Prompt**:

You are computing the Goldstone mass that emerges when the fabric phase field is coupled to 4D Friedmann dynamics through the superfluid density. Gate: FRIEDMANN-GOLDSTONE-49.

**Context**: S48 proved that all single-cell equilibrium mass sources vanish (trace theorem, self-tuning runaway). The Volovik review identified an 84-order scale crisis: the Josephson coupling J * K_pivot^2 ~ 3.7 M_KK^2 overwhelms m_G^2 ~ 10^{-84} M_KK^2. Even the correct mass (m ~ H_0) is drowned by the KK-scale coupling. The Einstein review requires this computation to be parameter-free: the mass must be determined entirely by rho_s, J, N_cells, and GGE initial conditions (EIH constraint). No tunable parameters.

**Method**:
1. Load the superfluid density tensor from `tier0-computation/s47_rhos_tensor.npz` and the texture correlation function from `tier0-computation/s47_texture_corr.npz`.
2. Load GGE data: Richardson-Gaudin conserved quantities from `tier0-computation/s39_richardson_gaudin.npz` and GGE Lagrange multipliers from `tier0-computation/s39_gge_lambdas.npz`.
3. Construct the Goldstone effective action on the 32-cell Josephson network: S_eff[phi] = sum_{<ij>} J_ij * rho_s * [1 - cos(phi_i - phi_j)] + kinetic terms from Friedmann coupling.
4. The Friedmann equation H^2 = (8*pi*G/3)*rho sources a damping term for the phase field. Compute the effective mass from the linearized equation of motion: m_G^2 = (rho_s * J_eff) / (M_Pl^2 * H^2) evaluated at the fold.
5. Address the 84-order crisis: the ratio J * K_pivot^2 / m_G^2 must be explained. Does the Friedmann coupling screen the Josephson energy? Does the GGE initial condition (P_exc=1, non-thermal) change the effective J?
6. Compute m_G/M_KK and m_G in GeV. Compare to H_0 = 1.438e-42 GeV and to the target range [10^{-60}, 10^{-30}] M_KK.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s47_rhos_tensor.npz` (rho_s tensor, C^2 = 7.962)
- `tier0-computation/s47_texture_corr.npz` (Josephson phase correlations, 32-cell)
- `tier0-computation/s39_richardson_gaudin.npz` (8 conserved quantities)
- `tier0-computation/s39_gge_lambdas.npz` (GGE Lagrange multipliers)
- `tier0-computation/canonical_constants.py`

**Gate**: FRIEDMANN-GOLDSTONE-49
- PASS: m_G/M_KK in [10^{-60}, 10^{-30}] with no free parameters
- INFO: computable but outside range, or requires parameter tuning
- FAIL: m_G = 0 or computation breaks down

**Output**:
- Script: `tier0-computation/s49_friedmann_goldstone.py`
- Data: `tier0-computation/s49_friedmann_goldstone.npz`
- Plot: `tier0-computation/s49_friedmann_goldstone.png`
- Working paper section: W1-A

---

### W1-B: Fabric Pair Number (FABRIC-NPAIR-49)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus

**Prompt**:

You are computing the effective Cooper pair number for the 32-cell Josephson network at N=1/cell. Gate: FABRIC-NPAIR-49.

**Context**: S48 N-PAIR-FULL confirmed N=1 exactly in the 8-mode singlet (s48_npair_full.npz). The CC crossing at tau*=0.170 requires N >= 2. The Nazarewicz review identified that the BCS-BEC crossover (N=1 per cell) transitions to weak-coupling BCS (N=32 effective) at the fabric level. The PBCS/BCS ratio improves from 0.63 (N=1) to ~0.9 (N=32). The q-theory CC crossing shortfall shrinks from 2.5x to 1.7x. Compute this quantitatively.

**Method**:
1. Load S48 pair number results from `tier0-computation/s48_npair_full.npz`.
2. Load texture correlations from `tier0-computation/s47_texture_corr.npz` (Josephson coupling matrix J_ij).
3. Load q-theory self-consistent data from `tier0-computation/s46_qtheory_selfconsistent.npz`.
4. Construct the 32-cell BCS problem: each cell has N=1 pair, cells are Josephson-coupled. Compute the effective N_pair from the fabric-level BCS wavefunction (product of cell wavefunctions with inter-cell coherence).
5. Evaluate PBCS/BCS ratio at N_eff = 32. Compare to N_eff = 1 (ratio 0.63 from S48).
6. Recompute the q-theory CC crossing condition rho_q(tau*) = rho_Lambda at fabric-level N_eff. Does the crossing occur? At what tau*?
7. Nuclear benchmark: compare to pair transfer in nuclear chains (sd-shell).

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_npair_full.npz` (N=1 singlet result)
- `tier0-computation/s47_texture_corr.npz` (J_ij matrix, 32 cells)
- `tier0-computation/s46_qtheory_selfconsistent.npz` (q-theory self-consistent solution)
- `tier0-computation/canonical_constants.py`

**Gate**: FABRIC-NPAIR-49
- PASS: N_eff >= 2 at fabric level AND CC crossing shortfall < 1.5x
- INFO: N_eff >= 2 but crossing shortfall > 1.5x
- FAIL: N_eff = 1 persists at fabric level

**Output**:
- Script: `tier0-computation/s49_fabric_npair.py`
- Data: `tier0-computation/s49_fabric_npair.npz`
- Plot: `tier0-computation/s49_fabric_npair.png`
- Working paper section: W1-B

---

### W1-C: Bragg-Goldstone Gap (BRAGG-GOLDSTONE-49)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus

**Prompt**:

You are computing the Goldstone dispersion on the 32-cell phononic crystal formed by the tessellation, looking for a Bragg gap at the Brillouin zone boundary. Gate: BRAGG-GOLDSTONE-49.

**Context**: The Tesla review identified that the 32-cell tessellation is a phononic crystal for Goldstone waves. The Z_3 domain walls have impedance contrast sigma = 4.50 M_KK (from s48_aniso_oz.npz). In any 1D phononic crystal, impedance mismatch at periodic boundaries opens a Bragg gap at k = pi/a (Brillouin zone boundary). If the Goldstone mode has a Bragg gap, the effective mass is m_G = sqrt(omega_gap) without requiring explicit symmetry breaking.

**Method**:
1. Load the curvature extension data from `tier0-computation/s48_curv_extend.npz` (sectional curvatures across tau).
2. Load the texture correlations from `tier0-computation/s47_texture_corr.npz` (cell geometry, Josephson couplings).
3. Load the anisotropic Ornstein-Zernike data from `tier0-computation/s48_aniso_oz.npz` (wall impedance sigma = 4.50 M_KK, correlation lengths).
4. Construct the 1D transfer matrix for Goldstone wave propagation through the periodic cell structure. Each cell has phase velocity c_in, walls have impedance Z_wall = sigma * Z_bulk.
5. Compute the dispersion relation omega(k) by diagonalizing the Bloch Hamiltonian across the 1D Brillouin zone.
6. Extract the Bragg gap: Delta_omega at k = pi/a. Convert to effective mass: m_Bragg = Delta_omega / (2 * c_Goldstone).
7. Compare m_Bragg/M_KK to the target range [10^{-60}, 10^{-30}].
8. Check: does the gap survive disorder? The 32-cell tessellation is not perfectly periodic. Compute the gap with 10% random variation in cell sizes.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_curv_extend.npz` (curvature data, Z_3 wall structure)
- `tier0-computation/s47_texture_corr.npz` (cell geometry)
- `tier0-computation/s48_aniso_oz.npz` (wall impedance sigma=4.50, O-Z correlation)
- `tier0-computation/canonical_constants.py`

**Gate**: BRAGG-GOLDSTONE-49
- PASS: Bragg gap produces m_Bragg/M_KK in [10^{-60}, 10^{-30}]
- INFO: gap exists but outside target range
- FAIL: no gap (impedance contrast too weak) or gap at KK scale (too large)

**Output**:
- Script: `tier0-computation/s49_bragg_goldstone.py`
- Data: `tier0-computation/s49_bragg_goldstone.npz`
- Plot: `tier0-computation/s49_bragg_goldstone.png` (dispersion relation with gap)
- Working paper section: W1-C

---

### W1-D: Geometric Breaking from Phase Mismatch (GEOMETRIC-BREAKING-49)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus

**Prompt**:

You are computing the explicit U(1)_7 breaking parameter epsilon from WKB tunneling between the fold (tau=0.19) and the post-transition regime (tau > 0.537). Gate: GEOMETRIC-BREAKING-49.

**Context**: The Nazarewicz review proposed a new mass mechanism: if two vacua exist (fold at tau=0.19 and post-transition at tau > 0.537), their BCS condensate phases are independent. The phase mismatch is an explicit breaking of U(1)_7 (the global phase rotation is not a symmetry when two disconnected vacua are present). The breaking parameter epsilon comes from WKB tunneling through the curvature barrier between the two regimes. Nuclear analog: proton-neutron phase mismatch at high spin (proton and neutron superfluids decouple at the backbending point).

**Method**:
1. Load curvature data from `tier0-computation/s48_curv_extend.npz` (sectional curvatures, Ricci eigenvalues across tau in [0, 1]).
2. Load the off-Jensen Hessian from `tier0-computation/s40_hessian_offjensen.npz` (curvature barrier height and width).
3. Load GCM zero-point energy from `tier0-computation/s46_gcm_zero_point.npz` (quantum corrections to barrier).
4. Identify the curvature barrier between tau=0.19 (fold) and tau=0.537 (geometric phase transition). Extract barrier height V_barrier and width Delta_tau.
5. Compute the WKB tunneling amplitude: T = exp(-2 * integral[sqrt(2*M*V(tau))] dtau) where M is the ATDHFB collective mass from canonical_constants (M_ATDHFB = 1.695).
6. The explicit breaking parameter: epsilon = T * Delta_phi where Delta_phi is the phase mismatch (maximum pi for completely independent condensates).
7. The Goldstone mass from explicit breaking: m_G^2 = epsilon * f_pi^2 where f_pi is the decay constant (related to rho_s).
8. Compare m_G/M_KK to target range. Nuclear benchmark: compare epsilon to proton-neutron phase mismatch in ^158Er at the backbending point.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_curv_extend.npz` (curvature across tau, transition at 0.537)
- `tier0-computation/s40_hessian_offjensen.npz` (barrier structure)
- `tier0-computation/s46_gcm_zero_point.npz` (quantum corrections)
- `tier0-computation/canonical_constants.py`

**Gate**: GEOMETRIC-BREAKING-49
- PASS: epsilon > 0 and m_G/M_KK in [10^{-60}, 10^{-30}]
- INFO: epsilon > 0 but m_G outside range
- FAIL: barrier is zero (no tunneling suppression) or epsilon = 0

**Output**:
- Script: `tier0-computation/s49_geometric_breaking.py`
- Data: `tier0-computation/s49_geometric_breaking.npz`
- Plot: `tier0-computation/s49_geometric_breaking.png` (barrier profile + tunneling amplitude)
- Working paper section: W1-D

---

### W1-E: Multi-Temperature Friedmann Equation (MULTI-T-FRIEDMANN-49)

**Agent**: `einstein-theorist`
**Model**: opus

**Prompt**:

You are computing the modified Friedmann equation for the 8-temperature GGE relic, including the negative Euler pressure contribution. Gate: MULTI-T-FRIEDMANN-49.

**Context**: The Einstein review identified that the post-transit state is a GGE with 8 distinct temperatures (Richardson-Gaudin conserved quantities). Standard Friedmann assumes a single-temperature thermal bath with w = p/rho. The GGE has 8 independent Lagrange multipliers, and the Euler relation p = T*s - rho + mu*n fails for multi-temperature systems (negative Euler pressure, S48 W5-C). This means the standard equation of state w(z) = p(z)/rho(z) is not well-defined. The question: does the non-standard GGE thermodynamics shift w_0 from the Z-K prediction [-0.47, -0.59] toward DESI DR2?

**Method**:
1. Load the dark matter / dark energy refinement from `tier0-computation/s48_dmde_refine.npz` (w_0, w_a predictions, Z-K decomposition).
2. Load Richardson-Gaudin data from `tier0-computation/s39_richardson_gaudin.npz` (8 conserved quantities, their values).
3. Load chi-q phase data from `tier0-computation/s48_chi_q_phase.npz` (q-theory response function).
4. Construct the GGE energy-momentum tensor: T^{mu nu} = sum_{alpha=1}^{8} T^{mu nu}_alpha where each sector has its own temperature beta_alpha and energy density rho_alpha.
5. The effective pressure: p_eff = sum_alpha p_alpha(beta_alpha). Compute p_alpha for each Richardson-Gaudin sector.
6. Solve the modified Friedmann equation: H^2 = (8*pi*G/3) * sum_alpha rho_alpha(a) with sector-specific scale factor dependence rho_alpha(a) ~ a^{-3(1+w_alpha)}.
7. Extract the effective w_0 and w_a from the combined expansion history. Compare to single-temperature prediction and to DESI DR2 (w_0 = -0.727 +/- 0.067).

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_dmde_refine.npz` (current w_0, w_a predictions)
- `tier0-computation/s39_richardson_gaudin.npz` (8 conserved quantities)
- `tier0-computation/s48_chi_q_phase.npz` (q-theory chi response)
- `tier0-computation/canonical_constants.py`

**Gate**: MULTI-T-FRIEDMANN-49
- PASS: |w_0(GGE) - w_0(DESI)| < |w_0(single-T) - w_0(DESI)| (GGE moves prediction toward data)
- INFO: computable but shift is < 1% (negligible)
- FAIL: GGE thermodynamics moves w_0 away from data

**Output**:
- Script: `tier0-computation/s49_multi_t_friedmann.py`
- Data: `tier0-computation/s49_multi_t_friedmann.npz`
- Plot: `tier0-computation/s49_multi_t_friedmann.png` (w(z) comparison: single-T vs GGE vs DESI)
- Working paper section: W1-E

---

### W1-F: Conformal Transition Penrose Diagram (CONFORMAL-TRANSITION-49)

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus

**Prompt**:

You are constructing the Penrose diagram of the internal SU(3) manifold through the geometric phase transition at tau=0.537. Gate: CONFORMAL-TRANSITION-49.

**Context**: The Schwarzschild-Penrose review elevated the tau=0.537 transition to "most geometrically significant new discovery" of S48. At this tau, the minimum sectional curvature crosses zero (positive to negative). The [0.537, 0.78] window has mixed-sign sectional curvature but the SEC still holds. The Penrose diagram of the internal manifold changes topology at this point. The analog horizon analysis (s48_volovik_string.npz, Mach 54) shows 1D sonic surfaces on T^2, not 2D trapped surfaces.

**Method**:
1. Load curvature data from `tier0-computation/s48_curv_extend.npz` (all sectional curvatures, Ricci eigenvalues, scalar curvature for tau in [0, 1]).
2. Extract the conformal structure of the (tau, theta) plane where theta parametrizes the internal direction with minimum sectional curvature.
3. Compute the conformal factor Omega(tau) such that the internal metric ds^2 = Omega^2 * ds^2_flat has the correct causal structure.
4. Identify: (a) the tau=0.537 boundary where kappa_min = 0, (b) any conformal infinity or singularity, (c) the topology change (simply connected to multiply connected?).
5. Draw the Penrose diagram: compactify the (tau, internal_angle) plane. Mark the fold (0.19), transition (0.537), and full-degeneration (0.78).
6. Classify the conformal boundary at tau=0.537: spacelike, timelike, or null? What is the Penrose-Hawking singularity classification?

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_curv_extend.npz`
- `tier0-computation/canonical_constants.py`

**Gate**: CONFORMAL-TRANSITION-49
- PASS: Penrose diagram constructed with clear conformal boundary classification at tau=0.537
- INFO: diagram constructed but boundary classification ambiguous
- FAIL: conformal structure is trivial (no topology change)

**Output**:
- Script: `tier0-computation/s49_conformal_transition.py`
- Data: `tier0-computation/s49_conformal_transition.npz`
- Plot: `tier0-computation/s49_conformal_transition.png` (Penrose diagram)
- Working paper section: W1-F

---

### W1-G: Analog Trapped Surface Classification (ANALOG-TRAPPED-49)

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus

**Prompt**:

You are classifying the theta_+/theta_- expansions at the Mach-1 contour on T^2 to determine whether the analog horizon is a trapped surface or a sonic surface. Gate: ANALOG-TRAPPED-49.

**Context**: S48 found Mach 54 analog horizons on the maximal torus T^2 of SU(3) (s48_volovik_string.npz). The SP review classified these as 1D sonic surfaces, not 2D trapped surfaces, but this must be verified by computing the null expansion scalars theta_+/- in the Akama-Diakonov formalism.

**Method**:
1. Load the Volovik string data from `tier0-computation/s48_volovik_string.npz` (Mach number profile on T^2, Akama-Diakonov acoustic metric).
2. At each point on the Mach-1 contour, compute the outgoing and ingoing null expansions theta_+ and theta_- using the acoustic metric g_{mu nu}^{acoustic}.
3. Classification: (a) trapped surface if theta_+ < 0 AND theta_- < 0, (b) marginally trapped if theta_+ = 0 AND theta_- < 0, (c) sonic surface (untrapped) if theta_+ = 0 but theta_- > 0 or theta_+*theta_- < 0.
4. Compute the surface gravity kappa at the Mach-1 contour: kappa = |d(Mach)/dn| * c_s where n is the normal direction.
5. Is the horizon degenerate (kappa = 0) or non-degenerate?
6. Construct the (1+1)D Penrose diagram if the surface is sonic (not trapped).

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_volovik_string.npz` (Mach number, acoustic metric on T^2)
- `tier0-computation/canonical_constants.py`

**Gate**: ANALOG-TRAPPED-49
- PASS: classification unambiguous (trapped OR sonic, with theta_+/- computed)
- INFO: classification requires higher resolution or depends on acoustic metric details
- FAIL: Mach-1 contour not well-defined

**Output**:
- Script: `tier0-computation/s49_analog_trapped.py`
- Data: `tier0-computation/s49_analog_trapped.npz`
- Plot: `tier0-computation/s49_analog_trapped.png` (theta_+/- along Mach-1 contour)
- Working paper section: W1-G

---

### W1-H: Leggett Mode Transit Dynamics (LEGGETT-TRANSIT-49)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus

**Prompt**:

You are coupling the Leggett equation of motion to the modulus dynamics tau(t) during the transit, computing the post-transit amplitude and testing whether the Leggett mode produces a 9th conserved integral. Gate: LEGGETT-TRANSIT-49.

**Context**: S48 found sharp Leggett modes at omega_L = {0.070, 0.107} M_KK (s48_leggett_mode.npz). The Nazarewicz review recognized these as multi-band pairing vibrations (Broglia analog) and proposed that the relative phase between B2 and B3 sectors may add a 9th conserved integral to the 8-integral GGE. During the transit (dt_transit ~ 0.0011 M_KK^{-1}), the Leggett mode is driven by the time-dependent gap.

**Method**:
1. Load Leggett mode data from `tier0-computation/s48_leggett_mode.npz` (omega_L1, omega_L2, mode structure, coupling constants).
2. Load integrability check from `tier0-computation/s39_integrability_check.npz` (8 Richardson-Gaudin conserved quantities).
3. Write the coupled equations: (a) Leggett EOM: d^2(phi_rel)/dt^2 + gamma * d(phi_rel)/dt + omega_L^2(tau(t)) * sin(phi_rel) = driving(tau(t)), (b) tau(t) follows the ballistic transit from S38 (v_terminal, dt_transit from canonical_constants).
4. Integrate from pre-transit (phi_rel = 0, condensate phase locked) through the transit to post-transit.
5. Compute the post-transit Leggett amplitude A_L = max|phi_rel(t > t_transit)|.
6. Test 9th integral: compute {I_9, H_BCS} where I_9 = (N_B2 - N_B3)^2 + (relative phase terms). If the Poisson bracket vanishes (or is small), I_9 is approximately conserved.
7. What is the Leggett mode's fate when P_exc = 1 (all pairs broken)? Does a Leggett-like oscillation survive as a collective mode of the quasiparticle gas?

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_leggett_mode.npz` (Leggett frequencies, coupling)
- `tier0-computation/s39_integrability_check.npz` (8 conserved quantities)
- `tier0-computation/canonical_constants.py`

**Gate**: LEGGETT-TRANSIT-49
- PASS: post-transit amplitude A_L > 0.01 AND 9th integral approximately conserved ({I_9, H}/|E_cond| < 0.1)
- INFO: A_L > 0 but 9th integral not conserved, or Leggett mode destroyed by transit
- FAIL: Leggett mode is trivially zero post-transit

**Output**:
- Script: `tier0-computation/s49_leggett_transit.py`
- Data: `tier0-computation/s49_leggett_transit.npz`
- Plot: `tier0-computation/s49_leggett_transit.png` (phi_rel(t) through transit)
- Working paper section: W1-H

---

### W1-I: Self-Consistent HFB Backreaction (HFB-BACKREACTION-49)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus

**Prompt**:

You are computing the fully self-consistent Dirac-BCS iteration where the pairing gap modifies D_K which modifies the pairing gap. Gate: HFB-BACKREACTION-49.

**Context**: S48 established that HFB converges (s48_hfb_selfconsist.npz) and BCS is a 5% perturbation on geometry. The backreaction was estimated at 3.7% (S38). This computation closes the loop: Delta(tau) modifies the Dirac spectrum eigenvalues, which modifies the DOS, which modifies the BCS gap equation solution, which modifies Delta.

**Method**:
1. Load the HFB self-consistency data from `tier0-computation/s48_hfb_selfconsist.npz` (converged gap, iteration count, convergence history).
2. Load the DOS at multiple tau from `tier0-computation/s44_dos_tau.npz`.
3. Load the Dirac spectrum construction from `tier0-computation/tier1_dirac_spectrum.py` (or reconstruct eigenvalues from s44_dos_tau.npz).
4. Implement the full self-consistent loop:
   - Start with Delta_0 from BCS (no backreaction)
   - Compute D_K(Delta) = D_K + Delta * (pairing field in Peter-Weyl)
   - Diagonalize to get new eigenvalues {lambda_k(Delta)}
   - Solve BCS gap equation with new eigenvalues: Delta_new = -V * sum_k Delta_k / (2*E_k)
   - Iterate until |Delta_new - Delta_old| / |Delta_old| < 1e-8
5. Compare: Delta_selfconsistent vs Delta_no_backreaction. Quantify the shift in E_cond, in the CC crossing tau*, and in the Thouless parameter M_max.
6. The 3.7% estimate from S38: confirm or revise.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_hfb_selfconsist.npz` (HFB convergence data)
- `tier0-computation/s44_dos_tau.npz` (Dirac spectrum at multiple tau)
- `tier0-computation/canonical_constants.py`

**Gate**: HFB-BACKREACTION-49
- PASS: self-consistent iteration converges AND backreaction < 10% on all observables (E_cond, M_max, tau*)
- INFO: converges but backreaction > 10%
- FAIL: iteration does not converge

**Output**:
- Script: `tier0-computation/s49_hfb_backreaction.py`
- Data: `tier0-computation/s49_hfb_backreaction.npz`
- Plot: `tier0-computation/s49_hfb_backreaction.png` (convergence history + observable shifts)
- Working paper section: W1-I

---

### W1-J: Cavity Resonance Unification (CAVITY-RESONANCE-49)

**Agent**: `tesla-resonance`
**Model**: opus

**Prompt**:

You are computing the normal modes of the analog cavity bounded by the Mach-1 horizon and testing whether they match the Leggett frequencies. Gate: CAVITY-RESONANCE-49.

**Context**: The Tesla review proposed cavity resonance unification: if the analog horizon (Mach 54 on T^2, from s48_volovik_string.npz) confines quasiparticles, the normal modes of this cavity should be determined by the cavity geometry alone. If the Leggett frequencies omega_L = {0.070, 0.107} M_KK match cavity normal modes, the Leggett modes are cavity resonances of the internal analog spacetime.

**Method**:
1. Load the Volovik string data from `tier0-computation/s48_volovik_string.npz` (Mach number profile, cavity geometry on T^2).
2. Load Leggett mode data from `tier0-computation/s48_leggett_mode.npz` (omega_L1, omega_L2).
3. Extract the cavity geometry: the region where Mach > 1 defines the acoustic black hole interior. The boundary (Mach = 1) is the cavity wall.
4. Compute the normal modes of a scalar field in the cavity with Dirichlet boundary conditions at the Mach-1 surface: -nabla^2 phi = omega_n^2 phi, where nabla^2 is the Laplacian in the acoustic metric restricted to the cavity.
5. Compare omega_n to omega_L1 and omega_L2. Compute the matching ratio: R = omega_cavity / omega_Leggett for the closest modes.
6. If R is within 10%: the Leggett modes ARE cavity resonances. If not: they are distinct phenomena.
7. Compute the cavity Q-factor (quality factor) from the impedance mismatch at the boundary.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_volovik_string.npz` (Mach profile, acoustic metric)
- `tier0-computation/s48_leggett_mode.npz` (Leggett frequencies)
- `tier0-computation/canonical_constants.py`

**Gate**: CAVITY-RESONANCE-49
- PASS: |omega_cavity - omega_Leggett| / omega_Leggett < 0.10 for at least one mode pair
- INFO: modes exist but matching > 10%
- FAIL: no confined modes (cavity is open or does not support standing waves)

**Output**:
- Script: `tier0-computation/s49_cavity_resonance.py`
- Data: `tier0-computation/s49_cavity_resonance.npz`
- Plot: `tier0-computation/s49_cavity_resonance.png` (cavity mode spectrum vs Leggett lines)
- Working paper section: W1-J

---

### W1-K: Gauss-Codazzi at Transition (GAUSS-CODAZZI-TRANSITION-49)

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus

**Prompt**:

You are computing the extrinsic curvature K_ij at the tau=0.537 transition hypersurface and its backreaction on the 4D Einstein tensor through the Gauss-Codazzi equations. Gate: GAUSS-CODAZZI-TRANSITION-49.

**Context**: The geometric phase transition at tau=0.537 changes the sign of minimum sectional curvature. The Gauss-Codazzi equations relate the internal curvature change to the 4D Einstein tensor. If the extrinsic curvature K_ij is discontinuous at tau=0.537, there is a distributional stress-energy on the transition hypersurface (Israel junction conditions).

**Method**:
1. Load curvature data from `tier0-computation/s48_curv_extend.npz` (all curvature invariants across tau).
2. Load Kretschner scalar from `tier0-computation/s45_kretschner.npz`.
3. Compute the extrinsic curvature K_ij of the tau=0.537 hypersurface embedded in the 10D product M^4 x SU(3).
4. Apply the Gauss-Codazzi equations: G^{(4)}_{mu nu} = ... + K^2 terms + projection of internal Riemann tensor.
5. Evaluate the jump [K_ij] across tau=0.537. If nonzero, compute the surface stress-energy S_{ij} from Israel junction conditions: S_{ij} = -(1/8*pi*G) * ([K_ij] - [K]*h_ij).
6. What does the 4D observer see? Energy density? Pressure? Does it look like a phase transition in the expansion history?

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_curv_extend.npz`
- `tier0-computation/s45_kretschner.npz`
- `tier0-computation/canonical_constants.py`

**Gate**: GAUSS-CODAZZI-TRANSITION-49
- PASS: K_ij computed, [K_ij] jump quantified, 4D backreaction characterized
- INFO: K_ij computed but jump is continuous (no distributional source)
- FAIL: computation ill-defined at transition point

**Output**:
- Script: `tier0-computation/s49_gauss_codazzi.py`
- Data: `tier0-computation/s49_gauss_codazzi.npz`
- Plot: `tier0-computation/s49_gauss_codazzi.png` (K_ij components across transition)
- Working paper section: W1-K

---

### W1-L: Bayesian alpha_s Uncertainty (ALPHA-S-BAYES-49)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus

**Prompt**:

You are computing the Bayesian uncertainty on the spectral tilt alpha_s = -0.038 by propagating the J_ij coupling errors through the prediction. Gate: ALPHA-S-BAYES-49.

**Context**: The framework predicts alpha_s = -0.038 (running of spectral tilt), which is 4.9 sigma from Planck (alpha_s = 0.0 +/- 0.008). The Nazarewicz review proposed that the J_ij Josephson couplings carry uncertainties from the BCS solution and the tessellation geometry. Propagating these uncertainties through the alpha_s prediction may broaden the error band enough to reduce the tension with Planck.

**Method**:
1. Load anisotropic O-Z data from `tier0-computation/s48_aniso_oz.npz` (J_ij values, correlation lengths, alpha_s prediction).
2. Load the Bayesian GP posterior from `tier0-computation/s46_bayesian_gp.npz` (Gaussian process fit to n_s(tau), uncertainty bands).
3. Construct the J_ij error model: each J_ij has uncertainty delta_J from (a) BCS gap uncertainty, (b) tessellation geometry uncertainty, (c) finite-size effects.
4. Monte Carlo propagation: sample J_ij from their posterior distributions (N=10000 samples), compute alpha_s for each sample, build the posterior P(alpha_s | data).
5. Report: (a) median alpha_s, (b) 68% credible interval, (c) 95% credible interval.
6. Does the 95% interval include alpha_s = 0 (Planck)? What is the Bayesian tension (number of sigma)?
7. If tension persists: what J_ij uncertainty would be needed to reach 2-sigma compatibility?

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_aniso_oz.npz` (J_ij, alpha_s = -0.038)
- `tier0-computation/s46_bayesian_gp.npz` (GP posterior on n_s)
- `tier0-computation/canonical_constants.py`

**Gate**: ALPHA-S-BAYES-49
- PASS: 95% credible interval includes alpha_s = 0 (compatible with Planck)
- INFO: tension reduced but still > 2 sigma
- FAIL: error band negligible, tension unchanged at 4.9 sigma

**Output**:
- Script: `tier0-computation/s49_alpha_s_bayes.py`
- Data: `tier0-computation/s49_alpha_s_bayes.npz`
- Plot: `tier0-computation/s49_alpha_s_bayes.png` (posterior P(alpha_s) vs Planck band)
- Working paper section: W1-L

---

### W1-M: 3-Component Kibble-Zurek (KZ-3COMPONENT-49)

**Agent**: `gen-physicist`
**Model**: opus

**Prompt**:

You are sharpening the KZ defect density prediction by using the 3-component formula that separates the u(1) channel from the su(2) channels. Gate: KZ-3COMPONENT-49.

**Context**: S48 confirmed the KZ-aniso match to S38 at 6.5% (s48_curv_extend.npz). The Tesla review noted that the standard KZ formula treats all 8 BCS modes identically. The physical system has u(1)_7 (1 mode) and su(2) (remaining modes). Their critical exponents may differ. The 3-component formula: n_KZ = n_{u(1)} + n_{su(2)_1} + n_{su(2)_2} with separate tau_Q and nu for each component.

**Method**:
1. Load KZ data from `tier0-computation/s48_curv_extend.npz` (curvature-derived quench rates, defect density prediction).
2. Separate the 8 BCS modes into: 1 u(1)_7 mode (B1, K_7 charge) and 7 remaining modes (4 B2 + 3 B3).
3. For each component, compute the critical exponents: nu (correlation length), z (dynamic), from the spectral gap closing rate near tau_fold.
4. 3-component KZ formula: n_i = (tau_Q_i)^{-d*nu_i/(1+z_i*nu_i)} for each component i.
5. Total defect density: n_total = sum_i n_i.
6. Compare to the 1-component result (6.5% match to S38). Does the 3-component formula give < 3% match?
7. Report the fractional improvement and the component-resolved contributions.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_curv_extend.npz` (KZ data, curvature, quench rates)
- `tier0-computation/canonical_constants.py`

**Gate**: KZ-3COMPONENT-49
- PASS: 3-component match to S38 < 3%
- INFO: improvement over 1-component but still > 3%
- FAIL: 3-component prediction worse than 1-component

**Output**:
- Script: `tier0-computation/s49_kz_3component.py`
- Data: `tier0-computation/s49_kz_3component.npz`
- Plot: `tier0-computation/s49_kz_3component.png` (component-resolved KZ vs total)
- Working paper section: W1-M

---

### W1-N: Leggett-Phi Scan (LEGGETT-PHI-SCAN-49)

**Agent**: `tesla-resonance`
**Model**: opus

**Prompt**:

You are scanning the Leggett frequency ratio omega_L2/omega_L1 across tau to test whether it converges to phi_paasch = 1.531580 at any deformation. Gate: LEGGETT-PHI-SCAN-49.

**Context**: S48 found omega_L2/omega_L1 = 1.529, which is 0.17% from phi_paasch. The Tesla review flagged this as likely coincidence given V-matrix uncertainties, but proposed a decisive test: scan the ratio across tau. If it converges to phi_paasch at some tau (not necessarily the fold), there is a structural connection. If the ratio varies smoothly and 1.529 is just the fold value, it is a coincidence.

**Method**:
1. Load Leggett mode data from `tier0-computation/s48_leggett_mode.npz` (omega_L1, omega_L2 at the fold, mode structure, V-matrix elements).
2. Reconstruct the Leggett mode calculation at tau = {0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50} using the tau-dependent Dirac spectrum and V-matrix.
3. At each tau, compute omega_L1, omega_L2, and the ratio R(tau) = omega_L2/omega_L1.
4. Compare R(tau) to phi_paasch = 1.531580 at each tau. Find the minimum |R(tau) - phi_paasch|.
5. Classification: (a) if R(tau) = phi_paasch exactly at some tau (to within V-matrix uncertainty), there is a structural connection. (b) If R(tau) varies monotonically and the fold value happens to be close, coincidence. (c) If R(tau) has a minimum distance to phi_paasch at the fold, suggestive but not decisive.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_leggett_mode.npz` (Leggett mode data at fold)
- `tier0-computation/canonical_constants.py`

**Gate**: LEGGETT-PHI-SCAN-49
- PASS: R(tau) = phi_paasch to within 0.1% at some tau (structural connection)
- INFO: closest approach < 1% but no exact match
- FAIL: R(tau) varies smoothly, no special relationship to phi_paasch

**Output**:
- Script: `tier0-computation/s49_leggett_phi_scan.py`
- Data: `tier0-computation/s49_leggett_phi_scan.npz`
- Plot: `tier0-computation/s49_leggett_phi_scan.png` (R(tau) vs phi_paasch horizontal line)
- Working paper section: W1-N

---

### W1-O: DESI DR3 Preparation (DESI-DR3-PREP-49)

**Agent**: `gen-physicist`
**Model**: opus

**Prompt**:

You are computing the Bayes factor for the framework vs LCDM at the corrected alpha_s range, preparing a quantitative prediction for DESI DR3 comparison. Gate: DESI-DR3-PREP-49.

**Context**: S48 refined the dark energy prediction (s48_dmde_refine.npz): w_0 in [-0.47, -0.59] with the Z-K decomposition discrepancy at 39.4%. DESI DR2 reports w_0 = -0.727 +/- 0.067. The framework prediction is 2.8 sigma from DESI. DR3 data (expected 2026-2027) will sharpen the constraint. Compute the Bayes factor B_{framework/LCDM} to quantify whether the data already excludes the framework or is still compatible.

**Method**:
1. Load the dark energy prediction from `tier0-computation/s48_dmde_refine.npz` (w_0, w_a, uncertainty bands from Z-K discrepancy).
2. Construct the framework likelihood: P(data | framework) where data = DESI DR2 w_0 = -0.727 +/- 0.067 and the framework prediction is w_0 = -0.53 +/- 0.06 (midpoint of [-0.47, -0.59] with Z-K spread as uncertainty).
3. LCDM likelihood: P(data | LCDM) where LCDM predicts w_0 = -1.0 exactly.
4. Bayes factor: B = P(data | framework) / P(data | LCDM). Also compute B against w_0w_a CDM (DESI best fit).
5. Forecast DR3: assuming DESI DR3 halves the error bar (sigma_DR3 ~ 0.035), what Bayes factor do we predict? At what sigma_w does the framework become decisively excluded (B < 1/100)?
6. Pre-register: the framework predicts w_0 = -0.53 +/- 0.06 and w_a = [value from s48_dmde_refine.npz]. Report these as the falsifiable prediction.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_dmde_refine.npz` (w_0, w_a predictions)
- `tier0-computation/canonical_constants.py`

**Gate**: DESI-DR3-PREP-49
- PASS: B_{framework/LCDM} > 1 (framework currently preferred over LCDM by DESI data)
- INFO: 1/10 < B < 1 (inconclusive)
- FAIL: B < 1/10 (framework already disfavored by DR2)

**Output**:
- Script: `tier0-computation/s49_desi_dr3_prep.py`
- Data: `tier0-computation/s49_desi_dr3_prep.npz`
- Plot: `tier0-computation/s49_desi_dr3_prep.png` (Bayes factor vs sigma_w forecast)
- Working paper section: W1-O

---

### W1-P: Cosmic Censorship During Transit (COSMIC-CENSORSHIP-49)

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus

**Prompt**:

You are testing whether the ballistic transit overshoots tau=0.537 (negative curvature regime) and whether the resulting 4D stress-energy tensor violates cosmic censorship. Gate: COSMIC-CENSORSHIP-49.

**Context**: The transit is ballistic with v_terminal = 26.5 M_KK (S38). The fold is at tau=0.19, the geometric phase transition at tau=0.537. If the transit overshoots to tau > 0.537, the internal manifold enters the negative-curvature regime. The 4D stress-energy tensor T_{mu nu} from the negative-curvature internal space may violate the dominant energy condition (DEC), which would be a cosmic censorship issue.

**Method**:
1. Load collective inertia from `tier0-computation/s40_collective_inertia.npz` (M_ATDHFB, potential landscape).
2. Load curvature data from `tier0-computation/s48_curv_extend.npz` (curvature across tau, especially tau > 0.537).
3. Compute the ballistic trajectory: M_ATDHFB * d^2(tau)/dt^2 = -dV/dtau with initial conditions from the transit (v = v_terminal at tau = 0.19).
4. Does tau(t) reach 0.537? If so, at what t? Does it overshoot or turn around?
5. At each tau along the trajectory, compute T_{mu nu}^{(4D)} from the KK reduction. In the negative-curvature regime, which energy conditions hold? NEC, WEC, SEC, DEC?
6. If DEC is violated: is a naked singularity formed? Or is the violation transient?
7. Does the overshoot produce observable signatures (gravitational wave burst, sudden change in expansion rate)?

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s40_collective_inertia.npz` (collective mass, potential)
- `tier0-computation/s48_curv_extend.npz` (curvature in negative regime)
- `tier0-computation/canonical_constants.py`

**Gate**: COSMIC-CENSORSHIP-49
- PASS: transit does NOT overshoot to tau > 0.537, or overshoots but all energy conditions hold
- INFO: overshoots, transient DEC violation but no singularity
- FAIL: permanent DEC violation or naked singularity formed

**Output**:
- Script: `tier0-computation/s49_cosmic_censorship.py`
- Data: `tier0-computation/s49_cosmic_censorship.npz`
- Plot: `tier0-computation/s49_cosmic_censorship.png` (tau(t) trajectory + energy condition status)
- Working paper section: W1-P

---

### W1-Q: Higher-D Petrov Classification (CMPP-TRANSITION-49)

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus

**Prompt**:

You are computing the CMPP (Coley-Milson-Pravda-Pravdova) higher-dimensional Petrov classification of the Weyl tensor at the tau=0.537 geometric phase transition. Gate: CMPP-TRANSITION-49.

**Context**: The 4D Petrov classification (Type I, D, O, etc.) generalizes to higher dimensions via the CMPP scheme. At tau=0.537, the internal curvature changes sign. The Weyl tensor of the 10D product space M^4 x SU(3) may change CMPP type at this point, analogous to the Petrov type change at a black hole horizon.

**Method**:
1. Load curvature data from `tier0-computation/s48_curv_extend.npz` (Riemann tensor components, Weyl tensor).
2. Load curvature anatomy from `tier0-computation/s47_curvature_anatomy.npz` (detailed decomposition of Riemann into Weyl + Ricci + scalar parts).
3. At tau = {0.50, 0.53, 0.537, 0.54, 0.55, 0.60}, compute the 10D Weyl tensor C_{abcd} from the product metric.
4. Compute the CMPP invariants: the boost weight decomposition of C_{abcd} along a null frame. Classify into CMPP types: G (general), I_i, I, D, II_i, II, III_i, III, N, O.
5. Does the CMPP type change at tau=0.537? If so, from what to what?
6. Physical interpretation: what does the CMPP type transition mean for gravitational wave propagation in the bulk?

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_curv_extend.npz`
- `tier0-computation/s47_curvature_anatomy.npz`
- `tier0-computation/canonical_constants.py`

**Gate**: CMPP-TRANSITION-49
- PASS: CMPP type changes at tau=0.537 (clear classification on both sides)
- INFO: type change occurs but at slightly different tau (within 0.01)
- FAIL: CMPP type is constant across the transition

**Output**:
- Script: `tier0-computation/s49_cmpp_transition.py`
- Data: `tier0-computation/s49_cmpp_transition.npz`
- Plot: `tier0-computation/s49_cmpp_transition.png` (CMPP invariants across transition)
- Working paper section: W1-Q

---

### W1-R: Non-Left-Invariant TT Modes (NON-LI-TT-49)

**Agent**: `spectral-geometer`
**Model**: opus

**Prompt**:

You are computing the spectrum of non-left-invariant transverse-traceless (TT) modes on Jensen-deformed SU(3) and finding the first negative eigenvalue. Gate: NON-LI-TT-49.

**Context**: S48 computed the TT Lichnerowicz operator for left-invariant modes (s48_tt_lichnerowicz.npz) and found stability (no negative eigenvalues). However, non-left-invariant modes are a larger space. The question: does the first negative eigenvalue of the Lichnerowicz operator on the full (non-LI) TT space appear at some tau, and if so, is it before or after the fold?

**Method**:
1. Load the TT Lichnerowicz data from `tier0-computation/s48_tt_lichnerowicz.npz` (left-invariant eigenvalues, operator construction).
2. Extend the computation to non-left-invariant TT modes. On SU(3), these are sections of the TT bundle that transform non-trivially under left multiplication. They can be expanded in the Peter-Weyl basis with (p,q) != (0,0).
3. For tau = {0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.537, 0.60, 0.70, 0.78}, compute the Lichnerowicz eigenvalues for the lowest non-LI TT modes (at least the (1,0) and (0,1) representations).
4. Find tau_critical: the first tau at which a Lichnerowicz eigenvalue becomes negative.
5. Is tau_critical < tau_fold (instability before the fold = problem) or tau_critical > tau_fold (instability after the fold = expected in negative-curvature regime)?
6. The negative eigenvalue signals a linearized graviton instability. Physical interpretation?

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s48_tt_lichnerowicz.npz` (LI TT eigenvalues, operator)
- `tier0-computation/canonical_constants.py`

**Gate**: NON-LI-TT-49
- PASS: first negative eigenvalue at tau > tau_fold (stability at the fold preserved)
- INFO: first negative eigenvalue very close to tau_fold (within 0.02)
- FAIL: first negative eigenvalue at tau < tau_fold (instability before the fold)

**Output**:
- Script: `tier0-computation/s49_non_li_tt.py`
- Data: `tier0-computation/s49_non_li_tt.npz`
- Plot: `tier0-computation/s49_non_li_tt.png` (lowest eigenvalue vs tau for LI and non-LI)
- Working paper section: W1-R

---

### W1-S: Dipolar Interaction Catalog (DIPOLAR-CATALOG-49)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus

**Prompt**:

You are cataloging all interactions external to the BCS Hamiltonian on SU(3) and identifying which ones break U(1)_7. Gate: DIPOLAR-CATALOG-49.

**Context**: The Volovik review identified the 3He dipolar interaction as the structural template for U(1)_7 breaking. In 3He-B, the dipole-dipole interaction (external to the BCS pairing Hamiltonian) explicitly breaks SO(3)_S x SO(3)_L to SO(3)_{S+L}, giving the Goldstone modes a mass of order 10^{-3} T_c. The question: what is the analog on SU(3)? Which interactions are "external" to the BCS Hamiltonian and which ones break U(1)_7?

**Method**:
1. Read the Volovik paper index at `researchers/Volovik/index.md` for structural templates (especially papers on dipolar interaction in 3He, q-theory, and symmetry breaking).
2. Load the Goldstone mass data from `tier0-computation/s48_goldstone_mass.npz` (confirming m=0 from spectral action).
3. Catalog all interactions on Jensen-deformed SU(3) beyond the BCS Hamiltonian:
   - (a) Gravitational backreaction: does the Einstein equation couple to K_7 charge? Does gravity break U(1)_7?
   - (b) Torsion: if the connection has torsion (from the parallelizing structure of SU(3)), does it couple differently to K_7-charged vs K_7-neutral modes?
   - (c) WZW (Wess-Zumino-Witten) term: the topological term in the SU(3) sigma model. Does it break U(1)_7?
   - (d) Spectral action higher-order terms (a_6, a_8): do they break the [iK_7, D_K] = 0 symmetry?
   - (e) Inter-cell Josephson coupling: already in the Hamiltonian, does not break U(1)_7 (it preserves global phase).
   - (f) Finite-temperature corrections: do thermal fluctuations in the GGE break U(1)_7?
4. For each candidate: (i) write the interaction term, (ii) check [interaction, K_7] = 0 or != 0, (iii) if nonzero, estimate the breaking scale epsilon/M_KK.
5. Rank by breaking strength.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `researchers/Volovik/index.md` (Volovik paper catalog for structural templates)
- `tier0-computation/s48_goldstone_mass.npz` (m=0 confirmation)
- `tier0-computation/canonical_constants.py`

**Gate**: DIPOLAR-CATALOG-49
- PASS: at least one interaction breaks U(1)_7 with computable epsilon
- INFO: candidates identified but epsilon not computable without new data
- FAIL: all interactions preserve U(1)_7

**Output**:
- Script: `tier0-computation/s49_dipolar_catalog.py`
- Data: `tier0-computation/s49_dipolar_catalog.npz`
- Plot: `tier0-computation/s49_dipolar_catalog.png` (catalog table visualization)
- Working paper section: W1-S

---

### W1-T: Leggett Mode in GGE (LEGGETT-GGE-49)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus

**Prompt**:

You are testing whether the Leggett relative phase survives as a conserved quantity in the P_exc=1 (fully excited) GGE. Gate: LEGGETT-GGE-49.

**Context**: The S38 transit produces P_exc = 1.000 (all Cooper pairs broken). The post-transit state is a GGE with 8 Richardson-Gaudin conserved quantities. The Leggett mode is a relative phase oscillation between B2 and B3 pairing gaps. In the nuclear analog, pair vibrations survive above the pairing phase transition as enhanced pair-transfer strength (Broglia-type fluctuations). Does the Leggett relative phase survive in the broken-pair GGE?

**Method**:
1. Load S38 quench data: use `tier0-computation/s38_kz_defects.npz` for the transit dynamics and `tier0-computation/s38_otoc_bcs.npz` for the post-quench state.
2. Load Leggett mode data from `tier0-computation/s48_leggett_mode.npz`.
3. Construct the GGE density matrix: rho_GGE = exp(-sum_alpha lambda_alpha * I_alpha) / Z where I_alpha are the 8 Richardson-Gaudin integrals.
4. Compute the Leggett correlation function in the GGE: C_L(t) = <phi_rel(t) * phi_rel(0)>_GGE where phi_rel is the B2-B3 relative phase.
5. If C_L(t) oscillates with a well-defined frequency, the Leggett mode survives. If C_L(t) decays to zero, the Leggett mode is destroyed.
6. Nuclear benchmark: compare to pair-transfer strength function above T_c in ^158Er (Broglia, Mottelson).
7. Does the survival of the Leggett mode add a 9th conserved quantity? Check: is phi_rel a function of the 8 existing I_alpha? If not, it is independent.

Use `from canonical_constants import *` for all constants.

**Inputs**:
- `tier0-computation/s38_kz_defects.npz` (transit dynamics)
- `tier0-computation/s38_otoc_bcs.npz` (post-quench state)
- `tier0-computation/s48_leggett_mode.npz` (Leggett mode structure)
- `tier0-computation/canonical_constants.py`

**Gate**: LEGGETT-GGE-49
- PASS: C_L(t) oscillates at omega_L for t >> 1/omega_L (Leggett survives in GGE) AND phi_rel independent of the 8 I_alpha
- INFO: C_L(t) has damped oscillations (partial survival) or phi_rel is a function of existing integrals
- FAIL: C_L(t) decays monotonically (Leggett mode destroyed)

**Output**:
- Script: `tier0-computation/s49_leggett_gge.py`
- Data: `tier0-computation/s49_leggett_gge.npz`
- Plot: `tier0-computation/s49_leggett_gge.png` (C_L(t) correlation function)
- Working paper section: W1-T

---

## IV. Constraint Gates Summary

| Gate ID | Computation | Agent | Tier | Pass Criterion |
|:--------|:-----------|:------|:-----|:---------------|
| FRIEDMANN-GOLDSTONE-49 | Friedmann-Goldstone coupling | volovik | 1 | m_G/M_KK in [10^{-60}, 10^{-30}], no free parameters |
| FABRIC-NPAIR-49 | Fabric pair number | nazarewicz | 1 | N_eff >= 2, CC shortfall < 1.5x |
| BRAGG-GOLDSTONE-49 | Bragg gap on tessellation | landau | 1 | m_Bragg/M_KK in [10^{-60}, 10^{-30}] |
| GEOMETRIC-BREAKING-49 | WKB geometric breaking | nazarewicz | 1 | epsilon > 0, m_G in target range |
| MULTI-T-FRIEDMANN-49 | 8-temperature Friedmann | einstein | 1 | GGE shifts w_0 toward DESI |
| CONFORMAL-TRANSITION-49 | Penrose diagram at 0.537 | SP | 2 | Clear conformal boundary classification |
| ANALOG-TRAPPED-49 | Analog horizon classification | SP | 2 | theta_+/- computed, classification unambiguous |
| LEGGETT-TRANSIT-49 | Leggett transit dynamics | landau | 2 | A_L > 0.01, 9th integral conserved |
| HFB-BACKREACTION-49 | Self-consistent HFB | nazarewicz | 2 | Converges, backreaction < 10% |
| CAVITY-RESONANCE-49 | Cavity mode matching | tesla | 2 | omega_cavity matches omega_Leggett < 10% |
| GAUSS-CODAZZI-TRANSITION-49 | Extrinsic curvature at 0.537 | SP | 2 | K_ij computed, 4D backreaction quantified |
| ALPHA-S-BAYES-49 | Bayesian alpha_s uncertainty | nazarewicz | 3 | 95% CI includes alpha_s = 0 |
| KZ-3COMPONENT-49 | 3-component KZ formula | gen-physicist | 3 | Match to S38 < 3% |
| LEGGETT-PHI-SCAN-49 | omega_L2/omega_L1 vs tau | tesla | 3 | R(tau) = phi_paasch within 0.1% at some tau |
| DESI-DR3-PREP-49 | Bayes factor vs LCDM | gen-physicist | 3 | B > 1 (framework preferred) |
| COSMIC-CENSORSHIP-49 | Transit overshoot test | SP | 4 | No overshoot, or energy conditions hold |
| CMPP-TRANSITION-49 | Higher-D Petrov class | SP | 4 | CMPP type changes at 0.537 |
| NON-LI-TT-49 | Non-LI TT stability | spectral-geometer | 4 | First negative eigenvalue at tau > tau_fold |
| DIPOLAR-CATALOG-49 | U(1)_7 breaking catalog | volovik | 4 | At least one interaction breaks U(1)_7 |
| LEGGETT-GGE-49 | Leggett in GGE | nazarewicz | 4 | C_L(t) oscillates, phi_rel independent |

---

## V. Execution Notes

### Agent Assignment Summary

| Agent | Computations |
|:------|:------------|
| volovik-superfluid-universe-theorist | W1-A (FRIEDMANN-GOLDSTONE), W1-S (DIPOLAR-CATALOG) |
| nazarewicz-nuclear-structure-theorist | W1-B (FABRIC-NPAIR), W1-D (GEOMETRIC-BREAKING), W1-I (HFB-BACKREACTION), W1-L (ALPHA-S-BAYES), W1-T (LEGGETT-GGE) |
| landau-condensed-matter-theorist | W1-C (BRAGG-GOLDSTONE), W1-H (LEGGETT-TRANSIT) |
| einstein-theorist | W1-E (MULTI-T-FRIEDMANN) |
| schwarzschild-penrose-geometer | W1-F (CONFORMAL-TRANSITION), W1-G (ANALOG-TRAPPED), W1-K (GAUSS-CODAZZI), W1-P (COSMIC-CENSORSHIP), W1-Q (CMPP-TRANSITION) |
| tesla-resonance | W1-J (CAVITY-RESONANCE), W1-N (LEGGETT-PHI-SCAN) |
| gen-physicist | W1-M (KZ-3COMPONENT), W1-O (DESI-DR3-PREP) |
| spectral-geometer | W1-R (NON-LI-TT) |

### Runtime Environment

- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- **Script prefix**: `s49_`
- **Output directory**: `tier0-computation/`
- **Constants**: `from canonical_constants import *` -- NEVER hardcode framework constants
- **All agents**: opus model
- **All computations**: independent, single-wave parallel execution

### Standard Protocols

- Each agent receives only its own prompt (self-contained, no cross-references)
- Gate verdicts are permanent once recorded
- Results written to the working paper at `sessions/session-49/session-49-results-workingpaper.md`
- Wave 2 synthesis after all 20 computations complete
