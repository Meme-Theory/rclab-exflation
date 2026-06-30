"""
S84-W0-REGULATOR-RESOLUTION-SV5 — R_842 rectangle migration with SHA retention.

Audit script (META gate; NO physics compute; hashlib + canonical ordered-JSON
serialization only). Migrates DR3 watch from R_918 = [-1.05, -0.85] x [-0.2, 0.2]
(branch w_0 = -0.918, S58/S59 canonical) to R_842 = [-0.942, -0.742] x [-0.2, 0.2]
(branch (iv) w_0 = -0.842454, W0-workshop promoted provisional). Old R_918 SHA is
preserved as HISTORICAL SUPERSEDED. New R_842 SHA is computed from the canonical
ordered-JSON input-pin map. Both SHAs are 64-char hexdigests; verdict pin uses
S84+ dual-SHA schema (audit_sha256 + content_sha256).

Cross-checks: CC-i through CC-vi per plan §W1a-3.SV5. PASS iff all 6 verify
AND both SHAs full-64-char AND audit schedule strictly forward-time AND branch
(iv) center -0.842454 lies in interior of R_842 w_0 interval.

Environment: phonon-exflation-sim/.venv312/Scripts/python.exe; OMP_NUM_THREADS=8
fenced (audit only — no linear algebra). Writes:
  - computations/session-84/s84_w1a_w0_sv5.npz
  - computations/_shared/canonical_sha_ledger.json (created or extended)
  - computations/session-84/s84_gate_verdicts.txt (verdict line appended; created if missing)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import json
import hashlib
import datetime
from pathlib import Path

import numpy as np

# Canonical constants — w0_FW imported only for documentation / audit cross-reference.
# This is an audit script: no derivation uses it; we cite it to anchor the migration
# semantics (R_918 was tied to w0_FW=-0.918 via S58/S59 convention).
from canonical_constants import w0_FW, wa_FW

# ----------------------------------------------------------------------------
# 1. Pinned audit inputs — every value below is fixed by plan §W1a-3.SV5.
# ----------------------------------------------------------------------------

R_842_W0  = (-0.942, -0.742)                    # plan-pinned
R_842_WA  = (-0.2,    0.2)                      # plan-pinned (carried from R_918)
R_918_W0  = (-1.05,  -0.85)                     # historical, R_918 (npz on disk)
R_918_WA  = (-0.2,    0.2)                      # historical, R_918

BRANCH_IV_CENTER_W0   = -0.842454               # (local)  W0-workshop branch (iv) provisional anchor
BRANCH_IV_CENTER_WA   = 0.0                     # (local)  branch (iv) carries wa = 0
TRANSITION_DATE       = "2026-04-18"            # plan date

# Audit schedule (forward-time from plan date; DR3 window opens after W3 audit)
AUDIT_W1_DATE         = "2026-04-20"
AUDIT_W2_DATE         = "2026-04-21"
AUDIT_W3_DATE         = "2026-04-22"
DR3_WINDOW_OPENS_DATE = "2026-04-23"

SCHEMA_VERSION        = "S84+"                  # dual-SHA (audit_sha256 + content_sha256)

# Resolve I/O paths relative to this script's directory (computations/_shared/),
# so the script runs from any cwd.
_HERE = Path(__file__).resolve().parent

# R_918 npz (the actual file on disk, formerly named DR3-LIVE-WATCH; closest to the
# plan-pinned `s83_w3_g42_r_w0_rectangle.npz` that does NOT exist on disk).
R_918_NPZ_PATH = _HERE / "s83_w3_g42_dr3_live_watch.npz"

OUT_NPZ        = _HERE / "s84_w1a_w0_sv5.npz"
OUT_LEDGER     = _HERE / "canonical_sha_ledger.json"
OUT_VERDICTS   = _HERE / "s84_gate_verdicts.txt"

GATE_ID = "S84-W0-REGULATOR-RESOLUTION-SV5"

# ----------------------------------------------------------------------------
# 2. Load R_918 historical record from disk; recover old 64-char SHA verbatim.
# ----------------------------------------------------------------------------

if not R_918_NPZ_PATH.exists():
    raise FileNotFoundError(
        f"R_918 historical npz not found: {R_918_NPZ_PATH}. "
        "Plan pin specified s83_w3_g42_r_w0_rectangle.npz which is absent; "
        "fallback to s83_w3_g42_dr3_live_watch.npz also absent."
    )

_d = np.load(R_918_NPZ_PATH, allow_pickle=True)
R_918_loaded_w0 = tuple(float(x) for x in _d["rectangle_w0"])         # (local)
R_918_loaded_wa = tuple(float(x) for x in _d["rectangle_wa"])         # (local)
R_918_OLD_SHA   = str(_d["closure_sha"])                              # full 64-char hexdigest

# Sanity: R_918 npz bounds match the historical pin (no silent migration in disk file)
assert R_918_loaded_w0 == R_918_W0, (
    f"R_918 w_0 bounds on disk {R_918_loaded_w0} != pinned {R_918_W0}"
)
assert R_918_loaded_wa == R_918_WA, (
    f"R_918 w_a bounds on disk {R_918_loaded_wa} != pinned {R_918_WA}"
)

# Print the first 20 lines worth of input-SHA pinning for audit reproducibility
print(f"[SV5] gate_id        = {GATE_ID}")
print(f"[SV5] R_918 npz      = {R_918_NPZ_PATH}")
print(f"[SV5] R_918 npz_sha  = {hashlib.sha256(R_918_NPZ_PATH.read_bytes()).hexdigest()}")
print(f"[SV5] R_918 w_0      = {R_918_W0}")
print(f"[SV5] R_918 w_a      = {R_918_WA}")
print(f"[SV5] R_842 w_0      = {R_842_W0}")
print(f"[SV5] R_842 w_a      = {R_842_WA}")
print(f"[SV5] branch (iv)    = ({BRANCH_IV_CENTER_W0}, {BRANCH_IV_CENTER_WA})")
print(f"[SV5] transition     = {TRANSITION_DATE}")
print(f"[SV5] schedule       = W1:{AUDIT_W1_DATE} W2:{AUDIT_W2_DATE} W3:{AUDIT_W3_DATE} DR3:{DR3_WINDOW_OPENS_DATE}")
print(f"[SV5] R_918 old SHA  = {R_918_OLD_SHA}")
print(f"[SV5] R_918 SHA len  = {len(R_918_OLD_SHA)}")
print(f"[SV5] schema_version = {SCHEMA_VERSION}")
print(f"[SV5] w0_FW (cite)   = {w0_FW}    (R_918 anchor; not used in derivation)")
print(f"[SV5] wa_FW (cite)   = {wa_FW}    (R_918 anchor; not used in derivation)")

# ----------------------------------------------------------------------------
# 3. Migration consistency: width preserved, center shifted +0.108.
# ----------------------------------------------------------------------------

R_842_w0_width  = R_842_W0[1] - R_842_W0[0]                                       # (local)
R_918_w0_width  = R_918_W0[1] - R_918_W0[0]                                       # (local)
R_842_wa_width  = R_842_WA[1] - R_842_WA[0]                                       # (local)
R_918_wa_width  = R_918_WA[1] - R_918_WA[0]                                       # (local)

R_842_center_w0 = 0.5 * (R_842_W0[0] + R_842_W0[1])                               # (local)
R_918_center_w0 = 0.5 * (R_918_W0[0] + R_918_W0[1])                               # (local)
R_842_center_wa = 0.5 * (R_842_WA[0] + R_842_WA[1])                               # (local)
R_918_center_wa = 0.5 * (R_918_WA[0] + R_918_WA[1])                               # (local)

R_842_half_w0   = 0.5 * R_842_w0_width                                            # (local)

center_shift_w0 = R_842_center_w0 - R_918_center_w0                               # (local)
offset_from_iv  = R_842_center_w0 - BRANCH_IV_CENTER_W0                           # (local)
offset_fraction = abs(offset_from_iv) / R_842_half_w0                             # (local)

# ----------------------------------------------------------------------------
# 4. Compute new R_842 content SHA (SHA of the migration content payload only).
#    Canonical ordered-JSON serialization — same key ordering reproducible across runs.
# ----------------------------------------------------------------------------

content_payload = {
    "gate_id":              GATE_ID,
    "schema_version":       SCHEMA_VERSION,
    "rectangle_id":         "R_842",
    "rectangle_w0":         [R_842_W0[0], R_842_W0[1]],
    "rectangle_wa":         [R_842_WA[0], R_842_WA[1]],
    "branch_iv_center_w0":  BRANCH_IV_CENTER_W0,
    "branch_iv_center_wa":  BRANCH_IV_CENTER_WA,
    "transition_date":      TRANSITION_DATE,
    "audit_schedule": {
        "W1": AUDIT_W1_DATE,
        "W2": AUDIT_W2_DATE,
        "W3": AUDIT_W3_DATE,
        "DR3_window_opens": DR3_WINDOW_OPENS_DATE,
    },
    "superseded": {
        "rectangle_id":   "R_918",
        "rectangle_w0":   [R_918_W0[0], R_918_W0[1]],
        "rectangle_wa":   [R_918_WA[0], R_918_WA[1]],
        "old_sha256":     R_918_OLD_SHA,
        "anchor_w0":      float(w0_FW),
        "anchor_wa":      float(wa_FW),
        "convention":     "S59-pred-w0=-0.918",
    },
}
content_json     = json.dumps(content_payload, sort_keys=True, separators=(",", ":"))
R_842_CONTENT_SHA = hashlib.sha256(content_json.encode("utf-8")).hexdigest()

# Audit SHA: closure of the audit input-pin map (includes content SHA + the audit
# script's own pinned input map). This is what the verdict line references.
audit_payload = {
    "gate_id":              GATE_ID,
    "content_sha256":       R_842_CONTENT_SHA,
    "old_sha256":           R_918_OLD_SHA,
    "schema_version":       SCHEMA_VERSION,
    "transition_date":      TRANSITION_DATE,
    "rectangle_w0":         [R_842_W0[0], R_842_W0[1]],
    "rectangle_wa":         [R_842_WA[0], R_842_WA[1]],
    "branch_iv_center_w0":  BRANCH_IV_CENTER_W0,
    "audit_schedule_W1":    AUDIT_W1_DATE,
    "audit_schedule_W2":    AUDIT_W2_DATE,
    "audit_schedule_W3":    AUDIT_W3_DATE,
    "DR3_window_opens":     DR3_WINDOW_OPENS_DATE,
    "R_918_npz_sha":        hashlib.sha256(R_918_NPZ_PATH.read_bytes()).hexdigest(),
}
audit_json       = json.dumps(audit_payload, sort_keys=True, separators=(",", ":"))
R_842_AUDIT_SHA  = hashlib.sha256(audit_json.encode("utf-8")).hexdigest()

# ----------------------------------------------------------------------------
# 5. Cross-checks CC-i through CC-vi.
# ----------------------------------------------------------------------------

# CC-i: R_842 forms a valid rectangle (low < high in each axis).
CC_i_valid = (R_842_W0[0] < R_842_W0[1]) and (R_842_WA[0] < R_842_WA[1])

# CC-ii: Old R_918 SHA is full 64-char hexdigest, not truncated.
CC_ii_old_full   = (len(R_918_OLD_SHA) == 64) and all(c in "0123456789abcdef" for c in R_918_OLD_SHA.lower())

# CC-iii: New R_842 content SHA is 64-char and distinct from R_918 SHA.
CC_iii_new_full  = (len(R_842_CONTENT_SHA) == 64) and all(c in "0123456789abcdef" for c in R_842_CONTENT_SHA)
CC_iii_distinct  = (R_842_CONTENT_SHA.lower() != R_918_OLD_SHA.lower())
CC_iii_pass      = CC_iii_new_full and CC_iii_distinct

# CC-iv: Dual-SHA schema_version=S84+ valid (audit_sha256 + content_sha256 both present, both 64-char).
CC_iv_audit_full = (len(R_842_AUDIT_SHA) == 64) and all(c in "0123456789abcdef" for c in R_842_AUDIT_SHA)
CC_iv_pass       = (SCHEMA_VERSION == "S84+") and CC_iv_audit_full and CC_iii_new_full

# CC-v: Audit dates form strictly increasing sequence in forward time from plan date.
def _to_date(s):
    return datetime.date.fromisoformat(s)

plan_date  = _to_date(TRANSITION_DATE)                          # (local)
date_seq   = [_to_date(d) for d in [AUDIT_W1_DATE, AUDIT_W2_DATE, AUDIT_W3_DATE, DR3_WINDOW_OPENS_DATE]]
CC_v_strict_increasing = all(date_seq[i] < date_seq[i+1] for i in range(len(date_seq)-1))
CC_v_after_plan        = date_seq[0] > plan_date
CC_v_pass              = CC_v_strict_increasing and CC_v_after_plan

# CC-vi: DR3 window opens AFTER last audit (W3) date (terminal audit before DR3).
CC_vi_pass = _to_date(DR3_WINDOW_OPENS_DATE) > _to_date(AUDIT_W3_DATE)

# Center-in-interior check (PASS gate condition beyond the 6 CC).
center_in_interior = (R_842_W0[0] < BRANCH_IV_CENTER_W0 < R_842_W0[1])

CC_results = {
    "CC-i_rect_valid":           CC_i_valid,
    "CC-ii_old_sha_full_64":     CC_ii_old_full,
    "CC-iii_new_sha_full_distinct": CC_iii_pass,
    "CC-iv_dual_sha_schema_ok":  CC_iv_pass,
    "CC-v_schedule_monotone":    CC_v_pass,
    "CC-vi_dr3_after_w3":        CC_vi_pass,
}
all_cc_pass = all(CC_results.values())

print()
print("[SV5] === Cross-check results ===")
for k, v in CC_results.items():
    print(f"[SV5]   {k}: {'PASS' if v else 'FAIL'}")
print(f"[SV5]   center_in_interior: {'PASS' if center_in_interior else 'FAIL'}  "
      f"(branch_iv={BRANCH_IV_CENTER_W0} in ({R_842_W0[0]}, {R_842_W0[1]}); "
      f"offset_fraction={offset_fraction:.6f})")

# Verdict computation: PASS iff all 6 CC AND both SHAs full-64 AND schedule monotone AND center-in-interior.
both_sha_full_64 = (
    len(R_918_OLD_SHA) == 64
    and len(R_842_CONTENT_SHA) == 64
    and len(R_842_AUDIT_SHA) == 64
)
verdict = (
    "PASS" if (all_cc_pass and both_sha_full_64 and CC_v_pass and center_in_interior)
    else "FAIL"
)
# INFO is reserved for borderline (e.g., center exactly on boundary). Branch (iv) -0.842454
# sits 0.45% from R_842 center, far from any boundary -> not borderline.

# ----------------------------------------------------------------------------
# 6. Write canonical ledger entry (create or extend).
# ----------------------------------------------------------------------------

if OUT_LEDGER.exists():
    ledger = json.loads(OUT_LEDGER.read_text(encoding="utf-8"))
else:
    ledger = {
        "schema_version": SCHEMA_VERSION,
        "description": (
            "Canonical SHA ledger for S84+ dual-SHA audit pins. Each entry binds a "
            "rectangle / pre-registered target to a content SHA (the migration payload) "
            "and an audit SHA (the closure of the audit-script input map). Superseded "
            "entries retain their old SHAs verbatim."
        ),
        "entries": [],
    }

# Refuse silent overwrite of existing R_842 entry; in this session it should not exist yet.
existing_R842 = [e for e in ledger.get("entries", []) if e.get("rectangle_id") == "R_842"]
if existing_R842:
    print(f"[SV5] WARNING: ledger already has {len(existing_R842)} R_842 entry/entries; appending new audit row.")

ledger_entry = {
    "rectangle_id":          "R_842",
    "schema_version":        SCHEMA_VERSION,
    "gate_id":               GATE_ID,
    "transition_date":       TRANSITION_DATE,
    "rectangle_w0":          [R_842_W0[0], R_842_W0[1]],
    "rectangle_wa":          [R_842_WA[0], R_842_WA[1]],
    "branch_iv_center_w0":   BRANCH_IV_CENTER_W0,
    "branch_iv_center_wa":   BRANCH_IV_CENTER_WA,
    "audit_schedule": {
        "W1": AUDIT_W1_DATE,
        "W2": AUDIT_W2_DATE,
        "W3": AUDIT_W3_DATE,
        "DR3_window_opens": DR3_WINDOW_OPENS_DATE,
    },
    "content_sha256":        R_842_CONTENT_SHA,
    "audit_sha256":          R_842_AUDIT_SHA,
    "superseded": {
        "rectangle_id":      "R_918",
        "rectangle_w0":      [R_918_W0[0], R_918_W0[1]],
        "rectangle_wa":      [R_918_WA[0], R_918_WA[1]],
        "old_sha256":        R_918_OLD_SHA,
        "anchor_w0":         float(w0_FW),
        "anchor_wa":         float(wa_FW),
        "convention":        "S59-pred-w0=-0.918",
        "source_file":       str(R_918_NPZ_PATH),
    },
    "verdict":               verdict,
    "cross_checks": {k: bool(v) for k, v in CC_results.items()},
    "center_in_interior":    bool(center_in_interior),
}
ledger["entries"].append(ledger_entry)
OUT_LEDGER.write_text(json.dumps(ledger, indent=2, sort_keys=True), encoding="utf-8")
print(f"[SV5] Wrote ledger entry to {OUT_LEDGER}")

# ----------------------------------------------------------------------------
# 7. Save numeric audit record (npz).
# ----------------------------------------------------------------------------

np.savez(
    OUT_NPZ,
    gate_id=GATE_ID,
    rectangle_R842_w0=np.array(R_842_W0),
    rectangle_R842_wa=np.array(R_842_WA),
    rectangle_R918_w0=np.array(R_918_W0),
    rectangle_R918_wa=np.array(R_918_WA),
    R_842_center_w0=R_842_center_w0,
    R_842_center_wa=R_842_center_wa,
    R_918_center_w0=R_918_center_w0,
    R_918_center_wa=R_918_center_wa,
    R_842_w0_width=R_842_w0_width,
    R_918_w0_width=R_918_w0_width,
    center_shift_w0=center_shift_w0,
    branch_iv_center_w0=BRANCH_IV_CENTER_W0,
    branch_iv_center_wa=BRANCH_IV_CENTER_WA,
    offset_from_iv=offset_from_iv,
    offset_fraction=offset_fraction,
    R_918_old_sha256=R_918_OLD_SHA,
    R_842_content_sha256=R_842_CONTENT_SHA,
    R_842_audit_sha256=R_842_AUDIT_SHA,
    schema_version=SCHEMA_VERSION,
    transition_date=TRANSITION_DATE,
    audit_W1=AUDIT_W1_DATE,
    audit_W2=AUDIT_W2_DATE,
    audit_W3=AUDIT_W3_DATE,
    DR3_window_opens=DR3_WINDOW_OPENS_DATE,
    cc_i=CC_i_valid,
    cc_ii=CC_ii_old_full,
    cc_iii=CC_iii_pass,
    cc_iv=CC_iv_pass,
    cc_v=CC_v_pass,
    cc_vi=CC_vi_pass,
    center_in_interior=center_in_interior,
    verdict=verdict,
)
print(f"[SV5] Wrote npz to {OUT_NPZ}")

# ----------------------------------------------------------------------------
# 8. Print 4-tuple tag (final non-verdict line) and append verdict line.
# ----------------------------------------------------------------------------

value_field = R_842_CONTENT_SHA[:16]                                      # plan-pinned: first 16 of new R_842 SHA
print()
print(f"[SV5] 4-tuple: (value={value_field}, scheme=audit, convention=dual-SHA-S84, L_max=N/A)")

verdict_line = (
    f"{GATE_ID}: {verdict} -- value={value_field} scheme=audit "
    f"convention=dual-SHA-S84 L_max=N/A "
    f"sha256={R_842_AUDIT_SHA}"
)
# Mirror an extended dual-SHA line as a comment row (S84+ canonical record)
dual_sha_row = (
    f"# {GATE_ID} dual-SHA: content_sha256={R_842_CONTENT_SHA} "
    f"audit_sha256={R_842_AUDIT_SHA} old_sha256_R918={R_918_OLD_SHA}"
)

if not OUT_VERDICTS.exists():
    with OUT_VERDICTS.open("a", encoding="utf-8") as f:
        f.write(
            "# S84 gate verdicts. Schema: <GATE_ID>: PASS|FAIL|INFO -- "
            "value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>\n"
            "# S84+ dual-SHA gates also emit a # comment row with content_sha256 "
            "and audit_sha256 per .claude/rules/gate-verdicts.md.\n"
        )

with OUT_VERDICTS.open("a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
    f.write(dual_sha_row + "\n")

print(f"[SV5] Appended verdict to {OUT_VERDICTS}")
print(f"[SV5] verdict_line: {verdict_line}")
