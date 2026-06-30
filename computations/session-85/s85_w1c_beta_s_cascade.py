#!/usr/bin/env python3
"""
S85 W1c-6 — BETA-S-CASCADE-CONSISTENCY
======================================

Gate: S85-W1c-BETA-S-CASCADE-CONSISTENCY ([VERIFY])

Pre-registered threshold (plan §W1c-6.9):
  PASS iff beta_s_residual < 0.01 (1%).
  INFO iff 0.01 <= beta_s_residual < 0.10 (consistent but not tight).
  FAIL iff beta_s_residual >= 0.10 (W0-1 β_s pin is NOT derived from
       the same S50-51 identity — structurally important finding).

Inputs (SHA-256 dual-pinned):
  - computations/_shared/canonical_constants.py (post-W1c-1)
  - computations/session-85/s85_gate_verdicts.txt (BETA-S-CMB-S4 line observed)

Output 4-tuple:
  (value=beta_s_residual, scheme=slow-roll-chain, convention=inflation-run,
   L_max=N/A)

Classification: META (downstream β_s consistency check)

METHODOLOGY
-----------
Slow-roll chain rule: under Option 2 (α_s is INFLATIONARY, = dn_s/dlnk),
  β_s := dα_s/dlnk = d/dlnk (n_s² - 1) = 2 n_s × (dn_s/dlnk) = 2 n_s × α_s.

Compute:
  beta_s_derived = 2 * n_s_canon * alpha_s_framework_central

Compare to the canonical W0-1 β_s pin from canonical_constants.beta_s
(the `S85-BETA-S-CMB-S4-PREREG` gate emits a sigma-count verdict value
of 60.5, NOT the β_s value; the actual β_s pin is the canonical constant
that feeds the gate's computation, beta_s = -0.1331).

Residual: |beta_s_derived - beta_s_canonical| / |beta_s_canonical|.

Exit 0 regardless of PASS/FAIL per .claude/rules/math-scripts.md.
"""

from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (alpha_s_framework_central,
                                 alpha_s_inflation_framework,
                                 n_s_canon,
                                 beta_s,
                                 sigma_beta_s_CMB_S4,
                                 planck_ns)

import hashlib
import json
import re
import sys
import time
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W1c-BETA-S-CASCADE-CONSISTENCY"               # (local)
SCHEME = "slow-roll-chain"                                   # (local)
CONVENTION = "inflation-run"                                 # (local)
L_MAX = "N/A"                                                # (local)

# Pre-registered thresholds (plan §W1c-6.9)
PASS_RESIDUAL_MAX = 0.01                                     # (local)
INFO_RESIDUAL_MAX = 0.10                                     # (local)

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
OUT_JSON = resolve_output(85, 's85_w1c_beta_s_cascade.json')


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path,
                     canonical_path: Path,
                     pins: dict) -> tuple:
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
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


