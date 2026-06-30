# Session 88 Plan — Wave 3a: 3He-B inheritance substrate-compute family

> **Provenance**: planner-w3a split of stalled S88 W3 (volovik-superfluid-universe-theorist PRIMARY ownership; substrate-compute axis). Sister waves: W3b (cross-pillar bridge anatomy retry — volovik+connes joint), W3c (BdG-spectral-triple substrate-laboratory inheritance — volovik+landau joint, slated S89+).
> **Theme**: 3He-B inheritance retry under M_3(ℂ) Cartan-zone PRE-projection + observable-redefinition + L_max-scan robustness, addressing S87 W11-5 FWD-C3 REGISTRY-FAIL composite (ratio_mismatch=1.029 vs Level-2 envelope 0.05; structural cause = M_3(ℂ) Cartan-zone weight non-negligible at L_max=10 in multiplicity-weighted Mellin scheme).
> **Source-of-truth pins** (verified at planner-w3a freeze, do NOT re-verify): `canonical_constants.py` for `tau_fold = 0.19`, `Delta_BCS = 0.4642547394830737`, `M_KK = 7.428660036284456e+16`, `cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992`. S86 W-5 DONE-5 (Δ_B/Δ_A)^p cancellation theorem at p=0 (machine-precision residual 0.0e+00). s84 master spectrum cache `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949...`.

---

## Wave 3a Summary

Wave 3a is the **substrate-compute** half of the S88 3He-B inheritance retry workshop family. The S87 W11-5 cross-pillar bridge candidate FAILed registry-PASS at the Level-3 empirical anchor (ratio_mismatch=1.029 violates Level-2 algebraic envelope 0.05 by ~21×) — but the inheritance theorem at S86 W1b-T8 (canonical at `sessions/framework/correspondence/3HeB-inheritance-canonical.md`) was PRESERVED. The structural diagnosis was: the W11-5 substrate observable was constructed as a multiplicity-weighted Mellin-pole-window sum over the FULL Peter-Weyl spectrum of `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`; the M_3(ℂ) Cartan zone (which lives in `ker(ι_*)` under the BDI → BdG sector child morphism `χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)`) contributed non-negligibly because the multiplicity weights upgraded its sub-leading spectral content into the leading observable.

This wave executes three corrective probes, each pre-registering its falsification target:

| # | Gate ID | Theme | Verdict-source |
|:--|:--------|:------|:---------------|
| 14 | `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY` | Pre-project M_3(ℂ) Cartan zone OUT of substrate observable BEFORE Mellin-pole-window decomposition; test ratio_mismatch_M3C_projected ≤ 0.05 | `computations/s88_gate_verdicts.txt` |
| 18 | `S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY` | Redefine substrate observable as ι_*-composable cohomology-class pairing on post-ι_* image (H ⊕ ℂ sectors only); test R_substrate matches R_3HeB_lit at Level-2 envelope 0.001 | `computations/s88_gate_verdicts.txt` |
| 19 | `S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN` | L_max ∈ {16, 18, 20} robustness scan with pre-registered convention pins (Cβ unweighted-median OR B multiplicity-weighted-median; Cα frozen-pole REJECTED at planner-w3a freeze) | `computations/s88_gate_verdicts.txt` |

**Substrate framing (mandatory per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space")**: the substrate IS the finite-L spectral-triple structure `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The 3He-B laboratory observable is what the lab measures IN a 3He-B cryostat at the polycritical pressure point (P_pc=21.22 bar, T_pc=2.273 mK). The bridge map `ι : (A_K, H_K, D_K) → BdG-restricted M_2(ℂ) sector` (BDI → BdG child) sends the substrate-IS Hochschild pairing INTO the laboratory-IN BdG band-edge observable. Wave 3a tests whether the M_3(ℂ) sector contamination at L_max=10 is the structural FAIL cause; PASS at any of #14 / #18 / #19 promotes the bridge anatomy K-counter from K=2 (W11-5 REGISTRY-FAIL) to K=3 (MANDATORY status promotion per `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption").

---

## Wave 3a Decision Point Prerequisites

Wave 3a fires unconditionally at S88 dispatch — no upstream prerequisites from S87. The S86 W1b-T8 inheritance theorem canonical at `sessions/framework/correspondence/3HeB-inheritance-canonical.md` is the structural floor; W11-5 FAIL is observable-construction-specific, NOT bridge-map-defective.

**Cross-wave dependencies INTO Wave 3a**:
- s84 master spectrum cache `s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7fd6a6949...`) — provides Peter-Weyl block-diagonal eigenvalue inventory at L_max=12; #14 and #18 read directly; #19 extends via Casimir-bound + Friedrich-Bär saturation per `.claude/rules/math-scripts.md` §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check".
- `canonical_constants.py` cocycle norms (substrate-IS Sage-exact); inherited from S86 W-5 DONE-5.
- `sessions/framework/correspondence/3HeB-inheritance-canonical.md` (S86 W1b-T8 canonical inheritance theorem).
- `sessions/permanent-results-registry.md` §VII.AJ entry (W11-5 REGISTRY-FAIL row; Wave 3a outcomes append audit-pin sub-rows on PASS).

**Cross-wave dependencies OUT of Wave 3a** (forward to W3b + W3c):
- Wave 3b (cross-pillar bridge anatomy retry) consumes #14 and #18 verdicts; if either PASSes, W3b lands the K=3 promotion-event edit at `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption".
- Wave 3c (BdG-spectral-triple substrate-laboratory; queued S89+) consumes #19 L_max-scan structural envelope; if #19 PASSes, W3c uses the L_max → ∞ extrapolation for the FWD-C3 inheritance morphism rank-2 cohomology-asymmetry test.

---

## §W3a-14. S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY

### Gate ID

`S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`

Collision check: S87 verdict file `computations/s87_gate_verdicts.txt` does NOT contain this gate-ID at planner-w3a freeze (verified by orchestrator pre-flight; planner-w3a is bound to S88 verdict file).

### Trigger

