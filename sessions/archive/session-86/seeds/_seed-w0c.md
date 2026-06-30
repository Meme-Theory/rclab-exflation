# Seed file — sessions/archive/session-86/session-86-w0c-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w0c-workingpaper.md` (1,452 lines read)

## Candidates

### Candidate 1 — Substrate-first canonical-source discipline: codify the W0c-3 pattern as a permanent rule

**What it would do**: W0c-3 documents an interesting pattern under §(b): the plan §W0c-3 hypothesis cited "vdd §VI extraction at L_max=2" as the source for `nonflat_T_correction_L2`, but on inspection the 14 vdd papers have NO §VI heading; the actual canonical source is the framework's own first-principles computation in S83 W2-G24 (Cartan-flat at τ_fold ⇒ R|_Cartan⁴ = 0). W0c-3 routes the canonical to substrate-first per phononic-framing.md, but the rule is not yet codified. Workshop produces a permanent rule at `.claude/rules/substrate-first-canonical-sourcing.md` enumerating: (i) when external-paper provenance is methodological vs canonical; (ii) the audit pattern (glob external source for the heading; if absent, route to substrate computation); (iii) canonicalize the W0c-3 routing decision as the worked example.

**Why it's worthwhile**: This pattern is structurally recurring — agents repeatedly cite external papers (vdd §VI, CM-2008, etc.) as canonical when the framework's own first-principles computation is the substrate-first source. W0c-3 caught it once and rerouted correctly, but the routing was ad-hoc per the gate's verdict §(b). Without codification, the next agent encountering "extract X from external paper §Y" will not know whether to route substrate-first. The W0c-3 audit trail (vdd has no §VI; substrate computation S83 W2-G24 PASS gives `correction_P1_T = 0.0`) is a perfect calibration corpus exemplar — pin it in the rule. This dovetails with the "IS Space, Not IN Space" mandate but operationalizes it at the canonical-sourcing level rather than the explanation-direction level.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist (closest match for canonical-sourcing discipline given S82 lizzi atlas authorship + 5A workshop sub-diff B in `agent-standards.md`)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: W0c-3 §(b) "Substrate-first vs methodological-source distinction (entry #5)" verbatim; S83 W2-G24 verdict + npz file path; the 5 W0c-3 canonical landings as the calibration corpus (each with its substrate-first source vs methodological-cross-check); phononic-framing.md "IS Space, Not IN Space" mandate; the W0c-3 §(b) bash output showing zero §VI matches across 14 vdd papers as the worked example. Output deliverable: `.claude/rules/substrate-first-canonical-sourcing.md` with audit-pattern + worked-example + carry-forward audit script analogue (pattern: `_substrate_first_provenance_audit.py`).

---

### Candidate 2 — K_crit_BdG and K_base numerical coincidence: substrate-physics interpretation workshop

**What it would do**: W0c-2 §(f) flags a structural fact: `K_base = 2.035` (R3 band-weighted squeezing anchor, S82 W2-4) and `K_crit_BdG = 2.035` (BdG-channel critical coupling, S62 W2) coincide numerically but are documented as "semantically distinct" with DISTINCT-FROM enumeration. The W0c-2 verdict treats this as a coincidence requiring namespace separation. A focused workshop asks: *is this coincidence physical*? If the squeezing anchor and the BdG critical coupling lie at the same point in coupling-space, that is either (a) a numerical accident that future regulator refinements may break, or (b) a substrate-structural identity whose mechanism we have not yet articulated. The workshop attempts to derive whether the coincidence is structural — testing across L_max grid {8, 10, 12} (cache exists at all three) and across regulator schemes — and decides PROVEN-IDENTITY vs ACCIDENT-OF-FLOAT.

**Why it's worthwhile**: This is exactly the cross-domain pattern-detection mandate. Two semantically distinct couplings landing at the same point is either coincidence (and namespace separation is the right call) or hidden structure (and the namespace separation papers over a deeper identity). The DISTINCT-FROM block in W0c-2 records "if a future scheme refinement causes the two to diverge ... the namespace remains correct." That IS a pre-registered fork: do they diverge or not? L_max=10 cache has `K_base = 2.035` from S82 W2-4 and the moments cache exists. A direct K_base(L_max) and K_crit_BdG(L_max) extraction at L=8/10/12 would settle whether the equality is regulator-stable. If stable, the interpretation is structural; if drifting, the namespace separation is justified. Either outcome is a constraint-map update.

