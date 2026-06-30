#!/usr/bin/env python3
"""
S85 W9-1 — S85-W9-BOREL-FLOOR-REGISTRY-LANDING
==============================================

Gate: S85-W9-BOREL-FLOOR-REGISTRY-LANDING ([VERIFY-THEOREM])

Classification: GEOMETRIC. Borel-summability property of the Jensen-tau
instanton-action spectrum on the D_K-derived effective potential
landscape.

Pre-registered threshold:
  PASS iff (a) fraction == 1.0 over all (tau, mode) points in the
  W10-121 saddle-inventory with S_inst_abs > Borel_threshold_S_inst;
  AND (b) registry entry landed with dual-SHA (post-script manual Edit
  by orchestrator); AND (c) /weave --update confirms entry in
  tools/knowledge.db (post-script manual step by orchestrator).

  This script verifies condition (a) numerically and writes a registry
  patch payload for conditions (b)+(c). (a) is the scientific verdict.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - canonical_constants.py
  - sessions/archive/session-84/computation-artifacts/s84_w10a_121_saddle_inventory.npz
  - (this script bytes → content_sha256)

Output 4-tuple:
  (value=fraction_tau_above_threshold, scheme=W10-121-original,
   convention=Borel-disk-pointwise, L_max=5)

Plan documentation bugs noted and pinned to ACTUAL npz values:
  - Plan said slug `s84_w10_121_borel_floor.npz` → actual
    `sessions/archive/session-84/computation-artifacts/s84_w10a_121_saddle_inventory.npz`
  - Plan said n_tau=61 (tau_step=0.005) → actual n_tau=301 (tau_step=0.001),
    strict superset; dominance direction: 301-pt PASS ⟹ 61-pt PASS.
  - Plan said L_max=10 → actual L_max=5 (the npz was computed at L_max=5;
    this is pinned from the npz payload, not inherited).
  - Plan said registry at sessions/framework/permanent-results-registry.md
    → actual registry at sessions/permanent-results-registry.md
    (canonical-path rule per .claude/rules/gate-verdicts.md).

METHODOLOGY
-----------
Re-read the W10-121 saddle-inventory npz. The npz carries a 301-point
tau_scan over [0.05, 0.35] (finer than the plan-stated 61-pt grid), an
S_inst_table of shape (301, 35) giving the absolute instanton action at
each (tau, mode) point, and scalar reductions min_S_inst_abs and
borel_threshold. The re-audit verifies:

  1. min_S_inst_abs > Borel_threshold_S_inst      [transitive boundedness]
  2. fraction of tau-grid points with per-tau min(S_inst_abs) > threshold
     must be exactly 1.0 (THEOREM, boolean)
  3. Monotonicity across tau is NOT required by the plan — the plan only
     requires that EVERY tau satisfies the bound, which is equivalent to
     the global min bound (1) by definition of min.

If (1)-(3) hold, the gate PASSes. The script emits a registry patch
payload JSON for the orchestrator to apply as §VII.M entry in
sessions/permanent-results-registry.md.

DISCIPLINE
----------
- `from canonical_constants import *` (first import).
- Every local/intermediate is tagged `# (local)`.
- CPU-only (audit-class: re-read scalar comparisons, OMP=4).
- SHA-256 of inputs logged first 20 lines of stdout.
- Dual-SHA (audit_sha256 + content_sha256) emitted per S84+ schema.
- Verdict appended to computations/session-85/s85_gate_verdicts.txt.
- Exit 0 unconditionally on successful compute (math-scripts.md §Exit Codes).
"""

from __future__ import annotations

# --------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# --------------------------------------------------------------------
import os
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

os.environ.setdefault("OMP_NUM_THREADS", "4")
os.environ.setdefault("MKL_NUM_THREADS", "4")

from canonical_constants import *  # noqa: F401,F403
# Named imports for static-analyzer visibility
from canonical_constants import Borel_threshold_S_inst

# --------------------------------------------------------------------
# Section 2 — Standard imports
# --------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
# Section 3 — Paths + pre-registration pins
# --------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                             # (local)
GATE_ID = "S85-W9-BOREL-FLOOR-REGISTRY-LANDING"             # (local)
SCHEME = "W10-121-original"                                 # (local) audit re-read, no re-regulation
CONVENTION = "Borel-disk-pointwise"                         # (local) plan-specified convention label

