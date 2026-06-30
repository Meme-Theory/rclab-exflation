# Session 87 Plan — Sub-Wave 9b: Rescaled IC + Pole-Specificity (transit + lizzi+transit)

**Sub-wave-owner**: `transit-dynamics-theorist` (CF-55 sole transit-class) + `lizzi-spectral-functional-theorist` (CF-58 lead in `lizzi+transit` joint pair per S86 W-9 attribution; transit-dynamics-theorist co-owner). Sub-wave dispatch order: §W9b-1 (transit solo) parallel-eligible with §W9b-2 (lizzi-led joint).

**Sub-wave items (2)**: CF-55, CF-58. Both sourced from S86 W-9 workshop (Path-(c) reassessment workshop §EM-EXTENSIONS). Sub-wave 9a covers the other W-9 items (CF-22 sub-decompositions / CF-54 / CF-56 / CF-57); this sub-wave 9b carves out the two compute-heavy follow-on gates whose physics owners are the transit-axis rather than the mack/connes-axis.

**Specialist-agent assignment**: transit-dynamics-theorist owns CF-55 (SR-LO ODE compute on rescaled IC; substrate-physics owner of GGE-relic Bogoliubov ODE per `feedback_agent-roster.md` + `feedback_agent-roster.md` calibration); lizzi-spectral-functional-theorist + transit-dynamics-theorist co-own CF-58 (Mellin-cone substrate-distance-1 anti-correlation extension to substrate-distance-0 / s=4 — lizzi owns spectral-side, transit owns dynamical-side per S86 W-9 attribution lines 1535-1585).

**Carve-out rationale**: W9 stalled at 600s under unified scope; per `feedback_max-effort-full-fidelity.md` + skill §3c stall-handling precedent, splitting along owner-axis (transit vs mack/connes) preserves full 13-field fidelity per gate block.

**Registry-slot reservation**: Neither CF-55 nor CF-58 is a registry-landing gate. CF-55 lands a per-class numerical pin to `canonical_constants.py` (canonical write-order Step 2); CF-58 lands a pole-specificity scan diagnostic (PASS routes a Reading_1-vs-Reading_2 disambiguation to `permanent-results-registry.md` §VII.AJ.pole-scope sub-row at S88+ Stage-1 candidate, NOT in this sub-wave).

---

## Sub-Wave 9b Summary

| # | Gate ID | Owner | Effort | Trigger | Classification | Theme |
|:--|:--------|:------|:-------|:--------|:---------------|:------|
| 1 | `S87-RESCALED-IC-SR-LO-RERUN` | transit-dynamics-theorist | ~0.5 wave (~5-7h compute) | [VERIFY] | PHONONIC | Slow-roll-leading-order ODE rerun at 4 affine class-projected ξ²₀(R) values; numerically pin N_breakdown_observable(R) per L1-class |
| 2 | `S87-POLE-SPECIFICITY-SCAN` | lizzi-spectral-functional-theorist + transit-dynamics-theorist | ~1.0 wave (~10-12h compute) | [VERIFY] | GEOMETRIC | Test whether s=3 (substrate-distance-1) Spearman ρ_S = 1.0 anti-correlation across A_5 4-class projection generalizes to s=4 (substrate-distance-0) |

**Total sub-wave estimate**: ~15-19h compute (~1.5 wave-equivalents per S86 W-9 source effort estimates 0.5 + 1.0).

---

## Sub-Wave 9b Decision Point Prerequisites

This sub-wave runs INDEPENDENT of W1-W9a, W10-W13 landings. Both gates are self-contained against the L=12 master spectrum cache (CF-58 cite), the canonical_constants.py xi_E_GGE_inv pin (CF-55 cite), and the S86 W-9 §VII.AJ-pole-specificity reservation (CF-58 cite). One latent cross-link: if W9a-CF-42 (`S87-W5A-P3-IC-PER-CLASS-VERIFY`) lands per-class xi values **before** W9b-1 dispatches, those per-class xi values become an enriched input pin for CF-55 (replacing the four affine class-projected ξ²₀(R) construction with the W9a-CF-42 verified per-class restrictions). Per `feedback_dispatch-discipline.md`: this is a planner expectation, not a halt condition. CF-55 dispatches on the canonical xi_E_GGE_inv = 13.642473425595973 with affine class-projection scaling regardless of whether W9a-CF-42 landed; if W9a-CF-42 did land, the producing script reads the per-class npz and uses those values.

### Upstream pin map (read-only inputs)

| Pin name | Source | Role |
|:---------|:-------|:-----|
| `computations/canonical_constants.py:xi_E_GGE_inv = 13.642473425595973` | S86 W4 P4 commit; substrate-natural 59.8 · Δ_BCS / K_base anchor per `branch-iv-canonical.md` §3 | CF-55 IC central anchor; substrate-first canonical per `substrate-first-canonical-sourcing.md` Class-(f) HARD-HALT precedent |
| `computations/canonical_constants.py:tau_fold = 0.190` | S58 Volovik partition canonical | Both gates; τ_fold reference for SR-LO ODE start (CF-55) and Mellin-cone evaluation (CF-58) |
| `computations/canonical_constants.py:Delta_BCS, K_base, M_KK` | S58/S62 framework canonicals | CF-55 substrate-natural rescaling factor inputs (xi-rescaling formula 59.8·Δ_BCS/K_base); CF-58 dimensional bookkeeping anchor |
| `computations/s84_spectrum_cache_L12_tau019.npz` | S84 W-10 master spectrum cache | CF-58 D_K(τ_fold) eigenvalues at L_max=12 for full Mellin-cone moment evaluation at s=4 |
| `computations/_spectral_action_regulators.py` (Mellin-cone callable wrapper) | S86 W-12 calibrated infrastructure | CF-58 substrate-distance-{0,1} pole evaluation; verify PRIMARY pin (full physical Mellin-cone via `analytic_zeta`, not SCHEMATIC schematic) per `substrate-first-canonical-sourcing.md` §(iv) |
| S86 W-9 workshop §T-DR2.1 anchor-formula pre-registration sub-step lines 1438-1475 | S86 W-9 source | CF-58 anchor-formula pre-registration substrate (per `epistemic-discipline.md` §"Pre-Registration Completeness — Pole-Scope sub-clause" T1-20 step (b)) |
| S86 W-9 workshop §D-R2.2 + §T-CR2.2 lines 1046-1048 / 1249-1289 | S86 W-9 source | CF-58 discriminator-predicate pre-registration substrate (Reading_1 generic pluralism vs Reading_2 pole-specific localization) |
| S86 W-9 §L-CR3.2 lines 1758-1806 (4-class projection extremality |ρ_S|=1.0 EXACT) | S86 W-9 source | CF-58 reference baseline (s=3 anti-correlation extremality value to be tested against at s=4) |
| `sessions/framework/registry/branch-iv-canonical.md` §3 | S86 W4 P4 commit | CF-55 substrate-natural anchor formula source (xi_E_GGE_inv = 59.8·Δ_BCS/K_base); per-class affine-projection rescaling derivation |
| (LATENT cross-link) `computations/s87_w7_xi_E_per_class.npz` from W9a-CF-42 (if landed) | W9a-CF-42 = `S87-W5A-P3-IC-PER-CLASS-VERIFY` | CF-55 enriched input — per-class xi values replace affine class-projection construction if W9a landed first; otherwise CF-55 uses canonical-with-affine-projection construction |

### Validator coverage at Sub-Wave 9b plan-freeze

Per `session-87-context.md` §1.4, run before sub-wave dispatch:

