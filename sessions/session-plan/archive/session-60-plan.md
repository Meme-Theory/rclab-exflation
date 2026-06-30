# Session 60 Plan: Executing the S59 Recommendation Stack

**Date**: 2026-03-27
**Author**: Team-lead (planner: mack-cosmic-bridge)
**Format**: Parallel single-agent computations across 8 waves
**Source**: S59 collab reviews (Volovik, Hawking, Nazarewicz, Baptista, Mack), Mack-Landau workshop, S59 results working paper
**Motivation**: S59 produced 33 gates (13 PASS, 6 FAIL, 14 INFO) and fundamentally restructured the framework's observational profile: H_0 = 68.8 km/s/Mpc from zero free parameters, w_a = 0 at 4.29-sigma projected tension with DR3, CC redirected to q-theory (Lambda_residual = 10^{113} above observation), and all superfluid screening mechanisms closed permanently. Six collaborative reviews and the Mack-Landau workshop produced 29 unique deduped computations spanning CC q-theory, timescape screening, leptogenesis, H_0 convergence, and structural diagnostics. S60 executes the entire stack. Nothing deferred.
**Results file**: `sessions/archive/session-60/session-60-results-workingpaper.md`

---

## I. Session Objective

S59 mapped the constraint surface with unprecedented precision. The CC problem is now quantified at its irreducible form (epsilon(1) = -0.046 M_KK, Lambda_residual = 4.7 x 10^{113} * Lambda_obs), and three independent descriptions (q-theory, spectral action a_0, BCS vacuum energy) converge on the same number. The S59 collab reviews identified 29 computations that can either reduce this gap, provide additional observational predictions, or close remaining escape routes. S60 fires them all.

The session is organized by priority: Wave 0 runs zero-cost diagnostics and the highest-priority CC mechanism (unimodular gravity). Wave 1 addresses the CC staircase extension and Strutinsky renormalization. Wave 2 tackles H_0 convergence and the 3D Hessian. Wave 3 handles leptogenesis and the Leggett DM abundance. Wave 4 covers timescape screening and Bekenstein truncation. Wave 5 computes structural diagnostics (Richardson-Gaudin integrals, blocking interpretation, Bayesian error budgets). Wave 6 handles the remaining thermodynamic/topological computations. Wave 7 runs the DR3 pre-registration, compound mechanism test, and remaining items.

**Pre-registered master gate**:
- **RECOMMENDATION-STACK-60**: Session-level assessment
- **PASS**: At least 2 of (UNIMOD-GRAV-60, PW-H0-CONV-60, LEPTO-CP-60) produce PASS or structurally new results
- **FAIL**: All 3 highest-priority computations produce null or negative results
- **INFO**: Exactly 1 of 3 produces a structurally new result
- **Null hypothesis**: The CC gap remains 10^{113}, H_0 convergence is non-monotone, and the Majorana sector has zero CP violation

---

## II. Wave Structure

### Dependency Graph

```
Wave 0 (ZERO-COST + UNIMODULAR GRAVITY, 3 agents, ~2 hrs):
  W0-1: A4-TRACE-60 (baptista)            [INDEPENDENT, zero-cost]
  W0-2: CC-DIM-ANALYSIS-60 (volovik)      [INDEPENDENT, zero-cost]
  W0-3: UNIMOD-GRAV-60 (baptista)         [INDEPENDENT, analytical]

  ---- Decision Point 0 ----
  ---- If UNIMOD dissolves CC: redirect W1 priorities ----
  ---- If UNIMOD fails: proceed with Strutinsky + staircase ----

Wave 1 (CC STAIRCASE + STRUTINSKY, 3 agents, ~3 hrs):
  W1-1: STAIRCASE-EXT-60 (landau)         [INDEPENDENT]
  W1-2: STRUTINSKY-PW-60 (nazarewicz)     [INDEPENDENT]
  W1-3: INTER-SECTOR-ZUBAREV-60 (volovik) [INDEPENDENT]

  ---- Decision Point 1 ----
  ---- If Strutinsky reduces gap by >10 OOM: CC route viable ----
  ---- If inter-sector equilibrates: CC gap may be 10^67 not 10^113 ----

Wave 2 (H_0 CONVERGENCE + HESSIAN, 3 agents, ~3 hrs):
  W2-1: PW-H0-CONV-60 (baptista)          [INDEPENDENT]
  W2-2: HESSIAN-3D-60 (baptista)          [INDEPENDENT, ~19 min GPU]
  W2-3: ETA-INVARIANT-60 (spectral-geometer) [INDEPENDENT]

  ---- Decision Point 2 ----
  ---- If N -> 4.00 at max(p+q)=4: H_0 prediction strengthened ----
  ---- If non-monotone: 2% residual is structural, not truncation ----

Wave 3 (LEPTOGENESIS + LEGGETT DM, 3 agents, ~3 hrs):
  W3-1: LEPTO-CP-60 (feynman)             [INDEPENDENT]
  W3-2: LEGGETT-DM-ABUND-60 (volovik)     [INDEPENDENT]
  W3-3: LEGGETT-MASS-N2-60 (landau)       [INDEPENDENT]

  ---- Decision Point 3 ----
  ---- If epsilon_1 > 10^{-6}: leptogenesis viable ----
  ---- If Omega_DM h^2 matches 0.120: DM sector complete ----

Wave 4 (SCREENING + BEKENSTEIN, 3 agents, ~3 hrs):
  W4-1: SECTOR-DIM-REDUCT-60 (baptista)   [INDEPENDENT]
  W4-2: BEKENSTEIN-PW-60 (hawking)         [INDEPENDENT]
  W4-3: ENTANGLE-CG24-60 (hawking)        [INDEPENDENT]

  ---- Decision Point 4 ----
  ---- If screening ratio > 10^4: timescape revived ----
  ---- If Bekenstein truncates PW: CC UV catastrophe resolved ----

Wave 5 (STRUCTURAL DIAGNOSTICS, 4 agents, ~3 hrs):
  W5-1: RG-INTEGRALS-60 (landau)          [INDEPENDENT]
  W5-2: BLOCKING-N3-60 (nazarewicz)       [INDEPENDENT]
  W5-3: BAYESIAN-H0-60 (nazarewicz)       [INDEPENDENT]
  W5-4: BAYESIAN-PENROSE-60 (nazarewicz)  [INDEPENDENT]

  ---- Decision Point 5 ----
  ---- If RG integrals identify specific breaking mode: CC/DM implications ----
  ---- If Bayesian H_0 error bar narrows to +/-1.0: precision prediction ----

Wave 6 (THERMODYNAMIC + TOPOLOGICAL, 4 agents, ~3 hrs):
  W6-1: TRANSPLANCKIAN-BOGO-60 (hawking)  [INDEPENDENT]
  W6-2: GH-TEMP-DW-60 (hawking)           [INDEPENDENT]
  W6-3: GSL-TIMESCAPE-60 (hawking)         [INDEPENDENT]
  W6-4: LICHNEROWICZ-DW-60 (baptista)     [INDEPENDENT]

Wave 7 (DR3 PRE-REGISTRATION + REMAINING, 4 agents, ~3 hrs):
  W7-1: DR3-PREREGISTER-60 (mack)         [INDEPENDENT]
  W7-2: COMPOUND-MECH-60 (baptista+hawking) [DEPENDS: W0-3, W4-3]
  W7-3: PENROSE-SUPERRAD-60 (hawking)     [INDEPENDENT]
  W7-4: ANDREEV-OMEGA-60 (landau)         [INDEPENDENT]
  W7-5: Q-THEORY-GEODESIC-60 (baptista)   [INDEPENDENT]
  W7-6: PAIR-TRANSFER-N4-60 (nazarewicz)  [DEPENDS: W1-1]
```

Total computations: 29 (all deduped recommendations accounted for).

---

## III. Wave 0: Zero-Cost Diagnostics + Unimodular Gravity

Three independent computations. Two are zero-cost diagnostics using existing data. One is the highest-priority analytical derivation.

### W0-1: Trace Factor Verification in a_4 (B-1)

**Agent**: baptista-spacetime-analyst (opus)

**Gate**: A4-TRACE-60

**Context**: SPINOR-NORM-59 established that dividing a_2 by dim(Delta_8) = 16 gives H_0 = 68.8 km/s/Mpc. The Baptista collab (S3.1) raised the question: does the same trace factor 16 appear in a_4, which controls the Higgs mass prediction? If the trace factor differs between a_2 and a_4 (e.g., through the Weitzenbock formula D^2 = nabla*nabla + R/4 where R/4 acts differently on different spinor components), the Higgs mass prediction shifts. If a_4/a_2 is trace-factor independent (both carry the same Tr(1)), the ratio cancels and particle physics predictions are unchanged.

**Computation steps**:

1. Load the spectral action coefficients from `computations/s59_spinor_norm.npz`. Extract a_2 and a_4 at the fold, decomposed by Peter-Weyl sector.
2. Also load `computations/s58_friedmann_derivation.npz` for the raw a_2 and a_4 values (a2_fold from canonical_constants.py).
3. Compute a_4^{(0,0)} = sum over (0,0) sector eigenvalues of lambda^4 * f_4(lambda^2/Lambda^2).
4. Compute a_4^{total} = sum over ALL sectors of dim(p,q)^2 * a_4^{(p,q)}.
5. Evaluate: N_factor_a4 = a_4^{total} / a_4^{(0,0)}. Compare to N_factor_a2 = 3.920^2 = 15.37.
6. Compute the ratio a_4/a_2 at both total and (0,0) levels. If a_4(total)/a_2(total) = a_4(0,0)/a_2(0,0), the trace factor cancels in ratios relevant to particle physics (Higgs mass ~ sqrt(f_0 * a_4 / (f_2 * a_2))).
7. Report: N_factor_a4, a_4/a_2 (total vs sector), Higgs mass prediction impact.

