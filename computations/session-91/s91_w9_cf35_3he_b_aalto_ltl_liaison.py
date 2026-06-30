#!/usr/bin/env python3
"""
S91 W9-2 (CF-35) — 3He-B Aalto LTL First-Contact Liaison Verifier
==================================================================

Gate ID: S91-CF-35-3HE-B-AALTO-LTL-FIRST-CONTACT-LIAISON
Alias:   S91-W9-2; CF-35
Plan:    sessions/session-plan/session-91-plan-w9.md §W9-2 (lines 232-402)
Author:  mack-cosmic-bridge (SOLE-WRITER per feedback_mack-bridge-role.md)
Trigger: [VERIFY] — schema-v2 3-tuple companion row REQUIRED
Class:   PHONONIC × META (observational liaison; Pillar V 3He-B laboratory anchor)

Purpose
-------
Verifies that the CF-35 5-element first-contact liaison block has been
authored in `sessions/framework/registry/mack-observational-constraints.md`
with substrate prediction matching the Sage-QQ exact form
`Rational(114453, 15625) = 7.324992` to canonical_constants pin tolerance
1e-12.

PASS/FAIL/INFO thresholds (ABSOLUTE on artifact existence)
----------------------------------------------------------
- PASS iff (i) liaison block on disk with all 5 CF-35 pre-registered
  elements AND (ii) substrate prediction matches `114453/15625 = 7.324992`
  Sage-QQ exact.
- FAIL iff liaison block absent OR any required element missing OR
  substrate prediction does not match Sage-QQ.
- INFO iff liaison block present with 3-4 of 5 elements (partial).

Substrate framing
-----------------
The substrate IS the inheritance morphism `ι: A_K → A_BdG = M_2(C)`.
The cocycle-ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 114453/15625` IS the substrate's
intrinsic cohomology-asymmetry ratio at the (chiral-pair, Cartan-hypercharge)
generator pair in `ker(ι_*)`. The Aalto LTL Lancaster MCT-3 measurement
of `lab(F_1) / lab(F_2)` IS the laboratory image of this substrate-IS
ratio under the inheritance morphism's image-on-spectrum. By the
(Δ_B/Δ_A)^p Cancellation Theorem (W-5 DONE-5; 0.0e+00 residual), this
ratio is preserved INTACT in the lab measurement.

Canonical-pin discipline
------------------------
- `substrate_cocycle_ratio_67_88` is imported from canonical_constants.py
  (S86 W-5 R2-B Convergence #3 + R2-A EMERGENCE #2; W-5 CANONICAL-5).
- Sage-QQ Rational(114453, 15625) is the substrate-IS published canonical
  form (gcd=1, lowest terms; float-exact 7.324992).
- Per S91 W8-3 / W8-5 / W8-6 Element-3 fiducial-anchor binding workshop,
  the published-Sage-QQ canonical form (this file's `114453/15625`) is
  distinct from the empirical rank-2 anchor `Fraction(793346, 108307)
  = 7.3249744` (delta 1.76e-5 at 6th sig-fig; INFO-class arithmetic
  gloss surfaced as carry-forward S92 §VII.AY-OP-PROJ-E5 corrigendum).
  This CF-35 verifier audits the canonical `114453/15625` (registry-text
  published form), NOT the empirical anchor.
"""

import sys
import hashlib
import re
from pathlib import Path
from fractions import Fraction

# Project root resolution (script lives at computations/session-91/)
SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[2]

# Make computations/_shared importable
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))

from canonical_constants import substrate_cocycle_ratio_67_88


def sha256_of_file(path: Path) -> str:
    """SHA-256 hexdigest of file content."""
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def closure_hash(*items) -> str:
    """Order-sensitive closure hash over a sequence of input pins."""
    h = hashlib.sha256()
    for it in items:
        if isinstance(it, bytes):
            h.update(it)
        else:
            h.update(str(it).encode("utf-8"))
        h.update(b"\x00")  # separator
    return h.hexdigest()