# L_MAX pinned from the ACTUAL npz payload (plan said 10; npz has 5 — resolve to npz)
# (this is a runtime discovery; we initialize from the plan value and override below)
L_MAX_PLAN = 10                                             # (local) plan-stated (documentation bug)
L_MAX = None                                                # (local) will be set from npz in compute()

PASS_THRESHOLD_FRACTION = 1.0                               # (local) THEOREM; ALL tau-grid points must satisfy bound

# Input artifacts
SADDLE_NPZ = (PROJECT_ROOT / "sessions" / "session-84"
              / "computation-artifacts" / "s84_w10a_121_saddle_inventory.npz")
CANONICAL_PY = resolve_script(None, 'canonical_constants.py')

# Output artifacts
OUT_NPZ = resolve_output(85, 's85_w9_borel_floor_registry.npz')
OUT_PNG = resolve_output(85, 's85_w9_borel_floor_registry.png')
OUT_REGISTRY_PATCH = resolve_output(85, 's85_w9_borel_floor_registry_payload.json')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [
    CANONICAL_PY,
    SADDLE_NPZ,
]


# --------------------------------------------------------------------
# Section 4 — SHA-256 input-pin + dual-SHA closure
# --------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                    # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                               # (local)
    for p in inputs:
        sha = sha256_of(p)                                  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """S84+ dual-SHA closure.
    audit_sha256   = sha256(bytes(script) || bytes(canonical) || pinmap_json)
    content_sha256 = sha256(bytes(script))
    """
    script_bytes = b""                                      # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                   # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                       # (local)

    h_audit = hashlib.sha256()                              # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                             # (local)

    h_content = hashlib.sha256()                            # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                         # (local)
    return audit, content


# --------------------------------------------------------------------
# Section 5 — Compute
# --------------------------------------------------------------------

