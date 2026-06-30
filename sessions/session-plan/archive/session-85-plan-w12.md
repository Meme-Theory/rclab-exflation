# Session 85 Plan — Wave W12: gen-physicist-origin (structural-elimination next gates)

**Wave ID**: W12
**Owner**: gen-physicist
**Item count**: 4
**Source**: S84 s3-gen-elimination synthesis (ELIM-1..ELIM-8 carry-forwards)
**Output plan**: `sessions/session-plan/session-85-plan-w12.md`
**Verdict file**: `computations/s85_gate_verdicts.txt`
**Script prefix**: `s85_w12_<slug>.py`

## Wave W12 Summary

W12 is the gen-physicist-origin reviewer wave. All four items are next-elimination gates for mechanisms that survived the S84 structural-elimination workshop. Each gate probes a potentially-failing wall of the allowed substrate geometry, mapping constraint surfaces via H-SUR-1..H-SUR-4 next-probe logic.

Substrate framing: each ELIM gate measures the *walls* of the allowed region of the spectral triple (A_F, H, D_K)-space — not the falsification of an external cosmology. A PASS result pins the wall in place; a FAIL re-opens a direction for elimination. The direction of explanation flows FROM D_K eigenvalue structure → a_n Seeley-DeWitt moments → observable consequences; the gates instrument that flow at four distinct choke-points.

Item roster:

| Gate | Slug | ELIM origin | Probe target | Estimated effort |
|:-----|:-----|:------------|:-------------|:-----------------|
| S85-W12-ELIM-3 | `s85_w12_falsifier_catalog_extend` | ELIM-3 | Equivalence-class falsifier catalog lift 65→150 papers (W7a-7 closure) | 4h, CPU 8-thread |
| S85-W12-ELIM-6 | `s85_w12_prdr_consistency_audit` | ELIM-6 | Plan-layer PRDR consistency audit tool (hypothesis IMPLIES/CONTRADICTS each carry-forward) | 5h, CPU 1-thread (AST parse) |
| S85-W12-ELIM-1 | `s85_w12_branch_iv_reaudit_lmax` | ELIM-1 | Branch-(iv) re-audit at L_max ∈ {8, 10, 12} under inverted Josephson-dominance | 6h, GPU (torch.linalg on 155,984-eigenvalue D_K) |
| S85-W12-ELIM-8 | `s85_w12_w0_regulator_taxonomy` | ELIM-8 | W0-regulator-invariance taxonomy (CF-W4.1, companion to ELIM-4) | 4h, CPU 8-thread (5-regulator × 4-scheme scan) |

## Wave W12 Decision Point Prerequisites

Before dispatching W12 agents, the following artifacts MUST be on disk:

1. **canonical_constants.py** — all four gates import. Required constants: `M_KK`, `tau_fold`, `L_max_10`, `Delta_BCS`, `K_substrate`, `K_crit`, `K_R5`, `omega_L1`, `c_fabric`, `Vol_SU3`, `dS_fold`, `d2S_fold`, `S_fold`, `dt_transit`. If any missing, add with provenance + `update_constant(...)` BEFORE the wave dispatches.
2. **S84 s3-gen-elimination synthesis** — `sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md` (read-only reference; do NOT read during W12 per plan rules; contents already serialized into the four gate blocks below).
3. **D_K eigenvalue cache** at L_max ∈ {8, 10, 12} — for ELIM-1. If L_max=12 cache absent, ELIM-1 must emit PRE-REG-INCOMPLETE (Class-8 PRU) and the wave proceeds with the other three; L_max=12 is re-queued to a later wave.
4. **Plan file corpus** — ELIM-6's AST tool scans `sessions/session-plan/session-85-plan-w*.md`; the tool runs LAST in W12 (after the other three blocks commit their gate specs) so it has a non-empty corpus to audit.
5. **Verdict file** `computations/s85_gate_verdicts.txt` exists (created by W0 dispatch); W12 APPENDS, never creates.

## §W12-1. S85-W12-ELIM-3  (Extended equivalence-class falsifier catalog 65→150)

**1. Gate ID**: `S85-W12-ELIM-3`
**2. Trigger**: `[AUDIT]`
**3. Classification**: NON-PHONONIC (meta-epistemic: catalog completeness of the equivalence-class falsifier map for the S85-S90 horizon).
**4. Hypothesis**: The equivalence-class falsifier catalog (currently 65 papers as of W7a-7) remains complete-under-substrate-scope when extended to a target 150 papers. A PASS means the additional 85 papers add ZERO new framework-unique falsifier classes beyond the 12 already enumerated (k_sub-transit, f_DM-channel, K-corridor, HP^1 parity, L0/L3 dissonance, triality-orbit, KO-dim=6, rank-universality R_N, two-speed acoustic, c_sub, F_amp, partition-invariance). A FAIL identifies a ≥1 previously-unmapped class.
**5. Pass / Fail / INFO threshold**:
  - PASS: Δ(class_count) = 0 AND coverage_fraction ≥ 0.95 (≥ 143 of 150 papers assigned to an existing class).
  - FAIL: Δ(class_count) ≥ 1 (new class discovered — structural extension of falsifier map required).
  - INFO: 0.85 ≤ coverage_fraction < 0.95 (no new class but catalog sparse on S88-S90 frontier — schedule mid-session re-audit).
  - Tolerance rule: ABSOLUTE on Δ(class_count) and coverage_fraction.
