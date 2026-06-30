# S64 Synthesis + Working Paper Extraction for S65 Planning

**Date**: 2026-04-02
**Source files**: session-64-results-workingpaper.md, 7 synthesis documents, gge-kms-64-content.md, session-64-plan.md, evoi-framework.md

---

## I. Working Paper Forward Projection (Levels 1-3)

### Level 1 -- Structural Necessities (S65 Core)

| # | Computation | Description | Pre-Registered Gate | Priority |
|:--|:-----------|:-----------|:-------------------|:---------|
| T1-1 | **BCS-DRESSED-SA** | Compute S^{BCS}(tau) from BdG Dirac operator at 5-7 tau values. Extract eps_H^{BCS} and one-loop Hessian. Affects n_s (est. +0.0014 toward Planck, 2.2->1.5 sigma), fold Hessian structure, Sakharov coupling. Uses BdG heat kernel factorization (W3-B permanent). | \|delta(eps_H)/eps_H\| > 0.01 | **HIGHEST** |
| T1-2 | **BARYOGENESIS-SURVEY** | All 5 fiber-level channels closed. Two unexplored: (a) 4D effective Skyrme model from spectral action SU(3) gauge sector (emergent QCD skyrmions at QCD scale), (b) UV-completion via Paasch vacuum decay. | Identify at least one channel with eta_B within 5 OOM of 6.1e-10 | HIGH |
| T1-3 | **OFF-JENSEN-TRANSIT-DYNAMICS** | Transit trajectory in 36D moduli space not determined from dynamics. W2-A proved fold is saddle with 27 descent directions. Compute gradient flow from spectral action Hessian eigenbasis. Controls n_s, CC problem, tensor prediction. | eps_H along dynamical path | HIGH |

### Level 2 -- CC Surviving Paths

| # | Computation | Description | Pre-Registered Gate | Priority |
|:--|:-----------|:-----------|:-------------------|:---------|
| T2-4 | **VOLUME-BREAKING CC** | a_0/a_2 trap holds for volume-preserving only. Relaxing volume preservation changes a_0 (proportional to Vol). If a_0 decreases faster than a_2 in some direction, CC ratio decreases. | Find direction in full 36D space (not vol-preserving) where d(a_0/a_2)/ds < 0 | HIGH |
| T2-5 | **DISTINCT-SPECTRUM CC** | Spectral moment decoupling theorem (W5-B permanent) proves CC monotonicity breaks if B/F sectors see different spectra. In almost-commutative geometry, B/F share D_K but differ in grading (gamma_5 vs J). Does this produce distinct spectra for CC-relevant moments? | Break CC monotonicity while preserving NEC | HIGH |
| T2-6 | **NONLOCAL-SA** | Capozziello-Mazumdar-Meluccio (Paper 09 Mack corpus) propose nonlocal corrections. UNEXPANDED-SA-45 showed SDW exact for finite spectra, but at L_max -> infinity the full Tr f(D^2/Lambda^2) may differ by O(1) at a_0 level. Compute nonlocal correction at L_max=12. | Test convergence of a_0/a_2 beyond SDW | MEDIUM |

### Level 3 -- Observational Chain

| # | Computation | Description | Pre-Registered Gate | Priority |
|:--|:-----------|:-----------|:-------------------|:---------|
| T3-7 | **A_s NORMALIZATION** | 3.16 OOM gap dominated by (0,0) PW selection (3.50 OOM structural). Since M-S inapplicable (permanent), framework needs its own perturbation equation. GGE acoustic perturbation formalism (S63 W6-03, T12) provides structure; normalization constant missing. | Close remaining 3.16 OOM gap | MEDIUM |
| T3-8 | **DESI DR3 PREPARATION** | S64 DESI-DV: framework chi2=14.2 closer than LCDM chi2=21.7. Substrate compaction w_a=-0.645 correlates well (r=0.82). Pre-register predictions for DR3 redshift bins, especially 0.7<z<1.3 divergence range. | DR3 decision rules | MEDIUM |
| T3-9 | **L_MAX CONVERGENCE** | Shell Hessian (W7-A) showed 79.9% of one-loop from L=3. Extend to L_max=4 (8 new irreps). Test Hessian eigenvalue pattern stabilization vs growth. Controls UV-sensitivity of fold stability, n_s, Sakharov coupling. | Hessian convergence at L=4 | MEDIUM |

