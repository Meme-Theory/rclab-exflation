#!/usr/bin/env python3
"""Helper: update session-91-w9-workingpaper.md §W9-4 runtime block.

One-shot edit to bypass the Edit-tool mtime-conditional race against the
linter that touches the file between Read and Edit. NOT a computation
gate; pure file-replacement helper. # (local)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
wp = ROOT / "sessions" / "session-91" / "session-91-w9-workingpaper.md"
text = wp.read_text(encoding='utf-8')

old_block = """### Results (filled at runtime)

| Field | Value |
|:------|:------|
| `M_1_FW_CC` | M_KK (pinned) |
| `M_2_FW_CC` | √2·M_KK (pinned) |
| `c_1_FW_CC` | +2 (pinned) |
| `c_2_FW_CC` | -1 (pinned) |
| `a_2_CC` | pending (expected = 0) |
| `a_4_CC` | pending (expected = -2·M_KK^4) |
| `R_FULL` | pending |
| `R_canonical` | -40579.1500479506 (gv_canonical_difference_FW pin) |
| `Delta_FULL` | pending |
| `SECTOR_INDEX_AT_POLE_S3` | pending |
| `cache_sha256` | pending |
| `audit_sha256` | pending |

### Verdict (filled at runtime)

```
S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE: <PASS|FAIL|INFO> -- value=<Delta_FULL> scheme=full-connes-chamseddine-1996-physical-multipliers-spectral-action-pipeline convention=VII-AF-1-OP-PROJ-FULL-CC-MULTIPLIERS-PHYSICAL-substrate-distance-1-pole-s3 L_max=12 audit_sha256=<pending> content_sha256=<pending> schema_version=S84+
# audit_sha256_short=<pending> content_sha256_short=<pending> # S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE dual-SHA companion row
# sign_verdict=<pending> magnitude_verdict=<pending> regime_verdict=<pending> # S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE 3-tuple annotation (S87 schema-v2)
```

### Substrate framing (runtime addendum)

(reserved)

### Cross-references

- `substrate-first-canonical-sourcing.md §(iv)` — K=4 MANDATORY level-pin discipline; SCHEMATIC vs FULL physical
- `cross-pillar-bridge-anatomy.md §"Level-2 — Algebraic Convergence Envelope"` — L^{-3} envelope at d=4
- `regulator-pin-discipline.md` — UV-regulator axis Mellin/Pauli-Villars tagging
- §VII.AF.1.OP-PROJ canonical entry at `permanent-results-registry.md`
- W1 T1.1 §VII.AV FULL CC cross-pin

### Carry-forward computations (filled at runtime)

(reserved)"""

new_block = """### Results (runtime)

