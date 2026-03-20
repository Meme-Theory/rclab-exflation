# Session 34a: D_phys Fold Survival + Trap 1 Re-evaluation

**Date**: 2026-03-06
**Mode**: compute
**Depends on**: Session 33b complete (TRAP-33b PASS, M_max = 2.062)
**Source plan**: `sessions/session-plan/session-34-plan.md`

This is Wave 1 of 3. Two independent computations run in parallel. If DPHYS-34a-1 FAILS, Waves 2 and 3 are cancelled — mechanism chain CLOSED at D_phys level.

---

## AGENT ASSIGNMENTS

| Agent | Type | Role | Computation |
|:------|:-----|:-----|:------------|
| bap | baptista-spacetime-analyst | Computation | 34a-1: D_phys fold survival |
| connes | connes-ncg-theorist | Computation | 34a-4: Trap 1 re-evaluation with full kernel |
| coord | gen-physicist | Coordination | Gate classification, verdict file |

---

## REQUIRED READING (LEAN — max 4 files per agent)

### All agents
- `tier0-computation/s33b_gate_verdicts.txt` — confirms TRAP-33b PASS baseline

### bap (baptista)
- `sessions/session-33/session-33-connes-collab.md` — eq 15: eigenvector rotation formula for first-order phi correction
- `tier0-computation/tier1_dirac_spectrum.py` — Dirac infrastructure (su3_generators, structure_constants, metric, spin connection)

### connes
- `sessions/session-33/session-33-connes-collab.md` — eq 3: branching rule, eq 18: cyclic cohomology interpretation

### coord
- `sessions/session-plan/session-34-plan.md` — Section IV (gate conditions) and Section VIII (W1 predictions to test)

---

## COMPUTATION 34a-1: D_phys Construction and Fold Survival [EXISTENTIAL]

**Agent**: bap
**Priority**: P0 (7/7 unanimous, blocks everything)

**What**: Construct D_phys = D_K + phi + J*phi*J^{-1} in the singlet Peter-Weyl sector. Determine whether the B2 eigenvalue fold at tau ~ 0.190 survives inner fluctuations.

The inner fluctuation phi = sum_i a_i[D_K, b_i] with a_i, b_i in A_F = C + H + M_3(C) introduces off-diagonal terms that mix U(2) branches (B1, B2, B3). W1 classifies the fold as A_2 catastrophe with destruction bound 0.42.

**Method**:
1. Load bare D_K eigenvectors from `s23a_kosmann_singlet.npz` at tau_idx=3 (tau=0.190 region, interpolate between tau=0.15 and tau=0.20).
2. Construct the algebra A_F = C + H + M_3(C) action on H_F = C^{16}. C acts as scalar, H as 2x2 blocks on (nu_R, e_R) doublet, M_3(C) as 3x3 blocks on color indices.
3. Compute phi = sum_i a_i[D_K, b_i] for each independent generator b_i of A_F. In the eigenspinor basis: [D_K, b_i]_{nm} = (lambda_n - lambda_m) * <psi_n|b_i|psi_m>.
4. Identify the WORST CASE phi direction (maximally perturbs B2 branch).
5. Construct D_phys = D_K + phi + J*phi*J^{-1} as a 16x16 matrix.
6. Diagonalize. Extract 8 positive eigenvalues. Identify B2-analog branch.
7. Repeat at tau = 0.15, 0.20, 0.25. Locate B2 minimum under D_phys.
8. Sweep |phi_VEV| from 0 to 0.20. Record: fold location tau_min(phi), fold curvature d2(phi), B2 splitting delta_split(phi), minimum eigenvalue lambda_min(phi).

**MANDATORY CROSS-CHECKS** (built into script):
- At phi=0: D_phys eigenvalues must reproduce D_K eigenvalues exactly
- At small phi: delta_lambda_n = <n|phi|n> + O(phi^2) must match perturbation theory

**DATA KEYS in `s23a_kosmann_singlet.npz`**:
- `eigenvectors_{tau_idx}` — shape 16x16, columns are eigenspinors
- `eigenvalues_{tau_idx}` — shape 16, full eigenvalues
- `eigenvalues_singlet_{tau_idx}` — shape 16, singlet sector
- `tau_values` — array of 9 tau values
- `A_antisym_{tau_idx}_{gen}` — antisymmetrized algebra action matrices (tau_idx 0-8, gen 0-7)

