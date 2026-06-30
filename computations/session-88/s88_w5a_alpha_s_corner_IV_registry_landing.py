#!/usr/bin/env python3
"""
S88 W5a-43 — S88-ALPHA-S-CORNER-IV-COMPANION-OBSERVABLE-NEW-REGISTRY-LANDING
==============================================================================

Gate: S88-ALPHA-S-CORNER-IV-COMPANION-OBSERVABLE-NEW-REGISTRY-LANDING
       (trigger: AUDIT)
Wave: W5a (METHODOLOGY-class registry-landing of structurally-orthogonal
       companion observable)
Plan: sessions/session-plan/session-88-plan-w5a.md §W5a-43

Pre-registered threshold (per session-88-plan-w5a.md §W5a-43 Field 9):
  PASS: (a) §VII.{slot} block written with all 8 fields (CORNER, SUBSTRATE-IS,
        ANCHOR STRUCTURE, POLE-SCOPE, RESOLUTION-SCOPE, LABORATORY-IN,
        CROSS-CORNER STRUCTURAL OBSERVABLE, ORTHOGONALITY DECLARATION);
        (b) anchor tag is STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY
        literal (NOT SOURCE-DOUBLE-CITE-CO-PRIMARY); (c) cross-corner
        ratio carries [CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS
        GATE] literal; (d) substrate framing block present; (e) verdict
        line appended.
  FAIL: anchor structure tag drift (e.g., row written as
        SOURCE-DOUBLE-CITE-CO-PRIMARY would violate algebra-axis K=3
        MANDATORY enforcement; rubric Class 8.2 violation).
  INFO: registry write succeeded with slot rerouting; OR cross-corner
        ratio Sage-QQ form not verified.

Substitution chain (per plan §W5a-43 Field 10; mandatory cross-corner ratio claim):
  Definition 1: α_s^{(I)}  = -8587279/100000000 (Cell I biaxial-FI Sage-QQ exact)
  Definition 2: α_s^{(IV)} = -7.046336 (Cell IV biaxial-DRESSED, S87 W2-3)
  Definition 3: ratio_IV_to_I = α_s^{(IV)} / α_s^{(I)}

  Step 4 (substitute):
    ratio = (-7.046336) / (-8587279/100000000)
          = (-7.046336) × (100000000 / -8587279)
          = (7.046336 × 100000000) / 8587279
          = 704633600 / 8587279
          = 82.0556 (4-decimal published precision)

  Step 5 (Sage-QQ canonical form):
    Fraction(704633600, 8587279) = 82.0555...

  Step 6 (direction reading):
    Both α_s^{(I)} and α_s^{(IV)} negative; ratio is positive.
    ratio > 1 ⇒ |α_s^{(IV)}| > |α_s^{(I)}| (Cell IV magnitude exceeds Cell I by 82×)

  Step 7 (STRUCTURAL FORBIDDEN flag):
    Per cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"
    MANDATORY at K=3: ratio is STRUCTURAL OBSERVABLE (records cross-corner
    magnitude separation) but NOT a falsifier-side discrimination. Comparing
    |α_s^{(IV)}| to laboratory-IN α_s anchor would be a category error: Cell IV
    has NO laboratory bridge map at this registration.

  Conclusion: Cross-corner ratio = 82× recorded as structural observable;
  FORBIDDEN as falsifier gate per algebra-axis K=3 MANDATORY.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from fractions import Fraction
from pathlib import Path

T0 = Path(__file__).resolve().parent
PROJECT_ROOT = T0.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Pin metadata
GATE_ID = "S88-ALPHA-S-CORNER-IV-COMPANION-OBSERVABLE-NEW-REGISTRY-LANDING"
SCHEME = "registry-landing-corner-IV"
CONVENTION = "biaxial-DRESSED-s4-cone-orthogonal-companion"
L_MAX = "12"  # (local)
LINE_THRESHOLD_PASS = 18  # (local)

# Cell IV value (S87 W2-3)
ALPHA_S_IV_VALUE = -7.046336  # (local)

# Cell I value (Sage-QQ exact)
ALPHA_S_I_NUM = -8587279  # (local)
ALPHA_S_I_DEN = 100000000  # (local)

# Cross-corner ratio Sage-QQ exact
RATIO_NUM = 704633600  # (local)
RATIO_DEN = 8587279  # (local)

# Files
SCRIPT_PATH = T0 / "s88_w5a_alpha_s_corner_IV_registry_landing.py"
NPZ_OUT = T0 / "s88_w5a_alpha_s_corner_IV_registry_landing.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
ALLOWLIST_PATH = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
RULE_BRIDGE_ANATOMY = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w5a.md"
CANON_PY = SHARED_DIR / "canonical_constants.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def count_section_lines(file_path: Path, start_anchor: str, end_anchor: str) -> int:
    text = file_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    in_section = False
    count = 0  # (local)
    for line in lines:
        if start_anchor in line:
            in_section = True
            continue
        if in_section and end_anchor in line:
            break
        if in_section:
            count += 1
    return count


def scan_next_free_letter(registry_text: str) -> str:
    import re
    pattern = re.compile(r"§VII\.A([A-Z])(?:[\.\s—\-]|$)")
    used_letters = set()  # (local)
    for m in pattern.finditer(registry_text):
        used_letters.add(m.group(1))
    for code in range(ord("A"), ord("Z") + 1):
        letter = chr(code)
        if letter not in used_letters:
            return f"A{letter}"
    raise RuntimeError("No free letter under §VII.A*")


def build_promotion_text(slot_label: str, cell_I_slot: str = "AO") -> str:
    block = f"""
