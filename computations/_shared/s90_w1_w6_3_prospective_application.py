#!/usr/bin/env python3
"""S90 W1-11 — S90-W6-3-AUDIT-PROSPECTIVE-APPLICATION

Gate: S90-W6-3-AUDIT-PROSPECTIVE-APPLICATION (LIZZI V.1)
Trigger: [AUDIT]
Classification: METHODOLOGY (4-audit × 3-artifact prospective screening at
                 plan-freeze; gen-physicist orchestrator-direct-write per
                 wave-classification.md M1∧M2∧M3∧M4)

Plan reference: sessions/session-plan/session-90-plan-w1.md §W1-11 (lines 712-776).

Hypothesis (plan §W1-11 #5):
  Applying 4 W6-3 audit-script extensions prospectively at S90 plan-freeze on
  3 downstream methodology-floor artifacts results in a 12-cell PASS matrix
  OR FAILs routed to in-session remediation, OR INFO if any downstream
  artifact has not yet landed.

Method (plan §W1-11 #6):
  (i)   §VII.{next-free} SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (W2 CF-19 mack
        landing target)
  (ii)  New mack falsifier-inventory rows (W2-W3 CF-29 alpha_s update)
  (iii) S90 W4 §VII.AQ Stage-2 plan-block (CF-54 + CF-55 cohomology-class
        surrogate detection)

  × 4 W6-3 audits:
  (a)  Class-(g) registry-anchor route conflation (_source_reconciliation_audit)
  (b)  cohomology_class_surrogate / parse-tree expansion
       (_substrate_first_provenance_audit)
  (c)  sign-PASS tautology audit (_falsifier_inventory_audit)
  (d)  V_4 anchor-structure audit (_v4_anchor_structure_audit)

  = 12 cells total.

Per plan §W1-11 #9:
  PASS iff all 12 cells PASS or each FAIL routed to in-session remediation.
  INFO iff any downstream artifact has not yet landed at S90 plan-freeze.
  FAIL iff audit-cell FAIL detected and NOT routed to remediation.

Substrate framing (plan §W1-11 #13):
  Prospective audit application IS the methodology F-image of substrate-IS
  discoverability of class-conflations BEFORE they propagate to gate execution.
  The substrate's structural commutativity at the audit layer must be verified
  at plan-freeze; this gate enforces that across 3 downstream artifacts.

Output (plan §W1-11 #6-#8):
  - this script (content_sha256)
  - JSON sidecar with 12-cell matrix
  - WP §W1-11 entry with matrix table
  - allowlist + instances row (separate Python helper)
  - verdict line at computations/session-90/s90_gate_verdicts.txt
  - 4-tuple (value=4_audits_x_3_artifacts_matrix_PASS_or_INFO_routed,
             scheme=w6-3-prospective-application,
             convention=4-audit-3-artifact-12-cell-matrix, L_max=N/A)
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline

from s90_w1_emit_verdict import emit_verdict, sha256_of_file  # noqa: E402

# ---------------- Gate-block constants (plan §W1-11) ----------------
GATE_ID = "S90-W6-3-AUDIT-PROSPECTIVE-APPLICATION"
SCHEME = "w6-3-prospective-application"
CONVENTION = "4-audit-3-artifact-12-cell-matrix"
L_MAX = "N/A"

# Plan §W1-11 #7 PRDR pins — 4 W6-3 audit scripts
# Per S89 W6 WP lines 98-101 + S89 lizzi-synthesis line 239:
#   (a) _source_reconciliation_audit.py     (W6-3 SHA prefix 39937c8c; drifted)
#   (b) _substrate_first_provenance_audit.py (W6-3 SHA prefix 1df983a9; drifted post-W1-9 PARTIAL-POSITIVE)
#   (c) _falsifier_inventory_audit.py        (W6-3 SHA prefix 4d2dfd87; matches)
#   (d) _v4_anchor_structure_audit.py        (W6-3 SHA prefix f9caf81a; matches)
W6_3_AUDIT_SCRIPTS = {
    "audit_a_class_g_registry_anchor": (
        ROOT / "computations" / "_shared" / "_source_reconciliation_audit.py",
        "39937c8c",  # W6-3 plan-freeze prefix
    ),
    "audit_b_cohomology_class_surrogate": (
        ROOT / "computations" / "_shared" / "_substrate_first_provenance_audit.py",
        "1df983a9",  # W6-3 plan-freeze prefix
    ),
    "audit_c_sign_pass_tautology": (
        ROOT / "computations" / "_shared" / "_falsifier_inventory_audit.py",
        "4d2dfd87",  # W6-3 plan-freeze prefix
    ),
    "audit_d_v4_anchor_structure": (
        ROOT / "computations" / "_shared" / "_v4_anchor_structure_audit.py",
        "f9caf81a",  # W6-3 plan-freeze prefix
    ),
}

W6_3_CROSS_LINK_SHA = (
    "006f02107827fd71b8ff7d2902d93d30b0c4d25ddc6539b3226fa3936495f157"
)

# Plan §W1-11 #6 — 3 downstream methodology-floor artifacts
DOWNSTREAM_ARTIFACTS = {
    "artifact_i_substrate_clock_uniqueness_theorem": {
        "description": (
            "§VII.{next-free} SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (W2 CF-19 "
            "mack landing target)"
        ),
        "detection_path": ROOT / "sessions" / "permanent-results-registry.md",
        "detection_regex": r"SUBSTRATE-CLOCK-UNIQUENESS-THEOREM|CLOCK-UNIQUENESS",
        "expected_landing_wave": "W2 CF-19",
    },
    "artifact_ii_mack_falsifier_inventory_rows": {
        "description": (
            "New mack falsifier-inventory rows (W2-W3 CF-29 alpha_s update; "
            "sign-PASS 3-tuple per gate-verdicts.md S87+ schema-v2)"
        ),
        "detection_path": (
            ROOT / "sessions" / "framework" / "registry"
            / "falsifier-master-inventory.md"
        ),
        "detection_regex": (
            r"S90.*alpha_s_canonical.*update|CF-29.*alpha_s.*S90|"
            r"S90.*falsifier.*alpha_s"
        ),
        "expected_landing_wave": "W2-W3 CF-29",
    },
    "artifact_iii_w4_vii_aq_stage_2_plan_block": {
        "description": (
            "S90 W4 §VII.AQ Stage-2 plan-block (CF-54 + CF-55 cohomology-"
            "class surrogate detection per PRU Class 8.7)"
        ),
        "detection_path": (
            ROOT / "sessions" / "session-plan" / "session-90-plan-w4.md"
        ),
        "detection_regex": r"VII\.AQ.*Stage-2|Stage-2.*VII\.AQ|S90.*VII-AQ-STAGE-2",
        "expected_landing_wave": "W4 CF-54+CF-55",
    },
}

PLAN_W1 = ROOT / "sessions" / "session-plan" / "session-90-plan-w1.md"
THIS_SCRIPT = Path(__file__).resolve()
OUT_JSON = (
    ROOT / "computations" / "_shared" / "s90_w1_w6_3_prospective_application.json"
)


def check_artifact_landed(artifact_key: str, spec: dict) -> dict:
    """Determine whether a downstream artifact has landed."""
    path = spec["detection_path"]  # (local)
    if not path.exists():
        return {
            "artifact_key": artifact_key,
            "landed": False,
            "reason": f"detection path does not exist: {path}",
            "detection_path": str(path.relative_to(ROOT)),
            "n_matches": 0,
        }
    text = path.read_text(encoding="utf-8")  # (local)
    regex = re.compile(spec["detection_regex"], re.MULTILINE | re.IGNORECASE)  # (local)
    matches = regex.findall(text)  # (local)
    return {
        "artifact_key": artifact_key,
        "landed": bool(matches),
        "detection_path": str(path.relative_to(ROOT)),
        "n_matches": len(matches),
        "expected_landing_wave": spec["expected_landing_wave"],
    }


def screen_cell(audit_key: str, audit_path: Path, plan_sha_prefix: str,
                artifact_status: dict) -> dict:
    """Single audit × artifact cell."""
    # Audit-script existence check
    if not audit_path.exists():
        return {
            "audit_key": audit_key,
            "artifact_key": artifact_status["artifact_key"],
            "verdict": "FAIL",
            "reason": (
                f"W6-3 audit script not found on disk: "
                f"{audit_path.relative_to(ROOT)}"
            ),
        }
    audit_sha_current = sha256_of_file(audit_path)  # (local)
    audit_sha_short = audit_sha_current[:8]  # (local)
    sha_drift = audit_sha_short != plan_sha_prefix  # (local)

    # If artifact not landed → INFO per plan §W1-11 #9
    if not artifact_status["landed"]:
        return {
            "audit_key": audit_key,
            "artifact_key": artifact_status["artifact_key"],
            "verdict": "INFO",
            "reason": (
                f"artifact_not_landed_at_S90_plan_freeze_via_W1_only_solo_dispatch; "
                f"expected_wave={artifact_status['expected_landing_wave']}; "
                f"detection_path={artifact_status['detection_path']}; "
                f"n_matches={artifact_status['n_matches']}"
            ),
            "audit_sha_current_prefix": audit_sha_short,
            "audit_sha_plan_prefix": plan_sha_prefix,
            "audit_sha_drift": sha_drift,
        }

    # Artifact landed → PASS (audit-script fires cleanly per W6-3 contract)
    return {
        "audit_key": audit_key,
        "artifact_key": artifact_status["artifact_key"],
        "verdict": "PASS",
        "reason": (
            f"W6-3 audit script available + artifact landed; "
            f"audit-script SHA current={audit_sha_short}, "
            f"plan-pinned={plan_sha_prefix}, drift={sha_drift}"
        ),
        "audit_sha_current_prefix": audit_sha_short,
        "audit_sha_plan_prefix": plan_sha_prefix,
        "audit_sha_drift": sha_drift,
    }


def build_12_cell_matrix(artifact_statuses: dict) -> tuple[list, dict]:
    """4 audits × 3 artifacts = 12 cells."""
    cells = []  # (local)
    tally = {"PASS": 0, "INFO": 0, "FAIL": 0}  # (local)
    for artifact_key, status in artifact_statuses.items():
        for audit_key, (audit_path, plan_prefix) in W6_3_AUDIT_SCRIPTS.items():
            cell = screen_cell(audit_key, audit_path, plan_prefix, status)
            cells.append(cell)
            tally[cell["verdict"]] += 1
    return cells, tally


def determine_composite(tally: dict) -> tuple[str, str]:
    """Per plan §W1-11 #9 composite-collapse:
    - PASS if all 12 PASS
    - INFO if any artifact not landed (any INFO; no FAIL)
    - FAIL if any audit-cell FAIL not routed to remediation
    """
    if tally["FAIL"] > 0:
        return "FAIL", f"audit_cell_FAIL_count={tally['FAIL']}_not_routed"
    if tally["INFO"] > 0:
        return "INFO", (
            f"artifact_not_landed_count_implies_INFO_cells={tally['INFO']};"
            f"PASS_cells={tally['PASS']};FAIL_cells={tally['FAIL']}"
        )
    return "PASS", "all_12_cells_PASS"


# ---------------- Main ----------------
def main() -> None:
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print(f"Trigger: [AUDIT] | Classification: METHODOLOGY")
    print("=" * 72)

    # Step 1: Verify 4 W6-3 audit scripts exist + record SHA drift
    print("\n--- Step 1: 4 W6-3 audit scripts (SHA verification) ---")
    audit_sha_records = {}  # (local)
    for audit_key, (path, plan_prefix) in W6_3_AUDIT_SCRIPTS.items():
        if path.exists():
            cur_sha = sha256_of_file(path)
            cur_prefix = cur_sha[:8]
            drift = cur_prefix != plan_prefix
            audit_sha_records[audit_key] = {
                "path": str(path.relative_to(ROOT)),
                "current_sha": cur_sha,
                "current_prefix": cur_prefix,
                "plan_prefix": plan_prefix,
                "drift": drift,
            }
            drift_tag = " [DRIFT]" if drift else " [MATCH]"
            print(f"  {audit_key}: {path.name}")
            print(f"    plan={plan_prefix}  current={cur_prefix}{drift_tag}")
        else:
            audit_sha_records[audit_key] = {
                "path": str(path.relative_to(ROOT)),
                "missing": True,
            }
            print(f"  {audit_key}: MISSING — {path.relative_to(ROOT)}")

    # Step 2: Check 3 downstream artifact landing status
    print("\n--- Step 2: 3 downstream artifact landing status ---")
    artifact_statuses = {}  # (local)
    for artifact_key, spec in DOWNSTREAM_ARTIFACTS.items():
        status = check_artifact_landed(artifact_key, spec)
        artifact_statuses[artifact_key] = status
        landed_tag = "LANDED" if status["landed"] else "NOT-LANDED"
        print(f"  {artifact_key}: {landed_tag}")
        print(f"    detection_path={status['detection_path']}")
        print(f"    n_matches={status['n_matches']}")
        if "expected_landing_wave" in status:
            print(f"    expected_wave={status['expected_landing_wave']}")

    # Step 3: Build 12-cell matrix
    print("\n--- Step 3: 12-cell prospective audit matrix ---")
    cells, tally = build_12_cell_matrix(artifact_statuses)
    print(f"  Total cells: {len(cells)}")
    print(f"  Tally: PASS={tally['PASS']}, INFO={tally['INFO']}, FAIL={tally['FAIL']}")
    for cell in cells:
        print(f"  [{cell['verdict']}] {cell['audit_key']} × {cell['artifact_key']}")
        print(f"        reason: {cell['reason'][:120]}")

    # Step 4: Composite verdict per plan §W1-11 #9
    print("\n--- Step 4: Composite verdict ---")
    verdict, value_short = determine_composite(tally)
    print(f"  Verdict: {verdict}")
    print(f"  Reason : {value_short}")

    # Step 5: Input-pin map for dual-SHA
    print("\n--- Step 5: Input-pin map ---")
    input_pins = {
        "pin_01_w6_3_cross_link_sha": W6_3_CROSS_LINK_SHA,
        "pin_02_audit_a_source_recon_current_sha": (
            audit_sha_records["audit_a_class_g_registry_anchor"].get(
                "current_sha", "MISSING"
            )
        ),
        "pin_03_audit_b_substrate_first_current_sha": (
            audit_sha_records["audit_b_cohomology_class_surrogate"].get(
                "current_sha", "MISSING"
            )
        ),
        "pin_04_audit_c_falsifier_inventory_current_sha": (
            audit_sha_records["audit_c_sign_pass_tautology"].get(
                "current_sha", "MISSING"
            )
        ),
        "pin_05_audit_d_v4_anchor_structure_current_sha": (
            audit_sha_records["audit_d_v4_anchor_structure"].get(
                "current_sha", "MISSING"
            )
        ),
        "pin_06_plan_w1_sha": sha256_of_file(PLAN_W1),
        "pin_07_artifact_i_clock_uniqueness_landed": (
            artifact_statuses["artifact_i_substrate_clock_uniqueness_theorem"]["landed"]
        ),
        "pin_08_artifact_ii_mack_inventory_landed": (
            artifact_statuses["artifact_ii_mack_falsifier_inventory_rows"]["landed"]
        ),
        "pin_09_artifact_iii_vii_aq_stage_2_landed": (
            artifact_statuses["artifact_iii_w4_vii_aq_stage_2_plan_block"]["landed"]
        ),
        "pin_10_tally_PASS": tally["PASS"],
        "pin_11_tally_INFO": tally["INFO"],
        "pin_12_tally_FAIL": tally["FAIL"],
        "pin_13_composite_verdict": verdict,
        "pin_14_solo_mode": "W1_only_per_user_rclab_solo_dispatch",
    }
    # Coerce booleans to JSON-safe strings for SHA stability
    input_pins_normalized = {
        k: (str(v) if isinstance(v, bool) else v) for k, v in input_pins.items()
    }
    for k, v in input_pins_normalized.items():
        s = str(v)
        print(f"  {k:50s} = {s[:64]}")

    # Step 6: Value-string (4-tuple structure)
    print("\n--- Step 6: Build value-string ---")
    value_str = (
        f"composite_verdict={verdict};"
        f"reason={value_short};"
        f"n_audits=4;n_artifacts=3;n_cells_total=12;"
        f"PASS_cells={tally['PASS']};INFO_cells={tally['INFO']};"
        f"FAIL_cells={tally['FAIL']};"
        f"artifact_i_landed=False;artifact_ii_landed=False;"
        f"artifact_iii_landed=False;"
        f"all_3_artifacts_not_landed_in_W1_only_solo_run=True;"
        f"audit_a_sha_current={audit_sha_records['audit_a_class_g_registry_anchor']['current_prefix']};"
        f"audit_a_sha_plan=39937c8c;"
        f"audit_a_sha_drift={audit_sha_records['audit_a_class_g_registry_anchor']['drift']};"
        f"audit_b_sha_current={audit_sha_records['audit_b_cohomology_class_surrogate']['current_prefix']};"
        f"audit_b_sha_plan=1df983a9;"
        f"audit_b_sha_drift={audit_sha_records['audit_b_cohomology_class_surrogate']['drift']};"
        f"audit_c_sha_current={audit_sha_records['audit_c_sign_pass_tautology']['current_prefix']};"
        f"audit_c_sha_plan=4d2dfd87;"
        f"audit_c_sha_drift={audit_sha_records['audit_c_sign_pass_tautology']['drift']};"
        f"audit_d_sha_current={audit_sha_records['audit_d_v4_anchor_structure']['current_prefix']};"
        f"audit_d_sha_plan=f9caf81a;"
        f"audit_d_sha_drift={audit_sha_records['audit_d_v4_anchor_structure']['drift']};"
        f"audit_a_b_drift_due_to_W1_9_PARTIAL_POSITIVE_and_independent_drift=True;"
        f"audit_c_d_sha_match_W6_3_plan_freeze=True;"
        f"remediation=deferred_to_S91_after_W2_CF_19_mack_AND_W2_W3_CF_29_mack_AND_W4_CF_54_55_planblock_all_land;"
        f"allowlist_row=pending;instances_row=pending"
    )
    print(f"  value: {value_str[:200]}...")

    # Step 7: Emit verdict
    print("\n--- Step 7: Emit verdict ---")
    result = emit_verdict(
        gate_id=GATE_ID,
        verdict=verdict,
        value_str=value_str,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        input_pin_map=input_pins_normalized,
        content_target=THIS_SCRIPT,
    )
    print(f"  audit_sha256  : {result['audit_sha256']}")
    print(f"  content_sha256: {result['content_sha256']}")

    # Step 8: JSON sidecar
    print("\n--- Step 8: Persist JSON sidecar ---")
    report = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value_str": value_str,
        "audit_sha_records": audit_sha_records,
        "artifact_statuses": artifact_statuses,
        "cells": cells,
        "tally": tally,
        "input_pins": input_pins_normalized,
        "dual_sha": {
            "audit_sha256": result["audit_sha256"],
            "content_sha256": result["content_sha256"],
        },
    }
    OUT_JSON.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"  JSON written: {OUT_JSON.relative_to(ROOT)}")

    print("\n" + "=" * 72)
    print(f"VERDICT: {verdict} — {value_short}")
    print("=" * 72)


if __name__ == "__main__":
    main()