1. `python computations/_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w9b.md` → `sessions/session-plan/session-87-plan-w9b-validation.json` — upstream npz pin map verification
2. `python computations/_yaml_gate_validator.py sessions/session-plan/session-87-plan-w9b.md` — R3 schema_version + PRDR machinery checklist per gate
3. `python computations/_source_reconciliation_audit.py` — 5+1 class taxonomy pin-vs-canonical drift; HARD-HALT at D_max ≥ 3.0; class-(f) PIN-PLACEHOLDER detection for CF-55 (xi_E_GGE_inv canonical match required)
4. `python computations/_substrate_first_provenance_audit.py` (manual review until V.1 implementation lands) — substrate-first canonical sourcing for CF-55 (xi_E_GGE_inv MUST source from canonical_constants.py:xi_E_GGE_inv per W4 P4 commit, NOT placeholder `O(10⁻²)`); for CF-58 (PRIMARY vs SCHEMATIC disclosure on `_spectral_action_regulators.py` Mellin-cone callable)
5. `python computations/_a_n_regulator_pin_audit.py` for CF-58 (a_n regulator-tag enforcement on Mellin-cone moment outputs at s=3 and s=4 poles)
6. Post-dispatch grep on `computations/s86_gate_verdicts.txt` for collision check on `S87-RESCALED-IC-*`, `S87-POLE-SPECIFICITY-*` gate IDs (no S87-prefixed entries should pre-exist)

---

## §W9b-1. CF-55 — `S87-RESCALED-IC-SR-LO-RERUN`

**Source**: S86 W-9 CF-2 (compute-carryforward.md row CF-55; lizzi+transit recommending; transit-axis owner per `feedback_agent-roster.md`).

**Specialist agent**: `transit-dynamics-theorist` (substrate-physics authority on slow-roll-leading-order Mukhanov-Sasaki ODE + GGE-relic Bogoliubov initial-condition propagation per agent memory `s86_w5a_sr_lo_diagnostic.md` + branch-iv-canonical SR-LO precedent).

**Effort**: ~0.5 wave (~5-7h compute; SR-LO ODE integration is fast, the four-IC scan is the cost dominant).

### 1. Gate ID

`S87-RESCALED-IC-SR-LO-RERUN`

### 2. Trigger

`[VERIFY]` — verify whether the SR-LO Mukhanov-Sasaki ODE integration window N_breakdown_observable(R), evaluated at four affine class-projected ξ²₀(R) initial-condition rescalings of the canonical xi_E_GGE_inv anchor, depends sensitively on R (per-class IC heterogeneity effect on regime-of-validity boundary).

### 3. Classification

PHONONIC (xi_E_GGE_inv is the substrate-IS initial condition for the GGE-relic Bogoliubov mode-function evolution; the SR-LO ODE is the substrate-physics governing structure for slow-roll-leading-order trans-fold mode propagation; N_breakdown_observable(R) is the regime-validity boundary for SR-LO truncation per `gate-verdicts.md` §"Auto-shortening clause discipline").

### 4. Hypothesis being tested

The SR-LO ε ≪ 1 truncation regime-of-validity breakdown N-fold value `N_breakdown_observable(R)` (defined as the smallest N at which |ε(N) − ε(0)| / ε(0) > 0.5, i.e., SR-LO assumption breaks at >50% perturbation per `gate-verdicts.md` §"Auto-shortening clause discipline" 50% MARGINAL→BREAKDOWN cutover) is **R-dependent** (varies across the four affine class-projected ξ²₀(R) values).

The per-class IC rescaling spans the four L1-class affine-projection coordinates (R ∈ {R_1, R_2, R_3, R_4}; the 5th L1-class is the canonical fiducial reference). The rescaling formula:

```
ξ²₀(R) = xi_E_GGE_inv · α(R)²
```

where α(R) is the affine class-projection coefficient per L1-class (sourced from S86 W-9 §EM-CN-R3-1 dual-prior structure if W9a-CF-42 landed first; otherwise computed from S86 W-12 V_4 coset enumeration via the four-element Klein-four affine map). The four R values (one per non-trivial coset) each yield a distinct ξ²₀ and a distinct SR-LO trajectory.

The structural prediction (Reading_A): N_breakdown_observable(R) varies across R by more than the canonical fiducial spread (i.e., max_R |N_breakdown_observable(R) − N_breakdown_canonical| / N_breakdown_canonical > 5%). The structural alternative (Reading_B): N_breakdown_observable(R) is R-invariant (varies by ≤5% across the 4 R values; per-class IC heterogeneity does not propagate to regime-validity boundary).

### 5. Pass/fail/INFO threshold

- **PASS (Reading_A confirmed)**: max_R |N_breakdown_observable(R) − N_breakdown_canonical| / N_breakdown_canonical > 5% AND each per-R N_breakdown is computed cleanly (i.e., the SR-LO ε(N) trajectory has a well-defined first-crossing of the 0.5-perturbation boundary; not a numerical-artifact crossing).
  - Tolerance rule: RATIO; threshold pin 0.05 = 5%; PASS band (0.05, ∞).
- **FAIL (Reading_B confirmed)**: max_R |N_breakdown_observable(R) − N_breakdown_canonical| / N_breakdown_canonical ≤ 5%. R-invariance confirmed; per-class IC heterogeneity does not propagate to N_breakdown.
- **INFO**: 0.5% < max_R deviation ≤ 5% (between PASS and FAIL bands); precision-limited or cross-class spread comparable to canonical-fiducial-spread; rerun with finer integration step or extended N-window.

**Composite collapse rule** (S87+ schema-v2 per `gate-verdicts.md`): three-tuple (sign, magnitude, regime) per gate; sign_verdict pre-registered per Reading_A (positive deviation expected); magnitude_verdict per pass/fail/INFO band; regime_verdict per ε ≪ 1 SR-LO validity at each R (BREAKDOWN if any per-R trajectory has ε > 1 within the integration window before N_breakdown_observable is reached, indicating the integration window itself is non-physical).

### 6. Machinery pin (PRDR)

| Field | PIN |
|:------|:----|
| `N_eval` | 4 R values + 1 canonical fiducial = 5 SR-LO trajectories per integration |
| `L_max` | N/A (no L_max in SR-LO ODE; field-theoretic substrate already substrate-distance-1 reduced); cross-reference `s84_spectrum_cache_L12_tau019.npz` only via xi_E_GGE_inv canonical pin |
| `scan_range` | N ∈ [0, 100] e-folds (extended from canonical N=55 pivot range to allow N_breakdown identification beyond canonical); R values {R_1, R_2, R_3, R_4} per affine class-projection (W-12 V_4 coset alignment if W9a-CF-66 V_4 monodromy PASSes; if FAILs, fall back to S86 W-9 §EM-CN-R3-1 dual-prior 5-class enumeration) |
| `step_size` | dN = 0.01 (fine integration step to resolve N_breakdown crossings to ±0.01 e-folds; cross-validate at dN = 0.005 for the canonical-fiducial trajectory only) |
| `tolerance` | RATIO `0.05` for PASS gate (5%); INFO band (0.005, 0.05]; FAIL ≤ 0.005 |
| `scheme` | SR-LO Mukhanov-Sasaki ODE: `d²ζ/dN² + (3 + ε(N) − 2η(N)) dζ/dN + (k²/(aH)²) ζ = 0` truncated at LO in (ε, η). IC at N=0: ξ²₀(R) = xi_E_GGE_inv · α(R)² (substrate-natural anchor with affine class-projection rescaling). |
| `convention` | substrate-natural-xi-E-GGE-class-projected (anchored to canonical_constants.xi_E_GGE_inv = 13.642473425595973 with W-12 V_4 coset α(R) coefficients OR W-9 §EM-CN-R3-1 dual-prior 5-class projection); SR-LO truncation at ε ≪ 1 per `branch-iv-canonical.md` §3 |
| `random_seed` | 42 (for any IC perturbation cross-check; primary trajectories deterministic) |
| `GPU path` | CPU-only path acceptable with `OMP_NUM_THREADS=8` cap per `math-scripts.md` §Environment (5 SR-LO trajectories at dN=0.01 over N ∈ [0,100] = 50,000 ODE steps × 5 = 250K-step batch; trivially CPU-bound) |