def compute():
    """Re-audit the W10-121 Borel floor from the saddle-inventory npz."""
    global L_MAX

    if not SADDLE_NPZ.exists():
        raise FileNotFoundError(
            f"W10-121 saddle-inventory npz not found at {SADDLE_NPZ}"
        )

    d = np.load(SADDLE_NPZ, allow_pickle=True)              # (local)

    # Scalar metadata pinned from npz (runtime)
    npz_L_max = int(d["L_max"])                             # (local) actual (npz=5; plan-stated 10)
    L_MAX = npz_L_max
    npz_gate = str(d["gate"])                               # (local)
    npz_scheme = str(d["scheme"])                           # (local) "hessian_eigendirection_scan"
    npz_convention = str(d["convention"])                   # (local) "jensen_tau_wide_mesh"
    npz_seed = int(d["random_seed"])                        # (local)

    # Tau-grid reconstruction
    tau_scan = np.asarray(d["tau_scan"], dtype=float)       # (local) shape (301,)
    n_tau = int(d["n_tau"])                                 # (local) 301
    tau_min = float(d["tau_scan_min"])                      # (local) 0.05
    tau_max = float(d["tau_scan_max"])                      # (local) 0.35
    tau_step_actual = (tau_max - tau_min) / (n_tau - 1)     # (local) 0.001 (plan said 0.005 for 61-pt)

    # S_inst tables
    S_inst_table = np.asarray(d["S_inst_table"], dtype=float)  # (local) shape (301, 35)
    min_S_inst_abs = float(d["min_S_inst_abs"])             # (local) 242091.449
    min_S_inst_relative = float(d["min_S_inst_relative"])   # (local) -8269.23 (signed)
    min_abs_S_inst_relative = float(d["min_abs_S_inst_relative"])  # (local)

    # Borel threshold — pinned from canonical_constants (added S85 W9)
    borel_threshold_canonical = Borel_threshold_S_inst      # (local) 4.34
    borel_threshold_npz = float(d["borel_threshold"])       # (local) 4.34 (cross-check)

    # CONDITION (a): every (tau, mode) point must satisfy S_inst_abs > threshold
    above_mask = S_inst_table > borel_threshold_canonical   # (local) bool (301,35)
    n_total = int(S_inst_table.size)                        # (local) 301*35 = 10535
    n_above = int(above_mask.sum())                         # (local)
    fraction_point = n_above / n_total                      # (local) per-(tau,mode) fraction

    # Per-tau minimum across the 35 modes
    S_inst_min_per_tau = S_inst_table.min(axis=1)           # (local) shape (301,)
    above_per_tau = S_inst_min_per_tau > borel_threshold_canonical  # (local)
    n_tau_above = int(above_per_tau.sum())                  # (local)
    fraction_tau = n_tau_above / n_tau                      # (local) per-tau fraction (target = 1.0)

    # CC1 — W10-121 minimum re-verification at 2.42e5
    cc1_reference = 2.42e5                                  # (local) plan-pinned reference value
    cc1_tol_ratio = 5e-3                                    # (local) 0.5% tolerance on 2.42e5 anchor
    cc1_ratio = min_S_inst_abs / cc1_reference              # (local)
    cc1_rel_dev = abs(min_S_inst_abs - cc1_reference) / cc1_reference  # (local)
    cc1_pass = bool(cc1_rel_dev < cc1_tol_ratio)            # (local)

    # CC2 — monotonicity of per-tau S_inst across the 61-/301-point grid
    # The plan's §10 direction statement only asserts "EVERY tau satisfies
    # bound" (ensured by min bound). Monotonicity of S_inst_min_per_tau(tau)
    # is a STRONGER claim than required for PASS; we report the first-
    # difference sign distribution as a diagnostic, NOT a PASS gate.
    dS_per_tau = np.diff(S_inst_min_per_tau)                # (local)
    n_increasing = int((dS_per_tau > 0).sum())              # (local)
    n_decreasing = int((dS_per_tau < 0).sum())              # (local)
    n_flat = int((dS_per_tau == 0).sum())                   # (local)
    cc2_diagnostic_nondecreasing = (n_decreasing == 0)      # (local) boolean diagnostic

    # Substitution-chain evaluation (mandatory; logs the direction)
    # Definition 1: S_inst(tau, mode) = column-entry of S_inst_table.
    # Definition 2: PASS_a := fraction_tau == 1.0 (ALL tau-grid points
    #               have S_inst_min_per_tau > Borel_threshold).
    # Step 1 (substitute): min_S_inst_abs = 242091.449 = 2.42e5.
    # Step 2 (simplify): 242091.449 / 4.34 = 55781.44 (= borel_threshold_check_absolute).
    #                    log10(242091.449/4.34) = 4.747 ≈ 4.7 OOM.
    # Step 3 (direction): global min > threshold ⟹ every per-tau min >
    #                     threshold ⟹ every (tau, mode) > threshold ⟹
    #                     fraction_tau = 1.0.
    # Step 4 (conclusion): PASS iff fraction_tau == 1.0.
    ratio_min_over_threshold = min_S_inst_abs / borel_threshold_canonical  # (local)
    log10_safety_OOM = float(np.log10(ratio_min_over_threshold))           # (local)

    # Verdict on condition (a)
    condition_a_pass = bool(abs(fraction_tau - PASS_THRESHOLD_FRACTION) < 1e-12)

    # Package
    results = {
        "value": fraction_tau,
        "fraction_point": fraction_point,
        "fraction_tau": fraction_tau,
        "min_S_inst_abs": min_S_inst_abs,
        "min_S_inst_relative": min_S_inst_relative,
        "min_abs_S_inst_relative": min_abs_S_inst_relative,
        "borel_threshold_canonical": borel_threshold_canonical,
        "borel_threshold_npz": borel_threshold_npz,
        "ratio_min_over_threshold": ratio_min_over_threshold,
        "log10_safety_OOM": log10_safety_OOM,
        "cc1_rel_dev": cc1_rel_dev,
        "cc1_pass": cc1_pass,
        "cc1_ratio": cc1_ratio,
        "cc2_nondecreasing_diagnostic": cc2_diagnostic_nondecreasing,
        "n_increasing": n_increasing,
        "n_decreasing": n_decreasing,
        "n_flat": n_flat,
        "condition_a_pass": condition_a_pass,
        "n_tau": n_tau,
        "n_total_points": n_total,
        "n_above_threshold": n_above,
        "n_tau_above_threshold": n_tau_above,
        "tau_scan": tau_scan,
        "S_inst_min_per_tau": S_inst_min_per_tau,
        "tau_min": tau_min,
        "tau_max": tau_max,
        "tau_step_actual": tau_step_actual,
        "L_max_actual": npz_L_max,
        "L_max_plan": L_MAX_PLAN,
        "npz_gate": npz_gate,
        "npz_scheme": npz_scheme,
        "npz_convention": npz_convention,
        "npz_random_seed": npz_seed,
    }
    return results


