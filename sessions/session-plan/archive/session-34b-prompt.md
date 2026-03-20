# Session 34b: Kosmann Reprojection + RPA Curvature Under D_phys

**Date**: 2026-03-06
**Mode**: compute
**Depends on**: Session 34a complete, DPHYS-34a-1 = PASS
**Source plan**: `sessions/session-plan/session-34-plan.md`
**Prerequisite**: `tier0-computation/s34a_dphys_fold.npz` must exist. Read `tier0-computation/s34a_gate_verdicts.txt` to confirm DPHYS-34a-1 PASS before ANY computation.

This is Wave 2 of 3. Two computations that depend on 34a-1 output. Both feed into Wave 3 (Thouless criterion).

---

## AGENT ASSIGNMENTS

| Agent | Type | Role | Computation |
|:------|:-----|:-----|:------------|
| bap | baptista-spacetime-analyst | Computation | 34a-2: Kosmann kernel under D_phys eigenspinors |
| sim | phonon-exflation-sim | Computation | 34a-5: RPA spectral action curvature under D_phys |
| coord | gen-physicist | Coordination | Gate classification, verdict file |

---

## REQUIRED READING (LEAN)

### All agents
- `tier0-computation/s34a_gate_verdicts.txt` — MUST confirm DPHYS-34a-1 PASS before computing
- `sessions/session-34/session-34a-synthesis.md` — 34a results summary

### bap (baptista)
- `tier0-computation/s33b_trap1_wall_bcs.py` — lines 214-249: Thouless matrix construction template (for context on what 34a-2 feeds into)

### sim (phonon-exflation-sim)
- `tier0-computation/s32b_rpa1_thouless.npz` — bare curvature baseline (key: `bare_curvature` = 20.43)

---

## PRE-SESSION GATE CHECK (MANDATORY FIRST ACTION)

Before any computation:
1. Read `tier0-computation/s34a_gate_verdicts.txt` — confirm DPHYS-34a-1 = PASS
2. Verify `tier0-computation/s34a_dphys_fold.npz` exists and loads correctly
3. If DPHYS-34a-1 = FAIL or data missing, STOP and report

---

## COMPUTATION 34a-2: Kosmann Kernel Under D_phys Eigenspinors [10-15 min]

**Agent**: bap
**Priority**: P0 (feeds directly into 34a-3 Thouless criterion in Wave 3)

**What**: Recompute the Kosmann pairing kernel V_nm = sum_{a=0}^{7} |<psi_n(phi)|K_a|psi_m(phi)>|^2 using the D_phys eigenspinors from 34a-1. The K_a matrices are UNCHANGED (properties of the isometry algebra). What changes is the BASIS: D_phys eigenspinors rotate under phi, mixing branches.

Critical question: does V(B2,B2) remain nonzero and large enough for BCS when B2 eigenspinors acquire B3/B1 admixture from phi?

**Method**:
1. Load D_phys eigenspinors from `s34a_dphys_fold.npz` at the natural phi scale (|phi_VEV| = gap = 0.07) and at the fold location.
2. Load the 8 Kosmann matrices K_a from `s23a_kosmann_singlet.npz`.
3. Project K_a into the D_phys eigenspinor basis: K_a_nm(phi) = <psi_n(phi)|K_a|psi_m(phi)>.
4. Compute V_nm(phi) = sum_{a=0}^7 |K_a_nm(phi)|^2.
5. Extract V(B2,B2)(phi), V(B1,B2)(phi), V(B3,B2)(phi) where B2 labels D_phys eigenstates closest to original B2 cluster.
6. Decompose V(B2,B2)(phi) by generator type: C^2 (a=3-6), SU(2) (a=0-2), U(1) (a=7).
7. Sweep |phi_VEV| from 0 to 0.14. Track V(B2,B2)(phi_VEV) and decomposition.

