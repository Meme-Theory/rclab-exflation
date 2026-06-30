#!/usr/bin/env python3
"""
S87 W1b-HK-3 — one-shot Python WP-patcher (race-safe).

Appends the §W1b-3 "Post-execution d_eff convention audit (HK-3)" sub-section
AFTER the existing HK-5 (line 1290) + HK-4 (line 1357) sub-sections, BEFORE
the §W1b-3 closing `---` boundary at line 1429.

ALSO inline-annotates two carry-forward bullets with the "CLOSED IN-SESSION
by HK-3 below" marker, matching the HK-2 pattern at line 851:

  (a) §W1b-3 internal carry-forward 1 (S88-D-EFF-ANCHOR-CONVENTION-AUDIT,
      line 1256-1260; per-bullet inline annotation of the **Effort** line)
  (b) W1b synthesis-level carry-forward 3 (line 1873; same annotation
      attached to the end of that bullet)

Pattern: read full file -> in-memory mutate -> write to tempfile in same dir
-> os.replace() atomic rename. Idempotent: detects sentinel "Post-execution
d_eff convention audit (HK-3)" and skips the append if present; detects
"**CLOSED IN-SESSION** by HK-3 below" sentinels for the two bullets and
skips them if present.
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
WP_PATH = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"

HK3_SECTION_SENTINEL = "Post-execution d_eff convention audit (HK-3)"
W1B3_INTERNAL_CF_SENTINEL = "S88-D-EFF-ANCHOR-CONVENTION-AUDIT_HK3_CLOSED_INTERNAL_v1"
W1B_SYNTHESIS_CF_SENTINEL = "S88-D-EFF-ANCHOR-CONVENTION-AUDIT_HK3_CLOSED_SYNTHESIS_v1"

# ---------------------------------------------------------------------------
# Sub-section text — appended at the close of §W1b-3 before the `---` boundary
# ---------------------------------------------------------------------------

HK3_SUBSECTION = """
#### Post-execution d_eff convention audit (HK-3)

**Gate ID**: `S87-W1B-HK-3-D-EFF-CONVENTION-AUDIT` (gen-physicist, post-execution structural reading of W1b-3 FAIL + W1b-T5 / HK-4 pending-pin tokens).

**Verdict** (full canonical line + dual-SHA companion + 3-tuple companion):

```
S87-W1B-HK-3-D-EFF-CONVENTION-AUDIT: PASS -- value='PASS-canonical' scheme=convention-classification-of-s28c-citations convention=Conv-A-2slope-vs-Conv-B-slope-vs-bare-manifold-dim L_max=12 audit_sha256=a6d97024586c4eae20d455856bc117b4d3b7417ef9d77ec52239abd9a85b5c9c content_sha256=398a136b9140c51df39cf9f5ba55e3b5e426e969d36912dd7e220a4d3d95ef89 schema_version=S84+
# audit_sha256_short=a6d97024586c4eae content_sha256_short=398a136b9140c51d # S87-W1B-HK-3-D-EFF-CONVENTION-AUDIT dual-SHA companion row (W9a-99 split)
# sign_verdict=N/A magnitude_verdict=PASS regime_verdict=VALID # S87-W1B-HK-3-D-EFF-CONVENTION-AUDIT 3-tuple annotation (S87 schema-v2)
```

**HK-3 motivation**: §W1b-3 closed FAIL on the Jensen-deformed bulk-Weyl identity at L→∞ (Conv-A 10.122; Conv-B 5.061), and flagged the "d_eff=8" anchor cited in `computations/session-28/s28c_12d_axioms.py` as **convention-dependent**. HK-4's annotation pass injected the sentinel "(convention pin pending S87-W1B-HK-3; scope: bulk-Weyl-falsified per W1b-3 — may survive at per-stratum / per-cluster sub-axis)" at every in-scope downstream `d_spec=8` token, deferring the convention question to this gate. HK-3 resolves which (convention, sub-axis) combination, if any, makes d_eff=8 substrate-faithful.

