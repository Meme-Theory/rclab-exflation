---
name: s116-stateproj-track-b-no-a-sector
description: S116 W7 §VII.AJ.STATE-PROJ INFO (Track B) — the 3He A/B gap-square asymmetry is NOT substrate-first predictable; the substrate is a single 3He-B child with no intrinsic 3He-A sector. Inheritance scope-boundary + naming-vs-provenance trap.
metadata:
  type: project
---

S116 W7-1 (`S116-W7-STATEPROJ-BCS`, INFO/Track-B, audit_sha256 `0968093b…07c0a`). The STATE-PROJ companion to §VII.AJ: substrate-IS state-pair functional `R_STATE = (a−b)/(a+b)` with `a=ρ_BCS(P_A·H_pair)=½N(0)Δ_A²`, `b=½N(0)Δ_B²` reduces at A-B coexistence to `(Δ_A²−Δ_B²)/(Δ_A²+Δ_B²) = (SC_A²−SC_B²)/(SC_A²+SC_B²) = +0.0353559`, reproducing lab `R_3HeB_lit` to `rel=0.0` (bit-identical).

**Why INFO not PASS — the determination only I am positioned to make.** The controlling ratio `Δ_B/Δ_A = SC_corr_B/SC_corr_A = 1.111/1.151 = 0.96525` is LABORATORY-IN (Serene-Rainer 1983 / Greywall 1986), NOT substrate-first. The reproduction is a TAUTOLOGY (both sides are the same lab numbers; the S87 "lab gaps" `Delta_A_at_pc=2.0302224` ARE exactly `SC_A·πe^−γ`). **Track A is structurally UNAVAILABLE** because:
1. Substrate is a SINGLE BDI object (3He-B child, N_3=0); 3He-A is DIII (N_3=2). **No intrinsic A-sector ⇒ no substrate-first Δ_A.** The "A-sector central projection P_A" is a formal A_K projection, not a second physical superfluid phase the substrate selects.
2. SC corrections are 3He MATERIAL feedback (Landau params F_0^a, F_1^s); `Delta_BCS=0.4642547` is a SINGLE gap, does not split into an A/B pair with 3He feedback.
3. Volovik q-theory governs the vacuum 4-form `q` / equilibrium CC (DILUTION-CC) — NOT superfluid gap-anisotropy strong-coupling.

**SCOPE-BOUNDARY (reusable)**: any observable requiring a 3He-A gap (A/B coexistence, polycritical asymmetries) is NOT substrate-first predictable — the inheritance morphism ι gives a 3He-B child only. Such observables can be lab-fed (Track B) but not predicted until the no-A-sector obstruction is resolved. See [[project_3heb-inheritance]] (BDI/N_3=0/χ is the inheritance content; 3He-A is NOT inherited).

**Naming-vs-provenance trap**: `delta_B_over_delta_A_q_theory = 0.96528` is NAMED "q_theory" but its STRUCTURE is `(= 1.9597/2.0302)` = the lab reduced-gap ratio; S88 W4c's "three extraction methods" (Greywall/Halperin-Hammel/Volovik-q-theory) are three LAB extractions of the SAME 3He gap. NAME ≠ PROVENANCE (Observable-Naming-History vs Parse-Tree-Structure). Always read the parenthetical structure, never the suffix.

**What IS substrate-first (the honest claim)**: the FORM. STATE-PROJ is a genuine algebra-DEPENDENT BdG-occupation state-pair functional — confirmed on 78,080 cached substrate modes (p+q≤10): `R_BdG=+0.0688 > 0` same sign (magnitude diff = finite-DOS-curvature, substrate gap not in weak-gap limit). Sign-flip vs OP-PROJ (`R_∞≈−1.892<0`, spectrum-only count) is structural input to the W7-2 orthogonality workshop (different sign + different algebra-axis corner ⇒ orthogonal companions, not collapse). Slot RESERVED `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`; carry-forward CF-S117-STATEPROJ-SC-FROM-SUBSTRATE (substrate q-theory SC ratio; blocked by no-A-sector obstruction).

7 lab anchors added to canonical_constants.py SECTION E (S116) with LABORATORY-IN provenance: SC_corr_A/B, delta_A/B_over_kBTc, P_pc, T_pc, R_3HeB_lit. Always cross-check `get_constant` before citing — they are lab, NOT substrate.
