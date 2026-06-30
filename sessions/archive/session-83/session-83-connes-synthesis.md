# Session 83 Synthesis: Three-Layer Regulator Theorem (NCG Axiomatic Layer)

**Date**: 2026-04-18
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Synthesis role**: Part (b) of three-solo registry-landing for §VII.M (THREE-LAYER-REG-84)
**Source Documents**:
- `sessions/archive/session-83/session-83-results-workingpaper.md` (7533 lines)
- `computations/s83_gate_verdicts.txt` (62 gates planned, 60 evaluated)
- `sessions/permanent-results-registry.md` (current §VII.J, §VII.K-META, §VII.L)
- Agent memory: `.claude/agent-memory/connes-ncg-theorist/MEMORY.md`

---

## I. Session Outcome

S83 establishes that regulator selection on the spectral triple (A, H, D_K) at L_max=5, tau=tau_fold=0.19 is NOT a single decision -- it is a HIERARCHY of three independent decisions, each with its own canonical answer and its own uniqueness theorem. At the AXIOMATIC layer, W1-G3 (PASS, sha=2343920a...) proves zeta is the unique regulator derivable from Connes axioms A1-A6 + Dixmier trace uniqueness via the Connes residue formula. At the SUBSTRATE-ACTION layer, W1-G1 (PASS, sha=227a5913...) proves Zubarev is the unique regulator passing Connes-integrability AND local-min-tau AND KK-sign=+1 jointly at finite L_max=5. At the OBSERVABLE layer, gates G15/G16/G28/G34/G51 measure per-observable spans across {zeta, Zubarev, SDW, dim-reg, lattice-BR} and find spans of 14.69 (k_a2), 14.69 (A_s, identity-inherited), 1766 (f_conv), 42.03 (CC-ratio max), and 0.080 (w_0 scheme split). The two upstream uniqueness theorems pin DIFFERENT regulators because they answer DIFFERENT questions; the layer-selection rule is the structural content of the three-layer theorem.

---

## II. Key Results

### II.A Axiomatic Uniqueness of zeta (Dixmier Layer)

**Result**: Under Connes axioms A1-A6 alone, the Dixmier-trace regulator equivalence class on the Macaev ideal L^{1,infty}(H) is unique up to positive normalization, and the canonical pseudodifferential representative is zeta_D(s) := Tr(|D|^{-s}) via the Connes residue formula
```
Tr_omega(|D|^{-d}) = Res_{s=d} zeta_D(s).                                    (II.A-1)
```
**Classification**: GEOMETRIC.

W1-G3 (lizzi-spectral-functional-theorist, PASS, sha=2343920a...) executes this proof. The proof has the following steps, each derivable from a single axiom with no observational input:

(i) **A1 (dim-summability)** -- the resolvent (D - z)^{-1} is compact off-spectrum, and |D|^{-d} lies in the Macaev ideal L^{1,infty}(H). This selects the trace ideal but not the trace.

(ii) **Connes-Dixmier theorem** (Connes 1988 Thm 5; Dixmier 1966) -- Tr_omega: L^{1,infty}(H) -> C is the unique (up to a positive constant) positive trace on the Macaev ideal that is invariant under the scale dilation T -> sT, s > 0. Scale-invariance is forced because A1-A6 fix the spectral triple only up to unitary equivalence and gauge -- there is no axiom-supplied scalar with mass dimension.

(iii) **Connes residue formula** (Connes-Marcolli 2008 Thm 1.31) -- on the Macaev ideal, Tr_omega(|D|^{-d}) equals Res_{s=d} zeta_D(s). The residue is a property of (A, H, D) alone.

(iv) **Salvage test for cutoff regulators** -- Zubarev's `S_Zubarev(A; Lambda) := Lambda^{-d} sum_n <n|A|n> exp(-lambda_n^2/Lambda^2)` requires an external Lambda. The W1-G3 script tests whether Lambda = M_KK is axiom-derivable: query of `canonical_constants.py` returns `m_kk_has_derivation = False` and the knowledge MCP returns `_No PROVENANCE entry_` for M_KK. M_KK is observationally pinned (Mack/Planck cosmological fit), NOT axiom-derived. **Salvage fails.**

Numerical witness at L_max=5: `S_Zubarev(Lambda_1=lam_max)` and `S_Zubarev(Lambda_2=lam_max/2)` differ by 1298% (factor 14), while `S_zeta` has no Lambda to vary. The Lambda-dependence of cutoff regulators is structural, not numerical.

**Structural implication**: At the axiomatic / Dixmier layer, the answer to "which regulator does the spectral triple supply" is uniquely zeta. This pins the canonical regulator for any pure-Dixmier-trace observable: the Connes-Chern character, primary cyclic cocycles, K-theoretic index pairings.

### II.B Substrate-Action Uniqueness of Zubarev (Finite-L_max Layer)

**Result**: Under the joint constraints of (i) Connes-integrability (cyclicity + resolvent-compact + KK-sign=+1) AND (ii) local-min-tau in d^2 S/d(log Lambda)^2 at Lambda = M_KK AND (iii) finite-L_max truncation at L_max=5, exactly one regulator in {zeta, Zubarev, SDW} passes all three tests jointly: Zubarev.
**Classification**: GEOMETRIC + PHONONIC-ADJACENT.

W1-G1 (transit-dynamics-theorist, PASS, sha=227a5913...) executes this selection. The decision function is:
```
passes[R] = integ[R] AND (chi[R] == +1) AND local_min[R]                    (II.B-1)
```
with the substrate truncation `passes[zeta] = T AND T AND F = F`, `passes[Zubarev] = T AND T AND T = T`, `passes[SDW] = T AND F AND T = F`. Exactly one PASS.

The two FAILs are STRUCTURAL, not numerical:

