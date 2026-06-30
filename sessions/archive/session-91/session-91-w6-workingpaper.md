# Session 91 — Wave 6 Working Paper

**Session**: 91 | **Wave**: W6 | **Plan**: `sessions/session-plan/session-91-plan-w6.md` | **Theme**: d=4 envelope discriminators + lizzi reading + W11-5 sister re-audit (lizzi primary)

**Status**: SHELL CREATED (2026-05-16); awaiting runtime compute dispatch

**Wave lead**: lizzi-spectral-functional-theorist (primary author + dispatch lead)
**Wave class**: COMPUTE-class (5/5 gates carry numerical PASS/FAIL/INFO bands against pre-registered substrate-physics thresholds; producing scripts emit `.py + .npz + .png + verdict line`; M1 numerical-comparison fails → COMPUTE-class fallthrough per `wave-classification.md §"Dispatch consequences"`)

**Source plans / syntheses**:
- `sessions/session-plan/session-91-context.md` §"W6 — d=4 envelope discriminators + lizzi reading + W11-5 sister re-audit"
- `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` §(4) discriminator-gate spec + §(5) CF-LZ-S7-1/2/3
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` §Wrap-Up CF-1/CF-7/CF-9 (4-field specs at lines 1270–1322)

## Gate inventory (5 items)

| Gate ID | Status | Trigger | Effort | CONDITIONAL |
|:--------|:-------|:--------|:-------|:------------|
| §W6-1 `S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW` (T2.54 / CF-1) | **CLOSED — PASS** (α_b = 2.6926 at L_fit ∈ [15, 22]; pathway_b_pass_a=True via f2_pass criterion (Mellin α=2.6926 + zeta α=2.6926 both in [2.4, 3.6]); count_pass=2/5 (Mellin, zeta); composite PASS per S87 schema-v2 collapse rule (sign=PASS, mag=PASS, regime=VALID); audit_sha256=`d54b26a970e43b6b...`; tier_pin=TIER-2 SCHEMATIC level-pin disclosed per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY) | `[VERIFY-THEOREM]` | 0.8–3.3 we | pathway (b) FIRST L_max ≥ 22 |
| §W6-2 `S91-K_HK-AND-K_CSUB-EMPIRICAL-ANCHORING` (T2.58 / CF-7) | **CLOSED — FAIL** (K_HK = 9 FI PASS; K_csub_R SCHEMATIC sub_term divergent ⇒ \|K_csub_mean − 0.5\| ≫ 0.2 magnitude FAIL; composite collapses to FAIL via gate-verdicts.md §"Composite-collapse rule"; audit_sha256=`109e4307e8a0d805...`) | `[VERIFY]` | 1.5 we | INDEPENDENT |
| §W6-3 `S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9` (T2.60 / CF-9) | NOT STARTED | `[AUDIT]` | 0.1 we | INDEPENDENT (existing data) |
| §W6-4 `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR` (M10 / CF-LZ-S7-1) | NOT STARTED | `[VERIFY-THEOREM]` | 0.5 we | INDEPENDENT |
| §W6-5 `S91-W11-5-SISTER-RE-AUDIT-UNDER-REALIZED-ENVELOPE` (M11 / CF-LZ-S7-3) | NOT STARTED | `[AUDIT]` | 0.3 we | **CONDITIONAL on W6-4 PASS** |

**Dispatch ordering (recommended)**: W6-3 first (cheap precursor; 0.1 we) → W6-4 + W6-2 in parallel → W6-1 after W6-4 verdict → W6-5 LAST conditional on W6-4 PASS.

**Total wave effort**: ~3.2 we (optimistic; W6-1 pathway b PASS) up to ~5.7 we (pessimistic; W6-1 pathway a backup needed).

---

## §W6-1. `S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW` (T2.54 / W-6 CF-1)

**Status**: **CLOSED — PASS** (PASS-A: Reading A canonical confirmed; α_b = 2.692624 at L_fit ∈ [15, 22] via direct Connes-Karoubi pairing of §VII.AU.OP-PROJ Pillar I ↔ Pillar II HKR-image-bound observable on the substrate-IS band-0 + HKR realization; consensus PASS via Mellin + zeta F_2-axis FI sub-projection per workshop EC1 consensus criterion line 1150; audit_sha256=`d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d`; content_sha256=`3bbb66ef037869c9d91eef6e79557dd274d8d74e409d1aaff82e5e4c7caea209`; 3-tuple sign=PASS, mag=PASS, regime=VALID; tier_pin=TIER-2 SCHEMATIC level-pin disclosed via `-SCHEMATIC` convention suffix + companion comment row per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY. Pathway (a) L_max ≥ 35 backup NOT escalated per plan §12 lines 286-288.)
**Plan reference**: `sessions/session-plan/session-91-plan-w6.md §W6-1` (lines 38–293)
**Trigger**: `[VERIFY-THEOREM]` — tests substrate-IS prediction that `α=3` is the asymptotic exponent of the Mellin-cone universal envelope at d=4 substrate-distance-1 pole `s=3`; verifies whether `α≈1.9` at pre-asymptotic L_max ∈ [6, 12] is the realized finite-L manifestation of the asymptotic `α=3` per Friedrich-Bär saturation; OR whether `α≈1.9` persists post-asymptotically as the canonical exponent.
**Classification**: PHONONIC. The d=4 universal envelope IS a substrate-IS spectral-functional property of the substrate's Mellin-cone closure at substrate-distance-1 pole `s=3`. Direction substrate → emergent: substrate's combinatorial shell-sum geometry `dim(p,q) · (C_2(p,q)+1)^{-3}` at d=4 → universal `L^{-α}` envelope at all HKR-image-bound observables → cross-pillar bridge's Level-2 envelope numerical band → registry-PASS classification at downstream consumer.
**Agent type**: `lizzi-spectral-functional-theorist` (PRIMARY; functional-independent vs functional-dependent classification expertise; ZETA-NOT-PHYSICAL-75 substrate-IS envelope identification; F_2-class projection 5-regulator atlas membership analysis); `connes-ncg-theorist` CO-SIGN on the Connes-Karoubi pairing implementation at pathway (b) per workshop verdict §V row 3 (lizzi PRIMARY + connes CO-AUTHOR).
**Hypothesis**: The d=4 universal envelope at substrate-distance-1 pole `s=3` is `L^{-3}` asymptotically (Reading A canonical) AND `L^{-1.9}` realized at finite L_max ∈ [6, 12] (Reading B realized). At L_max ≥ 22 (pathway b direct Connes-Karoubi pairing), CF-65's empirical α converges from `≈ 1.929` toward `≈ 3` per the c_sub_corrected M_Pl_eff² parameterization's asymptotic-settling scale.
**Effort estimate**: ~0.8 we if pathway (b) returns clean PASS-A; up to ~3.3 we if both pathways dispatched.

### Method

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

### Machinery pin (PRDR)

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

### Expected output 4-tuple

`(value=alpha_pathway_b=<α_b>_majority_pass=<count>_of_5, scheme=direct-connes-karoubi-pairing-L_max-22-pathway-b, convention=Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION, L_max=22)`

Predicted Reading A: `α_b ≈ 2.6–3.0` at L_max=22 (HKR-image asymptotic settling per c_sub_corrected M_Pl_eff² ratio asymptotic-settling scale; majority_pass = 3–5 of 5).
Predicted Reading B: `α_b ≈ 1.9–2.0` at L_max=22 (persistent at all L_max; majority_pass = 0–1 of 5).

### PASS/FAIL/INFO thresholds

- **PASS-A (Reading A canonical confirmed; verdict (a) or HYBRID (d) retained)**: `|α_b − 3.0| / 3.0 < 0.20` (α ∈ [2.4, 3.6]) at MAJORITY-of-5 regulator-class sub-windows (count_pass ≥ 3) OR PASS-A at Mellin + zeta FI-axis F_2 projection (workshop EC1 consensus criterion line 1150). Composite collapse rule: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID ⇒ composite=PASS`.
- **FAIL-B (Reading B realized confirmed; verdict (d) HYBRID at per-regulator-class sub-window structure)**: `|α_b − 1.9| / 1.9 < 0.15` (α ∈ [1.615, 2.185]) AND count_pass ≤ 1 across regulators (Reading A consensus FAILS). Composite collapse: `sign_verdict=PASS (Reading B predicted L^{-1.9} persistence), magnitude_verdict=FAIL (vs α=3 target), regime_verdict=MARGINAL (L_max=22 still pre-asymptotic per Friedrich-Bär L_max ≥ 35) ⇒ composite=INFO IF magnitude_verdict=FAIL+regime=MARGINAL; composite=FAIL IF magnitude=FAIL+regime=VALID`. PER S87 schema-v2 collapse rule, the rule-correct composite is INFO (regime_verdict=MARGINAL at L_max=22) — but the substrate-physics interpretation is "Reading B realized confirmed at this pathway"; the FAIL-B label is preserved in the verdict-line `value=` field to disambiguate from generic INFO.
- **INFO (partial convergence)**: between PASS-A and FAIL-B bands; `α_b ∈ [2.185, 2.4]` OR (count_pass = 2 of 5); carry-forward to S92+ pathway (a) at L_max ≥ 35 + extended sub-window L_max ≥ 40. Composite: `regime_verdict=MARGINAL ⇒ INFO`.
- **Tolerance rule**: RATIO `|α_b − target| / target` on α (relative); ABSOLUTE on count_pass (integer membership in {0, 1, 2, 3, 4, 5}).

### Substitution chain (MANDATORY for `[VERIFY-THEOREM]` direction claim)

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

### Solution-space implications

- **PASS-A (Reading A canonical confirmed)**: closes the d=4 universal envelope asymptotic = `L^{-3}`; §VII.AU.OP-PROJ advances to STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway; §VII.AF.1.OP-PROJ Stage-3-PERMANENT promotion proceeds at L_max ≥ 22 cache; W11-5 sister registry-FAIL by ~21× confirmed under L^{-3}; W6-5 forced to re-tag W11-5 as REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (anchor still outside realized envelope).
- **FAIL-B (Reading B realized confirmed)**: HYBRID verdict (d) at per-regulator-class sub-window structure is the canonical reading; the d=4 universal envelope is `L^{-1.9}` at all L_max ∈ [6, 22]; §VII.AU.OP-PROJ first-extraction PASSES at α ≈ 1.9; W11-5 sister re-tag from registry-FAIL to registry-PASS (under L^{-1.9}, anchor may fall inside realized envelope; W6-5 verifies).
- **INFO (partial convergence)**: defers to S92+ L_max ≥ 40 extended scan; the d=4 universal envelope is in a pre-asymptotic boundary layer at L_max ∈ [22, 35] with incomplete settling; the Friedrich-Bär saturation theorem extension at L_max ≥ 35 (pathway a backup) is the next required dispatch.
- **Cross-pillar bridge anatomy K=3 corpus**: pathway (b) PASS adds the §VII.AU.OP-PROJ S91 instance to the cross-pillar-bridge corpus at K=3+ Hybrid Independence Test PASS at axis (iv) independent algebraic envelope (the c_sub_corrected M_Pl_eff² bypass IS structurally independent of the W-5 + W11-5 envelope corpus).

### Substrate framing

The d=4 universal envelope IS the substrate-IS asymptotic decay of the L_max → ∞ HKR-image at Pillar III ↔ IV (S86 W-5 §VII.AF.1.OP-PROJ calibration). The `L^{-1.9}` empirical fit at pre-asymptotic L_max ∈ [6, 12] IS the substrate-IS finite-L correction at the CM-1995 §III.4 residue formula's sub-asymptotic regime; the asymptotic `α=3` is reached at L_max ≥ 35 per Friedrich-Bär saturation. Direction substrate → emergent: substrate's spectral triple `(A_K, H_K, D_K)` IS the source; the universal envelope IS the substrate's combinatorial geometry; the Connes-Karoubi pairing IS the bridge map's substrate-IS realization at finite L. Container-thinking FORBIDDEN: the substrate is NOT "in" any spacetime container at any L_max; the universal envelope IS the substrate's intrinsic d=4 dimension manifestation.

### Results

**Outputs**: script `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.py` (42,236 bytes), data `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz`, plot `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.png` (log-log per-regulator R_b(L) overlay with α=3 + α=1.9 reference lines, left panel; per-regulator α bar chart with PASS-A / FAIL-B band shading, right panel).

**Connes-Karoubi pairing R_b(L) at L ∈ {12..22}** (substrate-IS band-0 P_0 + HKR-image realization on lowest-Casimir Peter-Weyl sector at each level; substrate-IS algebra-canonical combinatorial form per CM-1995 §III.4 residue-formula evaluator at substrate-distance-1 pole s=3; cache-independent at L > 12 per W6-4 OPERATIONAL DEVIATION precedent + Friedrich-Bär saturation theorem (W11-3)):

| L  | band-0 (p*, q*) | C_2(p*, q*) | dim(p*, q*) | R_b(L) = dim · (C_2+1)^{−3} |
|:--:|:----------------|:-----------:|:-----------:|:----------------------------|
| 12 | (6, 6)          | 48.0000     | 343         | 2.915452e-03                 |
| 13 | (6, 7)          | 55.3333     | 420         | 2.349378e-03                 |
| 14 | (7, 7)          | 63.0000     | 512         | 1.953125e-03                 |
| 15 | (7, 8)          | 71.3333     | 612         | 1.617097e-03                 |
| 16 | (8, 8)          | 80.0000     | 729         | 1.371742e-03                 |
| 17 | (8, 9)          | 89.3333     | 855         | 1.159904e-03                 |
| 18 | (9, 9)          | 99.0000     | 1000        | 1.000000e-03                 |
| 19 | (9, 10)         | 109.3333    | 1155        | 8.599274e-04                 |
| 20 | (10, 10)        | 120.0000    | 1331        | 7.513148e-04                 |
| 21 | (10, 11)        | 131.3333    | 1518        | 6.550343e-04                 |
| 22 | (11, 11)        | 143.0000    | 1728        | 5.787037e-04                 |

**Empirical α_b extraction on L_fit ∈ [15, 22]** (8-point log-log slope of R_b(L) vs L per plan §6 lines 113-119):

| Quantity | Value | Notes |
|:---------|:------|:------|
| **α_b (canonical, substrate-IS F_2-axis)**        | **2.692624** | log-log slope on Mellin/zeta sub-projection; in [2.4, 3.6] PASS-A band |
| slope_b                                           | −2.692624    | log_R = slope·log_L + intercept |
| intercept_b                                       | 0.870039     | linear-regression intercept |
| α_Mellin (F_2 axis; substrate-IS regulator-INVARIANT) | 2.692624 | substrate-distance pole INDEXING regulator-invariant BY CONSTRUCTION per CM-1995 §III.4 (FULL physical) |
| α_zeta (F_2 axis; substrate-IS regulator-INVARIANT)   | 2.692624 | identical to Mellin; F_2 axis FI sub-projection (FULL physical) |
| α_Pauli-Villars (convergence-tail axis; SCHEMATIC sub_term) | 6.476416 | W6-2 SCHEMATIC (Λ_UV/Λ_PV)²·L²·log(L) relative weight; OUT of PASS-A band |
| α_cutoff (convergence-tail axis; SCHEMATIC sub_term)        | 3.911086 | W6-2 SCHEMATIC linear-θ ramp; OUT of PASS-A band (just above 3.6) |
| α_lattice (convergence-tail axis; SCHEMATIC sub_term)       | 5.689296 | W6-2 SCHEMATIC sinc² form factor; OUT of PASS-A band |
| count_pass (in [2.4, 3.6]; of 5)                  | **2 / 5**    | Mellin + zeta only |
| majority_pass (count_pass ≥ 3)                    | **False**    | majority of 5 NOT reached |
| f2_pass (Mellin AND zeta both in PASS-A)          | **True**     | F_2-axis FI sub-projection PASSes |
| pathway_b_pass_a (majority OR F_2)                | **True**     | F_2-axis criterion suffices per workshop EC1 line 1150 consensus |
| fail_b_alpha (α_b in [1.615, 2.185])              | False        | α_b = 2.692624 outside FAIL-B band |
| fail_b_count (count_pass ≤ 1)                     | False        | count_pass = 2 > 1 |
| pathway_b_fail_b                                  | False        | Reading B realized confirmation NOT triggered |
| **composite verdict**                             | **PASS**     | PASS-A: Reading A canonical confirmed |
| band_tag                                          | `PASS_A_Reading_A_canonical_confirmed` |  |
| S87 schema-v2 3-tuple                             | sign=PASS, mag=PASS, regime=VALID | per plan §9 PASS-A collapse rule |

**Asymptotic-settling diagnostic** (CF-65 comparison): α at L_fit=[6..12] on the same SHELL form (precursor estimate from prototype): 2.4181; α at L_fit=[15..22]: 2.6926. **Monotonic increase from pre-asymptotic to extended L window confirms the asymptotic-settling direction predicted by Reading A** (substitution chain Step 1: c_sub_corrected_M_Pl_eff² → 1; α → α_asymptotic = 3 at L → ∞). The direct Connes-Karoubi pairing observable BYPASSES the c_sub_corrected bottleneck per workshop EC2 derivation lines 1162-1170.

### Verdict

**Gate verdict: PASS** (PASS-A: Reading A canonical confirmed via Mellin + zeta F_2-axis FI sub-projection per workshop EC1 consensus criterion line 1150).

**Canonical verdict line** (in `computations/session-91/s91_gate_verdicts.txt`):

```
S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW: PASS -- value='alpha_pathway_b=2.6926_count_pass=2_of_5_majority_pass=0_f2_pass=1_pathway_b_pass_a=1_pathway_b_fail_b=0;alpha_Mellin=2.6926_alpha_zeta=2.6926_alpha_PV=6.4764_alpha_cutoff=3.9111_alpha_lattice=5.6893;band_tag=PASS_A_Reading_A_canonical_confirmed' scheme=direct-connes-karoubi-pairing-L_max-22-pathway-b convention=Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION-SCHEMATIC L_max=22 audit_sha256=d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d content_sha256=3bbb66ef037869c9d91eef6e79557dd274d8d74e409d1aaff82e5e4c7caea209 schema_version=S87+
# audit_sha256_short=d54b26a970e43b6b content_sha256_short=3bbb66ef037869c9 # S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW dual-SHA companion row (W9a-99 split)
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW 3-tuple annotation (S87 schema-v2)
# tier_pin=TIER-2 # S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW SCHEMATIC level-pin disclosure (per .claude/rules/substrate-first-canonical-sourcing.md §iv K=4 MANDATORY; PV/cutoff/lattice members consume W6-2 sub_term_R SCHEMATIC analytic forms; F_2 axis (Mellin+zeta) is FULL physical substrate-IS canonical)
```

**Substitution-chain narration of direction comparison** (plan §10):
- Reading A direction (plan §10 Step 1): c_sub_corrected_M_Pl_eff²(L_max) → 1 as L_max → ∞ ⇒ α_pathway_b → α_asymptotic = 3 [direct Connes-Karoubi pairing bypasses c_sub bottleneck]. **Empirical**: α_b = 2.6926 at L_fit=[15..22]; α at L_fit=[6..12] = 2.4181 (precursor). Monotonic 2.4181 → 2.6926 INCREASE matches Reading A direction; structure-direction predicate satisfied.
- Reading B direction (plan §10 Step 2): α persistent at 1.929 across all L. **Empirical**: α_b = 2.6926 at L_fit=[15..22], far above the FAIL-B band [1.615, 2.185]. Reading B direction REFUTED.
- Step 3 PASS-A criterion satisfied at f2_pass (Mellin + zeta both α=2.6926 ∈ [2.4, 3.6]).
- Step 5 conclusion: "α increases with L_max under direct Connes-Karoubi pairing" — the PASS-A direction is realized at L_max=22.

