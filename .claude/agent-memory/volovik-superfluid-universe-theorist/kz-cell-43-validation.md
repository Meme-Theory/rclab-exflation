---
name: KZ-CELL-43 Validation
description: S43 W6-21 KZ-CELL-43 validation result. Infinite-plane approximation artifact identified. Tessellation channel CLOSED (robust). N=32 reliable, N>=128 upper bounds only. Scaling +0.265 is artifact not physics.
type: project
---

S43 W6-21 KZ-CELL-43 validation completed 2026-03-14.

Verdict: METHODOLOGY FLAWED (but conclusions survive and are strengthened).

Key findings:
1. L_max increases with N_cell because infinite-plane approximation prevents face intersections from shrinking as cells get smaller. For N>=240, R_cell < D_SHELL but r_circ still ~ D_SHELL.
2. BFS clustering of overlapping infinite-plane circles drives percolation. At N=1000, median L_max = 75% of shell circumference.
3. Measured scaling L_max ~ N^{+0.265} is an ARTIFACT, not a physical property of Voronoi tessellations.
4. N=32 result (median L_max = 4619 Mpc, 5x Giant Arc) is in the RELIABLE regime (R_cell(32) = 4488 > D_SHELL = 2350).
5. S42-S43 cross-check at N=32: 0.6% statistical difference. Consistent.
6. Tessellation channel CLOSED at all N. The model produces percolating boundary networks, not isolated ~1000 Mpc filaments.
7. Superfluid perspective: correct analog is vortex lines (1D), not Voronoi walls (2D). KZ defect scale = xi_KZ, not N_modes.

**Why:** Validates framework's treatment of large-scale structure channels.
**How to apply:** Tessellation-to-giant-structure mapping is permanently closed. Future LSS work should focus on KZ defect networks or effacement-based observables (ALPHA-ENV-43).
