# Seed file — sessions/archive/session-86/session-86-w8-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w8-workingpaper.md` (595 lines)

## Candidates

### Candidate 1 — Analytic derivation of LAYER-3 |ρ| from forward-map couplings

**What it would do**: Derive the LAYER-3 magnitude Pearson |ρ|(α_s, Ω_GW) analytically from the W13-2 forward-map couplings (κ_n_s = +1, κ_Ω = +1) and the W12-4 5-regulator (δ_a2^k, δ_a4^k) atlas without Monte Carlo. The MC value 0.950874 should reduce to a closed form involving the regulator covariance matrix entries Cov(δ_a2, δ_a4) / (σ_{δ_a2} σ_{δ_a4}) modulated by the n_s² nonlinearity in α_s = n_s² − 1. Test whether the 6-cell range [0.951, 0.983] reduces to three closed-form expressions per atlas-weighting × the magnitude/signed parity. Substantive question: is |ρ| a STRUCTURAL identity of the forward map, or does it depend on the empirical (δ_a2^k, δ_a4^k) values that the W12-4 atlas happens to have produced?

**Why it's worthwhile**: §W8-2 lines 287-295 substitution chain reads off the MC value but never derives it analytically. The +4.5% mismatch with the R3 spot-check 0.91 (line 256: "exact-Pearson value where the spot-check used a coarser ad-hoc estimate") is asserted but not explained. If |ρ| is structural (depends only on forward-map slope ratios κ_Ω/κ_n_s and atlas covariance shape), it generalizes to ALL future joint-channel ρ predictions: the substrate's Pearson is dictated by forward-map geometry, not by MC noise. If |ρ| is empirical (depends on the specific 5-regulator (δ_a2, δ_a4) tuple the W12-4 atlas computed), then the 0.951 reading is fragile under atlas extension to L_max=12 or 6th-regulator addition. Also addresses the structural coincidence that magnitude equals signed across ALL six cells (line 291: "NOT by definition but by the empirical fact"); if analytic, "empirical fact" upgrades to "geometric necessity given α_s < 0 throughout the atlas."

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: Five (δ_a2^k, δ_a4^k) values from §W8-2 line 209-216 atlas table. The forward-map identities n_s^k = planck_ns·(1 + κ_n_s·δ_a2^k), α_s^k = (n_s^k)² − 1, Ω_GW^k(f_LISA) = Ω_GW^ζ(f_LISA)·(1 + κ_Ω·δ_a4^k) with κ_n_s = κ_Ω = +1. Reference: P7 verdict-line `rho_signed_uniform = +0.950874`; |α_s straddles zero across atlas? Check: α_s ∈ {−0.069, −0.069, −0.112, −0.541, −0.962} — all negative. Pre-registered analytic threshold: |ρ_analytic − ρ_MC| < 1e-3 (within MC bootstrap σ). Atlas extension test: derive |ρ| under hypothetical 6th-regulator with δ_a2 = δ_a4 = 0 (additional ζ-equivalent point); analytic prediction must match repeat-MC.

---

### Candidate 2 — Atlas-shape sensitivity workshop: does |ρ| collapse if α_s straddles zero?