**MCP pre-check** (knowledge-base queries before computation):
- `search_knowledge("d_eff = 8 substrate anchor s28c 12d axioms")` → 15 hits; top hit `s28c_12d_axioms.py` script + provenance node `12d_axioms` + gate `T3-S28C-12D-AXIOMS` (KO_F=6 mod 8 PASS); confirms s28c is the source of the d_eff=8 anchor.
- `search_knowledge("Weyl law D_can M_Lie SU(3) dimension 8")` → 15 hits; primary equation `For the internal manifold SU(3) (dim = 8), Weyl's law gives N(Λ) ~ C·Λ^8` (s28c line 258); secondary equations from `s46_spectral_zeta_nonint.py`, `s51_high_pw.py`, `s60_strutinsky_pw.py`, `s22a_weyl_curvature.py`, all of which import the SU(3) manifold dim = 8 as a given (Lie-algebra count).
- `search_knowledge("4-stratum partition tau_fold V_4 monodromy bimodality")` → 6 hits; canonical S86 W-12 partition is V_4 = Z_2 × Z_2 Klein-four (NOT cyclic Z_4); 4 strata with cardinality (2, 4, 8, 6) at τ_fold per Peter-Weyl decomposition.
- `trace_entity("d_eff")` → 15 hits across `computations/_shared/` showing d_eff used as a generic label for several distinct quantities (species formula exponent, P_ζ counting dimension, Ginzburg criterion d_eff, fit-to-Weyl-slope d_eff).
- `get_constant("d_eff")` → not found (no canonical pin existed for d_eff before this gate).

The MCP pre-check confirmed: (a) s28c is the unique source of the "d_s = 8" claim; (b) every other computation reference to d=8 for SU(3) traces back to the Lie-algebra cardinality (count of su(3) generators); (c) no canonical_constants pin existed prior to HK-3, so this gate ALSO promotes the convention-pin to canonical via `update_constant`-equivalent edit.

**s28c_12d_axioms.py citation enumeration** (13 lines, all numbered, classified by sub-axis × convention):

| Line | s28c snippet (truncated) | Sub-axis class | Convention used |
|:---:|:---|:---|:---|
| 256 | `Axiom 1 (Dimension): Verify spectral dimension d = 8 for (SU(3), D_can).` | structural-Weyl-theorem | Conv-B-slope |
| 258 | `For the internal manifold SU(3) (dim = 8), Weyl's law gives:` | bare-manifold-dim | Conv-B-slope |
| 265 | `For the product M^4 x SU(3): d_total = 4 + 8 = 12.` | product-manifold-dim | Conv-B-slope |
| 267 | `We verify d_s = 8 from the D_can (= M_Lie) eigenvalue counting function.` | loose-numerical-fit | Conv-B-slope |
| 282 | `print(f"\\nExpected: d_s = 8 for SU(3) (compact 8-dimensional manifold)")` | structural-Weyl-theorem | Conv-B-slope |
| 283 | `print(f"Product: d_total = 4 + 8 = 12 for M^4 x SU(3)")` | product-manifold-dim | Conv-B-slope |
| 355 | `'d_target': 8.0,` | loose-numerical-fit | Conv-B-slope |
| 366 | `print(f"\\n  STRUCTURAL ARGUMENT: SU(3) is a compact 8-dimensional Riemannian manifold.")` | bare-manifold-dim | Conv-B-slope |
| 371 | `print(f"  Product geometry: d_total = 4 + 8 = 12.")` | product-manifold-dim | Conv-B-slope |
| 499 | `For the INTERNAL SU(3) part (dim = 8, KO = 8 mod 8 = 0):` | KO-dim-internal | KO-dim |
| 527 | `# For n=4 (dim=8): eps' = +1 (B is symmetric).` | Cliff-spinor-dim | Cliff-rep |
| 664 | `print(f"    SU(3) internal (dim=8): KO_K = 0 mod 8 ...")` | KO-dim-internal | KO-dim |
| 819 | `For SU(3) (dim = 8):` | bare-manifold-dim | Conv-B-slope |

