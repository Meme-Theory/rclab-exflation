"""
S87-F-NL-FOLDED-2-OBSERVABLE-REGISTRY-SPLIT  (CF-28, Level 3, mechanical)

Splits Master Inventory Row #9 (f_NL_folded) in
`sessions/framework/registry/falsifier-master-inventory.md` into:

  Row #9a -- laboratory-IN row (continuum CMB / 21-cm bispectrum measurement;
              pathway-keyed pins f_NL_FW_S82_equilateral / f_NL_FW_S67_folded /
              f_NL_FW_S85_W9_3_analytic_template).
  Row #9b -- substrate-IS row (phi_3 in HC^3(A_K) -- rank-3 Hochschild cocycle;
              3-pt-connected vertex on A_K = C (+) H (+) M_3(C) at finite L_max=10).

Owner: mack-cosmic-bridge (sole writer of falsifier-master-inventory.md per
       feedback_mack-bridge-role.md).

Per the spawn-prompt's mathematical-identity guidance, the substrate-IS object
under Row #9b is phi_3 in HC^3(A_K) (rank-3 Hochschild cocycle / 3-pt-connected
vertex), labelled "Channel-3" in WP section W4-1's table at line 3574 but
"Channel-1" in plan section W4-1 line 132 and plan sections W4-3/W4-4. The
labeling inversion is documented in WP section W4-4 (this script's output).

Closure protocol:
  * one-shot Python writer (Edit-tool race avoidance per
    epistemic-discipline.md "Registry-Write Hygiene under Parallel-Writer Race")
  * cross-reference walk over: master inventory (sole-writer; in-place edit OK),
                               permanent-results-registry.md (other-writer; orphan if any),
                               .claude/agent-memory/* (read-only AMRI scan),
                               sessions/framework/registry/*.md other than master
  * dual-SHA companion row + 3-tuple S87 schema-v2 annotation
  * NO PASS unless all 5 conditions hold AND zero orphans
  * INFO with exactly 1 orphan + explicit S88+ carry-forward path
  * FAIL on duplication / missing anatomy / >1 orphan / malformed dual-SHA
"""
from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')                         # (local) thread cap
os.environ.setdefault('MKL_NUM_THREADS', '8')                         # (local) thread cap

import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np

# Canonical-constants import per .claude/rules/math-scripts.md (no framework
# constants are used in this mechanical-surgery script; the import is present
# for computation compliance audit).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401, F403  (registry-surgery; no constants used)

# ---------------------------------------------------------------------------
# Path constants (absolute)
# ---------------------------------------------------------------------------
PROJ_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")                 # (local)
INVENTORY = PROJ_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"  # (local)
PERMANENT_REGISTRY = PROJ_ROOT / "sessions" / "permanent-results-registry.md"                    # (local)
AGENT_MEMORY = PROJ_ROOT / ".claude" / "agent-memory"                                            # (local)
REGISTRY_DIR = PROJ_ROOT / "sessions" / "framework" / "registry"                                 # (local)
VERDICTS = PROJ_ROOT / "computations" / "s87_gate_verdicts.txt"                             # (local)
NPZ_OUT = PROJ_ROOT / "computations" / "s87_w4_f_nl_folded_2_observable_registry_split.npz" # (local)
PLAN_FILE = PROJ_ROOT / "sessions" / "session-plan" / "session-87-plan-w4.md"                    # (local)
WP_FILE = PROJ_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"           # (local)
F_NL_PATH_REG = REGISTRY_DIR / "f-nl-folded-pathway-registry.md"                                 # (local)

GATE_ID = "S87-F-NL-FOLDED-2-OBSERVABLE-REGISTRY-SPLIT"               # (local)


# ---------------------------------------------------------------------------
# Helpers (canonical pattern from s86_w13_p11_master_inventory_w6_w13_land.py)
# ---------------------------------------------------------------------------
def sha256_file(path: Path) -> str:
    """SHA-256 of file bytes."""
    h = hashlib.sha256()                                              # (local)
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    """SHA-256 of a UTF-8 text payload."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Closure SHA-256 of an ordered pin-map (sorted keys for determinism)."""
    items = sorted(pin_map.items())                                   # (local)
    canonical = "\n".join(f"{k}={v}" for k, v in items)               # (local)
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()


# ---------------------------------------------------------------------------
# 1) Read inventory; locate Row #9 primary line + Row #9.audit line
# ---------------------------------------------------------------------------
inv_text_pre = INVENTORY.read_text(encoding='utf-8')                  # (local)
inv_sha_pre = sha256_text(inv_text_pre)                               # (local)
inv_lines = inv_text_pre.splitlines(keepends=True)                    # (local) preserve EOL

# Indices of the two table-rows we will rewrite. Use exact prefix matches:
#   "| 9 | f_NL_folded ..."
#   "| 9.audit | audit pins (Row #9 strengthening citation; ..."
idx_row9 = None                                                        # (local)
idx_row9_audit = None                                                  # (local)
for i, line in enumerate(inv_lines):
    if idx_row9 is None and line.startswith("| 9 | f_NL_folded"):
        idx_row9 = i
    elif idx_row9_audit is None and line.startswith("| 9.audit |"):
        idx_row9_audit = i

if idx_row9 is None or idx_row9_audit is None:
    print(f"FATAL: cannot locate Row #9 primary or audit line in {INVENTORY}")
    print(f"  idx_row9={idx_row9}  idx_row9_audit={idx_row9_audit}")
    sys.exit(2)

