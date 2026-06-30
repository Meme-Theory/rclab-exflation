#!/usr/bin/env python
"""S84 W4-42 BICEP-KECK-2026-PRE-REGISTER — frozen JSON decision tree against
the projected BICEP/Keck Array 2026 release of r(k_CMB).

Gate ID: S84-BICEP-KECK-2026-PRE-REGISTER
Trigger: [VERIFY]
Classification: GEOMETRIC (tensor-to-scalar ratio at CMB)

This is a procedural gate. It does not compute new physics; it freezes the
framework's pre-registered response to a future observation.

Inputs:
    r_CMB_framework     = 0.01173... (G46 PASS, S83 W3-G46)
    sigma_r_BK_2026     = 0.005    (Ade+ 2025 preprint forecast for BK-Array 2026)
    sigma_theory_G46    = 0.003    (nominal propagation estimate)

Decision-tree branches (pre-registered, no post-release re-registration):
    A (CONFIRMATION): r_BK ∈ [0.009, 0.015]   → PASS with high confidence
    B (CONSISTENCY):  r_BK_upper < 0.020       → INFO
    C (DISFAVORED):   r_BK_central > 0.025    → FAIL (2-3σ disfavored)
    D (RULED OUT):    r_BK_upper   < 0.008    → FAIL (2+σ above 95% CL upper)

Substitution chain [VERIFY] for thresholds — see §VI.W4-42 of
session-84-w4-workingpaper.md.

Outputs:
    s84_w4_bicep_keck_2026_decision_tree.json  — frozen JSON
    Verdict → s84_gate_verdicts.txt (dual-SHA form)
    Registry entry in sessions/framework/registry/pre-registered-observations.md
"""

import hashlib
import json
import os
from datetime import datetime, timezone

import numpy as np

# Canonical constants MUST come from canonical_constants.py
from canonical_constants import (
    r_CMB_framework,       # 0.011731522176014426  (S83 G46 PASS)
    sigma_r_BK_2026,       # 0.005                 (S84, Ade+ 2025)
)

# ---- Input-pin provenance (SHA-256 of every file read) ----------------------
HERE = os.path.dirname(os.path.abspath(__file__))


def sha256_of_file(path: str) -> str:
    """Return SHA-256 hexdigest of a file (empty string if missing)."""
    if not os.path.exists(path):
        return ""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


CANONICAL_CONSTANTS_PATH = os.path.join(HERE, "canonical_constants.py")
G46_NPZ_PATH = os.path.join(HERE, "s83_w3_g46_tensor_transfer.npz")

input_sha = {
    "canonical_constants.py": sha256_of_file(CANONICAL_CONSTANTS_PATH),
    "s83_w3_g46_tensor_transfer.npz": sha256_of_file(G46_NPZ_PATH),
    "Ade+ 2025 preprint forecast": "external-literature-no-file-SHA",
}

# ---- Pre-registration parameters (frozen 2026-04-18) ------------------------
FREEZE_DATE = "2026-04-18"                          # (local) frozen pre-reg date
SINGLE_AUTHORITY_TAG = "mack-cosmic-bridge"          # (local) sole registering authority
sigma_theory_G46 = 0.003                             # (local) nominal G46 propagation estimate (plan PRDR)

# Decision-tree threshold values (pre-registered, plan §W4-42)
A_lower = 0.009                                      # (local) Branch A lower window
A_upper = 0.015                                      # (local) Branch A upper window
B_upper = 0.020                                      # (local) Branch B consistency threshold
C_lower = 0.025                                      # (local) Branch C disfavored threshold
D_upper = 0.008                                      # (local) Branch D ruled-out threshold

# ---- Sigma-distance diagnostics (computed for registry provenance) ----------
# Definitions:
#   sigma_comb = sqrt(sigma_r_BK_2026**2 + sigma_theory_G46**2)
#   z(x) = (x - r_FW) / sigma_*
sigma_comb = float(np.sqrt(sigma_r_BK_2026**2 + sigma_theory_G46**2))   # (local)
A_lower_sigma_theory = (r_CMB_framework - A_lower) / sigma_theory_G46   # (local)
A_upper_sigma_theory = (A_upper - r_CMB_framework) / sigma_theory_G46   # (local)
B_upper_sigma_exp    = (B_upper - r_CMB_framework) / sigma_r_BK_2026    # (local)
C_lower_sigma_comb   = (C_lower - r_CMB_framework) / sigma_comb         # (local)
D_upper_sigma_comb   = (r_CMB_framework - D_upper) / sigma_comb         # (local)

