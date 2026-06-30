# Seed file — sessions/archive/session-86/session-86-w11-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w11-workingpaper.md` (359 lines read in full)

## Candidates

### Candidate 1 — Level-saturation diagnostic: is LAB-FALSIFIER-A informative when 9/9 rows land there?

**What it would do**: Audit the LAB-FALSIFIER level ladder calibration against W11's actual outcome. The pre-registered ladder partitions detection_ratio into A (≥10), B (3-10), C (1-3), D (<1), but W11's 9 rows distribute as {A:9, B:0, C:0, D:0} with the lowest d_r=28.5 (SW3 173Yb) and highest d_r=5.90e+04 (SW1/XA1 3He-A) — spanning 4 OOM yet collapsing to one level. Workshop would ask: (a) does the A-level-only outcome make the ladder uninformative for THIS row class (i.e., should there be an A-prime level above ~10^3 that flags 3He-A's headroom-rich rows)? (b) is the ladder calibrated for 5-yr horizon, or for an instantaneous-detection idealization? (c) what physical information distinguishes a d_r=28.5 row from a d_r=5.9e+04 row when both are level A?

**Why it's worthwhile**: The C6 verdict's own substitution chain (WP lines 250-279) shows the EVOI ordering is preserved by construction, but a ladder where 9/9 rows occupy the maximal level is structurally indistinguishable from no ladder at all for adjudication purposes. The framework's lab-falsifier portfolio has been lifted from 0 to 9 atomic rows (constraint-map row 4, WP line 346), but if all 9 are A-level the rank-ordering for W14-W6 priority is degenerate. C6 PASS-criteria silence on rank-ordering within level (WP §W11-2 PASS criteria, line 170) means downstream W14 / W15 will need a finer instrument. The WP itself flags the band 0.30-0.50 as "supports the upper end" given 9× A-level (WP line 287), but 0.30-0.50 is a single bin; W15's P_decisive denominator gains 9 entries with no internal ordering.

**Type**: 2-agent workshop

**Suggested agents**: sagan-empiricist, mack-cosmic-bridge

**Rounds (workshops only)**: 2

**Context the workshop will need**:
- Gate IDs: `S86-LAB-FALSIFIER-EVOI-TREE` (C6) and `S86-LAB-SI-TRANSLATION` (C5)
- Anchors: level_distribution = {A:9, B:0, C:0, D:0}; detection_ratio range [28.5, 5.9e+04]; A-level floor pre-registered at 10
- 4-branch tree's Branch-1 floor `max(3, 0.5·d_r)` (WP line 217)
- The 9-row CSV `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv`
- W14-W6 P_decisive band [0.30, 0.50] from partition manifest §1
- Adjudication question: does the framework need an `LAB-FALSIFIER-A+` super-level (e.g., d_r ≥ 1000) to preserve rank-ordering within decisive rows?

---

### Candidate 2 — Provisional-anchor structural audit: is the 3He-A and 173Yb sigma_detect upper-bound representation hiding a 2-3 OOM level-shift?

**What it would do**: Examine the 6 provisional rows (SW1/XA1/XB1 = 3He-A and SW3/XA3/XB3 = 173Yb) where σ_detect is recorded as "state-of-art upper-bound" rather than "single-shot 3-sigma floor." Specifically, verify the Aalto/ROTA NMR linewidth representation (1 kHz, used for 3 rows) and the SU(N)-lattice K_3 theoretical floor (0.05 s^-1, used for 3 rows). The WP claims (line 335) "any plausible tighter floor leaves them in level A" but does NOT compute the multiplicative factor between upper-bound and 3-sigma single-shot. If single-shot detection floors are 10-100× tighter than upper-bounds, detection ratios scale UP (more decisive); if 10-100× looser, some rows could drop level. The asymmetry between FeSe (non-provisional, single-shot 5 ppm) and 3He-A/173Yb (provisional) means the framework's confidence on 6/9 rows rests on a literature-anchor type that is not bit-identical to the FeSe one.

**Why it's worthwhile**: This is a structural cross-platform-comparison question, not a level-shuffle. The C5 INFO band fired BECAUSE these 6 rows are provisional (WP line 31-32), but the W14-W6 NEW row class will land all 9 rows under the same level-A flag. If the eventual single-shot floor for 3He-A is 10× tighter than 1 kHz (i.e., 100 Hz), SW1's d_r jumps from 5.9e+04 to 5.9e+05 — strengthening the A-level dominance. If it's 100× looser due to vortex-line broadening at base temperature, d_r drops to 5.9e+02 — still level A, but the "5 OOM headroom" claim collapses. For 173Yb, the K_3 theoretical floor is more vulnerable: experimental 3-body loss rates routinely exceed theoretical floors by 10×, which would push SW3 from d_r=28.5 down to d_r=2.85 — LEVEL C, breaking the 9× A-level claim. The structural pattern: provisional rows that clear A-level by 1-2 OOM (the 173Yb rows at d_r 28.5-131.9) are the level-shift candidates; provisional rows that clear by 4-5 OOM (the 3He-A rows) are level-stable.

**Type**: solo (2 agents)

**Suggested agents**: volovik-superfluid-universe-theorist, sagan-empiricist

**Rounds (workshops only)**: N/A (independent solo reports)

**Context the workshop will need**:
- 6 provisional rows: SW1, SW3, XA1, XA3, XB1, XB3
- Lit SHAs: 3He-A `ecc168738d744136` (Eltsov+ 2010 PRL 105, 125301); 173Yb `4cd097a278b4adbd` (Cazalilla+ 2009 NJP 11, 103033)
- Per-platform σ_detect values: 1 kHz (3He-A NMR), 0.05 s^-1 (173Yb K_3)
- Per-row d_r values from `s86_w11_lab_si_translation.csv`
- Specific question: for each of the 6 provisional rows, what level-shift would result from a 100× tighter / looser single-shot floor? Tabulate against the {A:≥10, B:3-10, C:1-3, D:<1} ladder.
- Level-shift threshold: d_r drops to <10 ⇒ level B/C/D; d_r drops to <1 ⇒ level D (sub-floor)

---

### Candidate 3 — λ_a direction-mapping audit: does the SI translation respect Gell-Mann SU(3) representation theory?

**What it would do**: Test whether the 3×3 (3 lambda × 3 platform) substrate-prediction matrix encoded in the C5 SI translation table preserves the expected Gell-Mann SU(3) representation structure. The W8-4 ratios (per WP line 41-50): λ_6 column gives {1.7267, 0.7674, 5.4938} for {3He-A, FeSe, 173Yb}, λ_7 gives {0.5756, 1.8226, 13.1852}, and λ_8 only fires on the SW3 sweet-spot diagonal at 2.85. Specifically: does the cross-platform SUPPRESSION 3He-A·λ_7=0.5756 (vs. native 3He-A·λ_6=1.7267, ratio 0.33) come from the same Gell-Mann commutation structure as the cross-platform AMPLIFICATION 173Yb·λ_7=13.1852 (vs. native 173Yb·λ_8=2.85, ratio 4.63)? Workshop would identify whether the off-diagonal projections match what one expects from <λ_a · π_platform> overlaps under the Jensen-deformed inner product, OR whether the cross-platform readings are independently free parameters.

**Why it's worthwhile**: This is the genuine cross-pillar bridge buried in W11. The 9-row table treats sweet-spot diagonal and cross-platform off-diagonal entries as 9 independent observables, but they are NOT independent if the platforms have well-defined projection operators π_3HeA, π_FeSe, π_173Yb onto the SU(3) Lie algebra. The W8-4 magnitudes (which W11 inherits as FROZEN per S85) already encode the projections; the SI translation just multiplies by the platform's energy scale. A workshop could check whether the 6 cross-platform entries (XA*, XB*) are derivable from the 3 sweet-spot entries (SW*) via the platform projection operators — if yes, the framework's 9-row corridor reduces to a 3-row corridor + Gell-Mann commutators (much stronger statement); if no, the cross-platform entries carry independent predictive content. Either outcome is a structural result that strengthens the lab-falsifier program.

**Type**: 3-agent workshop

**Suggested agents**: connes-ncg-theorist, volovik-superfluid-universe-theorist, lizzi-spectral-functional-theorist

**Rounds (workshops only)**: 3 (R1 each agent characterizes the platform projection operator; R2 derive cross-platform from sweet-spot; R3 converge on whether the 9 rows are 3+6 or genuinely 9)

**Context the workshop will need**:
- 9-row CSV `s86_w11_lab_si_translation.csv` with W8_4_ratio column
- Source W8-4 verdict: `S85-W8-4-SU3-OP-LAB-PREDICTIONS` PASS (from WP MCP audit line 20)
- Gell-Mann generator structure: λ_6, λ_7 are off-diagonal; λ_8 is the diagonal hypercharge-like generator
- Platform-specific projections: 3He-A → λ_6 sweet-spot (vortex-line direction); FeSe → λ_7 sweet-spot (NMR Knight-shift direction); 173Yb → λ_8 sweet-spot (3-body-loss SU(N) channel)
- The 6 cross-platform predictions: XA1=1.7267, XA2=0.7674, XA3=5.4938 (all λ_6); XB1=0.5756, XB2=1.8226, XB3=13.1852 (all λ_7)
- Adjudication: does cross-platform = π_platform · λ_a for some platform projection operators? Is the 9-row matrix rank-1, rank-2, or full rank-3?

---

### Candidate 4 — Branch-1 floor `max(3, 0.5·d_r)` re-examination: does it filter genuine detections at sub-magnitude?

**What it would do**: Audit the Branch-1 PASS-AT-LAB criterion `s_obs/sigma_detect ≥ max(3, 0.5·d_r)`. The WP's own example (SW1, line 200) shows this requires s_obs/σ ≥ 29479.4 — i.e., the substrate prediction must land within a factor 2 of full-magnitude to register as Branch-1 PASS. A clear 1000-sigma detection at, say, 1% of the framework's predicted magnitude would fall into Branch 2 (REGISTERED-NO-CLOSE) rather than Branch 1, even though the physical signal is unambiguous. This is by construction (per WP line 217: "eliminates 'detection at 3-sigma but at 1/100th the predicted magnitude' from triggering Branch 1"), but the asymmetry deserves scrutiny: the framework's level ladder is binary on d_r magnitude, but the branch tree is asymmetric on s_obs/σ. Workshop would test whether a substrate signal at 1/10 the predicted magnitude (still well above noise) carries enough framework-discriminating power to deserve Branch-1 PASS, or whether the 0.5·d_r floor is the right discipline.

**Why it's worthwhile**: The framework's substrate predictions are FROZEN (W8-4 ratios at S85 PASS, line 20). The lab-falsifier program will adjudicate against the W8-4 magnitudes. If a 2027 NMR experiment finds a 3He-A signal at 5.9 MHz (= 1/10 the predicted 58.96 MHz) with 1000-sigma confidence, the framework needs to decide: is this Branch 1 (PASS, shows substrate) or Branch 2 (REGISTERED-NO-CLOSE, queue for next-gen)? The current rule says Branch 2. But a sub-magnitude detection at high confidence is information — it could mean (a) the framework's M_KK normalization is off by 10× (recalibration, not refutation); (b) a different substrate direction is dominant at this platform; (c) the substrate prediction is correct AND there is an independent contribution at 90% of the magnitude. The 4-branch tree as written collapses these three physically distinct scenarios into one branch.

**Type**: 2-agent workshop

**Suggested agents**: sagan-empiricist, kaku-speculative-theorist

**Rounds (workshops only)**: 2

**Context the workshop will need**:
- 4-branch decision tree from WP §W11-2 lines 198-217
- Specific Branch-1 floor `max(3, 0.5·d_r)`
- Pre-registration discipline: Branch conditions are FROZEN per FROZEN-PREDICTION-DISCIPLINE-COMMIT; any modification is a NEW pre-registration, not a tweak
- Counter-example to test: hypothetical 1000-sigma detection at 1/10th magnitude on SW1 — what does the framework say?
- Question: should the 4-branch tree have a 5th "magnitude-recalibration" branch, OR is the binary "above-half-magnitude vs below" sufficient?
- Adjudication: keep the 4-branch tree as written (PRE-REGISTRATION DISCIPLINE) OR pre-register an extension for S87+ (NEW class, not modification)

---

### Candidate 5 — Phononic-substrate framing audit on the BCS prefactor (1.764 k_B T_c) and h_planck normalization

**What it would do**: Examine whether the C5 SI translation prefactors silently smuggle a container-thinking assumption. Specifically, the 3He-A row uses `Delta_3HeA = 1.764 · k_B · T_c` (BCS weak-coupling formula, WP line 67) and `nu_Delta_3HeA = Delta_3HeA / h_planck` (frequency conversion). Both prefactors treat the 3He-A platform as a system embedded in a thermodynamic ambient (T_c is a temperature in a thermal bath, h_planck is a quantum action defined on a spacetime manifold). The phononic framing rule says space is emergent from D_K spectral content, so T_c and h_planck should be readable as substrate spectral moments (T_c → BCS gap = lowest λ_a eigenvalue at the platform's compactification ratio; h_planck → dimensional bridge between substrate spectral units and lab clocks). Workshop would ask: does the SI translation chain {M_KK-units → 1.764 k_B T_c → MHz} silently invoke a thermal-equilibrium ambient that contradicts the GGE-relic-never-thermalizes claim of the framework?

**Why it's worthwhile**: This is a methodological consistency check, not a numeric one. The WP correctly enforces the IS-not-IN rule for phenomenology_note phrasing (lines 94-98), but the SI translation chain itself uses standard CGS/SI prefactors that assume container thinking. If the substrate is fundamental and 3He-A is an emergent superfluid in that substrate, then the BCS T_c is a derived quantity from the substrate's coupling to the quantum-vacuum eigenmodes — not an independent thermodynamic parameter. The ratio (W8-4 magnitude) is dimensionless and survives the framing question; but the prefactor (34.146 MHz on 3He-A) is what makes the ratio observable, and that prefactor inherits standard QM conventions. A workshop would test whether the framework's substrate-derivation of BCS T_c agrees numerically with 0.929 mK — if yes, the SI translation is internally consistent; if not, the 34.146 MHz prefactor is a contradiction with substrate-first reasoning.

**Type**: solo (1 agent)

**Suggested agents**: volovik-superfluid-universe-theorist

**Rounds (workshops only)**: N/A

**Context the workshop will need**:
- C5 substitution chain WP lines 61-91
- 3He-A weak-coupling BCS: `Delta = 1.764 k_B T_c`, `T_c = 0.929 mK` at 0 bar (Greywall 1986 canonical)
- FeSe analog: 200 ppm Knight-shift baseline, h_planck-implicit B0=14 T conversion
- 173Yb analog: K_3 = 0.5 s^-1 floor, n_lat = 1e14 cm^-3, h_planck-implicit photon-recoil scale
- The phononic framing rule's IS-not-IN table (`.claude/rules/phononic-framing.md`)
- Question: do the prefactors {34.146 MHz, 200 ppm, 0.5 s^-1} have substrate-first derivations from D_K spectral moments at the platform's compactification ratio? Or are they imported as independent dimensional anchors from CGS/SI?
- If imported: classify as METHODOLOGICAL DEBT (acceptable for translation-only gate) or as STRUCTURAL CONTRADICTION (substrate-first claim violated)

---

### Candidate 6 — Detection-ratio rank-order vs. rank correlation across platforms: do the 3 platforms agree on which lambda direction is most decisive?

**What it would do**: Test the structural prediction that the substrate's lambda-direction structure should produce a CONSISTENT rank-ordering across the 3 platforms. Read off the rank order of d_r within each platform: 3He-A {SW1=58958.864, XA1=58958.864, XB1=19652.955} (so λ_6 sweet-spot tied with cross-platform A, λ_7 cross-platform B is 3× lower); FeSe {SW2=72.904, XA2=30.696, XB2=72.904} (so λ_7 sweet-spot tied with cross-platform B, λ_6 cross-platform A is 2.4× lower); 173Yb {SW3=28.5, XA3=54.938, XB3=131.852} (so λ_8 sweet-spot is the LOWEST, λ_7 cross-platform B is the HIGHEST — 4.6× higher than native). The 173Yb pattern is anomalous: the platform's NATIVE direction (λ_8 sweet-spot) gives the LEAST decisive prediction, while a CROSS-platform reading (λ_7) gives the MOST decisive. This contradicts the implicit "compactification resonance" claim in the C5 phenomenology_note (line 53).

**Why it's worthwhile**: The WP framing (line 53) calls SW1/SW2/SW3 the "compactification-resonance rows: maximum projection of the framework-unique direction onto its native lab." But the 173Yb numbers contradict this: SW3 d_r=28.5 is BELOW XA3 d_r=54.9 and XB3 d_r=131.9. Either (a) "compactification-resonance" is the wrong mental model for 173Yb specifically; (b) the W8-4 ratios were computed under a Jensen-deformed inner product where projection magnitude doesn't correlate with physical detectability; or (c) the σ_detect for 173Yb (0.05 s^-1, theoretical floor) is the wrong normalization and the actual single-shot floor would re-rank. Either way, the 9-row table has a structural inconsistency hidden in the cross-platform sub-block that the C5/C6 verdicts didn't surface. A workshop would adjudicate which of (a)/(b)/(c) is correct, and what it implies for the W14-W6 NEW row class downstream.

**Type**: solo (2 agents)

**Suggested agents**: volovik-superfluid-universe-theorist, mack-cosmic-bridge

**Rounds (workshops only)**: N/A (independent solos, then a brief adjudication)

**Context the workshop will need**:
- 9-row CSV with d_r per row
- Per-platform rank ordering (computed above):
  - 3He-A: λ_6 ≥ λ_7 (factor 3)
  - FeSe: λ_7 > λ_6 (factor 2.4) — native > cross
  - 173Yb: λ_7 > λ_6 > λ_8 (native LOWEST)
- The "compactification resonance" claim in WP line 53
- The 173Yb anomaly: native sweet-spot is least decisive
- Question: why does 173Yb's native λ_8 reading come in last? Three hypotheses (a/b/c above); pick one, defend.
- If hypothesis (b): the 9-row table needs to be reinterpreted under the Jensen-deformed inner product, not under Euclidean rank-ordering — this changes how W14-W6 reads leveling.

---

### Candidate 7 — Cross-pillar synthesis: lab-falsifier vs cosmic-falsifier portfolio coherence

**What it would do**: Examine whether the 9-row LAB-FALSIFIER portfolio is coherent with the existing cosmic-scale falsifier portfolio (BK-Array 2026, DESI DR3, LISA, LiteBIRD, CMB-S4, CMB-HD, SKA-1) listed in the WP wave synthesis (line 333). The WP says the lab corridor "runs alongside, not in place of" the cosmic corridor. But the framework claims one spectral triple, one D_K, one substrate. If the substrate's λ_6 direction is decisive at 3He-A (d_r=5.9e+04) AND at LiteBIRD (cosmic-scale CMB polarization), the two predictions should be CORRELATED — a null at LiteBIRD should pre-bias expectations on the 3He-A reading. The WP currently treats lab and cosmic falsifiers as independent.

**Why it's worthwhile**: This is a structural-coherence question that the W11 wave didn't address. If 9 lab rows + N cosmic rows are genuinely independent falsifiers, the framework's joint-falsification probability is the product of per-row P_decisive — which would be EXTREMELY strong (a 9-row null + N-row null compounds the framework's exclusion). But if they're correlated (because they all probe D_K at different compactification ratios), the joint probability is much weaker. The framework's strength is that it has ONE structural source (the spectral triple) generating predictions across scales — that's the cross-pillar coherence. A workshop would map the correlation structure: which lab rows correlate with which cosmic predictions, what's the coupling strength, and how does this affect Bayesian updating on null/positive 2026-2031 outcomes.

**Type**: 3-agent workshop

**Suggested agents**: mack-cosmic-bridge, sagan-empiricist, connes-ncg-theorist

**Rounds (workshops only)**: 2

**Context the workshop will need**:
- 9-row lab-falsifier table (LAB-FALSIFIER level ladder)
- Cosmic falsifier portfolio per WP line 333: BK-Array 2026, DESI DR3, LISA, LiteBIRD, CMB-S4, CMB-HD, SKA-1
- W8-4 substrate predictions at PASS (S85)
- The "ONE spectral triple, ONE D_K" claim from `.claude/rules/phononic-framing.md`
- Question: what is the correlation matrix between lab d_r values and cosmic-falsifier predictions? Are they (a) independent (factor in joint product), (b) fully correlated (joint P_decisive = max single P_decisive), or (c) partially correlated through a shared D_K spectral moment?
- Decision: pre-register the correlation structure for S87+ joint Bayesian updating

## Notes on what I did NOT propose

- I did not propose recomputing W8-4 magnitudes — they are FROZEN per the FROZEN-PREDICTION-DISCIPLINE-COMMIT (WP line 337) and S85 PASS at `S85-W8-4-SU3-OP-LAB-PREDICTIONS`. Any workshop that touches the magnitudes is closed by precedent.
- I did not propose a "level-shuffle" workshop — the WP explicitly notes (JSON line 229) `is_shuffle_of_existing_tier: false`. This is a NEW class, not a re-binning.
- I did not propose a workshop on the C5 INFO clause itself — the INFO band fired correctly per plan §9, all 9 rows are populated, the provisional flag is documented, and the PASS-completeness for downstream landing is preserved. C5 INFO is a clean closure, not a deferred result.
- I did not propose work that duplicates the W14-W6 NEW row class landing — that's the next session's work, scheduled by W14 planner per the carry-forward messages (WP line 295).
- I did not propose a workshop on the 173Yb d_r=28.5 row's marginal placement above the A-level floor of 10 — by the pre-registered ladder it's clearly level A; convention-shopping the threshold to demote it would be PROHIBITED_ACTIONS Class 1 per `.claude/rules/v3-closure-recovery.md`.