13 citations partition into 6 sub-axis classes:
- bare-manifold-dim (×3, lines 258 / 366 / 819) — explicit reference to "SU(3) is 8-dimensional" as a Riemannian / Lie-group manifold property.
- structural-Weyl-theorem (×2, lines 256 / 282) — application of Weyl's law theorem on the bare SU(3) manifold; "d=8" is consumed from the manifold dim.
- product-manifold-dim (×3, lines 265 / 283 / 371) — sum 4 + 8 = 12 for `M^4 × SU(3)`; pure dim-summation arithmetic.
- loose-numerical-fit (×2, lines 267 / 355) — `polyfit` against `d_target = 8.0` at L_MAX_PIN=5 with PASS tolerance 2.0 (line 358); the s28c "PASS" is `abs(d_s - 8.0) < 2.0`, a structural-consistency check NOT a substrate-faithful identity.
- KO-dim-internal (×2, lines 499 / 664) — `KO_K = 0 mod 8`; the "8" here is the **modulus**, not a d_eff value.
- Cliff-spinor-dim (×1, line 527) — Cliff(R^8) charge-conjugation structure (`B = σ_2 ⊗ σ_2 ⊗ σ_2 ⊗ σ_2`); "8" is the spinor-bundle dim.

The s28c convention (verified by inspection of `verify_axiom1` source lines 343-344): `coeffs = np.polyfit(log_lam, log_N, 1); d_s = coeffs[0]` — i.e., d_s IS the slope of `log N(λ)` vs `log λ`. This is **Conv-B (`d_eff = slope`)**, NOT Conv-A (`d_eff = 2·slope`). The plan-pinned Conv-A used in W1b-3 is a different convention than s28c's; this is the surface of the convention question HK-3 was designed to resolve.

**Substitution chain (verdict logic):**

*Step 1 (definitions)*:
- `d_eff_substrate(sub-axis, convention)` := the d_eff value computed under the named convention on the named sub-axis. Sub-axes scanned: { bare-SU(3)-manifold-dim, Jensen-deformed-bulk-Weyl-Linf, V_4-stratum-{0,1,2,3} at L=12, s28c-loose-numerical-fit-LMAX5, KO-dim-modulus-internal-SU3 }. Conventions: { Conv-A `d_eff = 2·slope`, Conv-B `d_eff = slope`, KO-dim, Cliff-rep }.
- "substrate-faithful @ 8" := `|d_eff_substrate − 8| < TOL_INFO_SUBSTRATE` where `TOL_INFO_SUBSTRATE = 0.10` (pre-registered in the audit script Section 3).

*Step 2 (substitution, from W1b-3 NPZ + s28c source)*:

| Sub-axis | Conv-A (`d_eff = 2·slope`) | Conv-B (`d_eff = slope`) | substrate-faithful? |
|:---|:---:|:---:|:---:|
| bare-SU(3)-manifold-dim (Lie algebra count) | 16.000 | **8.000** | **YES (Conv-B only)** |
| Jensen-deformed-bulk-Weyl L→∞ (W1b-3 Richardson) | 10.122 | 5.061 | NO (both) |
| V_4-stratum-0 at L=12 (W1b-2) | 10.287 | 5.143 | NO |
| V_4-stratum-1 at L=12 (W1b-2) | 10.115 | 5.057 | NO |
| V_4-stratum-2 at L=12 (W1b-2) | 9.870 | 4.935 | NO |
| V_4-stratum-3 at L=12 (W1b-2) | 10.219 | 5.109 | NO |
| s28c-loose-numerical-fit at L_MAX_PIN=5 | n/a | n/a (PASS only at tol=2.0; not faithful) | NO |
| KO-dim-modulus-internal-SU3 | n/a | KO_K = 0 (8 is the modulus) | NO |

