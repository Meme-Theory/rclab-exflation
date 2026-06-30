# Session 72 Master Audit Synthesis
## 6 Specialists, One Problem List

**Date**: 2026-04-10
**Auditors**: gen-physicist, mack, volovik, connes, landau, phonon-first
**Source**: 6 independent audit documents totaling ~2,500 lines
**Method**: Exhaustive cross-reference, deduplication by mathematical content, citation counting

---

## I. Executive Summary

Six independent audits -- covering general physics, observational confrontations, superfluid/mechanism-chain physics, NCG foundations, condensed-matter/BCS problems, and cross-domain connections -- were compiled and cross-referenced. The raw item count across all audits exceeds 200 entries. After aggressive deduplication (many items appear under different names in multiple audits), the project carries **~90 unique open items**: 7 framework-threatening critical problems, 9 high-priority uncomputed gates (4 EVOI Priority 1, all 6+ sessions overdue), 20 deferred carry-forwards from S46-S47 (25+ sessions old), 7 incomplete mathematical proofs, 7 unresolved numerical tensions, 11 untested observational predictions, and 8 foundational assumptions never derived from first principles.

The top 3 framework-threatening problems, ordered by convergent citation count:

1. **A_s amplitude normalization** (flagged by 6/6 auditors). The 0.267 OOM residual gap reduces to a single computable number -- t_dec/t_transit at the exit sonic horizon. The EXIT-HORIZON-BOG-73 computation is universally identified as the single most important open computation.

2. **Spectral functional selection** (flagged by 6/6 auditors). The best-fit f* = 0.912 sqrt + 0.088 exp matches n_s = 0.9649 but introduces a free parameter and has divergent SDW moments. Without a first-principles selection principle, n_s is accommodation, not prediction, and all SDW-derived quantities require recomputation via direct spectral sums.

3. **DESI w_0/w_a tension** (flagged by 4/6 auditors). The framework predicts w_0 = -0.918, w_a = 0. DESI DR2+DESY5 gives 2.91-sigma and 2.92-sigma tensions respectively. w_a = 0 is four-fold locked and cannot be adjusted. DESI DR3 (2026-2027) is the make-or-break external confrontation.

**THE single most important open computation**: EXIT-HORIZON-BOG-73 -- Bogoliubov transformation at the exit sonic horizon, determining the mode-dependent phase spread and greybody factors that set t_dec/t_transit. Cited as #1 priority by all 6 auditors.

---

## II. Framework-Threatening Problems (CRITICAL)

### CRIT-1. A_s Amplitude Normalization Gap (0.267 OOM)

- **Problem**: Power spectrum amplitude predicted ~1.85x too large. All spectral-geometric ratios (n_s, sin^2 theta_W, Omega_DM) match; all absolute amplitudes (A_s, CC) required corrections. The residual gap after all identified corrections (Leggett vacuum r_L = 0.617, PW selection, gap corrections) is 0.267 OOM.
- **Cited by**: gen-physicist, mack, volovik, connes, landau, phonon-first (6/6)
- **Current status**: S72 exhaustively tested 18 decoherence channels. Only KZ pair-crossing at the exit horizon is fast enough. Two models bracket the gate band: statistical KZ (t_dec = 0.13 t_transit, over-decohered) vs Bogoliubov KZ (t_dec = 2.2 t_transit, under-decohered). Gate band: t_dec/t_transit in [0.57, 0.88].
- **Resolution path**: EXIT-HORIZON-BOG-73. Compute mode-dependent Bogoliubov coefficients beta_k(tau_exit), greybody factors, and pair-crossing phase spread at the exit sonic horizon. Use s72_dual_decoherence.npz data plus S70 sonic horizon locations and S64 global Bogoliubov phases.
- **Effort**: HIGH (dedicated Bogoliubov solver -- WKB inapplicable per CHIRP-PENUMBRA-70 PERMANENT)
- **Timeline**: Must resolve before DESI DR3 (2026-2027) to complete the amplitude-level prediction suite

### CRIT-2. Spectral Functional Selection / n_s Accommodation

- **Problem**: n_s = 0.9567 (bare, zero parameters, 1.95 sigma from Planck) OR n_s = 0.9649 (f*-fitted, one free parameter t* = 0.088, 0 sigma). The f* that matches n_s predicts m_H ~ 39-51 GeV (excluded by 3x). The SDW expansion does not exist for f* (all moments diverge). No selection principle determines f* from the spectral triple.
- **Cited by**: gen-physicist, mack, volovik, connes, landau, phonon-first (6/6)
- **Current status**: EVOI P3 (FUNCTIONAL-SELECT-67). S72 W2-C proves existence of positive f* matching (n_s, A_s) jointly. S66-67 anomaly + conservation hierarchy constrains f to be monotone increasing. The one-parameter dilaton family is identified but no unique selection principle exists.
- **Resolution path**: Two routes. (A) Derive f from anomaly cancellation + BCS self-consistency (Eliashberg-type equation for f*(x), phonon-first Bridge 1). (B) Accept n_s = 0.9567 as the zero-parameter prediction and compute the compound tilt including entry-horizon corrections (COMPOUND-NS-73).
- **Effort**: HIGH (mathematical: route A requires new NCG selection principle; computational: route B requires full ordered Bogoliubov product)
- **Timeline**: CMB-S4 (2034) will tighten n_s to sigma ~ 0.002, discriminating between bare and f*-fitted

### CRIT-3. DESI w_0/w_a Tension (2.91 sigma both)