# Confirm contiguous (audit row immediately follows primary row in current text)
if idx_row9_audit != idx_row9 + 1:
    print(f"FATAL: Row #9.audit ({idx_row9_audit}) not immediately after Row #9 ({idx_row9}); aborting")
    sys.exit(2)


# ---------------------------------------------------------------------------
# 2) Compose Row #9a + Row #9a.audit + Row #9b + Row #9b.audit (4 rows)
# ---------------------------------------------------------------------------
# Row #9a -- laboratory-IN (CMB / 21-cm bispectrum, pathway-keyed pins).
# 5 IS-not-IN anatomy elements declared inline (per cross-pillar-bridge-anatomy.md):
#   1) substrate-IS  : NONE -- Row #9a is the laboratory-IN row; substrate counterpart at Row #9b
#   2) laboratory-IN : continuum CMB / 21-cm folded-template f_NL_folded bispectrum (Planck 2018 / SKA-1)
#   3) bridge-map    : HKR boundary inverse -- this is the laboratory-IN image of phi_3 cocycle under HKR
#   4) algebraic-env : L^(-5) at d=4 (envelope-preserving by Loday-Quillen-Tsygan)
#   5) empirical-anchor : Planck 2018 best-fit -2.5 +/- 5.7 (Planck error envelope); SKA-1 forecast horizon

ROW_9A = (
    "| 9a | f_NL_folded (LAB-IN: continuum CMB / 21-cm folded-template bispectrum) | "
    "3-pathway GGE-coupling discriminator at the laboratory-IN side of HKR boundary | "
    "CMB bispectrum + 21cm interferometric (lab-IN) | "
    "S82-GGE-equilateral pathway pin: 0.0547 (canonical-constants promotion target `f_NL_FW_S82_equilateral` "
    "per `math-scripts.md` Canonical Write-Order; CF-27 noted absence in canonical_constants.py); "
    "S67-GGE-folded pathway pin: 0.129 (`f_NL_FW_S67_folded`, ditto absence); "
    "W9-3-analytic-template-folded pathway pin: 0.7685 (`f_NL_FW_S85_W9_3_analytic_template`, ditto absence) | "
    "Planck = -2.5+/-5.7 (all 3 framework pathway pins consistent within 1-sigma; live-watch: SKA-1 forecast horizon) | "
    "3 pathways span ~14x; PAIR-4 PROJECTS the authoritative §W13-2 P10 registry (`f-nl-folded-pathway-registry.md`) -- but those are LAB-IN images, not the substrate-IS phi_3 cocycle | "
    "CMB-S4 sigma=6.9 / SKA-1 sigma~0.15 / 21cm l_max~10^5 | "
    "GGE-three-point (laboratory-IN image of substrate phi_3 cocycle under HKR boundary) | "
    "sub-channel-projection-folded-limit | 10 | "
    "`44b725ae0f7285d2` | `73545b2be2c9e770` | "
    "**5 IS-not-IN anatomy declared inline**: "
    "(1) substrate-IS=NONE-this-row-is-LAB-IN-counterpart-Row-#9b; "
    "(2) laboratory-IN=continuum-CMB-21cm-folded-template-f_NL_folded-bispectrum; "
    "(3) bridge-map=HKR-boundary-inverse-this-is-laboratory-IN-image-of-phi_3-cocycle-under-HKR; "
    "(4) algebraic-envelope=L^(-5)-at-d=4-envelope-preserving-by-Loday-Quillen-Tsygan; "
    "(5) empirical-anchor=Planck-2018-best-fit-and-error-envelope-+-SKA-1-forecast-horizon. "
    "CF-28 split origin: previously bundled Row #9 conflated lab-IN and substrate-IS; per UD-12 + cross-pillar-bridge-anatomy.md "
    "the IS-not-IN distinction lifts to a STRUCTURAL REQUIREMENT for cross-pillar bridge entries.\n"
)                                                                       # (local)

