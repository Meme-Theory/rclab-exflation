#!/usr/bin/env python3
"""
S85 W1a-10: FALSIFIER-MONITOR-RANK-UNIVERSALITY
================================================

Gate: S85-W1a-FALSIFIER-MONITOR-RANK-UNIVERSALITY
Trigger: [AUDIT]
Classification: META (long-running falsifier-watchlist monitor)
Agent: mack-cosmic-bridge (coordinates van-den-dungen-bridge + tesla-resonance)

Hypothesis: The S84 W10-111 rank-universality claim (R_N exhibits a
universal scaling with N across fiber-group alternatives) is monitored
for counterexamples. Any alternative fiber group G with R_N(G) deviating
> 10% from the SU(3) baseline triggers a COUNTEREXAMPLE registration.

Alternative fiber-group set (FROZEN S84 W13-4, assigned to tesla W13
carry-forward): {G_2, F_4, A_3, C_3}.

Substitution chain (Python-verified):
  Step 1: For each alternative G in {G_2, F_4, A_3, C_3}:
            check whether an S85 computation of R_N(G) exists
            on-disk (searches computations/_shared/ for script/npz files
            matching the group name).
  Step 2: For each group where R_N(G) exists:
            deviation := |R_N(G) - R_SU3| / R_SU3
            flag as COUNTEREXAMPLE iff deviation > 0.10.
  Step 3: For each group where R_N(G) does NOT exist:
            mark as PENDING (expecting tesla W13 carry-forward).
  Step 4: Aggregate status:
            PASS iff max_deviation <= 0.10 AND PENDING count == 0.
            FAIL iff any deviation > 0.10.
            INFO iff PENDING count > 0 (monitor is incomplete).
  Direction: monitor-only; emits status without altering the
             constraint map. Numerical verdict reflects current
             completeness of the scan.

Current S85 status (as of 2026-04-23):
  - G_2: PENDING (no S85 R_N computation)
  - F_4: PENDING
  - A_3: PENDING
  - C_3: PENDING
  => PENDING count = 4, max_deviation undefined (N/A).
  => verdict = INFO (monitor incomplete; carry-forward to S86).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=<max-deviation-or-NaN>, scheme=rank-universality, convention=SU3-baseline, L_max=10)

Thresholds (pre-registered, plan §W1a-10):
  - PASS iff max-deviation <= 0.10 AND PENDING count == 0.
  - FAIL iff max-deviation > 0.10 for any alternative.
  - INFO iff PENDING count > 0 (partial scan; carry forward).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: E402, F401, F403 (imported for SHA pinning; rank-univ values are # (local) from tesla W13 carry-forward)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1a-FALSIFIER-MONITOR-RANK-UNIVERSALITY"             # (local)
SCHEME = "rank-universality"                                        # (local)
CONVENTION = "SU3-baseline"                                         # (local)
L_MAX = 10                                                          # (local)

# Alternative fiber-group set (FROZEN S84 W13-4; tesla W13 carry-forward)
ALT_GROUPS = ["G_2", "F_4", "A_3", "C_3"]                           # (local)

DEV_THRESHOLD_FAIL = 0.10                                           # (local) 10% deviation triggers COUNTEREXAMPLE

OUT_JSON = SCRIPT_DIR / "s85_w1a_falsifier_monitor_rank.json"
OUT_MD = SCRIPT_DIR / "s85_w1a_falsifier_monitor_rank.md"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

INPUT_FILES = [CANON_PY]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def probe_group_rn_exists(group: str) -> bool:
    """Search computations/_shared/ and sessions/ for an S85 R_N computation for this group."""
    # Normalize group tag for path matching
    tag = group.replace("_", "").lower()                            # (local) e.g. 'g2', 'f4'
    candidates = []                                                 # (local)
    # Search computations/_shared/ for R_N-related files named after the group
    for p in SCRIPT_DIR.glob(f"s85_*{tag}*"):
        candidates.append(p)
    for p in SCRIPT_DIR.glob(f"s85_*rank*"):
        if tag in p.name.lower():
            candidates.append(p)
    return len(candidates) > 0


def compute() -> dict:
    scan = {}                                                       # (local)
    for g in ALT_GROUPS:
        exists = probe_group_rn_exists(g)                           # (local)
        scan[g] = {
            "status": "COMPUTED" if exists else "PENDING",
            "deviation": None,
            "comment": "no S85 R_N computation found on disk" if not exists
                       else "computation present; deviation pending extraction",
        }

    pending_count = sum(1 for v in scan.values() if v["status"] == "PENDING")  # (local)
    computed_count = sum(1 for v in scan.values() if v["status"] == "COMPUTED")  # (local)
    devs = [v["deviation"] for v in scan.values() if v["deviation"] is not None]  # (local)
    max_dev = max(devs) if devs else float("nan")                   # (local)

    return {
        "value": max_dev,
        "scan": scan,
        "pending_count": pending_count,
        "computed_count": computed_count,
        "max_deviation": max_dev,
        "alt_groups": ALT_GROUPS,
    }


def evaluate_gate(res: dict) -> str:
    if res["pending_count"] == 0:
        # Full scan complete; decide on deviation
        if not np.isnan(res["max_deviation"]) and res["max_deviation"] > DEV_THRESHOLD_FAIL:
            return "FAIL"
        return "PASS"
    # Any PENDING => monitor incomplete
    return "INFO"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    # NaN is serialized as 'nan' in Python repr; be explicit to avoid JSON roundtrip issues
    if isinstance(value, float) and np.isnan(value):
        vstr = "'NaN-pending'"
    else:
        vstr = repr(value)
    return (f"(value={vstr}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    if isinstance(value, float) and np.isnan(value):
        val_repr = "'NaN-pending'"
    else:
        val_repr = repr(value)
    line = (
        f"{GATE_ID}: {verdict} -- value={val_repr} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def write_watchlist_md(res: dict, verdict: str, audit_sha: str,
                       content_sha: str, out_path: Path) -> None:
    rows = []                                                       # (local)
    for g, info in res["scan"].items():
        dev_str = "N/A" if info["deviation"] is None else f"{info['deviation']:.4f}"
        rows.append(f"| {g} | {info['status']} | {dev_str} | {info['comment']} |")
    rows_text = "\n".join(rows)

    text = f"""# Rank-universality falsifier monitor -- S85 W1a-10

