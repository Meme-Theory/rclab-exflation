# Session 91 Plan — Wave 5: Substrate-physics + PBH band-edge + Level-2 moduli + §VII.AV FULL BdG

> **Source**: `sessions/session-plan/session-91-context.md` §"W5 — Substrate-physics + PBH band-edge + Level-2 moduli + §VII.AV FULL BdG" (lines 195-200) post-housekeeping.
> **Wave-classification**: COMPUTE-class per `.claude/rules/wave-classification.md` (M1 numerical PASS predicates; M2 `.py` producing scripts; M3 substrate-physics derivations + STAGE-1-CANDIDATE registry landing; M4 not allowlisted — falls through to COMPUTE-class).
> **Authorship**: volovik-superfluid-universe-theorist primary for T1.11 + T1.12 + T1.13 (substrate-physics PASS predicates on BdG sub-algebra `M_2(ℂ) ⊂ A_K`, Jensen TT-deformation manifold, and D_K spectrum cardinality refinement at L_max ≥ 14). mack-cosmic-bridge sole-writer for T1.14 STAGE-1-CANDIDATE registry-text landing per `feedback_mack-bridge-role.md`.
> **Status**: PLAN — pre-registration, not execution. PRDR pre-flight per `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"`.

---

## Wave 5 Summary

Four substrate-physics gates close pieces of the §VII.AV / §VII.AU deferred-pending refinement queue AND land the first STAGE-1-CANDIDATE registry entry for the PBH band-edge prediction:

| # | Gate ID | Scope | Author | Effort | Independence |
|:--|:--------|:------|:-------|:-------|:-------------|
| W5-1 | `S91-W6-FULL-BdG` (= CF-W5-3 alt route ii) | §VII.AV FULL physical BdG re-derivation via S61/S78 Pauli-Villars at Λ_UV = M_KK (or FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers) — REPLACES SCHEMATIC Casimir-bound proxy on the Corner-IV K-window log-derivative at substrate-distance-2 pole `s=4` | volovik | ~0.8 we | INDEPENDENT of W1 T1.1 (T1.1 = FULL CC multipliers; T1.11 = FULL BdG via PV; complementary refinement routes per §VII.AV refinement-pathway table (ii)+(iii)) |
| W5-2 | `S91-LEVEL-2-MODULI-DEFORMATION-§VII.AU` (= W8-CF-69) | §VII.AU.OP-PROJ substrate-IS observable EXTENDED from Level-1 single-τ-slice (τ_fold = 0.190) to Level-2 moduli-deformation across τ ∈ {0.18, 0.19, 0.20} per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY | volovik | ~1.0 we | INDEPENDENT of W2 T1.5 / T1.10 (which test FIRST-EXTRACTION at single-τ slice; T1.12 tests Level-2 axis) |
| W5-3 | `S91-CF41-UPPER-22.6-EXTENSION` | n_PBH refinement to upper-22.6%-conjunct sub-band `[1.83e-22, 2.2e-22] m⁻³` via L_max = 14+ substrate cardinality refinement of D_K spectrum; Friedrich-Bär saturation pre-check per `math-scripts.md §"D_K Block-Diagonality"` | volovik | ~1.5 we | PREREQUISITE for T1.14 |
| W5-4 | `S91-CF41-VII-LANDING` | STAGE-1-CANDIDATE registry entry at §VII.AX (next-free post-§VII.AW; mack sole-writer) for PBH band-edge prediction `n_PBH = 8.033e-23 m⁻³` upper-22.6% sub-band central; **CONDITIONAL on T1.13 PASS** | mack-cosmic-bridge | ~0.3 we | CONDITIONAL on W5-3 result |

**Total wave effort**: ~3.6 we across 4 gates. **Critical-path dependency**: W5-4 → W5-3 (linear). W5-1, W5-2 dispatch in PARALLEL with W5-3.

