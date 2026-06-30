# Prep: S22B-KOSMANN-MATRIX

## Gate ID
S22B-KOSMANN-MATRIX

## Trigger
[VERIFY-THEOREM]

## Classification
GEOMETRIC

## Hypothesis
The spinorial Kosmann-Lichnerowicz operator family on Jensen-deformed SU(3)
satisfies four structural identities simultaneously:

  (H0) K_a_LX = (1/4)(L_{e_a} g)^{jk} gamma_j gamma_k = 0 for ALL a, tau —
       because L_X g is symmetric and Tr(L_X g) = 0 (volume-preserving
       Jensen), so sum_jk Lg_{jk} gamma_j gamma_k = sum_j Lg_{jj} * I = 0
       via {gamma_j, gamma_k} = 2 delta_jk.
  (H1) ||Lg_a|| = 0 for a in U(2)_IDX (Killing directions) at all tau.
  (H2) K_a_Ltilde = K_a_LX + Phi_a (Paper 18 eq 1.4) is nontrivial
       (||K_Ltilde|| >~ 0.04 at tau=0.10, growing monotonically to ~0.98
       at tau=0.50). The Phi correction is the physically meaningful
       content of the gauge-mass term (Paper 18 eq 1.2).
  (H3) D_K (the internal Dirac operator on L^2(SU(3), S)) is RIGOROUSLY
       block-diagonal in the Peter-Weyl decomposition; the inter-sector
       coupling matrix C_{nm} = <psi_n|V|psi_m> between eigenvectors
       of D_K in different (p,q) sectors is structurally zero when
       V is built from K_a alone (no CG intertwiner between distinct
       irreps exists via left-invariant data).

## Substitution chain (theorem / identity claim, not sign)

Step 1 (definition):  D_K = sum_a gamma_a (e_a + omega_a^{spin})  where e_a is a
  left-invariant vector field on G = SU(3) and omega_a^{spin} is a constant
  matrix on C^{16} (left-invariant spin connection in ON frame).

Step 2 (Peter-Weyl):  L^2(G) = direct-sum over (p,q) of  V_{(p,q)} (x) V*_{(p,q)}
  as G x G-representations.

Step 3 (substitute):  Left action L_g : f(x) -> f(g^{-1} x) commutes with e_a
  (since e_a is left-invariant), so e_a preserves each Peter-Weyl block. On
  block (p,q), e_a acts as rho_{(p,q)}(X_a) (x) I.

Step 4 (spin piece):  I_V (x) omega_a^{spin} is block-constant in (p,q): it acts
  as omega_a^{spin} inside every sector, identically.

Step 5 (simplify):  D_K|_{(p,q)} = sum_a gamma_a (rho_{(p,q)}(X_a) (x) I_S)
  + I_V (x) sum_a gamma_a omega_a^{spin}.   D_K = direct-sum_{(p,q)} D_{(p,q)}.

Step 6 (direction):  off-diagonal blocks of D_K vanish:  || D_K [(p1,q1) -> (p2,q2) ] ||_F = 0
  for (p1,q1) != (p2,q2).  Since K_a is purely spinorial (no function-space
  action), no CG intertwiner between distinct V_{(p1,q1)}, V_{(p2,q2)} exists
  from K_a alone, so C_{nm} = 0 for sectors differing by (+1,-1) or (-1,+1).

## Machinery pin (PRDR)

- `TAU_VALUES`: taken from PA-1 output `s22b_eigenvectors.npz`, field
  `tau_values = [0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]`.
  These are not canonical; they are the PA-1 scan grid. Diagnostic run uses
  the same list.
- `SECTOR_LIST`: fixed at [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)] (gap-edge
  sectors, per original script line 1300). Frozen.
- `MAX_PQ_SUM`: implicit = 3 (set by SECTOR_LIST). Frozen.
- `U1_IDX = [7]`, `SU2_IDX = [0,1,2]`, `C2_IDX = [3,4,5,6]`, `U2_IDX = [0,1,2,7]`
  — imported from `dirac_spectrum.py` (algebraic primitive, not a
  framework constant).
- `DIM_SPIN = 16` (Cliff8 irrep). Frozen.
- `SYM_TOL = 1e-10` (symmetry check tolerance on Lg). (local) per math-scripts.md.
- `NORM_TOL = 1e-14` (structural-zero tolerance for ||Lg_u2||, ||off-diag D||).
  (local).
- `COUPLING_TOL = 1e-12` (structural-zero tolerance for ||C_eig||_F on
  (p1,q1) != (p2,q2)). (local).
- `GPU path`: N/A. Matrices are 16x16 or 64x64 (combined sectors). CPU with
  `OMP_NUM_THREADS=8` per computation-environment.md. No torch required.
- `random_seed`: N/A (deterministic).

## Input SHA-256 pins (pre-fix)

