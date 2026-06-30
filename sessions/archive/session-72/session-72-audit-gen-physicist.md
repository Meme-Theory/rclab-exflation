# Session 72 Project Audit: General Physics

**Date**: 2026-04-10
**Scope**: Sessions 1-72, all atlas documents, EVOI framework, constraint mega-matrix, pre-registered observations, S72 results working paper + 4 workshops
**Method**: Exhaustive cross-reference of every open question, deferred computation, unresolved tension, and untested assumption across all project sources

---

## I. Critical Open Problems (framework-threatening if unresolved)

### I-1. A_s Amplitude Normalization Gap (0.267 OOM residual)

- **What**: The power spectrum amplitude A_s is predicted ~1.85x too large (0.267 OOM). All spectral-geometric RATIOS (n_s, sin^2 theta_W, M_W, Omega_DM) match observation; all absolute AMPLITUDES (A_s, CC, H_0) fail.
- **Where**: S70 baseline (0.267 OOM after Leggett PASS), S72 W1-A (gap curvature DEAD), S72 W2-A (dual decoherence INFO, cell-crossing 9.4x too slow)
- **Why it matters**: Without A_s, the CMB power spectrum is not predicted. The framework produces the right shape (n_s) but wrong normalization. This is the difference between a predictive cosmology and a mathematical exercise.
- **S72 status**: S72 exhaustively tested five decoherence channels. Only KZ freeze-out at the exit horizon is fast enough. Two competing models bracket the gate band: statistical KZ (t_dec/t_transit = 0.13, over-decohered) vs Bogoliubov KZ (t_dec/t_transit = 2.2, under-decohered). The gate band is [0.57, 0.88]. The exit-horizon greybody factor is the decisive arbiter.
- **Effort**: HIGH (dedicated Bogoliubov computation at exit horizon)
- **Blocks**: All CMB amplitude predictions, H_0 prediction, power spectrum normalization

### I-2. Spectral Functional Selection (eps_H sign reversal)

- **What**: The Hubble slow-roll parameter eps_H changes SIGN between cutoff families. sqrt(x) gives n_s = 0.957 (red tilt, Planck-compatible); zeta/exponential give n_s > 1 (blue tilt, excluded). The n_s spread across functionals is 0.164 (39x the Planck error bar).
- **Where**: S66 CUTOFF-NS-66 (discovery), atlas-05 Door 8, EVOI P3 FUNCTIONAL-SELECT-67
- **S72 update**: S72 W2-C found a positive spectral functional f* = 0.912 sqrt + 0.088 exp that matches n_s = 0.9649 exactly. But f* is NON-PERTURBATIVE (divergent SDW moments) and introduces a free parameter (the mixing fraction t*). No selection principle determines t* from the spectral triple alone.
- **Why it matters**: If f is a free parameter, n_s is accommodation, not prediction. The entire zero-free-parameter claim collapses unless f is uniquely determined by anomaly cancellation, conservation laws, or some other structural principle.
- **Effort**: HIGH (mathematical: requires new NCG selection principle)
- **Blocks**: n_s prediction status, alpha_s prediction, all claims of zero-parameter predictions

### I-3. DESI w_0-w_a Tension (2.91 sigma on both)

- **What**: Framework predicts w_0 = -0.918 (Volovik), w_a = 0 (four-fold locked). DESI DR2+DESY5 measures w_0 = -0.752 +/- 0.057, w_a = -0.73 +/- 0.25. Both at 2.9 sigma.
- **Where**: S67-68, pre-registered-observations.md, atlas-04 entries C4 and C5
- **Pre-registered decision**: Framework SURVIVES if w_a > -0.35. Framework FAILS if w_a < -0.530.
- **Why it matters**: DESI DR3 (2026-2027) is the only experiment that can EXCLUDE the framework on a 1-year timescale. w_a = 0 is structurally locked (GGE integrability + Josephson + frozen texture + thermalization barrier, 59 OOM gap). It cannot be adjusted.
- **Effort**: LOW (wait for data; no internal computation resolves this)
- **Blocks**: Framework viability as a cosmological model

### I-4. K_pivot Scale Mapping Paradox