| Field | Value |
|:------|:------|
| `M_1_FW_CC` | M_KK = 7.428660036284456e+16 (Connes-Chamseddine 1996 §2.2-2.3 canonical mass) |
| `M_2_FW_CC` | √2·M_KK = 1.050700e+17 (2-point PV pair upper mass) |
| `c_1_FW_CC` | +2 |
| `c_2_FW_CC` | -1 |
| PV identity Σ c_r | 1.0 (machine precision; expected +1) |
| PV identity Σ c_r M_r² | -4.44e-16 (machine precision; expected 0) |
| `a_2_CC` (Γ(1)·(c_1·M_1² + c_2·M_2²)) | 0.000000e+00 (machine precision; PV cancellation theorem verified) |
| `a_4_CC` (Γ(2)·(c_1·M_1⁴ + c_2·M_2⁴)) | -6.090766e+67 = -2·M_KK⁴ (relative residual 3.93e-16) |
| `a_4_expected` (= -2·M_KK⁴) | -6.090766e+67 |
| L_max cache | s84_spectrum_cache_L12_tau019.npz (SHA 9e6d9cf7fd6a6949...) |
| n_sectors | 90 Peter-Weyl (p,q) sectors |
| n_eigenvalues_raw | 166,896 |
| Σ_k mults_k (Peter-Weyl weighted N) | 31,956,720 |
| λ_min (spectral gap) | 0.819741 M_KK-natural |
| λ_max | 5.418937 M_KK-natural |
| `M_BARE(s=3)` (zeta/SDW pure spectrum-sum) | 1.7823154840e+04 |
| `M_FULL_CC(s=3)` (PV-regulated CC1996) | 1.8003004557e+04 |
| `rho_FULL(s=3)` = M_FULL_CC / M_BARE | +1.0100907902e+00 (regulator-INVARIANT atlas ratio at L_max=12) |
| `w_PV(λ², s=3)` range | [0.991467, 1.058870], mean 1.002747 |
| `R_canonical_AF1` | R_universal_HP1_strict_F4 = 1.030902 (W-5 V4 SDW residual ratio; canonical pin per canonical_constants.py L_max=10) |
| `eps_H_HP1_norm` (PRIMARY per Class-(d) chain) | 16.197719 |
| `gv_canonical_difference_FW` (cross-link only; §VII.AQ pin) | -4.0579150048e+04 |
| `Delta_FULL` = (rho_FULL − R_canonical) / \\|R_canonical\\| | -2.018738e-02 (= -2.02%) |
| \\|`Delta_FULL`\\| | 2.018738e-02 |
| Cross-pin: `rho_FULL(s=4)` (cross-link to W1 T1.1 §VII.AV) | +1.0219998057e+00 |
| `audit_sha256` | 79314db6a6aee05390f34d0a666540eee3ae5fb113273d4f73b2d980434ca2a3 |
| `content_sha256` | 52dd09aaabb1c5dce6d02dbc13b775ec7236f1672ac3af60859c593277c32ddb |
| Composite verdict | FAIL (\\|Delta_FULL\\| = 2.02% > 1% FAIL_TOL) |
| 3-tuple verdict | sign=FAIL, magnitude=FAIL, regime=VALID |
| Compliance class transition | PARTIAL-POSITIVE → PARTIAL-POSITIVE-RETAINED (upgrade NOT achieved) |

### Verdict (runtime)

```
S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE: FAIL -- value='Delta_FULL=-2.018738e-02_rho_FULL=+1.010091e+00_R_canonical_AF1=1.030902_M_BARE_s3=1.7823e+04_M_FULL_CC_s3=1.8003e+04_a_2_CC=0.0_a_4_CC=-2_M_KK_4_compliance_transition=PARTIAL-POSITIVE-RETAINED' scheme=full-connes-chamseddine-1996-physical-multipliers-spectral-action-pipeline convention=VII-AF-1-OP-PROJ-FULL-CC-MULTIPLIERS-PHYSICAL-substrate-distance-1-pole-s3 L_max=12 audit_sha256=79314db6a6aee05390f34d0a666540eee3ae5fb113273d4f73b2d980434ca2a3 content_sha256=52dd09aaabb1c5dce6d02dbc13b775ec7236f1672ac3af60859c593277c32ddb schema_version=S87+
# audit_sha256_short=79314db6a6aee053 content_sha256_short=52dd09aaabb1c5dc # S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE dual-SHA companion row (W9a-99 split)
# sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID # S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE 3-tuple annotation (S87 schema-v2)
# LEVEL_CLASS_PIN=FULL # S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY level-pin compliance (SCHEMATIC -> FULL physical CC multipliers upgrade; PARTIAL-POSITIVE -> POSITIVE compliance class)
# promotion_target=permanent-results-registry.md §VII.AF.1.OP-PROJ compliance_class_transition=PARTIAL-POSITIVE-RETAINED # S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE VII.AF.1.OP-PROJ FULL CC upgrade NOT achieved (composite=FAIL; FULL CC diverges from SCHEMATIC canonical)
```

### Substrate framing (runtime addendum)

The substrate IS the spectral triple `(A_K, H_K, D_K)` at `τ_fold = 0.19`; the FULL CC physical multipliers `(M_1, c_1, M_2, c_2) = (M_KK, +2, √2·M_KK, -1)` ARE the substrate's intrinsic regularization tuple per Connes-Chamseddine 1996 §2.2-2.3, with the Pauli-Villars consistency identities `Σ_r c_r = 1` and `Σ_r c_r M_r² = 0` verified at machine precision (Σ c_r = 1.0; Σ c_r M_r² = -4.44e-16). The two Seeley-DeWitt closed-form predictions of the substitution chain Step 2 are confirmed at machine precision: `a_2_CC = 0` to absolute precision (PV cancellation theorem holds), and `a_4_CC = -2·M_KK⁴` to relative residual 3.93e-16 (sub-machine-epsilon agreement with the closed form). These two structural identities ARE substrate-IS algebraic constraints; they cannot fail at the FULL CC layer because they are algebraic consequences of the PV identities that define the multiplier tuple.