---

## II. NOT STARTED Carry-Forwards from S64 Plan

| # | Gate ID | Wave | Description | Reason Not Started |
|:--|:--------|:-----|:-----------|:------------------|
| CF-1 | BCS-DRESSED-SA-64 | W2-A (original) | Compute BCS-dressed spectral action at 5 tau values, extract eps_H^{BCS} | **Slot repurposed** to HESSIAN-DESCENT-64 after W1-A FAIL pivoted session strategy. BCS-DRESSED-SA remains the highest-priority uncomputed correction. |
| CF-2 | W8-A Volovik x Landau Workshop | W8-A | Transit-as-relaxation deep dive: asymptotic S(tau), Volovik rho_vac relaxation | **Trigger condition not met**: W1-A returned FAIL (workshop required W1-A PASS or INFO). Path C permanently closed. Workshop topic is now moot. **DO NOT CARRY FORWARD.** |

**Note on W4-B KK-THRESHOLD and W4-D DESI-DV**: Both WERE completed in S64 (KK-THRESHOLD-64 returned INFO with delta=2.35, DESI-DV-64 returned INFO with chi2=14.19). They are NOT carry-forwards. The S64 plan listed them as carry-forwards from S62, and they were executed.

**Note on W5-A POST-TRANSIT-THERMO**: Completed in S64 (PASS, S_gen monotone). Not a carry-forward.

**Actual carry-forward**: Only CF-1 (BCS-DRESSED-SA) is a genuine carry-forward. CF-2's topic is permanently closed.

---

## III. Synthesis Recommendations (by Agent)

### Hawking (session-64-hawking-synthesis.md)

| # | Recommendation | Type | Priority | Details |
|:--|:-------------|:-----|:---------|:--------|
| H-1 | **BCS-DRESSED-EPS (H-65-1)** | Pre-registered gate | HIGHEST | Compute eps_H from BCS-dressed S^{BCS}(tau) at 5 tau values. Gate: \|delta(eps_H)/eps_H\| > 0.01. Estimated +0.0014 toward Planck (2.2->1.5 sigma). |
| H-2 | **DISTINCT-SPECTRUM-CC (H-65-2)** | Pre-registered gate | HIGH | Test whether B (Anderson-Bogoliubov, Leggett) and F (Bogoliubov quasiparticle) sectors have distinct spectral moments for CC-relevant F_{-1}. BCS condensate splits excitation spectrum; question is whether splitting breaks CC monotonicity while preserving NEC. |
| H-3 | **TRANSIT-ENTROPY-RATE (H-65-3)** | Pre-registered gate | MEDIUM | Compute dS/dtau through transit at 10 tau values. Verify entropy production consistent with Parker creation. S64 GSL tested 4 discrete stages; this tests continuous trajectory. |
| H-4 | r=0.033 + blue n_T | Observational prediction | -- | Testable by CMB-S4 and LiteBIRD (sigma(r)~0.001). First detection of blue tensor tilt would rule out all single-field slow-roll models. |
| H-5 | 36D moduli saddle landscape | Open direction | MEDIUM | 27 descent directions for R open vast unexplored landscape for post-Jensen dynamics. Physical transit path need not follow Jensen; off-Jensen trajectories may escape a_0/a_2 trap if volume changes. |

### Einstein (session-64-einstein-synthesis.md)

| # | Recommendation | Type | Priority | Details |
|:--|:-------------|:-----|:---------|:--------|
| E-1 | **BCS-DRESSED-SA** | Computation | HIGHEST | Compute S^{BCS}(tau) at 5 tau values. n_s decisive. |
| E-2 | **Nonlocal spectral action a_0/a_2** | Computation (CC) | HIGH | Sole structurally open CC route. Test whether full Tr f(D^2/Lambda^2) differs from SDW at O(1) for physical Lambda_sp = M_KK. |
| E-3 | **Off-Jensen transit trajectory** | Computation | HIGH | Physical trajectory in 36D from spectral action gradient flow. Determines both eps_H (n_s) and relevant a_0/a_2 along actual path. |
| E-4 | **L_MAX-CONVERGENCE** | Gate | MEDIUM | Spectral action at L_max=12. UV stability of all L_max=10 results. |
| E-5 | Jacobson route as reformulation | Structural insight | -- | Jacobson route survives as reformulation (correctly identifies integration constant), not as resolution. Principle 3 (nonlocal SA) is strongest surviving CC route. |

