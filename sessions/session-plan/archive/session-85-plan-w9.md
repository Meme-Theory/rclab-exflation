# Session 85 Plan — Wave W9: feynman-origin reviewer wave

**Wave ID**: W9
**Owner**: feynman-theorist
**Item count**: 5
**Output plan file**: `sessions/session-plan/session-85-plan-w9.md` (this file)
**Verdict file**: `computations/s85_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`)
**Script prefix**: `s85_w9_`
**Dispatch batch**: Batch 2 (per partition manifest)
**Substrate framing**: Path integrals, diagrammatic QFT, Borel summability, and Feynman-rule constructions are effective-field-theory lenses on the spectral action `Tr f(D_K/Lambda)`. The substrate — the Jensen-deformed SU(3) spectral triple with its D_K eigenvalue spectrum — is logically prior. Every "amplitude," "loop integral," and "counterterm" in this wave is a spectral moment or a convergence property of a spectral moment. The direction of explanation flows FROM the substrate TOWARD emergent QFT observables.

## Wave W9 Summary

Five feynman-origin carry-forward items from S84, all structurally about the convergence / classification / registry landing of the 3PI diagrammatic chain and its dependents:

| # | Gate ID | Subject | Classification | Trigger |
|:--|:--------|:--------|:---------------|:--------|
| W9-1 | S85-W9-BOREL-FLOOR-REGISTRY-LANDING | W10-121 Borel-summability per-tau scan cache + PERMANENT registry entry | GEOMETRIC | [VERIFY-THEOREM] |
| W9-2 | S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING | W6-69 F_amp^3PI clause-(b) FI chain promotion to PERMANENT registry | PHONONIC | [VERIFY-THEOREM] |
| W9-3 | S85-W9-FOLDED-TRIANGLE-21CM-SHAPE | Folded-triangle bispectrum SHAPE template at l_max = 1e5 (21-cm) | PHONONIC | [VERIFY] |
| W9-4 | S85-W9-MELLIN-BALANCE-16-OF-16 | Mellin-balance template compliance lift from 0/16 → 16/16 | META | [AUDIT] |
| W9-5 | S85-W9-YUKAWA-MW-TAUCS-REOPEN | Re-open W9b-107/108/109 post mu_BC obligation (i) remediation | PARTICLE | [VERIFY] |

