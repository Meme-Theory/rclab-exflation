# Session 86 Plan — Wave W5a: SECTOR-1 SR-flow Z-factor (DOMINANT load)

**Generated**: 2026-04-25
**Wave owner (planner)**: `transit-dynamics-theorist`
**Wave owner (runtime, per partition manifest §1.W5a)**: `transit-dynamics-theorist` — but per planner ≠ runner discipline, the dispatching orchestrator MUST select a fresh `transit-dynamics-theorist` instance OR co-dispatch `mack-cosmic-bridge` as ODE-numerical-method co-author (mack 9A §VI.3 is the cited source for the sub-wave structure). `gen-physicist` is explicitly NOT eligible as runtime agent for this wave (specialist-required per partition §1 Wave-W5a "Natural split candidates").
**Output (this file)**: `sessions/session-plan/session-86-plan-w5a.md`
**Theme**: SECTOR-1 SR-flow Z-factor — SR-LO ODE integration of (ε, η, α_s, ξ²) under substrate-first ξ²(0) IC, anchored at the W4 P4 ξ_E_GGE^{−1} pin
**Item count**: 1 (P3 dominant; 1.5 wave-equivalents per closeout §6.2)
**Verdict-file path (canonical, mandatory)**: `computations/s86_gate_verdicts.txt`

---

## §0. Wave W5a Summary

Wave W5a contains exactly ONE compute gate, but it is the **largest single-gate load in the entire S86 carry-forward** (1.5 wave-equivalents per closeout §6.2 + partition manifest §1.W5a). The gate is the SECTOR-1 anchor of the 2A SECTOR split (gen-physicist 9A §4.5a + mack 9A §VI.3): integrate the four-component slow-roll-flow ODE system from N=0 (fold) to N=N_pivot (canonical pivot) under a **substrate-first initial condition for ξ²(0)** sourced from the W4 P4 BRANCH-IV pin commit.

### Why this is one item, not two

- The (ε, η, α_s, ξ²) system is COUPLED: ξ² enters the η-equation through the SR-LO Mukhanov-Sasaki structure, ε enters the ξ²-equation through dε/dN, α_s is the second-derivative output of the trajectory. Splitting (ε, η) from (α_s, ξ²) would re-decouple after a few RK45 steps and require re-coupling — net cost is HIGHER than running the coupled solver once.
- The substrate-first vs LCDM-IC comparison REQUIRES the same integration architecture; running both ICs as one script (with the IC vector as a parameter swept from `xi2_0=xi_E_GGE_inv` to `xi2_0=0`) is the architecturally-clean implementation.

### GPU/CPU contention notes

- **ODE integration is sequential** (cannot parallelize across timesteps). GPU offers no advantage.
- The right-hand-side of the four-component ODE involves at most 4×4 matrix algebra → CPU is appropriate.
- Per `feedback_compute-environment.md`, the dispatch prompt MUST cap CPU threads: `os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`. This prevents 32-core contention with concurrently-running W5b (gen-physicist owner; W5b runs C15 + C16 in parallel batch-2).
- `scipy.integrate.solve_ivp` with method `'RK45'` (default Dormand-Prince adaptive) or `'LSODA'` (auto stiff/non-stiff switching) is the canonical numerical kernel.

### Effort + watchdog

- 1.5 wave-equivalents = 12-18 agent-hours (per closeout §6.2 wave-equivalent budget §7).
- HEAVIER than any single S85 gate. Per `feedback_dispatch-discipline.md` + S84 agent-death-when-overwhelmed lesson, this gate should NOT be co-dispatched with another HEAVY single-gate item; W5a runs alone in batch-2 alongside lighter waves.
- If the agent stalls without writing the script, the natural fallback per partition §1 is to dispatch a `gen-physicist` ODE-numerical-method co-author (NOT to re-dispatch with a leaner spec — S84 lesson: "stalled agents don't mean do it again, but shittier").

---

## §0.5. Wave W5a Decision-Point Prerequisites

| Type | Prerequisite | Source | Status pre-S86 | Action if unmet |
|:-----|:-------------|:-------|:---------------|:----------------|
| **HARD** | W4 P4 `S86-BRANCH-IV-FORMULATION-COMMIT` lands ξ_E_GGE^{−1} (s=−1 spectral diagnostic, distance-1) into `canonical_constants.py` AND permanent-results-registry | partition §1 Wave W4; closeout §6.4 sequencing row 4 | UNMET at S86-W5a dispatch time (W4 runs in batch-2 alongside W5a) | Wait for W4 P4 verdict line `S86-BRANCH-IV-FORMULATION-COMMIT: PASS` before launching W5a P3 script. The orchestrator MUST sequence: (W4 P4 lands `xi_E_GGE_inv` constant) → (W5a P3 imports it). |
| **HARD** | `xi_E_GGE_inv` registered in `canonical_constants.py` with full provenance | W4 P4 deliverable | UNMET | Same as above. |
| **SOFT** | W5b C15 GAUGE selection (3.12 e-folds substrate-native zeta vs 55 e-folds gauge-invariant Mukhanov-Sasaki) | partition §1 Wave W5b; gen-physicist S-7 §V.7 | UNMET (W5b runs in same batch-2 as W5a) | If W5b C15 has not landed at W5a start, W5a P3 PRE-REGISTERS BOTH pivots: report Z(N_pivot=55) and Z(N_pivot=3.12) as TWO output 4-tuples in the verdict file, both pre-registered against the same band. The pivot ambiguity is a separate gate, not a W5a methodology defect. |
| **SOFT** | W0a R3 cutoff_axis YAML pin landed | partition §1 Wave W0a | LIKELY landed by S86-W5a (W0a runs in batch-1) | If not, the W5a YAML gate block at §0.10 below cannot validate R3-schema; mark `schema_version: R3` field as `<pending-W0a-R3>` and re-run validator after W0a completes. |
| **SOFT** | W0c C18 `eps_H_HP1_norm` registered | partition §1 Wave W0c | LIKELY landed by S86-W5a | Used in cross-check (iii) below; if not landed, fall back to S84 W1a-1 `eps_H_anchor` value with regulator-pin tag. |

### Substitution chain — why SECTOR-1 sources from ξ_E_GGE^{−1}, not from R_JK

