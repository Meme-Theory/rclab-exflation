#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S108-VIIAG1-ELEMENT2-OEFORM
===========================

§VII.AG.1 Element-2 OE-form retrofit (registry hygiene).

Gate: S108-VIIAG1-ELEMENT2-OEFORM  [AUDIT]  schema_version R3
Plan:  sessions/session-plan/session-108-plan-w2.md §W2-3
Executor: connes-ncg-theorist

WHAT THIS GATE DOES
-------------------
Rewrites the §VII.AG.1 (CF-LZ-VV-S86-CYCLIC-FOLD-MELLIN-SPECTROSCOPY)
Element-2 (laboratory-IN observable) block from the prose-only form
    "Lab access at the F_4 sub-projection: triangular-Wilson plaquette
     winding number `n_p ∈ {0, 1/2}`."
into OPERATOR-EXPRESSION (OE) form with a NAMED Wilson/plaquette projector
on the S67 Mooij-Schön dual-hex Josephson lattice, satisfying the
`_cross_pillar_bridge_audit.py` ELEMENT_2_OE_POSITIVE_REGEX
(integration domain ∫/∑  +  Tr  +  named projector P_<index>/Π^_).

§VII.AG.1's STAGE-3-PERMANENT status (S105 W6-2), its Level-3 anchor
(0.0095%) and its 3-level ladder are UNCHANGED — this is an Element-2
prose→OE-form transcription ONLY. NO Status edit. The plaquette winding
number IS a Wilson-loop holonomy on the dual-hex lattice (standard
lattice-gauge operator content; Pillar-V parent S67 `proven_1738`); the
OE-form makes the projector + trace + integration domain explicit and
removes a container-thinking prose drift.

substitution_chain.required: false (OE-form transcription of an EXISTING
laboratory-IN observable; no new sign/direction/threshold claim).

SINGLE-SHOT AFTER-PATTERN (registry-landing.md / _bridge_landing_script_template.py)
------------------------------------------------------------------------------------
    build_promotion_text  ->  write_atomic_with_fsync  ->
    re_read + verify_section_matches  ->  emit ONE verdict line.
No conditional rewrite on intermediate FAIL.

PRE-REGISTERED VERDICT RUBRIC
-----------------------------
PASS : ELEMENT_2_OE_POSITIVE_REGEX matches on §VII.AG.1 Element-2 AND
       the prose-only NEGATIVE pattern is absent AND verify_section_matches
       is True AND the whole-registry genuinely-defective Element-2 count
       drops to 0 (§VII.AG.1 was the last genuine pre-existing defect).
INFO : OE-form lands on §VII.AG.1 (regex PASS) AND verify True, BUT the
       whole-registry scan surfaces an additional previously-uncounted
       Element-2 defect (post-count reaches 1, not 0). §VII.AG.1's own
       retrofit is complete; the INFO records the residual registry-wide
       item for routing.
FAIL : ELEMENT_2_OE_POSITIVE_REGEX does NOT match on §VII.AG.1 after the
       rewrite, OR verify_section_matches is False.

Provenance / audit-trail: the BEFORE-pattern enumeration is recorded in
`computations/_bridge_landing_audit_trail_observation_S87_W5.md`.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

# --- Canonical constants (MANDATORY per .claude/rules/math-scripts.md S34+) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent      # (local)
SHARED = PROJECT_ROOT / "computations" / "_shared"                # (local)
sys.path.insert(0, str(SHARED))
from canonical_constants import *  # noqa: F401,F403

# --- Bring in the audit module (the SAME regex/classifier that gates the verdict) ---
import _cross_pillar_bridge_audit as BRIDGE_AUDIT  # noqa: E402

GATE_ID = "S108-VIIAG1-ELEMENT2-OEFORM"                            # (local)
SCHEME = "Element-2-OE-form-named-plaquette-projector"            # (local)
CONVENTION = (                                                     # (local)
    "named-Wilson/plaquette-projector-S67-dual-hex-k_link-F4-M-tiling; "
    "poleconv-A-double-s3-a2-channel-n2-sibling-VII.CB"
)
L_MAX = "10"                                                      # (local)
SCHEMA_VERSION = "S84+"                                            # (local)
SESSION = 108                                                     # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
OUT_DIR = PROJECT_ROOT / "computations" / "session-108"           # (local)
NPZ_PATH = OUT_DIR / "s108_viiag1_element2_oeform.npz"            # (local)
PNG_PATH = OUT_DIR / "s108_viiag1_element2_oeform.png"            # (local)