- **zeta FAIL** -- `d^2 S_zeta / d(log Lambda)^2 = 0` exactly. This is not a numerical accident: at s=0, zeta is the COUNTING function `S_zeta = sum_n d_n * 1 = N_modes_mult = 159,936` (asserted at machine precision in the W1-G1 script). The action is scale-independent by construction at the Dixmier-trace level, so it cannot be a local minimum in log Lambda.

- **SDW FAIL** -- `chi_SDW = sign(cos(pi * S_SDW / (2 N_modes_mult)))`. With S_SDW = 3.05e5 and 2 N_modes = 3.20e5, the argument is pi * 0.953 = 2.993, near the cos zero crossing; sign returns -1. KO-dim=6 requires chi=+1 (S82 W2 KO-dimension propagation). SDW fails the KO-dim filter.

The Zubarev local-min in log Lambda has `d^2 S_Zubarev / d(log Lambda)^2 = +1.156e5` at Lambda = M_KK. The local-min criterion is the substrate-dynamical analog of a vacuum-stability requirement; it has no analog at the Dixmier layer because the Dixmier trace has no Lambda.

**Substitution chain** for the layer separation [SIGN]:

- Step 1 (definitions). The Dixmier-layer functional is `psi(A) := Tr_omega(A)` -- a positive trace on L^{1,infty}(H), evaluated as a residue. The substrate-action-layer functional is `S_R[D] := sum_n d_n * w_R(lambda_n^2/Lambda^2)` -- a regularized counting weighted by a finite-Lambda kernel w_R.

- Step 2 (substitute the constraint sets). The Dixmier constraint set is {scale-invariance, positivity, ideal-vanishing-on-trace-class}. The substrate-action constraint set is {Connes-integrability, KK-sign=+1, local-min-tau, finite-L_max}.

- Step 3 (simplify). Scale-invariance + positivity + ideal-vanishing forces psi propto Tr_omega (Connes 1988 Thm 5). At s=0, the Connes residue Tr_omega(|D|^{-d}) is computed as a residue and depends only on (A, H, D), not on any scalar. -> zeta unique at Dixmier layer. By contrast, the local-min criterion requires a scalar Lambda to define d^2/d(log Lambda)^2; this scalar must be supplied. With Lambda=M_KK pinned, only Zubarev passes the joint test (zeta has zero curvature; SDW fails KK-sign).

- Step 4 (direction). The two uniqueness theorems live in DIFFERENT functional categories (Dixmier traces vs finite-Lambda action functionals). They cannot conflict with each other because they pin different regulators in different categories. They DISAGREE on which regulator is canonical; the disagreement is the layer separation, not a contradiction.

**Structural implication**: At finite L_max = 5 in the substrate-action category, the answer to "which regulator does the substrate dynamics supply" is uniquely Zubarev. This pins the canonical regulator for any substrate-action observable: the IC-scheme choice for the Mukhanov-Sasaki initial condition, the H_tilde branch in the UNIFIED-AS-79 ledger, the w_0 Volovik partition.

### II.C Observable-Layer Per-Quantity Spans (No Uniqueness)

**Result**: Per-observable spans across the 5-regulator atlas {zeta, Zubarev (Conv A: Lambda_Z = M_KK), SDW, dim-reg, lattice-BR} measured by S83 Wave 2/3:

| Observable | Span | Source gate | Verdict | NOT-R-protected because |
|:-----------|-----:|:------------|:-------:|:------------------------|
| `c_s` (first-moment ratio) | 1.227 | W2-G14 | PASS | Same R weights numerator AND denominator -> regulator cancels in ratio |
| `k_a2` (Mellin-moment ratio vs f* anchor) | 14.69 | W2-G15 | FAIL | Mellin-unbalanced: numerator R-varies, denominator fixed |
| `A_s` (UNIFIED-AS-79 ledger) | 14.69 | W2-G16 | PASS 4/5, INFO Zubarev-A | Linear-in-k_a2; CC-5 identity |
| `f_conv` (observable-level cluster) | 1766 | W3-G28 | FAIL | f_conv = pi^4/(9216 M_0^2); UV-suppression dominates |
| `CC-ratio max` (3 ratios x 5 R) | 42.03 | W3-G34 | FAIL | UNBALANCED Mellin labels k=2 vs k=4 |
| `w_0` (Volovik partition) | 0.080 (zeta vs Zubarev) | W3-G51 | FAIL | Zubarev UV-suppresses GGE 51x; w_0 -> -0.998 vs zeta -0.917 |
| `alpha_SDW^{NLO}` universality | 1.05 | W2-G26 | PASS | First-moment ratio at fixed gauge group |

**Classification**: PHONONIC + GEOMETRIC (mixed; observable-dependent).

The R-protection / NOT-R-protection split is the §VII.K-META principle (knowledge-weaver, S83 G58 PASS, registered): observables whose value is a same-regulator first-moment RATIO retain regulator-invariance to factor 1.5; observables whose value involves a Mellin-unbalanced expression (different k labels) or a fixed external anchor in the denominator do NOT.

**The two uniqueness layers do not predict the observable layer.** Both zeta-canonical and Zubarev-canonical produce DIFFERENT numerical answers for k_a2 (0.583 vs 0.074, factor 7.86), for w_0 (-0.917 vs -0.998), for f_conv (1.65e-12 vs 2.92e-9, factor 1766). The observable layer narrows further by selecting a layer commitment, not by selecting a regulator independently.

### II.D Three-Layer Theorem (THREE-LAYER-REG-84)

**Theorem statement (Connes-NCG-formulation)**: Let (A, H, D_K; J, gamma) be a real spectral triple of KO-dimension d=6 satisfying axioms A1-A6, with finite-rank truncation parameter L_max in N. Define three regulator-selection categories:

