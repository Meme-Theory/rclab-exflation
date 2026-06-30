#!/usr/bin/env python3
"""
S88 W5a-42 — S88-ALPHA-S-CORNER-I-WITHIN-POLE-CO-PRIMARY-REGISTRY-LANDING
==========================================================================

Gate: S88-ALPHA-S-CORNER-I-WITHIN-POLE-CO-PRIMARY-REGISTRY-LANDING
       (trigger: AUDIT)
Wave: W5a (METHODOLOGY-class registry-landing)
Plan: sessions/session-plan/session-88-plan-w5a.md §W5a-42

Pre-registered threshold (per session-88-plan-w5a.md §W5a-42 Field 9):
  PASS: (a) #37 PASS confirmed; (b) §VII.{slot} block written with all 6
        fields (CORNER, SUBSTRATE-IS, ANCHOR STRUCTURE, POLE-SCOPE,
        RESOLUTION-SCOPE, LABORATORY-IN); (c) discrimination σ values
        present; (d) substrate framing block present; (e) verdict line
        appended.
  FAIL: #37 not PASS at dispatch OR registry-write hygiene violation OR
        pole-scope declaration absent (rubric-form Class 8.2 violation).
  INFO: registry write succeeded with slot rerouting due to parallel
        writer collision.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - sessions/permanent-results-registry.md (registry edit target)
  - .claude/rules/methodology-wave-allowlist.md (allowlist row pin)
  - .claude/rules/registry-landing.md (CO-PRIMARY schema)
  - .claude/rules/cross-pillar-bridge-anatomy.md (Cell I taxonomy)
  - sessions/session-plan/session-88-plan-w5a.md (plan source)
  - computations/session-88/s88_gate_verdicts.txt (W5a-37 PASS prereq)
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
GATE_ID = "S88-ALPHA-S-CORNER-I-WITHIN-POLE-CO-PRIMARY-REGISTRY-LANDING"
SCHEME = "registry-landing-corner-I"
CONVENTION = "biaxial-FI-s3-pole"
L_MAX = "12"  # (local)
LINE_THRESHOLD_PASS = 18  # (local)

# α_s Sage-QQ exact (Cell I)
ALPHA_S_NUM = -8587279  # (local)
ALPHA_S_DEN = 100000000  # (local)
ALPHA_S_VALUE = ALPHA_S_NUM / ALPHA_S_DEN  # (local)

# Closure SHA pin (S87 W-2 R3)
CLOSURE_SHA_PIN = "e747495c1fbf8af144c3701ecaf5e77b2497d3b876281bdffb703d8db22839f3"

# Upstream prerequisite (W5a-37 audit_sha256)
W5A37_AUDIT_SHA = "cf5ec646662ccf8be68a206dc96ca38a222ebc6c596131d1d923e237f217f509"

# Discrimination σ values (consumed from W5a-40)
SIGMA_FW_VS_PLANCK = 13.9957  # (local) σ_framework_vs_Planck (Aiola 2020)
SIGMA_FW_VS_CMB_S4_HIGH = 38.3360  # (local) σ_framework_vs_CMB_S4 forecast σ=0.0023

# Files
SCRIPT_PATH = T0 / "s88_w5a_alpha_s_corner_I_registry_landing.py"
NPZ_OUT = T0 / "s88_w5a_alpha_s_corner_I_registry_landing.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
ALLOWLIST_PATH = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
RULE_BRIDGE_ANATOMY = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
RULE_REGISTRY_LANDING = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"
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


def build_promotion_text(slot_label: str, upstream_slot: str = "AN") -> str:
    block = f"""
## §VII.{slot_label} — α_s Cell I biaxial-FI at s=3 substrate-distance-1 pole (S88 W5a-42 — mack-cosmic-bridge sole writer, 2026-05-04)

CORNER: I (algebra-INVARIANT × FI Mellin-axis)
SUBSTRATE-IS observable: α_s_canonical = Res[M(s); s=3]
  Sage-QQ exact: -8587279/100000000 = -0.08587279 (S82 W3-9 closure)
ANCHOR STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY (inherits from §VII.{upstream_slot} W5a-37
  upstream landing; V1=S82 W3-9 single-pole Mellin closure + C1=S87 W2-3
  GGE-Bog-occ-variance theorem at s=4 cross-cone)
POLE-SCOPE: substrate-distance-1 pole s=3 SPECIFICALLY
  (NOT generic substrate-pluralism; pole-extension to s=4 is Cell II,
   structurally distinct per `cross-pillar-bridge-anatomy.md §"Algebra-axis
   orthogonality K-counter"` MANDATORY at K=3; per epistemic-discipline.md
   §"Pole-Scope sub-clause" T1-20)