### 7. Input SHA-256 pins

- `computations/canonical_constants.py` — xi_E_GGE_inv, tau_fold, Delta_BCS, K_base, M_KK pins. Static; precompute SHA at plan-freeze. `<CANONICAL>` pin to be filled by `_plan_upstream_pin_validator.py` at S87 plan-freeze.
- `sessions/framework/registry/branch-iv-canonical.md` — substrate-natural anchor formula source (xi_E_GGE_inv = 59.8 · Δ_BCS / K_base; affine class-projection derivation). Static; precompute SHA at plan-freeze.
- `sessions/archive/session-86/session-86-w9-workshop.md` lines 1438-1475 (anchor-formula pre-registration substrate per pole-scope sub-clause T1-20 step (b)) AND lines 1535-1585 (3-class partition / 4-class projection partition table; affine class-projection α(R) coefficients). Static workshop-output; precompute SHA at plan-freeze.
- (CONDITIONAL upstream) `computations/s87_w7_xi_E_per_class.npz` from W9a-CF-42 if it landed first; else use canonical-with-affine-projection construction. Conditional; resolved at script entry by `os.path.exists` check; SHA pinned at runtime if present.
- (CONDITIONAL upstream) `computations/s87_w11_v4_monodromy_explicit.npz` from W11-1-CF-66 if it landed first (V_4 monodromy PASS gives the canonical α(R) coefficients); else fall back to dual-prior 5-class enumeration per W-9 §EM-CN-R3-1.

### 8. Expected output 4-tuple

`(value=max_R |N_breakdown_observable(R) − N_breakdown_canonical| / N_breakdown_canonical, scheme=SR-LO-Mukhanov-Sasaki, convention=substrate-natural-xi-E-GGE-class-projected, L_max=N/A-SR-LO)`

Auxiliary `.npz` keys:
- `R_values[4]` (affine class-projection coordinates)
- `xi2_0_per_R[4]` (rescaled IC values: xi_E_GGE_inv · α(R)²)
- `epsilon_trajectory_per_R[4, N_steps]` (ε(N) per R)
- `eta_trajectory_per_R[4, N_steps]` (η(N) per R)
- `N_breakdown_per_R[4]` (first-crossing of |ε(N) − ε(0)|/ε(0) = 0.5)
- `N_breakdown_canonical[1]` (canonical-fiducial reference)
- `max_R_deviation_observable[1]` (gate value)
- `regime_verdict_per_R[4]` (VALID / MARGINAL / BREAKDOWN per S87+ schema-v2)

### 9. Substitution chain (sign/direction discipline per `math-scripts.md`)

```
Step 1: Definitions
   xi_E_GGE_inv     = 59.8 · Δ_BCS / K_base = 13.642473425595973         [canonical, branch-iv-canonical.md §3, W4 P4 commit]
   α(R)             = affine class-projection coefficient per L1-class    [S86 W-9 §EM-CN-R3-1 dual-prior 5-class projection OR W-12 V_4 coset]
   ξ²₀(R)           = xi_E_GGE_inv · α(R)²                                [rescaled IC per L1-class]
   ε(N)             = -dH/dN · 1/H                                        [first SR parameter per Mukhanov-Sasaki convention]
   η(N)             = dε/dN · 1/ε                                         [second SR parameter]
   N_breakdown(R)   = min{N : |ε(N) − ε(0)|/ε(0) > 0.5}                  [SR-LO regime breakdown per gate-verdicts.md §"Auto-shortening clause discipline" 50% cutover]

Step 2: SR-LO ODE in IC ξ²₀(R)
   d²ζ_R/dN² + (3 + ε_R(N) − 2η_R(N)) dζ_R/dN + (k²/(aH)²) ζ_R = 0
   ζ_R(N=0) = ξ_0(R) = sqrt(ξ²₀(R)) = sqrt(xi_E_GGE_inv) · |α(R)|
   dζ_R/dN(N=0) = 0  (canonical SR-LO IC for adiabatic mode)

Step 3: Direction prediction
   IF α(R) varies across R (non-trivial class-projection structure):
     ξ²₀(R) varies across R   ⇒   ε_R(N=0) = ε_canonical · α(R)²   ⇒   ε_R(N) trajectory varies across R
     ⇒   N_breakdown(R) varies across R
     ⇒   max_R |N_breakdown(R) − N_breakdown_canonical| / N_breakdown_canonical > 0
     ⇒   gate value > 0   (Reading_A direction)
   IF α(R) is R-invariant (trivial class-projection):
     ξ²₀(R) ≡ xi_E_GGE_inv for all R   ⇒   N_breakdown(R) ≡ N_breakdown_canonical
     ⇒   gate value = 0   (Reading_B direction)

Step 4: Magnitude prediction (Reading_A, the substrate-prior expectation)
   The W-12 V_4 coset α(R) coefficients (if W11-1-CF-66 PASSes) span four distinct values; structural prior says max α(R)² / min α(R)² ≳ 1.5
   (per S86 W-12 §EMERGENCE E-1 R3-volovik final round V_4 coset spectral-action-moment spread).
   ε_R(N=0) spread of factor ~1.5 propagates to N_breakdown spread of ~ln(1.5) ≈ 0.41 e-folds (linear in ε for SR-LO truncation).
   N_breakdown_canonical ≈ 50-60 e-folds (canonical pivot range).
   ⇒  predicted gate value ≈ 0.41 / 55 ≈ 0.007 (0.7%; within INFO band, NOT PASS).
   So Reading_A direction (positive) is predicted, but at INFO magnitude unless α(R) spread is larger than the W-12-prior 1.5 factor.

Step 5: Sign vs magnitude verdict separation (per S87+ schema-v2)
   sign_verdict = PASS if max_R deviation > 0 (direction matches Reading_A);
                = N/A if both readings give the same sign (i.e., the test is purely magnitudinal);
                = FAIL if max_R deviation < 0 (anti-Reading_A; impossible by definition since deviation is absolute value).
   magnitude_verdict per band: PASS if > 5%; INFO if (0.5%, 5%]; FAIL if ≤ 0.5%.
   regime_verdict   = VALID if all four ε_R(N) trajectories satisfy ε ≪ 1 throughout [0, N_breakdown(R)];
                    = MARGINAL if one or more trajectories has ε ≳ 0.3 within [0, N_breakdown];
                    = BREAKDOWN if one or more trajectories has ε ≥ 1 within [0, N_breakdown].
```

### 10. What PASS and FAIL mean for the solution space

