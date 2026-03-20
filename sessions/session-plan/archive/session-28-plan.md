# Session 28 Plan

**Date**: 2026-02-27
**Motivation**: Session 27 delivered a T-1 PASS (torsion weakens the spectral gap by 33-78%) and a CONDITIONAL RESCUE (ERRATIC) from multi-sector BCS, while the four-reviewer collab review converged unanimously on torsionful BCS as the single most important uncomputed quantity and identified a concrete 5-step Constraint Chain for the 1D phonon collision mechanism.
**Prerequisites**: Session 27 data files (`s27_torsion_gap_gate.npz`, `s27_multisector_bcs.npz`), Session 19a sweep data (`s19a_sweep_data.npz`), Session 23a eigenvectors (`s23a_eigenvectors_extended.npz`, `s23a_kosmann_singlet.npz`), Session 25 spectral action data (`s25_*.npz`).

## Strategic Context

Post-Session 27, the T-1 PASS confirmed that D_can has a weaker spectral gap than D_K -- the obstruction that would have closed the torsion channel is removed. The multi-sector BCS showed an interior minimum at tau=0.35 (mu/lambda_min=1.20) but it is erratic (sector on/off transitions) and not self-consistent without an external source of chemical potential. The collab review converged on two themes: (1) torsionful BCS is the #1 unexplored degree of freedom (3/4 reviewers), and (2) the 1D phonon collision mechanism provides a physically coherent route to an effective mu via parametric amplification. Session 28 tests both threads through a structured Constraint Chain plus the decisive D_can BCS computation.

## Session Architecture

- **28a**: Zero-Cost Diagnostics + Torsionful BCS -- All post-processing of existing data (6 computations, <30 min) plus the single highest-priority new computation (torsionful BCS kernel), which was endorsed by 3/4 reviewers.
- **28b**: Landau Diagnostics + NCG Axiom Gates -- Deep condensed matter diagnostics (relaxation times, Pomeranchuk map, quasiparticle weight, cubic invariant, self-consistent tau-T) and the critical NCG order-one condition for D_can.
- **28c**: Constraint Chain Completion + Structural Gates -- The 1D phonon-phonon T-matrix (KC-2), conditional Constraint Chain steps KC-3 through KC-5, the 12D spectral triple axiom verification (C-6), and structural diagnostics (periodic orbits, Berry curvature at transitions, sector convergence).

## Priority Map

| ID | Name | Session | Cost | Input Data | Depends On |
|:---|:-----|:--------|:-----|:-----------|:-----------|
| KC-1 | Parametric injection rate | 28a | Zero | s19a_sweep_data.npz | None |
| L-1 | Thermal spectral action | 28a | Zero | s25 + s27 data | None |
| E-1 | Lichnerowicz gap decomposition | 28a | Zero | s27_torsion_gap_gate.npz | None |
| C-1 | Spectral action S_can vs S_LC | 28a | Zero | s27 D_can eigenvalues | None |
| C-4 | Spectral correlation R_2(s) | 28a | Zero | s27 multi-sector spectra | None |
| S-2 | M_max vs C_2 dispersion | 28a | Zero | s27_multisector_bcs.npz | None |
| E-4/S-1/L-4 | **Torsionful BCS** (merged) | 28a | Low | s27 D_can spectra + BCS code | None |
| C-3 | Order-one condition for D_can | 28b | Low | s8 J matrix + s27 M_Lie | None |
| L-3 | Landau-Khalatnikov relaxation | 28b | Low | s27 M_max interpolation | None |
| L-5 | Per-sector Pomeranchuk map | 28b | Low | s27 V_max + eigenvalues | None |
| L-6 | Quasiparticle weight Z(tau) | 28b | Low | s27 D_can + D_K eigenvectors | None |
| L-7 | Self-consistent (tau, T) min | 28b | Low-Mod | s25 + s27 combined | L-1 |
| L-9 | Cubic invariant / first-order | 28b | Low | s27 F_total boundaries | None |
| S-3 | Hessian of F_total at min | 28b | Low | s27 F_total data | None |
| E-5 | Lambda_eff from condensation | 28b | Low | s27 interior min energy | None |
| KC-2 | 1D phonon T-matrix | 28c | Moderate | s23a eigvecs + a_4 coeffs | KC-1 PASS |
| KC-3/4/5 | Constraint Chain completion | 28c | Follows KC-2 | KC-1 + KC-2 outputs | KC-2 PASS |
| C-6 | 12D spectral triple axioms | 28c | Moderate | s20a metrics + s8 J | C-3 |
| E-3 | Duistermaat-Guillemin orbits | 28c | Moderate | Jensen metric geodesics | None |
| S-4 | Berry curvature at transitions | 28c | Low | s23/s27 BCS solutions | None |
| L-8 | Sector count at p+q<=4 | 28c | Moderate | Extend s27 computation | None |

## Constraint Chain (Landau, from Master Collab)

| Step | Computation | Session | Condition for CLOSED |
|:-----|:-----------|:--------|:-------------------|
| KC-1 | Parametric injection rate (Bogoliubov |beta_k|^2) | 28a | |beta_k|^2 ~ 0 everywhere -- no drive |
| KC-2 | 1D phonon-phonon T-matrix | 28c | W << Gamma -- no bottleneck |
| KC-3 | Steady-state mu_eff from kinetic equation | 28c | mu_eff < lambda_min -- gap not filled |
| KC-4 | Luttinger parameter K (fermionization) | 28c | K >> 1 -- no Fermi surface |
| KC-5 | BCS gap with van Hove DOS | 28c | Delta = 0 -- pairing too weak |

KC-1 is the gateway. If Bogoliubov coefficients vanish, the entire 1D phonon mechanism dies and 28c redirects to structural gates only.

## Success Criteria

Session 28 is successful if it produces definitive gate verdicts for:
1. **KC-1**: Does parametric amplification from the evolving Jensen metric generate phonon injection? PASS/CLOSURE.
2. **Torsionful BCS (E-4/S-1/L-4)**: Does ANY sector in the D_can eigenbasis cross M_max > 1 at mu = 0? PASS/CLOSURE.
3. **C-3**: Does the order-one condition hold for M_Lie (the algebraic part of D_can)? PASS/CLOSURE.
4. **L-7**: Does the finite-temperature spectral action have a non-trivial minimum in (tau, T) space? PASS/CLOSURE.
5. **KC-2 (conditional)**: Does the 1D phonon-phonon scattering rate establish a thermalization bottleneck? PASS/CLOSURE.

The single decisive question: **Does D_can (torsionful) produce BCS condensation where D_K (torsion-free) could not?**
