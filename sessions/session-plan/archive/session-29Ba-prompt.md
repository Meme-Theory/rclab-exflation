# Session 29Ba: 3-Sector Depth + PMNS Extraction

**Date**: 2026-02-28
**Author**: Team-lead (decomposed from 29B plan)
**Depends on**: Session 28 (all sub-sessions). Does NOT depend on Session 29A — all three computations are 29A-independent.
**Input data**:
- `tier0-computation/s27_multisector_bcs.npz` (F_cond[9 sectors, 9 tau, 12 mu])
- `tier0-computation/s28b_hessian.npz` (Hessian eigenvalues at minima)
- `tier0-computation/s23a_kosmann_singlet.npz` (V_pairing matrices and eigenvalues at 9 tau values)
- `tier0-computation/s24a_eigenvalue_ratios.npz` (singlet eigenvalue structure)
- `tier0-computation/s24a_vspec.npz` (spectral potential V_spec(tau))

## Motivation

Session 29B addresses the **five fusion priorities that 29A deliberately omits**. This first sub-session tackles the three computations that have NO dependency on 29A results and can run immediately — potentially in parallel with late-stage 29A:

1. **29B-1**: Does the BCS stabilization survive restriction to only the 3 permanently supercritical sectors? (The L-8 divergence question.)
2. **29B-6**: Does the 3-sector gradient balance B-1 hold? (Downstream of 29B-1.)
3. **29B-2**: Does the tridiagonal Kosmann structure reproduce the PMNS mixing angles? (The last particle physics gate.)

