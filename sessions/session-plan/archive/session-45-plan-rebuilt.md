# Session 45 REBUILT: q-Theory, DM/DE, and the n_s Crisis

**Date**: 2026-03-15
**Author**: Team-lead (rebuilt from S44 master synthesis after W1 FAIL-FAIL)
**Format**: Parallel single-agent computations across 6 waves
**Source**: S44 master synthesis (VII. Priority-Ordered Next Steps), S44 Sagan assessment, S44 Section VI (fine-tuning question), W1 results (OCC-SPEC-45 FAIL, KZ-NS-45 FAIL)
**Results file**: `sessions/session-45/session-45-results-workingpaper.md`

---

## 0. Why the Original Plan Was Wrong

The original S45 plan elevated OCC-SPEC-45 (1/7 convergence, Connes alone) to co-lynchpin alongside KZ-NS-45, centering the session on the spectral action framework. Seven of seven S44 reviewers said the spectral action is exhausted for tau-stabilization and wrong for the CC. The S44 master synthesis listed q-theory as "#1, the single most important open computation" with 5/7 convergence. The original plan buried q-theory in W2-3 and built 7 of 29 tasks around the spectral action.

OCC-SPEC-45 failed predictably: bandwidth increases monotonically → Delta decreases monotonically → n_k decreases monotonically → S_occ decreases monotonically. BCS mean-field smoothing erases van Hove spikes. This was foreseeable from S37 + S38 results.

KZ-NS-45 failed as Landau predicted: n_s = -0.588 (370 sigma from Planck). The |beta_k|^2 ~ k^{-5.55} decay from the BCS gap overwhelms the d_k^2 ~ k^{+3.97} degeneracy growth. The k-mapping ambiguity (n_s spans -0.59 to +5.69) reveals a structural problem: the framework does not uniquely determine how internal KK quantum numbers map to 4D cosmological wavenumbers.

Both session-defining gates FAIL. Per Sagan's pre-registered matrix: P → 3-8%.

This rebuilt plan is derived from what S44 actually recommended.

---

## I. Session Objective (Rebuilt)

Session 45 now asks: **Does q-theory self-tune the CC on this specific system, and can the non-equilibrium GGE explain DM/DE?**

These were the #1 and #2 priorities from S44's master synthesis (5/7 and 3-5/7 convergence). The old plan buried them.

Secondary objective: **Is there a scale selection principle that rescues the spectral dimension route to n_s?** (DIMFLOW-44 found n_s = 0.961 at sigma = 1.10, but sigma is unfixed. With all three dynamical n_s routes now closed — epsilon_H, Lifshitz eta, Bogoliubov — sigma selection is the sole survivor.)

Tertiary: **Does the unexpanded spectral action (before polynomial expansion) naturally produce the f_4/f_2 ~ 10^{-121} hierarchy?** (3/7 convergence from Einstein, SP, Tesla. Section VI centerpiece. Never in the original plan.)

---

## II. Wave Structure

### W1 already complete (sunk cost — valid boundaries)

- OCC-SPEC-45: **FAIL** (monotone, 28th equilibrium closure)
- KZ-NS-45: **FAIL** (n_s = -0.588, third n_s closure)
- Cross-checks: Einstein ENDORSED KZ-NS FAIL (k-mapping structurally ill-defined). Nazarewicz rejected by user (not run).

### NEW Wave 1-R: q-THEORY + FRESH OCC-SPEC (LANDAU)

