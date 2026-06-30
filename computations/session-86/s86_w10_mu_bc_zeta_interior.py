"""
S86 W10 §W10-1 — S86-MU-BC-V2-ZETA-AT-INTERIOR (C37)

Goal (per sessions/session-plan/session-86-plan-w10.md §W10-1):
    Derive the integer-12 exponent in
        mu_BC = M_Z * sqrt(1 + exp(12 * tau_fold) / 3)
    via the zeta-at-interior route:
        n_exp = -2 * Re[ ln( analytic_zeta(s=3.5, L_max=10) ) ] / tau_fold
    PASS if |n_exp - 12| <= 1e-3 with L_max stability and delta_strip
    independence; INFO if |n_exp - 12| in (0.5, 1.0]; FAIL if > 1.0.

Pre-registered HARD prerequisites:
    - W2 C9  (S86-MELLIN-HEAT-KERNEL-INFRA)            verdict = PASS
    - W2 C10 (S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE)  verdict = PASS
    - analytic_zeta(s, L_max) API exposed by C10's _mellin_cone_residue.py

Pre-registered fallback (Method "Prerequisites (HARD)" clause, plan §6):
    "If EITHER C9 or C10 verdict in {FAIL, PRE-REG-INC}, emit
     PRE-REG-INCOMPLETE verdict with audit_sha256 derived from input pin map
     (do NOT compute the route; do NOT substitute a different scheme)."

This script implements the PRE-REG-INC path: it
    (1) reads the C9 and C10 verdict lines from
        computations/session-86/s86_gate_verdicts.txt,
    (2) detects that C9 = FAIL (orchestrator-confirmed at line 95),
    (3) builds the canonical input-pin map (canonical_constants.py SHA +
        C9 sha256 + C10 sha256 + machinery pins from plan §7),
    (4) derives audit_sha256 deterministically from a sorted-JSON
        serialization of the pin map,
    (5) computes content_sha256 over the .npz output payload,
    (6) appends the canonical verdict line (PRE-REG-INC, value=N/A) and
        the dual-SHA companion comment row (W9a-99 template) to
        computations/session-86/s86_gate_verdicts.txt.

The route's substitution chain (plan §W10-1 §10) is the route's
specification; it is NOT executed because the C9 prerequisite blocks
the analytic_zeta(s, L_max) API on which the chain depends. Per
.claude/rules/math-scripts.md, PRE-REG-INC is a valid pre-registered
outcome (a fired pre-registration clause); attempting to substitute a
different scheme to recover PASS would be S78 Class-6 iterate-until-PASS
(see .claude/rules/v3-closure-recovery.md PROHIBITED_ACTIONS #2).

Substrate-framing: mu_BC is the substrate's EW-sector boundary-condition
spectral object. The integer-12 exponent governs EW exponential stretch
under tau_fold transit. The PRE-REG-INC verdict reflects a methodology
gap (Mellin-cone residue infra unfinished), NOT a substrate-physical
defect of the integer-12 ansatz. Re-attempt is queued for S87 contingent
on Mellin-cone infra repair.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU adequate; no >=100x100 ops

import numpy as np

# Canonical constants (S34+ MANDATORY)
THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
from canonical_constants import tau_fold, M_Z  # noqa: E402

# ----- Paths -----
PROJECT_ROOT = THIS_DIR.parent
VERDICTS_PATH = THIS_DIR / "s86_gate_verdicts.txt"
CANON_CONSTS_PATH = THIS_DIR / "canonical_constants.py"
NPZ_OUT = THIS_DIR / "s86_w10_mu_bc_zeta_interior.npz"

GATE_ID = "S86-MU-BC-V2-ZETA-AT-INTERIOR"
SCHEME = "zeta-at-interior"
CONVENTION = "Mellin-cone-strip-d=8"
L_MAX_CANON = 10  # (local) plan-pinned canonical L_max


# ----- Helpers -----

def file_sha256(path: Path) -> str:
    """SHA-256 hexdigest of a file's bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_verdict_sha(path: Path, gate_id: str) -> str:
    """Extract the sha256= field from the canonical verdict line for gate_id.

    Looks for a line of the form
        {gate_id}: <STATUS> -- ... sha256=<64-hex>
    in the verdict file. Returns the 64-char hexdigest or raises if not found.
    """
    if not path.exists():
        raise FileNotFoundError(f"verdict file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith(f"{gate_id}:"):
                # Tolerate the canonical "sha256=<hex>" suffix
                tag = "sha256="
                idx = line.rfind(tag)
                if idx == -1:
                    raise ValueError(
                        f"verdict line for {gate_id} lacks sha256 pin: {line!r}"
                    )
                sha = line[idx + len(tag):].strip().split()[0]
                if len(sha) != 64 or any(c not in "0123456789abcdef" for c in sha):
                    raise ValueError(
                        f"verdict line for {gate_id} has malformed sha256: {sha!r}"
                    )
                return sha
    raise LookupError(f"no canonical verdict line for {gate_id} in {path}")


def parse_verdict_status(path: Path, gate_id: str) -> str:
    """Return the verdict status token (PASS / FAIL / INFO / PRE-REG-INC)."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(f"{gate_id}:"):
                # form: "{GATE}: STATUS -- value=..."
                rhs = line.split(":", 1)[1].strip()
                # Some PRE-REG-INC tokens contain a hyphen — split on first " --"
                token = rhs.split("--", 1)[0].strip()
                return token
    raise LookupError(f"no canonical verdict line for {gate_id} in {path}")


def deterministic_sha256(obj) -> str:
    """SHA-256 of canonical sorted-JSON serialization (UTF-8)."""
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


# ----- 1. Echo input SHAs (mandatory in first 20 stdout lines) -----

print("=" * 70)
print(f"GATE: {GATE_ID}")
print(f"SCRIPT: {Path(__file__).name}")
print(f"PYTHON: {sys.executable}")
print("-" * 70)
print("Input pins (SHA-256):")

canon_consts_sha = file_sha256(CANON_CONSTS_PATH)
print(f"  canonical_constants.py        : {canon_consts_sha}")

# Prereq verdict SHAs (read from canonical verdict file)
c9_sha = parse_verdict_sha(VERDICTS_PATH, "S86-MELLIN-HEAT-KERNEL-INFRA")
c10_sha = parse_verdict_sha(VERDICTS_PATH, "S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE")
c9_status = parse_verdict_status(VERDICTS_PATH, "S86-MELLIN-HEAT-KERNEL-INFRA")
c10_status = parse_verdict_status(VERDICTS_PATH, "S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE")
print(f"  W2 C9  S86-MELLIN-HEAT-KERNEL-INFRA           : {c9_sha} [{c9_status}]")
print(f"  W2 C10 S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE : {c10_sha} [{c10_status}]")
print("-" * 70)
print(f"Canonical constants used:")
print(f"  tau_fold = {tau_fold!r}")
print(f"  M_Z      = {M_Z!r}")
print("=" * 70)


# ----- 2. Pre-registered prerequisite check -----
# Plan §6 Method, "Prerequisites (HARD)" clause:
#   If EITHER C9 or C10 verdict in {FAIL, PRE-REG-INC}, emit PRE-REG-INC.

PREREQ_BLOCK_STATES = {"FAIL", "PRE-REG-INC", "PRE-REG-INCOMPLETE"}
prereq_block = (c9_status in PREREQ_BLOCK_STATES) or (c10_status in PREREQ_BLOCK_STATES)
which_blocked = []
if c9_status in PREREQ_BLOCK_STATES:
    which_blocked.append(f"W2 C9 = {c9_status}")
if c10_status in PREREQ_BLOCK_STATES:
    which_blocked.append(f"W2 C10 = {c10_status}")

PREREG_INC_REASON = (
    "W2 C9 (S86-MELLIN-HEAT-KERNEL-INFRA) FAIL "
    "(value=9.455686e+00, scheme=MB-Connes-Moscovici, "
    "sha256=1559e559208db268580961556082122cc4d97d73bb01a98c056cdde404155544) "
    "blocks the analytic_zeta(s, L_max) API on which the zeta-at-interior "
    "route depends. Per plan §6 Method 'Prerequisites (HARD)' clause: "
    "the route is NOT computed; PRE-REG-INC verdict is emitted with "
    "audit_sha256 derived from input pin map. Re-attempt queued for S87 "
    "contingent on Mellin-cone infrastructure repair."
)

if not prereq_block:
    # Defensive: this path should not fire under the orchestrator-confirmed
    # runtime status. If both prereqs are PASS, this script is the wrong
    # entry point — refuse to proceed with a route the agent did not implement.
    raise RuntimeError(
        "Both W2 C9 and W2 C10 verdicts cleared — "
        "PRE-REG-INC clause does not apply. The zeta-at-interior route "
        "compute path was not implemented in this scaffold. Re-dispatch "
        "with the full route once the Mellin-cone infra is live."
    )


# ----- 3. Build the canonical input-pin map (machinery pins from plan §7) -----

machinery_pins = {
    "L_max": 10,
    "L_max_cross_check": [8, 12],
    "scheme": SCHEME,
    "convention": CONVENTION,
    "n_eval_delta_strip": 0.5,
    "delta_strip_robustness_scan": [0.3, 0.5, 0.7],
    "scan_range_tau_fold": [0.190],
    "tolerance_rule": "RATIO 1e-3 PASS / 1.0 INFO band / >1.0 FAIL",
    "random_seed": "N/A (deterministic analytic continuation)",
    "GPU_path": "CPU; OMP_NUM_THREADS=8; no >=100x100 ops",
    "cutoff_axis": "spectral",
    "s_interior_canonical": 3.5,
    "d_spec": 8,
}

input_pin_map = {
    "gate_id": GATE_ID,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max_canonical": L_MAX_CANON,
    "tau_fold": tau_fold,
    "M_Z": M_Z,
    "canonical_constants_sha256": canon_consts_sha,
    "prereq_C9_S86-MELLIN-HEAT-KERNEL-INFRA": {
        "verdict": c9_status,
        "sha256": c9_sha,
    },
    "prereq_C10_S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE": {
        "verdict": c10_status,
        "sha256": c10_sha,
    },
    "machinery_pins": machinery_pins,
    "pre_registered_outcome_clause": (
        "plan-w10.md §W10-1 Method 'Prerequisites (HARD)': "
        "If EITHER C9 or C10 verdict in {FAIL, PRE-REG-INC}, emit "
        "PRE-REG-INCOMPLETE verdict with audit_sha256 derived from input "
        "pin map; do NOT compute the route; do NOT substitute a different "
        "scheme."
    ),
    "outcome_clause_fired": True,
    "outcome": "PRE-REG-INC",
    "blocked_by": which_blocked,
}

audit_sha256 = deterministic_sha256(input_pin_map)
print(f"audit_sha256 (sorted-JSON of input_pin_map): {audit_sha256}")


# ----- 4. Build the .npz output payload + content_sha256 -----

payload_dict = {
    "gate_id": GATE_ID,
    "verdict": "PRE-REG-INC",
    "value": "N/A",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max": L_MAX_CANON,
    "tau_fold": float(tau_fold),
    "M_Z_GeV": float(M_Z),
    "prereq_status_map": {
        "C9_S86-MELLIN-HEAT-KERNEL-INFRA": c9_status,
        "C10_S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE": c10_status,
    },
    "prereq_sha_map": {
        "C9_S86-MELLIN-HEAT-KERNEL-INFRA": c9_sha,
        "C10_S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE": c10_sha,
    },
    "input_pin_map": input_pin_map,
    "machinery_pins": machinery_pins,
    "pre_reg_inc_reason": PREREG_INC_REASON,
    "route_spec_reference": (
        "sessions/session-plan/session-86-plan-w10.md §W10-1 §10 "
        "(substitution chain n_exp = -2 * Re[ ln(analytic_zeta(s=3.5, "
        "L_max=10)) ] / tau_fold)"
    ),
    "s87_carry_forward_recommendation": (
        "Re-attempt S86-MU-BC-V2-ZETA-AT-INTERIOR after S87 Mellin-cone "
        "residue infrastructure repair lands (succeed-prerequisite chain: "
        "S86-MELLIN-HEAT-KERNEL-INFRA -> PASS, then "
        "S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE -> PASS, then expose "
        "analytic_zeta(s, L_max) API in _mellin_cone_residue.py)."
    ),
}

# Canonical content_sha256: SHA-256 of the payload's sorted-JSON
# serialization (mirrors the audit hash shape so the .npz is checkable
# without numpy).
content_sha256 = deterministic_sha256(payload_dict)
print(f"content_sha256 (sorted-JSON of payload): {content_sha256}")

# Save .npz with both numerical (none) and structured-text fields. Numpy
# tolerates Python objects via dtype=object; we use that for the nested
# dicts to keep round-trip readability.
np.savez(
    NPZ_OUT,
    gate_id=np.array(GATE_ID),
    verdict=np.array("PRE-REG-INC"),
    value=np.array("N/A"),
    scheme=np.array(SCHEME),
    convention=np.array(CONVENTION),
    L_max=np.array(L_MAX_CANON),
    tau_fold=np.array(float(tau_fold)),
    M_Z_GeV=np.array(float(M_Z)),
    canonical_constants_sha256=np.array(canon_consts_sha),
    prereq_status_map_json=np.array(json.dumps(payload_dict["prereq_status_map"])),
    prereq_sha_map_json=np.array(json.dumps(payload_dict["prereq_sha_map"])),
    input_pin_map_json=np.array(json.dumps(input_pin_map, sort_keys=True)),
    machinery_pins_json=np.array(json.dumps(machinery_pins, sort_keys=True)),
    pre_reg_inc_reason=np.array(PREREG_INC_REASON),
    route_spec_reference=np.array(payload_dict["route_spec_reference"]),
    s87_carry_forward=np.array(payload_dict["s87_carry_forward_recommendation"]),
    content_sha256=np.array(content_sha256),
    audit_sha256=np.array(audit_sha256),
)
print(f"NPZ written: {NPZ_OUT}")


# ----- 5. Final non-verdict 4-tuple line (canonical) -----

print(
    f"(value=N/A, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_CANON})"
)


# ----- 6. Append canonical verdict line + dual-SHA companion row -----
# Per .claude/rules/gate-verdicts.md S81+ canonical form and W9a-99
# dual-SHA template. Append-only, mtime-race-safe single open in "a" mode.

verdict_line = (
    f"{GATE_ID}: PRE-REG-INC -- value=N/A "
    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_CANON} "
    f"sha256={content_sha256}"
)
companion_line = (
    f"# {GATE_ID} dual-SHA: "
    f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
    f"schema_version=R3"
)

with open(VERDICTS_PATH, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
    f.write(companion_line + "\n")

print("=" * 70)
print("VERDICT LINE APPENDED:")
print(verdict_line)
print(companion_line)
print("=" * 70)

# Exit 0 — verdict is data; PRE-REG-INC is a valid pre-registered outcome
# (math-scripts.md "All Results Are Good Results"). Script ran cleanly.
sys.exit(0)