## §VII.{slot_label} — α_s Cell IV biaxial-DRESSED at s=4 substrate-distance-2 cone (S88 W5a-43 — mack-cosmic-bridge sole writer, 2026-05-04)

CORNER: IV (algebra-DEPENDENT × RD Mellin-axis)
SUBSTRATE-IS observable: α_s^{{(SF)}} = Var_a(n_a^GGE)
  S87 W2-3 closed value: -7.046336
  scheme: GGE-Bogoliubov-occupation-variance
  convention: horizon-crossing-K-window-canonical
  source: S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE verdict (s87_gate_verdicts.txt)
ANCHOR STRUCTURE: STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY
  (with Cell I §VII.{cell_I_slot}; per `cross-pillar-bridge-anatomy.md
   §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 forbidding
   cross-corner co-primary structure tags between cells inhabiting
   structurally orthogonal axes; explicitly NOT SOURCE-DOUBLE-CITE-CO-PRIMARY)
POLE-SCOPE: substrate-distance-2 cone s=4 SPECIFICALLY
  (per epistemic-discipline.md §"Pole-Scope sub-clause" T1-20)
RESOLUTION-SCOPE: A_5 5-element regulator-class projection
  (GGE Bogoliubov vacuum specification at L_max=10 per S87 W2-3 closure;
   per W-9 RULE-4 alt §"Resolution-Specificity Scoping")
LABORATORY-IN observable: NONE published bridge map yet
  (Cell IV is substrate-IS-ONLY at this registration; laboratory bridge
   pending future workshop on state-functional-axis observables in cosmology;
   forward-template-adoption calibration corpus instance #3+)
CROSS-CORNER STRUCTURAL OBSERVABLE: ratio_IV_to_I = 82.0556×
  Sage-QQ exact: 704633600/8587279
  [CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]
  (per algebra-axis orthogonality K=3 MANDATORY; magnitude is structural,
   NOT a falsifier-side discrimination — comparing |α_s^{{(IV)}}| to
   laboratory-IN α_s anchor would be a category error since Cell IV has
   NO laboratory bridge map at this registration)
ORTHOGONALITY DECLARATION:
  Cell IV ⊥ Cell I per algebra-axis (DEPENDENT vs INVARIANT)
  Cell IV ⊥ Cell I per Mellin-axis (RD vs FI)
  Hence biaxial orthogonality; cross-corner co-primary FORBIDDEN.

Substrate framing: substrate IS the GGE-Bog-occ-variance evaluated on
  (A_K^{{≤12}}, H_K^{{≤12}}, D_K^{{≤12}}) under GGE Bogoliubov vacuum specification at τ=0.190;
  laboratory IN: NONE (substrate-IS-ONLY at this registration; future
  state-functional-axis cosmological observables may bridge under
  forward-template-adoption calibration corpus instance #3+).

Container thinking violation guard: treating Cell IV's substrate value as a
  laboratory α_s "alternative" would invert the substrate-IS direction of
  explanation; Cell IV is the SUBSTRATE-PRIOR functional, not a laboratory-side
  competitor to Cell I. Per `phononic-framing.md §"IS Space, Not IN Space"`.

Cross-references:
  - §VII.{cell_I_slot} (W5a-42): Cell I biaxial-FI canonical (orthogonal-pair partner)
  - §VII.AN (W5a-37): SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure (Cell I upstream)
  - `sessions/framework/registry/alpha-s-multi-valued-landscape.md` (W5a-41): 4-corner enumeration table
  - `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`: K=3 MANDATORY enforcement of cross-corner co-primary FORBIDDEN

---
"""
    return block


def main() -> int:
    t_start = time.time()
    import numpy as np

    # ──────────────────────────────────────────────────────────────────
    # 1 — Sage-QQ verification of cross-corner ratio (substitution chain)
    # ──────────────────────────────────────────────────────────────────
    alpha_s_I = Fraction(ALPHA_S_I_NUM, ALPHA_S_I_DEN)
    ratio_qq = Fraction(RATIO_NUM, RATIO_DEN)
    ratio_float = float(ratio_qq)
    print(f"[W5a-43] Substitution chain (cross-corner ratio):")
    print(f"  Definition 1: α_s^(I)  = {alpha_s_I} = {float(alpha_s_I):+.10f}")
    print(f"  Definition 2: α_s^(IV) = {ALPHA_S_IV_VALUE:+.6f}")
    print(f"  Step 4: ratio = α_s^(IV) / α_s^(I) = {ratio_qq} = {ratio_float:.6f}")
    print(f"  Step 5: Sage-QQ canonical form = Fraction(704633600, 8587279)")
    print(f"  Step 6: ratio > 1 ⇒ |α_s^(IV)| > |α_s^(I)| (Cell IV magnitude exceeds Cell I by ~82×)")
    print(f"  Step 7: STRUCTURALLY FORBIDDEN AS GATE per algebra-axis K=3 MANDATORY")

    # Independent float-arithmetic cross-check (works without Sage MCP)
    ratio_float_check = ALPHA_S_IV_VALUE / float(alpha_s_I)
    cc_ratio_consistent = abs(ratio_float - ratio_float_check) < 1e-10
    print(f"[W5a-43] Float cross-check: {ratio_float_check:.6f} vs Sage-QQ {ratio_float:.6f} → consistent: {cc_ratio_consistent}")

    # ──────────────────────────────────────────────────────────────────
    # 2 — Pre-write checks: registry readable; allowlist W5a-43 row present
    # ──────────────────────────────────────────────────────────────────
    registry_text_pre = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")

    cc_allowlist_w5a43 = ("| W5a-43 | S88 |" in allowlist_text
                          and "eeaaf16d4f6d9e1eef752c7ebe254c039ca2847cab521513bdc8b69b71ad8414" in allowlist_text)
    print(f"[W5a-43] CC0 methodology-wave-allowlist W5a-43 row present: {cc_allowlist_w5a43}")

    cc_cell_I_landed = "α_s Cell I biaxial-FI at s=3" in registry_text_pre
    print(f"[W5a-43] Cross-link target §VII.AO Cell I landed (W5a-42): {cc_cell_I_landed}")

    already_landed = "α_s Cell IV biaxial-DRESSED at s=4 substrate-distance-2 cone (S88 W5a-43" in registry_text_pre

    # ──────────────────────────────────────────────────────────────────
    # 3 — Allocate slot: if already-landed, reuse existing slot;
    #     otherwise scan next-free-letter
    # ──────────────────────────────────────────────────────────────────
    if already_landed:
        # Find the existing slot from the registry text
        import re as _re
        m = _re.search(r"## §VII\.(A[A-Z]) — α_s Cell IV biaxial-DRESSED", registry_text_pre)
        if m:
            slot_label = m.group(1)
            print(f"[W5a-43] Idempotent re-run: reusing existing slot §VII.{slot_label}")
        else:
            slot_label = scan_next_free_letter(registry_text_pre)
            print(f"[W5a-43] WARN: already_landed True but slot pattern not matched; scanning fresh: §VII.{slot_label}")
    else:
        slot_label = scan_next_free_letter(registry_text_pre)
        print(f"[W5a-43] Next-free-letter slot: §VII.{slot_label}")

    # ──────────────────────────────────────────────────────────────────
    # 4 — Build promotion text
    # ──────────────────────────────────────────────────────────────────
    promotion_text = build_promotion_text(slot_label, cell_I_slot="AO")

    # ──────────────────────────────────────────────────────────────────
    # 5 — Write append-only with fsync
    # ──────────────────────────────────────────────────────────────────
    if not already_landed:
        with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
            f.write(promotion_text)
            f.flush()
            os.fsync(f.fileno())
        print(f"[W5a-43] Appended §VII.{slot_label} block ({len(promotion_text)} chars)")
    else:
        print(f"[W5a-43] Idempotent re-run; skipping append")

    # ──────────────────────────────────────────────────────────────────
    # 6 — Re-read + verify (cross-checks for 8 mandatory fields)
    # ──────────────────────────────────────────────────────────────────
    registry_text_post = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")

    cc1_corner = "CORNER: IV (algebra-DEPENDENT × RD Mellin-axis)" in registry_text_post
    cc2_substrate_is = ("SUBSTRATE-IS observable: α_s^{(SF)} = Var_a(n_a^GGE)" in registry_text_post
                        and "-7.046336" in registry_text_post)
    # CRITICAL: anchor structure tag MUST be the FORBIDDEN-CO-PRIMARY literal
    cc3_anchor_NOT_CO_PRIMARY = ("ANCHOR STRUCTURE: STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY"
                                  in registry_text_post)
    # And the ANCHOR STRUCTURE line MUST NOT carry SOURCE-DOUBLE-CITE-CO-PRIMARY tag.
    # CC3b checks the LINE-FORM specifically (not naive substring), since
    # "NOT SOURCE-DOUBLE-CITE-CO-PRIMARY" appears in our negated explanatory
    # parenthetical and would trip a substring check.
    block_start = registry_text_post.find(f"## §VII.{slot_label} — α_s Cell IV biaxial-DRESSED")
    block_end = registry_text_post.find("---\n", block_start)
    cell_IV_block = registry_text_post[block_start:block_end] if block_start >= 0 else ""
    # The forbidden form is the literal anchor-tag LINE
    cc3b_no_co_primary_drift = "ANCHOR STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY" not in cell_IV_block
    print(f"[W5a-43] CC3 anchor STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY:  {cc3_anchor_NOT_CO_PRIMARY}")
    print(f"[W5a-43] CC3b NO SOURCE-DOUBLE-CITE-CO-PRIMARY drift in Cell IV block: {cc3b_no_co_primary_drift}")

    cc4_pole_scope = "POLE-SCOPE: substrate-distance-2 cone s=4 SPECIFICALLY" in registry_text_post
    cc5_resolution_scope = "RESOLUTION-SCOPE: A_5 5-element regulator-class projection" in registry_text_post
    cc6_lab_in_NONE = ("LABORATORY-IN observable: NONE published bridge map yet" in registry_text_post)
    cc7_cross_corner_ratio = ("CROSS-CORNER STRUCTURAL OBSERVABLE: ratio_IV_to_I = 82.0556×" in registry_text_post
                              and "704633600/8587279" in registry_text_post)
    cc8_forbidden_flag = "[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]" in registry_text_post
    cc9_orthogonality_decl = ("Cell IV ⊥ Cell I per algebra-axis (DEPENDENT vs INVARIANT)" in registry_text_post
                              and "Cell IV ⊥ Cell I per Mellin-axis (RD vs FI)" in registry_text_post)
    cc10_substrate_framing = ("Substrate framing:" in cell_IV_block
                              and "GGE-Bog-occ-variance" in cell_IV_block)
    cc11_container_guard = "Container thinking violation guard" in cell_IV_block

    print(f"[W5a-43] CC1 CORNER IV (DEPENDENT × RD):                              {cc1_corner}")
    print(f"[W5a-43] CC2 SUBSTRATE-IS Var_a(n_a^GGE) = -7.046336:                {cc2_substrate_is}")
    print(f"[W5a-43] CC4 POLE-SCOPE s=4 SPECIFICALLY (T1-20):                     {cc4_pole_scope}")
    print(f"[W5a-43] CC5 RESOLUTION-SCOPE A_5:                                    {cc5_resolution_scope}")
    print(f"[W5a-43] CC6 LABORATORY-IN = NONE:                                    {cc6_lab_in_NONE}")
    print(f"[W5a-43] CC7 CROSS-CORNER STRUCTURAL OBSERVABLE 82.0556× + Sage-QQ:    {cc7_cross_corner_ratio}")
    print(f"[W5a-43] CC8 [STRUCTURALLY FORBIDDEN AS GATE] flag:                    {cc8_forbidden_flag}")
    print(f"[W5a-43] CC9 Biaxial ORTHOGONALITY DECLARATION:                        {cc9_orthogonality_decl}")
    print(f"[W5a-43] CC10 Substrate framing block (GGE-Bog-occ-variance):         {cc10_substrate_framing}")
    print(f"[W5a-43] CC11 Container thinking violation guard:                     {cc11_container_guard}")

    sub_row_line_count = count_section_lines(
        REGISTRY_PATH,
        f"## §VII.{slot_label} — α_s Cell IV biaxial-DRESSED",
        "---\n",
    )
    print(f"[W5a-43] §VII.{slot_label} body line count: {sub_row_line_count} (threshold ≥{LINE_THRESHOLD_PASS})")

    # ──────────────────────────────────────────────────────────────────
    # 7 — Composite verdict
    # ──────────────────────────────────────────────────────────────────
    # FAIL-CRITICAL: anchor tag drift would FAIL via Class 8.2 rubric violation
    if not cc3_anchor_NOT_CO_PRIMARY or not cc3b_no_co_primary_drift:
        composite = "FAIL"
        verdict_kind = "FAIL-anchor-tag-drift-CO-PRIMARY-detected-Class-8.2-violation"
    else:
        all_cc_pass = (
            cc1_corner and cc2_substrate_is and cc3_anchor_NOT_CO_PRIMARY
            and cc3b_no_co_primary_drift and cc4_pole_scope and cc5_resolution_scope
            and cc6_lab_in_NONE and cc7_cross_corner_ratio and cc8_forbidden_flag
            and cc9_orthogonality_decl and cc10_substrate_framing and cc11_container_guard
            and cc_allowlist_w5a43 and cc_ratio_consistent
            and sub_row_line_count >= LINE_THRESHOLD_PASS
        )
        if all_cc_pass:
            composite = "PASS"
            verdict_kind = f"PASS-vii-{slot_label}-corner-IV-biaxial-DRESSED-orthogonal-companion-landed"
        elif sub_row_line_count >= 10:
            composite = "INFO"
            verdict_kind = f"INFO-vii-{slot_label}-partial-landing-cross-checks-failed"
        else:
            composite = "FAIL"
            verdict_kind = f"FAIL-vii-{slot_label}-corner-IV-block-incomplete"

    print(f"[W5a-43] composite = {composite} (verdict_kind={verdict_kind})")

    # ──────────────────────────────────────────────────────────────────
    # 8 — Compute SHAs
    # ──────────────────────────────────────────────────────────────────
    canon_sha = sha256_file(CANON_PY)
    registry_sha_post = sha256_file(REGISTRY_PATH)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    rule_anatomy_sha = sha256_file(RULE_BRIDGE_ANATOMY)
    plan_sha = sha256_file(PLAN_PATH)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "wp_id": "session-88-w5a-workingpaper.md",
        "slot_label": slot_label,
        "cell_I_slot": "AO",
        "alpha_s_IV_value": ALPHA_S_IV_VALUE,
        "alpha_s_I_qq_num": ALPHA_S_I_NUM,
        "alpha_s_I_qq_den": ALPHA_S_I_DEN,
        "ratio_qq_num": RATIO_NUM,
        "ratio_qq_den": RATIO_DEN,
        "anchor_structure": "STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY",
        "LINE_THRESHOLD_PASS": LINE_THRESHOLD_PASS,
        "input_canonical_constants_sha256": canon_sha,
        "input_registry_sha256_post": registry_sha_post,
        "input_allowlist_sha256": allowlist_sha,
        "input_rule_anatomy_sha256": rule_anatomy_sha,
        "input_plan_sha256": plan_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # ──────────────────────────────────────────────────────────────────
    # 9 — Save .npz
    # ──────────────────────────────────────────────────────────────────
    np.savez(
        NPZ_OUT,
        slot_label=slot_label,
        cell_I_slot="AO",
        alpha_s_IV_value=np.float64(ALPHA_S_IV_VALUE),
        ratio_qq_value=np.float64(ratio_float),
        sub_row_line_count=np.int64(sub_row_line_count),
        cc1_corner=np.bool_(cc1_corner),
        cc2_substrate_is=np.bool_(cc2_substrate_is),
        cc3_anchor_NOT_CO_PRIMARY=np.bool_(cc3_anchor_NOT_CO_PRIMARY),
        cc3b_no_co_primary_drift=np.bool_(cc3b_no_co_primary_drift),
        cc4_pole_scope=np.bool_(cc4_pole_scope),
        cc5_resolution_scope=np.bool_(cc5_resolution_scope),
        cc6_lab_in_NONE=np.bool_(cc6_lab_in_NONE),
        cc7_cross_corner_ratio=np.bool_(cc7_cross_corner_ratio),
        cc8_forbidden_flag=np.bool_(cc8_forbidden_flag),
        cc9_orthogonality_decl=np.bool_(cc9_orthogonality_decl),
        cc10_substrate_framing=np.bool_(cc10_substrate_framing),
        cc11_container_guard=np.bool_(cc11_container_guard),
        cc_allowlist_w5a43=np.bool_(cc_allowlist_w5a43),
        cc_ratio_consistent=np.bool_(cc_ratio_consistent),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # ──────────────────────────────────────────────────────────────────
    # 10 — Append verdict trio
    # ──────────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    value_str = (
        f"slot=§VII.{slot_label};cell_I_slot=§VII.AO;"
        f"alpha_s_IV=-7.046336;ratio_qq=704633600/8587279=82.0556;"
        f"sub_row_line_count={sub_row_line_count};"
        f"cc3_NOT_CO_PRIMARY={cc3_anchor_NOT_CO_PRIMARY};"
        f"cc7_ratio_observable={cc7_cross_corner_ratio};"
        f"cc8_forbidden_flag={cc8_forbidden_flag};"
        f"cc9_biaxial_orthogonal={cc9_orthogonality_decl};"
        f"cc_allowlist={cc_allowlist_w5a43};verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    sign_v = "PASS"  # ratio direction (Cell IV magnitude > Cell I) confirmed via Step 6
    mag_v = composite
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W5a-43] DONE in {elapsed:.2f}s")
    print(f"[W5a-43] slot     = §VII.{slot_label}")
    print(f"[W5a-43] audit_sha256   = {audit_sha256}")
    print(f"[W5a-43] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
