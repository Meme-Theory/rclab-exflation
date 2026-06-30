# Session 86 Plan — Wave W3: Mellin-cone consequences

**Wave**: W3
**Owner subagent_type**: `lizzi-spectral-functional-theorist`
**Theme**: Mellin-cone consequences — use W2 infrastructure (C9 + C10 + C12) to close 3 W0-W5 Mellin-strip truncation FAILs (W0-7, W0-11, W0-20), land the REPLACEMENT-B asymptotic portion of the ζ-stabilization theorem (T9), extend the cluster-span identity beyond W0-3 single-K validation (C13), and disambiguate the W3-9 vs W3-11 Λ-convention dispute via empirical Λ_actual extraction (C43).
**Item count**: 6 (T9, W0-7 re-emit, W0-11 re-emit, W0-20 re-emit, C13, C43)
**Effort estimate**: ~10-12 agent-hours combined
**Level**: LEVEL 1 (must-do for S86)
**Verdict-file path**: `computations/s86_gate_verdicts.txt` (canonical, per `.claude/rules/gate-verdicts.md`)

---

## §0. Wave W3 Summary

W3 is the consequence-wave of W2's Mellin-Barnes infrastructure build. Its content is **structurally downstream** of W2: T9's REPLACEMENT-B asymptotic landing, the three W0-X re-emissions, and C13's cluster-span K-corridor extension all consume the `analytic_zeta(s, L_max)` API delivered by C10 and the master Mellin-Barnes residue extractor delivered by C9. C43 is the only W3 gate logically independent of W2 — it consumes W0c's C14 Λ_top empirical extraction and re-runs S85's W3-11 under the empirical convention.

**Substrate framing**: every W3 gate is a GEOMETRIC observation of how the substrate's spectral content (the Dirac-operator eigenvalue spectrum of D_K on Jensen-deformed SU(3)) behaves under analytic continuation in the Mellin parameter s and across the K-corridor. Mellin-Barnes residues are not regulator artifacts — they are the structural floor of the substrate's regulator-class taxonomy (lizzi S-1 Regulator-Family Boundary Theorem + lizzi S-7 §V.6 Mellin Strip / Convergence Cone Theorem). What survives the analytic continuation is structural; what is lost in truncation is the W0-7/W0-11/W0-20 corridor that re-emission is now equipped to test.

**Mellin-cone consequences = substrate spectral-content reveals**: each gate states "the substrate's spectral content reveals X under Mellin continuation." T9 reveals the asymptotic form of S_zeta_E^cont/ζ_D(3) at s=4 leading residue. W0-7 reveals whether the Jensen-Zubarev kernel admits a Mellin-Barnes-continued ρ-fit. W0-11 reveals the CC-3 residue magnitude under continuation. W0-20 reveals the s=3 R_inf MB cone-apex value. C13 reveals the b_pow(span_2) = 2·b_pow(span_3) corollary across the K-corridor and the post-fold Riemann cover. C43 reveals which Λ-convention (Casimir-saturated, c_fabric·M_KK ad hoc, or empirical Λ_top) is consistent with the substrate's actual top eigenvalue.

---

## §0.5. Wave W3 Decision-Point Prerequisites

W3 has **HARD execution-time dependencies** on W2 + W0c. Plan-write proceeds in parallel with W2 / W0c plan-writes (per partition §4 dispatch schedule), but W3 dispatches at compute time only after the following land:

| Prerequisite | Provider gate | Required outcome | Consumer in W3 |
|:-------------|:--------------|:------------------|:---------------|
| Mellin-Barnes residue extractor with Seeley-DeWitt counter-term subtraction | W2 C9 (`S86-MELLIN-HEAT-KERNEL-INFRA`) | PASS (\|Λ_CC^MB\|/\|a_0\| ≤ 1e-1 AND χ²/dof ≤ 5) | W0-11 re-emit; T9 (REPLACEMENT-B asymptotic) |
| `analytic_zeta(s, L_max)` API at d_spec=8 NCG | W2 C10 (`S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE`) | PASS (`analytic_zeta(s=3, L_max=10)` finite AND χ²/dof ≤ 5) | W0-7 re-emit; W0-20 re-emit; T9 |
| Reusable cluster-span extractor module | W2 C12 (`S86-CLUSTER-SPAN-EXTRACTOR-BUILD`) | PASS (W0-3 reproduced at L_max ∈ {8,10,12}) | C13 |
| Empirical Λ_top from D_K spectral cache (λ_max(L=10) to 6 sig figs) | W0c C14 (`S86-LAMBDA-TOP-DIRECT-EXTRACTION`) | PASS (6 sub-criteria) | C43 |
| `K_crit_BdG = 2.035` registered distinct from `K_crit = 91.5` | W0c C17 (`S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION`) | PASS (canonical_constants.py update) | C13 (K-corridor labeling sanity) |
| `K_floor` + `K_wall` + W5 D.4 registry block | W0c C19 (`S86-K-FLOOR-K-WALL-LAND`) | PASS | C13 (corridor endpoints) |

**Substitution chain — execution-time dependency closure**:
```
Step 1: W3 = {T9, W0-7-MB, W0-11-MB, W0-20-MB, C13, C43}
Step 2: requires(T9) = {C9, C10}; requires(W0-7-MB) = {C10}; requires(W0-11-MB) = {C9}; requires(W0-20-MB) = {C10}; requires(C13) = {C12, C17, C19}; requires(C43) = {C14}
Step 3: union(requires) = {C9, C10, C12, C14, C17, C19}; all live in {W2, W0c}
Step 4: W3 cannot dispatch before W2 ∧ W0c land. Direction: dispatch-after.
Conclusion: W3 enters compute queue ONLY after W2 (C9 PASS, C10 PASS, C12 PASS) and W0c (C14 PASS, C17 PASS, C19 PASS). Per partition §4 dispatch schedule, W3 is in Batch 2; Batch 2 launches "immediately after Batch 1 has ≥3 completions" — but for W3 specifically, the orchestrator gates dispatch on the 6 prerequisite verdicts above, not on Batch 1 completion count alone.
```

---

## §I. Carry-Forward Items Mapping

| W3 Item | Carry-Forward ID (closeout / partition) | Source synthesis | Effort | Level | Sequencing |
|:--------|:-----------------------------------------|:-----------------|:-------|:-----|:-----------|
| §W3-1 T9 `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` (REPLACEMENT-B asymptotic) | T9 (closeout §3.1; partition §1 W3) | lizzi 9A §A-2 + gen-physicist 9A §4.7 (3A REPLACED) | MODERATE 4-6h | PRIORITY 1 | HARD: requires C9 PASS + C10 PASS |
| §W3-2 W0-7 re-emission `S86-W0-7-MB-RE-EMIT` | W0-7 re-emission (partition §1 W3 line item 2) | gen-physicist S-7 §V.2 + lizzi S-7 §V.1 | 2h LOW-MODERATE | PRIORITY 1 | HARD: requires C10 PASS |
| §W3-3 W0-11 re-emission `S86-W0-11-MB-RE-EMIT` | W0-11 re-emission (partition §1 W3 line item 3) | lizzi S-7 §V.1 + gen-physicist S-7 §V.2 | 1.5h LOW | PRIORITY 1 | HARD: requires C9 PASS |
| §W3-4 W0-20 re-emission `S86-W0-20-MB-RE-EMIT` | W0-20 re-emission (partition §1 W3 line item 4) | lizzi S-7 §V.1 + gen-physicist S-7 §V.2 | 1.5h LOW | PRIORITY 1 | HARD: requires C10 PASS |
| §W3-5 C13 `S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION` | C13 (closeout §3.6 C13) | gen-physicist S-7 §V.4 | 2h LOW | PRIORITY 1 | HARD: requires C12 PASS, C17 PASS, C19 PASS |
| §W3-6 C43 `S86-W3-11-LAMBDA-CONVENTION-RESOLUTION` | C43 (closeout §3.6 C43) | lizzi S-7 §V.13 | 2-3h LOW | PRIORITY 1 | HARD: requires C14 PASS (Λ_top empirical) |

All 6 items are LEVEL 1 must-do per closeout §7.2 + partition §3.2.

---

## §W3-1. S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING (T9 REPLACEMENT-B)

**1. Gate ID**: `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING`

**2. Trigger**: `[VERIFY-THEOREM]` — asymptotic structural property at s=4 leading residue requires both the analytic-continuation proof (existence + non-vanishing of leading residue at s=4 in d_spec=8 NCG) AND a counterexample probe at L_max ∈ {7, 8, 9, 10} confirming the limit is approached monotonically. The theorem is conditional on C9 + C10 PASS; if either prerequisite FAILs in W2, T9 dispatches in PRE-REG-INCOMPLETE state with the prerequisite-failure rationale logged.

**3. Classification**: GEOMETRIC — operates on spectral structure of D_K on Jensen-deformed SU(3); the asymptotic limit `lim_{L→∞} S_zeta_E^cont(L) / ζ_D(3, L) > 1+ε` is a property of the substrate's regularized spectral functional, not of any propagating field. Per `.claude/rules/phononic-framing.md` classification guide, GEOMETRIC = "concerns the spectral triple structure, D_K eigenvalues, Jensen deformation, fiber topology — the fabric itself rather than its excitations."

**4. Agent type**: `lizzi-spectral-functional-theorist` — this agent is the originator of the ζ-spectral-action theory (arXiv:1412.4669) and authored the REPLACEMENT-B asymptotic spec (lizzi 9A §A-2). The agent's core methodology — "compare results across cutoff, zeta, and anomaly-derived actions; what is functional-independent is structural; what is functional-dependent requires determination" — is exactly the test T9 imposes on the asymptotic-residue claim. **Rationale for not assigning gen-physicist**: gen-physicist is a breadth-coordinator and stalls on dense single-functional asymptotic proofs (S84 W1/W2 lesson, partition §5 dispatch note 4). T9 is a single-functional theorem-landing; specialist authorship is mandatory. Fallback specialist if Lizzi unavailable: `connes-ncg-theorist` (NCG asymptotic analysis is within Connes-track competence; spectral-action s=4 leading-residue extraction is a pure NCG result).

**5. Hypothesis** (one sentence): The ratio `S_zeta_E^cont(L_max) / ζ_D(3, L_max)` admits a finite limit > (1 + ε_T9) as L_max → ∞ when computed via the C10 `analytic_zeta(s, L_max)` API extracting the s=4 leading residue, with ε_T9 = 0.01 the structural-stability tolerance per lizzi 9A §A-2.

**6. Method** (complete dispatch prompt):