- **Problem**: Framework predicts w_0 = -0.918, w_a = 0 (four-fold locked: GGE integrability + Josephson + frozen texture + thermalization barrier). DESI DR2+DESY5 measures w_0 = -0.752 +/- 0.057, w_a = -0.73 +/- 0.25.
- **Cited by**: gen-physicist, mack, phonon-first, volovik (4/6)
- **Current status**: Pre-registered survival condition: w_a > -0.35. S72 W1-D Cauchy-Schwarz formula gives w_0 = -0.687, NOT -0.918 (category error: only Volovik partition gives -0.918). Scheme variation +/- 0.06 (S72 workshop). Even at extreme band (w_0 = -0.858), DESI tension is 1.86 sigma.
- **Resolution path**: No internal computation resolves this. Wait for DESI DR3 (2026-2027). If w_a < -0.530, framework excluded at 3 sigma.
- **Effort**: LOW (external data)
- **Timeline**: DESI DR3 (2026-2027) -- the nearest-term make-or-break confrontation

### CRIT-4. alpha_s Falsification Threat (5.0 sigma from smooth cutoff)

- **Problem**: alpha_s = -0.038 from smooth cutoff spectral functional, at 5.0 sigma from Planck (-0.0045 +/- 0.0067). S70 F0-ALPHA-S-70 FAIL shows f_0 and alpha_s are anti-correlated, making this structural. alpha_s = 0 is the tree-level prediction (from c_s^2 = 0, DERIVED), which is at 0.67 sigma -- but requires accepting the trivial-bundle restriction.
- **Cited by**: gen-physicist, mack, volovik (3/6)
- **Current status**: Five independent arguments establish slow-roll consistency relation r = 16 epsilon is inapplicable. ATDHFB bounds alpha_s to [-0.019, -0.008]. Full transit power spectrum (TRANSIT-PS-67, EVOI P1) remains uncomputed after 6 sessions.
- **Resolution path**: TRANSIT-PS-67. Full Bogoliubov power spectrum through the fold with dedicated solver (WKB FAIL permanent). Also: BRANCHING-JOSEPHSON-73 (branching-resolved Josephson couplings may break the f_0 anti-correlation).
- **Effort**: HIGH (dedicated Bogoliubov solver)
- **Timeline**: CMB-S4 (2034) will measure alpha_s to sigma ~ 0.003

### CRIT-5. Leggett DM Gravitational Stability

- **Problem**: The Leggett-channel GGE quasiparticle DM candidate (Omega_DM h^2 = 0.120, 0.7 sigma from Planck) must satisfy Gamma_grav < H_0. Z_2 parity protection is established (S67), pair decay lifetime is 4.93e82 s (65 OOM margin, S70), but the gravitational decay vertex through the a_2 channel has never been computed from first principles.
- **Cited by**: gen-physicist, mack, volovik, landau (4/6)
- **Current status**: EVOI P2 (17.4%). Queued since S66 (6 sessions overdue). NOT STARTED.
- **Resolution path**: LEGGETT-GRAV-DECAY-67. Perturbative graviton vertex computation: Leggett mode -> graviton emission through a_2 spectral moment coupling. Compare Gamma_grav to H_0.
- **Effort**: MEDIUM
- **Timeline**: No external deadline, but if FAIL, the entire DM sector collapses

### CRIT-6. BBN Volovik Tracking EOS

- **Problem**: Volovik Scenario B (CC PASS at 0.01 OOM) gives G_eff/G = 1.5 at BBN. This is at the edge of BBN bounds. The detailed expansion history with full tracking EOS (not just leading term) has not been computed.
- **Cited by**: gen-physicist, mack, volovik (3/6)
- **Current status**: EVOI P4 (14.0%). S67 BBN-VOLOVIK-67 gave |w_vac - 1/3| = 3.39e-41 (PASS), but G_eff/G = 1.5 is marginal. Full BBN computation with modified expansion history not executed. 6 sessions overdue.
- **Resolution path**: BBN-VOLOVIK-67. Run standard BBN code with Volovik rho_vac = M_Pl^2 H^2 tracking vacuum. Gate: primordial D/H and He-4 within 2 sigma of observed.
- **Effort**: MEDIUM
- **Timeline**: No external deadline, but unresolved tension with established BBN physics

### CRIT-7. K_pivot Scale Mapping / Expansion History

- **Problem**: Two physically motivated mappings for the CMB pivot scale give contradictory answers. Physical e-fold mapping gives K = 4.3e-57 M_KK (flat n_s = 1). Tessellation mapping gives K = 2.0 M_KK (excluded by convex combination theorem). Neither works. The entire cosmological prediction suite (n_s, alpha_s, sigma_8) is conditional on this mapping.
- **Cited by**: gen-physicist, phonon-first (2/6)
- **Current status**: EFOLD-MAPPING-52 first queued S51. Partial S64: N_e = 3.73e-3 physical transit. Full expansion history (stiff epoch + backreaction + radiation transition): NOT COMPUTED. 21 sessions without completion.
- **Resolution path**: Full expansion history computation from fold to present, including stiff-era dynamics, Volovik tracking transition, and radiation era. Determines a(t) or its substrate analog.
- **Effort**: HIGH
- **Timeline**: Oldest decisive open computation in the project (21 sessions deferred)

---

## III. High-Priority Open Computations

### EVOI Priority 1 (all queued since S66, 6 sessions overdue)

| # | Computation | EVOI | Status | Flagged by (count) |
|:--|:-----------|:-----|:-------|:-------------------|
| 1 | **TRANSIT-PS-67**: Full Bogoliubov power spectrum through fold | 22.5% | NOT STARTED. WKB inapplicable (permanent). Dedicated solver mandatory. | gen, mack, volovik (3/6) |
| 2 | **LEGGETT-GRAV-DECAY-67**: Gravitational decay vertex | 17.4% | NOT STARTED | gen, mack, volovik, landau (4/6) |
| 3 | **BBN-VOLOVIK-67**: Volovik tracking EOS at T_BBN | 14.0% | NOT STARTED | gen, mack, volovik (3/6) |
| 4 | **FUNCTIONAL-SELECT-67**: Derive physical spectral functional | 13.2% | PARTIAL (S72 W2-C: f* exists with free parameter) | gen, mack, volovik, connes, landau, phonon-first (6/6) |

