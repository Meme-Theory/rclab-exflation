# Session 86 Plan — Wave W5b: Gauge selection + BASELINE forward integration + c_sub admissibility

**Owner**: `gen-physicist` (planner-of-record; runtime agents are SPECIALISTS — see per-gate Agent fields)
**Output of this plan**: `sessions/session-plan/session-86-plan-w5b.md` (this file)
**Sourced from**: gen-physicist S-7 §V.7 (C15 — gauge + baseline forward integration) + §V.8 (C16 — c_sub admissibility)
**Items planned**: 2 (C15, C16)
**Sequencing posture**: parallel to W5a (P3 SR-flow Z-factor); NOT a hard prerequisite of W5a but feeds W5a P3 pivot-pin (via C15(i) gauge selection rule) and feeds late-S86 W13 P2 r-Both-Pathways admissibility (via C16 c_sub classification).

---

## §0. Wave W5b Summary

Wave W5b supplements W5a's SECTOR-1 SR-LO ODE integration with two adjacencies the substrate-first pipeline cannot leave open before late-S86:

1. **C15 — GAUGE selection + BASELINE forward integration** (2 sub-gates):
   - **C15(i) GAUGE**: choose a canonical N-fold counter between (a) **substrate-native zeta** N = 3.12 e-folds (substrate's own Mellin-zeta-anchored fold count) and (b) **gauge-invariant Mukhanov-Sasaki (MS)** N = 55 e-folds (the comoving-mode-leaves-horizon convention). The selection rule is axiom-native vs observation-native; recommendation: pre-register BOTH at each pivot and report both columns until a W-2 workshop or explicit S86 verdict commits to one.
   - **C15(ii) BASELINE forward integration**: solve `dH/dN = −eps_H · H` from the substrate IC at `N_initial = N_pivot + 55 e-folds`, integrate forward to `N_pivot`, output `H(N_pivot)`. This is the BASELINE column SECTOR-1 needs for comparison to W5a P3 trajectory.

2. **C16 — PRDR-PIN-CSUB**: classify `c_sub = 3.647` as **ADMISSIBLE** or **EXCLUDED** through three pre-registered sub-tests:
   - **(a)** UV-cut + Mellin-convention + L_max combination that produces 3.647 must be a member of the canonical-constants regulator atlas (cite source);
   - **(b)** tau-stationarity per S83 W2-G12: `|d(c_sub)/dτ| / |c_sub|` (max_slope) must be < 0.1 in the neighborhood of the τ_fold-anchored evaluation point;
   - **(c)** conformal-anomaly consistency with S79 P1-2 W2-E sign-reversal rule.

Both gates are **PHONONIC** by classification: substrate-dynamics ODE (C15(ii)) + substrate-Mellin-cone admissibility (C16). Neither involves geometric-only structure or particle-content selection.

---

## §0.5. Wave W5b Decision-Point Prerequisites

W5b is **parallel** to W5a (the heavy SECTOR-1 ODE wave) but feeds two downstream decision points:

- **C15(i) → W5a P3 pivot-pin choice**: if W5a P3 reports SECTOR-1 results at both N=3.12 (substrate-zeta) and N=55 (MS) pivots and the user/orchestrator picks the canonical pivot at S86 close, C15(i)'s selection rule and substitution chain document why one is canonical. If C15(i) reports "DEFER to W-2 workshop", W5a P3 records both pivots and S86 closes with a `pivot_canonical_undecided` flag (legitimate INFO outcome).
- **C15(ii) → W5a P3 cross-check**: BASELINE H(N_pivot) is the no-running, free-streaming H trajectory. W5a P3's full SR-flow result must reduce to the BASELINE in the limit `(η, α_s, ξ²) → 0` at the same eps_H input. C15(ii) provides the comparison anchor.
- **C16 → late-S86 W13 P2 r-Both-Pathways admissibility**: P2 promotes r to falsifier-master-inventory under Path-H (r=0.00745) AND Path-C (r=0.0117). If C16 returns `c_sub = 3.647 EXCLUDED`, Path-C is structurally inadmissible and P2 reduces to Path-H-only (the 36.5% split flag in P2's spec absorbs this contingency). If `ADMISSIBLE`, P2 lands the dual registration as planned. If `INFO` (2 of 3 sub-tests pass), P2 lands the dual registration with an explicit `c_sub_admissibility = INFO` annotation.

Neither sequencing constraint is a HARD blocker for W5a or W13 — both downstream waves can run concurrently with W5b and ingest C15/C16 verdicts at their own consolidation points.

---

## §I. Carry-Forward Items Mapping

| §3 ID | This-wave gate | Source (closeout / synthesis) | Pre-S86 status | S86-W5b verdict path |
|:------|:--------------|:------------------------------|:---------------|:--------------------|
| C15 | §W5b-1 (sub-blocks (i) GAUGE + (ii) BASELINE) | gen-physicist S-7 §V.7 | OPEN (substrate-native pivot vs MS pivot disagreement noted in W0-A-i / W0-A-ii blocks of S85 plan) | `computations/s86_gate_verdicts.txt`: `S86-W5B-C15-i-GAUGE: PASS|FAIL -- ...` AND `S86-W5B-C15-ii-BASELINE: PASS|FAIL -- ...` |
| C16 | §W5b-2 | gen-physicist S-7 §V.8 | OPEN (c_sub = 3.647 used in Path-C r=0.0117 prediction without PRDR-compliant admissibility check) | `computations/s86_gate_verdicts.txt`: `S86-W5B-C16-CSUB-ADMISSIBILITY: PASS|FAIL|INFO -- ...` |

---

## §W5b-1. S86-W0-A-i / W0-A-ii — GAUGE + BASELINE FORWARD INTEGRATION (C15)

C15 is split into two independently-verdictable sub-blocks, **C15(i) GAUGE** and **C15(ii) BASELINE**, each with its own gate ID, trigger, threshold, and verdict line.

---

### §W5b-1.i — C15(i) GAUGE (substrate-native zeta vs gauge-invariant MS)

**1. Gate ID**: `S86-W5B-C15-i-GAUGE`

**2. Trigger**: `[AUDIT]`
- Rationale: C15(i) is a selection between two pre-existing conventions (substrate-native zeta N=3.12 vs gauge-invariant MS N=55), each with documented rationale. The gate audits whether the project commits to one as canonical OR pre-registers both at every pivot through S86 close. This is a methodology-discipline audit, not a numerical [VERIFY] gate.

**3. Classification**: **PHONONIC** (substrate's gauge-canonical structure for the spectral-zeta-anchored fold counter; the 3.12 figure derives from the substrate-native Mellin-zeta evaluation, the 55 figure derives from the gauge-invariant MS comoving-mode horizon-exit count — both are substrate properties under different gauges, not external observational impositions).

**4. Agent type** (runtime, not planner): `connes-ncg-theorist`
- Rationale: gauge selection on the spectral-zeta side is an NCG-axiomatic question (which gauge respects the spectral triple's axiom set most directly). connes-ncg-theorist owns the axiom-native rationale for the substrate-zeta convention. Cross-reviewer (gen-physicist) ingests the verdict but does not run the gate — gen-physicist is the planner-of-record only.

**5. Hypothesis** (one sentence): The substrate-native zeta N = 3.12 e-folds is canonical when the gate is "what does the substrate's own Mellin-cone say?", while the gauge-invariant MS N = 55 e-folds is canonical when the gate is "what does an observer measuring comoving modes leaving the horizon say?", and exactly one selection rule (axiom-native, observation-native, OR pre-register-both) must be documented and bound into the W5a SECTOR-1 reporting columns.

**6. Method** (full dispatch prompt skeleton — runtime agent will instantiate):

```
You are connes-ncg-theorist, dispatched on S86-W5B-C15-i-GAUGE.

TASK
Write a substitution-chain comparison of the two N-fold conventions and document a
selection rule for the S86 pipeline.

INPUTS (read-only; pin SHA at runtime via the script template)
- sessions/session-plan/session-86-plan-w5a.md (P3 reporting columns)
- sessions/framework/spectral-zeta-canonical.md if it exists; otherwise cite
  S85 W0 source documents that define the substrate-native zeta N.
- canonical_constants.py for tau_fold, M_KK, dt_transit, w0_FW.
- gen-physicist S-7 §V.7 (the source synthesis for this gate).

METHOD
1. Define each N counter:
   - N_substrate_zeta(τ_fold) — derived from the substrate's Mellin-zeta moment
     evaluated at the τ_fold slice; cite the equation and the canonical paper.
     Numerical value for canonical pin: N = 3.12 e-folds.
   - N_MS(k_pivot) — gauge-invariant Mukhanov-Sasaki count of e-folds between
     the comoving-mode horizon-exit and the end of inflation/transit; cite
     the equation. Numerical value for the standard r-pivot: N = 55 e-folds.

2. Substitution chain — write Steps 1-4 explicitly:
   Step 1 (definitions, both N counters)
   Step 2 (substitute each definition into the canonical observable they predict;
     here the canonical observable is H(N_pivot), so plug each N into the H(N) trajectory)
   Step 3 (simplify; show the 3.12/55 numerical disparity propagates linearly into
     the eps_H * (N_initial - N_pivot) accumulation term)
   Step 4 (read off the direction; do NOT assert "55 is bigger so MS suppresses H more"
     until you have written this step explicitly; the math-is-hard hook will flag you
     if you state a direction without the chain)

3. Selection rule — document ONE of three outcomes:
   (a) AXIOM-NATIVE COMMIT: substrate-zeta N=3.12 is canonical because the spectral
       triple's axiom set selects the Mellin-zeta moment as the gauge-invariant
       fold counter at the substrate level; MS N=55 is the observer's projection.
       Justify by citing the relevant axiom (KO-dim=6, [J,D_K]=0, or the relevant
       Connes-Chamseddine axiom).
   (b) OBSERVATION-NATIVE COMMIT: MS N=55 is canonical because the project's
       observational predictions (r, n_s, A_s) are pre-registered at the comoving
       horizon-exit pivot and the substrate-zeta count cannot be measured.
       Justify by citing the falsifier-master-inventory pivot conventions.
   (c) PRE-REG-BOTH: report both pivots through S86 close; defer the canonical
       commit to a W-2 workshop output. Justify by citing the absence of a
       structurally decisive criterion.

4. Output a 2-column table for S86 pipeline use:
   | Pivot | N (e-folds) | Source | Used by gates |
   | substrate-zeta | 3.12 | <source> | <gate list> |
   | MS | 55 | <source> | <gate list> |

5. Append the verdict line via the canonical helper:
   verdict = "PASS" if (selection_rule in {a, b, c} AND substitution_chain_documented)
             else "FAIL"
   Note: c (PRE-REG-BOTH) is a valid PASS — it is a structurally legitimate
   outcome when no decisive criterion exists.

OUTPUT FILES
- computations/s86_w5b_c15_i_gauge.py (the script that emits the verdict line)
- computations/s86_w5b_c15_i_gauge_table.json (the 2-column table)
- working paper §V.7.i (the substitution chain + selection rule narrative)

GPU consideration
- Pure analytical / table-write task; no matrix ops; CPU-only with
  os.environ.setdefault('OMP_NUM_THREADS', '8') before any numpy import.
```

**7. Machinery pin (PRDR)**:
- L_max: 10 (canonical Mellin-zeta evaluation pin; relevant for the N_substrate_zeta numerical value's reproducibility)
- scheme: `mellin_zeta_substrate` (cite source)
- convention: `gauge = {substrate_zeta | MS | both}` (the gate's output)
- tolerance: not numerical (selection-rule audit); the audit PASSES iff one of (a)/(b)/(c) is documented with substitution chain
- n_eval: not applicable (analytical gate)
- random_seed: not applicable
- GPU path: CPU-only, OMP_NUM_THREADS=8

**8. Expected output 4-tuple**:
`(value="<selection_rule_chosen>", scheme="mellin_zeta_substrate", convention="<gauge_chosen>", L_max=10)`
where `<selection_rule_chosen>` is one of `axiom-native`, `observation-native`, `pre-reg-both`, and `<gauge_chosen>` is one of `substrate_zeta`, `MS`, `both`.

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: a selection rule (one of a/b/c) is documented AND the 4-step substitution chain comparing the two N counters is present in the working paper §V.7.i. The 2-column table is emitted to JSON. The c outcome (PRE-REG-BOTH) is a structurally legitimate PASS — it is the project committing to deferral, not failure.
- **FAIL**: no selection rule documented OR substitution chain missing OR table not emitted.
- **INFO**: not used for this gate (binary gate; either the selection rule + chain + table are all present, or the gate fails the audit). Tolerance rule: PRDR audit binary.

**10. Substitution chain** (planner sketch — runtime agent will expand at compute time):

The audit demands the chain in working paper §V.7.i. Sketch:

```
Step 1 (definitions):
  N_substrate_zeta(τ_fold) = (definition from substrate Mellin zeta evaluation;
    cite equation and paper)
  N_MS(k_pivot) = log[a_end / a(k_pivot exits horizon)] = 55 (standard convention)
  H(N) = H_initial * exp(-∫_0^N eps_H(N') dN')   [SR-LO trajectory]

Step 2 (substitute each N into H(N)):
  H(N_pivot)|_substrate_zeta = H_initial * exp(-∫_0^{3.12} eps_H(N') dN')
  H(N_pivot)|_MS = H_initial * exp(-∫_0^{55} eps_H(N') dN')

Step 3 (simplify under SR-LO eps_H ≈ const = eps_H_canon):
  H(N_pivot)|_substrate_zeta ≈ H_initial * exp(-3.12 * eps_H_canon)
  H(N_pivot)|_MS ≈ H_initial * exp(-55 * eps_H_canon)

Step 4 (direction — read off ONLY now):
  Ratio = H_substrate_zeta / H_MS = exp(-(3.12 - 55) * eps_H_canon)
                                  = exp((55 - 3.12) * eps_H_canon)
                                  = exp(51.88 * eps_H_canon)
  Sign of (55 - 3.12) is positive ⇒ ratio > 1 ⇒
    H(N_pivot) under substrate-zeta > H(N_pivot) under MS
  (under the same H_initial and eps_H_canon).
  This is the bookkeeping consequence of the convention disparity, not a
  physical claim — the same physical H is being labeled at two different
  pivot times under two different fold-counter conventions.
```

Direction is documented; the gate does NOT assert one convention is correct, only that the disparity is bookkeeping-consistent and that the selection rule must commit (or pre-register both).

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS (axiom-native commit)**: SECTOR-1 reports H(N_pivot) at N=3.12 as canonical; MS pivot becomes auxiliary diagnostic. Late-S86 falsifier registry uses substrate-zeta for r prediction.
- **PASS (observation-native commit)**: SECTOR-1 reports H(N_pivot) at N=55 as canonical; substrate-zeta becomes axiom-trace diagnostic. Late-S86 falsifier registry uses MS for r prediction.
- **PASS (pre-reg-both)**: SECTOR-1 reports both columns through S86 close; canonical commit deferred to W-2 workshop. Both columns flow into late-S86 falsifier registry as Path-H-substrate-zeta and Path-H-MS.
- **FAIL**: SECTOR-1 has no canonical pivot rule; downstream gates use whichever pivot was "in the script" — exactly the floatation pattern PRDR exists to prevent. Carry-forward to S87 is mandatory.

**12. Effort estimate**: ~3-4h (analytical + table-write; no compute load).

**13. Substrate-framing reminder**: The gauge counter N is the substrate's own bookkeeping of its Mellin-zeta evolution under τ. MS N=55 is a projection convention used by observers measuring comoving-mode horizon exit. Neither pivot is "in" the substrate — they are two readouts OF the substrate's spectral-zeta evolution. Direction of explanation: substrate spectral-zeta evolution → Mellin-zeta moment → either pivot bookkeeping convention. NOT: "N e-folds elapsed in spacetime" (container thinking).

---

### §W5b-1.ii — C15(ii) BASELINE forward integration

**1. Gate ID**: `S86-W5B-C15-ii-BASELINE`

**2. Trigger**: `[VERIFY]`
- Rationale: numerical ODE result against pre-registered band. The gate verifies that forward integration of `dH/dN = −eps_H · H` from substrate IC at `N_initial = N_pivot + 55 e-folds` produces `H(N_pivot)` within the pre-registered band derived from the substrate IC.

**3. Classification**: **PHONONIC** (the substrate's own H trajectory under its substrate-IC; the integration is a substrate-dynamics ODE, not a metric-projected one).

**4. Agent type** (runtime, not planner): `transit-dynamics-theorist`
- Rationale: forward integration of `dH/dN` from substrate IC is transit-physics — it is a piece of the same SECTOR-1 ODE machinery W5a P3 runs on the full coupled (ε, η, α_s, ξ²) system. transit-dynamics-theorist owns the integration scheme and the substrate-IC pin. (Note: the heavier W5a P3 is owned by transit-dynamics-theorist; W5b C15(ii) is a lighter sibling running the BASELINE limit `(η, α_s, ξ²) → 0` so the two gates can cross-check at the eps_H side.)

**5. Hypothesis** (one sentence): Forward-integrating `dH/dN = −eps_H · H` from `N_initial = N_pivot + 55 e-folds` under the substrate IC and a SR-LO `eps_H = eps_H_canon` produces `H(N_pivot)` within ±5% of the substrate-IC-projected expected value at `N_pivot`, providing the BASELINE column SECTOR-1 needs to compare against W5a P3's full coupled ODE.

**6. Method** (full dispatch prompt skeleton — runtime agent will instantiate):

```
You are transit-dynamics-theorist, dispatched on S86-W5B-C15-ii-BASELINE.

TASK
Forward-integrate the SR-LO H trajectory:
   dH/dN = − eps_H * H
from N = N_initial = N_pivot + 55 to N = N_pivot under the substrate IC, and
emit H(N_pivot) with a verdict against the pre-registered band.

INPUTS (read-only; pin SHA at runtime via the script template)
- canonical_constants.py for: eps_H_canon, M_KK, tau_fold, dt_transit, w0_FW
  (use the canonical eps_H pin; if no eps_H pin exists in canonical_constants.py,
  add one via update_constant() FIRST and cite the source as part of the input
  pin map)
- sessions/session-plan/session-86-plan-w5a.md (for cross-check at the eps_H side
  against W5a P3 trajectory)

METHOD
1. Set H_initial = H_substrate_IC. The substrate IC for H at N_initial is derived
   from the substrate-zeta or MS pivot per C15(i)'s selection rule. For the
   BASELINE gate use BOTH pivots if C15(i) returned PRE-REG-BOTH; report
   H(N_pivot) per pivot.

2. ODE setup:
   dH/dN = − eps_H * H
   eps_H = eps_H_canon (SR-LO; constant under leading approximation)

3. Integration scheme: scipy.integrate.solve_ivp, method='RK45',
   rtol=1e-8, atol=1e-10, t_span=(N_initial, N_pivot), y0=[H_initial],
   max_step=0.1 (e-folds), dense_output=True.

4. Output H(N_pivot) per pivot.

5. Cross-check 1: analytic limit H(N_pivot) = H_initial * exp(-eps_H_canon * 55).
   The numerical result should agree with this analytic form to better than the
   rtol pin (1e-8). Emit the analytic vs numerical residual as a secondary
   verdict-line diagnostic.

6. Cross-check 2: against W5a P3 trajectory at the eps_H side. W5a P3's full
   coupled ODE in the limit (η, α_s, ξ²) → 0 must reduce to this BASELINE.
   If W5a P3 has not yet landed at compute time, emit the expected agreement
   as a pre-registered downstream check and append the cross-check to the
   working paper §V.7.ii to be filled when W5a P3 lands.

7. Pre-registered band: H(N_pivot) within ±5% of the substrate-IC-projected
   expected value at N_pivot. Define the expected value as the analytic
   H_initial * exp(-eps_H_canon * 55) (BASELINE limit, no running).
   Tolerance rule: ABSOLUTE relative residual |H_num - H_analytic| / |H_analytic| < 0.05.

8. Emit verdict line via the canonical helper.

OUTPUT FILES
- computations/s86_w5b_c15_ii_baseline.py
- computations/s86_w5b_c15_ii_baseline.npz (H trajectory, t array, H array)
- computations/s86_w5b_c15_ii_baseline.png (H(N) trajectory plot)
- working paper §V.7.ii (substitution chain + integration result + cross-checks)

GPU consideration
- Sequential ODE on a 1-D state; CPU-only with
  os.environ.setdefault('OMP_NUM_THREADS', '8') before any numpy import.
- scipy.integrate.solve_ivp does not benefit from GPU here; the state vector
  is too small.
```

**7. Machinery pin (PRDR)**:
- L_max: 10 (relevant only for the substrate-IC derivation upstream; the ODE itself does not depend on L_max)
- scheme: `RK45` (scipy.integrate.solve_ivp)
- convention: `gauge = <per C15(i) verdict>` (substrate_zeta OR MS OR both)
- tolerance: rtol=1e-8, atol=1e-10, max_step=0.1 e-folds; pre-registered band ±5% on H(N_pivot)
- n_eval: dense_output=True; ~550 evaluation points across the 55-e-fold span
- random_seed: not applicable (deterministic ODE)
- GPU path: CPU-only, OMP_NUM_THREADS=8

**8. Expected output 4-tuple**:
`(value=<H(N_pivot)_numerical>, scheme="RK45_rtol1e-8", convention="<gauge>", L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: numerical H(N_pivot) within ±5% of analytic H_initial * exp(-eps_H_canon * 55); cross-check 1 (analytic-vs-numerical residual) < rtol pin (1e-8); both pivots reported if C15(i) returned PRE-REG-BOTH.
- **FAIL**: numerical H(N_pivot) outside ±5% band, OR analytic-vs-numerical residual exceeds rtol by more than 1 OOM (indicating ODE solver instability), OR ODE failed to integrate (solver returned `success = False`).
- **INFO**: not used for this gate (binary VERIFY).
- Tolerance rule: ABSOLUTE for the ±5% band; THEOREM-grade for the cross-check 1 residual (analytic identity must hold to rtol pin).

**10. Substitution chain** (planner-side direction-claim — runtime agent will expand):

```
Step 1 (definitions):
  H(N) = Hubble parameter at N e-folds (substrate-side)
  eps_H = -dlnH/dN = first SR parameter
  N_initial = N_pivot + 55
  H_initial = H(N_initial) = substrate IC

Step 2 (substitute SR-LO eps_H = eps_H_canon = const):
  dH/dN = -eps_H_canon * H
  ⇒ H(N) = H_initial * exp(-eps_H_canon * (N - N_initial))

Step 3 (simplify at N = N_pivot, where N_pivot - N_initial = -55):
  H(N_pivot) = H_initial * exp(-eps_H_canon * (N_pivot - N_initial))
             = H_initial * exp(-eps_H_canon * (-55))
             = H_initial * exp(55 * eps_H_canon)
  Wait — sign check. Re-derive:
    dH/dN = -eps_H * H, with eps_H > 0 (canonical), means H DECREASES as N
    INCREASES (later e-folds). N_initial > N_pivot (we integrate FROM the
    earlier-by-counter N_pivot UP to the later-by-counter N_initial = N_pivot+55,
    OR from N_initial DOWN to N_pivot — direction depends on convention).

    Convention pin (per C15(i) and W5a P3): N is measured forward from the
    fold (N=0 at fold), increasing toward the present. Then:
      N_pivot < N_initial = N_pivot + 55, so we integrate BACKWARD in N from
      N_initial to N_pivot. H_initial is the value at N_initial (later e-fold);
      H(N_pivot) is the value at the earlier e-fold.

    Re-substitute: H(N_pivot) = H_initial * exp(-eps_H_canon * (N_pivot - N_initial))
                              = H_initial * exp(-eps_H_canon * (-55))
                              = H_initial * exp(+55 * eps_H_canon)

Step 4 (direction):
  eps_H_canon > 0 ⇒ exp(+55 * eps_H_canon) > 1 ⇒
    H(N_pivot) > H_initial.
  ✓ This is consistent with the SR picture: H is LARGER at earlier e-folds
  (smaller N) and DECREASES as N grows (more e-folds = closer to end of inflation).
```

The runtime agent must verify this direction at compute time and reconcile with the W5a P3 convention. If the convention in canonical_constants.py / W5a P3 has N increasing toward the past (opposite of above), the integration direction flips and the chain re-derives to `H(N_pivot) < H_initial`.

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: BASELINE H(N_pivot) is established as the no-running, free-streaming reference. W5a P3 must reduce to this in the (η, α_s, ξ²) → 0 limit. The full SR-flow result quantifies the running's effect on H(N_pivot).
- **FAIL**: ODE integration failed OR analytic limit violated. The latter implies a sign or convention bug in the substrate-IC pin or the eps_H pin; FAIL forces a re-pinning of canonical_constants.py before W5a P3 can be trusted.

**12. Effort estimate**: ~3-4h (script + integration + cross-check + working-paper section).

**Combined C15 effort estimate (i + ii)**: ~6-8h, matching partition §1 W5b allocation.

**13. Substrate-framing reminder**: H here is the substrate's own Hubble parameter at each fold-counter N. The trajectory is the substrate's eps_H-driven evolution under SR-LO; eps_H itself is a spectral-action moment of D_K (the leading slow-roll parameter is a Seeley-DeWitt-encoded substrate observable, not an inflaton-field roll rate).

---

## §W5b-2. S86-W0-0-PRDR-PIN-CSUB (C16)

**1. Gate ID**: `S86-W5B-C16-CSUB-ADMISSIBILITY`

**2. Trigger**: `[VERIFY]`
- Rationale: PRDR-compliant classification of `c_sub = 3.647` against three pre-registered sub-tests. Each sub-test produces a numerical residual against a threshold; the composite verdict is ADMISSIBLE iff all three pass, EXCLUDED iff any fails, INFO iff exactly two pass. This is a [VERIFY] gate (numerical residuals against pre-registered thresholds), not [AUDIT] (which would be procedural).

**3. Classification**: **PHONONIC** (the c_sub coefficient is a substrate-Mellin-cone quantity entering the Path-C r=0.0117 prediction; admissibility classification is a substrate-property test, not an observational one).

**4. Agent type** (runtime, not planner): `lizzi-spectral-functional-theorist`
- Rationale: c_sub admissibility is a Mellin-convention / L_max / UV-cut combination test (Lizzi-track infrastructure). Sub-tests (a) and (b) (UV cut + Mellin convention; tau-stationarity) are squarely lizzi-spectral-functional-theorist's domain. Sub-test (c) (conformal-anomaly consistency with S79 P1-2 W2-E sign-reversal) overlaps with connes-ncg-theorist's CCM-2007 framework but the sign-reversal rule itself is a Mellin-cone diagnostic. lizzi is the primary; connes-ncg-theorist is the cross-reviewer if sub-test (c) requires axiom-side adjudication.

**5. Hypothesis** (one sentence): The value `c_sub = 3.647` is ADMISSIBLE as a substrate-Mellin-cone coefficient if and only if (a) the UV-cut + Mellin-convention + L_max combination producing 3.647 is identifiable in the canonical-constants regulator atlas, (b) `c_sub` is τ-stationary at the τ_fold-anchored evaluation point with `max_slope = |d(c_sub)/dτ| / |c_sub| < 0.1` per S83 W2-G12, AND (c) `c_sub` is conformal-anomaly consistent with the S79 P1-2 W2-E sign-reversal rule.

**6. Method** (full dispatch prompt skeleton — runtime agent will instantiate):

```
You are lizzi-spectral-functional-theorist, dispatched on S86-W5B-C16-CSUB-ADMISSIBILITY.

TASK
Classify c_sub = 3.647 as ADMISSIBLE / EXCLUDED / INFO via three pre-registered
sub-tests.

INPUTS (read-only; pin SHA at runtime via the script template)
- canonical_constants.py for c_sub, c_fabric, M_KK, tau_fold (and confirm
  c_sub = 3.647 is present; if not, locate the source of 3.647 in S-7 §V.8
  and resolve via update_constant() OR mark sub-test (a) FAIL).
- sessions/archive/session-83/ artifacts referenced by W2-G12 (max_slope criterion).
- sessions/archive/session-79/ artifacts referenced by P1-2 W2-E (sign-reversal rule).
- gen-physicist S-7 §V.8 (the source synthesis).

METHOD — Sub-test (a) UV cut + Mellin convention + L_max identification
1. Locate the canonical-constants entry or S-7 §V.8 derivation that produces
   c_sub = 3.647. Record the full quadruple (UV_cut_name, Mellin_convention,
   L_max, source_paper_or_session).
2. Verify the quadruple is a member of the canonical regulator atlas (W12-4
   5-regulator atlas + any post-W4 cutoff_sqrt extensions). If not in the
   atlas, sub-test (a) FAILS.
3. Sub-test (a) verdict: PASS iff quadruple identified AND quadruple ∈ canonical
   regulator atlas; FAIL otherwise.

METHOD — Sub-test (b) tau-stationarity per S83 W2-G12
1. Compute c_sub(τ) for τ in a neighborhood of τ_fold:
   τ ∈ [τ_fold - δ, τ_fold + δ] with δ = 0.05 * τ_fold (5% perturbation),
   N_eval = 21 grid points (10 below, 10 above, 1 at τ_fold).
2. For each τ, evaluate c_sub at the SAME (UV_cut, Mellin_convention, L_max)
   quadruple from sub-test (a). If sub-test (a) FAILED, sub-test (b) is
   not runnable; mark sub-test (b) FAIL by inheritance.
3. Compute max_slope = max_{i} |c_sub(τ_{i+1}) - c_sub(τ_i)| /
                       (|c_sub(τ_fold)| * (τ_{i+1} - τ_i)).
   Then normalize per S83 W2-G12: max_slope_normalized = max_slope * τ_fold
   (so the criterion |d(c_sub)/dτ| / |c_sub| < 0.1 reads as a dimensionless
   stationarity bound).
4. Sub-test (b) verdict: PASS iff max_slope_normalized < 0.1; FAIL otherwise.
   Tolerance rule: ABSOLUTE on max_slope_normalized.

METHOD — Sub-test (c) conformal-anomaly consistency with S79 P1-2 W2-E sign-reversal
1. Locate the sign-reversal rule from S79 P1-2 W2-E: cite the equation and
   the verdict line. The rule states the sign of the conformal-anomaly
   contribution to c_sub MUST flip across τ_fold for substrate-admissible
   regulators (the substrate's spectral-action a_4 coefficient inherits the
   sign-reversal from the post-fold sheet structure).
2. Compute the conformal-anomaly contribution to c_sub at τ_fold - δ and
   τ_fold + δ (using the τ-grid from sub-test (b); take the endpoints).
   Read off the sign of each.
3. Sub-test (c) verdict: PASS iff sign(c_sub_anomaly(τ_fold - δ)) ≠
   sign(c_sub_anomaly(τ_fold + δ)) (sign reverses across τ_fold); FAIL otherwise.
   Tolerance rule: sign-comparison binary.

COMPOSITE VERDICT
- ADMISSIBLE iff (a) PASS AND (b) PASS AND (c) PASS.
- INFO iff exactly 2 of {(a), (b), (c)} PASS (downstream gates can use c_sub
  with explicit `c_sub_admissibility = INFO` annotation).
- EXCLUDED iff 0 or 1 of {(a), (b), (c)} PASS.

Emit ONE verdict line via the canonical helper:
   S86-W5B-C16-CSUB-ADMISSIBILITY: PASS|FAIL|INFO -- value=<ADMISSIBLE|INFO|EXCLUDED>
   scheme=<UV_cut_name>_<Mellin_convention> convention=tau_fold_anchored L_max=10
   sha256=<closure>

In the comment row immediately after, emit the per-sub-test outcomes:
   # sub_test_a=PASS|FAIL sub_test_b=PASS|FAIL sub_test_c=PASS|FAIL
   # max_slope_normalized=<value> sign_pre_fold=<+|-> sign_post_fold=<+|->
   # content_sha256=<64-char> audit_sha256=<64-char>

OUTPUT FILES
- computations/s86_w5b_c16_csub_admissibility.py
- computations/s86_w5b_c16_csub_admissibility.npz (τ-grid, c_sub(τ),
  c_sub_anomaly(τ_fold ± δ))
- computations/s86_w5b_c16_csub_admissibility.png (c_sub(τ) plot with
  max_slope envelope and sign-reversal markers)
- working paper §V.8 (3-sub-test substitution chain + composite classification +
  downstream consequences for late-S86 W13 P2 r-Both-Pathways)

GPU consideration
- The c_sub(τ) evaluation may invoke heat-kernel / Mellin-cone routines that
  involve matrix ops at L_max=10 (D_K cache is ≥100×100; W2 C9/C10 Mellin
  infrastructure when available will be GPU-accelerated). If the c_sub(τ)
  evaluator uses torch.linalg per W2 infrastructure, route through GPU.
  Otherwise CPU-only with OMP_NUM_THREADS=8 caps.
```

**7. Machinery pin (PRDR)**:
- L_max: 10 (canonical Mellin-cone evaluation pin)
- scheme: `<UV_cut_name>_<Mellin_convention>` — the quadruple from sub-test (a); script must read this from canonical_constants.py and emit it in the verdict line, NEVER hardcode
- convention: `tau_fold_anchored` (the τ-stationarity test is anchored at τ_fold from canonical_constants.py)
- tolerance: max_slope_normalized < 0.1 (sub-test b); sign-comparison binary (sub-test c); regulator-atlas membership binary (sub-test a)
- n_eval: 21 τ-grid points (sub-test b); 2 endpoint evaluations (sub-test c)
- random_seed: not applicable (deterministic Mellin evaluation)
- GPU path: torch.linalg if c_sub(τ) evaluator engages D_K matrix ops at L_max=10 (≥100×100); CPU-only otherwise with OMP_NUM_THREADS=8

**8. Expected output 4-tuple**:
`(value="<ADMISSIBLE|INFO|EXCLUDED>", scheme="<UV_cut_name>_<Mellin_convention>", convention="tau_fold_anchored", L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS (composite verdict = ADMISSIBLE)**: all three sub-tests PASS. Path-C with c_sub = 3.647 is substrate-admissible; late-S86 W13 P2 r-Both-Pathways lands the dual registration (Path-H r=0.00745 + Path-C r=0.0117).
- **FAIL (composite verdict = EXCLUDED)**: 0 or 1 sub-test PASSes. Path-C with c_sub = 3.647 is substrate-incompatible; late-S86 W13 P2 reduces to Path-H-only.
- **INFO (composite verdict = INFO)**: exactly 2 sub-tests PASS. Path-C c_sub = 3.647 is conditionally usable downstream with explicit `c_sub_admissibility = INFO` annotation; late-S86 W13 P2 lands the dual registration with the annotation appended.
- **Per-sub-test tolerance rules**: (a) regulator-atlas binary; (b) max_slope_normalized < 0.1 ABSOLUTE; (c) sign-reversal binary.

**10. Substitution chain** (sub-test (b) max_slope direction; runtime agent expands):

```
Step 1 (definitions):
  c_sub(τ) = substrate Mellin-cone coefficient at slice τ
  max_slope = max_{i} |c_sub(τ_{i+1}) - c_sub(τ_i)| / (τ_{i+1} - τ_i)
  max_slope_normalized = max_slope * τ_fold / |c_sub(τ_fold)|
  S83 W2-G12 criterion: |d(c_sub)/dτ| / |c_sub| < 0.1 at τ_fold

Step 2 (substitute the discrete approximation for d/dτ):
  d(c_sub)/dτ |_{τ ≈ τ_fold} ≈ (c_sub(τ_{i+1}) - c_sub(τ_i)) / (τ_{i+1} - τ_i)
  ⇒ |d(c_sub)/dτ| / |c_sub| ≈ max_slope / |c_sub(τ_fold)|

Step 3 (simplify by inserting τ_fold to dimensionless):
  max_slope_normalized = (max_slope / |c_sub(τ_fold)|) * τ_fold
  Criterion: max_slope_normalized < 0.1
  is equivalent to: |d(c_sub)/dτ| * τ_fold / |c_sub| < 0.1
  ⇔ |d(c_sub)/d(ln τ)| / |c_sub| < 0.1
  (scale-invariant logarithmic derivative bound)

Step 4 (direction):
  max_slope_normalized < 0.1 ⇒ c_sub is τ-stationary at τ_fold
  (insensitive to the τ-grid neighborhood; the value 3.647 is not an artifact
  of evaluating at a single τ point on a steep slope).
  max_slope_normalized ≥ 0.1 ⇒ c_sub is τ-sensitive at τ_fold
  (the value 3.647 is a snapshot of a fast-varying function; sub-test (b) FAILS
  and the value is not a stable substrate observable).
```

For sub-test (c), the substitution chain is qualitative (sign-comparison): the substrate's spectral-action a_4 coefficient must inherit a sign reversal across τ_fold per S79 P1-2 W2-E because the post-fold sheet structure of the Riemann cover flips the sign of the conformal-anomaly contribution. This is a structural claim, not a numerical residual; the chain documents WHY the sign must flip, then the gate verifies it does.

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS (ADMISSIBLE)**: c_sub = 3.647 is a stable, regulator-atlas-member, conformal-anomaly-consistent substrate observable. Path-C r=0.0117 is a structurally legitimate prediction. Late-S86 W13 P2 promotes r to falsifier-master-inventory under BOTH pathways (Path-H r=0.00745 + Path-C r=0.0117); SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030 fires both watch points.
- **FAIL (EXCLUDED)**: Path-C is structurally inadmissible. Late-S86 W13 P2 reduces to Path-H-only (r=0.00745). The 36.5% Path-H/Path-C split flagged in P2's spec is no longer a free parameter — it is closed (Path-C eliminated). The framework's r prediction collapses to a single number with no internal-consistency split.
- **INFO**: c_sub = 3.647 is conditionally usable. P2 lands the dual registration with `c_sub_admissibility = INFO` annotation. The 36.5% split remains as an OPEN flag carried forward to S87 for an explicit re-test under W2 Mellin-cone infrastructure when it lands in S86 W2.

**12. Effort estimate**: ~4h (script + 3-sub-test compute + working-paper section).

**13. Substrate-framing reminder**: c_sub is NOT a phenomenological knob. It is a Mellin-cone coefficient computed from the substrate's spectral zeta evaluated at the τ_fold slice under a specific (UV_cut, Mellin_convention, L_max) regulator. Sub-test (b) τ-stationarity asks: is 3.647 a property of the substrate at τ_fold, or an artifact of evaluating at one point on a τ-trajectory? Sub-test (c) sign-reversal asks: does the substrate's post-fold sheet structure produce the conformal-anomaly sign flip the canonical-constants ledger expects? Direction of explanation: substrate spectral zeta → Mellin-cone coefficient at τ slice → c_sub(τ) → admissibility for downstream observational gates. NOT: "c_sub is a tunable parameter in the model" (parameter-fitting framing).

---

## §X. Wave W5b → Downstream Decision Point

W5b's two verdicts feed two downstream pin actions:

1. **C15 → W5a P3 pivot pin** (S86 close):
   - If C15(i) = `axiom-native` PASS: W5a P3 reports SECTOR-1 at substrate-zeta pivot N=3.12 as canonical; MS pivot N=55 is auxiliary diagnostic. canonical_constants.py gets `N_pivot_canonical = 3.12` with provenance citing S86-W5B-C15-i-GAUGE.
   - If C15(i) = `observation-native` PASS: W5a P3 reports SECTOR-1 at MS pivot N=55 as canonical; substrate-zeta is axiom-trace diagnostic. canonical_constants.py gets `N_pivot_canonical = 55` with the same provenance.
   - If C15(i) = `pre-reg-both` PASS: W5a P3 reports both columns; canonical_constants.py gets BOTH `N_pivot_substrate_zeta = 3.12` AND `N_pivot_MS = 55`; canonical commit deferred to S87 W-2 workshop.
   - If C15(i) = FAIL: W5a P3 inherits the unpinned pivot; verdict is PRE-REG-INCOMPLETE downstream; carry-forward to S87 mandatory.

2. **C16 → late-S86 W13 P2 r-Both-Pathways admissibility** (S86 close):
   - If C16 = ADMISSIBLE: P2 promotes r to falsifier-master-inventory under BOTH-Pathways with both r=0.00745 (Path-H) and r=0.0117 (Path-C); the SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030 fires both branches.
   - If C16 = EXCLUDED: P2 promotes r to falsifier-master-inventory under Path-H ONLY (r=0.00745); late-S86 P2 records the c_sub=3.647 EXCLUDED finding as the closure event.
   - If C16 = INFO: P2 promotes r under BOTH pathways with `c_sub_admissibility = INFO` annotation; the 36.5% split remains OPEN for S87 re-test under W2 Mellin-cone infrastructure.

Both downstream pins are recorded by the W13 / W5a planners' verdict consolidation, NOT by W5b. W5b's responsibility ends at emitting the three verdict lines (C15(i), C15(ii), C16) to `computations/s86_gate_verdicts.txt`.

---

## §0.10. Wave W5b Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness (PRDR), every gate-relevant machinery parameter is enumerated below. A parameter left unpinned is PRU Class 8 (PRE-REG-INCOMPLETE), not FAIL.

| Gate | Parameter | Pin | Rationale |
|:-----|:---------|:----|:----------|
| C15(i) GAUGE | L_max | 10 | substrate-zeta N derivation depends on L_max (Mellin-zeta moment evaluation pin) |
| C15(i) GAUGE | scheme | `mellin_zeta_substrate` | the substrate's own zeta-anchored fold counter |
| C15(i) GAUGE | convention | `gauge ∈ {substrate_zeta, MS, both}` | the gate's OUTPUT (selection rule) |
| C15(i) GAUGE | tolerance | binary (audit) | selection rule + chain + table all present |
| C15(i) GAUGE | n_eval | n/a | analytical |
| C15(i) GAUGE | random_seed | n/a | deterministic |
| C15(i) GAUGE | GPU path | CPU, OMP_NUM_THREADS=8 | no matrix ops |
| C15(ii) BASELINE | L_max | 10 | upstream substrate-IC dependency |
| C15(ii) BASELINE | scheme | `RK45` (scipy.integrate.solve_ivp) | numerical ODE method pinned |
| C15(ii) BASELINE | convention | `gauge` per C15(i) verdict | substrate_zeta OR MS OR both |
| C15(ii) BASELINE | tolerance | rtol=1e-8, atol=1e-10, max_step=0.1 e-folds; ±5% band on H(N_pivot) | ODE solver pins + pre-registered band |
| C15(ii) BASELINE | n_eval | dense_output=True; ~550 pts across 55 e-folds | ODE solver evaluation density |
| C15(ii) BASELINE | random_seed | n/a | deterministic ODE |
| C15(ii) BASELINE | GPU path | CPU, OMP_NUM_THREADS=8 | 1-D state, no GPU benefit |
| C15(ii) BASELINE | eps_H | `eps_H_canon` from canonical_constants.py | SR-LO; if not yet pinned, add via update_constant() FIRST |
| C15(ii) BASELINE | H_initial | substrate-IC at N_initial = N_pivot + 55 | per C15(i) selection rule |
| C16 CSUB | L_max | 10 | canonical Mellin-cone evaluation pin |
| C16 CSUB | scheme | `<UV_cut_name>_<Mellin_convention>` from sub-test (a) | quadruple read from canonical_constants.py / S-7 §V.8; NEVER hardcoded |
| C16 CSUB | convention | `tau_fold_anchored` | τ-stationarity test anchored at τ_fold |
| C16 CSUB | tolerance | (a) atlas-membership binary; (b) max_slope_normalized < 0.1 ABSOLUTE; (c) sign-reversal binary | per-sub-test pre-registered |
| C16 CSUB | n_eval | 21 τ-grid points (sub-test b); 2 endpoints (sub-test c) | grid density pinned |
| C16 CSUB | random_seed | n/a | deterministic Mellin evaluation |
| C16 CSUB | GPU path | torch.linalg if D_K matrix ops at L_max=10 (≥100×100); else CPU OMP_NUM_THREADS=8 | per `feedback_compute-environment.md` |
| C16 CSUB | δ (τ-perturbation) | 0.05 * τ_fold (5%) | sub-test (b) neighborhood half-width |

PRU posture: if the runtime agent discovers a free parameter not enumerated above, the gate is suspended (NOT executed) and the planner is re-engaged to pin the parameter. PRU Class 8 (plan-property failure) is the correct verdict for any unpinned parameter discovered at compute time.

---

## §0.11. Wave W5b Input-SHA Ledger

| Gate | Input file | SHA pin | Notes |
|:-----|:----------|:--------|:------|
| C15(i), C15(ii), C16 | `computations/canonical_constants.py` | `<computed-at-runtime>` | version of canonical_constants.py at script invocation; runtime SHA emitted in first 20 lines of stdout per script-template §3 |
| C15(i) | `sessions/session-plan/session-86-plan-w5a.md` | `<computed-at-runtime>` | for cross-reference of pivot reporting columns; if W5a plan not yet present, gate emits an explicit "downstream-plan-not-yet-present" diagnostic and proceeds with C15(i) selection rule independently |
| C15(i) | `sessions/framework/spectral-zeta-canonical.md` (if exists) | `<computed-at-runtime>` | substrate-native zeta N derivation source; if absent, runtime agent cites S85 W0 source documents |
| C15(ii) | `sessions/session-plan/session-86-plan-w5a.md` | `<computed-at-runtime>` | for cross-check 2 (BASELINE vs W5a P3 (η, α_s, ξ²) → 0 limit) |
| C16 sub-test (a) | gen-physicist S-7 §V.8 | `<computed-at-runtime>` | source of c_sub = 3.647 quadruple |
| C16 sub-test (a) | canonical regulator atlas (W12-4 5-regulator atlas + post-W4 cutoff_sqrt extensions) | `<computed-at-runtime>` | atlas-membership check |
| C16 sub-test (b) | S83 W2-G12 artifacts (`computations/s83_w2_g12_*` files) | `<computed-at-runtime>` | max_slope criterion source |
| C16 sub-test (c) | S79 P1-2 W2-E artifacts (`computations/s79_*` files referenced) | `<computed-at-runtime>` | sign-reversal rule source |
| C15(ii) | substrate-IC source for H_initial | `<computed-at-runtime>` | per C15(i) selection rule; either substrate-zeta or MS pivot anchor |

Closure SHA per gate: computed at runtime from the ordered input-pin map per the canonical script template (§4). SHA is full 64-char hexdigest in the canonical verdict line per `.claude/rules/gate-verdicts.md`. The 16-char head form is permitted ONLY in the prose sections of the verdict file, NEVER in the canonical line.

---

## End of Wave W5b plan

Three verdict lines expected at S86 close, all written to `computations/s86_gate_verdicts.txt`:

1. `S86-W5B-C15-i-GAUGE: PASS|FAIL -- value=<axiom-native|observation-native|pre-reg-both> scheme=mellin_zeta_substrate convention=<gauge_chosen> L_max=10 sha256=<64-char>`
2. `S86-W5B-C15-ii-BASELINE: PASS|FAIL -- value=<H(N_pivot)_numerical> scheme=RK45_rtol1e-8 convention=<gauge> L_max=10 sha256=<64-char>`
3. `S86-W5B-C16-CSUB-ADMISSIBILITY: PASS|FAIL|INFO -- value=<ADMISSIBLE|INFO|EXCLUDED> scheme=<UV_cut_name>_<Mellin_convention> convention=tau_fold_anchored L_max=10 sha256=<64-char>`

Each followed by a comment row carrying `content_sha256=<64-char> audit_sha256=<64-char>` per dual-SHA infra (W0b R10 lift).

Three working-paper sections expected: §V.7.i (C15(i)), §V.7.ii (C15(ii)), §V.8 (C16). Each ≥15 lines of substantive content per `.claude/rules/agent-standards.md` completion check.