**Type**: 2-agent workshop

**Suggested agents**: volovik-superfluid-universe-theorist (BdG-channel canonical owner per S62 W2 derivation), connes-ncg-theorist (R3 band-weighted scheme + spectral structure)

**Rounds (workshops only)**: 2 default

**Context the workshop will need**: W0c-2 §(f) "Numerical-coincidence note" + the canonical_constants.py:124-138 K_crit_BdG block + canonical_constants.py:130 K_base block (both verbatim); S82 W2-4 producing artifact path; S62 W2 derivation routing via permanent-results-registry.md W2-12 row; the moments cache `s85_w12_elim1_D_K_Lmax_moments.npz` (L_max ∈ {8,10,12}, K_base scalar = 2.035 at L=10); pre-registered fork: PROVEN-IDENTITY iff K_base(L) = K_crit_BdG(L) to <1e-6 relative across all three L values AND across at least 2 regulator schemes; ACCIDENT-OF-FLOAT iff drift > 1e-3 relative at any (L, scheme) pair; INFO band in between.

---

### Candidate 3 — W0c-1 cache-provenance gap: pre-flight substrate-data audit infrastructure

**What it would do**: W0c-1 FAILed because the cache `s85_w12_elim1_D_K_Lmax_moments.npz` stores moments (a_2, a_4, R_JK, n_eigenvalues, K_base, …) but NOT raw eigvals. The plan §W0c-1 was authored under the stale assumption that 155984 raw eigvals existed in this cache. The carry-forward is `S87-LAMBDA-TOP-DIRECT-EXTRACTION-RERUN` (12-24h GPU regeneration). The workshop produces, BEFORE that 12-24h re-run is dispatched, a substrate-data cache audit infrastructure: a tool that walks every plan-pinned npz/csv file and verifies the cache contains the keys the plan expects. This is the substrate-data analog of `_yaml_gate_validator.py` (which W0c-5 surfaced as having scope-drift relative to the plan's literal lift instruction). Produces `computations/_cache_key_audit.py` + a cache-key registry at `sessions/framework/cache-key-registry.md`.

**Why it's worthwhile**: The same plan-vs-reality drift surfaced THREE times in this wave: W0c-1 (cache-content drift: moments vs raw eigvals), W0c-4 (cache-existence drift: producer script absent from repo), W0c-5 (cache-format drift: YAML vs markdown form for machinery_pin). All three are PRU-class plan-write-time failures where the plan author assumed an artifact state that didn't match reality. A cache-key audit infrastructure forecloses the W0c-1 and W0c-4 failure modes at plan-freeze time (PRU pipeline runs `_cache_key_audit.py` before plan-freeze; missing keys ⇒ plan-freeze halt with explicit remediation). The infrastructure is mechanical and well-defined: glob plan input-pin maps, extract cited keys, np.load each file, set-diff against the cited keys, report missing. The S87 re-run can then be triggered with confidence that the regenerated cache exposes the keys downstream gates need.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist (D_K cache structure expertise + spectral-action dependency tracing)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: W0c-1 §(a) six-sub-criterion table + §(b) cache-content vs plan-assertion gap (verbatim); W0c-4 §(c) substrate-derivation absence table; W0c-5 §(d) plan-vs-reality mismatches table; the canonical PRU pipeline order from `epistemic-discipline.md` §"PRU pipeline composition order"; existing infrastructure scripts to mirror: `_pru_cardinality_audit.py`, `_source_reconciliation_audit.py`, `_yaml_gate_validator.py`. Deliverable: `_cache_key_audit.py` + `cache-key-registry.md` + integration into the PRU pipeline at plan-freeze. Pre-registered PASS: at least one historic PRU-Class-8 cache miss (e.g., the W0c-1 missing eigvals key) is detected by the audit when run retroactively against the plan's input-pin map.

---

### Candidate 4 — W0c-5 validator-scope drift: clarify sig_4 metric definition before S87 plan-freeze

**What it would do**: W0c-5 surfaced a critical ambiguity: the plan-stated baseline was 9.2%, but the validator reports 17.65%. More importantly, the plan specified `schema_version: R3` insertion as the lift (a single-key check), while the validator's actual criterion is the full 8-item PRDR checklist (operator, strict_PASS_boundary, boundary_reachable_analytically, reachable_rationals, machinery_pin_map, audit_discriminators, substitution_chain, input_files). These are two completely different metrics. The carry-forward `S87-R3-COVERAGE-LIFT-STRUCTURED` is "LARGE multi-wave plan-revision effort", but it cannot start until the metric is unambiguous. Workshop adjudicates: is sig_4 (a) `schema_version: R3` presence OR (b) 8-item PRDR checklist completeness? The two have different remediation costs (mechanical insertion vs structural plan revision) and different effects on v3-closure-recovery Stage-1 routing.

**Why it's worthwhile**: Without disambiguation, S87 plan-write will encode the same plan-vs-reality drift that W0c-5 documented. The plan author will think `schema_version: R3` insertion is the lift; the validator will return 17.65%; the gate will FAIL again. This is the canonical iterate-until-the-metric-is-clear failure mode, and it is structurally distinct from convention-shopping (it's not gaming a result; it's that the plan and validator have always disagreed on what sig_4 means). The fix is upstream — adjudicate the metric, write it into both `v3-closure-recovery.md` sig_4 description AND `_yaml_gate_validator.py` docstring AND the plan-template's machinery-pin section. This forecloses recurrence.

**Type**: 2-agent workshop

**Suggested agents**: lizzi-spectral-functional-theorist (rule-file authority per recent rule landings), kitaev-topological-classifier (PRDR keyword-window / 8-K-atom enumeration ownership per `pru-pre-registration-template.md` §"PRDR keyword window")

**Rounds (workshops only)**: 2 default; R1 each agent presents their reading of sig_4 (schema_version single-key vs 8-item checklist) with grounding in the actual rule text; R2 converge on the canonical metric, write the rule-update + validator docstring + plan-template clarification.

**Context the workshop will need**: W0c-5 §(c) "Why the literal instruction had zero applicable sites" + §(d) plan-vs-reality mismatches table + §(g) Level-3 remediation route (verbatim); the literal text of `v3-closure-recovery.md` sig_4 remediation map (currently says "lacks the R3 YAML schema_version key"); `_yaml_gate_validator.py:73-82` REQUIRED_CHECKLIST_KEYS list (8 items); `_yaml_gate_validator.py:118-169` (the "EITHER form" YAML/markdown handling); pre-registered adjudication rule: the canonical sig_4 metric IS the validator's actual implementation (Source-Authority hierarchy: code is authoritative; rule-text is descriptive of code), so the rule-text and plan-template must be updated to match the 8-item checklist, not the other way around.

---

### Candidate 5 — W0c-7 NSDW vs SDW classification: design the 20k retrofit's machine-assistance

**What it would do**: W0c-7 FAILed because the 20,343 bare-`a_n` hits across 638 files cannot be safely auto-tagged — most are non-Seeley-DeWitt (lattice spacings, polynomial coefficients, generic indices). The carry-forward `S87-A-N-SEELEY-DEWITT-RETROFIT` is "10-20h manual review". A focused workshop asks: can context-classification be automated to triage SDW vs NSDW with high precision? The semantic context is rich: SDW occurrences appear in heat-kernel expansion code (`spectral_action`, `seeley_dewitt`, `Mellin-Barnes`, `zeta-regulated`); NSDW occurrences appear in lattice/polynomial/index contexts. A grep-window classifier (10 lines around each match) + keyword whitelist (`heat_kernel`, `Seeley`, `a_n`-as-coefficient, `Mellin-Barnes`) + per-file dominant-context detection can probably triage 90%+ correctly. Workshop produces the classifier + a sample retrofit on the top-10 offending files (e.g., `s42_constants_snapshot.py`: 79 hits) as calibration. The remaining tail can then be hand-reviewed in a fraction of the 20h estimate.

**Why it's worthwhile**: 20k violations is the largest open methodology debt in the wave, and the manual-review estimate (10-20h) is the binding constraint on closing it. If 90% can be triaged automatically — with the safety guard that auto-tagging proposes but doesn't commit, and a human reviews the proposed tagging in a single sweep — the 20h compresses to ~2-3h. This is high-leverage methodology work that is precisely the kind of pattern-detection across a domain (SDW physics has a recognizable lexical signature; NSDW physics does not) that this seed file's investigator is built for. PROHIBITED_ACTIONS.4 (no ansatz-forced PASS) is respected because the classifier proposes; the retrofit doesn't auto-commit; the human sweep makes the per-file decision.

**Type**: solo (2 agents) — co-author the classifier and the calibration corpus

**Suggested agents**: connes-ncg-theorist (Seeley-DeWitt + spectral-action domain expertise for lexical signature), gen-physicist (broad lexical context for NSDW occurrences in early-session code)

**Rounds (workshops only)**: N/A (parallel solos with shared deliverable)

**Context the workshop will need**: W0c-7 §(a) pre-pass audit population table + §(b) FALSE-POSITIVE-PRONE classification table (5 contexts) + §(e) Level-3 remediation route (verbatim); the actual top-10 file list from the audit JSON (`s86_w0c_7_a_n_regulator_pin_discipline.json`); the existing `_a_n_regulator_pin_audit.py` to extend with classification mode; pre-registered PASS: the classifier achieves ≥90% precision on a hand-labeled 200-occurrence calibration set (100 SDW exemplars + 100 NSDW exemplars manually selected by the agent before the classifier runs). Deliverable: `_a_n_regulator_pin_classifier.py` + calibration JSON + sample retrofit on `s42_constants_snapshot.py` with proposed tags annotated for human review.

---

### Candidate 6 — External-clock scaffold: pre-fire BK-Array decision-tree validation against framework predictions

**What it would do**: W0c-8 PASSed: the 11-session scaffold pre-registers a 4-branch decision tree for the BK-Array 2026 r-tensor-to-scalar publication. Branch 1 (r ∈ [0, 0.005)) → Path-H r=0.00745; Branch 2 (r ∈ [0.005, 0.015)) → Path-H r=0.00745 (consistent); Branch 3 (r ∈ [0.015, 0.030)) → Path-C r=0.0117; Branch 4 (r ≥ 0.030) → BOTH-PATHS excluded. The branches are pre-registered, but the *consistency* between framework prediction and branch boundary has not been verified. Specifically: Path-H predicts r=0.00745, which sits at the upper edge of Branch 1 and inside Branch 2 — so a BK-Array measurement at r=0.0074 lands in Branch 1 (null), while r=0.0075 lands in Branch 2 (consistent). This is a 1.3% sensitivity on the branch verdict from the BK-Array measurement uncertainty. Workshop computes the actual BK-Array 2026 expected sigma_r, the framework's Path-H r prediction uncertainty band, and the joint probability of each branch firing. Produces a quantitative pre-registration table (P(Branch i | framework, measurement_uncertainty)) so the S88 ingest is interpretable.

**Why it's worthwhile**: A pre-registration table that doesn't account for measurement uncertainty bands is a coarse pre-registration that can fire in the "wrong" branch via a 1-sigma fluctuation. The framework's r predictions have their own uncertainty bands (Path-H r=0.00745 with what error?). Without joint probability analysis, the S88 ingest will be a deterministic branch-from-central-value, which may not honor the actual statistical content of the data. This is the Mack observational-priority discipline operationalized: pre-register not just the branches but the probability mass within each branch given the framework + measurement model. This makes the S88 ingest a Bayesian update rather than a deterministic switch.

**Type**: 2-agent workshop

**Suggested agents**: mack-cosmic-bridge (observational-pipeline anchoring + BK-Array familiarity per `feedback_mack-bridge-role.md`), sagan-empiricist (statistical pre-registration + measurement-uncertainty propagation)

**Rounds (workshops only)**: 2 default

**Context the workshop will need**: W0c-8 §(c) S88-BK-ARRAY-INGEST 4-branch decision tree (verbatim); the framework's Path-H r=0.00745 and Path-C r=0.0117 predictions with uncertainty bands (cite source: scaffold §2 + framework canonical r values); BK-Array 2026 published forecasted sigma_r (must fetch from external literature via paper-search MCP); deliverable: `sessions/framework/registry/external-clock-scaffold.md` §2 augmented with P(Branch i | framework, measurement_uncertainty) table (the freeze-no-re-pin discipline permits augmentation that doesn't change branches, only annotates them); `computations/s86_w0c_8_branch_probability_extension.py` for reproducibility; respect freeze-no-re-pin: the BRANCHES THEMSELVES are unchanged, only annotated with probability mass.

