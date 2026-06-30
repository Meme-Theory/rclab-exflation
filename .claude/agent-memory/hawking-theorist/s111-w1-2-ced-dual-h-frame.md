---
name: s111-w1-2-ced-dual-h-frame
description: S111 W1-2 CLOCKLOC1-CED PASS — (C,E,D)-triple closure; the DUAL-H frame trap in minisuperspace H-closure
metadata:
  type: feedback
---

S111-CF-CLOCKLOC1-CED PASS: the minisuperspace (C,E,D) triple closes self-consistently in the substrate-natural τ-frame. `|Λ−3H²|=2.91e-11<1e-6` AND (D) well-posed (`min|τ̇|_[0,0.19]=1.814398>0`, `∫dτ/τ̇=0.1005` finite). c_track=3 EXACT consumed from `inv4_w3_de_sitter_clock_tracking.npz` (NOT a canonical_constants entry).

**DUAL-H FRAME TRAP (the load-bearing methodological finding).** When integrating the (C)+(E) homogeneous-sector EOM `τ̈=−3Hτ̇−(1/5)d ln V/dτ`, there are TWO physically-distinct H's and conflating them is a 4-OOM units bug:
- **H_kinematic** = emergent-FRW rate ȧ/a ≈ O(0.26) (median of the INV4 raychaudhuri trajectory). This is the friction rate `3H≈0.79` that enters (E). The substrate is dimensionless (τ,a dimensionless; t in M_KK⁻¹).
- **H_constraint(full-V)** = √(V/(3M_P²)) ≈ 289 at the fold. The landed spectral action S_full~2.5e5 carries an overall Λ⁴a₀ magnitude that is NOT the kinematic scale. Feeding `3·H_constraint≈867` into (E) over-drives the deceleration ~4 OOM, spuriously damping τ̇→0 at τ≈0.0024 (a NUMERICAL ARTIFACT, not a physical turning point).

**Why:** My first run FAILed with `min|τ̇|=-1e-6, n_zero=4991` — looked like a turning point inside the corridor. The tell it was a bug: CLOCKLOC2, integrating the SAME EOM *in τ* in the kinematic frame, got monotone τ̇≈1.8. The cross-gate `cl2_agree` flag caught it. Fix (in-session per fix-never-defer): corridor (E)-integration uses H_kinematic (== CLOCKLOC2's `friction_k=3·H_mid`); after fix the two gates agree to 4 sig-figs (1.814398 vs 1.814473).

**How to apply:** For ANY substrate minisuperspace ODE that closes H from a constraint involving the landed V_spec (~1e5 magnitude): use the DIMENSIONLESS kinematic H for the dynamics/friction, NOT √(V/3). The de Sitter CLOSURE `Λ=3H²` is frame-INVARIANT (it's the (C) RATIO identity `V/M_P²` vs `3·V/(3M_P²)` — the V SCALE cancels), so the closure residual is identical under either H. Document the dual-H structure in the script header; disclose the frame fix in the WP §Methodology (v3-closure-recovery Class-1 boundary — frame-of-integration fix is NOT convention-shopping when honestly disclosed and the gated quantity is frame-invariant). The DIRECTIONAL [SIGN]/[CHAIN] verdict is invariant to the H normalization (sign(force)=sign(dV/dτ) regardless); only the turning-point/dynamics magnitude scale changes. Related: CLOCKLOC2 [[MEMORY]] documents the same log-gradient-vs-raw-dV/dτ normalization on the force side. Plan: `session-111-plan-w1.md §W1-2`.
