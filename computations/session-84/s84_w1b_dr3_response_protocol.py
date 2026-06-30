#!/usr/bin/env python3
"""
S84 W1b-9 -- S84-DR3-RESPONSE-PROTOCOL
=======================================

Pre-commit framework response protocol BEFORE DESI DR3 release window opens
(2026-04-23). Locks rectangle R_842 = [-0.942, -0.742] x [-0.2, 0.2] in the
(w_0, w_a) CPL plane and enumerates 6 hard lockouts (A-F).

Gate ID: S84-DR3-RESPONSE-PROTOCOL
Trigger: [VERIFY] (PASS/FAIL binary on rectangle-containment)
         [AUDIT]  (R_918 -> R_842 historical migration closure)
Classification: META (pre-commitment + protocol registration)

SUBSTRATE FRAMING
-----------------
w_0 in this protocol is NOT a "dark energy equation of state parameter".
It is the substrate-effacement residual fraction projected onto the CPL plane
(0.03% leakage through substrate-to-observable coupling, branch (iv) canonical).
The "DR3 rectangle" is a phenomenological projection of observational data;
the framework predicts a specific (w_0, w_a) from substrate internal dynamics.

CONVENTION OVERRIDE (S84 orchestrator)
--------------------------------------
canonical_constants.py currently pins w0_FW = -0.918 (S58 four-fold lock).
THIS gate uses the post-W0-workshop branch-(iv) promotion w_0_pred = -0.842454
as the framework prediction under test by SV1-SV4. Provenance is recorded
explicitly in the JSON payload's framework_prediction.canonical_constants_source
field as "branch-(iv) promotion (W0-workshop), pending canonical_constants
update post-DR3 PASS/FAIL".

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py (closure hash)
  - s83_gate_verdicts.txt (G42 DR3-LIVE-WATCH PENDING-EVENT line)
  - DESI DR3 covariance projection (literature pin: DESI 2024 Y3 forecast)
  - R_918 historical SHA: 7f23a7c603522a105dffe271584cc22d7a25c6c22a0cccf09fe180954af5c140

Output 4-tuple:
  (value=R_842_locked, scheme=CPL-w_0_w_a,
   convention=branch-(iv)-canonical, L_max=N/A)

Substitution chains (verified inline, also in the Python REPL transcript):

CC1 (R_842 self-consistency, w_0 axis):
  Definition: w_0_pred = -0.842454 (branch (iv) canonical, W0-workshop)
  Definition: R_842_w0 = [w_0_min, w_0_max] = [-0.942, -0.742]
  Definition: in_R(w) := (w_0_min <= w) AND (w <= w_0_max)
  Substitution: in_R(-0.842454) = (-0.942 <= -0.842454) AND (-0.842454 <= -0.742)
  Simplify left:  -0.842454 - (-0.942) = +0.099546 >= 0 -> TRUE
  Simplify right: -0.742 - (-0.842454) = +0.100454 >= 0 -> TRUE
  Direction: BOTH TRUE => w_0_pred is INSIDE R_842 (self-consistent). PASS.

CC1' (R_918 self-falsifier diagnosis, retrospective):
  Old upper edge: -0.85
  Substitution: w_0_pred - (-0.85) = -0.842454 + 0.85 = +0.007546 > 0
  Direction: w_0_pred is OUTSIDE R_918 upper edge by +0.007546.
  Conclusion: R_918 was a self-falsifier under (iv) canonical -- migration is
              required, not a convenience.

CC3 (DR3 1-sigma extent vs rectangle half-width):
  Definition: half_width_w_0 = (w_0_max - w_0_min)/2 = 0.100
  Definition: sigma_w0_DR3 = 0.046
  Substitution: 1-sigma extent / half-width = 0.046/0.100 = 0.46
  Direction: 0.46 < 1 => 1-sigma DR3 ellipse fits inside R_842 with margin.
              ~2.17-sigma shift in central w_0 needed to exit rectangle.

CC4 (lockout enforcement count):
  Definition: required_lockouts = {A, B, C, D, E, F}, |required_lockouts| = 6
  Substitution: payload_lockouts = list of 6 enumerated entries
  Direction: count match => CC4 PASS.

CC5 (schedule SHA recomputation):
  Definition: schedule_tuple = ('2026-04-20','2026-04-21','2026-04-22','2026-04-23')
  Method: SHA-256 of json.dumps(list(schedule_tuple), separators=(',', ':'))
  Output: 64-char hexdigest, recorded as audit_flow_sha_payload.
"""

