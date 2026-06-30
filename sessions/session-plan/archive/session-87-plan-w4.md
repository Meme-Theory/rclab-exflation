# Session 87 Plan — Wave 4: Cross-Pillar + Type-F + f_NL Surgery

**Wave owner**: `connes-ncg-theorist` (lead, per S86 W-4 attribution `connes+lizzi` → connes lead per `feedback_agent-roster.md` + context §4 wave-owner mapping)
**Wave co-author**: `lizzi-spectral-functional-theorist` (Mellin-anchor / spectral-functional side of CF-25 + CF-29)
**Mechanical writer for inventory surgery (CF-27 + CF-28)**: `mack-cosmic-bridge` (sole `falsifier-master-inventory.md` writer per `feedback_mack-bridge-role.md`)
**Doc-only rule-promotion dispatcher (CF-30)**: `gen-physicist`
**Verdict file**: `computations/s87_gate_verdicts.txt` (per `.claude/rules/gate-verdicts.md` Canonical Verdict-File Path)
**Working paper target**: `sessions/archive/session-87/session-87-w4-workingpaper.md` (fanout mode)
**Total wave items**: 6 (CF-25, CF-26, CF-27, CF-28, CF-29, CF-30)
**Effort estimate (wave-equivalents)**: ~3.4 sessions ≈ 3.4 wave-equivalents (1 + 1/3 + 1/4 + 1/8 + 1 + 1/4 = 2.96; with adjudication overhead ≈ 3.4)

---

## Wave 4 Summary

Wave 4 closes the S86 W-4 connes+lizzi joint gate cluster — six items spanning Level 1 (cross-pillar 3-channel theorem proof, HIGH-EVOI) through Level 5 (operator-projection separation rule promotion, doc-only). The wave's substrate-first object is the **3-channel decomposition of substrate observables**: 3-pt-connected vertex (irreducible) / pair-cumulant (semi-reducible) / 2-pt-separable (reducible). CF-25 lifts this decomposition to a cross-pillar bridge theorem; CF-26 audits the per-mode Bogoliubov-phase distribution {phi_a}_{a=1..32} that the Type-F partition predicts; CF-27 + CF-28 are mechanical surgery on the W14-4 framework-language and Master Inventory Row #9 split; CF-29 audits the Type-F/Type-S partition across pillars; CF-30 decides whether the operator-projection separation rule rises to permanent epistemic-discipline.md status.

**Substrate framing** (per `phononic-framing.md` §"IS Space, Not IN Space"): the substrate IS the 3-channel-decomposed observable. Each channel is a phononic-excitation cohomology class on the spectral triple (A_K, H_K, D_K). The cross-pillar bridge map (HKR / K-theory boundary / Connes-Karoubi pairing) IS the substrate-IS-to-laboratory-IN morphism — NOT a coordinate transformation between two pre-existing geometric containers.

**Decisive vs informative** (per `feedback_reporting-framing.md`):
- Decisive gates: CF-25 (Level 1 theorem PASS = registry §VII-X landing; FAIL = no extension across Pillar II/III/IV, Level-1 candidate withdrawn).
- Informative gates: CF-26 (per-mode phase distribution, structural diagnostic with no a-priori threshold), CF-29 (cross-pillar partition audit; expected to re-classify ≥1 of {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s}).
- Mechanical: CF-27, CF-28 (registry surgery; PASS = on-disk artifact existence per §"Wave Classification" M1 substrate-COMPUTE classification).
- Decision: CF-30 (rule-promotion ternary; K calibration corpus cardinality test).

---

## Wave 4 Decision Point Prerequisites

Wave 4 has the following hard prerequisites at dispatch time. Per `feedback_dispatch-discipline.md`, planner expectations are recorded but the wave executes when the listed input artifacts exist with non-trivial size; runtime mismatches resolve in-script per the v3-recovery procedure.

### Required upstream artifacts (pre-existing at S86-close, verified at plan-freeze)

| Source | Path | S86-close status | Wave-4 consumer |
|:-------|:-----|:-----------------|:----------------|
| `permanent-results-registry.md` §VII.W (Pillar III↔IV bridge theorem; W-5 PASS-UNCONDITIONAL at Hochschild-cohomology level) | `sessions/permanent-results-registry.md` | LANDED (S86 W-5; level-3 empirical 0.0095% F_4 strict at L_max=10) | CF-25 (template for cross-pillar bridge anatomy; CF-25 extends Pillar III↔IV to 3-channel × Pillar II/III/IV) |
| `cross-pillar-bridge-anatomy.md` (5 IS-not-IN elements + 3-level ladder) | `.claude/rules/cross-pillar-bridge-anatomy.md` | LANDED (S86 W-5 RULE-1 + RULE-2; T1-3) | CF-25 (mandatory anatomy discipline) |
| `_cross_pillar_bridge_audit.py` | `computations/_cross_pillar_bridge_audit.py` | EXISTS (per context §0 validator inventory) | CF-25 plan-freeze validator |
| Type-F observable partition (S86 W-4 R3 closure) | `sessions/archive/session-86/session-86-w4-workingpaper.md` (and successor) | LANDED at S86 W-4 R3 | CF-26 (32-mode Bogoliubov basis indexing); CF-29 (Type-F vs Type-S partition source) |
| W14-4 framework-language §line 414-422 | `sessions/archive/session-86/session-86-w14-workingpaper.md:414-422` | LANDED at S86 W14-4 (target of CF-27 surgery) | CF-27 (replacement-text source) |
| Master Inventory Row #9 (f_NL_folded) | `sessions/framework/registry/falsifier-master-inventory.md` Row #9 | LANDED | CF-28 (split surgery target) |
| `joint-theorem-promotion.md` 4-stage pathway | `.claude/rules/joint-theorem-promotion.md` | LANDED (S86 W-9 RULE-1; T1-9) | CF-25 (joint clauses if any); CF-29 (partition audit may surface joint clauses) |
<!--
  AMRI fix (2026-04-28): row removed. The pin source path
  `.claude/agent-memory/orchestrator/feedback_rules-compensate-missing-structure.md` does
  NOT exist on disk (the actual file lives in user-project memory at
  `~/.claude/projects/C--sandbox-Ainulindale-Exflation/memory/feedback_rules-compensate-missing-structure.md`),
  AND orchestrator memory at that path triggers AMRI Test 1 per `.claude/rules/agent-standards.md` §AMRI.
  The K=3 promotion threshold is operationalized in CF-30's gate threshold itself
  (`count(corpus_instances) >= 3 ⇒ PASS`); the meta-rule prose is not load-bearing for the verdict.
  Per user instruction (2026-04-28) the meta-rule is NOT promoted to a project rule file
  (anti-rule-bloat: a rule warning against rule-bloat would itself be the bloat).
-->
| S38 algebraic GGE-permanence theorem | `permanent-results-registry.md` (S38 entry) | LANDED | CF-26 (post-tau_fold GGE state cross-check) |
| S86 W4 P4 commit `xi_E_GGE_inv = 13.642473425595973` | `canonical_constants.py` (per W5a-2 §10 substrate-first canonical) | LANDED | CF-26 (substrate-canonical for GGE quantities) |

### Plan-freeze validator gates (per context §0.4)

Per the no-tech-debt rule (`CLAUDE.md §"No Technical Debt"`), the W4 plan-freeze runs:

1. `python computations/_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w4.md`
2. `python computations/_yaml_gate_validator.py sessions/session-plan/session-87-plan-w4.md`
3. `python computations/_source_reconciliation_audit.py` (5+1-class taxonomy + cluster-span canonical-metric + Class-(f) PIN-PLACEHOLDER)
4. `python computations/_substrate_first_provenance_audit.py` (V.1 manual review until S87 implementation lands)
5. `python computations/_cross_pillar_bridge_audit.py` (mandatory for CF-25 5-anatomy + 3-level ladder discipline)
6. `python computations/_pru_cardinality_audit.py` (PRU cardinality pre-flight)
7. Pre-dispatch grep on `computations/s86_gate_verdicts.txt` for collision check on S87 gate IDs (no `S87-*` entries should pre-exist)

---

## §W4-1. S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF (CF-25, Level 1, HIGH-EVOI)

**Trigger**: `[VERIFY-THEOREM]`
**Classification**: GEOMETRIC (cross-pillar bridge theorem; substrate-IS spectral-triple cohomology)
**Owner**: `connes-ncg-theorist` (lead), `lizzi-spectral-functional-theorist` (Mellin-anchor co-signer)

### Hypothesis

The 3-channel decomposition of substrate observables — (Channel-1) 3-pt-connected vertex (irreducible) / (Channel-2) pair-cumulant (semi-reducible) / (Channel-3) 2-pt-separable (reducible) — extends as a STRUCTURAL THEOREM across Pillar II (Mellin-cone spectral) / Pillar III (BdG superfluid analog) / Pillar IV (Peotta-Törmä quantum-metric / continuum BZ-trace). The bridge map at each pillar pair is the same Connes-Karoubi pairing form that S86 W-5 §VII.W instantiated for Pillar III↔IV; CF-25 generalizes that bridge from a single-pillar pair to a 3-channel × 3-pillar tensor product.