**Input files**:
- `computations/s59_spinor_norm.npz`
- `computations/s58_friedmann_derivation.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: N_factor_a4 = N_factor_a2 to within 5% (trace factor cancels in ratios)
- **FAIL**: N_factor_a4 differs from N_factor_a2 by > 20% (trace factor differs, Higgs prediction shifts)
- **INFO**: 5-20% difference (partial cancellation, merits investigation)

**Output files**:
- `computations/s60_a4_trace.py`
- `computations/s60_a4_trace.npz`

**Cost**: Zero (uses existing eigenvalue data).

**WINDOWS BASH BUG**: Scripts save ALL results to .npz. Verify success by checking for output files, NOT by reading Bash stdout.

---

### W0-2: Paper 14 CC Dimensional Analysis (V-5)

**Agent**: volovik-superfluid-universe-theorist (opus)

**Gate**: CC-DIM-ANALYSIS-60

**Context**: Volovik S59 collab Computation 5 proposed a zero-cost dimensional analysis check. Paper 14 (Klinkhamer-Volovik 2009) derives Lambda ~ K_QCD^3 / E_Planck^2 ~ (3 meV)^4 for the QCD case. The framework analog is Lambda ~ Delta_BCS^3 / M_Pl^2, where Delta_BCS = 0.137 M_KK is the BCS condensation energy. The Mack-Landau workshop found the EXACT Lambda_residual = |epsilon(1)| * M_KK^3 = 1.4 x 10^{66} GeV^4. This computation checks whether the Paper 14 scaling formula reproduces this number, and if not, diagnoses why.

**Computation steps**:

1. Load constants from `computations/canonical_constants.py`. Extract M_KK, M_Pl (unreduced), Delta_BCS = 0.137 M_KK.
2. Compute Lambda_Paper14 = Delta_BCS^3 / M_Pl^2. Convert to GeV^4.
3. Compute the exact residual from the Mack-Landau workshop: Lambda_exact = 0.046 * M_KK^4. Convert to GeV^4.
4. Compare: ratio = Lambda_Paper14 / Lambda_exact. If ratio ~ 1, the Paper 14 scaling applies. If ratio << 1, there is additional suppression in the 3-flavor formula. If ratio >> 1, the BCS condensation energy is not the correct scale for Delta.
5. Also compute the alternative scaling Lambda ~ Delta_BCS^4 / M_Pl^2 (quartic, from generic seesaw arguments) and Lambda ~ (Delta_BCS * M_KK)^2 / M_Pl^2 (mixed scale).
6. Report: all three scaling predictions vs exact Lambda_residual, identification of which (if any) matches, and the physical interpretation.

**Input files**:
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Paper 14 cubic scaling matches exact residual within 3 OOM
- **FAIL**: All scaling formulas disagree with exact residual by > 10 OOM
- **INFO**: One scaling formula matches within 3-10 OOM

**Output files**:
- `computations/s60_cc_dim_analysis.py`
- `computations/s60_cc_dim_analysis.npz`

**Cost**: Zero (pure dimensional analysis).

---

### W0-3: Unimodular Gravity from Fiber Integration (Workshop Q2 / Mechanism 9)

**Agent**: baptista-spacetime-analyst (opus)

**Gate**: UNIMOD-GRAV-60

**Context**: The Mack-Landau workshop rated unimodular gravity as the HIGHEST PRIORITY novel CC suppression mechanism. The argument: Jensen deformation is volume-preserving (S12 theorem). If fiber integration constrains det(g_4), the CC becomes an integration constant that does not backreact on the geometry — it dissolves all 113 OOM. The question is binary: does the volume-preserving property of the Jensen deformation propagate through the dimensional reduction to constrain det(g_4)?

The S12 theorem established: the Jensen deformation of the round SU(3) metric preserves Vol(SU(3)) at all tau. Paper 13 eq (3.41) performs fiber integration to obtain the 4D Lagrangian. In unimodular gravity (Henneaux-Teitelboim 1989), the constraint sqrt(-g) = epsilon_0 (fixed volume element) removes the CC from the equations of motion, making it an integration constant determined by initial conditions rather than by the vacuum energy.

**Computation steps**:

1. Load the spectral action framework from Baptista Papers 13-14. Identify the fiber integration formula: S_4D = integral over M^4 of [integral over K of L_12D * sqrt(g_K) d^8x_K] * sqrt(-g_4) d^4x.
2. Compute the volume element: sqrt(g_K) for the Jensen-deformed SU(3) metric g_K(tau). The S12 theorem states Vol(K) = integral sqrt(g_K) = const for all tau.
3. Derive whether the 4D effective action inherits a constraint on sqrt(-g_4). The key question: when varying S_4D with respect to g_4^{mu nu}, does the fiber volume integral constrain the variation? Specifically, if Vol(K) = const enters as a multiplicative factor in S_4D, then delta(S_4D)/delta(g_4) includes terms proportional to delta(Vol(K))/delta(g_4). If the fiber metric is dynamically coupled to the base metric through the Riemannian submersion (Paper 13 eq 1.5), then constraining Vol(K) may propagate to a constraint on det(g_4).
4. Check: does the O'Neill tensor (Paper 13 eq 1.6) or the mean curvature vector of the fiber introduce a coupling between det(g_K) and det(g_4)? If the submersion is totally geodesic (which it is NOT for the Jensen deformation — the A-tensor is nonzero), this coupling is mediated by the A-tensor and the T-tensor.
5. Evaluate whether the unimodular constraint is: (a) EXACT (the Jensen volume-preservation forces det(g_4) to be constrained, dissolving all 113 OOM), (b) APPROXIMATE (the constraint holds at leading order but is violated by A-tensor corrections, providing partial suppression), or (c) ABSENT (the fiber and base volume elements are independent, and Vol(K) = const has no implication for det(g_4)).
6. If (a) or (b): derive the effective 4D action, identify the integration constant, and estimate Lambda from initial conditions at the fold.
7. Reference: Henneaux-Teitelboim (1989) for unimodular gravity formulation. Paper 13 eqs 1.5, 3.41 for Riemannian submersion and fiber integration. S12 theorem for volume preservation.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s59_cheeger_sigma.npz` (for sigma stability at fold)

**Gate criteria**:
- **PASS**: The Jensen volume-preservation propagates to a constraint on det(g_4), making the CC an integration constant. Dissolves >= 50 OOM
- **FAIL**: The fiber and base volume elements are independent. No CC suppression from this mechanism
- **INFO**: Partial constraint (leading-order coupling through A-tensor or T-tensor), suppression < 50 OOM but > 0

**Output files**:
- `computations/s60_unimod_grav.py`
- `computations/s60_unimod_grav.npz`

**Cost**: Low-moderate (analytical derivation with numerical verification at 3-5 tau values).

---

## Decision Point 0

Review W0 results. If UNIMOD-GRAV-60 is PASS, the CC problem structure changes fundamentally — redirect W1 to explore the integration constant determination rather than the staircase extension. If FAIL, proceed with the staircase and Strutinsky route as planned.

---

## IV. Wave 1: CC Staircase Extension + Strutinsky + Inter-Sector Zubarev

Three independent CC-focused computations.

### W1-1: Lambda(N_pair) Staircase for N=3,4 (V-1 + Workshop Q1)

**Agent**: landau-condensed-matter-theorist (opus)

**Gate**: STAIRCASE-EXT-60

**Context**: The Mack-Landau workshop computed E_GS(0) = 0, E_GS(1) = -0.046 M_KK, E_GS(2) = +0.325 M_KK for the (0,0) sector. The S59 exact diagonalization data at N=3 (560 states) and N=4 (1820 states) exists from NPAIR3-INTEG-59 and THERM-ORDER-59 but those were 2-CELL computations. This computation extracts the SINGLE-CELL ground state energies E_GS(3) and E_GS(4) and extends the vacuum equation of state staircase.

**Computation steps**:

1. Load the single-cell pairing Hamiltonian from `computations/s54_ed_sweep.npz`. Extract the 8 single-particle energies eps_k and the 8x8 pairing matrix V_fold at the fold.
2. Load epsilon_canonical = 0.00374 from `computations/s59_epsilon_canonical.npz`.
3. Construct the N-pair Fock space for N=3: enumerate all C(8,3) = 56 basis states |n_1,...,n_8> with sum(n_i) = 3, n_i in {0,1}.
4. Build H_3pair = sum_k 2*eps_k * n_k - epsilon_canonical * sum_{k,l} V_{kl} * c_k^dag c_{-k}^dag c_{-l} c_l. Exact diagonalize the 56 x 56 matrix.
5. Repeat for N=4: C(8,4) = 70 basis states. Build and diagonalize the 70 x 70 Hamiltonian.
6. Record E_GS(3) and E_GS(4). Extend the staircase table:

   | N_pair | E_GS (M_KK) | mu_forward = E(N+1) - E(N) |
   |--------|-------------|---------------------------|
   | 0 | 0.000 | -0.046 |
   | 1 | -0.046 | +0.371 |
   | 2 | +0.325 | E(3) - E(2) |
   | 3 | E(3) | E(4) - E(3) |
   | 4 | E(4) | -- |

7. Compute Lambda_residual(N) = 2*E(N) - E(N-1) - E(N+1) (discrete second derivative) for N = 1, 2, 3.
8. Compute q-theory equilibrium condition: find N_eq where d(epsilon)/dN = 0 (interpolation between integers).
9. Plot E_GS(N) and Lambda_residual(N) vs N.
10. Report: full staircase, q-theory N_eq, whether Lambda_residual decreases with N.

**Input files**:
- `computations/s54_ed_sweep.npz`
- `computations/s59_epsilon_canonical.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Lambda_residual decreases monotonically with N (suggesting approach to Lambda_obs at larger N)
- **FAIL**: Lambda_residual increases or oscillates (no approach to observation)
- **INFO**: Lambda_residual decreases but gap remains > 10^{100} at N=4

**Output files**:
- `computations/s60_staircase_ext.py`
- `computations/s60_staircase_ext.npz`
- `computations/s60_staircase_ext.png`

**Cost**: Low (~5 min for 56x56 and 70x70 ED).

---

### W1-2: Strutinsky Smoothing of PW CC Extension (N-2)

**Agent**: nazarewicz-nuclear-structure-theorist (opus)

**Gate**: STRUTINSKY-PW-60

**Context**: PW-CC-59 showed Lambda_eff jumping from 0.0014 M_KK^4 at L=0 to -22.5 M_KK^4 at L=1 — a UV catastrophe from unrenormalized V. Nazarewicz S59 collab (Section 3.2) proposed Strutinsky smoothing: decompose the PW sum into E_smooth (UV background) + delta_E_shell (physically meaningful oscillation). In nuclear physics, the shell correction is typically 0.1-0.3% of total binding energy. This computation implements the Strutinsky energy theorem on the PW-extended Lambda_eff spectrum.

**Computation steps**:

1. Load the PW-extended CC data from `computations/s59_pw_cc_extension.npz`. Extract Lambda_eff^{(p,q)} for all Peter-Weyl sectors at each level L = 0, 1, 2 (or as many levels as available).
2. Load the Casimir eigenvalues C_2(p,q) = (p^2 + q^2 + p*q)/3 + p + q for each sector.
3. Implement Strutinsky smoothing: define g_smooth(E) = (1/(gamma*sqrt(2*pi))) * sum_i exp(-(E - E_i)^2 / (2*gamma^2)) where E_i are the single-particle eigenvalues and gamma is the smoothing width. Standard choice: gamma = 1.2 * d_avg, where d_avg is the average level spacing.
4. Compute E_smooth = integral of E * g_smooth(E) dE (the smooth energy from the smoothed level density).
5. Compute the shell correction: delta_E_shell = E_total - E_smooth. This is the physical CC contribution.
6. Apply the Strutinsky correction to each PW level separately: delta_Lambda(L) = Lambda_eff(L) - Lambda_smooth(L).
7. Check convergence: does delta_Lambda(L) converge as L increases, even though Lambda_eff(L) diverges?
8. Report: Lambda_smooth(L), delta_Lambda(L), convergence ratio delta_Lambda(L+1)/delta_Lambda(L).

**Input files**:
- `computations/s59_pw_cc_extension.npz`
- `computations/s54_ed_sweep.npz` (for single-cell eigenvalues)
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: delta_Lambda converges and is < 10^{-3} * Lambda_eff (Strutinsky cancellation works, reduces CC by > 3 OOM)
- **FAIL**: delta_Lambda diverges or is O(1) * Lambda_eff (no separation between smooth and oscillating)
- **INFO**: delta_Lambda converges but reduction is < 3 OOM

**Output files**:
- `computations/s60_strutinsky_pw.py`
- `computations/s60_strutinsky_pw.npz`
- `computations/s60_strutinsky_pw.png`

**Cost**: Low (~10 min for smoothing + decomposition at each PW level).

---

### W1-3: Inter-Sector Zubarev Calculation (Workshop Q1)

**Agent**: volovik-superfluid-universe-theorist (opus)

**Gate**: INTER-SECTOR-ZUBAREV-60

**Context**: ZUBAREV-CC-59 proved that thermalization within the (0,0) sector is fast (t_CC << t_universe by 8-63 orders). But the Mack-Landau workshop (Section M1, Workshop Q1) identified that inter-sector equilibration is UNPROVEN. If L >= 1 sectors do NOT equilibrate with (0,0), the CC is determined only by the (0,0) staircase (10^{67} GeV^4). If they DO equilibrate, the full PW sum contributes (10^{113} or worse). The inter-sector thermalization timescale determines which CC estimate is physical.

**Computation steps**:

1. Load the PW-extended data from `computations/s59_pw_cc_extension.npz`. Extract the sector-resolved energies for L=0 and L=1.
2. Load the Zubarev relaxation rates from `computations/s59_zubarev_cc.npz` (all 5 methods, (0,0) sector).
3. Identify the inter-sector coupling mechanism. In the spectral geometry, sectors at different PW levels couple through:
   (a) The spectral action: cross-terms a_n^{(p,q) x (p',q')} arise from products of eigenvalues in different sectors.
   (b) The Josephson coupling: E_J connects cells, and within each cell the modes from different PW sectors interact through the full D_K.
   (c) Block-diagonal theorem (S22b): [D_K]_{(p,q) x (p',q')} = 0 to machine epsilon. This means direct coupling between sectors is ZERO in the Dirac operator.
4. Evaluate: if the block-diagonal theorem implies zero direct coupling, inter-sector thermalization requires SECOND-ORDER processes (e.g., via the spectral action cross-terms or through the Josephson fabric). Compute the effective coupling: V_inter ~ a_2^{(p,q)} * a_2^{(p',q')} / a_2^{total}.
5. Estimate the inter-sector Zubarev relaxation rate: Gamma_inter ~ |V_inter|^2 * rho_0(L=1). Compare to Gamma_intra from ZUBAREV-CC-59.
6. If Gamma_inter < H_0: the sectors are dynamically decoupled, and the physical CC is the (0,0) sector result only.
7. Report: V_inter, Gamma_inter / H_0, Gamma_inter / Gamma_intra, verdict on whether the full PW sum or only the (0,0) sector contributes to the physical CC.

**Input files**:
- `computations/s59_pw_cc_extension.npz`
- `computations/s59_zubarev_cc.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Gamma_inter / H_0 > 1 (sectors equilibrate; full PW sum contributes, CC gap = 10^{113})
- **FAIL**: Gamma_inter / H_0 < 10^{-10} (sectors decoupled; CC gap reduced to (0,0) sector = 10^{67})
- **INFO**: Gamma_inter / H_0 in [10^{-10}, 1]