- **What**: Two physically motivated mappings for the CMB pivot scale give contradictory answers. K = 4.3e-57 M_KK (physical e-fold mapping, gives flat n_s = 1) vs K = 2.0 M_KK (tessellation mapping, excluded by convex combination theorem W9). The framework's n_s prediction depends on which mapping is correct, and neither works.
- **Where**: Atlas-04 entries C2 (BROKEN) and C3 (BROKEN), atlas-05 Window 1, S51 W2-A
- **Why it matters**: The entire cosmological prediction suite (n_s, alpha_s, sigma_8) is CONDITIONAL on this mapping. Without it, proven spectral geometry does not connect to CMB observables.
- **Effort**: HIGH (requires full expansion history computation: EFOLD-MAPPING-52, never completed)
- **Blocks**: n_s, alpha_s, sigma_8, all CMB predictions

### I-5. alpha_s Falsification Threat

- **What**: alpha_s = -0.038 at 5.0 sigma from Planck (-0.0045 +/- 0.0067). S70 showed f_0 and alpha_s are anti-correlated (F0-ALPHA-S-70 FAIL), making this structural rather than a normalization issue.
- **Where**: EVOI P1 (TRANSIT-PS-67), S70 F0-ALPHA-S-70 FAIL, S72 W2-B (threshold corrections needed), S72 Landau-Baptista workshop (branching-resolved couplings flagged CRITICAL)
- **S72 status**: S72 alpha_s = 0 is now a functional-independent prediction (from S70 c_s^2 = 0 DERIVED). The alpha_s and f_NL^equil = 0.853 predictions are FUNCTIONALLY INDEPENDENT of each other. The f_0 anti-correlation remains unresolved.
- **Effort**: HIGH (requires TRANSIT-PS full Bogoliubov power spectrum)
- **Blocks**: CMB-S4 confrontation, sigma_8 prediction chain

### I-6. Leggett DM Gravitational Stability (LEGGETT-GRAV-DECAY-67)

- **What**: The Leggett mode dark matter candidate (Omega_DM h^2 = 0.120, 0.7 sigma from Planck) must be stable against gravitational decay. Gamma_grav < H_0 is the gate. This was flagged as EVOI P2 but never computed.
- **Where**: EVOI P2, atlas-05 Door 13, S66 analysis
- **Why it matters**: If FAIL, the entire DM sector collapses. The 0.6% agreement with Planck becomes meaningless if the candidate decays before the present epoch.
- **Effort**: MEDIUM (perturbative graviton vertex computation)
- **Blocks**: Omega_DM prediction, CDM by construction, sigma_8

### I-7. BBN Constraint on Volovik CC (BBN-VOLOVIK-67)

- **What**: Volovik Scenario B (CC PASS at 0.01 OOM) gives rho_vac/rho_rad = 0.67 at nucleosynthesis. This is a 67% contamination of the radiation energy density at T_BBN = 1 MeV.
- **Where**: EVOI P4, atlas-05 Door 12, S66 Workshop 4
- **Pre-registered gate**: PASS if |w_vac - 1/3| < 0.03 at T_BBN; FAIL if > 0.10.
- **Why it matters**: If the Volovik tracking vacuum contributes 67% of radiation at BBN, it alters primordial element abundances. This is a potential showstopper for the only surviving CC mechanism.
- **Effort**: MEDIUM (BBN code with modified expansion history)
- **Blocks**: CC mechanism viability, Volovik relaxation

---

## II. High-Priority Uncomputed Items (from EVOI + carry-forwards)

### EVOI Priority 1 (all four STILL UNCOMPUTED as of S72)

| ID | Computation | EVOI | Sessions queued | Status |
|:---|:-----------|:-----|:----------------|:-------|
| P1 | TRANSIT-PS-67: Full Bogoliubov power spectrum through fold | 22.5% | S67-S72 (6 sessions) | NOT STARTED. S70 proved WKB inapplicable (CHIRP-PENUMBRA-70 FAIL, gamma > 1 for 93.4% modes). Dedicated Bogoliubov solver mandatory. |
| P2 | LEGGETT-GRAV-DECAY-67: Gravitational decay vertex | 17.4% | S67-S72 (6 sessions) | NOT STARTED |
| P3 | FUNCTIONAL-SELECT-67: Derive physical spectral functional | 13.2% | S67-S72 (6 sessions) | PARTIAL. S72 W2-C found f* exists but has a free parameter. Selection principle UNCOMPUTED. |
| P4 | BBN-VOLOVIK-67: Volovik tracking EOS at T_BBN | 14.0% | S67-S72 (6 sessions) | NOT STARTED |

These four computations have been queued since S66 and assigned to S67 in the EVOI table. None has been completed through S72 (6 sessions of delay).

### EVOI Priority 2