### EVOI Priority 2 (queued since S66-S67)

| # | Computation | EVOI | Status | Flagged by |
|:--|:-----------|:-----|:-------|:-----------|
| 5 | BA-LIFETIME-FABRIC-67 | 6.5% | NOT STARTED | mack (1/6) |
| 6 | JOINT-FALSIFICATION-67 | 7.2% | NOT STARTED | gen (1/6) |
| 7 | BAYESIAN-FUNCTIONAL-67 | 7.0% | NOT STARTED | gen (1/6) |
| 8 | GGE-BISPECTRUM-67 | 4.8% | PARTIAL (S72 W4-A: f_NL = -0.313 from Bogoliubov only) | gen, mack (2/6) |
| 9 | PROJECTED-MOMENTS-67 | 5.0% | NOT STARTED | gen (1/6) |

### S72-Generated Critical Computations

| # | Computation | Source | Priority | Flagged by |
|:--|:-----------|:-------|:---------|:-----------|
| 10 | **EXIT-HORIZON-BOG-73**: Bogoliubov coefficients at exit horizon | S72 synthesis | CRITICAL | ALL 6/6 |
| 11 | **SPECTRAL-ACTION-PROFILE-73**: S(tau) for tau in [0, 2] via direct sum with f* | S72 Mack-VdD | CRITICAL | gen, mack, volovik, connes, phonon-first (5/6) |
| 12 | **COMPOUND-NS-73**: Total n_s including entry-horizon pre-squeeze (delta_n_s = +1.001) | S72 W3-C | CRITICAL | volovik, phonon-first, mack (3/6) |
| 13 | **BRANCHING-JOSEPHSON-73**: Branching-resolved J_C2^{SU(2)} vs J_C2^{U(1)} | S72 Landau-Baptista | CRITICAL | gen, landau (2/6) |
| 14 | **THRESHOLD-RATIOS-73**: PW-sector-resolved delta_1/delta_3 at tau_fold | S72 W2-B | HIGH | gen, connes, phonon-first, landau (4/6) |

---

## IV. Carry-Forward Graveyard

### Atlas-08 Carry-Forwards (20 items, S46-S47, none executed through S72)

| CF# | Item | Original Session | Age (sessions) | Current Relevance |
|:----|:-----|:-----------------|:---------------|:------------------|
| CF1 | TT 2-tensor Lichnerowicz | S47 | 25 | STILL NEEDED -- no alternative computation of 2-tensor on spectral triple |
| CF2 | Q-theory Goldstone self-tuning | S47 | 25 | SUPERSEDED -- Q-theory CC route CLOSED (S62). Goldstone mass itself still relevant. |
| CF3 | Sakharov curvature-weighted sum | S47 | 25 | STILL NEEDED -- tests G_N improvement from 0.36 OOM |
| CF4 | Three-phonon vertex | S46 | 26 | STILL NEEDED -- omega_B2 ~ 2*omega_B1 resonant friction untested |
| CF5 | DISSOLUTION-BERRY-47 | S46 | 26 | STILL NEEDED -- pi-phase survival |
| CF6 | CLOSED-LOOP-47 | S46 | 26 | STILL NEEDED -- round-trip Berry consistency |
| CF7 | Sector-resolved pair ratio | S46 | 26 | STILL NEEDED -- CPT symmetry test |
| CF8 | (2,1) pi-phase count = 5 | S46 | 26 | STILL NEEDED -- derivation |
| CF9 | GIBBS-DUHEM-GGE | S46 | 26 | STILL NEEDED -- 20% Zubarev/Keldysh discrepancy unresolved |
| CF10 | Keldysh sigma (pair-pair) | S46 | 26 | STILL NEEDED -- feeds CF9 |
| CF11 | LOG-SIGNED-40 | S40 | 32 | STILL NEEDED -- signed B-F log sum on 2912 eigenvalues |
| CF12 | PHI-GOLDEN-22 | S47 | 25 | SUPERSEDED by S72 eigenvalue convergence studies |
| CF13 | Six-sequence test | S47 | 25 | STILL NEEDED -- zero cost |
| CF14 | Swampland c(tau) | S47 | 25 | SUPERSEDED -- S48 Swampland PASS (c = 52.8, permanent) |
| CF15 | Poisson-Lie T-duality | S47 | 25 | STILL NEEDED -- monotonicity in dual frame |
| CF16 | Chladni patterns | S47 | 25 | STILL NEEDED -- eigenvector retention |
| CF17 | C^2 isotropization | S47 | 25 | STILL NEEDED -- Lifshitz transition |
| CF18 | Anisotropic KZ defects | S47 | 25 | STILL NEEDED -- feeds decoherence budget |
| CF19 | Akama-Diakonov metric | S47 | 25 | STILL NEEDED -- analog horizon |
| CF20 | 279-mode tachyonic velocity | S46 | 26 | STILL NEEDED -- completeness |

**Tally**: 15 STILL NEEDED, 3 SUPERSEDED, 2 partially superseded (retain sub-component).

### Decisive Computations Deferred >20 Sessions

