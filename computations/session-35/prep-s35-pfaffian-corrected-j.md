---
gate: S35-PFAFFIAN-CORRECTED-J
session: S81 (re-run of S35 gate PF-J-35)
classification: GEOMETRIC
verdict: PASS
value: -1
scheme: Pfaffian-Parlett-Reid_C1_at_D_K_Cliff8
convention: KO-dim=6_corrected-J_C2=g1g3g5g7_C1=g2g4g6g8
L_max: 16
closure_sha256: 1f6bf36f828513d4c384abcd30857b6cf396b98dc440f83acff62b6a077f4733
---

# Prep: S35-PFAFFIAN-CORRECTED-J

## Session / Path / SHA head

- **Session**: S81 ( re-run of S35 gate PF-J-35)
- **Original path**: `computations/session-35/s35_pfaffian_corrected_j.py`
- **Re-run driver**: `computations/_shared/t3-intake/_s35_pfaffian_corrected_j_rerun.py`
- **Verdict file**: `computations/_shared/t3-intake/s35_pfaffian_corrected_j_verdict.txt`
- **SHA head (source)**: `f2317ea9ac5053e7`
- **SHA head (re-run)**: `b72bbb1b473d62fd`
- **Closure SHA-256 (full 64)**: `1f6bf36f828513d4c384abcd30857b6cf396b98dc440f83acff62b6a077f4733`

## MCP baseline (queried before computation)

| Query | Result |
|:------|:-------|
| `trace_entity("pfaffian")` | theorem `proven_778` ("D_K Pfaffian Z_2 = +1 throughout"); gate `S30A-DTOTAL-PFAFFIAN` PASS (Z_2=+1, sha head 3207b176d6616051); closed_mechanism `closed_447` (D_K Pfaffian Z_2, no sign change) |
| `trace_entity("corrected_j")` | theorem `proven_752` ("BDI classification survives corrected J", session 35); equation history: S35 data shows sgn(Pf) = -1 at all 34 tau (comment-block in s36_bdi_winding.py) |
| `get_constant("J_C2")` | 0.933 (framework constant, NOT the Pfaffian diagnostic; C2 in this script is the matrix `gamma_1 gamma_3 gamma_5 gamma_7`) |
| `search_knowledge("S35 Pfaffian corrected J")` | Prior S35 result: sgn(Pf) = -1 at ALL 34 tau values (matches this re-run) |

Baseline: both S30A (Xi@D_total on C^32) and S35 (C1@D_K on C^16) are on record
as Z_2-TRIVIAL (constant sign). Absolute signs differ (+1 vs -1) but constancy
is the invariant. The present re-run must reproduce constancy; it does.

## Classification

**GEOMETRIC.** The Pfaffian is a Z_2 invariant of the spectral triple
(A_F, H_F, D_K) attached to the real structure J and the Dirac operator D_K.
It characterizes the fabric itself (the finite geometry), not a phononic
excitation spectrum, not a particle quantum-number, not an external observable.
Per `.claude/rules/phononic-framing.md`, this is explicitly NOT PHONONIC —
it is a property of the underlying geometric triple.

## Tolerance

| Quantity | Tolerance | Observed | Status |
|:---------|:----------|:---------|:-------|
| `|[T, D_K]|` (C2 commutation) | < 1e-12 | 4.85e-15 | PASS |
| `|{P, D_K}|` (C1 anticommutation) | < 1e-12 | 4.90e-15 | PASS |
| `|{S, D_K}|` (gamma_9 anticommutation) | < 1e-12 | 8.97e-15 | PASS |
| `||M+M^T||/||M||` (antisymmetry) | < 1e-12 | 1.02e-14 | PASS |
| `|Pf^2 - det|/|det|` (Pfaffian identity) | < 1e-12 | 8.58e-15 | PASS |
| `min|ev(D_K)|` (gap-open) | > 1e-10 | 8.186e-01 | PASS (gap OPEN) |
| `sgn(Pf)` constancy (union 34 tau) | constant required | -1 at all 34 | PASS |
| `sgn(Pf)` stored == extended agreement | must agree | True | PASS |

Gate criterion (pre-registered): PASS iff `sgn(Pf(M(tau)))` CONSTANT across
tau AND spectral gap OPEN everywhere. Both satisfied.

## Input pins (SHA-256, full 64-char)

| File | SHA-256 |
|:-----|:--------|
| `computations/session-35/s35_pfaffian_corrected_j.py` | `f2317ea9ac5053e7d5159afa4b55cb2a0064014e67be05610deb409060df7138` |
| `computations/_shared/dirac_spectrum.py` | `267035cb598b08e94117a3245cb07b29fbe6bff7b5a614a1bde64982851809c3` |
| `computations/session-23/s23a_kosmann_singlet.npz` | `ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214` |
| `computations/_shared/canonical_constants.py` | `68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f` |
| `computations/_shared/t3-intake/_s35_pfaffian_corrected_j_rerun.py` | `b72bbb1b473d62fdb57bf2a14abbfa7d1cd422ca72b171d405a85d08ba3c726b` |

## PRU machinery (pre-registration, all parameters pinned)