```
WAVE 1-R (2 tasks -- parallel)
  W1-R1: Q-THEORY-KK-45    [CC: q-theory self-tuning on corrected discrete KK tower]
  W1-R2: OCC-SPEC-45-LANDAU [tau-stab: Landau free energy approach, INDEPENDENT of Connes computation]
         |
         v
     DECISION POINT R1
         |
         v
WAVE 2-R (3 parallel -- DM/DE + CC alternatives)
  W2-R1: ALPHA-EFF-45       [DM/DE: non-eq specific heat from 8-temp GGE]
  W2-R2: UNEXPANDED-SA-45   [CC: full non-polynomial Tr f(D^2/Lambda^2)]
  W2-R3: ANALYTIC-TORSION-45 [CC: Ray-Singer torsion on SU(3)]
         |
         v
WAVE 3-R (4 parallel -- n_s crisis + tensions)
  W3-R1: SIGMA-SELECT-45    [n_s: scale selection for spectral dimension]
  W3-R2: MKK-TENSION-45     [resolve 0.83-decade M_KK tension]
  W3-R3: ECOND-RECONCILE-45 [resolve 0.115 vs 0.137 E_cond]
  W3-R4: DOS-FINE-SCAN-45   [van Hove fine structure at tau=0.19-0.21]
         |
         v
WAVE 4-R (5 parallel -- specialist, S44 recommendations)
  W4-R1: RUNNING-GN-45      [G_N(tau) across transit]
  W4-R2: EULER-DEFICIT-45   [prove GGE Euler identity]
  W4-R3: GL-GGE-STABILITY-45 [free energy landscape F(T_1,...,T_8)]
  W4-R4: TWO-FLUID-DESI-45  [Landau-Khalatnikov -> DESI w(z)]
  W4-R5: PETER-WEYL-CENSORSHIP-45 [non-singlet leakage at 1/sqrt(N)]
         |
         v
WAVE 5-R (3 tasks -- reconciliation)
  W5-R1: DATA-PROVENANCE-45 [upstream audit + canonical constants]
  W5-R2: CC-GAP-UPDATE-45   [updated CC gap with all S45 results]
  W5-R3: CONSTRAINT-MAP-45  [full constraint surface update]
         |
         v
WAVE 6-R (1 task -- assessment, runs LAST)
  W6-R1: SAGAN-45           [probability update from 23% prior through W1 FAIL-FAIL]
```

### Decision Points

**DECISION POINT R1** (after Wave 1-R):

| Q-THEORY-KK-45 | Wave 2-R Configuration |
|:----------------|:----------------------|
| PASS (zero-crossing in [0.10, 0.25]) | q-theory IS the CC mechanism. UNEXPANDED-SA becomes cross-check (does the full functional agree?). Framework recovers despite n_s crisis. |
| FAIL (no crossing in [0.00, 0.50]) | Spike cutoff is the only surviving mathematical solution. UNEXPANDED-SA becomes critical (is the spike physical?). Section VI question is now empirically urgent. |
| INFO (crossing exists but wrong tau) | Partial — q-theory works but not at the fold. Investigate whether the crossing migrates with BCS corrections. |

### Task Count

| Wave | Tasks | Priority |
|:-----|:------|:---------|
| 1-R | 1 | CRITICAL |
| 2-R | 4 | HIGH |
| 3-R | 4 | HIGH/MEDIUM |
| 4-R | 5 | MEDIUM |
| 5-R | 3 | META |
| 6-R | 1 | META |
| **Total** | **18** | -- |

---

## III. Wave Prompts

### Wave 1-R: q-Theory on Discrete KK Tower (Q-THEORY-KK-45)

**Agent**: `volovik-superfluid-universe-theorist` (primary), `hawking-theorist` (Gibbs-Duhem cross-check)
**Model**: opus
**Cost**: MEDIUM
**S44 convergence**: 5/7 — Volovik, Quantum-Foam, Einstein, Tesla, SP

**Prompt**:

You are computing the single most important quantity remaining in the phonon-exflation framework: does the Volovik q-theory self-tuning mechanism produce a zero-crossing of the vacuum energy density rho(q_0(tau)) within the physical domain tau in [0.00, 0.50]?

**Why this is #1.** All 7 S44 reviewers endorsed q-theory or its equivalent (Carlip foam equilibrium, Jacobson thermodynamics) as the structurally necessary replacement for the spectral action in the vacuum energy sector. The S44 master synthesis states: "This is the single most important open computation: it determines whether q-theory works for this specific system or remains an analogy."