```
Step 1 (definition):
  ξ_E_GGE^{−1}(N=0)  ≡ s=−1 spectral diagnostic of the GGE relic
                        at the fold, evaluated against Energy-class operator E.
                       (gen-physicist 9A §3.6; W4 P4 commit content).
                        Distance-1 quantity in the substrate-first taxonomy.
  R_JK(N=0)          ≡ K-functional, distance-2 (one substrate operator
                        composed with one Jensen-deformed inner product).
  ξ²(N)              ≡ quantum-pressure factor in the SR-LO MS equation
                        v_k'' + (k² − z''/z + ξ²·k²/(aH)²) v_k = 0
                       (Mukhanov-Sasaki canonical form per gen-physicist 9A §4.5a).

Step 2 (substitute):
  ξ²(N=0) IC = ξ_E_GGE^{−1}(N=0)    [substrate-first IC choice, 2A SECTOR-1]
  vs
  ξ²(N=0) IC = 0                     [LCDM-baseline reference]

Step 3 (simplify):
  The substrate-first IC is at distance-1 from the GGE relic state (ONE
  spectral evaluation s=−1 against E-class operator). R_JK would be at
  distance-2. The 2A SECTOR-1 split per gen-physicist 9A §4.5a SELECTS
  distance-1 for SECTOR-1 because:
    (i)  ξ²(0) IS a pressure factor in MS, not a K-functional output, so
         the natural homological pairing is (s=−1, E) not (K, E).
    (ii) distance-2 IC would route through R_JK and require an extra
         convolution, doubling the evolution-equation order.

Step 4 (direction):
  SECTOR-1 IC = ξ_E_GGE^{−1}, NOT R_JK. This is a CHOICE, fixed by the
  W4 P4 BRANCH-IV commit, not by the W5a integration. W5a measures
  Z(N_pivot) under this IC; if Z(N_pivot) FAILs, the FAIL closes the
  SECTOR-1 corridor (substrate-first ξ²(0) IC incompatible with SR-LO
  at N_pivot), NOT the BRANCH-IV commit itself.
```

---

## §I. Carry-Forward Items Mapping

| Carry-forward # | Title | Wave assignment | Wave-internal block |
|:----------------|:------|:----------------|:---------------------|
| **P3** | `S86-SECTOR-1-SR-FLOW-Z-FACTOR` (1.5 wave-equivalents — DOMINANT single-gate load) | **W5a** (this file) | §W5a-1 below |

Source: gen-physicist 9A §4.5a (substrate-first IC selection + 2A SECTOR-1 framing) + mack 9A §VI.3 (Z-factor target observable + SR-LO ODE prescription).

No other partition items live in W5a. P5 (SECTOR-2) lives in W4 (batch-2 sibling); C15 + C16 (gauge + BASELINE forward integration; c_sub admissibility) live in W5b (batch-2 sibling).

---

## §W5a-1. S86-SECTOR-1-SR-FLOW-Z-FACTOR (P3) [VERIFY] [SIGN]

### 1. Gate ID

`S86-SECTOR-1-SR-FLOW-Z-FACTOR`

### 2. Trigger

`[VERIFY]` — quantitative numerical agreement against pre-registered band (Z(N_pivot) ∈ [Z_min, Z_max] computed from substrate-first vs LCDM-IC ratio).

`[SIGN]` — final Z-factor magnitude direction vs LCDM-IC reference run carries an implication for whether the substrate-first IC SUPPRESSES or ENHANCES the canonical Mukhanov amplitude at the pivot. Substitution chain in §10 below is MANDATORY.

### 3. Classification

**PHONONIC** (substrate transit-physics; SR-flow ODE is a substrate-dynamics integration of how the quantum-pressure factor evolves across e-folds, NOT LCDM inflation). Per `.claude/rules/phononic-framing.md` "IS Space, Not IN Space" reframe: the (ε, η, α_s, ξ²) trajectory is the substrate's spectral-state evolution, not "fields evolving in inflating spacetime."

### 4. Agent type — runtime assignment

**Primary**: `transit-dynamics-theorist` (specialist; substrate-first IC + ODE integration is transit-physics, NOT a generalist task per partition §1 Wave-W5a "Natural split candidates"). The planner is `transit-dynamics-theorist`; the orchestrator MUST dispatch a FRESH `transit-dynamics-theorist` instance at runtime (planner ≠ runner separation).

**Cross-cite at runtime if specialist stalls**: `mack-cosmic-bridge` (mack 9A §VI.3 is the cited source for the Z-factor target + SR-LO prescription). Mack is the natural co-author for the ODE-numerical-method spec.

**EXPLICITLY blacklisted as runtime**: `gen-physicist` (breadth coordinator; per S84 W1/W2 lesson "per-wave specialists succeed where gen-physicist breadth-coordinator stalls on dense waves"). The 1.5 wave-equivalent load REQUIRES specialist depth, not breadth.

### 5. Hypothesis

**The Z-factor at N_pivot integrated under the substrate-first ξ²(0) IC differs from the LCDM-IC integration by a calculable substrate-spectral factor, anchoring SECTOR-1 of the 2A SECTOR split. Specifically: the substrate-first IC ξ²(0) = ξ_E_GGE^{−1} > 0 induces faster initial growth of ε(N) compared to ξ²(0) = 0, and consequently Z(N_pivot)|substrate < Z(N_pivot)|LCDM at fixed N_pivot, with the magnitude of the suppression ratio bounded by the canonical Mukhanov-Sasaki SR-LO trajectory and the W4 P4 ξ_E_GGE^{−1} value.**

### 6. Method (complete dispatch prompt)

