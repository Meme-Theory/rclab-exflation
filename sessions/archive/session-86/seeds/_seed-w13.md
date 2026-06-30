# Seed file — sessions/archive/session-86/session-86-w13-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w13-workingpaper.md` (862 lines, all read)

## Candidates

### Candidate 1 — α_s 11.31σ tension structural-origin investigation

**What it would do**: P12 (§W13-5) exposes that under the Aiola-2020 ACT DR4 + Planck canonical pin, the framework's frozen prediction `alpha_s_inflation_framework = -0.068968` (= n_s² − 1 from S50-51 substrate identity) sits at +11.31σ from the canonical observation. The synthesis explicitly defers "whether this is a real prediction failure OR indicates the framework's α_s derivation needs revisiting" as a downstream question. This workshop convenes a focused 3-agent re-examination of the S50-51 derivation chain n_s_canon → α_s = n_s² − 1, asking: (a) is the identity exact at the substrate level or is it leading-order in some expansion that has been truncated; (b) what spectral-action moment generates each observable, and does the n_s² − 1 form survive when one carries the next-order Seeley-DeWitt term; (c) does the framework's own GGE-acoustic dispersion second-derivative computation (the substrate's direct route to α_s) match −0.068968, or does it produce a different number that the n_s² − 1 identity merely approximates.

**Why it's worthwhile**: The synthesis (§W13-5 (6) "Tension-widening INFO sub-tag" and §3 of orchestrator wrap-up) explicitly names this as the substrate's largest tension and flags the question as unresolved. The α_s prediction is FROZEN under the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 codified in P1 (§W13-6) — meaning the framework has just COMMITTED to a value sitting 11.31σ from canonical data without re-examining the derivation. Pre-commitment audit is structurally important: if the S50-51 identity is approximate and the substrate's direct GGE-dispersion derivative gives a different (perhaps less tense) value, the framework froze the wrong number. Cross-pillar correspondence: in BCS (Pillar IV), the spectral tilt of the gap function and its running differ by terms involving the quantum-metric correction to the band curvature; the corresponding substrate-side question is whether n_s² − 1 captures only the leading geometric-tilt term and misses a quantum-metric contribution to α_s. CMB-S4 by 2028 will resolve experimentally; the workshop resolves theoretically before commitment.

**Type**: 3-agent workshop

**Suggested agents**: connes-ncg-theorist (spectral action moment derivation owner), volovik-superfluid-universe-theorist (GGE-acoustic dispersion owner; n_T = −r/8 cross-check pillar), mack-cosmic-bridge (observational pin and tension owner)

**Rounds (workshops only)**: 3 (R1 each agent steelmans the derivation route they own; R2 cross-rebuts: Connes asks Volovik to compute α_s from direct GGE dispersion second-derivative without invoking n_s² − 1 identity, Volovik asks Connes whether the spectral-action moment hierarchy gives n_s and α_s as INDEPENDENT moments or as LINKED via the identity, Mack asks both whether the 11.31σ tension survives a more careful uncertainty propagation that includes substrate-side derivation uncertainty; R3 converge on either "identity is exact, framework genuinely 11.31σ tense, falsification by CMB-S4 the next decisive test" OR "identity is leading-order, substrate's direct α_s differs, re-pin alpha_s_inflation_framework with structural uncertainty band")

**Context the workshop will need**: P12 verdict line + substitution chain (§W13-5 (3)); P1 FROZEN-COMMIT 2026-2030 (§W13-6 Element 1); the S50-51 identity statement `α_s = n_s² − 1` with n_s_canon = 0.9649; the substrate-framing block in §W13-5 (8); canonical_constants.py entries `alpha_s_inflation_framework`, `planck_alpha_s`, `alpha_s_canon_2020`, `n_s_canon`; Aiola+ 2020 sigma 0.0063; the n_T = −r/8 single-field-inflation consistency that P2 carries (§W13-7 footnote on Path-H / Path-C n_T derivation), as a cross-check that consistency relations DO survive at substrate level.