**Background.** Volovik's q-theory (Papers 15-16) introduces a thermodynamic vacuum variable q whose equilibrium value q_0 satisfies the stationarity condition d(rho)/dq = 0. At equilibrium, the Gibbs-Duhem identity forces rho(q_0) = 0 regardless of the microscopic energy scales. This is the superfluid analog of the CC self-tuning: in superfluid 3He, the equilibrium pressure equals zero despite the microscopic energy scale being 10^9 times larger.

**Prior attempt.** S43 QFIELD-43 found a zero-crossing at tau ~ 1.23 — outside the physical domain [0, 0.50]. However, S43 used: (a) the polynomial spectral action (not the trace-log), (b) the full spectral action (not the EIH singlet projection), and (c) a continuum approximation (not the discrete KK tower). S44 established three corrections that change the integrand by ~10 orders:

1. **Trace-log replacement** (S44 W1-4): The trace-log Tr ln(D_K^2) suppresses the vacuum energy by 5.11 orders relative to the polynomial spectral action. The q-theory vacuum variable should use the trace-log functional, not the polynomial.

2. **EIH singlet projection** (S44 W2-3): Only the (0,0) singlet component gravitates. S_singlet/S_fold = 5.684e-5 (4.25 orders suppression). The q-theory stationarity condition should be applied to the singlet-projected functional.

3. **Discrete KK tower** (S42): The 992 eigenvalues at max_pq_sum = 6 are discrete, not continuous. The spectral sums, zeta functions, and derivatives change when the continuum integral is replaced by a discrete sum.

**Computation Steps**:

