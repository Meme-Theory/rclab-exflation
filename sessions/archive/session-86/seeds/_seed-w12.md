# Seed file — sessions/archive/session-86/session-86-w12-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w12-workingpaper.md` (668 lines read in full)

## Reading summary

W12 is a META-infrastructure-anchoring wave with 5 gates owned by `mack-cosmic-bridge`: C30 detector-readiness 9-cell matrix (PASS), C31 BK-Array 2026 4-branch classifier pre-build (PASS), C32 Fisher-PDF SHA-pin closure with W4-3 + W4-6 re-emissions (PASS), C33 DR3 3-layer L_max ∈ {8,10,12} sub-tree (INFO, n_step=1 STEP-MONOTONE cell C1 with sequence (PASS, PASS, FAIL)), C36 CMB-HD α_s quarterly poll (INFO, NO-PUBLICATION-YET expected). All verdict lines + dual-SHA companion rows verified on disk at `computations/s86_gate_verdicts.txt` lines 174–196; three framework registries written and on disk.

The substantive openings are concentrated in **C33** (the only PHONONIC gate in the wave; surfaces a substrate-physical L=12 phantom-side excursion of `w_0_FW(L=12) = −0.976` crossing the R_842 lower boundary by 0.034 ≈ 17% of half-width) and in **convention dependence** (C33 §6(e) — rho-direct convention OSCILLATES, canonical-anchored convention is monotone — itself a methodological substrate-vs-bookkeeping discrimination). C36's polling unearthed an observation-side cross-domain signal (Fairbairn+ 2025 arXiv:2511.01612 reporting >2σ joint α_s/β_s indication from Planck+ACT DR6+SPT-3G+eBOSS Lyα) that the wave correctly classified as not-a-CMB-HD-detection but did not pursue as a framework-prediction validity-check. C32 and C30 expose minor SOURCE-RECON Class-(c) issues (`r_PathH = 0.00745` plan-pinned, oral citation only, untraceable in knowledge index). Five candidates worth scheduling.

## Candidates

### Candidate 1 — DR3 L=14+ deep-dive: substrate-genuine phantom migration vs sub-threshold ripple

**What it would do**: Extend the Zubarev rho(L) convergence series (currently at L ∈ {8, 9, 10, 11, 12} from S85 W0-7) to L ∈ {13, 14, 15} and fire the pre-registered 3-branch decision rule from C33 §"Carry-forward (S87+)". Decision tree on the C1 cell sequence: (PASS, PASS, FAIL, FAIL, FAIL) → substrate-genuine R_842 → R_phantom rectangle migration; (PASS, PASS, FAIL, PASS, PASS) → oscillation revealed, INFO converts retroactively to FAIL; (PASS, PASS, FAIL, PASS, FAIL) or (PASS, PASS, FAIL, FAIL, PASS) → n_step ≥ 2, deeper L-extension warranted. The 35-cell L_max × cell matrix would be the artifact.

**Why it's worthwhile**: This is the wave's only PHONONIC carry-forward and is explicitly pre-registered as `S87-DR3-LMAX-12-DEEP-DIVE` in C33 §"Carry-forward (S87+)" + §"Coexistence with W3-G42". The L=12 prediction `w_0(L=12) = −0.976` lies 0.034 OUTSIDE R_842 on the phantom side (canonical lower bound −0.942). Confirming this as substrate-genuine vs sub-threshold artifact is what determines whether the W3-G42 R_842 rectangle (S83 anchor, S84 W1b-9 lock 2026-04-23) needs migration to R_phantom — a structural change to the framework's DR3 prediction class. The required computation is L_max=14+ Zubarev rho extension; the GPU-pin is open in the C33 spawn-prompt design. The 3-branch decision rule is fully pre-registered; downstream W3-G42 coordination is also pre-registered. EVOI is high because the 3 branches map to genuinely distinct framework states (rectangle migration vs hard FAIL vs continued INFO).

**Type**: solo (1 agent)