> You are `transit-dynamics-theorist`, dispatched as the runtime computer for `S86-SECTOR-1-SR-FLOW-Z-FACTOR`. You are integrating **substrate dynamics**, NOT LCDM inflation. The (ε, η, α_s, ξ²) ODE system describes how the substrate's quantum-pressure factor evolves across e-folds; the Z-factor at N_pivot measures the substrate's Mukhanov-amplitude normalization at the canonical pivot.
>
> **Substrate-framing reminder (mandatory)**: The Mukhanov-Sasaki variable z(N, k) ≡ a(N)·sqrt(2ε(N))·M_Pl_eff(k) is the substrate's quantum-pressure normalization. ξ²(N) is NOT an inflaton attribute — it is the substrate's own pressure-factor evolution, sourced at N=0 by the GGE relic via ξ²(0) = ξ_E_GGE^{−1}. You are computing how this substrate quantity evolves; do NOT phrase the result in terms of "inflation predicting A_s" — phrase it as "substrate pressure-factor at the pivot."
>
> **Pre-flight checks (BEFORE writing the script)**:
> 1. Query `mcp__knowledge__get_constant("xi_E_GGE_inv")` to confirm the W4 P4 pin has landed in `canonical_constants.py`. If the constant returns "not registered," HALT and report "W4 P4 prerequisite unmet." Do NOT proceed.
> 2. Query `mcp__knowledge__get_constant("tau_fold")`, `mcp__knowledge__get_constant("M_Pl_eff")`, `mcp__knowledge__search_knowledge("SR-LO Mukhanov-Sasaki substrate-first")` to retrieve canonical inputs.
> 3. Query `mcp__knowledge__search_knowledge("Z-factor SR-flow ODE substrate-first IC")` to confirm no prior S86 verdict for this gate exists.
>
> **Write the script** at `computations/s86_w5a_p3_sector_1_sr_flow.py`:
>
> ```python
> # computations/s86_w5a_p3_sector_1_sr_flow.py
> # SECTOR-1 SR-flow Z-factor under substrate-first xi^2(0) IC
> # Gate: S86-SECTOR-1-SR-FLOW-Z-FACTOR
>
> import os
> os.environ.setdefault('OMP_NUM_THREADS', '8')  # CPU thread cap per feedback_compute-environment.md
>
> import numpy as np
> from scipy.integrate import solve_ivp
> from canonical_constants import (
>     tau_fold,            # fold position
>     xi_E_GGE_inv,        # W4 P4 pin (HARD DEPENDENCY)
>     M_Pl_eff,            # canonical Planck-effective for z normalization
>     # eps_H_HP1_norm,    # available if W0c C18 landed; fallback otherwise
> )
> # ... imports continue
>
> # ---------------- The four-component coupled ODE system (SR-LO) ----------------
> # Mukhanov-Sasaki SR-LO form (gen-physicist 9A §4.5a; mack 9A §VI.3):
> #   dε/dN  = ε(2η - 4ε + 2ξ²)
> #   dη/dN  = -ε·η + α_s + (η - ε)·η   [SR-LO truncation]
> #   dα_s/dN = -2ε·α_s + 2η·α_s + 2(higher-order terms truncated at SR-LO)
> #   dξ²/dN = -2ε·ξ² + (substrate-source term β_ξ from SR-LO closure)
> #
> # Refs: Mukhanov 2005 §8.1 + Sasaki 1986; substrate-first IC per 2A SECTOR-1
> # commit per gen-physicist 9A §4.5a; ξ²(0) source = xi_E_GGE_inv (W4 P4 pin).
>
> def rhs(N, y):
>     eps, eta, alpha_s, xi2 = y
>     deps_dN     = eps * (2*eta - 4*eps + 2*xi2)
>     deta_dN     = -eps*eta + alpha_s + (eta - eps)*eta
>     dalpha_s_dN = -2*eps*alpha_s + 2*eta*alpha_s   # SR-LO truncation
>     dxi2_dN     = -2*eps*xi2                          # substrate-source closure at SR-LO
>     return [deps_dN, deta_dN, dalpha_s_dN, dxi2_dN]
>
> # ---------------- Initial conditions at N=0 (fold) ----------------
> # Substrate-first IC (SECTOR-1, 2A path):
> eps_0       = 0.020             # canonical small-ε from W1a baseline (S85 W1a-1, see canonical_constants if registered)
> eta_0       = 0.005             # canonical small-η
> alpha_s_0   = 0.0               # SR-LO IC: α_s sourced dynamically
> xi2_0_sub   = xi_E_GGE_inv      # SUBSTRATE-FIRST IC (HARD DEPENDENCY on W4 P4)
> xi2_0_lcdm  = 0.0               # LCDM-baseline reference IC
>
> # ---------------- Pivot pre-registration ----------------
> # Pre-register BOTH pivots per W5a §0.5 SOFT prerequisite (W5b C15 may not have landed):
> N_PIVOTS = {
>     "MS_canonical": 55.0,       # gauge-invariant Mukhanov-Sasaki canonical
>     "substrate_native_zeta": 3.12,  # substrate-native ζ pivot
> }
>
> # ---------------- Integrate ----------------
> # Numerical-method choice (state explicitly + rationale):
> #   method='RK45' (Dormand-Prince adaptive timestep) — non-stiff fallback;
> #   method='LSODA' — auto stiff/non-stiff switching, robust if ε(N) → singular near fold-1.
> # Pre-register: USE 'LSODA' as primary; cross-check with 'RK45' on substrate-IC run.
> # Tolerances: rtol=1e-8, atol=1e-10, max_step=0.01 e-folds (per partition §1 Wave-W5a spec).
>
> N_span = (0.0, 60.0)            # integrate past 55 to capture both pivots
> N_eval = np.linspace(0.0, 60.0, 6001)  # 0.01 e-fold resolution → 6001 points
>
> sol_sub = solve_ivp(rhs, N_span,
>                     [eps_0, eta_0, alpha_s_0, xi2_0_sub],
>                     method='LSODA', rtol=1e-8, atol=1e-10, max_step=0.01,
>                     t_eval=N_eval)
>
> sol_lcdm = solve_ivp(rhs, N_span,
>                      [eps_0, eta_0, alpha_s_0, xi2_0_lcdm],
>                      method='LSODA', rtol=1e-8, atol=1e-10, max_step=0.01,
>                      t_eval=N_eval)
>
> # Cross-check: rerun substrate-IC under RK45
> sol_sub_RK45 = solve_ivp(rhs, N_span,
>                          [eps_0, eta_0, alpha_s_0, xi2_0_sub],
>                          method='RK45', rtol=1e-8, atol=1e-10, max_step=0.01,
>                          t_eval=N_eval)
>
> # ---------------- Compute Z(N) at both pivots, both ICs ----------------
> # z(N, k) = a(N) · sqrt(2·ε(N)) · M_Pl_eff(k)
> # Z(N_pivot) ≡ z(N_pivot, k_pivot) / z(0, k_pivot) = (a_pivot/a_0) · sqrt(ε_pivot/ε_0)
> # The k dependence cancels in the ratio if M_Pl_eff is k-independent at SR-LO.
>
> def Z_factor(sol, N_pivot):
>     idx = np.argmin(np.abs(sol.t - N_pivot))
>     eps_pivot = sol.y[0, idx]
>     a_ratio = np.exp(N_pivot)   # a(N)/a(0) = exp(N) by definition of e-fold
>     return a_ratio * np.sqrt(eps_pivot / eps_0)
>
> Z_results = {}
> for name, N_pivot in N_PIVOTS.items():
>     Z_sub  = Z_factor(sol_sub,  N_pivot)
>     Z_lcdm = Z_factor(sol_lcdm, N_pivot)
>     Z_results[name] = {
>         "Z_substrate_LSODA": float(Z_sub),
>         "Z_LCDM_LSODA":      float(Z_lcdm),
>         "Z_ratio":           float(Z_sub / Z_lcdm),
>         "Z_substrate_RK45":  float(Z_factor(sol_sub_RK45, N_pivot)),
>     }
>
> # ---------------- Cross-checks ----------------
> # (i) at N=0, ODE values match IC exactly:
> assert abs(sol_sub.y[0, 0] - eps_0) < 1e-12, "IC mismatch on ε"
> assert abs(sol_sub.y[3, 0] - xi2_0_sub) < 1e-12, "IC mismatch on ξ²"
>
> # (ii) ε(N) monotone non-decreasing toward fold (post-fold the SR-LO ODE may diverge;
> # we test monotone-non-decreasing on the segment N ∈ [0, min(55, N_breakdown)]):
> eps_traj = sol_sub.y[0, :]
> N_breakdown = sol_sub.t[np.where(eps_traj > 0.5)[0][0]] if np.any(eps_traj > 0.5) else 60.0
> mask = sol_sub.t <= min(55.0, N_breakdown)
> assert np.all(np.diff(eps_traj[mask]) >= -1e-9), "ε not monotone-non-decreasing on integration window"
>
> # (iii) LSODA vs RK45 cross-check on substrate-IC run (numerical-method robustness):
> for name in N_PIVOTS:
>     dev = abs(Z_results[name]["Z_substrate_LSODA"] - Z_results[name]["Z_substrate_RK45"])
>     rel_dev = dev / abs(Z_results[name]["Z_substrate_LSODA"])
>     assert rel_dev < 1e-4, f"LSODA-RK45 disagreement at {name}: {rel_dev}"
>
> # ---------------- Verdict logic ----------------
> # PASS band: |Z_ratio - 1| ≤ 0.05 (ABSOLUTE 5% on Z(N_pivot)/Z_LCDM(N_pivot))
> # Per feedback_arbitrary-gates.md: ratio against LCDM-IC reference is preferred over
> # round-number absolute thresholds.
> # The PASS band is set by dimensional analysis: substrate-first IC perturbs ξ² by ξ_E_GGE^{−1} ≈ O(10^-2)
> # at N=0; the integrated impact on ε(N_pivot) is O(ξ_E_GGE^{−1} · N_pivot) at SR-LO ≈ O(10^-2 · 55) = O(0.5);
> # the resulting Z-ratio deviates from 1 by sqrt(1 + O(0.5)) − 1 ≈ 0.225, so the ±5% PASS band
> # measures whether the substrate-first IC is in the LINEAR-perturbation regime around LCDM
> # OR has driven the trajectory into nonlinear deviation.
> # ABSOLUTE 5% on Z_ratio per partition §1 Wave-W5a.
>
> def classify(Z_ratio_val):
>     dev = abs(Z_ratio_val - 1.0)
>     if dev <= 0.05:
>         return "PASS"
>     elif dev <= 0.10:
>         return "INFO"   # band-overshoot diagnostic, ≤2× the PASS band
>     else:
>         return "FAIL"
>
> # ---------------- Emit verdicts ----------------
> # Two verdict lines (one per pre-registered pivot), per W5a §0.5 SOFT prereq handling.
> # SHA256 closure computed from input_pin_map ∪ machinery_pin_map per gate-verdicts.md.
>
> # ... emit verdict line per W9a-99 dual-SHA template:
> #   GATE_ID|VERDICT|VALUE|SCHEME|CONVENTION|L_MAX|content_sha256:<64>|audit_sha256:<64>
> # to computations/s86_gate_verdicts.txt
>
> # ---------------- Output files ----------------
> # computations/s86_w5a_p3_sector_1_z_factor.npz   (full ODE trajectory)
> # computations/s86_w5a_p3_sector_1_z_factor.png   (4-panel: ε, η, α_s, ξ² vs N)
> # computations/s86_w5a_p3_sector_1_z_factor.json  (Z(N_pivot) values + verdict for both pivots)
> ```
>
> **Output deliverables (all required for completion-verification per `.claude/rules/agent-standards.md` §Completion Verification)**:
>
> 1. `computations/s86_w5a_p3_sector_1_sr_flow.py` — non-stub, fully runnable.
> 2. `computations/s86_w5a_p3_sector_1_z_factor.npz` — keys: `N_eval`, `eps_substrate`, `eta_substrate`, `alpha_s_substrate`, `xi2_substrate`, `eps_lcdm`, `eta_lcdm`, `alpha_s_lcdm`, `xi2_lcdm`, `Z_at_pivots_substrate`, `Z_at_pivots_lcdm`.
> 3. `computations/s86_w5a_p3_sector_1_z_factor.png` — 4-panel: ε(N), η(N), α_s(N), ξ²(N) for substrate-IC vs LCDM-IC overlaid; vertical lines at N=3.12 and N=55.
> 4. `computations/s86_w5a_p3_sector_1_z_factor.json` — full Z(N_pivot) table + verdict classification for both pivots.
> 5. **TWO verdict lines** appended to `computations/s86_gate_verdicts.txt` (one per pre-registered pivot) under W9a-99 dual-SHA schema.
> 6. Working-paper section §VI.W5a-1 written IN FULL (not stub) before terminating.

