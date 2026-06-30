# Session 78 Plan — Scrubbed (Canonical Merge)

**Date**: 2026-04-15
**Source**: merged from four independent scrubs of `sessions/session-plan/session-78-plan.md`:
- `session-78-plan-scrubbed-nazarewicz.md` (UQ / pre-registration / Bayesian model averaging)
- `session-78-plan-scrubbed-lizzi.md` (scheme-discipline / convention pinning / F_amp exponent resolution)
- `session-78-plan-scrubbed-transit.md` (mode-dynamics / backreaction / IC selection)
- `session-78-plan-scrubbed-genphysicist.md` (adversarial / discrimination-margin / construction-forced PASS)

**Status of S78**: Executed and TOSSED. This plan is the cleaned specification against which a future re-run should be evaluated. It is NOT a re-run order.

**Headline correction**: Lizzi's scrub resolves the F_amp exponent ambiguity that propagated through at least six gates of the original plan. F_amp is a POWER RATIO, LINEAR in the A_s product — not F_amp^2. The original plan's master equation `A_s = (H^2/(8π^2 ε M_Pl_red^2)) × F_amp^2 × f_conv × S_IC` concealed a double-count of factor 6858 (≈ 3.8 OOM). Every appearance of F_amp^2 in the original plan must be replaced by F_amp^1 in any re-run. See Section 0 convention block below.

---

## 0. Plan-Wide Convention Pin Block (REQUIRED BEFORE ANY RE-RUN)

Every script and agent reading this plan must adopt these conventions. Any script that deviates fails the scheme-discipline audit at gate level.

### 0.1 F_amp — POWER RATIO, LINEAR
- **Definition**: F_amp(k) ≡ P_zeta(real, k) / P_zeta(pure dS, k). Dimensionless power ratio.
- **Usage in A_s**: A_s = F_amp × P_dS × f_conv × S_IC. LINEAR in F_amp, NOT squared.
- **Numerical reference**: F_amp(k_pivot) = 6858 at L_max=10 is a power ratio; it already contains the squaring of the amplitude. Multiplying again by F_amp double-counts by ~3.8 OOM.
- **Provenance**: `s77_transition_scale_pbh.py` is the canonical reference script (F_amp as P_zeta ratio). `s77_bogoliubov_friedmann_as.py` line 405 (`A_s = A_s(slow-roll) * F_amp^2`) has the wrong exponent and must be fixed or replaced.
- **Cite**: Parker 1966 (Transit-Dynamics/01); Birrell-Davies 1982 (Transit-Dynamics/02); Lizzi arXiv:1103.0478. Lizzi scrub Section 3.

### 0.2 a_n scheme (SDW vs zeta vs HK)
- **SDW moments**: a_n^{SDW} ≡ Seeley-DeWitt coefficient of Tr(sqrt(D^2)). Canonical heat-kernel expansion in the framework.
- **Zeta moments**: a_n^{zeta} ≡ coefficient in zeta_D(s) at s near n. Differs from SDW by dimensional factors.
- **Heat-kernel Taylor moments**: a_n^{HK} ≡ coefficient in formal Taylor expansion of Tr(exp(-t D^2)). Gilkey-universal.
- **Conversion (S78 W3-L dictionary)**: a_n^{HK} = c(n, d) × a_n^{SDW}. For d=4, c(0)=c(2)=c(4)=1/(16π^2). Confounding produces up to 9 OOM errors (S77 W2-K permanent).
- **Framework default**: zeta moments unless tagged otherwise in canonical_constants.py.

### 0.3 Cutoff family
- **Sharp cutoff** (Andrianov-Lizzi arXiv:1103.0478): f_0=1/2, f_2=1, f_4=1, f_n=0 for n>4. USED EXCLUSIVELY for the anomaly-derived comparison (W2-D).
- **f* cutoff** (S72): f*(x) = 0.912 sqrt(x) + 0.088 exp(-x). Framework default for cutoff-dependent computations.
- **SDW**: f(x) = sqrt(x) — canonical for HK expansion and chi_2 = <sqrt(x)> identity.
- **Zeta**: direct zeta-regularization of Tr(D^s), no cutoff. Canonical for framework a_n moments.

### 0.4 R_1 / R_2 normalization
- **R_1** ≡ a_0 × a_4 / a_2^2. Dimensionless. Level 2 scheme-invariant **per-branch only**, NOT cross-branch (S78 W3-L dictionary correction).
- **R_2** ≡ a_2 × a_6 / a_4^2. Level 2 scheme-invariant per-branch.
- **Framework default**: zeta, L_max=10. R_1 ≈ 1.0128.
- Cross-branch ratios (e.g., J_C2/J_su2) are Level 3 (scheme-dependent); NOT R-protected.

### 0.5 Pre-fold IC principle
- **Framework canonical default**: AZ-topology (Lizzi) / spectral stationarity (Transit) — see DISAGREEMENT BLOCK at W1-E. This plan adopts **spectral stationarity** as the primary, with AZ-topology and minimum-entropy as cross-checks, PENDING user decision on the axiomatic gap.
- **S_IC convention**: S_IC(k) = |alpha_k + beta_k|^2, the squeezed-vacuum power spectrum enhancement. NOT |alpha_k|^2 - |beta_k|^2 (this equals 1 by unitarity and is NOT a suppression factor). NOT |alpha_k|^2 + |beta_k|^2 (this is mean particle number + 1). The original plan's `|alpha_k - beta_k|^2` and `|alpha_k|^2 - |beta_k|^2` phrasing must be corrected to |alpha_k + beta_k|^2.
- **Cite**: Lizzi scrub Section 3; Parker 1966; Birrell-Davies 1982.

### 0.6 f_n Mellin moment normalization
- Mellin moment f_n = (1/Γ(n/2)) × ∫_0^∞ x^{n/2-1} f(x) dx for d=4 dimensional traces.
- For the anomaly derivation (sharp cutoff): f_0 = 1/2 is FORCED, not a free choice.
- For f*: Mellin moments {f_0^{f*}, f_2^{f*}, f_4^{f*}} computed numerically, reported as new canonical_constants entries.
- For SDW f(x) = sqrt(x): Mellin diverges; regularize with large-x cutoff at Lambda^2.

### 0.7 Leggett-channel Omega_DM formula (for W3-D)
- **Framework default** (linear GGE thermal): Omega_DM h^2 = n_L × m_L / rho_crit, where n_L is GGE relic Leggett density (S77 GGE-OCC) and m_L is Leggett mode mass in f* scheme.
- NOT full Bose-Einstein thermal (the GGE is not thermal; it is integrable).
- Cross-check scheme: SDW; zeta does not give a finite m_L (no IR mass scale).
- "Canonical 0.120" provenance: Planck 2018 central value; observational, not framework-derived.

### 0.8 k_pivot, horizon-crossing, integrator tolerances
- **k_pivot**: 0.05 Mpc^-1 (Planck convention). Pin this; no Mpc/h or Gpc variants.
- **Horizon crossing**: k/(aH) = 1 (not k = H).
- **Wronskian normalization**: Bunch-Davies amplitude 1/sqrt(2k).
- **Bunch-Davies IC imposed at**: k/(aH) = 100 (deep subhorizon).
- **Numeric integrator**: scipy solve_ivp method='DOP853', rtol=1e-10, atol=1e-12. Benchmark against exact de Sitter before physics run.

### 0.9 Tag discipline
Every numerical deliverable must carry the four-tuple **(value, scheme_tag, convention_tag, L_max_tag)**. Scheme tags: {SDW, zeta, f*, anomaly, SCHEME-INDEPENDENT}. Convention tags for F_amp: {POWER-RATIO}; for S_IC: {|alpha+beta|^2}. Absence of any tag is a scheme-discipline failure that pushes the gate to INFO by default.

### 0.10 Gate-level epistemic rule: INCOMPUTABLE is not FAIL
Per Transit scrub: every iterative or extrapolation method must pre-register a convergence criterion AND a fallback policy. If convergence cannot be reached in any pre-registered method, the verdict is **INCOMPUTABLE**, not FAIL. INCOMPUTABLE means the computation cannot return a scheme-consistent number; FAIL means the hypothesis was tested and disproved. Both are information; they are not the same verdict.

---

## I. Session Objective (restated with corrected conventions)

Session 78 is a consistency audit of the A_s normalization chain in the phonon-exflation framework. The question is whether the framework — as currently stated — produces a single, scheme-consistent, convention-pinned numerical value for A_s(k_pivot) that can be compared to Planck 2.1e-9 without post-hoc curation.

The original plan allowed convention-shopping at seven distinct points (F_amp exponent, a_n scheme, cutoff family, R-protection scope, IC principle selection, f_conv scheme, S_IC formula). Any one of these made the A_s PASS verdict dependent on the executing agent's convention choice rather than on the framework's internal structure. This scrubbed plan pins all seven conventions before gate evaluation.

**Master gate (re-registered)**: S78-MASTER — see Section III below. The original disjunctive "at least one of {A_s^{TE}, A_s^{LL}, A_s^{SPT}} matches within factor 3" is structurally unfixable and is replaced by a single pre-registered A_s^{framework} value under the pinned conventions.

---

## II. Wave Structure

Same 3-wave parallel compute structure as the original plan (Wave 1: 5 tasks, Wave 2: 7 tasks, Wave 3: 16 tasks = 28 gates). No changes to the dependency graph. Wave 2 and Wave 3 individual gates are re-registered, demoted to INFO/META, or removed per the verdict table in the Merge Log at end.

Decision points (after Wave 1, after Wave 2) retained with verdicts re-keyed to the pinned A_s^{framework} value; see Section VII.

---

## III. Master Gate (Re-registered)

### S78-MASTER: A_s-normalization-chain-end-to-end  [VERDICT: RE-REGISTER]

**Convention pins**: Section 0.1–0.9 apply in full. Pinned single scheme: **f*** (canonical); SDW and zeta as cross-checks per-gate. F_amp as POWER RATIO (Section 0.1). S_IC = |α+β|^2 (Section 0.5).

**Pre-registered gate**:
- **HYPOTHESIS**: Under the pinned conventions (Section 0), A_s^{framework}(k_pivot) = F_amp × P_dS × f_conv × S_IC produces a single numerical value with stated 1-sigma propagated error from the factor ledger.
- **Pre-registered expected value**: A_s^{framework}(f*, S_IC=1, F_amp=linearized 6858 power-ratio) = 1.72e-9 (Lizzi-Landau reading, Section 0.1 pinned). Tolerance: factor 2 (propagated uncertainty from the single-scheme factor ledger). This is the null hypothesis against which deviations are measured.
- **PASS**: Computed A_s^{framework} within the propagated error bar of 1.72e-9; AND every factor in the ledger carries its (value, scheme_tag, convention_tag, L_max_tag); AND any deviation from 2.1e-9 has a pre-named physical source (S_IC from W1-E, or a sub-horizon correction from W2-E, or a documented backreaction reduction from W1-C).
- **FAIL**: Any factor in the ledger lacks a tag; OR the computed value falls outside (1.72e-9 / 4, 1.72e-9 × 4) in the pinned convention; OR the three schemes (f*, SDW, zeta) produce values inconsistent with R-protection per-branch bounds (drift > 1.3%).
- **INFO**: Ledger complete, single-scheme value within band, but W1-C/W1-E return INCOMPUTABLE — then the session pre-registers the gap between computed A_s^{framework} and 2.1e-9 as the quantitative output, with a named target for S79.
- **INCOMPUTABLE**: Factor ledger cannot be closed because some factor's provenance is missing AND no Wave 1 script can compute it. This is NOT a PASS or FAIL — it is a "the plan cannot run" verdict.

**Cross-checks**:
1. The scheme-invariant ratio A_s(k_pivot) / A_s(2·k_pivot) is CONVENTION-INDEPENDENT (Lizzi scrub W1-A alternative). Report this ratio as the primary scheme-robust deliverable; its predicted value from tilt is (k/k_pivot)^{n_s-1} ≈ 1.030.
2. Dimensional consistency of every factor in the ledger.
3. R-protection per-branch: f_conv^{zeta}/f_conv^{SDW} = 1/R_1, verified within 0.053 OOM.
4. Null trace: report A_s under the canonical Bunch-Davies slow-roll pipeline (no F_amp ≠ 1, no S_IC ≠ 1) as the baseline against which every correction is a delta.

**Pre-registered Bayesian UQ band** (from Nazarewicz scrub Section 4): The A_s^{framework} ledger is a composite product of scheme-uncertain factors. The primary deliverable is a POSTERIOR distribution on A_s^{framework}, with mass computed under the pinned (f*, POWER-RATIO) convention and variance decomposed by factor. Report what fraction of the posterior mass falls within Planck 1-sigma; falls within 2-sigma; falls at or beyond the 9.51 OOM overproduction reading. The PASS band (1.72e-9 / 4, 1.72e-9 × 4) must capture ≥ 68% of the posterior.

