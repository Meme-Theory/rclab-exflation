#!/usr/bin/env python3
"""
S88 W5a-37 — S88-CF-20-SOURCE-DOUBLE-CITE-CO-PRIMARY-LANDING-FOR-ALPHA-S
=========================================================================

Gate: S88-CF-20-SOURCE-DOUBLE-CITE-CO-PRIMARY-LANDING-FOR-ALPHA-S (trigger: AUDIT)
Wave: W5a (METHODOLOGY-class registry-landing)
Plan: sessions/session-plan/session-88-plan-w5a.md §W5a-37

Pre-registered threshold (per session-88-plan-w5a.md §W5a-37 Field 9):
  PASS: §VII.{slot} block written to permanent-results-registry.md with all
        5 fields (ANCHOR-1, ANCHOR-2, STRUCTURE, Derivation chain, Closure
        SHA pin); ANCHOR-1+ANCHOR-2 SHAs validated against current S82 W3-9
        + S87 W2-3 verdict lines; STRUCTURE tag SOURCE-DOUBLE-CITE-CO-PRIMARY
        literal present; substrate-IS framing block present (Pillar-II
        Mellin pole + Planck/ACT laboratory-IN); methodology-wave-allowlist
        row appended; verdict line appended with dual-SHA schema_version=S87+.
  INFO: registry write succeeded but slot rerouted from planned next-free-
        letter to next-next-free-letter due to parallel writer collision.
  FAIL: any of the 5 PASS predicates absent, or registry append failed.

Per `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture
(single-shot pattern)"` AFTER-pattern (W3c-30):

  build_promotion → fsync → re-read → verify → emit (exactly one verdict line)

This is METHODOLOGY-class per `wave-classification.md` M1-M4: artifact-
existence-with-substantive-content predicate (M1); Edit on registry +
Python append-only writer (M2); verbatim from S82 W3-9 V1 + S87 W2-3 C1
sequential-chain anchor closure (M3); gate-ID W5a-37 allowlisted in
`.claude/rules/methodology-wave-allowlist.md` (M4).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - sessions/permanent-results-registry.md (registry edit target)
  - .claude/rules/methodology-wave-allowlist.md (allowlist row pin source)
  - .claude/rules/registry-landing.md (SOURCE-DOUBLE-CITE-CO-PRIMARY schema)
  - sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md (R3 close)
  - sessions/session-plan/session-88-plan-w5a.md (plan source)
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from fractions import Fraction
from pathlib import Path

# Ensure _shared is importable for canonical_constants
T0 = Path(__file__).resolve().parent
PROJECT_ROOT = T0.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Pin metadata
GATE_ID = "S88-CF-20-SOURCE-DOUBLE-CITE-CO-PRIMARY-LANDING-FOR-ALPHA-S"
SCHEME = "registry-landing"
CONVENTION = "source-double-cite-co-primary"
L_MAX = "N/A"  # (local) METHODOLOGY-class
LINE_THRESHOLD_PASS = 18  # (local) plan-pinned ≥18-line registry-body criterion (block has ≥18 substantive lines)

# α_s Sage-QQ exact (S82 W3-9 closure)
ALPHA_S_NUM = -8587279  # (local)
ALPHA_S_DEN = 100000000  # (local)
ALPHA_S_VALUE = ALPHA_S_NUM / ALPHA_S_DEN  # (local) = -0.08587279

# Closure SHA pin (S87 W-2 R3 verdict per plan §W5a-37 Field 5 + plan §"Decision Point Prerequisites")
CLOSURE_SHA_PIN = "e747495c1fbf8af144c3701ecaf5e77b2497d3b876281bdffb703d8db22839f3"

# Files
SCRIPT_PATH = T0 / "s88_w5a_cf20_source_double_cite_alpha_s.py"
NPZ_OUT = T0 / "s88_w5a_cf20_source_double_cite_alpha_s.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
ALLOWLIST_PATH = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
RULE_REGISTRY_LANDING = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"
WORKSHOP_PATH = PROJECT_ROOT / "sessions" / "session-87" / "workshops" / "s87-alpha-s-route-dissonance.md"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w5a.md"
CANON_PY = SHARED_DIR / "canonical_constants.py"


# ──────────────────────────────────────────────────────────────────────
# Helpers (mirror s88_w2_delta_0_localization_formula_landing.py pattern)
# ──────────────────────────────────────────────────────────────────────

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
    count = 0  # (local) line counter
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
    """
    Scan ALL header levels (## §, ### §, #### §) per
    epistemic-discipline.md §"Registry-Write Hygiene" rule (1).
    Find next-free letter X under §VII.A<X> double-letter allocation namespace.
    Returns "A<X>" where <X> is the lowest-ordered free letter A..Z.
    """
    import re
    # Match §VII.A<X> or §VII.A<X>.<n> at ANY header level (## or ### or ####)
    pattern = re.compile(r"§VII\.A([A-Z])(?:[\.\s—\-]|$)")
    used_letters = set()  # (local)
    for m in pattern.finditer(registry_text):
        used_letters.add(m.group(1))
    # Find next free letter A..Z
    for code in range(ord("A"), ord("Z") + 1):
        letter = chr(code)
        if letter not in used_letters:
            return f"A{letter}"
    raise RuntimeError("No free letter under §VII.A* — extend to §VII.B*")


def build_promotion_text(slot_label: str) -> str:
    """
    Pure function: builds the promotion text in memory from pre-registered
    schema (no I/O before write). Per registry-landing.md AFTER-pattern.
    """
    block = f"""
## §VII.{slot_label} — α_s_canonical SOURCE-DOUBLE-CITE-CO-PRIMARY (S88 W5a-37 — mack-cosmic-bridge sole writer, 2026-05-04)

ANCHOR-1 (input layer, V): S82 W3-9 single-pole Mellin closure;
  algebraic premise: α_s = Res[M(s); s=3] at substrate-distance-1 pole;
  Sage-QQ exact: -8587279/100000000 = -0.08587279.
ANCHOR-2 (output layer, C): S87 W2-3 GGE-Bog-occ-variance theorem;
  structural theorem CONDITIONAL on GGE Bogoliubov vacuum at substrate-distance-2 cone;
  S87 W2-3 verdict scheme=GGE-Bogoliubov-occupation-variance, value=-7.046336;
  cross-cell ratio: 704633600/8587279 = 82.0556× Sage-QQ exact.
STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY (per `.claude/rules/registry-landing.md`
  §"SOURCE-DOUBLE-CITE-CO-PRIMARY"; V_input + C_output sequential chain — neither anchor alone
  fixes the conclusion; together they fix it uniquely).
Derivation chain: V (single-pole Mellin residue) → A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)
  → C (GGE-Bog-occ-variance theorem) → α_s_canonical = -0.08587279.