def main() -> int:
    # ------------------------------------------------------------------
    # Step 1 — Sage-QQ exact cross-pin verification
    # ------------------------------------------------------------------
    # Sage-QQ Rational(114453, 15625) is realised here via Python's
    # exact rational arithmetic (Fraction). Sage's QQ field embeds
    # canonically into Python Fraction; for a 6-sig-fig substrate pin
    # both representations are float-equivalent at machine precision.
    qq_exact = Fraction(114453, 15625)  # (local) Sage-QQ canonical form
    qq_float = float(qq_exact)  # (local) 7.324992 exact at machine precision

    # Cross-pin against canonical_constants.py
    cross_pin_residual = abs(qq_float - substrate_cocycle_ratio_67_88)  # (local)
    cross_pin_pass = cross_pin_residual < 1e-12  # (local)

    print(f"[1] Sage-QQ exact form: Rational(114453, 15625) = {qq_exact}")
    print(f"    Float image:        {qq_float:.12f}")
    print(f"    canonical_constants.substrate_cocycle_ratio_67_88 = "
          f"{substrate_cocycle_ratio_67_88}")
    print(f"    Cross-pin residual: {cross_pin_residual:.2e}")
    print(f"    Cross-pin PASS (residual < 1e-12): {cross_pin_pass}")

    # Sanity: gcd should be 1 (lowest-terms canonical form)
    from math import gcd
    g = gcd(114453, 15625)
    print(f"    gcd(114453, 15625) = {g} (1 = lowest terms canonical)")

    # ------------------------------------------------------------------
    # Step 2 — Liaison block existence check
    # ------------------------------------------------------------------
    LIAISON_PATH = (
        PROJECT_ROOT / "sessions" / "framework" / "registry"
        / "mack-observational-constraints.md"
    )

    if not LIAISON_PATH.exists():
        print(f"[2] FAIL — liaison file missing: {LIAISON_PATH}")
        return 1

    liaison_text = LIAISON_PATH.read_text(encoding="utf-8")
    liaison_path_sha256 = sha256_of_file(LIAISON_PATH)  # (local)
    print(f"[2] Liaison file SHA-256: {liaison_path_sha256[:16]}...")
    print(f"    Liaison file size:    {len(liaison_text)} bytes")

    # ------------------------------------------------------------------
    # Step 3 — 5-element regex check against required content
    # ------------------------------------------------------------------
    # Element-keyed token set per plan §W9-2 Field 6 (5 CF-35 elements);
    # also the extra-strict tokens per the spawn prompt's Field 6 listing
    # (114453/15625, 7.324992, ±0.1% tolerance, Q4 2026, 2028-2029,
    # Aalto LTL, Lancaster MCT-3, Helsinki ROTA, Caroli-Matricon ladder
    # asymmetry).
    required_tokens = [
        "CF-35",                          # gate identifier in block heading
        "cocycle_ratio_67_88",            # Element 1 — substrate prediction symbol
        "114453/15625",                   # Element 1 — Sage-QQ exact form
        "Rational(114453, 15625)",        # Element 1 — Sage-QQ canonical literal
        "7.324992",                       # Element 1 — decimal 6-sig-fig
        "7.3250",                         # Element 1 — 4-sig-fig form
        "Aalto LTL",                      # Element 4 — primary contact partner
        "Lancaster MCT-3",                # Element 4 — secondary platform
        "Helsinki ROTA",                  # Element 4 — primary cell
        "Caroli-Matricon ladder asymmetry",  # Element 2 — measurement protocol F_1
        "±0.1%",                          # Element 3 — substrate tolerance band
        "±1%",                            # Element 3 — lab-systematic band
        "Q4 2026",                        # Element 5 — first-contact deadline
        "2028-2029",                      # Element 5 — feasibility window
        "(Δ_B/Δ_A)^p",                    # Element 2 — cancellation theorem cite
        "ker(ι_*)",                       # substrate framing — kernel symbol
        "Pillar V",                       # substrate framing — pillar partition
    ]

    element_results: dict[str, bool] = {}
    for tok in required_tokens:
        element_results[tok] = (tok in liaison_text)

    element_check_count = sum(1 for v in element_results.values() if v)
    total_required = len(required_tokens)
    element_check_all = (element_check_count == total_required)  # (local)

    print(f"[3] Required-token check ({element_check_count}/{total_required}):")
    for tok, present in element_results.items():
        flag = "PASS" if present else "MISSING"
        print(f"    [{flag}] {tok!r}")

    # ------------------------------------------------------------------
    # Step 4 — 5-element CF-35 structural check (grouped)
    # ------------------------------------------------------------------
    # Group tokens into the 5 CF-35 pre-registered elements per Field 6:
    element_groups = {
        "Element_1_substrate_prediction": [
            "cocycle_ratio_67_88", "114453/15625",
            "Rational(114453, 15625)", "7.324992",
        ],
        "Element_2_measurement_protocol": [
            "Caroli-Matricon ladder asymmetry", "(Δ_B/Δ_A)^p",
        ],
        "Element_3_tolerance_band": [
            "±0.1%", "±1%",
        ],
        "Element_4_contact_partners": [
            "Aalto LTL", "Lancaster MCT-3", "Helsinki ROTA",
        ],
        "Element_5_timeline": [
            "Q4 2026", "2028-2029",
        ],
    }
    element_group_pass: dict[str, bool] = {}
    for name, toks in element_groups.items():
        element_group_pass[name] = all(t in liaison_text for t in toks)

    elements_pass_count = sum(1 for v in element_group_pass.values() if v)
    elements_pass_all = (elements_pass_count == 5)  # (local)

    print(f"[4] 5-element CF-35 group check ({elements_pass_count}/5):")
    for name, ok in element_group_pass.items():
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")

    # ------------------------------------------------------------------
    # Step 5 — Verdict composition (PASS / FAIL / INFO)
    # ------------------------------------------------------------------
    if cross_pin_pass and elements_pass_all and element_check_all:
        verdict = "PASS"
        magnitude_verdict = "PASS"
        regime_verdict = "VALID"
    elif cross_pin_pass and elements_pass_count >= 3 and elements_pass_count < 5:
        verdict = "INFO"
        magnitude_verdict = "INFO"
        regime_verdict = "VALID"
    else:
        verdict = "FAIL"
        magnitude_verdict = "FAIL"
        regime_verdict = "VALID"

    # Sign-verdict: not applicable (artifact-existence gate; no signed delta)
    sign_verdict = "N/A"

    # ------------------------------------------------------------------
    # Step 6 — Audit + content SHAs
    # ------------------------------------------------------------------
    canonical_constants_path = (
        PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
    )
    canonical_constants_sha256 = sha256_of_file(canonical_constants_path)  # (local)
    inheritance_protocol_path = (
        PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"
    )
    inheritance_protocol_sha256 = (
        sha256_of_file(inheritance_protocol_path)
        if inheritance_protocol_path.exists()
        else "absent"
    )

    audit_sha256 = closure_hash(
        "S91-CF-35-3HE-B-AALTO-LTL-FIRST-CONTACT-LIAISON",
        liaison_path_sha256,
        canonical_constants_sha256,
        inheritance_protocol_sha256,
        f"substrate_cocycle_ratio_67_88={substrate_cocycle_ratio_67_88!r}",
        f"qq_exact_numerator=114453",
        f"qq_exact_denominator=15625",
        f"cross_pin_residual={cross_pin_residual:.2e}",
        f"element_check_count={element_check_count}",
        f"elements_pass_count={elements_pass_count}",
        f"verdict={verdict}",
    )
    content_sha256 = closure_hash(
        f"liaison_path_sha256={liaison_path_sha256}",
        f"canonical_constants_sha256={canonical_constants_sha256}",
        f"inheritance_protocol_sha256={inheritance_protocol_sha256}",
    )

    # ------------------------------------------------------------------
    # Step 7 — Verdict-line emission (canonical + dual-SHA + 3-tuple)
    # ------------------------------------------------------------------
    value_str = (
        f"element_check_count={element_check_count}_of_{total_required};"
        f"five_element_groups={elements_pass_count}_of_5;"
        f"sage_qq_exact_form=Rational(114453,15625)=7.324992;"
        f"cross_pin_residual={cross_pin_residual:.2e};"
        f"substrate_cocycle_ratio_67_88={substrate_cocycle_ratio_67_88};"
        f"liaison_path={LIAISON_PATH.as_posix()};"
        f"first_contact_deadline=Q4_2026;"
        f"feasibility_window=2028-2029;"
        f"contact_partners=Aalto_LTL_Helsinki_ROTA+Lancaster_MCT-3+Volovik_substrate_adjudicator;"
        f"falsifier_class=Class_B_cohomology_asymmetry_ratio_W-5_DONE-5_zero_residual_cancellation_theorem;"
        f"substrate_framing=substrate_IS_inheritance_morphism_iota_A_K_to_A_BdG_M_2_C_kernel_ker_iota_star_carries_cocycle_ratio_67_88_preserved_INTACT_in_lab_under_Delta_B_Delta_A_p_common_exponent_cancellation"
    )

    gate_id = "S91-CF-35-3HE-B-AALTO-LTL-FIRST-CONTACT-LIAISON"
    scheme = "substrate-cocycle-norm-inheritance-morphism-Pillar-V-3HeB"
    convention = (
        "Aalto-LTL-Lancaster-MCT3-Helsinki-ROTA-cell-Caroli-Matricon-"
        "ladder-asymmetry-F1-F2-decisive-triplet"
    )
    L_max = "N/A_observational_liaison"

    canonical_line = (
        f"{gate_id}: {verdict} -- value='{value_str}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version=S87+"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)"
    )
    three_tuple_companion = (
        f"# sign_verdict={sign_verdict} "
        f"magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)"
    )

    verdicts_file = (
        PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
    )
    # Atomic append (POSIX O_APPEND) per registry-write-hygiene rule
    with open(verdicts_file, "a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(dual_sha_companion + "\n")
        f.write(three_tuple_companion + "\n")

    print(f"[7] Verdict appended to {verdicts_file}:")
    print(f"    {canonical_line}")
    print(f"    {dual_sha_companion}")
    print(f"    {three_tuple_companion}")

    print(f"\nFINAL VERDICT: {verdict}")
    print(f"  audit_sha256:   {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")
    print(f"  3-tuple:        sign={sign_verdict} magnitude={magnitude_verdict} "
          f"regime={regime_verdict}")

    # Exit 0 regardless of verdict (per math-scripts.md §"Exit Codes and
    # Verdict Semantics" — verdict is data, not exit code)
    return 0


if __name__ == "__main__":
    sys.exit(main())