---

### Candidate 2 — r dual-pathway B1/B2 substrate eigenvalue partition uniqueness

**What it would do**: P2 (§W13-7) registers TWO distinct framework values for the tensor-to-scalar ratio r — Path-H r=0.00745 (transverse fiber-oscillation, H_tilde rescaling closure) and Path-C r=0.0117 (substrate-compaction, c_sub upper-spread expansion via fiber-tau density compaction). The 36.3% Path-C-relative split exceeds the 12.5% scheme-floor by 2.91× and is explicitly classified as "REAL substrate physics, NOT regulator artifact." The substrate-framing block declares both pathways "project from the SAME substrate observable (eigenvalue partition between B2 transverse fiber modes and B1 longitudinal acoustic modes evaluated at the pivot scale)." This workshop interrogates a structurally unsettling claim: if both pathways are valid projections of the SAME B1/B2 eigenvalue partition, the partition itself must be 2-valued (not unique) at the pivot scale — OR the two pathways are NOT projections of the same partition but of two distinct sub-partitions that the substrate-framing block conflates.

**Why it's worthwhile**: This is a Pillar I (acoustic gravity) ↔ Pillar IV (flat band BCS) ↔ Pillar VIII (KK on Lie groups) cross-pillar resonance test. In analog gravity, B1/B2 modes correspond to longitudinal/transverse phonon polarizations and their partition at a horizon is determined by the boundary conditions, not by an internal substrate freedom. In flat-band BCS, the quantum-metric superfluid weight has a unique geometric origin (Peotta-Toermae) — there is not a "Path-H derivation" and "Path-C derivation" giving different superfluid weights from the same band geometry. The substrate-framing block's claim that two pathways legitimately project from the same eigenvalue partition implies a structural multi-valuedness in the substrate's r-channel that is either (a) a deep feature analogous to the multiple Hopf charges of an SU(2) condensate, or (b) an unresolved degeneracy hiding a missing constraint. The framework just FROZE both values into the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030; if BK-Array 2026 returns a value clearly favoring one pathway, the OTHER pathway either falsifies along that axis or the framework reverts to "one of the two projections was always the correct one and we did not know it." LiteBIRD 2030 n_T discrimination (§W13-7) at >4σ separation between Path-H n_T = −0.000931 and Path-C n_T = −0.001463 will pin this experimentally — but the structural question is theoretical: WHY does the substrate produce two values? Solo-synthesis would not catch this; needs cross-pillar agents.

**Type**: 2-agent workshop

**Suggested agents**: volovik-superfluid-universe-theorist (Path-C owner; substrate-compaction / 3He-B inheritance theorist), connes-ncg-theorist (spectral action B1/B2 partition derivation owner)