1. **Construct the q-theory vacuum variable.** The vacuum variable q parametrizes the microscopic vacuum state. For the framework, candidates include: (a) the BCS gap Delta (vanishes post-transit, giving rho = 0 automatically — but this is trivial and doesn't test q-theory), (b) the spectral trace-log Tr ln(D_K^2) as a function of tau, (c) one of the 8 GGE conserved integrals. Use candidate (b) as the primary: q(tau) = (1/2) Tr ln(D_K(tau)^2) evaluated on the discrete KK tower with EIH singlet projection.

2. **Compute rho(q, tau).** The vacuum energy density as a function of q at each tau:

       rho(q, tau) = (1/(8*pi*G)) * [singlet-projected trace-log] = (M_KK^4 / (8*pi)) * sum_{k in singlet} d_k * ln(lambda_k(tau)^2)

   Apply the EIH singlet projection: only modes in the (0,0) representation contribute (f_s = 5.684e-5 of the full spectral action).

3. **Stationarity condition.** Solve d(rho)/d(tau) = 0 for tau* (the equilibrium point). This is the q-theory analog of finding the vacuum.

4. **Zero-crossing search.** Evaluate rho(tau) across tau in [0.00, 0.50] at 50 points. Search for tau* where rho(tau*) = 0. Report:
   - Does a zero-crossing exist?
   - Where is it? (tau*)
   - Is it in the physical domain [0.10, 0.25]?
   - What is rho'(tau*) (the slope at the crossing)?
   - What is the residual: |rho(tau*)| in GeV^4?

5. **Gibbs-Duhem verification.** At the zero-crossing tau*, verify the thermodynamic identity:

       rho + P = T * s + sum_k mu_k * n_k

   where P is the pressure (P = -rho for vacuum energy), T is the temperature (or the 8 GGE temperatures), s is the entropy density. If the identity holds, the zero-crossing is thermodynamically self-consistent.

6. **Sensitivity analysis.** How does tau* depend on:
   - The cutoff: max_pq_sum = 4, 5, 6 (truncation dependence)
   - The functional: trace-log vs polynomial (S44 showed 5.11 orders difference)
   - The projection: full vs singlet (S44 showed 4.25 orders difference)
   - The volume: Vol(SU(3)) = 1349.7 vs 8880.9 (S44 audit found 3 values)

7. **Comparison to S43 QFIELD-43.** The S43 computation found crossing at tau ~ 1.23 using polynomial SA without EIH projection. Reproduce S43's result, then show how each correction (trace-log, EIH, discrete) shifts the crossing point.

**FORMULA AUDIT PROTOCOL** (mandatory):
- (a) State: rho(tau) = (M_KK^4/(8pi)) * sum_{k in singlet} d_k ln(lambda_k^2), units [GeV^4]
- (b) Dimensional check: [M_KK^4] * [dimensionless sum] = [GeV^4]. Check.
- (c) Limiting case: for a single mode with lambda = M_KK, rho = M_KK^4/(8pi) * ln(1) = 0. For lambda >> M_KK, rho ~ M_KK^4 * ln(lambda/M_KK)^2 (logarithmic, not quartic — this is the trace-log advantage)
- (d) Cite: Volovik Papers 15-16 for q-theory; S44 W1-4 for trace-log; S44 W2-3 for EIH singlet

**Pre-registered gate Q-THEORY-KK-45**:
- **PASS**: Zero-crossing at tau* in [0.10, 0.25] with |rho(tau*)| < 10^{-10} M_KK^4
- **FAIL**: No zero-crossing in [0.00, 0.50] (repeats S43 failure)
- **INFO**: Zero-crossing exists but at tau* outside [0.10, 0.25]
- **BONUS**: tau* within 10% of tau_fold = 0.190

**Input files**:
- `tier0-computation/s43_qtheory_selftune.npz`
- `tier0-computation/s44_tracelog_cc.npz`
- `tier0-computation/s44_eih_grav.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s41_spectral_refinement.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- `tier0-computation/canonical_constants.py`
- `researchers/Volovik/15_2009_Volovik_Topology_Vacuum_Energy.md`
- `researchers/Volovik/16_2008_Volovik_q_Theory_Cosmological_Constant.md`

**Output files**:
- Script: `tier0-computation/s45_qtheory_kk.py`
- Data: `tier0-computation/s45_qtheory_kk.npz`
- Plot: `tier0-computation/s45_qtheory_kk.png`

**Working paper section**: W1-R

**Cross-check agent**: hawking-theorist
- Independent Gibbs-Duhem verification at tau*
- Check whether the zero-crossing is an artifact of the singlet projection
- Test the Carlip foam mechanism as an alternative route to rho = 0
- Report: `tier0-computation/s45_qtheory_kk_crosscheck.py`

---

### Wave 2-R: DM/DE + CC Alternatives (3 tasks, parallel)

#### W2-R1: Non-Equilibrium Specific Heat (ALPHA-EFF-45)

**Agent**: `volovik-superfluid-universe-theorist` (primary), `landau-condensed-matter-theorist` (cross-check)
**Model**: opus
**Cost**: MEDIUM
**S44 convergence**: 5/7

Compute alpha_eff from the 8-temperature GGE for DM/DE ratio. S44 W6-4 found best equilibrium estimate DM/DE = 1.06 (2.7x observed 0.387). The GGE has 8 independent temperatures (S44 W6-5), 3 of which are negative. Compute the non-equilibrium specific heat C_V^{GGE} = sum_k (dE_k/dT_k) and extract alpha_eff from the generalized Gibbs-Duhem relation. The 3 negative heat capacity eigenvalues create a sublinear effective alpha.

**Gate ALPHA-EFF-45**: PASS if alpha_eff in [0.3, 0.5]. FAIL if alpha_eff > 2.0. INFO if computed but model-dependent.

**Input files**: `tier0-computation/s44_multi_t_jacobson.npz`, `tier0-computation/s42_gge_energy.npz`, `tier0-computation/s44_dm_de_ratio.npz`
**Output**: Script `s45_alpha_eff.py`, Data `.npz`, Plot `.png`
**Working paper section**: W2-R1

---

#### W2-R2: Unexpanded Spectral Action for CC (UNEXPANDED-SA-45)

**Agent**: `connes-ncg-theorist`
**Model**: opus
**Cost**: MEDIUM
**S44 convergence**: 3/7 (Einstein, SP, Tesla) — Section VI centerpiece, NEVER IN ORIGINAL PLAN

The S44 master synthesis Section VI identified a critical gap: "the unexpanded spectral action (which may naturally produce the required moment hierarchy through nonlocal structure) is the one route that could bridge the 'impossibility' and 'fine-tuning' readings." The polynomial expansion S ~ a_0 Lambda^4 + a_2 Lambda^2 + a_4 + ... discards nonlocal information. The full functional Tr f(D^2/Lambda^2) contains the complete spectral content.

**Computation**: Evaluate the FULL (non-expanded) spectral action Tr f(D_K^2/Lambda^2) for several explicit f choices (not just the Seeley-DeWitt coefficients). For each f:
1. Compute S_full(tau) = sum_k d_k f(lambda_k(tau)^2/Lambda^2) directly (no asymptotic expansion)
2. Compare to the polynomial approximation S_poly = a_0 Lambda^4 + a_2 Lambda^2 + a_4
3. Compute the exact f_2 and f_4 moments from S_full and check whether f_4/f_2 ~ 10^{-121} arises naturally for any f
4. Test: does ANY f with O(1) support width produce f_4/f_2 < 10^{-10}?
5. Test the "bound state in the continuum" scenario: if one eigenvalue sits at a special value, does a natural f produce the hierarchy?

**Gate UNEXPANDED-SA-45**: INFO (does the full functional contain CC information the expansion discards?). PASS if any O(1)-width f produces f_4/f_2 < 10^{-50}. FAIL if polynomial expansion captures all content.

**Input files**: `tier0-computation/s42_hauser_feshbach.npz`, `tier0-computation/s41_spectral_refinement.npz`
**Output**: Script `s45_unexpanded_sa.py`, Data `.npz`
**Working paper section**: W2-R2

---

#### W2-R3: Analytic Torsion (ANALYTIC-TORSION-45)

**Agent**: `spectral-geometer`
**Model**: opus
**Cost**: MEDIUM

Compute the Ray-Singer analytic torsion T(SU(3), g_fold). The post-transit CC is purely geometric: Tr ln(D_K^2) on SU(3) at the fold. If analytic torsion vanishes or produces massive suppression, the geometric CC is solved.

**Gate ANALYTIC-TORSION-45**: PASS if log10(T) < -50. FAIL if T = O(1). INFO if computed but interpretation unclear.

**Input files**: `tier0-computation/s42_hauser_feshbach.npz`, `tier0-computation/s41_spectral_refinement.npz`
**Output**: Script `s45_analytic_torsion.py`, Data `.npz`, Plot `.png`
**Working paper section**: W2-R3

---

#### W2-R4: EIH Perturbation k-Mapping for Definitive n_s (KZ-NS-KMAP-45)

**Agent**: `einstein-theorist` (primary), `kaluza-klein-theorist` (KK reduction cross-check)
**Model**: opus
**Cost**: MEDIUM

**Context**: KZ-NS-45 reported n_s = -0.588 but Einstein's cross-check found n_s spans [-2.0, +5.8] across 4 k-mappings with R² < 0.05. The Bogoliubov coefficients |beta_k|² are solid (ENDORSED). The problem: no one has derived how internal KK quantum numbers map to 4D cosmological wavenumbers for PERTURBATIONS. The EIH projection (S44 W2-3) was derived for the background only. This is a structural gap, not a numerical failure.

**Computation**: Derive the KK perturbation projection from first principles:
1. 12D metric perturbation decomposition in Peter-Weyl harmonics
2. For each (p,q) mode, compute 4D effective perturbation and its gravitational coupling
3. The 4D wavenumber k(p,q) follows from the mode's contribution to delta H / H
4. With the DERIVED k-mapping, recompute P(k) and extract n_s
5. Report R² — if < 0.5, the spectrum is not a power law (report what it IS)

**Gate KZ-NS-KMAP-45**:
- **PASS**: Derived k-mapping → n_s in [0.80, 1.10]
- **FAIL**: Derived k-mapping → n_s outside [0.80, 1.10] with R² > 0.5
- **INFO**: Spectrum is not a power law
- **STRUCTURAL**: No unique k-mapping exists

**Input files**: `s45_kz_ns.npz`, `s44_eih_grav.npz`, `s42_hauser_feshbach.npz`, `s42_constants_snapshot.npz`
**Output**: `s45_kz_ns_kmap.{py,npz,png}`
**Working paper section**: W2-R4

---

### Wave 3-R: n_s Crisis + Tensions + CC Tests (5 tasks, parallel)

#### W3-R1: Scale Selection for Spectral Dimension n_s (SIGMA-SELECT-45)

**Agent**: `connes-ncg-theorist` (primary), `hawking-theorist` (backreaction)
**Model**: opus

S44 W2-2 found n_s = 0.961 at sigma = 1.10 but sigma is unfixed. With all three dynamical n_s routes now closed (epsilon_H invariance, Lifshitz eta, Bogoliubov), sigma selection is the SOLE SURVIVING n_s route. Test three selection principles:
1. Backreaction: Lambda = Lambda(tau, d_s) self-consistency loop
2. Hubble matching: sigma = 1/H^2 at the pivot scale
3. Occupied-state sigma: replace D_K^2 with n_k D_K^2 in the heat kernel

**Gate SIGMA-SELECT-45**: PASS if self-consistent sigma yields n_s in [0.955, 0.975]. FAIL if no fixed point. INFO if sigma found but n_s outside window.

**Input files**: `tier0-computation/s44_dimflow.npz`, `tier0-computation/s42_constants_snapshot.npz`
**Output**: Script `s45_sigma_select.py`
**Working paper section**: W3-R1

---

#### W3-R2: M_KK Tension Resolution (MKK-TENSION-45)

**Agent**: `baptista-spacetime-analyst`
**Model**: opus

S44 W7-1 confirmed 0.83-decade M_KK tension is real and Vol-independent. Definitive audit: (1) derive Vol(SU(3)) analytically from Macdonald formula, (2) trace where Vol enters Kerner formula, (3) recompute M_KK from both routes, (4) KK threshold corrections, (5) Baptista hypercharge normalization variants.

**Gate MKK-TENSION-45**: PASS if tension < 0.2 decades. FAIL if structural. INFO if partial.

**Input files**: `tier0-computation/s44_mkk_reconcile.npz`, `tier0-computation/s44_constants_corrected.npz`
**Output**: Script `s45_mkk_tension.py`, Data `.npz`
**Working paper section**: W3-R2

---

#### W3-R3: Truncated/Singlet Torsion at Dissolution Scale (TRUNCATED-TORSION-45)

**Agent**: `spectral-geometer`
**Model**: opus

W2-R3 found T(SU(3)) = 10^{20301} from 6440 modes. But only 16 singlet modes gravitate (EIH), and dissolution (epsilon_c ~ 1/√N) limits geometric resolution. At the M_KK scale (~10-100 Planck lengths), there's a physical limit on geometric twist. Compute T restricted to: (a) singlet sector only (16 modes), (b) progressive truncation levels (max_pq_sum = 1,2,3,4,5,6), (c) singlet at dissolution cutoff.

**Gate TRUNCATED-TORSION-45**: INFO (is physical torsion bounded to O(1)-O(10²)?).

**Input files**: `s45_analytic_torsion.npz`, `s42_hauser_feshbach.npz`, `s44_eih_grav.npz`
**Output**: Script `s45_truncated_torsion.py`, Data `.npz`
**Working paper section**: W3-R3

---

#### W3-R4: Van Hove Fine Scan (DOS-FINE-SCAN-45)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus

Fine scan at 20 tau values in [0.19, 0.21]. Track T3-T5 trajectories: do they CROSS or merely approach? Crossing topology determines van Hove enhancement strength for q-theory and occupied-state interpretations.

**Gate DOS-FINE-SCAN-45**: INFO (structural diagnostic).

**Input files**: `tier0-computation/s44_vanhove_track.npz`, `tier0-computation/tier1_dirac_spectrum.py`
**Output**: Script `s45_dos_fine_scan.py`, Data `.npz`, Plot `.png`
**Working paper section**: W3-R4

---

#### W3-R5: CC-Hierarchy Cubed Moment Ratio Test (CC-HIERARCHY-CUBED-45)

**Agent**: `gen-physicist`
**Model**: opus

User observation: CC gap (110.5 orders) / hierarchy problem (36 orders) = 3.07 ≈ 3. If each spectral action moment ratio (a₀→a₂, a₂→a₄) independently equals ~10^{36}, the CC is the hierarchy problem cubed — not an independent fine-tuning. Test from existing data: W2-R2 forward moments (A_0=6440, A_2=16448, A_4=45426) and zeta sums (Z_2=2776, Z_4=1351). Include Λ dependence and dimensional factors. Check whether Peter-Weyl degeneracy structure on SU(3) fixes these ratios.

**Gate CC-HIERARCHY-CUBED-45**: INFO (is CC = hierarchy³ structural or coincidental?).

**Input files**: `s45_unexpanded_sa.npz`, `s45_cc_balance_sheet.md`, `s42_hauser_feshbach.npz`, `s44_eih_grav.npz`, `canonical_constants.py`
**Output**: Script `s45_cc_hierarchy_cubed.py`, Data `.npz`
**Working paper section**: W3-R5

---

### Wave 4-R: Specialist (5 tasks, parallel)

#### W4-R1: Running Sakharov G_N(tau) (RUNNING-GN-45)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus

Compute G_N(tau) across the full transit using the Sakharov formula. Report whether G_N is monotone and how it evolves.

**Gate RUNNING-GN-45**: INFO.

**Input**: `s44_sakharov_gn_audit.npz`, `s41_spectral_refinement.npz`
**Output**: Script `s45_running_gn.py`, Data `.npz`, Plot `.png`
**Working paper section**: W4-R1

---

#### W4-R2: Euler Deficit Identity (EULER-DEFICIT-45)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus

Prove or disprove: E = sum_k T_k S_k - PV + sum_k mu_k N_k + |E_cond|. S44 W6-5 found the deficit = |E_cond| = 6.8% numerically.

**Gate EULER-DEFICIT-45**: INFO.

**Input**: `s44_multi_t_jacobson.npz`, `s42_gge_energy.npz`
**Output**: Script `s45_euler_deficit.py`
**Working paper section**: W4-R2

---

#### W4-R3: GL Free Energy Landscape (GL-GGE-STABILITY-45)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus

Construct F(T_1,...,T_8) on the 8-temperature GGE manifold. S44 W6-5 found 3/8 negative heat capacity eigenvalues. Map minima, saddle points, barriers.

**Gate GL-GGE-STABILITY-45**: INFO.

**Input**: `s44_multi_t_jacobson.npz`, `s42_gge_energy.npz`
**Output**: Script `s45_gl_gge.py`, Data `.npz`
**Working paper section**: W4-R3

---

#### W4-R4: Two-Fluid Cosmology → DESI w(z) (TWO-FLUID-DESI-45)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus

Map the two-fluid post-transit state to effective w(z). Compare to DESI DR1 data and S42 tessellation-lensing-bias hypothesis.

**Gate TWO-FLUID-DESI-45**: INFO.

**Input**: `s44_dm_de_ratio.npz`, `s42_constants_snapshot.npz`
**Output**: Script `s45_two_fluid_desi.py`, Data `.npz`
**Working paper section**: W4-R4

---

#### W4-R5: Peter-Weyl Censorship (PETER-WEYL-CENSORSHIP-45)

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus

S44 W2-3 found 17,594x suppression. S44 W6-7 found epsilon_c ~ 1/sqrt(N). Compute non-singlet leakage at 1/sqrt(N). Does the 17,594x suppression survive finite perturbations?

**Gate PETER-WEYL-CENSORSHIP-45**: INFO.

**Input**: `s44_eih_grav.npz`, `s44_dissolution_scaling.npz`
**Output**: Script `s45_peter_weyl_censorship.py`
**Working paper section**: W4-R5

---

### Wave 5-R: Reconciliation (3 tasks)

#### W5-R1: Data Provenance Audit (DATA-PROVENANCE-45)

**Agent**: `gen-physicist`
**Model**: opus

Complete the upstream audit. Produce canonical constants file. Cross-check all .npz files for consistency.

**Gate DATA-PROVENANCE-45**: INFO.
**Output**: `s45_data_provenance_audit.md`
**Working paper section**: W5-R1

---

#### W5-R2: CC Gap Update (CC-GAP-UPDATE-45)

**Agent**: `einstein-theorist`
**Model**: opus

Update CC gap from S44's 110.5 orders incorporating: q-theory result (W1-R), analytic torsion (W2-R3), unexpanded SA (W2-R2), and all new suppressions.

**Gate CC-GAP-UPDATE-45**: INFO.
**Output**: Script `s45_cc_gap_update.py`
**Working paper section**: W5-R2

---

#### W5-R3: Constraint Map Update (CONSTRAINT-MAP-45)

**Agent**: `gen-physicist`
**Model**: opus

Full constraint surface update: new walls, gate verdicts, closures, surviving regions. Feeds Sagan.

**Gate CONSTRAINT-MAP-45**: META.
**Working paper section**: W5-R3

---

### Wave 6-R: Assessment (1 task, runs LAST)

#### W6-R1: Sagan Assessment (SAGAN-45)

**Agent**: `sagan-empiricist`
**Model**: opus

Evaluate ALL S45 results. W1 FAIL-FAIL already establishes P in 3-8% range. If q-theory PASS, partial recovery. Full gate-by-gate Bayesian update from 23% prior.

**Output**: `sessions/session-45/s45_sagan_assessment.md`
**Working paper section**: W6-R1

---

## IV. Gate Summary (Rebuilt)

### Pre-Registered Gates

| Gate ID | Agent | Criterion (PASS) | Criterion (FAIL) |
|:--------|:------|:-----------------|:-----------------|
| Q-THEORY-KK-45 | volovik, hawking | Zero-crossing at tau in [0.10, 0.25] | No crossing in [0.00, 0.50] |
| ALPHA-EFF-45 | volovik, landau | alpha_eff in [0.3, 0.5] | alpha_eff > 2.0 |
| SIGMA-SELECT-45 | connes, hawking | Self-consistent sigma → n_s in [0.955, 0.975] | No fixed point |
| MKK-TENSION-45 | baptista | Tension < 0.2 decades | Structural, irreducible |
| ANALYTIC-TORSION-45 | spectral-geometer | log10(T) < -50 | T = O(1) |

### INFO Gates

| Gate ID | Agent | Purpose |
|:--------|:------|:--------|
| UNEXPANDED-SA-45 | connes | Does full functional contain CC info expansion discards? |
| ECOND-RECONCILE-45 | nazarewicz | Authoritative E_cond |
| DOS-FINE-SCAN-45 | quantum-acoustics | Van Hove crossing topology |
| RUNNING-GN-45 | volovik | G_N(tau) evolution |
| EULER-DEFICIT-45 | volovik | GGE thermodynamic identity |
| GL-GGE-STABILITY-45 | landau | Free energy landscape |
| TWO-FLUID-DESI-45 | volovik | w(z) prediction |
| PETER-WEYL-CENSORSHIP-45 | SP | EIH robustness |
| DATA-PROVENANCE-45 | gen-physicist | Upstream audit |
| CC-GAP-UPDATE-45 | einstein | Updated CC accounting |

### Already Complete (W1)

| Gate ID | Verdict | Result |
|:--------|:--------|:-------|
| OCC-SPEC-45 | **FAIL** | S_occ monotone decreasing. 28th equilibrium closure. |
| KZ-NS-45 | **FAIL** | n_s = -0.588. Third n_s closure. k-mapping structurally ill-defined. |

---

## V. Global Rules

1. ALL physics agents use opus
2. Script prefix: `s45_`
3. Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
4. Output directory: `tier0-computation/`
5. Working paper: `sessions/session-45/session-45-results-workingpaper.md`
6. Import constants from `tier0-computation/canonical_constants.py`
7. Formula audit protocol mandatory (S44 Section VII, #7)
8. Path quoting: ALL bash paths with "Ainulindale Exflation" double-quoted