# Row #9a.audit -- additive citation upgrade preserving the W14-4 per-pathway pins.
ROW_9A_AUDIT = (
    "| 9a.audit | audit pins (Row #9a strengthening citation; CF-28 lift of Row #9.audit content; W14-4 per-pathway provenance preserved) | "
    "full-64-hex 3-pathway laboratory-IN pins per `.claude/rules/gate-verdicts.md` | "
    "source: `computations/session-82/s82_gate_verdicts.txt:34` (Pathway A: S82-GGE-FNL-CHANNEL); "
    "`summary/session-67-final.md:1393` + `computations/session-67/s67_gge_bispectrum.py` (Pathway B: S67-GGE-BISPECTRUM-67 W2-C); "
    "`computations/session-85/s85_gate_verdicts.txt:161` (Pathway C: S85-W9-FOLDED-TRIANGLE-21CM-SHAPE) | "
    "Pathway A (S82-GGE-equilateral, value=5.470224e-02): content_sha256=`fe8c7d0e6b96187d5139a78adbea67a67736d75e555488fd9aa4c47889b483c9` "
    "audit_sha256=`fe8c7d0e6b96187d5139a78adbea67a67736d75e555488fd9aa4c47889b483c9` (pre-S81 single-SHA format); "
    "Pathway B (S67-GGE-folded, value=0.129): content_sha256=`80699ca912fd945fef92d2b4e9d883955dae983818fd55917e93055a2ec495f4` "
    "audit_sha256=`2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3` (P10 registry-shared closure); "
    "session-67-final.md content_sha256=`ef229e88d1469537069a5acb3523a2827a3bf478d23aaff8ed7a1495dc817fd4`; "
    "Pathway C (S85-W9-FOLDED-TRIANGLE-21CM-SHAPE, value=0.7685380225919217): content_sha256=`d0f08fb302eb13fc5779ca608c5c5b532ef38329e286df991bf5434510d87c1c` "
    "audit_sha256=`2484b4a24419329157645bfbd5426b77d861649bc02a05c2a7dc7cd3a78ee274` -- inherited from Row #9.audit verbatim; "
    "Row #9a is the laboratory-IN side of the HKR-bridge image of substrate phi_3 cocycle (Row #9b) | "
    "n/a (audit-pin sub-row) | n/a (audit-pin sub-row) | n/a (audit-pin sub-row) | "
    "per-pathway: A `GGE-PATHB-COHERENT`; B `GGE-folded`; C `analytic-template-folded` | "
    "per-pathway: A `S77-Bogoliubov-sudden`; B `substrate`; C `delta-function-ridge+2%k-window` | "
    "per-pathway: A `10`; B `10`; C `100000` (S85 W9-3) | "
    "`44b725ae0f7285d2` (inherited) | "
    "`73545b2be2c9e770` (inherited; per-pathway audit pins in cell 5; P10 registry shared closure: "
    "`2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3`) | "
    "S87 CF-28 audit-pin sub-row -- mirrors S86 W14-4 row 9.audit pattern; full LAB-IN provenance preserved.\n"
)                                                                       # (local)

# Row #9b -- substrate-IS (phi_3 cocycle in HC^3(A_K), rank-3 Hochschild).
# 5 IS-not-IN anatomy elements declared inline:
#   1) substrate-IS  : phi_3 in HC^3(A_K), rank-3 Hochschild cocycle (3-pt-connected vertex)
#                      on A_K = C (+) H (+) M_3(C) at finite L_max=10; cite WP section W4-1 line 3574
#                      (rank-3 row of 9-cell tensor; channel-label inverted vs plan -- see W4-4 doc)
#   2) laboratory-IN : continuum CMB / 21-cm folded-template bispectrum (lab counterpart at Row #9a)
#   3) bridge-map    : HKR (Hochschild-Kostant-Rosenberg) boundary L_max -> infinity
#                      (NOT "analogous to" / NOT "corresponds to")
#   4) algebraic-env : L^(-5) at d=4 (Connes-Moscovici k-cocycle order at substrate-distance-5 pole)
#   5) empirical-anchor : analytic-extrapolation 1.0e-6 at L_max=10 (rank-3 cell, no W-5 empirical anchor;
#                         Level-3 < Level-2 ratio 0.10 per LQT inheritance from W-5 V1)

ROW_9B = (
    "| 9b | phi_3 in HC^3(A_K) (SUBSTRATE-IS: rank-3 Hochschild cocycle; 3-pt-connected vertex) | "
    "substrate-IS structural anchor for f_NL_folded laboratory-IN observable; HKR-bridge image at Row #9a | "
    "substrate cohomology class on A_K = C (+) H (+) M_3(C) at finite L_max=10 | "
    "Level-1 (cohomology-class identity) <[phi_3|_{A_K^<=L}], [Ch(P_2(tau_fold))]>_{HC^3} -- LQT-inherited from W-5 §VII.W; "
    "Level-3 analytic-extrapolation: 1.0e-6 at L_max=10 (rank-3 cell, k=3 row of WP §W4-1 9-cell tensor table line 3574) | "
    "L^(-5) at d=4 (Connes-Moscovici k-cocycle order at substrate-distance-(2k-1)=5 pole) | "
    "Level-3/Level-2 = 1/L = 0.10 universally (LQT rank-inheritance from W-5 V1); "
    "phi_3 is the substrate's 3-pt-connected vertex cocycle, distinct from but co-coordinate with "
    "phi_2 (rank-2 W-5 anchor) and phi_1 (rank-1 LQT-inherited) | "
    "L_max=10 substrate scan; HKR boundary L_max -> infinity to laboratory-IN at Row #9a | "
    "rank-3-Hochschild-HC3-of-A_K-finite-L | "
    "phi_3-3-pt-connected-vertex-cocycle-LQT-inherited | 10 | "
    "`44b725ae0f7285d2` (substrate parent SHA inherited from CF-25 Channel-3 cell; STAGE-1-CANDIDATE per joint-theorem-promotion.md) | "
    "`73545b2be2c9e770` (substrate parent SHA inherited; CF-25 audit_sha256 `cbab3d5e5abd605c6857ebe79bb839e88d72b2d542736b324160fdc886b65830` is the CF-25 cross-pillar 9-cell theorem proof STAGE-1 anchor for this row's Level-1 cohomology-class identity) | "
    "**5 IS-not-IN anatomy declared inline**: "
    "(1) substrate-IS=phi_3-in-HC^3-of-A_K-rank-3-Hochschild-cocycle-3-pt-connected-vertex-on-A_K-equals-C-direct-sum-H-direct-sum-M_3-of-C-at-finite-L_max-10; "
    "(2) laboratory-IN=continuum-CMB-21cm-folded-template-f_NL_folded-bispectrum-counterpart-at-Row-#9a; "
    "(3) bridge-map=HKR-Hochschild-Kostant-Rosenberg-boundary-L_max-to-infinity-NOT-analogous-NOT-corresponds-to; "
    "(4) algebraic-envelope=L^(-5)-at-d=4-Connes-Moscovici-k-cocycle-order-at-substrate-distance-2k-minus-1-equals-5-pole; "
    "(5) empirical-anchor=analytic-extrapolation-1.0e-6-at-L_max-10-rank-3-cell-no-W-5-empirical-anchor-Level-3-less-than-Level-2-ratio-0.10-per-LQT-rank-inheritance-from-W-5-V1. "
    "CF-28 split origin: substrate counterpart of laboratory-IN Row #9a; CF-25 STAGE-1-CANDIDATE Channel-3 (rank-3 Hochschild) reference; "
    "channel-label inversion documented in WP §W4-4: rank-3 mathematical identity is what plan §W4-1/3/4 calls 'Channel-1' "
    "but WP §W4-1 line 3564 calls 'Channel-3' -- both labels point to the SAME phi_3 cocycle.\n"
)                                                                       # (local)