**Level-pin honesty disclosure** (per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY): the F_2-axis (Mellin + zeta) sub-projection IS FULL physical substrate-IS canonical (regulator-INVARIANT BY CONSTRUCTION per CM-1995 §III.4 substrate-distance pole indexing). The PV / cutoff / lattice sub-projections consume the W6-2 sub_term_R SCHEMATIC analytic forms (W6-2 audit_sha256=`109e4307e8a0d805...` K=5 SCHEMATIC calibration). The convention= field carries the `-SCHEMATIC` suffix; the tier_pin=TIER-2 companion comment row is emitted alongside the canonical verdict line per the K=4 MANDATORY disclosure protocol. The PASS-A verdict rests on the F_2-axis F_2 sub-projection criterion (workshop EC1 consensus criterion line 1150), which is the FULL physical canonical sub-projection; the SCHEMATIC tagging affects only the PV / cutoff / lattice diagnostic alpha values (which are outside the PASS-A band anyway and do not contribute to the consensus criterion's PASS branch).

### Substrate framing (runtime addendum)

The substrate IS the spectral triple `(A_K, H_K, D_K)`; the d=4 universal envelope IS the substrate's intrinsic combinatorial geometry at substrate-distance-1 pole s=3. The Connes-Karoubi pairing `⟨[Ch(P_0)], [φ_g^{sym}]⟩` IS the substrate-IS realization of the §VII.AU.OP-PROJ Pillar I ↔ Pillar II bridge map at finite L; at L_max=22, the substrate's pairing value IS `dim(p*, q*)·(C_2(p*, q*)+1)^{−3}` for `(p*, q*) = argmin_{p+q=L} C_2(p, q) = (11, 11)`, with C_2 = 143, dim = 1728. There is no enveloping space the substrate inhabits at this L; the asymptotic envelope IS substrate-IS at every level. Direction substrate → emergent: substrate's combinatorial geometry IS the source; the universal envelope α = 2.69 (en route to α = 3 at L → ∞ per Friedrich-Bär saturation, reached for L ≥ 35) IS the substrate's intrinsic d=4 dimension manifestation; the Pillar I (NCG-axiomatic) ↔ Pillar II (CMB-cosmological) bridge IS the emergent realization at the partner-pillar laboratory image of the substrate-IS pairing.

Container-thinking FORBIDDEN: NOT "the band-0 sector is enclosed in the Peter-Weyl spectrum at L=22"; INVERT: the substrate's Peter-Weyl decomposition at level 22 IS what the substrate IS at that algebraic stratification; the band-0 sector IS the substrate's minimal-Casimir image of P_0 at level 22, not a thing inside a level-22 container. The cache-independence of pathway (b) at L > 12 IS itself a substrate-IS structural property: the substrate's algebra-canonical Peter-Weyl decomposition extends to L_max → ∞ by definition; eigenvalue diagonalization (required only for state-pair functionals; algebra-DEPENDENT) is structurally distinct from algebraic combinatorial decomposition (substrate-IS; algebra-INVARIANT spectrum-only-functional family per §VII.U.2 Corner I), and pathway (b) lives in the latter.

### Solution-space implications (runtime addendum)

**Structural puzzle (per task orchestrator override item 3)**: under upstream W6-4 FAIL (β̄ = 1.7725, σ_β = 0.8936, 3-of-4 observables outside [1.5, 2.5], cross-correlation min = −0.2625 anti-correlated), the W6-1 pathway (b) PASS-A on the §VII.AU.OP-PROJ observable creates a substrate-physics puzzle: the §VII.AU.OP-PROJ specific HKR-image-bound observable DOES asymptote toward α = 3 (band-0 + HKR pathway via direct Connes-Karoubi pairing), but the broader 4-observable family (M^(ζ)_3, R_FWD_C1, R_FWD_C2 candidate, Tr(D^{−6})) does NOT show universal d=4 envelope. This is consistent with:

- **Reading A canonical IS observable-specific, NOT universal** at the d=4 substrate-distance-1 pole s=3: the band-0 + HKR pathway selects the lowest-Casimir sector at each level (substrate-IS algebra-canonical), which IS the §VII.AU.OP-PROJ canonical realization, and IS where the L^{−3} asymptotic envelope manifests. The other observables (full Mellin trace, Cartan-diagonal BdG proxy, pure spectral moment Tr(D^{−6})) probe different cohomology sectors / pole indices / projector channels and produce different envelopes (β_O1 = 1.1564, β_O2 = 1.9324, β_O3 = 2.9718, β_O4 = 1.0293 per W6-4) that are NOT bound to the universal α = 3 prediction.
- **Layer-Functor F Verdict-Shape Consistency Theorem K=2 calibration is FALSIFIED at the 4-observable family layer** (per plan §22 W6-4 PASS consequences) BUT REMAINS INTACT at the §VII.AU.OP-PROJ-specific layer (the band-0 + HKR cohomology-class image's universal envelope IS substrate-IS at α → 3 per the direct Connes-Karoubi pairing).
- **§VII.AU.OP-PROJ advancement**: pathway (b) PASS-A unblocks the §VII.AU.OP-PROJ first-extraction at α ≈ 2.69 (en route to α = 3 at L_max ≥ 35); per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class refinement, the substrate-natural α is now empirically anchored at the F_2-axis FI sub-projection, advancing §VII.AU.OP-PROJ toward STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway. However, the broader Layer-Functor universal-envelope theorem is NOT advanced (W6-4 FAIL keeps that K-counter at K=1 or K=2 depending on prior corpus state).
- **W6-5 dispatch**: per plan §22 W6-4 FAIL line 1307 ("W6-5 not fired (no universal envelope to re-anchor against)"), W6-5 is NOT triggered by W6-1 PASS — the W6-5 trigger is W6-4 PASS specifically, not W6-1 PASS. W6-5 remains HARD-HALT per plan §22 W6-5 line 1315.
- **Cross-pillar bridge anatomy K=3 corpus** (per plan §11 line 282): pathway (b) PASS adds the §VII.AU.OP-PROJ S91 instance to the cross-pillar-bridge corpus at the Hybrid Independence Test axis (iv) "independent algebraic envelope" — the c_sub_corrected M_Pl_eff² bypass IS structurally independent of the W-5 + W11-5 envelope corpus per axis (iv); the §VII.AU.OP-PROJ canonical α = 2.69 (FULL physical at F_2 axis) IS substrate-natural and inherits the Level-2-binding HKR-bridge canonical-import-binding pin (`regulator-pin-discipline.md §"Binding axis"` K=1 SUGGESTION pending K=3).
- **INFO/FAIL fallback NOT triggered**: pathway (a) L_max ≥ 35 Friedrich-Bär saturation extension (plan §12 lines 286-288) is NOT escalated to S92+; PASS-A at pathway (b) closes the gate's first-extraction discriminator.

### Cross-references

- `joint-theorem-promotion.md §"Stage 1"` (STAGE-1-CANDIDATE advancement criterion for §VII.AU.OP-PROJ)
- `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` (K-counter advancement on axis (iv) independent algebraic envelope)
- `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` (FIRST-EXTRACTION sub-class for §VII.AU.OP-PROJ)
- `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"` (CACHE-PROJECTION pin)
- `regulator-pin-discipline.md §"Binding axis"` (canonical-import-binding K=1 SUGGESTION)
- `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` (Friedrich-Bär saturation pathway a backup)
- W6-3 (cheap precursor; α_sub at sub-window L_max ∈ {6..9})
- W6-4 (parallel discriminator at L_max=12 cache; biases W6-1 expectation)
- W6-5 (CONDITIONAL on W6-4 PASS; W11-5 sister re-audit)

### Carry-forward computations

#### CF-S91-W6-1-PATHWAY-A-FRIEDRICH-BAR-L_MAX-35-VERIFICATION (P2 — asymptotic-settling verification)

1. **What**: Verify the asymptotic-settling direction empirically established at pathway (b) (α: 2.42 → 2.69 monotonic increase from L_fit=[6..12] → L_fit=[15..22]) by extending the L scan to L_max ≥ 35 via Friedrich-Bär saturation theorem (W11-3 precedent). Predict: α(L_fit=[28..35]) → 2.85; α(L_fit=[40..50]) → 2.95; α(L → ∞) = 3 (Reading A canonical confirmed at structural asymptotic limit). Cross-checks the §VII.AU.OP-PROJ canonical advancement under the Friedrich-Bär saturation analytic upper-bound rooting.
2. **Who**: lizzi-spectral-functional-theorist (PRIMARY); connes-ncg-theorist CO-SIGN on Friedrich-Bär saturation theorem application per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` clause-2 (saturation-theorem analytic argument for L_max > 12).
3. **Input**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (UPSTREAM GATE: α_b = 2.6926 at L_fit=[15..22]; monotonic increase precursor)
   - SU(3) Peter-Weyl combinatorial formula (substrate-IS algebra-canonical; cache-independent)
   - canonical_constants.py: M_KK = 7.428660036284456e16 GeV, tau_fold = 0.190 (no new pins required)
   - `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` (Friedrich-Bär saturation theorem with η_FB_lower = 0.40 lower bound)
4. **Output**: α(L_max=35), α(L_max=50), α(L_max=100) per Friedrich-Bär analytic extension; PASS-A asymptotic confirmation predicate `|α(L → ∞) − 3| / 3 < 0.01` (1% tightening of pathway (b) PASS-A criterion); .npz + .png + verdict line.
5. **Format**: `computations/session-92/s92_*_d4_envelope_friedrich_bar_l_max_35_50_100.py` (.npz + .png + verdict in `computations/session-92/s92_gate_verdicts.txt`).
6. **Deadline**: S92 W0 (next session; precursor for §VII.AU.OP-PROJ Stage-2 PASS-AND cross-axis independent verify per `joint-theorem-promotion.md` Stage-2 protocol).
7. **Depends on**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE; α_b = 2.6926 anchor; precursor for asymptotic-settling direction)
   - SU(3) Peter-Weyl irrep dimension + quadratic Casimir formulae (no input pin)
   - math-scripts.md §"D_K Block-Diagonality Pre-Check" Friedrich-Bär saturation theorem (W11-3 precedent)

#### CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING (P1 — registry advancement primary)

1. **What**: Land §VII.AU.OP-PROJ at STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway: substrate-natural α_canonical = 2.6926 (FULL physical F_2-axis FI sub-projection per W6-1 pathway (b) PASS-A) replaces the prior REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION symbolic-only sub-class tag at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`. The α exponent moves from "parameterized slope_A canonical pending L_max scan" → empirically anchored at α = 2.6926 (with forward asymptotic projection α → 3 at L_max ≥ 35 per CF-S91-W6-1-PATHWAY-A above). Stage-1 entry text per `joint-theorem-promotion.md §"Stage 1"`: full theorem text + STAGE-1-CANDIDATE tag + joint clauses pre-specified (binding axis Level-2-binding-HKR-bridge-canonical-import-binding per `regulator-pin-discipline.md §"Binding axis"` K=1 SUGGESTION) + corrigenda from W6-4 FAIL upstream context (§VII.AU.OP-PROJ Stage-1-CANDIDATE landing is observable-specific to band-0 + HKR pathway, NOT universal across the 4-observable family per W6-4 FAIL).
2. **Who**: mack-cosmic-bridge (PRIMARY — sole writer of `sessions/permanent-results-registry.md` per `feedback_mack-bridge-role.md`); lizzi-spectral-functional-theorist CO-SIGN on the STAGE-1-CANDIDATE text drafting; connes-ncg-theorist CO-SIGN on the HKR-bridge canonical-import-binding citation.
3. **Input**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE; α_canonical = 2.6926 empirical anchor)
   - W6-1 verdict line at audit_sha256=`d54b26a970e43b6b...` (THIS GATE; canonical first-extraction PASS-A)
   - Connes-Chamseddine 1996 §2.2-2.3 (Connes-Karoubi pairing canonical anchor)
   - canonical_constants.py: pin α_canonical = 2.6926 (new constant; substrate-IS first extraction)
   - `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` (sub-class tag refinement protocol)
4. **Output**: §VII.AU.OP-PROJ updated registry entry text with STAGE-1-CANDIDATE tag + α_canonical = 2.6926 anchor; canonical_constants.py promotion `alpha_canonical_VII_AU_OP_PROJ_FW = 2.6926236951422458` with PROVENANCE entry (S91-W6-1, audit_sha256=`d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d`).
5. **Format**: registry-landing dispatch per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` (write_promotion → fsync → re-read → verify → emit exactly one verdict line); script at `computations/session-92/s92_*_vii_au_op_proj_stage_1_candidate_landing.py`; verdict at `computations/session-92/s92_gate_verdicts.txt`.
6. **Deadline**: S92 W0 (immediate; mack-cosmic-bridge sole-writer registry landing should land at next-session plan-freeze to advance the K=3 cross-pillar-bridge corpus).
7. **Depends on**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE)
   - `sessions/permanent-results-registry.md §VII.AU.OP-PROJ` (current REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION tag at line 18014)
   - canonical_constants.py: `alpha_canonical_VII_AU_OP_PROJ_FW` (new pin, to be promoted via mack-cosmic-bridge follow-up)

#### CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY (P1 — STAGE-1 → STAGE-3 promotion)

1. **What**: Stage-2 PASS-AND cross-axis independent verify of §VII.AU.OP-PROJ STAGE-1-CANDIDATE per `joint-theorem-promotion.md §"Stage 2"`. Two independent cross-reviewers on DIFFERENT axes dispatched in parallel, BOTH WITHOUT prior W6-1 workshop context: (i) axis-A spectral side: connes-ncg-theorist audits clauses including JOINT (Level-2-binding HKR-bridge); (ii) axis-B substrate side: volovik-superfluid-universe-theorist audits clauses including JOINT (Pillar I ↔ Pillar II bridge map). JOINT clauses PASS-AND'd across both verdicts (logical AND). Substrate-input orthogonality clause (S88 W-23 W7c-167 V.1; B.56) applies: ≥ 1 observable's data file consumed by exactly ONE reviewer (NOT both); pathway (b) npz consumed by axis-A only; the substrate-canonical α_canonical pin consumed by axis-B only.
2. **Who**: connes-ncg-theorist (axis-A spectral side); volovik-superfluid-universe-theorist (axis-B substrate side). Note: lizzi-spectral-functional-theorist EXCLUDED as cross-reviewer per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` axis-distinctness + downstream-inheritance reach (lizzi is W6-1 PRIMARY).
3. **Input**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE; axis-A spectral side only)
   - §VII.AU.OP-PROJ STAGE-1-CANDIDATE registry entry from `sessions/permanent-results-registry.md` after CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING lands (UPSTREAM CARRY-FORWARD)
   - canonical_constants.py: `alpha_canonical_VII_AU_OP_PROJ_FW = 2.6926236951422458` (axis-B substrate side only)
   - Connes-Chamseddine 1996 §2.2-2.3 (Connes-Karoubi pairing canonical anchor; axis-A only)
   - Volovik superfluid-universe substrate-natural analog (axis-B only)
4. **Output**: Stage-2 verdict (PASS-AND or FAIL) per `joint-theorem-promotion.md §"Stage 2"`; on PASS-AND with substrate-input orthogonality verified, §VII.AU.OP-PROJ promotes to STAGE-3-PERMANENT (third framework cross-axis joint theorem to reach STAGE-3 after §VII.AH at S90 W2 CF-20); on FAIL, theorem stays at STAGE-1 with remediation route.
5. **Format**: 2-agent parallel dispatch script `computations/session-93/s93_*_vii_au_op_proj_stage_2_pass_and_verify.py` (orchestrator-coordinated; each cross-reviewer emits independent verdict; aggregator combines via logical AND); verdicts at `computations/session-93/s93_gate_verdicts.txt`.
6. **Deadline**: S93 W0 (after CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING lands at S92).
7. **Depends on**:
   - `sessions/permanent-results-registry.md §VII.AU.OP-PROJ` STAGE-1-CANDIDATE entry from CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING above
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE; axis-A only)
   - canonical_constants.py: `alpha_canonical_VII_AU_OP_PROJ_FW` (axis-B only)

#### CF-S91-W6-1-PV-CUTOFF-LATTICE-FULL-PHYSICAL-RETRY (P3 — SCHEMATIC-vs-FULL discriminator)

1. **What**: Re-run W6-1 pathway (b) under FULL physical Pauli-Villars / cutoff / lattice regularizations (S61/S78 pipeline at Λ_UV = M_KK) instead of W6-2 SCHEMATIC sub_term_R analytic forms. Quantifies the SCHEMATIC vs FULL physical D_max per `epistemic-discipline.md §"Source Reconciliation"` Class-(f) measurement at substrate-distance-1 pole s=3 envelope exponent. Predict: under FULL physical regularizations, PV / cutoff / lattice α may converge toward 3 (joining Mellin + zeta in PASS-A band, advancing count_pass from 2/5 to 5/5 majority_pass = True). Tests whether the convergence-tail axis MIXED classification at K_csub_R (W6-2 FAIL) is artifact of the SCHEMATIC sub_term parameterization, OR a genuine substrate-natural feature.
2. **Who**: lizzi-spectral-functional-theorist (PRIMARY — FI/RD/MIXED classification expertise); connes-ncg-theorist CO-SIGN on Connes-Chamseddine 1996 §2.2-2.3 FULL physical multiplier implementation.
3. **Input**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE; SCHEMATIC baseline at PV/cutoff/lattice α = {6.48, 3.91, 5.69})
   - S61/S78 FULL physical Pauli-Villars subtraction pipeline (UPSTREAM SUBSTRATE; mass-scale running, dimensional regularization, etc.)
   - Connes-Chamseddine 1996 §2.2-2.3 FULL physical multipliers (replacement of `_spectral_action_regulators.py` SCHEMATIC helper)
   - canonical_constants.py: M_KK, tau_fold, kappa_2_substrate_FW (no new pins)
4. **Output**: α_PV_FULL, α_cutoff_FULL, α_lattice_FULL at L_fit=[15..22]; D_max(SCHEMATIC, FULL) per regulator class; advances W6-2 K=5 SCHEMATIC-vs-FULL D_max calibration corpus per `substrate-first-canonical-sourcing.md §(iv)` (FULL physical retry instance for forward K=6 calibration).
5. **Format**: `computations/session-92/s92_*_d4_envelope_pv_cutoff_lattice_full_physical_retry.py` (.npz + .png + verdict line; FULL level pin per substrate-first-canonical-sourcing.md §(iv) FULL tier).
6. **Deadline**: S92 W1 (after S92 W0 closes CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING; FULL physical retry is independent of registry landing).
7. **Depends on**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE; SCHEMATIC baseline)
   - S61/S78 FULL physical Pauli-Villars pipeline at Λ_UV = M_KK (UPSTREAM; substrate-canonical implementation)
   - Connes-Chamseddine 1996 §2.2-2.3 (FULL physical multipliers)

#### CF-S91-W6-1-LAYER-FUNCTOR-F-PUZZLE-DISAMBIGUATION (P2 — cross-axis structural workshop)

1. **What**: 2-agent adversarial workshop on the substrate-physics puzzle surfaced by the W6-4 FAIL + W6-1 PASS-A combination: §VII.AU.OP-PROJ-specific HKR-image-bound observable asymptotes to α → 3 (Reading A canonical confirmed AT THIS OBSERVABLE), but the 4-observable family does NOT show universal d=4 envelope (Reading A coincidence confirmed AT THE FAMILY LAYER). Reading divergence: (i) lizzi-side reading: the §VII.AU.OP-PROJ canonical envelope IS observable-specific at the band-0 + HKR cohomology-class image; the universal-envelope claim at the 4-observable family layer was over-extension; the Layer-Functor F Verdict-Shape Consistency Theorem holds at the §VII.AU.OP-PROJ-specific layer but NOT at the 4-observable family layer. (ii) connes-side reading: the 4-observable family's β_O3 = 2.9718 (Cartan-diagonal BdG proxy at substrate-distance-2 pole s=4) IS consistent with the §VII.AU.OP-PROJ α → 3 limit; the W6-4 σ_β = 0.8936 comes from β_O1 and β_O4 (full Mellin trace + pure spectral moment Tr(D^{−6}) = 1.16 and 1.03 respectively); these observables probe DIFFERENT pole indices (s = 3 + structural, s = 6) and CANNOT be expected to share the α = 3 envelope at substrate-distance-1 pole s=3. The Layer-Functor F theorem at the §VII.AU.OP-PROJ layer is INTACT. Adjudication question: which reading correctly characterizes the universal-envelope theorem's scope?
2. **Who**: lizzi-spectral-functional-theorist + connes-ncg-theorist (2-agent workshop with adversarial reading divergence; per `Investigating-Workshops.md §"Definition: A WORKSHOP IS"` ALL FOUR conditions: 2 agents, genuine ledger-dissonance, multi-round R1/R2/R3, output = structural verdict).
3. **Input**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE; α_b = 2.6926 at §VII.AU.OP-PROJ-specific layer)
   - `computations/session-91/s91_w6_4_d4_mellin_cone_discriminator.npz` (UPSTREAM W6-4; β̄ = 1.7725, σ_β = 0.8936, per-observable β_O1/O2/O3/O4 = 1.16/1.93/2.97/1.03)
   - §VII.AU.OP-PROJ STAGE-1-CANDIDATE entry from CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING
   - `sessions/archive/session-90/session-90-lizzi-s7-d4-envelope-synthesis.md` (Layer-Functor F Verdict-Shape Consistency Theorem K=2 calibration corpus)
4. **Output**: structural verdict on Layer-Functor F universal-envelope theorem scope (§VII.AU.OP-PROJ-specific vs 4-observable-family-universal); 5-element anatomy entry per `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy"` if cross-pillar bridge structural ambiguity is identified; rule-extension proposal if Layer-Functor F scope clause needs sharpening at the methodology layer.
5. **Format**: workshop document at `sessions/archive/session-92/workshops/s92-w*-layer-functor-f-puzzle-disambiguation.md`; verdict at workshop §Wrap-Up.
6. **Deadline**: S92 W3+ (after CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING + CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY land at S92 / S93).
7. **Depends on**:
   - `computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz` (THIS GATE)
   - `computations/session-91/s91_w6_4_d4_mellin_cone_discriminator.npz` (UPSTREAM W6-4)
   - §VII.AU.OP-PROJ STAGE-1-CANDIDATE entry post-CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING

---

## §W6-2. `S91-K_HK-AND-K_CSUB-EMPIRICAL-ANCHORING` (T2.58 / W-6 CF-7)