**6. Machinery pin (PRDR)**:
  - `N_papers_source = 150` (extend from W7a-7 snapshot at 65; draw from researchers/{Baptista, Volovik, Kaluza-Klein, Antimatter, Little-Red-Dots, Einstein} indices + fresh arXiv 2025-2026).
  - `class_enumerator_version = "s85_w12_v1"` (frozen vocabulary of 12 classes above).
  - `assignment_rule = "majority_vote_among_3_keyword_buckets"` — each paper assigned via 3 disjoint keyword sets; if 2/3 agree, class fixed; if 0/3 or 3/3 disagree, flagged for manual review.
  - `scan_range`: papers published 2020-01-01 to 2026-04-21.
  - `step_size`: N/A (categorical).
  - `tolerance`: integer comparison on class_count, 0.01 on coverage_fraction.
  - `scheme = "catalog-extension"`, `convention = "equivalence-class-disjoint"`.
  - `random_seed = None` (deterministic catalog lookup; no sampling).
  - `GPU path`: N/A; CPU 8-thread for keyword filtering.
**7. Input SHA-256 pins**:
  - `researchers/index.md` — `<computed-at-runtime>`
  - `researchers/Baptista/index.md` — `<computed-at-runtime>`
  - `researchers/Volovik/index.md` — `<computed-at-runtime>`
  - `researchers/Kaluza-Klein/index.md` — `<computed-at-runtime>`
  - `researchers/Antimatter/index.md` — `<computed-at-runtime>`
  - `researchers/Little-Red-Dots/index.md` — `<computed-at-runtime>`
  - `sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md` — `<computed-at-runtime>` (W7a-7 baseline reference)
  - `computations/canonical_constants.py` — `<computed-at-runtime>`
**8. Expected output 4-tuple**: `(value=<Δ_class_count, coverage_fraction>, scheme=catalog-extension, convention=equivalence-class-disjoint, L_max=n/a)`
**9. Substitution chain** (for the "no new class" direction claim):
  - Step 1: class_count(W7a-7) = 12 (definition, from W7a-7 row 5; frozen).
  - Step 2: new_paper_set = {p_66, …, p_150} with |new_paper_set| = 85 (construction).
  - Step 3: For each p_i in new_paper_set: assign(p_i) ∈ {C_1, …, C_12, C_new}; class_count after = 12 + |{C_new occurrences}|.
  - Step 4: PASS ⇔ |{C_new occurrences}| = 0 ⇔ every new paper fits an existing class.
  - Step 5: Direction: adding papers can ONLY INCREASE OR HOLD class_count; it cannot decrease it. Therefore PASS requires strict containment of the new evidence within the existing 12-class partition. The gate's conclusion is one-sided (non-decreasing), which is why the PASS threshold is ABSOLUTE (= 0) not RATIO.
**10. PHONONIC classification rationale**: This is NON-PHONONIC (catalog/meta-epistemic). It does not compute a D_K moment. It audits whether the substrate-falsifier-class partition, as induced by the 12-class taxonomy, spans the observational literature horizon out to S90. A PASS narrows the uncertainty on "could a paper outside our corpus falsify an unmapped framework signature?"; a FAIL *adds* a new class to the constraint map, which is itself a substrate-geometric result (a new wall was missed).
**11. What PASS means**: The 12-class falsifier partition is stable-under-corpus-extension for the current paradigm horizon. Substrate walls as currently mapped are a complete cover of the observational frontier; no hidden falsifier direction.
**12. What FAIL means**: A new framework-unique falsifier class exists in the 2025-2026 literature. This is a *gain* for the constraint map: a previously-unmapped substrate wall has been identified. The new class name and its associated observable(s) must be added to the permanent-results-registry as a pre-registered S86+ gate.
**13. Producing script & verdict-line target**: `computations/s85_w12_falsifier_catalog_extend.py`. Emits canonical verdict line `S85-W12-ELIM-3: PASS|FAIL|INFO -- value=<Δ,frac> scheme=catalog-extension convention=equivalence-class-disjoint L_max=n/a sha256=<64-hex>` via atomic `open("a")` append to `computations/s85_gate_verdicts.txt`. Uses `.claude/templates/script-template.py` scaffold. Data artifact: `computations/artifacts/s85_w12_elim3_catalog.json` (paper → class map). Plot: `computations/artifacts/s85_w12_elim3_hist.png` (class-population histogram).

## §W12-2. S85-W12-ELIM-6  (Plan-layer PRDR consistency audit tool)