The Hochschild-pairing image at substrate-distance-1 pole `s=3` was evaluated via the regulator-INVARIANT atlas ratio `rho_FULL(s=3) = M_FULL_CC(s=3) / M_BARE(s=3)` on the full L_max=12 master spectrum cache (90 Peter-Weyl sectors, 166,896 raw eigenvalues, multiplicity-weighted 31,956,720 states). At L_max=12 with the FULL CC PV multiplier `w_PV(λ²; s=3) = 1 − Σ_r c_r · (M_r² / (λ² + M_r²))^3` evaluated point-wise across the spectrum (multiplier range [0.991467, 1.058870], mean 1.002747), the substrate's atlas ratio reads `rho_FULL = 1.0100907902`. The §VII.AF.1.OP-PROJ canonical anchor (`R_universal_HP1_strict_F4 = 1.030902` per W-5 V4 substitution chain Step 3 at L_max=10) is the SDW-residual atlas ratio anchoring the registry Level-3 empirical confirmation. The FULL CC pipeline produces `Delta_FULL = (1.0100907902 − 1.030902) / 1.030902 = −2.0187e-02`, i.e., a 2.02% downward divergence from the registry canonical.

### Verdict analysis — what FAIL means

Per plan §W9-4 Field 11, FAIL means "SCHEMATIC pin was systematically biased; the FULL CC pipeline diverges by >1% from the prior canonical." The observed `|Delta_FULL| = 2.02%` exceeds the FAIL threshold (1%) by a factor of 2.02 and exceeds the PASS threshold (0.1%) by a factor of 20.2. The verdict is FAIL by pre-registered RATIO tolerance rule; the 3-tuple verdict is `(sign=FAIL, magnitude=FAIL, regime=VALID)` — `regime=VALID` because the L_max=12 master cache satisfies the Friedrich-Bär saturation theorem at η_FB ≥ 0.40 (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`), so the substrate-IS observable evaluation is within its regime of validity throughout the scan; the failure is at the substrate-physics layer (atlas ratio mismatch), not at the numerical-method layer.

The FAIL is informative on the constraint surface in three structurally distinct ways:

1. **Regulator-class is consequential at substrate-distance-1 pole**. The §VII.AF.1.OP-PROJ canonical anchor `R_universal_HP1_strict_F4 = 1.030902` was derived via the W-5 V4 SDW-residual atlas evaluation (per registry line 14790 Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY chain), which inherits its regulator class from the SDW-class Mellin moments. The FULL CC pipeline evaluates the regulator-INVARIANT atlas ratio under the 2-point Pauli-Villars subtraction (Connes-Chamseddine 1996 §2.2-2.3). The 2.02% divergence between the two readings at substrate-distance-1 pole s=3 surfaces the FI vs RD axis at the per-pole layer per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`: the substrate-distance-1 pole atlas-row identity is REGULATOR-DEPENDENT (RD) on the SDW ↔ FULL CC PV axis, not FI as the SCHEMATIC pin's tag implied.

2. **Level-1 cohomology-class identity remains intact**. The §VII.AF.1.OP-PROJ three-level structural-confidence ladder (per registry lines 14821-14835) explicitly distinguishes Level 1 (substrate-IS structural identity at cohomology-class level, regulator-invariant) from Level 3 (empirical anchor at L_max=10 satisfying Level 2 envelope). The FULL CC FAIL at the 1% Level-3 layer does NOT invalidate the Level-1 cohomology-class identity (the Connes-Karoubi pairing on band-0 projector). What FAIL invalidates is the unqualified claim that the SCHEMATIC PV-envelope proxy AT LEVEL-3 reproduced the FULL CC PV-multiplier evaluation at sub-1% precision; the substrate-IS regulator-invariant cohomology-class identity at Level-1 is independent of regulator class by construction.

3. **The cross-pin diagnostic at substrate-distance-2 pole (s=4) yields `rho_FULL(s=4) = 1.022000`**. This is the cross-pin reference for W1 T1.1 §VII.AV FULL CC (Pillar IV proxy-refinement gate), and the two atlas ratios are mutually consistent (both are positive small upward shifts from unity under FULL CC PV regulation, ~1-2%), confirming that the FULL CC multiplier pipeline itself is structurally sound; the FAIL at §VII.AF.1.OP-PROJ is a regulator-class mismatch against the SDW-class canonical pin, not a pipeline defect.

### Downstream consequences (per plan Field 11 FAIL branch)

- §VII.AF.1.OP-PROJ Level-2 envelope re-pin required at S92+; downstream consumers (Stage-2 cross-axis verifies; Pillar IV continuum BZ-trace bridge map citations) must inherit the FULL CC value as the new diagnostic data point, with both `R_universal_HP1_strict_F4 = 1.030902` (SDW class) and `rho_FULL(s=3) = 1.0100907902` (FULL CC class) preserved as STRUCTURAL-ORTHOGONAL-COMPANION readings per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`.
- The §VII.AF.1.OP-PROJ compliance class transition stalls at PARTIAL-POSITIVE; the SCHEMATIC pin's UV-regulator axis remains the canonical reading on the SDW-residual ratio. The FULL CC pipeline IS POSITIVE-compliant at the disclosure layer (LEVEL_CLASS_PIN=FULL, convention suffix `-FULL-CC-MULTIPLIERS-PHYSICAL`, full SCHEMATIC-vs-FULL disclosure in this section), but the upgrade-from-PARTIAL-POSITIVE-to-POSITIVE event at §VII.AF.1.OP-PROJ itself does NOT fire because the FULL CC reading diverges from the SCHEMATIC canonical by >1%.
- Substantive S92 carry-forward: re-derive `R_universal_HP1_strict_F4` at substrate-distance-1 pole s=3 under each regulator class atlas (ζ-, SDW-, Pauli-Villars FULL-CC, Mellin-, lattice-) at L_max=12 and recompute the atlas spread; the 2.02% SDW ↔ FULL-CC delta becomes the K=1 calibration corpus instance for an FI-vs-RD reclassification of the §VII.AF.1.OP-PROJ Level-3 empirical anchor.

### Cross-pin with W1 T1.1 §VII.AV (FULL CC at substrate-distance-2 pole s=4)

The same FULL CC physical multiplier tuple was evaluated at substrate-distance-2 pole `s=4` as a cross-pin diagnostic. The numerics:

- `M_BARE(s=4) = 3.0908999757e+03` (zeta/SDW pure)
- `M_FULL_CC(s=4) = 3.1588991747e+03` (PV-regulated)
- `rho_FULL(s=4) = +1.0219998057e+00` (regulator-INVARIANT atlas ratio at substrate-distance-2 pole)

This is consistent with the S91 W1-2 (CF-S91-CF-70) FULL CC `s=4` evaluation (per `s91_w1_cf70_full_cc_multipliers.py` and the corresponding npz output): the FULL CC PV multiplier produces a positive 2.20% upward shift from the bare moment at s=4, comparable to the 1.01% shift at s=3. The FULL CC pipeline itself is structurally sound; the two pole-pin readings are mutually consistent under the SAME multiplier tuple.

### PV cancellation cross-check (substitution chain Step 2 verification)

The substitution chain Step 2 prediction `a_n^{CC} = Γ(n/2) · (c_1 · M_1^n + c_2 · M_2^n)` is verified at the substrate-IS algebra layer at machine precision:

- **n=2**: `a_2^{CC} = Γ(1) · (2·M_KK² + (-1)·2·M_KK²) = 1 · 0 = 0`. Computed: `a_2_CC = 0.000000e+00`. Verified machine-precision identity (|a_2_CC| / M_KK² = 0; sub-machine-epsilon by construction since the PV consistency `Σ c_r M_r² = 0` holds at machine precision and `a_2_CC` is a direct linear combination of it).
- **n=4**: `a_4^{CC} = Γ(2) · (2·M_KK⁴ + (-1)·4·M_KK⁴) = 1 · (-2·M_KK⁴) = -2·M_KK⁴`. Computed: `a_4_CC = -6.090766e+67`. Predicted: `-2·M_KK⁴ = -2·(7.428660e+16)⁴ = -6.090766e+67`. Relative residual = `|a_4_CC − a_4_predicted| / |a_4_predicted| = 3.93e-16` (sub-machine-epsilon).

Both closed-form identities are STRUCTURAL THEOREMS at the Connes-Chamseddine 1996 §2.2-2.3 spectral-action multiplier layer — they hold as algebraic consequences of `Σ c_r = 1` and `Σ c_r M_r² = 0` regardless of the underlying spectrum, and are confirmed at machine precision by the computation. The substrate-physics finding of this gate is NOT about these structural identities (which trivially hold); it is about whether the regulator-INVARIANT atlas ratio at substrate-distance-1 pole s=3 reproduces the §VII.AF.1.OP-PROJ canonical SDW-residual ratio under the FULL CC PV pipeline. The answer is no, by 2.02% — exceeding the pre-registered 1% FAIL tolerance.

### Connes-Chamseddine 1996 §2.2-2.3 citation

The 2-point Pauli-Villars regularization tuple `(M_1, c_1, M_2, c_2) = (M_KK, +2, √2·M_KK, -1)` is the canonical substrate-IS regularization at the spectral-action UV layer per Connes & Chamseddine, "The Spectral Action Principle" (Commun. Math. Phys. 186, 731-750, 1996), §2.2-2.3 (multiplier-vector grading; spectral-action functional `Tr f(D/Λ)` with smooth cutoff f represented via Gaussian sum). The Pauli-Villars consistency identities `Σ c_r = 1` (UV identity reproduction at λ² → ∞) and `Σ c_r M_r² = 0` (no quadratic divergence; Mellin multiplier-vector grading `f_0^anomaly = 0` per Andrianov-Lizzi 1001.2036 §V) are the substrate-IS algebraic constraints on the regularization tuple. The closed forms `a_2^{CC} = 0` and `a_4^{CC} = -2·M_KK⁴` follow by direct substitution `a_n^{CC} = Γ(n/2)·(c_1·M_1^n + c_2·M_2^n)` and exhaust the structural content of the Seeley-DeWitt expansion at orders n=2 and n=4 under the PV pair. The 2-point PV pair is the minimal-rank regularization compatible with both consistency identities; the upper mass `M_2 = √2·M_KK` and the coefficient pair `(c_1, c_2) = (+2, -1)` are the unique solution.

### Cross-references

- `substrate-first-canonical-sourcing.md §(iv)` — K=4 MANDATORY level-pin discipline; SCHEMATIC vs FULL physical
- `cross-pillar-bridge-anatomy.md §"Level-2 — Algebraic Convergence Envelope"` — L^{-3} envelope at d=4
- `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` — FI/RD/MIXED per-pole taxonomy
- `regulator-pin-discipline.md` — UV-regulator axis Mellin/Pauli-Villars tagging
- `permanent-results-registry.md §VII.AF.1.OP-PROJ` — Pillar III ↔ Pillar IV bridge theorem canonical entry (LANDED S87 W5-1)
- `canonical_constants.py` — `R_universal_HP1_strict_F4 = 1.030902` (canonical pin per W-5 V4); `eps_H_HP1_norm = 16.197719` (PRIMARY per Class-(d) chain); `gv_canonical_difference_FW = -40579.1500479506` (cross-link to §VII.AQ)
- `computations/_pauli_villars_subtraction.py` — PRIMARY FULL physical PV helper (landed S88 W13-159 lizzi)
- `s91_w1_cf70_full_cc_multipliers.py` — sibling FULL CC at substrate-distance-2 pole s=4 (W1 T1.1 §VII.AV gate; cross-pin reference)
- `math-scripts.md §"All Results Are Good Results"` — FAIL informativeness discipline (PASS, FAIL, INFO all are results; convention-shopping forbidden)

### Carry-forward computations (runtime)

1. **S92-VII-AF-1-OP-PROJ-FI-RD-ATLAS-CLASSIFICATION** (4-field spec):
   - **What**: Re-derive `R_universal_HP1_strict_F4` at substrate-distance-1 pole `s=3` across the 5-regulator atlas (ζ-, SDW-, Pauli-Villars FULL-CC, Mellin-, lattice-) at L_max=12 on the master spectrum cache; compute atlas spread and per-class ratio; pre-register FI-vs-RD classification per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` taxonomy.
   - **Inputs**: `s84_spectrum_cache_L12_tau019.npz` (SHA pinned); `canonical_constants.py` pins for `R_universal_HP1_strict_F4` (SDW class) and `rho_FULL(s=3)` (FULL CC class, this gate); the 3 remaining atlas regulators from `_spectral_action_regulators.py`.
   - **Gate**: PASS iff atlas spread `(max − min) / mean < 1e-3` (FI; reclassify §VII.AF.1.OP-PROJ Level-3 anchor as FI); FAIL iff spread `> 1e-2` (RD; reclassify Level-3 anchor as RD); INFO iff 1e-3 ≤ spread ≤ 1e-2 (MIXED).
   - **Effort**: ~1.5 we (compute trivial once helpers loaded; analysis + classification + registry annotation main cost).

2. **S92-VII-AF-1-OP-PROJ-STRUCTURAL-ORTHOGONAL-COMPANION-LANDING** (4-field spec):
   - **What**: Land both `R_universal_HP1_strict_F4 = 1.030902` (SDW canonical) and `rho_FULL(s=3) = 1.0100907902` (FULL CC canonical) as STRUCTURAL-ORTHOGONAL-COMPANION readings at §VII.AF.1.OP-PROJ per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`; emit explicit regulator-class tag on each reading (`a_n^{SDW}` vs `a_n^{Pauli-Villars-CC1996}` per `regulator-pin-discipline.md`).
   - **Inputs**: §VII.AF.1.OP-PROJ registry text (current); both regulator-class numerics (from this gate's npz); cross-pin SHA from this gate's verdict line.
   - **Gate**: Artifact-existence per `wave-classification.md §"M1 PASS predicate type"` (METHODOLOGY-class wave); mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`.
   - **Effort**: ~0.5 we (registry-text edit + audit-script verification).

3. **S92-CC1996-MULTIPLIERS-CONSISTENCY-WITH-VII-AV-CROSS-PIN** (4-field spec):
   - **What**: Cross-pin the FULL CC multiplier tuple `(M_KK, +2, √2·M_KK, -1)` between §VII.AF.1.OP-PROJ (this gate at s=3, `rho_FULL = 1.0101`) and §VII.AV (W1 T1.1 CF-70 at s=4, `Delta_FULL` per CF-70 verdict); land structural-consistency theorem at L_max=12: "Under FULL CC physical multipliers, `rho_FULL(s) − 1` is monotonically increasing in s across substrate-distance-1 and substrate-distance-2 poles on L_max=12 cache; the increase encodes the substrate's regulator-axis subleading expansion at the pole-class level."
   - **Inputs**: this gate's npz (s=3, rho_FULL=1.0101); CF-70 W1 npz (s=4, rho_FULL=1.0220); analytic Friedrich-Bär saturation bound.
   - **Gate**: PASS iff monotonicity `rho_FULL(s=4) > rho_FULL(s=3) > 1` empirically holds (already does: 1.0220 > 1.0101 > 1); STAGE-1-CANDIDATE registry landing for the structural-consistency theorem.
   - **Effort**: ~1.0 we."""

if old_block in text:
    new_text = text.replace(old_block, new_block, 1)
    wp.write_text(new_text, encoding='utf-8')
    print(f"OK -- replaced {len(old_block)} chars with {len(new_block)} chars")
    print(f"Total file size now: {len(new_text)} chars")
else:
    print("ERROR -- old_block not found in file")
    # Diagnostic: show what the file currently contains around the expected area.
    idx = text.find("### Results (filled at runtime)")
    if idx >= 0:
        print(f"Found 'Results (filled at runtime)' at offset {idx}")
        print(repr(text[idx:idx+500]))
    else:
        print("'### Results (filled at runtime)' not found anywhere")
        # try lowercase 'pending'
        idx = text.find("pending")
        if idx >= 0:
            print(f"Found 'pending' at offset {idx}")
            print(repr(text[idx-200:idx+300]))
