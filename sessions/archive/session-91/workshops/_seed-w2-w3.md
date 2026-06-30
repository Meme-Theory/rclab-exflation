# Seed file — Chunk C2 (w2 + w3)

**Date**: 2026-05-21
**Investigator**: phonon-first-cosmologist
**Source**: sessions/archive/session-91/session-91-w2-workingpaper.md (1366 lines) + sessions/archive/session-91/session-91-w3-workingpaper.md (1388 lines)
**Plan files**: sessions/session-plan/session-91-plan-w2.md, sessions/session-plan/session-91-plan-w3.md
**Wave summary**:
- **w2 (3 gates)**: §W2-1 PASS (Reading V regulator-class-pluralism at substrate-distance-2 χ' restriction) + §W2-2 FAIL (regime=BREAKDOWN; numerical first-extraction at substrate-distance-1 pole s=3 not L_max-saturated at L_max=12) + §W2-3 PASS (Reading A WIN on Spearman rank-ordering for §VII.AU.OP-PROJ at substrate-distance-1; N_above_3=4/5). Cross-gate synthesis: substrate-distance-1 corridor CONFIRMED at the anchor-rank layer (§W2-3) but numerical first-extraction DEFERRED at L_max-saturation (§W2-2). Substrate-distance-2 χ' restriction PASSes Reading V multi-pin atlas (§W2-1).
- **w3 (4 gates)**: T1.6 INFO (composite via MARGINAL regime collapse; literal magnitude-FAIL at T=1 GeV rel_dev=23.65% well above 10% gate-band ceiling) + T1.7 FAIL mechanical PRE-REG-INC (upstream-block; T1.6 magnitude-FAIL fires the conditional-dispatch FAIL branch) + T1.8 FAIL (substrate-distance-1 (c)∘(d) AUX-4 corridor; γ_weight_aux=0.404 substrate-derived; rel_dev=0.82) + T1.9 FAIL (substrate-distance-1 (d)∘(b) FULL CM-1995 corridor; χ'_weight_FULL=5/14 Hilbert-space-DIM; rel_dev=0.84). Cross-gate synthesis: Track A species-multiplicity cascade closes at phase-weight-model failure (NOT kernel-machinery); Track B substrate-distance-1 LRD α-anchor pursuit PERMANENTLY closes at BOTH compositional corridors; LRD α-anchor pursuit moves to substrate-distance-2 §VII.AX forward gates at S92+.

## Slot 1 candidates — solo reviews (`/rclab-review`; 1+ agents per entry, default 1)

### S1-1 — w3 LRD α-anchor structural closure: substrate-derivation taxonomy review across CF-37, T1.8, T1.9

**What this review answers**: Three substrate-derivations of the inheritance-restricted-projector weight on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` produced three distinct canonical numerical values that ALL FAIL the empirical 1/458 anchor at substrate-distance-1 pole s=3:
- CF-37 (S90): Wedderburn-RANK ratio = 3/6 = 0.500 → α'_CF37=4.80e-4 → rel_dev=0.78
- T1.8 (S91): Wedderburn + digamma-modulated γ-kernel = 0.404 → α''=3.87e-4 → rel_dev=0.82
- T1.9 (S91): Hilbert-space-DIMENSION fraction = 5/14 ≈ 0.357 → α'_FULL=3.43e-4 → rel_dev=0.84

The three derivations span structural factor 5/7 (T1.9 vs CF-37 in 0.714 ratio) and are not numerical refinements of one another — they invoke DISTINCT substrate-IS machinery. The WP team-lead synthesis frames them as convergent FAILs on the structural-orthogonality K-counter axis, BUT it does NOT adjudicate which substrate-derivation IS the canonical inheritance-restricted projector weight on `A_K`. The substrate must have one canonical answer (or a structural theorem on simultaneous validity). This review produces a substrate-derivation taxonomy with adjudication criteria for which is canonical — useful as preparation for the workshop S2-1 below.

**Why solo (not workshop)**: This is the substrate-derivation **inventory** step — single-agent compilation of the three derivations side-by-side with their substrate-physics provenance citations (Wedderburn vs HS-dim vs digamma-modulated-Wedderburn). The adversarial adjudication of which is canonical is the workshop S2-1 task; the inventory is the prerequisite. Independent reading by one agent (volovik or van-den-dungen) suffices to assemble the taxonomy.

**Agents**: van-den-dungen-bridge-theorist (default 1; NCG-axiomatic side; OAA admissible since connes-ncg + phonon-first are HARD-excluded from CF-37 lineage)

**Source docs**:
- sessions/archive/session-91/session-91-w3-workingpaper.md §W3-3 (T1.8 γ_weight_aux derivations lines 651-678) + §W3-4 (T1.9 χ'_weight_FULL=5/14 derivation lines 944-998)
- sessions/archive/session-90/session-90-w4-workingpaper.md §"Carry-Forward Computations" CF-37 origin lines 715-722, 724-731
- computations/session-91/s91_w2_3_vii_au_op_proj_w7a74_first_extraction.npz (5×5 Spearman matrix; substrate-IS rank-ordering on the same OP-PROJ image)
- sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ W-5 baseline calibration corpus instance #1
- computations/_shared/_cm_1995_residue_formula.py (FULL physical evaluator docstring lines 50-63)

**Output**: Single-agent synthesis report `sessions/archive/session-91/workshops/s91-substrate-derivation-taxonomy-chi-prime-weight.md` enumerating the three derivations + machinery citations + substrate-physics provenance arguments; classifies each derivation by the algebra-axis (rank vs dim vs digamma-residue) and identifies which axis is structurally pinned by which substrate identity (Wedderburn decomposition theorem / KO-dim 6 spectral triple / CM-1995 §III.4 residue formula). Provides the substrate-derivation inventory for downstream S2-1 workshop adjudication.

### S1-2 — w2 numerical-vs-rank-axis epistemological complementarity review for §VII.AU.OP-PROJ at substrate-distance-1

**What this review answers**: §W2-2 (numerical FAIL at L_max=12 via 85.7% drift BREAKDOWN) and §W2-3 (Spearman rank-ordering PASS Reading A at 4/5 anchors with max|Δρ_S|=0.0000 across L_max=10 vs 12) give APPARENTLY contradictory verdicts on the same §VII.AU.OP-PROJ first-extraction at substrate-distance-1 pole s=3. The WP team-lead synthesis §C item (2) lines 1238-1245 self-reads this as "structurally complementary" via the cardinality-vector saturation theorem (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`). This solo review independently audits that self-reading: is the rank-vector saturation theorem genuinely structural (rank-vector saturation precedes numerical-magnitude saturation in L_max headroom by factor 1.5-2× at pole-weight |λ|^{-6}), or is the "structurally complementary" framing a team-lead post-hoc reconciliation that papers over a genuine epistemic divergence? If the former, document the theorem as a permanent structural lemma; if the latter, surface it as a workshop candidate for S92.

**Why solo (not workshop)**: This is methodology audit of the W2 wave-synthesis self-reading, NOT adversarial substrate-physics. Independent reading by lizzi-spectral-functional-theorist (Spearman rank-axis canonical author per §W2-3) suffices — lizzi can audit the team-lead synthesis without volovik counter-argument; the question is structural-correctness of the cardinality-vector saturation theorem application, not a tension between two substrate-physics readings.

**Agents**: lizzi-spectral-functional-theorist (default 1; sole author of §W2-3 Spearman rank-axis canonical)

**Source docs**:
- sessions/archive/session-91/session-91-w2-workingpaper.md §"Wave 2 — Cross-gate decision points" lines 1168-1180 + §C item (2) lines 1238-1245
- sessions/archive/session-91/session-91-w2-workingpaper.md §W2-2 results table lines 670-706 (85.7% L_max=10→12 drift)
- sessions/archive/session-91/session-91-w2-workingpaper.md §W2-3 results table lines 1014-1099 (max|Δρ_S|=0.0000)
- math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check" (W11-2 + W11-3 saturation theorem precedents)
- Friedrich-Bär saturation theorem application to pole-weight |λ|^{-2s} scaling

**Output**: Single-agent audit report `sessions/archive/session-91/workshops/s91-rank-vs-magnitude-axis-complementarity-audit.md` either (a) confirming the cardinality-vector saturation theorem applies structurally with explicit Friedrich-Bär lower-bound derivation for pole s=3 and recommending the W2 self-reading as canonical; OR (b) identifying a structural gap in the team-lead synthesis and queueing it as an S92 workshop candidate. Either outcome is a structural verdict on the methodology rule's reach.

## Slot 2 candidates — workshops (`/rclab-workshop`; EXACTLY 2 agents, 2 rounds default)

### S2-1 — χ'_weight canonical substrate-derivation on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`: Wedderburn-RANK vs Hilbert-space-DIM vs digamma-modulated-residue

**Tension**: Three structurally distinct substrate-derivations of the inheritance-restricted-projector weight on the same `A_K` algebra produced three numerical values for the same observable (LRD α-anchor at M=10⁷ M_sun, L_max=10):

- **CF-37 (S90 W4 phonon-first-cosmologist; structural-ansatz layer)**: `χ'_weight = 3/6 = 0.5` derived from Wedderburn-RANK ratio (rank of `M_2(ℂ) ⊗ Cl(1)` target / total rank of A_K). Gate-ID: `S90-CF37-LRD-ALPHA-ANCHOR` at audit_sha256=`10ee072fe2c193f3...` (`session-90-w4-workingpaper.md §W4-1`).
- **T1.9 (S91 W3 van-den-dungen-bridge-theorist; FULL CM-1995 layer)**: `χ'_weight_FULL = 5/14 = 0.357143` derived from Hilbert-space-DIMENSION fraction (dim_HS(ℂ)+dim_HS(ℍ))/dim_HS(A_K) = (1+4)/(1+4+9). Gate-ID: `S91-CF37-FULL-CM1995-RESIDUE` at audit_sha256=`752a8f2b862a9aa5...` (`session-91-w3-workingpaper.md §W3-4`).
- **T1.8 (S91 W3 volovik-superfluid-universe-theorist; modified-universal-kernel γ(s) layer)**: `γ_weight_aux^(3) = χ'_weight · (1 + c_aux · ψ(s_*=1)) = 0.5 · (1 − γ_Euler/3) ≈ 0.404` derived from CM-1995 residue at the simple pole of γ(s) = Γ(s)·(1 + (1/3)·(s−1)^{-1}). Gate-ID: `S91-CF37-AUX-4-SECONDARY-CORRIDOR` at audit_sha256=`8ab158e9e45aab37...` (`session-91-w3-workingpaper.md §W3-3`).

The three weights differ by structural factor 5/7 (T1.9 vs CF-37) and digamma-modulation (T1.8 vs CF-37). ALL three FAIL the empirical 1/458 anchor (rel_dev 0.78, 0.84, 0.82 respectively); ALL three PASS Sub-clause A sign-positivity. The substrate-physics question this workshop must adjudicate: **which substrate-derivation IS the canonical inheritance-restricted-projector weight on `A_K`?** Or — if multiple are simultaneously valid — what structural theorem on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` admits THREE structurally distinct substrate-IS weights for the same observable?

The wave-synthesis §"Track B consequence map" lines 1290-1299 of the W3 WP frames these three as convergent FAILs that close substrate-distance-1 at the algebra-axis-orthogonality K-counter axis — but does NOT adjudicate which IS canonical. The substrate cannot host three simultaneous canonical answers without a structural theorem of simultaneous validity; otherwise one (or none) is canonical and the others are non-canonical lab-side images.

**Why workshop (not solo)**: Cross-rebuttal is essential. Volovik's substrate-Wedderburn-natural argument (rank is the substrate's intrinsic algebraic invariant; HS-dim is a representation-dependent quantity) versus van-den-dungen's NCG-axiomatic argument (CM-1995 §III.4 residue formula evaluates the Chern character via HS-dim trace; the FULL physical evaluation IS the canonical substrate-derivation) genuinely diverge at first principles. Both arguments invoke substrate-IS structural identities. The third reading (T1.8 digamma-modulated) introduces a γ(s) ≠ Γ(s) cohomology-class shift that further complicates the canonical choice. A single-agent solo review cannot adjudicate which substrate-derivation IS canonical; cross-axis adversarial round structure is needed because each agent brings a DIFFERENT canonical machinery argument.

**Agents (EXACTLY 2)**: `volovik-superfluid-universe-theorist`, `van-den-dungen-bridge-theorist`

OAA compliance: Both agents are non-connes-ncg + non-phonon-first per the S91 W3 OAA exclusion (downstream-inheritance reach extension per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` clause 2). Volovik authored T1.8; van-den-dungen authored T1.9 (Axis-A) and T1.8 (Axis-B); both are OAA-admissible as workshop participants for THIS adjudication. The workshop's structural question is precisely the substrate-derivation choice their respective gates instantiated — they hold the load-bearing structural arguments.

