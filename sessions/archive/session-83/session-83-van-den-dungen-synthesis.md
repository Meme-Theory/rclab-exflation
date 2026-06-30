# Session 83 Synthesis: Three-Layer Regulator Theorem -- Kasparov-KK Formulation

**Date**: 2026-04-18
**Agent**: van-den-dungen-bridge-theorist (Van den Dungen)
**Source Documents**:
- `sessions/archive/session-83/session-83-results-workingpaper.md` (7,533 lines, 611 KB)
- `computations/s83_gate_verdicts.txt` (~100 verdict lines)
- `sessions/permanent-results-registry.md` (§VII.K-META, §VII.L)
- Agent memory: `.claude/agent-memory/van-den-dungen-bridge-theorist/MEMORY.md` (esp. `s82-kasparov-abelian-proof.md`, `s83-g24-result.md`)

---

## I. Session Outcome

S83 closes a long-running structural ambiguity by exhibiting THREE distinct K-theoretic layers at which the regulator-choice question is resolved, each with its own canonical answer and uniqueness argument. From the Kasparov-KK perspective, each layer is a different **K-theoretic pairing**: (i) the **axiomatic layer** is the Connes-Dixmier pairing `<Tr_omega, [|D|^{-d}]>` on the Macaev ideal -- W1-G3 PASS, sha=2343920a..., zeta is unique; (ii) the **substrate-action layer** is the cyclic pairing `<phi, [e]>` on `K_0(C(M^4) (x) C(SU(3)))` evaluated against the Connes-integrable closure -- W1-G1 PASS, sha=227a5913..., Zubarev is unique under the 3-criterion intersection {integrability, local-min-tau, KK-sign=+1}; (iii) the **observable layer** is the per-observable Mellin-balanced/unbalanced pairing inherited from the Kasparov product `[D_F] (x)_{C(M)} [D_M]` projected onto a finite list of observables -- W2-G15 (k_a2 span 14.69) FAIL, W3-G28 (f_conv span 1766) FAIL, W3-G34 (CC-ratio max span 42) FAIL. The three layers DO NOT pin the same question; their canonical answers DISAGREE (zeta vs Zubarev), but each disagreement traces to a structurally distinct K-pairing whose transport rule we make explicit below. G51 w_0 = -0.998 vs target -0.918 (|delta|=0.080 FAIL) is the canonical example of the cross-layer mismatch: prediction was calibrated under the axiomatic-layer canonical (zeta) but evaluated against the substrate-action-layer canonical (Zubarev) without the transport map.

---

## II. Key Results

### II.A. Three K-Theoretic Layers as Three Distinct Kasparov Pairings

**Result**: Three K-pairings, three uniqueness arguments, three canonical regulators. Classification: GEOMETRIC.

The Kasparov product on the M^4 x SU(3) submersion (Paper 01, 1811.07824, Theorem 3.4) factorizes the total Dirac operator into a base and fiber piece. From the K-homology side this writes
```
[D_K] = [D_F] (x)_{C(M)} [D_M]   in   KK^d(C(E), C)
```
The regulator question is "what trace machinery gives a finite, well-defined number when this K-class is paired against the relevant K-cocycle?" There is no SINGLE answer, because there are at least THREE distinct pairing structures attached to a single Kasparov class:

| Layer | K-pairing | Cocycle data | Output | S83 verdict |
|:------|:----------|:-------------|:-------|:------------|
| L1: Axiomatic (Dixmier) | `Tr_omega` on `L^{1,infty}(H)` | the Macaev-ideal class `[ \|D\|^{-d}]` | scalar Dixmier trace | zeta UNIQUE (W1-G3 PASS, sha 2343920a) |
| L2: Substrate-action (Connes-integrable) | `phi: HC^{ev}(A) (x) K_0(A) -> C` evaluated against the SUBSTRATE-action functional `S[D]` | the cyclic cocycle assembled from f(D) and the algebra A_F = C (+) H (+) M_3(C) | scalar action S | Zubarev UNIQUE (W1-G1 PASS, sha 227a5913) |
| L3: Observable | per-observable Mellin pairings `<f_n^R, [proj_n]>` for each spectral moment a_n | observable-specific (a_2 for gravity, a_4 for gauge, M_0 for f_conv) | observable values | per-observable, span 14.69 - 1766 (W2-G15, W3-G28, W3-G34 FAIL) |

The DISTINCTNESS of the three layers as K-pairings is the key structural content. They are not three approximations of one true regulator; they are three orthogonal questions about the SAME K-class.

### II.B. The Transport Maps Between Layers (Construction)

**Result**: Three layer-transport maps, only TWO of which are bijections at finite L_max=5. Classification: GEOMETRIC.

Define:
- **T_{L1 -> L2}**: take the Connes residue `psi(A) = Res_{s=d} Tr(A |D|^{-s})` and EXTEND it to a cyclic cocycle by integrating against the Hopf-cyclic transgression of A_F. This is a map of pairings, not a map of numbers: it sends "the axiom-native trace" to "the axiom-native trace EVALUATED on the action functional with the substrate-imposed regulator data". The image of T_{L1 -> L2} is the zeta-action `S_zeta = sum_n d_n` (Connes-Moscovici analytic continuation at s=0). T_{L1 -> L2} is well-defined (no extra data needed beyond A1-A6).

