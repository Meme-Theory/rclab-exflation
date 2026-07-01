---
name: Paper Index, Key Equations, and Conventions
description: Baptista paper numbering, critical equation references, 5D moduli parameterization, infrastructure, and workflow lessons.
type: reference
---

# Paper Index, Key Equations, and Conventions

## Paper Groups (57 papers, 52 unique, 5 duplicate pairs: 15=29, 18=34, 19=27, 20=31, 30=35)

| Range | Topic | Priority |
|-------|-------|----------|
| 01-12 | Baptista vortex foundations | LOW |
| 13-18 | Baptista KK-SM (6 papers) | CRITICAL |
| 19-27 | NCG spectral action bridge | MEDIUM-CRITICAL |
| 28-30 | Lichnerowicz stability | CRITICAL |
| 31-34 | Second quantization + S7 spectrometry | HIGH |
| 35-40 | Geometric analysis + DESI | MEDIUM-HIGH |
| 41-46 | Supplementary KK + diff geom | HIGH-MEDIUM |

Full index at `researchers/Baptista/index.md`.

**KK arXiv IDs**: 13=2105.02899, 14=2105.02901, 15=2306.01049, 16=2406.09503, 17=2506.09126, 18=2601.08902.

## Key Equation References

| Equation | Paper | Content |
|----------|-------|---------|
| 1.5 | 13 | R_P = R_M + R_K - |F|^2 - |S|^2 - |N|^2 - 2div(N) |
| 2.37 | 13 | Volume form; Jensen restriction makes constant |
| 3.35 | 13 | f = const on Jensen (volume-preserving) |
| 3.41-3.42 | 13 | Kinetic term for Higgs line bundle; U(1)_{N_pair} Noether |
| 5.21, 5.25 | 13 | sin^2(theta_W) = 3*L2/(L1+3*L2); coupling ratios |
| 2.25, 2.37 | 14 | Fiber integration = CG selection rules |
| 2.62 | 14 | L_v, R_v actions on Psi_+ |
| 2.65 | 14 | L-failure = Higgs = order-one constraint |
| 2.85, 2.88, 2.93 | 14 | g' = 3*sqrt(2kM/<Y,Y>), <Y,Y>=6*L1; g = sqrt(2kM/<T3,T3>) |
| 3.58 | 15 | su(3) = u(1) + su(2) + C^2 |
| 3.60 | 15 | General U(2)-invariant metric (3D family) |
| 3.62 | 15 | Ad(U(2)) action on su(3) |
| 3.65 | 15 | **OCR GARBLED — DO NOT USE** |
| 3.67, A.28 | 15 | Lie derivative DeWitt metric |
| 3.68 | 15 | Jensen scale factors lambda_1=e^{2s}, lambda_2=e^{-2s}, lambda_3=e^s |
| 3.70 | 15 | R(s) = (3/2)*(2*e^{2s} - 1 + 8*(e^{-s} - e^{-4s})) DEFINITIVE |
| 3.79 | 15 | Two-field Lagrangian (phi, sigma), kinetic 1/2 and 5/2 |
| 1.2, 7.1 | 16 | Mass variation from d_A g_K != 0 (geometric expansion) |
| 9.5 | 16 | Null geodesic metric (no rho_s needed) |
| 3.8, Cor 3.4 | 17 | D_P decomposition; D_K = mass term |
| 4.1 | 17 | Kosmann with antisymmetric covariant derivative |
| 4.7 | 17 | Correct chiral observable: [D_K, L_{e_a}] commutator |
| 1.1 | 17 | Chirality proposition |
| 1.4 | 18 | L_tilde_V (new Lie derivative, closure property) |
| 7.5 | 18 | M = <phi, D_K phi> = D_F (dim-reduced Dirac) |
| App B | 18 | BG spinor comparison map (tilde{Phi}) |
| App E | 18 | Z_3 x Z_3 -> three generations |

## 5D Moduli Parameterization

- Jensen tangent: v_J = (2, -2, 1). Volume normal: n_V = (1, 3, 4). v_J . n_V = 0.
- T1 (breathing): (7, 11, 8). T2 (cross-block, vol-preserving): (-11, -7, 8).
- T3 (su(2) aniso): breaks Ad(SU(2)) on su(2). T4 (C^2 aniso): breaks Ad(SU(2)) on C^2.
- Off-Jensen gauge coupling: g_1/g_2 = sqrt(L2/L1).
- Weinberg angle: sin^2(theta_W) = 3*L2/(L1+3*L2). SM=0.231 requires eps_T2=0.049 from Jensen s=0.35.
- R normalization: our R=2.000 vs Baptista R=1.500 at round (factor 4/3, Killing form convention).
- g_0(T_a, T_b) = (1/2)*delta_ab where T_a = lambda_a/2.
- Milnor formula sign: R = -(1/4)T1 - (1/2)T2 (NOT +T2/2).

## Infrastructure

- Jensen metric: e^{2tau}(u1), e^{-2tau}(su2), e^{tau}(C^2), volume-preserving
- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- C2_IDX = [3,4,5,6], SU2_IDX = [0,1,2], U1_IDX = [7]
- NumPy 2.x: use np.trapezoid (not np.trapz)

## Workflow Lessons

- NEVER write synthesis before cross-talk arrives. Wait for responses, integrate, THEN mark complete.
- "Simultaneously real and purely imaginary" is common proof error — verify constraints independent.
- Wigner-Eckart on abstract rep theory can be TOO STRONG for Dirac — Clifford correlations.
- Don't extrapolate matrix norm statistics to specific algebraic tests.
- K-1e lesson: ALWAYS sum over ALL generators, not just a subalgebra.
- V MATRIX LESSON (S34a): A_antisym (frame indices) != K_a_matrix (spinor indices). NEVER use A_antisym for BCS pairing. Error propagated S23a-S33b (11 sessions).
- NEVER use d^2(Tr D_K)/dtau^2 (= 0 by tracelessness). Use sum|lambda| or f(D^2).
- Convention warning: S41 "a_k" (spectral zeta) != S60 "a_k" (power sums) != Gilkey a_k (heat kernel).