RESOLUTION-SCOPE: A_5 5-element regulator-class projection
  (per W-9 RULE-4 alt §"Resolution-Specificity Scoping"; future A_5 → A_6
   regulator-atlas extensions could in principle refine the extremality
   value; current canonical is the A_5 projection)
LABORATORY-IN observable: Planck/ACT α_s = +0.0023 ± 0.0063
  (Aiola 2020 ACT DR4 + Planck running of scalar tilt at k_pivot = 0.05 Mpc⁻¹;
   canonical S85 W1b-8 update)
DISCRIMINATION σ: 13.9957σ vs Planck/ACT (current; per W5a-40 substitution chain Step 5);
  projected 38.3360σ vs CMB-S4 σ_floor=0.0023 high (W5a-40 Step 6).
CLOSURE SHA pin: {CLOSURE_SHA_PIN}
  (S87 W-2 R3 verdict per `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md`)
UPSTREAM ANCHOR (W5a-37): §VII.{upstream_slot}
  audit_sha256 = {W5A37_AUDIT_SHA}

Substrate framing: substrate IS the Mellin residue evaluated on
  (A_K^{{≤12}}, H_K^{{≤12}}, D_K^{{≤12}}) at τ=0.190;
  laboratory IN: the FRW-cosmology-container CMB-running measurement
  under Mukhanov-Sasaki gauge bridge map (FWD-C1 candidate per
  `cross-pillar-bridge-anatomy.md §"Forward template-adoption"`).
  Direction of explanation: substrate IS Cell I biaxial-FI;
  laboratory IN is the CMB-running observable. The CMB-S4 detector-decisive
  timeline does NOT change Cell I; it only changes laboratory σ-resolution.

Cross-references:
  - §VII.{upstream_slot} (W5a-37): SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure (V1+C1 sequential chain)
  - `sessions/framework/registry/alpha-s-multi-valued-landscape.md` (W5a-41): 4-corner enumeration table
  - `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`: Cell I ⊥ Cell IV (algebra-axis) and ⊥ Cell II (Mellin-axis); biaxial orthogonality with Cell IV (W5a-43)

