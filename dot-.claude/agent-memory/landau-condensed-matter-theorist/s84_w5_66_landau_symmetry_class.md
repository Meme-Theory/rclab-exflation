---
name: S84 W5-66 Landau Symmetry Class of K-Corridor — INFO
description: G/H decomposition of K-corridor: SU(3)xSO(3)xU(1)_relxT → SU(2)xU(1)xSO(2)xZ_2xT; N_OP=8 overshoots 3He-B N=5 by 3 (SU(3)/(SU(2)xU(1)) = CP^2 framework-unique); AZ class BDI hybrid (vs 3He-B canonical DIII); corridor multi-valued across K_crit=91.5; BDI certification valid only on inflationary sub-corridor K ≤ 91.5.
type: project
---

# S84 W5-66 GATE-LANDAU-SYMMETRY-CLASS — INFO

**Verdict line**: `W5-66: INFO -- value=(G:SU(3)xSO(3)xU(1)_relxT|H:SU(2)xU(1)xSO(2)xZ_2xT|N_OP=8|class=BDI) scheme=Landau-Ginzburg convention=Volovik-2003-Ch7 L_max=N/A sha256=519c8c03f1bf97ede9d47fe1e20bf72c93e024e7feed15c7b4cff20bb21d8ecc`

## Numbers (pre-registered gate)
- G_framework = SU(3) × SO(3) × U(1)_rel × T, dim = 12
- H_framework = SU(2) × U(1) × SO(2) × Z_2 × T, dim = 5
- dim(G/H)_framework = N_OP = **8**
  - SU(3)/(SU(2)×U(1)) = CP² (4 dim, framework-unique)
  - SO(3)/SO(2) = S² (2 dim)
  - U(1)_rel/Z_2 (1 dim)
  - K-dilation axis (1 dim)
- N_OP_3HeB = **5** (Volovik 2003 Ch. 7: SO(3)_L × SO(3)_S × U(1)_φ / SO(3)_{L+S} = 4 coset + 1 gap modulus)
- AZ class framework = BDI (T² = +1, C² = +1, S present); forced by `[iK_7, D_K] = 0` and μ = 0 PH symmetry
- AZ class 3He-B canonical = DIII (T² = −1)
- K_crit = K_anchor/ε_anchor = 2.035/0.02223 = 91.543 (W5-55 pole where ε_eff = 1)
- K_* framework = coth(1) = 1.3130; K_* lab 3He-B = coth(0.98) = 1.3279; ratio 1.13% (W5-58 PASS)

## Why INFO (not PASS, not FAIL)
- **NOT FAIL**: G/H decomposition is clean and unambiguous. Each factor traces to a specific framework feature (SU(3) from D_K internal space, SO(3) from fiber occupation, U(1)_rel from Leggett-band phase, T from BDI). No structural ill-definition.
- **NOT PASS**: Per plan threshold PASS requires N_OP match (= 5) AND AZ class match (= BDI in 3He-B textbook sense). Both fail:
  - N_framework = 8 ≠ 5 = N_3HeB. Over-inherits by 3 directions (CP² from SU(3) gauge, no 3He-B analog).
  - AZ class 3He-B textbook is DIII (T² = −1), not BDI. Framework's BDI holds structurally (via PH-forced μ = 0) but matches a BDI-TCI submanifold of 3He-B, not its bulk AZ.
- **INFO threshold met**: plan specifies "G/H identified but N mismatch (e.g., N=4 or N=6 instead of 5) — inheritance partial". N=8 mismatch is larger but the verdict structure applies.

## Structural harvest
- Framework inherits 3He-B topology + SU(3) Casimir algebra (framework-unique) + 0D discreteness (framework-unique). S79 P3-A "inheritance-hybrid" reading confirmed at symmetry-group level.
- 3 extra continuous broken directions = CP² = SU(3)/(SU(2) × U(1)) — these are the framework's internal SU(3) gauge structure, absent in 3He-B's SO(3)_L orbital sector.
- BDI certification valid ONLY on inflationary sub-corridor K ∈ (1, 91.5] (W5-55 pole at K_crit = 91.5 removes 3 of 6 pre-registered K samples from 1D Landau manifold).
- K is regulator-dependent (W5-54 FAIL: Zubarev 32.40 vs zeta 0.6366 at R5, span 10^1.71). OP magnitude is scheme-dependent; coset STRUCTURE is scheme-invariant.

## Does NOT trigger
- Plan §Decision Point item 5 (Gate 66 FAIL → framework-level 3He-B inheritance re-audit). INFO verdict means 3He-B inheritance is preserved at the parent-child level, restricted to BDI submanifold and valid at K_* = 1.3130.

## W6 carry-forward
- Landau-Ginzburg functional F[φ] on 8-dim coset, restricted to K ∈ (1, 91.5]; verify that the 3 SU(3)-internal broken directions do NOT generate new Goldstone modes beyond block-diagonal theorem S22b.
- Scheme-invariant OP coordinate search (K-functional invariant under regulator change).
- Agent memory updated (this file).

## File pointers
- Script: `computations/s84_w5_landau_symmetry_class.py`
- Data: `computations/s84_w5_66_data.npz`
- Plot: `computations/s84_w5_66_plot.png`
- Working paper: `sessions/archive/session-84/session-84-w5-workingpaper.md` §W5-66

**Why**: Gate 66 pre-registered whether the K-corridor admits a Landau 1-parameter OP classification matching 3He-B's BDI universality class with N=5 order-parameter components. The G/H decomposition is clean but N mismatches (8 vs 5) and AZ class is HYBRID (framework BDI via PH μ=0 vs 3He-B textbook DIII); corridor is multi-valued across W5-55's K_crit=91.5 pole.
**How to apply**: When questions of 3He-B inheritance arise at the symmetry-group level, cite this gate — inheritance is PARTIAL (dimensional over-inheritance + hybrid AZ), valid at K_* pivot (W5-58) and on inflationary sub-corridor only. Use Z_2 gauge theorem (S82 W2-11) as structural input to justify the U(1)_rel → Z_2 entry in H_framework.