### Volovik (session-64-volovik-synthesis.md)

| # | Recommendation | Type | Priority | Details |
|:--|:-------------|:-----|:---------|:--------|
| V-1 | **BCS-DRESSED SPECTRAL ACTION** | Computation | HIGHEST | BdG heat kernel factorization K_BdG = exp(-Delta^2 t) K_bare is exact (W3-B). Compute a_2^{BCS}(tau) at 5 tau values. Tests whether BCS condensate modifies n_s toward/away from Planck. Also: if a_2^{BCS} differs from a_2^{bare} by >36% (Sakharov), effective a_0/a_2 changes and CC arithmetic changes. |
| V-2 | **VOLUME-BREAKING CC** | Computation | HIGH | Test Sector A: compute a_0(g) and a_2(g) for non-volume-preserving deformation. If d(a_0/a_2)/ds < 0 exists, trap is evaded. Most direct analog of Volovik equilibrium theorem: allowing mode count to adjust. |
| V-3 | **DISTINCT-SPECTRUM CC** | Computation | HIGH | Test Sector B: BdG heat kernel factorization creates different effective spectra for different channels. Compute effective B and F spectral moments for CC-relevant (a_0) and gravity-relevant (a_2) channels. If they differ at a_0 level, shared-spectrum maximum theorem evaded. |
| V-4 | **OFF-JENSEN TRANSIT DYNAMICS** | Computation | HIGH | Physical transit trajectory in 36D not determined from dynamics. If trajectory curves into 27 descent directions, S(tau) profile changes, affecting n_s, r, CC arithmetic. |
| V-5 | **BARYOGENESIS SURVEY** | Computation | HIGH | All 5 fiber channels closed. Framework's deepest open wound. From superfluid perspective, needs CP-breaking mechanism for BCS condensate. Framework is B-class (N_3=0), so 3He-A baryogenesis inapplicable. UV completion or emergent 4D mechanism needed. |
| V-6 | Seven broken superfluid rules | Structural | -- | S64 adds 3 more: a_0/a_2 trap (no 3He analog), Q<1 quasiparticles (3He-B has Q>>1), Fermi-surface lock is absolute. Framework diverges from 3He-B in thermodynamic behavior. |

### Quantum Acoustics (session-64-quantum-acoustics-synthesis.md)

| # | Recommendation | Type | Priority | Details |
|:--|:-------------|:-----|:---------|:--------|
| QA-1 | **BCS-DRESSED-SA profile** | Computation | HIGHEST | Same as others: n_s correction, Planck tension reduction. |
| QA-2 | **COLLECTIVE-MODE-LINEWIDTH** | Computation | HIGH | LINEWIDTH FAIL established Q<1 for individual quasiparticles. DM candidate is collective Leggett mode, not individual quasiparticle. Compute Leggett linewidth from RPA response function. In nuclear structure, giant dipole resonance has Q~3-5 even when single-particle Q<1. Gate: Gamma_Leggett < omega_L (Q>1 for collective mode). |
| QA-3 | **BISPECTRUM-PHASE** | Computation | HIGH | Phase coherence R=1.0000 invisible in C_l but should produce specific f_NL signature. Compute bispectrum from sudden-quench Bogoliubov modes with uniform \|beta\|^2 and phase pi. Gate: f_NL distinguishable from slow-roll at 3-sigma for Planck data. |
| QA-4 | **A_s NORMALIZATION** | Computation | MEDIUM | 3.16 OOM residual gap requires understanding mode-counting normalization in substrate perturbation theory. M-S inapplicable; scalar power spectrum must derive from GGE acoustic excitation spectrum. Framework's native acoustic calculation. |
| QA-5 | **CC COLLECTIVE-THERMALIZATION** | Computation | MEDIUM | 14 CC closures block single-mode channels. Substrate has 256 degrees of freedom. Compute <r> at N_pair=4,5,6 in pairing-only sector. If <r>->0.53 (GOE) with increasing N, collective thermalization reopens. |
| QA-6 | Transport vs scattering correction | Methodological | -- | LINEWIDTH FAIL reveals systematic bias: acoustic perspective defaults to transport intuition on discrete spectra. Correction: start from matrix element + density of final states, never from group velocity. |

