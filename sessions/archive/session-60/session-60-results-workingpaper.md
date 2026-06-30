# Session 60 Results Working Paper

**Date**: 2026-03-27
**Format**: Parallel single-agent computations across 8 waves (29 computations)
**Plan**: `sessions/session-plan/session-60-plan.md`
**Status**: IN PROGRESS
**Source**: S59 collab reviews (Volovik, Hawking, Nazarewicz, Baptista, Mack), Mack-Landau workshop, S59 results working paper
**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Script prefix**: `s60_`
**Constants**: `from canonical_constants import *`

---

## Agent Instructions

When recording results for your computation, include:

1. **Verdict**: PASS / FAIL / INFO with the gate ID and one-sentence justification
2. **Key numbers**: All numerical results with units, dimensional checks, and limiting-case verification
3. **Cross-checks**: Independent verification methods used (symmetry, limiting cases, dimensional analysis, comparison to prior results)
4. **Data files**: List all `.npz`, `.py`, and `.png` files produced with brief descriptions
5. **Assessment**: What region of solution space this result constrains, what survives, what is excluded, and why
6. **WINDOWS BASH BUG**: Scripts save ALL results to `.npz` and `.png`. Verify success by checking for output files, NOT by reading Bash stdout (which will be empty due to Windows bug)

---

## Wave 0: Zero-Cost Diagnostics + Unimodular Gravity

### W0-1: Trace Factor Verification in a_4 (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: A4-TRACE-60. PASS if N_factor_a4 = N_factor_a2 within 5%. FAIL if > 20% difference. INFO if 5-20% difference.

**Results**:

**Verdict: FAIL** -- The trace factor does NOT cancel between a_2 and a_4. The ratio (a_4/a_2) differs by 82.3% between total Peter-Weyl sum and singlet sector, far exceeding the 20% FAIL threshold. Particle physics predictions (Higgs mass) are sensitive to which sector set is used.

**Key Numbers** (all at tau_fold = 0.19, max(p+q) = 3 Peter-Weyl truncation, 992 eigenvalues):

| Quantity | Value | Notes |
|:---------|:------|:------|
| N_a2 = a2_total / a2_singlet | 11453.9 | Includes Peter-Weyl multiplicity d^2 and mode count |
| N_a4 = a4_total / a4_singlet | 20885.4 | Same, but omega^2-weighted |
| N_a4 / N_a2 | 1.8234 | **Deviation from 1: 82.3% (FAIL)** |
| (a4/a2)_total | 1.6301 | Mean eigenvalue of full spectrum |
| (a4/a2)_singlet | 0.8940 | Mean eigenvalue of singlet sector |
| Higgs mass shift: sqrt(N_a4/N_a2) | 1.350 | **35% shift if using total vs singlet** |
| N_a0 = a0_total / a0_singlet | 6374.0 | Pure multiplicity counting |
| N_a6 = a6_total / a6_singlet | 38577.9 | omega^3-weighted |

The hierarchy N_a0 (6374) < N_a2 (11454) < N_a4 (20885) < N_a6 (38578) is monotonically increasing because higher SU(3) representations have systematically larger Dirac eigenvalues (Casimir growth). When computing higher spectral moments, the larger eigenvalues of higher reps are amplified more, so the total/singlet ratio grows with moment order.

**Tau dependence**: The ratio N_a4/N_a2 is nearly tau-independent:
- tau=0.00: N_a4/N_a2 = 1.831
- tau=0.05: N_a4/N_a2 = 1.830
- tau=0.10: N_a4/N_a2 = 1.829
- tau=0.15: N_a4/N_a2 = 1.826
- tau=0.19: N_a4/N_a2 = 1.823

This near-constancy (spread < 0.5%) means the FAIL verdict is structural and independent of the Jensen deformation parameter.

**Cross-checks performed**:
1. a4_singlet from direct eigenvalue sum vs sector accumulation: agree to 1.78e-15 (machine epsilon)
2. a2_total, a4_total match S59 stored values exactly (0.00e+00 difference)
3. a2_total, a4_total match S58 WDW values to 1.5e-10 (machine precision)
4. Per-sector a4/a2 ratios increase monotonically with Casimir: (0,0)=0.894, (1,0)=1.132, (2,0)=1.411, (1,1)=1.369, (3,0)=1.712, (2,1)=1.642

**Physical interpretation**: The SPINOR-NORM-59 result (dividing a_2 by dim(Delta_8)=16 gives H_0=68.8) used the singlet sector as a proxy for "gravitational a_2." The analogous singlet a_4 gives (a4/a2)_singlet = 0.894. But the Chamseddine-Connes Higgs mass formula uses the FULL trace, giving (a4/a2)_total = 1.630. The ratio differs by factor 1.82. This means:

- **Gravity** (M_Pl, H_0): Uses a_2. The spinor-norm correction of dividing by 16 applies. H_0 = 68.8 km/s/Mpc is robust.
- **Higgs mass**: Uses a_4/a_2. If both are at the total level, the spinor trace cancels in the ratio BUT the ratio equals 1.630, not 0.894. If the physical Higgs formula requires the singlet-sector ratio (because only gauge-singlet contributions survive KK reduction for the Higgs potential), the Higgs mass prediction is 35% lower.
- **This distinction was invisible in S59** because S59 only examined a_2. The a_4 computation reveals that the sector-resolution matters for particle physics even though it approximately cancels for gravity.

**Constraint surface update**: The region where "trace factor cancels uniformly across all Seeley-DeWitt coefficients" is EXCLUDED. Particle physics predictions from the spectral action require careful sector decomposition, not just division by dim(Delta_8).

**Data files**:
- `computations/s60_a4_trace.py` -- computation script
- `computations/s60_a4_trace.npz` -- all numerical results
- `computations/s60_a4_trace.png` -- 4-panel diagnostic plot

---

### W0-2: Paper 14 CC Dimensional Analysis (volovik-superfluid-universe-theorist)

**Status**: COMPLETE
**Gate**: CC-DIM-ANALYSIS-60. PASS if Paper 14 cubic scaling matches exact residual within 3 OOM. FAIL if all scaling formulas disagree by > 10 OOM. INFO if one scaling matches within 3-10 OOM.

**Results**:

**Verdict: INFO** -- The Paper 14 cubic scaling (properly dimensionalized as K^3/M_Pl^2 with K = |E_cond/M_KK| * M_KK^2) matches the exact residual within 5.7 OOM, falling in the INFO band (3-10 OOM). The |E_cond|^2 * M_KK^4 formula matches at 0.39 OOM (ratio 0.41), but this is a q-theory identity, not a Paper 14 seesaw prediction. The Paper 14 seesaw mechanism is structurally inapplicable because the M_KK/M_Pl hierarchy (6.1e-3, 2.2 decades) is too shallow for the seesaw suppression to operate.

**Key Numbers**:

| Quantity | Value | Notes |
|:---------|:------|:------|
| M_KK / M_Pl | 6.08e-3 | Only 2.2 decades of hierarchy (QCD has 20 decades) |
| (M_KK/M_Pl)^2 | 3.70e-5 | The seesaw suppression factor -- negligible |
| Lambda_exact = 0.046 * M_KK^4 | 1.40e+66 GeV^4 | S59 Mack-Landau workshop exact residual |
| Lambda_obs | 2.70e-47 GeV^4 | CC gap = 112.7 orders |
| K^3/M_Pl^2 (Paper 14 analog) | 2.89e+60 GeV^4 | Ratio to exact: 2.1e-6 (5.7 OOM short) |
| Delta^6/M_Pl^2 (K=Delta^2 variant) | 7.41e+57 GeV^4 | Ratio to exact: 5.3e-9 (8.3 OOM short) |
| \|E_cond\|^2 * M_KK^4 | 5.70e+65 GeV^4 | Ratio to exact: 0.41 (0.39 OOM, q-theory identity) |
| epsilon(1) / \|E_cond\| | 0.336 | Ground state is 34% of condensation energy |

**Dimensional analysis of the three task-specified formulas**:

1. **Delta_BCS^3 / M_Pl^2**: Dimensionally WRONG ([E]^3/[E]^2 = [E], not [E]^4). Inapplicable. 56 OOM off.
2. **Delta_BCS^4 / M_Pl^2**: Dimensionally WRONG ([E]^4/[E]^2 = [E]^2, not [E]^4). 40 OOM off.
3. **(Delta_BCS * M_KK)^2 / M_Pl^2**: Dimensionally WRONG ([E]^4/[E]^2 = [E]^2, not [E]^4). 39 OOM off.

The task-specified formulas all have dimensional inconsistencies because Paper 14 uses K_QCD (dim [E^2], the QCD string tension), not a single energy scale. The correct analog maps K_QCD -> |E_cond/M_KK| * M_KK^2 (dimensionless coupling times energy^2), giving K^3/M_Pl^2 -> [E^4] correctly.

**Structural finding: epsilon(1) ~ E_cond^2 (q-theory, not seesaw)**:

The near-exact match |E_cond|^2 * M_KK^4 / Lambda_exact = 0.41 reveals that epsilon(1) ~ |E_cond|^2 / (2*chi_q) with chi_q ~ O(1). This is the q-theory relation (Paper 14 eq. 5.2b): the ground state energy goes as the SQUARE of the gap parameter divided by the vacuum compressibility. The factor 0.41 corresponds to chi_q ~ 1.2, entirely consistent with O(1) BCS compressibility.

This is NOT a Paper 14 seesaw -- it is pure microscopic physics with no reference to M_Pl. The Paper 14 seesaw introduces M_Pl via the Friedmann equation (H^2 ~ Lambda/M_Pl^2), which couples the condensate perturbation to Hubble expansion. In the framework, M_KK is so close to M_Pl that this coupling is unsuppressed.