- **PASS (Reading_A)**: per-class IC heterogeneity propagates to a >5% spread in the SR-LO regime-validity boundary N_breakdown. Confirms that the F_2-class STRUCTURAL-PRIMACY interpretation extends from the IC layer (W9a-CF-42) to the regime-validity layer (this gate). The four R values are observable-distinct, not reparametrization equivalents. Downstream gates citing "the" SR-LO regime-validity window must respect per-R restrictions. Strongest reading: the SR-LO truncation has class-projected validity boundaries — different L1-classes admit different N-windows for slow-roll-leading-order analysis.
- **FAIL (Reading_B)**: per-class IC heterogeneity is invisible to the SR-LO regime-validity boundary; N_breakdown is R-invariant within 5%. Closes the F_2-class STRUCTURAL-PRIMACY interpretation at the regime-validity layer. The four α(R) coefficients act as IC reparametrizations (multiplicative renormalizations of ξ²₀ that wash out in N_breakdown). Downstream gates may cite a single canonical N_breakdown_canonical without per-class restriction. Forces re-examination of whether F_2-class STRUCTURAL-PRIMACY survives at any layer beyond IC.
- **INFO (0.5%, 5%])**: precision-limited; cross-R spread is comparable to canonical-fiducial-spread but not decisively above the W-12-prior 1.5 factor. Rerun with finer integration step (dN = 0.005) and extended N-window (N_max = 150) at S88+; promote to ADVISORY-S2 in `_source_reconciliation_audit.py` advisory list pending higher-precision rerun.
- **MARGINAL or BREAKDOWN regime_verdict on any per-R trajectory**: SR-LO truncation breaks within the integration window; the underlying ε ≪ 1 assumption is violated; the gate's value is well-defined numerically but its physical interpretation (N_breakdown as regime-validity boundary) is degraded. Per `gate-verdicts.md` composite collapse rule, regime_verdict=BREAKDOWN forces composite=FAIL regardless of magnitude. INFO with regime=MARGINAL preserves diagnostic value (sign-PASS substrate finding) per S86 W5a SR-flow Z-factor precedent.

### 11. Output artifacts

- Script: `computations/s87_w9b_rescaled_ic_sr_lo_rerun.py` (~300-500 lines; loads canonical xi_E_GGE_inv + α(R) coefficients, integrates SR-LO ODE per R, computes N_breakdown(R), evaluates max_R deviation, emits dual-SHA verdict line + 3-tuple annotation companion row).
- Data: `s87_w9b_rescaled_ic_sr_lo_rerun.npz` per §8 keys.
- Plot: `s87_w9b_rescaled_ic_sr_lo_rerun.png` (4-panel: ε_R(N) trajectories per R; η_R(N) per R; |ε(N) − ε(0)|/ε(0) crossing diagnostic with 0.5 threshold line; N_breakdown(R) bar chart with canonical-fiducial reference).
- Verdict line: appended to `computations/s87_gate_verdicts.txt` per S87+ schema-v2 (canonical line + dual-SHA companion + 3-tuple annotation row [sign / magnitude / regime]).
- Working-paper section: `sessions/archive/session-87/session-87-w9b-workingpaper.md` §W9b-1 (>15 lines; substrate framing of per-class IC heterogeneity; full substitution chain + 4-trajectory N_breakdown table + composite-collapse audit trail).
- Canonical_constants update (post-PASS): if PASS, write per-R N_breakdown_observable(R) values to `canonical_constants.py` via `update_constant("N_breakdown_R{i}", value, session="S87", source="S87-RESCALED-IC-SR-LO-RERUN", comment="...")` per `math-scripts.md` §"Canonical Write-Order" Step 2.

### 12. YAML pin

```yaml
gate_id: S87-RESCALED-IC-SR-LO-RERUN
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: VERIFY
classification: PHONONIC
specialist_agent: transit-dynamics-theorist
trigger_subtype: SIGN_AND_MAGNITUDE  # 3-tuple annotation required per S87+ schema-v2
sign_verdict_predicted: PASS  # Reading_A direction (positive max_R deviation)
magnitude_verdict_predicted: INFO  # W-12-prior estimate ~0.7%, within INFO band
regime_verdict_at_risk: VALID-or-MARGINAL  # SR-LO ε ≪ 1 truncation may reach ε ~ 0.3 by N=50 in the largest-α(R) trajectory
canonical_pins:
  xi_E_GGE_inv: 13.642473425595973  # canonical_constants.py:xi_E_GGE_inv per W4 P4 commit
  source_xi_E_GGE_inv: computations/canonical_constants.py
  rejection_class: substrate-first-canonical-sourcing.md Class-(f) HARD-HALT — placeholder O(10⁻²) FORBIDDEN
class_projection_source: W-12 V_4 coset (PRIMARY, conditional on W11-1-CF-66 PASS) | W-9 §EM-CN-R3-1 dual-prior 5-class (FALLBACK)
upstream_optional_dependencies:
  - computations/s87_w7_xi_E_per_class.npz  # if W9a-CF-42 PASSes first
  - computations/s87_w11_v4_monodromy_explicit.npz  # if W11-1-CF-66 PASSes first
auto_shortening_clause:
  active: true
  D_intended: 100  # N e-folds
  bands:
    valid: f_used >= 0.95
    marginal: 0.50 <= f_used < 0.95
    breakdown: f_used < 0.50
```

---

## §W9b-2. CF-58 — `S87-POLE-SPECIFICITY-SCAN`

**Source**: S86 W-9 CF-5 (compute-carryforward.md row CF-58; lizzi+transit recommending; `lizzi+transit → lizzi-spectral-functional-theorist` lead per S86 W-9 attribution; transit-dynamics-theorist co-owner per axis-pairing).

**Specialist agents**: `lizzi-spectral-functional-theorist` (lead, spectral-side authority on Mellin-cone substrate-distance pole structure per agent memory `s85_w12_4_canon_regulator_pin_discipline.md` + S86 W-9 §L-CR3.1 / §L-CR3.2 lines 1707-1755 / 1758-1806 attribution); `transit-dynamics-theorist` (co-owner, dynamical-side authority on the spectral-dynamical anti-correlation observable per S86 W-9 §T-CR2.2 / §T-DR2.1 lines 1249-1289 / 1438-1475 attribution).

**Effort**: ~1.0 wave (~10-12h compute; full Mellin-cone substrate-distance-0 evaluation at L_max=12 across 4-class projection × 5 atlas regulators).

### 1. Gate ID

`S87-POLE-SPECIFICITY-SCAN`

### 2. Trigger

`[VERIFY]` — verify whether the s=3 (substrate-distance-1) Mellin-cone Spearman ρ_S = 1.0 EXACT anti-correlation across the A_5 4-class projection (S86 W-9 §L-CR3.2 result) generalizes to s=4 (substrate-distance-0).

### 3. Classification

GEOMETRIC (substrate spectral-dynamical anti-correlation is a spectral-triple property derived from D_K eigenvalue structure under regulator-class projection; not phononic excitation, not particle quantum number — though dynamical-side observables are phononic-adjacent, the anti-correlation ITSELF is geometric per `phononic-framing.md` §"Classification Guide").

### 4. Hypothesis being tested

The Mellin-cone substrate-distance-1 spectral-dynamical anti-correlation observed at s=3 with extremality value `|ρ_S(s=3)| = 1.0 EXACT across the A_5 4-class projection` (S86 W-9 §L-CR3.2 lines 1758-1806) admits TWO substantively distinct interpretive readings:

- **Reading_1 (generic pluralism)**: the anti-correlation is structural and pole-independent. The same |ρ_S| = 1.0 extremality holds at every Mellin-cone pole including s=4 (substrate-distance-0).
- **Reading_2 (pole-specific localization)**: the anti-correlation is localized to the s=3 pole. At s=4, |ρ_S(s=4)| < 1.0 (loses extremality) OR the sign of the correlation reverses (no anti-correlation at s=4).

The discriminator predicate (per `epistemic-discipline.md` §"Pre-Registration Completeness — Pole-Scope sub-clause" T1-20 step (c)):

