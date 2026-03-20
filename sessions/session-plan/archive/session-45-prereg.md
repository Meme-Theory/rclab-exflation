# Session 45 Pre-Registered Gates

**Date**: 2026-03-15
**Source**: S44 collab reviews (9 specialists), S44 quicklook, S44 master synthesis, S22 transit constraint comparison, S44 data provenance audit
**Prior**: 23% (S44 Sagan, 68% CI 13-37%)
**Decisive computation**: OCC-SPEC-45 (6/7 convergence on Bogoliubov n_s; Connes identified occupied-state route)

---

## Priority Tiers

### TIER 1: CRITICAL PATH (Session-defining)

#### OCC-SPEC-45: Occupied-State Spectral Action Minimum Search
- **Full spec**: `sessions/session-plan/s45-prereg-occupied-state.md`
- **Agent**: connes-ncg-theorist (primary), nazarewicz (cross-check)
- **Gate**: PASS if S_occ(tau) has local minimum at tau_min in [0.10, 0.35] with barrier > 1%. FAIL if monotone.
- **Why critical**: Sole surviving tau-stabilization route within spectral action. Paper 16 (Dong-Khalkhali-van Suijlekom 2022) finite-density extension. S37 monotonicity theorem does NOT apply to occupation-weighted sums. S22 found ~1 e-fold at tau=0.3 from vacuum potential — occupied-state functional may have a deeper feature there.
- **Landau framing**: The spectral action (one-body) weighted by BCS state (many-body) = Landau free energy evaluated at the physical state. This is where the one-body/many-body partition dissolves.

#### KZ-NS-45: Kibble-Zurek Bogoliubov Spectrum for n_s
- **Agent**: volovik-superfluid-universe-theorist (primary), einstein (cross-check)
- **Convergence**: 6/7 S44 collab reviewers independently proposed this
- **Gate**: PASS if n_s in [0.955, 0.975] from Bogoliubov coefficients. FAIL if n_s outside [0.80, 1.10].
- **Method**: Compute |beta_k|^2 = (Delta E_k)^2 / (4 E_k^{in} E_k^{out}) for Parker-type particle creation during transit. P(k) = |beta_k|^2. n_s - 1 = d ln|beta_k|^2 / d ln k at pivot scale. Use S38 sudden-quench parameters (P_exc = 1.000, S_inst = 0.069).
- **Why critical**: Both static n_s routes FAILED in S44 (Lifshitz eta CLOSED at 889σ, DIMFLOW unpredictive without scale selection). Volovik cross-check: "n_s is quench dynamics, not internal geometry." This is the DYNAMICAL route.
- **Sagan assessment**: PASS → BF 10-20, P > 50%. FAIL → BF 0.3, P ~ 8%.
- **Connection to S22**: S22 found epsilon < 1 in [0.11, 0.35] but eta > 2.2 everywhere. The Bogoliubov spectrum doesn't need slow-roll — it's set by the quench rate, not the potential shape.
- **Input**: `s38_cc_instanton.npz`, `s42_hauser_feshbach.npz`, `s44_dos_tau.npz`, `s44_vanhove_track.npz`
- **Output**: `s45_kz_ns.{py,npz,png}`

---

### TIER 2: HIGH PRIORITY (CC + DM/DE)