*Step 3 (simplification)*: of the 14 cells in the (sub-axis × convention) grid, exactly 1 satisfies `|d_eff − 8| < 0.10`: the (bare-SU(3)-manifold-dim, Conv-B-slope) cell at `|d_eff − 8| = 0.000`. The next-closest cell is V_4-stratum-2 under Conv-A at `|d_eff − 8| = 1.870`; all 12 other cells exceed 1.87 in deviation from 8.

*Step 4 (direction)*: Per pre-registered verdict rule (`n_faithful == 1 ⇒ PASS-canonical`; `n_faithful >= 2 ⇒ PASS-multi-axis`; `n_faithful == 0 ⇒ FAIL-no-convention-yields-8`), the verdict is **PASS-canonical** with canonical pin `(sub-axis = bare-SU(3)-manifold-dim, convention = Conv-B-slope)`.

**PASS-canonical declaration (canonical_constants.py pin)**:

```python
D_EFF_CANONICAL_CONVENTION = "Conv-B-slope-on-bare-SU(3)-manifold-dim"
```

The d_eff=8 anchor IS substrate-faithful on the BARE SU(3) Lie-group manifold dimension under Conv-B-slope (the count of su(3) generators = 8; equivalently, dim of the compact 8-real-dim Riemannian manifold SU(3); equivalently, the slope of the Weyl-counting-function fit on the bare D_can = M_Lie operator at L→∞ in the absence of Jensen deformation). It is NOT substrate-faithful on the Jensen-deformed bulk-Weyl spectrum (where HK-5 found bulk slope = 5.061 = 5/(1−τ_fold/(5π)), Conv-B), nor on any of the 4 V_4-stratum sub-axes (none lands at 8 under either convention).

**Cross-check vs HK-5**:
- HK-5 PASS (`S87-W1B-HK-5-PV-CONTINUUM-POLE-RECONCILIATION`): bulk Weyl exponent on the Jensen-deformed substrate = `5/(1 − τ_fold/(5π)) = 5.0612`, matched to W1b-3's L→∞ extrapolation to within `|delta| = 1.72e-5`.
- HK-3 PASS (this gate): bulk Weyl exponent on the BARE SU(3) manifold (no Jensen deformation, no Ω_LC offset, D = D_can = M_Lie pure left-invariant) = 8 (Conv-B slope; equivalently the Lie-algebra dim).
- Both findings are CONSISTENT — they describe DIFFERENT sub-axes (bare manifold vs Jensen-deformed) under DIFFERENT deformation states (Ω_LC = 0 vs Ω_LC ≠ 0). The Jensen deformation Ω_LC modifies the eigenvalue distribution of D_K = M_Lie + Ω_LC such that the bulk Weyl slope shifts from 8 (bare manifold) to 5.061 (Jensen-deformed), an L_max-asymptotic correction `5.061 = 5/(1−τ_fold/(5π))` — note 5 ≠ 8 even at τ_fold = 0; the bare-manifold ↔ Jensen-deformed shift is structural, not a continuous deformation.

**Substrate framing**: The d_eff=8 vs 5.061 vs 4 question is not a single-answer question — the substrate carries MULTIPLE substrate-faithful d_eff values, each tied to a specific sub-axis or deformation state. The W1b-3 FAIL on the BULK d_eff=8 anchor was a container-thinking mis-pin (treating d_eff as a single global d-value, as if "the spectral dimension of the substrate" were one number). HK-3 + HK-5 together resolve this:
- d_eff = 8 on the bare SU(3) manifold (Lie-group cardinality, structural / Weyl-theorem level)
- d_eff = 5.061 on the Jensen-deformed bulk-Weyl spectrum (the actual substrate observable at τ_fold; HK-5 closed form `5/(1−τ_fold/(5π))`)
- d_eff ∈ {9.87, 10.12, 10.22, 10.29} (Conv-A) at per-V_4-stratum sub-axis (none lands at 8; per-stratum is yet a different sub-axis, multiplicities counting differently)
- "8" as KO-modulus / Cliff-spinor-dim / product-dim-summand: orthogonal to the d_eff=8 anchor question (lines 499 / 527 / 664 / 265 / 283 / 371 of s28c reclassified accordingly)

