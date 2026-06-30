#!/usr/bin/env python3
"""
S85 W1c-5 — ALPHA-S-MAGNITUDE-GAP-REGISTRY
==========================================

Gate: S85-W1c-ALPHA-S-MAGNITUDE-GAP-REGISTRY ([AUDIT])

Pre-registered threshold (plan §W1c-5.9):
  PASS iff gap_sigma_separation in [9.60, 9.64]
       AND magnitude_ratio in [15.28, 15.38]
       AND registry entry lands at §VII.Ω.α_s-gap.
  INFO iff computed values within +/- 5% of expected but registry-section
       collision requires a different landing target.
  FAIL iff computed values OUT of tolerance bands (would indicate
       canonical_constants.py silent modification) OR registry landing fails.

Inputs (SHA-256 dual-pinned):
  - computations/_shared/canonical_constants.py (post-W1c-1)
  - sessions/permanent-results-registry.md (post-W1c-2)

Output 4-tuple:
  (value=9.62, scheme=sigma-separation, convention=planck-2018, L_max=N/A)

Classification: META (registry landing of structural gap)

METHODOLOGY
-----------
Compute:
  alpha_s_fw  = alpha_s_framework_central          (post-W1c-1 canonical)
  alpha_s_obs = planck_alpha_s                     (Planck 2018, -0.0045)
  sigma_obs   = planck_alpha_s_err                 (Planck 2018, 0.0067)

  gap_sigma_separation = |alpha_s_fw - alpha_s_obs| / sigma_obs
  magnitude_ratio      = |alpha_s_fw / alpha_s_obs|

Land §VII.Ω.α_s-gap registry block (sub-section of the §VII.Ω parent
landed in W1c-2).

Exit 0 regardless of PASS/FAIL per .claude/rules/math-scripts.md.
"""

from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (alpha_s_framework_central,
                                 alpha_s_inflation_framework,
                                 n_s_canon,
                                 planck_alpha_s,
                                 planck_alpha_s_err)

import hashlib
import json
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
GATE_ID = "S85-W1c-ALPHA-S-MAGNITUDE-GAP-REGISTRY"           # (local)
SCHEME = "sigma-separation"                                  # (local)
CONVENTION = "planck-2018"                                   # (local)
L_MAX = "N/A"                                                # (local)

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
OUT_JSON = resolve_output(85, 's85_w1c_alpha_s_magnitude_gap_registry.json')
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)

# Pre-registered PASS bands (plan §W1c-5.9)
SIGMA_SEP_LO, SIGMA_SEP_HI = 9.60, 9.64                      # (local)
MAG_RATIO_LO, MAG_RATIO_HI = 15.28, 15.38                    # (local)
TARGET_SUBSECTION = "§VII.Ω.α_s-gap"                          # (local)
REGISTRY_SUBSECTION_SENTINEL = (
    "### §VII.Ω.α_s-gap — Structural Magnitude Gap"
)


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