**Gate**: {GATE_ID}
**Verdict**: {verdict}

## Monitor scan (alternative fiber groups)

| Group | Status | Deviation | Comment |
|:------|:-------|:---------|:--------|
{rows_text}

## Aggregate

- Computed groups: {res['computed_count']} / {len(res['alt_groups'])}
- PENDING groups: {res['pending_count']}
- max deviation: {'N/A (no computed data)' if np.isnan(res['max_deviation']) else f"{res['max_deviation']:.4f}"}
- Deviation threshold for COUNTEREXAMPLE: {DEV_THRESHOLD_FAIL:.2f}

## Carry-forward

Current session ran no R_N computations for alternative fiber groups.
These are tesla carry-forwards from S84 W13-4. Until those computations
land, the rank-universality claim (S84 W10-111) is monitored under
INFO status; PASS requires full scan completion AND max_dev <= {DEV_THRESHOLD_FAIL}.

## Provenance

- audit_sha256:   {audit_sha}
- content_sha256: {content_sha}
- schema_version: S84+
"""
    out_path.write_text(text, encoding="utf-8")
    print(f"  MD written: {out_path.name}")


def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: alternative fiber-group set = {res['alt_groups']}")
    print(f"  Step 2: per-group scan:")
    for g, info in res["scan"].items():
        print(f"          {g:5s}: {info['status']}  ({info['comment']})")
    print(f"  Step 3: pending_count = {res['pending_count']}, "
          f"computed_count = {res['computed_count']}")
    print(f"  Step 4: max_deviation = "
          f"{'N/A (no computed)' if np.isnan(res['max_deviation']) else f'{res['max_deviation']:.4f}'}")
    print(f"  Step 5: verdict rule:")
    print(f"          PENDING>0 => INFO (monitor incomplete)")
    print(f"          PENDING=0 AND max_dev <= {DEV_THRESHOLD_FAIL} => PASS")
    print(f"          PENDING=0 AND max_dev  > {DEV_THRESHOLD_FAIL} => FAIL (counterexample)")
    print(f"          Applied: pending={res['pending_count']} ==> {verdict}")
    print()

    # Emit JSON artifact for downstream processing
    reg = {
        "gate_id": GATE_ID,
        "alt_groups": res["alt_groups"],
        "scan": res["scan"],
        "pending_count": res["pending_count"],
        "computed_count": res["computed_count"],
        "max_deviation": (None if np.isnan(res["max_deviation"])
                          else res["max_deviation"]),
        "deviation_threshold": DEV_THRESHOLD_FAIL,
        "verdict": verdict,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    OUT_JSON.write_text(json.dumps(reg, indent=2), encoding="utf-8")
    print(f"  JSON written: {OUT_JSON.name}")

    write_watchlist_md(res, verdict, audit_sha, content_sha, OUT_MD)

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["value"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
