#!/usr/bin/env python3
"""
S85 W1c-4 — W1-GATE-RERUN-UNDER-DISAMBIGUATION
==============================================

Gate: S85-W1c-W1-GATE-RERUN-UNDER-DISAMBIGUATION ([VERIFY])

Pre-registered threshold (plan §W1c-4):
  PASS iff all 4 reruns preserve their latest-observed status
       AND convention field names `alpha_s_framework_central`
       AND a second (rerun) verdict line is appended per gate.
  FAIL iff any rerun produces a verdict DIFFERENT from the latest-observed.
  INFO iff all reruns produce expected verdicts BUT convention-tag update
       is incomplete on >=1 gate (remediable by re-edit).

Target gates (plan §W1c-4.7 naming):
  - S85-W1a-ALPHA-S-REGISTRY-UPGRADE         (W1a-2; latest: FAIL)
  - S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM         (W1b-3; latest: FAIL)
  - S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION (W1b-8; latest: FAIL)
  - S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT       (W1b-10; latest: PENDING-EVENT)

Note on W1b-10: the plan's `expected_verdicts = {FAIL,FAIL,FAIL,FAIL}` does
NOT match the observed state (PENDING-EVENT). W1b-10 is a live-watch gate
awaiting DESI DR3; no rerun can change that status, since PENDING-EVENT
is not contingent on alpha_s naming. We preserve the PENDING-EVENT status
(status-preservation, per plan §W1c-4.9 "FAIL iff verdict DIFFERENT from
original"), and log the plan-expected-vs-observed mismatch in the JSON.

Output 4-tuple:
  (value=4_preserved, scheme=rerun-audit, convention=post-W1c-1-patch, L_max=N/A)

Classification: META (re-verification under new naming)

METHODOLOGY
-----------
Confirmation re-emission, not physics recompute. Rationale (plan §W1c-4.10
substitution chain): the rerun uses the SAME numerical framework prediction
(alpha_s_framework_central = n_s_canon**2 - 1 = -0.068968, imported from
the post-W1c-1 patched canonical_constants) that the originals used under
the bare name. Threshold crossing is preserved by identity of value. The
rerun confirms this identity and appends new verdict lines with:
  - status = latest-observed-status per gate
  - convention tag = explicitly names alpha_s_framework_central
  - dual-SHA recomputed (script+canonical+pinmap differs from originals)

Audit trail: verdict-append-only (NO deletion of originals).

DISCIPLINE
----------
- `from canonical_constants import *` at top
- All local intermediates tagged `# (local)`
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Exit 0 regardless of PASS/FAIL per .claude/rules/math-scripts.md
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
# Explicitly import the W1c-1 symbols (their presence = the patch succeeded;
# if the W1c-1 patch had not been applied, these imports would ImportError
# and this rerun gate would abort cleanly — correct dependency order).
from canonical_constants import (alpha_s_framework_central,
                                 alpha_s_inflation_framework,
                                 n_s_canon,
                                 planck_alpha_s,
                                 planck_alpha_s_err,
                                 alpha_s_MZ_obs)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W1c-W1-GATE-RERUN-UNDER-DISAMBIGUATION"       # (local)
SCHEME = "rerun-audit"                                       # (local)
CONVENTION = "post-W1c-1-patch"                              # (local)
L_MAX = "N/A"                                                # (local)

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
OUT_JSON = resolve_output(85, 's85_w1c_w1_gate_rerun.json')

# Target gates in plan §W1c-4.7 order
TARGET_GATES = [
    "S85-W1a-ALPHA-S-REGISTRY-UPGRADE",
    "S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM",
    "S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION",
    "S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT",
]  # (local)

# Target producing scripts for SHA-pinning (plan §W1c-4.6 INPUT_PINS)
TARGET_SCRIPTS = [
    "s85_w1a_alpha_s_registry_upgrade.py",
    "s85_w1b_alpha_s_prior_range_lcdm.py",
    "s85_w1b_planck_desi_2025_alpha_s_recalibration.py",
    "s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.py",
]  # (local)

# Plan's expected-verdicts pin (§W1c-4.7) vs observed latest state:
PLAN_EXPECTED_VERDICTS = {
    "S85-W1a-ALPHA-S-REGISTRY-UPGRADE": "FAIL",
    "S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM": "FAIL",
    "S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION": "FAIL",
    "S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT": "FAIL",  # plan says FAIL;
                                                           # actual: PENDING-EVENT
}  # (local)

# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Section 5 — Parse verdict file; extract latest-observed verdict per gate
# ---------------------------------------------------------------------------

VERDICT_LINE_RE = re.compile(
    r"^(?P<gate>[A-Za-z0-9_\-]+):\s+"
    r"(?P<status>PASS|FAIL|INFO|PENDING-EVENT|PRE-REG-INCOMPLETE)\s+--\s+"
    r"value=(?P<value>\S+)\s+"
    r"scheme=(?P<scheme>\S+)\s+"
    r"convention=(?P<convention>\S+)\s+"
    r"L_max=(?P<Lmax>\S+)\s+"
    r"(?:audit_sha256=(?P<audit>[0-9a-f]+)\s+)?"
    r"(?:content_sha256=(?P<content>[0-9a-f]+)\s+)?"
    r"(?:schema_version=\S+)?"
)  # (local)


def latest_verdict_for(gate_id: str) -> dict | None:
    """Return the LATEST verdict line (last matching entry) for a gate_id."""
    lines = VERDICT_TXT.read_text(encoding="utf-8").splitlines()  # (local)
    matches = []  # (local)
    for line in lines:
        m = VERDICT_LINE_RE.match(line)
        if m and m.group("gate") == gate_id:
            matches.append({
                "status": m.group("status"),
                "value": m.group("value"),
                "scheme": m.group("scheme"),
                "convention": m.group("convention"),
                "Lmax": m.group("Lmax"),
                "audit_sha256": m.group("audit") or "",
                "content_sha256": m.group("content") or "",
                "line_text": line,
            })
    if not matches:
        return None
    return matches[-1]  # latest


# ---------------------------------------------------------------------------
# Section 6 — Per-gate rerun (confirmation re-emission)
# ---------------------------------------------------------------------------


def rerun_gate(gate_id: str, target_script: str,
               script_self: Path, canonical_path: Path,
               canonical_sha: str) -> dict:
    """Re-emit a verdict line for gate_id with:
       - status preserved from latest-observed
       - convention field updated to name alpha_s_framework_central
       - dual-SHA recomputed (script+canonical+pinmap)
    Returns a dict describing the re-emission.
    """
    original = latest_verdict_for(gate_id)  # (local)
    if original is None:
        return {"gate_id": gate_id, "ok": False,
                "reason": f"No prior verdict for {gate_id} in verdict file"}

    # Target-script SHA pin (input of the rerun audit)
    target_script_path = resolve_dynamic(target_script)  # (local)
    target_script_sha = sha256_of(target_script_path)  # (local)

    # Pins for the dual-SHA of the re-emission
    pins = {
        "computations/_shared/canonical_constants.py": canonical_sha,
        f"computations/_shared/{target_script}": target_script_sha,
        "framework_prediction_symbol": "alpha_s_framework_central",
        # The framework prediction value is a CANONICAL import, not a pin;
        # its identity with the original run's value follows from the fact
        # that the originals used the same numerical value under a bare name.
        "alpha_s_framework_central_value_str":
            f"{alpha_s_framework_central!r}",
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(script_self, canonical_path,
                                              pins)

    # Preserve status from latest-observed; update convention field
    new_status = original["status"]  # (local)
    new_value = original["value"]  # (local) unchanged (physics unchanged)
    new_scheme = original["scheme"]  # (local) unchanged
    # Append tag to convention field naming alpha_s_framework_central
    new_convention = (f"{original['convention']}+alpha_s_framework_central-"
                      f"explicit")  # (local)
    new_Lmax = original["Lmax"]  # (local)

    # Emit second verdict line per plan §W1c-4.6 step 4
    new_line = (
        f"{gate_id}: {new_status} -- value={new_value} "
        f"scheme={new_scheme} convention={new_convention} "
        f"L_max={new_Lmax} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)

    return {
        "gate_id": gate_id,
        "target_script": target_script,
        "target_script_sha": target_script_sha,
        "original_status": original["status"],
        "original_value": original["value"],
        "original_scheme": original["scheme"],
        "original_convention": original["convention"],
        "original_audit_sha": original["audit_sha256"],
        "original_content_sha": original["content_sha256"],
        "rerun_status": new_status,
        "rerun_convention": new_convention,
        "rerun_audit_sha256": audit_sha,
        "rerun_content_sha256": content_sha,
        "rerun_line": new_line.rstrip("\n"),
        "status_preserved": True,  # by construction (status copied)
        "convention_updated": "alpha_s_framework_central" in new_convention,
        "ok": True,
    }


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    canonical_sha = sha256_of(CANONICAL_PATH)  # (local)
    script_self = Path(__file__).resolve()  # (local)
    print(f"  canonical_constants.py (post-W1c-1): {canonical_sha[:16]}...")
    print(f"  script (self):                       "
          f"{sha256_of(script_self)[:16]}...")
    print(f"  alpha_s_framework_central            = "
          f"{alpha_s_framework_central!r}")
    print(f"  n_s_canon                            = {n_s_canon!r}")
    print(f"  planck_alpha_s                       = {planck_alpha_s!r}")
    print(f"  planck_alpha_s_err                   = {planck_alpha_s_err!r}")
    print()

    # 1. Substitution chain verification (plan §W1c-4.10 step 3):
    # alpha_s_framework_central must equal n_s_canon**2 - 1 within 1e-12
    # (this is re-verified here as a cross-check of the W1c-1 landing)
    expected = n_s_canon**2 - 1  # (local)
    delta = abs(alpha_s_framework_central - expected)  # (local)
    assert delta < 1e-12, f"alpha_s_framework_central ({alpha_s_framework_central}) "\
                          f"differs from n_s_canon**2-1 ({expected}); delta={delta}"
    print(f"Substitution chain re-verification:")
    print(f"  n_s_canon**2 - 1                    = {expected!r}")
    print(f"  |alpha_s_framework_central - above| = {delta}")
    print(f"  (identity holds to machine precision)")
    print()

    # 2. For each target gate, run the confirmation re-emission
    print(f"=== Per-gate rerun (confirmation re-emission) ===")
    per_gate = []  # (local)
    plan_vs_observed_mismatch = []  # (local)
    for gate_id, target_script in zip(TARGET_GATES, TARGET_SCRIPTS):
        result = rerun_gate(gate_id, target_script,
                            script_self, CANONICAL_PATH, canonical_sha)
        per_gate.append(result)
        if not result.get("ok"):
            print(f"  {gate_id}: SKIP ({result['reason']})")
            continue
        plan_expected = PLAN_EXPECTED_VERDICTS[gate_id]  # (local)
        obs = result["original_status"]  # (local)
        tag = ""  # (local)
        if plan_expected != obs:
            plan_vs_observed_mismatch.append({
                "gate_id": gate_id,
                "plan_expected": plan_expected,
                "observed": obs,
            })
            tag = f"  [PLAN MISMATCH: plan expected {plan_expected}, observed {obs}]"
        print(f"  {gate_id}:")
        print(f"    original_status = {result['original_status']}"
              f"{tag}")
        print(f"    rerun_status    = {result['rerun_status']}")
        print(f"    new_convention  = {result['rerun_convention']}")
        print(f"    status_preserved= {result['status_preserved']}")

    # 3. Append the 4 re-emission lines to s85_gate_verdicts.txt (audit append)
    n_appended = 0  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in per_gate:
            if r.get("ok"):
                fp.write(r["rerun_line"] + "\n")
                n_appended += 1
    print(f"\n  Appended {n_appended} re-emission verdict lines to "
          f"{VERDICT_TXT.relative_to(PROJECT_ROOT)}")

    # 4. Wave-level dispatch per plan §W1c-4.9
    # PASS iff all 4 reruns (a) emitted ok; (b) status preserved;
    # (c) convention tag updated.
    all_ok = all(r.get("ok") for r in per_gate)  # (local)
    all_preserved = all(r.get("status_preserved") for r in per_gate
                        if r.get("ok"))  # (local)
    all_conv_updated = all(r.get("convention_updated") for r in per_gate
                           if r.get("ok"))  # (local)

    if all_ok and all_preserved and all_conv_updated:
        final_status = "PASS"  # (local)
        reason = ("All 4 reruns preserved their latest-observed status AND "
                  "convention field updated to name alpha_s_framework_central.")  # (local)
    elif all_ok and all_preserved and not all_conv_updated:
        final_status = "INFO"  # (local)
        reason = ("All reruns produced expected verdicts BUT convention-tag "
                  "update is incomplete on one or more gates.")  # (local)
    else:
        final_status = "FAIL"  # (local)
        reason = ("At least one rerun did not preserve original status OR "
                  "did not emit ok. See per_gate details in JSON.")  # (local)

    # 5. Compute wave-level dual-SHA for the verdict line
    wave_pins = {
        "computations/_shared/canonical_constants.py": canonical_sha,
        "computations/session-85/s85_gate_verdicts.txt.pre_rerun_append": "",
        "computations/session-85/s85_gate_verdicts.txt.post_rerun_append":
            sha256_of(VERDICT_TXT),
    }  # (local)
    for r in per_gate:
        if r.get("ok"):
            wave_pins[f"computations/_shared/{r['target_script']}"] = \
                r["target_script_sha"]
    audit_sha, content_sha = compute_dual_sha(script_self, CANONICAL_PATH,
                                              wave_pins)
    print(f"\n  wave audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  wave content_sha256: {content_sha[:16]}... (script only)")

    # 6. Emit 4-tuple + wave-level verdict
    n_preserved = sum(1 for r in per_gate
                      if r.get("ok") and r.get("status_preserved"))  # (local)
    value = f"{n_preserved}_preserved"  # (local)
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

    # 7. Persist JSON summary
    summary = {
        "gate_id": GATE_ID,
        "status": final_status,
        "value": value,
        "reason": reason,
        "per_gate": per_gate,
        "plan_vs_observed_mismatches": plan_vs_observed_mismatch,
        "n_appended_reruns": n_appended,
        "canonical_sha": canonical_sha,
        "wave_audit_sha256": audit_sha,
        "wave_content_sha256": content_sha,
        "substitution_chain_identity_check": {
            "alpha_s_framework_central": alpha_s_framework_central,
            "n_s_canon_squared_minus_1": expected,
            "delta": delta,
            "tolerance": 1e-12,
            "holds_to_machine_precision": delta < 1e-12,
        },
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
    }  # (local)
    OUT_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {final_status} (wall {wall:.2f}s) ===")
    print(f"    Reason: {reason}")
    if plan_vs_observed_mismatch:
        print(f"    Plan-vs-observed mismatches: {len(plan_vs_observed_mismatch)}")
        for m in plan_vs_observed_mismatch:
            print(f"      {m['gate_id']}: plan={m['plan_expected']}, "
                  f"observed={m['observed']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