**1. Gate ID**: `S85-W12-ELIM-6`
**2. Trigger**: `[AUDIT]`
**3. Classification**: NON-PHONONIC (infrastructure: plan-file consistency audit via AST parse).
**4. Hypothesis**: Each session-85 carry-forward hypothesis, when pre-registered as a gate block, either IMPLIES or CONTRADICTS every other carry-forward in a deterministically-computable, logged way. No pair of gates in the W0-W13 set is *silently mutually irrelevant* (which would indicate a missing cross-wave cross-check) AND no pair is *silently contradictory* (which would indicate a PRU Class-8 plan-property failure).
**5. Pass / Fail / INFO threshold**:
  - PASS: 100% of gate-pair (i, j) relations classified by the tool's four-valued predicate {IMPLIES, CONTRADICTS, INDEPENDENT-DECLARED, ORTHOGONAL}. Count of pairs classified UNDECLARED = 0.
  - FAIL: ≥ 1 pair with CONTRADICTS verdict (surfaces a plan-level contradiction requiring pre-dispatch mediation).
  - INFO: 0 < UNDECLARED ≤ 5% × total_pairs (plan mostly-classified; remaining pairs documented as carry-forward to W14-consolidation).
  - Tolerance rule: ABSOLUTE on UNDECLARED count; ABSOLUTE on CONTRADICTS count.
**6. Machinery pin (PRDR)**:
  - `plan_corpus = sessions/session-plan/session-85-plan-w{0, 1a, 1b, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}.md` (all 15 wave plans must exist on disk at tool-run time).
  - `gate_extractor_version = "s85_w12_ast_v1"` — regex `^##\s+§\S+\.\s+(\S+)` for gate-block headings; hypothesis extracted from the "Hypothesis" field.
  - `predicate_classifier = "keyword_overlap + observable_crossref"` — two-factor: (a) shared observable (e.g. both gates constrain α_s), (b) shared mechanism (e.g. both invoke f_conv).
  - `scan_range`: all gate IDs listed in each plan's summary table.
  - `step_size`: N/A.
  - `tolerance`: integer on UNDECLARED and CONTRADICTS; decimal 0.01 on coverage ratio.
  - `scheme = "plan-layer-prdr"`, `convention = "four-valued-predicate"`.
  - `random_seed = None` (deterministic AST parse).
  - `GPU path`: N/A; CPU 1-thread (parse-bound, not compute-bound).
**7. Input SHA-256 pins**:
  - `sessions/session-plan/session-85-plan-w0.md` — `<computed-at-runtime>`
  - `sessions/session-plan/session-85-plan-w1a.md` through `session-85-plan-w13.md` — `<computed-at-runtime>` (14 files)
  - `sessions/session-plan/session-85-partition.md` — `<computed-at-runtime>`
  - `computations/canonical_constants.py` — `<computed-at-runtime>`
  - This W12 plan file itself is excluded from self-audit.
**8. Expected output 4-tuple**: `(value=<N_IMPLIES, N_CONTRADICTS, N_INDEPENDENT, N_UNDECLARED>, scheme=plan-layer-prdr, convention=four-valued-predicate, L_max=n/a)`
**9. Substitution chain** (for "CONTRADICTS implies FAIL" direction):
  - Step 1: total_pairs = C(N_gates, 2) where N_gates = Σ over W0-W13 of items-per-wave = 129 (definition, from partition manifest).
  - Step 2: For pair (g_i, g_j): classified_as(g_i, g_j) ∈ {IMPLIES, CONTRADICTS, INDEPENDENT-DECLARED, ORTHOGONAL, UNDECLARED}.
  - Step 3: N_CONTRADICTS = |{(i, j) : classified_as(g_i, g_j) = CONTRADICTS}|.
  - Step 4: PASS predicate: N_UNDECLARED = 0 AND N_CONTRADICTS = 0.
  - Step 5: Direction: a single CONTRADICTS pair SUFFICES to fail the PASS predicate (quantifier structure: ∀ pairs, classification ≠ UNDECLARED AND classification ≠ CONTRADICTS). The direction is one-sided (non-falsifying only under total absence of contradiction), which is why N_CONTRADICTS ≥ 1 → FAIL is ABSOLUTE and NOT threshold-tuneable.
**10. PHONONIC classification rationale**: NON-PHONONIC (infrastructure). Does not compute a D_K observable. Instead, it is a plan-integrity tool that closes the Class-8 PRU failure mode at the plan-authoring layer. A PASS certifies that the session-85 plan is internally consistent BEFORE any compute dispatches; a FAIL surfaces a plan-authoring defect requiring a targeted orchestrator edit. This is structurally the next layer above the gate-level PRDR: gate-layer PRDR enumerates free parameters within one gate; plan-layer PRDR enumerates consistency relations across gates.
**11. What PASS means**: Session-85's 129 carry-forwards span a consistent constraint-geometry. Every pair is either explicitly related (IMPLIES/CONTRADICTS) or explicitly orthogonal — no silent gaps, no silent contradictions. The wave-by-wave dispatch strategy is safe from the kind of plan-property failure that generated S78's scrubbed-re-run floatation.
**12. What FAIL means**: The plan has a contradiction (two gates cannot simultaneously PASS under their pre-registered predicates) OR a UNDECLARED count exceeding the INFO band. In either case, orchestrator must mediate BEFORE dispatch (e.g., weaken a threshold, split a gate, or explicitly declare independence). The FAIL is a *gain* for the plan-integrity constraint map: a previously-hidden plan-layer relation is now surfaced.
**13. Producing script & verdict-line target**: `computations/s85_w12_prdr_consistency_audit.py`. Emits canonical verdict line `S85-W12-ELIM-6: PASS|FAIL|INFO -- value=<IMP,CON,IND,UND> scheme=plan-layer-prdr convention=four-valued-predicate L_max=n/a sha256=<64-hex>` via atomic append. Uses stdlib `ast` + regex for gate-block extraction. Data artifact: `computations/artifacts/s85_w12_elim6_pair_matrix.npz` (N_gates × N_gates predicate matrix). Plot: `computations/artifacts/s85_w12_elim6_heatmap.png` (symmetric predicate heatmap, color-coded by predicate value).