### 7. Machinery pin (PRDR — Pre-Registration Dry-Run)

```yaml
schema_version: R3
gate_id: S86-SECTOR-1-SR-FLOW-Z-FACTOR
machinery_pin_map:
  L_max: 10                       # canonical for substrate spectra
  n_tau: N/A                      # this is e-fold integration, not τ scan
  n_eval: 6001                    # N=0 to N=60 at 0.01 e-fold resolution
                                  #   (covers both pivots: 3.12 and 55)
  N_span: [0.0, 60.0]
  scheme: SR-LO-Mukhanov-Sasaki
  convention: substrate-first-xi2(0)-IC
                                  #   (vs LCDM-baseline xi2(0)=0 reference run)
  cutoff_axis: spectral           # per W0a R3 cutoff_axis YAML pin
  numerical_method_primary: LSODA
  numerical_method_crosscheck: RK45 (Dormand-Prince)
  rtol: 1.0e-8
  atol: 1.0e-10
  max_step: 0.01                  # e-folds
  random_seed: N/A                # deterministic ODE
  GPU_path: CPU OMP_NUM_THREADS=8
                                  #   (ODE sequential, no GPU benefit)
  pivot_pre_registration:
    - name: MS_canonical
      N_pivot: 55.0
      source: gauge-invariant Mukhanov-Sasaki (60 e-folds before horizon exit at CMB pivot)
    - name: substrate_native_zeta
      N_pivot: 3.12
      source: S77 N-PIVOT-MAP (substrate-native ζ pivot; superhorizon at fold)
  PASS_band: "|Z_ratio - 1| <= 0.05  (ABSOLUTE 5% on Z(N_pivot)/Z_LCDM(N_pivot))"
  INFO_band: "0.05 < |Z_ratio - 1| <= 0.10  (band-overshoot diagnostic)"
  FAIL_clause: "|Z_ratio - 1| > 0.10  OR ODE diverges  OR LSODA-RK45 disagreement > 1e-4 relative"

input_pin_map:
  canonical_constants_imports:
    - tau_fold:       <provenance: canonical_constants.py current SHA at dispatch>
    - xi_E_GGE_inv:   <computed-at-runtime: W4 P4 commit output SHA>
                       # HARD DEPENDENCY: must exist in canonical_constants.py before script imports
    - M_Pl_eff:       <provenance: canonical_constants.py current SHA at dispatch>
    - eps_H_HP1_norm: <provenance: W0c C18 commit output SHA, OR fallback to S84 W1a-1 anchor>
  external_inputs: NONE  (this gate is purely substrate-derivable)
  closure_hash: <computed-at-runtime>  # SHA256 of input_pin_map ∪ machinery_pin_map (audit_sha256)
```

