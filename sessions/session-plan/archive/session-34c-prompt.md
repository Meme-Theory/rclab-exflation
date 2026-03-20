# Session 34c: Thouless Criterion Under D_phys — The Final BCS Gate

**Date**: 2026-03-06
**Mode**: compute
**Depends on**: Session 34b complete, RPA-34a not CHALLENGE
**Source plan**: `sessions/session-plan/session-34-plan.md`
**Prerequisite**: `tier0-computation/s34b_dphys_kosmann.npz` and `tier0-computation/s34a_dphys_fold.npz` must exist. Read `tier0-computation/s34a_gate_verdicts.txt` and `tier0-computation/s34b_gate_verdicts.txt` to confirm all prior gates PASS.

This is Wave 3 of 3. The decisive gate: does M_max > 1 survive under the physical Dirac operator?

---

## AGENT ASSIGNMENTS

| Agent | Type | Role | Computation |
|:------|:-----|:-----|:------------|
| bap | baptista-spacetime-analyst | Computation | 34a-3: Thouless criterion under D_phys |
| coord | gen-physicist | Coordination | Gate classification, final synthesis, constraint map update |

---

## REQUIRED READING (LEAN)

### All agents
- `tier0-computation/s34a_gate_verdicts.txt` — DPHYS-34a-1, TRAP1-34a verdicts
- `tier0-computation/s34b_gate_verdicts.txt` — RPA-34a verdict, Kosmann diagnostic

### bap (baptista)
- `tier0-computation/s33b_trap1_wall_bcs.py` — template for Thouless computation (lines 214-249: Thouless matrix, lines 260-310: self-consistent BdG)
- `sessions/session-34/session-34a-synthesis.md` — 34a fold survival details

### coord
- `sessions/session-plan/session-34-plan.md` — Section VIII (W1 predictions table) for final assessment
- `tier0-computation/s33b_gate_verdicts.txt` — TRAP-33b baseline (M_max = 2.062) for comparison

---

## PRE-SESSION GATE CHECK (MANDATORY FIRST ACTION)

Before any computation:
1. Read `tier0-computation/s34a_gate_verdicts.txt` — confirm DPHYS-34a-1 = PASS
2. Read `tier0-computation/s34b_gate_verdicts.txt` — confirm RPA-34a = CONSISTENT (or at minimum not CHALLENGE)
3. Verify `s34a_dphys_fold.npz`, `s34b_dphys_kosmann.npz`, `s32b_wall_dos.npz` all load
4. If any prerequisite fails, STOP and report

---

## COMPUTATION 34a-3: Thouless Criterion Under D_phys [EXISTENTIAL]

**Agent**: bap
**Priority**: P0 (the decisive gate for inner fluctuation survival)

**What**: Compute M_max under D_phys — the maximum eigenvalue of the Thouless matrix M_nm = V_nm(phi) * rho_m / (2|xi_m(phi)|) using D_phys eigenvalues, D_phys eigenspinors, and the rotated Kosmann kernel from Waves 1 and 2.

The wall DOS rho_m from W-32b is UNCHANGED by phi (wall structure set by spatial Turing pattern, depends on spectral action curvature not eigenspinors). The computation uses the BARE wall DOS as the conservative choice.

**Method**:
1. Load D_phys eigenvalues from `s34a_dphys_fold.npz` at the fold location.
2. Load rotated Kosmann kernel V_nm(phi) from `s34b_dphys_kosmann.npz` at same phi_VEV.
3. Load wall DOS from `s32b_wall_dos.npz`.
4. At each phi_VEV, construct the Thouless matrix in the B1+B2 subspace (5x5, same procedure as `s33b_trap1_wall_bcs.py` lines 214-249, substituting D_phys data).
5. Compute M_max = max eigenvalue of Thouless matrix.
6. Run full self-consistent BdG (4x4 in B2 only) if M_max > 1, to get Delta_max(phi).
7. Repeat for all 3 wall configurations (Wall 0, 1, 2).
8. Sweep phi_VEV from 0 to 0.20. Produce M_max(phi_VEV) curve.
9. Identify phi_c where M_max = 1 (the BCS destruction threshold), if it exists.

