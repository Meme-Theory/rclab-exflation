# Session 87 Plan — Wave 10: Bulletin Rescue + ρ_∞ Wall

**Wave owner**: `connes-ncg-theorist` (lead) + `lizzi-spectral-functional-theorist` (co-sign on CF-61 Mellin-anchor side + CF-63 lizzi-observable promotion authority)
**Source carry-forwards**: CF-61, CF-62, CF-63, CF-64 (per `sessions/session-plan/session-87-context.md` §2.1 lines 158–161)
**Plan-freeze date**: 2026-04-27
**Verdict file**: `computations/s87_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`)
**Schema version**: `R3` (all four gate blocks)

---

## Wave 10 Summary

| # | Gate ID | Specialist | Trigger | Effort | Conditional? |
|:--|:--------|:-----------|:--------|:-------|:------------|
| §W10-1 | `S87-BULLETIN-#3-RESCUE-RESIDUAL` | connes-ncg-theorist (lead) + lizzi-spectral-functional-theorist (co-sign) | `[VERIFY]` | MEDIUM (~2.5 waves) | No |
| §W10-2 | `S87-BULLETIN-#4-IRRATIONAL-RHO-PERMANENT-WALL-LANDING` | connes-ncg-theorist | `[AUDIT]` | LOW-MEDIUM (~2 waves) | No |
| §W10-3 | `S87-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION` | lizzi-spectral-functional-theorist (lead) + connes-ncg-theorist (co-sign) | `[VERIFY-THEOREM]` | LOW (~half-wave) | **Yes** — CONDITIONAL on §W10-1 PASS-or-PASS-with-residual |
| §W10-4 | `S87-STRICT-LAMBDA-RATIO-EXTRACTION` | connes-ncg-theorist | `[VERIFY]` | LOW (~half-wave) | No |

**Wave-class** (per `.claude/rules/wave-classification.md` 4-test M1-M4):

| Gate | M1 (predicate) | M2 (op) | M3 (source) | M4 (allowlist) | Class |
|:--|:--|:--|:--|:--|:--|
| §W10-1 | numerical (ρ-fit residual band) | `.py` audit | new derivation (L1↔L2 cascade audit) | N/A | **COMPUTE** |
| §W10-2 | numerical (ρ_∞ Sage-exact match) AND artifact-existence (registry sub-row) | `.py` + Edit | verbatim from CF-62 source classification | N/A | **MIXED** → sub-decompose at execution: §W10-2a numerical + §W10-2b registry-write per `wave-classification.md` NROY clause; sub-decomposition deferred to executing agent at runtime per S86 W0a-2 precedent (single-gate-block authorized per CF-62 brief "4-level registry-mechanic schema implementation") |
| §W10-3 | numerical (s_eff threshold) | `.py` | verbatim from S86 W-10 workshop s_eff = 11/2 candidate | N/A | **COMPUTE** |
| §W10-4 | numerical (bit-exact ratio extraction) | `.py` | new extraction from existing cache | N/A | **COMPUTE** |

W10-1, W10-3, W10-4 dispatch via `/rclab-coordinate` compute-mode; W10-2 dispatched as single-block COMPUTE-class gate with executing agent authorized to perform the in-script registry-write (per `.claude/rules/mechanical-closure-discipline.md` §"Working-paper update is in-script" precedent — registry-write is the same disciplined in-script update pattern).

---

## Wave 10 Decision Point Prerequisites

Before any §W10 gate dispatches:

1. **Verdict-file collision check**: `grep -c "^S87-BULLETIN-#3-RESCUE-RESIDUAL" computations/s86_gate_verdicts.txt` MUST return 0 (no S87 gate IDs pre-existing in S86 verdict file). Same check for the four §W10 gate IDs.
2. **Spectrum cache verification**: `computations/s84_spectrum_cache_L12_tau019.npz` MUST exist on disk and its content_sha256 matches the pin in §"Wave 10 Input-SHA Ledger" below. CF-64 hard-fails at plan-freeze if absent.
3. **Bulletin source**: `sessions/framework/registry/elimination-bulletins.md` MUST contain Bulletin #3 (registry-flag grade) and Bulletin #4 (PERMANENT-WALL ρ_∞ ≈ −0.8104 L2-IRRATIONAL FERMIONIC-SIGNED-RESIDUE substrate constant) per S86 W-10 closure (memory ref `s86-cm1995-kernel-normalization-r2b.md`).
4. **§VII.K-PROP existence**: `sessions/permanent-results-registry.md` MUST contain §VII.K-PROP parent header (S86 W1a-1 17-row landing per context.md §1.1 line 62). Sub-row §VII.K-PROP.W10-4 is pre-allocated per the registry summary table (context.md §"§VII.K-PROP-W10-4 already in summary table").
5. **Source-recon pre-flight**: `python computations/_source_reconciliation_audit.py sessions/session-plan/session-87-plan-w10.md` MUST emit no `D_max ≥ 1.0` advisory on the four §W10 gate blocks. Pin values flagged at `0.1 ≤ D_max < 1.0` are advisory-only.
6. **PRU cardinality pre-flight**: `python computations/_pru_cardinality_audit.py sessions/session-plan/session-87-plan-w10.md` MUST return D_PRU_raw = 0 across all four gates.
7. **YAML schema_version validation**: `python computations/_yaml_gate_validator.py sessions/session-plan/session-87-plan-w10.md` MUST PASS with `schema_version: R3` on all four gate blocks.
8. **CF-63 conditional-trigger predicate**: §W10-3 dispatch is GATED on §W10-1 verdict. If §W10-1 verdict is FAIL, §W10-3 routes to mechanical closure per `.claude/rules/mechanical-closure-discipline.md` (verdict line emitted as `FAIL -- value='PRE-REG-INC_blocked_by_S87-BULLETIN-#3-RESCUE-RESIDUAL_FAIL'` with deferral to S88+).

