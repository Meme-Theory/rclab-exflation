---
name: Structural Anchors (Computations + Paper Audit)
description: 24-computation registry through S62 + 16 paper-audit fixes (provenance). Compressed from former computation-registry.md + berry-audit-log.md.
type: project
---

## Computation Registry (24 total through S62)

| # | Name | Sess | Verdict | Result |
|---|------|------|---------|--------|
| 1-13 | S21b-S25 suite | 21-25 | Various | Spacings, rigidity, metric, Chern, d_FS, Wilson |
| 14 | Landau-Zener | 28d | MOOT (PERM) | Codim mismatch |
| 15 | BDI winding | 36 | nu=0 TRIVIAL | mu=0+E_B2>0 => det(q)>0. 33x from transition |
| 16 | Zak phase | 48 | ARTIFACT (RETR) | Index-tracking, not topology |
| 17 | Non-Abelian Wilson | 48 | TRIVIAL | KS p=0.52, uniform phases. L2 CLOSED |
| 18-19 | Berry completion+Dissolution | 48 | 0/10 | All pi-phases vanish at eps=0.1*eps_c |
| 20 | GL band Berry | 53 | DOUBLY TRIVIAL | V_cross=0, Zak=0 all 6 bands. Im(A_n)=0 |
| 21 | Berry around fold | 55 | gamma=0 | No degen 2D. Min gap 0.031. Real-symm H |
| 22 | Fabric Josephson holonomy | 56 | L6 CLOSED | Rank-1 preserves R-G integrability |
| 23a | Higgs order-one isolation | 62 | PASS | (1,2,Y=1) dim=64, mix=3.5e-14. 10 exact irreps |
| 23b | BERRY-PROJECTION-62 | 62 | PASS | \|A_coset\|^2=2.2015 EXACT. CF-9. O'Neill factor 3 |

## Topological Triviality Chain (L0-L7, ALL trivial on Jensen line)
- L0: Berry curvature = 0 (Kosmann anti-Hermiticity)
- L1: Chern = 0
- L2: Wilson loop = trivial
- L3: Zak phase = artifact
- L4: BDI winding = 0
- L5: GL band = doubly trivial
- L6: Fold Berry = 0
- L7: Fabric holonomy = trivial

## Open Gates (S61+)
1. **P-30w**: Off-Jensen Berry curvature. HIGHEST PRIORITY.
2. **QGT-EIGENVALUES**: Quantum metric tensor diag in 36D moduli space.
3. **FIDELITY-SCALING**: chi_F(tau) near fold. Test A_2 vs QPT (Paper 17).
4. **N-PARTICLE-BT**: Paper 10 trace formula for Richardson-Gaudin BCS.

## Paper Audit Log (2026-02-21; 16 fixes across 10 files)

### Author/citation corrections
- Paper 06 (Maslov): added K.E. Mount co-author; J. Phys. A 5:341 -> Rep. Prog. Phys. 35:315
- Paper 09 (Catastrophe Optics): added C. Upstill co-author
- Paper 10 (BGS): PRL 56:2256 -> Proc. R. Soc. A 400:229
- Paper 12 (Trace Formula): K.E. Keating -> J.P. Keating; pp 4839-4866 -> 4839-4849
- Paper 11 (QHE/Chern): fabricated PRB 31:3794 -> composite (Berry PRSA 392, TKNN PRL 49, Xiao/Chang/Niu RMP 82)
- Paper 14 (Synthesis): fabricated RMP 81:1441 -> composite Berry pubs 1988-2010
- Paper 07 (Optical Vortices): J. Opt. A 15:207 -> Proc. SPIE 3487:1
- Paper 08 (Pancharatnam): Nature 326:277 -> J. Mod. Optics 34:1401

### Math corrections
- Paper 01: "gauge-dependent" wrong for closed loops -> gauge-invariant mod 2pi, continuous, quantized to pi only at diabolical points
- Paper 03: nonsensical self-referential gap formula -> correct two-level avoided crossing; "Quantum Dots" -> "Triangles"
- Paper 07: removed self-correction garble; m^2 pi -> winding 2pi*m
- Paper 10: GOE label on GUE form factor -> labeled GUE + added GOE form
- Paper 11: anomalous velocity sign error fixed (3 locations in INDEX.md)
- Paper 13: GH shift sign inconsistency -> harmonized positive convention

### Unfixable / verification needed
- Paper 05 (Berry & Gover, J. Phys. A 22:4697 1989): plausible, unverified
- Paper 12 title: "Semiclassical Trace Formula and Scattering Resonances" vs actual "A rule for quantizing chaos?"
- Paper 13 (Berry & Balazs, J. Mod. Opt. 37:845 1990): unverified