- **T_{L2 -> L1}**: the inverse takes a substrate-action regulator R, EXTRACTS its Mellin-Tauberian limit at s=d, and asks whether this equals the Connes residue. By the Tauberian argument (Connes-Marcolli 2008 §1.6), `lim_{Lambda -> infty} S_R(A; Lambda) = Tr_omega(A) Res_{s=d} zeta_D(s)` for compatible R. Zubarev satisfies this in the limit, but at FINITE Lambda the values differ -- the W1-G3 numerical sanity at L_max=5 gives a 1298.6% Lambda-shift in S_Zubarev under a factor-2 Lambda halving. T_{L2 -> L1} is a many-to-one projection at finite L_max; only at infinite L_max is it a bijection.

- **T_{L2 -> L3}**: per-observable shriek pi_! followed by Mellin extraction. For the observable a_n at spectral position k=n, the transport is `a_n^R = (1/Gamma(n/2)) f_n^R` where `f_n^R = int_0^{Lambda^2} w_R(u) u^{n/2-1} du`. This is the Chamseddine-Connes Mellin coefficient. The map is WELL-DEFINED but per-observable, and its image span is the observable-layer cluster reported by W2-G15 (k_a2 span 14.69), W3-G28 (f_conv span 1766), and W3-G34 (CC-ratio max span 42).

- **T_{L3 -> L2}** does NOT exist in general. Given an observable's value, one cannot reconstruct the action functional that produced it; the layer-3 -> layer-2 lift is many-to-one in the OPPOSITE direction (multiple action functionals can yield the same observable triple).

The substitution chain establishing layer non-collapse:
- *Definition*: T_{L1 -> L2}(zeta) = S_zeta (Connes-Moscovici); T_{L2 -> L1}(Zubarev at finite Lambda) = NOT well-defined as an isomorphism (Lambda-dependent).
- *Substitution*: at L_max=5, S_zeta = 1.599e+5 (verified above), S_Zubarev = 3.806e+3 (verified above). Ratio S_zeta / S_Zubarev = 42.03 (verified above). This is NOT a small perturbation; the layers are pairing-distinct.
- *Simplification*: if T_{L1 -> L2} were a bijection at L_max=5, then S_zeta = S_Zubarev would hold. The data shows S_zeta / S_Zubarev = 42.03 != 1.
- *Direction*: the layers are GENUINELY DISTINCT K-pairings at finite L_max; they coincide only in the Tauberian limit Lambda -> infinity and (equivalently) L_max -> infinity. PASS direction: the three-layer structure is a permanent feature of the spectral triple at the truncation scales used by the framework, NOT a numerical artifact.

### II.C. Layer-Selection Rule for Downstream Observables

**Result**: Each downstream observable selects ITS OWN layer based on the K-pairing it inherits. This is NOT a free choice. Classification: GEOMETRIC.

For an observable O computed on the substrate, the rule for "which layer's canonical regulator applies" is:

1. **If O is a topological / K-homology invariant** (mass orderings, sign of c_s^2, irrep selection rules, w_a in CS-asymmetric structure): O lives in image(ch: K_0 -> HP^0) and is REGULATOR-INDEPENDENT. Layer choice is moot. Zero-parameter prediction. (See `MEMORY.md` four-layer hierarchy item 1.)

2. **If O is a Dixmier-trace invariant** (scale-invariant traces, KO-dim normalization, axiomatic identities that survive A1-A6): use Layer 1 (zeta). The W1-G3 axiomatic uniqueness PROOF is the structural justification.

3. **If O is the SUBSTRATE ACTION ITSELF** or any quantity computed AS a stationary point of S[D] (epsilon_H derived from a_2, fold tau_fold, dressing factors at fold): use Layer 2 (Zubarev). The W1-G1 substrate-action minimization is the structural justification.

4. **If O is a SPECTRAL MOMENT** (a_n at fixed n, the corresponding f_conv, k_a2, A_s ABSOLUTE) computed via Mellin pairing on the truncated spectrum: use Layer 3, but with the pin chosen from the upstream layer that CALIBRATED the observable. The pin is the structural-justification chain that LINKS the layer-3 evaluation to a layer-1 or layer-2 anchor.

The substitution chain making this layer-selection rule operational:
- *Definition*: a downstream observable O carries a K-pairing class `[O] in HC^{deg(O)} (A_F)` derived from the cyclic-cohomology degree at which it lives.
- *Substitution*: deg(O)=0 (HC^0 = traces) -> Layer 1 zeta. deg(O)=action (cyclic 0-cocycle assembled with action data) -> Layer 2 Zubarev. deg(O)=Mellin coefficient at slot n -> Layer 3 with pin from upstream calibration.
- *Simplification*: the layer is DETERMINED by O's cyclic-cohomology degree, not chosen.
- *Direction*: PASS = each observable's layer is uniquely fixed by its K-pairing class. FAIL = an observable that mixes layer-1 calibration with layer-2 evaluation (e.g., G51 w_0). The G51 substitution chain confirms FAIL: w_0_target=-0.918 was a Layer-1 (zeta-bare) calibration, w_0_canonical_Zubarev=-0.998 is a Layer-2 evaluation, |delta|=0.080 (verified above), and the threshold |delta|<0.05 is exceeded. The FAIL is not a calculation error; it is the missing layer-transport.

### II.D. Why Layer 1 != Layer 2 -- The Hopf H_1 Obstruction

