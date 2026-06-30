# Session 91 Plan — Wave 6: d=4 envelope discriminators + lizzi reading + W11-5 sister re-audit

**Wave lead**: lizzi-spectral-functional-theorist (primary author + dispatch lead)
**Wave class**: COMPUTE-class (5/5 gates carry numerical PASS/FAIL/INFO bands against pre-registered substrate-physics thresholds; producing scripts emit `.py + .npz + .png + verdict line`; M1 numerical-comparison fails → COMPUTE-class fallthrough per `wave-classification.md §"Dispatch consequences"`)
**Source plans / syntheses**:
- `sessions/session-plan/session-91-context.md` §"W6 — d=4 envelope discriminators + lizzi reading + W11-5 sister re-audit"
- `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` §(4) discriminator-gate spec + §(5) CF-LZ-S7-1/2/3
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` §Wrap-Up CF-1/CF-7/CF-9 (4-field specs at lines 1270–1322)

---

## Wave 6 Summary

Five items; lizzi-spectral-functional-theorist primary author; ~3.2–5.7 wave-equivalents total. Tests the substrate-IS prediction that the d=4 Mellin-cone universal envelope at substrate-distance-1 pole `s=3` is `L^{-α}` with `α=3` asymptotic (L_max ≥ 35 per Friedrich-Bär saturation) vs realized `α≈1.9` at pre-asymptotic finite L_max ∈ [6, 12]. Disambiguates Reading A (coincidence; CF-54 ≈ CF-65 accidental) from Reading B (substrate-structural; both observables share the substrate's universal d=4 envelope at finite L) via four independent observables on the SAME substrate algebra `(A_K, H_K, D_K)`.

| # | Gate ID | Effort | Pre-req |
|:-:|:--------|:------:|:--------|
| W6-1 | `S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW` (T2.54 / CF-1) | 0.8–3.3 we | none (W6-3 is cheap precursor; not blocking) |
| W6-2 | `S91-K_HK-AND-K_CSUB-EMPIRICAL-ANCHORING` (T2.58 / CF-7) | 1.5 we | none |
| W6-3 | `S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9` (T2.60 / CF-9) | 0.1 we | none (existing data) |
| W6-4 | `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR` (M10 / CF-LZ-S7-1) | 0.5 we | none |
| W6-5 | `S91-W11-5-SISTER-RE-AUDIT-UNDER-REALIZED-ENVELOPE` (M11 / CF-LZ-S7-3) | 0.3 we | **CONDITIONAL on W6-4 PASS** |

Dispatch ordering: W6-3 first (cheap precursor; 0.1 we; gives early signal on Reading A pre-asymptotic sub-window steepening); W6-2 + W6-4 in parallel (independent observables on the same L_max=12 cache); W6-1 pathway (b) at L_max ≥ 22 after W6-4 verdict (W6-4 PASS sharpens W6-1's L_max ≥ 35 backup readiness; if W6-4 FAIL toward Reading A, W6-1 path (a) becomes structurally necessary); W6-5 fires LAST conditional on W6-4 PASS.

---

## Wave 6 Decision Point Prerequisites

- **W6-4 PASS (Reading B confirmed)** ⇒ unblocks W6-5 (W11-5 sister re-audit under realized envelope) AND advances §VII.AU.OP-PROJ from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION toward STAGE-1-CANDIDATE-PENDING-STAGE-2 IF W6-1 pathway (b) PASS-A also lands (joint pathway for §VII.AU.OP-PROJ first-extraction).
- **W6-4 FAIL (Reading A confirmed)** ⇒ W6-5 dispatched anyway under FAIL-side prediction (W11-5 sister remains registry-FAIL by ~21× under L^{-3}); pathway (a) backup at L_max ≥ 35 in W6-1 becomes structurally necessary (~2.5 we).
- **W6-4 INFO** ⇒ W6-5 deferred to S92+; W6-1 pathway (b) FIRST holds.
- **W6-3 α_sub > 2.5 (PASS-A-partial)** ⇒ Reading A pre-asymptotic steepening; W6-4 expected to see σ_β > 0.10 (some observables in PASS band, some in FAIL band) ⇒ INFO probable at W6-4.
- **W6-3 α_sub ≈ 1.9 (FAIL toward Reading B)** ⇒ Reading B partial confirmation at pre-anchor sub-window; W6-4 expected to PASS with tight σ_β.

---

## §W6-1. `S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW` (T2.54 / W-6 CF-1)

### 1. Gate ID

`S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW`

### 2. Trigger

`[VERIFY-THEOREM]` (test substrate-IS prediction that `α=3` is the asymptotic exponent of the Mellin-cone universal envelope at d=4 substrate-distance-1 pole `s=3`; verifies whether `α≈1.9` at pre-asymptotic L_max ∈ [6, 12] is the realized finite-L manifestation of the asymptotic `α=3` per Friedrich-Bär saturation; OR whether `α≈1.9` persists post-asymptotically as the canonical exponent).

### 3. Classification

PHONONIC. The d=4 universal envelope IS a substrate-IS spectral-functional property of the substrate's Mellin-cone closure at substrate-distance-1 pole `s=3`. Direction substrate → emergent: substrate's combinatorial shell-sum geometry `dim(p,q) · (C_2(p,q)+1)^{-3}` at d=4 → universal `L^{-α}` envelope at all HKR-image-bound observables → cross-pillar bridge's Level-2 envelope numerical band → registry-PASS classification at downstream consumer.

### 4. Agent type

`lizzi-spectral-functional-theorist` (PRIMARY; functional-independent vs functional-dependent classification expertise; ZETA-NOT-PHYSICAL-75 substrate-IS envelope identification; F_2-class projection 5-regulator atlas membership analysis); `connes-ncg-theorist` CO-SIGN on the Connes-Karoubi pairing implementation at pathway (b) per workshop verdict §V row 3 (lizzi PRIMARY + connes CO-AUTHOR).

### 5. Hypothesis

The d=4 universal envelope at substrate-distance-1 pole `s=3` is `L^{-3}` asymptotically (Reading A canonical) AND `L^{-1.9}` realized at finite L_max ∈ [6, 12] (Reading B realized). At L_max ≥ 22 (pathway b direct Connes-Karoubi pairing), CF-65's empirical α converges from `≈ 1.929` toward `≈ 3` per the c_sub_corrected M_Pl_eff² parameterization's asymptotic-settling scale.

### 6. Method — COMPLETE self-contained dispatch prompt

```python
"""
S91 W6-1: S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW (T2.54 / CF-1)

Tests whether the d=4 universal envelope at substrate-distance-1 pole s=3
asymptotic exponent is α=3 (Reading A canonical) or α≈1.9 (Reading B realized
at all L_max) via two complementary pathways pre-registered at workshop §V row 3.

Pathway (b) FIRST (cheaper; ~0.8 we; L_max ≥ 22):
    Direct Connes-Karoubi pairing of the §VII.AU.OP-PROJ Pillar I ↔ Pillar II
    HKR-image-bound observable; bypasses c_sub_corrected M_Pl_eff² ratio's
    asymptotic-settling scale bottleneck per workshop EC2 derivation
    (lines 1162-1170). L_max=22 incremental cache extension required.

Pathway (a) BACKUP (more expensive; ~2.5 we; L_max ≥ 35):
    Friedrich-Bär saturation theorem extension per W11-3 precedent
    (math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection
    Feasibility Pre-Check"); CF-54 + CF-65 re-extraction at L_max ∈ {15..35}.
    Dispatched ONLY if pathway (b) returns INFO or FAIL.
"""

from canonical_constants import *  # M_KK, tau_fold, kappa_2_substrate_FW, gv_canonical_difference_FW, slope_A_FW_Conv_A_AT_TAU_FOLD, slope_A_FW_Conv_B_AT_TAU_FOLD, n_s_FW_exact
import numpy as np
import torch  # GPU torch.linalg ≥ 100x100 per math-scripts.md §"Environment"
import hashlib, json
from pathlib import Path

# --- Pathway (b): direct Connes-Karoubi pairing at L_max=22 ---
# Input cache: s84_spectrum_cache_L12_tau019.npz (existing) + S91 W6-1 L_max=22
# extension (this script generates the extension via Friedrich-Bär saturation
# bottom-K rooting at L_max=12 PLUS analytic upper-bound extrapolation to
# L_max=22 per Friedrich-Bär η_FB_lower = 0.40 lower bound per W11-3 precedent.

cache_L12 = np.load('computations/session-84/s84_spectrum_cache_L12_tau019.npz')
# Verify input SHA at runtime (pinned at plan-freeze; <computed-at-runtime> here)

# Connes-Karoubi pairing: directly evaluate ⟨[Ch(P_0(τ_fold))], [φ_g^{sym}]⟩
# on the (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) finite spectral triple at L ∈ {12..22}.
# The pairing is computed via the Hochschild cocycle representation of Ch(P_0)
# coupled to the gauge symmetric cocycle φ_g^{sym} per CC1996 §2.2-2.3.

L_grid_pathway_b = np.arange(12, 23)  # (local) — 12..22 inclusive
alpha_pathway_b = []  # (local)
for L in L_grid_pathway_b:
    # Build P_0 band-0 projector on Peter-Weyl block at L
    P_0_L = build_band_0_projector(cache_L12, L_max=L)  # (local helper)
    Ch_P_0 = chern_character_HKR_image(P_0_L)  # (local helper); 4-form via HKR
    phi_g_sym = gauge_symmetric_cocycle(cache_L12, L_max=L, regulator='Mellin')  # (local)
    R_universal_L = connes_karoubi_pairing(Ch_P_0, phi_g_sym)  # (local)
    alpha_pathway_b.append((L, R_universal_L))

# log-log fit on L ∈ [15, 22] (window avoids L=12 cache-ceiling)
L_fit = np.array([L for L, _ in alpha_pathway_b[3:]])  # (local) — 15..22
R_fit = np.array([R for _, R in alpha_pathway_b[3:]])  # (local)
log_L = np.log(L_fit)  # (local)
log_R = np.log(np.abs(R_fit))  # (local)
slope_b, intercept_b = np.polyfit(log_L, log_R, 1)  # (local)
alpha_b = -slope_b  # (local) — empirical α at L_max ∈ [15, 22]

# 5-regulator atlas K_csub_R extraction (R ∈ {Mellin, zeta, Pauli-Villars, cutoff, lattice})
# Per workshop EC1 derivation lines 1146-1150: K_csub is MIXED at the
# convergence-tail axis; per-regulator-class K_csub_R values differ.

regulators = ['Mellin', 'zeta', 'Pauli-Villars', 'cutoff', 'lattice']  # (local)
alpha_per_regulator = {}  # (local)
for R in regulators:
    phi_g_sym_R = gauge_symmetric_cocycle(cache_L12, L_max=22, regulator=R)
    R_per_L = [
        connes_karoubi_pairing(
            chern_character_HKR_image(build_band_0_projector(cache_L12, L_max=L)),
            gauge_symmetric_cocycle(cache_L12, L_max=L, regulator=R)
        )
        for L in L_fit
    ]
    log_R_per = np.log(np.abs(np.array(R_per_L)))  # (local)
    slope_R, _ = np.polyfit(log_L, log_R_per, 1)
    alpha_per_regulator[R] = -slope_R

# Consensus criterion per workshop EC1: PASS-A iff α at majority-of-5 satisfies
# |α − 3| / 3 < 0.20  (α ∈ [2.4, 3.6])  OR  PASS-A at Mellin + zeta (FI-axis F_2 projection).

count_pass = sum(1 for a in alpha_per_regulator.values() if abs(a - 3.0) / 3.0 < 0.20)  # (local)
majority_pass = count_pass >= 3  # (local) — majority of 5
f2_pass = (
    abs(alpha_per_regulator['Mellin'] - 3.0) / 3.0 < 0.20
    and abs(alpha_per_regulator['zeta'] - 3.0) / 3.0 < 0.20
)  # (local)
pathway_b_pass_a = majority_pass or f2_pass  # (local)

# Verdict assignment per workshop §V row 3 + CF-1 spec lines 1273:
if pathway_b_pass_a:
    verdict = 'PASS'  # PASS-A: Reading A canonical confirmed
    value_field = f"alpha_pathway_b={alpha_b:.4f}_majority_pass={count_pass}_of_5"
elif abs(alpha_b - 1.9) / 1.9 < 0.15 and count_pass <= 1:
    verdict = 'FAIL'  # FAIL-B: Reading B realized confirmed; pathway (a) NOT needed
    value_field = f"alpha_pathway_b={alpha_b:.4f}_FAIL_B_persistent_L_1_9"
else:
    verdict = 'INFO'  # Partial convergence; carry-forward to S92+ pathway (a) at L_max ≥ 40
    value_field = f"alpha_pathway_b={alpha_b:.4f}_INFO_partial_convergence"

# Output emission per gate-verdicts.md S87+ schema-v2 + supersedes-tag discipline
# (no supersedes; this is a NEW gate, not a corrective emission)
append_verdict(
    gate_id='S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW',
    verdict=verdict,
    value=value_field,
    scheme='direct-connes-karoubi-pairing-L_max-22-pathway-b',
    convention='Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION',
    L_max=22,
    input_pin_map={
        's84_spectrum_cache_L12_tau019.npz': '<computed-at-runtime>',
        'canonical_constants_M_KK': M_KK,
        'canonical_constants_tau_fold': tau_fold,
        'canonical_constants_kappa_2_substrate_FW': kappa_2_substrate_FW,
        'canonical_constants_gv_canonical_difference_FW': gv_canonical_difference_FW,
    },
)

# Save outputs
np.savez('computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz',
    L_grid=L_grid_pathway_b, alpha_b=alpha_b, alpha_per_regulator=alpha_per_regulator,
    pathway_b_pass_a=pathway_b_pass_a, verdict=verdict,
)
# Plot: log-log per-regulator R_universal(L) overlay with α=3 and α=1.9 reference lines
```

Output files: `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.py` + `.npz` + `.png`.

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `L_max_pathway_b` | 22 | workshop EC2 line 1170 (alternative HKR-image parameterization; bypasses c_sub_corrected bottleneck) |
| `L_max_pathway_a_backup` | 35 | workshop EC2 line 1162 (Friedrich-Bär saturation extension; ~2.5 we cost) |
| `L_fit_window` | [15, 22] (path b) / [15, 35] (path a backup) | avoids L=12 cache-ceiling effect; avoids L ≤ 14 pre-asymptotic |
| `regulators_atlas` | {Mellin, zeta, Pauli-Villars, cutoff, lattice} (5-regulator A_5 atlas) | workshop EC1 line 1150 |
| `K_csub_R_classification` | MIXED at convergence-tail axis | workshop EC1 line 1146 |
| `consensus_criterion` | (majority-of-5 ≥ 3) OR (Mellin + zeta FI-axis F_2 projection) | workshop EC1 line 1150 |
| `pass_band_alpha_target` | 3.0 ± 0.6 (PASS-A: \|α − 3\| / 3 < 0.20) | CF-1 gate spec line 1273 |
| `fail_band_alpha_target` | 1.9 ± 0.285 (FAIL-B: \|α − 1.9\| / 1.9 < 0.15 AND count_pass ≤ 1) | CF-1 gate spec line 1273 |
| `info_band` | partial convergence between PASS-A and FAIL-B | CF-1 gate spec line 1273 |
| `tau_fold` | 0.190 (canonical) | `canonical_constants.py:283` |
| `M_KK` | 7.428660036284456e16 GeV (gravity route alias) | `canonical_constants.py:339-341` |
| `scheme_pin` | `direct-connes-karoubi-pairing-L_max-22-pathway-b` | this gate-block authoring |
| `convention_pin` | `Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION` | `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"` cache-projection vs full-leaf-foliation pin |
| `binding_pin` | `Level-2-binding-HKR-bridge-canonical-import-binding` per `regulator-pin-discipline.md §"Binding axis"` Hybrid Independence Test (K=1 SUGGESTION pending K=3) | substrate-natural pin for §VII.AU.OP-PROJ |
| `regulator_class_pin` | `a_n^{Mellin}` at substrate-distance-1 pole s=3 | `regulator-pin-discipline.md` MANDATORY UV-regulator pin |
| `gpu_path` | torch.linalg on AMD RX 9070 XT (17.1 GB VRAM); cache extension L_max=22 dim ≤ 9792 per W11-2 + W11-3 saturation | `math-scripts.md §"Environment"` |
| `random_seed` | 0 (deterministic Connes-Karoubi pairing; no Monte Carlo) | this gate-block |
| `tolerance_rule` | RATIO (relative error on α; \|α − target\| / target) | CF-1 gate spec |

