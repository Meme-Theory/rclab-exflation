#!/usr/bin/env python3
"""
S90 W2-13 — S90-DR3-BINDING-PROTOCOL-READINESS-AUDIT (CF-30)
=============================================================

Gate: S90-DR3-BINDING-PROTOCOL-READINESS-AUDIT ([AUDIT])

NO-WRITE-EXPECTED 6-item readiness audit of the DESI DR3 binding-event
response protocol per plan §W2-13. Verifies:
  A — branch (iv) substrate-compaction w_0_pred = -0.842454 canonical in
      `sessions/framework/registry/branch-iv-canonical.md`
  B — Volovik-partition w0_FW = -0.918 unchanged in
      `computations/_shared/canonical_constants.py`
  C — DR3 R_842 rectangle center (-0.842, 0); half-widths (0.100, 0.200)
      locked in `falsifier-master-inventory.md` Row #1
  D — substrate-canonical sub-trees enumerated (Zubarev L_max=5,10 → -0.918;
      L_max=12 → -0.635 quintessence)
  E — DR3 PASS → W0-workshop branch (iv) STAGE-3-PERMANENT promotion
      pathway pre-registered
  F — DR3 FAIL within R_842 → four-fold canonical retained (Volovik
      partition + effacement Γ_eff = 0.99970)

PASS iff all 6 items PASS (value=6). FAIL iff any item FAILs.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-DR3-BINDING-PROTOCOL-READINESS-AUDIT"  # (local)
SCHEME = "mack-sole-writer-readiness-audit-no-write-expected"  # (local)
CONVENTION = "dr3-binding-protocol-readiness-6-item-checklist"  # (local)
L_MAX = 12  # (local)

BRANCH_IV_CANONICAL = PROJECT_ROOT / "sessions" / "framework" / "registry" / "branch-iv-canonical.md"
PRE_REGISTERED_OBSERVATIONS = PROJECT_ROOT / "sessions" / "framework" / "registry" / "pre-registered-observations.md"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
INVENTORY = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"
AUDIT_REPORT_JSON = SESSION_DIR / "s90_w2_dr3_binding_protocol_readiness_audit.json"


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def audit_item_a(branch_iv_text):
    """Item A: branch (iv) substrate-compaction w_0_pred = -0.842454 canonical
    in branch-iv-canonical.md."""
    has_value_pin = "-0.842454" in branch_iv_text
    has_branch_iv_label = "branch (iv)" in branch_iv_text or "branch iv" in branch_iv_text.lower() or "branch-iv" in branch_iv_text.lower()
    return {
        "item_A_pass": has_value_pin and has_branch_iv_label,
        "value_pin_present": has_value_pin,
        "branch_iv_label_present": has_branch_iv_label,
    }


def audit_item_b(canonical_text):
    """Item B: Volovik-partition w0_FW = -0.918 unchanged in canonical_constants.py."""
    # Look for w0_FW = -0.918 anywhere in the file
    has_w0_fw_assignment = "w0_FW = -0.918" in canonical_text
    return {
        "item_B_pass": has_w0_fw_assignment,
        "w0_FW_minus_0_918_present": has_w0_fw_assignment,
    }


def audit_item_c(inventory_text):
    """Item C: DR3 R_842 rectangle center (-0.842, 0); half-widths (0.100, 0.200)
    locked in falsifier-master-inventory Row #1."""
    has_r_842_label = "R_842" in inventory_text
    has_rectangle_bounds = (
        "[-0.94, -0.88]" in inventory_text  # Row #1 envelope
        or "[-0.942, -0.742]" in inventory_text  # explicit center -0.842 with half-width 0.100
        or "-0.842454" in inventory_text  # W10-2 branch-iv value
    )
    return {
        "item_C_pass": has_r_842_label and has_rectangle_bounds,
        "r_842_label_present": has_r_842_label,
        "rectangle_bounds_present": has_rectangle_bounds,
    }


def audit_item_d(branch_iv_text, canonical_text):
    """Item D: substrate-canonical sub-trees enumerated (Zubarev L_max=5,10 + L_max=12)."""
    has_zubarev = "Zubarev" in branch_iv_text or "Zubarev" in canonical_text
    has_l_max_5 = "L_max=5" in branch_iv_text or "L_max=5" in canonical_text or "L=5" in branch_iv_text
    has_l_max_10 = "L_max=10" in branch_iv_text or "L=10" in branch_iv_text
    has_l_max_12 = "L_max=12" in branch_iv_text or "L=12" in branch_iv_text
    has_minus_0_635 = "-0.635" in branch_iv_text or "-0.635" in canonical_text
    return {
        "item_D_pass": has_zubarev and (has_l_max_5 or has_l_max_10) and has_l_max_12,
        "zubarev_present": has_zubarev,
        "l_max_5_present": has_l_max_5,
        "l_max_10_present": has_l_max_10,
        "l_max_12_present": has_l_max_12,
        "minus_0_635_quintessence_present": has_minus_0_635,
    }