| ID | Computation | EVOI | Status |
|:---|:-----------|:-----|:-------|
| P5 | BA-LIFETIME-FABRIC-67 | 6.5% | NOT STARTED |
| P6 | JOINT-FALSIFICATION-67 | 7.2% | NOT STARTED |
| P7 | BAYESIAN-FUNCTIONAL-67 | 7.0% | NOT STARTED |
| P8 | GGE-BISPECTRUM-67 | 4.8% | PARTIAL (S72 W4-A computed decoherence bispectrum: f_NL^equil = -0.313, but from Bogoliubov only, not in-in formalism) |
| P9 | PROJECTED-MOMENTS-67 | 5.0% | NOT STARTED |

### S72 Workshop Carry-Forwards (new high-priority items)

| ID | Computation | Source | Priority |
|:---|:-----------|:-------|:---------|
| EXIT-HORIZON-BOG-73 | Bogoliubov transformation AT exit horizon (greybody factor, mode-dependent phase spread) | S72 SP synthesis, S72 laminar flow workshop | CRITICAL |
| SPECTRAL-ACTION-PROFILE-73 | S(tau) from direct spectral sums for tau in [0.19, 2.0] with f*. Three-in-one: moduli stabilization + CC + w(z) | S72 Mack-VdD workshop | CRITICAL |
| BRANCHING-JOSEPHSON-73 | Branching-resolved Josephson couplings J_C2^{SU(2)} vs J_C2^{U(1)} | S72 Landau-Baptista workshop CF-2 | CRITICAL |
| THRESHOLD-RATIOS-73 | PW-sector-resolved threshold ratios delta_1/delta_3, delta_2/delta_3 at tau_fold | S72 W2-B priority follow-up | HIGH |

---

## III. Unresolved Tensions (numbers that don't match)

### III-1. n_s: Two predictions, both conditional

- 0.9567 (bare Hubble slow-roll, all cutoffs that give red tilt)
- 0.9595 (BCS + CW dressed, S65)
- S72 W3-A v2: BCS dressing is NEGLIGIBLE (3.8e-6 shift). Bare prediction stands at 0.9567, which is 1.95 sigma from Planck (0.9649).
- S72 W2-C: Best-fit f* gives n_s = 0.9649 EXACTLY by construction (free parameter t*).
- **Tension**: Is n_s a prediction (0.9567, 1.95 sigma) or accommodation (tuned to match via f*)?
- **Source**: S62 W2-01, S72 W2-C, S72 W3-A v2

### III-2. sin^2(theta_W): 34.6% gap requires uncomputed KK thresholds

- Geometric boundary condition at M_KK: sin^2 = 0.584
- SM RG running to M_Z: sin^2 = 0.357 (54.5% discrepancy from PDG 0.231)
- Universal threshold model: sin^2 = 0.229 (1.2% from PDG) -- but threshold equality at tau = 0.19 is undemonstrated
- **Source**: S72 W2-B, S72 W1-E

### III-3. alpha_GUT: 1/10.8 vs 1/25

- Framework one-loop extraction: f_0 = 4.258, giving alpha_GUT = 1/10.8
- Standard CCM value: f_0 = 9.82, giving alpha_GUT = 1/25
- Factor 2.3 discrepancy, structural (tracks S_1loop/S_tree = 0.52)
- **Source**: S62 W3-08, atlas-08 Q18a

### III-4. w_0: Volovik vs spectral moment formula

- S72 W1-D FAIL: Formula w_0 = -1 + (2/3)R/(1+R) with R = a_2^2/(a_0 a_4) gives w_0 in [-0.848, -0.612], not -0.918
- Canonical w_0 = -0.918 comes from Volovik partition (S58), categorically different from spectral moment ratio
- The formula connecting spectral moments to late-time EoS does not exist
- **Source**: S72 W1-D

### III-5. f_NL: S70 vs S72 sign and magnitude

- S70: f_NL^equil = 0.853 (positive)
- S72 W4-A: f_NL^equil = -0.313 to -0.026 (negative, at physical/target decoherence)
- Different methods: S70 from in-in-like formalism, S72 from Bogoliubov bispectrum with decoherence
- Both within Planck bounds (-26 +/- 47), so observationally equivalent, but the theoretical prediction is sign-ambiguous
- **Source**: S70 W3, S72 W4-A

### III-6. Zubarev vs Keldysh w_0 discrepancy (20%)

- w_0(Zubarev) = -0.430, w_0(Keldysh) = -0.589
- Neither matches canonical -0.918 (Volovik partition)
- 20% discrepancy between two legitimate thermodynamic formalisms applied to the same GGE
- Never resolved; flagged as CF9 since S46
- **Source**: Atlas-08 CF9, MEMORY.md