| Computation | First Queued | Age | Status |
|:------------|:-------------|:----|:-------|
| EFOLD-MAPPING-52 | S51 | 21 sessions | PARTIAL (S64: N_e = 3.73e-3). Full expansion history NOT COMPUTED. |
| Self-Consistent HFB Gap (Q15) | S47 | 25 sessions | NOT STARTED. Mean-field overestimates by 60%. Nazarewicz priority 1. |
| Non-Abelian Berry Phase Wilson Loop (Q14) | S46 | 26 sessions | NOT STARTED. Computable with existing code. |
| Complete A_F Extraction (Q11) | S10 | 62 sessions | CONDITIONAL. o-map route identified, never executed. |

### Unpropagated Corrections

| Correction | Age | Status |
|:-----------|:----|:-------|
| alpha* = 3.91 -> 0.775 (FN-CENTROID-47) | 26 sessions | Never propagated |
| CHAOS-1 <r> = 0.321 -> 0.439 | 25 sessions | Acknowledged, never recomputed |

---

## V. Structural Gaps

### V-1. Order-One Condition for D_total (Axiom 5 FAIL)

- **Status**: FAIL. Maximum violation 4.000 at (H,H). 6/7 NCG axioms pass; this one does not.
- **Flagged by**: gen-physicist, connes (2/6)
- **Escape routes**: Weak order-one CLOSED (S45). BdG twist CLOSED (S46). CCS 2013 formalism OPEN (169 extra Omega^1_D directions). Pati-Salam extension OPEN (S63 PS-KASPAROV-63 PASS).
- **Impact**: The spectral action is unaffected. The fermionic action and Higgs mechanism may be modified by the 169 additional scalar directions from the CCS formalism.

### V-2. KO-Dimension Mismatch (Product KO=4, Finite KO=6)

- **Status**: PERMANENT mismatch. Product KO(M^4 x SU(3)) = 4 + 0 = 4, but finite triple KO = 6.
- **Flagged by**: connes (1/6)
- **Impact**: epsilon'' = +1 instead of -1 changes the chirality condition on physical fermions. Impact on mass predictions and Yukawa couplings is UNCOMPUTED.

### V-3. SDW Expansion Non-Existence for f*

- **Status**: PERMANENT. f* = 0.912 sqrt + 0.088 exp has divergent SDW moments (f_0 = infinity). The asymptotic expansion S ~ f_0 a_0 Lambda^4 + ... does not exist.
- **Flagged by**: gen-physicist, connes, landau, phonon-first (4/6)
- **Impact**: All predictions depending on individual SDW coefficients (a_0, a_2, a_4 independently) must be recomputed via direct spectral sums. The first ~3 SDW coefficients are still reliable as truncation-independent ratios, but individual moment values are undefined for f*.

### V-4. tau-to-Cosmic-Time Mapping (Assumption C1)

- **Status**: ASSUMED since S1. Never derived from 12D Einstein equations reduced to M^4 x SU(3). DeWitt supermetric G_mod = 5.0 computed but coupling to FRW is approximate.
- **Flagged by**: gen-physicist, volovik, connes, phonon-first (4/6)
- **Impact**: Core framework postulate. If wrong, the entire spectral-action-to-cosmology chain disconnects.

### V-5. 4D Effective Action for Modulus Dynamics (Q8)

- **Status**: No first-principles derivation of the modulus kinetic term from the path integral. SA penalizes BCS pairing (wrong sign, 93x). SA may be categorically wrong as modulus potential.
- **Flagged by**: gen-physicist, connes (2/6)

### V-6. n_s > 1 Structural Proof (Contradictory Status)

- **Status**: Listed as PROVEN in atlas-04 P3 but "unvalidated" in atlas-07 D13. Contradictory between atlas documents. Claimed: bare Dirac heat kernel on any compact manifold gives n_s >= 1; red tilt requires dynamics.
- **Flagged by**: gen-physicist (1/6)

### V-7. Three Generations Not From Axioms

- **Status**: Framework CLAIMS three generations from Z_3 x Z_3 quantum number on PW sectors. Standard NCG treats generation number as INPUT, not OUTPUT. Plausible conjecture, not proven.
- **Flagged by**: connes (1/6)

---

## VI. Observational Confrontations

### Imminent (2026-2027): DESI DR3 -- SURVIVAL OR EXCLUSION

| Scenario | DR3 Outcome | FW Tension | FW Status |
|:---------|:------------|:----------:|:---------:|
| A: confirms DR2 | w_0 = -0.75, w_a = -0.73 | 3.91 sigma | **EXCLUDED** |
| B: toward LCDM | w_0 = -0.90, w_a = -0.30 | ~2.1 sigma | **SURVIVES** |
| C: more dynamical | w_0 = -0.65, w_a = -1.0 | 6.33 sigma | **EXCLUDED** |

Decision rule: w_a > -0.35 survives. w_a < -0.530 excluded at 3 sigma.
Survival condition: FW is STRUCTURALLY LOCKED (w_a = 0, four-fold protected). Cannot be adjusted.
**Flagged by**: gen-physicist, mack, volovik, phonon-first (4/6)

### Near-Term (2028-2032)

| Experiment | What It Tests | FW Prediction | Timeline |
|:-----------|:-------------|:-------------|:---------|
| JUNO / Hyper-K | Neutrino mass ordering | Normal (BDI structural) | 2028-2030 |
| Euclid DR1 | ISW tracking (c_s^2 = 0) | +7.6% vs quintessence, SNR 1.58 | 2029 |
| Euclid DR1 | f*sigma_8 | chi^2/dof = 0.761 (beats LCDM) | 2029 |
| Euclid + CMB-S4 | Lensing C_l^{kk} | -1.29% suppression | 2030+ |
| DUNE | Mass ordering (5 sigma) | Normal | 2032 |

### Medium-Term (2034)

