# NCG Bridge Reference (Sessions 6-11, compressed)

## A_F Derivation Summary
- Phase 4a gate (Session 6): End_{U(2)_LR}(Psi+) = C + M_2(C) + M_3(R) + R (dim 20). NOT A_F.
- With J on C^32 (Session 9): 128-dim J-compatible commutant, 3 factors (32,32,64).
- Order-zero selects A_F = C + H + M_3(C) (dim 24) as maximal compatible subalgebra.
- R_u(2) is correct gauge: electroweak Killing symmetry of Jensen SU(3). L is NOT homomorphism (v_11 anomaly = Higgs).
- Metric-independence: End_{U(2)}(Delta_8) depends only on group embedding (topological).

## Order-One Results (Session 10-11)
- Connes left-Yukawa (block-diag): 5/9 factor pairs PASS (all M_3(C) sector). 4/9 C+H FAIL.
- delta_v is NOT D_F. Correct D_F = <phi_alpha, D_K phi_beta> from Dirac on (SU(3), g_s).
- Order-one subalgebra from L-closure: dim 20 = C + M_3(C). Missing H (requires bimodule).
- Yukawa-INDEPENDENT: same 20-dim for identity and random Yukawa.

## Chirality Resolution (Session 11)
- gamma_F should be ROW-BASED internal chirality (RH rows 0-1 = +1, LH rows 2-3 = -1).
- NOT the Psi+/Psi- particle/antiparticle grading.
- Block-diagonal left-Yukawa D_F ANTICOMMUTES with corrected gamma_F. Chirality half resolved.
- 4/9 C+H failures remain. Require actual D_K computation.
- Barrett existence theorem: valid D_F guaranteed for KO-dim 6 + dim 32.
- D_K commutes with R_su(3) (Killing isometries) -> explains 5/9 M_3(C) passes.
- D_K anticommutes with Gamma_K (Lichnerowicz theorem).
- AZ class: BDI (T^2=+1). Corrected from DIII in Session 17c.

## Key Scripts (Session 10)
- `tier0-computation/phase25_connes_embedding_test.py` — DECISIVE order-one test
- `tier0-computation/phase25_DF_on_Lclosure.py` — L-closure order-one (dim 20)
- `tier0-computation/phase25_wedderburn_detail.py` — Wedderburn decomposition
- `tier0-computation/branching_computation.py` — Original branching + Gell-Mann matrices

## Key Numbers
| Quantity | Value |
|----------|-------|
| L-closure dim | 38 |
| Order-one constraint rank | 18 |
| Order-one subalgebra dim | 20 (C + M_3(C)) |
| Order-one verification | 6.3e-17 |
| Gate check (M3 rows vs R) | EXACT 0 |

## Debugging Lessons
- f-string with `R_{u(2)}` causes NameError in Python
- scipy null_space overflows for matrices > ~65k rows (use eigh on A^T A)
- Cross-factor order-zero is automatic; within-factor is the hard constraint
- Center of commutative algebra: adjoint method gives spurious result (trivially zero constraint matrix)