### III-7. Higgs mass: tree vs Aitken vs W2-C

- 134.0 GeV (tree-level, filter-independent, A10)
- 127.5 GeV (Aitken-extrapolated PW convergence, 1.9% from observed)
- f*(0) = 0.088 from S72 W2-C predicts m_H ~ 39-51 GeV (EXCLUDED)
- The W2-C result exposes a tension: the f* that matches n_s predicts a Higgs mass that is 3x too low. Resolution requires KK threshold RG from M_KK to M_Z.
- **Source**: S62, S66, S72 W2-C

---

## IV. Deferred Computations (explicitly postponed, never returned to)

### From Atlas-08 Carry-Forward List (20 items, none executed S47-S72)

| CF# | Item | Source | Sessions deferred | Notes |
|:----|:-----|:-------|:-----------------|:------|
| CF1 | TT 2-tensor Lichnerowicz | S47 B-5 | 25 sessions | Flagged "next decisive" in S47. Never started. |
| CF2 | Q-theory Goldstone self-tuning | S47 C-5 | 25 sessions | m ~ 10^{-39} GeV. Q-theory CC route now CLOSED (S62), but Goldstone mass itself still relevant. |
| CF3 | Sakharov curvature-weighted sum | S47 B-4 | 25 sessions | Tests G_N improvement from 0.36 OOM |
| CF4 | Three-phonon vertex | S46 D-2 | 26 sessions | omega_B2 ~ 2*omega_B1 resonant friction. Never tested. |
| CF5 | DISSOLUTION-BERRY-47 | S46 D-3 | 26 sessions | Pi-phase survival |
| CF6 | CLOSED-LOOP-47 | S46 D-3 | 26 sessions | Round-trip Berry consistency |
| CF7 | Sector-resolved R(p,q) pair ratio | S46 D-3 | 26 sessions | CPT symmetry test |
| CF8 | (2,1) pi-phase count = 5 | S46 D-3 | 26 sessions | Derivation |
| CF9 | GIBBS-DUHEM-GGE | S46 D-4 | 26 sessions | 20% Zubarev/Keldysh discrepancy |
| CF10 | Keldysh sigma (pair-pair) | S46 D-4 | 26 sessions | |
| CF11 | LOG-SIGNED-40 | S40 | 32 sessions | Signed B-F log sum on 2912 eigenvalues |
| CF12 | PHI-GOLDEN-22 | S47 D-5 | 25 sessions | (2,2)/(0,0) ratio sweep |
| CF13 | Six-sequence test | S47 D-5 | 25 sessions | Zero cost |
| CF14 | Swampland c(tau) | S47 D-6 | 25 sessions | de Sitter conjecture |
| CF15 | Poisson-Lie T-duality | S47 D-6 | 25 sessions | Monotonicity in dual frame |
| CF16 | Chladni patterns | S47 B-6 | 25 sessions | Eigenvector retention |
| CF17 | C^2 isotropization | S47 Landau Q-1 | 25 sessions | Lifshitz transition |
| CF18 | Anisotropic KZ defects | S47 Landau S-5 | 25 sessions | |
| CF19 | Akama-Diakonov metric | S47 Volovik 3.1 | 25 sessions | Analog horizon |
| CF20 | 279-mode tachyonic velocity | S46 D-8 | 26 sessions | |

### S46 Corrections Never Propagated

| Correction | Status | Age |
|:-----------|:-------|:----|
| alpha* = 3.91 -> 0.775 | FN-CENTROID-47 unexecuted | 26 sessions |
| CHAOS-1 < r > = 0.321 -> 0.439 | Acknowledged, never recomputed | 25 sessions |

### EFOLD-MAPPING-52 (THE decisive computation)

- Atlas-08 Q1: "HIGHEST -- the single question to which 51 sessions reduce"
- First queued: S51
- Status after S72: PRELIMINARY PASS (S64 partial: N_e = 3.73e-3 physical transit). Full expansion history including stiff epoch, backreaction, radiation transition: NOT COMPUTED.
- Age: 21 sessions without completion

### Self-Consistent HFB Gap Equation (Q15)

- Source: S47 wayforward C-2, Nazarewicz priority 1
- Full Hartree-Fock-Bogoliubov iteration with sector-resolved Delta_{(p,q)}
- Never executed. Current mean-field overestimates by 60% (S46 PBCS).
- Age: 25 sessions

### Non-Abelian Berry Phase Wilson Loop (Q14, WILSON-LOOP)

- Source: S46-47, predicted pi-count in [13, 50]
- Computable with existing code
- Never executed. Age: 26 sessions.