**PRU vulnerability check**: every free parameter in the script is pinned above. The numerical-method choice (LSODA primary + RK45 cross-check) is pinned to prevent convention-shopping; the tolerance is fixed; the pivot is pre-registered as TWO values (not a free post-hoc choice). The substrate-first IC vs LCDM-baseline split is two RUNS of the same script, not two separate gates.

### 8. Expected output 4-tuple(s) — TWO verdict lines per W5a §0.5 pivot pre-registration

For each pivot, the verdict line uses the W9a-99 dual-SHA schema:

```
S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55|<VERDICT>|value=<Z_ratio_at_55>|scheme=SR-LO-Mukhanov-Sasaki|convention=substrate-first-xi2(0)-IC|L_max=10|content_sha256:<64-hex>|audit_sha256:<64-hex>
S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT312|<VERDICT>|value=<Z_ratio_at_3.12>|scheme=SR-LO-Mukhanov-Sasaki|convention=substrate-first-xi2(0)-IC|L_max=10|content_sha256:<64-hex>|audit_sha256:<64-hex>
```

Plus the 16-hex companion comment row per W9a-99 split:

```
# audit_sha256_short=<16-hex>
```

Per `.claude/rules/gate-verdicts.md` "Canonical Verdict-File Path": these two lines append to `computations/s86_gate_verdicts.txt`. The variants `sessions/archive/session-86/...` and `sessions/session-plan/...` are FORBIDDEN.

### 9. PASS / FAIL / INFO thresholds with tolerance rule

| Outcome | Numerical criterion | Tolerance type | Rationale |
|:--------|:---------------------|:---------------|:----------|
| **PASS** | `|Z_ratio - 1| ≤ 0.05` at the pivot, where `Z_ratio = Z_substrate(N_pivot) / Z_LCDM(N_pivot)` | ABSOLUTE 5% on the dimensionless Z-ratio | The substrate-first IC is in the LINEAR-perturbation regime around the LCDM baseline; the SR-LO truncation is self-consistent at the pivot. |
| **INFO** | `0.05 < |Z_ratio - 1| ≤ 0.10` | ABSOLUTE 10% on Z-ratio (band-overshoot diagnostic) | The substrate-first IC is at the BOUNDARY of linear-perturbation validity; SR-LO may need NLO extension to close the residual factor of 2 gap. Methodology-flagged result — INFO is a structured pre-registered outcome per `feedback_arbitrary-gates.md`, NOT a near-FAIL. |
| **FAIL** | `|Z_ratio - 1| > 0.10`  OR  ODE diverges before reaching N_pivot  OR  LSODA-RK45 cross-check relative deviation > 1e-4 | mixed (10% on Z-ratio; structural on ODE divergence; numerical-method robustness on cross-check) | The substrate-first IC is INCOMPATIBLE with the SR-LO trajectory at N_pivot; the substrate-distance-1 ξ²(0) cannot source a consistent SR-LO flow. SECTOR-1 corridor closes. |

Per `feedback_arbitrary-gates.md`: the threshold is computed as a **ratio against LCDM-IC reference run**, NOT a round-number absolute on Z(N_pivot) itself. The 5% / 10% bands derive from the SR-LO linear-perturbation regime around LCDM (substitution chain in §10).

Per `.claude/rules/math-scripts.md` §Exit Codes and Verdict Semantics: PASS, FAIL, and INFO ALL exit code 0. They are scientific outcomes, not script errors.

### 10. Substitution chain (MANDATORY for [SIGN] direction claim)