def evaluate_gate(results):
    """PASS iff condition (a) holds AND CC1 re-verification passes.

    Note: conditions (b) registry-landing and (c) /weave --update are
    operator-applied after the script runs. This script emits condition
    (a) as the scientific verdict; (b)+(c) are orchestrator follow-ups.
    """
    if not results["condition_a_pass"]:
        return "FAIL"
    if not results["cc1_pass"]:
        return "FAIL"
    return "PASS"


# --------------------------------------------------------------------
# Section 6 — Output artifacts
# --------------------------------------------------------------------

def write_npz(results, audit_sha, content_sha):
    to_save = {
        "gate_id": np.array(GATE_ID),
        "scheme": np.array(SCHEME),
        "convention": np.array(CONVENTION),
        "L_max": np.array(results["L_max_actual"]),
        "borel_threshold": np.array(results["borel_threshold_canonical"]),
        "min_S_inst_abs": np.array(results["min_S_inst_abs"]),
        "fraction_tau": np.array(results["fraction_tau"]),
        "fraction_point": np.array(results["fraction_point"]),
        "ratio_min_over_threshold": np.array(results["ratio_min_over_threshold"]),
        "log10_safety_OOM": np.array(results["log10_safety_OOM"]),
        "tau_scan": results["tau_scan"],
        "S_inst_min_per_tau": results["S_inst_min_per_tau"],
        "n_tau": np.array(results["n_tau"]),
        "n_total_points": np.array(results["n_total_points"]),
        "audit_sha256": np.array(audit_sha),
        "content_sha256": np.array(content_sha),
    }
    np.savez_compressed(OUT_NPZ, **to_save)
    print(f"  npz:  {OUT_NPZ.relative_to(PROJECT_ROOT)}")


def write_plot(results):
    tau_scan = results["tau_scan"]                          # (local)
    S_min = results["S_inst_min_per_tau"]                   # (local)
    thr = results["borel_threshold_canonical"]              # (local)

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))            # (local)
    ax.semilogy(tau_scan, S_min, "b-", lw=1.5, label="per-tau min(S_inst_abs)")
    ax.axhline(thr, color="r", ls="--", lw=1.2,
               label=f"Borel threshold = {thr}")
    ax.set_xlabel(r"Jensen deformation parameter $\tau$")
    ax.set_ylabel(r"$\min_{\mathrm{mode}}\ S_{\mathrm{inst,abs}}(\tau)$  (log scale)")
    ax.set_title(f"{GATE_ID}\nmin/threshold = {results['ratio_min_over_threshold']:.2e} "
                 f"({results['log10_safety_OOM']:.2f} OOM safety)")
    ax.legend(loc="best")
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"  png:  {OUT_PNG.relative_to(PROJECT_ROOT)}")