---

## V. INFO Gates Needing Resolution (from S72 + prior sessions)

### S72 INFO Gates (8 of 20 computations)

| Gate | Value | Issue | Required follow-up |
|:-----|:------|:------|:-------------------|
| KAPPA-DELTA-72 | t_dec/t_transit = 5.5e9 | Gap curvature decoherence negligible (delta_OOM = 1.6e-10). Assumed d(Delta)/dtau = 0 was WRONG. | A_s budget must use phase dynamics (Leggett, Josephson), not gap amplitude. |
| GILKEY-REEVAL-72 | delta = 13.3% (was 26.9%) | S71 HIGHER-ORDER-CCM PASS downgraded to INFO. Gilkey ratio halves the correction. | Effect is maximally scheme-dependent (0% to 27%). Needs spectral functional selection. |
| DUAL-DECOHERENCE-72 | delta_OOM = 1.692 | Cell-crossing 9.4x too slow. Gate band requires t_dec/t_transit in [0.57, 0.88]. | EXIT-HORIZON-BOG-73 computation needed |
| BCS-DRESSED-SA-72 | |n_s - 0.9649| = 0.0082 | 1.94 sigma. Mode-selective correction negligible (3.8e-6). | n_s gap must close via full-spectrum mechanism or f* selection |
| ASYMPTOTIC-TRUNCATION-72 | |a_8/a_6| = 0.681 > |a_6/a_4| = 0.567 | SDW expansion past optimal at order a_8. For f*, SDW DOES NOT EXIST. | All a_6+ predictions require direct spectral sums |
| TAU-EQUILIBRIUM-72 | Quartic models have stable minima, cubic do not | Post-transit equilibrium REDUCES to S(tau) global shape, not BCS. | SPECTRAL-ACTION-PROFILE-73 needed |
| INSTANTON-KAPPA-72 | kappa(peak) = 1.057 | At instanton measure peak, marginally above Kato-Rellich bound. Large rho viable. | kappa(rho, tau) stability across transit |
| CG24-GGE-ENTROPY-72 | S_cell between 2.21 and 4.11 nats | J_C2/Delta = 2.01 (strong coupling) makes perturbation theory unreliable. | Strong-coupling many-body calculation on CG(24) |

### Prior Sessions -- INFO Gates Still Open

| Gate | Session | Value | Issue |
|:-----|:--------|:------|:------|
| F0-ALPHA-S-70 | S70 | alpha_s and m_H anti-correlated in f_0 | Structural, not normalization. Branching-resolved Josephson (CF-2) is the proposed resolution. |
| PARAMETRIC-GGE-70 | S70 | Post-transit resonance excluded (overdamped) | Establishes GGE formation is single-pass KZ, not parametric |
| LMAX7-PW-70 | S70 | m_H in [127, 135] GeV with oscillatory convergence | Needs SPECTRAL-ZETA-THRESHOLD to bypass oscillatory PW convergence |
| HIGHER-ORDER-CCM-71 | S71 | Downgraded S72: delta = 13% not 27% | Scheme-dependent; cannot resolve without f selection |

---

## VI. Mathematical Gaps (proofs incomplete)

### VI-1. Order-One Condition for D_total (Atlas-04 N3)

- D_K satisfies 6/7 NCG axioms. Axiom 5 (orientability) FAILS at 4.000 for D_total. Order-one norm = 3.117.
- This is not an approximation or truncation; it is a structural failure of the full spectral triple.
- **Status**: BROKEN. No repair proposed.
- **Source**: S28, atlas-04 N3

### VI-2. Complete A_F Extraction (Atlas-04 N2)

- C + M_3(C) extracted (dim 20). Quaternion factor H requires bimodule construction never computed.
- o-map route identified S10, never executed.
- **Source**: S10, atlas-04 N2, atlas-08 Q11. Age: 62 sessions.

### VI-3. 4D Effective Action for Modulus Dynamics (Atlas-08 Q8)

- The spectral action provides one functional; the true modulus effective action may be categorically different.
- F.5 showed SA penalizes BCS pairing (wrong sign, 93x). SA is a spectral moment, not a total energy.
- No first-principles derivation of the modulus kinetic term from the path integral exists.
- **Source**: Atlas-04 S3, spectral-post-mortem Section 5

### VI-4. tau-to-Cosmic-Time Mapping (Atlas-08 Q13)

- The identification tau-evolution = cosmic expansion is the framework's core postulate. It has never been derived from the 12D Einstein equations reduced to M^4 x SU(3).
- DeWitt supermetric G_mod = 5.0 is computed but coupling to FRW is approximate.
- **Source**: Atlas-04 C1

