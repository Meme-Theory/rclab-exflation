---
name: inv9-w1-1-modular-flavor-fail
description: INV9-W1-1 FAIL — bottom-N D_K(τ) gen matrix elements are τ-INVARIANT (not a Dedekind-η modular form); extends the §VII.BL homogeneity wall from τ_fold to the full moduli window [0.15,0.25]
metadata:
  type: project
---

INV9-W1-1-MODULAR-FLAVOR-FORM (investigation-9, kaku NS-1 = string NS-1 flagship) FAILed.

**The compute**: Y_i(τ) = ⟨ψ_i(τ)|D_K(τ)|ψ_i(τ)⟩ = lowest |λ| of the three generation Peter-Weyl sectors (1,0)/(1,1)/(3,0) [C₂=(4/3,3,6)], built fresh on τ-grid [0.15,0.25] (Δτ=0.005) via `dirac_spectrum.collect_spectrum_with_eigenvectors` (max_pq_sum=3). Tested the Dedekind-η-power ansatz Y_i = A·η(ε)^{w_i} with w_i=C₂_i for three ε-maps (linear/jensen/nome).

**Result (numbers)**: Y(1,0)=0.8359, Y(1,1)=0.8730, Y(3,0)=1.2483 at τ_fold. R_direct = Y(3,0)/Y(1,0) = **1.4933** (NOT 9.86 rank-1, NOT 1e5 physical). Best-map min_R²=**0.258** ≪ 0.95; fitted weights ≈ 0 (NOT the Casimir tower); grading_dev=1.437. Diagonal-element x-check = 6.22e-15 (machine-precision; the diag element IS the ground-state eigenvalue). Verdict FAIL (sign=PASS, mag=FAIL, regime=VALID).

**Why (the structural reason — this is the durable finding)**: the Y_i are nearly **τ-INVARIANT** (Y(1,0): +1.1%, Y(3,0): −2.5% across the whole ±26% window). This is FORCED by [[s99-generation-blindness-theorem]] (§VII.BL, STAGE-3-PERMANENT, I co-authored Stage-0): the Jensen TT-deformation τ is a U(2)-isometric, volume-preserving, **left-invariant** metric deformation. A left-invariant D_K(τ) is multiplicity-scalar at EVERY τ (homogeneity wall W2), so the τ-deformation preserves the multiplicity-scalar structure for ALL τ — it acts on the C² off-diagonal metric block, NOT on the Peter-Weyl multiplicity index. A modular flavor form would need τ-dependence BREAKING left-invariance on the generation space, which Jensen structurally cannot supply.

**What this extends**: §VII.BL was proven AT the fold. INV9-W1-1 extends it to the full moduli window — the rank-1 Yukawa wall is a left-invariance feature for ALL τ in [0.15,0.25], not just τ_fold. The modular-flavor (Dedekind-η) route to the Yukawa hierarchy is CLOSED on the substrate; the surviving mechanism is the external non-LI fibre connection ε_LX (inv-5 W1-3/W1-4), NOT a τ-modulus.

**Canonical constants surfaced (now in canonical_constants.py SECTION E with PROVENANCE)**: `R_S96_matter_hierarchy = 9.86183067373777` (the rank-1 wall anchor, was verdict-file+graph only); `C2_gen_sectors = [4/3, 3, 6]` (SU(3) Casimir for the gen sectors, S61 W8).

**Verdict SHA** (investigation-track): audit_sha256=c63cc11549c86f7a5ef6fd154a5e3966e260eb7d12cad88d2b3e2c97c629860b.