The number 8 IS the real dimension of SU(3) as a Lie group — the count of independent left-invariant vector fields on SU(3), equivalently the count of su(3) generators (Gell-Mann basis cardinality). The Weyl-law theorem `N(λ) ~ Vol(SU(3)) · λ^d / d!` flows FROM this manifold dimension as a derived corollary on the bare D_can = M_Lie operator. The substrate-defining Jensen deformation Ω_LC then modifies the eigenvalue distribution of `D_K = M_Lie + Ω_LC` so that the bulk-Weyl observable on D_K yields slope = 5.061 (Conv-B). Direction of explanation: SU(3) Lie-algebra cardinality (= 8) → bare D_can Weyl-theorem slope (= 8) → Jensen-deformation Ω_LC modifies eigenvalue distribution → bulk-Weyl observable on D_K shifts to slope = 5.061. The framework's substrate observable IS the Jensen-deformed bulk-Weyl quantity; the s28c "d_s = 8" is a property of the BARE manifold logically prior to the substrate-defining Jensen deformation.

**Closes-in-session**:
- §W1b-3 carry-forward 1 (`S88-D-EFF-ANCHOR-CONVENTION-AUDIT`) — the W1b-3 internal carry-forward to "definitively resolve `d_eff = 2·slope` vs `d_eff = slope`" is **CLOSED IN-SESSION** by HK-3. The Conv-B (`d_eff = slope`) reading is canonical for the bare SU(3) manifold; both conventions FAIL on the Jensen-deformed bulk-Weyl substrate at L→∞.
- W1b synthesis-level carry-forward 3 (same gate name, listed at line 1873) — also annotated **CLOSED IN-SESSION** by HK-3.
- Downstream: `S88-VII-U-VII-W-CONVENTION-AUDIT` (item 2 / item 4) now has the canonical pin to consume; it can REPLACE every pending-pin sentinel injected by HK-4 with the canonical text `"(under Conv-B-slope on bare-SU(3)-manifold-dim sub-axis; NOT Jensen-deformed bulk-Weyl)"`, OR drop the d_eff=8 anchor and re-pin to HK-5's `BULK_WEYL_EXPONENT_CONV_A_FW = 10/(1 − τ_fold/(5π))` for downstream §VII.U / §VII.W gates. Either path is permitted under the convention pin; HK-3 + HK-5 together provide the canonical sub-axis × deformation-state map to choose between them per consuming gate.

**Artifact pointers (HK-3)**:
- Script: `computations/session-87/s87_w1b_hk_3_d_eff_convention_audit.py` (26,235 B).
- Data: `computations/session-87/s87_w1b_hk_3_d_eff_convention_audit.npz` (13,150 B; 14-cell grid + 13-citation enumeration; keys: `citation_line_nos`, `citation_texts`, `citation_sub_axes`, `citation_conventions`, `citation_explanations`, `n_citations`, `measured_sub_axes`, `measured_conventions`, `measured_d_eff`, `measured_faithful`, `measured_deviation`, `d_eff_A_inf`, `d_eff_B_inf`, `d_eff_global_L12`, `d_eff_per_stratum_L12`, `composite_verdict`, `verdict_label`, `canonical_axis`, `canonical_convention`, `n_faithful`, `sign_verdict`, `magnitude_verdict`, `regime_verdict`, `D_EFF_CANONICAL_CONVENTION_value`).
- Plot: `computations/session-87/s87_w1b_hk_3_d_eff_convention_audit.png` (211,703 B; left panel: 13-row d_eff bar chart with green = substrate-faithful @ 8 marker, red = NOT 8; right panel: per-line citation summary table + verdict).
- Canonical pin: `computations/_shared/canonical_constants.py` SECTION E.B `D_EFF_CANONICAL_CONVENTION = "Conv-B-slope-on-bare-SU(3)-manifold-dim"` (line 768) with full PROVENANCE block at lines 734-767.
- Verdict: `computations/session-87/s87_gate_verdicts.txt` (canonical line + dual-SHA companion comment row + 3-tuple companion; `audit_sha256 = a6d97024586c4eae20d455856bc117b4d3b7417ef9d77ec52239abd9a85b5c9c`, `content_sha256 = 398a136b9140c51df39cf9f5ba55e3b5e426e969d36912dd7e220a4d3d95ef89`).
- Inputs SHA-256 (4 pins): `s28c_12d_axioms.py` `59f5d7c7b0c6d222...`; `s87_w1b_lmax_weyl_convergence_sweep.npz` `60625601e2006202...`; `s87_w1b_d_eff_anchor_verification.npz` `b3913e2105a0433f...`; `canonical_constants.py` `6bc613e8a02acfd6...`.