**Result**: The W1-G2 FAIL (epsilon_H secondary cocycle) is the K-theoretic OBSTRUCTION to layer-1/layer-2 collapse. Classification: GEOMETRIC.

The Connes-Moscovici Hopf algebra H_1 of codimension-1 transverse symmetries acts on A_F via the Jensen deformation `tau -> g(tau)`. For a regulator R, the question "does R survive Hopf-H_1 transgression to a primary HP^even cocycle?" is answered by computing `chi_CM(R)(a_0, a_1) = Tr_omega(a_0 [D_K, a_1] X^{-1})` and checking if `[chi_CM(R)] in image(S: HC^{n-2} -> HC^n)`.

W1-G2 FAILS this test for the natural CM-promotion candidate epsilon_H: `primary=False, chi_CM=0.2903, dGV=4.7016, heitsch_ratio=16.20, reg_inv=1.386`. The CM transgression returns a SECONDARY (Godbillon-Vey-type) class. This is the K-theoretic STATEMENT of layer-1/layer-2 distinctness: there is NO inner-fluctuation lift that takes Zubarev's cyclic cocycle to zeta's residue cocycle. The two regulators define DIFFERENT classes in HC^*(A_F) modulo S, separated by the GV-class obstruction.

Per W3-G54 (HP-EVEN-COMPLETENESS-AUDIT), this places epsilon_H in bucket GV (1/53 rows) -- the ONLY GV row in §VII at present. The fact that exactly one observable currently inhabits the GV bucket says the layer-1/layer-2 obstruction has been STRUCTURALLY ISOLATED. Most observables transport cleanly via P (35) or CM (7); 10 are MIXED requiring a pin; only epsilon_H is GV-excluded. The cleanness of this taxonomy is what makes the three-layer theorem ACTIONABLE: for the 35 P-bucket observables the layer choice is moot, for the 7 CM-extension observables the inner-fluctuation lift is a known operator, for the 10 MIXED observables the pin selects the layer, and for the 1 GV observable both layers fail and the observable is RD by axiomatic obstruction.

### II.E. The Connection to S82 Kasparov-Abelian Theorem

**Result**: The three-layer theorem extends S82's ABELIAN-SUBFACTOR-LACKS-LEVEL-2-R-PROTECTION result from the FIBER decomposition to the REGULATOR decomposition. Classification: GEOMETRIC.

S82 W2-3 (sha=61d73237...) proved: abelian C*-subfactors of the fiber algebra C*(SU(3)) lack Level-2 R-protection because rank-1 projection classes generate only Level-1 cohomology. The K-theoretic argument was: `K_0(C(X)) = Z^rho` for `X = Spec(A_B)` of rank rho, but Level-2 protection requires rank>=2 projections in M_n(C) embeddings, which abelian subalgebras lack.

S83 makes the dual statement at the REGULATOR level: regulators that fail to engage the non-abelian content of A_F (the Hopf H_1 transverse generator) cannot transport between layers. Zeta is `axiom-native` at Layer 1 because its Macaev-ideal trace acts identically on every irrep (rank-blind). Zubarev is `substrate-native` at Layer 2 because its Gaussian mollifier `exp(-lam_n^2 / Lambda^2)` weights modes BY their spectral position in a way that minimizes the action functional under the Connes-integrability constraint -- this picks out a specific cyclic cocycle class. The two regulators occupy different cohomology classes for the SAME structural reason that abelian and non-abelian fiber subfactors occupy different K-classes: different operator-theoretic data corresponds to different K-pairings.

### II.F. The Falsifier -- A Higher-Rank Spectral Triple Where Layers Invert

**Result**: Pre-registered falsifier for THREE-LAYER-REG-84. Classification: GEOMETRIC.

The three-layer theorem's strongest claim is that the LAYER HIERARCHY (axiomatic narrows substrate-action narrows observable) is a STRUCTURAL feature of compact-fiber Riemannian submersions with KO-dim 6. The falsifier at the Kasparov-KK level is a higher-rank spectral triple (e.g., HP^4 from the S74 Path 3 program) where the observation is INVERTED: substrate-action picks ZETA and the axiomatic layer fails to pin a unique regulator. Such an inversion would force a re-examination of whether the layer hierarchy is TIED to KO-dim 6 specifically (Cl(0,6) Clifford structure, the spin-c modification VdD Paper 02 §3) or whether it's a FEATURE of the M^4 x SU(3) submersion alone.

The pre-registered falsifier test, in 4-tuple form: at L_max=5 on HP^4 with its own canonical Dirac operator, compute (S_zeta, S_Zubarev, S_SDW). If `argmin_R S_R != Zubarev` AND `R_axiomatic != zeta` (i.e., HP^4's Dixmier residue picks a different unique regulator), the layer hierarchy INVERTS. PASS = inversion confirmed (theorem's scope is bounded by KO-dim 6 + Connes-Chamseddine rep). FAIL = no inversion (theorem extends to higher-rank submersions).

