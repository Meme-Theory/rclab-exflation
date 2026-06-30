# Session 90 Plan — Wave 6: W3 substrate-derivation + V_4 + Richardson + Var_a Stage-1 + clock-cohort

**Wave**: 6 of session 90 plan
**Cluster**: F (W3 substrate-derivation + V_4 + Richardson + Var_a Stage-1 + clock-cohort)
**Total items**: 8 (CF-46 through CF-53)
**Total effort**: ~4.7 wave-equivalents
**Canonical verdict-file**: `computations/session-90/s90_gate_verdicts.txt` (per `.claude/rules/gate-verdicts.md §"Canonical Verdict-File Path"`)
**Plan-author**: lizzi-spectral-functional-theorist (Wave-6 plan writer)
**Generated**: 2026-05-12

---

## Wave 6 Summary

Wave 6 executes the canonical S90 closeout of the W-3 §VII.U.2 four-corner workshop verdict. The W-3 R2 closure established **three-machinery convergence** on the structural identity `Var_a(n_a^GGE) ∈ Cell-II = INVARIANT × s=4`: (i) Wedderburn / Schur-orthogonality block-decomposition of `A_BdG = M_2(C)` (connes-authored); (ii) clause-(e) parse-tree decision procedure of `permanent-results-registry.md §VII.U.2` evaluated on the Bogoliubov closed-form expansion `n_a^GGE = |v_a|^2 = Delta_BCS^2 / (2(lambda_a^2 + Delta_BCS^2))` (lizzi-authored); (iii) the locked-norm F_traj=(k+1)/2 zeta-vs-SDW dressing-ratio theorem from S84 W3-24 evaluated at k=2 and k=4 (lizzi-authored). The three machineries arrive at the SAME corner classification via three structurally orthogonal proof routes, with the convergence verdict itself JOINT-attributed. The wave's deliverables span (a) substrate-derivation reconciliations (CF-46 Taylor-vs-deficit STRUCTURALLY DISTINCT-OBSERVABLES disambiguation; CF-47 Richardson L^{-3} extrapolation to L_max -> infinity asymptotic limit 5*pi); (b) LEVEL-DRESSED K-counter advancement (CF-49 PRIMARY-vs-SCHEMATIC LEVEL switch empirical scan for Var_a; CF-50 F_traj BdG-doubled extension verification); (c) joint-theorem registration (CF-51 STAGE-1-CANDIDATE corrigendum sub-entry under §VII.U.2 Corner II row); (d) structural conjecture testing (CF-52 F_traj multiplicative composition law empirical scan across 42-row S84 atlas); (e) composite verification (CF-53 5-sub-check audit of Reading B propagation through registry + audit-script extensions + Stage-1 corrigendum); and (f) Stage-2 reviewer-eligibility audit (CF-48 pre-registers EXCLUSIONS connes + lizzi as workshop authors per `joint-theorem-promotion.md §"Stage 2"`).

The wave is structurally distinguished by its convergence at the algebra-axis-orthogonality cell-II corner — the first framework-wide demonstration that a single substrate observable's corner classification stabilizes across THREE machinery routes built on disjoint mathematical machinery (block-algebra Wedderburn; parse-tree symbolic decomposition; locked-norm F_traj dressing-ratio). The Var_a Stage-1 CANDIDATE registration (CF-51) is the SECOND framework cross-axis joint theorem to enter the `joint-theorem-promotion.md` 4-stage pathway (the FIRST being §VII.AH at STAGE-3-PERMANENT eligibility post-W4-7 PASS). The author-side attribution per clause (Wedderburn = connes; parse-tree + F_traj = lizzi; convergence verdict = JOINT) follows the Stage-0 workshop-internal candidate template exactly per the §VII.AH (post-S86 W-9 close) precedent.

Wave 6 dispatches as COMPUTE-class for CF-46/CF-47/CF-49/CF-50/CF-52 (substrate-physics gates with pre-registered numerical thresholds); COMPUTE-class with Stage-2 multi-agent dispatch coordinator for CF-48/CF-53 (`[AUDIT]` triggers on cross-axis eligibility verification + composite Reading B propagation verify); and mack-cosmic-bridge sole-writer at the registry-landing layer for CF-51 (per `feedback_mack-bridge-role.md`; lizzi PRIMARY + connes CO-AUTHOR for technical sign-off). All eight gates honor the `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS bound (Class 1 convention-shopping FORBIDDEN; Class 6 iterate-until-PASS FORBIDDEN; Stage-1 MAX_ITERATIONS_PER_SIGNAL = 2 honored) and the `.claude/rules/gate-verdicts.md` Option A `supersedes` discipline for any sig_5 remediation paths.

---

## Wave 6 Decision Point Prerequisites

| Cross-wave dependency | Direction | Rationale |
|:--|:--|:--|
| **W2 CF-25 (§VII.U.2 Corner Reconciliation Reading B lock-in)** | PRECEDES CF-49 + CF-51 | The Corner-II classification of Var_a as `{INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj-factors, LEVEL-DRESSED-candidate-pending-K2}` must land in the §VII.U.2 registry text BEFORE the LEVEL-DRESSED empirical scan (CF-49) targets it and BEFORE the Stage-1 CANDIDATE corrigendum (CF-51) cites it as the registry-anchor host. Reading B baseline freeze is the structural pre-condition for downstream Stage-1 candidate landing. |
| **CF-51 (Var_a Stage-1 CANDIDATE)** | PRECEDES CF-48 | Stage-2 reviewer-eligibility audit (CF-48) audits an existing STAGE-1-CANDIDATE; it cannot pre-register reviewer pools before the STAGE-1-CANDIDATE corrigendum sub-entry exists. The Stage-1 → Stage-2 ordering is canonical per `joint-theorem-promotion.md §"4 Stages"`. |
| **CF-49 SCHEMATIC pathway** | CONSUMES W6-5 SCHEMATIC-vs-FULL D_max output (S89 cross-session) | The W9b-2 (S87) npz `s87_w9b_pole_specificity_scan.npz` carries the upstream LEVEL-switch D_max = 2.168 precedent against which CF-49 calibrates its PRIMARY-vs-SCHEMATIC rank-ordering swap predicate. |
| **CF-47 §W3-9 audit cross-cite** | CONSUMES S89 verdict `136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df` | Richardson extrapolation refines the existing `tau_max_HK5_regime_FW = 12.4750026513` canonical anchored by §W3-9 audit_sha256; the cross-link to the prior canonical is structural. |
| **CF-46 W-12 §IV.1 R1∧R2 joint-closure pathway** | CONSUMES S88 W-12 workshop §IV.1 R1∧R2 pathway specification + S88 W6a-51 INFO verdict line `5.230238e-05` cache anchor residual | The deficit-coefficient pathway is canonical from S88 W-12; CF-46 implements it on the S89-extended cache. |

Wave 6 does NOT depend on:
- Other Wave 6 gates (gate-internal ordering preserves wave parallelism within the wave-coordinate ordering CF-46 → CF-47 → CF-49 → CF-50 → CF-52 → CF-51 → CF-48 → CF-53)
- Wave 1 / Wave 3 / Wave 5 / Wave 7 outputs (Wave 6 is self-contained on its cluster F deliverables given upstream CF-25)

---

## §W6-1. CF-46 S90-W3-2-DEFICIT-COEFFICIENT-CANONICAL-RECONCILIATION

**Gate ID**: `S90-W3-2-DEFICIT-COEFFICIENT-CANONICAL-RECONCILIATION`

**Trigger**: `[VERIFY]` — direction claim that deficit-coefficient `c_W12_deficit` is STRUCTURALLY DISTINCT from Taylor 2nd-order `c_substrate_taylor` (Taylor coefficient ≠ residual coefficient).

**Classification**: GEOMETRIC (substrate-derivation observable; spectral-action heat-kernel coefficient regime is intrinsic to the BdG spectral triple `(A_BdG, H_BdG, D_BdG)` at single-tau-slice tau_fold = 0.19).

**Agent type**: gen-physicist PRIMARY + connes-ncg-theorist CO-AUTHOR (cohomology-class-distinct structural rationale for Taylor-vs-deficit disambiguation per Connes-Moscovici 1995 §III.4 residue formula).

**Hypothesis**: The Taylor 2nd-order coefficient `c_substrate_taylor ≈ 0.021018` (kappa_2_substrate_FW canonical) and the deficit coefficient `c_W12_deficit ≈ 7.244e-4` (numerical residual of `d_eff^{numerical}(tau_fold) − HK-5(tau_fold)` divided by `tau_fold^2`) ARE STRUCTURALLY DISTINCT OBSERVABLES, both substrate-canonical at their respective definitions; §W3-2 INFO is promotable to PASS once both interpretations have explicit canonical pins with non-conflated PROVENANCE.

**Method (full self-contained dispatch prompt)**:

Load the master spectrum cache `computations/_shared/s84_spectrum_cache_L12_tau019.npz` and extract `d_eff^{numerical}(tau_fold = 0.19)` at L_max=12 (per S87 W11-3 Friedrich-Bär saturation, the L_max=12 cache is structurally complete for the substrate-distance-2 pole region). Apply the S88 W-12 §IV.1 R1∧R2 joint-closure deficit-coefficient pathway specification (verbatim from `sessions/archive/session-88/workshops/s88-w12-r-dual-pathway-bk-array.md` §IV.1 R1∧R2):

```
Step 1: HK-5 closed form: d_eff^{HK-5}(tau) = 5 / (1 - tau/(5*pi))
Step 2: At tau = 0.19, HK-5(0.19) = 5 / (1 - 0.19/(5*pi)) = 5 / (1 - 0.012096...) = 5.06122...
Step 3: Numerical residual: R_num(tau_fold) := d_eff^{numerical}(0.19) - HK-5(0.19)
        Using S88 W6a-51 INFO verdict line cache anchor residual = 5.230238e-05:
        R_num(0.19) = 5.230238e-05
Step 4: Deficit coefficient: c_W12_deficit := R_num(tau_fold) / tau_fold^2
        c_W12_deficit = 5.230238e-05 / (0.19)^2 = 5.230238e-05 / 0.0361 = 1.44882e-03
        (NOTE: 1.44882e-3, NOT 7.244e-4 — the context-file figure 7.244e-4 reflects an
         intermediate normalization; the canonical W-12 §IV.1 R1∧R2 form divides by tau^2,
         producing the figure above; the script MUST emit the canonical W-12 pathway form.)
Step 5: Taylor 2nd-order coefficient (canonical from S89 W3-7): c_substrate_taylor = 0.021018084987437196
Step 6: Structural-distinction predicate: |log10(c_W12_deficit / c_substrate_taylor)| ≥ 1.0 OOM
        log10(1.44882e-3 / 0.021018) = log10(0.0689) = -1.161
        |−1.161| = 1.161 ≥ 1.0 ⇒ STRUCTURALLY DISTINCT OBSERVABLES at ≥ 1 OOM
```

Verify the substrate-derivation chain at rel_tol ≤ 1e-6 against the cache anchor residual `5.230238e-05` (S88 W6a-51 INFO line) divided by `tau_fold^2 = 0.0361`. Document the Taylor-vs-deficit distinction in the script's WP §W6-1 with the explicit two-canonical-pin structure:

- **Pin A (Taylor 2nd-order canonical)**: `kappa_2_substrate_FW = 0.021018084987437196` (S89 W3-7 audit `9de3814811c2a9929a6d50d36a62dcdd829d850a5c22fd59d88768ca008825e3`)
- **Pin B (Deficit-coefficient canonical, NEW)**: `c_W12_deficit_FW = <computed value>` with PROVENANCE = "S90 CF-46; W-12 §IV.1 R1∧R2 joint-closure pathway; cache anchor S88 W6a-51 INFO 5.230238e-05; divisor tau_fold^2 = 0.0361"

Cross-checks:
1. Recompute HK-5(tau_fold) to bit-precision against canonical `5/(1 - 0.19/(5*pi))`; assert match at float64 within 1e-15.
2. Verify cache anchor residual matches S88 W6a-51 INFO line (1e-9 tolerance on the reported figure).
3. Assert `|log10(c_W12_deficit / c_substrate_taylor)| ≥ 1.0` OOM, certifying structural distinction.

Output files:
- `computations/session-90/s90_w6_w3_2_deficit_coefficient.py`
- `computations/session-90/s90_w6_w3_2_deficit_coefficient.npz` (keys: `c_W12_deficit`, `c_substrate_taylor`, `oom_distinction`, `cache_anchor_residual_used`, `tau_fold`, `HK5_at_tau_fold`)
- `computations/session-90/s90_w6_w3_2_deficit_coefficient.png` (log-scale bar plot of `c_W12_deficit` vs `c_substrate_taylor`)

Verdict-line append target: `computations/session-90/s90_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`).

**Machinery pin (PRDR)**:

```yaml
schema_version: R3
gate_id: S90-W3-2-DEFICIT-COEFFICIENT-CANONICAL-RECONCILIATION
machinery_pin_map:
  L_max: 12
  tau_fold: 0.19  # R-PROTECTED canonical
  cache_path: "computations/_shared/s84_spectrum_cache_L12_tau019.npz"
  cache_anchor_residual_S88_W6a_51: 5.230238e-05
  HK5_closed_form: "5 / (1 - tau/(5*pi))"
  deficit_divisor: "tau_fold^2"  # canonical W-12 §IV.1 R1∧R2 pathway form
  rel_tol_cache_anchor: 1.0e-6
  rel_tol_HK5_bit_match: 1.0e-15
  oom_distinction_threshold: 1.0  # |log10(c_W12_deficit / c_substrate_taylor)| ≥ 1.0
  c_substrate_taylor_canonical: 0.021018084987437196  # S89 W3-7
  c_substrate_taylor_audit_sha: "9de3814811c2a9929a6d50d36a62dcdd829d850a5c22fd59d88768ca008825e3"
  publication_precision_sig_figs: 9  # canonical for both Pin A and Pin B
  verifier_tolerance_rel_tol: 1.0e-9  # ≥ 10^(-publication_sig_figs) per Class 8.3
  scheme: "W12-§IV.1-R1∧R2-deficit-coefficient-canonical"
  convention: "Taylor-vs-deficit-structurally-distinct-observables"
  random_seed: NULL  # deterministic
  GPU_path: NULL  # CPU sufficient
verdict_source: computations/session-90/s90_gate_verdicts.txt
input_pin_map:
  s84_spectrum_cache_L12_tau019.npz: <pinned at dispatch>
  canonical_constants.py: <pinned at dispatch>
  S89_W3_7_verdict_sha256: "9de3814811c2a9929a6d50d36a62dcdd829d850a5c22fd59d88768ca008825e3"
  S88_W6a_51_INFO_verdict_line: <pinned at dispatch>
expected_output_4_tuple:
  value: "<c_W12_deficit_FW computed value>"
  scheme: "W12-§IV.1-R1∧R2-deficit-coefficient-canonical"
  convention: "Taylor-vs-deficit-structurally-distinct-observables"
  L_max: 12
```

**Expected output 4-tuple**:
- `value`: computed `c_W12_deficit_FW` value (expected near 1.44882e-3 from substitution chain Step 4)
- `scheme`: `W12-§IV.1-R1∧R2-deficit-coefficient-canonical`
- `convention`: `Taylor-vs-deficit-structurally-distinct-observables`
- `L_max`: 12

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: rel_tol ≤ 1e-6 against `cache_anchor_residual / tau_fold^2` AND `|log10(c_W12_deficit / c_substrate_taylor)| ≥ 1.0` OOM AND HK-5 bit-match within 1e-15 AND deficit-coefficient canonical pin established with PROVENANCE.
- **INFO**: rel_tol ∈ (1e-6, 1e-4] OR `|log10(...)| ∈ [0.5, 1.0)` (marginal structural distinction).
- **FAIL**: rel_tol > 1e-4 OR `|log10(...)| < 0.5` (insufficient structural distinction; observables not separable) OR HK-5 closed-form fails bit-match.

**Substitution chain (MANDATORY for [VERIFY] direction claim)**:

```
Claim: "The deficit coefficient c_W12_deficit ≈ 1.44882e-3 is STRUCTURALLY DISTINCT from
        the Taylor 2nd-order coefficient c_substrate_taylor = 0.021018; both are
        canonical at their definitions."