```
PASS-Reading_1: |ρ_S(s=4)| ≥ 0.95 AND sign(ρ_S(s=4)) = sign(ρ_S(s=3))
                (anti-correlation generalizes to s=4 with near-extremality preserved)

PASS-Reading_2: |ρ_S(s=4)| < 0.95 OR sign(ρ_S(s=4)) ≠ sign(ρ_S(s=3))
                (anti-correlation is pole-specific; either weakened OR reversed at s=4)
```

The pre-registered anchor-formula (per T1-20 step (b)):

```
ρ_S(s) := Spearman_correlation(spectral_class_projection_4_class(s), dynamical_class_projection_4_class(s))
spectral_class_projection_4_class(s)   := [a_n^{Mellin}(s) for class c ∈ {C_1, C_2, C_3, C_4} of A_5 4-class partition]
dynamical_class_projection_4_class(s)  := [⟨phi_a^{(c)}, phi_a^{(c)}⟩ Mellin-cone moment at pole s for c ∈ {C_1..C_4}]
n = 4 → s = 4 substrate-distance-0 pole evaluation; n = 6 → s = 3 substrate-distance-1 reference baseline
```

The anchor-formula is pre-registered AT PLAN-FREEZE (this document; not discovered during execution); per PRU Class 8 prevention measure, the producing script CITES this formula by §-anchor and verbatim-extract, NOT recomputes the formula structure at runtime.

### 5. Pass/fail/INFO threshold

- **PASS-Reading_1**: |ρ_S(s=4)| ≥ 0.95 AND sign(ρ_S(s=4)) = sign(ρ_S(s=3)). Tolerance rule: ABSOLUTE (Spearman ρ is bounded in [−1, +1]); threshold 0.95 = 95% extremality preservation.
- **PASS-Reading_2 (pole-specificity confirmed)**: |ρ_S(s=4)| < 0.95 OR sign mismatch. PASS routes a Reading_2-ADVISORY entry to `permanent-results-registry.md` §VII.AJ.pole-scope sub-row at S88+ Stage-1 candidate.
- **FAIL**: NOT applicable in this scan-style gate. Both readings are substantively distinct PASS outcomes (Reading_1 PASS = generalization; Reading_2 PASS = pole-specificity; either is a structural finding). FAIL reserved for: (a) numerical breakdown of Mellin-cone moment evaluation at s=4 (poles too close to next ζ-divergence; `_spectral_action_regulators.py` returns NaN or > 1e10 magnitude); OR (b) signature mismatch between independent regulators within A_5 atlas at s=4 (cross-regulator |ρ_S(s=4)| spread > 0.30).
- **INFO**: 0.85 < |ρ_S(s=4)| < 0.95 (between near-extremality and clear pole-specificity); precision-limited; rerun with extended L_max ∈ {13, 14, 15} cross-check or higher-precision Mellin-cone evaluator.

**Composite collapse rule** (S87+ schema-v2): three-tuple per gate.

- sign_verdict: PASS if Reading_1 (sign matches s=3 reference) OR if Reading_2 sign-reversal is structurally verified (sign computation succeeds; the question is which Reading the data supports, not whether the sign is well-defined); FAIL if numerical signature mismatch across atlas regulators.
- magnitude_verdict: PASS if |ρ_S(s=4)| ≥ 0.95 (Reading_1) OR |ρ_S(s=4)| < 0.85 (clear Reading_2); INFO if 0.85 ≤ |ρ_S(s=4)| < 0.95.
- regime_verdict: VALID if Mellin-cone moment evaluation at s=4 is structurally clean (all 4 classes × 5 regulators yield finite, ζ-residue-consistent moment values); MARGINAL if 1-2 (class, regulator) pairs return NaN/divergent (auto-shortening clause activates); BREAKDOWN if > 2 (class, regulator) pairs fail.

### 6. Machinery pin (PRDR)

| Field | PIN |
|:------|:----|
| `N_eval` | full bottom-20 + extended top-K spectrum at L_max=12 (master cache); ~155,984 eigenvalues addressable; class-projection on full spectrum required |
| `L_max` | 12 (canonical S84 master cache; cross-check at L_max ∈ {13, 14, 15} only if INFO band lands and precision rerun is required) |
| `scan_range` | s ∈ {3.0, 4.0} (two pole evaluations; s=3 reference baseline reproduces S86 W-9 §L-CR3.2 |ρ_S|=1.0; s=4 is the test pole). Cross-checks at s ∈ {3.5, 4.5} as MARGINAL discriminators. |
| `step_size` | N/A (discrete pole evaluation; no continuous s-scan in core gate; cross-check pole values discrete) |
| `tolerance` | ABSOLUTE `0.95` for Reading_1 PASS; ABSOLUTE `< 0.85` for clear Reading_2 PASS; INFO band [0.85, 0.95). Sign-match: STRICT (sign agrees with s=3 reference exactly). |
| `scheme` | Mellin-cone substrate-distance-0 (s=4 pole) for primary test; substrate-distance-1 (s=3 pole) for reference baseline. Per `regulator-pin-discipline.md`, output moments tagged as `a_n^{Mellin}` (zeta-divergent regularization handled via `analytic_zeta` callable in `_spectral_action_regulators.py`). |
| `convention` | A_5 4-class projection per S86 W-9 §L-CR3.2 enumeration (4 classes from A_5 5-class atlas; see §L-CR3.2 lines 1758-1806 for the specific 4-class subset). 5 atlas regulators: ζ, Pauli-Villars, Mellin (default), lattice, cutoff. |
| `random_seed` | N/A (deterministic Mellin-cone moment evaluation + Spearman correlation) |
| `GPU path` | `torch.linalg.eigh` on AMD RX 9070 XT for L_max=12 spectrum if cache regeneration required; else CPU-only Mellin-cone moment evaluation on cached eigenvalues with `OMP_NUM_THREADS=8` cap per `math-scripts.md` §Environment. Spearman correlation is trivially CPU-bound. |

### 7. Input SHA-256 pins

- `computations/canonical_constants.py` — tau_fold = 0.190, M_KK pins. Static; precompute SHA at plan-freeze.
- `computations/s84_spectrum_cache_L12_tau019.npz` — D_K(τ_fold) eigenvalues at L_max=12 (master spectrum cache from S84 W-10). Static; precompute SHA at plan-freeze.
- `computations/_spectral_action_regulators.py` — Mellin-cone callable wrapper. level pin: PRIMARY (full physical Mellin-cone via `analytic_zeta`, NOT SCHEMATIC schematic). Verify `convention=substrate-distance-{0,1}-MELLIN` (NOT `-SCHEMATIC`) per `substrate-first-canonical-sourcing.md` §(iv). Static; precompute SHA at plan-freeze.
- `sessions/archive/session-86/session-86-w9-workshop.md` lines 1438-1475 (anchor-formula pre-registration substrate per pole-scope sub-clause T1-20 step (b)) AND lines 1535-1585 (3-class partition / 4-class projection) AND lines 1758-1806 (s=3 reference baseline |ρ_S|=1.0 EXACT). Static workshop-output; precompute SHA at plan-freeze.
- `sessions/permanent-results-registry.md` §VII.AJ.pole-scope-OPEN-RESERVATION marker (if landed via W9a-CF-22 sub-decompositions; conditional). Static; precompute SHA at plan-freeze.

### 8. Expected output 4-tuple

`(value=|ρ_S(s=4)|, scheme=Mellin-cone-substrate-distance-0, convention=A_5-4-class-projection-W9-LCR3.2, L_max=12)`