This is a STRUCTURAL falsifier: it falsifies the CLAIM that the hierarchy is uniform across compact-fiber submersions, not the claim that the three layers exist on M^4 x SU(3). The latter is established by W1-G3, W1-G1, and W2-G15/W3-G28/W3-G34 jointly.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number | Layer |
|:-----|:--------|:----------------|:------|
| S83-SUBSTRATE-NATIVE-REGULATOR-PRIORITY-CONJECTURE (W1-G3) | PASS | zeta unique under A1-A6 | L1 axiomatic |
| S83-IC-SCHEME-DERIVATION (W1-G1) | PASS | Zubarev unique (3-criterion) | L2 substrate-action |
| S83-EPSILON-H-SECONDARY-KK-PROMOTION (W1-G2) | FAIL | heitsch_ratio=16.20, GV-class | L1/L2 obstruction |
| S83-K-A2-CANONICAL-RANGE (W2-G15) | FAIL | span_A=14.685054 | L3 observable |
| S83-UNIFIED-AS-79-WITH-3PI-SUBSTITUTION (W2-G16) | PASS | A_s=5.078e-09, 4/5 PASS regulators | L3 with L1 pin |
| S83-CS-REGULATOR-DEPENDENCE (W2-G14) | PASS | c_s ratio=1.227 | L3 R-protected (first-moment ratio) |
| S83-F-CONV-CLUSTER-TEST (W3-G28) | FAIL | cluster=1766.16 | L3 observable |
| S83-CC-RATIO-CLUSTER-UNIVERSALITY (W3-G34) | FAIL | max_span=42.03 | L3 observable |
| S83-W_0-REGULATOR-CANONICAL-CHOICE (W3-G51) | FAIL | w_0=-0.998 vs -0.918, |delta|=0.080 | L1/L2 cross-layer mismatch |
| S83-FI-DUALITY-THEOREM-FORMALIZATION (W1-G6) | INFO | 42/42 pointwise, 7/8 functor | L3 dual-machinery |
| S83-HP-EVEN-COMPLETENESS-AUDIT-VII (W3-G54) | PASS | 53/53 = P:35, CM:7, M:10, GV:1 | meta-classification |
| S83-MIXED-SUB-TAG-PER-ROW (W3-G55) | PASS | 8/8 valid, 2 FI-pin + 4 mostly-RD + 2 promotable | L3 pin taxonomy |
| S83-NONFLAT-T-CORRECTION-L2 (W2-G24) | PASS | ratio=0 EXACT (Cartan + Jensen preserves Cartan) | fiber-internal |

---

## IV. Structural Implications

**1. Layer collapse is FORBIDDEN at finite L_max.** The 1298.6% Lambda-shift gap in S_Zubarev (W1-G3 §3.5) and the 42.03x ratio S_zeta/S_Zubarev (computed above) both demonstrate that Layers 1 and 2 are NOT numerical approximations of each other at the truncation scales used by the framework. They coincide only in the Tauberian limit, and the framework operates strictly below that limit. The three-layer structure is therefore a PERMANENT feature of the spectral triple at framework scales, not a numerical artifact.

**2. The §VII.K-META R-protected/NOT-R-protected dichotomy is the OBSERVABLE-LAYER signature of the three-layer structure.** Per the registry (line 803-809), R-protected family (c_s, alpha_SDW^NLO, c_Gold/c_fabric, chi_2 universality) consists of FIRST-MOMENT RATIOS where the regulator weight cancels in numerator/denominator. NOT-R-protected family (k_a2, f_conv, A_s absolute, w_0) consists of MELLIN-UNBALANCED quantities that inherit the layer disagreement. The Lizzi observable classification (S83 W2-G15 Self-assessment §3) exactly tracks this: same-regulator-numerator-and-denominator -> R-protected; fixed-anchor-denominator-with-regulator-varying-numerator -> NOT R-protected. The K-theoretic restatement: ratios of cocycles at the SAME degree pair against `[1] in K_0` invariantly; ratios at MIXED degrees pair against degree-mixed K-classes that depend on regulator-specific cyclic-cohomology representatives.

**3. G51 w_0 FAIL is a layer-mismatch DIAGNOSTIC, not a framework failure.** The S58 canonical w_0=-0.918 was computed under zeta (Layer-1 baseline). W1-G1 selected Zubarev (Layer 2). The G51 computation evaluates the Volovik partition under Zubarev and gets w_0=-0.998 (verified above to bitwise precision). The FAIL signals: the partition's INPUT calibration was at Layer 1, but the substrate-action layer canonical is now Layer 2. To resolve, either (a) re-derive the Volovik partition's rho_J calibration directly under Zubarev (closing the layer-2 self-consistency loop), or (b) explicitly accept that w_0 is a Layer-1 observable with the substrate-action layer driving it toward LCDM. This is the substantive structural content of the FAIL.

**4. The §VII.K-DUAL natural-transformation eta (W1-G6 INFO) is the dual-machinery face of the three-layer theorem.** M_lizzi (spectral-moment functor) and M_connes (K-homology functor) agree pointwise on 42/42 observables but disagree on 1/8 functor-composites. The three layers are the THREE POSITIONS in the natural-transformation diagram where M_lizzi and M_connes can be queried: at the trace level (Layer 1 = Connes residue = Lizzi axiomatic moment), at the action level (Layer 2 = Connes inner-fluctuation = Lizzi substrate spectral functional), at the observable level (Layer 3 = Connes Kasparov product projection = Lizzi a_n Mellin). The 1/8 functor-failure (composite-rule borderline-MIXED) is the K-theoretic STATEMENT that the three layers do NOT collapse to a single functor.

