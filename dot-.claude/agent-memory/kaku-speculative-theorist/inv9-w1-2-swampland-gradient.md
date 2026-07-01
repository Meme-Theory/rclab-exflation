---
name: inv9-w1-2-swampland-gradient
description: INV9-W1-2 swampland dS gradient bound — FAIL on JOINT; the substrate's "no minimum / forced rolling" is REAL but DISTINCT from swampland-steep; survey k=3586.5 drift corrected
metadata:
  type: project
---

INV9-W1-2-SWAMPLAND-GRADIENT-BOUND (investigation-9, kaku-origin CF14/B-2). [SIGN] gate. Verdict **FAIL** (sign=FAIL, magnitude=FAIL, regime=VALID); audit_sha256 `9ca9b4743222099a6cc859a99f61f0ac754ca42830160b08f7f76e10cbbf1887`.

**The cross-domain bridge (swampland dS conjecture ↔ substrate gradients) BROKE on one of two legs — informatively.**
- **Leg A — S(τ) [PASS, cross-check]**: reproduced the PROVEN S69 W4-B dressed `g_S=3.52` (cutoff) / `~6.6` (zeta) > c~O(1). Bare ratio `|dS/dτ|/S_fold = 58672.80/250360.68 = 0.2343` is NOT swampland-relevant (must use the field-space-metric-dressed value; do NOT cite 0.2343 as the swampland ratio).
- **Leg B — V(φ) dilaton potential [FAIL, FRESH]**: the s66 Weyl-anomaly dilaton `V(φ)=(1/8)(e^{4φ}−1)a₀+(1/2)(e^{2φ}−1)a₂R+φa₄` has Sage-EXACT asymptotics `g_V(φ→+∞)=4` [cutoff catastrophe, AVOIDED] and `g_V(φ→−∞)=0` (`~1/|φ|`) [zeta runaway, the ATTRACTOR]. The dS gradient bound `|∇V|/V≥c` FAILS exactly where the dilaton rolls to. `V''>0` convex ⇒ refined-dS curvature disjunct also fails.

**Durable structural distinction (the result's real content)**: "forced rolling" (no minimum, `has_minimum=False`, A4=roll) and "swampland gradient bound" (steep enough, `|∇V|/V≥c`) are DISTINCT conditions. The substrate satisfies the first (the dilaton rolls, driven by the linear a₄ survivor of the zeta regime) but FAILS the second on the V(φ) axis (the runaway is asymptotically LINEAR, too shallow). So the "swampland mandates the framework's no-minimum structure" reading (Track A) is REFUTED on the dilaton axis; A4 still resolves to ROLL but NOT for the swampland's reason. Inter-axis tension (Track B): S(τ) is swampland-steep, V(φ) is not.

**Survey-drift correction (retire this conflation)**: the kaku-survey "k=+3586.5 M_KK" is NOT a V'(q) gradient — it is the S62 q-theory ZERO-POINT-ENERGY curvature `d²E_ZP/dq²|₀ = −3586.531181` (s62_cc_qtheory_gge), a 2nd derivative of a DIFFERENT potential. The s66 dilaton gradient at the operating point is `V'(0)=43210.72` (12× drift, wrong differential order). Any downstream cite of 3586.5 as a dilaton gradient inherits both errors.

**Three distinct substrate potentials in the lore — keep them separate**: (1) s66 dilaton V(φ) [Weyl-anomaly, V(0)=0 node, runaway]; (2) s62 q-theory E_ZP(q) [d²E_ZP/dq²|₀<0 local max, the "speed bump", source of 3586.5]; (3) s53 V_eff=V_KK+E_cond [local MAX at τ=0.2015]. ALL three share "no metastable minimum" — that convergence is real, but the swampland gradient bound is satisfied by NONE on its rolling branch.

CF14 does NOT close swampland-consistent; it resolves to an axis-dependent classification. No falsifiable quintessence-w(z) falsifier-row warranted (V-leg fails the forcing argument). Links: [[s80-w1-3-fold-inst-gradient]] (dS_inst/dτ monotone — a different gradient observable). Per phononic-framing: the substrate IS the potential; the picture is a cliff that becomes a gentle ramp toward the attractor.