### Substrate framing (per `phononic-framing.md` §"IS Space, Not IN Space")

The substrate IS the 3-channel-decomposed cohomology class on (A_K, H_K, D_K). Each channel is a phononic-excitation cohomology class — Channel-1 is a rank-3 Hochschild cocycle (3-pt-connected = irreducible vertex); Channel-2 is a rank-2 pair-cumulant cocycle (semi-reducible = pair-correlator with subtracted 2-pt); Channel-3 is a rank-1 2-pt-separable cocycle (Wick-decomposable). The pillar labels (II, III, IV) are NOT pre-existing geometric containers in which the channels live — they ARE the substrate-IS observables themselves under three distinct regulator-class restrictions.

### Threshold (PASS / FAIL / INFO; pre-registered)

- **PASS** = ALL FIVE of the following hold:
  1. Cross-pillar bridge anatomy 5-element block (per `cross-pillar-bridge-anatomy.md`) declared explicitly in script output JSON for each of the three channels: substrate-IS observable / laboratory-IN observable / bridge map / algebraic envelope / empirical anchor.
  2. 3-level structural-confidence ladder declared for each of the three channels: Level 1 cohomology-class identity (regulator-invariant; L-independent); Level 2 algebraic envelope (L^{-α} bound for some α ≥ 2); Level 3 empirical anchor at canonical L_max=10 satisfying Level 2.
  3. Level-3 empirical value `< Level-2 envelope value` at canonical L_max for ALL three channels (cross-pillar bridge anatomy registry-PASS criterion).
  4. Bridge map for each channel explicitly named (HKR / K-theory boundary / Connes-Karoubi pairing — NOT "analogous to" or "corresponds to").
  5. NCG-axiomatic verification: each channel's bridge preserves the 7 NCG axioms (dimension, regularity, finiteness, reality, first-order, orientability, Poincaré duality) under the morphism A_K ⊗ A_pillar → A_K (channel-restricted); explicit verification per axiom in working-paper §Substrate framing.

- **FAIL** = ANY of the following hold:
  - Any of the 5 anatomy elements absent for any channel (cross-pillar bridge anatomy registry-INCOMPLETE);
  - Level-3 violates Level-2 at any channel (empirical anchor exceeds algebraic envelope);
  - Any bridge map cited only via "analogous"/"corresponds to" without explicit HKR/K-theory/Connes-Karoubi naming;
  - First-order condition `[[D, a], b^o] = 0` violated for any channel-restricted algebra.

- **INFO** = exactly TWO of the three channels achieve Level-1 + Level-2 + Level-3 satisfaction; the third channel has Level-1 candidate but Level-3 unverified at canonical L_max=10. Records as STAGE-1-CANDIDATE per `joint-theorem-promotion.md`; Stage-2 cross-reviewer dispatch deferred to S88.

**Tolerance rule**: THEOREM (axiom-level + cohomology-class identity at Level 1; numerical RATIO at Level 3 with `match/envelope < 1.0` mandatory).

### Machinery pin (PRDR) — per `gate-verdicts.md` §Pre-Registration Protocol

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt

N_eval: 155984              # canonical L_max=10 D_K spectrum cache size
L_max: 10                   # canonical pin per S86-close
scan_range: tau = tau_fold = 0.190 (fixed, single-point bridge evaluation)
step_size: N/A (analytic + spectral cache; no numerical integration)
tolerance:
  Level_1: bit-exact cohomology-class identity (Sage QQ verification mandatory)
  Level_2: algebraic envelope L^{-3} at d=4 (substrate-distance-3 pole; matches W-5 §VII.W canonical)
  Level_3: rel_err < L_max^{-3} = 10^{-3} = 0.10% per channel
scheme: 3-channel x 3-pillar tensor product over Connes-Karoubi pairing
convention: substrate-distance-anchored Mellin-cone (canonical from CCM 1996; Connes-Chamseddine spectral action)
random_seed: N/A (deterministic spectral cache)
GPU path: N/A for analytic verification; torch.linalg.eigh via "phonon-exflation-sim/.venv312/Scripts/python.exe" if numerical cross-check on L_max=10 spectrum dispatched

publication_sig_figs: 15 (full float64 for Level 3 numerical anchors; Sage QQ exact rationals for Level 1 cohomology pairings)
```

### Substitution chain (per `math-scripts.md` §"Double-Check Logic Before Compute")

```
Step 1 (definitions):
  Channel-1 cocycle:   phi_3 ∈ HC^3(A_K)        [3-pt-connected; rank-3 Hochschild]
  Channel-2 cocycle:   phi_2 ∈ HC^2(A_K) - im(b)  [pair-cumulant; rank-2 modulo coboundary]
  Channel-3 cocycle:   phi_1 ∈ HC^1(A_K)        [2-pt-separable; rank-1, Wick-reducible]
  Pillar restriction:  pi_p : A_K -> A_p,  p ∈ {II, III, IV}
  Bridge map:          B_p^k : (A_K^{<=L} channel-k) -> (A_p continuum channel-k)
                       B = HKR / K-theory-boundary / Connes-Karoubi pairing

Step 2 (substitution):
  Cross-pillar 3-channel pairing tensor:
    R_{p,q}^{(k)}(L_max) := <[phi_k|_{A_K^{<=L}}], [Ch(P_pillar_q^{(k)}(tau_fold))]>_{HC^k}

  where P_pillar_q^{(k)} is the channel-k Bott projector on pillar q's spectral data.

Step 3 (simplification):
  By S86 W-5 §VII.W (registered cross-pillar bridge), the (k=2, p=III, q=IV) instance
  satisfies Level-1 identity at the cohomology-class level:
    R_universal^{(2)}_{III,IV} = <[phi_g^{sym}], [Ch(P_0(tau_fold))]>
  with Level-2 L^{-3} envelope at d=4 and Level-3 0.0095% F_4 strict at L_max=10.

  CF-25 extends this to all 9 cells (k=1,2,3) x (p,q) ∈ pillar-pair set:
    R^{(k)}_{p,q}(L_max=10) ?  satisfies (Level-1 cohomology + Level-2 envelope + Level-3 < envelope)

Step 4 (direction):
  PASS direction: ALL 9 cells satisfy the 3-level ladder simultaneously.
  No single cell can rescue the theorem if another cell FAILs.
  Logical AND across 9 cells; rank-3 statement.

Step 5 (sign for [VERIFY-THEOREM] trigger):
  sign_verdict = PASS iff predicted Level-3 < Level-2 direction holds at every cell
                 (numerical |error| < envelope across all 9 cells).
  magnitude_verdict = PASS iff Level-3 max relative error < 0.10% (canonical Level-3 band).
  regime_verdict = VALID iff L_max=10 within bridge-map convergence radius
                  (S86 W-5 § verified L_max=10 within radius for k=2; CF-25 extends to k=1, k=3).