| Observable | FW Prediction | Precision | Significance |
|:-----------|:-------------|:----------|:-------------|
| r (LiteBIRD) | 0.024 | sigma = 0.001 | 24-sigma detection |
| n_s (CMB-S4) | 0.957-0.965 | sigma = 0.002 | Mode B kill test |
| alpha_s (CMB-S4) | ~0 (tree) | sigma = 0.003 | Discrimination window |
| f_NL equil (CMB-S4) | -0.31 to 0.85 | sigma = 5.0 | Undetectable |

### Long-Term (2035-2040s)

| Observable | FW Prediction | Instrument | SNR |
|:-----------|:-------------|:-----------|:----|
| Omega_GW (domain walls) | ~10^{-10} | LISA | Detectable if > 10^{-11} |
| f_NL folded (unique discriminant) | 0.129 | 21cm tomography | 3.6 sigma |
| ISW tracking (unique discriminant) | +7.6% vs quint | 21cm intensity | 7.9 sigma |

**Missing error budgets** (flagged by mack): f_NL sign discrepancy (S67 vs S72), Omega_GW spectral shape (LISA needs sigma), ISW Gamma sensitivity, r uncertainty propagation.

---

## VII. Cross-Domain Bridges Missing

### Bridge 1: Spectral Functional -> BCS Self-Consistency (6/6 auditors)

The spectral functional f*(x) selected by observation has no derivation from the spectral triple. An Eliashberg-type self-consistency between pairing interaction and spectral weight has never been formulated. This is simultaneously the deepest NCG gap (connes), the deepest condensed-matter gap (landau), and the central prediction-vs-accommodation question (gen-physicist, mack, volovik, phonon-first).

### Bridge 2: KK Thresholds -> Gauge Coupling Running (4/6 auditors)

sin^2(theta_W) = 0.5839 at M_KK (permanent). Pure SM running gives 0.357 at M_Z (54.5% FAIL). Universal thresholds give 0.229 (1.2%). The PW-sector-resolved branching SU(3) -> SU(2) x U(1) at tau_fold that determines the threshold ratios has never been computed. Flagged by gen-physicist, connes, landau, phonon-first.

### Bridge 3: GGE Integrability -> Spectral Dimension (2/6 auditors)

Richardson-Gaudin integrability protects the GGE. Does it also protect the spectral dimension from fluctuations? The spectral dimension of the GGE STATE (not vacuum) on CG(24) is uncomputed. The GGE occupation numbers alter the spectral weight. Flagged by phonon-first, volovik.

### Bridge 4: CG(24) Entanglement -> Bekenstein-Hawking (2/6 auditors)

Area law on CG(24) established (R^2 = 0.988). Connection to S_BH = A/(4G) through the spectral action is conceptual (S70 Hawking workshop) but the numerical check -- whether per-edge entanglement s_edge = 1.386 nats relates to 1/(4G) in Planck units -- has never been computed. Flagged by phonon-first, gen-physicist.

### Bridge 5: Volovik Partition -> BCS Spectral Function (2/6 auditors)

The S72 workshop corrected the Volovik two-fluid partition: it is NOT Landau two-fluid hydrodynamics. The correct mapping is to the BCS spectral function A(k, omega). This function has never been computed on the 8-mode BCS system at the fold. Its first moment should reproduce w_0 = -0.918. Flagged by phonon-first, volovik.

### Bridge 6: Entry-Horizon Tilt -> Compound n_s (3/6 auditors)

S72 W3-C finds delta_n_s = +1.001 from the entry horizon -- an O(1) correction. The bare prediction n_s = 0.9567 does NOT include this. Whether the correction is additive (giving absurd n_s ~ 2.0) or modifies the slope per unit ln(omega) is UNRESOLVED. The compound Bogoliubov product through the full transit (entry + fold + exit) has never been computed. Flagged by volovik, phonon-first, mack.

---

## VIII. Convergent Findings

Items independently identified by 4+ auditors. These are the real priorities.

### 8.1 Exit-Horizon Bogoliubov Coefficients (6/6)

Every auditor, without exception, identifies this as the #1 open computation. The mathematical problem is well-posed: compute beta_k(tau_exit) for each BCS mode k at the exit sonic horizon, extract the mode-dependent phase spread delta_phi, and determine whether the KZ pair-crossing timescale falls in [0.57, 0.88] t_transit. This resolves A_s, the framework's most glaring quantitative failure.

### 8.2 Spectral Functional Selection Principle (6/6)

Every auditor flags the absence of a selection principle for f(x). The consensus: without one, n_s is accommodation. The S72 W2-C result that f* exists but has divergent SDW moments forces a method change (direct spectral sums), which no auditor disputes. The disagreement is on urgency: volovik and phonon-first rank it below exit-horizon; connes ranks it as Priority 2 (NCG); gen-physicist and mack note it is existentially important but computationally less tractable.

### 8.3 Leggett Gravitational Decay (4/6)

gen-physicist, mack, volovik, landau all flag LEGGETT-GRAV-DECAY-67 as a binary gate with delta_P(fail) = -30%. If FAIL, the entire DM sector (Omega_DM h^2 = 0.120 match) is vacuous. 6 sessions overdue, effort MEDIUM, and NOT STARTED.

### 8.4 S(tau) Full Profile Beyond Fold (5/6)

gen-physicist, mack, volovik, connes, phonon-first identify SPECTRAL-ACTION-PROFILE-73 as a three-in-one computation: it simultaneously determines (a) post-transit equilibrium existence, (b) late-time CC, and (c) expansion history w(z). Only landau omits it (focusing on BCS-specific problems).

### 8.5 PW-Sector Threshold Corrections (4/6)

gen-physicist, connes, landau, phonon-first flag the PW-sector-resolved KK threshold ratios as the decisive test for sin^2(theta_W) at M_Z. The 34.6% gap between SM running and geometric boundary condition must be bridged by these thresholds.