```
Run `computations/s86_w3_zeta_stabilization_theorem.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- Input pin: SHA-256 of `computations/s86_w2_mellin_cone_residue_infra.py` output
  payload (provider: W2 C10; runtime SHA recorded in s86_gate_verdicts.txt at C10 PASS)
- Input pin: SHA-256 of `computations/s86_w2_mellin_heat_kernel_infra.py` output
  payload (provider: W2 C9; runtime SHA recorded at C9 PASS)
- Import `analytic_zeta` from `_mellin_cone_residue_infra.py` API (W2 C10 build)
- For L_max ∈ {7, 8, 9, 10}:
    Compute S_zeta_E^cont(L_max) via analytic_zeta(s=4, L_max) leading-residue extraction
    Compute ζ_D(3, L_max) via direct evaluation
    Compute ratio_L = S_zeta_E^cont(L_max) / ζ_D(3, L_max)
- Fit asymptotic form ratio_L = ratio_inf + alpha · L_max^(-beta) via least-squares
- Test (a) ratio_inf > 1 + ε_T9 with ε_T9 = 0.01
- Test (b) monotone-increasing ratio across {7, 8, 9, 10}: ratio_8 ≥ ratio_7 - δ_mon, etc.,
  with δ_mon = 1e-6 (allows numerical noise)
- Test (c) Richardson extrapolation residual ≤ 5% of (ratio_inf - 1)
- Counterexample probe: at L_max=10, perturb leading-residue extraction kernel by
  ±1% (proxy for analytic-continuation systematic) and check ratio_L stays > 1 + ε_T9 / 2
  on at least one perturbation arm

GPU: use `torch.linalg` for any eigvals/SVD/matmul on matrices ≥100×100 (D_K block
sizes at L_max=10 are ~155,984 eigenvalues; use ROCm 7.2 path on AMD RX 9070 XT,
17.1 GB VRAM). Cap `OMP_NUM_THREADS = 8` if any CPU fallback path executes.

Outputs:
- `computations/s86_w3_zeta_stabilization_theorem.npz` (ratio_L array, fit
  coefficients, monotonicity diagnostic, counterexample-probe outcomes)
- `computations/s86_w3_zeta_stabilization_theorem.png` (ratio_L vs L_max plot
  with asymptote)
- `computations/s86_w3_zeta_stabilization_theorem.json` (verdict 4-tuple +
  Richardson residual + tests (a)/(b)/(c) outcomes)

Verdict line append to `computations/s86_gate_verdicts.txt`:
S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING|<VERDICT>|<value=ratio_inf>|
  scheme=zeta|convention=s4_leading_residue_d8|L_max=10|content_sha256:<64-hex>|
  audit_sha256:<64-hex>