---

## §W10-1. Bulletin #3 Rescue Residual (L1↔L2 audit + s_eff = 11/2 + NROY-cascade)

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

**Gate ID**: `S87-BULLETIN-#3-RESCUE-RESIDUAL`
**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (NCG-axiomatic substrate audit on derivation chain; not directly phononic, but constrains substrate-spectral derivation provenance)
**Specialist**: `connes-ncg-theorist` (lead) + `lizzi-spectral-functional-theorist` (co-sign Mellin-anchor side per CF-61 source attribution `connes+lizzi`)
**Source**: CF-61 (`sessions/archive/session-86/compute-carryforward.md` line W-10 CF-1; brief "L1↔L2 audit of S52-S77 derivation chain for F_amp/c_sub/f_conv; folds in s_eff = 11/2 + NROY-cascade audit")

### Hypothesis

Bulletin #3 closure at S86 W-10 R2-B emitted PASS-B at `c_sub = 3.5169` with `r = 11/7 = 1.5714`, `r/Γ(3) = 11/14 = 0.7857` (registry-flag grade per FROZEN-DISCIPLINE per memory `s86-cm1995-kernel-normalization-r2b.md`). The S52-S77 derivation chain for the F_amp / c_sub / f_conv triple was assembled across multiple sessions under heterogeneous regulator conventions (L1 Zubarev / L2 zeta-regulated / per-Q span). The hypothesis under test: **the residual rescue at PASS-B is structurally L1↔L2-axis-decomposable per the Three-Layer Regulator Theorem (`s84-w2a-11-vii-m-landing.md` §VII.M)**, AND **the s_eff = 11/2 candidate from S86 W-10 workshop emerges as the canonical exponent under L2 axis after L1↔L2 axis-decomposition**, AND **the NROY-cascade audit (W-13 RULE-1 NROY clause precedent) confirms the M_meta classification (a) registry-flag grade is invariant under L1↔L2 axis substitution**.

### Pre-registered substitution chain (sign/direction)

```
Step 1: F_amp(L) = (substrate-distance-1 Mellin moment of D_K^2)        [definition, S62 anchor]
Step 2: c_sub(L) = M_Pl_eff(k_pivot)^2 / M_Pl_eff(0)^2                   [definition, S77 anchor]
Step 3: f_conv(L) = ratio of L1 spectral-moment trace to L2 zeta-regularized
                    spectral-moment trace at fixed L_max                  [definition, S52-S77 chain]
Step 4: r_L1L2(L) := f_conv(L) under L1 / f_conv(L) under L2              [substitute Step 1+2+3]
Step 5: s_eff(r_L1L2) defined via Mellin-pole locus                       [W-10 workshop candidate]
Step 6: PASS iff |s_eff − 11/2| ≤ pass_band AND |r_L1L2 − r_anchor| ≤ rescue_residual_band
                                                                          [direction from canonical form]
```

**Direction claim**: at PASS-B (c_sub = 3.5169), the L1↔L2 rescue residual `r_L1L2` evaluated at L_max ∈ {10, 11, 12} converges to r_anchor = 11/7 monotonically with `r_L1L2(L=12) − r_anchor < r_L1L2(L=10) − r_anchor`. Sign predicted by Three-Layer Regulator Theorem (L1 → L2 axis is a regularization-strengthening direction per `regulator-pin-discipline.md` Pauli-Villars vs zeta hierarchy).

### Threshold

- **PASS**: `|r_L1L2(L=12) − 11/7| ≤ 1e-3` (RATIO tolerance) AND `|s_eff − 11/2| ≤ 5e-3` (RATIO tolerance) AND NROY-cascade audit returns no inconsistency in M_meta classification (a) under L1↔L2 axis substitution
- **PASS-WITH-RESIDUAL**: `1e-3 < |r_L1L2(L=12) − 11/7| ≤ 1e-2` OR `5e-3 < |s_eff − 11/2| ≤ 5e-2` AND NROY-cascade clean
- **INFO**: NROY-cascade audit returns at most ONE inconsistency that is regulator-class-localized (per W-13 NROY clause "regulator-axis-decomposable")
- **FAIL**: `|r_L1L2(L=12) − 11/7| > 1e-2` OR `|s_eff − 11/2| > 5e-2` OR NROY-cascade returns ≥ 2 inconsistencies

### Machinery pin (PRDR)

```
N_eval: derived from L_max=12 master cache (fixed; ~155,984 eigenvalues at L_max=10; cache regen at L_max=12)
L_max: 12 (canonical L_max for L1↔L2 rescue residual; per CF-61 source plan)
scan_range: L_max ∈ {10, 11, 12} for monotonic-convergence sub-check
step_size: N/A (closed-form Mellin-moment evaluation, not a scan)
tolerance: 1e-3 RATIO (PASS) / 1e-2 RATIO (PASS-WITH-RESIDUAL) / 5e-2 RATIO (INFO/FAIL boundary on s_eff)
scheme: L1 = Zubarev (canonical per regulator-convention-lockdown.md; offset-anchored at L_max=10) ↔ L2 = zeta-regulated (per regulator-pin-discipline.md a_n^{ζ} tagging)
convention: substrate-distance-1 Mellin moment, Three-Layer Regulator Theorem decomposition
random_seed: N/A (deterministic Mellin-moment evaluation)
GPU path: torch.linalg.eigvalsh on AMD RX 9070 XT for L_max=12 cache regen if uncached; CPU-fallback torch.linalg.eigvalsh with OMP_NUM_THREADS=8 if VRAM exceeded
```