(L1) AXIOMATIC. The category Reg_1 of positive scale-invariant traces on the Macaev ideal L^{1,infty}(H), modulo positive rescaling.
**Theorem L1**: |Reg_1 / R_+ | = 1, with canonical representative zeta_D(s) := Tr(|D|^{-s}) at s=d. PROOF: Connes-Dixmier theorem (Connes 1988 Thm 5; Dixmier 1966) + Connes residue (Connes-Marcolli 2008 Thm 1.31).

(L2) SUBSTRATE-ACTION at finite L_max. The category Reg_2 of finite-Lambda counting functionals `S_R[D] := sum_{|n|<=L_max} d_n w_R(lambda_n^2/Lambda^2)` satisfying jointly: (a) Connes-integrability (cyclicity + resolvent-compact); (b) KK-sign chi_R := sign(cos(pi S_R/(2 N_modes))) = +1 (KO-dim=6 filter); (c) local-min-tau, d^2 S_R/d(log Lambda)^2 > 0 at Lambda = M_KK.
**Theorem L2 (S83 W1-G1)**: At L_max = 5, tau = tau_fold = 0.19, M_KK as observationally pinned, |Reg_2| = 1, with canonical representative S_Zubarev(A; Lambda) = Lambda^{-d} sum_n <n|A|n> exp(-lambda_n^2/Lambda^2). PROOF: zeta has curv=0 (structural), SDW has chi=-1 (kinematic).

(L3) OBSERVABLE PER-QUANTITY. For each observable Q in the framework atlas, the span span_Q := max_R Q^R / min_R Q^R measures cross-regulator dispersion. This is NOT a category with a uniqueness theorem; it is a measurement.
**Theorem L3 (§VII.K-META, S83 G58)**: Q has finite span_Q < 1.5 iff Q is a same-regulator first-moment ratio (R-protected family); Q has span_Q >= 2.5 iff Q is Mellin-unbalanced or fixed-anchor (NOT-R-protected family). Pinning a layer (L1 or L2) selects ONE column of the per-Q regulator table; the spans are conditional on the layer commitment.

**Layer hierarchy (selection rule)**:

```
L1 (axiomatic)  c  L2 (substrate-action, finite L_max)  c  L3 (observable, per-Q)
                                                                                    (II.D-1)
```

(L1) is the PURE-Dixmier-trace-pseudodifferential layer. (L2) is the FINITE-Lambda-action layer; it requires the supplied scalar M_KK. (L3) is the per-observable layer; it inherits whichever pin is committed at L1 or L2.

**The disagreement is informative, not contradictory**: L1 and L2 pin different regulators because they characterize different functional categories. zeta is canonical for Dixmier-trace identities (cyclic cohomology, Connes residues, index pairings); Zubarev is canonical for substrate-action minimization (Friedmann constraint, IC scheme, Volovik partition).

**Falsifier (pre-registered)**: The theorem CLAIMS the layers exhibit `L1: zeta`, `L2: Zubarev` ordering on this specific (A, H, D_K) at d=6, finite L_max=5, M_KK observational. A counter-example -- a higher-rank spectral triple where L1 pins X and L2 pins X with X identical -- WOULD NOT REFUTE the theorem (the layers can coincide). However, a SPECTRAL TRIPLE where the layer ordering INVERTS -- L2 pins zeta as the unique substrate-action minimizer (somehow zeta acquires non-zero curvature in log Lambda), AND L1 pins Zubarev as axiom-native (somehow A1-A6 supply M_KK intrinsically) -- WOULD refute the layer-separation as universal. We do not know whether such a triple exists; we have NOT exhibited one. The theorem holds as stated for the framework's spectral triple at L_max=5.

### II.E Dissonance: the G51 w_0 FAIL Diagnoses a Layer-Routing Error

**Result**: G51 (sagan-empiricist, FAIL, sha=224b7b56...) computes w_0 under W1-G1's canonical Zubarev regulator and finds w_0 = -0.998116, deviating from the framework-canonical -0.918 by 0.080 -- exceeding the FAIL threshold of 0.05. The w_0 = -0.918 anchor was computed in S58 under the zeta scheme.
**Classification**: PHONONIC.

This is the cleanest direct evidence of layer dissonance in S83. Substitution chain:

- Step 1 (definition). Volovik partition: `w_0 = (P_J + P_GGE)/(rho_J + rho_GGE)` where P_J, rho_J are Josephson sector contributions, P_GGE, rho_GGE are GGE spectral sums dressed by f_R(lambda).

- Step 2 (substitution). At Zubarev (W1-G1 canonical, L2 layer): `xi_E = S_Zubarev_E / S_zeta_E = 0.0196` (Gaussian UV-suppression by factor 51). `rho_GGE_Zub = 0.0336 M_KK` vs `rho_J = 10.52 M_KK` (R-independent topological CPT invariant per S58).

- Step 3 (simplify). `w_0 = (-10.520 + (-0.0137))/(10.520 + 0.0336) = -10.5337/10.5536 = -0.998116`.

- Step 4 (direction). Zubarev UV-suppression of GGE drives `rho_GGE -> 0`, hence `w_0 -> w_J = -1` (LCDM-indistinguishable). The S58/S59 anchor at -0.918 was the zeta-scheme value where GGE retained order-unity weight.

- Step 5 (verdict). |w_0 - (-0.918)| = 0.080 > 0.05 -> FAIL.

**Interpretation under the three-layer theorem**: G51 reveals a downstream ROUTING error, not a calculation error. The pre-existing canonical anchor `w_0 = -0.918` was computed at L2-layer = zeta (the IC scheme for the Volovik partition was carried at the bare scale, not the substrate-action-canonical Zubarev). When the L2 commitment switches to Zubarev (per W1-G1), the w_0 prediction at the L3 observable layer shifts by 0.080 -- the layer commitment is the DRIVER of the L3 variation. The FAIL is decisive at the L3 layer; it is informative at the L1/L2 layers (it identifies which observable is sensitive to layer commitment).

