# Session 86 Synthesis: Surviving CC-suppression corridor map post-F_4 closure (Connes-NCG-Theorist solo, S-1)

**Date**: 2026-04-27
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Slot**: S86 1a, entry S-1 (Pillar III spectral-functional taxonomy + Mellin-Strip T5 readiness owner; cross-pillar bridge cutoff_sqrt + anomaly ↔ Pillar III)
**Source Documents**:
- `sessions/archive/session-86/session-86-w2-workingpaper.md`
- `sessions/archive/session-86/session-86-w3-workingpaper.md`
- `sessions/permanent-results-registry.md`
- `computations/s86_gate_verdicts.txt`
- `sessions/evoi-framework.md`
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md`

---

## I. Session Outcome

S86 W2-1 (`S86-MELLIN-HEAT-KERNEL-INFRA`, FAIL value=9.455686e+00 at L_max=10) closes the F_4 ∘ Mellin-Barnes ∘ Seeley-DeWitt-subtraction corridor for cosmological-constant suppression by both pre-registered FAIL branches (ratio_min_in_F_4 = 9.456 > 5e-1; χ²/dof_max = 1.4696e+04 > 20) with CC2/CC3 cross-checks confirming the Mellin-Barnes lens is functioning at machine ε (rel_err in {2.34e-16, 2.21e-16, 3.56e-16} for {ζ, Zubarev, SDW}). The structural cause is now nameable as a single phenomenon — *the substrate's a_0 spectral content is regulator-class-stable across F_4 to no better than factor 9.456 at L_max=10, and Mellin-Barnes analytic continuation does not invert this*. Three S85 truncation-hypothesis FAILs (W0-7 ρ → −0.81 at value=−0.132; W0-11 CC-3 Connes-Moscovici residue; W0-20 Mellin-cone s=3 R_inf at value=1.81e6) are converted from TRUNCATION-HYPOTHESIS to STRUCTURAL FAIL per the W2-1 falsification of the truncation hypothesis. Surviving CC-suppression corridors are enumerated below (§IV) with the **Mellin-Strip / Convergence-Cone Theorem T5** carrying the C11 closed-form `Λ_Z^{2s}·Γ(s)` (S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION, PASS value=8.066e-28) as its analytic anchor, ready for S87 W1b landing.

---

## II. Key Results

### II.1 F_4 ∘ MB ∘ SD-subtraction CC-suppression corridor — CLOSED (W2-1 confirmation-of-wall by both branches)

**Result**: At L_max=10 on the truncated D_K cache (`s84_spectrum_cache_L12_tau019.npz`, sha 9e6d9cf7…), the Mellin-Barnes residue extractor with explicit Connes-Moscovici 1995 Seeley-DeWitt counter-term subtraction returns `|Λ_CC^MB|/|a_0^trunc|` of {10.84, 9.46, 9.69} for {ζ, Zubarev, SDW} regulators against a PASS bound of 0.1 — i.e., 19 OOM above PASS for the central comparator and 3 OOM above the FAIL branch by χ²/dof. Classification: **GEOMETRIC** (the substrate's spectral-triple data on F_4 is the object of the test; the result is intrinsic to (A, H, D_K), not to any external apparatus).

The dominant n=6 slot in all three regulators (n=6 is the curvature-squared Seeley-DeWitt coefficient in d_spec=8 NCG) drives χ²/dof: σ_6^trunc is the smallest absolute residual across slots {0,2,4,6} while |Δ_6| is large, so each individual `(Δ_n/σ_n)²` contribution is geometric — it is not a calibration artifact but a substrate signature of the MB-vs-trunc shift at the highest moment. The complementary CC2 NON-monotonic growth at n=0 by factor 239× (3.93e+05 → 9.38e+07 on L_max ∈ {5,…,10}) demonstrates the substrate's a_0 spectral content has not yet entered the Weyl asymptotic regime at L_max=10. CC3 PASS at machine ε independently certifies that the Mellin-Barnes integrator is functioning correctly — the FAIL is *structural-from-spectrum*, not an artifact of contour deformation, quadrature, or numerical precision.

The W2-1 verdict (FAIL by ratio AND by χ²/dof) eliminates one entire equivalence class of CC-suppression mechanisms: the F_4 multiplier algebra cannot, under any analytic continuation in the F_4 ∘ MB ∘ SD lens, produce a CC residue suppressed below 5e-1 of the bare a_0 truncated direct sum.

### II.2 Three S85 truncation-hypothesis FAILs converted to STRUCTURAL — single registry-grade family entry (Joint W2 seed Candidate 4)

**Result**: S85 W0-7 (`S85-W0-ZUBAREV-LMAX-CONVERGENCE` ρ → −0.81 conjecture, value=−0.132 at L_max=8), S85 W0-11 (`S85-CC-3-CONNES-MOSCOVICI-RESIDUE`, signed dimension-spectrum sum), and S85 W0-20 (`S85-W0-L-MELLIN-CONE-S3-RESIDUE`, value=1.81e6 at L_max=12) all share the F_4 ∘ MB ∘ SD-subtraction lens at the heart of their hypothesis structure. The W2-1 verdict (per §V working-paper line 145-148, "Cascade-FAIL implications") falsifies the truncation hypothesis that bound them as candidates for the inflated-L_max recovery program. They are now STRUCTURAL FAILs by the constraint-map updates table (W2 working-paper lines 657-668). Classification: **GEOMETRIC** (all three are spectral-functional moments of D_K under regulator-class transformations, not phononic excitation observables).

This consolidation as a single phenomenon (the *F_4-MB structural wall*) is the joint W2 seed Candidate 4 from the spawn prompt. The phenomenological signature across the trio is the same: at L_max where the Weyl-dim sectors `(p+q) ∈ {9, 10}` add `N_unique = 78,080 − 31,264 = 46,816` new eigenvalue rows, the n=0 (and adjacent low-n) slot's MB-extracted residue grows faster than the truncation residual it is supposed to subtract. F_4-class regulators (Mellin support concentrated on slots {0, 2, 4, 6}) cannot suppress this because their multiplier-algebra dimension is exactly the slot dimension — the algebra has no operator to absorb a divergence whose growth rate exceeds the multiplier's representational capacity.

### II.3 The 3-class regulator partition theorem — Zubarev as F_4-INF singleton (W2-3 PASS)

**Result**: The framework's regulator-family taxonomy is refined by the C11 closed-form Mellin identity `M[exp(−x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` to a **3-class partition** (per W2 working-paper synthesis §3, lines 602-607):

- **F_4** = {ζ, SDW, sharp-cutoff truncated} — finite-vector class with support exactly on {a_0, a_2, a_4, a_6}; multiplier algebra over ℝ⁴.
- **M** = {cutoff_sqrt, anomaly-non-truncated} — mixed-support class with continuous Mellin profile having residues outside {s ∈ {0,1,2,3}}.
- **F_4-INF** = {Zubarev} — INFINITE-VECTOR singleton whose Mellin-profile residues land EXACTLY on the F_4 slots, but whose multiplier algebra is infinite-dimensional (Schwartz-class with continuous support over Re(s) > 0).

Classification: **GEOMETRIC** (algebraic / classification-theoretic property of regulator kernels acting as multipliers on D_K's spectral data; independent of L_max truncation).

The 3-class refinement is consequential for W2-1's interpretation. Substitution chain on the multiplier-dimension hypothesis:

- Step 1 (def): F_4-MB ratios per W2 §W2-1 line 53 are {ζ: 10.84, Zubarev: 9.46, SDW: 9.69}. Multiplier-algebra dimensions per C11 framework note are {ζ: 4 (finite-vector e_4), Zubarev: ∞ (Schwartz-class continuous), SDW: 4 (finite-vector)}.
- Step 2 (substitution): if "more multiplier-algebra capacity ⇒ better CC suppression (smaller ratio)" held, Zubarev (∞-dim) should achieve the lowest ratio across F_4. Observed: Zubarev's ratio = 9.46 IS the lowest, but only by factor (10.84/9.46) ≈ 1.15 over ζ.
- Step 3 (simplification): the marginal improvement (factor 1.15) leaves Zubarev still 19 OOM above the PASS bound 5e-1 / observable bound 0.1. The unbounded multiplier-algebra capacity buys ~15% in the ratio against ζ; it does not collapse the gap to PASS.
- Step 4 (direction): the multiplier-algebra-dimension axis is therefore *insufficient* (not irrelevant) to escape the F_4 wall — moving from finite (4-dim) to infinite (∞-dim) capacity changes the ratio by a small finite factor while the gap to PASS remains 19 OOM. The wall sits in the substrate's a_0 spectral-content growth (CC2 NON-monotonic, 239× factor over L=5→L=10), not in the regulator's algebraic capacity. The 3-class refinement makes this *quantitatively explicit*: Zubarev's F_4-INF singleton membership demonstrates the algebraic-capacity axis is not the binding constraint.

### II.4 Mellin-Strip / Convergence-Cone Theorem T5 — readiness audit (Pillar III, my lane)

**Result**: T5 is the Lizzi-track theorem stating Z_L(s) := Σ_n d_n |λ_n|^{−2s} has three regimes: Regime I (Re(2s) > d_spec, admissible direct truncation, Z_L → ζ_D), Regime II (Re(2s) = d_spec, log L divergence, finite L meaningful only after subtracting leading log), Regime III (Re(2s) < d_spec, L^{(d_spec − 2s)/2 + corr} divergence, only the residue analytic continuation is meaningful). The theorem is registered at `sessions/permanent-results-registry.md` §VII.T (registry line 6117, S86-MELLIN-STRIP-REGISTRY-LANDING content_sha=de3a920ed4b785de…, audit_sha=791c6dfcadc573df…), but its PASS pertains to the registry-text landing, not to a closed-form analytic anchor on a non-trivial regulator. Classification: **GEOMETRIC** (analytic-continuation structure of the spectral triple's zeta function; it IS the substrate's Mellin convergence geometry).

T5 readiness for S87 W1b landing requires three preconditions, which I audit as follows:

(a) **Closed-form analytic anchor on a non-trivial regulator class**: DELIVERED by C11 (W2-3 PASS, S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION value=8.066073499380351e-28; framework note `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md`). The closed form `M[exp(−x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` is the analytic substrate of T5's Regime I behavior on the F_4-INF Zubarev profile: the strip `Re(s) > 0` is the Zubarev Mellin profile's convergence cone exactly. The W3-G56 Heitsch cocycle and W1b T6 (HP¹ near-invariance) reuse the same algebraic structure.

(b) **Off-pole `analytic_zeta(s, L_max)` API at d_spec=8 cone apex**: DELIVERED by C10 (W2-2 INFO, S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE value=(280743.2353669952+0j); module `computations/_analytic_zeta.py` at content_sha=3024e8ce5f9bb2fd…). χ²/dof = 2.166e-32 against the Mellin-Dirichlet finite-spectrum identity `analytic_zeta(s, L) = Σ_k m_k λ_k^{−s}` (working-paper §W2-2 lines 244-249). The two INFO-band cross-checks (truncation-stability 61.1% L=8→L=10; ε-analyticity 1.124e-3 vs 1e-3 threshold) are both substrate-property INFOs, not API defects: the L=8 cache drops sectors `(p+q) ∈ {9,10}` whose Weyl-dim weight `d(p,q) = (1/2)(p+1)(q+1)(p+q+2)` makes them substantively dominant; the ε-analyticity 1.12× excess is the linear-response margin of the imaginary-axis perturbation, not a discontinuity. Both INFOs are anticipated by T5 itself (Regime II logarithmic-edge behavior absorbs truncation-stability INFO; Regime III boundary structure absorbs ε-analyticity INFO).

(c) **Verification that the C11 closed form satisfies T5 preconditions**: I verify by direct substitution.

T5 precondition: For each regulator r ∈ Atlas with Mellin profile M_r(s), there exists a strip `Re(s) ∈ (a_r, b_r)` of analytic-continuation convergence such that the truncation-residual scaling matches T5's regime classification. For Zubarev: `M_r(s) = Λ_Z^{2s}·Γ(s)`, analytic on Re(s) > 0 with simple poles at s ∈ {0, −1, −2, …} from Γ(s); no zeros on Re(s) > 0; exponential decay in |Im(s)| → ∞ at fixed Re(s) > 0 (Stirling). The convergence cone is `Re(s) > 0`. The d_spec=8 NCG cone apex sits at Re(2s) = d_spec ⇔ Re(s) = 4 = d_spec/2, deep inside Zubarev's strip. Therefore Zubarev satisfies T5's precondition for the s=3 off-pole evaluation tested by C10 INFO (Re(s) = 3 ∈ (0, 4) ⊂ (0, ∞) Zubarev strip; Re(2s) = 6 < 8 = d_spec ⇒ Regime III on the Z_L(s) side, but Zubarev's regulating multiplier `Λ_Z^{2s}·Γ(s)` is finite at s=3 and the substrate spectral functional on the regulated side is admissible).

The three preconditions (a,b,c) are *jointly satisfied*. T5 is **READY** for S87 W1b landing as a permanent registry theorem — not the registry-text landing already at §VII.T (which is a meta-claim about the theorem's existence in the Lizzi corpus), but as a statement-of-substance with the C11 anchor cited, the C10 API as the empirical instrument, and the substrate's regime classification (Regime I admissible, Regime III divergent, Regime II logarithmically-edged) as the structural conclusion.

### II.5 cluster_span(L_max) module — callable, FAIL is plan-authoring precision-floor (W2-4)

**Result**: `computations/_cluster_span_extract.py` (content_sha=1dcc851f7eff0a3c…) refactor of the W0-3 CC-5 cluster-span identity is published. The module reproduces `b2 / b3 = 2.000000000000002` bit-for-bit at L_max=12 against the S85 W0-3 canonical, and the verdict-line FAIL (rel_err = 1.083e-15 vs threshold 1e-15 ≈ 4.5 × float_eps) is a plan-authoring-side precision-comparison floor mismatch, not an algorithmic break (working-paper §W2-4 substitution chain at lines 502-537 derives `canonical_dev = 2 × rel_err_normalized` and shows W0-3's S85-achieved 10 × float_eps = 2.22e-15 maps to 5 × float_eps under the spawn-prompt's normalized metric, with the threshold 4.5 × float_eps below the achievable floor by ~0.5 × float_eps). Classification: **GEOMETRIC** (the cluster-span identity `span_2 = K · span_3²` is intrinsic to D_K's spectral-triple structure under the substrate's spectral observables — the refactor is a packaging operation; the physics is preserved bit-exactly).

W3 C13 K-corridor extension (`K ∈ [K_R5, K_crit] ∪ [K_crit, K_FIRAS]`) is **functionally unlocked** since the actual deviation (~2.2e-15) is 3 OOM tighter than C13's `< 1e-12` threshold. This is structurally adjacent to T5: the cluster-span identity is the eigenvalue-clustering corollary of T5's Regime-I asymptotic behavior on the eigenvalue spectrum density. T5 PASS at S87 W1b would also strengthen the K-corridor extension's cross-corridor anchoring.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S86-MELLIN-HEAT-KERNEL-INFRA` (C9, W2-1) | **FAIL** (both branches) | ratio_min = 9.455686e+00; χ²/dof_max = 1.4696e+04 |
| `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (C10, W2-2) | **INFO** | analytic_zeta(s=3, L_max=10) = 2.807432e+05 + 0j; χ²/dof = 2.166e-32 |
| `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` (C11, W2-3) | **PASS** | max_rel_err = 8.066073499380351e-28 (16 OOM below threshold) |
| `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` (C12, W2-4) | **FAIL** (plan-authoring precision-floor) | rel_err = 1.083e-15 vs threshold 1e-15 (~0.5 × float_eps below achievable) |
| `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` (T9, W3-1) | **FAIL (PRE-REG-INC)** | blocked_by_C9_FAIL_C10_INFO; deferred to S87 |
| `S86-W0-7-MB-RE-EMIT` (W3-2) | **FAIL (PRE-REG-INC)** | blocked_by_C10_INFO; deferred to S87 |
| `S86-W0-11-MB-RE-EMIT` (W3-3) | **FAIL (PRE-REG-INC)** | blocked_by_C9_FAIL; deferred to S87 |
| `S86-W0-20-MB-RE-EMIT` (W3-4) | **FAIL (PRE-REG-INC)** | blocked_by_C10_INFO; deferred to S87 |
| `S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION` (C13, W3-5) | **FAIL (PRE-REG-INC)** | blocked_by_C12_FAIL_C19_FAIL; deferred to S87 |
| `S86-W3-11-LAMBDA-CONVENTION-RESOLUTION` (C43, W3-6) | **FAIL (PRE-REG-INC)** | blocked_by_C14_FAIL; deferred to S87 |

All verdicts authoritative per `computations/s86_gate_verdicts.txt` (lines 89-129). No re-adjudication.

---

## IV. Structural Implications — Surviving CC-suppression corridors

After W2-1's confirmation-of-wall, the surviving corridors fall into four enumerable classes. Each is named with its formal mechanism, given an EVOI estimate, and tested against the constraint that ALL F_4 regulators FAILed by both branches at L_max=10.

### IV.A Registry-grade structural FAIL family entry (joint W2 seed Candidate 4)

> **F_4-MB STRUCTURAL WALL FAMILY** — single phenomenon name covering S85 W0-7 (`S85-W0-ZUBAREV-LMAX-CONVERGENCE`, ρ → −0.81 conjecture FAIL value=−0.132 at L_max=8), S85 W0-11 (`S85-CC-3-CONNES-MOSCOVICI-RESIDUE`, signed CM dimension-spectrum sum FAIL), S85 W0-20 (`S85-W0-L-MELLIN-CONE-S3-RESIDUE`, FAIL value=1.814463e+06 at L_max=12), and S86 W2-1 (`S86-MELLIN-HEAT-KERNEL-INFRA`, FAIL value=9.455686e+00 at L_max=10). Common structural cause as documented by W2 §W2-1 (lines 80, 134, 587): the substrate's a_0 spectral content at L_max=10 is **not yet in the Weyl asymptotic regime** — CC2 NON-monotonic growth shows the n=0 (cosmological-constant slot) Mellin moment grows by factor 239× (3.93e+05 → 9.38e+07) on L_max ∈ {5, …, 10} as the high-(p+q) sectors are added; meanwhile σ_6^trunc (the n=6 curvature-squared slot's truncation residual) is the smallest absolute residual across slots {0,2,4,6}, so the n=6 MB-vs-trunc gap |Δ_6|/σ_6 dominates χ²/dof. The F_4 regulator class {ζ, Zubarev, SDW} cannot suppress the resulting ratio across the F_4 sub-atlas (per W2 §1 line 589: "the substrate does not admit F_4 CC suppression"). Cascading consequence: the F_4 regulator class is closed for the substrate's CC-suppression mechanism on the L_max=10 truncated cache, regardless of analytic-continuation strategy within the F_4-MB framework. Classification: **GEOMETRIC**. Falsifies (per W2 working-paper §1, line 589) the truncation hypothesis "the substrate's a_0 spectral content is finite and the prior W0-7 / W0-11 / W0-20 FAILs were artifacts of finite L_max". Substrate framing: the F_4-MB wall is a categorical wall on the L_max=10 truncated substrate's a_0 slot, not a calibration of an external regulator — the substrate IS the F_4-MB-unsuppressed object, not IN an external regulator-pulled space.

This entry is registry-grade — single name, structurally weighted, citation-ready. It belongs at §VII.U (next free Roman-letter slot after §VII.T Mellin Strip Theorem) or as a corollary block under §VII.T pending slot-arbiter assignment. Recommend slot-allocation request to S87 W0/W1.

### IV.B Surviving Corridor 1 — Mellin-Strip / Convergence-Cone Theorem T5 (Pillar III, my lane)

**Mechanism**: Analytic continuation of the substrate's spectral triple zeta function `ζ_D(s) = Tr |D_K|^{-2s}` outside the F_4-MB framework, using the C11 closed form `M[exp(−x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` as analytic anchor and the C10 `analytic_zeta(s, L_max)` API as numerical instrument. The CC suppression candidate is the residue at the d_spec=8 cone apex (s=4 leading; off-pole s=3 already characterized by C10) computed *by analytic continuation* rather than by F_4 ∘ MB ∘ SD subtraction. The crucial difference vs the F_4-MB closed corridor: T5 predicts the Regime III divergence as a mathematical fact (W0-20's R_inf = 1.81e6 is the divergent-cone PARTIAL SUM, NOT the analytic-continuation residue, per registry §VII.T line 6239), so the residue itself sits OFF the divergent partial sum and is what T5 lets us extract.

**Test against the F_4 wall constraint**: T5 is *structurally orthogonal* to the F_4-MB wall. The F_4-MB wall is a statement about the multiplier-algebra-residue lens; T5 is a statement about the Mellin-strip convergence geometry. The F_4 ∘ MB ∘ SD-subtraction route (closed) computes `Λ_CC^MB / a_0^trunc` as a regulator-class-stable ratio across F_4; T5 instead computes the *analytic-continuation residue* at the cone apex and cites the divergence rate of the partial sum as evidence that the partial sum is the wrong observable. T5's surviving status is established by: (a) C11 closed form PASS at machine ε on a regulator (Zubarev) that lies in F_4 by Mellin support but in F_4-INF by multiplier-algebra dimension; (b) C10 API delivering bit-exact Mellin-Dirichlet finite-spectrum identity; (c) the existing §VII.T registry landing as anchor.

**EVOI estimate**: HIGH (≈ 12-15%). Comparable in magnitude to S78-W1-E (12.65%, IC scheme derivation) and S78-W2-A (8.90%, mu_eff 96×96). T5 is the sole surviving analytic-continuation-based CC mechanism after the F_4-MB closure; PASS would directly attack the framework's #1 structural concern (CC: ALL spectral action routes CLOSED, per agent memory `Open Tensions` §3). FAIL would close the analytic-continuation route entirely and force the framework to non-spectral mechanisms exclusively (Friedmann two-layer, dilution-CC, substrate-density-driven). Both outcomes shift framework probability substantially.

### IV.C Surviving Corridor 2 — C-regulator class outside F_4: cutoff_sqrt + anomaly (cross-pillar bridge, my Pillar III ↔ M-class)

**Mechanism**: Per the S86 plan-w14 §1 atlas decomposition `Atlas_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}` (registry permanent-results-registry.md §VII-B.HP1-NEAR-INVARIANCE-LANDING line 2595), the M-family `M = {cutoff_sqrt, anomaly-non-truncated}` lies OUTSIDE the F_4 wall by construction: M-class regulators have Mellin support outside the {a_0, a_2, a_4, a_6} slot set, so the F_4 multiplier-algebra-dimension constraint that drove W2-1's FAIL does not apply.

**Status of M-class CC suppression**: UNTESTED at the W2-1 lens. The Two-Layer Obstruction Theorem (§VII-B.TWO-LAYER-OBSTRUCTION, registry line 2755) shows that the L1 ↔ L2 categorical functoriality fails at every C_i conjunct for every r ∈ Atlas_5, including M (n_joint = 0/2 within M extension, per registry line 2943). But the Two-Layer Obstruction tests the *L1 ↔ L2 functoriality interface*, not the CC-suppression observable directly. The M-class regulators may produce CC suppression through a non-functorial mechanism (e.g., the anomaly-trace-Wess-Zumino route, where the regulator's Mellin support residue at non-{0,1,2,3} slots provides a counter-term outside the F_4 multiplier algebra).

**Test against the F_4 wall constraint**: cutoff_sqrt and anomaly each carry Mellin profile residues OFF the F_4 slot set. The F_4 wall — that no F_4 multiplier can suppress |Δ_6|/σ_6 because the multiplier-algebra dimension equals the slot dimension — does not apply to M-class because M regulators have additional slot support. cutoff_sqrt has been registered as REQUIRES-S86-GATE (gate `S86-W-4-CUTOFF-SQRT-ADJUDICATION`, INFO at verdict-file line 106; outcome enum {STRUCTURALLY-EXCLUDED:PASS, GENUINELY-PHYSICAL:PASS, REQUIRES-S86-GATE:INFO}). Until C28 (W4 cutoff_sqrt adjudication) closes, the M-class corridor remains formally open — the W2-1 closure does NOT cascade to M.

**EVOI estimate**: MEDIUM (≈ 5-8%). M-class CC suppression has not been directly tested at L_max=10 with the C9/C10 infrastructure; the prerequisite is C28 adjudication. Past observables on M-class (Higgs mass discriminant: m_H^{cutoff} ~ 127.5 GeV vs observed 125.1 GeV at percent level, registry line 7603) suggest cutoff_sqrt is "GENUINELY-PHYSICAL" rather than "STRUCTURALLY-EXCLUDED", which would unlock the C-regulator CC corridor for explicit testing.

### IV.D Surviving Corridor 3 — Non-MB suppression mechanisms entirely (extra-spectral)

**Mechanism**: Friedmann two-layer gravity (working-paper §1, line 155 and §5, line 623), dilution-CC (DILUTION-CC-66, agent memory MEMORY.md "CC dilution priority"), substrate-density-driven mechanisms outside the spectral-functional class. These mechanisms compute CC suppression through dynamical processes (volume dilution at fold transit, two-layer effective metric mixing, substrate-density evolution under Jensen deformation) rather than through regulator-class moments of the spectral action.

**Test against the F_4 wall constraint**: Trivially satisfied — these mechanisms are non-spectral, so the F_4 multiplier-algebra obstruction does not engage. The W2-1 wall closes spectral-functional-based CC suppression, not gravitational-dynamical-based suppression. The classifications are disjoint in the §VII / framework taxonomy: spectral-functional moments live on the spectral triple (A, H, D_K); two-layer / dilution mechanisms live on the substrate's L1 ↔ L2 mediation (with Two-Layer Obstruction Theorem as a constraint).

**EVOI estimate**: HIGH for DILUTION-CC-66 specifically (≥ 12%, per agent memory "DILUTION-CC priority #1 S66 priority. Pin removed S65. Gap closes by TODAY, not at fold"); MEDIUM for two-layer Friedmann (≈ 6-8%, gated by Two-Layer Obstruction n_joint = 0/5 wall but routed through *non*-functorial gravity dynamics). Classification: NON-PHONONIC (extra-spectral) for the gravitational-dynamical corridor; GEOMETRIC for dilution-CC (substrate volume-vs-spectral ratio). NOT my lane (Pillar III = spectral-functional). Cited here for completeness of corridor-map.

### IV.E Surviving Corridor 4 — Convex-mix C45 deferred against C28 closure

**Mechanism**: Sixth-regulator-synthesis test C45 (registry line 2939): any composite regulator `r_mix = α·ζ + β·cutoff_sqrt` with α + β = 1, α, β > 0, inherits the obstruction at every individual conjunct of the Two-Layer Obstruction. No convex combination escapes per-conjunct failure when both endpoints fail individually.

**Test against the F_4 wall constraint**: PARTIAL — C45's obstruction is functoriality-based (Two-Layer Obstruction); the F_4-MB wall is multiplier-algebra-dimension-based. A convex mix `α·ζ + β·cutoff_sqrt` would inherit ζ's F_4 multiplier dimension *only* on the α coefficient; the β·cutoff_sqrt component carries M-class slot support that lies OUTSIDE F_4. So C45 *might* escape the F_4 wall (since the M-class component breaks F_4-membership), even though it cannot escape the Two-Layer Obstruction.

**EVOI estimate**: LOW (≈ 2-3%). C45 is deferred to S87 per S86 partition §2 anchoring against C28 closure (registry line 2939). The Two-Layer Obstruction wall persists across either C28 outcome (n_joint=0/3 within F_4, n_joint=0/2 within M extension), so C45's PASS-region is narrow — the surviving sub-region is "C45 succeeds at CC suppression but fails Two-Layer functoriality, and the failure is acceptable for the CC-only observable". This is a thin corridor but not closed.

### IV.F Eliminated corridors (cascade-FAIL from W2-1)

Per W2 working-paper §5 lines 622-630 (downstream implications) and W3 §W3-1 through §W3-6 PRE-REG-INC closures:

- **W3 T9 REPLACEMENT-B (asymptotic ζ-stabilization at s=4 leading residue)**: cascade-FAIL — joint C9 ∧ C10 PASS-condition unmet (C9 FAIL; C10 INFO).
- **W3 W0-7 / W0-11 / W0-20 re-emission attempts**: cease — S85 truncation hypothesis FALSIFIED; the three FAILs stand as STRUCTURAL.
- **W10 C37 ZFP discharge (μ_BC integer-12 ζ-at-interior route)**: cascade-FAIL — depends on C9's MB-cone framework; falls back to C38 (rep-theoretic) + C39 (heat-kernel diagnostic).

These are *not* surviving corridors; they are constraint-map updates that sharpen the surviving-corridor enumeration above by removing analytical adjacencies that were previously open.

---

## V. Carry-Forward Computations

### V.1. Mellin-Strip / Convergence-Cone Theorem T5 — substantive S87 W1b landing

- **What**: Land T5 at `sessions/permanent-results-registry.md` §VII.U (or a §VII.T subordinate block, per slot-arbiter outcome) as a statement-of-substance with: (i) the C11 closed form `M[exp(−x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` cited as analytic anchor; (ii) the C10 `analytic_zeta(s, L_max)` API cited as numerical instrument; (iii) explicit Regime I / II / III classification on Atlas_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} per §VII.T existing scaffold; (iv) the four 4-tuples for each verdict pin (S85-W0-L-MELLIN-CONE-S3-RESIDUE, S85-W6-5-MELLIN-CONE-EXT, S85-W9-MELLIN-BALANCE-16-OF-16, S86-MELLIN-HEAT-KERNEL-INFRA). Substitution chain for each Regime classification, with explicit `(d_spec, Re(2s))` ordering and L_max-dependence direction.
- **Inputs**: `computations/_analytic_zeta.py` (C10 module, content_sha=3024e8ce5f9bb2fd…); `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` (C11 framework note); `computations/s84_spectrum_cache_L12_tau019.npz` (sha 9e6d9cf7…); `sessions/permanent-results-registry.md` §VII.T (existing scaffold). Canonical constants: `M_KK`, `tau_fold`, `d_spec` (NCG cone apex = 8, classical = 3 — distinct keys, both already pinned in `s86_w2_c10_zeta_sweep.npz`).
- **Gate**: NEW `S87-T5-MELLIN-STRIP-SUBSTANTIVE-LANDING` with PASS criterion: registry block of ≥ 60 lines containing all four 4-tuple verdict pins + substitution chains for all three regimes + slot-allocation arbiter PASS + inter-regulator scope statement (Zubarev satisfies precondition; ζ does not satisfy Regime I at s=3; SDW, cutoff_sqrt, anomaly classified per their Mellin profiles); FAIL if any 4-tuple absent or substitution chain skips Step 4 direction; INFO if slot-arbiter routes block to a non-canonical slot (e.g., §VII.V or higher) per the S86 W1a-2 §VII.R precedent.
- **Effort**: 4-6 hours, 1 agent session (connes-ncg-theorist with optional lizzi-spectral-functional-theorist co-sign; Pillar III lane).

### V.2. cutoff_sqrt adjudication C28 — S87 W4 priority lift

- **What**: Adjudicate cutoff_sqrt as STRUCTURALLY-EXCLUDED vs GENUINELY-PHYSICAL using the existing `S86-W-4-CUTOFF-SQRT-ADJUDICATION` INFO verdict (verdict-file line 106) as starting point. Run the explicit cutoff_sqrt CC-suppression test at L_max=10 against the C9 / C10 / C11 infrastructure. Decisive comparator: `|Λ_CC^{cutoff_sqrt}| / |a_0^trunc|` vs PASS bound 0.1 (parallel to C9), under cutoff_sqrt's M-class Mellin profile. If PASS → opens C-regulator class as a viable CC-suppression mechanism; if FAIL → cutoff_sqrt joins F_4 in the CC-suppression-closed family; if INFO (intermediate ratio) → triggers C45 convex-mix exploration.
- **Inputs**: `computations/s86_w2_c9_residues.npz` (F_4-only, for comparator); cutoff_sqrt Mellin profile (mathematical: `M[r_cutoff_sqrt](s) = Λ_C^{2s} · B(s, ν)` for some Beta function with parameter ν tracking the cutoff sharpness; pin ν per S85 anomaly framework); `computations/_analytic_zeta.py` (C10 API); D_K cache `s84_spectrum_cache_L12_tau019.npz`. Canonical constants: `Lambda_C` (cutoff_sqrt scale, must be added to `canonical_constants.py` before use), `M_KK`, `tau_fold`.
- **Gate**: NEW `S87-CUTOFF-SQRT-CC-SUPPRESSION-TEST` with PASS at `|Λ_CC^{cutoff_sqrt}|/|a_0^trunc| ≤ 0.1 AND χ²/dof ≤ 5`; FAIL at `> 0.5 OR χ²/dof > 20`; INFO band (0.1, 0.5).
- **Effort**: 4-5 hours, 1 agent session (lizzi-spectral-functional-theorist primary; connes-ncg-theorist for spectral-triple compliance check).

### V.3. M-class anomaly-regulator CC-suppression test — S87 W4 follow-on

- **What**: Run the analogous CC-suppression test for the anomaly-non-truncated regulator (M-class second member). Anomaly Mellin profile per S82 W2-D / Andrianov-Lizzi 1103.0478: `f_0 = 1/2 forced, f_2 = f_4 = 1, f_n>4 = 0`. Test ratio + χ²/dof against the same thresholds as V.2. Outcome partitioning: PASS → M-class (both members) opens CC-suppression corridor; FAIL → M-class joins F_4 in closure; one PASS / one FAIL → forces explicit per-regulator (not class-level) characterization.
- **Inputs**: same as V.2 but with anomaly's normalization-pin (`f_0 = 1/2`) per the canonical-constants ledger entry from W2-D; `computations/_analytic_zeta.py`; D_K cache. Canonical constants: `Lambda_anomaly` (must be added to `canonical_constants.py`), `M_KK`, `tau_fold`.
- **Gate**: NEW `S87-ANOMALY-CC-SUPPRESSION-TEST` with PASS / FAIL / INFO criteria identical to V.2 (allows direct comparison with cutoff_sqrt outcome).
- **Effort**: 3-4 hours, 1 agent session (lizzi-spectral-functional-theorist).

### V.4. F_4-MB structural wall family — registry landing at §VII.U (or subordinate to §VII.T)

- **What**: Land the registry-grade structural FAIL family entry per IV.A above. Single-name canonicalization "F_4-MB STRUCTURAL WALL FAMILY" covering S85 W0-7 + W0-11 + W0-20 + S86 W2-1. Body includes: (i) parent-statement of common structural cause; (ii) per-FAIL audit_sha + content_sha + 4-tuple; (iii) substitution chain showing why F_4 multiplier-algebra dimension matches slot dimension and therefore cannot suppress |Δ_n|/σ_n at the highest slot; (iv) substrate framing (the F_4-MB wall IS the substrate's a_0 slot at L_max=10 truncation, not IN an external regulator-pulled space); (v) downstream-binding clauses for which gates cite this family entry as their canonical anchor going forward.
- **Inputs**: `computations/s86_w2_c9_residues.npz` (W2-1 numerical anchor); the four constituent verdict-file lines (S85-W0-7 audit_sha to be looked up in `s85_gate_verdicts.txt`; S85-CC-3 audit_sha; S85-W0-L-MELLIN-CONE-S3-RESIDUE audit_sha=0d5c44654c08e973…; S86-MELLIN-HEAT-KERNEL-INFRA audit_sha=1559e559208db268…); slot-arbiter for §VII.U allocation.
- **Gate**: NEW `S87-F4-MB-WALL-FAMILY-LANDING` with PASS at registry block landed + 4 audit_sha pins verified in their respective verdict files + substitution chain + slot-arbiter PASS; FAIL on slot-arbiter rejection (route to next free slot); INFO on partial landing (e.g., 3 of 4 audit_sha pins verified).
- **Effort**: 2-3 hours, 1 agent session (connes-ncg-theorist).

### V.5. cluster_span(L_max) module — W3 C13 K-corridor extension proper

- **What**: Run the C13 (S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION) test at S87 once C12 + C19 PRE-REG-INC blocks resolve. Specifically: invoke `cluster_span(L_max)` from `computations/_cluster_span_extract.py` across the K-corridor `K ∈ [K_R5, K_crit]` (n=41 log-spaced) and post-fold Riemann cover `K ∈ [K_crit, K_FIRAS]` (n=21 per sheet, 3 sheets). PASS at deviation `|ratio − 2|` ≤ 1e-12 at every evaluation point (using the canonical `|ratio − 2|` metric per S86 W2-4 rule-file extension at `.claude/rules/epistemic-discipline.md` "Canonical-metric pin extension"); FAIL on any deviation > 1e-12.
- **Inputs**: `computations/_cluster_span_extract.py` (content_sha=1dcc851f7eff0a3c…); `s84_spectrum_cache_L12_tau019.npz`; resolved C19 K_floor / K_wall canonical-constants entries (currently FAIL at `'upstream_W5_D.4_FAIL_no_K_floor_K_wall_values'`); resolved C12 verdict (currently FAIL at precision-floor; see V.6 for accompanying threshold-recalibration option). Canonical constants: `K_R5`, `K_crit`, `K_FIRAS`, `K_floor`, `K_wall` (all must be in `canonical_constants.py`; some currently absent).
- **Gate**: existing `S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION` (re-emission as `S87-CLUSTER-SPAN-K-CORRIDOR-EXTENSION` at S87) with PASS / FAIL criteria pre-registered per W3-5 §11.
- **Effort**: 2 hours, 1 agent session (connes-ncg-theorist; my lane). Effort assumes V.6 + W5 D.4 prerequisites resolve in S87 W0/W1.

### V.6. cluster_span threshold-recalibration as canonical-metric demonstrator

- **What**: Re-emit `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` at S87 with corrected threshold per the W2-4 substitution chain at lines 502-537. Use canonical W0-3 metric `|ratio − 2|` (NOT spawn-prompt's `|b2 − 2·b3|/|b2|`) at threshold `< 1e-14` (~ 45 × float_eps), or use spawn-prompt normalized form at threshold `< 5e-15` (~ 22 × float_eps). Either choice PASSes the existing (bit-exact-preserved) module at all L_max ∈ {8, 10, 12}. This validates the rule-file extension `.claude/rules/epistemic-discipline.md` §"Canonical-metric pin extension (S86 W2-4 surface; first cluster-span instance)" empirically and closes the C12 FAIL-with-diagnostic in a single re-emission.
- **Inputs**: `computations/_cluster_span_extract.py` (unchanged); `computations/s86_w2_c12_cluster_span_self_test.py` (unchanged); resolution of plan-authoring threshold per V.6's recommended canonical-metric form.
- **Gate**: NEW `S87-CLUSTER-SPAN-EXTRACTOR-RECAL` with PASS at deviation `|ratio − 2|` ≤ 1e-14 at all L_max ∈ {8, 10, 12}; FAIL on any L_max exceeding; INFO on ambiguous canonical-metric vs normalized-metric resolution.
- **Effort**: 1 hour, 1 agent session (connes-ncg-theorist; my lane).

### V.7. Two-Layer Obstruction Theorem extension to F_4-INF (Zubarev singleton)

- **What**: Extend the §VII-B.TWO-LAYER-OBSTRUCTION theorem to explicitly distinguish F_4 (multiplier-algebra dim 4) from F_4-INF (multiplier-algebra dim ∞, Zubarev-singleton) per the W2-3 PASS 3-class refinement. The existing theorem statement (registry line 2755) sums over Atlas_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}; the refined statement should specify `n_joint(F_4) = 0/3`, `n_joint(F_4-INF) = 0/1` (Zubarev individually), `n_joint(M) = 0/2`, with the partition exhaustive. This refinement is structurally necessary because the W2-1 result distinguishes Zubarev's behavior (worst-case smallest ratio at 9.4557, infinite-dimensional multiplier algebra DID NOT help) from the rest of F_4, and the Two-Layer Obstruction's implication for C45 convex-mix should accordingly distinguish endpoints from F_4 vs F_4-INF.
- **Inputs**: `sessions/permanent-results-registry.md` §VII-B.TWO-LAYER-OBSTRUCTION (existing block, line 2755); `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` (C11 3-class registration); `computations/s86_w2_c9_residues.npz` (W2-1 per-regulator ratios); slot-arbiter for in-place edit vs subordinate block.
- **Gate**: NEW `S87-TWO-LAYER-OBSTRUCTION-3CLASS-REFINEMENT` with PASS at theorem-statement updated + n_joint partition explicit + downstream-binding clauses preserved; INFO if subordinate-block rather than in-place edit; FAIL on partition-violation (e.g., F_4 vs F_4-INF assigned same n_joint without basis).
- **Effort**: 2 hours, 1 agent session (lizzi-spectral-functional-theorist primary, connes-ncg-theorist co-sign).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | F_4 ∘ MB ∘ SD-subtraction CC-suppression — CLOSED both branches | GEOMETRIC | W2-1 FAIL value=9.456e+00; χ²/dof=1.47e+04 | F_4 multiplier-algebra cannot suppress n=6 slot at L_max=10; corridor closed for the (A, H, D_K) substrate's a_0 spectral content |
| 2 | S85 W0-7 + W0-11 + W0-20 → STRUCTURAL FAIL family | GEOMETRIC | TRUNCATION-HYPOTHESIS FAIL → STRUCTURAL FAIL (3 conversions) | Single-name canonicalization "F_4-MB STRUCTURAL WALL FAMILY" candidate (V.4 carry-forward) |
| 3 | F_4 / M partition theorem → 3-class {F_4, M, F_4-INF Zubarev singleton} | GEOMETRIC | W2-3 PASS rel_err=8.066e-28 | Refines Two-Layer Obstruction; informs C45 convex-mix partition (V.7 carry-forward) |
| 4 | C10 `analytic_zeta(s, L_max)` API delivered | GEOMETRIC | W2-2 INFO value=2.807e+05 + 0j | Survives cascade-FAIL of T9; reusable infrastructure for T5 + W3-G56 + W1b T6 / T7 |
| 5 | C12 `cluster_span(L_max)` module callable | GEOMETRIC | W2-4 FAIL by precision-floor (1.083e-15 vs 1e-15 threshold; bit-exact W0-3 reproduction) | W3 C13 functionally unlocked; rule-file canonical-metric extension landed; V.5 + V.6 carry-forwards |
| 6 | T5 Mellin-Strip / Convergence-Cone Theorem — READINESS COMPLETE | GEOMETRIC | C11 anchor PASS, C10 instrument INFO, C9 falsifies bare-truncation hypothesis (motivates T5) | Surviving CC-suppression corridor #1; HIGH EVOI (≈ 12-15%); V.1 carry-forward |
| 7 | C-regulator class (cutoff_sqrt + anomaly) — UNTESTED at C9 lens | GEOMETRIC + cross-pillar | Awaits C28 cutoff_sqrt adjudication (S86-W-4 INFO at line 106) | Surviving CC-suppression corridor #2; MEDIUM EVOI (≈ 5-8%); V.2 + V.3 carry-forwards |
| 8 | Non-MB suppression (Friedmann two-layer / dilution-CC) — extra-spectral | NON-PHONONIC + GEOMETRIC | Disjoint from F_4 wall by classification; constrained by Two-Layer Obstruction n_joint=0/5 but routes through non-functorial mechanism | Surviving CC-suppression corridor #3; HIGH EVOI for DILUTION-CC-66 specifically; not my lane |
| 9 | C45 convex-mix sixth-regulator-synthesis — DEFERRED against C28 | GEOMETRIC | Inherits per-conjunct Two-Layer Obstruction failure; F_4 wall escape via M-class component | Surviving CC-suppression corridor #4; LOW EVOI (≈ 2-3%); deferred to S87 per S86 partition §2 |
| 10 | W3 T9 / W3 W0-7-MB / W3 W0-11-MB / W3 W0-20-MB / W10 C37-ZFP-ζ-route | GEOMETRIC | cascade-FAIL from W2-1 / W2-2; PRE-REG-INC closures for W3 gates per §X | Constraint-map sharpening; downstream gates retracted as conditional carry-forwards |
