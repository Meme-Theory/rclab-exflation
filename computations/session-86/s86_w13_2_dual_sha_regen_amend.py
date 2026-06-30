"""S86 1b S-9 V.1 carry-forward HOUSEKEEPING INSTALL — W13-2 dual-SHA regen amend.

Provenance
----------
Author       : lizzi-spectral-functional-theorist (S86 in-session install)
Source-spec  : sessions/archive/session-86/session-86-1b-s9-lizzi.md §3.1 + §5.1
Spawn-prompt : "do the V.1 carry-forward in-session" (user directive 2026-04-27)
Verdict file : computations/session-85/s85_gate_verdicts.txt (append-only)

Function
--------
Append a Schema-v2 dual-SHA companion ANNOTATION row to the W13-2 verdict in
``s85_gate_verdicts.txt`` so the §W8-3 recontextualization (band-width was
spectral slope, NOT truncation defect; C7 PASS at delta_rel=4.28%) surfaces at
the verdict-row level for grep-based downstream consumers and for future
knowledge MCP queries that index annotation rows.

The original W13-2 verdict line at s85_gate_verdicts.txt:201 is **PRESERVED
VERBATIM** (all-3-lines-retained discipline; S86 W1c-5 BULLETIN-S4 precedent +
S86 PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING line 144 amend pattern).

Schema reference
----------------
``.claude/rules/gate-verdicts.md`` §"S87+ canonical form" + W9a-99 dual-SHA
companion-row pattern + S85 W4-3/W4-6 ``info_reason=`` precedent.

Substitution chain — audit_sha256 computation
---------------------------------------------
Step 1 (definitions):
    audit_sha256(amend) = sha256( bytes(this_script)
                                  || bytes(canonical_constants.py)
                                  || pinmap_json_bytes )
    where pinmap_json is the canonical-sorted JSON of the input-pin map.

Step 2 (substitute):
    pins = {
      "original_w13_2_content_sha256":
            "58630dc36e59af32dfece11e521736c13c27f9a943a91ac03bb91249f2529779",
      "original_w13_2_audit_sha256":
            "f514d642fe2a80ac408ddc0a09da94c5a8590a0127b4754fd337ea57eb2c02c1",
      "w8_recontextualization_source":
            "session-86-w8-workingpaper.md_section_W8-3_lines_372_466_482",
      "w8_c7_pass_anchor": "S86-CGWB-LMAX-DIRECT_delta_rel=4.277e-2",
      "synthesis_provenance": "sessions/archive/session-86/session-86-1b-s9-lizzi.md",
    }

Step 3 (simplify):
    h_audit = sha256(); h_audit.update(script_bytes); h_audit.update(canonical_bytes);
    h_audit.update(pinmap_json); audit = h_audit.hexdigest()
    h_content = sha256(); h_content.update(script_bytes); content = h_content.hexdigest()

Step 4 (direction):
    By SHA-256 collision resistance, this audit/content pair is distinct from
    the original W13-2 row's audit_sha256=f514d642... and content_sha256=58630dc3...
    The composite line includes ``info_reason=`` plus a SECOND companion-row
    annotation to surface the recontextualization at MCP query time.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

# Tier0 canonical-constants import (mandatory per computations/_shared/CLAUDE.md).
# This script does no numerical physics computation; the import is here to
# satisfy the audit and to make canonical names available if the amend block
# ever needs to cite an observable value (none used in this run).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Section 1 — Identity (S86 housekeeping install)
# ---------------------------------------------------------------------------

GATE_ID = "S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT"  # row being amended (NOT a new gate)
AMEND_ID = "S86-W13-2-DUAL-SHA-REGEN-AMEND"  # this housekeeping install's identity
SCHEME = "zeta"  # preserved verbatim from original line
CONVENTION = (
    "LISA-PLS-2024+CMB-S4-Book-2019+recontextualization-W8-3"
)  # original convention + recontextualization tag
L_MAX = 10  # (local) preserved verbatim from original W13-2 line; not a framework const
SCHEMA_VERSION = "S86+"  # bumped from S84+ to mark the amend's schema-v2 annotation

REPO_ROOT = Path(__file__).resolve().parent.parent  # (local)
VERDICT_TXT = REPO_ROOT / "computations" / "session-85" / "s85_gate_verdicts.txt"  # (local)
CANONICAL_PY = REPO_ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
SYNTHESIS_MD = REPO_ROOT / "sessions" / "session-86" / "session-86-1b-s9-lizzi.md"  # (local)
W8_WP_MD = REPO_ROOT / "sessions" / "session-86" / "session-86-w8-workingpaper.md"  # (local)

# ---------------------------------------------------------------------------
# Section 2 — Input pins (the rows the amend binds to)
# ---------------------------------------------------------------------------

# Original W13-2 verdict row (s85_gate_verdicts.txt:201) — preserved VERBATIM upstream.
ORIGINAL_W13_2_AUDIT_SHA = (
    "f514d642fe2a80ac408ddc0a09da94c5a8590a0127b4754fd337ea57eb2c02c1"
)  # (local) read from s85_gate_verdicts.txt:201
ORIGINAL_W13_2_CONTENT_SHA = (
    "58630dc36e59af32dfece11e521736c13c27f9a943a91ac03bb91249f2529779"
)  # (local) read from s85_gate_verdicts.txt:201
ORIGINAL_W13_2_VALUE_TUPLE = (
    "(alpha_s=-0.068968,Omega_GW_LISA=8.299e-58,rho_cc=0.0,Fisher_PD=1)"
)  # (local) preserved
W8_C7_PASS_DELTA_REL = 4.277e-2  # (local) C7 PASS magnitude per §W8-3 line 385

# Annotation text — verbatim per session-86-1b-s9-lizzi.md §5.1 PASS criterion (iii)
INFO_REASON = (
    "recontextualized-S86-W8-3-band-width-was-spectral-slope-not-truncation-"
    "defect-C7-PASS-delta_rel-4.28pct"
)  # (local)

# Substantive recontextualization phrase, verbatim per §W8-3 line 482
RECONTEXTUALIZATION_PHRASE = (
    "INFO band-width-DIAGNOSTIC was spectral-slope, NOT truncation; "
    "C7 confirms truncation-stable at delta_rel = 4.28%"
)  # (local)

# Layer/arm/f_pivot fields per §VII.M.5 6-axis schema; bring W13-2 from 4/6 -> 6/6
LAYER = "experimental-Fisher"  # (local)
ARM = "signed-vs-magnitude"  # (local)
F_PIVOT = "3mHz-canonical-LISA-PLS-2024-derived"  # (local)


# ---------------------------------------------------------------------------
# Section 3 — Dual-SHA helpers (mirrors .claude/templates/script-template.py)
# ---------------------------------------------------------------------------

def closure_hash(pins: dict) -> str:
    """Stable hash over input pins (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(pins: dict) -> tuple[str, str]:
    """Return (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    script_path = Path(__file__).resolve()  # (local)
    script_bytes = script_path.read_bytes()  # (local)
    try:
        canonical_bytes = CANONICAL_PY.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


def file_sha256(path: Path) -> str:
    """Return SHA-256 of the file at path; '<missing>' if absent."""
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "<missing>"


# ---------------------------------------------------------------------------
# Section 4 — Compute amend SHAs
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # Build the input-pin map. Bind the amend to:
    #   (a) the row being amended (original W13-2 SHAs);
    #   (b) the W8-3 recontextualization source section + its current SHA;
    #   (c) the C7 PASS anchor;
    #   (d) the synthesis provenance file + its current SHA.
    pins = {  # (local)
        "original_w13_2_audit_sha256": ORIGINAL_W13_2_AUDIT_SHA,
        "original_w13_2_content_sha256": ORIGINAL_W13_2_CONTENT_SHA,
        "w8_recontextualization_source":
            "session-86-w8-workingpaper.md_section_W8-3_lines_372_466_482",
        "w8_workingpaper_sha256": file_sha256(W8_WP_MD),
        "w8_c7_pass_anchor":
            f"S86-CGWB-LMAX-DIRECT_delta_rel={W8_C7_PASS_DELTA_REL:.3e}",
        "synthesis_provenance_path":
            "sessions/archive/session-86/session-86-1b-s9-lizzi.md",
        "synthesis_provenance_sha256": file_sha256(SYNTHESIS_MD),
        "schema_reference":
            ".claude/rules/gate-verdicts.md_S87+_canonical_form",
        "amend_layer_pin": LAYER,
        "amend_arm_pin": ARM,
        "amend_f_pivot_pin": F_PIVOT,
    }

    # First 20 lines of stdout: input-pin map (audit-trail discipline)
    print(f"[s86_w13_2_dual_sha_regen_amend] AMEND_ID = {AMEND_ID}")
    print(f"[s86_w13_2_dual_sha_regen_amend] amending row = {GATE_ID}")
    print(f"[s86_w13_2_dual_sha_regen_amend] target file  = {VERDICT_TXT}")
    print("[s86_w13_2_dual_sha_regen_amend] input-pin map:")
    for k, v in sorted(pins.items()):
        v_disp = v if len(str(v)) < 80 else str(v)[:76] + "..."  # (local)
        print(f"  {k} = {v_disp}")

    # Compute the dual-SHA pair for the amend
    audit_sha, content_sha = compute_dual_sha(pins)  # (local)
    closure = closure_hash(pins)  # (local) intermediate, kept for audit-trail

    print()
    print(f"[s86_w13_2_dual_sha_regen_amend] amend audit_sha256   = {audit_sha}")
    print(f"[s86_w13_2_dual_sha_regen_amend] amend content_sha256 = {content_sha}")
    print(f"[s86_w13_2_dual_sha_regen_amend] amend closure_hash   = {closure}")

    # Direction-of-distinctness audit — verify amend SHAs differ from original
    assert audit_sha != ORIGINAL_W13_2_AUDIT_SHA, (
        "amend audit_sha256 collides with original W13-2 — abort"
    )
    assert content_sha != ORIGINAL_W13_2_CONTENT_SHA, (
        "amend content_sha256 collides with original W13-2 — abort"
    )

    # Build the amend block: ONE canonical verdict-style line + TWO companion rows
    # (Schema-v2 dual-SHA companion + recontextualization-annotation companion).
    # The composite top-line carries verdict=INFO (preserved from original) plus
    # info_reason= field per S85 W4-3/W4-6 precedent.
    #
    # The amend is APPEND-ONLY: original line at s85_gate_verdicts.txt:201 +
    # original companion at line 202 are PRESERVED VERBATIM upstream.

    amend_value_tuple = (
        f"(alpha_s=-0.068968,Omega_GW_LISA=8.299e-58,rho_cc=0.0,Fisher_PD=1,"
        f"layer={LAYER},arm={ARM},f_pivot={F_PIVOT},"
        f"recontext_anchor=delta_rel={W8_C7_PASS_DELTA_REL:.3e})"
    )  # (local) value tuple now carries layer/arm/f_pivot for §VII.M.5 6-axis schema

    canonical_line = (
        f"{GATE_ID}: INFO -- value={amend_value_tuple} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION} "
        f"info_reason={INFO_REASON}\n"
    )  # (local)

    dual_sha_companion = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"# {AMEND_ID} dual-SHA companion row "
        f"(W9a-99 split; amends row at s85_gate_verdicts.txt:201 per "
        f"S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING precedent + "
        f"all-3-lines-retained discipline S86 W1c-5 BULLETIN-S4)\n"
    )  # (local)

    annotation_companion = (
        f"# recontextualization annotation: {GATE_ID} "
        f"# {RECONTEXTUALIZATION_PHRASE} "
        f"-- source: sessions/archive/session-86/session-86-w8-workingpaper.md "
        f"section W8-3 lines 372/466/482 (anchor=S86-CGWB-LMAX-DIRECT PASS, "
        f"delta_rel={W8_C7_PASS_DELTA_REL:.3e}); "
        f"original_audit_sha256={ORIGINAL_W13_2_AUDIT_SHA[:16]}; "
        f"amend_audit_sha256={audit_sha[:16]}; "
        f"provenance: sessions/archive/session-86/session-86-1b-s9-lizzi.md "
        f"V.1 carry-forward in-session install; "
        f"installs §VII.M.5 4/6->6/6 layer/arm/f_pivot pins; "
        f"surfaces at MCP query_entity('gates',GATE_ID) post-knowledge.db rebuild\n"
    )  # (local)

    # Atomic append: a single open("a") write. Block-of-three is one buffer.
    amend_block = (  # (local)
        "\n# ===== S86 W13-2 DUAL-SHA REGEN AMEND (in-session V.1 install) =====\n"
        + canonical_line
        + dual_sha_companion
        + annotation_companion
        + f"# ===== end S86 W13-2 amend =====\n"
    )

    print()
    print("[s86_w13_2_dual_sha_regen_amend] block to append (verbatim):")
    print(amend_block)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(amend_block)

    print(
        f"[s86_w13_2_dual_sha_regen_amend] APPENDED 4 lines to {VERDICT_TXT.name}; "
        f"elapsed = {time.time() - t0:.3f}s"
    )

    # 4-tuple output (final non-verdict line per gate-verdicts.md protocol)
    print()
    print(
        f"4-tuple: (value={amend_value_tuple}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