#### ANALYTIC-TORSION-45: Geometric CC from Analytic Torsion
- **Agent**: spectral-geometer (primary), nazarewicz (Strutinsky cross-check)
- **Convergence**: 5/7 proposed q-theory or trace-log route; Nazarewicz top priority
- **Gate**: PASS if analytic torsion of SU(3) at fold is < 10^{-50} (in units where geometric CC ~ 10^{114.8}). FAIL if O(1). INFO if computed but interpretation unclear.
- **Method**: The post-transit CC is purely geometric: Tr ln(D_K^2) on SU(3) at the fold (W1-4 result). This is related to the Ray-Singer analytic torsion. Compute T(SU(3), g_tau) = exp(-(1/2) zeta'_{D_K^2}(0)) at tau = 0.19. If Volovik's Gibbs-Duhem identity forces T = 1 (equilibrium), the geometric CC vanishes.
- **Input**: `s42_hauser_feshbach.npz`, `s41_spectral_refinement.npz`
- **Output**: `s45_analytic_torsion.{py,npz,png}`

#### ALPHA-EFF-45: Non-Equilibrium Specific Heat for DM/DE
- **Agent**: volovik (primary), landau (cross-check)
- **Convergence**: 5/7 proposed (Volovik, Einstein, Landau, QA, Tesla variants)
- **Gate**: PASS if alpha_eff in [0.3, 0.5] (matching observed DM/DE = 0.387). FAIL if alpha_eff > 2.0. INFO if computed but model-dependent.
- **Method**: The DM/DE ratio = specific heat exponent alpha (Landau S44 collab). Equilibrium alpha = 1.06 (W6-4, 2.7× observed). The GGE has 8 temperatures — compute the non-equilibrium specific heat C_V^{GGE} = sum_k (dE_k/dT_k) and extract alpha_eff from the generalized Gibbs-Duhem relation. The 3 negative heat capacity eigenvalues (W6-5) create a sublinear effective alpha.
- **Input**: `s43_gge_temperatures.npz`, `s42_gge_energy.npz`, `s44_multi_t_jacobson.npz`
- **Output**: `s45_alpha_eff.{py,npz,png}`

#### Q-THEORY-KK-45: Volovik q-Theory on Discrete KK Tower
- **Agent**: volovik (primary), hawking (Gibbs-Duhem cross-check)
- **Convergence**: 5/7 proposed q-theory as CC path
- **Gate**: PASS if q-theory self-tuning zero-crossing occurs at tau in [0.10, 0.25]. FAIL if no crossing in physical domain (repeats S43 QFIELD-43 failure). INFO if crossing exists but at different tau.
- **Method**: S43 QFIELD-43 found zero-crossing at tau ~ 1.23 (outside physical domain). Redo with: (1) corrected trace-log functional (not polynomial), (2) EIH singlet projection (only (0,0) gravitates), (3) discrete KK tower (not continuum). These three corrections change the integrand by ~10 orders. Does the crossing move into [0.10, 0.25]?
- **Input**: `s43_qtheory_selftune.npz`, `s44_tracelog_cc.npz`, `s44_eih_grav.npz`, `s42_hauser_feshbach.npz`
- **Output**: `s45_qtheory_kk.{py,npz,png}`

---

### TIER 3: MEDIUM PRIORITY (Diagnostics + Infrastructure)

#### MKK-TENSION-45: Resolve the 0.83-Decade M_KK Tension
- **Agent**: baptista (primary), connes (NCG cross-check)
- **Gate**: PASS if tension narrows to < 0.2 decades. FAIL if structural and irreducible. INFO if partially resolved.
- **Method**: S44 W7-1 confirmed tension is real and Vol-independent. The Kerner formula (gauge route) and spectral zeta (gravity route) compute M_KK with different spectral weightings (Nazarewicz: "Strutinsky shell correction" between global and local). Compute: (1) KK threshold corrections to alpha_EM at M_KK, (2) 2-loop RGE shift, (3) Baptista hypercharge normalization variants (factor 3 from Paper 14 vs SU(5) 5/3), (4) whether f_2 = 0.75 (W4-2 bosonic) reconciles. S43 MKK-BAYES-43 had 0.70-decade tension; S44 found 0.83.
- **Input**: `s44_mkk_reconcile.npz`, `s44_constants_corrected.npz`, `s42_constants_snapshot.npz`

#### SIGMA-SELECT-45: Scale Selection for Spectral Dimension n_s
- **Agent**: connes (primary), hawking (backreaction)
- **Gate**: PASS if self-consistent sigma found. FAIL if no fixed point. INFO if multiple.
- **Method**: S44 W2-2 found n_s = 0.961 at sigma = 1.10 but no principle selects this scale. Test: (1) backreaction self-consistency Lambda = Lambda(tau, d_s), (2) matching 4D Hubble scale to internal diffusion time sigma = 1/H^2, (3) Connes' suggestion of an occupied-state sigma. If any produces sigma ~ 1.10 self-consistently, DIMFLOW is rescued.
- **Input**: `s44_dimflow.npz`, `s42_constants_snapshot.npz`

#### ECOND-RECONCILE-45: Resolve E_cond 0.115 vs 0.137 Discrepancy
- **Agent**: nazarewicz
- **Gate**: INFO (determine authoritative value, rerun 6 affected scripts)
- **Method**: S44 data provenance found E_cond = 0.115 (s42_hauser_feshbach hardcoded) vs 0.137 (s37 ED, 256-state Fock, machine epsilon). The s37 value is more authoritative (full ED vs approximate). Rerun the 6 downstream scripts with corrected E_cond and report which results change by > 5%.
- **Input**: `s37_pair_susceptibility.npz`, `s42_hauser_feshbach.npz`

#### DATA-PROVENANCE-45: Complete Upstream Audit
- **Agent**: gen-physicist
- **Gate**: INFO (audit all tier0 .npz files for consistency)
- **Method**: The S44 parallel audit found 3 issues (Vol(SU(3)) 3 values, E_cond 2 values, stale M_KK). Complete the audit of S7-S24 foundational scripts (the early-sessions audit agent was still running). Produce a canonical constants file imported by all future scripts.

#### DEBYE-WALLER-45: Spectral Action Thermal Correction
- **Agent**: quantum-acoustics
- **Source**: QA S44 collab suggestion
- **Gate**: INFO (diagnostic — does the DW factor modify the spectral action at the few-percent level?)
- **Method**: The Debye-Waller factor exp(-2W) suppresses coherent scattering in crystals. On SU(3), the phonon spectrum (W5-3) gives a DW factor for the spectral action. If 2W ~ O(1), the spectral action is significantly modified by thermal fluctuations.

---

### TIER 4: SPECIALIST (from collab reviews)

#### LK-RELAX-45: Landau-Khalatnikov Relaxation Dynamics for n_s
- **Agent**: landau
- **Source**: Landau S44 collab, Section 3.1
- **Method**: Solve the LK equation d(phi)/dt = -(1/tau_0) dF/dphi with F = S_occ (occupied-state spectral action). If OCC-SPEC-45 finds a minimum, compute the relaxation dynamics near it. Extract the KZ freeze-out spectrum and n_s.

#### SAKHAROV-UV-DISSOLUTION-45: Link Sakharov UV Cutoff to Dissolution Scale
- **Agent**: quantum-foam
- **Source**: QF S44 collab suggestion
- **Method**: W1-1 audit found Lambda_eff ~ 10×M_KK. W6-7 found epsilon_c ~ 1/sqrt(N). Is there a relationship? At N ~ (Lambda_eff/M_KK)^8, does epsilon_c match the foam strength?

#### EXTREMAL-RN-45: Penrose Diagram of the Cutoff Fine-Tuning
- **Agent**: schwarzschild-penrose
- **Source**: SP S44 collab addendum
- **Method**: SP mapped the spike function (width 10^{-121}) to extremal Reissner-Nordstrom in functional space. Construct the full Penrose diagram for the modulus space, with the fine-tuned cutoff as an extremal horizon.

#### OCCUPIED-CYCLIC-45: Cyclic Cohomology Pairing for Occupied-State Triple
- **Agent**: connes
- **Source**: Connes S44 collab, Section 3.4
- **Method**: The occupied-state spectral action defines a modified spectral triple. Compute the Connes-Chern character and verify the cyclic cohomology pairing is nondegenerate.

---

## S22 ↔ S44 ↔ S45 Transit Constraint Thread

| Session | Finding | Implication for S45 |
|:--------|:--------|:-------------------|
| S22a | epsilon < 1 in [0.11, 0.35], eta > 2.2 everywhere | Potential has a slow region at tau~0.3, NOT the fold |
| S22d | ~1 e-fold at tau=0.3, settling time 232 Gyr | Transit stalls briefly near tau=0.3 in vacuum potential |
| S22d | Clock constraint: 15,000× violation if rolling today | Transit must be FROZEN now (tau_dot < 25 ppm) |
| S36 | TAU-DYN FAIL: 38,600× too fast | BCS dynamics blow through the potential feature |
| S43 | FRIEDMANN-BCS: 60,861× shortfall, surface empty | Confirmed S36 |
| S44 W4-3 | epsilon_H = 2.999, ratio-invariant (THEOREM) | No amplitude projection can fix n_s |
| S44 W2-2 | n_s = 0.961 at sigma=1.10 (unfixed) | Spectral dimension CONTAINS the answer |
| S44 W1-3 | Lifshitz eta = 3.77 (CLOSED) | Static geometry cannot give n_s |
| **S45** | **OCC-SPEC-45**: Does S_occ have minimum at tau=0.3? | **Many-body state may create the slow region vacuum SA couldn't** |
| **S45** | **KZ-NS-45**: n_s from Bogoliubov quench | **Dynamical route, independent of potential shape** |

---

## Decision Tree

```
S45 starts
  │
  ├─ OCC-SPEC-45: minimum found?
  │   ├─ YES at tau ~ 0.3 → tau-stabilization SOLVED
  │   │   └─ Compute n_s from relaxation near minimum (LK-RELAX-45)
  │   │       ├─ n_s in [0.955, 0.975] → FRAMEWORK VIABLE (P > 50%)
  │   │       └─ n_s outside → stabilization works but tilt wrong
  │   ├─ YES at tau ~ 0.19 (fold) → self-consistent fold selection
  │   │   └─ Same n_s branch as above
  │   └─ NO (monotone) → occupied-state route CLOSED
  │       └─ 6th monotonicity confirmation. Spectral action framework exhausted for tau-stabilization.
  │
  ├─ KZ-NS-45: n_s from Bogoliubov?
  │   ├─ PASS → n_s EXPLAINED (dynamical, not geometric)
  │   │   └─ If OCC-SPEC also PASS → complete picture
  │   │   └─ If OCC-SPEC FAIL → n_s works but no stabilization (transit is right, stalling is wrong)
  │   └─ FAIL → n_s UNEXPLAINED after 45 sessions
  │       └─ Framework probability drops to ~8%
  │
  ├─ ANALYTIC-TORSION-45: geometric CC = 0?
  │   ├─ T(SU(3)) ~ 1 (trivial) → Gibbs-Duhem kills geometric CC
  │   └─ T(SU(3)) >> 1 → geometric CC persists, q-theory needed for dynamics
  │
  └─ ALPHA-EFF-45: DM/DE ratio nailed?
      ├─ alpha_eff ~ 0.39 → DM/DE EXPLAINED from universality
      └─ alpha_eff >> 1 → thermodynamic argument fails
```

---

## Master Gate: What Would Change the Probability?

| Outcome | BF | New P (from 23%) |
|:--------|:---|:-----------------|
| OCC-SPEC PASS + KZ-NS PASS | 50-100 | **60-75%** |
| KZ-NS PASS alone | 10-20 | **50-65%** |
| OCC-SPEC PASS alone | 3-5 | **35-45%** |
| Both FAIL | 0.1-0.3 | **3-8%** |
| ANALYTIC-TORSION = trivial | 2-3 | +5-10 pp |
| ALPHA-EFF = 0.39 | 2-3 | +5-10 pp |
| MKK tension resolved | 1.5 | +3-5 pp |