## §W12-3. S85-W12-ELIM-1  (Branch-(iv) re-audit at L_max ∈ {8, 10, 12})

**1. Gate ID**: `S85-W12-ELIM-1`
**2. Trigger**: `[VERIFY]`
**3. Classification**: GEOMETRIC (D_K spectral-structure probe at varying regulator L_max under inverted Josephson-dominance ansatz).
**4. Hypothesis**: The S84 retracted branch-(iv) (inverted Josephson-dominance: σ_J · |Δ|^2 > σ_K · |K|, the substrate-OP regime where Josephson coupling dominates the kinetic-regulator coupling) remains-retracted as L_max increases from 8 → 10 → 12. A PASS confirms the S84 retraction is L_max-robust: the branch fails at every regulator depth, so the retraction stands as a permanent wall. A FAIL would reopen the branch at higher L_max, signaling that the S84 retraction was a truncation artifact.
**5. Pass / Fail / INFO threshold**:
  - PASS: At each L_max ∈ {8, 10, 12}, the branch-(iv) residual D_iv = |σ_J · |Δ|^2 − σ_K · |K||/|σ_K · |K|| < 0.05 AND sign(σ_J · |Δ|^2 − σ_K · |K|) < 0 (Josephson does NOT dominate). All three L_max values must PASS independently (three-way AND).
  - FAIL: Any one L_max gives D_iv > 0.05 with sign(·) > 0 (Josephson dominates at some regulator depth — S84 retraction was artifact-driven).
  - INFO: Monotonic-trend detected (|D_iv(12)| < |D_iv(10)| < |D_iv(8)|) but none crossing the sign-change threshold — asymptotic convergence toward dominance, re-audit at L_max = 14 scheduled for S86.
  - Tolerance rule: RATIO 0.05 on D_iv; ABSOLUTE on sign comparison.
**6. Machinery pin (PRDR)**:
  - `L_max ∈ {8, 10, 12}` (three runs).
  - `N_eval = 155,984` at L_max = 10 (canonical); re-counted at 8 and 12 per the D_K spectral generator.
  - `D_K source = jensen_deformed_SU3_dirac(tau=tau_fold, L_max=L_max)` (canonical generator).
  - `Josephson coupling σ_J = spectral-moment-a_4` at fold (pinned from canonical_constants).
  - `Kinetic coupling σ_K = spectral-moment-a_2` at fold (pinned from canonical_constants).
  - `|Δ| = Delta_BCS`, `|K| = K_substrate = 2.035` (both canonical).
  - `scan_range`: L_max ∈ {8, 10, 12}.
  - `step_size`: integer step L_max += 2.
  - `tolerance`: 0.05 RATIO on residual, strict sign comparison.
  - `scheme = "inverted-josephson-dominance"`, `convention = "jensen-deformed-SU3-dirac"`.
  - `random_seed = 42` (for any stochastic eigenvector-initialization in torch.linalg; deterministic otherwise).
  - `GPU path`: REQUIRED. Use `phonon-exflation-sim/.venv312/Scripts/python.exe` with `torch.linalg.eigvalsh` on ROCm (RX 9070 XT). Matrices at L_max=12 are ~250k × 250k — CPU path infeasible (would run ~48h; GPU ~45min).
**7. Input SHA-256 pins**:
  - `computations/canonical_constants.py` — `<computed-at-runtime>`
  - `computations/artifacts/D_K_eigenvalues_Lmax8.npz` — `<computed-at-runtime>` (must exist or will be computed in-script; hash logged post-generation)
  - `computations/artifacts/D_K_eigenvalues_Lmax10.npz` — `<computed-at-runtime>`
  - `computations/artifacts/D_K_eigenvalues_Lmax12.npz` — `<computed-at-runtime>` (L_max=12 NEW — if cache absent, emit PRE-REG-INCOMPLETE)
  - `sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md` — `<computed-at-runtime>` (branch-(iv) retraction reference)