Companion comment row: # audit_sha256_short=<16-hex>
```

**7. Machinery pin (PRDR)**:
- `L_max`: {7, 8, 9, 10} (4-point ladder for Richardson + monotonicity)
- `scheme`: `zeta` (S_zeta_E^cont built on ζ_D(s) via analytic continuation)
- `convention`: `s4_leading_residue_d8` (s=4 leading residue, d_spec=8 NCG dimension)
- `n_eval`: leading-residue extraction at single s=4 + ζ_D(3) at single s=3 per L_max → 8 evaluations total
- `scan_range`: L_max ladder fixed; no scan
- `step_size`: N/A (analytic, not numerical-integration)
- `tolerance`: ε_T9 = 0.01 (structural-stability bound on ratio_inf - 1)
- `random_seed`: N/A (deterministic Mellin-Barnes residue)
- `GPU path`: `torch.linalg` (ROCm 7.2 / AMD RX 9070 XT) for D_K eigvals at L_max=10; CPU fallback caps `OMP_NUM_THREADS = 8`
- `cutoff_axis`: `spectral` (per W0a R3 YAML pin; ζ-class regulator is spectral, not coherence)
- `regulator_pin_tag`: `a_4^{ζ}` for any bare `a_4` citation in script (per W0c P14)

**8. Expected output 4-tuple**:
`(value=<ratio_inf, fitted asymptote>, scheme=zeta, convention=s4_leading_residue_d8, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: all 3 tests pass — (a) ratio_inf > 1 + ε_T9 = 1.01; (b) monotone-increasing ratio across {7, 8, 9, 10}; (c) Richardson residual ≤ 5% of (ratio_inf - 1)
- **FAIL**: test (a) fails — ratio_inf ≤ 1.01, indicating no structural stabilization beyond unity in the asymptotic limit
- **INFO**: test (a) PASSes but (b) or (c) fails — asymptote exists but approach is non-monotone or extrapolation is unstable; the theorem is empirically supported but the structural-monotonicity claim is qualified
- **PRE-REG-INCOMPLETE**: C9 OR C10 FAILed in W2 — REPLACEMENT-B asymptotic cannot be tested without the analytic-continuation infrastructure
- **Tolerance rule**: THEOREM (binary structural property; ε_T9 is the asymptotic-limit margin, not a fit-quality tolerance)

**10. Substitution chain** (asymptotic-limit direction):
```
Step 1 (definitions):
  S_zeta_E^cont(L) = sum over L_max=L eigenvalues of D_K of leading residue at s=4
                     of analytic_zeta(s, L) (per lizzi 9A §A-2)
  ζ_D(3, L)       = direct evaluation of spectral zeta at s=3, L_max=L
  ratio_L         = S_zeta_E^cont(L) / ζ_D(3, L)
  ratio_inf       = lim_{L→∞} ratio_L (target of fit)
  ε_T9            = 0.01 (per lizzi 9A §A-2 structural-stability margin)

Step 2 (substitute the PASS test (a)):
  PASS_a = (ratio_inf > 1 + ε_T9) = (ratio_inf > 1.01)

Step 3 (simplify; no algebra collapse — direct comparison):
  PASS_a ⇔ asymptotic value of S_zeta_E^cont / ζ_D(3) exceeds unity by at least 1%

Step 4 (direction from canonical form):
  IF ratio_inf > 1.01 THEN structural stabilization HOLDS
                          (the ζ-regulator restores the target functional above
                           direct ζ_D(3) by a non-trivial margin in the L→∞ limit)
  IF ratio_inf ≤ 1.01 THEN structural stabilization FAILS
                          (no asymptotic separation; REPLACEMENT-B does not deliver
                           the claimed regulator-class stabilization)

Conclusion: PASS direction is "ratio_inf strictly exceeds 1.01"; the test does
not assume sign, only magnitude relative to a hard floor at 1.0 + ε_T9. Per
math-scripts.md, no further sign/direction claims are made without explicit
substitution of the fitted ratio_inf into the comparison.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: REPLACEMENT-B asymptotic completes the ζ-stabilization theorem (alongside REPLACEMENT-A windowed kinematic, PROVEN at L ∈ {5,6,7,8} per closeout §1.3). The combined REPLACEMENT-A + REPLACEMENT-B pair is then the canonical replacement for the original 3A ζ-stabilization theorem (which was retracted in S85 per closeout §1.3) and lands as a permanent §VII registry entry. The substrate's spectral content is structurally stable above ζ_D(3) under analytic continuation to s=4.
- **FAIL**: REPLACEMENT-B is structurally vacuous; the asymptotic limit does not separate from ζ_D(3) and the regulator-stabilization claim collapses to the windowed-kinematic content of REPLACEMENT-A alone. The 3A ζ-stabilization line of inquiry closes definitively. lizzi 9A §A-2's asymptotic-limit conjecture is refuted; the theorem as stated requires re-formulation OR retraction.
- **INFO**: The asymptote exists but its approach is non-monotone or unstable; theorem is provisionally supported with monotonicity-qualifier annotation in the registry. Future S87+ work would need to refine the asymptotic-form ansatz (e.g., higher-order Richardson terms or non-power-law approach).

**12. Effort estimate**: 4-6h MODERATE (per partition §1 W3 + closeout §3.1 T9). Heavy-side because the C10 `analytic_zeta` API must be exercised at 4 L_max values + Richardson fit + counterexample probe; light-side because the test is single-functional (ζ only) and the s=4 evaluation is at a single point per L_max.

**13. Substrate-framing reminder**: T9 is a GEOMETRIC theorem about the substrate's spectral content. State as: **"The substrate's spectral content reveals an asymptotic structural-stability margin above the direct ζ_D(3) value when the spectral functional is built via Mellin-cone analytic continuation to s=4; the L→∞ limit is the substrate's regulator-class structural floor."** Avoid framing as "the ζ-functional better approximates ζ_D(3)" (this is functional-comparison narrative); the correct framing is "the substrate's spectral structure admits a finite asymptotic value of the ratio S_zeta_E^cont / ζ_D(3) > 1, structurally." Per `.claude/rules/phononic-framing.md`: substrate is logically prior; the spectral-functional language is consequence, not cause.

---

## §W3-2. S86-W0-7-MB-RE-EMIT (W0-7 Mellin-Barnes Re-emission)

**1. Gate ID**: `S86-W0-7-MB-RE-EMIT`

**2. Trigger**: `[VERIFY]` — quantitative re-emission of W0-7 Jensen-Zubarev ρ-conjecture under the C10 Mellin-Barnes-continued kernel; ρ-fit value with uncertainty band determines PASS-or-explicitly-refuted state. Original W0-7 FAIL (S85: ρ=−1 conjecture refuted, c_0=−0.8104 from unconstrained fit) was attributed to truncated heat-kernel inadequacy; the MB-continuation route is the structural test of whether truncation was the cause.

**3. Classification**: GEOMETRIC — operates on the Jensen-Zubarev kernel (analytic substrate-regulator pair) and tests a structural exponent ρ in the kernel's analytic continuation; ρ is a geometric exponent of the spectral functional, not a particle/excitation observable.

**4. Agent type**: `spectral-geometer` (heat-kernel asymptotics + analytic continuation are within spectral-geometer competence) OR `lizzi-spectral-functional-theorist` (Lizzi authored the original W0-7 conjecture analysis per gen-physicist S-7 §V.2 + lizzi S-7 §V.1; preferred). **Rationale for not assigning gen-physicist**: re-emission is a focused single-kernel test; specialist authorship per partition §5 dispatch note 4. Both `spectral-geometer` and `lizzi-spectral-functional-theorist` are acceptable; primary assignment to `lizzi-spectral-functional-theorist` because Lizzi co-owns W3 wave (originator-track per partition §1 W3 owner field).

**5. Hypothesis**: The Jensen-Zubarev kernel ρ-exponent, fit under the Mellin-Barnes-analytically-continued form (provided by C10 `analytic_zeta`), lands within ρ ∈ [−1.05, −0.95] (the ρ=−1 conjecture corridor with 5% structural margin); if not, the conjecture is explicitly refuted under the MB-continuation route AND the W0-7 FAIL is upgraded from "truncation-attributable" to "structural" — closing the truncation-attributable corridor.

**6. Method** (complete dispatch prompt):

```
Run `computations/s86_w3_w0_7_mb_re_emit.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- Input pin: SHA-256 of original W0-7 Jensen-Zubarev kernel definition file (S85
  W0-7 producing-script SHA, recoverable from s85_gate_verdicts.txt W0-7 line)
- Input pin: SHA-256 of `s86_w2_mellin_cone_residue_infra.py` output (W2 C10
  PASS-pinned; runtime SHA from s86_gate_verdicts.txt at C10 PASS)
- Import `analytic_zeta(s, L_max)` from W2 C10 module
- Load Jensen-Zubarev kernel K_JZ(t) at L_max=10 (D_K cache from W0c C14 or
  upstream; pin SHA recoverable at runtime)
- Apply analytic_zeta to the Mellin-continued form of K_JZ:
    M[K_JZ](s) = ∫_0^∞ t^(s-1) K_JZ(t) dt under Mellin-Barnes contour
                 (provided by C10 API at d_spec=8 NCG)
- Fit ρ via linear regression in log-log space:
    ln(M[K_JZ](s)) = c_0 + ρ · ln(s) + higher-order terms
  over s ∈ [s_min, s_max] = [2.5, 4.5] (Mellin strip per closeout §1.5
  Mellin Strip / Convergence Cone Theorem)
- Report ρ ± σ_ρ from least-squares covariance
- Test PASS criterion: ρ ∈ [−1.05, −0.95]
  Test FAIL criterion: ρ outside [−1.05, −0.95] with σ_ρ < 0.025 (statistical
  significance > 2σ)
  Test INFO: ρ outside but σ_ρ ≥ 0.025 (band overlaps; ambiguous)
- Cross-check: report c_0 and compare to S85 W0-7 unconstrained-fit value
  c_0 = −0.8104; document MB-continuation effect on c_0 (diagnostic only)

GPU: `torch.linalg` for D_K eigvals at L_max=10; CPU fallback `OMP_NUM_THREADS=8`.

Outputs:
- `s86_w3_w0_7_mb_re_emit.npz` (ρ array over s-window, fit coefficients,
  covariance, c_0 diagnostic)
- `s86_w3_w0_7_mb_re_emit.png` (log-log fit plot)
- `s86_w3_w0_7_mb_re_emit.json` (verdict 4-tuple + ρ ± σ_ρ + c_0 diagnostic)

Verdict line:
S86-W0-7-MB-RE-EMIT|<VERDICT>|<value=ρ ± σ_ρ>|scheme=Jensen-Zubarev|
  convention=Mellin-Barnes-continued|L_max=10|content_sha256:<64-hex>|
  audit_sha256:<64-hex>
```

**7. Machinery pin (PRDR)**:
- `L_max`: 10 (single-point; ρ-fit is a kernel property, not L_max-converged extrapolation)
- `scheme`: `Jensen-Zubarev` (the kernel under test; structurally distinct from ζ-class regulators per closeout §1.5 F_4 / M partition)
- `convention`: `Mellin-Barnes-continued` (the analytic continuation route, not direct truncation)
- `n_eval`: ρ-fit over s ∈ [2.5, 4.5] sampled at 21 equispaced points (Δs = 0.1)
- `scan_range`: s ∈ [2.5, 4.5] (Mellin strip per Mellin Strip Theorem)
- `step_size`: Δs = 0.1
- `tolerance`: PASS-band ρ ∈ [−1.05, −0.95]; statistical-significance threshold σ_ρ < 0.025 for FAIL classification
- `random_seed`: N/A
- `GPU path`: `torch.linalg` (ROCm 7.2)
- `cutoff_axis`: `coherence` (Jensen-Zubarev is a coherence-class kernel per W0a R3 YAML pin; distinguish from spectral ζ)
- `regulator_pin_tag`: `M[K_JZ]^{Jensen-Zubarev,MB-continued}` for kernel citations

**8. Expected output 4-tuple**:
`(value=<ρ ± σ_ρ>, scheme=Jensen-Zubarev, convention=Mellin-Barnes-continued, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: ρ ∈ [−1.05, −0.95] (Jensen-Zubarev ρ=−1 conjecture confirmed under MB-continuation; W0-7 truncation FAIL was structural-from-truncation, not structural-from-kernel)
- **FAIL**: ρ outside [−1.05, −0.95] with σ_ρ < 0.025 (conjecture explicitly refuted under MB-continuation; W0-7 FAIL is structural-from-kernel, NOT truncation-attributable; a permanent corridor closure)
- **INFO**: ρ outside but σ_ρ ≥ 0.025 (band overlaps PASS-corridor edges; ambiguous; further refinement of fit window required in S87+)
- **Tolerance rule**: ABSOLUTE (ρ-band is a hard structural bound; not relative to S85 c_0=−0.8104)

**10. Substitution chain** (ρ direction):
```
Step 1 (definitions):
  K_JZ(t)              = Jensen-Zubarev kernel (closeout §1.3 W0-7 source)
  M[K_JZ](s)           = Mellin transform of K_JZ via C10 analytic_zeta API
  Conjecture (lizzi)   : ln M[K_JZ](s) ~ c_0 + ρ · ln(s) with ρ = −1
  Empirical (S85 W0-7) : c_0 = −0.8104 from unconstrained fit (truncated heat kernel,
                         NOT MB-continued); ρ-fit was inconsistent with ρ=−1
  PASS-band            : ρ ∈ [−1.05, −0.95] (5% structural margin around ρ=−1)

Step 2 (substitute the PASS test):
  PASS_W0-7-MB = (|ρ - (−1)| ≤ 0.05) = (−1.05 ≤ ρ ≤ −0.95)

Step 3 (simplify; direct interval test):
  PASS_W0-7-MB ⇔ MB-continued ρ lies within 5% of canonical ρ=−1

Step 4 (direction from canonical form):
  IF ρ ∈ [−1.05, −0.95]  THEN MB-continuation RECOVERS the conjectured ρ=−1
                              (W0-7 FAIL was truncation-attributable; closure)
  IF ρ outside, σ_ρ small THEN conjecture is REFUTED structurally under MB
                              (W0-7 FAIL is structural-from-kernel, not from truncation)
  IF ρ outside, σ_ρ large THEN INFO; band overlaps; further work required

Conclusion: PASS direction is "ρ within 5% of −1"; the test does not assume the
sign of the deviation, only its magnitude relative to a centred hard band. Per
math-scripts.md, the direction claim "MB-continuation recovers ρ=−1" is conditional
on the PASS test outcome; not asserted ex ante.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: W0-7's S85 FAIL was truncation-attributable; the Jensen-Zubarev kernel structurally satisfies the ρ=−1 conjecture under analytic continuation. Closes the W0-7 corridor as a truncation FAIL, not a kernel-structural FAIL. Replaces the W0-7 FAIL line in the S85 verdict ledger with a PASS line in S86 (audit-distinct verdict line, NOT a retroactive S85 edit per `feedback_pre-registration-completeness.md`). Strengthens the F_4 / M regulator-class taxonomy (Jensen-Zubarev belongs to F_4 = {ζ, Zubarev, SDW} pure-a_4 family per closeout §1.5).
- **FAIL**: ρ-conjecture is structurally refuted; W0-7 FAIL is permanent-structural. The Jensen-Zubarev kernel does NOT satisfy ρ=−1 even under exact MB-continuation. lizzi S-1 Regulator-Family Boundary Theorem must be re-examined for whether this implies Jensen-Zubarev exits the F_4 family — a substrate spectral-content discovery that closes a corridor and opens a meta-question about regulator-family membership.
- **INFO**: ambiguous; band overlaps the boundary. S87+ refinement of the s-window or higher-order fit terms required. The S85 W0-7 FAIL line remains valid; S86 contributes a diagnostic re-emission, not a re-classification.

**12. Effort estimate**: 2h LOW-MODERATE. Re-emission consumes the C10 API; the work is analytic-continuation kernel evaluation + log-log fit, not infrastructure build.

**13. Substrate-framing reminder**: state as: **"The substrate's Jensen-Zubarev kernel reveals — under Mellin-Barnes analytic continuation to s ∈ [2.5, 4.5] — a ρ-exponent that either confirms or refutes the ρ=−1 conjecture as a structural property of the kernel itself, separately from any truncation-induced fit artifact."** The substrate's regulator-class structure is logically prior; the Jensen-Zubarev kernel is the substrate's specific regulator instantiation; the MB-continuation is the substrate's analytic-continuation route.

---

## §W3-3. S86-W0-11-MB-RE-EMIT (W0-11 CC-3 MB Residue Re-emission)

**1. Gate ID**: `S86-W0-11-MB-RE-EMIT`

**2. Trigger**: `[VERIFY]` — quantitative re-emission of W0-11 CC-3 Mellin-Barnes residue under the C9 master Mellin-Barnes residue extractor; the residue-magnitude criterion is the original W0-11 PASS-condition lifted from truncated form to MB-continued form.

**3. Classification**: GEOMETRIC — CC-3 is a substrate-residue observable at the Mellin-Barnes contour pole; structurally a property of the heat-kernel's analytic continuation, not of any specific particle/excitation channel.

**4. Agent type**: `spectral-geometer` (heat-kernel residue extraction is core spectral-geometer competence) OR `lizzi-spectral-functional-theorist` (Lizzi authored the W0-11 carry-forward rationale per closeout §3.6 C9 source: lizzi S-7 §V.1 + gen-physicist S-7 §V.2; preferred per W3 owner). Primary: `lizzi-spectral-functional-theorist`. **Rationale for not assigning gen-physicist**: per partition §5 dispatch note 4.

**5. Hypothesis**: The CC-3 residue, extracted via the C9 Mellin-Barnes residue extractor with explicit Seeley-DeWitt counter-term subtraction, satisfies the original W0-11 PASS criterion (\|Λ_CC^MB\|/\|a_0\| ≤ 1e-1 AND χ²/dof ≤ 5 per W2 C9 build's PASS spec — re-applied at the W0-11 entry point); if not, W0-11's truncation FAIL is upgraded to structural FAIL on the MB-continued kernel.

**6. Method** (complete dispatch prompt):

```
Run `computations/s86_w3_w0_11_mb_re_emit.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *`
- Input pin: SHA-256 of original W0-11 producing-script (recoverable from
  s85_gate_verdicts.txt W0-11 line)
- Input pin: SHA-256 of `s86_w2_mellin_heat_kernel_infra.py` output (W2 C9
  PASS-pinned)
- Import `mellin_barnes_residue_extractor()` from W2 C9 module (with explicit
  Seeley-DeWitt counter-term subtraction as built per W2 C9 spec)
- Compute Λ_CC^MB at L_max=10 via the C9 extractor on the W0-11 source kernel
- Compute |a_0| at L_max=10 from canonical_constants pinned a_0^{ζ} value
  (regulator-pin-tagged per P14)
- Compute ratio = |Λ_CC^MB| / |a_0|
- Compute χ²/dof of MB-continuation fit over the residue extraction window
- PASS criterion: ratio ≤ 1e-1 AND χ²/dof ≤ 5 (verbatim from W2 C9 PASS spec
  re-applied to W0-11 entry point per closeout §3.6 W0-11 source: lizzi S-7 §V.1
  + gen-physicist S-7 §V.2)
- INFO band: ratio ∈ (1e-1, 1e0] OR χ²/dof ∈ (5, 10] (ambiguous; documents
  partial closure)
- FAIL: ratio > 1 OR χ²/dof > 10 (structural FAIL under MB-continuation)

GPU: `torch.linalg`; CPU fallback OMP_NUM_THREADS=8.

Outputs:
- `s86_w3_w0_11_mb_re_emit.npz` (Λ_CC^MB, |a_0|, ratio, χ²/dof, residue-fit
  diagnostics)
- `s86_w3_w0_11_mb_re_emit.png` (residue-extraction plot)
- `s86_w3_w0_11_mb_re_emit.json` (verdict 4-tuple)

Verdict line:
S86-W0-11-MB-RE-EMIT|<VERDICT>|<value=|Λ_CC^MB|/|a_0|>|scheme=heat-kernel|
  convention=Mellin-Barnes-with-SD-subtraction|L_max=10|content_sha256:<64-hex>|
  audit_sha256:<64-hex>
```

**7. Machinery pin (PRDR)**:
- `L_max`: 10
- `scheme`: `heat-kernel` (the W0-11 source scheme; CC-3 residue extraction operates on heat-kernel coefficients)
- `convention`: `Mellin-Barnes-with-SD-subtraction` (per C9 master build; explicit Seeley-DeWitt counter-term subtraction)
- `n_eval`: residue extraction at single MB pole; χ²/dof over fit window of 11 points (Δs = 0.05 around pole)
- `scan_range`: MB pole window per C9 build
- `step_size`: Δs = 0.05 (in fit window)
- `tolerance`: ratio threshold 1e-1 (PASS), 1e0 (FAIL); χ²/dof threshold 5 (PASS), 10 (FAIL)
- `random_seed`: N/A
- `GPU path`: `torch.linalg`
- `cutoff_axis`: `spectral` (heat-kernel CC-3 is spectral-class)
- `regulator_pin_tag`: `a_0^{ζ}` (per W0c P14; canonical regulator-pinning of the bare a_0 reference)

**8. Expected output 4-tuple**:
`(value=<|Λ_CC^MB| / |a_0|>, scheme=heat-kernel, convention=Mellin-Barnes-with-SD-subtraction, L_max=10)`

**9. PASS/FAIL/INFO thresholds** (verbatim from W0-11 source via C9 master per closeout §3.6 / partition §1 W2 C9 spec):
- **PASS**: |Λ_CC^MB| / |a_0| ≤ 1e-1 AND χ²/dof ≤ 5
- **INFO**: |Λ_CC^MB| / |a_0| ∈ (1e-1, 1e0] OR χ²/dof ∈ (5, 10]
- **FAIL**: |Λ_CC^MB| / |a_0| > 1e0 OR χ²/dof > 10
- **Tolerance rule**: RATIO (the |Λ_CC^MB| / |a_0| criterion is a dimensionless ratio with explicit hard thresholds at 1e-1 and 1e0)

**10. Substitution chain** (CC-3 residue magnitude direction):
```
Step 1 (definitions):
  Λ_CC^MB     = CC-3 Mellin-Barnes-extracted residue with Seeley-DeWitt
                counter-term subtraction (per C9 master spec)
  a_0         = zeroth Seeley-DeWitt coefficient, regulator-pinned to a_0^{ζ}
                (per P14 canonical pin; ζ-class scheme)
  ratio_CC3   = |Λ_CC^MB| / |a_0|
  PASS_thr    = 1e-1 (per W2 C9 spec)
  FAIL_thr    = 1e0  (per W2 C9 spec)

Step 2 (substitute PASS test):
  PASS = (ratio_CC3 ≤ 1e-1) AND (χ²/dof ≤ 5)

Step 3 (simplify; direct comparison):
  PASS ⇔ MB-continued CC-3 residue is at most 10% of the bare a_0 magnitude
       AND the MB-fit quality is acceptable (χ²/dof ≤ 5)

Step 4 (direction from canonical form):
  IF ratio_CC3 ≤ 1e-1 AND χ²/dof ≤ 5  THEN MB-continuation closes W0-11
                                          truncation FAIL with structural PASS
  IF ratio_CC3 > 1e0 OR χ²/dof > 10    THEN MB-continuation fails to close
                                          W0-11; CC-3 residue is structurally
                                          inadmissible
  Intermediate                          THEN INFO band; partial closure

Conclusion: PASS direction is "ratio at most 0.1 AND fit at most χ²/dof=5".
Test does not assume Λ_CC^MB sign (only magnitude); does not assume direction
of MB-correction (only its size). All directional language is conditional on
the empirical ratio.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: W0-11 truncation FAIL was truncation-attributable; the Mellin-Barnes-continued kernel, with explicit Seeley-DeWitt counter-term subtraction, recovers the CC-3 PASS condition. Closes one of the 6 W0-W5 truncation FAILs (per closeout §1.4 partition: Truncation=6). The cumulative effect of W0-11 + W0-20 (both truncation FAILs in the W0-7/W0-11/W0-20 cluster) closing under MB-continuation would reduce the truncation-FAIL bulletin from 6 to 4.
- **FAIL**: W0-11 FAIL is structural under MB-continuation; the CC-3 residue exceeds the |a_0| anchor by > 1 OOM even after analytic continuation. This is a stronger substrate-content statement than the original truncation FAIL — the corridor closure is upgraded from "truncation-induced" to "kernel-structural." Affects the BULLETIN-W0W5-FAIL-PARTITION classification in W1c (the W0-11 entry would migrate from Truncation=6 to a structural-FAIL bulletin, requiring partition recount).
- **INFO**: partial closure; documents the MB-continuation effect direction (smaller or larger CC-3 residue than truncated form) without crossing the PASS threshold.

**12. Effort estimate**: 1.5h LOW. Single residue extraction + ratio test using already-built C9 infrastructure.

**13. Substrate-framing reminder**: state as: **"The substrate's CC-3 residue at the Mellin-Barnes contour pole reveals — under explicit Seeley-DeWitt counter-term subtraction — whether the W0-11 truncation FAIL was an artifact of the heat-kernel truncation or a structural property of the kernel under exact analytic continuation."** The substrate is logically prior; CC-3 is a substrate-residue observable; W0-11 is the gate that probes it.

---

## §W3-4. S86-W0-20-MB-RE-EMIT (W0-20 Mellin-cone s=3 R_inf Re-emission)

**1. Gate ID**: `S86-W0-20-MB-RE-EMIT`

**2. Trigger**: `[VERIFY]` — quantitative re-emission of W0-20 Mellin-cone s=3 R_inf gate under the C10 `analytic_zeta(s, L_max)` API evaluated off-pole at s=3 (the Mellin-cone apex per W6-5 — closeout §1.1 W6-5 PASS); the original W0-20 PASS criterion is re-applied at the analytic-continuation route.

**3. Classification**: GEOMETRIC — Mellin-cone apex evaluation at s=3 is a structural property of the spectral-zeta function under analytic continuation in d_spec=8 NCG; substrate-spectral-content observation, not particle/excitation observable.

**4. Agent type**: `spectral-geometer` (analytic continuation of spectral zeta is core competence) OR `lizzi-spectral-functional-theorist` (Lizzi authored the W0-20 carry-forward source per closeout §3.6 C10 source: lizzi 9A §A-1 + 3A REPLACEMENT-B prerequisite; preferred). Primary: `lizzi-spectral-functional-theorist`. **Rationale for not assigning gen-physicist**: specialist authorship per partition §5 note 4.

**5. Hypothesis**: `analytic_zeta(s=3, L_max=10)` evaluated off-pole at the Mellin-cone apex returns a finite R_inf value within the W0-20 PASS-criterion band, with χ²/dof ≤ 5 against direct subtraction (per C10 PASS spec re-applied at the W0-20 entry point); if not, W0-20's truncation FAIL is upgraded to structural FAIL.

**6. Method** (complete dispatch prompt):

```
Run `computations/s86_w3_w0_20_mb_re_emit.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"`:

- `from canonical_constants import *`
- Input pin: SHA-256 of original W0-20 producing-script (from s85_gate_verdicts.txt
  W0-20 line)
- Input pin: SHA-256 of `s86_w2_mellin_cone_residue_infra.py` output (W2 C10
  PASS-pinned)
- Import `analytic_zeta(s, L_max)` from C10 module
- Compute R_inf = analytic_zeta(s=3, L_max=10) off-pole evaluation in d_spec=8 NCG
- Cross-check: independently compute R_inf via direct heat-kernel subtraction
  (closed-form Seeley-DeWitt at s=3 in d=8); compute χ²/dof of MB-continued vs
  direct values
- PASS criterion: R_inf finite (no NaN, no inf, no overflow) AND χ²/dof ≤ 5
- INFO band: R_inf finite AND χ²/dof ∈ (5, 10]
- FAIL: R_inf non-finite OR χ²/dof > 10
- Diagnostic: report R_inf value with full MB-residue decomposition (leading +
  subleading residues at s=3) for downstream W6-5 (Mellin-cone apex universal
  s=3) cross-citation

GPU: `torch.linalg`; CPU fallback OMP_NUM_THREADS=8.

Outputs:
- `s86_w3_w0_20_mb_re_emit.npz` (R_inf, MB residue decomposition, direct-subtraction
  cross-check, χ²/dof)
- `s86_w3_w0_20_mb_re_emit.png` (analytic_zeta(s, L_max=10) curve through s=3)
- `s86_w3_w0_20_mb_re_emit.json` (verdict 4-tuple)

Verdict line:
S86-W0-20-MB-RE-EMIT|<VERDICT>|<value=R_inf>|scheme=zeta|
  convention=Mellin-cone-s3-off-pole-d8|L_max=10|content_sha256:<64-hex>|
  audit_sha256:<64-hex>
```

**7. Machinery pin (PRDR)**:
- `L_max`: 10
- `scheme`: `zeta` (analytic_zeta is ζ-class)
- `convention`: `Mellin-cone-s3-off-pole-d8` (s=3 off-pole evaluation in d_spec=8 NCG; the Mellin-cone apex per W6-5)
- `n_eval`: single-point at s=3 + direct-subtraction cross-check single-point + 5-point window for χ²/dof
- `scan_range`: s ∈ [2.95, 3.05] for χ²/dof window
- `step_size`: Δs = 0.025 (5-point window)
- `tolerance`: PASS R_inf finite + χ²/dof ≤ 5; FAIL non-finite or χ²/dof > 10
- `random_seed`: N/A
- `GPU path`: `torch.linalg`
- `cutoff_axis`: `spectral`
- `regulator_pin_tag`: `analytic_zeta^{Mellin-cone-d8}`

**8. Expected output 4-tuple**:
`(value=<R_inf>, scheme=zeta, convention=Mellin-cone-s3-off-pole-d8, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: R_inf finite (no NaN/inf) AND χ²/dof ≤ 5 (Mellin-cone apex closes W0-20 truncation FAIL)
- **INFO**: R_inf finite AND χ²/dof ∈ (5, 10] (apex evaluable but cross-check loose)
- **FAIL**: R_inf non-finite OR χ²/dof > 10 (Mellin-cone apex does NOT exist or diverges from direct subtraction; W0-20 FAIL is structural)
- **Tolerance rule**: ABSOLUTE (R_inf finiteness is binary; χ²/dof has explicit numeric thresholds)

**10. Substitution chain** (Mellin-cone apex at s=3 direction):
```
Step 1 (definitions):
  R_inf            = analytic_zeta(s=3, L_max=10)
                     (Mellin-cone apex value at d_spec=8 NCG, off-pole evaluation)
  R_inf^direct     = direct heat-kernel subtraction at s=3 in d=8
                     (closed-form Seeley-DeWitt; cross-check anchor)
  χ²/dof           = goodness-of-fit of MB-continued curve vs direct evaluation
                     over s ∈ [2.95, 3.05] window
  PASS_thr         = (R_inf finite) AND (χ²/dof ≤ 5)
  FAIL_thr         = (R_inf non-finite) OR (χ²/dof > 10)

Step 2 (substitute PASS test):
  PASS = isfinite(R_inf) ∧ (χ²/dof ≤ 5)

Step 3 (simplify; direct logical test):
  PASS ⇔ Mellin-cone apex at s=3 is empirically accessible (not pole-blocked)
       AND MB-continued value matches direct subtraction within χ²/dof ≤ 5

Step 4 (direction from canonical form):
  IF isfinite(R_inf) AND χ²/dof ≤ 5 THEN Mellin-cone apex EXISTS structurally;
                                         W0-20 truncation FAIL was truncation-
                                         attributable; closure
  IF non-finite                      THEN apex pole-blocked; W0-20 FAIL is
                                         structural-from-kernel-pole; corridor
                                         permanently closed
  IF χ²/dof > 10                     THEN apex evaluable but inconsistent with
                                         direct subtraction; FAIL on cross-check

Conclusion: PASS direction is "apex finite AND χ²/dof at most 5". Test does not
assume R_inf sign, only finiteness and cross-check consistency. Direction-of-
deviation diagnostics reported but not asserted as pre-condition.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: W0-20 truncation FAIL was truncation-attributable; the Mellin-cone apex at s=3 is structurally well-defined under analytic continuation. Closes the second of the 3 W0-W5 Mellin-strip cluster FAILs (alongside W0-11 in §W3-3; W0-7 in §W3-2 has a distinct PASS criterion). Strengthens W6-5 (closeout §1.1) "Mellin-cone apex universal s=3 deviation 0" theorem PASS by extending its scope from W6-5's own L_max range to L_max=10.
- **FAIL**: W0-20 FAIL is structural; the Mellin-cone apex at s=3 is not analytically accessible via C10's `analytic_zeta` API. This would be a serious blow to the C10 infrastructure's universality claim and would require S87+ reformulation of the d_spec=8 NCG analytic-continuation framework. The bulletin partition recount would shift W0-20 from Truncation=6 to a kernel-structural-FAIL bulletin.
- **INFO**: apex finite but cross-check loose; partial closure; the MB-continued and direct-subtraction values diverge at the 5 < χ²/dof ≤ 10 level. Diagnostic for refinement of either the MB contour choice or the direct subtraction's truncation order.

**12. Effort estimate**: 1.5h LOW. Single off-pole evaluation + direct-subtraction cross-check; consumes C10 infrastructure.

**13. Substrate-framing reminder**: state as: **"The substrate's Mellin-cone spectral structure reveals — at the s=3 apex in d_spec=8 NCG — whether the analytic continuation of ζ_D admits a finite, cross-check-consistent off-pole value, completing the W0-20 truncation FAIL closure path."** The substrate is logically prior; the Mellin-cone is the substrate's analytic-continuation geometry; the s=3 apex is the universal point shared with W6-5's PASS theorem.

---

## §W3-5. S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION (C13)

**1. Gate ID**: `S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION`

**2. Trigger**: `[VERIFY]` — quantitative test of the cluster-span identity `b_pow(span_2) = 2 · b_pow(span_3)` at machine precision, extended from W0-3's single-K validation (closeout §1.1: W0-3 / W1a-3 CC-5 cluster-span identity 2.000…002) across the full K-corridor (K ∈ [K_R5, K_crit]) at L_max=10, and sheet-by-sheet on the post-fold Riemann cover (K ∈ [K_crit, K_FIRAS]).

**3. Classification**: GEOMETRIC — cluster-span identity is a structural CC-5 property of the substrate's spectral-cluster decomposition; K is the substrate-distance parameter (per W0a R5 K-disambiguation: K_corridor / K_R5 / K_crit / K_FIRAS); the Riemann cover is a substrate-topological structure post-fold.

**4. Agent type**: `connes-ncg-theorist` — CC-5 cluster-span identity is a Connes-Chamseddine-Marcolli (CCM) module construction; the cluster decomposition operates on the spectral triple and its NCG K-cycle structure, which is core Connes-track competence. **Rationale for not assigning lizzi**: while Lizzi co-owns W3 wave, C13 is a cluster-span identity test (CCM-2007 §3 provenance), not a regulator-functional test; the appropriate specialist is `connes-ncg-theorist`. Fallback: `lizzi-spectral-functional-theorist` if Connes unavailable (Lizzi authored related cluster-span work in S78-S80 atlas extensions; competent secondary). **Rationale for not assigning gen-physicist**: specialist authorship per partition §5 note 4.

**5. Hypothesis**: The cluster-span identity `b_pow(span_2) = 2 · b_pow(span_3)` holds at machine-epsilon precision (relative deviation ≤ 1e-12) at every K in the corridor scan (K ∈ [K_R5, K_crit] under L_max=10) AND on every sheet of the post-fold Riemann cover (K ∈ [K_crit, K_FIRAS]); deviation > 1e-12 at any K or any sheet refutes the K-corridor extension claim.

**6. Method** (complete dispatch prompt):

```
Run `computations/s86_w3_cluster_span_k_corridor_extension.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"`:

- `from canonical_constants import *`  # imports K_R5, K_crit, K_FIRAS,
                                       # K_crit_BdG (W0c C17 pin), K_floor,
                                       # K_wall (W0c C19 pin)
- Input pin: SHA-256 of `_cluster_span_extract.py` (W2 C12 PASS-pinned
  reusable module)
- Input pin: SHA-256 of W0c C17 canonical_constants update (K_crit_BdG = 2.035
  registered distinct from K_crit = 91.5)
- Input pin: SHA-256 of W0c C19 K_floor + K_wall + W5 D.4 registry block
- Self-test reproduce: call `_cluster_span_extract.py` at single-K W0-3 reference
  point; verify reproduces W0-3 PASS value 2.000…002 (sanity check on C12 module)

- Pre-fold corridor scan: K ∈ [K_R5, K_crit] at L_max=10
    n_scan = 41 K-values, log-spaced
    For each K_i:
        Compute b_pow(span_2; K_i, L_max=10)
        Compute b_pow(span_3; K_i, L_max=10)
        Compute identity_LHS = b_pow(span_2)
        Compute identity_RHS = 2 · b_pow(span_3)
        Compute deviation_i = |identity_LHS - identity_RHS| / max(|identity_LHS|, 1e-300)
    PASS_pre_fold = max_i(deviation_i) ≤ 1e-12

- Post-fold Riemann cover sheet-by-sheet: K ∈ [K_crit, K_FIRAS]
    For each sheet ∈ {sheet_1, sheet_2, sheet_3}:
        n_scan = 21 K-values, log-spaced on the sheet
        Repeat per-K identity test as above; report max_sheet_deviation
    PASS_post_fold = max over all sheets of max_sheet_deviation ≤ 1e-12

- Aggregate PASS: PASS_pre_fold AND PASS_post_fold

GPU: `torch.linalg` for D_K eigvals at L_max=10 (per K); CPU fallback OMP=8.
Per K, the eigenvalue problem is at L_max=10 D_K block — well above 100×100;
GPU mandatory for throughput.

Outputs:
- `s86_w3_cluster_span_k_corridor_extension.npz` (per-K identity LHS/RHS/deviation,
  per-sheet diagnostics, max_deviation across all K and sheets)
- `s86_w3_cluster_span_k_corridor_extension.png` (deviation vs K log-log plot,
  per-sheet annotated)
- `s86_w3_cluster_span_k_corridor_extension.json` (verdict 4-tuple + max_deviation
  + sheet-wise breakdown)

Verdict line:
S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION|<VERDICT>|<value=max_deviation>|
  scheme=NCG-CCM-cluster-span|convention=K-corridor+Riemann-cover-sheet-by-sheet|
  L_max=10|content_sha256:<64-hex>|audit_sha256:<64-hex>
```

**7. Machinery pin (PRDR)**:
- `L_max`: 10 (canonical for full corridor)
- `scheme`: `NCG-CCM-cluster-span` (Connes-Chamseddine-Marcolli cluster decomposition)
- `convention`: `K-corridor+Riemann-cover-sheet-by-sheet` (pre-fold corridor + post-fold cover)
- `n_eval`: 41 K-values pre-fold + 21 K-values × 3 sheets post-fold = 41 + 63 = 104 evaluations
- `scan_range`: pre-fold K ∈ [K_R5, K_crit]; post-fold K ∈ [K_crit, K_FIRAS]
- `step_size`: log-spaced (Δlog(K) determined by n_scan and corridor endpoints)
- `tolerance`: identity deviation ≤ 1e-12 (machine-epsilon-class structural threshold; matches W0-3's 2.000…002 precision)
- `random_seed`: N/A
- `GPU path`: `torch.linalg` (ROCm 7.2)
- `cutoff_axis`: `coherence` (K is a coherence-class corridor parameter per W0a R3 YAML pin; K_crit is the coherence-fold transition)
- `regulator_pin_tag`: `b_pow^{NCG-CCM}` for cluster-span citations
- `K-disambiguation`: per W0a R5; K_R5, K_crit, K_FIRAS are explicit canonical-constants entries; bare "K" is forbidden; K_crit_BdG = 2.035 is distinct from K_crit = 91.5 and is NOT used in this gate (BdG-corridor is W2-12; this gate is the inflationary K-corridor)
- `Riemann-cover sheets`: 3 sheets enumerated; sheet ID is part of per-K output diagnostic

**8. Expected output 4-tuple**:
`(value=<max_deviation across all K and sheets>, scheme=NCG-CCM-cluster-span, convention=K-corridor+Riemann-cover-sheet-by-sheet, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: max_deviation ≤ 1e-12 across all 104 (K, sheet) evaluations
- **FAIL**: max_deviation > 1e-6 at any (K, sheet) — identity collapses outside W0-3's single-K point
- **INFO**: max_deviation ∈ (1e-12, 1e-6] — identity holds approximately but loses machine-epsilon precision at corridor edges; structural-stability claim qualified
- **Tolerance rule**: THEOREM (CC-5 cluster-span identity is a structural-theorem-class property; deviation ≤ 1e-12 is the machine-epsilon test; 1e-6 is the structural-collapse threshold)

**10. Substitution chain** (cluster-span identity in C13):
```
Step 1 (definitions):
  span_2(K)         = 2-cluster spectral span at corridor parameter K, L_max=10
                      (per CCM-2007 §3 cluster decomposition)
  span_3(K)         = 3-cluster spectral span at K, L_max=10
  b_pow(span_n; K)  = bag power of n-cluster span at K (extracted via C12
                      `_cluster_span_extract.py` module, refactored from
                      W0-3 ad-hoc code)
  identity_LHS(K)   = b_pow(span_2; K, L_max=10)
  identity_RHS(K)   = 2 · b_pow(span_3; K, L_max=10)
  deviation(K)      = |identity_LHS - identity_RHS| / max(|identity_LHS|, 1e-300)
  W0-3 reference    = single-K validation at K = K_R5 with deviation = 2e-15
                      (PASS at machine-epsilon)

Step 2 (substitute PASS test):
  PASS_C13 = max over (K, sheet) of deviation(K, sheet) ≤ 1e-12

Step 3 (simplify; per-(K, sheet) bound):
  PASS_C13 ⇔ ∀ K ∈ [K_R5, K_crit] at L_max=10
              AND ∀ sheet ∈ {1,2,3} on Riemann cover [K_crit, K_FIRAS]:
              |b_pow(span_2; K, sheet) - 2 · b_pow(span_3; K, sheet)|
              / max(|b_pow(span_2)|, 1e-300) ≤ 1e-12

Step 4 (direction from canonical form):
  IF max_deviation ≤ 1e-12  THEN cluster-span identity HOLDS structurally
                                 across the full K-corridor + Riemann cover;
                                 W0-3's single-K PASS extends to a corridor
                                 PASS — a stronger structural claim
  IF 1e-12 < max ≤ 1e-6      THEN identity holds approximately; INFO band;
                                 corridor-extension claim qualified
  IF max > 1e-6              THEN identity collapses at some K or sheet;
                                 W0-3 was a fortuitous single-point match,
                                 NOT a corridor-wide structural property

Conclusion: PASS direction is "max deviation at machine-epsilon AT EVERY
(K, sheet)". Test does not assume direction of deviation, only its magnitude
relative to the structural threshold. The factor "2" in identity_RHS is a
combinatorial-CCM property (2-cluster vs 3-cluster span ratio), not a
fitted coefficient.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: CC-5 cluster-span identity extends from W0-3's single-K validation to a corridor-wide + Riemann-cover-wide structural property of the substrate's CCM cluster decomposition. The identity becomes a permanent §VII registry entry (sister to the original W0-3 entry, with explicit corridor-scope annotation). Strengthens the §VII.K-CC-5 family. Stress-tests the C12 reusable module across 104 evaluations.
- **FAIL**: cluster-span identity is K-fragile — W0-3's PASS was a single-point fluke or a corridor-edge property that does not extend. Closes the corridor-extension corridor (paradoxically) and demotes the W0-3 entry from "structural identity" to "single-K observation." Significant constraint-map content: a CC-5 identity that does NOT extend across the K-corridor is a sharper substrate statement than one that does extend.
- **INFO**: identity holds approximately (1e-12 < max ≤ 1e-6); corridor-extension claim is qualified by "approximate, not machine-epsilon." Documents a structural-floor approximation but not a registry-grade theorem extension.

**12. Effort estimate**: 2h LOW (per partition §1 W3 + closeout §3.6 C13). Self-test on C12 module + 104 evaluations + per-sheet aggregation; the heavy lifting is the C12 module build (in W2), not the corridor scan (in W3).

**13. Substrate-framing reminder**: state as: **"The substrate's CCM cluster decomposition reveals — across the full K-corridor at L_max=10 and on every sheet of the post-fold Riemann cover — whether the b_pow(span_2) = 2·b_pow(span_3) identity is a corridor-wide structural property or a single-K fortuitous match."** The substrate is logically prior; the K-corridor is a substrate-distance parameterization; the Riemann cover is the substrate's post-fold topological structure; the cluster-span identity is a CC-5 substrate-spectral-content property.

---

## §W3-6. S86-W3-11-LAMBDA-CONVENTION-RESOLUTION (C43)

**1. Gate ID**: `S86-W3-11-LAMBDA-CONVENTION-RESOLUTION`

**2. Trigger**: `[VERIFY]` — quantitative re-run of S85's W3-11 gate with the Λ-convention switched from `Casimir-saturated` (S85 W3-11 default) and the `c_fabric · M_KK` ad hoc choice to the empirical Λ_actual = λ_max(L=10) extracted from the D_K spectral cache (provided by W0c C14, with reference value `lambda_max = 5.42 M_KK at L=12` from the W0-7 series per closeout §3.6 C43); coexistence test of W3-9 (Ginzburg-Oz validity, S85 PASS at Gi=5.50e-10 per closeout §1.1) AND W3-11 under the empirical Λ.

**3. Classification**: GEOMETRIC — Λ_actual is the substrate's actual top eigenvalue, a structural property of D_K; W3-11 is a substrate-cutoff observable; W3-9 (Ginzburg-Oz validity) is a substrate-coherence-length observable. The W3-9 vs W3-11 coexistence question is a GEOMETRIC consistency test on the substrate's spectral-content / coherence-length pair, not a particle observable.

**4. Agent type**: `lizzi-spectral-functional-theorist` — Lizzi is the Λ-convention authority per closeout §3.6 C43 source (lizzi S-7 §V.13) AND per the agent's defined role on regulator-functional questions ("the cosmological constant... is determined by the regularization scheme as much as by the Dirac operator spectrum"). The W3-11 vs W3-9 coexistence question is a regulator-functional sensitivity question (does the Λ-convention switch break Ginzburg-Oz validity?), squarely in Lizzi's competence. **Rationale for not assigning gen-physicist**: per partition §5 note 4. Fallback: `connes-ncg-theorist` (Λ-convention is also an NCG axiomatic question per S83 W1-G3 EN3 theorem; Connes is competent secondary).

**5. Hypothesis**: Re-running S85's W3-11 with Λ_actual = λ_max(L=10) replacing both Casimir-saturated and `c_fabric · M_KK` produces a W3-11 verdict that (a) lands within 30% of the S85 W3-11 value under at least one of the two ad hoc conventions OR (b) is structurally distinct in a way that explicitly disambiguates the convention; AND W3-9's Ginzburg-Oz validity (Gi=5.50e-10 PASS) is preserved (Gi-deviation under Λ_actual ≤ 50% relative to S85 W3-9 value) — the coexistence test confirms the empirical Λ-convention is admissible with both gates.

**6. Method** (complete dispatch prompt):

```
Run `computations/s86_w3_lambda_convention_resolution.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"`:

- `from canonical_constants import *`
  # imports M_KK, c_fabric, and Λ_top once W0c C14 lands
- Input pin: SHA-256 of W0c C14 output (`s86_w0c_lambda_top_direct_extraction.json`
  or canonical_constants.py update SHA after C14 PASS — the empirical Λ_top to
  6 sig figs with provenance)
- Input pin: SHA-256 of S85 W3-11 producing-script (recoverable from
  s85_gate_verdicts.txt W3-11 line)
- Input pin: SHA-256 of S85 W3-9 producing-script
- Input pin: SHA-256 of D_K spectral cache at L_max=10 (reference for
  λ_max extraction; cited as `<computed-at-runtime>`)

- Step A: load Λ_actual from canonical_constants (post-C14) — should match the
  W0-7 series reference 5.42 M_KK at L=12 per closeout §3.6 C43 within 6 sig figs
  at L_max=10 cache, OR document the L_max=10 vs L_max=12 difference as
  diagnostic. (NOTE: 5.42 is the L=12 reference; the L=10 actual may differ
  slightly; W0c C14 PASSes at L=10 6-sig-fig precision, that is what we use.)

- Step B: re-run S85 W3-11 with Λ_substrate ← Λ_actual replacing both
  Casimir-saturated and c_fabric*M_KK conventions
    Compute W3_11_value_actual
    Compute deviation_from_Casimir = |W3_11_value_actual - W3_11_value_Casimir| / |W3_11_value_Casimir|
    Compute deviation_from_cfabric = |W3_11_value_actual - W3_11_value_cfabric| / |W3_11_value_cfabric|
    PASS_W3_11_a (recovery): min(deviation_from_Casimir, deviation_from_cfabric) ≤ 0.30
    PASS_W3_11_b (disambiguation): both deviations > 0.30 AND the structural
                                    direction is documented (which convention
                                    is closer; sign of deviation; substrate
                                    framing of why)

- Step C: re-run S85 W3-9 with Λ_substrate ← Λ_actual
    Compute Gi_actual; compare to S85 Gi = 5.50e-10
    Compute |Gi_actual - 5.50e-10| / 5.50e-10
    PASS_W3_9_preserved: relative deviation ≤ 0.50

- Aggregate gate verdict:
    PASS = (PASS_W3_11_a OR PASS_W3_11_b) AND PASS_W3_9_preserved
    INFO = PASS_W3_11_a OR PASS_W3_11_b, but Gi-deviation ∈ (0.50, 1.0]
    FAIL = neither PASS_W3_11_a nor PASS_W3_11_b OR Gi-deviation > 1.0

GPU: `torch.linalg` for any D_K spectral re-evaluation; CPU fallback OMP=8.

Outputs:
- `s86_w3_lambda_convention_resolution.npz` (Λ_actual, W3-11 values under all
  three conventions, W3-9 Gi values, deviations, sub-test outcomes)
- `s86_w3_lambda_convention_resolution.png` (W3-11 + W3-9 values vs Λ-convention
  bar plot)
- `s86_w3_lambda_convention_resolution.json` (verdict 4-tuple + sub-test outcomes
  + diagnostic for coexistence test)

Verdict line:
S86-W3-11-LAMBDA-CONVENTION-RESOLUTION|<VERDICT>|<value=Λ_actual at L=10>|
  scheme=Λ_actual_empirical|convention=lambda_max_DK_cache|L_max=10|
  content_sha256:<64-hex>|audit_sha256:<64-hex>
```

**7. Machinery pin (PRDR)**:
- `L_max`: 10 (canonical for D_K cache; Λ_actual is λ_max(L=10) per W0c C14)
- `scheme`: `Λ_actual_empirical` (the empirical top-eigenvalue convention; explicitly distinct from `Casimir-saturated` and `c_fabric_x_M_KK`)
- `convention`: `lambda_max_DK_cache` (extracted directly from D_K spectral cache, NOT from Casimir saturation, NOT from c_fabric ad hoc product per W0a R4 canonical-phrasing audit)
- `n_eval`: 1 evaluation of W3-11 at Λ_actual + 1 evaluation of W3-9 at Λ_actual = 2 substrate-spectral evaluations + 2 reference-comparison evaluations (S85 W3-11 + W3-9 reference values from s85_gate_verdicts.txt) = 4 total
- `scan_range`: N/A (no Λ-scan; the gate fixes Λ at the empirical Λ_actual and re-runs both W3-11 and W3-9)
- `step_size`: N/A
- `tolerance`: PASS_W3_11 deviation thresholds 0.30 (recovery) or > 0.30 with disambiguation (b); PASS_W3_9 Gi-deviation ≤ 0.50; FAIL if Gi-deviation > 1.0
- `random_seed`: N/A
- `GPU path`: `torch.linalg`
- `cutoff_axis`: `spectral` (Λ is a spectral cutoff; per W0a R3 YAML pin)
- `c_fabric pinning`: per W0a R4 — c_fabric is documented as "substrate sound speed (velocity scale, NOT a momentum cutoff)"; the c_fabric · M_KK product is one of the rejected ad hoc Λ-conventions; Λ_actual replaces it

**8. Expected output 4-tuple**:
`(value=<Λ_actual at L=10>, scheme=Λ_actual_empirical, convention=lambda_max_DK_cache, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: (PASS_W3_11_a OR PASS_W3_11_b) AND PASS_W3_9_preserved — i.e., either Λ_actual recovers the S85 W3-11 value within 30% under at least one ad hoc convention, OR it disambiguates with documented structural reason; AND Ginzburg-Oz validity holds with relative Gi-deviation ≤ 50%
- **INFO**: W3-11 sub-test PASSes but Gi-deviation ∈ (0.50, 1.0] — coexistence is partial; the empirical Λ-convention is admissible for W3-11 but stresses W3-9
- **FAIL**: W3-11 sub-test fails (neither recovery nor disambiguation succeeds) OR Gi-deviation > 1.0 — empirical Λ-convention is INCONSISTENT with at least one of W3-11 or W3-9; the convention dispute is not resolved by Λ_actual
- **Tolerance rule**: RATIO (all sub-test thresholds are dimensionless relative deviations)

**10. Substitution chain** (Λ_actual vs Casimir-saturated direction):
```
Step 1 (definitions):
  Λ_actual            = λ_max(L_max=10) from D_K spectral cache (W0c C14 output;
                        empirical top eigenvalue; closeout §3.6 C43 reference
                        5.42 M_KK at L=12 — L=10 value pinned by C14)
  Λ_Casimir           = Casimir-saturated cutoff (S85 W3-11 default; structurally
                        derived from group-theoretic Casimir invariant of
                        Jensen-deformed SU(3))
  Λ_cfabric           = c_fabric · M_KK (S85 W3-11 ad hoc alternative; rejected
                        per W0a R4 canonical-phrasing audit because c_fabric is
                        a velocity scale not a momentum cutoff)
  W3_11_value(Λ)      = S85 W3-11 gate output as function of substrate Λ
  W3_9_Gi(Λ)          = S85 W3-9 Ginzburg-Oz Gi parameter as function of Λ

Step 2 (substitute the PASS sub-tests):
  PASS_W3_11_a = (min(|W3_11(Λ_actual) - W3_11(Λ_Casimir)| / |W3_11(Λ_Casimir)|,
                      |W3_11(Λ_actual) - W3_11(Λ_cfabric)| / |W3_11(Λ_cfabric)|)
                  ≤ 0.30)
  PASS_W3_9_preserved = (|W3_9_Gi(Λ_actual) - 5.50e-10| / 5.50e-10 ≤ 0.50)

Step 3 (simplify; logical conjunction):
  PASS_C43 = (PASS_W3_11_a OR PASS_W3_11_b) AND PASS_W3_9_preserved

Step 4 (direction from canonical form):
  IF Λ_actual recovers W3-11 within 30% of either ad hoc convention
     AND Gi-deviation ≤ 50%
                                    THEN empirical Λ-convention is ADMISSIBLE
                                         and DISAMBIGUATING; resolves the
                                         W3-11 Λ-convention dispute in favor
                                         of empirical Λ_actual
  IF Λ_actual fails W3-11 recovery
     AND no documented disambiguation
                                    THEN empirical Λ_actual is INCONSISTENT
                                         with W3-11 expectations under both
                                         ad hoc conventions; the dispute is
                                         not resolved; FAIL
  IF W3-9 Gi-deviation > 50%        THEN Ginzburg-Oz validity is broken under
                                         empirical Λ; coexistence FAILS

Conclusion: PASS direction is "empirical Λ_actual is admissible AND coexists
with W3-9". The test does not assume direction of deviation between Λ_actual
and either ad hoc convention; both directions are admissible if explicitly
documented (PASS_W3_11_b disambiguation branch). The 30% and 50% thresholds
are per closeout §3.6 C43 LOW-effort spec; they are recovery / preservation
bounds, not sign claims.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: empirical Λ_actual is the canonical W3-11 Λ-convention going forward; replaces both Casimir-saturated and `c_fabric · M_KK` ad hoc choices in S86+ scripts. W3-9 + W3-11 coexist under empirical Λ — a substrate-spectral-content + substrate-coherence-length consistency. Strengthens W0a R4 canonical-phrasing audit (c_fabric is properly a velocity, not a Λ). Closes the lizzi S-7 §V.13 carry-forward.
- **FAIL**: empirical Λ_actual is INCONSISTENT with W3-11 OR breaks W3-9; the convention dispute is unresolved by Λ_actual. Either (a) S85 W3-11's PASS was an artifact of the ad hoc Λ-convention (a sharp substrate-content statement), OR (b) Λ_actual extraction at L=10 is incomplete (L=12 reference 5.42 M_KK may not be the L=10 value; W0c C14 should re-validate). Constrains future Λ-convention work to either accept the ad hoc convention as canonical or to investigate the L_max-dependence of Λ_actual.
- **INFO**: partial coexistence; W3-11 admissible under empirical Λ but W3-9's Gi-deviation falls in (50%, 100%]. Documents that empirical Λ is admissible for the cutoff-class observable but stresses the Ginzburg-Oz coherence-length observable. S87+ would refine either the W3-9 calculation or the Λ-convention interpretation.

**12. Effort estimate**: 2-3h LOW (per partition §1 W3 + closeout §3.6 C43). Re-run + comparison; the heavy work was the W0c C14 Λ_top extraction.

**13. Substrate-framing reminder**: state as: **"The substrate's empirical top eigenvalue Λ_actual = λ_max(L=10) reveals — when substituted for both the Casimir-saturated and c_fabric·M_KK ad hoc Λ-conventions — whether the substrate's W3-11 cutoff observable and W3-9 Ginzburg-Oz coherence-length observable coexist consistently under the substrate's actual spectral content."** The substrate is logically prior; Λ is the substrate's spectral cutoff (specifically λ_max of D_K, the substrate's actual top eigenvalue); the convention dispute is a question about which mathematical proxy for Λ best matches the substrate, NOT a question about the substrate's intrinsic content. Per W0a R4: c_fabric is a velocity scale (substrate sound speed), NEVER labeled "Λ" without explicit Layer-B qualification.

---

## §X. Wave W3 → Downstream Decision Point

W3 outcomes drive the following S86 + S87 downstream consequences:

| W3 Gate Outcome | Downstream Consequence (S86) | Downstream Consequence (S87+) |
|:----------------|:------------------------------|:------------------------------|
| T9 PASS | ζ-stabilization REPLACEMENT-A + REPLACEMENT-B lands as combined permanent §VII registry entry; cited by W1a (T1, T5) registry landings as supporting structural evidence | None pending; theorem complete |
| T9 FAIL | REPLACEMENT-B is structurally vacuous; only REPLACEMENT-A (windowed kinematic, PROVEN at L ∈ {5,6,7,8}) is canonical; lizzi 9A §A-2 conjecture refuted | S87 reformulation of asymptotic ansatz OR retraction of the asymptotic claim |
| T9 INFO | Theorem provisionally landed with monotonicity-qualifier annotation | S87 refinement of Richardson extrapolation or higher-order ansatz |
| T9 PRE-REG-INC | C9 OR C10 FAILed in W2 — REPLACEMENT-B not testable; T9 deferred to S87 | S87 re-attempt after W2 prerequisites land |
| W0-7 MB-RE PASS | W0-7 truncation FAIL closure; F_4 / M regulator-class taxonomy strengthened (Jensen-Zubarev confirmed in F_4) | None |
| W0-7 MB-RE FAIL | W0-7 FAIL is structural-from-kernel; lizzi S-1 Regulator-Family Boundary Theorem requires re-examination of Jensen-Zubarev's F_4 membership | S87 meta-question on F_4 family criteria |
| W0-11 MB-RE PASS | Closes 1 of 6 W0-W5 truncation FAILs; bulletin-partition recount Truncation 6→5 | None |
| W0-11 MB-RE FAIL | W0-11 corridor closure upgraded from truncation-attributable to kernel-structural; bulletin partition recount adds structural-FAIL bulletin | None |
| W0-20 MB-RE PASS | Closes 1 of 6 W0-W5 truncation FAILs; combined with W0-11 PASS, brings count from 6→4; strengthens W6-5 Mellin-cone apex theorem scope | None |
| W0-20 MB-RE FAIL | C10 universality claim weakened; serious structural concern requiring S87+ d_spec=8 NCG analytic-continuation framework refinement | S87 d_spec=8 NCG framework refinement |
| C13 PASS | CC-5 cluster-span identity extends to corridor-wide + Riemann-cover-wide structural property; new permanent §VII registry entry (corridor-extension sister to W0-3) | None |
| C13 FAIL | CC-5 identity is K-fragile; W0-3 single-K PASS demoted to single-K observation; constraint-map content gain (sharper substrate statement) | S87 investigation of which K-substructure breaks the identity |
| C43 PASS | Empirical Λ_actual = λ_max(L=10) becomes canonical W3-11 Λ-convention; S86+ scripts adopt; closes lizzi S-7 §V.13 | None |
| C43 FAIL | Empirical Λ_actual inconsistent with W3-11 or breaks W3-9; convention dispute unresolved | S87 either reaffirm ad hoc Λ or refine Λ_actual extraction at higher L_max |
| C43 INFO | Partial coexistence; W3-11 admissible but W3-9 stressed | S87 refine W3-9 or interpret stress as physical |

**Cross-wave interactions**:
- T9 PASS feeds W1a T5 (Mellin Strip / Convergence Cone Theorem registry landing as Lizzi-track sibling alongside ZETA-NOT-PHYSICAL-75 — strengthens the Lizzi-track registry-grade theorem cluster).
- W0-11 + W0-20 MB-RE PASS would collapse the 28-FAIL W0-W5 bulletin partition (Truncation=6, …) toward Truncation=4 — affecting BULLETIN-W0W5-FAIL-PARTITION in W1c (which assumes Truncation=6 at S85-close; S86 W3 outcomes would update this).
- C13 PASS extends W0-3 (a W1a T1 mechanical-write target) — the registry write in W1a would need to cite C13 corridor-extension scope OR await S87 re-write.
- C43 PASS interacts with W4 C28 (cutoff_sqrt adjudication): Λ-convention resolution under empirical Λ_actual partially disambiguates the cutoff_axis YAML pin (W0a R3) usage downstream.

---

## §0.10. Wave W3 Machinery-Enumeration Pin (PRDR)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness — every gate-relevant machinery parameter is enumerated and pinned (or declared diagnostic) for each W3 gate. Aggregated table:

| Gate | L_max | scheme | convention | n_eval | scan_range | step_size | tolerance | random_seed | GPU path | cutoff_axis | regulator_pin_tag |
|:-----|:------|:-------|:-----------|:-------|:-----------|:----------|:----------|:------------|:---------|:------------|:-------------------|
| T9 | {7,8,9,10} | zeta | s4_leading_residue_d8 | 8 | L_max ladder fixed | N/A (analytic) | ε_T9 = 0.01 | N/A | torch.linalg / OMP=8 | spectral | a_4^{ζ} |
| W0-7 MB-RE | 10 | Jensen-Zubarev | Mellin-Barnes-continued | 21 (s ∈ [2.5, 4.5]) | s ∈ [2.5, 4.5] | Δs=0.1 | ρ ∈ [−1.05, −0.95]; σ_ρ < 0.025 (FAIL); σ_ρ ≥ 0.025 (INFO) | N/A | torch.linalg / OMP=8 | coherence | M[K_JZ]^{Jensen-Zubarev,MB-continued} |
| W0-11 MB-RE | 10 | heat-kernel | Mellin-Barnes-with-SD-subtraction | 1 + 11 = 12 | MB pole window per C9 | Δs=0.05 | ratio thr 1e-1 (PASS), 1e0 (FAIL); χ²/dof thr 5/10 | N/A | torch.linalg / OMP=8 | spectral | a_0^{ζ} |
| W0-20 MB-RE | 10 | zeta | Mellin-cone-s3-off-pole-d8 | 1 + 1 + 5 = 7 | s ∈ [2.95, 3.05] | Δs=0.025 | finite + χ²/dof ≤ 5 (PASS); 5-10 (INFO); >10 (FAIL) | N/A | torch.linalg / OMP=8 | spectral | analytic_zeta^{Mellin-cone-d8} |
| C13 | 10 | NCG-CCM-cluster-span | K-corridor+Riemann-cover-sheet-by-sheet | 41 + 63 = 104 | K ∈ [K_R5, K_crit] pre-fold + [K_crit, K_FIRAS] post-fold per sheet | log-spaced | dev ≤ 1e-12 (PASS); ≤ 1e-6 (INFO); else FAIL | N/A | torch.linalg / OMP=8 | coherence | b_pow^{NCG-CCM} |
| C43 | 10 | Λ_actual_empirical | lambda_max_DK_cache | 4 | N/A (no scan) | N/A | W3-11 dev ≤ 0.30 (recovery) or disambig; W3-9 Gi-dev ≤ 0.50 | N/A | torch.linalg / OMP=8 | spectral | (none — Λ-convention test, not a_n test) |

All 6 gates explicitly pin every PRDR-required machinery parameter; none are left as free runtime degrees of freedom. PRU Class 8 (Pre-Registration Underspecification) is structurally avoided.

---

## §0.11. Wave W3 Input-SHA Ledger

All input SHA-256 pins for W3 gates. Static files have precomputed hashes (deferred to compute-time ledger update); dynamic inputs from W2/W0c PASS verdicts are marked `<computed-at-runtime>`.

| Gate | Input pin | SHA-256 source |
|:-----|:----------|:---------------|
| T9 | W2 C10 output payload | `<computed-at-runtime>` (from s86_gate_verdicts.txt at C10 PASS) |
| T9 | W2 C9 output payload | `<computed-at-runtime>` (from s86_gate_verdicts.txt at C9 PASS) |
| W0-7 MB-RE | S85 W0-7 producing-script | `<computed-at-runtime>` (from s85_gate_verdicts.txt W0-7 audit_sha256) |
| W0-7 MB-RE | W2 C10 output payload | `<computed-at-runtime>` (from s86_gate_verdicts.txt at C10 PASS) |
| W0-7 MB-RE | D_K cache at L_max=10 | `<computed-at-runtime>` (D_K cache provenance from W0c canonical_constants update) |
| W0-11 MB-RE | S85 W0-11 producing-script | `<computed-at-runtime>` (from s85_gate_verdicts.txt W0-11 audit_sha256) |
| W0-11 MB-RE | W2 C9 output payload | `<computed-at-runtime>` (from s86_gate_verdicts.txt at C9 PASS) |
| W0-11 MB-RE | canonical_constants.py a_0^{ζ} pin | `<computed-at-runtime>` (canonical_constants.py SHA after W0c P14 retrofit) |
| W0-20 MB-RE | S85 W0-20 producing-script | `<computed-at-runtime>` (from s85_gate_verdicts.txt W0-20 audit_sha256) |
| W0-20 MB-RE | W2 C10 output payload | `<computed-at-runtime>` (from s86_gate_verdicts.txt at C10 PASS) |
| C13 | W2 C12 reusable module `_cluster_span_extract.py` | `<computed-at-runtime>` (from s86_gate_verdicts.txt at C12 PASS) |
| C13 | W0c C17 canonical_constants update (K_crit_BdG = 2.035) | `<computed-at-runtime>` (canonical_constants.py SHA after C17 PASS) |
| C13 | W0c C19 K_floor + K_wall + W5 D.4 registry block | `<computed-at-runtime>` (registry SHA after C19 PASS) |
| C43 | W0c C14 output (`s86_w0c_lambda_top_direct_extraction.json` or canonical_constants.py update) | `<computed-at-runtime>` (from s86_gate_verdicts.txt at C14 PASS) |
| C43 | S85 W3-11 producing-script | `<computed-at-runtime>` (from s85_gate_verdicts.txt W3-11 audit_sha256) |
| C43 | S85 W3-9 producing-script | `<computed-at-runtime>` (from s85_gate_verdicts.txt W3-9 audit_sha256) |
| C43 | D_K spectral cache at L_max=10 | `<computed-at-runtime>` |

Audit closure SHA per gate is `closure_hash(input_pin_map ∪ machinery_pin_map)` per `.claude/rules/gate-verdicts.md` §6.2; computed inside each producing script and emitted on the verdict line as `audit_sha256:<64-hex>`.

**Substitution chain — input-pin closure for W3**:
```
Step 1 (definition):
  W3_input_pins = union over W3 gates of (input file SHA-256 references)
Step 2 (substitute):
  W3_input_pins = {C9 output, C10 output, C12 module, C14 output, C17 canon, C19 registry,
                   S85 W0-7, S85 W0-11, S85 W0-20, S85 W3-9, S85 W3-11, D_K cache,
                   canonical_constants.py at W0c-PASS state}
Step 3 (simplify):
  W3_input_pins partitions into: (a) W2 outputs {C9, C10, C12} — required-after-W2-PASS;
                                  (b) W0c outputs {C14, C17, C19} — required-after-W0c-PASS;
                                  (c) S85 verdict references {W0-7, W0-11, W0-20, W3-9, W3-11}
                                      — historically pinned at S85 close;
                                  (d) D_K spectral cache + canonical_constants.py — provenance
                                      pinned at compute time
Step 4 (direction):
  Conclusion: W3 has 6 dynamic input pins (a + b) all marked <computed-at-runtime>;
  5 historical input pins (c) recoverable from s85_gate_verdicts.txt; 2 cache/canon pins
  (d) recoverable from W0c-PASS canonical_constants.py state. Total 13 input pins, 0
  unspecified — PRU-clean for the Wave W3 input ledger.
```

---

**End of Wave W3 plan.** Per partition §5 dispatch note 5: this plan file MUST run through `computations/_plan_upstream_pin_validator.py --json` before Phase 4 dispatch. Per partition §5 note 4: the lizzi-spectral-functional-theorist owner is mandatory for T9 + C43 (originator-track); spectral-geometer / connes-ncg-theorist are explicitly named as fallback / alternative specialists for the W0-X re-emissions and C13 respectively, never gen-physicist.