Auxiliary `.npz` keys:
- `rho_S_s3[1]` (reference baseline at s=3; reproduces S86 W-9 §L-CR3.2 |ρ_S| = 1.0 EXACT)
- `rho_S_s4[1]` (gate value at s=4 substrate-distance-0)
- `rho_S_per_regulator_s4[5]` (per-atlas-regulator ρ_S at s=4; cross-regulator consistency check)
- `spectral_projection_s3[4]` (4-class spectral-axis values at s=3 reference)
- `spectral_projection_s4[4]` (4-class spectral-axis values at s=4 gate)
- `dynamical_projection_s3[4]` (4-class dynamical-axis values at s=3 reference)
- `dynamical_projection_s4[4]` (4-class dynamical-axis values at s=4 gate)
- `cross_check_s3p5[1]`, `cross_check_s4p5[1]` (intermediate-pole MARGINAL discriminator values)
- `reading_classification[str]` ("Reading_1_PASS" | "Reading_2_PASS" | "INFO" | "FAIL_numerical")

### 9. Substitution chain (sign/direction discipline per `math-scripts.md`)

```
Step 1: Definitions
   spectral_proj(s, c)   := a_n^{Mellin}(s) restricted to A_5 4-class partition class c                  [n=2(s−1) for substrate-distance-(4-n/2) pole; s=3 ↔ a_4; s=4 ↔ a_2]
   dynamical_proj(s, c)  := ⟨phi_a^{(c)}, phi_a^{(c)}⟩ Mellin-moment at pole s in class c               [class-projected dynamical-axis observable]
   ρ_S(s)                := Spearman(spectral_proj(s, c), dynamical_proj(s, c)) over c ∈ {C_1, C_2, C_3, C_4}   [Spearman rank correlation across 4 classes]

Step 2: Reference baseline (S86 W-9 §L-CR3.2)
   ρ_S(s=3) = ±1.0 EXACT                   [substrate-distance-1 pole; |ρ_S| = 1.0 across A_5 4-class projection]
   sign(ρ_S(s=3)) = − (anti-correlation)   [per S86 W-9 §L-CR3.2 anti-correlation finding]

Step 3: Test substitution at s=4 (substrate-distance-0)
   ρ_S(s=4) = Spearman(spectral_proj(s=4, c), dynamical_proj(s=4, c))   [computed per the 4-class projection at the s=4 Mellin pole]

Step 4: Reading discriminator
   PASS-Reading_1 (generic pluralism):
     IF |ρ_S(s=4)| ≥ 0.95 AND sign(ρ_S(s=4)) = sign(ρ_S(s=3))
     THEN anti-correlation generalizes; pole-INDEPENDENT structural property
   PASS-Reading_2 (pole-specific localization):
     IF |ρ_S(s=4)| < 0.95  OR  sign(ρ_S(s=4)) = +(weakened or reversed)
     THEN anti-correlation localizes to s=3; pole-SPECIFIC structural property

Step 5: Direction prediction (substrate prior)
   Reading_2 (pole-specific) is the substrate-prior expectation per Mellin-cone substrate-distance pole structure:
     - s=3 substrate-distance-1 hits the a_4 spectral-action moment (Yang-Mills + Higgs quartic load-bearing per Connes-Chamseddine)
     - s=4 substrate-distance-0 hits the a_2 spectral-action moment (Einstein-Hilbert kinematic skeleton per Connes-Chamseddine)
     The phenomenological content of a_2 vs a_4 is structurally distinct (Phi correspondence per agent-standards.md §"Layer-Decomposition" T2-7);
     anti-correlation across 4-class projection is unlikely to be pole-INDEPENDENT given this structural distinction.
     Substrate prior: Reading_2 PASS expected (pole-specificity); |ρ_S(s=4)| ≲ 0.6-0.85 with possible sign reversal.

Step 6: Sign vs magnitude vs regime verdict separation (per S87+ schema-v2)
   sign_verdict = PASS if sign computation succeeds and sign-match-or-reversal is well-defined;
                  FAIL if cross-regulator sign signature mismatch >0.30 spread.
   magnitude_verdict = PASS if |ρ_S(s=4)| ≥ 0.95 (Reading_1) OR |ρ_S(s=4)| < 0.85 (clear Reading_2);
                       INFO if 0.85 ≤ |ρ_S(s=4)| < 0.95.
   regime_verdict   = VALID if all 4-class × 5-regulator Mellin-cone evaluations yield finite, ζ-residue-consistent values;
                      MARGINAL if 1-2 (class, regulator) pairs return NaN/divergent;
                      BREAKDOWN if > 2 (class, regulator) pairs fail.
```

### 10. What PASS and FAIL mean for the solution space

- **PASS-Reading_1 (generic pluralism)**: |ρ_S(s=4)| ≥ 0.95 with sign-match. The Mellin-cone substrate-distance pole anti-correlation is pole-INDEPENDENT — a structural property of the A_5 4-class projection that holds across the Mellin-cone substrate-distance hierarchy. Strong reading: the 4-class partition is more fundamental than the pole-axis it is evaluated at. Lands `Reading_1-CONFIRMED-GENERIC-PLURALISM` annotation in S87 verdict file; routes to permanent-results-registry §VII.AJ.pole-scope sub-row at S88+ Stage-1 candidate as a generic-pluralism theorem candidate (per `joint-theorem-promotion.md` Stage-0 → Stage-1 pathway, since this is a JOINT spectral+dynamical theorem requiring two-axis verification at S88+ Stage-2).
- **PASS-Reading_2 (pole-specific localization)**: |ρ_S(s=4)| < 0.95 OR sign reversal. The s=3 anti-correlation is LOCALIZED to the substrate-distance-1 pole; it does not extend to s=4 substrate-distance-0. Strong reading: the pole-axis carries structural information that is NOT subordinate to the 4-class partition; the partition is pole-conditioned. Closes generic-pluralism interpretation at the Mellin-cone substrate-distance hierarchy. Routes to permanent-results-registry §VII.AJ.pole-scope sub-row at S88+ Stage-1 candidate as a pole-specificity-confirmed theorem candidate (with explicit s=3-only scoping per `epistemic-discipline.md` §"Source Reconciliation — Resolution-Specificity Scoping sub-clause" T1-21).
- **FAIL (numerical breakdown)**: Mellin-cone moment evaluation at s=4 fails OR cross-regulator signature spread > 0.30. The s=4 pole is too close to the next ζ-divergence for clean evaluation in the current `_spectral_action_regulators.py` infrastructure; OR the 5 atlas regulators give substantively distinct ρ_S values (regulator-class scheme dependence at s=4). Routes to S88+ infrastructure remediation: extend `_spectral_action_regulators.py` Mellin-cone callable to handle pole-proximate regularization OR re-pre-register the gate at a pole farther from the next ζ-divergence.
- **INFO (0.85 ≤ |ρ_S(s=4)| < 0.95)**: precision-limited; cross-pole behavior is intermediate between Reading_1 and Reading_2. Rerun with extended L_max ∈ {13, 14, 15} cross-check at S88+; promote to ADVISORY-S2 in `_source_reconciliation_audit.py` advisory list pending higher-L precision rerun.
- **MARGINAL or BREAKDOWN regime_verdict**: auto-shortening clause activates per `gate-verdicts.md` §"Auto-shortening clause discipline"; the gate value remains numerically well-defined but its physical interpretation is degraded. Per composite collapse rule, regime_verdict=BREAKDOWN forces composite=FAIL regardless of magnitude.

### 11. Multi-output decomposition (per `agent-standards.md` HIGH-DENSITY WORKSHOP TEMPLATE T2-5)