```

### Input SHA-256 pins

| File | Pin type | Provenance |
|:-----|:---------|:-----------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | runtime SHA-256 | canonical L_max=12 spectrum cache (S84) — load-bearing for L_max=10 strict subset extraction |
| `sessions/permanent-results-registry.md` §VII.W | content_sha256 of registry block | S86 W-5 PASS-UNCONDITIONAL anchor (Pillar III↔IV bridge theorem) |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | content_sha256 | mandatory anatomy discipline source |
| `.claude/rules/joint-theorem-promotion.md` | content_sha256 | 4-stage pathway (CF-25 lands STAGE-1-CANDIDATE if INFO band) |
| `computations/canonical_constants.py` | content_sha256 | xi_E_GGE_inv, tau_fold, M_KK, Vol_SU3 imports |
| `sessions/archive/session-86/session-86-w4-workingpaper.md` (Type-F partition section) | content_sha256 | Type-F 32-mode Bogoliubov basis source |
| S38 algebraic GGE-permanence theorem block in `permanent-results-registry.md` | content_sha256 | post-tau_fold GGE relic structure cross-reference |

### Expected output 4-tuple

```
(value=max_rel_err_across_9_cells, scheme=3-channel-x-3-pillar-Connes-Karoubi, convention=substrate-distance-anchored-Mellin, L_max=10)
```

### Output artifacts (mandatory at task-complete per `agent-standards.md` §"Completion Verification")

- **Script**: `computations/s87_w4_cross_pillar_3_channel_theorem_proof.py`
- **Data**: `computations/s87_w4_cross_pillar_3_channel_theorem_proof.npz` with the 9-cell `R^{(k)}_{p,q}(L_max=10)` tensor + level-1 / level-2 / level-3 status per cell + axiom-verification status per channel
- **Plot**: `computations/s87_w4_cross_pillar_3_channel_theorem_proof.png` (9-cell heatmap of level-3 rel_err / level-2 envelope ratio)
- **Verdict line**: appended to `computations/s87_gate_verdicts.txt` per S87+ schema-v2 dual-SHA + 3-tuple annotation
- **Working-paper section**: §VII.W4-1 "Cross-Pillar 3-Channel Theorem" with substantive content (≥15 lines; 5 anatomy elements + 3-level ladder per channel + axiom-verification table + substrate framing block)
- **Registry landing target**: `sessions/permanent-results-registry.md` §VII-X.W4-1 (allocate next-free letter under §VII-X umbrella; use parallel-writer-race append-only Python writer per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene")

### Joint clauses (per `joint-theorem-promotion.md`)

The theorem is JOINT cross-axis (NCG-axiomatic + spectral-functional). Joint clauses requiring Stage-2 two-agent independent-verify (deferred to S88+):
- (joint) Bridge-map axiom-preservation across all 3 channels (NCG-axiomatic side, connes-ncg);
- (joint) Mellin-cone substrate-distance-3 envelope at d=4 verified across all 3 channels (spectral-functional side, lizzi-spectral).
- (single-axis) Channel-1 / Channel-2 / Channel-3 cocycle-rank verification (connes-ncg only);
- (single-axis) Pillar II / III / IV regulator-class restriction (lizzi-spectral only).

If CF-25 closes PASS → STAGE-1-CANDIDATE registry entry under `joint-theorem-promotion.md`; Stage-2 dispatch queued as S88-CF-25-STAGE-2-INDEPENDENT-VERIFY (NEW carry-forward).
If CF-25 closes INFO → STAGE-1-CANDIDATE recorded with the missing-channel flag; Stage-2 dispatch deferred until missing channel closes.
If CF-25 closes FAIL → no registry entry; theorem withdrawn; carry-forward to S88 only if a specific axiom-preservation defect is identified and remediable.

### What PASS / FAIL / INFO mean for the solution space

- **PASS** opens the 3-channel decomposition as a structural axis of the framework — every substrate observable can be channel-decomposed and pillar-restricted, with quantitative bridge-map convergence rates. Pillar-V (Type-F partition; W-4 origin) gains a structural extension from the Pillar III↔IV W-5 result. Future falsifier rows can use the channel-decomposition to specify SUBSTRATE-CLEAN cocycles (per `inheritance-falsifier-protocol.md` Class-A kernel-signature tests).
- **FAIL** closes the 3-pillar uniform extension — the 3-channel decomposition is then localized to specific pillar pairs and CANNOT be uniformly assumed across substrate observables. Downstream consumers (CF-29 cross-pillar audit; falsifier-design at S88+) must then specify pillar-pair-by-pillar-pair which channels apply.
- **INFO** records the 2-channel partial extension; STAGE-1-CANDIDATE preserves the result for S88 Stage-2 verify; the missing channel becomes a discrete S88 follow-up (NEW carry-forward).

### Plan-freeze validator: `_cross_pillar_bridge_audit.py` — MANDATORY

Per `cross-pillar-bridge-anatomy.md` §Audit at plan-freeze, run the 4-element audit before dispatch:

1. All 5 IS-not-IN anatomy elements present for all 3 channels (script-output JSON enumeration);
2. All 3 level markers (Level 1 / Level 2 / Level 3) present with explicit values for all 3 channels;
3. Level 3 numerical value < Level 2 envelope at canonical L_max=10 for all 3 channels;
4. Bridge map explicitly named per channel (HKR / K-theory boundary / Connes-Karoubi pairing — NOT "analogous to").

Failure of any of (1)-(4) → audit FAIL → CF-25 routes to FAIL with NEEDS-COMPUTATION block at the missing element.

---

## §W4-2. S87-TYPE-F-PER-MODE-PHASE-AUDIT (CF-26, Level 1.5, MEDIUM-HIGH-EVOI)

**Trigger**: `[VERIFY]`
**Classification**: PHONONIC (Bogoliubov-phase distribution on post-tau_fold GGE state; substrate-IS phase-content of Type-F mode partition)
**Owner**: `connes-ncg-theorist` (lead, NCG-axiomatic phase-content per A_K bimodule structure), `lizzi-spectral-functional-theorist` (co-signer, Mellin-anchor cross-check)

### Hypothesis

The Type-F observable partition (S86 W-4 R3 closure) predicts a CANONICAL Bogoliubov-phase distribution {phi_a}_{a=1..32} on the post-tau_fold GGE state. The distribution is determined by the spectral triple's bimodule structure (A_K = C ⊕ H ⊕ M_3(C); KO-dim=6, J-D_K=0, gamma-A=A-gamma) and the S38 algebraic GGE-permanence theorem (post-tau_fold relic state is integrable; never thermalizes; phase distribution persists). CF-26 computes {phi_a} explicitly and audits against expected NCG-axiomatic constraints.

### Substrate framing

The substrate IS the 32-mode Bogoliubov-phase tuple {phi_a}_{a=1..32}. Each phi_a is a phononic-excitation phase angle — NOT a coordinate phase on a pre-existing 32-D space. The 32 modes ARE the Type-F partition's irreducible representation count under the (A_K, H_K, D_K) bimodule action; the phase distribution IS the GGE relic structure restricted to Type-F.

### Threshold (PASS / FAIL / INFO; pre-registered)

- **PASS** = ALL THREE of the following hold:
  1. The 32-mode Bogoliubov-phase distribution {phi_a}_{a=1..32} computed; histogram emitted.
  2. NCG-axiomatic constraints satisfied: (a) phase distribution invariant under J (real-structure); (b) phase distribution invariant under gamma (chirality); (c) phase distribution consistent with first-order condition [[D_K, a], b^o] = 0 for all (a, b) ∈ A_K × A_K^{op}.
  3. S38 algebraic GGE-permanence cross-check: phase distribution at tau_fold + delta = 0.001, 0.01, 0.05 stable (max relative deviation < 1% across delta values; INFO band 1-10%; FAIL > 10% — GGE relic should not thermalize).

- **FAIL** = ANY of the following:
  - Histogram cannot be computed (e.g., 32-mode basis not well-defined on canonical L_max=10 cache);
  - Any of the 3 NCG-axiomatic invariances violated;
  - GGE-stability cross-check fails (phase distribution drifts > 10% across delta values).

- **INFO** = phase distribution computed AND NCG-axiomatic invariances satisfied AND GGE-stability cross-check in the 1-10% drift band; no a-priori threshold for the histogram shape itself (this is a structural diagnostic; CF-26 emits the distribution as data for S87+ downstream consumption).

**Tolerance rule**: ABSOLUTE for invariance checks (machine-eps for J / gamma / first-order); RATIO for GGE-stability (1% / 10% bands).

### Machinery pin (PRDR)

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt

N_eval: 155984              # L_max=10 D_K spectrum cache (canonical)
L_max: 10                   # S86-close canonical
scan_range: tau ∈ {tau_fold, tau_fold + 0.001, tau_fold + 0.01, tau_fold + 0.05} = {0.190, 0.191, 0.200, 0.240}
step_size: N/A (4-point GGE-stability scan)
tolerance:
  axiom_invariance: < 1e-12 (machine-eps for J / gamma / first-order under SU(N) generators)
  GGE_stability: < 1% PASS, 1-10% INFO, > 10% FAIL
scheme: Bogoliubov-phase angle decomposition on Type-F 32-mode basis (S86 W-4 R3 closure)
convention: post-tau_fold GGE relic state per S38 algebraic permanence theorem
random_seed: N/A (deterministic from spectral cache + canonical phase-extraction algorithm)
GPU path: torch.linalg.eigh on AMD RX 9070 XT for spectrum subset extraction; "phonon-exflation-sim/.venv312/Scripts/python.exe"

publication_sig_figs: 12 (phase angles in radians, full float64 emitted; histogram bin precision 0.01 rad = 1e-2)
```

### Substitution chain

```
Step 1 (definitions):
  D_K(tau)         = Jensen-deformed SU(3) Dirac operator at deformation tau
  Type-F partition = S86 W-4 R3 closure: 32-mode irreducible decomposition of
                     A_K bimodule action restricted to Type-F (operator-projection-clean)
  {U_a, V_a}_{a=1..32} = Bogoliubov coefficients on Type-F mode a
  phi_a            = arg(U_a / V_a*) ∈ (-π, π]   [Bogoliubov phase angle, mode a]
  J                = real structure on H_K
  gamma            = chirality grading on H_K
  GGE relic state  = post-tau_fold integrable phase-distribution per S38

Step 2 (substitution):
  phi_a(tau) := arg(U_a(tau) / V_a*(tau))  for tau in {tau_fold, tau_fold+δ}
  J-invariance test:    {phi_a(tau)} =? {J(phi_a)(tau)}  (set equality up to permutation)
  gamma-invariance:     {phi_a(tau)} =? {-phi_a(tau)} (gamma-flip on chirality-odd modes)
  First-order test:     <[[D_K, a], b^o] psi_mode_a, psi_mode_a> = 0 for all (a, b) ∈ A_K × A_K^op

Step 3 (simplification):
  PASS iff (axiom_invariance machine-eps) AND (GGE-stability rel_dev < 1%)
  INFO iff (axiom_invariance machine-eps) AND (1% ≤ GGE-stability < 10%)
  FAIL iff (axiom violation) OR (GGE-stability > 10%)

Step 4 (direction):
  No directional pre-registration on the histogram shape — CF-26 emits {phi_a}
  as a structural diagnostic for S87+ downstream consumers (CF-29 partition audit
  may consume the distribution for cross-pillar comparison).

Step 5 (sign for [VERIFY] trigger):
  sign_verdict = N/A (no signed delta predicted; histogram is data)
  magnitude_verdict = PASS iff GGE-stability < 1%; INFO iff 1-10%; FAIL iff > 10%
  regime_verdict = VALID iff tau ∈ [tau_fold, tau_fold + 0.05] within S38 GGE-permanence
                   integrable regime (S38 verified for delta < 0.1 of tau_fold)
```