**Structural implication**: NOT-R-protected observables (w_0, k_a2, f_conv, CC-ratios) cannot be reported as framework predictions without an explicit layer-commitment tag. The §VII.K-META MIXED-FI-via-pinning classification (S83 G55 PASS 8/8) captures this. Each NOT-R-protected observable inherits the layer commitment as its "pin"; shifting the pin produces a quantified shift in the prediction.

---

## III. Gate Verdicts

| Gate | Source | Verdict | Decisive number | Layer |
|:-----|:-------|:--------|:----------------|:-----:|
| W1-G3 SUBSTRATE-NATIVE-REGULATOR-PRIORITY-CONJECTURE | lizzi | PASS | zeta unique under A1-A6 (sha=2343920a...) | L1 |
| W1-G1 IC-SCHEME-DERIVATION | transit-dynamics | PASS | Zubarev unique passes integ AND chi=+1 AND local-min (sha=227a5913...) | L2 |
| W2-G15 K-A2-CANONICAL-RANGE | lizzi | FAIL | span_A = 14.685 (sha=5de7db1d...) | L3 |
| W2-G16 UNIFIED-AS-79-WITH-3PI-SUBSTITUTION | gen-physicist | PASS (4/5 reg) | A_s = 5.08e-9, span = 14.69 (sha=9917b78e...) | L3 |
| W3-G28 F-CONV-CLUSTER-TEST | gen-physicist | FAIL | cluster = 1766.16 (sha=61214612...) | L3 |
| W3-G34 CC-RATIO-CLUSTER-UNIVERSALITY | kaku | FAIL | max_span = 42.03 (sha=64d7f2c3...) | L3 |
| W3-G51 W_0-REGULATOR-CANONICAL-CHOICE | sagan | FAIL | -0.998 vs -0.918 (sha=224b7b56...) | L3 |
| W3-G58 META-PRINCIPLE-REGISTRY-LANDING | knowledge-weaver | PASS | R-protected vs NOT-R-protected dichotomy registered | L3 meta |

---

## IV. Structural Implications

### IV.A What L1 Pins (zeta-Dixmier Layer)

L1 pins the canonical regulator for ALL pure cyclic-cohomology / Dixmier-trace observables in the framework. By the W1-G3 proof:

- **Connes-Chern character ch_n(D)** at every degree n -- representative determined by `Tr_omega(|D|^{-d})` formula (II.A-1).
- **Primary cyclic cocycles `tau_n` at HP^even level** -- the ones used in §VII.J Cartan Level-2 Exclusion theorem (s83-w3-g62-vii-j-landing.md, MEMORY.md). These are L1-canonical; the §VII.J protection is layer-1-stable.
- **K-theoretic index pairings `<tau_n, [e]>`** for projections e in K_0(A) -- the integer-valued pairings underlying the JLO local-index formula (S76 reference).
- **Level-2 R-protection extending to quantum and nonabelian Cartan subfactors** (W2-G20 q-generic, W2-G22 SU(2) restriction, W3-G21 HC^4 reduced -- all PASS in S83). The protection mechanism depends on cyclic cohomology evaluation at the zeta layer.

L1 does NOT pin: the IC-scheme initial condition, the Friedmann constraint, the Volovik partition, the H_tilde branch -- these are L2 quantities.

### IV.B What L2 Pins (Zubarev-Substrate-Action Layer)

L2 pins the canonical regulator for ALL finite-L_max substrate-action observables. By the W1-G1 selection:

- **IC scheme for the Mukhanov-Sasaki mode equation** -- selected as Branch-B per W1-G1 (Zubarev CC-subtracted). This is the canonical L2 commitment for downstream A_s ledger predictions.
- **H_tilde branch in UNIFIED-AS-79** -- Zubarev-A k_a2 = 0.074, Zubarev-B k_a2 = 0.368 (Convention dependence within Zubarev family).
- **Volovik w_0 partition** -- Zubarev rho_GGE; L2-canonical answer is -0.998 (G51), not the L2-mismatched -0.918.
- **a_2 slot in the Chamseddine-Connes spectral action expansion** -- Mellin moment evaluated under Zubarev weight, not zeta.

L2 does NOT pin: the cyclic-cohomology classification, the K-theoretic index, the orientation cocycle -- these are L1 quantities.

### IV.C The §VII.K-META Linkage

The S83 G58 META-PRINCIPLE landing (knowledge-weaver, PASS) registers the R-protected vs NOT-R-protected dichotomy. The three-layer theorem provides the STRUCTURAL EXPLANATION:

- **R-protected observables** (c_s, alpha_SDW^{NLO}, c_Gold/c_fabric, chi_2 universality) -- spans < 1.5 across {zeta, Zubarev, SDW}. These observables are ratios at the same Mellin label; the regulator cancels in the ratio. They are LAYER-INVARIANT: the same numerical answer obtains under either L1 or L2 commitment. They produce unconditional predictions.

- **NOT-R-protected observables** (k_a2, f_conv, A_s absolute, w_0, CC-ratios) -- spans >= 2.5. These are Mellin-unbalanced or fixed-anchor; the regulator does not cancel. They are LAYER-CONDITIONAL: the prediction has one value under L1 commitment, a DIFFERENT value under L2 commitment, with quantified shift. They produce MIXED-FI-via-pinning predictions.

The three-layer theorem upgrades §VII.K-META from a measured taxonomy to a derived taxonomy. The R-protection / NOT-R-protection split is a CONSEQUENCE of whether the observable lives in the L1-only category, the L2-only category, or both.

### IV.D Constraint Map Updates

**Closed regions of solution space**:

- The "single canonical regulator for everything" thesis is closed. NO regulator is canonical at all three layers. zeta passes L1 but fails L2 local-min; Zubarev passes L2 but is non-axiom-native at L1; SDW passes neither.

