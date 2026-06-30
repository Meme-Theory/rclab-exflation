#!/usr/bin/env python3
"""
S88 W8-88 — S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING
==============================================================================

Gate: S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING (METHODOLOGY)
Wave: W8 (B-K-counter block, Wave 8 plan §W8-88)
Plan: sessions/session-plan/session-88-plan-w8.md §W8-88

Method (per plan §W8-88):
  1. Edit `.claude/rules/cross-pillar-bridge-anatomy.md` §"Three-Level Structural-
     Confidence Ladder" to insert §"Level-2 Layer Distinction" sub-section between
     Level-2 spec and Level-3 spec.
  2. Define Level-2-binding (HKR-image binds Level-1 cohomology class) vs
     Level-2-non-binding (bare-decomposition envelope, no HKR image to lab).
  3. Specify enforcement: registry-PASS criterion `Level-3 < Level-2 envelope`
     ONLY counts under Level-2-binding.
  4. Cross-link to §"Audit at plan-freeze" — auditor verifies Level-2 envelope is
     binding via explicit bridge-map citation.
  5. Append allowlist row `W8-88` to methodology-wave-allowlist.md.

Threshold (PASS iff ALL 5):
  (a) §"Level-2 Layer Distinction" sub-section present with Level-2-binding +
      Level-2-non-binding definitions verbatim
  (b) enforcement clause specifying Level-3 < Level-2 envelope only counts under
      Level-2-binding
  (c) cross-link to §"Audit at plan-freeze" present
  (d) allowlist row appended
  (e) substantive line count ≥ 15

Substrate framing (per phononic-framing.md §"IS Space, Not IN Space"):
  Level-2-binding is a structural property of the bridge map (HKR / Connes-
  Karoubi pairing). The substrate-IS observable on Pillar A binds to the
  laboratory-IN observable on Pillar B ONLY via HKR-image bridge maps; bare-
  decomposition envelopes describe substrate-internal Mellin-truncation
  convergence without binding to any continuum laboratory observable.

Substitution chain (per plan §W8-88, transcribed into rule-file body):
  Step 1: HKR : HH^*(A^{≤L}) → H^*_{dR}(continuum-image) (Hochschild-Kostant-
          Rosenberg, classical NCG).
  Step 2: Level-1 := [ε_substrate-IS] ↔ HKR-image[ε_laboratory-IN] at the
          cohomology-class level (regulator-invariant, L-independent).
  Step 3: A `L^{-α}` envelope on `‖HKR(c_L) - c_continuum‖` IS a binding envelope
          iff `c_continuum` is the HKR-image of the Level-1 cohomology class.
  Step 4: A `L^{-α}` envelope on `Tr(D_K^{-2s})` (Mellin moment, no HKR image
          to continuum observable) does NOT bind Level-1; it is a bare-
          decomposition envelope.
  Step 5 (direction): registry-PASS criterion `Level-3 < Level-2 envelope` is
          meaningful ONLY for Level-2-binding envelopes; applying it to non-
          binding envelopes admits false-PASS. Therefore the layer distinction
          MUST be enforced at the audit level.

This is a single-shot bridge-landing script per registry-landing.md §"Bridge-
Landing Script Architecture (single-shot pattern)" — build_promotion_text →
write_atomic_with_fsync → re-read → verify → emit (exactly one verdict).
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

# Ensure _shared is importable for canonical_constants
_T0 = Path(__file__).resolve().parent
_PROJECT_ROOT = _T0.parent.parent
_SHARED_DIR = _PROJECT_ROOT / "computations" / "_shared"
if str(_SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(_SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

GATE_ID = "S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING"
WP_ID = "W8-88"
SCHEME = "METHODOLOGY-rule-file-edit"
CONVENTION = "level2-binding-vs-non-binding-layer-distinction"
L_MAX = "N/A"

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPT_PATH = Path(__file__).resolve()
CROSS_PILLAR_RULE = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
ALLOWLIST_RULE = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
PLAN_W8 = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w8.md"
VERDICT_FILE = SCRIPT_PATH.parent / "s88_gate_verdicts.txt"
JSON_OUT = SCRIPT_PATH.parent / "s88_w8_level2_layer_distinction.json"


# ============================================================================
# Helpers
# ============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(pin_map: dict) -> str:
    return hashlib.sha256(
        json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def extract_plan_block(plan_text: str, anchor: str = "## §W8-88", terminator: str = "## §W8-89") -> str:
    """Extract the W8-88 gate block for SHA computation (plan-block SHA pin)."""
    start = plan_text.find(anchor)
    end = plan_text.find(terminator)
    if start == -1 or end == -1 or start >= end:
        raise RuntimeError(f"Could not locate plan §W8-88 block; start={start}, end={end}")
    return plan_text[start:end]


# ============================================================================
# Build the §"Level-2 Layer Distinction" sub-section text (verbatim per plan)
# ============================================================================

LEVEL2_LAYER_DISTINCTION_TEXT = """### Level-2 Layer Distinction (S88 W8-88 hardening)

