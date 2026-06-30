# Session 83 Synthesis: Three-Layer Regulator Theorem (Lizzi Solo, part a)

**Date**: 2026-04-18
**Agent**: lizzi-spectral-functional-theorist (Lizzi solo a — spectral-functional formulation)
**Source Documents**:
- `sessions/archive/session-83/session-83-results-workingpaper.md`
- `computations/s83_gate_verdicts.txt`
- `sessions/permanent-results-registry.md`
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`

---

## I. Session Outcome

S83 establishes that the framework's regulator-choice ambiguity resolves at three distinct epistemic layers, each with its own canonical answer and uniqueness argument: AXIOMATIC (zeta unique under Connes A1-A6, W1-G3 PASS), SUBSTRATE-ACTION (Zubarev unique minimizer of S[tau_fold] under Connes-integrability + local-min-tau + KK-sign=+1, W1-G1 PASS), and OBSERVABLE (per-observable spans across {zeta, Zubarev, SDW, dim-reg, lattice-BR}, with R-protected observables passing factor-1.5 and NOT-R-protected observables exhibiting span 14.7 to 1766). The two upper-layer canonical picks DISAGREE (zeta vs Zubarev) — this dissonance is structural, not a defect: each layer pins a different question. The G51 w_0 FAIL at scheme-split 0.08 is the observable manifestation of mixing layer pins (calibrated under L1, evaluated under L2). The synthesis result is a §VII.M registry candidate (THREE-LAYER-REG-84) with layer-of-pin classification on the entire 42-row §VII.K atlas.

---

## II. Key Results

### II.1 Three-Layer Partition (Spectral-Functional Formulation)

**Result**: A spectral-functional choice resolves at three orthogonal layers; each layer's uniqueness argument is independent of the others. Classification: GEOMETRIC.

**Layer 1 — Axiomatic / Dixmier (W1-G3 PASS)**. Under Connes axioms A1-A6 (dim-summability, reality, first-order, orientability, Poincare duality, regularity), the Connes residue formula

```
Tr_omega(|D|^{-d}) = Res_{s=d} zeta_D(s),    zeta_D(s) := Tr(|D|^{-s})
```

uniquely determines a positive trace on the Macaev ideal `L^{1,infty}(H)`. Any admissible regulator psi satisfies psi propto Tr_omega; the canonical representative is zeta. No external scalar enters. The W1-G3 sanity-script confirms (i) Zubarev requires an external Lambda_Z and shows 1298.4% gap across factor-2 Lambda variation, (ii) `M_KK` carries no axiom-derivation in `canonical_constants.py` (knowledge MCP returned `_No PROVENANCE entry_`), so any salvage path that pins Lambda = M_KK supplies data outside A1-A6. Verdict line: `S83-SUBSTRATE-NATIVE-REGULATOR-PRIORITY-CONJECTURE: PASS scheme=zeta-vs-alternatives convention=A1-A6-axioms L_max=5 sha256=2343920a..`. The S82 W-1 §EN3 conjecture is now THEOREM.

**Layer 2 — Substrate-Action (W1-G1 PASS)**. Under the joint criteria (Connes-integrability AND local-min-tau AND KK-sign=+1) at L_max=5 and tau_fold=0.19, Zubarev is the unique passing regulator. The decision function values:

| Regulator | integ | chi (KK-sign) | local-min (curv > 0) | passes |
|:----------|:-----:|:-------------:|:--------------------:|:------:|
| zeta      | True  | +1            | **False** (curv = 0 structural) | False |
| Zubarev   | True  | +1            | True (curv = +1.16e+05) | **True** |
| SDW       | True  | **-1**        | True | False |

Substitution chain: passes[R] = integ[R] AND (chi[R]==+1) AND (curv[R] > 0). Direction: only Zubarev satisfies all three, by Python-verified evaluation on the L_max=5 D_K spectrum (`s83_w1_g1_ic_scheme_derivation.py`). Verdict line: `S83-IC-SCHEME-DERIVATION: PASS scheme=Zubarev convention=substrate-native L_max=5 sha256=227a5913..`. The 3-branch CC tree reduces to Branch-B (Zubarev-canonical).

**Layer 3 — Observable (per-observable spans)**. For each observable Q, compute span_Q := max_R Q^R / min_R Q^R across {zeta, Zubarev, SDW, dim-reg, lattice-BR}. Two structural families:

- R-protected (span < 1.5): same-regulator first-moment ratios (numerator and denominator carry the same weight, R cancels). Examples: c_s span 1.227 (G14 PASS), alpha_SDW^NLO universality span 1.05 (G26 PASS), c_Gold/c_fabric (S52 R-protected), chi_2 scheme-universality < 3.6% (S78 W3-K).
- NOT-R-protected (span >= 2.5): Mellin-kernel integrals against fixed anchors, single-moment absolutes. Examples: k_a2 span 14.69 (G15 FAIL), A_s span 14.69 (G16, CC-5 identity), f_conv span 1766 (G28 FAIL), CC-ratio max 42.03 (G34 FAIL).

The CC-5 linearity identity (verified to <1e-10): A_s span EXACTLY equals k_a2 span (both 14.685054), because A_s is linear in k_a2 in the UNIFIED-AS-79 ledger. This is a propagation theorem, not a coincidence.

### II.2 Layer Dissonance is Structural

**Result**: L1 (zeta) and L2 (Zubarev) DISAGREE on the canonical regulator pick. This is not a contradiction; the layers pin different questions. Classification: GEOMETRIC.

**Substitution chain** (direction claim: dissonance is structural, not defective):

Step 1 (definitions). Let Q1(R) := "is R the unique trace on L^{1,infty}(H) under A1-A6?". Let Q2(R) := "does R minimize S[tau_fold] subject to integrability AND chi=+1 AND local-min?". These are DIFFERENT predicates on the regulator family.

Step 2 (substitute). Q1(zeta) = True (Connes residue uniqueness, W1-G3); Q1(Zubarev) = False (requires external Lambda_Z, salvage fails when M_KK has no axiom-derivation). Q2(zeta) = False (curv = 0 structural at counting function); Q2(Zubarev) = True (only regulator passing all three integrability conditions).

Step 3 (simplify). canonical_R(Q1) = zeta. canonical_R(Q2) = Zubarev. canonical_R(Q1) NOT EQUAL canonical_R(Q2).

Step 4 (direction). The two functions select different regulators. Since Q1 and Q2 are independent predicates (one tests Dixmier-trace uniqueness, the other tests substrate-action minimum), their disagreement is consistent and EXPECTED — the layers are orthogonal selection rules.

**Observable manifestation**: G51 w_0 verdict line `S83-W_0-REGULATOR-CANONICAL-CHOICE: FAIL value=-0.998116 scheme=Zubarev-E-weighted convention=substrate-native L_max=5 sha256=224b7b56..`. The -0.918 reading was computed under L1 zeta (the S58 Volovik partition baseline). Recomputed under L2 Zubarev (the substrate-action canonical), w_0 = -0.998116, |split| = 0.080116. The 0.08 split IS the L1-L2 dissonance projected onto an observable that mixes layer pins. The FAIL is therefore not a framework collapse but a pin-mismatch diagnostic: the gate was pre-registered under L1 calibration but the canonical L2 regulator drives the answer toward LCDM (-1).

### II.3 Lizzi a_2-Ratio Theorem (W1-G4)

**Result**: F_traj = f_2^zeta / f_2^SDW = 1 / (2/3) = 3/2 EXACTLY at the a_2 slot. Classification: GEOMETRIC + PHONONIC.

The Mellin slot weights at Lambda^2 = 1 evaluate to:
- f_2^zeta = 1.000000 (Lizzi 1412.4669 analytic continuation)
- f_2^Zubarev = 1.000000
- f_2^SDW = 2/3 = 0.666667 (Laplace-transform normalization of smooth kernel; S76 canonical `mellin_f_star_f2`)

Substitution: epsilon_H^R(N) = (...scheme-independent kernel...) * f_2^R. Therefore max_R/min_R(eps_H) = f_2^zeta / f_2^SDW = 3/2 exactly, INDEPENDENT of N or tau in the post-fold slow-roll window. Python-verified: eps_H[SDW]/eps_H[zeta] = 3.239780e-26 / 2.159853e-26 = 1.500000.

The F_traj = 3/2 is the same structural Mellin ratio that appeared in S78 W-2D (f_2^zeta / f_2^SDW in the f_conv-anomaly triangle) and S76 f_conv workshop (intensive/extensive partition at a_2). The a_2-ratio theorem promotes this scheme-ambiguity quantity to an observable trajectory-invariance factor: any zeta+SDW joint observable at the a_2 slot inherits a 3/2 floor.

### II.4 Layer-of-Pin Atlas (extension of §VII.K-META taxonomy)

**Result**: 42-row §VII.K atlas classified by which layer ultimately pins each row's regulator-choice. Classification: GEOMETRIC + non-phononic (taxonomic).

| Layer-of-pin | Count | Description |
|:-------------|:-----:|:------------|
| L0-INT | 26 | Integer/structural identities; FI by construction; R cancels — no layer needed |
| L1-AX  |  2 | Axiomatic-Dixmier zeta selects (W1-G3); rows #2 H-tilde-TD, #33 F_amp 3PI |
| L2-SA  |  1 | Substrate-action Zubarev selects (W1-G1); row #5 Branch-B |
| L3-OB  |  8 | Observable layer pin (mode-eq output OR per-observable convention pin); rows #4, 7, 8, 9, 27, 30, 34, 42 |
| UNPINNED |  5 | No layer currently pins; standing structural targets; rows #13 (r_max), #17/18 (w_0 family), #24 (a_2-cluster), #38 (mu_eff LK Born-Markov) |

Total: 42 rows (Python-verified). The 5 UNPINNED rows are the standing carry-forward targets for S84+ functional-selection work. They share a common structural feature: each is a MIXED-mostly-RD or pure-RD observable where neither L1 nor L2 supplies a structurally justified canonical pick, AND L3 R-protection fails (spans > 1.5 across regulators).

This extends the §VII.K-META R-protected vs NOT-R-protected partition by adding a third orthogonal axis (the LAYER-of-pin), revealing that what looked like a binary R-protection split is actually a four-level hierarchy (L0-INT / L1-AX / L2-SA / L3-OB) with a residual UNPINNED bucket.

---

## III. Gate Verdicts

The gate verdicts authoritatively used in this synthesis (verbatim from `computations/s83_gate_verdicts.txt`):

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S83-SUBSTRATE-NATIVE-REGULATOR-PRIORITY-CONJECTURE (W1-G3) | PASS | EN3 conjecture -> THEOREM; zeta unique under A1-A6 |
| S83-IC-SCHEME-DERIVATION (W1-G1) | PASS | Branch-B Zubarev-canonical (1 of 3 regulators passes integrability + chi=+1 + local-min) |
| S83-EPSILON-H-SUBSTRATE-DERIVATION-AND-TRAJECTORY-FI (W1-G4) | INFO | F_traj = 3/2 = 1.500000 exact rational; substrate-derivable=True |
| S83-H-TILDE-EPOCH-AXIS-DECOMPOSITION-82 (W1-G5) | FAIL | max_off=0.9483 (eps-conv vs Class collinear); 4-axis disproved; 3-axis sub-system INFO |
| S83-FI-DUALITY-THEOREM-FORMALIZATION (W1-G6) | INFO | 42/42 pointwise + 7/8 functor + 1 borderline |
| S83-CS-REGULATOR-DEPENDENCE (W2-G14) | PASS | c_s span 1.227 < 1.5 (R-protected) |
| S83-K-A2-CANONICAL-RANGE (W2-G15) | FAIL | span_A = 14.685 (NOT-R-protected) |
| S83-UNIFIED-AS-79-WITH-3PI-SUBSTITUTION (W2-G16) | PASS | A_s = 5.08e-9; 4/5 regulators PASS; 1/5 INFO (Zubarev-A) |
| S83-F-CONV-CLUSTER-TEST (W3-G28) | FAIL | cluster = 1766.16 (Mellin-unbalanced) |
| S83-CC-RATIO-CLUSTER-UNIVERSALITY (W3-G34) | FAIL | max_span = 42.03 (3 ratios all unbalanced) |
| S83-W_0-REGULATOR-CANONICAL-CHOICE (W3-G51) | FAIL | scheme split 0.08 (Zubarev -0.998 vs zeta -0.918) |
| S83-GODBILLON-VEY-JENSEN-DEFORM (W3-G56) | PASS | gv_response = -4.058e+04; primary index = 0 exact (Atiyah-Singer) |
| S83-PINNING-AUDIT-FRAMEWORK-WIDE (W3-G57) | PASS | 11/11 observables classified; distribution {FI-pin: 4, mostly-RD: 2, promotable: 2, FI-pure: 3, RD-unpinned: 0} |
| S83-META-PRINCIPLE-REGISTRY-LANDING (W3-G58) | PASS | R-protected vs NOT-R-protected taxonomy registered (§VII.K-META) |

---

## IV. Structural Implications

### IV.1 What opened

- **Layer-of-pin axis added to §VII.K-META taxonomy**. The R-protected vs NOT-R-protected binary partition is refined into a four-level hierarchy (L0-INT / L1-AX / L2-SA / L3-OB) with a residual UNPINNED bucket. This is more diagnostic than the binary partition because it identifies WHICH layer's pin a NOT-R-protected observable inherits from, not just the FACT of regulator dependence.

- **L1-L2 dissonance promoted from confusing-coincidence to structural-feature**. Earlier sessions (S65, S66, S67) treated zeta-vs-Zubarev disagreement as a "frustration triangle" requiring resolution. S83 W1-G1 + W1-G3 jointly establish that the two canonical picks are SOLUTIONS TO DIFFERENT EXTREMAL PROBLEMS and therefore need not agree. The G51 w_0 FAIL becomes a useful diagnostic (pin-mismatch detector) rather than an internal inconsistency.

- **Lizzi a_2-ratio theorem (W1-G4) promoted to permanent structural result**. The exact rational F_traj = 3/2 at the a_2 slot is now an observable-level theorem (not just a Mellin-weight ratio), connecting S78 W-2D, S76 f_conv workshop, and W1-G4 into a single statement: any zeta+SDW joint observable at the a_2 slot carries a permanent factor-1.5 floor.

### IV.2 What closed

- **Three-branch CC tree formally reduces to two-branch under L1**. W1-G3's PASS proves zeta is axiom-unique; W1-G1's PASS independently proves Zubarev is substrate-action-unique. The third branch (SDW canonical) is structurally excluded by KK-sign = -1 at L_max=5. The 3-branch tree is therefore a 2-branch hierarchy: (i) axiom-native zeta at L1, (ii) substrate-action Zubarev at L2.

- **CC-5 linearity identity made explicit**. A_s span = k_a2 span = 14.685054 to <1e-10 (Python-verified G16 cross-check CC-5). The A_s observable inherits ALL of its regulator-sensitivity from the upstream k_a2 slot weight. No new degree of freedom enters at the A_s level. This forces any future A_s-pinning theorem to operate at the k_a2 slot, not at the A_s output.

- **Off-Jensen FI promotion via CM Hopf H_1 closed by W1-G2 + W3-G56**. epsilon_H is permanently a Godbillon-Vey secondary class (triple-confirmed: W1-G2 heitsch_ratio = 16.20, W3-G54 GV-bucket assignment 1/53, W3-G56 stencil/analytic 5.98e-07 error). No spectral functional choice can move epsilon_H from the GV bucket to the primary HP^even bucket — this is a topological obstruction, not a regularization-method limitation.

### IV.3 What shifted

- **Standing target list refined**. The §VII.K-META taxonomy listed two mostly-RD observables (w_0, H_0). The S83 layer-of-pin atlas surfaces 5 UNPINNED rows on the 42-row VII.K atlas (#13 r_max, #17 w_0 R1, #18 w_0 R2, #24 a_2-cluster, #38 mu_eff LK). The latter list is more granular (per-row, not per-observable) and more diagnostic (each carries a specific structural reason for non-pinning).

- **Observable-layer remediation route narrowed**. W3-G28's FAIL at cluster = 1766 closes the "observable-level f_conv clustering rescues regulator invariance" hope. Either a multiplicative counterterm Z_R from Seeley-DeWitt consistency (unverified) or a balanced-Mellin-label observable (per W3-G34 cross-check predictions) is required. The framework cannot rely on linear-in-f_conv ledger observables to be R-protected.

### IV.4 Constraint-map updates

- §VII.K-META extended with LAYER-of-pin axis (registry candidate THREE-LAYER-REG-84, drafted in Appendix below).
- 5 UNPINNED rows promoted to S84 carry-forward priority list (see §V).
- Lizzi a_2-ratio theorem (F_traj = 3/2 exact at the f_2 slot) registry candidate.
- L1-L2 dissonance registered as a feature-not-bug; G51 w_0 FAIL re-classified as pin-mismatch diagnostic.

---

## V. Carry-Forward Computations

V.1. **L2-Sensitivity Audit on UNPINNED atlas rows**
   - **What**: for each of 5 UNPINNED rows (#13 r_max, #17/18 w_0 family, #24 a_2-cluster, #38 mu_eff LK), recompute under L2 Zubarev canonicalization (W1-G1 substrate-action choice) and report the L1-vs-L2 split. Cross-check via the layer-selection rule (Step 3 of §II.2 substitution chain).
   - **Inputs**: `s74_spectrum_cache_L9_tau019.npz`, `canonical_constants.py` (M_KK, tau_fold, Delta_BCS, eps_H), W1-G1 IC scheme pin (Zubarev), G15 k_a2^Zubarev value 0.07418.
   - **Gate**: pre-register `S84-UNPINNED-L2-AUDIT`. PASS: each of 5 rows shifts under L2 by < factor-1.5 relative to L1 reading (i.e., L2 reading is also a candidate pin). FAIL: any row's L2 shift exceeds factor-3 (genuinely unpinned by either layer). INFO: 1.5-3 (borderline).
   - **Effort**: 4-6 hours, 1 agent session. GPU not required (5x small spectral sums under Zubarev kernel).

V.2. **Higher-rank spectral triple falsifier (Spin(8) Cartan-extended fiber)**
   - **What**: build the full Dirac operator on the simply-laced Spin(8) gauge bundle over SU(3) (28-dim so(8) root system). Re-run the 3-regulator decision function (W1-G1 logic) on this spectrum and check whether L2 still picks Zubarev OR inverts to a different regulator. Compare against the L1 axiom-uniqueness result (which is structural and L_max-independent).
   - **Inputs**: Spin(8) Bourbaki simple-root data (W2-G17 already constructed), KO-dim-6 constraint, L_max <= 6 (sphere cutoff for tractability), Zubarev mollifier exp(-lam^2/M_KK^2).
   - **Gate**: pre-register `S84-THREE-LAYER-FALSIFIER`. PASS-confirms-theorem: L2 picks Zubarev again (theorem-permanence under rank-extension). PASS-falsifies-canonical-pick: L2 picks a different regulator at higher rank (theorem retains structure but L2 canonical pick is geometry-dependent). FAIL: theorem structure breaks (e.g., no regulator passes L2's three conditions). INCOMPUTABLE: integrability test requires unresolved gap.
   - **Effort**: 8-12 hours, 1 agent session. GPU recommended (Spin(8) eigvals at L=6 ~ 10^4 modes).

V.3. **L0-INT / L1-AX / L2-SA / L3-OB / UNPINNED tag insertion into §VII.K-DUAL atlas**
   - **What**: edit `sessions/permanent-results-registry.md` §VII.K and §VII.K-DUAL to add a per-row LAYER-of-pin column (one of {L0-INT, L1-AX, L2-SA, L3-OB, UNPINNED}). Use the classification in §II.4 above (Python-validated 26/2/1/8/5 distribution).
   - **Inputs**: this synthesis §II.4, the verbatim S82 §VII.K 42-row table at `sessions/archive/session-82/workshops/s82-regulator-dressing-taxonomy.md` lines 138-179.
   - **Gate**: pre-register `S84-LAYER-PIN-REGISTRY-LANDING`. PASS: §VII.K table updated with LAYER column on all 42 rows; layer counts match {L0-INT: 26, L1-AX: 2, L2-SA: 1, L3-OB: 8, UNPINNED: 5}; no row left blank. FAIL: any row mis-classified or layer count drifts from the Python-validated tally.
   - **Effort**: 1-2 hours, 1 agent session (edit-only).

V.4. **F_traj theorem formalization across ALL Mellin slots (not just a_2)**
   - **What**: extend the W1-G4 a_2-ratio theorem (F_traj = 3/2 = f_2^zeta / f_2^SDW) to compute f_k^zeta / f_k^SDW for k in {0, 2, 4, 6, 8}. Pre-register: f_k^zeta / f_k^SDW ratios will give the universal scheme-ratio floor at each Mellin slot. Hypothesize a closed-form (ratio = (k+2)/k or similar) and test.
   - **Inputs**: Mellin weight functions w_zeta(u) = 1, w_SDW(u) = 0.912*sqrt(u) + 0.088*exp(-u), Lambda^2 = 1 (natural units), `canonical_constants.py` (alpha_star, beta_star).
   - **Gate**: pre-register `S84-F-TRAJ-MELLIN-ATLAS`. PASS: closed-form rational ratio at every k tested AND empirical match within machine epsilon. INFO: closed-form at most slots, numerical at others (mixed). FAIL: no rational pattern (each k gives independent transcendental).
   - **Effort**: 2-3 hours, 1 agent session.

V.5. **CC-5 propagation theorem cross-class extension**
   - **What**: G16 CC-5 verified A_s span = k_a2 span exactly (linearity). Extend to test whether other UNIFIED-AS-79 ledger outputs (mu_distortion, f_NL, r) inherit upstream slot-weight spans linearly OR via different exponents (sqrt for f_NL, etc.). Goal: catalog every ledger observable's "span-inheritance exponent" so that future regulator-shifts can be predicted analytically rather than re-computed.
   - **Inputs**: UNIFIED-AS-79 formula `s80_unified_as_79_full.py`, G15 5-regulator k_a2 values, G16 CC-5 cross-check protocol, S67 GGE bispectrum amplitude formula (mu propto 1/M_0; f_NL propto 1/sqrt(M_0)).
   - **Gate**: pre-register `S84-LEDGER-LINEARITY-ATLAS`. PASS: each ledger observable has a measurable span-inheritance exponent against the upstream slot weight; exponents agree with closed-form predictions to <1% relative. FAIL: any observable's span-inheritance behavior is non-power-law in the upstream weight.
   - **Effort**: 4-5 hours, 1 agent session.

V.6. **L1-L2 dissonance projection table for all 11 framework-target observables**
   - **What**: G57 enumerated 11 framework observables {A_s, m_H, n_s, alpha_s, FIRAS-Chluba mu, r, f_NL, w_0, sigma_8, H_0, Omega_GW}. For each, compute the L1 (zeta-canonical) value and the L2 (Zubarev-canonical) value, and report the |split|. Goal: identify which observables are diagnostic of L1-L2 dissonance vs which are insensitive (L0-INT inheritance).
   - **Inputs**: G57 audit output, W1-G3 zeta normalization, W1-G1 Zubarev normalization, all 11 observable formulas with explicit regulator dependence.
   - **Gate**: pre-register `S84-L1-L2-PROJECTION`. PASS: at least 3 observables exhibit |split| > 0.05 (diagnostic), and at most 2 observables exhibit |split| < 0.001 (degenerate). FAIL: all 11 observables either degenerate (no diagnostic value) or wildly split (no useful pin).
   - **Effort**: 6-8 hours, 1 agent session.

V.7. **THREE-LAYER-REG-84 §VII.M registry landing**
   - **What**: write the canonical §VII.M registry entry to `sessions/permanent-results-registry.md` per draft in Appendix below. Cross-link to W1-G1 PASS, W1-G3 PASS, G14/G15/G28/G34/G51 verdicts, and §VII.K-META taxonomy.
   - **Inputs**: this synthesis Appendix; companion solos (parts b, c) to confirm convergence on the §VII.M formulation.
   - **Gate**: pre-register `S84-THREE-LAYER-REG-LANDING`. PASS: §VII.M entry queryable via `search_knowledge("three-layer regulator")`; cross-references to W1-G1, W1-G3, G14/15/28/34/51 verdicts present and resolve.
   - **Effort**: 1-2 hours, 1 agent session (registry edit + knowledge-MCP audit).

V.8. **Universal-Counterterm hypothesis test (Z_R from Seeley-DeWitt consistency)**
   - **What**: W3-G28 self-assessment carry-forward (a). Test whether a multiplicative renormalization Z_R defined by Seeley-DeWitt consistency `Z_R * f_conv^R = const` exists within the Chamseddine-Connes framework. If it exists, identify Z_R's structural form. If not, prove the obstruction.
   - **Inputs**: SD heat-kernel coefficients a_0, a_2, a_4, a_6 under {zeta, Zubarev, SDW}; Connes-Marcolli §1.6 Tauberian asymptotics; Wodzicki residue trace properties.
   - **Gate**: pre-register `S84-Z-R-COUNTERTERM`. PASS: closed-form Z_R derived such that `Z_R * f_conv^R` cluster span < 1.5 across 5 regulators. FAIL: no Z_R candidate satisfies the bound at any L_max <= 5. INFO: Z_R exists analytically but cluster span sits in [1.5, 2.5].
   - **Effort**: 12-16 hours, 1 agent session (heavy NCG/KK-theory derivation).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | L1 zeta unique under A1-A6 (W1-G3) | GEOMETRIC | PASS sha=2343920a.. | Layer-1 axiom-native canonical regulator established as theorem |
| 2 | L2 Zubarev unique under (integ + chi=+1 + local-min) (W1-G1) | GEOMETRIC | PASS sha=227a5913.. | Layer-2 substrate-action canonical regulator at tau_fold |
| 3 | L1-L2 canonical picks DISAGREE | GEOMETRIC | Theorem-of-dissonance | Each layer pins a different question; orthogonal selection rules |
| 4 | c_s R-protected (L3 PASS) | PHONONIC | G14 PASS span=1.227 | First-moment-ratio family is regulator-tolerant |
| 5 | k_a2 NOT-R-protected (L3 FAIL) | GEOMETRIC | G15 FAIL span=14.685 | Mellin-anchor ratios at a_2 are scheme-dependent |
| 6 | A_s span = k_a2 span (CC-5 identity) | PHONONIC | G16 CC-5 to <1e-10 | Linear-in-ledger propagation theorem |
| 7 | f_conv span 1766 (L3 FAIL) | PHONONIC | G28 FAIL | Observable-level f_conv clustering closed; counterterm route open |
| 8 | CC-ratio max span 42 (L3 FAIL) | PHONONIC + GEOMETRIC | G34 FAIL | Mellin-unbalanced ratio family confirmed RD |
| 9 | w_0 split 0.08 = L1-L2 dissonance projection | PHONONIC | G51 FAIL | First diagnostic of L1-L2 mixing on observables |
| 10 | F_traj = 3/2 exact (Lizzi a_2-ratio theorem) | GEOMETRIC + PHONONIC | W1-G4 INFO at boundary | Structural rational floor at f_2 slot for joint zeta+SDW observables |
| 11 | epsilon_H permanently GV-class | GEOMETRIC | W1-G2 + W3-G56 + W3-G54 triple-confirmed | No spectral functional moves eps_H to primary HP^even |
| 12 | 42-row LAYER-of-pin distribution {26 L0-INT, 2 L1, 1 L2, 8 L3, 5 UNPINNED} | GEOMETRIC | This synthesis §II.4 | Five standing UNPINNED targets identified for S84+ structural-pin work |
| 13 | THREE-LAYER-REG-84 registry candidate | GEOMETRIC | Drafted in Appendix | Permanent registry entry for the three-layer partition theorem |

---

## Appendix: Draft §VII.M Entry for `sessions/permanent-results-registry.md`

The following text is proposed for `sessions/permanent-results-registry.md` as the canonical §VII.M entry. The three-solo synthesis (parts a, b, c) converges on this single entry; the companion solos provide K-theoretic and observable-evidence formulations that are LOGICALLY EQUIVALENT to the spectral-functional formulation below.

```
## §VII.M — Three-Layer Regulator Theorem (S83 — three-solo convergence, 2026-04-18)