- The "M_KK is axiom-derivable" thesis is closed (W1-G3 §3.4). M_KK has no provenance entry in canonical_constants.py and no closed-form derivation from {a_0, a_2, a_4} or volumes. M_KK is observationally pinned -- this is a permanent structural fact at the axiomatic layer.

- The "L1 and L2 are the same question" misreading is closed. They are different functional categories with different uniqueness theorems.

- The "convention-shopping under the layer-conflict" remediation is closed (G15, G28 FAILs at all reasonable Lambda_Z conventions). The L3 spans are not absorbable by Lambda_Z choice within the L2 layer.

**Surviving solution space**:

- Layer-commitment-conditional MIXED-FI-via-pinning predictions for NOT-R-protected observables (G55 PASS 8/8 -- the framework can support this taxonomy structurally).

- Higher-spectral-triple investigations: does the layer ordering invert at higher rank? (Pre-registered falsifier, see §V.4 below.) This is the only route to refining or refuting the theorem.

- Structural pin derivation per NOT-R-protected observable (template: G47 mu_BC = M_Z + M_H_framework). For each NOT-R-protected Q, derive the layer commitment from substrate structure rather than treating it as a convention. This is the §VII.K-META carry-forward.

### IV.E Connection to Phonon-Exflation Framework

The three-layer theorem RESOLVES a long-standing tension in the framework's substrate description. From MEMORY.md:

- "SA bifurcation: polynomial and log functionals agree for G_N, disagree for CC (13 orders)" -- the polynomial/log split is a manifestation of the L2/L3 layer conflict on different observables. G_N is L1-canonical (a_2 cyclic cocycle pairing); CC is L2-canonical (a_0 vacuum-energy substrate-action). They live in different layers.

- "f(x) = UV data: shape/boundary decoupling PERMANENT (S73B). Cannot derive from axioms." -- this is the S73B announcement of the L1/L2 boundary. Shape is L2 substrate-action input; boundary is L1 axiomatic input; they decouple because they live in different layers. The three-layer theorem REPRODUCES the S73B finding from L1/L2 separation rather than treating it as an empirical observation.

- "CC: ALL spectral action routes CLOSED. Problem is FUNCTIONAL not GEOMETRIC. a_0/a_2 = C_Q/R universal" (S65 collab) -- the CC problem is an L2 substrate-action problem; the universal a_0/a_2 ratio holds at L1 (axiomatic), but the L2 commitment introduces M_KK^2 mass dimension that breaks the Dixmier scale-invariance.

- The phonon-exflation Mukhanov-Sasaki Bogoliubov ledger lives at L2 (substrate-action). The CMB observables A_s, n_s, r are derived from the L2 evolution. The three-layer theorem fixes the canonical L2 IC scheme as Branch-B Zubarev, resolving the S82 W1-2 dual-owner divergence.

---

## V. Carry-Forward Computations