**DISAGREEMENT BLOCK — Master gate structural form**:
- **Gen-Physicist position**: The original disjunctive "at least one of three candidates matches within factor 3" is structurally unfixable. Even the re-registered single-value form above is only informative if the three candidates are explicit FAILURE modes, not disjunctive PASS paths. Gen-Physicist would write A_s^{TE} (10^{+9.5} overproduction), A_s^{LL} (1.72e-9 match), A_s^{SPT} (O(1) saturation) as three explicit pre-named failure modes whose presence is evidence of a specific mis-identification, not as disjunctive PASS escape hatches.
- **Nazarewicz position**: Keep the master gate with tightening — a single scheme-pinned expected value and propagated error bar is sufficient. The three candidate accounts are methodological forks whose resolution comes from W1-A's factor-ledger audit, not from the master gate itself.
- **Implication for plan**: If user selects Gen-Physicist framing, the three accounts become explicitly-FAIL patterns and the Decision Point 1 branch selection becomes "which of the three specific failure patterns is computed," not "which of the three is the correct branch." If user selects Nazarewicz framing, the master gate is a consistency check and the branch selection is made in synthesis using the W1-A ledger.
- **USER DECISION REQUIRED**: structural form of the master gate.

**Notes from scrub**: Nazarewicz provided the BMA/posterior framing. Lizzi provided the convention pins (F_amp power-ratio; S_IC = |α+β|^2). Transit provided the INCOMPUTABLE-distinct-from-FAIL discipline. Gen-Physicist flagged the disjunctive-PASS structural flaw that required the DISAGREEMENT BLOCK above.

---

## IV. Wave 1: Critical Path (5 gates, all re-registered)

### W1-A: AS-NORMALIZATION-TRACE  [VERDICT: RE-REGISTER]

**Convention pins (REQUIRED BEFORE RUN)**:
- F_amp: POWER RATIO (Section 0.1). The original plan's `F_amp^2` in the master equation is a convention error and must read `F_amp × …`.
- a_n: zeta moments (framework default, Section 0.2).
- Cutoff family: f* primary; SDW and zeta as cross-checks.
- M_Pl convention: reduced Planck M_Pl_red = 2.435e18 GeV.
- epsilon: slow-roll eps = -dH/dN / H^2, evaluated at horizon crossing for k_pivot.
- R_scheme identically 1 when the ledger is evaluated in a single scheme throughout. The three workshop accounts {TE, LL, SPT} are distinguished by which factor each modifies, NOT by a multiplicative R_scheme.
- f_conv units: dimensionless in CMB-target units (M_KK/M_Pl_red)^2; canonical SDW value 2.549e-10.
- S_IC: symbolic; no pre-announced numerical value in this gate (W1-E supplies).

**Pre-registered gate**:
- **HYPOTHESIS**: With the Section 0 conventions pinned, A_s(k_pivot) = F_amp × P_dS × f_conv × S_IC is reproducible to within 1% across independent recomputations by any agent. The three S77 workshop accounts differ in which factor they reassign.
- **Pre-registered expected value**: A_s^{framework}(f*, S_IC=1, linearized F_amp=6858 power-ratio) = 1.72e-9 ± factor 2.
- **PASS**: (1) Ledger table produced; every factor carries (value, scheme_tag, convention_tag, L_max_tag). (2) The product under the pinned convention agrees with 1.72e-9 within factor 2 propagated error. (3) Workshop accounts {TE, LL, SPT} are each identified with a specific factor reassignment: TE modifies f_conv (claims double-count with M_KK^2/M_Pl_red^2), LL is the pinned-convention product, SPT modifies F_amp (claims self-consistent O(1) cap via W1-C).
- **FAIL**: Any factor lacks a tag; OR the pinned-convention product differs from 1.72e-9 by more than factor 4 with no named source; OR the three schemes produce values inconsistent with R-protection per-branch drift < 1.3%.
- **INFO**: Ledger complete and product in band but the three-scheme spread is larger than the propagated error bar — scheme-dependence is material and W2-D/W2-F resolution is required before a PASS verdict.
- **INCOMPUTABLE**: Any factor's provenance is not locatable and no Wave 1 script can compute it.

**Cross-checks (each tests an INDEPENDENT physical consequence)**:
1. Dimensional consistency: [A_s] = dimensionless; [F_amp] = dimensionless; [f_conv] = (M_Pl_red)^{-2} × (M_KK)^2 = dimensionless in CMB target units. Close dimensionally before numerics. (Tests: unit coherence.)
2. R-protection identity: f_conv^{zeta}/f_conv^{SDW} = 1/R_1 = 0.053 OOM drift. (Tests: S76 R2 identity preserved.)
3. Null trace: A_s under canonical Bunch-Davies slow-roll pipeline without F_amp amplification reported as reference baseline. (Tests: deltas are measured against a derivation, not against an assertion.)
4. Factor-degeneracy check: d(ln A_s)/d(ln F_amp) = 1 under the pinned POWER-RATIO convention; report this derivative. If it comes out 2, the script is still using F_amp^2. (Tests: convention pin is enforced in code, not just in prose.)
5. Scheme-invariant alternative: ratio A_s(k_pivot)/A_s(2·k_pivot) predicted from tilt ≈ 1.030; report this as a convention-independent primary deliverable. (Tests: scheme-robust consequence.)
6. Scheme-tag audit: every factor carries explicit tag; untagged factors reject the ledger. (Tests: discipline of tagging.)

**Notes from scrub**: Lizzi contributed the F_amp power-ratio resolution and the scheme-invariant ratio alternative. Nazarewicz contributed the propagated-error structure (replacing "factor 3"). Transit contributed the validity-regime column requirement (each factor tagged adiabatic-WKB / sudden / exact-numeric / symbolic). Gen-Physicist forced the RE-REGISTER from disjunctive "at least one … in at least one scheme" to a single pre-registered numerical expectation.

---

### W1-B: NORMALIZATION-INDEPENDENT-VERIFICATION  [VERDICT: RE-REGISTER]

**Convention pins**:
- k_pivot = 0.05 Mpc^-1 (no variants).
- Horizon crossing: k/(aH) = 1.
- Wronskian normalization: Bunch-Davies amplitude 1/sqrt(2k).
- Bunch-Davies IC imposed at k/(aH) = 100.
- F_amp as POWER RATIO (Section 0.1).

