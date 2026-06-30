"""
s92_hk_vii_au_class_full_level3_landing_verdict.py
==================================================

S92-HK-VII-AU-CLASS-FULL-LEVEL-3-LANDING-WITH-MARGINAL-SATURATION

Emits the canonical verdict line + dual-SHA companion row + level-pin
discipline rows for the in-session housekeeping landing of the
CF-S93-W1-2 spec (executed at S92, NOT deferred to S93, per
`CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`).

This is a REGISTRY-LANDING closure, NOT a new physics computation. The
substrate-physics value rho_FULL_CC_VII_AU_SAT_s3 = 1.0076927826 was
ALREADY computed at gate S92-W1-CF-W9-8-2-VII-AU-FULL-PHYSICAL-RE-EXTRACTION
(INFO verdict, s92_gate_verdicts.txt:12). This gate documents that:
  (i)  rho_FULL_CC_VII_AU_SAT_s3 was promoted to canonical_constants.py
       SECTION E (line ~600 assignment; line ~1393 PROVENANCE) via
       update_constant() with full provenance (supersedes + marginal-
       saturation rate + corpus §19 cite);
  (ii) the §VII.AU.OP-PROJ registry entry gained a STRUCTURAL-ORTHOGONAL-
       COMPANION dual-reading block (Reading A SCHEMATIC convergence-exponent
       two-pin protocol RETAINED + Reading B FULL-CC residue-value
       CLASS=FULL-MARGINAL-SAT anchor) at the level-pin axis, NOT a slot-split.

The STAGE-1-CANDIDATE status is UNCHANGED (STAGE-3 promotion is a separate
concern, CF-S93-W5-1, genuinely blocked on Stage-2 PASS-AND). The Planck
n_s 2.0952sigma Level-3 empirical-anchor leg is UNCHANGED (a different
observable from the substrate-IS residue value rho_FULL).

Convention discipline: -FULL-CC-1996 + level-pin suffixes per
`substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY.

Exit code reflects SCRIPT HEALTH, not verdict (PASS is a valid result).
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

# -----------------------------------------------------------------------------
# Path discipline (project root contains a space — absolute paths only)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

# Canonical constants (MANDATORY per computations/_shared/CLAUDE.md). This
# landing closure cross-checks the just-promoted FULL-CC marginal-saturation
# anchor against its canonical_constants.py value (the SCHEMATIC Reading-A
# two-pin protocol is imported alongside to confirm both readings co-exist).
from canonical_constants import (  # noqa: E402
    rho_FULL_CC_VII_AU_SAT_s3,
    alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,
    alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,
)

VERDICT_TXT = PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

GATE_ID = "S92-HK-VII-AU-CLASS-FULL-LEVEL-3-LANDING-WITH-MARGINAL-SATURATION"
SCHEME = (
    "registry-landing-structural-orthogonal-companion-dual-reading-"
    "level-pin-axis-SCHEMATIC-plus-FULL-CC-AFTER-pattern"
)
CONVENTION = (
    "VII-AU-OP-PROJ-CLASS-FULL-MARGINAL-SAT-Reading-B-residue-value-companion-"
    "to-SCHEMATIC-Reading-A-convergence-exponent-two-pin-FULL-CC-1996-"
    "substrate-distance-1-pole-s3-Lmax-14-K4-MANDATORY-level-pin-discipline"
)
L_MAX = "12_14"  # (local) Reading-B FULL-CC L_max pair {12,14}

# Option A supersedes-tag (full 64-char; S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX)
SUPERSEDES_TARGET = "0da19aba653fa19ddf7bf2178581ec5c767c115e4508dd6e92906e68e6875e1f"

# -----------------------------------------------------------------------------
# Input-pin map: artifacts this landing depends on (per W9a-99 dual-SHA split).
# audit_sha256 = sha256 over (sorted pin SHAs) — sig_5-safe (computed, not
# hardcoded). content_sha256 = sha256 over this producing script's own bytes.
# -----------------------------------------------------------------------------
INPUT_FILES = {
    "computations/_shared/canonical_constants.py":
        PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py",
    "sessions/permanent-results-registry.md":
        PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
    "computations/session-92/s92_w1_cf_w9_8_2_vii_au_full_physical_re_extraction.npz":
        PROJECT_ROOT / "computations" / "session-92"
        / "s92_w1_cf_w9_8_2_vii_au_full_physical_re_extraction.npz",
    "computations/session-92/s92_gate_verdicts.txt":
        VERDICT_TXT,
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    """Stable hash over input-pin SHAs (invariant to dict ordering)."""
    h = hashlib.sha256()
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def main() -> int:
    print(f"=== {GATE_ID} ===")
    print("Registry-landing closure (NOT a new physics computation).")

    # 1) Compute input-pin SHA map
    pins = {k: sha256_of(p) for k, p in INPUT_FILES.items()}  # (local)
    print("\n=== Input pins (SHA-256 heads) ===")
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}")

    # 2) Confirm the landing's two effects are on disk (verification gate)
    cc_path = INPUT_FILES["computations/_shared/canonical_constants.py"]
    cc_text = cc_path.read_text(encoding="utf-8")  # (local)
    # Cross-check imported canonical values (load-bearing import per
    # computations/_shared/CLAUDE.md): the FULL-CC anchor matches the spec,
    # and the SCHEMATIC Reading-A two-pin protocol co-exists at its canonical
    # values (1.0076927826 / -3 / 2.6926236951422458).
    const_value_matches = (
        abs(rho_FULL_CC_VII_AU_SAT_s3 - 1.0076927826) < 1e-12
        and alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC == -3
        and abs(alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22 - 2.6926236951422458)
        < 1e-12
    )  # (local)
    print(f"  imported rho_FULL_CC_VII_AU_SAT_s3      : {rho_FULL_CC_VII_AU_SAT_s3}")
    print(f"  imported alpha_canonical (asymptotic)   : {alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC}")
    print(f"  imported alpha_sample (PATHWAY_B L15_22): {alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22}")
    const_assigned = (
        "rho_FULL_CC_VII_AU_SAT_s3 = 1.0076927826" in cc_text
        and const_value_matches
    )  # (local)
    const_in_provenance = (
        '"rho_FULL_CC_VII_AU_SAT_s3"' in cc_text
    )  # (local)

    reg_path = INPUT_FILES["sessions/permanent-results-registry.md"]
    reg_text = reg_path.read_text(encoding="utf-8")  # (local)
    companion_block_present = (
        "S92 W1 (CF-W9-8-2) STRUCTURAL-ORTHOGONAL-COMPANION dual reading" in reg_text
        and "CLASS=FULL-MARGINAL-SAT" in reg_text
        and "rho_FULL_CC_VII_AU_SAT_s3 = 1.0076927826" in reg_text
    )  # (local)
    schematic_retained = (
        "alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = -3" in reg_text
        and "alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22 = 2.6926236951422458"
        in reg_text
    )  # (local)
    # STAGE-1-CANDIDATE status must be UNTOUCHED on the §VII.AU.OP-PROJ slot
    stage_tag_intact = (
        "§VII.AU.OP-PROJ — FWD-C1 Pillar I↔II Bridge Theorem Candidate "
        "(W7c REGISTRY-1; STAGE-1-CANDIDATE" in reg_text
    )  # (local)

    print("\n=== Landing verification (on disk) ===")
    print(f"  canonical_constants assignment present : {const_assigned}")
    print(f"  canonical_constants PROVENANCE present : {const_in_provenance}")
    print(f"  registry companion block present       : {companion_block_present}")
    print(f"  SCHEMATIC two-pin protocol retained     : {schematic_retained}")
    print(f"  STAGE-1-CANDIDATE tag intact (untouched): {stage_tag_intact}")

    all_ok = (
        const_assigned
        and const_in_provenance
        and companion_block_present
        and schematic_retained
        and stage_tag_intact
    )  # (local)

    verdict = "PASS" if all_ok else "FAIL"  # (local) landing-on-disk verification

    # 3) Dual-SHA
    audit_sha = closure_hash(pins)  # (local)
    content_sha = hashlib.sha256(
        Path(__file__).resolve().read_bytes()
    ).hexdigest()  # (local)

    print("\n=== Dual-SHA ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    value_str = (
        f"landing_on_disk={verdict}_"
        f"rho_FULL_CC_VII_AU_SAT_s3=1.0076927826_"
        f"rho_FULL_L12=1.0100907902_rel_drift=2.3740515966e-03_"
        f"marginal_saturation_rate=0.0024_per_dL=2_INFO_band_[1e-3,1e-2)_"
        f"Reading_A_SCHEMATIC_alpha_canon=-3_alpha_sample=2.6926_RETAINED_"
        f"Reading_B_FULL_CC_CLASS=FULL-MARGINAL-SAT_"
        f"STAGE-1-CANDIDATE_UNCHANGED_Planck_ns_2.0952sigma_Level3_UNCHANGED_"
        f"canonical_constants_assigned={const_assigned}_provenance={const_in_provenance}_"
        f"companion_block={companion_block_present}_schematic_retained={schematic_retained}_"
        f"stage_tag_intact={stage_tag_intact}_"
        f"supersedes={SUPERSEDES_TARGET}"
    )  # (local)

    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)

    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"in-session housekeeping landing of CF-S93-W1-2 spec at S92 (NOT S93) "
        f"per CLAUDE.md No-Technical-Debt; supersedes={SUPERSEDES_TARGET}\n"
    )  # (local)

    level_pin_row = (
        f"# LEVEL_CLASS_PIN=FULL-MARGINAL-SAT "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY "
        f"level-pin: Reading B FULL-CC residue value rho_FULL_CC_VII_AU_SAT_s3 "
        f"(consumes _pauli_villars_subtraction.py PRIMARY helper; FULL CC1996 "
        f"§2.2-2.3 2-point PV multipliers; -FULL-CC-1996 + -CLASS-FULL-MARGINAL-SAT "
        f"suffix) STRUCTURAL-ORTHOGONAL-COMPANION to Reading A SCHEMATIC two-pin "
        f"convergence-exponent protocol (alpha_canonical=-3 + alpha_sample=2.6926 "
        f"RETAINED at CLASS=SCHEMATIC tier_pin=TIER-2)\n"
    )  # (local)

    corpus_row = (
        f"# CORPUS_CITE=cross-pillar-bridge-corpus.md§19 "
        f"# {GATE_ID} atlas-row + cache-moment are members of the weighting-functional "
        f"family (§19.0 line 997); 3-layer K-counter REJECTED (§19(c) line 1016); "
        f"Reading A + Reading B are STRUCTURAL-ORTHOGONAL-COMPANIONS at the level-pin "
        f"axis per registry-landing.md Operator-Projection Reading-A Naming Hygiene "
        f"MANDATORY K=3; NO sub-slot split\n"
    )  # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(level_pin_row)
        fp.write(corpus_row)

    print("\n=== Verdict line + companion rows appended ===")
    print(f"  {VERDICT_TXT}")
    print(f"  verdict = {verdict}")

    # Exit code reflects SCRIPT HEALTH only (PASS/FAIL is data, exit 0 either way).
    return 0


if __name__ == "__main__":
    sys.exit(main())