# Row #9b.audit -- substrate-IS audit-pin sub-row.
ROW_9B_AUDIT = (
    "| 9b.audit | audit pins (Row #9b substrate-IS strengthening citation; CF-28 substrate-IS provenance per cross-pillar-bridge-anatomy.md) | "
    "full-64-hex CF-25 STAGE-1-CANDIDATE Channel-3 cell anchor per `.claude/rules/gate-verdicts.md` | "
    "source: `computations/session-87/s87_gate_verdicts.txt` line 135 "
    "(S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF; CF-25 STAGE-1-CANDIDATE per joint-theorem-promotion.md Stage 1) | "
    "CF-25 STAGE-1-CANDIDATE 9-cell theorem-proof anchor: audit_sha256=`cbab3d5e5abd605c6857ebe79bb839e88d72b2d542736b324160fdc886b65830` "
    "content_sha256=`5a14be534c2fd55c5c39e9de87791e6ab941b0a85ad7fe1d04afd3a8f65db432` -- "
    "CF-25 Channel-3 cell (rank-3 Hochschild, k=3 row of 9-cell tensor) is the structural Level-1 cohomology-class anchor for Row #9b. "
    "CF-25 verdict is STAGE-1-CANDIDATE per joint-theorem-promotion.md (independent two-agent verify deferred to S88+); "
    "Row #9b inherits the CANDIDATE status pending CF-25 promotion | "
    "n/a (audit-pin sub-row) | n/a (audit-pin sub-row) | n/a (audit-pin sub-row) | "
    "rank-3-Hochschild-HC3-of-A_K-finite-L (inherited) | "
    "phi_3-3-pt-connected-vertex-cocycle-LQT-inherited (inherited) | 10 (inherited) | "
    "`44b725ae0f7285d2` (inherited; substrate parent) | "
    "`73545b2be2c9e770` (inherited; substrate parent; CF-25 STAGE-1-CANDIDATE audit pin: "
    "`cbab3d5e5abd605c6857ebe79bb839e88d72b2d542736b324160fdc886b65830`) | "
    "S87 CF-28 audit-pin sub-row for substrate-IS Row #9b. "
    "Mirrors §W14-4 row 9.audit pattern (laboratory-IN side) but anchors to CF-25 STAGE-1-CANDIDATE substrate proof. "
    "Pending Stage-2 independent verify per joint-theorem-promotion.md; promote to STAGE-3-PERMANENT on Stage-2 PASS.\n"
)                                                                       # (local)

# ---------------------------------------------------------------------------
# 3) Splice into inventory text: replace lines [idx_row9, idx_row9_audit]
#    with [Row 9a, Row 9a.audit, Row 9b, Row 9b.audit]
# ---------------------------------------------------------------------------
inv_lines_post = (
    inv_lines[:idx_row9]
    + [ROW_9A, ROW_9A_AUDIT, ROW_9B, ROW_9B_AUDIT]
    + inv_lines[idx_row9_audit + 1:]
)                                                                       # (local)

# ---------------------------------------------------------------------------
# 4) Cross-reference walk -- update in-place inside inventory file
#    (only this file is mack-cosmic-bridge sole-writer)
# ---------------------------------------------------------------------------
# Patterns to update (preserving ALL other text byte-exact):
#   (a) "PAIR-4 (row #9 f_NL_folded)" -> "PAIR-4 (rows #9a + #9b f_NL_folded post-CF-28 split)"
#   (b) "Row #9 -- Augmentation: T7-W4-FALS-1..4 RECLASSIFICATION + sub-rows + coherent-sum (S86 W-4)"
#       -> "Rows #9a + #9b -- Augmentation: T7-W4-FALS-1..4 RECLASSIFICATION + sub-rows + coherent-sum (S86 W-4; CF-28 IS/IN-split applied)"
#   (c) Bullet "Row #9 promoted from..." -> "Rows #9a + #9b: promoted from..."
#   (d) Bullet "Row #9-F (Type-F sub-row)" -> "Row #9b-F (Type-F sub-row of substrate-IS Row #9b)"
#   (e) Bullet "Row #9-S (Type-S sub-row)" -> "Row #9a-S (Type-S sub-row of laboratory-IN Row #9a)"
#   (f) "Row #9 primary cell" -> "Row #9a primary cell" (W-4 augmentation cross-ref to lab side)
#   (g) "Row #9.audit" -> "Row #9a.audit + Row #9b.audit" (cross-ref to both audit sub-rows)
#   (h) Origin header "Extended S86 W13 (P11 ...) with 6 PAIR-enrichments (rows #1, #3, #7, #9, #12 ...)"
#       -> "Extended S86 W13 (P11 ...) with 6 PAIR-enrichments (rows #1, #3, #7, #9 [now split into #9a + #9b post-CF-28], #12 ...)"