**Three regimes to test**:
1. |phi_VEV| = 0 — MUST reproduce TRAP-33b M_max = 2.062 (cross-check)
2. |phi_VEV| = gap_{B2-B3} = 0.07 — the gate fires here
3. |phi_VEV| = 2*gap = 0.14 — stress test

**DATA KEYS**:
- From `s34a_dphys_fold.npz`: D_phys eigenvalues at each (tau, phi_VEV) — for |xi_m(phi)|
- From `s34b_dphys_kosmann.npz`: V_nm(phi) at each phi_VEV — the rotated pairing kernel
- From `s32b_wall_dos.npz`:
  - `wall_{w}_B2_{i}_rho` — DOS at wall w, B2 mode i
  - `wall_{w}_B2_{i}_overlap` — eigenvector overlap with wall profile
  - `wall_{w}_B2_{i}_trapped` — trapping verdict per mode
- From `s33b_trap1_wall_bcs.npz` (for cross-check at phi=0):
  - `primary_M_max` = 2.062
  - `V_5x5_full` — bare Thouless matrix
  - `impedance_factor` = 1.56

**MANDATORY CROSS-CHECK**: At phi=0, M_max must reproduce 2.062 (TRAP-33b). If discrepancy > 1%, STOP and debug.

**Script**: `tier0-computation/s34c_dphys_thouless.py` (~250 lines)
**Output**: `tier0-computation/s34c_dphys_thouless.{py,npz,png}`
**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`

**Gate DPHYS-34a-3** (pre-registered, EXISTENTIAL):
- **PASS**: M_max > 1.0 at |phi_VEV| = gap = 0.07 for at least one wall config
- **STRONG PASS**: M_max > 1.0 at |phi_VEV| = 2*gap = 0.14 for all three walls
- **FAIL**: M_max < 1.0 at |phi_VEV| = gap for ALL wall configurations

**If PASS**: Mechanism chain survives inner fluctuations. The 5-link chain (I-1 -> RPA-32b -> U-32a -> W-32b -> TRAP-33b) is physically valid under D_phys.

**If FAIL**: BCS link CLOSED under D_phys. Mechanism chain valid for bare D_K only — physically incomplete. Record phi_c (the critical phi where M_max crosses 1) and characterize the transition.

---

## CONSTRAINT GATES SUMMARY

| ID | Type | Condition | Fires If | Consequence |
|:---|:-----|:----------|:---------|:------------|
| DPHYS-34a-3 | Existential | M_max > 1.0 at phi=gap for >= 1 wall | M_max < 1.0 for all walls | BCS CLOSED under D_phys |

---

## SYNTHESIS & OUTPUT

**Designated writer**: coord
**Gate verdicts file**: `tier0-computation/s34c_gate_verdicts.txt`
**Final synthesis**: `sessions/session-34/session-34c-synthesis.md`

The final synthesis must contain:
1. **Session 34 overview** — all 3 waves, all gates, full conditional chain outcome
2. **DPHYS-34a-3 result** — M_max(phi_VEV) curve, wall-by-wall results, phi_c identification
3. **W1 predictions tested** — table from session-34-plan.md Section VIII, each prediction vs actual result
4. **Aggregate D_phys assessment** — does the mechanism chain survive inner fluctuations?
5. **Constraint map update** — updated chain status, new closures or survivals
6. **What remains** — next gates (null hypothesis SU(2)xSU(2), thick-wall Coleman bounce, self-consistent phi_VEV)
7. **Files created across all 3 waves** — complete paths

The gate verdicts file format:
```
DPHYS-34a-3: [PASS/STRONG PASS/FAIL] -- M_max = [value] at phi = [value] for Wall [N]. [One-line justification.]
```

---

## OPERATIONAL RULES

- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Output directory: `tier0-computation/`
- Script prefix: `s34c_`
- NUMBERS first. Gate classification second. Interpretation third.
- Check inbox between computation blocks.
