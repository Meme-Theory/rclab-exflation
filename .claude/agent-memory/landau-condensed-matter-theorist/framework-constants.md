---
name: Framework Constants and Structural Walls
description: Key equations, symmetry facts, spectrum structure, proven constraint-map walls — all permanent
type: reference
---

# Framework Constants and Structural Walls

## Symmetry and Order Parameter
- Jensen deformation parameter tau = order parameter for SU(3) shape transition
- Breaking: (SU(3)_L x SU(3)_R)/Z_3 --> (SU(3)_L x SU(2)_R x U(1)_R)/Z_6
- Internal space is **SU(3)** (group manifold), NOT coset SU(3)/(SU(2)xU(1))
- AZ class: **BDI**, T^2=+1. KO-dim: 6. Phi_paasch: 1.531580 at tau=0.15
- V_tree cubic inflection at tau=0: V'''(0) = -7.2 (first-order by Landau criterion)
- d_int=8 > d_uc=4: mean-field EXACT for internal fluctuations
- SUBTLETY: d_eff=1 (one modulus) for moduli fluctuations — different Ginzburg criteria

## (0,0) Singlet Spectrum
- 16 eigenvalues: 3 levels B3 (mult 3), B2 (mult 4), B1 (mult 1) x 2 (PH symmetric)
- B1 gap-edge, non-degenerate, closest to zero
- PH symmetry exact (BDI class), mu=0 forced
- Constant-ratio trap: F/B = 0.55, fiber dimension 44 vs 16

## Key Equations
- Landau: F = F_0 + a_0*(T-T_c)*eta^2 + b*eta^4
- GL: kappa = lambda/xi; Type I < 1/sqrt(2) < Type II
- Pomeranchuk: F_l^{s,a} > -(2l+1)
- Effective mass: m*/m = 1 + F_1^s/3
- Running coupling: alpha_eff = alpha/(1 - (alpha/3pi)*ln(q^2/m^2))
- Critical velocity: v_c = min_p[epsilon(p)/p]

## Proven Constraint-Map Walls (PERMANENT)
1. **Spectral action monotonicity** (S37+S40): ALL single-trace S_f(tau) with monotone f are monotonic on [0,0.5]. No tau-stabilization. 27 total closures.
2. **Block-diagonality** (S22b): D_K exactly block-diagonal in Peter-Weyl. Inter-sector matrix elements = 0 identically.
3. **Clock constraint** (S22d): dalpha/alpha = -3.08*tau_dot. Rolling modulus -> 15,000x violation.
4. **Trap 1** (S34): V(B1,B1)=0 exact (U(2) singlet). V(B1,B3)=0. B1 couples ONLY to B2.
5. **[iK_7, D_K]=0** (S34): SU(3)->U(1)_7 exact in Dirac spectrum. B2=+/-1/4, B1=0, B3=0.
6. **mu=0 forced** (S34): PH symmetry forces mu=0. Helmholtz convex.
7. **Goldstone mass from SA = 0** (S48): Tr[f(D(phi)^2)] = Tr[f(D^2)] for any unitary conjugation. 5-line proof.
8. **BCS universality class** (S43): 3D Ising (Z_2, d=3, n=1). PERMANENT.
9. **a_0/a_2 ratio trap** (S64): Decreasing a_2 off-Jensen INCREASES a_0/a_2 because a_0=const.

## BCS Mechanism Chain — 5/5 PASS (but broken by SA gradient)
- M_max=1.674, E_cond=-0.137, Z=1.016, rho=14.02
- BCS instability is 1D theorem (any g>0)
- Dense instanton gas: S_inst=0.069, tunneling 93%

## Two-Layer Architecture (S72, PERMANENT)
- Spectral (all sectors): governs n_s / gravity / H_0
- BCS ((0,0) only): governs DM / pairs / A_s budget
- 16/155984 weighted eigenvalues in BCS sector = O(1e-4) effect on bulk spectral moments

## Seeley-DeWitt Hierarchy at Fold
- a_4 >> |a_2| >> a_0. Gauge kinetic dominates by 1000:1.
- a_4(K)=0 at Einstein point: gauge kinetics EMERGE from Jensen deformation.
- KK-NCG bridge: R=1/2 exact. sqrt(2/3) = Dynkin index ratio.
