# S116-W3-GOLDSTONE-M2 — Goldstone-mass graph-stiffness ceiling (Landau principle)

**Gate**: S116-W3-GOLDSTONE-M2, composite **FAIL** (SIGN=PASS ∧ MAGNITUDE=FAIL ∧ REGIME=VALID). Verdict in `computations/session-116/s116_gate_verdicts.txt` (audit_sha256 2959c503...); numbers are project-level (knowledge.db / atlas) — NOT repeated here.

## Reusable Landau-domain principle (the durable takeaway)

The U(1)₇ phase Goldstone of the SU(3) Josephson tessellation cannot be massed by the spectral action (SA-mass=0 EXACT, wall #7) — so its mass is a **graph spectral moment**. Two readings of the SAME `m_G = E_disorder/ξ_disorder`:
- **Imry-Ma (disorder)** = LONG Larkin length ξ_Larkin≈17 bonds (weak random field of the soft non-C² couplings) → SMALL mass. The inv5 baseline.
- **Cheeger (connectivity)** = SHORT cell scale ξ_eff~1 bond → LARGE mass `m_G = h(L)/2 = J_C2` (h=2·J_C2/Vol, Vol=1).

The two are the long-ξ and short-ξ faces of the same pinning formula; `∂m_G/∂ξ<0` is the whole SIGN sub-test (shorter ξ ⇒ larger m_G; the connectivity reading is ~293× the Imry-Ma baseline — correct direction).

**THE WALL (stiffness ceiling)**: a graph cannot pin its own phase mode harder than its stiffest bond. The Goldstone mass is the **Cheeger bottleneck (min-cut conductance) h/2**, bounded by the largest phase-stiffness `J_C2 ≈ 2·Δ_BCS`. The Fiedler λ_1 = 4·J_C2 (C² K₄ optical mode) and the soft inter-block λ_1≈J_u1 BRACKET the spectrum; NO graph mode reaches the 170× DM-mass target (170·Δ_BCS=78.9). Coupling-scale ceiling pinches the Cheeger lower bound (h/2=J_C2) against the Step-6 upper bound (E≤J_C2,ξ≥1) → m_G=J_C2 exactly = inv5 construction-E ceiling.

**Consequence (constraint map)**: the disorder/connectivity corridor for the DM structure-formation mass is STRUCTURALLY CLOSED — frac170 ≤ J_C2/(170·Δ_BCS), ~85× short. The Leggett-DM mass is **graph-unanchored** (abundance-fixed by Leggett 0.6%-Planck, below-edge protected x_G=0.356<1, but magnitude-free on this route, like M_KK). Any DM mass is anchored OUTSIDE the graph scale.

## Convention / sourcing notes (cross-session)
- ρ_s (C² phase stiffness, 7.962) is NOT in canonical_constants — load from the SHA-pinned `s48 npz` key `rho_s_C2` (substrate-first; cross-checks inv5 npz `rho_s`). Hygiene candidate for promotion to canonical_constants with S48 provenance (surfaced to synthesis; not done unilaterally — not a NEW prediction, orchestrator canonical-write-order owns it).
- s29b npz stores only `tau3_J_matrix_frobenius=0.427` (scalar), NOT the raw J-matrix; graph weights = canonical bond inventory {4×J_C2, 3×J_su2, 1×J_u1}, consistent with block-diagonal D_K (wall #2).
- omega_G=m_G/√ρ_s, x_G=omega_G/(2Δ_BCS) reproduce inv5 br_E to all digits — the Cheeger surviving-mechanism mass and the disorder-family construction-E ceiling are the SAME point. See [[framework-constants]].