### Landau (session-64-landau-synthesis.md)

| # | Recommendation | Type | Priority | Details |
|:--|:-------------|:-----|:---------|:--------|
| L-1 | **BCS-Dressed Spectral Action** | Computation | HIGHEST | Same as all others. K_BdG = exp(-Delta^2 t) K_bare provides backbone. |
| L-2 | **Volume-Breaking CC Direction** | Computation | HIGH | a_0/a_2 trap holds only vol-preserving. Relaxing volume changes a_0 (proportional to Vol). Find direction where d(a_0/a_2)/ds < 0. In Landau terms: allow extensive variable to vary, look for first-order transition where volume jumps. |
| L-3 | **Collective Mode DM Reformulation** | Computation | HIGH | Linewidth FAIL (Q<1) + quantum metric FAIL (D_s(PT)=0) demand DM stability analysis in collective-mode basis. Pomeranchuk stability (PASS S61) guarantees collective modes well-defined. Compute RPA response for Leggett mode at finite frequency. |
| L-4 | **Distinct-Spectrum CC Path** | Computation | HIGH | Spectral moment decoupling opens CC path through distinct B/F spectra. Determine whether grading structure produces distinct spectra for inverse moment F_{-1}. Sole surviving theoretical path. |
| L-5 | **L_max=4 Convergence** | Computation | MEDIUM | Shell Hessian UV-dependence demands testing. Extend from L_max=3 to L_max=4 (8 new irreps). Controls UV-sensitivity of fold stability, n_s, Sakharov coupling. |
| L-6 | CC is vacuum subtraction, not pairing | Structural insight | -- | R-G charge decomposition definitively establishes 94.6% of rho_ZP outside Gaudin. CC problem is in the background condensate, not quasiparticles. Surviving paths require changing the Hamiltonian, not the order parameter. |

### Connes (session-64-connes-synthesis.md)

| # | Recommendation | Type | Priority | Details |
|:--|:-------------|:-----|:---------|:--------|
| C-1 | **BCS-DRESSED-SA (S65 Core)** | Computation | HIGHEST | Single most consequential uncomputed quantity. BDG-KASPAROV-64 factorization provides framework. Compute eps_H^{BCS} at 5-7 tau values. Controls n_s, fold Hessian, Sakharov 31%->100% chain. Gate: \|delta(eps_H)/eps_H\| > 0.01. |
| C-2 | **Distinct B/F spectra (NCG-native CC path)** | Computation | HIGH | Can almost-commutative geometry's grading structure produce distinct B/F spectra for CC-relevant F_{-1}? B/F share D_K but differ in gamma_5 and J gradings. Most NCG-native surviving path. |
| C-3 | **Volume-breaking deformations** | Computation | HIGH | Relaxing det(g_K)=const allows a_0 to change. Whether dynamical mechanism exists to simultaneously decrease a_0 and increase a_2 in full 36D is untested. |
| C-4 | **Modular flow CC connection** | Computation | MEDIUM | Does sigma_t^{GGE}(Tr f(D^2/Lambda^2)) produce dynamical CC relaxation? Modular flow acts on algebra; spectral action is trace on algebra hence modular invariant. Whether modular dynamics produces non-trivial CC evolution is open. |
| C-5 | **L_max convergence** | Computation | MEDIUM | Per-shell Frobenius norm scales as L^{2.5}. L=4 verification needed: 8 new irreps would add ~2.6x L=3 contribution if scaling continues. |
| C-6 | **Chiral asymmetry matrix C_{alpha,beta}** | Computation | LOW | VAB rank=5 establishes 5 independent Yukawa texture directions. Whether SU(3) fiber SELECTS 3 generations from these 5 requires computing C_{alpha,beta} (Baptista Paper 17, Prop 5.1). |
| C-7 | GGE modular structure as mathematical home | Structural insight | -- | GGE-KMS provides natural home within NCG: 8-fold modular flow, Tomita-Takesaki compatible, type III_1 limit. Three coexisting times (modular, cosmological, Unruh) related by Connes cocycle. |

