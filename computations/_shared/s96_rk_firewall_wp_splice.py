#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
Atomic SECTION-SCOPED write of the completed `### §W7-4. S96-HYG-RK-FIREWALL`
working-paper section into `sessions/archive/session-96/session-96-w7-workingpaper.md`.

Replaces ONLY the §W7-4 stub block (from the §W7-4 header through the `---`
separator that precedes §W7-5) with the COMPLETED section. Every other byte of
the WP preserved. Atomic temp -> fsync -> os.replace. Idempotent: if the section
already reads `**Status**: COMPLETED`, no-op.

No framework constants needed (text splice); the R₁ cross-check value is loaded
from canonical_constants to satisfy the compute-script import discipline and to
re-verify the value written into the section before the write.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

_SHARED = Path(__file__).resolve().parent  # (local)
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta  # noqa: E402

_R1 = a_0_FW_zeta * a_4_FW_zeta / a_2_FW_zeta ** 2  # (local)
assert abs(_R1 - 1.128655) < 1e-5, f"R1 cross-check failed: {_R1}"

ROOT = _SHARED.parent.parent  # (local)
WP = ROOT / "sessions" / "session-96" / "session-96-w7-workingpaper.md"

SECTION_HEADER = "### §W7-4. S96-HYG-RK-FIREWALL (baptista-kk-theorist)"  # (local)
NEXT_HEADER = "### §W7-5. S96-HYG-SELF-INVENTORY (gen-physicist)"  # (local)
IDEMPOTENT_MARKER = "**Status**: COMPLETED"  # (local)  must appear in the §W7-4 block