**Output files**:
- `computations/s60_inter_sector_zubarev.py`
- `computations/s60_inter_sector_zubarev.npz`

**Cost**: Low-moderate (~30 min analytical + numerical).

---

## Decision Point 1

Review W1 results. The Strutinsky reduction and inter-sector decoupling determine the effective CC gap. If both favor the (0,0) sector being the physical contribution with Strutinsky smoothing, the CC gap could shrink from 10^{113} to ~10^{64} — still enormous but within the landscape of known mechanisms. Update the CC constraint map before proceeding.

---

## V. Wave 2: H_0 Convergence + Spectral Action Hessian + eta-invariant

### W2-1: Peter-Weyl H_0 Convergence to max(p+q)=4 (B-2 + M-1)

**Agent**: baptista-spacetime-analyst (opus)

**Gate**: PW-H0-CONV-60

**Context**: SPINOR-NORM-59 found N_factor = 3.920 at max(p+q)=3, giving H_0 = 68.8 km/s/Mpc. The 2.0% residual from sqrt(16) = 4.00 is attributed to PW truncation. Both Mack (S3.1) and Baptista (S3.2) recommended extending to max(p+q)=4 (15 irreps, ~1456 positive modes). If N converges monotonically toward 4.00, the zero-parameter H_0 prediction strengthens. If N oscillates or saturates at 3.92, the 2% is structural and requires explanation.

**Computation steps**:

1. Load the Dirac eigenvalue computation infrastructure from the existing codebase. The code computes eigenvalues of D_K(tau) on SU(3) for each irrep (p,q) at the fold tau_fold.
2. Run the eigenvalue computation at max(p+q) = 4. This adds 5 new irreps beyond max(p+q)=3: (4,0), (3,1), (2,2), (1,3), (0,4). Each irrep has dim(p,q)^2 multiplicity.
3. Compute a_2^{(p,q)} for each new irrep using the heat kernel formula: a_2^{(p,q)} = sum over eigenvalues lambda_i of lambda_i^{-2} * dim(p,q)^2.
4. Compute a_2^{total}(L=4) = sum over all irreps at L <= 4.
5. Compute N_factor(L=4) = sqrt(a_2^{total}(L=4) / a_2^{(0,0)}).
6. Track convergence: N(L=1), N(L=2), N(L=3), N(L=4). Fit to a geometric series model N(L) = 4 - c * r^L to estimate convergence rate.
7. Compute H_0(L=4) = H_0(L=3) * N(L=3) / N(L=4). Report with truncation error estimate.
8. If computationally feasible within ~45 min, also attempt max(p+q) = 5 (adds (5,0), (4,1), (3,2), (2,3), (1,4), (0,5) — 6 more irreps).

**Input files**:
- `computations/s59_spinor_norm.npz` (contains a_2 at L=0 through L=3)
- `computations/s58_friedmann_derivation.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: |N(L=4) - 4.00| < |N(L=3) - 4.00| (monotone convergence toward sqrt(16))
- **FAIL**: N(L=4) > N(L=3) or N(L=4) < N(L=3) - 0.04 (non-monotone or divergent)
- **INFO**: Convergence confirmed but |N(L=4) - 4.00| > 0.01 (convergence slow)

**Output files**:
- `computations/s60_pw_h0_conv.py`
- `computations/s60_pw_h0_conv.npz`
- `computations/s60_pw_h0_conv.png` (N vs L plot with convergence fit)

**Cost**: Moderate. ~8.7s per eigenvalue solve x 5 new irreps x mode count ~ 20-30 min GPU.

---

### W2-2: Full 3D Spectral Action Hessian (B-3)

**Agent**: baptista-spacetime-analyst (opus)

**Gate**: HESSIAN-3D-60

**Context**: SA-EJ-ORTHOG-59 exposed that the curvature-volume proxy (used for the 3D Hessian) disagrees with the true spectral action Hessian (from eigenvalues). The 2D result (cos = 0.114) is reliable; the 3D result (cos = 0.993) is not. A genuine 3D Hessian requires Dirac eigenvalues on a 3D grid in (tau, sigma, delta_1) space. Baptista collab S3.3 estimated cost at ~125 x 9s = 19 min GPU.

**Computation steps**:

1. Define the 3D grid in the U(2)-invariant moduli space: tau in [tau_fold - 0.02, tau_fold + 0.02] (5 points), sigma in [-0.01, +0.01] (5 points), delta_1 in [-0.01, +0.01] (5 points). Total: 125 grid points.
2. At each grid point, compute the Dirac eigenvalues of D_K(tau, sigma, delta_1) at max(p+q)=3. Note: sigma and delta_1 break the U(2) Jensen symmetry.
3. Compute the spectral action S(tau, sigma, delta_1) = sum over eigenvalues of f(lambda^2/Lambda^2) at each grid point.
4. Compute the 3x3 Hessian matrix H_{ij} = d^2 S / dq_i dq_j using finite differences (q = tau, sigma, delta_1). Use central differences: H_{ij} = (S(q+e_i+e_j) - S(q+e_i-e_j) - S(q-e_i+e_j) + S(q-e_i-e_j)) / (4*dq_i*dq_j).
5. Diagonalize H. Report eigenvalues and eigenvectors.
6. Compute the angle between the Hessian eigenvectors and the energy-Josephson (EJ) basis vectors. Compare to the 2D result (cos = 0.114, near-orthogonal).
7. Identify whether ANY mixed direction (tau-sigma, tau-delta_1, sigma-delta_1) is unstable (negative Hessian eigenvalue). If so, the fold position in the full 3D moduli space may differ from the Jensen line.

**Input files**:
- `computations/s59_sa_ej_orthog.npz` (2D Hessian baseline)
- `computations/s59_cheeger_sigma.npz` (sigma stability)
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: All 3 Hessian eigenvalues positive. Fold is a local minimum in full 3D space.
- **FAIL**: One or more negative eigenvalues. Fold is a saddle point, and the true minimum is off-Jensen.
- **INFO**: All positive but one eigenvalue < 10% of largest (flat direction exists).

**Output files**:
- `computations/s60_hessian_3d.py`
- `computations/s60_hessian_3d.npz`
- `computations/s60_hessian_3d.png` (contour plots in 2D slices)

**Cost**: Moderate (~125 x 9s = 19 min GPU).

---

### W2-3: eta-Invariant of D_K at Fold (Workshop Q6)

**Agent**: spectral-geometer (opus)

**Gate**: ETA-INVARIANT-60

**Context**: The Mack-Landau workshop listed the APS eta-invariant as one of the 14 novel CC suppression mechanisms (Mechanism 5). The eta-invariant eta(D_K) = sum over eigenvalues of sign(lambda) * |lambda|^{-s} at s=0 measures the spectral asymmetry of the Dirac operator. For a BDI system at the fold boundary, a nonzero eta-invariant would indicate a topological anomaly that modifies the effective action. In the APS index theorem, the boundary contribution to the index is (1/2)(eta(D_boundary) + dim(ker D_boundary)). If eta(D_K) is nonzero at the fold, it contributes to the effective CC through the topological boundary term.

**Computation steps**:

1. Load the full Dirac spectrum at the fold from `computations/s59_spinor_norm.npz` or the underlying eigenvalue data.
2. The eta function is eta(s) = sum_lambda sign(lambda) * |lambda|^{-s}. For the numerical computation, this is a zeta-function regularization: compute eta(s) for several values of s > dim/2 (convergent regime), then analytically continue to s = 0.
3. Numerically: compute partial sums eta_N(s) = sum_{|lambda| < Lambda_N} sign(lambda) * |lambda|^{-s} for increasing cutoffs Lambda_N. Extrapolate to Lambda_N -> infinity using the known asymptotic expansion.
4. Cross-check: for a compact Riemannian manifold with a self-adjoint Dirac operator, the eta-invariant is related to the spectral asymmetry N_+ - N_- where N_+/- count positive/negative eigenvalues. For a BDI system with T^2 = +1, the spectrum is symmetric under lambda -> -lambda (from J-symmetry), which should give eta = 0 exactly. Verify this.
5. If eta = 0 (as J-symmetry predicts): mechanism 5 is closed. Report the precision of the cancellation.
6. If eta != 0: check whether J-symmetry is broken at the fold. This would be a new structural result.
7. Also compute: the spectral flow of D_K(tau) from tau = 0 to tau_fold. Each zero-crossing of an eigenvalue changes the eta-invariant by +/-2. The total spectral flow gives the number of eigenvalue crossings.

**Input files**:
- `computations/s59_spinor_norm.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: eta != 0 at the fold (topological anomaly contributes to CC)
- **FAIL**: eta = 0 to machine precision (J-symmetry enforces; mechanism 5 closed)
- **INFO**: eta computation inconclusive due to convergence issues

**Output files**:
- `computations/s60_eta_invariant.py`
- `computations/s60_eta_invariant.npz`

**Cost**: Low (~10 min, uses existing eigenvalues).

---

## Decision Point 2

Review W2 results. The H_0 convergence result determines whether the zero-parameter prediction strengthens. The 3D Hessian determines whether the fold is a true local minimum or merely a saddle point along the Jensen line. The eta-invariant tests whether a topological boundary term contributes to the CC. Update observational constraint map.

---

## VI. Wave 3: Leptogenesis + Leggett DM + Leggett Mass

### W3-1: Majorana Leptogenesis from B3 Sector (V-4 + M-5)

**Agent**: feynman-theorist (opus)

**Gate**: LEPTO-CP-60

**Context**: BARYON-DIAGNOSTIC-59 proved eta_B = 0 from the BCS sector (BDI T-symmetry, three independent proofs). The only escape is Majorana leptogenesis through the B3 = (0,3) sector. M_R ~ 7.3 x 10^{16} GeV exceeds the Davidson-Ibarra bound by 7 orders. The key question: does the Majorana mass matrix M_R constructed from B3 eigenstates have complex entries producing nonzero CP violation (epsilon_1 > 10^{-6})?