**What it would do**: Run a controlled sensitivity scan over hypothetical W12-4-shaped 5-regulator atlases where (δ_a2^k) is shifted so that some α_s^k > 0 and others α_s^k < 0 (the framework's α_s straddles zero hypothetically). Predict and verify whether the §W8-2 line 291 "magnitude = signed" coincidence breaks. Two scans: (a) δ_a2 globally shifted so n_s^k clusters above 1.0 → α_s^k > 0; (b) δ_a2 shifted so 2 of 5 regulators have n_s^k > 1, 3 have n_s^k < 1 → α_s^k mixed sign. Compute the 6-cell ρ_grid in each case. Compare to W8-2 baseline.

**Why it's worthwhile**: §W8-2 line 291 explicitly flags the coincidence ("If α_s straddled zero, magnitude and signed would generally differ") but does not test the conditional. The P7 magnitude-Pearson outer-|·| defect (lines 333-350) was caught only because plan §10 line 469-470 forced ρ_magnitude ≥ 0 by construction. If the framework's α_s straddled zero — which it does NOT at canonical pin (−0.069) but COULD under future atlas refinement — the entire P7 result might reorder. The 4-cell signed/magnitude distinction would split into 6 distinct values. This stress-tests the "registry-durable under (sign × atlas-weighting) freedom" claim of §W8-2 line 319 by introducing a third axis (atlas-zero-crossing) the registry doesn't currently expose.

**Type**: solo (1 agent)

**Suggested agents**: mack-cosmic-bridge

**Rounds (workshops only)**: n/a

**Context the workshop will need**: P7 baseline `rho_grid` shape (2,3) from `_artifacts/s86_w8_p7_rho_mc_ensemble.npz`. Hypothetical atlas-shift parameters: shift_uniform ∈ {+0.05, +0.10}, shift_mixed = (+0.10, +0.10, 0, −0.10, −0.10). For each shift, recompute α_s^k, then the 6-cell Pearson grid. Pre-registered prediction: under shift_uniform → α_s^k > 0 throughout, magnitude and signed Pearson should agree (same direction logic as baseline). Under shift_mixed → α_s^k straddles zero, magnitude ≠ signed in at least one cell (ρ_magnitude is non-negative; ρ_signed can flip sign on a subgrid). Threshold: detect at least one cell with |ρ_signed − ρ_magnitude| ≥ 0.10 in the shift_mixed scan to falsify the §W8-2 line 291 conditional.

---

### Candidate 3 — Pre-W8 joint-channel ρ verdict audit against new 6-axis schema

**What it would do**: Audit ALL existing project verdicts that quote a joint-channel ρ(O_1, O_2 | shared substrate parameter p) against the W8-1 P6 6-axis machinery-pin schema (scheme, convention, L_max, layer, arm, f_pivot). Identify which verdicts are PRU Class 8 under the new canonical schema (i.e., missing one or more of the 6 pins). Classify into: (a) verdict already pins all 6 axes (compliant); (b) verdict pins 4-5 axes (partial-PRU; default-pin-fillable); (c) verdict pins ≤3 axes (full-PRU; requires explicit re-registration). Output a registry update for `permanent-results-registry.md` listing classifications and proposing remediations.

**Why it's worthwhile**: Constraint-map row 5 (`Joint-channel ρ verdict machinery-pin schema: UNCANONIZED → CANONICAL`) declares the new schema is mandatory for all FUTURE joint-channel ρ verdicts. But the project has historical joint-channel ρ verdicts (W13-2 itself, S69 transit-GW × CMB cross-channel, S77 domain-wall GW correlations, etc.). Are these now PRU Class 8 under the new schema? §W8 final synthesis is silent on this. The W13-2 verdict-line dual-SHA regen amend was DROPPED from carry-forward (§W8 line 564); this audit determines whether more such regen amends are needed across the registry. If yes, this is a significant cross-session structural debt; if no, the schema retroactively classifies existing verdicts as compliant by default, which is itself a registry-durable result. Either outcome is registry-grade.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: 6-axis schema from §W8-1 line 75-82 (table). Project verdict file `computations/s86_gate_verdicts.txt` plus all prior `s{N}_gate_verdicts.txt` files. Search criterion: any verdict-line value tuple containing `rho` or `ρ` AND naming two distinct observables. Per-verdict classification rule: count the number of axes pinned in the verdict's `convention=` field. Threshold: ≥6 axes named or default-pinnable → compliant; 4-5 → partial-PRU advisory; ≤3 → full-PRU MANDATORY remediation per `.claude/rules/epistemic-discipline.md`. Output: verdict-class table + registry-write to `permanent-results-registry.md` with classification ledger.

---

### Candidate 4 — Promote S65 → C7 cross-session structural coupling to permanent theorem

**What it would do**: Formalize and register the §W8 line 530 cross-session structural coupling "S65 NONLOCAL-SA-65 → C7 truncation bound" as a permanent theorem in `permanent-results-registry.md`. The theorem statement: any spectral-truncation diagnostic at fixed frequency that uses leading-order Casimir scaling for M_KK MUST damp the leading-order shift by the S65 regulator factor 0.12 (or its analog) to obtain truncation-converged predictions. Without this damping, the L=8 → L=10 shift in M_KK is 19% (4.67/3.9222 leading-order) → 38% in Ω_GW, far outside the 5% PASS band that C7 achieved at delta_rel = 4.28%. Verify the theorem by re-deriving: (a) the leading-order Casimir scaling result M_KK_leading = M_KK · sqrt(λ_max(L=10)/λ_max(L=8)) = M_KK · 1.190; (b) the S65 regulator damping factor f_reg = 0.12 from `Lambda_sp = 2.06 M_KK` and the exponential cutoff above the eigenvalue truncation; (c) the damped result M_KK_at_L8 = M_KK + 0.12·(0.190·M_KK) = 1.0228·M_KK = 7.5859e+16 GeV (matching §W8-3 line 470 substituted value).

**Why it's worthwhile**: §W8 line 530 declares "this is a clean cross-session structural coupling that future spectral-truncation diagnostics can inherit," but the synthesis registers no theorem and adds no carry-forward. Without explicit theorem registration, the inheritance is verbal not structural; future spectral-truncation diagnostics that don't know to apply the S65 damping factor will reproduce the misdiagnosis the W13-2 §(f) band-width verdict made (attributing slope to truncation). The theorem belongs in `permanent-results-registry.md` so subsequent gates can cite it as input-pin. The audit also confirms the §W8-3 line 470 derivation chain (currently in WP-prose, not registry-locked); registry-write hardens it.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: §W8-3 line 470 derivation; S65 verdict line for NONLOCAL-SA-65 PASS at <0.1 OOM drift between L=10 and L=12; canonical M_KK = 7.4287e+16 GeV (S42 CONST-FREEZE-42); λ_max(L=8) = 3.9222 M_KK and λ_max(L=10) = 4.67 M_KK from S85 W1 PASS verdict; S65 regulator factor 0.12 from `Lambda_sp = 2.06 M_KK` exponential cutoff. Pre-registered theorem statement form: "For any spectral-truncation diagnostic using leading-order Casimir scaling on (a_0, a_2, a_4) Seeley-DeWitt coefficients to evaluate M_KK(L_max), the L_max=L_1 → L_2 shift in M_KK satisfies |ΔM_KK|/M_KK ≤ f_reg · |Δλ_max|/λ_max where f_reg ≤ 0.12 is the S65-NONLOCAL-SA-65 regulator damping factor." Threshold: derive f_reg from S65 inputs without circular reference to C7. Output: theorem entry + registry-write + cross-link to S65 + S86 W8-3.

---

### Candidate 5 — Phonon-fabric interpretation of LAYER-3 |ρ| ≈ 0.95: forward-map slope coherence

**What it would do**: Workshop the substrate-physics interpretation of LAYER-3 |ρ| ≈ 0.951 — what does the substrate's internal regulator co-monotonicity ACTUALLY mean as a substrate property? Two competing interpretations to adjudicate: (A) "regulator co-monotonicity" reflects the substrate's intrinsic spectral-functional coherence — a deep structural property that any first-principles substrate would exhibit; (B) "regulator co-monotonicity" is an artifact of the W13-2 forward-map ANSATZ specifically, and would dissolve under a different forward-map family that decouples α_s and Ω_GW. Under (A) |ρ| ≈ 0.95 is a genuine substrate prediction; under (B) it is a methodology consequence of how the framework chose to map (a_2, a_4) → (n_s, Ω_GW). Test (B) by computing |ρ| under an alternative forward map (e.g., n_s^k = planck_ns·(1 + κ_n_s·δ_a4^k) — swap the coupling so n_s tracks a_4 instead of a_2). If |ρ| under the alternative still computes to ~0.95, conclusion supports (A); if it drops to ~0 (or flips sign), conclusion supports (B).

**Why it's worthwhile**: §W8-2 substrate-framing reminder (line 325-329) explicitly calls the result "the substrate's own internal consistency across regulator schemes" — claim (A). But the result is computed exclusively through the W13-2 forward map, which encodes a specific (a_2, a_4) → (n_s, Ω_GW) pairing; switching to a degenerate forward-map ansatz where n_s and Ω_GW couple to the SAME spectral coefficient would trivially make |ρ| = 1.0 (Cauchy-Schwarz saturation), and a degenerate ansatz where n_s and Ω_GW couple to ORTHOGONAL coefficients should make |ρ| = 0. So the |ρ| value lives between these limits, controlled by the (a_2, a_4) covariance across the 5-regulator atlas, modulated by the κ_n_s/κ_Ω forward-map ratios. The deeper question — is the W13-2 forward map itself UNIQUE among first-principles substrate ansätze, or is it ONE of a family — is unresolved in the WP. This is the difference between "the substrate predicts |ρ| ≈ 0.95" (deep) vs "the W13-2 ansatz predicts |ρ| ≈ 0.95" (methodological). Both interpretations are consistent with PASS; the workshop would force the team to identify which one the framework actually claims.

**Type**: 2-agent workshop

**Suggested agents**: connes-ncg-theorist, phonon-first-cosmologist

**Rounds (workshops only)**: 2 default

**Context the workshop will need**: W13-2 forward-map identities (n_s^k = planck_ns·(1 + δ_a2^k), Ω_GW^k = Ω_GW^ζ·(1 + δ_a4^k)). Alternative forward maps to test: (i) swap (n_s ← a_4, Ω_GW ← a_2); (ii) couple both to a_0 with different coefficients; (iii) couple both to a_2 with different coefficients (degenerate, Cauchy-Schwarz |ρ|=1 limit); (iv) couple n_s to a_2 alone and Ω_GW to a_0 alone (orthogonal-decoupled limit). Pre-registered prediction: alternatives (iii) → |ρ|=1 trivially; (iv) → |ρ|≈0 trivially; (i, ii) → some nontrivial value. R1 R1 each agent steelmans (A) and (B) respectively; R2 cross-respond and converge on which interpretation the framework's first-principles structure (NCG spectral action, not just the W13-2 numerical pipeline) actually supports.

---

### Candidate 6 — Are the four "structural-zero" cells genuine identities or convention-dependent?

**What it would do**: Examine the four §W8-1 structural-zero cells (Arm-1×Layer-1, Arm-2×Layer-1, Arm-3×Layer-1, Arm-2×Layer-2) and verify they ARE identically zero under the cited mechanisms (LAYER-1 Wick contraction at canonical pins; Layer-2 Fisher diagonality after marginalization), NOT just empirically zero with finite numerical scatter. Specifically: derive the LAYER-1 Wick contraction for each Arm and confirm the result is exact algebraically. For the Layer-2 Fisher diagonality cells, verify Fisher matrix off-diagonal vanishes by construction at the (canonical α_s, pure-W12-4 Ω_GW) pin pair, not approximately. Output: theorem-class entries for each structural-zero cell with proof sketch.

**Why it's worthwhile**: §W8-1 line 71 calls the four cells "structural-zero by construction" with mechanisms cited (LAYER-1 diagrammatic null per W0b R8 §VII.M.4; Layer-2 Fisher diagonality per S85 6A tesla T4 Step 4). But the WP does not derive the structural identity — it cites W0b R8 + S85 tesla T4 as anchors. The audit would verify the cited anchors actually constitute structural identities (not numerical floors) for the cell at hand. If yes, four registry-grade theorems emerge (one per cell). If no, the "structural-zero" classification is downgraded to "below-threshold-zero" with associated numerical floor and stability bound. Either outcome registry-grade. Closes a quiet hole in the §W8-1 PASS justification.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: §W8-1 line 61-69 9-cell table. W0b R8 §VII.M.4 LAYER-1 diagrammatic null definition (Wick contraction at canonical substrate pins). S85 6A tesla T4 Step 4 Layer-2 Fisher diagonality construction. Plan §6 reporting order. Pre-registered structure: for each structural-zero cell, write the Wick contraction OR Fisher diagonal-decomposition explicitly, then evaluate at canonical pins, then verify the result is identically zero (not zero ± numerical scatter). Threshold: each cell admits a closed-form proof OR a counter-example breaks the structural-zero claim. Output: 4 structural-zero theorem proof sketches OR 4 counter-claims with downgrade recommendations.

---

### Candidate 7 — PV-down-weighting analytic geometry: why does anomaly up-weighting tighten Pearson?

**What it would do**: Derive analytically why up-weighting the anomaly regulator (the most extreme M-class point) and down-weighting cutoff_sqrt INCREASES |ρ| from 0.951 (uniform) → 0.977 (PV-dn) → 0.983 (PV-excluded). §W8-2 line 289 attributes this to "stretching along the principal axis." Verify by computing the principal-component-analysis (PCA) decomposition of the 5-point ensemble in (α_s, Ω_GW) space; show that anomaly is ~5σ along PC1 and ~0σ along PC2 (or equivalent ratio); confirm that up-weighting a high-PC1/low-PC2 point geometrically increases the Pearson because it amplifies the major axis of the elongated ensemble distribution. Also explain the PV-excluded → 0.983 result in terms of M-family removal: F_4 trio (ζ, Zubarev, SDW) is intrinsically tighter (intra-family spread = 1.6% in a_2; PC2 spread → 0; ρ → +1 limit).

**Why it's worthwhile**: §W8-2 line 289 asserts the geometric mechanism without computing it. The 0.951 → 0.977 → 0.983 progression is monotonic but at three distinct values, which means there's a structural relationship between the (atlas-weighting) axis and the principal-axis geometry of the (α_s, Ω_GW) point cloud. If derivable analytically, the result has predictive power beyond W8-2's empirical value: any future 5+-regulator atlas with identifiable F_4 vs M stratification would predict its own |ρ|_uniform vs |ρ|_PV-excluded gap. Adds geometric reasoning to the W12-4 5-class taxonomy that's currently described combinatorially. Cross-references to Candidate 1's analytic-derivation candidate; this one focuses on the geometry of the atlas-weighting axis whereas Candidate 1 addresses the value at fixed weighting.

**Type**: solo (1 agent)

**Suggested agents**: kitaev-topological-theorist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: 5-regulator (α_s^k, Ω_GW^k) values from §W8-2 line 209-216 atlas table. Atlas weightings (uniform, PV-dn, PV-excl) from §W8-2 line 232-234 ρ_grid. PCA mathematical machinery (covariance matrix eigendecomposition; singular-value decomposition of the centered 5×2 data matrix). Pre-registered prediction: PC1 explains ≥98% of variance for the 5-point ensemble (M-family dominates spread); ⟨PC2⟩ ≈ 0 (intra-F_4 spread negligible). Threshold: predicted analytic |ρ|_uniform / |ρ|_PV-excluded ratio matches MC values to within 1e-3. Output: PCA decomposition + analytic derivation showing the (atlas-weighting) axis acts as a principal-axis weight redistribution.

---

### Candidate 8 — The PINNED-BUT-DRIFT W12-4 5-class envelope: pin or close

**What it would do**: Address the open PRU Class 8.1 PINNED-BUT-DRIFT entry on P7's W12-4 5-class uncertainty envelope (±5% Gaussian fallback, σ = 0.001 for F_4 family, σ = 0.05 for M family) noted in §W8-2 line 219. The synthesis (line 565-566) DROPPED the canonical lift from S87 carry-forward by citing `no-technical-debt.md` "use-pulled at time of authorship." Determine whether the envelope is pinnable from W12-4's own 5-class taxonomy structure (i.e., is there a derivable σ from the (a_0^k, a_2^k, a_4^k) atlas itself that would make the ±5% Gaussian fallback unnecessary?) or whether the envelope is an irreducible ansatz freedom that future MC scripts must declare separately.

**Why it's worthwhile**: A "PINNED-BUT-DRIFT" classification is documented in P7 but its persistence as a canonical-constants entry is unaddressed. If W12-4's own structure yields a σ analytically (e.g., the within-family spread of (a_2^k, a_4^k) computed from the 5-regulator atlas itself), the envelope IS pinnable and `canonical_constants.py` should carry the lifted value. If the envelope is an ansatz freedom (ad-hoc Gaussian width on top of the 5-point atlas), then every future MC over the W12-4 atlas inherits the freedom; this should be a permanent registry entry naming the ansatz and its bounds. Either way, the resolution belongs in the registry, not in the per-script PINNED-BUT-DRIFT tag the synthesis chose to leave inline. Synthesis line 567 said "future MC scripts over the W12-4 atlas address the envelope inline at the time they're authored" — this is the behavior the no-technical-debt rule warns against (deferring vs fixing). Note: this candidate is auditing whether the synthesis's drop-decision was correct, not contesting it; the audit may CONFIRM the drop.

**Type**: solo (1 agent)

**Suggested agents**: sagan-empiricist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: §W8-2 line 219-220 P7 Gaussian-perturbation σ_F = 0.001 / σ_M = 0.05 specification. W12-4 5-regulator (a_0, a_2, a_4) atlas values from §W8-2 line 199-205. The W12-4 5-class taxonomy classification F_4 vs M and the "16-observable W12-4 PASS (n_a=13, n_d=3)" anchor from §W8-2 line 274-276. `canonical_constants.py` to determine if such σ values exist already as constants (use `mcp__knowledge__list_constants('w12_4_envelope')`). Pre-registered classification: (a) σ_F and σ_M derivable from atlas → CANONICAL-LIFT-CANDIDATE → emit `update_constant` proposal; (b) σ_F and σ_M ansatz-only → REGISTRY-ENTRY-NAMING ansatz with bounds → emit registry-write proposal; (c) PINNED-BUT-DRIFT is the correct stable state because the W12-4 atlas itself is in flux → KEEP DEFERRED with explicit no-technical-debt justification → emit synthesis-validation note. Threshold: one of the three classifications fires definitively. Output: classification verdict + corresponding registry/canonical-constants action.

---

### Candidate 9 — Closeout follow-up: verify the dropped W13-2 verdict-line dual-SHA regen amend

**What it would do**: Verify that §W8 synthesis's decision to DROP the W13-2 verdict-line dual-SHA regen amend (§W8 line 564) was correct under the no-technical-debt rule. The synthesis claim: "Downstream consumers reading the W13-2 verdict line can find the recontextualization annotation in §W8-3 of this WP; no cross-session SHA regen needed." Test by simulating a downstream consumer: write a hypothetical S87 gate that pins W13-2's INFO band-width verdict as input and ask whether the consumer would find the recontextualization without reading session-86-w8-workingpaper.md. If the answer is no — the consumer must traverse a session-spanning WP cross-reference to learn that the W13-2 INFO band-width was spectral-slope and not truncation — then the regen amend is genuinely needed and the synthesis dropped it incorrectly. If the answer is yes — `permanent-results-registry.md` and the knowledge MCP search surface the recontextualization without WP traversal — the drop is correct.

**Why it's worthwhile**: The S82 / S84 task-complete-lie pattern (verdict appended without WP) and the no-technical-debt rule (fix-now vs defer) are repeatedly cited project rules. §W8 synthesis self-classifies the W13-2 amend drop as no-technical-debt-compliant (deferral by recontextualization-in-WP, not by carry-forward), but the test is whether downstream consumers structurally inherit the recontextualization. If the W13-2 verdict-line PRU/RECON audit (Candidate 3 above) already runs against W13-2, that audit could surface the same question; if it doesn't, this is a parallel audit checking whether the §W8 synthesis's self-classification was honest. Closes a quiet self-consistency check on the wave's own debt-deferral decisions.

**Type**: solo (1 agent)

**Suggested agents**: gen-physicist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: W13-2 verdict line at `computations/s85_gate_verdicts.txt` (search for `S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT`). §W8-3 line 466 recontextualization claim. §W8 synthesis line 564 drop justification. `mcp__knowledge__search_knowledge('W13-2 truncation spectral slope')` test query (post-S86 closeout): does the recontextualization surface? `mcp__knowledge__query_entity('gates', 'S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT')`: does the entity record carry a recontextualization annotation, or only the original verdict? Pre-registered test outcome: (a) MCP queries return the recontextualization → drop correct; (b) MCP queries return only the original W13-2 verdict → drop incorrect; the regen amend should have been kept on the carry-forward queue. Threshold: binary outcome from the two MCP queries. Output: verification verdict + corrective action if drop was incorrect.

---

### Candidate 10 — Arm-3 LISA-fold-folded preparation: pre-register the convolution architecture

**What it would do**: Although §W8 line 562 marks Arm-3 as "STAYS DEFERRED... use-pulled when LISA observational pressure motivates it" (not S87-queued), pre-register the LISA-fold-folded convolution architecture NOW — write the spec for Arm-3×Layer-1 and Arm-3×Layer-3 cells without computing them. Specify: (i) the LISA PLS-2024 frequency-response kernel functional form; (ii) the integration band [0.5, 2] f_LISA; (iii) the convolution operator that maps Ω_GW^k(f) into Ω_GW^k_folded; (iv) the resulting forward-map coupling κ_Ω_folded that replaces κ_Ω = +1; (v) the modified ρ Pearson under the folded amplitude. The deliverable is a registry-grade spec sheet, not a computation.

**Why it's worthwhile**: The "use-pulled at need" deferral pattern is convenient but creates LATER PRU debt: when LISA observation lands and someone needs Arm-3 cells, they will rediscover the convolution architecture from scratch (with no pre-registered spec). Pre-registering the architecture NOW — while the wave's authors and reviewers still have context — preserves institutional knowledge. The spec doesn't run the MC; it documents the recipe. Future S87+ gates that pull Arm-3 inline can cite this spec as their input-pin map. This converts "deferred-with-loss-of-context" into "deferred-with-pre-registered-architecture." Light effort (~1 agent-session); permanent registry value.

**Type**: solo (1 agent)

**Suggested agents**: hawking-quantum-acoustician

**Rounds (workshops only)**: n/a

**Context the workshop will need**: §W8-1 line 67-69 Arm-3 cell entries. LISA PLS-2024 kernel definition (search via `mcp__paper-search__` for LISA PLS-2024 forecast paper if needed; or cite `canonical_constants.py` if `f_LISA_pivot` references the kernel). §W8-1 line 81 Axis-5 arm-pin definition. P7 forward map identities. Pre-registered spec elements: (a) PLS-2024 kernel mathematical form K(f, f_LISA) → write the convolution as Ω_GW_folded = ∫ K(f, f_LISA) · Ω_GW(f) df; (b) forward-map propagation: how κ_Ω modifies under the convolution; (c) Cell semantics: Arm-3×Layer-1 (LISA-fold-folded × parameter-pin) — what does this CELL READ as a substrate-prediction (vs Arm-1 and Arm-2 alternative readings)? (d) Cell semantics: Arm-3×Layer-3 (LISA-fold-folded × substrate-marginalized-observable) — same question. Threshold: spec sheet contains all 4 elements; deliverable IS the spec, not the value. Output: registry-grade Arm-3 architecture spec + cross-link to §W8-1 cell entries.

---

### Candidate 11 — Magnitude vs signed Pearson: structural identity at α_s < 0 throughout

**What it would do**: Prove (or disprove) that when the entire 5-regulator atlas has α_s^k < 0 (which holds for canonical W12-4 atlas), the magnitude Pearson |ρ|(|α_s|, |Ω_GW|) — under the outer-|·| construction — equals the signed Pearson ρ(α_s, Ω_GW) bit-exactly, NOT just numerically. §W8-2 line 291 calls this "the empirical fact" — specifically: "the absolute-value transformation here flips both Cov sign AND σ products in a way that preserves magnitude." This is either a structural identity (theorem-class) or an empirical near-coincidence (pin a numerical floor). If structural, derive: |α_s^k| = −α_s^k ∀ k (since all negative), and |Ω_GW^k| = +Ω_GW^k ∀ k (all positive). Cov(|α_s|, |Ω_GW|) = Cov(−α_s, Ω_GW) = −Cov(α_s, Ω_GW). σ_|α| = σ_{−α} = σ_α. σ_|Ω| = σ_Ω. So Pearson(|α|, |Ω|) = Cov(|α|, |Ω|) / (σ_|α| · σ_|Ω|) = −Cov(α, Ω) / (σ_α · σ_Ω) = −ρ(α, Ω). Outer |·| restores magnitude: |Pearson(|α|, |Ω|)| = |−ρ(α, Ω)| = |ρ(α, Ω)|. **Structural identity, conditional on α_s^k uniformly signed across atlas.**

**Why it's worthwhile**: Provides the missing rigor for §W8-2 line 291. Confirms the magnitude=signed coincidence is theorem-class when α_s is uniformly signed, NOT empirical. Reverses the §W8-2 line 291 conditional ("If α_s straddled zero, magnitude and signed would generally differ") into a precise structural statement: when α_s is uniformly signed AND Ω_GW is uniformly positive, ρ_magnitude ≡ |ρ_signed| identically; when α_s straddles zero, ρ_magnitude ≠ |ρ_signed| in general. This sharpens the registry-durability claim for LAYER-3 and connects to Candidate 2's atlas-shape sensitivity scan. Trivial proof effort; clear registry value.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: §W8-2 line 287-291 substitution chain. 5-regulator α_s^k values from line 209-216 atlas table (all negative: −0.069, −0.069, −0.112, −0.541, −0.962). Plan §10 line 442-445 magnitude Pearson definition with outer |·|. Pre-registered structural statement: "If sign(X^k) is constant across the atlas and Y^k > 0 ∀ k, then ρ_magnitude(|X|, |Y|) = |ρ_signed(X, Y)| identically." Threshold: ALGEBRAIC PROOF (not numerical match). Output: registry-grade theorem entry + cross-link to §W8-2 line 291 conditional.

---

### Candidate 12 — Substrate-framing audit of W8 wave: did the wave evade LCDM-comparison framings cleanly?

**What it would do**: Audit the W8 working paper's adherence to substrate-first framing per `.claude/rules/phononic-framing.md`. The §W8 line 544-554 "substrate-framing observations" section claims all three gates "reasoned FROM D_K spectrum TOWARD emergent observables, never the inverse." Verify by reading every sign/direction/threshold claim in the WP and checking each one against the container-vs-substrate framing matrix in `phononic-framing.md`. Identify any claims that slip into LCDM-language (e.g., "the LISA detector resolves Ω_GW to within X%", "α_s is correlated with Ω_GW in the data"). The §W8-2 line 325-329 "substrate framing reminder" already corrects one such tendency explicitly; the audit checks whether other implicit reversions exist.

**Why it's worthwhile**: `phononic-framing.md` is a project-canonical rule that agents repeatedly violate (per the rule's own examples). The §W8 synthesis self-certifies substrate-framing compliance; an independent audit verifies the certification. If audit clears, the W8 wave becomes a calibration corpus exemplar for substrate-framing discipline (the rule explicitly invites such corpora — see §"Pre-registered calibration corpus" of `epistemic-discipline.md`). If audit identifies slips, the WP gets corrected and the slips become teaching examples for future agents. Either outcome registry-relevant.