### 8.6 SDW Non-Existence for f* Requires Method Change (4/6)

gen-physicist, connes, landau, phonon-first flag that f* having divergent SDW moments is not merely inconvenient -- it forces ALL predictions previously derived from individual SDW coefficients to be recomputed via direct spectral sums. This is structural, not a one-time fix.

### 8.7 tau-Cosmic-Time Mapping Never Derived (4/6)

gen-physicist, volovik, connes, phonon-first flag that assumption C1 (tau = cosmic time) has been the framework's core postulate since S1 and has never been derived from the 12D Einstein equations. This is a 72-session-old foundational gap.

---

## IX. Divergent Assessments

### 9.1 Severity of n_s = 0.9567 (1.95 sigma)

- **gen-physicist**: Lists as framework-threatening (CRIT-2). The accommodation-vs-prediction boundary is blurred.
- **mack**: Active tension, Mode B failure mode. Scheme-dependent (functional layer).
- **volovik**: CONDITIONAL. The entry-horizon O(1) tilt revision (W3-C) makes the compound prediction mandatory before assessing severity.
- **connes**: Priority 7 (compound tilt) -- important but downstream of spectral functional.
- **landau**: Not in top 5 (BCS dressing permanently negligible, so this is a spectral layer problem).
- **phonon-first**: Unresolved internal inconsistency (delta_n_s = +1.001 could destroy or save the prediction).

**Assessment**: The disagreement is on the ROUTE to resolution. All agree n_s is conditional. volovik and phonon-first emphasize the entry-horizon complication; connes and gen-physicist emphasize the spectral functional; landau correctly notes it is not a BCS problem.

### 9.2 Severity of Order-One Axiom FAIL

- **connes**: Priority 1 for NCG foundations. The single failing axiom.
- **gen-physicist**: Lists in structural gaps but below observational priorities.
- **Other auditors**: Do not flag it.

**Assessment**: The order-one failure affects the fermionic action, not the spectral action. All topological and metric-layer predictions are unaffected. Connes correctly identifies it as the deepest NCG gap; the observationally-focused auditors correctly deprioritize it for S73 planning.

### 9.3 Urgency of DESI DR3 Preparation

- **mack**: CRITICAL -- front-loaded, make-or-break within 1 year. No internal computation resolves it.
- **gen-physicist**: Lists as computation monitoring.
- **volovik**: Framework is structurally locked (w_a = 0). Nothing to compute.
- **Other auditors**: Acknowledge tension without prescribing action.

**Assessment**: Consensus that DESI DR3 is existential, but consensus also that no internal computation changes the prediction. The framework lives or dies on external data here.

### 9.4 Off-Jensen Dynamics Importance

- **phonon-first**: Flags off-Jensen BCS spectrum (abandoned since S58) as relevant.
- **connes**: Notes off-Jensen flow for spectral action is unexplored.
- **gen-physicist**: Lists off-Jensen 5D Hessian at Level 2.
- **volovik, landau, mack**: Do not flag.

**Assessment**: Off-Jensen dynamics is a legitimate structural gap but lower priority than the five items with 4+ citations.

---

## X. Priority-Ordered Master Agenda for S73

The following is the definitive computation list for S73, ordered by convergent citation count, EVOI, and downstream impact. Each item is specified with sufficient detail for prompt generation.

### computation: MUST COMPUTE (cited by 4+ auditors, framework-defining)

**1. EXIT-HORIZON-BOG-73** -- Exit-Horizon Bogoliubov Coefficients
- **What**: Compute mode-dependent Bogoliubov coefficients beta_k(tau_exit) at the exit sonic horizon (tau ~ 0.160). Extract greybody factors, phase spread delta_phi per mode, and pair-crossing timescale distribution. Include CG(24) anisotropy (11.8x, S63) and Mott charge noise coupling (delta_phi ~ 0.5 estimate).
- **Why**: Resolves A_s amplitude normalization (0.267 OOM gap), the #1 open problem cited by ALL 6 auditors.
- **Input**: s72_dual_decoherence.npz, S70 sonic horizon locations (tau_entry = 0.220, tau_exit = 0.160), S64 global Bogoliubov phases (phi_Bog = pi, delta_phi = 2.4e-4), S63 anisotropy distribution, canonical_constants.py.
- **Output**: t_dec/t_transit with uncertainty band. Mode-dependent delta_OOM contributions.
- **Gate**: t_dec/t_transit in [0.57, 0.88] -> PASS. Outside -> FAIL or INFO depending on direction.
- **Effort**: HIGH
- **Flagged by**: gen-physicist, mack, volovik, connes, landau, phonon-first (6/6)

**2. LEGGETT-GRAV-DECAY-73** -- Leggett Mode Gravitational Decay Width
- **What**: Compute the gravitational decay vertex for the Leggett-channel GGE quasiparticle. The Leggett mode couples to gravity through the a_2 spectral moment (second Seeley-DeWitt coefficient generates G_N). Calculate Gamma_grav from the spectral action coupling and compare to H_0.
- **Why**: Binary gate with delta_P(fail) = -30%. If FAIL, the Omega_DM h^2 = 0.120 match is vacuous.
- **Input**: Leggett mode parameters (omega_L1 = 0.138 M_KK, Q = 18.6, Z = 0.972), a_2 coefficient at fold, Z_2 parity structure (S67).
- **Output**: Gamma_grav in units of H_0.
- **Gate**: Gamma_grav < H_0 -> PASS. Gamma_grav > H_0 -> FAIL (DM sector collapses).
- **Effort**: MEDIUM
- **Flagged by**: gen-physicist, mack, volovik, landau (4/6)