**Rounds (workshops only)**: 2 default (R1 each agent steelmans the derivation route they own; R2 each agent must answer whether the OTHER pathway's derivation is (a) a separate substrate observable that should be in the inventory as TWO different rows, or (b) the same observable computed two ways with one being incorrect, or (c) a regulator-class freedom that the substrate genuinely possesses)

**Context the workshop will need**: P2 verdict line + the substrate-framing block (§W13-7) declaring "both project from the SAME substrate observable"; the three split-fraction interpretations (57.0% / 44.4% / 36.3%); the n_T table (Path-H = −0.000931, Path-C = −0.001463); the SEQUENCED detector chain BK-Array 2026 4-branch tree + LiteBIRD 2030 STRUCTURAL-FLOOR; the source-pin trail through `s85-w2-as-band-authority.md` line 1882 (Path-H source) and `mack-cosmic-bridge/project_3heb-inheritance.md` (Path-C source); S86 W12 boundary table (b1_b2 = 0.005, b2_b3 = 0.015, b3_b4 = 0.030).

---

### Candidate 3 — f_NL_folded 14× pathway-spread substrate adjudication

**What it would do**: P10 (§W13-2) creates the f_NL_folded pathway registry with three values spanning ~14×: S82-GGE-equilateral 0.0547, S67-GGE-folded 0.129, W9-3-analytic-template-folded 0.7685. The structural finding is explicit: "This is methodological spread — three distinct reductions of the substrate inter-band coherence — not measurement uncertainty." The W9-3 pathway (0.7685) is the only one detector-discriminable in the 2030s suite (SKA-1 σ ~ 0.15 at folded ridge); S82 (0.0547) and S67 (0.129) are detector-sterile (CMB-S4 σ = 6.9, Planck σ ~ 5.7). The registry leaves "downstream substrate-prediction citations of the framework's f_NL_folded prediction are now required to specify the pathway tag, eliminating the conflation hazard." The unaddressed question: if the same substrate observable is reduced three ways and the reductions disagree by 14×, which reduction is the substrate's actual prediction — or are they three different observables that the framework has been calling by the same name?

**Why it's worthwhile**: A 14× spread in a non-Gaussianity prediction is structurally severe. In standard inflation, f_NL is a single number once the inflaton model is specified; "three pathways giving 14× spread" would be a sign of three different models, not three reductions of one. The framework's claim is that all three are reductions of the SAME substrate inter-band coherence. The workshop tests this by asking each pathway to write down its in-in formalism vertex explicitly: S82 GGE-equilateral uses what 3-point coupling; S67 GGE-folded uses what 3-point coupling; W9-3 analytic-template-folded uses what 3-point coupling. If the three vertices are the same operator evaluated three ways, the 14× spread is a regulator/regime-of-validity question. If the three vertices are DIFFERENT operators (e.g., one is the connected cumulant and another is the disconnected reducible piece, or one is in-in and another is in-out), the registry has been treating distinct observables as if they were the same. Cross-pillar test: in BCS (Pillar IV), the bispectrum of pair fluctuations in the folded triangle limit has a unique vertex per band-coupling channel; multiple channels ARE allowed but they correspond to physically distinguishable processes, not regulator-class artifacts of one process.

**Type**: solo (3 agents) — independent-parallel; each agent reads the same sources and writes their own report on which pathway IS the substrate's f_NL_folded prediction

**Suggested agents**: connes-ncg-theorist (spectral-action vertex derivation owner), volovik-superfluid-universe-theorist (in-in formalism on superfluid substrate), kaku-speculative-theorist (broad-pattern detector for which pathway maps onto known GR/inflationary computations correctly)

**Rounds (workshops only)**: N/A — solo (3 agents independent-parallel)

**Context the workshop will need**: P10 verdict line + 3-row table; the producing scripts `s67_gge_bispectrum.py`, `s82_w3_4_gge_fnl_channel.py`, `s85_w9_folded_triangle_21cm_shape.py` (named in the MCP audit); detector σ values (CMB-S4 6.9, Planck 5.7, SKA-1 folded 0.15); the substrate-framing block (§W13-2) declaring "3 sub-channel projections of the SAME substrate observable, not 3 competing models"; the S86 P11 master-inventory Row #9 cross-reference establishing all 3 within Planck 1-σ (-26±21).

---

### Candidate 4 — DR3 sub-tree L=8 sub-cell direct extraction methodology

**What it would do**: P8 (§W13-4) emits INFO with 14 populated cells + 7 stub cells because S85 W7-7 publishes only `max_L_sensitivity = 0.0204` over an unrelated basket of 8 W_0-dependent constants — NOT a Zubarev w_0(L=8) value or 7-scenario sub-decomposition. The S87-W0 carry-forward is pre-registered as `S87-DR3-SUB-TREE-3-ROW-PIN-PROMOTION` with the methodology pinned: "direct Zubarev w_0 extraction at L=8 from the L=8 D_K eigenvalue cache, scenario classification, fill 7 stubs, re-emit gate at PASS level." But the synthesis (§4) also documents a sibling gate W12-4 `S86-DR3-3-LAYER-SUB-TREE` that ALREADY filled L=8 via canonical-anchored offset reconstruction (rho(L=8) + offset = -0.845, scenario A1) and PASSed. The two sibling gates produce STRUCTURALLY DIVERGENT outputs on the same physical question. The synthesis's resolution — "downstream sessions can choose which discipline to cite" — is not closure. The workshop pre-registers the S87-W0 direct extraction protocol now, before S87, so the dispatch is mechanical rather than methodological.

**Why it's worthwhile**: The two sibling gates' divergence is a methodological-discipline test: P8 forbids fabrication; W12-4 permits offset reconstruction. The latter PASSes; the former is INFO. If the L=8 D_K eigenvalue cache exists and direct Zubarev extraction is mechanically dispatchable, P8's discipline produces the right answer and W12-4's offset reconstruction was a stand-in. If the cache doesn't exist or the extraction has unresolved scheme choices, W12-4's offset reconstruction is the practical-route answer and P8's INFO is the honest-route answer. Either way, S87 has to dispatch one of the two; pre-registering the direct extraction methodology now (rather than letting S87 inherit ambiguity) closes a Class-8 PRU vulnerability. Cross-pillar: in NCG (Pillar III), the spectral action's a_n moments at finite L_max are well-defined truncations and direct Seeley-DeWitt computation should produce w_0(L=8) without offset interpolation, given the eigenvalue cache. If it doesn't, that itself is a finding.

**Type**: solo (1 agent)

**Suggested agents**: cosmic-web-theorist (P8 owner; same agent who hit the W7-7 fallback wall) OR connes-ncg-theorist (NCG spectral-action moment direct extraction)

**Rounds (workshops only)**: N/A — solo

**Context the workshop will need**: P8 verdict line + the 21-cell matrix + 4-branch protocol (REG-INVARIANT / REG-DEP-MAJORITY / STRUCTURAL-AMBIGUITY-FREEZE / EXTERNAL); the S86 W12-4 sibling verdict line at `s86_gate_verdicts.txt:195` (rho(L=8) = -0.504 + offset_-0.341 = -0.845 in scenario A1); the W7-7 source verdict line `s85_gate_verdicts.txt:175` `S85-W7-W0-RE-AUDIT-AT-L8: PASS value=0.0204` (max_L_sensitivity scalar over 8-constant basket); the S85 W1b-1 source `s85_gate_verdicts.txt:38` (the L=10 → L=12 A1→B2 cell flip that motivated the 3-row tree); pointer to the L=8 D_K eigenvalue cache location (whichever computation-archive directory holds the L_max=8 eigenvalues); the W4-44 7-cell partition definitions (A1, A2, B1, B2, B3, C1, C2) as enumerated in P8's substrate-framing block.

---

### Candidate 5 — SOURCE-RECON calibration-corpus extension for R_842 rectangle drift

**What it would do**: P9 (§W13-3) detected at runtime that the plan §W13-3.6 INPUT-PIN MAP cited `R_842 = [-1.05, -0.85] × [-0.2, +0.2]` (range-form, half-width 0.100, center -0.95) while the mack-9A canonical from `sessions/archive/session-85/session-85-mack-synthesis-w6-13.md:75` is `R_842 = [-0.942, -0.742] × [-0.2, +0.2]` (center -0.842, half-widths 0.100/0.200). These are geometrically distinct rectangles. Sagan-empiricist correctly recorded both definitions, honored the mack-9A canonical, and proved the verdict invariant under either label (A wins on Criterion 4 registry-history-priority regardless). The synthesis (§2) flags this as a Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY drift and explicitly queues "SOURCE-RECON calibration-corpus extension as technical-debt action." Per CLAUDE.md project rule "No Technical Debt" and feedback `feedback_fix-in-session-never-defer.md`, this should be fixed in-session (S86), not carry-forwarded. The workshop produces the calibration-corpus extension entry now and validates that `_source_reconciliation_audit.py` would have caught it at plan-freeze.

**Why it's worthwhile**: The S86 W2-4 verdict already canonicalizes `R_842 = [-0.942, -0.742] × [-0.2, +0.2]` as the structural source per the S84 W1b-9 migration ledger (this is documented in `epistemic-discipline.md` v3 calibration-corpus entry W13-3 R_842 stale-rectangle relabel), but the SOURCE-RECON audit script does not yet automatically validate plan-prompt INPUT-PIN MAP rectangles against the most-recent migration ledger. Adding the test mechanically + a precedent entry in the rule's calibration corpus closes the technical debt. Future plan-freezes will catch the same drift by construction. Effort is single-session; this is exactly the "fix-in-session" route the rule mandates.

**Type**: solo (1 agent)

**Suggested agents**: sagan-empiricist (the runtime detector; owns the in-wave evidence) OR mack-cosmic-bridge (project-level registry custodian)

**Rounds (workshops only)**: N/A — solo

**Context the workshop will need**: P9 verdict line + §1 of `sessions/framework/registry/w0-primary-decision-rule.md` (both rectangles recorded); the S84 W1b-9 migration ledger at `sessions/archive/session-84/session-84-w1-workingpaper.md:879`; the S86 W2-4 canonicalization in `epistemic-discipline.md` v3 §"Canonical-metric pin extension" calibration-corpus entry (the W13-3 stale-rectangle-relabel precedent already exists in the rule's calibration corpus — extension is the audit-script-side automated check); the audit-script `computations/_source_reconciliation_audit.py` SOURCE-RECON pipeline; the 4-class taxonomy (a) PIN-TIGHT-SOURCE-LOOSE / (b) PIN-LOOSE-SOURCE-TIGHT / (c) PIN-DRIFT-FROM-STALE-SOURCE / (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY / (e) PIN-PROMOTES-TO-CANONICAL-ON-PASS as documented in `epistemic-discipline.md`.

---

### Candidate 6 — n_T = −r/8 inflation consistency relation under Path-H/Path-C dual-pathway substrate

**What it would do**: P2 (§W13-7) inherits the n_T = −r/8 single-field-inflation tensor tilt identity (S84 W4-39 exact) for both pathways: Path-H gives n_T = −0.000931; Path-C gives n_T = −0.001463; Δn_T = −0.000532. The framework treats this as a "consistency relation, inherited by both pathways from the underlying B2-mode kinematics." But n_T = −r/8 is a SINGLE-field-inflation identity — and the framework is explicitly NOT single-field inflation; it is supersonic transit through the van Hove fold, with two distinct B1/B2 substrate channels giving different r values. The workshop tests whether the n_T = −r/8 identity actually holds for the substrate's tensor-mode generation, or whether the framework has been borrowing a single-field-inflation result that does NOT generalize. If the substrate's tensor-mode generation does NOT obey n_T = −r/8 exactly, the LiteBIRD 2030 discrimination of Path-H vs Path-C at >4σ via n_T separation rests on a borrowed identity that may not be the framework's actual prediction.

**Why it's worthwhile**: The S84 W4-39 identity was registered as exact. But the framework's tensor-to-scalar ratio is now explicitly TWO-valued (Path-H + Path-C). Single-field-inflation gives a unique r and a unique n_T; the consistency relation is a COROLLARY of having a single inflaton driving both. With two distinct substrate-derivation pathways for r, there are two routes for n_T, and the question is whether the n_T = −r/8 corollary applies to each pathway separately, jointly, or to neither. This is a Pillar I (acoustic gravity — n_T from acoustic-mode dispersion) ↔ Pillar VIII (KK on Lie groups — tensor mode generation from internal-geometry oscillation) cross-pillar test. If the substrate's actual tensor-tilt computation gives n_T values different from -r/8 for Path-H or Path-C, the LiteBIRD discrimination at >4σ separation reported in §W13-7 is overstating discriminability, and the framework's frozen prediction needs revising before LiteBIRD 2030.

**Type**: 2-agent workshop

**Suggested agents**: hawking-vdd-bridge (if available; horizon thermodynamics + tensor mode owner) OR connes-ncg-theorist + volovik-superfluid-universe-theorist (NCG spectral-action tensor moment + GGE-acoustic dispersion)

**Rounds (workshops only)**: 2 default

**Context the workshop will need**: P2 verdict line + the n_T table (Path-H -0.000931, Path-C -0.001463); the S84 W4-39 exact n_T = −r/8 identity (the verdict line at `s84_gate_verdicts.txt`); the LiteBIRD STRUCTURAL-FLOOR registry from S85 W1a (sigma(n_T) ≈ 0.000125 at sigma(r) ≈ 0.001); the substrate-framing block declaring B2-mode kinematics inheritance; the BK-Array 2026 4-branch tree (boundaries 0.005/0.015/0.030); the LiteBIRD discrimination band table for Path-C at <1σ / 1-3σ / >3σ.

---

### Candidate 7 — α_s tension as a substrate-eigenvalue regime-of-validity test

**What it would do**: P12 substitution chain shows the framework α_s = -0.068968 is the S50-51 identity n_s² − 1 with n_s = 0.9649 → α_s exactly. The Aiola-2020 canon central is +0.0023 (positive!); the framework's prediction is negative. The 11.31σ tension is large in σ-units, but the more interesting question is the SIGN: the substrate predicts negative α_s (red running of the tilt), the data favors positive α_s (blue running). The workshop investigates whether the n_s² − 1 identity FORCES α_s < 0 by construction (which would mean any positive observed α_s falsifies the substrate identity AS-IS), or whether the framework has additional substrate-side α_s sources (e.g., subdominant spectral-action moments) that could shift the sign. This connects to Candidate 1 but with a sharper structural focus: the SIGN, not the magnitude.

**Why it's worthwhile**: The substitution chain in §W13-5 (3) shows: n_s_canon = 0.9649 → n_s² = 0.93103201 → α_s = n_s² − 1 = -0.06896799. This is negative for ANY n_s < 1. The substrate's identity FORCES α_s sign = sign(n_s − 1) × |any| − but more specifically, sign(α_s) = sign(n_s² − 1) = sign(n_s² − 1), which is negative whenever 0 < n_s < 1. Since Planck observation pins n_s = 0.9649 < 1, the substrate's α_s identity is SIGN-LOCKED to negative. The Aiola-2020 +0.0023 measurement is OPPOSITE-SIGN to the framework prediction; this is a categorical tension, not just a magnitude tension. CMB-S4 by 2028 will pin the sign at high confidence; if the sign holds at +ve, the n_s² − 1 identity is falsified independent of magnitude, and the framework needs a different substrate route to α_s. This is a falsifier-class observation that the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 has now committed the framework to. Workshop verifies the sign-lock structurally before commitment lapses.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist (spectral identity owner — n_s and α_s as spectral moments)

**Rounds (workshops only)**: N/A — solo

**Context the workshop will need**: P12 substitution chain (§W13-5 (3)); the canonical_constants.py entries `alpha_s_inflation_framework = -0.068968`, `n_s_canon = planck_ns = 0.9649`; the S50-51 source for the n_s² − 1 identity (atlas-summary documents per project memory `s50_s51_atlas`); Aiola+ 2020 ACT DR4 + Planck combined α_s = +0.0023 ± 0.0063 (the new canonical pin); CMB-S4 forecast σ(α_s) = 2.1e-3 (used in P12 §(4)); the spectral-action moment hierarchy linking n_s (a_4 derivative) and α_s (a_4 second derivative or a_6 derivative — workshop determines which).