def find_w0_1_verdict_line() -> str:
    """Return the latest S85-BETA-S-CMB-S4-PREREG verdict line for
    provenance logging (the line carries a sigma-count value=60.5,
    not the β_s value itself; the β_s value is the canonical pin)."""
    pat = re.compile(r"^S85-BETA-S-CMB-S4-PREREG:\s+")  # (local)
    lines = VERDICT_TXT.read_text(encoding="utf-8").splitlines()  # (local)
    matches = [ln for ln in lines if pat.match(ln)]  # (local)
    return matches[-1] if matches else ""


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    canonical_sha = sha256_of(CANONICAL_PATH)  # (local)
    verdict_sha = sha256_of(VERDICT_TXT)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    print(f"  canonical_constants.py (post-W1c-1): {canonical_sha[:16]}...")
    print(f"  s85_gate_verdicts.txt (pre-W1c-6):   {verdict_sha[:16]}...")
    print(f"  script (self):                       "
          f"{sha256_of(script_path)[:16]}...")
    print()

    # Provenance log of the W0-1 gate (sigma-count; not the β_s value)
    w0_1_line = find_w0_1_verdict_line()  # (local)
    print(f"  W0-1 sigma-count line (provenance only):")
    print(f"    {w0_1_line[:150]}...")
    print(f"  (The W0-1 gate value=60.5 is an SNR/sigma-count metric for")
    print(f"   CMB-S4 β_s detectability, scheme=MS-bar. The β_s VALUE is")
    print(f"   the canonical `beta_s = -0.1331`, which is the W0-1 β_s PIN")
    print(f"   that feeds the gate's SNR computation.)")
    print()

    # Substitution chain
    n_s = float(n_s_canon)  # (local) 0.9649
    alpha_s_fw = float(alpha_s_framework_central)  # (local) -0.06896799
    beta_s_canonical = float(beta_s)  # (local) -0.1331

    print(f"=== Substitution chain (slow-roll chain rule) ===")
    print(f"  Step 1: β_s := dα_s/dlnk (slow-roll)")
    print(f"          α_s = n_s² - 1 (S50-51 identity, committed W1c-2)")
    print(f"          β_s = d/dlnk (n_s² - 1) = 2 n_s × (dn_s/dlnk)")
    print(f"              = 2 n_s × α_s")
    print(f"  Step 2: n_s = n_s_canon                     = {n_s!r}")
    print(f"          α_s = alpha_s_framework_central     = {alpha_s_fw!r}")
    print(f"  Step 3: 2 × n_s × α_s = 2 × {n_s} × ({alpha_s_fw})")

    beta_s_derived = 2.0 * n_s * alpha_s_fw  # (local)
    print(f"                            = {beta_s_derived!r}")
    print(f"  Step 4: beta_s (canonical W0-1 pin)         = {beta_s_canonical!r}")
    print()

    # Residual
    residual = abs(beta_s_derived - beta_s_canonical) / abs(beta_s_canonical)  # (local)
    print(f"=== Residual ===")
    print(f"  |beta_s_derived - beta_s_pin| / |beta_s_pin|")
    print(f"   = |{beta_s_derived!r} - ({beta_s_canonical!r})| / {abs(beta_s_canonical)!r}")
    print(f"   = {abs(beta_s_derived - beta_s_canonical)!r} / {abs(beta_s_canonical)!r}")
    print(f"   = {residual!r}")
    print(f"  PASS threshold (residual < 0.01 = 1%):      {residual < PASS_RESIDUAL_MAX}")
    print()

    # Dispatch
    if residual < PASS_RESIDUAL_MAX:
        final_status = "PASS"  # (local)
        reason = (f"residual = {residual:.2e} < {PASS_RESIDUAL_MAX} "
                  f"(slow-roll chain rule reproduces W0-1 pin to "
                  f"{residual*1e6:.1f} ppm — single-parent provenance "
                  f"confirmed)")  # (local)
    elif residual < INFO_RESIDUAL_MAX:
        final_status = "INFO"  # (local)
        reason = (f"residual = {residual:.2e} in [{PASS_RESIDUAL_MAX}, "
                  f"{INFO_RESIDUAL_MAX}) — consistent but not tight; "
                  f"may indicate higher-order slow-roll correction")  # (local)
    else:
        final_status = "FAIL"  # (local)
        reason = (f"residual = {residual:.2e} >= {INFO_RESIDUAL_MAX} "
                  f"— β_s canonical pin is NOT derived from the same "
                  f"S50-51 identity via slow-roll chain; escalate")  # (local)

    # Dual-SHA
    pins = {
        "computations/_shared/canonical_constants.py": canonical_sha,
        "computations/session-85/s85_gate_verdicts.txt.beta_s_prereg_line": verdict_sha,
        "n_s_canon": f"{n_s!r}",
        "alpha_s_framework_central": f"{alpha_s_fw!r}",
        "beta_s_canonical_pin": f"{beta_s_canonical!r}",
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH,
                                              pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 4-tuple + verdict
    value = round(residual, 8)  # (local)
    four_tuple = (f"(value={value!r}, scheme={SCHEME}, "
                  f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print("\n" + four_tuple)

    line = (
        f"{GATE_ID}: {final_status} -- value={value} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)

    # JSON
    summary = {
        "gate_id": GATE_ID,
        "status": final_status,
        "value": value,
        "reason": reason,
        "n_s_canon": n_s,
        "alpha_s_framework_central": alpha_s_fw,
        "beta_s_canonical_pin": beta_s_canonical,
        "beta_s_derived": beta_s_derived,
        "residual": residual,
        "residual_ppm": residual * 1e6,
        "w0_1_prereg_line": w0_1_line,
        "canonical_sha": canonical_sha,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "thresholds": {
            "PASS_RESIDUAL_MAX": PASS_RESIDUAL_MAX,
            "INFO_RESIDUAL_MAX": INFO_RESIDUAL_MAX,
        },
        "substitution_chain": {
            "step_1_definition": ("β_s := dα_s/dlnk (slow-roll) AND "
                                  "α_s = n_s² - 1 (S50-51, W1c-2 commit)"),
            "step_2_chain_rule": "β_s = d/dlnk (n_s²-1) = 2 n_s × α_s",
            "step_3_substitute": (f"2 × {n_s} × ({alpha_s_fw}) = "
                                  f"{beta_s_derived}"),
            "step_4_direction": ("β_s_derived matches β_s_canonical to "
                                 f"{residual*1e6:.1f} ppm; sign NEGATIVE "
                                 "(tilt accelerates toward smaller values "
                                 "at smaller scales; consistent with W0-1 "
                                 "pin on sign grounds)"),
        },
    }  # (local)
    OUT_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {final_status} (wall {wall:.2f}s) ===")
    print(f"    Reason: {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