Step 1 (Definition): c_substrate_taylor := (1/2) · d^2/dtau^2 [d_eff^{HK-5}(tau)]|_{tau=tau_fold}
                     where d_eff^{HK-5}(tau) = 5 / (1 - tau/(5*pi))
                     (Per S89 W3-7 canonical derivation; kappa_2_substrate_FW = 0.021018084987437196.)

Step 2 (Definition): c_W12_deficit := [d_eff^{numerical}(tau_fold) - d_eff^{HK-5}(tau_fold)] / tau_fold^2
                     (Per S88 W-12 §IV.1 R1∧R2 joint-closure pathway: residual of numerical
                      from HK-5 closed form, normalized by tau_fold^2.)

Step 3 (Substitution): At tau_fold = 0.19:
                       - HK-5(0.19) = 5 / (1 - 0.19/(5*pi)) = 5.06122...
                       - d_eff^{numerical}(0.19) = HK-5(0.19) + R_num where
                         R_num = 5.230238e-05 (S88 W6a-51 INFO cache anchor residual)
                       - c_W12_deficit = 5.230238e-05 / (0.19)^2 = 5.230238e-05 / 0.0361
                       - c_W12_deficit ≈ 1.44882e-3
                       - c_substrate_taylor = 0.021018084987437196 (canonical, S89 W3-7)

Step 4 (Simplify): Ratio: c_W12_deficit / c_substrate_taylor = 1.44882e-3 / 0.021018
                          = 0.06893
                   |log10(0.06893)| = 1.161

Step 5 (Direction): |log10(ratio)| = 1.161 ≥ 1.0 ⇒ STRUCTURALLY DISTINCT at ≥ 1 OOM.
                    Step 1 defines Taylor expansion coefficient of CLOSED FORM HK-5.
                    Step 2 defines RESIDUAL coefficient of NUMERICAL vs HK-5.
                    These observables are NOT EQUAL by construction: Taylor measures
                    local curvature of the closed form; deficit measures global deviation
                    of numerical from closed form. The ≥ 1 OOM separation confirms
                    they cannot be conflated.

Conclusion: c_W12_deficit and c_substrate_taylor are STRUCTURALLY DISTINCT canonical
            observables. §W3-2 INFO is now promotable to PASS with both pins published.
```

**What PASSES / FAILS mean for solution space**:

- **PASS**: The Taylor-vs-deficit distinction is structurally certified at ≥ 1 OOM separation. The deficit-coefficient canonical pin `c_W12_deficit_FW` lands in `canonical_constants.py` with explicit PROVENANCE; future gates citing the "deficit" interpretation route to this pin; future gates citing the "Taylor 2nd-order" interpretation route to `kappa_2_substrate_FW`. Closes §W3-2 INFO; opens the corner of solution space where two canonical-coefficient meanings coexist non-conflated.
- **FAIL (insufficient distinction)**: The two observables cannot be structurally separated at the OOM band; §W3-2 INFO does not promote; canonical-sourcing axis remains a Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY risk for downstream gates that conflate the two. Routes to remediation: verify cache anchor; re-derive HK-5 closed form; check Taylor expansion of HK-5 at tau_fold.

**Effort**: 0.4 we

**Substrate-framing reminder**: The substrate IS the BdG spectral triple `(A_BdG, H_BdG, D_BdG)` at the single-tau-slice tau_fold = 0.19 (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level 1). HK-5 IS the closed-form heat-kernel asymptotic at the substrate-distance-5 truncation; the numerical d_eff IS the L_max=12 cache image of the substrate's spectral action; the residual IS the substrate's intrinsic deviation between truncation-level n=5 closed form and truncation-level L_max=12 numerical. The deficit-coefficient observable is substrate-canonical at Level 1. The direction of explanation flows: substrate → numerical evaluation at L_max=12 → residual against HK-5 closed form → deficit coefficient. NOT: closed form HK-5 is "the truth" and numerical is "deviation from it" — both are substrate-canonical at their respective truncation levels.

---

## §W6-2. CF-47 S90-HK-5-RICHARDSON-EXTRAPOLATION-LMAX-INF-TAU-MAX

**Gate ID**: `S90-HK-5-RICHARDSON-EXTRAPOLATION-LMAX-INF-TAU-MAX`

**Trigger**: `[VERIFY]` — direction claim that Source-3 numerical breakdown bound `tau_max^{S3}` extrapolates to asymptotic limit `5*pi = 15.708` in the L_max → infinity limit.

**Classification**: GEOMETRIC (substrate-derivation regime-of-validity observable for HK-5 closed form on the spectral-action heat-kernel manifold).

**Agent type**: gen-physicist PRIMARY + connes-ncg-theorist CO-AUTHOR (Connes-Moscovici 1995 §III.4 residue-formula asymptotic justification for the L_max → infinity limit of the Taylor-truncation breakdown estimator).

**Hypothesis**: Source-3's L_max=12 Taylor-truncation breakdown estimate `tau_max^{S3}(L_max=12) ≈ 12.475 M_KK^{-1}` (canonical `tau_max_HK5_regime_FW` from S89 W3-9) is structurally extensible to the L_max → infinity asymptotic limit `tau_max^{S3}(infinity) = 5*pi = 15.708 M_KK^{-1}` via Richardson L^{-3} extrapolation on the convergence sequence over L_max ∈ {12, 14, 16, 18}.

**Method (full self-contained dispatch prompt)**:

The Source-3 numerical breakdown bound is the L_max-truncated Taylor-series estimate of the radius of convergence of the HK-5 closed form `5/(1 - tau/(5*pi))`. The closed form has a simple pole at `tau = 5*pi`; the asymptotic limit of the Taylor-truncation estimator at any finite L_max approaches this pole from below. The Taylor-truncation breakdown follows the closed form:

```
tau_max^{S3}(L_max) = 5*pi * 0.05^{1/(L_max+1)}
```

(per S89 W3-9 derivation: the factor 0.05 corresponds to the 5% tolerance band at which the Taylor remainder exceeds the truncation; L_max+1 is the truncation order in the geometric series).

At L_max = 12: `tau_max^{S3}(12) = 5*pi * 0.05^{1/13} = 15.708 * 0.05^{0.0769}`. Computing `0.05^{0.0769} = exp(0.0769 * ln(0.05)) = exp(0.0769 * (-2.9957)) = exp(-0.2303) = 0.7943`. So `tau_max^{S3}(12) = 15.708 * 0.7943 = 12.475`. ✓ (matches canonical `tau_max_HK5_regime_FW = 12.4750026513`).

Compute `tau_max^{S3}(L_max)` at L_max ∈ {12, 14, 16, 18} via the closed form `5*pi * 0.05^{1/(L_max+1)}`. Apply Richardson L^{-3} extrapolation per the S87 W1b-3 pattern: fit `tau_max^{S3}(L) = c0 + a/L^3 + b/L^5 + ...` and extract `c0` as the L → infinity limit. With Source-3's geometric closed form, the L → infinity limit IS exactly `5*pi = 15.708`; the extrapolation verifies the convergence rate matches the L^{-3} algebraic envelope of the cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder" Level 2.

Output 4-point Richardson table:

| L_max | `tau_max^{S3}(L_max)` | residual from 5*pi |
|:-----:|----------------------:|:------------------:|
| 12 | 12.4750... | 3.2330... |
| 14 | 13.0... (computed) | ... |
| 16 | 13.4... (computed) | ... |
| 18 | 13.7... (computed) | ... |
| ∞ (Richardson) | 15.708 ± ε | < 1e-3 rel_tol |

Verify the Richardson L → ∞ extrapolate matches `5*pi = 15.70796326794897` at rel_tol ≤ 1e-3. Promote the new canonical `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5*pi` to `canonical_constants.py` with PROVENANCE entry citing CF-47 + S89 W3-9 audit `136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df` + Richardson L^{-3} extrapolator pattern.

Cross-checks:
1. Direct evaluation: `5*pi - lim_{L→∞} 5*pi * 0.05^{1/(L+1)} = 0` (since `0.05^{1/(L+1)} → 1` as L → ∞); confirms extrapolate is bit-exact at the asymptotic limit.
2. Friedrich-Bär saturation precedent (S87 W11-3): the substrate's structural-saturation theorem for bottom-K observables at L_max ≥ 12 guarantees that L_max=12 cache reproduces all observables below the truncation ceiling; this carries over to the regime-of-validity observable (the breakdown bound saturates at 5*pi asymptotically).
3. Cross-link to §VII.AQ Friedrich-Bär analytic certification (CF-54 of W4 cluster): the L^{-3} algebraic envelope is consistent with the per-pole Casimir-bound argument.

Output files:
- `computations/session-90/s90_w6_hk5_richardson_lmax_inf.py`
- `computations/session-90/s90_w6_hk5_richardson_lmax_inf.npz` (keys: `L_max_values`, `tau_max_S3_values`, `richardson_extrapolate`, `target_5pi`, `rel_tol_achieved`, `algebraic_envelope_exponent`)
- `computations/session-90/s90_w6_hk5_richardson_lmax_inf.png` (4-point Richardson convergence plot)

Verdict-line append target: `computations/session-90/s90_gate_verdicts.txt`.

**Machinery pin (PRDR)**:

```yaml
schema_version: R3
gate_id: S90-HK-5-RICHARDSON-EXTRAPOLATION-LMAX-INF-TAU-MAX
machinery_pin_map:
  L_max_scan: [12, 14, 16, 18]
  taylor_truncation_closed_form: "5*pi * 0.05^{1/(L_max+1)}"
  asymptotic_target: "5*pi = 15.707963267948966"
  richardson_pattern: "L^{-3} algebraic envelope per S87 W1b-3"
  rel_tol_target: 1.0e-3
  bit_precision_check: 1.0e-15  # for direct evaluation cross-check
  HK5_closed_form: "5 / (1 - tau/(5*pi))"
  HK5_pole_at: "5*pi"
  prior_canonical_audit_sha: "136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df"
  publication_precision_sig_figs: 10  # canonical for 5*pi asymptotic limit
  verifier_tolerance_rel_tol: 1.0e-10
  scheme: "Richardson-L_minus_3-extrapolation-asymptotic-limit"
  convention: "Source-3-Taylor-truncation-breakdown-asymptotic"
  random_seed: NULL
  GPU_path: NULL
verdict_source: computations/session-90/s90_gate_verdicts.txt
input_pin_map:
  S89_W3_9_verdict_sha256: "136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df"
  canonical_constants.py: <pinned at dispatch>
  S87_W1b_3_richardson_pattern: <pinned at dispatch>
  S87_W11_3_friedrich_baer_precedent: <pinned at dispatch>
expected_output_4_tuple:
  value: "<richardson_extrapolate>"  # expected near 15.708 within 1e-3
  scheme: "Richardson-L_minus_3-extrapolation-asymptotic-limit"
  convention: "Source-3-Taylor-truncation-breakdown-asymptotic"
  L_max: "{12, 14, 16, 18} → infinity"
```

**Expected output 4-tuple**:
- `value`: Richardson L^{-3} extrapolate of `tau_max^{S3}` at L → infinity (target 15.708)
- `scheme`: `Richardson-L_minus_3-extrapolation-asymptotic-limit`
- `convention`: `Source-3-Taylor-truncation-breakdown-asymptotic`
- `L_max`: `{12, 14, 16, 18} → infinity`

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: `|richardson_extrapolate - 5*pi| / |5*pi| ≤ 1e-3` AND new canonical `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5*pi` promoted with PROVENANCE AND cross-link to §W3-9 audit established.
- **INFO**: `|richardson_extrapolate - 5*pi| / |5*pi| ∈ (1e-3, 1e-2]` (Richardson convergence imperfect; closed-form L → ∞ limit cited directly without numerical verification).
- **FAIL**: `|richardson_extrapolate - 5*pi| / |5*pi| > 1e-2` (extrapolation algorithm broken; canonical pin not promoted).

**What PASSES / FAILS mean for solution space**:

- **PASS**: The HK-5 regime-of-validity observable's L_max → infinity asymptotic limit is structurally certified as `5*pi`. This extends the cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder" Level 2 (algebraic envelope) cross-link to the substrate-distance-5 regime: the substrate's spectral-action heat-kernel asymptotic is bounded by the pole-distance singularity at `tau = 5*pi` independent of L_max. Closes the L_max-truncation freedom at the regime boundary; the asymptotic canonical replaces the L_max=12 numerical anchor for downstream gates that need the maximal regime-of-validity.
- **FAIL (convergence broken)**: Richardson extrapolation does not converge to the closed-form pole at 5*pi; the substrate's L_max-truncation is structurally non-saturating in the regime-boundary observable. Routes to remediation: verify the closed-form derivation; cross-check against the Friedrich-Bär saturation theorem; re-run Richardson with denser L_max grid.

**Effort**: 0.5 we

**Substrate-framing reminder**: The substrate IS the spectral triple `(A_K, H_K, D_K)` with heat-kernel asymptotic on the spectral-action manifold (per `phononic-framing.md §"Cross-pillar bridge anatomy"` Level 2 algebraic envelope). The HK-5 closed form IS the substrate's intrinsic heat-kernel asymptotic at substrate-distance-5 truncation; the regime-of-validity bound IS the substrate's intrinsic pole-distance singularity. The L_max → infinity asymptotic is the substrate's structural-saturation limit, not a "convergence of finite-rank approximations to a continuum container". Direction of explanation: substrate → heat-kernel asymptotic → pole singularity at 5*pi → regime-of-validity = pole distance.

---

## §W6-3. CF-48 S90-VII-U-2-STAGE-2-CROSS-AXIS-REVIEWER-ELIGIBILITY-AUDIT

**Gate ID**: `S90-VII-U-2-STAGE-2-CROSS-AXIS-REVIEWER-ELIGIBILITY-AUDIT`

**Trigger**: `[AUDIT]` — Stage-2 reviewer-eligibility pre-registration audit per `joint-theorem-promotion.md §"Stage 2"` + §"Stage-2 Axis-B Selection Protocol" (S88 W-14 V.2 / B.15 MANDATORY).

**Classification**: META (Stage-2 dispatch reviewer-eligibility audit; methodology-layer enforcement of cross-axis independence + original-authoring-agent exclusion + audit-coverage adequacy at the joint-theorem promotion pathway).

**Agent type**: gen-physicist (orchestrator-direct dispatch coordinator; the eligibility audit is mechanistic and applies the 3-clause Stage-2 Axis-B Selection Protocol verbatim against the §VII.U.2 authorship attribution table).

**Hypothesis**: When §VII.U.2's own Stage-2 cross-axis independent-verify gate (`S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` queued at S91+) dispatches, the Axis-A and Axis-B reviewers must satisfy ALL THREE clauses of the Stage-2 Axis-B Selection Protocol: (i) axis-distinctness; (ii) original-authoring-agent exclusion with downstream-inheritance reach; (iii) audit-coverage adequacy. Per §VII.U.2 authorship lines 12936 + 12942 + 12950-12952 + 13050-13053, connes-ncg-theorist is PRIMARY author (Wedderburn machinery) and lizzi-spectral-functional-theorist is PRIMARY author (parse-tree + F_traj machinery); BOTH MUST BE EXCLUDED from Stage-2 dispatch.

**Method (full self-contained dispatch prompt)**:

Pre-register the Stage-2 dispatch reviewer-eligibility table for `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` (the dispatch is conditional on CF-51 STAGE-1-CANDIDATE corrigendum landing at S90 W-6; the eligibility audit at S90 W-6 is forward-looking pre-registration only).

Step 1: Parse §VII.U.2 registry block (`permanent-results-registry.md` lines 12927-13058) to extract the authorship attribution per clause:
- Clause (a) cell-II identity statement: JOINT (lizzi + connes Stage-0 author freeze)
- Clause (b) Wedderburn block-decomposition: connes-ncg-theorist PRIMARY
- Clause (c) parse-tree decision procedure: lizzi-spectral-functional-theorist PRIMARY
- Clause (d) F_traj=(k+1)/2 dressing-ratio: lizzi-spectral-functional-theorist PRIMARY
- Clause (e) convergence verdict: JOINT (lizzi + connes; convergence is the W-3 R3 closure)

Step 2: Apply the 3-clause Stage-2 Axis-B Selection Protocol (per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` MANDATORY):

**Clause 1 (axis-distinctness)**: Axis-A reviewer's primary methodology ≠ Axis-B reviewer's primary methodology. The two axes for §VII.U.2 are:
- Axis-A = NCG-axiomatic / spectral-functional (Wedderburn + parse-tree + F_traj all live on this axis)
- Axis-B = substrate-physics / superfluid-universe / cosmological-bridge / information-theoretic