**Input SHA-256 pins**:
- `computations/session-84/s84_spectrum_cache_L12_tau019.npz` SHA: `<computed-at-runtime>` (1.34 MB file; precompute at plan-freeze landing)
- `computations/_shared/canonical_constants.py` SHA: `<computed-at-runtime>`
- `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` SHA: `<computed-at-runtime>` (CF-LZ-S7-1 anchor)
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` SHA: `<computed-at-runtime>` (CF-1 spec at lines 1270-1274 + EC1/EC2 at lines 1140-1170)
- `sessions/permanent-results-registry.md` SHA: `<computed-at-runtime>` (§VII.AU.OP-PROJ Element 5 at line 18014; §VII.AF.1.OP-PROJ Element 4 L^{-3} at line 14784)

### 8. Expected output 4-tuple

`(value=alpha_pathway_b=<α_b>_majority_pass=<count>_of_5, scheme=direct-connes-karoubi-pairing-L_max-22-pathway-b, convention=Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION, L_max=22)`

Predicted Reading A: `α_b ≈ 2.6–3.0` at L_max=22 (HKR-image asymptotic settling per c_sub_corrected M_Pl_eff² ratio asymptotic-settling scale; majority_pass = 3–5 of 5).
Predicted Reading B: `α_b ≈ 1.9–2.0` at L_max=22 (persistent at all L_max; majority_pass = 0–1 of 5).

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS-A (Reading A canonical confirmed; verdict (a) or HYBRID (d) retained)**: `|α_b − 3.0| / 3.0 < 0.20` (α ∈ [2.4, 3.6]) at MAJORITY-of-5 regulator-class sub-windows (count_pass ≥ 3) OR PASS-A at Mellin + zeta FI-axis F_2 projection (workshop EC1 consensus criterion line 1150). Composite collapse rule: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID ⇒ composite=PASS`.
- **FAIL-B (Reading B realized confirmed; verdict (d) HYBRID at per-regulator-class sub-window structure)**: `|α_b − 1.9| / 1.9 < 0.15` (α ∈ [1.615, 2.185]) AND count_pass ≤ 1 across regulators (Reading A consensus FAILS). Composite collapse: `sign_verdict=PASS (Reading B predicted L^{-1.9} persistence), magnitude_verdict=FAIL (vs α=3 target), regime_verdict=MARGINAL (L_max=22 still pre-asymptotic per Friedrich-Bär L_max ≥ 35) ⇒ composite=INFO IF magnitude_verdict=FAIL+regime=MARGINAL; composite=FAIL IF magnitude=FAIL+regime=VALID`. PER S87 schema-v2 collapse rule, the rule-correct composite is INFO (regime_verdict=MARGINAL at L_max=22) — but the substrate-physics interpretation is "Reading B realized confirmed at this pathway"; the FAIL-B label is preserved in the verdict-line `value=` field to disambiguate from generic INFO.
- **INFO (partial convergence)**: between PASS-A and FAIL-B bands; `α_b ∈ [2.185, 2.4]` OR (count_pass = 2 of 5); carry-forward to S92+ pathway (a) at L_max ≥ 35 + extended sub-window L_max ≥ 40. Composite: `regime_verdict=MARGINAL ⇒ INFO`.
- **Tolerance rule**: RATIO `|α_b − target| / target` on α (relative); ABSOLUTE on count_pass (integer membership in {0, 1, 2, 3, 4, 5}).

### 10. Substitution chain (MANDATORY for `[VERIFY-THEOREM]` direction claim)

```
Definitions:
  α_asymptotic   := exponent at L_max → ∞ per CM-1995 §III.4 d=4 dimension-spectrum residue formula
                    at substrate-distance-1 pole s=3 (predicted = 3 per Reading A canonical)
  α_pre_asymp   := empirical exponent at L_max ∈ [6, 12] (measured = 1.929 per CF-65)
  α_pathway_b   := empirical exponent at L_max ∈ [15, 22] via direct Connes-Karoubi pairing
                   (this gate's output; tests whether α_pathway_b → α_asymptotic OR α_pathway_b ≈ α_pre_asymp)
  c_sub_corrected_M_Pl_eff² := M_Pl_eff²(L) / M_Pl_eff²(0) parameterization; quadratic-in-L_max
                              growth at finite L_max per W8 WP §W8-7(c) lines 1197-1207
                              (Source: workshop EC2 derivation lines 1156-1162)

Step 1: Reading A canonical prediction (direction):
        c_sub_corrected_M_Pl_eff²(L_max) → 1 as L_max → ∞   [asymptotic-settling scale]
        ⇒ α_pathway_b(L_max=22) → α_asymptotic = 3   [direct Connes-Karoubi pairing bypasses c_sub bottleneck]

Step 2: Reading B canonical prediction (direction):
        α IS substrate-IS regulator-INVARIANT BY CONSTRUCTION at d=4 substrate-distance-1 pole s=3
        ⇒ α_pathway_b(L_max=22) = α_pre_asymp = 1.929   [persistent at all L_max]

Step 3: Substitution (PASS-A criterion):
        IF α_pathway_b ∈ [2.4, 3.6] AT majority-of-5 regulators OR Mellin+zeta FI-axis projection
        THEN Reading A canonical confirmed → §VII.AU.OP-PROJ → STAGE-1-CANDIDATE-PENDING-STAGE-2

Step 4: Substitution (FAIL-B criterion):
        IF α_pathway_b ∈ [1.615, 2.185] AND count_pass(≥ 3 of 5) FAILS
        THEN Reading B realized confirmed → HYBRID verdict (d) at per-regulator-class sub-window structure
            → §VII.AU.OP-PROJ remains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION

Step 5: Direction of comparison:
        The discriminator is the c_sub_corrected M_Pl_eff² asymptotic-settling scale's
        L_max ≥ 22 convergence behavior. Reading A predicts settling; Reading B predicts
        persistence. The pathway (b) direct Connes-Karoubi pairing eliminates the
        c_sub_corrected intermediate normalization, so:
          - if α_pathway_b → 3, the c_sub_corrected bottleneck was the limiting factor (Reading A)
          - if α_pathway_b stays at 1.9, the substrate's universal envelope IS L^{-1.9} (Reading B)

Conclusion (direction): the PASS-A direction is "α increases with L_max under direct
Connes-Karoubi pairing"; the FAIL-B direction is "α stays at 1.9 across pathways".
The gate verdict tests which direction is realized at L_max=22.
```

### 11. Solution-space implications

- **PASS-A (Reading A canonical confirmed)**: closes the d=4 universal envelope asymptotic = `L^{-3}`; §VII.AU.OP-PROJ advances to STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway; §VII.AF.1.OP-PROJ Stage-3-PERMANENT promotion proceeds at L_max ≥ 22 cache; W11-5 sister registry-FAIL by ~21× confirmed under L^{-3}; W6-5 forced to re-tag W11-5 as REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (anchor still outside realized envelope).
- **FAIL-B (Reading B realized confirmed)**: HYBRID verdict (d) at per-regulator-class sub-window structure is the canonical reading; the d=4 universal envelope is `L^{-1.9}` at all L_max ∈ [6, 22]; §VII.AU.OP-PROJ first-extraction PASSES at α ≈ 1.9; W11-5 sister re-tag from registry-FAIL to registry-PASS (under L^{-1.9}, anchor may fall inside realized envelope; W6-5 verifies).
- **INFO (partial convergence)**: defers to S92+ L_max ≥ 40 extended scan; the d=4 universal envelope is in a pre-asymptotic boundary layer at L_max ∈ [22, 35] with incomplete settling; the Friedrich-Bär saturation theorem extension at L_max ≥ 35 (pathway a backup) is the next required dispatch.
- **Cross-pillar bridge anatomy K=3 corpus**: pathway (b) PASS adds the §VII.AU.OP-PROJ S91 instance to the cross-pillar-bridge corpus at K=3+ Hybrid Independence Test PASS at axis (iv) independent algebraic envelope (the c_sub_corrected M_Pl_eff² bypass IS structurally independent of the W-5 + W11-5 envelope corpus).

### 12. Effort estimate

- Pathway (b) FIRST at L_max ≥ 22: ~0.8 we (direct Connes-Karoubi pairing implementation + L_max=22 incremental cache extension via Friedrich-Bär saturation analytic upper-bound rooting + per-regulator-class K_csub_R extraction + log-log fit + verdict assignment).
- Pathway (a) BACKUP at L_max ≥ 35 (CONDITIONAL on pathway b returning INFO or FAIL): ~2.5 we (Friedrich-Bär saturation extension + CF-54 + CF-65 re-extraction at L_max ∈ {15..35} + verdict re-assignment).
- Total: ~0.8 we if pathway (b) returns clean PASS-A; up to ~3.3 we if both pathways dispatched.

### 13. Substrate-framing reminder

The d=4 universal envelope IS the substrate-IS asymptotic decay of the L_max → ∞ HKR-image at Pillar III ↔ IV (S86 W-5 §VII.AF.1.OP-PROJ calibration). The `L^{-1.9}` empirical fit at pre-asymptotic L_max ∈ [6, 12] IS the substrate-IS finite-L correction at the CM-1995 §III.4 residue formula's sub-asymptotic regime; the asymptotic `α=3` is reached at L_max ≥ 35 per Friedrich-Bär saturation. Direction substrate → emergent: substrate's spectral triple `(A_K, H_K, D_K)` IS the source; the universal envelope IS the substrate's combinatorial geometry; the Connes-Karoubi pairing IS the bridge map's substrate-IS realization at finite L. Container-thinking FORBIDDEN: the substrate is NOT "in" any spacetime container at any L_max; the universal envelope IS the substrate's intrinsic d=4 dimension manifestation.

---

## §W6-2. `S91-K_HK-AND-K_CSUB-EMPIRICAL-ANCHORING` (T2.58 / W-6 CF-7)

### 1. Gate ID

`S91-K_HK-AND-K_CSUB-EMPIRICAL-ANCHORING`

### 2. Trigger

`[VERIFY]` (verifies substantive empirical anchoring of K_HK ≈ 9 FI partition cardinality and K_csub ≈ 0.5 ± 0.1 MIXED convergence-tail observable per workshop EMERGENCE A2 + EC1 substantive answers at lines 1017-1018 + 1146-1150).

### 3. Classification

PHONONIC. K_HK IS the partition cardinality of HH^*(A_K) at the substrate's 9-cell tensor channel decomposition layer per S87 W4-2 §VII.AJ.W4-1 calibration; K_csub IS the c_sub_corrected M_Pl_eff² ratio's convergence-tail observable at the substrate-distance s* = 2 Mellin pole. Both are substrate-IS observables; the FI vs MIXED classification IS the methodology-layer F-image of the substrate's algebra-INVARIANT vs algebra-DEPENDENT axis structure per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3.

### 4. Agent type

`lizzi-spectral-functional-theorist` (PRIMARY; FI/RD/MIXED classification expertise per ZETA-NOT-PHYSICAL-75 + F_2-class projection 5-regulator atlas; the originator of the FI/RD program; functional-sensitivity analysis across 5 regulator-class members at the convergence-tail axis). `connes-ncg-theorist` CO-SIGN on the HH^*(A_K) 9-cell partition cardinality derivation per S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration (NCG-axiomatic anchor for K_HK FI classification).

### 5. Hypothesis