**Adjudication question**:
- (a) Is `χ'_weight` on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` canonically the Wedderburn-RANK ratio (volovik substrate-natural reading; counts the substrate's primitive idempotents) OR the Hilbert-space-DIMENSION fraction (van-den-dungen NCG-axiomatic reading; appears in the CM-1995 §III.4 residue trace)? Which substrate identity is binding at the inheritance-morphism layer?
- (b) Does the γ(s) ≠ Γ(s) modified-universal-kernel cohomology-class shift produce a STRUCTURALLY DISTINCT canonical weight (T1.8 reading), or is it a substrate-natural refinement of one of the above (e.g., the digamma factor is the L_max → ∞ asymptotic correction to one of the bare weights)?
- (c) Is the χ' inheritance morphism's image faithful (S89 §W2-3 derived theorem ker rank 9 on M_3(ℂ) forces zero map; the image is `ℂ ⊕ ℍ` only) — and does that faithfulness pin the canonical weight to one of the three (or to a fourth: e.g., the K-theoretic dim ratio)?
- (d) Does the algebra-axis orthogonality K=3 MANDATORY discipline at `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` constrain the choice — i.e., is there a Cell-I × pole-s=3 structural theorem that forces a unique substrate-derivation, or are all three derivations within Cell-I and the K-counter does not discriminate?

**Rounds**: 2 (default; bump to 3 if R1+R2 produces convergence without genuine ledger-dissonance OR if R1+R2 produces TWO competing positions both with first-principles support; the latter would indicate genuine 3-round adjudication required)

**Output**: Pre-registered structural verdict producing ONE of three outcomes:
- (i) **Canonical-weight verdict**: one substrate-derivation is canonical; the other two are non-canonical lab-side images; CF-37 retroactive reading is updated and an `S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT` registry slot lands in `permanent-results-registry.md` as STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway.
- (ii) **Simultaneous-validity theorem**: all three substrate-derivations are simultaneously valid via a structural theorem on `A_K`'s 3-summand Wedderburn decomposition (e.g., the three weights correspond to three structurally distinct functionals on `A_K` that are NOT equivalent at the algebra layer; downstream gates must explicitly tag which functional is consumed); registry-text correction at §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ.
- (iii) **Open registry slot**: workshop converges on the structural question being genuinely open at S91; new §VII slot opened with `STAGE-1-CANDIDATE-OPEN-CHI-PRIME-WEIGHT-CANONICALIZATION` sub-class tag; carry-forward to S92 with explicit substrate-physics pre-registration (which test would discriminate).

## Carry-forwards (route to investigated wave's WP CF section, NOT this workshop schedule)

- **[Q2-hygiene] T1.6 schema-v2 INFO vs literal magnitude-FAIL gate-band-predicate dual-reading clarification (target wave: w3)**:
  - **What**: Document the boundary between the schema-v2 composite-collapse rule at `gate-verdicts.md §"S87+ canonical form Schema-v2"` (which collapses magnitude-FAIL ∧ regime-MARGINAL → composite=INFO) and the literal gate-band predicate per plan §6 PASS/FAIL/INFO bands (which routes rel_dev > 0.10 as FAIL at ANY anchor). T1.6 closed composite=INFO but T1.7's CONDITIONAL DISPATCH RULE reads the literal gate-band FAIL at T=1 GeV (rel_dev=23.65% > 0.10) as the FAIL trigger for mechanical PRE-REG-INC closure. Both readings are pre-registered; both fire on the same numerical output. This is a calibration corpus instance for the composite-collapse boundary — clarify which axis governs CANONICAL-PROMOTION conditional dispatches when the two readings give opposite verdicts.
  - **Inputs**: `computations/session-91/s91_gate_verdicts.txt` lines 33-35 (T1.6 canonical + dual-SHA + 3-tuple); `sessions/archive/session-91/session-91-w3-workingpaper.md §W3-1 "Reading the verdict for T1.7 conditional-dispatch routing"` lines 189-194 (explicit acknowledgment of the dual-reading); `gate-verdicts.md §"S87+ canonical form (Schema-v2)"` composite-collapse rule.
  - **Gate**: Calibration corpus addition to `gate-verdicts.md §"Composite-collapse rule"` documenting T1.6 as the calibration instance for the schema-v2-vs-literal-gate-band dual-reading; rule extension specifying which reading is canonical for canonical-promotion conditional dispatches (likely the literal gate-band predicate governs canonical-promotion gates per the T1.7 routing decision; the schema-v2 INFO collapse is a sub-result-preserving annotation).
  - **Effort**: ~0.2 we.

- **[Q2-hygiene-already-in-WP] Pointer: T1.9 sig_5 duplicate audit_sha256 self-supersedes degeneracy (target wave: w3)**:
  - Already queued as `CF-S92-T1.9-SIG-5-DUPLICATE-SHA-AUDIT-REMEDIATION` in W3 WP lines 1141-1148 + 1359-1364. Surface as pointer: the duplicate `audit_sha256 = 752a8f2b...` at verdict-file lines 42 + 45 with self-referential `supersedes=752a8f2b...` token is a sig_5 SHA-uniqueness violation per `v3-closure-recovery.md §"Stage 1"`. The consolidator should preserve this CF entry in the W3 WP — no new CF needed.

- **[Q2-hygiene-already-in-WP] Pointer: T1.6 lizzi-prediction-refutation diagnostic (target wave: w3)**:
  - Already queued as `CF-S92-LIZZI-S4-META-P3-PREDICTION-FAILURE-DIAGNOSTIC` in W3 WP lines 240 + 1366-1371. Lizzi-s4-meta-p3-synthesis §1.3 line 122 predicted T=1 GeV in 5-10% INFO band; empirical 23.65% FAIL. The unaccounted-for kernel-vs-phase-weight interaction term is the diagnostic. Consolidator preserves CF entry; no new CF needed.

- **[Q3-wave-together] §VII.AU.OP-PROJ substrate-distance-1 L_max=14+ extension parallel-wave-together (target wave: w2)**:
  - Already queued as the THREE coupled CFs in W2 WP lines 769-771 + 1299-1301: `CF-S92-W2-2-LMAX14` (volovik PRIMARY + landau CONFIRMER; 1.5 we), `CF-S92-W2-2-SLOPE-A-CANON` (mack-cosmic-bridge; 0.3 we), `CF-S92-W2-2-W2-3-JOINT` (mack + Stage-2 lizzi+connes; 0.5 we). These three CFs are STRUCTURALLY a parallel-compute-wave: each is on its own substrate-physics / canonical-pin / Stage-2 cross-axis pre-registered PASS criterion AND the three verdicts combine via logical AND for the §VII.AU.OP-PROJ STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED Stage-1 landing. The W2 WP already enumerates them as ACTIVATED CFs; consolidator should mark them as "wave-together" at S92 plan-freeze per `Investigating-Workshops.md §Q3` discriminator.

- **[Q3-wave-together] §VII.AX substrate-distance-2 multi-pin atlas landing parallel-wave (target wave: w2)**:
  - Already queued in W2 WP lines 1297-1298 + W3 WP line 1382: `CF-W2-1-S91-W2-PASS-V` (mack-cosmic-bridge §VII.AX NEW slot landing; 0.3 we) + `CF-W2-2-S91-W2-K-COUNTER-ADVANCEMENT` (gen-physicist + connes-ncg co-author; 0.2 we) + (eventually) §VII.AX-SUBSTRATE-DISTANCE-2-FORWARD-GATES from S91 W0 R5 LANDED (3.5 we). These are 3 coupled gates on distinct axes (registry-landing / K-counter / forward-substrate-physics-evaluation) combining via logical AND for the substrate-distance-2 LRD α-anchor candidate verdict at S92+. Mark as "wave-together" at S92 plan-freeze.

- **[Q-other] CF-S92-PHASE-WEIGHT-QCD-CROSSOVER-REFINEMENT chain (target wave: w3)**:
  - Already queued as 3-coupled CFs in W3 WP lines 1338-1357: `CF-S92-PHASE-WEIGHT-QCD-CROSSOVER-REFINEMENT` (Borsanyi-2016 lattice-QCD anchor; 1.0 we) → `CF-S92-T1.6-RETRY-PHASE-WEIGHT-REFINED` (CONDITIONAL on prior PASS; 0.5 we) → `CF-S92-T1.7-CF39-SUBSTANTIVE-RETRY` (CONDITIONAL on T1.6 retry PASS; 0.5 we). This is a STRUCTURALLY SEQUENTIAL chain (NOT wave-together); each CF depends on the prior one's PASS. Already structured correctly in W3 WP; consolidator preserves the sequential dependency.

- **[Q-other] CF-S92-GAMMA-S-SUBSTRATE-DERIVATION-REFINEMENT-ALTERNATIVE-C-AUX (target wave: w3)**:
  - Already queued in W3 WP lines 1373-1378. Investigates alternative `c_aux` values beyond the Wedderburn (1−2+3)/6 = 1/3 default (e.g., gauge anomaly polynomial coefficient; SU(3) Casimir invariant ratios; χ_BdG-based rank ratio). This is the T1.8 substrate-derivation refinement axis. If the workshop S2-1 above resolves canonical-weight verdict, this CF may become redundant or refined; otherwise it stays in the queue.

## Wave-by-wave digest (consolidator background)

### w2 digest

W2 closed 3 gates: §W2-1 (T0.7 CHI-PRIME-WEIGHT-CANONICALIZED) PASS-V, §W2-2 (T1.5 OP-PROJ-FIRST-EXTRACTION-PARAMETERIZATION) FAIL-BREAKDOWN, §W2-3 (T1.10 OP-PROJ-FIRST-EXTRACTION-W7A74) PASS Reading A. The cross-gate joint verdict: substrate-distance-2 χ' restriction PASSes Reading V regulator-class-pluralism (multi-pin atlas at §VII.AX); substrate-distance-1 OP-PROJ first-extraction has corridor CONFIRMED (Spearman rank-axis) but numerical first-extraction DEFERRED (L_max=12 truncation 85.7% drift exceeds BREAKDOWN threshold).

The most structurally interesting feature: the rank-vs-magnitude axis split at substrate-distance-1 pole s=3. §W2-3 PASSes with max|Δρ_S|=0.0000 across L_max=10 vs 12 (rank-vector saturation BY L_max=10), while §W2-2 fails with 85.7% drift across the same L_max range (numerical-magnitude UN-saturated at L_max=12). The W2 wave-synthesis self-reads this as structurally complementary via the cardinality-vector saturation theorem (`math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`). The Slot 1 S1-2 review independently audits whether this self-reading is structurally sound or a post-hoc reconciliation. The substrate-distance-2 PASS-V at §W2-1 is a Reading V multi-pin atlas canonical (axis β multi-scheme convention per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding"`); CF-W2-1 queues the §VII.AX landing at S92 W1.