S87 W11-5 FWD-C3 cross-pillar bridge candidate REGISTRY-FAIL at Level-3 empirical anchor (ratio_mismatch = 1.029 vs Level-2 envelope 0.05). Structural diagnosis (W11-5 §6 closeout): the M_3(ℂ) Cartan zone of the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` contributed non-negligibly to the multiplicity-weighted Mellin-pole-window observable at L_max=10 because the Peter-Weyl multiplicity weights upgraded its sub-leading spectral content (Casimir-suppressed at the bare-eigenvalue layer per W11-2 stratum-3 scan) into the leading-order multiplicity-weighted observable. Pre-projecting M_3(ℂ) OUT — i.e., constructing the Mellin-pole window on the BdG-projection-image only — tests whether the contamination is the structural FAIL cause.

### Classification

**PHONONIC** (per `.claude/rules/phononic-framing.md` §"Classification Guide"). The gate computes a substrate-IS observable on the finite-L spectral-triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` AFTER pre-projection; the 3He-B laboratory comparison is to a relay-pattern excitation at the polycritical pressure point (excitation IS a reorganization of the fiber's eigenvalue spectrum, NOT a particle in 3He-B). The relay-pattern direction of explanation flows substrate → BdG-sector child → 3He-B laboratory observable.

### Agent type

**volovik-superfluid-universe-theorist** (PRIMARY, sole writer). Authoritative voice on (a) substrate ↔ 3He-B inheritance (parent-child morphism per S86 W1b-T8 canonical), (b) the (Δ_B/Δ_A)^p cancellation theorem operational form at p=0 (S86 W-5 DONE-5), (c) the W11-5 §6 structural diagnosis. Per `feedback_agent-roster.md` (memory pin), volovik is the framework's authoritative reviewer for inheritance-morphism falsifier-protocol design.

Connes-ncg-theorist NOT co-author at this gate (the Cartan-zone projection is an algebra-level operation on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` that volovik authored at S86 W-5 DONE-5; the cohomology-class-level redefinition is deferred to #18 where connes IS co-author).

### Hypothesis

H_M3C_projected: After pre-projecting M_3(ℂ) Cartan-zone spectral content OUT of the substrate observable construction (i.e., constructing the multiplicity-weighted Mellin-pole window on the BdG-restricted ℂ ⊕ ℍ image only, before the pole-window decomposition), the W11-5 ratio_mismatch falls into the Level-2 algebraic envelope:

```
ratio_mismatch_M3C_projected := |R_substrate_M3C_projected − R_3HeB_lit| / |R_3HeB_lit|  ≤  0.05
```

Pre-registered substantive direction (this is the workshop's track-discriminator dual prior per `.claude/rules/epistemic-discipline.md` §"Dual-prior pre-registration as track-discriminator pattern"):

- **Track A (M_3(ℂ) IS the FAIL cause)**: PRIOR = 0.65; PASS at this gate REROUTES probability mass to Track A → 0.92.
- **Track B (M_3(ℂ) is NOT the dominant FAIL cause; observable-construction must be redefined per #18 OR L_max-scan must extend per #19)**: PRIOR = 0.35; FAIL at this gate REROUTES probability mass to Track B → 0.91.
- INFO at this gate (e.g., 0.05 < ratio_mismatch_M3C_projected < 0.15) leaves priors unchanged; Track A and Track B both remain in the wave 3b synthesis.

### Method

#### Substitution chain (mandatory per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute" — sign + threshold claim present)

```
Step 1: A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)                                [definition, S86 W1b-T8]
Step 2: ι_* : A_K → M_2(ℂ)                                   [BDI → BdG child morphism, χ]
        ker(ι_*) = M_3(ℂ) ⊕ {0_ℂ ⊕ 0_ℍ}                      [W-5 DONE-5; Cartan zone]
Step 3: P_BdG : H_K → H_K^{BdG}                              [orthogonal projector onto BdG image]
        H_K^{BdG} = π(ℂ) · H_K ⊕ π(ℍ) · H_K                  [Peter-Weyl block-diagonal]
        rank(P_BdG) = dim(ℂ) + dim(ℍ) = 1 + 4 = 5            [per-fiber dim count, ÷ 1 sector dim]
Step 4: D_K^{BdG} := P_BdG · D_K · P_BdG                     [BdG-restricted Dirac, definition]
Step 5: rho_M3C_projected(s, τ_fold) := ζ-regulated trace
        Σ_{(p,q)∈BdG-image} m_{(p,q)} · λ_{(p,q)}^{-2s}      [exclusion of M_3(ℂ) Peter-Weyl indices]
Step 6: R_substrate_M3C_projected :=
        Res[rho_M3C_projected(s); s = (d-1)/2]               [Mellin-Barnes pole at substrate-distance-1]
        evaluated at d = 4, τ = 0.190                        [canonical pole, Jensen-deformed]
Step 7: ratio_mismatch_M3C_projected =
        |R_substrate_M3C_projected − R_3HeB_lit| / |R_3HeB_lit|   [PASS/FAIL metric]
        where R_3HeB_lit = +0.03536                          [polycritical 3He-B literature anchor]
Step 8: Direction: if M_3(ℂ) is the dominant W11-5 FAIL contributor,
        excluding it should reduce |R_substrate − R_3HeB_lit|
        by factor ≥ (1.029) / 0.05 = 20.58×                  [ratio of measured to envelope]
Conclusion: PASS at ratio_mismatch_M3C_projected ≤ 0.05      [direction from canonical form]
```

#### Method dispatch prompt (volovik-superfluid-universe-theorist)

```
Volovik, you are PRIMARY on `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`.

INPUT PINS (verify SHAs at dispatch):
- s84_spectrum_cache_L12_tau019.npz (master Peter-Weyl block-diagonal eigvals/multiplicities)
- canonical_constants.py: tau_fold = 0.19; Delta_BCS = 0.4642547394830737; M_KK = 7.428660036284456e+16;
  cocycle_norm_phi67 = 0.793346 (M_KK²); cocycle_norm_phi88 = 0.108307 (M_KK²);
  substrate_cocycle_ratio_67_88 = 7.324992 (Sage-exact)
- W11-5 measured anchors: R_substrate = -1.21222; R_3HeB_lit = +0.03536; ratio_mismatch = 1.029
- 3He-B polycritical: P_pc = 21.22 bar; T_pc = 2.273 mK; T_pc/T_c = 0.9125;
  SC_corr_A = 1.151; SC_corr_B = 1.111; Δ_A/(k_BT_c) = 2.0302; Δ_B/(k_BT_c) = 1.9597
- Inheritance morphism χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) (M_3(ℂ) → 0 ∈ ker(ι_*))
- (Δ_B/Δ_A)^p cancellation at p = 0 (S86 W-5 DONE-5; machine-precision residual 0.0e+00)

TASK:
1. Build the M_3(ℂ) Cartan-zone projector P_M3C via Peter-Weyl decomposition:
     P_M3C = Σ_{(p,q)∈M_3(ℂ)-image} |⟨p,q,Cartan⟩⟨p,q,Cartan|⟩
   The M_3(ℂ) Peter-Weyl indices are the (p,q) sectors carrying SU(3)-adjoint Cartan-toral
   weight under the canonical embedding ℂ ⊕ ℍ ⊕ M_3(ℂ) ↪ A_K.
   Reference: S86 W-5 DONE-5 §III.4 Cartan-zone enumeration; W11-2 stratum-3 sector list.

2. Construct the BdG-restricted projector P_BdG = 1 - P_M3C (orthogonal complement on H_K).
   Verify rank(P_BdG) per Step 3 of substitution chain.

3. Construct D_K^{BdG} := P_BdG · D_K · P_BdG. Verify D_K^{BdG} is block-diagonal with
   M_3(ℂ) blocks set to zero (numerical zero ≤ 1e-14 ULP).

4. Compute rho_M3C_projected(s, τ_fold = 0.190) via ζ-regulated trace on D_K^{BdG} only.
   Use M_PV mass cutoff = 100 · M_KK (Pauli-Villars regulator; pre-registered, no shopping).
   Integration window: s ∈ [substrate-distance-1 - 0.5, substrate-distance-1 + 0.5] with
   pole at s = (d-1)/2 = 1.5 for d = 4. ULP_tol = 1e-12.

5. Extract Mellin-Barnes residue R_substrate_M3C_projected at s = 1.5 (substrate-distance-1
   pole, d = 4 canonical).

6. Compute ratio_mismatch_M3C_projected per Step 7 of substitution chain.

7. Cross-check: compute the M_3(ℂ) sector's standalone contribution
   R_substrate_M3C_only = Res[rho_M3C(s); s = 1.5] where rho_M3C is the ζ-trace on
   D_K · P_M3C only. Decomposition consistency: R_substrate_full = R_substrate_M3C_projected
   + R_substrate_M3C_only (modulo cross-block terms; report both and verify additive
   decomposition holds at ULP_tol).

OUTPUT FILES:
- computations/s88_w3a_3heb_excess_inheritance_m3c_projected_retry.py
- computations/s88_w3a_3heb_excess_inheritance_m3c_projected_retry.npz
  (keys: R_substrate_M3C_projected, R_substrate_M3C_only, R_substrate_full,
   ratio_mismatch_M3C_projected, P_M3C_rank, P_BdG_rank, M_PV_mass, ULP_tol_used,
   substrate_cocycle_ratio_67_88_verified, decomposition_residual)
- computations/s88_w3a_3heb_excess_inheritance_m3c_projected_retry.png
  (3-panel: top = D_K^{BdG} eigenvalue distribution vs D_K full; middle = rho integrand
   on s ∈ [1.0, 2.0]; bottom = ratio_mismatch comparison W11-5 vs W3a-14)

VERDICT LINE (append to s88_gate_verdicts.txt):
S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY: <PASS|FAIL|INFO> -- value=<r_mismatch> \
  scheme=ζ-regulated-Mellin-Barnes-residue-pole-1 convention=M3C-cartan-zone-pre-projected \
  L_max=10 audit_sha256=<64-char> content_sha256=<64-char> schema_version=R3

WORKING-PAPER SECTION: §W3a-14 in sessions/archive/session-88/session-88-results-workingpaper.md
  (≥ 15 lines substantive content; substrate framing block; ι_*-composability disclosure)