The Mack-Landau workshop (M4, M4-Q) identified the structural question: the BDI classification forces real Yukawa couplings in the D_K sector, but D_F (the finite Dirac operator in Connes' spectral triple) is NOT constrained by [J, D_K] = 0. The Majorana mass enters through D_F, not D_K.

**Computation steps**:

1. Load the B3 = (0,3) sector eigenvalues from the Dirac spectrum data at the fold. Extract the 6 B3 eigenvalues.
2. Construct the Majorana mass matrix M_R. In the NCG framework (Chamseddine-Connes-Marcolli), M_R enters through the finite Dirac operator D_F on the internal space F = M_2(H) + M_4(C). The Majorana mass is the off-diagonal block connecting the right-handed neutrino to its charge conjugate.
3. Check whether the NCG axioms (first-order condition, J-reality, chirality) permit complex entries in M_R. Specifically: J_F D_F J_F^{-1} = D_F (reality) and [[D_F, a], b^0] = 0 (first-order) constrain the form of M_R. In the standard CCM model, M_R is a symmetric matrix that CAN have complex entries (the phases are physical CP-violating parameters).
4. If complex entries are permitted: construct M_R from the B3 eigenvalues. The simplest ansatz is M_R_ij = lambda_B3_i * delta_ij + off_diag_ij, where the off-diagonal elements are determined by the mixing between B3 modes.
5. Compute the Jarlskog invariant J = Im(M_R_12 * M_R_23 * M_R_31^*). If J != 0, CP violation exists.
6. Compute the Davidson-Ibarra CP asymmetry parameter: epsilon_1 = -(3/(16*pi)) * sum_{j!=1} Im[(M_R^dag M_R)_{1j}^2] * f(M_j^2/M_1^2) / ((M_R^dag M_R)_{11} * M_1).
7. Propagate through sphaleron processing: eta_B = (28/79) * epsilon_1 * kappa / g_*, where kappa is the washout efficiency (strong washout for M_R >> 10^{12} GeV gives kappa ~ 10^{-3}).
8. Compare eta_B to observation: (6.12 +/- 0.04) x 10^{-10} (Planck 2018).
9. Also check: is the baryon-to-DM ratio Omega_b/Omega_DM = 0.185 consistent with the predicted eta_B and the Leggett DM abundance?

**Input files**:
- `computations/s59_baryon_diagnostic.npz`
- `computations/s54_ed_sweep.npz` (Dirac spectrum)
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: epsilon_1 > 10^{-6} and eta_B within 2 OOM of 6 x 10^{-10}
- **FAIL**: M_R is forced to be real by NCG axioms (epsilon_1 = 0 exact)
- **INFO**: M_R can be complex but epsilon_1 < 10^{-6} or eta_B > 2 OOM from observation

**Output files**:
- `computations/s60_lepto_cp.py`
- `computations/s60_lepto_cp.npz`

**Cost**: Moderate (~1 hr, analytical + numerical construction of M_R).

---

### W3-2: Leggett Mode Cosmological Abundance (V-3)

**Agent**: volovik-superfluid-universe-theorist (opus)

**Gate**: LEGGETT-DM-ABUND-60

**Context**: f_DM-DEPLETION-59 proved f_DM(z=0) = 1.000 within the substrate (only Leggett survives). But the total Omega_DM h^2 depends on the absolute Leggett number density and mass. EPSILON-CANONICAL-59 gives omega_L = 0.049 M_KK (corrected), and the squeezing parameters from the transit are in `s59_epsilon_canonical.npz`. The S59 corrected f_DM(B) = 0.365 at transit needs to be propagated through standard cosmological relic abundance equations.

**Computation steps**:

1. Load the Leggett mode parameters from `computations/s59_epsilon_canonical.npz`: omega_L (gap), E_L_exc (excitation energy per cell), f_DM(B) at transit.
2. Load the Bogoliubov squeezing parameters from `computations/s59_bogoliubov_coeff.npz`: |beta_k|^2 = 0.273 (universal).
3. Compute the total Leggett energy at the moment of transit: E_L_total = N_cells * E_L_exc, where N_cells = 32 (CG(24) + 8 boundary cells).
4. Convert to physical energy density: rho_L(z_shat) = E_L_total * M_KK / V_cell, where V_cell = 1/M_KK^3 gives rho_L = E_L_total * M_KK^4.
5. Propagate to z = 0 using non-relativistic matter redshifting: rho_L(z=0) = rho_L(z_shat) * (1 + z_shat)^{-3} / (1 + z_shat)^{-3} (both scale as a^{-3}, so the ratio rho_L/rho_c is preserved if rho_c also scales appropriately).
6. Compute Omega_DM h^2 = rho_L(z=0) / rho_c(z=0), where rho_c = 3 H_0^2 / (8 pi G). Use H_0 = 68.8 km/s/Mpc.
7. Compare to Planck: Omega_DM h^2 = 0.1186 +/- 0.0020.
8. Also compute: the Leggett gravitational decay lifetime Gamma ~ m_L^3 / M_Pl^2 (from Mack S59 collab Section 5, Q5). Report tau_DM = 1/Gamma in years and compare to t_universe = 1.38 x 10^{10} yr.

**Input files**:
- `computations/s59_epsilon_canonical.npz`
- `computations/s59_bogoliubov_coeff.npz`
- `computations/s59_fdm_depletion.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Omega_DM h^2 within factor 3 of 0.120 AND tau_DM > 100 * t_universe
- **FAIL**: Omega_DM h^2 > 10 * 0.120 (overclosure) OR tau_DM < t_universe (DM decays)
- **INFO**: Omega_DM h^2 within factor 3-10 of 0.120 OR tau_DM in [1, 100] * t_universe

**Output files**:
- `computations/s60_leggett_dm_abund.py`
- `computations/s60_leggett_dm_abund.npz`

**Cost**: Low (~30 min).

---

### W3-3: Leggett Mode Mass at N_pair = 2 (Workshop Q7)

**Agent**: landau-condensed-matter-theorist (opus)

**Gate**: LEGGETT-MASS-N2-60

**Context**: The Mack-Landau workshop noted that the 4.5% thermal admixture at N_pair = 2 (from the Boltzmann factor exp(-0.371/0.135) = 0.064 at T_GGE) affects the Leggett mode mass at the percent level. Workshop Q7 asks: what is m_L(2) - m_L(1)? This determines the DM mass variation from thermal fluctuations and bounds the precision of the DM mass prediction.

**Computation steps**:

1. Load the single-cell BCS data from `computations/s54_ed_sweep.npz` and `computations/s56_leggett_fabric.npz`.
2. At N_pair = 1: the Leggett mode is the collective pair vibration. Its mass is omega_L(1) = 0.049 M_KK (from EPSILON-CANONICAL-59).
3. At N_pair = 2: construct the 2-pair BCS Hamiltonian in the 28-dimensional C(8,2) Fock space. Diagonalize to get E_GS(2) = +0.325 M_KK (from workshop staircase).
4. Compute the Leggett mode at N=2: this is the lowest-energy pair vibration above the N=2 ground state. In the pair-vibration formalism, it is the state with Delta_N = 0 (pair number conserved) and the quantum number corresponding to relative pair oscillation.
5. The Leggett frequency at N=2 is omega_L(2) = E_first_excited(N=2) - E_GS(N=2), where the first excited state has the same N_pair and parity but different pair configuration.
6. Compute the mass shift: delta_m_L = omega_L(2) - omega_L(1). Report in M_KK units and as a fractional change.
7. Compute the thermally averaged mass: <m_L> = m_L(1) * P(N=1) + m_L(2) * P(N=2), where P(N=1) = 1/(1 + exp(-0.371/T_GGE)) and P(N=2) = 1 - P(N=1).
8. Report: omega_L(1), omega_L(2), delta_m_L, <m_L>, fractional width.

**Input files**:
- `computations/s54_ed_sweep.npz`
- `computations/s56_leggett_fabric.npz`
- `computations/s59_epsilon_canonical.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: |delta_m_L/m_L| < 10% (DM mass prediction robust to N_pair fluctuations)
- **FAIL**: |delta_m_L/m_L| > 50% (DM mass strongly N_pair-dependent, prediction unreliable)
- **INFO**: |delta_m_L/m_L| in [10%, 50%]

**Output files**:
- `computations/s60_leggett_mass_n2.py`
- `computations/s60_leggett_mass_n2.npz`

**Cost**: Low (~15 min for 28x28 ED plus excited states).

---

## Decision Point 3

Review W3 results. If leptogenesis produces epsilon_1 > 10^{-6} AND Omega_DM h^2 is within range, the matter sector (baryons + DM) is self-consistent with zero free parameters. If the Leggett gravitational decay lifetime is short, this constrains indirect DM detection signals.

---

## VII. Wave 4: Screening + Bekenstein + Entanglement

### W4-1: Sector-Resolved Dimensional Reduction for Screening (B-6 + Workshop Q4)

**Agent**: baptista-spacetime-analyst (opus)

**Gate**: SECTOR-DIM-REDUCT-60

**Context**: The Mack-Landau workshop permanently closed ALL superfluid screening mechanisms. The only surviving screening route is GEOMETRIC: the Riemannian submersion structure of Paper 13 eq 1.5 might separate the tau-dependence of G_eff (which controls the lapse through a_2(total)) from the tau-dependence of alpha (which depends on g_1/g_2 = e^{-2*tau}). The screening ratio is currently 99.1/4 = 24.8x, but the required ratio is 10^4. Baptista collab S3.6 proposed that the (M_KK/M_Pl)^2 suppression factor from the fiber integration measure might provide the additional factor.

**Computation steps**:

1. Load the Riemannian submersion structure from Paper 13. The O'Neill formula (eq 1.5) decomposes the total scalar curvature: R_P = R_{M^4} + R_K - (1/4)|F|^2 - |T|^2.
2. The 4D Friedmann equation comes from the variation of S_4D = integral R_{M^4} * sqrt(-g_4) d^4x + correction terms from R_K, |F|^2, |T|^2.
3. Compute: how does spatial delta_tau enter each term? R_{M^4} depends on the base metric (no direct tau-dependence). R_K = R_K(tau) depends on the fiber metric. |F|^2 depends on the gauge field strength (which couples to both tau and the base metric).
4. The lapse function N in the ADM decomposition satisfies N^2 = 1/(16*pi*G_eff * rho), where G_eff = 1/(16*pi*a_2). Compute delta_N/N from delta_tau.
5. The fine structure constant is alpha = g_1^2/(4*pi), where g_1/g_2 = e^{-2*tau}. Compute delta_alpha/alpha from delta_tau.
6. The screening ratio is: (delta_N/N) / (delta_alpha/alpha). Include the fiber integration measure explicitly: the 4D projected G_eff involves an integral over K of (some kernel involving a_2 and the fiber volume form), while alpha involves a point evaluation on the root lattice.
7. Compute the effective screening ratio including the (M_KK/M_Pl)^2 = 2.4 x 10^{-6} suppression factor. Determine whether this enters the alpha channel, the G channel, or neither.
8. Report: screening ratio (with and without fiber integration corrections), whether the 10^4 threshold can be met, and if so, the resulting delta_alpha/alpha and delta_G/G for sigma_tau = 0.0053.

**Input files**:
- `computations/s59_timescape_wa.npz`
- `computations/s59_spinor_norm.npz` (sector-resolved a_2)
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Screening ratio > 10^4 (timescape mechanism survives: lapse varies while alpha constrained)
- **FAIL**: Screening ratio < 100 (no viable decoupling)
- **INFO**: Screening ratio in [100, 10^4] (partial screening, some tension remains)

**Output files**:
- `computations/s60_sector_dim_reduct.py`
- `computations/s60_sector_dim_reduct.npz`

**Cost**: Moderate (~1 hr analytical + numerical).

---

### W4-2: Bekenstein Bound on PW Sectors (H-A)

**Agent**: hawking-theorist (opus)

**Gate**: BEKENSTEIN-PW-60

**Context**: Hawking S59 collab Section 3A proposed applying the Bekenstein entropy bound S_max = 2*pi*R*E to each PW sector. Higher-Casimir representations have larger energies; if confined to a region of size ~1/M_KK, their entropy may SATURATE the Bekenstein bound. Sectors that saturate cannot contribute independently to the CC. This could provide a physical truncation that selects the (0,0) sector.

**Computation steps**:

1. Load the PW-extended CC data from `computations/s59_pw_cc_extension.npz`. Extract E_BCS(p,q) and mode counts for each sector.
2. For each sector (p,q) at level L: compute S_Bekenstein = 2*pi*R_KK * |E_BCS(p,q)|, where R_KK = 1/M_KK.
3. Compute S_vN of the BCS ground state in each sector. For the (0,0) sector, S_vN is available from `computations/s59_page_curve.npz`. For higher sectors, estimate S_vN ~ N_modes * S_single_mode where S_single_mode = -v^2 ln(v^2) - u^2 ln(u^2).
4. Compare: if S_vN(p,q) > S_Bekenstein(p,q) for L >= 1, those sectors are Bekenstein-saturated.
5. If sectors are saturated: their contribution to the CC should be absorbed into the area-entropy of the confining region, not counted as independent vacuum energy. Compute the effective Lambda_eff using only unsaturated sectors.
6. Report: S_vN vs S_Bekenstein for each sector, list of saturated sectors, Lambda_eff with truncation.

**Input files**:
- `computations/s59_pw_cc_extension.npz`
- `computations/s59_page_curve.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: L >= 1 sectors are Bekenstein-saturated; truncation reduces CC by > 10 OOM
- **FAIL**: No sectors are saturated (S_vN << S_Bekenstein everywhere)
- **INFO**: Some sectors saturated but reduction < 10 OOM

**Output files**:
- `computations/s60_bekenstein_pw.py`
- `computations/s60_bekenstein_pw.npz`

**Cost**: Low (~30 min).

---

### W4-3: Entanglement-Area Law on CG(24) Graph (H-B + Workshop Q3)

**Agent**: hawking-theorist (opus)

**Gate**: ENTANGLE-CG24-60

**Context**: Workshop Mechanism 12 estimated ~62 OOM suppression from entanglement-area law, with a 50 OOM gap remaining. Hawking S59 collab Section 3B proposed computing the quantum extremal surface on the CG(24) graph using the island formula. The 4-cell Page curve data (S_ent(k=1) = 1.201 nats) provides a baseline. The CG(24) graph has 24 vertices and 72 edges; the question is whether a quantum extremal surface exists that separates "gravitating" from "non-gravitating" vacuum energy.

**Computation steps**:

1. Load the 4-cell Page curve data from `computations/s59_page_curve.npz`. Extract S_ent(k) for k = 1, 2.
2. Define the generalized entropy functional on subgraphs of CG(24): S_gen(Sigma) = |dSigma|/(4*G_eff) + S_bulk(inside Sigma), where |dSigma| is the number of severed edges and G_eff = 1/(16*pi*a_2) with a_2 from the fold.
3. For the Josephson fabric: define "area" of a graph cut as the number of severed Josephson bonds, each contributing 1/E_J to the gravitational term. So A/(4G) -> |dSigma| / (4*G_eff * E_J^{-1}).
4. Systematically enumerate all bipartitions of the CG(24) graph (or a representative subset — the full enumeration of 2^{24} partitions requires heuristic sampling). For each bipartition, compute S_gen.
5. Identify the minimum-S_gen partition (the quantum extremal surface). If S_gen_min < S_gen_trivial (trivial = no partition), a non-trivial extremal surface exists.
6. If a quantum extremal surface exists: compute the entanglement entropy suppression factor for the CC. The island formula gives Lambda_eff_physical = Lambda_eff_bulk * exp(-S_ent_boundary / S_ent_bulk).
7. Also compute the topological entanglement entropy S_topo from the PAGE-CURVE-59 area-law fit.
8. Report: S_gen_min, the extremal surface topology, Lambda suppression factor, comparison to the 62 OOM estimate from the workshop.

**Input files**:
- `computations/s59_page_curve.npz`
- `computations/s59_josephson_phase.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Nontrivial quantum extremal surface exists; Lambda suppression > 50 OOM
- **FAIL**: No nontrivial extremal surface (S_gen monotone with partition size)
- **INFO**: Extremal surface exists but suppression < 50 OOM

**Output files**:
- `computations/s60_entangle_cg24.py`
- `computations/s60_entangle_cg24.npz`
- `computations/s60_entangle_cg24.png`

**Cost**: Moderate (~1-2 hrs for graph enumeration + entropy computation).

---

## Decision Point 4

Review W4 results. If the screening ratio exceeds 10^4 (W4-1), the timescape mechanism is revived and the w_a prediction changes. If Bekenstein truncation works (W4-2), the CC UV catastrophe is resolved and the effective CC is the (0,0) sector value. If the entanglement area law provides significant suppression (W4-3), it may combine with other mechanisms for the compound test in W7-2.

---

## VIII. Wave 5: Structural Diagnostics

Four independent diagnostics testing structural properties of the BCS system and error budgets.

### W5-1: Richardson-Gaudin Integrals as Explicit Diagnostics (N-4)

**Agent**: landau-condensed-matter-theorist (opus)

**Gate**: RG-INTEGRALS-60

**Context**: Nazarewicz S59 collab Section 3.4 proposed computing the Richardson-Gaudin conserved integrals explicitly for the 2-cell system. The framework repeatedly invokes "8 RG integrals" but has never computed them. The mode-resolved commutator ||[H_full, R_k]||/||H_full|| identifies which specific modes break integrability and which remain conserved. This is superior to the global <r> statistic.

**Computation steps**:

1. Load the 2-cell BCS Hamiltonian from `computations/s58_npair2_integ.npz`. Extract the single-particle energies, pairing matrix V_fold, and Josephson coupling.
2. Construct the Richardson-Gaudin integrals for the separable part of V_fold. The RG integrals are: R_k = S_k^z + sum_{k' != k} [S_k^+ S_{k'}^- + S_k^- S_{k'}^+ + 2 S_k^z S_{k'}^z] / (2*epsilon_k - 2*epsilon_{k'}), where S_k^z = (n_k - 1/2)/2, S_k^+ = c_k^dag c_{-k}^dag, S_k^- = c_{-k} c_k.
3. For each k = 0, ..., 7 (the 8 single-particle modes per cell): compute R_k as a matrix in the 2-cell Fock space.
4. Compute the commutator [H_full, R_k] for each k. H_full includes the non-separable part of V_fold and the Josephson coupling.
5. Compute the normalized breaking measure: delta_k = ||[H_full, R_k]|| / ||H_full|| for each mode k.
6. Rank the modes by delta_k. Identify which modes are approximately conserved (delta_k < 0.01) and which are broken (delta_k > 0.1).
7. Determine whether the dominant integrability-breaking comes from: (a) the non-separable fraction of V_fold (intra-cell), or (b) the Josephson coupling (inter-cell).
8. Report: delta_k for all 16 modes (8 per cell), ranking, identification of breaking source.

**Input files**:
- `computations/s58_npair2_integ.npz`
- `computations/s54_ed_sweep.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Dominant breaking from Josephson (inter-cell) — separable intra-cell integrals approximately conserved
- **FAIL**: All integrals strongly broken (delta_k > 0.1 for all k) — no residual integrability
- **INFO**: Mixed (some modes conserved, some broken, no clear pattern)

**Output files**:
- `computations/s60_rg_integrals.py`
- `computations/s60_rg_integrals.npz`
- `computations/s60_rg_integrals.png` (bar chart of delta_k by mode)

**Cost**: Moderate (~1 hr for Fock-space matrix construction and commutator computation).

---

### W5-2: Nuclear Blocking Interpretation of N_pair = 3 Minimum (N-3)

**Agent**: nazarewicz-nuclear-structure-theorist (opus)

**Gate**: BLOCKING-N3-60

**Context**: The non-monotonic <r> sequence (0.442, 0.412, 0.419 for N=2,3,4) has a minimum at N=3. Nazarewicz S59 collab Section 3.3 proposed a nuclear blocking interpretation: at N=3 in 8 modes (37.5% filling), blocking is near-maximal. The odd-even staggering Delta_OES = S_2(N) - S_2(N+1) should have a minimum at N=3 if blocking dominates.

**Computation steps**:

1. Load the ED ground states from `computations/s59_npair3_integ.npz` (N=3 data) and `computations/s59_therm_order.npz` (N=4 data). Also load N=2 from `computations/s58_npair2_integ.npz`.
2. Extract the canonical-basis occupation numbers v_k^2 = <n_k> from the ground state eigenvectors at N = 1, 2, 3, 4.
3. Compute the BCS gap from odd-even staggering: Delta_OES(N) = (-1)^N * [E(N+1) - 2*E(N) + E(N-1)] / 2. Use E_GS values from the staircase (W1-1 will provide E(3), E(4); use Mack-Landau workshop values for E(0), E(1), E(2)).
4. Compute the blocking parameter: b(N) = sum_k (v_k^2 - 1/2)^2 / N_modes. This measures the departure from half-filling of individual orbitals. Blocking is maximal when b(N) is minimal (all orbitals partially filled).
5. Plot v_k^2 vs k at each N. Identify the Fermi surface position and whether it sharpens or broadens with N.
6. Check: does Delta_OES have a minimum at N=3? Does b(N) have a minimum at N=3? If both do, the blocking interpretation is confirmed.
7. Report: v_k^2(N) for all N, Delta_OES(N), b(N), identification of whether blocking or interaction dominates.

**Input files**:
- `computations/s59_npair3_integ.npz`
- `computations/s59_therm_order.npz`
- `computations/s58_npair2_integ.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Delta_OES minimum at N=3, confirming blocking dominance
- **FAIL**: Delta_OES minimum at N != 3 (blocking interpretation fails)
- **INFO**: Delta_OES minimum at N=3 but b(N) does not follow (mixed physics)

**Output files**:
- `computations/s60_blocking_n3.py`
- `computations/s60_blocking_n3.npz`
- `computations/s60_blocking_n3.png`

**Cost**: Low (~30 min using existing eigenvectors).

---

### W5-3: Bayesian Error Budget for H_0 (N-1)

**Agent**: nazarewicz-nuclear-structure-theorist (opus)

**Gate**: BAYESIAN-H0-60

**Context**: H_0 = 68.8 has zero free parameters but also zero formal error bars. Nazarewicz S59 collab Section 3.1 proposed the methodology from Paper 06 (Bayesian inference for nuclear DFT): define a model space (PW truncation level L, Jensen deformation tau, cutoff function choice), assign priors, compute posterior on H_0. DEPENDS ON W2-1 output for L=4 data; if W2-1 is not yet available, use L=0 through L=3 data only.

**Computation steps**:

1. Load the sector decomposition data from `computations/s59_spinor_norm.npz`: a_2(L) for L = 0, 1, 2, 3.
2. If W2-1 (PW-H0-CONV-60) data is available, also load a_2(L=4).
3. Define the model space:
   - PW truncation level L: data at L = 0, 1, 2, 3 (and 4 if available)
   - Jensen deformation tau: fold value tau_fold +/- uncertainty from CHEEGER-SIGMA-59 (sigma stiffness)
   - Cutoff function f: the spectral action depends on the choice of test function f(x). Use the standard step function + 2 alternative smooth cutoffs.
4. For each (L, tau, f) combination, compute H_0.
5. Define priors: uniform on L (truncation is geometric, not random), Gaussian on tau centered at tau_fold with width from sigma stiffness, uniform on f choices.
6. Compute the posterior distribution P(H_0 | data) using Bayesian model averaging (Paper 06 eq. 15).
7. Extract: H_0_median, 68% credible interval, 95% credible interval.
8. Report: H_0 = XX +/- YY (truncation) +/- ZZ (tau) +/- WW (cutoff).

**Input files**:
- `computations/s59_spinor_norm.npz`
- `computations/s59_cheeger_sigma.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: 68% credible interval includes Planck H_0 = 67.36 (framework consistent)
- **FAIL**: 95% credible interval excludes Planck H_0 (framework in > 2-sigma tension)
- **INFO**: 68% interval excludes Planck but 95% includes it (mild tension)

**Output files**:
- `computations/s60_bayesian_h0.py`
- `computations/s60_bayesian_h0.npz`
- `computations/s60_bayesian_h0.png` (posterior distribution of H_0)

**Cost**: Low (~30 min).

---

### W5-4: Bayesian Error Propagation for Penrose Threshold (N-6)

**Agent**: nazarewicz-nuclear-structure-theorist (opus)

**Gate**: BAYESIAN-PENROSE-60

**Context**: PENROSE-ACCESS-59 reports alpha_total = 0.555, only 6.1% above threshold alpha_crit = 0.523, with the overlap parameter omega = 0.70 as a modeling choice. Nazarewicz S59 collab Section 3.6 proposed a Bayesian analysis: define a prior on omega (uniform on [0.3, 1.0]) and propagate through the combination formula to get P(alpha_total > alpha_crit).

**Computation steps**:

1. Load the Penrose access data from `computations/s59_penrose_access.npz`: alpha_mp (multi-pair contribution), alpha_Andreev (inter-cell contribution), combination formula alpha_total(omega).
2. Define the prior on omega: uniform on [0.3, 1.0] (reflecting "both channels feed B3 but degree uncertain").
3. Sample omega from the prior (N = 10,000 samples). For each omega, compute alpha_total = alpha_mp + omega * alpha_Andreev (or whatever the combination formula is in the S59 computation).
4. Compute P(alpha_total > alpha_crit) = fraction of samples where alpha_total > 0.523.
5. Compute the posterior on alpha_total: median, 68% CI, 95% CI.
6. Identify the critical omega: omega_crit where alpha_total = alpha_crit. Report P(omega > omega_crit).
7. If P(alpha_total > alpha_crit) > 0.95: the PASS is robust. If P ~ 0.60: the PASS is fragile.

**Input files**:
- `computations/s59_penrose_access.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: P(alpha_total > alpha_crit) > 0.90
- **FAIL**: P(alpha_total > alpha_crit) < 0.50
- **INFO**: P in [0.50, 0.90]

**Output files**:
- `computations/s60_bayesian_penrose.py`
- `computations/s60_bayesian_penrose.npz`
- `computations/s60_bayesian_penrose.png` (posterior on alpha_total with threshold)

**Cost**: Zero (Monte Carlo on existing parameters).

---

## Decision Point 5

Review W5 results. The RG integrals identify which modes break integrability (informing future CC/screening work). The Bayesian H_0 error bar turns the prediction from a number into a measurement. The Penrose Bayesian analysis determines the CC chain's weakest link robustness.

---

## IX. Wave 6: Thermodynamic + Topological Diagnostics

### W6-1: Trans-Planckian Check on Bogoliubov Coefficients (H-C)

**Agent**: hawking-theorist (opus)

**Gate**: TRANSPLANCKIAN-BOGO-60

**Context**: Hawking S59 collab Section 3C proposed extending the trans-Planckian check from TRANSPLANCKIAN-46 (B2 exactly invariant) to the full 8-mode spectrum. The question: are the Bogoliubov coefficients |beta_k|^2 = 0.273 (universal, sudden-quench) sensitive to UV modification of the dispersion relation at the KK scale?

**Computation steps**:

1. Load the baseline Bogoliubov data from `computations/s59_bogoliubov_coeff.npz`: |beta_k|^2 for all 8 modes.
2. Define the modified dispersion: omega(k) = omega_0 * tanh(k/k_KK), where k_KK = M_KK. This is the standard trans-Planckian regulator that saturates at the KK scale.
3. Also test two alternative modifications: (a) Unruh's modified dispersion omega = c * k * (1 - k^2/k_KK^2)^{1/2}, and (b) Corley-Jacobson superluminal: omega = c * k * (1 + k^2/k_KK^2)^{1/2}.
4. Recompute |beta_k|^2 using each modified dispersion. The mode equation is: d^2 phi_k / d(tau)^2 + omega_modified(k, tau)^2 * phi_k = 0, with the same tau-dependent background as the original computation.
5. Compare: delta_beta_k = |beta_k(modified) - beta_k(standard)| / beta_k(standard) for each mode and each modification.
6. Report: delta_beta_k for all modes and modifications. If delta_beta < 10^{-3} for all modes, the sudden-quench universality is UV-robust.

**Input files**:
- `computations/s59_bogoliubov_coeff.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: delta_beta_k < 1% for all modes and all modifications (UV-robust)
- **FAIL**: delta_beta_k > 10% for any mode (UV-sensitive, sudden quench not universal)
- **INFO**: delta_beta_k in [1%, 10%] (mild UV sensitivity)

**Output files**:
- `computations/s60_transplanckian_bogo.py`
- `computations/s60_transplanckian_bogo.npz`

**Cost**: Low (~30 min).

---

### W6-2: Gibbons-Hawking Temperature at Domain Wall (H-D)

**Agent**: hawking-theorist (opus)

**Gate**: GH-TEMP-DW-60

**Context**: Hawking S59 collab Section 3D proposed computing the Euclidean periodicity at tau_DW = 0.113, where sectional curvature changes sign. A conical singularity in the Wick-rotated geometry would define a Gibbons-Hawking temperature T_DW = 1/(2*pi*R_cone). This introduces a new physical scale.

**Computation steps**:

1. Load the domain wall curvature data from `computations/s59_ricci_dw.npz`. Extract K_sec^min(tau) and all curvature components.
2. At tau_DW = 0.113, identify the plane with K_sec = 0 (the first plane to develop negative curvature).
3. Compute the surface gravity analog: kappa = sqrt(|dK_sec/dtau|) at K_sec = 0. This is the "acceleration" experienced by a geodesic crossing the curvature sign boundary.
4. The Euclidean periodicity is beta = 2*pi/kappa. The GH temperature is T_DW = 1/beta = kappa/(2*pi).
5. Convert T_DW to M_KK units and to GeV.
6. Compare T_DW to: T_GGE = 0.135 M_KK, T_acoustic = 0.112 M_KK, and the BCS gap Delta = 0.137 M_KK.
7. If T_DW ~ T_GGE: the domain wall is in thermal equilibrium with the GGE. If T_DW << T_GGE: the wall is effectively cold. If T_DW >> T_GGE: the wall is a hot spot.
8. Check whether the conical singularity exists at all: if the Euclidean geometry is smooth at tau_DW (no conical deficit), T_DW is undefined and the mechanism is closed.

**Input files**:
- `computations/s59_ricci_dw.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: T_DW is well-defined and comparable to T_GGE (new thermal scale)
- **FAIL**: No conical singularity at tau_DW (smooth Euclidean geometry)
- **INFO**: T_DW defined but >> or << T_GGE

**Output files**:
- `computations/s60_gh_temp_dw.py`
- `computations/s60_gh_temp_dw.npz`

**Cost**: Low (~20 min).

---

### W6-3: GSL Check on Timescape Mechanism (H-E)

**Agent**: hawking-theorist (opus)

**Gate**: GSL-TIMESCAPE-60

**Context**: Hawking S59 collab Section 3E proposed a GSL (generalized second law) check on the timescape mechanism before declaring it dead. If G varies spatially by 53%, A/(4G) varies enormously across the fabric. The GSL may provide a tighter constraint than observational bounds.

**Computation steps**:

1. Load the timescape data from `computations/s59_timescape_wa.npz`: sigma_tau = 0.00530, frac_da2 = 99.1, delta_G/G = -0.53.
2. Compute S_gen(void) = S_matter(void) + A_H(void)/(4*G(void)). For the void region: G(void) = G_0 * (1 + delta_G/G * (tau_void - tau_mean)/sigma_tau).
3. Compute S_gen(wall) similarly with tau_wall.
4. The GSL requires: S_gen(wall) + S_gen(void) >= S_gen(uniform) where S_gen(uniform) uses the spatially averaged G = G_0.
5. Evaluate: is the GSL violated? If so, the timescape mechanism is thermodynamically forbidden, not merely observationally excluded.
6. Also compute: the entropy production rate dS_gen/dt in the timescape configuration. If dS_gen/dt < 0, the second law is violated dynamically.
7. Report: S_gen(void), S_gen(wall), S_gen(uniform), GSL violation (if any), entropy production rate.

**Input files**:
- `computations/s59_timescape_wa.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: GSL violated — timescape mechanism thermodynamically forbidden (provides independent closure)
- **FAIL**: GSL satisfied — timescape is thermodynamically consistent (no additional closure from GSL)
- **INFO**: GSL marginally satisfied/violated within numerical precision

**Output files**:
- `computations/s60_gsl_timescape.py`
- `computations/s60_gsl_timescape.npz`

**Cost**: Low (~20 min).

---

### W6-4: Lichnerowicz Eigenvalue Tracking at Domain Wall (B-4)

**Agent**: baptista-spacetime-analyst (opus)

**Gate**: LICHNEROWICZ-DW-60

**Context**: Baptista S59 collab S3.4 proposed tracking all 31 Lichnerowicz TT eigenvalues through tau_DW with fine resolution (Delta_tau = 0.001). The domain wall energy crossing aligns with the sectional curvature sign change. The Berger inequality bounds volumes of manifolds with positive curvature; at tau_DW these constraints relax. Paper 28 (Lauret Stability I) eq 3.11 connects Lichnerowicz eigenvalues to sectional curvatures. A specific eigenvalue crossing at tau_DW would explain the domain wall.

**Computation steps**:

1. Load the Lichnerowicz eigenvalue code. Set up a fine tau grid: tau in [tau_DW - 0.02, tau_DW + 0.02] with Delta_tau = 0.001 (41 points).
2. At each tau, compute all 31 Lichnerowicz TT eigenvalues of the Jensen-deformed SU(3) metric.
3. Track each eigenvalue continuously through the grid. Use adiabatic continuity to avoid crossing identification errors.
4. Check: does any eigenvalue cross zero at tau_DW? Does any have an inflection point?
5. Compute the Lichnerowicz gap: lambda_min(tau) = min over all TT eigenvalues. Plot vs tau.
6. If a zero-crossing exists: identify the TT tensor mode responsible and its symmetry properties. This mode would be the domain wall's "soft mode."
7. Report: all eigenvalue trajectories, zero-crossings, inflection points, and identification of the DW-triggering mode.

**Input files**:
- `computations/s59_ricci_dw.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: A specific Lichnerowicz eigenvalue crosses zero at tau_DW (explains the domain wall)
- **FAIL**: All eigenvalues remain positive through tau_DW (no soft mode, DW unexplained)
- **INFO**: An eigenvalue has a minimum near tau_DW but does not cross zero

**Output files**:
- `computations/s60_lichnerowicz_dw.py`
- `computations/s60_lichnerowicz_dw.npz`
- `computations/s60_lichnerowicz_dw.png` (eigenvalue trajectories through tau_DW)

**Cost**: Moderate (~30 min for 41 tau points x eigenvalue computation).

---

## X. Wave 7: DR3 Pre-Registration + Remaining Computations

Six computations covering observational forecasting, compound mechanisms, and remaining items.

### W7-1: DESI DR3 Scenario Pre-Registration (M-2)

**Agent**: mack-cosmic-bridge (opus)

**Gate**: DR3-PREREGISTER-60

**Context**: Mack S59 collab Section 3.2 proposed pre-registering a CPL forecast for three DR3 scenarios before data arrives. This makes the adjudication automatic when DR3 is released. P(DR3 excludes w_a = 0 at 3-sigma) = 87% from WA-ERROR-PROP-59.

**Computation steps**:

1. Load the framework predictions from `computations/s59_wa_error_prop.npz` (w_0, w_a, projected DR3 errors) and `computations/s59_obs_discriminant.npz` (BAO D_V, f*sigma_8).
2. Load GROWTH-FACTOR-59 data from `computations/s59_growth_factor.npz` (f*sigma_8(z) at 6 redshift bins).
3. Define three DR3 scenarios:

   **Scenario A**: DR3 confirms w_a ~ -0.7 at 3-sigma (dynamical DE confirmed).
   - Both LCDM (w_a = 0) and framework face exclusion.
   - Pre-register: framework-DESI tension in (w_0, w_a), framework-LCDM tension (now academic), BAO D_V prediction (which is conditional on surviving w_a).

   **Scenario B**: DR3 softens to w_a ~ -0.3 +/- 0.2 (systematic partially identified).
   - Framework tension drops to ~2-sigma.
   - Pre-register: BAO D_V discriminant at DR3 precision, f*sigma_8 per-bin chi2 at DR3+Euclid.

   **Scenario C**: DR3 finds w_a consistent with 0 (systematic identified or statistical fluctuation).
   - Framework vindicated. LCDM also vindicated.
   - Pre-register: BAO D_V at Euclid precision (5.7-sigma), sigma_8 = 0.793 vs LCDM 0.811.

4. For each scenario: compute the specific framework predictions for BAO D_V(z) at z = 0.3, 0.5, 0.7, 1.0, 1.5, 2.0 using the w_0 = -0.918 equation of state; f*sigma_8(z) at the same redshifts; sigma_8(z=0); and the 2D contour overlap in (w_0, w_a) with the DR3 posterior under that scenario.
5. Pre-register the decision rule: "If DR3 central value w_a < -0.530, the framework is excluded at 3-sigma. If w_a > -0.35, the framework is consistent at 2-sigma. If w_a in [-0.530, -0.350], the framework is in tension but not excluded."
6. Plot the three-scenario forecast panel.

**Input files**:
- `computations/s59_wa_error_prop.npz`
- `computations/s59_obs_discriminant.npz`
- `computations/s59_growth_factor.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Pre-registration complete with specific numerical predictions for all 3 scenarios
- **FAIL**: Cannot compute predictions (missing inputs or inconsistency)
- **INFO**: Partial pre-registration (not all scenarios covered)

**Output files**:
- `computations/s60_dr3_preregister.py`
- `computations/s60_dr3_preregister.npz`
- `computations/s60_dr3_preregister.png` (three-panel forecast)

**Cost**: Low (~45 min).

---

### W7-2: Compound Mechanism Test: Unimodular + Entanglement (Workshop Q8)

**Agent**: baptista-spacetime-analyst (opus)

**Gate**: COMPOUND-MECH-60

**Context**: Workshop Q8 asked whether Mechanisms 9 (unimodular gravity) and 12 (entanglement-area law) can be combined for additional CC suppression. This computation tests the compound mechanism using outputs from W0-3 and W4-3.

**DEPENDS ON**: W0-3 (UNIMOD-GRAV-60) and W4-3 (ENTANGLE-CG24-60).

**Computation steps**:

1. Load results from W0-3 (unimodular gravity): does the Jensen volume-preservation propagate to det(g_4)?
2. Load results from W4-3 (entanglement-area law): what is the Lambda suppression factor from the quantum extremal surface?
3. If both provide suppression:
   - Compute the compound suppression: total OOM reduction = OOM(unimod) + OOM(entangle).
   - Check whether the mechanisms are independent (multiplicative) or interfere (sub-multiplicative).
   - The compound test is: if unimodular gravity makes the CC an integration constant of magnitude M_KK^4, and the entanglement area law then constrains that constant through the Bekenstein bound, the net CC could be Lambda ~ M_KK^4 * exp(-S_ent) where S_ent ~ 62 OOM gives Lambda ~ 10^{66-62} = 10^4 GeV^4. Still 51 OOM above observation but structurally different.
4. If one or both mechanisms produce FAIL: report the compound as FAIL with the specific failure modes.
5. Evaluate: what is the minimal additional suppression needed after the compound mechanism? How many OOM remain?

**Input files**:
- `computations/s60_unimod_grav.npz` (from W0-3)
- `computations/s60_entangle_cg24.npz` (from W4-3)
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Compound suppression > 80 OOM (CC gap reduced to < 10^{33})
- **FAIL**: Compound suppression < 10 OOM or mechanisms interfere destructively
- **INFO**: Compound suppression in [10, 80] OOM

**Output files**:
- `computations/s60_compound_mech.py`
- `computations/s60_compound_mech.npz`

**Cost**: Low (~30 min, analytical combination of prior results).

---

### W7-3: Penrose Process — Superradiance Analogy (H-F)

**Agent**: hawking-theorist (opus)

**Gate**: PENROSE-SUPERRAD-60

**Context**: Hawking S59 collab Section 3F proposed computing the superradiance condition: which B2 modes can extract energy from the B3 "ergosphere"? The Hessian eigenvalue lambda_min = -15.60 at alpha_total sets the depth of the negative-energy region. This computation identifies the specific modes responsible for the Penrose transfer, independent of the overlap parameter omega.

**Computation steps**:

1. Load the Penrose access data from `computations/s59_penrose_access.npz`: alpha_mp, alpha_Andreev, Hessian eigenvalues.
2. Compute the effective energy in the B3 frame: E_eff(k) = E_k - q_7(k) * Phi_7, where q_7(k) is the K_7 charge of mode k and Phi_7 is the chemical potential conjugate to K_7.
3. Identify modes where E_eff < 0 (the analog of the ergosphere region).
4. For each negative-energy mode: compute the superradiance extraction rate Gamma_SR ~ |V_{B2-B3}|^2 * rho_B3 * Theta(omega - m*Omega_H_analog).
5. Sum over all superradiant modes to get the total CC reduction rate: dLambda/dt = sum_k Gamma_SR(k) * |E_eff(k)|.
6. Compare: this extraction rate is independent of omega. If dLambda/dt * t_universe > Lambda_eff, the Penrose process can significantly reduce the CC.
7. Report: list of superradiant modes, E_eff(k), Gamma_SR(k), total extraction rate.

**Input files**:
- `computations/s59_penrose_access.npz`
- `computations/s54_ed_sweep.npz` (B3 spectrum)
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: Total extraction rate * t_universe > Lambda_eff (Penrose process can reduce CC)
- **FAIL**: Total extraction rate * t_universe << Lambda_eff (Penrose process negligible)
- **INFO**: Extraction rate non-negligible but insufficient by itself

**Output files**:
- `computations/s60_penrose_superrad.py`
- `computations/s60_penrose_superrad.npz`

**Cost**: Low (~30 min).

---

### W7-4: Andreev Overlap Parameter from Joint Spectral Statistics (V-2)

**Agent**: landau-condensed-matter-theorist (opus)

**Gate**: ANDREEV-OMEGA-60

**Context**: Volovik S59 collab Computation 2 proposed deriving the overlap parameter omega from joint spectral statistics, rather than treating it as a modeling parameter. The CC chain's conditional PASS at omega = 0.70 (PENROSE-ACCESS-59) is the weakest link. This computation constructs H = H_RG + alpha_mp * V_mp + alpha_A * V_A and sweeps the 2D parameter space to determine whether the channels add (omega ~ 1), interfere (omega ~ 0), or are partially independent (omega ~ 0.5-0.7).

**Computation steps**:

1. Load the multi-pair sector data from `computations/s59_npair3_integ.npz` (V_fold non-separable part) and `computations/s56_fabric_integ.npz` (anisotropic Josephson).
2. Construct H(alpha_mp, alpha_A) = H_RG + alpha_mp * V_mp + alpha_A * V_A.
   - H_RG: the integrable Richardson-Gaudin Hamiltonian (separable V_fold part).
   - V_mp: the non-separable part of V_fold (intra-cell integrability breaking).
   - V_A: the anisotropic Josephson coupling (inter-cell breaking).
3. Sweep the 2D grid: alpha_mp in [0, 1], alpha_A in [0, 1], with 20 x 20 = 400 points.
4. At each point, exact-diagonalize H (use N_pair = 2 Fock space, dim = 120 for 2-cell) and compute <r>_even.
5. Map the <r>(alpha_mp, alpha_A) surface. Identify:
   - The physical point: alpha_mp = 1, alpha_A = 1.
   - The isolines <r> = 0.523 (Penrose threshold).
   - Whether the surface is convex (additive, omega ~ 1) or concave (sub-additive, omega < 1).
6. Extract omega from the surface: omega = [alpha_total(joint) - alpha_mp] / alpha_A at the physical point.
7. Report: the derived omega, its uncertainty from the grid resolution, and P(alpha_total > alpha_crit).

**Input files**:
- `computations/s59_npair3_integ.npz`
- `computations/s56_fabric_integ.npz`
- `computations/s58_npair2_integ.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: omega > 0.52 (Penrose PASS confirmed from first principles)
- **FAIL**: omega < 0.40 (Penrose chain breaks, CC chain at risk)
- **INFO**: omega in [0.40, 0.52] (marginal, Penrose verdict uncertain)

**Output files**:
- `computations/s60_andreev_omega.py`
- `computations/s60_andreev_omega.npz`
- `computations/s60_andreev_omega.png` (2D <r> surface with isolines)

**Cost**: Moderate (~2 hrs for 400 x 120-dim ED).

---

### W7-5: q-Theory Geodesic Winding Interpretation (B-5)

**Agent**: baptista-spacetime-analyst (opus)

**Gate**: Q-THEORY-GEODESIC-60

**Context**: Baptista S59 collab S3.5 proposed exploring whether N_pair can be interpreted as a geometric charge — the number of geodesic windings in the fiber. Paper 16 eq (1.2) gives d(m^2)/ds = -(d_A g_K)(p_V, p_V), connecting mass variation to the covariant derivative of the internal metric. If the BCS pairing interaction can be rewritten as a geodesic energy, q-theory connects directly to KK geometry.

**Computation steps**:

1. Load the fiber connection coefficients from existing geometry data. The covariant derivative d_A g_K at the fold.
2. Evaluate d_A g_K along the BCS pairing direction: identify the tangent vector in the fiber corresponding to the pair creation operator S_k^+.
3. Compute the mass variation: d(m^2)/ds = -(d_A g_K)(p_V, p_V), where p_V is the projection of the pairing momentum onto the fiber tangent space.
4. Check: does d(m^2)/ds have a natural quantization in terms of N_pair? If the geodesic energy is E_geod = N * d(m^2)/ds * L_geod, where L_geod is the geodesic length, then N_pair = E_BCS / (d(m^2)/ds * L_geod) should be integer.
5. Compute L_geod for the closed geodesic in the SU(3) fiber that wraps along the pairing direction.
6. Report: d(m^2)/ds, L_geod, whether N_pair has a geodesic winding interpretation.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s59_q_variable.npz`

**Gate criteria**:
- **PASS**: N_pair = E_BCS / (geodesic energy quantum) to within 10% (winding interpretation confirmed)
- **FAIL**: No correspondence between BCS energy levels and geodesic quantization
- **INFO**: Qualitative correspondence but > 10% numerical discrepancy

**Output files**:
- `computations/s60_q_theory_geodesic.py`
- `computations/s60_q_theory_geodesic.npz`

**Cost**: Low-moderate (~1 hr, mostly algebraic).

---

### W7-6: Pair Transfer Matrix Elements S_+(k) for N=1,2,3,4 (N-5 + Workshop Q5)

**Agent**: nazarewicz-nuclear-structure-theorist (opus)

**Gate**: PAIR-TRANSFER-N4-60

**Context**: The Mack-Landau workshop computed S_+(1) = 1.013 for the single-cell system. This computation extends to the 2-cell system at N=1,2,3,4, including Josephson coupling. The 2-cell S_+(1) may differ qualitatively from the 1-cell result (the workshop flagged this). Also computes the pair-removal amplitudes S_-(N) for the CC diagnostic (whether N_pair can change permanently).

**DEPENDS ON**: W1-1 (STAIRCASE-EXT-60) for E_GS(3), E_GS(4) single-cell values.

**Computation steps**:

1. Load the 2-cell ED data from `computations/s58_npair2_integ.npz` (N=2 ground state, 120-dim Fock space).
2. Load the N=3 and N=4 2-cell ground states from `computations/s59_npair3_integ.npz` and `computations/s59_therm_order.npz`.
3. Construct the pair-addition operator P^+ = sum_k S_k^+ for cell 0 (or cell 1).
4. For N = 1 -> 2: compute S_+(1) = sum_k |<N=2,GS|S_k^+|N=1,GS>|^2 in the 2-cell Fock space.
5. Repeat for N = 2 -> 3 and N = 3 -> 4.
6. Also compute the pair-removal S_-(N) = sum_k |<N-1,GS|S_k^-|N,GS>|^2 for N = 1, 2, 3, 4.
7. Compare the 2-cell S_+(1) to the workshop's 1-cell result (1.013). Does the Josephson coupling modify S_+?
8. Report: S_+(N) and S_-(N) for all N, comparison between 1-cell and 2-cell, implications for CC self-tuning timescale.

**Input files**:
- `computations/s58_npair2_integ.npz`
- `computations/s59_npair3_integ.npz`
- `computations/s59_therm_order.npz`
- `computations/canonical_constants.py`

**Gate criteria**:
- **PASS**: 2-cell S_+(1) within factor 2 of 1-cell result (Josephson does not qualitatively change pair transfer)
- **FAIL**: 2-cell S_+(1) < 0.01 (Josephson suppresses pair transfer — changes CC dynamics)
- **INFO**: 2-cell S_+(1) > 2 (Josephson enhances pair transfer)

**Output files**:
- `computations/s60_pair_transfer_n4.py`
- `computations/s60_pair_transfer_n4.npz`
- `computations/s60_pair_transfer_n4.png` (S_+ and S_- vs N)

**Cost**: Moderate (~1 hr, requires 2-cell ED at multiple N).

---

## XI. Constraint Gates Summary

| Gate ID | Wave | Agent | PASS Criterion | FAIL Criterion |
|:--------|:-----|:------|:--------------|:---------------|
| A4-TRACE-60 | W0 | baptista | N_a4 = N_a2 within 5% | > 20% difference |
| CC-DIM-ANALYSIS-60 | W0 | volovik | Paper 14 scaling within 3 OOM | All scalings > 10 OOM off |
| UNIMOD-GRAV-60 | W0 | baptista | CC dissolved (>= 50 OOM) | No propagation to det(g_4) |
| STAIRCASE-EXT-60 | W1 | landau | Lambda_res decreasing with N | Increasing or oscillating |
| STRUTINSKY-PW-60 | W1 | nazarewicz | Shell correction < 10^{-3} * total | No separation |
| INTER-SECTOR-ZUBAREV-60 | W1 | volovik | Gamma_inter/H_0 > 1 | Gamma_inter/H_0 < 10^{-10} |
| PW-H0-CONV-60 | W2 | baptista | N(L=4) closer to 4.00 | Non-monotone |
| HESSIAN-3D-60 | W2 | baptista | All eigenvalues positive | Negative eigenvalue |
| ETA-INVARIANT-60 | W2 | spectral-geometer | eta != 0 | eta = 0 to machine eps |
| LEPTO-CP-60 | W3 | feynman | epsilon_1 > 10^{-6} | M_R forced real |
| LEGGETT-DM-ABUND-60 | W3 | volovik | Omega_DM h^2 within 3x of 0.120 | Overclosure or DM decays |
| LEGGETT-MASS-N2-60 | W3 | landau | |delta_m/m| < 10% | |delta_m/m| > 50% |
| SECTOR-DIM-REDUCT-60 | W4 | baptista | Screening ratio > 10^4 | < 100 |
| BEKENSTEIN-PW-60 | W4 | hawking | L >= 1 saturated, > 10 OOM | No saturation |
| ENTANGLE-CG24-60 | W4 | hawking | QES exists, > 50 OOM | No QES |
| RG-INTEGRALS-60 | W5 | landau | Josephson dominates breaking | All strongly broken |
| BLOCKING-N3-60 | W5 | nazarewicz | OES minimum at N=3 | Minimum at N != 3 |
| BAYESIAN-H0-60 | W5 | nazarewicz | 68% CI includes Planck | 95% CI excludes Planck |
| BAYESIAN-PENROSE-60 | W5 | nazarewicz | P(alpha > alpha_c) > 0.90 | P < 0.50 |
| TRANSPLANCKIAN-BOGO-60 | W6 | hawking | delta_beta < 1% | delta_beta > 10% |
| GH-TEMP-DW-60 | W6 | hawking | T_DW well-defined, ~ T_GGE | No conical singularity |
| GSL-TIMESCAPE-60 | W6 | hawking | GSL violated | GSL satisfied |
| LICHNEROWICZ-DW-60 | W6 | baptista | Zero-crossing at tau_DW | All positive |
| DR3-PREREGISTER-60 | W7 | mack | All 3 scenarios computed | Cannot compute |
| COMPOUND-MECH-60 | W7 | baptista | > 80 OOM combined | < 10 OOM |
| PENROSE-SUPERRAD-60 | W7 | hawking | Extraction rate * t > Lambda | Negligible |
| ANDREEV-OMEGA-60 | W7 | landau | omega > 0.52 | omega < 0.40 |
| Q-THEORY-GEODESIC-60 | W7 | baptista | Winding interpretation within 10% | No correspondence |
| PAIR-TRANSFER-N4-60 | W7 | nazarewicz | 2-cell S_+(1) ~ 1-cell | S_+(1) << 0.01 |

---

## XII. Decision Points Summary

| After Wave | Key Question | Outcome A | Outcome B |
|:-----------|:-------------|:----------|:----------|
| W0 | Does unimodular gravity dissolve CC? | Redirect W1 to integration constant | Proceed with staircase + Strutinsky |
| W1 | Strutinsky + inter-sector: how big is CC gap? | Gap shrinks by >10 OOM | Gap unchanged at 10^{113} |
| W2 | H_0 convergence + fold stability | N -> 4.00 (strengthens H_0) | Non-monotone (structural residual) |
| W3 | Matter sector self-consistent? | Leptogenesis + DM abundance match | CP violation zero or DM overcloses |
| W4 | Screening + truncation viable? | w_a prediction updated | Timescape dead, PW catastrophe real |
| W5 | Error budgets quantified? | H_0 = 68.8 +/- 1.4, Penrose robust | Large uncertainties or fragile Penrose |

---

## XIII. Execution Notes

### Agent Assignments (deduplication accounting)

| Agent | Computations | Wave(s) |
|:------|:------------|:--------|
| baptista-spacetime-analyst | W0-1, W0-3, W2-1, W2-2, W4-1, W6-4, W7-2, W7-5 | 0, 2, 4, 6, 7 |
| volovik-superfluid-universe-theorist | W0-2, W1-3, W3-2 | 0, 1, 3 |
| landau-condensed-matter-theorist | W1-1, W3-3, W5-1, W7-4 | 1, 3, 5, 7 |
| nazarewicz-nuclear-structure-theorist | W1-2, W5-2, W5-3, W5-4, W7-6 | 1, 5, 7 |
| hawking-theorist | W4-2, W4-3, W6-1, W6-2, W6-3, W7-3 | 4, 6, 7 |
| feynman-theorist | W3-1 | 3 |
| spectral-geometer | W2-3 | 2 |
| mack-cosmic-bridge | W7-1 | 7 |

### Batch Sizing

- Max 3-4 agents per parallel sub-batch (per project rules).
- W0: 3 agents (2 baptista + 1 volovik). Note: two baptista computations in W0. W0-1 is zero-cost (5 min), W0-3 is analytical (1 hr). Run W0-1 first, then W0-3 in sequence on the same baptista spawn, or use a second baptista spawn.
- W1: 3 agents (landau, nazarewicz, volovik).
- W2: 3 agents (2 baptista, spectral-geometer). Same baptista note — W2-1 is GPU-heavy (~30 min), W2-2 is GPU-heavy (~19 min). Sequence on same spawn or use 2 spawns.
- W3: 3 agents (feynman, volovik, landau).
- W4: 3 agents (2 baptista, 2 hawking). Sub-batch: 2 hawking + 1 baptista, then 1 baptista.
- W5: 4 agents (landau, 3 nazarewicz). Sub-batch: 3 nazarewicz (W5-2, W5-3, W5-4 are all low-cost) + 1 landau.
- W6: 4 agents (3 hawking, 1 baptista). Sub-batch: 3 hawking + 1 baptista.
- W7: Sub-batch A: mack + baptista (W7-1, W7-2), Sub-batch B: hawking + landau (W7-3, W7-4), Sub-batch C: baptista + nazarewicz (W7-5, W7-6).

### Runtime Estimates

| Wave | Estimated Time | Limiting Factor |
|:-----|:--------------|:----------------|
| W0 | 2 hrs | W0-3 analytical derivation |
| W1 | 3 hrs | W1-2 Strutinsky smoothing |
| W2 | 3 hrs | W2-1/W2-2 GPU eigenvalue computations |
| W3 | 3 hrs | W3-1 Majorana sector construction |
| W4 | 3 hrs | W4-3 CG(24) graph enumeration |
| W5 | 3 hrs | W5-1 Fock-space commutator computation |
| W6 | 2 hrs | All low-cost |
| W7 | 3 hrs | W7-4 400-point 2D sweep |

Total estimated wall time: ~22 hrs (8 sequential waves). Effective compute time: ~8-10 hrs (parallelism within waves).

### File Conventions

- All scripts: prefix `s60_`, located in `computations/`.
- All scripts import from `canonical_constants.py`.
- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`.
- All agents use opus model.
- Output: .npz (data), .py (script), .png (plots where specified).
- WINDOWS BASH BUG: Verify by checking output files, not stdout.

### Deduplication Map (29 unique from context package)

| # | Context Label | Gate ID | Wave | Agent |
|:--|:-------------|:--------|:-----|:------|
| 1 | V-1 + Workshop Q1 (E(3),E(4)) | STAIRCASE-EXT-60 | W1 | landau |
| 2 | V-2 (Andreev omega) | ANDREEV-OMEGA-60 | W7 | landau |
| 3 | V-3 (Leggett DM abundance) | LEGGETT-DM-ABUND-60 | W3 | volovik |
| 4 | V-4 + M-5 (Majorana lepto) | LEPTO-CP-60 | W3 | feynman |
| 5 | V-5 (Paper 14 dim analysis) | CC-DIM-ANALYSIS-60 | W0 | volovik |
| 6 | H-A (Bekenstein PW) | BEKENSTEIN-PW-60 | W4 | hawking |
| 7 | H-B + Workshop Q3 (entanglement CG24) | ENTANGLE-CG24-60 | W4 | hawking |
| 8 | H-C (trans-Planckian Bogo) | TRANSPLANCKIAN-BOGO-60 | W6 | hawking |
| 9 | H-D (GH temp at DW) | GH-TEMP-DW-60 | W6 | hawking |
| 10 | H-E (GSL timescape) | GSL-TIMESCAPE-60 | W6 | hawking |
| 11 | H-F (Penrose superradiance) | PENROSE-SUPERRAD-60 | W7 | hawking |
| 12 | N-1 (Bayesian H_0) | BAYESIAN-H0-60 | W5 | nazarewicz |
| 13 | N-2 (Strutinsky PW) | STRUTINSKY-PW-60 | W1 | nazarewicz |
| 14 | N-3 (blocking N=3) | BLOCKING-N3-60 | W5 | nazarewicz |
| 15 | N-4 (RG integrals) | RG-INTEGRALS-60 | W5 | landau |
| 16 | N-5 + Workshop Q5 (pair transfer) | PAIR-TRANSFER-N4-60 | W7 | nazarewicz |
| 17 | N-6 (Bayesian Penrose) | BAYESIAN-PENROSE-60 | W5 | nazarewicz |
| 18 | B-1 (a_4 trace) | A4-TRACE-60 | W0 | baptista |
| 19 | B-2 + M-1 (PW to L=4) | PW-H0-CONV-60 | W2 | baptista |
| 20 | B-3 (3D Hessian) | HESSIAN-3D-60 | W2 | baptista |
| 21 | B-4 (Lichnerowicz DW) | LICHNEROWICZ-DW-60 | W6 | baptista |
| 22 | B-5 (q-theory geodesic) | Q-THEORY-GEODESIC-60 | W7 | baptista |
| 23 | B-6 + Workshop Q4 (sector dim reduct) | SECTOR-DIM-REDUCT-60 | W4 | baptista |
| 24 | M-2 (DR3 pre-register) | DR3-PREREGISTER-60 | W7 | mack |
| 25 | Workshop Q2 (inter-sector Zubarev) | INTER-SECTOR-ZUBAREV-60 | W1 | volovik |
| 26 | Workshop Q6 (eta-invariant) | ETA-INVARIANT-60 | W2 | spectral-geom |
| 27 | Workshop Q7 (Leggett mass N=2) | LEGGETT-MASS-N2-60 | W3 | landau |
| 28 | Workshop Q8 (compound mechanism) | COMPOUND-MECH-60 | W7 | baptista |
| 29 | Workshop Q2-unimod (unimodular gravity) | UNIMOD-GRAV-60 | W0 | baptista |

All 29 deduped computations accounted for. None deferred.

### GW Background Note (M-4)

Mack collab item M-4 (GW background) was identified as already permanently closed by STOCHASTIC-GW-59 FAIL (f_peak = 1.86e7 Hz, inaccessible). No new computation needed. This is recorded as a permanent closure, not a deferred item.

### N_eff Precision (M-3)

Mack collab item M-3 (N_eff precision improvement) is addressed implicitly by W3-2 (LEGGETT-DM-ABUND-60), which computes the full relic abundance including the Leggett mode's contribution at BBN and its effect on N_eff at the precision level. The existing NEFF-BA-59 gave Delta_N_eff = 0.027 for g_BA = 1 Goldstone; the Leggett mode is non-relativistic at BBN and contributes zero additional N_eff (as Mack verified in S59 collab Section 3.3). No separate computation needed beyond W3-2.