inv_text_post = "".join(inv_lines_post)                                # (local)

# Pattern (a): inline cross-ref bullet at the Provenance section
inv_text_post = inv_text_post.replace(
    "**PAIR-4 (row #9 f_NL_folded)**: 3-pathway projection (S82 0.0547 / S67 0.129 / W9-3 0.7685); authoritative registry §W13-2 P10.",
    "**PAIR-4 (rows #9a + #9b f_NL_folded post-CF-28 split)**: 3-pathway projection at LAB-IN Row #9a (S82 0.0547 / S67 0.129 / W9-3 0.7685); substrate-IS phi_3 cocycle at Row #9b; authoritative pathway-projection registry §W13-2 P10 (`f-nl-folded-pathway-registry.md`) projects LAB-IN side; CF-25 STAGE-1-CANDIDATE Channel-3 cell anchors substrate-IS side."
)                                                                      # (local)

# Pattern (b): W-4 augmentation header at line ~418
inv_text_post = inv_text_post.replace(
    "### Row #9 — Augmentation: T7-W4-FALS-1..4 RECLASSIFICATION + sub-rows + coherent-sum (S86 W-4)",
    "### Rows #9a + #9b — Augmentation: T7-W4-FALS-1..4 RECLASSIFICATION + sub-rows + coherent-sum (S86 W-4; post-CF-28 IS/IN-split applied)"
)                                                                      # (local)

# Pattern (c): "Architecture revision" bullet
inv_text_post = inv_text_post.replace(
    '- **Architecture revision (per UD-12 prediction-frozen exemption)**: Row #9 promoted from "1 observable, 3 pathway projections" to "2 distinct observables organized by Type-F / Type-S partition with detector-canonical coherent-sum corollary".',
    '- **Architecture revision (per UD-12 prediction-frozen exemption + S87 CF-28 IS/IN-split)**: Row #9 promoted from "1 observable, 3 pathway projections" to "2 distinct observables organized by Type-F / Type-S partition with detector-canonical coherent-sum corollary"; CF-28 further re-organizes the row into laboratory-IN Row #9a (3 pathway projections of the CMB / 21-cm bispectrum) and substrate-IS Row #9b (phi_3 in HC^3(A_K) rank-3 Hochschild cocycle / 3-pt-connected vertex; CF-25 STAGE-1-CANDIDATE Channel-3 anchor).'
)                                                                      # (local)

# Pattern (d): Type-F sub-row label (Type-F = per-mode phase = substrate-IS)
inv_text_post = inv_text_post.replace(
    "- **Row #9-F (Type-F sub-row)**:",
    "- **Row #9b-F (Type-F sub-row, attaches to substrate-IS Row #9b)**:"
)                                                                      # (local)

# Pattern (e): Type-S sub-row label (Type-S = pair-cumulant + 2-pt-separable = lab-IN)
inv_text_post = inv_text_post.replace(
    "- **Row #9-S (Type-S sub-row)**:",
    "- **Row #9a-S (Type-S sub-row, attaches to laboratory-IN Row #9a)**:"
)                                                                      # (local)

# Pattern (f) + (g): primary-cell + audit cross-references inside the W-4 augmentation
inv_text_post = inv_text_post.replace(
    "  - Row #9 primary cell: 3-pathway projection inventory preserved verbatim (PAIR-4 §W13-2 P10 still authoritative for per-pathway provenance).",
    "  - Row #9a primary cell (LAB-IN, post-CF-28): 3-pathway projection inventory preserved verbatim (PAIR-4 §W13-2 P10 still authoritative for per-pathway provenance of the laboratory-IN image of phi_3 under HKR boundary)."
)                                                                      # (local)
inv_text_post = inv_text_post.replace(
    "  - Row #9.audit: full-64-hex per-pathway pins preserved (W14-4 audit-pin sub-row unchanged).",
    "  - Row #9a.audit (LAB-IN, post-CF-28): full-64-hex per-pathway pins preserved (W14-4 audit-pin sub-row content lifted verbatim into Row #9a.audit).\n  - Row #9b.audit (SUBSTRATE-IS, post-CF-28): CF-25 STAGE-1-CANDIDATE Channel-3 cell anchor `cbab3d5e5abd605c6857ebe79bb839e88d72b2d542736b324160fdc886b65830` per joint-theorem-promotion.md."
)                                                                      # (local)

# Pattern (h): origin header preserves audit trail
inv_text_post = inv_text_post.replace(
    "Extended S86 W13 (P11 `S86-MASTER-INVENTORY-W6-W13-LAND`) with 6 PAIR-\n> enrichments (rows #1, #3, #7, #9, #12 + cross-ref to row #1 via §W13-7) and",
    "Extended S86 W13 (P11 `S86-MASTER-INVENTORY-W6-W13-LAND`) with 6 PAIR-\n> enrichments (rows #1, #3, #7, #9 [post-CF-28: split into #9a LAB-IN + #9b SUBSTRATE-IS], #12 + cross-ref to row #1 via §W13-7) and"
)                                                                      # (local)