All three produce results with **standalone mathematical value** regardless of the KC-3 verdict from 29A.

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s29b_`

## PRE-SESSION GATE

Before any computation, verify that all input data files are intact and accessible. Load each .npz, verify key names, print array shapes. If ANY file is missing or corrupted, STOP and report.

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 28 fusion synthesis**: `sessions/session-28/session-28-fusion-synthesis.md` — Section III (Constraint Chain status), Section IV (XS-6: 3-sector identification), Section VIII (unified priorities).
2. **Session 29B plan**: `sessions/session-plan/session-29B-plan.md` — Section III (29B-1, 29B-2, 29B-6 computation specs), Section V (gate structure).
3. **Session 23a synthesis**: `sessions/session-23/session-23a-synthesis.md` — Kosmann singlet results, tridiagonal selection rules, V(gap,gap) = 0 selection rule.
4. **MathVariables**: `sessions/framework/MathVariables.md` — Section 4 (BCS variables), Section 5 (neutrino variables).
5. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:-------------------|
| phonon-exflation-sim | `tier0-computation/s27_multisector_bcs.py` (multi-sector BCS infrastructure), `tier0-computation/s24a_neutrino.py` (existing neutrino computation to extend) |
| neutrino-detection-specialist | `researchers/Neutrino/index.md` — PDG mixing angle values, PMNS parametrization conventions |
| coordinator | This prompt Section III (gate conditions). Memorize ALL thresholds before first computation completes |

---

# II. COMPUTATIONS

## 29B-1: 3-Sector F_BCS^{eff} [ZERO-COST, POTENTIAL CLOSURE]

**Fusion Priority**: 3 (elevated from no team synthesis's top 3 through fusion deliberation, XS-6)
**Dependency**: None — runs from existing s27/s28 data

**What**: Restrict the BCS free energy to the 3 permanently supercritical sectors identified by the LZ retraction (Synthesis D, Section 1.5):
- **(3,0)**: multiplicity 100, first-order (L-9, c = 0.00552)
- **(0,3)**: multiplicity 100, first-order (L-9, c = 0.00723)
- **(0,0)**: multiplicity 16 (Spin(8) spinor), always supercritical at mu = lambda_min

Compute:
$$F_{BCS}^{3\text{-sector}}(\tau, \mu) = \sum_{r \in \{(3,0),(0,3),(0,0)\}} \text{mult}(r) \cdot F_{\text{cond}}^{(r)}(\tau, \mu)$$

**Why this matters**: The full-sector F_total from `s27_multisector_bcs.npz` includes re-entrant sectors ((2,0), (0,2), (1,1), (2,1), etc.) that dissolve at second-order boundaries. If stabilization depends on sectors that dissolve, the mechanism is structurally unsound. The 3-sector restriction tests whether the permanently supercritical sectors alone satisfy the B-3 depth condition.

**Critical finding from agent research**: At mu/lambda_min = 1.20 (the S-3 interior minimum), F_3sect = -17.22 vs F_total = -18.56 (**93% of total** — load-bearing sectors dominate). But at mu/lambda_min = 1.50 (deepest Hessian-confirmed minimum), F_3sect = -3.72 vs F_total = -43.55 (**only 8.5%** — re-entrant sectors dominate at deeper mu). The 3-sector minimum may be at a DIFFERENT (tau, mu) location than the full-sector minimum.

**Method**:
1. Load `s27_multisector_bcs.npz` — extract F_cond for sectors (3,0) = idx 6, (0,3) = idx 7, (0,0) = idx 0
2. Apply multiplicities: 100, 100, 16 respectively
3. Sum across 3 sectors for each (tau, mu) grid point
4. Locate minimum of F_BCS^{3-sector} on the (tau, mu) grid
5. Compute 2D Hessian at the minimum via finite differences
6. Check both Hessian eigenvalues positive (genuine minimum)

**Gate condition**: |F_BCS^{3-sector}(tau_0)| > (G_{tau,tau}/2) * (dtau/dt)^2 at the 3-sector minimum. With G_{tau,tau} = 5 and dtau/dt ~ 0.2: threshold = 0.1. F_3sect = -17.22 at mu/lmin = 1.20 comfortably exceeds this. But the 3-sector Hessian must confirm this is a genuine minimum (both eigenvalues positive).

**Constraint Condition (B-29a)**: If F_BCS^{3-sector} < threshold at ALL (tau, mu) grid points, stabilization requires re-entrant sectors and the L-8 divergence problem returns. Framework structurally weakened (not closed, but weakened).

**Inputs**: `s27_multisector_bcs.npz`, `s28b_hessian.npz` (reference)

**Script**: `s29b_3sector_fbcs.py` — new, ~50 lines. Read s27 data, index sectors, apply multiplicities, sum, locate minimum, Hessian, check B-3.

**Computational cost**: < 1 minute. Pure numpy post-processing.

**Agent**: phonon-exflation-sim

**Output**: `s29b_3sector_fbcs.npz`

---

## 29B-6: 3-Sector Gradient Balance (B-1 Check) [ZERO-COST, DOWNSTREAM OF 29B-1]

**Fusion Priority**: Embedded in XS-8 (Lambda_crit ~ 3 estimate)
**Dependency**: Requires 29B-1 output (3-sector F_BCS)

**What**: Verify the gradient balance B-1 for the 3-sector potential:

$$S_b'(\tau_0) + F_{BCS}^{3\text{-sector}'}(\tau_0) = 0$$

The fusion's XS-8 computed Lambda_crit ~ 3.0 using full-sector F_BCS''. With 3-sector restriction, Lambda_crit may shift.

**Method**:
1. Load F_BCS^{3-sector}(tau) from 29B-1 output
2. Load S_b(tau) from `s24a_vspec.npz`
3. Compute finite-difference derivatives: F_BCS'(tau) and S_b'(tau)
4. Find tau_0 where F_BCS'(tau_0) + S_b'(tau_0) = 0
5. Compute Lambda_crit_3sect and compare to full-sector Lambda_crit
6. Report delta_tau = |tau_0^{3-sector} - tau_0^{full-sector}|

**Gate condition (P-29a extension)**: tau_0 exists in [0.20, 0.50] with Lambda_crit = O(1). If satisfied: natural stabilization at compactification scale with only permanently supercritical sectors.

**Inputs**: Output of 29B-1, `s24a_vspec.npz`

**Computational cost**: < 1 minute. Pure post-processing.

**Agent**: phonon-exflation-sim

**Output**: Included in `s29b_3sector_fbcs.npz` (add gradient balance fields to the same output file)

---

## 29B-2: Tridiagonal PMNS Extraction [LOW COST, LAST PARTICLE PHYSICS GATE]

**Fusion Priority**: 4 (last surviving particle physics test; UV-safe)
**Dependency**: Standalone — independent of KC-3 verdict. Uses 29A tau(t) trajectory only to determine which tau value is physical (but can run at all 9 tau values without 29A).

**What**: Extract the full 3x3 PMNS mixing matrix from the tridiagonal Kosmann kernel in the (0,0) singlet sector. The tridiagonal selection rules measured in Session 23a are:
- V(L1, L2) = 0.07-0.13 (nearest-neighbor coupling)
- V(L1, L3) = 0 EXACTLY (next-nearest = zero, selection rule)
- V(L2, L3) = 0.01-0.03 (nearest-neighbor coupling)

The effective mass matrix H_eff = diag(E_1, E_2, E_3) + V_pairing is tridiagonal. Its eigenvectors U define the PMNS matrix.

**Existing infrastructure**:
- `s24a_neutrino.py`: computes R and theta_12 from H_eff. Needs extension to full 3x3 PMNS.
- `s23a_kosmann_singlet.npz`: V_pairing matrices and eigenvalues at 9 tau values
- `s23a_gap_equation.npz`: BCS gap for mode-dependent extension
- `s24a_eigenvalue_ratios.npz`: confirmed zero phi crossings in singlet; 16 eigenvalues split 2+8+6

**R_BCS = R_bare theorem** (Team Synthesis C, Section III.1): Under uniform BCS gap, Delta^2 cancels in mass-squared ratios. R = 5.68 is **independent of BCS dressing**. PMNS angles are the ONLY remaining neutrino test.

**Method**:
1. Load H_eff = diag(lambda_1, lambda_2, lambda_3) + V_tridiagonal from `s23a_kosmann_singlet.npz`
2. Diagonalize at tau = 0.15, 0.25, 0.35: H_eff U = U diag(m_1, m_2, m_3)
3. Extract PMNS angles:
   - sin^2(theta_13) = |U_{e3}|^2
   - tan^2(theta_12) = |U_{e2}|^2 / |U_{e1}|^2
   - tan^2(theta_23) = |U_{mu3}|^2 / |U_{tau3}|^2
4. (Optional) Extract delta_CP from the Jarlskog invariant: J = Im(U_{e1} U_{mu2} U_{e2}* U_{mu1}*)
5. Compare to PDG values at each tau

**Gate condition (P-29b)**: sin^2(theta_13) in [0.015, 0.030] (PDG: 0.0218 ± 0.0007). theta_12 in [28, 38] degrees (PDG: 33.44 ± 0.77).

**Constraint Condition (B-29b)**: If sin^2(theta_13) < 0.005 or > 0.10, the tridiagonal structure fails to reproduce the reactor angle. The particle physics prediction program is fully closed.

**Extension — mode-resolved BdG**: If the 3x3 PMNS from uniform-gap H_eff fails, the escape route is a mode-dependent gap Delta_n from solving the full BdG equation within (0,0) with the tridiagonal V_{nm}. This tests whether non-uniform dressing shifts theta_13 toward the measured value.

**Inputs**: `s23a_kosmann_singlet.npz`, `s24a_eigenvalue_ratios.npz`

**Script**: `s29b_pmns_extraction.py` — extend `s24a_neutrino.py` with full 3x3 eigenvector extraction. ~80 additional lines.

**Computational cost**: < 2 minutes. 3x3 diagonalization at 9 tau values.

**Agent**: phonon-exflation-sim (computation), neutrino-detection-specialist (physics context)

**Output**: `s29b_pmns_extraction.npz`

---

# III. CONSTRAINT CONDITIONS AND GATE STRUCTURE

## Hard Closes

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-29a | F_BCS^{3-sector} < 0.1 at ALL (tau, mu) | Load-bearing sectors alone cannot stabilize. Re-entrant sectors required. L-8 divergence problem returns. |
| B-29b | sin^2(theta_13) < 0.005 or > 0.10 | Tridiagonal PMNS fails. Particle physics prediction program fully closed. |

## Positive Signals

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-29a | F_3sect > 0.1 with genuine minimum (both Hessian eigenvalues > 0) | 3-sector stabilization confirmed. L-8 evaporated for stabilization. |
| P-29b | sin^2(theta_13) in [0.015, 0.030] | First BCS-era particle physics PASS. Framework has a surviving prediction. |

---

# IV. OUTPUT FILES

| Computation | Output .npz | Output .py | Gate Verdict |
|:------------|:-----------|:-----------|:-------------|
| 29B-1 + 29B-6 | `s29b_3sector_fbcs.npz` | `s29b_3sector_fbcs.py` | B-3 depth + gradient balance (3-sector) |
| 29B-2 | `s29b_pmns_extraction.npz` | `s29b_pmns_extraction.py` | sin^2(theta_13) gate |

Gate verdicts appended to: `tier0-computation/s29b_gate_verdicts.txt`

---

# V. SUCCESS CRITERIA

Session 29Ba is successful if it produces:

1. **A definitive 3-sector depth verdict** — F_BCS^{3-sector} sufficient or insufficient for B-3, with Hessian confirmation of genuine minimum
2. **A 3-sector gradient balance** — tau_0 location and Lambda_crit for the restricted potential
3. **PMNS mixing angles** — sin^2(theta_13), theta_12, theta_23 at tau = 0.15, 0.25, and 0.35, compared to PDG values

These results stand independently of the 29A verdict and have publishable mathematical value (JGP/CMP level) even in the worst-case KC-3 FAIL scenario.

---

*Prompt decomposed from Session 29B Plan (Section III: 29B-1, 29B-2, 29B-6). Computation order: 29B-1 → 29B-6 (sequential chain), then 29B-2 (independent). All zero-cost or low-cost. Total runtime: < 10 minutes.*