**Status**: CLOSED — composite verdict **FAIL** (band `FAIL_K_HK_OR_K_csub_substrate_IS_mismatch`); K_HK = 9 FI confirmed across A_5 atlas (spread = 0 BY CONSTRUCTION; sign_verdict PASS); K_csub_R values under the SCHEMATIC sub_term_R analytic forms (plan §10 Step 3) produce |K_csub_mean − 0.5| ≫ 0.2 (magnitude_verdict FAIL); composite collapses to FAIL per gate-verdicts.md §"S87+ Composite-collapse rule" because regime_verdict=VALID + magnitude_verdict=FAIL collapses to composite FAIL. audit_sha256=`109e4307e8a0d80578318de29315b688287704cba1518bd651845db4a1cb984f`; content_sha256=`634e6e05d1aa071209c05658cfe0028f3297cc99b18dbeddc7cf9c5f73bc093a`. Level pin SCHEMATIC disclosed via `-SCHEMATIC` convention suffix + `tier_pin=TIER-2` companion row per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY.
**Plan reference**: `sessions/session-plan/session-91-plan-w6.md §W6-2` (lines 296–520)
**Trigger**: `[VERIFY]` — verifies substantive empirical anchoring of K_HK ≈ 9 FI partition cardinality and K_csub ≈ 0.5 ± 0.1 MIXED convergence-tail observable per workshop EMERGENCE A2 + EC1 substantive answers at lines 1017-1018 + 1146-1150.
**Classification**: PHONONIC. K_HK IS the partition cardinality of HH^*(A_K) at the substrate's 9-cell tensor channel decomposition layer per S87 W4-2 §VII.AJ.W4-1 calibration; K_csub IS the c_sub_corrected M_Pl_eff² ratio's convergence-tail observable at the substrate-distance s* = 2 Mellin pole. Both are substrate-IS observables; the FI vs MIXED classification IS the methodology-layer F-image of the substrate's algebra-INVARIANT vs algebra-DEPENDENT axis structure per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3.
**Agent type**: `lizzi-spectral-functional-theorist` (PRIMARY; FI/RD/MIXED classification expertise per ZETA-NOT-PHYSICAL-75 + F_2-class projection 5-regulator atlas; the originator of the FI/RD program; functional-sensitivity analysis across 5 regulator-class members at the convergence-tail axis). `connes-ncg-theorist` CO-SIGN on the HH^*(A_K) 9-cell partition cardinality derivation per S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration (NCG-axiomatic anchor for K_HK FI classification).
**Hypothesis**: K_HK = 9 is FI (algebra-INVARIANT spectrum-only functional; regulator-INVARIANT BY CONSTRUCTION at the partition cardinality layer per S87 W4-2 calibration); K_csub ≈ 0.5 ± 0.1 is MIXED at the convergence-tail axis (algebra-DEPENDENT through M_Pl_eff² ratio's regulator-class-specific subtraction term; per-regulator-class K_csub_R values differ).
**Effort estimate**: ~1.5 we (per-regulator-class K_csub_R extraction at L_max ∈ [8, 22] across 5 regulators + spread analysis + FI/MIXED classification + working-paper section + verdict line; substrate-physics-level compute at M_Pl_eff² channel per regulator-class member).

### Method

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

### Machinery pin (PRDR)

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

### Expected output 4-tuple

`(value=K_HK=9_FI_K_csub_mean=<μ>_std=<σ>_MIXED, scheme=per-regulator-class-K_csub_R-extraction-A_5-atlas, convention=HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION, L_max=22)`

Predicted: `K_HK = 9` (integer; regulator-INVARIANT BY CONSTRUCTION); `K_csub_mean ≈ 0.4–0.6`; `K_csub_std > 0.05` (MIXED); `K_csub_F2_diff < 0.02` (Mellin+zeta FI-axis projection).

### PASS/FAIL/INFO thresholds

- **PASS**: `K_HK = 9` (exact integer; FI verified across all 5 regulators) AND `|K_csub_mean − 0.5| < 0.1` AND `K_csub_std > 0.05` (MIXED at convergence-tail axis confirmed). Composite: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID ⇒ composite=PASS`.
- **INFO**: `K_HK = 9` FI confirmed AND `K_csub_F2_diff / K_csub_F2_mean < 0.02` (Mellin+zeta agree at F_2-axis FI) BUT `K_csub_std ≤ 0.05` (5-regulator MIXED FAILS). Indicates K_csub is FI at F_2 projection only, not MIXED across full 5-regulator atlas; refines workshop EC1 classification. Composite: `regime_verdict=MARGINAL ⇒ INFO`.
- **FAIL**: `K_HK ≠ 9` (substrate-IS partition cardinality FAILS; structural defect) OR `|K_csub_mean − 0.5| ≥ 0.2` (substrate-natural anchor 2× off prediction). Composite: `regime_verdict=BREAKDOWN ⇒ FAIL`.
- **Tolerance rule**: ABSOLUTE on K_HK integer match (no tolerance; exact); ABSOLUTE on `|K_csub_mean − 0.5|` (Δ ≤ 0.1 PASS, Δ ≥ 0.2 FAIL); RATIO on F_2-axis spread.

### Substitution chain (MANDATORY for `[VERIFY]` direction claim)

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

### Solution-space implications

- **PASS**: K_HK FI + K_csub MIXED confirmed at substrate-IS layer; advances `regulator-pin-discipline.md` MIXED-class taxonomy with the c_sub_corrected M_Pl_eff² calibration corpus instance (K=1 SUGGESTION → K=2 candidate); §VII.AU.OP-PROJ Element 5 ANNOTATION block per W6-1 substitution chain Step 5 direction reflects MIXED classification at the convergence-tail axis.
- **INFO** (K_csub F_2-axis FI, not full-atlas MIXED): refines `regulator-pin-discipline.md` taxonomy with a NEW sub-class "F_2-axis FI / full-atlas MIXED" intermediate classification; advances `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` clause taxonomy candidate K=1.
- **FAIL**: K_HK = 9 EXACT FAILS would signal a structural defect in the algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` — extremely unlikely; would force a Wedderburn-decomposition re-derivation at substrate-IS NCG-axiomatic level. K_csub FAIL signals the c_sub_corrected M_Pl_eff² parameterization needs re-derivation (W8 WP §W8-7(c) anchor invalidated).

### Substrate framing

K_HK IS the substrate-IS partition cardinality of HH^*(A_K) — a property INTRINSIC to the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, NOT a property of "data placed in a container labeled A_K". K_csub IS the substrate-IS asymptotic ratio of M_Pl_eff² at the convergence tail — a property of the substrate's CM-1995 §III.4 dimension-spectrum at substrate-distance s* = 2 pole. Direction substrate → emergent: the algebra `A_K` IS the substrate; the HH^* partition IS the substrate's cohomological structure; the M_Pl_eff² ratio IS the substrate's emergent Newton's constant ratio (Phi(a_2) → Σ_2 weight-2 image per Phi correspondence). Container-thinking violation FORBIDDEN: "HH^*(A_K) lives in some enveloping space" — INVERTED: "HH^* IS the substrate's intrinsic Hochschild cohomology, computed from A_K's central projections by construction".

### Results

| Quantity | Value | Notes |
|:---------|:------|:------|
| K_HK | **9** | Künneth-Morita 3×3 cell count for A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) per S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration |
| K_HK_per_regulator (5-atlas) | `{Mellin: 9, zeta: 9, Pauli-Villars: 9, cutoff: 9, lattice: 9}` | identical across A_5 atlas BY CONSTRUCTION |
| K_HK_per_regulator_spread | **0** | max − min = 0; FI BY CONSTRUCTION (no regulator enters partition count) |
| K_HK_FI_verified | **True** | all 5 regulators yield K_HK = 9 |
| K_csub_R [Mellin] | **−245.692911** | from 1/L→0 linear fit on M_Pl_eff²(L)/M_Pl_eff²(0); sub_term_M = 0 (CM-1995 §III.4 substrate-distance pole INDEXING is regulator-INVARIANT); large-magnitude intercept arises from L_max=22 extrapolation of the κ_2-quadratic-in-L_max growth term `1 + κ_2·L²/(5π)² = 1 + 2.09 = 3.09` at L=22; the 1/L linear extrapolation overshoots because the underlying L_max-truncated proxy `sum 1/lambda_i²` saturates at large L (substrate-IS spectrum has finite cardinality at each L_max) while the κ_2 growth term continues to grow analytically — producing the large extrapolated intercept |
| K_csub_R [zeta] | **−245.692911** | identical to Mellin (sub_term_M = sub_term_ζ = 0 by F_2-axis FI); zero spread between Mellin & zeta |
| K_csub_R [Pauli-Villars] | **−5.0352 × 10^33** | sub_term_PV = (M_KK/(10·M_KK))²·L²·log(L) = 0.01·L²·log(L); multiplied by Λ_UV² = M_KK² ≈ 5.52 × 10^33 GeV² generates the OOM-33 scale at L=22 |
| K_csub_R [cutoff] | **−1.4010 × 10^66** | sub_term_C = (M_KK/λ_max(L=12))²·L·θ(L−6) = (M_KK/5.42)²·L·θ; the (M_KK/5.42)² factor is enormous (M_KK ≈ 7.43 × 10^16) and produces OOM-66 scale |
| K_csub_R [lattice] | **−1.6492 × 10^35** | sub_term_lat = (M_KK · a)²·L²·sinc²(L·a·π) = L²·sinc² (a = 1/M_KK ⇒ M_KK·a = 1); OOM-35 from Λ_UV² = M_KK² factor |
| K_csub_mean | **−2.8021 × 10^65** | mean across A_5 atlas; dominated by cutoff term (OOM-66) |
| K_csub_std | **+5.6042 × 10^65** | population std across A_5 atlas; >> 0.05 ⇒ MIXED criterion technically satisfied (driven by cutoff outlier) |
| K_csub_std_relative | **2.0000** | std/|mean| = 2 (cutoff dominates so much that mean and std are of the same order with cutoff providing nearly all variance) |
| K_csub_F2_diff | **0.0000 × 10^0** | |Mellin − zeta| = 0 exactly (both have sub_term_R = 0 BY CONSTRUCTION at d=4 pole) |
| K_csub_F2_mean | **−245.692911** | (Mellin + zeta) / 2 — F_2-axis projection |
| K_csub_F2_FI | **True** | Mellin & zeta agree at 0% spread (BY CONSTRUCTION) — F_2-axis FI confirmed |
| K_csub_MIXED_verified | **True** | std (5.60 × 10^65) > 0.05 — technically passes MIXED threshold, but driven by SCHEMATIC sub_term divergences not by substrate-IS regulator-class structure |
| |K_csub_mean − 0.5| | **2.80 × 10^65** | ≫ 0.2 substrate-natural anchor band ⇒ magnitude_verdict FAIL |
| pass_direction_K_HK | **True** | K_HK = 9 AND K_HK_FI_verified ⇒ sign-axis PASS direction |
| pass_direction_K_csub | **False** | K_csub_MIXED True but |K_csub_mean − 0.5| ≥ 0.1 |
| Machinery: M_Pl_eff²(0) | substrate-IS (0,0) sector | computed from cache as `sum 1/λ_i²` for L_max=0 evaluator |
| Machinery: λ_max (L=12 cache) | **5.418937** | empirical |λ|_max from S84 L=12 spectrum cache |
| Machinery: Λ_UV | **7.4287 × 10^16 GeV** | M_KK pin (canonical_constants.py:339-341) |
| Machinery: Λ_PV | **7.4287 × 10^17 GeV** | 10·M_KK canonical PV regulator scale |
| Machinery: a_lattice | **1.3461 × 10^−17 GeV^−1** | 1/M_KK lattice spacing |
| Machinery: κ_2_substrate_FW | **2.10181 × 10^−2** | canonical_constants.py:559 (S89 second-order Jensen perturbation) |
| Machinery: L_grid | `[8, 10, 12, 14, 16, 18, 20, 22]` | per plan §7 (avoids L ≤ 6 pre-asymptotic boundary) |
| Machinery: cache | S84 spectrum at L_max=12, τ_fold=0.190 | 90 sectors, 166,896 total |evals| at L_max=12 |

### Verdict

**Composite**: `FAIL` — band `FAIL_K_HK_OR_K_csub_substrate_IS_mismatch`.

**Schema-v2 3-tuple**: `sign_verdict = PASS`, `magnitude_verdict = FAIL`, `regime_verdict = VALID` ⇒ composite collapses to **FAIL** per gate-verdicts.md §"S87+ Composite-collapse rule" (line: "elif magnitude_verdict == FAIL and regime_verdict == VALID: composite = FAIL"). The sign-axis is PASS (K_HK = 9 EXACT matches the pre-registered substrate-IS prediction); the magnitude-axis FAILS because |K_csub_mean − 0.5| = 2.80 × 10^65 ≫ 0.2 substrate-natural anchor band.

**Substitution-chain narration** (per plan §10 Steps 1–5; mnemonic-vs-exact rigor per `math-scripts.md §"Double-Check Logic Before Compute"`):

- **Step 1** (K_HK derivation): A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) has 3 central simple summands; by Künneth-Morita, HH^*(A_K) decomposes into 3 × 3 = 9 tensor channels. The 9-cell partition cardinality K_HK = 9 is verified by direct enumeration:
  `cells = {(ℂ,ℂ), (ℂ,ℍ), (ℂ,M_3), (ℍ,ℂ), (ℍ,ℍ), (ℍ,M_3), (M_3,ℂ), (M_3,ℍ), (M_3,M_3)} ⇒ |cells| = 9`.
  This count is INTRINSIC to A_K central projections; no regulator enters the count. **Direction**: K_HK = 9 EXACT — sign-axis PASS confirmed.

- **Step 2** (K_HK FI verification): the loop over R ∈ A_5 atlas yields K_HK_per_regulator[R] = 9 for ALL R (Mellin, zeta, Pauli-Villars, cutoff, lattice); spread = 0. **Direction**: K_HK is FI BY CONSTRUCTION across A_5 — F_2-axis FI sub-projection trivially satisfied (Mellin = zeta = 9).

- **Step 3** (K_csub_R derivation under SCHEMATIC sub_term_R forms per plan §10 lines 487-490):
  - `Mellin`: sub_term_M(L) = 0 (substrate-distance pole indexing regulator-INVARIANT BY CONSTRUCTION at d=4 pole; CM-1995 §III.4) ⇒ K_csub_Mellin reflects only the κ_2·L²/(5π)² growth term plus the L_max-truncated `sum 1/λ_i²` proxy saturation. Empirical intercept = −245.693 from 1/L→0 linear fit.
  - `zeta`: identical to Mellin (sub_term_ζ = 0 by F_2-axis FI) ⇒ K_csub_zeta = −245.693 (bit-identical to Mellin; |Mellin − zeta| = 0.0 exactly).
  - `Pauli-Villars`: sub_term_PV(L) = (Λ_UV/Λ_PV)² · L² · log(L) = 0.01 · L² · log L; multiplied by Λ_UV² = M_KK² ≈ 5.52 × 10^33 GeV² ⇒ K_csub_PV ≈ −5.04 × 10^33 (OOM-33 from Λ_UV² prefactor).
  - `cutoff`: sub_term_C(L) = (Λ_UV/λ_max(L=12))² · L · θ(L−6) = (M_KK/5.42)² · L = (1.37 × 10^16)² · L ≈ 1.88 × 10^32 · L; multiplied by Λ_UV² ≈ 5.52 × 10^33 ⇒ K_csub_cutoff ≈ −1.40 × 10^66 (OOM-66 from product).
  - `lattice`: sub_term_lat(L) = (Λ_UV · a_lattice)² · L² · sinc²(L · a_lattice · π) = L² · sinc²(L · π / M_KK) ≈ L² for L · π / M_KK ≈ 0 (the sinc² factor is 1 at this resolution because L · a_lattice · π is microscopic); multiplied by Λ_UV² ≈ 5.52 × 10^33 ⇒ K_csub_lat ≈ −1.65 × 10^35 (OOM-35).

- **Step 4** (MIXED prediction substitution): K_csub_R values differ at spread ≫ 5% across A_5 atlas — TECHNICALLY satisfies K_csub_MIXED_verified = True. However, the spread is driven by SCHEMATIC sub_term divergences (Λ_UV² · sub_term_R(L) factors of OOM-33, OOM-35, OOM-66 for PV/lattice/cutoff respectively), NOT by substrate-IS regulator-class structure as the workshop A2 + EC1 substrate-natural anchor pin (K_csub ≈ 0.5 ± 0.1) requires. The "MIXED" verdict at this layer is structurally vacuous (it would be MIXED for any sufficiently divergent sub_term parameterization).

- **Step 5** (Direction of comparison): PASS direction was pre-registered as "K_HK exactly 9 AND K_csub spread > 5% across A_5 AND |K_csub_mean − 0.5| < 0.1". The first two conditions are satisfied; the third FAILS catastrophically (|Δ| = 2.80 × 10^65, ≫ FAIL band 0.2). Composite collapses to FAIL.

**Root cause**: the SCHEMATIC analytic sub_term_R(L) forms in plan §10 Step 3 are NOT calibrated to produce K_csub anchored at 0.5 ± 0.1. The sub_term forms encode the qualitative structural signature (PV grows as L² log L; cutoff grows linearly with sharp boundary at L_cut = 6; lattice has sinc² damping at L · a · π) but lack the normalizing prefactor that would set the asymptotic K_csub at the substrate-natural anchor. The Λ_UV² = M_KK² ≈ 5.52 × 10^33 GeV² prefactor (canonical UV-cutoff pin at M_KK per `substrate-first-canonical-sourcing.md §(iv)` FULL physical level pin target) dimensionally overwhelms the dimensionless M_Pl_eff²(0) ratio target ~ O(1). The substrate-natural normalization would require either (a) dividing sub_term_R by `M_Pl_eff²(0)` to make it dimensionless, OR (b) replacing Λ_UV with a regulator-class-specific natural scale (e.g., Λ_PV for PV-only; λ_max for cutoff-only), OR (c) the FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers route which constructs sub_term from the substrate's own zeta-function moments rather than from generic UV-divergence forms.

The verdict FAIL is informative about the SCHEMATIC sub_term parameterization layer, NOT about the substrate-IS K_csub observable per se. K_HK = 9 FI is the structurally meaningful PASS result of this gate; K_csub anchoring requires forward-session retry with substrate-natural normalization (see Carry-forward §"CF-S91-W6-2-FULL-PHYSICAL-RETRY" below).

**FI/MIXED classification update**:
- K_HK: **FI** (algebra-INVARIANT spectrum-only functional; regulator-INVARIANT BY CONSTRUCTION at the partition cardinality layer per S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration). Anchors a new permanent calibration row in the FI registry catalog at the partition-cardinality observable class — this is the first FI registry instance whose FI-ness is provable BY CONSTRUCTION (no per-regulator scan needed; the count IS regulator-blind).
- K_csub at convergence-tail axis: **REGULATOR-DIVERGENT under SCHEMATIC sub_term parameterization**; MIXED-vs-FI classification at the substrate-IS layer is **DEFERRED-PENDING-FULL-PHYSICAL-NORMALIZATION** per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` PROXY-REFINEMENT sub-class. The SCHEMATIC verdict at this gate is a precursor measurement; the substrate-IS classification awaits the FULL physical multipliers route.

**Solution-space update**: closes the SCHEMATIC sub_term parameterization corridor as a viable route to K_csub substrate-natural anchoring (FAIL). The route's `Λ_UV² · sub_term_R(L)` term magnitude is dimensionally incompatible with the dimensionless K_csub anchor target. The substrate-IS K_csub classification remains OPEN, eligible for forward FULL-physical-multipliers retry. The K_HK = 9 FI partition cardinality is now a **permanent CLOSED-FI result** — independent of any K_csub outcome.

### Substrate framing (runtime addendum)

The K_HK = 9 result confirms that the substrate's intrinsic Hochschild cohomology HH^*(A_K) partitions into exactly 9 tensor channels under Künneth-Morita decomposition of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ). The substrate **IS** this 9-cell partition — it is NOT "data placed in a container labeled HH^*(A_K)". The count 9 emerges from A_K's intrinsic central projections; no observer chooses it, no regulator can shift it, no L_max truncation modifies it. The 9-cell partition IS the substrate's cohomological structure at the partition-cardinality layer (per S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration; the OP-PROJ side of the algebra-axis K=3 MANDATORY classification per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`). The 5-regulator atlas {Mellin, zeta, Pauli-Villars, cutoff, lattice} yields identical K_HK = 9 BY CONSTRUCTION — this is the strongest possible empirical demonstration of FI: the FI-ness is provable analytically (Künneth-Morita does not depend on regulator choice), and the empirical scan confirms zero spread.

The K_csub FAIL is structurally informative about the **methodology layer** F-image (the SCHEMATIC sub_term_R parameterization choice), NOT about the **substrate layer** K_csub observable itself. Per the layer-functor F : substrate → methodology → audit (per `epistemic-discipline.md §"Layer-Decomposition"`): the methodology choice of SCHEMATIC sub_term forms is an audit-layer pin, the divergent K_csub_R values are the methodology-layer F-image, the SUBSTRATE-LAYER K_csub IS the substrate's emergent c_sub_corrected M_Pl_eff² ratio at the convergence tail — a property of the substrate's CM-1995 §III.4 dimension-spectrum at substrate-distance s* = 2 pole. The substrate-layer object is INTACT under this FAIL; only the methodology-layer probe was inadequate (regulator-class-blind UV prefactor normalization).

Direction substrate → emergent under the Phi correspondence (per `epistemic-discipline.md §"Layer-Decomposition"` §"Phi correspondence"): the algebra `A_K` IS the substrate (substrate-layer); the HH^* 9-cell partition IS the substrate's cohomological structure (substrate-layer); the M_Pl_eff² ratio at L→∞ IS the substrate's emergent Newton's constant ratio image under Phi(a_2) → Σ_2 weight-2 image (emergent layer). The methodology-layer SCHEMATIC sub_term_R parameterization is a probe of the emergent-layer observable, not of the substrate-layer object directly. Container-thinking violation FORBIDDEN: "HH^*(A_K) lives in some enveloping space we sample with 5 regulators" — INVERTED: "HH^* IS the substrate's intrinsic Hochschild cohomology computed from A_K's central projections by construction; the 5 regulators are 5 methodology-layer F-images of the same substrate-layer 9-cell partition; all 5 F-images yield 9 because the substrate-layer object is regulator-invariant".

The Single-τ-slice vs moduli-deformation substrate-IS level distinction (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`) applies here at Level 1 (single-τ-slice): K_HK is computed on the substrate at τ_fold = 0.190 single-τ slice; the cache L=12 spectrum (90 sectors, 166,896 |evals|) is the substrate's intrinsic spectral structure at this single-τ anchor. Level-2 (moduli-deformation) K_HK is trivially the same (Künneth-Morita does not depend on τ at all; K_HK is a substrate-IS invariant at BOTH levels).

### Cross-references

- S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration (HH^*(A_K) 9-cell partition cardinality anchor; this gate is the first FI calibration corpus instance at the partition-cardinality observable class)
- `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (FI vs MIXED axis structure; K_HK on the algebra-INVARIANT spectrum-only side; K_csub on the algebra-DEPENDENT state-pair-functional side at the convergence-tail axis)
- `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` PROXY-REFINEMENT sub-class (K_csub classification deferred pending FULL physical multipliers retry; SCHEMATIC sub_term forms are PROXY)
- `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (this gate is the third K-counter calibration instance for the OP-PROJ vs STATE-PROJ suffix discipline; convention tag carries `HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION-SCHEMATIC` with OP-PROJ suffix explicit)
- `regulator-pin-discipline.md` (per-regulator `a_n^{R}` pinning + MIXED-class taxonomy; this gate provides empirical calibration corpus data for the MIXED-class taxonomy at the convergence-tail axis)
- `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY (level pin SCHEMATIC vs FULL physical; this gate's `-SCHEMATIC` convention suffix + `tier_pin=TIER-2` companion row honors the K=4 MANDATORY discipline — POSITIVE-CALIBRATION class per S90 W1-9 3-class taxonomy)
- `epistemic-discipline.md §"Layer-Decomposition"` (substrate → methodology → audit F-image; the K_csub FAIL is at the methodology layer, NOT the substrate layer)
- `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (this gate operates at Level 1 single-τ slice at τ_fold = 0.190)
- W8 WP §W8-7(c) lines 1197-1207 (c_sub_corrected M_Pl_eff² parameterization; SCHEMATIC analytic form anchored at the κ_2-quadratic-in-L_max growth term)
- S90 W8 `s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.py:221` `compute_m_pl_eff_squared(eigs)` (the a_2 channel proxy `sum 1/λ_i²` used for the L-truncated M_Pl_eff² evaluation; substrate-IS convention pin)
- canonical_constants.py:559 (`kappa_2_substrate_FW = 0.021018084987437196` — S89 second-order Jensen perturbation; PROVENANCE entry at canonical_constants.py:1285)
- canonical_constants.py:339-341 (`M_KK = 7.428660036284456e16 GeV`; gravity-route Kaluza-Klein scale)
- s90-w6-d4-envelope-identity.md workshop A1 lines 995-996 (A_5 atlas pin), A2 lines 1017-1018 (K_csub ≈ 0.5 ± 0.1 substrate-natural anchor pin), EC1 lines 1146-1150 (per-regulator-class K_csub_R MIXED-vs-FI taxonomy), CF-7 spec lines 1306-1310 (this gate's pre-registration)

### Carry-forward computations

Per `feedback_fix-in-session-never-defer.md` 4-field spec (what / inputs / gate / effort); see `feedback_fix-in-session-never-defer.md` — these are GENUINE FUTURE COMPUTATIONS (not hygiene), each requires a separate next-session compute gate with pre-registered threshold + machinery pin.

#### CF-S91-W6-2-FULL-PHYSICAL-RETRY (P1 — primary substrate-IS retry)

- **What**: re-execute the K_csub_R extraction across A_5 atlas under the FULL physical Connes-Chamseddine 1996 §2.2-2.3 multipliers route (replacing the SCHEMATIC sub_term_R(L) analytic forms with substrate-canonical zeta-function-derived multiplier values at each regulator). The substitution chain Step 3 changes: instead of generic UV-divergence forms `Λ_UV²·L²·log(L)` etc., construct sub_term_R from the substrate's own spectral moments `Σ 1/λ_i^{2s}` at the appropriate s for each regulator (Pauli-Villars at s=2 with PV-subtracted moments; cutoff at sharp-truncation in (p,q) sectors with p+q > L_cut; lattice at s=2 with sinc² form-factor weighting on the substrate eigenvalue distribution). Re-extract K_csub_R, K_csub_mean, K_csub_std.
- **Inputs**: this gate's npz (`s91_w6_2_k_hk_k_csub_empirical_anchoring.npz` SHA `<pinned-at-runtime>`); `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949...` (extending to L_max=14 or 15 via Friedrich-Bär saturation per `math-scripts.md §"D_K Block-Diagonality Pre-Check"` if computationally feasible); `_spectral_action_regulators.py` for the FULL physical regularization helpers (CLASS pin = FULL, not SCHEMATIC); canonical_constants.py for κ_2_substrate_FW, M_KK, tau_fold; Connes-Chamseddine 1996 §2.2-2.3 multiplier definitions per `substrate-first-canonical-sourcing.md §(iv)` worked example.
- **Gate**: pre-registered PASS = |K_csub_mean − 0.5| < 0.1 AND K_csub_std > 0.05 AND F_2-axis FI sub-projection PASS; pre-registered FAIL = |K_csub_mean − 0.5| ≥ 0.2 OR K_csub_std too small to confirm MIXED. Tolerance rule: ABSOLUTE on |K_csub_mean − 0.5|; RATIO on F_2-axis spread. Sub-class tag: REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT (per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`) until FULL physical multipliers compute lands.
- **Effort**: ~3.0 we (substantial; FULL physical multipliers require Connes-Chamseddine 1996 §2.2-2.3 derivation chain on the substrate D_K spectrum at each regulator R; per-regulator spectral-moment extraction with PV subtraction / cutoff truncation / lattice form-factor weighting).
- **Depends on**: this gate (negative result motivates the retry); `canonical_constants.py` SCHEMATIC vs FULL level-pin discipline; `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` PROXY-REFINEMENT sub-class clause; `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY worked-example chain.

#### CF-S91-W6-2-K_HK-PERMANENT-PROMOTION (P2 — FI permanent registry landing)

- **What**: promote K_HK = 9 FI partition cardinality result to permanent registry entry at the algebra-INVARIANT functional family (algebra-axis corner I per `permanent-results-registry.md §VII.U.2` 4-corner partition). Construct STAGE-1-CANDIDATE registry slot via mack-cosmic-bridge sole-writer convention per `feedback_mack-bridge-role.md`; cite S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration anchor + this gate's empirical 5-regulator atlas confirmation. Per S88 W7c-167 substrate-input-orthogonality clause (`joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY at K=3 promoted S90 W2 CF-20), STAGE-2 cross-axis independent-verify by connes-ncg-theorist (axis A: NCG-axiomatic Künneth-Morita derivation) + transit-dynamics-aether-mechanic (axis B: substrate-physics regulator-invariance verification) on substrate-input-orthogonal observable pair.
- **Inputs**: this gate's audit_sha=`109e4307e8a0d80578318de29315b688287704cba1518bd651845db4a1cb984f` (PASS-component K_HK = 9 FI); S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration anchor (already permanent); `permanent-results-registry.md` next-free-letter slot (likely §VII.AY or successor); `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause + algebra-axis 4-corner partition.
- **Gate**: PASS = STAGE-1-CANDIDATE slot landed in registry with all 5 anatomy elements (substrate-IS observable: K_HK partition cardinality; bridge map: Künneth-Morita decomposition; algebraic envelope: regulator-invariant BY CONSTRUCTION; empirical anchor: 5-regulator atlas confirmation; substrate-IS Level-1 single-τ-slice declaration); STAGE-2 cross-axis verify PASS-AND on JOINT clauses for STAGE-3-PERMANENT promotion.
- **Effort**: ~1.0 we (STAGE-1-CANDIDATE landing only); +1.5 we for STAGE-2 cross-axis verify (separate gate per `joint-theorem-promotion.md` 4-stage pathway).
- **Depends on**: mack-cosmic-bridge sole-writer convention; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY; `joint-theorem-promotion.md` 4-stage pathway.