def write_registry_patch(results, audit_sha, content_sha):
    payload = {
        "gate_id": GATE_ID,
        "trigger": "VERIFY-THEOREM",
        "classification": "GEOMETRIC",
        "agent": "feynman-theorist",
        "wave": "S85 W9-1",
        "source_gate": "W10-121 (S84 W10a — tau-kink-inventory-closure)",
        "source_artifact": str(SADDLE_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "theorem_statement": (
            "min_{tau in [0.05, 0.35]} S_inst(tau, mode) = 242091.449 "
            ">> Borel_threshold = 4.34 (4.75 OOM safety margin). The "
            "Jensen-tau instanton-action spectrum on the D_K-derived "
            "effective potential landscape is Borel-summable across the "
            "entire physical scan window; no genuine bound saddle exists "
            "in [0.05, 0.35] at L_max=5."
        ),
        "pass_conditions": {
            "a_fraction_tau_above_threshold": results["fraction_tau"],
            "a_pass": results["condition_a_pass"],
            "cc1_w10_121_reference_match_pct": results["cc1_rel_dev"] * 100.0,
            "cc1_pass": results["cc1_pass"],
        },
        "key_numbers": {
            "min_S_inst_abs": results["min_S_inst_abs"],
            "borel_threshold": results["borel_threshold_canonical"],
            "ratio": results["ratio_min_over_threshold"],
            "log10_safety_OOM": results["log10_safety_OOM"],
            "n_tau_grid": results["n_tau"],
            "n_total_points": results["n_total_points"],
            "tau_scan_range": [results["tau_min"], results["tau_max"]],
            "L_max": int(results["L_max_actual"]),
        },
        "wall_added_to_constraint_map": "W_Borel_tau_[0.05,0.35]_L5",
        "downstream_implications": [
            "Perturbation-theory claims (tree + 1-loop F_amp^3PI, Mukhanov-Sasaki z_R, f_conv Z_R two-loop) are epistemically justified without instanton-contamination concerns inside the physical scan window.",
            "Companion to W2-HARMONIC-NOT-INSTANTON (S_harm = 0.203 < Borel 4.34): together immunize the perturbative ledger against false instanton interpretations and against genuine-instanton intrusions in [0.05, 0.35].",
            "Per-tau scan cache (tau_scan + S_inst_min_per_tau arrays in s85_w9_borel_floor_registry.npz) available for downstream 1/N expansions.",
        ],
        "dual_sha": {
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
        },
        "registry_target": "sessions/permanent-results-registry.md §VII.M (to be appended by orchestrator)",
        "plan_documentation_corrections": [
            "Actual artifact path: sessions/archive/session-84/computation-artifacts/s84_w10a_121_saddle_inventory.npz (plan stated s84_w10_121_borel_floor.npz)",
            f"Actual n_tau: {results['n_tau']} (plan stated 61)",
            f"Actual L_max: {int(results['L_max_actual'])} (plan stated 10)",
            "Actual registry path: sessions/permanent-results-registry.md (plan stated sessions/framework/permanent-results-registry.md)",
            f"Actual npz scheme label: {results['npz_scheme']} (plan convention label Borel-disk-pointwise retained for verdict 4-tuple)",
        ],
    }
    with OUT_REGISTRY_PATCH.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, indent=2)
    print(f"  json: {OUT_REGISTRY_PATCH.relative_to(PROJECT_ROOT)}")


def append_verdict(verdict, value, audit_sha, content_sha):
    """Append S84+ dual-SHA verdict line + companion comment row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    print(f"  verdict appended to {VERDICT_TXT.relative_to(PROJECT_ROOT)}")


# --------------------------------------------------------------------
# Section 7 — Main
# --------------------------------------------------------------------

def main():
    t0 = time.time()                                        # (local)

    # 1. Input-pin SHAs (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)                      # (local)

    # 2. Dual-SHA closure
    script_path = Path(__file__).resolve()                  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_PY, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 3. Compute
    results = compute()
    print(f"  min_S_inst_abs       = {results['min_S_inst_abs']:.3f}")
    print(f"  borel_threshold      = {results['borel_threshold_canonical']}")
    print(f"  ratio (min/thr)      = {results['ratio_min_over_threshold']:.4e}")
    print(f"  log10 safety OOM     = {results['log10_safety_OOM']:.3f}")
    print(f"  fraction_tau         = {results['fraction_tau']}")
    print(f"  fraction_point       = {results['fraction_point']}")
    print(f"  n_tau                = {results['n_tau']}")
    print(f"  n_total_points       = {results['n_total_points']}")
    print(f"  CC1 rel dev vs 2.42e5 = {results['cc1_rel_dev']*100:.4f}%  -> {'PASS' if results['cc1_pass'] else 'FAIL'}")
    print(f"  L_max (npz actual)   = {results['L_max_actual']}  [plan-stated: {results['L_max_plan']}]")
    print(f"  tau-grid step actual = {results['tau_step_actual']:.6f}  "
          f"[plan-stated: 0.005]")
    print()

    # 4. Evaluate gate
    verdict = evaluate_gate(results)
    value = results["value"]                                # (local)

    # 5. 4-tuple + artifacts
    tag = (f"(value={value!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")      # (local)
    print(tag)
    write_npz(results, audit_sha, content_sha)
    write_plot(results)
    write_registry_patch(results, audit_sha, content_sha)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                 # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # per math-scripts.md: exit 0 for any scientific verdict


if __name__ == "__main__":
    sys.exit(main())