> **Provenance**: S88 W8-88 RULE-EXTENSION (gen-physicist orchestrator PRIMARY; CO-AUTHOR connes-ncg-theorist for cohomology-class-binding rationale review per Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula). Closes the bare-decomposition envelope false-PASS pathway by construction at the rule-file level. Promoted via `methodology-wave-allowlist.md` row W8-88; `wave-classification.md` METHODOLOGY-class M1∧M2∧M3∧M4 conjunction.

The Level-2 algebraic-convergence-envelope spec admits TWO structurally distinct sub-classes that the registry-PASS criterion `Level-3 < Level-2 envelope at canonical L_max` treats DIFFERENTLY. Future cross-pillar bridge-theorem entries MUST declare which sub-class their Level-2 envelope inhabits; entries leaving the sub-class undeclared are registry-incomplete.

#### Level-2-binding (admissible for registry-PASS)

- **Definition**: the algebraic envelope `L^{-α}` is the convergence rate of an HKR-image (Hochschild-Kostant-Rosenberg map) that BINDS the Level-1 cohomology class. Operationally, the envelope bounds `‖HKR(c_L) − c_continuum‖` where `c_L` is the substrate-IS finite-L cocycle / Hochschild moment / spectral-triple invariant and `c_continuum` is the HKR-image realized as the laboratory-IN continuum observable on the partner pillar.
- **Calibration (W-5 §VII.AF.1)**: `L^{-3}` envelope at d=4 IS Level-2-binding. The HKR `L_max → ∞` map identifies the substrate-IS finite-L Hochschild pairing `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` with the laboratory-IN continuum BZ-trace `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` (Peotta-Törmä quantum-metric). The envelope describes convergence of the Level-1 cohomology-class binding under the bridge map; the predicted 0.10% bound at L_max=10 is a structural prediction about the HKR image, NOT a substrate-internal Mellin-truncation rate.

#### Level-2-non-binding (FORBIDDEN for registry-PASS)

- **Definition**: the algebraic envelope `L^{-α}` is a bare-decomposition convergence rate that does NOT bind Level-1. Operationally, the envelope bounds `‖c_L − c_∞‖` where `c_∞` is a substrate-internal limit (e.g., a bare Mellin truncation `Tr(D_K^{-2s})`) WITH NO HKR image to a continuum laboratory observable on the partner pillar.
- **Counter-example pattern**: a `L^{-α}` envelope on `Tr(D_K^{-2s})` evaluated at substrate-distance pole s ∈ {3, 4, ...} that lacks an HKR image to a continuum lab observable. Such an envelope describes substrate-internal Mellin-truncation convergence; it does NOT describe the convergence of any cross-pillar bridge map. The `c_continuum` reference quantity is undefined for this envelope class.

#### Substitution chain (cohomology-class binding; substrate-physics derivation)

Per `math-scripts.md §"Double-Check Logic Before Compute"`:

- **Step 1 (definition)**: HKR : HH^*(A^{≤L}) → H^*_{dR}(continuum-image) is the Hochschild-Kostant-Rosenberg map of classical NCG (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula context). It maps periodic Hochschild cohomology of the finite-L spectral algebra to de Rham cohomology of the continuum image.
- **Step 2 (definition)**: Level-1 of the cross-pillar bridge ladder states `[ε_substrate-IS] ↔ HKR-image[ε_laboratory-IN]` at the cohomology-class level (regulator-invariant, L-independent). The identity holds at every L_max.
- **Step 3 (substitution)**: A `L^{-α}` envelope on `‖HKR(c_L) − c_continuum‖` IS a Level-2-binding envelope iff `c_continuum` is the HKR-image of the Level-1 cohomology class. The envelope describes convergence of the Level-1 binding under the bridge map's `L → ∞` limit.
- **Step 4 (simplification)**: A `L^{-α}` envelope on `Tr(D_K^{-2s})` (substrate-internal Mellin moment, no HKR image to a continuum laboratory observable on the partner pillar) does NOT bind Level-1; it is a bare-decomposition envelope. The substrate-internal limit `c_∞ = lim_{L→∞} Tr(D_K^{<=L,-2s})` is an INTRINSIC substrate quantity, not a laboratory image.
- **Step 5 (direction)**: registry-PASS criterion `Level-3 < Level-2 envelope at canonical L_max` is MEANINGFUL ONLY for Level-2-binding envelopes; applying it to Level-2-non-binding envelopes admits false-PASS (the empirical Level-3 anchor passes a numerical bound on a quantity that does not bind to the laboratory measurement). Therefore the layer distinction MUST be enforced at the audit level.

#### Enforcement clause

The registry-PASS criterion `Level-3 empirical value < Level-2 envelope value at canonical L_max` (see §"Registry-PASS criterion" above) COUNTS toward registry-PASS if and only if the Level-2 envelope is Level-2-binding per this sub-section's definition. Bare-decomposition envelopes (Level-2-non-binding) DO NOT contribute to registry-PASS regardless of how tightly the Level-3 anchor satisfies the numerical bound; their false-PASS pathway is closed by construction.

Specifically:

- IF Level-2-binding ∧ (Level-3 < Level-2 envelope at canonical L_max) → registry-PASS ELIGIBLE (other audit clauses still apply).
- IF Level-2-non-binding (regardless of Level-3 vs Level-2 numerical comparison) → registry-INELIGIBLE; the bridge entry is registry-incomplete and routes to plan-freeze halt with remediation request to cite the HKR / Connes-Karoubi / K-theory boundary bridge map and the corresponding `c_continuum` reference quantity in the partner pillar's continuum.
- IF Level-2 sub-class undeclared → registry-INCOMPLETE per §"Audit at plan-freeze" item-extension below; plan-freeze halt.

#### Cross-link to §"Audit at plan-freeze"

Plan-freeze validators landing a cross-pillar bridge entry MUST verify (extending the existing 4-item audit at §"Audit at plan-freeze"):

5. Level-2 envelope sub-class explicitly declared: Level-2-binding (with HKR / Connes-Karoubi pairing / K-theory boundary bridge map cited) OR Level-2-non-binding (REJECTED at plan-freeze halt; remediation: identify the bridge map and the HKR image of the Level-1 cohomology class, OR re-classify the entry as a substrate-internal observable NOT a cross-pillar bridge).
6. If Level-2-binding declared, the bridge map citation MUST be explicit (HKR / Connes-Karoubi / K-theory boundary — not "analogous" or "corresponds to"; see §"Audit at plan-freeze" item 4 for the existing convention).

The audit script `computations/_shared/_cross_pillar_bridge_audit.py` (S86 W-5 AUDIT-1, extended at S88 W7a-73 for OE-form discipline) is forward-extensible at S88 W8-88 to test the Level-2 sub-class declaration; the extension is queued as `S89-CROSS-PILLAR-BRIDGE-AUDIT-LEVEL2-SUB-CLASS-CHECK` and lands the regex-based detector for the `Level-2-binding` / `Level-2-non-binding` declaration tag in the bridge-anatomy block.

#### Calibration corpus

- **Instance #1 (positive; W-5 §VII.AF.1)**: `L^{-3}` envelope at d=4 IS Level-2-binding. The HKR `L_max → ∞` image binds the HP^1 cohomology class to the Peotta-Törmä quantum-metric trace; the empirical W5-6 atlas match 0.0095% F_4 strict at L_max=10 satisfies the binding envelope. Level-2-binding declaration MANDATORY (retroactively documented; pre-S88-W8-88 entry grandfathered with the sub-class flag).
- **Instance #2 (negative; counter-example pattern, no current registry entry)**: a hypothetical `L^{-α}` envelope on `Tr(D_K^{-2s})` evaluated at substrate-distance pole s=3 with no HKR image to a continuum lab observable on a partner pillar would be Level-2-non-binding and FAIL plan-freeze. Future cross-pillar bridge candidates (FWD-C1 / FWD-C2 / FWD-C3 per §"Three forward bridge candidates for S88+ dispatch") must demonstrate Level-2-binding via explicit HKR / Connes-Karoubi pairing citation.