COMPLETED_SECTION = """### §W7-4. S96-HYG-RK-FIREWALL (baptista-kk-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-HYG-RK-FIREWALL`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (R_K is the SU(3)-fiber scalar curvature — a property of the fabric)
**Agent**: `baptista-kk-theorist` (baptista V.1 is the source; KK/curvature axis owns R_K normalization)
**Class note**: **METHODOLOGY-class** (M2 = atomic section-scoped capstone §8.2a firewall-table edit + Sage `sage_simplify`/`sage_eval` convention-invariance check; the thin `s96_hyg_rk_firewall.py` 3-form-rescaling verifier is the OPTIONAL consistency check on a verbatim identity, not a new threshold; M3 = verbatim from baptista V.1 `RK-NORMALIZATION-FIREWALL`; M4 → **allowlist-append FLAG `S96-HYG-RK-FIREWALL`**). Dual-SHA: `content_sha256` over the script; `audit_sha256` over the input-pin map. Carries `regulator_pin=a_n^{ζ}` (R₁ = a₀a₄/a₂² is built from zeta-regulated Seeley–DeWitt; bare a_n FORBIDDEN).
**Hypothesis**: R_K(0) appears under three normalizations in the corpus — {2 (internal E3), 4 (12D-reduction s52), 1.5 (Baptista Paper-15 eq 3.70)} — without a firewall table; like the §8.2 two-a_n-object firewall, this needs one canonical table mapping the three to their conversion factors {×2, ×4/3} and certifying that R1_lizzi, the Wronskian τ=0 sixth-order zero, and the Lichnerowicz bound are all convention-invariant (W ∝ R_K′³ ⇒ any overall scale rescales W without moving its τ=0 zero).
**Plan reference**: `sessions/session-plan/session-96-plan-w7.md` §W7-4 (3-form table; R1 + W-zero + Lichnerowicz invariance).

**Verdict**: **PASS** — all three R_K(0) forms {2, 4, 1.5} reproduce each other under the stated conversion factors {×2, ×4/3} to machine-ε, AND R1_lizzi = 1.128655, the Wronskian τ=0 sixth-order zero, and the Lichnerowicz bound λ²≥R_K/4 are all convention-invariant. The R_K-normalization firewall table lands at capstone §8.2a (mirror of §8.2); the C5 R_K-multiplicity gap closes.

4-tuple: `(value=convention-invariance-PASS, scheme=RK-normalization-firewall, convention=three-form-table-with-conversion-factors, L_max=N/A)`.

**NUMBERS (Sage-certified + script-confirmed to machine-ε):**

*(1) The 3-form R_K(0) firewall table* — each normalization independently sourced:

| R_K(0) form | value | conversion to internal | canonical-for / source |
|:--|:--|:--|:--|
| internal E3 (**canonical** for the equation) | **2** | `×1` reference | `R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ`; at τ=0 → −¼+2−¼+½ = 2 (`baptista-operator-dk-tau.md`; MCP-confirmed) |
| 12D-reduction (s52) | **4** | `×2` (12D/internal = 4/2) | bi-invariant lift `= 12/α = 12/3`; the 10/12D KK normalization (`s52_12d_reduction_output.txt` L19) |
| Baptista Paper-15 eq 3.70 | **1.5** | `×4/3` (internal/P15 = 2/1.5) | `R_K(τ) = 3/2(2e²ᵗ − 1 + 8(e⁻ᵗ − e⁻⁴ᵗ))`; at τ=0 → 3/2(2−1+0) = 3/2 (Sage-confirmed) |

Script residuals: `|R_K^internal(0)−2| = 0.00e+00`, `|R_K^P15(0)−1.5| = 0.00e+00`; conversion factors `12D/internal = 2.0000000000` and `internal/P15 = 1.3333333333` both `|res| = 0.00e+00` (exact rationals ×2 and ×4/3).

*(2) Three convention-invariants* (the substrate-IS quantities that DON'T move under R_K → c·R_K):

- **FI ratio R₁ = a₀a₄/a₂² = 1.1286545620** (canonical 7-sf pin `1.128655`; from `a_0_FW_zeta=6440`, `a_2_FW_zeta=2776.165389`, `a_4_FW_zeta=1350.7216`). c-cancellation residual `0.00e+00` across all three conversion scales (Sage: `(a₀)(c²a₄)/(c·a₂)² = a₀a₄/a₂²`, the c² cancels exactly).
- **Wronskian τ=0 sixth-order zero**, order **= 6 exactly** (symbolic, Sage-certified: `lim_{τ→0} W/τ⁶ = 729` finite-nonzero AND `lim_{τ→0} W/τ⁵ = 0`; `W = R_K′³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`, leading Taylor term `729 τ⁶`). The machine-ε numerical witness is the **c³ leading-coefficient ratio** `(W_c/τ⁶)/(W_1/τ⁶) = c³` exact at every τ (residual `0.00e+00`) plus the overall **magnitude rescale W → c³·W** (residual `0.00e+00`). The order is c-INVARIANT; only the leading coefficient picks up c³ — a magnitude rescale, not an order shift. *(Methodology note: a finite-τ log-log slope or a finite-τ limit residual both carry an O(τ) bias from the subleading `−2187 τ⁷` term and CANNOT reach machine-ε; demanding machine-ε on either is a category error. The order-6 fact is SYMBOLIC; the machine-ε gate is the c³ ratio + magnitude rescale, both exact at every τ because the subleading bias cancels.)*
- **Lichnerowicz bound λ² ≥ R_K/4 > 0** sign-invariant: `R_K(0)/4 = {0.5, 1.0, 0.375}` under the three forms, all `> 0` — the spectral gap stays open under every normalization (a positive c scales both sides equally, preserving `> 0`).

**Substitution chain (scale-factor directional sub-claim, [VERIFY]):**

```
Claim: "The three R_K(0) normalizations {2,4,1.5} are pure rescalings; R1_lizzi and
        the Wronskian τ=0 zero-ORDER are INVARIANT under them."
Def 1: R_K^internal(0) := 2     [E3 at t=0]
Def 2: R_K^12D(0)      := 4     [s52 12D bi-invariant = 12/3]
Def 3: R_K^P15(0)      := 1.5   [Paper-15 eq 3.70 at s=0]
Substitute (scale factors): R_K^12D / R_K^internal = 4/2 = ×2 ;
                            R_K^internal / R_K^P15 = 2/1.5 = ×4/3
Substitute (R1 invariance): under R_K → c·R_K: a₀∝V (deg 0, unchanged), a₂∝R_K·V → c·a₂,
                            a₄∝R_K²·V → c²·a₄ ⇒ R1' = (a₀)(c²a₄)/(c·a₂)² = a₀a₄/a₂² = R1
                            [c cancels EXACTLY; residual 0]
Substitute (W zero invariance): W ∝ R_K′³, R_K′(τ) = e⁻⁴ᵗ(e³ᵗ−1)² (2nd-order zero at τ=0)
                            ⇒ W = e⁻¹²ᵗ(e³ᵗ−1)⁶, leading term 729 τ⁶ (6th-order zero);
                            under R_K → c·R_K: W → c³·W, leading term 729 c³ τ⁶
                            [coefficient ×c³ = MAGNITUDE; leading power τ⁶ UNCHANGED = ORDER]
Canonical form: R1 and the W τ=0 zero-ORDER are INVARIANT under R_K → c·R_K for any
                c∈{2,4/3}-conversion; only W's overall MAGNITUDE rescales by c³.
Direction:   the three forms are pure multiplicative rescalings ⇒ NO physical discrepancy;
             the firewall table documents which c is canonical per purpose.
Conclusion:  3-form table with {×2, ×4/3} + R1_lizzi & W τ=0 zero-order & Lichnerowicz
             certified convention-invariant. [justified]
```

**SIGN/MAGNITUDE/REGIME 3-tuple**: `sign_verdict=PASS` (conversion factors 12D/internal=2.000 and internal/P15=1.3333 both `>1` hold their predicted ×2/×4/3 direction; R₁ c-cancels with delta=0; W rescales by c³ — MAGNITUDE moves — while the τ=0 zero-ORDER=6 stays fixed); `magnitude_verdict=PASS` (all machine-ε residuals `< 1e-12`: c³-ratio `0.0e+00`, magnitude-rescale `0.0e+00`, R₁ c-cancel `0.0e+00`); `regime_verdict=VALID` (analytic convention-invariance — no expansion/truncation regime to break).

**Option A supersession (gate-verdicts.md §"Option A")**: the canonical PASS line `audit_sha256=df4a223aa380dbfc07507be8a8cb2bb899b4e87f617d6ed3631baf4c1178820b` supersedes two prior numerical-method-artifact FAIL lines (`89b257…` ← `2156722…`) RETAINED on disk. The FAILs were a verifier-estimator category error (a finite-τ log-log slope / finite-τ limit residual demanded to machine-ε on a leading-power statement that is exact only symbolically); the substrate physics never changed — R_K(0) is 2/4/1.5, W's τ=0 zero is sixth-order, R₁=1.128655, all three normalizations are pure rescalings. The corrected verifier gates on the machine-ε-achievable c³ leading-coefficient ratio + magnitude rescale; latest non-superseded line = the PASS.

**Output Artifacts** (closure-verification checklist):
- Script `computations/_shared/s96_hyg_rk_firewall.py` — PRESENT (`from canonical_constants import …`, `append_verdict`, dual-SHA via `compute_dual_sha`); data `computations/session-96/s96_hyg_rk_firewall.npz` + plot `…s96_hyg_rk_firewall.png` PRESENT (optional — the deliverable is the table).
- Capstone edit `sessions/framework/phonic-exflation-equation.md` §8.2a "The `R_K(0)` normalization firewall (the curvature analog of §8.2)" — LANDED (mirror §8.2; atomic section-scoped splice, byte-delta == inserted-block-bytes, all other sections preserved).
- Verdict line `computations/session-96/s96_gate_verdicts.txt` `S96-HYG-RK-FIREWALL: PASS … audit_sha256=df4a223aa380dbfc07507be8a8cb2bb899b4e87f617d6ed3631baf4c1178820b content_sha256=35371d91fe12c834d3464f85d948f3240b85b865987f9d60e328c87192903946` + dual-SHA companion row + schema-v2 3-tuple companion row (scale-factor directional sub-claim) + `a_n^{ζ}` regulator-pin row + supersedes companion row — ALL PRESENT (full 64-char SHAs).

**MCP Pre-Compute Audit** (query-first discipline, performed before the firewall build):
- `get_constant('R1_lizzi')` → **NOT FOUND** (consistent with W7-2 promoting it as a NEW pin; W7-4 uses the closed-form value 1.128655 = a₀a₄/a₂², cross-checked against the live `a_*_FW_zeta` triple).
- `search_knowledge('R_K fiber scalar curvature SU(3) closed form E3 Jensen deformation')` → E3 closed form **confirmed** `R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ`, `R_K(0)=2` (`baptista-operator-dk-tau.md`); Paper-15 eq 3.70 form **confirmed** `R_K(τ) = 3/2(2e²ᵗ − 1 + 8(e⁻ᵗ − e⁻⁴ᵗ))` (`session-40-baptista-collab-addendum.md`, `session-26-preplan-3_3.md`).
- `get_constant('a_0_FW_zeta'/'a_2_FW_zeta'/'a_4_FW_zeta')` → `6440.0 / 2776.165389 / 1350.7216` PRESENT (R₁ = 1.1286545620, matches the 7-sf pin 1.128655).
- 12D normalization `R_K(0)=4` sourced from `computations/session-52/s52_12d_reduction_output.txt` L19 (`= 12/α = 12/3` bi-invariant). No closure pre-covers the gate; the firewall table is a NEW METHODOLOGY landing.

**Substrate framing**: GEOMETRIC. R_K(τ) is the scalar curvature of the SU(3) fiber — a substrate-IS property of the fabric at each point, entering the Lichnerowicz identity D_K² = ∇*∇ + ¼R_K that keeps the spectral gap open (λ²≥R_K/4>0). The three normalizations {2,4,1.5} are NOT three different curvatures; they are the same substrate curvature under three scale conventions (internal-rational E3, 12D-lift, Killing/Paper-15-rational). The firewall certifies that the substrate-IS invariants — the FI ratio R₁=a₀a₄/a₂² (D_K eigenvalues → a₀/a₂/a₄ spectral moments → dimensionless ratio) and the W τ=0 sixth-order zero (the genesis-only spectral-moment degeneracy where the layers are algebraically dependent) — are unchanged under any of them, so no downstream observable inherits a convention artifact. The substrate IS the curvature; the normalization is a laboratory bookkeeping choice. Direction of explanation preserved: D_K eigenvalues → R_K (fiber curvature) → spectral moments → R₁ + W algebraic-independence Wronskian.

---
"""  # (local)


