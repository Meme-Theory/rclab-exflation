---
name: Early Sessions Reference
description: Consolidated reference for sessions 6-21: NCG bridge, V_eff closure chain, phi recheck, Cartan flux, algebraic traps, session 16-21 details
type: reference
---

# NCG Bridge (Sessions 6-11)

## A_F Derivation
- End_{U(2)_LR}(Psi+) = C + M_2(C) + M_3(R) + R (dim 20). NOT A_F.
- With J on C^32: 128-dim J-compatible commutant, 3 factors.
- Order-zero selects A_F = C + H + M_3(C) (dim 24) as maximal compatible subalgebra.
- R_u(2) is correct gauge: electroweak Killing symmetry of Jensen SU(3).

## Order-One (Sessions 10-11)
- 5/9 factor pairs PASS (M_3(C) sector). 4/9 C+H FAIL.
- Order-one subalgebra from L-closure: dim 20 = C + M_3(C). Missing H (requires bimodule).
- Chirality: gamma_F = ROW-BASED internal chirality (NOT particle/antiparticle grading).
- Barrett existence: valid D_F guaranteed for KO-dim 6 + dim 32.
- AZ class: BDI (T^2=+1). Corrected from DIII in S17c.

## Key Scripts
- `phase25_connes_embedding_test.py`, `phase25_DF_on_Lclosure.py`, `phase25_wedderburn_detail.py`, `branching_computation.py`

# V_eff Closure Chain (Sessions 13-20b)

All 7 perturbative spectral mechanisms exhausted. NP physics required.

1. V_tree minimum (17a SP-4)
2. 1-loop CW (S18): fermion-dominated, monotone. 714 scalar + 1456 vector eigenvalues.
3. Casimir scalar+vector (19d): R=F/B=9.9 constant. DOF ratio 439,488F/52,556B = 8.36.
4. Casimir WITH TT (20b): R=0.55 boson-dominated (TT flips ratio), monotone positive. 741,652 TT DOF.
5. Fermion condensate (19a): spectral gap > 0.
6. Seeley-DeWitt a_2/a_4 (20a).
7. False vacuum double-counting (19a): F_spectral IS dV_CW/dtau.

Key lessons: On compact manifolds, fermion/boson DOF ratio dominates ALL polynomial weightings. Koiso-Besse instability is CONFORMAL only, not TT. Rough Laplacian on constant tensors is NOT zero.

# Phi Recheck (Session 13b)

- IVT margin = 0.38%: (3,0)/(0,0) starts 1.5275, max 1.5374 at s~0.08, crosses phi at s~0.15.
- (3,0) UNIQUELY saturates Parthasarathy bound: lambda^2*36 = 63 = pred 63.
- s=ln(phi) is TAUTOLOGY. sigma doesn't select psi_0=0.15.
- V_eff fourth parameter (mu): psi_0=0.15 needs kappa~212 (unnatural).
- Eigenvalue data (s=0, lambda^2*36): (0,0):{27}, (1,0):{25,37,49}, (1,1):{27,45,63,75}, (2,0):{37,49,61,79}, (2,1):{49,61,73,91,97,109}, (3,0):{63,81,93,117}

# Cartan Flux + FR Double-Well (Session 21b)

- |omega_3|^2(tau) = (1/2)e^{-4tau} + 1/2 + (1/3)e^{6tau} (EXACT, verified <2e-13 at 21 points)
- V_FR(tau) = -alpha*R_K(tau) + beta*|omega_3|^2(tau). tau=0 ALWAYS local min.
- Critical ratio: beta/alpha = 0.313. Below -> true min at tau_0 > 0.
- Weinberg chain: g_1/g_2=e^{-2tau} -> sin^2(theta_W)=0.231 => tau_0=0.2994 => beta/alpha=0.28
- Instantons: 4D gauge CLOSED (tau-indep). Internal YM CLOSED (monotonic). Euclidean grav OPEN.
- Flux >> metric deformation at FR min (81 vs 0.81). S_bounce~0.2. G_tt=5.

# Phase 0 Results (Session 21c)

- T''(0) = 7,969 (unweighted), 3.67e5 (weighted). POSITIVE. 89% from p+q=5-6.
- S_signed: Monotonically decreasing. CP-1 REFUTED.
- b_1/b_2 = 4/9 EXACTLY (Dynkin: Tr(Y^2)/Tr(T_a^2) = (2/3)/(3/2)).
- Three-monopole structure: M0(tau=0), M1(tau~0.10), M2(tau~1.58). Physical window [0,1.58].

# Sessions 16-21 Details

- D_K on (SU(3), g_s) IS correct mass operator per Baptista Corollary 3.4.
- Peter-Weyl: L^2(SU(3),S) = bigoplus V_(p,q) x V_(p,q)^* x C^16.
- LEFT U(2) (gauge) acts on V_(p,q)^*. RIGHT Z_3: gen = (p-q) mod 3.
- (3,0) U(2)-singlet CONFIRMED: unique C^1_{-3} in Sym^3(C^3).
- ALL Dirac eigenvalues are FERMIONIC (negative CW sign).
- CRITICAL: collect_spectrum() line 1328: eigvals(D) -> eigh(1j*D).