```
Step 1 (definitions):
  Mukhanov-Sasaki canonical:
    z(N, k)       ≡ a(N) · sqrt(2·ε(N)) · M_Pl_eff(k)         [Mukhanov 2005 §8.1]
    a(N)          ≡ exp(N)                                      [definition of e-fold]
    ε(N)          ≡ -dH/dN / H                                 [first SR parameter]
    η(N)          ≡ dε/dN / ε                                   [second SR parameter, SR-LO]
    α_s(N)        ≡ d²ln(P_ζ) / d(ln k)²                       [running of running, SR-LO output]
    ξ²(N)         ≡ quantum-pressure factor in MS equation     [substrate-distance-1 IC source]
    ξ_E_GGE^{−1}  ≡ s=−1 spectral diagnostic of GGE relic
                    against E-class operator at the fold        [W4 P4 pin; gen-physicist 9A §3.6]

  Z-factor target observable:
    Z(N_pivot)    ≡ z(N_pivot, k_pivot) / z(0, k_pivot)
                  = (a_pivot/a_0) · sqrt(ε_pivot/ε_0)
                                                               [k-dependence cancels at SR-LO]
                  = exp(N_pivot) · sqrt(ε(N_pivot)/ε(0))
                                                               [substituting a(N) = exp(N)]

Step 2 (substitute IC choice):
  Substrate-first IC (SECTOR-1):  ξ²(0) = ξ_E_GGE^{−1}  > 0
  LCDM-baseline IC (reference):   ξ²(0) = 0

  The SR-LO ODE for ε(N) is:
    dε/dN = ε(2η - 4ε + 2ξ²)
  Initial slope at N=0:
    (dε/dN)|substrate(0) = ε(0)·(2·η(0) - 4·ε(0) + 2·xi_E_GGE_inv)
    (dε/dN)|LCDM(0)      = ε(0)·(2·η(0) - 4·ε(0) + 0)
  Difference:
    Δ(dε/dN)|N=0 = ε(0) · 2 · xi_E_GGE_inv
                 = 2·ε_0·xi_E_GGE_inv > 0    [since ε_0 > 0 and xi_E_GGE_inv > 0]

Step 3 (simplify direction):
  Substrate-first IC drives ε(N) to grow FASTER than LCDM-baseline at N=0.
  Integrating across N ∈ [0, N_pivot] (assuming the perturbation stays linear):
    ε_substrate(N_pivot) ≈ ε_LCDM(N_pivot) + 2·ε_0·xi_E_GGE_inv·N_pivot · (1 + O(SR^2))
  Therefore:
    ε_substrate(N_pivot) > ε_LCDM(N_pivot)        (substrate-first IC INCREASES ε at the pivot)

  Substituting into Z(N_pivot):
    Z_substrate(N_pivot) = exp(N_pivot) · sqrt(ε_substrate(N_pivot) / ε_0)
    Z_LCDM(N_pivot)      = exp(N_pivot) · sqrt(ε_LCDM(N_pivot)      / ε_0)

  Z-ratio:
    Z_ratio ≡ Z_substrate(N_pivot) / Z_LCDM(N_pivot)
            = sqrt(ε_substrate(N_pivot) / ε_LCDM(N_pivot))

  Since ε_substrate(N_pivot) > ε_LCDM(N_pivot):
    Z_ratio > 1                                   (substrate-first IC ENHANCES Z at the pivot)

Step 4 (read direction from canonical form):
  CLAIM (refined from §5 hypothesis): The substrate-first ξ²(0) IC ENHANCES Z(N_pivot)
  relative to the LCDM-baseline IC, BECAUSE faster initial ε-growth produces a larger
  ε(N_pivot), and Z scales as sqrt(ε).

  CORRECTION TO §5 HYPOTHESIS: the original hypothesis ("substrate-first IC SUPPRESSES
  Z(N_pivot)") was WRONG IN DIRECTION. The substitution chain shows substrate-first IC
  ENHANCES Z(N_pivot) (Z_ratio > 1), it does not suppress.

  Magnitude estimate (linear-perturbation):
    Z_ratio - 1 ≈ (1/2)·(ε_substrate(N_pivot) − ε_LCDM(N_pivot))/ε_LCDM(N_pivot)
                ≈ (1/2)·(2·ε_0·xi_E_GGE_inv·N_pivot)/ε_LCDM(N_pivot)
                ≈ ε_0·xi_E_GGE_inv·N_pivot / ε_LCDM(N_pivot)

  Plugging in: ε_0 ≈ 0.020; xi_E_GGE_inv pending W4 P4 (estimate O(10^-2));
  N_pivot = 55; ε_LCDM(55) ≈ 0.05 (SR-flow grows ε by factor ~2.5 over 55 e-folds at SR-LO):
    Z_ratio - 1 ≈ 0.020 · 0.01 · 55 / 0.05 ≈ 0.22

  THIS EXCEEDS THE PASS BAND (|Z_ratio - 1| ≤ 0.05). The pre-registered prediction is
  THEREFORE that the gate FAILs at MS_canonical pivot (N=55), unless xi_E_GGE_inv is
  smaller than the O(10^-2) estimate by ~5×. AT N=3.12 (substrate-native ζ pivot):
    Z_ratio - 1 ≈ 0.020 · 0.01 · 3.12 / 0.025 ≈ 0.025
  WHICH IS WITHIN THE PASS BAND. SO THE PRE-REGISTERED PREDICTION IS:
    - PIVOT55:  expected FAIL (|Z_ratio - 1| ≈ 0.22)
    - PIVOT312: expected PASS (|Z_ratio - 1| ≈ 0.025)

Direction (final): substrate-first IC ENHANCES Z(N_pivot); the magnitude depends linearly
on N_pivot. The smaller pivot (3.12 e-folds, substrate-native ζ) is consistent with PASS;
the larger pivot (55 e-folds, MS canonical) is expected to FAIL — which is itself
a CONSTRAINT-MAP RESULT consistent with the broader S77/S78 finding that substrate-first
predictions live at small N_pivot, not at the LCDM-canonical 55-e-fold pivot.

VERIFY-PYTHON: the magnitude estimates above (0.22 and 0.025) are ANALYTIC pre-registrations.
The actual W5a P3 numerical verdicts will replace these estimates; if numerical Z_ratio at
PIVOT55 lands in PASS band (≤0.05), that REFUTES the SR-LO linear-perturbation analysis
above and indicates either ξ_E_GGE_inv ≪ 10^-2 OR nonlinear backreaction not captured at
SR-LO. Either outcome is a constraint-map gain.
```

**Note on hypothesis correction**: §5 above stated "substrate-first IC SUPPRESSES Z(N_pivot)"; the substitution chain shows the direction is OPPOSITE (substrate-first IC ENHANCES Z). Per `.claude/rules/agent-standards.md` §Formal Rigor "Self-correct immediately if an error is detected mid-derivation," the §5 hypothesis is hereby corrected: **substrate-first IC ENHANCES Z(N_pivot) by a calculable factor** (Z_ratio > 1 at fixed N_pivot).

### 11. What PASS / FAIL / INFO MEAN for the solution space