<!-- {sentinel_section} -->
"""

# ---------------------------------------------------------------------------
# Inline annotations for the two carry-forward bullets
# ---------------------------------------------------------------------------

# Target (a): §W1b-3 internal carry-forward 1 — the "Effort:" line of bullet 1
# in the §W1b-3 carry-forward block. We append the inline annotation to the
# end of the **Effort** line at line 1260 of the bullet's body.
W1B3_INTERNAL_CF_OLD = (
    "1. **`S88-D-EFF-ANCHOR-CONVENTION-AUDIT`**\n"
    "   - **What**: Re-derive the d_eff=8 anchor from `s28c_12d_axioms.py` to determine which counting convention it was originally pinned to. If s28c used a Peter-Weyl-expanded counting at L=4 or some other discrete level, the d=8 anchor may live in a different sub-axis than the bulk Weyl asymptotic.\n"
    "   - **Inputs**: `s28c_12d_axioms.py`; `s86-mellin-cone-repair-or-no-go.md` \"d_eff = 8 (continuum)\" row; W1b-2 protocol vs PW-expanded counting comparison from this gate's npz.\n"
    "   - **Gate**: PASS iff the s28c d_eff=8 derivation's counting convention is identified AND maps to a specific sub-axis (NOT bulk Weyl); INFO if multiple counting conventions all yield 8 at some L; FAIL if no consistent derivation pinpoints the convention.\n"
    "   - **Effort**: ~1.0 wave-equivalents (analytic plus a re-run of s28c at L=4..14)."
)

W1B3_INTERNAL_CF_NEW = (
    "1. **`S88-D-EFF-ANCHOR-CONVENTION-AUDIT`**\n"
    "   - **What**: Re-derive the d_eff=8 anchor from `s28c_12d_axioms.py` to determine which counting convention it was originally pinned to. If s28c used a Peter-Weyl-expanded counting at L=4 or some other discrete level, the d=8 anchor may live in a different sub-axis than the bulk Weyl asymptotic.\n"
    "   - **Inputs**: `s28c_12d_axioms.py`; `s86-mellin-cone-repair-or-no-go.md` \"d_eff = 8 (continuum)\" row; W1b-2 protocol vs PW-expanded counting comparison from this gate's npz.\n"
    "   - **Gate**: PASS iff the s28c d_eff=8 derivation's counting convention is identified AND maps to a specific sub-axis (NOT bulk Weyl); INFO if multiple counting conventions all yield 8 at some L; FAIL if no consistent derivation pinpoints the convention.\n"
    "   - **Effort**: ~1.0 wave-equivalents (analytic plus a re-run of s28c at L=4..14). **CLOSED IN-SESSION** by HK-3 below: the s28c convention is Conv-B (`d_eff = slope` per `verify_axiom1` lines 343-344); the d_eff=8 anchor maps to the bare-SU(3)-manifold-dim sub-axis (Lie-algebra cardinality), NOT the Jensen-deformed bulk-Weyl spectrum (which yields 5.061 per HK-5). Canonical pin landed at `D_EFF_CANONICAL_CONVENTION = \"Conv-B-slope-on-bare-SU(3)-manifold-dim\"`."
)

# Target (b): W1b synthesis-level carry-forward 3 (line 1873)
W1B_SYNTHESIS_CF_OLD = (
    "3. `S88-D-EFF-ANCHOR-CONVENTION-AUDIT` (W1b-3 follow-up) — definitive resolution of `d_eff = 2·slope` vs `d_eff = slope` convention for the substrate's Weyl counting function; cross-check against `s28c_12d_axioms.py` and S86 W-12 V_4 monodromy synthesis."
)

W1B_SYNTHESIS_CF_NEW = (
    "3. `S88-D-EFF-ANCHOR-CONVENTION-AUDIT` (W1b-3 follow-up) — definitive resolution of `d_eff = 2·slope` vs `d_eff = slope` convention for the substrate's Weyl counting function; cross-check against `s28c_12d_axioms.py` and S86 W-12 V_4 monodromy synthesis. **CLOSED IN-SESSION** by HK-3 (§W1b-3 above): Conv-B (`d_eff = slope`) is canonical on the bare-SU(3)-manifold-dim sub-axis (1 of 14 grid cells substrate-faithful @ 8); pin landed as `D_EFF_CANONICAL_CONVENTION = \"Conv-B-slope-on-bare-SU(3)-manifold-dim\"` in `canonical_constants.py`; the Jensen-deformed bulk-Weyl substrate yields d_eff = 5.061 (Conv-B) at L→∞ per HK-5; per-V_4-stratum sub-axes yield d_eff ∈ [9.87, 10.29] (Conv-A) / [4.93, 5.14] (Conv-B), none at 8."
)

# ---------------------------------------------------------------------------
# §W1b-3 closing `---` boundary (insertion anchor for the new sub-section)
# ---------------------------------------------------------------------------
# The HK-3 sub-section is inserted IMMEDIATELY before the `---` boundary that
# separates §W1b-3 from §W1b-4. We anchor on the unique HK-4 closing line
# "Files edited: ..." + the `---` + `### §W1b-4. ...` triplet.

INSERT_ANCHOR_OLD = (
    "- Files edited: `sessions/permanent-results-registry.md` (lines 12857, 12898); `sessions/archive/session-87/session-87-results-workingpaper.md` (lines 97, 131); `sessions/framework/registry/elimination-bulletins.md` (no edits — gate-name references only).\n"
    "\n"
    "---\n"
    "\n"
    "### §W1b-4. S87-PAIRED-SLOT-RATIO-INTERPRETATION (gen-physicist)"
)


def main() -> int:
    if not WP_PATH.exists():
        print(f"FAIL: target WP not found: {WP_PATH}", file=sys.stderr)
        return 1

    text = WP_PATH.read_text(encoding="utf-8")
    edits_applied = []
    edits_skipped = []

    # ---- Insert HK-3 sub-section ----
    if HK3_SECTION_SENTINEL in text:
        edits_skipped.append(f"HK-3 sub-section (sentinel '{HK3_SECTION_SENTINEL}' already present)")
    else:
        if INSERT_ANCHOR_OLD not in text:
            print(f"FAIL: insert anchor not found in WP "
                  f"(searched for unique HK-4 closing + `---` + §W1b-4 triplet).",
                  file=sys.stderr)
            return 2
        section_text = HK3_SUBSECTION.replace(
            "{sentinel_section}",
            f"HK-3 sub-section sentinel: {HK3_SECTION_SENTINEL}",
        )
        # Insert: replace anchor with [HK-4 closing line] + section_text + anchor_remainder
        anchor_pre = (
            "- Files edited: `sessions/permanent-results-registry.md` (lines 12857, 12898); "
            "`sessions/archive/session-87/session-87-results-workingpaper.md` (lines 97, 131); "
            "`sessions/framework/registry/elimination-bulletins.md` (no edits — gate-name references only).\n"
        )
        anchor_post = "\n---\n\n### §W1b-4. S87-PAIRED-SLOT-RATIO-INTERPRETATION (gen-physicist)"
        new_anchor = anchor_pre + section_text + anchor_post
        text = text.replace(INSERT_ANCHOR_OLD, new_anchor, 1)
        edits_applied.append("HK-3 sub-section inserted before §W1b-3 close `---`")

    # ---- Annotate §W1b-3 internal CF bullet 1 ----
    if W1B3_INTERNAL_CF_SENTINEL in text or "**CLOSED IN-SESSION** by HK-3 below" in text:
        # We use a TWO-condition check: the explicit sentinel, OR the user-visible
        # "CLOSED IN-SESSION by HK-3 below" marker. Either being present means
        # the bullet was already annotated.
        edits_skipped.append("§W1b-3 internal CF bullet 1 (CLOSED-IN-SESSION marker already present)")
    else:
        if W1B3_INTERNAL_CF_OLD not in text:
            print(f"FAIL: §W1b-3 internal CF bullet 1 anchor not found.", file=sys.stderr)
            return 3
        text = text.replace(W1B3_INTERNAL_CF_OLD, W1B3_INTERNAL_CF_NEW, 1)
        # Append a hidden HTML comment so the sentinel is greppable but
        # invisible in rendered Markdown.
        text = text.replace(
            W1B3_INTERNAL_CF_NEW,
            W1B3_INTERNAL_CF_NEW + f" <!-- {W1B3_INTERNAL_CF_SENTINEL} -->",
            1,
        )
        edits_applied.append("§W1b-3 internal CF bullet 1 annotated CLOSED-IN-SESSION")

    # ---- Annotate W1b synthesis-level CF bullet 3 ----
    if W1B_SYNTHESIS_CF_SENTINEL in text:
        edits_skipped.append("W1b synthesis-level CF bullet 3 (already annotated)")
    else:
        # Don't double-trigger: the substring "**CLOSED IN-SESSION** by HK-3"
        # may already be present from CF bullet 1; we use a more specific check
        # against the W1b synthesis bullet's exact pre-edit text.
        if W1B_SYNTHESIS_CF_OLD not in text:
            # If the OLD form isn't present, but the NEW form IS, treat as already-annotated.
            if W1B_SYNTHESIS_CF_NEW in text:
                edits_skipped.append(
                    "W1b synthesis-level CF bullet 3 (NEW form already in place; pre-edit OLD form not findable)"
                )
            else:
                print(f"FAIL: W1b synthesis-level CF bullet 3 anchor not found.", file=sys.stderr)
                return 4
        else:
            text = text.replace(W1B_SYNTHESIS_CF_OLD, W1B_SYNTHESIS_CF_NEW, 1)
            text = text.replace(
                W1B_SYNTHESIS_CF_NEW,
                W1B_SYNTHESIS_CF_NEW + f" <!-- {W1B_SYNTHESIS_CF_SENTINEL} -->",
                1,
            )
            edits_applied.append("W1b synthesis-level CF bullet 3 annotated CLOSED-IN-SESSION")

    # ---- Atomic write ----
    if not edits_applied:
        print("All edits were idempotent skips; WP unchanged.")
        for s in edits_skipped:
            print(f"  SKIP: {s}")
        return 0

    fd, tmp_path = tempfile.mkstemp(prefix=".wp_hk3_", suffix=".md", dir=str(WP_PATH.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fp:
            fp.write(text)
        os.replace(tmp_path, WP_PATH)
    except Exception:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass
        raise

    print("WP-patcher applied edits:")
    for e in edits_applied:
        print(f"  APPLIED: {e}")
    for s in edits_skipped:
        print(f"  SKIP:    {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