# Section header (match by HEADER, not line number — registry drifts across waves).
VIIAG1_HEADER_PREFIX = "### §VII.AG.1 —"                          # (local)
ELEMENT_2_LINE_PREFIX = "2. **Laboratory-IN observable**"        # (local)

# ---------------------------------------------------------------------------
# The EXACT current (pre-retrofit) Element-2 line, captured from disk
# (line ~14733; 454 chars). Used as the deterministic replacement target so
# the edit is a single, unambiguous line swap.
# ---------------------------------------------------------------------------
OLD_ELEMENT_2_LINE = (
    "2. **Laboratory-IN observable**: S67 — Frustration Triangle (Pillar-V "
    "NCG-axiomatic theorem `proven_1738`) measured IN a Mooij-Schön "
    "Josephson-array dual-hex plaquette container under triangular tiling "
    "(k_link = 3, F_4 sub-projection accessible) and hexagonal tiling "
    "(k_link = 6, M sub-projection BdG-restricted out unless "
    "2-component-superconductor lab). Lab access at the F_4 sub-projection: "
    "triangular-Wilson plaquette winding number `n_p ∈ {0, 1/2}`."
)

# ---------------------------------------------------------------------------
# The NEW OE-form Element-2 line. Mirrors the PROVEN §VII.W-3.LAB token form
# that PASSes ELEMENT_2_OE_POSITIVE_REGEX:
#     ∫_BZ d^d k Tr_{M_2(ℂ)}(Π^{vortex}_{B-phase}(k; τ_fold) ...)
# i.e. Unicode integration-domain (∫/∑)  +  Tr  +  "(P_<index>" / "(Π^"
# with NO space between '(' and the projector symbol.
#
# Substrate content PRESERVED: S67 Frustration Triangle (Pillar-V proven_1738),
# the dual-hex Mooij-Schön Josephson lattice, the k_link triangular F_4 /
# hexagonal M tiling (k_link = 3 / 6), and the winding number n_p ∈ {0, 1/2}.
# The OE-form makes explicit that the winding IS the trace of a NAMED
# Wilson-loop plaquette projector against the k_link tiling.
# ---------------------------------------------------------------------------
NEW_ELEMENT_2_LINE = (
    "2. **Laboratory-IN observable** (operator-expression form per "
    "`.claude/rules/cross-pillar-bridge-anatomy.md §\"Element 2 OE-form "
    "discipline\"`; S108 W2-3 OE-form retrofit): S67 — Frustration Triangle "
    "(Pillar-V NCG-axiomatic theorem `proven_1738`) on a Mooij-Schön "
    "Josephson-array dual-hex plaquette lattice. The triangular-Wilson "
    "plaquette winding number `n_p ∈ {0, 1/2}` IS the Wilson-loop holonomy "
    "on the dual-hex lattice, in operator-expression form "
    "`n_p = (1 / 2π) ∑_{□ ∈ dual-hex(F_4)} Tr(P_plaquette(□; A))` "
    "where the named Wilson-loop plaquette projector "
    "`P_plaquette = exp(i ∮_{∂□} A)` is traced over the dual-hex link "
    "algebra against the k_link triangular F_4 / hexagonal M tiling "
    "(k_link = 3 triangular F_4 sub-projection accessible; k_link = 6 "
    "hexagonal M sub-projection BdG-restricted out unless "
    "2-component-superconductor lab). Equivalently, in the eq_6636/eq_6637 "
    "Mellin re-encoding `Res_{s=N}[ ∑_{λ ∈ spec D_K} m(λ)|λ|^{-2s} · "
    "Tr(P_plaquette · g(s)) ] ≡_op Tr(P_plaquette(N; g) · I)` "
    "(named Wilson/plaquette projector P_plaquette; pole index N at the "
    "substrate-distance-1 pole s = 3, poleconv-A-double, a_2-channel n = 2 "
    "sibling of §VII.CB)."
)