**3. SPECTRAL-ACTION-PROFILE-73** -- Full S(tau) from Direct Spectral Sums
- **What**: Compute S[f*, D_K(tau)] via direct eigenvalue sum (NOT SDW expansion, which diverges for f*) for tau in [0, 2.0] at L_max = 7, sampling 50+ tau values. This simultaneously determines: (a) whether a post-transit equilibrium exists, (b) the late-time CC value, (c) the expansion history shape w(z).
- **Why**: Three-in-one computation. Without the global S(tau), moduli stabilization, CC, and w(z) are all undetermined.
- **Input**: D_K eigenvalues at L_max = 7 for tau grid, f*(x) = 0.912 sqrt(x) + 0.088 exp(-x), volume-preserving constraint.
- **Output**: S(tau) profile with identified extrema. tau_eq (equilibrium) location. w(z) from S''(tau)/S'(tau).
- **Gate**: Stable minimum at tau_eq in [0.19, 1.0] -> PASS (moduli stabilized). No minimum -> FAIL (no equilibrium, framework physically incomplete).
- **Effort**: HIGH
- **Flagged by**: gen-physicist, mack, volovik, connes, phonon-first (5/6)

**4. THRESHOLD-RATIOS-73** -- PW-Sector Resolved KK Thresholds
- **What**: Compute the branching decomposition SU(3) -> SU(2) x U(1) for each PW sector (p,q) at tau_fold = 0.19, L_max >= 7. Extract threshold correction ratios delta_1/delta_3 and delta_2/delta_3. Determine whether sin^2(theta_W) runs correctly from 0.5839 at M_KK to 0.231 at M_Z.
- **Why**: Resolves WEINBERG-72 FAIL (54.5% gap under pure SM running) vs Model A (1.2% match with universal thresholds).
- **Input**: D_K eigenvalues by sector, SU(3) branching rules, RG beta functions.
- **Output**: delta_1/delta_3, delta_2/delta_3 at fold. sin^2(theta_W) at M_Z from full threshold-corrected running.
- **Gate**: |sin^2(M_Z) - 0.23122| < 0.035 -> PASS. |delta| > 0.10 -> FAIL.
- **Effort**: MEDIUM
- **Flagged by**: gen-physicist, connes, landau, phonon-first (4/6)

### PRIORITY 1: HIGH PRIORITY (cited by 3+ auditors or EVOI > 10%)

**5. COMPOUND-NS-73** -- Entry + Fold + Exit Compound Tilt
- **What**: Compute the total n_s from the ordered Bogoliubov product through the full transit sequence: entry horizon (tau = 0.220) -> fold (tau = 0.190) -> exit horizon (tau = 0.160). S72 W3-C gives delta_n_s = +1.001 from the entry horizon alone; the compound product including the fold squeeze and exit-horizon decoherence is uncomputed.
- **Why**: Resolves whether n_s = 0.9567 (bare) or requires entry-horizon correction.
- **Input**: S72 W3-C entry-horizon parameters, S64 fold Bogoliubov phases, canonical transit parameters.
- **Output**: n_s(compound) with uncertainty from non-additive corrections.
- **Gate**: |n_s - 0.9649| < 0.0042 -> PASS. |n_s - 0.9649| > 0.010 -> FAIL.
- **Effort**: HIGH
- **Flagged by**: volovik, phonon-first, mack (3/6)

**6. BBN-VOLOVIK-73** -- Full BBN with Volovik Tracking EOS
- **What**: Run standard BBN code (PArthENoPE or AlterBBN) with modified expansion history incorporating Volovik tracking vacuum rho_vac = M_Pl^2 H^2. Compute primordial D/H, He-4 mass fraction Y_p, and Li-7 abundance. Compare to observational constraints.
- **Why**: G_eff/G = 1.5 at BBN is marginal. The only surviving CC mechanism must not violate BBN.
- **Input**: Volovik Scenario B parameters, standard nuclear reaction rates.
- **Output**: Y_p, D/H, Li/H with uncertainties.
- **Gate**: Y_p within 2 sigma of 0.245 +/- 0.003 AND D/H within 2 sigma of (2.55 +/- 0.03) x 10^{-5}.
- **Effort**: MEDIUM
- **Flagged by**: gen-physicist, mack, volovik (3/6)

**7. BRANCHING-JOSEPHSON-73** -- Representation-Resolved Josephson Couplings
- **What**: Compute branching-resolved Josephson couplings J_C2^{SU(2)} and J_C2^{U(1)} from the PW decomposition of the C^2 coset overlap at tau_fold. Determine whether representation selectivity breaks the f_0 anti-correlation between alpha_s and m_H.
- **Why**: If J_C2^{SU(2)} != J_C2^{U(1)}, the non-perturbative Josephson correction (~679) breaks the universal f_0 dependence, potentially resolving the alpha_s/m_H anti-correlation.
- **Input**: PW-sector overlap integrals for C^2 coset generators at fold, BCS gap parameters.
- **Output**: J_C2^{SU(2)}, J_C2^{U(1)}, ratio.
- **Gate**: |J_C2^{SU(2)}/J_C2^{U(1)} - 1| > 0.1 -> PASS (selectivity exists). < 0.01 -> FAIL (universal).
- **Effort**: MEDIUM
- **Flagged by**: gen-physicist, landau (2/6), but feeds CRIT-4 (alpha_s) which is flagged by 3/6

### PRIORITY 2: IMPORTANT (cited by 2+ auditors, fills significant gaps)