### VI-5. n_s > 1 Structural Proof (Atlas-07 D13)

- Claimed: bare Dirac heat kernel on ANY compact manifold gives n_s >= 1. Red tilt REQUIRES dynamics.
- Listed as PROVEN in atlas-04 P3 but as "unvalidated" in atlas-07 D13.
- Contradictory status between atlas documents needs resolution.
- **Source**: S51, atlas-04 P3 vs atlas-07 D13

### VI-6. SDW Expansion Non-Existence for f*

- S72 W2-C: The best-fit f* = 0.912 sqrt + 0.088 exp has DIVERGENT SDW moments (f_0 = infinity for sqrt component).
- S72 W3-B: SDW ratio sequence is monotone increasing (asymptotic, not convergent).
- All predictions depending on a_6 or higher must use direct spectral sums, not SDW.
- But many framework numbers (a_0, a_2, a_4 in canonical_constants.py) were computed from SDW. Their validity under f* needs re-examination.
- **Source**: S72 W2-C, S72 W3-B

### VI-7. Off-Jensen Moduli Landscape (Atlas-08 Q9)

- Structural monotonicity theorem proven ONLY on Jensen 1-parameter family.
- Full 5D U(2)-invariant landscape untested (Window 3).
- T4 instability at tau = 0.60, eps = +0.15 suggests U(2) surface is itself unstable.
- S64 VP Hessian: 35D all positive at fold (genuine minimum), but this is at a SINGLE point.
- **Source**: Atlas-05 Window 3, atlas-08 Q9

---

## VII. Observational Predictions Untested

### VII-1. Predictions with Upcoming Data

| Prediction | Value | Experiment | Timeline | Gate |
|:-----------|:------|:-----------|:---------|:-----|
| w_a = 0 (exact) | 0 | DESI DR3 | 2026-2027 | FAIL if w_a < -0.530 |
| w_0 = -0.918 | -0.918 | DESI DR3 | 2026-2027 | Current 2.91 sigma tension |
| Mass ordering = Normal | NO | JUNO | 2028-2030 | FAIL if IO at > 3 sigma |
| sigma_8 = 0.799 | 0.799 | Euclid DR1 | 2029 | Between Planck and lensing |
| ISW tracking c_s^2 = 0 | +7.6% vs quintessence | Euclid tomographic | ~2030 | SNR 1.58 (marginal) |
| r = 0.0242 | 0.0242 | LiteBIRD | 2034 | 24 sigma detection; non-detection falsifies |
| alpha_s = 0 (exact) | 0 | CMB-S4 | 2034 | Planck 0.67 sigma, CMB-S4 sigma ~ 0.003 |
| f_NL^equil = 0.853 | 0.853 | CMB-S4 | 2034 | UNDETECTABLE (0.17 sigma) |
| Omega_GW ~ 10^{-10} | 10^{-10} | LISA | 2035 | Domain wall spectrum |
| f_NL^folded = 0.129 | 0.129 | 21cm tomography | 2040s | 3.6 sigma (purpose-built) |
| ISW tracking | +7.6% | 21cm | 2040s | SNR 7.9 (definitive) |

### VII-2. Predictions Never Tested Against Existing Data

| Prediction | Value | Available Data | Status |
|:-----------|:------|:---------------|:-------|
| ALPHA-ENV-43 | delta_alpha/alpha ~ 10^{-6} (void vs filament) | Spectroscopic surveys | Queued since S43 (29 sessions) |
| DM pair decay lifetime | tau_DM = 4.93e82 s | FIRAS constraints | PASS (57 OOM margin, S70) but never confronted with gamma-ray/neutrino limits |
| n_T(transit) = +0.075 | Blue tilt at 10^37 Hz | No detector exists | Structurally inaccessible |
| Domain wall GW spectrum shape | Specific Omega_GW(f) profile | NANOGrav, EPTA | Not computed in detail |

---

## VIII. Framework Assumptions Untested

### Foundational Assumptions (Atlas-04 entries marked ASSUMED)

