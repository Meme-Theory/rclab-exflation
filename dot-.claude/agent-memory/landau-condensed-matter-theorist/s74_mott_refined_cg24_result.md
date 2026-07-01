---
name: S74 MOTT-REFINED-CG24-74 Result
description: Refined Mott delta_OOM = 0.1411 OOM using canonical E_C = 0.4643 and sector-specific J via C^2 branching. INFO gate. C^2 confined. Compound with dispersive = 0.2911 vs target 0.267 (+0.024 OOM residual, resolves S73A over-closure).
type: project
---

# S74 MOTT-REFINED-CG24-74 — Sector-Specific Mott Decoherence

**Gate**: MOTT-REFINED-CG24-74 = **INFO**
**Verdict**: delta_OOM_total = 0.141074 in info band [0.10, 0.40] but below pass band [0.18, 0.28]. C^2 contribution exactly zero (structural, < 1e-6).

## Key Numbers

| Quantity | Value |
|:---------|:------|
| E_C canonical (W1-D Method A OES) | 0.4643 M_KK |
| J_C2 (per bond) | 0.933 M_KK |
| dim(SU(2) branch), dim(U(1) branch), dim(C^2) | 4, 2, 0 (sum=6=z_CG24) |
| J_{SU(2)} = J_C2 * 4/2 | 1.866 M_KK |
| J_{U(1)}  = J_C2 * 2 | 1.866 M_KK |
| J_{C^2}  | 0 (confined) |
| delta_OOM_{SU(2)} | 0.07054 |
| delta_OOM_{U(1)}  | 0.07054 |
| delta_OOM_{C^2}   | 0 (structural) |
| **delta_OOM_total** | **0.141074** |

## Formula

`delta_OOM_a = log10(1 + sqrt(E_C / (8*J_a)))` — quantum-rotor phase-diffusion OOM.

## Key Results

1. **Reduction from S73A baseline**: 0.336 -> 0.141 (2.38x). Combined effect of (a) Method A canonical E_C instead of geometric mean, (b) log10(1+sqrt) formula instead of delta_phi^2/(2*ln10).

2. **Resolves S73A W4-B over-closure**: Compound (refined Mott 0.141 + dispersive 0.150) = 0.2911 vs target 0.267. Residual +0.024 (was +0.219 OOM in S73A). Nearly exact closure of A_s budget.

3. **C^2 confinement structural**: The C^2 intrinsic sector has no Josephson coupling at the fold (broken by deformation). delta_OOM_{C^2} = 0 is not an approximation; it is a structural statement of zero phase coherence in a confined sector.

4. **SU(2)/U(1) degeneracy**: Both sectors give identical J_a = 1.866 M_KK after branching rules (SU(2) dim 4 / 2 = U(1) dim 2 / 1 = 2). Physically distinct but numerically degenerate for Mott floor.

5. **E_C sensitivity confirms Method A**: Method C (0.061) gives delta_OOM=0.053 (under-decoheres). Method B (9.01) gives delta_OOM=0.498 (over-decoheres). Only Method A (0.4643, W1-D canonical) produces sensible Mott floor.

## Cross-checks (all PASS)

- Linearity: exact (error 0.00e+00)
- E_C -> 0: delta_OOM -> 0 (PASS)
- J -> 0+: diverges as ~1/sqrt(J) (PASS); structural exception at J=0 gives 0
- Monotonicity in E_C: 0.102 < 0.141 < 0.193 (PASS)
- S73A comparison: 2.38x reduction matches Hawking-workshop prediction (PASS)
- Compound budget: 0.2911 within 0.05 OOM of target 0.267 (PASS)

## Files

- `computations/s74_mott_refined_cg24.py`
- `computations/s74_mott_refined_cg24.npz`
- `computations/s74_mott_refined_cg24.png`

## Classification

**PHONONIC**. Static phase-diffusion signature of the CG(24) Josephson network's ground state at quantum-critical E_J/E_C ~ 4 on canonical E_C.