- `s22b_kosmann_matrix.py`:  12258df3ae251657fc5ddcef7ba6210a02e969282e65f218298f7571f530e013
- `dirac_spectrum.py`: eee1b6fdcbb86847385130b3b3467c76fe1b5b73573d7dac4baf428cf4ff163f
- `canonical_constants.py`:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
- `s22b_eigenvectors.npz`:   8e08fc4f36386430c01ca5bab99447359584b4a5ac74a8a0a01599f5028583e6

## Pre-registered threshold (4-tuple)

**PASS** (joint structural identity, all four must hold):

  (H0)  max_a in C2_IDX, max_tau    ||K_a_LX||_F   <  NORM_TOL = 1e-14
        (structural vanishing of L_X Kosmann spinor term)
  (H1)  max_a in U2_IDX, max_tau    ||Lg_a||_F     <  NORM_TOL = 1e-14
        (U(2) Killing directions at all tau)
  (H2)  min_a in C2_IDX, tau >= 0.1 ||K_a_Ltilde||_F > KLT_FLOOR = 1e-3
        (Paper 18 correction is operative across grid)
  (H3)  max over sector pairs and tau, both schemes (L_X and L_tilde):
        ||C_eig(((p1,q1),(p2,q2)))||_F  <  COUPLING_TOL = 1e-12
        for all (p1,q1) != (p2,q2).

**FAIL**: any of (H0), (H1), (H2), (H3) violated.

**INFO**: (H1), (H2) hold but (H3) finds nonzero C_eig only from CG-matrix
  failure (numerical breakdown) rather than a structural nonzero.

Scheme:   `Kosmann_spinor_LX_and_Ltilde_Baptista_P17-P18`
Convention: `KO-dim=6_Cliff8_ON-frame_PW-decomp`
L_max (effective): `L_max=max_pq_sum=3_(sectors_00_10_01_11_20_02)`

## Value reported

4-tuple scalar value summary:
  `value = {max||Lg||_u2, max||K_LX||, min||K_Ltilde||_posTau, max||C_eig||_interSector}`

## Threshold derivation (substitution chain for KLT_FLOOR = 1e-3)

Step 1 (def): K_Ltilde = K_LX + Phi, where Phi is the transport-map correction
  from Paper 18 eq 5.11.
Step 2 (subst): Jensen scale factors are (e^{2tau}, e^{-2tau}, e^{tau}) on
  (u(1), su(2), C^2). The Phi correction in ON frame scales as
  (L_V phi)_{jk} ~ O(tau) near tau=0 (first derivative of phi in the TT
  direction).
Step 3 (simplify): So ||K_Ltilde|| ~ c * tau for small tau, c = O(1).
  Computed: at tau=0.10, ||K_Ltilde||=3.847e-02 (per C2 direction). For
  tau_min = 0.10, c = 0.385.
Step 4 (direction): KLT_FLOOR = 1e-3 is 38x below the measured min value;
  H2 probes structural nontriviality, not magnitude matching. This floor
  is well above machine noise (1e-16) and well below the physical scale
  (3.8e-2 at tau_min = 0.10).

## Pre-fix actions

1. Add `from canonical_constants import *` — no hardcode violations anyway
   (the script already uses no framework constants; the only numerics are
   geometric — dim_spin=16 from Cliff8, coset index sets, scan tau grid
   inherited from PA-1).
2. Tag local computed scalars in main/diagnostic with `# (local)`.
3. Point script at `computations/_shared/` for PA-1 input (script/output location
   = `computations/_shared/`), since both files are archived.
4. **Bug fix**: Schema mismatch. PA-1 stored `eigvec_{i_tau}_sector_{idx}` +
   `sector_labels_{i_tau}`, but s22b_kosmann_matrix.py expected
   `eigenvectors_{i_tau}_p{p}_q{q}`. Add a schema adapter that reads
   sector_labels to build eigvec_dict[(p,q)] = (eigenvalues, eigenvectors).
5. Add closure-SHA computation and stdout SHA pin logging per §4.5 of plan.

## What PASSES and FAILS mean

**PASS boundary**: This gate confirms the permanent structural theorem that
D_K on SU(3) is block-diagonal in Peter-Weyl, which forecloses any attempt to
generate inter-generation (or inter-sector) coupling from the internal Dirac
operator alone. Three generations cannot emerge from K_a-mediated sector
mixing. The `V(M2) = 4e-6` gap-edge coupling claim from S21b/S22a is thereby
isolated to a different operator (full D_P, or a perturbation) and must be
re-derived in that context.

**FAIL boundary**: Would imply either (a) the Peter-Weyl decomposition fails
numerically, which contradicts 11 prior structural verifications; or (b) K_a
carries a hidden function-space component producing CG-mediated sector
mixing, which would open a new mechanism for generation-mixing.

## Remaining uncomputed

- The inter-sector coupling from the full D_P = D_M + D_K on P = M^4 x K
  (gauge-coupling channel). This is a separate computation (S29/S29a-b).
- The anisotropic-quasiparticle-tunneling channel (see MEMORY.md, sole
  surviving integrability-breaking route, per S56).