### Van den Dungen (session-64-van-den-dungen-synthesis.md)

| # | Recommendation | Type | Priority | Details |
|:--|:-------------|:-----|:---------|:--------|
| VdD-1 | **BCS-DRESSED-SA** | Computation | HIGHEST | Leading correction to n_s. BdG factorization provides backbone: S^{BCS} = exp(-Delta^2/Lambda^2) * S^{bare} + occupation-weighted corrections. 69% missing Sakharov component must be computed explicitly. |
| VdD-2 | **Off-Jensen transit path** | Computation | HIGH | Dynamical trajectory in 36D from spectral action gradient flow. W2-A shows fold is saddle with 27 descent directions. Physical transit may not follow 1D Jensen. |
| VdD-3 | **Volume-breaking mechanism** | Computation | HIGH | a_0/a_2 trap closes all vol-preserving directions. What physical mechanism breaks volume preservation? Self-consistent back-reaction loop (Volovik V2) could break this. |
| VdD-4 | **Nonlocal spectral action (Paper 09)** | Computation | MEDIUM | If full Tr f(D^2/Lambda^2) differs from SDW polynomial in way that makes a_0 effectively tau-dependent, trap is evaded. UNEXPANDED-SA-45 exact for finite spectra, so requires infinite-volume effects or different f. |
| VdD-5 | **Connes cocycle computation** | Structural | MEDIUM | Does GGE modular flow connect to cosmological time through Connes cocycle? Would formalize "three times" picture within NCG. |
| VdD-6 | **Shell Hessian convergence (L_max=4,5)** | Computation | MEDIUM | Per-shell Frobenius ~L^{2.5} suggests convergence. Verification at L=4,5 needed. |
| VdD-7 | **Mode-changing virtual hopping for quantum metric** | Computation | LOW | D_s(PT)=0 because T = E_J * I_8 (mode-preserving). Does mode-changing second-order virtual hopping break this proportionality and give nonzero quantum geometric tensor? |
| VdD-8 | Kasparov = topology, CC = analysis | Structural insight | -- | Kasparov product gives exact K-theory, exact factorizations, exact indices. But CC depends on spectral moments (analytical, not topological). Two operators in same K-class can have spectral actions differing by arbitrary amounts. |

### GGE-KMS Content (gge-kms-64-content.md)

| # | Open Question | Type | Details |
|:--|:-------------|:-----|:--------|
| GK-1 | Approximate KMS under gravitational breaking | Theory | Gravity breaks R-G charges at O(alpha_G). Modular decomposition holds only to O(alpha_G). Rigorous treatment of approximate KMS for perturbed integrable systems beyond scope of S64. |
| GK-2 | Total GGE entropy as single spectral action | Theory | Each sector entropy is spectral-action-type, but total S_GGE as single Tr(f(D_BdG^2/Lambda^2)) is unresolved. Obstruction: R_k are many-body operators, not single-particle functions of D_K. |
| GK-3 | Type III_1 limit physical relevance | Theory | Dense Connes spectrum and type III_1 implications are formal for truncated system. Physically relevant only if KK tower extended beyond L_max=10. |

---

## IV. EVOI Framework Current State

**Source**: sessions/evoi-framework.md (dated S61, pre-S64)

The EVOI table was last updated after S61 and needs significant revision post-S64. Key changes:

### Items Requiring Update

