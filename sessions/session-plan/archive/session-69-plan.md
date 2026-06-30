# Session 69 Plan: Nice.

**Date**: 2026-04-05
**Author**: Team-lead (planner: main agent, from S68 master collab carry-forward)
**Format**: Parallel single-agent computations across 6 waves
**Source**: S68 master collab synthesis (28 deduplicated computations from 6 reviewers), S68 phonon-vs-data test suite (12 queued tests), S68 working paper results
**Motivation**: S68 established that the A_s gap is 0.755 OOM with phi_eff as the single most consequential unknown (6/6 reviewers), the 12.9x normalization mismatch as logically prior (5/6 reviewers), and ISW tracking as the nearest unique observational discriminant (6/6 reviewers). S69 answers the first two and tests the third. Additionally, the phonon-vs-data pipeline (3 executed in S68) extends to real supernova, growth rate, and CMB data.
**Results file**: `sessions/archive/session-69/session-69-results-workingpaper.md`

---

## I. Session Objective

Determine phi_eff (the squeeze phase that controls the non-BD A_s enhancement), resolve the 12.9x normalization chain mismatch, compute the ISW tracking signal at full Boltzmann level, and execute 3+ phonon-vs-data tests against real astronomical observations via the astro MCP.

The session has two tracks:
1. **Close the A_s gap's rate-limiting unknowns** — phi_eff, normalization, off-Jensen, sector-resolved BCS
2. **Stress-test the framework against real data** — SNe Ia, growth rate, angular distances, CMB power spectrum

**Pre-registered master gates**:

- **PHI-EFF-69**: PASS if enhancement in [1.3, 4.0]. INFO if [1.0, 1.3]. FAIL if < 1.0 (destructive interference).
- **AS-NORM-69**: INFO — diagnostic decomposition of the 12.9x mismatch.

---

## II. Wave Structure

### Dependency Graph

```
Wave 1 (parallel, no dependencies -- CRITICAL + HIGH):
  W1-A: PHI-EFF-BCS-BOGOL-69         W1-B: AS-NORMALIZATION-CHAIN-69
  W1-C: ISW-TRACKING-BOLTZMANN-69    W1-D: SECTOR-RESOLVED-BCS-A4-69
  W1-E: OFF-JENSEN-SA-69             W1-F: NON-BD-SQUEEZE-RECONCILED-69

    Decision Point: W1-A determines sign of non-BD correction
    Decision Point: W1-B determines whether 12.9x is bookkeeping or physics
    Decision Point: W1-C determines whether ISW tracking survives Boltzmann treatment

Wave 2 (parallel, can co-run with W1 -- consistency + data):
  W2-A: TRANSIT-CONSISTENCY-69       W2-B: SU(1,1)-PHASE-CG24-69
  W2-C: CMB-S4-NS-PREREGISTER-69    W2-D: PVD-05-FSIGMA8-69
  W2-E: PVD-04-SNE-PANTHEON-69      W2-F: PVD-13-DA-DESI-69

    Decision Point: W2-A determines how many CMB predictions are independent

Wave 3 (depends on Wave 1 results):
  W3-A: SONIC-PENROSE-INEQUALITY-69  W3-B: EUCLID-ISW-RSD-JOINT-69
  W3-C: KK-THRESHOLD-HIGGS-69       W3-D: PVD-07-PLANCK-CL-69

Wave 4 (medium refinements, no hard deps):
  W4-A: EP-TRANSIT-CORRECTION-69     W4-B: SWAMPLAND-1LOOP-69
  W4-C: CONFORMAL-ANOMALY-EPSH-69   W4-D: EUCLID-LENSING-TRACKING-69
  W4-E: SPECTRAL-DIM-BCS-PROTECTION W4-F: CONFORMAL-FACTOR-TRANSIT-69
  W4-G: BCS-DRESSED-HESSIAN-69

Wave 5 (low level + remaining data, all independent):
  W5-A through W5-P: 16 computations (lab analogs, structural, data tests)

Wave 6 (synthesis):
  W6-A: SESSION-69-ASSESSMENT
```

---

## III. Wave 1: The Squeeze and the Chain (6 parallel)

### W1-A: PHI-EFF-BCS-BOGOL-69 — Squeeze Phase Determination

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: C1 from master collab (6/6 reviewers)

**Prompt**:

Compute the BCS squeeze phase phi_eff from the coupled gap equation and Mukhanov-Sasaki mode equation at the fold. This is the single most consequential unknown in the framework — it determines whether the non-BD initial state HELPS or HURTS the A_s gap.

**Context.** The S68 Landau-Transit workshop (Tr1) discovered that the A_s enhancement from non-BD initial state is NOT simply cosh(2r_eff) but includes an interference term:

P_zeta(non-BD) = P_zeta(BD) * [cosh(2r_eff) + sinh(2r_eff) * cos(phi_eff)]

At r_eff = 0.338: enhancement ranges from 0.89 (phi_eff = pi, destructive) to 1.58 (phi_eff = 0, constructive). Three independent predictions exist:
- QA (adiabatic impedance matching): phi_eff ~ 0 (enhancement 1.58, +0.20 OOM)
- Landau (Josephson analogy): phi_eff ~ pi/4 (enhancement 1.48, +0.17 OOM)
- Phonon-First (KZ defect topology): <cos(phi_eff)> = -1/2 if Z_3 winding (partial destructive)

**Computation steps:**

1. Load BCS parameters from canonical_constants.py and the transit background from `computations/s67_transit_ps.npz`.

2. Solve the time-dependent BCS gap equation Delta(tau) through the fold. The gap transitions from ~0 (pre-transit) to Delta_0 = 0.52 (post-transit). The Landau-Transit workshop (Ld2) established that tau_relax/dt_transit = 0.003 — the gap tracks equilibrium adiabatically.

3. Compute the BCS squeeze parameter r_k and squeeze phase phi_k for each GGE branch. The squeeze parameter is r_k = arctanh(v_k/u_k) where u_k, v_k are the BCS coherence factors. The phase phi_k depends on the TDGL dynamics of Delta(tau).

4. Compute the variance-weighted effective phi_eff = sum_I f_I * phi_I where f_I are the multifield delta-N branch fractions (acoustic 3.3%, Leggett 46.2%, optical 50.6%).

5. Compute the full enhancement factor including interference: Enhancement = cosh(2r_eff) + sinh(2r_eff) * cos(phi_eff).

6. Report: phi_eff, enhancement factor, A_s correction in OOM, comparison to QA (0), Josephson (pi/4), and KZ (-1/2) predictions.

**Input files:**
- `computations/s67_transit_ps.npz`
- `computations/s67_multifield_delta_n.npz`
- `computations/s68_bcs_dressed_mode.npz`
- `computations/canonical_constants.py`

**Gate**: PHI-EFF-69
- **PASS**: Enhancement in [1.3, 4.0] (A_s gap improved by 0.11-0.60 OOM)
- **FAIL**: Enhancement < 1.0 (destructive interference, gap WORSENS)
- **INFO**: Enhancement in [1.0, 1.3] (modest, need additional channels)

**Output:**
- Script: `computations/s69_phi_eff.py`
- Data: `computations/s69_phi_eff.npz`
- Plot: `computations/s69_phi_eff.png`
- Working paper: Section W1-A

---

### W1-B: AS-NORMALIZATION-CHAIN-69 — Resolve 12.9x Mismatch

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: C2 from master collab (5/6 reviewers)

**Prompt**:

Decompose the factor 12.9 (1.11 OOM) mismatch between the direct amplitude chain (S68 W1-A: A_s from |beta_k|^2 at transit, yielding P_phys * enhancement_M1 = 4.25e-9) and the multifield delta-N chain (S67 W3-B: A_s = 3.29e-10). This mismatch is logically prior to all A_s corrections — if it's a physics effect, the gap is different than we think. Mack: "the entire gap closure budget is meaningless until this normalization is resolved."

**Computation steps:**

1. Load both chains: `s67_transit_ps.npz` (direct Bogoliubov amplitude: P_W1A = 2.56e6 M_KK units, P_phys = 2380, P_phys * M1_enhancement = 4.25e-9) and `s67_multifield_delta_n.npz` (delta-N: A_s = 3.29e-10).

2. Trace the normalization conventions at each step of both chains. Identify where factors of 2pi, M_Pl, M_KK, spectral action normalization (f_0, f_2, f_4), and volume factors enter. The S68 W1-A working paper noted: "Factor-of-13 discrepancy between chains indicates normalization convention mismatch in W3-B."

3. Decompose the 12.9x into: (a) geometric factors (2pi, volume of SU(3)), (b) mass unit conversions (M_KK/M_Pl), (c) spectral action normalization (the f_2 coefficient in S = f_0*a_0 + f_2*a_2 + ...), (d) physics (if any). Baptista: "not a convention choice — it is a factor that must be tracked through the fiber integration measure."

4. Determine whether the mismatch is pure convention (bookkeeping) or contains a physics contribution that changes the A_s gap. If bookkeeping: identify the correct chain and report the revised gap. If physics: explain the origin and implications.