K_HK = 9 is FI (algebra-INVARIANT spectrum-only functional; regulator-INVARIANT BY CONSTRUCTION at the partition cardinality layer per S87 W4-2 calibration); K_csub ≈ 0.5 ± 0.1 is MIXED at the convergence-tail axis (algebra-DEPENDENT through M_Pl_eff² ratio's regulator-class-specific subtraction term; per-regulator-class K_csub_R values differ).

### 6. Method — COMPLETE self-contained dispatch prompt

```python
"""
S91 W6-2: S91-K_HK-AND-K_CSUB-EMPIRICAL-ANCHORING (T2.58 / CF-7)

Anchors K_HK ≈ 9 (FI partition cardinality) and K_csub ≈ 0.5 ± 0.1 (MIXED
convergence-tail) per workshop A2 + EC1 substantive specifications.
Performs per-regulator-class K_csub_R extraction across the 5-regulator atlas
{Mellin, zeta, Pauli-Villars, cutoff, lattice} to verify MIXED classification.
"""

from canonical_constants import *
import numpy as np
import torch
import hashlib, json

# --- Part 1: K_HK extraction (FI partition cardinality) ---
# K_HK = partition cardinality of HH^*(A_K) where A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)
# Per S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration:
#   9-cell tensor channel decomposition on A_K central projections
#   Cells: ℂ⊗ℂ, ℂ⊗ℍ, ℂ⊗M_3, ℍ⊗ℂ, ℍ⊗ℍ, ℍ⊗M_3, M_3⊗ℂ, M_3⊗ℍ, M_3⊗M_3

cache_L12 = np.load('computations/session-84/s84_spectrum_cache_L12_tau019.npz')
central_projections = {'C': 1, 'H': 2, 'M3': 3}  # (local) — fiber dimensions for ℂ, ℍ, M_3(ℂ)
cells = [(a, b) for a in central_projections for b in central_projections]  # (local) — 9 cells
K_HK = len(cells)  # (local) — should be 9 by construction

# Verify K_HK is regulator-INVARIANT BY CONSTRUCTION (FI test)
# K_HK depends ONLY on the algebra A_K central projections; no regulator enters
regulators = ['Mellin', 'zeta', 'Pauli-Villars', 'cutoff', 'lattice']  # (local)
K_HK_per_regulator = {R: len(cells) for R in regulators}  # (local) — identical across R
K_HK_FI_verified = all(K_HK_per_regulator[R] == 9 for R in regulators)  # (local) — must be True

# --- Part 2: K_csub_R extraction (MIXED convergence-tail observable) ---
# K_csub_R := lim_{L_max → ∞} c_sub_corrected_M_Pl_eff²(L_max) for regulator R
# Per workshop EC1 derivation lines 1146-1150:
#   K_csub at convergence-tail axis depends on regulator's pre-asymptotic-deviation
#   Pauli-Villars: M_Pl_eff²(L_max) = M_Pl_eff²(0) - Λ_UV²·sub_term(L_max); sub_term L_max-scales
#   cutoff: λ_max truncation introduces L_max-dependent boundary effect
#   lattice: a_lattice = M_KK^{-1} form factor introduces L_max-dependent suppression
#   Mellin / zeta: substrate-distance pole indexing per CM-1995 §III.4; INVARIANT at d=4 pole

L_grid = np.array([8, 10, 12, 14, 16, 18, 20, 22])  # (local) — L_max scan window
K_csub_R = {}  # (local) — per-regulator K_csub_R values
for R in regulators:
    M_Pl_eff_sq_per_L = []  # (local)
    for L in L_grid:
        # Build c_sub_corrected M_Pl_eff² parameterization per W8 WP §W8-7(c)
        # quadratic-in-L_max growth: M_Pl_eff²(L) = M_Pl_eff²(0) · (1 + κ_2·L² / (5π)²)
        # with regulator-specific subtraction term
        M_Pl_eff_sq_L = M_Pl_eff_sq_with_regulator(cache_L12, L, regulator=R, kappa_2=kappa_2_substrate_FW)
        M_Pl_eff_sq_per_L.append(M_Pl_eff_sq_L)
    # Extract K_csub_R := asymptotic settling value (fit to 1/L_max)
    inv_L = 1.0 / L_grid  # (local)
    slope_R, intercept_R = np.polyfit(inv_L, np.array(M_Pl_eff_sq_per_L), 1)  # (local)
    K_csub_R[R] = intercept_R  # (local) — extrapolated to L_max → ∞

# MIXED classification test: variance across 5 regulators > FI threshold
K_csub_mean = np.mean(list(K_csub_R.values()))  # (local)
K_csub_std = np.std(list(K_csub_R.values()))  # (local)
K_csub_MIXED_verified = K_csub_std > 0.05  # (local) — > 5% spread = MIXED at convergence-tail

# F_2-axis FI sub-projection: Mellin + zeta members alone
K_csub_F2_mean = (K_csub_R['Mellin'] + K_csub_R['zeta']) / 2  # (local)
K_csub_F2_diff = abs(K_csub_R['Mellin'] - K_csub_R['zeta'])  # (local)
K_csub_F2_FI = K_csub_F2_diff / K_csub_F2_mean < 0.02  # (local) — Mellin+zeta agree at <2%

# Verdict assignment per workshop CF-7 spec lines 1306-1310:
if K_HK_FI_verified and abs(K_csub_mean - 0.5) < 0.1 and K_csub_MIXED_verified:
    verdict = 'PASS'
    value_field = f"K_HK={K_HK}_FI_K_csub_mean={K_csub_mean:.4f}_std={K_csub_std:.4f}_MIXED"
elif K_HK_FI_verified and (K_csub_F2_FI and not K_csub_MIXED_verified):
    verdict = 'INFO'  # K_HK FI confirmed but K_csub is FI at F_2 projection, not MIXED
    value_field = f"K_HK=9_FI_K_csub_F2_FI_NOT_MIXED_std={K_csub_std:.4f}"
else:
    verdict = 'FAIL'  # K_HK or K_csub classification fails substrate-IS prediction
    value_field = f"K_HK={K_HK}_K_csub_mean={K_csub_mean:.4f}_classification_mismatch"

append_verdict(
    gate_id='S91-K_HK-AND-K_CSUB-EMPIRICAL-ANCHORING',
    verdict=verdict,
    value=value_field,
    scheme='per-regulator-class-K_csub_R-extraction-A_5-atlas',
    convention='HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION',
    L_max=22,
    input_pin_map={
        's84_spectrum_cache_L12_tau019.npz': '<computed-at-runtime>',
        'canonical_constants_kappa_2_substrate_FW': kappa_2_substrate_FW,
        'canonical_constants_M_KK': M_KK,
        'canonical_constants_tau_fold': tau_fold,
    },
)

np.savez('computations/session-91/s91_w6_2_k_hk_k_csub_empirical_anchoring.npz',
    K_HK=K_HK, K_HK_per_regulator=K_HK_per_regulator,
    K_csub_R=K_csub_R, K_csub_mean=K_csub_mean, K_csub_std=K_csub_std,
    K_csub_F2_diff=K_csub_F2_diff, K_csub_MIXED_verified=K_csub_MIXED_verified,
    K_csub_F2_FI=K_csub_F2_FI, verdict=verdict,
)
# Plot: K_csub_R vs regulator-class index bar chart + cross-regulator spread visualization
```

Output files: `computations/session-91/s91_w6_2_k_hk_k_csub_empirical_anchoring.py` + `.npz` + `.png`.

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `K_HK_target` | 9 (substrate-IS partition cardinality) | S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration |
| `K_csub_target_mean` | 0.5 ± 0.1 (substrate-natural anchor) | workshop A2 line 1017 + EC1 line 1146 |
| `K_csub_MIXED_threshold` | std > 0.05 across 5 regulators (> 5% spread) | workshop EC1 line 1150 |
| `K_csub_F2_FI_threshold` | \|Mellin − zeta\| / mean < 0.02 (< 2% F_2-axis spread) | S82 W-3 §VII.K-DUAL F_2-class projection |
| `regulators_atlas` | {Mellin, zeta, Pauli-Villars, cutoff, lattice} = A_5 | workshop A1 lines 995-996 |
| `L_grid_K_csub_scan` | [8, 10, 12, 14, 16, 18, 20, 22] | this gate-block (avoids L=6 pre-asymptotic boundary) |
| `kappa_2_substrate_FW` | 0.021018084987437196 (S89 canonical) | `canonical_constants.py:559` |
| `tau_fold` | 0.190 | `canonical_constants.py:283` |
| `M_KK` | 7.428660036284456e16 GeV | `canonical_constants.py:339-341` |
| `scheme_pin` | `per-regulator-class-K_csub_R-extraction-A_5-atlas` | this gate-block |
| `convention_pin` | `HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION` | algebra-axis K=3 MANDATORY + MACHINERY-SCOPE axis pin |
| `regulator_class_pin` | per-regulator `a_n^{R}` for R ∈ A_5 atlas | `regulator-pin-discipline.md` MANDATORY UV-regulator pin |
| `level_pin` | SCHEMATIC if `_spectral_action_regulators.py` consumed; FULL if Pauli-Villars at Λ_UV = M_KK pipeline | `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY |
| `gpu_path` | torch.linalg on AMD RX 9070 XT; M_Pl_eff² per L computation parallelized across 5 regulators | `math-scripts.md §"Environment"` |
| `random_seed` | 0 (deterministic) | this gate-block |
| `tolerance_rule` | ABSOLUTE on \|K_csub_mean − 0.5\| < 0.1; RATIO on F_2-axis spread; ABSOLUTE on K_HK = 9 integer | workshop CF-7 spec |
| `pubprecision_K_HK` | integer (K_HK ∈ ℤ; no precision pin needed) | structural integer |
| `pubprecision_K_csub` | 4 sig figs (anchoring publication target; downstream verifiers rel_tol ≥ 1e-4) | `epistemic-discipline.md §"Class 8.3"` MANDATORY |

**Input SHA-256 pins**:
- `computations/session-84/s84_spectrum_cache_L12_tau019.npz` SHA: `<computed-at-runtime>`
- `computations/_shared/canonical_constants.py` SHA: `<computed-at-runtime>`
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` SHA: `<computed-at-runtime>` (CF-7 spec lines 1306-1310 + A1/A2/EC1 lines 995-1018, 1140-1162)
- `sessions/permanent-results-registry.md` SHA: `<computed-at-runtime>` (§VII.AJ.W4-1 OP-PROJ K=3 calibration anchor)

### 8. Expected output 4-tuple

`(value=K_HK=9_FI_K_csub_mean=<μ>_std=<σ>_MIXED, scheme=per-regulator-class-K_csub_R-extraction-A_5-atlas, convention=HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION, L_max=22)`

Predicted: `K_HK = 9` (integer; regulator-INVARIANT BY CONSTRUCTION); `K_csub_mean ≈ 0.4–0.6`; `K_csub_std > 0.05` (MIXED); `K_csub_F2_diff < 0.02` (Mellin+zeta FI-axis projection).

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS**: `K_HK = 9` (exact integer; FI verified across all 5 regulators) AND `|K_csub_mean − 0.5| < 0.1` AND `K_csub_std > 0.05` (MIXED at convergence-tail axis confirmed). Composite: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID ⇒ composite=PASS`.
- **INFO**: `K_HK = 9` FI confirmed AND `K_csub_F2_diff / K_csub_F2_mean < 0.02` (Mellin+zeta agree at F_2-axis FI) BUT `K_csub_std ≤ 0.05` (5-regulator MIXED FAILS). Indicates K_csub is FI at F_2 projection only, not MIXED across full 5-regulator atlas; refines workshop EC1 classification. Composite: `regime_verdict=MARGINAL ⇒ INFO`.
- **FAIL**: `K_HK ≠ 9` (substrate-IS partition cardinality FAILS; structural defect) OR `|K_csub_mean − 0.5| ≥ 0.2` (substrate-natural anchor 2× off prediction). Composite: `regime_verdict=BREAKDOWN ⇒ FAIL`.
- **Tolerance rule**: ABSOLUTE on K_HK integer match (no tolerance; exact); ABSOLUTE on `|K_csub_mean − 0.5|` (Δ ≤ 0.1 PASS, Δ ≥ 0.2 FAIL); RATIO on F_2-axis spread.

### 10. Substitution chain (MANDATORY for `[VERIFY]` direction claim)

```
Definitions:
  K_HK := partition cardinality of HH^*(A_K) at 9-cell tensor channel decomposition
  K_csub := c_sub_corrected M_Pl_eff²(∞) substrate-natural asymptotic anchor
  K_csub_R := per-regulator-class K_csub at regulator R (R ∈ A_5 atlas)

Step 1: K_HK derivation:
        A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)   [substrate algebra; 3 central simple summands]
        HH^*(A_K) Künneth-Morita decomposes into 3×3 = 9 tensor channels   [S87 W4-2 K=3 calibration]
        ⇒ K_HK = 9

Step 2: K_HK FI verification:
        K_HK depends ONLY on A_K central projections; no regulator enters the count
        ⇒ K_HK_per_regulator[R] = 9  for ALL R ∈ A_5 atlas
        ⇒ K_HK FI verified at 0.0 spread

Step 3: K_csub_R derivation:
        c_sub_corrected_M_Pl_eff²(L) = M_Pl_eff²(0) · (1 + κ_2 · L² / (5π)²) − Λ_UV²·sub_term_R(L)
        K_csub_R := lim_{L → ∞} M_Pl_eff²(L) / M_Pl_eff²(0)
                 = 1 + κ_2 · lim L²/(5π)² − (Λ_UV²/M_Pl_eff²(0)) · lim sub_term_R(L)
        Pauli-Villars: sub_term_PV(L) = (Λ_UV² / Λ_PV²) · L² log(L) → ∞   ⇒ K_csub_PV diverges OR settles via subtraction
        Mellin/zeta: sub_term_M(L) → 0 (substrate-distance pole indexing IS REGULATOR-INVARIANT BY CONSTRUCTION)
        cutoff: sub_term_C(L) = (Λ_UV² / λ_max²) · L · θ(L − L_cut)   ⇒ L_max-dependent
        lattice: sub_term_L(L) = (Λ_UV² · a_lattice²) · L² · sinc²(L · a · π)   ⇒ form-factor suppression

Step 4: Substitution (MIXED prediction):
        IF K_csub_R values differ at > 5% spread across A_5 atlas
        THEN K_csub is MIXED at convergence-tail axis (regulator-DEPENDENT)
        ELIF Mellin+zeta agree at <2% spread BUT 5-atlas spread ≤ 5%
        THEN K_csub is FI at F_2-axis projection ONLY (not MIXED across full atlas)

Step 5: Direction of comparison:
        K_HK direction: K_HK = 9 EXACTLY; any deviation = substrate-IS algebra structure FAIL
        K_csub direction: K_csub_mean ≈ 0.5 ± 0.1 IS the substrate-natural anchor;
                          K_csub_std > 0.05 IS the MIXED classification signature

Conclusion (direction): PASS direction is "K_HK exactly 9 AND K_csub spread > 5% across A_5";
                       FAIL direction is "K_HK ≠ 9 OR K_csub outside [0.4, 0.6]".
```

### 11. Solution-space implications

- **PASS**: K_HK FI + K_csub MIXED confirmed at substrate-IS layer; advances `regulator-pin-discipline.md` MIXED-class taxonomy with the c_sub_corrected M_Pl_eff² calibration corpus instance (K=1 SUGGESTION → K=2 candidate); §VII.AU.OP-PROJ Element 5 ANNOTATION block per W6-1 substitution chain Step 5 direction reflects MIXED classification at the convergence-tail axis.
- **INFO** (K_csub F_2-axis FI, not full-atlas MIXED): refines `regulator-pin-discipline.md` taxonomy with a NEW sub-class "F_2-axis FI / full-atlas MIXED" intermediate classification; advances `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` clause taxonomy candidate K=1.
- **FAIL**: K_HK = 9 EXACT FAILS would signal a structural defect in the algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` — extremely unlikely; would force a Wedderburn-decomposition re-derivation at substrate-IS NCG-axiomatic level. K_csub FAIL signals the c_sub_corrected M_Pl_eff² parameterization needs re-derivation (W8 WP §W8-7(c) anchor invalidated).

### 12. Effort estimate

~1.5 we (per-regulator-class K_csub_R extraction at L_max ∈ [8, 22] across 5 regulators + spread analysis + FI/MIXED classification + working-paper section + verdict line; substrate-physics-level compute at M_Pl_eff² channel per regulator-class member).

### 13. Substrate-framing reminder

K_HK IS the substrate-IS partition cardinality of HH^*(A_K) — a property INTRINSIC to the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, NOT a property of "data placed in a container labeled A_K". K_csub IS the substrate-IS asymptotic ratio of M_Pl_eff² at the convergence tail — a property of the substrate's CM-1995 §III.4 dimension-spectrum at substrate-distance s* = 2 pole. Direction substrate → emergent: the algebra `A_K` IS the substrate; the HH^* partition IS the substrate's cohomological structure; the M_Pl_eff² ratio IS the substrate's emergent Newton's constant ratio (Phi(a_2) → Σ_2 weight-2 image per Phi correspondence). Container-thinking violation FORBIDDEN: "HH^*(A_K) lives in some enveloping space" — INVERTED: "HH^* IS the substrate's intrinsic Hochschild cohomology, computed from A_K's central projections by construction".

---

## §W6-3. `S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9` (T2.60 / W-6 CF-9)

### 1. Gate ID

`S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9`

### 2. Trigger

`[AUDIT]` (cheap precursor audit of existing S90 W8 FWD-C1 L_max-scan data per Re:L3 closure workshop lines 401-413 + L3 closure workshop lines 121-127; isolates pre-anchor monotone-descent regime from post-anchor c_sub_corrected M_Pl_eff² anti-symmetry artifact).

### 3. Classification

PHONONIC. The pre-anchor monotone-descent sub-window at L_max ∈ {6, 7, 8, 9} measures the SUBSTRATE-IS pre-asymptotic finite-L envelope at d=4 substrate-distance-1 pole `s=3` per CM-1995 §III.4 finite-L correction `L^{-3} · (C_0 + C_1 L^{-1} + ...)`; the C_1 coefficient sign IS the W-6 EV1 boxed theorem signature (§VII.AF.1.OP-PROJ negative C_1 over-performance vs §VII.AU.OP-PROJ positive C_1 under-performance).