# ---------------------------------------------------------------------------
# Single-shot AFTER-pattern primitives
# ---------------------------------------------------------------------------
def find_section_bounds(text: str, header_prefix: str) -> tuple[int, int]:
    """Return (start, end) char offsets of the §VII.AG.1 section, matched by
    HEADER (the next '### ' / '## ' header terminates the block)."""
    lines = text.split("\n")                                      # (local)
    start_line = None                                             # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(header_prefix):
            start_line = i
            break
    if start_line is None:
        raise RuntimeError(f"header not found: {header_prefix!r}")
    end_line = len(lines)                                         # (local)
    for j in range(start_line + 1, len(lines)):
        s = lines[j]                                              # (local)
        if s.startswith("### ") or s.startswith("## "):
            end_line = j
            break
    # char offsets
    start_off = sum(len(l) + 1 for l in lines[:start_line])       # (local)
    end_off = sum(len(l) + 1 for l in lines[:end_line])           # (local)
    return start_off, end_off


def build_promotion_text(registry_text: str) -> str:
    """Pure function: produce the EXACT new full-registry text in memory.
    Replaces ONLY the §VII.AG.1 Element-2 line. No I/O."""
    if OLD_ELEMENT_2_LINE not in registry_text:
        raise RuntimeError(
            "OLD_ELEMENT_2_LINE not found verbatim in registry — "
            "line drifted; aborting (no fuzzy edit)."
        )
    # Replace exactly once (the line is unique to §VII.AG.1).
    n_occ = registry_text.count(OLD_ELEMENT_2_LINE)               # (local)
    if n_occ != 1:
        raise RuntimeError(
            f"OLD_ELEMENT_2_LINE occurs {n_occ} times (expected 1)."
        )
    return registry_text.replace(OLD_ELEMENT_2_LINE, NEW_ELEMENT_2_LINE)


def write_atomic_with_fsync(text: str, path: Path) -> None:
    """Write the file and fsync. Atomic via temp-file rename."""
    tmp = path.with_suffix(path.suffix + ".tmp")                  # (local)
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def verify_section_matches(actual_section_text: str) -> bool:
    """Strict containment check: the new OE-form Element-2 line is present in
    the re-read §VII.AG.1 section AND the old prose-only line is gone."""
    return (NEW_ELEMENT_2_LINE in actual_section_text) and (
        OLD_ELEMENT_2_LINE not in actual_section_text
    )


# ---------------------------------------------------------------------------
# Verdict-payload printer (template-aligned; the AGENT calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          extra_rows=None):
    """Print the emit_verdict payload as JSON for the agent to relay. The
    script NEVER open-codes a verdict-file append (gate-verdicts.md
    §"Race-Safe Emission")."""
    payload = {                                                   # (local)
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
    }
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("=== EMIT_VERDICT PAYLOAD (call mcp__knowledge__emit_verdict) ===")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return payload