**Script**: `tier0-computation/s34a_dphys_fold.py` (~350 lines)
**Output**: `tier0-computation/s34a_dphys_fold.{py,npz,png}`
**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`

**Gate DPHYS-34a-1** (pre-registered):
- **PASS**: B2 fold persists (d2 > 0 at some tau in [0.14, 0.24]) at |phi_VEV| = gap_{B2-B3} = 0.07
- **STRONG PASS**: Fold persists up to |phi_VEV| = 2*gap = 0.14
- **FAIL**: Fold destroyed (d2 <= 0 everywhere in [0.14, 0.24]) at |phi_VEV| = gap_{B2-B3}

**If FAIL**: Mechanism chain CLOSED at D_phys level. No van Hove singularity, no enhanced DOS, no pairing threshold crossing. Waves 2 and 3 cancelled.

---

## COMPUTATION 34a-4: Trap 1 Re-evaluation With Full Kernel [STRUCTURAL]

**Agent**: connes
**Priority**: P1 (independent of 34a-1, runs in parallel)

**What**: Re-evaluate Trap 1 (V(gap,gap) = 0 at exact gap edge) with the FULL 8-generator Kosmann kernel. Session 23a established Trap 1 using only C^2 generators. The K-1e retraction (Session 33b) showed V(B2,B2) = 0.287 with the full kernel. But Trap 1 concerns a DIFFERENT quantity: the pairing matrix element at the EXACT gap boundary (where one eigenvalue crosses zero), not the B2 branch interior.

If V(gap,gap) = 0 with the full kernel, the gap-edge divergence M ~ V/|xi| is regulated and Trap 1 remains. If V(gap,gap) != 0, the gap edge becomes a STRONGER pairing site.

**Method**:
1. Load gap-edge modes at each tau from `s23a_kosmann_singlet.npz`.
2. Extract the full 8-generator Kosmann matrix elements at gap-edge modes.
3. Compute V(gap,gap) = sum_{a=0}^7 |<gap|K_a|gap>|^2 using ALL 8 generators.
4. If V(gap,gap) != 0, decompose by generator type (C^2: a=3-6, SU(2): a=0-2, U(1): a=7).
5. Check across all 9 tau values.

**DATA KEYS in `s23a_kosmann_singlet.npz`**:
- `gap_edge_indices_{tau_idx}` — indices of gap-edge modes at each tau
- `K_a_matrix_{tau_idx}_{a}` — Kosmann matrices (tau_idx 0-8, generator a 0-7), shape 16x16
- `eigenvectors_{tau_idx}` — eigenspinor basis
- `eigenvalues_singlet_{tau_idx}` — eigenvalues (to identify gap edge)

**Script**: `tier0-computation/s34a_trap1_reeval.py` (~120 lines)
**Output**: `tier0-computation/s34a_trap1_reeval.{py,npz}`
**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`

**Gate TRAP1-34a** (pre-registered):
- **CONFIRMED**: V(gap,gap) = 0 (to ~1e-14) with full kernel at all tau. Trap 1 remains.
- **BROKEN**: V(gap,gap) > 0.01 with full kernel. Trap 1 RETRACTED. Gap edge becomes additional pairing channel (STRENGTHENS BCS).

---

## CONSTRAINT GATES SUMMARY

| ID | Type | Condition | Fires If | Consequence |
|:---|:-----|:----------|:---------|:------------|
| DPHYS-34a-1 | Existential | B2 fold d2 > 0 in [0.14, 0.24] at phi=gap | d2 <= 0 everywhere | Mechanism chain CLOSED at D_phys |
| TRAP1-34a | Structural | V(gap,gap) = 0 to machine precision | V(gap,gap) > 0.01 | Trap 1 RETRACTED (strengthens BCS) |

---

## SYNTHESIS & OUTPUT

**Designated writer**: coord
**Gate verdicts file**: `tier0-computation/s34a_gate_verdicts.txt`
**Synthesis file**: `sessions/session-34/session-34a-synthesis.md`

Coord classifies both gates against pre-registered criteria. Records verdicts. If DPHYS-34a-1 FAIL, writes closure assessment and session ends. If PASS, writes interim synthesis and notes readiness for Wave 2 (session-34b).

---

## OPERATIONAL RULES

- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Output directory: `tier0-computation/`
- Script prefix: `s34a_`
- NUMBERS first. Gate classification second. Interpretation third.
- Check inbox between computation blocks.