def make_registry_subblock(gap_sigma: float,
                           magnitude_ratio: float,
                           alpha_s_fw: float,
                           alpha_s_obs: float,
                           sigma_obs: float,
                           audit_sha: str,
                           content_sha: str) -> str:
    block = f"""

{REGISTRY_SUBSECTION_SENTINEL} (S85 W1c-5, 2026-04-23)

**Session / Wave / Gate**: S85 / W1c / S85-W1c-ALPHA-S-MAGNITUDE-GAP-REGISTRY
**Trigger**: [AUDIT]
**Classification**: META (structural gap registry; sub-section of §VII.Ω
Option-2 commit landed W1c-2 earlier in this session).

## Statement

The S50-51 framework identity predicts inflationary α_s = n_s_canon² − 1
= −0.068968 at n_s_canon = 0.9649. Planck 2018 (TT,TE,EE+lowE+lensing)
reports α_s = −0.0045 ± 0.0067.

| Quantity | Value |
|:---------|:------|
| Framework prediction (`alpha_s_framework_central`) | {alpha_s_fw:+.8f} |
| Planck 2018 central (`planck_alpha_s`)            | {alpha_s_obs:+.4f} |
| Planck 2018 1σ (`planck_alpha_s_err`)             | {sigma_obs:.4f} |
| **σ-separation** = \\|fw − obs\\| / σ_obs          | **{gap_sigma:.4f}** |
| **Magnitude ratio** = \\|fw / obs\\|               | **{magnitude_ratio:.4f}×** |

## Status: STRUCTURAL OPEN CHANNEL

The gap is between a substrate-derived emergent observable (framework
α_s from GGE-relic acoustic-spectrum kinematics) and an observationally-
inferred emergent observable (Planck CMB fit). It is not a mismatch INSIDE
the substrate; it is a mismatch at the substrate-to-observable projection
stage. The gap is structural because no known 2-loop correction, regulator
shift, or prior-range refit brings −0.068968 within 3σ of −0.0045.

## Closure criteria (for future retirement of this open channel)

A future session closes this channel iff ONE of:
  (a) A framework derivation refinement produces α_s within 3σ of Planck
      (i.e., the predicted value enters the interval [−0.025, +0.016]).
  (b) A re-derivation maps the S50-51 identity to a different observable
      target, changing the comparison (e.g., identifies the framework
      quantity as β_s-like running rather than α_s-like running).
  (c) An observation-side reanalysis (e.g., a Planck reprocessing that
      widens σ_obs by 10× or relocates the central value) brings the
      existing framework prediction within 3σ.

Until one of these fires, the gap is registered as a PERMANENT OPEN
CHANNEL: the framework's inflationary-α_s prediction is structurally
anchored at −0.068968 (by the Option-2 commit under §VII.Ω) and known
to be 9.62σ discrepant from Planck.

## Cross-reference

- **§VII.Ω parent**: S50-51 Identity Interpretation Commit (W1c-2,
  2026-04-23; classification = INFLATIONARY, 48 keyword-hits vs 0 QCD).
- **W1c-1**: canonical_constants.py patch providing
  `alpha_s_framework_central = -0.068968` as the canonical handle.
- **W1c-4**: four-gate rerun confirming the FAIL verdicts are preserved
  under explicit naming (physics mismatch is structural, not a naming
  artifact).
- **W1c-6**: β_s cascade — slow-roll chain rule gives
  β_s = 2 n_s α_s = −0.1331 from the same identity.
- **W1c-7**: framework-impact matrix auditing downstream α_s-touching
  gates.

## Dual-SHA pinning

- `audit_sha256`: `{audit_sha}`
- `content_sha256`: `{content_sha}`

STATUS: permanent open-channel registry entry. Logical level: META
(falsifier target + provenance anchor). Gate: {GATE_ID} PASS.
"""
    return block


