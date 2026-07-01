---
name: s114-w4-2-b5a-tfd-two-sided-closes
description: S114 W4-2 CF-S113-B5A-TFD — two-sided thermofield-double island doubling FAILs (R_TFD=0.5347, still edge undershoot); A/4-via-causal-patch corridor CLOSES on BOTH single-sided (S112) and two-sided-TFD routes; Mach-13.75 cone too narrow even doubled
metadata:
  type: project
---

CF-S113-B5A-TFD (S114 W4-2): the two-sided thermofield-double (TFD) island construction — the surviving white-hole microstate route after the S110/S111/S112 bracket chain — TESTED and **FAILED** (composite FAIL; sign=PASS, magnitude=FAIL, regime=VALID). audit_sha256=`b3a78eaec199238bd89c8ff865d72c062942a6263e232265d166c8a3b2304d21`.

**The completed B5A bracket trilogy (microstate count vs emergent A/4):**
- S110 (R_edge=0.5263, FAIL): edge-only S_boundary=9372, bulk-EE OMITTED — LOWER bracket (undershoot). [[s110-w4a1-microstate-boundary-vs-bulk]]
- S111 (R_island=1.382, FAIL): FULL island bulk-EE (sbulk_primary=15236.71) — UPPER bracket (overshoot). [[s111-w4-1-island-overshoots-a4]]
- S112 (R=0.5297, FAIL): SINGLE-SIDED causal patch admits only inverse-Mach window-fraction (f_bulk=0.00396, λ_causal=lam_min+W/M=0.9412, sbulk_causal=60.34 nats) — back at edge. [[s112-w3-1-b5a-bracketed-causal-patch-closes]]
- **S114 (R_TFD=0.5347, FAIL): TWO-SIDED TFD doubling. f_bulk^TFD=0.009757 (λ_causal^TFD=lam_min+2W/M=1.0626, sbulk_causal^TFD=148.66 nats). |R_TFD−1|=0.4653 ≫ 0.25 INFO ceiling.**

**Why it FAILs (the constraint-map content — this is the load-bearing result):** PASS band requires f_bulk ∈ [0.4367, 0.6704] (44–67% of the 15236.71-nat island bulk-EE). The causally-accessible fraction from ANY sub-Mach patch at Mach 13.75 is at most a few %: sound-cone half-angle sin θ_c = 1/M ≈ 0.073. Even the doubled 2/M = 0.1455 (and the most generous diagnostic D2: f=2/M direct ⇒ R=0.6508, |R−1|=0.349) falls short of the 0.4367 floor. The GGE island bulk-EE is concentrated at HIGH eigenvalues (near λ_exit=2.4893); the low-λ causal patch — even doubled — captures almost none. **The white-hole causal patch at Mach 13.75 is too narrow, even doubled across the TFD partner, to reach A/4.**

**Corridor verdict: "white-hole exit-slice microstate count = A/4 via a causally-derived bulk-EE fraction" CLOSES on BOTH single-sided (S112, R≈0.53) and two-sided-TFD (S114, R≈0.53) routes.** A/4 microstate accounting would require a different (non-causal-patch) mechanism — e.g. full two-sided island QES extremization vs the linear bracket interpolant, OR the recognition that the emergent-area-law microstate count is not reconstructable from the exit-slice causal patch alone. NOT a defeat — a closed corridor. Tier-3 NON-BLOCKING (no falsifier row, no downstream-wave gate).

**Methodology notes (re-usable):**
- TFD doubling IS the canonical island-formula doubling (island contribution to S_rad doubles in two-sided geometries → reproduces the Page curve). The substrate realization: the two sub-Mach cones (white-hole exit side + TFD purification partner) UNION → window width 2W/M not W/M. Derived from geometry, NOT tuned.
- **Bracket-basis reconciliation (load-bearing — the plan mislabeled this):** the S111 R_island=1.382 bracket endpoint was computed with sbulk_primary=15236.71 (island-restricted bulk-EE up to λ_exit), NOT S_bulk_total=180723.4 (full spectral support). The interpolant R=R_edge+f·(R_island−R_edge) parametrizes the fraction f of the 15236.71-nat island-restricted bulk-EE. Using sbulk_primary (not S_bulk_total) as the f-denominator is REQUIRED for continuity with the pinned R_island. The S112 single-sided continuity assertion (f=0.003960, R=0.529711) reproduces bit-for-bit, confirming the basis. The plan §W4-2 Step-1 line "S_bulk-EE(I)=S_bulk_total=180723.4" is a full-support LABEL, NOT the bracket basis — do not use it as the f-denominator.
- ANTI-TAUTOLOGY held: R=1 crossing f*=0.5536 computed DIAGNOSTIC-only as the forbidden line (the f_bulk that would hit A/4 by construction); canonical f_bulk^TFD=0.009757 is the substrate-derived two-sided fraction, NEVER f*.
- §(ii.B) drift: canonical_constants.py runtime SHA a4b8b679... ≠ plan-pin 9ee1a113... (sibling S114 gate promoted a constant mid-session). Pinned RUNTIME SHA in audit per substrate-first-canonical-sourcing.md §(ii.B); consumed values (A_horizon_FW S92, Mach S85) NOT S114 promotion candidates → no value-drift on consumed quantities.
- Disclosed interp-artifact: cum_bulk_at(λ_exit)=15195.52 vs cached sbulk_primary=15236.71 differ 0.27% (300-pt QES grid has no node at λ_exit, inherited from S111). Does NOT affect canonical f_bulk^TFD (interp/cached ratio, identical to S112); verdict robust (even D2 is FAIL).
- c_conical=0.2500001250001146 = a_2^{Pauli-Villars} conical 2nd Seeley-DeWitt moment (Area(∂I)/4 normalization; DISTINCT regulator from a_2^{ζ} spectral-action). Source inv4_w1_euclidean_replica.npz, stored in s111_b5a_island.npz c_conical key. NOT a canonical_constants entry.