| Outcome (per pivot) | Solution-space implication |
|:---------------------|:---------------------------|
| **PASS at PIVOT55** (MS canonical 55 e-folds) | SECTOR-1 anchored as the substrate-first SR-flow at the LCDM-canonical pivot. Unblocks substrate→A_s/n_s prediction chain at MS-pivot resolution. Strong constraint: substrate-first IC is consistent with LCDM-style SR-flow over 55 e-folds. |
| **INFO at PIVOT55** | SR-LO linear-perturbation regime is at boundary of validity at MS pivot; consider NLO extension. Methodology-flagged, NOT a corridor closure. |
| **FAIL at PIVOT55** | Substrate-first IC is incompatible with SR-LO at the MS canonical pivot. THIS DOES NOT CLOSE THE FRAMEWORK — it CLOSES THE SR-LO-AT-N=55 corridor. The substrate-native pivot (3.12 e-folds) is the natural alternative; per substitution-chain pre-registration, FAIL at PIVOT55 + PASS at PIVOT312 is the substrate-first signature. |
| **PASS at PIVOT312** (substrate-native ζ pivot 3.12 e-folds) | SECTOR-1 anchored at substrate-native pivot. Confirms S77 N-PIVOT-MAP finding that substrate predictions are subhorizon at fold (k/aH=14.7 at PIVOT312). Unblocks substrate→A_s/n_s at substrate-pivot resolution. |
| **INFO at PIVOT312** | Substrate-pivot SR-flow at boundary of linear regime; same caveat as INFO at PIVOT55 but with smaller magnitude. |
| **FAIL at PIVOT312** | Substrate-first IC is incompatible with SR-LO even at the substrate-native pivot. This WOULD close SECTOR-1 entirely (no pivot at which substrate-first IC produces consistent SR-flow). 2A SECTOR split would collapse: BRANCH-IV would no longer have a path-(c) sector-1 anchor. |
| **DOUBLE FAIL (both pivots)** | The 2A SECTOR split per gen-physicist 9A §4.5a collapses. SECTOR-1 corridor is closed. SECTOR-2 (W4 P5) becomes the only path-(c) anchor. Major framework reorganization required. |
| **DOUBLE PASS (both pivots)** | Substrate-first IC is robust across both pivots (substrate-native and MS-canonical). Strongest possible SECTOR-1 anchoring. Unblocks A_s + n_s + α_s prediction chain at both resolutions. |

Per `.claude/rules/epistemic-discipline.md` §"How to Assess a Mechanism": the gate maps the boundary of the SR-LO + substrate-first IC corridor. Each verdict is a constraint-map result, NOT a framework-status update. PASS, INFO, FAIL all advance the constraint map per `feedback_reporting-framing.md`.

### 12. Effort estimate

- **1.5 wave-equivalents** (12-18 agent-hours per `feedback_dispatch-discipline.md` 8-agent × 2h/agent = 16 agent-hours/wave).
- Bottlenecks: (a) script-write + LSODA implementation 4-6h; (b) 4-panel plot generation 1-2h; (c) two-pivot verdict line generation + working-paper section 3-5h; (d) cross-check verification + numerical-method robustness 2-3h; (e) buffer for LSODA stiffness near fold-1 boundary 2-4h.
- GPU/CPU contention: NONE on GPU (ODE is sequential). CPU contention with W5b (gen-physicist owner, batch-2 sibling) is mitigated by `OMP_NUM_THREADS=8` cap.
- Watchdog: if the dispatched agent reports "killed" or "stalled" without writing the script after the equivalent of 1 wave (8-10 hours), invoke partition §1 Wave-W5a fallback: dispatch `mack-cosmic-bridge` as ODE-numerical-method co-author with the SAME full-fidelity spec (NOT a leaner spec — S84 lesson).

### 13. Substrate-framing reminder

**MANDATORY in agent dispatch prompt**: "You are integrating substrate dynamics, not LCDM inflation. The ξ²(0) IC encodes the substrate's spectral state at the fold via the s=−1 diagnostic against E-class operators (W4 P4 pin: ξ_E_GGE^{−1}). Z(N_pivot) measures how the substrate's quantum-pressure factor evolves across e-folds. The Mukhanov-Sasaki form is borrowed as a calculational scaffold for the substrate's SR-LO trajectory; it is NOT an inflaton-as-fundamental-field assertion. Per `.claude/rules/phononic-framing.md` IS-Space-Not-IN-Space: the (ε, η, α_s, ξ²) trajectory IS the substrate's spectral-state evolution, not 'fields evolving in inflating spacetime.' Do not phrase results as 'inflation predicts A_s'; phrase as 'substrate pressure-factor at the pivot, integrated under substrate-first ξ²(0) IC.'"

Per `.claude/rules/phononic-framing.md` "Exflation vs Inflation" table: agents MUST avoid "slow-roll inflation" / "inflaton field" / "reheating" vocabulary in the working paper. Use "supersonic transit / Mach 13.75 fold" / "Jensen deformation parameter τ" / "GGE relic formation" instead. The Z-factor itself is a calculational quantity from the MS scaffold; the framing of WHAT Z measures is "substrate quantum-pressure normalization at e-fold N," not "inflaton perturbation amplitude at horizon exit."

---

## §X. Wave W5a → Downstream Decision Point

### Z(N_pivot) feeds the substrate→A_s/n_s prediction chain

The Z-factor at the canonical pivot (whether MS=55 or substrate-native=3.12) directly normalizes the Mukhanov amplitude:
```
A_s = (H/Z(N_pivot))² / (8π² · M_Pl_eff²)
n_s − 1 = −2ε(N_pivot) − η(N_pivot)
α_s = (dn_s / d ln k)|_pivot, output of the SR-LO trajectory
```

W5a P3 produces the Z(N_pivot), ε(N_pivot), η(N_pivot), α_s(N_pivot) numerical values that downstream gates (P6 CGWB α_s independence, P7 ρ_substrate MC, late-S86 P9/P10 falsifier consolidation) consume.

### If W5a P3 PASSes (at either pivot)

- SECTOR-1 anchoring confirmed; the 2A SECTOR split has its substrate-first sector instantiated.
- W4 P5 SECTOR-2 + W7 C1 joint CC residue can quote SECTOR-1 ε/η/Z values as inputs.
- The substrate→A_s prediction chain is LIVE at the PASS-pivot resolution.

### If W5a P3 FAILs (at both pivots — the most adversarial outcome)

- The 2A SECTOR split per gen-physicist 9A §4.5a COLLAPSES: SECTOR-1 has no path-(c) anchor.
- BRANCH-IV (W4 P4) would need to commit ENTIRELY to the SECTOR-2 (Mellin-kernel K-invariant) anchoring.
- This is a CONSTRAINT-MAP RESULT (closes one of two SECTOR alternatives), NOT a framework-status update.
- Late-S86 EVOI refresh (P13) would record SECTOR-1 closure under the constraint-map ledger.

### If W5a P3 returns mixed (FAIL at PIVOT55 + PASS at PIVOT312 — the substitution-chain pre-registered prediction)

- The pre-registered substitution chain (§10 Step 4) IS verified.
- Substrate-first predictions are confirmed to live at substrate-native pivot (3.12 e-folds), NOT at the LCDM-canonical 55-e-fold pivot.
- This INFORMS the W5b C15 GAUGE selection: substrate-native ζ pivot is the canonical N-fold counter for substrate-first predictions; gauge-invariant MS pivot is the canonical for LCDM-comparison purposes ONLY.
- The W5b C15 verdict (in batch-2) becomes the natural CONFIRMATION-OR-REFUTATION gate for this substitution-chain prediction.