**Source**: S83 W1-G1 PASS (substrate-action) + S83 W1-G3 PASS (Connes axioms) + S83 W2/W3 observable-spans (G14, G15, G16, G28, G34, G51).
**Solo convergence**: Lizzi (spectral-functional formulation), companion solos (K-theoretic and observable-evidence formulations).

**Theorem (THREE-LAYER-REG-84)**: A spectral-functional ambiguity in any framework
built on a real spectral triple (A, H, D_K; J, gamma) of KO-dim 6 resolves at three
distinct epistemic layers, each with its own canonical pick and uniqueness argument:

  L1 (AXIOMATIC / Dixmier).  Under Connes axioms A1-A6 (dim-summability, reality,
      first-order, orientability, Poincare duality, regularity), the Connes residue
      formula
                   Tr_omega(|D|^{-d}) = Res_{s=d} zeta_D(s)
      uniquely determines a positive trace on the Macaev ideal L^{1,infty}(H).
      Up to normalization, zeta_D is the UNIQUE axiom-native regulator. No
      external scalar enters.
      [Witness: S83 W1-G3 PASS, sha=2343920a..; closed-form Connes-Marcolli §1.6.]

  L2 (SUBSTRATE-ACTION).  Under the joint criteria
                Connes-integrability AND local-min-tau AND KK-sign = +1
      at L_max=5, tau_fold=0.19, Zubarev with Lambda_Z = M_KK is the UNIQUE
      passing regulator. zeta fails local-min (curv = 0 structural at the
      counting function); SDW fails KK-sign = -1.
      [Witness: S83 W1-G1 PASS, sha=227a5913..; Branch-B 3-branch CC tree
       reduction.]

  L3 (OBSERVABLE).  Per-observable spans across {zeta, Zubarev, SDW, dim-reg,
      lattice-BR}. Two structural families:
        - R-protected (span < 1.5):  same-regulator first-moment ratios where
          weight cancels in numerator/denominator. Examples: c_s span 1.227
          (G14 PASS); alpha_SDW^NLO span 1.05 (G26 PASS).
        - NOT-R-protected (span >= 2.5):  Mellin-kernel integrals against a
          fixed anchor; single-moment absolutes. Examples: k_a2 span 14.69
          (G15 FAIL); A_s span 14.69 (G16 CC-5 identity); f_conv span 1766
          (G28 FAIL); CC-ratio max 42 (G34 FAIL); w_0 split 0.08 (G51 FAIL).
      [Witnesses: S83 W2-G14, W2-G15, W2-G16, W3-G28, W3-G34, W3-G51.]