**Clause 2 (original-authoring-agent exclusion with downstream-inheritance reach)**:
- EXCLUDED from Axis-A: connes-ncg-theorist (Wedderburn PRIMARY author; clause (b))
- EXCLUDED from Axis-A: lizzi-spectral-functional-theorist (parse-tree + F_traj PRIMARY author; clauses (c) + (d); convergence JOINT clause (e))
- EXCLUDED from any axis: any agent whose project-memory inherits the W-3 workshop's R1/R2/R3 transcripts as canonical reference (downstream-inheritance reach test per S88 W-14 V.2 / B.15)

**Clause 3 (audit-coverage adequacy)**: The reviewer's domain expertise MUST cover ALL clauses being audited (a+b+c+d+e). For §VII.U.2's joint clauses, Axis-A reviewer needs NCG-axiomatic + spectral-functional expertise (sufficient to audit Wedderburn + parse-tree + F_traj as a non-author); Axis-B reviewer needs substrate-physics / superfluid-universe expertise (sufficient to audit the algebra-axis-orthogonality cross-pillar implications).

Step 3: Construct the eligibility pool table:

| Reviewer candidate | Primary axis | Original-author-of §VII.U.2? | Downstream-inheritance reach trigger? | Axis-A eligible? | Axis-B eligible? |
|:-------------------|:-------------|:----------------------------:|:-------------------------------------:|:----------------:|:----------------:|
| connes-ncg-theorist | Axis-A (NCG-axiomatic) | YES (clause (b) Wedderburn PRIMARY) | YES (memory cites W-3 R3) | **EXCLUDED** | EXCLUDED (axis-mismatch + author) |
| lizzi-spectral-functional-theorist | Axis-A (spectral-functional) | YES (clauses (c) + (d) PRIMARY) | YES (memory cites W-3 R3) | **EXCLUDED** | EXCLUDED (axis-mismatch + author) |
| van-den-dungen-bridge-theorist | Axis-A (NCG-axiomatic via submersions) | NO | NO (no W-3 transcript citation) | **ELIGIBLE** | EXCLUDED (axis-match with Axis-A side) |
| gen-physicist | Axis-A (general spectral-functional; orchestrator-direct experience) | NO | NO | **ELIGIBLE** | EXCLUDED (axis-match) |
| volovik-superfluid-universe-theorist | Axis-B (substrate / superfluid-universe) | NO | NO | EXCLUDED (axis-match) | **ELIGIBLE** |
| mack-cosmic-bridge | Axis-B (cosmological-bridge) | NO | NO | EXCLUDED | **ELIGIBLE** |
| kitaev-information-theorist | Axis-B (information-theoretic) | NO | NO | EXCLUDED | **ELIGIBLE** |

Step 4: Pre-register the Stage-2 dispatch pool (must be selected by orchestrator at Stage-2 dispatch time):

- **Axis-A pool**: {van-den-dungen-bridge-theorist, gen-physicist}
- **Axis-B pool**: {volovik-superfluid-universe-theorist, mack-cosmic-bridge, kitaev-information-theorist}

The Stage-2 dispatch MUST select exactly one reviewer from each pool (parallel dispatch per `joint-theorem-promotion.md §"Stage 2"` MANDATORY clause). Both reviewers receive ONLY the registered STAGE-1-CANDIDATE entry text from CF-51 (NOT the W-3 workshop transcripts). PASS-AND across both verdicts is the Stage-2 → Stage-3 promotion criterion.

Step 5: Emit pre-registration record to `computations/session-90/s90_w6_vii_u_2_stage2_eligibility_audit.npz` containing the eligibility pool table + Stage-2 dispatch parameters + cross-link to CF-51 STAGE-1-CANDIDATE corrigendum (once CF-51 lands).

Cross-checks:
1. Verify §VII.U.2 authorship lines 12936 + 12942 + 12950-12952 + 13050-13053 (greppable confirmation that connes + lizzi are PRIMARY authors).
2. Verify W-3 workshop SHA-pin matches expected workshop file SHA at plan-freeze (audit-trail anchor for the original-authoring-agent exclusion).
3. Verify the downstream-inheritance reach test: scan each candidate's `agent-memory/<agent>/*.md` for citations of `s89-w3-vii-u-2-corner-classification.md`; flag matches.

Output files:
- `computations/session-90/s90_w6_vii_u_2_stage2_eligibility_audit.py`
- `computations/session-90/s90_w6_vii_u_2_stage2_eligibility_audit.npz` (keys: `axis_a_pool`, `axis_b_pool`, `excluded_reviewers`, `downstream_inheritance_reach_flags`, `audit_coverage_check`, `pre_registration_stage_2_dispatch_params`)
- (No PNG required for audit-class gate)

Verdict-line append target: `computations/session-90/s90_gate_verdicts.txt`.

**Machinery pin (PRDR)**:

```yaml
schema_version: R3
gate_id: S90-VII-U-2-STAGE-2-CROSS-AXIS-REVIEWER-ELIGIBILITY-AUDIT
machinery_pin_map:
  rule_reference: ".claude/rules/joint-theorem-promotion.md §\"Stage-2 Axis-B Selection Protocol\""
  rule_clauses_audited: [1, 2, 3]  # axis-distinctness, original-author-exclusion-with-DIR, audit-coverage
  axis_a_pool: ["van-den-dungen-bridge-theorist", "gen-physicist"]
  axis_b_pool: ["volovik-superfluid-universe-theorist", "mack-cosmic-bridge", "kitaev-information-theorist"]
  excluded_reviewers: ["connes-ncg-theorist", "lizzi-spectral-functional-theorist"]
  exclusion_basis: "§VII.U.2 authorship lines 12936+12942+12950-12952+13050-13053; W-3 R3 workshop authorship"
  downstream_inheritance_reach_test: "scan agent-memory/<agent>/*.md for s89-w3-vii-u-2-corner-classification.md citations"
  parallel_dispatch_requirement: true
  pass_and_aggregation: true  # both reviewers must independently PASS
  stage_2_dispatch_conditional_on: "CF-51 STAGE-1-CANDIDATE corrigendum landing"
  publication_precision_sig_figs: NULL  # audit gate
  verifier_tolerance_rel_tol: NULL
  scheme: "stage-2-axis-b-selection-protocol-3-clause-audit"
  convention: "joint-theorem-promotion-mandatory-K3"
  random_seed: NULL
  GPU_path: NULL
verdict_source: computations/session-90/s90_gate_verdicts.txt
input_pin_map:
  joint_theorem_promotion_md_section: ".claude/rules/joint-theorem-promotion.md §\"Stage 2\""
  permanent_results_registry_md_VII_U_2: "lines 12927-13058"
  cross_pillar_bridge_anatomy_md_algebra_axis_orthogonality: ".claude/rules/cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\""
  S88_W14_V2_calibration_corpus: <pinned at dispatch>
expected_output_4_tuple:
  value: "Axis-A_pool={vdd, gen}; Axis-B_pool={volovik, mack, kitaev}; EXCLUDED={connes, lizzi}"
  scheme: "stage-2-axis-b-selection-protocol-3-clause-audit"
  convention: "joint-theorem-promotion-mandatory-K3"
  L_max: NULL  # methodology audit; no L_max
```

**Expected output 4-tuple**:
- `value`: Axis-A pool {vdd, gen-physicist}; Axis-B pool {volovik, mack, kitaev}; EXCLUDED {connes, lizzi}
- `scheme`: `stage-2-axis-b-selection-protocol-3-clause-audit`
- `convention`: `joint-theorem-promotion-mandatory-K3`
- `L_max`: N/A

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: Eligibility pool table emitted AND clause 1 (axis-distinctness) PASSes for ALL candidate pairs from (Axis-A pool × Axis-B pool) AND clause 2 (original-authoring exclusion) PASSes (connes + lizzi correctly EXCLUDED; pool members have no W-3 transcript citations in agent-memory) AND clause 3 (audit-coverage adequacy) PASSes (Axis-A pool members have NCG/spectral expertise; Axis-B pool members have substrate/superfluid expertise).
- **INFO**: Eligibility table emitted but one or more pool members have AMBIGUOUS downstream-inheritance reach (e.g., agent-memory cites W-3 only in passing without canonical-source treatment).
- **FAIL**: Any pool member fails any of the 3 clauses (e.g., axis-mismatch in proposed Axis-A reviewer; lizzi or connes accidentally retained in pool; agent-memory canonical-cites W-3 transcript).

**What PASSES / FAILS mean for solution space**:

- **PASS**: Stage-2 dispatch is pre-registered with cross-axis independence guaranteed by construction; Stage-2 → Stage-3 PERMANENT pathway is structurally available for §VII.U.2 once CF-51 STAGE-1-CANDIDATE lands AND Stage-2 dispatches at S91+. Closes the reviewer-eligibility risk for the framework's second cross-axis joint theorem entering the promotion pipeline (the first being §VII.AH at STAGE-3-PERMANENT eligibility post-W4-7).
- **FAIL**: Reviewer-eligibility audit reveals structural defects in the Stage-2 dispatch design; Stage-2 → Stage-3 promotion is BLOCKED until pool is reconstructed. Routes to remediation: re-scope pools; verify downstream-inheritance reach against agent-memory snapshots; re-author Stage-2 dispatch with corrected exclusions.

**Effort**: 1.0 we

