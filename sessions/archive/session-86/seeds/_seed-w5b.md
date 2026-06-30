# Seed file — sessions/archive/session-86/session-86-w5b-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w5b-workingpaper.md` (467 lines)

## Candidates

### Candidate 1 — eps_H pin reconciliation (S80 dS/dτ-fold vs S85 W1a-1 SR-LO baseline)

**What it would do**: Adjudicate the canonical SR-LO ε_H pin between the two coexisting pinned values: `eps_H_W6 = 0.02163` (S80, derived from dS/dτ-fold pin in `canonical_constants.py` L1318) and `eps_H_canon = 0.020` (S85 W1a-1, the in-script baseline anchor used by W5a P3 SECTOR-1 and C15(ii)). Establish whether (i) one is structurally derived and the other is a derived/legacy form (and which), (ii) the 8.15% offset has physical content (i.e., they encode different substrate observables that happen to play the same role in the SR-LO ODE), or (iii) the disparity is a documentation defect that should collapse to one canonical pin with provenance-superseding-flag on the other. Produce a substitution chain showing how the dS/dτ-fold derivation gives 0.02163 and how the S85 W1a-1 baseline gives 0.020, and identify the structural difference.

**Why it's worthwhile**: Cross-gate observation flagged in W5b synthesis (lines 407-421): C15(i) substituted 0.02163 in its substitution chain Step 2; C15(ii) substituted 0.020 in its substitution chain Step 1. The 8.15% offset (verified via Python in WP synthesis: `|0.02163 - 0.020|/0.020 = 0.0815`) is structurally significant for downstream SECTOR-1 consumers because A_s ∝ (H/Z)² propagates ε_H through `H(N) = H_initial · exp(-∫ ε_H dN)` — an 8% offset in ε_H over N=55 e-folds amplifies to `exp(0.0815·1.10) = 1.094` in H, ~9% in H². This compounds with the 0.487-OOM substrate-zeta vs MS bookkeeping ratio (C15(i) Step 3) into a non-trivial calibration disagreement that the late-S86 falsifier registry will inherit. The C15(ii) agent already wrote this as a 4-field carry-forward (S87-W2-EPS-H-PIN-RECONCILIATION); a workshop sharpens the structural question.

**Type**: 2-agent workshop

**Suggested agents**: connes-ncg-theorist (axiom-side: dS/dτ-fold derivation as Mellin-zeta moment of D_K), spectral-action-theorist (alternative: lizzi-spectral-functional-theorist for spectral-action-side adjudication if connes is busy)

**Rounds**: 2 default — R1 each agent steelmans one pin's structural origin (connes argues 0.02163 = dS/dτ-fold spectral moment; lizzi/alternative argues 0.020 = SR-LO baseline anchor with separate provenance); R2 converge on whether they encode the same observable or different ones.

**Context the workshop will need**:
- C15(i) Step 2 substitution chain (uses 0.02163), §W5b-1.i lines 53-77
- C15(ii) Step 1 substitution chain (uses 0.020), §W5b-1.ii lines 175-212
- `canonical_constants.py` L1318 (eps_H_W6 = 0.02163) provenance pin
- W5a P3 in-script anchor `EPS_0` line 90 (cited as "S85 W1a-1 baseline anchor")
- S80 dS/dτ-fold derivation source (cite by line in canonical_constants.py)
- S85 W1a-1 baseline-anchor derivation source
- Adjudication rule: ONE canonical eps_H pin must emerge with substitution chain; the other gets superseded-flag with explicit provenance reason

---

### Candidate 2 — Pivot canonical commit (substrate-zeta N=3.12 vs MS N=55) post-S86

**What it would do**: The W-2 axiom-trace methodology workshop already pre-registered as `S87-W2-PIVOT-CANONICAL-COMMIT` (W5b synthesis line 441). C15(i) rejected (a) AXIOM-NATIVE because substrate-zeta N=3.12 flips to ~2.0 at c_s=0.485 (S77 transit-einstein-workshop L976, convention-sensitive, not an axiom-native invariant) and (b) OBSERVATION-NATIVE because the canonical `N_pivot = 64.08 = 55 + ln(c/c_s)` is already a HYBRID (S83 W1-G5). The PRE-REG-BOTH selection is structurally legitimate but DEFERRED — both pivots flow downstream as Path-H-substrate-zeta and Path-H-MS through S86 close. The workshop should produce ONE selection rule with pre-registered substitution chain pinning canonical pivot for S87+ falsifier registry. Includes deciding whether the 0.487-OOM substrate-zeta vs MS bookkeeping ratio (matching S82 W1-1 0.517-OOM cascade within rounding) is a structural feature of the framework or a mere convention disparity.