**8. Expected output 4-tuple**: `(value=<D_iv(8), D_iv(10), D_iv(12), sign_triple>, scheme=inverted-josephson-dominance, convention=jensen-deformed-SU3-dirac, L_max=mixed)`
**9. Substitution chain** (for "retraction-stands" direction):
  - Step 1 (definitions): σ_J = a_4 spectral moment = (1/Vol_SU3) ∫ Tr(D_K^(-4)) (canonical, Connes-Chamseddine spectral action). σ_K = a_2 spectral moment = (1/Vol_SU3) ∫ Tr(D_K^(-2)) (canonical). |Δ| = Delta_BCS (canonical from BdG). |K| = K_substrate = 2.035 (canonical from W6-A).
  - Step 2 (substitute into residual): D_iv = (σ_J · |Δ|^2 − σ_K · |K|) / (σ_K · |K|) = σ_J · |Δ|^2 / (σ_K · |K|) − 1.
  - Step 3 (simplify): For branch-(iv) to DOMINATE, we need σ_J · |Δ|^2 > σ_K · |K|, i.e., the ratio R_JK := σ_J · |Δ|^2 / (σ_K · |K|) > 1.
  - Step 4 (direction claim): At S84 L_max=10, R_JK = 0.87 < 1 (Josephson DOES NOT dominate; branch retracted). CLAIM: at L_max ∈ {8, 12}, R_JK remains < 1.
  - Step 5 (from canonical form — numerically-calibrated scaling): σ_J = Tr(D_K^{-4}) / Vol_SU3 and σ_K = Tr(D_K^{-2}) / Vol_SU3. Both are sums over the L_max-truncated eigenvalue spectrum of D_K on Jensen-deformed SU(3). **Plan-time Python verification** (multiplicity-weighted SU(3) Casimir schematic; see plan-authoring log): |spectrum(L_max)| grows polynomially with fitted exponent ≈ L_max^3.77 (not L_max^8, which was a dimensional over-count in an earlier draft — corrected at plan-time). Both raw moments Σ λ_i^{-2} and Σ λ_i^{-4} grow polynomially in L_max over the scanned range L_max ∈ {4…14} (neither is absolutely-convergent in the window of interest); Σ λ_i^{-2} grows faster than Σ λ_i^{-4}. Numerical ratio-behavior (schematic): σ_J / σ_K ≈ 0.206 at L_max=4, 0.089 at L_max=8, 0.049 at L_max=12 — monotone-decreasing across the scanned range. Direction-claim (PRE-REGISTERED, tested at compute-time): R_JK(L_max) = σ_J(L_max) · |Δ|^2 / (σ_K(L_max) · |K|) DECREASES with L_max for L_max ∈ {8, 10, 12}. If numerical run confirms monotone decrease AND R_JK < 1 at all three L_max, branch-(iv) retraction is L_max-robust → PASS. **The specific asymptotic scaling form is NOT a pre-registered criterion** — it is a diagnostic readout in the plot artifact. Only the two-clause direction (monotone-decreasing AND R_JK < 1 at all three L_max) is the PASS predicate.
  - Step 6 (direction on the residual): D_iv = R_JK − 1. Under the hypothesis R_JK < 1 at L_max=10 (S84 anchor) AND monotone-decreasing in L_max, D_iv < 0 at all three L_max values and |D_iv| grows with L_max (further from zero). PASS predicate (sign(D_iv) < 0 at each L_max AND |D_iv(12)| ≥ |D_iv(10)| ≥ |D_iv(8)| within the 0.05 RATIO tolerance on each residual) is consistent with the decreasing-ratio hypothesis. Monotonicity is enforced as an ORDER constraint on the three residuals — NOT as a scaling-form fit. The plan-time numerical survey was a SANITY CHECK of the direction, not a pre-registered prediction of the scaling exponent.
**10. PHONONIC classification rationale**: GEOMETRIC. This is a direct measurement on the D_K spectral moments at varying regulator. The gate IS the substrate at three probe depths: L_max = 8 (coarser partition of the fiber eigenvalue lattice), 10 (canonical anchor), 12 (refined partition). The L_max sweep tests whether the branch-(iv) wall of the allowed spectral-action region is an artifact of a specific regulator choice or a genuine structural feature of the spectral triple (A_F, H, D_K). A PASS pins the wall regardless of regulator; a FAIL re-opens the Josephson-dominance corner of substrate OP-space.
**11. What PASS means**: The S84 branch-(iv) retraction holds L_max-robustly across a meaningful regulator range. Inverted Josephson-dominance is PERMANENTLY closed as a substrate mechanism — not a truncation artifact. This strengthens the OP-direction elimination map by one regulator-independent wall and narrows the allowed Landau OP region on SU(3) from 5 surviving directions to a regulator-independent 5 (the wall was already there at L_max=10; the PASS makes it permanent).
**12. What FAIL means**: Branch-(iv) becomes dominant at higher L_max — the S84 retraction was a regulator-truncation artifact. The Josephson-dominance corner of OP-space re-opens; permanent-results-registry row for "branch-(iv) retracted" must be demoted to "branch-(iv) retracted-at-L_max=10-only", and a new gate must be pre-registered at L_max=14 to find the L_max-asymptotic verdict. This is a *gain*: the constraint map grows a new open direction (a previously-closed wall was premature).
**13. Producing script & verdict-line target**: `computations/s85_w12_branch_iv_reaudit_lmax.py`. Emits canonical verdict line `S85-W12-ELIM-1: PASS|FAIL|INFO -- value=<D_iv(8),D_iv(10),D_iv(12)> scheme=inverted-josephson-dominance convention=jensen-deformed-SU3-dirac L_max=mixed sha256=<64-hex>` via atomic append. Uses `torch.linalg.eigvalsh` on ROCm GPU path. Data artifacts: `computations/artifacts/s85_w12_elim1_D_K_Lmax{8,10,12}_moments.npz`, `computations/artifacts/s85_w12_elim1_residual_trajectory.npz`. Plot: `computations/artifacts/s85_w12_elim1_R_JK_vs_Lmax.png` (log-log plot of R_JK ratio vs L_max with L_max^(-2) asymptote overlaid).