CF-58 is a HIGH-DENSITY output that produces multiple independent OUTPUT slots from a single pole-specificity probe (per T2-5 calibration corpus instance #1 — V_4 monodromy precedent at S86 W-12):

1. **Literal pre-reg verdict slot**: `S87-POLE-SPECIFICITY-SCAN` itself emits a PASS-Reading_1 OR PASS-Reading_2 OR INFO OR FAIL verdict per §5 thresholds.
2. **Structural candidate slot at moment-integral layer (Reading_1 path)**: §VII.AJ.pole-scope.generic-pluralism candidate; routes to S88+ Stage-1 candidate per `joint-theorem-promotion.md`.
3. **Structural candidate slot at moment-integral layer (Reading_2 path)**: §VII.AJ.pole-scope.pole-specific candidate; routes to S88+ Stage-1 candidate with explicit s=3-only scoping per `epistemic-discipline.md` T1-21.
4. **Methodology validation slot**: pre-registered anchor-formula (per T1-20 step (b)) is validated by the producing script citing it verbatim — this validates the PRU Class 8 prevention measure (anchor-formula pinned at plan-freeze; not discovered at execution).
5. **Cross-regulator atlas calibration slot**: per-regulator ρ_S(s=4) values give a 5-point scheme-dependence calibration on the s=4 Mellin pole; informs `regulator-pin-discipline.md` whether substrate-distance-0 is regulator-class-stable.

This gate's verdict line emission services slot 1; slots 2+3 become S88+ candidate landings depending on Reading; slot 4 is in-script validation; slot 5 is a side-output to the npz that informs future regulator-class work.

### 12. Output artifacts

- Script: `computations/s87_w9b_pole_specificity_scan.py` (~400-600 lines; loads cached spectrum + 5-regulator Mellin-cone callable, applies 4-class projection per S86 W-9 §L-CR3.2 enumeration, computes spectral_proj and dynamical_proj at s ∈ {3, 4} reference + test, computes ρ_S per s and per regulator, evaluates Reading classification, emits dual-SHA verdict line + 3-tuple annotation companion row).
- Data: `s87_w9b_pole_specificity_scan.npz` per §8 keys.
- Plot: `s87_w9b_pole_specificity_scan.png` (4-panel: scatter spectral_proj vs dynamical_proj at s=3 with ρ_S = ±1.0 line; same at s=4 with computed ρ_S line; per-regulator ρ_S(s=4) bar chart with 5-atlas spread; cross-pole intermediate-s discriminator panel at s ∈ {3, 3.5, 4, 4.5}).
- Verdict line: appended to `computations/s87_gate_verdicts.txt` per S87+ schema-v2 (canonical line + dual-SHA companion + 3-tuple annotation row [sign / magnitude / regime]).
- Working-paper section: `sessions/archive/session-87/session-87-w9b-workingpaper.md` §W9b-2 (>15 lines; full Reading_1 vs Reading_2 substitution chain + pre-registered anchor-formula verbatim-extract + 5-regulator atlas spread audit trail + Phi correspondence cross-link to a_2 vs a_4 spectral-action moment structure).
- (CONDITIONAL post-PASS) Registry pre-allocation: `sessions/permanent-results-registry.md` §VII.AJ.pole-scope sub-row OPEN-RESERVATION update (no landing in this sub-wave; just reservation-marker update).

### 13. YAML pin

```yaml
gate_id: S87-POLE-SPECIFICITY-SCAN
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: VERIFY
classification: GEOMETRIC
specialist_agent: lizzi-spectral-functional-theorist  # lead
co_owner: transit-dynamics-theorist
trigger_subtype: SIGN_AND_MAGNITUDE  # 3-tuple annotation required per S87+ schema-v2
sign_verdict_predicted: PASS  # sign computation succeeds; the question is which Reading
magnitude_verdict_predicted: PASS-Reading_2  # substrate prior: pole-specificity; |ρ_S(s=4)| < 0.85 expected
regime_verdict_at_risk: VALID-or-MARGINAL  # s=4 substrate-distance-0 pole is closer to a_2 ζ-divergence than s=3 was to a_4
pole_scope_sub_clause: epistemic-discipline.md T1-20  # pre-registration discipline
resolution_specificity_sub_clause: epistemic-discipline.md T1-21  # if Reading_2 PASS, registry text scopes to "the A_5 4-class projection at s=3"
pre_registered_anchor_formula:
  s_values: [3.0, 4.0]
  s_cross_check: [3.5, 4.5]
  spectral_projection: a_n^{Mellin}(s)_per_class_4
  dynamical_projection: phi_a_phi_a_Mellin_moment_per_class_4
  rho_S_definition: Spearman(spectral_proj, dynamical_proj) over 4 classes
  reference_baseline: rho_S(s=3) = ±1.0 EXACT  # S86 W-9 §L-CR3.2 lines 1758-1806
discriminator_predicate:
  Reading_1_PASS: |rho_S(s=4)| >= 0.95 AND sign-match
  Reading_2_PASS: |rho_S(s=4)| < 0.95 OR sign-reversal
  INFO: 0.85 <= |rho_S(s=4)| < 0.95
  FAIL_numerical: cross-regulator signature spread > 0.30 OR NaN/divergence in Mellin evaluation
high_density_workshop: true
output_slots: [literal_preg_verdict, structural_VII_AJ_generic_pluralism_candidate, structural_VII_AJ_pole_specific_candidate, methodology_anchor_formula_validation, cross_regulator_atlas_calibration]
auto_shortening_clause:
  active: true
  D_intended: 5  # 5 atlas regulators × 4 classes = 20 (regulator, class) pairs
  bands:
    valid: ge_18_pairs_clean
    marginal: 14_to_17_pairs_clean
    breakdown: lt_14_pairs_clean
canonical_pins:
  source_spectrum_cache: computations/s84_spectrum_cache_L12_tau019.npz
  source_mellin_callable: computations/_spectral_action_regulators.py  # PRIMARY only, NOT SCHEMATIC
  source_4_class_partition_enumeration: sessions/archive/session-86/session-86-w9-workshop.md lines 1535-1585
  source_s3_reference_baseline: sessions/archive/session-86/session-86-w9-workshop.md lines 1758-1806
upstream_optional_dependencies:
  - sessions/permanent-results-registry.md §VII.AJ.pole-scope-OPEN-RESERVATION marker (W9a-CF-22-conditional)
```

---

## Sub-Wave 9b → next-sub-wave Decision Point

**Outcomes feeding S87 close + S88+ planning**:

- **W9b-1 PASS (Reading_A confirmed: per-class IC heterogeneity propagates to N_breakdown)**: per-R N_breakdown_observable values land as canonical_constants entries (`N_breakdown_R{i}` for i ∈ {1, 2, 3, 4}) per `math-scripts.md` §"Canonical Write-Order" Step 2. Downstream gates citing "the" SR-LO regime-validity boundary must re-spec to per-R restriction. Carry-forward to S88+: `S88-SR-LO-PER-CLASS-DOWNSTREAM-RESPEC` audit walks all S87+ gates citing canonical N_breakdown for re-spec under per-class restriction.

- **W9b-1 FAIL (Reading_B: R-invariance)**: F_2-class STRUCTURAL-PRIMACY interpretation closes at the SR-LO regime-validity layer. Forces re-examination at S88+: does F_2-class STRUCTURAL-PRIMACY survive at any layer beyond IC? Carry-forward: `S88-F2-CLASS-PRIMACY-LAYER-AUDIT` examines remaining downstream consumers (n_s ranked-route, A_s closure, c_sub branch trajectories) for per-class detectability.

- **W9b-1 INFO**: precision rerun at S88+ with finer dN and extended N-window; promote to ADVISORY-S2 in source-reconciliation advisory list.

- **W9b-2 PASS-Reading_1 (generic pluralism)**: §VII.AJ.pole-scope.generic-pluralism candidate routes to S88+ Stage-1 candidate registry-landing (per `joint-theorem-promotion.md` Stage-0 → Stage-1; CF-58 is the joint-theorem author-pair authoring step at Stage-0 in S86 W-9; this gate is the S87 Stage-1 candidate-evaluation step). Stage-2 two-agent independent-verify carries forward to S88+ as `S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY`.

- **W9b-2 PASS-Reading_2 (pole-specific localization)**: §VII.AJ.pole-scope.pole-specific candidate routes to S88+ Stage-1 candidate with explicit s=3-only scoping per T1-21. Carry-forward: `S88-POLE-SCOPE-S3-SPECIFIC-VERIFY` Stage-2 two-agent independent-verify under the resolution-specificity scoping discipline.

- **W9b-2 INFO**: L_max ∈ {13, 14, 15} precision rerun at S88+; carry-forward `S88-POLE-SPECIFICITY-LMAX-PRECISION-RERUN`.

- **W9b-2 FAIL (numerical breakdown OR regulator-class signature mismatch)**: routes to S88+ infrastructure remediation. Carry-forward: `S88-MELLIN-CONE-S4-INFRASTRUCTURE-EXTEND` to extend `_spectral_action_regulators.py` Mellin-cone callable for s=4-proximate regularization, OR re-pre-register the gate at a pole farther from the next ζ-divergence.

**Cross-sub-wave dependency check**: W9b-1 and W9b-2 are independent (no pin overlap beyond canonical_constants.py). Both can dispatch in parallel.

**Cross-wave dependency check (latent)**: if W11-1-CF-66 (V_4 monodromy) lands first with PASS verdict, W9b-1 may use V_4 coset α(R) coefficients as PRIMARY input (replacing dual-prior fallback). If W9a-CF-42 lands first, W9b-1 may use per-class xi values as enriched input (replacing affine class-projection construction). Per `feedback_dispatch-discipline.md`, neither is a halt condition; W9b dispatches with the canonical-fiducial fallbacks if the optional upstream gates have not landed.

---

## Sub-Wave 9b Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md` §"Pre-Registration Completeness — PRDR" and the canonical machinery-enumeration discipline.

| Gate | N_eval | L_max | scan_range | step_size | tolerance | scheme | convention | random_seed | GPU path |
|:-----|:-------|:------|:-----------|:----------|:----------|:-------|:-----------|:------------|:---------|
| `S87-RESCALED-IC-SR-LO-RERUN` | 4 R values + 1 canonical = 5 SR-LO trajectories | N/A (SR-LO field-theoretic; spectral cache referenced via xi_E_GGE_inv only) | N ∈ [0, 100] e-folds; R ∈ {R_1, R_2, R_3, R_4} affine class-projection | dN = 0.01 (cross-validated dN = 0.005 on canonical-fiducial only) | RATIO 0.05 PASS / [0.005, 0.05] INFO / ≤ 0.005 FAIL | SR-LO Mukhanov-Sasaki ODE: `d²ζ/dN² + (3 + ε − 2η) dζ/dN + (k²/(aH)²) ζ = 0` truncated at LO in (ε, η); IC ξ²₀(R) = xi_E_GGE_inv · α(R)² | substrate-natural-xi-E-GGE-class-projected; α(R) from W-12 V_4 cosets (PRIMARY) or W-9 §EM-CN-R3-1 dual-prior 5-class (FALLBACK) | 42 (deterministic primary; perturbation cross-check only) | CPU-only with `OMP_NUM_THREADS=8` |
| `S87-POLE-SPECIFICITY-SCAN` | full bottom-20 + extended top-K spectrum at L_max=12 (~155,984 eigenvalues) | 12 (master cache); L_max ∈ {13, 14, 15} only on INFO precision rerun | s ∈ {3.0, 4.0} primary; s ∈ {3.5, 4.5} cross-check | N/A (discrete pole evaluation) | ABSOLUTE 0.95 PASS-Reading_1 / [0.85, 0.95) INFO / < 0.85 PASS-Reading_2; cross-regulator spread > 0.30 = FAIL | Mellin-cone substrate-distance-{0, 1} via `analytic_zeta` callable in `_spectral_action_regulators.py` (PRIMARY full physical, NOT SCHEMATIC schematic) | A_5 4-class projection per S86 W-9 §L-CR3.2; 5 atlas regulators {ζ, Pauli-Villars, Mellin, lattice, cutoff} per `regulator-pin-discipline.md` | N/A (deterministic) | CPU-only with `OMP_NUM_THREADS=8` for cached-eigenvalue Mellin moments; `torch.linalg.eigh` on AMD RX 9070 XT only if L_max regeneration required |

---

## Sub-Wave 9b Input-SHA Ledger

Static-input SHA pins are `<CANONICAL>` placeholders to be filled by `_plan_upstream_pin_validator.py` at S87 plan-freeze.

| Pin | Path | Used by | SHA pin |
|:----|:-----|:--------|:--------|
| `canonical_constants_py` | `computations/canonical_constants.py` | W9b-1, W9b-2 | `<CANONICAL>` (xi_E_GGE_inv = 13.642473425595973; tau_fold = 0.190; M_KK; Delta_BCS; K_base) |
| `branch_iv_canonical_md` | `sessions/framework/registry/branch-iv-canonical.md` | W9b-1 | `<CANONICAL>` (substrate-natural anchor xi_E_GGE_inv = 59.8 · Δ_BCS / K_base derivation) |
| `s84_spectrum_cache` | `computations/s84_spectrum_cache_L12_tau019.npz` | W9b-2 | `<CANONICAL>` (D_K eigenvalues at L_max=12, τ_fold=0.190) |
| `spectral_action_regulators_py` | `computations/_spectral_action_regulators.py` | W9b-2 | `<CANONICAL>` (Mellin-cone callable; PRIMARY verification) |
| `s86_w9_workshop_md_anchor_formula` | `sessions/archive/session-86/session-86-w9-workshop.md` lines 1438-1475 | W9b-2 | `<CANONICAL>` (T1-20 step (b) anchor-formula pre-registration substrate) |
| `s86_w9_workshop_md_4_class_partition` | `sessions/archive/session-86/session-86-w9-workshop.md` lines 1535-1585 | W9b-1, W9b-2 | `<CANONICAL>` (W-9 §EM-CN-R3-1 dual-prior 5-class enumeration; A_5 4-class partition) |
| `s86_w9_workshop_md_s3_reference_baseline` | `sessions/archive/session-86/session-86-w9-workshop.md` lines 1758-1806 | W9b-2 | `<CANONICAL>` (s=3 reference |ρ_S| = 1.0 EXACT baseline result) |
| `permanent_results_registry_md` | `sessions/permanent-results-registry.md` | W9b-2 (CONDITIONAL) | `<CANONICAL>` (§VII.AJ.pole-scope OPEN-RESERVATION marker; conditional on W9a-CF-22 sub-decompositions landing) |
| `s87_w7_xi_E_per_class_npz` (LATENT) | `computations/s87_w7_xi_E_per_class.npz` | W9b-1 (CONDITIONAL on W9a-CF-42) | `<RUNTIME>` (resolved at script entry by `os.path.exists`; SHA pinned at runtime if present) |
| `s87_w11_v4_monodromy_explicit_npz` (LATENT) | `computations/s87_w11_v4_monodromy_explicit.npz` | W9b-1 (CONDITIONAL on W11-1-CF-66) | `<RUNTIME>` (resolved at script entry by `os.path.exists`; SHA pinned at runtime if present) |

**End of session-87-plan-w9b.md.**