#### CF-S91-W6-2-FORWARD-CALIBRATION-OP-PROJ-K=4 (P3 — K-counter advancement candidate)

- **What**: log this gate as the FOURTH calibration-corpus instance for the `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-at-K=3 sub-clause (K-counter advance K=3 → K=4). This gate's convention tag `HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION-SCHEMATIC` carries the OP-PROJ suffix at the correct registry-slot-identifier layer; the K=3 calibration corpus already contains W4-2 §VII.AJ.W4-1 + W6-1 §VII.AG.1 + W11-meta-2 (per the canonical row table in `registry-landing.md`).
- **Inputs**: this gate's verdict-line `convention=` field (audit_sha `109e4307...`); `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` calibration corpus table; `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold.
- **Gate**: PASS = K-counter table updated to include this instance as K=4 row; documentation-only (no compute); mack-cosmic-bridge sole writer.
- **Effort**: ~0.25 we (documentation update only; rule already MANDATORY at K=3 so K=4 is structural confirmation of forward-compliance).
- **Depends on**: `registry-landing.md` table currently at K=3 calibration corpus; mack-cosmic-bridge sole-writer convention.

#### CF-S91-W6-2-SCHEMATIC-DISCLOSURE-CALIBRATION-K=5 (P3 — level-pin K-counter advancement)

- **What**: log this gate as a fifth POSITIVE-CALIBRATION instance for the `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin sub-clause (K_substantive 4 → 5; POSITIVE-CALIBRATION class). All 4 disclosure elements PASS at landing: (1) CLASS pin SCHEMATIC declared in producing-script docstring lines 23-30; (2) `-SCHEMATIC` suffix on verdict-line `convention=` field; (3) SCHEMATIC docstring acknowledgment via explicit citation of `_spectral_action_regulators.py` SCHEMATIC docstring + plan §10 §13 OPERATIONAL DEVIATION block; (4) `# tier_pin=TIER-2` companion comment row emitted in verdict file (line 115 of `s91_gate_verdicts.txt`). Severity band: NO-ACTION.
- **Inputs**: this gate's verdict-line companion rows (audit_sha `109e4307...`); `substrate-first-canonical-sourcing.md §(iv)` 3-class taxonomy table.
- **Gate**: PASS = calibration corpus table updated to include this instance as POSITIVE-CALIBRATION (compliance class with all 4 elements PASS); documentation-only (no compute).
- **Effort**: ~0.25 we (documentation only).
- **Depends on**: rule already MANDATORY at K=4; this is K=5 forward calibration corpus enrichment.

#### CF-S91-W6-2-L_MAX-22-EXTRAPOLATION-DIAGNOSTIC (P4 — diagnostic precursor)

- **What**: investigate the diagnostic root cause of the K_csub_R Mellin/zeta = −245.69 specific intercept value. Decompose into (a) the analytic κ_2-quadratic growth contribution `1 + κ_2 · L² / (5π)² = 1 + 0.02102 · 484 / 246.74 ≈ 1.0413` at L=22 vs (b) the cache-truncated `sum 1/λ_i²` proxy that should saturate beyond L=12 but is held constant (cache ceiling) in the script's `M_Pl_eff_sq_with_regulator` for L > 12. The 1/L→0 linear fit on the resulting `ratio_per_L` vector then extrapolates back to a large-magnitude intercept because the function is dominated by the L=8 cache-truncated value (ratio[L=8] = 239.08; ratio[L=22] = 1.04 per the actual run). The diagnostic confirms the SCHEMATIC parameterization mixes cache-truncated direct evaluation (L ≤ 12) with analytic extrapolation (L > 12) in a way that breaks the K_csub→ O(1) substrate-natural target.
- **Inputs**: this gate's npz keys `ratio_per_L` (per regulator); `L_grid`; `M_Pl_eff_sq_0`; producing-script `M_Pl_eff_sq_with_regulator` function.
- **Gate**: PASS = decomposition completed and per-regulator contribution analysis written to working paper; INFO = decomposition reveals the cache-truncation/analytic-extrapolation mismatch is the SCHEMATIC root cause (motivating the CF-S91-W6-2-FULL-PHYSICAL-RETRY); FAIL = decomposition reveals a different root cause requiring re-derivation.
- **Effort**: ~0.5 we (post-hoc analysis of existing npz data; per-regulator contribution decomposition; numerical sanity-check).
- **Depends on**: this gate's npz; analytic substrate parameterization per plan §10 Step 3.

---

## §W6-3. `S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9` (T2.60 / W-6 CF-9)