---

### Candidate 7 — Cross-pillar synthesis: K_crit_BdG vs Lambda_top vs scheme_floor — what's the substrate's coupling-space topology?

**What it would do**: W0c surfaces three substrate-coupling-space anchors with different roles: `K_crit_BdG = 2.035` (BdG-channel critical coupling, W0c-2 PASS), `Lambda_top = ?` (D_K top eigenvalue, W0c-1 FAIL pending re-run, expected band [4.5, 6.5]·M_KK), `scheme_floor = 12.5%` (W3-7 metric attainability boundary, W0c-9 PASS). These are three distinct anchors at different layers of the substrate's coupling-space topology: K_crit_BdG is in the BdG sub-corridor, Lambda_top is at the spectral ceiling, scheme_floor is the metric's attainability under the heat_kernel/Branch-A/L_max=10 scheme. Workshop maps the substrate's coupling-space topology layer-by-layer: K_R5 (1.9222) < K_crit_BdG (2.035) ≈ K_base (2.035) < K_crit (91.5) — and asks where Lambda_top, scheme_floor, K_floor, K_wall fit. The structural goal: produce a coupling-space topological diagram that organizes ALL the named scales in the substrate's coupling-space hierarchy.

**Why it's worthwhile**: The framework has accumulated ~10 canonical coupling-space scales (K_R5, K_crit_BdG, K_base, K_crit, K_floor, K_wall, K_FIRAS, scheme_floor, Lambda_top, M_KK), and the namespace pressure is mounting (W0c-2's DISTINCT-FROM block had to enumerate 4 distinct K_*-named scales to prevent confusion). A coupling-space topology map answers: which scales are upper bounds (K_crit, K_wall, Lambda_top), which are critical points (K_crit_BdG), which are anchors (K_base, K_R5), which are floors (K_floor, scheme_floor)? Without this map, future PRU vulnerabilities will repeat the K_crit triple-collision pattern. The map is also a substrate-physics insight: the named scales reflect the substrate's BdG/inflationary/spectral-ceiling structure; their relative positions encode the framework's spectral hierarchy. This is exactly the cross-domain pattern detection mandate (Pillar VIII KK on Lie groups + Pillar IV BCS flat bands + Pillar III NCG spectral structure all converge in coupling-space).