**Suggested agents**: `mack-cosmic-bridge` (extends C33's authorship; shortest provenance chain) OR `volovik-superfluid-universe` (Volovik-effacement physics is the substrate basis of the canonical-anchored convention; he holds the project memory `project_volovik-convergence.md` + `project_substrate-compaction-timescape.md` directly relevant)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: Gate ID `S87-DR3-LMAX-12-DEEP-DIVE` (pre-registered in C33 carry-forward §"Carry-forward (S87+)" lines 492–496); input pin `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.npz` (SHA `cdfe9d62...`); upstream cache `computations/s84_spectrum_cache_L12_tau019.npz` for fresh L=13/14/15 D_K eigvals (`torch.linalg` GPU pin per `.claude/rules/computation-environment.md`); canonical anchor `w_0_FW = −0.918` (canonical_constants.py L1215; offset = −0.340827 absorbing S58 effacement); R_842 boundary `w_0 ∈ [−0.942, −0.742]` (S84 W1b-9 lock); 3-branch decision rule from C33 §492–496; cell predicates from W12-4 §"Cell roster" lines 379–388 (C1..C7); coexistence note with W3-G42 (S83) + R_842 (S84 W1b-9). PASS/INFO/FAIL band per C33 plan §9 (≤ 2 step-monotone INFO; ≥ 3 FAIL; oscillation FAIL).

---

### Candidate 2 — DR3 convention-lockdown formalization: rho-direct vs canonical-anchored substrate-vs-bookkeeping demarcation

**What it would do**: Promote C33's cross-cutting finding §6(e) — that rho-direct convention produces OSCILLATION FAIL while canonical-anchored convention produces monotone INFO — into a formal substrate-vs-bookkeeping demarcation theorem. Specifically: derive the equivalence class of admissible regulator-stability conventions under the constraint that they preserve S58 Volovik-partition effacement, prove that rho-direct violates this preservation, register the canonical-anchored convention as the S87+ binding form for ALL DR3-class L_max-stability gates, and formalize the precedent for similar gates that may arise elsewhere (e.g., w_a stability, alpha_s stability). The artifact is a permanent rule entry plus a worked demonstration that the OSCILLATION pattern under rho-direct is a regulator artifact, not substrate physics.

**Why it's worthwhile**: C33 §6(e) explicitly says "CONVENTION CHOICE is determinative for whether a regulator-stability gate FAILs (oscillation) or INFOs (step-monotone). The substrate-correct convention is canonical-anchored (preserves S58 Volovik effacement)" and pre-registers `S87-DR3-CONVENTION-LOCKDOWN-MEMO`. This is exactly the kind of substrate-vs-container demarcation the project's `phononic-framing.md` rule cares about: the rho-direct convention IS container-thinking (treats rho as the cosmological observable) while canonical-anchored is substrate-thinking (preserves the Volovik-effacement physical content as an additive offset). Without lockdown the Class-1 PROHIBITED_ACTIONS (`v3-closure-recovery.md`) "convention-shopping" failure mode is structurally available — a future agent could re-fire the gate under rho-direct, get FAIL, declare it informative, and accidentally retract substrate physics. EVOI is high because the lockdown is the prerequisite for any further regulator-stability gate landing reliably.

**Type**: solo (2 agents) — independent reviews to triangulate the demarcation rule

**Suggested agents**: `connes-ncg-theorist` (NCG-side: spectral-action regulator dependence, Wodzicki-trace homogeneity; he can derive what regulator class preserves S58 Volovik effacement at the spectral-triple level) AND `lizzi-spectral-functional-theorist` (functional-analysis-side: convention-equivalence under monotone reparametrization of the regulator axis)

**Rounds (workshops only)**: N/A (solo independent reviews; consolidator stitches)

**Context the workshop will need**: C33 §6(e) verbatim (lines 622–623); pre-registered S87 gate ID `S87-DR3-CONVENTION-LOCKDOWN-MEMO`; canonical_constants.py `w0_FW = -0.918` provenance (S58 Volovik partition + effacement; L1215); rho_Zubarev(L=10) = -0.577173, offset = -0.340827 (C33 §391–395); precursor S85 W1b-1 OSCILLATION pattern C4-C1-C4 under rho-direct (C33 §"Cross-check (precursor S85 W1b-1 rho-direct scheme)" lines 405); S58 Volovik partition gate (`S58 VOLOVIK-PARTITION-58 = INFO Variant B NROY=0.18%`, see agent memory `s58_volovik_partition.md`); `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class-1 convention-shopping; `.claude/rules/phononic-framing.md` substrate-vs-container demarcation. Decision rule for the demarcation theorem: a convention is "substrate-correct" iff (a) it preserves S58 effacement as an additive constant under L_max variation AND (b) does not introduce regulator-induced cell-flips that the substrate prediction itself does not predict.

---

### Candidate 3 — Fairbairn+ 2025 (arXiv:2511.01612) >2σ α_s/β_s observational hint vs framework prediction

**What it would do**: C36's literature scan unearthed Fairbairn-Heurtier-Olea-Romacho 2025 (arXiv:2511.01612) reporting a >2σ joint α_s/β_s indication from Planck+ACT DR6+SPT-3G+eBOSS Lyα. The wave correctly classified this as observation-side (not a CMB-HD detector forecast), so it did NOT trigger C36 PASS. But the wave-synthesis §5(c) explicitly flags: "if α_s running is observationally hinted at >2σ, the framework's α_s prediction (S85 W1b-6 = +0.0023) acquires sharper relevance." The workshop reads the Fairbairn+ paper, extracts their joint posterior or marginal contour for (α_s, β_s), and tests where the framework's central values sit relative to that contour. Specifically: framework α_s_inflation_framework = -0.068968 (canonical_constants.py n_s²-1 identity), framework β_s = ? (need to identify if framework has a β_s prediction or if S85 W1b-8 +0.0023 ACT DR4 update IS the proxy), Planck pivot α_s = -0.0045 ± 0.0067. Compute: under Fairbairn+'s posterior, where does the framework prediction lie? Inside 1σ, 2σ, 3σ? Outside?

**Why it's worthwhile**: This is a genuine framework-validity test that the wave correctly identified but did not pursue (C36's gate criterion was CMB-HD detector forecast detection, not observational-data adjudication). The framework's alpha_s prediction is locked at -0.068968 via n_s²-1 (S50-51 identity, permanent theorem). A >2σ observational indication of nonzero α_s/β_s is a NEW data input that bears on the framework's validity — completely independent of W12's META scope. The cross-domain signal noted in §5(c) of the W12 synthesis — `cross-domain signal: if α_s running is observationally hinted at >2σ, the framework's α_s prediction acquires sharper relevance` — is exactly the kind of pattern-detection-across-domains opening that should not get lost on the W12 cutting-room floor. The Fairbairn+ paper is paper-search-fetchable (already cited); the framework prediction is a permanent theorem; the comparison is a 1-day computation.

**Type**: solo (1 agent)

**Suggested agents**: `mack-cosmic-bridge` (he cited the paper in C36 §523; he holds the role per `feedback_mack-bridge-role.md`: Mack's priorities = user's observational priorities; this is a MACK-PRIMARY gate by construction)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: arXiv:2511.01612 Fairbairn+ 2025 abstract + posterior tables (paper-search-fetchable per C36's existing query trail); framework prediction `alpha_s_inflation_framework = -0.068968` (canonical_constants.py; provenance `S50-ALPHA_S=NS2-1` permanent identity); S85 W1b-6 framework β_s = +0.0023 ACT DR4 update (referenced in C36 §"trace_entity" line 519); Planck 2018 pivot α_s = -0.0045 ± 0.0067 (canonical_constants.py `planck_alpha_s`, `planck_alpha_s_err`); S86 detector-readiness 9-cell matrix row (c) CMB-S4 σ-target column (sigma_alpha_s_CMBS4 = 0.003, sigma_beta_s_CMB_S4 = 0.0022); decision rule: classify framework central position in {1σ-confirmation, 1σ-2σ-band, 2σ-3σ-tension, ≥3σ-FAIL} relative to Fairbairn+'s joint posterior. NOT a falsifier (Fairbairn+ is data-side; the framework is prediction-side; one >2σ paper is not framework-falsification), but a sharpening of the constraint-map row for α_s under post-2024 data.

---

### Candidate 4 — r_PathH primary anchoring closure (SOURCE-RECON Class-(c))

**What it would do**: Resolve the SOURCE-RECON Class-(c) issue surfaced in W12 synthesis §6(a): `r_PathH = 0.00745` is plan-pinned in W12-2 §7 (boundary-derivation comment table) but `mcp__knowledge__get_constant("r_PathH")` returns NOT-FOUND, `trace_entity("S85 W1b-6")` returns NO-TRACE, and the W12-2 script comment explicitly tags it `framework anchor (oral citation S85 W1b-6; not in canonical_constants)`. The workshop re-derives r_PathH from the primary substrate source (acoustic-route folded-shape relay prediction, per W12-2 §"Boundary-derivation comment block" provenance column), or locates the originating S85 verdict line that produced the 0.00745 numeric, then promotes the value to `computations/canonical_constants.py` with full session/source/gate provenance via `update_constant`. If primary-source re-derivation is impossible, document the value as oral-citation-only and lower its rule-status to "auxiliary anchor".

**Why it's worthwhile**: This is the W12 wave's only standing SOURCE-RECON debt — pre-registered by mack-cosmic-bridge himself in §6(a) as `S87-R-PATH-H-PRIMARY-ANCHORING`. The C31 (BK-Array classifier) PASS was structurally guaranteed by the boundary set, but its validity depends on r_PathH being the "framework Path-H" prediction with traceable provenance. Without a primary anchor, the entire BK-Array branch-2 confirmation region (Path-H + Path-C-central, the framework-survival region) rests on an oral citation. If a 2026 BK-Array publication lands at r_observed = 0.0075 (squarely on Path-H), the framework's "PASS" classification trace would lead back to a non-canonical, non-derivable number. EVOI is moderate but the provenance debt is structural — the rule-file `.claude/rules/epistemic-discipline.md` SOURCE-RECON sub-audit explicitly fires on this class.

**Type**: solo (1 agent)

**Suggested agents**: `mack-cosmic-bridge` (pre-registered the gate; knows where to look) OR `kaku-speculative-theorist` (acoustic-route folded-shape relay derivation is in the BK-Array Path-H lineage; if the primary derivation is missing, he is the agent who would be writing it for the first time)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: W12-2 §"Boundary-derivation comment block" lines 159–169 (provenance column says "acoustic-route folded-shape relay prediction"); W12-2 §"MCP Pre-Compute Audit" lines 132–137 (confirms r_PathH not a canonical constant; r_CMB_framework = 0.011731522176014426 is the canonical Path-C anchor from S83 W3-G46 TENSOR-TRANSFER PASS, but Path-H is unanchored); cross-reference S84 W4-42 / S85 W1a-4 livewatch tree (boundaries 0.005/0.018/0.030; cited in W12-2 §"Coexistence" line 229) — the Path-H/Path-C central separation lives there, may carry the primary derivation; decision rule for promotion to canonical_constants.py: re-derived value matches plan-pinned 0.00745 to 4 significant figures OR document the oral-citation path with explicit source-stub stating the value is an auxiliary anchor not eligible for `update_constant`. SOURCE-RECON taxonomy classification per `.claude/rules/epistemic-discipline.md` (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE; D_max calibration band).

---

### Candidate 5 — Two coexisting BK-Array trees: stress-test under joint synthetic firing

**What it would do**: W12-2 §"Coexistence with S85 W1a-4 livewatch" (lines 229) confirms that two distinct BK-Array 2026 4-branch trees coexist with different boundaries (W12-2: 0.005/0.015/0.030; S85 W1a-4: 0.005/0.018/0.030). Both fire on the SAME publication event. The wave-synthesis §2 says "distinct gate IDs, distinct epistemic questions (livewatch = framework-PASS-overall; this gate = Path-H-vs-Path-C discrimination); both fire on the same publication event without verdict-line collision." The workshop fires a synthetic 7-input panel `r ∈ {0.003, 0.0074, 0.0117, 0.014, 0.017, 0.025, 0.040}` (test points: below B1, exactly at Path-H, exactly at Path-C, between W12-2 b2_b3 and S85 b2_b3, in the contested 0.015–0.018 zone, in the extended Path-C tail, framework-falsified) through BOTH classifiers and produces a **joint discrimination matrix** — i.e., a 7×2 outcome table showing which (W12-2 branch, S85 branch) pair maps to which framework-state. The interesting region is `r ∈ (0.015, 0.018)` where W12-2 says branch-3 (Path-C extended tail) but S85 says branch-2 (Path-H + Path-C unified PASS). The workshop tabulates this contested region and emits a meta-classifier that combines both into a single substrate-state label set.

**Why it's worthwhile**: Both trees are operational and pre-committed. When BK-Array 2026 publishes r_observed, both trees will fire mechanically per their pre-registered boundaries — including in the contested 0.015–0.018 zone where they disagree. The framework's response posture should be deterministic, not "two mechanical classifiers fire and disagree". Either (i) the joint discrimination resolves cleanly via meta-classifier (each (W12-2, S85) pair maps to a unique substrate state), or (ii) the contested region surfaces a genuine epistemic question not yet pre-registered. The C31 verdict line says "boundaries are PINNED in §7; FAIL at any synthetic input would be a script-logic bug, NOT permission to shift boundaries" — meaning the boundary set is locked. The clean way to resolve possible disagreement is upfront, before publication, via an explicit joint discrimination matrix rather than ad-hoc post-publication tie-breaking. EVOI is moderate; structurally, this closes a small but real ambiguity in the framework's pre-registered response.

**Type**: solo (1 agent)

**Suggested agents**: `mack-cosmic-bridge` (authored both classifiers' related infrastructure; sole writer for `falsifier-master-inventory.md`)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: W12-2 §"Coexistence with S85 W1a-4 livewatch" verbatim (line 229); both classifier scripts on disk (`computations/s86_bk_array_2026_classifier.py` 18,729 B + `computations/s85_w1a_bk_array_livewatch.py` per S85 W1a-4); test-input panel `r ∈ {0.003, 0.0074, 0.0117, 0.014, 0.017, 0.025, 0.040}` (one per regime + one in contested zone); both classifiers' boundary sets (W12-2: 0.005/0.015/0.030; S85: 0.005/0.018/0.030); framework anchors r_PathH = 0.00745, r_PathC = 0.011731522176014426; substrate-state interpretation per W12-2 §"Substrate-framing reminder" (line 225) — branches are substrate-state classifications, not measurement bins. Decision rule: emit joint discrimination matrix; flag contested 0.015–0.018 zone with a substrate-state resolution (does (branch-3, branch-2) collapse to a single substrate state? if not, what is the resolution?). Output: `sessions/framework/bk-array-joint-classifier.md` registry + meta-classifier helper.

---

## Notes on what was NOT promoted to a candidate

- **C30 detector-readiness 9-cell matrix updates**: the 3 admissibly TBD-S87 cells (CMB-HD framework-prediction MacInnis pin, SKA-1 α_fNL envelope, lab-analogs EISCAT_3D xi_E_GGE_inv) are explicit carry-forward items but each is a single-cell update, not a workshop. They are mechanical-update items per S87 Wn quarterly poll cadence, not pattern-detection-across-domains opportunities.
- **C32 W4-3 / W4-6 physics re-execution**: the wave explicitly carries forward `S87-W4-3-FISHER-REEXECUTE` and `S87-W4-6-FISHER-REEXECUTE` as physics scripts re-run under pinned σ-target chain. These are mechanical re-executions, not pattern-finding workshops; they belong in next-session compute mode, not in W12 follow-up.
- **C36 next-quarter poll (S87-Q3 2026-07-26)**: cadence carry-forward; no synthesis content until publication detection event fires.
- **W12 synthesis §6 cross-cutting findings (b), (c), (d)**: verdict-line normalization, slot-audit race-delay, plan-w12 cache-path correction. These are infrastructure / documentation hygiene items per `feedback_fix-in-session-never-defer.md`'s Class-d "minor-self-report" — they should be addressed via mechanical S87 plan entries, not as pattern-detection workshops.
- **r_PathC (0.0117) provenance**: already canonical (`r_CMB_framework = 0.011731522176014426` from S83 W3-G46 TENSOR-TRANSFER PASS). No SOURCE-RECON debt here, in contrast to r_PathH.