**DATA KEYS**:
- From `s34a_dphys_fold.npz`: D_phys eigenvectors and eigenvalues at each (tau, phi_VEV) — check keys after loading
- From `s23a_kosmann_singlet.npz`:
  - `K_a_matrix_{tau_idx}_{a}` — 16x16 Kosmann matrices (tau 0-8, gen 0-7)
  - `eigenvectors_{tau_idx}` — bare eigenspinors (for cross-check at phi=0)

**MANDATORY CROSS-CHECK**: At phi=0, V_nm(phi=0) must reproduce the bare Kosmann kernel from Session 23a. Specifically V(B2,B2)(0) should match `V_pairing_{tau_idx}` restricted to B2 indices.

**Script**: `tier0-computation/s34b_dphys_kosmann.py` (~200 lines)
**Output**: `tier0-computation/s34b_dphys_kosmann.{py,npz,png}`
**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`

**Diagnostic** (not standalone gate — feeds 34a-3):
- V(B2,B2)(phi) > 0.15: substantial pairing survives
- V(B2,B2)(phi) < 0.05: pairing severely suppressed (Thouless unlikely to pass)

---

## COMPUTATION 34a-5: RPA Spectral Action Curvature Under D_phys [5 min]

**Agent**: sim
**Priority**: P0 (structural companion — if fold survives but curvature collapses, Turing link fails)

**What**: Recompute the spectral action curvature d^2(sum|lambda_k(phi)|)/dtau^2 at the dump point using D_phys eigenvalues. The bare RPA-32b result is 20.43 with threshold 0.54 (margin 38x). W1 predicts this margin is implausible to overturn. This computation tests that claim directly.

**Method**:
1. Load D_phys eigenvalues across the tau grid from `s34a_dphys_fold.npz`.
2. At each phi_VEV, compute sum|lambda_k(phi, tau)| at each tau.
3. Fit a quadratic around the dump point (tau ~ 0.19) to extract d^2(sum|lambda|)/dtau^2.
4. Compare to bare value 20.43 (from `s32b_rpa1_thouless.npz`, key: `bare_curvature`).
5. Sweep phi_VEV from 0 to 0.14.
6. Compute the RPA correction factor: chi(phi)/chi(bare).

**DATA KEYS**:
- From `s34a_dphys_fold.npz`: D_phys eigenvalues at each (tau, phi_VEV) grid point
- From `s32b_rpa1_thouless.npz`: `bare_curvature` = 20.43, `chi_pass_threshold` = 0.54, `d2S_abs`, `d2S_trace`

**Script**: `tier0-computation/s34b_rpa_curvature.py` (~120 lines)
**Output**: `tier0-computation/s34b_rpa_curvature.{py,npz,png}`
**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`

**Gate RPA-34a** (diagnostic):
- **CONSISTENT**: d^2(sum|lambda|)/dtau^2 > 0.54 at |phi_VEV| = gap = 0.07 (RPA survives)
- **CHALLENGE**: curvature < 0.54 (RPA FAILS — closes Turing link U-32a under D_phys)

---

## CONSTRAINT GATES SUMMARY

| ID | Type | Condition | Fires If | Consequence |
|:---|:-----|:----------|:---------|:------------|
| RPA-34a | Diagnostic | d^2(sum\|lambda\|)/dtau^2 > 0.54 at phi=gap | Curvature < 0.54 | Turing link U-32a CLOSED under D_phys |

(34a-2 Kosmann result is a diagnostic feeding Wave 3, not a standalone gate.)

---

## SYNTHESIS & OUTPUT

**Designated writer**: coord
**Gate verdicts file**: `tier0-computation/s34b_gate_verdicts.txt`
**Synthesis addendum**: append to `sessions/session-34/session-34a-synthesis.md` or create `sessions/session-34/session-34b-synthesis.md`

Coord classifies RPA-34a, records Kosmann kernel diagnostic, assesses readiness for Wave 3 (session-34c: Thouless criterion). If RPA-34a = CHALLENGE, this is a major unexpected result that the user must evaluate before proceeding.

---

## OPERATIONAL RULES

- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Output directory: `tier0-computation/`
- Script prefix: `s34b_`
- NUMBERS first. Gate classification second. Interpretation third.
- Check inbox between computation blocks.