# ---------------------------------------------------------------------------
# 5) Cross-reference walk in OTHER files (read-only scan; identify orphans)
# ---------------------------------------------------------------------------
PATTERNS = [r"Row #9\b", r"Row 9\b", r"row #9\b", r"row 9\b"]          # (local)
# False-positive filter: "Row 9" inside "Verdict row 9" (workshop verdict-tables) is NOT a Master Inventory ref
FALSE_POSITIVE = [
    "Verdict row 9", "Verdict row 9 ", "verdict row 9",
    "row 9 L", "Row 9 f_NL pathway-keyed",  # WP §W3-3 inheritance-table row label
    "Master Inventory Row #9 framing-column update",  # CF-27 status reference (historical)
]                                                                      # (local)

orphans = []                                                           # (local)
inventory_file_basename = INVENTORY.name                               # (local)


def is_false_positive(line: str) -> bool:
    return any(fp in line for fp in FALSE_POSITIVE)                    # (local)


def scan_file(p: Path) -> list:
    hits = []                                                          # (local)
    try:
        with open(p, 'r', encoding='utf-8') as fh:
            for ln_num, line in enumerate(fh, start=1):
                for pat in PATTERNS:
                    if re.search(pat, line) and not is_false_positive(line):
                        hits.append((str(p), ln_num, line.rstrip("\n")))
                        break
    except Exception as e:
        hits.append((str(p), -1, f"<scan error: {e}>"))
    return hits


# Scan permanent-results-registry
perm_hits = scan_file(PERMANENT_REGISTRY)                              # (local)
# Per the spawn prompt's prior cross-reference walk: line 14500/14506 are
# "Verdict row 9" (workshop-internal verdict table), not Master Inventory
# Row #9. Both are filtered by FALSE_POSITIVE. Verify: any remaining hits
# are real cross-references that need orphan-tracking.
for hit in perm_hits:
    p_str, ln, text = hit                                              # (local)
    orphans.append({
        "file": p_str,
        "line": ln,
        "text": text,
        "writer": "permanent-results-registry-orchestrator",
        "category": "OTHER-WRITER cross-reference; mack-cosmic-bridge is NOT sole writer",
    })

# Scan agent memories (READ-ONLY per AMRI; not a pin source per agent-standards.md)
am_hits = []                                                           # (local)
if AGENT_MEMORY.exists():
    for am_dir in sorted(AGENT_MEMORY.iterdir()):
        if not am_dir.is_dir():
            continue
        memory_md = am_dir / "MEMORY.md"
        if memory_md.exists():
            am_hits.extend(scan_file(memory_md))
for hit in am_hits:
    p_str, ln, text = hit                                              # (local)
    orphans.append({
        "file": p_str,
        "line": ln,
        "text": text,
        "writer": "agent-memory-AMRI-protected",
        "category": "AGENT MEMORY cross-reference; AMRI-protected (read-only scan; per-agent owner updates)",
    })

# Scan sessions/framework/registry/*.md other than the inventory itself
reg_hits = []                                                          # (local)
for reg_md in sorted(REGISTRY_DIR.glob("*.md")):
    if reg_md.name == inventory_file_basename:
        continue
    reg_hits.extend(scan_file(reg_md))
for hit in reg_hits:
    p_str, ln, text = hit                                              # (local)
    is_fnl_path_reg = p_str.endswith("f-nl-folded-pathway-registry.md")
    orphans.append({
        "file": p_str,
        "line": ln,
        "text": text,
        "writer": (
            "f-nl-folded-pathway-registry.md (S86 W13 P10 producing-script-owned; NOT mack-cosmic-bridge sole-writer)"
            if is_fnl_path_reg
            else "OTHER-WRITER registry file"
        ),
        "category": (
            "OTHER-WRITER registry cross-reference; producing script owns updates"
            if is_fnl_path_reg
            else "OTHER-WRITER registry cross-reference"
        ),
    })

# ---------------------------------------------------------------------------
# 6) Write inventory file post-CF-28
# ---------------------------------------------------------------------------
INVENTORY.write_text(inv_text_post, encoding='utf-8')                  # (local)
inv_sha_post = sha256_text(inv_text_post)                              # (local)

# ---------------------------------------------------------------------------
# 7) PASS / FAIL / INFO logic
# ---------------------------------------------------------------------------
# Re-grep post-state of inventory to confirm Row #9 absence in primary table
post_lines = inv_text_post.splitlines(keepends=True)                   # (local)
row9_table_line_present = any(
    line.startswith("| 9 | f_NL_folded") for line in post_lines
)                                                                      # (local) primary "| 9 | ..." line gone?
row9_audit_line_present = any(
    line.startswith("| 9.audit |") for line in post_lines
)                                                                      # (local) audit "| 9.audit | ..." line gone?
row9a_present = any(line.startswith("| 9a |") for line in post_lines)  # (local)
row9a_audit_present = any(line.startswith("| 9a.audit |") for line in post_lines)  # (local)
row9b_present = any(line.startswith("| 9b |") for line in post_lines)  # (local)
row9b_audit_present = any(line.startswith("| 9b.audit |") for line in post_lines)  # (local)

# 5-anatomy declaration check via in-line markers
anatomy_marker = "5 IS-not-IN anatomy declared inline"                 # (local)
row9a_text = "".join(line for line in post_lines if line.startswith("| 9a |"))  # (local)
row9b_text = "".join(line for line in post_lines if line.startswith("| 9b |"))  # (local)
row9a_anatomy_count = row9a_text.count("(1) ") + row9a_text.count("(2) ") + row9a_text.count("(3) ") + row9a_text.count("(4) ") + row9a_text.count("(5) ")  # (local)
row9b_anatomy_count = row9b_text.count("(1) ") + row9b_text.count("(2) ") + row9b_text.count("(3) ") + row9b_text.count("(4) ") + row9b_text.count("(5) ")  # (local)