**8. TRANSIT-PS-67** -- Full Bogoliubov Power Spectrum Through Fold
- **What**: Compute P(k) from the full Bogoliubov transformation through the van Hove fold using a dedicated ODE solver (WKB inapplicable: CHIRP-PENUMBRA-70 PERMANENT). Determines alpha_s(k_CMB), A_s, and full n_s(k) simultaneously.
- **Why**: EVOI P1 (22.5%). 6 sessions overdue. The only route to the full power spectrum.
- **Input**: D_K eigenvalues, transit velocity profile, BCS parameters.
- **Output**: P(k) across 8 BCS modes. alpha_s at k_CMB.
- **Gate**: alpha_s in [-0.020, +0.005] -> PASS.
- **Effort**: HIGH
- **Flagged by**: gen-physicist, mack, volovik (3/6)

**9. EXACT-POMERAN-Z6** -- Exact Pomeranchuk at Physical Coordination
- **What**: Exact diagonalization of 4-cell BCS + Josephson Hamiltonian at z = 6 (physical CG(24) coordination number). Perturbative RPA predicts instability at z_crit = 4.1 < 6, but this is expected to be an artifact.
- **Why**: If physical coordination IS Pomeranchuk-unstable, the BCS condensate at the fold is qualitatively different.
- **Input**: BCS Hamiltonian parameters, Josephson couplings at fold.
- **Output**: min(1 + F_l) across Landau channels.
- **Gate**: min(1 + F) > 0 -> PASS (stable). < 0 -> FAIL.
- **Effort**: MEDIUM
- **Flagged by**: landau (1/6), but binary gate affecting fold stability

**10. MULTI-CELL-INTEGRABILITY-73** -- Level Statistics at N_pair = 4
- **What**: Level statistics of multi-cell BCS + Josephson Hamiltonian at N_pair = 4 on 4-cell CG(24) subgraph. Tests whether Richardson-Gaudin integrability extends to the multi-cell system.
- **Why**: If integrability breaks at N_pair > 2, GGE is only approximate.
- **Input**: Multi-cell Hamiltonian matrix.
- **Output**: Level spacing ratio <r>.
- **Gate**: <r> < 0.45 (Poisson, integrable) -> PASS. <r> > 0.50 (Wigner-Dyson) -> FAIL.
- **Effort**: MEDIUM
- **Flagged by**: landau, volovik (2/6)

### PRIORITY 3: STRUCTURAL REFINEMENT

**11. SELF-CONSISTENT-GAP-PROFILE** -- Full V_eff(tau) HFB Solve
- **What**: Solve BCS gap equation self-consistently at 20 tau values in [0.14, 0.25].
- **Gate**: d(Delta)/dtau agrees with W1-A within 10%.
- **Flagged by**: landau, volovik (2/6)

**12. SDW-VALIDATION-DIRECT-SUM** -- Validate a_0, a_2, a_4 Under f*
- **What**: Compute spectral action via direct sum at canonical tau values. Compare to SDW-derived values.
- **Gate**: Ratio within 5% for a_0/a_2 and a_2/a_4.
- **Flagged by**: gen-physicist, connes, phonon-first (3/6)

**13. VIRTUAL-PARTICLE-73** -- Single-Mode Perturbation Decay on CG(24)
- **What**: Introduce delta_n_k perturbation on one cell, evolve under BCS + Josephson, measure decay rate and spatial extent.
- **Gate**: Gamma_virt > Gamma_Josephson AND off-shell spectral component.
- **Flagged by**: phonon-first (1/6)

**14. ORDER-ONE-CCS-73** -- CCS 2013 Formalism on D_K
- **What**: Compute inner fluctuations from full 342-dimensional Omega^1_D without order-one condition. Identify the 169 additional scalar directions.
- **Gate**: Physical predictions (Higgs mass, gauge couplings) compatible with observation.
- **Flagged by**: connes (1/6)

### PRIORITY 4: MONITORING

**15. DESI DR3** -- External data, no internal computation.
**16. JUNO mass ordering** -- 2028.
**17. Euclid ISW/lensing** -- 2029+.
**18. ALPHA-ENV-43** -- When survey data available (29 sessions overdue).

---

## Summary Statistics

| Category | Count |
|:---------|------:|
| Unique open items after deduplication | ~90 |
| Framework-threatening critical problems | 7 |
| EVOI Priority 1 computations uncomputed (6 sessions overdue) | 4 |
| S72-generated critical computations | 5 |
| Atlas-08 carry-forwards never executed | 15 still needed |
| Decisive computations deferred >20 sessions | 4 |
| Unresolved numerical tensions | 7 |
| Incomplete mathematical proofs / structural gaps | 7 |
| Observational confrontations with dates | 11 |
| Cross-domain bridges missing | 6 |
| Items cited by 4+ auditors (convergent) | 7 |
| Items with auditor disagreement | 4 |
| S73 Master Agenda items | 18 (4 computation, 3 Level 1, 3 Level 2, 4 Level 3, 4 Level 4) |

### The Three Structural Patterns (confirmed by all auditors)

**Pattern 1: The EVOI queue is frozen.** All four Level 1 EVOI computations have been queued since S66 (6 sessions, ~10 days). The project computes refined subsidiary quantities while decisive gates remain untouched.

**Pattern 2: The carry-forward graveyard.** 15 carry-forward items from S46-S47 remain relevant and uncomputed after 25-26 sessions. EFOLD-MAPPING-52 ("the single question to which 51 sessions reduce") is 21 sessions deferred. The carry-forward mechanism is structurally broken.

**Pattern 3: f* forces method change.** The spectral functional selected by observation (f* = 0.912 sqrt + 0.088 exp) has divergent SDW moments. This is not a fixable bug -- it permanently requires all spectral action computations to use direct eigenvalue sums rather than the Seeley-DeWitt expansion. This methodological shift propagates through the entire computational infrastructure.

---

*This synthesis is the canonical reference for S73 planning. Section X (Master Agenda) feeds directly into /rclab-plan. Gate verdicts are permanent. Citation counts are from 6 independent audits performed without inter-auditor communication.*