Wave-class: COMPUTE-class (all 3 gates have numerical PASS thresholds + `.py`/`.npz`/`.png` outputs). PRDR Class-8 cardinality: 50 free parameters pinned, 0 unpinned. Source-RECONCILIATION: PASS with runtime fallback (`slope_A_canonical` resolved via plan-text-drift correction). All 4-axis pin compliance (LEVEL × MACHINERY-SCOPE × Binding × bridge-map-scheme) declared.

### w3 digest

W3 closed 4 gates organized as two structurally INDEPENDENT tracks. Track A (species-multiplicity cascade): T1.6 INFO (composite-collapse via MARGINAL regime; literal magnitude-FAIL at T=1 GeV rel_dev=23.65%) + T1.7 FAIL mechanical PRE-REG-INC (upstream-block topology fires on T1.6 magnitude-FAIL). Track B (LRD α-anchor parallel pathways): T1.8 FAIL (substrate-distance-1 (c)∘(d) AUX-4 corridor with γ(s) ≠ Γ(s) modified-universal-kernel; γ_weight_aux=0.404; rel_dev=0.82) + T1.9 FAIL (substrate-distance-1 (d)∘(b) FULL CM-1995 corridor; χ'_weight_FULL=5/14=0.357 Hilbert-space-DIM; rel_dev=0.84).

Track A structural finding: canonical Kolb-Turner Eq.3.62 FD/BE integrated form is structurally correct at well-separated regimes (T=100 GeV: 4.5× tightening; T=1 MeV: 20× tightening) but FAILs at QCD-crossover band T=1 GeV. The failure axis is the smooth-tanh `qcd_crossover_weight(T)` phase-weight model saturating prematurely to w=1; lattice-QCD Borsanyi 2016 shows residual confinement suppression past T=1 GeV. The S90 simplified `exp(-m/T)` accidentally cancelled the phase-weight error; canonical Kolb-Turner reveals it. The lizzi-s4-meta-p3-synthesis §1.3 line 122 prior prediction (5-10% INFO band) was empirically refuted at 23.65% FAIL.

Track B structural finding: BOTH substrate-distance-1 LRD α-anchor pursuits CLOSE PERMANENTLY at the FULL substrate-derivation layer. Three distinct substrate-derivations of χ'_weight on `A_K` (CF-37 Wedderburn-RANK 3/6, T1.9 Hilbert-space-DIM 5/14, T1.8 Wedderburn+digamma 0.404) ALL fall structurally below the required γ_weight_aux ∈ [1.593, 2.958] band for empirical 1/458 PASS at substrate-distance-1. The dimensional bridge factor `(M_KK/M_Pl_reduced)² = 9.307e-4` is the structural bottleneck. LRD α-anchor pursuit moves to substrate-distance-2 §VII.AX forward gates pre-registered at S91 W0 R5 LANDED (queued for S92+).

Notable methodology features: (a) T1.9 emitted THREE canonical verdict lines (lines 39 + 42 + 45 of `s91_gate_verdicts.txt`) with Option-A supersession chain — Line 39 superseded by Line 42 (script-bug fix on `chi_prime_morphism_matrix` semantics); Line 42 + Line 45 byte-identical (no-op re-emission with degenerate self-supersedes tag). Sig_5 SHA-uniqueness violation at Lines 42+45 queued for S92+ low-effort remediation (CF-S92-T1.9-SIG-5-DUPLICATE-SHA-AUDIT-REMEDIATION). (b) T1.6 composite=INFO via schema-v2 MARGINAL collapse but literal gate-band predicate rel_dev_1GeV=23.65% > 10% is FAIL — T1.7's CONDITIONAL DISPATCH RULE reads the literal gate-band FAIL, triggering mechanical PRE-REG-INC. The schema-v2-vs-literal-gate-band dual-reading is a methodology calibration corpus instance (queued as Q2-hygiene carry-forward above).

Wave-class: MIXED (per plan §6); all 4 gates are substantive computation EXCEPT T1.7's FAIL branch which is mechanical-closure PRE-REG-INC per `mechanical-closure-discipline.md` 5-clause admissibility (ALL 5 CLAUSES PASS). OAA HARD-exclusion of connes-ncg + phonon-first applies to Track B (T1.8 + T1.9); volovik PRIMARY + van-den-dungen Axis-B on T1.8; van-den-dungen PRIMARY + mack-cosmic-bridge Axis-B on T1.9. Three independent cross-review confirmations (gen-physicist on T1.6 numerical machinery; vdd on T1.8 substrate-derivation; mack on T1.9 bridge-map verification) all PASS-AND the substrate-physics structural correctness of the FAIL diagnoses — the FAILs are HONEST closures at substrate-distance-1, not implementation defects.

K-counter status after W3: Hybrid Independence Test K=1 PRESERVED (W-5 §VII.AF.1.OP-PROJ baseline; T1.8 + T1.9 both FAIL → instance #2 NOT advanced); Cross-axis JOINT-WIN K=6 PRESERVED; Substrate-input-orthogonality K=3 MANDATORY PRESERVED; Algebra-axis orthogonality K=4 PRESERVED; Deferred-pending K=2 SUGGESTION PRESERVED. No K-counter advancement; no new §VII registry STAGE-1-CANDIDATE landing at W3.