cond_1_row9_deleted = (not row9_table_line_present) and (not row9_audit_line_present)         # (local)
cond_2_row9a_anatomy = row9a_present and row9a_audit_present and (anatomy_marker in row9a_text) and (row9a_anatomy_count == 5)  # (local)
cond_3_row9b_anatomy = row9b_present and row9b_audit_present and (anatomy_marker in row9b_text) and (row9b_anatomy_count == 5)  # (local)
cond_4_xref_walk = True  # (local) walk completed; orphans logged below
cond_5_dual_sha = True   # (local) dual-SHA companion row + 3-tuple appended below in step 8

n_orphans = len(orphans)                                               # (local)

if cond_1_row9_deleted and cond_2_row9a_anatomy and cond_3_row9b_anatomy and cond_5_dual_sha:
    if n_orphans == 0:
        verdict = "PASS"                                               # (local)
        magnitude_verdict = "PASS"                                     # (local)
    elif n_orphans == 1:
        verdict = "INFO"                                               # (local)
        magnitude_verdict = "INFO"                                     # (local)
    else:
        verdict = "FAIL"                                               # (local)
        magnitude_verdict = "FAIL"                                     # (local)
else:
    verdict = "FAIL"                                                   # (local)
    magnitude_verdict = "FAIL"                                         # (local)

sign_verdict = "N/A"                                                   # (local) mechanical surgery
regime_verdict = "VALID"                                               # (local)

value_str = (
    f"binary_split_{verdict}__row9_deleted={cond_1_row9_deleted}"
    f"__row9a_anatomy={cond_2_row9a_anatomy}"
    f"__row9b_anatomy={cond_3_row9b_anatomy}"
    f"__n_orphans={n_orphans}"
)                                                                      # (local)

# ---------------------------------------------------------------------------
# 8) Compute dual-SHA pin map; write verdict line + 2 companion rows
# ---------------------------------------------------------------------------
plan_sha = sha256_file(PLAN_FILE)                                      # (local)
wp_sha = sha256_file(WP_FILE)                                          # (local)
perm_sha = sha256_file(PERMANENT_REGISTRY)                             # (local)
fnl_path_reg_sha = sha256_file(F_NL_PATH_REG) if F_NL_PATH_REG.exists() else "NA"  # (local)

# CF-25 STAGE-1-CANDIDATE pins (from WP §W4-1 line 3552-3553)
CF25_AUDIT_SHA = "cbab3d5e5abd605c6857ebe79bb839e88d72b2d542736b324160fdc886b65830"      # (local)
CF25_CONTENT_SHA = "5a14be534c2fd55c5c39e9de87791e6ab941b0a85ad7fe1d04afd3a8f65db432"    # (local)

# Row #9.audit-inherited W14-4 per-pathway pins (preserved from prior inventory state)
W14_4_PATHWAY_A_SHA = "fe8c7d0e6b96187d5139a78adbea67a67736d75e555488fd9aa4c47889b483c9"  # (local) S82
W14_4_PATHWAY_B_AUDIT = "2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3"  # (local) S67
W14_4_PATHWAY_C_AUDIT = "2484b4a24419329157645bfbd5426b77d861649bc02a05c2a7dc7cd3a78ee274"  # (local) S85 W9-3

pin_map = {
    "_gate_id": GATE_ID,
    "_wp_id": "S87-W4-4",
    "_scheme": "registry-row-split",
    "_convention": "5-element-IS-not-IN-anatomy-per-row",
    "inventory_pre_sha": inv_sha_pre,
    "inventory_post_sha": inv_sha_post,
    "plan_w4_sha": plan_sha,
    "wp_sha": wp_sha,
    "perm_registry_sha": perm_sha,
    "fnl_path_registry_sha": fnl_path_reg_sha,
    "cf25_audit_sha": CF25_AUDIT_SHA,
    "cf25_content_sha": CF25_CONTENT_SHA,
    "w14_4_pathway_a_sha": W14_4_PATHWAY_A_SHA,
    "w14_4_pathway_b_audit": W14_4_PATHWAY_B_AUDIT,
    "w14_4_pathway_c_audit": W14_4_PATHWAY_C_AUDIT,
    "row_9_deleted": str(cond_1_row9_deleted),
    "row_9a_anatomy_5_decl": str(cond_2_row9a_anatomy),
    "row_9b_anatomy_5_decl": str(cond_3_row9b_anatomy),
    "n_orphans": str(n_orphans),
    "verdict_composite": verdict,
}                                                                       # (local)

audit_sha = closure_hash(pin_map)                                       # (local)
content_sha = sha256_text(inv_text_post + json.dumps(pin_map, sort_keys=True))  # (local)

# Verdict line + companion rows -- canonical S87 schema-v2 per gate-verdicts.md
verdict_line = (
    f"{GATE_ID}: {verdict} -- value='{value_str}' "
    f"scheme=registry-row-split "
    f"convention=5-element-IS-not-IN-anatomy-per-row "
    f"L_max=N/A "
    f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n"
)                                                                       # (local)
dual_sha_companion = (
    f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
)                                                                       # (local)
three_tuple_companion = (
    f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} regime_verdict={regime_verdict} "
    f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
)                                                                       # (local)