## §W12-4. S85-W12-ELIM-8  (W0-regulator-invariance taxonomy)

**1. Gate ID**: `S85-W12-ELIM-8`
**2. Trigger**: `[VERIFY]`
**3. Classification**: GEOMETRIC (spectral-action regulator-invariance structural probe; companion to the ELIM-4 reduction catalog).
**4. Hypothesis**: The W0-regulator-invariance property — namely, that the zeroth-moment a_0 coefficient of the Connes-Chamseddine spectral action is invariant under a canonical 5-regulator atlas {heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars} — admits a rigorous 4-class taxonomy: (a) INVARIANT (same numerical value across all 5, within 0.1%), (b) CONDITIONALLY-INVARIANT (same under 4/5, one regulator outlier — potentially rescheme-able), (c) SCHEME-DEPENDENT (spread > 1% but < 10% — inherited from CF-W4.1 parent gate), (d) STRUCTURALLY-DIVERGENT (spread > 10% — regulator is not a scheme choice but a physical truncation). The hypothesis: every one of the 16 spectral-action observables in the permanent-results-registry admits a unique taxonomic class assignment.
**5. Pass / Fail / INFO threshold**:
  - PASS: All 16 observables assigned to exactly one of {a, b, c, d} by the tool, with no assignment-ambiguity (coverage = 16/16).
  - FAIL: ≥ 1 observable is *structurally unclassifiable* under the 4-class partition (requires a 5th class — the taxonomy is structurally incomplete).
  - INFO: 1 ≤ observables_in_class_(b) ≤ 3 (a handful of conditionally-invariants surfacing — schedule a mid-session regulator-remediation pass).
  - Tolerance rule: ABSOLUTE on coverage count; RATIO (0.1%, 1%, 10%) on regulator-spread class boundaries.
**6. Machinery pin (PRDR)**:
  - `regulator_atlas = ["heat-kernel", "zeta", "Mellin", "hard-cutoff", "Pauli-Villars"]` (fixed 5-element ordered list).
  - `observables = 16-entry permanent-results-registry spectral-action list` (pinned: a_0, a_2, a_4, m_H, m_t, alpha_s_MZ, w0_FW, n_s, τ_fold, dS_fold, d2S_fold, S_fold, Delta_BCS, K_substrate, K_R5, K_crit — the 16 registry rows).
  - `class_boundary_thresholds = (0.001, 0.01, 0.1)` (ABSOLUTE on regulator-spread as fraction of mean).
  - `scan_range`: all 5 × 16 = 80 (regulator, observable) evaluations.
  - `step_size`: N/A (categorical over regulators).
  - `tolerance`: 0.001 RATIO for class-(a) boundary, 0.01 for class-(b), 0.1 for class-(c).
  - `scheme = "regulator-invariance-taxonomy"`, `convention = "5-regulator-atlas-W0"`.
  - `random_seed = None` (deterministic spectral-moment evaluation).
  - `GPU path`: CPU 8-thread sufficient (80 evaluations, each ~10s; total ~15min). Use `phonon-exflation-sim/.venv312/Scripts/python.exe` with `os.environ['OMP_NUM_THREADS'] = '8'` before `import numpy`.
**7. Input SHA-256 pins**:
  - `computations/canonical_constants.py` — `<computed-at-runtime>` (all 16 observables anchored here)
  - `computations/_spectral_action_regulators.py` — `<computed-at-runtime>` (assumed existing helper from W0 regulator-invariance codebase; if absent, write as part of this gate)
  - `computations/artifacts/D_K_eigenvalues_Lmax10.npz` — `<computed-at-runtime>` (L_max=10 canonical)
  - `sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md` — `<computed-at-runtime>` (ELIM-4/ELIM-8 parent reference)
