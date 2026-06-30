# NOISE Spot Check — 5% random sample per table

Random seed: 42 (deterministic; rerun produces identical sample).
Sample rule: max(ceil(5% * |NOISE|), 2) per table; tables with <= 20 NOISE include ALL entries.

## Summary

| Table | NOISE total | Sampled | AGREE | DISAGREE | BORDERLINE |
|:------|----:|----:|----:|----:|----:|
| closed_mechanisms | 26 | 2 | 1 | 0 | 1 |
| open_channels | 481 | 25 | 6 | 0 | 19 |
| theorems | 1020 | 51 | 9 | 0 | 42 |
| gates | 293 | 15 | 4 | 0 | 11 |
| data_provenance | 186 | 10 | 0 | 0 | 10 |
| session_files | 4 | 4 | 0 | 0 | 4 |
| equations | 144 | 8 | 0 | 8 | 0 |
| researchers | 2 | 2 | 0 | 0 | 2 |
| constants | 2 | 2 | 0 | 0 | 2 |
| registries | 4 | 4 | 0 | 0 | 4 |
| **TOTAL** | **2162** | **123** | **20** | **8** | **95** |

Spot-check agreement: 16.3% AGREE, 6.5% DISAGREE, 77.2% BORDERLINE.

---

## Table: closed_mechanisms  -  sampled 2 of 26 NOISE (7.7%)

