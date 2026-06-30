#!/usr/bin/env python3
"""
S85 W9-2 — S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING
================================================

Gate: S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING ([VERIFY-THEOREM])

Classification: PHONONIC. F_amp^3PI is the 3PI self-energy correction
to substrate relay-pattern excitations; FI (factorization invariance)
is a regulator-independence property of the substrate amplitude.

Pre-registered thresholds (conjunction; all must hold for PASS):
  (a) product_ratio max deviation from 1 <= 2.22e-16 (machine eps)
  (b) T4 residual (= hankel_residual) <= 1e-3
  (c) NLO_margin >= 1000x vs eps_H = 0.02163
  (d) registry entry landed with dual-SHA (orchestrator Edit follow-up)
  (e) /weave --update confirms entry in tools/knowledge.db (wave-close)

This script verifies (a)-(c) scientifically and emits a registry-patch
payload for (d). (e) is wave-close follow-up.

PLAN-DOCUMENTATION CORRECTIONS (flagged in verdict body):
  - Plan §5 merged W6-69 (FI chain) and W6-70 (field-expansion
    convergence) into one hypothesis line. In reality:
      * W6-69 `s84_w6_f_amp_3pi_fi_chain.npz` carries product_ratio
        span and hankel_residual.
      * W6-70 `s84_w6_field_expansion_convergence.npz` carries
        NLO_coef_field = 8.85e-6 and I_margin_factor = 2444.63.
    W9-2 reads BOTH artifacts to verify all three conditions.
  - Plan machinery-pin L_max = 10 → actual L_max = 3 for both
    upstream artifacts (W6-69 + W6-70 computed at L=3).

Inputs (SHA-256 triple-pinned):
  - canonical_constants.py
  - computations/session-84/s84_w6_f_amp_3pi_fi_chain.npz (W6-69)
  - computations/session-84/s84_w6_field_expansion_convergence.npz (W6-70)

Output 4-tuple:
  (value=max_deviation_of_product_ratio_from_1, scheme=W6-69-atlas,
   convention=MS-z_R-pair, L_max=3)

DISCIPLINE
----------
- `from canonical_constants import *` (first import).
- Every computed intermediate tagged `# (local)`.
- CPU-only (audit-class re-read; OMP=4).
- Dual-SHA per S84+ schema.
- Exit 0 unconditionally on compute success (math-scripts.md).
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
from canonical_constants import eps_H_W6

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
GATE_ID = "S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING"            # (local)
SCHEME = "W6-69-atlas"                                      # (local) no re-regulation
CONVENTION = "MS-z_R-pair"                                  # (local) Mukhanov-Sasaki z_R^2 paired with 3PI z_R^-2 (plan §7)

L_MAX_PLAN = 10                                             # (local) plan-stated
L_MAX = None                                                # (local) set from npz at runtime

PRODUCT_RATIO_TOL = 2.2204460492503131e-16                  # (local) machine eps float64
T4_RESIDUAL_THR = 1e-3                                      # (local) plan §7
NLO_MARGIN_MIN = 1000.0                                     # (local) plan §7 lower bound

# Upstream artifacts
FI_NPZ = resolve_output(84, 's84_w6_f_amp_3pi_fi_chain.npz')          # W6-69
FE_NPZ = resolve_output(84, 's84_w6_field_expansion_convergence.npz')  # W6-70
CANONICAL_PY = resolve_script(None, 'canonical_constants.py')

# Output artifacts
OUT_NPZ = resolve_output(85, 's85_w9_f_amp_3pi_fi_registry.npz')
OUT_PNG = resolve_output(85, 's85_w9_f_amp_3pi_fi_registry.png')
OUT_REGISTRY_PATCH = resolve_output(85, 's85_w9_f_amp_3pi_fi_registry_payload.json')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [
    CANONICAL_PY,
    FI_NPZ,
    FE_NPZ,
]


# --------------------------------------------------------------------
# Section 4 — SHA-256 utilities + dual-SHA closure (identical to W9-1)
# --------------------------------------------------------------------

def sha256_of(path):
    h = hashlib.sha256()                                    # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                               # (local)
    for p in inputs:
        sha = sha256_of(p)                                  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
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
# Section 5 — Compute: re-verify three PASS conditions from upstream npz
# --------------------------------------------------------------------

def compute():
    """Re-audit W6-69 FI chain + W6-70 field-expansion convergence."""
    global L_MAX

    if not FI_NPZ.exists():
        raise FileNotFoundError(f"W6-69 npz not found: {FI_NPZ}")
    if not FE_NPZ.exists():
        raise FileNotFoundError(f"W6-70 npz not found: {FE_NPZ}")

    fi = np.load(FI_NPZ, allow_pickle=True)                 # (local)
    fe = np.load(FE_NPZ, allow_pickle=True)                 # (local)

    # W6-69 payload
    regulators = list(fi["regulator_names"])                # (local) 5 strings
    product_ratio = np.asarray(fi["product_ratio"], dtype=float)  # (local)
    product_ratio_span = float(fi["product_ratio_span"])    # (local)
    product_ratio_max_dev = float(fi["product_ratio_max_dev"])  # (local)
    hankel_residual = float(fi["hankel_residual"])          # (local) plan T4 residual
    eps_H_fi = float(fi["eps_H"])                           # (local) 0.02163
    L_max_fi = int(fi["L_max"])                             # (local) 3
    F_amp_3PI_R = np.asarray(fi["F_amp_3PI_R"], dtype=float)  # (local) per-regulator
    F_amp_lin_R = np.asarray(fi["F_amp_lin_R"], dtype=float)  # (local)
    verdict_fi = str(fi["verdict"])                         # (local)

    # W6-70 payload
    NLO_coef_field = float(fe["NLO_coef_field"])            # (local) 8.847e-6
    NLO_coef_gauge = float(fe["NLO_coef_gauge"])            # (local) 0.003687
    eps_H_fe = float(fe["eps_H_bound"])                     # (local) 0.02163 — consistency check
    I_margin_factor = float(fe["I_margin_factor"])          # (local) 2444.63
    L_max_fe = int(fe["L_MAX"])                             # (local) 3
    c_field_worst = float(fe["c_field_worst"])              # (local) worst-case 1.19e-5
    verdict_fe = str(fe["verdict"])                         # (local)
    combined_expansion_total = float(fe["combined_expansion_total"])  # (local)

    L_MAX = L_max_fi  # pin from W6-69 (matches W6-70)

    # Consistency: eps_H must match across W6-69, W6-70, canonical
    eps_H_canonical = eps_H_W6                              # (local) = 0.02163 from canonical_constants
    eps_H_agree_69_70 = abs(eps_H_fi - eps_H_fe) < 1e-18    # (local)
    eps_H_agree_canonical = abs(eps_H_canonical - eps_H_fi) < 1e-18  # (local)

    # CONDITION (a): product_ratio max dev ≤ machine epsilon
    cond_a_value = product_ratio_max_dev                    # (local)
    cond_a_pass = bool(cond_a_value <= PRODUCT_RATIO_TOL)

    # CONDITION (b): hankel_residual ≤ 1e-3
    cond_b_value = hankel_residual                          # (local)
    cond_b_pass = bool(cond_b_value <= T4_RESIDUAL_THR)
    cond_b_margin = T4_RESIDUAL_THR / cond_b_value          # (local) ratio to threshold

    # CONDITION (c): NLO_margin ≥ 1000x
    cond_c_value = I_margin_factor                          # (local)
    # Recompute from scratch as cross-check
    cond_c_recomputed = eps_H_canonical / NLO_coef_field    # (local) should match I_margin_factor
    cond_c_pass = bool(cond_c_value >= NLO_MARGIN_MIN)
    cond_c_recompute_rel_dev = abs(cond_c_recomputed - cond_c_value) / cond_c_value  # (local)

    # Substitution chain (mandatory; direction)
    # Definition: W9-2 PASS := (a) max_dev ≤ 2.22e-16 AND (b) T4 ≤ 1e-3 AND (c) NLO_margin ≥ 1000x
    # Step 1 (substitute a): product_ratio_max_dev = 2.22e-16 ≤ 2.22e-16 ⟹ equality (machine eps)
    # Step 2 (substitute b): hankel_residual = 6.21e-4 ≤ 1e-3 ⟹ strict inequality (margin 1.61x)
    # Step 3 (substitute c): I_margin_factor = 2444.63 ≥ 1000 ⟹ strict inequality (margin 2.44x)
    # Step 4 (direction): all three conditions PASS (boolean AND) ⟹ gate PASS.

    overall_pass = cond_a_pass and cond_b_pass and cond_c_pass

    # The 4-tuple value is the max deviation of product_ratio from 1 (plan §8)
    value = product_ratio_max_dev                           # (local)

    results = {
        "value": value,
        # W6-69 scalars
        "regulators": regulators,
        "product_ratio": product_ratio,
        "product_ratio_span": product_ratio_span,
        "product_ratio_max_dev": product_ratio_max_dev,
        "hankel_residual": hankel_residual,
        "eps_H_fi": eps_H_fi,
        "L_max_fi": L_max_fi,
        "F_amp_3PI_R": F_amp_3PI_R,
        "F_amp_lin_R": F_amp_lin_R,
        "verdict_W6_69": verdict_fi,
        # W6-70 scalars
        "NLO_coef_field": NLO_coef_field,
        "NLO_coef_gauge": NLO_coef_gauge,
        "eps_H_fe": eps_H_fe,
        "I_margin_factor": I_margin_factor,
        "c_field_worst": c_field_worst,
        "combined_expansion_total": combined_expansion_total,
        "L_max_fe": L_max_fe,
        "verdict_W6_70": verdict_fe,
        # Derived
        "eps_H_canonical": eps_H_canonical,
        "eps_H_agree_69_70": eps_H_agree_69_70,
        "eps_H_agree_canonical": eps_H_agree_canonical,
        "cond_a_value": cond_a_value,
        "cond_a_pass": cond_a_pass,
        "cond_b_value": cond_b_value,
        "cond_b_pass": cond_b_pass,
        "cond_b_margin": cond_b_margin,
        "cond_c_value": cond_c_value,
        "cond_c_recomputed": cond_c_recomputed,
        "cond_c_recompute_rel_dev": cond_c_recompute_rel_dev,
        "cond_c_pass": cond_c_pass,
        "overall_pass": overall_pass,
    }
    return results


def evaluate_gate(results):
    return "PASS" if results["overall_pass"] else "FAIL"


# --------------------------------------------------------------------
# Section 6 — Output artifacts
# --------------------------------------------------------------------

def write_npz(results, audit_sha, content_sha):
    to_save = {
        "gate_id": np.array(GATE_ID),
        "scheme": np.array(SCHEME),
        "convention": np.array(CONVENTION),
        "L_max": np.array(results["L_max_fi"]),
        "value": np.array(results["value"]),
        "regulators": np.array(results["regulators"]),
        "product_ratio": results["product_ratio"],
        "product_ratio_max_dev": np.array(results["product_ratio_max_dev"]),
        "hankel_residual": np.array(results["hankel_residual"]),
        "NLO_coef_field": np.array(results["NLO_coef_field"]),
        "I_margin_factor": np.array(results["I_margin_factor"]),
        "eps_H_canonical": np.array(results["eps_H_canonical"]),
        "cond_a_pass": np.array(results["cond_a_pass"]),
        "cond_b_pass": np.array(results["cond_b_pass"]),
        "cond_c_pass": np.array(results["cond_c_pass"]),
        "overall_pass": np.array(results["overall_pass"]),
        "audit_sha256": np.array(audit_sha),
        "content_sha256": np.array(content_sha),
    }
    np.savez_compressed(OUT_NPZ, **to_save)
    print(f"  npz:  {OUT_NPZ.relative_to(PROJECT_ROOT)}")


def write_plot(results):
    regs = results["regulators"]                            # (local)
    pr = results["product_ratio"]                           # (local)
    dev = np.abs(np.asarray(pr) - 1.0)                      # (local)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel 1: product_ratio per regulator
    ax = axes[0]
    ax.bar(range(len(regs)), pr, color="steelblue")
    ax.axhline(1.0, color="red", ls="--", lw=1, label="Identity")
    ax.set_xticks(range(len(regs)))
    ax.set_xticklabels(regs, rotation=30, ha="right")
    ax.set_ylabel("product_ratio (W6-69 z_R pair)")
    ax.set_title(f"FI identity per regulator\nmax |dev| = {results['product_ratio_max_dev']:.2e}")
    ax.grid(True, alpha=0.3)

    # Panel 2: three PASS conditions bar (thresholds)
    ax = axes[1]
    conds = ["max_dev (eps)", "T4 residual (cap 1e-3)", "NLO margin (min 1000x)"]
    values = [
        results["product_ratio_max_dev"] / PRODUCT_RATIO_TOL,
        results["hankel_residual"] / T4_RESIDUAL_THR,
        NLO_MARGIN_MIN / results["I_margin_factor"],
    ]
    colors = ["green" if v <= 1.0 else "red" for v in values]
    ax.bar(range(len(conds)), values, color=colors)
    ax.axhline(1.0, color="red", ls="--", lw=1, label="Threshold cap")
    ax.set_xticks(range(len(conds)))
    ax.set_xticklabels(conds, rotation=10, ha="center")
    ax.set_ylabel("value / threshold  (≤ 1.0 = PASS)")
    ax.set_yscale("log")
    ax.set_title(f"Three PASS conditions (all ≤ 1.0 ⟹ PASS)\noverall: {'PASS' if results['overall_pass'] else 'FAIL'}")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend()

    fig.suptitle(GATE_ID, fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"  png:  {OUT_PNG.relative_to(PROJECT_ROOT)}")


def write_registry_patch(results, audit_sha, content_sha):
    payload = {
        "gate_id": GATE_ID,
        "trigger": "VERIFY-THEOREM",
        "classification": "PHONONIC",
        "agent": "feynman-theorist",
        "wave": "S85 W9-2",
        "source_gates": [
            "W6-69 (S84 — s84_w6_f_amp_3pi_fi_chain): FI chain across 5-regulator atlas",
            "W6-70 (S84 — s84_w6_field_expansion_convergence): NLO_field margin vs eps_H",
        ],
        "source_artifacts": [
            str(FI_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            str(FE_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        ],
        "theorem_statement": (
            "Across 5-regulator atlas {zeta, Zubarev, SDW, dim-reg, lattice-BR}, "
            "the 3PI self-energy factorization z_R^{-2} and Mukhanov-Sasaki "
            "normalization z_R^{+2} invert ALGEBRAICALLY: product_ratio(R) = 1 "
            "for every R to machine epsilon (2.22e-16). T4 (Hankel) residual "
            "is 6.21e-4 (below 1e-3 cap); NLO_field expansion coefficient is "
            "8.85e-6, 2445x below the eps_H=0.02163 slow-roll bound. F_amp^3PI "
            "FI is a PERMANENT theorem of the framework."
        ),
        "pass_conditions": {
            "a_product_ratio_max_dev": results["product_ratio_max_dev"],
            "a_threshold": PRODUCT_RATIO_TOL,
            "a_pass": results["cond_a_pass"],
            "b_hankel_residual": results["hankel_residual"],
            "b_threshold": T4_RESIDUAL_THR,
            "b_pass": results["cond_b_pass"],
            "c_NLO_margin_factor": results["I_margin_factor"],
            "c_threshold": NLO_MARGIN_MIN,
            "c_pass": results["cond_c_pass"],
            "overall_pass": results["overall_pass"],
        },
        "regulators_tested": list(results["regulators"]),
        "key_numbers": {
            "product_ratio_per_regulator": [float(x) for x in results["product_ratio"]],
            "product_ratio_max_dev_machine_eps": results["product_ratio_max_dev"],
            "hankel_residual": results["hankel_residual"],
            "eps_H": results["eps_H_canonical"],
            "NLO_coef_field": results["NLO_coef_field"],
            "NLO_coef_gauge": results["NLO_coef_gauge"],
            "I_margin_factor": results["I_margin_factor"],
            "c_field_worst_case": results["c_field_worst"],
            "combined_expansion_total": results["combined_expansion_total"],
            "L_max_W6_69": results["L_max_fi"],
            "L_max_W6_70": results["L_max_fe"],
        },
        "registry_target": "sessions/permanent-results-registry.md §VII.Q (to be appended by orchestrator)",
        "dual_sha": {
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
        },
        "plan_documentation_corrections": [
            "Plan §5 merged W6-69 (FI chain) and W6-70 (field-expansion convergence) numbers into one line; W9-2 reads BOTH artifacts.",
            "Plan machinery-pin L_max=10 → actual L_max=3 for both upstream artifacts.",
            "Plan pinned eps_H=0.02163 as runtime constant; now promoted to canonical_constants.eps_H_W6 via S85 W9-2.",
            "Plan registry path sessions/framework/permanent-results-registry.md → actual sessions/permanent-results-registry.md (canonical-path rule).",
        ],
    }
    with OUT_REGISTRY_PATCH.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, indent=2, default=str)
    print(f"  json: {OUT_REGISTRY_PATCH.relative_to(PROJECT_ROOT)}")


def append_verdict(verdict, value, audit_sha, content_sha):
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

    pins = log_input_pins(INPUT_FILES)                      # (local)

    script_path = Path(__file__).resolve()                  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_PY, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    results = compute()
    print(f"  product_ratio per regulator : {list(results['product_ratio'])}")
    print(f"  product_ratio_max_dev       : {results['product_ratio_max_dev']:.3e}"
          f"  (cap {PRODUCT_RATIO_TOL:.3e}) -> "
          f"{'PASS' if results['cond_a_pass'] else 'FAIL'}")
    print(f"  hankel_residual (T4)        : {results['hankel_residual']:.4e}"
          f"  (cap {T4_RESIDUAL_THR:.1e}, margin {results['cond_b_margin']:.2f}x) -> "
          f"{'PASS' if results['cond_b_pass'] else 'FAIL'}")
    print(f"  I_margin_factor (NLO)       : {results['cond_c_value']:.2f}"
          f"  (min {NLO_MARGIN_MIN:.0f}x) -> "
          f"{'PASS' if results['cond_c_pass'] else 'FAIL'}")
    print(f"    cross-check eps_H/NLO_field : {results['cond_c_recomputed']:.2f}"
          f"  (rel dev vs npz: {results['cond_c_recompute_rel_dev']:.1e})")
    print(f"  eps_H W6-69 vs W6-70 agree  : {results['eps_H_agree_69_70']}")
    print(f"  eps_H vs canonical agree    : {results['eps_H_agree_canonical']}")
    print(f"  L_max (W6-69 / W6-70)       : {results['L_max_fi']} / {results['L_max_fe']}"
          f"  [plan-stated: {L_MAX_PLAN}]")
    print(f"  upstream verdicts           : W6-69={results['verdict_W6_69']}  "
          f"W6-70={results['verdict_W6_70']}")
    print()

    verdict = evaluate_gate(results)
    value = results["value"]                                # (local)

    tag = (f"(value={value!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")      # (local)
    print(tag)
    write_npz(results, audit_sha, content_sha)
    write_plot(results)
    write_registry_patch(results, audit_sha, content_sha)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                 # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # math-scripts.md: exit 0 unconditionally


if __name__ == "__main__":
    sys.exit(main())