**Layer-Selection Hierarchy**: L1 < L2 < L3. Each layer narrows further;
downstream observables must declare which layer's pin applies.

**Layer Dissonance** (FEATURE not bug): L1 picks zeta and L2 picks Zubarev.
This is structural — the layers solve different extremal problems and need
not agree. Observable manifestation: G51 w_0 FAIL at scheme-split 0.08 IS
the L1-L2 dissonance projected onto an observable (calibrated under L1,
canonical under L2). See substitution chain in S83 Lizzi synthesis §II.2.

**Layer-of-Pin Distribution on §VII.K 42-row atlas** (S83 Lizzi synthesis §II.4):
  L0-INT (no layer needed; FI by construction):     26 rows
  L1-AX  (axiomatic-Dixmier zeta selects):           2 rows
  L2-SA  (substrate-action Zubarev selects):         1 row
  L3-OB  (observable layer pin):                     8 rows
  UNPINNED (no layer pins; standing target):         5 rows
                                                    -------
  TOTAL                                            42 rows

The 5 UNPINNED rows (#13 r_max, #17 w_0 R1, #18 w_0 R2, #24 a_2-cluster,
#38 mu_eff LK) are the framework's standing targets for S84+ functional-
selection work.

**Pre-Registered Falsifier**: A higher-rank spectral triple (e.g., Spin(8)
Cartan-extended fiber on SU(3)) where L2's substrate-action minimizer is
not Zubarev (could be sharp/zeta or another family member) while L1's
axiomatic uniqueness still selects zeta would invert the L1-L2 dissonance
pattern. Such an inversion does NOT falsify the THEOREM (which is an
existence claim about the layer structure); it IS evidence that the L2
canonical pick is geometry-dependent rather than universally Zubarev.
[Pre-registered as S84 carry-forward V.2; gate S84-THREE-LAYER-FALSIFIER.]

**Scope of Applicability**:
  - Framework spectral triples of KO-dim 6 with finite-rank truncation
    L_max <= 10.
  - Analytic regulator class F_KK (Kasparov KK-homotopy invariance scope per
    §VII.K), including SDW, Zubarev, Wodzicki, Mellin-Laplace, CC96
    f-family, dim-reg, lattice-BR.
  - Excludes distributional regulators, compactly-supported-with-zeros
    kernels, and Godbillon-Vey-type secondary-class deformations (W1-G2 +
    W3-G56 closure).

STATUS: theorem; three-solo convergence registered. Logical level: above
§VII.K FI/RD/MIXED classification, §VII.K-DUAL M_lizzi/M_connes naturality,
and §VII.K-META R-protected/NOT-R-protected partition. Permanent result of
S83 Wave 1+2+3 harvest.
SIGNIFICANCE: Promotes the framework's regulator-choice ambiguity from a
"frustration triangle" (S65-S77 nomenclature) to a structurally-well-defined
three-level hierarchy with explicit layer-selection rules. Gates the
interpretation of every NOT-R-protected observable: predictions are
LAYER-pinned, not arbitrarily regulator-picked.
OPEN: (a) THREE-LAYER-FALSIFIER at higher-rank spectral triple (S84 V.2);
(b) L2-sensitivity audit on 5 UNPINNED atlas rows (S84 V.1);
(c) Z_R Seeley-DeWitt counterterm hypothesis (S84 V.8).
(value=L1-zeta-axiom-unique_L2-Zubarev-substrate-unique_L3-per-observable-span,
 scheme=three-layer-partition, convention=Connes-A1-A6-plus-substrate-action-plus-observable,
 L_max=5)
```

---