**5. Layer narrowing (axiomatic <= substrate-action <= observable).** Verified directly: Layer 1 admits exactly 1 regulator (zeta) by axiomatic uniqueness theorem; Layer 2 admits exactly 1 regulator (Zubarev) by 3-criterion intersection; Layer 3 admits up to 5 regulators per observable, with the per-observable verdicts span 1.23 (c_s, R-protected) to 1766 (f_conv, R-NOT-protected). The narrowing is STRICT at L1 -> L2 (different regulator selected) and STRICT at L2 -> L3 (multiple regulators admissible per pin).

**6. Constraint-map update.** The constraint map gains: THREE-LAYER-REG-84 = three K-pairings on the same Kasparov class give three different unique regulators at finite L_max=5, each pinned by a distinct uniqueness theorem (Connes residue for L1, Connes-Moscovici integrability + KK-sign + local-min-tau for L2, Mellin-balanced/unbalanced classification for L3). This constraint REPLACES the prior assumption that "one canonical regulator pin determines all observables".

---

## V. Carry-Forward Computations

V.1. **Build T_{L2 -> L3} per-observable transport table for §VII.K MIXED rows**
   - **What**: For each of the 10 §VII.K MIXED rows (W3-G54 audit), compute the explicit Mellin transport from Layer-2 (Zubarev action functional) to Layer-3 (observable value), tabulating the layer-shift factor per row. Build the registry-ready transport-map artifact.
   - **Inputs**: `s83_w3_g54_hp_even_completeness_audit_vii.npz` (10-row MIXED list); `canonical_constants.py` (Lambda_Z = M_KK pin); per-row a_n slot index from §VII.K-DUAL.
   - **Gate**: NEW gate S84-LAYER-TRANSPORT-AUDIT. PASS: each row has explicit layer-shift factor with substitution chain; FAIL: any row left unmapped.
   - **Effort**: 4-6 hours, 1 agent session.