**Why it's worthwhile**: This is the structural canonical question downstream falsifier registry depends on. Three independent pivots float in the framework: substrate-zeta N=3.12 (S77), MS N=55 (S82, Mukhanov-Sasaki gauge-invariant), and the canonical hybrid N_pivot=64.08 (S83). Each anchors a different observational comparison. The C15(i) PASS validates the dual-column reporting architecture but DEFERS the canonical commit. The cross-pillar pattern is sharp: substrate-zeta is a Pillar III (NCG/spectral-action) Mellin-cone evaluation, MS is a Pillar I (acoustic gravity / cosmological perturbation theory) horizon-exit count. A canonical commit that does not fall on either pillar (i.e., the hybrid 64.08) is a structural admission that the framework's observational predictions live at a pillar-junction. Worth probing whether this is a feature (cross-pillar fluency) or a sign of incomplete derivation.

**Type**: 2-agent workshop

**Suggested agents**: connes-ncg-theorist (axiom-side, NCG Mellin-cone), mukhanov-sasaki / gauge-invariant cosmologist analog (sagan-empiricist as second-best — empirical MS pivot side)

**Rounds**: 3 (genuine ledger-dissonance: R1 steelman each pivot, R2 respond, R3 converge with substitution chain pinning canonical for S87+ falsifier registry)

