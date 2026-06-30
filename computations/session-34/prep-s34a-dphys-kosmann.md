# S34A-DPHYS-KOSMANN — Prep block (S81 canonical)

## Canonical one-liner
`S81|S34A-DPHYS-KOSMANN|PASS|GEOMETRIC|0.0859396|gate=0.05/0.15|ret=1.5037|ov=0.9346|B3open=NO|L_fib=16|seed=NA|script=c5fbb8770a27b4ed39e9c04a512f4373f71fefc7fb1cbc591ad88c9f0b97a6f9`

## Locate + read
- Script (runnable): `C:/sandbox/Ainulindale Exflation/computations/session-34/s34a_dphys_kosmann.py`  (28802 B)
- Wrapper:        `C:/sandbox/Ainulindale Exflation/computations/session-34/s34a_dphys_kosmann.py`
- Deps (archive):    `s34a_dphys_fold.py`, `s23a_kosmann_singlet.npz`
- Dep ():       `computations/_shared/dirac_spectrum.py`
- Domain: pure NCG — Kosmann-Lichnerowicz derivative `K_a = L_{X_a}` on Killing fields of SU(3), reprojected into D_phys eigenbasis under inner-fluctuation `phi`.

## MCP queries
- `trace_entity("dphys")` -> gate `DPHYS-34a`, provenance `s34a_dphys_fold.py`, `s34a_dphys_kosmann.py`, `s34a_dphys_thouless.py`, `s35_k7_dphys.py`.
- `trace_entity("kosmann")` -> gates `S75-M1-KOSMANN`, `S76-C6-KOSMANN`; provenance incl. `s23a_kosmann_singlet.npz`, `s22b_kosmann_matrix.py`.
- `search_knowledge("S34 D_phys Kosmann")` -> closed mechanism "Kosmann-BCS at mu=0" (S23a/S34); 5 equation hits confirming `phi=0 ⇒ D_phys = D_K`.
- No prior S81-canonical verdict for this gate. Consistent with prior S22B-KOSMANN-MATRIX (K_a matrices are anti-hermitian, basis-independent of phi) and S23A-KOSMANN-SINGLET (singlet-channel selection rule).

## Fixes applied
1. Canonical import header prepended via `s34a_dphys_kosmann.py` wrapper (`from canonical_constants import *`).
2. `sys.path` extended to include both `computations/_shared/` and `computations/_shared/` so `s34a_dphys_fold`, `dirac_spectrum`, and `s23a_kosmann_singlet.npz` all resolve.
3. Hilbert-dimension pin: `L_FIBER_DPHYS = 16` (spinor module on Cliff(R^8), `dim H_F = 2^(8/2) = 16`). Not a sweep parameter — fixed by algebra.
4. `canonical_constants.py` NOT modified.
5. All stdlib + path scratch vars tagged `# (local)`.

## SHA-256 pins (64-char, input)
- s34a_dphys_kosmann.py   : `abfedd34d07d0184ab4722490c9581f1fe43b7bb973cd2d9fef64412d6b29a4a`
- s34a_dphys_fold.py      : `7b7e769fd5018b694743c004d72aea97dfd596ea2108854b833c105fa60985cc`
- s23a_kosmann_singlet.npz: `ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214`
- canonical_constants.py  : `68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f`
- dirac_spectrum.py : `eee1b6fdcbb86847385130b3b3467c76fe1b5b73573d7dac4baf428cf4ff163f`

## Closure SHA-256 (64-char, output)
- s34a_dphys_kosmann.py: `d86015bac314909f311c986ad65c64afeb65d231a71285c6e40dd6afb88ec8cf`
- s34a_dphys_kosmann.npz  : `c5fbb8770a27b4ed39e9c04a512f4373f71fefc7fb1cbc591ad88c9f0b97a6f9`
- s34a_dphys_kosmann.png  : `fae1dc005e257c0d9e7d74943feacd423da0f79388f3cf3a0b7cb03782c47f1b`

## Execution
- `python = "C:/sandbox/Ainulindale Exflation/phonon-exflation-sim/.venv312/Scripts/python.exe"`.
- Matrices 16x16 (<100) ⇒ CPU path per rule; numpy `eigh` sufficient, no GPU ship-over needed.
- Runtime: 0.9 s. No warnings, no NaN, unitarity error max 1e-12, Hermiticity errors within numerical tolerance.