Themes: regulator-invariance (2), permanent-results-reg (1), alpha-s-preregistration (1 via folded-triangle detector-sterile route), cc-5-multiplicative (1), regulator-invariance (1). Two registry-landing items (low effort, high permanence payoff), one novel numerical computation (21-cm template), one audit lift (Mellin compliance), one conditional re-open (predicated on W0's V.2 cube-3 derivation in S85 W0 or earlier-wave resolution of mu_BC obligation (i)).

## Wave W9 Decision Point Prerequisites

Gates execute independently (no intra-wave serial dependency). Cross-wave prerequisites:

- **W9-5 (Yukawa/MW/tau-cross-scale re-open)** is conditional on mu_BC obligation (i) remediation. The S84 feynman synthesis §V.2 identifies three alternative derivation pathways (heat-kernel, zeta-at-interior-s*, rep-theoretic) for the "12" exponent in `mu_BC = M_Z * sqrt(1 + exp(12 * tau_fold) / 3)`. If any S85 wave (likely W0 or W2 connes) lands at least one route returning integer-12, W9-5 proceeds as a three-sub-gate spec. If all routes FAIL, W9-5 downgrades to PRE-REG-INCOMPLETE with documented empirical chain-check fallback. Per `.claude/rules/v3-closure-recovery.md`, a gate left PRE-REG-INCOMPLETE due to upstream FAIL is NOT a FAIL — it is a plan-property state.
- **W9-1, W9-2** depend on S84 artifacts already on disk: `computations/s84_w6_f_amp_3pi_fi_chain.{py,npz,png}` (W6-69) and the W10-121 Borel floor artifact (slug to be resolved at runtime via `computations/_consolidate_intake.py` lookup; cross-reference S84 feynman synthesis §II W10-121 entry for exact SHA).
- **W9-3** depends on canonical_constants: n_s_obs, n_s_framework_predicted, k_21cm_max, f_NL_local_planck2018_upper — any not present must be added to `canonical_constants.py` BEFORE runtime per `.claude/rules/math-scripts.md`.
- **W9-4** depends on `.claude/templates/mellin-balance-pre-declaration.md` (referenced by S84 feynman §V.8) and the 16-gate enumeration from S84 W6-71.

## §W9-1. S85-W9-BOREL-FLOOR-REGISTRY-LANDING

**1. Gate ID**: `S85-W9-BOREL-FLOOR-REGISTRY-LANDING` (no S82/S83/S84 collision — verified against session-84-synthesis-collation verdict tables).

**2. Trigger**: [VERIFY-THEOREM]

**3. Classification**: GEOMETRIC. The Borel floor `min(S_inst) = 2.42e+5` is a property of the Jensen-tau instanton-action spectrum — a geometric property of the D_K-derived effective potential landscape across `tau in [0.05, 0.35]`. Instantons are geometric (substrate saddle points); their action values are spectral-moment-derived.

**4. Agent type**: feynman-theorist (solo).

**5. Hypothesis**: W10-121's Borel-summability result (`min(S_inst) = 2.42e+5` vs Borel threshold 4.34; 4.7 OOM safety margin; Jensen-tau scan in [0.05, 0.35] yields no genuine bound saddle; fold is Morse-index-0 ridge minimum in 35 VP directions) is a PERMANENT theorem of the framework. It justifies tree-level-plus-1-loop computations without requiring non-perturbative instanton corrections inside the physical scan window. A per-tau scan cache should be registered for downstream 1/N-expansion reuse.

**6. Method**:
- Script: `computations/s85_w9_borel_floor_registry.py`
- Inputs: S84 artifact `s84_w10_121_borel_floor.{npz,py}` (slug per W10-121 artifact, resolve via `_consolidate_intake.py --lookup W10-121`); canonical_constants: `tau_fold = 0.190`, Borel-threshold = `4.34` (add to canonical_constants as `Borel_threshold_S_inst = 4.34 # W10-121 lower bound for Borel summability in Jensen-tau sector` if not present).
- GPU/CPU policy: CPU-only. This is a registry-landing audit (re-read npz, verify monotonicity of S_inst across tau grid, emit dual-SHA + T4-theorem-chain). No heavy linear algebra.
- Thread cap: `os.environ.setdefault('OMP_NUM_THREADS', '4')` (audit-class).
- Outputs: `s85_w9_borel_floor_registry.{py,npz,png}`; npz carries per-tau S_inst cache; png plots S_inst(tau) vs Borel threshold.
- SHAs: input SHA-256 of W10-121 npz; output closure SHA via `closure_hash(pins)` (dual-SHA per `gate-verdicts.md` S81+ requirement).

**7. Machinery pin (PRDR §0.11)**:
- `tau_scan_range = [0.05, 0.35]` (matches W10-121 scan)
- `tau_step = 0.005` (61-point grid; re-reads W10-121 npz without recomputation)
- `L_max = 10` (inherited from W10-121 eigenvalue cache)
- `scheme = "W10-121-original"` (no re-regulation; audit-class)
- `convention = "Borel-disk-pointwise"`
- `random_seed = None` (deterministic re-read of static npz)
- `GPU_path = "CPU-only (re-read + monotonicity audit)"`
- `Borel_threshold = 4.34` (pinned constant; add to canonical_constants if absent)
- `S_inst_min_reference = 2.42e5` (W10-121 verdict value, pinned for re-verification)
- `registry_file = "sessions/framework/permanent-results-registry.md"`
- `weave_command = "/weave --update"` (post-landing confirmation)

**8. Expected 4-tuple**: `(value=1.0 [fraction of tau-grid points with S_inst > Borel_threshold], scheme=W10-121-original, convention=Borel-disk-pointwise, L_max=10)`. Registry-landing dual-SHA pair emitted as auxiliary pins.

**9. PASS/FAIL/INFO thresholds**:
- **PASS** iff (a) fraction = 1.0 (all 61 tau-grid points satisfy S_inst > 4.34); AND (b) registry entry landed with T4-theorem-chain and dual-SHA; AND (c) `/weave --update` confirms the entry in `tools/knowledge.db`. Tolerance: THEOREM (boolean).
- **FAIL** iff any tau-grid point has S_inst <= 4.34 (would contradict W10-121 verdict; indicates data corruption, not a new physics result).
- **INFO** iff registry file write succeeds but `/weave --update` fails for an unrelated reason (e.g., knowledge-db lock); gate auto-retries.

**10. Substitution chain** [VERIFY-THEOREM]:

```
Definition 1: S_inst(tau) = classical action of the dominant instanton at Jensen-deformation parameter tau.
Definition 2: Borel_threshold = 4.34 (pinned; W10-121 says Borel-summable iff S_inst > 4.34).
Definition 3: PASS := (for all tau in scan_grid) S_inst(tau) > Borel_threshold.

Step 1 (substitute): W10-121 reports min_{tau in [0.05, 0.35]} S_inst(tau) = 2.42e+5.
Step 2 (simplify): min(S_inst) = 2.42e+5 > 4.34 = Borel_threshold (both positive reals).
  2.42e+5 / 4.34 = 5.58e+4 ≈ 4.7 OOM above threshold (verify via Python: log10(2.42e5/4.34) = 4.746).
Step 3 (direction): Since min(S_inst) > Borel_threshold, EVERY tau in the grid satisfies S_inst > Borel_threshold (minimum is the tightest).
Step 4 (conclusion): PASS iff re-audit re-confirms min = 2.42e+5 and no tau drops below threshold.

Therefore: monotonicity + minimum-value re-verification is SUFFICIENT to PASS. Direction: PASS is achieved by re-confirming the W10-121 minimum; no new physics needed — this is a registry landing, not a new measurement.
```

**11. Implications**:
- **If PASS**: Borel-summability becomes a PERMANENT wall (GEOMETRIC). Perturbation-theory claims across the framework (tree + 1-loop F_amp^3PI, Mukhanov-Sasaki z_R, f_conv Z_R two-loop investigation) are epistemically justified without instanton-contamination concerns inside the physical scan window. Downstream 1/N expansions reference the per-tau cache rather than recomputing.
- **If FAIL**: Would indicate data corruption in W10-121 npz OR a plan-authoring error in the scan-range pin; triggers v3-closure recovery Stage-1 sig_1 remediation.
- **Constraint-map entry**: adds a wall labeled `W_Borel_tau_[0.05,0.35]_L10` to the solution space — any future mechanism that requires a genuine instanton inside this window is closed.

**12. Effort**: 0.5 agent-session (LOW). Registry-landing + dual-SHA emission + `/weave --update`. No new numerical computation.

**13. Substrate framing**: Instanton action `S_inst` is a spectral-action saddle-point integral over Euclidean-time paths on the Jensen-SU(3) substrate. A "Borel-summable perturbation series" is the statement that the spectral action's tau-expansion has convergent Borel-sum integral representation. The substrate's spectral spectrum is what sets S_inst; the QFT language is the derived-observable lens. No "particles" exist in this picture — only relay-pattern resonances whose propagator poles are spectral moments.

---

## §W9-2. S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING

**1. Gate ID**: `S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING` (new, no collision).

**2. Trigger**: [VERIFY-THEOREM]

**3. Classification**: PHONONIC. F_amp^3PI is the 3PI (three-particle-irreducible) amplitude correction to the substrate's relay-pattern self-energy. The FI (factorization invariance / regulator-independence) property is a phononic statement — excitations of the substrate retain their amplitude structure under choice of regulator.

**4. Agent type**: feynman-theorist (solo).

**5. Hypothesis**: W6-69 (`clause-(b) product_ratio span = 1.0 to machine epsilon across {zeta, Zubarev, SDW, dim-reg, lattice-BR}; T4 residual 6.21e-4; NLO_field = 8.85e-6, 2,445x below eps_H = 0.02163`) is a PERMANENT theorem: the Mukhanov-Sasaki `z_R^2` normalization and the 3PI self-energy `z_R^{-2}` embedded factor are inverse counterparts in A_s reconstruction — their product is machine-epsilon 1 across 5 regulators. This is the F_amp^3PI FI chain; landing it as permanent registry entry with dual-SHA + T4 derivation chain is the W9-2 task.

**6. Method**:
- Script: `computations/s85_w9_f_amp_3pi_fi_registry.py`
- Inputs: `computations/s84_w6_f_amp_3pi_fi_chain.{py,npz}` (W6-69); `computations/s84_w6_mellin_balance_template_audit.{py,csv,npz}` (W6-70 field-convergence cross-reference); canonical_constants: `eps_H = 0.02163` (add if absent as `eps_H_W6 = 0.02163 # slow-roll bound, W6 chain`).
- GPU/CPU policy: CPU-only; re-read + audit. Re-verify product_ratio span across 5 regulators matches claimed `1.0 to machine epsilon`.
- Outputs: `s85_w9_f_amp_3pi_fi_registry.{py,npz,png}`; registry entry append-only to `sessions/framework/permanent-results-registry.md` under §VII-B or §VII-M (agent verifies the correct section at runtime).
- SHAs: input SHA-256 of W6-69 npz + W6-70 npz + canonical_constants.py; output closure SHA.

**7. Machinery pin (PRDR)**:
- `regulators = ["zeta", "Zubarev", "SDW", "dim-reg", "lattice-BR"]` (5-atlas)
- `clause_tested = "(b)"` (W6-69 specific; clause-(a) is separate theorem)
- `product_ratio_tolerance = 2.22e-16` (machine epsilon float64)
- `T4_residual_threshold = 1e-3` (W6-69 reports 6.21e-4; pinned re-verification)
- `NLO_field_reference = 8.85e-6`
- `eps_H = 0.02163`
- `NLO_margin_required = 1000x` (W6-69 reports 2,445x; pinned lower bound)
- `L_max = 10`
- `scheme = "W6-69-atlas"` (no re-regulation)
- `convention = "Mukhanov-Sasaki z_R^2 normalization + 3PI self-energy z_R^{-2} factor"`
- `random_seed = None` (deterministic re-read)
- `GPU_path = "CPU-only"`

**8. Expected 4-tuple**: `(value=<max_deviation_of_product_ratio_from_1>, scheme=W6-69-atlas, convention=MS-z_R-pair, L_max=10)`. Registry entry dual-SHA emitted.

**9. PASS/FAIL/INFO thresholds**:
- **PASS** iff (a) max_deviation <= 2.22e-16 (machine epsilon); AND (b) T4_residual <= 1e-3; AND (c) NLO_margin >= 1000x; AND (d) registry entry landed with dual-SHA + T4-chain; AND (e) `/weave --update` confirms. Tolerance: THEOREM (boolean AND of 5 conditions).
- **FAIL** iff any deviation > machine epsilon OR T4 residual exceeds threshold OR NLO margin falls below 1000x. Would indicate W6-69 data corruption OR regulator-atlas degradation.
- **INFO** iff registry landing succeeds but a 6th regulator (e.g., Pauli-Villars) subsequently added and product_ratio_span >= machine epsilon on that regulator only; note as extended-atlas contingency.

**10. Substitution chain** [VERIFY-THEOREM]:

```
Definition 1: product_ratio(R) = [z_R^{-2}]_{F_amp^3PI} * [z_R^{+2}]_{Mukhanov-Sasaki}   [for regulator R]
Definition 2: W6-69 claim: product_ratio(R) = 1 exactly for each R in 5-atlas, to machine eps.

Step 1 (substitute): For each R in {zeta, Zubarev, SDW, dim-reg, lattice-BR}, compute product_ratio(R).
Step 2 (simplify): Since the z_R^{-2} in F_amp^3PI and the z_R^{+2} in Mukhanov-Sasaki are INVERSE counterparts of the SAME geometric normalization factor (the substrate's post-transit acoustic-metric re-scaling), they cancel ALGEBRAICALLY, not numerically. Ratio should be 1 to machine eps for any R.
Step 3 (direction): max_R |product_ratio(R) - 1| <= 2.22e-16 = machine_eps.
Step 4 (conclusion): PASS iff re-verification confirms algebraic cancellation across all 5 regulators.

Therefore: this is a claim that the 3PI self-energy-normalization IDENTITY is exact at the substrate level, with the regulators acting only as computational lenses. Direction: PASS is ensured IF the underlying z_R pairing is literally the same substrate quantity; the regulator-atlas width tests robustness of the identity under computational conventions, not its truth.
```

**11. Implications**:
- **If PASS**: F_amp^3PI FI promoted to PERMANENT theorem T4. A_s amplitude is regulator-independent at the 3PI level. This closes the "scheme-dependence" concern for A_s (CF W6 D.1 two-loop Z_R investigation is NOT about A_s; it's about f_conv, a different Mellin slot). Strengthens the ZFP (zero-free-parameter) claim for A_s across the transit.
- **If FAIL**: Would force re-opening W6-69 and re-running the full 5-regulator atlas with a fresh eigenvalue cache. Very unlikely given W6-69 clean PASS verdict.
- **Constraint-map entry**: adds a theorem-wall `T_F_amp_3PI_FI` to the permanent-results-registry.

**12. Effort**: 0.5 agent-session (LOW).

**13. Substrate framing**: The 3PI diagram in QFT is a lens on the substrate's three-relay-pattern correlation. The "self-energy" is a spectral-moment integral; "FI" means that the substrate's spectral moment is a regulator-independent invariant. The Mukhanov-Sasaki `z_R` is NOT an inflaton-trajectory quantity (the framework rejects inflation); it is the substrate's acoustic-metric normalization factor at the transit-horizon-scale. Product_ratio = 1 is an identity about the substrate, not a property of an inflaton field.

---

## §W9-3. S85-W9-FOLDED-TRIANGLE-21CM-SHAPE

**1. Gate ID**: `S85-W9-FOLDED-TRIANGLE-21CM-SHAPE` (new).

**2. Trigger**: [VERIFY]

**3. Classification**: PHONONIC. The folded-triangle bispectrum at 21-cm `l_max = 1e5` is a non-Gaussianity signature of GGE-relic acoustic interference. It is a phononic amplitude observable — the three-mode correlator of substrate relay-patterns in the post-transit regime.

**4. Agent type**: feynman-theorist (solo).

**5. Hypothesis**: After the S84 synthesis established that amplitude-running (`alpha_s`, `beta_s`) is the primary alpha-s-preregistration detector axis, the folded-triangle bispectrum SHAPE template at 21-cm l_max = 1e5 provides a STRUCTURAL ALTERNATIVE: if the GGE relic is the post-transit acoustic excitation pattern, its three-mode correlator has a specific folded-triangle shape (k1 + k2 ≈ k3, or permutations) distinct from both local-NG (squeezed) and equilateral templates. Pre-register the SHAPE and the amplitude-scale for 21-cm detection.

**6. Method**:
- Script: `computations/s85_w9_folded_triangle_21cm_shape.py`
- Inputs: canonical_constants: `k_21cm_max = 1e5` (add to canonical as `l_max_21cm_forecast = 1e5 # 21-cm bispectrum high-multipole forecast horizon` if absent); `n_s_framework = 0.9561` (S84 predicted); `beta_s = -0.1331` (S85-BETA-S-CMB-S4-PREREG canonical); `tau_fold = 0.190`; Jensen-tau eigenvalue cache for k-mode enumeration.
- GPU/CPU policy: GPU preferred (GGE-relic three-mode correlator integral over momentum triangles is `O(l_max^3)` scan — for l_max = 1e5 this is 10^15 triangles; AGGRESSIVE PRUNING or analytic template substitution required). If full scan intractable, use analytic folded-triangle template `B(k1, k2, k3) = f_NL * [P(k1) P(k2) + cyclic]` with GGE-relic cross-correlator inserted; compute ONLY the shape response function, not the full bispectrum sweep. Use `torch.linalg` for GPU eigensystem ops; ROCm GPU path per `.claude/rules/math-scripts.md`.
- Outputs: `s85_w9_folded_triangle_21cm_shape.{py,npz,png}`; npz carries shape template + f_NL_folded projection; png plots shape response vs folded/squeezed/equilateral reference shapes.
- SHAs: input SHA-256 of canonical_constants.py + eigenvalue cache; output closure SHA.

**7. Machinery pin (PRDR)**:
- `l_max = 1e5`
- `shape_template = "folded-triangle"` (k1 + k2 = k3 ridge, with 2% tolerance window in k-space)
- `triangle_pruning = "ridge-only"` (restrict integration to folded-ridge neighborhood to make O(l_max^3) scan tractable)
- `f_NL_prior_range = [-1e3, +1e3]` (Planck 2018 local-NG upper bound f_NL^local < 5, but folded-template has weaker observational bound — prior widened)
- `GGE_relic_cross_correlator = "I-1-channel"` (per S84 framework registry)
- `L_max_eigenvalue = 10`
- `scheme = "analytic-template-folded"` (no full triangle scan; analytic response function)
- `convention = "delta-function-ridge + 2% k-window"`
- `random_seed = 42` (for ridge-sampling Monte Carlo, if used)
- `GPU_path = "torch.linalg on ROCm (if eigenvalue cache re-used)"`
- `n_s_framework = 0.9561`
- `beta_s = -0.1331`

**8. Expected 4-tuple**: `(value=f_NL_folded_predicted, scheme=analytic-template-folded, convention=ridge-delta-function, L_max=1e5)`. Auxiliary outputs: shape_response_function, SNR_projection at 21-cm noise floor.

**9. PASS/FAIL/INFO thresholds**:
- **PASS** iff (a) f_NL_folded_predicted is FINITE (dimensionless real number emitted by the script); AND (b) shape_response_function integrates to a well-defined real value over the folded-ridge (convergent, no log-divergences); AND (c) SNR projection at nominal 21-cm experiment noise is computed and emitted (whether or not detectable — gate is pre-registration, not detection). Tolerance: THEOREM (well-definedness).
- **FAIL** iff the shape response diverges (would indicate wrong template scaling or a plan-authoring error) OR f_NL_folded is non-finite.
- **INFO** iff f_NL_folded < 0.1 (unmeasurable at any planned 21-cm experiment — template still registered but flagged EVOI = 0 under current detector roadmap).

**10. Substitution chain** [VERIFY]:

```
Definition 1: folded-triangle bispectrum amplitude f_NL_folded = B_folded(k1, k2, k3 = k1 + k2) / [2 * P(k1) * P(k2)]  (definition per Komatsu 2010).
Definition 2: B_folded arises from non-Bunch-Davies initial states — ON the substrate, this corresponds to the GGE-relic post-transit distribution (non-vacuum initial condition for acoustic modes).

Step 1 (substitute): For GGE relic, the mode-function initial condition is a Bogoliubov-mixed state with alpha = cosh(chi), beta = sinh(chi) per Parker pair-production in the substrate transit.
Step 2 (substitute): f_NL_folded ~ |beta|^2 / |alpha|^2 * (k1 k2 k3)-dependent shape factor.
Step 3 (simplify): S84 framework gives |beta|^2 = N_pairs = 59.8 per k-mode (Parker result, S42 canonical). |alpha|^2 = 1 + |beta|^2 ≈ 60.8.
  ratio = 59.8 / 60.8 ≈ 0.984 → f_NL_folded is O(1) if shape factor is O(1), not suppressed.
Step 4 (direction): f_NL_folded predicted to be ORDER UNITY (not vanishingly small, not giant). Exact value depends on the shape-factor geometric integral, which is what the script computes.

Therefore: the script's job is to compute the exact shape-factor, combine with |beta|^2/|alpha|^2, and emit f_NL_folded. PASS means the computation converges to a finite real — direction: we expect O(1), not zero, not divergent.
```

Verify via Python before running: `import math; print(59.8/60.8)` → 0.9836. Script should confirm this ratio and produce f_NL_folded scaled by the geometric shape-factor.

**11. Implications**:
- **If PASS with measurable f_NL_folded**: Provides a STRUCTURAL ALTERNATIVE to the amplitude-running detector axis. Complementary to the 33.98-sigma alpha_s CMB-S4 channel; independent of alpha_s measurement systematics.
- **If PASS with f_NL_folded < 0.1**: Template still registered; EVOI for 21-cm deployment low under current roadmap, but framework's non-Gaussianity signature is quantitatively pinned for future >= l_max = 1e5 experiments.
- **If FAIL**: Triangle-shape computation pathology; triggers re-audit of the Bogoliubov-relic mode-function normalization.
- **Constraint-map entry**: adds a detection channel `C_21cm_folded` with pre-registered SHAPE and amplitude.

**12. Effort**: 1.5 agent-session (MEDIUM). New numerical computation; analytic template known but GGE-relic shape-factor integral must be evaluated on Jensen-eigenvalue-pruned mode grid.

**13. Substrate framing**: 21-cm bispectrum is NOT "inflation non-Gaussianity from a multi-field inflaton." It is the three-mode correlator of the GGE-relic acoustic-excitation pattern — the post-transit substrate's phononic interference signature at recombination-era hydrogen hyperfine transitions. The folded shape arises because the GGE relic is a squeezed acoustic state with specific mode-mixing (Bogoliubov beta_k ≠ 0). The "inflaton" language is the QFT-lens; the physics is phonon-phonon correlators on a post-transit substrate.

---

## §W9-4. S85-W9-MELLIN-BALANCE-16-OF-16

**1. Gate ID**: `S85-W9-MELLIN-BALANCE-16-OF-16` (new).

**2. Trigger**: [AUDIT]

**3. Classification**: META. Template-compliance audit — a methodological gate, not a new physics claim.

**4. Agent type**: feynman-theorist (as origin) but delegation-eligible to gen-physicist if concurrency-cap requires. For this plan, owner = feynman-theorist.

**5. Hypothesis**: The 16 S84 cluster-test gate blocks enumerated in W6-71 can be lifted from the current `compliance_fraction = 0.0` to `1.0` by systematic application of the Mellin-balance pre-declaration template (`.claude/templates/mellin-balance-pre-declaration.md`). The lift requires adding a "saturated-balanced / floor" subclass for the four zero-cluster gates (VII-K-PROP, CC5-ADJACENT, LEDGER-LINEARITY, M0-FCONV-BACK) whose Mellin-clusters are singletons by construction.

**6. Method**:
- Script: `computations/s85_w9_mellin_balance_16_of_16.py`
- Inputs: `.claude/templates/mellin-balance-pre-declaration.md`; `computations/s84_w6_mellin_balance_template_audit.{py,csv}` (the W6-71 audit that reported 0/16); 16-gate enumeration from S84 W6-71 CSV.
- GPU/CPU policy: CPU-only. Audit-class — per-gate template-snippet derivation and re-audit via W6-71 script.
- Outputs: `s85_w9_mellin_balance_16_of_16.{py,csv,png}`; 16-row CSV with per-gate template-snippet + compliance-verdict; png plots compliance_fraction pre/post.
- SHAs: input SHA-256 of template.md + W6-71 audit CSV; output closure SHA.

**7. Machinery pin (PRDR)**:
- `gate_count = 16`
- `floor_subclass_gates = ["VII-K-PROP", "CC5-ADJACENT", "LEDGER-LINEARITY", "M0-FCONV-BACK"]` (zero-cluster singletons)
- `cluster_subclass_gates = 12` (remaining)
- `template_file = ".claude/templates/mellin-balance-pre-declaration.md"`
- `template_version = "current HEAD"` (pinned via git HEAD SHA at runtime)
- `compliance_target = 1.0`
- `compliance_reference = 0.0` (W6-71)
- `audit_rerun_script = "computations/s84_w6_mellin_balance_template_audit.py"`
- `L_max = 10` (if re-audit requires eigenvalue reference)
- `scheme = "Mellin-balance-pre-declaration-v1"`
- `convention = "saturated-balanced-floor + cluster-product subclass split"`
- `random_seed = None` (deterministic)
- `GPU_path = "CPU-only"`

**8. Expected 4-tuple**: `(value=compliance_fraction_post, scheme=Mellin-balance-v1, convention=floor+cluster-split, L_max=10)`.

**9. PASS/FAIL/INFO thresholds**:
- **PASS** iff compliance_fraction_post == 1.0 (all 16 gates have template snippets landed and re-audit confirms). Tolerance: THEOREM (exact fraction, 16/16).
- **FAIL** iff compliance_fraction_post < 1.0 — at least one gate rejected the template snippet. Identifies WHICH gate(s) rejected and WHY; logs to CSV.
- **INFO** iff compliance_fraction_post ∈ [12/16, 15/16] — substantial lift but incomplete; partial-landing verdict with per-gate breakdown.

**10. Substitution chain** [AUDIT]:

```
Definition 1: compliance_fraction(post) = count(gates with template snippet accepted) / 16.
Definition 2: Accepted := the gate's §Mellin-balance subsection contains either (a) a non-empty cluster-product pair list OR (b) a "saturated-balanced floor" declaration for zero-cluster gates.
Definition 3: W6-71 reported compliance_fraction(pre) = 0/16.

Step 1 (substitute): For each of 16 gates, generate the template snippet per .claude/templates/mellin-balance-pre-declaration.md. Four fall into the floor subclass (zero-cluster), twelve into the cluster-product subclass.
Step 2 (substitute): Re-run s84_w6_mellin_balance_template_audit.py with the lifted gate blocks.
Step 3 (simplify): If every gate's snippet satisfies (a) or (b) per definition 2, count = 16, compliance_fraction = 16/16 = 1.0.
Step 4 (direction): PASS direction is compliance_fraction(post) - compliance_fraction(pre) = 1.0 - 0.0 = +1.0. The 0.0 → 1.0 lift is the target.

Therefore: PASS requires ALL 16 gates to present a non-empty §Mellin-balance subsection, with the floor subclass properly distinguished for the four zero-cluster gates. Direction: compliance_fraction is monotone non-decreasing under template application (adding snippets can only increase count), so failure means at least one gate's template snippet fails re-audit (identifies a template-definition bug, not a physics result).
```

**11. Implications**:
- **If PASS**: S84 cluster-test gate family fully compliant with the Mellin-balance template. Closes CF W6-71 methodological carry-forward. Template self-sufficient per `.claude/rules/epistemic-discipline.md` PRU first-invocation discipline.
- **If PARTIAL**: Identifies template-definition bugs (e.g., floor subclass needs further refinement; cluster-product counting rule ambiguous). Triggers template edit + re-dispatch.
- **If FAIL**: Unlikely; would indicate template is fundamentally incompatible with the gate family. Forces structural template redesign.

**12. Effort**: 1 agent-session (MEDIUM). Tedious 16-gate per-snippet derivation.

**13. Substrate framing**: "Mellin balance" is a bookkeeping convention for how 3PI diagrams partition into cluster-products when the spectral action is expanded in Mellin-space. It is META-methodology about how QFT-lens expansions relate to the underlying spectral-action integrals. The substrate's spectral moments are frozen; the Mellin-expansion is a choice of basis. Template compliance is a methodology-layer property, orthogonal to physics.

---

## §W9-5. S85-W9-YUKAWA-MW-TAUCS-REOPEN

**1. Gate ID**: `S85-W9-YUKAWA-MW-TAUCS-REOPEN` (new; carries three sub-gates W9-5a, W9-5b, W9-5c internally).

**2. Trigger**: [VERIFY]

**3. Classification**: PARTICLE. Yukawa closure, MW-consistency, and tau-cross-scale are quantum-number / Standard-Model-observable checks on the mu_BC closure.

**4. Agent type**: feynman-theorist (orchestrator); three parallel sub-agents (each a feynman-theorist spawn, or delegated to gen-physicist if concurrency-cap requires).

**5. Hypothesis**: The S84 W9b-107/108/109 PRE-REG-INCOMPLETE gates (Yukawa-closure, MW-consistency, tau-cross-scale) were blocked by the W9b-105 spectral-dimension-probe FAIL (`d_spec = 4.895` outside expected window `[2.5, 3.5]`). If mu_BC obligation (i) remediation (S84 feynman §V.2: three alternative derivation routes for "12" exponent) lands via an upstream S85 wave (likely W0 or W2), then W9-5 re-opens the three gates with the new derivation pathway pinned as the upstream dependency. If ALL V.2 routes FAIL (returning non-integer-12), W9-5 downgrades to empirical chain-check against accommodated `mu_BC = 188.185 GeV` with explicit SCHEME-DEP flag.

**6. Method**:
- Orchestrator script: `computations/s85_w9_yukawa_mw_taucs_reopen.py`
- Three sub-scripts:
  - `s85_w9_5a_yukawa_closure.py` — top-quark Yukawa `y_t` prediction vs PDG `m_t_pole = 172.69 GeV` and `v_ew = 246.0 GeV`
  - `s85_w9_5b_mw_consistency.py` — MW mass consistency via `mu_BC` and CKM-sector constraint
  - `s85_w9_5c_tau_cross_scale.py` — tau-cross-scale flow of mu_BC from M_Z to M_Planck (or UV cutoff per framework)
- Inputs: canonical_constants: `v_ew = 246.0`, `m_t_pole = 172.69`, `alpha_s_MZ_obs = 0.1180`, `m_H_obs = 125.1`; S85-MU-BC-OBLIGATION-I-DERIV verdict (from upstream wave); W9b-107/108/109 PRE-REG-INCOMPLETE entries from S84 verdict file.
- GPU/CPU policy: CPU for Yukawa + MW (analytic RG flow); GPU if tau-cross-scale requires a large eigenvalue re-scan. Use `torch.linalg` for any matrix eig > 100x100.
- Outputs: `s85_w9_yukawa_mw_taucs_reopen.{py,npz,png}` + three sub-npz files; png plots y_t and m_W predictions vs observed.
- SHAs: input SHA-256 of canonical_constants + upstream V.2 verdict; output closure SHAs (three sub-gates, three sub-SHAs; orchestrator emits aggregate SHA).

**7. Machinery pin (PRDR)**:
- `sub_gate_count = 3` (Yukawa, MW, tau-cross-scale)
- `upstream_dependency = "S85-MU-BC-OBLIGATION-I-DERIV"` (from S84 feynman §V.2; may land in W0 or W2)
- `route_pinned_if_V2_PASS = "first-route-that-returns-12"` (heat-kernel, zeta-at-interior, or rep-theoretic — whichever lands first)
- `fallback_mode_if_V2_FAIL = "empirical-chain-check-accommodated-mu_BC"` (with SCHEME-DEP flag per W4-48)
- `mu_BC_accommodated = 188.185`  (GeV; current best-fit value; add to canonical_constants if absent as `mu_BC_GeV = 188.185 # S84 W9b-105 accommodated value, SCHEME-DEP W4-48`)
- `y_t_prior = m_t_pole * sqrt(2) / v_ew`  (tree-level, per Standard Model)
- `y_t_tolerance = 1e-2`  (1% Yukawa-closure tolerance)
- `m_W_prior = 80.379`  (GeV, PDG 2024; add to canonical as `m_W_obs = 80.379`)
- `m_W_tolerance = 5e-4`  (0.05%, PDG precision)
- `tau_cross_scale_range = "[M_Z, M_Planck]"`
- `L_max = 10`
- `scheme = "V.2-upstream-conditional"`
- `convention = "RG flow in MS-bar; one-loop for Yukawa, two-loop for MW"`
- `random_seed = None`
- `GPU_path = "torch.linalg (ROCm) for any eigen > 100x100"`

**8. Expected 4-tuple**: `(value=<3-tuple (y_t_pred, m_W_pred, mu_BC_tau_cross)>, scheme=V.2-conditional, convention=MS-bar, L_max=10)`.

**9. PASS/FAIL/INFO thresholds**:
- **PASS (W9-5a)** iff `|y_t_pred - y_t_prior| / y_t_prior <= 1e-2`. RATIO tolerance.
- **PASS (W9-5b)** iff `|m_W_pred - m_W_obs| / m_W_obs <= 5e-4`. RATIO tolerance.
- **PASS (W9-5c)** iff `mu_BC(M_Z) → mu_BC(M_Planck)` flow is convergent (no Landau pole; no tachyonic mass inversion) across the RG range. THEOREM (boolean).
- **Aggregate PASS** iff all three sub-gates PASS.
- **Partial PASS** if 1 or 2 sub-gates PASS (each sub-gate reports independently).
- **FAIL** iff all three sub-gates FAIL.
- **PRE-REG-INCOMPLETE** iff upstream V.2 returns FAIL for all three alternative-derivation routes AND the fallback empirical-chain-check is not yet specified (would require new pre-registration).

**10. Substitution chain** [VERIFY]:

```
Definition 1: y_t (top Yukawa) = m_t_pole * sqrt(2) / v_ew        [Standard Model tree-level; PDG convention]
Definition 2: m_W (W-boson mass) = g * v_ew / 2                   [SM tree; g from electroweak mixing]
Definition 3: mu_BC(scale) = running mass-scale derived from framework eigenvalue structure + "12" exponent in the cube-3 derivation route.

Step 1 (substitute Yukawa): y_t_prior = 172.69 * sqrt(2) / 246.0 = 172.69 * 1.41421356 / 246.0
Step 2 (Python-verify): 172.69 * 1.41421356 = 244.238... ; /246.0 = 0.99284... — so y_t_prior ≈ 0.9928.
Step 3 (direction): Framework prediction y_t_pred must land within 1e-2 of 0.9928, i.e., y_t_pred ∈ [0.9829, 1.0027]. The framework's y_t_pred comes from the mu_BC-adjusted running, conditional on V.2 route's "12" exponent.

Step 1 (substitute MW): m_W_prior = 80.379 GeV (PDG central). m_W_pred comes from framework's CKM-sector + mu_BC closure.
Step 2 (simplify): tolerance = 5e-4 → m_W_pred ∈ [80.379 * (1 - 5e-4), 80.379 * (1 + 5e-4)] = [80.339, 80.419] GeV.
Step 3 (direction): PASS direction is |m_W_pred - 80.379| <= 0.040 GeV.

Step 1 (substitute tau-cross-scale): mu_BC(M_Z) = 188.185 GeV (accommodated). RG flow to M_Planck ≈ 1.22e19 GeV.
Step 2 (simplify): No Landau pole means beta(mu_BC) has finite integral from M_Z to M_Planck. Tachyonic inversion means mu_BC crosses zero during the flow — forbidden.
Step 3 (direction): PASS direction is monotone mu_BC(mu) remains positive and finite across [M_Z, M_Planck]. Any sign-flip or blow-up = FAIL.

Therefore: three independent thresholds, each a ratio or boolean. Aggregate PASS is conjunction. Direction: PASSes are tight (1%, 0.05%, boolean-positive); framework's ZFP claim for the SM electroweak sector rests on the V.2 upstream derivation.
```

Python verification: `import math; print(172.69 * math.sqrt(2) / 246.0)` → 0.9928... (as stated above).

**11. Implications**:
- **If aggregate PASS**: mu_BC obligation (i) — and by extension the quark/lepton mass hierarchy via Yukawa closure + MW-consistency — is discharged. The framework's prediction for the Standard Model electroweak sector is ZFP at the mu_BC level.
- **If partial PASS**: Identifies which sub-sector (Yukawa / MW / RG flow) is the remaining obstruction. Directional constraint on the V.2 derivation pathway.
- **If FAIL across all three**: The "12" exponent in mu_BC is ACCOMMODATION, not ZFP; the framework's electroweak-sector prediction is SCHEME-DEP per W4-48, and this is recorded permanently in the ledger with explicit flag.
- **If PRE-REG-INCOMPLETE**: Gate defers to S86 with upstream V.2 redispatched via other routes (e.g., adding a 4th route).

**12. Effort**: 1.5 agent-sessions (MEDIUM-HIGH); three parallel sub-agents; conditional on V.2 upstream resolution.

**13. Substrate framing**: Yukawa couplings, MW mass, and RG flow are emergent QFT observables. The substrate's spectral triple fixes the mu_BC via the Jensen-tau eigenvalue structure; the "12" exponent is a geometric integer from the substrate's representation-theoretic or heat-kernel structure. The "Standard Model" is the QFT-lens effective theory on the substrate at energies << KK threshold. RG flow is the substrate's spectral-action response to scale-variation; Landau poles or tachyonic inversions would indicate substrate-level pathology (spectral action non-convex at some scale), not QFT-level pathology alone.

---

## Wave W9 → Wave W10 Decision Point

**Required upstream for W9 dispatch**:
- W9-1, W9-2, W9-3, W9-4: dispatch immediately (no upstream dependency beyond S84 artifacts).
- W9-5: dispatch AFTER upstream V.2 resolution (S85 W0 or W2). Orchestrator checks for `S85-MU-BC-OBLIGATION-I-DERIV` verdict in `computations/s85_gate_verdicts.txt` before dispatching W9-5. If absent at W9 dispatch time, W9-5 is deferred to the next batch (still within S85 if latency allows; otherwise S86 with PRE-REG-INCOMPLETE carry-forward).

**Emitted to W10 (kaku-speculative-theorist)**:
- W9 outputs are read by W10 only if they touch the Witten-alternative-parents item (S85-WITTEN-ALTERNATIVE-PARENTS) — the folded-triangle bispectrum (W9-3) may inform the alternative-parents enumeration.
- No direct W9 → W10 dependency.

**Orchestrator action at W9 close**:
- Read `computations/s85_gate_verdicts.txt` for W9-1..W9-5 verdict lines.
- Run `v3-closure-audit.sh` per `.claude/rules/v3-closure-recovery.md`. If any sig_* = 0, execute Stage-1 remediation (max 2 iterations per signal).
- Update `permanent-results-registry.md` via registry-landing sub-script (W9-1, W9-2).
- Run `/weave --update` to rebuild knowledge index.
- Append to S85 handoff §5 (action items) any W9-5 PRE-REG-INCOMPLETE carry-forward to S86.

---

## Wave W9 Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §PRDR, enumerate every free parameter in every W9 gate. The consolidated pin table:

| Gate | Parameter | Value | Provenance |
|:-----|:----------|:------|:-----------|
| W9-1 | tau_scan_range | [0.05, 0.35] | W10-121 original |
| W9-1 | tau_step | 0.005 | W10-121 inherited |
| W9-1 | Borel_threshold | 4.34 | W10-121 verdict |
| W9-1 | S_inst_min_reference | 2.42e5 | W10-121 verdict |
| W9-1 | L_max | 10 | canonical_constants |
| W9-1 | scheme | W10-121-original | no re-regulation |
| W9-1 | GPU_path | CPU-only | audit-class |
| W9-1 | random_seed | None | deterministic |
| W9-2 | regulators | [zeta, Zubarev, SDW, dim-reg, lattice-BR] | W6-69 atlas |
| W9-2 | product_ratio_tolerance | 2.22e-16 | machine epsilon float64 |
| W9-2 | T4_residual_threshold | 1e-3 | W6-69 reports 6.21e-4 |
| W9-2 | NLO_margin_required | 1000x | W6-69 reports 2445x |
| W9-2 | eps_H | 0.02163 | W6-69 |
| W9-2 | L_max | 10 | canonical |
| W9-2 | scheme | W6-69-atlas | no re-regulation |
| W9-2 | GPU_path | CPU-only | audit-class |
| W9-3 | l_max | 1e5 | 21-cm forecast horizon |
| W9-3 | shape_template | folded-triangle | |
| W9-3 | triangle_pruning | ridge-only | tractability |
| W9-3 | f_NL_prior_range | [-1e3, +1e3] | weak folded-NG bound |
| W9-3 | GGE_relic_cross_correlator | I-1-channel | framework registry |
| W9-3 | L_max_eigenvalue | 10 | canonical |
| W9-3 | scheme | analytic-template-folded | |
| W9-3 | convention | delta-function-ridge + 2% k-window | |
| W9-3 | random_seed | 42 | ridge MC |
| W9-3 | GPU_path | torch.linalg on ROCm | matrix eig |
| W9-3 | n_s_framework | 0.9561 | S84 |
| W9-3 | beta_s | -0.1331 | canonical |
| W9-4 | gate_count | 16 | W6-71 |
| W9-4 | floor_subclass_gates | [VII-K-PROP, CC5-ADJACENT, LEDGER-LINEARITY, M0-FCONV-BACK] | zero-cluster |
| W9-4 | cluster_subclass_gates | 12 | remaining |
| W9-4 | template_version | current HEAD | git SHA at runtime |
| W9-4 | compliance_target | 1.0 | |
| W9-4 | scheme | Mellin-balance-pre-declaration-v1 | |
| W9-4 | GPU_path | CPU-only | audit-class |
| W9-4 | random_seed | None | deterministic |
| W9-5 | sub_gate_count | 3 | Yukawa, MW, tau-cross |
| W9-5 | upstream_dependency | S85-MU-BC-OBLIGATION-I-DERIV | V.2 route |
| W9-5 | y_t_tolerance | 1e-2 | 1% Yukawa closure |
| W9-5 | m_W_tolerance | 5e-4 | PDG precision |
| W9-5 | m_W_obs | 80.379 GeV | PDG 2024 |
| W9-5 | mu_BC_accommodated | 188.185 GeV | S84 W9b-105 |
| W9-5 | tau_cross_scale_range | [M_Z, M_Planck] | |
| W9-5 | L_max | 10 | canonical |
| W9-5 | scheme | V.2-upstream-conditional | |
| W9-5 | convention | MS-bar, 1-loop Yukawa, 2-loop MW | |
| W9-5 | random_seed | None | deterministic |
| W9-5 | GPU_path | torch.linalg for eig>100x100 | |

**Machinery-enumeration cardinality (D_PRU_raw)**: 0. All parameters pinned either to a numerical value, an enumerated set, or a runtime-resolved reference (canonical_constants lookup or git SHA). Per the PRU cardinality audit (`_pru_cardinality_audit.py`), this plan should emit `D_PRU_raw = 0` when validated.

---

## Wave W9 Input-SHA Ledger

SHAs resolved at script-runtime via `hashlib.sha256(file_bytes)`. Static-input SHAs are listed with explicit file paths; dynamic outputs are `<computed-at-runtime>`.

| Gate | Input file | SHA pin |
|:-----|:-----------|:--------|
| W9-1 | `computations/s84_w10_121_borel_floor.npz` (slug resolved via W10-121 artifact lookup) | `<computed-at-runtime>` |
| W9-1 | `computations/canonical_constants.py` | `<computed-at-runtime>` |
| W9-1 | `sessions/framework/permanent-results-registry.md` (pre-landing) | `<computed-at-runtime>` |
| W9-2 | `computations/s84_w6_f_amp_3pi_fi_chain.npz` | `<computed-at-runtime>` |
| W9-2 | `computations/s84_w6_mellin_balance_template_audit.csv` | `<computed-at-runtime>` |
| W9-2 | `computations/canonical_constants.py` | `<computed-at-runtime>` |
| W9-2 | `sessions/framework/permanent-results-registry.md` (pre-landing) | `<computed-at-runtime>` |
| W9-3 | `computations/canonical_constants.py` | `<computed-at-runtime>` |
| W9-3 | Jensen-tau eigenvalue cache (path resolved at runtime from L_max=10 canonical) | `<computed-at-runtime>` |
| W9-4 | `.claude/templates/mellin-balance-pre-declaration.md` | `<computed-at-runtime>` |
| W9-4 | `computations/s84_w6_mellin_balance_template_audit.csv` | `<computed-at-runtime>` |
| W9-4 | `computations/s84_w6_mellin_balance_template_audit.py` | `<computed-at-runtime>` |
| W9-5 | `computations/canonical_constants.py` | `<computed-at-runtime>` |
| W9-5 | `computations/s85_gate_verdicts.txt` (for upstream V.2 verdict lookup) | `<computed-at-runtime>` |
| W9-5 | `computations/s84_gate_verdicts.txt` (for W9b-107/108/109 PRE-REG-INCOMPLETE lines) | `<computed-at-runtime>` |

**Output closure-SHA pins** (emitted by each script per `gate-verdicts.md` S81+ format):

| Gate | Output closure SHA |
|:-----|:-------------------|
| W9-1 | `<computed-at-runtime>` (from closure_hash(pins) over W9-1 machinery table) |
| W9-2 | `<computed-at-runtime>` |
| W9-3 | `<computed-at-runtime>` |
| W9-4 | `<computed-at-runtime>` |
| W9-5a | `<computed-at-runtime>` |
| W9-5b | `<computed-at-runtime>` |
| W9-5c | `<computed-at-runtime>` |
| W9-5  | `<computed-at-runtime>` (aggregate over sub-SHAs) |

**Verdict-line format** (per `.claude/rules/gate-verdicts.md` S81+ canonical form, appended to `computations/s85_gate_verdicts.txt`):

```
S85-W9-BOREL-FLOOR-REGISTRY-LANDING: PASS|FAIL|INFO -- value=<v> scheme=W10-121-original convention=Borel-disk-pointwise L_max=10 sha256=<64-char-closure>
S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING: PASS|FAIL|INFO -- value=<v> scheme=W6-69-atlas convention=MS-z_R-pair L_max=10 sha256=<64-char-closure>
S85-W9-FOLDED-TRIANGLE-21CM-SHAPE: PASS|FAIL|INFO -- value=<f_NL_folded> scheme=analytic-template-folded convention=delta-ridge-2pct L_max=1e5 sha256=<64-char-closure>
S85-W9-MELLIN-BALANCE-16-OF-16: PASS|FAIL|INFO -- value=<compliance_fraction> scheme=Mellin-balance-v1 convention=floor+cluster L_max=10 sha256=<64-char-closure>
S85-W9-YUKAWA-MW-TAUCS-REOPEN: PASS|FAIL|INFO|PRE-REG-INCOMPLETE -- value=<aggregate> scheme=V2-conditional convention=MS-bar L_max=10 sha256=<64-char-aggregate>
S85-W9-YUKAWA-MW-TAUCS-REOPEN-5a: PASS|FAIL -- value=<y_t_pred> scheme=V2-conditional convention=SM-tree L_max=10 sha256=<64-char>
S85-W9-YUKAWA-MW-TAUCS-REOPEN-5b: PASS|FAIL -- value=<m_W_pred> scheme=V2-conditional convention=MS-bar-2loop L_max=10 sha256=<64-char>
S85-W9-YUKAWA-MW-TAUCS-REOPEN-5c: PASS|FAIL -- value=<mu_BC_tau_cross> scheme=V2-conditional convention=RG-flow L_max=10 sha256=<64-char>
```

---

## Compliance summary

- 5 gate blocks with 13-field specs — COMPLETE
- Machinery-enumeration pin (§PRDR) — COMPLETE (D_PRU_raw = 0 target)
- Input-SHA ledger — COMPLETE (all inputs enumerated with `<computed-at-runtime>` where appropriate)
- Substitution chains for all sign/direction/threshold claims — COMPLETE (W9-1, W9-2, W9-3, W9-4, W9-5 each carry explicit chain with Python-verified arithmetic where applicable)
- Substrate framing present per-gate and in wave-level preamble — COMPLETE
- No execute instructions; no cross-wave writes; no working-paper sections — COMPLETE (per /rclab-plan rules)
- Script prefix `s85_w9_` — enforced across all 5 gates (and 3 W9-5 sub-scripts)
- Verdict file `computations/s85_gate_verdicts.txt` — canonical path per `.claude/rules/gate-verdicts.md`
- Gate IDs checked against S82/S83/S84 verdict files — no collisions