**Type**: solo (1 agent)

**Suggested agents**: volovik-superfluid-universe-theorist

**Rounds (workshops only)**: n/a

**Context the workshop will need**: `.claude/rules/phononic-framing.md` (in-full). §W8 working paper sections W8-1, W8-2, W8-3 + synthesis (full text). Pre-registered audit rule: for each direction/sign/magnitude claim in the WP, classify as (a) substrate-first (compliant); (b) LCDM-comparison (non-compliant — must be corrected); (c) experimental-noise-framing (non-compliant unless explicitly Layer-2). Threshold: ≤2 (b)/(c) classifications across the entire WP → CALIBRATION-CORPUS-CANDIDATE; >2 → CORRECTION-CANDIDATE. Output: per-claim classification table + CALIBRATION-CORPUS or CORRECTION verdict + (if correction) explicit text patches for the WP.

---

### Candidate 13 — The "rho_computed_count = 1" pre-registration: is the inheritance-cell accounting honest?

**What it would do**: Examine the §W8-1 P6 4-tuple where `rho_computed_count = 1` is pre-registered, but the 9-cell table contains TWO computed cells (Arm-1×Layer-3 and Arm-2×Layer-3, both pulling from P7's 6-cell grid). The reconciliation §W8-1 line 55: "The 'other-computed-inheritance' cell is Arm-1×Layer-3 (signed Pearson over the W12-4 atlas) which inherits its value from the same P7 6-cell grid as the canonical Arm-2×Layer-3 anchor, but is NOT registry-counted separately (per spawn-prompt expected output `rho_computed_count = 1`)." Test whether this counting convention is structurally honest or numerologically convenient. Two cells share the same P7 source → which one is registry-counted? Why? The convention is to count the (signed, uniform) cell once but credit it under Arm-2×Layer-3 because that's the canonical magnitude-Pearson reading; Arm-1×Layer-3 (signed Pearson, same source) inherits but is not counted. Audit: does this convention generalize, or is it ad hoc to make `rho_computed_count = 1` match pre-registration? If the convention is ad hoc, the pre-registration was looser than it appears.

**Why it's worthwhile**: The §W8-1 PASS criterion was structural-completeness binary: n_cells = 9 AND n_axes = 6 AND `rho_computed_count = 1`. If the inheritance cell convention exists primarily to preserve `rho_computed_count = 1` against the actual two-cell inheritance, the pre-registration was a numerology consistency that would have FAILed if the criterion read `rho_computed_count = 2` or `rho_computed_or_inherited_count = 2`. This isn't claim-shopping at compute time (the verdict line is correct under the pre-registration), but it suggests the pre-registration parameter was chosen post-hoc-fittable to the cell-inheritance accounting. Audit confirms or rejects the suspicion. If confirmed, propose a tightening of the pre-registration scheme for future audit-class gates: explicit cell-counting convention with no inheritance-vs-canonical accounting freedom.

**Type**: solo (1 agent)

**Suggested agents**: einstein-skeptic

**Rounds (workshops only)**: n/a

**Context the workshop will need**: §W8-1 line 36 pre-registered `rho_computed_count = 1`. §W8-1 line 55 inheritance-cell explanation. §W8-1 lines 61-69 9-cell table. Plan reference §W8-1 to confirm the pre-registered value. Pre-registered audit question: "Was `rho_computed_count = 1` pre-registered with explicit awareness that 2 cells inherit from the same P7 grid, with conscious choice to count only one as canonical and the other as inheritance? Or was the value chosen first and the inheritance-cell convention invented at compute time to fit?" Threshold: review of plan-file sequence (does plan §W8-1 explicitly distinguish "canonical vs inheritance" before the verdict?) → (a) yes, distinction predates compute → convention is honest; (b) no, distinction emerges only in WP synthesis → convention is post-hoc accounting. Output: classification verdict + (if (b)) tightening proposal for future audit-class gate pre-registrations.