5. Cross-check: Does 12.9 factorize into recognizable geometric quantities? (Einstein's PASS criterion: "decomposes into recognizable geometric factors.") Check against 4*pi = 12.57, Vol(SU(3))/(2pi)^4 = ?, f_2/f_0 ratios.

**Input files:**
- `computations/s67_transit_ps.npz`
- `computations/s67_multifield_delta_n.npz`
- `computations/s68_acoustic_transfer.npz`
- `computations/canonical_constants.py`

**Gate**: AS-NORM-69 — INFO (diagnostic). Einstein: PASS if decomposes into recognizable geometric factors. Mack: INFO (diagnostic).

**Output:**
- Script: `computations/s69_as_normalization.py`
- Data: `computations/s69_as_normalization.npz`
- Working paper: Section W1-B

---

### W1-C: ISW-TRACKING-BOLTZMANN-69 — Full Boltzmann ISW

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: H1 from master collab (5/6 reviewers)

**Prompt**:

Compute the ISW-galaxy cross-correlation C_l^{Tg} using a full Boltzmann hierarchy integration (not the Limber approximation from S68). Include QA's cancellation concern: the self-consistent phonon vacuum may reduce potential gradients, partially canceling the ISW enhancement.

The S68 ISW-TRACKING-68 found +12.3% (FW/LCDM) with +7.6% substrate-specific (c_s^2=0 vs c_s^2=1). The S68 computation used the Limber approximation. The full Boltzmann treatment may change this, especially at low l where Limber breaks down and where ISW signal is concentrated.

**Computation steps:**

1. Implement a minimal Boltzmann integrator for the ISW kernel. The ISW contribution to C_l^{Tg} is: C_l^{Tg} = integral dchi W_ISW(chi) * W_g(chi) * P(k=l/chi, z(chi)) where W_ISW = 2 * d(Phi+Psi)/d(eta) and Phi, Psi are metric potentials.

2. Compute C_l^{Tg} for three models: LCDM (w=-1, c_s^2=1), Framework (w=-0.918, c_s^2=0), Quintessence (w=-0.918, c_s^2=1). The FW-specific signal = FW - Quintessence (isolates the c_s^2=0 tracking).

3. Include the QA cancellation quantitatively: if delta_DE tracks delta_m exactly (c_s^2=0), the Poisson equation source becomes rho_m*delta_m + rho_DE*delta_DE = (rho_m + rho_DE*(1+w)/(1-3w)) * delta_m. For w=-0.918: (1+w)/(1-3w) = 0.082/3.754 = 0.0218. DE clustering adds only 2.2% to the gravitational source, reducing the naive ISW enhancement.

4. Report: C_l^{Tg} at l=2-30, Delta(FW vs Quintessence)/C_l(LCDM), integrated SNR vs Planck noise + Euclid galaxy density projections.

**Input files:**
- `computations/s68_isw_tracking_test.npz`
- `computations/canonical_constants.py`

**Gate**: ISW-BOLTZ-69
- **PASS**: Delta(FW vs Quintessence) > 5% at l < 30 (Euclid 2.5-sigma detection threshold)
- **FAIL**: Delta < 1% (ISW tracking effectively undetectable)
- **INFO**: Delta between 1% and 5% (detectable but marginal)

**Output:**
- Script: `computations/s69_isw_boltzmann.py`
- Data: `computations/s69_isw_boltzmann.npz`
- Plot: `computations/s69_isw_boltzmann.png`
- Working paper: Section W1-C

---

### W1-D: SECTOR-RESOLVED-BCS-A4-69 — Fix alpha_s(M_Z) and m_H

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: H2 from master collab (Baptista B1, addresses tensions flagged by 4/6)

**Prompt**:

Compute the sector-resolved BCS correction to a_4 in the Peter-Weyl decomposition. The S68 master collab flags that the mean-field 29.8% a_4 correction worsens m_H (127.5 → 137.4 GeV) and creates a 15.3-sigma alpha_s(M_Z) tension. Sector-resolved corrections may differ from the mean-field average because different PW sectors have different BCS gap magnitudes, different Dynkin indices, and different color Casimirs.

**Computation steps:**

1. Load the D_K spectrum from `computations/s61_fabric_landau_params.npz` (5704 eigenvalues at L_max=6, 28 irreps).

2. Decompose a_4 into PW sector contributions: a_4 = sum_{(p,q)} a_4^{(p,q)} where each sector has its own BCS gap Delta_{(p,q)} determined by the eigenvalue spacing near the Fermi level in that sector.

3. Compute the BCS correction per sector: delta(a_4^{(p,q)}) using the sector-specific gap and the BdG heat kernel factorization (S64 T36: K_BdG(t) = exp(-Delta^2 t) * K_bare(t)).

4. Reassemble: delta(a_4)/a_4 = sum_sectors w_sector * delta(a_4^{sector})/a_4^{sector}. The color sector (relevant for alpha_s(M_Z)) and the Higgs sector (relevant for m_H) may receive different corrections.

5. Compute the corrected gauge couplings: g_1^2 and g_2^2 from the BCS-corrected a_4^{color} sectors, then sin^2(theta_W), alpha_s(M_Z), and m_H.

6. Cross-check: the Cartan Trace Identity T10 constrains sector relations. The color sector correction must respect T_{SU(3)}(p,q) = T_{SU(2)}(q,p) = T_{U(1)}(q,p)/12.

**Input files:**
- `computations/s61_fabric_landau_params.npz`
- `computations/s67_projected_moments.npz`
- `computations/canonical_constants.py`

**Gate**: SECTOR-BCS-69
- **PASS**: alpha_s(M_Z) in [0.110, 0.126] AND m_H in [120, 135] GeV
- **FAIL**: alpha_s(M_Z) outside [0.100, 0.140] or m_H outside [110, 150] GeV
- **INFO**: intermediate

**Output:**
- Script: `computations/s69_sector_bcs_a4.py`
- Data: `computations/s69_sector_bcs_a4.npz`
- Working paper: Section W1-D

---

### W1-E: OFF-JENSEN-SA-69 — Off-Jensen Spectral Action

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: H3 from master collab (3/6 reviewers, sole non-BCS A_s lever)

**Prompt**:

Evaluate the spectral action at one off-Jensen point (tau = 0.19, epsilon = 0.05 along the softest Hessian direction). This is the rate-limiting computation for A_s gap closure — the off-Jensen channel is the sole remaining lever for O(0.3) OOM corrections beyond BCS dressing.

The S63 Hessian analysis found 36 eigenvalues in 10 clusters (Ad(U(2)) decomposition, T8). The softest mode determines the easiest direction to deform the Jensen metric. The S66 Yukawa theorem (C^2 degeneracy on Jensen line) constrains off-Jensen: the 4-fold C^2 degeneracy lifts to 2+2 off-Jensen, generically INCREASING total multifield variance.

**Computation steps:**

1. Load the Hessian eigenvectors from the S63 computation infrastructure. Identify the softest mode (smallest positive eigenvalue).

2. Construct the off-Jensen deformation: g_ab(tau, epsilon) = g_ab^{Jensen}(tau) + epsilon * h_ab where h_ab is the softest Hessian eigenvector projected to Sym^2(su(3)). Use epsilon = 0.05 (perturbative regime).

3. Compute D_K at the off-Jensen point. This requires modifying the Jensen metric by the deformation h_ab and recomputing the eigenvalue spectrum.

4. Compute S(tau, epsilon) = f_0*a_0(epsilon) + f_2*a_2(epsilon) + f_4*a_4(epsilon) at the deformed point. Use the CC cutoff f(x) = sqrt(x).

5. Extract delta(z''/z)/(z''/z) from the change in spectral action curvature. The multifield A_s gets an additional term from the off-Jensen variance: sigma_off^2 = (dN/d(epsilon))^2 * <delta(epsilon)^2>.

6. Report: delta(S)/S, delta(a_2)/a_2, delta(z''/z)/(z''/z), estimated A_s correction in OOM from the off-Jensen channel alone.

**Input files:**
- `computations/s66_zeta_sa.npz`
- `computations/s67_transit_ps.npz`
- `computations/canonical_constants.py`

**Gate**: OFF-JENSEN-69
- **PASS**: delta(z''/z)/(z''/z) > 0.1 (off-Jensen contributes meaningfully to A_s)
- **FAIL**: delta < 0.01 (off-Jensen negligible at epsilon = 0.05)
- **INFO**: intermediate

**Output:**
- Script: `computations/s69_off_jensen_sa.py`
- Data: `computations/s69_off_jensen_sa.npz`
- Working paper: Section W1-E

---

### W1-F: NON-BD-SQUEEZE-RECONCILED-69 — Reconciled Squeeze Estimate

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: H6 from master collab (Phonon-First #5, Baptista B3)

**Prompt**:

Compute the variance-weighted r_eff and cosh(2r_eff) from 8-band BCS coherence factors with proper spectral (van Hove) weighting. Reconcile the Lizzi-Transit naive estimate (0.26-0.50 OOM) with the Landau downward revision (0.07-0.16 OOM). The discrepancy traces to the optical branch weighting.

The key physics: the van Hove spectral density diverges as 1/sqrt(omega - omega_min) near the band edge (S28 theorem). This means the effective epsilon/Delta for the optical branch is NOT the band-average (~3) but the van Hove weighted value (~1.4), which gives a much larger r_optical and reconciles the two estimates upward.

**Computation steps:**

1. Load multifield fractions from `s67_multifield_delta_n.npz` (acoustic 3.3%, Leggett 46.2%, optical 50.6%).

2. For each of the 8 BCS bands, compute the squeeze parameter r_I = arctanh(v_I/u_I) where the coherence factors come from the sector-specific BCS gap.

3. Weight by the van Hove spectral density near each band edge: w_I(omega) = N_I / sqrt(omega - omega_min^I). This corrects the effective epsilon/Delta per band.

4. Compute the variance-weighted effective: r_eff = sqrt(sum_I f_I * r_I^2) and cosh(2r_eff).

5. Compare to: Lizzi-Transit naive (0.26-0.50 OOM), Landau revised (0.07-0.16 OOM), this computation.

**Input files:**
- `computations/s67_multifield_delta_n.npz`
- `computations/s68_bcs_dressed_mode.npz`
- `computations/canonical_constants.py`

**Gate**: SQUEEZE-RECON-69
- **PASS**: Enhancement 0.07-0.30 OOM (consistent with van Hove correction)
- **INFO**: outside this range

**Output:**
- Script: `computations/s69_squeeze_reconciled.py`
- Data: `computations/s69_squeeze_reconciled.npz`
- Working paper: Section W1-F

---

## IV. Wave 2: Consistency + Data Tests (6 parallel, can co-run with late W1)

### W2-A: TRANSIT-CONSISTENCY-69 — Impulsive Consistency Relations

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: MEDIUM-HIGH
**Carry-Forward**: H4 from master collab (Einstein #4)

**Prompt**:

Derive the impulsive-regime consistency relations that connect the framework's 7 CMB predictions (n_s, r, n_T, alpha_s, f_NL^equil, f_NL^folded, beta_iso). The S68 Lizzi-Transit workshop (E1) established that the CMB power spectrum is determined by exactly three numbers at the fold: z''/z, d(z''/z)/dtau, d^2(z''/z)/dtau^2. If 7 observables depend on 3 inputs, there must be 4 consistency relations among them. Finding them tells us which predictions are truly independent and which are derived consequences.

**Context.** Standard slow-roll inflation has a well-known consistency relation r = -8 n_T. This does NOT apply to the impulsive transit (r = 16*eps is violated by 50x per S67 W6-B: r = 0.0071 vs 16*eps = 0.35). The Kofman-Linde-Starobinsky formula r = 16*eps * (sinh(delta N))^{-2} applies to impulsive transitions. The S68 result alpha_s = 0 (from Bogoliubov saturation) already provides one relation: alpha_s is not independent but fixed at zero by the transit physics.

**Computation steps:**

1. Load the transit parameters from `computations/s67_transit_ps.npz`: eps_H = 0.96, c_s = 0.485, N_e = 7.75, z''/z at fold, and the Bogoliubov coefficients.

2. Express each of the 7 observables in terms of (z''/z, d(z''/z)/dtau, d^2(z''/z)/dtau^2):
   - n_s: from d(ln P_zeta)/d(ln k) evaluated at the fold via the spectral action mapping
   - r: from the tensor/scalar power ratio, using the non-slow-roll KLS formula
   - n_T: from the tensor spectral index (blue, +0.075 from S67 W6-B)
   - alpha_s: = 0 (Bogoliubov saturation, 5 independent proofs from S68 W1-C)
   - f_NL^equil: from the in-in bispectrum integral (S67 W2-C: 1.03)
   - f_NL^folded: from the GGE relic shape (S67 W2-C: 0.129)
   - beta_iso: from the inter-branch isocurvature (S67 W4-E: 3.22e-12)

3. Identify the consistency relations by eliminating the 3 fold parameters between pairs of observables. Check whether any derived relation contradicts a computed value (this would indicate an error in a prior computation).

4. Count the independent predictions: 7 - (number of valid consistency relations) = N_independent.

5. Cross-check: verify each relation holds numerically using the S67/S68 computed values.

6. Report: the explicit consistency relations, N_independent, and any contradictions found.

**Input files:**
- `computations/s67_transit_ps.npz`
- `computations/s67_gge_bispectrum.npz`
- `computations/s68_alpha_s_transfer.npz`
- `computations/canonical_constants.py`

**Gate**: TRANSIT-CONSIST-69
- **PASS**: Independent predictions reduce from 7 to ≤ 4
- **FAIL**: A derived relation contradicts a computed value (indicates error in prior computation)
- **INFO**: Relations found but N_independent > 4

**Output:**
- Script: `computations/s69_transit_consistency.py`
- Data: `computations/s69_transit_consistency.npz`
- Working paper: Section W2-A

---

### W2-B: SU(1,1)-PHASE-CG24-69 — KZ Phase Topology

**Agent**: `phonon-first-cosmologist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: M6 from master collab (Phonon-First #3)

**Prompt**:

Compute the spatially averaged cos(phi_eff) on the Cayley graph CG(24) from Kibble-Zurek defect topology. This is an independent check on W1-A (which computes phi_eff from BCS dynamics). If the KZ defects produce a Z_3 phase winding on the 24-cell Josephson array, the spatial average <cos(phi_eff)> = -1/2 (partial destructive interference). If phase disorder averages out, <cos(phi_eff)> > 0 (constructive on average).

**Context.** The Josephson array on CG(24) (the dual graph of the 24-cell, S52) has N_domains = 3 (from KZ scaling with quench rate) and Josephson coupling E_J = 7.04 (S52 Rank-1 identity J_12/J_23 = 19.52). After the transit, each domain acquires a random BCS phase. The relative phases at domain boundaries are the phi_eff that controls A_s. The SU(1,1) structure (S68 master collab Theme 5) means the same group element acts on both the BCS pairing and the cosmological Bogoliubov transformation.

**Computation steps:**

1. Load the Cayley graph structure from `computations/s57_cayley_josephson.npz`: 24 vertices, 96 edges, edge weights J_ij, Josephson energy E_J = 7.04.

2. Partition CG(24) into N_domains = 3 KZ domains using the Kibble-Zurek prescription: the quench rate dt_transit = 0.145 and the domain equilibration timescale tau_GL give N_domains = (L_system / xi_KZ)^d where xi_KZ = xi_0 * (tau_Q / tau_0)^{nu/(1+z*nu)}.

3. Assign a random BCS phase phi_a to each domain (a = 1, 2, 3), drawn from the Z_3 subgroup of U(1) (phases 0, 2pi/3, 4pi/3). This is the maximally frustrated configuration.

4. Compute the spatial average <cos(phi_eff)> = (1/N_edges) * sum_{<ij>} J_ij * cos(phi_i - phi_j) where phi_i is the phase of the domain containing vertex i.

5. Repeat for (a) Z_3 winding, (b) uniform random phases, (c) thermal distribution P(phi) ~ exp(E_J cos(phi)/T). Report all three.

6. Compute the variance: var(cos(phi_eff)) to determine the uncertainty on the phase average.

**Input files:**
- `computations/s57_cayley_josephson.npz`
- `computations/canonical_constants.py`

**Gate**: SU11-PHASE-69
- **PASS**: <cos(phi_eff)> > 0 (net constructive interference)
- **INFO**: <cos(phi_eff)> < 0 (net destructive) or large variance (indeterminate)

**Output:**
- Script: `computations/s69_su11_phase.py`
- Data: `computations/s69_su11_phase.npz`
- Plot: `computations/s69_su11_phase.png`
- Working paper: Section W2-B

---

### W2-C: CMB-S4-NS-PREREGISTER-69 — n_s Decision Rules

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: M2 from master collab (Mack #5, Einstein implicit in Q3)

**Prompt**:

Pre-register the framework's n_s prediction and define decision rules for the CMB-S4 measurement. The framework predicts n_s = 0.9595 from spectral geometry (0.9567 bare SA + 0.0028 BCS correction from S68 W1-B). CMB-S4 will measure n_s to sigma ~ 0.002 (vs Planck sigma ~ 0.004). The CC cutoff functional has a structural maximum n_s ~ 0.963 (from the critical exponent alpha_c = 1.4314, S67 T4). This means CMB-S4 can definitively test the framework.

**Computation steps:**

1. Assemble the framework's n_s prediction chain:
   - n_s(bare, SA L3 at tau = 0.19) = 0.9567 (S66 RUNNING-NS-66)
   - n_s(BCS-dressed) = 0.9595 (S68 W1-B: delta_ns = +0.0028 from eps_H shift)
   - n_s(structural maximum) = 0.963 (from alpha_c = 1.4314, T4)
   - n_s(Planck 2018) = 0.9649 +/- 0.0042
   - n_s(CMB-S4 projected) = ? +/- 0.002

2. Compute the framework's prediction window: [n_s(min), n_s(max)] = [0.955, 0.963] where the lower bound is the bare SA value and the upper bound is the structural maximum.

3. Define decision rules for CMB-S4:
   - **STRONG PASS**: CMB-S4 n_s in [0.957, 0.963] at 95% CL — framework prediction confirmed within structural bounds
   - **WEAK PASS**: CMB-S4 n_s in [0.955, 0.957] — below BCS-dressed prediction but within bare SA value
   - **TENSION**: CMB-S4 n_s in [0.963, 0.970] — above structural maximum but not catastrophic (may indicate missing physics: off-Jensen correction, higher-loop BCS)
   - **FAIL**: CMB-S4 n_s > 0.970 — above structural maximum by > 3 sigma; framework falsified in the n_s sector

4. Compute the Bayes factor B(FW/LCDM) as a function of hypothetical CMB-S4 n_s measurement, given the prior range [0.955, 0.963] for FW and a broad prior [0.93, 1.00] for generic models.

5. Report: prediction, decision tree, projected discrimination power.

**Input files:**
- `computations/s68_bcs_dressed_mode.npz` (n_s = 0.9595)
- `computations/s66_running_ns.npz`
- `computations/canonical_constants.py`

**Gate**: CMB-S4-NS-69
- **PASS**: Framework n_s prediction window [0.955, 0.963] is well-defined and testable
- **FAIL**: Internal inconsistency in prediction chain (should not happen)

**Output:**
- Script: `computations/s69_cmbs4_preregister.py`
- Data: `computations/s69_cmbs4_preregister.npz`
- Plot: `computations/s69_cmbs4_preregister.png`
- Working paper: Section W2-C

---

### W2-D: PVD-05-FSIGMA8-69 — Growth Rate vs Data

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: PVD-05 from S68 phonon-vs-data plan (HIGH priority, QUEUED)

**Prompt**:

Compare the framework's growth rate prediction f*sigma_8(z) against published redshift-space distortion (RSD) measurements. The framework predicts ~4% lower f*sigma_8 than LCDM (sigma_8 = 0.793 vs 0.811) due to the w_0 = -0.918 dark energy equation of state suppressing late-time growth. This is one of the tightest constraints on the combination of Omega_m and w_0.

**Context.** The S65 computation `s65_fsigma8.npz` produced framework predictions at 7 redshift bins. The S68 phonon-vs-data plan (PVD-05) identified the published data:
- FW bins [z, f*sigma8]: [0.15, 0.443], [0.38, 0.457], [0.51, 0.455], [0.70, 0.444], [0.85, 0.431], [1.05, 0.412], [1.52, 0.363]
- Observed: [0.530, 0.497, 0.459, 0.448, 0.430, 0.376, 0.342] with typical errors 0.03-0.06

**Computation steps:**

1. Load the framework f*sigma_8(z) predictions from `computations/s65_fsigma8.npz`.

2. Compile published RSD measurements from: 6dFGS (Beutler+12, z=0.067), SDSS MGS (Howlett+15, z=0.15), BOSS DR12 (Alam+17, z=0.38, 0.51, 0.61), eBOSS (z=0.70, 0.85), DESI DR1 (z=1.05, 1.52). Use values from the S68 phonon-vs-data plan Section 3.2 PVD-05.

3. Compute chi^2 = sum_i (f*sigma_8^{obs}(z_i) - f*sigma_8^{FW}(z_i))^2 / sigma_i^2 for the framework. Compute the same for LCDM (sigma_8 = 0.811). Report both chi^2/dof.

4. Compute the sigma_8 tension: the low-z points (z < 0.3) from 6dFGS and SDSS typically have f*sigma_8 ~ 0.48-0.53, which is higher than both FW (0.44) and LCDM (0.46). Determine if the framework's lower sigma_8 makes this worse or better.

5. Check for redshift-dependent trends in the residuals: (obs - FW)/sigma vs z. A systematic trend would indicate the growth history is wrong.

6. Try astro MCP for any accessible RSD catalogs (SDSS, DESI). If MCP data available, compare directly to raw measurements rather than published compilations.

**Input files:**
- `computations/s65_fsigma8.npz`
- `computations/canonical_constants.py`
- S68 phonon-vs-data plan `sessions/archive/session-68/session-68-phonon-vs-data-plan.md` Section 3.2 PVD-05

**Gate**: PVD-FSIG8-69
- **PASS**: chi^2/dof < 2 (framework consistent with growth rate data)
- **FAIL**: chi^2/dof > 3 (systematic tension with growth rate)
- **INFO**: chi^2/dof in [2, 3] (marginal)

**Output:**
- Script: `computations/s69_pvd05_fsigma8.py`
- Data: `computations/s69_pvd05_fsigma8.npz`
- Plot: `computations/s69_pvd05_fsigma8.png`
- Working paper: Section W2-D

---

### W2-E: PVD-04-SNE-PANTHEON-69 — Supernova Distance Modulus

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: PVD-04 from S68 phonon-vs-data plan (HIGH priority, QUEUED)

**Prompt**:

Compare the framework's luminosity distance prediction d_L(z) against Pantheon+ Type Ia supernova data (~1700 SNe, Scolnic et al. 2022). The framework predicts distances from flat wCDM with w_0 = -0.918, w_a = 0, Omega_m = 0.315, H_0 = 67.4. Supernovae provide the tightest constraint on w_0 in the z < 1 regime — this is the data that first hinted at dark energy.

**Context.** The S68 phonon-vs-data plan identified VizieR catalog J/ApJ/938/110 but encountered MaskedColumn serialization errors. Workaround options: (1) try VizieR query with smaller column selection, (2) query SDSS supernova catalog via SQL, (3) hardcode the published Pantheon+ binned Hubble diagram (40 bins in z from 0.01 to 2.26).

**Computation steps:**

1. Compute the framework's distance modulus: mu_FW(z) = 5*log10(d_L(z)/10 pc) where d_L(z) = (1+z) * integral_0^z dz'/H(z') and H(z) = H_0 * sqrt(Omega_m*(1+z)^3 + Omega_DE*(1+z)^{3(1+w_0)}). Use w_0 = -0.918, Omega_m = 0.315, Omega_DE = 0.685, H_0 = 67.4 km/s/Mpc.

2. Attempt to retrieve Pantheon+ data via astro MCP (VizieR: J/ApJ/938/110). If MaskedColumn error persists, use the published binned Hubble diagram from the paper (Table 2: 40 redshift bins with m_B^corr, uncertainty, and bin redshift).

3. Compute Hubble residuals: delta_mu(z) = mu_obs(z) - mu_FW(z) for each SN or bin.

4. Compute chi^2 for the framework. For binned data: chi^2 = sum_i (delta_mu_i)^2 / sigma_i^2. For individual SNe with covariance: chi^2 = delta_mu^T C^{-1} delta_mu (if covariance matrix available).

5. Compare to LCDM (w_0 = -1): compute chi^2(LCDM) and report Delta chi^2 = chi^2(FW) - chi^2(LCDM). The framework's w_0 = -0.918 makes the universe expand slightly faster at late times, giving slightly brighter (closer) SNe at z ~ 0.5-1.0.

6. Check for redshift-dependent systematics in the residuals. A trend in delta_mu(z) would indicate the expansion history is wrong at the level probed by SNe.

**Input files:**
- `computations/canonical_constants.py`
- S68 phonon-vs-data plan `sessions/archive/session-68/session-68-phonon-vs-data-plan.md` Section 3.2 PVD-04

**Gate**: PVD-SNE-69
- **PASS**: chi^2/dof < 1.5 (Hubble residuals consistent with zero within Pantheon+ errors)
- **FAIL**: Systematic redshift-dependent trend exceeding 0.05 mag
- **INFO**: chi^2/dof in [1.5, 2.5] (marginal fit)

**Output:**
- Script: `computations/s69_pvd04_sne.py`
- Data: `computations/s69_pvd04_sne.npz`
- Plot: `computations/s69_pvd04_sne.png`
- Working paper: Section W2-E

---

### W2-F: PVD-13-DA-DESI-69 — Angular Diameter Distance

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: PVD-13 from S68 phonon-vs-data plan (HIGH priority, QUEUED)

**Prompt**:

Compute the angular diameter distance d_A(z) from the framework's expansion history and compare to DESI DR1 measurements. This is a more direct comparison than PVD-02 (which used the volume-averaged distance D_V/r_d, an approximate combination of d_A and H(z)). The angular diameter distance is measured through the BAO transverse mode as D_M(z)/r_d = (1+z) * d_A(z)/r_d.

**Context.** The S68 PVD-02 test found chi^2/dof = 4.06 for the framework vs DESI DR1 D_V/r_d, driven by 2-4 sigma overshoots at z = 0.5-0.9. The D_V metric mixes radial (H^{-1}) and transverse (d_A) distances with weights that depend on the fiducial model. A direct comparison of D_M/r_d is cleaner and separates the transverse from the radial signal.

**Computation steps:**

1. Compute d_A(z) = chi(z)/(1+z) where chi(z) = integral_0^z dz'/H(z') and H(z) = H_0 * sqrt(Omega_m*(1+z)^3 + Omega_DE*(1+z)^{3(1+w_0)}). Use w_0 = -0.918, Omega_m = 0.315, H_0 = 67.4.

2. Compute the sound horizon at drag epoch: r_d = integral_{z_d}^{inf} c_s(z)/H(z) dz with c_s = c/sqrt(3(1 + 3*Omega_b/(4*Omega_gamma) * 1/(1+z))). Use z_d = 1059.94, Omega_b h^2 = 0.02237.

3. Form D_M(z)/r_d = (1+z) * d_A(z) / r_d at the 7 DESI DR1 effective redshifts: z = [0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330].

4. Compare to DESI DR1 published D_M/r_d values with their uncertainties. Compute per-bin residuals (obs - pred)/sigma and total chi^2.

5. Also compute D_H(z)/r_d = c/(H(z)*r_d) at the same redshifts — the radial BAO measurement. Compare to DESI DR1 D_H/r_d. This separates the distance vs expansion rate contributions to the PVD-02 tension.

6. Cross-check: verify r_d computation against Planck value (147.09 +/- 0.26 Mpc). The framework with standard BBN should give the same r_d as LCDM (the pre-recombination physics is identical).

**Input files:**
- `computations/s64_desi_dv.npz`
- `computations/canonical_constants.py`
- DESI DR1 published BAO summary table (7 effective redshifts)

**Gate**: PVD-DA-69
- **PASS**: chi^2/dof < 3 for D_M/r_d alone
- **FAIL**: chi^2/dof > 5
- **INFO**: chi^2/dof in [3, 5] (marginal, consistent with PVD-02 tension)

**Output:**
- Script: `computations/s69_pvd13_da.py`
- Data: `computations/s69_pvd13_da.npz`
- Plot: `computations/s69_pvd13_da.png`
- Working paper: Section W2-F

---

## V-A. Wave 3: Depends on W1 Results (4 parallel)

### W3-A: SONIC-PENROSE-INEQUALITY-69 — Geometric A_s Bound

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: H5 from master collab (SP #4, unique methodological approach)

**Prompt**:

Apply the Penrose inequality to the sonic horizon of the transit spacetime. The Penrose inequality in GR states M >= sqrt(A/(16*pi)) for a trapped surface of area A. The sonic analog replaces the trapped surface with the sonic horizon at k_tach = 1974 M_KK, where modes transition from frozen (|beta_k|^2 = 1) to oscillating (|beta_k|^2 → 0). If the "sonic area" (= number of frozen modes N_modes ~ 4000) provides a geometric upper bound on A_s, this constrains the amplitude from global causal structure rather than mode-by-mode physics.

**Context.** This approach was proposed uniquely by SP in the S68 master collab. No other reviewer considered it. The method bypasses all normalization chain ambiguities (the 12.9x mismatch in W1-B) because it works from the horizon area, not from the Bogoliubov coefficients directly. SP's conformal diagram of the transit (S68 master collab, Section V.2) identifies the sonic horizon as a spacelike surface separating Region I (frozen CMB modes) from the production region.

**Computation steps:**

1. Load the transit Bogoliubov spectrum from `computations/s67_transit_ps.npz`: |beta_k|^2 as a function of k/k_tach, identifying the sonic horizon at the threshold k_tach = 1974 M_KK.

2. Define the "sonic area" A_sonic: count the number of independent modes with |beta_k|^2 > 0.5 (the "frozen" modes). Each mode contributes one Planck area unit in the sonic metric. A_sonic = N_modes * l_sonic^2 where l_sonic is the sonic Planck length (c_BLV / M_KK).

3. Formulate the sonic Penrose inequality: A_s^{max} = f(A_sonic / A_Pl^{sonic}) where the function f encodes the mass-area relation for the sonic metric. For a sonic Schwarzschild analog: M_sonic^2 = A_sonic / (16*pi), giving P_zeta^{max} = H^2 / (8*pi^2 * M_sonic^2).

4. Compute the bound numerically using k_tach = 1974 M_KK, N_modes from the transit spectrum, and H at the fold.

5. Compare: A_s^{bound} vs A_s^{observed} = 2.1e-9 (Planck). If bound < A_s^{obs}, the framework has a geometric obstruction to matching the observed amplitude — the sonic horizon is too small to support the required A_s.

6. Cross-check: verify the bound against the multifield delta-N result A_s = 3.29e-10 (S67 W3-B). The bound should satisfy A_s^{delta-N} < A_s^{bound} for consistency.

**Input files:**
- `computations/s67_transit_ps.npz`
- `computations/canonical_constants.py`

**Gate**: SONIC-PENROSE-69
- **PASS**: A_s^{bound} ≥ A_s^{observed} = 2.1e-9 (no geometric obstruction)
- **FAIL**: A_s^{bound} < A_s^{observed} (geometric obstruction to matching amplitude)
- **INFO**: bound is close to A_s (within a factor of 2)

**Output:**
- Script: `computations/s69_sonic_penrose.py`
- Data: `computations/s69_sonic_penrose.npz`
- Plot: `computations/s69_sonic_penrose.png`
- Working paper: Section W3-A

---

### W3-B: EUCLID-ISW-RSD-JOINT-69 — Combined Fisher Forecast

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: M1 from master collab (Mack #4, depends on W1-C output)

**Prompt**:

Construct a combined Fisher matrix forecast for Euclid ISW + RSD + lensing to determine the joint discrimination power between the framework (w_0 = -0.918, c_s^2 = 0) and w_0CDM (generic w_0, c_s^2 = 1). This takes the W1-C ISW-BOLTZMANN result as input for the ISW channel and combines it with growth rate and lensing constraints.

**Context.** The S68 ISW-TRACKING-68 established the ISW enhancement at 7.6-12.3% (FW/LCDM). W1-C refines this with full Boltzmann treatment and QA's cancellation concern. Even if the ISW signal alone is marginal, the COMBINED constraint (ISW + RSD + lensing) may reach detection threshold. Mack's S68 review estimated 2.5-sigma Euclid detection for ISW alone; the joint constraint should be stronger.

**Computation steps:**

1. Load the W1-C output: C_l^{Tg} for FW, LCDM, and Quintessence models, and the ISW Delta at l < 30.

2. Construct the ISW Fisher matrix: F_ISW = sum_l (2l+1)/(2) * (dC_l^{Tg}/d(theta_i)) * C_l^{-1} * (dC_l^{Tg}/d(theta_j)) where theta = {w_0, c_s^2_DE}. Use Euclid galaxy density n_g ~ 30 arcmin^{-2} and survey area 15,000 deg^2.

3. Construct the RSD Fisher matrix from the growth rate: F_RSD from sigma(f*sigma_8) at 5 redshift bins (Euclid spectroscopic, z = 0.9-1.8). Use the growth rate formula f = Omega_m(z)^{0.55 + 0.05*(1+w)} and sigma_8(z) from the framework.

4. Construct the lensing Fisher matrix from the CMB lensing power spectrum: F_lens from C_l^{kk} sensitivity at l = 100-500 with CMB-S4 noise levels.

5. Combine: F_total = F_ISW + F_RSD + F_lens (Fisher matrices add for independent probes).

6. Report: sigma(w_0), sigma(c_s^2), the sigma-contour ellipse in the (w_0, c_s^2) plane, and the combined discrimination significance (in sigma) between FW and w_0CDM.

**Input files:**
- W1-C output: `computations/s69_isw_boltzmann.npz`
- `computations/s65_fsigma8.npz`
- `computations/canonical_constants.py`

**Gate**: EUCLID-JOINT-69
- **INFO**: Report combined sigma(w_0), sigma(c_s^2), discrimination significance

**Output:**
- Script: `computations/s69_euclid_joint.py`
- Data: `computations/s69_euclid_joint.npz`
- Plot: `computations/s69_euclid_joint.png`
- Working paper: Section W3-B

---

### W3-C: KK-THRESHOLD-HIGGS-QUARTIC-69 — Corrected Higgs Mass

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: M10 from master collab (Baptista B4, depends on W1-D output)

**Prompt**:

Compute the KK threshold correction to the Higgs quartic coupling lambda(M_KK) using the sector-resolved BCS-corrected a_4 from W1-D. The tree-level Higgs mass from the spectral action is m_H = 134 GeV (filter-independent, S62 T20). The Aitken-extrapolated value is 127.5 GeV (1.9% from observed 125.1). The S68 master collab flagged that mean-field BCS dressing WORSENS m_H to 137.4 GeV. The sector-resolved correction from W1-D may differ from the mean-field average and potentially compensate.

**Computation steps:**

1. Load the W1-D output: sector-resolved delta(a_4^{(p,q)})/a_4^{(p,q)} for each PW sector at L_max = 6 (28 irreps).

2. The Higgs quartic is lambda = pi^2 * a_4 / (2 * f_0 * a_2^2) in the Chamseddine-Connes-Marcolli formula. The Higgs mass is m_H = sqrt(2*lambda) * v where v = 246 GeV.

3. Compute the KK threshold correction: the heavy KK modes above M_KK contribute to the running of lambda from M_KK down to the electroweak scale. The sector-resolved a_4 modifies the initial condition lambda(M_KK) differently than the mean-field average.

4. Use the PW Dynkin indices from S64 to determine which sectors contribute to the Higgs channel. The Higgs lives in the (1,1) representation of SU(3); the relevant sectors for lambda are those coupling to the (1,1) channel through the Yukawa structure.

5. Compute the corrected m_H: m_H(corrected) = m_H(tree) * sqrt(1 + delta(lambda)/lambda) where delta(lambda)/lambda comes from the sector-resolved a_4 correction.

6. Report: m_H(corrected), comparison to 125.1 GeV observed, comparison to 127.5 GeV (Aitken), and comparison to 137.4 GeV (mean-field BCS worsened).

**Input files:**
- W1-D output: `computations/s69_sector_bcs_a4.npz`
- `computations/s61_fabric_landau_params.npz` (PW Dynkin indices)
- `computations/canonical_constants.py`

**Gate**: KK-HIGGS-69
- **PASS**: m_H in [120, 135] GeV (consistent with observation within uncertainties)
- **FAIL**: m_H outside [110, 150] GeV
- **INFO**: intermediate

**Output:**
- Script: `computations/s69_kk_higgs.py`
- Data: `computations/s69_kk_higgs.npz`
- Working paper: Section W3-C

---

### W3-D: PVD-07-PLANCK-CL-69 — Planck Power Spectrum Shape Test

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: PVD-07 from S68 phonon-vs-data plan (HIGH priority, QUEUED)

**Prompt**:

Compute the CMB temperature angular power spectrum C_l^{TT} from the framework's parameters and compare its SHAPE to Planck 2018 data. The A_s normalization is known to be off by 0.755 OOM — this test is not about the overall amplitude but about whether n_s = 0.9595 and alpha_s = 0 produce the correct spectral shape across l = 2-2500.

**Context.** The framework predicts: n_s = 0.9595, alpha_s = 0, r = 0.0242, Omega_m h^2 = 0.1424, Omega_b h^2 = 0.02237, H_0 = 67.4, tau_reion = 0.054. These are the SAME parameters as LCDM except for n_s (0.9595 vs 0.9649) and A_s (3.69e-10 vs 2.1e-9). The n_s difference tilts the spectrum: 0.4% redder at l = 100, 1.5% redder at l = 1000, 3% redder at l = 2000 relative to LCDM. This cumulative tilt is detectable by Planck.

**Computation steps:**

1. Implement the Eisenstein-Hu transfer function T(k) for cold dark matter with baryonic oscillations. This gives the matter power spectrum P(k) = A_s * (k/k_pivot)^{n_s-1} * T^2(k) * (k/H_0)^4.

2. Compute C_l^{TT} using the integral: C_l = (2/pi) * integral dk k^2 P(k) |Delta_l(k)|^2 where Delta_l(k) is the transfer function from the radiation perturbation equations. Use the Sachs-Wolfe approximation Delta_l ~ j_l(k*chi_*)/3 for l > 30, with correction terms for the integrated Sachs-Wolfe and acoustic oscillations via the fitting functions from Hu & Sugiyama (1996).

3. Rescale C_l to remove the A_s offset: define the shape C_l^{shape} = C_l / A_s, so both framework and LCDM are compared at unit normalization. The shape is controlled by n_s, Omega_m, Omega_b, not A_s.

4. Retrieve Planck 2018 binned TT power spectrum: D_l = l(l+1)C_l/(2*pi) in microKelvin^2. Published in Planck Legacy Archive. Hardcode the 29 binned values from the published paper (l_eff = [2-29, 30-100, 101-200, ..., 2001-2508]).

5. Compute shape residuals: delta_l = (D_l^{FW,shape} - D_l^{Planck,shape}) / D_l^{Planck,shape} as a function of l, after normalizing both to the same A_s.

6. Report: the shape residuals vs l, maximum deviation, chi^2 for shape alone, and the specific l-range where n_s = 0.9595 vs 0.9649 produces the largest difference.

**Input files:**
- `computations/canonical_constants.py`
- Planck 2018 binned power spectrum (hardcoded from published data)

**Gate**: PVD-CL-69
- **PASS**: Shape residuals < 5% for all l > 30 (after removing A_s normalization)
- **FAIL**: Shape mismatch > 10% in any l-bin (indicates n_s is wrong)
- **INFO**: residuals 5-10% (marginal, may indicate BCS correction needed)

**Output:**
- Script: `computations/s69_pvd07_planck_cl.py`
- Data: `computations/s69_pvd07_planck_cl.npz`
- Plot: `computations/s69_pvd07_planck_cl.png`
- Working paper: Section W3-D

---

## V-B. Wave 4: Medium Refinements (7 parallel, no hard dependencies)

### W4-A: EP-TRANSIT-CORRECTION-69 — Finite Relaxation Correction to eps_H

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: M3 from master collab (Einstein #2)

**Prompt**:

Compute the leading correction to eps_H from the finite BCS relaxation time during the transit. The S68 eps_H cancellation theorem (proven to machine epsilon 6.4e-13) shows that a tau-INDEPENDENT multiplicative correction to S(tau) leaves eps_H exactly invariant. But the BCS gap has a finite relaxation time (tau_relax/dt_transit = 0.003 from Landau Ld2), meaning the BCS correction to S(tau) is NOT perfectly tau-independent. The residual tau-dependent correction breaks the cancellation at some order. This computation determines that order.

**Computation steps:**

1. Load the transit dynamics from `computations/s67_transit_ps.npz` and the BCS relaxation timescale from the S68 W1-B result (tau_relax/dt_transit = 0.003).

2. Model the BCS correction to S(tau) as S_BCS(tau) = S_bare(tau) * [1 + f(tau)] where f(tau) = f_0 * (1 - exp(-(tau - tau_onset)/tau_relax)). The correction ramps on with timescale tau_relax during the transit.

3. Compute eps_H = (dS/dtau)^2 / (2 * S * d^2S/dtau^2) for both S_bare and S_BCS. The correction delta(eps_H) = eps_H(BCS) - eps_H(bare) arises from the tau-dependence of f(tau).

4. Expand to leading order in tau_relax/dt_transit << 1: delta(eps_H)/eps_H ~ (tau_relax/dt_transit) * (f_0'' / f_0) ~ O(0.003 * 0.1) ~ O(3e-4). Verify this estimate numerically.

5. Propagate to n_s: delta(n_s) = delta(eps_H) * (dn_s/deps_H) using the constant-epsilon formula n_s = (1 - 3*eps)/(1 - eps).

**Input files:**
- `computations/s67_transit_ps.npz`
- `computations/s68_bcs_dressed_mode.npz`
- `computations/canonical_constants.py`

**Gate**: EP-TRANSIT-69
- **PASS**: |delta(eps_H)| < 10^{-4} (negligible, cancellation survives finite relaxation)
- **FAIL**: |delta(eps_H)| > 10^{-3} (cancellation broken at significant level)
- **INFO**: intermediate

**Output:**
- Script: `computations/s69_ep_transit.py`
- Data: `computations/s69_ep_transit.npz`
- Working paper: Section W4-A

---

### W4-B: SWAMPLAND-1LOOP-69 — BCS-Dressed Swampland Distance

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: M4 from master collab (Einstein #3)

**Prompt**:

Test the swampland distance conjecture with BCS-dressed spectral moments. The conjecture requires |V'|/V > c ~ O(1)/M_Pl for any consistent theory of quantum gravity. The framework's spectral action provides V(tau) = S(tau) and V'(tau) = dS/dtau. The bare field range from tau = 0 to tau_fold = 0.19 is Delta_phi = 7.67 M_Pl (S43). BCS dressing shifts the spectral moments: a_2 by +11.6%, a_4 by +29.8%, a_6 by +51% (S67 PROJECTED-MOMENTS-67). These shifts modify both V and V'.

**Computation steps:**

1. Load the spectral action S(tau) from `computations/s66_zeta_sa.npz` and the BCS corrections from `computations/s67_projected_moments.npz`.

2. Compute the BCS-dressed spectral action: S_BCS(tau) = f_0 * a_0(tau) + f_2 * (1.116) * a_2(tau) + f_4 * (1.298) * a_4(tau) + ... where the BCS correction factors are applied to each Seeley-DeWitt coefficient.

3. Compute |V'|/V = |dS_BCS/dtau| / S_BCS at the fold (tau = 0.19). The BCS correction increases a_4 more than a_2, which steepens the potential.

4. Convert to Planck units using the canonical normalization: phi = sqrt(K_DeWitt) * tau = sqrt(5.0) * tau (S63 T14: K_DeWitt = 5.0 exact). Delta_phi = 2.236 * 0.19 = 0.425 in canonical units, times the spectral action normalization → 7.67 M_Pl.

5. Report: |V'|/V at fold, Delta_phi/M_Pl, and whether the framework satisfies (V'/V > c) or the refined de Sitter conjecture (min(V'/V, V''/V) > c ~ O(1)/M_Pl).

**Input files:**
- `computations/s66_zeta_sa.npz`
- `computations/s67_projected_moments.npz`
- `computations/canonical_constants.py`

**Gate**: SWAMP-69
- **PASS**: |V'|/V > 1 M_Pl^{-1} (swampland distance conjecture satisfied)
- **FAIL**: |V'|/V < 0.5 M_Pl^{-1} (potential obstruction)
- **INFO**: intermediate

**Output:**
- Script: `computations/s69_swampland.py`
- Data: `computations/s69_swampland.npz`
- Working paper: Section W4-B

---

### W4-C: CONFORMAL-ANOMALY-EPSH-69 — Anomaly vs eps_H Protection

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: M5 from master collab (Einstein #5)

**Prompt**:

Determine whether the conformal anomaly (Euler density E_4 + Weyl tensor C^2 at one loop) breaks the eps_H cancellation theorem that was proven to machine epsilon in S68 W1-D. The cancellation theorem applies to classical (tree-level) multiplicative corrections to S(tau). Quantum corrections from the conformal anomaly are NOT multiplicative — they add a non-trivial tau-dependent function delta_S_anomaly(tau) ~ (a/16*pi^2) * integral (alpha*E_4 + beta*C^2 + gamma*Box R). This could potentially introduce a non-uniform correction that shifts n_s.

**Computation steps:**

1. Load the curvature invariants of Jensen-deformed SU(3) from the analytic formulas (permanent results registry, Section III): R(tau), |Ric|^2(tau), K(tau), |C|^2(tau). These are exact rational functions of exponentials.

2. Compute the one-loop conformal anomaly contribution: delta_S_anomaly(tau) = (1/(16*pi^2)) * integral_K d^8x sqrt(g_K) * [alpha * E_8 + beta * C_8^2 + gamma * Box^4 R] where alpha, beta, gamma are determined by the field content (bosonic and fermionic modes of D_K).

3. In practice, use the 8D Euler density E_8 = chi(SU(3)) = 0 (S21c, Gauss-Bonnet). The Weyl term C_8^2 is nonzero and tau-dependent. Compute delta_S_anomaly from the Weyl-squared contribution.

4. Compute the corrected eps_H: eps_H(corrected) = eps_H(bare) + delta_eps_H where delta_eps_H comes from the tau-dependence of delta_S_anomaly. If delta_S_anomaly is a polynomial in exp(tau) (like the curvature invariants), it will generically be non-uniform and break the cancellation.

5. Propagate to n_s: delta(n_s) from the conformal anomaly correction.

6. Cross-check: the Euler contribution vanishes (chi = 0), so only the Weyl term matters. Compare its magnitude to the S68 eps_H cancellation residual (1.12% from BCS non-uniformity).

**Input files:**
- `computations/canonical_constants.py`
- Analytic curvature invariants from permanent results registry Section III

**Gate**: CONF-ANOM-69
- **PASS**: eps_H invariant under conformal anomaly (anomaly is uniform or sub-percent)
- **FAIL**: Non-uniform correction shifts n_s by > 0.001

**Output:**
- Script: `computations/s69_conformal_anomaly.py`
- Data: `computations/s69_conformal_anomaly.npz`
- Working paper: Section W4-C

---

### W4-D: EUCLID-LENSING-TRACKING-69 — CMB Lensing from Tracking DE

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: M7 from master collab (Mack #6)

**Prompt**:

Compute the tracking-induced modification to the CMB lensing convergence power spectrum C_l^{kappa kappa} at l = 100-500. The framework's tracking vacuum (c_s^2_DE = 0) means dark energy perturbations track matter perturbations, modifying the lensing potential growth at z < 2. This signature is independent of the ISW effect and may be detectable by CMB-S4.

**Computation steps:**

1. Compute the lensing convergence power spectrum C_l^{kk} = (9/4) * Omega_m^2 * H_0^4 * integral_0^{chi_*} dchi (chi_* - chi)^2 / (a^2 * chi_*^2) * P_Phi(l/chi, z(chi)) where P_Phi is the gravitational potential power spectrum.

2. For the tracking vacuum: P_Phi includes both matter and DE contributions. The Poisson equation gives Phi = -4*pi*G*a^2 * (rho_m*delta_m + rho_DE*delta_DE). With c_s^2 = 0: delta_DE = (1+w)/(1-3w) * delta_m * (rho_m/rho_DE). At z ~ 1 (Euclid lensing peak): rho_DE/rho_m ~ 1, so delta_DE adds ~2.2% to the potential.

3. Compute C_l^{kk} for three cases: LCDM (smooth DE), Framework (tracking c_s^2 = 0), and Quintessence (c_s^2 = 1). The FW-specific lensing modification Delta_kk = (C_l^{FW} - C_l^{Quint}) / C_l^{LCDM}.

4. Estimate CMB-S4 sensitivity: the lensing reconstruction noise N_l^{kk} from CMB-S4 (T noise 1 microK-arcmin, beam 1 arcmin, f_sky = 0.4). Compute SNR = sqrt(sum_l (2l+1)/2 * (Delta C_l^{kk})^2 / (C_l^{kk} + N_l^{kk})^2).

5. Report: Delta_kk(l) at l = 100-500, integrated SNR, and comparison to CMB-S4 detection threshold.

**Input files:**
- `computations/canonical_constants.py`
- `computations/s68_isw_tracking_test.npz` (for w_0 and Omega parameters)

**Gate**: EUCLID-LENS-69
- **PASS**: Delta > 0.5% at l = 100-500 (CMB-S4 detectable)
- **FAIL**: Delta < 0.1% (below all foreseeable detection)
- **INFO**: Delta 0.1-0.5% (marginal)

**Output:**
- Script: `computations/s69_euclid_lensing.py`
- Data: `computations/s69_euclid_lensing.npz`
- Plot: `computations/s69_euclid_lensing.png`
- Working paper: Section W4-D

---

### W4-E: SPECTRAL-DIM-BCS-PROTECTION-69 — d_s Protection Under BCS

**Agent**: `phonon-first-cosmologist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: M8 from master collab (Phonon-First #4)

**Prompt**:

Test whether the spectral dimension d_s on CG(24) satisfies an analog of the eps_H cancellation theorem under BCS dressing. If the BCS condensate modifies D_K by adding off-diagonal BdG pairing terms, the return probability P(sigma) = Tr(exp(-sigma * D_BdG^2)) changes, shifting d_s = -2 * d(ln P)/d(ln sigma). If this shift is < 2%, spectral rigidity is established as a universal property connecting Pillar VII (spectral dimension flow) to Pillar IV (flat-band BCS).

**Computation steps:**

1. Load the 8-band BCS spectrum at the fold from `computations/s68_bcs_dressed_mode.npz`: the BdG eigenvalues E_n = sqrt(epsilon_n^2 + Delta^2) for each of the 8 paired bands.

2. Compute the bare return probability on CG(24): P_bare(sigma) = (1/24) * sum_n exp(-sigma * lambda_n^2) where lambda_n are the 5704 D_K eigenvalues at L_max = 6.

3. Compute the BCS-dressed return probability: P_BCS(sigma) = (1/24) * sum_n exp(-sigma * E_n^2). The BdG spectrum has the same number of eigenvalues but shifted by the pairing gap.

4. Extract the spectral dimension at the fold: d_s(sigma) = -2 * d(ln P)/d(ln sigma) for both bare and BCS cases. Evaluate at sigma = 1/Lambda^2 where Lambda = 2.048 M_KK (the spectral action cutoff).

5. Compute the fractional shift: delta(d_s)/d_s = (d_s^{BCS} - d_s^{bare}) / d_s^{bare}.

6. Cross-check: at sigma → 0 (UV limit), d_s → 8 (full fiber dimension) for both cases. At sigma → inf (IR limit), d_s → 0. The BCS effect should only matter at intermediate scales sigma ~ 1/Delta^2.

**Input files:**
- `computations/s68_bcs_dressed_mode.npz`
- `computations/s61_fabric_landau_params.npz`
- `computations/canonical_constants.py`

**Gate**: SPEC-DIM-BCS-69
- **PASS**: delta(d_s)/d_s < 2% (spectral dimension protected)
- **FAIL**: delta(d_s)/d_s > 10% (spectral dimension sensitive to BCS)
- **INFO**: between 2% and 10%

**Output:**
- Script: `computations/s69_spectral_dim_bcs.py`
- Data: `computations/s69_spectral_dim_bcs.npz`
- Plot: `computations/s69_spectral_dim_bcs.png`
- Working paper: Section W4-E

---

### W4-F: CONFORMAL-FACTOR-TRANSIT-69 — Penrose Diagram Shape

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: M9 from master collab (SP #2)

**Prompt**:

Compute the exact conformal factor Omega(tau, k) of the transit spacetime. The transit from tau = 0.10 to tau = 0.30 at Mach 13.75 creates a causal structure analogous to a white hole. The conformal factor determines the shape of the Penrose diagram and the width of the "penumbra" region near k_tach where the Bogoliubov coefficients transition from |beta_k|^2 = 1 (fully excited) to |beta_k|^2 = 0 (vacuum).

**Computation steps:**

1. Load S(tau) and a(tau) from `computations/s67_transit_ps.npz`. The transit background gives the effective Hubble rate H(tau) = sqrt(S(tau) / (3 * a_2(tau))) and the Mukhanov variable z(tau).

2. Define the conformal coordinates: the conformal time eta = integral dt/a(t) and the tortoise coordinate r* = integral dk / omega(k). The conformal factor Omega relates the physical metric to the conformally flat one: ds^2 = Omega^2(tau,k) * ds^2_Minkowski.

3. For each k-mode, compute Omega(tau, k) = a(tau) * z(tau) / sqrt(2*k). This determines how the mode's physical wavelength relates to the conformal wavelength.

4. Identify the penumbra: the k-range where 0.1 < |beta_k|^2 < 0.9 (the transition region). Compute its width Delta k / k_tach. A narrow penumbra (Delta k / k_tach << 1) means the transition is sharp; a wide one means there's a gradual freeze-out.

5. Construct the Penrose diagram by plotting the null coordinates u = eta - r* and v = eta + r* in the compactified plane. Identify the three nested causal boundaries from SP's S68 review: tachyonic shell, BCS stretched horizon, cosmological event horizon.

6. Report: Omega(tau_fold, k) as a function of k, penumbra width, Penrose diagram shape.

**Input files:**
- `computations/s67_transit_ps.npz`
- `computations/canonical_constants.py`

**Gate**: CONF-FACTOR-69
- **INFO**: Report conformal factor at fold, penumbra width, diagram shape

**Output:**
- Script: `computations/s69_conformal_factor.py`
- Data: `computations/s69_conformal_factor.npz`
- Plot: `computations/s69_conformal_factor.png`
- Working paper: Section W4-F

---

### W4-G: BCS-DRESSED-HESSIAN-69 — Fold Stability Under BCS

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: M11 from master collab (Baptista B6)

**Prompt**:

Recompute the 36-eigenvalue spectral action Hessian at the fold with BCS dressing included. The S63 Hessian analysis found all 36 eigenvalues positive with a stabilization margin of alpha = 26x above critical (alpha_crit from S60). The BCS condensate modifies D_K by shifting eigenvalues by O(Delta = 0.52) and adding off-diagonal BdG terms. This could potentially destabilize some Hessian eigenvalues, especially the softest mode that controls the off-Jensen A_s channel (W1-E).

**Computation steps:**

1. Load the bare Hessian eigenvectors and eigenvalues from the S63 infrastructure. The 36 eigenvalues cluster into 10 groups (Ad(U(2)) decomposition, T8).

2. Compute the BCS-dressed spectral action: S_BCS(tau, h^a) = Tr sqrt(D_BdG^2(tau, h^a) / Lambda^2) where D_BdG includes the BCS pairing gap. The BdG heat kernel factorization (S64 T36: K_BdG(t) = exp(-Delta^2 t) * K_bare(t)) provides the connection.

3. Compute the Hessian: H_ab = d^2 S_BCS / d(h^a) d(h^b) evaluated at h = 0 (Jensen line) and tau = tau_fold = 0.19. This requires computing second derivatives of the BCS-dressed spectral action with respect to the 36 off-Jensen deformation parameters.

4. Diagonalize the BCS-dressed Hessian. Compare eigenvalues to the bare Hessian: are all 36 still positive? What is the revised stabilization margin?

5. Identify the softest mode: has its eigenvalue increased or decreased under BCS dressing? If decreased, by how much? Is the fold still a local maximum of S in the off-Jensen directions?

6. Cross-check: the trace of the Hessian should be related to the second Seeley-DeWitt coefficient through the heat kernel expansion. Verify Tr(H_BCS) against the a_2 BCS correction (11.6%).

**Input files:**
- `computations/s61_fabric_landau_params.npz`
- `computations/s68_bcs_dressed_mode.npz`
- `computations/canonical_constants.py`

**Gate**: BCS-HESS-69
- **PASS**: All 36 eigenvalues remain positive at Lambda = 2.048 M_KK (fold stable under BCS)
- **FAIL**: Any eigenvalue turns negative (BCS destabilizes the fold)
- **INFO**: All positive but margin reduced to < 5x (marginal stability)

**Output:**
- Script: `computations/s69_bcs_hessian.py`
- Data: `computations/s69_bcs_hessian.npz`
- Plot: `computations/s69_bcs_hessian.png`
- Working paper: Section W4-G

---

## V-C. Wave 5: Low Level + Remaining Data Tests (16 parallel, all independent)

### Lab Analog Designs

### W5-A: BEC-IMPEDANCE-ANALOG-69 — BEC Quench Protocol for |T(k)|^2 = 1

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: L6 from master collab (QA #2)

**Prompt**:

Design a BEC quench experiment that tests the framework's prediction |T(k)|^2 = 1 (Weinberg superhorizon conservation) in a laboratory analog. The framework claims that the scalar acoustic transfer function is identically unity for all superhorizon modes — the transit produces power but does not modify it during propagation. A BEC undergoing a rapid interaction quench (Feshbach resonance modulation) provides an analog: the quench creates Bogoliubov excitations whose power spectrum should be conserved at wavelengths longer than the healing length.

**Computation steps:**

1. Define the BEC analog parameters: map the framework's transit (Mach 13.75, duration 0.145 in units of tau) to a BEC Feshbach quench. The analog mapping is: c_BLV → sound speed c_s^{BEC}, k_tach → 1/xi (healing length), dt_transit → quench time dt_Q.

2. Compute the required quench parameters: scattering length a_s before and after quench, quench time dt_Q, and BEC density n_0, such that the Mach number M = v_Q/c_s^{BEC} matches 13.75 (where v_Q is the rate of change of c_s during the quench).

3. Predict the post-quench Bogoliubov spectrum: n_k = |beta_k|^2 for the BEC analog. For k << 1/xi (analog of superhorizon modes), the spectrum should be flat (all modes equally excited) — testing |T(k)|^2 = 1.

4. Design the measurement: momentum-space density after time-of-flight imaging. The signature is a flat n_k plateau for k < k_tach^{BEC} = 1/xi.

5. Estimate experimental requirements: atom number, temperature, trap geometry, imaging resolution. Identify which existing cold atom labs could perform this (MIT, JILA, Munich, etc.).

6. Report: protocol specification, predicted signal, required precision, feasibility assessment.

**Input files:**
- `computations/s67_transit_ps.npz` (for analog mapping)
- `computations/canonical_constants.py`

**Gate**: BEC-ANALOG-69 — INFO (design study)

**Output:**
- Script: `computations/s69_bec_analog.py`
- Data: `computations/s69_bec_analog.npz`
- Working paper: Section W5-A

---

### W5-B: BAW-SQUEEZE-ANALOG-69 — Phonon Squeeze Measurement Design

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: L7 from master collab (QA #3)

**Prompt**:

Design a bulk acoustic wave (BAW) resonator experiment to measure the non-Bunch-Davies squeeze parameter r_eff via phonon counting. The framework predicts that the BCS condensate produces a squeezed vacuum initial state with r_eff = 0.338. In a BAW resonator, coupling a phonon mode to a qubit (Chu-Cleland protocol) and performing a rapid coupling quench produces an analogous squeezed state. The variance of phonon number measurements reveals the squeeze parameter.

**Computation steps:**

1. Map the framework's BCS squeeze to the BAW analog: r_BCS → r_BAW through the coupling quench. The BAW mode frequency omega_BAW ~ 5 GHz, the quench modulates the piezoelectric coupling g.

2. Compute the predicted phonon variance: <n^2> - <n>^2 = sinh^2(r) * cosh^2(r) for a squeezed vacuum. At r = 0.338: <n> = sinh^2(0.338) = 0.118, var(n) = 0.132. The excess variance over Poissonian (var = <n>) is the squeeze signature.

3. Design the measurement protocol: (a) cool the BAW mode to n_thermal < 0.01 (dilution fridge, T < 10 mK), (b) perform a coupling quench at rate dg/dt matching the BCS transit rate, (c) read out phonon number via dispersive coupling to a transmon qubit.

4. Estimate the number of measurement shots needed to distinguish r = 0.338 from r = 0 (vacuum) at 3-sigma: N_shots ~ (sigma_n / delta_n)^2 * 9 where delta_n = <n(r=0.338)> - <n(r=0)> = 0.118.

5. Identify existing BAW-qubit platforms (Chu group at Yale, Cleland group at Chicago, NIST). Assess feasibility with current technology.

**Input files:**
- `computations/s67_multifield_delta_n.npz` (r_eff values)
- `computations/canonical_constants.py`

**Gate**: BAW-ANALOG-69 — INFO (design study)

**Output:**
- Script: `computations/s69_baw_analog.py`
- Data: `computations/s69_baw_analog.npz`
- Working paper: Section W5-B

---

### W5-C: Z2-BAW-ANALOG-69 — Breathing-Mode Selection Rule Test

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: L10 from master collab (QA #6)

**Prompt**:

Design a BAW resonator experiment testing the Z_2 selection rule that forbids single-Leggett gravitational decay (S67 T1). In the acoustic analog, couple two BAW modes with different symmetries (breathing vs dipole). The Z_2 parity predicts that single-mode decay is forbidden while pair decay is allowed. Measure the coupling rates Gamma_single and Gamma_pair as a function of mode overlap.

**Computation steps:**

1. Map the Leggett Z_2 parity to BAW modes: the breathing mode (even parity) cannot decay to a single phonon via a quadratic coupling (analogous to the gravitational a_2 moment). The dipole mode (odd parity) can decay.

2. Design a two-mode BAW system: mode A (breathing, even) at omega_A and mode B (waveguide, odd) at omega_B, coupled through a nonlinear piezoelectric element.

3. Predict the coupling rates: Gamma_pair ~ g^4 / omega_A (fourth-order process), Gamma_single = 0 (by symmetry). The ratio Gamma_pair/Gamma_single tests the selection rule.

4. Estimate the signal: at g ~ 10 MHz coupling, Gamma_pair ~ 10^{-4} Hz (measurable over minutes), while Gamma_single = 0 (or leaks at the 10^{-8} Hz level from symmetry breaking).

5. Report: protocol, predicted rates, required Q-factors, feasibility.

**Input files:**
- `computations/canonical_constants.py`

**Gate**: Z2-BAW-69 — INFO (design study)

**Output:**
- Script: `computations/s69_z2_baw.py`
- Data: `computations/s69_z2_baw.npz`
- Working paper: Section W5-C

---

### W5-D: FOUR-SPEED-3HE-69 — Velocity Hierarchy vs 3He-B

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: L8 from master collab (QA #5)

**Prompt**:

Compare the framework's four-velocity hierarchy (c_mod, c_BLV, c_BA, c_L from S64) to measured velocities in superfluid 3He-B. The framework is not an analogy to 3He-B but a parent theory (project memory: "correspondence is parent→child, not analogy"). If the velocity ratios in the framework match the velocity ratios in 3He-B to within the expected scaling, this provides an independent consistency check.

**Computation steps:**

1. Load the framework velocities from `computations/s64_four_velocities.npz` (if available) or compute from canonical_constants: c_mod = sqrt(S''(tau) / (2*a_2)), c_BLV = 0.485 (BLV sound speed), c_BA = sqrt(E_BA / (rho_s * V)) (BA phonon speed), c_L = sqrt(omega_L^2 / k_L^2) (Leggett mode speed).

2. Compute the velocity ratios: c_mod/c_BLV, c_BA/c_BLV, c_L/c_BLV.

3. Look up published 3He-B velocity data: first sound c_1, second sound c_2, pair-breaking velocity c_PB, Leggett frequency omega_L. Source: Vollhardt & Wolfle textbook values and Lancaster group measurements.

4. Compare ratios: does c_BA/c_BLV (framework) match c_2/c_1 (3He-B)? Does c_L/c_BLV match omega_L * xi / c_1? The parent-child relationship predicts the same RATIOS, not the same absolute values.

5. Report: velocity table, ratio comparison, qualitative assessment of correspondence.

**Input files:**
- `computations/canonical_constants.py`
- 3He-B velocity data from literature (hardcoded)

**Gate**: FOUR-SPEED-69 — INFO (comparison, no pass/fail for parent-child correspondence)

**Output:**
- Script: `computations/s69_four_speed.py`
- Data: `computations/s69_four_speed.npz`
- Working paper: Section W5-D

---

### Structural Computations

### W5-E: BELL-GGE-69 — Quantum Entanglement of GGE Relic

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: LOW-MEDIUM
**Carry-Forward**: L1 from master collab (Einstein #4)

**Prompt**:

Compute the CHSH Bell inequality value S(CHSH) for the GGE relic Bogoliubov pair correlations. The transit produces 59.8 quasiparticle pairs (S38, S67 T7 Brundobler-Elser guarantee). These pairs are produced in a squeezed vacuum state |r, phi> via the Bogoliubov transformation. For a two-mode squeezed vacuum, S(CHSH) = 2*sqrt(2)*tanh(r) which exceeds the classical bound S = 2 for any r > 0. This tests whether the GGE relic retains quantum entanglement or has decohered to a classical mixed state.

**Computation steps:**

1. Load the GGE occupation numbers from `computations/s38_gge_permanence.npz` (or equivalent): N_pair = 59.8, branch fractions, squeeze parameter r per branch.

2. For each GGE branch (acoustic, Leggett, optical), compute S(CHSH) = 2*sqrt(2)*tanh(r_I) using the branch-specific squeeze parameter. The acoustic branch has r_acoustic ~ 0.05 (small squeeze, S ~ 2.14), the Leggett branch r_L ~ 0.34 (moderate, S ~ 2.67), optical r_opt ~ 0.12 (small, S ~ 2.24).

3. Account for decoherence: the GGE evolves for ~132 e-folds from transit to today. Does the entanglement survive? For a Bogoliubov pair in a thermal bath at temperature T, S(CHSH, T) = 2*sqrt(2)*tanh(r)*exp(-Gamma_decoherence * t). The GGE is NOT thermal (Ordered Veil theorem), so decoherence operates only through gravitational interactions (Gamma_grav ~ H_0).

4. Report: S(CHSH) per branch, decoherence timescale, whether quantum entanglement persists to today.

**Input files:**
- `computations/s67_multifield_delta_n.npz`
- `computations/canonical_constants.py`

**Gate**: BELL-GGE-69 — PASS if S > 2 (quantum entanglement). INFO if S = 2 (classical).

**Output:**
- Script: `computations/s69_bell_gge.py`
- Data: `computations/s69_bell_gge.npz`
- Working paper: Section W5-E

---

### W5-F: TRANSIT-GW-SPECTRUM-69 — Gravitational Waves from Transit

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: LOW-MEDIUM
**Carry-Forward**: L2 from master collab (Einstein #6)

**Prompt**:

Compute the gravitational wave spectrum Omega_GW(f) emitted by the impulsive transit, redshifted to today's LISA and PTA frequency bands. The transit at Mach 13.75 is an impulsive deformation of the internal geometry that produces a quadrupole moment change. Using the Einstein-Infeld-Hoffmann (EIH) quadrupole formula adapted to the spectral action, compute the GW energy density.

**Computation steps:**

1. Compute the quadrupole moment change during the transit: Q_ij = integral d^8x rho(x) * (x_i x_j - delta_ij |x|^2/3) where rho is the spectral action energy density on SU(3). The transit changes Q by delta Q from the Jensen deformation.

2. Apply the EIH quadrupole formula: P_GW = (G/(5*c^5)) * <d^3Q/dt^3>^2. The impulsive transit gives d^3Q/dt^3 ~ delta_Q / dt_transit^3 where dt_transit ~ 0.145 / M_KK.

3. Compute the present-day GW energy density: Omega_GW(f) = (2*pi^2/(3*H_0^2)) * f^2 * S_h(f) where S_h(f) = (G * <d^3Q/dt^3>^2) / (4*pi^2*c^3*f^2*r^2) and r is the Hubble radius.

4. Redshift the spectrum: the transit occurs at T ~ 10^{15} GeV, redshifting the characteristic frequency f_transit ~ M_KK ~ 10^{15} GeV to today's f ~ f_transit * (T_CMB/T_transit) ~ 10^{-3} Hz (LISA band).

5. Compare to LISA sensitivity: Omega_GW^{LISA} ~ 10^{-13} at f ~ 10^{-3} Hz. The project memory (project_lisa-gw-prediction.md) estimates Omega_GW ~ 10^{-10} from domain walls.

6. Flag if Omega_GW > 10^{-12} at LISA frequencies.

**Input files:**
- `computations/s67_transit_ps.npz`
- `computations/canonical_constants.py`

**Gate**: TRANSIT-GW-69 — INFO. FLAG if Omega_GW > 10^{-12} at LISA.

**Output:**
- Script: `computations/s69_transit_gw.py`
- Data: `computations/s69_transit_gw.npz`
- Plot: `computations/s69_transit_gw.png`
- Working paper: Section W5-F

---

### W5-G: OFF-JENSEN-GRADIENT-69 — Jensen Line Trajectory Check

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: L5 from master collab (Baptista B5, byproduct of W1-E)

**Prompt**:

Compute the off-Jensen gradient of the spectral action at the fold and verify that the Jensen line (the one-parameter family of metrics parameterized by tau alone) is the physical trajectory. This is a byproduct of W1-E (off-Jensen SA): if the gradient perpendicular to the Jensen line is small compared to the gradient along it, the transit naturally follows the Jensen path without fine-tuning.

**Computation steps:**

1. If W1-E has already computed S(tau, epsilon), extract the gradient: nabla_a S = dS/d(h^a) at h = 0 (Jensen line), tau = tau_fold = 0.19.

2. Compare the perpendicular gradient |nabla_perp S| = sqrt(sum_a (dS/dh^a)^2) to the longitudinal gradient |dS/dtau|.

3. Compute the ratio: |nabla_perp S| / |dS/dtau|. If this is << 1, the Jensen line is an attractor and the transit naturally follows it. If ~ 1, the trajectory requires fine-tuning to stay on the Jensen line.

4. Check at multiple tau values: tau = 0.10, 0.15, 0.19, 0.25, 0.30 (before, at, and after the fold). The gradient should remain small throughout the transit.

5. Cross-check against the S65 Hessian: the off-Jensen gradient should be related to the Hessian eigenvalues by |nabla_perp| ~ sum_a lambda_a * delta h^a for small deformations.

**Input files:**
- W1-E output (if available): `computations/s69_off_jensen_sa.npz`
- `computations/canonical_constants.py`

**Gate**: OFF-JENSEN-GRAD-69 — PASS if |nabla_perp|/|dS/dtau| < 0.1. INFO otherwise.

**Output:**
- Script: `computations/s69_off_jensen_gradient.py`
- Data: `computations/s69_off_jensen_gradient.npz`
- Working paper: Section W5-G

---

### W5-H: KZ-PHASE-FNL-69 — KZ Phase Winding in Bispectrum

**Agent**: `phonon-first-cosmologist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: L9 from master collab (Phonon-First #5)

**Prompt**:

Map the Kibble-Zurek phase winding on CG(24) to a modulation of the bispectrum. The KZ defects produce domain walls where the BCS phase jumps. These phase jumps imprint a spatial modulation on phi_eff, which in turn modulates the squeezed vacuum initial state. Through the in-in bispectrum integral, this modulation produces a correction to f_NL^folded = 0.129 (S67 W2-C).

**Computation steps:**

1. Load the KZ domain structure from W2-B (if available) or from `s57_cayley_josephson.npz`.

2. Model the phase winding: at each domain wall, phi_eff jumps by 2*pi/3 (Z_3 winding) or a random angle (disordered winding). The domain wall density is N_DW ~ 3 walls per cell (from N_domains = 3).

3. Compute the phase modulation function phi_eff(x) = sum_DW phi_jump * Theta(x - x_DW) where Theta is the step function and x_DW are the domain wall positions.

4. Map to k-space: delta f_NL = (1/2*pi) * integral dk_1 dk_2 dk_3 * delta(k_1+k_2+k_3) * B(k_1,k_2,k_3) where B is the bispectrum contribution from the phase modulation.

5. Estimate |delta f_NL| / f_NL = |phase modulation correction| / 0.129. Flag if > 10%.

6. Cross-check: the phase modulation is a O(epsilon) correction where epsilon ~ (xi_KZ / L_system)^d ~ 0.1. So delta f_NL / f_NL should be O(0.1).

**Input files:**
- `computations/s57_cayley_josephson.npz`
- `computations/s67_gge_bispectrum.npz`
- `computations/canonical_constants.py`

**Gate**: KZ-FNL-69 — INFO. FLAG if |delta f_NL| > 0.013 (10% of 0.129).

**Output:**
- Script: `computations/s69_kz_phase_fnl.py`
- Data: `computations/s69_kz_phase_fnl.npz`
- Working paper: Section W5-H

---

### W5-I: PETROV-TYPE-BCS-69 — CMPP Classification with BCS

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: L11 from master collab (SP #4)

**Prompt**:

Determine the CMPP Petrov type of the transit spacetime with BCS backreaction included. The S50 permanent result (#14) established Lorentzian CMPP Type D for the bare Jensen-deformed SU(3) at all tau. The BCS condensate adds an additional stress-energy T_uv^{BCS} that modifies the Weyl tensor through Einstein's equations. Does the BCS backreaction maintain Type D or promote to algebraically general (Type G)?

**Computation steps:**

1. Load the Weyl tensor C_abcd(tau) from the analytic formulas (permanent results, Section III) and the BCS stress-energy from `s68_bcs_dressed_mode.npz`.

2. Compute the BCS-corrected Weyl tensor: the BCS condensate contributes to the Ricci tensor via R_ab = 8*pi*G * T_ab^{BCS}. The Weyl tensor changes as C_abcd → C_abcd + delta C_abcd where delta C comes from the trace-free part of delta R_ab.

3. Classify the corrected Weyl tensor using the CMPP algorithm: compute the 8 eigenvalues of the superenergy tensor. Type D requires exactly 2 distinct eigenvalues with multiplicities {3,4,1} (as found in S25). Any splitting of these multiplicities promotes to Type G.

4. Report: CMPP type at tau = tau_fold with BCS, eigenvalue splitting (if any), and how far from Type D.

**Input files:**
- `computations/s68_bcs_dressed_mode.npz`
- `computations/canonical_constants.py`

**Gate**: PETROV-BCS-69 — INFO: report CMPP type (D or G).

**Output:**
- Script: `computations/s69_petrov_bcs.py`
- Data: `computations/s69_petrov_bcs.npz`
- Working paper: Section W5-I

---

### W5-J: BCS-SURFACE-GRAVITY-69 — Spectral Gap Thermodynamics

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: LOW-MEDIUM
**Carry-Forward**: L4 from master collab (SP #3)

**Prompt**:

Compute the surface gravity kappa_BCS of the BCS spectral gap and the associated temperature T_BCS = kappa_BCS / (2*pi). The BCS gap Delta = 0.52 M_KK creates a spectral boundary in D_K analogous to a horizon in the energy spectrum. The surface gravity measures the "redshift" at this boundary: how rapidly eigenvalues accumulate near the gap edge.

**Computation steps:**

1. Load the D_K eigenvalue spectrum from `computations/s61_fabric_landau_params.npz` (5704 eigenvalues at L_max = 6).

2. Identify the gap edges: the BCS gap opens at E_gap = Delta = 0.52 M_KK. Count the eigenvalue density near the gap edge: rho(E) = dN/dE at E = Delta.

3. Define the analog surface gravity: kappa_BCS = (d/dE)(sqrt(E^2 - Delta^2)) |_{E=Delta} = lim_{E→Delta} sqrt(E^2-Delta^2)/(E-Delta) = 0 — the naive surface gravity vanishes because the BCS dispersion is quadratic near the gap. Use instead the second-order expression: kappa_BCS = sqrt(2*Delta * dE/dk |_{k=k_gap}).

4. Compute T_BCS = Delta / (2*pi) as the natural temperature scale of the spectral gap (the analog of the Hawking temperature for an acoustic horizon with gap Delta).

5. Compare T_BCS to the Gibbons-Hawking analog temperature T_GH = 66 M_KK (from S55 thermodynamic stabilization). The ratio T_BCS/T_GH = 0.52/(2*pi*66) = 0.00125 — the BCS gap is much colder than the cosmological horizon.

6. Report: kappa_BCS, T_BCS, T_BCS/T_GH ratio, physical interpretation.

**Input files:**
- `computations/s61_fabric_landau_params.npz`
- `computations/canonical_constants.py`

**Gate**: BCS-SURFACE-69 — INFO: report T_BCS and comparison to T_GH analog.

**Output:**
- Script: `computations/s69_bcs_surface_gravity.py`
- Data: `computations/s69_bcs_surface_gravity.npz`
- Working paper: Section W5-J

---

### Data Tests

### W5-K: EUCLID-GALAXY-FOLDED-69 — Bispectrum Folded Shape Forecast

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: LOW-MEDIUM
**Carry-Forward**: L3 from master collab (Mack #7)

**Prompt**:

Forecast the Euclid spectroscopic survey's sensitivity to the framework's predicted folded-triangle bispectrum shape (f_NL^folded = 0.129, S67 W2-C). The folded shape is the framework's unique bispectrum signature — it arises from the GGE relic's squeezed vacuum initial state and is absent in standard slow-roll inflation.

**Computation steps:**

1. Compute the galaxy bispectrum B_g(k_1, k_2, k_3) for the folded configuration (k_1 + k_2 = k_3) at z = 0.9-1.8 (Euclid spectroscopic). B_g = f_NL^folded * F_folded(k_1, k_2, k_3) * P(k_1) * P(k_2) + cyclic.

2. Estimate the Euclid bispectrum Fisher information: F^{-1/2} = sigma(f_NL^folded) from the galaxy survey volume V_eff ~ 20 Gpc^3 and number density n_g ~ 2e-3 (Mpc/h)^{-3}.

3. Compare sigma(f_NL^folded) to the predicted signal: f_NL^folded = 0.129. If sigma > 0.129, the folded shape is undetectable by Euclid. If sigma < 0.065, it's a 2-sigma detection.

4. Compare to CMB-S4 bispectrum sensitivity: sigma(f_NL^equil) ~ 5 for CMB-S4 — the galaxy bispectrum may be more sensitive to the folded shape because it probes smaller scales.

5. Report: sigma(f_NL^folded) from Euclid, detection significance, comparison to CMB-S4.

**Input files:**
- `computations/s67_gge_bispectrum.npz`
- `computations/canonical_constants.py`

**Gate**: EUCLID-FOLDED-69 — INFO: intermediate detection path assessment.

**Output:**
- Script: `computations/s69_euclid_folded.py`
- Data: `computations/s69_euclid_folded.npz`
- Working paper: Section W5-K

---

### W5-L: PVD-06-GALAXY-CL-69 — Galaxy Angular Power Spectrum

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: PVD-06 from S68 phonon-vs-data plan (MEDIUM priority, QUEUED)

**Prompt**:

Compute the galaxy angular power spectrum C_l^{gg} from the framework's matter power spectrum and compare to SDSS + DESI galaxy clustering data. The framework predicts P(k) with n_s = 0.9595, sigma_8 = 0.793, and T(k) = 1.0000 at all observable scales (WDM fraction negligible). The power spectrum shape is determined by Omega_m h^2, Omega_b h^2, n_s — all fixed by the framework with zero free parameters.

**Computation steps:**

1. Compute the linear matter power spectrum P(k) using the Eisenstein-Hu transfer function with framework parameters: Omega_m h^2 = 0.1424, Omega_b h^2 = 0.02237, n_s = 0.9595, sigma_8 = 0.793.

2. Project to angular power spectrum: C_l^{gg} = integral dk k^2 P(k) |W_l(k)|^2 where W_l is the window function for the galaxy sample. Use the Limber approximation C_l = integral dchi n(chi)^2 / chi^2 * P(l/chi, z(chi)) for l > 30.

3. Retrieve galaxy angular clustering data via astro MCP: query SDSS photometric galaxy catalog (SQL query for galaxy positions in a well-studied field), compute the angular auto-correlation or power spectrum from the galaxy positions.

4. Alternatively, use published SDSS angular power spectrum measurements (e.g., Huterer+01, Tegmark+02) as comparison data.

5. Compare the framework C_l^{gg} to observed. The dominant signal is the BAO wiggles at l ~ 100-300 and the overall amplitude (controlled by sigma_8).

6. Report: C_l^{gg} comparison, BAO feature match, amplitude ratio.

**Input files:**
- `computations/canonical_constants.py`
- Astro MCP for SDSS/DESI galaxy data

**Gate**: PVD-GALCL-69 — INFO: report power spectrum shape comparison.

**Output:**
- Script: `computations/s69_pvd06_galaxy_cl.py`
- Data: `computations/s69_pvd06_galaxy_cl.npz`
- Plot: `computations/s69_pvd06_galaxy_cl.png`
- Working paper: Section W5-L

---

### W5-M: PVD-08-CLUSTER-MF-69 — Cluster Mass Function

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: PVD-08 from S68 phonon-vs-data plan (MEDIUM priority, QUEUED)

**Prompt**:

Compare the framework's predicted cluster mass function (sigma_8 = 0.793, Omega_m = 0.315) against observed galaxy cluster counts. The cluster mass function is exponentially sensitive to sigma_8 — it's one of the best probes of the matter power spectrum normalization. The framework's sigma_8 = 0.793 is 2.2% lower than Planck's 0.811, which predicts ~10-15% fewer massive clusters.

**Computation steps:**

1. Compute the halo mass function dn/dM using the Press-Schechter or Tinker et al. (2008) fitting function with framework parameters: sigma_8 = 0.793, Omega_m = 0.315, n_s = 0.9595.

2. Compute the same for LCDM: sigma_8 = 0.811. The ratio dn/dM(FW) / dn/dM(LCDM) gives the expected difference in cluster counts as a function of mass.

3. Retrieve cluster catalog data via astro MCP (VizieR: SDSS cluster catalogs, or HEASARC for eROSITA). Alternatively, use published cluster counts from Planck SZ (Planck Collaboration XXIV, 2016) or ACT (Hilton+21).

4. Compute chi^2 for both FW and LCDM against the cluster counts. The framework's lower sigma_8 is in the SAME DIRECTION as the well-known sigma_8 tension between CMB and clusters.

5. Report: mass function comparison, chi^2 for FW and LCDM, assessment of whether the framework's sigma_8 resolves or exacerbates the cluster tension.

**Input files:**
- `computations/canonical_constants.py`
- Cluster catalog data (VizieR or published)

**Gate**: PVD-CLUST-69 — PASS if chi^2/dof < 3. INFO otherwise.

**Output:**
- Script: `computations/s69_pvd08_cluster.py`
- Data: `computations/s69_pvd08_cluster.npz`
- Plot: `computations/s69_pvd08_cluster.png`
- Working paper: Section W5-M

---

### W5-N: PVD-09-DESI-NZ-69 — DESI n(z) by Tracer

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: PVD-09 from S68 phonon-vs-data plan (MEDIUM priority, QUEUED)

**Prompt**:

Test the framework's predicted comoving volume element dV/dz against DESI DR1 galaxy number counts n(z) by tracer class (LRG, ELG, BGS, QSO). The framework predicts 3-5% smaller comoving volume at z > 0.3 (from w_0 = -0.918 vs w = -1). Each tracer class has a different selection function, so comparing the SHAPE of n(z) (after removing the selection function) tests the volume element.

**Computation steps:**

1. Compute dV/dz/dOmega for the framework: dV/dz = 4*pi * chi^2(z) * c / H(z) with H(z) from w_0 = -0.918. Compute the same for LCDM.

2. Query DESI DR1 via astro MCP: retrieve galaxy catalogs for each tracer class (LRG, ELG, BGS, QSO) in a fixed sky area. The S68 PVD-03 already retrieved 825 galaxies; expand the search to multiple 2-degree fields for better statistics.

3. For each tracer, construct the observed n(z) histogram. Model the selection function as n_obs(z) = phi(z) * dV/dz * S(z) where phi is the luminosity function and S is the selection probability.

4. Compare the RATIO n_obs(z) / n_LCDM(z) to the predicted ratio dV(FW)/dV(LCDM) = (H_LCDM/H_FW) * (chi_FW/chi_LCDM)^2. The selection function cancels in the ratio (assuming it's model-independent).

5. Report: n(z) per tracer, volume element ratios, consistency with w_0 = -0.918.

**Input files:**
- `computations/canonical_constants.py`
- Astro MCP for DESI DR1 galaxy catalogs

**Gate**: PVD-NZ-69 — INFO: report volume element comparison per tracer.

**Output:**
- Script: `computations/s69_pvd09_desi_nz.py`
- Data: `computations/s69_pvd09_desi_nz.npz`
- Plot: `computations/s69_pvd09_desi_nz.png`
- Working paper: Section W5-N

---

### W5-O: PVD-10-ISW-SDSS-69 — ISW-Galaxy Cross-Correlation from Data

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: PVD-10 from S68 phonon-vs-data plan (LOW priority but HIGH impact if ISW-BOLTZ-69 passes)

**Prompt**:

Attempt to measure (or set upper limits on) the ISW-galaxy cross-correlation using SDSS LRG data and Planck temperature maps. If W1-C (ISW-BOLTZ-69) finds a > 5% tracking signal, this computation determines whether it's already visible in existing data. The ISW effect at l < 30 is a ~1-3 microK signal, historically detected at 2-4 sigma.

**Computation steps:**

1. Retrieve SDSS LRG positions via astro MCP (SDSS SQL query: SELECT ra, dec, z FROM SpecObj WHERE class = 'GALAXY' AND z > 0.2 AND z < 0.7 AND ...). Construct the LRG galaxy overdensity map delta_g(theta, phi) in HEALPix pixels.

2. The Planck CMB temperature map is not directly available via MCP. Instead, use the theoretical C_l^{Tg} from W1-C and the SDSS LRG galaxy density to PREDICT the expected cross-correlation signal, rather than measuring it directly.

3. Compute the predicted C_l^{Tg} for the SDSS LRG sample using the galaxy bias b ~ 2 and the ISW kernel from W1-C. The signal-to-noise is S/N = sqrt(sum_l (2l+1) * f_sky * (C_l^{Tg})^2 / ((C_l^{TT} + N_l^{TT}) * (C_l^{gg} + N_l^{gg}))) where f_sky ~ 0.25 for SDSS.

4. Compare the predicted S/N to published SDSS ISW detections: Granett+08 (4.4 sigma), Giannantonio+08 (3.7 sigma). The framework predicts a 7.6-12.3% enhancement over LCDM, which would increase the expected S/N by ~10%.

5. Report: predicted C_l^{Tg} for SDSS LRG, S/N comparison to published detections, whether existing data can distinguish FW from LCDM.

**Input files:**
- W1-C output: `computations/s69_isw_boltzmann.npz`
- `computations/canonical_constants.py`
- Astro MCP for SDSS LRG catalog

**Gate**: PVD-ISW-69 — INFO: report predicted S/N and comparison to published detections.

**Output:**
- Script: `computations/s69_pvd10_isw_sdss.py`
- Data: `computations/s69_pvd10_isw_sdss.npz`
- Plot: `computations/s69_pvd10_isw_sdss.png`
- Working paper: Section W5-O

---

### W5-P: PVD-11-KAPPA-LENSING-69 — Gravitational Lensing Convergence

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: PVD-11 from S68 phonon-vs-data plan (MEDIUM priority, QUEUED)

**Prompt**:

Compute the gravitational lensing convergence kappa from the framework's parameters (Omega_m = 0.315, sigma_8 = 0.793) and compare to published weak lensing measurements. Weak lensing is sensitive to the combination S_8 = sigma_8 * sqrt(Omega_m / 0.3) which the framework predicts as S_8 = 0.793 * sqrt(0.315/0.3) = 0.813. The well-known "S_8 tension" between CMB (S_8 ~ 0.83) and weak lensing (S_8 ~ 0.76) means the framework falls BETWEEN the two — potentially in a sweet spot.

**Computation steps:**

1. Compute the framework's lensing convergence power spectrum C_l^{kk} using the Limber approximation with framework parameters: Omega_m = 0.315, sigma_8 = 0.793, n_s = 0.9595.

2. Compute S_8 = sigma_8 * sqrt(Omega_m/0.3) = 0.813 for the framework.

3. Compare to published weak lensing S_8 measurements: DES Y3 (S_8 = 0.776 +/- 0.017), KiDS-1000 (S_8 = 0.759 +/- 0.024), HSC Y3 (S_8 = 0.776 +/- 0.032), Planck CMB (S_8 = 0.834 +/- 0.016).

4. Compute the chi^2 of the framework's S_8 = 0.813 against each survey. The framework is 2.2 sigma above DES, 2.3 sigma above KiDS, 1.2 sigma above HSC, and 1.3 sigma below Planck. It's intermediate but on the Planck side.

5. If possible, compute the full C_l^{kk} comparison (not just S_8) against published lensing bandpowers.

6. Report: S_8 comparison table, chi^2 per survey, assessment of whether the framework resolves or sits within the S_8 tension.

**Input files:**
- `computations/canonical_constants.py`
- Published weak lensing measurements (hardcoded from papers)

**Gate**: PVD-KAPPA-69 — INFO: report S_8 comparison and chi^2 per survey.

**Output:**
- Script: `computations/s69_pvd11_kappa.py`
- Data: `computations/s69_pvd11_kappa.npz`
- Plot: `computations/s69_pvd11_kappa.png`
- Working paper: Section W5-P

---

## V-D. Wave 6: Synthesis

### W6-A: SESSION-69-ASSESSMENT

**Agent**: `mack-cosmic-bridge` | **Model**: opus | **Cost**: LOW

Consolidate all results. Update the observational comparison table with PVD results. Compute the updated A_s gap accounting (phi_eff, normalization, off-Jensen, sector BCS). Report the phonon-vs-data scorecard. Flag any new tensions or closures.

**Output**: Working paper: Synthesis section.

---

## VI. Constraint Gates Summary

| ID | Wave | Type | Condition | Fires If | Consequence |
|:---|:-----|:-----|:----------|:---------|:------------|
| PHI-EFF-69 | W1-A | CRITICAL | Enhancement in [1.3, 4.0] | Enhancement < 1.0 | Non-BD channel closes or widens gap |
| AS-NORM-69 | W1-B | CRITICAL | Decomposes into geometric factors | Irreducible physics factor | A_s gap magnitude changes |
| ISW-BOLTZ-69 | W1-C | HIGH | Delta > 5% at l < 30 | Delta < 1% | ISW tracking testable or killed |
| SECTOR-BCS-69 | W1-D | HIGH | alpha_s in [0.110, 0.126] | Outside [0.100, 0.140] | Particle physics sector viable or broken |
| OFF-JENSEN-69 | W1-E | HIGH | delta(z''/z) > 0.1 | delta < 0.01 | Off-Jensen channel open or closed |
| SQUEEZE-RECON-69 | W1-F | HIGH | Enhancement 0.07-0.30 OOM | Outside range | Squeeze estimate reconciled |
| TRANSIT-CONSIST-69 | W2-A | HIGH | Independent preds ≤ 4 | Contradiction found | Prediction count updated |
| SU11-PHASE-69 | W2-B | MEDIUM | <cos(phi_eff)> > 0 | <cos(phi_eff)> < 0 | Phase topology constructive or destructive |
| PVD-FSIG8-69 | W2-D | DATA | chi^2/dof < 2 | chi^2/dof > 3 | Growth rate test |
| PVD-SNE-69 | W2-E | DATA | chi^2/dof < 1.5 | Systematic > 0.05 mag | Supernova test |
| PVD-DA-69 | W2-F | DATA | chi^2/dof < 3 | chi^2/dof > 5 | Angular distance test |
| SONIC-PENROSE-69 | W3-A | HIGH | Bound ≥ observed A_s | Bound < A_s | Geometric A_s constraint |
| KK-HIGGS-69 | W3-C | MEDIUM | m_H in [120, 135] GeV | Outside [110, 150] | Higgs mass from KK threshold |
| EP-TRANSIT-69 | W4-A | MEDIUM | delta(eps_H) < 10^{-4} | > 10^{-3} | eps_H finite-time correction |
| SWAMP-69 | W4-B | MEDIUM | \|V'\|/V > 1 M_Pl | < 0.5 M_Pl | Swampland compatibility |
| CONF-ANOM-69 | W4-C | MEDIUM | eps_H invariant | n_s shifts | Conformal anomaly test |
| EUCLID-LENS-69 | W4-D | MEDIUM | Delta > 0.5% | < 0.1% | Lensing tracking signal |
| SPEC-DIM-BCS-69 | W4-E | MEDIUM | delta(d_s)/d_s < 2% | > 10% | Spectral dimension protection |
| BCS-HESS-69 | W4-G | MEDIUM | All 36 positive | Any negative | BCS stabilization |

---

## VII. Decision Points

**After Wave 1**:
- If PHI-EFF-69 PASS (enhancement > 1.3): Non-BD channel closes 0.11-0.60 OOM. Combined with BCS dressing (0.046 OOM) and off-Jensen (W1-E), may approach gap closure.
- If PHI-EFF-69 FAIL (enhancement < 1.0): Destructive interference. Non-BD channel WORSENS the gap. Off-Jensen becomes the sole remaining lever.
- If AS-NORM-69 reveals physics (not bookkeeping): The A_s gap magnitude itself changes. All prior closure budgets need revision.
- If ISW-BOLTZ-69 FAIL (Delta < 1%): ISW tracking killed by Boltzmann treatment. Remove from pre-registered observational discriminants. The framework loses its nearest unique CMB signature.
- If SECTOR-BCS-69 PASS: alpha_s(M_Z) and m_H back in viable range. If FAIL: particle physics sector has a new tension.

**After Wave 2**:
- If TRANSIT-CONSIST-69 reduces 7 predictions to ≤ 4: Fewer independent predictions than claimed. Update the pre-registered observations document.
- If SU11-PHASE-69 disagrees with W1-A: Phase topology introduces systematic uncertainty in phi_eff.
- PVD data results accumulate on the scorecard. If PVD-04 FAIL (SNe systematic): w_0 = -0.918 directly challenged.

**After Wave 3**:
- If SONIC-PENROSE-69 provides tight bound: Geometric A_s constraint independent of mode physics.
- W3-B + W3-D results update the combined observational forecast.
- W3-C (KK Higgs) depends on W1-D; if W1-D was INFO, W3-C may be inconclusive.

---

## VIII. Execution Notes

- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Output directory: `computations/`
- Script prefix: `s69_`
- Astro MCP available for data tests (W2-D, W2-E, W2-F, W5-L through W5-P)
- Total: **39 computations** across 6 waves (+ synthesis)
  - Wave 1: 6 parallel (CRITICAL + HIGH, no dependencies)
  - Wave 2: 6 parallel (consistency + data, can co-run with W1)
  - Wave 3: 4 parallel (depends on W1 outputs)
  - Wave 4: 7 parallel (medium refinements, no hard deps)
  - Wave 5: 16 parallel (low level + remaining data)
  - Wave 6: 1 synthesis
- Each agent writes results ONLY to their designated section in the working paper
- No TeamCreate — all agents are independent Agent tool calls