# ----------------------------------------------------------------------------
# Environment + canonical imports
# ----------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import datetime
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as MPLRectangle
from matplotlib.patches import Ellipse as MPLEllipse

# Canonical constants (mandatory imports for computation S34+)
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import w0_FW, wa_FW  # noqa: F401  -- S58 pin used for provenance only

# ----------------------------------------------------------------------------
# Pinned inputs (per plan §W1b-9 + orchestrator override)
# ----------------------------------------------------------------------------

# Branch (iv) canonical w_0 prediction (orchestrator override, NOT canonical_constants pin)
W_0_PRED_BRANCH_IV = -0.842454                                 # (local) W0-workshop branch (iv)
WA_PRED_BRANCH_IV  = 0.0                                       # (local) implicit (iv) canonical, no running

# Migrated rectangle R_842 (post-S83 self-falsifier diagnosis)
R842_W0_RANGE = (-0.942, -0.742)                               # (local) w_0 axis half-width 0.100
R842_WA_RANGE = (-0.2, 0.2)                                    # (local) w_a axis half-width 0.200 (UNCHANGED from R_918)
R842_CENTER_W0 = -0.842                                        # (local) nearest half-decimal to w_0_pred
R842_CENTER_WA = 0.0                                           # (local) implicit branch (iv) center

# Historical R_918 (superseded; retained as reference)
R918_HISTORICAL_SHA = "7f23a7c603522a105dffe271584cc22d7a25c6c22a0cccf09fe180954af5c140"  # (local) S83 G42 closure

# DESI DR3 projected covariance (DESI 2024 Y3 forecast pin; per S71 DESI-DR3-SCENARIO-B-PRECISE)
SIGMA_W0_DR3 = 0.046                                           # (local) DESI forecast
SIGMA_WA_DR3 = 0.177                                           # (local) DESI forecast
RHO_W0_WA_DR3 = -0.85                                          # (local) DESI forecast (anti-correlation)

# Audit-flow schedule (locked, SHA-pinned)
SCHEDULE = ("2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23")  # (local) W1, W2, W3, DR3 window-open
DATE_PRE_REGISTERED = "2026-04-19"                              # (local) registration date
DR3_WINDOW_OPENS = "2026-04-23"                                 # (local) hard date

OUT_DIR = Path(__file__).parent
SCRIPT_NAME = Path(__file__).name
GATE_ID = "S84-DR3-RESPONSE-PROTOCOL"

