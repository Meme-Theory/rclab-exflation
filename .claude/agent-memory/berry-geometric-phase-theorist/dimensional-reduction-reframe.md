---
name: Berry Phase as SU(3)->SU(2) Dimensional Reduction
description: Berry curvature on SU(2) EMERGES from SU(3) projection via C^2 cross-terms. Quantum metric is the reservoir. S36 paradox dissolves.
type: project
---

## Core Insight (S61 Addendum, 2026-03-28)

Berry curvature = 0 on SU(3) (Kosmann anti-Hermiticity). But SU(2) is embedded in SU(3) via su(3) = u(1) + su(2) + C^2. The PROJECTION Pi_{su(2)} onto the su(2) sub-bundle GENERATES nonzero Berry curvature from the C^2 cross-terms.

**Why:** The projected connection A^{su(2)} picks up a commutator [A^{C^2}, A^{C^2}]|_{su(2)} that is nonzero because [C^2, C^2] has a nonzero su(2) component (A-tensor, |A|^2 = 3/2 + 3/2 e^{-4tau}). The projection breaks anti-Hermiticity: Pi K_alpha Pi is NOT anti-Hermitian on the su(2) subspace when alpha is a C^2 index.

**How to apply:** Every Berry SU(2) result (Papers 01,02,03,04,06,08,10,13,16,18,21) is EMERGENT from SU(3) projection. Papers about SU(3)-level structure (09,11,12,14,15,17,19,20,22) apply directly. The quantum metric g=982.5 is the RESERVOIR from which su(2) Berry curvature is drawn: Re(QGT) on SU(3) becomes Im(QGT) on SU(2).

## Key Equations
- eq PR-3: Omega^{su(2)} = Omega^{full}|_{su(2)} + [A^{C^2}, A^{C^2}]|_{su(2)}. First term=0, second term nonzero.
- eq PR-4: Omega^{su(2),eff}_{ij} = sum_{C^2} f_{i,alpha,beta} <n|K_alpha|m><m|K_beta|n>/(E_n-E_m)^2
- eq MECH-2: |Omega^{su(2),eff}| ~ Re(QGT)|_{C^2 cross-block}
- KK analogy: Berry curvature : SU(2) :: gauge field F_{mu,nu} : KK compactification

## Calculation F (pre-registered)
Compute projected Berry curvature on su(2) subspace of 16D spinor. Tests:
1. Omega != 0 on projected space
2. Magnitude ~ quantum metric of C^2 cross-block
3. Monopole structure at projected degeneracies
4. Chern number = integer

## Status
- Structural argument COMPLETE (addendum written in session-61-berry-relook.md)
- Quantitative test (Calc F) UNCOMPUTED
- S36 paradox DISSOLVED by reframe: "sensitivity without protection" on SU(3) = "sensitivity WITH protection" on su(2)