| EVOI ID | Pre-S64 State | Post-S64 State |
|:--------|:-------------|:---------------|
| P1 (n_s from transit Bogoliubov) | 0.7 prereqs, EVOI 13.8% | **Partially resolved**: n_s = 0.9557 +/- 0.0036 computed (zero free parameters, one-loop). BCS dressing is sole remaining correction. EVOI should INCREASE (single highest-impact correction). |
| P2 (Phase-basis CC) | 0.5 prereqs, EVOI 8.5% | **Partially superseded**: CC paths C, A closed. a_0/a_2 trap established. Surviving paths are volume-breaking, distinct spectra, nonlocal SA. Needs complete reformulation. |
| P3 (Higgs mass 2-loop) | 0.8 prereqs, EVOI 6.5% | **KK-THRESHOLD-64 INFO**: delta=2.35 (outside [0.73,1.48] pass band). tree-level m_H=131.8 GeV stable. 2-loop still needed. |
| P4 (f_0 from gauge unification) | 0.6 prereqs, EVOI 9.0% | **Unchanged** |
| P5 (DM abundance f_DM) | 0.4 prereqs, EVOI 6.8% | **Needs reformulation**: Q<1 linewidths + D_s(PT)=0 demand collective-mode DM analysis, not quasiparticle. |
| P6 (w(z) substrate compaction) | 0.3 prereqs, EVOI 6.0% | **Advanced**: DESI-DV-64 computed (chi2=14.2 vs LCDM 21.7). DR3 preparation is next step. |
| P7 (Baryogenesis washout) | 0.6 prereqs, EVOI 3.5% | **CLOSED**: All 5 channels now closed. Must be replaced with BARYOGENESIS-SURVEY (4D effective skyrmions + UV completion). |
| P8 (Filter moment f_4) | 0.9 prereqs, EVOI 2.6% | **Unchanged** |
| P9 (Yukawa from KK + BCS NJL) | 0.2 prereqs, EVOI 3.0% | **Unchanged** (VAB rank=5 provides structural room) |

### New EVOI Entries Needed

| ID | Computation | Est. Prereqs | Est. P(pass) | Notes |
|:---|:-----------|:-------------|:-------------|:------|
| P10 | BCS-DRESSED-SA | 0.9 (BdG factorization done) | 0.7 | HIGHEST EVOI: affects n_s, CC, fold Hessian |
| P11 | VOLUME-BREAKING CC | 0.3 | 0.3 | New CC path: relax volume preservation |
| P12 | DISTINCT-SPECTRUM CC | 0.2 | 0.3 | New CC path: B/F grading split |
| P13 | BARYOGENESIS-SURVEY (4D) | 0.1 | 0.3 | Replace P7 |
| P14 | COLLECTIVE-MODE-DM | 0.5 | 0.5 | RPA Leggett linewidth |
| P15 | BISPECTRUM-PHASE | 0.7 | 0.4 | f_NL from sudden-quench coherence |

### Milestone Completion Update

```
Mechanism chain links:  7/9 complete at 7/7 PASS  (unchanged from S61)
  [x] Geometric a_k (a_0, a_2, a_4) -- PROVEN
  [x] Product decomposition (A-tensor, Kasparov) -- PROVEN
  [x] GGE permanence (9/9 + structural theorem) -- PROVEN
  [x] Fold stability (36D Hessian) -- PROVEN (but UV-dependent, L=3 critical)
  [x] SM gauge group (extended gauge module) -- PROVEN
  [x] Higgs mass (tree-level, 131.8 GeV, 5.4%) -- PASS (stable under KK threshold)
  [x] Baryogenesis -- ALL 5 CHANNELS CLOSED (was PASS at 3x, now FAIL)
  [ ] CC mechanism -- 114 OOM gap confirmed, 14 closures, 3 surviving paths
  [ ] n_s / observational spectrum -- 0.9557, 2.2 sigma, BCS dressing uncomputed

New observational results (S64):
  r:      0.033 (PASSES BICEP/Keck, 2 independent computations)
  n_T:    > 0 (blue tilt, discriminant vs inflation)
  n_s:    0.9557 +/- 0.0036 (one-loop, zero free parameters)
  A_s:    3.16 OOM gap (reduced from 8.01)
  DESI:   chi2 = 14.2 vs LCDM 21.7
```

---

## V. Convergent Recommendations (2+ Syntheses Agree)

