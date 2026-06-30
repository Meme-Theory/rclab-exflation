---
name: Feynman Test Scorecard & Constraint Map
description: Feynman Test scorecard (7 steps), constraint map walls, structural results, forward program, Ricci gauge
type: project
---

## Feynman Test Scorecard

| Step | Status |
|------|--------|
| 1. Action | CLOSED (spectral action). S_occ min sharp cutoff only. Zeta-reg TBD. Post-transit EFT DONE (S55: 8-mode L_eff with V_kl). |
| 2. Propagators | DONE -- G_BdG anomalous. Lattice 8-mode TB propagator. |
| 3. Vertices | DONE+AMP -- S52 QP-QP vertex. S54: Lattice V_kl from Kosmann. |
| 4. Power count | DONE+RG -- 1D marginal. Lattice d/Delta=42, pairing collapse. Threshold CLOSED (4 OOM mismatch). |
| 5. Compute something | S52 AMP PASS. S54 ED-SWEEP FAIL (193x). SA-LATT-OCC PASS (5.35% barrier sharp cutoff). |
| 6. Unitarity | OPT-35 PASS 2.2e-12. S55 OPTICAL-THEOREM PASS 1.1e-15 (lattice T-matrix). |
| 7. Compare to data | sin^2=0.584 FAIL. Threshold CLOSED. FIRAS PASS (BF=1). n_s=0.501 FAIL. w_0=-1 PASS. |

## Constraint Map Walls

- **W4 (spectral action monotone)**: CONFIRMED Jensen + transverse. HESS-40: 22/22 positive, min H=+1572, margin 1.57e7. Jensen fold = 28D local minimum.
- **W_Josephson (S56)**: E_J(tau) monotone decreasing + E_J/E_c>>1 => F_fabric monotone. Structural, N_cell-independent.
- **W_integ_Josephson (S56)**: Isotropic Josephson preserves R-G integrability. Random control: <r>=0.543 (GOE).
- **W_J_Majorana (S60)**: [J,D_K]=0 forces M_R real => epsilon_1=0 exact. Universal CP shield.
- W1-W3, W5-W6: unchanged from s36.
- **27 total equilibrium closures** (S17a through HESS-40). Search COMPLETE.
- QRPA stable: margin 3.1x, V_rem time-even.
- Quantum delocalization CLOSED: sigma_ZP=0.026, M_ATDHFB=1.695.

## Key Structural Results (persistent)

- KO-dim=6 (parameter-free). SM quantum numbers C^16. [J,D_K]=0. g1/g2=e^{-2tau}.
- Lambda_min turnaround: tau=0.2323, depth 6.28%
- Van Hove DOS: g(omega) ~ 1/sqrt(omega-omega_min) at 1D band edge
- V_spectral(s) monotonically increasing -- internal spectral action alone INSUFFICIENT
- B2 near-integrable island: Poisson <r>=0.401, rank-1 86%, g_T=0.087
- Transit classical: sigma_ZP=0.026, M_ATDHFB=1.695
- Compound nucleus dissolution IS the framework (not equilibrium stabilization)
- BDG-SPECTRAL-DET-53: log det(D_BdG^2) MONOTONE (inherits W4). Wrong bridge functional.
- S_F^Connes = 0 identically (BDI T-symmetry). Pfaffian channel monotonic (S41).

## Forward Program

- **Computation A**: Heat kernel at finite density. delta_a_2 = -N_pairs * Delta^2. Computable from existing data.
- **Computation B**: KK graviton mass from HESS-40 eigenvalues. Compare to BCS gap hierarchy.
- **Computation C**: DELIVERED (S55 EFT-RULES-55). Post-transit L_eff, full Feynman rules.
- **Insight**: GSL monotonicity = spectral action monotonicity (same fact, different language).
- **Insight**: T_acoustic 0.7% may derive from one-loop det'(-d^2/dtau^2 + alpha).
- **CRITICAL OPEN**: Zeta-regularized Gamma[tau] = S_cl + (1/2) Tr log D^2 from existing eigenvalue data.

## Ricci Gauge Kinetic (s35, VERIFIED)

- Ric_su2/Ric_u1 at s=0.190: 0.832 (sin^2_combined = 0.333 with NCG 3/5 trace)
- RGE MATCH at M_KK=10^{10.06} GeV (0.3%)
- Spin Casimir PERMANENTLY EXCLUDED: sin^2=0.523 > 3/8

## Library Gaps (S42 audit, still open)

- **Heat kernel manual**: Vassilevich hep-th/0306138 (Priority A; used every spectral computation)
- **One-loop spectral action**: van Nuland & van Suijlekom arXiv:2107.08485 (Priority A; needed for Comp C quantization)
- **Spectral action principle**: Chamseddine & Connes hep-th/9606001 (founding paper)
- **Parker particle creation**: Parker & Navarro-Salas arXiv:1702.07132 (S38 transit IS Parker creation)
- **Richardson-Gaudin / GGE**: Claeys arXiv:1809.04447 (central to S38-42)