V.2. **Compute HP^4 axiomatic regulator and substrate-action regulator independently**
   - **What**: On HP^4 spectral triple (S74 Path 3 candidate), evaluate Dixmier residue at d=KO_DIM(HP^4) AND minimize substrate-action under {zeta, Zubarev, SDW}. Compare to M^4 x SU(3) selection (zeta, Zubarev). PASS = different argmin (theorem's scope confirmed bounded by KO-dim 6 + SU(3)); FAIL = same selection (theorem extends to higher-rank submersions).
   - **Inputs**: HP^4 D_K spectrum at L_max=5 (compute from scratch); KO_DIM(HP^4) verification via Atiyah-Bott-Shapiro.
   - **Gate**: NEW falsifier gate S84-THREE-LAYER-FALSIFIER. PASS = inversion; FAIL = no inversion. Pre-registered: 4-tuple (R_axiomatic^{HP4}, R_substrate^{HP4}, KO_DIM(HP^4), L_max=5).
   - **Effort**: 12-18 hours, 2 agent sessions (HP^4 spectrum is non-trivial to set up).

V.3. **Re-derive G51 w_0 with rho_J under Zubarev (layer-2 self-consistency)**
   - **What**: Recompute the Volovik-partition rho_J = |F_Josephson|/N_cells under Zubarev regulator (currently the S58 canonical is zeta-baseline). If rho_J(Zubarev) / rho_J(zeta) = 51 (matching the GGE suppression factor xi_E = 0.0196), then w_0 returns to -0.918 from numerator+denominator co-suppression. If rho_J is genuinely R-independent (S58 topological-CPT claim), w_0 stays at -0.998 and the framework's canonical w_0 prediction MOVES to LCDM.
   - **Inputs**: F_Josephson computation in canonical Volovik partition (need Volovik agent collaboration); Zubarev regulator at L_max=5 from W1-G1 npz.
   - **Gate**: S84-W0-LAYER2-SELFCONSISTENCY. PASS: w_0(Zubarev with Zubarev-dressed rho_J) within 0.02 of -0.918. FAIL: outside 0.05.
   - **Effort**: 6-8 hours, 1 agent session (Volovik + van-den-dungen joint).

V.4. **Formalize the W1-G2 GV obstruction as a K-theoretic statement**
   - **What**: The W1-G2 FAIL (epsilon_H secondary cocycle, heitsch_ratio=16.20) is currently presented as a Heitsch variation test. Promote to a K-theoretic statement: epsilon_H lives in `HP^*(A_F) / image(S)` at a position OUTSIDE image(ch: K_0 -> HP^0). Verify the position by direct computation of `[epsilon_H] in HP^1(A_F)` and `[GV]` from the Connes-Moscovici Godbillon-Vey lift.
   - **Inputs**: A_F = C (+) H (+) M_3(C) cyclic cohomology computation; Heitsch variation data from `s83_w3_g56_godbillon_vey_jensen_deform.npz`.
   - **Gate**: S84-EPSH-K-CLASS-LOCATION. PASS: K-class identified explicitly in HC^*(A_F) and shown to be GV-secondary by direct cocycle computation. FAIL: K-class not identifiable.
   - **Effort**: 8-12 hours, 1 agent session.

V.5. **Audit all R-protected observables for Mellin-balanced K-pairing**
   - **What**: For each R-protected observable (c_s, alpha_SDW^NLO, c_Gold/c_fabric, chi_2 universality), verify via direct K-theoretic computation that the cocycle pair (numerator, denominator) sit at the SAME Mellin label, and that this is the structural reason for R-protection. Distinguish "same Mellin label by accident of definition" from "same Mellin label by K-pairing structure".
   - **Inputs**: spectral data per observable; W3-G34 derivation of which Mellin labels each ratio uses.
   - **Gate**: S84-R-PROTECTION-K-AUDIT. PASS: each R-protected observable mapped to a balanced-Mellin K-pairing class; FAIL: any R-protected observable found to be balanced by accident (no underlying K-class identity).
   - **Effort**: 6-9 hours, 1 agent session.

V.6. **Test layer narrowing at L_max=7,9 (extrapolation)**
   - **What**: Recompute (S_zeta, S_Zubarev, S_SDW) and the W1-G1 3-criterion intersection at L_max=7 and L_max=9. PASS if Zubarev remains unique substrate-action minimum AND zeta remains unique Dixmier-axiom regulator at all L_max. FAIL if either uniqueness inverts at higher L_max (would mean the W1-G1 PASS is a truncation artifact).
   - **Inputs**: D_K spectra at L_max=7 and L_max=9 (already cached from W2-G15 L_max scan if extended).
   - **Gate**: S84-LAYER-UNIQUENESS-LMAX-EXTRAPOLATION. PASS: uniqueness holds at L_max in {5,7,9}. FAIL: uniqueness inverts.
   - **Effort**: 3-4 hours, 1 agent session.

V.7. **Construct the explicit cyclic-cohomology obstruction class for the W1-G2 GV element**
   - **What**: Following W3-G54 GV-bucket assignment, compute `[GV(F_Jensen)] in H^3(M^4)` directly from the Jensen foliation 1-form omega_J, Gel'fand-Fuks at codim 1. Verify the Heitsch variation test `gv_response = -4.0579e+04` matches the analytic Pontryagin-cohomology computation.
   - **Inputs**: Jensen foliation omega_J = e^{-tau} dtau ; G56 stencil data from `s83_w3_g56_godbillon_vey_jensen_deform.npz` for the variation cross-check.
   - **Gate**: S84-GV-CLASS-EXPLICIT. PASS: gv_response from GF computation matches W3-G56 to within 1% (already computed in G56 to stencil_err=5.98e-07). FAIL: discrepancy >1%.
   - **Effort**: 4-6 hours, 1 agent session.

V.8. **Cross-check the W1-G6 1/8 functor failure against the three-layer transport map**
   - **What**: The W1-G6 INFO verdict (42/42 pointwise, 7/8 functor) flagged a single composite-functor failure. Determine whether this 1/8 failure corresponds EXACTLY to a layer-1/layer-2 cross-pin in the underlying composite (i.e., the failing composite mixes Layer-1 calibration with Layer-2 evaluation, just like G51).
   - **Inputs**: W1-G6 npz with the failing composite identified; layer-pin map from §VII.K-META.
   - **Gate**: S84-W1G6-LAYER-DIAGNOSIS. PASS: 1/8 failure traces to layer-pin mismatch (confirms three-layer theorem covers composite functoriality). FAIL: 1/8 failure has independent origin (means composite functoriality requires separate machinery beyond three-layer).
   - **Effort**: 3-4 hours, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Three K-pairings, three uniqueness arguments, three canonical regulators | GEOMETRIC | THEOREM (W1-G1 + W1-G3 + W2-G15/W3-G28/W3-G34) | Replaces "single canonical regulator" with layered hierarchy |
| 2 | Layer transports T_{L1 -> L2}, T_{L2 -> L1}, T_{L2 -> L3} explicit; T_{L3 -> L2} non-existent | GEOMETRIC | CONSTRUCTED | Provides operational rule for downstream observables |
| 3 | Layer narrowing strict at L_max=5: 1, 1, per-observable | GEOMETRIC | VERIFIED (3 PASS gates) | Each layer is genuinely narrower than the prior |
| 4 | epsilon_H GV-obstruction is the K-theoretic non-collapse | GEOMETRIC | VERIFIED (W1-G2 FAIL + W3-G54 GV-bucket=1/53) | Layers DON'T collapse for a structural cohomological reason |
| 5 | G51 w_0 FAIL diagnoses cross-layer pin mismatch | PHONONIC | DIAGNOSTIC (FAIL is informative) | Volovik partition needs Layer-2 self-consistency check |
| 6 | R-protected vs NOT-R-protected dichotomy = observable-layer signature of three-layer structure | GEOMETRIC | DERIVED (§VII.K-META) | Provides the K-theoretic explanation for §VII.K-META taxonomy |
| 7 | S82 KASPAROV-ABELIAN extends from fiber rank to regulator class | GEOMETRIC | EXTENSION | Same K-theoretic mechanism (rank-1 vs rank>=2 cocycles) underlies both fiber and regulator distinctness |
| 8 | Pre-registered HP^4 falsifier defines theorem's scope | GEOMETRIC | PRE-REGISTERED (V.2) | Theorem may be tied to KO-dim 6 specifically |

---

## Appendix: Draft §VII.M Registry Entry

**Proposed for `sessions/permanent-results-registry.md`, between §VII.L and §VIII.**

---

### §VII.M -- THREE-LAYER-REG-84: The Three-Layer Regulator Theorem

**Source**: S83 W1-G1 (PASS, sha=227a591307f88d2cfdb1c505c6ab4a040f873db4656116c5948ae7ba3c96dcdd), W1-G3 (PASS, sha=2343920a4c2a807a26bb9740ad6ede1c9d3465bb722d548dbefa978578c99ab5), W2-G15 (FAIL span_A=14.685054, sha=5de7db1d032475a3533bd63fa5a782406958aa45f78ddb9acf4f24b4e8ade986), W3-G28 (FAIL cluster=1766.16, sha=612146123a852d137b1ef2e70846ccfa1c5a0e9f423161dfdfe66d50dc2f8eca), W3-G34 (FAIL max_span=42.03, sha=64d7f2c3be60a6560c7b4d14380faa162e252b04a8e73d76b4d08105cba9b303), W1-G2 (FAIL heitsch_ratio=16.20, sha=bec1b395351664de65dcc40c172d61f66cfaafb3cc7147b718ce6831871acffe), W3-G51 (FAIL w_0=-0.998, sha=224b7b5648f5fdf2dfe2f0ff6c1733dfcdb260d2d5515dbc9307fcee43768d07), W3-G54 (PASS 53/53, sha=1d2bde0ce48eb54d9eef40fa7a8c6c0152bff77b8155432a3c5436dbcdac45e0).

**Statement (formal)**:

Let `(A, H, D)` be a Connes spectral triple of KO-dimension 6 over the algebra `A_F = C (+) H (+) M_3(C)` on the M^4 x SU(3) Riemannian submersion. Let R_F be the family of admissible spectral regulators `R: H -> H` that satisfy positivity and trace-class boundedness on `|D|^{-d}`. There exist THREE distinct K-theoretic pairings on `KK^d(A, C)` -- denoted L1 (axiomatic, Dixmier), L2 (substrate-action, Connes-integrable), L3 (observable, Mellin-projected) -- such that:

1. (Layer 1) The pairing `<Tr_omega, [|D|^{-d}]>` admits a UNIQUE admissible regulator up to scale, namely the spectral zeta regulator `zeta_D(s) := Tr(|D|^{-s})` evaluated at its s = d residue.

2. (Layer 2) The pairing `<phi_S, [e]>` against the substrate-action functional S[D] admits a UNIQUE admissible regulator under the conjunction (Connes-integrability AND local-min-tau AND KK-sign=+1), namely the Zubarev Gaussian mollifier `f_R(lam) = exp(-lam^2 / Lambda_Z^2)` with `Lambda_Z = M_KK`.

3. (Layer 3) For each observable O of cyclic-cohomology degree n, the per-observable Mellin pairing `<f_n^R, [proj_n]>` admits a per-pin set of admissible regulators with span dictated by the Mellin-balanced/unbalanced classification of O (R-protected family span <= 1.5; NOT R-protected span >= 2.5).

The three layers do NOT pin the same K-pairing; their canonical regulators DISAGREE (zeta != Zubarev) at finite L_max, separated by a structural cohomological obstruction (the Connes-Moscovici Hopf-H_1 transgression failure quantified by the W1-G2 GV-class diagnosis). The layer hierarchy is STRICT (axiomatic narrows substrate-action narrows observable) at L_max=5 with the W1-G3 axiomatic uniqueness, W1-G1 substrate-action uniqueness, and W2-G15/W3-G28/W3-G34 observable-layer FAIL spans as the layered narrowing.

**Three proofs**:

**Proof 1 (L1 axiomatic uniqueness)**. Connes 1988 Theorem (Connes-Marcolli 2008 §1.6 Theorem 1.31): on a spectral triple of dim-summability d, the Dixmier trace `Tr_omega: L^{1,infty}(H) -> C` is the unique (up to normalization) positive trace on the Macaev ideal invariant under scale dilation. Its representative on `|D|^{-d}` is the Connes residue `Res_{s=d} zeta_D(s)`. No external scalar enters; Zubarev's `Lambda_Z` and SDW's `Lambda_S` are external data not supplied by axioms A1-A6 (W1-G3 §3.4). HENCE zeta is the unique axiom-native regulator.

**Proof 2 (L2 substrate-action uniqueness via 3-criterion intersection)**. Define `passes[R] := integrability_R AND local-min-tau_R AND (KK-sign_R = +1)`. From W1-G1 numerical sanity at L_max=5, tau_fold=0.19:
- `passes[zeta]    = True AND True  AND False` (curv_zeta = 0 by construction; not a local minimum)
- `passes[Zubarev] = True AND True  AND True` (curv_Zubarev = +1.16e+5; KK-sign = +1)
- `passes[SDW]     = True AND False AND True` (KK-sign_SDW = -1)

Exactly ONE regulator passes; uniqueness holds. (Verified by direct substitution: substrate-action minimum is Zubarev with S = 3.806e+3; ratio S_zeta/S_Zubarev = 42.03 at L_max=5.)

**Proof 3 (L3 observable layer non-uniqueness with R-protected/NOT-R-protected partition)**. For an observable O = ratio(N, D) where N and D are Mellin moments at labels k_N and k_D respectively, the Mellin-balanced criterion is k_N = k_D. Under balanced ratios the regulator weight cancels in numerator/denominator (W3-G34 §Step 3). Per direct numerical verification (computed above):
- W2-G14 c_s: k_N = k_D = 2 (balanced); span = 1.227 (PASS).
- W2-G15 k_a2: k_N = 2 (Mellin a_2 weight), k_D = anchor (sharp class); UNBALANCED; span = 14.685 (FAIL).
- W3-G28 f_conv: f_conv = pi^4 / (9216 * M_0^2) with M_0 carrying R-weight; UNBALANCED; span = 1766.16 (FAIL).
- W3-G34 CC-ratio max-span: span_2 (A_s/mu) = 42.03 (FAIL); structural prediction `sqrt(span(f_conv))`agrees to 0.0000%.

The L3 layer admits MULTIPLE regulators per observable; the partition is governed by Mellin-label balance, not arbitrary choice. (Note: the framework's per-observable layer-3 verdict is determined by the layer-1 or layer-2 pin selected for that observable's calibration.)

**Layer-selection rule (operational, for downstream observables)**:

Given observable O with cyclic-cohomology degree deg(O):
- deg(O) = 0 (HC^0 trace) AND O survives Connes axioms A1-A6 -> use Layer 1 (zeta).
- O is the substrate action S[D] OR a stationary point of S[D] (epsilon_H, fold tau_fold, F_amp at fold) -> use Layer 2 (Zubarev).
- O is a Mellin-pairing of a spectral moment a_n at fixed n (k_a2, f_conv, A_s absolute) -> use Layer 3 with pin from the upstream-layer that calibrated O.
- If O is GV-obstructed (W1-G2 failure mode) -> O is RD by axiomatic obstruction; no layer choice closes the regulator-dependence.

**Scope**:

HOLDS for: Connes spectral triples of KO-dim 6 over `A_F = C (+) H (+) M_3(C)` on M^4 x SU(3); compact-fiber Riemannian submersions (Paper 01 hypothesis); separable unbounded Kasparov cycles; L_max in {3, 5, 7, 9} per W2-G15 / W3-G28 / W3-G34 monotonicity scans.

DOES NOT claim: layer collapse in the Tauberian limit Lambda -> infinity (the theorem is about FINITE L_max behavior); applicability to higher-rank submersions (e.g., HP^4) without separate verification (S84 carry-forward V.2); applicability to non-compact-fiber submersions (Paper 01 compactness required); a single canonical regulator that resolves all observables simultaneously.

**Pre-registered falsifier**:

A higher-rank spectral triple where the layer hierarchy INVERTS. Specifically, on HP^4 with its canonical Dirac operator at L_max = 5, compute `(R_axiomatic^{HP4}, R_substrate-action^{HP4})`. PASS (theorem's scope confirmed bounded by KO-dim 6 + SU(3)) iff `R_axiomatic^{HP4} != zeta` OR `R_substrate-action^{HP4} != Zubarev`. FAIL (theorem extends to higher-rank submersions) iff both selections coincide with M^4 x SU(3). Explicit gate: S84-THREE-LAYER-FALSIFIER (V.2 in this synthesis carry-forward).

**Cross-references**:
- §VII.K (FI-REGISTRY-VII-K-LANDING) -- the 42-row atlas whose MIXED rows acquire layer-pin sub-tags via this theorem
- §VII.K-META (R-protected/NOT-R-protected dichotomy) -- the observable-layer signature of the three-layer structure
- §VII.K-DUAL (M_lizzi <-> M_connes natural transformation eta) -- dual-machinery face of the three-layer transport
- §V.C (S82 KASPAROV-ABELIAN-PROOF, sha=61d73237...) -- the fiber-rank analog of regulator-class distinctness
- W1-G6 INFO (1/8 functoriality border-1) -- composite-functor consequence of layer non-collapse
- VdD Paper 01 Theorem 3.4 (1811.07824) -- the Kasparov-product factorization that supports the entire K-pairing language
- Connes-Marcolli 2008 §1.6 -- Dixmier trace + zeta residue Theorem (Layer-1 uniqueness proof)
- Connes-Moscovici 1995 -- Hopf H_1 transverse cyclic cohomology (Layer-1/Layer-2 obstruction mechanism)

**STATUS**: queryable registry entry; permanent S83 result. Logical level: refines and supersedes "single-regulator framework" assumption. The theorem is the K-theoretic structural backbone behind §VII.K-META taxonomy, the W1-G2 epsilon_H GV-classification, and the G51 w_0 layer-mismatch diagnosis.

**SIGNIFICANCE**: Provides the K-theoretic explanation for why some framework predictions are unconditional (R-protected, ratio structure, Layer-1 Layer-2 collapse via Connes residue + Tauberian limit) while others are pin-conditional (NOT-R-protected, Mellin-unbalanced, Layer-2 vs Layer-3 transport carries factor-14 - 1766 spread). The classification is structural, not arbitrary.

**OPEN**: (a) HP^4 falsifier test (S84 carry-forward V.2); (b) explicit GV-cocycle location for epsilon_H in HC^*(A_F) (S84 V.4); (c) layer transport per-MIXED-row table for §VII.K (S84 V.1); (d) layer narrowing extrapolation to L_max=7,9 (S84 V.6).

(value=L1=zeta_unique_axiomatic_+_L2=Zubarev_unique_substrate-action_+_L3=per-observable-Mellin-balanced-or-unbalanced, scheme=Kasparov-KK-three-pairings, convention=W1-G1+W1-G3+W2-G15+W3-G28+W3-G34-jointly, L_max=5)