| # | Recommendation | Sources | Priority | Notes |
|:--|:-------------|:--------|:---------|:------|
| 1 | **BCS-DRESSED-SA** | ALL 7 syntheses + working paper | **HIGHEST** | Unanimous #1 priority. Single most consequential uncomputed correction. Affects n_s (2.2->1.5 sigma), fold Hessian, Sakharov coupling, potentially CC arithmetic. BdG factorization (W3-B permanent) provides backbone. |
| 2 | **OFF-JENSEN TRANSIT DYNAMICS** | Hawking, Einstein, Volovik, VdD, Working Paper | HIGH | Transit trajectory in 36D not determined from dynamics. Fold = saddle with 27 descent directions. Controls n_s, r, CC via actual a_0/a_2 along physical path. |
| 3 | **VOLUME-BREAKING CC** | Volovik, Landau, Connes, VdD, Working Paper | HIGH | Sole moduli-space CC path after a_0/a_2 trap. Relax det(g_K)=const constraint. If a_0 decreases faster than a_2 in some direction, CC ratio decreases. |
| 4 | **DISTINCT-SPECTRUM CC** | Hawking, Volovik, Landau, Connes, Working Paper | HIGH | Spectral moment decoupling (permanent theorem) opens this path. Test whether B/F grading difference produces distinct spectra for CC-relevant F_{-1}. |
| 5 | **BARYOGENESIS-SURVEY (4D effective)** | Volovik, Working Paper | HIGH | All 5 fiber channels closed. Framework's deepest open wound. Two directions: emergent QCD Skyrme model, UV completion via Paasch decay. |
| 6 | **COLLECTIVE-MODE-DM / LEGGETT LINEWIDTH** | QA, Landau | HIGH | Q<1 for all quasiparticles demands DM stability reformulation in collective-mode basis. RPA Leggett linewidth computation needed. Pomeranchuk stability guarantees collective modes well-defined. |
| 7 | **L_MAX CONVERGENCE (L=4)** | Einstein, Landau, Connes, VdD, Working Paper | MEDIUM | Shell Hessian UV-dependence (79.9% from L=3) demands verification. Extend to L_max=4. Controls fold stability, n_s, Sakharov coupling UV-sensitivity. |
| 8 | **NONLOCAL SPECTRAL ACTION** | Einstein, VdD, Working Paper | MEDIUM | Sole CC path that modifies a_0/a_2 beyond SDW expansion. Compute at L_max=12. UNEXPANDED-SA-45 exact for finite spectra; question is what happens at physical cutoff. |
| 9 | **BISPECTRUM-PHASE (f_NL from coherence)** | QA (sole source) | MEDIUM | Phase coherence R=1.0000 invisible in C_l. Bispectrum signature is most promising discriminant: sudden-quench f_NL with specific scale dependence. |
| 10 | **A_s NORMALIZATION** | QA, Working Paper | MEDIUM | 3.16 OOM residual gap. M-S inapplicable. Framework needs its own perturbation equation. GGE acoustic formalism provides structure; normalization constant missing. |
| 11 | **TRANSIT-ENTROPY-RATE** | Hawking | MEDIUM | Continuous dS/dtau verification (S64 tested 4 discrete stages). Consistency with Parker creation. |
| 12 | **CC COLLECTIVE-THERMALIZATION (N_pair scaling)** | QA | MEDIUM | Compute <r> at N_pair=4,5,6. If <r>->0.53 (GOE), collective thermalization reopens. |
| 13 | **DESI DR3 PREPARATION** | Working Paper | MEDIUM | Pre-register predictions for DR3 bins. Framework already closer to DESI than LCDM. |
| 14 | **MODULAR FLOW CC CONNECTION** | Connes | LOW | Does GGE modular flow produce CC relaxation? Connects GGE-KMS to CC problem. |
| 15 | **CONNES COCYCLE (three times)** | VdD | LOW | Formalize modular/cosmological/Unruh time relationship within NCG. |
| 16 | **CHIRAL ASYMMETRY MATRIX C_{alpha,beta}** | Connes | LOW | VAB rank=5 gives room for 3 generations. Does SU(3) SELECT 3 from 5? |
| 17 | **MODE-CHANGING VIRTUAL HOPPING** | VdD | LOW | D_s(PT)=0 because T proportional to identity. Does second-order virtual hopping break proportionality? |