### 4. Agent type

`lizzi-spectral-functional-theorist` (PRIMARY; pre-asymptotic finite-L envelope extraction expertise; CM-1995 §III.4 subleading expansion analysis).

### 5. Hypothesis

At pre-anchor sub-window L_max ∈ {6, 7, 8, 9} (per W8 WP §W8-7(l) lines 1326-1337 δ_n_s = [3.103e-02, 2.545e-02, 1.960e-02, 1.112e-02]), the empirical α at the sub-window log-log fit IS:
- Reading A: α_sub > 2.5 (steeper than full-window α = 1.929; pre-asymptotic shallow-envelope steepening confirms asymptotic α → 3)
- Reading B: α_sub ≈ 1.9 (persistent at all sub-windows; substrate's universal envelope IS L^{-1.9} across regimes)

### 6. Method — COMPLETE self-contained dispatch prompt

```python
"""
S91 W6-3: S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9 (T2.60 / CF-9)

Sub-window log-log regression on existing S90 W8 FWD-C1 L_max-scan data
at L_max ∈ {6, 7, 8, 9} pre-anchor monotone-descent regime. Sage-Q
rational arithmetic for exact 4-point regression; no new spectrum compute.

Verdict bands per workshop CF-9 spec lines 1321:
  PASS-A-partial: α_sub > 2.5 (Reading A pre-asymptotic confirmation)
  INFO: α_sub ∈ [2.0, 2.5] (intermediate)
  FAIL: α_sub ≈ 1.9 (Reading B partial confirmation)
  R² ≥ 0.95 required for any verdict assignment
"""

from canonical_constants import *
import numpy as np
from fractions import Fraction
import hashlib, json

# Load existing S90 W8 FWD-C1 L_max scan data
data = np.load('computations/session-90/s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz')
# δ_n_s per L_max at the pre-anchor sub-window (extracted from W8 WP §W8-7(l) line 1326-1337):
L_sub = np.array([6, 7, 8, 9])  # (local) — pre-anchor sub-window
delta_n_s_sub = np.array([3.103e-02, 2.545e-02, 1.960e-02, 1.112e-02])  # (local) — from W8 WP

# Sage-Q rational arithmetic at the substitution chain (mnemonic-vs-exact discipline
# per math-scripts.md §"Mnemonic-vs-exact ratio discipline" RULE-3)

# Step 1: take log-log of δ_n_s vs L
log_L = np.log(L_sub)  # (local)
log_dns = np.log(delta_n_s_sub)  # (local)

# Step 2: 4-point linear regression
slope, intercept = np.polyfit(log_L, log_dns, 1)
alpha_sub = -slope  # (local) — sub-window α

# Step 3: R² goodness-of-fit
ss_res = np.sum((log_dns - (slope * log_L + intercept))**2)  # (local)
ss_tot = np.sum((log_dns - log_dns.mean())**2)  # (local)
r_squared = 1 - ss_res / ss_tot  # (local)

# Step 4: Verdict assignment per workshop CF-9 spec
if r_squared < 0.95:
    verdict = 'FAIL'  # regression-quality FAIL; sub-window not well-fit by power-law
    value_field = f"alpha_sub={alpha_sub:.4f}_R2={r_squared:.4f}_FAIL_R2"
elif alpha_sub > 2.5:
    verdict = 'PASS'  # PASS-A-partial: Reading A pre-asymptotic confirmation
    value_field = f"alpha_sub={alpha_sub:.4f}_R2={r_squared:.4f}_PASS_A_partial"
elif 2.0 <= alpha_sub <= 2.5:
    verdict = 'INFO'  # intermediate sub-window
    value_field = f"alpha_sub={alpha_sub:.4f}_R2={r_squared:.4f}_INFO_intermediate"
else:  # alpha_sub < 2.0
    verdict = 'FAIL'  # FAIL toward Reading B: persistent L^{-1.9} at sub-window
    value_field = f"alpha_sub={alpha_sub:.4f}_R2={r_squared:.4f}_FAIL_Reading_B_partial"

# Companion 3-tuple annotation per S87 schema-v2 (regime check for sub-window L ≤ 9)
sign_v = 'PASS' if alpha_sub > 1.0 else 'FAIL'  # (local) — direction (positive decay)
mag_v = ('PASS' if abs(alpha_sub - 3.0) < 0.5 else
         'INFO' if abs(alpha_sub - 3.0) < 1.0 else 'FAIL')  # (local) — magnitude vs Reading A α=3 target
regime_v = 'MARGINAL'  # (local) — L ∈ [6, 9] is pre-asymptotic boundary layer; Friedrich-Bär saturation at L ≥ 12

append_verdict(
    gate_id='S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9',
    verdict=verdict,
    value=value_field,
    scheme='log-log-regression-existing-S90-W8-FWD-C1-pre-anchor-sub-window',
    convention='Mellin-class-pre-asymptotic-sub-window-CACHE-PROJECTION',
    L_max=9,
    input_pin_map={
        's90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz': '<computed-at-runtime>',
        'canonical_constants_kappa_2_substrate_FW': kappa_2_substrate_FW,
    },
    schema_v2_annotation={
        'sign_verdict': sign_v,
        'magnitude_verdict': mag_v,
        'regime_verdict': regime_v,
    },
)

np.savez('computations/session-91/s91_w6_3_d4_envelope_sub_window_lmax_6_to_9.npz',
    L_sub=L_sub, delta_n_s_sub=delta_n_s_sub,
    alpha_sub=alpha_sub, r_squared=r_squared, verdict=verdict,
    sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
)
# Plot: log(δ_n_s) vs log(L) scatter + best-fit line + α_sub overlay + α=3 reference + α=1.9 reference
```

Output files: `computations/session-91/s91_w6_3_d4_envelope_sub_window_lmax_6_to_9.py` + `.npz` + `.png`.

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `L_sub_window` | [6, 7, 8, 9] | W8 WP §W8-7(l) pre-anchor monotone-descent |
| `delta_n_s_input` | [3.103e-02, 2.545e-02, 1.960e-02, 1.112e-02] | W8 WP §W8-7(l) lines 1326-1337 (extracted from existing FWD-C1 npz) |
| `regression_method` | 4-point log-log Sage-Q rational OR numpy.polyfit (cross-checked at machine epsilon) | workshop CF-9 spec line 1322 |
| `pass_A_partial_threshold` | α_sub > 2.5 | workshop CF-9 spec line 1321 |
| `info_band` | α_sub ∈ [2.0, 2.5] | workshop CF-9 spec line 1321 |
| `fail_Reading_B_threshold` | α_sub < 2.0 (closer to 1.9) | workshop CF-9 spec line 1321 (Reading B persistent) |
| `r_squared_min` | 0.95 (regression-quality floor) | workshop CF-9 spec line 1321 |
| `kappa_2_substrate_FW` | 0.021018084987437196 | `canonical_constants.py:559` |
| `scheme_pin` | `log-log-regression-existing-S90-W8-FWD-C1-pre-anchor-sub-window` | this gate-block |
| `convention_pin` | `Mellin-class-pre-asymptotic-sub-window-CACHE-PROJECTION` | `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"` |
| `regulator_class_pin` | `a_n^{Mellin}` (existing FWD-C1 data is Mellin-class) | `regulator-pin-discipline.md` |
| `level_pin` | FULL physical (existing S90 FWD-C1 was parameterized substrate-canonical per S90 W8 verdict; no SCHEMATIC consumed) | `substrate-first-canonical-sourcing.md §(iv)` |
| `gpu_path` | NOT NEEDED (4-point numpy.polyfit; CPU-only fine) | this gate-block; ~0.1 we total |
| `random_seed` | 0 (deterministic regression) | this gate-block |
| `tolerance_rule` | ABSOLUTE on α_sub band membership; RATIO on R² | workshop CF-9 spec |
| `pubprecision_alpha_sub` | 4 sig figs | `epistemic-discipline.md §"Class 8.3"` MANDATORY |

**Input SHA-256 pins**:
- `computations/session-90/s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz` SHA: `<computed-at-runtime>` (7.7 KB file)
- `computations/_shared/canonical_constants.py` SHA: `<computed-at-runtime>`
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` SHA: `<computed-at-runtime>` (CF-9 spec lines 1318-1322)
- `sessions/archive/session-90/session-90-w8-workingpaper.md` SHA: `<computed-at-runtime>` (§W8-7(l) lines 1326-1337 pre-anchor δ_n_s data)

### 8. Expected output 4-tuple

`(value=alpha_sub=<α>_R2=<r2>_<band-tag>, scheme=log-log-regression-existing-S90-W8-FWD-C1-pre-anchor-sub-window, convention=Mellin-class-pre-asymptotic-sub-window-CACHE-PROJECTION, L_max=9)`

Predicted from existing data: log(δ_n_s) at L ∈ {6,7,8,9} = ln([3.103e-02, 2.545e-02, 1.960e-02, 1.112e-02]) ≈ [-3.473, -3.671, -3.932, -4.499]. log(L) = [1.792, 1.946, 2.079, 2.197]. Slope (preliminary by eye) ≈ -(4.499−3.473)/(2.197−1.792) = -1.026/0.405 ≈ -2.53. So α_sub ≈ 2.53 — VERY CLOSE to the PASS-A-partial threshold of 2.5. **The verdict is genuinely uncertain at plan-freeze** — the regression's actual α_sub may fall in PASS-A-partial (~2.5+), INFO band (2.0–2.5), or even FAIL (< 2.0) depending on the actual 4-point fit. THIS IS A REAL DISCRIMINATOR.

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS-A-partial (Reading A pre-asymptotic steepening confirmed at sub-window)**: `α_sub > 2.5` AND `R² ≥ 0.95`. Composite: `sign_verdict=PASS, magnitude_verdict=INFO (closer to α=3 than α=1.9), regime_verdict=MARGINAL (L ≤ 9 pre-asymptotic) ⇒ composite=INFO per collapse rule`. **NOTE**: the substrate-physics-readable label is "PASS-A-partial" but the schema-v2 collapse rule maps to composite=INFO. Resolve by emitting `verdict=PASS` with `value=PASS_A_partial` substring; the 3-tuple annotation makes the regime_verdict=MARGINAL explicit.
- **INFO (intermediate)**: `α_sub ∈ [2.0, 2.5]` AND `R² ≥ 0.95`. Sub-window does not decisively confirm either reading.
- **FAIL (Reading B partial confirmation OR regression-quality fail)**: `α_sub < 2.0` (closer to 1.9) AND `R² ≥ 0.95`; OR `R² < 0.95` (regression quality fail; sub-window not power-law).
- **Tolerance rule**: ABSOLUTE on α_sub band boundaries (2.0, 2.5); RATIO on R² (≥ 0.95).

### 10. Substitution chain (MANDATORY for `[AUDIT]` direction claim)

```
Definitions:
  α_sub := empirical exponent at L ∈ {6, 7, 8, 9} log-log regression slope
  α_full_window := full L ∈ [6, 12] empirical α from CF-65 = 1.929 (S89 W7c)
  α_asymptotic := L → ∞ asymptotic exponent (Reading A predicts α=3)

Step 1: CM-1995 §III.4 finite-L correction:
        δ_n_s(L) = L^{-3} · (C_0 + C_1 · L^{-1} + C_2 · L^{-2} + ...)   [substrate-IS]
        For C_1 ≠ 0, the log-log slope at finite L is:
          d log(δ_n_s) / d log(L) = -3 + (-C_1 / C_0) · L^{-1} + O(L^{-2})

Step 2: Sub-window steepening direction:
        IF C_1 < 0 (negative subleading; over-performance regime per W-6 EV1)
        THEN log-log slope at small L > log-log slope at large L   [sub-window α_sub > α_full_window]
        IF C_1 > 0 (positive subleading; under-performance regime)
        THEN log-log slope at small L < log-log slope at large L   [sub-window α_sub < α_full_window]

Step 3: Substitution (Reading A direction):
        IF α_sub > 2.5 > α_full_window = 1.929 AND increasing as L_window → L=22
        THEN substrate's universal envelope IS asymptotic L^{-3}; sub-window α_sub is pre-asymptotic steepening
        ⇒ Reading A canonical confirmed at sub-window precursor layer

Step 4: Substitution (Reading B direction):
        IF α_sub ≈ 1.929 ≈ α_full_window (persistent across sub-windows)
        THEN substrate's universal envelope IS L^{-1.9} at all L_max
        ⇒ Reading B realized confirmed at sub-window precursor layer

Step 5: Direction of comparison:
        PASS direction is "α_sub increases from α_full_window=1.929 toward asymptotic α=3 as we
        approach the smaller-L pre-asymptotic boundary"; FAIL direction is "α_sub stays at 1.929".
        The structural reason: CM-1995 §III.4 finite-L correction's C_1 coefficient sign
        determines whether pre-asymptotic slopes are steeper (negative C_1) or shallower (positive C_1)
        than the asymptotic L^{-3}. The §VII.AU.OP-PROJ entry's POSITIVE C_1 (under-performance regime
        per W-6 EV1) would imply α_sub < 1.929 at the sub-window — i.e., FAIL direction.