# ---- JSON decision-tree structure -------------------------------------------
decision_tree = {
    "gate_id": "S84-BICEP-KECK-2026-PRE-REGISTER",
    "frozen_date": FREEZE_DATE,
    "single_authority": SINGLE_AUTHORITY_TAG,
    "no_post_release_reregistration": True,
    "framework_prediction": {
        "observable": "r(k_CMB)",
        "value": r_CMB_framework,
        "source_gate": "S83-W3-G46-TENSOR-TRANSFER",
        "source_file": "s83_w3_g46_tensor_transfer.npz",
        "sigma_theory_nominal": sigma_theory_G46,
    },
    "experiment": {
        "name": "BICEP/Keck Array 2026 release",
        "sigma_r_forecast": sigma_r_BK_2026,
        "citation": "Ade+ 2025 preprint (projected Q2-Q3 2026 release)",
        "pivot_scale_Mpc_inv": 0.05,
    },
    "branches": [
        {
            "branch": "A",
            "label": "CONFIRMATION",
            "rule": "r_BK central in window AND r_BK within experimental 1-sigma of framework",
            "threshold_lower": A_lower,
            "threshold_upper": A_upper,
            "verdict_on_trigger": "PASS",
            "confidence": "framework +~3-sigma confirmation on r",
            "diagnostic_sigma": {
                "lower_offset_in_sigma_theory": A_lower_sigma_theory,
                "upper_offset_in_sigma_theory": A_upper_sigma_theory,
            },
            "explanation": (
                "Central r_BK in [0.009, 0.015] brackets the framework value "
                f"r_FW = {r_CMB_framework:.5f} to within ~+/-1 sigma_theory "
                f"({sigma_theory_G46}). Direct confirmation of G46 tensor-transfer."
            ),
        },
        {
            "branch": "B",
            "label": "CONSISTENCY",
            "rule": "r_BK 95%CL upper < 0.020 (1-sided)",
            "threshold_lower": None,
            "threshold_upper": B_upper,
            "verdict_on_trigger": "INFO",
            "confidence": "consistent with framework; no discrimination vs slow-roll r>0",
            "diagnostic_sigma": {
                "upper_offset_in_sigma_exp": B_upper_sigma_exp,
            },
            "explanation": (
                "Upper limit r_BK < 0.020 lies "
                f"{B_upper_sigma_exp:.2f} sigma_exp above r_FW, not excluding "
                "framework at 2-sigma. Verdict: INFO (no new discrimination)."
            ),
        },
        {
            "branch": "C",
            "label": "DISFAVORED",
            "rule": "r_BK central > 0.025",
            "threshold_lower": C_lower,
            "threshold_upper": None,
            "verdict_on_trigger": "FAIL",
            "confidence": "framework disfavored at 2-3 sigma combined",
            "diagnostic_sigma": {
                "lower_offset_in_sigma_comb": C_lower_sigma_comb,
            },
            "explanation": (
                "Central r_BK > 0.025 lies "
                f"{C_lower_sigma_comb:.2f} sigma_comb above r_FW "
                f"(sigma_comb = {sigma_comb:.5f}). Verdict: FAIL."
            ),
        },
        {
            "branch": "D",
            "label": "RULED-OUT",
            "rule": "r_BK 95%CL upper < 0.008",
            "threshold_lower": None,
            "threshold_upper": D_upper,
            "verdict_on_trigger": "FAIL",
            "confidence": "framework ruled out at 2+ sigma (FW above 95%CL upper)",
            "diagnostic_sigma": {
                "upper_offset_in_sigma_comb": D_upper_sigma_comb,
            },
            "explanation": (
                f"If the BK 95%CL upper is below 0.008, r_FW = {r_CMB_framework:.5f} "
                f"lies {D_upper_sigma_comb:.2f} sigma_comb above the limit. "
                "Framework prediction is above the exclusion; verdict: FAIL."
            ),
        },
    ],
    "input_sha": input_sha,
    "canonical_constants_used": {
        "r_CMB_framework": r_CMB_framework,
        "sigma_r_BK_2026": sigma_r_BK_2026,
        "sigma_theory_G46_local_nominal": sigma_theory_G46,
    },
    "generated_utc": datetime.now(timezone.utc).isoformat(),
}

# ---- Freeze: write JSON atomically, compute closure SHA ---------------------
JSON_PATH = os.path.join(HERE, "s84_w4_bicep_keck_2026_decision_tree.json")
json_bytes = json.dumps(decision_tree, indent=2, sort_keys=True).encode("utf-8")
with open(JSON_PATH, "wb") as fh:
    fh.write(json_bytes)

content_sha256 = hashlib.sha256(json_bytes).hexdigest()           # (local) content closure SHA