---

## VI. Permanent Theorems Established in S64 (for reference)

These constrain all future computations:

1. **R-monotonicity on Jensen** (AM-GM proof): dR/dtau >= 0 for all tau > 0. Path C permanently closed.
2. **Lambda_SA = Lambda_J** (structural): 114-OOM gap is real. Category-error escape permanently closed.
3. **a_0/a_2 trap**: Off-Jensen volume-preserving a_2 descent WORSENS CC (a_0 constant, a_0/a_2 increases).
4. **Spectral moment decoupling** (F_{-1} vs F_{+1}): CC and NEC operate through independent spectral channels. CC resolution need not violate area theorem.
5. **BdG heat kernel factorization**: K_BdG(t) = exp(-Delta^2 t) K_bare(t), exact to machine epsilon.
6. **Fermi-surface lock**: v^2(B2[0]) = 1/2 identically for any Delta when eps = 0. Immune to energy-shift perturbations.
7. **H2 theorem**: Volume-preserving Jensen = traceless in DeWitt superspace. pi_{ij} = 0, first-order tensors killed structurally.
8. **Chirality antisymmetry**: {gamma_9, dD_K/dtau} = 0. Chiral pairs ADD in scalar source (no cancellation).
9. **Mukhanov-Sasaki inapplicability**: N_e = 7.75, eta_H = 0.96. Three independent obstructions. Permanent.
10. **GGE-KMS compatibility**: 4 theorems proven. 8-fold modular flow, Tomita-Takesaki compatible.

---

## VII. Closures Established in S64 (mechanisms that can never be re-opened)

1. CC Path C (transit relaxation along Jensen) -- R-monotonicity
2. CC category-error escape (Lambda_SA != Lambda_J) -- structural proof
3. CC Jacobson multi-T (S43 E3) -- T_Unruh is kinematic, 3 arguments
4. CC Jacobson-Kasparov (12D fiber) -- Lambda_eff wrong sign
5. CC Spectral monotonicity rigid coupling (Level 2->3 flexible, not rigid)
6. Baryogenesis via fiber skyrmions -- M = 10^22 GeV, 22 OOM above proton
7. Mukhanov-Sasaki perturbation theory for this framework -- permanent
8. Peotta-Torma superfluid weight on CG(24) -- three structural zeros
9. First-order tensor production -- H2 theorem, pi_{ij} = 0

---

## VIII. S65 Planning Priority Queue (merged from all sources)

### Wave 1 candidates (core, no dependencies)

1. **BCS-DRESSED-SA** -- HIGHEST priority, unanimously. 5 tau values, BdG factorization backbone.
2. **OFF-JENSEN-TRANSIT-DYNAMICS** -- Gradient flow in 36D from Hessian eigenbasis.
3. **VOLUME-BREAKING CC** -- Non-volume-preserving deformations, test d(a_0/a_2)/ds < 0.
4. **BARYOGENESIS-SURVEY** -- 4D effective Skyrme model + UV completion channel.

### Wave 2 candidates (depend on W1 or independent)

5. **DISTINCT-SPECTRUM CC** -- B/F grading split for F_{-1}.
6. **COLLECTIVE-MODE-DM (Leggett RPA)** -- DM stability in collective basis.
7. **L_MAX CONVERGENCE (L=4)** -- Extend shell Hessian, test stabilization.
8. **NONLOCAL-SA** -- a_0/a_2 beyond SDW at L_max=12.

### Wave 3 candidates (observational chain)

9. **BISPECTRUM-PHASE** -- f_NL from sudden-quench coherence.
10. **A_s NORMALIZATION** -- Mode-counting in substrate perturbation theory.
11. **DESI DR3 PREPARATION** -- Pre-register predictions for DR3 bins.
12. **TRANSIT-ENTROPY-RATE** -- Continuous dS/dtau at 10 tau values.

### Later waves

13. CC COLLECTIVE-THERMALIZATION (N_pair=4,5,6 level statistics)
14. Modular flow CC connection
15. Connes cocycle three-times formalization
16. Chiral asymmetry matrix C_{alpha,beta}
17. Mode-changing virtual hopping for quantum metric