| # | Assumption | Status | Risk |
|:--|:-----------|:-------|:-----|
| G1 | M^4 x K product structure | ASSUMED (S1) | No derivation from deeper principle. If non-product, entire spectral triple changes. |
| G2 | K = SU(3) specifically | ASSUMED (S1) | Vindicated by output (SM quantum numbers) but not unique. S72 W4-F: G_2 also has stable a_2/a_4. |
| G3 | Jensen 1-parameter family | ASSUMED (S12) | Full 28D moduli space untested. Hessian at fold positive (S64) but landscape topology unknown. |
| G6 | Volume-preserving constraint | ASSUMED (S12) | If relaxed: G_N acquires tau-dependence, entire spectral landscape changes. No selection principle. |
| G7 | Left-invariant metrics only | ASSUMED (S22b) | Peter-Weyl block-diagonality (W2) depends on this. Inhomogeneous deformations break it. |
| S2 | Cutoff function f is physical | ASSUMED (S37) | S72 confirms: n_s is scheme-dependent. No selection principle exists. |
| S3 | SA provides correct modulus effective action | ASSUMED | F.5: SA penalizes BCS (wrong sign, 93x). SA may be categorically wrong as modulus potential. |
| C1 | tau = cosmic time | ASSUMED (S1) | Core postulate. Never derived from 12D Einstein equations. Load-bearing. |

### Conditional Results (pass only if conditions met)

| # | Result | Condition | Risk |
|:--|:-------|:----------|:-----|
| B2 | Kosmann = BCS interaction | "Natural" is not "unique" | Other connections could give different physics |
| B4 | Mean-field adequate for N_pair=1 | 60% overestimate acceptable | Affects gap magnitude, CDM abundance |
| B7 | Mechanism chain unconditional | Assumes tau reaches fold | Requires transit dynamics (T1-T6) |
| B8 | Instanton gas description | Dense gas regime | Cosmological consequences unestablished |
| C6 | eta from pair-breaking | Exactly 2 pair breaks, specific M_KK | Plausible but not a precision prediction |
| C7 | CDM from GGE quasiparticles | rho_DM/rho_Lambda = 5.4e5 | CC problem in disguise; abundance not predicted |

---

## IX. Priority-Ordered Master List

Items ranked by estimated impact x urgency. Impact = what fraction of framework predictions depend on resolution. Urgency = external deadline or downstream blockers.

### computation: Framework-Survival (resolve before DESI DR3)

| # | Item | Type | Effort | Blocks |
|:--|:-----|:-----|:-------|:-------|
| 1 | **EXIT-HORIZON-BOG-73**: Bogoliubov transformation at exit horizon | Computation | HIGH | A_s budget, all CMB amplitudes |
| 2 | **LEGGETT-GRAV-DECAY-67**: Gravitational decay width of Leggett mode | Computation | MEDIUM | DM sector viability |
| 3 | **BBN-VOLOVIK-67**: Volovik tracking EOS at nucleosynthesis | Computation | MEDIUM | CC mechanism, expansion history |
| 4 | **DESI DR3 monitoring**: Pre-registered w_a decision rule | External data | LOW | Framework viability |

### Level 1: Structural Resolution

| # | Item | Type | Effort | Blocks |
|:--|:-----|:-----|:-------|:-------|
| 5 | **SPECTRAL-ACTION-PROFILE-73**: Full S(tau) for tau in [0, 2] with f* | Computation | HIGH | Post-transit equilibrium, CC, w(z), moduli stabilization |
| 6 | **FUNCTIONAL-SELECT**: Selection principle for f(x) from first principles | Mathematical | HIGH | n_s prediction status, all zero-parameter claims |
| 7 | **EFOLD-MAPPING-52**: Full expansion history (stiff + transit + GGE + radiation) | Computation | HIGH | K_pivot, n_s, alpha_s, sigma_8 |
| 8 | **TRANSIT-PS-67**: Full Bogoliubov power spectrum (WKB FAIL, dedicated solver) | Computation | HIGH | alpha_s, A_s, full P(k) |
| 9 | **THRESHOLD-RATIOS-73**: PW-sector-resolved KK thresholds at tau_fold | Computation | MEDIUM | sin^2(theta_W), alpha_GUT, gauge coupling unification |
| 10 | **BRANCHING-JOSEPHSON-73**: Branching-resolved Josephson couplings | Computation | MEDIUM | alpha_s, f_0 anti-correlation |

### Level 2: Quantitative Completion

| # | Item | Type | Effort | Blocks |
|:--|:-----|:-----|:-------|:-------|
| 11 | SDW-to-direct spectral sum validation under f* | Computation | MEDIUM | All canonical constants (a_0, a_2, a_4) |
| 12 | Off-Jensen 5D Hessian at one point | Computation | MEDIUM | Landscape topology |
| 13 | Self-consistent HFB gap equation (Q15) | Computation | MEDIUM | Gap magnitudes, CDM abundance |
| 14 | 4D effective action derivation (Q8) | Mathematical | HIGH | Modulus dynamics, transit physics |
| 15 | Yukawa hierarchy beyond rank-1 (Q18b) | Mathematical | HIGH | Fermion mass spectrum |
| 16 | alpha_GUT tension resolution (Q18a) | Computation | MEDIUM | Gauge coupling unification |
| 17 | A_F quaternion extraction (Q11) | Mathematical | MEDIUM | NCG axiom completion |
| 18 | Tau-to-cosmic-time derivation (Q13) | Mathematical | HIGH | Core postulate validation |