**8. Expected output 4-tuple**: `(value=<n_a, n_b, n_c, n_d>, scheme=regulator-invariance-taxonomy, convention=5-regulator-atlas-W0, L_max=10)`
**9. Substitution chain** (for taxonomy-completeness direction):
  - Step 1 (definitions): For observable O_k and regulator r ∈ R_atlas, let v_r(O_k) = value of O_k computed under regulator r. Define spread(O_k) = (max_r v_r(O_k) − min_r v_r(O_k)) / mean_r v_r(O_k) (definition, fractional range).
  - Step 2 (class assignment substitution): class(O_k) =
    - (a) if spread(O_k) < 0.001,
    - (b) if spread(O_k) ∈ [0.001, 0.01) AND 4/5 regulators cluster within 0.001 of each other,
    - (c) if spread(O_k) ∈ [0.001, 0.1) AND the class-(b) 4/5-cluster predicate FAILS,
    - (d) if spread(O_k) ≥ 0.1.
  - Step 3 (simplify: is the partition total?): The four conditions on spread({<0.001}, {0.001-0.01 with cluster}, {0.001-0.1 without cluster}, {≥0.1}) must exhaustively cover [0, ∞). Consistency check: the union of intervals is [0, 0.001) ∪ [0.001, 0.01) ∪ [0.001, 0.1) ∪ [0.1, ∞) — note the overlap at [0.001, 0.01). Resolved by the cluster predicate: if 4/5 cluster, class-(b); else class-(c). Therefore partition IS exhaustive-and-disjoint.
  - Step 4 (canonical form): class is a well-defined function class : R → {a, b, c, d}.
  - Step 5 (direction claim): PASS ⇔ ∀ O_k ∈ 16-registry : class(O_k) ∈ {a, b, c, d}. FAIL ⇔ ∃ O_k : the cluster predicate is undefined (e.g., bimodal spread with two 2-regulator clusters but no 4-regulator majority). Direction: the failure mode requires EXACTLY a bimodal-no-majority structure, which is the signature of a structurally-incomplete taxonomy. If FAIL, add a 5th class "POLYMODAL" in the next iteration.
**10. PHONONIC classification rationale**: GEOMETRIC. Each observable is a spectral moment (a_n Seeley-DeWitt coefficient or a threshold derived from one). The taxonomy is a statement about the spectral triple's *regulator-invariance structure* — i.e., which spectral moments are genuine invariants of the underlying geometry (A_F, H, D_K) and which depend on the regulator choice (hence the scheme-dependence residue). This directly maps the walls of allowed regulator-agnostic observables vs regulator-contingent ones. Every class-(a) membership is a wall that is unconditionally pinned; class-(d) membership flags an observable as structurally-ill-defined outside an explicit regulator declaration.
**11. What PASS means**: The 5-regulator atlas is a complete structural probe of the registry's 16 spectral-action observables. Every observable receives a well-defined regulator-invariance class. This closes the CF-W4.1 companion probe: the regulator-invariance question is decidable-and-decided across the registry. Class-(a) observables become permanent-results-registry unconditional walls; class-(d) observables require an EXPLICIT regulator pin in any future gate-verdict.
**12. What FAIL means**: At least one observable in the registry has a regulator-dependence structure that falls OUTSIDE the 4-class partition (e.g., a trimodal spread). The taxonomy must be extended with a 5th class. This is a *gain* for the constraint map: a previously-un-named regulator-dependence topology is now surfaced. The offending observable's registry entry must be flagged as "regulator-polymodal, taxonomy-extension-required" and the gate re-dispatched in S86 with the extended class set.
**13. Producing script & verdict-line target**: `computations/s85_w12_w0_regulator_taxonomy.py`. Emits canonical verdict line `S85-W12-ELIM-8: PASS|FAIL|INFO -- value=<n_a,n_b,n_c,n_d> scheme=regulator-invariance-taxonomy convention=5-regulator-atlas-W0 L_max=10 sha256=<64-hex>` via atomic append. Requires `_spectral_action_regulators.py` helper (write if absent, with all 5 regulator evaluators). Data artifact: `computations/artifacts/s85_w12_elim8_regulator_matrix.npz` (16 × 5 value matrix). Plot: `computations/artifacts/s85_w12_elim8_spread_histogram.png` (histogram of log10(spread) across 16 observables with class boundaries annotated).

## Wave W12 → Wave W13 Decision Point

W12 closure transitions the session to W13 (tesla-origin) under the following rules:

1. **Verdict-file integrity check**: After all 4 W12 gates complete, grep `computations/s85_gate_verdicts.txt` for `S85-W12-*` — expected exactly 4 canonical verdict lines with dual-SHA companion rows. If count ≠ 4, HALT and re-dispatch the missing gate(s).
2. **Working-paper section presence**: Each W12 gate writes to `sessions/archive/session-85/session-85-s3-gen-elimination-w12-working-paper.md` §W12-1 through §W12-4 (≥15 lines each, per `agent-standards.md`). Stub detection triggers a dedicated write-only re-dispatch.
3. **PRDR consistency audit self-test**: §W12-2's PASS is a *precondition* for dispatching W13 safely. If §W12-2 returns FAIL (contradiction surfaced), orchestrator MUST mediate BEFORE W13 dispatch — the contradicted pair may span W12↔W13 and dispatching blind re-compounds the defect.
4. **Branch-(iv) retraction status**: §W12-3's PASS pins the retraction L_max-robustly. W13 (tesla-origin) has one item whose prerequisite is that branch-(iv) is closed ("R_1 rank-distinguishability sharpening"). A §W12-3 FAIL demotes that W13 item to PRE-REG-INCOMPLETE until L_max=14 re-audit lands in S86.
5. **Catalog state**: §W12-1 PASS increments the canonical falsifier-catalog counter from 65 to 150 (permanent-results-registry update). This is a pre-dispatch update — W13 and subsequent waves read the extended catalog.