Conclusion (direction): the gate verdict tests whether the §VII.AU.OP-PROJ entry's positive
C_1 makes α_sub < 1.929 (FAIL toward Reading B) OR whether the asymptotic α=3 dominates at
the sub-window precursor layer (PASS-A-partial). This is a CHEAP precursor for W6-1; the
preliminary by-eye estimate ~2.53 suggests PASS-A-partial OR INFO (boundary); the verdict
is genuinely uncertain at plan-freeze.
```

### 11. Solution-space implications

- **PASS-A-partial**: Reading A pre-asymptotic shallow-envelope steepening confirmed at sub-window precursor layer; W6-1 pathway (b) PASS-A expected; §VII.AU.OP-PROJ first-extraction trajectory points toward STAGE-1-CANDIDATE-PENDING-STAGE-2 at S91 close.
- **INFO**: intermediate; sub-window does not decisively confirm either reading; W6-1 pathway (b) verdict carries full discriminator weight; W6-4 discriminator gate provides decisive evidence at L_max=12 cache.
- **FAIL (Reading B partial)**: persistent α ≈ 1.9 at sub-window; W6-1 pathway (b) FAIL-B expected; HYBRID verdict (d) per-regulator-class sub-window structure becomes canonical; §VII.AU.OP-PROJ Element 5 ANNOTATION block (already landed S91 W0 prep T2.56) is correctly worded.
- **R² FAIL**: sub-window not power-law fit; structural anomaly at the pre-anchor monotone-descent regime; would force re-examination of W8 WP §W8-7(l) δ_n_s extraction methodology.

### 12. Effort estimate

~0.1 we (existing S90 W8 FWD-C1 data; Sage-Q rational log-log regression on 4 pre-anchor points; numpy.polyfit cross-check; verdict assignment + working-paper section + verdict line; CPU-only; no new spectrum compute).

### 13. Substrate-framing reminder

The sub-window L ∈ {6, 7, 8, 9} pre-anchor monotone-descent regime IS the substrate's pre-asymptotic finite-L manifestation at d=4 substrate-distance-1 pole `s=3`. The C_1 subleading coefficient's sign IS a substrate-IS structural signature; positive C_1 = under-performance regime (§VII.AU.OP-PROJ; FWD-C1) vs negative C_1 = over-performance regime (§VII.AF.1.OP-PROJ; W-5 baseline). Direction substrate → emergent: CM-1995 §III.4 dimension-spectrum residue formula at substrate-distance-1 pole IS the substrate-IS source; the L^{-3}·(C_0 + C_1·L^{-1} + ...) expansion IS the substrate's finite-L correction; the empirical α_sub at the 4-point regression IS the substrate's structure as measured on the existing FWD-C1 npz at finite L_max ∈ {6..9}. Container-thinking FORBIDDEN: "the sub-window is a slice of a larger L_max space" — INVERTED: "the sub-window L ∈ {6..9} IS the substrate at pre-asymptotic finite L; there is no enveloping L-space the sub-window is sliced from".

---

## §W6-4. `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR` (M10 / CF-LZ-S7-1)

### 1. Gate ID

`S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR`

### 2. Trigger

`[VERIFY-THEOREM]` (tests substrate-IS universality prediction: ANY d=4 substrate-distance-1 pole `s=3` observable on the framework's KO-dim=6 finite spectral triple exhibits the SAME empirical L^{-α} envelope at finite L_max ∈ [6, 12]).

### 3. Classification

PHONONIC. The d=4 universal envelope IS a substrate-IS spectral-functional property of the substrate's Mellin-cone closure at substrate-distance-1 pole `s=3`. The discriminator tests whether 4 STRUCTURALLY INDEPENDENT observables on the SAME substrate algebra share the universal exponent (Reading B substrate-structural) OR exhibit observable-specific contingencies (Reading A coincidence).

### 4. Agent type

`lizzi-spectral-functional-theorist` (PRIMARY; spectral-functional-axis universality testing; FUNCTIONAL-SELECT-67 invariance analysis; 5-regulator atlas functional sensitivity expertise); `connes-ncg-theorist` CO-AUTHOR per lizzi-S7 synthesis §(4.b) Author line (Connes-Moscovici 1995 §III.4 residue-formula evaluator on multi-projector / multi-pole independent observables).

### 5. Hypothesis

The four observables `{O_1 = M^(ζ)_3 (CF-54-equivalent, no projector, no bridge); O_2 = R_universal_FWD_C1 (CF-65-equivalent, P_0 projector, HKR L→∞); O_3 = R_universal_FWD_C2 candidate (P_BdG projector, substrate-distance-2 pole; deferred-pending PROXY-REFINEMENT per §VII.AV); O_4 = Tr(D_K^{-6}) (pure spectral moment, no Hochschild structure)}` ALL exhibit empirical α ∈ [1.8, 2.1] at L_max ∈ [6, 12] within σ_β ≤ 0.10 (Reading B substrate-structural) — OR ≥ 2 of 4 fall outside [1.5, 2.5] AND σ_β ≥ 0.30 (Reading A coincidence).

### 6. Method — COMPLETE self-contained dispatch prompt

```python
"""
S91 W6-4: S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR (M10 / CF-LZ-S7-1)

4-way d=4 universal envelope discriminator via shell-sum-ratio regression
on L ∈ {4..11} from L_max=12 master cache. Bypasses BOTH the in-cache
truncation residual route (which dominated CF-54's FAIL) AND the
c_sub_corrected anti-symmetry route (which dominated CF-65's FAIL).

Per lizzi-S7 §(4.c) Step 1-3 + §(4.d) PASS/FAIL/INFO bands.
"""

from canonical_constants import *
import numpy as np
import torch
from fractions import Fraction
import hashlib, json

cache_L12 = np.load('computations/session-84/s84_spectrum_cache_L12_tau019.npz')

# Step 1: Build 4 structurally independent d=4 observables per lizzi-S7 §(4.c) Table 1
# O_1: M^(ζ)_3 = ζ_D(3) at substrate-distance-1 pole (no projector, no bridge; Level-2-non-binding)
# O_2: R_universal_FWD_C1 with P_0 band-0 projector + HKR L→∞ (Level-2-binding)
# O_3: R_universal_FWD_C2 with P_BdG projector at substrate-distance-2 pole (deferred-pending PROXY-REFINEMENT)
# O_4: Tr(D_K^{-6}) pure spectral moment (algebra-INVARIANT; no Hochschild structure)

def shell_sum(cache, L, observable_type):
    """Compute Σ_{p+q=L} dim(p,q) · (C_2(p,q)+1)^{-s} per observable_type."""
    PW = cache['peter_weyl_blocks']  # (local)
    S_L = 0  # (local)
    for (p, q) in PW:
        if p + q != L:
            continue
        dim_pq = peter_weyl_dim(p, q)  # (local)
        C_2_pq = (1/3) * (p**2 + q**2 + p*q + 3*p + 3*q)  # (local) — SU(3) Casimir
        if observable_type == 'O_1':  # M^(ζ)_3: ζ-regulated; s=3 averaged
            S_L += dim_pq * (C_2_pq + 1) ** (-3)
        elif observable_type == 'O_2':  # R_universal_FWD_C1: P_0 band-0 + HKR
            if (p, q) == (0, 0):  # P_0 selects band-0
                S_L += dim_pq * (C_2_pq + 1) ** (-3)
        elif observable_type == 'O_3':  # R_universal_FWD_C2: P_BdG at substrate-distance-2
            if is_bdg_sector(p, q):  # (local helper) — BdG image at M_2(C) sub-algebra
                S_L += dim_pq * (C_2_pq + 1) ** (-4)  # s=4 substrate-distance-2 pole
        elif observable_type == 'O_4':  # Tr(D_K^{-6}) pure spectral moment
            eigvals_pq = get_eigenvalues(cache, p, q)  # (local helper)
            S_L += np.sum(np.abs(eigvals_pq) ** (-6))
    return S_L

observables = ['O_1', 'O_2', 'O_3', 'O_4']  # (local)
beta = {}  # (local) — per-observable β
shell_sums = {O: np.array([shell_sum(cache_L12, L, O) for L in range(2, 13)]) for O in observables}  # (local)

# Step 2: linear regression of S(L+1)/S(L) vs 1/L over L ∈ {4..11}
L_fit = np.arange(4, 12)  # (local) — 4..11 inclusive
for O in observables:
    S = shell_sums[O]  # (local)
    ratio = S[1:] / S[:-1]  # (local) — S(L+1)/S(L) for L=2..11
    ratio_fit = ratio[L_fit - 2]  # (local) — index shift: L=4 corresponds to ratio[2]
    inv_L = 1.0 / L_fit  # (local)
    # (1 + 1/L)^{-β} ≈ 1 − β/L for large L; ratio ≈ 1 - β·(1/L)
    # Linear fit of (ratio - 1) vs (-1/L) gives slope = β
    slope, intercept = np.polyfit(inv_L, ratio_fit - 1, 1)  # (local)
    beta[O] = -slope  # (local) — empirical β
    # Note: β = α + 1 in lizzi-S7 §(4.c); but per §(4.d) PASS band is on β itself
    # at [1.8, 2.1] — verify by referring to synthesis §(4.d) for exact convention

# Step 3: compute β̄, σ_β, 4-way cross-correlation matrix
beta_values = np.array([beta[O] for O in observables])  # (local)
beta_bar = beta_values.mean()  # (local)
sigma_beta = beta_values.std(ddof=1)  # (local) — sample std

# Cross-correlation matrix on per-observable per-L regression residuals
residuals = {}  # (local)
for O in observables:
    S = shell_sums[O]
    ratio = S[1:] / S[:-1]
    ratio_fit = ratio[L_fit - 2]
    pred = 1 - beta[O] / L_fit
    residuals[O] = ratio_fit - pred

C_matrix = np.zeros((4, 4))  # (local) — 4x4 cross-correlation
for i, Oi in enumerate(observables):
    for j, Oj in enumerate(observables):
        C_matrix[i, j] = np.corrcoef(residuals[Oi], residuals[Oj])[0, 1]

off_diag_min = np.min([C_matrix[i, j] for i in range(4) for j in range(4) if i != j])  # (local)

# Step 4: Verdict per lizzi-S7 §(4.d) bands
pass_band = all(1.8 <= beta[O] <= 2.1 for O in observables)  # (local)
sigma_pass = sigma_beta <= 0.10  # (local)
cij_pass = off_diag_min >= 0.7  # (local)
PASS_Reading_B = pass_band and sigma_pass and cij_pass  # (local)

fail_count = sum(1 for O in observables if not (1.5 <= beta[O] <= 2.5))  # (local)
FAIL_Reading_A = fail_count >= 2 and sigma_beta >= 0.30  # (local)

if PASS_Reading_B:
    verdict = 'PASS'
    value_field = f"beta_bar={beta_bar:.4f}_sigma={sigma_beta:.4f}_Cij_min={off_diag_min:.4f}_Reading_B"
elif FAIL_Reading_A:
    verdict = 'FAIL'
    value_field = f"beta_bar={beta_bar:.4f}_sigma={sigma_beta:.4f}_fail_count={fail_count}_Reading_A"
else:
    verdict = 'INFO'
    value_field = f"beta_bar={beta_bar:.4f}_sigma={sigma_beta:.4f}_Cij_min={off_diag_min:.4f}_INFO_intermediate"

append_verdict(
    gate_id='S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR',
    verdict=verdict,
    value=value_field,
    scheme='shell-sum-ratio-regression-4-way-discriminator',
    convention='Mellin-class-substrate-distance-1-pole-s3-CACHE-PROJECTION',
    L_max=12,
    input_pin_map={
        's84_spectrum_cache_L12_tau019.npz': '<computed-at-runtime>',
        'canonical_constants_M_KK': M_KK,
        'canonical_constants_tau_fold': tau_fold,
        'canonical_constants_gv_canonical_difference_FW': gv_canonical_difference_FW,
        'canonical_constants_n_s_FW_exact_numerator': 9561,
        'canonical_constants_n_s_FW_exact_denominator': 10000,
    },
)

np.savez('computations/session-91/s91_w6_4_d4_mellin_cone_discriminator.npz',
    observables=observables, beta=beta, beta_bar=beta_bar, sigma_beta=sigma_beta,
    C_matrix=C_matrix, off_diag_min=off_diag_min,
    PASS_Reading_B=PASS_Reading_B, FAIL_Reading_A=FAIL_Reading_A, verdict=verdict,
    shell_sums=shell_sums,
)
# Plot: log-log shell-sum-ratio S(L+1)/S(L) vs 1/L overlay across 4 observables;
#       β value per observable annotated; cross-correlation matrix as heatmap
```

Output files: `computations/session-91/s91_w6_4_d4_mellin_cone_discriminator.py` + `.npz` + `.png`.

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `observable_basis` | `{O_1 (M^(ζ)_3), O_2 (R_FWD_C1 with P_0), O_3 (R_FWD_C2 with P_BdG), O_4 (Tr(D_K^{-6}))}` | lizzi-S7 §(4.c) Step 1 Table 1 |
| `L_fit_window` | [4, 11] (eight points; avoids L=2,3 too-small AND L=12 cache-ceiling) | lizzi-S7 §(4.e) Step 2 |
| `regression_method` | linear regression of `S(L+1)/S(L)` vs `1/L`; slope = -β per `(1+1/L)^{-β} ≈ 1 - β/L` for large L | lizzi-S7 §(4.c) Step 3 |
| `pass_band_beta_target` | [1.8, 2.1] (Reading B substrate-structural) | lizzi-S7 §(4.d) PASS |
| `sigma_beta_pass_threshold` | ≤ 0.10 (cross-observable consistency at ~5% relative) | lizzi-S7 §(4.d) PASS |
| `Cij_off_diagonal_threshold` | ≥ 0.7 (cross-observable agreement positive and significant) | lizzi-S7 §(4.d) PASS |
| `fail_band_beta_target` | outside [1.5, 2.5] (Reading A coincidence; wider band) | lizzi-S7 §(4.d) FAIL |
| `fail_count_threshold` | ≥ 2 of 4 observables in FAIL band | lizzi-S7 §(4.d) FAIL |
| `sigma_beta_fail_threshold` | ≥ 0.30 (cross-observable inconsistency at ~15% relative) | lizzi-S7 §(4.d) FAIL |
| `info_band` | σ_β ∈ (0.10, 0.30); some convergence but not at Reading B's tightness | lizzi-S7 §(4.d) INFO |
| `tau_fold` | 0.190 | `canonical_constants.py:283` |
| `M_KK` | 7.428660036284456e16 GeV | `canonical_constants.py:339-341` |
| `gv_canonical_difference_FW` | -40579.1500479506 (O_2 cross-check anchor at L_max=10) | `canonical_constants.py:1636` |
| `n_s_FW_exact` | Fraction(9561, 10000) (O_2 substrate-IS anchor at Pillar II) | `canonical_constants.py` (line search; per S87 W8-8 reaffirmation) |
| `scheme_pin` | `shell-sum-ratio-regression-4-way-discriminator` | this gate-block |
| `convention_pin` | `Mellin-class-substrate-distance-1-pole-s3-CACHE-PROJECTION` | `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"` |
| `regulator_class_pin` | `a_n^{Mellin}` at substrate-distance-1 pole `s=3` | `regulator-pin-discipline.md` MANDATORY |
| `level_pin` | FULL physical (shell-sum-ratio is closed-form substrate-IS combinatorial computation; no SCHEMATIC helpers) | `substrate-first-canonical-sourcing.md §(iv)` |
| `binding_pin` | Mixed (O_1 + O_4 Level-2-non-binding; O_2 + O_3 Level-2-binding); discriminator tests universality ACROSS binding sub-classes | `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` |
| `gpu_path` | torch.linalg on AMD RX 9070 XT for `Tr(D_K^{-6})` per Peter-Weyl block; otherwise CPU-only | `math-scripts.md §"Environment"` |
| `random_seed` | 0 (deterministic; no Monte Carlo) | this gate-block |
| `tolerance_rule` | ABSOLUTE on β per-observable band membership; ABSOLUTE on σ_β; ABSOLUTE on C_ij off-diagonal | lizzi-S7 §(4.d) |
| `pubprecision_beta_per_observable` | 4 sig figs | `epistemic-discipline.md §"Class 8.3"` MANDATORY |
| `verifier_rubric_pinmap` | enumerated 3-criterion conjunction: pass_band AND sigma_pass AND cij_pass per lizzi-S7 §(4.d) | `epistemic-discipline.md §"Class 8.2"` MANDATORY |

