---
name: PI-SECTOR-47 Results
description: S47 pi-phase sector classification -- B1/B2/B3 breakdown, K7 non-commutativity in higher reps, rank-based method
type: project
---

## PI-SECTOR-47 Results (2026-03-16)

**Gate**: PASS. All 13 pi-phases classified, 0 ambiguous.

**Method**: Rank-based within each PW sector. Lowest 2*dim -> B1, next 8*dim -> B2, top 6*dim -> B3. Verified on (0,0) exactly.

**Sector Distribution**:
- B1: 1 unweighted, 15 PW-weighted (11.5%)
- B2: 9 unweighted, 81 PW-weighted (61.8%)
- B3: 3 unweighted, 35 PW-weighted (26.7%)

**Key Finding**: [iK_7, D_K] = 0 holds ONLY in the (0,0) sector. In higher PW sectors, ||[I tensor iK_7, D_K]||/||D_K|| = 7.5% for (0,1). The B1/B2/B3 classification is approximate (not exact) in higher reps because eigenstates are mixtures of spinor sectors.

**Why:** The Kosmann derivative K_7 on the spinor bundle involves only the spinor part in the (0,0) sector (where the PW rep is trivial). In higher sectors, the Dirac operator entangles the PW rep and spinor spaces. The rank-based classification uses adiabatic continuity from tau=0 where B1 < B2 < B3 ordering is exact.

**How to apply:** The corrected BCS-accessible pi-phase ratio is 81/59.8 = 1.35x (B2 only) or 116/59.8 = 1.94x (B2+B3). This replaces the S46 undifferentiated 131/59.8 = 2.19x.

**Files**: `tier0-archive/s47_pi_sector.{py,npz,png}`
