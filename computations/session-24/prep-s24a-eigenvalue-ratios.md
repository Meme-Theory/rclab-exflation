# Prep — S24A-EIGENVALUE-RATIOS

**Gate**: S24A-EIGENVALUE-RATIOS
**Upstream gate**: R-1 (S24a prompt Section IV)
**Original session**: S24a (2026-02-21) — verdict FAIL
**Re-run session**: S81 (canonical form)
**Script under re-run**: `computations/session-24/s24a_eigenvalue_ratios.py`
**Re-run script**: `computations/_shared/t3-intake/s24a_eigenvalue_ratios.py`

## Locate

- Primary: `computations/session-24/s24a_eigenvalue_ratios.py` — **not present**.
- Found in: `computations/session-24/s24a_eigenvalue_ratios.py` (5743 bytes, SHA-256
  `64240ef8ad9c37122dfa650068486e364de1c6c57cf8cce1accc9ee1a585c85d`).
- Input data: `computations/session-23/s23a_kosmann_singlet.npz`, SHA-256
  `ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214`.

## Structural classification

Pure **post-process** over a pre-computed 16-eigenvalue singlet-sector
spectrum at 9 tau values. **No D_K diagonalization inside this script.**
GPU path is therefore inapplicable (no matrices to diagonalize). CPU-only
with `OMP_NUM_THREADS=8` is correct.

The "eigenvalue matrix" referenced in the task description is produced
upstream by `s23a_kosmann_singlet.py` (already committed to computations/_shared).
That is where a GPU path would apply — not here.

## MCP context (query-before-compute)

- `trace_entity("eigenvalue_ratios")`:
  - theorem: FUNCTIONAL-INDEPENDENT eigenvalue ratios (S676 proven).
  - gates: V-3 FAIL, R-1 FAIL, AC-1 DOES-NOT-CLOSE, V-1 CLOSED.
  - session: S24a final — "Panel 8%, Sagan 5%, V-1 CLOSED".
- `get_constant("phi_paasch")`: **1.53158** (canonical, PROVEN S12).
- `get_constant("J_C2")`: **0.933** (present, used elsewhere — not needed here).
- `search_knowledge("S24a eigenvalue ratios phi_paasch")`: prior run
  produced `s24a_eigenvalue_ratios.npz/.png`; verdict FAIL recorded in
  `session-24-sagan-verdict.md`.

Conclusion: re-run is a **reproduction** under S81 canonical form. No
new physics; verdict must agree with S24a R-1 FAIL to within equality of
the input hash.

## Fixes applied

1. **Canonical import**: `from canonical_constants import phi_paasch, tau_fold`.
   Removed hardcoded `phi_paasch = 1.53158` (was line 30 of original).
2. **Local tagging**: every computed scalar/array tagged `# (local)` —
   loop indices, tolerances, counts, closest-ratio bookkeeping.
3. **L_max pin**: 16 eigenvalue entries per tau — structural lineage pin
   to upstream singlet projection (`s23a`, L_max=3). No freedom at this
   stage; input-shape-enforced via `N_EIG_EXPECTED = 16` check.
4. **Input-SHA guard**: script raises if `s23a_kosmann_singlet.npz` SHA
   drifts from pinned value.
5. **Canonical-SHA advisory**: if `canonical_constants.py` SHA drifts,
   note printed but run continues (constants themselves are version-
   checked by value, not file).
6. **Substitution chain**: embedded in the module docstring and repeated
   in the verdict.

## SHA-256 pins (64-char, pre-run)

| file | SHA-256 |
|:-----|:--------|
| `computations/session-24/s24a_eigenvalue_ratios.py` | `64240ef8ad9c37122dfa650068486e364de1c6c57cf8cce1accc9ee1a585c85d` |
| `computations/session-23/s23a_kosmann_singlet.npz`  | `ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214` |
| `computations/_shared/canonical_constants.py`| `68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f` |

## SHA-256 closure (64-char, post-run)

| file | SHA-256 |
|:-----|:--------|
| `t3-intake/s24a_eigenvalue_ratios.py`  | `9581cff300a7b239dd07720009935a92fed0d31c590f43a5fa3f72dfdd1ac37f` |
| `t3-intake/s24a_eigenvalue_ratios.npz` | `2e6929adf3f06fdcf07f7477d53ae1df26213e3ba9d1ebff6123fd0b6f3c41c6` |
| `t3-intake/s24a_eigenvalue_ratios.png` | `910a6f3716876d24b83d178d5c666830a9462e81a8659d0d8eec35cb459266eb` |

## Substitution chain (direction claim)

Target claim: "phi_paasch crossings in |eigenvalue| neighbor-ratio spectrum".

- Step 1 (def): `r_n(tau) = |lambda_{n+1}(tau)| / |lambda_n(tau)|`, with
  `|lambda_0| <= |lambda_1| <= ... <= |lambda_15|`.
- Step 2 (sub): monotone-ascending sort ⇒ numerator ≥ denominator ⇒
  `r_n >= 1` for all (n, tau). (Numerically verified: min r = 1.000 at
  tau=0 where 5-fold degeneracy `|lambda| = sqrt(3)/2` pins the
  lowest ratios to unity.)
- Step 3 (simp): `CROSS_{n,tau} := 1` iff
  `|r_n(tau) - phi_paasch| / phi_paasch < 0.001`.
- Step 4 (dir): verdict = `PASS` if `sum(CROSS) > 0` else `FAIL`.
- Numerical: `sum(CROSS) = 0` at 0.1% tol; also 0 at 1% tol; closest
  `dev = 10.147%` at (tau=0.5, n=9). ⇒ verdict **FAIL**.

## Gate outcome

**FAIL** — matches S24a R-1 classification. Verdict file:
`t3-intake/s24a_eigenvalue_ratios_verdict.txt`.

## Run record

- Environment: `phonon-exflation-sim/.venv312/Scripts/python.exe` (3.12).
- Wall time: sub-second (NPZ post-process; no linalg).
- GPU: not invoked (no matrix operations).
- CPU threads: capped at 8 via `OMP_NUM_THREADS`.
- Exit code: 0.
- Output printed verdict + SHA-pinned artefacts in `t3-intake/`.
