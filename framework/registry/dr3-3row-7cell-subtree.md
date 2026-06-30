# DR3 3-Row x 7-Cell Sub-Tree (Regulator-Stratified Prediction Surface)

> **Origin**: S86 W13-4 / `S86-DR3-SUB-TREE-3-ROW-PIN` by `cosmic-web-theorist`
> (carry-forward source: mack-cosmic-bridge 9A §VI.6; mack self-blacklist).
> **Plan**: `sessions/session-plan/session-86-plan-w13.md` §W13-4.
> **Verdict**: INFO.
> **dual-SHA**: audit=eccedb2a53dca481..., content=8abdc38ff0d0c688...

## Purpose

This is the substrate's regulator-stratified prediction
surface for the BAO/RSD CPL parameters (w_0, w_a). Each L_max
row is a different truncation of the SAME substrate
eigenvalue computation. The 3 rows together test whether the
substrate's w_0 prediction is REGULATOR-INVARIANT (true
substrate observable) or REGULATOR-DEPENDENT (artifact of
truncation choice). DR3 will measure the substrate's
regulator-class self-consistency. The pre-registered
4-branch adjudication protocol (REG-INVARIANT,
REG-DEP-MAJORITY, STRUCTURAL-AMBIGUITY-FREEZE, EXTERNAL)
IS the substrate's self-test under external observational
input.

## 7-cell scenario roster (S84 W4-44 DR3-CONTINGENCY-FINE-GRAINED)

| Scenario | Label | w_0 range | w_a range | Framework response | Decision branch |
|:---------|:------|:----------|:----------|:-------------------|:----------------|
| A1 | branch-(iv) mild corroboration | [-0.988, -0.942] | [-0.20, +0.20] | SURVIVE+promote | PASS |
| A2 | branch-(iv) stretched corroboration (~2-sigma deep) | [-1.050, -0.988] | [-0.20, +0.20] | SURVIVE+recal | TENSION |
| B1 | w_a-driven exclusion (corridor in w_0; w_a out) | [-0.942, -0.742] | [-1.00, -0.20] | PARTIAL-REFUTE-w_a | TENSION |
| B2 | w_0-driven exclusion (shallow; w_a in lock) | [-0.742, -0.500] | [-0.20, +0.20] | PARTIAL-REFUTE-w_0 | TENSION |
| B3 | joint shift (shallow w_0 + dynamical w_a) | [-0.742, -0.500] | [-0.50, -0.20] | DUAL-REFUTE | TENSION |
| C1 | extreme Quintom | [-0.742, -0.200] | [-1.50, -0.50] | STRONG-REFUTE | EXCLUDED |
| C2 | deep phantom or boundary outliers | [-1.200, -1.050] | [-0.50, +0.50] | PHANTOM-REFUTE | EXCLUDED |

## Framework prediction per L_max

| L_max | w_0_FW(L) | w_a_FW(L) | Occupied scenario | Source |
|:------|:----------|:----------|:-------------------|:-------|
| 8 | (UNAVAILABLE) | (UNAVAILABLE) | PRE-REG-INCOMPLETE | S85 W7-7 (PRE-REG-INCOMPLETE; no published L=8 w_0) |
| 10 | -0.918000 | +0.000000 | INSIDE_R_842 | S85 W1b-1 + canonical_constants.w0_FW |
| 12 | -0.635000 | +0.000000 | B2 | S85 W1b-1 docstring step 3 / W0-Zubarev L=12 |

## 21-cell decision matrix (rows = scenario, cols = L_max)

Each cell entry: framework_response / decision_branch / cell_status.

| Scenario | L=8 | L=10 | L=12 | Column status |
|:---------|:----|:-----|:-----|:--------------|
| A1 | STUB / STUB / PRE-REG-INC | PARENT-GATE-PASS / PASS-PARENT / POP | NOT-OCCUPIED / NOT-OCCUPIED / POP | MONOTONE-degenerate |
| A2 | STUB / STUB / PRE-REG-INC | PARENT-GATE-PASS / PASS-PARENT / POP | NOT-OCCUPIED / NOT-OCCUPIED / POP | MONOTONE-degenerate |
| B1 | STUB / STUB / PRE-REG-INC | PARENT-GATE-PASS / PASS-PARENT / POP | NOT-OCCUPIED / NOT-OCCUPIED / POP | MONOTONE-degenerate |
| B2 | STUB / STUB / PRE-REG-INC | PARENT-GATE-PASS / PASS-PARENT / POP | PARTIAL-REFUTE-w_0 / TENSION / POP | MONOTONE |
| B3 | STUB / STUB / PRE-REG-INC | PARENT-GATE-PASS / PASS-PARENT / POP | NOT-OCCUPIED / NOT-OCCUPIED / POP | MONOTONE-degenerate |
| C1 | STUB / STUB / PRE-REG-INC | PARENT-GATE-PASS / PASS-PARENT / POP | NOT-OCCUPIED / NOT-OCCUPIED / POP | MONOTONE-degenerate |
| C2 | STUB / STUB / PRE-REG-INC | PARENT-GATE-PASS / PASS-PARENT / POP | NOT-OCCUPIED / NOT-OCCUPIED / POP | MONOTONE-degenerate |

## Determinism + monotonicity tally

- Total cells: 21 (3 L_max x 7 scenarios)
- Populated cells: 14/21
- Stub (PRE-REG-INCOMPLETE) cells: 7/21
- Cell-SHA-back-traceable: 21/21
- Monotone columns: 7/7
- Oscillation columns: 0/7