### Input SHA-256 pins

- `computations/s84_spectrum_cache_L12_tau019.npz`: `<computed-at-runtime; pin verified at plan-freeze 2026-04-27 to be on disk>`
- `computations/canonical_constants.py`: `<computed-at-runtime>` (constants imported: `M_KK`, `tau_fold`, `c_sub_baseline = 2.238`, `r_PathH = 0.0074705`, `dS_fold`, `Vol_SU3`, plus any regulator-axis pins added per `regulator-convention-lockdown.md`)
- `sessions/framework/registry/elimination-bulletins.md`: `<computed-at-runtime>` (Bulletin #3 source classification + s_eff = 11/2 candidate seed)
- `sessions/permanent-results-registry.md`: `<computed-at-runtime>` (§VII.M Three-Layer Regulator Theorem source per `s84-w2a-11-vii-m-landing.md`)
- Memory: `.claude/agent-memory/connes-ncg-theorist/s86-cm1995-kernel-normalization-r2b.md` (PASS-B registry-flag grade source)

### Expected output 4-tuple

```
(value=<r_L1L2(L=12) deviation from 11/7 + s_eff deviation from 11/2 + NROY-cascade-count tuple>,
 scheme=L1-Zubarev-vs-L2-zeta,
 convention=substrate-distance-1-Mellin-Three-Layer-Regulator,
 L_max=12)
```

### NROY-cascade audit protocol

Per W-13 RULE-1 NROY clause (`wave-classification.md` §"NROY clause"), the L1↔L2 axis decomposition admits a fallback substrate axis (LAYER 3 per-Q span, per Three-Layer Regulator Theorem). The cascade audit:

1. Compute `r_L1L2` AND `r_L1L3` AND `r_L2L3` at L_max=12.
2. Check pairwise consistency: `r_L1L2 · r_L2L3 = r_L1L3` (composition law) within `1e-4` RATIO tolerance.
3. If composition-law fails for any pair: log NROY inconsistency at the failing axis pair.
4. Cascade completes when all three axes traversed; result is the M_meta classification (a) registry-flag invariance check.

### What PASS / FAIL means

- **PASS** closes Bulletin #3 rescue residual at theorem grade. The S52-S77 derivation chain is L1↔L2-axis-decomposable; the s_eff = 11/2 candidate becomes Lizzi-observable promotion-eligible (triggers §W10-3 unconditional dispatch). Registry-flag grade per FROZEN-DISCIPLINE upgrades to wall grade. Closes corridor: SOURCE-DOUBLE-CITE-CO-PRIMARY structure preserved across L1↔L2 axis.
- **PASS-WITH-RESIDUAL** preserves Bulletin #3 closure but flags residual quantitative drift; §W10-3 dispatches conditionally with promotion routed through Stage-1 candidate per `joint-theorem-promotion.md` rather than direct theorem-grade landing.
- **INFO** (regulator-class-localized inconsistency) keeps Bulletin #3 at registry-flag grade; §W10-3 routes to mechanical closure per CF-63 conditional-trigger predicate (`mechanical-closure-discipline.md`); NROY-cascade output recorded as carry-forward S88 sub-investigation.
- **FAIL** invalidates the s_eff = 11/2 candidate; §W10-3 routes to mechanical closure unconditionally; corridor closed: L1↔L2 axis-decomposition is NOT preserved across the S52-S77 chain — implies a load-bearing convention drift that triggers SOURCE-RECONCILIATION class-(c) PIN-DRIFT-FROM-STALE-SOURCE remediation in S88.

---

## §W10-2. Bulletin #4 Irrational ρ_∞ Permanent-Wall Landing (§VII.K-PROP-W10-4)

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

**Gate ID**: `S87-BULLETIN-#4-IRRATIONAL-RHO-PERMANENT-WALL-LANDING`
**Trigger**: `[AUDIT]`
**Classification**: GEOMETRIC (substrate-spectral-residue substrate constant; ρ_∞ as L2-IRRATIONAL FERMIONIC-SIGNED-RESIDUE)
**Specialist**: `connes-ncg-theorist` (CF-62 source attribution `connes+lizzi`; connes lead per S86 W-12 attribution convention; lizzi co-sign deferred to executing agent's judgment under autonomous-rolling discipline)
**Source**: CF-62 (`sessions/archive/session-86/compute-carryforward.md` line W-10 CF-2; brief "Permanent-wall registry-landing-target §VII.K-PROP for ρ_∞ ≈ −0.8104; 4-level registry-mechanic schema implementation"). Binding reservation per `partition.md` CF-62 (§VII.K-PROP-W10-4 sub-row pre-allocated in registry summary table per context.md mention).

### Hypothesis

The L2-IRRATIONAL FERMIONIC-SIGNED-RESIDUE substrate constant ρ_∞ ≈ −0.8104 (per S86 W-10 R2-B closure; memory ref `s86-cm1995-kernel-normalization-r2b.md`) is a **permanent-wall registry entry** at §VII.K-PROP.W10-4 with the **4-level registry-mechanic schema** = wall / boundary / corridor / open per Bulletin #4 source classification. Specifically:

1. **Level-1 (wall)**: ρ_∞ is irrational at L → ∞ (Sage-exact rational form unattainable; the constant is fundamentally irrational in the Mellin-cone limit).
2. **Level-2 (boundary)**: ρ_∞ as L_max-dependent envelope satisfies `|ρ(L_max) − ρ_∞| ≤ C · L_max^{−α}` with `α ≥ 2` (predicted from Three-Layer Regulator Theorem L_max-convergence rate at substrate-distance-2 pole).
3. **Level-3 (corridor)**: at L_max = 12 canonical, `ρ(L_max=12) = −0.8104 ± 1e-3` lies inside the Level-2 envelope.
4. **Level-4 (open)**: residual structural questions about FERMIONIC-SIGNED-RESIDUE class membership (whether ρ_∞ admits a Connes-Karoubi pairing representation) are flagged as forward-research carry-forwards.

### Pre-registered substitution chain (publication-precision)

Per `.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration" (Class 8.3) and `.claude/rules/regulator-pin-discipline.md` §"Sage-Exact Rationals for Ω_GW" extension applied to irrational substrate constants:

```
Step 1: ρ(L_max) = Mellin-cone substrate-distance-2 residue at s=4 pole on (A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max})
                                                                          [definition, Bulletin #4]
Step 2: rho_data_value := -0.8104 (canonical 4-sig-fig presentation precision per memory pin)
Step 3: rho_full_precision := <load from .npz, full float64; substrate-first canonical per substrate-first-canonical-sourcing.md>
Step 4: PASS iff (rho_full_precision matches Bulletin #4 closure SHA pin)
                AND (Level-2 envelope satisfied: |rho_data_value - rho_full_precision| < L_max^{-2})
                AND (registry sub-row §VII.K-PROP.W10-4 written with all 4 levels explicit)
                                                                          [composite verdict]
```

ρ_∞ MUST NOT be claimed as a Sage-exact rational. The L2-IRRATIONAL classification per Bulletin #4 is a **structural** finding — the constant is fundamentally irrational. Citation form in registry text uses full float64 from the produced `.npz` data file with publication precision pinned at 10 sig figs (per Class 8.3 publication-precision rule); the 4-sig-fig form `−0.8104` is presentation-precision only and MUST carry the "approximately" qualifier in all narrative prose.

### Threshold

- **PASS**: All four levels populated in §VII.K-PROP.W10-4 sub-row; Level-3 numerical value loaded from `.npz` matches Bulletin #4 source SHA pin (bit-exact to 10 sig figs); Level-2 envelope `|ρ(L_max=12) − ρ_∞_extrapolated| ≤ 12^{−2} = 6.94e-3` satisfied; registry-mechanic schema (wall / boundary / corridor / open) declared explicitly with 4 separate paragraphs in the sub-row text.
- **INFO**: 3 of 4 levels populated; missing level is Level-4 (open) carry-forward annotation only.
- **FAIL**: Any of (i) Level-3 numerical value diverges from Bulletin #4 source pin beyond 10 sig figs, (ii) Level-2 envelope violated, (iii) registry sub-row not written with all 4 levels, (iv) §VII.K-PROP.W10-4 slot unavailable (collision with another concurrent landing — reroute per `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" to next-free-letter `§VII.K-PROP.W10-4'` and emit FAIL-with-remediation per S84 W2a-11 §VII.M→§VII.N precedent).

### Machinery pin (PRDR)

```
N_eval: load from L_max=12 master cache (155,984+ eigenvalues; substrate-distance-2 pole evaluator)
L_max: 12 (canonical anchor for Level-3 empirical pinpoint)
scan_range: L_max ∈ {10, 11, 12} for Level-2 envelope verification
step_size: N/A (closed-form Mellin-cone residue evaluation at s=4 pole)
tolerance: ABSOLUTE 6.94e-3 (Level-2 envelope at L_max=12 = 12^{-2}); ABSOLUTE 1e-10 for Level-3 SHA-pin bit-exactness against Bulletin #4 closure
scheme: substrate-distance-2-Mellin-cone-residue (per Three-Layer Regulator Theorem; L2 zeta-regulated axis)
convention: L2-IRRATIONAL-FERMIONIC-SIGNED-RESIDUE (Bulletin #4 source classification)
random_seed: N/A
GPU path: CPU-only (Mellin-residue evaluator is closed-form on cached eigenvalues; no large matrix ops)
publication_precision_pin: 10 sig figs for narrative cite; full float64 for .npz data file (per Class 8.3)
```

### Input SHA-256 pins

- `computations/s84_spectrum_cache_L12_tau019.npz`: pin verified at plan-freeze
- `sessions/framework/registry/elimination-bulletins.md`: Bulletin #4 source SHA pin `<computed-at-runtime>`
- `sessions/permanent-results-registry.md`: §VII.K-PROP parent header verification (must exist; sub-row §VII.K-PROP.W10-4 pre-allocated)
- `computations/canonical_constants.py`: any new pin promotion under `update_constant("rho_inf_FW", ..., session="S87", source="S87-BULLETIN-#4", comment="L2-IRRATIONAL-FERMIONIC-SIGNED-RESIDUE per Bulletin #4 closure; full float64; presentation precision 10 sig figs")` per canonical write-order Step 2 (math-scripts.md §"Canonical Write-Order")
- Memory: `.claude/agent-memory/connes-ncg-theorist/s86-cm1995-kernel-normalization-r2b.md` (PERMANENT-WALL classification source)

### Expected output 4-tuple

```
(value=<rho_at_Lmax12 + level-2-envelope-residual + 4-level-completeness-bit>,
 scheme=substrate-distance-2-Mellin-residue,
 convention=L2-IRRATIONAL-FERMIONIC-SIGNED-RESIDUE,
 L_max=12)
```

### Registry-write protocol (in-script per mechanical-closure-discipline.md analog)

The producing script `s87_w10_bulletin_4_rho_permanent_wall.py` MUST perform the registry-write IN THE SAME RUN as the verdict-line append (per `.claude/rules/agent-standards.md` §"Completion Verification"):

1. **Step 1 — Verdict-file emission**: append canonical dual-SHA verdict line to `computations/s87_gate_verdicts.txt`.
2. **Step 2 — canonical_constants.py promotion**: invoke `update_constant("rho_inf_FW", ...)` per the canonical write-order rule. New constant entry with provenance `"S87-BULLETIN-#4-IRRATIONAL-RHO-PERMANENT-WALL-LANDING"`.
3. **Step 3 — Registry sub-row write**: open `sessions/permanent-results-registry.md`, locate §VII.K-PROP parent header, append §VII.K-PROP.W10-4 sub-row text with all 4 levels explicit. Use append-only Python writer pattern (NOT Edit tool round-trip) per `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" (2). Scan ALL header levels (`## Bulletin #`, `### Bulletin #`, `#### Bulletin #` analog applied to §VII slot levels) to verify slot uniqueness before append.
4. **Step 4 — Working-paper section**: write `sessions/archive/session-87/session-87-w10-workingpaper.md §W10-2` with substantive content (>15 lines, not stub) per agent-standards.md §"Completion Verification".

If any of Steps 1-4 fails on disk, the gate emits FAIL regardless of numerical PASS — per S82/S84 task-complete-lie failure-mode prevention.

### What PASS / FAIL means

- **PASS** lands ρ_∞ as permanent-wall substrate constant at registry-grade with 4-level mechanic schema. Bulletin #4 closes with WALL classification (highest grade per memory ref). Closes corridor: irrational FERMIONIC-SIGNED-RESIDUE class is registry-recognized; downstream gates (S88+) may cite §VII.K-PROP.W10-4 directly.
- **INFO** lands the constant as boundary/corridor entry with Level-4 carry-forward annotation; Bulletin #4 retains permanent-wall grade pending Level-4 follow-up.
- **FAIL** routes to S88 remediation with SOURCE-RECONCILIATION class-(c) PIN-DRIFT-FROM-STALE-SOURCE if Bulletin #4 source SHA pin diverged, OR slot-collision FAIL-with-remediation if §VII.K-PROP.W10-4 unavailable.

---

## §W10-3. Bulletin #3 Lizzi-Observable Promotion (CONDITIONAL on §W10-1)

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

**Gate ID**: `S87-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: GEOMETRIC (Lizzi-observable theorem-grade promotion of substrate-spectral exponent s_eff = 11/2)
**Specialist**: `lizzi-spectral-functional-theorist` (lead — Lizzi-observable promotion is lizzi's promotion authority per CF-63 source attribution `connes+lizzi`) + `connes-ncg-theorist` (co-sign on substrate-axiomatic side)
**Source**: CF-63 (`sessions/archive/session-86/compute-carryforward.md` line W-10 CF-3; brief "Conditional on CF-61 outcome — promote s_eff = 11/2 candidate to Lizzi-observable theorem grade")
**Conditional-trigger predicate**: PASS iff §W10-1 verdict ∈ {PASS, PASS-WITH-RESIDUAL}; otherwise routes to mechanical closure per `.claude/rules/mechanical-closure-discipline.md` (FAIL value pre-registered as `'PRE-REG-INC_blocked_by_S87-BULLETIN-#3-RESCUE-RESIDUAL_FAIL'` or `'PRE-REG-INC_blocked_by_S87-BULLETIN-#3-RESCUE-RESIDUAL_INFO'`; deferred to S88+).

### Hypothesis

The substrate-spectral exponent `s_eff = 11/2` (S86 W-10 workshop candidate; surfaced in Bulletin #3 R2-B closure) is a **Lizzi-observable theorem-grade quantity** — i.e., it is the canonical exponent of the substrate-distance-1 Mellin-cone residue at the L2-axis with regulator-pin-discipline cite, and admits the Lizzi-observable promotion classification per CF-63 source attribution.

The Lizzi-observable promotion criteria (per lizzi-spectral-functional-theorist promotion authority):

1. **Regulator-pin compliance**: s_eff is L_max-stable (Level-2 envelope `|s_eff(L_max=12) − 11/2| ≤ 12^{−2} = 6.94e-3` satisfied).
2. **Three-Layer-Regulator-Theorem invariance**: s_eff = 11/2 is the canonical exponent under L1 ↔ L2 axis composition (verified by §W10-1 PASS).
3. **Mellin-cone-residue locus**: s_eff = 11/2 corresponds to a substrate-distance-1 pole of the Mellin-cone evaluator (closed-form algebraic identity).

### Pre-registered substitution chain

```
Step 1 (CONDITIONAL on §W10-1 PASS): adopt L1↔L2 axis-decomposition with r_L1L2 = 11/7
                                                                          [from §W10-1]
Step 2: s_eff = 11/2 surfaces as canonical Mellin-cone-residue exponent at substrate-distance-1
                                                                          [W-10 workshop candidate]
Step 3: Verify (a) L_max-stability, (b) Three-Layer-Regulator invariance, (c) Mellin-cone-residue locus
                                                                          [substitute Step 1+2]
Step 4: PASS iff all 3 criteria satisfied                                 [direction: theorem-grade]
```

### Threshold

- **PASS**: §W10-1 returned PASS AND all 3 Lizzi-observable criteria satisfied. s_eff = 11/2 promoted to theorem-grade Lizzi-observable; eligible for permanent-results-registry landing-target §VII.U or §VII.M sub-slot in S88+ (per `.claude/rules/joint-theorem-promotion.md` Stage 0/1/2/3 progression; promotion-target only — binding reservation deferred until S88+ Stage-2 verify lands).
- **INFO**: §W10-1 returned PASS-WITH-RESIDUAL. Promotion routed through Stage-1 candidate (per `joint-theorem-promotion.md` Stage 1) rather than direct theorem-grade landing. Stage-2 two-agent independent verify deferred to S88+ as carry-forward.
- **FAIL**: Mechanical closure per CF-63 conditional-trigger predicate. Verdict line `value='PRE-REG-INC_blocked_by_S87-BULLETIN-#3-RESCUE-RESIDUAL_<status>'` per `.claude/rules/mechanical-closure-discipline.md`.

### Machinery pin (PRDR)

```
N_eval: derived from L_max=12 master cache (Mellin-cone-residue at s=11/2 pole)
L_max: 12 (canonical L_max for Level-2 envelope verification)
scan_range: L_max ∈ {10, 11, 12} for L_max-stability sub-check
step_size: N/A (closed-form Mellin-cone-residue at s=11/2 pole; algebraic-identity verification)
tolerance: 6.94e-3 ABSOLUTE (Level-2 envelope at L_max=12); 1e-4 RATIO for L1↔L2 axis composition cross-check
scheme: L2-zeta-regulated Mellin-cone-residue (per regulator-pin-discipline.md a_n^{ζ} tagging at substrate-distance-1)
convention: substrate-distance-1-Mellin-cone-residue, Lizzi-observable promotion classification
random_seed: N/A
GPU path: CPU-only (Mellin-residue evaluator is closed-form on cached eigenvalues)
conditional_dispatch_predicate: §W10-1 verdict ∈ {PASS, PASS-WITH-RESIDUAL}
```

### Input SHA-256 pins

- `computations/s87_w10_bulletin_3_rescue_residual.npz`: `<computed-at-runtime; produced by §W10-1 dispatch>` (CRITICAL upstream dependency)
- `computations/s87_gate_verdicts.txt`: `<computed-at-runtime>` for §W10-1 verdict-line lookup (conditional-dispatch predicate evaluation)
- `computations/s84_spectrum_cache_L12_tau019.npz`: pin verified at plan-freeze
- `computations/canonical_constants.py`: standard imports
- `sessions/framework/registry/elimination-bulletins.md`: Bulletin #3 source SHA pin
<!--
  AMRI fix (2026-04-28): the agent-memory line was removed.
  - `connes-ncg-theorist/s86-cm1995-kernel-normalization-r2b.md` was deleted by the
    S87 W0 connes-ncg /shortterm collapse (merged into `s86-cluster-results.md`); the
    Bulletin source classification + PASS-B grade content lives canonically in
    `sessions/framework/registry/elimination-bulletins.md` Bulletin #3, already pinned
    on the line above and at §W10-3 pre-flight pin map.
  - `lizzi-spectral-functional-theorist/MEMORY.md` pin triggered AMRI Test 1 per
    `.claude/rules/agent-standards.md` §AMRI. The "Lizzi-observable promotion
    authority" content has been promoted to
    `sessions/framework/registry/lizzi-signature-observable.md` (S87 W0 lizzi
    AMRI-promotion landing); pin the framework file at runtime instead.
-->

### Expected output 4-tuple

```
(value=<3-criteria-pass-bitfield + s_eff_at_Lmax12_residual>,
 scheme=L2-zeta-Mellin-cone-residue,
 convention=substrate-distance-1-Lizzi-observable,
 L_max=12)
```

### What PASS / FAIL means

- **PASS** promotes s_eff = 11/2 to theorem-grade Lizzi-observable; downstream registry landing in S88+ enabled. Closes corridor: substrate-spectral exponent = 11/2 is theorem-grade canonical (NOT fitted parameter).
- **INFO** registers s_eff = 11/2 as Stage-1 candidate; Stage-2 two-agent independent verify is the S88+ carry-forward (analogous to CF-59 Stage-2 protocol per `joint-theorem-promotion.md`).
- **FAIL** (mechanical closure): CF-63 explicit conditional-trigger fired with §W10-1 FAIL/INFO; deferred to S88+; no theorem-grade promotion; corridor remains open.

---

## §W10-4. Strict |λ|_min/|λ|_max Spectrum-Cache Extraction

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

**Gate ID**: `S87-STRICT-LAMBDA-RATIO-EXTRACTION`
**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (direct cache-extraction; no derivation)
**Specialist**: `connes-ncg-theorist`
**Source**: CF-64 (`sessions/archive/session-86/compute-carryforward.md` line W-10 CF-4; brief "Direct extraction from `s84_spectrum_cache_L12_tau019.npz` to obtain bit-exact ratio")

### Hypothesis

The strict ratio `|λ|_min / |λ|_max` extracted bit-exactly from the L_max=12 spectrum cache at τ_fold=0.190 is a substrate-spectral invariant of D_K(τ_fold). Direct extraction (no derivation, no regulator choice) gives the canonical anchor for any future substrate-spectral-condition-number argument.

### Pre-registered substitution chain

```
Step 1: λ_array := loaded eigenvalues from s84_spectrum_cache_L12_tau019.npz       [definition]
Step 2: |λ| := numpy.abs(λ_array)                                                  [definition]
Step 3: |λ|_min := numpy.min(|λ|[|λ| > 0])    (exclude exact zero-modes if present)
                                                                                   [definition]
Step 4: |λ|_max := numpy.max(|λ|)                                                  [definition]
Step 5: ratio := |λ|_min / |λ|_max                                                 [substitute]
Step 6: PASS iff bit-exact extraction completes (no float epsilon allowed)         [direction]
```

### Threshold

- **PASS**: extraction completes; `ratio` is a finite positive float64; cache content_sha256 matches input pin bit-exactly.
- **FAIL**: cache content_sha256 mismatch (cache file changed since plan-freeze) OR `ratio` is non-finite (NaN, Inf, or ≤ 0) OR zero-mode exclusion logic raised an exception.
- **INFO**: ratio is finite positive but lies outside the diagnostic band `[1e-12, 1e+0]` (informative for L_max-scaling diagnostics; not pre-registered as PASS/FAIL).

### Machinery pin (PRDR)

```
N_eval: full eigenvalue array from cache (~155,984+ at L_max=10; full L_max=12 cache)
L_max: 12 (cache-fixed; no scan)
scan_range: N/A (single-point extraction)
step_size: N/A
tolerance: 0 (BIT-EXACT; no float epsilon allowed per CF-64 brief specification)
scheme: direct-numpy-extract
convention: bit-exact float64
random_seed: N/A
GPU path: CPU-only (numpy.abs, numpy.min, numpy.max are O(N) trivial operations; no GPU needed)
zero_mode_exclusion: |λ| > 0 strict (zero-modes if present excluded from |λ|_min)
```

### Input SHA-256 pins

- `computations/s84_spectrum_cache_L12_tau019.npz`: pin verified at plan-freeze 2026-04-27 to be on disk; content_sha256 `<computed-at-runtime; SHA-pin verified bit-exact in script>`
- `computations/canonical_constants.py`: standard imports (`tau_fold`, `M_KK`)

### Expected output 4-tuple

```
(value=<|λ|_min/|λ|_max ratio bit-exact + zero-mode-count>,
 scheme=direct-numpy-extract,
 convention=bit-exact-float64,
 L_max=12)
```

### What PASS / FAIL means

- **PASS** records the canonical strict ratio `|λ|_min / |λ|_max` as a substrate-spectral invariant at τ_fold; available for downstream condition-number arguments in S88+ and beyond. This is a foundational cache-extraction; no closure of any open mechanism, but enables future spectral-condition-number arguments. Promotion to canonical_constants.py via `update_constant("lambda_min_max_ratio_FW", ..., session="S87", source="S87-STRICT-LAMBDA-RATIO-EXTRACTION", comment="Bit-exact extraction from L_max=12 spectrum cache at τ_fold=0.190; strict |λ|_min/|λ|_max ratio")` per canonical write-order.
- **FAIL** indicates cache integrity violation (content_sha256 drift since plan-freeze) — triggers SOURCE-RECONCILIATION class-(c) PIN-DRIFT-FROM-STALE-SOURCE remediation with priority HIGH (cache file is upstream of multiple S87+ gates including §W10-1, §W10-2, §W10-3).
- **INFO** (out-of-band ratio) records the value with diagnostic flag; downstream consumers should re-evaluate L_max-scaling assumptions.

---

## Wave 10 → Wave 11 Decision Point

After §W10-1, §W10-2, §W10-3, §W10-4 complete:

| Outcome | Wave 11 entry condition |
|:--------|:------------------------|
| All four PASS | Bulletin #3 + Bulletin #4 closed at theorem grade; s_eff = 11/2 promoted; spectrum-cache ratio canonical. Wave 11 may proceed with downstream substrate-spectral landings. |
| §W10-1 PASS, §W10-2 PASS, §W10-3 INFO, §W10-4 PASS | s_eff Stage-1 candidate; Stage-2 two-agent independent verify deferred to S88+ via `joint-theorem-promotion.md`. Wave 11 proceeds normally. |
| §W10-1 FAIL | §W10-3 routes to mechanical closure unconditionally. §W10-2 + §W10-4 unaffected (independent gates). S88 must include `S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION` carry-forward (NEW gate; not currently in CF-1..CF-79). |
| §W10-2 FAIL (slot collision OR SHA mismatch) | §VII.K-PROP.W10-4 reroute to `§VII.K-PROP.W10-4'` per S84 W2a-11 §VII.M→§VII.N precedent; FAIL-with-remediation. S88 must verify Bulletin #4 source SHA against current canonical. |
| §W10-4 FAIL | Cache integrity violation; HIGH-priority remediation triggers S88 W0a-equivalent first-wave gate. §W10-1, §W10-2, §W10-3 verdicts may need re-evaluation if cache-derived. |

The decision point feeds directly into §0.10(b) of `session-87-plan-w11.md` (per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness").

---

## Wave 10 Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"PRDR (Pre-Registration Dry-Run)", every gate-relevant machinery parameter is enumerated and pinned at plan-freeze:

| Parameter | §W10-1 | §W10-2 | §W10-3 | §W10-4 |
|:----------|:-------|:-------|:-------|:-------|
| `N_eval` | L_max=12 cache (~155,984+ EVs) | L_max=12 cache | L_max=12 cache | L_max=12 cache (full) |
| `L_max` | 12 | 12 | 12 | 12 |
| `scan_range` | L ∈ {10,11,12} | L ∈ {10,11,12} | L ∈ {10,11,12} | N/A |
| `step_size` | N/A (closed-form) | N/A (closed-form) | N/A (closed-form) | N/A |
| `tolerance` | 1e-3 RATIO PASS / 1e-2 PASS-W-RES / 5e-2 INFO/FAIL | 6.94e-3 ABSOLUTE Level-2; 1e-10 ABSOLUTE Level-3 SHA bit-exact | 6.94e-3 ABSOLUTE Level-2; 1e-4 RATIO L1↔L2 cross-check | 0 BIT-EXACT |
| `scheme` | L1-Zubarev vs L2-zeta | substrate-distance-2-Mellin-cone-residue | L2-zeta Mellin-cone-residue | direct-numpy-extract |
| `convention` | substrate-distance-1 Three-Layer-Regulator | L2-IRRATIONAL FERMIONIC-SIGNED-RESIDUE | substrate-distance-1 Lizzi-observable | bit-exact float64 |
| `random_seed` | N/A | N/A | N/A | N/A |
| `GPU path` | torch.linalg.eigvalsh on AMD RX 9070 XT (cache regen if needed); else CPU | CPU-only | CPU-only | CPU-only |

All four gates are deterministic; no random_seed pinning needed. Each gate's substitution chain is recorded explicitly in its block above.

---

## Wave 10 Input-SHA Ledger

Pre-flight SHA-pin map (verified on disk at plan-freeze 2026-04-27):

| File | Used by | SHA pin status |
|:-----|:--------|:---------------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | §W10-1, §W10-2, §W10-3, §W10-4 | **<computed-at-runtime>** — verified on disk; bit-exact pin enforced in §W10-4 |
| `computations/canonical_constants.py` | §W10-1, §W10-2, §W10-3, §W10-4 | **<computed-at-runtime>** — imports include `M_KK`, `tau_fold`, `c_sub_baseline`, `r_PathH`, `dS_fold`, `Vol_SU3`, `w0_FW` |
| `sessions/framework/registry/elimination-bulletins.md` | §W10-1, §W10-2, §W10-3 | **<computed-at-runtime>** — Bulletins #3 + #4 source pin |
| `sessions/permanent-results-registry.md` | §W10-1, §W10-2 | **<computed-at-runtime>** — §VII.M source (W10-1 ref); §VII.K-PROP parent + §VII.K-PROP.W10-4 sub-row pre-allocation (W10-2 target) |
| `computations/s87_gate_verdicts.txt` | §W10-3 (conditional-dispatch predicate); ALL (verdict-line append) | **<runtime>** — Wave 10 verdict-file emission target; conditional-dispatch reads §W10-1 verdict line for §W10-3 trigger |
| `computations/s87_w10_bulletin_3_rescue_residual.npz` | §W10-3 (upstream dependency) | **<computed-at-runtime; produced by §W10-1>** |
| `sessions/framework/registry/lizzi-signature-observable.md` | §W10-3 (Lizzi-observable promotion authority; AMRI-promoted 2026-04-28 from lizzi MEMORY.md) | **<computed-at-runtime>** |
<!--
  AMRI fix (2026-04-28):
  - `connes-ncg-theorist/s86-cm1995-kernel-normalization-r2b.md` row removed: file was
    deleted by S87 W0 connes-ncg /shortterm collapse (merged into `s86-cluster-results.md`);
    Bulletin source content lives canonically at `sessions/framework/registry/elimination-bulletins.md`
    Bulletin #3 (already pinned in this same table; redundant pin removed).
  - `lizzi-spectral-functional-theorist/MEMORY.md` row replaced by the framework-promoted
    `sessions/framework/registry/lizzi-signature-observable.md` per AMRI Test 1
    (`.claude/rules/agent-standards.md` §AMRI: agent memory cannot be a project-level pin source).
-->


All SHA pins computed at runtime by the producing scripts and emitted in the first 20 lines of stdout per `.claude/rules/gate-verdicts.md` §"Pre-Registration Protocol" Step 2.

### Script slot allocation

| Gate | Producing script | Output `.npz` | Output `.png` |
|:--|:--|:--|:--|
| §W10-1 | `computations/s87_w10_bulletin_3_rescue_residual.py` | `s87_w10_bulletin_3_rescue_residual.npz` | `s87_w10_bulletin_3_rescue_residual.png` |
| §W10-2 | `computations/s87_w10_bulletin_4_rho_permanent_wall.py` | `s87_w10_bulletin_4_rho_permanent_wall.npz` | `s87_w10_bulletin_4_rho_permanent_wall.png` |
| §W10-3 | `computations/s87_w10_bulletin_3_lizzi_observable_promotion.py` | `s87_w10_bulletin_3_lizzi_observable_promotion.npz` | `s87_w10_bulletin_3_lizzi_observable_promotion.png` |
| §W10-4 | `computations/s87_w10_strict_lambda_ratio_extraction.py` | `s87_w10_strict_lambda_ratio_extraction.npz` | `s87_w10_strict_lambda_ratio_extraction.png` |

Working-paper section: `sessions/archive/session-87/session-87-w10-workingpaper.md` with sub-sections §W10-1 / §W10-2 / §W10-3 / §W10-4 each carrying ≥15 lines of substantive content per `.claude/rules/agent-standards.md` §"Completion Verification".

**End of session-87-plan-w10.md.**