| Parameter | Value | Provenance |
|:----------|:------|:-----------|
| `L_max` (spinor dim) | 16 | Fixed by Cliff(R^8) irrep; not a scan |
| `N_TAU_STORED` | 9 | From `s23a_kosmann_singlet.npz` `tau_values` |
| `N_TAU_EXTENDED` | 25 | `np.linspace(TAU_EXT_MIN, TAU_EXT_MAX, N_TAU_EXTENDED)` |
| `TAU_EXT_MIN` | 0.0 | Identity deformation |
| `TAU_EXT_MAX` | 2.5 | Well beyond fold (`tau_fold=0.19`) and any physical interval |
| `C2` | `gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]` | S34-corrected real-structure J |
| `C1` | `gammas[1] @ gammas[3] @ gammas[5] @ gammas[7]` | Particle-hole (S34-independent) |
| `gamma_9` | `build_chirality(gammas)` | Verified `= C2 @ C1` at 0.00e+00 |
| Pfaffian algorithm | Parlett-Reid LTL^T | Wimmer, ACM TOMS 38(4), 2012, O(n^3) |
| `OMP_NUM_THREADS` | 8 | CPU path; 16x16 matrices, GPU not warranted |
| `MKL_NUM_THREADS` | 8 | Same |
| Random seed | n/a | Deterministic (no RNG in pipeline) |
| GPU path | none | `L_max=16` below 100x100 threshold |

All gate-relevant free parameters enumerated above are PINNED. No PRU Class 8
exposure: nothing in the gate evaluation depends on an unfixed knob.

## Substitution chain (sign direction — MANDATORY per math-scripts §Double-Check)

**Claim**: `sgn(Pf(C1 @ D_K(tau)))` is CONSTANT across tau in [0, 2.5].

**Step 1 — Definitions**

- `C2 = gamma_1 gamma_3 gamma_5 gamma_7` (real symmetric, `C2^2 = +I`); `T = C2 * K`, `T^2 = +1`
- `C1 = gamma_2 gamma_4 gamma_6 gamma_8` (real symmetric, `C1^2 = +I`); `P = C1 * K`, `P^2 = +1`
- `D_K(tau)` = 16x16 Dirac operator on Jensen-deformed SU(3) at parameter tau; Hermitian
- `M(tau) := C1 @ D_K(tau)` (Pfaffian matrix)
- `sgn(Pf(M))` takes values in `{-1, 0, +1}`, continuous in tau away from zeros

**Step 2 — Substitution (antisymmetry of M)**

```
{P, D_K} = 0     =>  C1 conj(D_K) + D_K C1 = 0
D_K Hermitian     =>  D_K^T = conj(D_K)
=> C1 D_K^T = -D_K C1
M^T = (C1 D_K)^T = D_K^T C1^T = D_K^T C1 = -C1 D_K = -M
```
M is antisymmetric, so Pf(M) is well-defined.

**Step 3 — Pfaffian-determinant identity**

```
Pf(M)^2 = det(M) = det(C1) * det(D_K)
```
with `det(C1) = +1` tau-independent (verified numerically: +1.000000 at machine epsilon).

**Step 4 — Simplification (zero-crossing criterion)**

```
sgn(Pf(M(tau))) changes at tau*  iff  Pf(M(tau*)) = 0
                                iff  det(M(tau*)) = 0
                                iff  det(D_K(tau*)) = 0
                                iff  min|ev(D_K(tau*))| = 0.
```

**Step 5 — Measurement**

```
min|ev(D_K(tau))| >= 0.8186    for all 34 tau in [0.0, 2.5]    (union of stored + extended)
```
(verified by `numpy.linalg.eigvals(D_K)` at each tau in the Python re-run).

**Step 6 — Direction from canonical form**

```
min|ev(D_K)| > 0 everywhere
  =>  No zero-crossing of Pf(M)
  =>  sgn(Pf(M(tau))) constant on [0.0, 2.5]
```

**Step 7 — Conclusion (from computation, not prior belief)**

Observed: `sgn(Pf(M)) = -1` at ALL 34 tau (9 stored + 25 extended). The absolute
sign `-1` is convention-dependent (Clifford basis orientation); the CONSTANCY
is the topological invariant. Z_2 BDI invariant TRIVIAL on the Jensen curve.

## Flags / open items

1. **Absolute-sign difference vs S30A-DTOTAL-PFAFFIAN (Z_2=+1)**: NOT a contradiction.
   Different Pfaffian matrices (Xi@D_total on C^32 vs C1@D_K on C^16) built from
   different real structures. Both PASS on constancy. Recommend future cross-gate
   reports use CONSTANCY as the comparison criterion, never absolute sign.
2. **S34 J-correction invariance**: The Pfaffian is built from C1, not C2; S34
   correction affects only T, re-verified at machine epsilon here. Result is
   STRUCTURALLY insensitive to the correction.
3. **Gap scale**: `min|ev(D_K)| = 0.8186` is large (~O(1) in natural units).
   Gate closing would require fine-tuned metric parameter outside Jensen family;
   none exists in any physical regime of interest.