### closed_atlas02_eraXI_147
- **name**: §VII.K-PROP-W8.CELL-OCCUPANCY (cutoff_AL2010 / cutoff_sqrt L2 status update)
- **source_file**: sessions\framework\Atlas\atlas-02-mechanism-lifecycle.md
- **Haiku NOISE reason**: Name mixes registry slot (§VII.K-PROP-W8) with cutoff parameters and status-update language; lacks clear mechanism descriptor.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      294: | 139 | §VII.AC.4 V1+C1 sequential-chain derivation of classification (a) | S87 CF-20 | LANDED | NON-PHONONIC | §VII.AC.4; SOURCE-DOUBLE-CITE-CO-PRIMARY anchor | volovik + connes |
      295: | 140 | §VII.AB.1-8 Atlas_5 / triple-protection family (C4 substrate sign-lock + K-homogeneity ODE family + sign-AND-magnitude lock + triple-protection at CMB pivot) | S86 W-3 | PROVEN structural | PHONONIC | §VII
      296: | 141 | **§VII.AF.1.OP-PROJ Pillar III ↔ Pillar IV Bridge — FIRST registered cross-pillar bridge** | S87 W5-1 | PASS Level-3 = 0.0095% F_4 strict; envelope L^{-3} at d=4 = 0.10%; margin 10.5× inside | GEOMETRIC | 
      297: | 142 | §VII.AF.2 §VII.P-v2 HP^1-content-distinct refinement (replaces failed HP^0-content-distinct) | S87 W5-4 | LANDED via mechanical-edit remediation | GEOMETRIC | §VII.AF.2; (η = 0, GV ≠ 0) parity-twin signatu
      298: | 143 | §VII.AG.1 T7 ↔ S67 cyclic-fold isomorphism (SECOND cross-pillar bridge) | S87 W6-1 | LANDED STAGE-1-CANDIDATE | GEOMETRIC | §VII.AG.1; canonical quotient-functor lift example (∞-dim Pillar-VII to finite-ra
      299: | 144 | §VII.AG.2-AG.6 sub-row family (PASS-quotient-isomorphism + Z_3 gauge-sector + D1 gauge-counting correction 
    ... [truncated]

### closed_28
- **name**: CF-68
- **source_file**: sessions\session-88\session-88-w12-workingpaper.md
- **Haiku NOISE reason**: Bare carry-forward ID fragment (CF-68); closed_by is process label (S87 stratum-3 L_max scan), not a mechanism identity.
- **Spot-check judgment**: **AGREE**  -  bare ID fragment (e.g. KC-2, L-1)
- **source_context (first 8 lines)**:
      618: | ULP_TOL | 1.0e-14 (S87 W11-2 canonical) |
      619: | N_BOT | 20 (S87 W11-2 canonical) |
      620: | regulator_axis | (Zubarev, zeta, Pauli-Villars, Mellin) |
      621: | scheme_axis | (HypA, HypB, HypC, HypD) |
      622: | N_CELLS | 16 (= 4 × 4) |
      623: | CV_CANONICAL | (2, 4, 8, 6) (S87-PARTITION-STABILITY-4STRATUM cv_anchor) |
      624: | spectrum source | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` filtered to p+q ≤ 10 |
      625: | GPU path | none (cache read + integer partition; CPU sufficient, OMP_NUM_THREADS=8) |
    ... +9 more lines

## Table: open_channels  -  sampled 25 of 481 NOISE (5.2%)

### open_123
- **name**: M_GUT (10^16 GeV)
- **source_file**: sessions\archive\session-25\session-25-Workshop-einstein-results.md
- **Haiku NOISE reason**: Table row entry (M_GUT scale) from cosmological-constant discrepancy analysis; is a row-label not an open channel itself.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted from a markdown table row
- **source_context (first 8 lines)**:
      185: **Partition function minimum (Feynman F-1)**: The depth is 12.1% in the T -> 0 limit:
      186: 
      187:     Delta F = lambda_min^2(0) - lambda_min^2(0.25) = 0.694 - 0.670 = 0.024
      188: 
      189: In KK units, Delta V / M_KK^4 ~ 0.024. The observed cosmological constant is Lambda_obs ~ 10^{-122} M_Pl^4. For any reasonable KK scale:
      190: 
      191: | M_KK | Delta V / Lambda_obs | Discrepancy |
      192: |:-----|:--------------------|:------------|
    ... +9 more lines

### open_684
- **name**: Non-standard M_KK
- **source_file**: sessions\framework\registry\constraint-mega-matrix.md
- **Haiku NOISE reason**: Closed-mechanism summary; lists M_KK value extracted as past event ('proton decay constraints + extraction') without open question.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      253: 
      254: ### IV.B Resolved Channels (Formerly Surviving)
      255: 
      256: | Channel (from S31) | Resolution | Session |
      257: |:-------------------|:-----------|:--------|
      258: | Instanton-driven Kapitza | CLOSED — structural monotonicity theorem | S37 |
      259: | Threshold corrections for NCG-KK | CLOSED — subsumed by pure KK interpretation | S50-S51 |
      260: | Finite-density spectral action (P2b) | CLOSED — no formalism developed, deprioritized | S38+ |
    ... +9 more lines

### open_368
- **name**: Concurrent agents
- **source_file**: sessions\session-85\session-85-full-s85-closeout.md
- **Haiku NOISE reason**: Concurrent agent count is a resource-allocation parameter, not a scientific question.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      667: ### §6.2 Wave-by-wave proposal (S86 plan opening draft)
      668: 
      669: Each wave below lists: (i) primary objective; (ii) §3 carry-forward IDs landing in this wave; (iii) sequencing prerequisites (must-precede dependencies); (iv) concurrent-agent count (target ≤ 8 per `feedback_max-8
      670: 
      671: **S86-W0 (FOUNDATION) — pipeline-discipline + canonical pin scoreboard refresh**
      672: - Primary objective: clear the methodology backlog so subsequent waves have clean tooling.
      673: - Carry-forwards landing: R1 `S86-RULE-FILE-V3-LANDING`, R2 `S86-PRU-EXTENSION-RULE-V2-LANDING`, R3 `S86-CUTOFF-AXIS-YAML-PIN`, R4 `S86-CANONICAL-PHRASING-AUDIT` (c_fabric), R5 `S86-CANON-PRDR-K-DISAMBIGUATION`, R
      674: - Sequencing prerequisite: NONE (foundation wave). MUST PRECEDE all later waves so SOURCE-RECONCILIATION sub-audit + cutoff_axis YAML pin + K-disambiguation are operative at S86 plan-freeze for subsequent
    ... +1 more lines

### open_339
- **name**: EMPIRICAL-τ_fold RETENTION
- **source_file**: sessions\session-84\session-84-w8-workingpaper.md
- **Haiku NOISE reason**: Name is a status tag (ACTIVE (default fallback)) not a scientific tension; description confirms empirical treatment, not an open question being tested.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
     1070: #### Constraint-map update (W9 branches closed vs open)
     1071: 
     1072: | Branch                                                   | Status                              | Reason |
     1073: |:---------------------------------------------------------|:------------------------------------|:-------|
     1074: | **BARE-SPECTRAL-ACTION as V.P. for τ_fold**              | **CLOSED**                          | §W8a-85 measures dS/dτ(Gauss) = −2.036 × 10⁴ ≠ 0 at τ_fold. Jensen ansatz falsified (slope 0.64, not in {+1, −1, +
     1075: | **DRESSED-SPECTRAL-ACTION as V.P. for τ_fold**           | **OPEN**                            | S42 canonical dS_fold = +58,672.8 uses abs-like cutoff (a DIFFERENT functional from Gaussian). BCS/GGE/Gilkey loop
     1076: | **GGE-ENTROPY-FUNCTIONAL as V.P.**                       | **OPEN**                            | τ_fold may extremize S_GGE (Jacobson-Λ_J horizon-entropy, BCS free-energy, integrated-out KK modulus effective act
     1077: | **MECHANISM-CHAIN selects τ_fold (dynamical, non-V.P.)** | **OPEN**                            | I-1 + Turing + RPA + WALL + BCS first-order transition criterion. Not a variational principle but a dynamical sele
    ... +1 more lines

### open_324
- **name**: F_amp(N3LO; N=3)
- **source_file**: sessions\session-84\session-84-w5-workingpaper.md
- **Haiku NOISE reason**: Table row with computed expansion coefficient F_amp(N3LO; N=3); computational output, not an open anomaly.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
       80: | Required cumulative suppression | 65.23 % | 1 − 1/R_req = 0.6523 |
       81: | a_1 (NLO coefficient) | 0.619204 | pinned to S82 W1-2 F_amp_canonical=1.0166 at N=3 |
       82: | a_2 (NNLO coefficient) | 9.298e-4 | pinned to S83 G11 Δ_NNLO = 1.32e-4 at N=3 |
       83: | a_3 (N3LO, Berges Borel-summable) | 2.653e-4 | a_1·a_2·(2/S_0), S_0 = 4.34 Jensen |
       84: | a_3 (leading-log cross-check) | 1.396e-6 | a_2²/a_1 |
       85: | F_amp(LO; N=3) | 1.281000 | — |
       86: | F_amp(NLO; N=3) | 1.016600 | reproduces S82 W1-2 F_amp_canonical ✓ |
       87: | F_amp(NNLO; N=3) | 1.016495 | Δ = +1.05e-4 (reproduces G11 Δ_NNLO) |
    ... +10 more lines

### open_245
- **name**: (b) RG
- **source_file**: sessions\session-62\session-62-results-workingpaper.md
- **Haiku NOISE reason**: RG-evolution subcomponent from combined-analysis table; constituent sub-route, not open question.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
     1274: BCS pairing modifies effective Yukawas by at most a factor 1.48 (additive O(1) correction). The generation-dependent correction arises from different sector overlaps with the pair wave function, but the B2-dominan
     1275: 
     1276: **Combined Analysis**
     1277: 
     1278: | Route | Best Ratio | Physical? | Mechanism |
     1279: |:------|:----------|:----------|:----------|
     1280: | Tree (S61) | 1.6 | Yes | Jensen scale factors |
     1281: | (a) KK modes | 6670 | Model-dependent | Sector-resolved overlaps |
    ... +9 more lines

### open_682
- **name**: Threshold corrections for NCG-KK
- **source_file**: sessions\framework\registry\constraint-mega-matrix.md
- **Haiku NOISE reason**: Status entry from resolved-channels table; purely narrative closure summary without new testable content.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      251: | **Spectral functional selection** | **NEW CRISIS (S66)** | ε_H sign reversal between cutoff families. Only sqrt(x) and anomaly(φ) survive Bayesian evidence. | FUNCTIONAL-SELECT-67: unique φ with n_s ∩ m_H |
      252: | **Transit dynamics** | OPEN | Mach 13.75 supersonic transit. Power spectrum computation pending. | TRANSIT-PS-67: |α_s(k_CMB)| < 0.015 |
      253: 
      254: ### IV.B Resolved Channels (Formerly Surviving)
      255: 
      256: | Channel (from S31) | Resolution | Session |
      257: |:-------------------|:-----------|:--------|
      258: | Instanton-driven Kapitza | CLOSED — structural monotonicity theorem | S37 |
    ... +9 more lines

### open_208
- **name**: Route E (cumulative geometric corrections)
- **source_file**: sessions\session-58\session-58-volovik-baptista-workshop.md
- **Haiku NOISE reason**: Route E is a categorical meta-observation (cumulative geometric corrections push downward) rather than a testable open channel; the real tension is whether individual corrections (mass, epsilon, weigh
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      524: **ENABLED by geometry:**
      525: 
      526: - **Route A (non-Leggett depletion)**: The geometric distinction between gapless (BA) and gapped (Leggett) modes is structural. BA modes are the Goldstone mode of the broken SU(3)$\times$SU(3) symmetry (Paper 15 S
      527: 
      528: - **Route D (spinor normalization)**: The factor $M_{Pl,\text{eff}}/M_{Pl,\text{unred}} = 3.92 \approx \sqrt{16}$ is derivable within the fiber geometry. Paper 14 constructs the 12D spinor as $\Delta_{12} = M_{8\t
    ... [truncated]

### open_63
- **name**: Plan SHA
- **source_file**: sessions\permanent-results-registry.md
- **Haiku NOISE reason**: Plan SHA is a verdict-line/artifact caption describing content, not a scientific tension or anomaly.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
    16767:    §VII.W-3.SUBSTRATE) → χ : A_F → M_2(ℂ) inheritance morphism → BdG laboratory measurement
    16768:    IN M_2(ℂ) image (§VII.W-3.LAB).
    16769: 
    16770: **Cross-link**: §VII.W-3.SUBSTRATE (substrate instance) + §VII.W-3.LAB (laboratory image bridge) +
    16771: §VII.W-2 (S87 W1a-5 BACKWARD biconditional with synthetic 2-eigenvalue toy; structurally
    16772: related FAIL-with-remediation precedent that motivated the rescue characterization).
    16773: 
    16774: **Audit SHAs** (this entry):
    ... +9 more lines

### open_803
- **name**: [-0.988, -0.942)
- **source_file**: sessions/framework/registry/pre-registered-observations.md
- **Haiku NOISE reason**: Cell A1 range is a table-row numeric boundary with associated verdict label; not an independent tension or forecast.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
       72: **Content SHA-256**: `801e4690eee8e7f4c4152be7701567229a377ab3d23a66a5a39b318469323d6f`
       73: **Audit SHA-256**: `f6e102fd5f322dd3f6fa1e4866c6a2f0c425f344d359cf07e37e4d5877cb265e`
       74: **Artifacts**: `computations/s84_w4_dr3_contingency_fine_grained.py`, `s84_w4_dr3_contingency_fine_grained.json`
       75: 
       76: This gate pre-registers a fine-grained seven-cell partition of the {DR3 central (w_0, w_a): outside R_842} plane, activated *only if* the parent gate (binary rectangle containment) fires FAIL at DR3 release. The r
       77: 
       78: | Cell | w_0 range | w_a range | Framework verdict | Scorecard entry |
       79: |:----|:----------|:----------|:------------------|:----------------|
    ... +6 more lines

### open_552
- **name**: Transit production
- **source_file**: sessions\session-67\session-67-synthesis.md
- **Haiku NOISE reason**: Table row (15.1 OOM is machinery parameter, not a real tension).
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      119: | Beta-relaxation microscopic rate | W7-C | PASS (52 OOM above H_eq) |
      120: 
      121: The Volovik CC mechanism is now structurally complete with no remaining obstructions.
      122: 
      123: ### 4d. Amplitude Gap — 0.80 OOM Remaining
      124: 
      125: | Stage | A_s gap | Computation |
      126: |:------|:--------|:------------|
    ... +9 more lines

### open_180
- **name**: EIGENVECTOR-48
- **source_file**: sessions\archive\session-48\session-48-results-workingpaper.md
- **Haiku NOISE reason**: Verdict-line summary: EIGENVECTOR-48 is a gate batch sub-item ID with weights summary, not a scientific anomaly or forecast.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
     1830: | Sub-item | Verdict | Key Number |
     1831: |:---------|:--------|:-----------|
     1832: | BERRY-EDGE-48 | INFO | 0 wall-localized states (t_inter=0.969, 0D limit) |
     1833: | DISSOLUTION-GOE-48 | INFO | <r>(eps=0)=0.366, no Poisson->GOE crossover in [0,eps_c] |
     1834: | VH-HIGHER-ORDER-48 | INFO | ||V^3||/||V||=0.0225, NOT forbidden by selection rules |
     1835: | B3-REPULSIVE-48 | INFO | No population inversion (Schwinger saturation), gap -3.5% |
     1836: | THREE-PHONON-48 | INFO | Gamma_3ph/gamma_H=6e-6 (single-particle: 94% off-resonance) |
     1837: | TRANSIT-279-48 | INFO | eps_SR=0.027, eta_SR=1.27 (NOT slow-roll), N_e=0.66 |
    ... +9 more lines

### open_576
- **name**: A_s insensitive to E_C** (W2-G)
- **source_file**: sessions\session-75\session-75-tesla-synthesis.md
- **Haiku NOISE reason**: Elasticity numerical parameter (0.003) with status tag (PASS); no novel tension.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      163: | **N_eff post-thermalization** (W3-M) | N_eff = 3.044 exactly, GGE erased by 10^{14} e-folds | PASS |
      164: | **Lefschetz n* = 60 promoted to permanent** (W3-C) | L_max=7 verified, topological invariant of L_Y | PASS |
      165: | **BDI class constant at all tau** (W3-B) | Pfaffian sgn = -1 at all 10 tau values, gap open | PASS |
      166: | **J-invariance tau-independent** (W3-D) | |Z_J/Z - 1| < 6e-11 at all 5 tau values | PASS |
      167: | **DNP, Pomeranchuk, FR all ROBUST at L=5,7** (W3-A) | Block-diagonal theorem makes (0,0) sector L-invariant | PASS |
      168: | **6-layer composite protection registered** (W4-A) | Registry entry #48, codimension-6 failure mode | PASS |
      169: | **BCC tiling uniquely determined** (W4-J) | 5 converging constraints: z=8, vertex-transitive, 4+3+1 bonds, S_4 symmetry, D_4 root lattice | PASS |
      170: | **Cross-correlation negligible** (W2-F) | delta_OOM = 2.84e-4, N_eff(phi) = 1 (single-mode concentration) | PASS |
    ... +6 more lines

### open_450
- **name**: Verdict file
- **source_file**: sessions\session-87\session-87-results-workingpaper.md
- **Haiku NOISE reason**: Verdict-file storage path reference; administrative note on artifact location.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
     2235: ### Cross-wave dependencies introduced
     2236: 
     2237: - **§VII.U / §VII.W d_eff=8 citations** are flagged for L-dependence audit per W1b-3 FAIL. Downstream gates (W2 / W4 / W5 / W6 cross-pillar bridge) citing d_eff=8 must include a **convention pin** (Conv A `d_eff =
     2238: - **§VII.U continuum-SD scheme remains canonical** per W1b-1 FAIL; PV-finite-L recalibration is closed at canonical PV/M_KK; alternative PV schemes (smooth-window) and mpmath-50-digit identity-precision audit carr
     2239: - **No new §VII.{letter} registry entry promoted from W1b** — W1b-6 CLASS-γ closes the only candidate conjecture for new-letter promotion. W1b-4 CLASS-B near-unique is conditional on disambiguation; not yet promot
     2240: 
     2241: ### Sig_5 ladder note (legitimate honest iteration)
     2242: 
    ... +2 more lines

### open_135
- **name**: [SP]S-5 Twistor correspondence
- **source_file**: sessions\archive\session-25\session-25-Workshop-sp-results.md
- **Haiku NOISE reason**: Status 'DEFERRED' and 'not computable' marks this as deferred carry-forward, not active open channel.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      370: | Einstein sign obstruction | Einstein [MEME]S-1 | Extended to a_4 level: c_mixed = 0, c_net = +0.444 > 0. |
      371: | KK |omega_3|^2 growth | KK-Q4 | Explained as fiber torsion, not base gauge field. Already in a_4_geom. |
      372: | Lichnerowicz bound | Baptista | Closes [SP]S-3 (spectral flow extension). |
      373: 
      374: ### Items Still Open
      375: 
      376: | Item | Status | Reason | Priority for Session 26 |
      377: |:-----|:-------|:-------|:----------------------|
    ... +9 more lines

### open_13
- **name**: Window-16
- **source_file**: sessions\session-88\atlas-uplift-materials\atlas-05-walls-doors-windows-materials.md
- **Haiku NOISE reason**: ID-only pattern 'Window-16' — actual channel name is 'CMB-HD α_s' in source context.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
       87: | Window-8 | BBN-VOLOVIK-67: can Volovik tracking vacuum reproduce BBN constraints at z ~ 10^9? Door-S66 enabled CC at present epoch but rho_vac/rho_rad = 0.67 at nucleosynthesis is the open question | S67 carry-f
       88: | Window-9 | TRANSIT-PS-67: transit power spectrum vs A_s mismatch; α_s prediction adjudication | S67 carry-forward; falsified by absence of consistent dynamical pathway | 0 yr (computational; deferred since S67) 
       89: | Window-10 | Cross-pillar K=3 Stage-2 verify: §VII.W-3.LAB STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion via 3-axis cross-reviewer dispatch (volovik transit-side + connes spectral-side + landau condensed-matter
       90: | Window-11 | 3He-B vortex spectroscopy (W11-C5): Caroli-Matricon ladder asymmetry at φ_67-clean; Gate 1 NULL on F1+F2+F5; Gate 2 ratio 7.3250±0.1%; Lancaster MCT-3 / Helsinki ROTA cells | `inheritance-falsifier-p
       91: | Window-12 | LISA Ω_GW (CGWB): Companion-null prediction Ω_GW = 8.299e-58 (5+ OOM null) at LISA m
    ... [truncated]

### open_191
- **name**: Volume exchange
- **source_file**: sessions\session-53\session-53-results-workingpaper.md
- **Haiku NOISE reason**: CLOSED status label in a mechanisms table, not a scientific question or observed tension.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
     1294: #### 3. SURVIVING PATHS TO FLATNESS
     1295: 
     1296: | Path | Status | Mechanism |
     1297: |:-----|:-------|:----------|
     1298: | Initial condition | OPEN | k=0 assumed, no explanation (standard cosmology) |
     1299: | BDI topology (Volovik) | OPEN (heuristic) | Z-classification protects Fermi point -> emergent flatness |
     1300: | Prior inflation | OPEN | Inflation at E > M_KK, pre-transit |
     1301: | Quantum cosmology (WDW) | OPEN | HH boundary condition on 12D WDW may select k=0 |
    ... +9 more lines

### open_321
- **name**: R_req = F_amp_bare / F_amp_target
- **source_file**: sessions\session-84\session-84-w5-workingpaper.md
- **Haiku NOISE reason**: Table row with derived numerical ratio (R_req = F_amp_bare / F_amp_target); not a scientific tension or forecast.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted from a markdown table row
- **source_context (first 8 lines)**:
       71: ```
       72: 
       73: **Key numbers (numbers-first)**:
       74: 
       75: | Quantity | Value | Source/pin |
       76: |:---|---:|:---|
       77: | F_amp_bare (LO) | 1.281 | plan anchor; S82 W2-4 dynamics-layer pivot |
       78: | F_amp_target | 0.4454 | plan §Key anchors; K_R5=1.9222 easiest-rescue branch |
    ... +9 more lines

### open_329
- **name**: `scan_range`
- **source_file**: sessions\session-84\session-84-w5-workingpaper.md
- **Haiku NOISE reason**: Plan machinery pin specification (scan_range discrete orders); computational parameter, not an open channel.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
       50: - PASS: F_amp(N3LO, K=2.035) ≤ 0.4454, AND |Δ(N3LO) − Δ(NNLO)| / |Δ(NNLO)| ≥ 10× (monotonic convergence).
       51: - FAIL: F_amp(N3LO, K=2.035) ≥ 0.4454 AND 1/N ratio |a_{N3LO}/a_NNLO| ≥ 0.75 (series saturating — rescue inaccessible).
       52: - INFO: F_amp < 0.4454 but ratio ≥ 0.75 (numerical PASS, structural stagnation).
       53: - Tolerance: RATIO (factor-3 band on F_amp).
       54: 
       55: **Machinery pin (PRDR)** (verbatim from plan):
       56: - `N_eval`: per-order a_i coefficients at 1/N expansion, evaluated at K=2.035 via 3PI resummation + FKK dressing.
       57: - `L_max`: 5 (S83 canonical for W2 regulator atlas).
    ... +9 more lines

### open_511
- **name**: 67/67 Baptista geometry checks
- **source_file**: sessions\archive\session-23\session-23a-synthesis.md
- **Haiku NOISE reason**: Table-row entry citing proven status 'PERMANENT' and session reference 17b; no scientific tension or anomaly tested.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      257: The K-1e closure is specific to the BCS condensation mechanism. Everything proven at machine epsilon is unaffected:
      258: 
      259: | Result | Session | Status |
      260: |:-------|:--------|:-------|
      261: | KO-dim = 6 | 7-8 | PERMANENT |
      262: | SM quantum numbers from Psi_+ = C^16 | 7 | PERMANENT |
      263: | [J, D_K(tau)] = 0 (CPT hardwired) | 17a | PERMANENT |
      264: | g_1/g_2 = e^{-2tau} | 17a | PERMANENT |
    ... +9 more lines

### open_590
- **name**: Step 4 (direction)
- **source_file**: sessions\session-82\session-82-mack-synthesis.md
- **Haiku NOISE reason**: Step 4 direction is verification result, not an open physical channel.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
       25: ### II.A. α_f_NL = 0 across 5 decades k (W3-4)
       26: 
       27: **Framework prediction** (S82 §VI.D): f_NL^{GGE,fabric}(k) = 0.054702 exactly across k ∈ {10⁻⁴, 10⁻³, 10⁻², 10⁻¹, 10⁰} Mpc⁻¹ (W2-15 phase-alignment k-scan confirmed 0% variation across 5 decades).
       28: 
       29: **Substitution chain (direction)**:
       30: - Step 1 (definition): α_f_NL := d ln f_NL / d ln k
       31: - Step 2 (substitution): f_NL(k) = |f_NL^cell| · N_cells / E_pathB² with |f_NL^cell| set at the fold, k-independent
       32: - Step 3 (simplification): only the dispersion phase k²·r_s·c_fabric / (2·ω_a·M_KK) introduces k-dependence; at CMB scales this is O(10⁻⁵¹) rad/mode
    ... +10 more lines

### open_124
- **name**: M_Planck (10^19 GeV)
- **source_file**: sessions\archive\session-25\session-25-Workshop-einstein-results.md
- **Haiku NOISE reason**: Table row entry (M_Planck scale) from same CC discrepancy table; row-label not an independent open question.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted from a markdown table row
- **source_context (first 8 lines)**:
      186: 
      187:     Delta F = lambda_min^2(0) - lambda_min^2(0.25) = 0.694 - 0.670 = 0.024
      188: 
      189: In KK units, Delta V / M_KK^4 ~ 0.024. The observed cosmological constant is Lambda_obs ~ 10^{-122} M_Pl^4. For any reasonable KK scale:
      190: 
      191: | M_KK | Delta V / Lambda_obs | Discrepancy |
      192: |:-----|:--------------------|:------------|
      193: | M_GUT (10^16 GeV) | 10^{112} | Factor 10^{112} |
    ... +9 more lines

### open_560
- **name**: N_eff = 3.044 post-thermalization
- **source_file**: sessions\session-75\session-75-mack-synthesis.md
- **Haiku NOISE reason**: Table row gate result (N_eff = 3.044 is a verified prediction, not an open tension).
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted from a markdown table row
- **source_context (first 8 lines)**:
      146: ## 3. Constraint Map Update
      147: 
      148: ### 3.1 Opened
      149: 
      150: | Constraint | Source | Significance |
      151: |:-----------|:-------|:-------------|
      152: | f_conv = (M_KK/M_Pl)^4 x (a_2/a_0)^2 | W1-E PASS | A_s gap structurally understood; 0.12 OOM residual |
      153: | Non-power-law H(tau) -> n_s = 0.9649 | W1-I PASS | Isocurvature mechanism reproduces Planck best-fit |
    ... +9 more lines

### open_298
- **name**: 0.950
- **source_file**: sessions\session-74\session-74-results-workingpaper.md
- **Haiku NOISE reason**: Tau-grid value (0.950) from Region II spectral scan; numerical data point, not open research tension.
- **Spot-check judgment**: **AGREE**  -  bare number
- **source_context (first 8 lines)**:
     4353: | 0.550 | 0.9680 | 6.5706 | 1.401e-03 | 3.105e-05 |
     4354: | 0.600 | 0.9419 | 5.9453 | 2.618e-03 | 5.250e-05 |
     4355: | 0.650 | 0.9140 | 5.3796 | 4.610e-03 | 8.364e-05 |
     4356: | 0.700 | 0.8848 | 4.8676 | 7.692e-03 | 1.263e-04 |
     4357: | 0.750 | 0.8547 | 4.4044 | 1.222e-02 | 1.816e-04 |
     4358: | 0.800 | 0.8239 | 3.9853 | 1.859e-02 | 2.498e-04 |
     4359: | 0.850 | 0.7929 | 3.6060 | 2.716e-02 | 3.302e-04 |
     4360: | 0.900 | 0.7619 | 3.2629 | 3.828e-02 | 4.211e-04 |
    ... +9 more lines

### open_660
- **name**: W11 Volovik CC Tracking promotion gap (§VII.AT slot allocation)**: W11 Volovik CC Tracking Wall (DILUTION-CC-66) is currently anchored at `framework-cc-oom.md` (Door 12 in atlas-05) and `falsifier-wat
- **source_file**: sessions/framework/Atlas/atlas-08-open-questions.md
- **Haiku NOISE reason**: W11 Volovik CC Tracking slot allocation is a registry-landing housekeeping task, not a physics test.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      275: 
      276: ## VII. Methodology Class (NEW 5th class; S82-S88)
      277: 
      278: > **Provenance**: Class introduced 2026-05-09 per atlas-08 uplift. Methodology-floor questions live at the layer-functor F image (substrate ↔ methodology pair) per `epistemic-discipline.md §"Layer-Decomposition"`.
      279: 
      280: | Q | Question | Session opened | Status | Source registry |
      281: |:--|:---------|:---------------|:-------|:-----------------|
      282: | **Q32** | **D3 audit knowledge.db round-trip gap**: ~37 of 66 §VII slots in `permanent-results-registry.md` are missing from `tools/knowledge.db` per atlas-07-materials Section 2 round-trip audit (PARTIAL or NO 
    ... +2 more lines

## Table: theorems  -  sampled 51 of 1020 NOISE (5.0%)

### proven_502
- **name**: Inputs**: `computations/canonical_constants.py`; the original session producing M_KK = 7.428660e+16 GeV (likely S52-S58 
- **source_file**: sessions\session-86\workshops\session-86-1a-s4-mack.md
- **statement (DB field)**: Inputs**: `computations/canonical_constants.py`; the original session producing M_KK = 7.428660e+16 GeV (likely S52-S58 era); MCP `mcp__knowledge__update_constant` interface.
- **Haiku NOISE reason**: Input enumeration from a carry-forward action item; not a theorem statement.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
      211: - **What**: `S87-LAB-FALSIFIER-S-LEVEL-PROPOSAL` — propose a new sub-A level `LAB-FALSIFIER-S` for rows with detection_ratio ≥ 100. Currently 7/9 rows clear this floor (SW1=XA1=58958, SW2=XB2=72.9, SW3=28.5, XA2=3
      212: - **Inputs**: `s86_w11_lab_falsifier_evoi_tree.csv` (9 rows with detection_ratio); `sessions/framework/evoi-framework.md` (current level ladder); W11 C6 verdict for current ladder definition (LAB-FALSIFIER A/B/C/D
      213: - **Gate**: `S87-LAB-FALSIFIER-S-LEVEL-PROPOSAL`. PASS = new level-S landed with sub-A threshold, 7/9 rows reassigned to level-S, lab-pillar joint P_decisive recomputed under new ladder. INFO = proposal lands but 
      214: - **Effort**: ~2 hours, 1 agent session (sagan-empiricist primary; mack-cosmic-bridge consult).
      215: 
      216: ### V.5. M_KK PROVENANCE add to canonical_constants.py
      217: 
      218: - **What**: `S87-M-KK-PROVENANCE-ADD` — add the missing PROVENANCE entry for `M_KK = 7.428660036284456e+16` GeV in `computations/ca
    ... +1 more lines

### proven_57
- **name**: Regulator-pin tag**: `a_2^{Mellin}` (per
- **source_file**: sessions\permanent-results-registry.md
- **statement (DB field)**: Regulator-pin tag**: `a_2^{Mellin}` (per
- **Haiku NOISE reason**: Incomplete fragment: 'Regulator-pin tag**: `a_2^{Mellin}` (per' cuts off mid-clause.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
    13305: - **Landing date**: 2026-04-28.
    13306: - **Landing agent**: lizzi-spectral-functional-theorist.
    13307: - **Plan reference**: `sessions/session-plan/session-87-plan-w1a.md` §W1a-1
    13308:   (lines 49-211).
    13309: - **Producing script**: `computations/s87_w1a_w1b_t5_mellin_strip_landing.py`.
    13310: - **JSON sidecar**: `computations/s87_w1a_w1b_t5_landing.json`.
    13311: - **Verdict file**: `computations/s87_gate_verdicts.txt`.
    13312: - **Landing audit_sha256**: `74c16f36e83643f121948b969da1e1a4270a982c0974a94e39442c96710ad3bb`.
    ... +9 more lines

### proven_375
- **name**: Script: `computations/s82_w2_5_heat_kernel_mp.py`
- **source_file**: sessions\session-82\session-82-results-workingpaper.md
- **statement (DB field)**: Script: `computations/s82_w2_5_heat_kernel_mp.py`
- **Haiku NOISE reason**: File path only; artifact listing without theorem content.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
     1980: Consequence for UNIFIED-AS-79 (per P4-C §D1-E2): the sign-flip between a_0 routing (f* amplifies by 32x) and a_2 routing (f* suppresses by 2.617x) is NOT a regulator-choice ambiguity — it is a **manifestation of t
     1981: 
     1982: The taxonomy above also answers P4-C's open question on "non-C^1-regulator exclusion generality": any kernel with fractional-power branch at x = 0 (0 < alpha < 1) is excluded by the same mechanism; log kernels are
     1983: 
     1984: ---
     1985: 
     1986: #### §V.E.5 Artifacts and provenance
     1987: 
    ... +6 more lines

### proven_1925
- **name**: STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY (V supplies spectral-functional premise; C supplies SR-LO-dynamical theorem C
- **source_file**: sessions\framework\registry\falsifier-master-inventory.md
- **statement (DB field)**: STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY (V supplies spectral-functional premise; C supplies SR-LO-dynamical theorem CONDITIONAL on substrate-IC class assignment; both must converge for the rank to 
- **Haiku NOISE reason**: Incomplete: STRUCTURE tag fragment; no substantive theorem content, just label.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      965: **L3 (spectral-functional, lizzi-side) + T3 (transit-dynamics / SR-LO ODE side, volovik) cross-domain convergence at S86 W-9 R3 closure**: `sessions/session-86/workshops/s86-alpha-s-tension-and-sign-lock.md` Round
      966: 
      967: ### Provenance — SOURCE-DOUBLE-CITE-CO-PRIMARY
      968: 
      969: Per `.claude/rules/registry-landing.md` §"SOURCE-DOUBLE-CITE-CO-PRIMARY": the rank ordering is a sequential V_input + C_output chain — neither layer alone fixes the conclusion.
      970: 
      971: - **ANCHOR-1 (input layer V — L3 spectral-functional evaluation domain)**: lizzi's L3 ranking criteria — (a) NCG-axiomatic compatibility, (b) spectral-action moment hierarchy independence, (c) propagator-class-pro
    ... [truncated]

### proven_1615
- **name**: Sessions S52–S60
- **source_file**: sessions/framework/ARCHIVE/baseline-findings-s66.md
- **statement (DB field)**: S52–S60 | ~50 | 15 | 20 | 15 | — | —
- **Haiku NOISE reason**: Table row label with session statistics, not a theorem.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      135: ## Section 3: Complete Gate Verdict Registry
      136: 
      137: ### 3A. Cumulative Gate Statistics
      138: 
      139: | Source | Period | Total | PASS | FAIL | INFO | CLOSED | CONDITIONAL |
      140: |:-------|:-------|:------|:-----|:-----|:-----|:-------|:------------|
      141: | Permanent registry | S7–S28 | ~30 | 12 | 5 | — | 8 | 1 (KC-3) |
      142: | Mega-matrix | S29–S31 | ~20 | 6 | 6 | — | 5 | — |
    ... +9 more lines

### proven_218
- **name**: Fermionic fiber: 16
- **source_file**: sessions\archive\session-20\session-20b-paasch-collab.md
- **statement (DB field)**: Fermionic fiber: 16
- **Haiku NOISE reason**: Single-word bare statement 'Fermionic fiber: 16' is a fact fragment, not a theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
       10: 
       11: ### 1.1 The Constant-Ratio Trap as a Structural Theorem
       12: 
       13: The central result of Session 20b is not merely that the TT Casimir route fails. It is that the failure has the same character as every previous failure: the fermion-to-boson energy ratio R = F/B is set geometrica
       14: 
       15: From my perspective as a mass quantization analyst, this is the most important finding of the entire session. The fiber dimension ratio determines the asymptotic F/B balance:
       16: 
       17: - Bosonic fiber: 1 (scalar) + 8 (vector) + 35 (TT at tau=0) = 44
    ... +7 more lines

### proven_434
- **name**: W3-5 two-speed transfer identity c_S_canon = f_B** (PASS, machine precision): max|ratio−1| = 0.000e+00 across all 5 regu
- **source_file**: sessions\session-85\session-85-s7-combined-landscape-gen-physicist.md
- **statement (DB field)**: W3-5 two-speed transfer identity c_S_canon = f_B** (PASS, machine precision): max|ratio−1| = 0.000e+00 across all 5 regulators on the inflationary sub-corridor; promotable as a Landau structural theor
- **Haiku NOISE reason**: Status tag with numerical result across regulators; lacks theorem structural form.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
       34: (B) observational pre-registrations (flagship channels with frozen 0-free-parameter predictions awaiting external data);
       35: (C) structural open channels (FAILs that map a wall, refinements pending);
       36: (D) surviving FAIL classes (truncation / methodology / observability / infrastructure).
       37: 
       38: #### (A) Permanent-registry-grade theorems (17 entries)
       39: 
       40: **PHONONIC-class** —
       41: - **W3-1 PIXIE K_FIRAS regulator-invariance** (PASS, 5-regulator spread = 0 by γ=1 lockout fixed point): μ(K_FIRAS) = 8.6949e-5 is regulator-invariant *by construction*; paired with W0-8 PIXIE pull = 8693σ as flag
    ... +7 more lines

### proven_1687
- **name**: Casimir scalar + vector
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: Casimir scalar + vector | Monotonically increasing | S19d D-1
- **Haiku NOISE reason**: Table-row closure mechanism: one-word property + session code; insufficient for theorem validation.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
       45: Mechanisms tested and proven unable to stabilize the modulus, produce the required dynamics, or solve the CC problem. Running total: 141+ closures across 10 eras.
       46: 
       47: ### II.A Perturbative Potential (14 closures, Sessions 17-22)
       48: 
       49: | # | Mechanism | Why It Fails | Session |
       50: |:--|:---------|:-------------|:--------|
       51: | 1 | V_tree minimum | No tree-level minimum in Dirac spectrum functional | S17a SP-4 |
       52: | 2 | 1-loop Coleman-Weinberg | F/B = 8.4:1 fermionic dominance, monotonic | S18 |
    ... +9 more lines

### proven_688
- **name**: Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY closure**: plan substitution-chain L^{-3} attribution drift surfaced via anal
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY closure**: plan substitution-chain L^{-3} attribution drift surfaced via analytical pre-compute + empirical Richardson fit comparison; resolved in-session by
- **Haiku NOISE reason**: Truncated Class-(d) closure note; incomplete methodological resolution statement.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
      344: - `S89_W3_9_tau_max_HK5_regime_FW_verdict_sha` (pinned in pin-map): `136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df`
      345: - **audit_sha256** (full 64-char): `5c7cbe480ded228cdd7d0879a23d4c07d335c21f8921ddbbcdb8d3e85ed0410b`
      346: - **content_sha256** (full 64-char): `f3d3386b169f624ff32a2a1cefb79c3568e15ec3128d07623453e9e483a098a4`
      347: 
      348: ##### (l) Self-assessment
      349: 
      350: - **Structural position**: New canonical `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5π = 15.707963267948966` lands as the substrate-first asymptotic-limit pin; the pre-existing `tau_max_HK5_regime_FW = 12.475002
      351: - **L^{-1}-vs-L^{-3} structural finding**: empirically confirmed that the Source-3 Taylor-truncation estimator has L^{-1}-dominant convergence (NOT L^{-3} as plan asserted). The plan's L^{-3} attribution was a cro
    ... +2 more lines

### proven_748
- **name**: Forward gate at S91+**: `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` Stage-2 dispatch (pre-registered at CF-48);
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: Forward gate at S91+**: `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` Stage-2 dispatch (pre-registered at CF-48); parallel dispatch with one Axis-A reviewer + one Axis-B reviewer; PASS-AND aggr
- **Haiku NOISE reason**: Forward gate specification truncated mid-sentence.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
     1250: - **Structural position**: Var_a(n_a^GGE) is the SECOND framework cross-axis joint theorem in the `joint-theorem-promotion.md` 4-stage pipeline. The §VII.U.2 Corner-II classification (algebra-INVARIANT × s=4) is s
     1251: - **CF-50 INFO clause-(d) atlas-row re-frame**: honest disclosure preserved in corrigendum text; the F_traj=(k+1)/2 identity is at the atlas-row layer (S84 W3-24 theorem), NOT the BdG-cache extension. MIXED-of-RD-
     1252: - **Solo-runner ownership preservation of mack canonical role**: `mack-cosmic-bridge` sole-writer-role per `feedback_mack-bridge-role.md` is preserved as substrate-physics content authorship; the orchestrator-dire
     1253: - **Bridge-landing AFTER-pattern compliance**: build_promotion_text → write_atomic_with_fsync (Windows-compatible try/except OSError on fsync) → re_read_and_verify (6 verifier rubric clauses) → emit_verdict_line (
    ... [truncated]

### THEO-8835
- **name**: <missing>
- **source_file**: <?>
- **Haiku NOISE reason**: Single-word file/section reference 'Atlas' without substantive theorem content.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:

### proven_634
- **name**: content_sha256** (full 64-char): `e1d2cc0761a606a6d3787fcf5e9186b94496f60406b5e30dbd6e3cf75fe78f7c` = SHA-256
- **source_file**: sessions\session-90\session-90-w2-workingpaper.md
- **statement (DB field)**: content_sha256** (full 64-char): `e1d2cc0761a606a6d3787fcf5e9186b94496f60406b5e30dbd6e3cf75fe78f7c` = SHA-256
- **Haiku NOISE reason**: Another SHA-256 hash label without theorem statement or substance.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
      357: | Registry entry (§VII.AW.OP-PROJ block) | `sessions/permanent-results-registry.md` line 17435 (~140 lines block) | Heading grep at 17435; 4 clauses at relative lines 41/45/50/62; idempotency-guarded under re-run 
      358: | Verdict file (V.0 FAIL + V.1 PASS supersedes chain) | `computations/session-90/s90_gate_verdicts.txt` (4 lines: V.0 canonical + V.0 companion + V.1 canonical + V.1 companion) | tail-verified; gate-ID grep count 
      359: | MCP audit queries | 3 queries logged in §"MCP Pre-Compute Audit" above | Pre-compute hygiene per `knowledge-index-usage.md` |
      360: 
      361: ##### (k) Input-pin SHAs (S84+ dual-SHA closure)
      362: 
      363: V.1 dual-SHA:
      364: - **audit_sha256** (full 64-char): `86d4414497f82dbd30d2ad6bc03299e09dfb9beddc497b0ab2b8c8c71622de85` = SHA-256(V.1_script_bytes ‖ canonical_constants_bytes ‖ pinmap_json_canonical)
    ... +10 more lines

### proven_685
- **name**: content_sha256** (full 64-char): `f3d3386b169f624ff32a2a1cefb79c3568e15ec3128d07623453e9e483a098a4`
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: content_sha256** (full 64-char): `f3d3386b169f624ff32a2a1cefb79c3568e15ec3128d07623453e9e483a098a4`
- **Haiku NOISE reason**: Bare SHA-256 hex string; no theorem content, only audit artifact label.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      338: | Plot | `computations/session-90/s90_w6_hk5_richardson_lmax_inf.png` | 127997 bytes; two-panel: (left) 4-point convergence with three c0 horizontal lines (DIRECT 5π PRIMARY, L^{-3} c0=13.75, L^{-1}+L^{-3} c0=15.5
      339: | Verdict line | `computations/session-90/s90_gate_verdicts.txt` last 3 lines (canonical + W9a-99 + S87+ 3-tuple) | tail-verified; audit_sha256 `5c7cbe480ded228c...` unique |
      340: 
      341: ##### (k) Input-pin SHAs (S84+ dual-SHA closure)
      342: 
      343: - `computations/_shared/canonical_constants.py` SHA-256: `5a19a04e0adef8cd…`
      344: - `S89_W3_9_tau_max_HK5_regime_FW_verdict_sha` (pinned in pin-map): `136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df`
      345: - **audit_sha256** (full 64-char): `5c7cbe480ded228cdd7d0879a23d4c07d335c21f8921ddbbcdb8d3e85ed0410b`
    ... +6 more lines

### proven_138
- **name**: Writer**: mack-cosmic-bridge
- **source_file**: sessions\session-88\s88-pending-edits-ledger.md
- **statement (DB field)**: Writer**: mack-cosmic-bridge
- **Haiku NOISE reason**: Single bare identifier; not a theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      312: - **Source**: `s88-mack-arxiv-2511-07517-desi-review.md` §5.6
      313: - **Target**: `sessions/framework/registry/pre-registered-observations.md` (or `falsifier-master-inventory.md` as scope note)
      314: - **Append**: ~5-line scope note — substrate framework is silent on SN intrinsic-color physics (α=0.169, β=3.14, γ=0.033 fit empirically; no first-principles prediction; explicit-silence prevents future inference 
      315: 
      316: ### B.28 — permanent-results-registry.md: §VII.AF.1 OP-PROJ suffix-retrofit
      317: - **Source**: `s88-w11-w3b-15-kde-substrate-vs-tautology.md` §V.4
      318: - **Target**: `sessions/permanent-results-registry.md` §VII.AF.1
      319: - **Action**: rename `§VII.AF.1` → `§VII.AF.1.OP-PROJ`; allocate parallel empty `§VII.AF.1.STATE-PROJ` slot with PENDING-VERIFICATION marker
    ... +7 more lines

### proven_566
- **name**: L_max: N/A
- **source_file**: sessions\session-88\session-88-w5b-workingpaper.md
- **statement (DB field)**: L_max: N/A
- **Haiku NOISE reason**: L_max parameter label only; single-word entry without substantive theorem content.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      105:    → §VII.U.2 STAGE-1-CANDIDATE registry landing  (laboratory-IN audit-trail commitment)
      106: ```
      107: 
      108: No "container space" appears in this chain; the substrate IS the spectral triple, IS the orthogonal classification, and IS the registry-PASS observable.
      109: 
      110: **4-tuple**:
      111: - scheme: `four-corner-NCG-axiomatic-classification`
      112: - convention: `joint-theorem-promotion-Stage-1-CANDIDATE`
    ... +9 more lines

### proven_1928
- **name**: Producing script: `computations/s86_w12_fisher_pdf_pin.py`
- **source_file**: sessions\framework\registry\fisher-pdf-registry.md
- **statement (DB field)**: Producing script: `computations/s86_w12_fisher_pdf_pin.py`
- **Haiku NOISE reason**: File path reference only: script name; no theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      106:              Original verdict VALUE/SCHEME/CONVENTION/L_max preserved
      107:              unchanged in s85_gate_verdicts.txt; only input-pin map
      108:              changes (now references Fisher-PDF SHAs from this registry).
      109: ```
      110: 
      111: ## Provenance
      112: 
      113: - Plan: `sessions/session-plan/session-86-plan-w12.md` §W12-3
    ... +9 more lines

### proven_1819
- **name**: 52-60
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: — | — | Transit era. 33+ closures. No formal Sagan assessment.
- **Haiku NOISE reason**: Era label with closure count reference; meta-statement without theorem form.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
       78: 
       79: ### II.C Retracted / Superseded
       80: 
       81: | Claim | Status | Session |
       82: |:------|:-------|:--------|
       83: | Session 21b "4-5x coupling" | RETRACTED — within-sector Kosmann norm, not inter-sector matrix elements | S22b |
       84: | Tesla g·N(0) ~ 8-10 | RETRACTED — corrected to 3.24 | S22c |
       85: 
    ... +9 more lines

### proven_1359
- **name**: phi_paasch status
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: Physical prediction (BF=5) | Mathematical property (BF=2) | 28
- **Haiku NOISE reason**: Status-reclassification entry; statement is a meta-claim about evidence basis.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      483: 
      484: | What | Original | Corrected | Session |
      485: |:-----|:---------|:----------|:--------|
      486: | AZ class | DIII (T^2 = -1) | BDI (T^2 = +1) -- chiral, not Kramers | 17c |
      487: | "4-5x coupling" | Inter-sector D_K coupling | RETRACTED: was Kosmann norm, not matrix elements | 22b |
      488: | Berry curvature B=982.5 | Berry curvature | ERRATUM: was quantum metric. Berry = 0 exactly (W5). | 25 |
      489: | a_6 "theorem" | All a_{2n} monotone | Downgraded to conjecture beyond a_6 | 27 |
      490: | Baptista P_LZ = 0.97 | LZ transition probability | Retracted: LZ inapplicable (codim-1) | 28 |
    ... +9 more lines

### proven_1590
- **name**: Chirality antisymmetry: {γ_9, dD_K/dτ}=0. Chiral pairs ADD, not cancel
- **source_file**: sessions/framework/ARCHIVE/baseline-findings-s66.md
- **statement (DB field)**: S64 W6-B | PERMANENT
- **Haiku NOISE reason**: Statement is table-cell label with session code and status only, lacks substantive content.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted from a markdown table row
- **source_context (first 8 lines)**:
       84: 
       85: | Result | Session | Status |
       86: |:-------|:--------|:-------|
       87: | R-monotonicity on Jensen (AM-GM exact): dR/dτ ≥ 0 | S64 W1-A | PERMANENT |
       88: | Fermi-surface lock: v²(B2[0]) = 1/2 identically | S64 W2-C | PERMANENT |
       89: | a_0/a_2 trap (off-Jensen): decreasing a_2 INCREASES a_0/a_2 | S64 W2-A | PERMANENT |
       90: | Spectral moment decoupling: F_{−1}(CC) vs F_{+1}(NEC) are different moments | S64 W5-B | PERMANENT |
       91: | H2 theorem: π_{ij}=0 from DeWitt tracelessness (volume-preserving) | S64 W3-A | PERMANENT |
    ... +10 more lines

### proven_902
- **name**: What**: Merge the W8-86 OZ derivation, W5-62 partition invariance, W10-123 axiomatic closure, and W6-52 CMB-S4 projectio
- **source_file**: sessions\session-84\session-84-s1-landau-alpha_s-synthesis.md
- **statement (DB field)**: What**: Merge the W8-86 OZ derivation, W5-62 partition invariance, W10-123 axiomatic closure, and W6-52 CMB-S4 projection into a single UPGRADED permanent-result registry entry for "α_s = n_s² − 1". S
- **Haiku NOISE reason**: Incomplete carry-forward task description (starts with 'What**:'), not a substantive theorem.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      299: 
      300: - **What**: Land a formal registry entry in `sessions/framework/landau-classification-of-phonon-exflation.md` classifying the substrate's scalar-perturbation sector as "OZ single-pole universality class (gapped me
      301: - **Inputs**: This synthesis, W8-86 working paper, Landau-classification-of-phonon-exflation.md current text.
      302: - **Gate**: Registry-hygiene PASS — one canonical classification statement with derivation chain linked to the five decisive gates.
      303: - **Effort**: 0.25 session.
      304: 
      305: ### V.6. Consolidated permanent-result upgrade
      306: 
    ... +7 more lines

### proven_641
- **name**: PRU compliance**: all machinery enumerated in plan §W2-2 §7 (registry slot allocation, writer assignment, co-signer chai
- **source_file**: sessions\session-90\session-90-w2-workingpaper.md
- **statement (DB field)**: PRU compliance**: all machinery enumerated in plan §W2-2 §7 (registry slot allocation, writer assignment, co-signer chain, producing script, verdict source, allowlist append, L_max=10, scheme, convent
- **Haiku NOISE reason**: Incomplete fragment; statement truncated mid-sentence with no closing delimiters.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      376: The V.0/V.1 audit_sha256 difference arose from: (i) V.1 script bytes differ (window-extraction fix + supersedes constant added); (ii) V.1 registry pre-edit SHA differs from V.0 (V.0 mutated registry to add §VII.AW
      377: 
      378: ##### (l) Self-assessment
      379: 
      380: - **Structural position**: registers the SUBSTRATE-CLOCK-UNIQUENESS-THEOREM as STAGE-1-CANDIDATE in the framework's permanent-results registry. The 5-criteria saturation theorem (proven at S89 W3-6 close) is now t
      381: - **Substitution-chain canonicality**: 19 anchor-text-matching checks (CC1-CC19) stated explicitly and Python-verified post-write on V.1. The 19/19 verify result is the artifact-existence boolean driving the V.1 P
      382: - **L_max robustness**: L_max=10 per S89 W3-1 PASS LANDED; Friedrich-Bär saturation theorem analytically certifies bottom-K invariance for ALL L_max ≥ 10. The theorem's structural content is L_max-INDEPENDENT at t
      383: - **Honest disclosure of V.0→V.1 corrective**: the V.0 FAIL was a script-bug (verify-window 8000-char cap; the entry was correctly landed but verify falsely failed 3/19 checks on late-block clauses). T
    ... +1 more lines

### proven_1814
- **name**: 24b
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: 5% (4-7%) | 3% (2-4%) | Combined BF = 0.31
- **Haiku NOISE reason**: Probability bounds with descriptor; table row fragment, not substantive theorem.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      345: |:--------|:------|:------|:----------|
      346: | Pre-22 | 40% | — | Before traps discovered |
      347: | 22a | 46% | — | Pomeranchuk pass |
      348: | 22b | 38% | — | Block-diagonal theorem |
      349: | 22c | 44% | — | Perturbative Exhaustion |
      350: | 22d | 40% | 27% | Clock closure, DESI closed |
      351: | 23a | 6-10% | 4-8% | **Venus: K-1e fires** |
      352: | 24a | 5-7% | 2-3% | V-1 fires |
    ... +9 more lines

### proven_1243
- **name**: Extended from 1D Jensen to full 3D U(2)-invariant surface (V_spec/F_BCS ~ 8000)
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: Extended from 1D Jensen to full 3D U(2)-invariant surface (V_spec/F_BCS ~ 8000) | 30Ba
- **Haiku NOISE reason**: Table cell fragment—extension note with session code, not a theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      238: | W4 | Spectral Action Monotonicity | Tr f(D^2/Lambda^2) monotone in tau, both connections, all cutoffs, all T | Exact to 10^{-39} |
      239: | W5 | Berry Curvature Vanishing | K_a anti-Hermitian => Berry curvature = 0 identically. Closes all topological mechanisms. | Exact |
      240: | W6 | Thermodynamic Stabilization | Smooth functional trap + Matsubara stiffening. | Exact |
      241: 
      242: ### Walls Extended (Sessions 30-40)
      243: 
      244: | Wall | Extension | Session |
      245: |:-----|:----------|:--------|
    ... +9 more lines

### proven_1208
- **name**: [NEW S62] Delta > 0.353 M_KK along softest Hessian direction
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: 20 points | 7.1x threshold | 62 | `s62_type_i_transit.py`
- **Haiku NOISE reason**: Table cell: threshold and scale values, no complete theorem.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      152: | [NEW S61] 36D Hessian ALL 36 eigenvalues negative | 36 directions | All negative | 61 | `s61_hessian_36d.py` |
      153: | [NEW S61] Kasparov product 6/6 conditions | First computation | All PASS | 61 | `s61_kasparov_product.py` |
      154: | [NEW S61] EWSR Thouless identity | 16/16 checks | 14 sig figs | 61 | `s61_ewsr_thouless.py` |
      155: | [NEW S62] CF-9 |A_coset|^2 = 3/2 + (3/2)e^{-4tau} | 21 tau points | < 2e-14 | 62 | `s62_berry_projection.py` |
      156: | [NEW S62] Higgs doublet gauge-invariant in End(C^48) | 10 irreps | 3.5e-14 mixing | 62 | `s62_higgs_order_one.py` |
      157: | [NEW S62] Cauchy-Schwarz hierarchy on D_K spectrum | 6 families | All PASS (discrete) | 62 | `s62_cauchy_schwarz.py` |
      158: | [NEW S62] Meissner D_s(GGE)/D_s(fold) = 0.9885 | 5 routes | All PASS | 62 | `s62_meissner_gge.py` |
      159: | [NEW S62] BdG gauge fraction: gauge/gravity = 2.723 (structural formula) | 8 modes | Algebraic identity | 62 | `s62_bdg_gauge_fraction.py` |
    ... +9 more lines

### proven_1885
- **name**: Cross-Reviewer Audit-Machinery Self-Citation
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: SUGGESTION | K=1 | S88 W-23 W7c-167 V.8 | `pru-class-corpus.md §16` + `cross-pillar-bridge-corpus.md §12`
- **Haiku NOISE reason**: Table row with bare code citations; not a theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      567: | Mechanical-closure layer-separability carve-out (Type-F) | SUGGESTION | K=1 | S88 W8-89 | `mechanical-closure-discipline.md §"Layer-separability carve-out"` |
      568: | Element 3 fiducial-anchor binding discipline (cross-pillar) | SUGGESTION | K=1 | S88 W-15 W15-V.7 | `cross-pillar-bridge-corpus.md §6` (Element 3) |
      569: | Single-τ-slice vs moduli-deformation substrate-IS levels | advancing | K=2 | S88 W2-10 + W7 W2-2 V.4 | `phononic-framing.md §"Single-τ-slice vs moduli-deformation"` |
      570: | Definitional-datum-vs-derived-theorem K-counter | advancing | K=2 | S88 (`epistemic-discipline.md §"Layer-Decomposition"`) | `pru-class-corpus.md §9` |
      571: | F(observable) vs F(trigger predicate) split | SUGGESTION | K=1 | S88 (`epistemic-discipline.md §"Layer-Decomposition"`) | `pru-class-corpus.md §10` |
      572: | Forward-pinned-follow-up wave class | SUGGESTION | K=1 | S88 W-25 W7c-167 | `pru-class-corpus.md §13` |
      573: | Layer-2-A vs Layer-2-B coverage | SUGGESTION | K=1 | S88 W4a-17 V.3 | `cross-pillar-bridge-corpus.md §9` |
      574: | Surrogate-vs-Canonical at cohomology-class layer | SUGGESTION | K=1 | S88 W-9 W3a-18 V.5 | `pru-class-corpus.md §11` |
    ... +4 more lines

### proven_1233
- **name**: EIH Casimir Monotonicity: local a_0/a_2 increases with C_2(p,q)
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: PERMANENT | 65 W6-A | Structural
- **Haiku NOISE reason**: Statement field contains only metadata codes (PERMANENT | 65 W6-A | Structural), no substantive mathematical content.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      190: | a_0/a_2 trap (off-Jensen): decreasing a_2 INCREASES a_0/a_2 | PERMANENT | 64 W2-A | Candidate wall |
      191: | Spectral moment decoupling: F_{-1}(CC) vs F_{+1}(NEC) are different moments | PERMANENT | 64 W5-B | Structural |
      192: | H2 theorem: pi_ij=0 from DeWitt tracelessness (volume-preserving) | PERMANENT | 64 W3-A | Structural |
      193: | Chirality antisymmetry: {gamma_9, dD_K/dtau}=0. Chiral pairs ADD, not cancel | PERMANENT | 64 W6-B | Algebraic |
      194: | BdG Heat Kernel Factorization: K_BdG(t) = exp(-Delta^2 t) K_bare(t) | PERMANENT | 64-65 | Structural |
      195: | CC Ratio from Scalar Curvature Only: d(a_0/a_2)/ds = -(a_0/a_2)/R dR/ds | PERMANENT | 65 W1-B | Structural |
      196: | B/F Spectral Asymmetry = 0: |A|=0 EXACTLY on pure Riemannian triple | PERMANENT | 65 W1-C | Exact |
      197: | Bogoliubov Gaussianity Preservation: f_NL = O(eps) regardless of squeezing | PERMANENT | 65 W5-D | Structural |
    ... +6 more lines

### proven_1863
- **name**: Cross-pillar-bridge Pole-Scope (T1-20)
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: MANDATORY | K=4 | S88 W7a-72 close, 2026-05-05 | `pru-class-corpus.md §3`
- **Haiku NOISE reason**: Status string + reference only; no substantive theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      540: 
      541: | Rule / discipline | Status | K-count | Source | Calibration corpus location |
      542: |:-------------------|:-------|:-------:|:-------|:------------------------------|
      543: | Cross-pillar-bridge-anatomy 5-anatomy + 3-level | MANDATORY | K=3 | S88 W4a-17 close, 2026-05-04 | `cross-pillar-bridge-corpus.md §5` |
      544: | Algebra-axis orthogonality 4-corner | MANDATORY | K=3 | S87 W-2 R3 close | `cross-pillar-bridge-corpus.md §6` |
      545: | PRU Class 8.2 verifier-rubric | MANDATORY | K=5 | S88 W-7+W-21+W-22 simultaneous K=2→K=5, 2026-05-08 | `pru-class-corpus.md §1` |
      546: | PRU Class 8.3 publication-precision | MANDATORY | K=4 | post-S87 W8 | `pru-class-corpus.md §2` |
      547: | Cross-pillar-bridge Level-2 Layer Distinction | MANDATORY | K=3 (post-W3b-15 + W7a-74 V.5 promotion) | S88 W-22 W7a-74 V.5 close | `cross-pillar-bridge-corpus.md §1+§7` |
    ... +6 more lines

### proven_727
- **name**: lizzi-spectral-functional-theorist** is PRIMARY author of clauses (a) Cell-II identity (JOINT), (c) parse-tree decision 
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: lizzi-spectral-functional-theorist** is PRIMARY author of clauses (a) Cell-II identity (JOINT), (c) parse-tree decision procedure, (d) F_traj atlas-row identity (S84 W3-24 theorem), (e) convergence ve
- **Haiku NOISE reason**: Authorship attribution list fragment; role disclosure, not a theorem
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
     1191: 
     1192: ##### (h) Solo-runner ownership disclosure (per `/rclab-solo` agent-ownership-takeover)
     1193: 
     1194: `mack-cosmic-bridge` is the canonical SOLE WRITER for the §VII.U.2 registry row per `feedback_mack-bridge-role.md`. Plan §W6-6 designates this role explicitly. Under `/rclab-solo` agent-ownership-takeover discipli
     1195: 
     1196: > "The solo runner TAKES OWNERSHIP of the gate — DO NOT spawn the designated agent via the Agent tool. ... The corpus is loaded for context only, NOT for delegation. No Agent-tool dispatch under any circumstance d
     1197: 
     1198: The substrate-physics content authorship is PRESERVED:
    ... +6 more lines

### proven_1824
- **name**: Fabric + n_s
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: S46-S49 | 7 | O-Z Friedmann mass (115 OOM), Bragg gap (KK scale), Leggett transit (destroyed post-transit)
- **Haiku NOISE reason**: Table-cell enumeration of closures without theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      395: **Source**: `sessions/framework/Atlas/atlas-02-mechanism-lifecycle.md`, `atlas-05-walls-doors-windows.md`
      396: 
      397: ### IX.A Closure Eras (S32-S51: 49 closures, bringing total from 26 to 75)
      398: 
      399: | Era | Sessions | Count | Key Closures |
      400: |:----|:---------|:------|:-------------|
      401: | BCS Chain + Instanton | S35-S38 | 7 | Cutoff SA (structural monotonicity), one-loop RPA self-trapping (wrong sign), (B1,B3,G1) PMNS triad (algebraic), CC-through-instanton (76x margin) |
      402: | Transit + Cosmology | S39-S46 | 15 | Friedmann-BCS (38,600x), self-tuning runaway, Zak phase retracted, acoustic horizon retracted |
    ... +9 more lines

### proven_458
- **name**: Structural position**: AUDIT / registration gate; lands the ledger consequence of S84-W7-74's FAIL verdict. The PASS is 
- **source_file**: sessions\session-85\session-85-w10-workingpaper.md
- **statement (DB field)**: Structural position**: AUDIT / registration gate; lands the ledger consequence of S84-W7-74's FAIL verdict. The PASS is infrastructural (ledger bookkeeping) — the physics verdict ("det(P)=1 does not u
- **Haiku NOISE reason**: Truncated self-assessment label and partial status descriptor.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      196: - `.claude/agent-memory/kaku-speculative-theorist/s64-collab-review.md`: `21f63191551cecf5...`
      197: - `.claude/agent-memory/kaku-speculative-theorist/s64-phonon-strings-investigation.md`: `7c5175218ed6f690...`
      198: - S84-W7-74 closure reference SHA (verified byte-for-byte): `def5d0cdb8a39d16017820a602cb8821fefcbbc8720700f3eb6e5b095d4af1d2`
      199: - Gate closure — `audit_sha256`: `e034e19f7fbc3d9642997559ed8fd77c070e98331d07dddbf04405b2c464fddc`
      200: - Gate closure — `content_sha256`: `5e5f6f0dcb6cbefcbfe146aa9ecc056f55b653469308a487308518ef36042138`
      201: 
      202: ##### (l) Self-assessment
      203: 
    ... +5 more lines

### proven_1661
- **name**: 155,984
- **source_file**: sessions/framework/ARCHIVE/baseline-findings-s66.md
- **statement (DB field)**: — | D_K eigenvalues at L_max=10
- **Haiku NOISE reason**: Table cell entry: single-word label '155,984' paired with bare count, no substantive theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      529: | a_0 | 6440 | Mode count (τ-independent) |
      530: | a_2(fold) | 2776.17 | Second Seeley-DeWitt coefficient |
      531: | a_4(fold) | 1350.72 | Fourth Seeley-DeWitt coefficient |
      532: | Δ_B3 | 0.370 M_KK | BCS gap at fold |
      533: | ω_L1 | 0.138 M_KK | Leggett mode frequency |
      534: | Q_Leggett | 18.6 | Quality factor |
      535: | E_J/E_C | 8.57 (zeta a_4) | Josephson ratio |
      536: | φ_paasch | 1.531580 | Eigenvalue ratio at τ=0.15 |
    ... +9 more lines

### proven_686
- **name**: Structural position**: New canonical `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5π = 15.707963267948966` lands as the 
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: Structural position**: New canonical `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5π = 15.707963267948966` lands as the substrate-first asymptotic-limit pin; the pre-existing `tau_max_HK5_regime_FW = 
- **Haiku NOISE reason**: Truncated structural-position statement; incomplete theorem about canonical pin definitions.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
      342: 
      343: - `computations/_shared/canonical_constants.py` SHA-256: `5a19a04e0adef8cd…`
      344: - `S89_W3_9_tau_max_HK5_regime_FW_verdict_sha` (pinned in pin-map): `136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df`
      345: - **audit_sha256** (full 64-char): `5c7cbe480ded228cdd7d0879a23d4c07d335c21f8921ddbbcdb8d3e85ed0410b`
      346: - **content_sha256** (full 64-char): `f3d3386b169f624ff32a2a1cefb79c3568e15ec3128d07623453e9e483a098a4`
      347: 
      348: ##### (l) Self-assessment
      349: 
    ... +3 more lines

### proven_1084
- **name**: §VII.AF.1.STATE-PROJ companion slot
- **source_file**: sessions/framework/Atlas/atlas-04-assumptions.md
- **statement (DB field)**: §VII.AF.1.STATE-PROJ companion slot | Pillar III↔IV state-projection STRUCTURALLY-ORTHOGONAL-COMPANION | PENDING-VERIFICATION
- **Haiku NOISE reason**: Status marker and slot identifier only; no substantive theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      157: |:--|:---------------------------|:----------------------|:----------------------|
      158: | **K1** | §VII.U.2 four-corner classification | Algebra-axis × Mellin-pole 4-corner partition | Stage-2 pending |
      159: | **K2** | §VII.AC.1 Path-H/Path-C classification (a) | Multi-valued classification with V+C SOURCE-DOUBLE-CITE-CO-PRIMARY | Stage-2 pending |
      160: | **K3** | §VII.AD Δ_0 localization formula | Δ_0 = 4·c_{σ⁻¹((-1,-1))} on substrate (2,4,8,6) at τ_fold | Stage-2 pending |
      161: | **K4** | §VII.AG.1 T7↔S67 cyclic-fold isomorphism | Pillar VII↔V cross-pillar bridge with 0.0095% residual | Stage-2 pending |
      162: | **K5** | §VII.W-3.LAB inheritance-falsifier protocol | rank-2 ker(ι_*) 4-gate Class A NULL + Class B cohomology-asymmetry | Stage-2 pending |
      163: | **K6** | §VII.AM Universal Lock Condition | 3-clause: pixelation lock + effacement lock + Page-time lock | Stage-2 pending |
      164: | **K7** | §VII.X.W4-1 9-cell tensor 3-channel bridge | Cross-pillar 3-channel R^{(k)}_{p,q}(L_max=10) | Stage-2 pending |
    ... +5 more lines

### proven_604
- **name**: audit_sha256 (script || canonical || pinmap): `ae56c819b1cc3e038180728f4f7d0d05fd6ce92256dcc0d86a45741d61a37c47`
- **source_file**: sessions\session-88\session-88-w7a-workingpaper.md
- **statement (DB field)**: audit_sha256 (script || canonical || pinmap): `ae56c819b1cc3e038180728f4f7d0d05fd6ce92256dcc0d86a45741d61a37c47`
- **Haiku NOISE reason**: Bare SHA-256 hash string; not a theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      417: 
      418: ##### (k) Input-pin SHAs (S84+ dual-SHA closure)
      419: 
      420: - `.claude/rules/epistemic-discipline.md` post-edit: `963b6ec306e003a9...`
      421: - `.claude/rules/methodology-wave-allowlist.md` post-edit: `007179fc3b1330b3...`
      422: - `sessions/session-plan/session-88-plan-w7a.md`: `3d8fa396d4c13187...`
      423: - `computations/session-87/s87_gate_verdicts.txt` (input source for instance verdict-lines): `fa96b3bde6fe269d...`
      424: - `computations/_shared/canonical_constants.py`: `a42eb64b78024715...`
    ... +10 more lines

### proven_25
- **name**: Canonical reference S66_RAW_RANGE = 381.0 in
- **source_file**: sessions\permanent-results-registry.md
- **statement (DB field)**: Canonical reference S66_RAW_RANGE = 381.0 in
- **Haiku NOISE reason**: Bare canonical reference assignment; not a theorem statement.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
     4823: | Block structure D_K = D_B1 + D_B2 + D_B3                   | **FUNCTIONAL-INDEPENDENT** (exact at all L_max) |
     4824: | dim ker D_K, eta invariant, index                          | **FUNCTIONAL-INDEPENDENT** (integer-valued topological) |
     4825: 
     4826: ### Provenance
     4827: 
     4828: - S75 W3 gate verdict: S75-G3-ZETA-NOT-PHYS PASS 3/3 routes
     4829:   (`computations/s75_zeta_not_physical.py`, lines 607-637 PERMANENT
     4830:    THEOREM block; 34,473 B; canonical at L_max = 3 truncation)
    ... +9 more lines

### proven_360
- **name**: FUNCTIONAL-INDEPENDENT: eigenvalue ratios, moment ratios, ratio-of-ratios (1.7% L_max shift), tau-derivatives, block str
- **source_file**: sessions\session-75\session-75-results-workingpaper.md
- **statement (DB field)**: FUNCTIONAL-INDEPENDENT: eigenvalue ratios, moment ratios, ratio-of-ratios (1.7% L_max shift), tau-derivatives, block structure D_K = D_B1 + D_B2 + D_B3, topological invariants, w_0 = -0.918, alpha_s =
- **Haiku NOISE reason**: Truncated list fragment (FUNCTIONAL-INDEPENDENT:...) with incomplete statement and ellipsis; no substantive theorem
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
     1786: 
     1787: S_zeta = a_4 shifts **10.4x (1.02 OOM)** from L_max=3 to L_max=7. The cutoff action shifts 69.0x. But the ratio-of-ratios (a_0/a_2)/(a_2/a_4) shifts only **1.7%** across the same range. Physical observables must b
     1788: 
     1789: **Common obstruction**: UV_REGULARIZATION_CONFLATION. zeta_D(s) at any fixed s = s_0 imposes a SPECIFIC weighting |lam|^{-2s_0} on the eigenvalue sum. This weighting determines which UV modes contribute. Different
     1790: 
     1791: **PERMANENT THEOREM (Spectral Zeta Non-Observability)**: Let D_K be a Dirac operator on a compact spectral triple (A, H, D_K). The spectral zeta function zeta_D(s) = Tr |D_K|^{-2s} is NOT a physical observable. (i
     1792: 
     1793: **Positive classification -- what IS physical**:
    ... +2 more lines

### proven_1276
- **name**: [NEW S45] Bogoliubov/KZ n_s (all k-mappings)
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: [NEW S45] Bogoliubov/KZ n_s (all k-mappings) | 45 | n_s = -4.45 (EIH), -0.588 (primary)
- **Haiku NOISE reason**: Table row excerpt; numeric results for alternative parameterizations, no theorem body.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      311: | 36 | [NEW S40] HESS full moduli stabilization | 40 | W9: all 22 eigenvalues positive, 27th equilibrium closure |
      312: | 37 | [NEW S42] Fano interference (discrete+discrete) | 42 | K anti-Hermitian forces q=infinity |
      313: | 38 | [NEW S42] Polariton Higgs | 42 | Min gap 0.063 M_KK, 3.7e13x too large |
      314: | 39 | [NEW S42] Slow-roll n_s from spectral action | 42 | eta = 0.243, structural |
      315: | 40 | [NEW S44] Lifshitz anomalous dimension for n_s | 44 | eta_eff = 3.77, Weyl's law |
      316: | 41 | [NEW S44] Foam stabilization of tau | 44 | 0/900 minima found |
      317: | 42 | [NEW S45] Occupied-state spectral action | 45 | S_occ monotone decreasing |
      318: | 43 | [NEW S45] Unexpanded spectral action CC hierarchy | 45 | Taylor exactness on finite spectrum |
    ... +9 more lines

### proven_938
- **name**: Three algebraic traps
- **source_file**: sessions\archive\session-23\session-23-sagan-verdict.md
- **statement (DB field)**: Three algebraic traps
- **Haiku NOISE reason**: Bare heading listing three algebraic trap types; no complete statement.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      179: These survive K-1e and would survive even if the entire physical program collapses:
      180: 
      181: - KO-dim = 6 (parameter-free)
      182: - SM quantum numbers from C^16
      183: - CPT hardwired: [J, D_K(tau)] = 0
      184: - g_1/g_2 = e^{-2tau} structural identity
      185: - 67/67 Baptista geometry checks
      186: - D_K block-diagonality theorem
    ... +9 more lines

### proven_84
- **name**: W4a-16 data: `computations/s88_w4a_a0_m2_backward_rescue_theorem.npz` + `.json`
- **source_file**: sessions\permanent-results-registry.md
- **statement (DB field)**: W4a-16 data: `computations/s88_w4a_a0_m2_backward_rescue_theorem.npz` + `.json`
- **Haiku NOISE reason**: Data file path label, no theorem content.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    16774: **Audit SHAs** (this entry):
    16775: - Plan SHA: pinned at §W4a-16 + §W4a-17 plan blocks
    16776: - W4a-16 audit_sha256: `63acc9cd17a2323d30f6c722792ff839400a9378e8307b496d1d456b1f30d731`
    16777: - W4a-16 content_sha256: `1912cc503085cf8b5abbcf7a184d10f385ebd3928275fd34691b930ca1f606d8`
    16778: - Workshop precedent SHA (S87 W1a-5 R3 Prompt-3): `9c0a290ef55b128b`
    16779: 
    16780: **Producing artifacts**:
    16781: - W4a-16 script: `computations/s88_w4a_a0_m2_backward_rescue_theorem.py`
    ... +9 more lines

### proven_1883
- **name**: Layer-2-A vs Layer-2-B coverage
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: SUGGESTION | K=1 | S88 W4a-17 V.3 | `cross-pillar-bridge-corpus.md §9`
- **Haiku NOISE reason**: Table cell label with section reference; no theorem content.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      565: | Substrate-input-orthogonality clause (Stage-2) | SUGGESTION | K=1 | S88 W7c-167 | `pru-class-corpus.md §15` + `cross-pillar-bridge-corpus.md §11` |
      566: | Closing-paragraph-coherence audit pattern (EG1) | SUGGESTION | K=1 | S88 W7c-167 | `pru-class-corpus.md §14` |
      567: | Mechanical-closure layer-separability carve-out (Type-F) | SUGGESTION | K=1 | S88 W8-89 | `mechanical-closure-discipline.md §"Layer-separability carve-out"` |
      568: | Element 3 fiducial-anchor binding discipline (cross-pillar) | SUGGESTION | K=1 | S88 W-15 W15-V.7 | `cross-pillar-bridge-corpus.md §6` (Element 3) |
      569: | Single-τ-slice vs moduli-deformation substrate-IS levels | advancing | K=2 | S88 W2-10 + W7 W2-2 V.4 | `phononic-framing.md §"Single-τ-slice vs moduli-deformation"` |
      570: | Definitional-datum-vs-derived-theorem K-counter | advancing | K=2 | S88 (`epistemic-discipline.md §"Layer-Decomposition"`) | `pru-class-corpus.md §9` |
      571: | F(observable) vs F(trigger predicate) split | SUGGESTION | K=1 | S88 (`epistemic-discipline.md §"Layer-Decomposition"`) | `pru-class-corpus.md §10` |
      572: | Forward-pinned-follow-up wave class | SUGGESTION | K=1 | S88 W-25 W7c-167 | `pru-class-corpus.md §13` |
    ... +4 more lines

### proven_1177
- **name**: TT stability: no tachyons
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: all tau in [0,2] | Positive | 20b | `l20_lichnerowicz.py`
- **Haiku NOISE reason**: Status field contains script name only; statement is measurement results without theorem form.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      121: | Riemann tensor R_{abcd}(tau) | 147/147 | Machine epsilon | 20a | `r20a_riemann_tensor.py` |
      122: | Volume-preserving TT-deformation | det = 1.000000000 | Exact | 12 | `dirac_spectrum.py` |
      123: | 4 curvature invariants (analytic) | Exact formulas | Rational coefficients | 17b | `sp2_analytic_derivation.py` |
      124: | Dirac pipeline (8 validations) | All < 10^{-10} | Machine epsilon | 12 | `dirac_spectrum.py` |
      125: | AZ class BDI, T^2 = +1 | -- | Exact | 17c | `d4_bdg_classification.py` |
      126: | lambda^2 = n/36 algebraic spectrum | 16 integers | Exact algebraic | 12 | `dirac_spectrum.py` |
      127: | Pfaffian Z_2 = +1 throughout | 100+ tau | Binary | 17c | `d2_pfaffian_computation.py` |
      128: | Gauss-Bonnet chi(SU(3)) = 0 | 21 tau | 1.24e-15 | 21c | -- |
    ... +9 more lines

### proven_383
- **name**: Hille-Phillips, *Functional Analysis and Semi-Groups* (1957): Bernstein functions have Levy-Khintchine representation bu
- **source_file**: sessions\session-82\session-82-results-workingpaper.md
- **statement (DB field)**: Hille-Phillips, *Functional Analysis and Semi-Groups* (1957): Bernstein functions have Levy-Khintchine representation but only CM functions have positive Radon Laplace representation.
- **Haiku NOISE reason**: Truncated bibliographic citation; incomplete theorem statement about Bernstein functions.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
     1991: - Canonical reproduction: f*(0) = 0.088, int_0^50 f* du = 215.05, int_0^50 x f* du = 6448.90 -- within 0.04% of canonical `mellin_f_star_{f0, f2, f4}`
     1992: - Closure SHA: `98267d631c9f7a2c57f68e5feb767284a211f1987bc1e7fd412f2cfdfbf693c0`
     1993: - Verdict line: appended to `computations/s82_gate_verdicts.txt`.
     1994: 
     1995: **References**:
     1996: - Chamseddine-Connes 1996 (arXiv:hep-th/9606001) §2.2-2.3: the regulator f enters the bosonic spectral action via Mellin moments f_0, f_2, f_4 of its restriction to [0, infinity); the heat-kernel expansion uses th
     1997: - Connes-Moscovici 1995 §5: the local index formula requires a regular spectral triple with simple dimension spectrum Sd subset Z; integer-power-Lambda asymptotic follows from the residue calculus on zeta function
     1998: - Widder, *The Laplace Transform* (1941), Ch. IV: Hausdorff-Bernstein-Widder characterization of CM functions as positive Laplace transforms.
    ... +5 more lines

### proven_1716
- **name**: 30-55
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: *26 additional fabric-scale closures* | See Atlas D02 + session working papers S52-S60 | S52-S60
- **Haiku NOISE reason**: Bare reference to range '30-55' with only indirect pointer to external docs, not a substantive theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
       89: |:--|:---------|:-------------|:--------|
       90: | 23 | N_e saturation (e-fold mapping) | N_e = 0.1734, IC-independent. Structural theorem. | S52 |
       91: | 24 | BCS baryogenesis | φ_CP = 0 identically (algebraic) | S52 |
       92: | 25 | Lattice ED stabilization | d²E_0/dτ² = 0.33, 193x below threshold | S54 |
       93: | 26 | Gauge frustration | < 3.5% flux quantum — negligible | S56 |
       94: | 27 | Unimodular gravity for CC | Volume preservation ≠ CC suppression | S60 |
       95: | 28 | CC staircase | |Λ_res| oscillates, no convergence | S60 |
       96: | 29 | Leptogenesis (real M_R) | No CP phase | S60 |
    ... +9 more lines

### proven_706
- **name**: audit_sha256** (full 64-char): `2ba9d07429912025d7d9cac9d39ef4cfbdf794de5102f94e4406c1509d01dffe`
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: audit_sha256** (full 64-char): `2ba9d07429912025d7d9cac9d39ef4cfbdf794de5102f94e4406c1509d01dffe`
- **Haiku NOISE reason**: SHA hash value; not a theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      790: | Plot | `computations/session-90/s90_w6_var_a_level_dressed_k2_scan.png` | 126,984 bytes; two-panel: (left) 5-regulator bar chart side-by-side LEVEL=S vs LEVEL=P on log scale + D_max + ρ_S; (right) rank-vector co
      791: | Verdict line | `computations/session-90/s90_gate_verdicts.txt` last 4 lines (canonical + W9a-99 + S87+ 3-tuple + tier_pin=TIER-2) | tail-verified; audit_sha256 `2ba9d07429912025...` unique |
      792: 
      793: ##### (q) Input-pin SHAs (S84+ dual-SHA closure)
      794: 
      795: - `computations/_shared/canonical_constants.py` SHA-256: `5a19a04e0adef8cd…`
      796: - `computations/session-84/s84_spectrum_cache_L12_tau019.npz` SHA-256: `9e6d9cf7fd6a6949…`
      797: - `computations/_shared/_spectral_action_regulators.py` SHA-256: `2fc40ccbb62fcbf1…`
    ... +8 more lines

### proven_481
- **name**: CC-4** all L_max = 10:           **PASS
- **source_file**: sessions\session-85\session-85-w3-workingpaper.md
- **statement (DB field)**: CC-4** all L_max = 10:           **PASS
- **Haiku NOISE reason**: Bare PASS/FAIL result label from a checklist item; no substantive theorem statement.
- **Spot-check judgment**: **AGREE**  -  algebraic identity extracted as bullet sub-clause inside larger theorem
- **source_context (first 8 lines)**:
      355: - **Joint statement — "Landau structural block"**:
      356:   > *The inflationary sub-corridor K ∈ [K_R5, K_crit] carries an Altland-Zirnbauer BDI class certified at L_max=10 with 8 Goldstones via G = SU(3)×SO(3)×U(1)_rel×U(1)_T → H = SU(2)×U(1)×SO(2), and all regulator-cl
      357: 
      358: - **Registry patch (draft, assembled for future landing — see `s85_w3_consolidated_upgrade.json`)**: ready to append to `sessions/framework/permanent-results-registry.md` when that file is created (the file does n
      359: 
      360: - **CC-1** n_inconsistencies == 0:  **PASS** (= 0)
      361: - **CC-2** 4 components present:    **PASS**
      362: - **CC-3** 6 pairs (4 choose 2):    **PASS**
    ... +9 more lines

### proven_471
- **name**: PRU compliance**: 9/9 machinery-pin parameters pinned; 4 N/A for audit class, 5 substantive. No PRU Class-8 gap. No exec
- **source_file**: sessions\session-85\session-85-w10-workingpaper.md
- **statement (DB field)**: PRU compliance**: 9/9 machinery-pin parameters pinned; 4 N/A for audit class, 5 substantive. No PRU Class-8 gap. No execution-property failure classes (binary audit; canonical input-pin map).
- **Haiku NOISE reason**: Truncated fragment from self-assessment section; status tag only, no complete theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      411: - Gate closure — `content_sha256`: `b9a6a3014218386add94df8fef1034df5e17feb467c4d4b9cecacadfb133cd09`
      412: 
      413: ##### (l) Self-assessment
      414: 
      415: - **Structural position**: AUDIT gate; LOCKOUT-C verification + DR3 wiring lineage check + V.1-conditional addendum. The PASS value `locked-v1-pending` occupies the dispatch-not-halt leaf of the plan's decision tr
      416: - **Substitution-chain canonicality**: 6 chains (CC1–CC6) stated explicitly and Python-verified inline. All equalities checked against registry §VII.M.1 verbatim values. No shortcut reasoning; the derived half-wid
      417: - **L_max robustness**: N/A. R_842 is an observational rectangle with no L_max dependence. Lineage inherits L_max=N/A from S84-W1b-9.
      418: - **Downstream triggers**: (i) Post-Batch-2 carry-forward: complete the V.1-conditional addendum once a V.1-schema-compliant W6 output lands. (ii) W10-4 w_0 branch enumeration may produce a third stable w_0 branch
    ... +2 more lines

### proven_773
- **name**: Depends on**: mack-cosmic-bridge sole-writer convention; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-
- **source_file**: sessions\session-91\session-91-w6-workingpaper.md
- **statement (DB field)**: Depends on**: mack-cosmic-bridge sole-writer convention; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY; `joint-theorem-promotion.md` 4-stage pathway.
- **Haiku NOISE reason**: Bare dependency reference to rule files without a substantive theorem claim or structural statement.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      767: - **Depends on**: this gate (negative result motivates the retry); `canonical_constants.py` SCHEMATIC vs FULL level-pin discipline; `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` P
      768: 
      769: #### CF-S91-W6-2-K_HK-PERMANENT-PROMOTION (P2 — FI permanent registry landing)
      770: 
      771: - **What**: promote K_HK = 9 FI partition cardinality result to permanent registry entry at the algebra-INVARIANT functional family (algebra-axis corner I per `permanent-results-registry.md §VII.U.2` 4-corner part
      772: - **Inputs**: this gate's audit_sha=`109e4307e8a0d80578318de29315b688287704cba1518bd651845db4a1cb984f` (PASS-component K_HK = 9 FI); S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 cal
    ... [truncated]

### proven_740
- **name**: audit_sha256** (full 64-char): `8c89990382f16a9b1ffd9b506ee98bb8231fefed49d9b84da437aa564eae93d3`
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: audit_sha256** (full 64-char): `8c89990382f16a9b1ffd9b506ee98bb8231fefed49d9b84da437aa564eae93d3`
- **Haiku NOISE reason**: SHA-256 hash literal — table cell value, not a theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
     1237: | Verdict line | `computations/session-90/s90_gate_verdicts.txt` last 2 lines (canonical + W9a-99 dual-SHA companion) | tail-verified; audit_sha256 `8c89990382f16a9b...` unique |
     1238: 
     1239: ##### (l) Input-pin SHAs (S84+ dual-SHA closure)
     1240: 
     1241: - `computations/_shared/canonical_constants.py` SHA-256: `5a19a04e0adef8cd…`
     1242: - `sessions/permanent-results-registry.md` (pre-edit) SHA-256: `9177352b7e6d516f…`
     1243: - `sessions/permanent-results-registry.md` (post-edit) SHA-256: `69594707c6f48e12…`
     1244: - Promotion text SHA-256 (corrigendum content): `93e07fe58ed7e2d5…`
    ... +8 more lines

### proven_1866
- **name**: Joint-theorem 4-stage promotion pathway
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: MANDATORY (single-instance origin) | — | S86 W-9 close | corpus growing (§VII.AH instance #1, §VII.AM #2, §VII.W-3.LAB #3)
- **Haiku NOISE reason**: Status string + corpus reference only; no substantive theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      512: 
      513: Per atlas-12: the S82–S88 era produced a structured methodology floor binding plan-freeze admissibility. The full enumeration lives in atlas-12; this is the high-level mega-matrix surface.
      514: 
      515: | Methodology constraint | Status | Source rule | Cross-link |
      516: |:------------------------|:-------|:-------------|:-----------|
      517: | Layer-functor F (substrate ↔ methodology ↔ audit triplet) | pair-verified at S86 R3; audit-leg pending | `epistemic-discipline.md §"Layer-Decomposition"` | atlas-12 §II |
      518: | Phi correspondence (graded-ring isomorphism `weight(a_n^SD) = weight(Σ_n)`) | pair-verified | `epistemic-discipline.md §"Phi correspondence"` | atlas-12 §III |
      519: | PRU Class 8.0–8.6 sub-class taxonomy | mixed (8.0/8.1 MANDATORY; 8.2 MANDATORY-K=5; 8.3 MANDATORY-K=4; 8.4/8.5/8.6 K=1 advisory) | `epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class
    ... +5 more lines

### proven_419
- **name**: Registry citations (T-9, T-19, T-27, T-41, §VII.P, §XV-B, DILUTION-CC-66, framework-cc-oom CC Closures 5/6) traced via k
- **source_file**: sessions\session-85\session-85-1a-cc-residue-phonon-first.md
- **statement (DB field)**: Registry citations (T-9, T-19, T-27, T-41, §VII.P, §XV-B, DILUTION-CC-66, framework-cc-oom CC Closures 5/6) traced via knowledge MCP search results to `permanent-results-registry.md` lines 42, 50, 91,
- **Haiku NOISE reason**: Provenance footer bullet point; citation traceability listing, not a theorem.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      297: 
      298: ## Provenance footer
      299: 
      300: - All quantitative claims in §II.6 verified via Python (`phonon-exflation-sim/.venv312/Scripts/python.exe`) before being stated:
      301:   - log₁₀(ρ_Parker / ρ_Λ_obs) = 116.4828 OOM (matches W7-2 verdict to 4 s.f.)
      302:   - factor mismatch (CC-Γ A / obs) = 2.5584 (matches W7-3 self-assessment 2.56 to 3 s.f.)
      303:   - log-additive joint H_3 = 116.89 OOM, multiplicative H_4 = 112.96 OOM, ε^N for full cancellation requires N ≈ 33.07
      304: - All identity claims preceded by knowledge MCP queries listed in the source-document block.
    ... +3 more lines

### proven_1487
- **name**: §VII.P → §VII.AF.2 v2
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: DEPRECATED (S86 W9 C24 HP^0-content-distinct attempt superseded by §VII.AF.2 HP^1-content-distinct at S87 W5-4) | atlas-09 Item 39 cross-link
- **Haiku NOISE reason**: Slot reference: §VII.P deprecated pointer to §VII.AF.2 v2; is cross-link marker, not theorem.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      745: | §VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE | First fb_pair(M) construction at S86 W-7 (per `epistemic-discipline.md §"Forward-Backward Inference Closure"`) | S86 W-7 | gen-physicist | PERMANENT (methodology-floo
      746: 
      747: ### XVI.H. Promotion-gap & deprecated slots
      748: 
      749: | §VII slot | Status | Notes |
      750: |:----------|:-------|:------|
      751: | §VII.AT | OPEN (recommended for S89+ housekeeping per atlas-08 Q34) | W11 Volovik CC Tracking Wall (DILUTION-CC-66) currently anchored at `framework-cc-oom.md` + `falsifier-watchlist.md`; lacks dedicated §VII sl
      752: | §VII.AN | RETRACTED-anchor-structure (S88 W-15 V.6 cross-corner conflation retraction per atlas-09 Item 41); ANCHOR-1 + ANCHOR-2 retained but reclassified from CO-PRIMARY to STRUCTURALLY-ORTHOGONAL-COMPANION | a
    ... +9 more lines

## Table: gates  -  sampled 15 of 293 NOISE (5.1%)

### gate_G-29c
- **name**: G-29c
- **source_file**: sessions\archive\session-29\session-29Ab-synthesis.md
- **Haiku NOISE reason**: Single letter prefix; no wave or mechanism context; not S82+ gate-ID format.
- **Spot-check judgment**: **AGREE**  -  bare ID fragment (e.g. KC-2, L-1)
- **source_context (first 8 lines)**:
       20: ---
       21: 
       22: ## II. Gate Verdicts (Summary)
       23: 
       24: | Gate | Type | Verdict | Decisive Number |
       25: |:-----|:-----|:--------|:----------------|
       26: | K-29c | Hard close | **DOES NOT FIRE** | F_BCS = -5.63 at tau=0.50 (mu=lambda_min); < 0 everywhere |
       27: | K-29d | Hard close | **DOES NOT FIRE** | Sign reversal = False at all tau; Gi_ratio = 0.13 |
    ... +9 more lines

### gate_E-2
- **name**: E-2
- **source_file**: sessions\archive\session-22\session-22-master-synthesis.md
- **Haiku NOISE reason**: Single-letter round identifier (E-2); round-name label without session/wave/mechanism context.
- **Spot-check judgment**: **AGREE**  -  bare ID fragment (e.g. KC-2, L-1)
- **source_context (first 8 lines)**:
      220: |:---------|:----|:-----|:--|:---------|:----|:----|:------|
      221: | A: FR trapping | 0.05 | 0 | V_FR | 0.0463 | −0.9999 | −0.0002 | CLOSED (15,000×) |
      222: | B: FR overshoot | 0.05 | 0.02 | V_FR | 0.0463 | −0.9999 | −0.0002 | CLOSED (15,000×) |
      223: | C: Pure CW roll | 0.05 | 0 | V_CW | 0.0258 | −0.9957 | −0.005 | CLOSED (82,000×) |
      224: | D: Frozen at min | 0.30 | 0 | V_FR | 0.3000 | −1.0000 | 0 | PASS |
      225: | E: Near-minimum | 0.29 | 0 | V_FR | 0.2902 | −1.0000 | 0 | CLOSED (800×) |
      226: | F: Settling | 0.25 | 0.001 | V_FR | 0.2500 | −1.0000 | 0 | CLOSED (85×) |
      227: 
    ... +9 more lines

### gate_T3-BATCH-S21C-GB-DEBUG6
- **name**: T3-BATCH-S21C-GB-DEBUG6
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: T3 prefix + BATCH tag + debug suffix are experimental batch markers, not substantive gate identifiers.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
       64:   # script: tier0-archive\s21c_gb_debug4.py
       65:   # script_sha: d272e7473ef0dc9339ff3db29250fbefd178bccd10e0476f161dc99729356257
       66:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
       67: T3-BATCH-S21C-GB-DEBUG5: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=19e6a7f9c69c6a25e6f351066f83886bde5a0d7fbc9b768e5a37b2c6add15c58
       68:   # script: tier0-archive\s21c_gb_debug5.py
       69:   # script_sha: 4325ea858a675e157aed6cade2e2a2990a5b740f969461eaf1fb71301c0a57ed
       70:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
       71:   # input: r20a_riemann_tensor.npz fc256a9b4791b1d6e1416f93cabbb0e28fe0c858bf2aeb04414b7767a7351fe9
    ... +8 more lines

### gate_T3-BATCH-S45-EULER-DEFICIT
- **name**: T3-BATCH-S45-EULER-DEFICIT
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: T3-BATCH prefix is batch hygiene label, not a real gate with session+wave+mechanism context.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
     6271: T3-BATCH-S45-DOS-FINE-SCAN: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=d9637cbc173a9a4e90a5350a9ffeadc66923cd5ae5b6dda95db5c44e3134ecdc
     6272:   # script: tier0-archive\s45_dos_fine_scan.py
     6273:   # script_sha: 26b5189f70058728aba06e6e7a812ea90c3d15412e87f4c176b7caa817579623
     6274:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6275: T3-BATCH-S45-ECOND-RECONCILE: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=b35a7a237c44f423fd86341c7954689a40306f3b76ee56c54de86b2c9f608897
     6276:   # script: tier0-archive\s45_econd_reconcile.py
     6277:   # script_sha: d6fadc398c6a18e3e8d0dd4608d19c734bf0a52381bafec57623bbfd292f4010
     6278:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +7 more lines

### gate_Higgs-sigma
- **name**: Higgs-sigma
- **source_file**: sessions\archive\session-23\session-23-sagan-verdict.md
- **Haiku NOISE reason**: Single-word category label without session-wave-mechanism context; bare mechanism name only.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      162: | 6 | D_K Pfaffian Z_2 | 17c D-2 | No sign change |
      163: | 7 | Perturbative fermion condensate | 19a S-4 | No attractive channel (perturbative) |
      164: | 8 | Single-field slow-roll | 19b R-1 | eta >> 1 everywhere |
      165: | 9 | Connes 8-cutoff positive spectral sums | 21a | All monotonic, AM-GM proof |
      166: | 10 | V''_total spinodal | 21a Landau | V'' > 0 everywhere |
      167: | 11 | S_signed(tau) gauge-threshold | 21c R2 | Monotonic, Delta_b < 0 algebraic (Trap 2) |
      168: | 12 | Coupled delta_T crossing (PB-3) | 22b | Block-diagonal exactly |
      169: | 13 | Coupled V_IR minimum (PB-2) | 22b | Block-diagonal exactly |
    ... +9 more lines

### gate_T3-BATCH-S21C-NEUTRINO-FINE-GRID
- **name**: T3-BATCH-S21C-NEUTRINO-FINE-GRID
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: T3 prefix + BATCH tag are experimental batch markers; mechanism name alone without session/wave structure.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
       79:   # script_sha: b6220f0b383b7b3cf8760348016550055d63cf999f33fc5f31a901c58eeb1cfe
       80:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
       81:   # input: r20a_riemann_tensor.npz fc256a9b4791b1d6e1416f93cabbb0e28fe0c858bf2aeb04414b7767a7351fe9
       82: T3-BATCH-S21C-KK-VERIFY: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=2a55a77db1238509f5bb41aac21116c504d3d5e7742aa2a25b9afcc37f1f85b8
       83:   # script: tier0-archive\s21c_kk_verify.py
       84:   # script_sha: 6fc82aeecf7f480a8b2db68d24c6d85ef32ef799dd45f51f24da347490eaebea
       85:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
       86:   # input: s19a_sweep_data.npz ad2a0da375f516aa24430db6630c733300428fa9682b0986a70b9b766aec1f5a
    ... +8 more lines

### gate_KC-1
- **name**: 7-10%
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **Haiku NOISE reason**: Single-letter + digit bare label; lacks session, wave, or mechanism context
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      346: | Pre-22 | 40% | — | Before traps discovered |
      347: | 22a | 46% | — | Pomeranchuk pass |
      348: | 22b | 38% | — | Block-diagonal theorem |
      349: | 22c | 44% | — | Perturbative Exhaustion |
      350: | 22d | 40% | 27% | Clock closure, DESI closed |
      351: | 23a | 6-10% | 4-8% | **Venus: K-1e fires** |
      352: | 24a | 5-7% | 2-3% | V-1 fires |
      353: | 24b | 5% (4-7%) | 3% (2-4%) | Combined BF = 0.31 |
    ... +9 more lines

### gate_T3-BATCH-S52-RICCI-FLOW
- **name**: T3-BATCH-S52-RICCI-FLOW
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: Domain-specific term without gate context or session+wave+mechanism structure.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
      739: T3-BATCH-S52-QM-DISPERSION: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=657bac4b3ec6050861331d41e24696b69a56e18a0166a49fd5650c874283fb38
      740:   # script: tier0-computation\s52_qm_dispersion.py
      741:   # script_sha: 4b4464b2e9cd93e131dc956e651944f90a7aa38f554478eba798f350978452ea
      742:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
      743: T3-BATCH-S52-QUICK-TEST: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=288eaf5e4f8004c0b8859ad1d7d2a6bcbd763f9d66d51ea3418533828c5098f4
      744:   # script: tier0-computation\s52_quick_test.py
      745:   # script_sha: c6bb835a385d7bcf658f97a3885a0d349966d8a01b27aa8e57d85f370062eed4
      746:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +7 more lines

### gate_T3-BATCH-S45-COLLECTIVE-NS-RPA
- **name**: T3-BATCH-S45-COLLECTIVE-NS-RPA
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: T3-BATCH prefix is batch hygiene label from tier0-archive, lacks session+wave+mechanism real gate structure.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
     6238:   # script_sha: 746ff666d4db394af63a531baba4e0426c5bfbc3c5f8b0837d5c7f76a85d749c
     6239:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6240: T3-BATCH-S45-COLLECTIVE-NS: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=7d60657aee768b3bca9401776a3c479c6794d924814009be4bcbf35d5b4f502a
     6241:   # script: tier0-archive\s45_collective_ns.py
     6242:   # script_sha: 902ce887203476c98ad378e9943dff109eb9ec0dc7a91d25951971bdca5240e5
     6243:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6244:   # input: s45_acoustic_ns.npz 2352c6170b82d5542b66d8ee80f135721dbdaeb04a78c0c2b502a119ad41de67
     6245:   # input: s38_cc_instanton.npz db1e7eb13a3c4fb1d03d790eae3d799942b7be3c59ff51c32e892e12e93e5a28
    ... +8 more lines

### gate_T3-BATCH-S64-GSL-ENTROPY
- **name**: T3-BATCH-S64-GSL-ENTROPY
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: Bare T3-BATCH label with S64 session reference; no substantive gate context (session/wave/mechanism).
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
     2781: T3-BATCH-S64-EPSILON-PROFILE: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=d1caea56b58a490a63bcea8d4a5beb860c2ac2d1bed5fcd56684f08f4104358e
     2782:   # script: tier0-computation\s64_epsilon_profile.py
     2783:   # script_sha: 394a73682b42639d0250f9697886365058cce69877003ddbe6832ee5be7cbcaf
     2784:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     2785: T3-BATCH-S64-FINITE-SIZE-VAC: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=75204bfc8672e6f5ab662bfa0d36fb6a251a4fd1bab1e94272dd2eded1574cd1
     2786:   # script: tier0-computation\s64_finite_size_vac.py
     2787:   # script_sha: 75b49e97ffff22686dcfbf21ba43c04d6e596d6221a176d93a0fc0772c6c8c0a
     2788:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +7 more lines

### gate_T3-BATCH-S52-HFB-FULL
- **name**: T3-BATCH-S52-HFB-FULL
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: Batch archive tag; no substantive gate identifier beyond mechanism name and batch marker.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
      675: T3-BATCH-S52-GL-JOSEPHSON: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=e8ac3cd92f3f3c61ff34addda8dfe454c20a26e813dfb77c246c6f36b42c91d9
      676:   # script: tier0-computation\s52_gl_josephson.py
      677:   # script_sha: f229de2272fbd478bf380b4063ebc0be512dad4644463bef80336d1c59c57e1f
      678:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
      679: T3-BATCH-S52-HAWKING-T-SWEEP: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=c76e9953d3c7e84eadd1c8b839ca6d9f0a600c7aa3cd9a639835451c8d8a1ce9
      680:   # script: tier0-computation\s52_hawking_t_sweep.py
      681:   # script_sha: d7065c35a71852ec855a2f4c722874ad75ec8f8d50ac506b950ee3325881daf1
      682:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +7 more lines

### gate_QA-1
- **name**: QA-1
- **source_file**: sessions\archive\session-22\session-22a-synthesis.md
- **Haiku NOISE reason**: Bare label QA-1; verdict-tag fragment without session+wave+mechanism structure.
- **Spot-check judgment**: **AGREE**  -  bare ID fragment (e.g. KC-2, L-1)
- **source_context (first 8 lines)**:
        8: ---
        9: 
       10: ## I. EXECUTIVE SUMMARY
       11: 
       12: Session 22a executed all ten pre-registered zero-cost computations from existing `.npz` data. The session produced two COMPELLING results, two INTERESTING results, one CLOSED, two NEUTRAL results, one STRUCTURAL r
       13: 
       14: **The central finding**: No single computation provides a decisive stabilization mechanism. However, three independent results converge on the same tau window and, taken together, constitute a coherent dynamical p
       15: 
    ... +4 more lines

### gate_T3-BATCH-S52-LIOUVILLIAN
- **name**: T3-BATCH-S52-LIOUVILLIAN
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: Batch migration record; verdict='MIGRATED' is a status marker, not a gate verdict; no substantive gate structure.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
      687: T3-BATCH-S52-INSPECT-DATA: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=aec25f4ffe89b6f1af2891cda500b0dc4ee598fb9b3bf46bae167b41531156ea
      688:   # script: tier0-computation\s52_inspect_data.py
      689:   # script_sha: c7021d7bbfa1294c42f9ec3567bc1d50c7cb6ec605fcaf59508b46d8d7844d94
      690:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
      691: T3-BATCH-S52-JACOBSON-MULTI-T: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=a46a99f0014ac29406bd4ae1df63fdd24de870dd4a8dcfe80cd2ace2135c7407
      692:   # script: tier0-computation\s52_jacobson_multi_t.py
      693:   # script_sha: 2e5a7bb526a3f76429627402df92232b67d8c80959994aea7045f5765bd50ca1
      694:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +7 more lines

### gate_T3-BATCH-S52-ETA-B
- **name**: T3-BATCH-S52-ETA-B
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: Batch tag with mechanism suffix; no session+wave+context structure of a real gate ID.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
      652: T3-BATCH-S52-CASIMIR-JOSEPHSON: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=745600cf964440080f45f70d78e52374815b27fdc07b8701e0afc798a9cf9470
      653:   # script: tier0-computation\s52_casimir_josephson.py
      654:   # script_sha: 7c568c6ba8dd6de459af667d91500635563b9c623199c0e8276f18ac08101fe8
      655:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
      656: T3-BATCH-S52-DDG-MKK: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=cbcfdb2830bdaf3ea5e4d5c47adda59cc54643d17c6a76556957fae37cd7b813
      657:   # script: tier0-computation\s52_ddg_mkk.py
      658:   # script_sha: 54f06786916622fb7434b3c82549bbfe77909b98d8b2a8f6fb4f37437b8d5d77
      659:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +7 more lines

### gate_SP-3
- **name**: SP-3
- **source_file**: sessions\archive\session-22\session-22a-synthesis.md
- **Haiku NOISE reason**: Bare label SP-3; round name without session+mechanism+gate-ID structure.
- **Spot-check judgment**: **AGREE**  -  bare ID fragment (e.g. KC-2, L-1)
- **source_context (first 8 lines)**:
        8: ---
        9: 
       10: ## I. EXECUTIVE SUMMARY
       11: 
       12: Session 22a executed all ten pre-registered zero-cost computations from existing `.npz` data. The session produced two COMPELLING results, two INTERESTING results, one CLOSED, two NEUTRAL results, one STRUCTURAL r
       13: 
       14: **The central finding**: No single computation provides a decisive stabilization mechanism. However, three independent results converge on the same tau window and, taken together, constitute a coherent dynamical p
       15: 
    ... +4 more lines

## Table: data_provenance  -  sampled 10 of 186 NOISE (5.4%)

### prov_775
- **name**: neff_read
- **source_file**: computations/session-59/s59_neff_read.py
- **Haiku NOISE reason**: Simple data-reading script with no outputs; reads from s59_neff_ba.npz but produces only side-effect text file, not gate output.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: import numpy as np
        2: d = np.load('computations/session-59/s59_neff_ba.npz', allow_pickle=True)
        3: f = open('computations/session-59/s59_neff_read.txt', 'w')
        4: for k in ['Delta_N_eff_conservative', 'Delta_N_eff_aggressive', 'g_BA_conservative',
        5:            'g_BA_aggressive', 'gate_verdict', 'gate_detail', 'dilution_factor_CMB',
        6:            'rho_1nu_over_rho_gamma', 'F_BA', 'E_matter_Volovik', 'M_KK',
        7:            'g_star_Shattering', 'g_star_S_post_ee', 'g_star_S_Shattering',
        8:            'N_eff_Planck_2018', 'sigma_N_eff_Planck_2018', 'n_BA_modes']:
    ... +3 more lines

### prov_2076
- **name**: w5_falsifier_inventory_consolidation_writer
- **source_file**: computations/session-87/s87_w5_falsifier_inventory_consolidation_writer.py
- **Haiku NOISE reason**: Empty outputs field; script is documentation/commentary on carry-forward structure with no computational output.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      198: 1. **What**: register §VII.AM candidate cross-pillar bridge entry with all 5 anatomy + 3-level declarations + binomial(2,2)=1 cross-cocycle ratio (canonical 7.324992); land at registry once Lancaster MCT-3 + Aalto
      199: 2. **Inputs**: Lancaster MCT-3 vortex-core spectroscopy data (~2027-2030 horizon, Pickett group); Aalto LTL µSR data (~2027 horizon, Krusius/Tuoriniemi/Eltsov); W5-2+W5-3 Rows #47-#54b + their substrate-derived pr
      200: 3. **Gate criterion**: PASS iff both lab ratios in [7.3177, 7.3323] AND |r_A − r_B| < 0.1% (cross-platform substrate-resident-ness confirmation); INFO if one ratio in band but not both; FAIL if either ratio outsid
      201: 4. **Effort**: 0.5 wave-equivalents (~2-4h) for the registry-write + falsifier-row append + Stage-1-CANDIDATE tagging once both lab datasets land; the lab-execution cycle itself is multi-year (2027-2030+ horizon).
      202: 
      203: 
      204: ## Section closure — S87 W5 consolidation (S-5 workshop output)
      205: 
    ... +2 more lines

### prov_9
- **name**: w1_deferred_pending_audit_test
- **source_file**: computations/_shared/s90_w1_deferred_pending_audit_test.py
- **Haiku NOISE reason**: Self-test driver for deferred-pending audit detection with synthetic fixtures, not real physics computation; empty outputs indicates test harness only.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: #!/usr/bin/env python3
        2: """S90 W1-14 — Self-test driver for `detect_deferred_pending_sub_class()`.
        3: 
        4: Per `sessions/session-plan/session-90-plan-w1.md` §W1-14 #6 output files:
        5:     `computations/_shared/s90_w1_deferred_pending_audit_test.py`
        6:     (self-test against §VII.AV + §VII.AU as positive instances after CF-63
        7:     W6 lands them).
        8: 
    ... +5 more lines

### prov_779
- **name**: npz_probe
- **source_file**: computations/session-59/s59_npz_probe.py
- **Haiku NOISE reason**: Probe/inspection utility with text-only output; generic data dumper without gate computation semantics.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
       12:         v = d[k]
       13:         if v.ndim == 0:
       14:             lines.append(f'  {k}: scalar = {v.item()}')
       15:         elif v.size < 30:
       16:             lines.append(f'  {k}: shape={v.shape}, dtype={v.dtype}, values={v}')
       17:         else:
       18:             lines.append(f'  {k}: shape={v.shape}, dtype={v.dtype}, min={v.min():.6e}, max={v.max():.6e}')
       19: 
    ... +2 more lines

### prov_7
- **name**: w1_17_vii_ah_stage_2_orthogonality_k2_rule_update
- **source_file**: computations/_shared/s90_w1_17_vii_ah_stage_2_orthogonality_k2_rule_update.py
- **Haiku NOISE reason**: Shared substrate-input-orthogonality K-counter update script for rule-file landing, not data generation; empty outputs indicates methodology verification only.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    <name 'w1_17_vii_ah_stage_2_orthogonality_k2_rule_update' not found in source>
    --- file head ---
        1: #!/usr/bin/env python3
        2: """S90 W1-17 — §VII.AH Stage-2 substrate-input-orthogonality K-counter K=1 → K=2 rule update.
        3: 
        4: Per `sessions/session-plan/session-90-plan-w1.md` §W1-17 (CF-17 / CF-W4-7-ORTHOGONALITY-K2).
        5: 
        6: This script performs the artifact-existence verification + [VERIFY] structural-
    ... +24 more lines

### prov_1214
- **name**: chirp_penumbra
- **source_file**: computations/session-70/s70_chirp_penumbra.py
- **Haiku NOISE reason**: session-70 does not exist in computations directory; no substantive script path
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      644:     print(f"    {n_multi} modes show multiple crossings (possible parametric resonance).")
      645: else:
      646:     print(f"    No multiple crossings => single-pass chirp, no parametric resonance.")
      647: 
      648: # ============================================================================
      649: #  SECTION 10: Save data
      650: # ============================================================================
      651: 
    ... +9 more lines

### prov_651
- **name**: conformal_diagram
- **source_file**: computations/session-55/s55_conformal_diagram.py
- **Haiku NOISE reason**: Script path references session-55 but file context shows incomplete path documentation from archived session.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        6: tests particle horizon existence, SEC violation, and discrete trapped surfaces
        7: on the 32-cell graph.
        8: 
        9: Input:
       10:   computations/session-54/s54_connes_latt.npz  (distance_matrix, adjacency, mean_distance)
       11:   computations/session-54/s54_scale_factor.npz (tau, a, H, q)
       12: 
       13: Output:
    ... +9 more lines

### prov_658
- **name**: euclid_continuum
- **source_file**: computations/session-55/s55_euclid_continuum.py
- **Haiku NOISE reason**: Script path references multiple session inputs (s44, s27, s54) but file context shows docstring only without computation or verdict.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: #!/usr/bin/env python3
        2: """
        3: s55_euclid_continuum.py — EUCLID-CONTINUUM-55: Euclidean Free Energy on 992-Mode Continuum
        4: 
        5: Repeats the EUCLID-55 computation (which PASSED on the 32-cell lattice with tau_min=0.220,
        6: 30% barrier) on the full 992-mode continuum spectrum from the Dirac operator on SU(3).
        7: 
        8: Physical content:
    ... +3 more lines

### prov_159
- **name**: rge_running_legacy
- **source_file**: computations/session-30/s30b_rge_running_legacy.py
- **Haiku NOISE reason**: Legacy variant with mismatched docstring (says s30b_rge_running.py) and no actual substantive distinction from prov_158.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    <name 'rge_running_legacy' not found in source>
    --- file head ---
        1: #!/usr/bin/env python3
        2: """
        3: s30b_rge_running.py — RGE Running + NCG-KK Tension Analysis
        4: ============================================================
        5: 
        6: Session 30Bb Step 4: Take g1/g2 from the grid data at the SM Weinberg contour
    ... +24 more lines

### prov_440
- **name**: fwd_bwd_ns
- **source_file**: computations/session-46/s46_fwd_bwd_ns.py
- **Haiku NOISE reason**: Session 46 does not exist in framework; Kibble-Zurek universality is external physics reference, not framework gate computation.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
       67:     E_B1, E_B2_mean, E_B3_mean,
       68: )
       69: 
       70: import matplotlib
       71: matplotlib.use('Agg')
       72: import matplotlib.pyplot as plt
       73: 
       74: DATA_DIR = Path(__file__).parent
    ... +9 more lines

## Table: session_files  -  sampled 4 of 4 NOISE (100.0%)

### sf_63:session-63-W7-workingpaper.md
- **name**: session-63-W7-workingpaper.md
- **source_file**: sessions/session-63/session-63-W7-workingpaper.md
- **Haiku NOISE reason**: Wave 7 template stub (10 KB) with agent instructions but no completed gate entries—only section header and 'NOT STARTED' status.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    <name 'session-63-W7-workingpaper.md' not found in source>
    --- file head ---
        1: # Session 63 Wave 7 Working Paper
        2: 
        3: **Date**: 2026-03-30
        4: **Session**: S63 — Folding CC
        5: **Format**: Parallel single-agent computations across 7 waves
        6: **Plan**: `sessions/session-plan/session-63-plan.md`
    ... +24 more lines

### sf_66:session-66-wrapup.md
- **name**: session-66-wrapup.md
- **source_file**: sessions/session-66/session-66-wrapup.md
- **Haiku NOISE reason**: Stub file with 'to be filled' placeholder; only header and computation listing without substantive content.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    <name 'session-66-wrapup.md' not found in source>
    --- file head ---
        1: # Session 66 Wrapup: Spectral Ops. Engagement
        2: 
        3: **Date**: 2026-04-04
        4: **Session**: 66
        5: **Format**: 8-wave parallel computation (37 tasks) + 10 collab reviews + 5 workshops + inflation deep dive + Bellazzini analysis
        6: **Planner**: lizzi-spectral-functional-theorist
    ... +24 more lines

### sf_sessions/framework/registry/_registry-template.md
- **name**: _registry-template.md
- **source_file**: sessions/framework/registry/_registry-template.md
- **Haiku NOISE reason**: Template file with placeholder content and instruction comments, not a substantive registry entry; belongs in framework/Templates, not framework/registry.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    <name '_registry-template.md' not found in source>
    --- file head ---
        1: ---
        2: type: registry-template
        3: ingested-by: /weave --update
        4: ---
        5: 
        6: # &lt;Registry Name&gt;
    ... +24 more lines

### sf_sessions/session-plan/archive/session-29Aa-prompt.md
- **name**: session-29Aa-prompt.md
- **source_file**: sessions/session-plan/archive/session-29Aa-prompt.md
- **Haiku NOISE reason**: Path fragment is malformed (missing session number in anchor_id; says session='' in JSON), reads as session-29Aa-prompt.md but labeled with sessions/ prefix fragment.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    <name 'session-29Aa-prompt.md' not found in source>
    --- file head ---
        1: # Session 29Aa: KC-3 Closure + Entropy Balance
        2: 
        3: **Date**: 2026-02-28
        4: **Author**: Hawking (hawking-theorist), dissected by team-lead
        5: **Depends on**: Session 28 (all sub-sessions: 28a KC-1 PASS, 28b self-consistent tau-T, 28c phonon T-matrix + van Hove BCS + Luttinger + steady-state mu)
        6: **Input data**:
    ... +24 more lines

## Table: equations  -  sampled 8 of 144 NOISE (5.6%)

### eq_19972
- **name**: scheme=stage-2-cross-axis-3-reviewer-axis-a-pillar-1-ncg-axiomatic \
- **source_file**: sessions\session-plan\session-91-plan-w8.md
- **Haiku NOISE reason**: Plan-block convention/scheme tag (backslash-escaped, line-continuation syntax); not mathematical equation.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no obvious sub-clause / table-row marker
- **source_context (first 8 lines)**:
     3023:     PASS|INFO|FAIL -- \
     3024:     value='axis_a=van-den-dungen-bridge-theorist;clauses_A1_A2_pass=N;\
     3025:     joint_hypersurface_iii_admissibility_pillar_1_PASS=True;\
     3026:     kunneth_morita_triviality_structural_theorem_verification_PASS=True;\
     3027:     pillar_1_ncg_axiomatic_framing_preserved=True;\
     3028:     substrate_input_orthogonality_axis_a_loads_pillar_1_data=True;\
     3029:     OAA_exclusion_PASS=connes_lizzi_volovik_excluded;\
     3030:     procedural_floor_PASS=w4_transcripts_not_consumed' \
    ... +9 more lines

### eq_18596
- **name**: chi_A_volovik_2003             = 1.500000              [canonical_constants; 3He-A susceptibility]
- **source_file**: sessions\session-plan\archive\session-88-plan-w4c.md
- **Haiku NOISE reason**: Named constant assignment from canonical_constants with annotation, not a mathematical relation.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no obvious sub-clause / table-row marker
- **source_context (first 8 lines)**:
      898: substrate_cocycle_ratio_67_88  = 7.324992              [canonical_constants; Sage-exact]
      899: delta_B_over_delta_A_q_theory  = 0.96528               [canonical_constants; q-theory]
      900: P_pc                           = 21.22 bar             [canonical_constants; polycritical anchor]
      901: T_pc                           = 2.273e-3 K            [canonical_constants; polycritical anchor]
      902: delta_A_over_kBTc              = 2.0302                [canonical_constants]
      903: delta_B_over_kBTc              = 1.9597                [canonical_constants]
      904: SC_corr_A                      = 1.151                 [canonical_constants; strong-coupling A]
      905: SC_corr_B                      = 1.111                 [canonical_constants; strong-coupling B]
    ... +9 more lines

### eq_7325
- **name**: N_C = 1/(1+N_B²) is NOT an emergent algebraic relation between two independent
- **source_file**: sessions\session-86\workshops\s86-fnl-folded-pathway-adjudication.md
- **Haiku NOISE reason**: Prose statement embedded as equation name, not mathematical expression.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no obvious sub-clause / table-row marker
- **source_context (first 8 lines)**:
     1070: Step 3 [substitution, identity-test under canonical definition]:
     1071:   1/(1 + N_B^{canonical}^2)
     1072:     = 1/(1 + 1/N_pair_eff)                                  -- substitute N_B definition
     1073:     = N_pair_eff / (1 + N_pair_eff)                          -- algebraic simplification
     1074:     = N_C^{canonical}                                        -- match by definition
     1075: 
     1076: Step 4 [direction]: under the canonical definitions used by s67 and s85, both N_B and
     1077:   N_C are scalar FUNCTIONS of the SAME aggregate quantity N_pair_eff. The identity
    ... +9 more lines

### eq_3790
- **name**: R(0)  = 4.0000000000
- **source_file**: computations\session-59\s59_ricci_dw_results.txt
- **Haiku NOISE reason**: Numerical result output (Ricci scalar R(0) = 4.0) from gate execution, not a formula or equation.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no obvious sub-clause / table-row marker
- **source_context (first 8 lines)**:
       11: gate_name    = RICCI-DW-59
       12: gate_verdict = INFO
       13: gate_detail  = E_DW=0 at tau=0.1135. A_crit=0.673063. sec_min(DW)=-0.000000. sec_min>0 throughout. Margin sign: -1 throughout. Partial correspondence only.
       14: 
       15: === Ricci components at tau=0 (validation) ===
       16: r1(0) = 0.5000000000
       17: r2(0) = 0.5000000000
       18: r3(0) = 0.5000000000
    ... +9 more lines

### eq_20639
- **name**: D_can slightly more repulsive (Delta_q = +0.075)
- **source_file**: computations\session-28\s28a_gate_verdicts.txt
- **Haiku NOISE reason**: Summary prose statement of numerical result, not symbolic equation
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no obvious sub-clause / table-row marker
- **source_context (first 8 lines)**:
       21: C-1   Spectral Action S_can vs S_LC               CLOSED
       22:   S_can(tau) monotonically DECREASING under all smooth cutoffs
       23:   S_LC(tau) monotonically DECREASING under all smooth cutoffs
       24:   V-1 transfers to torsionful sector: connection-independent
       25:   Spectral action stabilization via torsion CLOSED
       26: 
       27: C-4   Spectral Correlation R_2(s)                  DIAGNOSTIC (WEAK)
       28:   Brody q: D_can = 0.28+/-0.23, D_K = 0.16+/-0.24
    ... +9 more lines

### eq_9821
- **name**: T^{(3)} = T^{(3)}_{[abc]}
- **source_file**: sessions\session-plan\archive\session-26-preplan-3_2.md
- **Haiku NOISE reason**: Symbolic notation T^{(3)} = T^{(3)}_{[abc]} in prose context about torsion; not a functional equation.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no obvious sub-clause / table-row marker
- **source_context (first 8 lines)**:
      433: The physically relevant question from the preplan is different from comparing $\not{D}_K$ and $\not{D}_0$. It is: **does the Levi-Civita Dirac operator on a Lie group with deformed metric have eigenvalues that cou
      434: 
      435: The standard Dirac operator $\not{D}_K$ already uses the Levi-Civita connection, which is torsion-free. The Lichnerowicz bound $\lambda^2 \geq R_K/4$ applies to this operator. The question is whether a torsionful 
      436: 
      437: The answer depends on what "physically motivated" means:
      438: 
      439: 1. **If we use the Schouten connection**: Zero eigenvalue on singlet. The gap is destroyed. This is physically the wrong operator for mass generation -- the zero modes don't produce masses.
      440: 
    ... +4 more lines

### eq_19561
- **name**: pole s=4. Expected band: NO-ACTION or ADVISORY (SCHEMATIC and FULL-physical
- **source_file**: sessions\session-plan\session-90-plan-w8.md
- **Haiku NOISE reason**: Fragmented plan-document prose describing a classification category, not a mathematical equation.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no obvious sub-clause / table-row marker
- **source_context (first 8 lines)**:
     2017: Reconciliation"` 4-band calibration (NO-ACTION / ADVISORY / MANDATORY /
     2018: HARD-HALT).
     2019: 
     2020: ### Classification
     2021: META (D_max measurement methodology + W3 A.14 cross-wave npz consumption).
     2022: The D_max IS the structural distance between the SCHEMATIC level-pin output
     2023: (SCHEMATIC tier from `_spectral_action_regulators.py`) and the FULL physical
     2024: level-pin output (full PV pipeline at Λ_UV = M_KK) at the substrate-distance-2
    ... +9 more lines

### eq_22473
- **name**: s_cm2 = float(np.sum(c_arr * m_arr * m_arr))
- **source_file**: computations\_pauli_villars_subtraction.py
- **Haiku NOISE reason**: NumPy reduction (s_cm2 = float(np.sum(...))) from verification function, not mathematical formula.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no obvious sub-clause / table-row marker
- **source_context (first 8 lines)**:
       86: PV_PRIMARY_C = np.array([+2.0, -1.0], dtype=np.float64)
       87: PV_PRIMARY_M_DIMLESS = np.array([1.0, np.sqrt(2.0)], dtype=np.float64)
       88: # (dimensionless: when λ_k is in M_KK units, m_r is dimensionless mass ratio)
       89: 
       90: 
       91: def _verify_pv_identities(c_arr=PV_PRIMARY_C, m_arr=PV_PRIMARY_M_DIMLESS):
       92:     """Verify Σ c_r = 1 and Σ c_r m_r² = 0 to machine precision."""
       93:     s_c = float(np.sum(c_arr))
    ... +9 more lines

## Table: researchers  -  sampled 2 of 2 NOISE (100.0%)

### researcher_Lost-Treasures
- **name**: Lost-Treasures
- **source_file**: researchers/Lost-Treasures/index.md
- **Haiku NOISE reason**: Source file not found and paper count is zero; empty or deleted stub folder.
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
    <source file not found: researchers\Lost-Treasures\index.md>

### researcher_RF-Antimatter
- **name**: RF-Antimatter
- **source_file**: researchers/RF-Antimatter/index.md
- **Haiku NOISE reason**: Index file not found; folder contains only 1 paper with empty description (missing metadata).
- **Spot-check judgment**: **BORDERLINE**  -  short section-heading-like name; insufficient context to judge
- **source_context (first 8 lines)**:
    <source file not found: researchers\RF-Antimatter\index.md>

## Table: constants  -  sampled 2 of 2 NOISE (100.0%)

### const_Vol_SU3_WRONG
- **name**: Vol_SU3_WRONG
- **source_file**: computations/_shared/canonical_constants.py
- **Haiku NOISE reason**: Deprecated constant marked DO NOT USE; explicitly flagged as wrong incorrect value kept only for audit trail.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
      303: # Residual (closed-form vs L=14 measured): |delta_A| = 5.23e-5, |delta_B| = 2.62e-5
      304: # under "10/(1 - tau/(5*pi))" form; |delta_A| = 3.44e-5, |delta_B| = 1.72e-5 under
      305: # the 2nd-truncation form "10*(1 + tau/(5*pi) + (tau/(5*pi))^2)". Both well within
      306: # the W1b-HK-5 PASS threshold 1e-3.
      307: 
      308: # SU(3) Haar volume — the CORRECT Weyl integration formula
      309: # S44 CORRECTION: 8*sqrt(3)*pi^4 = 1349.74 (replaces wrong sqrt(3)*(4*pi^2)^3/12 = 8880.93)
      310: Vol_SU3_Haar = 8.0 * np.sqrt(3) * PI**4   # = 1349.74 (S44 s44_constants_corrected)
    ... +9 more lines

### const_lambda_unit_canonical
- **name**: lambda_unit_canonical
- **source_file**: computations/_shared/canonical_constants.py
- **Haiku NOISE reason**: Value is string literal 'dimensionless_M_KK_natural' (not numerical); placeholder-form constant for unit labeling rather than physics value.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      555: V2_weight_FW_sum = 23  # Schur-projected real-dim functional on A_F, sum across all 3 blocks = 1+4+18 = 23 = real_dim(A_F). Canonical Connes-Marcolli 2008 Thm 11.1; A_F = C+H+M_3(C) Connes-Chamseddine canonical em
      556: a_0_FW_zeta = 6440.0  # zeta-regulated zeroth Seeley-DeWitt coefficient of D_K^2 at tau_fold; substrate dimensionless mode count (a_0 = zeta_{D_K}(0) = Tr(1)) per CCM 2007 + S64 / S77 R-protection; W11-124 canonic
      557: a_2_FW_zeta = 2776.165389  # zeta-regulated second Seeley-DeWitt coefficient of D_K^2 at tau_fold; spectral-zeta sum a_2(spectral, S42) = 2776.165389; S46 a_2 split = a_2^zeta / a_2^SD = 2776.165389 / 0.7282349726
      558: xi_KZ_FW = 0.018760052113614717  # Substrate-natural xi_KZ derived from atlas T1 dt/T_L=1.25e-5 + Bogoliubov-unitary BdG-A_2 (nu=1/2, z=1, m=1/3) + S53 xi_BCS-analog 0.808346 M_KK^-1. M_KK^-1 units. Closes S88 W-2
      559: kappa_2_substrate_FW = 0.021018084987437196  # CM-1995 §III.4 second-order Jensen perturbation on HK-5 closed form 5/(1-tau/(5*pi)); kappa_2 = 1/(5*pi^2 * A^3) with A = 1 - tau_fold/(5*pi) at tau_fold = 0.19. Subs
      560: t
    ... [truncated]

## Table: registries  -  sampled 4 of 4 NOISE (100.0%)

### registry_Phononic-Crystal-Geometry
- **name**: Phononic Crystal Geometry of SU(3)
- **source_file**: sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md
- **Haiku NOISE reason**: Archived registry (superseded by Phononic-Substrate-Geometry); marked ARCHIVED per container-thinking reframe.
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
        1: ---
        2: ARCHIVED: 2026-05-10
        3: Last meaningful session: S41 (Fabric Discovery; superseded mid-S86)
        4: Superseded by: sessions/framework/Phononic-Substrate-Geometry.md
        5: Reason: Phononic-Crystal-Geometry framing replaced by Phononic-Substrate-Geometry framing post-S86 (substrate IS the spectral triple, not a crystal IN a container); per phononic-framing.md IS-not-IN substrate-dire
        6: ---
        7: 
        8: # Phononic Crystal Geometry of SU(3)
    ... +8 more lines

### registry__registry-template
- **name**: &lt;Registry Name&gt;
- **source_file**: sessions/framework/registry/_registry-template.md
- **Haiku NOISE reason**: Template stub file with placeholder text, not a substantive registry entry.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: ---
        2: type: registry-template
        3: ingested-by: /weave --update
        4: ---
        5: 
        6: # &lt;Registry Name&gt;
        7: 
        8: > **This is a template.** Copy to `sessions/framework/<slug>.md`, replace every `<...>` placeholder, delete this blockquote. `/weave --update` will ingest the resulting file into `tools/knowledge.db`.
    ... +6 more lines

### registry_framework-bbn-hypothesis
- **name**: Framework BBN Hypothesis: Scale-Dependent Tau and the Phonon Cascade
- **source_file**: sessions/framework/ARCHIVE/framework-bbn-hypothesis.md
- **Haiku NOISE reason**: Archived file with SUPERSEDED status marker; conceptual hypothesis without computational closure.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: ---
        2: ARCHIVED: 2026-05-10
        3: Last meaningful session: S36
        4: Superseded by: sessions/framework/framework-parametric-amplification.md + sessions/framework/Phononic-to-Cosmos.md
        5: Reason: BBN hypothesis from S36 transit-dynamics era; superseded by parametric-amplification framework + cosmological mapping; modern accounting at atlas-07 §VII registry slots
        6: ---
        7: 
        8: # Framework BBN Hypothesis: Scale-Dependent Tau and the Phonon Cascade
    ... +8 more lines

### registry_lrd-observational-constraints
- **name**: LRD Observational Constraints Registry
- **source_file**: sessions/framework/registry/lrd-observational-constraints.md
- **Haiku NOISE reason**: Stub registry with minimal content (3 lines of header only, truncated at line 9).
- **Spot-check judgment**: **BORDERLINE**  -  short title; context contains theorem markers OR table
- **source_context (first 8 lines)**:
        1: # LRD Observational Constraints Registry
        2: 
        3: **Registry ID**: `lrd-observational-constraints`
        4: **Owner agent(s)**: `little-red-dots-jwst-analyst`
        5: **Last updated**: `2026-04-23, S85-W4 AMRI migration`
        6: **Ingestion**: `/weave --update`; `knowledge.db` stores rows under `closed | open` per entry status.
        7: 
        8: ---
    ... +1 more lines