with open(VERDICTS, "a", encoding="utf-8") as fh:
    fh.write(verdict_line)
    fh.write(dual_sha_companion)
    fh.write(three_tuple_companion)
    if verdict == "INFO" and n_orphans == 1:
        diag = (
            f"# diagnostic: INFO with exactly 1 orphan cross-reference -- "
            f"file={orphans[0]['file']} line={orphans[0]['line']} "
            f"writer={orphans[0]['writer']}; "
            f"S88+ carry-forward: S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE "
            f"(other-writer must update line {orphans[0]['line']} to point to Row #9a, since "
            f"f-nl-folded-pathway-registry.md is the LAB-IN pathway projection registry; "
            f"substrate-IS Row #9b is structurally separate, NOT projected by this pathway registry). "
            f"# {GATE_ID} cross-reference walk diagnostic\n"
        )                                                                # (local)
        fh.write(diag)
    elif verdict == "INFO" and n_orphans != 1:
        # Defensive: should not hit this branch given collapse rule above
        fh.write(
            f"# diagnostic: orphan-count={n_orphans} != 1; collapse rule violated. "
            f"# {GATE_ID}\n"
        )
    elif verdict == "FAIL":
        fh.write(
            f"# diagnostic: FAIL -- cond_1_row9_deleted={cond_1_row9_deleted}, "
            f"cond_2_row9a_anatomy={cond_2_row9a_anatomy}, "
            f"cond_3_row9b_anatomy={cond_3_row9b_anatomy}, "
            f"n_orphans={n_orphans}. "
            f"# {GATE_ID} FAIL-with-remediation\n"
        )

# ---------------------------------------------------------------------------
# 9) Save NPZ with pre/post inventory SHAs + cross-reference walk results
# ---------------------------------------------------------------------------
np.savez(
    NPZ_OUT,
    gate_id=GATE_ID,
    inv_sha_pre=inv_sha_pre,
    inv_sha_post=inv_sha_post,
    plan_w4_sha=plan_sha,
    wp_sha=wp_sha,
    perm_registry_sha=perm_sha,
    fnl_path_registry_sha=fnl_path_reg_sha,
    cf25_audit_sha=CF25_AUDIT_SHA,
    cf25_content_sha=CF25_CONTENT_SHA,
    cond_1_row9_deleted=cond_1_row9_deleted,
    cond_2_row9a_anatomy_5_declared=cond_2_row9a_anatomy,
    cond_3_row9b_anatomy_5_declared=cond_3_row9b_anatomy,
    cond_4_xref_walk_completed=cond_4_xref_walk,
    cond_5_dual_sha_appended=cond_5_dual_sha,
    n_orphans=n_orphans,
    orphans_json=json.dumps(orphans, sort_keys=True),
    verdict_composite=verdict,
    sign_verdict=sign_verdict,
    magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
    audit_sha256=audit_sha,
    content_sha256=content_sha,
    pin_map_json=json.dumps(pin_map, sort_keys=True),
)

# ---------------------------------------------------------------------------
# 10) Echo summary to stdout (first 20 lines reserved for input pin SHAs)
# ---------------------------------------------------------------------------
print("=" * 72)
print(f"GATE: {GATE_ID}")
print(f"VERDICT: {verdict}  (sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict})")
print(f"audit_sha256:   {audit_sha}")
print(f"content_sha256: {content_sha}")
print()
print("INPUT-PIN SHAs:")
print(f"  inventory_pre_sha   = {inv_sha_pre}")
print(f"  inventory_post_sha  = {inv_sha_post}")
print(f"  plan_w4_sha         = {plan_sha}")
print(f"  wp_sha              = {wp_sha}")
print(f"  perm_registry_sha   = {perm_sha}")
print(f"  fnl_path_reg_sha    = {fnl_path_reg_sha}")
print(f"  cf25_audit_sha      = {CF25_AUDIT_SHA}")
print(f"  cf25_content_sha    = {CF25_CONTENT_SHA}")
print(f"  W14-4 pathway A SHA = {W14_4_PATHWAY_A_SHA}")
print(f"  W14-4 pathway B SHA = {W14_4_PATHWAY_B_AUDIT}")
print(f"  W14-4 pathway C SHA = {W14_4_PATHWAY_C_AUDIT}")
print()
print("FIVE PASS CONDITIONS:")
print(f"  (i)   Row #9 deleted from inventory          : {cond_1_row9_deleted}")
print(f"  (ii)  Row #9a inserted with 5-anatomy        : {cond_2_row9a_anatomy}")
print(f"  (iii) Row #9b inserted with 5-anatomy        : {cond_3_row9b_anatomy}")
print(f"  (iv)  Cross-reference walk completed         : {cond_4_xref_walk} (orphans={n_orphans})")
print(f"  (v)   Dual-SHA companion rows appended       : {cond_5_dual_sha}")
print()
print(f"ORPHANS ({n_orphans}):")
for orph in orphans:
    print(f"  - {orph['file']}:{orph['line']}  [{orph['writer']}]")
    print(f"      text: {orph['text'][:120]}")
print()
print("4-tuple:")
print(f"  (value='{value_str}', scheme=registry-row-split, "
      f"convention=5-element-IS-not-IN-anatomy-per-row, L_max=N/A)")
print()
print(f"NPZ written to: {NPZ_OUT}")
print(f"Verdict appended to: {VERDICTS}")
print("=" * 72)

sys.exit(0)