def main() -> int:
    text = WP.read_text(encoding="utf-8")  # (local)
    n_before = len(text.encode("utf-8"))   # (local)

    if SECTION_HEADER not in text:
        print("ERROR: §W7-4 header not found; refusing to splice.", file=sys.stderr)
        return 2
    if NEXT_HEADER not in text:
        print("ERROR: §W7-5 header not found; refusing to splice.", file=sys.stderr)
        return 2

    start = text.index(SECTION_HEADER)                     # (local)
    next_start = text.index(NEXT_HEADER, start)            # (local)

    # Idempotency: if the EXISTING §W7-4 block already says COMPLETED, no-op.
    existing_block = text[start:next_start]  # (local)
    if IDEMPOTENT_MARKER in existing_block and "convention-invariance-PASS" in existing_block:
        print(f"IDEMPOTENT: §W7-4 already COMPLETED; no-op. (bytes={n_before})")
        return 0

    head = text[:start]        # (local)  everything before the §W7-4 header
    tail = text[next_start:]   # (local)  starts at "### §W7-5 …"
    # COMPLETED_SECTION ends with "---\n"; preserve the blank line before §W7-5
    # exactly as the stub had it ("---\n\n### §W7-5").
    new_text = head + COMPLETED_SECTION + "\n" + tail  # (local)

    fd, tmp_path = tempfile.mkstemp(dir=str(WP.parent),
                                    prefix=".s96_w7_4_", suffix=".tmp")  # (local)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fp:
            fp.write(new_text)
            fp.flush()
            os.fsync(fp.fileno())
        os.replace(tmp_path, WP)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    verify = WP.read_text(encoding="utf-8")  # (local)
    # must_contain checks (plan output_artifacts):
    blk_start = verify.index(SECTION_HEADER)  # (local)
    blk_end = verify.index(NEXT_HEADER, blk_start)  # (local)
    blk = verify[blk_start:blk_end]  # (local)
    checks = {
        "Status COMPLETED": "**Status**: COMPLETED" in blk,
        "Verdict PASS": ("**Verdict**:" in blk and "PASS" in blk),
        "Output Artifacts": "**Output Artifacts**" in blk,
        "MCP Pre-Compute Audit": "**MCP Pre-Compute Audit**" in blk,
        "3-form table": ("internal E3" in blk and "12D-reduction" in blk
                         and "Paper-15 eq 3.70" in blk),
        "invariance cert": ("convention-invariant" in blk
                            and "1.128655" in blk and "sixth-order" in blk),
        "full audit_sha": "df4a223aa380dbfc07507be8a8cb2bb899b4e87f617d6ed3631baf4c1178820b" in blk,
    }  # (local)
    # neighboring sections preserved:
    sibling_ok = all(h in verify for h in (
        "### §W7-3. S96-HYG-MELLIN-POLESET (lizzi-spectral-functional-theorist)",
        "### §W7-5. S96-HYG-SELF-INVENTORY (gen-physicist)",
    ))  # (local)
    print(f"WP SPLICE OK: sibling_sections_preserved={sibling_ok}")
    for k, v in checks.items():
        print(f"  must_contain[{k}] = {v}")
    print(f"  bytes_before={n_before} bytes_after={len(verify.encode('utf-8'))}")
    if not (all(checks.values()) and sibling_ok):
        print("ERROR: post-splice must_contain verification FAILED.", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