## Pre-registered gate & observed numerics
Gate DPHYS-34a-2: `V(B2,B2)_max_off-diag(phi = gap_{B3-B2})` vs thresholds {0.15 STRONG, 0.05 PASS, <0.05 FAIL}.

| Quantity                              | Value                           |
|---------------------------------------|---------------------------------|
| gap_{B3-B2}                           | 0.13295479                      |
| V(B2,B2) max off-diag at phi=gap      | 0.08593957                      |
| V(B2,B2) max off-diag bare (phi=0)    | 0.05715284                      |
| Retention ratio                       | 1.5037                          |
| SU(2) / C^2 / U(1) decomposition      | 0.03081 / 0.01653 / 0.05442     |
| V(B1,B2) max                          | 0.07699 (bare 0.07991, 0.964x)  |
| V(B3,B2) max                          | 0.02196 (bare 0.02654, 0.828x)  |
| B2 overlap with bare B2               | 0.9346                          |
| Multi-tau V(B2,B2) at phi=gap         | 0.0810 (tau=0.10) ... 0.0907 (tau=0.30) — monotone in tau |
| Cross-check err (phi=0 reprojection)  | 1.94e-16 (machine epsilon)      |

## Substitution chain (direction/sign claims)

- Retention ratio > 1 (V enhanced at phi=gap):
  - def: V_B2B2^phys = sum_a |U^H K_a U|^2_{B2,B2}; at phi=0, U=I ⇒ V_B2B2^phys(0)=V_B2B2^bare.
  - sub: U mixes rows of B2 with B1 (and B3) ⇒ off-diagonal |K_a^bare|_{B1,B2}=0.0799 enters the B2-B2 block as |U^H K_a U|_{B2,B2} cross-terms.
  - simplified: the large bare B1-B2 matrix element (0.0799) transfers quadratic weight into the B2-B2 block as B2 acquires B1 admixture (overlap 1.000 -> 0.935).
  - direction: V_B2B2^phys(gap) > V_B2B2^bare. Verified numerically: 0.0859 > 0.0572 (ratio 1.504). Non-monotone along phi (dip at phi=0.06) but positive at gap.
- B3 channel does not open (ratio < 1.05):
  - def: V_B3B2^phys(phi)/V_B3B2^bare; W1 threshold = 1.05.
  - sub: admixture that RAISES V_B2B2^phys SUBTRACTS amplitude from the same K_a |K_a|^2 mass that previously sat in V_B3B2^bare (sum rule Tr(V) invariant under unitary).
  - simplified: ratio = 0.828 < 1.05 ⇒ channel closes.
- Gate classification: 0.05 < 0.0859 < 0.15 ⇒ PASS (moderate). Thresholds preserved verbatim from pre-registration.

## Verdict & classification
- Verdict: `PASS` (moderate) — V(B2,B2) = 0.0859 exceeds 0.05 but not 0.15.
- Classification: `GEOMETRIC` — this measures a property of the spectral triple (D_phys eigenbasis vs K_a kernel) under inner fluctuations; no excitation spectrum is integrated. The fabric's Kosmann kernel survives the Higgs-sector inner fluctuation.
- Cross-checks: phi=0 reproduction err = 1.94e-16 (PASS, machine epsilon). U unitary to 1e-12. Multi-tau monotone rise 0.081 -> 0.091 across tau in [0.10, 0.30] ⇒ fold region robust. Prior S22B/S23A anti-hermiticity of K_a preserved (basis change is unitary conjugation).

## Notes for team
- Consistent with prior S22B-KOSMANN-MATRIX (K_a anti-hermitian, block-structure of |K_a|^2) and S23A-KOSMANN-SINGLET (bare B2-B2 diagonal ~ 0.063).
- Non-monotonicity in phi (dip at 0.06) is genuine — arises from rank-1 unitarity of U on the degenerate B2 block, not numerical artifact. Worth noting in any later workshop on inner-fluctuation stability.
- W1 "B3 channel opens" prediction from S34a plan is refuted (ratio 0.828 < 1.05). This does not invalidate gate DPHYS-34a-2 but closes a subsidiary pathway.