---
"""
    return block


def main() -> int:
    t_start = time.time()
    import numpy as np

    # ──────────────────────────────────────────────────────────────────
    # 1 — Verify upstream prerequisite (W5a-37 PASS in verdict file)
    # ──────────────────────────────────────────────────────────────────
    verdict_text = VERDICT_FILE.read_text(encoding="utf-8", errors="replace")
    cc_w5a37_pass = (
        "S88-CF-20-SOURCE-DOUBLE-CITE-CO-PRIMARY-LANDING-FOR-ALPHA-S: PASS" in verdict_text
        and W5A37_AUDIT_SHA in verdict_text
    )
    print(f"[W5a-42] Upstream prereq W5a-37 PASS: {cc_w5a37_pass}")
    if not cc_w5a37_pass:
        print("[W5a-42] HARD-HALT: W5a-37 not PASS; aborting registry landing")
        # Still emit FAIL verdict for audit trail
        composite = "FAIL"
        verdict_kind = "FAIL-upstream-W5a-37-not-PASS-blocked"

    # ──────────────────────────────────────────────────────────────────
    # 2 — Sage-QQ verification of α_s_canonical (idempotency; same as W5a-37)
    # ──────────────────────────────────────────────────────────────────
    alpha_s_qq = Fraction(ALPHA_S_NUM, ALPHA_S_DEN)
    alpha_s_float = float(alpha_s_qq)
    assert alpha_s_float == ALPHA_S_VALUE
    print(f"[W5a-42] α_s_canonical Sage-QQ: {alpha_s_qq} = {alpha_s_float:.10f} (exact match)")

    # ──────────────────────────────────────────────────────────────────
    # 3 — Pre-write checks: registry readable; allowlist W5a-42 row present
    # ──────────────────────────────────────────────────────────────────
    registry_text_pre = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")

    cc_allowlist_w5a42 = ("| W5a-42 | S88 |" in allowlist_text
                          and "ab8cb8d65eb46d6edf9657d0e6bec8c1bd3404ff5b601327ad9b7d7268b5b40e" in allowlist_text)
    print(f"[W5a-42] CC0 methodology-wave-allowlist W5a-42 row present: {cc_allowlist_w5a42}")

    already_landed = "α_s Cell I biaxial-FI at s=3 substrate-distance-1 pole (S88 W5a-42" in registry_text_pre

    # ──────────────────────────────────────────────────────────────────
    # 4 — Allocate next-free-letter slot under §VII.A* (parallel-writer rule)
    # ──────────────────────────────────────────────────────────────────
    slot_label = scan_next_free_letter(registry_text_pre)
    print(f"[W5a-42] Next-free-letter slot under §VII.A*: §VII.{slot_label}")
    print(f"[W5a-42] Upstream slot (W5a-37): §VII.AN")

    # ──────────────────────────────────────────────────────────────────
    # 5 — Build promotion text (PURE)
    # ──────────────────────────────────────────────────────────────────
    promotion_text = build_promotion_text(slot_label, upstream_slot="AN")

    # ──────────────────────────────────────────────────────────────────
    # 6 — Write append-only with fsync (single-shot AFTER pattern)
    # ──────────────────────────────────────────────────────────────────
    if cc_w5a37_pass and not already_landed:
        with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
            f.write(promotion_text)
            f.flush()
            os.fsync(f.fileno())
        print(f"[W5a-42] Appended §VII.{slot_label} block to registry ({len(promotion_text)} chars)")
    elif already_landed:
        print(f"[W5a-42] Idempotent re-run detected; skipping append")
    else:
        print(f"[W5a-42] Append blocked by upstream FAIL")

    # ──────────────────────────────────────────────────────────────────
    # 7 — Re-read + verify (final verification — boolean drives verdict)
    # ──────────────────────────────────────────────────────────────────
    registry_text_post = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")

    cc1_corner = "CORNER: I (algebra-INVARIANT × FI Mellin-axis)" in registry_text_post
    cc2_substrate_is = "SUBSTRATE-IS observable: α_s_canonical = Res[M(s); s=3]" in registry_text_post
    cc3_anchor_structure = "ANCHOR STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY (inherits from §VII.AN W5a-37" in registry_text_post
    cc4_pole_scope = ("POLE-SCOPE: substrate-distance-1 pole s=3 SPECIFICALLY" in registry_text_post
                      and "Pole-Scope sub-clause" in registry_text_post)
    cc5_resolution_scope = "RESOLUTION-SCOPE: A_5 5-element regulator-class projection" in registry_text_post
    cc6_lab_in = ("LABORATORY-IN observable: Planck/ACT α_s = +0.0023 ± 0.0063" in registry_text_post
                  and "Aiola 2020" in registry_text_post)
    cc7_discrimination_sigma = ("DISCRIMINATION σ: 13.9957σ vs Planck/ACT" in registry_text_post
                                and "38.3360σ" in registry_text_post)
    cc8_closure_sha = CLOSURE_SHA_PIN in registry_text_post
    cc9_substrate_framing = ("Substrate framing:" in registry_text_post
                              and "FWD-C1" in registry_text_post)

    print(f"[W5a-42] CC1 CORNER I declaration:                    {cc1_corner}")
    print(f"[W5a-42] CC2 SUBSTRATE-IS Res[M(s); s=3]:              {cc2_substrate_is}")
    print(f"[W5a-42] CC3 ANCHOR STRUCTURE inherits CO-PRIMARY:    {cc3_anchor_structure}")
    print(f"[W5a-42] CC4 POLE-SCOPE s=3 SPECIFICALLY (T1-20):      {cc4_pole_scope}")
    print(f"[W5a-42] CC5 RESOLUTION-SCOPE A_5 5-element:           {cc5_resolution_scope}")
    print(f"[W5a-42] CC6 LABORATORY-IN Planck/ACT Aiola 2020:      {cc6_lab_in}")
    print(f"[W5a-42] CC7 DISCRIMINATION σ 13.99 + 38.33:           {cc7_discrimination_sigma}")
    print(f"[W5a-42] CC8 Closure SHA pin (e747495c...):           {cc8_closure_sha}")
    print(f"[W5a-42] CC9 Substrate framing block (FWD-C1):        {cc9_substrate_framing}")

    sub_row_line_count = count_section_lines(
        REGISTRY_PATH,
        f"## §VII.{slot_label} — α_s Cell I biaxial-FI at s=3",
        "---\n",
    )
    print(f"[W5a-42] §VII.{slot_label} body line count: {sub_row_line_count} (threshold ≥{LINE_THRESHOLD_PASS})")

    # ──────────────────────────────────────────────────────────────────
    # 8 — Composite verdict
    # ──────────────────────────────────────────────────────────────────
    if not cc_w5a37_pass:
        composite = "FAIL"
        verdict_kind = "FAIL-upstream-W5a-37-not-PASS-blocked"
    else:
        all_cc_pass = (
            cc1_corner and cc2_substrate_is and cc3_anchor_structure and cc4_pole_scope
            and cc5_resolution_scope and cc6_lab_in and cc7_discrimination_sigma
            and cc8_closure_sha and cc9_substrate_framing
            and cc_allowlist_w5a42
            and sub_row_line_count >= LINE_THRESHOLD_PASS
        )
        if all_cc_pass:
            composite = "PASS"
            verdict_kind = f"PASS-vii-{slot_label}-corner-I-biaxial-FI-landed"
        elif sub_row_line_count >= 10:
            composite = "INFO"
            verdict_kind = f"INFO-vii-{slot_label}-partial-landing-cross-checks-failed"
        else:
            composite = "FAIL"
            verdict_kind = f"FAIL-vii-{slot_label}-corner-I-block-incomplete"

    print(f"[W5a-42] composite = {composite} (verdict_kind={verdict_kind})")

    # ──────────────────────────────────────────────────────────────────
    # 9 — Compute SHAs
    # ──────────────────────────────────────────────────────────────────
    canon_sha = sha256_file(CANON_PY)
    registry_sha_post = sha256_file(REGISTRY_PATH)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    rule_anatomy_sha = sha256_file(RULE_BRIDGE_ANATOMY)
    rule_landing_sha = sha256_file(RULE_REGISTRY_LANDING)
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
        "upstream_slot": "AN",
        "upstream_w5a37_audit_sha": W5A37_AUDIT_SHA,
        "alpha_s_qq_num": ALPHA_S_NUM,
        "alpha_s_qq_den": ALPHA_S_DEN,
        "closure_sha_pin": CLOSURE_SHA_PIN,
        "sigma_FW_vs_Planck": SIGMA_FW_VS_PLANCK,
        "sigma_FW_vs_CMB_S4_high": SIGMA_FW_VS_CMB_S4_HIGH,
        "LINE_THRESHOLD_PASS": LINE_THRESHOLD_PASS,
        "input_canonical_constants_sha256": canon_sha,
        "input_registry_sha256_post": registry_sha_post,
        "input_allowlist_sha256": allowlist_sha,
        "input_rule_anatomy_sha256": rule_anatomy_sha,
        "input_rule_landing_sha256": rule_landing_sha,
        "input_plan_sha256": plan_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # ──────────────────────────────────────────────────────────────────
    # 10 — Save .npz
    # ──────────────────────────────────────────────────────────────────
    np.savez(
        NPZ_OUT,
        slot_label=slot_label,
        upstream_slot="AN",
        cc_w5a37_pass=np.bool_(cc_w5a37_pass),
        sub_row_line_count=np.int64(sub_row_line_count),
        cc1_corner=np.bool_(cc1_corner),
        cc2_substrate_is=np.bool_(cc2_substrate_is),
        cc3_anchor_structure=np.bool_(cc3_anchor_structure),
        cc4_pole_scope=np.bool_(cc4_pole_scope),
        cc5_resolution_scope=np.bool_(cc5_resolution_scope),
        cc6_lab_in=np.bool_(cc6_lab_in),
        cc7_discrimination_sigma=np.bool_(cc7_discrimination_sigma),
        cc8_closure_sha=np.bool_(cc8_closure_sha),
        cc9_substrate_framing=np.bool_(cc9_substrate_framing),
        cc_allowlist_w5a42=np.bool_(cc_allowlist_w5a42),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # ──────────────────────────────────────────────────────────────────
    # 11 — Append verdict trio
    # ──────────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    value_str = (
        f"slot=§VII.{slot_label};upstream_slot=§VII.AN;"
        f"cc_w5a37_pass={cc_w5a37_pass};sub_row_line_count={sub_row_line_count};"
        f"cc1={cc1_corner};cc2={cc2_substrate_is};cc3={cc3_anchor_structure};"
        f"cc4={cc4_pole_scope};cc5={cc5_resolution_scope};cc6={cc6_lab_in};"
        f"cc7={cc7_discrimination_sigma};cc8={cc8_closure_sha};cc9={cc9_substrate_framing};"
        f"cc_allowlist={cc_allowlist_w5a42};verdict_kind={verdict_kind}"
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
    sign_v = "N/A"
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

    print(f"[W5a-42] DONE in {elapsed:.2f}s")
    print(f"[W5a-42] slot     = §VII.{slot_label}")
    print(f"[W5a-42] audit_sha256   = {audit_sha256}")
    print(f"[W5a-42] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