# ----------------------------------------------------------------------------
# SHA-256 input pinning helpers
# ----------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    """SHA-256 of a file's bytes (full 64-char hex)."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s: str) -> str:
    """SHA-256 of a string."""
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def grep_g42_line(verdict_path: Path) -> str:
    """Extract the G42 DR3-LIVE-WATCH line from s83_gate_verdicts.txt."""
    with open(verdict_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("S83-DR3-LIVE-WATCH"):
                return line.rstrip("\n")
    raise RuntimeError(f"S83-DR3-LIVE-WATCH not found in {verdict_path}")

# ----------------------------------------------------------------------------
# Compute input pins (printed in first 20 lines of stdout per gate-verdicts.md)
# ----------------------------------------------------------------------------

cc_path = OUT_DIR / "canonical_constants.py"
s83_verdicts_path = OUT_DIR / "s83_gate_verdicts.txt"

CC_SHA = sha256_file(cc_path)
G42_LINE = grep_g42_line(s83_verdicts_path)
G42_LINE_SHA = sha256_text(G42_LINE)

# DESI DR3 covariance literature pin -- since we only have the projected scalar
# triplet (sigma_w0, sigma_wa, rho), the "literature pin" is the SHA of the
# canonical triplet string itself. This is the policy-equivalent of pinning a
# forecast.csv file we would have if DESI published the projection as a file.
DR3_PROJECTION_PIN = f"sigma_w0={SIGMA_W0_DR3}|sigma_wa={SIGMA_WA_DR3}|rho={RHO_W0_WA_DR3}|source=DESI-2024-Y3-forecast|S71-DESI-DR3-SCENARIO-B-PRECISE"
DR3_PROJECTION_PIN_SHA = sha256_text(DR3_PROJECTION_PIN)

# ----------------------------------------------------------------------------
# Dump first-20 input-pin block (per gate-verdicts.md)
# ----------------------------------------------------------------------------

print(f"[{GATE_ID}] script: {SCRIPT_NAME}")
print(f"[{GATE_ID}] pre-registered: {DATE_PRE_REGISTERED}")
print(f"[{GATE_ID}] DR3 window opens: {DR3_WINDOW_OPENS}")
print(f"[{GATE_ID}] INPUT-PIN canonical_constants.py = {CC_SHA}")
print(f"[{GATE_ID}] INPUT-PIN s83_gate_verdicts.txt G42 line SHA = {G42_LINE_SHA}")
print(f"[{GATE_ID}] INPUT-PIN DR3 projection pin SHA = {DR3_PROJECTION_PIN_SHA}")
print(f"[{GATE_ID}] INPUT-PIN R_918 historical SHA = {R918_HISTORICAL_SHA}")
print(f"[{GATE_ID}] CANONICAL-CONST w0_FW (current pin) = {w0_FW}  (S58)")
print(f"[{GATE_ID}] BRANCH-(iv) w_0_pred OVERRIDE = {W_0_PRED_BRANCH_IV}  (W0-workshop)")
print(f"[{GATE_ID}] R_842 = [{R842_W0_RANGE[0]}, {R842_W0_RANGE[1]}] x [{R842_WA_RANGE[0]}, {R842_WA_RANGE[1]}]")
print(f"[{GATE_ID}] R_842 supersedes R_918 = [-1.05, -0.85] x [-0.2, 0.2]")
print(f"[{GATE_ID}] DESI DR3 projected: sigma_w0={SIGMA_W0_DR3}, sigma_wa={SIGMA_WA_DR3}, rho={RHO_W0_WA_DR3}")
print(f"[{GATE_ID}] schedule: W1={SCHEDULE[0]}, W2={SCHEDULE[1]}, W3={SCHEDULE[2]}, DR3={SCHEDULE[3]}")
print()

# ----------------------------------------------------------------------------
# Build covariance matrix (CPL plane)
# Substitution chain:
#   sigma_w0^2 = 0.046^2 = 0.002116
#   sigma_wa^2 = 0.177^2 = 0.031329
#   rho * sigma_w0 * sigma_wa = -0.85 * 0.046 * 0.177 = -0.0069207
# Plan-stated rounded matrix uses -0.006919 (rounded to 6dp);
# we use the EXACT computed -0.0069207 in the artifacts and document the
# round-off difference in the JSON payload.
# ----------------------------------------------------------------------------

cov_w0w0 = SIGMA_W0_DR3 ** 2                                    # (local) variance w_0
cov_wawa = SIGMA_WA_DR3 ** 2                                    # (local) variance w_a
cov_offdiag = RHO_W0_WA_DR3 * SIGMA_W0_DR3 * SIGMA_WA_DR3       # (local) covariance

cov_DR3 = np.array(
    [[cov_w0w0, cov_offdiag],
     [cov_offdiag, cov_wawa]],
    dtype=np.float64,
)

# Sanity: positive-definiteness of cov
cov_eigvals = np.linalg.eigvalsh(cov_DR3)                       # (local) numpy CPU is fine on 2x2
assert np.all(cov_eigvals > 0), f"cov_DR3 not PD; eigvals = {cov_eigvals}"
cov_det = float(np.linalg.det(cov_DR3))                         # (local)

print(f"[{GATE_ID}] cov_DR3 = {cov_DR3.tolist()}")
print(f"[{GATE_ID}] cov_DR3 eigvals = {cov_eigvals.tolist()}")
print(f"[{GATE_ID}] cov_DR3 det = {cov_det:.6e}")
print()

# ----------------------------------------------------------------------------
# Self-consistency check (CC1): w_0_pred inside R_842
# ----------------------------------------------------------------------------

def in_R_842(w_0: float, w_a: float) -> bool:
    """Decision rule: rectangle-containment for R_842."""
    in_w0 = (R842_W0_RANGE[0] <= w_0 <= R842_W0_RANGE[1])
    in_wa = (R842_WA_RANGE[0] <= w_a <= R842_WA_RANGE[1])
    return in_w0 and in_wa

cc1_pass = in_R_842(W_0_PRED_BRANCH_IV, WA_PRED_BRANCH_IV)
offset_from_center_w0 = abs(W_0_PRED_BRANCH_IV - R842_CENTER_W0)  # (local)
half_width_w0 = (R842_W0_RANGE[1] - R842_W0_RANGE[0]) / 2.0       # (local) = 0.100
relative_offset_pct = 100.0 * offset_from_center_w0 / half_width_w0  # (local) = 0.454%

print(f"[{GATE_ID}] CC1 (rectangle self-consistency): w_0_pred in R_842 = {cc1_pass}")
print(f"[{GATE_ID}] CC1 offset from center: {offset_from_center_w0:.6f} (= {relative_offset_pct:.4f}% of half-width)")

# CC1' (retrospective R_918 self-falsifier diagnosis)
r918_w0_max = -0.85                                             # (local) old upper edge
offset_outside_r918 = W_0_PRED_BRANCH_IV - r918_w0_max          # (local) +0.007546
print(f"[{GATE_ID}] CC1' R_918 retrospective: w_0_pred - (-0.85) = {offset_outside_r918:+.6f} (R_918 self-falsifier confirmed)")

# CC3 (DR3 1-sigma vs half-width)
cc3_ratio = SIGMA_W0_DR3 / half_width_w0                        # (local) 0.46
cc3_sigma_to_exit = (half_width_w0 - offset_from_center_w0) / SIGMA_W0_DR3  # (local) ~2.17-sigma
print(f"[{GATE_ID}] CC3 sigma_w0/half_width = {cc3_ratio:.4f} (1-sigma fits with margin)")
print(f"[{GATE_ID}] CC3 sigma-to-exit (nearest edge): ~{cc3_sigma_to_exit:.3f}-sigma shift")

# ----------------------------------------------------------------------------
# Schedule SHA (CC5)
# ----------------------------------------------------------------------------

schedule_canonical = json.dumps(list(SCHEDULE), separators=(',', ':'))  # (local)
audit_flow_sha = sha256_text(schedule_canonical)                # (local) 64-char
print(f"[{GATE_ID}] CC5 schedule canonical form: {schedule_canonical}")
print(f"[{GATE_ID}] CC5 audit_flow_sha_payload = {audit_flow_sha}")

# ----------------------------------------------------------------------------
# Lockouts (CC4): exactly 6, A-F, all HARD
# ----------------------------------------------------------------------------

LOCKOUTS = [
    "LOCKOUT-A: NO retreat to dual-pin (branch (iv)-only is the framework commitment).",
    "LOCKOUT-B: NO scheme-shopping post-data (convention is the one pinned here).",
    "LOCKOUT-C: NO rectangle-resizing (R_842 is locked at 0.10-half-width in w_0).",
    "LOCKOUT-D: NO w_a axis migration (w_a rectangle [-0.2, 0.2] is locked).",
    "LOCKOUT-E: NO post-2026-04-23 redefinition of branch (iv) canonical w_0_pred.",
    "LOCKOUT-F: NO post-2026-04-23 tau_fold relocation that shifts w_0_pred.",
]
assert len(LOCKOUTS) == 6, "CC4 FAIL: lockout count != 6"
print(f"[{GATE_ID}] CC4 lockouts enumerated: {len(LOCKOUTS)}/6")

# ----------------------------------------------------------------------------
# Build the locked pre-registration payload
# ----------------------------------------------------------------------------

payload = {
    "gate_id": GATE_ID,
    "session": 84,
    "wave": "W1b-9",
    "date_pre_registered": DATE_PRE_REGISTERED,
    "dr3_window_opens": DR3_WINDOW_OPENS,
    "rectangle": {
        "name": "R_842",
        "w_0_range": list(R842_W0_RANGE),
        "w_a_range": list(R842_WA_RANGE),
        "center_w_0": R842_CENTER_W0,
        "center_w_a": R842_CENTER_WA,
        "half_width_w_0": half_width_w0,
        "half_width_w_a": (R842_WA_RANGE[1] - R842_WA_RANGE[0]) / 2.0,
        "supersedes": "R_918",
        "R_918_w_0_range": [-1.05, -0.85],
        "R_918_w_a_range": [-0.2, 0.2],
        "R_918_historical_sha": R918_HISTORICAL_SHA,
        "R_918_retention": "permanent-results-registry/superseded (forward-pointer to R_842)",
        "migration_reason": (
            "Post-S83 (iv) canonical w_0_pred = -0.842454 lies +0.007546 OUTSIDE the "
            "R_918 upper edge -0.85 -- R_918 was a self-falsifier of its own central "
            "prediction. R_842 centered on -0.842 with same 0.100 half-width restores "
            "self-consistency (offset 0.454% of half-width)."
        ),
    },
    "framework_prediction": {
        "w_0_pred": W_0_PRED_BRANCH_IV,
        "w_a_pred": WA_PRED_BRANCH_IV,
        "branch": "(iv)",
        "canonical_constants_source": (
            "branch-(iv) promotion (W0-workshop, S83); pending canonical_constants "
            f"update post-DR3 PASS/FAIL. canonical_constants.py currently pins "
            f"w0_FW = {w0_FW} (S58 four-fold lock); branch-(iv) override = {W_0_PRED_BRANCH_IV} "
            "is the prediction under test by SV1-SV4."
        ),
        "offset_from_rectangle_center_w_0": offset_from_center_w0,
        "offset_relative_pct_of_half_width": relative_offset_pct,
        "self_consistency_check": "CC1 PASS: w_0_pred inside R_842",
    },
    "covariance_DR3_projected": {
        "sigma_w0": SIGMA_W0_DR3,
        "sigma_wa": SIGMA_WA_DR3,
        "rho_w0_wa": RHO_W0_WA_DR3,
        "matrix_exact": cov_DR3.tolist(),
        "matrix_plan_rounded_6dp": [[0.002116, -0.006919], [-0.006919, 0.031329]],
        "matrix_diff_offdiag_exact_minus_rounded": float(cov_DR3[0, 1] - (-0.006919)),
        "eigenvalues": cov_eigvals.tolist(),
        "determinant": cov_det,
        "source_pin": DR3_PROJECTION_PIN,
        "source_pin_sha256": DR3_PROJECTION_PIN_SHA,
    },
    "decision_rule": {
        "PASS": "DR3_central in R_842",
        "FAIL": "DR3_central NOT in R_842 -> branch (iv) REFUTED at rectangle-containment confidence",
        "INFO_margin": "DR3_central within margin region OR one component inside + one outside -> escalate to S84-DR3-CONTINGENCY-FINE-GRAINED (CF #44, 7-scenario sub-tree)",
    },
    "scorecard_on_fail": {
        "REQUIRED": True,
        "section": "refutations",
        "linked_sha_field": "content_sha256",
        "instruction": (
            "If DR3 central lies outside R_842, append a refutation entry to the "
            "permanent-results-registry under §VII.M.scorecard.refutations linking "
            "this payload's content_sha256. NO retreat permitted (LOCKOUTS A-F)."
        ),
    },
    "lockouts": LOCKOUTS,
    "audit_flow_schedule": {
        "W1": SCHEDULE[0],
        "W2": SCHEDULE[1],
        "W3": SCHEDULE[2],
        "DR3_window_opens": SCHEDULE[3],
    },
    "audit_flow_canonical": schedule_canonical,
    "audit_flow_sha_payload": audit_flow_sha,
    "input_pins": {
        "canonical_constants_py_sha256": CC_SHA,
        "s83_gate_verdicts_G42_line": G42_LINE,
        "s83_gate_verdicts_G42_line_sha256": G42_LINE_SHA,
        "DR3_projection_pin": DR3_PROJECTION_PIN,
        "DR3_projection_pin_sha256": DR3_PROJECTION_PIN_SHA,
        "R_918_historical_sha": R918_HISTORICAL_SHA,
    },
    "cross_checks": {
        "CC1_rectangle_self_consistency": {
            "w_0_pred_in_R_842": bool(cc1_pass),
            "w_a_pred_in_R_842": bool(R842_WA_RANGE[0] <= WA_PRED_BRANCH_IV <= R842_WA_RANGE[1]),
            "left_margin_w_0": W_0_PRED_BRANCH_IV - R842_W0_RANGE[0],
            "right_margin_w_0": R842_W0_RANGE[1] - W_0_PRED_BRANCH_IV,
            "verdict": "PASS",
        },
        "CC1_prime_R918_retrospective": {
            "w_0_pred_minus_R918_upper_edge": float(offset_outside_r918),
            "verdict": "R_918 self-falsifier confirmed; migration justified",
        },
        "CC2_w_a_axis": {
            "w_a_pred_implicit": WA_PRED_BRANCH_IV,
            "w_a_range": list(R842_WA_RANGE),
            "verdict": "PASS (w_a=0 inside [-0.2, 0.2]; conservative tolerance unchanged from R_918)",
        },
        "CC3_sigma_extent_vs_half_width": {
            "ratio_sigma_w0_over_half_width": float(cc3_ratio),
            "sigma_to_nearest_edge": float(cc3_sigma_to_exit),
            "interpretation": "1-sigma DR3 ellipse fits inside R_842; ~2.17-sigma central shift to exit nearest edge",
        },
        "CC4_lockout_count": {
            "required": 6,
            "present": len(LOCKOUTS),
            "verdict": "PASS",
        },
        "CC5_schedule_sha": {
            "canonical_form": schedule_canonical,
            "method": "sha256(json.dumps(list, separators=(',', ':')))",
            "sha256": audit_flow_sha,
            "verdict": "PASS (recomputed from schedule tuple)",
        },
    },
    "fourtuple_tag": {
        "value": "R_842_locked",
        "scheme": "CPL-w_0_w_a",
        "convention": "branch-(iv)-canonical",
        "L_max": "N/A",
    },
    "carry_forward_pointers": {
        "CF_44": "S84-DR3-CONTINGENCY-FINE-GRAINED (7-scenario sub-tree for INFO/margin cases)",
    },
}

# ----------------------------------------------------------------------------
# Compute content_sha256 and audit_sha256 (S84+ dual-SHA schema)
#  - content_sha256: SHA of the canonical-JSON-serialized payload MINUS the SHA
#                    fields themselves (so the digest is over the substantive
#                    content, not over previous digests).
#  - audit_sha256:   SHA over the ordered input-pin map (canonical-JSON form).
# ----------------------------------------------------------------------------

# Audit SHA = SHA over the input-pin map (ordered dict, JSON-canonical)
audit_pin_map = {
    "gate_id": GATE_ID,
    "canonical_constants_py_sha256": CC_SHA,
    "s83_gate_verdicts_G42_line_sha256": G42_LINE_SHA,
    "DR3_projection_pin_sha256": DR3_PROJECTION_PIN_SHA,
    "R_918_historical_sha": R918_HISTORICAL_SHA,
    "audit_flow_sha_payload": audit_flow_sha,
    "lockouts_count": len(LOCKOUTS),
}
audit_canonical = json.dumps(audit_pin_map, sort_keys=True, separators=(',', ':'))
AUDIT_SHA = sha256_text(audit_canonical)

# Content SHA: serialize payload (without SHA fields) deterministically
payload_for_content_sha = dict(payload)
payload_for_content_sha.pop("content_sha256", None)
payload_for_content_sha.pop("audit_sha256", None)
content_canonical = json.dumps(payload_for_content_sha, sort_keys=True, separators=(',', ':'))
CONTENT_SHA = sha256_text(content_canonical)

# Insert SHAs into final payload
payload["content_sha256"] = CONTENT_SHA
payload["audit_sha256"] = AUDIT_SHA

# Sanity: content and audit SHAs MUST be distinct
assert CONTENT_SHA != AUDIT_SHA, "Content and audit SHA collision -- payload pathological"

# ----------------------------------------------------------------------------
# Write JSON payload
# ----------------------------------------------------------------------------

json_path = OUT_DIR / "s84_w1b_dr3_response_protocol.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(payload, f, indent=2, sort_keys=False)
print(f"[{GATE_ID}] JSON payload written: {json_path}")
print(f"[{GATE_ID}] content_sha256 = {CONTENT_SHA}")
print(f"[{GATE_ID}] audit_sha256   = {AUDIT_SHA}")

# ----------------------------------------------------------------------------
# Write NPZ (cov matrix + rectangle corners + framework point + DR3 pin)
# ----------------------------------------------------------------------------

npz_path = OUT_DIR / "s84_w1b_dr3_response_protocol.npz"
rectangle_corners = np.array([
    [R842_W0_RANGE[0], R842_WA_RANGE[0]],
    [R842_W0_RANGE[1], R842_WA_RANGE[0]],
    [R842_W0_RANGE[1], R842_WA_RANGE[1]],
    [R842_W0_RANGE[0], R842_WA_RANGE[1]],
    [R842_W0_RANGE[0], R842_WA_RANGE[0]],
], dtype=np.float64)

np.savez_compressed(
    npz_path,
    cov_DR3=cov_DR3,
    rectangle_corners=rectangle_corners,
    framework_point=np.array([W_0_PRED_BRANCH_IV, WA_PRED_BRANCH_IV], dtype=np.float64),
    rectangle_center=np.array([R842_CENTER_W0, R842_CENTER_WA], dtype=np.float64),
    sigma_triplet=np.array([SIGMA_W0_DR3, SIGMA_WA_DR3, RHO_W0_WA_DR3], dtype=np.float64),
    R918_corners=np.array([
        [-1.05, -0.2], [-0.85, -0.2], [-0.85, 0.2], [-1.05, 0.2], [-1.05, -0.2]
    ], dtype=np.float64),
    audit_flow_schedule=np.array(SCHEDULE, dtype='U10'),
)
print(f"[{GATE_ID}] NPZ written: {npz_path}")

# ----------------------------------------------------------------------------
# Plot: (w_0, w_a) plane with R_842 + R_918 (superseded) + framework point + 1-sigma ellipse
# ----------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8.5, 6.5))

# R_918 (superseded, thin grey dashed)
ax.add_patch(MPLRectangle(
    (-1.05, -0.2), 0.20, 0.40,
    fill=False, edgecolor='#888888', linestyle='--', linewidth=1.0,
    label='R_918 (superseded)',
))

# R_842 (active, bold solid)
ax.add_patch(MPLRectangle(
    (R842_W0_RANGE[0], R842_WA_RANGE[0]),
    R842_W0_RANGE[1] - R842_W0_RANGE[0],
    R842_WA_RANGE[1] - R842_WA_RANGE[0],
    fill=False, edgecolor='#1f4e79', linestyle='-', linewidth=2.0,
    label='R_842 (active)',
))

# Framework branch (iv) point
ax.plot(
    W_0_PRED_BRANCH_IV, WA_PRED_BRANCH_IV,
    marker='*', markersize=18, color='#c0392b',
    markeredgecolor='black', markeredgewidth=0.8,
    linestyle='None',
    label=f'branch (iv) w_0_pred = {W_0_PRED_BRANCH_IV}',
    zorder=5,
)

# DR3 projected 1-sigma ellipse at (w_0_pred, w_a=0)
# Eigen-decomposition gives ellipse semi-axes and orientation
evals, evecs = np.linalg.eigh(cov_DR3)
# Larger eigenvalue first
order = np.argsort(evals)[::-1]
evals, evecs = evals[order], evecs[:, order]
semi_major = float(np.sqrt(evals[0]))                           # (local) 1-sigma
semi_minor = float(np.sqrt(evals[1]))                           # (local)
angle_deg = float(np.degrees(np.arctan2(evecs[1, 0], evecs[0, 0])))  # (local)

ellipse_1sigma = MPLEllipse(
    (W_0_PRED_BRANCH_IV, WA_PRED_BRANCH_IV),
    width=2.0 * semi_major,
    height=2.0 * semi_minor,
    angle=angle_deg,
    fill=False, edgecolor='#2c7a3e', linestyle='-.', linewidth=1.5,
    label='DR3 projected 1-sigma',
)
ax.add_patch(ellipse_1sigma)

# Old S58 canonical w0_FW = -0.918 marker (for context only)
ax.plot(
    w0_FW, 0.0,
    marker='x', markersize=10, color='#888888',
    markeredgewidth=1.5, linestyle='None',
    label=f'(prior) w0_FW S58 = {w0_FW}',
    zorder=4,
)

# Reference: LCDM
ax.plot(
    -1.0, 0.0,
    marker='+', markersize=12, color='black',
    markeredgewidth=1.2, linestyle='None',
    label='LCDM (w_0=-1, w_a=0)',
    zorder=3,
)

ax.set_xlim(-1.10, -0.70)
ax.set_ylim(-0.30, 0.30)
ax.set_xlabel("$w_0$ (CPL plane projection of substrate-effacement residual)", fontsize=11)
ax.set_ylabel("$w_a$", fontsize=11)
ax.set_title(
    f"{GATE_ID}: pre-registered DR3 response under R_842\n"
    f"Pre-reg {DATE_PRE_REGISTERED}; DR3 window opens {DR3_WINDOW_OPENS}",
    fontsize=11,
)
ax.grid(True, alpha=0.3)
ax.legend(loc='lower left', fontsize=9, framealpha=0.92)
ax.set_aspect('auto')

plt.tight_layout()
png_path = OUT_DIR / "s84_w1b_dr3_response_protocol.png"
plt.savefig(png_path, dpi=140, bbox_inches='tight')
plt.close(fig)
print(f"[{GATE_ID}] Plot written: {png_path}")

# ----------------------------------------------------------------------------
# Verdict construction (PASS at registration)
# ----------------------------------------------------------------------------

# Verify all 6 artifacts are on disk for PASS at registration:
#   1. script (this file)         -- always present at runtime
#   2. JSON payload
#   3. NPZ
#   4. PNG
#   5. registry entry            -- separate write, verified by orchestrator
#   6. schedule SHA computed     -- audit_flow_sha above

artifacts_check = {
    "script": (OUT_DIR / SCRIPT_NAME).exists(),
    "json": json_path.exists() and json_path.stat().st_size > 0,
    "npz":  npz_path.exists() and npz_path.stat().st_size > 0,
    "png":  png_path.exists() and png_path.stat().st_size > 0,
    "schedule_sha_computed": (audit_flow_sha is not None and len(audit_flow_sha) == 64),
}
all_artifacts_present = all(artifacts_check.values())
all_lockouts_codified = (len(LOCKOUTS) == 6)
all_cc_pass = (
    cc1_pass
    and (R842_WA_RANGE[0] <= WA_PRED_BRANCH_IV <= R842_WA_RANGE[1])
    and (offset_outside_r918 > 0)
    and (cc3_ratio < 1.0)
    and (len(LOCKOUTS) == 6)
)

verdict = "PASS" if (all_artifacts_present and all_lockouts_codified and all_cc_pass) else "FAIL"

print()
print(f"[{GATE_ID}] Artifact check: {artifacts_check}")
print(f"[{GATE_ID}] Lockouts codified: {len(LOCKOUTS)}/6")
print(f"[{GATE_ID}] All cross-checks PASS: {all_cc_pass}")
print(f"[{GATE_ID}] PASS-AT-REGISTRATION verdict: {verdict}")
print()

# ----------------------------------------------------------------------------
# Append verdict line (S84+ dual-SHA schema)
# ----------------------------------------------------------------------------

verdicts_path = OUT_DIR / "s84_gate_verdicts.txt"
verdict_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value=R_842_locked "
    f"scheme=CPL-w_0_w_a "
    f"convention=branch-(iv)-canonical "
    f"L_max=N/A "
    f"content_sha256={CONTENT_SHA} "
    f"audit_sha256={AUDIT_SHA}\n"
)

# Header on first append
header_lines = []
if not verdicts_path.exists():
    header_lines = [
        f"# Session 84 Gate Verdicts (S84+ dual-SHA schema)\n",
        f"# Format: <GATE_ID>: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> content_sha256=<64> audit_sha256=<64>\n",
        f"# Pre-S81 single-SHA closure form remains valid for legacy migration; S84+ NEW lines MUST use dual-SHA.\n",
        f"\n",
    ]
with open(verdicts_path, 'a', encoding='utf-8') as f:
    if header_lines:
        f.writelines(header_lines)
    f.write(verdict_line)

print(f"[{GATE_ID}] Verdict appended: {verdicts_path}")
print(f"[{GATE_ID}] line: {verdict_line.strip()}")
print()
print(f"[{GATE_ID}] 4-tuple: (value=R_842_locked, scheme=CPL-w_0_w_a, convention=branch-(iv)-canonical, L_max=N/A)")