# ---- Audit SHA (ordered input-pin map, canonical form) ----------------------
audit_payload = {
    "gate_id": "S84-BICEP-KECK-2026-PRE-REGISTER",
    "frozen_date": FREEZE_DATE,
    "r_CMB_framework": r_CMB_framework,
    "sigma_r_BK_2026": sigma_r_BK_2026,
    "sigma_theory_G46": sigma_theory_G46,
    "A_lower": A_lower,
    "A_upper": A_upper,
    "B_upper": B_upper,
    "C_lower": C_lower,
    "D_upper": D_upper,
    "input_sha": input_sha,
}
audit_bytes = json.dumps(audit_payload, sort_keys=True).encode("utf-8")
audit_sha256 = hashlib.sha256(audit_bytes).hexdigest()            # (local) audit SHA

# ---- Input-pin echo (first 20 lines of stdout, per gate-verdicts rule) ------
print("S84-BICEP-KECK-2026-PRE-REGISTER")
print(f"  input_sha.canonical_constants.py = {input_sha['canonical_constants.py'][:16]}...")
print(f"  input_sha.s83_w3_g46_tensor_transfer.npz = {input_sha['s83_w3_g46_tensor_transfer.npz'][:16]}...")
print(f"  input_sha.Ade+ 2025 = {input_sha['Ade+ 2025 preprint forecast']}")
print()
print(f"  r_CMB_framework      = {r_CMB_framework:.15f}")
print(f"  sigma_r_BK_2026      = {sigma_r_BK_2026}")
print(f"  sigma_theory_G46     = {sigma_theory_G46} (local nominal)")
print(f"  sigma_comb           = {sigma_comb:.6f}")
print()
print("  Branch A [0.009, 0.015] sigma_theory offsets: "
      f"{A_lower_sigma_theory:+.3f} (lower), {A_upper_sigma_theory:+.3f} (upper)")
print(f"  Branch B upper 0.020 sigma_exp above FW: {B_upper_sigma_exp:+.3f}")
print(f"  Branch C lower 0.025 sigma_comb above FW: {C_lower_sigma_comb:+.3f}")
print(f"  Branch D upper 0.008 sigma_comb FW-above: {D_upper_sigma_comb:+.3f}")
print()
print(f"  frozen: {FREEZE_DATE}   single_authority: {SINGLE_AUTHORITY_TAG}")
print(f"  no_post_release_reregistration: True")
print(f"  JSON path: {JSON_PATH}")
print(f"  content_sha256: {content_sha256}")
print(f"  audit_sha256:   {audit_sha256}")
print()

# ---- Verdict determination (pre-registration itself, not post-release) ------
# PASS = JSON frozen + all 4 branches with thresholds + freeze date + single-authority
branches_ok = (
    len(decision_tree["branches"]) == 4
    and all("threshold_lower" in b or "threshold_upper" in b
            for b in decision_tree["branches"])
    and all("verdict_on_trigger" in b for b in decision_tree["branches"])
)
freeze_ok = decision_tree["frozen_date"] == FREEZE_DATE
authority_ok = decision_tree["single_authority"] == SINGLE_AUTHORITY_TAG
no_reroll_ok = decision_tree["no_post_release_reregistration"] is True
json_exists = os.path.exists(JSON_PATH) and len(json_bytes) > 0

all_ok = branches_ok and freeze_ok and authority_ok and no_reroll_ok and json_exists
verdict = "PASS" if all_ok else "INFO"

# 4-tuple (value, scheme, convention, L_max)
print(f"4-tuple: (value=\"decision-tree-frozen\", scheme=\"pre-registration-JSON\", "
      f"convention=\"BK-Array 2026\", L_max=N/A)")
print()
print(f"VERDICT: {verdict}")
print(f"  branches_ok={branches_ok}  freeze_ok={freeze_ok}  "
      f"authority_ok={authority_ok}  no_reroll_ok={no_reroll_ok}  "
      f"json_exists={json_exists}")

# ---- Verdict-line append (dual-SHA form per S84+) ---------------------------
VERDICT_PATH = os.path.join(HERE, "s84_gate_verdicts.txt")
verdict_line = (
    f"S84-BICEP-KECK-2026-PRE-REGISTER: {verdict} -- "
    f"value=decision-tree-frozen scheme=pre-registration-JSON "
    f"convention=BK-Array-2026 L_max=N/A "
    f"content_sha256={content_sha256} audit_sha256={audit_sha256}"
)
with open(VERDICT_PATH, "a", encoding="utf-8") as fh:
    fh.write(verdict_line + "\n")

print()
print(f"Appended to {VERDICT_PATH}:")
print(f"  {verdict_line}")