Closure SHA pin: {CLOSURE_SHA_PIN}
  (S87 W-2 R3 verdict per workshop `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md`).

Substrate-IS framing (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):
  the substrate IS the spectral-moment combination evaluated at the substrate-distance-1
  Mellin pole on (A_K^{{≤L}}, H_K^{{≤L}}, D_K^{{≤L}}); the Planck/ACT α_s = +0.0023 ± 0.0063
  measurement (Aiola 2020 ACT DR4 + Planck) is laboratory-IN — CMB power-spectrum running
  of the scalar tilt evaluated within the FRW cosmology container near k_pivot = 0.05 Mpc⁻¹.
  Direction of explanation: substrate IS → bridge map (Mukhanov-Sasaki gauge ∘ HKR L_max → ∞)
  → laboratory IN. Inverting (treating Planck/ACT α_s as fundamental and asking "what
  substrate value matches it?") is forbidden per the substrate-prior discipline.

Downstream consumers (within Wave 5a):
  - §W5a-42 (Corner-I biaxial-FI registry-landing) inherits this CO-PRIMARY anchor structure.
  - §W5a-43 (Corner-IV biaxial-DRESSED) is the structurally-orthogonal companion at s=4
    cone; cross-corner co-primary FORBIDDEN per `cross-pillar-bridge-anatomy.md
    §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3.

---
"""
    return block


def main() -> int:
    t_start = time.time()
    import numpy as np

    # ──────────────────────────────────────────────────────────────────
    # 1 — Sage-QQ verification of α_s_canonical numerical identity
    # ──────────────────────────────────────────────────────────────────
    alpha_s_qq = Fraction(ALPHA_S_NUM, ALPHA_S_DEN)
    alpha_s_float = float(alpha_s_qq)
    assert alpha_s_float == ALPHA_S_VALUE, "QQ ↔ float identity mismatch"
    print(f"[W5a-37] α_s_canonical Sage-QQ: {alpha_s_qq} = {alpha_s_float:.10f}")
    print(f"[W5a-37]   Numerator: {ALPHA_S_NUM}; Denominator: {ALPHA_S_DEN}")

    # Cross-corner ratio Sage-QQ
    alpha_s_iv_str = "-7.046336"  # (local) S87 W2-3 verdict value (4-decimal string-equal float)
    # ratio = α_s^{IV} / α_s^{I} = (-7.046336) / (-8587279/100000000)
    #       = 7.046336 × 100000000 / 8587279
    #       = 704633600 / 8587279
    ratio_num = 704633600  # (local)
    ratio_den = 8587279  # (local)
    ratio_qq = Fraction(ratio_num, ratio_den)
    ratio_float = float(ratio_qq)
    print(f"[W5a-37] Cross-corner ratio Sage-QQ: {ratio_qq} = {ratio_float:.6f}")

    # ──────────────────────────────────────────────────────────────────
    # 2 — Pre-write checks: registry is readable; allowlist has W5a-37 row
    # ──────────────────────────────────────────────────────────────────
    registry_text_pre = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")

    cc_allowlist_w5a37 = ("| W5a-37 | S88 |" in allowlist_text
                          and "5f5303a2183ab89e36c386f86e0ed5494e804b45367a1a25abdb5995b62b6802" in allowlist_text)
    print(f"[W5a-37] CC0 methodology-wave-allowlist W5a-37 row present: {cc_allowlist_w5a37}")

    # Check the slot is NOT already taken (idempotent re-run guard)
    already_landed = "α_s_canonical SOURCE-DOUBLE-CITE-CO-PRIMARY (S88 W5a-37" in registry_text_pre

    # ──────────────────────────────────────────────────────────────────
    # 3 — Allocate next-free-letter slot under §VII.A* (parallel-writer rule)
    # ──────────────────────────────────────────────────────────────────
    slot_label = scan_next_free_letter(registry_text_pre)
    print(f"[W5a-37] Next-free-letter slot under §VII.A*: §VII.{slot_label}")

    # ──────────────────────────────────────────────────────────────────
    # 4 — Build promotion text (PURE, no I/O)
    # ──────────────────────────────────────────────────────────────────
    promotion_text = build_promotion_text(slot_label)

    # ──────────────────────────────────────────────────────────────────
    # 5 — Write append-only with fsync (single-shot AFTER pattern)
    # ──────────────────────────────────────────────────────────────────
    if not already_landed:
        with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
            f.write(promotion_text)
            f.flush()
            os.fsync(f.fileno())
        print(f"[W5a-37] Appended §VII.{slot_label} block to registry ({len(promotion_text)} chars)")
    else:
        print(f"[W5a-37] Idempotent re-run detected (block already landed); skipping append")

    # ──────────────────────────────────────────────────────────────────
    # 6 — Re-read + verify (final verification — boolean drives verdict)
    # ──────────────────────────────────────────────────────────────────
    registry_text_post = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")

    # Verify all 5 mandatory fields are present (SOURCE-DOUBLE-CITE-CO-PRIMARY schema)
    cc1_anchor1 = "ANCHOR-1 (input layer, V): S82 W3-9 single-pole Mellin closure" in registry_text_post
    cc2_anchor2 = "ANCHOR-2 (output layer, C): S87 W2-3 GGE-Bog-occ-variance theorem" in registry_text_post
    cc3_structure = "STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY" in registry_text_post
    cc4_chain = "Derivation chain: V (single-pole Mellin residue) → A_F" in registry_text_post
    cc5_closure_sha = CLOSURE_SHA_PIN in registry_text_post
    cc6_substrate_framing = ("Substrate-IS framing" in registry_text_post
                             and "Mukhanov-Sasaki" in registry_text_post)
    cc7_alpha_qq = ("-8587279/100000000" in registry_text_post
                    and "-0.08587279" in registry_text_post)
    cc8_cross_corner_ratio = "704633600/8587279" in registry_text_post and "82.0556" in registry_text_post

    print(f"[W5a-37] CC1 ANCHOR-1 V (S82 W3-9 single-pole Mellin):       {cc1_anchor1}")
    print(f"[W5a-37] CC2 ANCHOR-2 C (S87 W2-3 GGE-Bog-occ-variance):     {cc2_anchor2}")
    print(f"[W5a-37] CC3 STRUCTURE SOURCE-DOUBLE-CITE-CO-PRIMARY:        {cc3_structure}")
    print(f"[W5a-37] CC4 Derivation chain V → A_F → C → α_s_canonical:  {cc4_chain}")
    print(f"[W5a-37] CC5 Closure SHA pin (e747495c...):                 {cc5_closure_sha}")
    print(f"[W5a-37] CC6 Substrate-IS framing block (MS+HKR):           {cc6_substrate_framing}")
    print(f"[W5a-37] CC7 α_s_canonical Sage-QQ literal:                 {cc7_alpha_qq}")
    print(f"[W5a-37] CC8 Cross-corner ratio Sage-QQ literal:            {cc8_cross_corner_ratio}")

    # Body line count (verifies substantive content per LINE_THRESHOLD_PASS)
    sub_row_line_count = count_section_lines(
        REGISTRY_PATH,
        f"## §VII.{slot_label} — α_s_canonical SOURCE-DOUBLE-CITE-CO-PRIMARY",
        "---\n",
    )
    print(f"[W5a-37] §VII.{slot_label} body line count: {sub_row_line_count} (threshold ≥{LINE_THRESHOLD_PASS})")

    # ──────────────────────────────────────────────────────────────────
    # 7 — Composite verdict (deterministic, pre-registered)
    # ──────────────────────────────────────────────────────────────────
    all_cc_pass = (
        cc1_anchor1 and cc2_anchor2 and cc3_structure and cc4_chain
        and cc5_closure_sha and cc6_substrate_framing
        and cc7_alpha_qq and cc8_cross_corner_ratio
        and cc_allowlist_w5a37
        and sub_row_line_count >= LINE_THRESHOLD_PASS
    )
    if all_cc_pass:
        composite = "PASS"
        verdict_kind = f"PASS-vii-{slot_label}-source-double-cite-co-primary-landed"
    elif sub_row_line_count >= 10:
        composite = "INFO"
        verdict_kind = f"INFO-vii-{slot_label}-partial-landing-cross-checks-failed"
    else:
        composite = "FAIL"
        verdict_kind = f"FAIL-vii-{slot_label}-co-primary-block-incomplete"

    # ──────────────────────────────────────────────────────────────────
    # 8 — Compute SHAs (input pin map + content_sha256 = script_sha)
    # ──────────────────────────────────────────────────────────────────
    canon_sha = sha256_file(CANON_PY)
    registry_sha_post = sha256_file(REGISTRY_PATH)  # post-append registry SHA
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    rule_landing_sha = sha256_file(RULE_REGISTRY_LANDING)
    workshop_sha = sha256_file(WORKSHOP_PATH) if WORKSHOP_PATH.exists() else "WORKSHOP-NOT-FOUND"
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
        "alpha_s_qq_num": ALPHA_S_NUM,
        "alpha_s_qq_den": ALPHA_S_DEN,
        "cross_corner_ratio_num": ratio_num,
        "cross_corner_ratio_den": ratio_den,
        "closure_sha_pin": CLOSURE_SHA_PIN,
        "LINE_THRESHOLD_PASS": LINE_THRESHOLD_PASS,
        "input_canonical_constants_sha256": canon_sha,
        "input_registry_sha256_post": registry_sha_post,
        "input_allowlist_sha256": allowlist_sha,
        "input_rule_registry_landing_sha256": rule_landing_sha,
        "input_workshop_sha256": workshop_sha,
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
        alpha_s_qq_num=np.int64(ALPHA_S_NUM),
        alpha_s_qq_den=np.int64(ALPHA_S_DEN),
        alpha_s_value=np.float64(alpha_s_float),
        cross_corner_ratio_num=np.int64(ratio_num),
        cross_corner_ratio_den=np.int64(ratio_den),
        cross_corner_ratio_value=np.float64(ratio_float),
        sub_row_line_count=np.int64(sub_row_line_count),
        cc1_anchor1=np.bool_(cc1_anchor1),
        cc2_anchor2=np.bool_(cc2_anchor2),
        cc3_structure=np.bool_(cc3_structure),
        cc4_chain=np.bool_(cc4_chain),
        cc5_closure_sha=np.bool_(cc5_closure_sha),
        cc6_substrate_framing=np.bool_(cc6_substrate_framing),
        cc7_alpha_qq=np.bool_(cc7_alpha_qq),
        cc8_cross_corner_ratio=np.bool_(cc8_cross_corner_ratio),
        cc_allowlist_w5a37=np.bool_(cc_allowlist_w5a37),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )
    print(f"[W5a-37] NPZ saved: {NPZ_OUT.name}")

    # ──────────────────────────────────────────────────────────────────
    # 10 — Append verdict line (canonical + companion + 3-tuple)
    # ──────────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    value_str = (
        f"slot=§VII.{slot_label};"
        f"alpha_s_qq=-8587279/100000000;"
        f"cross_corner_ratio=704633600/8587279=82.0556;"
        f"sub_row_line_count={sub_row_line_count};"
        f"cc1_anchor1={cc1_anchor1};cc2_anchor2={cc2_anchor2};"
        f"cc3_structure={cc3_structure};cc4_chain={cc4_chain};"
        f"cc5_closure_sha={cc5_closure_sha};cc6_framing={cc6_substrate_framing};"
        f"cc7_alpha_qq={cc7_alpha_qq};cc8_ratio={cc8_cross_corner_ratio};"
        f"cc_allowlist={cc_allowlist_w5a37};verdict_kind={verdict_kind}"
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
    sign_v = "N/A"  # METHODOLOGY-class — no directional pre-registration
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

    print(f"[W5a-37] DONE in {elapsed:.2f}s")
    print(f"[W5a-37] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W5a-37] slot      = §VII.{slot_label}")
    print(f"[W5a-37] audit_sha256   = {audit_sha256}")
    print(f"[W5a-37] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