### Input SHA-256 pins

| File | Pin type | Provenance |
|:-----|:---------|:-----------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | runtime SHA-256 | L_max=10 strict subset (canonical) |
| `sessions/archive/session-86/session-86-w4-workingpaper.md` (Type-F partition § R3 closure) | content_sha256 | Type-F 32-mode partition source |
| `permanent-results-registry.md` (S38 algebraic GGE-permanence theorem block) | content_sha256 | post-tau_fold GGE relic structure |
| `computations/canonical_constants.py` (tau_fold, M_KK, Vol_SU3, xi_E_GGE_inv) | content_sha256 | substrate-canonical pins |
| `computations/s52_bogoliubov_amp.npz` | runtime SHA-256 | existing Bogoliubov amplitude data (cross-check baseline) |
| `computations/canonical_classes.py` (EXFLATION_CLASS for n_pairs CONSEQUENCE / w0_FW + n_s_framework OBSERVABLE_OUTPUT) | content_sha256 | cross-class consistency check |

### Expected output 4-tuple

```
(value=max_GGE_drift_rel_dev_across_4_tau_points, scheme=Bogoliubov-phase-Type-F-32-mode, convention=post-tau_fold-S38-GGE-relic, L_max=10)
```

### Output artifacts

- **Script**: `computations/s87_w4_type_f_per_mode_phase_audit.py`
- **Data**: `computations/s87_w4_type_f_per_mode_phase_audit.npz` with `phi_a` 32-tuple at each of 4 tau points + axiom-invariance flags + GGE drift table
- **Plot**: `computations/s87_w4_type_f_per_mode_phase_audit.png` (32-bin phase histogram at tau_fold + GGE drift vs delta_tau)
- **Verdict line**: appended to `computations/s87_gate_verdicts.txt`
- **Working-paper section**: §VII.W4-2 "Type-F Per-Mode Phase Audit" with substantive content (≥15 lines; histogram description + axiom-invariance verification + GGE-stability table + substrate framing block)

### What PASS / FAIL / INFO mean for the solution space

- **PASS** confirms the Type-F partition predicts a STABLE Bogoliubov-phase distribution under S38 GGE-permanence, with NCG-axiomatic constraints intact. The {phi_a} distribution becomes a substrate-canonical 32-tuple consumable by CF-29 (cross-pillar Type-F/Type-S audit), CF-25 (Channel-2 pair-cumulant cross-check on Type-F-restricted observables), and S88+ falsifier-design rows requiring per-mode phase signatures.
- **FAIL** closes the canonical Type-F 32-mode partition as a substrate-stable structural object — either the partition is not well-defined on the canonical cache, or NCG-axiomatic invariances fail (which would invalidate the S86 W-4 R3 closure and force its re-derivation), or GGE-stability fails (which would falsify S38 algebraic permanence). All three FAIL routes would be high-impact framework events; downstream consumers must wait for re-derivation.
- **INFO** records the 32-tuple distribution + GGE drift in the 1-10% band; downstream consumers cite the distribution but flag the band as a partial GGE-stability constraint requiring S88+ refinement.

---

## §W4-3. S87-F-NL-FOLDED-W14-4-LANGUAGE-CORRECTION (CF-27, Level 2)

**Trigger**: `[AUDIT]`
**Classification**: NON-PHONONIC (mechanical text-replacement registry surgery; no new substrate-physics derivation)
**Owner**: `mack-cosmic-bridge` (sole writer for `falsifier-master-inventory.md` per `feedback_mack-bridge-role.md`); `connes-ncg-theorist` co-signs as the W-4 wave lead

### Hypothesis

W14-4 framework-language at `sessions/archive/session-86/session-86-w14-workingpaper.md:414-422` contains framework-language errors (phrasing that violates `phononic-framing.md` §"IS Space, Not IN Space" by treating substrate as in-container; or mis-attribution of f_NL_folded prediction as substrate-derived when it is laboratory-IN observable). The locked replacement text (drafted at S86 W-4 R3 closure; verbatim source: `sessions/archive/session-86/session-86-w4-workingpaper.md` joint-recommendation block) corrects the framing and re-attributes the observable correctly. CF-27 mechanically replaces the §line 414-422 block AND updates the corresponding Master Inventory row's framing column.

### Substrate framing

f_NL_folded is a LABORATORY-IN observable (CMB bispectrum measurement on continuum sky; folded-template pathway-keyed). The substrate-IS counterpart is the 3-pt-connected vertex cocycle phi_3 ∈ HC^3(A_K) Channel-1 of CF-25. The bridge map (HKR boundary) connects them. The W14-4 framework-language correction makes this substrate-IS-vs-laboratory-IN distinction explicit; the replacement text adopts the per-section §3 language pattern from `phononic-framing.md`.

### Threshold (PASS / FAIL / INFO)

- **PASS** = ALL FOUR of the following hold:
  1. `sessions/archive/session-86/session-86-w14-workingpaper.md:414-422` block contains the locked replacement text verbatim (byte-exact match against the joint-recommendation source);
  2. Master Inventory row corresponding to f_NL_folded has its framing column updated to substrate-IS-vs-laboratory-IN distinction (citing CF-25 Channel-1 as the substrate-IS counterpart);
  3. content_sha256 of the replaced block matches the pre-registered locked-replacement-text SHA;
  4. No other §lines outside [414, 422] modified (mechanical-surgery scope discipline; verified by line-count diff).

- **FAIL** = ANY of:
  - The replacement is not byte-exact to the locked text;
  - Master Inventory row framing column not updated;
  - content_sha256 mismatch;
  - Side-effects detected (modifications outside [414, 422]).

- **INFO** = N/A (mechanical surgery is binary: PASS or FAIL).

**Tolerance rule**: ABSOLUTE (byte-exact text match; no numerical tolerance).

### Machinery pin (PRDR)

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt

N_eval: N/A (text-replacement; no spectrum)
L_max: N/A (text-replacement; no L_max scan)
scan_range: lines [414, 422] of session-86-w14-workingpaper.md
step_size: N/A
tolerance: byte-exact (SHA-256 match against locked replacement text)
scheme: in-place line-range Edit via Python writer (NOT Edit tool; per `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" — append-only Python writer pattern adapted to in-place line-range surgery)
convention: phononic-framing.md §"IS Space, Not IN Space" mandatory reframe
random_seed: N/A
GPU path: N/A

publication_sig_figs: N/A (text)
```

### Substitution chain

```
Step 1 (definitions):
  W14-4_block       = current text at session-86-w14-workingpaper.md:414-422
  locked_text       = pre-registered replacement text (source: S86 W-4 R3 joint-recommendation block)
  inventory_row_f_NL_folded = Master Inventory row #9 (per CF-28; pre-split)

Step 2 (substitution):
  diff = (W14-4_block before CF-27) XOR (W14-4_block after CF-27)
  PASS criterion: diff = (locked_text replacement on lines [414, 422] only)

Step 3 (simplification):
  Verify: SHA-256(new W14-4_block lines 414-422) == SHA-256(locked_text)
  Verify: SHA-256(W14-4 lines 1-413 + 423-end before CF-27) == SHA-256(W14-4 lines 1-413 + 423-end after CF-27)
  Verify: inventory_row_f_NL_folded.framing column updated to substrate-IS-vs-laboratory-IN

Step 4 (direction):
  No direction; mechanical replacement.

Step 5 (sign for [AUDIT] trigger):
  sign_verdict = N/A
  magnitude_verdict = PASS iff byte-exact; FAIL iff not byte-exact
  regime_verdict = VALID (text replacement always within regime of validity)
```

### Input SHA-256 pins

| File | Pin type | Provenance |
|:-----|:---------|:-----------|
| `sessions/archive/session-86/session-86-w14-workingpaper.md` (full file pre-CF-27) | content_sha256 | pre-replacement state |
| `sessions/archive/session-86/session-86-w4-workingpaper.md` (joint-recommendation block) | content_sha256 | locked replacement text source |
| `sessions/framework/registry/falsifier-master-inventory.md` (Row #9 pre-CF-28) | content_sha256 | inventory framing-column update target |
| `.claude/rules/phononic-framing.md` (substrate-IS-vs-laboratory-IN reframe) | content_sha256 | framing convention source |
| `computations/canonical_constants.py` (f_NL_FW_S82_equilateral, f_NL_FW_S67_folded, f_NL_FW_S85_W9_3_analytic_template per `math-scripts.md` §"Canonical Write-Order" pathway-keyed) | content_sha256 | pathway-keyed canonical pins |

### Expected output 4-tuple

```
(value=byte_exact_PASS_or_FAIL_flag, scheme=text-replacement-byte-exact, convention=phononic-framing-reframe, L_max=N/A)
```

### Output artifacts

- **Script**: `computations/s87_w4_f_nl_folded_w14_4_language_correction.py` (mack-cosmic-bridge writes; one-shot Python writer; preserves audit trail per `epistemic-discipline.md`)
- **Data**: `computations/s87_w4_f_nl_folded_w14_4_language_correction.npz` with pre/post SHA-256 of W14-4 block + diff line range + inventory-row-update flag
- **Plot**: N/A (mechanical surgery; no plot)
- **Verdict line**: appended to `computations/s87_gate_verdicts.txt`
- **Working-paper section**: §VII.W4-3 "f_NL_folded W14-4 Language Correction" with substantive content (≥15 lines; locked replacement text reproduced + diff summary + substrate framing block + cross-link to CF-28)

### What PASS / FAIL means for the solution space

- **PASS** corrects the W14-4 framework-language and updates the Master Inventory framing column. No structural change to the framework's predictions; the f_NL_folded prediction value is unchanged. The substrate-IS-vs-laboratory-IN distinction becomes explicit in the registry; downstream falsifier-design citations cannot drift on the framing.
- **FAIL** indicates a mechanical surgery defect (byte-mismatch or scope-overrun); the W14-4 block remains in its pre-correction state; the carry-forward propagates to S88 with the specific defect identified and a re-dispatch spec.

---

## §W4-4. S87-F-NL-FOLDED-2-OBSERVABLE-REGISTRY-SPLIT (CF-28, Level 3, mechanical)

**Trigger**: `[AUDIT]`
**Classification**: NON-PHONONIC (mechanical registry surgery; row split)
**Owner**: `mack-cosmic-bridge` (sole writer for `falsifier-master-inventory.md`); `connes-ncg-theorist` co-signs

### Hypothesis

Master Inventory Row #9 (f_NL_folded) currently bundles TWO distinct observables: (a) f_NL_folded as a CMB bispectrum laboratory-IN observable; (b) a related substrate-IS / per-mode 3-pt-connected vertex prediction. Per the W-4 R3 closure, these are observationally and structurally distinct — different detector horizons, different internal-consistency splits, different canonical_constants.py pathway keys (per `math-scripts.md` §"Canonical Write-Order for New Framework Predictions" pathway-keyed sub-keying). CF-28 mechanically splits Row #9 into Row #9a + Row #9b with appropriate framing per row.

### Substrate framing

The split makes EXPLICIT that the substrate IS the 3-pt-connected vertex cocycle (phi_3 ∈ HC^3(A_K), Channel-1 of CF-25); the laboratory measures the CMB bispectrum (f_NL_folded). Pre-split, Row #9 conflates these layers; post-split, Row #9a is laboratory-IN and Row #9b is substrate-IS, with explicit bridge map (HKR / Connes-Karoubi pairing) cited.

### Threshold (PASS / FAIL / INFO)

- **PASS** = ALL FIVE of:
  1. Row #9 deleted from `falsifier-master-inventory.md`;
  2. Row #9a inserted with f_NL_folded laboratory-IN framing (5 IS-not-IN anatomy elements declared);
  3. Row #9b inserted with substrate-IS phi_3 cocycle framing (5 IS-not-IN anatomy elements declared);
  4. All cross-references to Row #9 (in other inventory rows, in registry entries, in agent memories) updated to point to Row #9a OR Row #9b as appropriate (cross-reference walk required);
  5. SHA-256 of the inventory file post-CF-28 emitted; rows #9a and #9b appear with full 64-char audit_sha256 + content_sha256 dual-SHA companion rows per inventory append-only Python writer pattern.

- **FAIL** = ANY of:
  - Row #9 still present alongside #9a/#9b (duplication);
  - Either #9a or #9b missing IS-not-IN anatomy elements;
  - Cross-reference walk incomplete (orphaned references to Row #9 detected by grep);
  - Dual-SHA companion rows malformed.

- **INFO** = exactly one cross-reference orphaned and cited as a discrete S88+ carry-forward (specific orphan path identified); other 4 PASS conditions held.

**Tolerance rule**: ABSOLUTE (binary structural integrity).

### Machinery pin (PRDR)

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt

N_eval: N/A
L_max: N/A
scan_range: Master Inventory rows; cross-reference walk over registry + agent memories
step_size: N/A
tolerance: binary (PASS iff all 5 conditions; FAIL iff any condition violated; INFO iff exactly 1 orphan)
scheme: registry-row split via append-only Python writer (per `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race")
convention: 5-element IS-not-IN anatomy declared per row (per `cross-pillar-bridge-anatomy.md`)
random_seed: N/A
GPU path: N/A

publication_sig_figs: N/A (text)
```

### Substitution chain

```
Step 1 (definitions):
  Row_9_pre  = current Master Inventory Row #9 (single bundled f_NL_folded row)
  Row_9a     = post-split laboratory-IN row (f_NL_folded CMB bispectrum)
  Row_9b     = post-split substrate-IS row (phi_3 cocycle ∈ HC^3(A_K), Channel-1)
  cross_refs(Row_9) = grep("Row #9", filesystem) - excluded paths

Step 2 (substitution):
  Inventory_post = Inventory_pre - Row_9 + Row_9a + Row_9b
  cross_refs_pre = grep("Row #9", filesystem) (pre-CF-28)
  cross_refs_post = each cross_ref ∈ cross_refs_pre is updated to either Row_9a or Row_9b

Step 3 (simplification):
  PASS iff (Row_9 absent post-CF-28) AND (Row_9a + Row_9b present with 5-anatomy each)
       AND (forall ref ∈ cross_refs_pre: ref points to {9a, 9b} post-CF-28)
       AND (dual-SHA rows correctly formatted for #9a + #9b)

Step 4 (direction):
  No direction; mechanical split.

Step 5 (sign for [AUDIT] trigger):
  sign_verdict = N/A
  magnitude_verdict = PASS iff all 5 conditions; FAIL iff any violated; INFO iff exactly 1 orphan
  regime_verdict = VALID
```

### Input SHA-256 pins

| File | Pin type | Provenance |
|:-----|:---------|:-----------|
| `sessions/framework/registry/falsifier-master-inventory.md` (pre-CF-28; pre-CF-27 framing-column update propagated) | content_sha256 | source state |
| `sessions/permanent-results-registry.md` (cross-reference scan target) | content_sha256 | cross-reference target file |
| `.claude/agent-memory/*/MEMORY.md` (cross-reference scan target) | content_sha256 | agent memory cross-reference targets |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | content_sha256 | 5-anatomy template source |
| CF-25 (CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF) verdict line — UPSTREAM dependency in same wave | runtime SHA | Channel-1 phi_3 cocycle definition for Row #9b substrate-IS framing |

### Cross-wave dependency

CF-28 depends on CF-25 PASS (Channel-1 phi_3 cocycle existence at Level-1 cohomology-class identity) for Row #9b substrate-IS framing. If CF-25 closes FAIL, CF-28 routes to PRE-REG-INC (per `mechanical-closure-discipline.md`) blocked on CF-25; the inventory split is deferred. If CF-25 closes INFO with Channel-1 PASS but Channel-2 / Channel-3 partial, CF-28 proceeds with Channel-1 reference for Row #9b.

### Expected output 4-tuple

```
(value=binary_split_PASS_FAIL_INFO_flag, scheme=registry-row-split, convention=5-element-IS-not-IN-anatomy-per-row, L_max=N/A)
```

### Output artifacts

- **Script**: `computations/s87_w4_f_nl_folded_2_observable_registry_split.py` (mack-cosmic-bridge writes; one-shot Python writer; cross-reference walk + grep-based orphan detection)
- **Data**: `computations/s87_w4_f_nl_folded_2_observable_registry_split.npz` with pre/post inventory SHA + cross-reference walk results + orphan list (empty on PASS; ≤1 entry on INFO)
- **Plot**: N/A
- **Verdict line**: appended to `computations/s87_gate_verdicts.txt`
- **Working-paper section**: §VII.W4-4 "f_NL_folded 2-Observable Registry Split" with substantive content (≥15 lines; pre-CF-28 Row #9 reproduced + post-CF-28 #9a + #9b reproduced + cross-reference walk summary + substrate framing block)

### What PASS / FAIL / INFO means for the solution space

- **PASS** establishes the substrate-IS-vs-laboratory-IN distinction at the registry level for f_NL_folded. Future falsifier-design citations cite Row #9a (lab) or Row #9b (substrate) explicitly; the conflation is closed.
- **FAIL** indicates a mechanical surgery defect; pre-CF-28 state preserved; carry-forward to S88 with specific defect.
- **INFO** records exactly one orphaned cross-reference; carry-forward to S88 specifies the orphan path for explicit update.

---

## §W4-5. S87-TYPE-F-TYPE-S-CROSS-PILLAR-AUDIT (CF-29, Level 4, post-Level-1)

**Trigger**: `[AUDIT]`
**Classification**: GEOMETRIC (cross-pillar partition audit on substrate spectral triple structure)
**Owner**: `connes-ncg-theorist` (lead, NCG-axiomatic partition criteria), `lizzi-spectral-functional-theorist` (co-signer, Mellin-anchor cross-classification)

### Hypothesis

The Type-F (operator-projection-clean) / Type-S (operator-projection-mixed) observable partition, established at S86 W-4 R3 closure for Pillar V (finite spectrum of A_K = C ⊕ H ⊕ M_3(C)), extends as a STRUCTURAL classification across Pillar II / III / IV. CF-29 audits the Type-F/Type-S partition cross-pillar and re-classifies three priority observables: (1) S70 LEGGETT-MOMENT (Pillar III, BdG superfluid analog); (2) Pillar III BCS condensate; (3) Pillar VI A_s/n_s (cosmological observables). Each is classified Type-F or Type-S based on a NCG-axiomatic operator-projection criterion: an observable is Type-F iff its expectation on the canonical state factorizes as a single-operator projection trace; Type-S iff it requires ≥2 mixed projections.

### Substrate framing

The substrate IS the operator-projection structure on (A_K, H_K, D_K). Type-F observables ARE single-projection trace cocycles; Type-S observables ARE mixed-projection trace cocycles. The pillar labels (II, III, IV, V, VI) are NOT containers — they ARE substrate-IS observables under distinct regulator-class restrictions. CF-29 re-classifies the three priority observables based on NCG-axiomatic operator-projection criteria, NOT based on pillar-label conventions.

### Threshold (PASS / FAIL / INFO)

- **PASS** = ALL FOUR of:
  1. Each of {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s} classified as Type-F or Type-S with explicit operator-projection-criterion justification;
  2. NCG-axiomatic verification of the Type-F/Type-S criterion: Type-F preserves the bimodule structure under projection; Type-S requires explicit mixed-projection trace decomposition;
  3. Cross-pillar consistency: re-classification result for each observable consistent with its pillar's regulator-class restriction (no contradictions between pillar-restricted classification and global operator-projection criterion);
  4. If any re-classification differs from prior pillar-label-based classification, surface the discrepancy explicitly in the working-paper §VII.W4-5 with framework-implication analysis.

- **FAIL** = ANY of:
  - Any of the 3 observables cannot be classified (operator-projection criterion ill-defined on the canonical cache);
  - NCG-axiomatic verification fails (Type-F observable's projection does not preserve bimodule structure);
  - Cross-pillar consistency violated (an observable classified Type-F at one pillar-restriction and Type-S at another).

- **INFO** = ALL three observables classified BUT one or more re-classification triggers a cross-cutting framework re-evaluation with deferred resolution to S88+ (specific cross-cutting issue identified).

**Tolerance rule**: THEOREM (axiom-level + classification-criterion verification at machine-eps for projection trace algebra).

### Machinery pin (PRDR)

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt

N_eval: 155984              # canonical L_max=10 D_K cache
L_max: 10                   # canonical
scan_range: 3 priority observables × {Pillar II, III, IV, V, VI} regulator-class restrictions
step_size: N/A
tolerance:
  axiom_verification: < 1e-12 (machine-eps for bimodule projection trace algebra)
  classification: Type-F / Type-S binary per observable; cross-pillar consistency strict (no contradiction allowed)
scheme: NCG-axiomatic operator-projection-criterion classification
convention: A_K = C ⊕ H ⊕ M_3(C); single-projection trace ⇒ Type-F; mixed-projection trace ⇒ Type-S
random_seed: N/A
GPU path: torch.linalg.eigh on AMD RX 9070 XT for projection trace computations on L_max=10 spectrum

publication_sig_figs: 12 (projection trace values; classification flags binary)
```

### Substitution chain

```
Step 1 (definitions):
  P_a               = projection onto irreducible component a of A_K bimodule
                      (a ∈ {C, H, M_3(C)} for A_K = C ⊕ H ⊕ M_3(C))
  Type-F observable O := single-projection trace: O = Tr(P_a O P_a) for some unique a
  Type-S observable O := mixed-projection trace: O = sum_{a≠b} Tr(P_a O P_b) (≥ 2 nontrivial cross-terms)
  S70 LEGGETT_MOMENT  = Pillar III analog of Leggett-mode momentum operator on BdG spectrum
  Pillar_III_BCS      = BCS condensate order parameter on Pillar III spectral triple
  Pillar_VI_As_ns     = cosmological observables A_s (scalar amplitude) + n_s (spectral index)

Step 2 (substitution):
  Classify(LEGGETT_MOMENT) = Type-F iff Tr(P_a LEGGETT_MOMENT P_a) ≠ 0 for unique a
                           = Type-S iff requires ≥ 2 cross-projections
  similarly for Pillar_III_BCS and Pillar_VI_As_ns
  cross_pillar_check(O): for each pillar p, restrict O to A_p and re-classify;
                        consistent iff classification-flag is pillar-invariant

Step 3 (simplification):
  PASS iff (3 classifications well-defined) AND (axiom-verification PASS) AND (cross-pillar consistency)
  INFO iff (3 classifications PASS but ≥ 1 re-classification triggers framework re-eval)
  FAIL iff (≥ 1 classification ill-defined) OR (axiom violation) OR (cross-pillar inconsistency)

Step 4 (direction):
  No direction; classification is data + structural diagnostic.

Step 5 (sign for [AUDIT] trigger):
  sign_verdict = N/A
  magnitude_verdict = PASS iff all 3 classifications + axiom + cross-pillar; FAIL iff any violated;
                      INFO iff cross-cutting reeval triggered
  regime_verdict = VALID iff projections well-defined on L_max=10 cache for all 3 observables
```

### Input SHA-256 pins

| File | Pin type | Provenance |
|:-----|:---------|:-----------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | runtime SHA | L_max=10 strict subset |
| `sessions/archive/session-86/session-86-w4-workingpaper.md` (Type-F partition § R3 closure) | content_sha256 | Type-F/Type-S partition criterion source |
| `sessions/archive/session-70/...` (S70 LEGGETT-MOMENT entry per `permanent-results-registry.md`) | content_sha256 | LEGGETT-MOMENT definition source |
| Pillar III BCS condensate definition (per `permanent-results-registry.md` BCS block) | content_sha256 | BCS observable source |
| Pillar VI A_s / n_s (per `canonical_constants.py` A_s_FW_eps_02163, A_s_FW_eps_020 + n_s_framework, plus pivot-keyed sub-entries) | content_sha256 | cosmological observable source |
| `computations/canonical_constants.py` | content_sha256 | A_K bimodule pin |
| CF-25 (CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF) verdict line — UPSTREAM if Level 1 PASS | runtime SHA | bridge-map availability for cross-pillar comparison |
| CF-26 (TYPE-F-PER-MODE-PHASE-AUDIT) verdict line — UPSTREAM | runtime SHA | Type-F 32-mode partition validation |

### Cross-wave dependencies

CF-29 depends on CF-25 (cross-pillar bridge) AND CF-26 (Type-F partition validation) for the audit substrate. If either upstream FAILs, CF-29 routes to PRE-REG-INC per `mechanical-closure-discipline.md` blocked on the failing upstream(s). If both PASS or INFO, CF-29 proceeds with the available substrate.

### Expected output 4-tuple

```
(value=cross_pillar_consistency_flag_PASS_FAIL_INFO, scheme=NCG-axiomatic-operator-projection-criterion, convention=A_K-tripartite-bimodule, L_max=10)
```

### Output artifacts

- **Script**: `computations/s87_w4_type_f_type_s_cross_pillar_audit.py`
- **Data**: `computations/s87_w4_type_f_type_s_cross_pillar_audit.npz` with classification flags + projection trace values + axiom-verification table + cross-pillar consistency matrix
- **Plot**: `computations/s87_w4_type_f_type_s_cross_pillar_audit.png` (3 observables × 5 pillar-restrictions classification heatmap)
- **Verdict line**: appended to `computations/s87_gate_verdicts.txt`
- **Working-paper section**: §VII.W4-5 "Type-F / Type-S Cross-Pillar Audit" with substantive content (≥15 lines; per-observable classification justification + axiom-verification table + cross-pillar consistency matrix + framework-implication analysis if any re-classification surfaces + substrate framing block)

### What PASS / FAIL / INFO means for the solution space

- **PASS** establishes the Type-F/Type-S partition as a STRUCTURAL classification axis across Pillar II/III/IV/V/VI, with NCG-axiomatic justification per observable. The 3 priority observables receive canonical classifications consumable by S88+ falsifier-design rows.
- **FAIL** localizes the Type-F/Type-S partition to Pillar V only (cross-pillar extension fails); each pillar-restricted observable must be classified independently per pillar.
- **INFO** records the 3 classifications BUT triggers a cross-cutting framework re-evaluation (e.g., S70 LEGGETT-MOMENT was prior labeled Type-S but the operator-projection criterion classifies it Type-F, which conflicts with downstream consumers); the specific cross-cutting issue is logged as S88+ carry-forward with explicit re-evaluation spec.

---

## §W4-6. S87-OPERATOR-PROJECTION-SEPARATION-RULE-PROMOTE (CF-30, Level 5, doc-only)

**Trigger**: `[AUDIT]`
**Classification**: NON-PHONONIC (rule-promotion decision; no substrate-physics derivation)
**Owner**: `gen-physicist` (rule-file decision dispatcher per `feedback_rules-compensate-missing-structure.md` discipline); `connes-ncg-theorist` co-signs as W-4 wave lead

### Hypothesis

The "operator-projection separation rule" — established at S86 W-4 R3 as the technical criterion distinguishing Type-F from Type-S observables (single-projection trace vs mixed-projection trace) — may rise to permanent epistemic-discipline.md status as a MANDATORY rule for substrate-observable classification. CF-30 decides whether the rule has accumulated sufficient calibration corpus instances (K=3 threshold per `feedback_rules-compensate-missing-structure.md`) to merit promotion, or whether it remains a workshop-design SUGGESTION with insufficient corpus.

### Substrate framing

The rule itself is METHODOLOGY-class (per `wave-classification.md` M1-M4 conjunction); CF-30 is doc-only with no substrate-physics derivation. However, the rule's CONTENT is substrate-first: the operator-projection criterion is defined on the spectral triple's bimodule structure; the rule's promotion would enforce that all future substrate-observable classification cite this criterion at plan-freeze. The decision is whether the corpus K supports this enforcement.

### Threshold (PASS / FAIL / INFO; pre-registered per `feedback_rules-compensate-missing-structure.md`)

- **PASS** = K ≥ 3 distinct calibration corpus instances of the operator-projection criterion identified in S86 + S87-W4 closure events. Specific instances enumerated:
  1. S86 W-4 R3 closure (Type-F/Type-S partition origin; Pillar V calibration);
  2. CF-29 (cross-pillar Type-F/Type-S audit — IF CF-29 closes PASS or INFO with the operator-projection criterion explicitly applied);
  3. ≥1 prior session's classification application (e.g., S70 LEGGETT-MOMENT classification, Pillar III BCS classification, etc., IF the prior classification can be re-derived under the operator-projection criterion).

  PASS outcome: rule lands as MANDATORY in `.claude/rules/epistemic-discipline.md` (or a new dedicated file if scope warrants); rule-file v3 changelog entry added; calibration corpus pinned.

- **FAIL** = K ≤ 1 (only the S86 W-4 R3 origin instance). NO rule promotion. Per `feedback_rules-compensate-missing-structure.md`, MANDATORY rules without ≥3 corpus instances are technical-debt-prone and MUST NOT be added.

- **INFO** = K = 2 (S86 W-4 R3 + ONE additional instance). The rule is recorded as a workshop-design SUGGESTION with the existing 2-instance corpus, and the promotion-decision is queued for S88+ when a third corpus instance accumulates.

**Tolerance rule**: ABSOLUTE (K is a discrete integer count; PASS iff K ≥ 3, FAIL iff K ≤ 1, INFO iff K = 2).

### Machinery pin (PRDR)

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt

N_eval: N/A (corpus-instance enumeration; not numerical)
L_max: N/A
scan_range: S82..S87 sessions; S87 W-4 closure; prior pillar-restricted classification events
step_size: N/A
tolerance:
  K = 3 PASS threshold (per `feedback_rules-compensate-missing-structure.md`)
  K = 2 INFO band (workshop-design SUGGESTION recorded; promotion deferred)
  K = 1 FAIL band (no promotion; technical debt prevented)
scheme: corpus-instance enumeration via grep + manual semantic verification
convention: per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold
random_seed: N/A
GPU path: N/A

publication_sig_figs: N/A (integer count)
```

### Substitution chain

```
Step 1 (definitions):
  K = count of distinct calibration corpus instances of "operator-projection separation criterion"
      identified in S82..S87 closure events
  PASS iff K ≥ 3 (rule-promotion calibrated)
  INFO iff K = 2 (workshop-design SUGGESTION)
  FAIL iff K ≤ 1 (technical debt prevention)

Step 2 (substitution):
  Instance 1: S86 W-4 R3 closure (Type-F/Type-S partition origin; Pillar V) — VERIFIED
  Instance 2: CF-29 outcome (cross-pillar Type-F/Type-S audit; depends on CF-29 PASS/INFO)
              — VERIFIED iff CF-29 closes PASS or INFO with criterion applied
  Instance 3: prior session re-derivation (S70 LEGGETT-MOMENT or Pillar III BCS or other)
              — VERIFIED iff a specific prior classification can be re-derived under the criterion

  K = count(Instance_1, Instance_2, Instance_3 ∈ {VERIFIED})

Step 3 (simplification):
  K is a discrete integer in {0, 1, 2, 3}.
  PASS iff K ≥ 3.

Step 4 (direction):
  No direction; ternary outcome based on K.

Step 5 (sign for [AUDIT] trigger):
  sign_verdict = N/A
  magnitude_verdict = PASS iff K ≥ 3; INFO iff K = 2; FAIL iff K ≤ 1
  regime_verdict = VALID (corpus enumeration within scope)
```

### Input SHA-256 pins

| File | Pin type | Provenance |
|:-----|:---------|:-----------|
| `sessions/archive/session-86/session-86-w4-workingpaper.md` (R3 closure block) | content_sha256 | Instance 1 source (S86 W-4 R3) |
| CF-29 verdict line (UPSTREAM in same wave) | runtime SHA | Instance 2 source (CF-29 PASS/INFO required for verification) |
| `sessions/archive/session-70/...` (S70 LEGGETT-MOMENT entry) | content_sha256 | Candidate Instance 3 source |
| `permanent-results-registry.md` (Pillar III BCS) | content_sha256 | Candidate Instance 3 source |
<!-- AMRI fix (2026-04-28): orchestrator-memory pin removed; K=3 threshold lives in the gate predicate itself, not pinned via meta-rule cite. -->
| `.claude/rules/epistemic-discipline.md` | content_sha256 | rule-promotion target file (only edited on PASS) |
| `.claude/rules/wave-classification.md` | content_sha256 | M4 allowlist gate (CF-30 is METHODOLOGY-class iff ALLOWLISTED) |
| `.claude/rules/methodology-wave-allowlist.md` | content_sha256 | allowlist target (CF-30 entry pre-allocated only if PASS) |

### Cross-wave dependency

CF-30 depends on CF-29 closure (Instance 2 verification source). If CF-29 closes FAIL, Instance 2 is unverified and K ≤ 2 deterministically (PASS impossible). If CF-29 closes PASS or INFO with the criterion applied, Instance 2 is verified and K depends on Instance 3. Because of this strict ordering, CF-30 is dispatched AFTER CF-29.

### Wave-classification (per `.claude/rules/wave-classification.md` M1-M4)

- **M1** (PASS predicate type): artifact-existence + corpus-count + (optional) rule-file edit predicate. PASS iff K ≥ 3 and (on PASS) rule-file diff lands. ✓ (artifact-existence-with-substantive-content; not a numerical comparison).
- **M2** (Producing-operation type): grep + integer count + Edit on `.claude/rules/epistemic-discipline.md`. ✓ (no `.py` script with numerical-threshold comparison; doc-only).
- **M3** (Source-of-truth): verbatim from S86 W-4 R3 closure + CF-29 outcome + prior session classification cite. ✓ (no first-principles new derivation).
- **M4** (Allowlist membership): CF-30 is a METHODOLOGY-class candidate; per `.claude/rules/methodology-wave-allowlist.md` discipline, the gate-ID `S87-OPERATOR-PROJECTION-SEPARATION-RULE-PROMOTE` MUST appear in the allowlist before classification as METHODOLOGY-class. **At plan-freeze, the orchestrator appends a new row** to the allowlist (pending SHA initially; finalized at plan-freeze SHA computation):
  ```
  | S87-OPERATOR-PROJECTION-SEPARATION-RULE-PROMOTE | S87 | CF-30; rule-promotion decision per K=3 corpus discipline | pending |
  ```
  This is the canonical orchestrator-direct edit per the recursion-attack-closure protocol.

### Expected output 4-tuple

```
(value=K_corpus_instance_count_in_{0,1,2,3}, scheme=corpus-instance-enumeration, convention=K=3-promotion-threshold-per-rules-compensate-missing-structure, L_max=N/A)
```

### Output artifacts

- **Script**: `computations/s87_w4_operator_projection_separation_rule_promote.py` (gen-physicist writes; corpus enumeration + grep + manual semantic verification + conditional rule-file edit)
- **Data**: `computations/s87_w4_operator_projection_separation_rule_promote.npz` with K count + Instance 1/2/3 verification flags + (on PASS) rule-file diff SHA
- **Plot**: N/A (corpus enumeration; no plot)
- **Verdict line**: appended to `computations/s87_gate_verdicts.txt`
- **Working-paper section**: §VII.W4-6 "Operator-Projection Separation Rule Promotion Decision" with substantive content (≥15 lines; corpus enumeration table + per-instance verification + decision outcome + (on PASS) rule-file diff + (on FAIL/INFO) carry-forward to S88 with explicit corpus-instance-3 source identification + substrate framing block)
- **Rule-file edit (only on PASS)**: append new section to `.claude/rules/epistemic-discipline.md` (or NEW file if scope warrants) with the operator-projection separation criterion as MANDATORY rule + 3-instance calibration corpus + provenance (S86 W-4 R3 + CF-29 + Instance 3)

### What PASS / FAIL / INFO means for the solution space

- **PASS** lands the operator-projection separation rule as MANDATORY in `.claude/rules/epistemic-discipline.md`. Future substrate-observable classification at plan-freeze MUST cite this rule. The S86 W-4 R3 closure becomes a permanent methodology anchor.
- **FAIL** prevents technical debt: a MANDATORY rule with ≤1 corpus instance is a Class-1 tech-debt-source per `feedback_rules-compensate-missing-structure.md`. The rule remains a workshop-design suggestion only; CF-30 records the prevention; S88+ carry-forward triggers re-evaluation when corpus accumulates.
- **INFO** records K=2; the workshop-design suggestion is logged with 2-instance corpus; the promotion is deferred to S88+ when Instance 3 accumulates. Specific carry-forward spec: identify candidate Instance 3 sources and queue an explicit verification gate.

---

## Wave 4 → Wave 5 Decision Point

After Wave 4 closure, the W4 → W5 decision rule is:

| W4 Outcome | W5 Implication |
|:-----------|:----------------|
| CF-25 PASS + CF-26 PASS + CF-29 PASS | W5 dispatches CF-31..CF-35 (W-5 Pillar III↔IV bridge follow-ups) with cross-pillar bridge anatomy template informed by CF-25 3-channel × 3-pillar tensor extension. CF-30 PASS lands rule promotion; W5 plan-freeze validators cite the new rule. |
| CF-25 INFO (2-channel partial) | CF-25 records STAGE-1-CANDIDATE; CF-29 proceeds with available 2-channel substrate; CF-30 K=2 INFO most likely (Instance 2 partial). W5 dispatches with Stage-1-candidate flag on cross-pillar references. |
| CF-25 FAIL | CF-29 routes to PRE-REG-INC blocked on CF-25; CF-30 K ≤ 2 deterministically (Instance 2 unverified); W5 plan-freeze re-evaluates cross-pillar 3-channel decomposition substrate; potential workshop dispatch to recover Channel-1/2/3 partition correctness before W5 dispatch. |
| CF-26 FAIL | High-impact framework event (S38 algebraic GGE-permanence falsified OR Type-F partition not well-defined on canonical cache). W5 dispatch DEFERRED until S88; orchestrator escalates to user adjudication. |
| CF-27 FAIL OR CF-28 FAIL | Mechanical surgery defect; pre-W4 state preserved; carry-forward to S88 with specific defect spec; W5 proceeds with pre-W4 inventory state. |
| CF-30 PASS | New MANDATORY rule lands in `.claude/rules/epistemic-discipline.md`; W5 plan-freeze validators cite; methodology-wave-allowlist.md row finalized with computed SHA. |

---

## Wave 4 Machinery-Enumeration Pin (§0.11 PRDR)

Per `epistemic-discipline.md` §"Pre-Registration Completeness" PRDR (Pre-Registration Dry-Run): every gate-relevant machinery parameter is enumerated in the per-gate Machinery pin (PRDR) blocks above. Cross-wave aggregated enumeration:

| Parameter | CF-25 | CF-26 | CF-27 | CF-28 | CF-29 | CF-30 |
|:----------|:------|:------|:------|:------|:------|:------|
| `N_eval` | 155984 | 155984 | N/A | N/A | 155984 | N/A |
| `L_max` | 10 | 10 | N/A | N/A | 10 | N/A |
| `scan_range` | tau=tau_fold | 4-pt tau scan | line range | inventory rows + cross-refs | 3 obs × 5 pillar | corpus enumeration |
| `tolerance` | THEOREM + RATIO | ABSOLUTE + RATIO | ABSOLUTE | ABSOLUTE | THEOREM | ABSOLUTE (K integer) |
| `scheme` | 3-channel × 3-pillar Connes-Karoubi | Bogoliubov-phase Type-F | text-replacement | registry-row split | NCG-projection criterion | corpus-enumeration |
| `convention` | substrate-distance Mellin-cone | post-tau_fold S38 GGE | phononic-framing reframe | 5-element IS-not-IN per row | A_K tripartite bimodule | K=3 per feedback rule |
| `random_seed` | N/A | N/A | N/A | N/A | N/A | N/A |
| `GPU path` | torch.linalg.eigh (cross-check) | torch.linalg.eigh | N/A | N/A | torch.linalg.eigh | N/A |
| `publication_sig_figs` | 15 (Sage QQ) | 12 | N/A | N/A | 12 | N/A (integer) |

All gates use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` per `math-scripts.md` §Environment.

PRU cardinality pre-flight per `_pru_cardinality_audit.py`: each row of the table above is 1 pin per gate; D_PRU_raw = 0 expected for all gates at plan-freeze.

---

## Wave 4 Input-SHA Ledger

Aggregated input-SHA pins across all 6 gates (deduplicated):

| File | Pin type | Consumer gates |
|:-----|:---------|:---------------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | runtime SHA-256 | CF-25, CF-26, CF-29 |
| `computations/canonical_constants.py` | content_sha256 | CF-25, CF-26, CF-27, CF-29 |
| `computations/canonical_classes.py` | content_sha256 | CF-26 (EXFLATION_CLASS cross-class consistency) |
| `computations/s52_bogoliubov_amp.npz` | runtime SHA-256 | CF-26 (cross-check baseline) |
| `sessions/permanent-results-registry.md` | content_sha256 | CF-25 (§VII.W S86 W-5 anchor), CF-26 (S38 GGE-permanence block), CF-28 (cross-reference scan), CF-29 (BCS block), CF-30 (Pillar III BCS Instance-3 candidate) |
| `sessions/archive/session-86/session-86-w4-workingpaper.md` | content_sha256 | CF-25 (Type-F partition), CF-26 (32-mode source), CF-27 (locked replacement text source), CF-29 (Type-F/Type-S criterion source), CF-30 (Instance 1 source) |
| `sessions/archive/session-86/session-86-w14-workingpaper.md` | content_sha256 | CF-27 (W14-4 §line 414-422 surgery target) |
| `sessions/framework/registry/falsifier-master-inventory.md` | content_sha256 | CF-27 (framing-column update target), CF-28 (Row #9 split target) |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | content_sha256 | CF-25 (mandatory anatomy), CF-28 (5-anatomy per row) |
| `.claude/rules/joint-theorem-promotion.md` | content_sha256 | CF-25 (4-stage pathway) |
| `.claude/rules/phononic-framing.md` | content_sha256 | CF-27 (substrate-IS-vs-laboratory-IN reframe) |
| `.claude/rules/epistemic-discipline.md` | content_sha256 | CF-30 (rule-promotion target) |
| `.claude/rules/wave-classification.md` | content_sha256 | CF-30 (M1-M4 classification) |
| `.claude/rules/methodology-wave-allowlist.md` | content_sha256 | CF-30 (allowlist append) |
<!--
  AMRI fix (2026-04-28): two rows removed from the aggregated input-SHA ledger.
  - orchestrator-memory pin (K=3 threshold source) removed; the K=3 threshold is
    operationalized in CF-30's gate predicate, not via meta-rule cite.
  - Wildcard `agent-memory/*/MEMORY.md` content_sha256 pin removed; CF-28 performs a
    runtime cross-reference walk over agent memories — that is a runtime READ operation,
    not an Input-SHA pin commitment. Scanning ≠ pinning. Per `.claude/rules/agent-standards.md`
    §AMRI, agent memory cannot be a project-level pin source even via wildcard.
-->
| Per-gate upstream verdict-line runtime SHAs | runtime SHA | CF-28 (depends on CF-25), CF-29 (depends on CF-25 + CF-26), CF-30 (depends on CF-29) |

Per `gate-verdicts.md` §Pre-Registration Protocol: every script logs the SHA-256 of every input in the first 20 lines of stdout AND emits the closure hash. Dual-SHA companion comment row + S87+ schema-v2 3-tuple annotation (sign_verdict, magnitude_verdict, regime_verdict) appended per the `gate-verdicts.md` extended schema.

---

## Wave 4 Dispatch Order

Sequential per upstream-dependency topology:

1. **CF-25** (no W4 prereqs; depends on S86 W-5 §VII.W + cross-pillar bridge anatomy rule).
2. **CF-26** (no W4 prereqs; depends on S86 W-4 R3 Type-F partition + S38 GGE-permanence).
3. **CF-27** (no W4 prereqs; mechanical text replacement; can run in parallel with CF-25 / CF-26).
4. **CF-28** (depends on CF-25 PASS or INFO with Channel-1; mechanical inventory split).
5. **CF-29** (depends on CF-25 + CF-26).
6. **CF-30** (depends on CF-29).

Parallelism: CF-25 + CF-26 + CF-27 dispatched in parallel (no inter-dependency); CF-28 follows CF-25; CF-29 follows CF-25 + CF-26; CF-30 follows CF-29. Per `feedback_dispatch-discipline.md`, total concurrent ≤ 8 at any time. Wave-4 max concurrency = 3 (CF-25 + CF-26 + CF-27 batch); subsequent batches singletons or pairs.

Per `feedback_dispatch-discipline.md` (workshop discipline does not apply here — this is compute-mode, not workshop-mode) and `feedback_dispatch-discipline.md`, in compute mode no permission-pause between batches/waves; the wave executes through to closure.

---

**End of Wave 4 plan.**