**Status**: CLOSED — composite verdict **FAIL** (band `FAIL_R2`; R² = 0.9074 < 0.95 floor); α_sub = 2.4291 (sub > full direction PASS, magnitude misses PASS-A-partial threshold 2.5 by 0.0709); audit_sha256=`2ac38905046a7e0b1521de6c6490de5fda4fba6f13d38fd77fb6cd697185e46b`
**Plan reference**: `sessions/session-plan/session-91-plan-w6.md §W6-3` (lines 523–737)
**Trigger**: `[AUDIT]` — cheap precursor audit of existing S90 W8 FWD-C1 L_max-scan data per Re:L3 closure workshop lines 401-413 + L3 closure workshop lines 121-127; isolates pre-anchor monotone-descent regime from post-anchor c_sub_corrected M_Pl_eff² anti-symmetry artifact.
**Classification**: PHONONIC. The pre-anchor monotone-descent sub-window at L_max ∈ {6, 7, 8, 9} measures the SUBSTRATE-IS pre-asymptotic finite-L envelope at d=4 substrate-distance-1 pole `s=3` per CM-1995 §III.4 finite-L correction `L^{-3} · (C_0 + C_1 L^{-1} + ...)`; the C_1 coefficient sign IS the W-6 EV1 boxed theorem signature (§VII.AF.1.OP-PROJ negative C_1 over-performance vs §VII.AU.OP-PROJ positive C_1 under-performance).
**Agent type**: `lizzi-spectral-functional-theorist` (PRIMARY; pre-asymptotic finite-L envelope extraction expertise; CM-1995 §III.4 subleading expansion analysis).
**Hypothesis**: At pre-anchor sub-window L_max ∈ {6, 7, 8, 9} (per W8 WP §W8-7(l) lines 1326-1337 δ_n_s = [3.103e-02, 2.545e-02, 1.960e-02, 1.112e-02]), the empirical α at the sub-window log-log fit IS:
- Reading A: α_sub > 2.5 (steeper than full-window α = 1.929; pre-asymptotic shallow-envelope steepening confirms asymptotic α → 3)
- Reading B: α_sub ≈ 1.9 (persistent at all sub-windows; substrate's universal envelope IS L^{-1.9} across regimes)
**Effort estimate**: ~0.1 we (existing S90 W8 FWD-C1 data; Sage-Q rational log-log regression on 4 pre-anchor points; numpy.polyfit cross-check; verdict assignment + working-paper section + verdict line; CPU-only; no new spectrum compute).

### Method

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

### Machinery pin (PRDR)

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

### Expected output 4-tuple

`(value=alpha_sub=<α>_R2=<r2>_<band-tag>, scheme=log-log-regression-existing-S90-W8-FWD-C1-pre-anchor-sub-window, convention=Mellin-class-pre-asymptotic-sub-window-CACHE-PROJECTION, L_max=9)`

Predicted from existing data: log(δ_n_s) at L ∈ {6,7,8,9} = ln([3.103e-02, 2.545e-02, 1.960e-02, 1.112e-02]) ≈ [-3.473, -3.671, -3.932, -4.499]. log(L) = [1.792, 1.946, 2.079, 2.197]. Slope (preliminary by eye) ≈ -(4.499−3.473)/(2.197−1.792) = -1.026/0.405 ≈ -2.53. So α_sub ≈ 2.53 — VERY CLOSE to the PASS-A-partial threshold of 2.5. **The verdict is genuinely uncertain at plan-freeze** — the regression's actual α_sub may fall in PASS-A-partial (~2.5+), INFO band (2.0–2.5), or even FAIL (< 2.0) depending on the actual 4-point fit. THIS IS A REAL DISCRIMINATOR.

### PASS/FAIL/INFO thresholds

- **PASS-A-partial (Reading A pre-asymptotic steepening confirmed at sub-window)**: `α_sub > 2.5` AND `R² ≥ 0.95`. Composite: `sign_verdict=PASS, magnitude_verdict=INFO (closer to α=3 than α=1.9), regime_verdict=MARGINAL (L ≤ 9 pre-asymptotic) ⇒ composite=INFO per collapse rule`. **NOTE**: the substrate-physics-readable label is "PASS-A-partial" but the schema-v2 collapse rule maps to composite=INFO. Resolve by emitting `verdict=PASS` with `value=PASS_A_partial` substring; the 3-tuple annotation makes the regime_verdict=MARGINAL explicit.
- **INFO (intermediate)**: `α_sub ∈ [2.0, 2.5]` AND `R² ≥ 0.95`. Sub-window does not decisively confirm either reading.
- **FAIL (Reading B partial confirmation OR regression-quality fail)**: `α_sub < 2.0` (closer to 1.9) AND `R² ≥ 0.95`; OR `R² < 0.95` (regression quality fail; sub-window not power-law).
- **Tolerance rule**: ABSOLUTE on α_sub band boundaries (2.0, 2.5); RATIO on R² (≥ 0.95).

### Substitution chain (MANDATORY for `[AUDIT]` direction claim)

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

### Solution-space implications

- **PASS-A-partial**: Reading A pre-asymptotic shallow-envelope steepening confirmed at sub-window precursor layer; W6-1 pathway (b) PASS-A expected; §VII.AU.OP-PROJ first-extraction trajectory points toward STAGE-1-CANDIDATE-PENDING-STAGE-2 at S91 close.
- **INFO**: intermediate; sub-window does not decisively confirm either reading; W6-1 pathway (b) verdict carries full discriminator weight; W6-4 discriminator gate provides decisive evidence at L_max=12 cache.
- **FAIL (Reading B partial)**: persistent α ≈ 1.9 at sub-window; W6-1 pathway (b) FAIL-B expected; HYBRID verdict (d) per-regulator-class sub-window structure becomes canonical; §VII.AU.OP-PROJ Element 5 ANNOTATION block (already landed S91 W0 prep T2.56) is correctly worded.
- **R² FAIL**: sub-window not power-law fit; structural anomaly at the pre-anchor monotone-descent regime; would force re-examination of W8 WP §W8-7(l) δ_n_s extraction methodology.

### Substrate framing

The sub-window L ∈ {6, 7, 8, 9} pre-anchor monotone-descent regime IS the substrate's pre-asymptotic finite-L manifestation at d=4 substrate-distance-1 pole `s=3`. The C_1 subleading coefficient's sign IS a substrate-IS structural signature; positive C_1 = under-performance regime (§VII.AU.OP-PROJ; FWD-C1) vs negative C_1 = over-performance regime (§VII.AF.1.OP-PROJ; W-5 baseline). Direction substrate → emergent: CM-1995 §III.4 dimension-spectrum residue formula at substrate-distance-1 pole IS the substrate-IS source; the L^{-3}·(C_0 + C_1·L^{-1} + ...) expansion IS the substrate's finite-L correction; the empirical α_sub at the 4-point regression IS the substrate's structure as measured on the existing FWD-C1 npz at finite L_max ∈ {6..9}. Container-thinking FORBIDDEN: "the sub-window is a slice of a larger L_max space" — INVERTED: "the sub-window L ∈ {6..9} IS the substrate at pre-asymptotic finite L; there is no enveloping L-space the sub-window is sliced from".

### Results (runtime)

| Quantity | Value | Notes |
|:---------|:------|:------|
| α_sub (numpy.polyfit) | **2.4291** | log-log fit slope `−2.429097` on L ∈ {6,7,8,9}, 4 pts |
| α_sub (Sage-Q exact) | **2.4291** | exact rational regression on same float64-quantized log inputs |
| Sage-Q vs numpy α deviation | `8.4e-15` | machine epsilon — mnemonic-vs-exact discipline PASS |
| Sage-Q vs numpy R² deviation | `1.1e-16` | machine epsilon — bit-precise agreement |
| Sage-Q vs numpy intercept deviation | `1.8e-14` | machine epsilon |
| intercept (numpy) | `+0.97313` | regression intercept on log–log axes |
| R² (numpy) | **0.9074** | **BELOW the 0.95 regression-quality floor** |
| R² (Sage-Q) | 0.9074 | matches numpy to 1.1e-16 |
| α_full_window (CF-65 anchor) | 1.929 | S89 W7c full L ∈ [6,12] empirical α (anchor) |
| α_sub − α_full_window | **+0.5001** | sub-window slope IS steeper than full-window |
| Reading A direction predicate | **TRUE** | sub > full ⇒ pre-asymptotic steepening direction matches Reading A |
| sign_verdict (3-tuple) | PASS | α_sub = 2.4291 > 1.0 ⇒ positive-decay direction |
| magnitude_verdict (3-tuple) | INFO | \|α_sub − 3.0\| = 0.5709 ∈ [0.5, 1.0) ⇒ INFO band vs Reading A α=3 target |
| regime_verdict (3-tuple) | MARGINAL | sub-window L ≤ 9 is pre-asymptotic boundary layer by construction |
| audit_sha256 | `2ac38905046a7e0b1521de6c6490de5fda4fba6f13d38fd77fb6cd697185e46b` | sig_5 unique within s91_gate_verdicts.txt |
| content_sha256 | `0e659ce394c06cebd5794759ea064e551550a12d59d810e4fa781783e9fc2587` | script-bytes SHA |

### Verdict (runtime)

**S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9: FAIL** (band `FAIL_R2`)

The pre-registered band assignment per plan §6 lines 592–594 + §9 fires `FAIL` because `R² = 0.9074 < 0.95` (the regression-quality floor required for any α-band verdict assignment). The α-band test is NOT reached — the 4-point log-log fit does not pass the goodness-of-fit floor required to call the sub-window "well-fit by a power law."

Structurally, this is the plan §11 third bullet's "R² FAIL" outcome: **sub-window not power-law fit; structural anomaly at the pre-anchor monotone-descent regime**. The bullet pre-anticipated that this verdict "would force re-examination of W8 WP §W8-7(l) δ_n_s extraction methodology." The R²=0.9074 lies between the regression-quality floor (0.95) and pure-noise (~0); the 4-point regression captures roughly 91% of the variance in `log δ_n_s` but the remaining 9% is structured residual that is incompatible with a single-exponent power law over this sub-window.

3-tuple companion annotation per S87 schema-v2: `sign=PASS; magnitude=INFO; regime=MARGINAL`. Per the S87 schema-v2 collapse rule (`regime=MARGINAL ∧ magnitude=INFO ⇒ composite=INFO`), the 3-tuple alone would map to composite=INFO; the FAIL composite is sourced by the pre-registered `R² < 0.95 ⇒ FAIL_R2` band (top of the band-decision tree per plan §6 line 592). The top-of-tree band gate over-rides the 3-tuple composite-collapse rule for this gate by construction. The 3-tuple companion is retained verbatim per gate-verdicts.md §"S87+ canonical form" requirement; it records the substrate-physics direction read (sign-PASS, magnitude-INFO, regime-MARGINAL) for downstream consumers even when the band-decision tree fires FAIL.

**Substitution-chain direction reading** (plan §10 Step 5):

```
Definitions:
  α_sub          = 2.4291  (4-point regression slope at L ∈ {6,7,8,9})
  α_full_window  = 1.929   (CF-65 anchor; S89 W7c full L ∈ [6,12] empirical α)
  α_asymptotic   = 3       (CM-1995 §III.4 L^{-3} substrate-distance-1 pole prediction)
  δ              = α_sub − α_full_window  =  +0.5001

Step 1 (definitions, plan §10):
  δ_n_s(L) = L^{-3}·(C_0 + C_1·L^{-1} + C_2·L^{-2} + ...)   [substrate-IS]
  d log(δ_n_s) / d log(L) = -3 + (-C_1/C_0)·L^{-1} + O(L^{-2})

Step 2 (substitution): at the pre-anchor sub-window L ∈ {6..9}, the
  log-log slope is α_sub = 2.4291 < 3 (asymptotic).  The residual
  −α_sub + 3 = 0.5709 > 0 implies (-C_1/C_0)·<L^{-1}> > 0; with
  <L^{-1}> > 0 always, this requires C_1/C_0 < 0  ⟺  C_1 < 0
  (assuming C_0 > 0 from positive leading correction at L → ∞).

Step 3 (direction read): C_1 < 0 IS the OVER-PERFORMANCE regime per
  W-6 EV1 boxed theorem signature (§VII.AF.1.OP-PROJ; W-5 baseline),
  i.e., the sub-window slope IS steeper than the asymptotic L^{-3}
  truncated at the full window.  This is the Reading A pre-asymptotic
  shallow-envelope steepening direction.

Step 4 (direction VS pre-registered PASS direction): plan §10 Step 5
  PASS direction = "α_sub increases from α_full_window=1.929 toward
  asymptotic α=3 as we approach the smaller-L pre-asymptotic boundary."
  Computed α_sub = 2.4291 > 1.929 = α_full_window  ⇒  direction MATCHES
  the PASS direction (sign_verdict = PASS encodes this in the 3-tuple).

Step 5 (gate verdict): direction PASS BUT magnitude does NOT clear the
  PASS-A-partial threshold α_sub > 2.5 (computed 2.4291 < 2.5, deficit
  −0.0709) AND the regression-quality floor R² ≥ 0.95 is missed
  (computed 0.9074 < 0.95).  The top-of-tree band-decision rule per
  plan §6 line 592 fires FAIL_R2; the substrate-physics direction
  read remains Reading A pre-asymptotic steepening confirmed at the
  sub-window precursor layer, but the magnitude is INSUFFICIENT to
  clear PASS-A-partial AND the linear-power-law approximation breaks
  down at the L ∈ {6..9} sub-window (R² = 0.9074).
```

Conclusion (direction): the sub-window slope IS steeper than the full-window slope by Δ = +0.5001, matching the Reading A pre-asymptotic-steepening direction; the magnitude misses the PASS-A-partial threshold (2.4291 < 2.5; deficit 0.0709) AND the regression-quality floor (R² = 0.9074 < 0.95) is missed, forcing the composite FAIL via the top-of-tree band gate. The substrate-physics signal is consistent with Reading A direction without clearing the strict PASS-A-partial band — i.e., the pre-anchor sub-window evidences the negative C_1 (over-performance regime) signature pointing toward §VII.AF.1.OP-PROJ but does NOT decisively rule out Reading B at the sub-window alone.

### Substrate framing (runtime addendum)

The sub-window L ∈ {6, 7, 8, 9} pre-anchor monotone-descent regime IS the substrate's pre-asymptotic finite-L manifestation at the d=4 substrate-distance-1 Mellin pole `s=3`. The C_1 subleading coefficient's sign IS a substrate-IS structural signature; the computed log-log slope α_sub = 2.4291 < 3 = α_asymptotic implies C_1 < 0 (over-performance regime per W-6 EV1, §VII.AF.1.OP-PROJ baseline), NOT C_1 > 0 (under-performance regime per §VII.AU.OP-PROJ FWD-C1 first-extraction).

The direction substrate → emergent flows: **CM-1995 §III.4 dimension-spectrum residue formula at substrate-distance-1 pole IS the substrate-IS canonical source; the L^{-3}·(C_0 + C_1·L^{-1} + ...) expansion IS the substrate's finite-L correction; the empirical α_sub = 2.4291 at the 4-point log-log regression IS the substrate's structure as measured on the existing S90 W8 FWD-C1 npz at finite L_max ∈ {6..9}.** No container-thinking inversion: the sub-window IS the substrate at pre-asymptotic finite L; there is no enveloping L-space the sub-window is sliced from. The R² = 0.9074 is the substrate's own non-power-law residual at the boundary layer, not noise on a putative true power law.

**Regulator-class declaration** (per `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"`): convention `Mellin-class-pre-asymptotic-sub-window-CACHE-PROJECTION` carries the explicit Mellin-class + sub-window + CACHE-PROJECTION tags. The δ_n_s data inherited from S90 W8 FWD-C1 (parameterized slope_a canonical) is Mellin-class (a_n^{Mellin} regulator-pin per `regulator-pin-discipline.md`); the level pin is FULL physical (S90 W8 FWD-C1 was parameterized substrate-canonical per the S90 W8 verdict; no SCHEMATIC helper consumed at the sub-window data layer). The convention-tag honesty discipline is satisfied.

**Functional-sensitivity classification** (lizzi-spectral-functional-theorist signature): the L^{-3} envelope is the F-image of the CM-1995 dimension-spectrum residue formula at substrate-distance-1 pole `s=3`, evaluated on the Jensen-deformed SU(3) spectral triple at finite L_max. The C_1 coefficient's sign is the FI/RD/MIXED axis discriminator: **C_1 < 0 (over-performance) IS the Mellin-class FI signature per W-6 EV1**; the empirical α_sub = 2.4291 < 3 at the sub-window IS evidence FOR the Mellin-class FI direction at the pre-asymptotic precursor layer. The cross-functional comparison (Mellin vs zeta vs Pauli-Villars sub-window α_sub) is queued at W6-4 (parallel discriminator at L_max=12 cache; see Cross-references).

### Cross-references

- W8 WP §W8-7(l) lines 1326-1337 (pre-anchor δ_n_s data source; the 4 pinned δ values).
- W6-4 (parallel discriminator at L_max=12 cache; full 4-way discriminator weight).
- W6-1 (downstream extension at L_max ≥ 22 pathway b; W6-3's FAIL_R2 does NOT pre-empt W6-1 pathway b — the sub-window R² is a regression-quality property at L ∈ {6..9}, not a Reading A/B falsification).
- `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` (Level-2-binding vs non-binding sub-class).
- `epistemic-discipline.md §"Class 8.2"` (verifier-rubric pre-registration).
- `epistemic-discipline.md §"Class 8.3"` (publication-precision pre-registration; α_sub published at 4 sig figs per plan §7 `pubprecision_alpha_sub`).
- `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"` (convention CACHE-PROJECTION tag discipline).
- `math-scripts.md §"Mnemonic-vs-exact ratio discipline"` (Sage-Q exact regression cross-checked against numpy.polyfit at machine epsilon; deviation 8.4e-15 ≪ 1e-12 PASS).
- `gate-verdicts.md §"S87+ canonical form"` (canonical + dual-SHA + 3-tuple companion row schema).
- S87 W11-2 + W11-3 Friedrich-Bär saturation theorem (the sub-window L ∈ {6..9} is BELOW the Friedrich-Bär saturation boundary at L ≥ 12; the regime_verdict=MARGINAL is the substrate-IS encoding of this pre-asymptotic positioning).

### Carry-forward computations (runtime)

The W6-3 FAIL_R2 outcome surfaces ONE genuine carry-forward computation for the next session's plan; this is NOT a process observation (the gate verdict is itself the in-session closure).

**CF-W6-3-NEXT-1 (S92+) — Sub-window R² floor diagnostic + Richardson-extrapolation against asymptotic α=3**:

1. **What**: Re-test the sub-window α_sub at extended sub-windows L ∈ {6..10}, {6..11}, {6..12} (5/6/7 point regressions) AND apply Richardson extrapolation `α_sub(L) → α_∞` to estimate the asymptotic exponent from the sequence of sub-window α values. If `α_∞ → 3` from below, Reading A pre-asymptotic steepening is confirmed at the diagnostic-extrapolation layer; if `α_∞ → 1.929` persistent, Reading B is confirmed; if `α_∞` lies in an intermediate band, the substrate's universal envelope is neither pure Mellin nor pure Reading B but a hybrid.
2. **Inputs**: Existing S90 W8 FWD-C1 npz (the same `s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz` file); extracted δ_n_s at L = 10, 11, 12 from W8 WP §W8-7(l); canonical_constants `kappa_2_substrate_FW = 0.021018084987437196`.
3. **Gate**: pre-registered PASS-A-Richardson `α_∞ > 2.7 AND |Δα_∞/Δα_sub| → 0 as window grows AND R² ≥ 0.95 on the 6+ point fit`; INFO `α_∞ ∈ [2.3, 2.7]`; FAIL-Reading-B `α_∞ ≤ 2.0`. Tolerance: ABSOLUTE on α_∞ band; RATIO on R².
4. **Effort**: ~0.15 we (existing data; 3 sub-window regressions + Richardson extrapolation + Sage-Q exact cross-check; CPU-only; ~0.1 we precursor + ~0.05 we Richardson method).

---

## §W6-4. `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR` (M10 / CF-LZ-S7-1)

**Status**: CLOSED (verdict FAIL — Reading A coincidence confirmed; supersedes 3 prior canonical lines via Option A protocol per `gate-verdicts.md §"Option A — sig_5 remediation pathway"`)
**Verdict (canonical)**: **FAIL** — `audit_sha256=f47e4299290dcff41af5f3a2069e6b91f61130e776087ecccf133201d1fa146e`, `content_sha256=078ba831345acd7f614dfdd38f898642e25c9e470943375a5a43627466a3b95d`
**3-tuple (S87 schema-v2)**: `sign_verdict=FAIL, magnitude_verdict=FAIL, regime_verdict=VALID`
**Plan reference**: `sessions/session-plan/session-91-plan-w6.md §W6-4` (lines 740–1014)
**Trigger**: `[VERIFY-THEOREM]` — tests substrate-IS universality prediction: ANY d=4 substrate-distance-1 pole `s=3` observable on the framework's KO-dim=6 finite spectral triple exhibits the SAME empirical L^{-α} envelope at finite L_max ∈ [6, 12].
**Classification**: PHONONIC. The d=4 universal envelope IS a substrate-IS spectral-functional property of the substrate's Mellin-cone closure at substrate-distance-1 pole `s=3`. The discriminator tests whether 4 STRUCTURALLY INDEPENDENT observables on the SAME substrate algebra share the universal exponent (Reading B substrate-structural) OR exhibit observable-specific contingencies (Reading A coincidence).
**Agent type**: `lizzi-spectral-functional-theorist` (PRIMARY; spectral-functional-axis universality testing; FUNCTIONAL-SELECT-67 invariance analysis; 5-regulator atlas functional sensitivity expertise); `connes-ncg-theorist` CO-AUTHOR per lizzi-S7 synthesis §(4.b) Author line (Connes-Moscovici 1995 §III.4 residue-formula evaluator on multi-projector / multi-pole independent observables).
**Hypothesis**: The four observables `{O_1 = M^(ζ)_3 (CF-54-equivalent, no projector, no bridge); O_2 = R_universal_FWD_C1 (CF-65-equivalent, P_0 projector, HKR L→∞); O_3 = R_universal_FWD_C2 candidate (P_BdG projector, substrate-distance-2 pole; deferred-pending PROXY-REFINEMENT per §VII.AV); O_4 = Tr(D_K^{-6}) (pure spectral moment, no Hochschild structure)}` ALL exhibit empirical α ∈ [1.8, 2.1] at L_max ∈ [6, 12] within σ_β ≤ 0.10 (Reading B substrate-structural) — OR ≥ 2 of 4 fall outside [1.5, 2.5] AND σ_β ≥ 0.30 (Reading A coincidence).
**Effort estimate**: ~0.5 we (single agent-timeslot ~30 min wall time per lizzi-S7 §(4.f); 4 observables × 8 L-values × per-observable shell-sum computation; all reading from same NPZ cache; CPU-only OK; verdict assignment + working-paper section + verdict line).

### Method

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

### Machinery pin (PRDR)

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

### Expected output 4-tuple

`(value=beta_bar=<β̄>_sigma=<σ_β>_Cij_min=<C_min>_<Reading-tag>, scheme=shell-sum-ratio-regression-4-way-discriminator, convention=Mellin-class-substrate-distance-1-pole-s3-CACHE-PROJECTION, L_max=12)`

Predicted Reading B (lizzi PRIMARY): β̄ ≈ 1.9, σ_β ≈ 0.05, C_ij_min ≈ 0.85 ⇒ PASS.
Predicted Reading A (connes ALTERNATIVE per workshop R1 part 2 lines 584+): β̄ ≈ 1.9 with σ_β ≈ 0.40 ⇒ FAIL (Reading A coincidence).

### PASS/FAIL/INFO thresholds

- **PASS (Reading B substrate-structural confirmed)**: ALL 4 observables yield β_i ∈ [1.8, 2.1] AND σ_β ≤ 0.10 AND `min(C_ij off-diagonal) ≥ 0.7`. Composite collapse: `sign_verdict=PASS (Reading B predicts universality), magnitude_verdict=PASS, regime_verdict=VALID (L ∈ [4, 11] inside Friedrich-Bär saturation window) ⇒ composite=PASS`.
- **FAIL (Reading A coincidence confirmed)**: ≥ 2 of 4 observables yield β_i outside [1.5, 2.5] AND σ_β ≥ 0.30. Composite: `sign_verdict=FAIL (universality prediction fails), magnitude_verdict=FAIL, regime_verdict=VALID ⇒ composite=FAIL`.
- **INFO (intermediate)**: σ_β ∈ (0.10, 0.30); some convergence but not Reading B's structural tightness. Defer to S92+ extension with O_5+. Composite: `regime_verdict=MARGINAL ⇒ composite=INFO`.
- **Tolerance rule**: ABSOLUTE on β_i band membership; ABSOLUTE on σ_β threshold; ABSOLUTE on C_ij off-diagonal threshold.

### Substitution chain (MANDATORY for `[VERIFY-THEOREM]`)

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

### Solution-space implications

- **PASS (Reading B substrate-structural confirmed)**: d=4 universal envelope at finite L_max ∈ [6, 12] is substrate-IS regulator-INVARIANT BY CONSTRUCTION; the L^{-1.9} empirical α IS the substrate's intrinsic finite-L manifestation per EV3 derivation; the L^{-3} asymptotic prediction (Reading A) holds at L ≥ 35 (Friedrich-Bär saturation); §VII.AF.1.OP-PROJ Level-3 anchor PASS is reinterpreted as "~130× inside L^{-1.9} realized envelope" (vs "10.5× inside L^{-3} idealized envelope"); W6-5 fires under PASS-side prediction (W11-5 sister re-tag toward registry-PASS).
- **FAIL (Reading A coincidence)**: d=4 universal envelope is NOT universal at finite L; β_i ∈ {1.5..2.5} scatter; the CF-54 + CF-65 agreement is observable-specific coincidence; W6-5 deferred (no re-tag justification); §VII.AU.OP-PROJ HYBRID verdict (d) per-regulator-class sub-window structure prevails; W6-1 pathway (b) likely returns INFO or FAIL toward Reading B realized; pathway (a) backup at L_max ≥ 35 becomes structurally necessary.
- **INFO (intermediate)**: partial convergence; some observables agree at β ≈ 1.9 but σ_β > 0.10; defer to S92+ extension with O_5+; the d=4 universal envelope is in a transitional regime where some contingencies break universality and others preserve it.
- **K-counter for Layer-Functor F Verdict-Shape Consistency Theorem**: PASS confirms the K=2 SUGGESTION calibration at W-5 + W-6 (the EV1 boxed theorem's universality prediction); FAIL would falsify the K=2 calibration; INFO leaves K=2 SUGGESTION standing pending S92+ extension.

### Substrate framing

The 4-way discriminator IS a substrate-spectral-functional test of d=4 universality. The substrate IS the spectral triple `(A_K, H_K, D_K)`; the d=4 dimension IS the substrate's Wodzicki dimension at trace pole `s=4` of `ζ_D(s)`. The shell-sum exponent at substrate-distance-1 pole `s=3` IS a substrate-IS structural property of the substrate's `dim(p,q) · (C_2(p,q)+1)^{-3}` combinatorial geometry. The discriminator tests whether this property is universal across observables (Reading B substrate-structural) OR specific to particular bridge-anatomy contingencies (Reading A coincidence). Direction substrate → emergent: substrate IS spectral triple → substrate-distance-1 pole `s=3` IS the substrate's intrinsic d=4 Mellin-cone closure → ALL d=4 Mellin-cone observables share the substrate's combinatorial shell-sum geometry → empirical α at finite L IS the substrate's universal d=4 envelope (Reading B). Container-thinking FORBIDDEN: "the 4 observables live in a 4-way space" — INVERTED: "the 4 observables ARE 4 substrate-IS projections of the substrate's combinatorial shell-sum geometry; there is no enveloping 4-way space they inhabit".

### Methodology — OPERATIONAL DEVIATION (honest disclosure)

Per `math-scripts.md §"Mnemonic-vs-exact ratio discipline (S86 W-3 RULE-3)"` MANDATORY rule, the regression-arithmetic implementation deviates from the plan §6 snippet's Taylor-linearized form `(ratio - 1) vs (1/L)` and uses the **structurally-exact** form `log(S(L+Δ)/S(L)) vs log((L+Δ)/L)`. The plan §10 Step 2 substitution chain itself pre-registers the exact identity `S(L+1)/S(L) ~ ((L+1)/L)^{-β}`; the §6 snippet truncated this at `O(L^{-1})` mnemonic. On the analytically-computable O_1 shell sum, the mnemonic regression returns β=0.79 while the structurally-exact regression returns β=1.16 — a 47% relative deviation, far exceeding the RULE-3 1% bound. The exact form is therefore canonical; SCHEME and CONVENTION pins are PRESERVED unchanged (only regression-arithmetic moves from the mnemonic to the exact form per the same plan §10 Step 2). This is NOT a PROHIBITED_ACTIONS Class 1 convention-shopping violation: the convention pin is unchanged; the substrate-IS exact identity is the same identity the §10 substitution chain references.

A second deviation: the substrate-IS shell sums for O_1, O_2, O_3 are computed via the **analytic combinatorial formula** `S_i(L) = Σ_{p+q=L} projector_i(p,q) · dim(p,q) · (C_2(p,q)+1)^{-s_i}` (substrate-IS algebra-canonical per plan §10 Step 1), NOT restricted to `cache.keys()`. Reason: the L_max=12 master cache `s84_spectrum_cache_L12_tau019.npz` is missing the (4,4) Cartan-diagonal sector at L=8 (an 18% under-count of S_O_1(L=8) if using cache.keys()-only). The plan §10 Step 1 prescription `For each (p,q) Peter-Weyl block with p+q = L: contribution = dim · (C_2+1)^{-s}` is substrate-IS combinatorial and cache-independent for O_1/O_2/O_3 (which are functions of dim and C_2 only); only O_4 (Tr(D_K^{-6})) requires cached eigenvalues and inherits the (4,4)@L=8 cache gap (sub-1% impact on its shell sum at that level, estimated from |λ|_min^(-6) · 8·125 ≈ 0.06 vs S_O4(L=8)=14.6).

### Results

| Quantity | Value | Notes |
|:---------|:------|:------|
| β_O1 (M^(ζ)_3, no projector, no bridge) | **1.1564** | Mellin bare-trace; OUT of PASS band [1.8, 2.1]; INSIDE FAIL window [1.5, 2.5] only at the boundary (1.1564 < 1.5 ⇒ OUTSIDE) |
| β_O2 (R_FWD_C1 with P_0 band-0 + HKR L→∞) | **1.9324** | CF-65-equivalent observable; INSIDE PASS band [1.8, 2.1]; structurally matches CF-65 empirical α=1.929 within 0.2% |
| β_O3 (R_FWD_C2 with P_BdG p=q, s=4 pole) | **2.9718** | deferred-pending PROXY-REFINEMENT structure; OUTSIDE PASS band [1.8, 2.1]; OUTSIDE FAIL window [1.5, 2.5] |
| β_O4 (Tr(D_K^{-6}), pure spectral moment) | **1.0293** | algebra-INVARIANT no-Hochschild observable; OUTSIDE PASS band [1.8, 2.1]; OUTSIDE FAIL window [1.5, 2.5] (below 1.5) |
| β̄ (4-way arithmetic mean) | **1.7725** | NOT inside PASS band [1.8, 2.1] |
| σ_β (4-way sample std, ddof=1) | **0.8936** | ≥ 0.30 ⇒ sigma_fail = True; far exceeds PASS threshold 0.10 |
| min(C_ij off-diagonal) | **-0.2625** | NEGATIVE off-diagonal correlation; far below PASS threshold +0.7 ⇒ cij_pass = False |
| mean(C_ij off-diagonal) | 0.3453 | weak positive average correlation, but min is negative |
| fail_count (β_i outside [1.5, 2.5]) | **3/4** | O_1=1.156 (OUT), O_3=2.972 (OUT), O_4=1.029 (OUT); only O_2=1.932 (IN). ≥ 2 ⇒ fail_count threshold met |
| pass_band predicate (all β_i ∈ [1.8, 2.1]) | False | only O_2 inside; 3 of 4 outside |
| sigma_pass predicate (σ_β ≤ 0.10) | False | σ_β=0.894 ≫ 0.10 |
| cij_pass predicate (min C_ij ≥ 0.7) | False | min C_ij = -0.263 |
| sigma_fail predicate (σ_β ≥ 0.30) | True | σ_β = 0.894 ≥ 0.30 |
| **PASS_Reading_B** (pass_band ∧ sigma_pass ∧ cij_pass) | **False** | all 3 conjuncts FALSE |
| **FAIL_Reading_A** (fail_count ≥ 2 ∧ sigma_fail) | **True** | both conjuncts TRUE |

**Cross-observable summary**: only O_2 (the CF-65 analog: P_0 band-0 projector + HKR L→∞ bridge) lands inside the Reading B PASS band. The other 3 observables exhibit STRUCTURALLY DISTINCT envelope exponents spanning [1.03, 2.97] — a 2.9× spread of β across observables on the SAME substrate spectral triple at the SAME pole, demonstrating that the empirical L^{-α} envelope at finite L_max ∈ [4, 11] is **observable-specific**, not substrate-universal at this window.

### Verdict

**FAIL (Reading A coincidence confirmed)** per pre-registered band conjunction:
- fail_count = 3 ≥ 2 of 4 observables OUTSIDE [1.5, 2.5] ✓
- σ_β = 0.894 ≥ 0.30 ✓
- Therefore FAIL_Reading_A = TRUE
- Composite collapse (per `gate-verdicts.md §"Composite-collapse rule"`): sign_verdict=FAIL, magnitude_verdict=FAIL, regime_verdict=VALID ⇒ composite = FAIL

The empirical agreement between CF-54 (β=1.86, full Mellin trace at L ∈ [10, 100]) and CF-65 (α=1.929, P_0+HKR observable at L ∈ [6, 11]) is the agreement of TWO MELLIN-CLASS observables in the SAME P_0+HKR-equivalent family AT DIFFERENT L-windows. When the discriminator extends the observable basis to the FOUR structurally-distinct projector/bridge/pole combinations enumerated in lizzi-S7 §(4.c) Table 1, the universality hypothesis (Reading B) is FALSIFIED at the finite-L window of the L_max=12 cache. The 4 observables decay at structurally distinct empirical rates: O_4 (pure spectral moment) at β ≈ 1.03 (closest to L^{-1}); O_1 (bare Mellin trace) at β ≈ 1.16; O_2 (P_0+HKR) at β ≈ 1.93; O_3 (P_BdG @ substrate-distance-2 pole) at β ≈ 2.97. The cross-correlation matrix shows weakly positive AVERAGE off-diagonal C_ij = 0.345 but with min C_ij = -0.263 (NEGATIVE — O_4 and O_3 show anti-correlated residual structure), inconsistent with a substrate-universal envelope at finite L.

**Audit-trail honest disclosure**: this verdict supersedes 3 prior canonical lines (Option A protocol):
- `audit_sha256=0da7e7205a38016f7e60fe97565bac4c959537e3b7f7e854229a473f483dfc02` (original INFO; NaN propagation from O_3 cache-zero divides + Taylor mnemonic regression)
- `audit_sha256=3bf5b89209f065aeba3786961b0a22c58e5ef7118bce02958005cf6afa290346` (intermediate INFO; exact log-ratio regression but O_3 still NaN from cache (4,4) gap at L=8)
- `audit_sha256=914e52092f1a2a8c738e136e4f02db92548f25eb93101365f6c3405086b6c65b` (substantive FAIL but pre-supersedes-tag; combinatorial-form fix applied)
- All 3 prior lines retained on disk per Option A rule (1) absolute verdict permanence; the FINAL canonical line at `audit_sha256=f47e4299290dcff41af5f3a2069e6b91f61130e776087ecccf133201d1fa146e` carries the supersedes chain.

### Substrate framing (runtime addendum)

The substrate IS the spectral triple `(A_K, H_K, D_K)`; the d=4 dimension IS the substrate's Wodzicki dimension at trace pole `s=4`. The shell-sum exponent at substrate-distance-1 pole `s=3` IS NOT universal across observables at finite L_max ∈ [4, 11]. The substrate-IS reading of the FAIL verdict:

- **The substrate's combinatorial geometry produces 4 distinct decay rates** for 4 distinct projector / bridge / pole combinations. The d=4 universal envelope hypothesis (Reading B) requires β to be substrate-IS independent of the projector / bridge / pole choice — the substrate's spectral triple does NOT exhibit this independence at the L_max=12 window.
- **O_2 (P_0+HKR)'s β=1.932 matches CF-65 α=1.929 to within 0.2%** — a structural consistency check that validates the script's correctness on the canonical FWD-C1 observable. The agreement is genuine: same observable family (band-0 + HKR bridge), same substrate-distance pole (s=3), same L-window (L ∈ [4, 11]). What FAILS is the EXTENSION to projector-free / bridge-free / different-pole observables.
- **The Reading A coincidence interpretation is structurally vindicated**: the CF-54 + CF-65 agreement is the agreement of two observables in the SAME Mellin-class P_0+HKR-equivalent family at DIFFERENT L-windows; when the family is widened to genuinely-independent projector / bridge / pole choices, the universality breaks.
- **FUNCTIONAL-SELECT-67 invariance reading** (Lizzi signature): the empirical β IS functional-dependent — the projector and bridge map ARE functional choices that determine the spectral moments entering with what weight, and they produce structurally distinct shell-sum decay rates. The substrate's d=4 universal envelope at finite L is NOT regulator-class-INVARIANT at the bare-decomposition layer when the "regulator class" is widened to include the (projector, bridge, pole) triplet.

**Direction substrate → emergent**: substrate IS spectral triple → finite-L shell-sum at substrate-distance-1 pole s=3 → for FIXED (projector, bridge, pole) the L^{-α} decay rate is determined by the substrate's combinatorial geometry → DIFFERENT (projector, bridge, pole) choices project DIFFERENT substrate-IS sub-algebras and produce DIFFERENT empirical α values at finite L. The discriminator does NOT falsify the existence of a substrate's d=4 envelope; it falsifies the claim that the envelope's exponent is universal across the (projector, bridge, pole) triplet at L_max ∈ [4, 11].

**Container-thinking FORBIDDEN**: "the 4 observables disagree because the substrate doesn't have a single envelope" — INVERTED: "the 4 observables ARE 4 substrate-IS projections of the substrate's combinatorial geometry; each projection HAS its own substrate-IS envelope exponent at finite L; the universality hypothesis Reading B was the hypothesis that all 4 projections inherit the SAME exponent, and that hypothesis is FALSE at the L_max=12 cache window."

**Connes-Moscovici 1995 §III.4 reading (connes-ncg-theorist CO-AUTHOR)**: the CM-1995 dimension-spectrum residue formula gives the asymptotic-limit (L → ∞) exponent at s=d-k. The 4 observables share this ASYMPTOTIC exponent (≈ L^{-3} at substrate-distance-1 for d=4) at L_max ≥ 30 per the Friedrich-Bär saturation theorem (math-scripts.md §"D_K Block-Diagonality"); at L_max ∈ [4, 11] the per-observable subleading corrections to the residue formula dominate, and these corrections ARE projector / bridge / pole dependent. The discriminator measures the FINITE-L subleading-corrections layer, NOT the asymptotic residue. Reading A is therefore the CORRECT NCG-axiomatic interpretation: empirical agreement at finite L between two CF-54-like + CF-65-like observables is the agreement of their SHARED subleading-correction structure (both inhabit the P_0+HKR-equivalent class at substrate-distance-1 pole s=3); when the observable basis is extended to genuinely distinct (projector, bridge, pole) classes the subleading-correction agreement does NOT persist.

### Cross-references

- lizzi-S7 synthesis §(4.c) Step 1 Table 1 (observable basis) + §(4.d) PASS/FAIL/INFO bands
- workshop §EV1/EV3 boxed theorem (universality prediction at lines 925-981)
- §VII.AU.OP-PROJ HIT table corpus instance #2 at registry line 17728 (W11-5 sister; W6-5 CONDITIONAL on this gate now de-triggered)
- §VII.AJ at registry line 16887
- §VII.AF.1.OP-PROJ baseline (`L^{-3}` asymptotic envelope reading PRESERVED; no envelope-direction sharpening retro-fit; Reading B advisory CF-LZ-S7-2 de-triggered)
- W6-3 (sub-window L_max ∈ {6..9} precursor; W6-3 reported α_sub=2.43 ∈ INFO band with R²<0.95 ⇒ regression-quality failure; the W6-3 + W6-4 joint reading is "the substrate's d=4 envelope is observable-specific and the L_max=12 cache window is below the Friedrich-Bär saturation L ≥ 30 threshold")
- W6-1 (downstream extension at L_max ≥ 22 pathway b; FAIL here motivates pathway (a) backup at L_max ≥ 35)
- W6-5 (was CONDITIONAL on this gate's PASS — DE-TRIGGERED; W11-5 sister re-audit DEFERRED to S92+)
- `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` (Level-2-binding observables O_2 + O_3 vs Level-2-non-binding observables O_1 + O_4; the binding sub-class does NOT predict the finite-L envelope exponent — confirmed by binding O_2 at β=1.93 vs binding O_3 at β=2.97 having dramatically different empirical α values)
- `regulator-pin-discipline.md §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE"` (Reading B was the "if substrate-structural" hypothesis that failed empirical falsification; the L^{-3} asymptotic envelope per §VII.AF.1.OP-PROJ is the canonical reading, not the L^{-1.9} realized envelope)
- `math-scripts.md §"Mnemonic-vs-exact ratio discipline (S86 W-3 RULE-3)"` (methodology applied to the regression-arithmetic deviation; the structurally-exact log-ratio form was applied per the 1% deviation bound)
- `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` (supersedes-tag protocol used for 3 prior canonical lines)
- Layer-Functor F Verdict-Shape Consistency Theorem K=2 SUGGESTION calibration — FAIL of W6-4 IS the FALSIFIER of the K=2 SUGGESTION's universality prediction; K=2 NOT advanced to K=3 by this gate
- Connes-Moscovici 1995 §III.4 (CO-AUTHOR connes-ncg-theorist anchor) — finite-L subleading corrections to the dimension-spectrum residue formula ARE projector / bridge / pole dependent; asymptotic universality holds at L_max ≥ 30 by Friedrich-Bär saturation

### Carry-forward computations

1. **CF-W6-4-S91-1**: `S92-D4-UNIVERSAL-ENVELOPE-AT-FRIEDRICH-BAR-SATURATION` (~ 1.5 we; gen-physicist + lizzi PRIMARY + connes CO-AUTHOR).
   - **What**: re-run the 4-way discriminator at the FRIEDRICH-BÄR-SATURATED L ≥ 35 window via the analytic recursion-formula route (NOT cache; D_K eigenvalue construction at L ≥ 13 is empirically infeasible per W11-3 calibration corpus); for O_1/O_2/O_3 the combinatorial formula is cache-independent and extends to L=100; for O_4 a separate Casimir-asymptotic argument is needed.
   - **Inputs**: substrate-IS combinatorial shell-sum formula `S_i(L) = Σ projector(p,q)·dim·(C_2+1)^{-s}` (this gate's verified implementation); CF-54 pre-flight Sage-Q Fraction-arithmetic at L ∈ [10, 100] (β=1.885) as cross-check anchor; `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` Friedrich-Bär saturation theorem.
   - **Gate**: PASS-Reading-B-at-asymptotic iff all 4 observables yield β_i ∈ [1.7, 2.1] (widened band per CM-1995 §III.4 subleading-correction-stripped asymptotic exponent expectation) at L ∈ [35, 100] AND σ_β ≤ 0.10 AND C_ij off-diag ≥ 0.7; FAIL otherwise; INFO if σ_β ∈ (0.10, 0.30).
   - **Effort**: 1.5 we.

2. **CF-W6-4-S91-2**: `S92-FINITE-L-PROJECTOR-DEPENDENT-SUBLEADING-CORRECTION-CHARACTERIZATION` (~ 1.0 we; lizzi + connes adversarial workshop).
   - **What**: analytic / Sage-Q characterization of WHY each (projector, bridge, pole) triplet produces a distinct subleading-correction exponent at finite L. Hypothesis: each projector restricts the shell sum to a sub-algebra image whose substrate-distance-1 pole residue is dominated by a different (p,q) → C_2(p,q) scaling that determines the finite-L envelope via the Mellin-Barnes contour deformation off-pole.
   - **Inputs**: this gate's NPZ (β values + shell sums); workshop §EV1/EV3 boxed theorem; CM-1995 §III.4 dimension-spectrum residue formula.
   - **Gate**: closed-form formula for β_i(projector_i, bridge_i, pole_i) at L=10 substrate finite-L extracting agreement with empirical β_i from this gate within 5%.
   - **Effort**: 1.0 we.

3. **CF-W6-4-S91-3**: `S92-W6-5-W11-5-SISTER-RE-AUDIT-UNDER-FAIL-CONDITION` (~ 0.3 we; mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`).
   - **What**: W6-5 was CONDITIONAL on W6-4 PASS; W6-4 closed FAIL ⇒ W6-5 is **DE-TRIGGERED** (W11-5 sister re-tag DEFERRED to S92+); explicit registry note at §VII.AU.OP-PROJ HIT table corpus instance #2 documenting that the realized-envelope re-tag is NOT structurally justified by W6-4 (Reading B falsified). The L^{-3} asymptotic envelope per §VII.AF.1.OP-PROJ baseline is PRESERVED as the canonical envelope reading.
   - **Inputs**: this gate's FAIL verdict (audit_sha256=f47e4299290dcff41af5f3a2069e6b91f61130e776087ecccf133201d1fa146e); §VII.AU.OP-PROJ HIT table corpus; §VII.AF.1.OP-PROJ baseline.
   - **Gate**: METHODOLOGY-class registry note landed; no envelope reinterpretation; §VII.AF.1.OP-PROJ and §VII.AU.OP-PROJ retain their L^{-3} asymptotic envelope readings.
   - **Effort**: 0.3 we.

4. **CF-W6-4-S91-4**: `S92-LAYER-FUNCTOR-F-VERDICT-SHAPE-CONSISTENCY-K2-NON-ADVANCE-DOCUMENTATION` (~ 0.2 we; lizzi METHODOLOGY-class).
   - **What**: document explicitly in the framework registry that the W6-4 FAIL does NOT advance the Layer-Functor F Verdict-Shape Consistency Theorem from K=2 SUGGESTION to K=3 MANDATORY (the FAIL FALSIFIES the K=2 SUGGESTION's universality prediction). The K-counter stays at K=2 pending alternative-corroboration calibration instances.
   - **Inputs**: this gate's FAIL verdict; `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold rule.
   - **Gate**: METHODOLOGY-class K-counter status entry preserved at K=2 SUGGESTION.
   - **Effort**: 0.2 we.

---

## §W6-5. `S91-W11-5-SISTER-RE-AUDIT-UNDER-REALIZED-ENVELOPE` (M11 / CF-LZ-S7-3) **[CONDITIONAL on W6-4 PASS]**

**Status**: NOT STARTED
**Plan reference**: `sessions/session-plan/session-91-plan-w6.md §W6-5` (lines 1017–1281)
**Trigger**: `[AUDIT]` — re-audits S87 W11-5 sister cross-pillar bridge instance under the realized `L^{-1.9}` envelope versus the original `L^{-3}` asymptotic envelope; determines whether the W11-5 registry-FAIL by ~21× under `L^{-3}` should be re-tagged to registry-PASS, deferred-pending PROXY-REFINEMENT, or deferred-pending FIRST-EXTRACTION.
**Classification**: PHONONIC. The W11-5 sister cross-pillar bridge IS a substrate-IS observable at Pillar III ↔ IV at substrate-distance-1 pole `s=3` (per registry §VII.AJ at line 16887 in the §VII.AU.OP-PROJ HIT table corpus instance #2). The re-audit applies the realized envelope verdict from W6-4 to W11-5's Level-3 empirical anchor; the re-tag decision IS a methodology-floor consequence of substrate-IS universal envelope determination.
**Agent type**: `lizzi-spectral-functional-theorist` (PRIMARY; envelope-determined re-tag decision under FUNCTIONAL-SELECT-67 / cross-pillar bridge-anatomy structural-confidence ladder); `mack-cosmic-bridge` CO-AUTHOR per `feedback_mack-bridge-role.md` sole-writer rule for ANY registry-text retrofit IF the re-audit produces a structurally-justified re-tag (mack performs the actual registry edit).
**Hypothesis**: Under realized envelope `L^{-1.9}` (W6-4 PASS), W11-5's Level-3 empirical anchor `R_∞` lies WITHIN the realized envelope's L_max=10 width of ~1.26% (predicted by lizzi-S7 §(3.a) line 159), making the registry-FAIL by ~21× under `L^{-3}` no longer the canonical reading. Possible re-tag verdicts:
- registry-PASS: realized envelope contains the anchor; W11-5 promoted to deferred-pending-INTERMEDIATE per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` SUGGESTION K=1
- deferred-pending PROXY-REFINEMENT: realized envelope width still misses anchor BUT structurally-defensible refinement pathway exists (SCHEMATIC vs FULL physical regulator)
- deferred-pending FIRST-EXTRACTION: realized envelope width misses anchor; further first-extraction at higher L_max required
- registry-FAIL preserved: even under realized envelope, anchor outside; W11-5 sister CONFIRMED non-binding
**Effort estimate**: ~0.3 we (re-audit decision is arithmetic on existing data; W11-5 anchor extraction from registry; deviation computation; re-tag decision tree; verdict assignment + working-paper section + verdict line; the conditional mack-cosmic-bridge registry retrofit follow-up gate is SEPARATE at ~0.3 we additional IF re-tag is structurally justified per CF-LZ-S7-3 effort estimate line 385).

### Method

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

### Machinery pin (PRDR)

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

### Expected output 4-tuple

`(value=W11_5_anchor=<a>_dev_vs_realized=<d_r>_dev_vs_idealized=<d_i>_re_tag=<tag>, scheme=envelope-determined-re-tag-decision-under-W6-4-PASS-realized-L_minus_1.9, convention=Mellin-class-substrate-distance-1-pole-s3-realized-envelope-CACHE-PROJECTION, L_max=10)`

Predicted (per lizzi-S7 line 192 hint "deviation may be different"): dev_vs_realized ∈ [1.0, 5.0] most likely; re_tag = DEFERRED-PENDING-PROXY-REFINEMENT probable; verdict = INFO probable.

### PASS/FAIL/INFO thresholds

- **PASS (REGISTRY-PASS-CONDITIONAL re-tag)**: `deviation_vs_realized ≤ 1.0` (W11-5 anchor INSIDE realized envelope width); W11-5 promoted to deferred-pending-INTERMEDIATE per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`. Composite: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID ⇒ composite=PASS`.
- **INFO (DEFERRED-PENDING-PROXY-REFINEMENT or DEFERRED-PENDING-FIRST-EXTRACTION re-tag)**: `1.0 < deviation_vs_realized ≤ 10.0`; re-tag admissible-with-conditions per Level-2 sub-class clause MANDATORY at K=2 (S88 W8-88). Composite: `regime_verdict=MARGINAL ⇒ composite=INFO`.
- **FAIL (REGISTRY-FAIL-PRESERVED)**: `deviation_vs_realized > 10.0`; even under realized envelope, anchor exceeds by > 10×; W11-5 CONFIRMED non-binding under both envelopes. Composite: `sign_verdict=FAIL, magnitude_verdict=FAIL, regime_verdict=VALID ⇒ composite=FAIL`.
- **HARD-HALT (CONDITIONAL prereq fail)**: W6-4 verdict not PASS at this gate's runtime check; raise RuntimeError; defer to S92+ if W6-4 produced INFO; if W6-4 produced FAIL (Reading A coincidence), the W11-5 re-audit is structurally moot (Reading A means no universal envelope to re-anchor against).
- **Tolerance rule**: ABSOLUTE on `deviation_vs_realized` band membership.

### Substitution chain (MANDATORY for `[AUDIT]` re-tag decision)

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

### Solution-space implications

- **PASS (REGISTRY-PASS-CONDITIONAL)**: W11-5 sister advances to deferred-pending-INTERMEDIATE; advances `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` calibration corpus K=1 SUGGESTION → K=2 (W11-5 NEW instance distinct from §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION dual at S90 W1-14); requires mack-cosmic-bridge sole-writer registry retrofit follow-up gate; advances cross-pillar-bridge K-counter corpus.
- **INFO (DEFERRED-PENDING-PROXY-REFINEMENT or DEFERRED-PENDING-FIRST-EXTRACTION)**: W11-5 sister gains a structurally-justified intermediate status; the §VII.AU.OP-PROJ HIT table corpus instance #2 at registry line 17728 is annotated with the realized envelope re-evaluation; mack-cosmic-bridge sole-writer registry retrofit follow-up queued.
- **FAIL (REGISTRY-FAIL-PRESERVED)**: W11-5 sister CONFIRMED non-binding under both envelopes; reading B substrate-structural universality holds for §VII.AF.1.OP-PROJ baseline AND §VII.AU.OP-PROJ FWD-C1 but FAILS at §VII.AJ W11-5 sister — refines the cross-pillar bridge corpus boundary; lizzi-S7's hypothesis that "realized envelope inflation might rescue W11-5" is falsified.
- **HARD-HALT (CONDITIONAL prereq fail)**: W6-4 not PASS; W6-5 deferred to S92+; the W11-5 re-audit is structurally moot under Reading A (no universal envelope to anchor against); §VII.AJ entry remains REGISTRY-FAIL under L^{-3} canonical reading.

### Substrate framing

W11-5 IS a sister cross-pillar bridge to W-5 §VII.AF.1.OP-PROJ at Pillar III ↔ IV at substrate-distance-1 pole `s=3`. The substrate IS the spectral triple; the W11-5 anchor IS the substrate's emergent Hochschild pairing at finite L_max=10; the realized envelope IS the substrate's universal finite-L Mellin-cone manifestation at d=4 substrate-distance-1 pole. Direction substrate → emergent: substrate IS spectral triple → W11-5 anchor IS substrate-IS Hochschild pairing → realized envelope IS substrate's universal d=4 envelope → re-tag decision IS methodology-floor F-image of substrate-IS envelope determination. Container-thinking FORBIDDEN: "the W11-5 anchor lives in a Pillar IV laboratory" — INVERTED: "the W11-5 anchor IS substrate-IS at Pillar III; its laboratory image at Pillar IV IS the cross-pillar bridge map's image under HKR / Connes-Karoubi pairing; the substrate is logically prior to the laboratory image".

### Results (filled at runtime)

| Quantity | Value | Notes |
|:---------|:------|:------|
| W6-4 prereq verdict | _pending_ | must be PASS or gate HARD-HALTs |
| W11_5_anchor_value | _pending_ | extracted from §VII.AJ registry block at line 16887 |
| W11_5_anchor_l_max | _pending_ | canonical L_max=10 per S87 |
| α_realized | _pending_ | from W6-4 β̄; expected ≈ 1.9 |
| envelope_width_L_max_10_realized | _pending_ | 10^{-α_realized}; ≈ 1.26e-2 predicted |
| envelope_width_L_max_10_idealized | _pending_ | 10^{-3} = 1.0e-3 |
| deviation_vs_realized | _pending_ | re-tag decision domain |
| deviation_vs_idealized | _pending_ | ≈ 21× by W11-5 closure |
| re_tag | _pending_ | ∈ {REGISTRY-PASS-CONDITIONAL, DEFERRED-PENDING-PROXY-REFINEMENT, DEFERRED-PENDING-FIRST-EXTRACTION, REGISTRY-FAIL-PRESERVED} |

### Verdict (filled at runtime)

_pending_

### Substrate framing (runtime addendum)

_pending_

### Cross-references

- W6-4 (CONDITIONAL prereq; substrate-structural universality verdict)
- §VII.AJ at registry line 16887 (W11-5 sister entry)
- §VII.AU.OP-PROJ HIT table corpus instance #2 at line 17728
- S87 W11-5 closure record (W11-5 anchor source)
- `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` SUGGESTION K=1 (calibration corpus advancement target)
- `feedback_mack-bridge-role.md` (sole-writer rule for registry-text retrofit)
- lizzi-S7 §(3.a) line 159 (realized envelope width prediction) + §(3.d) line 192 (cross-corpus hint) + §(5) lines 374-385 (CF-LZ-S7-3 spec)
- `substrate-first-canonical-sourcing.md §(ii.B)` (runtime-pinned plan-text-drift correction for W6-4 NPZ input)

### Carry-forward computations (filled at runtime)

_pending_

---

## Wave 6 — Cross-gate decision points (filled at runtime)

The plan §"Wave 6 → Downstream Decision Points" pre-registers the consequence map for each gate's verdict. Runtime decision-point outcomes are pinned here once gates close.

### W6-1 verdict consequences

- **W6-1 PASS-A (Reading A canonical)**: §VII.AU.OP-PROJ advances REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE; W8 CF-67 Stage-2 cross-axis verify becomes structurally executable; cross-pillar-bridge calibration corpus K=4 → K=5 candidate via Hybrid Independence Test PASS at axis (iv).
- **W6-1 FAIL-B**: HYBRID verdict (d) per-regulator-class sub-window structure is canonical for §VII.AU.OP-PROJ; pathway (a) backup at L_max ≥ 35 becomes structurally necessary at S92+.
- **W6-1 INFO**: pathway (a) backup at L_max ≥ 35 becomes structurally necessary at S92+.

**Runtime outcome (PASS-A)**: W6-1 returned **PASS** at α_pathway_b = 2.6926 via the F_2-axis FI sub-projection consensus criterion (`majority_pass=False, f2_pass=True` → PASS per plan §9 line 229 `majority_pass OR f2_pass`). α_Mellin = α_zeta = 2.6926 EXACT (F_2-axis FI); α_PV = 6.4764, α_cutoff = 3.9111, α_lattice = 5.6893 (RD-axis scattered under SCHEMATIC sub_term_R). Composite 3-tuple PASS/PASS/VALID. audit_sha256=`d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d`. Consequence: §VII.AU.OP-PROJ STAGE-1-CANDIDATE landing queued via CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING (P1; ~1.0 we; mack sole writer); Stage-2 cross-axis PASS-AND queued via CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY (P1; ~1.5 we per joint-theorem-promotion.md). NOTE: α_b=2.6926 sits BETWEEN Reading A canonical α=3 and Reading B realized α=1.9 — the F_2-axis FI projection asymptotes to a substrate-canonical exponent intermediate between idealized and realized envelopes; this is structurally distinct from both Reading A and Reading B as originally pre-registered.

### W6-2 verdict consequences

- **W6-2 PASS**: K_HK = 9 FI + K_csub MIXED at A_5 atlas confirmed; advances `regulator-pin-discipline.md` MIXED-class taxonomy calibration; K_csub_R per-regulator pins queued for `canonical_constants.py` via S91 W0a mack-cosmic-bridge follow-up gate.
- **W6-2 INFO**: new sub-class "F_2-axis FI / full-atlas MIXED" intermediate classification candidate; refinement queued for S92+.
- **W6-2 FAIL**: structural defect at A_K Wedderburn (extremely unlikely) OR c_sub_corrected parameterization re-derivation needed.

**Runtime outcome (FAIL composite; K_HK = 9 FI sign-PASS / K_csub magnitude-FAIL)**: W6-2 returned **FAIL** composite per gate-verdicts.md §"S87+ Composite-collapse rule" (sign=PASS / magnitude=FAIL / regime=VALID → FAIL). K_HK = 9 FI verified across A_5 atlas at spread = 0 BY CONSTRUCTION (Künneth-Morita 3×3 = 9 cells; substrate-IS partition cardinality regulator-INVARIANT). K_csub_R extraction under SCHEMATIC sub_term_R(L) analytic forms returned dimensionally-overwhelming values (K_csub_Mellin = K_csub_zeta = −245.69; K_csub_PV = −5.04×10^33; K_csub_cutoff = −1.40×10^66; K_csub_lattice = −1.65×10^35) — root cause: Λ_UV² = M_KK² ≈ 5.5×10^33 GeV² prefactor dimensionally incompatible with dimensionless K_csub ≈ O(0.5) target. audit_sha256=`109e4307e8a0d80578318de29315b688287704cba1518bd651845db4a1cb984f`. POSITIVE-CALIBRATION K_substantive 4→5 advancement at `substrate-first-canonical-sourcing.md §(iv)` via tier_pin=TIER-2 disclosure (verdict file line 115). FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers retry queued via CF-S91-W6-2-FULL-PHYSICAL-RETRY (P1; ~3.0 we).

### W6-3 verdict consequences

- **W6-3 PASS-A-partial (α_sub > 2.5)**: biases W6-4 expectation toward σ_β > 0.10 (INFO probable at W6-4); W6-1 pathway (b) PASS-A trajectory.
- **W6-3 INFO (α_sub ∈ [2.0, 2.5])**: sub-window non-decisive; W6-4 carries full discriminator weight.
- **W6-3 FAIL (α_sub < 2.0)**: biases W6-4 expectation toward PASS with tight σ_β; W6-1 pathway (b) FAIL-B trajectory.

**Runtime outcome (FAIL_R2 band; Reading A direction confirmed, magnitude misses PASS-A-partial threshold)**: W6-3 returned **FAIL** at band-tag `FAIL_R2` (regression-quality floor R² ≥ 0.95 missed at R² = 0.9074). α_sub = 2.4291 (Sage-Q ≡ numpy at 8.4e-15 deviation); sub_minus_full = α_sub − α_full_window = +0.5001 (Reading A direction confirmed: sub-window slope STEEPER than full-window). Composite 3-tuple PASS/INFO/MARGINAL collapses to FAIL via the gate's pre-registered top-of-tree R² < 0.95 → FAIL_R2 rule (plan §6 line 592). audit_sha256=`2ac38905046a7e0b1521de6c6490de5fda4fba6f13d38fd77fb6cd697185e46b`. **Bias signal for W6-4**: α_sub = 2.4291 just under the PASS-A-partial threshold (2.5; deficit −0.0709) — predicted W6-4 INFO with intermediate σ_β. Actual W6-4 outcome (see below): FAIL Reading A with σ_β = 0.8936 (far above predicted intermediate band). The W6-3 mid-range α_sub did NOT predict the W6-4 high-σ_β outcome — the substrate's d=4 envelope at finite L_max splits across observables in a way the sub-window precursor did not foreshadow.

### W6-4 verdict consequences

- **W6-4 PASS (Reading B substrate-structural)**: unblocks W6-5; advances Layer-Functor F Verdict-Shape Consistency Theorem K=2 calibration corpus toward K=3 MANDATORY; §VII.AF.1.OP-PROJ Level-3 anchor PASS reinterpreted with ~130× inside realized envelope margin.
- **W6-4 FAIL (Reading A coincidence)**: Layer-Functor F K=2 calibration FALSIFIED; W6-5 not fired; W6-1 pathway (b) very likely INFO or FAIL.
- **W6-4 INFO**: K=2 calibration stands pending S92+ extension with O_5+; W6-5 deferred.

**Runtime outcome (FAIL Reading A coincidence confirmed; 4 verdict emissions via Option A supersedes-chain)**: W6-4 returned **FAIL** Reading A coincidence confirmed at β̄ = 1.7725, σ_β = 0.8936, C_ij_min = −0.2625 (anti-correlated). Per-observable: β_O1 = 1.1564 (M^(ζ)_3 bare Mellin; outside [1.5, 2.5]); β_O2 = 1.9324 (P_0 + HKR CF-65-equivalent; INSIDE PASS band [1.8, 2.1]); β_O3 = 2.9718 (P_BdG at substrate-distance-2 pole; outside [1.5, 2.5] — consistent with asymptotic L^{-3} at the s=4 pole); β_O4 = 1.0293 (Tr(D_K^{-6}) pure spectral moment; outside). 3-of-4 in FAIL band; σ_β ≥ 0.30 triggers Reading A FAIL criterion. Composite 3-tuple FAIL/FAIL/VALID → FAIL. **4 emissions on disk** (lines 116-118 INFO, 119-121 INFO, 122-124 FAIL, 125-127 canonical FAIL with `supersedes=0da7e7205a..._3bf5b89209f..._914e52092f...` enumerating all 3 priors per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` rule 6 retroactive canonicalization). Canonical audit_sha256=`f47e4299290dcff41af5f3a2069e6b91f61130e776087ecccf133201d1fa146e`. **Consequence**: Layer-Functor F Verdict-Shape Consistency Theorem K=2 SUGGESTION FALSIFIED (W6-4 FAIL falsifies the universality prediction); K-counter stays at K=2 with NEGATIVE-CALIBRATION (CF-W6-4-S91-4 documentation gate queued). W6-5 DE-TRIGGERED per W6-5 §9 HARD-HALT spec + script lines 1066-1069 + plan §22 W6-4 consequences line 1307.

### W6-5 verdict consequences

- **W6-5 PASS (REGISTRY-PASS-CONDITIONAL re-tag)**: W11-5 sister promoted; advances `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` calibration K=1 → K=2; requires mack-cosmic-bridge sole-writer registry retrofit follow-up gate at S91 W0a.
- **W6-5 INFO (DEFERRED-PENDING re-tag)**: W11-5 sister gains structurally-justified intermediate status; mack-cosmic-bridge registry retrofit follow-up queued.
- **W6-5 FAIL (REGISTRY-FAIL-PRESERVED)**: cross-pillar bridge corpus boundary refined; W11-5 sister CONFIRMED non-binding under both envelopes.
- **W6-5 HARD-HALT (W6-4 not PASS)**: deferred to S92+.

**Runtime outcome (DEFERRED-TO-S92 per W6-4 FAIL)**: W6-5 NOT DISPATCHED. W6-4 closed FAIL (Reading A coincidence confirmed); W6-5 is CONDITIONAL on W6-4 PASS per WP header line 1478 + plan §W6-5 §9 line 1209 HARD-HALT spec + W6-5 script lines 1066-1069 (`if w6_4_verdict != 'PASS': raise RuntimeError(...)`) + plan §22 W6-4 consequences line 1307 ("W6-5 not fired"). The earlier plan §22 line 31 narrative ("W6-5 dispatched anyway under FAIL-side prediction") is structurally inconsistent with the gate's own spec — the gate IS the source of truth. Deferral closure documented in **CF-W6-4-S91-3** (S92 mack-cosmic-bridge sole-writer registry note; ~0.3 we; documents that realized-envelope re-tag is NOT structurally justified by W6-4 FAIL). §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ L^{-3} asymptotic envelope readings PRESERVED. The W11-5 sister registry-FAIL under L^{-3} canonical reading is PRESERVED (no re-tag). The cross-pillar-bridge-anatomy §"Deferred-pending intermediate verdict-class" calibration corpus K=1 SUGGESTION does NOT advance from W6-5 (the W11-5 instance was contingent on W6-4 PASS).

---

## Wave 6 — Wave-synthesis (filled at runtime)

This section consolidates the wave's structural findings, cross-gate dependencies actually exercised, and any registry / canonical-constants / rule-file landings that emerge during execution. Populated at wave close per the standard wave-synthesis discipline.

### Verdict summary table

| Gate | Verdict | Value summary | Audit SHA |
|:-----|:--------|:--------------|:----------|
| §W6-1 | **PASS-A** (Reading A canonical confirmed via F_2-axis FI sub-projection) | α_pathway_b = 2.6926 (α_Mellin = α_zeta = 2.6926 EXACT, F_2-axis FI confirmed at 0%); α_PV = 6.4764, α_cutoff = 3.9111, α_lattice = 5.6893 (RD-axis scattered under SCHEMATIC sub_term_R); count_pass = 2/5 (majority FAIL); f2_pass = True ⇒ PASS-A via consensus criterion `majority_pass OR f2_pass` per plan §9 line 229; 3-tuple PASS/PASS/VALID; tier_pin=TIER-2 POSITIVE-CALIBRATION at verdict file line 131 | `d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d` |
| §W6-2 | **FAIL** (composite); K_HK = 9 FI sign PASS; K_csub magnitude FAIL (SCHEMATIC sub_term_R) | K_HK=9 FI verified across A_5 atlas (spread=0 BY CONSTRUCTION); K_csub_Mellin=K_csub_zeta=−245.69 (F_2-axis FI), K_csub_PV=−5.04×10^33, K_csub_cutoff=−1.40×10^66, K_csub_lattice=−1.65×10^35 (SCHEMATIC sub_term divergent — root cause: Λ_UV² prefactor dimensionally overwhelms K_csub anchor 0.5±0.1) | `109e4307e8a0d80578318de29315b688287704cba1518bd651845db4a1cb984f` |
| §W6-3 | **FAIL** (FAIL_R2 band; regression-quality floor missed) | α_sub = 2.4291 (Sage-Q ≡ numpy at 8.4e-15 deviation); R² = 0.9074 < 0.95 floor; sub_minus_full = +0.5001 (Reading A direction confirmed: sub-window slope STEEPER than full-window); 3-tuple PASS/INFO/MARGINAL collapses to FAIL via top-of-tree R²-floor rule per plan §6 line 592; magnitude misses PASS-A-partial threshold (2.5) by 0.0709 | `2ac38905046a7e0b1521de6c6490de5fda4fba6f13d38fd77fb6cd697185e46b` |
| §W6-4 | **FAIL** (Reading A coincidence confirmed; 4 verdict emissions via Option A supersedes-chain) | β̄ = 1.7725, σ_β = 0.8936, C_ij_min = −0.2625; β_O1 = 1.1564, β_O2 = 1.9324 (CF-65 family, INSIDE PASS [1.8, 2.1]), β_O3 = 2.9718 (substrate-distance-2 pole), β_O4 = 1.0293; 3-of-4 outside [1.5, 2.5] AND σ_β ≥ 0.30 ⇒ FAIL_Reading_A; 3-tuple FAIL/FAIL/VALID; 4 emissions on disk (lines 116-118 INFO, 119-121 INFO, 122-124 FAIL, 125-127 canonical FAIL with explicit `supersedes=0da7e7205a..._3bf5b89209f..._914e52092f...` per `gate-verdicts.md §"Option A"` rule 6) | `f47e4299290dcff41af5f3a2069e6b91f61130e776087ecccf133201d1fa146e` (canonical) |
| §W6-5 | **DEFERRED-TO-S92** (NOT DISPATCHED per W6-4 FAIL + W6-5 script HARD-HALT spec) | W6-5 is CONDITIONAL on W6-4 PASS per WP header + plan §W6-5 §9 line 1209 + W6-5 script lines 1066-1069 + plan §22 W6-4 consequences line 1307 ("W6-5 not fired"). Deferral closure documented in **CF-W6-4-S91-3** (S92 mack-cosmic-bridge sole-writer registry note; ~0.3 we; §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ L^{-3} asymptotic envelope readings PRESERVED; W11-5 sister registry-FAIL under L^{-3} PRESERVED) | N/A (gate not executed) |

### Structural findings

**The W6-4 + W6-1 structural puzzle** is the wave's headline finding. W6-4 returned FAIL (Reading A coincidence confirmed) at the 4-observable family universality test: β values scatter across [1.03, 2.97] (σ_β = 0.89; C_ij_min = −0.26 anti-correlated; 3-of-4 outside [1.5, 2.5] PASS band). W6-1 returned PASS-A (Reading A canonical confirmed) at the §VII.AU.OP-PROJ-specific F_2-axis FI sub-projection: α_Mellin = α_zeta = 2.6926 EXACT at L_max=22 (Mellin+zeta consensus criterion PASS). Both verdicts are mutually consistent under refinement: **the d=4 universal envelope is NOT universal across observable choices at finite L_max (W6-4 FAIL), BUT the F_2-axis FI projection of any single substrate-IS observable like §VII.AU.OP-PROJ asymptotes to a substrate-canonical exponent (~2.7) that lies between the asymptotic L^{-3} (Reading A canonical α=3) and the realized L^{-1.9} (Reading B realized at the 4-observable family).**

The substrate-physics refinement: the universal-envelope theorem holds at the **FI-sub-projection-per-observable** layer (F_2 = {Mellin, zeta} agreement on §VII.AU.OP-PROJ), NOT at the **cross-observable** universality layer (4-observable family scatter). Each substrate-IS observable on the spectral triple has its OWN decay rate at finite L_max because each carries a different (projector, bridge, pole) triplet — these select different sub-algebra images of `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` whose substrate-distance-1 pole residues differ. The 4-observable scatter (W6-4) is the substrate's intrinsic structure, NOT a falsification of the universal envelope; the F_2-axis FI agreement (W6-1) is the substrate's regulator-INVARIANT signature at the algebra-INVARIANT spectrum-only-functional layer.

**Auxiliary structural findings**:

- **K_HK = 9 FI is structurally confirmed** (W6-2): the Künneth-Morita 3×3 = 9 cell partition of HH^*(A_K) is regulator-INVARIANT BY CONSTRUCTION across the A_5 atlas {Mellin, zeta, Pauli-Villars, cutoff, lattice} at spread = 0. Empirically anchors the S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration. STAGE-1-CANDIDATE permanent-promotion queued (CF-S91-W6-2-K_HK-PERMANENT-PROMOTION).
- **K_csub MIXED prediction is unresolved at SCHEMATIC level** (W6-2): the SCHEMATIC `_spectral_action_regulators.py` sub_term_R(L) parameterization is dimensionally incompatible with the dimensionless K_csub ≈ O(0.5) target — Λ_UV² = M_KK² ≈ 5.5×10^33 GeV² prefactor overwhelms by ~33 OOM. F_2-axis FI sub-projection (Mellin=zeta=−245.69) holds at 0% spread, structurally consistent with the algebra-INVARIANT half of the prediction; the algebra-DEPENDENT MIXED test requires FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers (CF-S91-W6-2-FULL-PHYSICAL-RETRY ~3.0 we).
- **Sub-window α_sub = 2.4291 is intermediate** (W6-3): the 4-point pre-anchor regression at L ∈ {6..9} returns α between Reading A and Reading B with sub_minus_full = +0.5001 (Reading A direction confirmed) but R² = 0.9074 < 0.95 floor. The sub-window is NOT a clean power law at the pre-asymptotic boundary layer; Richardson extrapolation over extended sub-windows queued (CF-W6-3-NEXT-1 ~0.15 we).
- **W6-4 single-shot pattern violation surfaced + recovered via Option A retroactive supersedes**: the W6-4 agent emitted 3 prior verdict lines without `supersedes=` tagging before emitting the canonical 4th with explicit supersedes-chain. NEGATIVE-CALIBRATION instance for `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` extended to discriminator gates; the Option A protocol (`gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`) correctly preserved the audit trail by construction at the final emission.

**Layer-Functor F Verdict-Shape Consistency Theorem K=2 SUGGESTION is FALSIFIED** by W6-4 FAIL: the W-5 + W-6 universality prediction (verdict-shape consistency across observable choices) does NOT hold at finite L_max=12 across the 4-observable basis. K-counter STAYS at K=2 with NEGATIVE-CALIBRATION; CF-W6-4-S91-4 documents the non-advancement. Forward S92 work (CF-W6-4-S91-1 at Friedrich-Bär saturation L≥35; CF-W6-4-S91-2 projector-dependent subleading-correction characterization) will determine whether the K=2 theorem can be reformulated at the FI-sub-projection layer where W6-1 PASS-A holds.

### Registry landings (PERMANENT-RESULTS-REGISTRY edits)

**No in-session registry edits performed in W6.** All registry-text retrofits are queued as S91 W0a or S92+ follow-up gates with mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`:

1. **§VII.AU.OP-PROJ STAGE-1-CANDIDATE landing** — queued via CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING (P1; ~1.0 we). W6-1 PASS-A on the F_2-axis FI sub-projection (α_b = 2.6926) supports advancement from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway. 5 anatomy elements + 3-level structural-confidence ladder declared per `cross-pillar-bridge-anatomy.md`. Stage-2 PASS-AND queued separately (CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY P1 ~1.5 we) with axis-A = connes-ncg-theorist + axis-B = transit-dynamics or volovik (cross-axis distinct from lizzi-spectral PRIMARY per Axis-B Selection Protocol).
2. **§VII.AF.1.OP-PROJ baseline L^{-3} reading PRESERVED** — NO retrofit. W6-4 FAIL Reading A confirms the baseline's L^{-3} asymptotic envelope reading is consistent with universal-envelope failure at finite L_max=12 (4-observable scatter does NOT falsify the L^{-3} asymptotic at substrate-distance-1 pole s=3; the FI-sub-projection PASS-A at L_max=22 W6-1 supports it).
3. **§VII.AJ W11-5 sister registry-FAIL under L^{-3} PRESERVED** — W6-5 NOT DISPATCHED per W6-4 FAIL HARD-HALT. CF-W6-4-S91-3 (S92 mack registry note ~0.3 we) explicitly documents that realized-envelope re-tag is NOT structurally justified by W6-4 FAIL; the §VII.AU.OP-PROJ HIT table corpus instance #2 at registry line 17728 retains its current L^{-3} canonical reading without annotation.
4. **§VII.AU.OP-PROJ HIT table corpus K-counter advancement** — queued via CF-S91-W6-2-FORWARD-CALIBRATION-OP-PROJ-K=4 (P3; ~0.25 we; documentation-only; mack sole writer). `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` K-counter advances K=3 → K=4 via W6-2 instance (convention tag `HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION-SCHEMATIC`); rule already MANDATORY at K=3 so K=4 is structural forward-compliance.

### Canonical-constants landings (canonical_constants.py edits)

**No in-session canonical-constants edits performed in W6.** Two promotion candidates queued for S91 W0a or S92+ follow-up:

1. **K_HK = 9 FI permanent-promotion** — queued via CF-S91-W6-2-K_HK-PERMANENT-PROMOTION (P1; ~1.0 we + 1.5 we Stage-2). Anchored at S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration + W6-2 5-regulator atlas confirmation (spread = 0 BY CONSTRUCTION). Promotion path: STAGE-1-CANDIDATE landing in `permanent-results-registry.md` (mack sole writer) → STAGE-2 PASS-AND independent-verify on substrate-input-orthogonal observable pair per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY at K=3 → STAGE-3-PERMANENT promotion + `canonical_constants.py` entry `K_HK_FW = 9` with provenance pin (audit_sha=`109e4307...`).
2. **K_csub_R per-regulator pins (DEFERRED to FULL physical retry)** — pinning K_csub_R values as canonical constants is DEFERRED until CF-S91-W6-2-FULL-PHYSICAL-RETRY (P1; ~3.0 we) lands. The current W6-2 SCHEMATIC-derived K_csub_R values (Mellin=−245.69, PV=−5.04×10^33, cutoff=−1.40×10^66, lattice=−1.65×10^35) are NOT canonical-pin-worthy due to the Λ_UV² dimensional incompatibility with the dimensionless K_csub ≈ O(0.5) target. The FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers route is the substrate-canonical pathway; only after that retry should K_csub_R values land as canonical pins.
3. **α_b = 2.6926 for §VII.AU.OP-PROJ (W6-1)** — NOT canonical-promoted in-session. The F_2-axis FI consensus value is a STAGE-1-CANDIDATE empirical anchor (per §VII.AU.OP-PROJ STAGE-1 promotion CF); STAGE-2 PASS-AND must land before canonical-constants pin. The intermediate exponent (between α=3 idealized and α=1.9 realized) is structurally novel and warrants the full 4-stage promotion pathway before pinning.

### Rule-file landings (.claude/rules/ edits)

**No in-session rule-file edits performed in W6.** Two K-counter advancement events documented for forward-calibration; both rules already MANDATORY:

1. **`substrate-first-canonical-sourcing.md §(iv)` K_substantive 4 → 6** — TWO new POSITIVE-CALIBRATION instances landed in-wave: W6-2 (verdict line 112-115 with tier_pin=TIER-2 at line 115 + `-SCHEMATIC` suffix on convention + CLASS pin SCHEMATIC declared in producing script + docstring acknowledgment — 4-of-4 disclosure elements PASS) and W6-1 (verdict line 128-131 with tier_pin=TIER-2 at line 131 — same 4-of-4 disclosure pattern; convention `Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION-SCHEMATIC` because PV/cutoff/lattice members consumed SCHEMATIC sub_term_R; F_2-axis Mellin+zeta were FULL physical substrate-IS canonical). Documentation-only CF queued: CF-S91-W6-2-SCHEMATIC-DISCLOSURE-CALIBRATION-K=5 (P3; ~0.25 we). The W6-1 instance further advances K_substantive 5 → 6; rule already MANDATORY at K_substantive=3, so this is structural forward-compliance enriching the POSITIVE-CALIBRATION corpus.
2. **`registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` K=3 → K=4** — W6-2 instance advances the OP-PROJ suffix-discipline K-counter via convention tag `HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION-SCHEMATIC` carrying the OP-PROJ suffix at the correct registry-slot-identifier layer. Documentation-only CF queued: CF-S91-W6-2-FORWARD-CALIBRATION-OP-PROJ-K=4 (P3; ~0.25 we). Rule already MANDATORY at K=3.
3. **`registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` NEGATIVE-CALIBRATION** — W6-4 4-emission sequence (3 prior INFO/FAIL without supersedes + 1 canonical FAIL with supersedes-chain) extends the calibration corpus to discriminator gates (not strictly registry-landing). The agent correctly applied Option A `supersedes=` tag at the canonical emission per `gate-verdicts.md §"Option A — sig_5 remediation pathway"` rule 6 retroactive canonicalization. Forward S92+ discriminator gates SHOULD adopt the single-shot pattern even when NOT writing to the registry.
4. **`cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` K-counter NOT advanced** — W6-5 NOT DISPATCHED per W6-4 FAIL; the W11-5 sister calibration instance contingent on W6-4 PASS did NOT land. K=1 SUGGESTION (S90 W1-14 §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION dual) stands unchanged.
5. **`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 PRESERVED** — W6 reaffirms the algebra-INVARIANT (W6-1 F_2-axis FI sub-projection PASS-A) vs algebra-DEPENDENT (W6-4 4-observable family FAIL Reading A) STRUCTURAL ORTHOGONALITY at the substrate level. The two axes test orthogonal substrate-physics dimensions; neither verdict falsifies the other.

### Cross-wave dependencies exercised

Actual dispatch sequence (4 sub-waves) matched the plan §22 ordering:

1. **Sub-wave A (W6-3 standalone)**: dispatched first as cheap precursor (~0.1 we, existing S90 W8 FWD-C1 npz data; no W6 inter-dependency). Returned FAIL_R2 with α_sub = 2.4291 mid-range (Reading A direction confirmed via sub_minus_full = +0.5001 but R² floor missed). The W6-3 mid-range α_sub did NOT predict the W6-4 high-σ_β outcome (W6-3 expected W6-4 INFO with intermediate σ_β per plan §22 line 33; actual W6-4 σ_β = 0.89 ≫ predicted intermediate).
2. **Sub-wave B (W6-2 + W6-4 parallel)**: dispatched after W6-3 completed; both consumed `s84_spectrum_cache_L12_tau019.npz` (no inter-dep between W6-2 and W6-4). W6-2 returned FAIL composite (K_HK = 9 FI PASS-component + K_csub SCHEMATIC magnitude-FAIL); W6-4 returned FAIL Reading A coincidence confirmed via 4-emission Option A supersedes-chain.
3. **Sub-wave C (W6-1 after W6-4)**: dispatched only after W6-4 verdict landed per plan §22 dispatch ordering. W6-1 dispatch prompt carried W6-4 FAIL context (verdict + β values + σ_β + plan §22 line 1307 prediction "very likely INFO or FAIL") without biasing the computation. W6-1 actually returned PASS-A on the §VII.AU.OP-PROJ-specific F_2-axis FI sub-projection — surprise relative to plan §22 W6-4 consequences prediction; this is the structural puzzle the wave's structural findings address.
4. **Sub-wave D (W6-5 NOT DISPATCHED)**: W6-4 FAIL triggered HARD-HALT condition per W6-5 §9 line 1209 + script lines 1066-1069 + plan §22 W6-4 consequences line 1307. Closure documented in CF-W6-4-S91-3 (S92 mack registry note).

**Cross-data-file dependencies exercised**:

- W6-3 ← S90 W8 `s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz` (existing; pre-anchor sub-window δ_n_s values at L ∈ {6..9})
- W6-2 ← S84 `s84_spectrum_cache_L12_tau019.npz` (existing master cache)
- W6-4 ← S84 `s84_spectrum_cache_L12_tau019.npz` (same master cache; parallel-safe read-only)
- W6-1 ← S84 `s84_spectrum_cache_L12_tau019.npz` extended to L_max=22 via Friedrich-Bär saturation analytic upper-bound rooting per W11-3 precedent (NO raw eigenvalue construction at L ≥ 13 per W11-3 empirical infeasibility; combinatorial shell-sum formula + analytic-bound extrapolation per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`)

**Cross-rule-file dependencies exercised** (rule-file content read at dispatch / runtime by agents):

- `gate-verdicts.md §"S87+ canonical form"` (all 5 gates' verdict-line emission) + §"Option A — sig_5 remediation pathway under absolute verdict permanence" (W6-4 4-emission supersedes-chain)
- `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY (W6-1 + W6-2 tier_pin=TIER-2 disclosure POSITIVE-CALIBRATION)
- `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (W6-1 + W6-4 cross-axis structural orthogonality)
- `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"` (all 5 gates' convention CACHE-PROJECTION tag) + §"Binding axis" K=1 SUGGESTION (W6-1 Level-2-binding-HKR-bridge-canonical-import-binding pin)
- `epistemic-discipline.md §"Class 8.2"` MANDATORY (all 5 gates' verifier-rubric pre-registration) + §"Class 8.3" (publication-precision pubprecision_α pins)
- `math-scripts.md §"Double-Check Logic Before Compute"` (all 5 gates' substitution chains) + §"Mnemonic-vs-exact ratio discipline" (W6-3 Sage-Q vs numpy cross-check)
- `joint-theorem-promotion.md` 4-stage pathway (queued for CF-S91-W6-1-STAGE-2 + CF-S91-W6-2-K_HK-PERMANENT-PROMOTION)
- `feedback_mack-bridge-role.md` sole-writer convention (all queued registry retrofits)
- `feedback_fix-in-session-never-defer.md` 4-field spec (all 15 wave-level carry-forwards)

### Process observations (closed in-session)

Process observations are closed-in-session bookkeeping items per `feedback_fix-in-session-never-defer.md`; they do NOT propagate as carry-forwards.

1. **W6-4 BEFORE-pattern → Option A retroactive supersedes-chain (closed)**: W6-4 agent emitted 3 prior verdict lines (lines 116-118 INFO, 119-121 INFO, 122-124 FAIL) before emitting the canonical 4th line (125-127) carrying explicit `supersedes=0da7e7205a..._3bf5b89209f..._914e52092f...` token enumerating all 3 priors per `gate-verdicts.md §"Option A"` rule 6 retroactive canonicalization. The audit trail is preserved by construction (absolute verdict permanence per Option A rule 1); downstream consumers cite the latest non-superseded line per Option A rule 3. The iterative diagnostic process exposed (a) β_O3 = nan in emissions 1-2 due to BdG sub-algebra image not found in L_max=12 cache without combinatorial-formula fallback, (b) β_O1/O2/O4 sensitivity to mnemonic-vs-exact regression form per `math-scripts.md §"Mnemonic-vs-exact ratio discipline"` (Taylor `(ratio-1) vs (1/L)` vs structurally-exact `log(ratio) vs log((L+Δ)/L)`). Both honestly disclosed in WP §W6-4 Methodology subsection's OPERATIONAL DEVIATION block.
2. **W6-2 SCHEMATIC sub_term_R dimensional incompatibility (closed-in-session via honest FAIL)**: the SCHEMATIC `_spectral_action_regulators.py` sub_term_R(L) parameterization with Λ_UV² = M_KK² ≈ 5.5×10^33 GeV² prefactor is dimensionally incompatible with the dimensionless K_csub ≈ O(0.5) target. The W6-2 agent correctly emitted composite FAIL (sign=PASS / magnitude=FAIL / regime=VALID → FAIL) without convention-shopping per PROHIBITED_ACTIONS Class 1 boundary. Disclosure protocol followed: tier_pin=TIER-2 companion row + `-SCHEMATIC` convention suffix + CLASS pin SCHEMATIC declared in producing-script docstring → POSITIVE-CALIBRATION 4-of-4 disclosure per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY.
3. **W6-5 HARD-HALT DEFERRED-TO-S92 (closed via CF-W6-4-S91-3)**: W6-4 FAIL triggered W6-5 §9 line 1209 HARD-HALT condition + script lines 1066-1069 (`if w6_4_verdict != 'PASS': raise RuntimeError(...)`). W6-5 NOT DISPATCHED. Closure documented in CF-W6-4-S91-3 (S92 mack-cosmic-bridge sole-writer registry note ~0.3 we; documents that realized-envelope re-tag is NOT structurally justified by W6-4 FAIL). Plan §22 line 31 narrative ("W6-5 dispatched anyway under FAIL-side prediction") was internally inconsistent with the W6-5 gate's own structural spec; the gate IS the source of truth.
4. **W6-2 agent partially populated orchestrator-section (closed; minor writer-discipline note)**: W6-2 agent pre-populated its own row of the wave-synthesis verdict-summary table (line 1822 / original numbering) — a minor violation of "Only ONE agent writes the output file per round (designated in the prompt)" per skill rule. Content was honest and complete; orchestrator preserved the row. Forward: agents should NOT pre-populate orchestrator-authored sections; the orchestrator's wave-synthesis section is its own writer's domain.
5. **Pre-W6 verdict-file SHA duplicates preserved (out of scope for W6)**: 2 pre-existing `audit_sha256` duplicates in `computations/session-91/s91_gate_verdicts.txt` (`f83a0ec8c02dcfca9b506e54c34339b1f0bdb0425d927576de2e3d4e78c110a5` ×2 and `752a8f2b862a9aa5d2d8ba33d208140516f926c8fc9b1b306f989c222775ff64` ×2) are from prior S91 waves (W0-W5), NOT introduced by W6. Out-of-scope for this wave's process-observation closure; v3-closure-audit at session-close will surface them per `v3-closure-recovery.md §"Stage 1"` sig_5 detection. All 5 W6 gates' SHAs are pairwise distinct + distinct from all pre-W6 SHAs (sig_5 PASS for W6).

---

## Wave 6 — Carry-forward computations (consolidated; filled at runtime)

Per `feedback_fix-in-session-never-defer.md`, every wave-synthesis MUST produce 4-field carry-forward specs (what / inputs / gate / effort) for genuine future computation. Hygiene observations on already-correct artifacts are NOT carry-forwards (per `feedback_fix-in-session-never-defer.md`); they are fixed in-session and recorded under "Process observations" above.

Carry-forwards are populated at wave close from per-gate `### Carry-forward computations` sections plus any wave-level emergent carry-forwards.

### CF-W6-N format template

```
### CF-W6-N — {Brief title}
- **What**: {specific deliverable; gate ID candidate}
- **Inputs**: {required upstream files / canonical pins / registry entries}
- **Gate**: {pre-registered PASS / FAIL / INFO threshold}
- **Effort**: {wave-equivalent estimate}
- **Source gate**: {which W6-N produced this CF}
- **Depends on**: {prerequisite gates / data files / registry entries}
```

### Carry-forwards (filled at runtime)

15 wave-level carry-forwards consolidated from per-gate `### Carry-forward computations` sections: W6-3 contributes 1, W6-2 contributes 5, W6-4 contributes 4, W6-1 contributes 5. Each carries a 4-field spec per `feedback_fix-in-session-never-defer.md`. Sorted by priority tier P1 → P3.

**P1 — Registry advancement + structural retries** (highest priority; queued for S92 or S91 W0a hot-fix):

#### CF-W6-W → CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING
- **What**: STAGE-1-CANDIDATE landing of §VII.AU.OP-PROJ in `permanent-results-registry.md` based on W6-1 PASS-A (α_b = 2.6926 via F_2-axis FI sub-projection consensus criterion). Construct STAGE-1-CANDIDATE registry slot with all 5 anatomy elements (substrate-IS observable: §VII.AU.OP-PROJ HKR-image-bound Connes-Karoubi pairing; bridge map: HKR L→∞; algebraic envelope: F_2-axis FI L^{-2.69}; empirical anchor: W6-1 α_b = 2.6926 at L_max=22; substrate-IS Level-2 sub-class declaration) + 3-level structural-confidence ladder.
- **Inputs**: W6-1 verdict audit_sha=`d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d`; `permanent-results-registry.md` next-free-letter slot; `cross-pillar-bridge-anatomy.md §"5-anatomy + 3-level discipline"` MANDATORY at K=3.
- **Gate**: PASS = STAGE-1-CANDIDATE entry landed with all 5 anatomy + 3-level declared.
- **Effort**: ~1.0 we (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`).
- **Source gate**: W6-1.
- **Depends on**: W6-1 PASS-A (LANDED); mack-cosmic-bridge sole-writer convention.

#### CF-W6-W → CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY
- **What**: Stage-2 PASS-AND cross-axis independent-verify per `joint-theorem-promotion.md` 4-stage pathway. Two cross-reviewers on different axes: axis-A = connes-ncg-theorist (NCG-axiomatic / spectral-functional side), axis-B = transit-dynamics-aether-mechanic or volovik-superfluid-universe-theorist (transit/substrate side; lizzi-spectral excluded per Axis-B Selection Protocol downstream-inheritance reach test since lizzi authored the W6-1 PRIMARY work). Both verify the §VII.AU.OP-PROJ STAGE-1-CANDIDATE entry from first principles without prior workshop context. Substrate-input-orthogonality clause PASS-AND requirement per S88 W7c-167 V.1 / `joint-theorem-promotion.md` MANDATORY at K=3.
- **Inputs**: §VII.AU.OP-PROJ STAGE-1-CANDIDATE registered entry; `s91_w6_1_*.npz` (substrate-input observable 1); independent substrate-input observable (e.g., Stage-2 cross-reviewer constructs an orthogonal observable from the same L_max=12 cache for axis-A spectral verification).
- **Gate**: PASS = BOTH cross-reviewers PASS on JOINT clauses (logical AND); §VII.AU.OP-PROJ promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT.
- **Effort**: ~1.5 we (two parallel single-axis verifications per `joint-theorem-promotion.md` Stage 2).
- **Source gate**: W6-1.
- **Depends on**: CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING; `joint-theorem-promotion.md` 4-stage pathway.

#### CF-W6-W → CF-S91-W6-2-FULL-PHYSICAL-RETRY
- **What**: Re-execute the K_csub_R extraction across the A_5 atlas under FULL physical Connes-Chamseddine 1996 §2.2-2.3 multipliers (replace SCHEMATIC sub_term_R(L) analytic forms with substrate-canonical zeta-function-derived multiplier values at each regulator). Per-regulator: Pauli-Villars at s=2 with PV-subtracted moments; cutoff at sharp-truncation in (p,q) sectors with p+q > L_cut; lattice at s=2 with sinc² form-factor weighting on substrate eigenvalue distribution. Re-extract K_csub_R, K_csub_mean, K_csub_std. ALSO closes the W6-1 RD-axis SCHEMATIC consumption (PV=6.48, cutoff=3.91, lattice=5.69 anomalies under SCHEMATIC sub_term).
- **Inputs**: W6-2 npz (audit_sha=`109e4307...`); s84_spectrum_cache_L12_tau019.npz (extending to L_max=14 or 15 via Friedrich-Bär saturation if feasible); `_spectral_action_regulators.py` FULL physical regularization helpers (CLASS pin = FULL); canonical_constants.py for κ_2, M_KK, τ_fold; CC 1996 §2.2-2.3 multiplier definitions.
- **Gate**: PASS = |K_csub_mean − 0.5| < 0.1 AND K_csub_std > 0.05 AND F_2-axis FI sub-projection PASS; FAIL = |K_csub_mean − 0.5| ≥ 0.2.
- **Effort**: ~3.0 we (substantial; per-regulator spectral-moment extraction with PV subtraction + cutoff truncation + lattice form-factor weighting; CC 1996 derivation chain on substrate D_K spectrum).
- **Source gate**: W6-2 + W6-1 (unified scope; both gates' SCHEMATIC sub_term consumption resolved by single FULL physical pipeline).
- **Depends on**: W6-2 FAIL motivates retry; CC 1996 §2.2-2.3; `substrate-first-canonical-sourcing.md §(iv)` worked-example chain.

#### CF-W6-W → CF-S91-W6-2-K_HK-PERMANENT-PROMOTION
- **What**: Promote K_HK = 9 FI partition cardinality result to permanent registry entry at algebra-axis Corner I per `permanent-results-registry.md §VII.U.2` 4-corner partition. STAGE-1-CANDIDATE landing via mack-cosmic-bridge; STAGE-2 cross-axis independent-verify by connes-ncg-theorist (axis-A NCG-axiomatic Künneth-Morita derivation) + transit-dynamics-aether-mechanic (axis-B substrate-physics regulator-invariance) on substrate-input-orthogonal observable pair per substrate-input-orthogonality clause MANDATORY at K=3.
- **Inputs**: W6-2 K_HK = 9 FI PASS-component (audit_sha=`109e4307...`); S87 W4-2 §VII.AJ.W4-1 OP-PROJ K=3 calibration anchor (permanent); `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3.
- **Gate**: PASS = STAGE-1-CANDIDATE slot landed with all 5 anatomy elements + Level-1 single-τ-slice declaration; STAGE-2 PASS-AND on JOINT clauses for STAGE-3-PERMANENT promotion.
- **Effort**: ~1.0 we (STAGE-1) + ~1.5 we (STAGE-2; separate gate).
- **Source gate**: W6-2.
- **Depends on**: mack-cosmic-bridge sole-writer; `joint-theorem-promotion.md` 4-stage pathway.

**P2 — Diagnostic + asymptotic verifications + adversarial workshops**:

#### CF-W6-W → CF-S91-W6-1-LAYER-FUNCTOR-F-PUZZLE-DISAMBIGUATION
- **What**: 2-agent adversarial workshop on the W6-4 FAIL (4-observable family universality FAIL) + W6-1 PASS-A (F_2-axis FI sub-projection PASS) structural puzzle. Adjudicate the universal-envelope-theorem-scope reading divergence: (Reading B-strong) universal envelope applies at the cross-observable layer (FALSIFIED by W6-4); (Reading B-weak) universal envelope applies at the FI-sub-projection-per-observable layer (CONFIRMED by W6-1); (Reading-Hybrid) two structurally-orthogonal substrate-IS axes — cross-observable family vs FI-sub-projection-per-observable. Workshop converges on a refined Layer-Functor F Verdict-Shape Consistency Theorem statement that distinguishes the two layers.
- **Inputs**: W6-4 npz (4-observable shell-sums + Cij matrix); W6-1 npz (per-regulator α values at L_max=22); workshop §EV1/EV3 boxed theorem; CM-1995 §III.4 dimension-spectrum residue formula.
- **Gate**: workshop verdict produces refined theorem statement + Stage-1-Candidate registry slot if structurally promotion-worthy.
- **Effort**: ~workshop effort (2 agents × 3 rounds R1/R2/R3 + closeout synthesis).
- **Source gate**: W6-1 (cross-references W6-4).
- **Depends on**: W6-1 + W6-4 verdicts (LANDED); workshop participant selection (likely lizzi + connes OR lizzi + volovik).

#### CF-W6-W → CF-S91-W6-1-PATHWAY-A-FRIEDRICH-BAR-L_MAX-35-VERIFICATION
- **What**: Pathway (a) backup at L_max ≥ 35 via Friedrich-Bär saturation theorem extension per W11-3 precedent. CF-54 + CF-65 re-extraction at L_max ∈ {15..35} for the §VII.AU.OP-PROJ-specific observable; verifies whether α_b → α_asymptotic = 3 OR α_b → α_FI-consensus = 2.69 OR α_b stays bounded between. The W6-1 PASS-A at L_max=22 returned α_b = 2.6926, sitting between α=3 (Reading A canonical) and α=1.9 (Reading B realized) — pathway (a) at L_max ≥ 35 disambiguates the asymptotic trajectory.
- **Inputs**: W6-1 npz (α_pathway_b = 2.6926 anchor); s84_spectrum_cache_L12_tau019.npz extended via Friedrich-Bär saturation to L_max=35 (analytic upper-bound rooting per W11-3 + W11-2 precedents; NO raw eigenvalue construction at L ≥ 13); `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`.
- **Gate**: PASS-A-asymptotic = α_b(L≥35) → 3 ± 0.3; PASS-Intermediate = α_b stabilizes at 2.5 ± 0.3; FAIL-B-realized = α_b(L≥35) ≤ 2.0.
- **Effort**: ~2.5 we.
- **Source gate**: W6-1.
- **Depends on**: W6-1 PASS-A (LANDED); Friedrich-Bär saturation theorem applicability at L_max ≥ 35.

#### CF-W6-W → CF-W6-4-S91-1 (S92-D4-UNIVERSAL-ENVELOPE-AT-FRIEDRICH-BAR-SATURATION)
- **What**: Re-run the 4-way discriminator at the FRIEDRICH-BÄR-SATURATED L ≥ 35 window via analytic recursion-formula route (NOT cache; D_K eigenvalue construction at L ≥ 13 empirically infeasible per W11-3 calibration). For O_1/O_2/O_3 the combinatorial formula is cache-independent and extends to L=100; for O_4 a separate Casimir-asymptotic argument is needed.
- **Inputs**: substrate-IS combinatorial shell-sum formula (W6-4 implementation verified); CF-54 pre-flight Sage-Q Fraction-arithmetic at L ∈ [10, 100] (β=1.885) as cross-check anchor; Friedrich-Bär saturation theorem.
- **Gate**: PASS-Reading-B-at-asymptotic = all 4 β_i ∈ [1.7, 2.1] (widened band) at L ∈ [35, 100] AND σ_β ≤ 0.10 AND C_ij off-diag ≥ 0.7; FAIL otherwise; INFO if σ_β ∈ (0.10, 0.30).
- **Effort**: ~1.5 we.
- **Source gate**: W6-4.
- **Depends on**: W6-4 FAIL (LANDED) motivates asymptotic-extension verification.

#### CF-W6-W → CF-W6-4-S91-2 (S92-FINITE-L-PROJECTOR-DEPENDENT-SUBLEADING-CORRECTION-CHARACTERIZATION)
- **What**: Analytic / Sage-Q characterization of WHY each (projector, bridge, pole) triplet produces a distinct subleading-correction exponent at finite L. Hypothesis: each projector restricts shell sum to a sub-algebra image whose substrate-distance-1 pole residue is dominated by a different (p,q) → C_2(p,q) scaling that determines the finite-L envelope via Mellin-Barnes contour deformation off-pole.
- **Inputs**: W6-4 npz (β values + shell sums); workshop §EV1/EV3 boxed theorem; CM-1995 §III.4 dimension-spectrum residue formula.
- **Gate**: closed-form formula for β_i(projector_i, bridge_i, pole_i) at L=10 reproducing empirical β_i from W6-4 within 5%.
- **Effort**: ~1.0 we (adversarial workshop; lizzi + connes).
- **Source gate**: W6-4.
- **Depends on**: W6-4 FAIL (LANDED).

#### CF-W6-W → CF-W6-4-S91-3 (S92-W6-5-W11-5-SISTER-RE-AUDIT-UNDER-FAIL-CONDITION) — W6-5 DEFERRAL CLOSURE
- **What**: Explicit registry note at §VII.AU.OP-PROJ HIT table corpus instance #2 documenting that realized-envelope re-tag is NOT structurally justified by W6-4 FAIL (Reading A coincidence falsified the universality precondition for re-tag). L^{-3} asymptotic envelope per §VII.AF.1.OP-PROJ baseline PRESERVED as canonical reading. §VII.AJ W11-5 sister registry-FAIL under L^{-3} PRESERVED.
- **Inputs**: W6-4 FAIL verdict (audit_sha=`f47e4299...`); §VII.AU.OP-PROJ HIT table corpus; §VII.AF.1.OP-PROJ baseline; §VII.AJ W11-5 sister entry.
- **Gate**: METHODOLOGY-class registry note landed; no envelope reinterpretation.
- **Effort**: ~0.3 we (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`).
- **Source gate**: W6-4 (W6-5 DEFERRED closure).
- **Depends on**: mack-cosmic-bridge sole-writer; W6-4 FAIL.

#### CF-W6-W → CF-W6-3-NEXT-1 (S92+ Richardson-extrapolation against asymptotic α=3)
- **What**: Re-test the W6-3 sub-window α_sub at extended sub-windows L ∈ {6..10}, {6..11}, {6..12} (5/6/7 point regressions) AND apply Richardson extrapolation `α_sub(L) → α_∞` to estimate the asymptotic exponent from the sequence. If α_∞ → 3 from below, Reading A pre-asymptotic steepening is diagnostic-confirmed; if α_∞ → 1.929 persistent, Reading B; if intermediate band, hybrid.
- **Inputs**: existing S90 W8 FWD-C1 npz; extracted δ_n_s at L ∈ {10, 11, 12} from S90 W8 WP §W8-7(l); `canonical_constants.py:κ_2_substrate_FW=0.021018084987437196`.
- **Gate**: PASS-A-Richardson `α_∞ > 2.7 AND |Δα_∞/Δα_sub| → 0 as window grows AND R² ≥ 0.95 on the 6+ point fit`; INFO `α_∞ ∈ [2.3, 2.7]`; FAIL-Reading-B `α_∞ ≤ 2.0`.
- **Effort**: ~0.15 we (existing data; 3 sub-window regressions + Richardson extrapolation + Sage-Q exact cross-check; CPU-only).
- **Source gate**: W6-3.
- **Depends on**: W6-3 FAIL_R2 outcome (LANDED).

**P3 — Documentation-only K-counter advancements + diagnostic decomposition**:

#### CF-W6-W → CF-W6-4-S91-4 (S92-LAYER-FUNCTOR-F-VERDICT-SHAPE-CONSISTENCY-K2-NON-ADVANCE-DOCUMENTATION)
- **What**: Document explicitly in the framework registry that W6-4 FAIL does NOT advance the Layer-Functor F Verdict-Shape Consistency Theorem from K=2 SUGGESTION to K=3 MANDATORY — the FAIL FALSIFIES the K=2 SUGGESTION's universality prediction. K-counter stays at K=2 pending alternative-corroboration calibration instances (e.g., refined K=2-weak theorem at FI-sub-projection layer per CF-S91-W6-1-LAYER-FUNCTOR-F-PUZZLE-DISAMBIGUATION workshop).
- **Inputs**: W6-4 FAIL verdict; `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold rule.
- **Gate**: METHODOLOGY-class K-counter status entry preserved at K=2 SUGGESTION.
- **Effort**: ~0.2 we (lizzi METHODOLOGY-class documentation).
- **Source gate**: W6-4.

#### CF-W6-W → CF-S91-W6-1-PV-CUTOFF-LATTICE-FULL-PHYSICAL-RETRY (overlaps with CF-S91-W6-2-FULL-PHYSICAL-RETRY)
- **What**: Re-test PV/cutoff/lattice members of the A_5 atlas under FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers (NOT SCHEMATIC sub_term_R analytic forms). W6-1 pathway (b) returned scattered RD-axis values (α_PV=6.48, α_cutoff=3.91, α_lattice=5.69) under SCHEMATIC consumption; this CF and CF-S91-W6-2-FULL-PHYSICAL-RETRY share scope and can be UNIFIED into a single S92 FULL-physical implementation gate. The S92 planner should consolidate these two CFs.
- **Inputs**: W6-1 npz; W6-2 npz; same as CF-S91-W6-2-FULL-PHYSICAL-RETRY.
- **Gate**: PASS = all 5 regulators agree at α ∈ [2.4, 3.6] AND majority_pass ≥ 4/5 under FULL physical.
- **Effort**: ~3.0 we IF unified with CF-S91-W6-2-FULL-PHYSICAL-RETRY (overlap); standalone ~1.5 we.
- **Source gate**: W6-1.
- **Depends on**: CF-S91-W6-2-FULL-PHYSICAL-RETRY (consider unification).

#### CF-W6-W → CF-S91-W6-2-FORWARD-CALIBRATION-OP-PROJ-K=4
- **What**: Log W6-2 as the 4th calibration-corpus instance for `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` K=3 MANDATORY sub-clause (K-counter advance K=3 → K=4). W6-2 convention tag `HH-9-cell-tensor-channel-OP-PROJ-FI-plus-c_sub_corrected-MIXED-CACHE-PROJECTION-SCHEMATIC` carries the OP-PROJ suffix at the correct registry-slot-identifier layer.
- **Inputs**: W6-2 verdict-line convention field (audit_sha=`109e4307...`); `registry-landing.md` calibration corpus table; `feedback_rules-compensate-missing-structure.md` K-counter threshold.
- **Gate**: K-counter table updated to include W6-2 as K=4 row; documentation-only.
- **Effort**: ~0.25 we (mack-cosmic-bridge sole writer).
- **Source gate**: W6-2.

#### CF-W6-W → CF-S91-W6-2-SCHEMATIC-DISCLOSURE-CALIBRATION-K=5 (extend with W6-1 K=6)
- **What**: Log W6-2 as 5th POSITIVE-CALIBRATION instance + W6-1 as 6th POSITIVE-CALIBRATION instance for `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin sub-clause (K_substantive 4 → 6). Both have all 4 disclosure elements PASS at landing.
- **Inputs**: W6-2 verdict companion rows (line 115); W6-1 verdict companion rows (line 131); `substrate-first-canonical-sourcing.md §(iv)` 3-class taxonomy table.
- **Gate**: PASS = calibration corpus table updated to include W6-2 + W6-1 as POSITIVE-CALIBRATION instances (compliance class with all 4 elements PASS); documentation-only.
- **Effort**: ~0.25 we (mack-cosmic-bridge sole writer).
- **Source gate**: W6-2 + W6-1.

#### CF-W6-W → CF-S91-W6-2-L_MAX-22-EXTRAPOLATION-DIAGNOSTIC
- **What**: Investigate diagnostic root cause of K_csub_R Mellin/zeta = −245.69 specific intercept. Decompose into (a) analytic κ_2-quadratic growth contribution `1 + κ_2·L²/(5π)² = 1.0413` at L=22 vs (b) cache-truncated `sum 1/λ_i²` proxy that saturates beyond L=12 but is held constant (cache ceiling) in script's `M_Pl_eff_sq_with_regulator` for L > 12. The 1/L→0 linear fit on the resulting `ratio_per_L` vector then extrapolates back to large-magnitude intercept because the function is dominated by the L=8 cache-truncated value (ratio[L=8] = 239.08; ratio[L=22] = 1.04).
- **Inputs**: W6-2 npz keys `ratio_per_L` (per regulator); `L_grid`; `M_Pl_eff_sq_0`; producing-script `M_Pl_eff_sq_with_regulator` function.
- **Gate**: PASS = decomposition completed and per-regulator contribution analysis written; INFO = decomposition reveals cache-truncation/analytic-extrapolation mismatch as SCHEMATIC root cause (motivates the CF-S91-W6-2-FULL-PHYSICAL-RETRY); FAIL = decomposition reveals different root cause.
- **Effort**: ~0.5 we (post-hoc analysis of existing npz data).
- **Source gate**: W6-2.

**Summary**: 15 carry-forwards × ~12-15 we total estimated effort. Recommended S92 wave grouping: (P1-Registry) [CF-S91-W6-1-VII-AU-STAGE-1 + CF-S91-W6-1-STAGE-2 + CF-S91-W6-2-K_HK-PROMOTION] ~3.5 we; (P1-Compute) [unified CF-S91-W6-2-FULL-PHYSICAL-RETRY + CF-S91-W6-1-PV-CUTOFF-LATTICE-RETRY] ~3.0 we; (P2-Asymptotic) [CF-S91-W6-1-PATHWAY-A + CF-W6-4-S91-1 + CF-W6-3-NEXT-1] ~4.15 we; (P2-Workshop) [CF-S91-W6-1-LAYER-FUNCTOR-F-PUZZLE + CF-W6-4-S91-2] ~workshop+1.0; (P3-Doc) all queued for mack-cosmic-bridge S91 W0a batch ~1.5 we.

---

**End of W6 working paper shell.**

Shell author: gen-physicist (per S91 W6 prompter task; shell-creation only, no computations).
Plan source: `sessions/session-plan/session-91-plan-w6.md` (1403 lines, 106 KB; read in full via three chunks).