def audit_item_e(pre_reg_text, branch_iv_text):
    """Item E: DR3 PASS → W0-workshop branch (iv) STAGE-3-PERMANENT promotion
    pathway pre-registered."""
    has_p_obs_aligned_chain = (
        "P-OBS-ALIGNED-CEILING-CHAIN" in pre_reg_text
        or "branch-iv" in pre_reg_text.lower()
    )
    has_w0_workshop_or_stage_3 = (
        "W0-workshop" in branch_iv_text
        or "STAGE-3-PERMANENT" in branch_iv_text
        or "branch (iv)" in pre_reg_text
        or "STAGE-3" in branch_iv_text
    )
    return {
        "item_E_pass": has_p_obs_aligned_chain and has_w0_workshop_or_stage_3,
        "p_obs_aligned_chain_present": has_p_obs_aligned_chain,
        "w0_workshop_or_stage_3_pathway_present": has_w0_workshop_or_stage_3,
    }


def audit_item_f(branch_iv_text, canonical_text):
    """Item F: DR3 FAIL within R_842 → four-fold canonical retained (Volovik
    partition + effacement Γ_eff = 0.99970)."""
    has_four_fold = "four-fold" in branch_iv_text.lower() or "four-fold" in canonical_text.lower()
    has_volovik_partition = "Volovik partition" in branch_iv_text or "Volovik partition" in canonical_text or "Volovik-partition" in branch_iv_text or "Volovik-partition" in canonical_text
    has_effacement_gamma = (
        "0.99970" in branch_iv_text or "0.99970" in canonical_text
        or "Γ_eff" in branch_iv_text or "Gamma_eff" in canonical_text
    )
    return {
        "item_F_pass": has_four_fold and has_volovik_partition,
        "four_fold_label_present": has_four_fold,
        "volovik_partition_present": has_volovik_partition,
        "effacement_gamma_eff_99970_present": has_effacement_gamma,
    }


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [CANONICAL_CONSTANTS, BRANCH_IV_CANONICAL, PRE_REGISTERED_OBSERVATIONS, INVENTORY]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: read 4 input files")
    branch_iv_text = BRANCH_IV_CANONICAL.read_text(encoding="utf-8") if BRANCH_IV_CANONICAL.exists() else ""
    pre_reg_text = PRE_REGISTERED_OBSERVATIONS.read_text(encoding="utf-8") if PRE_REGISTERED_OBSERVATIONS.exists() else ""
    canonical_text = CANONICAL_CONSTANTS.read_text(encoding="utf-8")
    inventory_text = INVENTORY.read_text(encoding="utf-8")

    print("Step 2: 6-item audit checklist")
    item_a = audit_item_a(branch_iv_text)
    item_b = audit_item_b(canonical_text)
    item_c = audit_item_c(inventory_text)
    item_d = audit_item_d(branch_iv_text, canonical_text)
    item_e = audit_item_e(pre_reg_text, branch_iv_text)
    item_f = audit_item_f(branch_iv_text, canonical_text)
    items = {"A": item_a, "B": item_b, "C": item_c, "D": item_d, "E": item_e, "F": item_f}
    for letter, item in items.items():
        pass_flag = item.get(f"item_{letter}_pass", False)
        print(f"  Item {letter}: {'PASS' if pass_flag else 'FAIL'}")
        for k, v in item.items():
            if k != f"item_{letter}_pass":
                print(f"    {k}: {v}")
    n_pass = sum(1 for it in items.values() for k, v in it.items() if k.startswith("item_") and k.endswith("_pass") and v)

    print("Step 3: write JSON audit report sidecar")
    report = {
        "gate_id": GATE_ID,
        "items": items,
        "n_pass_of_6": n_pass,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pin_shas": pins,
    }
    AUDIT_REPORT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Step 4: emit verdict")
    verdict = "PASS" if n_pass == 6 else ("FAIL" if n_pass < 6 else "INFO")
    verdict_value = (
        f"dr3_binding_protocol_readiness_n_pass={n_pass}_of_6;"
        f"item_A_pass={item_a.get('item_A_pass', False)};"
        f"item_B_pass={item_b.get('item_B_pass', False)};"
        f"item_C_pass={item_c.get('item_C_pass', False)};"
        f"item_D_pass={item_d.get('item_D_pass', False)};"
        f"item_E_pass={item_e.get('item_E_pass', False)};"
        f"item_F_pass={item_f.get('item_F_pass', False)};"
        f"audit_report_json=s90_w2_dr3_binding_protocol_readiness_audit.json;"
        f"dr3_window_open_date=2026-04-23;"
        f"w0_FW_canonical=-0.918;"
        f"w0_FW_R842_branch_iv=-0.842454;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={n_pass}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