**Pre-registered gate**:
- **HYPOTHESIS**: Three independent methods reproduce (N_pivot, k/aH at N_end, F_amp power-ratio) within the quadrature sum of each method's pre-registered systematic error.
- **PASS**: Method A (analytic matching) and Method B (direct numeric) agree on all three numbers within the quadrature sum of (a) Method A's matching-region ambiguity and (b) Method B's integrator tolerance. Method C (tensor cross-check) pins N_pivot within the same combined error band. Critically: Method A and Method B must implement DIFFERENT mode equations so that disagreement exceeds numerical noise only under physics mismatches (Gen-Physicist). For example, Method A in conformal time, Method B in cosmic time with explicit Hubble friction.
- **FAIL**: Any method disagrees with any other by > 20% and the disagreement is not attributable to a clearly-identified regime-validity issue.
- **INFO**: Methods agree within 5-20%; residual disagreement root-caused.
- **INCOMPUTABLE**: WKB adiabaticity diagnostic max(|omega'/omega^2|) > 0.3 AND integrator fails to close on the exact de Sitter benchmark to 1e-5 drift per period. Means the numerical foundation is not laid.

**Pre-registered regime-of-validity per method (Transit)**:
- Method A: WKB adiabaticity max(|omega'/omega^2|) < 0.3; report Stokes/Weber coefficients at each turning point.
- Method B: scipy solve_ivp DOP853, rtol=1e-10 atol=1e-12; drift per period against exact de Sitter < 1e-5.
- Method C: report d ln(epsilon)/dN at N_pivot; N_pivot^T = N_pivot^S only if epsilon is slowly-varying there; otherwise report the predicted gap as a pre-registered non-trivial quantity (Gen-Physicist).

**Cross-checks**:
1. Bunch-Davies recovery: in a control with epsilon=const slow-roll and a(N)=exp(N), Method B must reproduce F_amp = 1 to integrator tolerance. (Tests: integrator has no bug.)
2. WKB reduction: Method A matching conditions reduce to WKB in adiabatic limit. (Tests: analytic matching is correctly implemented.)
3. Stokes-phenomenon: report subdominant-exponential coefficient near turning points. (Tests: connection formulas not miscounted.)
4. Energy conservation: (H^2/epsilon) × (F_amp × F_amp*) drift across a control interval. (Tests: Wronskian preservation.)

**Notes from scrub**: Nazarewicz contributed the propagated-error PASS threshold (replacing "5%"). Transit contributed the per-method regime-of-validity diagnostics and the DOP853 integrator pin. Lizzi contributed the POWER-RATIO pin for F_amp reporting. Gen-Physicist forced Method A and Method B to implement different mode equations so the gate tests physics, not implementation coincidence.

---

### W1-C: BACKREACTION-SELFCONSIST  [VERDICT: RE-REGISTER]

**Convention pins**:
- F_amp^{sc} as POWER RATIO (same convention as W1-A/W1-B).
- rho_particles/rho_bg computed at conformal time N_end.
- "6858" reference is power-ratio, not amplitude or amplitude-squared.
- Primary method: 2PI effective action at 2-loop (Berges 2002 / Transit-Dynamics paper 10/26) OR Hartree with damping parameter eta ∈ [0.3, 0.7] and pre-registered eta scan.
- UV regulator, IR cutoff, Bunch-Davies vacuum at iteration-0: all pinned upfront before run.

**Pre-registered gate**:
- **HYPOTHESIS**: Self-consistent closure of the mode equation yields F_amp^{sc}(k_pivot) that differs from the linearized 6858 by a calculable factor; rho_particles/rho_bg remains < 1 throughout the trajectory at convergence.
- **Pre-registered expected value**: Hartree closure of a Bunch-Davies squeezed state typically gives ~30% reduction (Gen-Physicist). Pre-register F_amp^{sc}(k_pivot) ~ 5000 ± factor 2 as the prior-expectation PASS band.
- **PASS**: (1) Iteration convergence demonstrated: |F_amp^{sc}_{n+1} − F_amp^{sc}_n| / |F_amp^{sc}_n| < 1% for 10 consecutive iterations. (2) rho_particles/rho_bg < 0.1 throughout trajectory at convergence. (3) F_amp^{sc}(k_pivot) ∈ [3428, 13716] (factor 2 of linearized 6858 — Gen-Physicist band). Linearization is quantitatively valid. Replace the original "factor 10" with this explicit validity criterion.
- **INFO**: rho_particles/rho_bg ∈ [0.1, 1] at some point in trajectory but self-consistent F_amp^{sc} is well-defined; OR F_amp^{sc} in [343, 3428] (1-OOM reduction). Report and defer interpretation to synthesis.
- **FAIL-with-caveat**: F_amp^{sc} in [6.9, 343] (2-3 OOM reduction) — backreaction is material and the S77 overproduction narrative loses its F_amp factor.
- **FAIL (SPT-confirmed)**: F_amp^{sc} ∈ [0, 6.9] — energy-conservation bound saturated; SP-Transit's "F_amp = O(1)" reading is confirmed. Branch C in the Decision Point fires.
- **INCOMPUTABLE**: If Hartree oscillates AND 2PI oscillates or fails to close AND Kadanoff-Baym with Markovian kernel fails. Apply energy-conservation bound F_amp^max (analytical, guaranteed to converge) and explicitly report verdict as INCOMPUTABLE-FALLBACK-TO-BOUND. This is NOT equivalent to FAIL.

**Convergence / validity criteria (MANDATORY)**:
- Relative change in F_amp^{sc}(k_pivot) < 1% over 10 consecutive iterations.
- rho_p(t)/rho_bg(t) < 1 throughout trajectory at the converged state.
- Energy conservation: |rho_p(t) + rho_bg(t) − initial total|/initial total < 1% over full trajectory.

**Fallback policy (pre-registered, Transit)**:
- Primary: 2PI 2-loop effective action.
- If 2PI oscillates: switch to constrained HFB with Nazarewicz-style damping eta ∈ [0.3, 0.7]; require stability across eta scan within 10%.
- If damped Hartree fails: Kadanoff-Baym with 1-loop Markovian kernel.
- If all three fail: report INCOMPUTABLE-FALLBACK-TO-BOUND with the analytical F_amp^max.

**Cross-checks**:
1. Regularization-scheme independence: compare Pauli-Villars / hard cutoff / dim-reg / lattice L_max cutoff; F_amp^{sc}(k_pivot) shifts < 10%. (Tests: UV sensitivity.)
2. Quasiparticle-quasihole symmetry (nuclear-HFB analog): E_alpha ↔ -E_alpha preserved at each iteration. (Tests: Bogoliubov-response structure.)
3. Energy-budget accounting at each N (Tests: no missing self-energy term.)
4. IR cutoff dependence k_min ∈ {1e-4, 1e-3, 1e-2} × k_pivot; F_amp stable within 5%. (Tests: IR sensitivity.)
5. Linearization recovery: setting Hartree self-energy to zero reproduces S77 linearized 6858 within 1%. (Tests: the baseline control.)
6. The scheme-invariant ratio F_amp^{sc}(k_pivot) / F_amp^{sc}(k=0) (Lizzi scrub W1-C alternative) — tests whether tilt is preserved under backreaction.

**Notes from scrub**: Transit contributed the central 2PI prescription, the damped-Hartree fallback, the INCOMPUTABLE verdict, and the Branch-C preservation mechanism. Nazarewicz contributed the BMA framing (F_amp^{sc} as MAP estimate with iteration-residual uncertainty). Lizzi contributed the POWER-RATIO pin on "6858." Gen-Physicist contributed the four disjoint PASS/INFO/FAIL bands and the prior expected-value ~5000 with factor-2 tolerance.

---

### W1-D: MULTI-BAND-E_COND  [VERDICT: RE-REGISTER]

**Convention pins**:
- Canonical E_cond is the f* scheme value; 72× threshold is in f*.
- PW sector indexing: (0,0), (1,0), (0,1), (1,1); 96-dim space indexed first by sector, then by 24-dim internal rep.
- Inter-sector coupling sign structure (s++ vs s+−) determined by diagonalizing coupled Eliashberg equations, NOT by assumption (Transit).
- Josephson coupling sign convention pinned before run.
- tau_min expected in [0.40, 0.60] (Gen-Physicist prior; near pre-fold saddle).

**Pre-registered gate**:
- **HYPOTHESIS**: E_cond^{multi, f*}(tau_w=0.05) / E_cond^{(0,0), f*}(tau_w=0.05) ≥ 72 AND V_eff^{multi, f*}(tau) has a local minimum tau_min in [0.40, 0.60] with d^2V_eff/dtau^2 at tau_min > pre-registered curvature (to be stated before run).
- **PASS**: Both conditions hold in the physical (energy-preferred, not maximally-constructive) sign configuration. Report the same ratio in SDW and zeta as Level 2 cross-check.
- **FAIL**: No minimum in [0.19, 0.70] OR ratio < 10. Single-band bottleneck confirmed structurally.
- **INFO**: Minimum outside the narrowed [0.40, 0.60] window but inside [0.19, 0.70]; OR ratio in [10, 72]; OR s++ is energetically preferred but does not deliver 72× (indicating Leggett-mode structure is different from framework prior).
- **INCOMPUTABLE**: Multi-sector BdG ED convergence fails at any tau point in the scan.

**Cross-checks**:
1. Single-band limit reproduces S36 (0,0) E_cond within 1%. (Tests: method reduction.)
2. E_cond^{multi}/E_cond^{single} within 1.3% across schemes (ratio-FI at Level 2, per-branch). (Tests: R-protection.)
3. Hermiticity and sum rules on 96×96 block. (Tests: assembly correctness.)
4. Gap-equation self-consistency: multi-channel Eliashberg solved to iteration residual < 1e-3.
5. Leggett-mode consistency: if s+− is preferred, omega_L(multi) must stand in a pre-registered relationship to omega_L1; state which relationship before run. (Tests: Leggett physics is diagnosed, not asserted.)
6. Sign structure: report inter-sector phase differences (0 for s++, π for s+−); cross-reference with W3-D. (Tests: sign structure is derived from diagonalization.)

**Notes from scrub**: Nazarewicz flagged the 72× uncertainty (S77 W1-A) and kept the gate. Lizzi pinned the canonical scheme (f*) for the threshold. Transit contributed the s++/s+− diagonalization requirement. Gen-Physicist narrowed tau_min to [0.40, 0.60] with pre-registered curvature.

---

### W1-E: PRE-FOLD-VACUUM-STATE  [VERDICT: RE-REGISTER]

**Convention pins**:
- S_IC(k) = |alpha_k + beta_k|^2 (Section 0.5 pinned; NOT |alpha_k − beta_k|^2, NOT |alpha_k|^2 − |beta_k|^2).
- Ordering of IC principles: PRIMARY is spectral stationarity (Transit canonical; minimizes Tr(ρ · D_K^2)). Cross-checks: minimum entropy, AZ topology.
- Bogoliubov-coefficient sign convention alpha + beta (not −) pinned in script header.
- Airy-function turning-point matching implementation pinned.
- L_max = 10, f* scheme.

**Pre-registered gate**:
- **HYPOTHESIS**: Under the canonical IC principle (spectral stationarity) and S_IC = |α + β|^2, S_IC(k_pivot) can be reported with full tag 4-tuple. The other two IC principles cross-check within factor 2 — this is the secondary test (not the primary).
- **PASS**: S_IC(k_pivot) canonical value lies in [10^{-10}, 10^{-9}] AND cross-check principles (min-entropy, AZ) agree with canonical within factor 2. IF ambient substrate considerations force a different IC principle (see DISAGREEMENT BLOCK), re-register accordingly.
- **INFO**: Canonical value in [10^{-9}, 10^{-2}] (partial suppression; gap reduced but not closed); OR cross-check principles agree with canonical within factor 2-100 (IC underdetermined at a moderate level).
- **FAIL**: Canonical S_IC ∈ [0.1, 1] (pre-fold is NOT a meaningful A_s suppression channel); OR canonical principle disagrees with EITHER cross-check by factor > 100 (IC selection is axiomatically underdetermined — the framework has an axiomatic gap, not a numerical problem).
- **INCOMPUTABLE**: Tachyonic turning-point integration fails convergence at any tau in the scan AND all three Airy-matching variants diverge. The pre-fold substrate state cannot be computed under the current framework axioms.

**Cross-checks**:
1. Adiabatic recovery: with fold replaced by slow adiabatic evolution, all three principles give α=1, β=0, S_IC=1. (Tests: BD limit.)
2. First-order phase-transition signature: dS_bare/dtau discontinuous at tau_fold. (Tests: fold reality.)
3. Level-crossing count at fold consistent with 59.8 GGE pair prediction. (Tests: GGE structure preserved.)
4. Non-BD squeeze scheme-invariance: S_IC must be Level 1 FI if non-BD squeezing is FI (S69 Lizzi memory). (Tests: the FI claim.)
5. Principle-ordering stability: 10% perturbation of pre-fold spectral action must not flip the ordering of the three S_IC values. (Tests: robustness.)
6. Scheme-invariant ratio S_IC(k_pivot)/S_IC(k=0): report as a convention-independent alternative diagnostic. (Tests: whether squeezing is concentrated at k_pivot.)

**DISAGREEMENT BLOCK — IC-principle selection**:
- **Gate ID**: W1-E
- **Transit position**: A 32-OOM spread across three IC principles (as encountered in the S78 execution that was tossed) is NOT a Bayesian Model Averaging problem; it is a **framework-level axiomatic gap**. The three principles (spectral stationarity, minimum entropy, AZ topology) are INEQUIVALENT DEFINITIONS of "pre-fold vacuum" in a substrate that does not yet have an FRW scale factor. Transit's recommended resolution: pre-register **spectral stationarity** as THE canonical principle (substrate-framing consistency; Parker/Birrell-Davies adiabatic vacuum analog; Volovik 3He-A parent-system BCS ground-state stationarity; Jacobson horizon-thermodynamics stationarity demand). Minimum entropy and AZ-topology become cross-checks, not alternatives. Before re-run, the user must formally adopt this axiom.
- **Nazarewicz position**: Three IC principles are three prior models on the same physical quantity. Bayes-factor comparison between them (adapted to model-selection vs parameter-estimation) is the correct methodology. If the three are treated on equal prior, posterior S_IC is the weighted average; if one is strongly preferred on prior (e.g., AZ topology — respects a proven theorem), Bayes factors weight it higher. This is a computable specification; no axiom needs to be adopted before re-run.
- **Lizzi position** (intermediate): AZ-topology principle is the framework default because substrate's AZ class is a structural feature (permanent theorem [J, D_K]=0, CPT class BDI). If cross-checks disagree with AZ by > factor 2, flag as IC-underdetermined INFO, but do NOT select a different principle.
- **Implication for plan**:
  - Axiomatic gap (Transit): needs a user-level selection rule BEFORE any re-run; the re-run adopts the selected principle as canonical and the other two as cross-checks with INFO verdict if they disagree.
  - BMA (Nazarewicz): is a computation the plan can specify; re-run reports a posterior, not a point estimate, and the gate verdict is on posterior mass in the [10^{-10}, 10^{-9}] band.
  - AZ-default (Lizzi): needs no user decision but accepts a specific risk — if AZ disagrees with the two cross-checks, the framework absorbs the disagreement as INFO and does NOT adopt their value.
- **USER DECISION REQUIRED**: Which IC principle is canonical for the framework, and is the choice axiomatic (Transit), Bayesian-weighted (Nazarewicz), or theorem-justified with cross-check INFO (Lizzi)? This plan defaults to **spectral stationarity (Transit canonical)** PROVISIONAL until the user decides.

**Notes from scrub**: Lizzi contributed the |α+β|^2 correction. Transit contributed the axiomatic-gap diagnosis. Nazarewicz contributed the BMA posterior framing. Gen-Physicist contributed the independence-of-principles skepticism (all three may select the same rho in ground-state limit). User decision is needed to select between the three framings.

---

## V. Wave 2: Structural Audit and Scheme Completion (7 gates)

### W2-A: MU-EFF-96x96  [VERDICT: RE-REGISTER]

**Convention pins**:
- J-matrix normalization: graph-Laplacian sign convention pinned.
- J matrix entries use f* Josephson scheme (consistent with W1-D).
- Inter-branch coupling (B1-B2, B1-B3, B2-B3) all included (not subset).
- [0.005, 0.020] phenomenological band is in the f* scheme; re-threshold for SDW.

**Pre-registered gate**:
- **HYPOTHESIS**: Under f* J matrix with canonical 93-bond graph × 3 branches × 32 cells, the dimensionless ratio mu_eff / Tr(J) × 96 lies in a pre-registered narrow band from simplified Bethe-lattice sum; the slow eigenvector's weight distribution identifies its physical character (inter-cell coherence / intra-cell phase slip / phase gradient).
- **Pre-registered expected value**: Compute Bethe-lattice analytic estimate on the 93-bond graph; require the full 96×96 result to agree within factor 2 (Gen-Physicist).
- **PASS**: (1) mu_eff ∈ [0.005, 0.020] AND agrees with Bethe-lattice estimate within factor 2. (2) Slow eigenvector localization-length (IPR) and B1/B2/B3 weight distribution reported; the slow mode's physical character classified. (3) Slow-mode weight is concentrated on B2/B3 per framework prior (NOT automatic from graph Laplacian structure).
- **FAIL**: mu_eff outside [0.005, 0.020] OR outside factor 2 of Bethe-lattice estimate.
- **INFO**: mu_eff in band but slow-mode character cannot be cleanly classified (cluster of near-degenerate slow modes rather than an isolated mode).

**Cross-checks**:
1. 2×2 limit: reducing to B2-B3 only reproduces S77 8.58e-4. (Tests: reduction consistency.)
2. J matrix Hermiticity. (Tests: assembly.)
3. Sum rule Tr(J) = sum of eigenvalues. (Tests: linear algebra.)
4. Level-repulsion test: 1% random Hermitian noise perturbation; slow eigenvalue stable. (Tests: whether slow mode is structural vs accidental.)
5. Symmetry-block decomposition: if J commutes with any exact symmetry, slow mode sits in a specific block. (Tests: symmetry classification.)
6. Slow eigenvector {IPR, inter-cell overlap, phase-gradient content}; classify {coherence, phase-slip, gradient}. (Tests: physical interpretation, not just numerical value.)

**Notes from scrub**: Nazarewicz kept the gate. Lizzi pinned the J-matrix scheme. Transit added the slow-mode classification requirement. Gen-Physicist contributed the Bethe-lattice analytic prior and the B2/B3 localization requirement.

---

### W2-B: BCS-FORMATION-DYNAMICS  [VERDICT: RE-REGISTER — demoted to INFO + validity-check]

**Convention pins**:
- Delta_BCS canonical from f* provenance (verify in canonical_constants.py; update provenance tag if missing).
- F(Delta) = Tr(f*(D_K^2/Λ^2 + Delta^2/Λ^2)) − Tr(f*(D_K^2/Λ^2)); SDW cross-check replaces f* → sqrt.
- gamma_GL scheme-tag added to canonical_constants.
- Initial condition Delta(0) = 0 (literal zero, not small seed).

**Pre-registered gate**:
- **HYPOTHESIS**: GL dynamics from GGE seed has a pre-registered overshoot ratio (peak/equilibrium) from the damping coefficient gamma_GL.
- **Pre-registered expected value**: Overshoot ∈ [1.1, 1.5] (literature on GL quench; Gen-Physicist). If outside this band, either the GL coefficient's provenance or the GGE seed structure is mis-identified.
- **PASS**: Overshoot ∈ [1.1, 1.5] AND Delta(t → ∞) matches canonical Delta_BCS within 5% AND t_eq consistent with canonical t_BCS.
- **FAIL**: Trajectory shows Delta(t) decays to zero (contradicts S77 BCS timing PASS); OR overshoot > 2 (GL coefficient provenance wrong); OR t_eq > 10 × t_BCS (GL closure insufficient).
- **INFO**: Overshoot in [1.0, 1.1] or [1.5, 2.0]; report with sensitivity to GL coefficient.
- **INCOMPUTABLE**: Full-BdG validity check (Transit: compute Delta(t)-Delta_GL(t) at t < t_eq/10) shows mismatch > 10% — GL dynamics is inadequate in the GGE regime and BdG time-evolution must be used instead.

**Convergence / validity criteria**:
- Method validity: compare GL trajectory to short-time BdG; if mismatch > 10% at t < t_eq/10, switch method (BdG replaces GL).
- Stiffness-parameter sensitivity: gamma_GL varied by factor 2 each way; trajectory features scale as gamma_GL^1 in t_eq while overshoot is scale-invariant.

**Cross-checks**:
1. Delta(t → ∞) matches canonical Delta_BCS within 5%. (Tightened from ambiguous "matches.")
2. Luttinger superselection [H_BCS, N_pair] = 0 preserved during dynamics. (Tests: blocking consistency.)
3. GL-vs-BdG short-time comparison (Transit). (Tests: method validity.)
4. Stiffness scaling: t_eq scales as gamma_GL^1; overshoot scale-invariant. (Tests: GL closure self-consistency.)

**Notes from scrub**: Nazarewicz correctly diagnosed the original as VACUOUS ("PASS INFO by convention"). Gen-Physicist contributed the [1.1, 1.5] overshoot prior band turning this into a discriminating gate. Transit contributed the GL-vs-BdG validity diagnostic. Lizzi added the scheme-tag discipline.

---

### W2-C: ZETA-JOSEPHSON  [VERDICT: RE-REGISTER]

**Convention pins**:
- Phi_J perturbation amplitude: 10^{-4} × M_KK; second-derivative central finite difference stencil 5-point with step 10^{-5} × M_KK.
- Zeta-regulator convention in a_4(D_K + Phi_J) expansion pinned.
- R-protection is STRICTLY per-branch (within C2, within su2, within u1); cross-branch ratios are Level 3 (scheme-dependent), NOT R-protected.

**Pre-registered gate**:
- **HYPOTHESIS**: Per-branch R-protection holds: J^{zeta}/J^{SDW} within each of branches C2, su2, u1 to 2%. Additionally: J^{zeta} computed INDEPENDENTLY (not via R-protection identity) must match the R-protection prediction within 2%.
- **Pre-registered expected value**: Per-branch drift < 1.3% (documented S74 R-protection result); cross-branch ratios can drift up to ~1.3% but are NOT gated.
- **PASS**: All three within-branch ratios within 2% AND direct zeta trace matches R-protection prediction within 2%.
- **FAIL**: Any within-branch ratio > 5%; OR direct zeta trace disagrees with R-protection prediction by > 5% (implementation bug, not theorem violation).
- **INFO**: 2-5% within-branch drift (consistent with L_max drift only).
- **INCOMPUTABLE**: Finite-difference stencil returns non-convergent derivative across step-sizes {10^{-4}, 10^{-5}, 10^{-6}} × M_KK.

**Cross-checks**:
1. Reproduce S70 SDW Josephson in SDW limit. (Tests: reduction.)
2. Ratio J_C2 / J_su2 consistent with Dynkin ratio 20/9 from T_1/T_3. (Tests: representation-theoretic content.)
3. omega_L^{zeta}/omega_L^{SDW} matches R_1 drift 0.053 OOM. (Tests: Leggett mode preservation.)
4. Phi_J sensitivity: vary amplitude by factor 2; J^{zeta} extraction stable. (Tests: non-linear bleed.)

**Notes from scrub**: Lizzi contributed the per-branch vs cross-branch distinction (critical). Gen-Physicist contributed the "direct zeta trace vs R-protection prediction" implementation test (otherwise R-protection PASS is guaranteed if the identity is used). Nazarewicz kept the gate.

---

### W2-D: F-CONV-ANOMALY  [VERDICT: RE-REGISTER]

**Convention pins**:
- Anomaly-derived cutoff: SHARP cutoff with Mellin weights f_0 = 1/2, f_2 = 1, f_4 = 1, f_n = 0 for n > 4 (Andrianov-Lizzi arXiv:1103.0478). FORCED by the anomaly derivation, NOT a free choice.
- For f*-scheme comparison: Mellin weights {f_0^{f*}, f_2^{f*}, f_4^{f*}} numerically computed; NEW canonical_constants entries `mellin_f_star_{f0,f2,f4}`.
- Zeta: f_0^{zeta} ≡ 0 (structural CC-elimination).
- Heat-kernel cutoff, coincidence-limit renormalization subtraction scheme: pinned upfront.

**Pre-registered gate**:
- **HYPOTHESIS**: f_conv^{anomaly, sharp} with (f_0=1/2, f_2=1, f_4=1) lies in the 3-scheme cluster {f_conv^{SDW}, f_conv^{zeta}, f_conv^{anomaly, sharp}} with spread < factor 1.5 (not 2). Additionally: f_conv^{anomaly, f*-weights} with numerically computed f*-Mellin weights agrees with f_conv^{f*} within factor 1.5.
- **Pre-registered expected value**: Specific numerical prediction for f_conv^{anomaly} from the published Lizzi arXiv:1103.0478 formula evaluated on the D_K L=10 spectrum. This value must be computed and pre-registered BEFORE the gate runs (Gen-Physicist).
- **PASS**: 3-scheme spread < factor 1.5 AND anomaly-with-f*-weights agrees with f* within factor 1.5 AND computed f_conv^{anomaly} matches the pre-registered formula prediction within factor 1.5.
- **FAIL**: 3-scheme spread > factor 5; OR anomaly-with-f*-weights disagrees with f* by > factor 5.
- **INFO**: Spread factor 1.5-5 — identify which Mellin weight causes the drift.
- **INCOMPUTABLE**: The Lizzi published formula cannot be instantiated on the framework's Jensen-deformed D_K (e.g., normalization factors don't close dimensionally on the Jensen metric).

**Cross-checks**:
1. Dimensional consistency ([f_conv] = M^{-2}). (Tests: unit coherence.)
2. Single-mode-spectrum limit: all three schemes identical. (Tests: scheme reduction.)
3. f_conv^{zeta}/f_conv^{SDW} = 1/R_1 per S76 R2 identity. (Tests: R-protection preservation.)
4. The scheme-invariant ratio f_conv^{anomaly, sharp}/f_conv^{SDW} (Lizzi scrub W2-D alternative) is a pure Mellin-weight ratio — a structural scheme-consistency test at the functional level, not the spectrum level.

**Notes from scrub**: Lizzi contributed the critical f_0 = 1/2 forcing and the sharp-cutoff pin (the single most important correction in Wave 2). Gen-Physicist contributed the pre-computed formula-prediction requirement (tightening from factor 2 to factor 1.5). Nazarewicz kept. Transit's scrub flagged f_conv convergence-dependence on kernel smoothness properties.

---

### W2-E: F-CONV-SUBHORIZON  [VERDICT: RE-REGISTER]

**Convention pins**:
- Canonical scheme: f*. Cross-checks in SDW and zeta.
- Mode-integral UV regulator, horizon-crossing-vs-subhorizon-phase cutoff: pinned upfront.
- Which k_pivot/aH value: either 14.7 from S77 or recomputed from W1-B — state upfront.
- F_amp exponent in the c_sub integrand: POWER RATIO (Gen-Physicist flag; the subhorizon correction cannot float between F_amp^1 and F_amp^2).
- f_conv dimensionless in (M_Pl_red)^{-2} units.

**Pre-registered gate**:
- **HYPOTHESIS**: Subhorizon correction factor c_sub(k_pivot) = f_conv(k_pivot)/f_conv(k=0) in the f* scheme lies in [0.5, 2.0]; cross-scheme spread (f*, SDW, zeta) < factor 1.5.
- **PASS**: c_sub^{f*}(k_pivot) ∈ [0.5, 2.0] AND c_sub^{SDW}(k_pivot) ∈ [0.5, 2.0] AND the two agree within 10%.
- **FAIL**: c_sub^{f*}(k_pivot) outside [0.1, 10]; OR cross-scheme spread > factor 10.
- **INFO**: c_sub^{f*} in [0.1, 0.5] or [2, 10]; OR scheme disagreement 10-100%.
- **INCOMPUTABLE**: Cross-scheme spread > factor 10 — the "subhorizon correction" concept is scheme-dependent at OOM level and the calculation has unspecified meaning.

**Cross-checks**:
1. k → 0 limit recovers S75 f_conv^{SDW} exactly. (Tests: scheme-consistency baseline.)
2. Smooth across CMB range k ∈ [1e-4, 1] Mpc^-1. (Tests: no pathological k-dependence.)
3. Consistent with f_conv^{zeta}/f_conv^{SDW} = 1/R_1 in superhorizon limit. (Tests: R-protection preservation.)

**Notes from scrub**: Lizzi contributed the scheme-canonical pin. Transit contributed the cross-scheme spread INCOMPUTABLE verdict. Nazarewicz kept. Gen-Physicist explicitly flagged the F_amp exponent as the S77 convention-shopping failure point — resolution is Section 0.1.

---

### W2-F: A_4-R^2-UNDER-F-STAR  [VERDICT: RE-REGISTER]

**Convention pins**:
- a_4 identity: a_4^{f*} = f_4^{f*} × a_4^{HK}, where a_4^{HK} is the bare HK coefficient with Gilkey-universal coefficients.
- Gilkey decomposition performed on a_4^{HK} (scheme-independent), not on a_4^{f*}.
- Metric: Jensen-deformed SU(3) fiber at canonical tau = 0.190; Gilkey expansion in normal coordinates, second-order curvature invariants.
- Lambda cutoff convention; Gilkey basis expansion order (a_8 cross-check yes/no): pinned.

**Pre-registered gate**:
- **HYPOTHESIS**: a_4^{HK} (bare, scheme-independent) is R^2-dominated at > 90%; the f*-scheme rescales by the Mellin multiplier f_4^{f*} without changing the relative fractions.
- **Pre-registered expected value**: Specific numerical R^2 coefficient under f* computed from the f*(x) = 0.912√x + 0.088 exp(-x) response on D_K^2 spectrum (Gen-Physicist). Pre-register this value (e.g., 98%) BEFORE the gate runs.
- **PASS**: R^2 fraction of a_4^{HK} > 90% AND |Ric|^2 + |Riem|^2 fractions < 10% AND the pre-registered specific R^2 coefficient under f* is matched within 5%.
- **FAIL**: R^2 fraction of a_4^{HK} < 50% (different invariant dominates); OR the f* R^2 coefficient deviates from pre-registered value by > 10%.
- **INFO**: R^2 fraction in [50%, 90%]; report second-dominant invariant.

**Cross-checks**:
1. a_4^{f*}/a_4^{SDW} ratio matches documented f*-family result. (Tests: Mellin-multiplier correctness.)
2. Cross-term decomposition: R·|Ric|, R·|Riem|, |Ric|·|Riem| — a pure-R^2 f* is structurally different from one where cross-terms cancel to produce 90% R^2 (Nazarewicz).
3. a_4 itself matches a_4^{SDW} up to R_1 = 0.053 OOM. (Tests: scheme-invariance up to R-protection.)

**Notes from scrub**: Lizzi contributed the HK-identity decomposition (the Gilkey fractions are scheme-invariant in the HK decomposition; the Mellin multiplier is only a rescaling). Gen-Physicist contributed the pre-registered specific f* R^2 coefficient requirement. Nazarewicz added the cross-term scrutiny.

---

### W2-G: EPS-ZERO-MATCHING  [VERDICT: RE-REGISTER]

**Convention pins**:
- Epsilon = 0 is a COORDINATE singularity of the Mukhanov variable z = a·√(2·epsilon)·M_Pl, NOT a physical singularity. a''/a is smooth there.
- Primary variable: scalar field phi (NOT Mukhanov u = a·ζ·√(2·epsilon)·M_Pl).
- Integrate mode equation for delta_phi through epsilon = 0 WITHOUT singular change of variables (Transit; cite Motohashi paper 19).
- Secondary diagnostic: |beta| in zeta gauge via ratio zeta = delta_phi / (dphi/dN) to confirm gauge-invariance.
- Epsilon definition: eps_H = -dH/dN / H^2 (not eps_V) pinned.

**Pre-registered gate**:
- **HYPOTHESIS**: |beta_k^{(2)}(k_pivot)|^2 < 0.01 in the scalar-field phi variable; no physical particle creation at epsilon = 0; slow-roll parametrization error is controlled.
- **PASS**: |beta_k^{(2)}|^2_phi < 0.01 AND phi-variable and zeta-gauge computations agree (gauge-invariance preserved).
- **FAIL**: |beta_k^{(2)}|^2_phi > 1 AND result is consistent between phi and zeta gauges (physically competitive particle creation at epsilon=0).
- **INFO**: |beta_k^{(2)}|^2 ∈ [0.01, 1]; report.
- **INCOMPUTABLE**: phi and zeta gauge results disagree at the relevant level (gauge-invariance failure in numerical treatment) — integration scheme is inadequate.

**Cross-checks**:
1. Smooth limit as epsilon → 0 from either side in the phi variable. (Tests: the claim that the singularity is coordinate, not physical.)
2. Consistent with W1-B mode equation integration at N_turn. (Tests: method linkage.)
3. Adiabaticity parameter omega/omega_dot at N_turn computed; |beta^{(2)}|^2 compared to adiabatic bound exp(-2πω/|omega_dot|).
4. N_turn sensitivity: small variation in N_turn definition does not flip the gate verdict (Nazarewicz).

**Notes from scrub**: Transit contributed the core correction (scalar field phi, not Mukhanov u; the z-variable divergence is coordinate, not physical; cite Motohashi). Lizzi contributed the matching-reference pin. Gen-Physicist wanted the gate REMOVED as redundant with W1-B; this plan keeps it RE-REGISTERED because the phi-variable computation is substantively different from W1-B's mode equation at horizon exit, and the gauge-invariance cross-check is an independent test.

---

## VI. Wave 3: Diagnostic, Prediction-Layer, EVOI Recalibration (16 gates)

### W3-A: CHI_2-LMAX-CONVERGENCE  [VERDICT: RE-REGISTER]

**Convention pins**:
- Primary scheme for the gate: **SDW** (chi_2 = <sqrt(x)> identity is defined in SDW; this is the only scheme with a literature target).
- chi_2^{zeta} and chi_2^{f*} reported as INFO-level cross-checks only, not gated (no literature target in these schemes).
- Extrapolation fit forms: pre-register {L_max^{-alpha}, L_max^{-alpha}·log(L_max), Richardson} as BMA set (Nazarewicz).
- L_max achievable: declared upfront BEFORE run (avoid "reports what is feasible" moving target).

**Pre-registered gate**:
- **HYPOTHESIS**: chi_2^{SDW}(L_max → ∞) extrapolated via BMA across three fit forms returns a posterior with 68% mass in either [0.651, 0.719] (consistent with 0.685 — direct Omega_Lambda) OR [1.952, 2.158] (consistent with 2.055 — Friedmann-3 × Omega_Lambda).
- **PASS-direct**: posterior 68% mass overlaps [0.651, 0.719].
- **PASS-Friedmann**: posterior 68% mass overlaps [1.952, 2.158].
- **FAIL**: posterior falls entirely outside BOTH bands.
- **INFO** (Lizzi): L_max=15 infeasible AND extrapolation posterior width > 10% — report achievable L_max, extrapolation uncertainty, and the three fit-form values. This is NOT a PASS-equivalent.
- **INCOMPUTABLE** (Gen-Physicist): tail fit residuals show chi_sq/dof > 2 from L_max=10, 12 alone — the extrapolation is not well-posed even at achievable L_max. UNCOMPUTED, not PASS-equivalent.

**Pre-registered Bayesian UQ requirement (Nazarewicz)**: Multi-model extrapolation across the three fit forms with AIC-weighted posterior. Report (a) posterior mean, (b) posterior width, (c) fraction of mass in each target band, (d) model-averaged exponent alpha if applicable. The gate PASSes on posterior-mass overlap, not on mean-matches-target.

**Convergence criteria**:
- Tail fit: chi_sq/dof < 2 required for PASS.
- Fit-form spread: if the three forms disagree at the extrapolated value by > 5%, the extrapolation is fit-form-dependent and gate is INFO until convergence theorem is proved or higher L_max is computed.

**Cross-checks**:
1. chi_2 = <sqrt(x)> identity verified at each L_max in SDW. (Tests: identity preservation.)
2. R-protection chi_2 ratios across L_max drift < 1.3%. (Tests: R-protection at chi_2.)
3. Exponent alpha fit dimensionally consistent with rank-scaling (cross-reference W3-K). (Tests: structural consistency.)

**DISAGREEMENT BLOCK — Primary scheme for gate**:
- **Gate ID**: W3-A
- **Lizzi position**: chi_2 literature targets (0.685 and 2.055) are SDW-only; zeta and f* schemes have no literature target and are exploratory. The gate applies ONLY to chi_2^{SDW}; the other schemes are INFO-level cross-checks.
- **Nazarewicz position**: BMA extrapolation should use the posterior across all three schemes in addition to across fit forms. Scheme uncertainty is a model-form uncertainty (Paper 06) and should propagate to the gate verdict.
- **Implication**: Lizzi's framing keeps the gate sharp (one target, one scheme, BMA across fit forms only). Nazarewicz's framing widens the posterior but accommodates scheme uncertainty. Lizzi's is tighter; Nazarewicz's is more honest about model-form uncertainty.
- **USER DECISION REQUIRED**: Is chi_2 primarily an SDW quantity (Lizzi) or a BMA-across-schemes-and-fit-forms quantity (Nazarewicz)?

**Notes from scrub**: Lizzi contributed the SDW-only framing. Nazarewicz contributed the BMA requirement and the INFO-vs-INCOMPUTABLE distinction. Gen-Physicist contributed the contingency-against-L_max=15-infeasibility clause (UNCOMPUTED ≠ PASS). Transit had no dynamics flag on this gate.

---

### W3-B: FAMP-TILT-SMOOTHED  [VERDICT: KEEP with convention pin]

**Convention pins**:
- F_amp convention: POWER RATIO (Section 0.1). The original plan's implicit F_amp^2 exponent is now F_amp^1.
- Input: W1-C output (F_amp^{sc} array over k) if W1-C converges; else linearized F_amp with "superseded by backreaction" caveat.
- Smoothing: Savitzky-Golay polynomial order 3, window 7.
- k-range: [0.1, 10] × k_pivot; extrapolate slope to k_pivot by fitting.
- Slope extraction is a logarithmic derivative — CONVENTION-INVARIANT (the F_amp convention factor cancels).

**Pre-registered gate**:
- **HYPOTHESIS**: |slope| = |d ln F_amp / d ln k| at k_pivot < 0.1 under the converged F_amp^{sc} (W1-C output) or under the linearized F_amp with explicit caveat.
- **PASS**: |slope| < 0.1 from converged F_amp^{sc}.
- **FAIL**: |slope| > 0.2 after backreaction; OR slope is dominated by self-consistency effects that challenge BLV n_s = 0.9567.
- **INFO**: |slope| ∈ [0.1, 0.2]; OR W1-C returned INCOMPUTABLE and the slope is computed from linearized F_amp with caveat.

**Cross-checks**:
1. BLV n_s = 0.9567 unchanged. (Tests: Bogoliubov-invariance.)
2. Smoothing-window sensitivity: slope value for 3 polynomial orders / bandwidths; verify slope is not a smoothing artifact (Nazarewicz).
3. Under Branch-C (converged F_amp^{sc} at saturation floor): slope should be near zero by construction — this is a CONSISTENCY CHECK on Branch-C, not an independent prediction (Transit).

**Notes from scrub**: Nazarewicz, Lizzi, Gen-Physicist all KEEP. Transit contributed the W1-C dependency (sequential: W3-B runs AFTER W1-C). Lizzi pinned the POWER-RATIO convention; the logarithmic derivative is convention-invariant so this pin only matters for input-output consistency.

---

### W3-C: TENSOR-FAMP  [VERDICT: RE-REGISTER]

**Convention pins**:
- F_amp^T and F_amp^S both as POWER RATIOS.
- r formula: r = (F_amp^T × P_dS^T) / (F_amp^S × P_dS^S), with P_dS explicit (no slow-roll shortcuts).
- Tensor mode normalization (graviton polarization factor √2/M_Pl vs 2/M_Pl) pinned.
- Epsilon definition: eps_H (not eps_V) pinned.
- Same regime-treatment for F_amp^T as for F_amp^S: if W1-C produced F_amp^{sc,S}, tensor must also be recomputed with self-consistent backreaction (Transit).

**Pre-registered gate**:
- **HYPOTHESIS**: r(k_pivot) computed without slow-roll shortcut lies in a pre-registered band from the framework's a''/a pump evaluation.
- **Pre-registered expected value**: Compute a specific r ± factor 2 from the tensor mode equation under the converged F_amp^{sc,T} (or linearized F_amp^T if W1-C returned INCOMPUTABLE). Pre-register this band BEFORE run (Gen-Physicist).
- **PASS**: Computed r matches pre-registered prediction within factor 2 AND tensor backreaction diagnostic rho_T/rho_bg at peak amplification < 0.1 (linear OK) or recomputed self-consistently if > 0.1.
- **FAIL**: r = 16·epsilon(N_pivot) accidentally reproduced within 20% (substrate-framing violation per phononic-framing rule).
- **INFO**: Computed r differs from prediction by factor 2-5, with diagnostic reported; OR rho_T/rho_bg ∈ [0.01, 0.1] (mild tensor backreaction).
- **INCOMPUTABLE**: Tensor mode integrator fails control (slow-roll tensor r = 16·epsilon not reproduced in the slow-roll-control sanity check).

**Cross-checks**:
1. Slow-roll control: in the slow-roll limit, r = 16·epsilon MUST recover. Absence = miscoded tensor equation. (Tests: tensor equation correctness.)
2. r vs LiteBIRD r < 0.024 target: pre-register as a falsifiable observational prediction for post-LiteBIRD evaluation.
3. Tensor backreaction diagnostic rho_T/rho_bg at peak amplification. (Tests: linearity.)
4. Same scheme / regime consistency as F_amp^S. (Tests: sectorial coherence.)

**Notes from scrub**: Gen-Physicist contributed the specific-prediction requirement (moving from "INFO by convention" to a real gate). Transit contributed the regime-consistency-with-W1-C requirement. Lizzi contributed the POWER-RATIO pin. Nazarewicz noted the "PASS INFO by convention" was vacuous; retired.

---

### W3-D: JOSEPHSON-LEGGETT-MIXING  [VERDICT: RE-REGISTER]

**Convention pins**:
- delta Omega_DM h^2 derived FROM FIRST PRINCIPLES via integral of mixing-angle × Leggett density of states × red-shift factor — NOT a linear rescale (Nazarewicz).
- J-coupling sign convention in H_graph ⊗ H_internal + J_coupling form pinned.
- Off-diagonal B3 occupation-shift convention pinned.
- Mixing parameter (mixing angle vs off-diagonal matrix element magnitude) pinned.
- GGE multipliers λ_n consistent with S77 GGE-OCC (Transit).
- Omega_DM formula: linear GGE thermal (Section 0.7).

**Pre-registered gate**:
- **HYPOTHESIS**: |delta Omega_DM h^2| from Leggett-Josephson mixing, derived from the non-linear mixing-angle/density-of-states/red-shift integral, is in a pre-registered band from first-principles computation.
- **Pre-registered expected value**: Specific numerical delta Omega_DM h^2 from the non-linear integral; factor 2 tolerance (Gen-Physicist).
- **PASS**: Computed |delta Omega_DM h^2| matches pre-registered value within factor 2 AND scaling d(ln Omega_DM)/d(ln n_slow) is DERIVED from the relic-density calculation (not assumed unity) AND the derived exponent is consistent with GGE thermal structure.
- **FAIL**: Computed value deviates from pre-registered by > factor 5; OR scaling exponent not derivable from first principles.
- **INFO**: Computed in [factor 2, factor 5] of pre-registered value; OR scaling law non-linear and the derivation is incomplete.
- **INCOMPUTABLE**: GGE multipliers λ_n not extractable from S77 GGE-OCC; the GGE state is underspecified.

**Cross-checks** (each tests an INDEPENDENT physical consequence):
1. Mixing-angle: the WHAT of the mixing. (Tests: inter-branch J coupling.)
2. Leggett density of states: the HOW MUCH. (Tests: occupation via S77 GGE-OCC.)
3. Cosmological red-shift integration: the WHEN of DM freeze-out. (Tests: thermal history.)
4. Replace previous "Luttinger superselection" cross-check (Nazarewicz flagged as measuring the same observable as primary). Instead: direct Omega_DM estimate from thermal history is a substantively independent cross-check.
5. CPT neutrality preserved. (Tests: AZ class preservation.)
6. GGE cannot shift chi_2 (S77 W1-D permanent theorem) — verify mixing does not violate. (Tests: mixing within theorem scope.)

**Notes from scrub**: Nazarewicz flagged the "linear rescale as cross-check" error as the precise failure the plan explicitly committed (CROSS-CHECK-ERROR per prompt). Transit flagged the GGE-multiplier dependency. Gen-Physicist demanded a specific pre-registered prediction from the non-linear integral. Lizzi pinned the linear GGE thermal formula (Section 0.7).

---

### W3-E: PBH-CONSTRAINT-ASSESSMENT  [VERDICT: RE-REGISTER]

**Convention pins**:
- P_zeta(k_trans) uses F_amp as POWER RATIO (Section 0.1).
- S_IC(k_trans) uses |α+β|^2 (Section 0.5) from W1-E output.
- PBH mass function: Carr press-formula; horizon-crossing at k_trans; H(k_trans) from canonical fold parameters.
- Under Branch-C (W1-C FAIL): P_zeta at k_trans is suppressed by the same backreaction factor as at k_pivot; compute both linearized and self-consistent constraints (Transit).
- S_IC propagation: pin which IC principle's S_IC is used (per W1-E DISAGREEMENT BLOCK resolution).

**Pre-registered gate** (split into two sub-gates per Gen-Physicist):
- **W3-E-1 PRE-IC**: P_zeta(k_trans, un-IC-suppressed, linearized or W1-C self-consistent). Pre-registered expected 0.089 (linearized) or ~reduced (self-consistent). PASS if < 10^{-2}; FAIL if > 10^{-2} (confirms that raw pre-fold-and-IC power exceeds LIGO/Virgo bound and IC suppression is required).
- **W3-E-2 REQUIRED-SUPPRESSION**: Compute required S_IC,min at k_trans to meet LIGO/FIRAS. PASS if W1-E provides ≥ that much suppression; FAIL if W1-E provides less.

**Pre-registered expected values**:
- W3-E-1: P_zeta(k_trans, linearized) = 0.089 from S77 W3-O; under Branch-C (self-consistent) roughly P_zeta × F_amp^{sc}/F_amp^{linear}. This sub-gate AUTOMATICALLY FAILS if P_zeta > 10^{-2}; the question becomes "what S_IC is required."
- W3-E-2: Required S_IC,min = 10^{-2} / P_zeta(k_trans); PASS if W1-E S_IC(k_trans) ≤ required; FAIL if > required.

**Cross-checks**:
1. PBH mass function normalization against Carr press template. (Tests: PBH formalism.)
2. FIRAS mu-distortion integration over k ∈ [1, 10^4] Mpc^-1 with bound 9e-5.
3. Report P_zeta(k) × S_IC(k) as function of k across [1, 10^4] Mpc^-1; strongest constraint may come from a different k than k_trans. Gate evaluated at the most-constraining k, not k_trans by default (Nazarewicz).
4. The scheme-invariant ratio P_zeta(k_trans)×S_IC(k_trans)/P_zeta(k_pivot) — SCHEME-INDEPENDENT and CONVENTION-INVARIANT (Lizzi).

**Notes from scrub**: Gen-Physicist contributed the sub-gate split (required vs provided). Transit contributed the Branch-C suppression computation. Nazarewicz contributed the most-constraining-k requirement. Lizzi contributed the scheme-invariant ratio cross-check.

---

### W3-F: f_NL-COHERENCE-VERIFICATION  [VERDICT: KEEP with convention pin]

**Convention pins**:
- f_NL convention: Maldacena (Komatsu) standard: f_NL = (5/6) × (bispectrum / (2 × power spectrum)^2), evaluated at equilateral k_1=k_2=k_3.
- Power spectrum normalization consistent with W1-A (F_amp POWER RATIO).
- Equilateral vs squeezed vs folded template: equilateral pinned.
- H_3 vertex sign convention pinned.

**Pre-registered gate**:
- **HYPOTHESIS**: f_NL(equilateral, coherent) = 0.056 ± 20% reproducible by INDEPENDENT algebraic path (different symbolic manipulation or numerical contraction from S77's path) — not an idempotence test.
- **PASS**: Independent re-derivation returns 0.056 within 20%.
- **FAIL**: Independent re-derivation outside 20% band.
- **INFO**: 20-50% deviation; diagnose which vertex / measure differs.
- **INCOMPUTABLE**: Independent path cannot be constructed without re-using S77 intermediate expressions.

**Cross-checks**:
1. Squeezed-limit consistency relation: Maldacena's consistency requires |f_NL^{squeezed}| ~ (n_s - 1) in the BD limit. Recover this. (Tests: squeezed-limit Maldacena.)
2. Permutation symmetry. (Tests: symmetrization.)
3. Dimensional check of bispectrum integral. (Tests: unit coherence.)

**Notes from scrub**: Nazarewicz, Lizzi, Gen-Physicist all KEEP. Transit flagged the regime-consistency requirement: f_NL must be in the same regime as the F_amp used (linearized or self-consistent). Verify with W1-C output regime. Lizzi pinned the f_NL convention.

---

### W3-G: DESI-DR3-UPDATE  [VERDICT: RE-REGISTER]

**Convention pins**:
- a_0 / dilaton mixing formula version (S74 vs S77) pinned.
- DESI DR3 data version pinned.
- w_0, w_a likelihood prior family pinned.
- f_conv scheme in the w_0, w_a tree: SDW (canonical_constants.py provenance default; Lizzi).
- Compute w_0, w_a FROM SCRATCH using (a) post-fold a_0 and dilaton formulas, (b) with N_pivot = 3.12 only feeding into F_amp (which does not enter w_0, w_a by the framework's mechanism). DO NOT load w0_FW from canonical_constants as both "pre" and "post" — that is the original tautology (Nazarewicz).

**Pre-registered gate**:
- **HYPOTHESIS**: The physics claim "w_0, w_a depend on post-fold a_0 and dilaton mixing, NOT on N_pivot or F_amp" is verified by explicit partial derivatives d w_0 / d F_amp and d w_a / d F_amp being numerically zero within partial-derivative precision. Additionally: w_0, w_a extracted from the post-fold a_0(tau) trajectory match DESI DR3 likelihood at > 1-sigma (Gen-Physicist).
- **PASS**: |d w_0 / d F_amp| < 0.001 and |d w_a / d F_amp| < 0.001 as numerical partials of F_amp(k_pivot) variation ±50% AND w_0, w_a from post-fold trajectory within 1-sigma of DESI DR3.
- **FAIL**: Either partial exceeds 0.001 (F_amp does propagate and the mechanism claim is wrong); OR w_0, w_a deviate from DESI DR3 by > 2-sigma.
- **INFO**: Partials in [0.001, 0.01]; OR w_0, w_a within 1-2 sigma of DESI DR3.

**Cross-checks**:
1. Pre-S77 DESI prediction reproduced at F_amp = F_amp_pre-S77. (Tests: pre-S77 consistency.)
2. Post-fold a_0 functional-independence (S66 FUNCTIONAL-INDEPENDENT permanent theorem) verified. (Tests: functional-independence reliance.)
3. Explicit numerical partial derivative d w_0 / d F_amp computed (not asserted to be zero).

**DISAGREEMENT BLOCK — Structural form**:
- **Gate ID**: W3-G
- **Nazarewicz position**: RE-REGISTER with explicit numerical partial-derivative computation plus fresh DESI extraction.
- **Gen-Physicist position**: REMOVE — this is structurally the S78 audit Pattern 3 (load-and-compare-to-self); even the RE-REGISTER form risks being a post-hoc fix of a gate that was conceptually broken. Replace with a substantive DESI test (fresh a_0(tau) extraction).
- **Lizzi position**: KEEP with f_conv scheme pin.
- **Implication for plan**: Nazarewicz's framing converts the original tautology into a real test of the propagation claim; Gen-Physicist's framing replaces the gate with a different DESI test. The two are not contradictory — Nazarewicz's version tests "N_pivot does not propagate"; Gen-Physicist's version tests "the framework's w_0, w_a match DESI." Both CAN be tested as two sub-gates. This plan adopts the merged approach above (both sub-hypotheses are PASS criteria).
- **USER DECISION REQUIRED**: Merge both sub-tests, or pick one? Plan default is merge.

**Notes from scrub**: Nazarewicz diagnosed the tautology (Pattern 3 from the audit). Gen-Physicist proposed REMOVE. Lizzi contributed the f_conv scheme-pin. Transit had no dynamics flag.

---

### W3-H: CMPP-AT-TAU-0.537  [VERDICT: RE-REGISTER]

**Convention pins**:
- CMPP convention (Coley-Milson-Pelavas-Pravda vs simplified variant) pinned.
- Weyl-tensor convention (Newman-Penrose vs Bel-Robinson decomposition) pinned.
- Perturbation size for the ansatz-breaking test pinned.

**Pre-registered gate** (recast per Nazarewicz):
- **HYPOTHESIS**: CMPP Type D persists at tau = 0.537 under a small, pre-specified, NON-TRIVIAL perturbation of the static M^{3,1} × K^8 product ansatz (e.g., small dilatation of the 4D–K cross-block mixing, or a non-block-diagonal Riemann component). The pure ansatz case is construction-forced PASS (ANSATZ-FORCED per the S78 audit) and NOT a physics test.
- **PASS**: Under the pre-registered non-trivial perturbation, CMPP Type D persists to first order in the perturbation parameter. Specifically: a pre-registered non-linear CMPP-invariant (e.g., a specific scalar invariant vanishing, or an eigenvalue degeneracy of the Weyl operator) vanishes/is-non-zero within a pre-registered tolerance at tau = 0.537 under the perturbed geometry.
- **FAIL**: Type D breaks under the small perturbation (Type II or Type I emerges).
- **INFO**: Type D persists under the perturbation but the pre-registered CMPP-invariant is ambiguous at tau = 0.537 (fails to distinguish from boundary values).
- **INCOMPUTABLE**: The perturbed Weyl tensor computation diverges or returns non-physical components; the perturbation amplitude is too small or too large.

**Cross-checks**:
1. In the exact block-diagonal (unperturbed) case, Weyl^2 trivially non-negative and Bel-Robinson has prescribed structure; verify. (Tests: baseline.)
2. Sectional curvature C^2 = 0 at tau = 0.537 reported as a scalar number with numerical resolution. (Tests: the interesting geometric feature.)
3. A pre-registered CMPP-related observable (Gen-Physicist) detects C^2 = 0 — i.e., the gate tests whether a non-trivial geometric fact is detected by a CMPP invariant.

**DISAGREEMENT BLOCK — REMOVE vs RE-REGISTER**:
- **Gate ID**: W3-H
- **Gen-Physicist position**: REMOVE. Without a pre-registered non-trivial invariant that could distinguish tau = 0.537 from other tau, the gate is construction-forced. If a non-trivial invariant exists, that's a different gate.
- **Nazarewicz position**: RE-REGISTER as the ansatz-breaking perturbation test above.
- **Lizzi position**: no-flaw (CMPP is purely geometric, scheme-independent).
- **Implication for plan**: Gen-Physicist's REMOVE is structurally cleaner; Nazarewicz's RE-REGISTER makes a substantive geometric test possible. If no pre-registered CMPP invariant can be constructed that distinguishes tau = 0.537, the gate should be REMOVED. Plan default: RE-REGISTER with the perturbation test; if that test cannot be specified before run, demote to REMOVE.
- **USER DECISION REQUIRED**: Keep as ansatz-breaking perturbation test, or remove?

**Notes from scrub**: Nazarewicz explicitly identified this as Pattern 1 ANSATZ-FORCED (per S78 audit) and proposed the perturbation-breaking test. Gen-Physicist advocated REMOVE. Lizzi noted scheme-independence. Transit had no dynamics flag.

---

### W3-I: EVOI-RECALIBRATION-78  [VERDICT: KEEP — labeled META/PROCESS, not a physics gate]

**Convention pins**:
- EVOI methodology per `.claude/rules/evoi-prioritization.md`.
- P(pass) elicitation procedure pinned before populating.
- EVOI computed using the SCRUBBED gate verdicts (per this plan), NOT the original plan's verdicts.
- P(pass) for each EVOI item reflects probability under the pinned convention.

**Pre-registered deliverable**:
- **HYPOTHESIS** (procedural): Updated `sessions/evoi-framework.md` with S78 stamp, all closed items removed, all new items from S78 Wave 1+2 added with P(pass) and delta_P cited.
- **Acceptance** (procedural, NOT a physics gate): At least 3 items changed; all closed items removed; all S78-derived items added. (Note: this is a low bar; the realistic number is 15-30 per Gen-Physicist; report actual count.)
- **Classification**: META/PROCESS; do NOT count in physics-gate statistics.

**Cross-checks** (procedural): All S73B items either closed / carried / deprioritized with reason.

**Notes from scrub**: Nazarewicz proposed REMOVE (bookkeeping, not physics). Gen-Physicist KEEP-as-META. Lizzi KEEP. Transit n/a. Plan default: KEEP but explicitly label as META/PROCESS and exclude from physics-gate counts.

---

### W3-J: SIN2-W-NON-TREE  [VERDICT: RE-REGISTER]

**Convention pins**:
- RG scheme: MS-bar, matching standard PDG convention at M_Z.
- Input Lambda: canonical Lambda_QCD (canonical_constants).
- KK-threshold scale matching pinned.

**Pre-registered gate** (from Gen-Physicist and Nazarewicz):
- **HYPOTHESIS**: Framework tree value sin^2(θ_W) = 0.2348 (T_1/T_3 = 20/9; permanent theorem) running under 1-loop SM RG from the KK-threshold scale to M_Z produces sin^2(θ_W, M_Z) that matches 0.2312 within a pre-registered tolerance.
- **Pre-registered expected value**: Compute the expected 1-loop shift (~0.003) from the framework's KK-threshold scale; pre-register the tolerance (factor 1.5 on the shift).
- **PASS**: Computed sin^2(θ_W, M_Z) within 1-sigma of PDG 0.2312 (factor 1.5 on the shift).
- **FAIL**: Computed outside 2-sigma of 0.2312 (mechanism predicts a different value).
- **INFO**: Between 1-2 sigma; alternative mechanisms (topological anomaly matching, different threshold) reported.
- **INCOMPUTABLE**: No viable mechanism identifiable at 1-loop level.

**Cross-checks**:
1. Dynkin ratio T_1/T_3 = 20/9 respected at tree level. (Tests: tree-level permanent.)
2. SM RG running self-consistent. (Tests: method.)
3. Cross-check in alternative renormalization scheme (on-shell) — sin^2(θ_W) ratio convention-tagged.

**Notes from scrub**: Nazarewicz diagnosed VACUOUS ("PASS INFO by convention"). Gen-Physicist RE-REGISTER with specific expected shift. Lizzi added MS-bar pin. Transit n/a.

---

### W3-K: R_1-L-MAX-CONVERGENCE-CROSS-GROUPS  [VERDICT: KEEP with cross-scheme addition]

**Convention pins**:
- Primary test: rank-scaling exponent in SDW scheme.
- Cross-check: same test in f* and zeta. Rank-scaling exponent universal to 10% across schemes (Lizzi).
- L_max sampling points pinned upfront (not post-hoc chosen to fit the rank-law).
- Group-normalization (Cartan matrix convention, Dynkin labels) pinned.

**Pre-registered gate**:
- **HYPOTHESIS**: R_1 drift exponent is rank-universal in SDW to 10%; cross-schemes f* and zeta agree on the exponent to 15%.
- **PASS**: All three schemes within 15% of rank = 4 (SU(5)) and rank = 3 (Sp(3)) with tight-fit residuals.
- **FAIL**: SDW exponent > 15% off rank.
- **INFO**: SDW PASSes but f* or zeta disagree by > 15%; report group-specific residuals.

**Cross-checks**:
1. Group-specific correction test: residual deviation from rank-law scaling consistent across groups; if SU(5) residual is 10× larger than Sp(3), that is a group-specific correction (Nazarewicz).
2. Exponent alpha dimensionally consistent (cross-reference W3-A). (Tests: structural consistency.)
3. Fit residuals: scaling truly a single power law vs logarithmic corrections. (Tests: functional form.)

**Notes from scrub**: Nazarewicz, Gen-Physicist KEEP. Lizzi added cross-scheme exponent-universality. Transit n/a.

---

### W3-L: SDW-vs-ZETA-DICTIONARY  [VERDICT: RE-REGISTER — substantive content, NOT procedural]

**Convention pins**:
- "Ambiguous" defined: a_n value used in > 1 script WITHOUT scheme_tag in canonical_constants.py provenance.
- R-protection per-branch / cross-branch tagged (Lizzi).
- Candidate scripts (5-10) to audit declared BEFORE the dictionary audit runs (Gen-Physicist).

**Pre-registered gate**:
- **HYPOTHESIS**: Dictionary built; every a_n, every R-protected ratio has explicit scheme_tag AND per-branch / cross-branch tag in canonical_constants.py. Scripts that use cross-branch R-protection (treating as Level 2) are flagged as misuse.
- **PASS**: Dictionary built; all canonical constants tagged; at most 3 script misuses flagged AND corrected in-session.
- **FAIL**: > 10 script misuses flagged; OR audit finds ambiguities but fails to correct them.
- **INFO**: 4-10 script misuses; report list with proposed re-tags.

**Cross-checks**:
1. Conversion formula dimensional consistency.
2. R-protection preserved under conversion.
3. W2-K 9-OOM reproduction as sanity. (Tests: dictionary correctness.)

**Notes from scrub**: Nazarewicz proposed REMOVE (procedural). Lizzi and Gen-Physicist RE-REGISTER with substantive content (the 5-10 candidate scripts pre-audit, the per-branch / cross-branch distinction). Plan default: RE-REGISTER because the dictionary has substantive content (pinning the HK-vs-zeta-vs-SDW identities is a structural gate).

---

### W3-M: PHASE-SLIP-NULL-TEST-REGISTRATION  [VERDICT: KEEP — labeled as pre-registration, not a gate]

**Convention pins**:
- E_J computed in f* (canonical); cross-check in SDW.
- T_rh from W3-O modulus-decay; reported with its scheme tag.
- Threshold 50 justification reference cited.

**Pre-registered deliverable**:
- Pre-registration document at specified path, stating E_J/T > 50 (at both f* and SDW for robust null) as the null hypothesis, CMB-S4 sensitivity threshold, and observational signature.
- **Classification**: PRE-REGISTRATION; NOT a gate verdict. The ACTUAL gate is deferred to CMB-S4 data.

**Cross-checks** (procedural): Canonical E_cond, T_rh, E_J consistency; E_J^{f*}/T > 50 AND E_J^{SDW}/T > 50 (Lizzi).

**Notes from scrub**: Nazarewicz REMOVE (procedural). Lizzi KEEP with scheme-tag; Gen-Physicist KEEP-as-PRE-REGISTRATION. Plan default: KEEP, explicitly label.

---

### W3-N: DC-PERMANENCE-74  [VERDICT: KEEP with additions]

**Convention pins**:
- Canonical 20% DC fraction: f* provenance.
- Cells extension 4, 8, 12 in f* scheme; SDW cross-check at 8 cells only.
- "DC component" definition (zero-frequency band vs low-frequency cutoff) pinned exactly.
- Fit-form family upfront (Nazarewicz).
- 8-cell and 12-cell are FULL RE-RUNS, not extrapolations from 4-cell (Gen-Physicist).
- IR regulator test: k_min ∈ {1e-4, 1e-3, 1e-2} × k_pivot at each cell count (Transit).

**Pre-registered gate**:
- **HYPOTHESIS**: Report DC fraction at 4, 8, 12 cells. Fit DC(N_cells) = f_infinity + c × N_cells^{-gamma}. f_infinity = 0.20 ± 0.02 with fit quality chi^2/dof < 2.
- **PASS**: f_infinity = 0.20 ± 0.02 AND fit quality acceptable AND DC fraction k_min-independent at each cell count (IR artifact check).
- **FAIL**: f_infinity drifts > 0.05 away from 0.20; OR DC fraction is k_min-dependent (IR artifact not structural).
- **INFO**: Fit quality poor and extrapolation is fit-form-dependent; report which forms agree.

**Cross-checks**:
1. Sum rule on occupation. (Tests: occupation normalization.)
2. Luttinger preserved. (Tests: superselection.)
3. Cell-count scaling of computational cost reported. (Tests: finite-size convergence rate.)
4. Scheme-invariant ratio DC_fraction(12 cells) / DC_fraction(4 cells) ≈ 1 within 2% (Lizzi). (Tests: Level 2 ratio-FI.)

**Notes from scrub**: Nazarewicz KEEP with extrapolation structure. Gen-Physicist KEEP with full-re-run requirement. Lizzi added scheme restriction. Transit added IR regulator independence.

---

### W3-O: MODULUS-DECAY-74  [VERDICT: RE-REGISTER — original was VACUOUS (18 OOM margin)]

**Convention pins**:
- Instanton action S_inst: scheme-independent (topological).
- Alpha_gauge at instanton scale: f* canonical; SDW cross-check.
- Instanton-vertex normalization; tau-modulus-to-gauge-field coupling strength; Lambda-QCD at vertex scale: pinned.
- Semi-classical validity: S_inst > 10 (required); > 100 unambiguous; < 10 out-of-regime (Transit).

**Pre-registered gate** (per Nazarewicz):
- **HYPOTHESIS**: Compute T_rh from instanton vertex rate with its systematic uncertainty (instanton action ambiguity, vertex-coefficient ambiguity). Report T_rh ± delta T_rh. Framework prediction well-defined (finite, positive, with stated 1-sigma band). Compare to pre-registered framework expected value.
- **Pre-registered expected value**: Framework-predicted T_rh ~ 10^{18} MeV from instanton-mediated gauge-field production; factor 10 tolerance (Gen-Physicist).
- **PASS**: Computed T_rh within factor 10 of 10^{18} MeV AND semi-classical regime (S_inst > 10) AND compatible with BBN (trivially, as the prompt notes).
- **FAIL**: Computed T_rh differs from 10^{18} MeV by > factor 100 (indicates computational error in instanton vertex rate).
- **INFO**: Deviation 10-100× (diagnose vertex-rate source); OR semi-classical regime 10 > S_inst > 1 (boundary of validity).
- **INCOMPUTABLE**: S_inst < 1 (out of semi-classical regime).

**Cross-checks**:
1. Instanton action positive. (Tests: semi-classical reality.)
2. Reheating efficiency < 1 (bounded). (Tests: energy budget.)
3. BBN eta_B consistent. (Tests: cosmological BBN coherence.)
4. E_J(T_rh)/T_rh > 50 or < 50 — this is the substantive downstream consequence and feeds W3-M (Nazarewicz).
5. Gauge-group branching ratios: SU(3)/SU(2)/U(1) respecting group-theoretic factors (Gen-Physicist alternative).

**Notes from scrub**: Nazarewicz diagnosed this as VACUOUS (Pattern 2 from audit — 18 OOM margin cannot FAIL). Gen-Physicist RE-REGISTER with framework-predicted T_rh ± factor 10. Transit added semi-classical validity. Lizzi contributed the alpha_gauge scheme pin.

---

### W3-P: PATI-SALAM-FURTHER  [VERDICT: KEEP]

**Convention pins**:
- Rank computation threshold (eigenvalue-magnitude cutoff for "zero") pinned.
- Intermediate-symmetry candidate list (SO(10), Pati-Salam, LR, etc.) pinned upfront.

**Pre-registered gate**:
- **HYPOTHESIS**: Rank of D_K at tau < 0 shows the same obstruction as at tau > 0 (S77 W3-N permanent). No Pati-Salam-compatible rank at tau ∈ {-0.10, -0.05, 0.00}.
- **PASS**: Rank obstruction confirmed at all tested tau < 0; rank values reported.
- **FAIL**: Rank at some tau < 0 permits an intermediate symmetry (framework-level surprise).
- **INFO**: Rank at tau = 0 (fold boundary) is ambiguous.

**Cross-checks**:
1. Reproduce S77 W3-N at tau > 0. (Tests: method.)
2. Consistent with SM-unique theorem. (Tests: structural closure.)
3. Rank value reported (not just "obstruction confirmed") — the datum IS the rank integer (Nazarewicz).

**Notes from scrub**: Nazarewicz, Lizzi KEEP. Gen-Physicist asked for a physical mechanism that could give a Pati-Salam-compatible rank at tau < 0 as a pre-registered alternative — rejected because the representation-theoretic argument holds at any tau unless the pre-fold D_K has a different rep content (which is structurally unlikely). Plan default: KEEP.

---

## VII. Constraint Gates Summary (Re-registered)

| ID | Type | Verdict | Criterion (pinned) | Fires If |
|:---|:-----|:--------|:-------------------|:---------|
| S78-MASTER | Master-path | RE-REGISTER | Ledger + propagated error against 1.72e-9 | PASS/FAIL/INFO/INCOMPUTABLE |
| W1-A | Master-chain | RE-REGISTER | Single-scheme ledger, 68% posterior in PASS band | see §IV |
| W1-B | Verification | RE-REGISTER | Method A ≠ Method B equations; quadrature-sum agreement | see §IV |
| W1-C | Structural | RE-REGISTER | F_amp^{sc} in [3428, 13716] band, 10-iter convergence | see §IV |
| W1-D | Structural | RE-REGISTER | 72× + tau_min ∈ [0.40, 0.60] + energy-preferred sign | see §IV |
| W1-E | Structural | RE-REGISTER | Spectral-stationarity canonical, S_IC ∈ [1e-10, 1e-9] | see §IV + DISAGREEMENT |
| W2-A | Structural | RE-REGISTER | mu_eff in band + Bethe-lattice agreement + B2/B3 localization | see §V |
| W2-B | Diagnostic | RE-REGISTER | Overshoot ∈ [1.1, 1.5] + GL-BdG validity | see §V |
| W2-C | Scheme-consistency | RE-REGISTER | Per-branch R-protection + direct zeta trace verification | see §V |
| W2-D | Scheme-comparison | RE-REGISTER | Sharp cutoff (f_0=1/2); 3-scheme spread < factor 1.5 + formula match | see §V |
| W2-E | Correction | RE-REGISTER | c_sub ∈ [0.5, 2] in f* and SDW, spread < 1.5 | see §V |
| W2-F | Scheme-check | RE-REGISTER | a_4^HK R^2-dominance + pre-registered f* R^2 coefficient | see §V |
| W2-G | Diagnostic | RE-REGISTER | |β^(2)|^2_phi < 0.01 in phi variable + gauge-invariance | see §V |
| W3-A | Decisive | RE-REGISTER | BMA extrapolation, 68% mass in [0.651,0.719] ∪ [1.952,2.158] | see §VI + DISAGREEMENT |
| W3-B | Diagnostic | KEEP | \|slope\| < 0.1 from W1-C output | see §VI |
| W3-C | Prediction | RE-REGISTER | Pre-registered r ± factor 2 + slow-roll control | see §VI |
| W3-D | Structural | RE-REGISTER | Non-linear mixing-angle × DOS × red-shift integral | see §VI |
| W3-E | Observational | RE-REGISTER | Split into W3-E-1 (PRE-IC) and W3-E-2 (REQUIRED-SUPPRESSION) | see §VI |
| W3-F | Verification | KEEP | Independent algebraic path; 0.056 ± 20% | see §VI |
| W3-G | Verification | RE-REGISTER | d w_0 / d F_amp < 0.001 + fresh DESI extraction | see §VI + DISAGREEMENT |
| W3-H | Structural | RE-REGISTER | Ansatz-breaking perturbation + pre-registered CMPP invariant | see §VI + DISAGREEMENT |
| W3-I | Meta | KEEP (META) | EVOI update; NOT counted in physics gates | see §VI |
| W3-J | Exploratory | RE-REGISTER | 1-loop MS-bar shift ~0.003 ± factor 1.5 | see §VI |
| W3-K | Structural | KEEP | Rank-scaling + cross-scheme universality within 15% | see §VI |
| W3-L | Meta→Substantive | RE-REGISTER | 5-10 script audit + tag corrections | see §VI |
| W3-M | Pre-registration | KEEP (PRE-REG) | Document written; NOT a gate verdict | see §VI |
| W3-N | Structural | KEEP | Cell extrapolation + IR regulator independence | see §VI |
| W3-O | Observational | RE-REGISTER | T_rh ~ 10^{18} MeV ± factor 10 + semi-classical validity | see §VI |
| W3-P | Structural | KEEP | Rank obstruction confirmed; rank values reported | see §VI |

**Count by verdict**: KEEP (with additions / pins): 6 gates. RE-REGISTER: 22 gates. REMOVE: 0 gates (all originally-proposed REMOVEs were converted to RE-REGISTER with substantive content or to labeled META/PRE-REG with reduced statistics weight).

---

## VIII. Decision Points (Re-keyed to pinned values)

### Decision Point 1 — After Wave 1

Inputs: W1-A through W1-E gate verdicts (all under pinned conventions).

**Branch A** — Lizzi-Landau confirmed (pinned-convention PASS):
- **Condition**: W1-A PASSes at 1.72e-9 ± factor 2 AND W1-B confirms N_pivot pipeline AND (W1-C PASSes linearized F_amp) OR (W1-C INFO shows F_amp reduction moderate + W1-E provides compensating S_IC in [1e-10, 1e-9]).
- **Wave 2 scope**: Consolidation. All W2 gates run as structural robustness checks.
- **Wave 3 scope**: As planned.
- **Session verdict**: Framework predicts A_s = 2.1e-9 with zero free parameters under pinned conventions. Strongest prediction-layer result in framework history — IF master gate closes.

**Branch B** — Transit-Einstein confirmed (9.5 OOM overproduction):
- **Condition**: W1-A PASSes at ~10^{+9.5} × 2.1e-9 in pinned convention AND W1-E S_IC ∈ [1, 1e-2] (cannot close 9.5 OOM) AND W1-C PASS (linearization valid, F_amp 6858 real).
- **Wave 2 scope**: Suppression-mechanism search. W2-D, W2-E, W2-F become critical. Others documentation only.
- **Wave 3 scope**: Frame 9.51 OOM overproduction as a new open problem; EVOI Level-1 add.
- **Session verdict**: Framework requires a 9.5-OOM suppression factor; possibilities: (a) unaccounted scheme conversion, (b) late-time decoherence, (c) structural bug in F_amp computation. NOTE: Per Gen-Physicist red-team question 19: if R-protection bounds cross-scheme f_conv spread to factor 2, Wave 2 cannot deliver 9 OOM suppression. Branch B may be dead-end.

**Branch C** — SP-Transit confirmed (linearization broken):
- **Condition**: W1-C FAIL (SPT-confirmed band [0, 6.9]) — F_amp^{sc} << 6858.
- **Wave 2 scope**: Split. W2-E, W2-G now treat non-perturbative mode equation. Others as planned.
- **Wave 3 scope**: INFO on self-consistent mode spectrum; possibly extend to higher Hartree orders.
- **Session verdict**: A_s at k_pivot is not perturbative; all S77/S78 perturbative claims superseded by self-consistent value.

**Branch D** — Inconsistent (INCOMPUTABLE on master chain):
- **Condition**: W1-A INCOMPUTABLE (ledger cannot close) OR W1-B FAIL (N_pivot not reproducible) OR W1-C INCOMPUTABLE (no method converges).
- **Wave 2 scope**: HALT A_s-dependent gates; run only W2-A, W2-C, W2-D, W2-F as scheme-audit.
- **Wave 3 scope**: EVOI becomes flagging; DESI separately bucketed.
- **Session verdict**: A_s is not currently computable to a single scheme-consistent number. S79 must repair the normalization chain.

### Decision Point 2 — After Wave 2

- Branch A reinforced: Promote "zero-param A_s" as headline — ONLY if master gate closed with propagated error.
- Branch B reinforced: "S78 identifies the A_s suppression problem" — with the Wave 2 dead-end caveat if applicable.
- Branch C: "S78 shows F_amp perturbative treatment fails."
- Branch D: "S78 flags normalization-pipeline gap; no A_s claim."

---

## IX. Success Criteria

**Hard success (unchanged structurally)**:
1. All 28 carry-forward items either completed with gate verdict (PASS/FAIL/INFO/INCOMPUTABLE) or flagged as infeasible with replacement.
2. Working paper built by QA (W3-F) with all sections merged, gate verdicts attached, full four-tuple tags.
3. Gate verdicts file complete and gate-verdicts.md compliant.
4. EVOI table updated (S78 stamp).
5. Master gate resolves to PASS / FAIL / INFO / INCOMPUTABLE with justification.

**Soft success (tightened)**:
1. At least one of the three pinned-account-identifications in W1-A has a specific factor attributed.
2. Multi-band E_cond closes the V_eff-minimum gap OR structurally closes the path.
3. Pre-fold vacuum characterized under canonical principle with cross-check INFO if disagreement.
4. At least 15 EVOI items change from S73B snapshot (Gen-Physicist's realistic bar; not the original's 3-item minimum).

**What this session is NOT trying to do** (unchanged):
- Resolve moduli-stabilization entirely.
- Resolve sin^2(θ_W) (W3-J exploratory).
- Add new mechanisms.

---

## X. Risk Register (unchanged + new)

Original risks from plan retained. New items:

| Risk | Likelihood | Mitigation |
|:-----|:-----------|:-----------|
| F_amp convention agents re-introduce F_amp^2 via non-canonical script | MEDIUM | Section 0.1 convention block; d(ln A_s)/d(ln F_amp) = 1 cross-check catches it |
| S_IC formula drifts back to \|α\|^2 - \|β\|^2 | MEDIUM | Section 0.5 explicit; \|α+β\|^2 pin forced in W1-E script header |
| DISAGREEMENT BLOCKs remain unresolved at re-run time | HIGH | User decision required before re-run; this plan runs with defaults but each default carries a note |
| Pre-registered expected values (Gen-Physicist) cannot be computed before run | MEDIUM | If no pre-registration possible, gate is demoted to INFO pending pre-registration scrub |
| Posterior computation (BMA) too costly at L_max=10 scale | MEDIUM | Use Laplace approximation as fallback; report mean + width instead of full posterior |
| "INCOMPUTABLE" verdict overused | LOW | Distinguish: INCOMPUTABLE requires that pre-registered fallbacks all fail, not just the primary method |

---

## XI. References

**Plan references** (unchanged from original): `.claude/rules/*.md`, `sessions/session-plan/session-78-context.md`, S77 synthesis, S77 workshops, `permanent-results-registry.md`.

**Scrub references**:
- `session-78-plan-scrubbed-nazarewicz.md` — Paper 06 McDonnell 2015, Bayesian UQ for truncated computations.
- `session-78-plan-scrubbed-lizzi.md` — arXiv:1412.4669, 1103.0478, 1210.2663, 1305.2605 — F_amp power-ratio resolution, anomaly f_0=1/2.
- `session-78-plan-scrubbed-transit.md` — Parker 1966, Birrell-Davies 1982, Motohashi, Berges 2002, Calzetta-Hu, Kamenev, Amin, Rigol, Volovik, Jacobson — IC-principle axiomatic gap, 2PI/Kadanoff-Baym methods.
- `session-78-plan-scrubbed-genphysicist.md` — discrimination-margin red-team, construction-forced / vacuous / load-and-compare patterns.

---

## XII. Execution Notes (unchanged from original)

Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`. Output: `computations/s78_*`. Designated writer W3-F (qa). All verdicts append-only to `s78_gate_verdicts.txt`. `/weave --update` after gate verdicts.

**Additional scrub discipline**:
- Every script must emit its (value, scheme_tag, convention_tag, L_max_tag) 4-tuple for each numerical output.
- Every gate block must include a "Convention pins" sub-section written BEFORE the script runs.
- Every iterative method must emit its convergence diagnostic (|change|/|value|) at each iteration.
- Any gate returning INCOMPUTABLE must include a "why" breakdown (which method failed, what the failure signature was).
- Gate verdict re-writes (PASS flipped to FAIL or vice-versa post-hoc) are STRICTLY FORBIDDEN per gate-verdicts.md + Gen-Physicist rule 11 (no verdict-flipping).

---

## Merge Log

### 28-gate verdict table (vote counts: K = KEEP as-is, R = RE-REGISTER, Rem = REMOVE; across 4 reviewers where each reviewer had a dominant verdict)

| Gate | Nazarewicz | Lizzi | Transit | Gen-Physicist | Merge verdict |
|:-----|:-----------|:------|:--------|:--------------|:--------------|
| S78-MASTER | K | R | R | R | RE-REGISTER (DISAGREEMENT) |
| W1-A | R | R | R | R | RE-REGISTER |
| W1-B | K | K | R | R | RE-REGISTER |
| W1-C | K | R | R | R | RE-REGISTER |
| W1-D | K | R | R | K | RE-REGISTER |
| W1-E | K | R | R | R | RE-REGISTER (DISAGREEMENT) |
| W2-A | K | K | R | R | RE-REGISTER |
| W2-B | R | K | R | Rem | RE-REGISTER |
| W2-C | K | R | — | R | RE-REGISTER |
| W2-D | K | R | — | R | RE-REGISTER |
| W2-E | K | R | R | R | RE-REGISTER |
| W2-F | K | R | — | R | RE-REGISTER |
| W2-G | K | R | R | Rem | RE-REGISTER |
| W3-A | K | R | — | R | RE-REGISTER (DISAGREEMENT) |
| W3-B | K | K | R | K | KEEP (with convention pin) |
| W3-C | R | K | R | R | RE-REGISTER |
| W3-D | R | K | R | R | RE-REGISTER |
| W3-E | K | K | R | R | RE-REGISTER |
| W3-F | K | K | R | K | KEEP (with convention pin) |
| W3-G | R | K | — | Rem | RE-REGISTER (DISAGREEMENT) |
| W3-H | R | — | — | Rem | RE-REGISTER (DISAGREEMENT) |
| W3-I | Rem | K | — | K (META) | KEEP as META |
| W3-J | R | K | — | R | RE-REGISTER |
| W3-K | K | R | — | K | KEEP + cross-scheme |
| W3-L | Rem | R | — | R | RE-REGISTER (substantive) |
| W3-M | Rem | K | — | K (PRE-REG) | KEEP as PRE-REGISTRATION |
| W3-N | K | R | R | K | KEEP + additions |
| W3-O | R | K | R | R | RE-REGISTER |
| W3-P | K | K | — | R | KEEP |

Totals: **KEEP (with additions / labels)**: 6 — W3-B, W3-F, W3-I (META), W3-K, W3-M (PRE-REG), W3-N, W3-P = actually 7 counting W3-P. **RE-REGISTER**: 21. **REMOVE**: 0 (structurally REMOVE-class gates were converted to labeled META or PRE-REGISTRATION with reduced statistics weight; W3-I and W3-M were the candidates).

### DISAGREEMENT BLOCKS (USER DECISION REQUIRED)

1. **S78-MASTER** — Structural form of master gate: Gen-Physicist's "three explicit FAIL modes" vs Nazarewicz's "single pre-registered value with propagated error."
2. **W1-E** — IC-principle selection: Transit's axiomatic gap (requires user-level axiom before re-run) vs Nazarewicz's BMA (computable specification) vs Lizzi's AZ-default with cross-check INFO.
3. **W3-A** — chi_2 primary scheme: Lizzi's SDW-only gate vs Nazarewicz's BMA across schemes and fit forms.
4. **W3-G** — Structural form: Nazarewicz's "partial derivative test" vs Gen-Physicist's "REMOVE and replace with fresh DESI extraction" vs this plan's "merge both into sub-gates."
5. **W3-H** — KEEP (as ansatz-breaking perturbation test) vs REMOVE (Gen-Physicist: construction-forced even under perturbation unless specific non-trivial CMPP invariant is pre-registered).

### Plan-wide convention pins applied (Section 0 block)

1. F_amp is a POWER RATIO, LINEAR in A_s (NOT F_amp^2). Replaces the single biggest plan-wide convention error.
2. a_n scheme default: zeta; SDW and f* as cross-checks; HK via conversion dictionary.
3. Cutoff family: f* primary; sharp cutoff for anomaly only; SDW canonical for chi_2 identity.
4. R_1 / R_2: per-branch only; cross-branch is Level 3 (not R-protected).
5. IC principle default: spectral stationarity (Transit canonical), AZ as cross-check. User decision pending.
6. S_IC = |α + β|^2. Replaces |α − β|^2 and |α|^2 − |β|^2 (both wrong in the original plan).
7. f_n Mellin normalization: f_0 = 1/2 forced for anomaly (sharp cutoff).
8. Omega_DM Leggett formula: linear GGE thermal (Section 0.7).
9. k_pivot, horizon crossing, integrator tolerances: all explicit.
10. Tag discipline: 4-tuple (value, scheme, convention, L_max) on every deliverable.
11. Epistemic rule: INCOMPUTABLE ≠ FAIL.

### Single biggest change from the original plan

The F_amp exponent correction from F_amp^2 to F_amp^1. Lizzi's derivation from the Bogoliubov formalism (Parker; Birrell-Davies) shows F_amp is the dimensionless power ratio P_zeta(real)/P_zeta(pure-dS) — already squared in the Wronskian sense — and appears LINEARLY in A_s. The original plan's master equation `A_s = (H^2/(8π^2 ε M_Pl_red^2)) × F_amp^2 × f_conv × S_IC` concealed a double-count of factor 6858 ≈ 3.8 OOM. Every gate that touched F_amp (W1-A, W1-B, W1-C, W2-E, W3-B, W3-C, W3-E) was downstream-curated by this error. The S78 executing agent's arithmetic match to Planck (0.09 OOM) under F_amp^1 was the right answer for the wrong reason (the agent picked F_amp^1 post-hoc because it matched Planck, not from derivation). Pinning the POWER-RATIO convention in Section 0.1 makes the PASS at 1.72e-9 a derivation, not a curation. Every other convention pin (S_IC = |α+β|^2, sharp-cutoff f_0 = 1/2 for anomaly, per-branch R-protection, spectral-stationarity IC default) rides on top of this single correction. Without it, the A_s ledger PASSes by convention-choice rather than by physics.

---

**End of scrubbed plan.**