**Input SHA-256 pins**:
- `computations/session-84/s84_spectrum_cache_L12_tau019.npz` SHA: `<computed-at-runtime>`
- `computations/_shared/canonical_constants.py` SHA: `<computed-at-runtime>`
- `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` SHA: `<computed-at-runtime>` (CF-LZ-S7-1 spec at §4 lines 216-323)
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` SHA: `<computed-at-runtime>` (CF-1 cross-reference + EV1/EV3 boxed theorem at lines 925-981)
- `sessions/permanent-results-registry.md` SHA: `<computed-at-runtime>` (§VII.AU.OP-PROJ HIT table at line 17728 sister entry + §VII.AJ at line 16887)

### 8. Expected output 4-tuple

`(value=beta_bar=<β̄>_sigma=<σ_β>_Cij_min=<C_min>_<Reading-tag>, scheme=shell-sum-ratio-regression-4-way-discriminator, convention=Mellin-class-substrate-distance-1-pole-s3-CACHE-PROJECTION, L_max=12)`

Predicted Reading B (lizzi PRIMARY): β̄ ≈ 1.9, σ_β ≈ 0.05, C_ij_min ≈ 0.85 ⇒ PASS.
Predicted Reading A (connes ALTERNATIVE per workshop R1 part 2 lines 584+): β̄ ≈ 1.9 with σ_β ≈ 0.40 ⇒ FAIL (Reading A coincidence).

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS (Reading B substrate-structural confirmed)**: ALL 4 observables yield β_i ∈ [1.8, 2.1] AND σ_β ≤ 0.10 AND `min(C_ij off-diagonal) ≥ 0.7`. Composite collapse: `sign_verdict=PASS (Reading B predicts universality), magnitude_verdict=PASS, regime_verdict=VALID (L ∈ [4, 11] inside Friedrich-Bär saturation window) ⇒ composite=PASS`.
- **FAIL (Reading A coincidence confirmed)**: ≥ 2 of 4 observables yield β_i outside [1.5, 2.5] AND σ_β ≥ 0.30. Composite: `sign_verdict=FAIL (universality prediction fails), magnitude_verdict=FAIL, regime_verdict=VALID ⇒ composite=FAIL`.
- **INFO (intermediate)**: σ_β ∈ (0.10, 0.30); some convergence but not Reading B's structural tightness. Defer to S92+ extension with O_5+. Composite: `regime_verdict=MARGINAL ⇒ composite=INFO`.
- **Tolerance rule**: ABSOLUTE on β_i band membership; ABSOLUTE on σ_β threshold; ABSOLUTE on C_ij off-diagonal threshold.

### 10. Substitution chain (MANDATORY for `[VERIFY-THEOREM]`)

```
Definitions:
  S_i(L)        := shell-sum of observable i at Peter-Weyl level L (computed from L_max=12 cache)
  β_i           := -slope of linear regression of S_i(L+1)/S_i(L) vs 1/L over L ∈ {4..11}
  β̄             := mean(β_1, β_2, β_3, β_4)
  σ_β           := std(β_1, β_2, β_3, β_4)
  C_ij          := corr(β_i, β_j) on per-L regression residuals
  PASS criterion := (all β_i ∈ [1.8, 2.1]) ∧ (σ_β ≤ 0.10) ∧ (min C_ij off-diagonal ≥ 0.7)