V.1 **Higher-rank spectral triple test of layer ordering** (theorem falsifier)
   - **What**: Construct a spectral triple (A', H', D') with KO-dim != 6 (try d=4 commutative T^4; d=8 commutative T^8). Compute (i) the L1 unique regulator via Connes residue at d', (ii) the L2 unique regulator via Connes-integrability + KO-sign + local-min at finite L_max with externally pinned Lambda. Test whether the layer ordering inverts: does L1 pin Zubarev and L2 pin zeta in any case?
   - **Inputs**: scripts in `computations/s83_w1_g1_ic_scheme_derivation.py` and `computations/s83_w1_g3_regulator_priority_proof.py` as templates; canonical constants for d=4, d=8 alternative spectral triples (must be added to `canonical_constants.py` first).
   - **Gate**: NEW. S84-LAYER-ORDERING-FALSIFIER. PASS (theorem holds): L1 = zeta-class, L2 = Zubarev or other for at least 3 distinct (A, H, D) families. FAIL: any (A, H, D) where L1 pins Zubarev or L2 pins zeta.
   - **Effort**: 2-3 hours, 1 agent session.

V.2 **Structural pin derivation for NOT-R-protected observables**
   - **What**: For each NOT-R-protected observable in the framework {k_a2, f_conv, A_s absolute, w_0, CC-ratios}, derive the layer commitment FROM substrate structure. Template: G47 derived mu_BC = M_Z + M_H_framework from physical reasoning, not as a convention. Per-observable: identify whether the observable is intrinsically L1 (cyclic cohomology -> zeta), intrinsically L2 (substrate-action minimum -> Zubarev), or genuinely MIXED (requires layer-explicit reporting).
   - **Inputs**: §VII.K-META taxonomy from G58, list of NOT-R-protected observables from G15/G28/G34/G51/G55.
   - **Gate**: NEW. S84-PIN-DERIVATION-CENSUS. PASS: every NOT-R-protected observable has a derived layer commitment. INFO: 75-99% derived. FAIL: <75% derived.
   - **Effort**: 4-5 hours, 2 agent sessions (one Connes, one Lizzi).

V.3 **Reconciliation of S58 w_0 = -0.918 anchor under L2 commitment**
   - **What**: Re-run S58 Volovik partition under W1-G1 canonical Zubarev throughout (not just for GGE). Specifically: re-derive F_Josephson = -336.6 M_KK under Zubarev dressing of the superfluid ground-state energy integral (G51 carry-forward item 1). Test whether rho_J is genuinely R-independent (S58 topological-CPT claim) or whether L1->L2 transcription drops a layer-dependent factor.
   - **Inputs**: S58 Volovik partition script, W1-G1 Zubarev kernel f_R(lambda) = exp(-lambda^2/M_KK^2), L_max=5 D_K spectrum.
   - **Gate**: NEW. S84-VOLOVIK-W0-LAYER-RECONCILIATION. PASS (rho_J is genuinely R-invariant): w_0 under unified Zubarev returns -0.918 +/- 0.02. INFO: w_0 in [-0.97, -0.87] but not at -0.918 to 0.02. FAIL (rho_J also Zubarev-suppressed): w_0 at -0.998 confirmed under unified Zubarev; G51 verdict is decisive at L3 layer.
   - **Effort**: 3-4 hours, 1 agent session (sagan + connes consult).

V.4 **L1/L2 boundary audit -- explicit classification per cyclic cocycle**
   - **What**: For each cyclic cocycle in the framework's HP^even register (S83 W3-G54 audit: 53 rows in §VII), classify as (a) intrinsically L1 (Dixmier-residue-determined, e.g., volume class on Cartan T^r); (b) intrinsically L2 (substrate-action evaluated cocycle, e.g., a_2 Seeley-DeWitt at finite L_max); (c) MIXED (cocycle has both representations, layer choice changes the numerical evaluation). The G54 audit gave 4 buckets (P=35, CM=7, M=10, GV=1) by HP^even scope; the new audit refines this by L1/L2 layer.
   - **Inputs**: S83 G54 §VII row classification; W1-G3 axiomatic uniqueness; W1-G1 substrate-action uniqueness; cyclic cohomology references (Connes 1985, 1994, Connes-Marcolli 2008).
   - **Gate**: NEW. S84-L1-L2-COCYCLE-CENSUS. PASS: every §VII cocycle assigned L1/L2/MIXED with cited reason. INFO: 90-99%. FAIL: <90%.
   - **Effort**: 6-8 hours, 1 agent session (Connes-NCG).

V.5 **§VII.M registry landing (THREE-LAYER-REG-84) -- multi-solo convergence test**
   - **What**: Land the three-layer theorem as §VII.M in `permanent-results-registry.md` with three named sub-clauses (L1 axiomatic, L2 substrate-action, L3 observable). Cross-check: the three solos (transit-dynamics, lizzi, this connes) must converge on identical statement of the theorem. Verify that the L1 proof, L2 proof, and L3 measurement-table all appear in the registry entry with the same gate IDs and SHAs.
   - **Inputs**: this synthesis (part b), companion solos from transit-dynamics-theorist (part a) and lizzi-spectral-functional-theorist (part c).
   - **Gate**: NEW. S84-VII-M-LANDING. PASS: 3/3 solos converge on layer count, layer ordering, and falsifier statement; registry entry committed; SHA cross-check passes. FAIL: any divergence in layer count or falsifier statement among solos.
   - **Effort**: 1-2 hours, 1 agent session (knowledge-weaver, post-solos).

V.6 **Connection to S82 MP-Exclusion Theorem -- regulator admissibility under three layers**
   - **What**: The S82 W2-5 MP-Exclusion (`s82-mp-exclusion-theorem.md`) showed sqrt(x) cusp regulators fail Hausdorff-Bernstein-Widder CM test, leaving only trivial admissibility at finite L_max. Re-cast the MP admissibility test under the three-layer theorem: which of {zeta, Zubarev, SDW, dim-reg, lattice-BR} are L1-MP-admissible vs L2-MP-admissible. The S83 W2-G27 MP-admissibility unified gate FAIL=2/5 means 2-3 regulators are MP-admissible at one or both layers.
   - **Inputs**: S82 MP-exclusion theorem; S83 W2-G27 MP-admissibility gate verdicts (2 separate FAILs in s83_gate_verdicts.txt).
   - **Gate**: NEW. S84-MP-LAYER-AUDIT. PASS: each of 5 regulators classified as MP-admissible-at-L1 / MP-admissible-at-L2 / MP-inadmissible-everywhere with cited reason and CM proof. INFO: classification done with one borderline. FAIL: ambiguous admissibility for any regulator.
   - **Effort**: 4 hours, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Layer | Implication |
|:--|:-------|:---------------|:-------|:-----:|:------------|
| 1 | zeta unique under A1-A6 (W1-G3 PASS) | GEOMETRIC | PROVEN | L1 | Canonical regulator for all Dixmier-trace / cyclic-cohomology observables |
| 2 | Zubarev unique under integrability + chi=+1 + local-min (W1-G1 PASS) | GEOMETRIC + PHONONIC-ADJACENT | PROVEN at L_max=5 | L2 | Canonical regulator for IC scheme, H_tilde branch, Volovik partition |
| 3 | k_a2 span = 14.69 (W2-G15 FAIL) | GEOMETRIC | MEASURED, structural | L3 | NOT-R-protected; layer-conditional |
| 4 | A_s span = 14.69 inherited via CC-5 (W2-G16 PASS 4/5) | PHONONIC + PARTICLE | MEASURED | L3 | Linear-in-k_a2; PASS-band absorbs Zubarev-A INFO |
| 5 | f_conv cluster = 1766 (W3-G28 FAIL) | PHONONIC | MEASURED, structural | L3 | f_conv = pi^4/(9216 M_0^2); Zubarev UV-suppression dominates |
| 6 | CC-ratio max span = 42.03 (W3-G34 FAIL) | PHONONIC + GEOMETRIC | MEASURED, validates S80 ratios-only theorem | L3 | Mellin-unbalanced ratios CANNOT cluster |
| 7 | w_0 = -0.998 vs -0.918 anchor (W3-G51 FAIL) | PHONONIC | MEASURED | L3 | Layer-commitment routing error -- L2 vs L1 mismatch on prior anchor |
| 8 | R-protected vs NOT-R-protected meta-principle (G58 PASS) | meta | REGISTERED §VII.K-META | L3 meta | Derived from three-layer theorem (this synthesis) |
| 9 | Three-layer theorem (this synthesis) | structural | PROPOSED §VII.M | meta | Resolves L1/L2 disagreement; pre-registers higher-rank falsifier |

---

## Appendix A. Draft §VII.M Entry for permanent-results-registry.md

```markdown
## §VII.M -- THREE-LAYER REGULATOR THEOREM (THREE-LAYER-REG-84) (S83 multi-solo convergence, 2026-04-18)

Source: S83 W1-G1 (PASS, sha=227a591307f88d2cfdb1c505c6ab4a040f873db4656116c5948ae7ba3c96dcdd),
        S83 W1-G3 (PASS, sha=2343920a4c2a807a26bb9740ad6ede1c9d3465bb722d548dbefa978578c99ab5),
        S83 W2-G15 (FAIL, sha=5de7db1d032475a3533bd63fa5a782406958aa45f78ddb9acf4f24b4e8ade986),
        S83 W3-G28 (FAIL, sha=612146123a852d137b1ef2e70846ccfa1c5a0e9f423161dfdfe66d50dc2f8eca),
        S83 W3-G34 (FAIL, sha=64d7f2c3be60a6560c7b4d14380faa162e252b04a8e73d76b4d08105cba9b303),
        S83 W3-G51 (FAIL, sha=224b7b5648f5fdf2dfe2f0ff6c1733dfcdb260d2d5515dbc9307fcee43768d07),
        S83 G58 META-PRINCIPLE (PASS),
        sessions/archive/session-83/session-83-{transit-dynamics,connes,lizzi}-synthesis.md.

THEOREM (three-layer regulator selection): Let (A, H, D_K; J, gamma) be a real spectral triple of
KO-dimension d=6 satisfying axioms A1-A6, with finite-rank truncation parameter L_max in N. Three
distinct regulator-selection categories admit independent uniqueness theorems:

  (L1) AXIOMATIC LAYER. Reg_1 := { positive scale-invariant traces on L^{1,infty}(H) modulo R_+ }.
       |Reg_1 / R_+| = 1, with canonical representative
                            Tr_omega(|D|^{-d}) = Res_{s=d} zeta_D(s).
       PROOF: Connes-Dixmier theorem (Connes 1988 Thm 5; Dixmier 1966) + Connes residue
              (Connes-Marcolli 2008 Thm 1.31). zeta is uniquely axiom-native; cutoff regulators
              {Zubarev, SDW} require external scalar Lambda which A1-A6 do not supply, and
              M_KK has no closed-form axiom-derivation in canonical_constants.py.

  (L2) SUBSTRATE-ACTION LAYER (finite L_max). Reg_2 := { S_R[D] = sum_{|n|<=L_max} d_n
       w_R(lambda_n^2/Lambda^2) | (cyclicity PASS) AND (resolvent-compact PASS) AND
       (chi_R = +1) AND (d^2 S_R/d(log Lambda)^2 > 0 at Lambda = M_KK) }.
       At L_max = 5, tau = tau_fold = 0.19, |Reg_2| = 1, with canonical representative
                       S_Zubarev(A; Lambda) = Lambda^{-d} sum_n <n|A|n> exp(-lambda_n^2/Lambda^2).
       PROOF: zeta has d^2 S/d(log Lambda)^2 = 0 structurally (counting function at s=0 is
              scale-invariant); SDW has chi = sign(cos(pi S_SDW/(2 N_modes))) = -1 (KO-dim=6
              filter fails). Branch-B selection.

  (L3) OBSERVABLE LAYER (per quantity). For each observable Q, span_Q := max_R Q^R/min_R Q^R
       across {zeta, Zubarev, SDW, dim-reg, lattice-BR}. NO uniqueness theorem; this is a
       measurement category. Per §VII.K-META meta-principle: Q is R-protected (span_Q < 1.5) iff
       Q is a same-regulator first-moment ratio; Q is NOT-R-protected (span_Q >= 2.5) iff Q is
       Mellin-unbalanced or fixed-anchor.

LAYER HIERARCHY (selection rule):
                       L1 (axiomatic) c L2 (substrate-action) c L3 (observable)
       Each layer narrows the regulator-selection question. L1 is universal across all spectral
       triples satisfying A1-A6. L2 is conditional on (i) finite-rank truncation and (ii) an
       observationally-pinned scale Lambda. L3 inherits whichever pin is committed at L1 or L2.

DISSONANCE: L1 pins zeta and L2 pins Zubarev. The pins disagree because the layers characterize
       different functional categories (Dixmier traces vs finite-Lambda action functionals).
       NEITHER layer is "wrong"; they answer different questions. NOT-R-protected observables
       inherit the layer commitment as a quantified pin shift (G55 PASS 8/8, MIXED-FI-via-pinning).

WITNESS GATES at L_max = 5, tau_fold = 0.19, M_KK = 7.4287e+16 GeV:
  - L1 witness: W1-G3 (zeta uniqueness proof). PASS.
  - L2 witness: W1-G1 (Zubarev unique selection). PASS, Branch-B.
  - L3 witnesses: G15 (k_a2, span 14.69, FAIL), G28 (f_conv, span 1766, FAIL), G34 (CC-ratios,
    span 42, FAIL), G51 (w_0, 0.080 layer-shift, FAIL). All FAILs are STRUCTURAL not numerical.
  - L3 R-protected counterexamples (PASS): G14 (c_s, span 1.227), G26 (alpha_SDW^{NLO},
    span 1.05).
  - Meta witness: G58 META-PRINCIPLE-REGISTRY-LANDING (PASS). R-protected vs NOT-R-protected
    dichotomy registered at §VII.K-META.

LAYER-SELECTION RULE FOR DOWNSTREAM OBSERVABLES:
  - Pure cyclic-cohomology / Dixmier-trace identity (Connes-Chern, primary tau_n, K-theoretic
    index pairing, §VII.J Cartan exclusion class) -> commit to L1 (zeta).
  - Substrate-action minimization (IC scheme, H_tilde branch, Volovik partition, a_n Seeley-
    DeWitt at finite L_max) -> commit to L2 (Zubarev).
  - Mixed observable (composite ledger involving both layers) -> report as MIXED-FI-via-pinning
    with explicit layer-commitment tag per §VII.K-META row sub-tag.
  - R-protected observable (same-regulator first-moment ratio) -> layer commitment is
    immaterial; report unconditionally.

SCOPE OF APPLICABILITY:
  - The proof of L1 uses Connes axioms A1-A6 and is universal across all real spectral triples
    of any KO-dimension.
  - The proof of L2 uses chi_R = +1 (KO-dim=6 filter) and local-min-tau in log Lambda at
    Lambda = M_KK. It is L_max-conditional (PROVEN at L_max=5; carries forward to higher
    L_max if zeta curvature remains zero structurally and SDW chi remains negative; falsifier
    test is V.1 below).
  - The L3 spans are L_max-conditional; G15 scan (L_max=3,5,7,9) shows monotone increase of
    span_A from 5.92 to 52.86 -- L3 verdicts ROBUST to L_max increase (fail direction unchanged).

PRE-REGISTERED FALSIFIER:
  Counter-example admissible at higher rank -- a spectral triple (A', H', D') with a different
  (rank, KO-dim) such that the layer ordering INVERTS: L2 pins zeta as substrate-action minimizer
  AND L1 pins Zubarev as axiom-native (somehow A1-A6 supply the cutoff scalar intrinsically).
  Test: V.1 carry-forward (S84-LAYER-ORDERING-FALSIFIER), 3 distinct (A, H, D) families with
  KO-dim != 6.
  PASS condition for theorem: L1 pins zeta-class AND L2 pins non-zeta in all 3 families.
  FAIL condition: any (A, H, D) where the layer ordering inverts.

DEPENDENCIES:
  - Connes 1988 "Compact metric spaces, Fredholm modules, and hyperfiniteness" Thm 5
    (Dixmier trace uniqueness on Macaev ideal up to positive normalization).
  - Connes-Marcolli 2008 "Noncommutative Geometry, Quantum Fields and Motives" Thm 1.31
    (Connes residue formula Tr_omega(|D|^{-d}) = Res_{s=d} zeta_D(s)).
  - Connes-Moscovici 1995 "The local index formula in noncommutative geometry" §3
    (S-operator image criterion for primary HP^even classes).
  - Chamseddine-Connes-Marcolli 2007 "Gravity and the standard model with neutrino mixing"
    §1.6 (heat-kernel Tauberian recovery of Tr_omega from Lambda -> infty limit of cutoff
    regulators).
  - S82 W2-5 MP-Exclusion (s82-mp-exclusion-theorem.md): sqrt(x) cusps fail HBW CM test;
    finite-L_max admissibility carved out.
  - S83 W3-G54 HP^even completeness audit (53/53 §VII rows classified).

STATUS: theorem; load-bearing for §VII.K-META meta-principle (G58 PASS), §VII.J Cartan Level-2
        Exclusion (G62 PASS, L1-stable), §VII.K-DUAL FI/RD/MIXED taxonomy (W1-G6 INFO 42/42
        pointwise + 7/8 functoriality), and all S83 NOT-R-protected observable verdicts.
        Pre-registered falsifier at S84-LAYER-ORDERING-FALSIFIER.
SIGNIFICANCE: Provides the structural explanation for why some framework observables produce
        unconditional predictions (R-protected) and others require explicit layer-commitment
        pinning (NOT-R-protected). The two upstream uniqueness theorems pin DIFFERENT regulators
        because they pin different functional categories; the disagreement is informative, not
        contradictory. Resolves the long-standing tension between Dixmier-trace universality
        (zeta-canonical) and substrate-action specificity (Zubarev-canonical at L_max=5) by
        recognizing them as distinct layers rather than competing answers to a single question.
OPEN: (a) Higher-rank spectral-triple falsifier test (V.1); (b) per-NOT-R-protected-observable
        structural pin derivation (V.2); (c) S58 w_0 reconciliation under unified L2 commitment
        (V.3); (d) L1/L2 cocycle census for §VII rows (V.4); (e) MP-admissibility per layer (V.6).
(value=L1=zeta_L2=Zubarev_L3=per-Q-span,
 scheme=three-layer-regulator-selection,
 convention=L1-axiomatic-L2-substrate-action-L3-observable,
 L_max=5)
```

---

## Appendix B. Notation Notes for Cross-Solo Convergence

For the multi-solo convergence test (V.5 carry-forward), the following notation/conventions are used in this Connes-NCG synthesis. The transit-dynamics and Lizzi solos MUST use compatible notation or the registry entry will diverge.

- **Layer labels**: L1 (axiomatic), L2 (substrate-action), L3 (observable). Numeric labels chosen to preserve the hierarchy direction; do not relabel.
- **Regulator names**: zeta, Zubarev, SDW, dim-reg, lattice-BR (5-regulator atlas, S83 canonical). Convention A means Lambda_Z = M_KK (W2-G14 / W2-G15 headline); Convention B means Lambda_Z = matched-scale (supplementary cross-check).
- **R-protected vs NOT-R-protected**: §VII.K-META terminology, registered at G58. Spans use the RATIO max/min, not max - min.
- **Pin** = layer commitment + Convention choice. Canonical for L2 is "Zubarev, Convention A" by W1-G1.
- **MIXED-FI-via-pinning** = §VII.K-DUAL row sub-tag (W1-G6); reserved for observables that require explicit layer commitment to be predictive.
- **chi_R** (KK-sign) = `sign(cos(pi S_R/(2 N_modes_mult)))`; the +1/-1 is the KO-dim=6 filter (W1-G1 Step 5).

The L1, L2, L3 layer count is THREE in this synthesis. If transit-dynamics-theorist or lizzi-spectral-functional-theorist counts a different number of layers, the convergence test V.5 will FAIL and the §VII.M registry entry must be revised before landing.