## Wave W12 Machinery-Enumeration Pin

| Gate | N_eval | L_max | Scan | Step | Tol | Scheme | Conv | Seed | GPU | Time |
|:-----|-------:|:------|:-----|:-----|:----|:-------|:-----|:-----|:----|:-----|
| S85-W12-ELIM-3 | 150 papers | n/a | class assignment over 12 classes | categorical | 0 ABS class, 0.01 RATIO coverage | catalog-extension | equivalence-class-disjoint | None | CPU 8-thread | 4h |
| S85-W12-ELIM-6 | 129² / 2 pairs | n/a | plan-file AST over 14 wave plans | pairwise | 0 ABS undeclared, 0 ABS contradicts | plan-layer-prdr | four-valued-predicate | None | CPU 1-thread | 5h |
| S85-W12-ELIM-1 | 3 × 155,984 eigenvalues (scales at L_max=8,12) | {8, 10, 12} | L_max step +2 | 2 | 0.05 RATIO residual, strict sign | inverted-josephson-dominance | jensen-deformed-SU3-dirac | 42 | ROCm GPU REQUIRED | 6h |
| S85-W12-ELIM-8 | 5 × 16 = 80 | 10 | regulator × observable | categorical | (0.001, 0.01, 0.1) class boundaries | regulator-invariance-taxonomy | 5-regulator-atlas-W0 | None | CPU 8-thread | 4h |

**PRU (Pre-Registration Underspecification) statement**: Each of the 10 machinery fields (N_eval, L_max, scan, step, tolerance, scheme, convention, seed, GPU, expected-output) is pinned above for all 4 gates. No free parameter remains at dispatch time. Wave W12 is PRU-Class-8-compliant.

**PROHIBITED_ACTIONS pin** (inherited from v3-closure-recovery.md): No convention-shopping on {inverted-josephson-dominance, regulator-invariance-taxonomy}; no iterate-until-PASS on §W12-1 class count or §W12-3 L_max sweep; no post-hoc threshold edits on (0.05, 0.001, 0.01, 0.1); no ansatz-forced PASS via manual verdict-file edit.

## Wave W12 Input-SHA Ledger

The following files are the union of inputs pinned across §W12-1 through §W12-4. Computed at runtime (dynamic inputs) unless marked STATIC:

| Path | Status | Used by |
|:-----|:-------|:--------|
| `computations/canonical_constants.py` | STATIC (pinned in all 4 scripts) | all 4 |
| `researchers/index.md` | STATIC | §W12-1 |
| `researchers/Baptista/index.md` | STATIC | §W12-1 |
| `researchers/Volovik/index.md` | STATIC | §W12-1 |
| `researchers/Kaluza-Klein/index.md` | STATIC | §W12-1 |
| `researchers/Antimatter/index.md` | STATIC | §W12-1 |
| `researchers/Little-Red-Dots/index.md` | STATIC | §W12-1 |
| `researchers/Einstein/index.md` | STATIC | §W12-1 |
| `sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md` | STATIC | §W12-1, §W12-3, §W12-4 |
| `sessions/session-plan/session-85-partition.md` | STATIC | §W12-2 |
| `sessions/session-plan/session-85-plan-w0.md` | DYNAMIC (exists post-W0 dispatch) | §W12-2 |
| `sessions/session-plan/session-85-plan-w{1a,1b,2,3,4,5,6,7,8,9,10,11,13}.md` | DYNAMIC (13 files; exist post-their-respective-dispatch) | §W12-2 |
| `computations/artifacts/D_K_eigenvalues_Lmax8.npz` | DYNAMIC (cache; computed if absent) | §W12-3 |
| `computations/artifacts/D_K_eigenvalues_Lmax10.npz` | DYNAMIC (canonical cache) | §W12-3, §W12-4 |
| `computations/artifacts/D_K_eigenvalues_Lmax12.npz` | DYNAMIC (NEW; computed if absent; if compute-infeasible, §W12-3 emits PRE-REG-INCOMPLETE) | §W12-3 |
| `computations/_spectral_action_regulators.py` | DYNAMIC (helper; write-if-absent during §W12-4) | §W12-4 |

Closure-hash rule: each script computes sha256 of the ordered input-pin map (path, sha256) pairs at runtime, emits it as the `sha256=<64-hex>` field of its canonical verdict line. Hash is NEVER hardcoded, NEVER copy-pasted, NEVER truncated below 64 hex chars. Dual-SHA gates (§W12-3 due to L_max cache dependencies) emit the companion comment row with `content_sha256=<64-hex> audit_sha256=<64-hex>`.

---

**Wave W12 plan complete.** 4 gates pre-registered with full 13-field blocks. Plan is PRU-compliant (all machinery pinned) and PROHIBITED_ACTIONS-compliant (no post-hoc threshold shopping, no iterate-until-PASS). Dispatch-ready once W0-W11 wave-plan files exist on disk (prerequisite for §W12-2).