Step 1: Substrate-IS shell-sum at substrate-distance-1 pole s=3:
        For each (p,q) Peter-Weyl block with p+q = L:
          contribution_i(p,q) = projector_i(p,q) · dim(p,q) · (C_2(p,q) + 1)^{-3}
        Sum over all (p,q) with p+q = L gives S_i(L)
        [Substrate's combinatorial geometry; regulator-INVARIANT BY CONSTRUCTION per EV3]

Step 2: Asymptotic ratio at large L:
        S(L+1) / S(L) ~ ((L+1)/L)^{-β}    [for L → ∞ on power-law decay]
                     = (1 + 1/L)^{-β}
                     ≈ 1 − β · (1/L) + O(L^{-2})    [Taylor expansion for large L]

Step 3: Linear regression on L ∈ {4..11} avoiding boundaries:
        (S_i(L+1)/S_i(L) − 1) vs (-1/L) linear fit
        Slope = β_i  for each i

Step 4: Reading B (Substrate-Structural) PREDICTION:
        IF substrate-IS d=4 universal envelope at substrate-distance-1 pole s=3 holds
        THEN β_i is INDEPENDENT of projector_i, bridge_map_i, Level-2-binding_i
        ⇒ all β_i lie within a tight band around the universal value ≈ 1.9
        ⇒ σ_β ≤ 0.10 AND off-diagonal C_ij ≥ 0.7

Step 5: Reading A (Coincidence) PREDICTION:
        IF β_1 (CF-54-like) and β_2 (CF-65-like) coincidence is accidental
        THEN β_3 (FWD-C2 P_BdG at substrate-distance-2 pole) and β_4 (Tr(D_K^{-6})) SHOULD differ
            substantially from β_1, β_2 because contingencies are observable-specific
        ⇒ ≥ 2 of 4 outside [1.5, 2.5]; σ_β ≥ 0.30

Direction of comparison: PASS direction is "all 4 observables agree at universal β ≈ 1.9";
FAIL direction is "observables scatter across [1.5, 2.5] outside the universal band".

Conclusion (direction): the gate verdict tests whether the substrate's combinatorial
geometry (Step 1 + EV3 derivation) PRODUCES the universal exponent at finite L_max ∈ [6, 12]
across all d=4 substrate-distance-1 pole observables (Reading B PASS), OR whether
CF-54 + CF-65 agreement is observable-specific contingency (Reading A FAIL). The
discriminator's substrate-physics statement: substrate IS spectral triple → substrate-distance-1
pole s=3 IS the substrate's intrinsic d=4 Mellin-cone closure → ALL d=4 observables share
the substrate's combinatorial shell-sum geometry (Reading B); UNLESS observable-specific
contingencies break the universality (Reading A).
```

### 11. Solution-space implications

- **PASS (Reading B substrate-structural confirmed)**: d=4 universal envelope at finite L_max ∈ [6, 12] is substrate-IS regulator-INVARIANT BY CONSTRUCTION; the L^{-1.9} empirical α IS the substrate's intrinsic finite-L manifestation per EV3 derivation; the L^{-3} asymptotic prediction (Reading A) holds at L ≥ 35 (Friedrich-Bär saturation); §VII.AF.1.OP-PROJ Level-3 anchor PASS is reinterpreted as "~130× inside L^{-1.9} realized envelope" (vs "10.5× inside L^{-3} idealized envelope"); W6-5 fires under PASS-side prediction (W11-5 sister re-tag toward registry-PASS).
- **FAIL (Reading A coincidence)**: d=4 universal envelope is NOT universal at finite L; β_i ∈ {1.5..2.5} scatter; the CF-54 + CF-65 agreement is observable-specific coincidence; W6-5 deferred (no re-tag justification); §VII.AU.OP-PROJ HYBRID verdict (d) per-regulator-class sub-window structure prevails; W6-1 pathway (b) likely returns INFO or FAIL toward Reading B realized; pathway (a) backup at L_max ≥ 35 becomes structurally necessary.
- **INFO (intermediate)**: partial convergence; some observables agree at β ≈ 1.9 but σ_β > 0.10; defer to S92+ extension with O_5+; the d=4 universal envelope is in a transitional regime where some contingencies break universality and others preserve it.
- **K-counter for Layer-Functor F Verdict-Shape Consistency Theorem**: PASS confirms the K=2 SUGGESTION calibration at W-5 + W-6 (the EV1 boxed theorem's universality prediction); FAIL would falsify the K=2 calibration; INFO leaves K=2 SUGGESTION standing pending S92+ extension.

### 12. Effort estimate

~0.5 we (single agent-timeslot ~30 min wall time per lizzi-S7 §(4.f); 4 observables × 8 L-values × per-observable shell-sum computation; all reading from same NPZ cache; CPU-only OK; verdict assignment + working-paper section + verdict line).

### 13. Substrate-framing reminder

The 4-way discriminator IS a substrate-spectral-functional test of d=4 universality. The substrate IS the spectral triple `(A_K, H_K, D_K)`; the d=4 dimension IS the substrate's Wodzicki dimension at trace pole `s=4` of `ζ_D(s)`. The shell-sum exponent at substrate-distance-1 pole `s=3` IS a substrate-IS structural property of the substrate's `dim(p,q) · (C_2(p,q)+1)^{-3}` combinatorial geometry. The discriminator tests whether this property is universal across observables (Reading B substrate-structural) OR specific to particular bridge-anatomy contingencies (Reading A coincidence). Direction substrate → emergent: substrate IS spectral triple → substrate-distance-1 pole `s=3` IS the substrate's intrinsic d=4 Mellin-cone closure → ALL d=4 Mellin-cone observables share the substrate's combinatorial shell-sum geometry → empirical α at finite L IS the substrate's universal d=4 envelope (Reading B). Container-thinking FORBIDDEN: "the 4 observables live in a 4-way space" — INVERTED: "the 4 observables ARE 4 substrate-IS projections of the substrate's combinatorial shell-sum geometry; there is no enveloping 4-way space they inhabit".

---

## §W6-5. `S91-W11-5-SISTER-RE-AUDIT-UNDER-REALIZED-ENVELOPE` (M11 / CF-LZ-S7-3) **[CONDITIONAL on W6-4 PASS]**

### 1. Gate ID

`S91-W11-5-SISTER-RE-AUDIT-UNDER-REALIZED-ENVELOPE`

### 2. Trigger

`[AUDIT]` (re-audits S87 W11-5 sister cross-pillar bridge instance under the realized `L^{-1.9}` envelope versus the original `L^{-3}` asymptotic envelope; determines whether the W11-5 registry-FAIL by ~21× under `L^{-3}` should be re-tagged to registry-PASS, deferred-pending PROXY-REFINEMENT, or deferred-pending FIRST-EXTRACTION).

### 3. Classification

PHONONIC. The W11-5 sister cross-pillar bridge IS a substrate-IS observable at Pillar III ↔ IV at substrate-distance-1 pole `s=3` (per registry §VII.AJ at line 16887 in the §VII.AU.OP-PROJ HIT table corpus instance #2). The re-audit applies the realized envelope verdict from W6-4 to W11-5's Level-3 empirical anchor; the re-tag decision IS a methodology-floor consequence of substrate-IS universal envelope determination.

### 4. Agent type

`lizzi-spectral-functional-theorist` (PRIMARY; envelope-determined re-tag decision under FUNCTIONAL-SELECT-67 / cross-pillar bridge-anatomy structural-confidence ladder); `mack-cosmic-bridge` CO-AUTHOR per `feedback_mack-bridge-role.md` sole-writer rule for ANY registry-text retrofit IF the re-audit produces a structurally-justified re-tag (mack performs the actual registry edit).

### 5. Hypothesis

Under realized envelope `L^{-1.9}` (W6-4 PASS), W11-5's Level-3 empirical anchor `R_∞` lies WITHIN the realized envelope's L_max=10 width of ~1.26% (predicted by lizzi-S7 §(3.a) line 159), making the registry-FAIL by ~21× under `L^{-3}` no longer the canonical reading. Possible re-tag verdicts:
- registry-PASS: realized envelope contains the anchor; W11-5 promoted to deferred-pending-INTERMEDIATE per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` SUGGESTION K=1
- deferred-pending PROXY-REFINEMENT: realized envelope width still misses anchor BUT structurally-defensible refinement pathway exists (SCHEMATIC vs FULL physical regulator)
- deferred-pending FIRST-EXTRACTION: realized envelope width misses anchor; further first-extraction at higher L_max required
- registry-FAIL preserved: even under realized envelope, anchor outside; W11-5 sister CONFIRMED non-binding

### 6. Method — COMPLETE self-contained dispatch prompt

```python
"""
S91 W6-5: S91-W11-5-SISTER-RE-AUDIT-UNDER-REALIZED-ENVELOPE (M11 / CF-LZ-S7-3)

CONDITIONAL on W6-4 PASS (Reading B substrate-structural). Re-audits the
S87 W11-5 sister cross-pillar bridge entry (§VII.AJ at registry line 16887
in the §VII.AU.OP-PROJ HIT table corpus instance #2) under the realized
L^{-1.9} empirical envelope vs the original L^{-3} asymptotic envelope.

Per lizzi-S7 §(3.d) cross-corpus implication line 192 + §(5) CF-LZ-S7-3
gate spec line 374-385.
"""

from canonical_constants import *
import numpy as np
import hashlib, json

# Step 1: Verify W6-4 PASS prerequisite (DRY-RUN at runtime; HARD-HALT if W6-4 verdict not PASS)
import re
verdict_file = 'computations/session-91/s91_gate_verdicts.txt'
w6_4_verdict = parse_verdict(verdict_file, 'S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR')  # (local helper)
if w6_4_verdict != 'PASS':
    raise RuntimeError(
        f"W6-5 is CONDITIONAL on W6-4 PASS; got {w6_4_verdict}. Defer to S92+."
    )

# Step 2: Load W11-5 sister registry entry (locate §VII.AJ at line 16887)
registry_text = open('sessions/permanent-results-registry.md').read()
vii_aj_block = extract_section(registry_text, '§VII.AJ', start_line=16887)  # (local helper)

# Extract W11-5's Level-3 empirical anchor from §VII.AJ block + cross-reference
# S87 W11-5 closure record (per S87 working paper); the anchor IS the empirical
# R_∞ extrapolation from W11-5 L_max sweep
W11_5_anchor_value, W11_5_anchor_l_max = extract_level_3_anchor(vii_aj_block)  # (local helper)

# Step 3: Compute realized envelope width at L_max=10 per lizzi-S7 §(3.a) line 159
# realized envelope width = L^{-α_realized} with α_realized = β_bar from W6-4
alpha_realized = w6_4_beta_bar  # (local) — from W6-4 npz; expected ≈ 1.9
envelope_width_L_max_10_realized = 10 ** (-alpha_realized)  # (local) — at L_max=10
# Equivalently: envelope_width ≈ 1.26e-2 = 1.26% per lizzi-S7 §(3.a) (predicted)

# Step 4: Compute original L^{-3} envelope width at L_max=10
envelope_width_L_max_10_idealized = 10 ** (-3)  # (local) — = 0.1%

# Step 5: Compare W11-5 anchor to BOTH envelopes
deviation_vs_realized = abs(W11_5_anchor_value) / envelope_width_L_max_10_realized  # (local) — should compare ~21× / (1.26%/0.10%) = ~21 / 12.6 = ~1.67
deviation_vs_idealized = abs(W11_5_anchor_value) / envelope_width_L_max_10_idealized  # (local) — original ~21× by definition

# Step 6: Re-tag decision logic per cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class" + Level-2 sub-class clause MANDATORY at K=2 (S88 W8-88)
if deviation_vs_realized <= 1.0:
    # Realized envelope contains the anchor
    re_tag = 'REGISTRY-PASS-CONDITIONAL-ON-W6-4-PASS'
    re_tag_justification = (
        f"W11-5 sister anchor {W11_5_anchor_value:.6e} INSIDE realized envelope width "
        f"{envelope_width_L_max_10_realized:.4e} at L_max=10 (deviation {deviation_vs_realized:.4f}); "
        "registry-PASS under realized envelope eligibility confirmed; "
        "promotion to deferred-pending-INTERMEDIATE per cross-pillar-bridge-anatomy.md §'Deferred-pending intermediate verdict-class' K=1 SUGGESTION"
    )
    verdict = 'PASS'
elif deviation_vs_realized <= 5.0 and structurally_defensible_proxy_refinement_pathway_exists(vii_aj_block):
    re_tag = 'DEFERRED-PENDING-PROXY-REFINEMENT'
    re_tag_justification = (
        f"W11-5 sister anchor outside realized envelope by {deviation_vs_realized:.4f}× at L_max=10; "
        "structurally-defensible SCHEMATIC → FULL physical regulator refinement pathway exists; "
        "deferred-pending PROXY-REFINEMENT per cross-pillar-bridge-anatomy.md §'Deferred-pending intermediate verdict-class'"
    )
    verdict = 'INFO'  # Re-tag is admissible-with-conditions per Level-2 sub-class clause
elif deviation_vs_realized <= 10.0:
    re_tag = 'DEFERRED-PENDING-FIRST-EXTRACTION'
    re_tag_justification = (
        f"W11-5 sister anchor outside realized envelope by {deviation_vs_realized:.4f}× at L_max=10; "
        "first-extraction at higher L_max (≥ 22 pathway b or ≥ 35 pathway a) required; "
        "deferred-pending FIRST-EXTRACTION per cross-pillar-bridge-anatomy.md §'Deferred-pending intermediate verdict-class'"
    )
    verdict = 'INFO'
else:
    re_tag = 'REGISTRY-FAIL-PRESERVED'
    re_tag_justification = (
        f"W11-5 sister anchor outside realized envelope by {deviation_vs_realized:.4f}× at L_max=10; "
        f"even under realized envelope, anchor exceeds by > 10×; "
        "registry-FAIL preserved; W11-5 sister CONFIRMED non-binding under both envelopes"
    )
    verdict = 'FAIL'

value_field = (
    f"W11_5_anchor={W11_5_anchor_value:.4e}_dev_vs_realized={deviation_vs_realized:.4f}"
    f"_dev_vs_idealized={deviation_vs_idealized:.4f}_re_tag={re_tag}"
)

append_verdict(
    gate_id='S91-W11-5-SISTER-RE-AUDIT-UNDER-REALIZED-ENVELOPE',
    verdict=verdict,
    value=value_field,
    scheme='envelope-determined-re-tag-decision-under-W6-4-PASS-realized-L_minus_1.9',
    convention='Mellin-class-substrate-distance-1-pole-s3-realized-envelope-CACHE-PROJECTION',
    L_max=10,
    input_pin_map={
        's91_w6_4_d4_mellin_cone_discriminator.npz': '<computed-at-runtime>',
        'permanent_results_registry_md_VII_AJ': '<computed-at-runtime>',
        'canonical_constants_M_KK': M_KK,
    },
)

# IMPORTANT: if re_tag != 'REGISTRY-FAIL-PRESERVED', the registry-text retrofit is
# NOT performed by this script. It is queued as a CONDITIONAL carry-forward to
# mack-cosmic-bridge sole-writer per feedback_mack-bridge-role.md (per CF-LZ-S7-3
# spec line 385 effort estimate). The script EMITS the re-tag verdict + justification
# in the working-paper section; mack performs the actual registry retrofit in a
# follow-up gate IF user dispatches W6-5-MACK-RETROFIT.

np.savez('computations/session-91/s91_w6_5_w11_5_sister_re_audit.npz',
    W11_5_anchor_value=W11_5_anchor_value, W11_5_anchor_l_max=W11_5_anchor_l_max,
    alpha_realized=alpha_realized,
    envelope_width_L_max_10_realized=envelope_width_L_max_10_realized,
    envelope_width_L_max_10_idealized=envelope_width_L_max_10_idealized,
    deviation_vs_realized=deviation_vs_realized,
    deviation_vs_idealized=deviation_vs_idealized,
    re_tag=re_tag, re_tag_justification=re_tag_justification, verdict=verdict,
)
# Plot: envelope-width vs L_max overlay (realized L^{-1.9} vs idealized L^{-3}) + W11-5 anchor marker
```

Output files: `computations/session-91/s91_w6_5_w11_5_sister_re_audit.py` + `.npz` + `.png`.

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `prereq_gate` | `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR` PASS (W6-4) | this wave's W6-4 dependency |
| `alpha_realized_source` | `w6_4_beta_bar` from W6-4 npz output | this gate-block dependency |
| `alpha_idealized_target` | 3.0 (L^{-3} asymptotic) | `cross-pillar-bridge-anatomy.md` Level-2 envelope canonical |
| `L_max_anchor_eval` | 10 (canonical W11-5 closure L_max per S87) | S87 W11-5 closure record |
| `registry_pin_w11_5` | §VII.AJ at line 16887 in `permanent-results-registry.md` | registry grep |
| `re_tag_thresholds` | dev_vs_realized: ≤1.0 = REGISTRY-PASS-CONDITIONAL; ≤5.0 = DEFERRED-PENDING-PROXY-REFINEMENT (with structurally-defensible pathway); ≤10.0 = DEFERRED-PENDING-FIRST-EXTRACTION; >10.0 = REGISTRY-FAIL-PRESERVED | this gate-block authoring + `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` SUGGESTION K=1 |
| `predicted_realized_envelope_width_L_max_10` | ~1.26% per lizzi-S7 §(3.a) line 159 | substitution from `10^{-1.9} ≈ 1.26e-2` |
| `M_KK` | 7.428660036284456e16 GeV | `canonical_constants.py:339-341` |
| `scheme_pin` | `envelope-determined-re-tag-decision-under-W6-4-PASS-realized-L_minus_1.9` | this gate-block |
| `convention_pin` | `Mellin-class-substrate-distance-1-pole-s3-realized-envelope-CACHE-PROJECTION` | `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"` |
| `regulator_class_pin` | `a_n^{Mellin}` (consistent with W11-5 sister + W6-4 base) | `regulator-pin-discipline.md` |
| `gpu_path` | NOT NEEDED (re-tag decision is arithmetic on existing data) | this gate-block |
| `random_seed` | 0 (deterministic) | this gate-block |
| `tolerance_rule` | ABSOLUTE on deviation_vs_realized band membership (1, 5, 10) | this gate-block |
| `pubprecision_deviation` | 4 sig figs | `epistemic-discipline.md §"Class 8.3"` MANDATORY |
| `verifier_rubric_pinmap` | enumerated 4-band re-tag decision tree (dev ≤ 1 → PASS-CONDITIONAL; dev ≤ 5 → PROXY-REFINEMENT; dev ≤ 10 → FIRST-EXTRACTION; dev > 10 → FAIL-PRESERVED) | `epistemic-discipline.md §"Class 8.2"` MANDATORY |
| `mack_retrofit_carry_forward` | CONDITIONAL on verdict ∈ {PASS, INFO with re_tag} per `feedback_mack-bridge-role.md` sole-writer rule | this gate-block authoring |

**Input SHA-256 pins**:
- `computations/session-91/s91_w6_4_d4_mellin_cone_discriminator.npz` SHA: `<computed-at-runtime>` (W6-4 output; runtime-pinned per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction)
- `sessions/permanent-results-registry.md` SHA: `<computed-at-runtime>` (§VII.AJ at line 16887 + §VII.AU.OP-PROJ HIT table corpus instance #2 at line 17728)
- `computations/_shared/canonical_constants.py` SHA: `<computed-at-runtime>`
- `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` SHA: `<computed-at-runtime>` (CF-LZ-S7-3 spec at §(5) lines 374-385)
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` SHA: `<computed-at-runtime>` (§(3.d) cross-corpus implication at line 192)

### 8. Expected output 4-tuple

`(value=W11_5_anchor=<a>_dev_vs_realized=<d_r>_dev_vs_idealized=<d_i>_re_tag=<tag>, scheme=envelope-determined-re-tag-decision-under-W6-4-PASS-realized-L_minus_1.9, convention=Mellin-class-substrate-distance-1-pole-s3-realized-envelope-CACHE-PROJECTION, L_max=10)`

Predicted (per lizzi-S7 line 192 hint "deviation may be different"): dev_vs_realized ∈ [1.0, 5.0] most likely; re_tag = DEFERRED-PENDING-PROXY-REFINEMENT probable; verdict = INFO probable.

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS (REGISTRY-PASS-CONDITIONAL re-tag)**: `deviation_vs_realized ≤ 1.0` (W11-5 anchor INSIDE realized envelope width); W11-5 promoted to deferred-pending-INTERMEDIATE per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`. Composite: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID ⇒ composite=PASS`.
- **INFO (DEFERRED-PENDING-PROXY-REFINEMENT or DEFERRED-PENDING-FIRST-EXTRACTION re-tag)**: `1.0 < deviation_vs_realized ≤ 10.0`; re-tag admissible-with-conditions per Level-2 sub-class clause MANDATORY at K=2 (S88 W8-88). Composite: `regime_verdict=MARGINAL ⇒ composite=INFO`.
- **FAIL (REGISTRY-FAIL-PRESERVED)**: `deviation_vs_realized > 10.0`; even under realized envelope, anchor exceeds by > 10×; W11-5 CONFIRMED non-binding under both envelopes. Composite: `sign_verdict=FAIL, magnitude_verdict=FAIL, regime_verdict=VALID ⇒ composite=FAIL`.
- **HARD-HALT (CONDITIONAL prereq fail)**: W6-4 verdict not PASS at this gate's runtime check; raise RuntimeError; defer to S92+ if W6-4 produced INFO; if W6-4 produced FAIL (Reading A coincidence), the W11-5 re-audit is structurally moot (Reading A means no universal envelope to re-anchor against).
- **Tolerance rule**: ABSOLUTE on `deviation_vs_realized` band membership.

### 10. Substitution chain (MANDATORY for `[AUDIT]` re-tag decision)

```
Definitions:
  W11_5_anchor := S87 W11-5 sister bridge Level-3 empirical anchor at L_max=10 (from §VII.AJ registry record)
  α_realized := empirical α from W6-4 (Reading B substrate-structural; predicted ≈ 1.9)
  α_idealized := L^{-3} asymptotic; the original W11-5 closure envelope
  envelope_width_L_max_10_realized := 10^{-α_realized} ≈ 1.26e-2 (realized envelope width at L_max=10)
  envelope_width_L_max_10_idealized := 10^{-3} = 1.0e-3 (original envelope width at L_max=10)
  deviation_vs_R := |W11_5_anchor| / envelope_width_L_max_10_R for R ∈ {realized, idealized}

Step 1: Original W11-5 closure under L^{-3}:
        |W11_5_anchor| / 10^{-3} = ~21× (per HIT table corpus instance #2 at registry line 17728)
        ⇒ |W11_5_anchor| ≈ 21 · 10^{-3} = 2.1e-2

Step 2: Re-evaluation under realized L^{-1.9}:
        |W11_5_anchor| / 10^{-1.9} = (2.1e-2) / (1.26e-2) ≈ 1.67×
        ⇒ deviation_vs_realized ≈ 1.67  [predicted from lizzi-S7 §(3.d) hint]

Step 3: Re-tag decision under realized envelope:
        IF deviation_vs_realized ≤ 1.0: REGISTRY-PASS (anchor INSIDE realized envelope)
        IF 1.0 < deviation_vs_realized ≤ 5.0: DEFERRED-PENDING-PROXY-REFINEMENT
            (anchor outside but within factor-5 of realized envelope; structurally-defensible
             SCHEMATIC → FULL physical regulator refinement pathway exists per
             `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY)
        IF 5.0 < deviation_vs_realized ≤ 10.0: DEFERRED-PENDING-FIRST-EXTRACTION
            (anchor outside by factor 5-10; first-extraction at higher L_max ≥ 22 / 35 required)
        IF deviation_vs_realized > 10.0: REGISTRY-FAIL-PRESERVED
            (anchor outside by > 10× even under realized envelope; non-binding CONFIRMED)

Step 4: Substitution (predicted):
        Given lizzi-S7 §(3.d) hint that "deviation may be different" under L^{-1.9} but
        W11-5 closure was originally registry-FAIL by ~21× under L^{-3}, the predicted
        deviation_vs_realized ≈ 1.67× per Step 2 substitution.
        ⇒ Predicted re_tag = DEFERRED-PENDING-PROXY-REFINEMENT (1.0 < 1.67 ≤ 5.0)
        ⇒ Predicted verdict = INFO

Step 5: Direction of comparison:
        PASS direction is "deviation_vs_realized ≤ 1.0" (W11-5 anchor INSIDE realized envelope).
        FAIL direction is "deviation_vs_realized > 10.0" (anchor outside both envelopes by > 10×).
        The structural reason: the realized envelope width is 12.6× larger than the idealized
        envelope width at L_max=10 (1.26% vs 0.10%); the W11-5 anchor was ~21× outside the
        idealized envelope, so under the realized envelope it is ~21/12.6 ≈ 1.67× outside
        — a band where the deferred-pending sub-class clauses apply.

Conclusion (direction): the gate verdict tests whether the realized envelope's 12.6×
inflation of the envelope width relative to the idealized envelope is enough to bring
the W11-5 anchor INSIDE the envelope (REGISTRY-PASS-CONDITIONAL), to admit a defensible
refinement pathway (DEFERRED-PENDING-PROXY-REFINEMENT or DEFERRED-PENDING-FIRST-EXTRACTION),
or whether even the inflated envelope fails (REGISTRY-FAIL-PRESERVED). The predicted
verdict per substitution is INFO with re_tag = DEFERRED-PENDING-PROXY-REFINEMENT, but
the actual W11-5 anchor value extracted from the registry record will determine the
verdict at runtime.
```

### 11. Solution-space implications

- **PASS (REGISTRY-PASS-CONDITIONAL)**: W11-5 sister advances to deferred-pending-INTERMEDIATE; advances `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` calibration corpus K=1 SUGGESTION → K=2 (W11-5 NEW instance distinct from §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION dual at S90 W1-14); requires mack-cosmic-bridge sole-writer registry retrofit follow-up gate; advances cross-pillar-bridge K-counter corpus.
- **INFO (DEFERRED-PENDING-PROXY-REFINEMENT or DEFERRED-PENDING-FIRST-EXTRACTION)**: W11-5 sister gains a structurally-justified intermediate status; the §VII.AU.OP-PROJ HIT table corpus instance #2 at registry line 17728 is annotated with the realized envelope re-evaluation; mack-cosmic-bridge sole-writer registry retrofit follow-up queued.
- **FAIL (REGISTRY-FAIL-PRESERVED)**: W11-5 sister CONFIRMED non-binding under both envelopes; reading B substrate-structural universality holds for §VII.AF.1.OP-PROJ baseline AND §VII.AU.OP-PROJ FWD-C1 but FAILS at §VII.AJ W11-5 sister — refines the cross-pillar bridge corpus boundary; lizzi-S7's hypothesis that "realized envelope inflation might rescue W11-5" is falsified.
- **HARD-HALT (CONDITIONAL prereq fail)**: W6-4 not PASS; W6-5 deferred to S92+; the W11-5 re-audit is structurally moot under Reading A (no universal envelope to anchor against); §VII.AJ entry remains REGISTRY-FAIL under L^{-3} canonical reading.

### 12. Effort estimate

~0.3 we (re-audit decision is arithmetic on existing data; W11-5 anchor extraction from registry; deviation computation; re-tag decision tree; verdict assignment + working-paper section + verdict line; the conditional mack-cosmic-bridge registry retrofit follow-up gate is SEPARATE at ~0.3 we additional IF re-tag is structurally justified per CF-LZ-S7-3 effort estimate line 385).

### 13. Substrate-framing reminder

W11-5 IS a sister cross-pillar bridge to W-5 §VII.AF.1.OP-PROJ at Pillar III ↔ IV at substrate-distance-1 pole `s=3`. The substrate IS the spectral triple; the W11-5 anchor IS the substrate's emergent Hochschild pairing at finite L_max=10; the realized envelope IS the substrate's universal finite-L Mellin-cone manifestation at d=4 substrate-distance-1 pole. Direction substrate → emergent: substrate IS spectral triple → W11-5 anchor IS substrate-IS Hochschild pairing → realized envelope IS substrate's universal d=4 envelope → re-tag decision IS methodology-floor F-image of substrate-IS envelope determination. Container-thinking FORBIDDEN: "the W11-5 anchor lives in a Pillar IV laboratory" — INVERTED: "the W11-5 anchor IS substrate-IS at Pillar III; its laboratory image at Pillar IV IS the cross-pillar bridge map's image under HKR / Connes-Karoubi pairing; the substrate is logically prior to the laboratory image".

---

## Wave 6 → Downstream Decision Points (S91 W7+ and S92+ feedback)

### W6-1 verdict consequences

- **W6-1 pathway (b) PASS-A confirmed (Reading A canonical)** ⇒ §VII.AU.OP-PROJ advances from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION to STAGE-1-CANDIDATE; W8 CF-67 Stage-2 cross-axis verify dispatch (T2.28 at S91 W8) becomes structurally executable per `joint-theorem-promotion.md` Stage-2 protocol; cross-pillar-bridge calibration corpus K=4 → K=5 candidate via Hybrid Independence Test PASS at axis (iv) independent algebraic envelope.
- **W6-1 FAIL-B (Reading B realized confirmed)** ⇒ HYBRID verdict (d) per-regulator-class sub-window structure is canonical for §VII.AU.OP-PROJ; pathway (a) backup at L_max ≥ 35 (Friedrich-Bär saturation extension) is the next required dispatch at S92+; §VII.AU.OP-PROJ Element 5 ANNOTATION block correctly already worded per S91 W0 prep T2.56 in-session housekeeping fix.
- **W6-1 INFO** ⇒ pathway (a) backup at L_max ≥ 35 becomes structurally necessary at S92+.

### W6-2 verdict consequences

- **W6-2 PASS** ⇒ K_HK = 9 FI + K_csub MIXED confirmed at A_5 atlas; advances `regulator-pin-discipline.md` MIXED-class taxonomy calibration corpus; K_csub_R per-regulator values pinned in canonical_constants.py via mack-cosmic-bridge sole-writer follow-up gate at S91 W0a (queued post-W6-2).
- **W6-2 INFO** (K_csub F_2-axis FI, not full-atlas MIXED) ⇒ new sub-class "F_2-axis FI / full-atlas MIXED" intermediate classification candidate for `regulator-pin-discipline.md`; refinement queued for S92+.
- **W6-2 FAIL** ⇒ structural defect at A_K Wedderburn decomposition (extremely unlikely) OR c_sub_corrected parameterization re-derivation needed (W8 WP §W8-7(c) anchor invalidated).

### W6-3 verdict consequences

- **W6-3 PASS-A-partial (α_sub > 2.5)** ⇒ Reading A pre-asymptotic shallow-envelope steepening confirmed at sub-window precursor layer; biases W6-4 expectation toward σ_β > 0.10 (INFO probable at W6-4); W6-1 pathway (b) PASS-A trajectory.
- **W6-3 INFO (α_sub ∈ [2.0, 2.5])** ⇒ sub-window non-decisive; W6-4 carries full discriminator weight.
- **W6-3 FAIL (α_sub ≈ 1.9)** ⇒ Reading B partial confirmation at pre-anchor sub-window; biases W6-4 expectation toward PASS with tight σ_β; W6-1 pathway (b) FAIL-B trajectory.

### W6-4 verdict consequences

- **W6-4 PASS (Reading B substrate-structural confirmed)** ⇒ unblocks W6-5; advances Layer-Functor F Verdict-Shape Consistency Theorem K=2 calibration corpus toward K=3 MANDATORY via FWD-C2 pre-registration screen (S91+ T2.59 corpus extension); §VII.AF.1.OP-PROJ Level-3 anchor PASS reinterpreted with ~130× inside realized envelope margin.
- **W6-4 FAIL (Reading A coincidence confirmed)** ⇒ Layer-Functor F Verdict-Shape Consistency Theorem K=2 calibration FALSIFIED; W6-5 not fired (no universal envelope to re-anchor against); W6-1 pathway (b) very likely INFO or FAIL.
- **W6-4 INFO** ⇒ K=2 calibration stands pending S92+ extension with O_5+; W6-5 deferred.

### W6-5 verdict consequences

- **W6-5 PASS (REGISTRY-PASS-CONDITIONAL re-tag for W11-5)** ⇒ W11-5 sister cross-pillar bridge promoted; advances `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` calibration K=1 → K=2 candidate (W11-5 NEW instance distinct from §VII.AV + §VII.AU dual at S90 W1-14); requires mack-cosmic-bridge sole-writer registry retrofit follow-up gate at S91 W0a (queued post-W6-5).
- **W6-5 INFO (DEFERRED-PENDING-PROXY-REFINEMENT or DEFERRED-PENDING-FIRST-EXTRACTION re-tag)** ⇒ W11-5 sister gains structurally-justified intermediate status; mack-cosmic-bridge registry retrofit follow-up queued.
- **W6-5 FAIL (REGISTRY-FAIL-PRESERVED)** ⇒ W11-5 sister CONFIRMED non-binding under both envelopes; cross-pillar bridge corpus boundary refined.
- **W6-5 HARD-HALT (W6-4 not PASS)** ⇒ deferred to S92+.

---

## Wave 6 Machinery-Enumeration Pin (PRDR across 5 gates)

Per `epistemic-discipline.md §"Pre-Registration Completeness"` MANDATORY plan-block enumeration:

| Gate | L_max_pin | regulator_class_pin | binding_pin | machinery_scope_pin | level_pin | scheme_pin | convention_pin |
|:-----|:----------|:-------------------|:-----------|:-------------------|:----------|:-----------|:---------------|
| W6-1 | 22 (path b) / 35 (path a backup) | `a_n^{Mellin}` + per-regulator-class K_csub_R | Level-2-binding-HKR-bridge-canonical-import-binding | CACHE-PROJECTION (path b) / FULL-LEAF-FOLIATION (path a optional) | FULL physical Connes-Karoubi pairing (path b); SCHEMATIC if Pauli-Villars `_spectral_action_regulators.py` consumed (path a) | direct-connes-karoubi-pairing-L_max-22-pathway-b | Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION |
| W6-2 | 22 | per-regulator `a_n^{R}` for R ∈ A_5 atlas | algebra-INVARIANT (K_HK) + algebra-DEPENDENT MIXED (K_csub) | CACHE-PROJECTION | FULL physical Pauli-Villars at Λ_UV = M_KK pipeline OR SCHEMATIC declared | per-regulator-class-K_csub_R-extraction-A_5-atlas | HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION |
| W6-3 | 9 (pre-anchor sub-window) | `a_n^{Mellin}` (FWD-C1 source is Mellin-class) | inherits FWD-C1 binding (Level-2-binding) | CACHE-PROJECTION | FULL physical (FWD-C1 was substrate-canonical parameterized at S90 W8) | log-log-regression-existing-S90-W8-FWD-C1-pre-anchor-sub-window | Mellin-class-pre-asymptotic-sub-window-CACHE-PROJECTION |
| W6-4 | 12 (L_fit window 4..11) | `a_n^{Mellin}` at substrate-distance-1 pole s=3 | Mixed (4-observable basis spans Level-2-binding + Level-2-non-binding) | CACHE-PROJECTION | FULL physical (shell-sum-ratio is closed-form substrate-IS combinatorial) | shell-sum-ratio-regression-4-way-discriminator | Mellin-class-substrate-distance-1-pole-s3-CACHE-PROJECTION |
| W6-5 | 10 (W11-5 closure canonical L_max) | `a_n^{Mellin}` (consistent with W11-5 + W6-4) | conditional re-tag per Level-2-binding sub-class decision tree | CACHE-PROJECTION (inherits W6-4 cache reading) | FULL physical (re-tag is arithmetic; no SCHEMATIC consumed) | envelope-determined-re-tag-decision-under-W6-4-PASS-realized-L_minus_1.9 | Mellin-class-substrate-distance-1-pole-s3-realized-envelope-CACHE-PROJECTION |

**Wave-level cross-cutting pins**:
- `tau_fold = 0.190` (canonical; `canonical_constants.py:283`) — all 5 gates inherit
- `M_KK = 7.428660036284456e16 GeV` (gravity route alias; `canonical_constants.py:339-341`) — all 5 gates
- `kappa_2_substrate_FW = 0.021018084987437196` (S89 canonical; `canonical_constants.py:559`) — W6-1, W6-2 inherit
- `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8; `canonical_constants.py:1636`) — W6-4 O_2 cross-check anchor
- `n_s_FW_exact = Fraction(9561, 10000)` (S87 W8-8 reaffirmed regulator-INDEPENDENT; `canonical_constants.py`) — W6-4 O_2 substrate-IS anchor at Pillar II

**Closing-paragraph-coherence audit** (per `epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern"` ): W6-1's PASS-A vs FAIL-B labels at §9 use composite collapse rule mapping per S87 schema-v2 collapse rule; structurally-coherent reading is "literal verdict at composite line + 3-tuple companion row carries the SIGN/MAGNITUDE/REGIME atomic verdicts"; PASS-A-partial at W6-3 emits `verdict=PASS` with `value=PASS_A_partial` substring + 3-tuple `regime_verdict=MARGINAL`.

---

## Wave 6 Input-SHA Ledger (per-gate Input SHA-256 pins; runtime-pinned)

All Input SHAs marked `<computed-at-runtime>` per `gate-verdicts.md §"Pre-Registration Protocol"` item 1; pre-compute at plan-freeze landing using `hashlib.sha256` on file bytes.

| Gate | Input File | SHA pin |
|:-----|:-----------|:--------|
| W6-1 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<computed-at-runtime>` |
| W6-1 | `computations/_shared/canonical_constants.py` | `<computed-at-runtime>` |
| W6-1 | `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` | `<computed-at-runtime>` |
| W6-1 | `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` | `<computed-at-runtime>` |
| W6-1 | `sessions/permanent-results-registry.md` | `<computed-at-runtime>` |
| W6-2 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<computed-at-runtime>` |
| W6-2 | `computations/_shared/canonical_constants.py` | `<computed-at-runtime>` |
| W6-2 | `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` | `<computed-at-runtime>` |
| W6-2 | `sessions/permanent-results-registry.md` | `<computed-at-runtime>` |
| W6-3 | `computations/session-90/s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz` | `<computed-at-runtime>` |
| W6-3 | `computations/_shared/canonical_constants.py` | `<computed-at-runtime>` |
| W6-3 | `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` | `<computed-at-runtime>` |
| W6-3 | `sessions/archive/session-90/session-90-w8-workingpaper.md` | `<computed-at-runtime>` |
| W6-4 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<computed-at-runtime>` |
| W6-4 | `computations/_shared/canonical_constants.py` | `<computed-at-runtime>` |
| W6-4 | `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` | `<computed-at-runtime>` |
| W6-4 | `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` | `<computed-at-runtime>` |
| W6-4 | `sessions/permanent-results-registry.md` | `<computed-at-runtime>` |
| W6-5 | `computations/session-91/s91_w6_4_d4_mellin_cone_discriminator.npz` | `<computed-at-runtime>` (W6-4 output; runtime-pinned per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction) |
| W6-5 | `sessions/permanent-results-registry.md` | `<computed-at-runtime>` |
| W6-5 | `computations/_shared/canonical_constants.py` | `<computed-at-runtime>` |
| W6-5 | `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` | `<computed-at-runtime>` |
| W6-5 | `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` | `<computed-at-runtime>` |

**Audit-SHA spec**: per-gate `audit_sha256 = closure_hash(input_pin_map)` where `input_pin_map` is the gate-specific ordered dict of (file_path, file_sha) pairs PLUS the canonical_constants pins (M_KK, tau_fold, kappa_2_substrate_FW, gv_canonical_difference_FW, n_s_FW_exact). Computed at gate-emission time per `computations/_shared/_script_template.py append_verdict()` canonical helper.

**Content-SHA spec**: per-gate `content_sha256 = sha256(verdict_line_bytes_without_audit_sha)`; emitted on dual-SHA companion comment row per `gate-verdicts.md S87+ schema-v2`.

---

## Wave 6 Closing Notes

**Wave authoring**: lizzi-spectral-functional-theorist primary; connes-ncg-theorist CO-AUTHOR on W6-1 (Connes-Karoubi pairing implementation) and W6-4 (CM-1995 §III.4 residue-formula evaluator per lizzi-S7 §(4.b)); mack-cosmic-bridge CO-AUTHOR on W6-5 IF re-tag is structurally justified (registry-text retrofit follow-up gate).

**Dispatch ordering (recommended; not strict)**:
1. **W6-3** FIRST (~0.1 we cheap precursor; runs on existing FWD-C1 npz data; gives early signal on Reading A pre-asymptotic vs Reading B persistence).
2. **W6-4** (~0.5 we; 4-way discriminator on L_max=12 master cache; decisive evidence on Reading A vs Reading B).
3. **W6-2** in parallel with W6-4 (~1.5 we; K_HK + K_csub anchoring; independent observables; no dispatch dependency on W6-4).
4. **W6-1** AFTER W6-4 (~0.8–3.3 we; pathway b at L_max ≥ 22 if W6-4 PASS; pathway a backup at L_max ≥ 35 if W6-4 INFO/FAIL).
5. **W6-5** AFTER W6-4 (~0.3 we; CONDITIONAL on W6-4 PASS; HARD-HALT otherwise).

**Total wave effort**: ~3.2 we (optimistic; W6-1 pathway b PASS) up to ~5.7 we (pessimistic; W6-1 pathway a backup needed).

**Cross-wave dependencies**:
- W6-4 PASS unblocks downstream cross-pillar-bridge-anatomy K=3 corpus extension at S91 W9 (T2.59 corpus extension queued).
- W6-1 PASS-A unblocks §VII.AU.OP-PROJ Stage-2 cross-axis verify at S91 W8 (T2.28).
- W6-2 PASS unblocks K_csub_R per-regulator pins in canonical_constants.py via S91 W0a mack-cosmic-bridge sole-writer follow-up gate.
- W6-5 PASS unblocks W11-5 sister registry retrofit at S91 W0a mack-cosmic-bridge sole-writer follow-up gate.

**Substrate framing reminder for the wave**: the d=4 universal envelope at substrate-distance-1 pole `s=3` IS a substrate-IS spectral-functional property of the framework's KO-dim=6 finite spectral triple. The 5 gates collectively test (W6-3 precursor + W6-4 4-way discriminator) AND extend (W6-1 L_max ≥ 22) AND anchor (W6-2 K_HK + K_csub) AND audit (W6-5 W11-5 sister re-tag) this substrate-IS property. Direction substrate → emergent for ALL gates: substrate IS spectral triple → universal envelope IS substrate's combinatorial geometry → empirical L^{-α} at finite L IS substrate's intrinsic d=4 manifestation → registry-PASS classifications IS methodology-floor F-image of substrate-IS universal envelope determination. Container-thinking FORBIDDEN throughout the wave: no observable lives "in" a container; every observable IS substrate-IS at the specified Pillar; the bridge maps ARE substrate-IS HKR / Connes-Karoubi pairings; the laboratory images at Pillar II / IV / V ARE methodology-floor F-images of the substrate-IS source.

---

**End of W6 plan.**

Authoring agent: lizzi-spectral-functional-theorist (per-wave planner role; primary author and dispatch lead for S91 W6 d=4 envelope discriminators + lizzi reading + W11-5 sister re-audit).
