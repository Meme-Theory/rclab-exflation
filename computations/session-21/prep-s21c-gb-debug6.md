# Prep: S21C-GB-DEBUG6

**Gate:** S21C-GB-DEBUG6
**Source script:** `computations/session-21/s21c_gb_debug6.py`
**rerun script:** `computations/_shared/t3-intake/s21c_gb_debug6.py`
**Companion:** `computations/_shared/t3-intake/s21c_gb_debug4.py` (landed earlier S81)
**Classification:** GEOMETRIC
**Domain:** Chern-Gauss-Bonnet density on bi-invariant SU(3) (dim=8, chi=0)

## Pins

| Artifact | SHA-256 (64-char) |
|:---|:---|
| script | `61f8453bd95395f232053dba99ec8d1e142f9a7ee9c5826688a25e75963fec83` |
| canonical_constants.py | `68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f` |
| r20a_riemann_tensor.npz | `fc256a9b4791b1d6e1416f93cabbb0e28fe0c858bf2aeb04414b7767a7351fe9` |
| closure (stdout log) | `9a9b14ecb795552a44bbe916c12499322f7e42a11304bbd0756d1b0406f11213` |

## Knowledge MCP queries

- `trace_entity("gauss_bonnet")` — returned 1 session hit (S21c), 1 provenance, 10 equations. Confirms chi(SU(3))=0 is established expectation, not a novel computation. Prior closure: equation `eq_50742` states "The chi=0 for SU(3) means the Gauss-Bonnet topological term vanishes."
- `search_knowledge("S21c GB debug6")` — returned 5 provenance hits including `gb_debug6` directly linked to `r20a_riemann_tensor.npz`. 15 equation hits, all confirming the brute-force einsum path (eps-R-R-R-R contraction via bivector intermediates T1..T4).

## Gate definition (pre-registered)

`|S(SU(3)) / 6144| < 1e-08` on BOTH analytic SU(3) (built from structure constants, R_{abcd} = (1/12) f_{abe} f_{cde}) AND stored tau=0 Riemann tensor from `r20a_riemann_tensor.npz`.

Supporting cross-checks (must PASS for gate to be credible):
- chi(S^4) = 2 exact (tests einsum pair-ordering `'pqrs,wxyz,pqwx,rsyz'`)
- chi(S^8) = 2 via `(1/(2pi)^4) * (S/6144) * Vol(S^8)` with Vol=32pi^4/105
- chi(U(1)xSU(2)) = 0 exact (rank-3 non-simple block)

## Substitution chain (chi(SU(3)) = 0 direction)

1. **Definition (Poincare-Hopf).** For a smooth compact orientable manifold M^n and any smooth vector field V with isolated zeros, chi(M) = sum_{p: V(p)=0} index(V, p).
2. **Substitution (Lie group specialization).** For a compact Lie group G of rank r, choose a regular element H_0 in the Cartan subalgebra. The left-invariant extension V(g) = (L_g)_* H_0 is a smooth vector field on G. Because H_0 is regular, V(g) != 0 everywhere on G when r >= 1.
3. **Simplification.** No zeros of V implies the right-hand side of step 1 is an empty sum, hence chi(G) = 0.
4. **Direction.** rank(SU(3)) = 2 >= 1, therefore chi(SU(3)) = 0. This is canonical (Poincare-Hopf); the Chern-Gauss-Bonnet integral must match, so the pointwise Euler-density integrand S is expected to vanish identically on the bi-invariant metric.

Independent confirmation at the integrand level: on a homogeneous (bi-invariant) metric the Euler density is pointwise constant; `S = 0` pointwise is consistent with `chi = 0` via any finite normalization (no volume- or dim-factor cancellation required).

## Fix summary (archive script -> rerun script)

1. Added `sys.path.insert(0, 'computations')` and `from canonical_constants import PI`.
2. Replaced all `np.pi` occurrences with `PI` in the Vol(S^8) formula and the (2pi)^4 normalization.
3. Tagged every intermediate assignment with `# (local)` (the Levi-Civita builder, R_S4, R_U2, R_SU3, T1..T4, S_*, chi_*, vol_S8, stored_path, d, gate thresholds).
4. Dropped the buggy `'abcd,efgh,aebf,cgdh'` einsum pair-misordering block from the archive version; retained only the corrected `'pqrs,wxyz,pqwx,rsyz'` pairing (and its 8D analogue via stepwise contraction).
5. Added explicit pre-registered gate evaluation block with PASS/FAIL reporting.
6. No framework constants hardcoded (GB is purely geometric-topological; M_KK, tau_fold etc. are not involved).

## Machinery enumeration (PRDR)

| Parameter | Value | Pinned by |
|:---|:---|:---|
| Bi-invariant metric on SU(3) | Killing, normalized so R_{abcd} = (1/12) f_{abe} f_{cde} | Script, lines 90-110 |
| Structure constants f_{abc} | Gell-Mann normalization (f_{012}=1, f_{347}=f_{567}=sqrt(3)/2, half-values for mixed triples) | Script f_values dict |
| Stored Riemann | `r20a_riemann_tensor.npz` at tau=0 (index 0 of R_abcd array) | npz SHA pin above |
| Levi-Civita builder | itertools.permutations + inversion-count sign | Script lines 26-43 |
| Einsum pair ordering | `'pqrs,wxyz,pqwx,rsyz'` in 4D; stepwise `'abcdefgh,abij->cdefghij'` then cdkl, efmn, ghop in 8D | Script lines 58, 100-117 |
| Normalization 1/6144 | = 1/(2^8 * 24) from Pfaffian expansion (four 2-forms, each 1/2 for eps-pair symmetry, 1/4! for block reorder, 1/2^4 for spatial wedge) | Script lines 98-99, verdict comment |
| Machine-epsilon gate | 1e-8 (far above observed 5e-20 residual) | Script var `eps_machine` |

All machinery parameters pinned; no free parameter at execution time. PRU-safe.

## Result

Analytic SU(3): `|S/6144| = 3.78e-20`, stored SU(3) tau=0: `|S/6144| = 4.82e-20`. Both cross-check manifolds (S^4, S^8) return chi=2 exactly. U(1)xSU(2) returns S=0 exactly (no floating-point residue; all contributions identically zero from the Lambda^2({1,2,3}) subspace).

**Verdict: PASS.** chi(SU(3)) = 0 confirmed at machine-epsilon level via independent brute-force Levi-Civita contraction, consistent with Poincare-Hopf (the canonical direction).