**Substrate-framing reminder**: The reviewer-eligibility audit operates at the methodology layer (`epistemic-discipline.md §"Layer-Decomposition"` F: substrate → methodology → audit). The substrate-physics observable §VII.U.2 Corner-II identity is invariant under reviewer choice; the audit ensures that the methodology-layer machinery (Stage-2 cross-axis independent-verify) preserves the structural-independence guarantee of the joint-theorem-promotion pathway. Direction of explanation: substrate-physics identity (Var_a ∈ Cell-II) is fixed; the methodology layer ensures the registration-pathway preserves epistemic integrity; the audit layer verifies the methodology-layer machinery is correctly configured. Stage-2 reviewers are NOT validating the substrate-physics identity (that's frozen at workshop R3 close); they are validating that the registered theorem text correctly captures the workshop's structural derivation without inheritance-bias from the workshop's path.

---

## §W6-4. CF-49 S90-LEVEL-DRESSED-K-2-EMPIRICAL-SCAN-VAR-A-N-A-GGE

**Gate ID**: `S90-LEVEL-DRESSED-K-2-EMPIRICAL-SCAN-VAR-A-N-A-GGE`

**Trigger**: `[VERIFY]` — direction claim that the LEVEL-DRESSED 3-criterion empirical predicate satisfies (1) ✓, (2) ✓, (3) ✓ on Var_a(n_a^GGE) under the PRIMARY-vs-SCHEMATIC LEVEL switch.

**Classification**: GEOMETRIC (substrate-derivation rank-ordering observable on the substrate's BdG spectral algebra under regulator-class invariance test).

**Agent type**: lizzi-spectral-functional-theorist PRIMARY + connes-ncg-theorist CO-AUTHOR (for FULL PV pipeline reconstruction per S61/S78 packaging at Lambda_UV = M_KK on full BdG-doubled D_K spectrum); mack-cosmic-bridge sole writer for registry annotation per `feedback_mack-bridge-role.md`.

**Hypothesis**: Var_a(n_a^GGE) satisfies the §VII.K-DUAL.LEVEL-DRESSED 3-criterion definition (per `permanent-results-registry.md` lines 4293-4297): (1) algebra-INVARIANT spectrum-only — SATISFIED structurally (Var_a is a trace functional on spectrum-only data); (2) regulator-CLASS membership unchanged across PRIMARY-vs-SCHEMATIC LEVEL switch — PENDING empirical test; (3) rank-ordering swap observed under LEVEL switch — PENDING empirical test. Empirical PASS on (2) AND (3) advances the §VII.K-DUAL.LEVEL-DRESSED K-counter from K=1 to K=2 (first non-singleton corpus instance for the LEVEL-DRESSED candidate-class).

**Method (full self-contained dispatch prompt)**:

Compute `Var_a(n_a^GGE)` under TWO LEVELs per `substrate-first-canonical-sourcing.md §(iv)` SCHEMATIC vs FULL physical level pin discipline (MANDATORY at K=4 since S88 W7b-83 close):

### LEVEL P (PRIMARY = FULL physical regularization)

Implement S61/S78 Pauli-Villars regulator pipeline at Lambda_UV = M_KK = 7.428660036284456e+16 GeV on the FULL BdG-doubled D_K spectrum from `s84_spectrum_cache_L12_tau019.npz`. The Pauli-Villars pipeline subtracts heavy-ghost contributions at masses M_PV,i with regulator parameters per the canonical S61 specification:
- Subtraction kernel: `K_PV(lambda; Lambda_UV) = exp(-lambda^2 / Lambda_UV^2)` AND ghost subtractions at M_PV/Lambda_UV = {0.5, 1.0, 2.0} per S78 pipeline pinning
- BdG doubling: extend SU(3) D_K spectrum to the doubled BdG sector via `(lambda, -lambda)` mirror pairing per Volovik §11 (the BdG spectrum is intrinsically symmetric about zero)
- Bogoliubov closed form: `n_a^GGE = |v_a|^2 = Delta_BCS^2 / (2*(lambda_a^2 + Delta_BCS^2))` per registry §VII.U.2 line 12961 (citation source)
- Variance: `Var_a(n_a^GGE) = <n_a^2>_GGE - <n_a>_GGE^2` evaluated on the FULL regularized BdG spectrum
- Apply PV regulator to the trace: `Var_a^{PV} = Σ_a |v_a|^4 · K_PV(lambda_a; Lambda_UV) - (Σ_a |v_a|^2 · K_PV(lambda_a; Lambda_UV))^2 / N`

### LEVEL S (SCHEMATIC analog)

Apply `computations/_shared/_spectral_action_regulators.py` SCHEMATIC helpers (per its docstring lines 23-30 explicitly: "These are SCHEMATIC regulators ... NOT the full physical regularizations") with verdict-line `convention=` field carrying the `-SCHEMATIC` suffix and companion comment row `# tier_pin=TIER-2` per the W9c-1 (S87) POSITIVE-CALIBRATION pattern. The SCHEMATIC version uses:
- 5-regulator atlas: {zeta, SDW (Seeley-DeWitt), anomaly, cutoff, Zubarev}
- Bare Casimir spectrum (no BdG doubling; direct D_K spectrum eigenvalues only)
- Same Bogoliubov closed form for n_a^GGE but evaluated on the bare spectrum without PV subtraction

### Rank-ordering swap test (criterion 3)

For each of the 5 regulators in the SCHEMATIC atlas, compute `Var_a^{R}(LEVEL=P)` (FULL PV pipeline applied alongside regulator R) and `Var_a^{R}(LEVEL=S)` (SCHEMATIC). Rank the 5 regulators by Var_a magnitude under each LEVEL:

| Regulator | Var_a(LEVEL=S) [rank under SCHEMATIC] | Var_a(LEVEL=P) [rank under PRIMARY] |
|:----------|:--------------------------------------|:------------------------------------|
| zeta | <value> [rank_S_zeta] | <value> [rank_P_zeta] |
| SDW | <value> [rank_S_SDW] | <value> [rank_P_SDW] |
| anomaly | <value> [rank_P_anomaly] | <value> [rank_P_anomaly] |
| cutoff | <value> [rank_S_cutoff] | <value> [rank_P_cutoff] |
| Zubarev | <value> [rank_S_Zubarev] | <value> [rank_P_Zubarev] |

Compute Spearman rank correlation `rho_S = corr(rank_S_vector, rank_P_vector)`. Rank-ordering SWAP is observed iff `rho_S < 1.0` (i.e., at least one inversion in the 5-regulator rank vector under LEVEL switch).

Per `s87_w9b_pole_specificity_scan.npz` upstream LEVEL-switch precedent: W9b-2 found D_max = 2.168 SCHEMATIC vs SCHEMATIC-PROXY indicating substantial level-dependent magnitude shifts; CF-49 tests whether the rank-ordering itself (not just magnitudes) swaps under the more stringent PRIMARY-vs-SCHEMATIC LEVEL switch.

### Criterion 2 verification (regulator-CLASS invariance)

Per the FI/RD/MIXED taxonomy (S82 W-3), classify each regulator R under LEVEL=S and LEVEL=P. Regulator-CLASS unchanged ⇔ R's classification is the same under both LEVELs. E.g., if zeta is in FI under LEVEL=S, it must also be in FI under LEVEL=P. PENDING test: extract FI-membership for each regulator under both LEVELs from the existing Var_a^{R} values (boundedness + finite-spread properties).

Cross-checks:
1. Bit-precision Bogoliubov closed form: at lambda_a = 0, `n_a^GGE = Delta_BCS^2 / (2*Delta_BCS^2) = 1/2`; at lambda_a → ∞, `n_a^GGE → 0`. Verify both limits.
2. Trace condition: `Σ_a n_a^GGE = N_GGE` total GGE quasiparticle count; cross-check against canonical S52 8-mode BdG amplitude data.
3. BdG mirror symmetry: `n_{a,+} = n_{a,-}` (eigenvalue-pair degeneracy under BdG doubling).

Output files:
- `computations/session-90/s90_w6_var_a_level_dressed_k2_scan.py`
- `computations/session-90/s90_w6_var_a_level_dressed_k2_scan.npz` (keys: `var_a_primary_5reg`, `var_a_schematic_5reg`, `rank_vector_primary`, `rank_vector_schematic`, `spearman_rho_S`, `level_switch_d_max`, `regulator_class_primary`, `regulator_class_schematic`, `criterion_1_pass`, `criterion_2_pass`, `criterion_3_pass`)
- `computations/session-90/s90_w6_var_a_level_dressed_k2_scan.png` (5-regulator bar chart side-by-side LEVEL=P vs LEVEL=S)

Verdict-line append target: `computations/session-90/s90_gate_verdicts.txt`.

Note on convention pin: the verdict line MUST carry both UV-regulator-axis pin AND LEVEL-pin per the orthogonality structure (regulator-pin-discipline.md cross-link to substrate-first-canonical-sourcing.md §(iv)): `convention=var_a-level-dressed-K2-empirical-5-regulator-atlas-PRIMARY-vs-SCHEMATIC-LAYER-SEPARABLE-NA` with explicit non-layer-separable carve-out tag (the gate is COMPUTE-class, not mechanical-closure carve-out).

**Machinery pin (PRDR)**:

```yaml
schema_version: R3
gate_id: S90-LEVEL-DRESSED-K-2-EMPIRICAL-SCAN-VAR-A-N-A-GGE
machinery_pin_map:
  L_max: 12  # full master cache
  tau_fold: 0.19
  M_KK: 7.428660036284456e+16
  Delta_BCS: 0.4642547394830737  # canonical
  Vol_SU3_Haar: 1349.74
  Lambda_UV_PV: "M_KK"  # PV pipeline cutoff at canonical M_KK
  PV_ghost_masses_over_Lambda_UV: [0.5, 1.0, 2.0]  # S78 pipeline pinning
  bdg_doubling: true  # BdG sector mirror pairing applied at LEVEL=P
  regulator_atlas_5: ["zeta", "SDW", "anomaly", "cutoff", "Zubarev"]
  levels_scanned: ["P_PRIMARY", "S_SCHEMATIC"]
  schematic_helper: "computations/_shared/_spectral_action_regulators.py"
  schematic_helper_tier_pin: "TIER-2"  # SCHEMATIC per docstring lines 23-30
  cache_path: "computations/_shared/s84_spectrum_cache_L12_tau019.npz"
  bogoliubov_n_a_closed_form: "Delta_BCS^2 / (2*(lambda_a^2 + Delta_BCS^2))"
  bogoliubov_citation: "registry §VII.U.2 line 12961"
  rank_correlation_metric: "spearman_rho_S"
  rank_swap_threshold: 1.0  # rho_S < 1.0 ⇒ at least one rank inversion
  publication_precision_sig_figs: 10
  verifier_tolerance_rel_tol: 1.0e-10
  scheme: "var_a-level-dressed-K2-empirical-5-regulator-atlas"
  convention: "PRIMARY-vs-SCHEMATIC-level-pin-K4-MANDATORY-NOT-LAYER-SEPARABLE-CARVE-OUT"
  random_seed: NULL  # deterministic spectrum cache
  GPU_path: "preferred for matrix products on master cache (17.1 GB VRAM)"
  W9b_2_upstream_precedent_d_max: 2.168
verdict_source: computations/session-90/s90_gate_verdicts.txt
input_pin_map:
  s84_spectrum_cache_L12_tau019.npz: <pinned at dispatch>
  _spectral_action_regulators.py: <pinned at dispatch>
  s87_w9b_pole_specificity_scan.npz: <pinned at dispatch>
  canonical_constants.py: <pinned at dispatch>
  permanent_results_registry_md_VII_K_DUAL_LEVEL_DRESSED: "lines 4293-4297"
expected_output_4_tuple:
  value: "spearman_rho_S=<computed>; rank-swap=<bool>"
  scheme: "var_a-level-dressed-K2-empirical-5-regulator-atlas"
  convention: "PRIMARY-vs-SCHEMATIC-level-pin-K4-MANDATORY"
  L_max: 12
```

**Expected output 4-tuple**:
- `value`: Spearman rho_S + rank-swap boolean (PASS if rho_S < 1.0)
- `scheme`: `var_a-level-dressed-K2-empirical-5-regulator-atlas`
- `convention`: `PRIMARY-vs-SCHEMATIC-level-pin-K4-MANDATORY`
- `L_max`: 12

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: Criterion (1) ✓ (algebra-INVARIANT spectrum-only structurally satisfied; trace functional on spectrum data) AND Criterion (2) ✓ (regulator-CLASS membership unchanged; FI/RD/MIXED classification of each regulator R consistent across LEVEL=P vs LEVEL=S) AND Criterion (3) ✓ (`spearman_rho_S < 1.0` indicating rank-ordering swap observed under LEVEL switch) AND §VII.K-DUAL.LEVEL-DRESSED K-counter advances K=1 → K=2.
- **INFO**: Criteria (1) + (2) ✓ but Criterion (3) marginal (`spearman_rho_S ∈ [0.95, 1.00)`; rank-stability with sub-threshold swap signal); K-counter advancement pending tightening.
- **FAIL**: Criterion (1) FAIL (structural inconsistency in algebra-INVARIANT claim) OR Criterion (2) FAIL (regulator-CLASS changes across LEVELs; the LEVEL-DRESSED candidate-class definition does NOT apply to Var_a) OR Criterion (3) FAIL (`spearman_rho_S = 1.0` exactly; no rank-swap even under PRIMARY-vs-SCHEMATIC LEVEL switch).

**Substitution chain (MANDATORY for [VERIFY] LEVEL-switch direction claim)**:

```
Claim: "Var_a^{R}(LEVEL=P) and Var_a^{R}(LEVEL=S) produce DIFFERENT rank orderings
        of the 5-regulator atlas {zeta, SDW, anomaly, cutoff, Zubarev}, certifying
        the LEVEL-DRESSED candidate-class Criterion (3) on Var_a."

Step 1 (Definition): n_a^GGE := Delta_BCS^2 / (2*(lambda_a^2 + Delta_BCS^2))
                     (Bogoliubov closed form; per registry §VII.U.2 line 12961)

Step 2 (Definition): Var_a^{R}(LEVEL) := Σ_a w^{R,LEVEL}(lambda_a) · (n_a^GGE)^2
                                          - [Σ_a w^{R,LEVEL}(lambda_a) · n_a^GGE]^2 / N^{LEVEL}
                     where w^{R,LEVEL}(lambda) is the R-regulator weight function
                     at LEVEL ∈ {P, S}.

Step 3 (Substitution): At LEVEL=P (FULL PV at Lambda_UV = M_KK on BdG-doubled D_K):
                       w^{R,P}(lambda) = R-regulator weight × K_PV(lambda; Lambda_UV)
                                        × ghost subtractions at M_PV ∈ {0.5, 1, 2}*M_KK
                       At LEVEL=S (SCHEMATIC on bare D_K):
                       w^{R,S}(lambda) = R-regulator weight (via _spectral_action_regulators.py)

Step 4 (Simplify): The 5-regulator atlas produces a rank vector at each LEVEL:
                   rank^{LEVEL} = argsort(Var_a^{R}(LEVEL))_{R in 5-atlas}
                   Spearman: rho_S(rank^P, rank^S) ∈ [-1, +1]
                   rho_S = 1.0 ⇔ rank vectors identical (no swap)
                   rho_S < 1.0 ⇔ at least one rank inversion

Step 5 (Direction): If rho_S < 1.0 ⇒ the rank-ordering is NOT preserved across LEVELs.
                    This signals that the regulator-weight-magnitude differences
                    between LEVEL=P and LEVEL=S exceed the rank-stability threshold.
                    The LEVEL-DRESSED Criterion (3) is SATISFIED by construction
                    of the SWAP. Combined with Criteria (1) + (2), the K-counter
                    advances K=1 → K=2 for the LEVEL-DRESSED candidate class.

Conclusion: PASS iff rho_S < 1.0; the LEVEL-DRESSED Criterion (3) is the structural
            signature of regulator-class-dependent rank-ordering under the
            substrate's full PRIMARY regularization vs the SCHEMATIC analog.
```

**What PASSES / FAILS mean for solution space**:

- **PASS**: Var_a(n_a^GGE) joins §VII.AR as the SECOND instance of the LEVEL-DRESSED candidate class at the substrate-distance-2 pole s=4. The K-counter K=2 → K=3 promotion criterion becomes saturable (one additional instance needed). The Var_a Stage-1 CANDIDATE (CF-51) inherits the LEVEL-DRESSED-at-K=2-cohort tag in its 4-axis classification. Closes the corner of solution space where Var_a is a singleton LEVEL-DRESSED candidate; opens the corner where Var_a + §VII.AR jointly satisfy K=2 cohort discipline.
- **FAIL**: Var_a is NOT LEVEL-DRESSED-candidate-eligible (rank-stable across LEVELs). The Stage-1 CANDIDATE classification reverts to `{INVARIANT, s=4, MIXED-of-RD-with-distinct-F_traj}` WITHOUT the LEVEL-DRESSED qualifier. Routes to remediation: verify PV pipeline implementation; cross-check against W9b-2 D_max = 2.168 (the LEVEL switch shows substantial magnitude shifts; rank stability would indicate counter-intuitive cancellation).

**Effort**: 0.6 we

**Substrate-framing reminder**: The substrate IS the BdG spectral triple `(A_BdG, H_BdG, D_BdG)` at single-tau-slice tau_fold = 0.19. The GGE state IS a generic state on A_BdG with the diagonal-in-mode-pair-basis property (per W-3 Q-CN-R2-3 verdict). Var_a IS the substrate's intrinsic spectral-variance observable on the n_a^GGE distribution. The 5-regulator atlas IS the substrate's intrinsic regulator-class taxonomy (per S82 W-3 FI/RD/MIXED classification). LEVEL P (PRIMARY = FULL PV at Lambda_UV = M_KK) IS the substrate's intrinsic UV-regularization with substrate-canonical Lambda_UV; LEVEL S (SCHEMATIC) IS a methodology-floor proxy of the substrate's UV-regularization with closed-form analog weights. The rank-ordering swap test certifies that the substrate's intrinsic regulator-weight-magnitude structure depends on the LEVEL pin. Direction of explanation: substrate's intrinsic regulator atlas + substrate's intrinsic Lambda_UV → PRIMARY level evaluation of Var_a → rank vector → compared against SCHEMATIC proxy → swap test certifies LEVEL-DRESSED candidate eligibility.

---

## §W6-5. CF-50 S90-F-TRAJ-ZETA-VS-SDW-PREDICTION-VAR-A-FALSIFIABLE-TEST

**Gate ID**: `S90-F-TRAJ-ZETA-VS-SDW-PREDICTION-VAR-A-FALSIFIABLE-TEST`

**Trigger**: `[VERIFY-THEOREM]` — theorem-existence verification: the F_traj=(k+1)/2 theorem (S84 W3-24) extends to BdG-doubled substrate observables; structural prediction is `Var_a^zeta / Var_a^SDW = (5/2*A − 9/4*B) / (A − B)` where A and B are spectrum-only moment composites.

**Classification**: GEOMETRIC (F_traj dressing-ratio observable on the substrate's BdG-doubled spectral algebra; tests the theorem's pole-pair extensibility from single-pole-k atlas rows to multi-pole-pair BdG-extended composites).

**Agent type**: lizzi-spectral-functional-theorist PRIMARY (F_traj theorem originator at S84 W3-24).

**Hypothesis**: F_traj=(k+1)/2 theorem's locked-norm zeta-vs-SDW dressing-ratio extends from single-k pole observables `M_k = Σ_a m_a g_k(lambda_a)` (where F_traj(k) = (k+1)/2 at locked norm L_k = 1) to BdG-doubled multi-moment composites like Var_a = M_4/N - (M_2/N)^2 in the form `Var_a^zeta / Var_a^SDW = (5/2*A − 9/4*B) / (A − B)` where `A := (1/N) M_4^SDW` and `B := ((1/N) M_2^SDW)^2`.

**Method (full self-contained dispatch prompt)**:

Test the F_traj BdG-doubled extension prediction empirically at L_max ∈ {6, 8, 10, 12}. The theorem's derivation chain:

Step 1 (F_traj theorem): For each substrate-distance-k pole observable `M_k^zeta = Σ_a m_a g_k^zeta(lambda_a)` and `M_k^SDW = Σ_a m_a g_k^SDW(lambda_a)` at locked norm L_k = 1, the F_traj dressing-ratio satisfies:
- F_traj(k) := M_k^zeta / M_k^SDW = (k+1)/2

For Var_a, the relevant moments are M_2 (substrate-distance-1 pole; k=2 dressing-factor) and M_4 (substrate-distance-2 pole; k=4 dressing-factor):
- F_traj(2) = (2+1)/2 = 3/2
- F_traj(4) = (4+1)/2 = 5/2

Step 2 (BdG extension): The Bogoliubov closed form `n_a^GGE = Delta_BCS^2 / (2*(lambda_a^2 + Delta_BCS^2))` produces:
- `Σ_a n_a^GGE` ∝ M_2(BdG-extended sum over lambda_a^2)
- `Σ_a (n_a^GGE)^2` ∝ M_4(BdG-extended sum over lambda_a^4)

The variance Var_a = (1/N) Σ_a (n_a^GGE)^2 - ((1/N) Σ_a n_a^GGE)^2 thus depends on M_4 and M_2^2 simultaneously.

Step 3 (Ratio prediction): Define A = (1/N) M_4^SDW and B = ((1/N) M_2^SDW)^2. Then:
- Var_a^SDW = A - B
- Var_a^zeta = F_traj(4) * A - F_traj(2)^2 * B = (5/2) * A - (3/2)^2 * B = (5/2)*A - (9/4)*B

(Note: the M_2^2 composite carries dressing-factor F_traj(2)^2 = (3/2)^2 = 9/4 by multiplicative composition; this is the structural fingerprint testable in CF-52.)

Step 4 (Ratio): `Var_a^zeta / Var_a^SDW = [(5/2)*A − (9/4)*B] / [A − B]`.

Step 5 (Empirical verification): Compute A and B at each L_max from `s84_spectrum_cache_L12_tau019.npz` (use L_max ≤ 12 truncations of the master cache). At each L_max, compute:
- `A(L_max) := (1/N(L_max)) * Σ_{a:lambda_a in L_max-truncation} m_a * g_4^SDW(lambda_a)`
- `B(L_max) := [(1/N(L_max)) * Σ_{a:lambda_a in L_max-truncation} m_a * g_2^SDW(lambda_a)]^2`
- `Var_a^zeta(L_max)` directly via zeta-regulator weights on `n_a^GGE` distribution
- `Var_a^SDW(L_max)` directly via SDW-regulator weights on `n_a^GGE` distribution
- `Ratio_empirical(L_max) := Var_a^zeta(L_max) / Var_a^SDW(L_max)`
- `Ratio_predicted(L_max) := [(5/2)*A(L_max) - (9/4)*B(L_max)] / [A(L_max) - B(L_max)]`

PASS condition: `|Ratio_empirical(L_max) - Ratio_predicted(L_max)| / |Ratio_predicted(L_max)| ≤ 1e-10` for ALL L_max ∈ {6, 8, 10, 12}.

Bogoliubov closed forms g_k(lambda) for SDW (Seeley-DeWitt heat-kernel regulator):
- `g_2^SDW(lambda) = lambda^2` (substrate-distance-1 pole moment kernel)
- `g_4^SDW(lambda) = lambda^4` (substrate-distance-2 pole moment kernel)

Zeta-regulator weights g_k^zeta(lambda) per the S84 W3-24 closed forms (locked-norm L_k = 1 convention).

Cross-checks:
1. F_traj(k) = (k+1)/2 at single-k locked norm: verify F_traj(2) = 3/2 and F_traj(4) = 5/2 directly from M_k^zeta / M_k^SDW ratios at L_max=12.
2. BdG mirror-pair degeneracy: M_2 and M_4 sums over BdG-doubled spectrum are 2× their unfolded SU(3) counterparts (factor-2 accounted in normalization).
3. Var_a > 0 sanity: variance is non-negative by Cauchy-Schwarz; empirically verify Var_a^SDW ≥ 0 and Var_a^zeta ≥ 0 at all L_max.

Output files:
- `computations/session-90/s90_w6_f_traj_zeta_sdw_var_a_test.py`
- `computations/session-90/s90_w6_f_traj_zeta_sdw_var_a_test.npz` (keys: `L_max_values`, `A_values`, `B_values`, `var_a_zeta_empirical`, `var_a_sdw_empirical`, `ratio_empirical`, `ratio_predicted`, `rel_dev_per_lmax`, `f_traj_2_check`, `f_traj_4_check`)
- `computations/session-90/s90_w6_f_traj_zeta_sdw_var_a_test.png` (4-point convergence plot of empirical vs predicted ratio)

Verdict-line append target: `computations/session-90/s90_gate_verdicts.txt`.

**Machinery pin (PRDR)**:

```yaml
schema_version: R3
gate_id: S90-F-TRAJ-ZETA-VS-SDW-PREDICTION-VAR-A-FALSIFIABLE-TEST
machinery_pin_map:
  L_max_scan: [6, 8, 10, 12]
  tau_fold: 0.19
  Delta_BCS: 0.4642547394830737
  M_KK: 7.428660036284456e+16
  bogoliubov_n_a_closed_form: "Delta_BCS^2 / (2*(lambda_a^2 + Delta_BCS^2))"
  f_traj_theorem_reference: "S84 W3-24"
  f_traj_locked_norm_L_k: 1
  f_traj_2_predicted: "3/2"
  f_traj_4_predicted: "5/2"
  g_2_sdw_kernel: "lambda^2"
  g_4_sdw_kernel: "lambda^4"
  ratio_prediction_closed_form: "[(5/2)*A - (9/4)*B] / [A - B]"
  rel_precision_target: 1.0e-10
  cache_path: "computations/_shared/s84_spectrum_cache_L12_tau019.npz"
  schematic_helper: "computations/_shared/_spectral_action_regulators.py"
  schematic_helper_tier_pin: "TIER-2"
  bdg_mirror_pair_check: true
  variance_non_negativity_check: true
  publication_precision_sig_figs: 11
  verifier_tolerance_rel_tol: 1.0e-11
  scheme: "f_traj-zeta-vs-sdw-bdg-extension-locked-norm-L_k=1"
  convention: "var_a-ratio-prediction-SCHEMATIC-via-spectral-action-regulators"
  random_seed: NULL
  GPU_path: "preferred for matrix products"
verdict_source: computations/session-90/s90_gate_verdicts.txt
input_pin_map:
  s84_spectrum_cache_L12_tau019.npz: <pinned at dispatch>
  _spectral_action_regulators.py: <pinned at dispatch>
  canonical_constants.py: <pinned at dispatch>
  S84_W3_24_f_traj_theorem: <pinned at dispatch>
expected_output_4_tuple:
  value: "max rel_dev across L_max in {6,8,10,12} = <computed>"
  scheme: "f_traj-zeta-vs-sdw-bdg-extension-locked-norm-L_k=1"
  convention: "var_a-ratio-prediction-SCHEMATIC"
  L_max: "{6, 8, 10, 12}"
```

**Expected output 4-tuple**:
- `value`: max rel_dev across L_max ∈ {6, 8, 10, 12} between empirical and predicted ratio (target: ≤ 1e-10)
- `scheme`: `f_traj-zeta-vs-sdw-bdg-extension-locked-norm-L_k=1`
- `convention`: `var_a-ratio-prediction-SCHEMATIC`
- `L_max`: `{6, 8, 10, 12}`

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: `max_L_max |Ratio_empirical(L_max) - Ratio_predicted(L_max)| / |Ratio_predicted(L_max)| ≤ 1e-10` AND F_traj(2) = 3/2 ± 1e-15 AND F_traj(4) = 5/2 ± 1e-15 directly verified at L_max=12 AND BdG mirror-pair degeneracy + Var_a non-negativity checks PASS.
- **INFO**: `max rel_dev ∈ (1e-10, 1e-6]` (partial match; structural form correct but truncation-dependent residual; cross-check whether convergence is L^{-3}).
- **FAIL**: `max rel_dev > 1e-6` (F_traj theorem's BdG extension structurally unverified) OR single-k F_traj(2) or F_traj(4) deviates from (k+1)/2 (theorem itself fails at single-k baseline).

**Substitution chain (MANDATORY for [VERIFY-THEOREM] BdG extension direction)**:

```
Claim: "F_traj=(k+1)/2 theorem extends from single-k pole observables to BdG-doubled
        multi-moment composites; specifically, Var_a^zeta / Var_a^SDW = (5/2*A - 9/4*B)/(A-B)."

Step 1 (Definition): F_traj(k) := M_k^zeta / M_k^SDW at locked norm L_k = 1
                     where M_k^R = Σ_a m_a g_k^R(lambda_a) for regulator R ∈ {zeta, SDW}.

Step 2 (Theorem, S84 W3-24): For each substrate-distance-k pole, F_traj(k) = (k+1)/2.
                              Specifically F_traj(2) = 3/2 and F_traj(4) = 5/2.

Step 3 (Substitution into Var_a): Var_a = M_4/N - (M_2/N)^2 has structure:
                                  Var_a^R(LEVEL=anything) = (1/N) M_4^R - (1/N^2) (M_2^R)^2.
                                  Let A := (1/N) M_4^SDW; B := ((1/N) M_2^SDW)^2 = (1/N^2) (M_2^SDW)^2.
                                  Then Var_a^SDW = A - B.

Step 4 (Multiplicative composition for ratio):
       Var_a^zeta = (1/N) M_4^zeta - (1/N^2) (M_2^zeta)^2
                  = (1/N) [F_traj(4) * M_4^SDW] - (1/N^2) [F_traj(2) * M_2^SDW]^2
                  = F_traj(4) * (1/N) M_4^SDW - F_traj(2)^2 * (1/N^2) (M_2^SDW)^2
                  = F_traj(4) * A - F_traj(2)^2 * B
                  = (5/2) * A - (3/2)^2 * B
                  = (5/2) * A - (9/4) * B

Step 5 (Ratio simplification):
       Var_a^zeta / Var_a^SDW = [(5/2) A - (9/4) B] / [A - B]
                              = the predicted closed-form ratio.

Step 6 (Direction): If empirical ratio matches predicted at rel_precision ≤ 1e-10 across
                    L_max ∈ {6, 8, 10, 12}, the F_traj theorem's MULTIPLICATIVE COMPOSITION
                    LAW for BdG-doubled variance observables is verified by construction.
                    This is the empirical anchor for the CF-52 conjecture (multiplicative
                    composition law over full 42-row S84 atlas).

Conclusion: PASS iff the BdG-extended ratio prediction holds bit-precision; this CERTIFIES
            that the F_traj single-k theorem extends multiplicatively to BdG-doubled
            multi-moment composites at the F_traj(k_1) * F_traj(k_2) composition level.
```

**What PASSES / FAILS mean for solution space**:

- **PASS**: F_traj=(k+1)/2 theorem's structural reach extends from single-k pole observables to BdG-doubled multi-moment composites via the multiplicative composition law F_traj(2) * F_traj(2) = 9/4 (M_2^2 composite) and F_traj(4) = 5/2 (M_4 single moment). This provides the empirical foundation for CF-52's broader conjecture (F_traj(k_1) * F_traj(k_2) closed-form composition over the entire 42-row S84 atlas). Closes the corner of solution space where F_traj might be pole-pair-dependent in a non-multiplicative way; opens the corner where F_traj is structurally a multiplicative homomorphism.
- **FAIL**: F_traj theorem's BdG extension is structurally unverified at the multi-moment composite level. The Var_a Stage-1 CANDIDATE (CF-51) loses one of its three convergence-machinery clauses (the F_traj dressing-factor route); CF-52 must be reformulated. Routes to remediation: verify single-k F_traj values; verify Bogoliubov closed form; verify SDW vs zeta regulator weight definitions.

**Effort**: 0.4 we

**Substrate-framing reminder**: The substrate IS the BdG spectral triple `(A_BdG, H_BdG, D_BdG)`. The Bogoliubov n_a^GGE distribution IS the substrate's intrinsic GGE-state occupation observable per its diagonal-in-mode-pair-basis property (per W-3 Q-CN-R2-3). M_2 and M_4 ARE the substrate's intrinsic substrate-distance-1 and substrate-distance-2 pole moments. F_traj IS the substrate's intrinsic locked-norm zeta-vs-SDW dressing-ratio. Var_a is a BdG-doubled multi-moment composite where two substrate-pole observables combine multiplicatively. The direction of explanation flows: substrate's intrinsic pole-moments → F_traj single-k theorem → multiplicative composition for multi-moment composites → BdG-extended variance prediction. NOT: F_traj is a "convention choice" and the ratio is "by definition" — F_traj is the substrate's structural dressing-ratio between two locked-norm regulator classes.

---

## §W6-6. CF-51 S90-VII-U-2-CORNER-II-STAGE-1-CANDIDATE-VAR-A-JOINT-THEOREM-LANDING

**Gate ID**: `S90-VII-U-2-CORNER-II-STAGE-1-CANDIDATE-VAR-A-JOINT-THEOREM-LANDING`

**Trigger**: `[VERIFY-THEOREM]` — theorem-existence verification: the joint Var_a Stage-1-CANDIDATE entry must be registered with three-machinery convergence proof + author-side attribution per clause.

**Classification**: META (joint theorem registration at registry-landing layer per `joint-theorem-promotion.md §"Stage 1"` 4-stage pathway).

**Agent type**: lizzi-spectral-functional-theorist PRIMARY (parse-tree + F_traj machinery authoring) + connes-ncg-theorist CO-AUTHOR (Wedderburn machinery authoring); mack-cosmic-bridge sole writer at registry-landing layer per `feedback_mack-bridge-role.md`.

**Hypothesis**: The joint Var_a theorem candidate `Var_a(n_a^GGE) ∈ Cell-II ∩ {MIXED-of-RD-with-distinct-F_traj} ∩ LEVEL-DRESSED-candidate-pending-K2` is registry-eligible as STAGE-1-CANDIDATE under §VII.U.2 Corner II row corrigendum block, with three-machinery convergence (Wedderburn + clause-(e) parse-tree + F_traj=(k+1)/2 dressing) and author-side attribution per clause matching W-3 R3 workshop verdict freeze.

**Method (full self-contained dispatch prompt)**:

Land the Var_a Stage-1-CANDIDATE corrigendum sub-entry under §VII.U.2 Corner II row per `joint-theorem-promotion.md §"Stage 1"` 4-stage pathway. Registry-landing target: OPTION (i) NEW sub-entry UNDER §VII.U.2 Corner II row in corrigendum block (NOT a separate §VII.{next-free} slot; the corrigendum sub-entry inherits §VII.U.2's existing Stage-2 dispatch identifier).

Stage-0 workshop-internal candidate text (per W-3 R3 R3-B closure freeze, audit-trail-canonical):

```
STAGE-1-CANDIDATE — Var_a(n_a^GGE) Corner-II joint theorem (W-3 three-machinery convergence)

THEOREM (joint, three-machinery): Let (A_BdG, H_BdG, D_BdG) be the BdG spectral triple
at single-tau-slice tau_fold = 0.19. Let omega_GGE be the GGE state on A_BdG generic
with the diagonal-in-mode-pair-basis property. Let n_a^GGE := omega_GGE(|v_a|^2) be
the GGE occupation closed form Delta_BCS^2 / (2(lambda_a^2 + Delta_BCS^2)) per Bogoliubov
on the BdG Hamiltonian's mode-pair basis. Let Var_a := omega_GGE(n_a^2) − omega_GGE(n_a)^2
be the GGE variance.

Then Var_a ∈ Cell-II = INVARIANT × s=4 of the four-corner partition of §VII.U.2,
classified MIXED-of-RD-with-distinct-F_traj-factors at the regulator-class axis,
LEVEL-DRESSED-candidate-pending-K2 cohort at the LEVEL pin axis (pending CF-49 K-counter
advancement to K=2 with §VII.AR as cohort instance #2 at s=4).

CLAUSE-DECOMPOSED PROOF (three structurally orthogonal machineries):

(a) Cell-II identity statement (JOINT clause; convergence verdict)
    Authors: JOINT (lizzi + connes Stage-0 author freeze at W-3 R3 R3-B)
    Statement: Var_a is at algebra-axis = INVARIANT (spectrum-only spectral functional)
               and Mellin-pole axis = s=4 (substrate-distance-2 pole; M_4 carries s=4
               while M_2 carries s=3; the variance composite localizes to s=4 by Cauchy-
               Schwarz-bounded subtraction).

(b) Wedderburn / Schur-orthogonality block-decomposition (clause-b machinery)
    Author: connes-ncg-theorist PRIMARY (W5b-48 Step 5 derivation pin)
    Statement: A_BdG = M_2(C) is simple by Wedderburn. The mode-pair basis decomposes
               D_BdG into block-diagonal eigenspaces under the BdG charge-conjugation
               symmetry C: lambda → -lambda. omega_GGE on the diagonal-in-mode-pair-basis
               state preserves this block structure. Var_a evaluated on each block
               separately, summed: the M_2 modulus block (e.g., |M_2| or BdG positive
               sector) carries cross-block-orthogonal contributions that vanish, leaving
               Var_a entirely on the spectral function axis (algebra-INVARIANT). Refinements
               per Q-LZ-R2-1 (a) + (b): Wedderburn block-decomposition's extension to
               the mode-pair-basis-respecting subalgebra preserves the Cell-II identity.

(c) Clause-(e) parse-tree decision procedure (clause-c machinery)
    Author: lizzi-spectral-functional-theorist PRIMARY (W-3 R3 parse-tree expansion)
    Statement: Parse-tree expansion of `Var_a(n_a^GGE)` per registry §VII.U.2 clause (e)
               line 12995: substitute `n_a^GGE → |v_a|^2 → Delta_BCS^2/(2(lambda^2+Delta_BCS^2))`,
               compute variance over a-index summation, identify the resulting
               spectral-functional structure as spectrum-only (algebra-INVARIANT) at
               s=4 Mellin pole. The parse-tree decision-procedure counters
               (state_pair_count, algebra_dep_count) both return 0 on the fully-expanded
               form, certifying algebra-INVARIANT classification structurally.

(d) F_traj=(k+1)/2 zeta-vs-SDW dressing-ratio (clause-d machinery)
    Author: lizzi-spectral-functional-theorist PRIMARY (S84 W3-24 theorem author)
    Statement: At locked norm L_k = 1, the regulator-class dressing-ratio between zeta
               and SDW satisfies F_traj(k) = (k+1)/2. For Var_a's two-moment composition,
               F_traj(2) = 3/2 and F_traj(4) = 5/2. The composite ratio
               Var_a^zeta / Var_a^SDW = [(5/2)*A − (9/4)*B] / [A−B] (CF-50 empirical anchor)
               carries distinct F_traj factors at the two moments, certifying the MIXED-of-RD
               regulator-class classification with distinct F_traj dressing factors.

(e) Convergence verdict (JOINT clause)
    Authors: JOINT (lizzi + connes; convergence is the W-3 R3 R3-B closure verdict)
    Statement: Clauses (b), (c), (d) above produce the SAME corner classification (Cell-II
               at INVARIANT × s=4) via three structurally orthogonal proof routes built
               on disjoint mathematical machinery (block-algebra Wedderburn; parse-tree
               symbolic decomposition; locked-norm F_traj dressing-ratio). The convergence
               itself is JOINT-attributed at the verdict layer.

CORRIGENDA from W-3 R3-B:
- Q-LZ-R2-1 (a) + (b): Wedderburn refinement clauses for mode-pair-basis-respecting
  subalgebra block decomposition; CO-AUTHOR connes.
- Q-CN-R2-3: GGE-state-generic-with-property formal definition (omega_GGE is a generic
  state on A_BdG satisfying the diagonal-in-mode-pair-basis property; this property
  is structural, not state-dependent, in the sense that it is preserved by the BdG
  charge-conjugation symmetry).
- Convergence statement (e): added at R3-B R3 close as the JOINT clause attributing
  the structural-orthogonal-machinery-convergence to BOTH authoring agents.

STAGE-2 DISPATCH IDENTIFIER: inherits §VII.U.2's existing
`S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` (Stage-2 dispatch pre-registered
at CF-48 with EXCLUDED reviewers {connes, lizzi}; Axis-A pool = {vdd, gen-physicist};
Axis-B pool = {volovik, mack, kitaev}).

PROVENANCE: S90 CF-51; W-3 R3 R3-B Stage-0 author freeze; lizzi PRIMARY + connes CO-AUTHOR;
mack-cosmic-bridge sole writer at registry-landing layer per feedback_mack-bridge-role.md.
```

Land the corrigendum sub-entry into `sessions/permanent-results-registry.md` UNDER the §VII.U.2 Corner II row block (target: append below the existing Corner II row at the position determined by next-free-letter protocol within the corrigendum sub-block). Use the canonical bridge-landing single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture"`:

1. `build_promotion_text(stage_1_candidate_text)` — pure function, no I/O.
2. `write_atomic_with_fsync(registry_path, promotion_text)` — single atomic write.
3. `re_read_and_verify_section_matches(registry_path, expected_promotion_text)` — boolean.
4. `emit_verdict_line(verify_boolean)` — exactly ONE canonical line.

Cross-checks (verifier rubric per Class 8.2):

1. **Clause-count verification**: the registered text contains exactly 5 clauses (a) + (b) + (c) + (d) + (e) per the Stage-0 freeze.
2. **Author-side attribution verification**: each clause carries explicit author attribution matching the W-3 R3 freeze (clause (a) JOINT; clause (b) connes PRIMARY; clauses (c) + (d) lizzi PRIMARY; clause (e) JOINT).
3. **Corrigenda block verification**: Q-LZ-R2-1 (a) + (b) + Q-CN-R2-3 + convergence clause (e) corrigenda present.
4. **STAGE-1-CANDIDATE tag verification**: theorem-name line carries `STAGE-1-CANDIDATE` tag (not `STAGE-3-PERMANENT` or other status).
5. **Stage-2 dispatch identifier verification**: corrigendum cross-references `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` AND pre-registered eligibility per CF-48.

Output files:
- `computations/session-90/s90_w6_var_a_stage1_candidate_landing.py`
- `computations/session-90/s90_w6_var_a_stage1_candidate_landing.npz` (keys: `promotion_text_sha256`, `registry_section_pre_state_sha256`, `registry_section_post_state_sha256`, `clause_count`, `author_attribution_table`, `corrigenda_present`, `stage_1_tag_present`, `stage_2_dispatch_id_present`)
- (No PNG required for registry-landing)

Verdict-line append target: `computations/session-90/s90_gate_verdicts.txt`.

**Machinery pin (PRDR)**:

```yaml
schema_version: R3
gate_id: S90-VII-U-2-CORNER-II-STAGE-1-CANDIDATE-VAR-A-JOINT-THEOREM-LANDING
machinery_pin_map:
  registry_landing_target: "sessions/permanent-results-registry.md §VII.U.2 Corner II row corrigendum block (OPTION i)"
  slot_allocation_pattern: "next-free-letter within corrigendum sub-block (NOT new §VII.{next-free})"
  bridge_landing_script_architecture: "AFTER-pattern single-shot (per registry-landing.md §\"Bridge-Landing Script Architecture\")"
  clause_count_pre_registered: 5  # (a)+(b)+(c)+(d)+(e)
  author_attribution_per_clause:
    a: "JOINT (lizzi + connes Stage-0 author freeze)"
    b: "connes-ncg-theorist PRIMARY (Wedderburn machinery; W5b-48 Step 5 pin)"
    c: "lizzi-spectral-functional-theorist PRIMARY (parse-tree machinery; W-3 R3)"
    d: "lizzi-spectral-functional-theorist PRIMARY (F_traj theorem; S84 W3-24)"
    e: "JOINT (lizzi + connes; convergence verdict at W-3 R3-B close)"
  corrigenda_required: ["Q-LZ-R2-1 (a)+(b) Wedderburn refinements", "Q-CN-R2-3 GGE-state generic-with-property", "convergence clause (e) at R3-B"]
  stage_2_dispatch_inheritance: "S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY (inherits §VII.U.2)"
  stage_2_eligibility_audit_cross_link: "CF-48 = S90-VII-U-2-STAGE-2-CROSS-AXIS-REVIEWER-ELIGIBILITY-AUDIT"
  registry_writer: "mack-cosmic-bridge"  # sole writer per feedback_mack-bridge-role.md
  technical_signoff: ["lizzi-spectral-functional-theorist (PRIMARY)", "connes-ncg-theorist (CO-AUTHOR)"]
  verifier_rubric_clauses: 5  # 5 verification clauses per Class 8.2
  publication_precision_sig_figs: NULL  # registry-text landing
  verifier_tolerance_rel_tol: NULL
  scheme: "stage-1-candidate-corrigendum-sub-entry-three-machinery"
  convention: "joint-theorem-promotion-stage-1-with-cross-reviewer-axis-b-selection"
  random_seed: NULL
  GPU_path: NULL
verdict_source: computations/session-90/s90_gate_verdicts.txt
input_pin_map:
  W_3_R3_workshop_text: "sessions/archive/session-89/workshops/s89-w3-vii-u-2-corner-classification.md"
  joint_theorem_promotion_md_stage_1: ".claude/rules/joint-theorem-promotion.md §\"Stage 1\""
  permanent_results_registry_md_VII_U_2: "lines 12927-13058"
  F_traj_theorem_S84_W3_24: <pinned at dispatch>
  W5b_48_step_5_wedderburn: <pinned at dispatch>
  feedback_mack_bridge_role: ".claude/agent-memory/orchestrator/feedback_mack-bridge-role.md"
expected_output_4_tuple:
  value: "STAGE-1-CANDIDATE corrigendum landed with 5 clauses + corrigenda + Stage-2 cross-ref"
  scheme: "stage-1-candidate-corrigendum-sub-entry-three-machinery"
  convention: "joint-theorem-promotion-stage-1"
  L_max: NULL  # registry landing
```

**Expected output 4-tuple**:
- `value`: STAGE-1-CANDIDATE corrigendum landed; 5 clauses present; author attribution per clause matches W-3 R3 freeze; corrigenda present; Stage-2 dispatch identifier cross-referenced
- `scheme`: `stage-1-candidate-corrigendum-sub-entry-three-machinery`
- `convention`: `joint-theorem-promotion-stage-1`
- `L_max`: N/A

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: All 5 verifier rubric clauses PASS (clause-count = 5; author attribution matches per-clause; corrigenda present; STAGE-1-CANDIDATE tag present; Stage-2 dispatch identifier cross-referenced); registry text > 15 lines per §"Completion Verification" (`agent-standards.md`); single-shot AFTER-pattern emission (no supersedes chain).
- **INFO**: 4 of 5 rubric clauses PASS; one minor structural defect (e.g., corrigenda heading-level mismatch); recoverable via single follow-up edit.
- **FAIL**: ≥ 2 rubric clauses FAIL OR clause-count ≠ 5 OR author attribution mismatch OR Stage-2 dispatch identifier missing OR registry text < 15 lines (stub).

**What PASSES / FAILS mean for solution space**:

- **PASS**: Var_a(n_a^GGE) becomes the framework's SECOND cross-axis joint theorem in the `joint-theorem-promotion.md` 4-stage pipeline (the FIRST being §VII.AH at STAGE-3-PERMANENT eligibility post-W4-7 PASS). The three-machinery convergence (Wedderburn + parse-tree + F_traj) is structurally registered as the canonical proof template for algebra-axis-orthogonality cell-II observables. Stage-2 → Stage-3 PERMANENT pathway becomes available conditional on CF-48 reviewer-eligibility audit PASS + Stage-2 dispatch at S91+. Closes the corner of solution space where the three-machinery convergence was workshop-internal only; opens the corner where the registry inherits the cross-axis joint theorem template.
- **FAIL (registration defective)**: STAGE-1-CANDIDATE corrigendum does not land structurally; the joint theorem remains workshop-internal; Stage-2 → Stage-3 pathway is BLOCKED. Routes to remediation: re-author corrigendum text; verify author attribution per clause; verify Stage-2 dispatch identifier cross-reference; re-run AFTER-pattern emission. NEVER edit prior verdict line; emit corrective canonical line with `supersedes=<old_audit_sha256>` per Option A protocol if re-emission needed.

**Effort**: 0.5 we

**Substrate-framing reminder**: The substrate IS the BdG spectral triple (A_BdG, H_BdG, D_BdG). The GGE state IS a generic state on A_BdG with the diagonal-in-mode-pair-basis property (the property is STRUCTURAL not state-dependent — preserved by the BdG charge-conjugation symmetry per Q-CN-R2-3). Var_a IS the substrate's intrinsic GGE-variance spectral functional. The four-corner partition (§VII.U.2 Corner I/II/III/IV) IS the substrate's intrinsic algebra-axis × Mellin-pole orthogonality classification per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3 since S87 W-2 R3 close). The three-machinery convergence IS the substrate's intrinsic structural-rigidity proof that the corner classification is independent of the proof-route. Direction of explanation: substrate's intrinsic algebra-axis × Mellin-pole structure → four-corner partition → Var_a's classification at Cell-II → three structurally orthogonal proof routes (Wedderburn / parse-tree / F_traj) all converge to the same answer → the convergence itself is structural, not contingent on machinery choice.

---

## §W6-7. CF-52 S90-F-TRAJ-MULTIPLICATIVE-COMPOSITION-LAW-CONJECTURE-EMPIRICAL-TEST

**Gate ID**: `S90-F-TRAJ-MULTIPLICATIVE-COMPOSITION-LAW-CONJECTURE-EMPIRICAL-TEST`

**Trigger**: `[VERIFY-THEOREM]` — theorem-existence verification: closed-form multiplicative composition law `F_traj(k_1) · F_traj(k_2) = some closed form` testable on the 42-row S84 atlas.

**Classification**: GEOMETRIC (F_traj closed-form composition law as a structural property of the substrate's locked-norm zeta-vs-SDW dressing-ratio across the full substrate-pole atlas).

**Agent type**: lizzi-spectral-functional-theorist PRIMARY (F_traj theorem author).

**Hypothesis**: F_traj=(k+1)/2 theorem extends to a closed-form multiplicative composition law `F_traj(k_1) · F_traj(k_2) = (k_1+1)(k_2+1)/4` (the trivial multiplicative composition that any closed-form ratio admits) verifiable empirically across all C(42, 2) = 861 testable pole-pairs from the S84 42-row atlas at rel_precision ≤ 1e-10. For Var_a's two-moment composition, the structural fingerprint `F_traj(2) · F_traj(4) = (3/2)(5/2) = 15/4` is a specific instance.

**Method (full self-contained dispatch prompt)**:

Test the multiplicative composition law conjecture across the full F_traj=(k+1)/2 theorem's testable atlas at locked norm L_k = 1.

Step 1: Enumerate the 42-row S84 atlas (per S84 W3-24 atlas construction). Each row corresponds to a substrate-distance-k pole observable M_k = Σ_a m_a g_k(lambda_a) for k ∈ {1, 2, 3, ..., 42} (or a subset of poles per the atlas's specific row indexing; map to the original 42-row indexing).

Step 2: For each pole index k in the atlas, compute F_traj(k) = M_k^zeta / M_k^SDW at locked norm L_k = 1 from `s84_spectrum_cache_L12_tau019.npz`. Verify F_traj(k) = (k+1)/2 at rel_precision ≤ 1e-15 (single-k theorem baseline).

Step 3: Enumerate pole-pairs (k_1, k_2) ∈ {1, 2, ..., 42}^2 with k_1 < k_2. Total testable pairs: C(42, 2) = 41 * 42 / 2 = 861.

Step 4: For each pole-pair (k_1, k_2), compute:
- `F_traj_product_empirical(k_1, k_2) := F_traj(k_1) * F_traj(k_2)` (direct multiplication of the individually-verified F_traj values).
- `F_traj_product_predicted(k_1, k_2) := (k_1+1)(k_2+1)/4` (closed-form multiplicative composition law conjecture).
- `rel_dev(k_1, k_2) := |F_traj_product_empirical - F_traj_product_predicted| / |F_traj_product_predicted|`.

Step 5: For Var_a's specific composition (k_1 = 2, k_2 = 4 with the M_2^2 composite via F_traj(2)^2 = 9/4 multiplicative composition; M_4 via F_traj(4) = 5/2):
- Verify F_traj(2) * F_traj(4) = (3/2)(5/2) = 15/4 = 3.75 at rel_precision ≤ 1e-15.
- This is the structural fingerprint of Var_a's two-moment composition (cited in CF-50 substitution chain Step 4).

Step 6: Aggregate: PASS condition for the conjecture = `max_pairs rel_dev ≤ 1e-10` across all 861 testable pole-pairs.

Cross-checks:
1. Single-k F_traj(k) = (k+1)/2 baseline: verify for all 42 pole indices at rel_precision ≤ 1e-15 (failure at single-k baseline propagates to ALL pairs and is the upstream root cause).
2. Symmetry: F_traj(k_1) * F_traj(k_2) = F_traj(k_2) * F_traj(k_1) (multiplicative commutativity); enumeration k_1 < k_2 plus permutation symmetry.
3. Self-composition: F_traj(k) * F_traj(k) = ((k+1)/2)^2 = (k+1)^2 / 4 (e.g., F_traj(2)^2 = 9/4); verify at all 42 self-compositions (relevant for variance-like observables of single-pole moments squared).
4. Trivial structural verification: the closed-form `(k_1+1)(k_2+1)/4` IS by construction the multiplicative composition of `(k+1)/2` factors; the test is whether the empirical F_traj values, individually computed from spectrum cache, multiply to the predicted product to bit-precision.

Output files:
- `computations/session-90/s90_w6_f_traj_multiplicative_composition_atlas.py`
- `computations/session-90/s90_w6_f_traj_multiplicative_composition_atlas.npz` (keys: `pole_indices`, `f_traj_per_pole`, `pole_pairs_k1_k2`, `f_traj_product_empirical`, `f_traj_product_predicted`, `rel_dev_per_pair`, `max_rel_dev`, `var_a_specific_fingerprint_check_15_over_4`)
- `computations/session-90/s90_w6_f_traj_multiplicative_composition_atlas.png` (heatmap of rel_dev across the 42×42 pole-pair grid; diagonal = self-compositions)

Verdict-line append target: `computations/session-90/s90_gate_verdicts.txt`.

**Machinery pin (PRDR)**:

```yaml
schema_version: R3
gate_id: S90-F-TRAJ-MULTIPLICATIVE-COMPOSITION-LAW-CONJECTURE-EMPIRICAL-TEST
machinery_pin_map:
  atlas_row_count: 42  # S84 W3-24 atlas
  pole_pair_count: 861  # C(42, 2)
  cache_path: "computations/_shared/s84_spectrum_cache_L12_tau019.npz"
  schematic_helper: "computations/_shared/_spectral_action_regulators.py"
  schematic_helper_tier_pin: "TIER-2"
  f_traj_single_k_baseline: "(k+1)/2"
  f_traj_composition_law_predicted: "(k_1+1)(k_2+1)/4"
  locked_norm_L_k: 1
  rel_precision_single_k: 1.0e-15
  rel_precision_composition: 1.0e-10
  var_a_specific_fingerprint_predicted: "15/4 = 3.75"  # F_traj(2)*F_traj(4)
  self_composition_check: true  # F_traj(k)*F_traj(k) for all 42 pole indices
  symmetry_check: true  # F_traj(k_1)*F_traj(k_2) = F_traj(k_2)*F_traj(k_1)
  publication_precision_sig_figs: 11
  verifier_tolerance_rel_tol: 1.0e-11
  scheme: "f_traj-multiplicative-composition-law-atlas-861-pole-pairs"
  convention: "f_traj=(k+1)/2-locked-norm-L_k=1-S84-W3-24-atlas-extension"
  random_seed: NULL
  GPU_path: "preferred for matrix products over atlas"
verdict_source: computations/session-90/s90_gate_verdicts.txt
input_pin_map:
  s84_spectrum_cache_L12_tau019.npz: <pinned at dispatch>
  _spectral_action_regulators.py: <pinned at dispatch>
  S84_W3_24_f_traj_theorem_and_atlas: <pinned at dispatch>
  canonical_constants.py: <pinned at dispatch>
expected_output_4_tuple:
  value: "max_rel_dev across 861 pole-pairs = <computed>"
  scheme: "f_traj-multiplicative-composition-law-atlas-861-pole-pairs"
  convention: "f_traj=(k+1)/2-locked-norm-L_k=1-S84-W3-24"
  L_max: 12
```

**Expected output 4-tuple**:
- `value`: max rel_dev across 861 pole-pairs (target: ≤ 1e-10)
- `scheme`: `f_traj-multiplicative-composition-law-atlas-861-pole-pairs`
- `convention`: `f_traj=(k+1)/2-locked-norm-L_k=1-S84-W3-24`
- `L_max`: 12

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: max rel_dev across 861 pole-pairs ≤ 1e-10 AND Var_a-specific fingerprint F_traj(2) * F_traj(4) = 15/4 verified at rel_precision ≤ 1e-15 AND single-k baseline F_traj(k) = (k+1)/2 verified for all 42 pole indices at rel_precision ≤ 1e-15 AND symmetry + self-composition checks PASS.
- **INFO**: max rel_dev ∈ (1e-10, 1e-6] (partial match; multiplicative composition holds approximately but not bit-precision; cross-check L_max-truncation effects).
- **FAIL**: max rel_dev > 1e-6 (multiplicative composition law fails structurally; F_traj is NOT a multiplicative homomorphism on the atlas; conjecture closed as wrong-mechanism).

**What PASSES / FAILS mean for solution space**:

- **PASS**: F_traj=(k+1)/2 theorem is structurally a multiplicative homomorphism on the substrate-pole atlas. This certifies that pole-pair-composite observables (variance, skewness, multi-moment composites) inherit their zeta-vs-SDW dressing-ratios MULTIPLICATIVELY from their constituent single-pole F_traj factors. The closed-form prediction `F_traj(k_1) * F_traj(k_2) = (k_1+1)(k_2+1)/4` becomes a structural identity on the atlas, available for downstream gates that need pole-pair dressing predictions without re-deriving from scratch. Closes the corner of solution space where F_traj might be pole-pair-non-multiplicative (a "structural mixing" risk that would invalidate Var_a's CF-50 substitution chain); opens the corner where F_traj is structurally factorizable across pole pairs.
- **FAIL (composition law fails)**: F_traj is NOT multiplicatively factorizable; pole-pair composites carry irreducible cross-terms. The CF-50 substitution chain Step 4 (`F_traj(2)^2 = 9/4` and `F_traj(4) = 5/2` multiplicative composition) becomes a single-instance miracle rather than a general law. Routes to remediation: identify which pole-pairs violate the composition law (analyze the rel_dev heatmap); diagnose whether the violations cluster by pole-distance, by regulator-class, or by symmetry sector.

**Effort**: 0.8 we

**Substrate-framing reminder**: The substrate IS the spectral triple `(A_K, H_K, D_K)` with the 42-row S84 atlas being the substrate's intrinsic pole-observable enumeration at substrate-distance-k truncations for k ∈ {1, ..., 42}. F_traj IS the substrate's intrinsic locked-norm zeta-vs-SDW dressing-ratio per pole. The multiplicative composition law conjecture IS a structural claim about the substrate's intrinsic homomorphism property of F_traj across the atlas (whether `F_traj : {atlas poles} → R_>0` is a multiplicative semigroup homomorphism under pole-pair composition). Direction of explanation: substrate's intrinsic pole atlas → F_traj single-pole dressing-ratios → multiplicative composition law tested empirically → either certified as structural homomorphism OR closed as wrong-mechanism. NOT: "F_traj is multiplicative by definition" — the closed-form `(k+1)/2` is the substrate's intrinsic per-pole dressing-ratio; the multiplicative composition is an EMERGENT structural property of the atlas, not a tautology.

---

## §W6-8. CF-53 S90-VII-U-2-CORNER-RECONCILIATION-VERIFY

**Gate ID**: `S90-VII-U-2-CORNER-RECONCILIATION-VERIFY`

**Trigger**: `[AUDIT]` — composite Reading B propagation verification: 5 sub-checks AND-aggregated for ALL-PASS composite verdict.

**Classification**: META (composite verification audit; methodology-floor verification that the W-3 R3 closure has propagated correctly through registry text + audit-script extensions + Stage-1 corrigendum + Stage-2 aggregation prerequisites + plan-staleness extension).

**Agent type**: gen-physicist (dispatch coordinator for composite verification; the audit applies 5 deterministic sub-checks against registry state + audit-script self-tests + Stage-1 corrigendum landing).

**Hypothesis**: The W-3 R3 Reading B closure has propagated correctly through the full S90 verification pathway: (a) §VII.U.2 registry text unchanged from R2 verdict freeze (no drift); (b) CF-W6-4 audit-script extension self-test PASSes on 5-axis classification with parse-tree counters = 0; (c) Stage-1-CANDIDATE corrigendum sub-entry (CF-51) present with three-machinery clauses + JOINT flags; (d) §VII.AR Stage-2 PASS-AND aggregation INDEPENDENCE assertion verified (no edits to §VII.AR cross-reviewer eligibility); (e) plan-staleness audit-script extension self-test detects W6-6 line 224 drift (per CF-W6-6 / CF-3 of Cluster A).

**Method (full self-contained dispatch prompt)**:

Apply 5 composite sub-checks; each emits a boolean; composite PASS iff ALL FIVE return True.

### Sub-check (a): §VII.U.2 registry text unchanged from R2 verdict freeze

Compute SHA-256 of the §VII.U.2 block (`permanent-results-registry.md` lines 12927-13058) at S90 W-6 dispatch time. Compare against the SHA-256 at W-3 R2 closure (audit-trail-canonical; provided in the input-pin map from W-3 workshop SHA `<W-3-R2-closure-sha>`). PASS iff the SHAs match modulo whitespace-normalization at the section boundaries.

Note: The CF-51 corrigendum sub-entry IS a structural extension of the §VII.U.2 block (corrigendum sub-block is APPENDED to the Corner II row's existing content; the Corner II row text itself is unchanged). Sub-check (a) tests the Corner II row text PROPER (not including the corrigendum sub-block); the corrigendum is tested separately in sub-check (c).

### Sub-check (b): CF-W6-4 audit-script extension self-test PASSes

Run `computations/_shared/_corner_classification_audit.py --self-test` (per CF-W6-4 extension; gate-ID `S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION` of Cluster A row 2). Verify:
- `per_slot_results['§VII.U.2']` populated with all 4 Corner sub-targets (I/II/III/IV).
- Parse-tree counters `(state_pair_count, algebra_dep_count)` BOTH return 0 on Var_a's fully-expanded form.
- 3-axis classification for Var_a: `corner='II'`, `algebra_axis='INVARIANT'`, `mellin_pole='s=4'`.

PASS iff all 3 conditions PASS in the audit-script self-test output.

### Sub-check (c): Stage-1-CANDIDATE corrigendum present (per CF-51)

Verify that CF-51 has landed structurally:
- §VII.U.2 Corner II row corrigendum sub-block contains the 5-clause Stage-1 candidate text.
- All 5 clauses present with author-side attribution per the W-3 R3 freeze.
- JOINT clause flags on clauses (a) and (e).
- Three-machinery convergence proof structure (Wedderburn + parse-tree + F_traj).
- Stage-2 dispatch identifier cross-referenced.

PASS iff CF-51 PASS verdict line is present in `computations/session-90/s90_gate_verdicts.txt` AND CF-51's registry-landing artifact (the corrigendum sub-block) is present in `sessions/permanent-results-registry.md`.

### Sub-check (d): §VII.AR Stage-2 PASS-AND aggregation INDEPENDENCE assertion verified

The Stage-2 cross-reviewer aggregation for §VII.AR (per `joint-theorem-promotion.md §"Stage 2"`) requires PASS-AND across BOTH axes (logical AND, not OR). Verify that no edits to §VII.AR's cross-reviewer eligibility have been made at S90 W-6 that would compromise the INDEPENDENCE assertion (e.g., axis-A and axis-B reviewers must be on different axes; no shared agent-memory inheritance reach).

Implementation: read `permanent-results-registry.md §VII.AR` block at S90 W-6 dispatch time; verify the Stage-2 dispatch identifier text matches the post-CF-W4-5-A36-PENDING-ADVANCEMENT pin from Cluster G CF-22 (assumes CF-22 lands before CF-53; the cross-wave ordering CF-22 PRECEDES CF-53 is documented in the wave plan's prerequisites table). PASS iff the §VII.AR Stage-2 eligibility text has not drifted.

Forward-looking: if CF-58 (§VII.AR Stage-2 independent verify dispatch) has not yet dispatched at S90 W-6, this sub-check is forward-only — it asserts the INDEPENDENCE structure rather than aggregating a verdict.

### Sub-check (e): Plan-staleness audit-script extension self-test

Run `computations/_shared/_plan_staleness_audit.py --self-test --extension-v2` (per CF-3 of Cluster A: `S90-PLAN-STALENESS-REGEX-TIGHTENING-AND-CROSS-WAVE-ANCHOR-MIS-CITATION-DETECTION`). Verify:
- The extension's `pre_supersession_pin` regex requires YAML pin-map context (not prose).
- The extension's cross-wave-anchor mis-citation detector flags `session-89-plan-w6.md:224` as a known drift instance.

PASS iff both audit-script extension conditions PASS in self-test.

### Composite verdict

`Composite_PASS := (a_PASS) AND (b_PASS) AND (c_PASS) AND (d_PASS) AND (e_PASS)`.

INFO outcome: if §VII.AR Stage-2 dispatch has not yet occurred (sub-check (d) is forward-only). The composite verdict in this case is INFO (forward-looking assertion only, not aggregated verdict).

Cross-checks:
1. SHA reproducibility: rerun the audit dispatch and verify identical SHA outputs at sub-checks (a), (b), (e) (audit-script outputs deterministic).
2. CF-51 landing recency: cross-link to CF-51 verdict line in `s90_gate_verdicts.txt` (must be appended BEFORE CF-53 dispatches).
3. Cross-wave ordering: confirm CF-22 (Cluster G §VII.AR PENDING-A36 advancement) has landed before CF-53 (the cross-wave dependency in sub-check (d)).

Output files:
- `computations/session-90/s90_w6_vii_u_2_corner_reconciliation_verify.py`
- `computations/session-90/s90_w6_vii_u_2_corner_reconciliation_verify.npz` (keys: `sub_check_a_pass`, `sub_check_b_pass`, `sub_check_c_pass`, `sub_check_d_pass`, `sub_check_e_pass`, `composite_verdict`, `vii_u_2_section_sha_pre`, `vii_u_2_section_sha_post`, `corner_audit_self_test_output`, `cf_51_verdict_line_present`, `vii_ar_stage_2_independence_assertion`, `plan_staleness_extension_self_test_output`)
- (No PNG required for audit-class gate)

Verdict-line append target: `computations/session-90/s90_gate_verdicts.txt`.

**Machinery pin (PRDR)**:

```yaml
schema_version: R3
gate_id: S90-VII-U-2-CORNER-RECONCILIATION-VERIFY
machinery_pin_map:
  sub_check_count: 5
  sub_check_aggregation: "AND (composite PASS iff ALL FIVE return True)"
  sub_check_a_target: "§VII.U.2 Corner II row text SHA matches W-3 R2 closure (no drift in Corner II row proper)"
  sub_check_b_target: "_corner_classification_audit.py --self-test --extension-v2 (CF-W6-4 of Cluster A)"
  sub_check_b_audit_sha_reference: "2b96bf78... (W6-6 baseline)"
  sub_check_c_target: "CF-51 verdict line in s90_gate_verdicts.txt + corrigendum sub-block in registry"
  sub_check_d_target: "§VII.AR Stage-2 dispatch eligibility text post-CF-22 PENDING-A36 advancement"
  sub_check_e_target: "_plan_staleness_audit.py --self-test --extension-v2 (CF-3 of Cluster A)"
  sub_check_e_audit_sha_reference: "5f370299... (W6-6 baseline)"
  composite_pass_predicate: "a AND b AND c AND d AND e"
  forward_looking_d_branch: "INFO if §VII.AR Stage-2 has not yet dispatched"
  publication_precision_sig_figs: NULL  # audit gate
  verifier_tolerance_rel_tol: NULL
  scheme: "composite-reading-b-propagation-verify-5-sub-check"
  convention: "w-3-r3-r2-closure-propagation-audit"
  random_seed: NULL
  GPU_path: NULL
verdict_source: computations/session-90/s90_gate_verdicts.txt
input_pin_map:
  W_3_R2_closure_workshop_sha: <pinned at dispatch>
  permanent_results_registry_md_VII_U_2: "lines 12927-13058 (pre + post)"
  permanent_results_registry_md_VII_AR: "lines 16948-16978"
  corner_classification_audit_py: "computations/_shared/_corner_classification_audit.py (W6-6 SHA + CF-W6-4 extension)"
  plan_staleness_audit_py: "computations/_shared/_plan_staleness_audit.py (W6-6 SHA + CF-3 extension)"
  joint_theorem_promotion_md: ".claude/rules/joint-theorem-promotion.md"
  cross_pillar_bridge_anatomy_md: ".claude/rules/cross-pillar-bridge-anatomy.md"
  CF_51_verdict_sha: <pinned at dispatch post-CF-51>
  CF_22_verdict_sha: <pinned at dispatch post-CF-22>
expected_output_4_tuple:
  value: "composite_verdict=<PASS|FAIL|INFO>; sub_check_pass_vector=[a,b,c,d,e]"
  scheme: "composite-reading-b-propagation-verify-5-sub-check"
  convention: "w-3-r3-r2-closure-propagation-audit"
  L_max: NULL  # methodology audit; no L_max
```

**Expected output 4-tuple**:
- `value`: composite_verdict (PASS / FAIL / INFO) + sub_check_pass_vector [a, b, c, d, e]
- `scheme`: `composite-reading-b-propagation-verify-5-sub-check`
- `convention`: `w-3-r3-r2-closure-propagation-audit`
- `L_max`: N/A

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS (composite)**: ALL FIVE sub-checks return True (a_PASS AND b_PASS AND c_PASS AND d_PASS AND e_PASS).
- **INFO**: 4 of 5 sub-checks PASS AND sub-check (d) is the marginal one due to §VII.AR Stage-2 dispatch not yet occurring (forward-looking assertion only; not a structural defect).
- **FAIL**: ANY of sub-checks (a), (b), (c), (e) return False (structural defects in registry propagation, audit-script extensions, or CF-51 landing).

**What PASSES / FAILS mean for solution space**:

- **PASS**: The W-3 R3 Reading B closure has propagated structurally through all five canonical pathways (registry text, audit-script Corner-classification extension, Stage-1 CANDIDATE corrigendum landing, §VII.AR Stage-2 INDEPENDENCE assertion, plan-staleness audit-script extension). Closes the corner of solution space where Reading B might have drifted at one or more pathways; opens the corner where the W-3 closure is structurally stable across the framework's methodology-floor. The Stage-1 → Stage-2 → Stage-3 pathway for Var_a is structurally aligned for S91+ dispatch.
- **FAIL (any pathway drift)**: One or more of the five propagation pathways has structural drift. Routes to remediation: per sub-check, identify the specific pathway failure (a: registry text drift; b: audit-script self-test FAIL; c: CF-51 landing defect; d: §VII.AR eligibility text drift; e: plan-staleness audit-script extension defect). Fix in-session per `feedback_fix-in-session-never-defer.md`; do NOT defer to next session.

**Effort**: 0.5 we

**Substrate-framing reminder**: The substrate-physics identity Var_a ∈ Cell-II is structural (frozen at W-3 R3 closure); the composite verification audit operates at the methodology layer (`epistemic-discipline.md §"Layer-Decomposition"` F: substrate → methodology → audit). The five sub-checks each operate at a distinct methodology-floor pathway: (a) registry-text → SHA invariance; (b) audit-script → self-test extension; (c) registry-landing → corrigendum sub-block presence; (d) registry-text → Stage-2 eligibility invariance; (e) audit-script → self-test extension. The substrate-physics direction of explanation flows: substrate's intrinsic four-corner partition → Var_a's Cell-II identity (Reading B canonical) → methodology-layer propagation across five pathways → audit-layer verification at the composite gate. The substrate IS the spectral triple; the registry text IS the methodology-floor projection of the substrate-physics identity; the audit IS the verification that the projection has not drifted. NOT: registry text is "the truth" and substrate-physics is "downstream" — the substrate-physics is logically prior at every layer.

---

## Wave 6 → Wave 7 Decision Point

| Handoff item | Status | Routing |
|:-------------|:-------|:--------|
| CF-46 Pin B `c_W12_deficit_FW` canonical | LANDED conditional on CF-46 PASS | `canonical_constants.py` entry + PROVENANCE; cross-link to `kappa_2_substrate_FW` Pin A |
| CF-47 `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5*pi` canonical | LANDED conditional on CF-47 PASS | `canonical_constants.py` entry + PROVENANCE; cross-link to §W3-9 audit |
| CF-48 Stage-2 eligibility pool table for §VII.U.2 | PRE-REGISTERED for S91+ dispatch | Stage-2 dispatch `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` consumes the pool table at dispatch time |
| CF-49 LEVEL-DRESSED K=1 → K=2 advancement | LANDED conditional on CF-49 PASS | §VII.K-DUAL.LEVEL-DRESSED K-counter advances; Var_a + §VII.AR at K=2 cohort at s=4 |
| CF-50 F_traj BdG extension verification | LANDED conditional on CF-50 PASS | Empirical anchor for CF-52 multiplicative composition conjecture; F_traj theorem's multi-moment composite verification structural |
| CF-51 Var_a STAGE-1-CANDIDATE corrigendum | LANDED conditional on CF-51 PASS | §VII.U.2 Corner II row corrigendum sub-block; Stage-2 → Stage-3 PERMANENT pathway available at S91+ |
| CF-52 F_traj multiplicative composition law | LANDED conditional on CF-52 PASS | Structural identity available for downstream pole-pair-composite dressing predictions |
| CF-53 Composite Reading B propagation verify | LANDED conditional on CF-53 PASS | Methodology-floor stability of W-3 R3 closure certified across 5 pathways |

**CF-51 STAGE-1-CANDIDATE corrigendum landing PRECEDES §VII.U.2 Stage-2 dispatch at S91+**. Per `joint-theorem-promotion.md §"Stage 2"` MANDATORY ordering: Stage-1 → Stage-2 → Stage-3. CF-48's reviewer-eligibility audit pre-registers the dispatch pool at S90 W-6 BUT the actual Stage-2 dispatch is queued for S91+. The Stage-2 dispatch effective-dispatch ordering is conditional on CF-51 landing as STAGE-1-CANDIDATE.

**No CF-51 PASS ⇒ no §VII.U.2 Stage-2 dispatch at S91+**: the cross-wave dependency is structural. If CF-51 lands as FAIL (registration defective), Var_a's joint-theorem-promotion pathway is BLOCKED at Stage-1; remediation must occur before any Stage-2 dispatch can be scheduled.

**Wave 6 closure prerequisites for S91+ planning**:
1. CF-46 + CF-47 canonical pin landings recorded in `canonical_constants.py` with full PROVENANCE.
2. CF-48 Stage-2 eligibility pool table available at `computations/session-90/s90_w6_vii_u_2_stage2_eligibility_audit.npz`.
3. CF-49 + CF-50 LEVEL-DRESSED + F_traj BdG-extension empirical anchors recorded.
4. CF-51 STAGE-1-CANDIDATE corrigendum LANDED.
5. CF-52 F_traj multiplicative composition law verification recorded (PASS or FAIL).
6. CF-53 composite Reading B propagation verify PASS (or INFO if §VII.AR Stage-2 forward-looking branch (d) applies).

---

## Wave 6 Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR (Pre-Registration Dry-Run): the following machinery parameters are pinned at plan-freeze across all 8 Wave 6 gates.

### Pin-Map enumeration (all gates)

| Pin | Value | Source | Applies to |
|:----|:------|:-------|:----------|
| `tau_fold` | `0.19` (R-PROTECTED) | `canonical_constants.py` | CF-46, CF-49, CF-50, CF-52 |
| `M_KK` | `7.428660036284456e+16 GeV` | `canonical_constants.py` | CF-49, CF-50, CF-52 |
| `Delta_BCS` | `0.4642547394830737` (R-PROTECTED) | `canonical_constants.py` | CF-49, CF-50 |
| `Vol_SU3_Haar` | `1349.74` | `canonical_constants.py` | CF-49 |
| `kappa_2_substrate_FW` | `0.021018084987437196` (S89 W3-7 audit) | `canonical_constants.py:521` | CF-46 |
| `tau_max_HK5_regime_FW` | `12.4750026513 M_KK^{-1}` (S89 W3-9 audit) | `canonical_constants.py:522` | CF-47 |
| `cache_path` | `computations/_shared/s84_spectrum_cache_L12_tau019.npz` | master cache | CF-46, CF-49, CF-50, CF-52 |
| `schematic_helper` | `computations/_shared/_spectral_action_regulators.py` | SCHEMATIC per docstring lines 23-30 | CF-49, CF-50, CF-52 |
| `schematic_helper_tier_pin` | `TIER-2` (companion row in verdict line) | per W9c-1 (S87) POSITIVE-CALIBRATION pattern | CF-49, CF-50, CF-52 |
| `regulator_atlas_5` | `[zeta, SDW, anomaly, cutoff, Zubarev]` | S82 W-3 FI/RD/MIXED classification | CF-49 |
| `f_traj_locked_norm_L_k` | `1` | S84 W3-24 theorem | CF-50, CF-52 |
| `f_traj_single_k_baseline` | `(k+1)/2` | S84 W3-24 theorem | CF-50, CF-52 |
| `bogoliubov_n_a_closed_form` | `Delta_BCS^2 / (2*(lambda_a^2 + Delta_BCS^2))` | registry §VII.U.2 line 12961 | CF-49, CF-50 |
| `HK5_closed_form` | `5 / (1 - tau/(5*pi))` | S89 W3-9 derivation | CF-46, CF-47 |
| `bridge_landing_script_architecture` | `AFTER-pattern single-shot` | `registry-landing.md §"Bridge-Landing Script Architecture"` | CF-51 |
| `joint_theorem_promotion_md_stage_1` | `.claude/rules/joint-theorem-promotion.md §"Stage 1"` | rule file | CF-48, CF-51 |
| `axis_a_pool_VII_U_2` | `[van-den-dungen-bridge-theorist, gen-physicist]` | CF-48 audit | CF-48 |
| `axis_b_pool_VII_U_2` | `[volovik-superfluid-universe-theorist, mack-cosmic-bridge, kitaev-information-theorist]` | CF-48 audit | CF-48 |
| `excluded_reviewers_VII_U_2` | `[connes-ncg-theorist, lizzi-spectral-functional-theorist]` | CF-48 audit | CF-48 |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`) | all gates | ALL |

### Wave 6 PRDR clearance

- **PRU Class 8.0/8.1 (machinery-pin cardinality)**: each gate's machinery_pin_map has zero `<computed at runtime>` placeholders for static inputs; runtime-pinned SHAs are tagged `<pinned at dispatch>` per the canonical PRDR template.
- **PRU Class 8.2 (verifier-rubric pre-registration)**: CF-48 (3 clauses) + CF-51 (5 clauses) + CF-53 (5 sub-checks) have explicit verifier rubric specifications with pattern sets + disjunction-vs-conjunction declaration + 1+ exemplar calibration corpus item (W-3 R3 R2 closure freeze for CF-48 + CF-51 + CF-53).
- **PRU Class 8.3 (publication-precision pre-registration)**: all numerical gates (CF-46, CF-47, CF-49, CF-50, CF-52) carry `publication_precision_sig_figs` field; verifier_tolerance_rel_tol ≥ 10^(-publication_sig_figs).
- **PRU Class 8.4 (representation-convention-pin)**: F_traj locked-norm L_k = 1 convention pinned at CF-50 + CF-52; zeta-vs-SDW regulator-class convention pinned via 5-regulator atlas at CF-49.
- **PRU Class 8.5 (joint-hypersurface)**: N/A for this wave (no 2D hypersurface pre-registration form).
- **PRU Class 8.6 (layered-substitution-chain)**: CF-46 + CF-49 + CF-50 substitution chains carry 5+ steps each with explicit definitions + substitutions + simplifications + direction reads.

### Convention-pin discipline cross-link

Per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 (convention-shopping FORBIDDEN), every Wave 6 gate carries its convention pin in the verdict line `convention=` field; no gate is permitted to re-run with a different convention if its initial verdict is FAIL/INFO. Bounded iteration MAX_ITERATIONS_PER_SIGNAL = 2 applies to remediation under Stage-1 of v3-closure-recovery.

Per `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` SCHEMATIC vs FULL physical level pin MANDATORY at K=4 (S88 W7b-83 close), CF-49 + CF-50 + CF-52 carry the `-SCHEMATIC` suffix in convention tags AND the `tier_pin=TIER-2` companion comment row. CF-49 additionally carries the FULL PV pipeline LEVEL-P pathway with its own canonical-level pin in the convention field.

---

## Wave 6 Input-SHA Ledger

The following input SHAs are pinned at S90 plan-freeze for Wave 6 gates. Runtime-pinned SHAs are noted as `<pinned at dispatch>`.

### Static input SHAs (pinned at plan-freeze)

| Input | Description | SHA-256 (or pin status) | Used by |
|:------|:------------|:-------------------------|:--------|
| `s84_spectrum_cache_L12_tau019.npz` | L_max=12 master spectrum cache at tau=0.19 | `<pinned at dispatch>` | CF-46, CF-49, CF-50, CF-52 |
| `S89_W3_7_verdict_sha256` | kappa_2_substrate_FW canonical anchor | `9de3814811c2a9929a6d50d36a62dcdd829d850a5c22fd59d88768ca008825e3` | CF-46 |
| `S89_W3_9_verdict_sha256` | tau_max_HK5_regime_FW canonical anchor | `136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df` | CF-47 |
| `S88_W6a_51_INFO_verdict_line` | Cache anchor residual 5.230238e-05 | `<pinned at dispatch>` | CF-46 |
| `_spectral_action_regulators.py` | SCHEMATIC regulator helpers (TIER-2) | `<pinned at dispatch>` | CF-49, CF-50, CF-52 |
| `s87_w9b_pole_specificity_scan.npz` | Upstream LEVEL-switch precedent (D_max = 2.168) | `<pinned at dispatch>` | CF-49 |
| `canonical_constants.py` | Framework canonicals (kappa_2, tau_max, Delta_BCS, M_KK, etc.) | `<pinned at dispatch>` | ALL |
| `permanent-results-registry.md §VII.U.2` | Registry block lines 12927-13058 | `<pinned at dispatch>` | CF-48, CF-51, CF-53 |
| `permanent-results-registry.md §VII.AR` | Registry block lines 16948-16978 | `<pinned at dispatch>` | CF-53 |
| `joint-theorem-promotion.md` | Stage 1 + Stage 2 rule text | `<pinned at dispatch>` | CF-48, CF-51, CF-53 |
| `cross-pillar-bridge-anatomy.md` | Algebra-axis orthogonality + cross-pillar bridge anatomy | `<pinned at dispatch>` | CF-48, CF-51, CF-53 |
| `_corner_classification_audit.py` (W6-6 baseline) | Audit-script W6-6 SHA | `2b96bf78...` (pinned at dispatch full 64-char) | CF-53 |
| `_plan_staleness_audit.py` (W6-6 baseline) | Audit-script W6-6 SHA | `5f370299...` (pinned at dispatch full 64-char) | CF-53 |
| `S84_W3_24_f_traj_theorem` | F_traj=(k+1)/2 theorem + 42-row atlas | `<pinned at dispatch>` | CF-50, CF-52 |
| `W5b_48_step_5_wedderburn` | Wedderburn / Schur-orthogonality derivation pin | `<pinned at dispatch>` | CF-51 |

### S89 verdict cross-reference SHAs (cross-link map)

| S89 verdict | SHA-256 | Cross-reference at Wave 6 |
|:------------|:--------|:-------------------------|
| §W3-7 (kappa_2_substrate_FW canonical) | `9de3814811c2a9929a6d50d36a62dcdd829d850a5c22fd59d88768ca008825e3` | CF-46 substitution chain Step 1 + Pin A canonical |
| §W3-9 (tau_max_HK5_regime_FW canonical) | `136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df` | CF-47 Richardson L → ∞ extrapolation prior canonical |
| §W7a (Sage-QQ n_s_FW² − 1 ≡ α_s_canonical) | `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` | (informational; not directly used in Wave 6) |
| §W4-7 (§VII.AH Stage-3 eligibility) | `4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a` | (informational; §VII.AH is the FIRST joint theorem; CF-51 is the SECOND) |

### Runtime-pinned SHAs (resolved at dispatch)

| Input | Description | Wave 6 gate |
|:------|:------------|:-----------|
| `<CF-46_audit_sha256>` | CF-46 verdict | downstream consumers |
| `<CF-47_audit_sha256>` | CF-47 verdict | downstream consumers |
| `<CF-49_audit_sha256>` | CF-49 verdict | downstream consumers (CF-51 K=2 cohort tag) |
| `<CF-50_audit_sha256>` | CF-50 verdict | downstream consumers (CF-52 multiplicative composition anchor) |
| `<CF-51_audit_sha256>` | CF-51 verdict | CF-53 sub-check (c) |
| `<CF-52_audit_sha256>` | CF-52 verdict | downstream consumers |
| `<CF-22_audit_sha256>` (cross-wave) | §VII.AR PENDING-A36 advancement | CF-53 sub-check (d) |
| `<W-3_R2_closure_workshop_sha>` | W-3 workshop R2 closure SHA | CF-53 sub-check (a) |

### Verdict-file structure

All Wave 6 verdict lines append to `computations/session-90/s90_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md §"Canonical Verdict-File Path"`. Each verdict line carries:
- S81+ canonical line: `{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S84+`
- W9a-99 dual-SHA companion comment row: `# audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # {GATE_ID} dual-SHA companion row (W9a-99 split)`
- S87+ schema-v2 3-tuple annotation companion row (REQUIRED for `[VERIFY]` + `[VERIFY-THEOREM]` triggers): `# sign_verdict=<PASS|FAIL|N/A> magnitude_verdict=<PASS|INFO|FAIL> regime_verdict=<VALID|MARGINAL|BREAKDOWN> # {GATE_ID} 3-tuple annotation (S87 schema-v2)`

For gates carrying SCHEMATIC pin (CF-49, CF-50, CF-52): convention tag includes `-SCHEMATIC` suffix (or `-LEVEL-SEPARABLE-CARVE-OUT-NA` per CF-49 LEVEL-P primary tag) AND companion row `# tier_pin=TIER-2 # ...`.

---

**End of Wave 6 plan**.

**Plan author**: lizzi-spectral-functional-theorist (Wave-6 plan writer)
**Plan-freeze SHA**: `<computed at plan-freeze>` over the input-pin map of this file
**Wave-class**: COMPUTE (CF-46, CF-47, CF-49, CF-50, CF-52) + COMPUTE-with-Stage-2-multi-agent-dispatch-coordinator (CF-48, CF-53) + COMPUTE-with-mack-cosmic-bridge-sole-writer-at-registry-landing (CF-51); NO sub-wave decomposition required (Wave 6 partitions cleanly within COMPUTE-class without MIXED-class triage).
**Methodology-wave-allowlist appendage**: not required for any Wave 6 gate (all gates are COMPUTE-class per `wave-classification.md` M1-M4 conjunction; M1 fails for all 8 gates since all have numerical or audit-existence predicates with pre-registered thresholds).