```

### Machinery pin (PRDR enumeration per `.claude/rules/epistemic-discipline.md` §"PRU pipeline composition order")

| Pin | Value | Source |
|:----|:------|:-------|
| `M_PV_mass` | 100 · M_KK = 7.4287e+18 GeV | Standard Pauli-Villars cutoff at 100× substrate scale |
| `ULP_tol` | 1e-12 | Float64 ULP for ratio comparisons; matches W11-5 §6 |
| `s_integration_window` | [1.0, 2.0] | Substrate-distance-1 pole at s=1.5 ± 0.5 |
| `pole_extraction_method` | Cauchy contour integration with ε-regularization at s=1.5±1e-7 | Matches W11-5 method |
| `tau_pin` | 0.190 (canonical Jensen fold position) | `canonical_constants.py:tau_fold` |
| `L_max` | 10 (s84 cache canonical) | s84_spectrum_cache_L12_tau019.npz key `L_max_canonical` |
| `regulator_class` | ζ-regulated (Pauli-Villars deformation, regulator-pin-discipline §"Tag Format") | a_n^{ζ} per regulator-pin-discipline.md |
| `M3C_projector_construction` | Peter-Weyl Cartan-zone decomposition via S86 W-5 DONE-5 §III.4 | Reference enumeration, NOT new derivation (M3 satisfied) |

PRDR pre-flight: all 8 pins present at plan-freeze; PRU cardinality D_PRU_raw = 0 expected.

SOURCE-RECONCILIATION pre-flight: `M_PV_mass` is a fresh canonical-pin-promotion candidate; `M_PV_mass_FW = 100 · M_KK_FW` is a derived pin (PIN-DERIVATIVE-VS-SOURCE-PRIMARY class (d) per epistemic-discipline §"Source Reconciliation"); D_max = 0; absorbable.

### Expected output 4-tuple

| # | Quantity | Pre-registered range | Expected value (Track A prior) |
|:--|:---------|:---------------------|:-------------------------------|
| 1 | `R_substrate_M3C_projected` | [+0.020, +0.060] (Track A: tracks 3He-B lit centered) | +0.034 ± 0.003 |
| 2 | `ratio_mismatch_M3C_projected` | [0.00, 0.30] | 0.04 ± 0.02 |
| 3 | `P_M3C_rank / dim(H_K^{≤10})` | [0.55, 0.75] (M_3(ℂ) is the dominant Peter-Weyl block) | 0.625 |
| 4 | `decomposition_residual` (additive consistency check) | < 1e-10 | 1e-12 to 1e-11 |

### PASS / FAIL / INFO thresholds

- **PASS**: `ratio_mismatch_M3C_projected ≤ 0.05` AND `decomposition_residual < 1e-10` AND `R_substrate_M3C_projected` sign matches sign(R_3HeB_lit) = +.
- **FAIL**: `ratio_mismatch_M3C_projected > 0.15` OR `decomposition_residual ≥ 1e-10` OR sign mismatch.
- **INFO**: `0.05 < ratio_mismatch_M3C_projected ≤ 0.15` AND consistency conditions hold (ambiguity range; M_3(ℂ) is partial-FAIL contributor; both Track A and Track B remain).

### Substitution chain — formal validation

(Already presented in §"Method" Steps 1-8 above; complete substitution chain with definitions, algebraic simplification, and direction reading. Sign claim "PASS at ratio_mismatch ≤ 0.05" derived from canonical form, NOT from narrative. Per `math-scripts.md` §"Double-Check Logic Before Compute" mandatory requirement.)

### What PASS / FAIL / INFO mean

**PASS**: M_3(ℂ) Cartan-zone contamination IS the dominant structural FAIL cause of W11-5. The substrate-IS observable correctly tracks the 3He-B laboratory-IN observable when the kernel of ι_* is excluded. The cross-pillar bridge anatomy K-counter advances K=2 → K=3, triggering MANDATORY-status promotion at `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption" (per the rule's K=3 promotion event clause). FWD-C3 instance #2 (W11-5) is RECLASSIFIED as REGISTRY-FAIL-WITH-RECOVERY-AT-W3a-14 in `sessions/permanent-results-registry.md` §VII.AJ via append-only audit-pin sub-row (mack-cosmic-bridge writes per `feedback_mack-bridge-role.md`).

**FAIL**: M_3(ℂ) is NOT the dominant FAIL cause. The W11-5 structural diagnosis is incorrect; the FAIL must originate elsewhere — either the substrate observable construction itself is non-ι_*-composable (#18 tests) or the L_max=10 truncation is below the structural-saturation threshold (#19 tests). Wave 3b consumes this verdict to prioritize #18 + #19 closeout in synthesis.

**INFO**: M_3(ℂ) is a PARTIAL FAIL contributor; some other structural cause (observable-construction OR L_max-truncation) shares the FAIL space. The closeout requires #18 + #19 to disambiguate; W3b synthesis treats Track A and Track B as both alive at this verdict.

### Effort

~0.7 wave-equivalents (matrix construction at L_max=10 from cache; Mellin-pole evaluation; cross-check decomposition consistency). Single-thread CPU; no GPU pin (matrix dim = 78,064 from L_max=10 cache, fits in float64 RAM).

### Substrate framing (mandatory per `.claude/rules/phononic-framing.md`)

The substrate IS the spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`. The M_3(ℂ) Cartan zone IS the SU(3)-adjoint sub-bundle of `A_K`; the BdG image IS the ℂ ⊕ ℍ orthogonal complement under χ. The 3He-B laboratory IS the polycritical-pressure observable measured IN a 3He-B cryostat. The bridge map ι sends the substrate-IS Hochschild pairing on the BdG-projection-image INTO the laboratory-IN BdG band-edge observable.

NOT: "the M_3(ℂ) sector is in some internal subspace of the substrate". The M_3(ℂ) sector IS the substrate's SU(3)-adjoint algebra-block; it is not "in" anything. The pre-projection IS the algebra-level operation `A_K → A_K · P_BdG`; the projection is structural, not geometric.

NOT: "particles in the BdG sector". The BdG sector IS a Peter-Weyl block of the substrate spectral triple. Excitations of D_K^{BdG} ARE the relay patterns the laboratory measures as 3He-B BdG band-edge observables.

---

## §W3a-18. S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY

### Gate ID

`S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY`

Collision check: S87 verdict file `computations/s87_gate_verdicts.txt` does NOT contain this gate-ID at planner-w3a freeze.

### Trigger

Companion to #14: tests an alternative structural interpretation of the W11-5 FAIL — that the substrate observable was constructed via a procedure NON-COMPOSABLE with ι_* (i.e., the multiplicity-weighted Mellin-pole window does not factor through the inheritance morphism), so even after pre-projecting M_3(ℂ) the residual ratio_mismatch may not collapse to the Level-2 envelope. The redefinition tests a cohomology-class-level pairing on the post-ι_* image directly (NCG-axiomatic substrate per `.claude/rules/cross-pillar-bridge-anatomy.md` §"Level 1 — Substrate-IS Structural Identity").

### Classification

**PHONONIC**. The redefined substrate observable is a cohomology-class pairing on the BdG-image spectral-triple; the relay-pattern direction of explanation is preserved (substrate cohomology-class IS, not laboratory-IN cohomology-class). The 3He-B laboratory comparison is to a relay-pattern excitation at the polycritical pressure point. Cohomology-class semantics are substrate-IS by construction (per `cross-pillar-bridge-anatomy.md` Level 1 calibration).

### Agent type

**volovik-superfluid-universe-theorist + connes-ncg-theorist** (joint dispatch; volovik PRIMARY writer; connes CO-AUTHOR on cohomology-class redefinition).

Volovik authority: substrate ↔ 3He-B inheritance morphism; ι_*-composability framing per S86 W1b-T8 canonical.

Connes authority: NCG-axiomatic redefinition of the substrate observable as a cohomology-class pairing per Connes-Moscovici 1995 §III.4 dim-spectrum residue formula at the substrate-distance-1 pole; HKR (Hochschild-Kostant-Rosenberg) `L_max → ∞` bridge map per S86 W-5 RULE-1 calibration.

Joint authorship by precedent: S86 W-5 (volovik PRIMARY + connes CO-AUTHOR) on Pillar III ↔ Pillar IV bridge theorem at `permanent-results-registry.md` §VII.AF.1.

### Hypothesis

H_iota_star_composable: When the substrate observable is REDEFINED as the ι_*-composable cohomology-class pairing on the post-ι_* image only (i.e., evaluated at the Hochschild cohomology level with M_3(ℂ) excised pre-image-construction, NOT post-projection on a non-composable definition), the redefined R_substrate matches R_3HeB_lit at the cohomology Level-2 envelope:

```
R_substrate_redefined := ⟨[φ_substrate_BdG], [Ch(P_0(τ_fold))_BdG]⟩       (cohomology-class pairing)
ratio_mismatch_redefined := |R_substrate_redefined − R_3HeB_lit| / |R_3HeB_lit|  ≤  0.001  (Level-2 cohomology envelope at L_max=10)
```

### Method

#### Substitution chain (mandatory; cohomology direction claim present)

```
Step 1: ι : (A_K, H_K, D_K) → (A_K^BdG, H_K^BdG, D_K^BdG)              [inheritance, S86 W1b-T8]
        A_K^BdG = ℂ ⊕ ℍ  (M_3(ℂ) excised pre-image-construction)
Step 2: Substrate-IS observable per cross-pillar-bridge-anatomy.md Level 1:
        R_universal_BdG := ⟨[φ_g^{sym}_BdG], [Ch(P_0(τ_fold))_BdG]⟩    [Connes-Karoubi pairing]
        evaluated on (A_K^{BdG, ≤10}, H_K^{BdG, ≤10}, D_K^{BdG, ≤10})
Step 3: Pillar IV continuum image (HKR L_max → ∞):
        R_3HeB_lit := lim_{L_max → ∞} R_universal_BdG(L_max)            [bridge map]
                    = continuum BdG-undoubled excess at polycritical    [Pillar IV laboratory-IN]
Step 4: Level 2 algebraic envelope:
        |R_universal_BdG(L_max=10) − R_3HeB_lit| ≤ envelope(L_max=10)  [structural prediction]
        envelope(d=4, L_max=10) ~ L^{-3}_max  ~  10^{-3}                [W-5 RULE-2 calibration]
Step 5: ratio_mismatch_redefined :=
        |R_universal_BdG(L_max=10) − R_3HeB_lit| / |R_3HeB_lit|         [PASS/FAIL metric]
Step 6: Direction: if observable is ι_*-composable + Level-2 envelope holds,
        ratio_mismatch_redefined ≤ envelope/|R_3HeB_lit|                [from canonical form]
        with R_3HeB_lit = +0.03536, envelope = 10^{-3}/L_max=10:
        ratio_mismatch_redefined ≤ 10^{-3} / 0.03536 ~ 0.028 ≈ 0.001 (Level 3 strict)
        OR ratio_mismatch_redefined ≤ 0.05 (Level 3 envelope-loose)
Step 7: Conclusion: PASS at ratio_mismatch_redefined ≤ 0.001            [strict cohomology Level 2/3]
        INFO at 0.001 < ratio_mismatch_redefined ≤ 0.05                  [envelope-loose]
        FAIL at ratio_mismatch_redefined > 0.05                          [bridge structurally fails]
```

#### Method dispatch prompt (volovik PRIMARY + connes CO-AUTHOR)

```
Volovik (PRIMARY) + Connes (CO-AUTHOR) — `S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY`

INPUT PINS (verify SHAs at dispatch):
- s84_spectrum_cache_L12_tau019.npz (Peter-Weyl block-diagonal eigvals/multiplicities, master)
- canonical_constants.py: tau_fold = 0.19; cocycle_norm_phi67 = 0.793346 (M_KK²);
  cocycle_norm_phi88 = 0.108307 (M_KK²); substrate_cocycle_ratio_67_88 = 7.324992 (Sage-exact)
- W11-5 measured anchors: R_substrate = -1.21222; R_3HeB_lit = +0.03536
- S86 W-5 §VII.AF.1 calibration: Level 1 R_universal Hochschild pairing on BdG-image at L=10
- Cross-pillar-bridge-anatomy.md Level-2 envelope: L^{-3} at d=4 → 10^{-3} at L_max=10
- Inheritance morphism ι : A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ); A_K^BdG = ℂ ⊕ ℍ (excised pre-image)
- (Δ_B/Δ_A)^p cancellation at p=0 (S86 W-5 DONE-5)