**Context the workshop will need**:
- C15(i) selection-rule justification §W5b-1.i lines 80-93 (rejection of (a) and (b), selection of (c))
- S77 `session-77-transit-synthesis.md` L103 (substrate-zeta = 3.12)
- S77 `transit-einstein-workshop.md` L976 (c_s sensitivity 3.12 → ~2.0)
- S82 `s82-w1-1-divergence-chase.md` L52-77 (MS = 55 derivation; cascade decomposition Step 2 Piece 1: `log₁₀(exp(ε_H · 55)) = 0.517 OOM`)
- S83 `S83-N-PIVOT-CS-CANONICALIZATION` (canonical hybrid 64.08)
- C15(i) Step 3 ratio derivation (0.487 OOM consistency check vs S82's 0.517 within rounding)
- W5a P3 SECTOR-1 dual-column architecture
- Late-S86 falsifier registry (Path-H-substrate-zeta + Path-H-MS slots)
- Adjudication rule: ONE canonical pivot must be selected with structural derivation, OR a defensible structural reason for retaining dual-pivot reporting must be written into the falsifier-registry charter (i.e., a positive structural argument for cross-pillar reporting, not just "both are needed")

---

### Candidate 3 — Axiom-side cross-review of C16 sub-test (c) sign-reversal predicate

**What it would do**: Already pre-registered as `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` (W5b synthesis line 443) and explicitly flagged by the C16 agent (lizzi) and the orchestrator (line 427-429: "Three options for the user: (a) auto-dispatch the cross-reviewer in this session..."). The lizzi agent's τ-flow-trace proxy `c_sub_anomaly(τ) := d c_sub(τ)/dτ` gave both pre-fold and post-fold slopes NEGATIVE (sign(pre)=sign(post)=-1, no sign-flip), forcing C16 to INFO. The connes-ncg-theorist cross-review would propose an alternative axiom-side proxy that separates the conformal-anomaly contribution (a_4 anomaly term) from the dominant smooth Jensen-flow background (a_0 + a_2 + smooth a_4 reconstruction). If the alternative proxy isolates the post-fold sheet flip, sub-test (c) flips PASS, composite goes INFO → ADMISSIBLE, Path-C r=0.0117 promotes to unconditional admissible.

**Why it's worthwhile**: This is the most actionable structural question in the WP. C16 sub-test (c) FAILed by 100% on the proxy chosen, but the proxy itself is operational, not axiomatic — the lizzi agent explicitly flagged in §W5b-2 (line 344) that the proxy "operationalizes the conformal-anomaly contribution as the τ-flow trace, which is the simplest substrate-framing reading. An axiom-side adjudication ... could in principle propose an alternative operational proxy." The path forward is concrete: apply the spectral-action a_n decomposition (a_0, a_2, a_4 separately) and isolate the a_4 anomaly term from the smooth a_0+a_2 background; the τ-derivative of just the a_4-anomaly piece is the canonical sign-reversal observable per S79 P1-2 W2-E. The structural question has a definite resolution under the alternative proxy. Path-C admissibility at LiteBIRD/BK-Array scale (r=0.0117 vs Path-H r=0.00745, a 36.5% split) directly depends on this.

**Type**: solo (1 agent) — cross-review by connes-ncg-theorist on the existing C16 data + an axiom-side proxy implementation. (Could alternatively be 2-agent workshop with lizzi as discussant; given connes is the natural axiom-side adjudicator and lizzi has already published her position, a solo connes review is the cleaner first move; if FAIL persists under axiom-side, escalate to a 2-agent workshop.)

**Suggested agents**: connes-ncg-theorist

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**:
- C16 §W5b-2 full section (sub-test (a)/(b)/(c) substitution chains, lines 275-345)
- `computations/s86_w5b_c16_csub_admissibility.npz` (τ-grid, c_sub(τ) full trajectory, endpoint pre/post-fold slopes, anomaly contributions)
- S79 P1-2 W2-E sign-reversal rule structural derivation in `sessions/archive/session-79/workshops/p1-2-wave2-closure.md` (Q2/Q4 zeta-scheme excess, four-factor-ledger sign-flip under UNIFIED-AS-79)
- `sessions/archive/session-85/workshops/session-85-s1-regulator-boundary-connes.md` (canonical 5-regulator atlas R_atlas, line 12)
- Spectral-action a_n decomposition machinery (a_0, a_2, a_4 separation per Seeley-DeWitt)
- Pre-registered re-classification rule: if alternative axiom-side proxy gives sign(pre)·sign(post) < 0, sub-test (c) flips to PASS, composite goes INFO → ADMISSIBLE; if same-sign persists, INFO is canonical; the axiom-side proxy MUST be pinned BEFORE the c_sub(τ) trajectory data is examined under it, to avoid iterate-until-PASS

---

### Candidate 4 — W5a P3-bis under strict (η₀, α_s_0, ξ²₀) → 0 IC limit

**What it would do**: Already registered as carry-forward `S87-W5A-P3-BIS-STRICT-LIMIT` (W5b synthesis line 444). C15(ii) CC2 found a 49-58% gap between BASELINE H(N_pivot) and W5a P3's LCDM trajectory at both pivots (substrate-zeta: 49% lower; MS: 58% lower with truncation). The gap is driven by W5a P3's η₀ = 0.005 ≠ 0 IC, NOT by α_s or ξ² (which are already 0 in the LCDM IC). Re-running W5a P3 under strict η₀ = 0 (alongside α_s_0 = 0 and ξ²_0 = 0) would close the BASELINE reduction gap to within rtol pin (machine ε), confirming that W5a P3's coupled SR-flow ODE reduces correctly to the SR-LO BASELINE in the strict reduction limit. This is a structural identity check — the SR-flow ODE `dε/dN = ε(2η - 4ε + 2ξ²)` with η=0 and ξ²=0 reduces to `dε/dN = -4ε²`, NOT the constant-ε SR-LO assumed by the BASELINE. So the strict η₀=0 limit STILL won't perfectly reduce to BASELINE — it reduces to a different ODE (`dε/dN = -4ε²`) with non-trivial integration. The actual reduction is W5a P3 with η, α_s, ξ² all set to 0 from N=0 onward AND the SR-flow η-driving term forcing them to stay 0. That is not just an IC change but an ODE structure check.

**Why it's worthwhile**: The BASELINE-to-W5aP3 reduction test is the kind of structural identity check that constrains the framework's ODE machinery. The 49-58% gap is large enough to be physical (η-driven running) and not numerical noise; but understanding whether it ALL traces to η₀=0.005 or also to α_s/ξ² couplings deserves pinning. If the strict-limit run STILL deviates from BASELINE by more than the η₀ contribution alone, it reveals additional running terms in W5a P3's ODE that the BASELINE reduction expectation missed. This is a genuine constraint-map gain: closing the gap confirms ODE correctness; a residual gap reveals new running structure. Note: this is mostly already pre-registered as a 4-field carry-forward; promoting it to workshop scope is only worthwhile if the structural ODE-reduction question (`dε/dN = -4ε²` ≠ constant-ε) is judged to need workshop-level treatment.

**Type**: solo (1 agent) — straightforward script reuse with IC swap, NOT workshop-scope.

**Suggested agents**: transit-dynamics-theorist (same agent as C15(ii))

**Rounds (workshops only)**: N/A (solo).

**Context the workshop will need**:
- C15(ii) CC2 derivation §W5b-1.ii lines 159-170 (49-58% gap)
- W5a P3 .npz: `s86_w5a_p3_sector_1_z_factor.npz` (LCDM eps trajectory)
- W5a P3 plan §6 method (SR-flow coupled ODE definition)
- C15(ii) BASELINE .npz: `s86_w5b_c15_ii_baseline.npz`
- Pre-registered band: ±5% match between W5a P3-bis(η₀=0, α_s_0=0, ξ²_0=0) and C15(ii) BASELINE H(N_pivot)
- Structural sub-question: if `dε/dN = -4ε²` is integrated from N=0 with ε(0)=0.020, what is H(N=55) under this strict-IC run? Compare to BASELINE 3.0042 and to W5a P3 LCDM 1.5222 — does the strict run land closer to BASELINE or stay closer to LCDM? This is the structural test, not just CC2 closure.

---

### Candidate 5 — Cross-session consistency theorem: 0.487 OOM ≈ 0.517 OOM

**What it would do**: C15(i) Step 3 derived `Ratio = exp(ε_H_W6 · ΔN) = exp(51.88 · 0.02163) = 3.0715`, equivalent to `log₁₀(3.0715) = 0.487 OOM` of bookkeeping cascade between substrate-zeta N=3.12 and MS N=55 pivots. S82 W1-1 divergence-chase Step 2 Piece 1 independently derived `log₁₀(exp(ε_H · N_pivot)) = 0.517 OOM` at N_pivot=55 cascade contribution. The W5b synthesis (lines 425, 458) flagged the agreement within rounding as a "non-trivial cross-session consistency check." A structural review would (i) derive both forms with full substitution chains, (ii) identify the source of the rounding gap (is it ΔN=51.88 vs N=55, or eps_H_W6=0.02163 vs eps_H_canon=0.020, or both?), (iii) write the consistency relation as a permanent registry theorem in `sessions/permanent-results-registry.md`, OR (iv) flag the discrepancy if it does not in fact close to machine ε.

**Why it's worthwhile**: This is a structural bridge between two independently-derived results (S82 cascade decomposition, S86 C15(i) bookkeeping ratio). The framework's consistency at the OOM level depends on results derived in different sessions converging on the same numerical value. The 0.487 vs 0.517 gap (Δ = 0.030 OOM, ~7%) could come from: (a) ΔN=51.88 vs N=55, since `log₁₀(exp(eps_H · ΔN)) ≠ log₁₀(exp(eps_H · N))` when ΔN ≠ N. Substitution chain verification: `log₁₀(exp(0.02163·51.88)) = 0.4872`, `log₁₀(exp(0.02163·55)) = 0.5165`, gap = 0.0293 OOM, matches the observed 0.030. SO the discrepancy is NOT a bug — it traces to ΔN vs N pivot-difference. This means the registry theorem should be: "C15(i) ratio at ΔN=51.88 = S82 cascade contribution at N=55, scaled by the (ΔN/N) factor in the exponent." Worth pinning explicitly to lock the cross-session consistency as a permanent result. Could promote eps_H pin reconciliation (Candidate 1) by showing that BOTH pins give consistent OOM-level cascades when paired with their pivot conventions.

**Type**: solo (1 agent), brief structural-review.

**Suggested agents**: phonon-first-cosmologist (cross-pillar structural review, my native mode) OR connes-ncg-theorist (axiom-side derivation)

**Rounds (workshops only)**: N/A (solo).

**Context the workshop will need**:
- C15(i) Step 3 derivation §W5b-1.i lines 62-78 (Ratio = 3.0715, log₁₀ = 0.487)
- S82 `s82-w1-1-divergence-chase.md` Step 2 Piece 1 (log₁₀(exp(eps_H · 55)) = 0.517)
- Both eps_H pins (0.02163 and 0.020) and substitution chain showing ΔN vs N origin of the ~0.030 OOM gap
- Pre-registered: write the registry-level theorem in `sessions/permanent-results-registry.md` IF the gap closes structurally; flag for workshop review if it does NOT close (i.e., if the ~0.030 gap is NOT explained by ΔN=51.88 vs N=55).

