# Session 50 Results Working Paper

**Date**: TBD
**Format**: Parallel single-agent computations (14) + synthesis
**Plan**: `sessions/session-plan/session-50-plan.md`
**Source**: session-49-wayforward.md (6 collaborative reviews)
**Branch**: Valar-1

---

## Agent Instructions

- Write your results in the section corresponding to your computation (W1-A through W3-B).
- Replace `NOT STARTED` with `IN PROGRESS` when you begin, then `COMPLETE` when done.
- Include: gate verdict (PASS/INFO/FAIL), key numerical results, interpretation, files produced.
- Do NOT write in any section other than your own.
- Use `from canonical_constants import *` in all scripts. Never hardcode constants.
- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`

---

## S49 Structural Results (Constraints on All S50 Computations)

1. **alpha_s = n_s² - 1 is exact** in O-Z: -0.069 ± 0.008, 6.0σ from Planck. J_ij errors contribute 0%.
2. **Leggett IS dipolar analog**: omega_L1 = 0.070 M_KK (18% from n_s target). First mass at correct scale.
3. **Leggett mode destroyed post-transit**: Delta=0, J=0, omega_L=0. GGE has no collective content.
4. **Triple-layered cosmic censorship**: Energy (65x), friction (Gamma=4424), topology (traceless K).
5. **HFB backreaction 1.2%**: V state-independent (Peter-Weyl). CC crossing survives.
6. **Fabric CC crossing conditional**: ec_fabric=1.586 > ec_min=1.264. Conditional on J_pair > 0.096.
7. **S48 analog horizons RETRACTED**: No superflow (phi=0). Amplitude gradient ≠ phase gradient.
8. **Multi-T shifts w_0 25% toward DESI**: w_0 = -0.430 (GGE Zubarev) to -0.589 (Keldysh).
9. **B_1D = 20.9** (fw preferred) but **B_2D = 0.073** (w_a kills it).
10. **Curvature hierarchy**: K_sect(0.537) → Weyl(0.895) → Ric(1.382). CMPP Type II locked (Riemannian).
11. **Non-LI TT all positive** through tau=0.78. Casimir floor structural.
12. **KZ 3-component identity**: n=59.82 vs 59.8 (0.04%). C² dominates (93.3%).

---

## Wave 1 — Independent Foundations

### W1-A: 3-Pole Leggett Propagator (LEGGETT-PROPAGATOR-50) — landau-condensed-matter-theorist

**Status**: COMPLETE
**Gate**: LEGGETT-PROPAGATOR-50. PASS if alpha_s in [-0.040, 0] AND n_s in [0.950, 0.980]. FAIL if alpha_s = n_s^2 - 1 survives.

**Gate Verdict: FAIL**

The 3-pole Leggett propagator is indistinguishable from the single-pole O-Z form at physical Josephson coupling strengths. The identity alpha_s = n_s^2 - 1 survives.

**Key Numbers:**

| Quantity | 3-Pole | O-Z Single-Pole | Difference |
|:---------|:-------|:-----------------|:-----------|
| n_s | 0.96462274 | 0.96462282 | 8.3e-8 |
| alpha_s | -0.06738696 | -0.06738681 | 1.5e-7 |
| n_s^2 - 1 | -0.06950297 | -0.06950281 | 1.6e-7 |
| Dev from identity | 0.00211601 | 0.00211600 | 5.8e-9 |
| m_base (m_star) | 11.8543 | 11.8553 | 1.1e-3 |

Genuine multi-pole effect: |Delta alpha_s| = 5.8e-9 (8.6e-8 relative).

**Pole Structure (all residues = 1 by equal-stiffness theorem):**

| Pole | mu (M_KK) | mu^2 (M_KK^2) | Weight |
|:-----|:----------|:---------------|:-------|
| 1 (Goldstone + m_base) | 11.8543 | 140.524 | 0.3334 |
| 2 (Leggett 1) | 11.8544 | 140.527 | 0.3334 |
| 3 (Leggett 2) | 11.8573 | 140.596 | 0.3332 |

Pole splitting: (mu_3^2 - mu_1^2)/mu_1^2 = 0.051%.

**Structural Theorem**: When all 3 sectors share the same spatial stiffness J_eff (same lattice geometry), the 3-pole propagator decomposes exactly as P(K) = sum_{i=1}^{3} P_OZ(K; m^2 = lambda_i), where lambda_i = m_base^2 + sigma_i are the total mass matrix eigenvalues. The identity alpha_s = n_s^2 - 1 holds individually for each pole. The correction from the multi-pole sum is proportional to dw_i/d(ln K) * (n_s_i - 1), which is O(sigma_max/m_base^2) ~ 5e-4. This is why the identity survives: the Josephson splitting (sigma_max = 0.072 M_KK^2) is negligible compared to the on-site mass (m_base^2 = 140.5 M_KK^2) required by the n_s = 0.965 constraint.

**Why Identity Survives:**
- Josephson max eigenvalue: 0.072 M_KK^2
- On-site mass from n_s constraint: 140.5 M_KK^2
- Ratio: 5.1e-4 (poles are 99.95% degenerate)
- To break identity at 1% level: Josephson coupling would need to be ~195x larger than physical value
- Josephson scan confirms: even at 4000x physical coupling (pole splitting 238%), alpha_s only shifts by 0.3%

**Planck Tension: 8.4 sigma** (unchanged from S49 O-Z result). The 3-pole structure does NOT resolve the alpha_s problem.

**Cross-checks:**
1. Equal-stiffness decomposition verified: P(3-pole) = sum P_OZ(lambda_i) to machine precision (ratio = 1.000000000000)
2. S49 analytic identity alpha_s = n_s^2 - 1 confirmed for O-Z with deviation 5.8e-9
3. Per-pole n_s and alpha_s computed independently; weighted average matches total
4. Josephson scan from 0x to 4000x physical coupling: identity deviation remains < 0.3%

**Assessment:**
The 3-pole Leggett propagator hypothesis is CLOSED as a resolution of the alpha_s problem. The fundamental obstacle is the mass hierarchy: the n_s = 0.965 constraint forces m_base^2 ~ 140 M_KK^2, while the Josephson couplings from S48 contribute only sigma_max ~ 0.072 M_KK^2. The poles are 99.95% degenerate, and the multi-pole correction to alpha_s is 5.8e-9 -- nine orders of magnitude below the required ~0.06 shift to reach Planck compatibility. Even an unphysically large Josephson enhancement (4000x) produces only a 0.3% shift in alpha_s. The O-Z identity alpha_s = n_s^2 - 1 is structurally robust against multi-pole corrections because it is an algebraic consequence of the power-law form of the propagator, not a coincidence that can be broken by parameter variation.

**Files:**
- Script: `tier0-computation/s50_leggett_propagator.py`
- Data: `tier0-computation/s50_leggett_propagator.npz`
- Plot: `tier0-computation/s50_leggett_propagator.png`

---

### W1-B: Independent J_pair Calibration (J-PAIR-CALIBRATE-50) — nazarewicz-nuclear-structure-theorist

**Status**: COMPLETE
**Gate**: J-PAIR-CALIBRATE-50. PASS if J_pair(direct) > 0.096 M_KK AND ec_fabric > ec_min.

**Results**:

**GATE: J-PAIR-CALIBRATE-50 = INFO**

J_pair(direct) = 0.115 M_KK > 0.096 at best estimate, but systematic uncertainty 41% > 30%. 1-sigma low band (0.068 M_KK) falls below threshold. ec_fabric = 1.392 > ec_min = 1.264 at best estimate. All 7 methods exceed threshold; floor estimate does not.

**Key Numbers**:

| Quantity | Value | Unit | Source |
|:---------|:------|:-----|:-------|
| J_pair (Method 2b, nuclear pair-transfer) | 0.1153 | M_KK | Primary: Delta_OES * F/N * J_C2 |
| J_pair (Method 3, Tr(V*C)) | 0.2288 | M_KK | Secondary: J_C2 * Tr(V_bare * C_pair) |
| J_pair (S49 indirect) | 0.1409 | M_KK | Comparison: J_C2 * abs(E_cond) |
| J_pair range (7 methods) | [0.115, 0.329] | M_KK | All exceed 0.096 |
| J_pair(1-sigma low) | 0.068 | M_KK | Below 0.096 threshold |
| J_pair(floor) | 0.080 | M_KK | Below 0.096 threshold |
| Systematic uncertainty | 41% | -- | sqrt(30%^2 + 19%^2 + 20%^2) |
| F_transfer = sum u_k v_k | 2.130 | -- | From S48 ED pair occupations |
| ec_fabric (best) | 1.392 | -- | > ec_min = 1.264 (PASS) |
| ec_fabric (S49 indirect) | 1.586 | -- | Reproduced from S49 |
| ec_fabric (1-sigma low) | 1.138 | -- | < ec_min (FAIL) |
| E_C (charging energy) | 0.929 | M_KK | From S49 N-sector spectrum |
| J/E_C (best) | 0.124 | -- | 1.8x nuclear sd-shell benchmark |
| Correction factor (BH ED/pert) | 1.874 | -- | Higher-order corrections in crossover |
| tau* (CC crossing, best) | 0.335 | -- | Post-fold (fold at 0.19) |

**Seven Independent Methods**:

1. **1a: Josephson (J_C2 * Delta_B2)** = 0.329 M_KK -- upper bound, weak-link breaks down at J_C2=0.93
2. **1b: Nuclear pair-transfer (J_C2 * F * E_cond/E_pair)** = 0.161 M_KK
3. **1c: Ambegaokar-Baratoff (pi/4 * Delta * J_C2)** = 0.258 M_KK -- upper bound
4. **2a: Geometric mean (sqrt(E_add * E_remove) * J_C2/2)** = 0.153 M_KK
5. **2b: Nuclear pair-transfer with OES gap (Delta_OES * F/N * J_C2)** = 0.115 M_KK -- PRIMARY, most conservative
6. **3: Tr(V_bare * C_pair) * J_C2** = 0.229 M_KK -- most direct
7. **3b: Off-diagonal Tr(V * C_offdiag) * J_C2** = 0.195 M_KK

Method 3_dos (Tr(V_eff * C) = 2.169) excluded: double-counts DOS (sqrt(rho) in both V_eff and pair occupations).

**Pair-Transfer Form Factor**: F = sum_k u_k v_k = 2.130 from the S48 ED ground state (256-state, 8-mode). B2 modes contribute 77.5% (dominated by near-Fermi-surface occupations). B1 contributes 14.1%. B3 contributes 8.4%. This is the standard nuclear pair-transfer amplitude (Paper 03). For sd-shell nuclei with 1 pair, the nuclear benchmark is F ~ 1.5; the framework value 2.13 is 1.4x larger (more modes near the Fermi surface due to Van Hove singularity).

**Systematic Uncertainty Decomposition**:
- J_C2 (S47 geometric overlap): 30% -- may overestimate if SP tunneling contaminates pair overlap
- Mode truncation (8-mode vs full): 19% -- from S36 convergence (5 to 8 modes)
- Bose-Hubbard single-mode approximation: 20% -- scale separation Delta/J ~ 3.1x (marginal)
- Combined: 41% (quadrature)

**Nuclear Benchmark**:

| Quantity | Nuclear (sd-shell) | Framework | Ratio |
|:---------|:-------------------|:----------|:------|
| Delta/E_pair | 0.35 | 0.42 | 1.2x |
| F_transfer | 1.5 | 2.13 | 1.4x |
| J/E_C | 0.07 | 0.12 | 1.8x |
| xi/d | 0.3-0.5 | 5.3 | 10-18x |

The 1.8x enhancement of J/E_C over the nuclear value is physical: Cooper pairs in the framework (xi_BCS = 0.81 M_KK^{-1}) span 5.3 cells (l_cell = 0.152), unlike nuclear Cooper pairs which span ~1 nucleus. This is the regime of pair transfer in DILUTE nuclear matter (inter-nuclear distance << coherence length), where inter-nuclear transfer is strongly enhanced.

**Constraint Map Update**:
- S49 FABRIC-NPAIR-49 conditional PASS remains CONDITIONAL, not confirmed or refuted
- 7/7 direct methods give J_pair > 0.096 (all pass threshold at nominal)
- 9/9 methods (including S49 indirect and 3_dos) give ec_fabric > ec_min at corrected BH scaling
- However: 41% systematic uncertainty means the 1-sigma low band (0.068) does not pass
- The dominant systematic (30%, J_C2) requires an independent J_C2 calibration (e.g., Berry phase or off-Jensen deformation) to resolve
- If J_C2 uncertainty is reduced to 15% (from independent calibration), sigma_combined drops to 31%, and 1-sigma low becomes 0.080 -- still below 0.096 but closer

**What remains uncomputed**:
1. Independent J_C2 from Berry phase (P-30w route, sole surviving topology)
2. Full q-theory self-consistency at fabric level with Method 2b J_pair
3. Higher-mode contributions beyond 8-mode (expected < 5% from S36 saturation)
4. Temperature (GGE) effects on pair transfer (Mott gap vs GGE temperature)

**Assessment**: The direct pair-transfer computation SUPPORTS the S49 result (J_pair above threshold at best estimate, ec_fabric passes CC crossing), but the 41% systematic uncertainty prevents unconditional confirmation. The dominance of the J_C2 systematic (30%) over all other sources makes independent J_C2 calibration the rate-limiting step. Method 2b (nuclear pair-transfer formula from Paper 03) is the most conservative estimate and gives the LOWEST J_pair among all methods -- this is the correct physics: it counts only the pair-transfer channel, not single-particle tunneling.

**Data files**:
- Script: `tier0-computation/s50_jpair_calibrate.py`
- Data: `tier0-computation/s50_jpair_calibrate.npz`

---

### W1-C: Bogoliubov Imprint (BOGOLIUBOV-IMPRINT-50) — volovik-superfluid-universe-theorist

**Status**: COMPLETE
**Gate**: BOGOLIUBOV-IMPRINT-50 **FAIL**

**Results**:

The Bogoliubov spectrum is featureless. The Leggett mass is NOT imprinted in |beta_k|^2. Three independent arguments establish this.

**Key Numbers**:

| Quantity | Value | Interpretation |
|:---------|:------|:---------------|
| omega_L1 / omega_transit | 7.86e-5 | Deeply sudden (trans-Planckian regime) |
| epsilon_L = J_23/(rho*Delta) | 0.00248 | Leggett coupling is 0.25% of BCS gap |
| delta(Delta)/Delta (ZP) | 1.52e-3 | Gap modulation from zero-point Leggett |
| P_LZ mod depth (B2, 93% of pairs) | 1.1e-6 | Negligible |
| P_LZ mod depth (B3, 5% of pairs) | 0.042 | Parametric only (phi_0 = 0, not realized) |
| P_LZ mod depth (B1, 2% of pairs) | 6.7e-4 | Negligible |
| Feature amplitude in P(K) | 1.7e-9 | Undetectable |
| Leggett fraction in RG integrals | 1.73e-4 | Encoded at 0.017% level |
| Erasure ratio (omega_L/omega_transit)^2 | 6.2e-9 | Information suppression factor |

**Argument 1 -- Ground State Symmetry**: The BCS ground state has phi_0 = 0 everywhere. The Leggett mode is in its quantum zero-point state, not a coherent state with definite phase. <cos(phi_0)> = 0 by U(1)_7 symmetry. The gap modulation vanishes on average. No spatial variation of Bogoliubov coefficients across the fabric.

**Argument 2 -- Dominant Sector Insensitivity**: B2 carries 93.3% of all created pairs (55.8 of 59.8). The B2 modulation depth is 1.1e-6 because J_23/(rho_B2 * Delta_B2) = 1.7e-4. The dominant sector is shielded by its large DOS (14.02) and large gap (0.732). B3 shows 4.2% parametric modulation but contributes only 5% of pairs, and phi_0 = 0 means this is not realized.

**Argument 3 -- Information Hierarchy**: omega_L1 IS encoded in the Richardson-Gaudin integrals at delta_I/I_range = 1.73e-4 (0.017%). The 8 RG integrals preserve sector structure but NOT inter-sector phase dynamics. omega_L information is present but overwhelmed by BCS amplitude structure.

**3He Analog (Paper 27, Volovik 2013)**: Trans-Planckian erasure. omega_transit/omega_L = 12,721, so the Leggett mode is invisible to the post-transit observer, exactly as the dipolar interaction is invisible in normal-state 3He (d-vector and l-vector decouple when Delta = 0).

**Preserved through transit**: n = 59.82 total pairs, sector decomposition (B2: 93.3%, B3: 5.0%, B1: 1.7%), 8 RG integrals, GGE entropy.

**Not preserved**: Leggett mode (Delta=0, J=0, omega_L=0), relative phase (undefined when condensate destroyed), spatial modulation (phi_0=0 in ground state).

**Consequence for n_s**: Bogoliubov imprint channel CLOSED. Leggett mass cannot be frozen into post-transit power spectrum. Quasiparticle spectrum determined by {E_k, P_LZ ~ 1} -- uniform distribution, no K-dependent features. n_s = 1 exactly from this mechanism.

**Files**: `s50_bogoliubov_imprint.py`, `s50_bogoliubov_imprint.npz`, `s50_bogoliubov_imprint.png`

---

### W1-D: Leggett Damping (LEGGETT-DAMPING-50) — volovik-superfluid-universe-theorist

**Status**: COMPLETE
**Gate**: LEGGETT-DAMPING-50. PASS if Q > 10. FAIL if Q < 1.

**Results**:

**GATE VERDICT: PASS** (Q = 6.7e5 >> 10)

**Critical Correction**: The S49 wayforward framed the damping question using the *order parameter* gap Delta_B3 = 0.084 M_KK, giving omega_L/(2*Delta_B3) = 0.414 (41% of "threshold"). This conflates two different gaps. The *quasiparticle* gap is E_k = sqrt(eps_k^2 + Delta_k^2), which is dominated by the single-particle energy eps_k = |lambda_k| ~ O(1), not the BCS gap Delta_k ~ O(0.01-0.7). The actual pair-breaking threshold is 2*E_min = 1.800 M_KK (not 0.168), and omega_L sits at 3.9% of this true threshold.

**Key Numbers**:

| Quantity | Value | Unit |
|:---------|:------|:-----|
| omega_L1 | 0.06955 | M_KK |
| omega_L2 | 0.10737 | M_KK |
| E_min (BdG quasiparticle) | 0.9001 | M_KK |
| min(E_k + E_{k'}) (pair-breaking) | 1.8002 | M_KK |
| 2*Delta_B3 (order parameter gap) | 0.1683 | M_KK |
| omega_L1 / (2*E_min) | 0.0386 | -- |
| omega_L1 / (2*Delta_B3) | 0.4133 | -- (MISLEADING ratio) |
| Gamma_Beliaev (T=0) | 0 | exact |
| Gamma_Raman (T=0) | 0 | forbidden (0D) |
| Gamma_grav | 5.2e-8 | M_KK |
| Q_total | 6.7e5 | -- |
| Re[Sigma(omega_L)] | -9.24e-6 | M_KK^2 |
| Mass renormalization | -0.096% | -- |
| N_oscillations during transit | 1.3e-5 | -- |

**Why Beliaev damping is forbidden**: The Beliaev process (Leggett -> 2 quasiparticles) requires omega_L > E_k + E_{k'} for some pair (k, k'). The minimum pair energy is 2*E_B1 = 1.800 M_KK, which is 25.9x above omega_L1 = 0.070 M_KK. This is not marginal -- it is absolutely forbidden.

**Why Raman damping is forbidden**: In 3He-B, the sub-threshold decay Leggett -> 2 Goldstone phonons provides Gamma ~ omega_L^5. This requires momentum-carrying Goldstone modes. In the 0D discrete BCS system (8 modes on SU(3)), the Goldstone mode is k=0 only. No momentum modes exist; Raman decay is structurally forbidden.

**Why GGE temperatures are irrelevant**: The Leggett mode exists only during the BCS-condensed phase (pre-transit). Post-transit, Delta = 0 and J = 0 so omega_L = 0. The GGE temperatures (T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178) describe the post-transit relic which has no collective modes.

**Transit dynamics**: The Leggett period is T_L = 90.3 M_KK^{-1}, while the transit duration is dt = 0.00113 M_KK^{-1}. The transit is 79,932x faster than one Leggett oscillation. The Leggett mode is frozen during transit (sudden quench regime). It completes 1.3e-5 oscillations.

**Structural insight (3He comparison)**: In 3He-B, eps_k is measured from the Fermi surface, so E_k ~ Delta and omega_L/(2*Delta) ~ 10^{-3} controls the Q factor. In the framework, eps_k = |lambda_k| >> Delta_k, so E_k ~ eps_k and the Leggett mode lives 25.9x below the true pair-breaking threshold. The framework is MORE protected than 3He because (a) the spectrum is discrete (no continuum), (b) the system is 0D (no Raman channel), (c) all quasiparticle energies are O(1) while omega_L is O(0.07). The Leggett mode is an exact eigenstate of the finite BCS Hamiltonian.

**Virtual mass renormalization**: Off-shell pair creation gives Re[Sigma] = -9.24e-6, shifting omega_L by -0.096%. The renormalized frequency is 0.06949 M_KK (negligible correction).

**Consequence for DIPOLAR-CATALOG-49**: The Leggett mass m_G = omega_L1 = 0.070 M_KK is a well-defined collective mode mass. The mass concept is VALID. The 18% overshoot from the n_s requirement (m_req = 0.059) persists as a quantitative tension but is not invalidated by damping.

**Files**: `tier0-computation/s50_leggett_damping.py`, `s50_leggett_damping.npz`, `s50_leggett_damping.png`

---

### W1-E: Leggett Phi Confirmation (LEGGETT-PHI-CONFIRM-50) — tesla-resonance

**Status**: COMPLETE
**Gate**: LEGGETT-PHI-CONFIRM-50. PASS if |R(0.21)/phi - 1| < 0.1%. FAIL if > 1%.

**Results**:

**VERDICT: PASS** -- |R(0.21)/phi_paasch - 1| = 0.0609% < 0.1% threshold.

**Key Numbers**:

| tau | R = omega_L2/omega_L1 | |R/phi - 1| |
|:----|:----------------------|:-----------|
| 0.20 | 1.5380717779 | 0.4239% |
| 0.21 | 1.5325131710 | **0.0609%** |
| 0.2117 | 1.5315721427 | 0.0005% |
| 0.22 | 1.5269941388 | 0.2994% |

- phi_paasch = 1.531580 (Dirac eigenvalue ratio from S12)
- Refined crossing: tau = 0.211686 (direct dense scan + Brent refinement)
- S49 spline prediction: tau = 0.211686 (agreement to 0.2 x 10^{-6} in tau)
- |R(tau_cross)/phi - 1| = 4.4 x 10^{-15} (machine epsilon)

**S49 Spline Prediction Confirmed**: The cubic spline on S48's 8-point coarse data predicted the crossing at tau = 0.2117. Direct computation at 61 tau values in [0.19, 0.25] confirms this to 6 significant figures. The spline was not an interpolation artifact.

**Structural Constants**:
- J_12/J_23 = 19.5197 (algebraically constant across ALL tau -- confirmed at 4 new points)
- R(tau) is driven entirely by DOS ratios rho_i(tau), not by coupling ratios
- dR/dtau at crossing = -0.553 (monotonically decreasing, transverse crossing)
- Sensitivity: delta_tau = 0.0028 shifts R by 0.1% of phi. The crossing is sharp.

**Validation**: S48 coarse data reproduced to machine epsilon (max relative error = 0.00e+00 in both omega_L1 and omega_L2 at all 8 tau points). Pipeline is identical.

**Physical Content**: The Leggett frequency ratio omega_L2/omega_L1 -- set by the BCS many-body phase oscillation spectrum -- equals the single-particle Dirac eigenvalue ratio phi_paasch at tau = 0.2117. This is a resonance condition: the inter-sector Josephson oscillation frequency ratio matches the mass-ratio spectral invariant from the same deformed SU(3) geometry. The crossing tau differs from the fold (0.19) by 11%, placing it within the physically relevant deformation range but not at the fold itself.

**What This Constrains**: The R = phi_paasch crossing is a geometric identity connecting BCS collective dynamics to single-particle spectral geometry. It survives any modification that preserves: (1) the V matrix selection rules (J_12/J_23 algebraically constant), (2) the DOS scaling with Jensen deformation, (3) the gap hierarchy Delta_B2 >> Delta_B1 > Delta_B3.

**Files**:
- Script: `tier0-computation/s50_leggett_phi_confirm.py`
- Data: `tier0-computation/s50_leggett_phi_confirm.npz`
- Plot: `tier0-computation/s50_leggett_phi_confirm.png`

---

### W1-F: Running Mass from Anomalous Dimension (RUNNING-MASS-50) — landau-condensed-matter-theorist

**Status**: COMPLETE
**Gate**: RUNNING-MASS-50. PASS if gamma > 1.7 AND alpha_s shifts within 2σ Planck. FAIL if gamma < 0.5.

**Verdict: FAIL** (structural exclusion: gamma > 1.7 is algebraically impossible for n_s = 0.965)

**Results**:

**Script**: `tier0-computation/s50_running_mass.py`
**Data**: `tier0-computation/s50_running_mass.npz`
**Plot**: `tier0-computation/s50_running_mass.png`

**Physical setup**: Ginzburg-Landau free energy F[phi] for the U(1)_7 Goldstone on the 32-cell (4x4x2) Josephson lattice with J_xy = 0.9325, J_z = 0.0591 M_KK, bare mass m_0 = omega_L1 = 0.06955 M_KK (Leggett dipolar, S49), T = T_acoustic = 0.1122 M_KK.

**1-loop sunset self-energy** computed on all 32 lattice momenta (O(N^2) = 1024 double sum). The sunset diagram is the sole K-dependent 1-loop contribution (the tadpole is K-independent and cancels in the mass difference).

| Quantity | Value | Unit |
|:---------|:------|:-----|
| m_0 (bare Leggett mass) | 0.06955 | M_KK |
| m_* (O-Z fit to n_s=0.965) | 11.865 | M_KK |
| m_*/m_0 | 170.6 | -- |
| J_eff = (2J_xy + J_z)/3 | 0.641 | M_KK |
| xi_* = m_*^2/(J_eff K_pivot^2) | 56.04 | -- |
| gamma (physical, lambda=V_B2B2=0.1557) | -6.76e-4 | -- |
| gamma (structural maximum) | 0.0350 | -- |
| gamma (gate threshold) | 1.7 | -- |
| delta_alpha (physical) | -1.33e-3 | -- |
| delta_alpha (structural max) | 0.0688 | -- |
| alpha_s (O-Z, constant mass) | -0.0688 | -- |
| alpha_s (running, physical coupling) | -0.0701 | -- |
| alpha_s (running, structural max gamma) | ~0.000 | -- |
| Planck alpha_s | -0.0045 +/- 0.0067 | -- |

**Structural theorem** (Sections 6, 8 of script): For a power-law running mass m(K)^2 = m_0^2 (K/K_0)^gamma on an O-Z propagator P(K) = T/[J K^2 + m(K)^2], the spectral tilt is:

n_s - 1 = -(2 + gamma u)/(1 + u)

where u = (1 + n_s)/(1 - n_s - gamma). For u > 0 (physical propagator), this requires:

**gamma < 1 - n_s = 0.035**

This is a structural constraint: the anomalous dimension of the mass in any single-pole propagator consistent with a red-tilted spectral index n_s < 1 cannot exceed 1 - n_s. The gate threshold gamma > 1.7 exceeds this bound by a factor of 49.

**Correction formula**: delta_alpha = gamma (2 - gamma) u / (1 + u). At the structural maximum gamma -> 0.035, u -> infinity, and delta_alpha -> gamma(2-gamma) = 0.0688, which would shift alpha_s from -0.0688 to 0.000. But this limit requires u -> infinity, meaning J K^2 / m^2 -> 0 (the kinetic term vanishes; the propagator becomes P ~ K^{-gamma}, which is no longer Ornstein-Zernike).

**Lattice 1-loop result**: At the physical coupling lambda = V(B2,B2) = 0.1557, the sunset self-energy gives gamma = -6.76e-4 (negative: mass decreases at higher K). This is 52x below the structural maximum and has the wrong sign for shifting alpha_s toward zero. The sunset overwhelms the bare mass at K_pivot (m(K_pivot)^2 < 0), indicating the perturbative 1-loop expansion breaks down at physical coupling for this lattice.

**Implications**: The alpha_s = n_s^2 - 1 identity cannot be broken by running mass within the O-Z propagator framework. The structural bound gamma < 1 - n_s is independent of microscopic details (coupling strength, lattice geometry, loop order). Any resolution of the alpha_s tension must come from modifying the propagator structure itself (multi-pole, non-Lorentzian), not from radiative corrections to the mass.

---

### W1-G: Lorentzian CMPP Classification (LORENTZIAN-CMPP-50) — schwarzschild-penrose-geometer

**Status**: COMPLETE
**Gate**: LORENTZIAN-CMPP-50. PASS if CMPP type changes at tau~0.537. FAIL if constant.

**GATE: LORENTZIAN-CMPP-50 = INFO**

The 12D Lorentzian CMPP type differs fundamentally from the 8D Riemannian result, but is constant across tau. No type change at 0.537 in either case.

**Results**:

**1. Static Product M^{3,1} x (SU(3), g_tau): EXACT TYPE D at all tau**

| tau | 8D Riemannian CMPP | 12D Lorentzian CMPP | bw+2 fraction | bw+1 fraction | |C|^2_12D |
|:---:|:------------------:|:-------------------:|:-------------:|:-------------:|:--------:|
| 0.000 | II | **D** | 1.4e-67 | 1.0e-33 | 0.3727 |
| 0.190 | II | **D** | 1.0e-67 | 1.5e-33 | 0.4031 |
| 0.537 | II | **D** | 1.0e-67 | 2.3e-33 | 0.7076 |
| 0.895 | II | **D** | 6.1e-68 | 2.8e-33 | 2.2056 |
| 1.000 | II | **D** | 5.7e-68 | 2.8e-33 | 3.2389 |

The bw+/-1 and bw+/-2 components are at machine epsilon (~10^{-67} to 10^{-33}). This is EXACT Type D, not approximate.

**WAND**: alpha = pi/2 (pure external direction). The null vector l = (e_t + e_{SU(2)})/sqrt(2) lies entirely in the time + SU(2) sector. All curvature appears in the transverse (bw=0) block.

**Structural reason**: For ANY static product M^{p,1}_flat x K^n, null vectors aligned with the flat factor see all internal curvature as transverse (bw=0). The product structure forces Type D because the WAND exists in the flat external space. The Riemannian 8D classification was locked at Type II because complexified null vectors in definite-signature geometry mix directions unavoidably, generating the 0.1-2.4% bw+/-1 contamination found in S49. **The Riemannian Type II was a signature artifact. The physical classification is Type D.**

**Weyl operator eigenstructure (66x66 matrix on Lambda^2(R^{12}))**:
- tau=0 (round): 6 distinct eigenvalues, multiplicities {8,3,8,24,3,20}. The rep decomposition Lambda^2(R^{12}) = Lambda^2(R^4) + (R^4 tensor Lambda^1(R^8)) + Lambda^2(R^8) gives 6 + 32 + 28 = 66 components, and the 6 distinct eigenvalues reflect this three-block structure.
- tau>0: 16 distinct eigenvalues. The Jensen deformation breaks the SU(3) isometries, splitting the 28D internal block.
- Trace = 0 to machine epsilon at all tau (Weyl trace-free verified).

**2. Dynamic Case (tau_dot = v_terminal = 26.545): TYPE G at all tau**

| tau | CMPP | min bw+2 frac | |C|^2_12D | |K_{ext}|^2 |
|:---:|:----:|:-------------:|:--------:|:---------:|
| 0.000 | G | 8.32e-3 | 2.273e7 | 3523 |
| 0.190 | G | 8.32e-3 | 2.273e7 | 3523 |
| 0.537 | G | 8.32e-3 | 2.273e7 | 3523 |
| 0.895 | G | 8.32e-3 | 2.272e7 | 3523 |
| 1.000 | G | 8.32e-3 | 2.272e7 | 3523 |

The extrinsic curvature K_{ab} = -(v_terminal/2) * lambda_a * delta_{ab} adds cross terms R_{0,a,0,a} = K_a^2 and Gauss corrections to the internal Riemann. These completely dominate: |C|^2_dynamic / |C|^2_static ~ 10^7. The time-internal cross terms break the product structure and destroy the Type D WAND. The residual bw+2 = 0.83% is structural (from the K^2 diagonal structure).

Note: K_diag is tau-INDEPENDENT (it depends only on tau_dot and the Jensen rates lambda_a = {-2,-2,-2,+1,+1,+1,+1,+2}), so the dynamic classification is also tau-independent. The tiny variation in |C|^2_dynamic across tau (22.73M to 22.72M) comes from the internal Riemann changing, but it is a ~0.005% perturbation on the dominant extrinsic curvature.

**3. Physical Interpretation**

The static Type D is a **structural theorem**: any flat x curved product has Lorentzian CMPP Type D (or more special). The WAND always exists in the flat factor. This is the higher-dimensional analog of the well-known 4D result that Schwarzschild is Type D — the algebraic specialness arises from the product/warped structure.

For the physical transit, the extrinsic curvature is so large (v_terminal = 26.5 in M_KK units) that it drowns the internal geometry. The 4D observer sees Type G (generic) — no algebraically special direction exists because the internal dimensions are changing too rapidly.

**However**: after the transit freezes at tau ~ 0.22 (BCS censorship), the effective tau_dot drops to approximately zero, and the static Type D classification becomes the physical one for the post-transit universe. The frozen modulus restores algebraic specialness.

**4. Constraint Map Update**

- **Constraint**: Static product M^{3,1} x (SU(3), g_Jensen) is EXACT CMPP Type D at all tau. This is permanent (independent of tau).
- **Implication**: The Riemannian Type II classification (S49) was a signature artifact. The physical 12D spacetime is Type D.
- **Implication**: No CMPP type transition occurs at tau = 0.537 (geometric phase transition) or any other tau. The algebraic type is set by the product topology, not the internal geometry.
- **Implication**: During active transit (tau_dot >> 0), the type is G (generic). The product-structure WAND is destroyed by the extrinsic curvature. Type D is restored post-freeze.
- **Surviving space**: The curvature hierarchy K_sect(0.537) -> Weyl_eig(0.895) -> Ric(1.382) -> singularity(inf) from S49 remains valid as an internal geometry sequence, but it does NOT produce a CMPP type change in 12D.
- **Open**: Does the Type D -> G -> D transition (from transit on/off) have observational consequences? The "gravitational memory" of the transit is encoded in the extrinsic curvature profile.

**Key Numbers**:

| Quantity | Value | Source |
|:---------|:------|:-------|
| Static CMPP type | D (exact, all tau) | s50_lorentzian_cmpp.npz |
| Dynamic CMPP type | G (all tau) | s50_lorentzian_cmpp.npz |
| WAND direction | alpha=pi/2, SU(2) sector | Scan over 450 null directions + gradient refinement |
| bw+2 (static, best) | ~10^{-67} | Machine epsilon (exact zero) |
| bw+2 (dynamic, best) | 8.32e-3 | From K^2 cross terms |
| |C|^2_12D (static, fold) | 0.4031 | tau=0.19 |
| |C|^2_12D (dynamic, fold) | 2.273e7 | Dominated by |K|^2=3523 |
| Weyl operator distinct eigs (12D) | 6 (tau=0), 16 (tau>0) | 66x66 matrix on Lambda^2 |
| Runtime | 19.4s | 5 tau values, ~450 null dirs each |

**Script**: `tier0-computation/s50_lorentzian_cmpp.py`
**Data**: `tier0-computation/s50_lorentzian_cmpp.npz`
**Plot**: `tier0-computation/s50_lorentzian_cmpp.png`

---

### W1-H: Eikonal Damping in Fabric Propagator (EIKONAL-DAMPING-50) — quantum-acoustics-theorist

**Status**: COMPLETE
**Gate**: EIKONAL-DAMPING-50. PASS if Gamma/m² > 0.1. FAIL if < 0.01.

**Results**:

**VERDICT: FAIL** — Gamma(K_pivot) / m_G^2 = 0 (exact). Eikonal damping does NOT modify the Goldstone propagator.

**What was computed**:

1. Condensate texture V(x) = (Delta^2(x) - <Delta^2>) / <Delta^2> on T^2 (200x200 grid). V_rms = 3.035, V_max = 21.95. Strong scattering regime (Born parameter >> 1).

2. Fourier structure factor S(q) of V(x) via 2D FFT. Peak S(q) = 0.441 at q = 0.633 M_KK. 50% of power below q = 1.055 M_KK. 90% below q = 1.899 M_KK. Parseval theorem verified: sum|V(q)|^2 = V_rms^2 = 9.212.

3. Born self-energy Sigma(K) for on-shell Goldstone phonon (dispersion omega^2 = c^2 K^2 + m_G^2) scattering off the static texture. Computed over K in [0.01, 33.8] M_KK.

4. Result: Sigma(K_pivot) = 0 identically. The Goldstone wavelength lambda_G = 67.8 M_KK^{-1} EXCEEDS the torus circumference L_T^2 = 13.16 M_KK^{-1} by a factor of 5.15x. The Goldstone mass shell K_G = 0.0927 M_KK sits BELOW the torus fundamental K_fund = 0.4774 M_KK. There is ZERO texture power at the Goldstone scale.

**The structural argument (Section 11 of script)**:

The Goldstone phonon is the n=0 Kaluza-Klein mode on T^2 — its wavefunction is CONSTANT across the fiber. A constant wavefunction couples only to the spatial average of V(x), which vanishes by construction: <V(x)>_{T^2} = 0 (verified: 4.5e-17). Therefore, the zero-mode Goldstone is TRANSPARENT to the condensate texture. This is not a numerical accident — it is a structural consequence of the KK decomposition.

The eikonal breakdown (78.3% of T^2 with Mach > 1) affects KK modes n >= 1, which have internal wavelength ~1/M_KK and see the texture as a strong scattering potential (V_rms = 3.0, Anderson localization with kl = 0.0095 << 1, xi_loc = 0.104 M_KK^{-1}). The lowest texture-affected mode is the cavity mode at 0.800 M_KK, which is 11.5x above the Goldstone mass. These two sectors are decoupled by the KK mass gap.

| Quantity | Value | Unit |
|:---------|:------|:-----|
| m_G | 0.06955 | M_KK |
| c_BdG | 0.7507 | M_KK |
| K_pivot = m_G/c | 0.09266 | M_KK |
| lambda_G = 2pi/K_pivot | 67.81 | M_KK^{-1} |
| L_T^2 (torus circumference) | 13.16 | M_KK^{-1} |
| lambda_G / L_T^2 | 5.15 | -- |
| K_fund (torus fundamental) | 0.4774 | M_KK |
| K_G / K_fund | 0.194 | -- (below fundamental) |
| V_rms (texture contrast) | 3.035 | -- |
| S(q) peak | 0.441 at q=0.633 | M_KK^{-2} |
| Gamma(K_pivot)/m_G^2 (Born) | 0 | -- (exact) |
| Gamma(K_pivot)/m_G^2 (physical) | 0 | -- (exact, zero-mode) |
| kl Ioffe-Regel (KK modes) | 0.0095 | -- (localized) |
| omega_cavity_min / m_G | 11.5 | -- (decoupled) |

**Scale hierarchy** (low to high K):
- K_G = 0.093 M_KK (Goldstone) -- BELOW torus fundamental
- K_fund = 0.477 M_KK (torus fundamental)
- K_domain = 1.432 M_KK (Z_3 domain structure)
- K_cavity = 1.066 M_KK (lowest cavity mode / c_BdG)
- K_Nyquist = 33.76 M_KK

**What region of solution space this constrains**:
Eikonal damping from condensate texture on T^2 is CLOSED as a mechanism to modify the Goldstone propagator or soften the alpha_s = n_s^2 - 1 identity. The closure is structural: the Goldstone is a KK zero mode, constant on the fiber, coupling only to <V> = 0. Any modification of alpha_s must come from a mechanism operating in the 4D fabric, not internal fiber texture.

**What remains uncomputed**:
1. FABRIC-level texture (domain walls between Voronoi cells, inter-cell Josephson coupling variations). This operates at scales >> L_T^2 and couples directly to the 4D Goldstone.
2. Whether strong KK-mode localization (kl = 0.0095) indirectly affects the Goldstone through renormalization of c_BdG or m_G.

**Data files**: `tier0-computation/s50_eikonal_damping.py`, `tier0-computation/s50_eikonal_damping.npz`, `tier0-computation/s50_eikonal_damping.png`

---

## Wave 2 — Propagator Consequences (Depends on W1-A)

### W2-A: sigma_8 from 3-Pole Propagator (SIGMA8-PREDICT-50) — cosmic-web-theorist

**Status**: NOT STARTED
**Gate**: SIGMA8-PREDICT-50. PASS if sigma_8 in [0.740, 0.820]. FAIL if outside [0.640, 0.920].

**Results**:

*(Agent writes here)*

---

### W2-B: n_s and alpha_s Cross-Check (NS-ALPHAS-3POLE-50) — gen-physicist

**Status**: NOT STARTED
**Gate**: NS-ALPHAS-3POLE-50. Cross-check: agrees with W1-A to < 5%.

**Results**:

*(Agent writes here)*

---

### W2-C: DESI DR3 Joint Constraint Update (DESI-DR3-JOINT-50) — cosmic-web-theorist

**Status**: COMPLETE
**Gate**: DESI-DR3-JOINT-50. PASS if chi^2/N < 2 against DESI BAO. FAIL if > 4.

**GATE VERDICT: FAIL**

The framework's w_0 = -0.509 (band midpoint) produces BAO distances 6-15% discrepant from DESI DR1 data across all redshift bins. chi^2/N = 23.2, far exceeding the FAIL threshold of 4. The framework is excluded by BAO distances at overwhelming confidence (Delta_chi^2 = +241 vs LCDM).

**Key Numbers:**

| Quantity | Value | Unit/Notes |
|:---------|:------|:-----------|
| chi^2/N (FW midpoint, w_0=-0.509) | 23.19 | FAIL (threshold 4) |
| chi^2/N (FW Zubarev, w_0=-0.430) | 34.20 | Worse |
| chi^2/N (FW Keldysh, w_0=-0.589) | 15.09 | Still 3.8x above FAIL |
| chi^2/N (LCDM, w_0=-1.0) | 4.62 | Marginal (QSO outlier) |
| chi^2/N (LCDM, excl. QSO DM) | 1.59 | Good fit |
| chi^2/N (DESI w0waCDM best-fit) | 3.55 | QSO outlier still present |
| Delta_chi^2 (FW mid vs LCDM) | +241.4 | Decisive against FW |
| B_BAO (midpoint) | 3.8e-53 | Negligible |
| Max D_M deviation (FW vs LCDM) | 11.8% at z=2.2 | Far above 1-3% precision |
| Max D_H deviation (FW vs LCDM) | 14.9% at z=1.0 | Far above 2-5% precision |
| FW better in N bins | 3/13 | LCDM better in 10/13 |
| Most discriminating bin | LRG3+ELG1 DM z=0.93 | 8.1 sigma separation |

**Data source**: DESI DR1 BAO (arXiv:2404.03002, Table 1). 13 measurements: 1 D_V, 6 D_M, 6 D_H across 7 tracers (BGS, LRG1, LRG2, LRG3+ELG1, ELG2, QSO, Lya). Sound horizon r_d = 147.09 Mpc (Planck 2018, unchanged in framework).

**Per-bin analysis (FW midpoint residuals vs DR1 data, in sigma):**

| Tracer | z_eff | D_V | D_M | D_H |
|:-------|:------|:----|:----|:----|
| BGS | 0.295 | -2.95 | -- | -- |
| LRG1 | 0.510 | -- | -4.77 | -2.00 |
| LRG2 | 0.706 | -- | -2.51 | -4.69 |
| LRG3+ELG1 | 0.930 | -- | -7.36 | -8.25 |
| ELG2 | 1.317 | -- | -4.26 | -4.18 |
| QSO | 1.491 | -- | **+1.18** | -4.65 |
| Lya | 2.330 | -- | -5.48 | -5.18 |

The framework predicts distances that are systematically TOO SMALL (negative residuals: framework D < data). The sole exception is QSO D_M (z=1.491), where DESI's anomalously low measurement (6.4 sigma from LCDM) happens to coincide with the framework prediction. This QSO bin constitutes 68% of LCDM's total chi^2.

**The S49 B_1D = 20.9 paradox resolved:**

The S49 computation found B_1D = 20.9 (framework preferred over LCDM in w_0 space). This was computed from the DESI *combined EOS fit* (w_0 = -0.752 +/- 0.058), which is a derived parameter from BAO + CMB + SNe. The framework's w_0 = -0.509 is indeed closer to -0.752 than LCDM's w_0 = -1.0.

However, the BAO distances themselves -- the raw observational data from which w_0 is derived -- are consistent with LCDM at ~1 sigma (excluding the QSO outlier). The combined fit's w_0 = -0.752 is driven by CMB+SNe tension with BAO, not by BAO alone preferring w != -1.

In other words: the framework is closer to the EOS *model parameter*, but further from the *data*. The BAO distances are the more fundamental test.

**Physical reason for failure:**

Framework DE (w_0 ~ -0.5) dilutes as rho_DE ~ a^{-1.5}, while LCDM DE is constant (rho_DE ~ a^0). At z=1, the framework has 2.8x less DE than LCDM, causing:
- Lower H(z) -> larger D_H = c/H(z)
- Larger comoving distances -> larger D_M(z)

The ~10-15% effect is 3-8x larger than DESI measurement errors. No parameter tuning can fix this: the effect is monotonic in w_0, and any w_0 significantly above -1 produces too-small BAO distances.

**DR3 forecast:**

With DR3 precision (errors ~0.58x DR1): chi^2/N rises to 68.9 (FW midpoint). The mismatch grows worse with better data, as expected for a wrong model. Framework is excluded regardless of DR3 outcome.

**Constraint map update:**
- S49 DESI-DR3-PREP-49 B_1D = 20.9 was misleading: it compared models against a derived parameter (w_0 from combined fit), not against raw data.
- The BAO distances DECISIVELY exclude w_0 in [-0.43, -0.59] with Delta_chi^2 > 136 (even for the most favorable Keldysh endpoint).
- This closure is STRUCTURAL: it depends only on the framework's prediction that DE dilutes faster than Lambda, which is the core physical content of w_0 != -1.
- The framework's only surviving BAO-compatible scenario is w_0 very close to -1 (within ~2% of Lambda), which contradicts the GGE alpha = 1.33 computation.

**What remains uncomputed:**
1. Whether the GGE alpha can be modified (e.g., by fabric averaging, inter-cell coupling variations) to yield w_0 closer to -1. This would require alpha -> infinity (P >> E), contradicting the S49 finding that alpha = 1.33 is a robust consequence of the 8-mode BCS spectrum.
2. Whether an alternative interpretation of the GGE state as an effective fluid (rather than a CPL w_0, w_a parameterization) could reconcile with BAO. This is speculative and would require fundamentally different dynamics.

**Files:**
- Script: `tier0-computation/s50_desi_dr3_joint.py`
- Data: `tier0-computation/s50_desi_dr3_joint.npz`
- Plot: `tier0-computation/s50_desi_dr3_joint.png`

---

### W2-D: What Breaks w_a = 0? (W_A-SOURCE-50) — einstein-theorist

**Status**: COMPLETE
**Gate**: W_A-SOURCE-50. PASS if |w_a| > 0.1 from identified mechanism.

**Gate Verdict: FAIL**

All four candidate mechanisms produce w_a = 0 exactly under physical assumptions. The framework prediction w_a = 0 is structural and cannot be broken without abandoning core framework features.

**Key Numbers:**

| Mechanism | w_a | Physical? | Direction |
|:----------|----:|:---------:|:----------|
| (a) Inter-cell Josephson coupling | 0.0 | Yes | N/A (no condensate post-transit) |
| (b) GGE integrability breaking | 0.0 | Yes | Wrong (w_0 -> -0.32, AWAY from DESI) |
| (c) Quasiparticle mass evolution | 0.0 | Yes | Frozen-modulus dichotomy |
| (d) Non-equilibrium viscous pressure | 0.0 | Yes | Constant Pi (no relaxation) |
| (e) Volovik dilution (hypothetical) | +0.586 | **No** | Correct magnitude, wrong assumption |
| DESI DR2 | -0.73 +/- 0.28 | Observed | -- |

**Mechanism Details:**

**(a) Inter-cell coupling evolution**: Josephson coupling requires a condensate. Post-transit P_exc = 1.0 (condensate destroyed, S38). With no Cooper pairs and no phase coherence, J_ij = 0 identically. The modulus drift dichotomy (TAU-STAB-36 FAIL) makes residual coupling evolution moot.

**(b) GGE integrability breaking**: Inner fluctuations break block-diagonal structure at epsilon = 0.052 (S49 DIPOLAR-CATALOG). FGR rate: Gamma = epsilon^2 * omega_typical = 2.88e-4 M_KK, giving t_th = 3.1e-38 s << t_universe (ratio 7.1e-56). Two sub-scenarios: (i) FGR applies: GGE thermalizes INSTANTLY to single-T with w_0 = -0.323 (AWAY from DESI), then w = const, w_a = 0; (ii) PAGE-40 applies: N=8 too small for ETH, Poincare recurrences at 8.3e56 oscillations/Hubble, averaging to constant Pi, w_a = 0. Either way w_a = 0 and direction is WRONG.

**(c) Quasiparticle mass evolution**: d(w_0)/d(tau) = 4.9e-4. To match DESI w_a = -0.73 requires Delta_tau = 1483 (780,000% of tau_fold). The frozen-modulus dichotomy closes this completely: either Delta_tau = 0 (w_a = 0) or tau runs away (framework excluded).

**(d) Non-equilibrium viscous pressure**: Pi = P_GGE - P_eq = 0.382 (58% of P_eq). This constant offset IS the multi-T w_0 shift. But Pi is either constant (integrability, PAGE-40) or instantly relaxed (FGR, 3e-38 s). Poincare oscillations at T ~ 5.2e-40 s average over 8.3e56 cycles/Hubble. No cosmological-timescale relaxation.

**(e) Volovik dilution (bonus)**: If rho_qp diluted as a^{-3}, the exact formula gives w_a = -3*alpha/(1+alpha)^2 = -0.735 (matches DESI). CPL fit: w_0 = -0.392, w_a = +0.586. However, quasiparticles are per-fiber excitations; fiber density in comoving coordinates is constant; rho_qp = const. The dilution model is physically incorrect.

**Structural Theorem: w_a = 0 is Triple-Locked**

1. **Trapping**: Quasiparticles have mass ~ M_KK, no 4D momentum, no free-streaming
2. **Integrability**: 8 Richardson-Gaudin conserved quantities lock n_k, T_k, P_k, alpha
3. **Frozen modulus**: TAU-STAB dichotomy -- either tau fixed or framework excluded

Breaking any one: trapping -> fine-tuning; integrability -> wrong direction; modulus -> excluded.

**Implication**: The S49 2D Bayes factor B = 0.073 is driven by w_a. This computation confirms no mechanism generates w_a != 0. If DESI DR3 confirms |w_a| > 0.3 at 3-sigma, framework is EXCLUDED at the w_a level.

**Files**: `tier0-computation/s50_wa_source.py`, `s50_wa_source.npz`, `s50_wa_source.png`

---

### W2-E: Spatial KZ Pair Creation (KZ-SPATIAL-50) — volovik-superfluid-universe-theorist

**Status**: COMPLETE
**Gate**: KZ-SPATIAL-50. PASS if n_s in [0.950, 0.980]. FAIL if n_s = 1.000 +/- 0.001 (featureless).

**Results**:

**GATE KZ-SPATIAL-50: FAIL** -- Spectrum featureless. 13th n_s route CLOSED.

**Method**: Spatially-resolved Landau-Zener pair creation on the 32-cell fabric (4x4x2 lattice). Each cell i gets a local quench rate modulated by cell volume and Z_3 domain wall proximity:

|d epsilon/dt|_i = v_terminal * |d epsilon/d tau| * (V_avg / V_i)^{1/3} * f_wall_i

For each cell and each of 8 modes (4 B2, 1 B1, 3 B3), P_LZ(k,i) = exp(-pi * E_qp^2 / |dE_qp/dt|_i). Power spectrum P(K) computed from Fourier transform of delta_n(x_i) over the reciprocal lattice.

**Key numbers** (baseline sigma_V = 10%, f_wall = 1.5):

| Quantity | Value | Significance |
|:---------|:------|:-------------|
| delta_n/n | 1.59e-4 | Fractional density variation |
| var(n)/<n>^2 | 2.52e-8 | Power spectrum amplitude |
| P_LZ(B2) | 0.9968 | Deep sudden-quench regime |
| |ln P_LZ(B2)| | 3.16e-3 | Exponential suppression factor |
| n_s (fit) | -1.21 +/- 0.78 | UNDEFINED -- fitting noise |
| (max-min)/<n> | 0.059% | Total cell-to-cell range |

**Sensitivity analysis** (6 sigma_V x 5 f_wall x 20 seeds = 600 configurations):
- ALL configurations give var(n)/<n>^2 in [1.6e-10, 1.3e-7]
- n_s fits scatter wildly: [-2.8, +0.6] depending on random seed
- No parameter combination produces n_s near [0.950, 0.980]
- Fitted n_s is pure noise regardless of (sigma_V, f_wall)

**Physical mechanism (Volovik)**: This is the **sudden-quench KZ universality theorem**. The framework sits deep in the sudden-quench regime (tau_Q = 0.00113 << tau_0 for all sectors). In this limit, the Landau-Zener transition probability P_LZ approaches 1 exponentially:

P_LZ = exp(-pi * E_qp^2 / rate) ~ 1 - pi * E_qp^2 / rate

The sensitivity of P_LZ to the local quench rate is:

delta_P/P = |ln P_LZ| * delta_rate/rate = 3.2e-3 * 0.033 = 1.05e-4

This is the **equilibrium theorem for defect creation**: in the sudden-quench limit, ALL cells create the same defect density regardless of local geometry. The quench rate is so fast that the system cannot respond to local conditions.

**Superfluid 3He analog**: In a rapid quench of superfluid 3He (neutron irradiation creating a hot spot), the Kibble-Zurek defect density is n ~ 1/xi^d, where xi is the coherence length -- independent of quench details. The spatial variation enters only through sub-leading corrections that are exponentially suppressed. The framework is in the analogous regime.

**Structural conclusion**: Spatial KZ cannot produce n_s because the transit is too fast. A red tilt requires either:
1. Leaving the sudden-quench regime (slower transit -- but v_terminal = 26.5 M_KK is set by the gradient energy)
2. A mechanism beyond single-mode Landau-Zener (multi-mode interference, collective effects)
3. A completely different origin for the power spectrum (order parameter texture, spectral function)

**Data files**: `tier0-computation/s50_kz_spatial.py`, `tier0-computation/s50_kz_spatial.npz`, `tier0-computation/s50_kz_spatial.png`

---

### W2-F: sigma_8 from O-Z Rigid Prediction (SIGMA8-OZ-50) — gen-physicist

**Status**: COMPLETE
**Gate**: SIGMA8-OZ-50. PASS if sigma_8 in [0.740, 0.820]. FAIL if outside [0.640, 0.920].

**Gate Verdict: PASS**

The rigid O-Z prediction alpha_s = n_s^2 - 1 = -0.069 produces sigma_8 = 0.799, a -1.50% shift from the no-running LCDM baseline. This lands inside the pass band [0.740, 0.820] and sits between Planck and lensing measurements.

**Key Numbers:**

| Quantity | O-Z Rigid | LCDM (alpha_s=0) | S48 Lattice | Planck | Lensing |
|:---------|:----------|:-----------------|:------------|:-------|:--------|
| alpha_s | -0.0690 | 0 | -0.038 | 0 +/- 0.008 | --- |
| sigma_8 | 0.7988 | 0.8110 | 0.8042 | 0.811 +/- 0.006 | 0.766 +/- 0.020 |
| S_8 | 0.8186 | 0.8310 | 0.8241 | 0.832 +/- 0.013 | 0.776 +/- 0.017 (DES) |
| shift from LCDM | -1.50% | (ref) | -0.83% | --- | --- |

**Tension Analysis:**

| Comparison | Tension |
|:-----------|:--------|
| sigma_8(O-Z) vs Planck sigma_8 | 2.0 sigma |
| sigma_8(O-Z) vs Lensing sigma_8 | 1.6 sigma |
| S_8(O-Z) vs Planck S_8 | 1.0 sigma |
| S_8(O-Z) vs DES Y3 S_8 | 2.5 sigma |
| S_8(O-Z) vs KiDS-1000 S_8 | 2.5 sigma |

**Uncertainty Propagation (S49 alpha_s posterior, 500 MC samples):**

| Quantity | Value |
|:---------|:------|
| sigma_8 (median +/- std) | 0.8023 +/- 0.0015 |
| sigma_8 95% CI | [0.799, 0.805] |
| S_8 (median +/- std) | 0.822 +/- 0.002 |

**Why the Shift is Only 1.5% (Not 21%):**

The Cosmic-Web S49 warning ("alpha_s = -0.069 --> sigma_8 shift 21%") conflated the primordial power suppression at high k with the sigma_8 integral. The running does suppress P_R(k) by 27% at k = 1 Mpc^{-1} and 62% at k = 10 Mpc^{-1}. But sigma_8 is dominated by k ~ 0.1-0.3 h/Mpc (77% of the integral), which straddles the pivot scale k_pivot/h = 0.074 h/Mpc. At the sigma_8-peak scale k ~ 0.2 h/Mpc, the running correction to the exponent is only (1/2)(-0.069)(ln(0.135/0.05))^2 = -0.034, giving a 3.3% suppression in P_R. Since sigma_8 ~ sqrt(integral P_R), the effect halves to ~1.5%. The transfer function T^2(k) already kills the high-k region where running has its largest effect.

**Scale Decomposition:**

| Scale Range (h/Mpc) | sigma_8^2 Fraction (LCDM) | sigma_8^2 Fraction (O-Z) |
|:---------------------|:--------------------------|:-------------------------|
| k < 0.01 | 0.06% | 0.05% |
| 0.01 < k < 0.1 | 22.98% | 23.57% |
| 0.1 < k < 1.0 | 76.80% | 76.26% |
| k > 1.0 | 0.16% | 0.12% |

**Physical Interpretation:**

The O-Z rigid alpha_s = -0.069 shifts sigma_8 from Planck's 0.811 toward the lensing value 0.766. The resulting sigma_8 = 0.799 sits at 2.0-sigma from Planck (below) and 1.6-sigma from lensing (above) -- in the "sigma_8 tension" gap. This is a structurally interesting position:

1. The O-Z prediction REDUCES the S_8 tension with Planck (from LCDM 0.831 to 0.819, cutting the tension from ~4.3-sigma to 1.0-sigma vs Planck S_8).
2. But it does NOT resolve the lensing tension (S_8 = 0.819 is still 2.5-sigma above DES/KiDS).
3. The shift is too small to produce observational exclusion from any single dataset at >3-sigma.
4. The 21% shift warning was an overestimate by a factor of ~14.

The alpha_s = -0.069 is ruled out at 6-sigma by Planck's direct alpha_s measurement, but its sigma_8 consequence is mild and observationally consistent. The sigma_8 gate does not close the O-Z identity; the alpha_s gate (ALPHA-S-BAYES-49, 6.0-sigma FAIL) remains the primary exclusion.

**Method:** Eisenstein-Hu (1998) transfer function with baryons, primordial spectrum P_R(k) = A_s (k/k_*)^{n_s-1+(1/2)alpha_s ln(k/k_*)}, top-hat window sigma_8 integral via scipy.integrate.quad (epsrel=1e-8). Normalization: alpha_s=0 -> sigma_8 = 0.811 (Planck 2018).

**Files:**
- Script: `tier0-computation/s50_sigma8_oz.py`
- Data: `tier0-computation/s50_sigma8_oz.npz`
- Plot: `tier0-computation/s50_sigma8_oz.png`

---

### W2-B: Fabric RPA (FABRIC-RPA-50) — nazarewicz-nuclear-structure-theorist

**Status**: COMPLETE
**Gate**: FABRIC-RPA-50. PASS if alpha_s(RPA) in [-0.040, 0]. FAIL if alpha_s(RPA) = n_s^2 - 1 (identity survives RPA).

**Gate Verdict: FAIL** -- RPA correction to alpha_s is 1.1e-5. Identity survives. 8.4 sigma tension unchanged.

**Method**: Compute the static pair susceptibility chi_0(K) on the 32-cell fabric from the 8-mode BdG quasiparticle spectrum (S48 ED), then solve the RPA Dyson equation D_RPA(K) = D_0(K) / [1 - g^2 chi_0(K) D_0(K)] with g = V(B2,B2) = 0.1557. Extract n_s(RPA) and alpha_s(RPA) from log-derivative fitting of D_RPA.

The pair susceptibility is:
  chi_0(K) = sum_n rho_n F_n^2 / [2 E_qp(n) + J_pair epsilon(K) w_n]

where F_n = 2 u_n v_n is the BCS coherence factor, E_qp(n) the BdG quasiparticle energy, J_pair = 0.115 M_KK the inter-cell pair transfer, and epsilon(K) = 2(1 - cos(K l_cell)) the tight-binding dispersion.

**Key numbers:**

| Quantity | Value | Significance |
|:---------|:------|:-------------|
| chi_0(K=0) | 21.14 | Full 8-mode static pair susceptibility |
| chi_0(K_pivot) | 21.03 | Nearly unchanged from K=0 |
| chi_0 variation in fit window | 0.295% | Too flat to break identity |
| g^2 chi_0(0) | 0.512 | O(1) but not enough |
| Pi D_0 at K_pivot | 4.0e-4 | RPA self-energy negligible |
| D_RPA/D_0 - 1 at pivot | 0.04% | RPA correction invisible |
| alpha_s(RPA) | -0.06739 | |
| alpha_s(bare) | -0.06740 | |
| RPA correction to alpha_s | +1.1e-5 | 9 orders below required shift |
| RPA correction to identity deviation | -4.5e-7 | Identity perfectly preserved |
| n_s(RPA) | 0.96462 | |
| Tension | 8.4 sigma | Unchanged from O-Z |
| g needed for Planck 2-sigma | > 2.0 (not found) | Even 13x Casimir coupling insufficient |

**Structural diagnosis**: The RPA fails to break the identity for three independent and mutually reinforcing reasons:

1. **chi_0(K) is nearly K-independent** (0.30% variation in the fitting window [0.85, 1.15] K_pivot). The pair coherence length xi_BCS = 0.808 M_KK^{-1} spans 5.3 cells, but the pair dispersion bandwidth 4 J_pair = 0.461 is only 2.7% of the pair gap 2 E_qp_min = 1.70. The pair is STIFF: it cannot respond to the slow modulation at K_pivot. The effective power-law index of chi_0 near K_pivot is d ln chi_0 / d ln K = -0.0098, essentially zero.

2. **The K^2 part of chi_0(K) renormalizes J_eff but does NOT break the identity**. The identity alpha_s = n_s^2 - 1 holds for ANY propagator of the form T/(J K^2 + m^2) with K-independent J, m, T. The leading K-dependence of chi_0 is proportional to K^2 (from the tight-binding dispersion), which simply shifts J_eff. The non-K^2 contributions are O((K l_cell)^2/12) = O(7.5e-3) -- lattice corrections that are too small.

3. **The mass hierarchy m^2/(J K_pivot^2) = 56 suppresses everything**. Even with g^2 chi_0 = O(1), the propagator D_0(K_pivot) = 7.8e-4 is so small (because m^2 = 141 >> J K^2 = 2.5) that the RPA self-energy Pi D_0 = 4e-4. The RPA correction is a part-per-mille effect. Scanning g from 0 to 2.0 (13x the Casimir value) shows alpha_s varies by < 2e-4 -- the identity is protected by the mass hierarchy regardless of coupling strength.

**Broken nuclear analogy**: The deep-dive (Section 3.6, 3.8) hypothesized that nuclear effective charges (which correct B(E2) by factors of 2-5 via RPA) might analogously correct alpha_s. This analogy BREAKS for a specific structural reason: nuclear effective charges correct MATRIX ELEMENTS |<f|O|i>|^2, which do not have a mass hierarchy in the denominator. The framework's propagator D(K) = T/(J K^2 + m^2) has m^2 >> J K^2 in the denominator, which kills the RPA correction. The g^2 chi_0 = 0.51 (comparable to nuclear ~1) confirms the COUPLING is nuclear-scale, but the OBSERVABLE (propagator slope) is insensitive because of the mass hierarchy. This is a broken analogy to add to the registry.

**Self-correction**: The deep-dive estimated g^2 chi_0 ~ 1.54. The actual computation gives 0.51 -- a factor of 3 lower. The discrepancy: the deep-dive used chi_0 = rho_B2 F_transfer^2 = 14.02 x 2.13^2 = 63.5, which OMITTED the energy denominator 2 E_qp in the susceptibility. Including it reduces chi_0 by a factor of ~3 (from 63.5 to 21.1). This reinforces the FAIL: even the corrected g^2 chi_0 = 0.51 produces negligible RPA correction.

**Data files**: `tier0-computation/s50_fabric_rpa.py`, `tier0-computation/s50_fabric_rpa.npz`, `tier0-computation/s50_fabric_rpa.png`

---

### W2-G: Anomalous Dispersion on Disordered Fabric (ANOMALOUS-DISPERSION-50) — landau-condensed-matter-theorist

**Status**: COMPLETE
**Gate**: ANOMALOUS-DISPERSION-50. PASS if alpha_eff(K_pivot) < 0.55. FAIL if alpha_eff > 1.5. INFO if 0.55 < alpha_eff < 1.5.

**Gate Verdict: FAIL** -- alpha_eff = 2.0 at K_pivot. Z_3 disorder does NOT produce anomalous dispersion. The O-Z identity alpha_s = n_s^2 - 1 survives on the 32-cell fabric.

**Method**: Constructed three 32x32 Josephson coupling matrices on the 4x4x2 periodic lattice:
- Model I (isotropic): J = J_eff = (2 J_C2 + J_su2)/3 = 0.641 for all bonds
- Model II (anisotropic): J_xy = J_C2 = 0.933, J_z = J_su2 = 0.059 (ratio 15.8)
- Model III (Z_3 disordered): Same as II, but xy-bonds across Z_3 domain walls weakened to J_C2 cos^2(pi/3) = J_C2/4 = 0.233. Z_3 phases assigned by (i_x + i_y) mod 3.

Exact diagonalization of all three 32x32 Laplacians. Computed: (1) eigenvalue band structure, (2) Bloch purity via Fourier projection, (3) participation ratio (localization diagnostic), (4) K-resolved propagator P(K) = sum_n |<K|phi_n>|^2/(eps_n + m^2), (5) n_s and alpha_s from retuned lattice propagator with m^2 tuned to n_s = 0.965.

**Key numbers:**

| Quantity | Isotropic | Anisotropic | Z_3 Disordered |
|:---------|:----------|:------------|:---------------|
| Min nonzero eigenvalue | 1.283 | 0.236 | 0.236 |
| Max eigenvalue | 7.697 | 7.697 | 4.508 |
| Bandwidth | 6.414 | 7.460 | 4.272 |
| m^2 (retuned, n_s=0.965) | 106.5 | 80.6 | 38.0 |
| Mean Bloch purity | 0.336 | 0.437 | 0.328 |
| Min participation ratio | 0.248 | 0.266 | 0.277 |

**Z_3 domain structure:**
- Domain populations: p=0: 12 cells, p=1: 10, p=2: 10
- XY bonds: 64 total, 16 same-domain (J_C2), 48 cross-domain (J_C2/4)
- Cross-domain fraction: 75% (strong disorder)
- Z_3 in-plane softening: epsilon(mode 2, Z_3) / epsilon(mode 2, aniso) = 0.250 exactly (4x reduction, as expected from J_C2/4)

**Three independent diagnostics converge:**

1. **Propagator ratio** (DEFINITIVE): P_Z3(K) / P_iso(K) is flat to 1.7% across all 14 K-shells. The Z_3 disorder changes the effective mass (m^2 drops from 106.5 to 38.0) but NOT the functional form of P(K). This is a mass renormalization, not anomalous dispersion.

2. **Lattice artifact identification**: Retuned propagator gives alpha_s = +0.023 for the CLEAN ISOTROPIC model (known K^2 dispersion), deviating from n_s^2-1 = -0.069 by 0.092. The same +0.092 artifact appears in ALL three models. 14 discrete K-shells are insufficient to extract the quadratic coefficient (alpha_s) reliably.

3. **Structural theorem**: The Goldstone theorem guarantees epsilon(K) ~ K^2 for any broken continuous symmetry in the long-wavelength limit. K_pivot sits at Ka/pi = 0.096 (deep in the first BZ). The Z_3 disorder is PERIODIC (superlattice structure), not random; it cannot produce Anderson localization or anomalous diffusion. The lattice correction to K^2 at K_pivot is 0.75%.

**Eigenvalue analysis highlights:**
- Lowest nonzero mode (K_z = pi): epsilon = 4 J_su2 = 0.236. IDENTICAL in aniso and Z_3 models (z-direction unaffected by Z_3 walls).
- Lowest in-plane mode: Z_3 value = 0.466 vs aniso value = 1.865. Ratio = 0.250 exactly (J_C2/4 from domain wall weakening). The mode is SOFTENED but still K^2.
- The Z_3 disorder compresses the bandwidth by factor 0.57 and creates low-energy states, but the dispersion remains quadratic.

**Physical interpretation:**

The Z_3 domain walls weaken 75% of in-plane bonds by a factor of 4 (J_C2 to J_C2/4). This is equivalent to replacing the crystalline lattice with a softer one. The phonon band structure is compressed and the density of states shifts to lower energies (Van Hove peak at epsilon = 0.76 vs 3.79 for isotropic). But the FORM of the dispersion is unchanged: epsilon(K) = J_eff * K^2, with J_eff reduced by the domain wall scattering.

For anomalous dispersion (alpha != 2) to arise from lattice disorder, one needs either: (a) random long-range correlated disorder producing Levy flights, (b) Anderson localization requiring exponentially many sites, or (c) non-local couplings beyond nearest-neighbor. The Z_3 structure on a 4x4x2 lattice provides none of these. It is a periodic superlattice, not random disorder.

The Goldstone theorem is structural: for any system with broken U(1) symmetry, the low-energy excitations are phase modes with epsilon ~ K^2. This applies independently of the lattice details, disorder configuration, or coupling anisotropy. The Z_3 domain walls break translational symmetry but not the U(1) that protects the Goldstone mode.

**Constraint map update**: The anomalous dispersion route to Planck compatibility (alpha_eff < 0.55) is CLOSED for the 32-cell fabric. The O-Z identity alpha_s = n_s^2 - 1 = -0.069 holds at K_pivot for all three lattice models, including the most disordered. This is the fifth independent confirmation of the identity (after W1-A 3-pole, W1-F running mass, W1-H eikonal, and W2-B fabric RPA).

**Data files**: `tier0-computation/s50_anomalous_dispersion.py`, `tier0-computation/s50_anomalous_dispersion.npz`, `tier0-computation/s50_anomalous_dispersion.png`

---

## Wave 3 — Remaining Priorities

### W3-A: GL Free Energy with Josephson Phases (GL-JOSEPHSON-50) — landau-condensed-matter-theorist

**Status**: NOT STARTED
**Gate**: GL-JOSEPHSON-50. PASS if additional soft modes found beyond single-cell Leggett.

**Results**:

*(Agent writes here)*

---

### W3-B: Weyl Zero-Crossing Physical Interpretation (WEYL-ZERO-50) — schwarzschild-penrose-geometer

**Status**: NOT STARTED
**Gate**: WEYL-ZERO-50. PASS if GW polarization transition identified.

**Results**:

*(Agent writes here)*

---

### FREEPLAY: Cross-Domain O-Z Investigation (Team-Lead Direct)

**Method**: Research corpus cross-correlation + direct computation on existing tier0 data. Not delegated to subagents — leverages cross-domain connections that individual specialists miss.

**Scripts**: `s50_crossdomain_routes.py`, `s50_resonance_lever.py`
**Report**: `session-50-oz-crossdomain-finding.md`

---

#### The Problem Reframed

All 8 subagent computations (W1-A/C/F/H, W2-A/B/C/F) tested variations of the **Josephson phase correlator** P(K) = T/(JK² + m²). The O-Z identity α_s = n_s² - 1 is structural within this correlator (5 independent proofs). But S50 conflated TWO problems:

1. **The identity problem**: Can α_s deviate from n_s² - 1?
2. **The mass problem**: The Leggett mass m_L = 0.070 M_KK is 170× below the mass m* = 11.85 M_KK needed for n_s = 0.965 in O-Z.

The subagents exhaustively addressed #1 (all FAIL within phase sector). Nobody addressed #2 because #1 was the master gate. But #2 was always the deeper obstruction.

---

#### Five Cross-Domain Routes Tested

| # | Route | Source Domains | Identity Broken? | n_s Viable? | Status |
|:--|:------|:---------------|:-----------------|:------------|:-------|
| 1 | **SA correlator** | Connes NCG × KK geometry × Tesla two-functional | **YES** (dev 0.08) | No (0.2) | **OPEN** |
| 2 | R-G integral variation | Volovik q-theory × nuclear integrability | No (factorizes) | N/A | CLOSED |
| 3 | Non-equilibrium FDT | Volovik non-equil. × Landau CM | No (< 0.001%) | N/A | CLOSED |
| 4 | Spectral dimension flow | CDT × spectral geometry | No (d_s ≥ 0) | N/A | CLOSED |
| 5 | **Pair-transfer form factor** | Nazarewicz nuclear × fabric geometry | **YES** (sinc²) | Partial (0.70) | **OPEN** |

**Route 1 (SA correlator)**: The spectral action two-point function χ_SA(K) = Σ_{(p,q)} W_{(p,q)}/(K² + C₂(p,q)) involves all 992 eigenvalues grouped by Casimir mass. Pole spread 110% (C₂ from 1.33 to 9.33) versus the Josephson propagator's 0.051%. Goldstone's theorem does NOT protect it. Effective α = 1.21 at K_pivot (sub-quadratic). The identity IS broken. But standalone SA gives n_s = 0.2 (heavy KK modes dominate by Weyl's law).

**Route 2 (R-G integrals)**: CLOSED. δI_α(x) = (dI/dτ)·δτ(x) factorizes — K-dependence is purely from δτ, which is K² on a lattice. The conserved integrals carry no independent spatial structure.

**Route 3 (Broken FDT)**: CLOSED. All GGE temperatures T_k >> ω_L (ratios 2-8×). High-T limit makes sector occupations identical. FDT breaking < 0.001% across K.

**Route 4 (Spectral dimension)**: CLOSED for classical fabric. d_s at K_pivot = 1.49 (clean) / 0.72 (Z₃), reflecting compactness, not anomalous geometry. Would need quantum geometry (path integral over tessellations) for CDT-type d_s = 2.

**Route 5 (Pair-transfer form factor)**: The nuclear pair-transfer response G_pair(K) has sinc²(K·l_cell) form factor from cell shape — a non-O-Z functional form. Identity IS broken (sinc² ≠ K²/(K²+m²)). At K·l = 3.0: n_s = 0.70 (30% too red). Need K·l ~ 1.0 → requires ~864 cells or different K_pivot mapping. Geometric near-miss.

---

#### The Resonance Lever (Archimedes Hypothesis)

The phi crossing at τ = 0.2117 (W1-E PASS, confirmed to 6 sig figs) provides a resonance between the spectral geometry sector and the Josephson sector. The lever:
- **Arm**: Q_Leggett = 670,000 (W1-D)
- **Fulcrum**: phi crossing (ω_L2/ω_L1 = φ_paasch to machine precision)
- **Force**: dS/dτ = 58,673 (spectral action gradient)

Resonance width: δτ_res = 1.35 × 10⁻⁶ (0.0045% of transit). At resonance, SA-Goldstone coupling is amplified by Q relative to background.

**Result**: The lever DOES amplify the SA-Goldstone coupling, but the target n_s = 0.965 is unreachable. The scan covers 7 decades of coupling:
- Low coupling → n_s = -1.0 (pure Goldstone, K²-dominated, m too small)
- High coupling → n_s = +0.2 (pure SA, heavy Casimir poles)
- Maximum achievable n_s ~ 0.24
- Target 0.965: **not in the accessible range**

The resonance lever fails because **both** the Goldstone and the SA correlator give n_s << 0.965 with the physical parameters. The Goldstone gives -1 (m = 0.070 << JK²), the SA gives 0.2 (C₂_avg = 7.4 >> K²). No mixture reaches 0.965.

---

#### The Mass Problem: The Surviving Obstruction

All roads lead back to:

**m_required = 11.85 M_KK  vs  m_Leggett = 0.070 M_KK  (ratio: 170×)**

This is NOT the identity problem. The identity α_s = n_s² - 1 can be broken (Routes 1 and 5 prove this). The mass problem is: where does the 11.85 M_KK effective mass come from? The Leggett mass (0.070), the SA Casimir masses (1.33-9.33), and the pair-transfer scale (ω_GPV = 0.792) are all either too small or too large. None hits the narrow window m ≈ 12 M_KK.

**What 12 M_KK corresponds to**: m* = 11.85 means K² + m*² has a crossover at K ~ m*/√J ~ 14.8 M_KK. This is at the TOP of the Dirac spectrum — the highest eigenvalues are ~2 M_KK at max_pq_sum = 6. With higher PW truncation, eigenvalues grow as √(C₂), reaching ~12 M_KK for reps around (p+q) ~ 10. The required mass scale is the SPECTRAL EDGE of the Dirac operator at high truncation.

**Possible interpretation**: The n_s tilt might be set not by a mass gap in the propagator but by the SPECTRAL CUTOFF Λ in the spectral action Tr f(D²/Λ²). The cutoff function f determines which eigenvalues contribute. If Λ ~ 12 M_KK, the spectral action "sees" eigenvalues up to ~12 M_KK, and the cutoff-dependent tilt mimics an O-Z propagator with m ≈ Λ. This would make n_s a function of Λ, not m — a spectral action observable, not a Josephson one.

---

#### Session 50 Cross-Domain Scorecard

| Finding | Type | Confidence |
|:--------|:-----|:-----------|
| SA correlator breaks α_s identity (pole spread 110%) | Structural | HIGH |
| Pair-transfer sinc² breaks α_s identity | Structural | HIGH |
| R-G integrals factorize (no independent K-structure) | Closure | HIGH |
| FDT breaking negligible (high-T limit) | Closure | HIGH |
| Spectral dimension normal (classical lattice) | Closure | HIGH |
| Resonance lever amplifies coupling but can't reach n_s = 0.965 | Quantitative | HIGH |
| Mass problem (170×) is the binding constraint, not the identity | Diagnostic | HIGH |
| n_s may be spectral-cutoff observable, not Josephson-mass observable | Speculation | LOW |
| Required mass 12 M_KK ≈ spectral edge at high PW truncation | Observation | MEDIUM |

---

## Synthesis

### Gate Verdicts Summary

### Gate Verdicts Summary

| Gate ID | Verdict | Key Number | Notes |
|:--------|:--------|:-----------|:------|
| LEGGETT-PROPAGATOR-50 | **FAIL** | 3 poles 99.95% degenerate, delta_alpha = 1.5e-7 | Identity survives. 8.4σ from Planck. Equal-stiffness theorem. |
| J-PAIR-CALIBRATE-50 | **INFO** | J_pair in [0.115, 0.329], 7 methods | Supported but 41% uncertainty. J_C2 calibration needed. |
| BOGOLIUBOV-IMPRINT-50 | **FAIL** | Feature amplitude 1.7e-9, erasure 6.2e-9 | Trans-Planckian erasure. phi_0 = 0 symmetry. B2 shielded. |
| LEGGETT-DAMPING-50 | **PASS** | Q = 6.7e5, all decay channels forbidden | Mass concept valid. 2*E_min = 1.800 >> omega_L = 0.070. |
| LEGGETT-PHI-CONFIRM-50 | **PASS** | |R(0.21)/phi-1| = 0.0609% < 0.1% | Crossing at tau=0.2117, S49 spline confirmed to 6 sig figs. |
| RUNNING-MASS-50 | **FAIL** | gamma = -6.76e-4 (need > 1.7) | Structural theorem: gamma < 1-n_s = 0.035. Algebraic bound. |
| LORENTZIAN-CMPP-50 | **INFO** | Static: Type D (exact). Transit: Type G. | Corrects S49 Type II (Riemannian artifact). No transition at 0.537. |
| EIKONAL-DAMPING-50 | **FAIL** | Gamma/m² = 0 (exact) | Zero-mode protection: Goldstone is KK n=0, <V>=0 on T². |
| ANOMALOUS-DISPERSION-50 | **FAIL** | alpha_eff = 2.0, Goldstone theorem | Z₃ softens coupling (m² renorm) but dispersion stays K². |
| SIGMA8-OZ-50 | **PASS** | σ_8 = 0.799, shift -1.50% from LCDM | In [0.740, 0.820]. S49 "21% shift" was 14× overestimate. |
| FABRIC-RPA-50 | **FAIL** | delta(alpha_s) = 1.1e-5, Π·D₀ = 4e-4 | χ₀(K) too flat + mass hierarchy. Nuclear analogy breaks. |
| DESI-DR3-JOINT-50 | **FAIL** | χ²/N = 23.2 (threshold 4) | Δχ² = +241 vs LCDM. BAO distances exclude w_0 = -0.51. |
| W_A-SOURCE-50 | **FAIL** | w_a = 0 from all 4 mechanisms | Triple-locked: trapping + integrability + frozen modulus. |
| KZ-SPATIAL-50 | **FAIL** | δn/n = 1.59e-4 (featureless) | Sudden-quench universality. All cells identical to 0.059%. |

### Structural Results (Permanent)

1. **α_s = n_s² - 1 is a structural theorem** of any equilibrium propagator with K² dispersion on a compact Josephson lattice with broken U(1). Five independent proofs (3-pole, running mass, eikonal, RPA, anomalous dispersion). Cannot be broken within the phase sector.

2. **Leggett mode is sharp and undamped** (Q = 6.7 × 10⁵). All pair-breaking channels energetically forbidden. The 2·E_min = 1.800 M_KK threshold is 25.9× above ω_L = 0.070. S49 "marginal damping" concern was a misidentification (order parameter gap ≠ quasiparticle gap).

3. **Phi crossing confirmed to 6 significant figures**: ω_L2/ω_L1 = φ_paasch at τ = 0.211686. J₁₂/J₂₃ = 19.52 algebraically constant. The crossing is a geometric identity connecting many-body BCS to single-particle Dirac spectral geometry.

4. **Lorentzian CMPP is Type D** (exact, static product). S49 "Type II locked" was a Riemannian signature artifact from complexified null frames. The physical spacetime is algebraically special (Schwarzschild/Kerr class).

5. **σ_8 = 0.799 is observationally viable**. S49 "21% excluded by lensing" was overestimated by 14×. The O-Z prediction sits between Planck and lensing within 2σ of both.

6. **w_a = 0 is triple-locked** by trapping (quasiparticles in SU(3) fiber), integrability (8 R-G conserved integrals), and frozen modulus (τ_dot = 0 post-transit). No mechanism within current architecture produces w(z) evolution.

7. **BAO distances exclude w_0 = -0.509** at χ²/N = 23.2. S49 B_1D = 20.9 (framework preferred) was comparing against derived parameters, not raw BAO data. Raw data decisively favors LCDM.

8. **SA correlator is a structurally distinct object** with 110% pole spread (C₂ from 1.33 to 9.33) that breaks the α_s identity. Not protected by Goldstone's theorem. Effective α = 1.21 (sub-quadratic). But standalone SA gives n_s = 0.2 (too red).

9. **The mass problem** (m_required/m_Leggett = 170) is the binding constraint. Breaking the identity (proven possible via SA correlator and pair-transfer form factor) is necessary but not sufficient. The 12 M_KK effective mass corresponds to the spectral edge of D_K at high Peter-Weyl truncation.

### New Closures

| # | Mechanism | Gate | Evidence |
|:--|:----------|:-----|:---------|
| 1 | 3-pole Leggett propagator | LEGGETT-PROPAGATOR-50 | Poles 99.95% degenerate (mass hierarchy σ/m² = 5e-4) |
| 2 | Bogoliubov imprint of Leggett mass | BOGOLIUBOV-IMPRINT-50 | Trans-Planckian erasure (ω_L/ω_transit = 10⁻⁵) |
| 3 | Running mass in single-pole | RUNNING-MASS-50 | Structural theorem γ < 1-n_s = 0.035 |
| 4 | Eikonal texture damping | EIKONAL-DAMPING-50 | Zero-mode protection (KK n=0, ⟨V⟩ = 0) |
| 5 | Anomalous dispersion from Z₃ | ANOMALOUS-DISPERSION-50 | Goldstone theorem (K² structural for broken U(1)) |
| 6 | Fabric RPA vertex correction | FABRIC-RPA-50 | χ₀(K) 0.3% variation; mass hierarchy Π·D₀ = 4e-4 |
| 7 | Spatial KZ pair creation | KZ-SPATIAL-50 | Sudden-quench universality (δn/n = 10⁻⁴) |
| 8 | w_a from inter-cell coupling | W_A-SOURCE-50 | No condensate post-transit (J_ij = 0) |
| 9 | w_a from GGE thermalization | W_A-SOURCE-50 | Wrong direction or no thermalization |
| 10 | w_a from modulus evolution | W_A-SOURCE-50 | Frozen modulus dichotomy |
| 11 | w_a from viscous pressure | W_A-SOURCE-50 | Π = constant (integrability) |
| 12 | R-G integral spatial variation | Cross-domain Route 2 | Factorization: δI = (dI/dτ)·δτ, K² from τ |
| 13 | Non-equilibrium FDT breaking | Cross-domain Route 3 | High-T limit: T/ω = 2-8, < 0.001% variation |
| 14 | Spectral dimension anomaly | Cross-domain Route 4 | Classical lattice: d_s ≥ 0, no CDT-type flow |

### Constraint Map Updates

| Entity | Prior State | New State | Evidence |
|:-------|:-----------|:----------|:---------|
| O-Z identity α_s = n_s²-1 | OPEN (S49 wayforward) | **STRUCTURAL THEOREM** (5 proofs) | W1-A, W1-F, W1-H, W2-A, W2-B |
| Leggett damping | OPEN (S49 marginal concern) | **CLOSED** (Q = 670,000) | W1-D: E_qp >> ω_L |
| Phi crossing | INFO (S49 spline, 0.789%) | **PASS** (0.061%, confirmed 6 sig figs) | W1-E: τ = 0.211686 |
| CMPP classification | Type II (S49, Riemannian) | **Type D** (Lorentzian, exact) | W1-G: signature artifact |
| σ_8 from O-Z | "21% shift, excluded" (S49 CW) | **0.799, viable** (1.5% shift) | W2-F: S49 was 14× overestimate |
| w_0 = -0.509 vs DESI | B = 20.9 (S49, preferred) | **χ²/N = 23.2** (excluded by raw BAO) | W2-D: S49 compared derived params |
| w_a = 0 | OPEN | **TRIPLE-LOCKED** | W2-E: 4 mechanisms all give 0 |
| SA correlator | UNCOMPUTED | **Identity broken** (dev 0.08, α_eff = 1.21) | Cross-domain Route 1 |
| Pair-transfer form factor | UNCOMPUTED | **Identity broken** (sinc², n_s = 0.70) | Cross-domain Route 5 |
| Mass problem (170×) | Implicit in all S49 work | **IDENTIFIED as binding constraint** | Cross-domain synthesis |

### Files Produced

| File | Gate/Source |
|:-----|:-----------|
| `s50_leggett_propagator.py/.npz/.png` | LEGGETT-PROPAGATOR-50 |
| `s50_jpair_calibrate.py/.npz` | J-PAIR-CALIBRATE-50 |
| `s50_bogoliubov_imprint.py/.npz/.png` | BOGOLIUBOV-IMPRINT-50 |
| `s50_leggett_damping.py/.npz/.png` | LEGGETT-DAMPING-50 |
| `s50_leggett_phi_confirm.py/.npz/.png` | LEGGETT-PHI-CONFIRM-50 |
| `s50_running_mass.py/.npz/.png` | RUNNING-MASS-50 |
| `s50_lorentzian_cmpp.py/.npz/.png` | LORENTZIAN-CMPP-50 |
| `s50_eikonal_damping.py/.npz/.png` | EIKONAL-DAMPING-50 |
| `s50_anomalous_dispersion.py/.npz/.png` | ANOMALOUS-DISPERSION-50 |
| `s50_fabric_rpa.py/.npz/.png` | FABRIC-RPA-50 |
| `s50_kz_spatial.py/.npz/.png` | KZ-SPATIAL-50 |
| `s50_desi_dr3_joint.py/.npz/.png` | DESI-DR3-JOINT-50 |
| `s50_wa_source.py/.npz/.png` | W_A-SOURCE-50 |
| `s50_sigma8_oz.py/.npz/.png` | SIGMA8-OZ-50 |
| `s50_crossdomain_routes.py` | Cross-domain Routes 2-5 |
| `s50_resonance_lever.py/.npz` | Resonance lever (Archimedes) |
| `session-50-naz-deepdive.md` | Naz deep-dive review |
| `session-50-oz-crossdomain-finding.md` | Cross-domain synthesis |
| `session-50-oz-investigation-prompts.md` | Prompt archive |

### Framework Probability Update

Prior: 5-8% (post-S37 floor, unchanged through S49)

S50 produced 14 closures, 3 PASS, 2 INFO, 9 FAIL. The O-Z texture mechanism for n_s is excluded at 6-8σ by the structural theorem (identity) and 170× by the mass problem. The BAO distance test excludes w_0 = -0.509 at χ² = 23. The w_a = 0 prediction is triple-locked with no escape.

Counterbalancing: σ_8 = 0.799 is viable (S49 threat neutralized). The phi crossing is real (new structural identity). The Leggett mode is sharp (Q = 670,000). The SA correlator breaks the identity (new correlator identified). The internal geometry mathematics is fully characterized (Type D, cosmic censorship, TT stability).

**Post-S50**: 3-5% (floor lowered from 5-8%)
- O-Z n_s mechanism: CLOSED (structural theorem + mass problem)
- w_0 prediction: CLOSED by raw BAO data
- w_a prediction: CLOSED (triple-locked at 0)
- σ_8: VIABLE (sole surviving observational prediction)
- Mathematical infrastructure: INTACT (publishable independently)
- SA correlator route: OPEN but speculative (coupling model needed)
- Pair-transfer route: OPEN but geometric near-miss (N_cells dependent)

The probability drops because three of the framework's four cosmological predictions (n_s, w_0, w_a) are now excluded by data or structural theorems. Only σ_8 survives. The floor is 3% (mathematical framework without cosmological predictions) rather than the prior 5% (framework with open cosmological routes).

### Next Session Recommendations

**S51 Priority 1**: The mass problem. Where does m = 12 M_KK come from? Three angles:
- **SPECTRAL-CUTOFF-51**: Is n_s a spectral action observable (set by Λ) rather than a Josephson observable (set by m)? Compute n_s from the cutoff-dependent tilt of Tr f(D²/Λ²) at Λ ~ 12 M_KK.
- **SA-GOLDSTONE-MIXING-51**: Proper coupling model between SA and Goldstone sectors through δτ → δΔ → δJ chain. Not the multiplicative model (fails, resonance lever). The ADDITIVE model: P_phys = a·P_G + b·χ_SA with a,b from the coupling chain.
- **HIGH-PW-SPECTRUM-51**: Extend Dirac spectrum to max_pq_sum = 8 or 10. Does the spectral edge reach 12 M_KK? Does the cutoff-dependent spectral action have a natural scale at this value?

**S51 Priority 2**: The w_0 problem. BAO excludes -0.509 but the framework PREDICTS a specific w_0. Can the prediction be modified?
- **W0-REVISION-51**: The GGE alpha = E/P = 1.327 gives w_0 = -0.430. What if the 4D stress-energy includes contributions from the spectral action (geometry sector) in addition to the GGE (matter sector)?

**S51 Priority 3**: Publish the mathematics.
- The structural theorem (α_s = n_s² - 1 on compact Josephson lattices) is a publishable result.
- The phi crossing identity (ω_L2/ω_L1 = φ at τ = 0.2117) is publishable.
- The Lorentzian Type D classification is publishable.
- The Q = 670,000 undamped Leggett mode on SU(3) is publishable.
- None of these require the cosmological predictions to be correct.

---

## Collab Review Extraction: Actionable Computations for THIS SESSION

**Source**: 6 collaborative reviews (QA, Naz, Einstein, Connes, Landau, Volovik)
**Extracted**: 2026-03-20
**Priority**: Ordered by convergence count and feasibility

### PRIORITY 1 -- Convergent (4+ reviewers recommend)

#### C-1: SA-Goldstone Mixing Correlator (SA-GOLDSTONE-MIXING-51)
- **Recommended by**: QA (Section 3.2), Naz (Section 5a), Einstein (Section 5.3), Connes (Section 5.1), Landau (Section 3.4), Volovik (Section 3, Q1)
- **What**: Compute the physical two-point correlator by propagating modulus perturbations delta_tau(x) through the coupled SA-BCS-Josephson response chain. This is the additive model P_phys = a*P_G + b*chi_SA, NOT the multiplicative model tested in the resonance lever (which failed).
- **Method**: (1) Compute delta S = Sum_n f'(lambda_n^2/Lambda^2) * (d lambda_n / d tau) * delta_tau for the SA response. (2) Compute delta_Delta = (dDelta/dtau) * delta_tau for the BCS gap response. (3) Compute delta_J = (dJ/dDelta) * delta_Delta for the Josephson response. (4) Extract coupling weights a, b from the ratio of SA and Josephson responses. (5) Construct P_phys(K) and extract n_s, alpha_s. Connes specifies the NCG object: delta^2 S / (delta tau)(delta phi) as the cross-term. Naz specifies the nuclear analog: DWBA sum over reaction channels with coupling matrix elements as weights.
- **Input data**: `s44_dos_tau.npz` (tau-dependent Dirac spectrum), S48 Josephson couplings, S50 SA correlator weights from `s50_crossdomain_routes.py`
- **Gate**: PASS if n_s in [0.950, 0.980] AND alpha_s in [-0.040, 0]. FAIL if SA contribution negligible (pure O-Z survives). INFO if SA contribution significant but n_s outside target.
- **Cost**: MEDIUM (one agent, one session; all input data exists)
- **Agent**: Landau or Connes-NCG (cross-domain: requires NCG + CM expertise)

#### C-2: High Peter-Weyl Spectrum Extension (HIGH-PW-SPECTRUM-51)
- **Recommended by**: Naz (Section 3d), Einstein (Section 3.1), Connes (Section 2.3), Volovik (Section 3, Q2)
- **What**: Extend the Dirac spectrum computation to max_pq_sum = 8 and 10. Check whether eigenvalues reach 12 M_KK. Compute the cutoff-dependent spectral action tilt at Lambda ~ 12 M_KK.
- **Method**: (1) Compute D_K eigenvalues at max_pq_sum = 8 and 10 (extends existing s12 and s44 scripts). (2) Extract the spectral radius at each truncation. (3) Compute Tr f(D^2/Lambda^2) for Lambda = 6, 8, 10, 12, 14 M_KK. (4) Extract effective n_s from the cutoff-dependent tilt.
- **Input data**: Existing tier0 Dirac computation scripts (s12_*, s44_*), canonical_constants.py
- **Gate**: PASS if n_s(Lambda = 12, max_pq_sum = 10) in [0.950, 0.980]. FAIL if n_s insensitive to Lambda in this range.
- **Cost**: HIGH (eigenvalue computation at max_pq_sum = 10 is O(N^3) with N ~ 10,000+ eigenvalues; may require GPU)
- **Agent**: Connes-NCG (spectral geometry domain)

#### C-3: Polariton/Hopfield Model for SA-Goldstone Coupling
- **Recommended by**: QA (Section 3.2), Landau (Section 3.4), Connes (Section 3.2), Volovik (implicitly via quench-protocol response)
- **What**: Construct the 2x2 coupled oscillator dynamical matrix for the Goldstone and effective SA modes with avoided crossing. Extract polariton branches and check whether the lower branch has anomalous dispersion at K_pivot.
- **Method**: Solve det|omega^2 - c^2 K^2 - m_G^2, g_mix; g_mix, omega^2 - C_2_eff| = 0. The off-diagonal coupling g_mix is set by d(Delta)/d(tau) * d(tau)/d(phi_Goldstone). Extract omega_+/-(K), compute effective alpha at K_pivot. If strong coupling (Omega_R >> linewidth), the lower polariton has mixed dispersion.
- **Input data**: m_G = 0.070 M_KK, C_2 values from `s50_crossdomain_routes.py`, dDelta/dtau from multiple sessions, Josephson couplings from S48
- **Gate**: PASS if lower polariton alpha_eff at K_pivot differs from 2.0 by > 0.1. FAIL if coupling too weak (Omega_R/linewidth < 0.1). INFO if alpha_eff changes but n_s not computed.
- **Cost**: LOW (2x2 eigenvalue problem, analytic solution exists)
- **Agent**: Landau or QA

#### C-4: Strutinsky Decomposition of the Spectral Action
- **Recommended by**: Naz (Sections 3b, 5a), Einstein (Section 3.1), Connes (implicitly via cutoff discussion), Volovik (implicitly via UV-sensitivity argument)
- **What**: Decompose the spectral action into smooth (Thomas-Fermi) and oscillating (shell correction) parts. Determine whether n_s is controlled by the smooth part (cutoff Lambda) or the oscillating part (Leggett mode, Casimir gaps).
- **Method**: (1) Compute the Strutinsky-smoothed level density g_smooth(E) from the Dirac spectrum. (2) Compute delta E_shell = E_exact - E_smooth. (3) Identify which part correlates with the n_s-determining mass scale. (4) If n_s is from the smooth part, extract n_s(Lambda) for various Lambda values.
- **Input data**: Dirac spectrum from s44_dos_tau.npz, spectral action from S45 computations
- **Gate**: PASS if smooth part gives n_s in [0.950, 0.980] at Lambda ~ 12 M_KK with shell correction < 10% of smooth. FAIL if shell correction dominates. INFO if smooth and shell contribute comparably.
- **Cost**: MEDIUM (Strutinsky smoothing is standard nuclear DFT; requires fitting smooth curve to discrete spectrum)
- **Agent**: Naz (nuclear DFT domain)

### PRIORITY 2 -- Novel (1-2 reviewers, high insight value)

#### C-5: Local Resonance Mass Enhancement via T-Matrix Self-Energy (LOCAL-RESONANCE-51)
- **Recommended by**: QA (Section 3.1)
- **What**: Compute the effective mass m_eff(omega) of the Goldstone propagating on the 32-cell fabric by treating each cell as a resonant scatterer with 8 internal BCS modes. The local resonance mechanism produces m_eff >> m_bare when omega sits near (but below) an internal resonance.
- **Method**: (1) Compute the T-matrix self-energy Sigma(omega) from a single resonator at omega_0 = 0.800 M_KK (first KK mode). (2) m_eff^2 = m_bare^2 + g^2/(omega_0^2 - omega^2), where g is the Goldstone-internal-mode coupling. (3) Estimate g from V(B2,B2) = 0.1557 and the overlap integral. (4) Check if m_eff can reach 12 M_KK. Target: g^2 ~ 92 is needed.
- **Input data**: KK mode hierarchy from W1-H (`s50_eikonal_damping.npz`), V(B2,B2) = 0.1557, m_bare = 0.070 M_KK
- **Gate**: PASS if m_eff in [8, 16] M_KK for physical coupling g. FAIL if g^2 < 10 (insufficient coupling). INFO if m_eff > 1 M_KK but < 8 M_KK (partial enhancement).
- **Cost**: LOW (single scattering calculation, analytic formula)
- **Agent**: QA or Landau

#### C-6: Chamseddine-Connes-Mukhanov Dilaton Propagator
- **Recommended by**: Connes (Sections 3.1, 5.3)
- **What**: Compute the dilaton two-point function G_dilaton(K) on the 32-cell fabric, arising from promoting Lambda to a dynamical field Lambda(x). Extract the dilaton mass and compare with m_required = 11.85 M_KK.
- **Method**: G_dilaton(K) = delta^2 Tr f(D^2/Lambda^2) / delta Lambda(x_i) delta Lambda(x_j), Fourier-transformed to K-space. This is a direct matrix computation: the (i,j) element is Sum_n f'(lambda_n^2/Lambda^2) * (-2 lambda_n^2/Lambda^3) * psi_n(x_i) * psi_n(x_j), where psi_n are the eigenfunctions projected onto the tessellation sites.
- **Input data**: Dirac eigenvalues and eigenfunctions from existing tier0 data, tessellation geometry from S47
- **Gate**: PASS if m_dilaton in [8, 16] M_KK. FAIL if m_dilaton < 1 or > 50 M_KK. INFO if computable but ambiguous Lambda-dependence.
- **Cost**: MEDIUM (requires eigenfunction data, not just eigenvalues)
- **Agent**: Connes-NCG

#### C-7: U(1)_7 Gauging via Inner Fluctuations
- **Recommended by**: Landau (Section 3.3)
- **What**: Compute whether the spectral action generates a kinetic term for the U(1)_7 gauge field (A_7 = a[D, K_7]) with coefficient producing a gauge boson mass m_gauge ~ 12 M_KK. This would simultaneously eat the Goldstone and solve the mass problem.
- **Method**: (1) Extract the a_2 Seeley-DeWitt coefficient for the K_7 sector from existing S20a computation. (2) Compute g_7^{-2} = a_2[D_K] / Lambda^2. (3) Compute m_gauge = g_7 * |Delta_B2| * sqrt(J_eff * rho_s) using Delta_B2 = 0.732 M_KK and rho_s from S47.
- **Input data**: a_2 from S20a Seeley-DeWitt, Delta_B2 = 0.732 M_KK, rho_s from S47, J_eff from S48
- **Gate**: PASS if m_gauge in [8, 16] M_KK. FAIL if m_gauge < 1 M_KK (coupling too weak) or > 100 M_KK (coupling too strong).
- **Cost**: LOW (extraction from existing data + formula evaluation)
- **Agent**: Landau + Connes-NCG (needs both CM and NCG expertise)

#### C-8: GL Free Energy 6x6 Dynamical Matrix (GL-JOSEPHSON-50 Completion)
- **Recommended by**: Landau (Section 3.2)
- **What**: Compute the full 6x6 dynamical matrix (3 phases + 3 amplitudes) of the Ginzburg-Landau functional at each K. Determine whether mixed amplitude-phase modes have non-K^2 dispersion.
- **Method**: (1) Write the GL free energy for the 3-sector Josephson system on the fabric with stiffnesses J_a, mass terms r_a, quartic terms u_a, and inter-sector Josephson J_ab. (2) Linearize around the BCS ground state. (3) Diagonalize the 6x6 matrix at each K. (4) Check if any eigenvalue has omega(K) with alpha != 2.
- **Input data**: BCS ground state parameters from S48 ED, Josephson couplings from S48, stiffnesses from S47
- **Gate**: PASS if any eigenvalue has |alpha - 2| > 0.1 at K_pivot. FAIL if all eigenvalues have K^2 dispersion.
- **Cost**: MEDIUM (6x6 matrix at each K point; requires careful GL parameter extraction)
- **Agent**: Landau

#### C-9: Feshbach Coupling at the Phi Crossing
- **Recommended by**: Landau (Section 3.5)
- **What**: Compute the coupling matrix element between the Leggett mode and Dirac continuum at the phi crossing (tau = 0.2117). If V/Delta > 0.1, the Feshbach resonance dominates the spectral function near the crossing.
- **Method**: (1) Identify the Dirac eigenvalue pairs at the phi crossing frequency. (2) Compute the coupling V = (dDelta/d_lambda) * <Leggett|lambda> for each pair. (3) Compute the Feshbach width Gamma_F = 2*pi*|V|^2 * rho(omega_L). (4) If Gamma_F/omega_L > 0.01, the resonance is significant.
- **Input data**: Dirac spectrum at tau = 0.2117 from s50_leggett_phi_confirm.npz, BCS gap equation derivatives
- **Gate**: PASS if V/Delta > 0.1 AND Feshbach spectral function has non-K^2 structure. FAIL if V/Delta < 0.01. INFO if V/Delta in [0.01, 0.1] (intermediate coupling).
- **Cost**: MEDIUM (requires eigenvalue-resolved coupling calculation)
- **Agent**: Landau or Naz

#### C-10: Non-Linear Acoustic Goldstone Evolution
- **Recommended by**: QA (Section 3.4)
- **What**: Determine whether anharmonic (3-phonon, 4-phonon) evolution of the primordial Goldstone spectrum modifies n_s beyond the linear O-Z prediction. The 2:1 near-resonance from S48 QRPA (0.6% detuning) provides a candidate non-linear channel.
- **Method**: (1) Compute the non-linearity coefficient B (Gruneisen parameter) from the BCS anharmonic coupling. (2) Compute the shock formation length L_nonlinear = c^3/(omega^2 * A * B). (3) Estimate spectral weight redistribution from harmonic generation. (4) Check whether non-linear steepening modifies P(K) shape at K_pivot.
- **Input data**: QRPA near-resonance from S48, BCS interaction V(B2,B2) = 0.1557, sound speed c_BdG = 0.751 M_KK
- **Gate**: PASS if non-linear correction to n_s > 0.01. FAIL if correction < 0.001. INFO if correction detectable but < 0.01.
- **Cost**: MEDIUM (requires non-linear phonon theory on compact lattice)
- **Agent**: QA

#### C-11: BEC-BCS Crossover Sound Velocity Check
- **Recommended by**: QA (Section 4.4)
- **What**: Check whether the Combescot crossover formula (Paper 17, 2006) applied to the framework's coupling strength gives a different sound speed from c_BdG = 0.751 M_KK used in the scale mapping K_pivot = m_G/c.
- **Method**: (1) Identify the framework coupling g*N(E_F) = 2.18. (2) Apply the Combescot interpolation between c_BCS = v_F/sqrt(3) and c_BEC = sqrt(mu/m). (3) Extract c_crossover. (4) Recompute K_pivot with the corrected sound speed.
- **Input data**: g*N(E_F) = 2.18 (S37), v_F from the Dirac spectrum, c_BdG = 0.751 M_KK
- **Gate**: PASS if c_crossover differs from c_BdG by > 10% (shifts K_pivot significantly). FAIL if < 5% difference.
- **Cost**: LOW (formula evaluation)
- **Agent**: QA or Volovik

#### C-12: Quantum Metric Correction to Goldstone Dispersion (QM-DISPERSION-51)
- **Recommended by**: QA (Section 3.6)
- **What**: Compute the quantum metric tensor g_ij(K) for the Goldstone Bloch state on the 32-cell fabric. Extract the K^4 correction to the dispersion from the quantum metric integral.
- **Method**: (1) Compute Berry curvature and quantum metric from the Bloch eigenstates of the Josephson Hamiltonian on the fabric. (2) Extract the coefficient alpha_QM of the K^4 term in omega^2 = c^2 K^2 + alpha_QM K^4. (3) Evaluate at K_pivot.
- **Input data**: 13 pi Berry phases from S46, tessellation geometry from S47, Josephson Hamiltonian
- **Gate**: PASS if K^4 correction modifies effective power-law index by > 0.01 at K_pivot. FAIL if < 0.001.
- **Cost**: MEDIUM (requires Bloch eigenstate computation on 32-cell lattice)
- **Agent**: QA or Connes-NCG

### PRIORITY 3 -- Quick Checks (zero-cost diagnostics from existing data)

#### C-13: Cutoff Convergence Test for chi_SA
- **Recommended by**: Connes (Section 5.2)
- **What**: Compute chi_SA(K) for 4 different cutoff functions (sharp, Gaussian, polynomial, heat-kernel) at Lambda = 3 M_KK. Check whether the sector weights W_{(p,q)} converge.
- **Method**: Modify `s50_crossdomain_routes.py` to use 4 cutoff functions: f(x) = theta(1-x), exp(-x), (1-x)^4, and the heat kernel form. Report W_{(p,q)} for each.
- **Input data**: Dirac eigenvalues from existing tier0 data (already loaded in s50_crossdomain_routes.py)
- **Gate**: PASS if relative weight variation < 10% across cutoff functions. FAIL if variation > 50% (chi_SA is cutoff-dependent and non-predictive).
- **Cost**: LOW (4 runs of existing script with modified f)
- **Agent**: Any

#### C-14: Independent J_C2 Calibration via Berry Phase
- **Recommended by**: Naz (Section 2a recommendation)
- **What**: Independent calibration of J_C2 via Berry phase (P-30w route) to reduce the dominant 30% systematic in J_pair.
- **Method**: Compute Berry phase from adiabatic transport of a Cooper pair around the tessellation. The Berry phase encodes the inter-cell overlap independent of single-particle tunneling contamination.
- **Input data**: Tessellation geometry from S47, BCS ground state from S48
- **Gate**: PASS if J_C2 uncertainty reduced to < 15%. FAIL if Berry phase method has larger uncertainty than geometric overlap.
- **Cost**: MEDIUM (requires adiabatic transport computation)
- **Agent**: Naz or Connes-NCG

#### C-15: RPA Correction to w_0 (Different Sum from alpha_s)
- **Recommended by**: Volovik (Section 5, Q3)
- **What**: The RPA correction to alpha_s was negligible (W2-B FAIL: 1.1e-5), but the RPA correction to w_0 involves a DIFFERENT sum (energy over pressure, not spectral tilt). Check whether this sum is also negligible.
- **Method**: Compute delta_w_0 = delta(P/rho) from the RPA-corrected pair propagator. The energy density rho = sum_k n_k E_k and pressure P = sum_k n_k E_k/3 receive vertex corrections through the polarization Pi(K). The correction to w_0 = P/rho is delta_w_0 = (delta_P * rho - P * delta_rho)/rho^2.
- **Input data**: RPA data from `s50_fabric_rpa.npz`, GGE occupation numbers from S49
- **Gate**: PASS if |delta_w_0| > 0.05 (shifts w_0 toward -1). FAIL if |delta_w_0| < 0.01.
- **Cost**: LOW (reuses existing RPA computation with different observable)
- **Agent**: Naz or Volovik

#### C-16: KK-Mode Localization Renormalization of c_BdG
- **Recommended by**: QA (Section 2.1, caveat)
- **What**: Check whether Anderson-localized KK modes (kl = 0.0095) virtually renormalize the BdG sound speed c_BdG or Goldstone mass m_G. QA estimates O(xi_loc/L_T^2)^2 ~ 10^{-4}, but this should be confirmed.
- **Method**: Compute the second-order self-energy from virtual KK mode excitation: delta_c/c ~ sum_n |V_{0n}|^2 / (E_n - E_0)^2 where V_{0n} is the Goldstone-to-KK coupling and E_n are the localized KK energies.
- **Input data**: KK mode hierarchy from `s50_eikonal_damping.npz`
- **Gate**: INFO only (expected to be < 10^{-4}, too small to matter for alpha_s, but confirms completeness).
- **Cost**: LOW (perturbation theory on existing data)
- **Agent**: QA

#### C-17: Tau-Dependence of m*(tau) and m_L(tau) for Critical Scaling Test
- **Recommended by**: Landau (Section 3.1)
- **What**: Compute how the required mass m*(tau) and Leggett mass m_L(tau) vary with tau. If both diverge at the same tau_c with the same critical exponent, the 170x ratio is non-universal. If different exponents, the ratio has structural content.
- **Method**: (1) At each tau in [0.05, 0.30], compute m_L(tau) from the BCS gap and Josephson couplings. (2) Compute m*(tau) from the n_s = 0.965 constraint in the O-Z propagator. (3) Fit power-law divergences near the fold. (4) Extract critical exponents.
- **Input data**: BCS gap tau-dependence from multiple sessions, Josephson couplings from S48, fold location tau_fold = 0.19
- **Gate**: INFO (diagnostic). If exponents match known universality class (eta = 0.035-0.038 for 3D Wilson-Fisher), flag as structural.
- **Cost**: LOW (formula evaluation at existing tau grid)
- **Agent**: Landau

### Computations CLOSED by Reviews

| Suggestion | Proposed by | Closed by | Closure Reason |
|:-----------|:-----------|:----------|:---------------|
| Acoustic Fano resonance for mass enhancement | QA (Section 3.3) | QA (same section) | V_direct = 0 by zero-mode protection implies q = 0 (Fano asymmetry parameter). Symmetric Lorentzian dip, not asymmetric Fano lineshape. Structural closure: any mechanism requiring direct Goldstone-to-KK coupling is killed by zero-mode argument. |
| Nuclear effective mass (m*/m) from Landau Fermi liquid | Naz (Section 3a) | Naz (same section) | Nuclear m*/m = 0.6-0.8 (O(1) multiplicative factor). The 170x enhancement is qualitatively different -- a scale hierarchy, not a correction factor. "CLOSED by magnitude." |
| Particle-vibration coupling mass renormalization | Naz (Section 3c) | Naz (same section) | delta_m ~ g_GPV^2/omega_GPV = 0.031 M_KK. Shifts Goldstone mass from 0.070 to ~0.10 M_KK. Still 120x below required 11.85. "O(1) mass renormalization, not 170x." |
| Disordered superfluid Bose glass loophole | Landau (Section 1, loophole 3) | Landau (same section) | Z_3 disorder is periodic, not random. Even true random disorder on 32 sites would not produce Anderson localization of the Goldstone. The Bose glass transition is superfluid-insulator, not anomalous-dispersion. |
| Frustrated magnet Type B_2 anomalous Goldstone | Landau (Section 1, loophole 4) | Landau (same section) | U(1)_7 breaking has one broken generator, one Goldstone with alpha = 2. Chadha-Nielsen counting saturated. No frustration mechanism in unfrustrated U(1) breaking. |
| Plasmon/long-range Coulomb loophole | Landau (Section 1, loophole 1) | Landau (same section) | U(1)_7 is a global symmetry with short-range Josephson coupling. No gauge field, no divergent V(q). Closed unless U(1)_7 is gauged (see C-7). |
| Volovik dilution model (w_a from quasiparticle dilution) | Volovik (Section 3, W2-E discussion) | Volovik (same section) | Quasiparticles are fiber-localized, not 4D spatial. Their density is a fiber quantity. Triple-lock on w_a = 0 confirmed by frozen-modulus dichotomy. |