**Cross-checks performed**:
1. QCD verification: K_QCD = (440 MeV)^2, K^3/E_Pl^2 = 4.87e-41 GeV^4 (6 OOM above Lambda_obs, consistent with Paper 14's k_Lambda ~ 10^-6 giving Lambda ~ Lambda_obs).
2. M_KK hierarchy: (M_KK/M_Pl)^2 = 3.70e-5, confirming that the seesaw factor is O(10^{-4.4}) not O(10^{-40}) as in QCD.
3. Dimensional audit: all 7 scaling variants checked for dimensional consistency. Only 4 are [E^4].
4. epsilon(1)/E_cond ratio = 0.336, confirming the ground state energy is NOT E_cond (it includes correlation energy, quantum fluctuations, and Fock space reconfiguration -- exactly the physics that Paper 14's chi_q encodes).

**Data files**:
- `computations/s60_cc_dim_analysis.py` -- computation script (7 scaling tests, QCD cross-check, diagnosis)
- `computations/s60_cc_dim_analysis.npz` -- all numerical results (30 fields)

**Assessment**: The Paper 14 K^3/E_Pl^2 formula is designed for systems with a vast hierarchy between the condensation scale and the gravitational scale (K_QCD/E_Pl ~ 10^{-20}). The framework has M_KK/M_Pl ~ 10^{-2.2}, rendering the seesaw negligible. The CC residual epsilon(1) = 0.046 is controlled by the BCS vacuum compressibility chi_q ~ O(1), not by the gravitational hierarchy. This confirms that the CC problem in the framework is an INTERNAL BCS problem (how the discrete ground state energy at N_pair = 1 relates to the O(1) condensation energy) rather than a gravitational hierarchy problem. The q-theory route (Paper 14 Section V, not Section VI) is the correct description: Lambda = epsilon(q_0) where q_0 is the equilibrium value of the conserved charge.

---

### W0-3: Unimodular Gravity from Fiber Integration (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: UNIMOD-GRAV-60. PASS if Jensen volume-preservation propagates to constraint on det(g_4), dissolving >= 50 OOM. FAIL if fiber and base volume elements are independent, no CC suppression. INFO if partial constraint with suppression < 50 OOM but > 0.

**Results**:

**Verdict: FAIL** -- The Jensen volume-preservation Vol(K) = const is a constraint on the INTERNAL geometry (K = SU(3)), not on the EXTERNAL geometry (M^4). The fiber and base volume elements are independent. CC suppression from this mechanism: **0 OOM**.

**Key Numbers:**

| Quantity | Value | Source |
|:---------|:------|:-------|
| Vol(K) deviation from 1 on Jensen line | 4.44e-16 (machine epsilon) | 10,000 samples, s in [0, 5] |
| CC gap (OOM) | 117.2 | rho_SA / rho_Lambda_obs at M_KK = 7.43e16 GeV |
| CC suppression from mechanism | 0 OOM | structural argument |
| Einstein frame Omega^2 deviation from 1 | 2.22e-16 | Jensen line has trivial conformal factor |
| Breathing mode excitation phi | < 4.2e-16 | Jensen TT projects out volume mode exactly |
| Conformal exponent b_1 | 0.1581 | sqrt(2/(k(k+m-2))) with k=8, m=4 |
| R_K effective at fold | 12.34 | From a_2 = 2776.2 via R_K V_K = 6 a_2 |
| Sigma modulus mass | 7.34 M_KK | S59 CHEEGER-SIGMA-59 PASS |

**Mathematical Argument (5 independent lines converging to FAIL):**

1. **Volume element factorization.** For any Riemannian submersion, vol(g_P) = vol(g_K) ^ vol(g_4). This factorization is exact regardless of the O'Neill A-tensor and T-tensor. The constraint Vol(K) = const enters the 4D action (Paper 13 eq 3.41) as a multiplicative constant: S_4D = (V_K / 2 kappa_P) int_{M^4} [R_M - 2 Lambda_eff] sqrt(-g_4) d^4x. The variation delta(S_4D)/delta(g_4^{mu nu}) gives standard 4D Einstein equations, not trace-free unimodular equations. V_K = const rescales Newton's constant but does not constrain det(g_4).

2. **Constraint on different objects.** The Jensen TT condition constrains the internal metric g_K (1 scalar constraint on an 8D object). Unimodular gravity constrains the external metric g_4 (1 scalar constraint on a 4D object). These are independent objects: the fiber metric at each point x in M^4 lives in Met(K), while g_4 lives in Met(M^4). No coupling between them transmits the internal constraint to the external geometry.

3. **O'Neill tensor analysis.** The A-tensor (gauge field strength F_A) and T-tensor (mean curvature N) provide curvature coupling between base and fiber (Paper 15 eq 1.5: R_P = R_M + R_K - |F|^2 - |S_ring|^2 - |N|^2 - 2 delta_check N). These are CURVATURE couplings, not VOLUME couplings. The term |d_A(vol_{g_K})|^2 in Paper 15 eq 1.5 vanishes identically on the Jensen line, confirming that the volume mode is decoupled from the dynamics.

4. **Einstein frame analysis.** On the Jensen line, the Jordan-to-Einstein frame conformal factor is Omega^2 = (Vol(K)/V_0)^{2/m} = 1 identically. The breathing mode phi = -k b_1 ln(Vol(K)/V_0) = 0 exactly. This means no conformal rescaling is needed -- the Jensen line IS already in Einstein frame. But this is a statement about the absence of conformal mode dynamics, not about constraining det(g_4).

5. **12D unimodular requirement.** For unimodular gravity to emerge from dimensional reduction, the 12D theory itself must be unimodular: sqrt(-g_12) = epsilon_12 (Henneaux-Teitelboim 1989). Then sqrt(g_K) sqrt(-g_4) = epsilon_12, and with Vol(K) = const, this WOULD constrain sqrt(-g_4). But the standard Einstein-Hilbert action on M^4 x K does not impose this constraint. Unimodular gravity in 12D is a separate theoretical assumption not entailed by the Kaluza-Klein framework.

**Cross-Checks:**

- Vol(K) verified to machine epsilon (4.4e-16) across 10,000 samples spanning s in [0, 5]
- Baptista's phi-deformation (Paper 13 eq 2.37) changes volume by up to 84.8% at |phi|^2 = 0.24, confirming volume-preservation is specific to the Jensen TT-deformation, not a generic property
- Einstein frame conformal factor Omega^2 deviates from 1 by < 2.2e-16 on Jensen line (numerically zero)
- Breathing mode phi is numerically zero (< 4.2e-16) on Jensen line
- S59 CHEEGER-SIGMA-59 PASS confirms sigma stability (m_sigma = 7.34 M_KK), so the internal geometry is rigid against both volume AND off-Jensen deformations

**Positive Consequences (Vol(K) = const, non-CC):**

While Vol(K) = const does NOT provide unimodular gravity or CC suppression, it has three important structural consequences:

1. **Newton constant stability**: G_4 = G_12/V_K is exactly constant along the Jensen line. dG/dt / G = 0 identically, satisfying LLR bounds trivially.
2. **No moduli problem**: The volume breathing mode is projected out by the TT constraint. There is no light scalar from the volume modulus.
3. **Shape-only dynamics**: All internal evolution is in the shape mode (Jensen parameter s), not the volume mode. This is cleaner than generic KK compactification.

**Data Files:**
- `computations/s60_unimod_grav.py` -- computation script (derivation + numerical verification)
- `computations/s60_unimod_grav.npz` -- all numerical results (28 KB)

**Assessment:**

The unimodular gravity mechanism is CLOSED. The Jensen volume-preservation constrains the internal geometry but leaves the 4D metric fully dynamical. The CC gap at 117.2 OOM is unchanged. The constraint on det(g_4) required for unimodular gravity cannot emerge from the Kaluza-Klein framework with standard Einstein-Hilbert action; it would require the 12D theory to be unimodular as an additional assumption. The structural reason is clean: the volume element of a Riemannian submersion factorizes into fiber and base contributions, and constraining one does not constrain the other. The mechanism's positive legacy is the three non-CC consequences (Newton stability, no moduli, shape-only dynamics), which remain structurally important for the framework's internal consistency.

---

## Decision Point 0

Review W0 results. If UNIMOD-GRAV-60 is PASS, the CC problem structure changes fundamentally -- redirect W1 to explore the integration constant determination rather than the staircase extension. If FAIL, proceed with the staircase and Strutinsky route as planned.

**Decision**:

*(Team-lead writes here after W0 completes)*

---

## Wave 1: CC Staircase Extension + Strutinsky + Inter-Sector Zubarev

### W1-1: Lambda(N_pair) Staircase for N=3,4 (landau-condensed-matter-theorist)

**Status**: COMPLETE
**Gate**: STAIRCASE-EXT-60. PASS if Lambda_residual decreases monotonically with N (suggesting approach to Lambda_obs at larger N). FAIL if Lambda_residual increases or oscillates. INFO if Lambda_residual decreases but gap remains > 10^{100} at N=4.

**Results**:

**Verdict: FAIL** -- |Lambda_residual(N)| oscillates: 0.360 (N=1) -> 0.293 (N=2) -> 0.368 (N=3). Not monotonically decreasing. No approach to observation.

**INCONSISTENCY CORRECTION**: The S59 Mack-Landau workshop staircase mixed two conventions: E_GS(1) = -0.046 included diagonal V[k,k] self-pairing, while E_GS(2) = +0.325 excluded it (taken from the s54 code which skips k=kp in the scattering sum). This script uses a CONSISTENT convention (diagonal V[k,k] INCLUDED, which is the standard BCS reduced Hamiltonian). The corrected E_GS(2) = +0.268, not +0.325. Both conventions are computed for completeness.

**Key Numbers** (Convention A: bare V_fold, diagonal included; all in M_KK units):

| N_pair | dim = C(8,N) | E_GS (M_KK) | mu = E(N+1)-E(N) | Lambda_res |
|:-------|:-------------|:-------------|:------------------|:-----------|
| 0 | 1 | 0.000000 | -0.046415 | -- |
| 1 | 8 | -0.046415 | +0.314029 | -0.360444 |
| 2 | 28 | +0.267614 | +0.607304 | -0.293275 |
| 3 | 56 | +0.874918 | +0.975280 | -0.367976 |
| 4 | 70 | +1.850198 | -- | -- |

The Lambda_residual = 2*E(N) - E(N-1) - E(N+1) is the discrete second derivative (negative of curvature). Its magnitude |Lambda_res| = {0.360, 0.293, 0.368} oscillates -- it dips at N=2 then rebounds at N=3, ruling out monotone decrease.

**q-theory equilibrium**: mu(N) = E(N+1) - E(N) crosses zero between N=0 and N=1. Linear interpolation gives N_eq = 0.129. The ground state N=1 is the unique minimum. All mu(N) > 0 for N >= 1, so the system is in the rising branch of the equation of state. Adding pairs always costs energy.

**CC gap in physical units**:

| N | |Lambda_res| * M_KK^4 (GeV^4) | Ratio to Lambda_obs | log10(ratio) |
|:--|:------------------------------|:-------------------|:-------------|
| 1 | 1.098e+67 | 4.07e+113 | 113.6 |
| 2 | 8.931e+66 | 3.31e+113 | 113.5 |
| 3 | 1.121e+67 | 4.15e+113 | 113.6 |

The CC gap is 10^{113.5-113.6} at every N value -- completely insensitive to pair number within the (0,0) sector. The absolute vacuum energy |E_GS(1)| * M_KK^4 = 1.41e+66 GeV^4 = 10^{112.7} * Lambda_obs, consistent with the S59 workshop value.

**Spectral gaps and stability**: d^2E/dN^2 is POSITIVE at all N = {1, 2, 3} (values: +0.360, +0.293, +0.368), confirming thermodynamic stability (convexity). The Fock-space spectral gap above E_GS ranges from 0.298 (N=2) to 0.515 (N=4) M_KK -- all well above thermal scales.

**Convention B cross-check** (epsilon_canonical = 0.00374, as in plan specification): E_GS = {0.000, -0.000096, +0.354, +1.013, +2.058}. The pairing is 260x weaker; the staircase is nearly the free-particle result. This convention is quantitatively irrelevant for the CC problem (|E_GS(1)| = 10^{-4} M_KK vs 0.046 M_KK).

**Ground state structure**: Pair occupation analysis shows the lowest modes fill sequentially:
- N=1: mode 0 at 95.6% (single bound pair)
- N=2: modes 0,1 at 98.8%, 94.6% (two-pair shell)
- N=3: modes 0,1,2 at 99.3%, 99.1%, 97.7%
- N=4: modes 0,1,2,3 at 99.6%, 99.4%, 98.9%, 97.0%

This is sequential Pauli filling from the lowest mode upward, with weak inter-mode correlations. The system is in the extreme dilute (BEC) limit, not the BCS regime.

**Cross-checks performed**:
1. Convention A no-diagonal matches s54 stored eigenvalues to machine precision (E_GS(1) = -0.020635, E_GS(2) = 0.32504)
2. V_fold = V_bare_cont verified identical (max difference 2.8e-17)
3. Hamiltonian Hermiticity verified at each N (max |H-H^T| < 1e-14)
4. Fock-space dimensions correct: C(8,N) = {1, 8, 28, 56, 70}
5. Three independent conventions (A, B, A-nodiag) computed; all internally consistent

**Data files**:
- `computations/s60_staircase_ext.py` -- computation script (3 conventions, 4-panel plot)
- `computations/s60_staircase_ext.npz` -- all numerical results (E_GS, mu, Lambda_res, metadata, gate)
- `computations/s60_staircase_ext.png` -- 4-panel diagnostic plot (staircase, mu, Lambda_res, log scale)

**Assessment**: The single-cell Lambda_residual OSCILLATES with N_pair, ruling out the hypothesis that increasing pair number drives the CC residual toward observation. The |Lambda_res| dip at N=2 (0.293) followed by rebound at N=3 (0.368) is characteristic of shell-filling effects in a finite Fock space: N=2 fills two modes with similar energies, producing smoother curvature, while N=3 begins filling a third mode with larger energy gap, steepening the curvature. The CC gap remains locked at 10^{113} regardless of N. The single-cell (0,0) sector q-theory cannot solve the cosmological constant problem through N_pair variation alone. Escape routes: (1) inter-sector equilibration across Peter-Weyl modes (the full SU(3) has ~10^4 modes, not 8), or (2) the Strutinsky renormalization (W1-2) which subtracts the smooth background, isolating the shell correction.

---

### W1-2: Strutinsky Smoothing of PW CC Extension (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: STRUTINSKY-PW-60 = **INFO** (best reduction 9.6 x 10^{-7} at L=5 exceeds 3 OOM threshold, but convergence is non-monotone and the method has a structural limitation: no Fermi surface in the PW CC sum)

**Results**:

**1. Gate Verdict: INFO**

The pre-registered criterion asked whether delta_Lambda converges and achieves < 10^{-3} reduction. The cubic polynomial (poly3) fit of Lambda_eff(L) vs n_modes achieves |delta/Lambda| = 9.6 x 10^{-7} at L=5 (6 OOM reduction), formally exceeding the PASS threshold. However, the convergence ratios are non-monotone (1.67, 0.49, 0.20, 0.073) and the L=1 residual is anomalously large (434% of Lambda_eff). The method also has a structural limitation identified during computation: the Strutinsky energy theorem requires a Fermi surface (partial occupation), which the all-sector PW CC sum lacks. Verdict: INFO rather than PASS.

**2. Key Numbers**

| Quantity | Value | Significance |
|:---------|:------|:-------------|
| Lambda_eff scaling | \|Lambda\| = 0.0053 * n_modes^{2.56} | UV divergence is power-law, not exponential |
| Poly3 residual at L=5 | +1.16 M_KK^4 | Shell correction 10^{-7} of Lambda_eff = -1.2 x 10^6 |
| Poly3 convergence (L=3-5) | ratios 0.20, 0.073 | Rapidly converging after initial oscillation |
| Prediction test (L=1..4 -> L=5) | 3.1% error | Poly3 captures genuine smooth structure |
| Gaussian shell correction | identically zero at all L, all gamma | Theorem: first moment preserved under convolution |

**3. Three Methods Tested**

*Method A: Polynomial in n_modes (most informative).* Poly3 (4 parameters, 1 DOF for 5 data points L=1..5) gives residuals that alternate in sign (+98, -163, +80, -16, +1.2 M_KK^4) and decrease rapidly. This is the classic Strutinsky oscillation pattern. Cross-validation: fit on L=1..4, predict L=5, error = 3.1%. Poly4 (5 params for 5 points) is exact interpolation (residual < 5e-10), confirming poly3 is the appropriate smoothing order.

*Method B: Power-law -A * n^alpha.* Poor fit: residuals oscillate wildly (relative error -586% to +244%). Single-term power law misses curvature in Lambda_eff(n).

*Method C: Quadratic in total PW-weighted Casimir.* Intermediate quality: residuals at L=5 reach 0.04% (comparable to poly2 at 0.04%), but oscillate non-systematically at lower L.

**4. Gaussian Strutinsky Is Identically Zero (Structural Theorem)**

The Gaussian-smoothed single-particle energy sum equals E_exact to machine epsilon for ALL levels (L=0..5) and ALL smoothing widths (gamma/d = 0.8 to 3.0). This is a mathematical identity: Gaussian smoothing preserves the first moment of any distribution. The Strutinsky shell correction from Gaussian smoothing of a FULLY OCCUPIED spectrum is exactly zero. This theorem proves that the standard Strutinsky approach (designed for partially-filled shells with a Fermi surface) does not apply to the PW CC sum where all sectors contribute. In nuclear physics, the shell correction arises because the Fermi surface samples a finite energy window; for the CC, there is no Fermi surface.

**5. Physical Diagnosis: Renormalization, Not Shell Correction**

The nuclear Strutinsky decomposition works because the Fermi energy provides a natural regulator: only levels within ~1-2 hbar*omega of E_F contribute to the shell correction. The PW CC sum has no such regulator. The UV divergence (n_modes^{2.56}) is a renormalization problem requiring a UV cutoff (Connes spectral action, zeta function, or dimensional regularization). The poly3 residuals identify the smooth background that must be subtracted, but do not themselves constitute a renormalization. If a proper renormalization scheme removes the smooth polynomial background, the residual oscillations are under excellent control: they converge rapidly (factor 5-14x per level after L=2) and are sub-percent of the background.

**6. Cross-Checks**

| Check | Result | Status |
|:------|:-------|:-------|
| S58 cross-check at L=0 | Lambda_eff = +0.00140 vs S58 +0.00142 | PASS (1.3%) |
| Poly4 exact interpolation | residual < 5e-10 for 5 pts | Expected (overfitting diagnostic) |
| Weyl law exponent | beta_weyl = 8.1 vs expected 10 (8D) | Reasonable (BCS != sp energy) |
| Gaussian shell correction | zero at all L | Structural theorem confirmed |
| Casimir shift model | dE_max = 0.443 * sqrt(C_2) | Consistent with S59 eigenvalue ranges |
| Poly3 prediction test | 3.1% error on L=5 from L=1..4 | Captures genuine smooth structure |

**7. Data Files**

- Script: `computations/s60_strutinsky_pw.py`
- Data: `computations/s60_strutinsky_pw.npz`
- Plot: `computations/s60_strutinsky_pw.png`
- Output log: `computations/s60_strutinsky_pw_output.txt`

**8. Assessment**

The Strutinsky decomposition applied to the PW CC extension reveals that Lambda_eff(L) is almost perfectly described by a cubic polynomial in n_modes, with tiny oscillating residuals (alternating sign, decreasing by 5-14x per level). This is structurally analogous to the nuclear Strutinsky decomposition where the shell correction is 0.1-0.3% of E_total. However, the nuclear case has a natural regulator (the Fermi energy) that the CC problem lacks. The Gaussian Strutinsky shell correction is identically zero (first-moment theorem), proving that standard Strutinsky does not apply to fully-occupied spectra. The correct tool for the PW UV catastrophe is renormalization, not shell correction. If a renormalization scheme subtracts the smooth cubic background, the residual oscillations converge rapidly, but this requires an independent physical justification for the subtraction. The computation constrains the solution space: the smooth background must be removed by a different mechanism (spectral action cutoff, zeta regularization, or q-theory vacuum selection).

---

### W1-3: Inter-Sector Zubarev Calculation (volovik-superfluid-universe-theorist)

**Status**: COMPLETE
**Gate**: INTER-SECTOR-ZUBAREV-60 **FAIL** -- V_inter = 0 (exact, block-diagonal theorem). Sectors dynamically decoupled. But CC unchanged: Lambda_eq = 0 per sector independently (Volovik equilibrium theorem).

**Results**:

**Gate Verdict**: FAIL. The inter-sector coupling V_inter = 0 exactly, by the block-diagonal theorem (S22b). PW sectors are dynamically decoupled at all orders of perturbation theory.

**Key Numbers**:

| Quantity | Value | Note |
|:---------|:------|:-----|
| V_inter | 0 (exact) | Block-diagonal theorem + Josephson preserves PW labels |
| Gamma_inter (physical) | 0 (exact) | No coupling = no relaxation |
| Gamma_inter (BD residual bound) | 3.74e-27 M_KK | Floating-point artifact, not physical |
| Delta_inter (sector energy gap) | 0.789 M_KK | E_L1_min / E_00_min = 1.96 |
| Lambda_00 | +1.40e-3 M_KK | (0,0) sector, near-cancellation R = 0.004 |
| Lambda_L1 contribution | -22.5 M_KK | L=1 dominates by 16122x |
| CC gap at L=0 | 10^{111.2} | (0,0) sector only |
| CC gap at L=5 | 10^{120.1} | Full PW sum to max_pq=5 |
| Delta_mf (L=0 mean) | 0.717 M_KK | BCS gap, (0,0) sector |
| Delta_mf (L=1 mean) | 2.392 M_KK | 3.34x larger => faster thermalization |

**Structural Proof of Decoupling** (6 steps):
1. D_K block-diagonal in PW basis (S22b, verified to 8.4e-15)
2. V_kl inherits block-diagonality (same Clifford algebra structure)
3. Josephson H_J preserves PW labels (spatial hopping only, diagonal in internal indices)
4. No term in H = H_BCS + H_J mixes PW representations
5. [H, C_2(SU(3))] = 0 where C_2 is the quadratic Casimir
6. PW sector occupations are exact constants of motion at ALL orders

**Physical Consequence**: The inter-sector decoupling does NOT affect the CC calculation. The question "does the full PW sum or only (0,0) contribute?" is rendered moot by the Volovik equilibrium theorem: each sector thermalizes independently (ZUBAREV-CC-59 applies per sector, with the L >= 1 sectors thermalizing FASTER due to larger BCS gaps), and Lambda_eq^{(p,q)} = 0 for each sector. Therefore Lambda_total = sum dim^2 * Lambda_eq^{(p,q)} = 0 regardless of whether inter-sector equilibration occurs. The CC gap is the same at all PW levels: it is the gap between Lambda = 0 and Lambda_obs = 2.7e-47 GeV^4.

**3He-B Analog**: In 3He-B, different angular momentum channels (J=0, J=2, etc.) ARE dynamically coupled through the nonlinear gap equation Delta(k) = Delta * A_{mu,i} * k_i * sigma_mu, which mixes channels at each k-point. In the exflation framework, the block-diagonal theorem forbids this mixing. The framework is MORE decoupled than 3He-B -- it is the analog of multiple separate superfluids that cannot exchange quasiparticles.

**Cross-checks**:
1. Three independent upper bounds computed (BD residual, SA cross-terms, Josephson second-order). Bounds 1 and 3 agree on structural zero.
2. SA cross-terms (Bound 2) give a STATIC energy contribution (V_inter_SA = 335 M_KK) that is NOT a dynamical coupling -- it contributes to equilibrium vacuum energy, not to inter-sector relaxation.
3. Lambda_eff decomposition by PW level reproduces S59 PW-CC-59 results exactly.
4. The formal BD residual bound (Gamma/H_0 ~ 10^{32}) is recognized as a floating-point artifact: epsilon = 8.4e-15 * E is machine epsilon, not a physical coupling. Squaring it and dividing by the tiny H_0 produces a large ratio that has no physical meaning.

**Data files**:
- Script: `computations/s60_inter_sector_zubarev.py`
- Data: `computations/s60_inter_sector_zubarev.npz`
- Plot: `computations/s60_inter_sector_zubarev.png`

**Assessment**: The PW sectors are exactly dynamically decoupled -- the block-diagonal theorem is not merely a numerical observation but an algebraic consequence of the SU(3) representation theory. The Josephson coupling between cells preserves PW labels and therefore cannot mediate inter-sector transfer. This means the (0,0) sector and higher sectors each thermalize independently. Combined with the equilibrium theorem (Lambda_eq = 0 per sector), the CC gap is 120 orders whether computed from one sector or all of them. The question the gate was designed to adjudicate -- whether the physical CC gap is 10^{67} (single sector) or 10^{113} (full PW sum) -- is superseded: BOTH non-equilibrium CC values relax to Lambda = 0, and neither matches observation. The CC problem remains a q-theory problem, not a PW-sector problem.

---

## Decision Point 1

Review W1 results. The Strutinsky reduction and inter-sector decoupling determine the effective CC gap. If both favor the (0,0) sector being the physical contribution with Strutinsky smoothing, the CC gap could shrink from 10^{113} to ~10^{64} -- still enormous but within the landscape of known mechanisms. Update the CC constraint map before proceeding.

**Decision**:

*(Team-lead writes here after W1 completes)*

---

## Wave 2: H_0 Convergence + Spectral Action Hessian + eta-Invariant

### W2-1: Peter-Weyl H_0 Convergence to max(p+q)=4 (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: PW-H0-CONV-60. PASS if |N(L=4) - 4.00| < |N(L=3) - 4.00| (monotone convergence toward sqrt(16)). FAIL if N(L=4) > N(L=3) or N(L=4) < N(L=3) - 0.04 (non-monotone or divergent). INFO if convergence confirmed but |N(L=4) - 4.00| > 0.01.

**Results**:

**Verdict: FAIL** -- N(L=4) = 13.404 >> N(L=3) = 4.859 >> 4.00. The Peter-Weyl spectral sum diverges as L^6.2. N_factor does NOT converge to sqrt(16). S59's N = 3.920 was an artifact of a missing irrep in the S44 eigenvalue data.

**S44 Data Bug Discovery**: The S44 eigenvalue file (`s44_dos_tau.npz`) was missing the (1,2) irrep entirely. S44 listed 9 sectors: (0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1) -- omitting (1,2), the conjugate of (2,1). This gave 992 stored eigenvalues instead of the correct 1232 at L<=3. The missing (1,2) sector contributes a_2 = 87,376 to the spectral sum. This bug originated in S27 (`s27_multisector_bcs.npz`), which defined the sector list with 9 entries rather than 10, and propagated to S44 and S59.

**Key Numbers**:

| Quantity | Value | Notes |
|:---------|:------|:------|
| N(L=3) from S59 | 3.920 | **ARTIFACT**: used S44 data missing (1,2) irrep |
| N(L=3) correct | 4.859 | Complete L<=3 with all 10 irreps |
| N(L=4) | 13.404 | 5 new irreps: (4,0), (3,1), (2,2), (1,3), (0,4) |
| N(L=5) | 31.883 | 6 new irreps: (5,0),...,(0,5) |
| N(L=6) | 67.922 | 7 new irreps: (6,0),...,(0,6) |
| N(L=7) | 121.036 | 7/8 irreps (missing (3,4) due to code limitation) |
| a_2 growth exponent | 6.24 | Power law fit: a_2(L) ~ L^6.2 |
| a_2(L=3) correct | 250,361 | vs S44's 162,984 (54% larger) |
| a_2(L=4) | 1,905,279 | 7.6x larger than L=3 |
| a_2(L=7) | 155,347,470 | 620x larger than L=3 |
| a_2_needed | 10,604 | For exact M_Pl match |
| S44 missing a_2 | 87,376 | From (1,2) irrep alone |
| Total irreps computed | ~48 | L=0 through L=7 |
| Max D_pi matrix size | 1440x1440 | (4,3) at L=7, computed in <5s |

**Why the spectral sum diverges**: The quantity "a_2" = sum_{(p,q)} dim(p,q)^2 * sum_i |lambda_i^{(p,q)}| is Tr(|D_K|), the trace of the absolute value of the Dirac operator, NOT a Seeley-DeWitt heat kernel coefficient. For a Dirac operator on a compact 8-manifold, eigenvalues grow as |lambda_n| ~ n^{1/8} by Weyl's law, and Peter-Weyl multiplicities grow as dim(p,q)^2 ~ (p+q)^4. The total sum diverges because more and more modes contribute at higher levels. The true heat kernel coefficient a_2(D_K^2) is a finite local geometric integral involving Ricci curvature and does not require Peter-Weyl truncation.

**Cross-checks performed**:
1. Conjugate representations have identical spectra: (p,q) vs (q,p) a_2 match to 10^{-14} relative error for all pairs tested (7 pairs)
2. D_pi anti-Hermiticity verified for all 48 irreps: max error < 10^{-10}
3. Eigenvalue purity (Re(lambda) = 0): max |Re(lambda)| < 10^{-10} for all irreps
4. Dimension formula dim(p,q) = (p+1)(q+1)(p+q+2)/2 verified for all 48 irreps
5. S44 a_2 + missing (1,2) a_2 = fresh L=3 a_2 to machine precision (confirms S44 bug is exactly one missing irrep)
6. Growth exponent 6.2 is consistent with Weyl's law for 8D Dirac operator (expected ~8-9 with corrections for the specific group structure)

**Data files**:
- `computations/s60_pw_h0_conv.py` -- computation script (48 irreps, L=0 through L=7)
- `computations/s60_pw_h0_conv.npz` -- all numerical results (level-cumulative and per-irrep)
- `computations/s60_pw_h0_conv.png` -- 4-panel diagnostic plot (a_2 growth, N divergence, per-level contributions, L=4 irrep breakdown)

**Assessment**: This computation closes the "Peter-Weyl convergence toward sqrt(16)" hypothesis. The S59 result N = 3.920 giving H_0 = 68.8 km/s/Mpc was built on two artifacts: (1) a bug in S44 that omitted the (1,2) irrep, and (2) the false assumption that the Peter-Weyl spectral sum converges to a finite limit. The spectral sum Tr(|D_K|) diverges, so it cannot be used as a_2 in the spectral action formula. The H_0 = 68.8 zero-parameter prediction is retracted. A correct H_0 derivation would need the true Seeley-DeWitt heat kernel coefficient a_2(D_K^2), which is a finite geometric integral, not a truncated Peter-Weyl sum. The constraint surface update: the region "N_factor converges to sqrt(16) with increasing L" is EXCLUDED.

---

### W2-2: Full 3D Spectral Action Hessian (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: HESSIAN-3D-60. PASS if all 3 Hessian eigenvalues positive (fold is local minimum in full 3D space). FAIL if one or more negative eigenvalues (fold is saddle point, true minimum off-Jensen). INFO if all positive but one eigenvalue < 10% of largest (flat direction exists).

**Results**:

**GATE VERDICT: FAIL.** All three Hessian eigenvalues negative for the heat-kernel spectral action. Signature (0+, 3-). The fold is a local MAXIMUM of the spectral action Tr[exp(-D^2/Lambda^2)] in the full U(2)-invariant moduli space.

**Key Numbers:**

| Quantity | Value | Cross-check |
|:---------|:------|:------------|
| H_heat eigenvalues | [-1.160e5, -3.006e3, -19.20] | chi8: [-5060, -113.5, -1.35] |
| Richardson eigenvalues | [-1.159e5, -3.006e3, -19.34] | rel. diff < 0.8% |
| H_a2 eigenvalues | [-1.324e6, -3.442e4, -173.4] | all negative |
| H_a4 eigenvalues | [+9.424e3, +1.810e6, +6.960e7] | all positive |
| Signature transition alpha_crit | 54.8 | f_2*Lambda^2/f_0 |
| cos(SA_neg, EJ_neg) 3D | 0.991 (heat), 0.982 (chi8) | angle: 7.9, 11.0 deg |
| cos(SA_neg, EJ_neg) 2D | 0.992 | S59 ref: 0.114 |
| Grid | 5^3 = 125 points, 12880 eigenvalues each | 6.6s total |

**Structural Finding — Cutoff-Regime Dependence:**

The Seeley-DeWitt decomposition H_SA = alpha * H_a2 + H_a4 (where alpha = f_2 * Lambda^2 / f_0) reveals that H_a2 and H_a4 have OPPOSITE definite signatures in all 3 directions:
- H_a2: all eigenvalues negative (fold maximizes scalar curvature integral)
- H_a4: all eigenvalues positive (fold minimizes Gauss-Bonnet integral)

This produces a sharp signature transition at alpha_crit ~ 55:
- alpha < 55 (a_4-dominated): signature (3+, 0-), fold IS a local minimum
- alpha > 55 (a_2-dominated): signature (0+, 3-), fold is a local maximum

The direct heat-kernel computation (f(x) = exp(-x) with Lambda^2 = 4 * max(lambda^2) ~ 17) gives effective alpha >> 55, placing it in the a_2-dominated regime. The chi8 cutoff (f(x) = exp(-x^4)) also sits in this regime. Both confirm (0+, 3-).

**Cross-Checks:**

1. *Richardson extrapolation*: relative difference < 0.8% in all eigenvalues. Finite differences well-converged.
2. *Chi8 vs heat kernel*: same signature (0+, 3-) despite different cutoff shape. CONSISTENT.
3. *Volume-preserving check*: verified analytically that log(Vol) = delta_1, confirming tau and sigma are volume-preserving.
4. *Reference spectrum at fold*: B1 = 0.8197 (canonical: 0.8191, 0.07% off). Agreement with canonical_constants.
5. *S58 comparison*: The S58 SA Hessian (eigenvalues [-98.5, +2424.3], signature (1+, 1-)) used curvature*volume proxy from s54_off_jensen_t2.py (V = -0.5 * M_P^2/M_KK^2 * R/alpha_K), NOT actual Dirac eigenvalues. The (1+, 1-) signature of S58 reflected the curvature proxy's properties, not the spectral action from D_K.

**2D Alignment Discrepancy with S59:**

The 2D cos(SA_neg, EJ_neg) = 0.992 contradicts the S59 result (cos = 0.114). This is because S59 compared the S58 curvature-proxy Hessian (which has a mixed-sign spectrum and hence different eigenvector structure) against the EJ Hessian. The genuine Dirac-eigenvalue SA Hessian, being all-negative, has its "most negative" direction aligned with sigma — the SAME direction as EJ's most negative direction. The near-orthogonality in S59 was an artifact of the curvature proxy's mixed signature.

**Assessment:**

The spectral action computed directly from D_K eigenvalues has no minimum at the fold in any direction. This is a structural extension of the S37 Structural Monotonicity Theorem from 1D (tau-only) to full 3D (tau, sigma, delta_1). The fold is where eigenvalue density is highest, making it a MAXIMUM of Tr[f(D^2/Lambda^2)] for any decreasing f. However, the Gauss-Bonnet contribution (a_4) DOES have a minimum at the fold, with all-positive Hessian. Whether the fold is stable depends on the UV completion: if the a_4 term dominates (alpha < 55), the fold is stable. This is the regime where the spectral action functions as a topological index rather than an action counting modes.

**Data Files:**
- Script: `computations/s60_hessian_3d.py`
- Data: `computations/s60_hessian_3d.npz` (12.9 MB, includes full eigenvalue data at all 125 grid points)
- Plot: `computations/s60_hessian_3d.png`

---

### W2-3: eta-Invariant of D_K at Fold (spectral-geometer)

**Status**: COMPLETE
**Gate**: ETA-INVARIANT-60 -- **FAIL**. eta(0) = 0 exact to machine precision. J-symmetry enforces spectral symmetry. Mechanism 5 CLOSED.

**Results**:

**Gate Verdict**: FAIL. eta(D_K, tau_fold) = 0 exactly. The APS eta-invariant cannot contribute to CC suppression.

**Key Numbers**:
1. **eta(0) = 0** at the fold (tau = 0.19), computed from 21 sectors up to max_pq_sum = 5 (6,048 distinct eigenvalues, 159,936 Peter-Weyl weighted)
2. **Maximum +/- pair error = 2.22e-14** (machine epsilon for float64). Every eigenvalue mu of H = iD_K is paired with -mu to this precision, in every sector independently
3. **N_+ = 79,968, N_- = 79,968, N_0 = 0** -- exact balance, zero kernel
4. **Spectral flow = 0** from tau = 0 to tau_fold (41 steps, max_pq_sum = 3). Zero eigenvalue crossings detected. eta(0) = 0 at every tau along the Jensen path
5. **eta(s) < 10^{-12}** for all s in [0.1, 10.0] -- the eta function vanishes identically, not merely at s = 0

**Cross-Checks**:
- **Sector-by-sector +/- pairing**: All 21 sectors show exact N_+ = N_- balance. Self-conjugate sectors (0,0), (1,1), (2,2) have internal +/- symmetry from the Clifford grading in dim 8. Non-self-conjugate pairs {(p,q), (q,p)} have matching spectra to ~10^{-14} (conjugation maps one to the other)
- **C2^2 = I verified**: The charge conjugation operator C2 = gamma_1 gamma_3 gamma_5 gamma_7 satisfies C2^2 = I exactly (err = 0)
- **Conjugate sector matching**: 9 conjugate pairs checked. Spectra of (p,q) and (q,p) agree to ~10^{-14}. Some pairs show commuting behavior, others anti-commuting -- the distinction is a phase convention, but in both cases the spectral symmetry is enforced
- **eta function convergence**: eta(s) is zero to machine precision for all tested s values (0.1 to 10.0), confirming the vanishing is not an artifact of analytic continuation but a consequence of exact spectral symmetry

**Data Files**:
- Script: `computations/s60_eta_invariant.py`
- Data: `computations/s60_eta_invariant.npz` (107 KB)

**Assessment**: The eta-invariant of D_K vanishes identically along the entire Jensen deformation path, not just at the fold. This is a structural consequence of the +/- spectral symmetry enforced by the real structure J (BDI class, T^2 = +1). The symmetry operates at two levels: (i) within each Peter-Weyl sector, the Clifford algebra in dimension 8 forces eigenvalues into +/- pairs; (ii) between conjugate sectors (p,q) and (q,p), the anti-linear charge conjugation maps eigenvalues bijectively. With zero spectral flow and zero eta-invariant at all tau, there is no topological boundary contribution from the APS index theorem. Mechanism 5 from the Mack-Landau workshop is CLOSED.

---

## Decision Point 2

Review W2 results. The H_0 convergence result determines whether the zero-parameter prediction strengthens. The 3D Hessian determines whether the fold is a true local minimum or merely a saddle point along the Jensen line. The eta-invariant tests whether a topological boundary term contributes to the CC. Update observational constraint map.

**Decision**:

*(Team-lead writes here after W2 completes)*

---

## Wave 3: Leptogenesis + Leggett DM + Leggett Mass

### W3-1: Majorana Leptogenesis from B3 Sector (feynman-theorist)

**Status**: COMPLETE
**Gate**: LEPTO-CP-60 **FAIL** — NCG axiom [J, D_K] = 0 forces M_R real; epsilon_1 = 0 exact.

**Results**:

**Gate Verdict: FAIL.** The J-symmetry theorem (T11: [J, D_K] = 0 at all tau) propagates to the Majorana mass matrix M_R, forcing it to be real symmetric in the natural basis. All CP-violating phases vanish identically. This is the same structural wall (W_J) that killed BCS baryogenesis in S52 (ETA-B-52) and was confirmed in S59 (BARYON-DIAGNOSTIC-59). The wall is universal: it applies to ALL sectors derivable from D_K on deformed SU(3).

**Key Numbers:**

| Quantity | Value | Unit |
|:---------|:------|:-----|
| M_1 (lightest N_R) | 7.461 x 10^16 | GeV |
| M_2 | 8.012 x 10^16 | GeV |
| M_3 (heaviest N_R) | 8.692 x 10^16 | GeV |
| M_3/M_1 (hierarchy) | 1.165 | (quasi-degenerate) |
| epsilon_1 (actual) | 0 | exact (structural) |
| eta_B (actual) | 0 | exact |
| epsilon_1_max (hypothetical DI bound) | 0.5 | (resonant cap) |
| eta_B_max (hypothetical) | 2.6 x 10^{-6} | (+3.6 OOM vs obs) |
| Y_3 (seesaw Yukawa) | 11.9 | (non-perturbative!) |
| E_exc / M_3 | 51.8 | (energy budget OK) |

**Structural Theorem (J-reality of Majorana sector):**

1. [J, D_K] = 0 at all tau (T11, proven S43).
2. The Kosmann-lifted interaction V_kl is real in Peter-Weyl basis (D_K block-diagonal theorem, S22b).
3. The B3 sub-block V_B3 is real symmetric: V_B3 = V_B3^T = V_B3*.
4. M_R constructed from D_K eigenvalues (real) and V_B3 mixing (real) is real symmetric.
5. Diagonalized by real orthogonal O: M_R = O diag(M_1, M_2, M_3) O^T.
6. Dirac Yukawa Y_nu also real (same J-argument).
7. CP asymmetry epsilon_i ~ Im[(Y^dag Y)^2_{ij}] = 0 identically for all i, j. QED.

**Cross-checks:**

- S59 estimate M_R = 7.27e16 GeV (used E_B3_mean); we get M_1 = 7.46e16 (2.6% agreement).
- S59's epsilon_1_max = 3.58 was unphysical (>1 violates unitarity). Corrected to resonant cap = 0.5.
- Seesaw round-trip verified: m_nu(seesaw) reproduces input m_2, m_3 to machine epsilon.
- Dimensional analysis on all quantities: all consistent.
- B3 masses are NOT monotonically decreasing (non-monotone at large tau), but decrease through the fold region.
- Perturbativity flag: Y_3 = 11.9 is at the boundary of strong coupling. M_R ~ 10^{16.9} GeV is 1-2 decades above the conventional seesaw range (10^{14}-10^{15} GeV). The framework's M_KK is simply too high for perturbative seesaw.

**Hypothetical assessment (IF J-breaking existed):**

The mass budget is not the obstruction. E_exc/M_3 = 52x, so heavy N_R production during the shattering is energetically trivial. With resonant CP violation (Delta_M < Gamma_1), epsilon_1 could reach O(0.1). The hypothetical eta_B ~ 2.6e-6 overshoots observed 6.1e-10 by 3.6 OOM — but washout parameters are crude. In the resonant regime, tuning kappa could bring eta_B into the observed range. The point is moot: epsilon_1 = 0 exactly.

**Constraint Map Update:**

- **New wall W_J_Majorana**: [J, D_K] = 0 forces M_R real in all sectors derivable from D_K. Same structural origin as W_J_BCS (S52). Universal CP shield.
- **Surviving escape routes** (all require EXTERNAL J-breaking):
  - (E1) UV completion beyond NCG axioms (physics above M_KK)
  - (E2) Twisted spectral triple (Connes-Devastato-Lizzi-Martinetti: relaxed first-order condition)
  - (E3) Cosmological CPT violation (time-arrow breaks J during transit?)
  - (E4) Gravitational CP anomaly (non-perturbative J-breaking)

**Data files:** `computations/s60_lepto_cp.npz`, `s60_lepto_cp.png`, `s60_lepto_cp_log.txt`

**Script:** `computations/s60_lepto_cp.py`

---

### W3-2: Leggett Mode Cosmological Abundance (volovik-superfluid-universe-theorist)

**Status**: COMPLETE
**Gate**: LEGGETT-DM-ABUND-60 **FAIL** (double failure: 26.4 OOM overclosure AND tau_L/t_U = 8.4e-52)

**Results**:

**Gate Verdict: FAIL.** The Leggett mode at m_L = 0.138 M_KK = 1.03e16 GeV fails as a dark matter candidate on two independent grounds: (1) overclosure by 26.4 orders of magnitude, and (2) gravitational decay lifetime tau_L = 3.6e-34 s, which is 52 orders below the age of the universe. Free-streaming is negligibly small (lambda_fs ~ 10^{-23} Mpc), so the mode would be ultra-cold if it survived -- but it does not survive.

**Key Numbers:**

| Quantity | Value | Status |
|:---------|:------|:-------|
| m_L | 1.025e16 GeV (0.138 M_KK) | Input (S52 GL-JOSEPHSON) |
| n_L per cell | 21.8 quanta | From E_L/omega_L = 3.01/0.138 |
| Omega_L h^2 | 3.23e25 | 26.4 OOM above 0.120 |
| tau_L (grav. decay) | 3.64e-34 s | Gamma = m^3/(32*pi*M_Pl^2) |
| tau_L / t_U | 8.37e-52 | UNSTABLE |
| lambda_fs | 1.95e-23 Mpc | Ultra-cold (if stable) |
| Dilution (a_prod/a_0)^3 | 3.16e-89 | T_prod = M_KK, T_0 = T_CMB |

**Cross-Checks:**

1. Two independent methods (number density x mass, energy fraction) agree exactly on Omega_L h^2 = 3.23e25.
2. Gravitational decay rate cross-checked with S50 Gamma_grav = 5.2e-8 M_KK (agrees to within factor 2, different M_Pl convention).
3. Unreduced M_Pl gives tau_L = 9.2e-33 s -- still 50 OOM short.
4. S50 LEGGETT-DAMPING-50 PASS (Q = 6.7e5) was about Beliaev/Raman channels at the BCS scale, NOT gravitational stability at cosmological timescales. Both results are correct; they apply to different physics.

**Diagnosis (3He analog perspective):**

The double failure is the cosmological moduli problem, which is the EXACT analog of the following situation in superfluid 3He: if you create a Leggett oscillation in a 3He-B droplet of microscopic size (L ~ xi), the oscillation energy is comparable to the gap energy, and the mode radiates away its energy via sound emission (Raman scattering) on timescales much shorter than the droplet's lifetime. The Leggett mode does not "accumulate" in 3He because there is always a dissipation channel available in 3D. In the framework, the dissipation channel is gravitational decay (Gamma ~ m^3/M_Pl^2), which is the 4D analog of Raman emission. The framework's 0D character blocks Raman in the BCS sector (S50) but cannot block gravitational radiation, which couples to all energy-momentum.

The overclosure problem is separately structural: any particle produced with O(1) occupation at T ~ M_KK ~ 10^16 GeV will overclose the universe by ~26 orders unless diluted by subsequent inflation. This is Coughlan et al. (1983). The framework lacks a dilution mechanism because the transit IS the phase transition -- there is no subsequent inflationary epoch.

**Assessment:** LEGGETT-DM-ABUND-60 is a clean double-FAIL. The Leggett mode cannot be dark matter: it decays in 10^{-34} seconds (far below the BBN timescale of 1 second) and would overclose the universe by 26 orders if it survived. This does NOT invalidate the Leggett mode as a physical excitation of the framework -- it means the Leggett mode's energy must thermalize into lighter degrees of freedom well before BBN. The DM candidate must be sought elsewhere (GGE quasiparticles, which are the surviving relic per FDM-DEPLETION-59, but those have the CC-scale energy density problem from THERMO-EXPANSION-GGE-54).

**Data files:** `computations/s60_leggett_dm_abund.py`, `computations/s60_leggett_dm_abund.npz`

---

### W3-3: Leggett Mode Mass at N_pair = 2 (landau-condensed-matter-theorist)

**Status**: COMPLETE
**Gate**: LEGGETT-MASS-N2-60
- Pre-registered criterion: PASS if omega_L(2)/omega_L(1) < 0.8; FAIL if > 1.2; INFO if in [0.8, 1.2]
- **Verdict: PASS** -- omega_L(2)/omega_L(1) = 0.7611 < 0.8

**Results**:

**1. Key Numbers**

| N_pair | dim(Fock) | E_GS [M_KK] | omega_L [M_KK] | omega_L(N)/omega_L(1) | Q_Leggett ME |
|:------:|:---------:|:------------:|:--------------:|:---------------------:|:------------:|
| 1      | 8         | -0.02064     | 1.5018         | 1.0000                | 0.337        |
| 2      | 28        | +0.32504     | 1.1431         | 0.7611                | 0.483        |
| 3      | 56        | +0.98368     | 0.8347         | 0.5558                | 0.621        |
| 4      | 70        | +2.01947     | 0.4575         | 0.3047                | 0.970        |

The Leggett mode mass decreases monotonically with pair number. At N_pair=2 the mass is 76.1% of N_pair=1; at N_pair=4 it drops to 30.5%. The decrease is approximately linear: omega_L(N) ~ omega_L(1) * (1 - 0.23*(N-1)).

**2. Leggett Mode Identification**

The Leggett mode is identified as the excitation with the largest matrix element of the relative sector-number operator Q = sqrt((N_B2/4 - N_B3/3)^2 + (N_B2 - 4*N_B1)^2). This is the operator conjugate to the relative phase between condensate sectors. Selectivity (ratio of first to second largest matrix element) is 6.3 at N=1 (clean separation) and 1.8-2.0 at N=2,3,4 (still dominant but less isolated, as expected when more excitations become available).

The Q operator matrix element sum rule is satisfied exactly: sum_n |<n|Q|GS>|^2 = Var(Q) to machine precision at all N_pair.

**3. Sector Occupations**

B2 dominates at every filling: f_B2 = <N_B2>/N_pair decreases from 0.995 (N=1) to 0.985 (N=4). B1 occupation grows from 0.005 to 0.058; B3 from 0.0003 to 0.0025. The condensate is overwhelmingly B2-centered at all fillings.

**4. Tau Robustness**

The mass ratio omega_L(2)/omega_L(1) was computed at 5 tau values spanning [0.153, 0.235]:

| tau    | omega_L(1) | omega_L(2) | ratio  |
|:------:|:----------:|:----------:|:------:|
| 0.1531 | 1.6945     | 1.2879     | 0.7600 |
| 0.1735 | 1.5925     | 1.2112     | 0.7605 |
| 0.1939 | 1.5018     | 1.1431     | 0.7611 |
| 0.2143 | 1.4218     | 1.0832     | 0.7619 |
| 0.2347 | 1.3519     | 1.0311     | 0.7627 |

The ratio is remarkably stable: 0.760-0.763 across the entire range. This is a structural result, not a fine-tuned feature.

**5. Cross-Checks**

- Hermiticity: ||H - H^T||/||H|| < 2.2e-17 at all N_pair (machine epsilon)
- Total number conservation: <N_total> = N_pair to 6 decimal places at all N_pair
- Q operator sum rule: sum|<n|Q|GS>|^2 = Var(Q) exact at all N_pair
- N=1 condensation energy E_cond = -0.0206 (consistent with S54 at fold using hybrid Strutinsky approach)

**6. Physical Interpretation**

The omega_L values computed here (1.50, 1.14, 0.83, 0.46 M_KK) are the bare single-cell Leggett excitation energies -- the microscopic cost of transferring a pair from B2 to B1/B3 within one cell. These are distinct from the dressed fabric Leggett frequencies of S56/S59 (0.049-0.138 M_KK), which include the epsilon suppression from the Josephson array.

The physically relevant result is the RATIO omega_L(N)/omega_L(1), which enters the fabric calculation multiplicatively: the dressed Leggett gap scales as omega_L0(N_pair) = omega_L0(1) * [omega_L(N)/omega_L(1)]. The 24% mass reduction at N_pair=2 translates directly to a 24% reduction in the dressed Leggett DM mass.

The monotonic decrease follows from Landau quasiparticle renormalization: as more pairs condense, inter-sector fluctuations soften because the ground state develops stronger sector correlations. The Leggett restoring force is reduced by the growing condensate fraction -- the same physics as Anderson-Bogoliubov mode softening in BEC-BCS crossover.

**7. DM Mass Constraint**

At N_pair=2: corrected f_DM ~ 0.76 * 0.161 = 0.122 (near S57 published 0.119). At N_pair=4: f_DM ~ 0.30 * 0.161 = 0.049 (too low vs Omega_DM/Omega_m = 0.844). The physical N_pair per cell at the fold is constrained to N_pair = 1-2 for the DM fraction to match observations.

**Data Files**:
- Script: `computations/s60_leggett_mass_n2.py`
- Data: `computations/s60_leggett_mass_n2.npz`
- Plot: `computations/s60_leggett_mass_n2.png`

**Assessment**: The Leggett mode mass decreases monotonically with pair number, passing the pre-registered gate at N_pair=2 with ratio 0.761. The result is structurally robust (tau-independent to 0.4%). The mass decrease follows from growing sector correlations in the BCS ground state -- standard Landau quasiparticle renormalization. The N_pair dependence constrains the physical pair density to N_pair=1-2 per cell for the DM fraction to match observations.

---

## Decision Point 3

Review W3 results. If leptogenesis produces epsilon_1 > 10^{-6} AND Omega_DM h^2 is within range, the matter sector (baryons + DM) is self-consistent with zero free parameters. If the Leggett gravitational decay lifetime is short, this constrains indirect DM detection signals.

**Decision**:

*(Team-lead writes here after W3 completes)*

---

## Wave 4: Screening + Bekenstein + Entanglement

### W4-1: Sector-Resolved Dimensional Reduction for Screening (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: SECTOR-DIM-REDUCT-60. PASS if screening ratio > 10^4 (timescape mechanism survives: lapse varies while alpha constrained). FAIL if screening ratio < 100 (no viable decoupling). INFO if screening ratio in [100, 10^4] (partial screening, some tension remains).

**Results**:

**GATE VERDICT: SECTOR-DIM-REDUCT-60 = FAIL** (screening ratio = 16.1 < 100)

**Setup.** The S59 timescape calculation found that spatial tau-variance (delta_tau_eff = 0.0053 from KZ transit) generates delta_G/G = -0.526 and delta_alpha/alpha = 0.033. The timescape mechanism requires delta_N/N ~ 0.08 for DESI w_a, but ALPHA-ENV-43 requires delta_alpha/alpha < 10^{-6}. The question: does the Riemannian submersion structure (Paper 13 eq 3.4) provide additional screening?

**Key structural result: the screening ratio is a fold constant.** Both G_eff and alpha depend on the same one-parameter Jensen deformation tau. The screening ratio is:

R_screen = |delta_N/N| / |delta_alpha/alpha| = (1/2)|frac_da_2| / |clock_coeff|

where frac_da_2 = (1/a_2)(da_2/dtau) = 99.13 and clock_coeff = -3.08. The delta_tau cancels -- the ratio is independent of the amplitude of the spatial tau-variation. This gives:

R_screen = (1/2)(99.13/3.08) = **16.1** (shortfall: 621x below 10^4 threshold)

**Three null results for additional suppression:**

1. **Fiber integration measure (f_phi):** The volume form f_phi(tau) = (1-tau)*sqrt(1-4tau) enters G_eff through the fiber integration of R_M. However, a_2(tau) from the spectral action already includes the fiber volume through the spectral measure. frac_da_2 = 99.13 already incorporates volume form effects. No independent suppression. (1/f)(df/dtau) = -9.57, which is 9.6% of frac_da_2.)

2. **(M_KK/M_Pl)^2 factor:** This is algebraically 1/(4*pi*a_2), the inverse of the coefficient that already determines G_eff. Inserting it would be double-counting. Verified: (M_KK/M_Pl)^2 = 9.31 x 10^{-4}, while 1/(4*pi*a_2_fold) = 2.87 x 10^{-5}. These differ by a factor of ~33 due to the a_2_fold vs a_2_corrected distinction, but the STRUCTURAL identity holds: M_Pl^2 = 4*pi*a_2*M_KK^2.

3. **Sector separation:** G_eff is a sum over all PW sectors (d^2-weighted), while alpha is a point evaluation on the fiber metric. But both trace back to the same g_phi(tau). The singlet (0,0) sector contributes only 0.009% of a_2, so higher sectors dominate G -- but this makes G MORE sensitive to tau, not less. The D_K block-diagonality theorem (S22b) confirms each sector evolves independently, but all track the same tau.

**Physical implication:** The timescape mechanism and ALPHA-ENV-43 are structurally incompatible. To achieve delta_alpha/alpha = 10^{-6}, the maximum allowed delta_tau = 3.25 x 10^{-7}, which gives delta_N/N = 1.6 x 10^{-5} -- five orders of magnitude below the delta_N/N ~ 0.08 needed for w_a.

**Escape routes (uncomputed):**
- A multi-parameter deformation (separate lambda_1, lambda_2, lambda_3 with independent dynamics) could decouple alpha from G. But the project's Jensen deformation is one-parameter by construction. This would require going beyond Paper 13's framework.
- Running coupling effects could modify clock_coeff at different energy scales. But ALPHA-ENV-43 is a low-energy constraint, and the clock constraint is derived from the full Dirac spectrum.

**Files:** `computations/s60_sector_dim_reduct.py`, `computations/s60_sector_dim_reduct.npz`, `computations/s60_sector_dim_reduct_log.txt`

---

### W4-2: Bekenstein Bound on PW Sectors (hawking-theorist)

**Status**: COMPLETE
**Gate**: BEKENSTEIN-PW-60. PASS if L >= 1 sectors are Bekenstein-saturated and truncation reduces CC by > 10 OOM. FAIL if no sectors are saturated (S_vN << S_Bekenstein everywhere). INFO if some sectors saturated but reduction < 10 OOM.

**Results**:

**BEKENSTEIN-PW-60: FAIL** — No L >= 1 sectors are Bekenstein-saturated. The bound grows faster than the entropy, so higher PW sectors are exponentially further from saturation, not closer. The Bekenstein bound cannot truncate the PW sum.

**What was computed.** For each PW level L = 0..5 at the fold (tau = 0.19):
- Bekenstein bound: S_Bek(L) = 2*pi*R_KK * E_phys = 2*pi*|E_BCS(L)| (in M_KK natural units, since R_KK = 1/M_KK)
- BCS ground state energy |E_BCS| from S59 ED (L=0) and mean-field (L >= 1)
- Entropy: three estimates — S_vN (conservative/liberal from Page curve scaling) and S_max = N_modes * ln(2)

**Core result table:**

| Level L | N_modes | |E_BCS| (M_KK) | S_Bek (nats) | S_max (nats) | S_max/S_Bek |
|:--------|:--------|:---------------|:-------------|:-------------|:------------|
| 0       | 8       | 0.137          | 0.861        | 5.545        | **6.44**    |
| 1       | 56      | 86.6           | 544.1        | 38.8         | 0.071       |
| 2       | 216     | 2,885          | 18,130       | 149.7        | 0.0083      |
| 3       | 616     | 37,638         | 236,485      | 427.0        | 0.0018      |
| 4       | 1,456   | 291,357        | 1,830,649    | 1,009        | 5.5e-4      |
| 5       | 3,024   | 1,916,855      | 12,043,957   | 2,096        | 1.7e-4      |

**Physical explanation.** |E_BCS| scales as N_modes^2.49 (superlinear power law from S59 data), while S_max = N*ln(2) grows linearly. The Bekenstein bound S_Bek = 2*pi*|E_BCS| therefore grows much faster than the available entropy. The saturation ratio S_max/S_Bek decreases monotonically from 6.44 (L=0) to 1.7e-4 (L=5).

**Unexpected finding: (0,0) IS Bekenstein-saturated.** At level 0, S_max/S_Bek = 6.44 and even the exact S_vN/S_Bek = 1.21 (conservative). This means the (0,0) sector's BCS state exceeds the Bekenstein bound for its energy and confinement radius. This is the OPPOSITE direction from the truncation hypothesis — it is the lightest sector that saturates, not the heavy ones.

This (0,0) Bekenstein violation has two possible interpretations:
1. The BCS ground state at the fold is holographically maximal — it carries the maximum information density consistent with its geometric confinement. This connects to the Page curve result (S_ent = 1.38 nats at k=N/2, 24% of random).
2. The effective confinement radius is larger than 1/M_KK for the (0,0) sector (e.g., the full SU(3) volume), which would relax the bound.

**Casimir-adjusted bound** (R_eff = 1/(M_KK * sqrt(C2))): tightens the bound for L >= 1 (reducing S_Bek by sqrt(C2)), but still no saturation. The bound remains dominated by the energy growth.

**Lambda_eff with hypothetical truncation:**
- Full sum (L=0..5): |rho_Lambda|/rho_obs = 1.35e+120 (120.1 OOM gap)
- L=0 only: |rho_Lambda|/rho_obs = 1.57e+111 (111.2 OOM gap)
- Reduction: 8.9 OOM — below the 10 OOM threshold, and physically unjustified regardless

**What this constrains.** The Bekenstein bound cannot serve as a UV cutoff on the PW sum for the CC. The bound is too generous for higher sectors because BCS binding energy grows superlinearly with mode count. Any physical truncation of the PW sum must come from a different mechanism (e.g., dimensional reduction, screening, or the block-diagonal structure itself).

**Classification**: GEOMETRIC. The Bekenstein bound is a geometric property of the confining space. The phononic spectrum enters only through E_BCS.

**Files**: `computations/s60_bekenstein_pw.py`, `s60_bekenstein_pw.npz`, `s60_bekenstein_pw.png`, `s60_bekenstein_pw_output.txt`

---

### W4-3: Entanglement-Area Law on CG(24) Graph (hawking-theorist)

**Status**: COMPLETE
**Gate**: ENTANGLE-CG24-60. PASS if nontrivial quantum extremal surface exists with Lambda suppression > 50 OOM. FAIL if no nontrivial extremal surface (S_gen monotone with partition size). INFO if extremal surface exists but suppression < 50 OOM.

**Results**:

**ENTANGLE-CG24-60: FAIL** — No nontrivial quantum extremal surface exists. The area term dominates the bulk entanglement by a factor of 1.36 x 10^6, making S_gen strictly monotone increasing with partition size. The trivial partition (k=0) is the global minimum. Lambda suppression: **0 OOM**.

**What was computed.** The generalized entropy S_gen(Sigma) = |dSigma| * E_J / (4 * G_eff) + S_bulk(Sigma) was evaluated over all bipartitions of CG(24) = Cayley(S_4, all 6 transpositions), a regular graph with 24 vertices, 72 edges, degree 6, and diameter 3.

**Area-law fit from 4-cell Page curve (S59):**
- S_ent(k=1) = 1.201 nats, S_ent(k=2) = 1.381 nats on K_4 (n_cut = 3, 4 respectively)
- Fit: S_bulk = s_0 * n_cut + gamma, with s_0 = 0.1802 nats/bond, gamma = 0.6608 nats
- S_topo = -gamma = -0.661 nats (NEGATIVE: super-area-law from BCS pairing correlations)

**Effective Newton constant:**
- G_eff = 1/(16*pi*a_2) = 7.17 x 10^{-6} M_KK^{-2}
- E_J(fold) = 7.042 M_KK (from s59_josephson_phase.npz)
- Area coefficient per bond: E_J/(4*G_eff) = 245,652
- Bulk coefficient per bond: s_0 = 0.180
- **Ratio: 1.36 x 10^6** — area term overwhelms bulk by six orders of magnitude

**CG(24) graph cuts (exact k=1..6, sampled k=7..12, symmetric k=13..23):**

| k | min cut | S_area | S_bulk | S_gen | S_gen/S_gen(triv) |
|---|---------|--------|--------|-------|-------------------|
| 0 (triv) | 0 | 0 | 0.661 | 0.661 | 1.00 |
| 1 | 6 | 1.47e6 | 1.742 | 1.47e6 | 2.23e6 |
| 2 | 10 | 2.46e6 | 2.463 | 2.46e6 | 3.72e6 |
| 4 | 16 | 3.93e6 | 3.544 | 3.93e6 | 5.95e6 |
| 8 | 24 | 5.90e6 | 4.985 | 5.90e6 | 8.92e6 |
| 12 | 24 | 5.90e6 | 4.985 | 5.90e6 | 8.92e6 |

Stoer-Wagner global minimum cut: 6 edges (singleton vertex). Cheeger constant h >= 2.0 (well-connected graph).

**Why the QES fails — structural analysis:**

The island formula S = min_I ext_{dI}[A(dI)/(4G) + S_bulk(I+R)] requires a competition between an area term that penalizes the cut and a bulk entropy term that rewards including high-entanglement degrees of freedom. A nontrivial QES exists only when S_bulk grows fast enough relative to the area term to create a minimum at nonzero partition size.

On CG(24): the area term per bond (245,652) exceeds the bulk entropy per bond (0.180) by a factor 1.36 x 10^6. This means cutting even a single edge costs ~10^6 times more in "gravitational area" than it gains in bulk entanglement. The graph is deeply in the **classical regime** where geometry dominates quantum corrections. This is the opposite of the regime where islands form.

**Comparison to the 62 OOM workshop estimate:** The workshop's ~62 OOM estimate appears to have used the volume-law maximum entropy S_max(24 cells) = 24 * 8 * ln(2) = 133.1 nats = 57.8 OOM as the suppression factor. This would require: (a) all 24 cells to be maximally entangled (volume-law), and (b) the area term to be absent. The actual system has area-law entanglement (S ~ 1-5 nats, not 133 nats) AND the area term dominates. The 62 OOM estimate is structurally inapplicable.

**Hypothetical bulk-only suppression (area term removed):**
- k=1: S_bulk = 1.74 nats = 0.76 OOM
- k=12: S_bulk = 4.99 nats = 2.16 OOM
- Even without the area term, the area-law entanglement of the BCS ground state provides at most ~2 OOM of suppression, not 50-62.

**Topological entanglement entropy:** S_topo = -0.661 nats. The negative value confirms the system has super-area-law entanglement from BCS pairing correlations (long-range order). The BDI winding number is 0 (S38), consistent with no topological order and no topological protection for entanglement.

**What region of solution space this constrains:** The entanglement-area-law CC suppression mechanism is CLOSED on the CG(24) Josephson fabric. The obstruction is structural: G_eff is too small (equivalently, a_2 is too large) relative to E_J, placing the system deep in the classical-area-dominated regime where no QES can form. This closure is independent of graph topology — any graph with these coupling constants will have the same area/bulk ratio.

**What remains uncomputed:** Whether a DIFFERENT definition of G_eff (e.g., from the Volovik-Sakharov trace-log rather than the Seeley-DeWitt a_2) could change the area/bulk ratio. The trace-log gives G_eff ~ 1/(N_modes * ln(Lambda/mu)), which could in principle be much larger than the spectral action value. This is the only escape route.

**Files:** `computations/s60_entangle_cg24.py`, `computations/s60_entangle_cg24.npz`, `computations/s60_entangle_cg24.png`

---

## Decision Point 4

Review W4 results. If the screening ratio exceeds 10^4 (W4-1), the timescape mechanism is revived and the w_a prediction changes. If Bekenstein truncation works (W4-2), the CC UV catastrophe is resolved and the effective CC is the (0,0) sector value. If the entanglement area law provides significant suppression (W4-3), it may combine with other mechanisms for the compound test in W7-2.

**Decision**:

*(Team-lead writes here after W4 completes)*

---

## Wave 5: Structural Diagnostics

### W5-1: Richardson-Gaudin Integrals as Explicit Diagnostics (landau-condensed-matter-theorist)

**Status**: COMPLETE
**Gate**: RG-INTEGRALS-60 — **FAIL** (all 8 integrals strongly broken, delta_k > 0.1 for all k). Breaking 99.8% Josephson-dominated. Without Josephson, integrals weakly broken (delta_noJ ~ 0.03-0.07).

**Results**:

**System**: N_pair=2, N_modes=8/cell, N_cells=2, dim(Fock)=120. tau_fold=0.1939, E_J=3.397 M_KK. Input: s56_gge_fabric.npz, cross-checked s58_npair2_integ.npz.

**Method**: Two integral families constructed as explicit 120x120 matrices:

1. **Gaudin integrals**: R_k^G = S_k^z + Sum_{l!=k} (S_k.S_l)/(2(eps_k - eps_l)). Mutually commute exactly: max||[R_k^G, R_l^G]|| = 0 (machine epsilon).

2. **Richardson integrals** (BCS-adapted): R_k^R with coupling g_eff*u_k*u_l/(eps_k - eps_l) from rank-1 SVD of V_fold. Proper integrals for separable BCS.

Hamiltonian decomposed: H_full = H_sep + H_nonsep + H_J. Decomposition exact (||residual||_max = 0). ||H_full||_F=77.6, ||H_J||_F=71.9, ||H_noJ||_F=29.3, ||H_nonsep||_F=1.09.

**Richardson delta_k = ||[H, R_k^R]||_F / ||H||_F (cell 0):**

| Mode k | eps_k | delta_full | delta_noJ | delta_sep | Source |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.000 | 0.3281 | 0.0575 | 0.0549 | Josephson (f_J=0.998) |
| 1 | 0.177 | 0.3281 | 0.0574 | 0.0549 | Josephson (f_J=0.998) |
| 2 | 0.329 | 0.3280 | 0.0556 | 0.0550 | Josephson (f_J=0.998) |
| 3 | 0.523 | 0.3280 | 0.0554 | 0.0548 | Josephson (f_J=0.998) |
| 4 | 0.726 | 0.3284 | 0.0696 | 0.0621 | Josephson (f_J=0.997) |
| 5 | 1.004 | 0.3276 | 0.0330 | 0.0337 | Josephson (f_J=0.999) |
| 6 | 1.079 | 0.3276 | 0.0330 | 0.0333 | Josephson (f_J=0.999) |
| 7 | 1.170 | 0.3277 | 0.0364 | 0.0330 | Josephson (f_J=0.999) |

**Mean values**: delta_full=0.3279, delta_noJ=0.0497, delta_sep=0.0477.

**Breaking source decomposition** (fractional norm ||[H_i, R_k]||/||[H_full, R_k]||):
- Josephson (inter-cell): mean f_J = 0.998 (dominant ALL 8 modes)
- Non-separable V (intra-cell): mean f_nonsep = 0.015 (negligible)
- Separable V (residual): mean f_sep = 0.050

**V_fold separability**: SVD [0.276, 0.133, 0.104, 0.072, 0.071, 0.042, 0.042, 0.007]. Rank-1 fraction=0.643. g_eff=0.276.

**Cell symmetry**: max|delta(cell0) - delta(cell1)| = 1.1e-16 (exact Z_2).

**Physical interpretation**:

RG integrals broken at O(0.33) — STRONG. System NOT integrable in 2-cell Josephson array (consistent with S58 <r>=0.40).

Sharp hierarchical structure:

1. **Josephson dominates** (99.8%): ||[H_J, R_k]||=25.42, mode-INDEPENDENT (collective operator). All RG integrals broken uniformly by inter-cell tunneling.

2. **Intra-cell approximately integrable**: Without Josephson, delta_noJ~0.03-0.07. B3 modes (k=5,6,7) better conserved (delta~0.033) than B2 modes (delta~0.057), reflecting V_fold block structure.

3. **GGE permanence topologically fragile**: S38 "permanent non-thermal GGE relic" valid for ISOLATED cells, breaks in fabric. Thermalization rate vs expansion timescale undetermined — delta_k gives perturbation strength, not thermalization time.

**Gate verdict**: **FAIL**. All 8 integrals strongly broken (delta_k>0.1, mean=0.328). Breaking 99.8% Josephson. Without Josephson, weakly broken (mean delta_noJ=0.050). Intra-cell BCS approximately integrable; inter-cell Josephson destroys it.

**Constraint surface**: GGE permanence requires isolated cells. CC mechanisms relying on exact integrability must explain why Josephson does not thermalize the relic. Candidate: Josephson is surface/volume effect vanishing in thermodynamic limit. Follow-up: GGE-THERM (Thouless time vs transit timescale).

**Classification**: PARTICLE.

**Files**: `computations/s60_rg_integrals.py`, `s60_rg_integrals.npz`, `s60_rg_integrals.png`

---

### W5-2: Nuclear Blocking Interpretation of N_pair = 3 Minimum (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: BLOCKING-N3-60 = **FAIL**. |Delta_OES| minimum at N_pair=5 (0.0336), not N_pair=3 (0.0470). But blocking parameter b(N) has minimum at N_pair=3 -- mixed physics, decoupled observables.

**Results**:

**1. Energy Staircase and OES (from S52 E_vs_N, 8-mode ED)**

| N_pair | E(N) [M_KK] | S_1(N) | Delta_OES(N) | |Delta_OES| |
|:------:|:-----------:|:------:|:------------:|:----------:|
| 0 | 0.000 | -- | -- | -- |
| 1 | 1.440 | 1.440 | -0.0657 | 0.0657 |
| 2 | 3.011 | 1.571 | +0.0506 | 0.0506 |
| 3 | 4.684 | 1.672 | -0.0470 | 0.0470 |
| 4 | 6.450 | 1.766 | +0.0394 | 0.0394 |
| 5 | 8.295 | 1.845 | -0.0336 | **0.0336** (min) |
| 6 | 10.208 | 1.912 | +0.0349 | 0.0349 |
| 7 | 12.190 | 1.982 | -0.0489 | 0.0489 |

|Delta_OES| decreases monotonically from N=1 to N=5, then recovers at N=6,7. This is standard mid-shell OES behavior (Paper 03, sd-shell systematics). The minimum at N=5 (=62.5% filling of 8 modes) corresponds to maximum effective level density near the Fermi surface, not to any special blocking at N=3.

**2. Occupation Numbers v_k^2 = <n_k> (ED ground states)**

| Mode | N=1 | N=2 | N=3 | N=4 |
|:----:|:---:|:---:|:---:|:---:|
| B2[0] | 0.168 | 0.379 | 0.556 | 0.714 |
| B2[1] | 0.164 | 0.375 | 0.559 | 0.719 |
| B2[2] | 0.139 | 0.350 | 0.571 | 0.743 |
| B2[3] | 0.129 | 0.339 | 0.577 | 0.755 |
| B1    | 0.388 | 0.504 | 0.599 | 0.701 |
| B3[0] | 0.004 | 0.016 | 0.041 | 0.107 |
| B3[1] | 0.004 | 0.016 | 0.041 | 0.107 |
| B3[2] | 0.005 | 0.021 | 0.056 | 0.154 |

Key observations:
- B1 crosses half-filling between N=1 (0.388) and N=2 (0.504), confirming B1 as the Fermi-surface mode (S53 result).
- At N=3, the B2 sector and B1 are all in the range [0.55, 0.60] -- near-half-filling for 5 of 8 modes. This is the most BCS-like configuration.
- B3 remains nearly empty at all N (superweak pairing regime, d/Delta >> 1).

**3. Blocking Parameter b(N) = <(v_k^2 - 1/2)^2>**

| N_pair | b(N) | Interpretation |
|:------:|:----:|:--------------|
| 1 | 0.1552 | Sharpest Fermi surface (far from 1/2) |
| 2 | 0.0971 | Intermediate |
| **3** | **0.0808** | **Minimum: most BCS-like (closest to half-filling)** |
| 4 | 0.0858 | Non-monotonic recovery |

The blocking parameter has its minimum at N=3 with a non-monotonic recovery at N=4 (b increases by 6.2%). This confirms that N=3 is the most BCS-like configuration in terms of occupation number smearing around the Fermi surface. The minimum b at N=3 directly reflects the 5 modes near n=0.5 (B2[0-3] + B1), while at N=4, occupations have moved past half-filling into the particle-like regime (v_k^2 > 0.7 for B2).

**4. Coherence Factors (S53 data)**

| N_pair | mean |u^2-v^2| | mean Z_k | Classification |
|:------:|:-------------:|:-----:|:--------------|
| 1 | 0.750 | 0.095 | Mostly particle-like |
| 2 | 0.502 | 0.153 | Intermediate, B1 phononic (Z=0.250) |
| **3** | **0.431** | **0.169** | **Most mixed** (minimum \|u^2-v^2\|, maximum Z) |
| 4 | 0.566 | 0.164 | Recovery toward particle-like |

The coherence factor mean |u^2-v^2| has its minimum at N=3 and the spectroscopic factor mean Z_k has its maximum at N=3. Both confirm that N=3 is the most BCS-like configuration at the Bogoliubov quasiparticle level. The non-monotonicity mirrors the blocking parameter.

**5. Gate Verdict: FAIL (OES) but with blocking-parameter confirmation**

The gate tests whether Delta_OES minimum occurs at N=3. It does not: |Delta_OES| decreases monotonically from N=1 to N=5 (standard mid-shell behavior). The minimum at N=5 reflects maximum level density at 62.5% filling, identical to the nuclear sd-shell pattern where OES is smallest near mid-shell (Paper 03, ^24Mg region).

However, three independent observables DO have their extrema at N=3:
- b(N) minimum at N=3 (0.081)
- mean |u^2-v^2| minimum at N=3 (0.431)
- mean Z_k maximum at N=3 (0.169)

These measure the Fermi surface width, not the pairing gap. The distinction is critical: OES measures the energy cost of adding/removing a pair (a bulk thermodynamic quantity), while b(N) and Z_k measure how close the system is to the BCS ideal of half-filled modes (a microscopic structural quantity).

**6. Nuclear Interpretation**

In nuclear physics (Paper 03), the OES pairing gap Delta^(3)(A) decreases through mid-shell because the single-particle level density increases, spreading pairing correlations over more orbitals. This is exactly what happens here: Delta_OES decreases from 0.066 (N=1, 12.5% filling) to 0.034 (N=5, 62.5%), then recovers by particle-hole symmetry.

The <r> minimum at N=3 is NOT explained by blocking-induced OES staggering. Instead, N=3 occupies a special structural position: it is the filling fraction (37.5%) where the BCS smearing is maximal (5 of 8 modes near half-filling), while the Hilbert space dimension (560) is large enough for Pauli correlations but small enough that Richardson-Gaudin integrability remnants suppress level repulsion. The non-monotonic <r> sequence is an INTEGRABILITY signature, not a pairing signature.

The nuclear analog is the transition from ^20Ne (mid-shell, collective, N=2) through ^24Mg (N=3, maximum deformation and BCS mixing) to ^28Si (subshell closure, seniority, N=4). In the sd-shell, ^24Mg has the largest quadrupole deformation and the most collective rotational band -- it is the "most BCS-like" nucleus, just as N=3 is the most BCS-like configuration here. But the nuclear OES is not minimized at ^24Mg either; it is minimized at the actual mid-shell.

**Files**: `computations/s60_blocking_n3.py` (script), `s60_blocking_n3.npz` (data), `s60_blocking_n3.png` (6-panel figure)

---

### W5-3: Bayesian Error Budget for H_0 (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: BAYESIAN-H0-60 = **FAIL**
**Revised gate criteria** (per W2-1 retraction of H_0 = 68.8): PASS if some spectral ratio converges with well-defined error bars. FAIL if all ratios diverge. INFO if partial convergence with large uncertainties.

**Results**:

**Context.** W2-1 (PW-H0-CONV-60) discovered that the Peter-Weyl spectral sum Tr(|D_K|) diverges as L^{6.2}. The S59 H_0 = 68.8 km/s/Mpc derivation used N_factor = a_2/(a_0/16) at L=3, which happened to give N ~ 4.86 ~ sqrt(16). This was an ACCIDENT of truncation level. At L=7, N = 121.0. The original gate (H_0 credible interval vs Planck) is therefore INAPPLICABLE. I redirect the Bayesian analysis to the question: do ANY spectral action ratios converge as L -> infinity?

**Method.** Bayesian model averaging (BMA) over three truncation models (L=3, 5, 7), three cutoff functions (step, exponential, Gaussian), and tau uncertainty (sigma_tau = 0.01 from CHEEGER-SIGMA-59 stiffness). Uniform prior on models. ANOVA-style variance decomposition. Richardson extrapolation for convergence limit. Incremental shell-by-shell ratio analysis.

**Key results:**

| Ratio | L=3 | L=5 | L=7 | BMA | Converging? |
|-------|-----|-----|-----|-----|-------------|
| a_4/a_2 | 1.634 | 2.165 | 2.695 | 2.157 +/- 0.430 | NO (9.7%/step) |
| N_factor | 25.68 | 34.08 | 42.44 | 25.84 +/- 8.18 | NO (9.6%/step) |
| delta_a4/delta_a2 (incr.) | 1.659 | 2.222 | 2.815 | -- | NO (10.8%/step) |

**Growth exponents** (power-law fit a_n ~ (L+1)^alpha for L >= 2):
- alpha_{a_0} = 8.44, alpha_{a_2} = 9.14, alpha_{a_4} = 9.82
- Effective exponent of a_4/a_2 ratio: alpha_{r42} = alpha_{a_4} - alpha_{a_2} = 0.69
- a_4/a_2 grows as L^{0.69}: the ratio DIVERGES, just slower than individual coefficients

**Incremental ratio analysis** (strongest convergence test). The shell-by-shell ratio delta_a4/delta_a2 for each new PW level L:
- L=0: 0.894, L=1: 1.132, L=2: 1.388, ..., L=6: 2.511, L=7: 2.815
- Step-to-step changes: +0.238, +0.256, +0.270, +0.279, +0.285, +0.289, +0.304
- Changes are NOT decreasing. The last change (+0.304) is LARGER than the previous (+0.289). No convergence.

**Richardson extrapolation**: Using L=5,6,7 Aitken delta-squared gives r_infty = 10.12 +/- 7.43. The extrapolation is UNSTABLE (error 3x larger than L=7 value). This confirms non-convergence; for a convergent sequence, Richardson would sharpen the limit, not explode.

**Variance decomposition for a_4/a_2:**
- Truncation level (L choice): **99.7%** of total variance
- Cutoff function (step/exp/Gaussian): **0.04%**
- tau uncertainty (sigma_tau = 0.01): **0.3%**

The cutoff function choice is negligible (spread < 0.7% at L=7). The tau uncertainty is also negligible. The ONLY source of uncertainty is the PW truncation level -- which is not an uncertainty but a DIVERGENCE.

**Nuclear DFT perspective.** In nuclear DFT (Paper 06, Bayesian UQ), theoretical uncertainty decomposes into (i) model form error (truncation of the functional), (ii) parameter uncertainty, and (iii) numerical convergence error. Here (i) dominates absolutely. The PW expansion is NOT converging to a finite limit for ANY ratio I tested. This is not a precision problem -- it is a structural problem with the truncated PW trace as a proxy for the true Seeley-DeWitt coefficients.

The analogy to nuclear physics is instructive: this is like computing nuclear binding energies by summing over harmonic oscillator shells without regularization. Each shell adds more kinetic energy than the previous, and the ratio KE/PE never converges. The solution in nuclear physics is to use a PROPER energy density functional (local in coordinate space), not a truncated expansion in the HO basis. The framework requires the same: local heat-kernel coefficients computed from curvature, not truncated PW spectral sums.

**What this means physically.** The true Seeley-DeWitt coefficients a_n(D_K^2) are FINITE integrals of local curvature invariants over SU(3). They do not depend on a PW truncation level. The PW spectral sum Tr(lambda^{2k}) up to level L is not computing a_n; it is computing a DIVERGENT partial sum that grows as L^{~9-10}. The ratio a_4/a_2 from this sum grows as L^{0.69}, never stabilizing. To obtain the actual a_n, one must either (a) compute the local heat kernel coefficients directly from the curvature tensor of the Jensen metric, or (b) use zeta-function regularization of the spectral sum, not a raw truncation.

**Constraint map update.**
- CLOSED: H_0 = 68.8 km/s/Mpc from truncated PW trace (retracted by W2-1, confirmed here)
- CLOSED: N_factor = sqrt(16) (accidental at L=3; diverges at all other L)
- CLOSED: Any prediction from raw truncated PW spectral sums (all ratios diverge)
- OPEN+UNCOMPUTED: H_0 from proper a_2 via local heat kernel on Jensen metric
- OPEN+UNCOMPUTED: a_4/a_2 from zeta-regularized spectral sum

**Files:**
- Script: `computations/s60_bayesian_h0.py`
- Data: `computations/s60_bayesian_h0.npz`
- Plot: `computations/s60_bayesian_h0.png`

---

### W5-4: Bayesian Error Propagation for Penrose Threshold (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: BAYESIAN-PENROSE-60. PASS if P(alpha_total > alpha_crit) > 0.90. FAIL if P(alpha_total > alpha_crit) < 0.50. INFO if P in [0.50, 0.90].

**Verdict: INFO** -- P(alpha_total > alpha_crit) = 0.574 +/- 0.002. S59 PASS not robust under parameter uncertainty.

**Results**:

**Method.** Bayesian error propagation using the S59 combination formula alpha_total(omega) = omega * alpha_additive + (1 - omega) * alpha_quadrature, where alpha_additive = alpha_mp + alpha_Andreev and alpha_quadrature = sqrt(alpha_mp^2 + alpha_Andreev^2). Three uncertain parameters: (1) omega ~ Uniform[0.3, 1.0] (overlap between Penrose directions of the multi-pair and Andreev channels); (2) r_npair3 ~ N(0.412, 0.025^2) truncated to [r_Poisson, r_GOE] (ED finite-size error on level spacing ratio); (3) r_Andreev ~ N(0.446, 0.025^2) truncated to [r_Poisson, r_GOE]. N = 100,000 Monte Carlo samples. Both alpha components derived from r via alpha = (r - r_Poisson)/(r_GOE - r_Poisson).

**Nuclear DFT analog (Paper 06, Dobaczewski et al.):** This is the standard problem of nuclear DFT uncertainty propagation. When a prediction sits near a threshold (here alpha_crit = 0.5227), the posterior straddles the threshold and the verdict becomes prior-dependent. The methodology is identical to propagating coupling-constant uncertainties through HFB to nuclear masses near the drip line.

**Key numbers:**

| Quantity | Value | Note |
|:---------|:------|:-----|
| alpha_total (S59 central) | 0.555 | omega = 0.70 |
| alpha_total (posterior median) | 0.562 | Full uncertainty |
| alpha_total (posterior std) | 0.209 | Dominated by r uncertainty |
| 68% CI | [0.359, 0.776] | Straddles alpha_crit |
| 95% CI | [0.178, 0.994] | Extremely wide |
| P(alpha > alpha_crit) | 0.574 +/- 0.002 | Barely above coin flip |
| omega_crit (central alphas) | 0.477 | Inside prior [0.3, 1.0] |
| omega_crit (median, with alpha uncertainty) | 0.407 | 68% CI: [0.121, 0.775] |
| Var decomposition: omega | 1.9% | NOT the dominant source |
| Var decomposition: r (level spacing) | 100.8% | DOMINANT source |
| P(PASS \| omega-only uncertainty) | 0.748 | Would be INFO even without r |
| P(PASS \| r-only uncertainty) | 0.587 | Level spacing ratio is decisive |

**Variance decomposition surprise.** The overlap parameter omega, flagged by S59 as the key uncertainty, contributes only 1.9% of the total posterior variance. The dominant uncertainty (101%) comes from the level spacing ratios r_npair3 and r_Andreev. These enter through the linear mapping alpha = (r - r_Poisson)/(r_GOE - r_Poisson), where r_GOE - r_Poisson = 0.144 is a small denominator. A sigma_r = 0.025 uncertainty on r translates to sigma_alpha = 0.025/0.144 = 0.174, which is 31% of the central alpha_Andreev value. This amplification is the bottleneck.

**Prior sensitivity.** P(PASS) is stable across omega priors: Uniform[0, 1] gives 0.54, Uniform[0.3, 1.0] gives 0.57, Uniform[0.5, 1.0] gives 0.60, Beta(5,2) gives 0.59, Gaussian(0.7, 0.15) gives 0.59. No reasonable omega prior pushes P above 0.60. Similarly, sigma_r in [0.010, 0.040] gives P in [0.58, 0.61]. The INFO verdict is robust to prior choices.

**Physical interpretation.** The S59 PENROSE-ACCESS-59 PASS was conditional on omega = 0.70 and exact level spacing ratios. Under Bayesian uncertainty propagation:

1. The 95% CI on alpha_total spans [0.18, 0.99], meaning parameter space includes both deep FAIL and strong PASS regions.
2. P(PASS) = 0.574 is only 0.074 above the coin-flip level. The Penrose channel is not decisively accessible.
3. omega_crit = 0.477 (at central alphas) lies at the 31st percentile of the omega prior. Above omega_crit, the channel opens; below, it is blocked. This is a genuine 50/50 situation under current knowledge.
4. The bottleneck is NOT omega but the level spacing statistics. Reducing sigma_r from 0.025 to 0.010 (by computing with larger Fock spaces or more modes) would raise P(PASS) to ~0.61. Even this is insufficient for a robust PASS.

**What would change the verdict?**

- To reach PASS (P > 0.90): would need either (a) sigma_r < 0.005 AND r values confirmed at current centrals, or (b) a first-principles derivation of omega > 0.65, or (c) independent confirmation of alpha_total > 0.60 from a different observable.
- To reach FAIL (P < 0.50): would need either (a) revised r_npair3 < 0.40 (closer to Poisson), or (b) demonstration that Andreev channel is weaker than r = 0.446.

**Constraint map update.** PENROSE-ACCESS-59 PASS is DOWNGRADED to INFO. The CC chain S56-S58-S59 now reads: integrability holds (S56-S58), threshold crossing is indeterminate (S59 + S60 Bayesian). The Penrose channel is neither open nor closed -- it requires higher-precision level statistics to resolve.

**Files:**
- Script: `computations/s60_bayesian_penrose.py`
- Data: `computations/s60_bayesian_penrose.npz`
- Plot: `computations/s60_bayesian_penrose.png`

---

## Decision Point 5

Review W5 results. The RG integrals identify which modes break integrability (informing future CC/screening work). The Bayesian H_0 error bar turns the prediction from a number into a measurement. The Penrose Bayesian analysis determines the CC chain's weakest link robustness.

**Decision**:

*(Team-lead writes here after W5 completes)*

---

## Wave 6: Thermodynamic + Topological Diagnostics

### W6-1: Trans-Planckian Check on Bogoliubov Coefficients (hawking-theorist)

**Status**: COMPLETE
**Gate**: TRANSPLANCKIAN-BOGO-60. PASS if delta_beta_k < 1% for all modes and all modifications (UV-robust). FAIL if delta_beta_k > 10% for any mode (UV-sensitive, sudden quench not universal). INFO if delta_beta_k in [1%, 10%] (mild UV sensitivity).

**Results**:

**VERDICT: FAIL (formal) — but with critical physical caveat**

The formal gate FAILS because modified dispersion relations change the frequency-ratio Bogoliubov coefficient |beta_k|^2 = 0.273 by >10%. However, the physical particle creation (Landau-Zener probability) is structurally protected for B2 modes (van Hove, delta = 0.000%) and only mildly affected for B1/B3 (delta = 2-9%).

**Baseline**: |beta_k|^2 = 0.27260495 (universal, sudden quench, S59). Frequency ratio r = 2.723. All 8 BCS modes at k/k_KK = 0.82-0.98 (NEAR the UV cutoff — worst case for trans-Planckian sensitivity).

**Method B — Ratio-preserving multiplicative modification** (gate-determining):
The modification acts as omega_mod = omega_std * g(omega/Lambda_UV), giving r_mod = r_std * g(omega_i/Lambda)/g(omega_f/Lambda). Since omega_i ~ 3.1 M_KK and omega_f ~ 1.1 M_KK, the nonlinear function g acts asymmetrically on the two endpoints.

| Modification | Mean delta_beta | Max delta_beta | B2 delta | B1 delta | B3 delta |
|:---|---:|---:|---:|---:|---:|
| tanh | 96.7% | 97.5% | 96.3% | 96.0% | 97.5% |
| Unruh | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| Corley-Jacobson | 275.1% | 284.6% | 270.0% | 266.9% | 284.6% |

- **Unruh** gives 0% deviation because both omega_i/Lambda >> 1 and omega_f/Lambda > 1, so g_Unruh = sqrt(1-x^2) maps both to ~0, preserving the ratio exactly.
- **tanh** and **CJ** give large deviations because g(3.1) and g(1.1) differ substantially (the function is nonlinear at x > 1).

**Method D — Van Hove protection (Landau-Zener formula)** (physically correct):
P_LZ(k) = exp(-pi*Delta^2 / |v*dE/dtau|). For B2: dE/dtau = 0 (van Hove condition) => P_LZ = 1.000 EXACTLY, UV-independent. This is the mechanism actually operating during the transit.

| Sector | Modes | P_LZ (standard) | delta (tanh) | delta (Unruh) | delta (CJ) |
|:---|---:|---:|---:|---:|---:|
| B2 | 4 | 1.000000 | 0.000% | 0.000% | 0.000% |
| B1 | 1 | 0.8689 | 4.2% | 8.7% | 8.0% |
| B3 | 3 | 0.9322 | 2.1% | 4.3% | 4.1% |

B2 is STRUCTURAL (van Hove dE/dtau = 0). B1 and B3 are in the INFO range (2-9%).

**Why the formal gate fails but the physics is robust**:
1. The S59 frequency-ratio formula gives |beta|^2 at the FOLD (mid-transit, tau=0.19). The FINAL particle creation probability is n_Bog = 0.999 (S38), set by the van Hove singularity, not the frequency ratio.
2. The modes operate at k/k_KK ~ 0.82-0.98. This is the regime where modified dispersion has MAXIMUM effect — far closer to the cutoff than in standard Hawking radiation (where k/k_cutoff << 1). The trans-Planckian universality theorem (Unruh 1995, Corley-Jacobson 1996) assumes k << k_cutoff, which does NOT apply here.
3. On compact SU(3), there are no trans-Planckian modes to begin with. The "trans-Planckian problem" of standard cosmology (unbounded UV redshifting) is structurally absent.
4. The sudden-quench theorem confirms: |beta|^2 depends ONLY on the ratio r = omega_i/omega_f. The modification changes this ratio when applied nonlinearly to frequencies at different scales.
5. TRANSPLANCKIAN-46 (PASS, 0.0% B2 deviation) remains valid: the physical particle creation mechanism (LZ at van Hove) is UV-independent by theorem.

**Consistency with TRANSPLANCKIAN-46**: That gate used the LZ formula (Method D here) and found EXACT invariance for B2. This S60 gate used the frequency-ratio formula (Method B) and found sensitivity. The two results are CONSISTENT: the frequency ratio is a UV-sensitive intermediate quantity, but the final particle creation probability is UV-independent. The transit's physical outcome does not depend on the UV completion.

**Sudden-quench regime**: dt_transit * omega = 0.0035 << 1 (factor 5,500 below unity). In this limit, the Bogoliubov formula is exact for any given r. The modification changes r itself, not the formula.

**Scripts**: `computations/s60_transplanckian_bogo.py`
**Data**: `computations/s60_transplanckian_bogo.npz`
**Plot**: `computations/s60_transplanckian_bogo.png`

---

### W6-2: Gibbons-Hawking Temperature at Domain Wall (hawking-theorist)

**Status**: COMPLETE
**Gate**: GH-TEMP-DW-60 — **FAIL** (No conical singularity)

**Results**:

The Gibbons-Hawking temperature is **undefined** at the domain wall (tau_DW = 0.1135). Three independent structural reasons close this mechanism permanently.

**Reason 1 — Curvature (structural flat plane):**
The minimum sectional curvature K_sec^min = 0.0 **identically** (not approximately) across the entire range tau in [0, 0.133]. The first Lichnerowicz eigenvalue is lambda_1 = 8.9e-17 (machine zero). This is a structural degeneracy — a flat curvature plane — not a sign crossing. Consequently dK_sec/dtau = 0 identically, giving kappa = sqrt(|dK/dtau|) = 0 and T_DW = kappa/(2*pi) = **undefined**.

Physical interpretation: a flat curvature plane means the geometry is locally product-like (R^1 x M_7), not cigar-like. The Gibbons-Hawking construction requires the Euclidean section to close like a cigar (the (r, tau_E) plane near a horizon), with the "tip" of the cigar determining the periodicity.

**Reason 2 — Metric (no degeneration):**
The Jensen metric components are g_i = alpha * exp(c_i * tau):
- g_1(tau_DW) = 3.764 (u(1), growing)
- g_2(tau_DW) = 2.391 (su(2), shrinking)
- g_3(tau_DW) = 3.361 (C^2, growing)

ALL components strictly positive for all finite tau. No metric component degenerates. No conical singularity can form.

**Reason 3 — Topology (compact, no bolt):**
SU(3) is simply connected (pi_1 = 0). The Euclidean section is compact with no boundary, no asymptotic region where periodicity would be imposed, and no bolt or nut in the smooth Jensen metric.

**Alternative — curvature sign change at tau ~ 0.133:**
The actual K_sec sign change (n_neg: 0 -> 4) occurs at tau_cross = 0.133, which is 16.9% away from tau_DW. A hypothetical temperature there gives:
- dK_sec/dtau = -0.111 at crossing
- kappa_cross = sqrt(|dK/dtau|) = 0.333 M_KK
- T_cross = kappa/(2*pi) = **0.053 M_KK** = 3.9e15 GeV
- T_cross / T_GGE = 0.39 (2.5x too cold)
- T_cross / T_acoustic = 0.47

This crossing is a Lichnerowicz instability onset (second eigenvalue drives 4 curvature planes negative), not a horizon formation. Even if interpreted as a temperature, it does not match T_GGE.

**Constraint map update:**
The Gibbons-Hawking mechanism on the internal geometry is structurally excluded. Temperature in this framework arises from Parker-type particle creation at the fold (T_acoustic = 0.112 M_KK from phonon scattering), not from Euclidean periodicity. This is consistent with the established result that transit is Parker radiation without a horizon (S38-S39 permanent).

**Classification**: GEOMETRIC (purely curvature/topology result, no phononic content)

**Files**: `computations/s60_gh_temp_dw.py`, `s60_gh_temp_dw.npz`, `s60_gh_temp_dw.png`

---

### W6-3: GSL Check on Timescape Mechanism (hawking-theorist)

**Status**: NOT STARTED
**Gate**: GSL-TIMESCAPE-60. PASS if GSL violated (timescape mechanism thermodynamically forbidden, provides independent closure). FAIL if GSL satisfied (timescape thermodynamically consistent, no additional closure). INFO if GSL marginally satisfied/violated within numerical precision.

**Results**:

*(Agent writes here)*

---

### W6-4: Lichnerowicz Eigenvalue Tracking at Domain Wall (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: LICHNEROWICZ-DW-60. PASS if a specific Lichnerowicz eigenvalue crosses zero at tau_DW (explains the domain wall). FAIL if all eigenvalues remain positive through tau_DW (no soft mode, DW unexplained). INFO if an eigenvalue has a minimum near tau_DW but does not cross zero.

**Results**:

**VERDICT: INFO** -- Eigenvalue minimum near tau_DW but no zero-crossing.

**Computation**: Full Lichnerowicz TT spectrum on G-invariant symmetric 2-tensors at 41 tau values in [0.093, 0.133] with Delta_tau = 0.001. All 31 TT modes tracked with adiabatic eigenvector overlap continuity.

**Key numbers**:
- All 31 eigenvalues strictly positive at all 41 grid points. Zero tachyonic modes.
- Global minimum: lambda_min = +0.31498055 at tau = 0.1160, distance 0.0025 from tau_DW = 0.1135.
- lambda_min(tau_DW) = +0.31498831. d(lambda_min)/d(tau) = -0.006 at DW. d^2(lambda_min)/d(tau)^2 = +2.53 (shallow bowl).
- Minimum sector: HARD(su2), degeneracy 5. These are the Jensen deformation modes.

**Spectrum at tau_DW** (8 degeneracy groups, 31 modes total):

| lambda | Degeneracy | Sector |
|:-------|:-----------|:-------|
| 0.3150 | 5 | HARD(su2) |
| 0.3337 | 8 | SOFT(su2-C2) |
| 0.3358 | 3 | C2-C2 |
| 0.3432 | 6 | C2-C2 |
| 0.3456 | 1 | U1-mixed |
| 0.3469 | 4 | U1-mixed |
| 0.6625 | 3 | U1-mixed |
| 0.8577 | 1 | HARD(su2) |

**Physical interpretation**: The Lichnerowicz gap lambda_min(tau) has a shallow minimum at tau ~ 0.116, coinciding (within 0.0025) with the domain wall tau_DW = 0.1135. The gap does NOT close -- minimum value is 31.5% of the bi-invariant value. The HARD(su2) modes (Jensen deformation directions) carry the minimum, consistent with the domain wall being a deformation-mode phenomenon.

**Constraint on phononic mechanism space**: Domain wall instability (if any) cannot arise from a soft TT mode in the singlet Peter-Weyl sector. Any DW condensation must come from:
(a) non-TT sector (conformal modes),
(b) non-singlet PW modes (L > 0),
(c) fermionic/mixed sectors not captured by the Lichnerowicz operator, or
(d) the DW is not a genuine instability but a topological transition point.

The near-coincidence of lambda_min with tau_DW is suggestive but not decisive: the geometry "knows" about the domain wall through its Ricci curvature structure, even though no mode actually softens to zero.

**Files**: `computations/s60_lichnerowicz_dw.{py,npz,png,_log.txt}`

---

## Wave 7: DR3 Pre-Registration + Remaining Computations

### W7-1: DESI DR3 Scenario Pre-Registration (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate**: DR3-PREREGISTER-60. PASS if pre-registration complete with specific numerical predictions for all 3 scenarios. FAIL if cannot compute predictions (missing inputs or inconsistency). INFO if partial pre-registration (not all scenarios covered).

**Results**:

*(Agent writes here)*

---

### W7-2: Compound Mechanism Test: Unimodular + Entanglement (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: COMPOUND-MECH-60. PASS if compound suppression > 80 OOM (CC gap reduced to < 10^{33}). FAIL if compound suppression < 10 OOM or mechanisms interfere destructively. INFO if compound suppression in [10, 80] OOM.
**DEPENDS ON**: W0-3 (UNIMOD-GRAV-60) and W4-3 (ENTANGLE-CG24-60).

**Results**:

**COMPOUND-MECH-60: FAIL** -- Both component mechanisms returned FAIL with 0 OOM suppression each. Compound suppression: **0 OOM**. CC gap unchanged at 118.6 OOM.

**Component Verdicts (loaded from .npz files):**

| Component | Gate | Verdict | Suppression (OOM) | CC Gap (OOM) | Structural Reason |
|:----------|:-----|:--------|:-------------------|:-------------|:------------------|
| W0-3 | UNIMOD-GRAV-60 | FAIL | 0 | 117.2 | Fiber/base volume elements independent; Vol(K)=const constrains g_K not g_4 |
| W4-3 | ENTANGLE-CG24-60 | FAIL | 0 | 120.0 | No nontrivial QES; area/bulk ratio = 1.36e6, deep classical regime |

**Compound Analysis:**

| Quantity | Value |
|:---------|:------|
| Additive suppression | 0 OOM |
| Multiplicative suppression | 0 OOM |
| Destructive interference | None (neither mechanism acts) |
| Remaining CC gap | 118.6 OOM |

**Why the compound is dead (4 independent reasons):**

1. **UNIMOD-GRAV-60 contributes zero.** The Jensen volume-preservation Vol(K) = const constrains the SU(3) fiber geometry but not the M^4 base geometry. The 12D volume element factorizes as vol(g_P) = vol(g_K) ^ vol(g_4), and constraining vol(g_K) leaves vol(g_4) fully dynamical. The 4D Einstein equations emerge with standard trace, not the trace-free unimodular form. Zero times anything is zero.

2. **ENTANGLE-CG24-60 contributes zero.** The area coefficient per bond (E_J/4G_eff = 245,652) exceeds the bulk entropy per bond (s_0 = 0.180) by a factor of 1.36 x 10^6. No nontrivial quantum extremal surface exists. The trivial partition (k=0) minimizes S_gen globally. The system is deep in the classical-area-dominated regime where islands cannot form.

3. **The mechanisms address different aspects and cannot synergize.** Unimodular gravity (if it worked) would remove Lambda from the field equations by constraining det(g_4). Entanglement suppression (if it worked) would reduce Lambda's numerical value via QES corrections. These are logically independent: one changes equation structure, the other changes a numerical input. Since neither works, the distinction is academic.

4. **No escape route for this combination.** UNIMOD-GRAV-60 is closed by a structural theorem (volume element factorization of Riemannian submersions -- cannot be bypassed within KK). ENTANGLE-CG24-60 is closed by numerical ratio (area/bulk = 1.36e6 -- could in principle change with a different G_eff definition, but that is a separate mechanism, not a compound of these two).

**Files:** `computations/s60_compound_mech.py`, `computations/s60_compound_mech.npz`

---

### W7-3: Penrose Process -- Superradiance Analogy (hawking-theorist)

**Status**: COMPLETE
**Gate**: PENROSE-SUPERRAD-60. PASS if total extraction rate * t_universe > Lambda_eff (Penrose process can reduce CC). FAIL if total extraction rate * t_universe << Lambda_eff (Penrose process negligible). INFO if extraction rate non-negligible but insufficient by itself.

**Results**:

**Verdict: INFO** -- Superradiance is kinematically REAL (3 of 8 modes satisfy E_eff < 0 with rates ~0.1 M_KK) but dynamically SELF-LIMITING via back-reaction. The ergosphere closes in t_spindown ~ 5e-42 s (10^{-59} t_universe), limiting total extraction to delta_F = 0.482 M_KK. This is O(1) in framework units, still 114 orders above Lambda_obs. The Penrose mechanism cannot bridge the CC gap.

**Key Numbers**:

| Quantity | Value | Notes |
|:---------|:------|:------|
| alpha_total | 0.5547 | Above alpha_crit = 0.5227 (S59 PENROSE-ACCESS-59 PASS) |
| lambda_alpha (Hessian) | -15.60 | Ergosphere depth — negative eigenvalue at alpha_total |
| Phi_7 (ergosphere) | 1.964 M_KK | K_7 chemical potential from Hessian structure |
| N_superradiant | 3 of 8 | B2_1 (q_7=+1/2), B1 (q_7=+1), B3_2 (q_7=+1) |
| E_eff(B2_1) | -0.805 M_KK | Deepest B2 superradiant mode |
| E_eff(B1) | -1.238 M_KK | B1 mode (coupling ~0 to B3, negligible rate) |
| E_eff(B3_2) | -0.794 M_KK | B3 mode in ergosphere |
| Gamma_SR(B2_1) | 0.0948 M_KK | Fermi golden rule with Bose factor 1.0008 |
| Gamma_SR(B3_2) | 0.1030 M_KK | Dominant extraction channel |
| Gamma_SR(B1) | 4.7e-57 M_KK | Negligible (V_B1_B3 ~ 10^{-59}) |
| Total dLambda/dt | 0.158 M_KK^2/M_KK^{-1} | Instantaneous extraction rate |
| **delta_F_ergo** | **0.482 M_KK** | **Total extractable before back-reaction closes ergosphere** |
| delta_F / Lambda_eff | 10.5 | Can fully extract Lambda_eff (0.046), but... |
| delta_F / Lambda_obs | 10^{113.7} | ...still 114 orders above observation |
| t_spindown | 5.0e-42 s | Ergosphere lifetime (10^{-59} t_universe) |
| Lambda_eff | 0.046 | S59 dimensionless CC residual |
| Lambda_obs_dimless | 8.9e-115 | Observed CC in M_KK^4 units |
| CC gap | 112.7 orders | Lambda_eff / Lambda_obs |
| B2_0 (condensate) | E_eff ~ 0, EXCLUDED | IR regularized: condensate mode, not quasiparticle |

**Superradiance condition**: E_eff(k) = E_k - q_7(k) * Phi_7 < 0, the precise analog of omega < m * Omega_H for Kerr black hole superradiance (Hawking Paper 05, Starobinsky amplification, Zel'dovich 1971). Modes with q_7 > 0 are shifted to negative effective energy by the ergosphere chemical potential Phi_7. Modes with q_7 <= 0 or q_7 = 0 are unaffected (B2_0 condensate mode IR-regulated out).

**Back-reaction analysis**: This is the decisive physical point. The naive linear extrapolation (rate x t_universe) gives extraction >> Lambda_eff, which appears to pass. But back-reaction (analog of Kerr BH spin-down) closes the ergosphere on timescale t_spindown = delta_alpha / (max(Gamma_SR) * alpha_total) ~ 5e-42 s. The total extractable free energy is the integral of |lambda(alpha)| from alpha_crit to alpha_total, which gives delta_F = 0.482 M_KK. This is O(1) in framework units, 114 orders above Lambda_obs. The system relaxes to the marginal GGE (lambda_min = 0) within ~ 10^{-41} s of the transit.

**Hawking analog table**:

| BH Property | Framework Analog | Status |
|:------------|:----------------|:-------|
| Ergosphere (r+ < r < r_ergo) | B3 sector with lambda_alpha < 0 | OPEN |
| omega < m*Omega_H | E_k < q_7 * Phi_7 | 3 modes |
| Superradiant amplification | Bose factor 1/(1-exp(E/T)) | ~1.001 (warm) |
| BH spin-down (J -> 0) | alpha -> alpha_crit (spindown) | t ~ 5e-42 s |
| S_gen = S_BH + S_rad >= 0 | GSL-QTHEORY-46 PASS (35,983x) | Satisfied |
| Radiation to infinity | No — redistribution within Fock space | Key difference |
| Penrose energy ~ M * (J/M^2) | delta_F ~ 0.482 M_KK | O(1), not O(10^{-115}) |

**Cross-checks**:
1. B1 mode has V_B1_B3 ~ 10^{-59} (essentially zero coupling to B3), confirming sector selection rules. The B1 superradiance is kinematically allowed but dynamically suppressed.
2. Bose enhancement factors ~ 1.001 (not divergent) because |E_eff| ~ 0.8 >> T_eff = 0.112. The system is in the classical (not quantum-enhanced) superradiance regime. No BH bomb instability.
3. B2_0 condensate mode (E_sp ~ 0, q_7 = 0) correctly excluded — its E_eff ~ 0 produces a divergent Bose factor (IR catastrophe), which is the condensate zero-mode, not a physical superradiant excitation. Regularization cutoff at E_IR = |E_cond| = 0.137 M_KK.
4. delta_F / Lambda_eff = 10.5: the ergosphere contains enough energy to erase Lambda_eff entirely, but this just means Lambda -> -0.44 M_KK, overshooting past zero by 113 orders past Lambda_obs.

**Constraint surface update**: The Penrose superradiance channel is KINEMATICALLY OPEN but DYNAMICALLY SELF-LIMITING. It reduces Lambda by O(1) in M_KK units via fast spindown (~10^{-42} s), then saturates. The 112-order CC gap requires exponential suppression (e^{-260}), not O(1) extraction. This closes the Penrose channel for CC tuning, adding it to the 27+ closed CC mechanisms. The q-theory self-tuning (Q-THEORY-BCS-45 PASS at tau* = 0.209) remains the unique surviving CC mechanism.

**Physical insight**: The framework's Penrose process is the WARM superradiance regime — T_eff/Delta = 0.64, unlike astrophysical BH superradiance where T_H/omega << 1. Despite this, the warm regime does not help because the back-reaction timescale scales inversely with temperature, making the spindown faster. Warm superradiance = fast spindown = small total extraction. This is a structural result: any analog Penrose process with T ~ O(M_KK) saturates in t ~ O(M_KK^{-1}), extracting O(M_KK) energy — never exponentially small amounts.

**Data files**:
- `computations/s60_penrose_superrad.py` — computation script (7 steps, back-reaction corrected)
- `computations/s60_penrose_superrad.npz` — all numerical results (30 arrays)
- `computations/s60_penrose_superrad.png` — 4-panel diagnostic (E_eff, rates, Hessian, CC gap)
- `computations/s60_penrose_superrad_log.txt` — full computation log

---

### W7-4: Andreev Overlap Parameter from Joint Spectral Statistics (landau-condensed-matter-theorist)

**Status**: COMPLETE
**Gate**: ANDREEV-OMEGA-60 = **PASS**
**Criterion**: PASS if omega > 0.52 (Penrose PASS confirmed from first principles). FAIL if omega < 0.40 (Penrose chain breaks). INFO if omega in [0.40, 0.52].
**Result**: omega = 0.695 +/- 0.067. Superadditive. alpha_total = 0.554, alpha_crit = 0.523, ratio = 1.06. **PASS**.

**Results**:

The overlap parameter omega between the multi-pair (intra-cell) and Andreev (inter-cell) integrability-breaking channels is derived from first principles via a 2D parameter sweep over 400 exact diagonalizations.

**Method.** The Hamiltonian H(alpha_mp, alpha_A) = H_RG + alpha_mp * V_mp + alpha_A * V_A is constructed on the 2-cell N_pair=2 Fock space (dim=120), where:
- H_RG = rank-1 separable BCS + isotropic Josephson (Richardson-Gaudin integrable)
- V_mp = non-separable part of V_bare (rank-1 fraction = 0.643, ||V_mp||/||V_RG|| = 0.745)
- V_A = anisotropic Andreev tunneling (t_k mode-dependent, mean subtracted)

All symmetries are resolved: the cell-exchange operator P is diagonalized exactly (P^2 = I), producing a symmetric (P=+1, 64 states) and antisymmetric (P=-1, 56 states) sector. Level statistics are computed within the irreducible symmetric sector.

**<r> surface.** The 20 x 20 grid yields:

| Point | <r>_sym | delta_r above baseline |
|:------|:--------|:----------------------|
| (0,0) RG baseline | 0.345 | 0.000 |
| (1,0) mp only | 0.406 | +0.061 |
| (0,1) A only | 0.352 | +0.006 |
| (1,1) both | 0.432 | +0.087 |
| Poisson target | 0.386 | -- |

**Superadditivity.** The combined effect (delta_r = 0.087) exceeds the sum of individual effects (0.061 + 0.006 = 0.068). The channels are superadditive: d^2<r>/(d alpha_mp d alpha_A) = +0.54 > 0 at the physical point. This is a resonant enhancement -- the anisotropic Andreev tunneling activates inter-cell correlations that amplify the intra-cell multi-pair breaking.

**Omega extraction.** Five methods:

| Method | omega |
|:-------|:------|
| Full-surface fit (all 400 pts) | 0.695 |
| Synergy coefficient (tanh map) | 1.000 |
| Alpha mapping (safe) | 1.294 |
| r-prediction inversion | 4.183 |
| delta_r formula | 4.183 |

Methods returning omega > 1 reflect the superadditivity -- the linear combination formula alpha_total = omega * (a1 + a2) + (1-omega) * sqrt(a1^2 + a2^2) is an underestimate. The full-surface least-squares fit (RMSE = 0.067) gives omega = 0.695, which is the most robust estimate.

**Penrose propagation.** Using omega = 0.695 with the S59 channel alphas (alpha_mp = 0.181, alpha_A = 0.417):
- alpha_total = 0.554
- alpha_crit = 0.523
- ratio = 1.06
- P(alpha > alpha_crit) = 1.00 within the omega uncertainty band

This confirms the S59 PENROSE-ACCESS-59 conditional PASS from first principles. The S59 modeling choice of omega = 0.70 was within 0.7% of the derived value.

**Physical interpretation.** The positive mixed partial derivative means the two integrability-breaking channels access OVERLAPPING sectors of the level-repulsion structure. In condensed matter language: the intra-cell non-separable pairing creates level correlations that the inter-cell anisotropic tunneling can amplify. This is analogous to the enhancement of chaotic mixing when multiple symmetry-breaking perturbations couple to the same avoided crossings.

**Critical assessment.** The <r> values remain in the intermediate regime (0.345-0.490), well below GOE (0.531). The system is partially chaotic, not fully ergodic. The Penrose threshold alpha_crit = 0.523 corresponds to <r>_crit = 0.462, which is above the surface maximum of 0.490 at the physical point. This means our decomposed Hamiltonian does not itself reach the Penrose threshold -- the threshold crossing relies on combining our omega estimate with the S59 channel alphas computed from separate (and larger) calculations.

**Data files**:
- `computations/s60_andreev_omega.py` (computation script, 45 KB)
- `computations/s60_andreev_omega.npz` (25 KB) -- full 20x20 surfaces, all omega estimates
- `computations/s60_andreev_omega.png` (367 KB) -- 4-panel diagnostic plot

---

### W7-5: q-Theory Geodesic Winding Interpretation (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: Q-THEORY-GEODESIC-60. PASS if N_pair = E_BCS / (geodesic energy quantum) to within 10% (winding interpretation confirmed). FAIL if no correspondence between BCS energy levels and geodesic quantization. INFO if qualitative correspondence but > 10% numerical discrepancy.

**Results**:

**Verdict: INFO** — Two-layer result. Topological layer (K_7 charge = weight lattice winding) is proven and permanent. Dynamical layer (Paper 16 geodesic winding) fails quantitatively — 44× energy mismatch, transit covers 0.06% of one circumference.

**Key Numbers**:

| Quantity | Value | Notes |
|:---------|:------|:------|
| Jensen metric eigenvalues at fold | x_{u(1)}=1.462, x_{su(2)}=0.684, x_{C^2}=1.209 | Volume-preserving to machine eps |
| d(m²_B2)/dτ | -0.840 M_KK² | Mean B2 mass-squared rate |
| Geodesic energy quantum (K_7, n=1) | Δ(m²)/n² = 0.0523 M_KK² | From KK quantization |
| N_pair(geodesic) | 1.35 | vs actual 59.8 pairs — 97.7% discrepancy |
| Geodesic length per winding | L_V(1) = 0.012 M_KK⁻¹ | 0.06% of K_7 circumference (19.54) |
| Dirac Δ(m²) vs geodesic | ratio 0.254 | 4× off, also wrong sign direction |

**Two layers**:
- **Layer 1 (Topological, proven)**: Cooper pair K_7 charge q_7 = ±1/2 IS a weight-lattice winding number. N_pair = 59.8 → total winding Q = ±29.9. Representation theory, holds unconditionally.
- **Layer 2 (Dynamical, fails)**: Paper 16 eq (1.2) geodesic mass variation gives energy quantum 44× too large. Transit too fast for geodesic winding (0.06% of circumference). BCS many-body physics and single-particle geodesics operate at fundamentally different scales.

**Cross-checks**: Volume preservation x₁¹·x₂³·x₃⁴ = 1.000 (exact). Cubic-spline derivatives from 50-point τ sweep. K_7 circumference from Killing norm.

**Data files**:
- `computations/s60_q_theory_geodesic.py`
- `computations/s60_q_theory_geodesic.npz`
- `computations/s60_q_theory_geodesic.png`

**Assessment**: N_pair is a topological charge (weight-lattice quantum number) but NOT a geodesic winding number in the dynamical sense. The geodesic framework correctly describes single-particle mass variation but the many-body pair counting has no geodesic analog. Future mechanisms linking pair number to fiber geometry should go through Richardson-Gaudin integrals (gauge holonomy), not geodesics.

---

### W7-6: Pair Transfer Matrix Elements S_+(k) for N=1,2,3,4 (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: PAIR-TRANSFER-N4-60 = **PASS**
**Criterion**: PASS if 2-cell S_+(1) within factor 2 of 1-cell (1.013). FAIL if < 0.01. INFO if > 2.
**Result**: 2-cell S_+(1) = 0.936, ratio to 1-cell = 0.924. Within factor 2. **PASS**.

**Results**:

#### Method

Constructed the full BCS + Josephson Hamiltonian for N_pair = 0, 1, 2, 3, 4, 5 in the 2-cell pair Fock space (C(16,N) basis states; dimensions 1, 16, 120, 560, 1820, 4368). Exact diagonalization via scipy.linalg.eigh at each N. Ground state eigenvectors extracted. Pair-addition operator S_k^+(cell=0) adds a Cooper pair in mode k of cell 0, mapping N-pair Fock space to (N+1)-pair Fock space. Matrix elements computed as:

P_k(N -> N+1) = <N+1, GS| S_k^+ |N, GS>

S_+(N) = sum_{k=0}^{7} |P_k(N -> N+1)|^2

Similarly for pair-removal S_-(N) via S_k^-(cell=0). All computations use the same eps_fold, V_fold, E_J_fold as the S58/S59 ED series. No free parameters.

#### Energy Staircase

| N_pair | dim | E_GS (M_KK) | mu(N) = E(N)-E(N-1) | d^2E/dN^2 |
|:-------|:----|:------------|:---------------------|:-----------|
| 0 | 1 | 0.000 | -- | -- |
| 1 | 16 | -12.653 | -12.653 | -- |
| 2 | 120 | -23.509 | -10.856 | 1.797 |
| 3 | 560 | -32.556 | -9.047 | 1.809 |
| 4 | 1820 | -39.780 | -7.224 | 1.823 |
| 5 | 4368 | -45.163 | -5.383 | 1.841 |

The chemical potential mu(N) DECREASES with N (pair binding weakens). The pair stiffness d^2E/dN^2 ~ 1.8 M_KK is nearly constant. E_GS monotonically decreases -- the deepest state is at maximum filling, NOT at N=1. The N=1 minimum reported by the workshop is a minimum of the energy PER PAIR, epsilon(N) = E_GS(N)/N, not of E_GS(N) itself.

#### Pair-Transfer Strength Functions

| Transition | S_+(N) | S_-(N+1) | B2 frac | B1 frac | B3 frac |
|:-----------|:-------|:---------|:--------|:--------|:--------|
| 0 -> 1 | 0.500 | 0.500 | 55.5% | 12.1% | 32.4% |
| 1 -> 2 | 0.936 | 0.936 | 54.7% | 12.2% | 33.1% |
| 2 -> 3 | 1.307 | 1.307 | 53.9% | 12.2% | 33.9% |
| 3 -> 4 | 1.615 | 1.615 | 53.1% | 12.3% | 34.6% |
| 4 -> 5 | 1.861 | 1.861 | 52.4% | 12.4% | 35.3% |

**Identity S_-(N) = S_+(N-1): EXACT.** This follows from Hermitian conjugation (S_k^- = (S_k^+)^dagger) and the reality of the ground state wavefunctions (H is real, BDI class). This is the nuclear pair-transfer sum rule: the (t,p) cross section from N to N+1 equals the (p,t) cross section from N+1 to N. Verified to machine precision.

**Cell symmetry check**: S_+(1, cell=0) = S_+(1, cell=1) = 0.936 exactly (Z_2 cell-exchange symmetry).

#### Scaling Law: Bosonic Enhancement with Pauli Blocking

The pair-transfer strength follows a nearly exact bosonic formula:

S_+(N) = (N+1)/2 * (1 - N/N_slots), where N_slots = 16

| N | S_+(N) ED | Bosonic formula | Ratio |
|:--|:----------|:----------------|:------|
| 0 | 0.500 | 0.500 | 1.0000 |
| 1 | 0.936 | 0.938 | 0.9980 |
| 2 | 1.307 | 1.313 | 0.9960 |
| 3 | 1.615 | 1.625 | 0.9941 |
| 4 | 1.861 | 1.875 | 0.9923 |

Agreement to 0.2-0.8% at all N. The factor (N+1) is bosonic enhancement (stimulated emission of Cooper pairs -- the same physics as stimulated emission of photons, but for pair-bosons). The factor (1 - N/16) is Pauli blocking of the underlying fermions (pair-slots already occupied cannot accept another pair). The 0.2-0.8% deviation from the bosonic formula is the effect of the BCS pairing interaction V_fold, which breaks the exact bosonic symmetry. This is a signature of the Josephson coupling E_J >> V_pairing regime (E_J = 3.40 M_KK vs max|V_fold| = 0.08 M_KK, ratio 42:1).

**Nuclear analog**: In nuclear pair transfer (Paper 18), the (t,p) cross section for sd-shell nuclei shows a similar bosonic enhancement for well-deformed nuclei where all pairs are in the same intrinsic orbital. The Pauli blocking factor is familiar from the BCS occupation formula v_k^2. The near-uniformity of |P_k|^2 across modes (max/min ratio 1.35 at N=1, approaching 1.16 at N=4) reflects the Josephson-dominated regime where all modes participate equally, unlike the nuclear case where only modes near the Fermi surface contribute significantly (Paper 03, odd-even staggering).

#### 1-Cell vs 2-Cell Comparison

| Quantity | 1-cell (workshop) | 2-cell (this) | Ratio |
|:---------|:------------------|:--------------|:------|
| S_+(1) | 1.013 | 0.936 | 0.924 |

The 7.6% reduction from 1-cell to 2-cell is physically expected: the Josephson coupling delocalizes each pair over 2 cells, so the pair-creation operator acting on cell 0 has only ~50% overlap with the delocalized pair wavefunction. The formula S_+(1, 2-cell) = S_+(1, 1-cell) * (1 - 1/N_slots) approximately accounts for this: 1.013 * (15/16) = 0.950 vs actual 0.936. The remaining 1.5% difference is from inter-cell correlations in the 2-cell ground state.

#### S_+(0) = 1/2 Exactly: A Structural Result

S_+(0) = sum_k |<1,GS|S_k^+(cell=0)|vacuum>|^2 = sum_{k in cell 0} |psi_GS(k)|^2. Since the N=1 ground state has Z_2 cell-exchange symmetry, the probability of finding the pair in cell 0 is exactly 1/2. This is a STRUCTURAL result, independent of the Hamiltonian parameters.

#### Odd-Even Staggering

| N | delta_3(N) (M_KK) |
|:--|:-------------------|
| 1 | -0.898 |
| 2 | +0.904 |
| 3 | -0.912 |
| 4 | +0.921 |

The staggering delta_3(N) = (-1)^N [E(N+1) - 2E(N) + E(N-1)]/2 shows no significant odd-even effect (magnitudes nearly constant ~0.91). This is consistent with the superweak pairing regime (d/Delta >> 1): there is no sharp distinction between even and odd pair numbers because the pairing gap is much smaller than the level spacing.

#### BCS Coherence Factor Comparison

The BCS approximation |P_k|_BCS ~ sqrt(u_k^2(N+1) * v_k^2(N)) systematically UNDERESTIMATES the ED result by 3-4% (using occupations extracted from prior ED data). This is the expected direction: BCS neglects the Josephson-induced coherence that enhances pair-transfer. The BCS formula works better as N increases (approaching the thermodynamic limit).

#### Constraint Map Update

**What was computed**: Pair-transfer matrix elements S_+(N) and S_-(N) for all N=0,...,5 transitions in the 2-cell system. Mode-resolved |P_k|^2 for all 8 modes at each N. Energy staircase E_GS(N) for N=0,...,5.

**What region of solution space it constrains**: S_+(1) = 0.936 = O(1) confirms that N_pair is NOT topologically or selection-rule locked. Pair-number changes are quantum-mechanically allowed with O(1) matrix elements. The pinning of N_pair = 1 as the physical ground state is THERMODYNAMIC (energy minimum of epsilon(N) = E(N)/N), not kinematic. The bosonic scaling law S_+(N) ~ (N+1)(1-N/16)/2 with <1% corrections confirms the Josephson-dominated regime where V_pairing is perturbative.

**What remains uncomputed**: (1) The physical pair-transfer RATE requires knowledge of the thermal occupation probability and the density of final states at the pair-transfer energy cost Delta_E = E(N+1) - E(N) - E(1). The workshop estimated Gamma_pair ~ 2 * 10^{40} s^{-1}, but this used 1-cell values. (2) The fabric-scale collective pair transfer, where all 32 cells participate, could show qualitatively different scaling. (3) The off-equilibrium pair-transfer dynamics during the transit, where the spectrum is time-dependent, has not been treated.

**Scripts/Data**: `computations/s60_pair_transfer_n4.py`, `.npz`, `.png`

---

## Synthesis

*(Team-lead writes here after all waves complete)*

### Summary of Gate Verdicts

| Gate ID | Wave | Agent | Verdict | Key Number |
|:--------|:-----|:------|:--------|:-----------|
| A4-TRACE-60 | W0 | baptista | **FAIL** | N_a4/N_a2 = 1.823 (82% diff, threshold 20%) |
| CC-DIM-ANALYSIS-60 | W0 | volovik | INFO | Paper 14 seesaw 5.7 OOM off; \|E_cond\|^2 matches at 0.39 OOM (q-theory, not seesaw) |
| UNIMOD-GRAV-60 | W0 | baptista | | |
| STAIRCASE-EXT-60 | W1 | landau | | |
| STRUTINSKY-PW-60 | W1 | nazarewicz | INFO | Poly3 residual 9.6e-7 at L=5 (6 OOM), but non-monotone convergence. Gaussian Strutinsky = 0 (theorem). No Fermi surface in PW sum. Renormalization needed, not shell correction. |
| INTER-SECTOR-ZUBAREV-60 | W1 | volovik | FAIL | V_inter=0 exact. Sectors decoupled. CC unchanged (Lambda_eq=0 per sector). |
| PW-H0-CONV-60 | W2 | baptista | | |
| HESSIAN-3D-60 | W2 | baptista | FAIL | All 3 eigenvalues negative (0+,3-). Fold is SA maximum. a_4 Hessian all-positive; transition at alpha=55. |
| ETA-INVARIANT-60 | W2 | spectral-geom | | |
| LEPTO-CP-60 | W3 | feynman | | |
| LEGGETT-DM-ABUND-60 | W3 | volovik | | |
| LEGGETT-MASS-N2-60 | W3 | landau | | |
| SECTOR-DIM-REDUCT-60 | W4 | baptista | | |
| BEKENSTEIN-PW-60 | W4 | hawking | | |
| ENTANGLE-CG24-60 | W4 | hawking | | |
| RG-INTEGRALS-60 | W5 | landau | | |
| BLOCKING-N3-60 | W5 | nazarewicz | | |
| BAYESIAN-H0-60 | W5 | nazarewicz | | |
| BAYESIAN-PENROSE-60 | W5 | nazarewicz | **INFO** | P(alpha > alpha_crit) = 0.574. S59 PASS not robust. r uncertainty dominates (101% of variance). |
| TRANSPLANCKIAN-BOGO-60 | W6 | hawking | | |
| GH-TEMP-DW-60 | W6 | hawking | **FAIL** | T_DW undefined. K_sec_min=0 structural (L_eig=8.9e-17). Jensen metric all-positive. No conical singularity. T_cross=0.053 at tau=0.133 (0.39x T_GGE). |
| GSL-TIMESCAPE-60 | W6 | hawking | | |
| LICHNEROWICZ-DW-60 | W6 | baptista | **INFO** | lambda_min=+0.3150 at tau=0.116 (0.0025 from DW). All 31 TT positive. Shallow bowl d2lambda/dtau2=+2.53. Min sector: HARD(su2) deg 5. No soft mode. |
| DR3-PREREGISTER-60 | W7 | mack | | |
| COMPOUND-MECH-60 | W7 | baptista | | |
| PENROSE-SUPERRAD-60 | W7 | hawking | **INFO** | 3 SR modes, delta_F=0.482 M_KK, 114 orders above Lambda_obs, t_spindown=5e-42 s |
| ANDREEV-OMEGA-60 | W7 | landau | **PASS** | omega = 0.695 > 0.52, superadditive, alpha_total = 0.554 |
| Q-THEORY-GEODESIC-60 | W7 | baptista | **INFO** | Topological layer (K_7 charge = winding) proven. Dynamical layer fails: 44× energy mismatch, 0.06% circumference. N_pair is topological charge, not geodesic winding. |
| PAIR-TRANSFER-N4-60 | W7 | nazarewicz | **PASS** | S_+(1) = 0.936, ratio 0.924 to 1-cell. Bosonic scaling (N+1)(1-N/16)/2 to <1%. |

### Constraint Surface Update

*(What regions of solution space were narrowed, eliminated, or confirmed?)*

### New Structural Results

*(Permanent results: theorems, exact identities, representation-theoretic facts)*

### Open Questions for S61

*(Carry-forward recommendations)*

---

## Constraint Map Updates

| ID | Type | Old Status | New Status | Evidence |
|:---|:-----|:-----------|:-----------|:---------|
| | | | | |

---

## Files Produced

| File | Description | Wave |
|:-----|:------------|:-----|
| `computations/s60_a4_trace.py` | a_4 trace factor verification script | W0 |
| `computations/s60_a4_trace.npz` | a_4 trace factor data | W0 |
| `computations/s60_cc_dim_analysis.py` | Paper 14 CC dimensional analysis script | W0 |
| `computations/s60_cc_dim_analysis.npz` | CC dimensional analysis data | W0 |
| `computations/s60_unimod_grav.py` | Unimodular gravity derivation script | W0 |
| `computations/s60_unimod_grav.npz` | Unimodular gravity data | W0 |
| `computations/s60_staircase_ext.py` | Lambda staircase extension script | W1 |
| `computations/s60_staircase_ext.npz` | Staircase extension data | W1 |
| `computations/s60_staircase_ext.png` | Staircase extension plot | W1 |
| `computations/s60_strutinsky_pw.py` | Strutinsky smoothing script | W1 |
| `computations/s60_strutinsky_pw.npz` | Strutinsky smoothing data | W1 |
| `computations/s60_strutinsky_pw.png` | Strutinsky smoothing plot | W1 |
| `computations/s60_inter_sector_zubarev.py` | Inter-sector Zubarev script | W1 |
| `computations/s60_inter_sector_zubarev.npz` | Inter-sector Zubarev data | W1 |
| `computations/s60_pw_h0_conv.py` | PW H_0 convergence script | W2 |
| `computations/s60_pw_h0_conv.npz` | PW H_0 convergence data | W2 |
| `computations/s60_pw_h0_conv.png` | N vs L convergence plot | W2 |
| `computations/s60_hessian_3d.py` | 3D Hessian computation script | W2 |
| `computations/s60_hessian_3d.npz` | 3D Hessian data | W2 |
| `computations/s60_hessian_3d.png` | Hessian 2D slice contour plots | W2 |
| `computations/s60_eta_invariant.py` | eta-invariant computation script | W2 |
| `computations/s60_eta_invariant.npz` | eta-invariant data | W2 |
| `computations/s60_lepto_cp.py` | Majorana leptogenesis script | W3 |
| `computations/s60_lepto_cp.npz` | Leptogenesis data | W3 |
| `computations/s60_leggett_dm_abund.py` | Leggett DM abundance script | W3 |
| `computations/s60_leggett_dm_abund.npz` | Leggett DM abundance data | W3 |
| `computations/s60_leggett_mass_n2.py` | Leggett mass at N=2 script | W3 |
| `computations/s60_leggett_mass_n2.npz` | Leggett mass at N=2 data | W3 |
| `computations/s60_sector_dim_reduct.py` | Sector-resolved dimensional reduction script | W4 |
| `computations/s60_sector_dim_reduct.npz` | Sector dimensional reduction data | W4 |
| `computations/s60_bekenstein_pw.py` | Bekenstein PW bound script | W4 |
| `computations/s60_bekenstein_pw.npz` | Bekenstein PW data | W4 |
| `computations/s60_entangle_cg24.py` | Entanglement CG(24) graph script | W4 |
| `computations/s60_entangle_cg24.npz` | Entanglement CG(24) data | W4 |
| `computations/s60_entangle_cg24.png` | CG(24) extremal surface plot | W4 |
| `computations/s60_rg_integrals.py` | Richardson-Gaudin integrals script | W5 |
| `computations/s60_rg_integrals.npz` | RG integrals data | W5 |
| `computations/s60_rg_integrals.png` | RG integral breaking bar chart | W5 |
| `computations/s60_blocking_n3.py` | Nuclear blocking interpretation script | W5 |
| `computations/s60_blocking_n3.npz` | Blocking N=3 data | W5 |
| `computations/s60_blocking_n3.png` | Blocking occupation plot | W5 |
| `computations/s60_bayesian_h0.py` | Bayesian H_0 error budget script | W5 |
| `computations/s60_bayesian_h0.npz` | Bayesian H_0 data | W5 |
| `computations/s60_bayesian_h0.png` | H_0 posterior distribution plot | W5 |
| `computations/s60_bayesian_penrose.py` | Bayesian Penrose threshold script | W5 |
| `computations/s60_bayesian_penrose.npz` | Bayesian Penrose data | W5 |
| `computations/s60_bayesian_penrose.png` | Penrose alpha posterior plot | W5 |
| `computations/s60_transplanckian_bogo.py` | Trans-Planckian Bogoliubov script | W6 |
| `computations/s60_transplanckian_bogo.npz` | Trans-Planckian data | W6 |
| `computations/s60_gh_temp_dw.py` | Gibbons-Hawking temperature script | W6 |
| `computations/s60_gh_temp_dw.npz` | GH temperature data | W6 |
| `computations/s60_gsl_timescape.py` | GSL timescape check script | W6 |
| `computations/s60_gsl_timescape.npz` | GSL timescape data | W6 |
| `computations/s60_lichnerowicz_dw.py` | Lichnerowicz DW tracking script | W6 |
| `computations/s60_lichnerowicz_dw.npz` | Lichnerowicz DW data | W6 |
| `computations/s60_lichnerowicz_dw.png` | Lichnerowicz eigenvalue trajectories | W6 |
| `computations/s60_dr3_preregister.py` | DR3 pre-registration script | W7 |
| `computations/s60_dr3_preregister.npz` | DR3 pre-registration data | W7 |
| `computations/s60_dr3_preregister.png` | Three-panel DR3 forecast plot | W7 |
| `computations/s60_compound_mech.py` | Compound mechanism test script | W7 |
| `computations/s60_compound_mech.npz` | Compound mechanism data | W7 |
| `computations/s60_penrose_superrad.py` | Penrose superradiance script | W7 |
| `computations/s60_penrose_superrad.npz` | Penrose superradiance data | W7 |
| `computations/s60_andreev_omega.py` | Andreev overlap parameter script | W7 |
| `computations/s60_andreev_omega.npz` | Andreev overlap data | W7 |
| `computations/s60_andreev_omega.png` | 2D <r> surface with isolines | W7 |
| `computations/s60_q_theory_geodesic.py` | q-theory geodesic winding script | W7 |
| `computations/s60_q_theory_geodesic.npz` | q-theory geodesic data | W7 |
| `computations/s60_pair_transfer_n4.py` | Pair transfer matrix elements script | W7 |
| `computations/s60_pair_transfer_n4.npz` | Pair transfer data | W7 |
| `computations/s60_pair_transfer_n4.png` | S_+ and S_- vs N plot | W7 |

---

## Session Verdict

**Gate**: RECOMMENDATION-STACK-60
- **PASS**: At least 2 of (UNIMOD-GRAV-60, PW-H0-CONV-60, LEPTO-CP-60) produce PASS or structurally new results
- **FAIL**: All 3 highest-priority computations produce null or negative results
- **INFO**: Exactly 1 of 3 produces a structurally new result
- **Null hypothesis**: The CC gap remains 10^{113}, H_0 convergence is non-monotone, and the Majorana sector has zero CP violation

**Verdict**:

*(Team-lead writes here after synthesis)*

---

## S61 Carry-Forward: Compound Staircase Modification (User-Directed Priority)

**Source**: User observation during S60 Wave 7 review, not captured by any of the 9 collab reviewers in this exact form.

**The problem**: S60 evaluates each CC mechanism independently against the full 113 OOM gap. Every mechanism produces O(1) effects in M_KK units and is classified FAIL because O(1) ≠ 10^{-113}. But the CC is determined by epsilon(N_eq) — the ground state energy at the q-theory equilibrium pair number — which depends on the FULL energy landscape including ALL O(1) corrections simultaneously.

**Specific O(1) effects dismissed individually but collectively uncomputed**:

1. **Penrose superradiance back-reaction**: delta_F = 0.482 M_KK per cell (10× the CC residual epsilon(1) = 0.046). Shifts E_GS(1) by O(1), rearranges the entire staircase. Classified "FAIL for CC" but this is the wrong comparison — it modifies which step the system equilibrates on.

2. **Josephson integrability breaking**: delta_k ~ 0.33 for all 8 RG integrals. Modifies the GGE equilibrium state. Doesn't "solve" CC but changes the ground state energy.

3. **Bekenstein saturation in (0,0) sector**: S_vN/S_Bek = 1.21. The BCS ground state is near holographic saturation — a real physical constraint on the entropy budget that feeds back into the free energy.

**The computation S61 must do**: Rebuild the staircase E_GS(N) with Penrose back-reaction, Josephson-broken integrals, and Bekenstein entropy constraint included self-consistently. Not "does mechanism X bridge 113 OOM?" but "what is epsilon(N_eq) in the full coupled system?"

**Connection to collab suggestions**: Landau's GL free energy (S-1) is the formalism for this. Phonon-First's "wrong compound" reframe (a_4 + q-theory) is the complementary angle. Tesla's impedance analysis could provide the coupling structure. Volovik's chi_q(N) computation provides the vacuum compressibility input.

**Pre-registered gate**: COMPOUND-STAIRCASE-61
- **PASS**: epsilon(N_eq) in the coupled system differs from epsilon(1) = 0.046 by > factor 10 (compound effects are material)
- **FAIL**: epsilon(N_eq) ~ 0.046 (compound effects are perturbative corrections, staircase structure unchanged)
- **INFO**: epsilon(N_eq) differs by factor 2-10 (corrections are significant but don't qualitatively change the landscape)

---

## Lost Treasure Appendix: Cross-Domain CC Approaches

**Source**: Post-S60 discussion. The CC problem in the framework reduces to: minimize a discrete function epsilon(N) over integers on the SU(3) weight lattice. This specific mathematical shape appears in fields that have never been connected to cosmology. Each entry below identifies the field, the structural match, who would know, and what they could compute.

### LT-1: Lattice Basis Reduction (Cryptography)

**The match**: The LLL algorithm (Lenstra-Lenstra-Lovasz, 1982) finds short vectors in high-dimensional lattices. The CC problem is: find a near-cancellation in a sum of BCS energies across Peter-Weyl sectors. The PW sectors form the weight lattice of SU(3). Finding the combination of sector occupations {N_{(p,q)}} that minimizes |epsilon_total| IS a shortest-vector problem on this lattice.

**Why it matters**: The CC gap (10^{113} OOM) might not be a physics problem -- it might be a computational complexity problem. The universe settles at N_pair = 1 (epsilon = 0.046) because finding the global minimum (epsilon -> 0) requires solving SVP on a high-dimensional lattice, which is NP-hard. The vacuum energy is "stuck" at a local minimum because the global minimum is computationally inaccessible -- even to the universe itself.

**Who would know**: Post-quantum cryptographers working on CRYSTALS-Kyber/Dilithium. Lattice reduction specialists (Nguyen, Ducas, Albrecht). The irony: the people trying to make encryption unbreakable might hold the key to why the CC is unbreakably large.

**What they could compute**: Apply LLL or BKZ-2.0 to the SU(3) weight lattice with BCS energies as coordinates. Find the shortest vector in the "CC lattice." Compare to epsilon(1) = 0.046. If the shortest vector is shorter (epsilon_SVP << 0.046), the universe is stuck at a suboptimal minimum. If equal, N_pair = 1 IS the global minimum and the CC gap is fundamental.

**Pre-registerable gate**: LATTICE-SVP-CC
- PASS: epsilon_SVP < 0.001 (global minimum exists far below current vacuum)
- FAIL: epsilon_SVP ~ 0.046 (current vacuum IS the global minimum)
- INFO: epsilon_SVP in (0.001, 0.046) (better minimum exists but improvement is modest)

---

### LT-2: Tropical Geometry

**The match**: Tropical geometry replaces smooth algebraic geometry with piecewise-linear structures. Addition becomes max, multiplication becomes addition. The CC staircase E_GS(N) IS piecewise linear -- it's a sequence of line segments connecting integer-N points. Tropical curves on the toric variety associated to SU(3)'s weight polytope would describe the "tropicalized" version of the spectral action.

**Why it matters**: Tropical methods have already appeared in string theory (Mikhalkin's enumeration of holomorphic curves, tropical amplitudes). The CC staircase might be the tropicalization of a smooth spectral action surface -- the piecewise-linear skeleton that survives when you take the "tropical limit" (Planck scale -> 0). In this picture, the CC gap is an artifact of tropicalization: the smooth surface has a minimum near zero, but the tropical approximation (discrete N_pair) misses it.

**Who would know**: Tropical geometers working on toric varieties (Mikhalkin, Itenberg, Sturmfels). Mirror symmetry specialists who use tropical methods (Gross, Siebert). Scattering amplitude physicists using tropical Feynman integrals (Arkani-Hamed, Cachazo).

**What they could compute**: Construct the Newton polytope of the spectral action as a function of PW sector occupations. Compute the tropical variety. Identify whether the tropical minimum coincides with the smooth minimum (epsilon -> 0) or is displaced (epsilon = 0.046). If displaced, the CC gap is a tropicalization artifact and the smooth spectral action might have a zero.

---

### LT-3: KAM Theory (Dynamical Systems)

**The match**: The KAM theorem (Kolmogorov-Arnold-Moser, 1954-1963) says that nearly-integrable Hamiltonian systems preserve quasi-periodic tori when the perturbation is below a critical threshold. The framework's BCS system has 8 Richardson-Gaudin integrals (exactly integrable) broken by Josephson coupling at delta ~ 0.33. KAM theory predicts whether the GGE (generalized Gibbs ensemble) survives this perturbation or thermalizes.

**Why it matters**: S60 W5-1 found all 8 RG integrals broken at delta > 0.1. But "broken" in a commutator norm is not the same as "thermalized" in a KAM sense. KAM theory distinguishes between: (a) integrals broken but tori surviving (quasi-periodic motion, GGE permanent), (b) tori destroyed, Arnold diffusion, eventual thermalization. The Thouless time that every S60 reviewer demanded is a KAM question in disguise.

**Who would know**: Ergodic theorists and Hamiltonian dynamicists (Poschel, Wayne, Celletti). KAM specialists who work on finite-dimensional systems with 8 degrees of freedom. The nuclear physics community already uses KAM theory for shell model integrability (Zelevinsky, Horoi).

**What they could compute**: Take the 8-mode BCS Hamiltonian H = H_RG + epsilon * V_Josephson. Compute the KAM critical perturbation epsilon_KAM for the 8-dimensional system. Compare to the actual epsilon = 0.33 (Josephson/pairing ratio). If epsilon < epsilon_KAM: GGE survives, non-thermal relic is permanent. If epsilon > epsilon_KAM: GGE thermalizes on the Thouless timescale.

**Pre-registerable gate**: KAM-THRESHOLD-61
- PASS: epsilon = 0.33 < epsilon_KAM (GGE survives, quasi-periodic motion preserved)
- FAIL: epsilon = 0.33 > epsilon_KAM (tori destroyed, Arnold diffusion, GGE thermalizes)
- INFO: epsilon ~ epsilon_KAM (marginal, requires higher-order analysis)

---

### LT-4: Coding Theory (Error-Correcting Codes)

**The match**: The CC staircase's near-cancellation is structurally identical to a code's minimum distance property. In coding theory, the "error" is the deviation from the intended codeword. In the CC problem, the "error" is epsilon(N_eq) -- the deviation of the vacuum energy from zero. A good error-correcting code minimizes the probability that errors accumulate beyond a threshold. A good internal geometry minimizes epsilon.

**Why it matters**: The Leech lattice (the densest lattice packing in 24 dimensions) already appears in string theory (Narain lattice for the bosonic string). SU(3)'s weight lattice is a 2D sublattice of a larger structure. If the CC is a statement about how well the weight lattice "corrects" vacuum energy errors, then the optimal internal geometry is the one whose weight lattice has the best error-correcting properties. SU(3) might be selected by the universe because its lattice is the best "code" for minimizing vacuum energy among all compact Lie groups.

**Who would know**: Algebraic coding theorists working on lattice codes (Conway, Sloane, Ebeling). Sphere packing specialists. String theorists working on Narain lattices and moonshine (Cheng, Duncan, Harvey).

**What they could compute**: Compute the covering radius and packing density of the SU(3) weight lattice weighted by BCS energies. Compare to other compact Lie groups (SU(2), SU(4), G2, Spin(7)). If SU(3) has the smallest covering radius (best error correction), this explains why the universe chose SU(3) -- not because of the particle content, but because of the CC.

---

### LT-5: Combinatorial Number Theory (Partitions and q-Series)

**The match**: The CC staircase is a discrete energy function E_GS(N) over integer N_pair, with energies determined by Dirac eigenvalues on SU(3). This is a partition function in the number-theoretic sense: the number of ways to distribute N pairs across 8 modes, weighted by BCS energies. The generating function Z(q) = sum_N E_GS(N) * q^N is a q-series. If the eigenvalues correlate with primes (per Connes' Addendum C), this q-series connects to modular forms.

**Why it matters**: Hardy and Ramanujan's partition function asymptotics (1918) show that p(n) ~ exp(pi * sqrt(2n/3)) / (4n*sqrt(3)). If E_GS(N) follows a similar asymptotic, the CC residual epsilon(N_eq) might be computable from the modular properties of Z(q). Mock theta functions (Ramanujan's last letter, 1920) describe partition-like functions with "errors" -- deviations from exact modularity. The CC residual might BE a mock modular form's shadow.

**Who would know**: Analytic number theorists working on partitions and modular forms (Ono, Andrews, Zagier, Bruinier). Mock modular form specialists (Zwegers, Bringmann). String theory partition function specialists (Dijkgraaf, Vafa, Gopakumar).

**What they could compute**: Compute the generating function Z(q) from the S60 staircase data {E_GS(0), E_GS(1), ..., E_GS(4)}. Test for modular or mock modular properties. If Z(q) transforms under SL(2,Z) with a specific weight, the CC residual is determined by the shadow of a mock theta function -- and Ramanujan already cataloged those in 1920.

---

### LT-6: Signal Processing / Acoustic Physics

**The match**: The substrate's eigenvalue spectrum is a signal. The spectral action is a filter applied to that signal. The zeta function's zeros are the nulls of the filtered output. The CC residual is the DC component (zero-frequency term) of the filtered signal. In signal processing, the DC component of a filtered signal depends on the filter's transfer function at omega = 0 -- which is the a_0 Seeley-DeWitt coefficient.

**Connection to Link 11**: The framework's structure is analogous to M-ary PSK (phase-shift keying) on a carrier wave -- discrete data (eigenvalues, pair numbers) modulated onto a continuous carrier (the Jensen metric flow). The "signal" looks like noise (quantum mechanics) but carries structured data (the spectral action). The CC is the residual carrier energy after demodulation -- the energy that doesn't decode into particles.

**Who would know**: Acoustic physicists working on phononic crystals and metamaterials (where band gaps are engineered from geometry). Sonar signal processing specialists who work with structured signals in noisy channels. Analog radio engineers who understand modulation residuals.

**What they could compute**: Treat the Dirac eigenvalue spectrum as a signal. Apply standard signal processing tools: power spectral density, autocorrelation function, cepstral analysis. The CC residual should appear as the DC component of the PSD. If the DC component is determined by the spectral geometry (band structure of the "phononic crystal"), the CC is a band-gap engineering problem, not a renormalization problem.