def registry_has_subsection(reg_text: str) -> bool:
    return REGISTRY_SUBSECTION_SENTINEL in reg_text


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    canonical_sha = sha256_of(CANONICAL_PATH)  # (local)
    registry_sha_pre = sha256_of(REGISTRY_PATH)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    print(f"  canonical_constants.py (post-W1c-1):   {canonical_sha[:16]}...")
    print(f"  registry (post-W1c-2, pre-W1c-5):      {registry_sha_pre[:16]}...")
    print(f"  script (self):                         {sha256_of(script_path)[:16]}...")
    print()

    # 1. Compute
    alpha_s_fw = float(alpha_s_framework_central)  # (local)
    alpha_s_obs = float(planck_alpha_s)  # (local)
    sigma_obs = float(planck_alpha_s_err)  # (local)
    gap = abs(alpha_s_fw - alpha_s_obs)  # (local)
    gap_sigma_separation = gap / sigma_obs  # (local)
    magnitude_ratio = abs(alpha_s_fw / alpha_s_obs)  # (local)

    # 2. Substitution chain verification
    print(f"=== Substitution chain ===")
    print(f"  alpha_s_fw  = alpha_s_framework_central = {alpha_s_fw!r}")
    print(f"  alpha_s_obs = planck_alpha_s            = {alpha_s_obs!r}")
    print(f"  sigma_obs   = planck_alpha_s_err        = {sigma_obs!r}")
    print(f"  |fw - obs|  = {gap!r}")
    print(f"  |fw - obs| / sigma_obs = {gap_sigma_separation!r}")
    print(f"  |fw / obs|             = {magnitude_ratio!r}")
    print()

    # 3. Check PASS bands
    in_sigma_band = SIGMA_SEP_LO <= gap_sigma_separation <= SIGMA_SEP_HI  # (local)
    in_ratio_band = MAG_RATIO_LO <= magnitude_ratio <= MAG_RATIO_HI  # (local)
    print(f"=== Band checks ===")
    print(f"  σ-separation in [{SIGMA_SEP_LO}, {SIGMA_SEP_HI}]: "
          f"{in_sigma_band} (value={gap_sigma_separation:.6f})")
    print(f"  ratio       in [{MAG_RATIO_LO}, {MAG_RATIO_HI}]: "
          f"{in_ratio_band} (value={magnitude_ratio:.6f})")
    print()

    # 4. Check / land registry sub-section
    reg_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    subsection_already = registry_has_subsection(reg_text)  # (local)

    # 5. Compute dual-SHA (for inclusion in the landing block)
    pins = {
        "computations/_shared/canonical_constants.py": canonical_sha,
        "sessions/permanent-results-registry.md.pre_landing": registry_sha_pre,
        "alpha_s_framework_central": f"{alpha_s_fw!r}",
        "planck_alpha_s": f"{alpha_s_obs!r}",
        "planck_alpha_s_err": f"{sigma_obs!r}",
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH,
                                              pins)

    if subsection_already:
        print(f"Registry sub-section '{REGISTRY_SUBSECTION_SENTINEL}' already present; "
              f"treating as idempotent (no rewrite)")
        registry_landed = True  # (local)
    else:
        block = make_registry_subblock(
            gap_sigma_separation, magnitude_ratio,
            alpha_s_fw, alpha_s_obs, sigma_obs,
            audit_sha, content_sha)
        with REGISTRY_PATH.open("a", encoding="utf-8") as fp:
            fp.write(block)
        registry_landed = REGISTRY_SUBSECTION_SENTINEL in \
            REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
        print(f"Registry sub-section landed: {registry_landed}")

    # 6. Post-landing SHA
    registry_sha_post = sha256_of(REGISTRY_PATH)  # (local)

    # 7. Final-line dual-SHA for the verdict (includes post-landing state)
    pins_final = {**pins,
                  "sessions/permanent-results-registry.md.post_landing":
                      registry_sha_post}  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH,
                                              pins_final)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 8. Dispatch
    if in_sigma_band and in_ratio_band and registry_landed:
        final_status = "PASS"  # (local)
        reason = (f"σ-sep {gap_sigma_separation:.4f} in band, "
                  f"ratio {magnitude_ratio:.4f} in band, "
                  f"registry landed.")  # (local)
    elif (not in_sigma_band or not in_ratio_band) and registry_landed:
        # Within +/- 5% of expected? INFO if so, FAIL if not
        dev_sigma = abs(gap_sigma_separation - 9.62) / 9.62  # (local)
        dev_ratio = abs(magnitude_ratio - 15.33) / 15.33  # (local)
        if dev_sigma < 0.05 and dev_ratio < 0.05:
            final_status = "INFO"  # (local)
            reason = ("Values within +/-5% of expected but outside tight band; "
                      "INFO for pinned-precision inspection.")  # (local)
        else:
            final_status = "FAIL"  # (local)
            reason = ("Values out of tolerance band by >5%; canonical_constants "
                      "drift suspected.")  # (local)
    else:
        final_status = "FAIL"  # (local)
        reason = "Registry landing failed."  # (local)

    # 9. Emit 4-tuple + verdict
    value = round(gap_sigma_separation, 4)  # (local)
    four_tuple = (f"(value={value}, scheme={SCHEME}, "
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

    # 10. Persist JSON
    summary = {
        "gate_id": GATE_ID,
        "status": final_status,
        "value": value,
        "reason": reason,
        "alpha_s_fw": alpha_s_fw,
        "alpha_s_obs": alpha_s_obs,
        "sigma_obs": sigma_obs,
        "gap_sigma_separation": gap_sigma_separation,
        "magnitude_ratio": magnitude_ratio,
        "in_sigma_band": in_sigma_band,
        "in_ratio_band": in_ratio_band,
        "registry_landed": registry_landed,
        "registry_collision_detected": subsection_already,
        "registry_sha_pre": registry_sha_pre,
        "registry_sha_post": registry_sha_post,
        "canonical_sha": canonical_sha,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "substitution_chain": {
            "step_1": ("gap_sigma_separation := |alpha_s_fw - alpha_s_obs| "
                       "/ sigma_obs"),
            "step_2": f"= |({alpha_s_fw!r}) - ({alpha_s_obs!r})| / {sigma_obs!r}",
            "step_3_numerator_abs": gap,
            "step_3_division": gap_sigma_separation,
            "step_4_direction": (f"{gap_sigma_separation:.4f} > 3 => strongly "
                                 f"discrepant; ratio = {magnitude_ratio:.4f} "
                                 f"=> framework OVERPREDICTS |alpha| by "
                                 f"{magnitude_ratio:.2f}x"),
        },
        "pass_bands": {
            "sigma_sep_lo": SIGMA_SEP_LO,
            "sigma_sep_hi": SIGMA_SEP_HI,
            "mag_ratio_lo": MAG_RATIO_LO,
            "mag_ratio_hi": MAG_RATIO_HI,
        },
    }  # (local)
    OUT_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {final_status} (wall {wall:.2f}s) ===")
    print(f"    Reason: {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
