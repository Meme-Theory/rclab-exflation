---
name: S83 Cartan Protection Cluster (G17, G20, G22, G54, G62)
description: Consolidated S83 W2-W3 Cartan-protection theorem cluster -- §VII.J landing, HP^even completeness audit, Spin(8) sanity, quantum/nonabelian extensions
type: project
---

## §VII.J landing (S83 W3-G62) -- PASS

Closure SHA: `711a0be75ff7cebba2651e2c7fe9bf181d48421cccf7b82227bcad160d13d1ac`. Registry §VII.J (between §VII-B and §VII.K, ~170 lines in `sessions/permanent-results-registry.md`). Working paper §W3-G62 (subsections .1-.8). 26/26 anchors, 9/9 gates in ledger AND registry, 9/9 classifications match.

**Theorem (Level-2 Cartan Exclusion, rank-scaling refined R2 post-G18)**: HC^2_primary(C) = 0 for any abelian Cartan subfactor C of (A, H, D) in simply-laced core. Protection scales with rank:
- r >= 2 (simply-laced A_n, D_n, E_6, E_7, E_8): drift_u1 ~ 0 to noise floor by Weyl-equivalence
- r = 1: HC^2 vanishes structurally (H^2_dR(S^1) = 0); margin weaker by ~1 order in 1/sqrt(N)
- Non-simply-laced (G_2, F_4): FALSIFIED -- drift_u1(G_2, L=8) = 4.11%, outside CLT band

**Preservation table**:
| Clause | Mechanism | Gate |
|:---|:---|:---|
| (a) | Abelian Künneth G x U(1) | G19 PASS, dev=1.2e-5 |
| (b) | Quantum U_q deformation at generic q | G20 PASS, 4-route |
| (c) | Inner-fluctuation Kasparov orbit | G23 PASS, cartan_resid_max=0 |
| (d) | Non-flat Jensen T-correction | G24 PASS, P_1|Cartan=0 pointwise |

**Other gates**: G21 PASS HC^4=0 (Connes periodicity); G22 PASS nonabelian SU(2); G17 PASS Spin(8) sanity (drift_u1=9.05e-9); G18 FAIL-BY-DESIGN G_2; G54 PASS HP^even-scope.

**How to apply**: If a future computation reduces an obstruction to a pairing on the Cartan subfactor of a simply-laced ambient group, the obstruction vanishes by §VII.J -- no regulator-scan needed. NOT universal: G_2/F_4 and exceptional require case-by-case classifier.

## G20 -- Quantum Cartan Protection (extension to U_q(su(2)))

**SHA**: `a119f3d1ce0ad92039e86af1e44c14be53c4303c6756ad64543d5bacf4d993a2`

HC^2_primary(U_q(su(2))_Cartan) = HC^2(C[K, K^{-1}])/S(HC^0) = 0 at generic q (not root of unity). Cartan sub-factor commutative, isomorphic to C(S^1). 4-route confluence: (A) HKR+SBI, (B) H^2_dR(S^1)=0, (C) q-scan uniform at 0 for q in {0.3, 0.5, 0.7, 1/sqrt(2), 1/pi}, (D) pullback i*(HC^2_primary(A_theta))=0. Root of unity case NOT covered.

## G22 -- Nonabelian SU(2) Protection

**SHA**: `a2404ce6a831388224a67a6543c4c96d9bca4db65e8bd8f55dc041cb085aa2b9`

HC^2_primary(SU(2)_Cartan_sub) = HC^2(C^inf(S^1))/S(HC^0) = 0. SU(2) rank 1; T^1_{SU(2)} ~ S^1; H^n_dR(S^1)=0 for n>=2. Pullback i*: HC^2(T^2_{SU(3)}) -> HC^2(T^1_{SU(2)}) kills volume 2-form. 4-route confluence (HKR+SBI, H^2_dR(S^1), simplicial, T^2->T^1 pullback).

**Three orthogonal dimensions covered**:
- Group: abelian (G16-G19) / nonabelian (G22)
- Quantization: classical (G16-G19, G22) / quantum (G20)
- Degree: Level-2 HC^2 (G16-G20, G22) / Level-3+ HC^{2k} (G21)

## G17 -- Cartan Spin(8) Sanity

**SHA**: `6f2b628da96950b8917aaff0809dd6f92764ce63f58cb7da55edaa2d170a37cf`

drift_u1(Spin(8), L=8)=9.05e-9; drift_u1(Spin(10), L=8)=1.56e-6; drift_u1(Spin(12), L=8)=1.83e-5. All below NOISE_FLOOR=1e-3. Pure Cartan T^r of simply-laced D_n -> drift_u1=0 structurally by Weyl-equivalence (|alpha|^2=2 uniform; n -> -n cancels odd-power root-projections). N_modes(D_4=Spin(8), L=8)=20,185 sphere cutoff.

**Noise-floor rule**: When |b| could be at noise floor in a relative deviation rule |a-b|/|b| < thresh, require absolute |a| < NOISE_FLOOR AND |b| < NOISE_FLOOR to classify PASS (family-consistent at noise floor) rather than divide-by-near-zero FAIL.

## G54 -- HP^even Completeness Audit of §VII -- PASS

**SHA**: `1d2bde0ce48eb54d9eef40fa7a8c6c0152bff77b8155432a3c5436dbcdac45e0`

53/53 rows classified. 4-bucket classifier:
- **P** (HP^even-primary): polynomial in bare-triple invariants. 35 rows.
- **CM** (CM-extension): inner fluctuation OR Hopf H_1 transgression. 7 rows.
- **M** (MIXED-KK-class): pinning-dependent. 10 rows.
- **GV** (Godbillon-Vey-excluded): NOT admissible per CE6. 1 row (epsilon_H = 0.02163 from W1-G2 FAIL carry-forward).

| Sub | Total | P | CM | M | GV |
|:---|:--|:--|:--|:--|:--|
| VII-A | 29 | 21 | 1 | 7 | 0 |
| VII-B | 24 | 14 | 6 | 3 | 1 |
| Total | 53 | 35 | 7 | 10 | 1 |

W1-G2 FAIL carry-forward honored (epsilon_H -> GV). W1-G6 INFO compatible (4-bucket congruent with §VII.K-DUAL {FI, RD, MIXED, G-V}).

## Landing methodology (audit pattern reuse)

Generalizable §VII.X registry-landing template:
1. Anchor checklist (case-sensitive substring match)
2. Carry-forward gate cross-check (ledger + registry)
3. Classification match (PASS/FAIL/INFO per gate)
4. Direction rule (4 boolean aggregates)
5. Closure SHA over pin-map-str

S84 carry-forwards: rank-2 exceptional refinement (G_2/F_4 short-long-root-weighted Weyl), non-simply-laced products (Spin(5)xU(1), G_2xU(1) Künneth), full Cartan-commuting 1-form cohomology.