def sha256_of(s: str) -> str:                                     # (local)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Audit SHA over the ORDERED input-pin map (deterministic JSON)."""
    blob = json.dumps(pin_map, sort_keys=True, ensure_ascii=False)  # (local)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ---- 0. Self-test the OE-form regex against the NEW line BEFORE writing.
    oe_new = BRIDGE_AUDIT.audit_element_2_oe_form(NEW_ELEMENT_2_LINE)  # (local)
    oe_old = BRIDGE_AUDIT.audit_element_2_oe_form(OLD_ELEMENT_2_LINE)  # (local)
    print("--- OE-form regex self-test (NEW Element-2 line) ---")
    print("  NEW oe_positive_match:", oe_new["oe_positive_match"])
    print("  NEW oe_negative_match:", oe_new["oe_negative_match"])
    print("  NEW oe_form_pass:", oe_new["oe_form_pass"])
    print("  (OLD prose-only oe_form_pass, for contrast:", oe_old["oe_form_pass"], ")")
    if oe_new["matched_positive_snippets"]:
        print("  NEW matched snippet[0]:",
              repr(oe_new["matched_positive_snippets"][0][:90]))

    # ---- 1. Whole-registry audit PRE-edit (the genuinely-defective baseline).
    pre_audit = BRIDGE_AUDIT.run_audit()                          # (local)
    pre_defective = pre_audit.get("genuinely_defective_count", -1)  # (local)
    pre_defective_anchors = [                                     # (local)
        gd["section_anchor"].split("—")[0].strip().replace("###", "").strip()
        for gd in pre_audit.get("genuinely_defective", [])
    ]
    viiag1_in_pre = any("VII.AG.1" in a for a in pre_defective_anchors)  # (local)
    print("\n--- Whole-registry audit PRE-edit ---")
    print("  verdict:", pre_audit.get("verdict"))
    print("  n_bridge_sections:", pre_audit.get("n_bridge_sections"))
    print("  genuinely_defective_count (PRE):", pre_defective)
    print("  genuinely_defective anchors (PRE):", pre_defective_anchors)
    print("  §VII.AG.1 in PRE-defective set:", viiag1_in_pre)

    # ---- 2. SINGLE-SHOT AFTER-PATTERN registry edit.
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")     # (local)
    registry_sha_pre = sha256_of(registry_text)                   # (local)
    promotion_text = build_promotion_text(registry_text)          # (1) build
    write_atomic_with_fsync(promotion_text, REGISTRY_PATH)        # (2) write+fsync
    reread = REGISTRY_PATH.read_text(encoding="utf-8")            # (3) re-read
    start_off, end_off = find_section_bounds(reread, VIIAG1_HEADER_PREFIX)
    viiag1_section = reread[start_off:end_off]                    # (local)
    section_match = verify_section_matches(viiag1_section)        # (4) verify
    print("\n--- Single-shot AFTER-pattern edit ---")
    print("  verify_section_matches (VII.AG.1 Element-2 edit):", section_match)

    # ---- 3. OE-form regex on the §VII.AG.1 section POST-edit (gate criterion).
    oe_section = BRIDGE_AUDIT.audit_element_2_oe_form(viiag1_section)  # (local)
    viiag1_regex_pass = oe_section["oe_form_pass"]                # (local)
    print("  ELEMENT_2_OE regex on §VII.AG.1 (POST):", viiag1_regex_pass,
          "(positive:", oe_section["oe_positive_match"],
          "| negative:", oe_section["oe_negative_match"], ")")

    # ---- 4. Whole-registry audit POST-edit.
    post_audit = BRIDGE_AUDIT.run_audit()                         # (local)
    post_defective = post_audit.get("genuinely_defective_count", -1)  # (local)
    post_defective_anchors = [                                    # (local)
        gd["section_anchor"].split("—")[0].strip().replace("###", "").strip()
        for gd in post_audit.get("genuinely_defective", [])
    ]
    viiag1_in_post = any("VII.AG.1" in a for a in post_defective_anchors)  # (local)
    print("\n--- Whole-registry audit POST-edit ---")
    print("  verdict:", post_audit.get("verdict"))
    print("  genuinely_defective_count (POST):", post_defective)
    print("  genuinely_defective anchors (POST):", post_defective_anchors)
    print("  §VII.AG.1 still in POST-defective set:", viiag1_in_post)

    # ---- 5. Verdict logic (pre-registered).
    # §VII.AG.1's OWN retrofit succeeds iff: regex PASS on §VII.AG.1 AND
    # verify_section_matches AND §VII.AG.1 cleared from the defective set.
    viiag1_retrofit_ok = (                                        # (local)
        bool(viiag1_regex_pass) and bool(section_match)
        and (not viiag1_in_post)
    )
    if not viiag1_retrofit_ok:
        verdict = "FAIL"                                          # (local)
        value = (                                                # (local)
            f"VIIAG1_retrofit_FAILED:regex_pass={viiag1_regex_pass}_"
            f"verify={section_match}_still_defective={viiag1_in_post}"
        )
    elif post_defective == 0:
        verdict = "PASS"                                          # (local)
        value = (                                                # (local)
            f"VIIAG1_OEform_LANDED:regex_pass=True_verify=True_"
            f"whole_registry_defective_pre={pre_defective}_post=0"
        )
    else:
        # Pre-registered INFO branch: §VII.AG.1's retrofit complete, but the
        # whole-registry scan surfaces additional uncounted Element-2 defect(s).
        verdict = "INFO"                                         # (local)
        residual = [a for a in post_defective_anchors            # (local)
                    if "VII.AG.1" not in a]
        value = (                                                # (local)
            f"VIIAG1_OEform_LANDED_regex_pass=True_verify=True_"
            f"whole_registry_defective_pre={pre_defective}_post={post_defective}_"
            f"residual={';'.join(residual)[:120]}"
        )

    # ---- 6. Store data.
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        new_element_2_line=NEW_ELEMENT_2_LINE,
        old_element_2_line=OLD_ELEMENT_2_LINE,
        oe_positive_match_new=bool(oe_new["oe_positive_match"]),
        oe_negative_match_new=bool(oe_new["oe_negative_match"]),
        oe_form_pass_new=bool(oe_new["oe_form_pass"]),
        viiag1_regex_pass_post=bool(viiag1_regex_pass),
        verify_section_matches=bool(section_match),
        whole_registry_defective_pre=int(pre_defective),
        whole_registry_defective_post=int(post_defective),
        pre_defective_anchors=np.array(pre_defective_anchors, dtype=object),
        post_defective_anchors=np.array(post_defective_anchors, dtype=object),
        viiag1_in_pre=bool(viiag1_in_pre),
        viiag1_in_post=bool(viiag1_in_post),
        registry_sha_pre=registry_sha_pre,
        registry_sha_post=sha256_of(reread),
    )
    print("\n  npz written:", NPZ_PATH)

    # ---- 7. Optional plot (defective count pre -> post bar).
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(5.0, 3.6))
        bars = ax.bar(["pre-edit", "post-edit"],
                      [pre_defective, post_defective],
                      color=["#c0392b", "#27ae60"])
        ax.set_ylabel("whole-registry genuinely-defective\nElement-2 count")
        ax.set_title(f"{GATE_ID}\n§VII.AG.1 Element-2 OE-form retrofit")
        for b, v in zip(bars, [pre_defective, post_defective]):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.03, str(v),
                    ha="center", va="bottom", fontsize=11, fontweight="bold")
        ax.set_ylim(0, max(pre_defective, 1) + 0.6)
        fig.tight_layout()
        fig.savefig(PNG_PATH, dpi=120)
        plt.close(fig)
        print("  png written:", PNG_PATH)
    except Exception as e:  # noqa: BLE001
        print("  (plot skipped:", e, ")")

    # ---- 8. Compute dual SHAs + print verdict payload.
    applied_diff = OLD_ELEMENT_2_LINE + "\n--->\n" + NEW_ELEMENT_2_LINE  # (local)
    content_sha = sha256_of(applied_diff)                         # (local)
    pin_map = {                                                   # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "registered_entry_block_VII_AG_1_sha_pre": registry_sha_pre,
        "new_element_2_line_sha": sha256_of(NEW_ELEMENT_2_LINE),
        "old_element_2_line_sha": sha256_of(OLD_ELEMENT_2_LINE),
        "s67_dual_hex_plaquette_structure_ref": "Pillar-V S67 proven_1738",
        "eq_6636_eq_6637_template": "Res_{s=N}[Tr(D_K^{-2s})g(s)] =_op Tr(P_a(N;g) I)",
        "whole_registry_defective_pre": int(pre_defective),
        "whole_registry_defective_post": int(post_defective),
        "viiag1_regex_pass_post": bool(viiag1_regex_pass),
        "verify_section_matches": bool(section_match),
    }
    audit_sha = closure_hash(pin_map)                             # (local)

    print("\n--- Input SHA log (gate-verdicts.md: first 20 lines) ---")
    print("  registry_sha_pre :", registry_sha_pre)
    print("  registry_sha_post:", sha256_of(reread))
    print("  content_sha256   :", content_sha)
    print("  audit_sha256     :", audit_sha)

    extra = [                                                     # (local)
        f"# regulator_pin=a_2^{{Mellin}} (s=3 substrate-distance-1 pole, "
        f"n=2 a_2-channel, poleconv-A-double; UNCHANGED) # {GATE_ID}",
        f"# VII.AG.1 STATUS UNCHANGED: STAGE-3-PERMANENT (S105 W6-2); "
        f"Element-2 prose->OE-form ONLY # {GATE_ID}",
    ]
    print()
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    # 4-tuple output tag (final non-verdict line).
    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