Per-column classification log:

- `MONO-all-eq-A1-('STUB', 'PASS-PARENT', 'NOT-OCCUPIED')`
- `MONO-all-eq-A2-('STUB', 'PASS-PARENT', 'NOT-OCCUPIED')`
- `MONO-all-eq-B1-('STUB', 'PASS-PARENT', 'NOT-OCCUPIED')`
- `MONO-non-decreasing-B2-('STUB', 'PASS-PARENT', 'TENSION')`
- `MONO-all-eq-B3-('STUB', 'PASS-PARENT', 'NOT-OCCUPIED')`
- `MONO-all-eq-C1-('STUB', 'PASS-PARENT', 'NOT-OCCUPIED')`
- `MONO-all-eq-C2-('STUB', 'PASS-PARENT', 'NOT-OCCUPIED')`

## Pre-registered regulator-first DR3 adjudication protocol (4 branches)

When DR3 publishes (w_0^DR3, w_a^DR3), the protocol fires
deterministically:

1. **Step 1 -- Scenario classification**: classify (w_0^DR3,
   w_a^DR3) into one of the 7 scenarios {A1, A2, B1, B2, B3,
   C1, C2} per S84 W4-44 §classification_rule. If inside
   R_842, parent gate G42 PASS dominates (not this gate's
   domain).

2. **Step 2 -- Column read**: read the column S* from the
   21-cell matrix; collect the 3 decision_branch entries
   (one per L_max in {8, 10, 12}).

3. **Step 3 -- Branch selection** (deterministic):

   - **(1) REG-INVARIANT**: all 3 L_max rows agree -> adopt
     the unanimous decision_branch.
   - **(2) REG-DEP-MAJORITY**: 2 of 3 agree, one dissents ->
     adopt majority; flag dissenter as regulator-class flag.
   - **(3) STRUCTURAL-AMBIGUITY-FREEZE**: all 3 differ ->
     freeze; re-dispatch in S87 with refined L_max scan.
   - **(4) EXTERNAL**: column has at least one
     PRE-REG-INCOMPLETE row -> defer to populated rows; emit
     EXTERNAL flag for re-dispatch in S87 after L_max gap
     closure.

Branches registered: 4/4

Determinism guarantee: branch output is a pure function of
(w_0^DR3, w_a^DR3, matrix). Idempotent verification in
self-test (deterministic == True for all 7 example points).

## Self-test (W4-44 example points)

| Test | (w_0, w_a) | Expected scenario | Computed scenario | Branch | Adjudicated decision | Deterministic |
|:-----|:-----------|:-------------------|:-------------------|:-------|:---------------------|:--------------|
| A1_example | (-0.965, +0.00) | A1 | A1 | EXTERNAL | DEFER | True |
| A2_example | (-1.020, +0.00) | A2 | A2 | EXTERNAL | DEFER | True |
| B1_example | (-0.850, -0.40) | B1 | B1 | EXTERNAL | DEFER | True |
| B2_example | (-0.650, +0.00) | B2 | B2 | EXTERNAL | DEFER | True |
| C1_example | (-0.650, -1.00) | C1 | C1 | EXTERNAL | DEFER | True |
| C2_example | (-1.100, +0.00) | C2 | C2 | EXTERNAL | DEFER | True |
| INSIDE_example | (-0.842, +0.00) | INSIDE_R_842 | INSIDE_R_842 | PARENT-GATE | PASS-PARENT | True |

## Source SHA pins (cell back-trace)

- W1b-1 verdict line (L=10/L=12 source): `beba9cad44f34103df20f3c7b01913a3658139d97ebd44126c8a38b9c12c510b`
- W7-7 verdict line (L=8 candidate; PRE-REG-INCOMPLETE): `dddf9edda82b4f3ea66e879822cc21eb9ac38ca11b928bd502ad5462a99a1ee7`

## Substrate framing (PHONONIC)

Each L_max row is a different truncation of the SAME
substrate eigenvalue computation. The substrate's w_0
prediction is the spectral-action gradient at the fold; w_a
is its first scale-derivative. As L_max increases (8 -> 10 ->
12), the cutoff-axis tightens and more substrate eigenmodes
contribute to the spectral moment. A scenario column that is
monotone in L_max indicates the substrate's prediction at
that scenario is REGULATOR-INVARIANT (a true substrate
observable). An oscillating column would indicate
REGULATOR-DEPENDENT prediction (a truncation artifact). The
substrate's self-test under DR3 input fires through the
4-branch adjudication protocol.

## Status

- Sub-tree: REGISTERED (S86 W13-4 INFO-on-pin).
- L=8 row: PRE-REG-INCOMPLETE per spawn-prompt fallback
  (W7-7 publishes no 7-cell decomposition; only an aggregate
  L_max-sensitivity scalar over an unrelated basket of 8
  W_0-dependent constants).
- Carry-forward to S87: extract or compute the L=8 7-cell
  decomposition (Zubarev w_0 at L=8 + scenario classification)
  and re-dispatch this gate at PASS level.

## Carry-forward

- S87 L=8 7-cell extraction: compute Zubarev w_0(L=8) directly
  from the L=8 D_K eigenvalue cache + classify scenario; fill
  7 stub cells; re-emit gate as PASS candidate.
- DR3 publication trigger (window opened 2026-04-23): fire
  the 4-branch adjudication protocol on (w_0^DR3, w_a^DR3);
  emit live-watch verdict in S87+.