---

## §0.10. Wave W5a Machinery-Enumeration Pin (single-gate PRDR table)

| Gate | Free parameter | Pinned value | Pinned by | Diagnostic-only? |
|:-----|:----------------|:--------------|:-----------|:-----------------|
| P3 | L_max | 10 | canonical for substrate spectra | NO |
| P3 | n_eval | 6001 | 0.01 e-fold resolution × 60 e-folds + 1 | NO |
| P3 | N_span | [0.0, 60.0] | covers both pivots (3.12 and 55) plus margin | NO |
| P3 | scheme | SR-LO Mukhanov-Sasaki | Mukhanov 2005 §8.1 + gen-physicist 9A §4.5a | NO |
| P3 | convention | substrate-first ξ²(0) IC | 2A SECTOR-1 commit (gen-physicist 9A §4.5a) | NO |
| P3 | reference convention | LCDM-baseline ξ²(0)=0 | reference for Z-ratio | NO |
| P3 | numerical_method_primary | LSODA | scipy auto stiff/non-stiff (handles potential stiffness near fold) | NO |
| P3 | numerical_method_crosscheck | RK45 (Dormand-Prince) | numerical-method robustness check | NO |
| P3 | rtol | 1.0e-8 | partition §1 Wave-W5a spec | NO |
| P3 | atol | 1.0e-10 | partition §1 Wave-W5a spec | NO |
| P3 | max_step | 0.01 e-folds | partition §1 Wave-W5a spec | NO |
| P3 | random_seed | N/A | deterministic ODE | NO |
| P3 | GPU_path | CPU OMP_NUM_THREADS=8 | sequential ODE; `feedback_compute-environment.md` | NO |
| P3 | cutoff_axis | spectral | W0a R3 cutoff_axis YAML pin | NO |
| P3 | pivot pre-registration | TWO values: 55.0 AND 3.12 | W5a §0.5 SOFT prereq handling for W5b C15 | NO (both pre-registered → both verdicted) |
| P3 | PASS band | |Z_ratio − 1| ≤ 0.05 | ABSOLUTE 5%; partition §1 Wave-W5a + `feedback_arbitrary-gates.md` ratio-against-LCDM rule | NO |
| P3 | INFO band | 0.05 < |Z_ratio − 1| ≤ 0.10 | band-overshoot diagnostic at 2× PASS band | NO |
| P3 | FAIL clause | |Z_ratio − 1| > 0.10  OR  ODE diverges  OR  LSODA-RK45 disagreement > 1e-4 | structural + numerical-method robustness | NO |
| P3 | numerical-method cross-check tolerance | 1e-4 relative | LSODA-RK45 self-consistency | YES (audit) |
| P3 | ε_0 IC | 0.020 | S85 W1a-1 baseline anchor (canonical_constants if registered) | NO |
| P3 | η_0 IC | 0.005 | canonical small-η; documented in MS literature | NO |
| P3 | α_s_0 IC | 0.0 | SR-LO IC (α_s sourced dynamically) | NO |
| P3 | ξ²_0 IC (substrate-first run) | xi_E_GGE_inv | W4 P4 commit output | NO |
| P3 | ξ²_0 IC (LCDM-baseline run) | 0.0 | reference IC | NO |

**PRU vulnerability count**: 0 (D_PRU_raw = 0). Every free parameter is pinned. The IC values for ε_0, η_0 are anchored to S85 W1a-1; if those land in canonical_constants.py via W0c C18 in batch-1, the runtime imports them; otherwise the dispatched agent uses the documented anchors with explicit `# (local)` tag per `.claude/rules/math-scripts.md`.

**Schema validator**: `computations/_yaml_gate_validator.py` MUST be run on this gate block AFTER W0a R3 lands; PASS at sig_4 ≥90% per `.claude/rules/v3-closure-recovery.md` per-signal remediation map.

---

## §0.11. Wave W5a Input-SHA Ledger (Phase 3e validator input)

| Input file / canonical-constants entry | SHA at dispatch time | Source / commit |
|:----------------------------------------|:----------------------|:-----------------|
| `computations/canonical_constants.py` | `<computed-at-runtime>` | current commit; latest snapshot at 2026-04-24 |
| `computations/canonical_constants.py::tau_fold` | `<provenance pin>` | S35 fold-derivation lineage |
| `computations/canonical_constants.py::xi_E_GGE_inv` | `<computed-at-runtime: W4 P4 commit output SHA>` | **HARD DEPENDENCY**: W4 P4 must land first |
| `computations/canonical_constants.py::M_Pl_eff` | `<provenance pin>` | canonical Planck-effective; established lineage |
| `computations/canonical_constants.py::eps_H_HP1_norm` | `<W0c C18 commit output SHA, OR fallback to S84 W1a-1 anchor SHA>` | SOFT dependency on W0c C18 |
| `sessions/session-plan/session-86-context.md` | `<as-checked-out at S86 plan-write>` | input to Phase 3e validator |
| `sessions/session-plan/session-86-partition.md` | `<as-checked-out at S86 plan-write>` | input to Phase 3e validator |
| Closure SHA for the gate audit_sha256 | `<computed-at-runtime>` | `closure_hash(input_pin_map ∪ machinery_pin_map)` per `.claude/rules/gate-verdicts.md` |

**Phase 3e validation**: `computations/_plan_upstream_pin_validator.py --json` MUST be invoked on this plan file before Phase 4. Exit 0 PASS / 1 HARD FAIL (pin drift, slug typo) / 2 PARSE-ERROR (re-dispatch as stall per `.claude/rules/v3-closure-recovery.md` Stage 1).

The runtime script `s86_w5a_p3_sector_1_sr_flow.py` MUST log the SHA-256 of every input listed above in the first 20 lines of stdout and emit the closure hash, per `.claude/rules/gate-verdicts.md` §"During computation."

---

**End of Wave W5a plan.** One full 13-field gate block delivered for the DOMINANT single-gate load of S86 (1.5 wave-equivalents). Sequencing: HARD on W4 P4 (ξ_E_GGE^{−1} pin) which runs in batch-1; SOFT on W5b C15 (gauge selection) which runs in batch-2 sibling. Pre-registered prediction per substitution chain §10 Step 4: PIVOT55 expected FAIL (Z_ratio − 1 ≈ 0.22), PIVOT312 expected PASS (Z_ratio − 1 ≈ 0.025); the actual verdict CONFIRMS or REFUTES this analytic pre-registration and feeds the W5b C15 GAUGE selection downstream.