### Level 3: Backlog (viable but never executed)

| # | Item | Sessions deferred | Source |
|:--|:-----|:-----------------|:-------|
| 19 | Wilson loop Berry phase (Q14) | 26 | S46-47 |
| 20 | Sakharov curvature-weighted sum (CF3) | 25 | S47 |
| 21 | Three-phonon vertex (CF4) | 26 | S46 |
| 22 | Zubarev/Keldysh discrepancy (CF9) | 26 | S46 |
| 23 | Signed B-F log sum (CF11) | 32 | S40 |
| 24 | Chladni eigenvector patterns (CF16) | 25 | S47 |
| 25 | C^2 isotropization (CF17) | 25 | S47 |
| 26 | Domain wall GW spectrum shape | ~13 | S59 |
| 27 | alpha* = 3.91 -> 0.775 propagation | 26 | S46 |
| 28 | CHAOS-1 recomputation | 25 | S47 |

### Level 4: Observational Monitoring

| # | Item | Timeline |
|:--|:-----|:---------|
| 29 | DESI DR3 w_0, w_a | 2026-2027 |
| 30 | JUNO mass ordering | 2028-2030 |
| 31 | Euclid sigma_8, ISW | 2029-2032 |
| 32 | LiteBIRD r detection | 2034 |
| 33 | CMB-S4 n_s, alpha_s | 2034+ |
| 34 | ALPHA-ENV-43 void/filament test | When survey data available |

---

## Summary Statistics

| Category | Count |
|:---------|------:|
| Critical open problems (framework-threatening) | 7 |
| EVOI Priority 1 computations still uncomputed (6 sessions overdue) | 4 |
| EVOI Priority 2 computations uncomputed | 5 |
| New CRITICAL carry-forwards from S72 workshops | 4 |
| Unresolved numerical tensions | 7 |
| Atlas-08 carry-forwards never executed | 20 |
| Unpropagated corrections (S46) | 2 |
| Decisive computations deferred > 20 sessions | 3 |
| INFO gates requiring resolution (S72) | 8 |
| INFO gates requiring resolution (prior sessions) | 4 |
| Mathematical proofs incomplete | 7 |
| Untested observational predictions (upcoming data) | 11 |
| Untested observational predictions (existing data) | 4 |
| Foundational assumptions untested | 8 |
| Conditional results requiring validation | 6 |
| **Total distinct open items** | **~90** |

---

## Audit Conclusion

The framework has 112+ permanent mathematical results and 141+ closed mechanisms -- an impressive constraint surface. But the audit reveals three structural patterns:

**Pattern 1: The EVOI queue is frozen.** All four Level 1 EVOI computations (TRANSIT-PS, LEGGETT-GRAV-DECAY, FUNCTIONAL-SELECT, BBN-VOLOVIK) have been queued since S66 and remain uncomputed after 6 sessions. The project has been computing increasingly refined subsidiary quantities (decoherence channels, spectral ratios, frustration effects) without addressing the decisive gates that control the framework's viability.

**Pattern 2: The carry-forward graveyard.** Twenty carry-forward items from S46-S47 have never been executed (25-26 sessions deferred). Two S46 numerical corrections have never been propagated. EFOLD-MAPPING-52, explicitly labeled "the single question to which 51 sessions reduce," remains incomplete after 21 additional sessions. The carry-forward mechanism is structurally broken: items that don't fit current session themes are silently abandoned.

**Pattern 3: The prediction-accommodation boundary is blurred.** S72 W2-C demonstrates that a positive f* matching n_s exists, but it introduces a free parameter. The Higgs mass from f* is 3x too low. The n_s prediction is either 1.95 sigma from Planck (bare, zero parameters) or 0 sigma (tuned via f*). The framework needs to decide which claim it makes and defend it.

The single highest-impact computation is EXIT-HORIZON-BOG-73, which resolves the A_s budget by computing the exit-horizon Bogoliubov coefficients. The single highest-impact mathematical question is the spectral functional selection principle. The single highest-impact external event is DESI DR3 (w_a < -0.530 excludes the framework).