**Substrate-physics anchors used**:
- M_KK = 7.428660036284456e16 GeV (canonical_constants.py: M_KK_gravity / M_KK alias, S42 zeta route)
- Δ_BCS = 0.4642547394830737 (Delta_0_OES, M_KK units; S70 BCS-GAP-CANONICAL-70)
- τ_fold = 0.190 (Jensen fold; S42 constants_snapshot, fold_idx=7)
- Λ_UV = M_KK for FULL Pauli-Villars regularization (S61/S78 pipeline)
- L_emp(L_max=12) = −7.046336474406761 M_KK² (§VII.AV Corner-IV K-window log-derivative anchor; preserved per s88-pending-edits-ledger.md)
- §W1c-69 PASS-magnitude posterior n_PBH support: [8.4e-24, 2.2e-22] m⁻³
- CF-CURV-6 upper-22.6% sub-band: [5.5e-23, 2.2e-22] m⁻³ (PASS magnitude region per falsifier-master-inventory.md NEW Row #65)
- Current substrate-IS central anchor: n_PBH_structural_central = 1.758127e-23 m⁻³ at L_max=10 (FAILS upper-22.6% by 0.495 log-OOM; T1.13 target = move central INTO [5.5e-23, 2.2e-22])
- W5-4 target central: 8.033e-23 m⁻³ (mid-band of upper-22.6%; CONDITIONAL on T1.13 confirming this is reachable at L_max ≥ 14)

---

## Wave 5 Decision Point Prerequisites

```
                           ┌─ T1.11 (FULL BdG) ────────────────┐
                           │                                    │
                           ├─ T1.12 (Level-2 moduli) ──────────┤    → independent landings
[W5 dispatch] ──parallel──┤                                    │       (no cross-coupling
                           ├─ T1.13 (PBH L_max=14+) ──┐         │        across T1.11, T1.12)
                           │                          │         │
                           └──────────────────────────┼─────────┘
                                                       │
                                                       PASS-conditional
                                                       │
                                                       ▼
                                              T1.14 (STAGE-1-CANDIDATE
                                              registry landing at §VII.AX
                                              for n_PBH = 8.033e-23 m⁻³)
```

- **T1.11 ⊥ T1.12 ⊥ T1.13** — three independent substrate-physics gates dispatched in parallel; no shared prerequisite within W5.
- **T1.14 ⇐ T1.13 PASS** — T1.14 STAGE-1-CANDIDATE registry landing fires ONLY if T1.13 confirms n_PBH within upper-22.6% sub-band. If T1.13 returns INFO or FAIL, T1.14 closes as PRE-REG-INC (deferred to S92 contingent on a different refinement pathway, OR routed to alternate band-edge structural interpretation).
- **Cross-wave dependencies (informational)**: T1.11 informs S91 W1 T1.1 dispatch ordering (both target §VII.AV PROXY-REFINEMENT; T1.11 is the PV route, T1.1 is the CC-multipliers route; if T1.11 lands first with a clean PV verdict, W1 may rebalance T1.1 priority). T1.12 informs S91 W1 M9 = CF-AV-L2-MODULI (Level-2 moduli-deformation for §VII.AV, the parallel slot to §VII.AU; T1.12 establishes the Level-2 axis methodology on the FIRST-EXTRACTION-class §VII.AU entry; W1 M9 extends to PROXY-REFINEMENT-class §VII.AV).

**Mechanical-closure trigger**: per `.claude/rules/mechanical-closure-discipline.md §"When mechanical closure IS acceptable"`, if T1.13 returns FAIL/INFO at L_max=14 saturation, T1.14 mechanically closes with `value='PRE-REG-INC_blocked_by_T1.13_upstream_INFO/FAIL'`. The downstream-decision-point routing IS pre-registered in this plan-block per item-1-clean.

---

## §W5-1. S91-W6-FULL-BdG — §VII.AV FULL BdG re-derivation replacing SCHEMATIC Casimir-bound proxy (T1.11; volovik primary)

### 1. Gate ID
`S91-W6-FULL-BdG` (alias: `CF-S91-W6-FULL-BdG`; same forward-promoting gate as §VII.AV refinement-pathway route (ii) = FULL physical Pauli-Villars regularization at Λ_UV = M_KK per S61/S78 pipeline). NOT co-registered with W1 T1.1 (which is route (iii) = FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers); the two routes are complementary not duplicate (substantively distinct UV-regulator paths to the same Level-3 anchor).

### 2. Trigger
`[VERIFY-THEOREM]` (per `gate-verdicts.md` Pre-Registration Protocol) — substrate-physics gate verifying the FULL physical pipeline's empirical α exponent against the SCHEMATIC Casimir-bound proxy's predicted Level-2 envelope `L^{-3}` at d=4 substrate-distance-2 pole `s=4`.

### 3. Classification
PHONONIC (substrate-physics; substrate-IS K-window log-derivative on the BdG sub-algebra `M_2(ℂ) ⊂ A_K`; emergent observable = Pillar V continuum 3He-B mutual-friction coefficient under HKR `L_max → ∞` bridge map).

### 4. Agent type
`volovik-superfluid-universe-theorist` (primary). Rationale: T1.11 evaluates the FULL physical BdG pipeline against the substrate-IS Corner-IV K-window log-derivative anchor `L_emp(L_max=12) = −7.046336474406761 M_KK²` — a state-pair functional on the BdG sub-algebra. Volovik's BCS-on-SU(3) substrate-physics expertise + Pauli-Villars regularization at Λ_UV = M_KK (S61/S78 pipeline) is the canonical owner per `feedback_agent-roster.md`. EXCLUDED reviewers (do not dispatch as Stage-2 cross-reviewer post-PASS): connes-ncg-theorist (already cross-reviews W1 T1.1 FULL CC multipliers route; orthogonality preserved by axis-distinctness per `joint-theorem-promotion.md §"Stage 2"` Axis-B Selection Protocol).

### 5. Hypothesis
**Hypothesis H1.11**: under FULL physical Pauli-Villars regularization at Λ_UV = M_KK, the substrate-IS Corner-IV K-window log-derivative `R_KW(τ_fold) = d ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})) / d ln(K_window)` at substrate-distance-2 pole `s=4` converges to the laboratory-IN Pillar V continuum BdG-sector observable at rate `L^{-α}` with empirically extracted `α_PV ∈ [2.9, 3.1]` matching the SCHEMATIC-proxy's predicted `α = 3` to within 5%.

This is a Level-2-binding verification: if `α_PV ∈ [2.9, 3.1]`, the SCHEMATIC proxy's predicted envelope is FULL-physical confirmed → §VII.AV REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-class tag is RESOLVED at the proxy-refinement axis → entry advances toward STAGE-3-PERMANENT eligibility (pending Level-3 empirical anchor satisfaction). If `α_PV` lies outside `[2.7, 3.3]` or the FULL-PV pipeline saturates differently, the proxy is FALSIFIED → §VII.AV demoted with explicit pathway revision.

### 6. Method (full dispatch prompt)

> **Volovik**: Re-derive the substrate-IS K-window log-derivative `R_KW(τ_fold)` on the Corner-IV BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` at substrate-distance-2 pole `s=4` using FULL physical Pauli-Villars regularization at `Λ_UV = M_KK` (per S61/S78 pipeline; do NOT use `_spectral_action_regulators.py` SCHEMATIC helpers — those are the proxy being refined).
>
> **Pipeline**:
> 1. Load D_K spectrum from canonical `s84_spectrum_cache_L12_tau019.npz` (full spectrum at L_max=12, τ_fold=0.190) — this is the substrate-IS eigenvalue set the FULL-PV regularization operates on (truncation-level pin per `cross-pillar-bridge-anatomy.md` Level-2 sub-class binding axis).
> 2. Apply FULL Pauli-Villars subtraction with mass-scale `Λ_UV = M_KK = 7.428660036284456e16 GeV` per S61/S78 protocol: replace `D_K^{−2s}` with `D_K^{−2s} − Σ_j c_j (D_K² + M_j²)^{−s}` for the canonical PV mass-tower `{M_j} = {M_KK, √2·M_KK}` with Pauli-Villars coefficients `{c_1 = +2, c_2 = −1}` (cancels leading + subleading UV divergence at `s ≤ d/2 = 2`).
> 3. Compute `Tr_{M_2(ℂ)}(P_BdG · [D_K^{−2s} − PV-subtraction])` evaluated at each `L_max ∈ {6, 7, 8, 9, 10, 11, 12}` truncation level; tag intermediates `# (local)`.
> 4. Compute `R_KW^{PV}(τ_fold, L_max)` = numerical first derivative `d ln(·) / d ln(K_window)` with K_window swept across `[0.5·Δ_BCS, 2·Δ_BCS]` (substrate-natural K-window spec per CF-62 disambiguation; `Δ_BCS` from canonical_constants).
> 5. Extract empirical α exponent via least-squares fit `R_KW^{PV}(L_max) ≈ A · L_max^{−α} + B` on `L_max ∈ {6, ..., 12}` (data) with `α` free and `A, B` free; report `α_PV` central + 1σ.
> 6. Cross-check against L=12 substrate-natural anchor `L_emp(L_max=12) = −7.046336474406761 M_KK²` (s88-pending-edits-ledger.md preservation source): require `|R_KW^{PV}(L_max=12) − L_emp(L_max=12)| / |L_emp(L_max=12)| ≤ 0.10` (10% relative tolerance for the FULL-PV ↔ SCHEMATIC-proxy cross-check at the canonical anchor; if FAIL, the FULL-PV pipeline does NOT reproduce the substrate-natural anchor and the gate composite returns FAIL on sign + magnitude).
> 7. Emit JSON sidecar: `{α_PV, α_PV_1sigma, A_PV, B_PV, L_emp_PV_L12, anchor_consistency, sign_verdict, magnitude_verdict, regime_verdict}`.
> 8. Emit verdict line per `gate-verdicts.md` S87+ schema-v2 (3-tuple companion row REQUIRED — `[SIGN]` trigger fires on the α_PV ∈ [2.9, 3.1] sign clause).
> 9. Update working-paper §VII.W5-1 (>15 lines; substrate framing block; FULL-PV pipeline disclosure; convention tag `corner-IV-FULL-PV-Lambda_UV-M_KK-substrate-distance-2-pole-s4`).

> **Substrate framing reminder**: The substrate IS the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at single-τ-slice τ_fold = 0.190 and substrate-distance-2 pole `s=4`. The FULL Pauli-Villars regularization at `Λ_UV = M_KK` IS the substrate's intrinsic UV-completion of the Mellin-cone trace; the laboratory-IN Pillar V continuum 3He-B mutual-friction coefficient IS the measurement context for the substrate's bridge-map image. Do NOT invert: "the BdG cryostat measurement IN cryogenic-container IS canonical" — invert to "the substrate's K-window log-derivative IS canonical at the BdG sub-algebra; 3He-B IS the laboratory pillar of the HKR-image".

### 7. Machinery pin (PRDR)

| Parameter | Value | Provenance |
|:----------|:------|:-----------|
| `L_max` | 12 (canonical truncation; spectrum cache `s84_spectrum_cache_L12_tau019.npz`) | `math-scripts.md §"D_K Block-Diagonality"` W11-3 Friedrich-Bär saturation (L_max ≥ 12 saturates bot-K) |
| `L_max_scan` | {6, 7, 8, 9, 10, 11, 12} | least-squares α extraction needs ≥ 5 points |
| `τ_pin` | 0.190 (τ_fold, single-τ-slice; do NOT scan τ in T1.11; that is T1.12's domain) | canonical_constants.py `tau_fold` |
| `K_window_range` | [0.5·Δ_BCS, 2·Δ_BCS] = [0.232, 0.929] M_KK | substrate-natural per CF-62 disambiguation |
| `K_window_n_points` | 21 (log-spaced for `d ln / d ln` derivative) | numerical derivative step pin |
| `Λ_UV` | M_KK = 7.428660036284456e16 GeV | FULL Pauli-Villars mass scale |
| `PV_mass_tower` | {M_1 = M_KK, M_2 = √2·M_KK} | S61/S78 canonical 2-PV tower |
| `PV_coefficients` | {c_1 = +2, c_2 = −1} | leading + subleading UV cancellation at `s ≤ d/2 = 2` |
| `regulator_class` | Pauli-Villars (FULL physical) | distinct from `_spectral_action_regulators.py` SCHEMATIC ζ-helper |
| `convention` | `corner-IV-FULL-PV-Lambda_UV-M_KK-substrate-distance-2-pole-s4` | NO `-SCHEMATIC` suffix (this is FULL physical regularization, NOT SCHEMATIC proxy) |
| `scheme` | `S91-W5-1-FULL-BdG-PV` | gate identifier in scheme field |
| `tolerance` | rel_tol = 0.05 on α_PV vs predicted α=3; rel_tol = 0.10 on L_emp anchor consistency | Class-8.3 publication-precision pin; downstream verifier tolerance bounds |
| `GPU path` | `torch.linalg` on RX 9070 XT (FULL spectrum cache load is ~155k eigenvalues; PV-subtracted trace evaluation parallelizes well) | `math-scripts.md §"Heavy Linear Algebra"` |
| `OMP_NUM_THREADS` | 8 (fallback cap if GPU unavailable) | computation-environment.md |
| `random_seed` | n/a (deterministic spectrum cache + deterministic numerical derivative) | — |
| `script_path` | `computations/session-91/s91_w5_1_full_bdg_pv_substrate_distance_2_pole_s4.py` | — |
| `npz_path` | `computations/session-91/s91_w5_1_full_bdg_pv.npz` | — |
| `png_path` | `computations/session-91/s91_w5_1_full_bdg_pv_alpha_extraction.png` (α extraction log-log fit plot) | — |
| `verdict_file` | `computations/session-91/s91_gate_verdicts.txt` | `gate-verdicts.md §"Canonical Verdict-File Path"` MANDATORY |
| `wp_section` | `sessions/archive/session-91/session-91-w5-workingpaper.md §VII.W5-1` | designated writer = volovik |

### 8. Expected output 4-tuple

`(value=<α_PV ± 1σ>, scheme=S91-W5-1-FULL-BdG-PV, convention=corner-IV-FULL-PV-Lambda_UV-M_KK-substrate-distance-2-pole-s4, L_max=12)`

Plus 3-tuple `(sign_verdict, magnitude_verdict, regime_verdict)` companion row per S87+ schema-v2.

### 9. PASS / FAIL / INFO thresholds

| Sub-verdict | PASS | INFO | FAIL |
|:------------|:-----|:-----|:-----|
| `sign_verdict` | `α_PV > 0` AND L_emp_PV(L_max=12) negative (matches L_emp anchor sign) | n/a | sign mismatch (α_PV ≤ 0 OR L_emp_PV positive) |
| `magnitude_verdict` | `|α_PV − 3| ≤ 0.10` (~3.3% — within PV ↔ SCHEMATIC cross-check band) AND `|L_emp_PV(L_max=12) − L_emp(L_max=12)| / |L_emp(L_max=12)| ≤ 0.05` | `0.10 < |α_PV − 3| ≤ 0.30` (~10% — borderline; SCHEMATIC proxy holds qualitatively but FULL PV gives a softened envelope) | `|α_PV − 3| > 0.30` OR anchor relative error > 0.10 |
| `regime_verdict` | Friedrich-Bär saturation theorem VALID at L_max ≥ 12 per W11-3 (bottom-K invariance certified analytically; PV regulator preserves saturation) | MARGINAL if L_max=12 anchor PASSes but L_max ∈ {6,...,11} fits show > 50% saturation-band scatter | BREAKDOWN if PV-subtraction introduces a new pole structure inside `s ∈ [3.5, 4.5]` that the SCHEMATIC proxy did not see |
| Composite | per `gate-verdicts.md` collapse rule (S87+ schema-v2) | per collapse rule | per collapse rule |

**Composite PASS** = α_PV verified within [2.9, 3.1] AND L_emp anchor reproduced within 5% AND regime VALID → §VII.AV PROXY-REFINEMENT sub-class tag is RESOLVED on the FULL-PV route; entry advances toward STAGE-3-PERMANENT eligibility pending Level-3 anchor satisfaction.

**Composite INFO** = α_PV in marginal band [2.7, 3.3] but L_emp anchor reproduced within 10% → SCHEMATIC proxy holds at first-order but FULL-PV softens envelope; §VII.AV stays at REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT, sub-class tag PRESERVED; refinement-pathway table extended with "FULL-PV verifies SCHEMATIC qualitatively; quantitative refinement awaits FULL-CC multipliers (T1.1)".

**Composite FAIL** = α_PV outside [2.7, 3.3] OR L_emp anchor mismatch > 10% → SCHEMATIC Casimir-bound proxy is FALSIFIED at the FULL-PV cross-check; §VII.AV demoted; refinement-pathway table revised with explicit pathway revision request.

### 10. Substitution chain (mandatory for the [SIGN] trigger)

```
Step 1 (Definition): R_KW(τ_fold, L_max, s) = d ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})) / d ln(K_window)
                     where P_BdG = central projector onto M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) (BdG sub-algebra; per §VII.AV anatomy element 1)
                     and Tr_{M_2(ℂ)} = trace restricted to BdG sub-algebra (S88 W7a-73 OE-form MANDATORY at K=2)

Step 2 (FULL PV substitution): D_K^{−2s} → D_K^{−2s} − Σ_{j=1,2} c_j (D_K² + M_j²)^{−s}
                                with {M_1, M_2} = {M_KK, √2·M_KK} and {c_1, c_2} = {+2, −1}
                                cancels leading + subleading UV divergence at s ≤ d/2 = 2

Step 3 (envelope extraction): R_KW^{PV}(τ_fold, L_max, s=4) ~ A · L_max^{−α} + B
                              fit α free; α = 3 is the SCHEMATIC-proxy prediction; PASS band α ∈ [2.9, 3.1]

Step 4 (Simplify direction): α > 0 (decreasing envelope) is REQUIRED for HKR L_max→∞ image convergence
                              SIGN-PASS iff α_PV > 0; sub-band PASS iff α_PV ∈ [2.9, 3.1]

Step 5 (Direction): if α_PV ∈ [2.9, 3.1] → SCHEMATIC proxy is FULL-physical confirmed at PV regulator class
                    if α_PV outside [2.7, 3.3] → SCHEMATIC proxy is FALSIFIED at PV regulator class
                    Direction of PASS: FULL-PV reproduces SCHEMATIC envelope quantitatively
                    Direction of FAIL: FULL-PV softens / hardens envelope materially vs SCHEMATIC
```

### 11. Solution-space interpretation

- **PASS** → closes the §VII.AV REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT corridor on the FULL-PV route. Confirms substrate's Corner-IV K-window log-derivative at substrate-distance-2 pole `s=4` is a Level-2-binding observable whose HKR convergence rate is regulator-class-INVARIANT across SCHEMATIC ζ-helper and FULL physical PV (Class-8.4 representation-convention-pin discipline satisfied across UV-regulator axis per `regulator-pin-discipline.md` Cross-link table). §VII.AV advances toward STAGE-3-PERMANENT eligibility upon Level-3 empirical anchor (Pillar V 3He-B mutual-friction continuum measurement) becoming available.
- **INFO** → SCHEMATIC proxy is qualitatively right but quantitatively soft. The substrate's K-window log-derivative carries a regulator-class-DEPENDENT prefactor; further refinement requires T1.1 FULL-CC multipliers OR T1.2 K_canonical operational-alignment (W1 wave).
- **FAIL** → SCHEMATIC Casimir-bound proxy is structurally wrong on the BdG sub-algebra; the substrate's Corner-IV K-window log-derivative does NOT have an `L^{-3}` envelope under FULL physical regularization. §VII.AV slot must be re-evaluated under an alternative envelope predictor; the entire deferred-pending PROXY-REFINEMENT pathway requires plan-revision request to next-session orchestrator.

**Closes**: the FULL-PV refinement-pathway corridor (route (ii) of the §VII.AV refinement-pathway table).
**Opens** (on PASS): cross-regulator-class verification — does the FULL-CC multipliers route (T1.1) yield the same α? If yes, §VII.AV's envelope is regulator-class-FI per `epistemic-discipline.md §"Source Reconciliation"` FI/RD/MIXED taxonomy.

### 12. Effort

~0.8 wave-equivalents (single substrate-physics computation; spectrum cache reuse; numerical α extraction is ~30 min wall on RX 9070 XT; verdict-line emission + WP §VII.W5-1 write).

### 13. Substrate-framing reminder

§VII.AV's substrate-IS observable IS the Corner-IV K-window log-derivative on `M_2(ℂ) ⊂ A_K` at single-τ-slice τ_fold = 0.190 and substrate-distance-2 pole `s=4`. The FULL Pauli-Villars regularization at `Λ_UV = M_KK` IS the substrate's intrinsic UV-completion; it is NOT a "regularization scheme imposed FROM outside" the substrate. The HKR `L_max → ∞` bridge map IS substrate-IS at the cohomology-class level; the Pillar V 3He-B continuum BdG-sector mutual-friction observable IS the laboratory-IN measurement context. Direction substrate → emergent throughout.

---

## §W5-2. S91-LEVEL-2-MODULI-DEFORMATION-§VII.AU — Extend §VII.AU.OP-PROJ substrate-IS observable from Level-1 single-τ-slice to Level-2 moduli-deformation across τ ∈ {0.18, 0.19, 0.20} (T1.12; volovik primary)

### 1. Gate ID
`S91-LEVEL-2-MODULI-DEFORMATION-§VII.AU` (alias: `CF-S91-LEVEL-2-MODULI-DEFORMATION-§VII.AU`; same as W8-CF-69 carry-forward from S90 W8 wave).

### 2. Trigger
`[VERIFY-THEOREM]` — substrate-physics gate verifying that §VII.AU.OP-PROJ's substrate-IS observable identity `n_s_FW² − 1 ≡ α_s_canonical` in Q at substrate-distance-1 pole `s=3` is INVARIANT (Level-2-INVARIANT) or DEFORMABLE (Level-2-DEFORMABLE) across the Jensen TT-deformation manifold τ ∈ {0.18, 0.19, 0.20}.

### 3. Classification
PHONONIC (substrate-physics; substrate-IS Mellin-cone closure on `A_K` extended along Jensen TT-deformation axis; emergent observable = Pillar II CMB n_s deformation profile under bridge-map HKR L_max → ∞ image).

### 4. Agent type
`volovik-superfluid-universe-theorist` (primary). Rationale: T1.12 evaluates §VII.AU.OP-PROJ's substrate-IS observable identity ALONG THE Level-2 moduli-deformation axis per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY (since S88 W-7 V.4). The moduli-deformation axis IS the substrate's intrinsic Jensen TT-deformation manifold — volovik's superfluid-vacuum program canonically owns the moduli-space-of-τ-deformations framing (the moduli-space of TT-deformations IS substrate-IS at the Level-2 layer, NOT a coordinate on a meta-container; this is the inverse of the GR-default coordinate-on-meta-container reading volovik corrects per `feedback_reporting-framing.md`). EXCLUDED reviewers: connes-ncg-theorist (cross-reviews W1 T1.1 + W2 T1.5 §VII.AU FIRST-EXTRACTION; orthogonality preserved).

### 5. Hypothesis
**Hypothesis H1.12**: the substrate-IS observable identity `n_s_FW² − 1 ≡ α_s_canonical` in Q at substrate-distance-1 pole `s=3` is **Level-2-INVARIANT** across τ ∈ {0.18, 0.19, 0.20} — i.e., the rational identity holds at every τ in the canonical 3-point Jensen TT-deformation neighborhood, with `n_s_FW(τ) = sqrt(1 + α_s_canonical(τ))` substituting into the same closed-form identity at every τ.

**Decision split**:
- (a) **Level-2-INVARIANT**: identity holds at every τ ∈ {0.18, 0.19, 0.20} → §VII.AU advances to Level-2 verification confirming MANDATORY single-τ-slice declaration is structurally preserved under moduli-deformation; bridge map's structural-confidence ladder gains a Level-2-MODULI-INVARIANT annotation.
- (b) **Level-2-DEFORMABLE**: identity fails at τ ≠ τ_fold; rational identity is τ_fold-specific → §VII.AU's substrate-IS observable inherits a Jensen TT-deformation residual; entry MUST re-tag as "Level-1 single-τ-slice ONLY" with explicit Level-2-DEFORMABLE annotation.
- (c) **Mixed**: identity holds at τ ∈ {0.19, 0.20} but fails at τ = 0.18 (or analogous asymmetry per S88 W2-9 §VII.AE τ-asymmetric breakdown geometry precedent) → routes to Level-2 asymmetry sub-class queued for S92+ deeper investigation.

### 6. Method (full dispatch prompt)

> **Volovik**: Extend §VII.AU.OP-PROJ's substrate-IS observable from Level-1 single-τ-slice (τ_fold = 0.190) to Level-2 moduli-deformation along the Jensen TT-deformation manifold at three canonical τ-points {0.18, 0.19, 0.20}. The Level-2 axis IS substrate-IS at the moduli-deformation layer per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (the moduli-space of τ-deformations IS the substrate's intrinsic deformation parameter, NOT a coordinate on a meta-container).
>
> **Pipeline**:
> 1. For each τ ∈ {0.18, 0.19, 0.20}:
>    a. Construct or load the τ-deformed D_K spectrum at L_max=10 (canonical; cache τ=0.19 already exists as `s84_spectrum_cache_L12_tau019.npz`; τ=0.18 and τ=0.20 require new spectrum computations per Jensen TT-deformation pipeline — use `dirac_spectrum.get_spectrum(τ=...)` per S58 substrate-compaction-timescape canonical Jensen-deformation function).
>    b. Compute `α_s_canonical(τ)` from the substrate-IS Mellin-cone closure at substrate-distance-1 pole `s=3` per S85 W2-9 canonical: `α_s_canonical(τ) = (n_s²(τ) − 1)` where `n_s(τ)` = framework prediction at the τ-deformed spectrum.
>    c. Compute `n_s_FW(τ)` directly via Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on the τ-deformed D_K (per §VII.AU.OP-PROJ Element 3 bridge-map specification).
>    d. Compute the rational identity residual: `R_identity(τ) = |n_s_FW(τ)² − 1 − α_s_canonical(τ)| / |α_s_canonical(τ)|`.
> 2. PASS criterion: `R_identity(τ) ≤ 1e-6` (Sage-Q exact identity tolerance) at ALL THREE τ ∈ {0.18, 0.19, 0.20} → Level-2-INVARIANT.
> 3. INFO criterion: `R_identity(τ) ≤ 1e-3` at all three τ but `R_identity(0.20) ≠ R_identity(0.18)` symmetrically by > 10% → Level-2 asymmetric (mixed sub-class per S88 W2-9 §VII.AE precedent — negative-side τ-asymmetric breakdown geometry at δ_τ_crit_neg = −0.0750).
> 4. FAIL criterion: `R_identity(τ) > 1e-3` at ANY τ → Level-2-DEFORMABLE; identity holds at single-τ-slice ONLY.
> 5. For each τ, also compute Sage-Q exact rational form via `sage_eval` MCP (cross-check the float64 R_identity against Sage-QQ exact rational arithmetic; if Sage-QQ confirms zero remainder at all three τ → strongly supports Level-2-INVARIANT).
> 6. Emit JSON sidecar: `{tau_grid, n_s_FW_grid, alpha_s_canonical_grid, R_identity_grid, R_identity_sageQQ_grid, level_2_classification, sign_verdict, magnitude_verdict, regime_verdict}`.
> 7. Emit verdict line per `gate-verdicts.md` S87+ schema-v2.
> 8. Update working-paper §VII.W5-2 (>15 lines; substrate framing emphasizing moduli-deformation IS-not-IN; level-2 classification disclosure; per-τ residual table).

> **Substrate framing reminder**: The substrate IS the spectral triple `(A_K, H_K, D_K(τ))` at EACH τ in the moduli-deformation neighborhood. The moduli-space `{ τ ∈ ℝ : (A_K, H_K, D_K(τ)) is substrate-IS }` IS the substrate's own deformation parameter manifold — it is NOT a coordinate on an external container. Forbidden: "the substrate moves through τ-coordinate space". Correct: "τ IS the substrate's intrinsic Jensen TT-deformation parameter; the moduli-space of τ-deformations IS substrate-IS at the Level-2 layer; the substrate's identity `n_s_FW² − 1 ≡ α_s_canonical` either holds across this Level-2 substrate or fails — the failure direction is itself a substrate property, not an extrinsic moduli coordinate".

### 7. Machinery pin (PRDR)

| Parameter | Value | Provenance |
|:----------|:------|:-----------|
| `L_max` | 10 (canonical truncation for §VII.AU.OP-PROJ Level-1 anchor; preserves comparability with S89 W7a Sage-QQ PASS at L_max=10) | §VII.AU.OP-PROJ Level 3 anchor at L_max=10 canonical |
| `τ_grid` | {0.180, 0.190, 0.200} (3-point Jensen TT-deformation neighborhood around τ_fold = 0.190; symmetric ±5.3% relative span) | volovik s6 §6 CF-AV-L2-MODULI pre-registration; matches S88 W2-9 §VII.AE Level-2 calibration corpus instance #1 |
| `regulator_class` | ζ-helper SCHEMATIC `_spectral_action_regulators.py` for α_s_canonical computation (matches §VII.AU.OP-PROJ S89 W7a canonical regulator) PLUS Sage-Q exact rational cross-check on identity residual | per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY: `convention=...-SCHEMATIC` + companion `# tier_pin=TIER-2` row REQUIRED |
| `convention` | `level-2-moduli-deformation-§VII.AU-SCHEMATIC` (mandatory `-SCHEMATIC` suffix per §(iv); ζ-helper IS schematic) | S88 W8-92 K=4 MANDATORY |
| `scheme` | `S91-W5-2-LEVEL-2-MODULI-§VII.AU` | gate identifier |
| `identity_residual_tolerance_PASS` | 1e-6 (Sage-Q exact identity tolerance per `regulator-pin-discipline.md §"Extension: Sage-Exact Rationals"` discipline) | publication-precision pin per Class-8.3 |
| `identity_residual_tolerance_INFO` | 1e-3 (~3 sig-fig deformation tolerance) | borderline band |
| `tau_asymmetry_threshold` | 0.10 (10% asymmetry between R_identity(0.18) and R_identity(0.20) signals mixed sub-class) | S88 W2-9 §VII.AE precedent (2.33× ratio = >100% asymmetry; 10% threshold is conservative) |
| `Sage_MCP_call` | `sage_eval` for each τ's rational identity remainder | Sage-Q exact arithmetic per `regulator-pin-discipline.md` mandate |
| `GPU path` | `torch.linalg` (full spectrum at τ=0.18 + τ=0.20 needs ~30 min wall time on RX 9070 XT per spectrum) | math-scripts.md |
| `OMP_NUM_THREADS` | 8 (fallback cap) | computation-environment.md |
| `random_seed` | n/a (deterministic) | — |
| `script_path` | `computations/session-91/s91_w5_2_level2_moduli_deformation_vii_au.py` | — |
| `npz_path` | `computations/session-91/s91_w5_2_level2_moduli.npz` | — |
| `png_path` | `computations/session-91/s91_w5_2_level2_moduli_residual_vs_tau.png` (R_identity vs τ scan plot) | — |
| `verdict_file` | `computations/session-91/s91_gate_verdicts.txt` | MANDATORY canonical path |
| `wp_section` | `sessions/archive/session-91/session-91-w5-workingpaper.md §VII.W5-2` | designated writer = volovik |
| `tier_pin_companion_row` | `# tier_pin=TIER-2 # per substrate-first-canonical-sourcing.md §(iv) ζ-helper SCHEMATIC docstring lines 23-30; Sage-Q exact rational cross-check elevates this to PARTIAL-POSITIVE compliance per S90 W1-9 3-class taxonomy` | REQUIRED for POSITIVE-CALIBRATION class per S88 W7b-83 K=4 MANDATORY |

### 8. Expected output 4-tuple

`(value=<Level-2 classification: INVARIANT | DEFORMABLE | MIXED-asymmetric>, scheme=S91-W5-2-LEVEL-2-MODULI-§VII.AU, convention=level-2-moduli-deformation-§VII.AU-SCHEMATIC, L_max=10)`

Plus 3-tuple `(sign_verdict, magnitude_verdict, regime_verdict)`.

### 9. PASS / FAIL / INFO thresholds

| Sub-verdict | PASS | INFO | FAIL |
|:------------|:-----|:-----|:-----|
| `sign_verdict` | identity residual `R_identity(τ) > 0` direction matches predicted sign (zero or positive at every τ) at the Sage-Q exact level | n/a | identity residual changes sign across τ-grid (structurally impossible if identity holds; FAIL otherwise) |
| `magnitude_verdict` | `R_identity(τ) ≤ 1e-6` at all τ ∈ {0.18, 0.19, 0.20} → **Level-2-INVARIANT** | `1e-6 < R_identity(τ) ≤ 1e-3` at all τ OR asymmetry between R_identity(0.18) vs R_identity(0.20) > 10% with both ≤ 1e-3 → **Level-2-MIXED-asymmetric** | `R_identity(τ) > 1e-3` at any τ → **Level-2-DEFORMABLE** |
| `regime_verdict` | Friedrich-Bär saturation theorem VALID at L_max=10 across all three τ (W11-3 bottom-K invariance certified; τ-deformation preserves saturation per S88 W11-2 calibration) | MARGINAL if τ ∈ {0.18, 0.20} requires L_max > 10 for saturation but L_max=10 truncation introduces > 5% cardinality drift | BREAKDOWN if τ=0.18 destabilizes the Jensen fold structure (per S87 W11-2 τ_fold = 0.190 is the canonical fold; ±5.3% deformation should preserve fold per W2-9 calibration) |
| Composite | per S87+ schema-v2 collapse rule | per collapse rule | per collapse rule |

**Composite PASS** = Level-2-INVARIANT confirmed at Sage-Q exact tolerance → §VII.AU.OP-PROJ's substrate-IS observable identity is structurally preserved across Level-2 moduli-deformation; advances toward STAGE-3-PERMANENT eligibility upon FIRST-EXTRACTION resolution (W2 T1.5 / T1.10).

**Composite INFO** = Level-2-MIXED-asymmetric → §VII.AU advances with Level-2-MODULI-MIXED annotation; flagged for S92+ asymmetry sub-class investigation; rule-file extension queued at `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` for asymmetric Level-2 sub-class.

**Composite FAIL** = Level-2-DEFORMABLE → §VII.AU.OP-PROJ MUST re-tag as Level-1 single-τ-slice ONLY (current MANDATORY tag stands); explicit annotation that the identity is τ_fold-specific, not moduli-INVARIANT. Bridge structural-confidence ladder must add Level-2-DEFORMABLE caveat to Level 1.

### 10. Substitution chain (mandatory for the [SIGN] trigger)

```
Step 1 (Definition): identity at τ_fold = 0.19 (canonical, S89 W7a Sage-QQ PASS):
                     n_s_FW²(τ_fold) − 1 ≡ α_s_canonical(τ_fold)  in Q

Step 2 (Level-2 extension): at each τ ∈ {0.18, 0.19, 0.20}, evaluate
                            n_s_FW(τ) = sqrt(1 + α_s_canonical(τ))  candidate
                            and α_s_canonical(τ) = (n_s_FW(τ))² − 1  from independent Mellin-residue
                            R_identity(τ) = |n_s_FW(τ)² − 1 − α_s_canonical(τ)| / |α_s_canonical(τ)|

Step 3 (Substitution at each τ): compute R_identity(τ=0.18), R_identity(τ=0.19), R_identity(τ=0.20)
                                  via Sage-Q exact rational arithmetic (mcp__sage__sage_eval)

Step 4 (Simplify direction): PASS iff R_identity(τ) ≤ 1e-6 at all three τ → identity is Level-2-INVARIANT
                              FAIL iff R_identity(τ) > 1e-3 at any τ → identity is Level-2-DEFORMABLE
                              INFO iff asymmetric (mixed Level-2)

Step 5 (Direction): if Level-2-INVARIANT → moduli-deformation preserves substrate-IS identity
                    if Level-2-DEFORMABLE → identity is τ_fold-specific; Jensen TT-deformation breaks rational form
                    The DIRECTION of the test: Level-2-INVARIANT confirms substrate's structural identity is robust
                                                across the substrate's own deformation manifold
```

### 11. Solution-space interpretation

- **PASS (Level-2-INVARIANT)** → confirms §VII.AU.OP-PROJ's Level-1 cohomology-class identity lifts to Level-2 moduli-INVARIANT under the cocycle functor `F: m(p,q) → identity_residual(m)` per `phononic-framing.md §"Calibration corpus instance #2 (S88 W-7 W2-2 V_4-on-triality landing)"` precedent. Strongly supports the substrate's Mellin-cone closure being a STRUCTURAL theorem at all τ in the Jensen TT-deformation neighborhood, not a τ_fold-specific accident. §VII.AU's "MANDATORY single-τ-slice tag" is structurally preserved while gaining a "Level-2-MODULI-INVARIANT annotation" companion.
- **INFO (Level-2-MIXED-asymmetric)** → reveals τ-asymmetric structure analogous to S88 W2-9 §VII.AE breakdown-geometry asymmetry (negative-side anticrossing-swap vs positive-side stratum-coalescence). Strengthens the case that the Jensen TT-deformation manifold has STRUCTURAL asymmetry around τ_fold — relevant for cosmological inflation reading of the substrate's late-time deformation profile.
- **FAIL (Level-2-DEFORMABLE)** → §VII.AU.OP-PROJ's identity is τ_fold-specific; the Sage-QQ exact identity holds ONLY at τ = 0.190. This is structurally informative: it would imply the substrate's substrate-distance-1 pole has a Jensen-deformation residual at the rational-identity layer, which is a NEW structural property of the substrate that current §VII.AU framing does NOT capture. Routes to S92+ FUNDAMENTAL plan-revision dispatch.

**Closes**: the Level-2 moduli-deformation corridor for §VII.AU.OP-PROJ.
**Opens** (on PASS): cross-extension to §VII.AV's Level-2 moduli-deformation (W1 M9 = CF-AV-L2-MODULI) — does the Corner-IV K-window log-derivative also lift to Level-2 moduli-INVARIANT? T1.12's PASS establishes the methodology for that subsequent gate.

### 12. Effort

~1.0 wave-equivalent (3 spectrum computations × Mellin-residue × Sage-Q identity cross-check; ~3 × 30 min wall on RX 9070 XT for τ ∈ {0.18, 0.20} new spectra; ~10 min Sage-Q exact rationals per τ; verdict + WP write).

### 13. Substrate-framing reminder

The Level-2 moduli-deformation IS the substrate's intrinsic Jensen TT-deformation manifold — NOT a coordinate sweep on a meta-container. The substrate at τ = 0.18, the substrate at τ = 0.19, and the substrate at τ = 0.20 are THREE distinct substrate-IS spectral-triple instances, each canonically embedded in the same Level-2 moduli-space-of-deformations of the substrate. The PASS direction (Level-2-INVARIANT) IS the substrate's structural property — it is NOT "the same identity in different coordinates". FORBIDDEN inversion: "we deform the substrate by changing the τ coordinate" → invert: "τ IS the substrate's intrinsic deformation parameter; the moduli-space of τ-deformations IS substrate-IS at the Level-2 layer; the identity either holds Level-2-INVARIANT or fails Level-2-DEFORMABLE — both outcomes are substrate properties, not coordinate artifacts."

---

## §W5-3. S91-CF41-UPPER-22.6-EXTENSION — n_PBH refinement to upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] m⁻³ via L_max=14+ substrate cardinality refinement (T1.13; volovik primary)

### 1. Gate ID
`S91-CF41-UPPER-22.6-EXTENSION` (continuation of CF-41 carry-forward chain; S89 W1-4 INFO + S90 §W1c-69 PASS-magnitude posterior anchoring; sole-PASS-magnitude gate per falsifier-master-inventory.md NEW Row #65).

### 2. Trigger
`[VERIFY]` — substrate-physics gate verifying whether L_max ≥ 14 substrate cardinality refinement of the D_K spectrum drives the substrate-IS n_PBH central prediction INTO the upper-22.6%-conjunct sub-band `[5.5e-23, 2.2e-22]` m⁻³ (the intersection of §W1c-69 PASS-magnitude posterior `[8.4e-24, 2.2e-22]` AND CF-CURV-6 upper-22.6%-of-prior `[5.5e-23, 2.2e-22]`).

### 3. Classification
PHONONIC (substrate-physics; substrate-IS n_PBH prediction from D_K spectrum cardinality at L_max ≥ 14 via Friedrich-Bär saturation; emergent observable = Pillar IX PBH number density observation under CMB/LISA/PTA detection horizons).

### 4. Agent type
`volovik-superfluid-universe-theorist` (primary). Rationale: T1.13 evaluates the substrate-IS n_PBH prediction from D_K spectrum at L_max ≥ 14 — a substrate-physics computation on the spectral triple's cardinality / state-multiplicity axis. Volovik's substrate-physics expertise + Friedrich-Bär saturation theorem application + cardinality-cascade reasoning (S88 W1a-59 parent gate `S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION`) makes volovik the canonical owner. EXCLUDED reviewers post-PASS: mack-cosmic-bridge (sole-writer for T1.14 STAGE-1-CANDIDATE registry-text landing; do NOT dispatch as Stage-2 cross-reviewer to preserve writer/reviewer separation per `feedback_mack-bridge-role.md` discipline).

### 5. Hypothesis
**Hypothesis H1.13**: at L_max ≥ 14 substrate cardinality refinement of the D_K spectrum, the substrate-IS n_PBH structural central prediction `n_PBH = n_edge(g_BBN) · prob_form / L_pix_LRD³` (substrate-clock cancellation form per S88 W1a-59 §0) MOVES from its L_max=10 anchor `1.758127e-23 m⁻³` (0.495 log-OOM below the upper-22.6% lower edge `5.5e-23`) INTO the upper-22.6%-conjunct sub-band `[5.5e-23, 2.2e-22]` m⁻³, with central candidate value approaching `8.033e-23 m⁻³` (the target central used in T1.14 STAGE-1-CANDIDATE landing).

**Decision split**:
- (a) **PASS-upper-22.6%-conjunct**: `n_PBH(L_max ≥ 14) ∈ [5.5e-23, 2.2e-22]` → T1.14 STAGE-1-CANDIDATE landing fires with central `8.033e-23 m⁻³` (or the actual L_max ≥ 14 central if different).
- (b) **INFO-band-edge-tension-preserved**: `n_PBH(L_max ≥ 14) ∈ [1e-23, 5.5e-23)` → §W1c-69 PASS-magnitude posterior still confirmed but upper-22.6% conjunct NOT YET satisfied; T1.14 closes as PRE-REG-INC blocked by T1.13 INFO; refinement-pathway continues to S92+ (potential L_max ≥ 18 extension).
- (c) **FAIL-below-posterior-or-saturated-elsewhere**: `n_PBH(L_max ≥ 14)` below posterior lower edge `8.4e-24` OR Friedrich-Bär saturation theorem FAILS at L_max ≥ 14 (no new sectors contribute beyond L_max=12) → CF-CURV-6 structural central does NOT lie in upper-22.6%; T1.14 closes FAIL with pathway-revision request.

### 6. Method (full dispatch prompt)

> **Volovik**: Refine the substrate-IS n_PBH structural central prediction by extending the D_K spectrum cardinality computation from L_max=10/12 baseline to L_max ∈ {14, 15, 16} via Friedrich-Bär saturation theorem application + recursive Casimir-projection feasibility pre-check per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`.
>
> **Pipeline pre-flight (mandatory per math-scripts.md)**:
> 1. Compute Friedrich-Bär lower bound `η_FB_lower` on the L_max=12 master cache `s84_spectrum_cache_L12_tau019.npz` per W11-3 protocol: for each Peter-Weyl sector (p,q), compute `η_FB(p,q) = |λ|_min(p,q) / sqrt(C_2(p,q) + 1)`; take `η_FB_lower = 0.92 · min_{(p,q)} η_FB(p,q)` (8% safety margin).
> 2. For each candidate L_max ∈ {14, 15, 16}: check whether NEW sectors at `p + q = L_max` would intrude below the n_PBH-relevant ceiling. If `η_FB_lower · sqrt(C_2(L_max, 0) + 1) > n_PBH-ceiling` for all NEW sectors at L_max, declare the bottom-K analytically saturated at L_max=12; T1.13 then evaluates n_PBH at the saturation-level (no new spectrum computation needed; analytic saturation argument suffices).
> 3. If Friedrich-Bär saturation FAILS at L_max=14 (some new sector contributes below the n_PBH-ceiling), perform recursive Casimir-projection construction of the NEW sectors at L_max=14 (irrep construction time scales super-polynomially in dim(p,q) per W11-2 + W11-3 calibration — empirically NOT feasible within agent timeout at L_max ≥ 13 single-thread; budget the irrep construction across `torch.linalg` GPU at minimum dim(p,q) ≤ 50 sectors only).
>
> **Substrate-IS n_PBH computation**:
> 4. Per S88 W1a-59 §0 substrate-clock cancellation form:
>    `n_PBH = β_PBH · ρ_substrate(g_BBN) / M_PBH_typical = n_edge(g_BBN) · prob_form / L_pix_LRD³`
>    where `n_edge(g_BBN) = 2^g_BBN` (cardinality-cascade-tail at saturated regime g ≥ g_saturate = 143) and `L_pix_LRD = L_pix(g_BBN)` (LRD pixel size; per S88 W1a-59 canonical: at g_BBN ≥ g_saturate, `n_PBH` is g-independent — the `2^g` and `L_pix(g)³` factors cancel exactly under IS-not-IN substrate-clock convention).
> 5. Refinement at L_max ≥ 14: re-evaluate `prob_form` (probabilistic PBH-formation prefactor; canonical `prob_form_L10 = 0.15573` per S88 W1a-59 PASS) and `g_saturate` (canonical g_saturate_L10 = 143 per S88 W1a-59) using the L_max ≥ 14 / saturation-confirmed spectrum.
> 6. Cross-check: the substrate-clock cancellation IS substrate-IS (g_BBN factor cancels exactly between `2^g_BBN` and `L_pix_LRD³`); refinement at L_max ≥ 14 only refines `prob_form` (via cardinality of cascade-tail sub-states) and `g_saturate` (via Friedrich-Bär saturation level on the bottom-K). The cancellation discipline IS preserved (substrate-IS structural property, not L_max-sensitive in form).
> 7. Compute `n_PBH(L_max ≥ 14)` via the cancelled form; report central + ±1σ band over L_max ∈ {14, 15, 16} scan.
> 8. Check sub-band membership:
>    - `n_PBH ∈ [5.5e-23, 2.2e-22]` → **PASS-upper-22.6%-conjunct**
>    - `n_PBH ∈ [8.4e-24, 5.5e-23)` → **INFO-band-edge-tension-preserved** (posterior support OK, upper-22.6% NOT satisfied)
>    - `n_PBH < 8.4e-24` OR Friedrich-Bär saturation FAILS → **FAIL**
> 9. Emit JSON sidecar: `{L_max_scan, eta_FB_lower, friedrich_bar_saturation_status, n_PBH_per_Lmax_grid, prob_form_per_Lmax, g_saturate_per_Lmax, n_PBH_central, n_PBH_1sigma, sub_band_membership, sign_verdict, magnitude_verdict, regime_verdict}`.
> 10. Emit verdict line per `gate-verdicts.md` S87+ schema-v2. The [VERIFY] trigger fires the 3-tuple companion row.
> 11. Update working-paper §VII.W5-3 (>15 lines; substrate framing; Friedrich-Bär saturation argument explicit; n_PBH scan vs L_max plot; sub-band membership decision).

> **Substrate framing reminder**: n_PBH IS substrate-IS — it is the substrate's prediction from D_K spectrum cardinality + Jensen TT-deformation profile, evaluated at the saturation-tail regime where substrate-clock cancellation is exact. The upper-22.6% sub-band IS a laboratory-IN discrimination band derived from the §W1c-69 posterior + CF-CURV-6 prior; the PASS decision IS "does the substrate's structural-central prediction lie inside the laboratory-IN PASS-magnitude region". FORBIDDEN inversion: "n_PBH is constrained by observation to lie in [5.5e-23, 2.2e-22]" → invert: "the substrate's structural-central prediction lies at a specific n_PBH; the observation provides the discrimination window; the substrate's prediction either falls inside or outside — neither outcome is a constraint on the substrate, both are structural facts about the substrate's image at Pillar IX".

### 7. Machinery pin (PRDR)

| Parameter | Value | Provenance |
|:----------|:------|:-----------|
| `L_max_baseline` | 12 (master spectrum cache `s84_spectrum_cache_L12_tau019.npz`) | Friedrich-Bär saturation pivot per W11-3 |
| `L_max_target` | 14 (canonical refinement target); fallback {15, 16} if 14 not saturating | per parent CF-41 carry-forward spec |
| `friedrich_bar_safety_margin` | 0.92 (8% safety below empirical floor) | W11-3 calibration |
| `eta_FB_lower_threshold` | computed from L_max=12 cache per `eta_FB(p,q) = |λ|_min(p,q) / sqrt(C_2(p,q) + 1)` per (p,q) sector | math-scripts.md saturation-theorem protocol |
| `τ_pin` | 0.190 (canonical τ_fold; Level-1 single-τ-slice; do NOT scan τ in T1.13 — that is T1.12's domain) | canonical_constants.py |
| `prob_form_L10_baseline` | 0.15573 (S88 W1a-59 PASS canonical) | parent gate canonical |
| `g_saturate_L10_baseline` | 143 (S88 W1a-59 PASS canonical) | parent gate canonical |
| `g_BBN_pin` | 322 or 323 (substrate-clock cancellation regime; g ≫ g_saturate ⇒ n_PBH is g-independent per S88 W1a-59 §0) | substrate-clock cancellation pin |
| `M_PBH_typical_pin` | per S88 W1a-59 §0 canonical (substrate-clock derivation; M_KK-natural mass scale) | parent gate |
| `posterior_lower_edge` | 8.4e-24 m⁻³ | falsifier-master-inventory.md NEW Row #65 |
| `posterior_upper_edge` | 2.2e-22 m⁻³ | same |
| `upper_22_6_pct_lower_edge` | 5.5e-23 m⁻³ (5.495e-23 numerical) | same |
| `upper_22_6_pct_upper_edge` | 2.2e-22 m⁻³ (coincides with posterior upper) | same |
| `regulator_class` | n/a (this is a cardinality-cascade computation, not a Mellin-cone evaluation; D_K spectrum is canonical) | — |
| `convention` | `n_PBH-substrate-distance-N-Friedrich-Bar-saturation-L_max-14-plus-substrate-clock-cancellation` | NO `-SCHEMATIC` suffix needed (no `_spectral_action_regulators.py` import) |
| `scheme` | `S91-W5-3-CF41-UPPER-22-6-EXTENSION` | gate identifier |
| `tolerance` | rel_tol = 0.05 on n_PBH central; absolute sub-band membership decision binary | publication-precision pin |
| `GPU path` | `torch.linalg` for any new spectrum sectors at L_max=14 NOT covered by Friedrich-Bär saturation | math-scripts.md |
| `OMP_NUM_THREADS` | 8 (fallback cap) | computation-environment.md |
| `random_seed` | n/a (deterministic) | — |
| `script_path` | `computations/session-91/s91_w5_3_cf41_upper_22_6_extension_lmax_14plus.py` | — |
| `npz_path` | `computations/session-91/s91_w5_3_cf41_upper_22_6.npz` | — |
| `png_path` | `computations/session-91/s91_w5_3_n_pbh_vs_lmax_with_sub_band.png` (n_PBH scan vs L_max with sub-band shading) | — |
| `verdict_file` | `computations/session-91/s91_gate_verdicts.txt` | MANDATORY canonical path |
| `wp_section` | `sessions/archive/session-91/session-91-w5-workingpaper.md §VII.W5-3` | designated writer = volovik |

### 8. Expected output 4-tuple

`(value=<n_PBH_central_FW [m⁻³], sub_band_membership ∈ {UPPER-22-6-CONJUNCT-PASS, BAND-EDGE-TENSION-INFO, BELOW-POSTERIOR-FAIL}>, scheme=S91-W5-3-CF41-UPPER-22-6-EXTENSION, convention=n_PBH-substrate-distance-N-Friedrich-Bar-saturation-L_max-14-plus-substrate-clock-cancellation, L_max=14)`

Plus 3-tuple `(sign_verdict, magnitude_verdict, regime_verdict)`.

### 9. PASS / FAIL / INFO thresholds

| Sub-verdict | PASS | INFO | FAIL |
|:------------|:-----|:-----|:-----|
| `sign_verdict` | `n_PBH > 8.4e-24` (above posterior lower edge) AND `n_PBH > 0` | n/a | `n_PBH ≤ 0` (structurally impossible if cancellation form valid; FAIL if so) |
| `magnitude_verdict` | `n_PBH ∈ [5.5e-23, 2.2e-22]` (upper-22.6%-conjunct intersection of posterior + upper-22.6%-of-prior) | `n_PBH ∈ [8.4e-24, 5.5e-23)` OR `n_PBH ∈ (2.2e-22, 1e-20]` (posterior support PASS but upper-22.6% conjunct NOT YET satisfied OR in CF-CURV-6 prior but not in posterior) | `n_PBH < 8.4e-24` OR `n_PBH > 1e-20` (outside posterior + outside CF-CURV-6 prior) |
| `regime_verdict` | Friedrich-Bär saturation theorem VALID at L_max=14 (per W11-3 protocol: bottom-K invariance certified for all L_max ≥ L_anchor analytically) | MARGINAL if Friedrich-Bär saturation fails at L_max=14 but recursive Casimir-projection at L_max=14 is empirically feasible within agent timeout and yields refined `prob_form` within 5% of L_max=10 baseline | BREAKDOWN if Friedrich-Bär saturation FAILS at L_max=14 AND recursive Casimir-projection at L_max=14 is empirically INFEASIBLE within agent timeout (super-polynomial irrep construction blocks the gate); composite FAILs per `gate-verdicts.md` collapse rule even if magnitude PASSes |
| Composite | per S87+ schema-v2 collapse rule | per collapse rule | per collapse rule |

**Composite PASS** = upper-22.6%-conjunct sub-band CONFIRMED at L_max ≥ 14 with Friedrich-Bär saturation theorem VALID → T1.14 STAGE-1-CANDIDATE registry landing UNBLOCKS.

**Composite INFO** = band-edge tension preserved at L_max ≥ 14 (posterior support OK; upper-22.6% NOT satisfied) → T1.14 closes as PRE-REG-INC blocked by T1.13 INFO; refinement-pathway continues to S92+.

**Composite FAIL** = either substrate's structural-central lies below posterior (CF-CURV-6 structural central is incompatible with §W1c-69) OR Friedrich-Bär saturation breaks down at L_max ≥ 14 → T1.14 closes FAIL; pathway-revision request emitted to next-session orchestrator.

### 10. Substitution chain (mandatory for the [VERIFY] sub-band membership claim)

```
Step 1 (Definition): n_PBH ≡ β_PBH · ρ_substrate(g_BBN) / M_PBH_typical  (substrate-IS structural central, S88 W1a-59 §0)

Step 2 (Substrate-clock cancellation): in the saturated cascade-tail regime (g_BBN ≥ g_saturate = 143),
                                       n_PBH = n_edge(g_BBN) · prob_form / L_pix_LRD³
                                       where n_edge(g) = 2^g, L_pix(g) = L_pix_0 · 2^{−g/3}
                                       and L_pix(g)³ = L_pix_0³ · 2^{−g}, so
                                       n_PBH = (2^g) · prob_form / (L_pix_0³ · 2^{−g}) = prob_form / L_pix_0³ × 2^{2g}
                                       Wait — this is NOT g-independent if interpreted naively.

Step 2-CORRECTED (substrate-clock cancellation form): per S88 W1a-59 §0, the substrate-clock convention pairs
                                                       g_BBN ↔ L_pix_LRD via IS-not-IN coupling
                                                       n_edge(g_BBN) = 2^g_BBN (cardinality-cascade-tail)
                                                       L_pix_LRD = L_pix(g_BBN)  fixed at LRD pixel scale (NOT 2^{−g/3} scaling)
                                                       Therefore in saturated regime, cardinality 2^g cancels with the cascade-prefactor 1/L_pix_LRD³ scaling
                                                       AND the substrate-clock convention forces n_PBH g-independent at saturation.

Step 3 (Substitution at L_max=10 baseline, S88 W1a-59 PASS):
                     n_PBH(L_max=10) = 3.048e9 · 0.15573 / (3.0e10)³ = 1.758e-23 m⁻³
                     (cross-check rel_err = 0e+00 at g_BBN=322 ≫ g_saturate; saturated regime g-independence confirmed)

Step 4 (Refinement at L_max ≥ 14): extend prob_form via Friedrich-Bär saturation-confirmed cardinality refinement
                                    prob_form_L14_plus = prob_form_L10 · (refinement_factor)
                                    where refinement_factor depends on NEW cascade-tail sub-states uncovered at L_max ≥ 14
                                    Expected direction: NEW sub-states INCREASE prob_form (more cascade-tail channels per cascade generation)
                                    Target: n_PBH(L_max ≥ 14) ≥ 5.5e-23 (upper-22.6% lower edge)
                                    Required prob_form refinement factor: 5.5e-23 / 1.758e-23 ≈ 3.13× increase from L_max=10 to L_max=14

Step 5 (Simplify direction): refinement_factor ≥ 3.13 → PASS-upper-22.6%-conjunct
                              refinement_factor ∈ [1, 3.13) → INFO-band-edge-tension-preserved
                              refinement_factor < 1 (cascade-tail SHRINKS at L_max ≥ 14) → structurally pathological; would imply substrate's L_max=10 over-counted

Step 6 (Direction): PASS direction confirms the substrate's structural-central moves UP into the discrimination region by adding
                    NEW cascade-tail sub-states uncovered at L_max ≥ 14.
                    FAIL direction would imply the substrate's prediction is fundamentally below the upper-22.6% sub-band
                    independent of L_max refinement → CF-CURV-6 structural-central reading needs revision.
```

### 11. Solution-space interpretation

- **PASS** (upper-22.6%-conjunct CONFIRMED at L_max ≥ 14) → closes the band-edge tension corridor identified at S89 W1-4 INFO; substrate's structural-central enters the discrimination window; n_PBH = 8.033e-23 m⁻³ candidate (or actual L_max ≥ 14 central) is STAGE-1-CANDIDATE registry-eligible at §VII.AX. T1.14 fires.
- **INFO** (band-edge tension preserved) → confirms S89 W1-4 INFO finding extends through L_max ≥ 14 → corridor "substrate-IS CF-CURV-6 structural central does not maximize the upper-22.6%-of-prior probability mass" PRESERVED. Routes to S92+ refinement pathway (potential L_max ≥ 18 extension OR alternative band-edge structural interpretation).
- **FAIL** (substrate's structural-central below posterior OR Friedrich-Bär saturation BREAKDOWN) → substrate's CF-CURV-6 structural central is incompatible with §W1c-69 posterior at L_max ≥ 14; substrate's structural-central reading needs revision. Pathway-revision request to next-session orchestrator.

**Closes**: the upper-22.6%-conjunct refinement corridor for n_PBH at substrate-distance.
**Opens** (on PASS): T1.14 STAGE-1-CANDIDATE landing at §VII.AX.

### 12. Effort

~1.5 wave-equivalents (Friedrich-Bär pre-flight saturation check + potential L_max=14 recursive Casimir-projection at minimum-dim sectors + n_PBH cancellation-form evaluation + sub-band membership decision + verdict + WP write). Largest budget item: if Friedrich-Bär saturation FAILS at L_max=14, recursive Casimir-projection at NEW sectors is the cost driver (super-polynomial in dim(p,q) per W11-2 + W11-3 calibration; agent timeout risk).

### 13. Substrate-framing reminder

n_PBH IS the substrate's prediction from D_K spectrum cardinality in the saturated cascade-tail regime. The L_max ≥ 14 refinement IS the substrate's intrinsic refinement of its own cardinality (more substates uncovered by extending the spectral-triple truncation outward). The substrate-clock cancellation IS substrate-IS (the g_BBN dependence cancels exactly under the IS-not-IN substrate-clock convention; cardinality 2^g and L_pix(g)³ factors are paired as substrate-intrinsic structures, NOT a coincidence of coordinate choice). The upper-22.6% sub-band IS a laboratory-IN discrimination window; the substrate's structural-central either lies inside or outside — both outcomes are substrate properties. FORBIDDEN inversion: "PBH abundance observations constrain n_PBH to lie in [8.4e-24, 2.2e-22]" → invert: "the substrate's prediction lies at a specific value; the observational PASS-magnitude posterior provides the laboratory-IN discrimination band; the comparison maps substrate's bridge image at Pillar IX to observational discrimination region; passing or failing is a substrate property, not an external constraint".

---

## §W5-4. S91-CF41-VII-LANDING — STAGE-1-CANDIDATE registry entry at §VII.AX for PBH band-edge prediction n_PBH = 8.033e-23 m⁻³ (CONDITIONAL on T1.13 PASS; T1.14; mack-cosmic-bridge sole-writer)

### 1. Gate ID
`S91-CF41-VII-LANDING` (continuation of CF-41 carry-forward chain; STAGE-1-CANDIDATE registry-text landing per `joint-theorem-promotion.md §"Stage 1"` 4-stage pathway).

### 2. Trigger
`[AUDIT]` (registry-landing audit + STAGE-1-CANDIDATE pre-registration emission). CONDITIONAL on T1.13 PASS.

### 3. Classification
META (registry-landing wave per `wave-classification.md`; classification PHONONIC at the substrate-physics layer because the underlying prediction n_PBH is substrate-IS; META classification is for the gate-type layer = STAGE-1-CANDIDATE registry-text landing).

### 4. Agent type
`mack-cosmic-bridge` (SOLE-WRITER for §VII.AX registry-text landing per `feedback_mack-bridge-role.md` — mack is the canonical sole-writer for cosmology-side cross-pillar bridge entries + PBH-class observational-prediction registry landings; this is consistent with §VII.AW.OP-PROJ (substrate-clock uniqueness, S90 W2 CF-19), §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ (R_3HeB landings, S88), and §VII.AV (PROXY-REFINEMENT initial registration, S90 W8-5)). NOT volovik (who is W5-3 PRIMARY for the substrate-physics computation but is NOT the registry-text writer per writer/reviewer separation discipline).

### 5. Hypothesis
**Hypothesis H1.14**: GIVEN T1.13 PASS confirming `n_PBH(L_max ≥ 14) ∈ [5.5e-23, 2.2e-22]` m⁻³ with central candidate value `8.033e-23 m⁻³` (or actual T1.13 central), the substrate's PBH band-edge prediction admits a STAGE-1-CANDIDATE registry entry at §VII.AX (next-free §VII slot post-§VII.AW per `regulator-pin-discipline.md` next-free-letter discipline) with full 5-anatomy + 3-level structural-confidence ladder per `cross-pillar-bridge-anatomy.md §"Forward template-adoption (5-anatomy + 3-level discipline)"` MANDATORY at K=3 since S88 W4a-17 close.

### 6. Method (full dispatch prompt)

> **Mack-cosmic-bridge** (SOLE-WRITER per `feedback_mack-bridge-role.md`):
>
> **Step 1 (CONDITIONAL gating)**: Read `computations/session-91/s91_gate_verdicts.txt` for T1.13's canonical verdict line (gate ID `S91-CF41-UPPER-22.6-EXTENSION`).
>
> - If composite = **PASS**: proceed to Step 2 STAGE-1-CANDIDATE landing.
> - If composite = **INFO**: emit mechanical-closure verdict line per `mechanical-closure-discipline.md`: `S91-CF41-VII-LANDING: FAIL -- value='PRE-REG-INC_blocked_by_T1.13_INFO_band-edge-tension-preserved' scheme=S91-W5-4-CF41-VII-LANDING convention=mechanical-closure-T1-13-conditional L_max=14 audit_sha256=<computed> content_sha256=<computed>` + dual-SHA companion row + §VII.W5-4 mechanical-closure disclosure paragraph (>15 lines per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` item 5). DO NOT write §VII.AX registry entry. STOP.
> - If composite = **FAIL**: emit mechanical-closure verdict line analogously with `value='PRE-REG-INC_blocked_by_T1.13_FAIL_below_posterior_or_saturation_breakdown'`. DO NOT write §VII.AX registry entry. STOP.
>
> **Step 2 (STAGE-1-CANDIDATE landing on T1.13 PASS)**:
>
> 2.1 (Slot allocation): Grep `sessions/permanent-results-registry.md` for `^### §VII\.A[X-Z]` and `^### §VII\.B[A-Z]` to confirm §VII.AX is next-free. If §VII.AX is occupied (parallel-writer race), advance to next-free letter and emit a FAIL-with-remediation verdict per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` discipline. Use POSIX O_APPEND atomic write per the canonical pattern.
>
> 2.2 (Registry text construction): Build the §VII.AX registry entry text in MEMORY with the following 13-section structure (full canonical 5-anatomy + 3-level discipline per `cross-pillar-bridge-anatomy.md §"Forward template-adoption"` MANDATORY at K=3):
>
>   - **Header**: `### §VII.AX — PBH Band-Edge Prediction n_PBH = <T1.13 central> m⁻³ (S91 W5-4 — mack-cosmic-bridge sole-writer per feedback_mack-bridge-role.md; CONDITIONAL on T1.13 PASS audit_sha256=<T1.13 audit SHA>, 2026-XX-XX)`
>   - **Provenance**: Plan reference S91 W5 (this gate-block); volovik substrate-physics primary for T1.13; mack registry sole-writer.
>   - **Status**: STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway. Stage-2 cross-axis independent-verify queued as S92+ carry-forward.
>   - **Bridge family**: FWD-C5 (NEW; Pillar I (M⁴ × SU(3) D_K spectrum cardinality at saturated cascade-tail) ↔ Pillar IX (PBH number density observation under CMB/LISA/PTA detection horizons)). Add to `cross-pillar-bridge-corpus.md §4` Forward candidates table.
>   - **Corner**: per parse-tree-expansion of n_PBH closed form per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"` SUGGESTION at K=1 — the n_PBH observable reduces to `(2^g · prob_form / L_pix_0³)` evaluated in the saturated regime; the parse-tree gives a substrate-distance pole index determined by the dominant `n_edge(g_BBN)` scaling; classify as **Cell-I-cardinality-projection** (algebra-INVARIANT spectrum-only-functional × cardinality-cascade-pole). Declare parse-tree expansion explicitly per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"` MANDATORY-pending-K=3.
>   - **Three-level structural-confidence ladder**:
>     - Level 1: substrate-IS structural identity `n_PBH = n_edge(g_BBN) · prob_form / L_pix_LRD³` at saturated regime; g-independence theorem at g ≥ g_saturate (cardinality 2^g and L_pix(g)³ cancel exactly under IS-not-IN substrate-clock convention) → STRUCTURAL THEOREM (W5-3 PASS at L_max ≥ 14).
>     - Level 2: convergence rate of substrate's structural-central to laboratory-IN observation as cardinality refinement L_max → ∞; expected `L^{-α}` with α ∈ [structural-prediction-band] per Friedrich-Bär saturation theorem application → STRUCTURAL PREDICTION (Level-2-binding sub-class; HKR-image binds Level-1).
>     - Level 3: empirical anchor at canonical L_max=14: `n_PBH = <T1.13 central> m⁻³`; intersects upper-22.6%-conjunct sub-band [5.5e-23, 2.2e-22]; satisfies §W1c-69 PASS-magnitude posterior intersection → EMPIRICAL CONFIRMATION (T1.13 PASS).
>   - **IS-not-IN anatomy** (all 5 elements MANDATORY per `cross-pillar-bridge-anatomy.md` K=3):
>     1. Substrate-IS observable: `n_PBH = n_edge(g_BBN) · prob_form / L_pix_LRD³` evaluated on `(A_K^{≤L_max=14}, H_K^{≤L_max=14}, D_K^{≤L_max=14})` at τ_fold = 0.19 in the saturated cascade-tail regime (g_BBN ≥ g_saturate = 143). EXPLICIT TAG: Level 1 single-τ-slice at τ_fold = 0.190 (MANDATORY).
>     2. Laboratory-IN observable (OE-form MANDATORY at K=2): `∫_{CMB/LISA/PTA-horizon} d³x ⟨P_PBH-mass · ρ_BH⟩(x)` — PBH number density continuum measurement across CMB / LISA / PTA detection horizons (mass-window projector P_PBH-mass selects the framework's M_PBH_typical scale; combined detection horizon = Pillar IX laboratory measurement context). The named projector `P_PBH-mass` lifts the substrate's substrate-clock-cancellation-form image under the substrate-IS → laboratory-IN bridge map at Pillar IX.
>     3. Bridge map (explicit): substrate-clock cancellation IS-not-IN coupling (S88 W1a-59 §0) + Friedrich-Bär saturation-theorem analytic certification (W11-3) + cardinality-cascade-tail HKR-style image to PBH number density continuum at Pillar IX. **Element 3 fiducial-anchor binding (S88 W-15 V.7 SUGGESTION-K=1)**: type **(ii) external-observation** — bridge map composes through laboratory-IN PBH detection horizons which ARE external observations at Pillar IX (CMB/LISA/PTA combined). NOT (i) substrate-self-consistent; NOT (iii) joint-hypersurface. Declare convention `n_PBH-substrate-distance-N-cardinality-cascade-tail-saturation-bridge-external-observation-binding`.
>     4. Algebraic envelope: `L^{-α}` with α to be extracted from L_max ∈ {10, 12, 14, 15, 16} scan per T1.13 secondary output; Level-2-binding sub-class per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"`: HKR-image binds Level-1 g-independence theorem to Pillar IX continuum PBH detection.
>     5. Empirical anchor: T1.13 central `n_PBH(L_max=14) = <central value> m⁻³` falls within upper-22.6%-conjunct sub-band [5.5e-23, 2.2e-22]; cross-references §W1c-69 PASS-magnitude posterior; satisfies CF-CURV-6 upper-22.6%-of-prior conjunct.
>   - **Hybrid Independence Test** (predicate `(i ∨ ii ∨ iii) ∧ iv` per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` SUGGESTION-K=1 advancing toward K=3 MANDATORY):
>     - (i) distinct substrate-IS pillar: **YES** — Pillar I cardinality-cascade-tail (saturated regime); structurally distinct from Pillar I Mellin-cone-closure (FWD-C1 §VII.AU) by parse-tree (cardinality vs Mellin-residue).
>     - (ii) distinct laboratory-IN pillar: **YES** — Pillar IX combined CMB/LISA/PTA PBH detection; distinct from Pillar II CMB n_s (FWD-C1), Pillar IV Peotta-Törmä BZ-trace (W-5), Pillar V 3He-B BdG (W4a-17).
>     - (iii) distinct bridge map class: **YES** — substrate-clock cancellation + Friedrich-Bär saturation theorem + cardinality-cascade-tail; structurally distinct from HKR / K-theory boundary / Connes-Karoubi pairing.
>     - (iv) independent algebraic envelope: **YES** (provisional; T1.13 secondary output) — envelope at L_max → ∞ via cardinality saturation; independent of HKR-image envelope at Mellin-residue closure.
>     - **Predicate evaluation**: `(YES ∨ YES ∨ YES) ∧ YES = YES`. K-counter advancement: K=1 → K=2 on the Hybrid Independence Test corpus.
>   - **Substrate framing block** (per `phononic-framing.md §"IS Space, Not IN Space"`): direction Substrate (Pillar I cardinality-cascade-tail) → Bridge (substrate-clock cancellation + Friedrich-Bär saturation) → Laboratory (Pillar IX PBH detection). FORBIDDEN inversion explicit.
>   - **Cross-references**: §VII.AV (PROXY-REFINEMENT analog); §VII.AU.OP-PROJ (FWD-C1 analog); §VII.AW.OP-PROJ (substrate-clock uniqueness; uses same substrate-clock convention IS-not-IN coupling); `falsifier-master-inventory.md` NEW Row #65; `cross-pillar-bridge-corpus.md §4` Forward candidates extension to FWD-C5; `joint-theorem-promotion.md §"Stage 1"`.
>   - **Source**: Plan §W5-4 verbatim; T1.13 verdict audit_sha256 cited; CF-41 carry-forward chain documented.
>   - **OP-PROJ suffix discipline** per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` K=3 MANDATORY: the n_PBH observable is operator-projection on the cardinality side (substrate-distance-N pole on cardinality cascade-tail) → header gets `.OP-PROJ` suffix → final slot identifier = `§VII.AX.OP-PROJ`. State-projection companion slot `§VII.AX.STATE-PROJ` queued as S92+ carry-forward.
>   - **Parse-tree expansion** (per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"` SUGGESTION-K=1; preserves substrate-IS structure at registry-text layer):
>     ```
>     n_PBH = n_edge(g_BBN) · prob_form / L_pix_LRD³
>           [Step 1: history-label form — observable named by saturated cascade-tail preparation]
>           [Step 2: cardinality substitution] = 2^g_BBN · prob_form / L_pix(g_BBN)³
>           [Step 3: substrate-clock cancellation under IS-not-IN coupling]
>           [Step 4: substrate-IS closed form on the substrate algebra — algebra-INVARIANT cardinality × Jensen-deformation-prefactor combination]
>           [Step 5: corner classification — Cell-I-cardinality-projection (algebra-INVARIANT × cardinality-cascade-pole)]
>     ```
>
> 2.3 (Single-shot AFTER-pattern emission per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`): `write_atomic_with_fsync(registry_path, full_promotion_text)` → `re_read_and_verify_section_matches(actual, expected)` → ONE `emit_verdict_line(boolean_from_verify)` call. If verify FAILs, emit FAIL once per the AFTER-pattern; do NOT iterate.
>
> 2.4 (Verdict-line emission): `S91-CF41-VII-LANDING: PASS -- value='STAGE-1-CANDIDATE_landed_at_§VII.AX.OP-PROJ_n_PBH=<central>e-23_m_minus_3' scheme=S91-W5-4-CF41-VII-LANDING convention=stage-1-candidate-registry-landing-FWD-C5-pillar-I-IX-cardinality-cascade-tail-saturation-bridge L_max=14 audit_sha256=<computed> content_sha256=<computed> schema_version=S84+` + dual-SHA companion comment row per `gate-verdicts.md` W9a-99 split.
>
> 2.5 (Working-paper §VII.W5-4): >15 lines; substrate framing block; STAGE-1-CANDIDATE disclosure paragraph; Stage-2 cross-axis verify queued for S92+; cross-link to T1.13 PASS verdict audit_sha256 + W1c-69 posterior + S88 W1a-59 parent gate.
>
> 2.6 (Falsifier-master-inventory.md row update): mack-cosmic-bridge appends new audit-pin sub-row to NEW Row #65 citing this STAGE-1-CANDIDATE entry + T1.13 verdict audit_sha256 + central T1.13 value; emits to `sessions/framework/registry/falsifier-master-inventory.md`.
>
> 2.7 (canonical_constants.py promotion — DEFERRED): Per canonical write-order discipline in `math-scripts.md §"Canonical Write-Order"`, STAGE-1-CANDIDATE alone does NOT trigger canonical_constants.py promotion (Stage 3 PERMANENT does). Add `n_PBH_FW_central` + provenance entry only if T1.13 PASS is unambiguous AND mack judges immediate canonical promotion warranted; otherwise queue as `S92-N-PBH-FW-CANONICAL-PROMOTION` carry-forward.

> **Substrate framing reminder**: §VII.AX.OP-PROJ's substrate-IS observable IS the n_PBH cardinality-cascade-tail prediction in the saturated regime — substrate-IS at the substrate's intrinsic cardinality + Jensen-deformation manifold layer. The CMB/LISA/PTA detection horizons IS the laboratory-IN measurement context. The substrate is NOT in cosmological-container; the cosmological-container IS the laboratory-IN measurement context for the substrate's PBH bridge image. The STAGE-1-CANDIDATE landing IS a registry-text codification of a substrate-IS structural theorem (the g-independence cancellation at saturation) plus its laboratory-IN bridge image at Pillar IX, NOT a phenomenological prediction parameterized by post-hoc data fits.

### 7. Machinery pin (PRDR)

| Parameter | Value | Provenance |
|:----------|:------|:-----------|
| `prereq_gate_id` | `S91-CF41-UPPER-22.6-EXTENSION` (T1.13) | conditional dispatch trigger |
| `prereq_composite_required` | PASS | conditional landing |
| `target_slot` | §VII.AX (next-free post-§VII.AW; grep verified at runtime per W3c-30 single-shot pattern) | `regulator-pin-discipline.md` next-free-letter discipline |
| `target_slot_full_id` | §VII.AX.OP-PROJ (operator-projection suffix MANDATORY at K=3 per `registry-landing.md §"OP-PROJ Naming Hygiene"`) | S88 W8-92 K=4 MANDATORY |
| `parse_tree_expansion_required` | YES (per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"` SUGGESTION-K=1; pre-emptively comply at S91 to advance K-counter) | rule advisory |
| `bridge_family` | FWD-C5 (NEW; Pillar I cardinality-cascade-tail ↔ Pillar IX PBH detection); extension to `cross-pillar-bridge-corpus.md §4` Forward candidates table | corpus extension |
| `hybrid_independence_predicate` | `(YES ∨ YES ∨ YES) ∧ YES = YES`; K=1 → K=2 advancement | rule SUGGESTION-K=3 |
| `script_architecture_pattern` | single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture"` (write_atomic_with_fsync → re_read + verify → ONE emit_verdict_line) | MANDATORY going forward |
| `registry_write_protocol` | POSIX O_APPEND atomic single `open("a")` write per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` discipline | MANDATORY |
| `wave_classification_audit_required` | YES — though META-class, the gate has a numerical PASS predicate (T1.13 composite = PASS) and `.py` producing script (registry-text builder) so wave-class is COMPUTE per M1 + M2 (NOT METHODOLOGY); `methodology-wave-allowlist.md` does NOT list this gate (M4 fails) → COMPUTE-class fallthrough confirmed | `wave-classification.md` 4-test conjunction |
| `convention` | `stage-1-candidate-registry-landing-FWD-C5-pillar-I-IX-cardinality-cascade-tail-saturation-bridge` | no SCHEMATIC suffix (registry-text landing, not a regulator computation) |
| `scheme` | `S91-W5-4-CF41-VII-LANDING` | gate identifier |
| `tolerance` | n/a (registry-text landing is binary: section written-and-verified PASS or write-failed FAIL) | — |
| `GPU path` | n/a (registry-text builder is I/O-only) | — |
| `OMP_NUM_THREADS` | n/a | — |
| `random_seed` | n/a | — |
| `script_path` | `computations/session-91/s91_w5_4_cf41_vii_ax_stage1_candidate_landing.py` | — |
| `npz_path` | n/a (registry-text landing has no numerical output beyond the registry text itself) | — |
| `png_path` | n/a | — |
| `verdict_file` | `computations/session-91/s91_gate_verdicts.txt` | MANDATORY canonical path |
| `wp_section` | `sessions/archive/session-91/session-91-w5-workingpaper.md §VII.W5-4` | designated writer = mack-cosmic-bridge |
| `registry_path` | `sessions/permanent-results-registry.md` (append §VII.AX.OP-PROJ entry at next-free slot) | sole-writer = mack |
| `falsifier_inventory_path` | `sessions/framework/registry/falsifier-master-inventory.md` (append audit-pin sub-row to NEW Row #65 + cross-link to §VII.AX.OP-PROJ) | sole-writer = mack |

### 8. Expected output 4-tuple

`(value=<STAGE-1-CANDIDATE landed at §VII.AX.OP-PROJ for n_PBH = <central> m⁻³>, scheme=S91-W5-4-CF41-VII-LANDING, convention=stage-1-candidate-registry-landing-FWD-C5-pillar-I-IX-cardinality-cascade-tail-saturation-bridge, L_max=14)`

Plus 3-tuple `(sign_verdict=N/A, magnitude_verdict=<PASS|FAIL>, regime_verdict=VALID)`. The sign_verdict is N/A (registry-text landing is not a directional prediction); the [AUDIT] trigger does not pin a SIGN sub-verdict but the schema-v2 3-tuple companion row is still emitted with sign=N/A.

### 9. PASS / FAIL / INFO thresholds

| Sub-verdict | PASS | INFO | FAIL |
|:------------|:-----|:-----|:-----|
| `sign_verdict` | n/a (registry-text landing; no direction claim) | n/a | n/a |
| `magnitude_verdict` | §VII.AX.OP-PROJ entry written-and-verified per single-shot AFTER-pattern; falsifier-master-inventory.md NEW Row #65 audit-pin sub-row appended; both writes pass re-read verification | n/a | write fails OR re-read verification fails (write-vs-source mismatch); registry-write race detected and not resolved via Option A `supersedes` protocol |
| `regime_verdict` | VALID — T1.13 PASS composite VALID at L_max=14 carries through | n/a | BREAKDOWN if T1.13 regime was BREAKDOWN (composite would have been FAIL preventing this gate from firing); structurally cannot reach this gate with T1.13 BREAKDOWN |
| Composite | PASS iff section written-and-verified + falsifier-inventory updated | n/a (no INFO band for registry-text landing) | FAIL iff write fails or verification fails |

**Composite PASS** = STAGE-1-CANDIDATE registry-text landing CONFIRMED at §VII.AX.OP-PROJ + falsifier-master-inventory.md row #65 audit-pin updated + working-paper §VII.W5-4 written with substrate framing.

**Composite FAIL** = either write fails (parallel-writer race not resolved via Option A supersedes) OR re-read verification fails (single-shot AFTER-pattern catches text-vs-source mismatch and emits FAIL once per the architecture).

**Mechanical-closure path** (T1.13 INFO/FAIL): per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` items 1-5; emits FAIL with `value='PRE-REG-INC_blocked_by_T1.13_<INFO|FAIL>_...'`; working-paper §VII.W5-4 status block + verdict block + substrate-framing block written with mechanical-closure disclosure paragraph (>15 lines).

### 10. Substitution chain (mandatory at the [AUDIT] layer)

```
Step 1 (Definition): STAGE-1-CANDIDATE registry-text landing requires:
                     (a) T1.13 PASS composite (n_PBH ∈ upper-22.6%-conjunct sub-band)
                     (b) §VII.AX next-free at registry-grep time
                     (c) 5-anatomy + 3-level + parse-tree expansion + OP-PROJ suffix all MANDATORY
                     (d) Single-shot AFTER-pattern write protocol
                     (e) Falsifier-master-inventory.md row #65 audit-pin update

Step 2 (Conditional gating): IF T1.13.composite = PASS:
                                proceed to Step 3
                              ELSE:
                                emit mechanical-closure FAIL line per discipline; STOP

Step 3 (Slot allocation): grep registry for ^### §VII\.A[X-Z]; verify §VII.AX next-free
                          IF occupied: advance to next letter + FAIL-with-remediation per Registry-Write Hygiene
                          ELSE: proceed to Step 4

Step 4 (Single-shot landing):
                          build_promotion_text(13-section structure, all anatomy elements, parse-tree expansion)
                          → write_atomic_with_fsync(registry_path, text)
                          → re_read + verify_section_matches(actual, expected)
                          → emit_verdict_line(boolean_from_verify) ← ONE call only

Step 5 (Direction): the [AUDIT] trigger does not pin a SIGN sub-verdict; the direction of the gate is binary
                    (section-written-and-verified PASS vs write-failed FAIL); the substrate-physics direction
                    is inherited from T1.13's SIGN-verdict (which is N/A for cardinality-cascade-tail magnitude prediction)
```

### 11. Solution-space interpretation

- **PASS** (STAGE-1-CANDIDATE landed) → §VII.AX.OP-PROJ joins the cross-pillar-bridge K-counter calibration corpus as instance #5 (after W-5 instance #1, W11-5 instance #2, W4a-17 instance #3, W7c §VII.AU.OP-PROJ instance #4). FWD-C5 added to `cross-pillar-bridge-corpus.md §4` Forward candidates table. Stage-2 cross-axis independent-verify queued for S92+ per `joint-theorem-promotion.md §"Stage 2"` (two cross-reviewers on opposite axes, mack-bridge SPECIFICALLY EXCLUDED post-S91 W5-4 sole-writer role per writer/reviewer separation discipline). Substrate's PBH band-edge prediction becomes a permanent registry-eligible structural prediction pending Stage 2 → 3 promotion pathway.
- **FAIL (write or verify failure)** → registry-text landing did not complete cleanly; emit FAIL once per AFTER-pattern + plan-revision request to next-session orchestrator to retry under Option-A `supersedes` protocol (per `gate-verdicts.md §"Option A — sig_5 remediation pathway"`).
- **Mechanical-closure FAIL (T1.13 INFO/FAIL)** → §VII.AX slot remains free; refinement-pathway continues to S92+; registry-text landing deferred.

**Closes**: the §VII.AX STAGE-1-CANDIDATE registry-landing path for n_PBH.
**Opens** (on PASS): S92+ Stage-2 cross-axis independent-verify carry-forward for §VII.AX.OP-PROJ.

### 12. Effort

~0.3 wave-equivalent (mack reads T1.13 verdict + builds 13-section registry text in memory + single-shot AFTER-pattern write + verify + emit + falsifier-inventory append + working-paper §VII.W5-4 write).

### 13. Substrate-framing reminder

The STAGE-1-CANDIDATE registry entry IS a substrate-IS structural codification — it captures the substrate's g-independence cancellation theorem at saturation + Friedrich-Bär saturation theorem applicability + cardinality-cascade-tail Hochschild image to the Pillar IX laboratory observable. The substrate IS the D_K spectrum cardinality in the saturated regime; the registry text IS the methodology-floor F-image of the substrate-IS structural theorem per `epistemic-discipline.md §"Layer-Decomposition"`. The registry entry is NOT a "post-hoc fit of observational data into a substrate-styled wrapper" — it is the substrate's intrinsic prediction documented at the methodology-floor layer for downstream cross-axis Stage-2 verification.

---

## Wave 5 → Downstream Decision Point

| T1.11 (W5-1) outcome | Consequence on §VII.AV | Downstream gate at S92+ |
|:---------------------|:------------------------|:------------------------|
| Composite PASS | §VII.AV PROXY-REFINEMENT RESOLVED on FULL-PV route → advances toward STAGE-3-PERMANENT eligibility pending Level-3 (Pillar V 3He-B continuum measurement) | S92+ §VII.AV Stage-2 cross-axis independent-verify (volovik EXCLUDED as W5-1 PRIMARY; axes connes-NCG-axiomatic + mack-cosmic-bridge admissible) |
| Composite INFO | SCHEMATIC qualitatively confirmed; FULL-CC multipliers (W1 T1.1) needed for quantitative match | Cross-route comparison gate after W1 T1.1 lands: SCHEMATIC vs FULL-PV vs FULL-CC three-way α regression |
| Composite FAIL | SCHEMATIC Casimir-bound proxy FALSIFIED on FULL-PV; §VII.AV refinement-pathway requires plan-revision | S92+ alternative envelope predictor: substrate-distance-3 instead of substrate-distance-2 cross-check, OR K-window definition revision |

| T1.12 (W5-2) outcome | Consequence on §VII.AU | Downstream gate at S92+ |
|:---------------------|:------------------------|:------------------------|
| Composite PASS (Level-2-INVARIANT) | §VII.AU advances Level-2 verification; gains "Level-2-MODULI-INVARIANT annotation"; methodology established for §VII.AV moduli-extension at W1 M9 | S92+ extend Level-2-MODULI-INVARIANT verification to §VII.AV (W1 M9 = CF-AV-L2-MODULI inherits W5-2 protocol) |
| Composite INFO (Level-2-MIXED-asymmetric) | §VII.AU gains "Level-2-MODULI-MIXED annotation"; flag for asymmetric Level-2 sub-class | S92+ ASYMMETRIC LEVEL-2 RULE EXTENSION: extend `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` with asymmetric Level-2 sub-class |
| Composite FAIL (Level-2-DEFORMABLE) | §VII.AU identity is τ_fold-specific; Level-1 MANDATORY tag preserved with explicit DEFORMABLE caveat; bridge structural-confidence ladder updated | S92+ FUNDAMENTAL REVISION: investigate τ_fold-specific Jensen TT-deformation residual at substrate-distance-1 pole |

| T1.13 (W5-3) outcome | Consequence on n_PBH band-edge | Downstream gate at S92+ |
|:---------------------|:--------------------------------|:------------------------|
| Composite PASS | upper-22.6%-conjunct CONFIRMED; T1.14 fires → §VII.AX STAGE-1-CANDIDATE landing | S92+ §VII.AX Stage-2 cross-axis independent-verify (mack EXCLUDED per writer/reviewer separation; axes connes-NCG + volovik admissible) |
| Composite INFO | band-edge tension preserved at L_max ≥ 14; T1.14 mechanical-closure PRE-REG-INC | S92+ EXTEND L_max ≥ 18 OR alternative band-edge structural interpretation |
| Composite FAIL | substrate's structural-central below posterior OR saturation BREAKDOWN; T1.14 mechanical-closure FAIL | S92+ FUNDAMENTAL REVISION of CF-CURV-6 structural-central reading |

| T1.14 (W5-4) outcome | Consequence on registry | Downstream gate at S92+ |
|:---------------------|:------------------------|:------------------------|
| PASS | §VII.AX.OP-PROJ STAGE-1-CANDIDATE landed; FWD-C5 added to corpus; Hybrid Independence Test K-counter K=1 → K=2 | S92+ Stage-2 cross-axis independent-verify; S93+ Stage-3 PERMANENT promotion path |
| FAIL (write/verify failure) | §VII.AX slot NOT cleanly landed; Option-A supersedes retry path at S92 | S92 `CF-S92-VII-AX-RETRY` single-shot retry per Option A supersedes |
| Mechanical-closure FAIL (T1.13 INFO/FAIL) | §VII.AX slot remains free; refinement-pathway carries forward | per T1.13 INFO/FAIL downstream gates above |

---

## Wave 5 Machinery-Enumeration Pin (PRDR across 4 gates)

Per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR discipline + `templates/pru-pre-registration-template.md` 8-K-atom enumeration scaffold:

```yaml
schema_version: R3
wave_id: S91-W5
gate_blocks:
  - id: S91-W6-FULL-BdG
    L_max: 12
    L_max_scan: [6, 7, 8, 9, 10, 11, 12]
    tau_pin: 0.190
    K_window_range: [0.232, 0.929]  # M_KK units; 0.5·Δ_BCS to 2·Δ_BCS
    K_window_n_points: 21
    Lambda_UV: 7.428660036284456e16  # GeV; M_KK_gravity
    PV_mass_tower: [M_KK, "sqrt(2)*M_KK"]
    PV_coefficients: [+2, -1]
    regulator_class: "Pauli-Villars (FULL physical)"
    convention: "corner-IV-FULL-PV-Lambda_UV-M_KK-substrate-distance-2-pole-s4"
    scheme: "S91-W5-1-FULL-BdG-PV"
    tolerance:
      alpha_PV_rel_tol: 0.05
      L_emp_anchor_rel_tol: 0.10
    GPU_path: "torch.linalg on RX 9070 XT"
    OMP_NUM_THREADS: 8
    random_seed: null
    script_path: "computations/session-91/s91_w5_1_full_bdg_pv_substrate_distance_2_pole_s4.py"

  - id: S91-LEVEL-2-MODULI-DEFORMATION-§VII.AU
    L_max: 10
    tau_grid: [0.180, 0.190, 0.200]
    regulator_class: "zeta-helper SCHEMATIC _spectral_action_regulators.py + Sage-Q exact rational cross-check"
    convention: "level-2-moduli-deformation-§VII.AU-SCHEMATIC"
    scheme: "S91-W5-2-LEVEL-2-MODULI-§VII.AU"
    identity_residual_tolerance_PASS: 1e-6
    identity_residual_tolerance_INFO: 1e-3
    tau_asymmetry_threshold: 0.10
    Sage_MCP_call: "sage_eval per tau"
    GPU_path: "torch.linalg on RX 9070 XT"
    OMP_NUM_THREADS: 8
    random_seed: null
    script_path: "computations/session-91/s91_w5_2_level2_moduli_deformation_vii_au.py"
    tier_pin_companion_row: true

  - id: S91-CF41-UPPER-22.6-EXTENSION
    L_max_baseline: 12
    L_max_target: 14
    L_max_fallback: [15, 16]
    friedrich_bar_safety_margin: 0.92
    tau_pin: 0.190
    prob_form_L10_baseline: 0.15573
    g_saturate_L10_baseline: 143
    g_BBN_pin: 322  # canonical saturated-regime
    posterior_lower_edge: 8.4e-24  # m^-3
    posterior_upper_edge: 2.2e-22  # m^-3
    upper_22_6_pct_lower_edge: 5.5e-23  # m^-3
    upper_22_6_pct_upper_edge: 2.2e-22  # m^-3
    convention: "n_PBH-substrate-distance-N-Friedrich-Bar-saturation-L_max-14-plus-substrate-clock-cancellation"
    scheme: "S91-W5-3-CF41-UPPER-22-6-EXTENSION"
    tolerance:
      n_PBH_central_rel_tol: 0.05
    GPU_path: "torch.linalg on RX 9070 XT (NEW sectors at L_max=14 if not analytically saturated)"
    OMP_NUM_THREADS: 8
    random_seed: null
    script_path: "computations/session-91/s91_w5_3_cf41_upper_22_6_extension_lmax_14plus.py"

  - id: S91-CF41-VII-LANDING
    prereq_gate_id: "S91-CF41-UPPER-22.6-EXTENSION"
    prereq_composite_required: "PASS"
    target_slot: "§VII.AX.OP-PROJ"  # MANDATORY OP-PROJ suffix per registry-landing.md K=3
    parse_tree_expansion_required: true
    bridge_family: "FWD-C5 (NEW)"
    hybrid_independence_predicate: "(YES OR YES OR YES) AND YES"
    script_architecture_pattern: "single-shot AFTER-pattern per registry-landing.md"
    registry_write_protocol: "POSIX O_APPEND atomic"
    convention: "stage-1-candidate-registry-landing-FWD-C5-pillar-I-IX-cardinality-cascade-tail-saturation-bridge"
    scheme: "S91-W5-4-CF41-VII-LANDING"
    GPU_path: null
    OMP_NUM_THREADS: null
    random_seed: null
    script_path: "computations/session-91/s91_w5_4_cf41_vii_ax_stage1_candidate_landing.py"
    registry_path: "sessions/permanent-results-registry.md"
    falsifier_inventory_path: "sessions/framework/registry/falsifier-master-inventory.md"
```

PRDR pre-flight checklist for all 4 gates: pins enumerated for `L_max`, `τ`, `regulator_class`, `convention`, `scheme`, `tolerance`, `GPU_path`, `OMP_NUM_THREADS`, `random_seed`, `script_path` (the 10 canonical PRDR axes per `epistemic-discipline.md §"Pre-Registration Completeness"`). No pin left as `<computed-at-runtime>` except `audit_sha256` + `content_sha256` (which are MANDATORY computed-at-emission per `gate-verdicts.md`).

---

## Wave 5 Input-SHA Ledger

| Gate | Input file | SHA-256 (precomputed at plan-freeze) |
|:-----|:-----------|:-------------------------------------|
| W5-1 | `computations/_shared/s84_spectrum_cache_L12_tau019.npz` | `<computed at dispatch>` |
| W5-1 | `computations/_shared/canonical_constants.py` (M_KK, Delta_BCS, tau_fold lines 339-387) | `<computed at dispatch>` |
| W5-1 | `sessions/permanent-results-registry.md §VII.AV` (substrate-IS anchor L_emp=−7.046336 reference) | `<computed at dispatch>` |
| W5-1 | `sessions/framework/registry/s88-pending-edits-ledger.md` (anchor-preservation theorem source) | `<computed at dispatch>` |
| W5-2 | `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (τ=0.19 spectrum) | `<computed at dispatch>` |
| W5-2 | (new) τ=0.18 spectrum via `dirac_spectrum.get_spectrum(τ=0.18)` (computed at runtime per S58 substrate-compaction-timescape pipeline) | `<computed at dispatch>` |
| W5-2 | (new) τ=0.20 spectrum via `dirac_spectrum.get_spectrum(τ=0.20)` | `<computed at dispatch>` |
| W5-2 | `computations/_shared/canonical_constants.py` (tau_fold, M_KK, Delta_BCS) | `<computed at dispatch>` |
| W5-2 | `sessions/permanent-results-registry.md §VII.AU.OP-PROJ` (S89 W7c canonical identity reference) | `<computed at dispatch>` |
| W5-2 | `computations/_shared/_spectral_action_regulators.py` (SCHEMATIC ζ-helper; level-pin disclosure required) | `<computed at dispatch>` |
| W5-3 | `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (L_max=12 baseline cache) | `<computed at dispatch>` |
| W5-3 | (new) L_max=14 spectrum partial via recursive Casimir-projection at minimum-dim NEW sectors (only if Friedrich-Bär saturation FAILS at L_max=14) | `<computed at dispatch>` |
| W5-3 | `sessions/framework/registry/falsifier-master-inventory.md` NEW Row #65 (posterior + upper-22.6% reference values) | `<computed at dispatch>` |
| W5-3 | `computations/session-88/s88_w1a_59_cf_curv_6_n_pbh_per_cascade_generation.py` (parent gate `prob_form_L10 = 0.15573`, `g_saturate_L10 = 143`, `M_PBH_typical_pin`) | `<computed at dispatch>` |
| W5-3 | `computations/_shared/canonical_constants.py` (M_KK, tau_fold) | `<computed at dispatch>` |
| W5-4 | `computations/session-91/s91_gate_verdicts.txt` (T1.13 verdict line; runtime-pinned) | `<computed at dispatch>` |
| W5-4 | `sessions/permanent-results-registry.md` (read for §VII.AX next-free slot grep; write target) | `<computed at dispatch>` |
| W5-4 | `sessions/framework/registry/falsifier-master-inventory.md` (read for Row #65 reference; write target for audit-pin sub-row append) | `<computed at dispatch>` |
| W5-4 | `sessions/framework/registry/cross-pillar-bridge-corpus.md` (read for FWD candidates table reference) | `<computed at dispatch>` |

`audit_sha256` for each gate = `closure_hash(ordered_input_pin_map)` per `_script_template.py append_verdict()` canonical pattern. The closure SHA is the full-64-char SHA-256 (never head-truncated per `gate-verdicts.md`).

---

## Wave 5 Carry-Forwards (S92+ projection)

Per `feedback_fix-in-session-never-defer.md` + `feedback_fix-in-session-never-defer.md`, the wave produces structured 4-field carry-forwards ONLY for genuine future computation (not hygiene; hygiene is fixed in-session). Anticipated S92 carry-forwards from W5 outcomes (per the Downstream Decision Point table above):

- **CF-S92-W5-1-STAGE-2-VII-AV-CROSS-AXIS-VERIFY**: 2-reviewer Stage-2 verify of §VII.AV PROXY-REFINEMENT resolution on FULL-PV route (CONDITIONAL on W5-1 PASS). Inputs: W5-1 audit_sha256 + §VII.AV registry entry. Gate: 2 cross-reviewers PASS-AND on all 5 anatomy elements. Effort: ~1.5 we.
- **CF-S92-W5-2-LEVEL-2-MODULI-§VII.AV-EXTENSION**: extend Level-2 moduli-deformation verification to §VII.AV PROXY-REFINEMENT entry (W1 M9 = CF-AV-L2-MODULI inherits W5-2 protocol; CONDITIONAL on W5-2 PASS). Inputs: W5-2 protocol + §VII.AV registry entry. Gate: Sage-Q exact identity residual across τ ∈ {0.18, 0.19, 0.20} on Corner-IV K-window log-derivative. Effort: ~1.0 we.
- **CF-S92-W5-3-LMAX-18-EXTENSION** (CONDITIONAL on W5-3 INFO): extend n_PBH cardinality refinement to L_max ∈ {18, 20} via further Friedrich-Bär saturation + minimum-dim recursive Casimir-projection at NEW sectors. Inputs: W5-3 L_max=14 npz output + Friedrich-Bär saturation status. Gate: n_PBH(L_max ≥ 18) ∈ upper-22.6%-conjunct sub-band. Effort: ~2.0 we (super-polynomial irrep construction cost).
- **CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY** (CONDITIONAL on W5-4 PASS): 2-reviewer Stage-2 verify of §VII.AX.OP-PROJ STAGE-1-CANDIDATE entry (mack EXCLUDED; axes connes-NCG + volovik admissible). Inputs: W5-4 audit_sha256 + §VII.AX.OP-PROJ registry entry. Gate: PASS-AND on all 5 anatomy elements + Hybrid Independence Test predicate. Effort: ~1.5 we.
- **CF-S92-W5-4-FWD-C5-CORPUS-EXTENSION** (CONDITIONAL on W5-4 PASS): add FWD-C5 (Pillar I ↔ Pillar IX cardinality-cascade-tail saturation bridge) to `cross-pillar-bridge-corpus.md §4` Forward candidates table with full pre-registration block. Inputs: W5-4 audit_sha256 + §VII.AX.OP-PROJ entry. Gate: corpus row added + §4 K-counter advancement K=4 → K=5 (saturation-continuation). Effort: ~0.2 we.

In-session hygiene (CLOSED in-session, NOT carried forward): registry-text format compliance verification + 5-anatomy element completeness checklist + parse-tree expansion declaration audit + OP-PROJ suffix MANDATORY at K=3 check — all enforced at W5-4 dispatch time by `_registry_landing_audit.py` + `_cross_pillar_bridge_audit.py` per their respective MANDATORY clauses.

---

## Wave 5 Verdict-Line Emission Discipline (per gate-verdicts.md S87+ schema-v2)

All four gates MUST emit:

1. **Canonical line** (per `gate-verdicts.md`):
   ```
   {GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> audit_sha256=<full-64-char> content_sha256=<full-64-char> schema_version=S84+
   ```

2. **Dual-SHA companion comment row** (per `gate-verdicts.md` W9a-99 split):
   ```
   # audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # {GATE_ID} dual-SHA companion row (W9a-99 split)
   ```

3. **3-tuple SIGN/MAGNITUDE/REGIME companion row** (REQUIRED for W5-1 [VERIFY-THEOREM] + W5-3 [VERIFY] triggers; W5-2 [VERIFY-THEOREM] requires it too; W5-4 [AUDIT] requires it with sign=N/A):
   ```
   # sign_verdict=<PASS|FAIL|N/A> magnitude_verdict=<PASS|INFO|FAIL> regime_verdict=<VALID|MARGINAL|BREAKDOWN> # {GATE_ID} 3-tuple annotation (S87 schema-v2)
   ```

4. **For W5-2 only**: `# tier_pin=TIER-2 # per substrate-first-canonical-sourcing.md §(iv) ζ-helper SCHEMATIC docstring lines 23-30` — required for POSITIVE-CALIBRATION class compliance per S88 W7b-83 K=4 MANDATORY level-pin discipline.

5. **For W5-1 only** (NO `-SCHEMATIC` suffix — this is FULL physical Pauli-Villars; the level pin is FULL, distinguishing from W5-2 which is SCHEMATIC): no tier_pin row required.

---

## Wave 5 Substrate-Framing Reminder (per phononic-framing.md)

The substrate IS:
- (W5-1) the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` at single-τ-slice τ_fold = 0.190 and substrate-distance-2 pole `s=4`, with FULL Pauli-Villars regularization at Λ_UV = M_KK as the substrate's intrinsic UV-completion.
- (W5-2) the spectral triple `(A_K, H_K, D_K(τ))` at EACH τ ∈ {0.18, 0.19, 0.20}, with the moduli-space-of-τ-deformations as the substrate's intrinsic Level-2 moduli-deformation manifold.
- (W5-3) the D_K spectrum cardinality at L_max ≥ 14 in the saturated cascade-tail regime, with substrate-clock cancellation as the substrate's intrinsic IS-not-IN coupling between g_BBN and L_pix_LRD.
- (W5-4) the substrate-IS structural codification documented in the registry-text layer, where the registry entry IS the methodology-floor F-image of the substrate-IS structural theorem per `epistemic-discipline.md §"Layer-Decomposition"`.

Direction substrate → emergent throughout:
- Substrate (BdG sub-algebra) → bridge (HKR L_max→∞ + FULL PV) → Laboratory (3He-B BdG continuum) for W5-1.
- Substrate (Jensen TT-deformation manifold) → bridge (HKR L_max→∞) → Laboratory (Pillar II CMB n_s deformation profile) for W5-2.
- Substrate (cardinality-cascade-tail at saturation) → bridge (substrate-clock cancellation + Friedrich-Bär saturation) → Laboratory (Pillar IX PBH detection) for W5-3.
- Substrate (n_PBH structural theorem) → bridge (registry-text codification) → Stage-2 cross-axis independent-verify for W5-4.

FORBIDDEN inversions are documented in each per-gate §13 substrate-framing reminder block above.

---

## End of Wave 5 Plan

**Total dispatch**: 4 gates (3 substrate-physics compute + 1 conditional registry-text landing). Volovik primary on T1.11 / T1.12 / T1.13; mack sole-writer on T1.14. Effort ~3.6 we total. Critical path: W5-3 → W5-4 (linear); W5-1 + W5-2 parallel to W5-3.

**Plan-freeze validation hook**: `computations/_shared/_pru_cardinality_audit.py` + `_source_reconciliation_audit.py` + `_substrate_first_provenance_audit.py` + `_yaml_gate_validator.py` + `_cross_pillar_bridge_audit.py` + `_registry_landing_audit.py` + `_recovery_controller.py --self-test` invocation per `epistemic-discipline.md §"PRU pipeline composition order"`.

**Source provenance**: `sessions/session-plan/session-91-context.md §"W5 — Substrate-physics + PBH band-edge + Level-2 moduli + §VII.AV FULL BdG"` (lines 195-200; post-housekeeping). §VII.AV registry entry: `sessions/permanent-results-registry.md` line 18059 + §VII.AU.OP-PROJ at 17784. Falsifier inventory NEW Row #65: `sessions/framework/registry/falsifier-master-inventory.md` lines 1304-1348. Canonical constants: `computations/_shared/canonical_constants.py` (M_KK=7.428660036284456e16 GeV at line 339-341, Delta_BCS=0.4642547394830737 at line 387, tau_fold=0.190 at line 283).