TASK:
1. Construct the BdG-restricted spectral triple PRE-IMAGE (i.e., excise M_3(ℂ) from A_K BEFORE
   constructing the spectral triple, NOT projecting AFTER):
     A_K^BdG_preimage = ℂ ⊕ ℍ
     H_K^BdG_preimage = restriction of L²(M_K) to ℂ ⊕ ℍ Peter-Weyl sectors only
     D_K^BdG_preimage = restriction of D_K to H_K^BdG_preimage (NOT D_K projected)
   The ι_*-composable distinction: this construction commutes with ι_* by definition;
   the W11-5 construction did NOT commute (M_3(ℂ) sector contributed via multiplicity weights).

2. Compute the cohomology-class-level Hochschild pairing per S86 W-5 RULE-1:
     R_substrate_redefined := ⟨[φ_g^{sym}_BdG], [Ch(P_0(τ_fold))_BdG]⟩
   Use Connes-Moscovici 1995 §III.4 dim-spectrum residue formula:
     R_substrate_redefined = Res[Tr(D_K^BdG_preimage^{-2s}); s = (d-n)/2] · pairing_kernel
   evaluated at d = 4, n = 1 (substrate-distance-1 pole), τ = 0.190.

3. Verify the redefined observable is ι_*-composable: compute
     R_substrate_via_iota = ι_*(R_universal_full_substrate)
   where R_universal_full_substrate is the W11-5 construction (multiplicity-weighted on full
   Peter-Weyl spectrum). Composability check: R_substrate_redefined should match
   R_substrate_via_iota at L_max=10 to within Level-2 envelope (~10^{-3}); deviation > 10^{-2}
   indicates the W11-5 construction was indeed non-composable (which is the diagnostic
   confirming the Track-2 hypothesis underlying #18).

4. Compute ratio_mismatch_redefined per Step 5 of substitution chain.

5. Cross-check at HP^1 cohomology level: compute the cocycle ratio
     ‖φ_67_BdG_redefined‖ / ‖φ_88_BdG_redefined‖
   This should equal substrate_cocycle_ratio_67_88 = 7.324992 (Sage-exact at machine precision)
   per the (Δ_B/Δ_A)^p cancellation theorem at p = 0 (S86 W-5 DONE-5). Deviation > 1e-12
   indicates the redefinition broke the cocycle-ratio invariant (which would be a severe
   structural defect, not a target-PASS).

OUTPUT FILES:
- computations/s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.py
- computations/s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.npz
  (keys: R_substrate_redefined, R_substrate_via_iota, ratio_mismatch_redefined,
   composability_residual, cocycle_ratio_67_88_redefined,
   cocycle_ratio_67_88_substrate_canonical, ULP_tol_used, L_max_used)
- computations/s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.png
  (3-panel: top = composability residual scan over L_max ∈ {6, 8, 10};
   middle = cohomology-class pairing convergence to R_3HeB_lit;
   bottom = cocycle ratio invariant check)

VERDICT LINE (append to s88_gate_verdicts.txt):
S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY: <PASS|FAIL|INFO> -- value=<r_mismatch> \
  scheme=NCG-cohomology-class-Hochschild-pairing-pole-1 convention=iota-star-composable-preimage-construction \
  L_max=10 audit_sha256=<64-char> content_sha256=<64-char> schema_version=R3

WORKING-PAPER SECTION: §W3a-18 in sessions/archive/session-88/session-88-results-workingpaper.md
  (≥ 15 lines substantive content; substrate framing + cohomology-class direction + 5 IS-not-IN
   anatomy elements; cross-link to cross-pillar-bridge-anatomy.md §"Forward template-adoption")
```

### Machinery pin (PRDR enumeration)

| Pin | Value | Source |
|:----|:------|:-------|
| `pole_residue_method` | Connes-Moscovici 1995 §III.4 dim-spectrum residue formula | NCG-axiomatic substrate per cross-pillar-bridge-anatomy.md Level 1 |
| `pairing_kernel` | Hochschild HKR L_max → ∞ image kernel (per S86 W-5 RULE-1) | W-5 calibration |
| `s_pole_substrate_distance_1` | 1.5 (= (d-n)/2 at d=4, n=1) | Substrate-distance-1 pole canonical |
| `tau_pin` | 0.190 | `canonical_constants.py:tau_fold` |
| `ULP_tol` | 1e-12 | Float64 ULP for cocycle ratio invariant check |
| `cocycle_invariant_threshold` | 1e-12 (Sage-exact match) | substrate_cocycle_ratio_67_88 = 7.324992 |
| `L_max` | 10 (canonical Level-3 anchor) | Cross-pillar-bridge-anatomy §"Level 3" calibration |
| `level2_envelope` | L_max^{-3} = 10^{-3} at d=4 | Cross-pillar-bridge-anatomy §"Level 2" |
| `level3_strict_threshold` | 0.001 (= envelope/|R_3HeB_lit|) | Step 6 substitution chain |
| `level3_loose_threshold` | 0.05 (envelope-loose, INFO band) | Per cross-pillar-bridge-anatomy §"Registry-PASS criterion" |

PRDR pre-flight: 10 pins all present; PRU cardinality D_PRU_raw = 0 expected.

SOURCE-RECONCILIATION pre-flight: `level2_envelope` value `10^{-3}` is canonical from `cross-pillar-bridge-anatomy.md` §"Level 2" (W-5 calibration); D_max = 0; absorbable. `cocycle_invariant_threshold` = 1e-12 matches `canonical_constants.py:cocycle_norm_phi67/cocycle_norm_phi88` Sage-exact pin precision.

### Expected output 4-tuple

| # | Quantity | Pre-registered range | Track A prior expected |
|:--|:---------|:---------------------|:-----------------------|
| 1 | `R_substrate_redefined` | [+0.020, +0.060] (Level-3 strict) or [+0.030, +0.040] (Level-3 loose) | +0.0353 ± 0.0001 |
| 2 | `ratio_mismatch_redefined` | [0.000, 0.10] | 0.0005 ± 0.0003 |
| 3 | `composability_residual` (R_substrate_redefined vs R_substrate_via_iota) | < 1e-2 (composable confirmation) | < 1e-3 |
| 4 | `cocycle_ratio_67_88_redefined / 7.324992` | 1.0 ± 1e-12 (Sage-exact invariant) | 1.0 (machine epsilon) |

### PASS / FAIL / INFO thresholds

- **PASS-strict** (Level-2/3 cohomology envelope): `ratio_mismatch_redefined ≤ 0.001` AND `composability_residual < 1e-2` AND `|cocycle_ratio_67_88_redefined / 7.324992 − 1| < 1e-12`. Confirms ι_*-composable redefinition; promotes K-counter K=2 → K=3 (cross-pillar-bridge-anatomy MANDATORY).
- **PASS-loose** / **INFO**: `0.001 < ratio_mismatch_redefined ≤ 0.05` AND consistency conditions hold. Bridge structure passes envelope-loose Level 3; cohomology-class redefinition is the structural fix; FWD-C3 instance #2 reclassifies as REGISTRY-PASS-AT-W3a-18 in `permanent-results-registry.md` §VII.AJ.
- **FAIL**: `ratio_mismatch_redefined > 0.05` OR `composability_residual ≥ 1e-2` (W11-5 construction was NOT the issue; redefinition does not recover) OR `|cocycle_ratio_67_88 invariant| > 1e-12` (severe structural defect — redefinition broke the substrate-derived cocycle ratio; abandons #18 as structural fix).

### Substitution chain — formal validation

(Steps 1-7 in §"Method" above; sign + threshold direction derived from canonical form; per `math-scripts.md` mandatory chain requirement.)

### What PASS / FAIL / INFO mean

**PASS-strict**: The cohomology-class redefinition IS the structural fix; W11-5 substrate observable was non-ι_*-composable (multiplicity-weighted Mellin-pole window does NOT factor through ι_*). Cross-pillar bridge anatomy K-counter advances K=2 → K=3 (MANDATORY-status promotion edits to `cross-pillar-bridge-anatomy.md` §"Forward template-adoption" by orchestrator-direct-write). FWD-C3 instance #2 (W11-5) is RECLASSIFIED as REGISTRY-PASS-AT-W3a-18 in `permanent-results-registry.md` §VII.AJ via append-only audit-pin sub-row.

**PASS-loose / INFO**: The redefinition recovers within envelope-loose Level 3 (between strict 0.001 and loose 0.05); the cohomology-class pairing IS approximately ι_*-composable but not at the canonical L_max=10 strict envelope. Wave 3b synthesis flags this as structural-fix-with-residual-tail; #19 L_max-scan extension provides the convergence rate.

**FAIL**: Either (a) the redefinition does not recover (composability_residual high, ratio_mismatch unchanged from W11-5 levels) — meaning W11-5's FAIL is NOT due to ι_*-non-composability, the inheritance bridge has a deeper structural defect; or (b) cocycle ratio invariant 7.324992 is broken — severe structural defect, the redefinition itself is malformed and must be re-derived. Both branches abandon #18 as the structural fix and route to W3c (BdG-spectral-triple substrate-laboratory inheritance, S89+ queue) for full reanalysis.

### Effort

~1.0 wave-equivalents (cohomology-class pairing construction with HKR-image residue extraction; cocycle invariant cross-check; composability scan over L_max ∈ {6, 8, 10}). Single-thread CPU; matrix dim per L_max ≤ 78,064 from cache (no GPU pin).

### Substrate framing (mandatory)

The substrate IS the spectral triple `(A_K^{BdG_preimage, ≤10}, H_K^{BdG_preimage, ≤10}, D_K^{BdG_preimage, ≤10})`. The cohomology-class `[φ_g^{sym}_BdG]` IS a Hochschild cocycle on `A_K^BdG`; the projector `Ch(P_0(τ_fold))_BdG` IS the Chern character of the band-0 Jensen-deformed projector. The pairing `⟨·, ·⟩` IS the Connes-Karoubi K-theory boundary at the substrate-distance-1 pole.

NOT: "the cohomology-class lives in the laboratory's de Rham complex". Cohomology-class is substrate-IS by NCG-axiomatic definition; the laboratory measures the HKR `L_max → ∞` image of the substrate cocycle, NOT the cocycle itself. Per `cross-pillar-bridge-anatomy.md` §"Direction of explanation" mandatory clause: substrate (Pillar A) IS the cohomology-class observable → bridge map (HKR) → laboratory (Pillar B) IN the BZ-trace observable.

NOT: "ι_*-composability is just commutation of operators". ι_*-composability IS a structural property of the cocycle definition itself; the W11-5 multiplicity-weighted Mellin-pole window construction did NOT factor through ι_* at the chain-complex level (it depended on Peter-Weyl multiplicity weights that are A_K-global, not A_K^BdG-local).

---

## §W3a-19. S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN

### Gate ID

`S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN`

Collision check: S87 verdict file does NOT contain this gate-ID at planner-w3a freeze.

### Trigger

Companion to #14 + #18: tests whether W11-5 ratio_mismatch is L_max-saturated at L_max=10 (the canonical Level-3 anchor) or convergence-incomplete. Pre-registers convention pin to close convention-shopping vulnerability identified in W11-5 §6 closeout (multiple pole-aggregation conventions yielded different ratio_mismatch values at L_max=10; structural causes of pole-aggregation ambiguity not fully resolved).

### Classification

**PHONONIC**. Substrate-IS observable scanned over L_max regulator axis; the L_max-saturation check is a regulator-stability test on the substrate spectral-triple structure. Per `.claude/rules/math-scripts.md` §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check", L_max ∈ {16, 18, 20} is feasible on the AMD RX 9070 XT GPU via Friedrich-Bär saturation theorem (§W11-3 calibration).

### Agent type

**volovik-superfluid-universe-theorist** (PRIMARY, sole writer). L_max-scan robustness is volovik's domain (regulator-axis stability on substrate-IS observables). No connes co-author needed (the convention pin is volovik-authored at W11-5 §6 closeout; no NCG-axiomatic redefinition required).

### Hypothesis

H_Lmax_saturated: With pole convention pre-registered (Cβ unweighted-median OR B multiplicity-weighted-median; Cα frozen-pole REJECTED per W11-5 §6 finding that frozen-pole sweep is convention-shopping-equivalent), the ratio_mismatch values at L_max ∈ {10, 16, 18, 20} satisfy structural-saturation:

```
saturated iff |ratio_mismatch(L_max=20) − ratio_mismatch(L_max=18)| < 0.05 · |ratio_mismatch(L_max=18)|
            AND |ratio_mismatch(L_max=18) − ratio_mismatch(L_max=16)| < 0.05 · |ratio_mismatch(L_max=16)|
```

If saturated AT ratio_mismatch ≤ 0.05: the bridge passes Level 3 at extended L_max (corrects W11-5 FAIL via L_max-completion).
If saturated AT ratio_mismatch > 0.05: W11-5 FAIL is L_max-saturated (NOT a truncation artifact; structural FAIL stands at higher L_max).
If unsaturated: L_max → ∞ extrapolation needed; FAIL composite with diagnostic.

### Method

#### Substitution chain (mandatory; convention + threshold direction claim)

```
Step 1: L_max-scan range pre-registered: L ∈ {16, 18, 20}             [feasibility per W11-3]
Step 2: Convention pin pre-registered ALTERNATIVES:
        Cβ = unweighted-median pole-aggregation                       [conv option 1]
        B  = multiplicity-weighted-median pole-aggregation            [conv option 2]
        Cα = frozen-pole sweep                                         [REJECTED at planner-w3a freeze;
                                                                       per W11-5 §6 convention-shopping]
Step 3: Per L_max in {10 (W11-5 anchor), 16, 18, 20}, per conv in {Cβ, B}:
        ratio_mismatch(L_max, conv) = |R_substrate(L_max, conv) − R_3HeB_lit| / |R_3HeB_lit|
Step 4: Saturation check at (Cβ): see H_Lmax_saturated
Step 5: Saturation check at (B): same form
Step 6: Direction:
        IF saturated at Cβ AND saturated at B AND ratio_mismatch ≤ 0.05 at L_max=20:
          PASS: W11-5 FAIL was L_max-truncation artifact; bridge passes Level 3 at extended L_max
        IF saturated at Cβ AND saturated at B AND ratio_mismatch > 0.05 at L_max=20:
          INFO-saturated-FAIL: W11-5 FAIL is structural; FWD-C3 instance #2 stands as REGISTRY-FAIL
        IF NOT saturated at either Cβ or B at L_max=20:
          FAIL: convention-or-truncation-incomplete; route to W3c re-analysis
Step 7: Cross-convention check: if Cβ and B disagree by > 50% on ratio_mismatch at L_max=20,
        the convention pin itself is structurally unstable; both compound INFO outcome.
```

#### Method dispatch prompt (volovik-superfluid-universe-theorist)

```
Volovik PRIMARY — `S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN`

INPUT PINS (verify SHAs at dispatch):
- s84_spectrum_cache_L12_tau019.npz (L_max=12 master cache)
- canonical_constants.py: tau_fold = 0.19; M_KK = 7.428660036284456e+16
- W11-5 anchors at L_max=10: R_substrate = -1.21222; R_3HeB_lit = +0.03536; ratio_mismatch = 1.029
- Convention pins (pre-registered at planner-w3a freeze):
    Cβ : unweighted-median pole-aggregation        (allowed)
    B  : multiplicity-weighted-median pole-aggregation  (allowed)
    Cα : frozen-pole sweep                                (REJECTED — convention-shopping)
- L_max scan: {16, 18, 20}; comparison anchor at L_max=10 (W11-5 measured)
- Friedrich-Bär saturation theorem per W11-3: η_FB_lower = 0.40; sector-bound + Casimir-projection
  feasibility verified per .claude/rules/math-scripts.md §"D_K Block-Diagonality"

TASK:
1. Verify L_max-scan feasibility per math-scripts.md §"D_K Block-Diagonality":
   For each L ∈ {16, 18, 20}, identify largest sector (p,q) with p+q=L; verify recursive
   Casimir-projection construction time < 10 min single-thread (per W11-3 timeout pattern).
   If unfeasible at L=20 within timeslot: invoke Friedrich-Bär saturation argument
   (η_FB_lower bound on (p+q=L) sector eigvals); replace direct construction with
   analytic saturation extrapolation; tag verdict-line scheme = "friedrich-baer-extrapolated".

2. Per (L, conv) ∈ {16, 18, 20} × {Cβ, B}:
   2a. Build sector-extended D_K^{≤L} from cache + on-demand higher-(p,q) construction
       (or Friedrich-Bär bound).
   2b. Compute multiplicity-weighted Mellin-pole window observable per W11-5 method,
       with conv ∈ {Cβ, B} pole aggregation (RE-RUN W11-5's method, NOT new construction).
   2c. Extract R_substrate(L, conv) and ratio_mismatch(L, conv).

3. Saturation analysis per Step 4-5 of substitution chain.

4. Cross-convention check (Step 7): compute |ratio_mismatch(L=20, Cβ) − ratio_mismatch(L=20, B)|
   relative to mean. If > 50%: emit Conv-B canonical-metric advisory per
   .claude/rules/regulator-convention-lockdown.md (the cross-convention deviation > 50% is the
   structural cause of convention pin instability; demarcation theorem applies).

5. GPU pin: AMD RX 9070 XT (17.1 GB VRAM, ROCm 7.2) for L_max ≥ 16 if matrix dim > 100,000.
   Per math-scripts.md §"Environment", largest single Peter-Weyl block at L_max=20 ≈ 9792
   (bounded; fits with margin > 11×). Use torch.linalg, not numpy.linalg.

OUTPUT FILES:
- computations/s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.py
- computations/s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.npz
  (keys: L_max_scan = [10, 16, 18, 20]; conv_scan = ['Cβ', 'B'];
   R_substrate_grid (4×2); ratio_mismatch_grid (4×2);
   saturation_Cbeta (bool); saturation_B (bool);
   cross_conv_deviation_at_Lmax20 (float); friedrich_baer_used (bool);
   M_KK_pin_verified, tau_fold_pin_verified)
- computations/s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.png
  (3-panel: top = ratio_mismatch vs L_max, two curves Cβ + B, with Level-3 thresholds 0.05 + 0.001;
   middle = R_substrate convergence to R_3HeB_lit anchor;
   bottom = cross-convention deviation vs L_max)

VERDICT LINE (append to s88_gate_verdicts.txt):
S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN: <PASS|FAIL|INFO> -- value=<r_mismatch_Lmax20_Cbeta> \
  scheme=multiplicity-weighted-Mellin-pole-window-Lmax-scan convention=<Cbeta-or-B-or-mixed> \
  L_max=20 audit_sha256=<64-char> content_sha256=<64-char> schema_version=R3

WORKING-PAPER SECTION: §W3a-19 in sessions/archive/session-88/session-88-results-workingpaper.md
  (≥ 15 lines substantive content; substrate framing; convention pin disclosure;
   regulator-convention-lockdown.md cross-link)
```

### Machinery pin (PRDR enumeration)

| Pin | Value | Source |
|:----|:------|:-------|
| `L_max_scan` | {16, 18, 20} (with anchor at 10 from W11-5) | Pre-registered at planner-w3a freeze |
| `convention_allowed` | {Cβ unweighted-median, B multiplicity-weighted-median} | Pre-registered; Cα frozen-pole REJECTED |
| `pole_aggregation_method_Cbeta` | unweighted median over Mellin-pole-window evaluation grid | W11-5 §6 calibration option 1 |
| `pole_aggregation_method_B` | multiplicity-weighted median (m_(p,q) weighting) | W11-5 method canonical at W11-5 anchor |
| `saturation_threshold` | 0.05 (relative L_max-step variation) | Pre-registered |
| `cross_conv_deviation_threshold` | 0.50 (relative cross-convention disagreement) | Pre-registered; >0.50 triggers Conv-B advisory |
| `level3_strict_threshold` | 0.001 | Cross-pillar-bridge-anatomy §"Level 3 strict" |
| `level3_loose_threshold` | 0.05 | Cross-pillar-bridge-anatomy §"Registry-PASS criterion" |
| `tau_pin` | 0.190 | `canonical_constants.py:tau_fold` |
| `gpu_pin` | AMD RX 9070 XT torch.linalg (ROCm 7.2) for L_max ≥ 16 | Per math-scripts.md §"Environment" |
| `friedrich_baer_lower` | 0.40 | W11-3 calibration; η_FB_lower for L_max ≥ 12 saturation extrapolation |
| `wall_time_cap_per_sector` | 600 s (10 min per recursive Casimir-projection) | Per agent timeslot |

PRDR pre-flight: 12 pins; PRU cardinality D_PRU_raw = 0 expected.

SOURCE-RECONCILIATION pre-flight: `friedrich_baer_lower = 0.40` is canonical from W11-3 (8.4% safety margin below empirical floor 0.4365); D_max ≈ 0; absorbable.

CONV-B canonical-metric pre-check (per `.claude/rules/regulator-convention-lockdown.md`): the convention pin lockdown does NOT directly govern this gate (gate is NOT DR3-class L_max-stability on `w_0_FW`), but the Cα frozen-pole REJECTION is structurally analogous (frozen-pole = effacement-non-anchored ≡ outside admissibility class). Pre-registration of Cβ + B (and rejection of Cα) at planner-w3a freeze is a forward-looking application of the demarcation-theorem template.

### Expected output 4-tuple

| # | Quantity | Pre-registered range | Expected (mid-prior) |
|:--|:---------|:---------------------|:---------------------|
| 1 | `ratio_mismatch(L_max=20, Cβ)` | [0.001, 1.5] (full range from PASS-strict to W11-5-level FAIL) | 0.5 ± 0.4 (high uncertainty pre-compute) |
| 2 | `saturation_Cβ` (bool) | {True, False} | True ~ 60% prior |
| 3 | `cross_conv_deviation_at_Lmax20` | [0.0, 5.0] | 0.3 ± 0.2 |
| 4 | `friedrich_baer_used` (bool) | {True, False} (depends on L=20 wall-time feasibility) | False ~ 70% prior (direct construction succeeds) |

### PASS / FAIL / INFO thresholds

- **PASS**: `saturation_Cβ = True` AND `saturation_B = True` AND `ratio_mismatch(L_max=20, Cβ) ≤ 0.05` AND `ratio_mismatch(L_max=20, B) ≤ 0.05` AND `cross_conv_deviation < 0.5`. W11-5 FAIL was L_max-truncation artifact; extended-L_max bridge passes Level 3 (loose).
- **INFO-saturated-FAIL**: `saturation_Cβ = True` AND `saturation_B = True` AND ANY ratio_mismatch > 0.05 at L_max=20. W11-5 FAIL is L_max-saturated structural; FWD-C3 instance #2 REGISTRY-FAIL stands at extended L_max; #14 / #18 are the only remaining structural-fix paths.
- **INFO-cross-conv-unstable**: `cross_conv_deviation_at_Lmax20 ≥ 0.5`. Convention pin is structurally unstable; demarcation theorem application required (per `regulator-convention-lockdown.md` §"Demarcation theorem"); W3c queue gets convention re-derivation as prerequisite.
- **FAIL**: NOT saturation_Cβ OR NOT saturation_B at L_max=20. Truncation incomplete or convergence non-monotone; W3c re-analysis at L_max → ∞ via Friedrich-Bär extrapolation.

### Substitution chain — formal validation

(Steps 1-7 in §"Method"; sign + threshold direction per `math-scripts.md` mandatory chain. Convention pin pre-registration validated per `epistemic-discipline.md` §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy" Class 8.0/8.1 machinery-pin cardinality.)

### What PASS / FAIL / INFO mean

**PASS**: W11-5 FAIL was an L_max-truncation artifact at L_max=10. Extending to L_max=20 (with feasibility-verified construction or Friedrich-Bär extrapolation) recovers Level-3 envelope-loose ratio_mismatch ≤ 0.05 at BOTH conventions Cβ and B. FWD-C3 instance #2 RECLASSIFIES as REGISTRY-PASS-AT-W3a-19 in `permanent-results-registry.md` §VII.AJ via append-only audit-pin sub-row. Cross-pillar bridge anatomy K-counter K=2 → K=3 promotion (sister to #14 / #18 promotion paths; W3b synthesis disambiguates which gate's path is canonical).

**INFO-saturated-FAIL**: L_max-saturation IS achieved (cross-L_max variation < 5%) but ratio_mismatch > 0.05 at L_max=20. W11-5 FAIL is a STRUCTURAL FAIL of the multiplicity-weighted Mellin-pole window construction, NOT a truncation artifact. The structural fix paths are #14 (M_3(ℂ) Cartan-zone projection) and #18 (cohomology-class redefinition); #19 confirms NEITHER is L_max-completion-recoverable.

**INFO-cross-conv-unstable**: Cβ and B disagree by ≥ 50% on ratio_mismatch at L_max=20. The pole-aggregation convention is itself structurally unstable on the substrate side; Conv-B canonical-metric advisory (per `regulator-convention-lockdown.md`) applies. W3c queue gets the convention re-derivation as prerequisite (analogous to S86 W12-4 CAC adoption replacing RDC).

**FAIL**: L_max-truncation is incomplete at L_max=20 OR convergence is non-monotone. Friedrich-Bär extrapolation needed for L_max → ∞; W3c queue re-analyses at substrate-distance-1 pole's structural-saturation limit.

### Effort

~1.2 wave-equivalents (3 L_max points × 2 conventions = 6 evaluation grid; recursive Casimir-projection at L_max ∈ {16, 18, 20} dominates wall time per W11-3 calibration; GPU-accelerated diagonalization mitigates). Friedrich-Bär extrapolation fallback if L_max=20 direct construction unfeasible within timeslot.

### Substrate framing (mandatory)

The substrate IS `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` for L ∈ {10, 16, 18, 20}. The L_max regulator axis IS the spectral-triple truncation parameter; the L_max → ∞ image IS the continuum HKR limit. Structural saturation at finite L IS the substrate's own statement that higher-(p,q) Peter-Weyl sectors do not contribute to the bottom-K observable.

NOT: "at higher L_max we resolve more of the geometry". The geometry IS the spectral-triple structure; "resolution" of (p,q) sectors is a regulator-axis observation, not a geometric resolution. Per `phononic-framing.md` §"IS Space, Not IN Space" mandatory clause: L_max-scan IS substrate-IS regulator stability check, NOT IN-spacetime resolution of features.

NOT: "the convention is a calculation choice". Pole-aggregation convention IS a substrate-level construction of the cohomology-class pairing; Cβ and B are STRUCTURALLY DISTINCT cohomology-class definitions, not numerical-method options. The Cα frozen-pole REJECTION at planner-w3a freeze is the substrate-level statement that frozen-pole sweep is an effacement-non-anchored construction (analog to RDC in DR3-class L_max-stability per `regulator-convention-lockdown.md`).

---

## Wave 3a → Wave 3b Decision Point

Wave 3a's three verdicts feed into Wave 3b (cross-pillar bridge anatomy retry; volovik+connes joint synthesizers) per the following decision-point matrix:

| W3a-14 | W3a-18 | W3a-19 | Wave 3b synthesis verdict |
|:-------|:-------|:-------|:--------------------------|
| PASS | PASS | PASS | TRIPLE-CONFIRMED structural-fix; W3b lands K=2 → K=3 promotion via #14 path canonical (Cartan-zone projection is simplest fix); audit-pin sub-rows for #18 + #19 |
| PASS | PASS | FAIL | DOUBLE-PASS structural-fix; W3b lands K=2 → K=3 via #14 path canonical; #19 FAIL routes to W3c (L_max→∞ re-analysis) for forward queue |
| PASS | FAIL | * | #14 SOLO; W3b lands K=2 → K=3 via #14 path; #18 FAIL flags cohomology-class redefinition is structurally insufficient; W3c queue takes #18 re-derivation |
| FAIL | PASS | * | #18 SOLO; W3b lands K=2 → K=3 via #18 path canonical; #14 FAIL flags M_3(ℂ) NOT dominant FAIL cause; surprising result; W3c queue takes #14 re-analysis |
| FAIL | FAIL | PASS | #19 SOLO; W3b lands K=2 → K=3 via L_max-completion (W11-5 FAIL was truncation artifact); #14 + #18 FAILs flag the M_3(ℂ) and cohomology-redefinition diagnoses are both incorrect |
| FAIL | FAIL | INFO-saturated-FAIL | TRIPLE-FAIL structural; W11-5 FAIL is bridge-defective; W3c queue gets full structural reanalysis; FWD-C3 instance #2 stands as REGISTRY-FAIL-CONFIRMED |
| FAIL | FAIL | INFO-cross-conv-unstable | Pole-aggregation convention structurally unstable; W3c queue gets convention re-derivation prerequisite (demarcation-theorem-based); FWD-C3 instance #2 stays REGISTRY-FAIL pending convention rework |
| FAIL | FAIL | FAIL | TRIPLE-FAIL with truncation incomplete; W3c queue gets Friedrich-Bär L_max → ∞ extrapolation |
| INFO | * | * | W3a-14 ambiguous; W3b synthesis weights #18 + #19 outcomes more heavily |
| * | INFO | * | W3a-18 ambiguous (PASS-loose between strict 0.001 and loose 0.05); W3b lands K=2 → K=3 with envelope-loose Level 3 disclosure |

Wave 3b synthesis is 0.6 wave-equivalents (single workshop-style synthesizer dispatch reading the 3 W3a verdicts and writing W3b registry-edit landings; volovik+connes joint authorship per S86 W-5 precedent for cross-pillar bridge entries).

---

## Wave 3a Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness", Wave 3a pre-registers all gate-relevant machinery parameters at plan-freeze time. PRDR pre-flight enumeration:

### Shared machinery (all 3 gates)

| Pin | Value | Provenance |
|:----|:------|:-----------|
| `s84_spectrum_cache` | `computations/s84_spectrum_cache_L12_tau019.npz` | Master Peter-Weyl block-diagonal eigvals/multiplicities cache |
| `s84_cache_sha256` | `9e6d9cf7fd6a6949...` (full 64-char hash at dispatch) | Cache integrity pin |
| `tau_fold` | 0.19 | `canonical_constants.py:tau_fold` |
| `Delta_BCS` | 0.4642547394830737 | `canonical_constants.py:Delta_BCS` |
| `M_KK` | 7.428660036284456e+16 (GeV) | `canonical_constants.py:M_KK` |
| `cocycle_norm_phi67` | 0.793346 (M_KK²) | `canonical_constants.py:cocycle_norm_phi67` |
| `cocycle_norm_phi88` | 0.108307 (M_KK²) | `canonical_constants.py:cocycle_norm_phi88` |
| `substrate_cocycle_ratio_67_88` | 7.324992 (Sage-exact) | `canonical_constants.py:substrate_cocycle_ratio_67_88` |
| `R_3HeB_lit` | +0.03536 | W11-5 measured anchor; 3He-B polycritical literature |
| `R_substrate_W11_5` | -1.21222 | W11-5 measured (anchor for cross-checks) |
| `ratio_mismatch_W11_5` | 1.029 | W11-5 measured (FAIL anchor) |
| `inheritance_morphism_iota` | χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ); ker(ι_*) = M_3(ℂ) | S86 W1b-T8 canonical |
| `cancellation_theorem_p` | p = 0 (Δ_B/Δ_A)^p cancellation | S86 W-5 DONE-5; machine-precision residual 0.0e+00 |
| `polycritical_anchors` | P_pc=21.22 bar; T_pc=2.273 mK; T_pc/T_c=0.9125 | 3He-B literature canonical |
| `gap_anchors` | SC_corr_A=1.151; SC_corr_B=1.111; Δ_A/(k_BT_c)=2.0302; Δ_B/(k_BT_c)=1.9597 | 3He-B literature |

### Per-gate machinery (already enumerated in §"Machinery pin" of each gate block)

PRU cardinality pre-flight: per gate D_PRU_raw = 0 (all pins enumerated explicitly).

SOURCE-RECONCILIATION pre-flight: all pinned values D_max < 0.1 against canonical sources (absorbable per epistemic-discipline §"Source Reconciliation" 4-band calibration); no MANDATORY remediation.

SUBSTRATE-FIRST-PROVENANCE pre-flight (per `.claude/rules/substrate-first-canonical-sourcing.md`): all numerical pins source from substrate-first computation:
- W3a-14: `M_PV_mass = 100 · M_KK_FW` is PIN-DERIVATIVE class (d); admitted.
- W3a-18: `level2_envelope = 10^{-3}` source = `cross-pillar-bridge-anatomy.md` §"Level 2" W-5 calibration (substrate-first); admitted.
- W3a-19: `friedrich_baer_lower = 0.40` source = W11-3 substrate-first compute; admitted.

PRDR pipeline composition (per `.claude/rules/epistemic-discipline.md`): PRU → SOURCE-RECON → SUBSTRATE-FIRST-PROVENANCE → PRDR → gate execution → v3-recovery audit. All pre-flights PASS at planner-w3a freeze; gate execution unblocked.

---

## Wave 3a Input-SHA Ledger

Per `.claude/rules/agent-standards.md` §"AMRI Test 1 (input-pin)", the Input-SHA pin map MUST enumerate file-level pins ONLY. Agent-memory pins are FORBIDDEN as Input-SHA pin sources.

### File-level Input-SHA pins (computed at dispatch time)

| Source | Path | Captured at | Pin role |
|:-------|:-----|:------------|:---------|
| Master spectrum cache | `computations/s84_spectrum_cache_L12_tau019.npz` | `<pinned at dispatch>` | Substrate eigvals/multiplicities |
| Canonical constants | `computations/canonical_constants.py` | `<pinned at dispatch>` | tau_fold, Delta_BCS, M_KK, cocycle_norm_phi67/88, ratio_67_88 |
| Inheritance canonical | `sessions/framework/correspondence/3HeB-inheritance-canonical.md` | `<pinned at dispatch>` | S86 W1b-T8 canonical theorem |
| Cross-pillar bridge anatomy rule | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<pinned at dispatch>` | 5 IS-not-IN anatomy + 3-level ladder + K-counter |
| Inheritance falsifier protocol rule | `.claude/rules/inheritance-falsifier-protocol.md` | `<pinned at dispatch>` | rank-2 generalization clause for #18 |
| Phononic framing rule | `.claude/rules/phononic-framing.md` | `<pinned at dispatch>` | IS-not-IN substrate framing |
| Math scripts rule | `.claude/rules/math-scripts.md` | `<pinned at dispatch>` | D_K block-diagonality + Friedrich-Bär feasibility |
| Regulator convention lockdown rule | `.claude/rules/regulator-convention-lockdown.md` | `<pinned at dispatch>` | Convention pin discipline (W3a-19) |
| Permanent results registry | `sessions/permanent-results-registry.md` | `<pinned at dispatch>` | §VII.AF.1 (W-5 calibration) + §VII.AJ (W11-5 FAIL row) |
| W11-5 anchors verdict line | `computations/s87_gate_verdicts.txt` (W11-5 row only) | `<pinned at dispatch>` | R_substrate, R_3HeB_lit, ratio_mismatch anchors |

### audit_sha256 computation

For each gate, `audit_sha256` is `closure_hash(file_level_pins)` over the file-level Input-SHA pin map only. NO agent-memory pins; NO derivative pins computed within the script.

Per `.claude/rules/gate-verdicts.md` dual-SHA discipline:
- `audit_sha256` = SHA-256 over canonical input-pin map serialization (per `script-template.py:append_verdict()`)
- `content_sha256` = SHA-256 over the producing-script source file at execution time
- Both emitted in canonical verdict line + companion comment row
- Per-gate audit_sha256 must be pairwise distinct (per `.claude/rules/v3-closure-recovery.md` sig_5 uniqueness check)

### AMRI compliance attestation

Wave 3a Input-SHA ledger contains ZERO agent-memory file paths. Per AMRI Test 1 (`agent-standards.md` §"Calibration instance — S87 W0 plan-w13.md AMRI fix"), removing agent-memory pins from the Input-SHA map is the correct discipline; per-agent role assignments (§W3a-14 volovik PRIMARY, §W3a-18 volovik PRIMARY + connes CO-AUTHOR, §W3a-19 volovik PRIMARY) are project-level role declarations, NOT Input-SHA pin sources.

---

**End of session-88-plan-w3a.md** (3 gates: §W3a-14, §W3a-18, §W3a-19; full PRDR pre-registration + substrate framing + decision-point matrix to W3b synthesis).
