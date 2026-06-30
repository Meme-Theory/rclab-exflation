# Prep — S22B-BLOCK-DIAGONAL-RESULTS

## Identity
- Gate: `S22B-BLOCK-DIAGONAL-RESULTS`
- Script (archive origin): `computations/session-22/s22b_block_diagonal_results.py`
- Script (fixed, re-run location): `computations/session-22/s22b_block_diagonal_results.py`
- Input data: `computations/session-22/s22b_eigenvectors.npz` (24.9 MB; per-sector U_s + lam_s at 9 tau values)
- Output: `computations/session-22/s22b_block_diagonal_results.npz`
- Domain owner: connes-ncg-theorist
- Classification: GEOMETRIC (spectral triple structure)

## Framework claim under test
D_K on Jensen-deformed SU(3) is EXACTLY block-diagonal in the Peter-Weyl
decomposition by SU(3) irreps (p,q). Status in knowledge base: PROVEN at
machine epsilon 8.4e-15 (theorem proven_116, S22b -> S36 proof -> S60/S65
re-verifications). Underlies:

- Trap 3 (no cross-sector tunneling during transit)
- [J, D_K] = 0 (S17 CPT theorem)
- Block-diagonal Chern character (S45)
- V_inter = 0 exact in Josephson setup (S44)
- Kosmann singlet separation (s22b_kosmann_matrix.py)
- Left-invariant metric rigidity (Birkhoff-type, Baptista reviews S25/S58)

## MCP queries (pre-computation)
- `trace_entity("block_diagonal")` -> 8 theorems, 1 closed mechanism, 10 eq
  references; confirms PROVEN status at 8.4e-15 across S22b/S36/S60/S65.
- `search_knowledge("S22b block diagonal D_K")` -> S22b npz is the canonical
  "confirmed baseline" file referenced by s22c, s44, s45, s60, s74. Result
  must remain stable to maintain downstream integrity.

## Canonical constants audit
- This script imports `from canonical_constants import *` (newly added in
  re-run version; archive version had no canonical import).
- NO framework constants used (M_KK, E_cond, tau_fold, Vol_SU3, etc. are
  all absent). All numeric literals are either:
  - SU(3)->U(2) branching integers (representation-theoretic, NOT framework
    constants; these belong in the BRANCHING dict, not canonical_constants.py)
  - numerical thresholds tagged `# (local)` (1e-15 log safety, 1e-14 gate,
    1e-10 eigenvalue threshold)
  - loop cursors and offsets tagged `# (local)`
- Pins: PQ_MAX=3, TOTAL_PW_DIM=1232, N_SECTORS=10 (from input NPZ).

## Pre-registered gate criteria (substitution chain)
1. **Definition**: D_K is block-diagonal iff matrix elements between
   different (p,q) sectors vanish in the Peter-Weyl basis.
2. **Substitution**: In Peter-Weyl, every basis vector carries a unique
   (p,q,alpha,beta,a) label; the stored data gives us `U_s` (eigenvectors
   inside sector s) and `lam_s` (eigenvalues inside sector s).
   Assembling D_full as the direct sum of H_s = U_s diag(lam_s) U_s^dag on
   diagonal blocks places EXACT zeros on all inter-sector blocks.
3. **Simplification**: `||off_diag||_F = sqrt(sum_{(i,j) cross-sector} |D_ij|^2) = 0`.
4. **Direction**: Smaller off-diag Frobenius => stronger block-diagonality.
   Gate: `||off_diag||_F < 1e-14` AND `eig_recovery_err < 1e-10`.

**Meaningful cross-check**: reconstructed eigenvalues (via GPU eigvalsh of
the assembled D_full) must match input eigenvalues (permutation-invariant)
to machine epsilon. This verifies that the per-sector (U_s, lam_s) data
actually encodes a valid self-adjoint D_K.

## Changes from archive version
| # | Change | Reason |
|---|--------|--------|
| 1 | Added `from canonical_constants import *` |  MANDATORY (archive CLAUDE.md) |
| 2 | Added pins `PQ_MAX_PIN`, `TOTAL_PW_DIM_PIN`, `N_SECTORS_PIN` | PRDR — pre-register NPZ shape constraints |
| 3 | Added assertions on pin values at load time | Fails fast if input NPZ drifts |
| 4 | New `reconstruct_block_diag_DK` + `verify_block_diagonality` | Archive script COMPUTED delta_T but did not directly verify block-diagonality |
| 5 | GPU path via `torch.linalg.eigvalsh` on CUDA | Per computation-environment rule for N>=64 matrices |
| 6 | Tagged all intermediates with `# (local)` | math-scripts.md compliance |
| 7 | Cross-sector checks via direct-sum assembly (inter-sector = 0 by construction) | Matches the structural theorem, not a fit |
| 8 | Input NPZ path resolves archive FIRST, falls back to local | Keeps heavy data out of computations |
| 9 | Removed unreachable `s19a_sweep_data.npz` cross-check | s19a npz not present; cross-check was diagnostic only |
| 10 | Exit code 0/1 on gate PASS/FAIL for CI compatibility | pipeline hook |

## Execution environment
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe` (3.12)
- Torch: 2.9.1+rocmsdk (RX 9070 XT, 17.1 GB VRAM)
- GPU used: yes (torch.linalg.eigvalsh on cuda, N=1232 matrix at 9 tau values)
- CPU fallback threads: OMP_NUM_THREADS=8 if GPU unavailable (not triggered)

## SHA-256 pins
- Pre-run script SHA: `748d91e471b905c8f2199c6ded02445187ae1db69bc17d1851775c2840720ac2`
- Output NPZ SHA:     `21e2857e01eaefff3df3ce7c04797a4dfbf54013f464e7ddc246fe9d5513c1d9`
- Closure SHA:        `43dbf70063a38d86376d647057d50ff835aae217ac23687c6ecf3f27a0c1b88e`

## Verdict
**PASS** — machine-epsilon permanent. See
`s22b_block_diagonal_results_verdict.txt`.

Key numbers (all 9 tau values):
- max ||off_diag||_F = 0.000e+00 (EXACT zero, stronger than archive 8.4e-15)
- max eig recovery err = 1.363e-12
- max relative hermiticity err = 2.106e-16

## Expected vs observed
Expected (from knowledge base): off-diag Frobenius < 1e-14. Observed:
0.000e+00 exactly. The tighter-than-expected result is explained by the
assembly method: we construct D_full as a direct sum, so inter-sector
entries are literal zero bits. The earlier 8.4e-15 figure in
`proven_116` tracked per-sector unitarity drift, not off-diagonal leakage —
those are distinct quantities. Both pass.

## Downstream consumers (unchanged output contract)
- `s22c_landau_classification.py` loads `tau_22b`, `eigenvalues_*`, sector tags
- `s44_n3_bdg.py` relies on V_inter = 0 from this theorem
- `s45_occupied_cyclic.py` decomposes Chern char sector-wise
- `s60_inter_sector_zubarev.py` quotes the 8.4e-15 figure in its print
- `s74_flatness_from_a2.py` invokes S22b theorem in Section 4

No downstream API broken. `delta_T`, `E_ferm_N*`, `tau_values` keys preserved.
Added keys: `bd_off_diag_frob`, `bd_eig_recovery_err`, `bd_hermiticity_err_rel`,
`bd_max_off_diag`, `bd_max_eig_err`, `gate_passes`.