**Type**: 3-agent workshop

**Suggested agents**: connes-ncg-theorist (spectral-ceiling Lambda_top + scheme floor), volovik-superfluid-universe-theorist (BdG-channel K_crit_BdG, K_floor, K_wall), lizzi-spectral-functional-theorist (canonical-namespace authority per S82 lizzi atlas + recent canonical landings)

**Rounds (workshops only)**: 2 default; R1 each agent maps their domain's coupling-space scales onto a unified diagram; R2 converge on a canonical topological diagram + write `sessions/framework/coupling-space-topology.md`.

**Context the workshop will need**: All canonical_constants.py K_* + Lambda_* lines (verbatim); W0c-1 Lambda_top expected band; W0c-2 K_crit_BdG provenance + DISTINCT-FROM enumeration; W0c-9 scheme_floor 12.5% derivation (heat_kernel + Branch-A + L_max=10); the moments cache scalar values K_base = 2.035 at L=10; the S85 W2-12 PROVEN theorem `BdG band → CMB l_crit projection`; pre-registered deliverable: a 1-page coupling-space topological diagram (K-axis with scale ordering + each scale's role tagged) + the supporting registry markdown file at `sessions/framework/coupling-space-topology.md`. INFO-band acceptance: the diagram is descriptive (organizes existing scales), not prescriptive (does not propose new scales); future canonical landings can extend the map without re-pinning existing entries.