#### Substrate framing (cross-link to phononic-framing.md §"IS Space, Not IN Space")

Level-2-binding vs Level-2-non-binding is a STRUCTURAL property of the bridge map at the substrate ↔ laboratory layer pair. The substrate-IS observable on Pillar A binds to the laboratory-IN observable on Pillar B ONLY via HKR-image bridge maps (or analogous Connes-Karoubi / K-theory boundary maps); bare-decomposition envelopes describe substrate-internal Mellin-truncation convergence without binding to any continuum laboratory. The direction of explanation flows:

```
Substrate (Pillar A) IS the [substrate-IS observable]
   → Bridge map (HKR; Level-2-binding REQUIRED)
   → Laboratory (Pillar B) IN [laboratory-IN observable]
```

A bare-decomposition envelope (Level-2-non-binding) lacks the bridge-map step; the would-be `c_continuum` reference is undefined, and the substrate-internal limit `c_∞` is NOT a laboratory observable. Treating such an envelope as registry-PASS-eligible inverts the substrate ↔ laboratory direction (a container-thinking violation per `phononic-framing.md`).

"""


def build_cross_pillar_edit(current_text: str) -> str:
    """Insert the §"Level-2 Layer Distinction" sub-section between Level-2 spec
    and Level-3 spec, per plan §W8-88 step 1."""
    # Anchor: insert just BEFORE the Level-3 heading
    anchor = "### Level 3 — Empirical Anchor at Canonical L_max"
    if anchor not in current_text:
        raise RuntimeError(f"Could not find anchor '{anchor}' in cross-pillar-bridge-anatomy.md")
    # Idempotency check: do not double-insert
    if "### Level-2 Layer Distinction (S88 W8-88 hardening)" in current_text:
        # Already inserted (re-run scenario); return text unchanged
        return current_text
    new_text = current_text.replace(
        anchor,
        LEVEL2_LAYER_DISTINCTION_TEXT + anchor,
        1,
    )
    return new_text


def build_allowlist_row(plan_block_sha: str) -> str:
    """Construct the W8-88 allowlist row per the row schema in
    methodology-wave-allowlist.md §"Schema"."""
    rationale = (
        "S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING "
        "(cross-pillar-bridge-anatomy.md §\"Three-Level Structural-Confidence Ladder\" Level-2 "
        "Layer Distinction sub-section landing — Level-2-binding (HKR-image binds Level-1 cohomology "
        "class; W-5 §VII.AF.1 calibration positive instance) vs Level-2-non-binding (bare-decomposition "
        "envelope on Tr(D_K^{-2s}) lacking HKR image to continuum lab observable; FORBIDDEN for "
        "registry-PASS) discipline; enforcement clause specifying registry-PASS criterion `Level-3 < "
        "Level-2 envelope at canonical L_max` only counts under Level-2-binding; cross-link to §\"Audit "
        "at plan-freeze\" extending audit items 5 and 6 with sub-class declaration MANDATORY + bridge-map "
        "explicit-citation MANDATORY; substitution chain (5-step cohomology-class binding) transcribed "
        "verbatim from plan §W8-88 step 6; closes bare-decomposition false-PASS pathway by construction "
        "at the rule-file level; M1-M4 conjunction satisfied [M1 artifact-existence on rule-file diff; "
        "M2 Edit on .claude/rules/cross-pillar-bridge-anatomy.md; M3 verbatim from plan §W8-88 substitution "
        "chain steps 1-5; M4 allowlist append herewith]; orchestrator-direct-write per "
        "wave-classification.md §\"Dispatch consequences\"; gen-physicist PRIMARY + connes-ncg-theorist "
        "CO-AUTHOR cohomology-class-binding review)"
    )
    return f"| W8-88 | S88 | {rationale} | {plan_block_sha} |\n"


def append_allowlist_row(current_text: str, row: str) -> str:
    """Append the W8-88 row at the end of the file (after W7b-79 last row).
    Idempotency: do not double-append."""
    if "| W8-88 | S88 |" in current_text:
        return current_text  # already appended; idempotent
    # Append at file end (matching precedent of W7b-79 row appended at file tail)
    if not current_text.endswith("\n"):
        current_text += "\n"
    return current_text + row


# ============================================================================
# Verify (5-clause threshold)
# ============================================================================

def verify_pass_conditions(updated_cp_text: str, updated_allow_text: str) -> dict:
    """Verify the 5 PASS conditions per plan §W8-88 threshold."""
    sub_section_anchor = "### Level-2 Layer Distinction (S88 W8-88 hardening)"
    in_sub_section = updated_cp_text.split(sub_section_anchor)
    if len(in_sub_section) < 2:
        sub_section_body = ""
    else:
        # Body extends until the §"Level 3" heading
        sub_section_body = in_sub_section[1].split("### Level 3 — Empirical Anchor at Canonical L_max")[0]

    cond_a = (
        sub_section_anchor in updated_cp_text
        and "**Level-2-binding" in updated_cp_text
        and "**Level-2-non-binding" in updated_cp_text
        and "HKR" in sub_section_body
        and "bare-decomposition" in sub_section_body
    )

    cond_b = (
        "registry-PASS criterion `Level-3 < Level-2 envelope at canonical L_max`" in updated_cp_text
        and "ONLY for Level-2-binding" in updated_cp_text
        # explicit text: enforcement clause body present
        and "Level-2-non-binding envelopes admits false-PASS" in updated_cp_text
    )

    cond_c = (
        "#### Cross-link to §\"Audit at plan-freeze\"" in updated_cp_text
        and "5. Level-2 envelope sub-class explicitly declared" in updated_cp_text
    )

    cond_d = "| W8-88 | S88 |" in updated_allow_text

    # Substantive line count: lines that are not blank and not pure markdown formatting
    sub_lines = [
        ln for ln in sub_section_body.splitlines()
        if ln.strip() and not ln.strip().startswith(("```",))
    ]
    cond_e_count = len(sub_lines)
    cond_e = cond_e_count >= 15

    return {
        "cond_a_definitions_verbatim": bool(cond_a),
        "cond_b_enforcement_clause": bool(cond_b),
        "cond_c_audit_cross_link": bool(cond_c),
        "cond_d_allowlist_row": bool(cond_d),
        "cond_e_substantive_line_count": int(cond_e_count),
        "cond_e_pass": bool(cond_e),
        "all_pass": bool(cond_a and cond_b and cond_c and cond_d and cond_e),
    }


# ============================================================================
# Main
# ============================================================================

def main() -> int:
    t_start = time.time()

    # ------------------------------------------------------------------------
    # Step 1 — Read BEFORE state of all input pins
    # ------------------------------------------------------------------------
    cp_before_text = CROSS_PILLAR_RULE.read_text(encoding="utf-8")
    allow_before_text = ALLOWLIST_RULE.read_text(encoding="utf-8")
    plan_text = PLAN_W8.read_text(encoding="utf-8")
    plan_block_text = extract_plan_block(plan_text)

    cp_before_sha = sha256_text(cp_before_text)
    allow_before_sha = sha256_text(allow_before_text)
    plan_block_sha = sha256_text(plan_block_text)
    plan_full_sha = sha256_file(PLAN_W8)
    script_sha = sha256_file(SCRIPT_PATH)

    print(f"[W8-88] BEFORE SHAs:")
    print(f"  cross-pillar-bridge-anatomy.md = {cp_before_sha}")
    print(f"  methodology-wave-allowlist.md  = {allow_before_sha}")
    print(f"  plan-block §W8-88              = {plan_block_sha}")
    print(f"  script                         = {script_sha}")

    # ------------------------------------------------------------------------
    # Step 2 — Build promotion text in memory (single-shot pattern)
    # ------------------------------------------------------------------------
    cp_after_text = build_cross_pillar_edit(cp_before_text)
    allow_row = build_allowlist_row(plan_block_sha)
    allow_after_text = append_allowlist_row(allow_before_text, allow_row)

    # ------------------------------------------------------------------------
    # Step 3 — Atomic write + fsync
    # ------------------------------------------------------------------------
    def write_atomic_with_fsync(path: Path, text: str) -> None:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())

    write_atomic_with_fsync(CROSS_PILLAR_RULE, cp_after_text)
    write_atomic_with_fsync(ALLOWLIST_RULE, allow_after_text)

    # ------------------------------------------------------------------------
    # Step 4 — Re-read + verify
    # ------------------------------------------------------------------------
    cp_after_reread = CROSS_PILLAR_RULE.read_text(encoding="utf-8")
    allow_after_reread = ALLOWLIST_RULE.read_text(encoding="utf-8")
    cp_after_sha = sha256_text(cp_after_reread)
    allow_after_sha = sha256_text(allow_after_reread)

    verify = verify_pass_conditions(cp_after_reread, allow_after_reread)
    composite = "PASS" if verify["all_pass"] else "FAIL"

    print(f"[W8-88] AFTER SHAs:")
    print(f"  cross-pillar-bridge-anatomy.md = {cp_after_sha}")
    print(f"  methodology-wave-allowlist.md  = {allow_after_sha}")
    print(f"[W8-88] Verify: {verify}")
    print(f"[W8-88] Composite verdict: {composite}")

    # ------------------------------------------------------------------------
    # Step 5 — Compute audit_sha256 from input-pin map and emit ONE verdict line
    # ------------------------------------------------------------------------
    pin_map = {
        "gate_id": GATE_ID,
        "wp_id": WP_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "input_cross_pillar_before_sha": cp_before_sha,
        "input_allowlist_before_sha": allow_before_sha,
        "input_plan_block_sha": plan_block_sha,
        "input_plan_full_sha": plan_full_sha,
        "input_script_sha": script_sha,
        "output_cross_pillar_after_sha": cp_after_sha,
        "output_allowlist_after_sha": allow_after_sha,
        "verify_cond_a": verify["cond_a_definitions_verbatim"],
        "verify_cond_b": verify["cond_b_enforcement_clause"],
        "verify_cond_c": verify["cond_c_audit_cross_link"],
        "verify_cond_d": verify["cond_d_allowlist_row"],
        "verify_cond_e": verify["cond_e_pass"],
        "verify_cond_e_line_count": verify["cond_e_substantive_line_count"],
        "composite": composite,
    }
    audit_sha256 = closure_hash(pin_map)
    content_sha256 = script_sha  # producing-script identity SHA

    # JSON sidecar (before/after SHAs pinned per spawn-prompt requirement)
    json_payload = {
        "gate_id": GATE_ID,
        "wp_id": WP_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "before_shas": {
            "cross_pillar_bridge_anatomy_md": cp_before_sha,
            "methodology_wave_allowlist_md": allow_before_sha,
            "plan_block_W8_88": plan_block_sha,
            "plan_full_w8": plan_full_sha,
            "script": script_sha,
        },
        "after_shas": {
            "cross_pillar_bridge_anatomy_md": cp_after_sha,
            "methodology_wave_allowlist_md": allow_after_sha,
        },
        "verify": verify,
        "composite": composite,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "elapsed_s": round(time.time() - t_start, 3),
    }
    JSON_OUT.write_text(
        json.dumps(json_payload, indent=2, sort_keys=True), encoding="utf-8"
    )

    value_str = (
        f"cond_a={int(verify['cond_a_definitions_verbatim'])};"
        f"cond_b={int(verify['cond_b_enforcement_clause'])};"
        f"cond_c={int(verify['cond_c_audit_cross_link'])};"
        f"cond_d={int(verify['cond_d_allowlist_row'])};"
        f"cond_e={int(verify['cond_e_pass'])};"
        f"line_count={verify['cond_e_substantive_line_count']};"
        f"cp_before_sha={cp_before_sha[:16]};cp_after_sha={cp_after_sha[:16]};"
        f"allow_before_sha={allow_before_sha[:16]};allow_after_sha={allow_after_sha[:16]}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    tuple_line = (
        f"# sign_verdict=N/A magnitude_verdict={composite} regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    elapsed = time.time() - t_start
    print(f"[W8-88] DONE in {elapsed:.2f}s; composite={composite}; audit_sha256={audit_sha256}")
    print(f"[W8-88] JSON: {JSON_OUT}")
    print(f"[W8-88] Verdict line appended to: {VERDICT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
